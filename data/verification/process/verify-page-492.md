# Verification process log — verify-page-492


## [2026-09-14T03:08:43.242Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 492 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-492.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-492.json. Write /home/sfmqrb/git/rishe/data/verification/page-492.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 492` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:44.258Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:45.097Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:45.109Z] TOOL RESULT

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


## [2026-09-14T03:08:45.592Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-492.txt"
}
```


### [2026-09-14T03:08:45.634Z] TOOL RESULT

```
1	=== PDF page 492 (book page 462) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Swep, Sup 1 : to sleep  (refs POK:1048)
4	#1 (parent #0) [Avestan] refs=POK:1048; HRN:107; FFD:50 | xwap, xvap, xwaf : to sleep ; xvafna, xwafsa : sleep ; hufsa : to sleep
5	  #2 (parent #1) [Pahlavi] refs=FFD:50 | xwâb, xuft : sleep
6	  #3 (parent #1) [Sogdian] refs=SOD:173 | xwbn : dream ; `wbs : to sleep
7	    #4 (parent #2) [Persian] refs=BQT:746,760,780; HUB:56; MON:1431 | xâb «خواب ( خوابیدن )» : sleep, dream ; xoftan «خُفتن ( خُسبیدن ، خسپیدن )» : to sleep ; xoftak «خُفتَک ( خُفتو ، بَختَک )» : nightmare ; xafj «خَفج ( خَفجا )» : nightmare
8	#5 (parent #0) [Greek] refs=AHD | hupnos : sleep
9	  #6 (parent #5) [French] refs=None | 
10	    #7 (parent #6) [Persian] refs=AMD:1985 | hîpnotîsm «هیپنوتیسم» : hypnotism
11	  #8 (parent #5) [English] refs=AHD | hypnotism
12	--- entry 1 ---
13	ROOT [Indo-European] Swer : to press, cut, hurt  (refs POK:1050; IEC:1348)
14	#1 (parent #0) [Avestan] refs=POK:1050; KLN:1554 | xvara : thorn, to pierce
15	  #2 (parent #1) [Persian] refs=HRN:109; BQT:766; DMO:110 | xalîdan «خلیدن» : to pierce, dip in water ; xaleh «خَله» : thorn, also an oar ; xale-bân «خلبان» : pilot, originally one who rows a boat
16	#3 (parent #0) [Avestan] refs=IEC:1348 | xwarô : wound
17	  #4 (parent #3) [Persian] refs=IEC:1348 | xoreh «خوره» : gangrene, leprosy, corruption | NOTE: MON:1455 derives this from Persian "xordan: to eat". See Swel 1.
18	#5 (parent #0) [Germanic] refs=KLN:1554; AHD | swerdam : sword
19	  #6 (parent #5) [English] refs=None | sword
20	--- entry 2 ---
21	ROOT Swer -> redirect to Wer 6
22	--- entry 3 ---
23	ROOT Swe-sor -> redirect to Seu 1
24	
```


## [2026-09-14T03:08:49.021Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-492.json",
 "description": "Read source JSON for page 492"
}
```


### [2026-09-14T03:08:49.077Z] TOOL RESULT

```
{
  "pdf_page": 492,
  "book_page": 462,
  "entries": [
    {
      "root": {
        "name": "Swep, Sup 1",
        "lang": "Indo-European",
        "refs": "POK:1048",
        "gloss": "to sleep"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1048; HRN:107; FFD:50",
          "words": [
            {"translit": "xwap, xvap, xwaf", "gloss": "to sleep", "script": null},
            {"translit": "xvafna, xwafsa", "gloss": "sleep", "script": null},
            {"translit": "hufsa", "gloss": "to sleep", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FFD:50",
          "words": [
            {"translit": "xwâb, xuft", "gloss": "sleep", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:173",
          "words": [
            {"translit": "xwbn", "gloss": "dream", "script": null},
            {"translit": "`wbs", "gloss": "to sleep", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:746,760,780; HUB:56; MON:1431",
          "words": [
            {"translit": "xâb", "gloss": "sleep, dream", "script": "خواب ( خوابیدن )"},
            {"translit": "xoftan", "gloss": "to sleep", "script": "خُفتن ( خُسبیدن ، خسپیدن )"},
            {"translit": "xoftak", "gloss": "nightmare", "script": "خُفتَک ( خُفتو ، بَختَک )"},
            {"translit": "xafj", "gloss": "nightmare", "script": "خَفج ( خَفجا )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "hupnos", "gloss": "sleep", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "AMD:1985",
          "words": [
            {"translit": "hîpnotîsm", "gloss": "hypnotism", "script": "هیپنوتیسم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "hypnotism", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Swer",
        "lang": "Indo-European",
        "refs": "POK:1050; IEC:1348",
        "gloss": "to press, cut, hurt"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1050; KLN:1554",
          "words": [
            {"translit": "xvara", "gloss": "thorn, to pierce", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:109; BQT:766; DMO:110",
          "words": [
            {"translit": "xalîdan", "gloss": "to pierce, dip in water", "script": "خلیدن"},
            {"translit": "xaleh", "gloss": "thorn, also an oar", "script": "خَله"},
            {"translit": "xale-bân", "gloss": "pilot, originally one who rows a boat", "script": "خلبان"}
          ],
          "note": null,
          "quote": {"text": "خونی که گرفت گردنت را - خاری که خلید دامنت را", "poet": "Nezâmî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "IEC:1348",
          "words": [
            {"translit": "xwarô", "gloss": "wound", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "IEC:1348",
          "words": [
            {"translit": "xoreh", "gloss": "gangrene, leprosy, corruption", "script": "خوره"}
          ],
          "note": "MON:1455 derives this from Persian \"xordan: to eat\". See Swel 1.",
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:1554; AHD",
          "words": [
            {"translit": "swerdam", "gloss": "sword", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "sword", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Swer",
        "redirect": "Wer 6"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Swe-sor",
        "redirect": "Seu 1"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T03:08:49.859Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T03:08:49.917Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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
```


## [2026-09-14T03:08:54.271Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','FFD','SOD','BQT','HUB','MON','AHD','AMD','KLN','IEC','DMO']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:600])\n\""
}
```


## [2026-09-14T03:08:54.987Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -40 && echo --- && head -60 data/verification/page-385.json"
}
```


### [2026-09-14T03:08:55.206Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
== AMD {"title": "Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf", "lookup_hint": "Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Entry-level verification only."}
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
== DMO {"title": "Sa'id Nafisi, Dar Maktab-e Ostad, Zohreh 1344/1965", "kind": "website", "url": "https://www.ketabnak.com/book/55983 (283 pp. PDF, login)", "lookup_hint": "Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF page exists; not fetched."}
```


### [2026-09-14T03:08:55.263Z] TOOL RESULT

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
---
{
  "pdf_page": 385,
  "book_page": 355,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-07",
  "entries": [
    {
      "entry": 0,
      "root": "Peg",
      "verdict": "plausible",
      "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
      "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
      "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
      "sources": [
        "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
        "https://en.wiktionary.org/wiki/pectus"
      ],
      "ref_check": [
        {
          "ref": "POK:792",
          "status": "partial",
          "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
        }
      ],
      "consulted": [
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. peg-",
          "stance": "supports",
          "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
          "stance": "partial",
          "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
        },
        {
          "src": "IEC",
          "where": "Mann, alphabetical",
          "stance": "silent",
          "note": "grep of IEC.txt for 'peg-', 'pokso-', 'pektos' returns no headword for this root."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Sanskrit",
          "words": "pakša",
          "verdict": "plausible",
          "derivation": "Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; only the gloss 'breast' is wrong.",
          "derivation_fa": "واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست است و تنها معنای «سینه» نادرست است.",
          "sources": [
            "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7"
          ],
          "ref_check": [
            {
              "ref": "AHD",
              "status": "partial",
              "note": "Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'."
```


## [2026-09-14T03:09:12.018Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==(1048-344)' POK_02.txt | head -80",
 "description": "Pokorny p.1048"
}
```


### [2026-09-14T03:09:13.062Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:09:13.389Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sup-no\" POK_02.txt | head -20; echo ===; grep -n \"swep\" POK_full.txt | head -20",
 "description": "Grep Pokorny for swep"
}
```


### [2026-09-14T03:09:13.454Z] TOOL RESULT

```
Exit code 1
(eval):2: == not found
```


## [2026-09-14T03:09:18.543Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('../refs_online.json'))\nprint(d['POK']['page_offset'])\nprint(d['POK'].get('lookup_hint'))\n\"\nfor f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"-- $f\"; python3 -c \"\nimport sys\nt=open('$f',encoding='utf-8',errors='replace').read()\nprint(len(t.split(chr(12))))\n\"; done"
}
```


### [2026-09-14T03:09:19.781Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
-- POK_01.txt
364
-- POK_02.txt
434
-- POK_03.txt
430
-- POK_full.txt
1
```


## [2026-09-14T03:09:23.170Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"lemma: su̯ep\\|lemma: suep\\|lemma: su̯er\\|lemma: suer\" POK_full.txt | head -30"
}
```


### [2026-09-14T03:09:23.226Z] TOOL RESULT

```
73769:Root/ lemma: septrp {* seR"!!-) : seven derived from a mutated Root/ lemma: sueRs, seRs, 
83529:Root/ lemma: sueRs, seRs, RseRs, RsueRs, ueRs{\ uRs) {*ghe-ska) 
84037:Root / lemma: suep-1, sup- {* kuep-1) 
84043:Root/ lemma: suep-1, sup-: "to sleep, *cease, die' derived from Root/ lemma: suep-2, 
84086:Root / lemma: suep-2, sup-, sueb- 
84141:Root / lemma: suergh- {*g"hergh- : ksuergh-) 
84162:Root / lemma: suer-1 (also ser-?) 
84188:Root / lemma: suer-2 
84233:Root / lemma: suer-3 
84255:Root / lemma: suer-4 
84282:Root / lemma: suer-5
```


## [2026-09-14T03:09:24.279Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 282 283 284 285 286; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n{print substr($0,1,700)}' POK_03.txt; done"
}
```


### [2026-09-14T03:09:25.281Z] TOOL RESULT

```
=== leaf 282
ugga,  mnd.  sugge.
WP.  II  512  f.,  WH.  II  635  ff.,  Trautmann  294,  Vasmer  2,  593,  Benve»^' BSL  45,   74 f..    90,  Thieme,   Heimat   d.   idg.   Gemeinsprache  26  f.,  8^^
1039
^^bl  ursprüngl.  .Gebärerin',  zu  2.  seu- :  sü~  ^gebären'  (oben  S.  913 f.);  vgl. ^' -j.  herit  ^Sau'  (*bherenti) ]  oder  aber  lautnachahmend?
.^^  soU'TO-  ,sauer,  salzig,  bitter',  zunächst  von  käsig  Gerinnendem^ ■^     schleimig  Nassem;  auch  in  Flußnamen;  Wurzel  seu(a)-,  sou(a)-:sa-.
^isl.  surr  ,sauer,  scharf,  m.  , Sauerteig',  mnd.  mhd.  sür  n.  ,Bitterkeit'; ^1^  syra  f.  , saure  Milch',  ags.  syring  ds.,  ahd.  sürl  ßäure^-^  ahd.  ags.  sür taue
=== leaf 283
e,   aisl.
■^tr  ,süß';  gall.  PN  SuadurJx,  -genus,  ir.  Sadb  f.  PN;  über  got.  sutis  , ruhige
«anff,  s.  Mayrhofer  KZ  71,  74 f.  u.  73,  116 f.
Kompar.  Superl.  ai.  svddlyas-,  gr.  ijdlwv',  ai.  svädistha-  ==  gr.  fjöiCTog]
1040  •
2.  suädos-  n.  ^Süßigkeit,  Wohlgefallen' :  ved.  prd-svädas-  »Hebli^ nehmS  ^ehijdrjg  »honigsüß^  ^dog  n.  ,Essig'  (gr.  ^öog  n.  ,Vorteü',  bleibt  ^^
5.  suädonom,  -ä:  ai.  svädanam,  gr.  i^dovij  f.  ,Lust^
4.  Verba  und  andere  Nominalbildungen:
ai.  ved.  svädate  ,ist  erfreut,  genießt*  =  gr.  ^So^xai  (böot.  S&dofit)  t*^ mich';  ^
av.  x'^äs^ö  , durch  Kochen  gar  (schmackhaft)  gemacht, 
=== leaf 284
ent)  blasen^  chwyth  ,das  Blasen^ Ay^ytJiell  »Pfeife'  (chwib  ds.,  Kreuzung  von  chwyth  mit  pib  ,Pfeife'  aus t^l  pip^)i  corn.  lühythe,  whethe,  bret.  c'houeza  »blasen';  aksl.  svistatij  zviz- iflti  ;Sibiläre^  (kann  aus  *svizdati  assimil.  sein);
rr.  <y^^^  ,zische',  Aor.  eai^a  {ai^Lg,  aiyfxög  ,das  Zischen')  ist  ähnliche gchallbil<i^^&  wie  lett.  slkt  ds.;
ebenso  lat.  sibüöj  -äre  ,zischen,  pfeifen*,  slUlus  ,zischend;  das  Zischen', Igkundär  slfilöj  sißlus,  vgl.  schwundstuf.  got.  swiglön  ,die  Flöte  blasen, •feifenS  ahd.  sweglön  ds.,  swegala  ,Flöte*  (*suighlä-)j
j^  jhnhch,  aber  ohne  geschichtlichen  Zusammenhang  
=== leaf 285
taumeln',  mhd.  swlmen  ds. ;  ags.  swlma  m. ihwindel,  Ohnmacht*,  aisl.  svlmij  ndl.  zwijm  ds. ;  mhd.  swlmel,  swimmel tWindel';  aisl.  sveimr  m..  sveim  n.  , Getümmel,  Tumult',  sveima  ,um- siehen',  mhd.  sweim  m.  ,das  Schweben,  Schweifen,  Schwingen',  sweimen ih  schwingen,  schwanken';  norw.  svil  n.  , Spirale;  der  krause  Samen- itel  dorschartiger  Fische';  nd.  svnr  , Schwung,  Drehung,  Bummeln', ?*"««  ,sich  schwingend  bewegen,  umherfliegen,  in  Saus  und  Braus  leben*.
\*^eib~ :  av.  xsvaewayat-aHra-  .die  Peitsche  schwingend*,  xSviwra-  .flink' ; 'midja-sweipains  , Sintflut'  (eig.  ,Fegung  der  Mitte*);  aisl.  sveipa  , werfen,
66
1042  
=== leaf 286
änzen  beginnen*,  ,?»Ü% ,glänzen',  lett.  svist  ,anbrechen,  vom  Tage*,  svdidlt  ,salben'  (^Ig^^ machen*) ;
ein  ähnliches  *sueit-,  aber  in  der  Bed.  ,sengen,  brennen'  iiaTSii- ahd.  swldan  ,brennen';  dazu  wohl  als  Aoristpräs.  ahd.  8wedan*ßch^ verbrennen*  und  mit  Ablautentgleisung  ags.  swadul  ,Rauch*,  xolfd*  f^ ,RauchscÄM;a(ien,  Dunst*  u.  dgl.
WP.  II  520  f.,  WH.  II  534,  Trautmann  296.
1043
gVieid'  ^schwitzen';  sueides-  n.,  su{e)id-ro-,  suoido-  ,Schweiß^ ^i.  svidyatij  svidate  ,schwitzt*,  svida-  m.  =  av.  xvaeda- , Schweiß*  (=  germ.
^m-  l^ii^t-T^,  Gen.  -an  ,Schweiß^  {rt  aus  dr^  vgl.  gv.  \dqwg,  lett.  sviec^W); -y.  (5)
```


## [2026-09-14T03:09:28.967Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '84037,84145p' POK_full.txt"
}
```


### [2026-09-14T03:09:29.023Z] TOOL RESULT

```
Root / lemma: suep-1, sup- {* kuep-1) 

Meaning: to sleep, *cease, die 

Note: 

Root/ lemma: suep-1, sup-: "to sleep, *cease, die' derived from Root/ lemma: suep-2, 

sup-, sueb-\ "to throw, *sway, swing (put to sleep)'. 

Material: Old Indie svapiti, svapati^ asleep, dozed off. Pass, supyate, participle supta- 
"dozed off, Kaus. svapayati^scVAaiexi ein' (= Old Icelandic S0fa), svapayat/ds. (= Old 
Icelandic sve^'a etc.); Avestan x'ap- 's\eep'; gr. urrap "Wehrtraum'; 

Latin sop/o, -fre' put to sleep ', sopor, -or/s' deep sleep' {*suepd/); Old Icelandic sofa 
[svafj. Old English swefan siem V. "sleep, cease'; Kaus. Old Icelandic svefja^ put to sleep, 
stillen, besanftigen'. Old English swefian6s.. Old English swebban^ put to sleep, slay'. Old 
Saxon answebbian. Old High German antswebben. Middle High German entswebenAs., 
Middle High German also " sleepy become, fall asleep ' ( *suopeJd); Old Icelandic S0fa 
"slay' ( *sudpejd); Old Icelandic suaefa " put to sleep ' {*suepeid), syfja unpers. " make 
sleepy ', East Frisian suffen^ become sleepy ' (Dutch sur dizzy, stupid'); Old Icelandic 
sofnasdcwN. V. " fall asleep '; Middle High German swep, -it'es "sleep'. Old English sweofot 
n. ds.; Old Church Slavic s-tpati. Iter, sypa// "sleep', us-bngti^ fall asleep '; 

Old Indie si/4o/7a- "sleep, dream', Avestan x'afna-m. ds.; Armenian k'un. Gen. k'noy 
"sleep' {*suopnos); gr. uirvog "sleep' (= Old Church Slavic sbnb and:) alb. gjume, 

Latin somnus : Italian sonno : Portuguese sono : Bolognese sann : Romagnolo : soni : 
Valencian son : Romanian somn : Sardinian Campidanesu sonnu : Sicilian sonnu : 
Swedish somnen : Spanish sueho : French sommeil : Calabrese suonnu : Zeneize seunno 
: Napulitano suonno : Greek unvoi; : Albanian gjume : Old Irish suan, cymr. corn. bret. hun 
"sleep' : Armenian k'un: Hittite sup- (Medium), suppar//a- 's\eep'. 



Latin somnus ' s\eep' {*suepnos or *suopnos); Old Irish suan, cymr. corn. bret. hun's\eep' 
{*sopnos= Lithuanian sapnas); Old Icelandic svefn. Old English swefn^s\eep, dream', 
(from *suepn6s)\ Lithuanian sapnas, sapnys^6ream', Latvian 5a/0/7/s "dream'; Old Church 
Slavic sbnb "sleep, dream'; compare Old Indie asvapna-^sc\r\\ai\os', Avestan ax'afna-ds., 
Latin insomnis, gr. aunvoq ds. and die/io-derivative Old Indie svapnyam' dream ', Latin 
so/77/7/^/77 "dream', zem. sayO/7/5 "sleep, dream'. Old Church Slavic sbn/je^ dream '; gr. 
evunviov (replicated Latin insomnium) ds., cymr. 5/7/7^/7eofa' "insomnia'; Tocharian A spa", 
B Sy05/7e "sleep, dream'; Hittite sup- (Medium), supparlia-^s\eep\ 

Maybe Breton hurt: Welsh hun: Estonian uni: Finnish ^A7/"sleep'. 

References: WP. II 523 f., WH. II 557 f., Trautmann 292 f., Vasmer 2, 694. 
Page(s): 1048-1049 

Root / lemma: suep-2, sup-, sueb- 

Meaning: to throw, *sway, swing 

Material: Old Indie svapu^ besom '; Old Church Slavic 5i/e'/0///s^"agitari'; zero grade sbpg, 

s^//"schutten, strew, distribute'. Iter. SK/05//"schutten', /■asK/05//"ausstreuen'; sungti 

"effundere', Sb/Ob"heap' (but Lithuanian si//0//" swing, wiegen' rather to 5e:/-"bend'); Latin 

supo, -aAe "throw', dissipo, -a/'e"auseinanderwerfen, scatter', obsipo, -are 

"entgegensprengen (water), reproach', //7s/pe/'e"hineinwerfen'; 

Germanic *svab- and *svap- (Indo Germanic *sueb-) in Old Icelandic 5d/7"Kehrbesen' 
{*swdbala-), svafn. "spear, javelin'; Old English ge-swopei. "offal, rubbish' (isl. sopa^ 
sweep, wash away ' is engl. loanword); Low German swabbe/n \irom water ) hin- and 
herschlagen, wogen'. Modern High German schwapp-en, -ein, -ern 

References: WP. II 524, WH. I 356 ff., Trautmann 293, Vasmer 3, 57. 
Page(s): 1 049 

Root/ lemma: sue/b^-{a\so suer-7) 

Meaning: to turn; to sweep 

Material: Cymr. c/7M/e/7^"das Wirbein, Umdrehen', cbwerfan'\Nh\r\ior a spindle'; chwyrn 

"quick, fast (drehend)' from *sueib^-nio-; Gothic af-, bi-swafrban "abwischen'. Old Icelandic 

sverfasiem V. "feilen', svarfu. "Abfall beim Feilen', Old English sweorfan ds., afr. swerva' 

grovel, truckle, creep ', Old Saxon SM/e/'i&5/7 "abwischen'. Old High German suuerban 

"extergere', suuarp, swv/'M"gurges, vortex'. Middle High German swerben^s\ch wirbeind 



bewegen'; Old Icelandic si/a/:'&"umherschweifen', Old Swedish svarva'turn, work a lathe, 
(Lijgen) ersinnen'; 

Slavic *svorbh in Church Slavic svrabh (in addition Old Church Slavic svrabbiTb 
"Kvr|a|j(jb5r|<;'); ablaut. Slavic *svbrbit-b, *svbrbeti^\\.c\\' in russ. sverbft, sverbetb etc.; 
compare Latvian svarpstvn. "borer' {*suarb-sta-)\ 

perhaps in addition gr. aupcpoq n., aupcpsToq m. 'rubbish', aupcpa^, -qkoc; ' anything 
swept together, sweepings, refuse, rubbish, litter'; compare also aaipu) 'sweep' {*suerid), 
aapov n., aapoc; m. ' besom, rubbish' and aupw (Fut. aupw) 'pull, drag, sweep, wash', 
a\J^\^6c, m. ' any lengthened sweeping motion, the moving, vomiting ', auppaia f. ' emetic, 
vomiting, purge-plant ', auppa n. ' anything trailed or dragged, towing dress, rubbish', 
aupTr|<; m. ' towing rope ', aupiK;, -i5o(;f. 'sandbank'. 

References: WP. II 529 f., Trautmann 295, Vasmer 2, 589, 596 f. 
Page(s): 1050-1051 

Root / lemma: suergh- {*g"hergh- : ksuergh-) 

Meaning: to take care of; to be ill 

Material: 1 . Old Indie sJA/rsa// "kiimmert sich um etwas'; common Old Indie -g"h- > -ksu-
```


## [2026-09-14T03:09:29.596Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '84162,84300p' POK_full.txt"
}
```


### [2026-09-14T03:09:29.672Z] TOOL RESULT

```
Root / lemma: suer-1 (also ser-?) 

Meaning: to speak 

Material: Latin sermo, -o/7/s'Wechselrede, conversation, entertainment, conversation ' 

{*sermd) is unclear; 

Maybe alb. {*sermd) th/rmen. f. 'shout, call' [common alb. s>thsh\it] 



Oscan sverruner 6evc\ Sprecher, WortfiJhrer'; Gothic swaran, swdr's\Near, vow', Old 
Icelandic sveria. Old English Old Saxon swerian. Old High German swerien, swerren6s.. 
Old Icelandic 50/7' Norn. PI. 'vow, pledge, oath'. Middle High German swuor\o\N, pledge'. 
Old Icelandic SKa^a'anworten, BiJrgschaft leisten', svgrP\. 'Antwort', 5/7o'-si/5/'"gerichtliche 
verdict ', Old English and-swaru ^ Antwort' , Old Saxon 5/7/-SM/d/' "Antwort, Verantwortung'; 
Old Church Slavic svarb "quarrel' (Hin- and Widerrede), svan, "fight, struggle', svariti 
"vilify, scold, fight, struggle'; russ. ssdAS "quarrel' from *s-bsoral 

*suer- "speak, talk' is perhaps (but not certainly) the use from suer- hum, whiz ' auf 
artikuliertes of speech. 

References: WP. II 527, WH. II 521 f., Trautmann 296 f., Vasmer 2, 712. 
Page(s): 1 049 

Root / lemma: suer-2 

Meaning: to hiss 

Material: Old Indie svarati^ sounds, erschallt, allows erschallen'; also si//7777"duct, tube, 

pipe' (flute?); svara- svara-xx\. " clangor, sound, tone'; 

upa^, -Koc, m. "Spitzmaus' ( *surak-), Cretan upov "swarm of bees' Hes.; 

Maybe alb. Geg {*sur/x) urith, tosk {*sam-uridh) hamuridhe^ mole ' 

Latin susurrus^ a humming, murmuring, muttering, whispering ', susurro, -are "hiss, 
whisper, buzz' (/^consonant increase in onomatopoeic words), absurdus^ adverse 
clinking, ungereimt' ( *suorodo-s)\ surdus'6eaV as "dull or inarticulate horend and 
redend'?); 

Maybe alb. shushurin, feshferin^ rustle ' : Breton sarac'hat: Galician susurrarkom Latin 
susurrus' a humming, murmuring, muttering, whispering '. 

Maybe alb shurdh^ deaf ' : French sourd : Napulitano surdo : Romagnolo surd : from Latin 
surdus "deaf. 

While Basque gor ; entzungor : Finnish kuuro : Turkish sagir : Hungarian siJket "deaf. 

Latin probably sorex, -ids (previously late sorex) " shrew, small mouselike mammal with a 
long snout ' from *sudr-ak-{: gr. upa^ ds.); cymr. chwyrnu^drone, grumble' (to *chwyrn 
from * suernjol); 



Old Icelandic svarra 'roar', Norwegian si/e/ra "whirl; kreisen', Modern High German 
schwirren; Norwegian surla'\e\se sing', Swedish soria' trickle, mumble, murmur'. Middle 
Low German Modern High German surren. Middle High German 5i//777"Gesumse'; 
vielleichtisl. svarmr' dizziness ', Old English swearm' swarm, bulk, mass'. Old High 
German swarm " swarm '; 

Lithuanian s^/777a 'flute', Old Church Slavic SK/Aa// "whistle' (lengthening from *svbr-), 

Maybe alb. (^ surma) zhurma' noise'. 

References: WP. II 527 f., WH. II 634 f., 637 f., Vasmer 2, 593. 
See also: s. also s^er- "speak'. 
Page(s): 1049-1050 

Root / lemma: suer-3 

Meaning: stake 

Material: Old Indie svaru-rx\. "picket, pole, Doppelpfosten, long bit of wood'; gr. sppa n. 

"pad'; homer. Akk. sppTva m. "Bettpfosten'; Old High German stv//'(9/7"bepfahlen'. Middle 

High German 5by//'"Uferpfahr, Modern High German Swiss Sc/7by//'e/7 "picket, pole'. Old 

English swier, swiorrr\. f. " jamb, column '; with /r-forms Old Icelandic svTriru. " neck, prow, 

bow of a ship' {*swerhjan-). Old English swTera, swTora " neck ' ( *swirhjan-)\ Latin zero 

grade surus'img, branch, picket, pole', Demin. surculus, surcellus, perhaps sura'caM, 

Wadenbein' (see below *sdra). 

References: WP. II 528 f., WH. II 635. 

Page(s): 1 050 

Root / lemma: suer-4 

Meaning: to cut, pierce 

Material: Avestan x'ara-r^. "wound, Verwundung'; 

Maybe alb. Geg {*svarna) varre' wound'. 

Old Irish serb, cymr. chwerw^bWief {*suer-uo), originally probably " burning, pricking '; 
cymr. chwarreni. 'gland' {*suorsina)\ 

Old High German sweran s\.err\ V. "ache, fester, swell', SM/e/'c»"leiblicher pain, esp. 
ulcer'. Modern High German Schware, Geschwur 'ulcer'. Old High German swer(a)do 
"leiblicher pain'. Old English sweornian 'curdle, coagulate, harden '; Old High German 
SM/e/t"Schwert', Old English sweord. Old Icelandic sverdirorr\ *swer-da- "stechende 
weapon'; 



proto Slavic. *syara- 'krankWcW in russ. chvoryj, Old Czech chvory, ablaut, churavy ds. 
and Church Slavic chyra' fragileness '; perhaps here serb. -Church Slavic svrbdb/b^ borer', 
proto Slavic. *svbrdblo. 

References: WP. II 529, Trautmann 295, Krogmann KZ. 59, 204, Vasnner2, 589, 3, 237, 
243, Loth RC. 41,233. 
Page(s): 1 050 

Root / lemma: suer-5 
Meaning: " scale, weigh ' 
See also: see below uer-1. 
Page(s): 1 050 

Root/ lemma: suesor-{*suestor) 

Meaning: sister 

Note: 

Root/ lemma: suesor-{* suestoi): sister' derived from Root/ lemma: se-\ "reflexive 

pronoun, *own' + common lllyrian -tar, -/o/'suffix; it was modelled after Root/ lemma: 

pate(r)Qer\. patr-es, -ds: father', Root/ lemma: mater-: mother'. Root/ lemma: b'^rater-: 

"brother'
```


## [2026-09-14T03:09:41.982Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('../refs_online.json'))\nfor k in ['KLN','IEC','BRT','PHD','SOD','BQT','HUB','FFD']:\n    print(k, d[k].get('page_offset'))\n    print('  hint:', str(d[k].get('lookup_hint'))[:300])\n\""
}
```


## [2026-09-14T03:09:42.872Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- BRT xvara\"; grep -n \"x\\^ara\\|xvara\\|x'ara\" BRT.txt | head -30"
}
```


### [2026-09-14T03:09:43.086Z] TOOL RESULT

```
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
BRT Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
PHD leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
SOD printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
  hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
  hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
HUB leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
FFD 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
  hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
```


### [2026-09-14T03:09:43.134Z] TOOL RESULT

```
--- BRT xvara
4389:•  j.  ana.x'arad'a-  Adj.  'ohne  Speise,  Nah- rung'; yal  at)hat  aitihä  zmiö  vi.äpö.- ttnumca  (sd.)  vi.urvarSi3minKa  ''^a  (ND.) ^pasu  vira  "wo  es  . ,  am  meisten  . .  man- gelt —  '>Tiere  und  Menschen  finden  keine Nahrung  — "  V. /o.  18.
6973:•  j,  a-x^arant-  Adj.  'nichtessend' :  nazcis 'r^iitam  tva  ns'it . .  asayam  (sd.)  . .  V.  j.33,
6975:•  j,  a-x^arata-  Adj.  'unfassbar,  unnahbar', vom  i^ar>nah-  (sd.):  tr/rpin  °tPin  d'annö mazdaiätfm  .  .  yahmi  paiti  ''parix''äi>e (sd.)  sp>ntasca  mainyui  anrasca  aäahmi paiti  at  'te  Y.%.  ig.  A,li.;  —  atari  .  .  uiti . .  mankanö  a3at  si'ar^nB  hangpr»/s3ne  yal 'fymYt.iff.4j;  — <'^I  vS  kascit  malyänqm id'artttS  "tsm  isaSta  Yt. /p.  53;  —  käva- yeheca  x''armar>hu  .  .  'taheca  ^farftta^hs mazd^ätahe  Y.  j.  14;  S.  i.  25,  Y.  2. 14,
7210:•  j,  a-x^arant-  Adj.  'nichtessend':  naiUs •nntam  tva  fidii  ..  asayam(sd.)  ..V.^.^y
9439:y  "^  •  j.    ka-x*araoa-   m.,   -x'araioi-  f.   Be-
9449:ii:jr-<j  frakavB  .  .  ml  'vis  (NS.)  mä  -braune  Teufel'.  —  .)  Zs.  15.  1  macbt  das Z'izbärii  V.2. 29.  a)  als  Dal!'a  perso-'  Wort  lum  EN.  —  3)  Vgl.  zu  kaxuii-. nifizirt:  -i-U  d„ni  p^llitl  äati'ü  .  .  V. ! .  ,  kax'arajainya-  Adj.  (fem.  -w-)  'üir J5.43.  2)  Adj.,  von  dem  damit  be- 1 ^toe  der  &A«oo  (sd.)  gehörig':  jM hafteten:  ml  m  alujä  mo^rays /rania- 1^,„„„„„-  .  y^^,  .5^,-,„  yt.  1. 9,  12,  i6'. r>ntlt   *t»3  *'vW^   (NS.)   Yt5.  92.  Ableit.  aus  kaiFartla..
13806:•  g.  duS-x^araS^-  n,  'üble  Speise"*; dar>gim  äyü  (sd.)  timanks  *°'i3m  ''. .  üble Speise"  Y.31.  20;  —  vaya.b?r?dubyB  (sd.) '%Sm  Y.5;.  6.
17987:♦)   Im    Gegensati    lu   andui-  und    lu  x^ara- (sd.),   sowie    lu   raiia-  (ad.).    Vgl.  auch   Bthl.
20050:(sd.)  mZ  'yü  x'ara^  vastnm  gave  V.j.20; — yaoeda  (sd.)  °yai  *aipT.wq%3m  ..gavöi .. Y.4S.$i  —  pasvasla  staoraüa  .  .  'yaca bizifigra  Ytf.  89;  —  pasvqmla  siaora- namm  'yanqmca  sünqmca  vttyqmca  V.  2.  8; to;  —  pasvas^a  ttaoraca  'ys&t  parB danivqnO  Yt  ^.  S ;  V.  2, 8,  9,  1 1 ;  —  asti/n . .  sBns  va  parairistahe  *yehe  va  V.tf.io;
21542:•  j.  'yäta-  n.  Terni.  techn.  für  die  der Schwere  nach  dritte  Art  von  Körperver- letzung"; %rUäm  tarS  x^araya  (sd.)  .  . vUp)m  larS  *yär?Jräjahehim  °t)m  ästrydti N.42i  F.4f.i  —  'fa  raifqm  . .  N.77T{?).
22013:—  yesi  .  .  dim  nsit  tanu.ptn'Afm  *v^ar)  im  Besitz  des  wahren  heiligen  Wissens (sPPfA.)''  "wenn  sie  es  (von  ihm)  nicht ^  befindlich,  darin  eingeweiht"-^;  n)  von wissen,  dass  er  /,  ist"  ^.3$ ,3g, 38')  — \AhM.:  *yqm  mBi  vtdva  matda  vaocat at  vS  xsmaibyä  asBrtä  vasdä  x^arai'^yä '  a/iurS  "was  mir  der  wissende  MAk. (sd)  srava  Y.2Ä10.  a)  'etwas  (Akk.)  1  verkündet  hat"  Y.45-3;  —  vaocä  mH kennen  als  (das)  des  —  (praedik.  Gen.),  j^i?  (VJ'w  zTrfz'i  a^ars  "tu  mir  kund  — denn scire  rem  (esse,  fore)  ahcuius':  yehyäxda  ja  bist  der  wissende,  o  Ah.  —"  Y, tnHi  asät  hacä  vahist>m  yesnl paiti  vaidä  4IS.2.  ß)  sonst:  müahvacff  v3  *Pr7s,- mazda  ahurü  ySi  nnharsia  htnticä  "wen '  rairc  vä  vTävä  vä  >vfdva  {sd.)  vä  Y. von  denen,  die  waren  und  die  sind,  MAh. als  einen  solchen  kennt,  dem  durch  Asa mein  Bestes  fiir  sein  Gebet  zu  teil  vrird" '^.51.22;  —  ynihe  Aätqm  aat  yesm  paitt vaahs  mazdä  ahurö  vatha  asät  hacä  Y. 27.  15;  —  yaisqm  nS  ahur5  .  .  va^hs vaiha  "quorum  nostium  Ahuras  ..  melius (fore)  seit"  Yt.iÜ.s;—  *yat  nSil  vist»m drvats  "wovon  man  nicht  weiss,  ob  es einem  Ungläubigen  gehört"  N.  54**;  — ysi  vaahsul  vaEdtnä  (PPfM.)  mananhs .  ,  ralxsnh  .  .  caxrayS  (sd.)  ".  .  die  dem guten  Sinn  gewissen  Erbanteile  .  ."  Y. 34.  7.  3)  Perf.  Pass.  'bekannt  sein als  —    (Nom.),    etwas   (Nom.)    gewisslich
27377:•  j.,  g.  sravah-  n.  i)  'Wort'  (in  koll. Sinn),  (Plur.)  'Worte':  at  vS  ximaihyä asünä  va^ä  x^arai^yä (sA.)  vaintyä  'vi" Y.  2tV.  10.  a)  sva.  'Spruch,  Lehre': dusjastis  'vä  mSrindaiisA^  V.^2. 9;  10;  1 —  ya  ränhaym  (Sp.  iji?  u-)  'vanha*''  1 vahistät  syao%anäi  mantiVW  Y.32.  la;  —  j masda  al  insi  vahiHa  'vsscä  iyaohanäcä ' vao/ä  . .  isiidpm  (sd.)  stS/J  Y.  34.  is^^i  — yai  ta    'Vit  dtvn/ayan  ya  ..  al%rapaiayö\
30673:">  Er  heisst  im  Mp,  x'arair  oder  x'arsel  Hhr und  wird  aralislär  ipähpal  genannt,  Bd.  J2.  %. Eig.  'sonnen gesichtig'.
```


## [2026-09-14T03:09:48.990Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Wunde\" BRT.txt | head -40"
}
```


### [2026-09-14T03:09:49.042Z] TOOL RESULT

```
5895:•  j.  asnae-rae§a-  Adj.  'in  der  Nähe Wunden  beibringend,  verwundend':  -ss (nämL  ist  der  Hund)  yatia  vaisS  V.  y. 46;  —  'iö  ydha  jahika  V.  rj.48.
16415:13.  132;    —  yimca   kavam    'mm  (AS.)->   ,  ^  ^^5^^»-  m.  i)  'Quetschung.  Quetsch- Ei|!'Bed.?     Ob  A(ygl.  aipty^sinah-  (zum  V.   r"*^^'    Jü"   j^'^Pfe«'   Instrument   beige- '■'■r/B''«flj-,  S2.i)?  — »Sid'/aE.   brachte  Wunde':  _>■?  jfiwe  'nm  jatntt  ytm
16695:Vgl.  got.Äoiy o 'Wunde',  ahd.  *a«fl' Verderben'». —  S.  auch  'band-.  —  Pü.;  vimärhtilan,  erl. : ähökcmian.  —  ■>  S  3g6.  3.  —  ')  Vgl.  dagegen IQ  ^aAümM-.  —  j)  Doch  a.  Zupitza  Gu(t,  30.
27496:'Komp.  mit  ND.  (*.  srü-  NÖ.  3)  im  1.  Glied; "iläy  f.,  zum  V.  ttä-,  s.  daiu  ZDMG.  4^.  665 und  mp.  ittnii.  Eig.;  'dem  ein  Horn(spltzen)- paar  als  Ständer  dient',  vom  Pfeil,  an  dem unterhalb  der  Spitze  ein  paar  Hornspitzen  als Widerhaken  eingesetzt  sind,  durch  die  er  in der  Wunde  zum  Stehen  gebracht  werden, festsitzen  solL
```


## [2026-09-14T03:09:50.304Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"x\\^afna\\|x'afna\\|xvafna\\|afna-\" BRT.txt | head -20; echo \"--- schlafen\"; grep -n \"'schlafen'\" BRT.txt | head -30"
}
```


### [2026-09-14T03:09:50.441Z] TOOL RESULT

```
6967:•  j.  a-x'afna-  Adj.  'schlaflos':  °w?  a/ii  . . terii  ys  ahurg  V.ifj.io;  —  mtiirstn  .  . 'mm  jai3urv3t»k?i)i  Vt.  10.7.
6970:Ableit.  aus  a^afna-;  vgl.  ^\.!nhäslya- :  stikäua: —  Pü.:  iLL''äplh.
7204:•  j.  a-x^afna-  Adj.  'schlaflos':  °tis  ahi . . tum  yS  akurö  V.  ip.  zo;  —  mtirim  .  . 'nsni  jar^iiurvaahiin  Ytio.  7.
22128:•  j.  vaenant-  Adj.,  PPA.:  s.  vafna-. KompE.  !
--- schlafen
```


## [2026-09-14T03:09:56.410Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Verwundung\\|hufs\\|x\\^afs\\|x'afs\\|xvafs\" BRT.txt | head -30"
}
```


### [2026-09-14T03:09:56.488Z] TOOL RESULT

```
12440:KonpA.,    E.    —    Et?    Gon.S  Versuch,   der '*daiaä-  und  *dainä-  etjrmologiich  gleichselit -  inm  V.  Väty)-  -  überzeugt  mich  nicht,    S. noch  No.  I.   —   np,  din.  —   Pü.:   den,   Sü.: dätih{%    —    I)  Wo  a?  im  Metram   für  iwei Silben   rechnet;    s.    'dainä-.     Also   wohl   ae ans  ar.  d^i^,  %  St. •  j.,  g.  'daena-  £  Hniieres  Wesen,  geistiges Ich,  Individualität',  öfters  kaum  übertrag- bar"; i)im  gAw.'':^<i/«J  maadapaour- vTm  gai%äslä  la^  'näs^  %wä  manankä xratüica"^  du,  qM.,  zu  Anfang  Individuen schufst  und  Individualitäten  durch  deinen Geist,   und  Verstandeskräfte"  Y.  3t.  1 46.  6;    —    nSit  nä    manä    ,  .   s}ngA3 xraiavö  .  .  varanä  (sd.)  .  .  uxla  .  .  }yi "hanä  .  .  "na  .  .  urvaaB  hacainil  Y.  4$. —  vaauklmcä  °nqm  ..  fstratam .. ärmaitim "^•37-  5i  —  ^^  ^'^  ux^äis  fyao%an3  'tiä (IS.)   a&m  spnvat  (sd.)  Y.5/.  ar;  —  y7 *iat  manS  vahyS . .  aSyaslä  (sd.)  kvö  'nqm iyaoiianacS  valanhScä  V.4S.4;   —  yqm yao/  (sd.)  •nqm  .,  dämyam  *hudJnao^ .. y.44.^;  —  yS  'nqm  vohü  ^sänltä  (sd.) ftananhä  Y.  49-  5 1  —  '?«"  ^^^  dqstvam (sd.)  'nayai  frävao'a  Y. 46^.7;  — frö  .  . a-sä    'na  fradaxsaya  (sd.)  Y.  j^.  13;    — AvB  tat  .  ,  ahtnäi  dazäz  (sd.)  'nayä  (IS.) z-aldMtttö  Y.57. 19";  —  mSnÜl  T  mqtdas- düm  *valds.düm  'näbll  aiyasta  (sd.)  ahBm yJ  . .  Y-53-  s";  — yas/ä  .  .  tarJ.mqsia  ,  . sao^aiUS   Sng  (sd.)   patdU  spmiä    'nä urvahs  .  .  ".  .  des  Saelyant  .  .  Ich  wird ihm  Freund  sein  ,  ."  Y.  45. 1 1***;  —  tJm aAfSfum  . .  'nä  saoiyantqm  yä  . .  urväxiat (sd.)  hyat  .  .  mTedtm  .  .  Y._j4.  '3;  —  yä "nü     vairXm    hanät   mjedtm    asahya  yssa astftt  (sd.)  Y.  54. 1 ;  —  hyai  'na  vakUn yBjpn  (sd.)  mlzdlH.49-  9;  —  ^y<'i  mlSdjm ^trtavai^lm   (sd.)  fradadä^S    'näbyni^  Y. 40.  I  ;    —    harthus  (sd.)  .  .  dadät   aAurS 'fiayüi  va^huyai  Y.  5j.  4;  —  'nayäi  va»- ktiy^i  yqm  ksi  Uyam  (sd.)  äatü  . .  ahuri>
19853:mit  a  'durch  Anstossen  besclddigen, verletzen':  ast>m  'ans  mattrauanqm"  vis- pala  yS  "mastraynqm  amqsta  (aSj-AorM.) "x^'arScÜnm  (sd.)  "aS^  anye  '^HkaiatS "wenn  einer  ^inen  Knochen  des  Schädels und  wenn  einer  den  ganzen  Schädel  (eines Toten)  durch  Anstossen  verletzt,  so  sollen sie  (beide)  dies  und  jenes  mit  der  Strafe btissen,  wie  sie  für  Verwundungen  (Leben- der) bestimmt  ist"  F. je
22042:—  yäha  drvä  gaom  *visie  (3SPM.)*'  .  . *viile'  Aog.  S2;  F.  Ä*>;  —  vispä  ta  p?nsqs ya'ha  diät  haSi  gam  vtdat  västryS  "nach all  dem  frag  idi,  ob  durch  A!a  der  Kuh teilhaftig  werden  wird  der  Bauer  . ,"  V. 5'-  S*''j  —  ""^  ^^  ""^  ät^ham  zadhranam (Gen,  ab  Obj.)  vindita  '(3SOM.)»  Yt ^7-  S4i  —  '^it  *^  ^^  asraoyanam  tanu- nqm  alahe  (Gen.  als  Obj.)  .  ,  *vthaiti^'> P.  75;  —  yim  dim  va^tät  *tvistaiha  (sd) *vindän?m  ndit  *'ava  yä  *vistas!va  (sva. 'gegen  Entgelt")  N.  t6;  —  s.  noch  i'ldat.', vKat."  a)  mit  Gen.  (statt  Abi.)  der Person  'von  .  .' :  asanS  sasta  draiimnS  .  . vindimnS  dahufs  akuräi  mazdäi  „Steine .  .  von  dem  Schöpfer  AhM.  (sie)  be- kommend" V./5.4.  3)  'Jemandem  (Dat) etwas  erwirken,  verschaffen,  verleihen':  at.. taibyB  xidhnm  vohB  mananha  (als  Subj.) *»S(i'riÄJjÄ(3SKA.)9'  a^byö  jaj«(sd.)  yBi . . Y.J0.8;  —  s.  noch  vindat.-.  4)  'fertig, zu  Stand  bringen,  bereiten':  aAyä  vohs aosO  vida  (sS.)  mananhä  "ihm  bereite, o  VM.,  den  Untergang"  Y.4g.  i;  —  kva ht  aols  vindäma  V.  ig.  46.
25960:sroawna  aisqm  'fänhüY.^j.tT.  a)  'Huf- stilck,  Stück  eines  Pferdehufs':  'fim  vä  ää- lirum  vä  zfm.var>tpm  vä  kqmBt  vä  xrüh äismanqm  "ein  Stück  Huf  oder  einen  Holz- klotz oder  einen  Erdklos  oder  sonst  ein Trumm  harter  Erde''  V.p.  11.
```


## [2026-09-14T03:09:58.661Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1870\\|1871\\|1872\" BRT.txt | head; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=t.find(\"x^ara\")\npages=t.split('\\f')\nfor n,p in enumerate(pages):\n    if 'x^ap-' in p or \"x^ara-\" in p:\n        print(n, p[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T03:09:59.884Z] TOOL RESULT

```
2070:Banbay  and  London   1872. AV.:  AlhaTvavtdasamkUä.
2113:ZL.:  Ein  zoroutrisches  IJcd.     Kapitel  30  des  Yasna.     H&nchen  1872.
2154:MHaug.    Bombay  undLondon  1870. (W)Pbeli.witz  WbGrSp.:  Etymologisches  Wörterbuch  der  griechischen  Sprache.  Göttingen  1892. PrJ.;  Preussische  Jahrbücher.     Berlin.
2166:E(r)A(1t).:  Eranische  Altertumskunde.    Leipzig  1871fr.
563 eit.   —   Zum  \'.  'mh-;   vgl.  aL firäj-llay  f.  'Zeugung';  s.  daiu  Bthl.  ZDMG. 50.  692,  Hbm.  IFAoi.  /0.47  und  'aan-  No.  6. —  mp.  (Pa.)/raianJ,  ap. /ariand.  —  ')  NA. hat  «inige
```


## [2026-09-14T03:10:06.440Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor n,p in enumerate(pages):\n    if \"Schlaf\" in p:\n        print(\"LEAF\",n)\n        for line in p.split('\\n'):\n            if 'Schlaf' in line: print(\"   \",line[:250])\nEOF"
}
```


### [2026-09-14T03:10:07.537Z] TOOL RESULT

```
LEAF 203
    %raodet  *^/ara%ra  (s  294.  3)  verlangte.  imSchlaf  ergossenenSamen  vorgeschrieben
LEAF 204
    T  rausgese    .  ,.,     .  ,         |  den  im  Schlaf  ergossenen  Samen  vorge-
    •  j.  ätrv.karst-  Adj.  'der  sich  mit  dem  j  ')  Nämt.  dem  Mann,  der  seinerieit  {»/•"  süram Feuer  zu  tun  macht,  dabei  tätig  ist':  'tä,  /raB.i-^y^nm)  aus  dem  im  Schlaf  ergossenen p  _                                           
LEAF 221
    •  j.  a-W8p0Ji''afnan-  Adj.  'der  keinen voUkommenen,  d.  i.  tiefen  Schlaf  Jiat': zainauha  'na  (NS.;  DämL:  ist  der  Hund) yaia  vastryS  fsuyas  V.  y.46.
LEAF 397
    mp.  (Pü.)  dm/istan  i),  PDi.  war-^aam  "ich  rede an»  dem  Schlafp).  —  ')  Im  Gegens.  zu  mrav und  vai-,  t,  H.  2.  \^,  35  twd  V.  ig.  6,  7.  — •)  Statt  davi',  %  36S.  22,  33,  3^.  —  S>  Hos.1 NpEt.  17  a.
LEAF 545
    Ableit,  aus  büsyanl-,  Bthl.  KZ.  25,  547-  — mp.  (Pü.),  np.  büiäsp  'Traum,  Schlaf;  s.  dazu NÖLDEKESWienAW.73ö'.2.  i.—  D Vgl.SWien- AW,  57,841.8:  bäsyäsp  u  büiäsp  um  i  dni  S  ail ti  i^äb  ärad.  —  ')  Statt  'Äjin.  Der  mask. 
LEAF 899
    •  g.  'zaeman-  n.  'Regsamkeit,  Munter-, Wachsein' :  ks  hvaph  c^afmmca  dät  'mäcä "wer  schuf  wohlwirkendSchlaf  und  Wachen" Y.  44. 5.
```


## [2026-09-14T03:10:14.031Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"nleaves\",len(pages))\nfor n in range(965,len(pages)):\n    p=pages[n]\n    head=p[:120].replace('\\n',' ')\n    print(n,'|',head)\nEOF"
}
```


### [2026-09-14T03:10:15.205Z] TOOL RESULT

```
nleaves 1041
965 |   selbe  Mutter hat':  bardiya^ . .  '13  hamapita  ka''bU}iyahyä Bh.  /.  10. Komp.;  ^a* -!-«(•■)  oder  ^hama-\m'  (m
966 |   vgl.  samyän, sarnict  —  Pfl,;  lässt  das  Wort  aus.  —  >)  So Jpi,  Mfi;  NA.  hat  hqiriM;  s.  nochNo.  3. — »)
967 | (ADn,)"' vaAyö  oA^misd.)^  Y.^0.3.  c)  imjAw.: yazalsa    ml  Alm  (ASf.)  .  .  yqm    andvlm sürqm  Vt.  5-  I ;   p
968 |  verschaffen suchen':  y.l  *malnil  (sd.)  yJ  drigvalti (Sp. 7760.)  xsä^nm  hunaiti  duL^aö^anäi ahurä  ".  .  der  d
969 |  ;  —  yim  as^nt .  .  iralsttm  dädarfsa  x'ahe  gayehe  ^an- vaiB(s&.)  ampiahe  Y.g.i  (s.  YLÄii  bei I  a);  —  as
970 | 2.  a)    mit    dariya-    'die  langdauemde (ewige)  Seligkeit':  tanvaica  * kaosravanhtm urunaeca    darrf>tn    'va
971 | enannt  Nach  Yt.  /p.  I umlagert   da»  Gebirg  alle  Länder  des  Westens I  sind  nach hanka- und    Ostens.     Es 
972 |  •  j.  harwSiS-'>  n.  'Wahnsinn,  Verrückt- heit': ma  a^ra  frakavS  . .  "ois  V.  2.  ig. VgL  mp.  <tj/iiX' 'mad, 
973 | la ahurB  mazdä .  .frä  'rata  (ND.)  amtr^täta Yt.  jo.  92;  —  saröi  buidyäi  (sd.)  'vätä am>r?tätä  Y.  44,  17; 
974 | tse V.  JÄ  67 ;  *75.  7,  8;   —  yat  ma^yS  mahm  1 V.  5.  26. xÄay-i  aw  franhsmaiti  V.  Ä  32.  mit  «/«  'mit 
975 | amm  vaa-  anietien,  s.  va- vana:  Zu  Y.  6i.  6  sind  die  WStter  in  NA. ^schlich  verbunden.  —  *)  Vgl.  iSt, 
976 |  Stars  V.&.So;  So  PüZ. Ableit.  aus  '-pia-').  —  Pü.:  /ij  looo lanisniA.  — ■>  Oder  aach  un-Part.  tai  gaa-; 
977 |  der  Getreideerate  zu  tun  hat,  fnimentaiius', snaehntis  .  .  •*!!  nivansaym  (sd.)    daaiaU(,a*paiHsJiaAya-{sA.
978 | ichung  des  Ziels':  atlqm  alnanhqm ttalclt  viävä  aojsi  (sd.)  'yi  (IS.)  ya  /ByJ (sji)  ssnghaia  ^.32.  7. Nom.
979 | Adj.  'dessen  (üble) ^•^^^•^''^"•^'•^"'^•^^'■'^*^^''^"-  Taten  ausgeglichen,   (durch  Sühne)   quitt .._-,_■  ,      
980 | aca  taSlaca  V.i<).g;  —  Aoa- ma/a  'naca  V.  5,  39115.9;  —  asmano 'na  ayanhama  'na  fraoirinmna  Jraisva- yamna
981 | osse  der  Priester- AbleiL  aus  A ji/aua-,  eig.  'der  das  Mörse^erät  1  ^unft-«):  ^Ä'a/rfwfl  (näml.  arf/ mi^^j)
982 | �m  samvidanti  ye tvaire^aya  'pi  nänloA  grämipi  ...  —  i>  Der Inhalt  der  Zeile  vird  durch  die  Verderbnis  ■
983 |   a:  liei  aorala.  1 •  j.  hi^m  i)  Adv.  a)  Praev,  S.  unter *ham.  [Yt  /o,  125:  lies  hqmJvqmca; —  V.  5.  j
984 | .  6)?  Un- klare Slelle. •  j,  ham.STJta  Inf,  'zu  verwenden,  zu  ge- brauchen', praedikativ  gebraucht:  kai  tä v
985 | g.  'zusammengehörend'; *vifya-  n.,  znm  V.  vat-;  ai.  vgl.  väfya- n, — Vi.  •.  AamnlgSsünJA  gmiäinik,  erl. :  n
986 |   Asa,  zu  dessen  Genossen- schaft der  heilige  Mann  (gehören  wird)" Y.^.7- Zum  V.  hi{yy.  —  PQ.:  » d  ddm  (»i
987 | 0.6; —  irpiuxhai  vacanhqm  xsayamnB  (sd.) •w?i>  vass  Y.31, 19.  a)  gAw.  IS.  und IP.  sva.  'durch,  im  Reden,  
988 | .  auch  Sp.  Komm.  2. 47J. g.  hisvi  Y.  4^.  i;  lies  hkvä;  s.  hitM-. •  j,  hiä  enkl.  Part. :  s.  unter  kXm.
989 |  hupahmainyqm  •nqm  Yt  16.  i. g.  hüJiarilä  Y.  34.  13:  lies  küMr'. •  j.  h&'kairya-'>  n.  Name  des  höchsten 
990 |  xüp  karl,  (la Y.  34)-  po  hakarlärlh.  —  ')  NA.  kü.karHä; s.  aber  R  4  und  wegen  der  Bedeutung  du vorherg
991 | gen: *g>us  asaonS  Yt  13.  118, Eig.  'der  schöne  Rinder  ti&t';  ai.  stigäv-  Adj.  — Vgl.  kvö^va-. •  ].,  g.  h
992 | öge  über  uns  -  Mann  oder  Weib  -  die Herrschaft  führen"  Y.  41.  3;  —  'raii j}mrqm  (sd.)  .  .  rämqmcä  Sil
993 | �itum,  —  »  Dbr.  VglS.  /.  389, •  j.   bux§a^5.t9inäi   zitiert   die   damit beginnende  Strophe  Y._y5, 5:  '^ris
994 |  'üittm  paiti    mihrahe    ".  .  bei  (Sp. 825  u.)  guter  Befriedigung  des  M."''> Yt.io.  log. 1)  Sva.  wenn  M.
995 | Lebensführung  fUr  M.  (ist) . ." Y./p.  i3(?).  a)Plur.  'Äusserungen  guter Lebensführung,  gute  Lebenswerke':  pair
996 | /j.  35;  —  ya^a  aztm käcayme  vamthlm  azatqm  •sqm  anumaße dainayäi  .  .  yä  ml  dalnqm  .  .  zrasca  dai apica 
997 |   1 7. Eig.  etwa  'Betrieb'  sti.  'Gewerbe';  zdtd  V. ihav.  —  Pü.:  hittuxi  ('induitciosus'),  Sü.: frakiliiarmä  
998 | ö  humanaahs . .  'oafna Yt.  ip,  95 ;  —  yä  'nS  asava  Yt.  4.  9;  9. Pü. :  AuJenii.  —  ')  Nur  Yt.  /p.  —  ')
999 | 3. A'bleit.  —  ai.  vgl.  sadki.  Adj.  —  Pü.  (tu  i): kudiilk,  (in  a):  hudinät  (im  gA«.),  hudäi (im  jAw.)5<; 
1000 | 9.  8''. -----  Gray  JAOS.  25.  125.  ai.  TgL  svädmin-  m.'),  —  Vgl.  1 neuerdings  Gruy  JAOS.  3/.  115,  — «)  
1001 | a- Adj. 'wohl  anerkanat, —  voTiZ<Jra>u/tra:  zaraliuslrftn  . .  AälamW  anerkannter,  geehrter  Stellung  befind- •mf
1002 |  (närol.  vayus)  Yt/5. 46. *dSA-  n.,  lum  V.  da-  (ar.  dM-).  —  Pü. ;  kadäk.       Zum    V.    li/j-.    —    Ga
1003 | W.  hpatatii,    s.  Hi AGr.  /.  iSo). •  g.  hupam^Twa-  Adj.  (fem.  'wä-)  'gut 'ü. :  j^  räi  tö  iten  .  .  hubo
1004 | /".  9.  *  I  ''^"^     avam  '/am    abaram    kyc^  .  ,  avam Komp.:   hi'-Yupa^busta;  zum  V.  iaorf-;    vgl.  ""
1005 | f  -qm)   begünitigt.    —    3)    Hds. Fü.:  ki-ia^iimA,  erl. :  eil  dätan.  ,       Itndf  stall  mndf. •  j.hu-b»r
1006 | -  \  Namens.  Ficks  Kon.tniktion  eines  ap.  *lm. ^ranqnt  hufräyasHca  as.frabfrpitila  zao- !  frahäia-  (BB.  24. 
1007 | homatanqm  1832 •  j.  hu•f^ä'yajit1»n'^  •yaStiyn'*  AbsoL  •  j.  bUDara'vant-Adj.  (fem. 'faüT-) 'kirnst- 'mit  guter
1008 | d,)  Vtj.  57;  —  >ff  /a«a/  °navB  Schwüngen,  gescbleuderf :  vazrvm  -ttm {ais  AP.)  yai  pa^^sanaya  nava  •ruiva
1009 | 3i  . .  yät  hl  ^"'"'^  hvaHt«nca  lyao-htam  Vr.  2.  5;  usw.; *mafas*aht\paiü-\  ava  barait'e  pascaäa . .  "  ™  
1010 | dainä-:  yvSfum  °na- aham  kvaca^ham  husyaokmm  hudalmm ^^-  J-  3  i  —  yUnü  fiumanatfhö  kvacanAs huiyao^nahe  kud
1011 | a  aita  däman  *dähimaide 'maya  clsmaide  'maya  matnyämaide  *yam da^at  ahurS  mazdä  Vr.  72.4'';  —  'maya upar»ha
1012 |   Shrma^  5  H  i  avaräiär .  .  pa  an  i  xüp  östnuriimh  baiet.  —  >)  Darf man  den  EN.  KtaiiapTAtir^  heranzie
1013 |   li.  sv)i/a-  Adj. —  Npü.:  ba  an  nii yaita  yimin.  —  »)  Vgl.  RV.  /.   162.  5. •  j  huyaäta'tara- ''  Adj.  
1014 |  amij 'rahyä  taumäya  Bh.s.s;  4.3,  Bh.  e;  — I  cih'c^taxmt^  namd"  asagartiyt^  .. dhaAer  adam  xsahrita^  atnty 
1015 |   drvaspqm  ..  'lam  Vtp. 2.  b)  sonst:  ianüm  ya  mf  valnaüe 'f^ Y.  io.  14;  —  yetihä  (sd.)  k>Arj>s  •oayä  Yt
1016 | . £tlr.  2.  331,  —  3)  Worüber  zuletzt  EKüHN KZ.  SS-  3'3-  Stoffliche  Gleichheit  der  ai. sürä'  und  der  ür. 
1017 |  havaiahäica .  .'nyäica yat  saolyantqm  Vr.5.  i. Ableit.  aus  *Aa-rvan-\  -run-  Adj.;  eig.  'Zu- stand dessen,  de
1018 | .  .  häirilli  pu&ri  vgrmvainti  .  .  *tB (NPf.)  srsuw«/!  Ytij.  15;  —  aiyävfm.. yS  . .  hairini  US  (APf.)  da
1019 | (näm!.  Ärm^  schenke uns  gutes  Wohnen,  sie  uns  Bestand  und Kraft  .  ."  Y.  48. 6. Zum  V.  iiy-;  aus  ar.  *xh
1020 | lsmanqm  aSavat  nafia- nqm  V.  7. 31;  —  vtlastiJrap  yat  (Sp. 1252  u.)  'kanqm  (als  Obj.)  ..  aitiha  s^mS nida
1021 | j. (fem.  •nä-)  i)  jAw."  'des  Tun  gut  ist': yvamm  humanaraA^m  (sd.,  auch  fdSt.) h%-alat»h>m  °%mm  hudaimm  Vr
1022 | .  2*3).  —  S.  das  folg. Wort  und  hqmJiar3lar.  vatj/wqm.  —  ')  Geringe Stelle;  offenbar  ReminUieni  an  V.  4-
1023 | �  *slatia  ahatiy avaiy  mä  dausta  Bh.  .^.  14.  2)  voraus- geht, uzw.  a)  hauv  (Sp.  I73r  u.):  hauv fravartis 
1024 | vum  ist  ohne Bezugsmasse;     hacä     paruviyat<^      'ya  ^' amäxam    taumä    xsäydi:iyä    äh<^    "anti- quitus
1025 | 45  m.)  va vidamahya  Bh.2.6;  j.  18;  —  kärt^  'ye^  \angrB  yS  .  J  fyanhcü  (Sp.  277  o.)  h'i  nStt manä  Bh.2
1026 | .,  DaL;  auf  die  s.Pers.  bezogen^zu  2):  vanhu h°  0ng  .  .  pai:mSng  .  .  *iarat  Y,  4O.  4;  iß  (Sp.  654  m
1027 | r  'Anhang". —  A'  asava  zara'iiuitrll  urva'i^m  lira-  Ableit.  (fcö-,  j'Ji').  —  Vgl.  lat. //*i,  ksl,  w*/, tär
1028 |   . jamyät  yS  na  .  .  sUsit  Y.  43-  3-  [Y. '  "Ä?  H.  2.  11,  11;  —  haxayS  ..  'canhö  Yt 29.7:  lies  hvd.u
1029 |   abava"  Bh. /.  16;  2.4. 1 Ableit.  aus  ^ujjaja-.  —  >)  NA.  bietet  ßlsch- lich  -yä,  NP.;  s.  'ava-,  Sp.  165
1030 | hvar»  ..hau  mä..  ave  siärS  V.p.  41;  Yt ij. 1 6,  *FrBy. ;  —  upa  tairtm  (sd.)  haraihyä . .  yat  ml  aiwtts  
1031 | xlaltai  YtJO.  143; —  yS  yataite  hvar»  yat  am»hm  raim aurvat.asptm  Yt,  6,  4;  —  mi^r»m  ..yakmäi hvar»  aurva
1032 | avakV^: •manu  asaene  Yt.  13. 128,  121. Eig.  'Sonnenlicht  bereitend  (?;'.  —  ')  Vgl.  Dd. jä.  4,    wo   der  N
1033 | �.:  ^arstt  nikitUn.  —  O  Die  Interpunktion der  NA.  ist  danach  la  andern,  —  »)  Vgl.  V. 5.  51./.  4Sf- •  j
1034 | wMa  ioa  ,.  'tpm syad^ram  vtr^zimnsm  Y. 3.0,2;  —  »M mqhrä  "die  gut  ausgeführten  Befehle"  Y. _j. 4,  4.1,  Vi.
1035 |   Vr.  ly.  i ; Y.4'  1 1  H.  2. 1 4;  — yetihf  n^manhs  ciknm humahmüa  küxtimtä  °t»mcä  Y. $8.\',  — kais  hl  (näm
1036 | ,  Npü.:  «»/a  ra.-ffl'a«.  ~  ■>  WörtL duitnafaht  nSii  akmi  hüxtahe  ahmt  dui- 1  'als  ein  paar  (Preile),  die
1037 | TTtS  ahi  spttama  'tW  (NSm.)'> danyS-bizaus  Yt.  I/.22. '}  Them. ;  auffaltige  Form,  die  einen  AS.  ir. *'iujfi
1038 | t  hv  *aahyeiti  .  .  ".  .  die Lanze,  die  der  jl/iärafeind  wirft;  wenn  er auch  gut  werfend  wirft",  .  ."  
1039 |  'p3i  nai
1040 | re banmnSi
```


## [2026-09-14T03:10:22.725Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in range(1030,1041):\n    print(\"=== LEAF\",n)\n    print(pages[n][:2500])\nEOF"
}
```


### [2026-09-14T03:10:23.848Z] TOOL RESULT

```
=== LEAF 1030
hvar»  ..hau  mä..  ave  siärS  V.p.  41;  Yt ij. 1 6,  *FrBy. ;  —  upa  tairtm  (sd.)  haraihyä . .  yat  ml  aiwtts  urvtsMit  starasca  mäsca hvarica  Yti2.25;  V.2.40;  —  strSuSca manhimca  hvar?ca  Y.  2,  11,  77.  9,  Yt. 10. 145,  G.J.  6,  V, /J.  I,  3,  7.5a,  Vyt.4j;
—  haca  hvar»  (statt  Abi)  V.TJ.  10;  — kasna  x^^ngiQß).')  *str^mca  daX  advamm (sd.)  '^.44.  3;  —  fravasayS  .  .  yä  sirqm  ' mäi»hB  hürff  (GS.)  .  .  pa^ff  dalsaym  Yt. ^S-  57'!  Y.  7. 16;  —  hax?6r»mca  yat  asli  . .
hvara.äaeäinan-  184S
I  aniars  mar?h>m^a  hvanca  Yt  6.  5;  — \yakra  aval  hvar»  uxaiti  F.^bj  — ya^ ^  hvar?  utuxsyeiti '^t.  6.  2;  3; — yat  hvar? '  raoxsne  tapayeiti  Yt6.i;  —  hau  Aa (GS.)  vaxiat  a  ha  fraimS-datSit  "von Sonnenaufgang  bis  Sonnenuntergang"  Yt 5.  91  usw.'';  ~ pasca  hü  fraitRSJaiilm  . . pasca  "hvs''  nStt  ueux^atnnS  (sd.)  Yt. 4-8;  —  para  avalAhe  hü  ^war/tS  (sd-) Y.ig.&;  —  raocä  (sd.)  a  . .  hü  paiti alwamm  V.  2.  10;  Yt /2.  3;  —  hvar» raocS  Vr,  ig.  2,  Yt  6.\\  —  ima  raocä bamiitjm  bar»simanqm  avat  (sd.)  yat hvar!  avaci  Y.j6.6;  Yi.ig.a;  —  raaci x'Jng  (GS.)  asnqm  uxsä  (sd.)  aiiirus  Y. 50.10; —  »r^jli..pourusa  hvarS pifyasü (sd.)  Y.  50.  a;  —  yS  acist»m  *vaenaAh! (sA.)  aog>da  gqm  astbya  kvancä  Y._j2. 10;
—  ^ha^"^  M»tya  (sd.)  
=== LEAF 1031
xlaltai  YtJO.  143;
—  yS  yataite  hvar»  yat  am»hm  raim aurvat.asptm  Yt,  6,  4;  —  mi^r»m  ..yakmäi hvar»  aurvat,asp»m  dürät  tutnS  baohayäti Yt.io.go;  Az.^;  — paurva.natmat am»sahe hu  yat  aurvat.aspahe  Ytio.  13; — hva  r»Ja am»s}  sp»ntt  yatamaide  Vr.  ig.  2  (?),
KompA.  {hvar>.',  i'/ng.');  s,  noch.  Az-ar>xJaela- (auch  für  Y.  T.  11).  —  ai.  jfdr-  n.,  np.  xer (aus  it.'x^ar-,  Srfp);  gol.  vgl.iHma.  —  iFlei. S.  S  J9«  40s.  -  Pü-:  ^«rlft.  -  .)  Slven. unter  vaxsa-  und  frähnS.dätay-.  —  '>  Soll jedenfolU  eine  Form  zu  hvar-  vorstellen. Wertlos.  —  3)  NA.  hü.bämya.
•  j.  hvar«-xäaeta- "  n.  'der  leuchtende Sonnenball,  Sonne',  auch  als  Gottheit;  yas? tava  mazdä  k»r»naot  tacar»  ''nsit ..  *anlar».- ann»m{s<i.)  upairi  't»m  Ytj.go; — ya'^a avat  't»m..fraca  ätti  YtJO.  118;  —  °t»m *utyS.raili  Y.ig.iB; — uzayara  uslra  'ta aurvat.aspa  V.27.5;  —  yatcit  ahi..upa  ave stärd  .  .  upa  aom  maT»h»m  .  .  upa  'lfm aurzaj.rijp»m\t  12. 33—^4;  —  -/»m  am»i»m ralm  aurvat.asp»m  yasamaide  Yt 6.\\  6, jj.Si,  Y. /ö'.  4,  S.S.  11;  —  °tai  aurval- aspäi  Y.68.22;  —  'tahe  amtsahe  Yt,  6. o, Y.  22.  24;  Vd.20;  —  hvar»ca  xiaHahe'^ aurvaLaspahe  Y,  /.  1 1 .  a)  hvar»xsattaht (näml.  ayar»)  heisst  der  11.  Monatstag: 'tahe  amfsahe  ralvahe  aurvat.aspahe  S.  i. 11;  vgl.  2.  II,  Y.lö.  4.
mp.  (Pü.)  Statut,  np.  xarsid;  %  89.  —  ■)  Aus der  synffllt.  Fügung  hvan  xSaiOm  erwacbseo; vgl.  i^iirc^mazddh-  und  *hü  bämya  xsofläi'^X. /o.  143.  —  *)  Tmese  durch  ia\
•  j.  hvar«.caeäman-  m.  EN.  eines  der sechs  Genossen  des  Saosyani  bei  der  Auf-
dby  Google
1 849  hvar«.{SidTa-
erstehung,  Ratav  des  Karhar  S
=== LEAF 1032
avakV^: •manu  asaene  Yt.  13. 128,  121.
Eig.  'Sonnenlicht  bereitend  (?;'.  —  ')  Vgl.  Dd. jä.  4,    wo   der  Name   n-^arcaim  l&ulel   (sUtt
•  j.  hvara.ciSra-    m.   EN.  des   zweiten
Sohns  Zarakui'tras  (aus  zweiter  Ehe)*': °raAe  zaraius'trSis  aiaonS  Yt.  y.gS.
">  Er  heisst  im  Mp,  x'arair  oder  x'arsel  Hhr und  wird  aralislär  ipähpal  genannt,  Bd.  J2.  %. Eig.  'sonnen gesichtig'.
•  j.  hvar9.dar9sa-  Adj.  'der  den  Blick der  (sva.  wie  die)  Sonne  hat,  sonoengleich blickend':  yimf  . .  :^ar>na»uhast)m5  täta- nqm  'SO  masyänqm  Y.p.  4; — yat  baväni ,  .  •am  (stattNS'j  ma^anqm  Ytij.iö''.
>L  vgL  svard^s-  Adj.  —  Vgl.  *:^ing.darisa' und  tar>darisa-  (Sp.  451).  —  Pü.:  ^ariit «ikirihilum  hai  marlumän,  erl. ;  huraSmIum. S.  d»iu  Sg.  /,  561  ke  vi!p  däiti  i  vih  huias- miiä  nikiret,  iahn  i  öi  eaim  i  :^arsei  asl.  — I)  Geringe  Stelle.
•  j.  hvar^.dar^sä-  f.  '(solis  conspectus sva.)  Besonnung':  ifä.siairi! . .  raocä-aiwi.- var>na  (sd.)  Sya  (IS.)  hl  z»me  paitt  ni- daihlta  V.6'.  51 ;  —  cvant»n  dräjB  zrvanpm sairi  .  .  raoc3.aiwi.var2na  (sd.)  'sya  Q.^.) . .  bai-ainli  V.  7. 45.
Zum  V.  daris:  —Vgl.  dat^ia-,  —  Pü.:  -^ariel
•  j.  hvarv.darasya-  Adj.  '{so  dass  man von  der  Sonne  zu  sehen  ist  sva.)  der  Sonne ausgesetzt': ^<3i  nSil  aite  matdi^asna  aihm k9hrp?in  'sim  ksrmavqn  yänJrajS^''  "wenn die  ^f,  den  Körper  nicht  ein  Jahr  lang der  Sonne  aussetzen"  V.5. 14";  13'^
"daiisya-  Adj.,  PFP.  lum  V.  dam-,  si.  dMya- 'sehenswert',  vgl.  dfiya-  Adj.  'sichtbar'.  — P�
=== LEAF 1033
�.:  ^arstt  nikitUn.  —  O  Die  Interpunktion der  NA.  ist  danach  la  andern,  —  »)  Vgl.  V. 5.  51./.  4Sf-
•  j.  hvara'Sä(y)- :  'of-  f.  EN.  eines  gläu- , bigen  Mädchens:  ''jyh  asaimyäYti^.  141.
Eig.  'den  Blick  der  (wie  die)  Sonne  habend, ! sonnengleich  blickend';  vgl.  hvarLdarisa-,
•  j.  hva^^.ba^^zah•  Adj,  'die  Höhe  der  1 Sonne  habend,   so  hoch  wie  die  Sonne':
aiöis  baesaza  . .  g^mJra^avAa  (sd.)  äänu.- äräjanha  'zanka  (APn.)'>  Y.6'0.4.
Pii.;  x^ari/t  bäläk.   —  ■>  Them.
"  j.  'hvarez-  Adj.  'des  Wirken,  Tun  gut ist,  wohlwirkcnd':  vattkus  haomö ..kukanß
'vanS  i:i^%.yy  Y.^.16.
Komp.:  hw \-'va>-is-.  —  Vgl.  Uvariz-  EN.  — woss.  roarz  'gut'.  —  Pü,;  hitkämak ,  erL ;  kul
apäyist  i  frärön, —  i)  Könnte  nach  IF.p  löl auch  als  NS.  aus '^f^vs- genommen  werden; s.  aber  'kvarn:
•  j.  'hvaraz-  m.  EN.  eines  G^ubigcn, Bruders(?)  des  Ankasa:  •tä  (GD.)  ania- sayS  a/iioni  "des  JI.  und  des  A.,  der beiden  Gläubigen"  Yt. /j.  124.
Vgl.   'Miarn-.
•  j,  hvarazäna-  Adj.  (fem.  •na-)  'gute Gemeinden,  Bauernschaften  habend,  deren (bei  denen  die)  Gemeinden  gut  aufgehoben sind';  /rava/ayS . .  Aui^axmanU (sd.)  •zänä darrjd^bys  haxthroHbyS  upasitse  vahi^tä Yt./j,3o.  '
Komp.:  ka' -Yvamäna-.
•  j.,  g.  hvaräta-,  hvaraäta-''  Adj.  (fem. •tu-)  'gut  getan,  betätigt,  gehandelt": vXspaca  •ta  fyadhna  yasamaide  varStala vansyamnaca  Y.  57.  4 ;  —  arsuxöanqmca vacankqm  sravanAqmca  ..  °lanamca  fyao- hnanqm  Vi.  12. 2;  —  
=== LEAF 1034
wMa  ioa  ,.  'tpm syad^ram  vtr^zimnsm  Y. 3.0,2;  —  »M mqhrä  "die  gut  ausgeführten  Befehle"  Y.
_j. 4,  4.1,  Vi.iff.2'^;   im  Gegensatz
zu  duzvaHta-:  daityanqm  rahwyanqm 'lanqm  lyadhnanqm  var)zäi  pairi  . .  duz- variianqm  syaöknanqm  varjzäi  Vr.  7J. I,  a)  sonst  nur  neben  hüxta-  und humata- :  humataht paiti  manaahe  küxtahe paiii  vacatahs  °tahe  paiti  iyao%nahe  Yt 16.  6;  —  ästuyi  humatim  manO . .  küxUm vacö  .  .  •Um  syad^amm  Y.  J2.  8;  — fra- stuyl  kumaisibyascä  hüxtsibyascä  'tdibyascä mahwsibyascä  vax>hwSibyascä  varltvSi- byascä  Y.  //.  17;  —  nanm  alavamm dahrUfUm  kumatimca  manB  hüxümca  vac5 •Umca  syaohtum  Vr.  2.  5;  —  aa^. .  manya mananha  humahm  . .  hitsva  mrätoi  hUxttm .  .  sasiaiibya  var>za  't»m  syadhium  Aog. 25  ff.;  ^  *ar»m.maiti  *Aumata  mamne  (Sp. 1121  f)  *ar>m.uxti  *  hüxta  (vavaca)  anm.- varsti  °ia'^  (vavarfzd)F.2^; — yezi  kuma- tim  mainySt  kUxt^m  väcim  mrväl  'bm'^ v»nsyäl  syadhn»m  Gk-iöy;  —  narS  asa- vanö  humataü  mainimna  hüxtäU  ntrvats 'täis(3.\sOb}.)v>rpzyant3Y.jo.4;—AumiUa- nqm  hüxtanqm  •tanqm  iyadaca  anya- dacä  v»r>zyamnanqmcä  vävtmananqmca mahl  aibT.jaritärS  Y._J5,  aj  FrW.^,  i;  — "•"rfil^r* (sd,) ,  .paiti  nivaitis . .  humaialsuia haxtalsuca  •taisu^a^'*  ti.S4;  —  vTtpäi/ 'hwa   humatäii  .  .  huxtäis  .  .  'täis  pairi-
\jasämaidl  Y.36.  SJ  —  yS  hvqm  anhvqm
dby  Google
i85i
hvar§ta-  A
*hvaspa-
1853
yaozdäite  kumatäüca  küxtäUca  'täüca  V, 5.  2i;Ytj. 3;  —  haptavhatöii  humataca hüxtala  "tala  aiwig?r>%mahi
=== LEAF 1035
  Vr.  ly.  i ; Y.4'  1 1  H.  2. 1 4;  — yetihf  n^manhs  ciknm humahmüa  küxtimtä  °t»mcä  Y. $8.\',  — kais  hl  (näm!.  ahunahe  vairyehe)  afsman (sd.)?  humatim  hüxUm  °t3m  Y.  ig.  16;  19;
—  vSca  humata  hüxta  'la  äyesi  yeiti  Y.
J.  4;   im  Gegensatz  zu  duivarsta-  (und
duimüta-,  duiaxla-):  aibigairyä  (sd.)  dathi vispa  kumatäcä  hüxtäcä  't3cä  paitiricyä daikl  vlspä  dmmatacä  duiüxtäeä  dui- varlt3(a  Y. //.  17;  —  frastavattö  huma- taea  huxtala  °taca  niibanmnS  dusmalaca duiüxtaca  duävarstaca  H.  J.  7 ;  —  mä  hra- yqm  vaAUtanam  aiwi^yS  buyata  humata- lieca  mananhs  häxtaheca  vacaahB  'taheca fyad^nake;  "hrayqm  acUianqm  aiwt^yS buyata  dusmatake^a  matiatihs  duiüxtaheca vaianhs  duivarUah^a  syao\  nahe  V.  /A'.  1 7 ;
—  framtniti  humatanamca  häxtanqmca •tanqmca  paiHstätle  dusmatanqmca  duz- üxtanqmca  duzvarstanamla  Vr.  20.  a;  — vlspa  humata  . .  hlixta  . .  'la  bao63.varSta; vlspa  dusmata  . .  dtizOxta  . .  duivarsta  nöU baodd.varita  FrW.  3.  \\  —  nsit  malyö gae'^yS  sll  aojs  manyete  dusmatim  ya^a
mi^rasc'it  .  .    kumatim;    nSit  .  .  /"raoHirf^Q^^  *^^},i^^„^j,^  ..     al^  ^^^  ^^^     ' duiüxtfmya^a  mihrascij  . .  Auxt^m,  nStt  geschossener(Pfeik)"Y.57. i8.       hfasüm . .  Vfrfzyati  duwarstim  yaha  mi^rascil . .  |  ^k  Absol.  sbes.
'timYuo.io6;Gl.l63l;—  humatahe  ahmi\  pa.:  iBi'fl«(?)
=== LEAF 1036
,  Npü.:  «»/a  ra.-ffl'a«.  ~  ■>  WörtL duitnafaht  nSii  akmi  hüxtahe  ahmt  dui- 1  'als  ein  paar  (Preile),  die  ali  gut  geschossene Bxtahe  neii  ahni  'tahe  ahmt  dnivarstahe\  ffA"^.^""'"  '"den';  Pä.  fügt  erläuternd  tir nSit  aÄmiY.io.i6;  —  vlspa  humata. .hüxta  '■
*)    Die   man   durchschreiten  muis,   am   zum
ewigen  Licht  (anaira  ran/d)  zu  gelangen.
KompA.  —  Komp.;  Au' -\-varJta;  —  PiL:M/ari/ (Transskr.);  s.  noch  No.  3.  —  ')  So  (mit  •rflf) P.  i5,  N.  S4,  G5. 163.  —  ')  Pü. :  ^arset/ramÖH
•  j.  "^hvarStay-'^  f.  'gutes  Tun,  Handeln': mananhasca  ^humaiti  hizvasca  *hBxti tastayascä  'ti  *ra^wyg.varJN  (sd.)  Y.28.
Komp. :  hu'-\-varilay-.  —  Pü.  1  kvarll,  —  1)  Hdi.
•  j.  hvarStä-varaz-  Adj.  (fem.  'ti-)  'gute Werke  wirkend';  'r?zqm  alaonqm  .,  •mi- nqm  alaoninqm  Vr.  j/,  14.
Pü.:  hvarit  varzüär.
•  j.  hvars.hazaola-  Adj.  'mit  der  Sonne gleichgewilU':  amisä  spinta  vlspe  'sa  (NP.) Yt.  JO-  5 1 ,  'S- 9^;  —  n^rnS  vi  am?sa  spmtä vispe  •sä  (VP.J  Ny. /.  I.
Pü. ;  harvhp  fa  iant  iäaiU  itär[i),  Npü. :  tamäm yak  murad  äSrand»,  Sü. :  sarei  ciäbMIiiäk.
•  j.  hv-as6av-  Adj.  'des  Waden  schön sind':  hukf
=== LEAF 1037
TTtS  ahi  spttama  'tW  (NSm.)'> danyS-bizaus  Yt.  I/.22.
'}  Them. ;  auffaltige  Form,  die  einen  AS.  ir. *'iujfiim  voraussetzt.
•  j.  hv-asta-  Adj.  'gut  gevorfen,  ge- schössen':  i^a.vasma  (sd.)  .  ,  ya^cit  va- saite'tim  \l.  14.20;  —  äsyaaha{sd.)  'tayä
..•ta  vakist?m  *aah!im  ^afatii (Sp. 360  o.), Vlspa  dusmata. .dttzBxta.. duivarsta  aUslsm *anham  *asaiti  FrW.  j.  2.  A)  n.,  Sing. und  Plur,  Name  des  dritten  und  letzten der  drei  Vorräume  des  Paradieses*>:^i)iVrm gäma  frabarat y5  nars  alaonS  urva  humate paiti  nidähm  bilim  .  .  huxte  . .  'hritlm  .  . 'ie  . .  tBirlm  . .  anayralsva  raocBhva  nida- oäf  H.  2. 15;  ungeschickt  verwendet  Vyt. 54;  —  vTspfm  asai-an>ta  aya  ratu/rtta.. Jasmtun  paiti.barähi  humatäisca  hüxiäisca 'täilca  "jeden  Gläubigen  .  ,  nimm  auf  in Humata  und  Huxla  und  Hvarsta"  Y. ^5.4;  —  am>sanqm  spfitianqm  ..yalsqm ainyU  ainyehe  urvämm  aiwi.vaSnaiti  mtn- 'kw>ntfm{%i..)  humataSsu ..hüxtaisu ..'taisu .  .  *gar5   nmamm    Yt.  13.  84.  Wett-
los: näirikayai  .  .  hus.ham.sastayai  'tayäi Vyt  64.
j,  hv-ast«in  Absol,"'  'mit  gutem  Werfen', in  Verbindung  mit  dem  V.  'ah—,  apasi (sd.)  vasaite  arstil  yqm  *anhyeili  avi.- mihri/  .  .  yafS
=== LEAF 1038
t  hv  *aahyeiti  .  .  ".  .  die Lanze,  die  der  jl/iärafeind  wirft;  wenn  er auch  gut  werfend  wirft",  .  ."    YtJO.  aoC
Zum  V.  'ai-.  —  ■)  iBLld.  s.  asrul>m.  —  ")  Vgl. huMxiim  und  ZUBATY  IF,  3.  135.
•  j.  "hv-aspa-,  p.  "uv-aapa-  Adj.  (fem. 'Pä-)  'des  Ross(e)  gut,  tüchtig  ist  (sind)': 'ps  ahi  *hurähvS  Yt  i0.j6;  —  lä^wan.- satim  ayan.baranqm  (sd.) 
=== LEAF 1039
 'p3i  nai
=== LEAF 1040
re banmnSi
```


## [2026-09-14T03:10:31.493Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hvafna\\|hvap\\|hvafsa\\|xvafna\\|x\\^afna\" BRT.txt | head -20"
}
```


### [2026-09-14T03:10:31.551Z] TOOL RESULT

```
6860:'rS  maaiä y7  mazistJ yjzatanqm yJ  vaAi^^  yt,i^.  ^T  \t%v.;  —  cattt  alte  mi^ra  tava  yit yazatanqm  Yt.J7.16; —  °r>m  tnazäqm  ..'.°ra  ma3äaV.4-3;  —  ahm  äuyoarfm 'rahe hudanfam  mazishm  yjzalim  yim  sjvisi?iH  \  mazdii  3^ai>karpm  ain>sanqm  spmtanam /rädat^ali:}m  dätänmvohunam  damanqm\'^K.i-j.z;  16,  V.  79.  13;  —  us  mg  fita \,  16.  i;  —  nh'afiayemi..daiusj(StvcTZ.)iAaomäi  draond  frSnnaoi  °rS  mazdh  ..  V. °rahe  mazdä  ralvatS  c^annarmAalS  (Sl-  /j,  4;  —  astvatintä  .  .  asts  mazda  °rahe verz.)  mazistahe'a  vahistahe^a  sralHahecaYlx.ig.f)-i;  I3.\\f>,  V./(7.34;  —  buyama xraoMistake'a  xraiwistaheÜa  kukinpttma- ,  'rahe  mazda  frya  väsiita  astayJ  (sd.)  V, he'a  aSät  apanSJtmahe'a  hwiHmanS  vouru.- 1  70. 4;  —  haomö  . .  zaota  °räi  (statt  Gen.) ra/na»/i^  y7  nS  daöa  yd  lata^aylltu^ruy?\mazdai  Vty.88f.;  —  ySs^a  t!  y?na  'ra yj  mainyus  ipmtSJimB  V.  /.  i ;  usw. ;  —  mazda  Vr.  7.  4 ;  —  fravasTm  avqm  yqm pQuru^ar)na)3ha  'ra  mazda  VyL  2^^;  —  °raAe  mazdä  Y.  26.  2;V. 1^.14;  —  vXsp»mca °raki  mazdh  ..  STvUtah!  \.  56.  1;  — ^k^rs/s  'rahe  mazdä  Y.ji,^; —  ««  'rahe ax^aßis  ahi  abai>hJ!  tum  yS  °rD  maxdä  1  mazda  yazamaide  dar?ir3i  (sd.)  mq^rahtr V,  jp.  20;  —  'rät  mazält  .  .  vpr/irayne ■  sp^ntaAe  xralüm  'rahe  masdi  ..  marjirrüi frädat^aliai  yat  huxla'iräi  .  .  ratu-l..  hievam  ° rahe  matdä  . .  fravSkäi  .  .  Yt. xla%rai  Vr.ll.i;  —  huxsa'irSJ^mli.'if  1.2%;  —  gayehe  marP^nS  .  .  yS  paoiryd at  xsa'ir?m  eiyJt  yat  'rät  masdäi  A.^.  °räi  (stitt  Gen.)  mazdJi  manlscä  *git/ta 6;  s.  Y.J5.5;  —  'rät  masdäi  fanhavl  säsnasca  Yt./_J.87;  Y.jp.14;  —  nazdys vohumaill  Y.  I2.\;  "V,  tg.  11;  —  vaAists\ahmi  az>m  (Stverz.,  unter  3)  yö  'rS 'ra  mazda  Y.  /p.  1 5 ;  —  xsayat?  "rahe  I  mazda  vispahe  aukSul .  .  ya^a  .  .  P.  2(.?; mazda  YX.13.-jZ;  —  ise  ^wqm  'ra  mazda ..\  usw.;  Vyt.j^';  —  pascasta  azim  ya  'rS aoaoyf  ahi  a'iaoyS.xratul ..vTsps.viwS  Yi.'mazdil  aoi  urune  urväsma  (sd.)  dassayeni /2,  i;  70.  III,  V.  ig.  20,  a6,  Vr.jp.  i;  — Ivahi/ipmea  ahüm  .  .  V.38;  Y.ig.6,  7;  — °rJ  mazda  hvapis  Yt  5.  85;  Y.  7/.  10  (wo  vasas^a  tu  'ra  mazda  . .  x/ag/a  havanqm ab  Vok.) ;  —  'ra  mazda  mainyl  spinUta  1  däinanqm  Y.  Ä*.  5 ;  —  imat  dqma  yat  "rahe dätar?  gai^anqm  astvaitinqm  asäum  {^\.-\  mazdh  V.jy.14,  17,  34;  Vyt  20,  Vd.  i, verz.,  unter  I  2  a.);  usw.;  —  tsm  bay?m\YX.i(f.iZ,\.22.Z;  —  irrj/^/^-rJ (statt Vok.) t)m  ratüm  ,  .yim  'ram  mazdqm  daovätih?m  \  mazdä  vanuhti  dämqn  .  .  yazamaide  yäü i^t^vcz)  rapant3mtarh'a»h?mt'üpa*voh[i^dadä'ia  pouruca  vanhuia  Y.  7;.  10;  ;.  1, Y.70.1;  usw.;  fo.  9;  —  'rim  mazdqm\  12.  7, Yt  ig.  10,  58,V.  21. 4;  —  azmi  daoqm mainyaem  mainyavanqm  dämanqm  main-...tistrim..ya'ia  mqmcit  yim  'nm  mazdam yaoyä  stSts  ahUm;a  ratümca  Vr.  2.  4;  7,IVlÄ'.5o;  —  ttstrlm  .  .  yahmäi  hazaitnm ^'■57-4j  —  allat  dim  vlspanqm  mazih?m\yaoxstinqm  fradd^at  °rS  mazda  Yt^.45; dazdyäi  (sd.)  ahUm^a  ratUmca  yim  °r}m\iQ.Z%; —  tistrim  ..yim  ratüm  frada'hat masdqm  Y.  27.  i;  Vr.  /;.  21;  —  imimca'  'ro  mazdä  YL<?.  44;  5-  89,  70.103,^5.35; isi"^ rahe paitim ..yim  'rsm  mazdqmY.2.i6;\  —  arpdvjm  . . yeiihe  ca'^wärB  arSäna  ham.- 13.1,  ^.I03{?);  —  ySvaram  °rS  mazdä ..^tlsaX  'rJ  mazdä  Yt. 5.120;  —  ya'ia  vs tä  varmScä  .  .  ahmi  Y.12.  7;  —  mi^rpm  '  'rS  mazdä  fradaiim  haxsat  F.  ^Ib;  —  tä ..yim  yazata  'rS  mazdä  raoxsnlt  paiti  (frava^ayS)  ii3..'ä^rayente  ..aomna  'ra{lS^ gars  nmänlt  Yt.  10.12s;  5- '7!    —    avi\  mazda  Yt  13. 146;  S.7,  $&;  —  äyaptj/r.
7204:•  j.  a-x^afna-  Adj.  'schlaflos':  °tis  ahi . . tum  yS  akurö  V.  ip.  zo;  —  mtirim  .  . 'nsni  jar^iiurvaahiin  Ytio.  7.
10715:gAw. :  ahya  '"kräXa  maziiiäcä  *hvapa- nhäisca  (sd.)  tsm  at  ,  .  yasamaidl  Y.^J/. a;  —  kudä  (sd.)  asim  vohuca  maus '%r)m^ä  Y.  25.  1 1 ;  —  yüism  aäbyS  .  . aogü  data  .  .  '%nmc3  .  .  yl  kuhitts  rä- mqmcS  (sd-)  däl  Y.  2p.  10;  —  isasä  (sd.) . .  maibyö  '"^nm  aojönahvat  yehy3  vfndä (sd.)  vanalmS  *drujim  Y.J/.  4;  benutzt V.ao.  8;  —  tat  mazdä  tava  '>rfm  yä  .. düAf  drigaov!\sA.)  vaiyj  Y.ß^.g;  — yJ vahyJ  varihSuS  dagdi..ahurö  '"S^rä  mazdä Y.5J.  6;  —  tici  '^rä  mazdä  dqmis  (sd.) ahurS  'V.4$.T,  9;  —  maibyS  masds  tavä rafinS  JräxStuiam  (sd.)  kyat  ^wä  °&rJ a/Jt  hacä  frqifa  Y.  4!?.  1 4 ;  34. 15;  —  y} dfmanahyä  'hnm  M^rahya  vä  daSySu:" va ../radahäi{sA.)  aspinzatä  Y.Ji,  16;  — yastJm  °ärJ/  mazäJ  mSÜai  (sd.)  jyätSul Vä  Y.  46.  4;  —  at  ratqm  zara'iuitrS  .  . dadäiij  paurvatätim  . .  mazdiU . .  ux^aHyäcß (sd.)  ifraespm  '"irimcä  "..  den  Gehorsam und  die  Herrschgewall"  \.33.i4;  benutzt Yt  IJ.  88 ;  —  vauhstts  dazd,l{%ü.)  manau/iS lyaöhananqm  a»fiSus  mazdäi  ''knmca ahuräi  a  X.2-j.iy,  —  hux^a^rSJimäi (sd.)  .  .  '"ir^m  .  .  äad)mahicä  cismahicä *hvqnmakicä  Y.^5. 5;  —  yS  dngvSUi '"^nm  hunüiiJ  {?,d.)  Y.j/,  15;  —  yais *ffrMm3{sd.)  asäivaratä..°'^r3mca  lianqm *dnfim  Y. 32.13;  —  '>rais  yujin  (sd.) karapanU  .  .  akäis  syaohanäis  .  .  Y.  46. II.  a)  mit  Gen.  'über  — '  (s.  2  a);  tarn
13161:d3t  apasia  äat  urvarosüt  . .  raocäsal  dal bämXmcä  vlspäcä  vohü  Y.^y.  i ;  38. 4;  —  ks hvapä  raecäicä  (sd.)  ääi  luttss^ä  Y.  44.  J ;
20155:ahyä  xlahraca  'jUnäOSyä  ^hvapanhäiS- (sd.)i'a  tSm  (näoiL  akunm)  yasamaidi  Y. 3'J.  2;  —  mihnm  .  ,  yahmi  ..  'sa  amava nilahm  Yt./o.  64(?).
27518:•  g.  'zaeman-  n.  'Regsamkeit,  Munter-, Wachsein' :  ks  hvaph  c^afmmca  dät  'mäcä "wer  schuf  wohlwirkendSchlaf  und  Wachen" Y.  44. 5.
30643:hvapah-
```


## [2026-09-14T03:10:33.161Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"-- PHD xwab/xuft\"; grep -n \"^xwāb\\|^xwab\\|^xuft\\|^xufs\\|xwamn\\|^xwāmn\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-14T03:10:33.242Z] TOOL RESULT

```
-- PHD xwab/xuft
PHD.txt:223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
PHD.txt:662:xwāb 95 xwārīdan
PHD.txt:663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
PHD.txt:1694:dream būšāsp, xwamn.
PHD.txt:2468:interpreter targuman; ~ of dreams xwamn-wizar.
PHD.txt:2980:oneirocritic xwamn-wizār.
PHD.txt:3694:sleep (n.) xwàb, xwamn; büšasp. sleep (v.) xuftan, nibastan, sleeping-platform bālēngāh. sleepless axwamn.
PHD.txt:5518:xwamn v. alo 9 45 éehelN
PHD_mackenzie.txt:1352: a-xwamn ['hwmn ] sleepless.
PHD_mackenzie.txt:5578:xuftan. xufs- [HLMWN-tn l < A "II (llm; hwptn l , hwps- I M xwpt, N
PHD_mackenzie.txt:5589:xwab [hw'b IN -] sleep.
PHD_mackenzie.txt:5608:xwamn [hzumn', bmn ' I M xwmn] sleep, dream.
PHD_mackenzie.txt:6435:dispute (v.) eraxtan; V. fight.         dream bilsasp, xwamn.
PHD_mackenzie.txt:6906:     xwamn-wizar.                          justice dad, dadestiin.
PHD_mackenzie.txt:7577:silent tust, xiimos.                          sleep (n.) xwab, xwamn; biisasp.
PHD_mackenzie.txt:7580:silken abresomen.                             sleepless axwamn.
PHD_mackenzie.txt:10875:sang, SHy                   Jft'     xwamn                               ,r:!J'
PHD_mackenzie.txt:11703:xufs- l                   -,~          harwisp                 ,te..u~
PHD_mackenzie.txt:11704:xuftan l               \,~,~           xrostan                \\te..1' ~
PHD_mackenzie.txt:11899:a\Vestam                   .<tc.vt-'       xwamnwiziir                )....~,~~
```


## [2026-09-14T03:10:46.621Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# leaf = printed + 21\nfor p in (107,):\n    for leaf in (p+21,):\n        print(\"=== HRN printed\",p,\"leaf\",leaf)\n        print(pages[leaf][:3000])\nEOF"
}
```


### [2026-09-14T03:10:47.690Z] TOOL RESULT

```
=== HRN printed 107 leaf 128
— 107 —
Dialektisch ist die ursprüngliche Flexion nach der
neunten indischen Klasse sekundär wieder eingeführt
in Kasan: V(öni§ün) Impt. bann (Inf. eirlän; das an-
lautende k ist hier erst zu h geworden, wie in g.
heridmün, und dann gänzlich geschwunden), Q(ohrad)
bd/rm, K(e8e) be/rln^ Z(efre) biirln.
483. y(usptden 'schlafen , {TCSir auch *beschlafen, schänden
(Is. 13, 16), ^Nr2'D?l5 (Jer. 50, 6), /?(/"/e/«, /uspamJen.
aw. [/^x^ap- , yjapta- , [/^/"afs- , /"'afsata 'schlafen* ;
phlv. x^aftaii , yj^aftak , /;'afsUan bezw. /uftmi ; ai.
y'svap'^ svdplH.
oss. d. /iissthi, t. Russin (309); bei. vapsay^ n. vafsay^
vapsay (403); wa/. rä-yp-am^ ro/opt-am yö/s-am, sar.
yufs-am, si;'n. sows-am.
Hierher gehört wohl auch np. /efj, /efjä, ber/efj (HF),
'Nachtmahr , das de Lagarde, Ges. Abh. 55 mit aw.
xawza- oder, wie er lesen will, yawja- (vd. 8, 32 (99))
zusammenstellt. Doch scheint mir auch das, Beitr. zur
altb. Lex. 44, über aw. x^mba- Beigebrachte diese
Ansicht nicht genügend zu stützen, und mir bleibt
daher die Übersetzung Napf und 'Topf (Geldner,
KZ. 25, 573, 583) die wahrscheinlichere^); vergl. auch
skr. kumbhä' in übertragener Bedeutung als 'Hure*
(allerdings spät), worauf Geiger, Ostiranische Kultur,
S. 341 Note 1 verweist. Mit np. küze lässt sich
aw. ;^aw'2:a- lautlich doch vereinigen, vergl. No. 872.
484. "^estü 'Kern*.
Vergl. s. V. est (No. 81).
aw. astu- 'Körper ist unsicher.
485. Y^astü gestehend, beichtend; Geständniss*, hestä^ ynste-
väne, ^esteväne.
aw. ^x^aMavana- (vergl. äMavana-) ; phlv. yustük,
x(u)stavän, arm. LW. /ostovan.
de Lagarde, Beiträge zur altb. Lexicogr. 21.
*) Auch Caland, Zur Syntax der Pronomina im Avesta, 15
billigt Geldner 's Übersetzung.
```


## [2026-09-14T03:10:47.748Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"=== HUB printed 56 leaf 66\")\nprint(pages[66][:3000])\nEOF"
}
```


### [2026-09-14T03:10:49.141Z] TOOL RESULT

```
=== HUB printed 56 leaf 66
— 56 -
persische anzusetzen: pr. krnamiy^) (vgL air. crenim
*kaufe'), ptc. xrlta- (vgl. air. crtthid 'kauflustig), inf.
*xrttanaiyy die im Np. zu* kirram^ xirld, odridan
werden sollten. Letztere liegen (nach dem Farhang
i Sh.) neben xartd, xarldan vor, zu ihnen wurde ein
Praes. xaram (Hafis ed. Rosenzweig I, p. 78, v. 11)
nach dem Muster von purmlan : pursam etc. neu ge-
bildet. Wo findet sich das pr. xartnam (Sal. Shuk.
p. 53)? 1st es alt (== skr. krinami) oder eine dialekti-
sche Neubildung? Jedenfalls das letztere. Vgl. die
Dialektformen bei Horn und ZDMG. 36, 74.
488. Ich trenne xafj ephialtes* von xuspidan schlafen' und
stelle es mit de La garde zu zd. xawza" (phi. xafzik
Phi. Vd. 113, 4 V. u., 114, 4 v. oben: lies xafzak?),
das mit np. kuza (arm. LW. kuS 'Krug* = zd. ^kum-)
nichts zu thun hat. Vgl. afgh. xapasa fem. night-
mare'*
488. Lies afgh. LW. xa^ta 'Ziegel*.
489. Ich sehe nicht ein, was der Begriif 'Aehre' (np. xoSa)
mit dem Begriflf 'trocken' (np. xuSk) zu thun hat. Np.
xdsa bedeutet zudem auch 'die Traube' (des Wein-
stockes und der Dattelpalme). Ebenso urteilt Geiger,
Etym. und Lautl. der Afgh. unter Nr. 266: vami
*Aehre*.
492. Zd. hareii- = phi. halak ^= paz. hala *foolish, silly
Min. 2, 61, Shk. 247 (davon halal Min. 51, 6; 58,
2, 3 'foolishness, silliness , als Gegensatz von danai
'Wissen' und hunarmandi 'Tiichtigkeit'), liesse ein np.
*hala *th5richt, verriickt' erwarten. Np. xala res
acuta, ictus, vulnus* etc. gehort jedenfalls nicht dazu.
497. Np. x^dsta = phi. x^astak 'Besitztum' = arm. LW.
xostak in xostakdar *der Erbe' (Steph. Orb.) = phi.
x^dstakddr (Besitz-halter) *Erbe* (Pand-nama i. A. M.,
Bombay 1869, Gl. p. 80).
*) Im Skr. stiinde krmami fiir *krnatni wie hhrmami ffir ^bhrnami.
8. p. 28, Anm. 4 und skr. kraya- *Kauf neben krl wie zd. harOii^a'
neben hhrl.
```


## [2026-09-14T03:11:02.705Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor p in (108,109,110):\n    print(\"=== HRN printed\",p)\n    print(pages[p+21][:3000])\nEOF"
}
```


### [2026-09-14T03:11:03.686Z] TOOL RESULT

```
=== HRN printed 108
— 108
486. yi^usur 'Schwiegervater.
aw. /asitru' 'Schwiegervater ; ai. imruru-; arm.
skesr]ah\ d. i. 'Mann der Scliwiegermutter (Hübsch-
mann, Xo. 253).
kuvd. /a2ur, xozJ)\ /aur 'Schwiegervater ; afy. s^or;
bei. n. vasarik 'Schwiegervater, vasar\2ä/t *Schwager
(405); wa;K'. yjtrs, sar. (LW.) Xasur.
•Vergl. /Hsrä (No. 487).
487. xusrfi, zesä^ /jisü^ /'es etc. 'Schwiegermutter.
Käs. /asrii',
ai. <;DarrU' 'Schwiegermutter'; arm. akesnr (H. No. 253) ;
lat. socru-s; ksl. soekry.
kuvd. /ost, /esü, yasrü 'Schwiegermutter; af/. ;K''ö4fa ;
bei. V((8sö, vasl, vase (406) ; wa;^. /as, si/n. /as, sar. /,e/.
Vergl. ytisur (No. 486).
488. x^Ht 'Ziegel, Backstein'.
aw. istya- 'Ziegel, Backstein' ; phlv. /ist ; skr. isfakOr-
'Backstein'.
afy. LW. /ßta; bei. ist (168).
489. ^usk 'trocken', /ös« ') 'Ähre', yös, yöslden, yösdniden
(AM. 236 Zeile 3 v. u.), /mkUm,
Kä§. tisk (jendn, husküdSn.
ap. Msia- trocken'; aw. huskd- 'trocken*, aflluiosemnu'
'nicht vertrocknend'; phlv. /<*^Ä;, /usklh^ /ösTnUän
(Bund.)-); ;rösaA; 'Ähre' (Bund.); ai. güska-, güsyati,
skr. gösa-.
kurd. LW. hüsk; afy. vud; oss. /tisk, ba/ussin (311
und Seite 141); bei. husay 'trocknen, austrocknen (160)
(LW?); wa/. vesk,
np, /uskar {/usk ärd, Vullers, 756, vergl. dial. ör,
oben No. 13), arab. LW. x^iskar 'Mehl', phlv. /nsk[a]r
V
(vd. 6 (9) Gl., Say. näsäy. 2, 35). Vergl. de Lagarde,
Semitica 1,41, Nöldeke, ZDMG. 32, 408; de Lagarde
*J Phlv. ;(Osak (Sternbild, Bund.); kurd. t*st, vasi^ krisl; afy. vazai;
bei LW. hösay, d. hösay (100).
2) Vd. 5 (43) (44) steht zwei Mal xösinUan,
=== HRN printed 109
-- 109 -
will auch np. /äsdk (jüd.-pers. T^^Z, Is. 7, 24) heran-
ziehen.
490. xiSm, xesm *Zorn*.
aw. aesma- 'Zorn*; phlv. /ism, x(h^fi^'
491. yi^eSTn 'bläulich, blauschwarz'; vergl. x^sisar (äähn. I,
157 Vers 510).
aw. a/saena- (Darmesteter, Et. ir. II, 53); phlv.
/asTn (Jamaspji, Pahlv. Dict. II, 421; falsch asgun,
asTu, 241), ;^ai;fm« oder axsin(?), vd. 22 (12).
kurd. stn, heslu 'blau ; afy. s7n bezw. xtn; oss. ä/sinäg
'Taube (46; vergl. Hübschmann, ZDMG. 38, 427/8);
sar. xoin, siyn. soin 'blau, yidg. ayßin (Tomaschek,
BB. VII, 204).
492. lele {jule) 'Wunde, Spitzes; Geschwätz', /ehden,
aw. hareöis; phlv. havak bezw. yarah^ vd. 2 (89).
Die Etymologie stammt von West (PPGl.s. vJialeh);
die Bedeutung der aw. und mittelp. Worte ist unsicher,
ebenso die Grundbedeutung des neupersischen. Im Men.
fasst West päzJiala als 'foolish, silly'. de Lagarde,
Beitr. z. altb. Lex. 38 wollte aw. /"ara- * Wunde' ver-
gleichen.
493. %ufn^ ;^Mw/;, yiimh Topf, Krug , /umre (HIOID, Is. 13, 12).
aw. /umba- *Topf ; phlv. yurnb*^ ai. Jcmnhhd',
kurd. LW. /um: bei. kumb, n. fftimh 'Teich, Pfuhl;
mit Wasser gefüllte Vertiefung im Felsgestein* (204);
wa/. Imbun,
494. fmkde 'Gelächter, ymdtden.
phlv. /andlta^i, yandak (PPGl.).
kurd. kenin 'lachen' ; bei. kandag, n. Uanday, yanday,
LW.') handag (186); wa/. känd-am, sar. söwrf-am (?).
oss. d. ;^odww, t. ;^wd/w (303) scheint hiervon ge-
trennt werden zu müssen und zu [/^svad- zu gehören.
Oder ist doch Urverwandtschaft vorhanden?
ffindeq 'Graben' siehe s. v. kenden (No. 869).
») Vergl. Bartholomae, ZDMG. 44, 550.
I
=== HRN printed 110
— 110 —
495. lym 'Schlaf, /ahtdefK
Kä§. ;^öw?[es; hevoft 'schlafen*.
aw. /'a/wa- *Schlaf; phlv. /*'äÄ; ai. svdpiw-; arm.
^un (H. No. 295).
kurd. /evii, /evin; af/. LW. yöb; bei. ^?a/>, n. väir
(410).
496. x'^^^ 'leicht, gerade; niedrig, verächtlich', x^^ärT,
aw. /'ad-ra- (Geldner, KZ. 25, 478, Studien I, 17
folgg. ; Darm est eter. Et. ir. II, 189)'); phlv. /"är, nur
in der Bedeutung 'leicht', /"änha *leichtlich' (Sa le-
rn an n, Mel. asiat. IX, 234).
LW. kurd. /(^r; afy. /'är; bei. vär (290).
Die Bedeutung 'niedrig, verächtlich' ist erst neu-
persisch.
497. i^äfiten 'wünschen, wollen, Praes. /"ähem, /"äliis,
/"äste 'Besitz'.
ai. l/^soad-, svädati 'sich schmecken lassen, Gefallen
finden*, svädate; gr. rjdoftat. Vergl. np. /iväi (No. 502).
phlv. yyastan 'wollen, wünschen', /^ah(i)§ff, x^stär,
y^astak 'Besitztum' etc.; kurd. /^dsthi , ;jfMSfni; bei.
vergl. västa 'für "(413).
498. x^äW/ 'Tischdecke; Tisch (gedeckter)'.
aw. /^'^aini' 'Teppich, Überzug, Decke',
kurd. LW. /an; af/. /^än; bei. n. vän 'Platte, Teller'
(289).
Geldner, Studien I, 17/8.
499. yiyänden Vufen, lesen etc.', /emden, /unlde, /unyä
'Musik, /unyäyer,
aw. l/";^^«;/- in /^anaf.ca/ra- ('klirrend'); phlv.
X'^äntan, /untt (GF.) ; ai. [/^svan-, sodnati 'tönen'.
kurd. y^ändin^ /ündin 'lesen; oss. d. /önim, i. xöJiin
'nennen , heissen , rufen , einladen' (305) ; bei. vänag,
n. vanay, vänganay 'lesen, recitiren, studiren' (412);
wa;f. ^an-am 'reden, sagen, sprechen'.
*) Sahn. I, 170 Vers 745 steht np. j^^är direkt im Gegensfttz zu
(hfsvär, wie im Awesta '^^äSra- zu (Inzä^ra-,
```


## [2026-09-14T03:11:04.591Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"xalidan\\|/;alUan\\|xale\\|/^ali\\|xâlidan\" HRN.txt | head -20; echo \"-- xab\"; grep -n \"x\\^ab \\|x\\^ab,\\|'Schlaf'\" HRN.txt | head -20"
}
```


### [2026-09-14T03:11:04.661Z] TOOL RESULT

```
-- xab
```


## [2026-09-14T03:11:26.010Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in (688,689,690):\n    print(\"=== IEC leaf\",leaf)\n    print(pages[leaf][:2500])\nEOF"
}
```


## [2026-09-14T03:11:27.497Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"swerdam\\|sweran\\|swer-\\|suer-\" IEC.txt | head -30"
}
```


### [2026-09-14T03:11:27.733Z] TOOL RESULT

```
=== IEC leaf 688
n Skt., OCS & Li.; -urtt-, -urst- in Skt. & Srb.
(song-, see seng-)
songh- ‘reaping, crop’; songhio, songheio ‘reap’. See sengh-, & cf. segh- Arm. hundzk, s. id.; hndzem, v. id. MHG sange, wf. ‘sheaf. Cf. (in sense of “bind, con- strict’? probably) Per. hanjam, v. “torture, af- flict; OE sengen, id.
songuhos (prob. *som-$uhos, see $uhon-,
1247
£uhuo) “noise, sound, voice’. WP, II, 496 Skt. cf. sam-hvaye, mp. “call out, shout to- gether’; Tokh. cf. sunk ‘throat’ (?); Gk. omphé, f. voice: Go. saggws, m. ‘song, music, reci- tal'; MHG sanc, gs: sanges, sm. & n. id.; OE sang, m., ON songr, gs: songs, pl. -var, m. id.; OCS cf. sü-zov9, -zvati, v. ‘summon’; R so- Zyv, m. ‘summons’
sont- (sontios, sonts, esonts, esnts) 'being; real, true, good, right; essence’ Cf. es- and extns. Skt. santyah ‘bountiful’; sat, asát, pres. p. ‘being’; Av. hás, acc. sg: hofitom, adj. ‘real, actual; haft, adj. ‘existing’; Arm. inc ‘thing’; Luvian, cf. Santas ( king or :god"); Gk. ousia, f. ‘essence, nature’; sunousía, f. ‘company’; On, gs: óntos, Aeol. eis gs: éntos, pres. p. ‘being’; Alb. gjå, gs: gjáni, m. ‘thing, matter’; Lat. ens, gs: entis, pres. part. and n. ‘being’ beside sons, gs: sontis, adj. ‘guilty’; Ir. sonn-, cpds. *truly-, very-' beside sonnta, inv. adj. ‘bold’; Go. *sanpa, f. ‘manner’ (misspelt as 'saupa"); OE sop ‘true; truth’; OFris. soth, s. ‘share, lot’; ON sannr ‘true; truth’; MIr. sond, sonn, m. (2) ‘hero’; Ir. son, m. ‘sake; ability’; OCS sọštije, n. “essence, reality’; sọštaja, f. (“money”, lit. ‘the necessary’); Srb. sušti, adj. ‘real’; R suščij, wd Blg. sást, săščij, adj. ‘the same’; OCS sẹ and sọ, sy, f: sọšta, pt. ‘being’; Ukr. suti, f. ‘substance’; OLi. sant, Li. esant, pt. ‘being’
sopos, à, ios (sopió(n)) (?) ‘stick, cane, rod, penis”. Cf. sap- Skt. (ambig.) sapab, m. (penis. Cf. EB: DELG:Príápos for speculations), Lat. cf. SOpiO, gs: -ionis, m. ‘penis’; ON sef, n. ‘reed’; Big. sop, m. ‘pipe’; OCS sopli, m. ‘flute’ be- side sopuxŭ, m. ‘reed’; sopotü, m. ‘pipe’
soqu- (1), soqueio ‘follow’. Cf. sequ- (1) Myc. cf. oqa- ‘household, retinue’; Gk. (de- nom.) opázō, v. ‘pursue’ beside a-osséð, v. (help, if fr. sm-°); Ir. soichim, v. ‘bestow; reach’; OCS po-sočọ, -sočiti, v. “extend, point out’; Blg. sòča, v. ‘point out
soqu- (2), soquió, soqu-nu-mi ‘utter, declare, pronounce, damn’. WP II, 479. Cf. sequ- (2) Gk. cf. ópis, gs: -idos, f. ‘divine revenge’; Umb. cf. sukatu “let him declare’; Br. hopa,
sont- (sontios, sonts, esonts, esnts) — soquos, à
20
25
30
35
40
4
=== IEC leaf 689
��; OCS sokü, R. Srb. sok, m. “juice, sap’; Li. sakai, m. pl. ‘pitch, gum, resin’; OPr. sackis, id.
soquos, is, à (2) ‘utterance, declaration; ut- terer, denouncer'. WP II, 479. Cf. sequ- (2) and sequ- (2) Gk. ons gs: -idos, f. ‘vengeance’; Br. hop, pl. u, m. ‘cal’; OCS sokü, m. ‘accuser, plain- tiff; Srb. sók, m. 'denouncer'; Li. sakà, f. legend, tale’; cf. uZz-sakai, pl. “marriage banns'; (oxytonic prototype in) MHG sage, sf. ‘speech, rumour’; ON saga, f. ‘tale, saga"; E saw “tale”
soquos, à (3) “follower; following'. Cf. so- quios, soqu- (1) & sequ- (1) Alb. gjah, m. ‘prey’; OCz. sok, m. ‘rival’; Big. cf. po-soka, f. ‘direction’; Li. cf. sakùs, adj. *well-orientated'; péd-sakas, m. ‘track’
1249
soqusos “following, accompaniment, com-
panion, tracker, track, procedure”. Cf. sequ- (1), soqu- (1), etc. Skt. sakkah, sakkih, m. ‘companion’; Av. haxa, nom. sg. m., pl: haxaya, id.; Ober haxa-, cpds. id.; Gk. ópson, n. 'food eaten 'cum pane"; cf. opúō and opüio, v. “marry” beside a-Ossæð, v. ‘help’; Lat. cf. socius, m. 'com- panion, ally; OS seg, i-st., OE secg, ON seggr, pl. -ir, m. ‘man, warrior’ (fr. *soquís); OCz. cf. sok, m. ‘rival’. Here also Av. haxo, m. ‘sole of foot’; Arm. ak, Let, leg’; Phryg. (DW?) sükhos, m. “sandal; Lat. (LCW?) soccus, gs: A. m. ‘shoe, sandal’
_soqutos, is, cf. sequ- (1) & soqu- (1)
Olr. cf. sochuide, f. ‘crowd, mass’; (Ukr. cf. sokotyty, v. ‘watch’. Here?)
(sórb- ‘sup’, etc. Cf. srb-, surb- (surbh-) and WP II, 204. Var: srób-, sreb- in Li. All onomatopoeic. Thus in Alb. gjerb, v. id.; gjerbé, f. “leak, droplet’)
sorbhos "a fish? (?) “perch, bass, roach’ or sim. See Supt: S Gk. orphós, Attic: orphós, m. Cperch, bass? or sim.); Sw. sarv, m. ‘roach’
sorgh- (?)
Icel. sarga, v. (1) ‘hack’; Sw. sarga, v. ‘wound, graze, têar’; OCS sragü, adj. “awfuP. (Hitt. sarkus, adj. = ‘mighty, glorious’ or sim.) sorguhð ‘watch, observe, sleuth, pester’. (Evidence ambig.). Cf. WP II, 529 Hitt. sarkumi, v. ‘equip myself”; sarikuwas, s. (equipment? or “armed soldier”); Ir. suir- ghim, v. ‘woo’; (Go. sarwa, npl. ‘armour’; OE searu, searo, n. ‘craft, device’); Li. sargùs, adj. “watchfuP; Latv. sargs, m., sardze, f. ‘watch’; sargu, inf: sargāt (sic) ‘watch’. (Li. sarginti, inf. ‘make ill’ is factitive to type ser- guhō, q. v.). For Gmc. (ambig.) see soruos (1) sormos (sormonos, sormot-) ‘glum, gloomy, downcast, shamed'. Gk. ambig. cf. suorm- Cf. Gk. hormaíno, v. ‘sulk’ ?; Hes. hormanós, adj. ‘saturnine’?; OCS sramü, m. ‘shame’; sraméjo, čti, v. “be ashamed
=== IEC leaf 690
�there’; Gk. hó, hé, def. art. beside hos, hé, rel. pron.; OLat. sum ‘him’, sam ‘her’; SOS, sàs, pl. ‘them’; (Sard. su, sa, def. art. prob. fr. ipse); MIr. so ‘this; these’; cf. Ir. so-nn (‘here’, cf. Arm. ho-n ‘there’); Go. sa, sð, mf. ‘thi; ON sá, sú “that; the’. Extn. in Gk. hoíos, hoia, pn. ((such?. Ambig. cf. ios-); Av. hoyo *this'; Alb. ay, f: ajó “he, she’
sós- ‘flaccid, limp, tired; tire’. (also: *pen- dant" ?) Du. soes, m. ‘drowsiness’; soezen, v. *drowse'; Li. suosiu, suósti, v. tr. ‘tire, bore’; suosà, f. ‘trouble, nuisance’; suoslüs, adj. 'importu- nate’; cf. (?) Skt. sasna, f. ‘dewlap’; Srb. (?) sasa, f. ‘anemone’; cf. Cz. Pol. sasanka, id.
sotios “true, right’. Cf sntios, sontios, esnt-, snt-. (Indo-Iran. ambig.) Skt. satyáh, id.; Av. haigyo, id.; Ober hašiya-, id.; Gk. hósios, id.; cf. Olr. uisse, comparat: uissiu, adv. id. (phonol. uncertain); ON saór (2), id.; Lat. cf. (?) sos-, in sos-pes, -pitis, OLat. sis-pes (Fest.) ‘safe and sound’
1251
sough- (sougho; soughos, à, iə) ‘guard, watch, care’. Cf. WP IL, 472 Arm. hogam, v. id.; hog, o-st. id.; OCS cf. pro-sugü, m. “fitness, aptness'; pro-suZinü, adj. ‘suitable’; R cf. do-sug, m. ‘leisure’; Li. saugüs, adj. ^watchful; safe’; saugà, f. ‘safety, protection’; OLi. sáugmi, mod. sáugoju, oti, v. ‘save, protect’; Latv. saudze, f. ‘rescue; care’; saudzēju, ēt, v. ‘spare’
soutos, iə, us ‘surge, seethe; surging, boil- ing’. Cf. seuto, ið Skt. sótuh, m. ‘soma-pressing; soma-libation'; Go. saups, m. ‘sacrificial offering’; MHG sot; MHG sot gs: sodes, sm. & n. “boiling, brew'; OE (queried) seaóa, m. ‘heartburn’; cf. G Sod-brennen, id.; OE séap, m. ‘spring, sour- ce’; ON seyðir, m. pl. ‘cooking-fire’; Pol. suty, adj. 'abundant' ; Ukr. sutyj, id.; Latv. saute, f. 'fomentation, scalding, steeping’; Li. cf. siau- tis, gs: -Cio, m. ‘squall’ beside (z-gde) siütis, gs: -Cio, m. ‘rage’
spadha *lath, spatula, spade’. WP II, 653 Gk. spáthe, f. “blade, weaver's reed; MHG spate, OE spadu, f.; Du. spade, f.; ON spaói, m., G Spaten, wm., Sw. spade, wm. ‘spade’
spagó (sphago), ið “break out, erupt’ Gk. spházo & sphátto, v. ‘cut, slay’; MHG spachen, wv. tr. ‘crack, burst’; G cf. Spach, m. ‘chip’; spachern, v. ‘crack open, get chap- ped”. (Isophones: Arm. pakem, v. ‘shut, fas- ten’; pak, i, iv ‘closure’; ON spakr, spak- ‘gen- tle’: Sw. spácka, v. ‘cram’)
spaið (spanið) ‘stretch, force, cram’. Cf. spanos Arm. cf. hy-panam, aor: -paçi, v. ‘get crammed’ (if fr. *pul-9); Gk. spáð, v. ‘stretch; skin’; cf. spátos “skin” and
```


### [2026-09-14T03:11:27.783Z] TOOL RESULT

```
6561:iusuer- (iuuer-), poss. adj. cf. ius, iusme- Olr. for, far ‘your’; Go. izwar, pl. id., OHG iuwér, iuwar, iuér; OE Gower Cf. variant in OS euwa, iuwa; Du. uw; Fris. jou, id.
17979:suer- (1) *weigh down, hang'. (Long-gde: suér-). WP 1,264 Oss. cf. xársun, Iron. xássín, v. ((1) ‘carry’, fr. *suersKO); Gk. cf. a-eiro, v. ‘raise’ (fr. n-^); Alb. vjerr, aor: vora beside m-vjerr, m-vora, v. id. A “lever up; weigh; hang’; Go. (long-gde)
17981:suens- — suer-, on, -en (suor-, sur-)
17990:sweran, wv. ((respect', lit. ‘weigh, consider’, fr. swérs ‘honoured’, lit. weighty"); Li. sveriù, sveiti, aor: sveriau, v. ‘raise, lever up’; Latv. sveru, svert, tr. & intr. ‘weigh’. (Long-gde in) Av. xwairis, f. ‘blame’; Per. xwar, adj. “indi- gent; Go. swērs, adj. 'honoured', lit. ‘weighty’; MHG swaàr, swaere “painful, glum, heavy’; OE sw&r ‘heavy, dull, sad, sluggish, weak’; n. ‘heaviness’, etc.; Scots sweer, adj. “lazy, reluctant’; ON svárr, adj. “heavy, grave’. Cf. type *suermn- in Gk. hérma, n. ‘pivot; earring, necklace’ beside (o-gde) hórmos, m. ‘necklace’, lit. ‘pendant’; Alb. vjerré, f. "ver, sification’; beside i vjerré, adj. ‘sloping’; Li. svermuó, gs: -ens, m. “weight — on a scale’; (o-gde in) Alb. i várun, T i várur, adj. (hanging, fr. *suor-)
17991:suer- (2) (suor-) “call, declare, state, speak, utter’. WP II 527 Skt. svaràmi, v. ‘sound; sing’; Gk. érō, éromai, v. ‘ask’; eíro, v. (2) “say, speak, tell’; cf. eirén, gs: -énos, m. “youth of speaking-age in Spar- tan parliament; MHG swéren, sv. 6. ‘swear’; OE swerian, sv. 6. id.; (o-gde in) Cz. ne- svor-ny, adj. ‘quarrelsome’; (long o-gde. in) OCS, Cz. svarü, svár, m. *quarrel' beside OCS svara, f., svarjo, -iti se, id.; ON sverja, v. ‘swear’ (p. t. sór & svór beside svaróa, pp: svarinn) (*-e-; *-0-; *-o-), (long o-gde in) MHG swuor, sm. (oath, curse: OCS svarü). Am- biguously *-e-/ *-o- in Skt. svárah, m. ‘sound, voice’. Ambiguous initial in Gk. éris, f. ‘strife’, and ambig. vocalism in Sw. sorl, n. ‘din’; sorla, v. (*syerol-?)
17992:suer- (3) “harm, hurt, corrupt. See next Skt. svaràmi, v. (1) ‘blame’; Av. xwar-, v. “blame, injure’; xwairis, s. “abuse, blame"; Per. xware, s. ‘corruption, gangrene’; cf. xire, adj. ‘malignant’; MHG swérn, sv. “hurt; suppurate’
17993:suer-, -on, -en (suor-, sur-) (4) 'swelling, suppuration, gangrene, ulcer. Cf. suer- (3) above. Av. xwaro, m. *wound'; Per. xware, s. 'gan- grene; leprosy?’ beside re, adj. ‘malignant’; Oss. cf. xàlmag, xwálmag, s. ‘scab, wound’; W cf. chwaren, f. (“gland”, fr. *suoren-); chwa- rel, m. (“breast tumour’, fr. *suorel-); OHG swéro, wm., MHG swér(e), s. & wm. ‘ulcer’;
17996:suer- (5) “post, pole, pillar, stump’. Cf. suir-. (Lat. ambig.) Skt. sváruh, m. id.; Gk. cf. hermís, gs: hermí- nos, f. id.; Lat. (ambig.) surus (“bough, stake, palisade’, fr. *suer- as in vocalism of vulva: Gk. eiláo or fr. type *guelbh-, oe: vult ^wishes', fr. *uel-, cf. (alleged) OLi. pa-velt, id.; or fr. *suir- as in vocalism of subitus, see suidh-, pudeo, fr. *po- or *pod-, and *uid-, q.V.) (for sul-phur cf. suel-, pür-, and for mulgeo cf. melg-)
17997:suér- (1) “heavy, hanging”, etc. See suer- (1)
18003:(sueró, sueros, suér-, see suer- (1-4))
18006:suer- — suesriios, io (suesrios, io)
18015:OHG cf. swéro, m. (fpain, sickness’, but see suer- (4); LG cf. sarw ‘tart, sour, harsh’; (variant in) OCS srüxükü, adj. *'rough'. Cf. Kauros, süros, quser-
18159:suor- “heavy; weight Cf. suer-. O-gde in Hes. á-oros, m. "lever; Alb. i várur, adj. “hanging, dependent’; Li. svarüs, adj. “heavy, serious’; sváras, m. ‘pound’; svarà, f. weight
18163:suór-, long-grade form of suer- (2), q.v. WP II, 527 MHG swuor, sm. ‘oath, curse’; ON særa, v. ‘adjure’; OCS svarü, svara, mf. ('quarrel, and com. S1.); svarjo se, svariti se, v. id.
18165:suorm- (2) ‘pendant’. Cf. suer- (1), suor- Gk. hórmos, m. (1) ‘necklace’; Alb. i varém, adj. ‘hanging’; Li. cf. svarmuó, gs: eng, m. *weight; loading”
18180:surio ‘dangle, swing, sway”. Cf. suer-, suor- and suir-. (Gk. ambig.) Gk. aíro, v. (‘raise’. Associated with a-eíro, id. See suer-); Li. svyriu, Eti, v. intr. ‘dangle, hang’. Cf. also Gk. artáo, v. ‘hang’; Li. svirtis, f. 'swing-beam, bar, windlass’; araiós (2) ‘flimsy, weak’; Li. svirüs, adj. ‘flimsy, tottery'. (For Gk. araiós (1) “thin”, see ursios)
```


## [2026-09-14T03:11:37.223Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index containing line 17993\nidx=0\nff=0\nfor i,l in enumerate(lines,1):\n    ff+=l.count('\\f')\n    if i==17993:\n        print(\"leaf approx\",ff)\n        break\npages=t.split('\\f')\nprint(pages[ff][:60])\nimport re\nprint([m for m in re.findall(r'\\n1(3[0-9]{2})\\n', pages[ff])])\nprint(\"---- page text around:\")\np=pages[ff]\nj=p.find('suer-, -on, -en (suor-, sur-) (4)')\nprint(p[max(0,j-1500):j+900])\nEOF"
}
```


### [2026-09-14T03:11:38.361Z] TOOL RESULT

```
leaf approx 742
or *suepsK-); Lat. sopiO, Ire, v. Cu fr. *suep-); OE swefan,
['348', '349']
---- page text around:
“indi- gent; Go. swērs, adj. 'honoured', lit. ‘weighty’; MHG swaàr, swaere “painful, glum, heavy’; OE sw&r ‘heavy, dull, sad, sluggish, weak’; n. ‘heaviness’, etc.; Scots sweer, adj. “lazy, reluctant’; ON svárr, adj. “heavy, grave’. Cf. type *suermn- in Gk. hérma, n. ‘pivot; earring, necklace’ beside (o-gde) hórmos, m. ‘necklace’, lit. ‘pendant’; Alb. vjerré, f. "ver, sification’; beside i vjerré, adj. ‘sloping’; Li. svermuó, gs: -ens, m. “weight — on a scale’; (o-gde in) Alb. i várun, T i várur, adj. (hanging, fr. *suor-)
suer- (2) (suor-) “call, declare, state, speak, utter’. WP II 527 Skt. svaràmi, v. ‘sound; sing’; Gk. érō, éromai, v. ‘ask’; eíro, v. (2) “say, speak, tell’; cf. eirén, gs: -énos, m. “youth of speaking-age in Spar- tan parliament; MHG swéren, sv. 6. ‘swear’; OE swerian, sv. 6. id.; (o-gde in) Cz. ne- svor-ny, adj. ‘quarrelsome’; (long o-gde. in) OCS, Cz. svarü, svár, m. *quarrel' beside OCS svara, f., svarjo, -iti se, id.; ON sverja, v. ‘swear’ (p. t. sór & svór beside svaróa, pp: svarinn) (*-e-; *-0-; *-o-), (long o-gde in) MHG swuor, sm. (oath, curse: OCS svarü). Am- biguously *-e-/ *-o- in Skt. svárah, m. ‘sound, voice’. Ambiguous initial in Gk. éris, f. ‘strife’, and ambig. vocalism in Sw. sorl, n. ‘din’; sorla, v. (*syerol-?)
suer- (3) “harm, hurt, corrupt. See next Skt. svaràmi, v. (1) ‘blame’; Av. xwar-, v. “blame, injure’; xwairis, s. “abuse, blame"; Per. xware, s. ‘corruption, gangrene’; cf. xire, adj. ‘malignant’; MHG swérn, sv. “hurt; suppurate’
suer-, -on, -en (suor-, sur-) (4) 'swelling, suppuration, gangrene, ulcer. Cf. suer- (3) above. Av. xwaro, m. *wound'; Per. xware, s. 'gan- grene; leprosy?’ beside re, adj. ‘malignant’; Oss. cf. xàlmag, xwálmag, s. ‘scab, wound’; W cf. chwaren, f. (“gland”, fr. *suoren-); chwa- rel, m. (“breast tumour’, fr. *suorel-); OHG swéro, wm., MHG swér(e), s. & wm. ‘ulcer’;
1349
(Z-gde in) G Geschwür, id.
suer- (5) “post, pole, pillar, stump’. Cf. suir-. (Lat. ambig.) Skt. sváruh, m. id.; Gk. cf. hermís, gs: hermí- nos, f. id.; Lat. (ambig.) surus (“bough, stake, palisade’, fr. *suer- as in vocalism of vulva: Gk. eiláo or fr. type *guelbh-, oe: vult ^wishes', fr. *uel-, cf. (alleged) OLi. pa-velt, id.; or fr. *suir- as in vocalism of subitus, see suidh-, pudeo, fr. *po- or *pod-, and *uid-, q.V.) (for sul-phur cf. suel-, pür-, and for mulgeo cf. melg-)
suér- (1) “heavy, hanging”, etc. See suer- (1
```


## [2026-09-14T03:11:45.660Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[741][-1800:])\nprint(\"@@@@ LEAF742 START\")\nprint(pages[742][:1500])\nEOF"
}
```


### [2026-09-14T03:11:46.858Z] TOOL RESULT

```
. swingel, f. “whip, lash, blow'; E cf. swingle-tree (of cart); Du. cf. zwingel, m. 'flax-beater' beside (o-gde) zwengel, m. “handle, arm’
suengh- (suongh-) (2) (?) ‘thin’. See next. (Irish ambig.) Olr. seng, Ir. seang, adj. ‘thin, slim, lean’; ON svangr (0o-gde), id.
suenĝð, ið ‘squeeze, constrain, torture; toil, falter, waver’. Cf. WP II, 526 Skt. svañje, sváje, mp. ‘clasp, embrace’; MIr. & Ir. seangaim, v. ‘press, squeeze; reduce’; intr. (‘waste away’. 2 wds? cf. suengh- (2)); OE swincan, sv. 1. ‘toil, languish’; swinc, n.
 
1347
‘hardship’; Sw. svinka, v. ‘falter, waver’
suens- extn. of type suen- (1) q. v. Olr. séis, f. (“music”), perh. fr. *suns-); OE swinsian, v. “sound, ring”
suent- ‘dash, rush,  swish, (Onomat.). (Irish variant: sunt-) Gk. (ambig.) éntos, usu. pl. éntea, n. *fighting- gear”; Lat. cf. sonticus, adj. (harmful; epilep- tic, cf. G Schwind-sucht); Go. swinps ‘strong’; MHG swint, swinde, adj. (strong, quick, violent, sharp, evil, dangerous; OE swip “strong, severe, violent; right-hand’; swidan, sv. 1. “strengthen; attack’; Mir séitim, sétim, v. ‘blow; flow, gush’; ON svinnr 'swift; shrewd'; (mod. also 'stingy")
suepnið ‘dream’. See next, and cf. suepó, supnos Lat. somnio, are, denom. id.; OE swefnian, v. id.
suepnos, om 'sleep, dream. Cf. supnos and next. WP II, 523 Skt. svápnah, id.; Av. xwafno, wd: adj. "dor, mant; Per. xwab, as Skt.; Lat. somnus, 1, m. ‘sleep’; somnium, n. ‘dream’; MHG swép, gs: swébes, sm., OE swefn, n. ‘sleep’; ON cf. sofa, p. t. svaf, v. ‘sleep’; sofna, v. ‘fall asleep’; Sw. somna, v. “sleep”
suepo, ið (1) “be drowsy, sleep’; suopeio ‘tull’. WP II, 523 Skt. svápami, svápimi, v. ‘sleep’; Av. xwap-, v. id.; Per. xuftan, inf. beside xabam, xabidan, v. id.; (variant in) Per. xuspidan, Av. xwafs-, Oss. xüssin, inf. id. (fr. *sueps- 
@@@@ LEAF742 START
or *suepsK-); Lat. sopiO, Ire, v. Cu fr. *suep-); OE swefan, sv. 5. “sleep; cease’; ON sofa, p. t. svaf, id.; Sw. sova, id.; cf. (o-gde) OHG swebjan, swebben, v. lul; ON (e-gde) svæfa, inf. id.
suepó, io (2) ‘sway, hover’. WP II, 524 Lat. cf. sopio, onis, m. ‘penis’; OHG swébon, MHG swében, wv. ‘dangle, sway, hover’; MHG swébe, sf. ‘suspense’; OCS svepljo se, svepiti se, as OHG
suer- (1) *weigh down, hang'. (Long-gde: suér-). WP 1,264 Oss. cf. xársun, Iron. xássín, v. ((1) ‘carry’, fr. *suersKO); Gk. cf. a-eiro, v. ‘raise’ (fr. n-^); Alb. vjerr, aor: vora beside m-vjerr, m-vora, v. id. A “lever up; weigh; hang’; Go. (long-gde)
hurtle'.
suens- — suer-, on, -en (suor-, sur-)
10
20
25
30
35
40
45
1348
sweran, wv. ((respect', lit. ‘weigh, consider’, fr. swérs ‘honoured’, lit. weighty"); Li. sveriù, sveiti, aor: sveriau, v. ‘raise, lever up’; Latv. sveru, svert, tr. & intr. ‘weigh’. (Long-gde in) Av. xwairis, f. ‘blame’; Per. xwar, adj. “indi- gent; Go. swērs, adj. 'honoured', lit. ‘weighty’; MHG swaàr, swaere “painful, glum, heavy’; OE sw&r ‘heavy, dull, sad, sluggish, weak’; n. ‘heaviness’, etc.; Scots sweer, adj. “lazy, reluctant’; ON svárr, adj. “heavy, grave’. Cf. type *suermn- in Gk. hérma, n. ‘pivot; earring, necklace’ beside (o-gde) hórmos, m. ‘necklace’, lit. ‘pendant’; Alb. vjerré, f. "ver, sification’; beside i vjerré, adj. ‘sloping’; Li. svermuó, gs: -ens, m. “weight — on a scale’; (o-gde in) Alb. i várun, T i várur, adj. (hanging, fr. *suor-)
suer- (2) (suor-) “call,
```


## [2026-09-14T03:11:47.440Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in (787,788,789,790):\n    p=pages[leaf]\n    if 'sword' in p or 'swerd' in p:\n        print(\"=== leaf\",leaf)\n        i=p.find('sword,')\n        print(p[max(0,i-200):i+1200])\nEOF"
}
```


### [2026-09-14T03:11:48.570Z] TOOL RESULT

```
=== leaf 787
,  n.  pi.,  a  long  gaiter.  —  Compound¬ ed  of  spatter  and  dash.  Cp.  spat,  ‘short  gaiter’, spatula,  n.,  an  instrument  resembling  a  knife.  — L.,  lit.  ‘a  broad  piece’,  dimin.  of  spat(h)a,  ‘a broad  tool  or  weapon',  fr.  Gk.  ott-xHt;.  See spathe  and  -ule.
Derivatives:  spatul-ar,  spatul-ate,  adjs. spatule,  n.,  spatula.  —  F.,  fr.  L.  spatula.  See  prec. word.
spatuliform,  adj.  —  See  spatula  and  form,  n. spavin,  n.,  disease  of  the  hock  joint  of  thi  horse.
—  ME.  spaveyne,  fr.  OF.  esparvin  (F.  eparviit), prob.  fr.  Frankish  *sparwun,  acc.  of  *sparo,  fr. Teut.  *sparwo,  ‘sparrow’,  which  is  rel.  to  OHG. sparo,  of  s.m.,  hence  lit.  ‘sparrowlike  disease’; so  called  from  the  jerky  motion  of  a  spavined horse  resembling  the  hopping  of  a  sparrow. Cp.  It.  spavenio,  Sp.  esparavan.  Port,  esparavao, ‘spavin’,  and  see  sparrow.
Derivative:  spuvin-ed,  adj. spawn,  tr.  v.,  to  produce  or  deposit  (eggs  or spawn);  intr.  v.,  to  produce  or  deposit  spawn.
—  ME.  spawnen,  for  *spaunden,  fr,  AF.  espaun-
dre,  corresponding  to  OF.  espandre  (F.  epan- dre),  ‘to  spread,  scatter,  sh
```


## [2026-09-14T03:11:56.001Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^sword,\" KLN_1966.txt KLN_1971.txt | head; echo \"-- hypnosis\"; grep -n \"^hypnosis,\\|^hypnotism,\\|^hypno\" KLN_1966.txt | head"
}
```


### [2026-09-14T03:11:56.080Z] TOOL RESULT

```
KLN_1971.txt:238606:sword, n. — ME. swerd. fr. OE. sweord , swurd, 
KLN_1971.txt:238607:sword, rel. to t)S., OFris. swerd , ON. sverd, 
KLN_1966.txt:37760:sword,  n.  —  ME.  swerd.  fr.  OE.  sweord,  swurd, sword,  rel.  to  OS.,  OFris.  swerd,  ON.  sverd.
-- hypnosis
18437:hypnology
18479:hypnoid,  adj. ,  resembl  ing  hypnosis. — Compound¬ ed  of  bypn-  and  Gk.  -oEiSfj?,  ‘like’,  fr.  eISo?, ‘form,  shape’.  See  -oid.
18480:hypnology,  n.,  the  study  of  (hypnotic)  sleep.  — Coined  by  James  Braid  (1795-1861)  fr.  hypno-
18481:hypnophobia
18485:hypnophobia,  n.,  a  morbid  fear  of  falling  asleep. —  Compounded  of  hypno-  and  Gk.  -<po(ita, ‘fear  of’,  fr.  <po$o<;,  ‘fear’.  See  -phobia.
18487:hypnosis,  n.  —  ModL.,  coined  fr.  Gk.  utcvouv, ‘to  put  to  sleep’,  and  suff.  -osis.  Gk.  ukvouv derives  fr.  urcvoc;,  ‘sleep’.  See  hypno-  and  cp. hypnotism.
18488:hypnotic,  adj.  —  L.  hypnoticus,  fr.  Gk.  6irvomx6s, ‘inclined  to  sleep’,  fr.  u7rvouv,  ‘to  put  to  sleep’, fr.  timioi ;,  ‘sleep’.  See  hypno-  and  -otic. Derivatives:  hypnotic,  n.,  hypnotic-al-ly,  adv.
18489:hypnotism,  n.  —  Coined  by  James  Braid  of Manchester  (1795-1861)  fr.  hypnotic  and  suff. -ism.  Cp.  hypnosis.
18490:hypnotist,  n.  —  Coined  fr.  hypnotic  and  suff.  -ist. Derivative:  hypnotist-ic,  adj.
18491:hypnotize,  tr.  v,  —  Coined  fr.  hypnotic  and  sufT. -ize.
```


## [2026-09-14T03:12:00.218Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '37755,37775p' KLN_1966.txt; echo \"@@@ hypno-\"; sed -n '18470,18480p' KLN_1966.txt"
}
```


### [2026-09-14T03:12:00.307Z] TOOL RESULT

```
switch, n., a  flexible  rod.  —  MDu.  swijch,  ‘scourge, whip',  rel.  to  OHG,  MHG.  zwee,  ‘wooden peg’,  G.  Zweck,  ‘aim,  design’  (orig.  ‘peg  in  the target’),  MHG.  zwic,  G.  Zwick,  ‘wooden  peg'. Derivatives:  switch,  tr.  and  intr.  v.,  swilch-ed, adj.,  switch-er,  n.,  switch-y,  adj.
Switzer,  n.,  a  Swiss  (archaic).  —  MHG.,  fr. Swilz  (whence  G.  Schweiz),  ‘Switzerland’. Switzerland  was  named  after  Schwyz,  one  of  its ancient  cantons.  Cp.  Swiss.  For  the  ending  see suff.  -er.
swivel,  n.  —  ME.  swivell,  rel.  to  OE.  swifan,  ‘to move  in  a  course,  sweep'.  See  sweep,  v.,  and  cp. words  there  referred  to.
swollen,  pp.  of  swell.  —  ME.,  fr.  OE.  geswollen, pp.  of  swellan.  See  swell, swoon,  intr.  v.  —  ME.  swowenen,  swuwnen,  back formation  fr.  swowening,  ‘swooning’,  fr.  OE. geswogen,  ‘in  a  swoon’,  pp.  of  a  lost  verb.  Cp. LG.  swogen,  ‘to  sigh',  and  sough.
Derivatives:  swoon,  n.,  swoon-ing-ly,  adv. swoop,  tr.  and  intr.  v.,  to  sweep  down.  —  ME. swopen,  fr.  OE.  swapan,  ‘to  sweep,  rush’,  rel.  to ME.  swepen,  ‘to  sweep,  rush’,  rel.  to  ME. swepen,  ‘to  sweep,  move  quickly’.  See  sweep. Derivatives:  swoop,  n.,  swoo-per,  n. swoop,  tr.  and  intr.  v.,  to  swap.  —  A  var.  of  swap. Derivative:  swoop,  n.
sword,  n.  —  ME.  swerd.  fr.  OE.  sweord,  swurd, sword,  rel.  to  OS.,  OFris.  swerd,  ON.  sverd.
1554
Dan.  sverd,  Swed.  sveird,  MDu.  swaert,  Du. zwaard,  OHG.,  MHG.  swert,  G.  Schwert,  fr. Teut.  *swerda,  lit.  ‘the  cutting  weapon’,  formed fr.  I.-E.  base  *swer-,  ‘to  press,  torment’,  orig.  ‘to cut’,  and  Teut.  suff.  -da.  Avestic  xvara,  ‘wound’, OI.  svar-,  ‘to  torment',  are  from  the  same  base. For  the  sense  developmeent  of  OE.  sweord,  etc., cp.  OI.  krpdnah  ‘sword’,  lit.  ‘a  cutting  weapon’, fr.  I.-E.  base  *(s)qerp-,  ‘to  cut’  (see  harvest). Derivatives:  sword,  v.,  sword-less,  adj. swore,  past  tense  of  swear.  —  ME.  swor,  fr.  OE. swor,  past  tense  of  swerian.  See  swear, sworn,  pp.  of  swear.  —  ME.  sworen,  fr.  OE. sworen,  pp.  of  swerian.  See  swear, swot,  n.,  hard  work,  toil  (slang).  —  Avar,  of  sweat.
Derivative:  swot,  intr.  v. swum,  pp.  of  swim.  —  ME.  swummen,  fr.  OE.  ge- swummen,  pp.  of  swimman.  See  swim,  ‘to  move in  water’.
swung,  past  tense  and  pp.  of  swing.  —  ME.  swang, swong,  past  tense,  resp.  sw ungen,  pp.  of  swingen, fr.  OE.  swang,  past  tense,  resp.  geswungen,  pp. of  swingan.  See  swing.
sy-,  pref.  —  Gk.  ou-,  form  of  ouv-,  before  a  fol¬ lowed  by  a  consonant  and  before  See  syn-. syagush,  n.,  the  caracal.  —  Pers.-Hind.  siyah- gosh,  lit.  ‘black  ear',  fr.  siyah,  ‘black’,  and  gosh, ‘ear’.  The  first  element  is  rel.  to  OI.  syamah, Avestic  sama,  ‘black’,  and  cogn.  with  L.  cimex, ‘a  bug’,  lit.  ‘the  dark-brown  insect’ ;  see  cimex. The  second  element  derives  fr.  OPers.  gausha-, ModPers.  gosh,  ‘ear’,  which  is  rel.  to  Avestic gaosho-,  ‘ear’,  and  to  OI.  ghosah,  ‘noise’. Sybarite,  n.,  and  adj.  —  L.  Sy  bar  it  a,  fr.  Gk. Su(iapf-nf]?,  inhabitant  of  Sybaris,  fr.  EuflapK;, name  of  a  Greek  town  in  southern  Italy  (now called  Sibari).  The  inhabitants  of  Sybaris  were famous  for  their  luxury,  whence  Sybarite  came to  denote  a  luxurious  person.  —  For  the  ending see  subst.  suff.  -ite.
Sybaritic,  also  Sybaritical,  adj.  —  L.  Sybariticus,- fr.  Gk.  SuPapTrixi)?,  fr.  DupapfT7];.  See  prec. word  and  -ic,  resp.  also  -al.
Derivative:  Sybaritical-ly,  adv. sybotic,  adj.,  pertaining  to  a  swineherd.  —  Gk. ctuJJcotixoi;,  compounded  of  au;,  gen.  auos, ‘swine’,  and  the  stem  of  (3 oaxetv,  ‘to  feed’.  Gk. ctO;  is  a  collateral  form  of  up;  see  sow,  ‘female pig’.  For  the  second  element  see  botany,  for the  ending  see  adj.  suff.  -ic. sycamine,  n.,  mulberry.  —  L.  sycaminus,  fr.  Gk. auxapuvo;,  fr.  Phoen.  shiqmtn,  corresponding to  Heb.  shiqmim,  pi.  of  shiqmdh,  ‘mulberry’ ;  cp. Aram,  shiqma,  pi.  shiqmtn.  Cp.  also  next  word, sycamore,  sycomore,  n.,  1)  a  tree  of  Egypt  and Asia  Minor,  the  sycamore  of  the  Bible;  2)  a Eurasian  maple  tree;  3)  the  plane  tree.  —  ME., fr.  OF.  sicamor  (F.  sycomore),  dissimilated  fr. L.  sycomorus,  fr.  Gk.  auxoizopop.  For  the  first element  of  this  compound  word  see  prec.  word. The  second  element  is  identical  with  Gk.  p.£5pop, pLopop,  ‘mulberry’;  see  mulberry.
1555
syce,  n.,  an  Indian  groom.  —  Arab,  sa'is  (in vulgar  pronunciation  sayis),  ‘groom’,  prop, pres,  participle  of  the  verb  sdsa,  ‘he  adminis¬ tered’.
sycee,  n.,  ingots  of  silver.  —  Chin,  hsi-se,  ‘fine silk’.
sychnocarpous,  adj.,  bearing  fruit  for  several seasons  (bo/.)  —  Compounded  of  Gk.  tsoyybq,, ‘many,  frequent,  dense,  compact’,  and  xapmop, ‘fruit’.  The  first  element  is  of  uncertain  origin. For  the  second  element  see  carpel,  for  the  end¬ ing  see  suff.  -ous.
Sycon,  n.,  a  genus  of  sponges  (zool.)  —  ModL. Sycon,  fr.  Gk.  ouxov,  ‘fig’,  which  is  prob.  a loan  word  from  a  Mediterranean  language.  Cp. next  word  and  Busycon.
syeonium,  n.,  fleshy  fruit  with  the  ovaries  borne in  a  hollow  receptacle,  as  in  the  fig.  (bot.)  — ModL.,  fr.  Gk.  ouxov,  ‘fig’.  See  prec.  word, sycophancy,  n.  —  L.sycophantia,  fr.  Gk.  ouxo9av- xta,  fr.  auxotpdivTqs.  See  next  word  and  -cy. sycophant,  n.,  flatterer;  toady.  —  L.  sycophanta, fr.  Gk.  ooxo 9avT/)s,  ‘informer,  denouncer’,  lit. ‘fig  shower’,  fr.  ouxov,  ‘fig’,  and  -rfd.VTt)<;,  from the  stem  of  oaivELv,  ‘to  show’;  see  sycon  and phantasm.  Several  attempts  have  been  made  to explain  how  the  expression  ‘fig  shower’  came to  denote  an  informer  in  Greek,  but  they  all lack  probability.
Derivatives:  sycophantic  (q.v.),  sycophant-ish, adj.,  sycophant-ish-ly,  adv.,  sycophant-ism,  n., sycophant-ize,  intr.  v.,  sycophant-ry,  n. sycophantic,  adj.  —  Gk.  ouxo9avxix6?,  fr.
ouxo9dvT7)<;.  See  prec.  word  and  adj.  suff.  -ic. sycosis,  n.,  skin  disease  attacking  especially  the bearded  part  of  the  face.  —  Medical  L.,  fr.  Gk. ouxtoou;,  ‘ulcer  resembling  a  fig’,  formed  fr. ouxov,  ‘fig’,  with  suff.  -toon;.  See  Sycon  and -osis.
@@@ hypno-
—  Medical  L.,  formed  fr.  hyper-,  Gk.  octxeov, ooxouv,  ‘bone’  (see  osteo-),  and  suff.  -osis.  Cp. ostosis  and  words  there  referred  to.
hypersensitive,  adj.,  excessively  sensitive  (med.)
—  A  hybrid  coined  fr.  Gk.  (n£p  (see  hyper)  and sensitive,  a  word  of  Latin  origin.  The  correct form  would  be  supersensitive,  in  which  both elements  are  of  Latin  origin.
Derivative:  hypersensitive-ness,  n. hyperspace,  n.,  a  space  of  more  than  three  di¬ mensions.  — -  A  hybrid  coined  fr.  Gk.  (nep  (see hyper-)  and  space  (fr.  L.  spatium).  The  correct form  would  be  superspace,  in  which  both  ele¬ ments  are  of  Latin  origin, hypertrophy,  n.,  excessive  development  of  an organ  (med.)  —  Medical  L.  hypertrophia,  formed fr.  hyper-  and  Gk.  -xpocpla,  fr.  xpo<pf),  ‘food, nourishment’.  See  trophic  and  cp.  atrophy, dystrophy.
Derivatives:  hypertrophy,  intr.  v.,  hypertroph-ic , hypertrophi-ed,  adjs.
hypha,  n.,  one  of  the  threadlike  elements  in  the shallus  of  a  fungus  (bot.)  —  ModL.,  fr.  Gk. (cpfj,  ‘web’,  which  is  rel.  to  utpo?,  ‘web’,  (xpaivEiv, ‘to  weave’,  fr.  I.-E.  base  *webh-,  ‘to  weave’, whence  also  OE.  we  fan,  ‘to  weave’.  See  weave, hypheme,  n.,  a  hyphened  compound  word. Coined  fr.  hyph(en)  and  (phon)eme. hyphen,  n.,  a  short  line  (-)  joining  parts  of  a  word.
—  L.,  fr.  Gk.  ucpEv,  ‘together,  in  one,  as  a  single word’,  fr.  (tp‘  slv,  which  stands  for  (too  £u,  lit., ‘under  one’.  For  the  first  element  see  hypo-; for  h>  which  is  the  neut.  of  el?,  ‘one’,  see  heno-. Derivatives:  hyphen,  tr.  v.,  hyphen-ate,  tr.  v., adj.  and  n.,  hyphen-at-ed,  adj.,  hyphen-ic,  adj., hyphen-ism,  n.,  hyphen-ize,  tr.  v.,  hyphen-iz- ation,  n.
hypn-,  form  of  hypno-  before  a  vowel, hypnagogic,  adj.,  inducing  sleep.  —  Compounded of  hypn-,  Gk.  dtyu>y6;,  ‘leading’  (see  -agogue), and  suff.  -ic.
hypnic,  adj.,  inducing  sleep.  —  Gk.  (nvix(i;,  ‘per¬ taining  to  sleep’,  fr.  (nvop.  See  hypno-  and  -ic. Derivative:  hypnic,  n.,  a  soporific, hypno-,  before  a  vowel  hypn-,  combining  form meaning  ‘sleep’.  —  Gk.  (rovo-,  (nv-,  fr.  unvoi;, ‘sleep’,  which  stands  for  *sup-no-s  and  is  cogn. with  OI.  svapnah,  ‘sleep,  dream’,  L.  somnus  (for *swepnos  or  *swopnos),  ‘sleep’.  See  somnolent  and cp.  Hypnos.
hypnoid,  adj. ,  resembl  ing  hypnosis. — Compound¬ ed  of  bypn-  and  Gk.  -oEiSfj?,  ‘like’,  fr.  eISo?, ‘form,  shape’.  See  -oid.
hypnology,  n.,  the  study  of  (hypnotic)  sleep.  — Coined  by  James  Braid  (1795-1861)  fr.  hypno-
```


## [2026-09-14T03:12:01.704Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in (37760,18487):\n    ff=0\n    for i,l in enumerate(lines,1):\n        ff+=l.count('\\f')\n        if i==target:\n            print(target,\"leaf\",ff); break\nEOF"
}
```


### [2026-09-14T03:12:03.040Z] TOOL RESULT

```
37760 leaf 824
18487 leaf 408
```


## [2026-09-14T03:12:11.603Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^swep-\\|^swer-\\|^swep\\|^swer\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T03:12:11.675Z] TOOL RESULT

```
1051:swep-2. To throw, sling, cast. 1. O-grade form *swop- perhaps in Germanic variant expressive form *swabb- in Middle Dutch swabbe, mop, splash: swaB. 2. Suffixed zero-grade form *sup-d- in Latin dissipdre, to disperse (dis-, apart): DISSIPATE. [Pok. 2. swep- 1049.]
1052:swer-'. To speak, talk. O-grade form *swor- in: a. Ger- manic *swarjan in Old English swerian, to swear, pro- claim: SWEAR; b. Germanic “*and-swar6, “a swearing against,” “rebuttal” (*andi-, against; see ant-), in Old English andswaru, answer: ANSWER. [Pok. 1. swer- 1049.] swer-2. To buzz, whisper. Imitative root. I. O-grade form *swor-. 1. Suffixed form *swor-mo- in Germanic *swar- maz in Old English swearm, swarm: SWARM. 2. Germanic *swar- in Dutch zwirrelen, to whirl, akin to the Low German source of Middle English swyrl, eddy: SWIRL. II. Zero-grade form *sur-. 1. Suffixed form *sur-do- perhaps in: a. Latin surdus, deaf, mute: SORDINO, SOUR- DINE, SURD; b. Latin absurdus, discordant, away from the right sound, harsh (ab-, away; see apo-): ABSURD. 2. Reduplicated expressive form *su-surr- in Latin susur- rus, whisper: SUSURRATION. [Pok. 2. swer- 1049.] swer-3, Post, rod. Suffixed zero-grade form *sur-o- in Latin surus, branch: SURCULOSE. [Pok. 3. suer- 1050.] swer-4. To cut, pierce. Germanic *swerdam in Old Eng- lish sweord, sword, sword: sworD. [Pok. 4. suer- 1050.] swer-5. Also ser-. To lift, hang on the scale; heavy. Variant *ser- in suffixed lengthened-grade form *sér-yo- in Latin sérius, serious, grave: SERIOUS.
1053:swerbh-. To turn, wipe off. 1. Germanic *swerb- in Old English sweorfan, to file away, scour, polish: SWERVE. 2. O-grade form *sworbh- in Germanic *swarb- in Old Norse svarf, filings, akin to the Scandinavian source of swakF. [Pok. suerbh- 1050.]
1054:swergh-. To worry, be sick. Germanic *sorg- in Old English sorh, sorg, anxiety, sorrow: soRROW. [Pok. suergh- 1051.]
```


## [2026-09-14T03:12:15.875Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1048,1051p' AHD_watkins1985.txt"
}
```


### [2026-09-14T03:12:15.928Z] TOOL RESULT

```
syt-
swing, shake: SWINGE; b. Germanic variant *swank- in Middle High German swanken, to turn, swing: SWANK. 4. Uncertain preform in Norwegian swagga, to sway, akin to the Scandinavian source of swac. [Pok. sueng-, suenk- 1047.]
swento-. Healthy, strong. Zero-grade form *sunto- in Germanic *sunth- in Old English gesund, healthy (ge-, intensive prefix; see kom): SOUND?. [Pok. suento- 1048.] swep-'. To sleep. 1. Suffixed form *swep-os- in Latin sopor, a deep sleep: SOPOR; (SOPORIFIC). 2. Suffixed form *swep-no- in Latin somnus, sleep: SOMNI-, SOMNOLENT; INSOMNIA. 3. Suffixed zero-grade form *sup-no- in Greek hupnos, sleep: HYPNO-, HYPNOS, (HYPNOSIS), HYPNOTIC. [Pok. 1. swep- 1048.]
swep-2. To throw, sling, cast. 1. O-grade form *swop- perhaps in Germanic variant expressive form *swabb- in Middle Dutch swabbe, mop, splash: swaB. 2. Suffixed zero-grade form *sup-d- in Latin dissipdre, to disperse (dis-, apart): DISSIPATE. [Pok. 2. swep- 1049.]
```


## [2026-09-14T03:12:20.975Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"xwßn\\|xwbn\\|'wbs\\|ʾwβs\\|xwβn\" SOD.txt SOD_pages.txt | head -20; echo \"@@ dream\"; grep -n \"dream\" SOD.txt | head -30"
}
```


### [2026-09-14T03:12:21.049Z] TOOL RESULT

```
SOD.txt:80536:10710  xwbn   C  =»  xwpn- 
SOD.txt:80539:xupn  (xwbn)  =*YwPn~ 
SOD.txt:83382:11105  yxwbny'   C  =  y-,  +xwbny*  =»  xwpn- 
SOD_pages.txt:34757:10710 xwbn C =» xwpn-                                             King, Lord
SOD_pages.txt:34760:      xupn (xwbn) =*YwPn~
SOD_pages.txt:36001:11105 yxwbny'       C = y-, +xwbny* =» xwpn-                 11116 yxyp8y     C = y- =* xyp5
@@ dream
36344:slcep,  dream 
36354:(to)dream 
80541:sleep,  dream 
88986:dream    4346,  10711 
88987:G<?)dream    4347
```


## [2026-09-14T03:12:23.604Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36335,36365p' SOD.txt; echo \"@@@\"; sed -n '80530,80560p' SOD.txt; echo \"@@@ 4346\"; grep -n \"^4346\\|^4347\\|^10711\\|^10712\" SOD.txt | head"
}
```


### [2026-09-14T03:12:23.698Z] TOOL RESULT

```
yo/updya   -^ywpty'h 

praising 
STii  1.8 

4346  ywpn-   B  ^l^ 
xwapn,  xuPn   ©<Av.  xwafna;  Yaghn.  xuvn 

©nom.  -y;  ace.  -w,  abl.  -\  loc.  -yh   =»xwPn- 
slcep,  dream 
GMS  503;  VJ  3.4;  SCE  5,  7  etc.  312,  329;  TSP 

2.409,  410,  808,  1160,  13.26,  6.4,  109.112,  7.66; 

STii  8.4 

4347  ywpnw  wyn-   B  o±*->lj>- 
xuPnw  wen- 

(to)dream 

VJ3.4 

4348  ywpny   M  ox,>. 
yopne   ©pres.  part.;  pi.  -t 

praising 
GMS  892 

4349  ywpt-  **  ywP-1 

@@@
weakness 

BBB  606,  712;  BSTii  892.5:  C2,  31R5 

10709  xw'yr-  =»  Ywyr-] 

10710  xwbn   C  =»  xwpn- 

10711  xwpn-   M,  B  ^1^ 
xupn  (xwbn)  =*YwPn~ 

sleep,  dream 

GMS  312,  503;  -y,  BBB  695;  STii  8.4;  loc.  -y\ 
C2,  48V9 


J  j* 


10712  xwpw   S,  B  .li 
xufu,  xupu  ©<*xwa-bawa  =»ywPw 

king 

STii  7.29,  39;  KG  595,  597;  S  W,  Apd.  3.4.3;  CII 
1990  G3,  16,  17,  18 

10713  xwc  C  ijn^jU* 
xw(o)c,  xwec  ?   ©f.  n.   =»xwyc,  xw>c,  xwcqy* 
illness,  pain 
@@@ 4346
36340:4346  ywpn-   B  ^l^ 
36351:4347  ywpnw  wyn-   B  o±*->lj>- 
80538:10711  xwpn-   M,  B  ^1^ 
80550:10712  xwpw   S,  B  .li
```


## [2026-09-14T03:12:30.709Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"'wPs\\|ʾwβs\\|'wbs\\|wps-\\|wPs-\" SOD.txt | head -20; echo \"@@ to sleep\"; grep -n \"(to)  sleep\\|(to)sleep\\|to  sleep\" SOD.txt | head -20"
}
```


### [2026-09-14T03:12:30.778Z] TOOL RESULT

```
19793:1856  *>wps-   S  oo^OjU^ 
47453:5918  nyrwps-   S  0-^»->^j>  <ooiojjii 
47456:*»zyrwPs- 
53106:pacyufs  ©pass.  st.  =*pcywp,  pcywPs- 
53317:pS'wps- 
53334:paSupd   ©pt.  st.  ^pS'wPs-  pSVm-,  pw5>wptk 
53340:pa8um   ©<*upa-dumb  ^pS'wPs-,  p5>wPt- 
53632:pSwps- 
53644:6827  pSwps-    B  *±  pSwfs- 
53648:pa5ufs   (p5wps-)  ©<*upa-dubsa  ©inf.  -y 
74110:wafs   ©impf.  ^w^s-,  **wps- 
84589:11277  zyrwps-   B  jjiUzil^l^  <jjiiJuL 
@@ to sleep
5798:(/Qfs/,  to  sleep)  might  be  long,  but  the  imperfect 
74111:(to)sleep 
74273:(to)sleep
```


## [2026-09-14T03:12:33.257Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '19788,19800p' SOD.txt; echo \"@@@\"; sed -n '74100,74120p' SOD.txt; echo \"@@@\"; sed -n '74265,74280p' SOD.txt"
}
```


### [2026-09-14T03:12:33.387Z] TOOL RESULT

```
aPruyde,  oPruyde  ?   ^bryty,  }nPrytk 

be  numbed 
SCE  28 

1856  *>wps-   S  oo^OjU^ 
ufs,  ofs   ©Av.  hufsa-;  Yaghn.  £fs-t  Khot.  hus; 

*awa-hufsa-   ©impf.  w*fls   ^'wfs-,  w'ps- 
(fo)sleep 
GMS  539;  Frag.  2a.l3;  S  W,  BSOAS  1989,  258 

1857  >wpt-   S,  M 
@@@
TSP  2.64  n  pl69;  VJ  1455;  Frag.  Len.  44,  8;  GMS 
1592,  1313A;  w'pryt,  VJ  1378 

9781  w'pry  =»  w>pr 

9782  w>pry5  =»  w>Pr>yS 

9783  w'pryt  =»  v)Pr,y5 

9784  w'ps-   B 
wafs   ©impf.  ^w^s-,  **wps- 
(to)sleep 

GMS  539;  Frag.  2a.l3;  S  W,  IIJ  1976,  58,  59  n  8, 
*awa-hufsa- 

9785  w'pw    B  =»  wpyw 

9786  w>py   B 
wafe/-i  ? 
so,  so  much 
@@@
Hen.  Cosm.  312.124;  JRAS  1942,  232  n  6,  GMS 
590 

9806  w}fry8(6)    M  =»  w>pr>y5 

9807  w}fs-   C  jjuly^ 
wafs   ©impf.  ^^wfs-,  wJ0s- 

(to)sleep 

Benv.  Eti  308;  C2,  60R8 

9808  w'fyd   C  ^^jiT 
wafeS   (w>fy55)   ^w'p'yS 

so  much
```


## [2026-09-14T03:12:42.574Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor leaf in (238,239,240):\n    print(\"=== leaf\",leaf)\n    print(pages[leaf][:900])\nEOF"
}
```


### [2026-09-14T03:12:43.609Z] TOOL RESULT

```
645
=== leaf 238
                              5i,**M.i'-V,fe&Kf ?i '^ ■ ■ :                             ^^HHHHill^H


 173

                                                                                                                        ywcm'nqy*
 4338 ywp-3 =» YwPw                                                            C2,48R18
                                                                          4352 ywpty B, M
 4339 ywp't =* YWP-*                                                                                      =»ywbc
 4340 Ywp'ty'kh B                                                 jj^          yfipde (ywP*!, ywbty) ©pp.
      yoPatyak ^ywpty'kh
                                                                                GMS 849; TSP; BBB; Hen. Tales. 473; STi 22.19;
                                                                                praised
       praise2.490; KG 41
=== leaf 239
                                      mmmmmmmmm


                                                                                                                            174
       yw&kih)

       4362 Yw&'kGi) B         (jjy ; jL^j), jio;l ^j^T ^U=t<o>            monastery
                                                                           Yumr ? ©loc. -y>
            Yo5e (ywdy) ©<Av. gaoiSL, gaoSana
            vessel, container, pitcher, measure                            C2, 60R26
            GMS 1117n 1; TSP 8.108; Dhy. 277, BSTBL; Frag.
                                                                     4374 ywmt'nc      B
              Len. 100c 12; Hen. LW 99; JRAS 1944, 143n3;
                                                                           xumdan                     (j^r JJ <JO*^ /-k) j'-^jp-
              STi 43.9, 10; C2, 94V 21 n pl77                  
=== leaf 240
4384 ywnV     B                                ^<^              SCE 318, 502

      xune, xwane =»ywny, ywn-1, xw'n2                    4397 ywdy     B =± yvsrfy
      proclamation, news
      Ywn>kwy VJ 75, 89                                   4398 ywny(w) «> Ywn?
                                                          4399 Ywnnc C                                            *xJ>l
4385 -ywn'k B                      (u,>-)jujU ««jf              increasing
                                                                yunanc  ? ©*Ywnny        ©f. adj. =$yv/n-7
     yonc (-ywny) ©<*gaunaka ©as suff. in
       compd. ^'nywn^, wvywnc, cYwny,                           BSTii 895.25: C2, 54R25
        wyspYwn}y                                         4400 ywnpyk      B                                        of
      like, similar to                                         foam
      GMS 1113,
```


## [2026-09-14T03:12:51.658Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[238])\nEOF"
}
```


### [2026-09-14T03:12:52.700Z] TOOL RESULT

```
                              5i,**M.i'-V,fe&Kf ?i '^ ■ ■ :                             ^^HHHHill^H


 173

                                                                                                                        ywcm'nqy*
 4338 ywp-3 =» YwPw                                                            C2,48R18
                                                                          4352 ywpty B, M
 4339 ywp't =* YWP-*                                                                                      =»ywbc
 4340 Ywp'ty'kh B                                                 jj^          yfipde (ywP*!, ywbty) ©pp.
      yoPatyak ^ywpty'kh
                                                                                GMS 849; TSP; BBB; Hen. Tales. 473; STi 22.19;
                                                                                praised
       praise2.490; KG 415, 559, 585
       TSP                                                                        STii 3.44; C2, 48R20, 94R26; Twfitk, Frag. Len.
 4341 Ywbc C                                                       <o^            44.4; ace. Yw0tykwf W-Li 71; ace. Ywbtw, C2,
                                                                                  51R17; pi. rw6ryr,C2, 48R19
      yoPc ©f. pp. =»ywP-\ ywpty
                                                                          4353 ywbty     C =» ywpty
       praised
       BSTii 883.10. C2,48R12                                             4354 ywbty*    C =* ywpty>h
 4342 ywpcy'k S                                               ^J-j"^      4355 ywpty'h M                        jJb^j sj^ «>j&
      yuPcyak                                                                  yfiptya (ywbty1) ©f. n.; pi. -/ ^ywbdy*
      beauty, glory                           ¥                                praise, glory
      W-Li 88: Gropp. p39                                                       GMS 948, 1015; BBB; W-Li: Gropp. p39; STi
 4343 ywpcyk S                           ^U^l,                                    14.18, 22.17; Sund. AoFviii 1981 p215; STii
      xupcik, xufcik ©ob. pi. -iy «*ywPw                                          4.22; BSTi 176; C2 gloss.
      royal                                                               4356 ywpty'kh B, S                                    jj^.
      Frag. Len. 40.11                                                         yu/optya(k) ©f. n. ^ywP'ty^h
4344 ywbd'r-      C -* ywp-1
                                                                               TSP 8.62; GMS lllln 1; KG 415, 559, 585
4345 ywbdy* C                                                     jj^          praise
                                                                          4357 ywpw B, S                             fla;U^<.U
     yo/updya -^ywpty'h
     praising                                                                  xufu, xuPu (ywP-3) ©<*xwa-bawa ? ©pi. -f
     STii 1.8
                                                                                 =»xwPw, MR'Y
4346 ywpn- B                               ^l^                                 king, chief
                                                                               VJ 198 etc.; TSP 2.832, 839, 22.7; STii 7.29; Frag.
     xwapn, xuPn ©<Av. xwafna; Yaghn. xuvn
                                                                                 Lcn.; MDii; Hen. Tales. 4742, 5 & etc., 483.4
         ©nom. -y; ace. -w, abl. -\ loc. -yh =»xwPn-
       slcep, dream                                                              etc.; JRAS 1944, 138.46; W-Li: Gropp. p39;
       GMS 503; VJ 3.4; SCE 5, 7 etc. 312, 329; TSP                              S W, KG pi 97, Appd. 3.4.3; Twfl, TSP 6.58
         2.409, 410, 808, 1160, 13.26, 6.4, 109.112, 7.66;                4358 ywpwy1 S                                         *UU
         STii 8.4                                                              xupuya, xufuya
                                                                               kingly, kinglike
4347 ywpnw wyn-         B                                     o±*->lj>-        Hen. Tales. 475.24
     xuPnw wen-
     (to)dream                                                            4359 ywc-     B                               J^y^^sy*-
     VJ3.4
                                                                               xuc ©nom. -y; ace. -w, abl. -> =»xwc-
4348 ywpny      M                                                ox,>.         nice, pleasant
       yopne ©pres. part.; pi. -t                                              GMS 504; VJ 61, 136, 1294, 1440; BSTBL, Dhy.
       praising                                                                  71; TSP 2.214; Frag. Len. 1.1
       GMS 892
                                                                          4360 ywck}    B                                   ^l jT * jU
4349 ywpt- ** ywP-1                                                            xuck ? =»xwcq, ywyck(>)
4350 ywptch S                                                     ^            open, 2.1080
                                                                                       free
     Yopc ©f. adj.                                                             TSP
     praised                                                              4361 ywcm'nqy* C              ? ^jIUa txJ j,y~ ij^sj^y-
     Mack. AI 1985, 425.31                                                     xucmankya ?

4351 ywbtr C                                                    j^^.           well-minded, well-meaning ?
     Yuptar ©comp. adj.; pi. -t                                                Sund. AoFviii 1981, 21R 2, 15, 22V 1, 3 pl81
     more glorious                                                               nl25
```


## [2026-09-14T03:12:59.306Z] TOOL CALL #45: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py FFD:50 2>&1 | head -60"
}
```


### [2026-09-14T03:13:00.376Z] TOOL RESULT

```
no scan of FFD covers printed page 50 (see 'scans' in refs_online.json)
```


## [2026-09-14T03:13:00.804Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"nleaves\",len(pages))\nfor leaf in (203,217,223,237):\n    print(\"=== leaf\",leaf,\"~printed\",leaf+543)\n    print(pages[leaf][:1200])\nEOF"
}
```


### [2026-09-14T03:13:01.938Z] TOOL RESULT

```
nleaves 684
=== leaf 203 ~printed 746
 ‫خز مر‬                                                                                                            ‫‏~‪9 {e‬ب‬


                                        ‫شبیه باشنان ‪.‬‬        ‫انی‬
                                                               ‫‪.‬ویند طوطی در آنولایت زکند‬
                                                                                        ‫آورند ‪ ۱‬گ‬
                               ‫‪- °‬‬   ‫حز ده‬               ‫اعت از‬       ‫نمیتواند کرد ‪ ۰‬وبعضی گوبیند نام ولاش‬
 ‫بر وزن دوتده ‪ .‬حشرات‬

 ‫الارش‌را گویند همجو(‪ )۲‬مور و مار وامثالآن ‪.‬‬             ‫ترکستان که مردم آنجا بيار سفید میباشند‬
                                                         ‫و‌جانوریست آبی شبیه‬
                                                                           ‫وق د‪ :‬ازآ نولات آورند‪ .‬آن‬
‫خزو ‪ - 2۱‬بفتح اول بروزن مکو کے‪.‬‬
                                                                                                                    ‫‪٠‬‬       ‫‪۰‬‏‬




                                                         ‫خز ران ‪ -‬بر وزن مرجان ‪ .‬معنی‬
 ‫حر هره ‪ -‬مخفف ‪.‬خرزحره است ‪. ۷‬‬
 ‫و آن‌رستنبی‌باشد کەبر کے آ راحیوانات‌منورند(‪)۳‬‬
‫دمر لد
=== leaf 217 ~printed 760
                                                                                                        ‫ی‬
                                                                                                        ‫‪۷‬‬ ‫ت‬


                                                                ‫ازجملة هفت خط جام جمشید (‪.)۱‬‬

                                                   ‫»>کنانه‬   ‫بی افطةٌ رده‬   ‫برای‬   ‫‪3‬‬   ‫کشیده‬   ‫بالف‬   ‫نقطهدار‬



                                                                              ‫از فلمزن ونیزه ور باشد ‪۰‬‬
                                               ‫‪۱‬‬   ‫خط کشیدن ‪ -‬کنابد از محو کردن‬
‫که قاری قرآن باشد ‪ -‬و موحد را نیزگوبند ‪.‬‬       ‫‪۰‬‬                             ‫وبرطرف ساختن باشد‪۶3 .‬‬
  ‫ب‬
  ‫ککو‬
    ‫خطیب فلك ۔ کشابه از‬                             ‫خط‪ 4‬اول ک‪-‬نابه ازعرش‌مجید است‬
                                 ‫‪.‬‬   ‫هشترست‬    ‫‪,‬‬




                                      ‫بیان سیز دهم‬
            ‫در خای نقطهدار بافامشتمل بربیدستولوغت کونایت‬
‫ی باشنف از اعراب رامزن‬
                       ‫روزن سراچه ‪ ۰‬طانفه‌ا‬
                                                    ‫»وعی‬
                              
=== leaf 223 ~printed 766
                                                                                                           ‫‪A‬‬‫‪A‬‬

 ‫ساخته آبرا منفقش سازند و داخل جهاز دختران‬                                          ‫وآنرا بهذت برین نیز گوبند ‪.‬‬
‫کنند » و بعضی گوبند کوزه کلینی (‪ )۲‬اس تکه‬                    ‫خلر ب=ضم و فتح ثانی و سکون رای‬
 ‫دختران در آن آبپای رنگن کنند‪ .‬بویکدیگر‬                      ‫قرشت غله‌است شبیه بکرسنه ‪ ۱‬و انرا در بزد‬
                                             ‫باشند؟‬
‫‪-‬ویاچهازاروشلواررنگن‌رانیز (‪ )۳‬کفته‌اند‬                   ‫ونواحی کرمان و لرستان (‪ )۱‬تاصز است خام‬
‫رضم اول وثانی‌هم |مده‌است(‪ »)4‬آب‌دهن‌را گویند‬                 ‫خور ندوبخورد گاولیزدهند‪ .‬کاورافربه کند وجون‬
                               ‫‪.‬‬    ‫کد خنو اڈ‬
                                                                                                      ‫همان‬          ‫ز سل‬

‫خلق ] تشين = بفتح اول ؛ کنابه از‬                                                                     ‫یز ند و بل«ورند‬

  ‫شياطين وجنبان است ‪ -‬وعم اکونلابه از شب‬                                                             ‫واهی درآغها‬
                                                             
=== leaf 237 ~printed 780
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
                       ‫و خدمتکاری که آلت‬                               ‫‪۱‬‬
```


## [2026-09-14T03:13:11.530Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ntargets=['خفتن','خفتک','خفج','خسبیدن','خسپیدن','بختک','خله','خلیدن','خوره','خفتو']\nfor n,p in enumerate(pages):\n    for w in targets:\n        if w in p:\n            print(n, n+543, w)\nEOF"
}
```


### [2026-09-14T03:13:12.666Z] TOOL RESULT

```
24 567 خله
43 586 خله
89 632 خله
180 723 خوره
193 736 خله
200 743 خوره
201 744 خوره
204 747 خفتن
204 747 خسپیدن
206 749 خوره
218 761 خفتن
218 761 خفج
218 761 خفتو
219 762 خفج
221 764 خله
223 766 خله
223 766 خلیدن
224 767 خله
224 767 خلیدن
225 768 خله
225 768 خلیدن
245 788 خوره
247 790 خوره
248 791 خوره
251 794 خوره
264 807 خله
286 829 خفتن
309 852 خفتن
330 873 خوره
380 923 خفتن
609 1152 خفج
639 1182 خله
653 1196 خوره
```


## [2026-09-14T03:13:20.889Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in (204,218,219):\n    print(\"=== leaf\",leaf)\n    print(pages[leaf][:2500])\nEOF"
}
```


### [2026-09-14T03:13:21.787Z] TOOL RESULT

```
=== leaf 204
                                                           ‫بیان نهم‬

            ‫در خای نقطه‌دار باسین بینقطه مشتمل برچهل ودو لغت و کنایت‬
                                                                    ‫حس۔ بفتح اول وسکون‌تانی “ معروف‬
                                                                    ‫است که خاشه وخلاعه ءخاشاك باشد ‪۷‬‏ ومردم‬
‫خسائیدی؟ ‪ -‬بروزنوسانیدن‪ .‬سعنی‬
                                                                    ‫فرومایه ویخیل و رذل دون ونا کی وزبوترانیز‬
                                   ‫بدندان کرشردن باشد ‪.‬‬             ‫نگاو کوعسان‬               ‫کرد‬             ‫کی‬
‫مستقمل‬           ‫خساید = بر وزن راید ‪.‬‬
                                                                   ‫می‌باشند‪ .‬خصوسا کفار صحرانشین ؛ وبعضی گوبند‬
    ‫«‬‫خالیدن است منی بدتدان کرشند ‪۵‬‬                                 ‫تاشمعتی هندی است چه خسبز ‪,‬ار عندی قومي‬
                                                                   ‫باشتد از کفار که دکروههای ماین هندوستان‬
‫فرتن ‪ -‬کناب ا‬ ‫خس بدهن گ‬
                                                                   ‫‪ -‬وتام جانور کی است که بدن او‬        ‫اند‬
                                                                                                          ‫نا‌سا‬
                                                                                                              ‫ءکخت‬
         ‫عجز کردن وزیتهار وامان خوامتن باشد ‪#.‬‬
                                                                    ‫شبیه است بدانةٌ جوی کوچك و پابهای اريك‬
‫لوس ۔‪ -‬با بای فارسی بر وزن‬                        ‫جس‬
                      ‫‪۰‬‬                 ‫&‬            ‫‪:‬‬




                                                                   ‫حراز دارد وبرروی آب میدمد‪ .‬وبضی گوبند خی‬
‫‪-‬نوابه از پنهان‬‫خکروش ‪ .‬معروف است ‪٩‬‏ ک‬                               ‫مرعی‌است‪ .‬سفید ویزر کتراز کلنك‪ -‬وبعربی‌کاهو‬
‫کردن چیزی وکاری مشپور باشد بطریق احتیاط‬                                                        ‫را مخیگوند ‪.‬‬
‫ومکر وحبله ونفاق واستخفای عوب واء‌رقبیحی‬                           ‫= بکسر اول بر وزن اجاره ‪.‬‬           ‫خاره‬
                                                                   ‫ستن است که برددن شاخهای زباد تی‬
                                                                                                 ‫ممعتی عابر‬
‫س اول وسکون الی‬                         ‫خسیی ‪= ۲‬‬                      ‫است ‪.‬‬     ‫ده‬
                                                 
=== leaf 218
 ‫سه پوت‬
                                                                                                           ‫‪۱‬‬     ‫قلحاقی خوانند‬
 ‫خفتیدن وغلطیدن است نی خوابید وغاط زد‬
                                                             ‫بر ون‬              ‫بطم اول‬               ‫خفتا نمدن =‬
‫و ماضی شیر ماست شدن هم هت » یعنی شیر‬                        ‫بمعتی خوا بان دن یاعد ‪ ۳۳‬غعاطانید تر |‬                     ‫خشکاندن‪,‬‬
                            ‫حفر ات شد وعاخت کدنف‬
                                                                                                                     ‫یز گفته‌اند ‪۲‬‬
‫حفتیدن ‪ = 1‬بروزن خشکیدن‪ .‬نمعتی‬                               ‫‪1‬‬     ‫فت‬      ‫وی‬      ‫ف‬     ‫بطم "اول‬          ‫‪۳‬‬    ‫‪۲۳‬‬         ‫‪۳‬‬



‫غاطیدن_ وخوابیدن ‪ - ۷‬وبزانو درآمدن شتر‪-‬‬                      ‫بمعتي کایوی است ‪ .‬وآن سنگینی و گرانیی )‪۱‬‬
        ‫وماست گردمدن شبر وجفرات شدن باشد ‪.‬‬
                                                             ‫باشد (‪ )۲‬در خواب که (‪ )۳‬بر مردم افتد ‪, ۴‬‬
‫بفتح‌اول وفانی وسکون جمع»‬           ‫‪‌ ۸‬‬      ‫جع‬             ‫که‬      ‫ای همهت‬         ‫ویرنده‬        ‫خفتق است ‪"7‬‬              ‫ومعرب‌ان‬

                                                                                             ‫رس‬   ‫لو ومد‬       ‫آترا کارو انك ه‪.‬‬
 ‫کین و گرافتن )‪ (۲‬باشد که مردم رادرخواب‬

‫بهمرسد وآنر! بعربی‌کابوی وعبدالجنه کویند ؛‬                   ‫حفتو بت هم اول بروزن بر گو » بمعنی‬
‫و فتحاولوسکون‌انی‌هم | مده‌باد_وبفتح‌اول وثانی‬               ‫آن‬     ‫باشد ه‪٠‬‏ و‬     ‫عدالحنه‬        ‫و‬    ‫است کەکایوی‬                  ‫خفتك‬

‫خردل‌صحراییاست کهآ نرا قکجوییند ‪٩‬‏ آنرا‬                       ‫سنگینیی است که درخواب برمردم می‌افند‪. ۴‬‬
‫بکوبند و درماست کنند وبا طعام خورند )‪(٩‬‏ ‪-‬‬                  ‫خفت و خیز هکنابه ازآهتگی وتانی‬
‫و در عربی مطلق لرزبدن باشد عموه‌او لرزیدن‬
                                                            ‫وتدریج ‪ -‬واضطراب وبیقراری باشد ‪ -‬کونابه از‬
‫همه‌حاه‬       ‫رون‬      ‫يفنح اول وئالی‬   ‫=‬   ‫خفحا‬
                                                                                                   ‫ام کن هم جنگ‬
                                                            ‫به‌عنی‬      ‫گفته ‪» :‬‬   ‫ورن‬       ‫اول بر‬    ‫تم‬        ‫؟‬    ‫حفته‬

‫گورانی در خواب‬              ‫کی‬
                             ‫بمعتی خفج است که مد‬             ‫و خمیده را نز‬                   ‫شمده‬
                                          
=== leaf 219
                                                                                                       ‫پا‬

            ‫بمعنی خمیده و خم شده باشد ‪. ۴‬‬                 ‫ونامبیابانی هم‌هست ازترکستانکه بدشت قبچاق‬
                                                                                              ‫مشهوراست ‪.‬‬
 ‫حفرج = بفتح‌اول وسکون انی بروزن‬
                                                          ‫حفحه = بفتح اول وجیم ابجد که ثالث‬
 ‫سبزه وگیاه خرفه را کوبند و بعرمی‬            ‫مخرح ‏‬
 ‫بقلةالحمقا خوانند؛ وبفتح‌اول وثانی همآمدهاست‬             ‫باشد ویسکون (‪ )۱‬نانی ‪ ۰‬نام درختی است برخار‬
                                                      ‫وت مبوء گردسرخ رنگ دارد ‪ ۰‬وآن درخت را‬
                       ‫که بر وزن تگرك باشد ‪.‬‬
                                                      ‫بعربی عوسج خوانند ‪٩‬‏ ‪ -‬وبفتح جیم فارسی که‬
 ‫خفر نج * د بر وزن شطرنج کرای‬                             ‫‪,‬آن‌طلا‬
                                                                ‫خفجه باشد شوه طلا ونقره است ‪ ۴‬و‬
 ‫وسنگینیی‌باشد که درخواب برمردم‌افتد ودرعرمی‬              ‫و نقرء کداخته باشد که در ناوچهٌ آهنن ریخته‬
                    ‫ابوس وعبدالجنه گویند ‪۶.‬‬               ‫(‪ )۲‬چند را زیگونند از زلف‬           ‫یوی‬
                                                                                                ‫مندو ‪-‬‬
                                                                                                     ‫باش‬
 ‫نج د بفتح اول و الی وسکون لون‬                            ‫جمم شده باشد (‪ )۳‬و برروی‬            ‫جها‬
                                                                                                ‫کل ک‬
                                                                                                   ‫یا ک‬
                                                                                                      ‫وک‬
                                                          ‫جوانان خوصورت افتد ‪ -‬وشاخ درختی که بسبار‬
‫وجیم ایجد‪ .‬بمعنی‌نفموفایده‪ -‬وعیش‌وطرب وناز‬
                                                                             ‫هموار وراعت رسته باشد ‪۶4 .‬‬
                                     ‫وغمزه باشد ‪.‬‬
‫خف‪ "4‬ب=فتح اول و انی » فشردن کلو‬                          ‫خفدان ‪ ۴‬د بادال ابجد‪ .‬بروزن ومعنی‬
‫‪ -‬وم اول‬         ‫یند‬
                   ‫وسه رگا نویز‬
                              ‫عط‬‫باشد ‪-‬‬                    ‫خفتان است که سلاح جامه باشد که درروزجنگه‬
```


## [2026-09-14T03:13:34.457Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in (223,224):\n    print(\"=== leaf\",leaf)\n    print(pages[leaf][:2600])\nEOF"
}
```


## [2026-09-14T03:13:35.422Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[237][:2600])\nEOF"
}
```


### [2026-09-14T03:13:35.667Z] TOOL RESULT

```
=== leaf 223
                                                                                                           ‫‪A‬‬‫‪A‬‬

 ‫ساخته آبرا منفقش سازند و داخل جهاز دختران‬                                          ‫وآنرا بهذت برین نیز گوبند ‪.‬‬
‫کنند » و بعضی گوبند کوزه کلینی (‪ )۲‬اس تکه‬                    ‫خلر ب=ضم و فتح ثانی و سکون رای‬
 ‫دختران در آن آبپای رنگن کنند‪ .‬بویکدیگر‬                      ‫قرشت غله‌است شبیه بکرسنه ‪ ۱‬و انرا در بزد‬
                                             ‫باشند؟‬
‫‪-‬ویاچهازاروشلواررنگن‌رانیز (‪ )۳‬کفته‌اند‬                   ‫ونواحی کرمان و لرستان (‪ )۱‬تاصز است خام‬
‫رضم اول وثانی‌هم |مده‌است(‪ »)4‬آب‌دهن‌را گویند‬                 ‫خور ندوبخورد گاولیزدهند‪ .‬کاورافربه کند وجون‬
                               ‫‪.‬‬    ‫کد خنو اڈ‬
                                                                                                      ‫همان‬          ‫ز سل‬

‫خلق ] تشين = بفتح اول ؛ کنابه از‬                                                                     ‫یز ند و بل«ورند‬

  ‫شياطين وجنبان است ‪ -‬وعم اکونلابه از شب‬                                                             ‫واهی درآغها‬
                                                                                                               ‫ک‬
                            ‫و تندی مزاج مردم ‪۰‬‬
                                                                                                     ‫نیز کرده آرد‬
‫خلم س بم اول وثالی رسکون میم»دام‬
                                                                                                    ‫آنرا نان یزند‬
 ‫قسبه است ازتوابع‌بلخ و درسرحد بدخشان واقع‬
                                                                                                      ‫وخورند؛ ونوعی‬
 ‫شده است وبده فرعون اشتهار دارد ‪ -‬وبکراول‬                                                             ‫طلست‬         ‫سگم‬

 ‫وکون الی» خلطغلیطی را کوبند که از بینی‬
                                      ‫س‬                                                               ‫صحرایی ‪,‬چون‬
 ‫آدمی وحیوانات دیگر برمیااید ‪٩‬‏ وآترا بعریی‬
                                                                                                          ‫زنان خورند‬
 ‫مخاط خوانند ؛ وباینمعنی بضم اول وسکون ثانی‬                                                      ‫بیقر ید ‪۳‬‬     ‫دمراشان‬
‫همگفته‌اند ‪ .-‬وخشم وغضب رانیز گوبندد وبمعنی‬
 ‫کل تیر چبنده‌هم هت که اکرپای دآنر‌بند‬                        ‫خلش ‪ = ۴‬بفتح‌اولو کرانی وسکون‬
                              ‫شود بسانی بررنیابد‪.‬‬             ‫شین قرشت » بمعنی جراحت کردن و فرو بردن‬
 ‫خلمفع‪ - ۲‬بکراولونالی وسک
=== leaf 224
  ‫‪7-۷٩‬‬


 ‫خکلرده نیز‬
          ‫بزرکه هم هت که (‪ )۱‬آنرا و‬                     ‫خلمه ه بش اول بر وزن سرمه » کره‬
 ‫ومهی است بسیار بزرکه وباد‬
                         ‫گویند ‪ -‬وکنا‬                                                ‫‪.‬‬    ‫ند‬
                                                                                           ‫وایرا‬
                                                                                               ‫گعص‬
                                                                                                 ‫سر‬
                              ‫وشامخ ‪,‬هنی رفیم (‪. )۲‬‬      ‫حل » م اول وکسرثانی و سکون‬
 ‫حلو گر ده = بم اول وکاف فارحی؛‬                          ‫نون » کسی را گونن دکه پیوسته آب غلیظ ازینی‬
 ‫نوعی‌ازآلوی بزرکه‌باشد‪ .‬وبعضی کوبندمیوه‌ایست‬                                          ‫او روان شود ‪.‬‬
                                      ‫شبیه بشفتالو ‪.‬‬     ‫خلنج ‪ » ۴‬بنتح اول و انی و سکون‬
                                                         ‫نون وجیم » هرچیز دورنگه باشد و بعربی ابلق‬
 ‫خلو لا = بضم اول ونانی‌مجهول وکر‬
                                                         ‫خوانند ؛ وباینمعتی بکسراول بروزن شکنج هم‬
‫لام بورزن فلوئیا» بی‌شرم و بی‌باك و بیحیا را‬
                                                         ‫آمده است ‪ -‬و کبوتری را نز گونند که تمامآن‬
 ‫کوبند ‪ -‬ومردم دیواله مزاج کرفاهتمه‌اند ‪- ۷‬‬
‫و چیزبرا لیر کوبند که هرکس خواهد او را‬                  ‫سیاء بود مگربك پربادوپرازبال او کهسفید‬
                                                         ‫میباشه ‪ -‬وبکراول وثالی بروزن برنج ‪ .‬گرفتن‬
 ‫متصرف‌شودمانعی لداشته باشد ‪ -‬وعلت مالیخولیا‬
                                    ‫را همگفته‌اند ‪5‬‬                        ‫دن بناخن باشد ‪.‬‬
                                                                                         ‫کضانو‬
                                                                                             ‫اع‬
                                                          ‫خلنده ‪ = ۴‬بفتح اول بر وزن دولده‪.‬‬
 ‫خله ‪ -‬بفتع اول و الی " چوب درازی‬
                                                               ‫باندرون رونده ومجروح کننده راکویند ‪.‬‬
‫که بدان کشتی میرانشد ؛ وبایتمعنی جضم اول‌هم‬
 ‫و فرو رونده‬             ‫ده‬
                          ‫لینکه‬
                              ‫خیز‬
                                ‫وچ‬      ‫آمده استھ ‏‬      ‫خلنگ ‪ ۴‬بنتماول بروزن پلنگه‪,‬‬
                                                          ‫بمعنی خلنج است که دورنگه وابلق باشد ® ‪-‬‬
 ‫درجایی باشد مالند سوزن و جوال دوز و درفش‬
‫وامثال آن ‪٩‬‏ ‪ -‬وبمعنی خالی
```


### [2026-09-14T03:13:36.860Z] TOOL RESULT

```
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
                                                                    ‫‪ - ۴‬از خ‬
       ‫‪ - ۴‬ریدکان خواب نا دیده مصاف اندرمصاف مکربان د!غ تاکرده قطار اندر قطار‪.‬‬
  ‫‪ +‬فرخی سیستانی‪.> ۹۷۱‬‬
  ‫« سخن سال ‪۲‬‬        ‫‪01‬‬
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
```


## [2026-09-14T03:13:49.404Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la MON_part1.txt MON_part2.txt incoming/MON/ 2>/dev/null; python3 - <<'EOF'\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print(f,len(t),len(t.split('\\f')))\n    print(t[:300])\nEOF"
}
```


### [2026-09-14T03:13:50.517Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt

incoming/MON/:
total 48692
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 20113727 Sep  4 14:06 MON_2vol_Adena_v1_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4377831 Sep  4 14:06 MON_2vol_Adena_v1_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 21014767 Sep  4 14:06 MON_2vol_Adena_v2_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4331421 Sep  4 14:06 MON_2vol_Adena_v2_djvu.txt
MON_part1.txt 2611770 1
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 

MON_part2.txt 2568024 1
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاعات فیپا. 
۱. فارسی -- واژه‌نامه‌ها. الف. عنوان. 
۴۵ف ۲۹۵۴/۸۷ ۳112 ۳ فا ۴ 
۱۳۸۱ 
کتابخانه ملی ا
```


## [2026-09-14T03:13:55.988Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"خوره\" MON_part1.txt | head -20"
}
```


### [2026-09-14T03:13:56.044Z] TOOL RESULT

```
1230:آب‌خوره: (-)20-2072 (امر .) آیخوری» 
1234:بلورین که با آن آب خورند آبخوره. 
9857:ارزانی: -2۳20 (ص نسه.) ارزنده. درخوره 
10045:می‌خورد» موریانه» خوره» چوب‌خوار» 
11841:درخت استر کث» قره‌بوخوره قره کونوک 
15905:اکول: اتاه [ع.] (ص.) برخورء سبار خوره 
17789:نمنا ک. بخورها. 
18658:آوندها» آیخورها» آبدان‌ها. 
28523:تاش بایگاه» آخوره اصطبل. حضیض 
47359:مستقیم است؛ آ کله» خوره. 
52608:حسجی: (ص.) سزاوار» درخوره 
58060:خوره: (0۲-۵)0: (.) انجه که جیزی را 
58063:خوره: (قد. -۵()0۵۲۲۵۰-)0۲۲۵ (۱.) موهست 
62718:هرزه. ولگرد. دست کج دزد. . پرخوره 
83659:ش‌ایسته: (0-)ام-(32 (امسف.) درخوره
```


## [2026-09-14T03:13:57.228Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"خلبان\" MON_part1.txt MON_part2.txt BQT_v2_pages.txt incoming/ARY/ARY_pages.txt 2>/dev/null | head -20"
}
```


### [2026-09-14T03:13:57.298Z] TOOL RESULT

```
MON_part1.txt:57105:خلبان: 2۵۱27 [- خله‌بان] (ص‌مر. امر.) 
MON_part1.txt:64232:سخن گفتن خلبانان است. در هواپیماهای 
MON_part1.txt:64448:خلبان می‌تواند آن رابه هر جهت که 
MON_part1.txt:97043:مخصوص دارد» بطوری که برخی خلبانان 
MON_part2.txt:16870:جایگاه مخصوص خلبان هواپیما. 
MON_part2.txt:92163:هدایت کند؛ خلبان.
```


## [2026-09-14T03:13:59.436Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '57095,57125p' MON_part1.txt; echo \"@@@ khoreh\"; sed -n '58050,58075p' MON_part1.txt"
}
```


### [2026-09-14T03:13:59.514Z] TOOL RESULT

```
(مصم.) فرو کردن چیزی باریک و نوک 
تیز مانند خار» سوزن و غیره در بدن یا در 
سیر 

خللا: 213 01 , خلاء ] ) ( فضایی که هسیج 
ماده‌ای در آن نباشد» فضای خالی» خلاء؛ 
مق. ملاً ملاء) ضح.- (فد.) مسأله‌ای مطرح 
ِِ اتف ی ی و 
نباشد هد که و فا او را 
اشیاء و مو جودات است و آن مورد اختلاف 
خلبان: 2۵۱27 [- خله‌بان] (ص‌مر. امر.) 
آنکه هواییما را هدایت کند) هوانورد. 
خلت: ۱ [- خله ] (امص.) دوستی. 
(تص.) تخلل مودت است در دل و متام 
خسلجان: 127 [ع. ۰[ اه[ پریدن 
توت و وی پهلو یا عضو دیگر. 
لرزیدن» تحان حوردن. اضطراب. به خاطر 
د رآمدن. (.) میل خاطر» خواهش چیزی. 
خلخال: 5۱« [ع.] (.) حلقه‌ای فلزی که 
پای‌اورنجن؛ ج. خلاخیل (غم.) خلخال زر: 


۴« 
(کد.) آفتاب. خلخال فلکك: (کد.) ماه. 
خلد: ۵(ع.] (.) (جا.) پستانداری است 
که از حشرات تغذبه می‌کند و چشمان وی 
ضصسعیف است و در زیر زمین زست 
می‌نماید؛ انگشت ب رکک. 

خلد؛: ۲014 [ع.] 0( دوام» همیشگی؛ بقا. 
بهشت. خلد بر ین: بهشت برین» بهشت اعلی. 
@@@ khoreh

خورند: 0۲:٩‏ (امر.) فراخورء سنأسب» 
در خور» شایسته. 


۳۴ 


حورئق: ۲2۷۵۲۵۷ [معر . خورنگه - خره] 
(.) کاخ با شکوه» کوشکک با جلال. (اخ.) 
خوره: (0۲-۵)0: (.) انجه که جیزی را 
بخورد و از میان برد. (پز.) جذام. 

خوره: (قد. -۵()0۵۲۲۵۰-)0۲۲۵ (۱.) موهست 
ایز دی که ره شاهان و بیامبران عطا شود و 
بدان بر مردم تسلط بابند+ فر؛ فره» خره. 
سخشی از وللاست» ناحبه: خورة اردشیر. 
خورة استخر. 

خسوزی: -2« (ص‌نسه.) منسوب به 
خورستان» از مردم خوزستان. خوزستانی. 
(مس.) شعبه بیست و سوم از شعب بیست و 
چها رگانهٌ موسیقی قدیم. کوفته کباب. 
خوش: (قد. 05)0۸5:(ص.) خوت؛ نیکد 
نبکو. شاده شادمان» خرم. (۱.) بو سه؛ قمله. 
ضوش: 5 (- خشک ] (ص.) خشکد»
```


## [2026-09-14T03:14:09.966Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '57060,57100p' MON_part1.txt; echo \"@@@ khaleh\"; grep -n \"^خله:\\|خله:\" MON_part1.txt | head"
}
```


### [2026-09-14T03:14:10.061Z] TOOL RESULT

```
تکدبری از دو تاده روز با غرامت تا 
دویست ریال است. 

خلافت: اهاقلت< [ع. خلافه] (مص‌ل.) 
خلیفه بودن. (امص.) خلیفگی» جانشینی 
بیغمبر. پادشاهی» سلطنت. (تص.) مقامی 
است که سالک بعد از قطع مسافت و رفع 
بعد میان خود و حق بر اثر تصفیه و تجلیه و 
نفی خاطر و خلع لباس صفات بشری از خود 
و تعدیل و تسويةٌ اخلاق و اعمال و جمیع 
1 منازل که اریاب تصفیه معلوم کرده‌اند و 
طی منازل سائرین و وصول به مبداً حاصل 
کرده به اصل و حقیقت قمقت حقیقت و اصل گشته سیر الی 
له و فی الله تمام شده و از خودی محو و 
فانی و به بقای احدیت باقی گشته آنگاه 
سزاوار خلافت است. خلافت الهی: (تسص.) 
مقام نفوس کامله انسانی است. 

شلاق: ما21 [ع. ۰ (ص.) آف یننده؛ 
آفر بدگار. خدای تعالی که آفر بنندهٌ جهان و 


خلال: ا2ا1:[ع.] (ص.) س رکه فر وش. 
خللال: 6121 [ع.] ((.) مان و فاصلة دو چبز. 
در خلال: در مبان» در اینای. جوت ۳ آفتن 
که بدان دو کنارة جامه را بهم بدوزند تا از 
باد نپرد. چوب باریکی که لای چیزی 
گذارند. چوب باریکی که بدان خرده غذا را 
از لای دندان‌ها رون آرند. آلتی که بدان 
سوراخ کنند. پوست نارنج و بادام و غیره را 
که ریزریز کنند. 

خ لالوش: 12174« [- خراروش - 
هلالوش] (ا.) فتنهء آشوب» شور و غوغا. 
خلانیدن: 2-1 [- خضاندن ] 
(مصم.) فرو کردن چیزی باریک و نوک 
تیز مانند خار» سوزن و غیره در بدن یا در 
سیر 

خللا: 213 01 , خلاء ] ) ( فضایی که هسیج 
ماده‌ای در آن نباشد» فضای خالی» خلاء؛ 
@@@ khaleh
57303:خله: (0-)2212 (.) چوب درازی که بدان 
57306:خله: (2۵۱2)۵ (۱.) آنجه که در چیزی با 
57313:خله: (ع)هللع [ع. خله ] (امص.) مصادقت» 
57316:خله: (۰-)0(۵<(ا.) (گیا.) قارچ» سماروغ. 
57317:خله: (۵-)0(۵<(.) آب بینی. 
57319:خله: (6-) 0112 [ع. خلة] (امص.) دوستی» 
58745:داخله: (ع)م12۵ (ع. داخله ] (افا.) مو نك 
58750:وزارت داخله: وزارت کشور.
```


## [2026-09-14T03:14:11.042Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"خواب:\" MON_part1.txt | head; echo \"@@@ khoftan\"; grep -n \"خفتن:\\|خفتک:\\|خفج:\" MON_part1.txt | head"
}
```


### [2026-09-14T03:14:11.185Z] TOOL RESULT

```
23394:خوابگاه» بستر خواب: رختخواب. بستر رود: 
23396:شیخواب: بستری که در شب بر او خواب 
26823:بیخواب: اقا (ص‌مر.) بیدار. آنکه 
28297:پاشنه‌نخواب: 0 (امر.) کفشی که 
34443:بیراهن خواب: جامه مخصوص هنگام 
38805:تخت خواب. تختخواب: «قد(ه)-.؛ 
46462:ندل. .بر جای: به عوض؛ بدل. جای خواب: 
46819:جامةٌ خواب: رخت‌خواب» مجموع لحاف و 
57677:خواب: (قد. 56050 (.) حالتی توأم با 
59000:جراحی و غبره. داروی خواب: دوایی که 
@@@ khoftan
22225:برخفج: 6 [- برخغج - برغفج] (ا.) 
31930:سکر داخل شراب کنند. به پشت خفتن: طاق 
33619:پهلوی ناز خفتن: در ستر راحت و آسایش 
56956:خفتن: 0 (مص‌ل.) (خفت»؛ خواند» 
56959:خفتن: نماز عشاء.
```


## [2026-09-14T03:14:14.656Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '57300,57325p' MON_part1.txt; echo \"@@@ khab\"; sed -n '57674,57690p' MON_part1.txt; echo \"@@@ khoftan\"; sed -n '56950,56975p' MON_part1.txt; echo \"@@@ barkhafj\"; sed -n '22222,22232p' MON_part1.txt"
}
```


### [2026-09-14T03:14:14.773Z] TOOL RESULT

```
شدن؛ بیآلایش بودن. ((سص) پاکسی» 
تال نت سادگی. تک 

خله: (0-)2212 (.) چوب درازی که بدان 
کشتی رانند؛ پاروی قایق‌رانی. 

خله: (2۵۱2)۵ (۱.) آنجه که در چیزی با 
جایی بسخلد و فرو رود مانند سوزن» 
جوال‌دوز» درفش و غیره. بادی که در شکم 
خلنده باشد. دردی که ناگاه در بهلو و 
خلهه: (م)هلاههد [ع. خله] (.) خصلت. 
حاجت» فقر؟ ج. خلال و خلل. 

خله: (ع)هللع [ع. خله ] (امص.) مصادقت» 
برادری. 

خله: (۰-)0(۵<(ا.) (گیا.) قارچ» سماروغ. 
خله: (۵-)0(۵<(.) آب بینی. 

خله: (6-) 0112 [ع. خلة] (امص.) دوستی» 
صداقت. خصلت. 

خلیج: لاله« (ع.] (.) (جغ.) قسمتی از در یا 
که در خشکی پیش رفته و از سه طرف از 
خشکی محصور باشد) شاخابه. 

@@@ khab
۴۰ 
دهند و بر بالای آن کار کنند؛ جوبت ست. 
قالبی که بنایان طاق بر بالای آن زنند. 
خواب: (قد. 56050 (.) حالتی توأم با 
آسایش و آرامش که بر اثر از کار بازماندن 
حواس ظاهر در انسان و حیوان پدید آید؛ 
نوم؛ مق. بیداری» یقظه. غفلت. پرز جامه 
(مانند. مخمل). (ص.) خواییده. حسن خواب 
است. خواب مر غفلت» تغافل» 
یه منز له خواب اش 0( 

خواب‌آلود: ۲-0 [- خواب آلوده] 
(ص‌مف.) آنکه مایل به خواب است با خواب 
کامل نکرده و رخوتی مخصو ص احساس 
می‌کند. 

خواب‌اندن: 5027020 [- خوابانیدن] 
@@@ khoftan
خفتان: (2066:« [- خفدان) (.) قسمی 
جبامة کهآ گند که به 4 هنگام جنگ 
می‌پوشیدند» که آ گند» قز گند. 
خسفتانیدن: 0۲۱-27( (مسص عم.) 
خوابانیدن. غلتانیدن. 

خفتن: 0 (مص‌ل.) (خفت»؛ خواند» 
خواهد خفت» بخواب؛ خواینده» خفته) 
خوابیدن» خواب کردن» خسییدن. نماز 
خفتن: نماز عشاء. 

خفتیدن: 700-1427 (مصل.) (خفتید؛ 
خفتد» خواهد خفتید (بخواب)» خفتنده 
خفتیده). خواییدن» خفتن» خسییدن. 
خفجچه: : (60-)۵662 (.) شوشه زر و سیم مللا 
و نقره گداخته که در ناوچهةٌ آهنین ریخته 
خفض: هام [ع.] (سصم) ست کردن» 
فرود آوردن» فرو داشتن (امص.) فراخی 
عیش؛ خوشگذرانی. . خفض جناح: بال 
او بر تردن (غم.) فروتنی. 0 


خفقان: 01( [غ. (مص‌ل.) تیبدن» تیش 
یافتن. (امص.) تبش دل» اضطراب. 

خفه: (0-)۵)۵ [- خبه - خیه] (ص.) آنکه 
@@@ barkhafj
برخچ: ۱۰26 (- فرخچ] (ص.) زشت» 
نازیبا. زبون» سست» ناتوان. 

برخفج: 6 [- برخغج - برغفج] (ا.) 
کابوس» بختکك» عبدالجنثه. 

برخوابه: (۵-)دهد.< (امر.) توشک» 
تشک. همخوابه» هم‌بستر. 

برخور: ۲ (افا.) بهره‌ور» بهره‌منده 
متم. شریکده نا
```


## [2026-09-14T03:14:30.494Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-14T03:14:30.561Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-14T03:14:36.062Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swep-\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%81%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%E1%BD%95%CF%80%CE%BD%CE%BF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/sword\" \\\n \"https://www.etymonline.com/word/hypnotism\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 492 verification (Swep/Swer): $u\" ; done"
}
```


### [2026-09-14T03:14:44.585Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5eee9028f61a1efb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e0bbdc4aa3559faf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3b5635f0b08d2da3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e398beaa2138f27e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6b434894807c1d8b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e2d1d2161fde0e0b.txt
```


## [2026-09-14T03:14:46.967Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== swep- ===\"; grep -n -A15 \"Proto-Indo-European\" 5eee9028f61a1efb.txt | sed -n '1,60p'"
}
```


### [2026-09-14T03:14:47.024Z] TOOL RESULT

```
=== swep- ===
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swep-
2-FETCHED: 2026-09-14T03:14:38Z
3-STATUS: 200
4:TITLE: Reconstruction:Proto-Indo-European/swep- - Wiktionary, the free dictionary
5-
6:Reconstruction:Proto-Indo-European/swep- - Wiktionary, the free dictionary 
7-
8- Jump to content 
9-
10- Main menu 
11-
12- Main menu
13-
14- move to sidebar 
15- hide 
16-
17- Navigation
18-
19- Main page 
20- Community portal 
21- Requested entries 
--
57: Proto-Indo-European 
58-
59: Toggle Proto-Indo-European subsection 
60-
61- 1.1 
62- Root 
63-
64- 1.1.1 
65- Reconstruction notes 
66-
67- 1.1.2 
68- Derived terms 
69-
70- 1.1.3 
71- Descendants 
72-
73- 1.2 
74- References 
--
78: Reconstruction:Proto-Indo-European/ swep- 
79-
80- Add languages 
81-
82- Reconstruction 
83-
84- Discussion 
85-
86- English 
87-
88- Read 
89-
90- Edit 
91-
92- View history 
93-
--
132: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
133-
```


## [2026-09-14T03:14:47.862Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== khab ===\"; sed -n '1,140p' e0bbdc4aa3559faf.txt"
}
```


### [2026-09-14T03:14:47.912Z] TOOL RESULT

```
=== khab ===
URL: https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%A8
FETCHED: 2026-09-14T03:14:39Z
STATUS: 200
TITLE: خواب - Wiktionary, the free dictionary

خواب - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Persian 

 Toggle Persian subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Derived terms 

 1.3.2 
 Related terms 

 1.3.3 
 Descendants 

 1.4 
 Adjective 

 1.5 
 References 

 1.6 
 Further reading 

 2 
 Sindhi 

 Toggle Sindhi subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 2.4 
 References 

 3 
 Urdu 

 Toggle Urdu subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Noun 

 3.3.1 
 Declension 

 3.3.2 
 Related terms 

 3.4 
 Further reading 

 Toggle the table of contents 

 خواب 

 23 languages 

 العربية 
 বাংলা 
 Deutsch 
 Esperanto 
 فارسی 
 Français 
 Frysk
```


## [2026-09-14T03:14:53.818Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nimport re\nfor f,key in [('5eee9028f61a1efb.txt','Root'),('e0bbdc4aa3559faf.txt','Etymology'),('3b5635f0b08d2da3.txt','Etymology'),('e398beaa2138f27e.txt','Etymology'),('6b434894807c1d8b.txt','Etymology')]:\n    t=open(f,encoding='utf-8').read()\n    i=t.find('Toggle the table of contents')\n    print(\"########\",f)\n    print(t[i:i+3000])\nEOF"
}
```


### [2026-09-14T03:14:54.791Z] TOOL RESULT

```
######## 5eee9028f61a1efb.txt
Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ swep- 

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

 *swep- ( perfective ) [ 1 ] [ 2 ] [ 3 ] 

 to sleep 
 Synonyms: *ses- , *drem- 

 Reconstruction notes
 [ edit ] 

 According to the EIEC, this term might have referred to sleep as experienced by the sleeper, rather than *ses- , which may have described sleep as observed by an onlooker. [ 4 ] 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *swep- (75 c, 0 e) 

 *swép-t ~ *sup-ént ( athematic root aorist ) [ 2 ] ( or originally only middle voice? [ 5 ] ) 
 Proto-Anatolian: *supó Hittite: 𒋗𒌒𒉺𒊑 ( šu-up-pa-ri /⁠šuppāri⁠/ , 3sg.pres.mid. ) 

 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: स्वपन् ( svapán , nom.m.sg.aor.ptc. ) ( Rigvedic; traditionally interpreted as from a present verb ) 
 ⇒ Sanskrit: स्वपिति ( svápiti ) , स्वपति ( svápati ) ( present verb supplanting Rigvedic सस्ति ( sásti , “ to sleep ” ) [ 6 ] ) 

 *swép-e-ti ( thematic root present ) 
 Proto-Germanic: *swefaną ( see there for further descendants )

 *sup-sḱé-ti ( sḱe-present ) [ 2 ] ( or only formed in Proto-Iranian? ) 
 Proto-Indo-Iranian: 
 Proto-Iranian: *hufsati , *xʷafsati [ 7 ] 
 Younger Avestan: 𐬓𐬀𐬟𐬯𐬀 ( xᵛafsa , 2sg.impv. ) 

 Old Persian: 
 Middle Persian: [script needed] ( hwps- /⁠xufs-⁠/ , present stem of /xuftan/ ) 
 Classical Persian: خسپ ( xusp , present stem of خفتن ( xuftan ) ) ( with metathesis ) 

 Yaghnobi: [script needed] ( ūfs- ) 

 *swop-éye-ti ( eye-causative ) [ 2 ] [ 8 ] 
 Proto-Germanic: *swabjaną ( see there for further descendants )

 Proto-Indo-Iranian: *swāpáyati 
 Proto-Indo-Aryan: *swāpáyati 
 Sanskrit: स्वापयति ( svāpáyati , “ to put to sleep, lull; to put to death ” ) 

 ? *swṓp-ye-ti ( lengthened grade causative ) [ 2 ] ( the existence of this verbal type is uncertain [ 1 ] ) 
 Proto-Germanic: 
 Old Norse: sǿfa ( “ to kill ” ) ( or from Proto-Germanic *swēbjaną , a secondary causative [ 9 ] ) 

 Proto-Italic: 
 Latin: sōpiō 

 *se-swóp-e ~ se-sup-ḗr ( reduplicated stative ) [ 2 ] 
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: सुष्वाप ( suṣvāpa ) 

 Proto-Iranian: 
 Younger Avestan: 𐬵𐬎𐬱𐬓𐬀𐬟𐬀 ( hušxᵛafa ) 

 *swóp-r̥ ~ *swép-n̥s or *swép-r̥ ~ *sup-n-ós [ 3 ] [ 10 ] or *swóp-r̥ ~ *sup-n-ós [ 8 ] [ 11 ] [ 12 ] 
 *súp-r̥ ( generalized zero-grade ) 
######## e0bbdc4aa3559faf.txt
Toggle the table of contents 

 خواب 

 23 languages 

 العربية 
 বাংলা 
 Deutsch 
 Esperanto 
 فارسی 
 Français 
 Frysk 
 हिन्दी 
 Hrvatski 
 Magyar 
 Bahasa Indonesia 
 日本語 
 ಕನ್ನಡ 
 한국어 
 Kurdî 
 Lietuvių 
 Malagasy 
 Polski 
 Русский 
 سرائیکی 
 Slovenščina 
 Shqip 
 中文 

 Entry 

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

 See also: جواب 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: خواب 

 Wikipedia fa 

 Etymology
 [ edit ] 

 From Middle Persian 𐭧𐭥𐭠𐭡 ( hwʾb /⁠xwāb⁠/ ) , from Proto-Iranian *hwápati , from Proto-Indo-Iranian *swap- , from Proto-Indo-European *swep- ( “ to dream ” ) . [ 1 ] Compare Sanskrit स्वप्न ( svapna ) , Northern Kurdish xew , xewn , Russian спать ( spatʹ ) , and Ancient Greek ὕπνος ( húpnos , “ sleep ” ) , whence hypnosis .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈxʷaːb/ 

 ( Dari, formal ) IPA ( key ) : [xɑːb] 

 ( Dari, formal ) IPA ( key ) : [xɑːb] 
 ( Kabuli ) IPA ( key ) : [xäw] 

 ( Hazaragi ) IPA ( key ) : [xäw] , [xeːw] 

 ( Iran, formal ) IPA ( key ) : [xɒːb̥] 

 ( Tajik, formal ) IPA ( key ) : [χɔb] 

 Rhymes: -aːb 

 Readings

 Classical reading ? 

 xwāb

 Dari reading ? 

 xāb

 Iranian reading ? 

 xâb

 Tajik reading ? 

 xob

 Noun
 [ edit ] 

 Dari

 خواب 

 Iranian Persian

 Tajik

 хоб 

 خواب • ( xwāb / xâb ) ( Tajik spelling хоб ) 

 sleep 
 c. 1390 , Shams-ud-Dīn Muḥammad Ḥāfiẓ , “ Ghazal 26 ”, in دیوان حافظ [ The Divān of Ḥāfiẓ ]‎ [1] : سر فرا گوش من آورد، به آواز حزین
گفت: ای عاشق دیرینه من خواب ت هست؟ sar farâ gôš-i man âward ba âwâz-i hazîn
guft ay âšiq-i dêrîna-yi man xwâb -at hast? He brought his head close to my ear and, in a plaintive voice,
Said, "Hey, old-time lover of mine, are you asleep [lit. is sleep upon you]?" (Classical Persian transliteration) 

 c. 1390 , Shams-ud-Dīn Muḥammad Ḥāfiẓ , “Ghazal 464”, in دیوان حافظ [ The Divān of Ḥāfiẓ ]‎ [2] : چون من خیال رویت جانا به خواب بینم
کز خواب می‌نبیند چشمم به جز خیالی čôn man xayâl-i rôy-at jân-â ba xwâb bênam
k-az xwâb mê-na-bênad čašm-am ba juz xayâlê My love, how can I glimpse your face in dreams
When my eyes cannot get but a single glimpse of sleep ? (Classical Persian transliteration) 

 c. 1720 , 'Abd al-Qādir Bēdil , دیوان بیدل [ The Divān of Bēdil ]: بیداری میان دو خواب است هستیم
گرد تخیل دو سراب است هستیم bîdârî-yi miyân-i dô xwâb ast hastêm
gard-i taxayyul-i dô sarâb ast hastêm There is wakefulness between two slumbers ; that is us;
There is the dust of fancies between two mirages; that is us. (Classical Persian transliteration) 

 dream 
 Synonym: رؤیا ( ru'yā  / ro'yâ ) 
 c. 930 , Rōdakī , د
######## 3b5635f0b08d2da3.txt
Toggle the table of contents 

 خفتن 

 4 languages 

 فارسی 
 کٲشُر 
 Kurdî 
 Malagasy 

 Entry 

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

 Arabic
 [ edit ] 

 Verb
 [ edit ] 

 خِفْتُنَّ • ( ḵiftunna ) ( form I ) /xif.tun.na/ 

 second-person feminine plural past active / passive of خَافَ ( ḵāfa ) 

 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 خسپیدن ( xospidan ) , خسبیدن ( xosbidan ) , خوابیدن ( xwabidan ) 

 Etymology
 [ edit ] 

 From Middle Persian [Term?] ( /⁠xuftan⁠/ ) , from Proto-Iranian *hwápati , from Proto-Indo-Iranian *swap- , from Proto-Indo-European *swep- ( “ to sleep ” ) . Compare Manichaean Parthian xwsp- ( xusp- ) , Vedic Sanskrit स्वपति ( svapati ) , Classical Sanskrit स्वपिति ( svapiti ) , Northern Kurdish xew , xewn , Russian спать ( spatʹ ) and Ancient Greek ὕπνος ( húpnos , “ sleep ” ) , whence hypnosis .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xuf.ˈtan/ 

 ( Dari, formal ) IPA ( key ) : [xʊf.t̪ʰän] 

 ( Dari, formal ) IPA ( key ) : [xʊf.t̪ʰän] 
 ( Kabuli ) IPA ( key ) : [xʊf.t̪ʰän] 

 ( Hazaragi ) IPA ( key ) : [xuf.t̪ʰän] 

 ( Iran, formal ) IPA ( key ) : [xof.t̪ʰæn] 

 ( Tajik, formal ) IPA ( key ) : [χuf.t̪ʰän] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 xuftan

 Dari reading ? 

 xuftan

 Iranian reading ? 

 xoftan

 Tajik reading ? 

 xuftan

 Verb
 [ edit ] 

 Dari

 خفتن 

 Iranian Persian

 Tajik

 хуфтан 

 خفتن • ( xoftan ) ( present stem خسپ ( xosp ) or خسب ( xosb ) ) 

 ( archaic ) to sleep 

 References
 [ edit ] 

 Dehkhoda, Ali-Akbar ( 1931– ), “ خفتن ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 

 MacKenzie, D. N. ( 1971 ), “xuftan”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press 

 Durkin-Meisterernst, Desmond ( 2004 ), “xwsp-”, in A Dictionary of Manichaean Middle Persian and Parthian (Corpus Fontium Manichaeorum; 3.1 ), Turnhout: Brepols 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=خفتن&oldid=91732620 "

 Categories : Arabic non-lemma forms 
 Arabic verb forms 
 Persian terms derived from Middle Persian 
 Persian terms derived from Proto-Iranian 
 Persian terms derived from Proto-Indo-Iranian 
 Persian terms derived from Proto-Indo-European 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/an 
 Rhymes:Persian/an/2 syllables 
 Persian lemmas 
 Persian verbs 
 Persian terms with archaic senses 

 Hidden categories: Pages with entries 
 Pages with 2 entries 
 Middle Persian term requests 
 Parthian terms in nonstandard scripts 
 Parth
######## e398beaa2138f27e.txt
Toggle the table of contents 

 ὕπνος 

 16 languages 

 Dansk 
 Deutsch 
 Ελληνικά 
 Eesti 
 فارسی 
 Français 
 Magyar 
 Italiano 
 한국어 
 Kurdî 
 Lietuvių 
 Malagasy 
 Polski 
 Русский 
 Türkçe 
 中文 

 Entry 

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

 See also: Ὕπνος , Ύπνος , and ύπνος 

 Ancient Greek
 [ edit ] 

 Etymology
 [ edit ] 

 From Proto-Hellenic *húpnos , from Proto-Indo-European *supnós ( “ sleep ” ) . Cognate with Sanskrit स्वप्न ( svápna ) and Albanian gjumë < *źúpnos. [ 1 ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /hý.pnos/ → /ˈy.pnos/ → /ˈi.pnos/ 

 ( 5 th BCE Attic ) IPA ( key ) : /hý.pnos/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /ˈ(h)y.pnos/ 

 ( 4 th CE Koine ) IPA ( key ) : /ˈy.pnos/ 

 ( 10 th CE Byzantine ) IPA ( key ) : /ˈy.pnos/ 

 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈi.pnos/ 

 Noun
 [ edit ] 

 ῠ̔́πνος • ( hŭ́pnos )  m ( genitive ῠ̔́πνου ) ; second declension 

 sleep , slumber 

 ( figuratively ) death 

 Inflection
 [ edit ] 

 Second declension of ὁ ῠ̔́πνος ; τοῦ ῠ̔́πνου ( Attic )

 Case / #

 Singular

 Dual

 Plural

 Nominative

 ὁ ῠ̔́πνος 
 ho hŭ́pnos 

 τὼ ῠ̔́πνω 
 tṑ hŭ́pnō 

 οἱ ῠ̔́πνοι 
 hoi hŭ́pnoi 

 Genitive

 τοῦ ῠ̔́πνου 
 toû hŭ́pnou 

 τοῖν ῠ̔́πνοιν 
 toîn hŭ́pnoin 

 τῶν ῠ̔́πνων 
 tôn hŭ́pnōn 

 Dative

 τῷ ῠ̔́πνῳ 
 tōî hŭ́pnōi 

 τοῖν ῠ̔́πνοιν 
 toîn hŭ́pnoin 

 τοῖς ῠ̔́πνοις 
 toîs hŭ́pnois 

 Accusative

 τὸν ῠ̔́πνον 
 tòn hŭ́pnon 

 τὼ ῠ̔́πνω 
 tṑ hŭ́pnō 

 τοὺς ῠ̔́πνους 
 toùs hŭ́pnous 

 Vocative

 ῠ̔́πνε 
 hŭ́pne 

 ῠ̔́πνω 
 hŭ́pnō 

 ῠ̔́πνοι 
 hŭ́pnoi 

 Notes:

 This table gives Attic inflectional endings. For declension in other dialects, see Appendix:Ancient Greek dialectal declension .

 Derived terms
 [ edit ] 

 ἄγρῠπνος ( ágrŭpnos ) 
 ἐνύπνιος ( enúpnios ) 
 ὑπναλέος ( hupnaléos ) 
 ὑπναπάτης ( hupnapátēs ) 
 ὑπνάω ( hupnáō ) 
 ὑπνηλός ( hupnēlós ) 
 ὑπνηρός ( hupnērós ) 
 ὑπνίδιος ( hupnídios ) 
 ὑπνίζω ( hupnízō ) 
 ὑπνικός ( hupnikós ) 
 ὑπνοδότειρα ( hupnodóteira ) 
 ὑπνοδότης ( hupnodótēs ) 
 ὑπνομαχέω ( hupnomakhéō ) 
 ὑπνοποιέω ( hupnopoiéō ) 
 ὑπνοποιός ( hupnopoiós ) 
 Ὕπνος ( Húpnos ) 
 ὑπνοφανής ( hupnophanḗs ) 
 ὑπνοφόβης ( hupnophóbēs ) 
 ὑπνοφόρος ( hupnophóros ) 
 ὑπνόω ( hupnóō ) 
 ὑπνώδης ( hupnṓdēs ) 
 ὑπνώδια ( hupnṓdia ) 
 ὑπνώσσω ( hupnṓssō ) 
 ὑπνωτικός ( hupnōtikós ) 
 ὑπνώω ( hupnṓō ) 

 Descendants
 [ edit ] 

 Greek: ύπνος ( ýpnos ) 

 Mariupol Greek: и́пну ( ípnu ) 

 ⇒ Translingual: Hypnea 

 References
 [ edit ] 

 ^ Beekes, Robert S. P. ( 2010 ), “ ὕπνος ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 
######## 6b434894807c1d8b.txt
Toggle the table of contents 

 sword 

 70 languages 

 Afrikaans 
 Ænglisc 
 العربية 
 Azərbaycanca 
 Беларуская 
 বাংলা 
 Brezhoneg 
 Català 
 Corsu 
 Čeština 
 Cymraeg 
 Dansk 
 Deutsch 
 Zazaki 
 Ελληνικά 
 Esperanto 
 Español 
 Eesti 
 Euskara 
 Suomi 
 Français 
 हिन्दी 
 Hrvatski 
 Magyar 
 Հայերեն 
 Interlingua 
 Bahasa Indonesia 
 Ido 
 Íslenska 
 Italiano 
 日本語 
 Қазақша 
 ភាសាខ្មែរ 
 ಕನ್ನಡ 
 한국어 
 Kurdî 
 Кыргызча 
 Limburgs 
 Lombard 
 ລາວ 
 Lietuvių 
 Latviešu 
 Malagasy 
 Македонски 
 മലയാളം 
 မြန်မာဘာသာ 
 Nederlands 
 Norsk bokmål 
 Occitan 
 Oromoo 
 Polski 
 Português 
 Română 
 Русский 
 Simple English 
 Slovenčina 
 Shqip 
 Српски / srpski 
 Sunda 
 Svenska 
 Kiswahili 
 தமிழ் 
 తెలుగు 
 ไทย 
 Türkçe 
 اردو 
 Oʻzbekcha / ўзбекча 
 Tiếng Việt 
 閩南語 / Bân-lâm-gí 
 中文 

 Entry 

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

 See also: Sword and s-word 

 English
 [ edit ] 

 A sword lying beside its scabbard. 
 The canting arms of Schwerte , Germany, are two swords. 
 Alternative forms
 [ edit ] 

 swerd , sweard , swoord , swoorde , sworde ( all obsolete ) 

 Etymology
 [ edit ] 

 Inherited from West Midland Middle English sword ( swerd in most dialects), from Old English sweord ( “ sword ” ) , from Proto-West Germanic *swerd ( “ sword ” ) , from Proto-Germanic *swerdą ( “ sword ” ) , possibly from Proto-Indo-European *seh₂w- ( “ sharp ” ) . 

 Cognates

 Cognate with North Frisian Swērt , Swiirt , swörd ( “ sword ” ) , Saterland Frisian Swid , Swäid ( “ sword ” ) , West Frisian swurd ( “ sword ” ) , Dutch zwaard ( “ sword ” ) , German Schwert ( “ sword ” ) , Luxembourgish Schwäert ( “ sword ” ) , Vilamovian świert ( “ sword ” ) , Yiddish שווערד ( shverd , “ sword ” ) , Danish sværd ( “ sword ” ) , Faroese svørð ( “ sword ” ) , Icelandic sverð ( “ sword ” ) , Norn svird ( “ small longish object ” ) , Norwegian Bokmål sverd ( “ sword ” ) , Norwegian Nynorsk sverd , svørd ( “ sword ” ) , Swedish svärd ( “ sword ” ) ; also Belarusian све́рдзел ( svjérdzjel , “ drill, drill bit ” ) , Bulgarian свре́дел ( svrédel , “ drill, drill bit ” ) , Czech svider ( “ drill bit ” ) , Polish świder ( “ drill ” ) , Russian сверло́ ( sverló , “ auger, bore, drill, drill bit ” ) , Serbo-Croatian свр̏дло , svȑdlo ( “ auger ” ) , Slovene sveder ( “ drill ” ) , Ukrainian све́рдел ( svérdel ) , све́рдло ( svérdlo , “ drill bit ” ) .

 Pronunciation
 [ edit ] 

 ( General American ) IPA ( key ) : /soɹd/ 
 Audio ( US ) : ( file ) 

 ( Received Pronunciation ) IPA ( key ) : /sɔːd/ 

 ( Standard Southern British , Australia , New Zealand , MLE ) IPA ( key ) : /soːd/
```


## [2026-09-14T03:15:13.516Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/swerd%C4%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%84%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%84%D8%A8%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%AE%D8%AA%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%DB%8C%D9%BE%D9%86%D9%88%D8%AA%DB%8C%D8%B2%D9%85\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 492 verification (Swep/Swer roots)\" ; done"
}
```


### [2026-09-14T03:15:18.243Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/583014f16b8248d5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e28c90e0e4202a97.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ea590bdefd0d0cd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c70b581a31cbcc68.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65ce08b8980c9fa2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d5dfe664bfcba75e.txt
```


## [2026-09-14T03:15:21.900Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nfor f in ['583014f16b8248d5.txt','e28c90e0e4202a97.txt','8ea590bdefd0d0cd.txt','c70b581a31cbcc68.txt','65ce08b8980c9fa2.txt','d5dfe664bfcba75e.txt']:\n    t=open(f,encoding='utf-8').read()\n    print(\"########\",f, t.split('\\n')[3][:80], \"len\",len(t))\n    i=t.find('Toggle the table of contents')\n    if i<0: i=0\n    print(t[i:i+1800])\nEOF"
}
```


### [2026-09-14T03:15:22.869Z] TOOL RESULT

```
######## 583014f16b8248d5.txt TITLE: Reconstruction:Proto-Germanic/swerdą - Wiktionary, the free dictionary len 5395
Toggle the table of contents 

 Reconstruction:Proto-Germanic/ swerdą 

 1 language 

 Français 

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

 This Proto-Germanic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Germanic
 [ edit ] 

 Etymology
 [ edit ] 

 Of disputed origin. Traditionally derived from a Proto-Indo-European *swerdʰ- ( “ sharp tool ” ) , often taken as an extension of *swer- ( “ to hurt ” ) , and compared with Proto-Slavic *svьrdьlъ ( “ drill, auger ” ) . [ 1 ] This is uncertain, however, since all other descendants, such as Proto-Germanic *sweraną , only suggest an original meaning 'to ache, hurt, fester'.

 Alternatively, Nikolaev (2015) [ 2 ] suggests derivation from Proto-Indo-European *sw-er , locative of *seh₂w- ( “ sharp ” ) (with a loss of *h₂ between *s and *w) and cognate to Luwian [script needed] ( šiḫual-, šiwal- , “ sword ” ) , [script needed] ( šiwa- , “ sharp ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈswer.ðɑ̃/ 

 Rhymes: -er.ðɑ̃ 

 Noun
 [ edit ] 

 *swerdą   n [ 1 ] 

 sword 
 Synonyms: *heruz , *mēkijaz , *wibraz 

 Inflection
 [ edit ] 

 Declension of *swerdą (neuter a-stem)

 singular

 plural

 nominative

 *swerdą

 *swerdō

 vocative

 *swerdą

 *swerdō

 accusative

 *swerdą

 *swerdō

 genitive

 *swerdas, *s
######## e28c90e0e4202a97.txt TITLE: خلیدن - Wiktionary, the free dictionary len 3512
Toggle the table of contents 

 خلیدن 

 3 languages 

 فارسی 
 Malagasy 
 Русский 

 Entry 

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

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xa.liː.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [xä.liː.d̪án] 

 ( Dari, formal ) IPA ( key ) : [xä.liː.d̪án] 
 ( Kabuli ) IPA ( key ) : [xä.liː.d̪án] 

 ( Hazaragi ) IPA ( key ) : [xä.li.d̪án] 

 ( Iran, formal ) IPA ( key ) : [xæ.liː.d̪ǽn] 

 ( Tajik, formal ) IPA ( key ) : [χä.li.d̪án] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 xalīdan

 Dari reading ? 

 xalīdan

 Iranian reading ? 

 xalidan

 Tajik reading ? 

 xalidan

 Verb
 [ edit ] 

 خلیدن • ( xalidan ) ( present stem خل ( xal ) ) 

 ( archaic in Iran ) to hurt by introducing a sharp point , to sting 
 11 th Century CE , Fakhruddin As'ad Gurgani , Vis and Rāmin 
 گهی از بهر او خوابش رمیده 
 گهی خارش به دست اندر خلیده gahi az bahr-e 'u xâbaš ramide
gahi xâraš be dast andar xalide Sometimes his (the gardener's) sleep has been disturbed because of it (the rose),
sometimes its thorn has cut his hand. 

 Derived terms
 [ edit ] 

 خلش ( xaleš ) 

 References
 [ edit ] 

 Dehkhoda, Ali-Akbar ( 1931– ), “ خلیدن ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda 
######## 8ea590bdefd0d0cd.txt TITLE: خوره - Wiktionary, the free dictionary len 4926
Toggle the table of contents 

 خوره 

 4 languages 

 فارسی 
 Kurdî 
 Malagasy 
 پښتو 

 Entry 

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

 See also: جوزة and حوزه 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 From خور ( xor , present stem of خوردن ( xordan , “ to eat ” ) ) +‎ ـه ( -e ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xʷa.ˈra/ 

 ( Dari, formal ) IPA ( key ) : [xʊ.ɾá] 

 ( Dari, formal ) IPA ( key ) : [xʊ.ɾá] 
 ( Kabuli ) IPA ( key ) : [xʊ.ɾá] 

 ( Hazaragi ) IPA ( key ) : [xu.ɾá] 

 ( Iran, formal ) IPA ( key ) : [xo.ɹé] 

 ( Tajik, formal ) IPA ( key ) : [χu.ɾá] 

 Rhymes: -a 

 Readings

 Classical reading ? 

 xwara

 Dari reading ? 

 xura

 Iranian reading ? 

 xore

 Tajik reading ? 

 xura

 Noun
 [ edit ] 

 خوره • ( xore ) ( plural خوره‌ها ) 

 leprosy 
 Synonym: جذام ( jozâm ) 

 ( idiomatic ) obsession , fascination (for something, e.g. a hobby)

 ( obsolete ) Any serious disease considered to " eat away " at the patient, not just leprosy. 
 c. 1599 , Bahāʾ al‐Dīn ʿĀmilī , کشکول ‎ [1] : حکومت حجاج بر عراق بیست سال طول کشید. و آخرین کسی را که بکشت سعید بن جبیر بود. در آخر کار به خوره‌ ی شکم مبتلا شد. hukūmat-i hajjāj bar irāq bīst sāl tūl kašīd. u āxarīn kasē rā ki bikušt sa'īd bin-i jabīr būd. dar āxar-i kār ba xwara -yi šikam mubtalā šud. Al-Hajjāj 's government over Iraq lasted for twenty years, and the last person he kill
######## c70b581a31cbcc68.txt TITLE: خلبان - Wiktionary, the free dictionary len 3276
Toggle the table of contents 

 خلبان 

 5 languages 

 فارسی 
 Magyar 
 Bahasa Indonesia 
 Kurdî 
 Malagasy 

 Entry 

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

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: خلبان 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 خله‌بان ( xale-bân ) 

 Etymology
 [ edit ] 

 From خله ( xale , “ helm , oar ” ) +‎ ـبان ( -bân ) . Purism that replaced پیلت ( pilot ) from French and طیاره‌چی ( tayyâre-či ) from Ottoman Turkish in Iranian Persian.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xal.ˈbaːn/ , /xa.la.ˈbaːn/ 

 ( Iran, formal ) IPA ( key ) : [xæl.bɒ́ːn] , [xæ.læ.bɒ́ːn] 

 Rhymes: -aːn 

 Readings

 Classical reading ? 

 xalbān, xalabān

 Iranian reading ? 

 xalbân, xalabân

 Noun
 [ edit ] 

 Dari

 پیلوت 

 Iranian Persian

 خلبان 

 Tajik

 лётчик 

 خلبان • ( xalbān, xalabān / xalbân, xalabân ) ( plural خلبانان ( xalbānān, xalabānān / xalbânân, xalabânân ) ) 

 ( Iran ) pilot ; aviator 
 Synonyms: هوانورد ( havâ-navard ) , ( obsolete ) طیاره‌چی ( tayyâre-či ) , ( obsolete ) پیلت ( pilot ) 

 ( archaic ) oarsman , rower 
 Synonym: پاروزن ( pâru-zan ) 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=خلبان&oldid=92301459 "

 Categories : Persian terms suffixed with ـبان 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/aːn 
 Rhymes:Persian/aːn/2 syllables 
 Rhymes:Persian/aːn/3 sy
######## 65ce08b8980c9fa2.txt TITLE: بختک - Wiktionary, the free dictionary len 2819
Toggle the table of contents 

 بختک 

 2 languages 

 فارسی 
 Malagasy 

 Entry 

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

 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /bax.ˈtak/ 

 ( Dari, formal ) IPA ( key ) : [bäx.t̪ʰäk] 

 ( Dari, formal ) IPA ( key ) : [bäx.t̪ʰäk] 
 ( Kabuli ) IPA ( key ) : [bäx.t̪ʰäk] 

 ( Hazaragi ) IPA ( key ) : [bäx.t̪ʰäk] 

 ( Iran, formal ) IPA ( key ) : [bæx.t̪ʰækʰʲ] 

 ( Tajik, formal ) IPA ( key ) : [bäχ.t̪ʰäk] 

 Rhymes: -ak 

 Readings

 Classical reading ? 

 baxtak

 Dari reading ? 

 baxtak

 Iranian reading ? 

 baxtak

 Tajik reading ? 

 baxtak

 Noun
 [ edit ] 

 بختک • ( baxtak ) 

 An evil spirit in Iranian folklore equivalent to Germanic mare ; nightmare .

 ( figuratively ) Any bad , miserable , difficult or terrifying situation or experience.

 Synonyms
 [ edit ] 

 درفنجک ( darfanjak ) 

 فرانجک ( farânjak ) 

 دیونسپرک ( divnesparak ) 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=بختک&oldid=91032759 "

 Categories : Persian terms with IPA pronunciation 
 Rhymes:Persian/ak 
 Rhymes:Persian/ak/2 syllables 
 Persian lemmas 
 Persian nouns 

 Hidden categories: Pages with entries 
 Pages with 1 entry 

 This page was last edited on 1 June 2026, at 07:50.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms m
######## d5dfe664bfcba75e.txt TITLE:  len 180
URL: https://en.wiktionary.org/wiki/%D9%87%DB%8C%D9%BE%D9%86%D9%88%D8%AA%DB%8C%D8%B2%D9%85
FETCHED: 2026-09-14T03:15:18Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T03:15:38.766Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la incoming/FFD/; python3 - <<'EOF'\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"leaves\",len(pages))\nfor leaf in (54,55,56):\n    print(\"=== leaf\",leaf)\n    print(pages[leaf][:1500])\nEOF"
}
```


### [2026-09-14T03:15:39.826Z] TOOL RESULT

```
total 1452
drwxrwxr-x  3 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 1301330 Sep  4 14:06 FFD_asmaneketab.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  170624 Sep  4 14:06 FFD_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  4 13:19 FFD_pages.txt.pages
leaves 115
=== leaf 54
[pdf page 55]
وا فعلهای فارسی دری
خرامیدن
«خرامید» ماد ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
: «خرام» < فارسی میانه 337370 < ایرانی باستان 3+737-8*. برای ۵ > آرای. 3
پیشوند فعلی است. ۳370 صورت بالاندةٌ ريشهٌ 77870 است و 77870(«گامبرداشتن» معنی
می‌دهد.
خریدن
خرید < فارسی میانه 7770 < ایرانی باستان 3۳7-1۵*. برای 14 -> آراست. 77 صورت
ضعیف 727 است و آن به معنی «خریدن» است.
خر + فارسی‌میانةٌ مانوی 37. 77 در فارسی‌میانهٌ مانوی و «خر» در فارسی دری‌به این
سبب به وجود آمده‌اند که تصور شده «خرید» مادهٌ ماضی جعلی است و با حذف ۲4مادة
مضارع به وجود می آید. مادةٌ مضارع 3374 در فارسی میانه 778 است» از ایرانی باستان
8 83 نشاته‌ای بوده که برای ساختن ماده مضارع از ريشه به کار می‌رفته است ->
بریدن,
خزیدن
«خزید» ماده ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خز < پهلوی اشکانی 382. فارسی میانهٌ مانوی 782 < ایرانی باستان ۶۵2-۵
3-2 برای 2 > آرای. 2 صورت افزوده و 7 صورت ضعیف ريشه هستند. 1817 به
معنی «خزیدن» است.
خست + فارسی‌میانه 3881 < ایرانی باستان 3۵9-1۵*. برای 18-> آراست. 740 صورت
اصلی 8 است. 4 پیش از 1به 8 بدل شده است. ريشةٌ 24 به معنی «پاره کردن» است.
خفت < فارسی میانه 911 < ایرانی باستان ۳۵۶-۵". برای 1۵ -> آراست. 1:۸0

=== leaf 55
[pdf page 56]
ماده‌های ماضی و مضارع فارسی دری --___شش ۵۱
صورت اصلی 3 است.» 0 پیش از ۲ به ۶ بدل شده است.
خواب < فارسی میانه 330: اسم است» در فارسی دری «خواب» به عنوان مادهٌ
مضارع «خفتن» به کار رفته است. ماده مضارع در فارسی میانه کته است.
بازماندهٌ ۹۷۵۵۵* ایرانی باستان. ۵۸:* ساخته شده است از ۸82 با بدل‌شدن 0 به ؟
پیش از 8 و 82 8 برای ساختن مادةٌ آغازی از ريشه به کار می‌رفته است. برای 2 آرای.
در فارسی دری از «خفس» که به صورتهای «خسپ» و «خسب» هم به کار رفته. مادهٌ
ماضی جعلی ساخته شده است: خفسید., خسپید, خسبید.
خندیدن
خندید < فارسی میانه ۰۵414 مادهٌ ماضی جعلی است. از ماده مضارع ساخته
شده است. َ
خند < فارسی میانه 75384 < ایرانی باستان ۰*۵4 380 در فارسی میانه و ایراتی
باستان» «خندیدن» معنی می‌دهد.
خواستن
خواست < فارسی میانه 7۳391« ایرانی باستان 9-1۵:*. برای اه آراست. 7۷36
صورت اصلی ۷38 است. 4 پیش از ۲ به 5 بدل شده است. ۷30 به معتی «خواستن»
است.
خواه + فارسی میانه ۳:5 < ایرانی باستان -۷۷24:*. برای ۵ -> آرای.
خواندن
خواند + فارسی میانه ۷384 < ایرانی باستان 1:۵۵-1۵*. برای 18 > آراست. ريشةٌ :
31 به معنی «بانگ کردن» است.
خوان < فارسی میانه ۷۸37 < ایرانی باستان -۳۷3:*. برای ۵ > آرای. 1۷۷3۵
صورت بالاندةٌ ۷۵2 است.

=== leaf 56
[pdf page 57]
فعلهای فارسی دری
خوردن
خورد + فارسی میانه ۷۵7۵4 + ایرانی باستان ۷۷۵۲-1۵*. برای 2 آراست.
: خور + فارسی میانه 5۷۵7 < ایرانی باستان ۴*3۵۲-۵. برای 8 -> آرای.
و 3۷/8۲ به معنی (خوردن» و «نوشیدن» هر دو به کار رفته‌اند.
خوشیدن
«خوشید» مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خوش « فارسی میانه 355 < ایرانی باستان 8۸۵05-8*. برای ۵ -> آرای. ريشةٌ 1205 به
معنی «خشک شدن» است.
واژةٌ «خشک» از ريشهٌ ۳203 گرفته شده است. صورت فارسی ميانةٌ آن 1031 است. از
ایرانی باستان 8۵5-2*. 1805 صورت ضعیف ريشه و 1۵ پسوند است.
دادن
داد < فارسی میانه 434 < ایرانی باستان 43-12*. برای "18 > آراست. ريشهٌ 45
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
```


## [2026-09-14T03:16:00.608Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ncd /home/sfmqrb/git/rishe\npdftoppm -f 55 -l 56 -r 200 -png /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd492 && ls /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-14T03:16:02.522Z] TOOL RESULT

```
391-top.png
394hi.png
394-zoom.png
400-bot.png
400-top.png
404-top.png
411-top.png
412-zoom.png
414-bot.png
417hi.png
417-top.png
417-zoom.png
421-top.png
428hi.png
428-zoom2.png
428-zoom.png
429hi.png
429-zoom.png
431-top.png
432-bot.png
436-full.png
440-top.png
442hi.png
442-zoom.png
444hi.png
444-zoom.png
445-mid.png
446-full.png
450hi.png
450-zoom.png
454-top.png
457hi.png
457-zoom.png
460-top.png
462-full.png
466hi.png
466-mid.png
472-top.png
474hi.png
474-zoom.png
afm74-420.png
afm76-421.png
agents.txt
ahd430.txt
asha-468.txt
beekes410.txt
bly78-473.png
bqt1328-ftr-437.png
bqt1328-hdr-437.png
bqt1328-top-437.png
bqt1330-top-437.png
bqt1-440.txt
bqt2123-fn-435.png
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
bqt439-l254.jpg
bqt469-n486-bottom.png
bqt469-n486.jpg
bqt469-n486-top.png
bqt469-n547-bottom.png
bqt469-n547-fn2.png
bqt469-n547-hdr.png
bqt469-n547.jpg
bqt469-n547-mid.png
bqt469-n547-top.png
bqt-482-389-foot.png
bqt-482-389.jpg
bqt-482-390-foot2.png
bqt-482-390-foot.png
bqt-482-390.jpg
bqt508-495-bl2.png
bqt508-495-bl.png
bqt508-495.jpg
bqt509-495.jpg
bqt509-495-tr.png
build2-434.py
build2-471.py
build3-434.py
build-389.py
build-390.py
build-391.py
build393.py
build-394.py
build-395.py
build-396.py
build-398.py
build-400.py
build-401.py
build-405.py
build-406.py
build-407.py
build-412.py
build-414.py
build-415.py
build-417.py
build-418.py
build-419.py
build-422.py
build-425.py
build-426.py
build-428.py
build-429.py
build-430.py
build-431.py
build-434.py
build-435.py
build-438.py
build-439.py
build-440.py
build-444.py
build-445.py
build-446.py
build-447.py
build-448.py
build-450.py
build-452.py
build-453.py
build-454.py
build-455.py
build-458.py
build460.py
build-461.py
build-463.py
build-464.py
build-465.py
build-468.py
build-470.py
build-471.py
build-472.py
build-473.py
build-474.py
c404-empty.png
c404-greek.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
c412_cedar.png
c412_makrome.png
c412_makrome_zoom.png
c412_meqrameh.png
c412_meq_zoom.png
c412_sedr_zoom2.png
c412_sedr_zoom.png
c442-fa8b.png
c442-fa8c.png
c442-fa8.png
c442-samavar2.png
c442-samavar3.png
c442-samavar.png
c442-symp-zoom2.png
c442-symp-zoom.png
c497-arabic.png
c497-shakuk.png
crop14-394.png
crop18-394.png
crop411_a.png
crop411_b.png
crop411_c.png
crop419_a.png
crop419_b.png
crop419_c.png
crop419_d.png
crop419_grk.png
crop419_skt.png
crop428a.png
crop428b.png
crop428c.png
crop428d.png
crop-437.png
crop460-fa.png
crop460-latin.png
crop460-mithere.png
crop460-shamunhdr.png
crop460-shamun.png
crop468a.png
crop480_astro.png
crop480_chol2.png
crop480_chol.png
crop480_ster.png
crop491b.png
crop491c.png
crop491.png
crop496-a.png
drd496.wiki
e0-434.json
edit_about.py
edit_research.py
ffd492-055.png
ffd492-056.png
ffprof
gen-420.py
irn-425.pdf
irn-425.txt
kent2-448.txt
kent-448.txt
knt-440.txt
knt443.txt
meta-443-knt.json
oew459.txt
out488.bin
part1-471.json
pg390b.jpg
pg390b.png
pg390.png
pg391big.png
pg391crop.png
pg391.png
pg391root.png
pg391sog.png
pg392.png
pg393.png
pg394hi.png
pg394.png
pg397.png
pg398.png
pg399-crop1.png
pg399-greek.png
pg399.png
pg399-sog.png
pg400big.png
pg400_fa_heli.png
pg400_fr2.png
pg400_french.png
pg400_kasak2.png
pg400_kasak3.png
pg400_kasak.png
pg400.png
pg402.png
pg404hi.png
pg404.png
pg405.png
pg406.png
pg407.png
pg408-ampus.png
pg408-germ.png
pg408.png
pg409.png
pg410hi.png
pg410-k2.png
pg410-kadm2.png
pg410-kadm.png
pg410-persian.png
pg410.png
pg410-q2.png
pg410-qedam.png
pg411_300.png
pg411.png
pg412_hi.png
pg412.png
pg412_uhi.png
pg413.png
pg414-greek.png
pg414.png
pg415-emptybox.png
pg415hi.png
pg415.png
pg416-v.png
pg417.png
pg418hi.png
pg418.png
pg418-raj2.png
pg418-raj3.png
pg418-rajidan.png
pg419_hi.png
pg419.png
pg420b.png
pg420.png
pg421.png
pg422.png
pg423.png
pg424.png
pg426.png
pg428hi.png
pg428.png
pg429-crop1.png
pg429-crop2.png
pg429-crop3.png
pg429hi.png
pg429.png
pg431.png
pg432.png
pg433.png
pg435-n1.png
pg435-n4.png
pg435.png
pg436.png
pg437-437.png
pg437hi-437.png
pg438.png
pg439.png
pg440.png
pg442hi-442.png
pg442-p442.png
pg442uhi-442.png
pg443.png
pg444.png
pg444-serom.png
pg444-sibum.png
pg445-crop.png
pg445.png
pg446.png
pg447-crop.png
pg447.png
pg449.png
pg450hi.png
pg450-pechkam.png
pg450.png
pg450-shangarf.png
pg451.png
pg452.png
pg453.png
pg454.png
pg456-germ.png
pg456hi.png
pg456.png
pg457_crop3b.png
pg457_crop3c.png
pg457_crop3.png
pg457hi.png
pg457.png
pg458.png
pg459.png
pg460hi.png
pg460.png
pg462-fa.png
pg462hi.png
pg462.png
pg462-sog2.png
pg462-sog.png
pg463-v.png
pg464.png
pg465.png
pg466-crop1.png
pg466-crop2.png
pg466-crop3.png
pg466hi.png
pg466-osqof.png
pg466.png
pg467.png
pg468hi.png
pg468.png
pg469.png
pg470.png
pg471.png
pg472-crop.png
pg472hi.png
pg472.png
pg473.png
pg474.png
pg474-sogd.png
pg475.png
pg476.png
pg477.png
pg479.png
pg480hi.png
pg480.png
pg482.png
pg484.png
pg486.png
pg487.png
pg488.png
pg490.png
pg491big.png
pg491.png
pg494hi.png
pg494.png
pg494-root.png
pg494-tambour.png
pg495.png
pg496hi.png
pg496.png
pg497.png
pla18-468-crop.png
pla18-468.png
queue.txt
sem410.html
u_mak.png
u_meq.png
u_sedr.png
write397.py
write-402.py
write409.py
write410.py
write436.py
write469.py
write476.py
```


## [2026-09-14T03:16:05.420Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd492-055.png"
}
```


### [2026-09-14T03:16:05.445Z] TOOL RESULT

```

```


## [2026-09-14T03:16:11.889Z] TOOL CALL #68: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd492-056.png"
}
```


### [2026-09-14T03:16:11.916Z] TOOL RESULT

```

```


## [2026-09-14T03:16:34.307Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/FFD\ncat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/FFD/50.vision.txt <<'EOF'\nAbolghasemi, Fe'l-ha-ye Farsi-ye Dari (FFD), printed p. 50 (PDF page 55) — read from the scan\n(pdftoppm -f 55 FFD_asmaneketab.pdf), used for rishe page 492 entry 0 (root Swep/Sup 1).\n\nخفتن\nخفت ← فارسی میانه xuft ← ایرانی باستان *xwaf-ta. برای ta ← آراست. xwap\n[continues on p. 51:] صورت اصلی xwaf است، p پیش از t به f بدل شده است.\n\n--- printed p. 51 (PDF page 56), continuation used for the same node ---\nخواب ← فارسی میانه xwāb: اسم است، در فارسی دری «خواب» به عنوان مادهٔ مضارع «خفتن»\nبه کار رفته است. مادهٔ مضارع xuftan در فارسی میانه xufs است، بازماندهٔ *xwafsa ایرانی\nباستان. *xwafsa ساخته شده است از xwap، با بدل‌شدن p به f پیش از s، و sa و s برای ساختن\nمادهٔ آغازی از ریشه به کار می‌رفته است. برای a ← آرای. در فارسی دری از «خفس» که به\nصورت‌های «خسپ» و «خسب» هم به کار رفته، مادهٔ ماضی جعلی ساخته شده است:\nخفسید، خسپید، خسبید.\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd492-055.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/FFD/50.png\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd492-056.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/FFD/51.png\nls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/FFD/"
}
```


### [2026-09-14T03:16:34.425Z] TOOL RESULT

```
50.png
50.vision.txt
51.png
77.png
77.vision.txt
```


## [2026-09-14T03:16:35.970Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG xwap/hufs\"; grep -n \"xwap\\|hufs\\|\\*xwafs\" CHEUNG.txt | head -20; echo \"=== CHEUNG xar/xal pierce\"; grep -n \"^\\*xar\\|^\\*xard\\|to prick\\|to pierce\" CHEUNG.txt | head -20"
}
```


### [2026-09-14T03:16:36.048Z] TOOL RESULT

```
=== CHEUNG xwap/hufs
=== CHEUNG xar/xal pierce
17430:*AVESTAN: (+ *а-) ? YAv. aman- ‘to pierce, bore ? || (+ *ui-) YAv. vaéman- ‘to 
22650:*skard ‘to pierce (through)’ 
22672:*PIE *skerd"- ‘to pierce, cut? > LIV: 558 | Pok.: 545, 923 f., 940 f. 
23183:*NWIR: NP sipöxtan/sipöz- ‘to prick, pierce, transfix, thrust, poke; to draw forth one 
24004:*su(m)p/b ‘to pierce, bore 
24005:*MIDDLE PERSIAN: BMP swmb- /sumb-/ ‘to pierce, bore’ 
24009:*SOGDIAN: BSogd. swnp-, CSogd. swb-, MSogd. swmb- ‘to pierce, bore’ 
24014:*CHORESMIAN: snb- ‘to pierce’ > Samadi: 184 
24016:*NWIR: NP suftan/sumb- ‘to pierce, bore’, Bal. supt, sumbit/sumb-, (EHB) 
24017:subt'-/sub- ‘to pierce’ (< NP ?) 
24773:*tard ‘to pierce, split’ 
24787:*SANSKRIT: tard ‘to split, to pierce’ (RV+) = EWAia I: 634 
24789:«PIE *terd- ‘to pierce’ = LIV: 631 | Pok.: 1076 
26128:wof-/wofta ‘to weave’ || (+ *pati-) ? Pash. pewd-, pey- ‘to pierce, transfix; string, 
26649:*KHOTANESE: bid- (br, bi(^)s-) ‘to pierce’ || (+ *ham-) OKh. hambit- ‘to pierce’. Q 
28399:(+ *ham-) BSogd. "nyó- ‘to prick, pierce’ 
28608:*xar 443 
28641:*xar ‘to go, pass’ 
28687:*xard ‘to defecate’ 
57287:to pierce
```


## [2026-09-14T03:16:41.271Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hwap\\|\\*xwap\\|xwafs\\|xufs\" CHEUNG.txt | head -20; echo \"=== xal\"; grep -n \"^\\*xal\\|xalidan\\|xal-\\b\\|xalīdan\" CHEUNG.txt | head -20"
}
```


### [2026-09-14T03:16:41.344Z] TOOL RESULT

```
10216:*MIDDLE PERSIAN: MMP xwpt (pret. stem), BMP hwps- /xufs/ (HLMWN-) ‘to 
35241:hwps- /xufs-/, 145 
49417:xufs-/xuvd, 146 
=== xal
```


## [2026-09-14T03:16:43.105Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10190,10250p' CHEUNG.txt"
}
```


### [2026-09-14T03:16:43.163Z] TOOL RESULT

```
*IE COGNATES: Lat. sonere, sonare ‘to sound, to ring’, sonus (m.) ‘noise, sound’, OE 
swinn ‘music’ 

*REFERENCES: Horn 1893: 3; KPF I: 137b, 206a; KPF II: 193; Christensen, Contributions I: 69 f., 63, 159, 
258; Christensen, Contributions II: 53, 113, 157; IIFL II: 552b, 193b; Abrahamian 1936: 125, 134; 
Lambton 1938: 77b; MacKenzie 1966: 111; Yarshater 1969: 183; EVS: 86b, 99b; WIM I: 70; DKS: 502a 
f£; WIM II/1: 79; Blau 1980: 269b; WIM III: 112; Omar 1992: 690a; Werba 1997: 330 Е; Paul 1998: 


318b; Cabolov 1997: 76; Abaev, Slovar’ IV: 253, 214; Steblin-Kamenskij 1999: 415; Lecoq 2002: 124, 
126 (passim); Korn 2005: 122, 411 (passim) 


*huap/f ‘to sleep’ 
*AVESTAN: Y Av. x"ab- (x'af-) ‘to sleep’ || (+ *aua-) ‘to go to sleep, fall asleep’ || (+ 


*ni-) caus. ‘to put to sleep’ = Liste: 17f. 

Pres. {1} da-: IND. med. 3pl. YAv. auuanhabdonte (N 52, N 53), OPT. med. 3sg. YAv. auuaghabdaeta (V 
4.45); Pres. {2} inch.: IMPV. 2sg. YAv. x'afsa (V 18.16, V 18.24), 2р1. x'afsata (H 2.42, rep.); Perf.: 
IND. 3sg. YAv. husx'afa (Y 57.17); Partic.: pres. med. YAv. auuay’habdomna- (H 1.11), perf. pass. YAv. 
x'apta- (V 18.46); Caus. da-: pres. IND. 3sg. YAv. nix’abdaiieiti (V 18.16, V 18.24) 


*MIDDLE PERSIAN: MMP xwpt (pret. stem), BMP hwps- /xufs/ (HLMWN-) ‘to 


sleep? = DMMPP: 368b 
Partic.: perf. pass. MMP xwpt’n (pl.), BMP hwptk /xuftag/ 


*PARTHIAN: xwsp- (inch.) ‘to fall asleep, sleep’. Ф The Wir. (notably Pth.) initial 
segment h(a)sp- seems to reflect *ham-su-, whereas the rear segment points to 
influence of *saiH! ‘to lie down, go to sleep’, cf. ppp. *si(H)ta-, nomin. *sai(H)ana-. 
= Ghilain: 95 | DMMPP: 369b 

Pres.: SUBJ. 3sg. xwsp’; Partic.: perf. pass. xwft, xwft, (pl.) xwftg’n 

*KHOTANESE: (h)us- ‘to sleep’ || (+ *aua-) um- (denomin.) ‘to fall asleep’ (< 
*aua-huaf-na-) || (+ *ui-) ? vau’s- (vo’-) ‘to faint’. 0 The origin of Khot. vau’s-/vo’- 
‘to faint’ needs some further clarification. According to Sims-Williams 1983: 49f., 


146 *huap/f 


the Khot. forms derive from aua-Suafsa-/*aua-Suafta- with secondary Zë Emmerick 
(SVK II. 134) remarks that the reconstruction remains a theoretical construct with 
no close parallel elsewhere. Perhaps, one may need one assumption less if the Khot. 
forms are rather prefixed with *ui- (which would perfectly explain *š due to ruki). 
The ui-formation does have a Skt. correspondence (albeit a late one):visupta-. 
c SGS: 154, 19, 125 

*SOGDIAN: CSogd. ?$рп- (denomin.) ‘to rest’ || (+ *aua-) BSogd. wBs-, CSogd. ’wfs- 
*to sleep, fall asleep* 

Pres.: OPT. 3sg. CSogd. ’spny; Impf.: IND. 3sg. CSogd. mspn || (+ *aua-) Impf.: IND. 3sg. BSogd. w’Bs, 
CSogd. w’fs; Perf.: intr. SUBJ. 3sg. dur. MSogd. ’wBtyy *’skw’t ‘should be asleep’; Partic.: perf. pass. 
CSogd. "wbc (f. ‘asleep’, CSogd. "wbtytpl., MSogd. "wftyy; Inf.: pret. SSogd. ’wBt
```


## [2026-09-14T03:16:58.305Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB\"; grep -n \"xwamn\\|xwâb\\|xwāb\\|xufs\\|xuft\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T03:16:58.359Z] TOOL RESULT

```
=== NYB
4302:xuftan [hwptn'; HLMWN-tn'] x"afs-, to sleep, to fall asleep 52. 6%. 32%, — Av. (1862) x"ap-, pres. xtafsa-; MPrthPrs xwftn; Paz. x"aftan, pres. avaft-, xtafs-; NP xuftan, xuspidan, pres. xuab-.
5226:x'"andra-kara-: *xYandrai xUanira0a: x"anirah xUap-: xuftan x"ápara-: xYāpar x" ar-: xUartan xUar-(xUan-)sand: xUansand xUarenah-: xVarrah xYaronahvant: farraxu xUasta-: xUastan x"ato: xUat x"áOra-: xuahr
6213:xwftn: xuftan
6906:x"aftan, xUaft-, xUafs-: xuftan
7502:xuda: xtatai xuftan, xuspidan: xuftan xuk: ?x"àr
```


## [2026-09-14T03:16:59.778Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index SWEP/SWER\"; grep -n -i \"SWEP\\|SWER\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -20; echo \"=== ARY fa\"; grep -n \"خواب\\b\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-14T03:16:59.851Z] TOOL RESULT

```
=== ARY latin index SWEP/SWER
9195:KNA  yswepisH) ped TAN ABALUCHI) gr she
=== ARY fa
1068:دختران را به اسیری ببرند. از این اسیران یا بردگان هم بعنوان همخوابه و هم خدمتکار استفاده می‌شد.
7196:بازگشت به آخواب" و آخواییدن".
7243:خراب, خوابیدن / ۲۴۷
7269:در زبان‌های ایرانی برای "خواب" (به چم "خفتن") و "خراب" (به چم "آنچه در خواب دیده می‌شود") یکك واژه‌ی
10420:۲ چم این واژه در زبان‌های ژرمنی: روی تخم خوابیدن؛ به وجرد آوردن,
11686:چم این واژه در زبان لاتین: چهارچوب تختخواب,
13333:۰ | لالايي لای لای (به چم "آواز برای خواباندن کودک»)
13346:چم این واژه در زبان‌های ژرمنی: سکوت و آرامش؛ بی سرو صدایی و سکون؛ خواباندن.
```


## [2026-09-14T03:17:05.576Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7240,7300p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T03:17:05.631Z] TOOL RESULT

```
افغانی (پشتو) (/4۳0/7۸۷)+ 0 ۸ 81۸3۸۸
مس
[pdf page 246]
خراب, خوابیدن / ۲۴۷
ارمنی (045۸1۸۸ق۸): 01۷ ,الا لیتوانی ((۸(/1۸نالل 7 ):
یونانی (07287): ۰ 11۳۳۲085 ,7111۳۸05 85 ,85477۸5
لاتین (۸71۸ل): نونی (لتی) (۸7/1۵07ما): 5
5 ,95020875 ,50808 ,80210 ایرلندی کهن (نلکلقا 07.0): ان
فرانسه (۳8۸/7): دازون گالی (9لولانا0۸): 111
اسپانیایی (52۸۸/377): ردان ولزی (7لک): 17
ایتالیایی (4له7/). رانا زان برتونی (875700): 1 ,13172
رومانی (۸1۸(14): لدانزان آلبانی (لفاالم‌قلم. تاره
پرتغالی (۳0700105588: ۰ 507 ,508110 هنبت (7177178): ان
ایسلندی کهن (/(210۸14بهفی5 صا0):
ب5757[۸ بغ[80 پسگشت‌ها ۲2۲2۲۵5
ساکسونی کهن 54300۸0 010): 5178881۸01 9 ۶0/0300
فریزی کهن (97ف51ل۲۶ 010): :امه
7 817۲852 1 (1773۵710) ,1034 (3014۳0211)
آلمانی کهن ((027(44 03ات صاه): 237 نقق منم لط0
لد اد ین :۸2052/215
انگلیسی کهن (8(01/5 طا0): 1 (0۸8۸31) ,133 (51.557)
7 5178۸ 270 : ماه
اسلاوی کهن (ع۷7ها5 تل#6ناتزه صا0): 348 60 :0۸/0/5
1 ,81۳۸1 1 (90۱/3018365) ود
لهستانی (۳0/87)+ ۳ ,852 ۸2/100
روسی (0۷فا55تا): 7 800 7 (51587) ,کا2 (273۸4)
صربی (587814/4): 7 ]5۳۸۷۸7۲ ,لال8۸ برهان قاطم + ۷۸۰
برهمی (80118211424): 1 588
او ی :
در زبان‌های ایرانی برای "خواب" (به چم "خفتن") و "خراب" (به چم "آنچه در خواب دیده می‌شود") یکك واژه‌ی
۱ واحد بکار می‌رود ولی در اکثر زبان‌های اروپایی برای این دو حالت دو واژه‌ی تمایز بکار می‌رزد. گاهی این دو
: واژه همريشه و گاهی ناهمریشه‌اند. در این فهرست واژه‌های همریشه وابسته به هر دو حالت داده شنده است. :
۱ ۰
[pdf page 247]
۸ / خواستن, خواست
آوستابی (4287/۷): یناه لیتوانی (۸۷ال۸تا 77 7آا): دا دا ری
بهلری (۲1اهاتزهه): ۸7
کردی (180150)): پسگشت‌ها ۹ ۸8782265
08710 ,20/۸8712 0 ۸000
سانسکریت (5275807): 26 نقققماتساطط
5 8۷۸2-870۸7 9 (۷۸۲) :25( ۸
آرمنی (۸ا/2452/): 0۸۴ 9 (81۸0) 57
برنانی (07888): تف800(1 ,11500۸1۸ 1 (088138) :۸10
این (0710): 5۷۸0585 ,8۷۸080 برهان قاطع : ۷۸۳
بادداشت:
۱ بازگشت به: شیرین.
فارسی (/۳881۸4): خوال (به چم "دو ده‌ای که برای ساختن مرکب از دود چراغ می‌گیرند")
اوستی (08557/6): ۸۲ دانمارکی (0۸۸/187): اک زان
سغخدی (/90001۸): نی نید سرئدی (317810150): این
خُتنی (2707۸/1885): 112۸۸ نروژی (/(0/05014: لاد
لاتین (/47): ۰ 9080588۳ ,8507255 هلندی (0076(7): اي ۸۷
گرتیک (007710): دی اد
نورس کهن (۸0782 010): دای امد پسگشت‌ها ۸5
ساکسونی کهن (54:00۷ ۰:01 8۷۷۸۲ 6 200220
فریزی کهن (۷لفا8لج7 صرا0): داد 0 (8۸35) 80
آلمانی کهن (/050/40 ۱۵ صا0): 3 داان :5/ نم ظ الما
4 برهان قاطع : ۷۸۲
آلمانی (0882/(۷): اما اند هن لغت‌نامه دهخدا: ۱۰۰۳۷
انگلیسی کهن 8۸۷01820 2ت0): 8۷/8۸7 فرهنگ معین : ۱۳۳۹
انگلیسی (50/ا8(/0): لا اون
ا
```


## [2026-09-14T03:17:16.336Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 492 -l 492 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg492 && echo ok"
}
```


## [2026-09-14T03:17:17.854Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN sleep\"; grep -n \"4.6[0-9]\\? *SLEEP\\|SLEEP (vb.)\\|SLEEP (sb.)\" SYN.txt | head; echo \"=== SYN sword\"; grep -n \"SWORD\" SYN.txt | head"
}
```


### [2026-09-14T03:17:18.146Z] TOOL RESULT

```
ok
```


### [2026-09-14T03:17:18.218Z] TOOL RESULT

```
=== SYN sleep
6908:4.61 SLEEP (vb.; sb.)
=== SYN sword
34804:20.27 SWORD Grk.  Elos, paxatpa Goth. hairus, méki (acc. sg.) Lith. kalavijas, kardas NG orabl, Elpos (lit.) ON sverd, mekir, hjorr Lett. zuobens Lat.  gladius, énsis (poet.), Dan. svard ChSl. met, kor(ti)da spatha (late) We svdrd SCr. maé It. spada OE sweord, méce, heoru Boh. meé Fr. épée (glaive) ME _ swerd Pol. miecz Sp. espada NE sword Russ. meé Rum. sabie, spadé Du. zwaard Skt. _asi-, khadga- Ir. claideb, colg OHG - swert Av. karata- Nir. clatdheamh MHG ss swert W. cleddyf NHG | schwert
```


## [2026-09-14T03:17:20.438Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6908,6960p' SYN.txt; echo \"@@@ sword text\"; sed -n '34804,34830p' SYN.txt"
}
```


### [2026-09-14T03:17:20.529Z] TOOL RESULT

```
4.61 SLEEP (vb.; sb.)
Grk.  xafebdw, xotpdopac; Goth. slépan; sléps Lith, miegoti; miegas
ixvos ON sofa; svefn Lett.  mieguot; miegs NG Koodpae (-Gyar); Dan. — sove; sdun ChSl.  stipati; stint
iavos Sw. sova; sémn SCr.  spavati; 8an, spavanje Lat. dormire; somnus OE sl@pan, swefan; sl@p, Boh. spat; spant, spdnek It. dormire; sonno swefn Pol. spac; sen, spanie Fy. dormir; sommeil ME slepe; slepe Russ. spat’; son, span'e Sp. dormir; suefio NE sleep; sleep Skt. svap-, dra-; svapna-, Rum. dormi; somn Du. zlapen; zlaap nidra- Ir. con-tulim (foaim); OHG | slafan; slaf Av. x’ap-; x*afna-
stian, cotlud MHG  slafen; slaf, swep NIr. _codlaim; codladh, NHG - schlafen; schlaf
suan W. cysgu, huno; hun,
cwsg Br. kousket, huni; kousk,
hun
Many of the words for ‘sleep’ belong to an inherited group reflecting an IE verbal root and an established substan- tive form for ‘sleep’. Others are cognate with words meaning ‘lie, rest, quiet, slack, blink’. Verb and noun are gener- ally parallel, but not in Greek or Latin, and both forms are listed. The verbal forms listed are those that mean ‘be asleep’, beside which there are distinc- tive types for ‘fall asleep’ and ‘put to sleep’. Several of the nouns are used also for ‘dream’ (4.62).
1. IE *swep-, sb. *swep-no-s, *swop- no-s, *sup-no-s. Walde-P. 2.523f. Er- nout-M. 954f. Falk-Torp 1109 f.
ON sofa, Dan. sove, Sw. sove, OF swe- fan; ChSI. sitipati, ete., general Slavic verbs; Skt. svap-, Av. x*ap-; beside forms for ‘put to sleep’, as Lat. sopire, ON svefja, OE swebban, OHG antsweb-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
jan, -swebban, MHG entsweben; or ‘fall asleep’, as ON sofna, ChSI. uszinati, ete.
Grk. tmvos; Lat. somnus (> It. sonno, Sp. suefio, Rum. somn, OFr. somme [now ‘nap’]; Fr. sommeil fr. dim. *som- niculus) ; Ir. stan, W., Br. hun (denom. vbs. W. huno, Br. huni, hun(i)a); ON svefn, Dan. sfun, Sw. sémn, OE swefn; (Lith. sapnas, Lett. sapnis, sapns dream’); ChSl. stinti, SCr. san, Pol. sen, Russ. son (all these also, and Boh. sen only, ‘dream’); Skt. svapna-, Av. x*afna- (also Iran. *x*Gpa-, NPers. x°Gp, cf. Beneveniste, BSL 30.75 ff.); Arm. k'un; Alb. gjum; Toch. A spdm, span-, sdpn-.
Lat. sopor, of different formation (*swepds, like amor, etc.), mostly poet. and esp. ‘overpowering sleep’, sometimes personified. ;
Chl. (late) stipanije, SCr. spavanjé, Boh. spant, spdnek, Pol. spanie, Russ.
‘ bs. ybl. nouns ‘sleeping’, fr. the v
; _ Walde-P. 1.358 f. - dormire (> Romance vps.) : Seg iinad ‘slumber, ee ; ; Skt, dra- ‘sleep’ Hom. aor. é5pafov 's ae Jate pres. bap04v., etc. Walde-P. 1.821. Ernout-M. 283 f. Walde-H. 1.372.
4, Olr. con-tulim, MIr. cotlaim, NIr. codlaim, vbl. n. OIr. cotlud, NI. codladh, also rarely uncompounded e.g. 3 sg. pret. toilis, etc. : ChSl. tolatz ‘pacify, quiet, still (nunger, thirst)’, Lith. tiltt ‘become quiet, silent’. Walde-P. 1.740f. Peder- sen 2.656 f.
Digitized by Arya Samaj Foundation Chennai and eGangotri
DY; BODILY FUNCTIONS AND CONDITIONS 269
Ir. foaim (‘sleep’ as ‘pass the night’), perh. : Skt. vas- ‘dwell’, etc. Pedersen 2.524.
W. cysgu, Br. kousket, Corn. cusce, fr. Lat. quiéscere, VLat. quéscere ‘rest, re- pose’. The sbs. W. cwsg, Br. kousk are back-formations. Loth, Mots lat. 155.
5. Goth. slépan, sléps, OE slépan, slép, OHG slafan, slaf, etc. (common to Goth. and WGmce.) : MLG, Du. slap, OHG slaf(f), NHG schlaff ‘slack, loose, lax’, ChSl. slab, Lith. slabnas ‘weak’, etc. Walde-P. 2.432. Falk-Torp 1056.
6. Lith. miegoti, miegas, miegojimas, Lett. mzeguot, miegs (Lith. migti, Lett. migt ‘go to sleep’): ChSl. mignati, mizati, Russ. migat’ ‘blink, twinkle’, etc. Walde-P. 2.246. Berneker 2.56 f.
7. Skt. svap-, Av. z*ap-, etc., above, 1.
Skt. drd-, sb. nidra- : Lat. dormire, above, 3.
4.62 DREAM (sb.)
Grk. — Svetpos, évbarvioy Goth. Lith. sapnas NG  bvetpo ON svefn, draumr Lett. sapnis, sapns Lat.  somnium, insomnium Dan. drém ChSl.  stinit It. sogno Sw. drém SCr. san Tr. __réve, songe OE swefn, meting Boh. sen §p. ensuefio, suefio ME __ sweven, drem(e), me- Pol. sen pi ne ting Russ. son aa aisling NE dream Skt.  svapna- - — briongloid, taidh- Du. —droom Av. hae W bhreadh, aisling OHG itroum py, euddwyd MHG troum * — hurtvre NHG itraum
Many of the nouns for ‘dream’ are the ne Ae or derived from, those for &p. Other sources are notions like
fe Sight, appear
ar i nate pearance, revelation’, or ‘de-
1. IE *swep. derivg, of it. tg
tk, bbmnov; Lat. somnium (> It 1 T. songe, Sp. suefio), later also
oe Sp. ensueno, etc.) mod- “ evbrviov; Br. hunvre (fr. iON svefn, OF swefn (also
8, etc. ‘sleep’ (4.61) or
‘sleep’), ME sweven; Lith. sapnas, Lett. sapnis, sapns; ChSl. stint, SCr. san, ete. (also ‘sleep’, except Boh. sen); Skt. svap- na- (also ‘sleep’); Toch. A. spdm (also ‘sleep’).
2. Grk. évepos and évap (mom.-acc. only), NG évepo: Arm. anurj, Alb. andéré ‘dream’, root connection? Walde-P. 1.180.
3. Fr. réve, beside vb. réver ‘dream’ also ‘be delirious, mad’, etym. much dis- puted. Derivation fr. VLat. *rabia,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
270 SELECTED INDO-EUROPEAN SYNONYMS
Lat. rabiés ‘madness’, with some, orig. local, differentiation from rage (so Diez 669; cf. also NED s.v. rave, vb.1) is semantically the most attractive, but is now generally rejected. REW 4210. Gamillscheg 762.
Rum. vis, fr. Lat. viswm ‘sight, ap- pearance, vision’. REW 9383.
4. Ir. atsling, etym. dub., perh. cpd. : sellaim ‘look’ (15.52). Stokes ap. Mac- bain 12.
NI. briongloid fr. Mir. brinngloid ‘a vision’ (K. Meyer, Contrib. 262) : MIr. brinda ‘vision’, NIr. brionn ‘fiction, dream’, but outside connection? Mac- bain 50.
NIv. taidhbhreadh, vbl. n. of vb. taidhbhrighim ‘dream’, cpd. of MI. brigaim ‘show, declare’ beside bricht ‘spell, charm, incantation’. A deriv. of
4.63 WAKE (a, trans., b, intr.)
this root *brig- is prob. also the final member of Br. huri-vre (above, 1) and the first of W. breu-ddwyd, older breid. dwyd, MW breidwyt (the final member obscure). Loth, RC 40.362 f.
5. ON svefn, OE swefn, above, 1.
ON draumr, Dan. drgm, Sw. drém, (OE dréam only ‘joy, music’), ME drem, dreme, NE dream, OS drém, Du. droom, OHG, MHG troum, NHG traum, prob, (as Gmc. *draugma-) : OS bidriogan, OHG triogan ‘deceive’, Skt. druh- ‘Seek to harm, injure’, Av. druz- ‘lie, deceive’, etc. Walde-P. 1.874. Falk-Torp 161,
OE meting, ME meting (e.g. Chaucer), with the more common vbs. OE m@ian, ME mete, etym.? NED s.v. mete, vb.2
6. Balto-Slavic and Skt. words, above, 1.
@@@ sword text
20.27 SWORD Grk.  Elos, paxatpa Goth. hairus, méki (acc. sg.) Lith. kalavijas, kardas NG orabl, Elpos (lit.) ON sverd, mekir, hjorr Lett. zuobens Lat.  gladius, énsis (poet.), Dan. svard ChSl. met, kor(ti)da spatha (late) We svdrd SCr. maé It. spada OE sweord, méce, heoru Boh. meé Fr. épée (glaive) ME _ swerd Pol. miecz Sp. espada NE sword Russ. meé Rum. sabie, spadé Du. zwaard Skt. _asi-, khadga- Ir. claideb, colg OHG - swert Av. karata- Nir. clatdheamh MHG ss swert W. cleddyf NHG | schwert
Br. kleze
Some of the words for ‘sword’ are con- nected with verbs for ‘cut, strike’ or the like, and in one group the basic charac- teristic is the flat blade. But many are of obscure root connection, and loan- words are frequent.
1. Grk. £idos, prob. a loanword fr. the same source as Egypt. sft ‘knife, sword’. Boisacq 679 with references. Myres, Who were the Greeks? 590.
Grk. dep (poet., freq. in Hom.), the sword as hung on the belt : delpw ‘raise’, pass. ‘be suspended’. Solmsen, Unter- suchungen 292.
Grk. paxapa ‘knife’ (9.23), also used for a kind of sword, ‘dagger’, and ‘saber’, in NT reg. word for ‘sword’.
NG onafi (the reg. pop. word; tidos lit., but official term in the army), fr. Grk. oraflov, dim. of o7aOn ‘flat wooden blade, spattle, blade’ (of an oar or sword, etc.) : OF spadu ‘spade’, ete. Walde-P.. 2.653.
2. Lat. gladius (> Olt. ghiado; Fr.
glaive, now arch., by blend with a Gallie
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
form; REW 3778), early loanword fr. Celtic (Ir. claideb, etc., below, 3). Er- nout-M. 423. Walde-H. 1.603 f.
Lat. énsis (old word, but only poet., in prose replaced by gladius) : Skt. asi- ‘sword’, root connection? Ernout-M. 302. Walde-H. 1.406.
Lat. spatha ‘spattle’, also ‘sword’ of the auxiliaries (Tac.), later reg. word for ‘sword’, displacing gladius, loanword fr. Grk. o746y (above, 1). Hence It. spada (> Rum. spadé), Fr. épée, Sp. espada. Couissin, op. cit. 489. REW 8128.
Rum. sabie, fr. the Slavic, cf. Bulg. sab(t)ja, SCr. sablja, Pol. szabla, etc. ‘saber’ (whence also NHG sabel, sdbel, It. sciabla, Fr. sabre > NE sabre), prob. orig. fr. Hung. szdblya (: szab ‘cut’). Tiktin 1350. Kluge-G. 493.
3. Ir. claideb, NIr., Gael. claidheamh (hence with mor ‘great’, NE claymore), W. cleddyf, Br. kleze, Corn. clethe, be- side Lat. gladius (fr. Celtic) : Ir. claidim, W. claddu ‘dig’, Lat. clddés ‘damage, in- jury’, Skt. khadga- ‘sword’, Lith. kalti
‘strike’, Grk. x\aw ‘break’, etc. Walde- Pp. 1.439. Walde-H. 1.603 f. (with refs. for Celtic).
Ir. colg (less common than claideb and denoting some special type of sword, Bauersfeld, op. cit. 339 ff.; also ‘beard on grain, prickle’) : W. cola ‘beard (on grain)’, col ‘sting’, cala, Br. kale’h ‘penis’ perh. fr. a root *kel- ‘prick, stick’ (or ultimately identical with *hel- ‘strike’ in above group?). Walde-P. 1.435.
4, Goth. hairus, ON hjgrr, OE heoru, OS heru, prob. fr. IE *(s)ker- in Grk. xelpw ‘shear’, OF sceran ‘cut, shear’, etc. (9.22). Walde-P. 2.576. Feist 235.
Goth. méki (acc. sg.), ON mekir, OE méce (loanword fr. ON?), OS maki, Crim.Goth. mycha ‘ensis’, orig. dub., perh. a loanword, but source unknown (cf. ChSl. mect, below, 6). Feist 352 f.
ON sverd, OF sweord,- etc., general Gmce. (except Goth.), etym. dub., perh. : OHG sweran ‘cause or suffer pain’, swero, swer(a)do ‘pain’, Ir. serb ‘bitter’, Av. x’ara- ‘wound’ (Walde-P. 2.529), with orig. sense of root ‘sting, cut’(?). W. Krogmann, KZ 59.204. Kluge-G. 552. Otherwise Falk-Torp 1214 (cf. also 1560).
ON brandr, OE brand, OHG brant ‘burning, brand’ were used (mostly poet.) for the ‘blade of a sword’ and ‘sword’. Hence as ‘sword’ It. brando,
Digitized by Arya Samaj Foundation Chennai and eGangotri
WARFARE
1393
OFr. brant. REW 1273.
5. Lith. kalawjas : OPruss. kalabian id., Lat. clava ‘club’, fr. the root in Lith. kalti ‘strike’, etc. (cf. Ir. claideb, above 3). Trautmann, Altpreuss. 351. (Walde- P. 1.437).
Lith. kardas (cf. NSB; formerly the usual word), fr. Pol. kord, cf. ChSl. kor(%)da (below, 6).
```


## [2026-09-14T03:17:32.495Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"leaves\",len(pages))\nimport re\nfor n,p in enumerate(pages):\n    if 'sŭep-' in p or 'suep-' in p or \"x'ara\" in p or 'x^ara' in p or 'Geschwür' in p:\n        head=p[:80].replace('\\n',' ')\n        print(n,head)\nEOF"
}
```


### [2026-09-14T03:17:33.759Z] TOOL RESULT

```
leaves 725
474 470                                                  sen-         ai. stin'd-h; 
528          ;                                                                      
533                                           Mier-     snerbh-                     
537                                                     sijelio(n)-     — suesor-
```


## [2026-09-14T03:17:36.567Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (527,528,529,530,532,533,534):\n    p=pages[n]\n    print(\"=== leaf\",n,\"|\",p[:100].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T03:17:37.668Z] TOOL RESULT

```
=== leaf 527 |                                                                8uep“, sup-                          
=== leaf 528 |          ;                                                                                          
=== leaf 529 |                                    suenq-, sunq-   — suento-, sunto                              525
=== leaf 530 | 526                   STiendh-   —   sneng-, suenq-   :   siieg-,       sueq-   :   seuq-   nennen, 
=== leaf 532 |                                                                                  ;     528          
=== leaf 533 |                                           Mier-     snerbh-                                  529  ue
=== leaf 534 | abwischen^, mhd. swerben „umlierwirbelii“ (ahd. mhd. swarp, -bes m. „gur- ges‘', ahd. swirbil m. „Wi
```


## [2026-09-14T03:17:40.688Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[527][:2200])\nprint(\"@@@@ leaf 533 (p.529)\")\nprint(pages[533][:2500])\nEOF"
}
```


### [2026-09-14T03:17:41.798Z] TOOL RESULT

```
                                                               8uep“, sup-                                                 523

Pedersen KZ. 36, 284 im Auslaut nicht mit ai. sasii-, av. xsvasti^s „60                                                     =
Sechsheit von Zehnem‘‘ gleichgesetzt, sondem wie die 7—9 als Nach-
ahmung von djeie         betrachtet) lat. sex\ air. se, 6. seser „6 Mann“,
                                                                      ;



mor-feser „magnus seviratus, 7 Mann“, cymr. usw. chivech „6‘‘; got. saihs^
anord. sex,                   ahd*
                  seJiS) lit. flektiert     aksl, sesth h (= ai.        Ygl.
lat.            sodaqa 16 ;     xsvaMasa^- „der 16.“). Ordinale: ai. sa^hd-,
                              ai.                      ,


av. xstva- (Erklarungsversuche bei Kleinhans IP. 3, 304, Bartholomae Grdr.
d. iran. Phil. I 113;                      arm. vecerord;                 gr. exrog]       alb. i-gasfets^ i-gaste;        lat.

                                umbr. sestentasiaru „sextantariarum^‘; idg.
sextus, seshts (Sestius o. ZeQTieg,
wohl *s{u)ehtos, im Lat. und Germ, mit Eindringen des 5 aus der Grund-
zahl);            cymr. chweched\ got. saihsta, ahd. seJisto, sehto, anord.
              air. sessed,
sette    auch Sverdrup IF. 35, 155 f.); lit. sUtas, apr. m, Tiefstufe tischts
            (s.

(aus einer ebenso vokalisierten apr. Form der Grundzahl stammt sicher
alit.   usios         „Wochenbett“ gegeniiber echt lit. Msios ds., Lit. bei Trautmann
Apr. 454):                aksl. sesfh,

     Altere Lit. bei Curtius 384,


1 . Suep-, sup- „schlafen“, suepno-s^                                      suopno~s (bait. kelt. "^^sopnos durch
        Diss.         gegen -op-? anders Bgm. I^ 340), supno-s „Schlaf‘.
     Ai. svdpiti^ svdpati „schlaft, schlaft ein“, Pass, siipyate^ Ptc. siiptd-h „ein-
geschlafen“,                   Kaus. svapdyati „schlafert ein“                         (== aisl. sefa)^     smpayati       ds.
(— aisl. svefja usw.); av. x^ap- „schlafen“ (Formen s. bei Bthl. Wb. 1862f.);
     lat.    sopio^ -Ire „einschlafern“                        (s.   zur Bildung Yf. LEWb.^ s. v.,              
@@@@ leaf 533 (p.529)
                                          Mier-     snerbh-                                  529

uer- „Schnur“,  sowie von sg/ua „Klippe, Hiiger' und eg/na „Ohrgehang'*),
horn, igjuiva Acc., ig/Luoi Dat. PI. „Bettpfosten, Bettfu6“ (aber igjurjvevco
„auslegen'' nicht eigeBtlich „feststellen“) auch "Egjurjg EQ/Lid(j:)cov als den
                                                      ;


als Pfahl verehrten zu deuten, ware nur erlaubt, wenn der Name echt
griech. ware (doch kleinasiatisch nach Kalinkas Mitteilung).


4, suer- „schwaren, eitern“.
   Av. x^ara- m. Wunde, Yerwundung^'; ahd. swera7i sfc. Y. „schmerzen,
eitern^  schwaren, schwellen^^, sivero „leiblicher Schmerz, bes. Geschwiir,
Geschwulst'', nhd. Schtvdre, Geschiviir^ ahd. swer{a)do „leiblicher Schmerz“,
ags. stveornian .,gerinnen“; Pick I ^ 153, 111^ 549 (unannehmbar iiber die
germ. Gruppe Schroeder Abl. 88 f.).
   Ahd. ivarah „Eiter'‘ (Pick III ^ 396) wohl nicht Z;-Erw. einer Wzf. ohne
anl. S-. Ir. serh^ cymr. chiverw „bitter'' (Pick II* 324; s. die Gruppe u. kser-
„trocken“) liegt in der Bed. ab (man miifite denn auf „brennend, stechend,
sowohl vom Geschmack, als von Wunden“ als Gdbed. raten s. auch u. sutvs   ;


„sauer“).


suergh- „sorgeiJ,         sich   worum kiimmerm'; serg(h?)- „krank sein‘\
   1.   Ai. surJcsati „kiimmert          sich   um etwas‘'; got. sailrga „Sorge, Betriib-
nis“,     aisl.   ags. sorg^   as.   sorga^   ahd, sorga^     afrank. sworga   jjSorge^'^;   got.
saiirgan^ aisl. stjrgja^ as. sorgdn, ags. sorgian, ahd. sorgen, sworgen „sorgen‘\
   2.     Air. serg ,jKrankheit‘‘, lit. sergii, sirgti „krank sein“, aksl. sraga „Krank-
heit'^, sragz „austerus, torvus“: die Zugehorigkeit von arm. crh „Muhe“.
erkn „Geburtsschmerzen'‘, erhinm „fiirchte'‘, die den Guttural der zweiten
Gruppe als idg. g bestimmen wiirden (Pedersen KG. I 71, gegen eine
friihere, unter perg- „Purcht‘' erwahnte Deutung) leuchtet der Bed. wegen
nicht recht ein.    ^Yohl aber wiirde alb. dergem „bin bettlagrig*' sich in
der Bed. fiigen, nur setzte es Anlaut         voraus, Gdf. ^stwrg(h)io. Yiel-
leicht sind daher, zumal auch aksl. sragz nicht auf kdrperliches Ubel-
befinden geht, beide Gruppen in der AYeise zu vereinigen, daB im Anlaut
su- und 5- abwechselten und der gemeinsame Bed. -Kern „korperliche oder
seelische Gedi’iicktheit, miirrisches Wesen, auch infolge von Krankheit“ war.
   Ygl. Pick I* 562, II* 301, Zup. 9, 179 (BB. 25, 104 verkniipft er freilich
ir. serg vielmehr mit ahd. seraiven „vertrockne
```


## [2026-09-14T03:17:55.590Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('e2d1d2161fde0e0b.txt',encoding='utf-8').read()\nprint(t[:60])\ni=t.find('hypnotism')\nprint(t[i:i+2500])\nEOF"
}
```


### [2026-09-14T03:17:56.629Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/hypnotism
FETCHED: 2026
hypnotism
FETCHED: 2026-09-14T03:14:44Z
STATUS: 200
TITLE: Hypnotism - Etymology, Origin & Meaning

Hypnotism - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of hypnotism 

 hypnotism (n.) 

 1843, short for neuro-hypnotism (1842), coined by Dr. James Braid of Manchester, England, from hypnotic + -ism . In the same work (1843) Braid coined the verb hypnotize .
 also from 1843 

 Entries linking to hypnotism 

 hypnotic (adj.) 

 1620s, of drugs, "inducing sleep," from French hypnotique (16c.) "inclined to sleep, soporific," from Late Latin hypnoticus , from Greek hypnotikos "inclined to sleep, putting to sleep, sleepy," from hypnoun "put to sleep," from hypnos "sleep" (from PIE root *swep- "to sleep"). Modern sense of "pertaining to an induced trance" first recorded in English 1843, along with hypnotize , hypnotism , hypnotist , in the works of hypnotism pioneer Dr. James Braid. Related: Hypnotical ; hypnotically .

 hypnotize (v.) 

 1843 (Braid); see hypnotic + -ize . Related: Hypnotized ; hypnotizing .

 hypnosis 
 -ism 
 *swep- 
 See All Related Words (5) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 mesmerism 

 "the doctrine that one person can exercise influence over the will and nervous system of another and produce certain phenomena by virtue of a supposed emanation called animal magnetism," 1798, from French mesmérisme, named for Franz Anton Mesmer (1734-1815), Austrian physician wh

 suggestion 

 mid-14c., suggestioun, "action of prompting or urging," originally especially "a prompting to evil," from Anglo-French and Old French suggestioun "hint; temptation," from Latin suggestionem (nominative suggestio) "an addition, intimation, suggestion," noun of action from suggestu

 influence 

 late 14c., an astrological term, "streaming ethereal power from the stars when in certain positions, acting upon character or destiny of men," from Old French influence "emanation from the stars that acts upon one's character and destiny" (13c.), also "a flow of water, a flowing 

 disorder 

 late 15c. (Caxton), "destroy or derange the order of, throw into confusion," from dis- "not" (see dis-) + order (v.). Replaced earlier disordeine (mid-14c.), from Old French desordainer, from Medieval Lat
```


## [2026-09-14T03:17:57.950Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://abadis.ir/fatofa/%D9%87%DB%8C%D9%BE%D9%86%D9%88%D8%AA%DB%8C%D8%B2%D9%85/\" \"https://fr.wiktionary.org/wiki/hypnotisme\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 492: Persian هیپنوتیزم / French hypnotisme\"; done"
}
```


### [2026-09-14T03:18:00.918Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9af9e591ae48a9fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b7897e09babf3ecd.txt
```


## [2026-09-14T03:18:05.469Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('b7897e09babf3ecd.txt',encoding='utf-8').read()\ni=t.find('Étymologie')\nprint(t[i:i+900] if i>0 else t[:1500])\nprint(\"#### abadis\")\nt2=open('9af9e591ae48a9fc.txt',encoding='utf-8').read()\nprint(len(t2))\nfor k in ['عمید','معین','دهخدا','هیپنوتیزم','فرانسه']:\n    j=t2.find(k)\n    print(\"--\",k,j, t2[max(0,j-200):j+400] if j>0 else '')\nEOF"
}
```


### [2026-09-14T03:18:06.525Z] TOOL RESULT

```
Étymologie 

 1.2 
 Nom commun 

 1.2.1 
 Traductions 

 1.3 
 Prononciation 

 1.4 
 Références 

 Basculer la table des matières 

 hypnotisme 

 10 langues 

 Ελληνικά 
 English 
 Magyar 
 Ido 
 日本語 
 Malagasy 
 Nederlands 
 Русский 
 Kiswahili 
 Tiếng Việt 

 Article 

 Discussion 

 français 

 Lire 

 Modifier le wikicode 

 Voir l’historique 

 Outils 

 Outils

 déplacer vers la barre latérale 
 masquer 

 Actions

 Lire 

 Modifier le wikicode 

 Voir l’historique 

 Général

 Pages liées 
 Suivi des pages liées 
 Téléverser un fichier 
 Lien permanent 
 Informations sur la page 
 Citer cette page 
 Obtenir l’URL raccourcie 
 Utiliser l’ancien analyseur 

 Imprimer / exporter

 Créer un livre 
 Télécharger comme PDF 
 Version imprimable 

 Dans d’autres projets

 Apparence

 déplacer vers la barre latérale 
 masquer 

 Définition, traduction, prononciation, anagramme et synonyme
#### abadis
4675
-- عمید 482 نی انگلیسی : hypnosis , hypnotism , animal magnetism 

 دنبال کنید 

 فرهنگ معین

 (نُ تِ ) [ فر. ] (اِ. ) خواب مصنوعی ، خواب مغناطیسی که در آن شخص تحت تأثیر القاهای شخص دیگر به خواب می رود. 

 فرهنگ عمید

 عملی که طی آن کسی را به خواب مصنوعی فرو می برند و تحت تاثیر القاهای ویژه، از او می خواهند تا به پرسش ها و خواست های خواب کننده پاسخ دهد. 

 دانشنامه عمومی

 هیپنوتیزم یا خوابگری[ ۱] [ ۲] شاخه ای از علم روان شناسی است که در آن به وسیلهٔ تلقین، شخص در حالت خاصی از هوشیاری قرار می گیرد. هیپنوتیزم یا به طور دقیقتر موجب تسلط دیگری بر فرد نمی شود بلکه دیگری با ضمیر ناخودآگاه آدمی به مکالمه و القا
-- معین 358 شنری آبادیس

هیپنوتیزم - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 هیپنوتیزم
 /hipnotizm/

 برابر پارسی : خواب گری
 معنی انگلیسی : hypnosis , hypnotism , animal magnetism 

 دنبال کنید 

 فرهنگ معین

 (نُ تِ ) [ فر. ] (اِ. ) خواب مصنوعی ، خواب مغناطیسی که در آن شخص تحت تأثیر القاهای شخص دیگر به خواب می رود. 

 فرهنگ عمید

 عملی که طی آن کسی را به خواب مصنوعی فرو می برند و تحت تاثیر القاهای ویژه، از او می خواهند تا به پرسش ها و خواست های خواب کننده پاسخ دهد. 

 دانشنامه عمومی

 هیپنوتیزم یا خوابگری[ ۱] [ ۲] شاخه ای از علم روان شناسی است که در آن به وسیلهٔ تلقین، شخص در حالت خاصی از هوشیار
-- دهخدا 4179  دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 

 لینک ها 

 حقوق این سامانه وابسته به دیکشنری آباد
-- هیپنوتیزم 135 URL: https://abadis.ir/fatofa/%D9%87%DB%8C%D9%BE%D9%86%D9%88%D8%AA%DB%8C%D8%B2%D9%85/
FETCHED: 2026-09-14T03:18:00Z
STATUS: 200
TITLE: هیپنوتیزم - معنی در دیکشنری آبادیس

هیپنوتیزم - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 هیپنوتیزم
 /hipnotizm/

 برابر پارسی : خواب گری
 معنی انگلیسی : hypnosis , hypnotism , animal magnetism 

 دنبال کنید 

 فرهنگ معین

 (نُ تِ ) [ فر. ] (اِ. ) خواب مصنوعی ، خواب مغناطیسی که در آن شخص تحت تأثیر القاهای شخص دیگر به خواب می رود. 

 فرهنگ عمید

 عملی که طی آن کسی را به خواب مصنوعی فرو می برن
-- فرانسه -1
```


## [2026-09-14T03:18:16.395Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('b7897e09babf3ecd.txt',encoding='utf-8').read()\ni=t.find('Basculer la table des mati')\nprint(t[i:i+1600])\nEOF"
}
```


### [2026-09-14T03:18:17.444Z] TOOL RESULT

```
Basculer la table des matières 

 hypnotisme 

 10 langues 

 Ελληνικά 
 English 
 Magyar 
 Ido 
 日本語 
 Malagasy 
 Nederlands 
 Русский 
 Kiswahili 
 Tiếng Việt 

 Article 

 Discussion 

 français 

 Lire 

 Modifier le wikicode 

 Voir l’historique 

 Outils 

 Outils

 déplacer vers la barre latérale 
 masquer 

 Actions

 Lire 

 Modifier le wikicode 

 Voir l’historique 

 Général

 Pages liées 
 Suivi des pages liées 
 Téléverser un fichier 
 Lien permanent 
 Informations sur la page 
 Citer cette page 
 Obtenir l’URL raccourcie 
 Utiliser l’ancien analyseur 

 Imprimer / exporter

 Créer un livre 
 Télécharger comme PDF 
 Version imprimable 

 Dans d’autres projets

 Apparence

 déplacer vers la barre latérale 
 masquer 

 Définition, traduction, prononciation, anagramme et synonyme sur le dictionnaire libre Wiktionnaire.

 Français 
 [ modifier le wikicode ] 

 Étymologie 
 [ modifier le wikicode ] 

 ( 1845 ) De hypnotique par substitution de suffixe avec -isme . 

 Nom commun 
 [ modifier le wikicode ] 

 Singulier Pluriel 

 hypnotisme 
 hypnotismes 

 \ip.nɔ.tism\ 

 hypnotisme \ip.nɔ.tism\ masculin 

 ( Médecine ) Ensemble des phénomènes classés sous le nom d’ hypnose .
 Étudier l’ hypnotisme . 

 ( En particulier ) État hypnotique.
 C’est de l’ hypnotisme . 

 Provocation des faits d’hypnose par divers procédés .
 Michel à Londres avait assisté avec passion à de nombreuses séances d’ hypnotisme . Un soir où le fameux Pittman s’exhibait sur la scène d’un grand music-hall, le magnétiseur, selon l’usage, fit appel à des spectateurs de bonne volonté. —   ( Marguer
```


## [2026-09-14T03:18:23.237Z] TOOL CALL #86: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg492.png"
}
```


### [2026-09-14T03:18:23.801Z] TOOL RESULT

```

```


## [2026-09-14T03:18:23.775Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:19:18.209Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[204]\nfor w in ['خسپیدن','خفتن','خسبیدن']:\n    i=p.find(w)\n    print(\"--\",w,i)\n    if i>0: print(p[max(0,i-350):i+250])\nEOF"
}
```


### [2026-09-14T03:19:19.284Z] TOOL RESULT

```
-- خسپیدن 4192
 -‬نا الاطاء ‪. ۴‬‬

                                             ‫* خصاییدی ‪ -‬بفتح اول وششم » رك ‪ :‬خسانیدن ‪.‬‬
        ‫‪14(Î-S-faVX‬‏‬                ‫لنو«ی‬
                                        ‫هسی‬
                                          ‫ب خف‬‫=‬     ‫جحم‬‫ن فت‬
                                                          ‫یو‬‫* خیدنر خسپیدن _ م اول‬
         ‫‪:‬ص‬       ‫لوستا ‏‪ » 62۷1 - 5 - 34a‬در لهجةٌ ءپودبان ابران ‪( 01-2-0۳50‬خید) «اسفا ‪٩‬‏‬
 ‫‪ ۰» ۰‬استی ‪nissu‬‏ ‪ . 22‬است ‪ ۰۸۱‬در اراك (سلطان آباد) ‪ 820101505‬و دبروجرد غالبا‬
                                          
-- خفتن 4481
                                                ‫یو‬‫* خیدنر خسپیدن _ م اول‬
         ‫‪:‬ص‬       ‫لوستا ‏‪ » 62۷1 - 5 - 34a‬در لهجةٌ ءپودبان ابران ‪( 01-2-0۳50‬خید) «اسفا ‪٩‬‏‬
 ‫‪ ۰» ۰‬استی ‪nissu‬‏ ‪ . 22‬است ‪ ۰۸۱‬در اراك (سلطان آباد) ‪ 820101505‬و دبروجرد غالبا‬
                                                          ‫مبهمن معنی(مکی تژاد)؛ خفتن‪ ,‬خوابیدن ‪:‬‬          ‫‪00‬‬
        ‫«لتان‪.»۱۱‬‬
                ‫ک‬                    ‫کرسنه خبد ملك لیمروز‪: .‬‬                  ‫ور بخرآأمی‌فتد ازمملکت‬

-- خسبیدن -1
```


## [2026-09-14T03:19:27.978Z] TOOL CALL #88: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:746 --image 2>&1 | tail -30"
}
```


### [2026-09-14T03:19:29.175Z] TOOL RESULT

```
no scan of BQT covers printed page 746 (see 'scans' in refs_online.json)
```


## [2026-09-14T03:19:34.876Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[204]\nprint(p[3900:5200])\nEOF"
}
```


### [2026-09-14T03:19:35.912Z] TOOL RESULT

```
        ‫* خصاییدی ‪ -‬بفتح اول وششم » رك ‪ :‬خسانیدن ‪.‬‬
        ‫‪14(Î-S-faVX‬‏‬                ‫لنو«ی‬
                                        ‫هسی‬
                                          ‫ب خف‬‫=‬     ‫جحم‬‫ن فت‬
                                                          ‫یو‬‫* خیدنر خسپیدن _ م اول‬
         ‫‪:‬ص‬       ‫لوستا ‏‪ » 62۷1 - 5 - 34a‬در لهجةٌ ءپودبان ابران ‪( 01-2-0۳50‬خید) «اسفا ‪٩‬‏‬
 ‫‪ ۰» ۰‬استی ‪nissu‬‏ ‪ . 22‬است ‪ ۰۸۱‬در اراك (سلطان آباد) ‪ 820101505‬و دبروجرد غالبا‬
                                                          ‫مبهمن معنی(مکی تژاد)؛ خفتن‪ ,‬خوابیدن ‪:‬‬          ‫‪00‬‬
        ‫«لتان‪.»۱۱‬‬
                ‫ک‬                    ‫کرسنه خبد ملك لیمروز‪: .‬‬                  ‫ور بخرآأمی‌فتد ازمملکت‬
```


## [2026-09-14T03:19:48.337Z] TOOL CALL #90: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T03:19:48.381Z] TOOL RESULT

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
```


## [2026-09-14T03:19:50.798Z] TOOL CALL #91: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T03:19:50.843Z] TOOL RESULT

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


## [2026-09-14T03:28:21.690Z] TOOL CALL #92: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-492.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_SWEP  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swep-\"\nW_XAB   = \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%A8\"\nW_XOFTAN= \"https://en.wiktionary.org/wiki/%D8%AE%D9%81%D8%AA%D9%86\"\nW_HUPNOS= \"https://en.wiktionary.org/wiki/%E1%BD%95%CF%80%CE%BD%CE%BF%CF%82\"\nW_SWORD = \"https://en.wiktionary.org/wiki/sword\"\nW_SWERDA= \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/swerd%C4%85\"\nW_XALID = \"https://en.wiktionary.org/wiki/%D8%AE%D9%84%DB%8C%D8%AF%D9%86\"\nW_XORE  = \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D9%87\"\nW_XALBAN= \"https://en.wiktionary.org/wiki/%D8%AE%D9%84%D8%A8%D8%A7%D9%86\"\nW_BAXTAK= \"https://en.wiktionary.org/wiki/%D8%A8%D8%AE%D8%AA%DA%A9\"\nE_HYPNO = \"https://www.etymonline.com/word/hypnotism\"\nFR_HYP  = \"https://fr.wiktionary.org/wiki/hypnotisme\"\nAB_HYP  = \"https://abadis.ir/fatofa/%D9%87%DB%8C%D9%BE%D9%86%D9%88%D8%AA%DB%8C%D8%B2%D9%85/\"\n\ndoc = {\n \"pdf_page\": 492,\n \"book_page\": 462,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------- ENTRY 0 -----------------------------------------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Swep, Sup 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *swep- 'to sleep' (Pokorny 1048-1049 su̯ep-1, sup-; Watkins/AHD swep-1), with the noun *swep-no-/*swop-no-/*sup-no- 'sleep, dream'\",\n \"note\": \"Nourai's headword reproduces Watkins's AHD entry 'swep-1. To sleep' exactly, and his page reference is Pokorny's own: IEW 1048-1049 prints '1. su̯ep-, sup- „schlafen“, su̯epno-s, su̯opno-s ... supno-s „Schlaf“'. Root, language label ('Indo-European' = PIE) and gloss are all correct, and the '1' in 'Swep, Sup 1' matches Pokorny's/Watkins's numbering (su̯ep-2 'to throw, sling' is a different root). The zero grade *sup- of the second headword is the grade that yields Greek hupnos < *sup-no-s. The only thing worth flagging on the chart is the Avestan box, which mixes true Avestan forms with a Proto-Iranian variant *hufsa- taken over from Gharib.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *swep- «خفتن، خوابیدن» است؛ پوکورنی در فرهنگ ریشه‌شناختی خود (ص ۱۰۴۸ تا ۱۰۴۹) آن را «su̯ep-, sup- ‹schlafen›» آورده و نام‌واژهٔ آن را *su̯ep-no-/*su̯op-no-/*sup-no- «خواب، رؤیا» بازسازی کرده است؛ واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ AHD نیز همین را با شمارهٔ swep-1 ثبت کرده است. صورت کاهیده (تهی‌درجهٔ) *sup- همان است که hupnos یونانی از *sup-no-s از آن برآمده و «خواب» ایرانی نیز از همین ریشه است. پس نام ریشه، برچسب زبانی و معنای آن، هر سه درست است و ادعای نورایی در این بخش پذیرفتنی است؛ تنها در جعبهٔ اوستایی صورت *hufsa- که ایرانی آغازین است در کنار صورت‌های اوستایی نشسته است.\",\n \"sources\": [W_SWEP],\n \"ref_check\": [\n   {\"ref\": \"POK:1048\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW pp. 1048-1049 (local POK_full.txt line 84037 'Root / lemma: suep-1, sup-', Meaning 'to sleep', Page(s) 1048-1049; German text in WLD_Bd2_pages.txt leaf 527 = p.523 'su̯ep-, sup- „schlafen“'): 'Avestan x'ap- ‘sleep’ ... Old Indic svapiti, svapati ... gr. hypnos ‘sleep’ ... Latin somnus'. Exactly Nourai's root, gloss and page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. swep-1 (AHD_watkins1985.txt line 1050)\", \"stance\": \"supports\",\n    \"note\": \"'swep-1. To sleep. 1. Suffixed form *swep-os- in Latin sopor ... 3. Suffixed zero-grade form *sup-no- in Greek hupnos, sleep: HYPNO-, HYPNOS, (HYPNOSIS), HYPNOTIC. [Pok. 1. swep- 1048.]' — the chart's headword 'Swep, Sup 1' is copied from here.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 523 (WLD_Bd2_pages.txt leaf 527)\", \"stance\": \"supports\",\n    \"note\": \"'1. su̯ep-, sup- „schlafen“, su̯epno-s, su̯opno-s ... supno-s „Schlaf“. Ai. svapiti, svapati ...; av. x'ap- „schlafen“ (Formen s. bei Bthl. Wb. 1862f.); lat. sopio, -ire „einschlafern“'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, cols. 1347-1348 (IEC.txt leaf 741-742)\", \"stance\": \"supports\",\n    \"note\": \"'suepnos, om ‘sleep, dream’ ... Skt. svapnah; Av. xwafno ...; Per. xwab, as Skt.; Lat. somnus' and 'suepo, io (1) ‘be drowsy, sleep’ ... Av. xwap-, v. id.; Per. xuftan, inf. beside xabam, xabidan'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.61 SLEEP (SYN.txt line 6908)\", \"stance\": \"supports\",\n    \"note\": \"'1. IE *swep-, sb. *swep-no-s, *swop-no-s, *sup-no-s. Walde-P. 2.523f. ... Skt. svap-, Av. xʷap- ... Grk. hupnos; Lat. somnus ... Skt. svapna-, Av. xʷafna- (also Iran. *xʷāpa-, NPers. xʷāp, cf. Benveniste, BSL 30.75 ff.)'.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"xwap, xvap, xwaf; xvafna, xwafsa; hufsa\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Avestan xᵛap- (weak stem xᵛaf-) 'to sleep' continues PIE *swep- with the regular Iranian treatment of initial *sw- > xᵛ- and of *p > f before a consonant; Bartholomae treats it in col. 1862 (cited as such by Nyberg and by Walde-Pokorny). The forms behind Nourai's three spellings 'xwap, xvap, xwaf' are one and the same verb (Y.Av. xᵛap-/xᵛaf-, ppp. xᵛapta-, perf. hušxᵛafa Y 57.17). 'xvafna' is the noun xᵛafna- n. 'sleep, dream' (< *swep-no-, = Skt. svapna-, Gk. hupnos, Lat. somnus); its negated adjective a-xᵛafna- 'sleepless' (V 19.20, Yt 10.7) is well attested. 'xwafsa' is not a noun but the inchoative present stem xᵛafsa- (impv. 2sg. xᵛafsa V 18.16, 2pl. xᵛafsata H 2.42) from *hwaf-sa- < *sup-sḱé-ti, so the gloss 'sleep' should read 'falls asleep'. 'hufsa' is not an attested Avestan form at all: it is Gharib's citation of the Proto-Iranian doublet *hufsa- (with *hw- > h- before u), which survives in Khotanese (h)us-, Yaghnobi ūfs- and in the Sogdian verb of node #3; Wiktionary reconstructs the pair as Proto-Iranian *hufsati / *xʷafsati. So the node is right in substance, loose in labelling.\",\n \"derivation_fa\": \"فعل اوستایی xᵛap- (ستاک ضعیف xᵛaf-) «خفتن» بازماندهٔ *swep- هندواروپایی آغازین است؛ *sw- آغازین در ایرانی به xᵛ- بدل شده و *p پیش از همخوان به f. سه املای «xwap، xvap، xwaf» در نمودار در واقع یک فعل‌اند (بارتولومه در ستون ۱۸۶۲ آن را آورده و نیبرگ و والده‑پوکورنی به همان‌جا ارجاع می‌دهند). «xvafna» نام‌واژهٔ xᵛafna- «خواب، رؤیا» است از *swep-no-، هم‌ریشه با svapna- سنسکریت و hupnos یونانی و somnus لاتین؛ صفت منفی آن a-xᵛafna- «بی‌خواب» در وندیداد ۱۹٫۲۰ و یشت ۱۰٫۷ گواهی شده است. اما «xwafsa» نام نیست، بلکه ستاک مضارع آغازی xᵛafsa- است (وجه امر xᵛafsa، xᵛafsata) از *hwaf-sa-، و معنای آن «به خواب می‌رود» است نه «خواب». «hufsa» نیز صورتی اوستایی نیست؛ قریب آن را به‌عنوان گونهٔ ایرانی آغازین *hufsa- آورده که در ختنی (h)us- و یغنابی ūfs- و در فعل سغدی گرهٔ ۳ بازمانده است. پس هستهٔ ادعای نورایی درست است، ولی برچسب‌گذاری صورت‌ها دقیق نیست.\",\n \"sources\": [W_SWEP, W_XOFTAN],\n \"ref_check\": [\n   {\"ref\": \"POK:1048\", \"status\": \"supports\",\n    \"note\": \"IEW 1048: 'Avestan x'ap- ‘sleep’ ... Old Indic svapna- ‘sleep, dream’, Avestan x'afna- m. ds.' (POK_full.txt lines 84043-84070); Walde-Pokorny II 523 adds 'av. x'ap- „schlafen“ (Formen s. bei Bthl. Wb. 1862f.)'.\"},\n   {\"ref\": \"HRN:107\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss p.107 no. 483 (HRN.txt leaf 128): 'xuspiden „schlafen“ ... aw. √xʷap-, xʷapta-, √xʷafs-, xʷafsata ‘schlafen’; phlv. xʷaftan, xʷaftak, xʷafsitan bezw. xuftan; ai. √svap, svapiti.' Every Avestan form of Nourai's box except 'hufsa' stands here.\"},\n   {\"ref\": \"FFD:50\", \"status\": \"supports\",\n    \"note\": \"Abolghasemi, Fe'lha-ye Farsi-ye Dari p.50 (PDF 55, read from the scan and saved to refs/ocr/FFD/50.vision.txt): 'خفت ← فارسی میانه xuft ← ایرانی باستان *xwaf-ta ... xwap صورت اصلی xwaf است، p پیش از t به f بدل شده است'; p.51 adds '*xwafsa ... ساخته شده است از xwap'. Supports xwap/xwaf and xwafsa.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae col. 1862 (xʷap-); a-xʷafna- in BRT.txt lines 6967, 7204\", \"stance\": \"supports\",\n    \"note\": \"The local OCR of Bartholomae breaks off around col. 1853, so the xʷap- article itself could not be read; but the cross-entries are there: '• j. a-xʷafna- Adj. „schlaflos“: V.19.20; Yt.10.7' and (leaf 899) 'kə hvapō xʷafnəmca dāt ... „wer schuf wohlwirkend Schlaf und Wachen“ Y.44.5'. Nyberg and Walde-Pokorny both cite Bthl. 1862 for xʷap-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung, Etym. Dict. of the Iranian Verb, *huap/f p.145-146 (CHEUNG.txt line 10203ff.)\", \"stance\": \"supports\",\n    \"note\": \"'*huap/f ‘to sleep’. AVESTAN: YAv. xʷab- (xʷaf-) ‘to sleep’ ... Pres. {2} inch.: IMPV. 2sg. YAv. xʷafsa (V 18.16, V 18.24), 2pl. xʷafsata (H 2.42); Perf.: IND. 3sg. YAv. husxʷafa (Y 57.17); Partic.: perf. pass. YAv. xʷapta- (V 18.46)'. Cheung knows no Avestan 'hufsa'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann col. 1347 (IEC.txt leaf 741)\", \"stance\": \"supports\",\n    \"note\": \"'suepo, io (1) ... Av. xwap-, v. id.; Per. xuftan, inf. ... (variant in) Per. xuspidan, Av. xwafs-, Oss. xüssin, inf. id. (fr. *sueps- or *suepsK-)'.\"}\n ],\n \"derivation_note\": None\n})\ndel e0[\"nodes\"][0][\"derivation_note\"]\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\",\n \"words\": \"xwâb, xuft\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian xwāb [hwʾb] 'sleep' and xuft, the past stem of xuftan 'to sleep' (present stem xufs-, Book Pahlavi hwps-, HLMWN-tn'), are both in MacKenzie's Concise Pahlavi Dictionary p.95. xuft continues Old Iranian *hwaf-ta- < *hwap-ta- (p > f before t), so it is the exact Iranian counterpart of Av. xᵛapta-. xwāb, however, does not come from xᵛafna-: MP has a separate reflex of that, xwamn [hwmn'] 'sleep, dream' (< *hwafna-, fn > mn), while xwāb continues an Iranian lengthened-grade noun *hwāpa- (Benveniste, BSL 30.75ff., accepted by Buck 4.61). Drawing xwāb from a box whose contents are xᵛap-/xᵛafna- is therefore right at the root level but slides over the fact that two different Iranian formations are involved.\",\n \"derivation_fa\": \"فارسی میانهٔ xwāb [hwʾb] «خواب» و xuft، مادهٔ ماضی xuftan «خفتن» (مادهٔ مضارع xufs-)، هر دو در فرهنگ کوچک پهلوی مکنزی ص ۹۵ آمده‌اند. xuft بازماندهٔ ایرانی باستان *hwaf-ta- < *hwap-ta- است (ابدال p به f پیش از t) و برابر دقیق xᵛapta- اوستایی است. اما «خواب» از xᵛafna- نیامده است: بازماندهٔ آن در پهلوی xwamn [hwmn'] «خواب، رؤیا» است (تحول fn به mn)، حال آنکه xwāb دنبالهٔ نام‌واژهٔ ایرانی *hwāpa- با مصوت کشیده است (بنونیست، BSL ۳۰، ص ۷۵ به بعد؛ مورد پذیرش باک). بنابراین کشیدن پیکان از جعبهٔ اوستایی به «خواب» در سطح ریشه درست است، ولی تفاوت دو ساخت ایرانی را نادیده می‌گیرد؛ ادعای نورایی با این احتیاط پذیرفتنی است.\",\n \"sources\": [W_XAB, W_XOFTAN],\n \"ref_check\": [\n   {\"ref\": \"FFD:50\", \"status\": \"supports\",\n    \"note\": \"Abolghasemi p.50-51 (scan read; refs/ocr/FFD/50.vision.txt): 'خفت ← فارسی میانه xuft ← ایرانی باستان *xwaf-ta' and 'خواب ← فارسی میانه xwāb: اسم است، در فارسی دری «خواب» به عنوان مادهٔ مضارع «خفتن» به کار رفته است'. Both of Nourai's Pahlavi words stand on the cited page (xwāb's own paragraph runs over onto p.51).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.95 (PHD.txt line 662-663; PHD_mackenzie.txt lines 5578, 5589, 5608)\", \"stance\": \"supports\",\n    \"note\": \"'xwāb [hwʾb | N ~] sleep' and 'xuftan, xufs- [HLMWN-tnʾ < A *llm; hwptnʾ, hwps- | M xwpt, N ~]'; also 'xwamn [hwmnʾ, hmnʾ | M xwmn] sleep, dream' — i.e. MP has both xwāb and xwamn.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. xuftan (NYB_vol2_glossary.txt line 4302)\", \"stance\": \"supports\",\n    \"note\": \"'xuftan [hwptnʾ; HLMWN-tnʾ] xʷafs-, to sleep, to fall asleep ... — Av. (1862) xʷap-, pres. xʷafsa-; MPrthPrs xwftn; Paz. xʷaftan, pres. avaft-, xʷafs-; NP xuftan, xuspidan, pres. xuāb.' Nyberg himself lists NP xuāb as the present stem — exactly the chart's Pahlavi>Persian link.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.61 (SYN.txt line 6908ff.)\", \"stance\": \"partial\",\n    \"note\": \"'Skt. svapna-, Av. xʷafna- (also Iran. *xʷāpa-, NPers. xʷāp, cf. Benveniste, BSL 30.75 ff.)' — Buck separates NP xʷāp/xwāb from xʷafna- and puts it on *xʷāpa-.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sogdian\",\n \"words\": \"xwbn; `wbs\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian γwβn / xwβn (Buddhist γwpn-, Christian xwbn) 'sleep, dream' is the exact cognate of Av. xᵛafna-: Gharib's entry 4346 prints 'xwapn, xuβn ⓔ<Av. xʷafna; Yaghn. xuvn ... sleep, dream'. The Sogdian verb ʾwβs- / wʾβs- 'to sleep, fall asleep' (Gharib no. 1856, Christian ʾwfs-, Buddhist wʾβs-) is not the bare root but the preverbed *ava-hufsa-, i.e. *ava- 'down' + the inchoative *hufsa-/*xʷafsa- of node #1; Gharib glosses it 'ⓔAv. hufsa-; Yaghn. ūfs-, Khot. hus; *awa-hufsa-' — which is also where Nourai's 'hufsa' in the Avestan box comes from. Cheung analyses the same forms as *huap/f + *aua-. Both Sogdian words are thus correctly placed under the root, though the arrow is better read 'Proto-Iranian → Sogdian' than 'Avestan → Sogdian'.\",\n \"derivation_fa\": \"واژهٔ سغدی γwβn / xwβn «خواب، رؤیا» (در متون بودایی γwpn-، در مسیحی xwbn) برابر دقیق xᵛafna- اوستایی است؛ قریب در مدخل ۴۳۴۶ می‌نویسد: «xwapn, xuβn، از اوستایی xʷafna؛ یغنابی xuvn؛ خواب، رؤیا». فعل سغدی ʾwβs-/wʾβs- «خفتن، به خواب رفتن» (مدخل ۱۸۵۶) ریشهٔ برهنه نیست، بلکه صورت پیشوند‌دار *ava-hufsa- است، یعنی پیشوند *ava- «فرو» به‌علاوهٔ ستاک آغازی *hufsa-/*xʷafsa-؛ همین یادداشتِ قریب («اوستایی hufsa-؛ یغنابی ūfs-؛ ختنی hus») سرچشمهٔ «hufsa» در جعبهٔ اوستایی نورایی است. چونگ نیز همین صورت‌ها را ذیل *huap/f با پیشوند *aua- می‌آورد. پس هر دو واژه به‌درستی زیر این ریشه نشسته‌اند، اگرچه پیکان را باید «ایرانی آغازین ← سغدی» خواند نه «اوستایی ← سغدی».\",\n \"sources\": [W_SWEP],\n \"ref_check\": [\n   {\"ref\": \"SOD:173\", \"status\": \"partial\",\n    \"note\": \"Gharib printed p.173 (SOD_pages.txt leaf 238) does carry entry '4346 γwpn- B | xwapn, xuβn ⓔ<Av. xwafna; Yaghn. xuvn ... slee[p], dream (GMS 503; VJ 3.4; SCE 5,7 ...)' — Nourai's xwbn (Gharib's Christian spelling, his cross-entry 10710 'xwbn C = xwpn-'). The second word `wbs is NOT on p.173: it is entry 1856 '*ʾwps- S | ufs, ofs ⓔAv. hufsa-; Yaghn. ūfs-, Khot. hus; *awa-hufsa- ... (to) sleep' (cf. 9784 wʾbs- B, 9807 wʽfs- C). So the page supports one of the two words; the other is elsewhere in the same dictionary.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib nos. 1856, 4346, 9784, 9807, 10710-10711\", \"stance\": \"supports\",\n    \"note\": \"'10711 xwpn- M, B | xupn (xwbn) ... sleep, dream'; '9784 wʾbs- B | wafs ⓔimpf. ... (to)sleep ... *awa-hufsa-'. Both of the chart's Sogdian words are real Gharib entries.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung *huap/f, SOGDIAN section (CHEUNG.txt ~line 10247)\", \"stance\": \"supports\",\n    \"note\": \"'SOGDIAN: CSogd. ʾspn- (denomin.) ‘to rest’ || (+ *aua-) BSogd. wβs-, CSogd. ʾwfs- ‘to sleep, fall asleep’' — confirms the preverb analysis of `wbs.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"xâb; xoftan; xoftak; xafj\",\n \"verdict\": \"plausible\",\n \"derivation\": \"خواب xāb < MP xwāb 'sleep, dream' (< Ir. *hwāpa-) and خفتن xoftan (pres. stem خسپ/خسب xosp/xosb, whence the secondary infinitives خسپیدن/خسبیدن) < MP xuftan, xufs- < OIr. *hwaf-ta-, *hwafsa-: both are straightforward continuations of the root, and Mo'in's own footnote at Borhān-e Qāṭeʿ p.746 s.v. خسپیدن cites Avestan xᵛafs- for it. خفتک xoftak 'nightmare' is the agent/diminutive in -ak on the same stem ('the thing that presses on the sleeper'), and BQT p.760 defines it as کابوس … سنگینی که در خواب بر مردم افتد; its by-form خفتو xoftu stands in the same column. The two extra forms in the chart are weaker: بختک baxtak, put here as a variant of خفتک, is not derived from خفتن by any modern source (Wiktionary gives it no etymology; it is normally referred to بخت), even though Moʿin's entry برخفج glosses that word 'کابوس، بختک، عبدالجنّه'. And خفج xafj / خفجا xafjā 'nightmare' is expressly detached from this root by Hübschmann on the very page Nourai cites: Persische Studien p.56 ad Horn 488, 'Ich trenne xafj ‘ephialtes’ von xuspidan ‘schlafen’ und stelle es mit de Lagarde zu zd. xawza- (phl. xafzik)'. Horn (p.107) had tentatively put xefj here, Hübschmann rejected it, and Nourai cites Hübschmann for it anyway. Verdict: xāb and xoftan confirmed, xoftak plausible, xafj (and the equation خفتک = بختک) not supported.\",\n \"derivation_fa\": \"«خواب» از فارسی میانهٔ xwāb «خواب، رؤیا» (از ایرانی *hwāpa-) و «خفتن» با مادهٔ مضارع «خسپ/خسب» (و از آن مصدرهای ثانوی خسپیدن و خسبیدن) از xuftan, xufs- پهلوی و ایرانی باستان *hwaf-ta-, *hwafsa- است؛ خود معین در حاشیهٔ برهان قاطع ص ۷۴۶ ذیل «خسپیدن» به xᵛafs- اوستایی ارجاع می‌دهد. «خفتک» نیز ساخت -ak بر همین ستاک است و برهان قاطع (ص ۷۶۰) آن را «کابوس … سنگینی که در خواب بر مردم افتد» تعریف کرده و گونهٔ «خفتو» را در همان ستون آورده است. اما دو صورت دیگر سست‌اند: «بختک» را که نورایی گونهٔ «خفتک» شمرده، هیچ منبع امروزی از «خفتن» نمی‌گیرد (ویکی‌واژه برای آن ریشه‌ای نمی‌دهد) هرچند معین در مدخل «برخفج» آن را با «کابوس، بختک» یکی گرفته است. «خفج/خفجا» را نیز هوبشمان درست در همان صفحه‌ای که نورایی به آن استناد کرده (پژوهش‌های فارسی، ص ۵۶، در نقد شمارهٔ ۴۸۸ هرن) از این ریشه جدا می‌کند: «من xafj را از xuspidan جدا می‌دانم و با دُ‑لاگارد آن را به xawza- اوستایی می‌بندم». پس: «خواب» و «خفتن» درست، «خفتک» پذیرفتنی، و «خفج» و یکی‌گرفتن «خفتک» با «بختک» پشتوانه ندارد.\",\n \"sources\": [W_XAB, W_XOFTAN, W_BAXTAK],\n \"ref_check\": [\n   {\"ref\": \"BQT:746\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' vol.2, printed p.746 (BQT_v2_pages.txt leaf 204) carries the entry خسپیدن/خسبیدن with Mo'in's etymological footnote: '* خسبیدن، خسپیدن ... اوستا [xʷafs-] ... اوسی [Ossetic xussun] ... خفتن، خوابیدن' (the Latin transliterations are mangled by the OCR but the Avestan reference and the gloss are legible).\"},\n   {\"ref\": \"BQT:760\", \"status\": \"supports\",\n    \"note\": \"vol.2 leaf 218 (p.760): 'خفتک ... کابوس است ... آن سنگینی و گرانیی باشد در خواب که بر مردم افتد، و معرّب آن خفتق است' and 'خفتو ... کابوس و عبدالجنّه است'; خفجا/خفج 'nightmare' follow on the same and the next column.\"},\n   {\"ref\": \"BQT:780\", \"status\": \"supports\",\n    \"note\": \"vol.2 leaf 237 (p.780): the خواب cluster — 'خواب جاوید', 'خواب خرگوش', 'خواب نادیده', 'خوابستان' with the Nezāmi and Farrokhi citations.\"},\n   {\"ref\": \"HUB:56\", \"status\": \"contradicts\",\n    \"note\": \"Hübschmann, Persische Studien p.56 (HUB.txt leaf 66), note on Horn no. 488: 'Ich trenne xafj „ephialtes“ von xuspidan „schlafen“ und stelle es mit de Lagarde zu zd. xawza- (phl. xafzik ...). Vgl. afgh. xapasa fem. „nightmare“.' The cited page denies exactly the link Nourai draws for xafj.\"},\n   {\"ref\": \"MON:1431\", \"status\": \"partial\",\n    \"note\": \"The 6-vol Amir Kabir pagination could not be checked (only the 2-vol Adena reprint is on disk), but Mo'in's entries were read there: 'خواب: (قد. ...) حالتی توأم با آسایش ...' (MON_part1.txt line 57677), 'خفتن: (مصل.) (خفت، خوابد ...) خوابیدن، خسبیدن' (line 56956), 'برخفج: [= برخغج، برغفج] کابوس، بختک، عبدالجنّه' (line 22225).\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn no. 483 (p.107) and no. 495 (p.110)\", \"stance\": \"partial\",\n    \"note\": \"no. 483 gives 'phlv. xʷaftan ... bezw. xuftan' for xospidan; no. 495: 'xʷāb „Schlaf“, xʷābiden. aw. xʷafna- „Schlaf“; phlv. xʷāb; ai. svápna-; arm. kʻun.' But at no. 483 Horn only tentatively adds 'Hierher gehört wohl auch np. xefj, xefjā, berxefj „Nachtmahr“' — the form Hübschmann then removed.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in (Adena 2-vol reprint) s.vv. خواب, خفتن, خفتیدن, برخفج\", \"stance\": \"partial\",\n    \"note\": \"Mo'in has all the words but gives no etymology for خفتک/خفج; his برخفج entry equates that word with بختک, which is as close as a Persian dictionary comes to Nourai's خفتک = بختک.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, خواب، خوابیدن, pp. 246-247 (ARY_pages.txt pdf pages 246-247)\", \"stance\": \"supports\",\n    \"note\": \"The cognate list runs Avestan / Pahlavi / Sanskrit / Greek HYPNOS / Latin SOPOR, SOMNUS, SOPIO / OE SWEFAN etc., with the remark 'در زبان‌های ایرانی برای «خواب» (به چم «خفتن») و «خواب» (به چم «آنچه در خواب دیده می‌شود») یک واژهٔ واحد به کار می‌رود'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung *huap/f, MIDDLE PERSIAN / PARTHIAN sections\", \"stance\": \"supports\",\n    \"note\": \"'MMP xwpt (pret. stem), BMP hwps- /xufs/ ... PARTHIAN: xwsp- (inch.) ‘to fall asleep, sleep’' — the Parthian metathesised xwsp- is the source of NP خسپ/خسب.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Greek\",\n \"words\": \"hupnos\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Ancient Greek ὕπνος (húpnos) 'sleep' goes back to Proto-Hellenic *húpnos < PIE *sup-nós, the zero-grade *sup- of *swep- plus the *-no- suffix; initial *s- before a vowel became the rough breathing h-, and *u is the vocalised *w of the cluster *sw-. It is the exact counterpart of Sanskrit svápna-, Latin somnus, Avestan xᵛafna- and Albanian gjumë. Watkins/AHD lists it under swep-1 as 'Suffixed zero-grade form *sup-no- in Greek hupnos, sleep', which is where the chart's box (labelled 'AHD') comes from.\",\n \"derivation_fa\": \"واژهٔ یونانی باستان ὕπνος (húpnos) «خواب» از یونانی آغازین *húpnos و آن از *sup-nós هندواروپایی آغازین است: تهی‌درجهٔ *sup- ریشهٔ *swep- به‌علاوهٔ پسوند *-no-. *s- آغازین پیش از واکه در یونانی به دمِ سخت (h-) بدل شده و u بازتاب واکه‌شدهٔ *w در خوشهٔ *sw- است. این واژه برابر دقیق svápna- سنسکریت، somnus لاتین، xᵛafna- اوستایی و gjumë آلبانیایی است. واتکینز نیز در AHD همین را ذیل swep-1 آورده است؛ همان جایی که نورایی از آن گرفته. ادعای نورایی درست است.\",\n \"sources\": [W_HUPNOS, W_SWEP],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. swep-1: '3. Suffixed zero-grade form *sup-no- in Greek hupnos, sleep: HYPNO-, HYPNOS, (HYPNOSIS), HYPNOTIC.' (AHD_watkins1985.txt line 1050).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. hypno- (KLN_1966.txt line 18479ff., p.~760)\", \"stance\": \"supports\",\n    \"note\": \"'hypno-, before a vowel hypn-, combining form meaning ‘sleep’. — Gk. ὑπνο-, ὑπν-, fr. ὕπνος, ‘sleep’, which stands for *sup-no-s and is cogn. with OI. svapnah, ‘sleep, dream’, L. somnus (for *swepnos or *swopnos), ‘sleep’.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 1048 (POK_full.txt line 84055)\", \"stance\": \"supports\",\n    \"note\": \"'Old Indie svapna- ‘sleep, dream’, Avestan xʷafna- m. ds.; Armenian kʻun ‘sleep’ (*suopnos); gr. ὕπνος ‘sleep’.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.61\", \"stance\": \"supports\",\n    \"note\": \"'Grk. hupnos; Lat. somnus (> It. sonno, Sp. sueño ...)' listed under IE *swep-.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"French\",\n \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The empty French box stands for hypnotisme (first recorded 1845), the French relay by which the word reached Persian. Formally French hypnotisme is hypnotique + -isme (French Wiktionary), and hypnotique is attested from the 16th c. from Late Latin hypnōticus < Greek hupnōtikós 'inclined to sleep' < hupnoûn 'to put to sleep' < hupnos. Historically, however, the modern sense is not a French creation: it follows James Braid's English hypnotism (1843, short for neuro-hypnotism 1842), which the French adopted almost at once. So the box is legitimate as a relay but the arrow Greek → French skips the English coinage that gave the word its meaning.\",\n \"derivation_fa\": \"جعبهٔ خالی «فرانسه» در نمودار نمایندهٔ واژهٔ hypnotisme فرانسوی (نخستین کاربرد ۱۸۴۵) است، یعنی همان حلقه‌ای که واژه از راه آن به فارسی رسیده است. از نظر ساخت، hypnotisme از hypnotique به‌علاوهٔ پسوند -isme ساخته شده و hypnotique خود از سدهٔ شانزدهم از لاتین متأخر hypnoticus و آن از hupnōtikós یونانی «خواب‌آور» از hupnos آمده است. اما از نظر تاریخی معنای امروزی آن ساختهٔ فرانسه نیست: جیمز برید در ۱۸۴۳ در انگلستان hypnotism را ساخت و فرانسویان بی‌درنگ آن را گرفتند. پس این حلقه درست است ولی پیکان «یونانی ← فرانسه» مرحلهٔ انگلیسی را نادیده می‌گیرد؛ با احتیاط پذیرفتنی است.\",\n \"sources\": [FR_HYP, E_HYPNO],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); checked against the French Wiktionary and Etymonline instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. hypnotic, hypnotism (KLN_1966.txt lines 18488-18489)\", \"stance\": \"partial\",\n    \"note\": \"'hypnotic, adj. — L. hypnoticus, fr. Gk. ὑπνωτικός ... fr. ὕπνος, ‘sleep’'; 'hypnotism, n. — Coined by James Braid of Manchester (1795-1861) fr. hypnotic and suff. -ism.' Klein makes the -ism word English, not French.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. hypnotic (archived)\", \"stance\": \"partial\",\n    \"note\": \"'hypnotic (adj.) 1620s, of drugs, ‘inducing sleep’, from French hypnotique (16c.) ‘inclined to sleep, soporific’, from Late Latin hypnoticus, from Greek hypnotikos' — the French adjective is old, the -isme noun is 19th c.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Persian\",\n \"words\": \"hîpnotîsm\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian هیپنوتیسم (also and more commonly هیپنوتیزم hipnotizm) 'hypnotism' is a 20th-century learned borrowing of French hypnotisme; the spelling with س reproduces the French -sme, the spelling with ز the pronunciation. Mo'in's dictionary tags the word '[فر.]' (= French) and defines it خواب مصنوعی، خواب مغناطیسی که در آن شخص تحت تأثیر القاهای شخص دیگر به خواب می‌رود; Amid, whom Nourai cites, has the same word. The chart's route Greek > French > Persian is therefore right for this final link, and the Persian word is an exact doublet of English hypnotism from the same Greek hupnos as خواب, i.e. a word that re-entered Persian through Europe after some 3,000 years.\",\n \"derivation_fa\": \"«هیپنوتیسم» (و رایج‌تر «هیپنوتیزم») وام‌واژه‌ای است که در سدهٔ چهاردهم خورشیدی از فرانسوی hypnotisme گرفته شده؛ املای با «س» بازتاب -sme فرانسوی و املای با «ز» بازتاب تلفظ آن است. فرهنگ معین این واژه را با نشان «[فر.]» یعنی فرانسوی آورده و چنین تعریف کرده است: «خواب مصنوعی، خواب مغناطیسی که در آن شخص تحت تأثیر القاهای شخص دیگر به خواب می‌رود»؛ فرهنگ عمید (مأخذ نورایی) نیز همین را دارد. بنابراین حلقهٔ پایانی نمودار درست است و نکتهٔ گیرا آن است که این واژه دوگانهٔ (doublet) «خواب» است: هر دو از یک ریشهٔ هندواروپایی‌اند، یکی از راه ایرانی باستان و دیگری پس از سه هزاره از راه یونانی و فرانسوی به فارسی بازگشته است.\",\n \"sources\": [AB_HYP, FR_HYP],\n \"ref_check\": [\n   {\"ref\": \"AMD:1985\", \"status\": \"partial\",\n    \"note\": \"Amid's 2-vol 1369 pagination is not mappable (refs_online.json: 'page numbers of the 2-vol 1369 print not mappable'), so the page could not be verified; the entry itself was read on abadis.ir, which reproduces فرهنگ عمید: 'عملی که طی آن کسی را به خواب مصنوعی فرو می‌برند ...'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir s.v. هیپنوتیزم (archived)\", \"stance\": \"supports\",\n    \"note\": \"'فرهنگ معین: (نُ تِ ) [ فر. ] (اِ. ) خواب مصنوعی، خواب مغناطیسی ...' — the tag [فر.] is Mo'in's mark for a French loan, exactly the chart's French > Persian arrow.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. hypnotism (archived)\", \"stance\": \"supports\",\n    \"note\": \"'hypnotism (n.) 1843, short for neuro-hypnotism (1842), coined by Dr. James Braid of Manchester, England, from hypnotic + -ism' — dates the European word that Persian then borrowed.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 8, \"lang\": \"English\",\n \"words\": \"hypnotism\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English hypnotism was coined in 1843 by the Manchester surgeon James Braid, shortened from his own neuro-hypnotism (1842), on hypnotic + -ism; in the same work he coined hypnotize, and hypnosis and hypnotist followed. hypnotic itself is older (1620s, of soporific drugs), from French hypnotique, Late Latin hypnōticus, Greek hupnōtikós, from hupnos 'sleep'. Watkins's AHD entry swep-1 accordingly lists HYPNO-, HYPNOS, (HYPNOSIS), HYPNOTIC among the English descendants of the root, which is Nourai's reference.\",\n \"derivation_fa\": \"واژهٔ انگلیسی hypnotism را در ۱۸۴۳ جیمز برید، جرّاح منچستری، از کوتاه‌کردن ساختهٔ خودش neuro-hypnotism (۱۸۴۲) و بر پایهٔ hypnotic + -ism ساخت؛ در همان اثر hypnotize را هم ساخت و سپس hypnosis و hypnotist پدید آمدند. خودِ hypnotic کهن‌تر است (۱۶۲۰م، دربارهٔ داروهای خواب‌آور) و از hypnotique فرانسوی، hypnoticus لاتین متأخر و hupnōtikós یونانی از hupnos «خواب» می‌آید. واتکینز نیز در مدخل swep-1 فرهنگ AHD واژه‌های HYPNO-, HYPNOS, HYPNOSIS, HYPNOTIC را در شمار بازماندگان انگلیسی این ریشه آورده است؛ همان مأخذ نورایی. ادعای نورایی درست است.\",\n \"sources\": [E_HYPNO, W_HUPNOS],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. swep-1: '... in Greek hupnos, sleep: HYPNO-, HYPNOS, (HYPNOSIS), HYPNOTIC. [Pok. 1. swep- 1048.]'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. hypnotism (KLN_1966.txt line 18489)\", \"stance\": \"supports\",\n    \"note\": \"'hypnotism, n. — Coined by James Braid of Manchester (1795-1861) fr. hypnotic and suff. -ism. Cp. hypnosis.'\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. hypnotism (archived)\", \"stance\": \"supports\",\n    \"note\": \"'1843, short for neuro-hypnotism (1842), coined by Dr. James Braid of Manchester, England, from hypnotic + -ism.'\"}\n ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ---------------- ENTRY 1 -----------------------------------------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Swer\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *swer- 'to cut, pierce; to fester' (Pokorny 1050, su̯er-4 'schneiden, stechen'; Walde-Pokorny II 529 su̯er- 'schwären, eitern'; Mann, IEC 1348 suer- (3)/(4))\",\n \"note\": \"Both of Nourai's references are exact. Pokorny p.1050 has 'Root/lemma: suer-4, Meaning: to cut, pierce. Material: Avestan xʷara- n. ‘wound, Verwundung’ ... OHG swert ‘Schwert’, OE sweord, ON sverd from *swer-da- ‘stechende weapon’', and Mann's col. 1348 has both 'suer- (3) ‘harm, hurt, corrupt’' and 'suer-, -on, -en (4) ‘swelling, suppuration, gangrene, ulcer’' with the Avestan and Persian words of this chart. Nourai's gloss 'to press, cut, hurt' is Klein's wording at KLN:1554 ('I.-E. base *swer-, ‘to press, torment’, orig. ‘to cut’'). The only caution: p.1050 of Pokorny carries five homophonous roots su̯er-1..5 ('hang/weigh', 'hiss', 'stake', 'cut', 'weigh'), and the chart's redirect entry 'Swer -> Wer 6' on the same book page shows Nourai knew this; the one meant here is unambiguously su̯er-4.\",\n \"note_fa\": \"هر دو ارجاع نورایی دقیق است. پوکورنی در ص ۱۰۵۰ ریشهٔ su̯er-4 را با معنای «بریدن، سوراخ کردن» آورده و مادهٔ آن را چنین داده است: «xʷara- اوستایی، خنثی، ‹زخم› ... و swert آلمانی کهن، sweord انگلیسی کهن، sverð نورس کهن از *swer-da- ‹سلاح برنده›»؛ مان نیز در ستون ۱۳۴۸ هم suer- (3) «آسیب رساندن، فاسد کردن» و هم suer- (4) «آماس، چرک، خوره، زخم» را با همان واژه‌های اوستایی و فارسی این نمودار می‌آورد. معنای «فشردن، بریدن، آزردن» که نورایی داده، عیناً عبارت کلاین در ص ۱۵۵۴ است. تنها نکتهٔ احتیاطی آنکه در ص ۱۰۵۰ پوکورنی پنج ریشهٔ هم‌آوا su̯er- آمده و مقصود اینجا بی‌گمان شمارهٔ ۴ است. ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n \"sources\": [W_SWORD, W_SWERDA],\n \"ref_check\": [\n   {\"ref\": \"POK:1050\", \"status\": \"supports\",\n    \"note\": \"IEW p.1050 (POK_full.txt line 84255): 'Root / lemma: suer-4. Meaning: to cut, pierce. Material: Avestan xʷara- n. ‘wound, Verwundung’; Old Irish serb, cymr. chwerw ‘bitter’ (*suer-uo) ... Old High German swer(a)do ‘leiblicher pain’ ... Old High German sweort ‘Schwert’, Old English sweord, Old Icelandic sverd from *swer-da- ‘stechende weapon’. References: WP. II 529 ... Page(s): 1050.'\"},\n   {\"ref\": \"IEC:1348\", \"status\": \"supports\",\n    \"note\": \"Mann, An Indo-European Comparative Dictionary, printed col. 1348 (IEC.txt leaf 742, the leaf whose running numbers are 1348/1349): 'suer- (3) “harm, hurt, corrupt. See next. Skt. svarami, v. (1) ‘blame’; Av. xwar-, v. ‘blame, injure’; xwairis, s. ‘abuse, blame’; Per. xware, s. ‘corruption, gangrene’ ...' and 'suer-, -on, -en (suor-, sur-) (4) ‘swelling, suppuration, gangrene, ulcer’ ... Av. xwaro, m. ‘wound’; Per. xware, s. ‘gangrene; leprosy?’ ...'. Exactly the material of nodes #3 and #4.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 529 (WLD_Bd2_pages.txt leaf 533)\", \"stance\": \"partial\",\n    \"note\": \"'4. su̯er- „schwaren, eitern“. Av. xʷara- m. „Wunde, Verwundung“; ahd. sweran st. V. „schmerzen, eitern, schwaren, schwellen“, swero „leiblicher Schmerz, bes. Geschwur“ ... ags. sweornian „gerinnen“.' The 1927 version glosses the root ‘fester, suppurate’ and does NOT yet list Germanic *swerda- under it; Pokorny 1959 added the sword.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. swer-4 (AHD_watkins1985.txt line 1052)\", \"stance\": \"supports\",\n    \"note\": \"'swer-4. To cut, pierce. Germanic *swerdam in Old English sweord, sword, sword: SWORD. [Pok. 4. suer- 1050.]' — the chart's gloss, its Germanic form and its reference all come from here.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein p.1553-1554 s.v. sword (KLN_1966.txt line 37760)\", \"stance\": \"supports\",\n    \"note\": \"'fr. Teut. *swerda, lit. ‘the cutting weapon’, formed fr. I.-E. base *swer-, ‘to press, torment’, orig. ‘to cut’, and Teut. suff. -da. Avestic xvara, ‘wound’, OI. svar-, ‘to torment’, are from the same base.'\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"xvara\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Avestan word is real, but not with this gloss. Bartholomae, Pokorny (IEW 1050), Walde-Pokorny (II 529), Klein (p.1554) and Mann (col. 1348) all give Av. xᵛara- 'wound, injury' (Wunde, Verwundung) — never 'thorn'; MacKenzie's Pahlavi dictionary even preserves it as a technical term, '2xwar [xwl = Av. xᵛara-] a degree of sin', i.e. one of the graded bodily injuries of the Vidēvdād penal code. Formally xᵛara- is *swer-o- with the regular Iranian *sw- > xᵛ-. The sense 'to pierce' is a back-projection from the root meaning and from the Persian words Nourai hangs on it; 'thorn' has no Avestan warrant at all. Note also that this box and box #3 (xwarô 'wound') are one and the same Avestan word entered twice, once from Pokorny/Klein and once from Mann.\",\n \"derivation_fa\": \"واژهٔ اوستایی واقعی است، اما نه با این معنا. بارتولومه، پوکورنی (ص ۱۰۵۰)، والده‑پوکورنی (ج ۲ ص ۵۲۹)، کلاین (ص ۱۵۵۴) و مان (ستون ۱۳۴۸) همگی xᵛara- اوستایی را «زخم، جراحت» معنا کرده‌اند، نه «خار»؛ مکنزی حتی بازماندهٔ آن را در پهلوی به‌عنوان اصطلاح حقوقی نگه داشته است: «xwar [= اوستایی xᵛara-] درجه‌ای از گناه»، یعنی یکی از درجه‌بندی‌های جراحت بدنی در نظام کیفری وندیداد. از نظر ساخت، xᵛara- همان *swer-o- است با تحول قاعده‌مند *sw- به xᵛ- در ایرانی. معنای «سوراخ کردن» برگرفته از معنای خودِ ریشه و از واژه‌های فارسی‌ای است که نورایی به آن آویخته، و «خار» هیچ پشتوانهٔ اوستایی ندارد. افزون بر این، این جعبه و جعبهٔ ۳ («xwarô: زخم») یک واژه‌اند که دو بار، یک‌بار از پوکورنی/کلاین و یک‌بار از مان، وارد نمودار شده‌اند.\",\n \"sources\": [W_SWERDA],\n \"ref_check\": [\n   {\"ref\": \"POK:1050\", \"status\": \"partial\",\n    \"note\": \"IEW 1050 su̯er-4 opens 'Material: Avestan xʷara- n. ‘wound, Verwundung’' — the form and the page are right, the gloss ‘thorn, to pierce’ is not Pokorny's.\"},\n   {\"ref\": \"KLN:1554\", \"status\": \"partial\",\n    \"note\": \"Klein p.1554 s.v. sword: 'Avestic xvara, ‘wound’, OI. svar-, ‘to torment’, are from the same base.' Same form, same page, but again ‘wound’.\"}\n  ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 529\", \"stance\": \"partial\",\n    \"note\": \"'Av. xʷara- m. „Wunde, Verwundung“' — wound, not thorn.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.95 (PHD.txt line 663)\", \"stance\": \"supports\",\n    \"note\": \"'2xwar [xwl = Av. xʷara-] a degree of sin' — independent evidence that the Avestan word denotes a bodily wound, continued into Middle Persian legal usage.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, xʷara- (col. ~1869; the local OCR of BRT breaks off at col. ~1853)\", \"stance\": \"silent\",\n    \"note\": \"The article itself is beyond the end of the available scan text; greps for 'xʷara' return only compounds such as F.9a 'xʷarəðəm ... wie sie für Verwundungen (Lebender) bestimmt ist' (BRT.txt line 19853), which is consistent with ‘wound’.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"xalîdan; xaleh; xale-bân\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The three Persian words are real and internally consistent: خلیدن xalīdan 'to prick, to pierce' (pres. stem خل xal; Gorgāni, Vis o Rāmin: گهی خارش به دست اندر خلیده), خله xale, in Borhān-e Qāṭeʿ (p.766) both 'چوب درازی که بدان کشتی می‌رانند' (the punting pole/oar) and 'چیز خلیده و فرورونده در جایی ... مانند سوزن و جوالدوز و درفش', and خلبان xalabān, an Iranian Academy purism of the 1930s replacing پیلت and طیاره‌چی, formed خله + ـبان and originally 'oarsman' — Moʿin's entry reads 'خلبان [< خله‌بان] آنکه هواپیما را هدایت کند، هوانورد' and Wiktionary 'From خله (xale, \\\"helm, oar\\\") + ـبان'. So the internal Persian chain خله → خلیدن → خلبان is confirmed. What is not established is the arrow from Av. xᵛara-: Horn at the page Nourai cites (p.109, no. 492 خله/خلیدن) derives the word, after West, from Av. hareθi-, and only records that 'de Lagarde, Beitr. z. altb. Lex. 38 wollte aw. xᵛara- \\\"Wunde\\\" vergleichen', adding that the meanings of the Avestan and Middle Persian words are uncertain; Hübschmann (p.56, ad Horn 492) rejects Horn's hareθi- — 'Np. xala \\\"res acuta, ictus, vulnus\\\" etc. gehört jedenfalls nicht dazu' — without adopting xᵛara-; and Wiktionary still marks the etymology of خلیدن as missing. Phonetically *xʷara- > xale would also need an unexplained r > l. Nourai is therefore repeating a 19th-century conjecture of de Lagarde's, not a settled derivation.\",\n \"derivation_fa\": \"هر سه واژهٔ فارسی واقعی و با یکدیگر سازگارند: «خلیدن» یعنی «فرو رفتن چیز نوک‌تیز، سوزن‌سوزن شدن» با مادهٔ مضارع «خل» (فخرالدین گرگانی در ویس و رامین: «گهی خارش به دست اندر خلیده»)؛ «خله» که برهان قاطع (ص ۷۶۶) هم «چوب درازی که بدان کشتی می‌رانند» یعنی پارو، و هم «چیز خلیده و فرورونده در جایی … مانند سوزن و جوالدوز و درفش» معنا کرده است؛ و «خلبان» که ساختهٔ فرهنگستان اول در دههٔ ۱۳۱۰ به‌جای «پیلت» و «طیاره‌چی» است، از «خله + ـبان» و در اصل «پاروزن» — معین می‌نویسد «خلبان [< خله‌بان] آنکه هواپیما را هدایت کند، هوانورد» و ویکی‌واژه نیز همین را می‌گوید. پس زنجیرهٔ درون‌فارسی «خله ← خلیدن ← خلبان» تأیید می‌شود. آنچه اثبات نشده پیکانِ «اوستایی xᵛara- ← خلیدن» است: هرن در همان صفحه‌ای که نورایی به آن ارجاع داده (ص ۱۰۹، شمارهٔ ۴۹۲) به پیروی از وست واژه را از hareθi- اوستایی می‌گیرد و تنها یادآور می‌شود که «دُ‑لاگارد می‌خواست xᵛara- ‹زخم› را با آن بسنجد» و می‌افزاید که معنای صورت‌های اوستایی و پهلوی نامطمئن است؛ هوبشمان (ص ۵۶) رأی هرن را رد می‌کند ولی xᵛara- را هم نمی‌پذیرد؛ و ویکی‌واژه هنوز ریشهٔ «خلیدن» را نامعلوم می‌داند. از نظر آوایی نیز تبدیل r به l در *xʷara- > xale توضیح‌ناپذیر می‌ماند. بنابراین نورایی حدسی از سدهٔ نوزدهم را بازگو می‌کند، نه ریشه‌شناسی‌ای پذیرفته‌شده.\",\n \"sources\": [W_XALID, W_XALBAN],\n \"ref_check\": [\n   {\"ref\": \"HRN:109\", \"status\": \"partial\",\n    \"note\": \"Horn, Grundriss p.109 no. 492 (HRN.txt leaf 130): 'xele (xole) „Wunde, Spitzes; Geschwätz“, xeliden. aw. hareθiš; phlv. havak bezw. xarah, vd. 2 (89). Die Etymologie stammt von West ...; die Bedeutung der aw. und mittelp. Worte ist unsicher, ebenso die Grundbedeutung des neupersischen. ... de Lagarde, Beitr. z. altb. Lex. 38 wollte aw. xʷara- „Wunde“ vergleichen.' The page has Nourai's claim, but only as a rejected-or-at-best-optional alternative to Horn's own hareθi-.\"},\n   {\"ref\": \"BQT:766\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' vol.2 leaves 223-224 (pp.766-767): 'خله – بفتح اول و ثانی، چوب درازی که بدان کشتی می‌رانند؛ و باین معنی بضم اول هم آمده است و چیز خلیده و فرورونده در جایی باشد مانند سوزن و جوالدوز و درفش'; also 'خلنده ... باندرون رونده و مجروح کننده را گویند' and 'خلش ... بمعنی جراحت کردن و فرو بردن'. Both of Nourai's senses of خله (oar and piercer) stand on the cited page; BQT offers no etymology.\"},\n   {\"ref\": \"DMO:110\", \"status\": \"not_checked\",\n    \"note\": \"Sa'id Nafisi, Dar Maktab-e Ostad — refs_online.json records it as available only behind a ketabnak login and 'not fetched'; no copy on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.56, note on Horn 492 (HUB.txt leaf 66)\", \"stance\": \"contradicts\",\n    \"note\": \"'Zd. hareθi- = phl. halak = paz. hala ‘foolish, silly’ ... liesse ein np. *hala ‘töricht, verrückt’ erwarten. Np. xala ‚res acuta, ictus, vulnus“ etc. gehört jedenfalls nicht dazu.' Hübschmann demolishes Horn's derivation and proposes nothing in its place — certainly not Av. xʷara-.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in s.vv. خله, خلبان, خلانیدن (MON_part1.txt lines 57105, 57303-57306)\", \"stance\": \"supports\",\n    \"note\": \"'خله: (ا.) چوب درازی که بدان کشتی رانند؛ پاروی قایق‌رانی'; 'خله: (ا.) آنچه که در چیزی یا جایی بخلد و فرو رود مانند سوزن، جوال‌دوز، درفش'; 'خلبان: [< خله‌بان] آنکه هواپیما را هدایت کند، هوانورد'. Mo'in confirms Nourai's خلبان < خله‌بان but supplies no Avestan antecedent.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung, Etymological Dictionary of the Iranian Verb\", \"stance\": \"silent\",\n    \"note\": \"Greps for '*xal', 'xalidan', 'xal-' in CHEUNG.txt return nothing: Cheung reconstructs no Iranian verbal root for خلیدن, so the verb has no accepted Old Iranian ancestor.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Avestan\",\n \"words\": \"xwarô\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"'xwarô' is Mann's citation form of the same Avestan word as node #1: IEC col. 1348, under 'suer-, -on, -en (suor-, sur-) (4) \\\"swelling, suppuration, gangrene, ulcer\\\"', reads 'Av. xwaro, m. \\\"wound\\\"'. The word is Av. xᵛara- 'wound, injury' (Bartholomae; Pokorny 1050 'xʷara- n. Wunde, Verwundung'; Walde-Pokorny II 529 'xʷara- m. Wunde, Verwundung'); Mann simply quotes the nominative with his own -ō and assigns it masculine gender where Pokorny has neuter. It continues *swer-o-/-es- with Iranian *sw- > xᵛ-, and its Welsh and German congeners chwaren 'gland', OHG swero, NHG Geschwür 'ulcer' show the same 'festering wound' semantics. The derivation from the root is sound; the only defect is that the chart splits one Avestan lexeme into two boxes.\",\n \"derivation_fa\": \"«xwarô» صورت استنادی مان از همان واژهٔ اوستایی گرهٔ ۱ است: در ستون ۱۳۴۸ فرهنگ تطبیقی هندواروپایی، ذیل «suer- (4) ‹آماس، چرک، خوره، زخم›»، آمده است: «Av. xwaro, m. ‹wound›». این واژه همان xᵛara- اوستایی «زخم، جراحت» است (بارتولومه؛ پوکورنی ص ۱۰۵۰ «xʷara- خنثی، Wunde, Verwundung»؛ والده‑پوکورنی ج ۲ ص ۵۲۹). مان تنها صورت فاعلی را با ō خود نقل کرده و جنس آن را مذکر گرفته، حال آنکه پوکورنی خنثی می‌داند. این واژه بازماندهٔ *swer-o-/-es- است با تحول *sw- به xᵛ- در ایرانی، و هم‌خانواده‌های آن یعنی chwaren ولزی «غده» و swero آلمانی کهن و Geschwür آلمانی «دُمل» همان معنای «زخم چرکین» را نشان می‌دهند. پس این پیکان درست است؛ تنها ایراد آن است که نمودار یک واژهٔ اوستایی را در دو جعبه آورده است.\",\n \"sources\": [W_SWERDA],\n \"ref_check\": [\n   {\"ref\": \"IEC:1348\", \"status\": \"supports\",\n    \"note\": \"IEC.txt leaf 742 (printed 1348): 'suer-, -on, -en (suor-, sur-) (4) ‘swelling, suppuration, gangrene, ulcer’. Cf. suer- (3) above. Av. xwaro, m. ‘wound’; Per. xware, s. ‘gangrene; leprosy?’ ... W. cf. chwaren, f. (“gland”, fr. *suoren-) ... OHG swéro, wm., MHG swér(e) ‘ulcer’.' Verbatim Nourai.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 1050 su̯er-4\", \"stance\": \"supports\",\n    \"note\": \"'Avestan xʷara- n. ‘wound, Verwundung’' — the same word, with neuter gender.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 529\", \"stance\": \"supports\",\n    \"note\": \"'4. su̯er- „schwaren, eitern“. Av. xʷara- m. „Wunde, Verwundung“; ahd. sweran ... swero „leiblicher Schmerz, bes. Geschwur, Geschwulst“, nhd. Schwäre, Geschwür.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 20.27 SWORD (SYN.txt line 34804ff.)\", \"stance\": \"supports\",\n    \"note\": \"'ON sverd, OE sweord ... perh. : OHG sweran ‘cause or suffer pain’, swero ‘pain’, Ir. serb ‘bitter’, Av. xʷara- ‘wound’ (Walde-P. 2.529), with orig. sense of root ‘sting, cut’(?)'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"xoreh\",\n \"verdict\": \"disputed\",\n \"derivation\": \"خوره xore 'a wasting disease; leprosy, gangrene' is real, old and well attested (Bahāʾ al-Dīn ʿĀmilī uses خورهٔ شکم). Mann does connect it with *swer- (IEC 1348: 'Per. xware, s. \\\"gangrene; leprosy?\\\" beside xīre, adj. \\\"malignant\\\"'), so Nourai reports his source correctly — but Mann stands alone. The received analysis, which the chart's own NOTE attributes to MON:1455 and which modern scholarship shares, is transparent and Persian-internal: خور xor, the present stem of خوردن xordan 'to eat', plus the nominal suffix ـه -a, 'the thing that eats (away)'. Moʿin's definition is itself the etymology — 'خوره: آنچه که چیزی را بخورد و از میان برد؛ (پزشکی) جذام' — and Wiktionary gives 'From خور (xor, present stem of خوردن (xordan, \\\"to eat\\\")) +‎ ـه (-e)'. The same metaphor gives Arabic آکلة ākila and English 'canker/eating disease'. Nourai himself flags the conflict and cross-refers to his root Swel 1; the modern view is MON's, so this arrow should be dropped.\",\n \"derivation_fa\": \"«خوره» به معنی بیماری فرساینده، جذام و قانقاریا واژه‌ای کهن و گواهی‌شده است (بهاءالدین عاملی: «به خورهٔ شکم مبتلا شد»). مان در ستون ۱۳۴۸ آن را به ریشهٔ *swer- می‌بندد («Per. xware ‹gangrene; leprosy?› در کنار xīre ‹بدخیم›»)، پس نورایی مأخذ خود را درست نقل کرده است — اما مان در این رأی تنهاست. تحلیل پذیرفته‌شده، که خودِ یادداشت نمودار آن را به معین (ص ۱۴۵۵) نسبت می‌دهد و پژوهش امروزی نیز همان را می‌گوید، سراسر درون‌فارسی و آشکار است: «خور»، مادهٔ مضارع «خوردن»، به‌علاوهٔ پسوند اسم‌ساز «ـه»، یعنی «آنچه می‌خورد». تعریف معین خود ریشه‌شناسی است: «خوره: آنچه که چیزی را بخورد و از میان برد؛ (پزشکی) جذام»، و ویکی‌واژه نیز می‌نویسد «از خور، مادهٔ مضارع خوردن + ـه». همین استعاره در «آکِله» عربی و در canker انگلیسی نیز دیده می‌شود. نورایی خود به این اختلاف اشاره کرده است؛ پژوهش امروزی جانب معین را می‌گیرد و این پیکان باید کنار گذاشته شود.\",\n \"sources\": [W_XORE],\n \"ref_check\": [\n   {\"ref\": \"IEC:1348\", \"status\": \"supports\",\n    \"note\": \"Mann col. 1348 really does say it: 'suer- (3) … Per. xware, s. ‘corruption, gangrene’; cf. xīre, adj. ‘malignant’' and 'suer- (4) … Per. xware, s. ‘gangrene; leprosy?’'. The reference supports Nourai's arrow; it is the reference itself that modern scholarship does not follow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in s.v. خوره (MON_part1.txt line 58060)\", \"stance\": \"contradicts\",\n    \"note\": \"'خوره: (ا.) آنچه که چیزی را بخورد و از میان برد. (پز.) جذام.' Mo'in's gloss is itself the derivation from خوردن, exactly as the chart's NOTE says (MON:1455).\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (greps for xore / xure)\", \"stance\": \"silent\",\n    \"note\": \"Horn has no entry for خوره ‘leprosy’ under xʷara- or elsewhere in the xʷ- section (nos. 490-497); he treats only xʷardan ‘eat’ and its family.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.2, خوره entries (BQT_v2_pages.txt leaves 180, 200-201, 245-251)\", \"stance\": \"silent\",\n    \"note\": \"Borhan lists خوره in several senses but attaches no etymological footnote from Mo'in to the disease word.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Germanic\",\n \"words\": \"swerdam\",\n \"verdict\": \"plausible\",\n \"derivation\": \"'swerdam' is Watkins's citation form (AHD swer-4: 'Germanic *swerdam in Old English sweord'); the standard reconstruction today is Proto-Germanic *swerdą n. 'sword' (a neuter a-stem, whence OS/OFris. swerd, ON sverð, OHG swert, Du. zwaard). The traditional derivation, which Nourai follows and which Pokorny 1050 and Klein p.1554 both state — *swer-dʰ-o-, literally 'the cutting/stabbing weapon', from *swer- 'to cut, pierce', with the Slavic 'drill' words (*svьrdьlъ) as parallels — is respectable but no longer secure: every other descendant of *swer- means 'ache, fester, suppurate' rather than 'cut', Buck already called the Germanic word 'etym. dub.', Walde-Pokorny II 529 did not list it under the root at all, and Wiktionary now labels it 'of disputed origin', reporting Nikolaev (2015), who takes *swerdą from *sw-er, locative of *seh₂w- 'sharp', with Luwian šiwal- 'sword' as a cognate. So: a well-established traditional etymology, contested by current scholarship.\",\n \"derivation_fa\": \"«swerdam» صورت استنادی واتکینز است (در AHD ذیل swer-4: «ژرمنی *swerdam در sweord انگلیسی کهن»)؛ بازسازی معیار امروز *swerdą ژرمنی آغازین «شمشیر» است (ستاک a خنثی، که swerd ساکسونی و فریزی کهن، sverð نورس کهن، swert آلمانی کهن و zwaard هلندی از آن آمده‌اند). ریشه‌شناسی سنتی که نورایی پیروی می‌کند و پوکورنی (ص ۱۰۵۰) و کلاین (ص ۱۵۵۴) هر دو آورده‌اند — *swer-dʰ-o- به معنی تحت‌اللفظی «سلاح برنده/فروبرنده» از ریشهٔ *swer- «بریدن، سوراخ کردن»، با شاهد واژه‌های اسلاوی به معنی «مته» — محترم اما دیگر قطعی نیست: همهٔ بازماندگان دیگر *swer- معنای «درد گرفتن، چرک کردن» دارند نه «بریدن»؛ باک همان زمان آن را «ریشه‌اش مشکوک» خوانده بود؛ والده‑پوکورنی در ۱۹۲۷ اصلاً آن را ذیل این ریشه نیاورده؛ و ویکی‌واژه امروز آن را «با خاستگاه مورد اختلاف» می‌داند و رأی نیکولایف (۲۰۱۵) را نقل می‌کند که *swerdą را از *sw-er، صورت مکانی *seh₂w- «تیز»، و هم‌ریشه با šiwal- لوویایی «شمشیر» می‌گیرد. پس: ریشه‌شناسی سنتیِ جاافتاده‌ای که پژوهش امروزی در آن تردید دارد.\",\n \"sources\": [W_SWERDA, W_SWORD],\n \"ref_check\": [\n   {\"ref\": \"KLN:1554\", \"status\": \"supports\",\n    \"note\": \"Klein p.1553-1554 s.v. sword (the page number 1554 is printed inside the entry): 'fr. Teut. *swerda, lit. ‘the cutting weapon’, formed fr. I.-E. base *swer-, ‘to press, torment’, orig. ‘to cut’, and Teut. suff. -da.' Exactly Nourai's arrow, page verified.\"},\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985: 'swer-4. To cut, pierce. Germanic *swerdam in Old English sweord, sword, sword: SWORD. [Pok. 4. suer- 1050.]' — the chart's form *swerdam is copied letter for letter.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 1050 su̯er-4\", \"stance\": \"supports\",\n    \"note\": \"'Old High German sweort „Schwert“, Old English sweord, Old Icelandic sverd from *swer-da- „stechende weapon“'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 529\", \"stance\": \"silent\",\n    \"note\": \"The 1927 entry for su̯er- ‘schwaren, eitern’ lists only av. xʷara-, ahd. sweran/swero, ags. sweornian — the sword is absent; it was added in Pokorny's 1959 revision.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 20.27 SWORD\", \"stance\": \"partial\",\n    \"note\": \"'ON sverd, OE sweord, etc., general Gmc. (except Goth.), etym. dub., perh. : OHG sweran ‘cause or suffer pain’ ... Av. xʷara- ‘wound’ (Walde-P. 2.529), with orig. sense of root ‘sting, cut’(?). W. Krogmann, KZ 59.204 ... Otherwise Falk-Torp 1214.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. sword\", \"stance\": \"partial\",\n    \"note\": \"Skeat likewise connects the word with a base meaning ‘to hurt, wound’ (cf. OHG sweran), i.e. the same traditional analysis as Klein and Watkins.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\",\n \"words\": \"sword\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English sword continues Old English sweord (with West Midland variant sword beside the more usual ME swerd), from Proto-West Germanic *swerd, Proto-Germanic *swerdą; the modern spelling with -o- is the West Midland form generalised, and the w of the cluster sw- before a back vowel was lost in pronunciation in the 15th-16th c. (compare 'two', 'answer'), leaving the silent w. Cognates: OS/OFris. swerd, ON sverð, Du. zwaard, OHG swert > German Schwert. Whether the Germanic noun goes back to *swer- 'cut' is the question raised at node #5; the Old English > Modern English link itself is beyond doubt.\",\n \"derivation_fa\": \"واژهٔ انگلیسی sword دنبالهٔ sweord انگلیسی کهن است (گونهٔ ویست‌میدلندی sword در کنار swerd رایج‌تر انگلیسی میانه)، از *swerd ژرمنی غربی آغازین و *swerdą ژرمنی آغازین. املای امروزی با -o- همان گونهٔ ویست‌میدلندی است که عمومیت یافت، و w در خوشهٔ sw- پیش از واکهٔ پسین در سده‌های پانزدهم و شانزدهم در تلفظ افتاد (مانند two و answer) و تنها در نوشتار ماند. هم‌ریشه‌ها: swerd ساکسونی و فریزی کهن، sverð نورس کهن، zwaard هلندی و swert آلمانی کهن (Schwert امروزی). اینکه خودِ نام ژرمنی از *swer- «بریدن» آمده باشد پرسشی است که در گرهٔ ۵ بررسی شد؛ ولی پیوند «انگلیسی کهن ← انگلیسی نو» جای هیچ تردیدی ندارد.\",\n \"sources\": [W_SWORD],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); checked against Klein p.1553-1554 and Wiktionary instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. sword (KLN_1966.txt line 37760)\", \"stance\": \"supports\",\n    \"note\": \"'sword, n. — ME. swerd, fr. OE. sweord, swurd, sword, rel. to OS., OFris. swerd, ON. sverd, Dan. sverd, Swed. svärd, MDu. swaert, Du. zwaard, OHG., MHG. swert, G. Schwert.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat / Wiktionary s.v. sword\", \"stance\": \"supports\",\n    \"note\": \"Wiktionary: 'Inherited from West Midland Middle English sword (swerd in most dialects), from Old English sweord, from Proto-West Germanic *swerd, from Proto-Germanic *swerdą.'\"}\n ]\n})\n\ndoc[\"entries\"].append(e1)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-492.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc,f,ensure_ascii=False,indent=2)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-492.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-492.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 492"
}
```


### [2026-09-14T03:28:23.046Z] TOOL RESULT

```
written
JSON OK
nodes verified: 14/14
node verdicts: {'plausible': 6, 'confirmed': 7, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'partial': 6, 'contradicts': 1, 'not_checked': 3}
books consulted: {'supports': 24, 'partial': 8, 'silent': 5, 'contradicts': 2} | by book: {'CHEUNG': 4, 'SYN': 4, 'MON': 4, 'KLN': 4, 'POK': 3, 'WEB': 3, 'WLD': 3, 'BRT': 2, 'PHD': 2, 'HRN': 2, 'SKT': 2, 'IEC': 1, 'NYB': 1, 'SOD': 1, 'ARY': 1, 'HUB': 1, 'BQT': 1}
```


## [2026-09-14T03:28:29.343Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i -A6 \"^SWORD\" SKT.txt | head -30"
}
```


### [2026-09-14T03:28:29.405Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:28:31.758Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Sword\\|sword,\" SKT.txt | head -10"
}
```


### [2026-09-14T03:28:31.826Z] TOOL RESULT

```
1781:Bill  (1),  a  chopper,  swoni, M.£.  M/,   sword,  axe;   Hk^   bIrdV
6876:FoiblO;  see  Feeble Foil  (iX   to  defeat    (T.  -  L^ jfpf  ^,  to  trample  ondei  (ooL  *  <  ' to  trwBple  OQ,  also  to  oppre:-- ciiarge  cxtiemdy  <Cot.).*Low  L* yWarc,  to  fall  cloth  ;   kce  Full  (3)^ frii»  a  bloni sword,  so  called  beovsc or  blunted  ;  faii,  a  defeat Foil  (2).  a  set-off;  sec  FoUa^O; Foin,  to  thrust  with  a  swprd.  (F.-L Ob&otcte.     Lit    *io    ihrast   with  an  «e] spcxr.*  — O.  F.  /pHi'mtt    an   oel-spcai.»I fuscima,  a  trident Foison :  see  Fnae  (i  \ Foist,  to  intrade  siirrcplitioakly    (O. O.  Du.  vystcH,  *  to  fiule,'  t.e.  to  break notscleA«iy,  which  is  also  the  orig. ffiitt;  allied    to   O.    Da.  wtst,    'a   fiak ^Sewel).      So  aUo  Dan.  /u,   the fiomJire,  to  fixi ;  see  Fiaa. Fold(i),to  '       ■    -      ■'■-'     '^ JoUen,  A,  S +  Dan.  faiiie,    :    ._.   , falda,  Goih.yii;/Adtf,  yj.fixi.'tn, Gk.  vA^cetv,  to  weave.    (^  PLAK.) foiJ^  sb.,  a  plait;  -ftU^  >offtiL.  u
7625:claymore,  a  Scottish  bfosflsword. ^GaeL)  Gael.  c'aUMtamk  mcr.  n  jjteil sword.  Here  ciaidheamh  is  cognate  wtili W.  deddyf^  cUddru,  a  sword,  and  with  L glAiiut  The  Gael.  mar.  great,  is  alUfld lo  W.  mawr,  L.  magnus,  great.
12622:Odd.  not  even,  strange.  (Scand.)  II nYt/f.  — Iccl.  oddt\  a  tn.ingle,  a  pcsBt l.ind  ;  melaphoricaUy  (fiom  tbe  tnaa|| an  odd  number  (orig.  thru)  ;  henot  aliiA phr.  sfandatk  t  odJa,  to  stand  (or  bet odds,  to  quarrel ;  oddamt^r,  the  od^  n third  man  who  gives  a  casting  voC^^ tala,  an  odd  number.  Alliro  to  «^ |ioint  of  a  weapon  (put  for  *nrflr*).+A ord,  point  of  a  sword,  point ;  Du.  m point,  Swed.  udda,  odd.  udd*^  a  neirt:! »ri,  a  place.  M.  H.G.  ort. (^  WAS.  to  cut) Ode.  a  song.  (F.-L-Gk.)  F. L.  9da,  odt,  —  Gk.  o^,  n  soni; ;  for song.  —  Gk.  dffSciK,  to  sing.  Allied  to: vad,  to  speak.     W  WAD.)
17920:expatiate.  (L.^  From  pp.  of  L. exfatiari^  better  txspatiari,  to  wander.— L.  tXt  out ;  sfatiari,  to  roam,  from spaiium^  spnce. Spade.  (E.)  A.  S.  spadu,  spada^  a  spade. +  Dq.  sptuie^  IceL  spdHi,  Dnn  Swed. spade,  G.  spatt,  spattn;  Gk.  ffvd^,  liro.-id blade,  sword-blade,  spathc  of  a  flower (whence  L.  spatha,  F.  ///f).  From  its flat  surface.  (^SFA,  to  draw  out.)  Der. spaddlt,  a  paddle:  spadiUe,  ace  of  spades. 1-.  spadilU,  Span,  espadiifa,  small  sword, ace  of  spades,  dimin.  of  Span,  tpada^  a spade  ( ■  L.  spatha  =  Gk.  erirafli;),
18523:FC  Uuht.  A.  S.  j/iV/.  a  pricking ikaiion.  —  A.  S.  ttician,  to  prick,  pierce. RACCodo.fitoooata,  athnist  in  fencing. ||.  w  Tcul.)  Stoicado  is  an  accnmmo- pij  form,  as  if  it  urere  Snanish.—  Ilal. Ird/a,  *a  foyne,  thrust,'  rlorio.  —  llal. |r#,  *a  fhort  sword,  a  tuck,*  Monri; b  pp.  suffix  -ata.  —  G.  f/A->(,  a  stick, IT,  tnuik,  ttump;  cognate  with  M,.  atook
```


## [2026-09-14T03:28:35.780Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sweord\\|Schwert\" SKT.txt | head -10"
}
```


### [2026-09-14T03:28:35.843Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:28:44.544Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt; do echo \"-- $f\"; grep -n \"sweord\" $f | head -3; done"
}
```


### [2026-09-14T03:28:45.588Z] TOOL RESULT

```
-- FSD_vol1.txt
-- FSD_vol2.txt
-- FSD_vol3.txt
-- FSD_vol4.txt
-- WEB_vol1.txt
```


## [2026-09-14T03:28:48.585Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in FSD_vol4.txt FSD_vol3.txt; do echo \"-- $f\"; head -3 $f; grep -c \"sword\" $f; done; echo; grep -n \"AS. sweord\\|A.S. sweord\\|swurd\" FSD_vol*.txt WEB_vol1.txt | head"
}
```


### [2026-09-14T03:28:49.859Z] TOOL RESULT

```
-- FSD_vol4.txt
GOVT.  COLLEGE,  LIBRfiRY
KOTA  (Raj.)
Students  can  retain  library  books  only  for  two weeks  at  the  most.
151
-- FSD_vol3.txt
FUNK & WAGNALLS
New Standard Dictionary
(Re» U S P»t (Iff ) •
61
```


## [2026-09-14T03:28:57.190Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\np='data/verification/page-492.json'\nd=json.load(open(p,encoding='utf-8'))\ne1=d['entries'][1]\nfor n in e1['nodes']:\n    for c in n['consulted']:\n        if c['src']=='SKT':\n            c['where']=\"SKT.txt s.v. sword (entry not recoverable)\"\n            c['stance']=\"silent\"\n            c['note']=\"greps of the local Skeat OCR for 'sweord', 'Schwert' and a 'Sword' headword return nothing — the relevant columns of the scan are too degraded, so Skeat could not be consulted for this word.\"\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)\nprint('patched')\nEOF\npython3 -m json.tool data/verification/page-492.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 492"
}
```


### [2026-09-14T03:28:58.375Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 14/14
node verdicts: {'plausible': 6, 'confirmed': 7, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'partial': 6, 'contradicts': 1, 'not_checked': 3}
books consulted: {'supports': 23, 'partial': 7, 'silent': 7, 'contradicts': 2} | by book: {'CHEUNG': 4, 'SYN': 4, 'MON': 4, 'KLN': 4, 'POK': 3, 'WEB': 3, 'WLD': 3, 'BRT': 2, 'PHD': 2, 'HRN': 2, 'SKT': 2, 'IEC': 1, 'NYB': 1, 'SOD': 1, 'ARY': 1, 'HUB': 1, 'BQT': 1}
```


## [2026-09-14T03:29:23.021Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-492.json` written; `verify_check.py 492` reports **0 PROBLEM lines** (14/14 nodes).

**PDF page 492 (book p. 462) — roots Swep/Sup 1 and Swer** (2 redirects skipped)

- Root verdicts: confirmed 2 (POK:1048 and POK:1050 + IEC:1348 are both exact page hits; Nourai's Swer gloss "to press, cut, hurt" is Klein's wording at KLN:1554).
- Node verdicts: confirmed 7, plausible 6, disputed 1.

Disputed:
- **Swer / خوره xoreh** — Mann (IEC 1348) really does put it under *swer- ("Per. xware 'gangrene; leprosy?'"), so Nourai cites correctly, but he stands alone: Mo'in ("آنچه که چیزی را بخورد و از میان برد") and Wiktionary derive it from خور-، present stem of خوردن + ـه. The chart's own NOTE (MON:1455) is the modern view.

Notable partials/contradictions (kept as `plausible`):
- **HUB:56 contradicts the node that cites it**: Hübschmann, Persische Studien p. 56 ad Horn 488 says "Ich trenne xafj 'ephialtes' von xuspidan 'schlafen'" — i.e. the page Nourai cites for خفج explicitly denies that link. Also بختک is not derivable from خفتک in any modern source.
- **Av. xvara "thorn, to pierce"** (Swer #1): every source (POK 1050, WLD II 529, KLN 1554, IEC 1348, MacKenzie's "2xwar … a degree of sin") glosses it 'wound'. Nodes #1 and #3 are the same Avestan lexeme entered twice.
- **خلیدن/خله ← Av. xvara**: Horn p.109 no. 492 derives خله from Av. hareθi- and only records de Lagarde's *wish* to compare xᵛara-; Hübschmann rejects Horn's version without adopting it; Cheung has no such verb root. خلبان < خله‌بان 'oarsman' is confirmed (Mo'in, Wiktionary).
- **Germanic *swerdam**: Pokorny/Klein/Watkins support it, but WLD II 529 omits it, Buck calls it "etym. dub.", Wiktionary calls the origin disputed (Nikolaev 2015: *seh₂w- 'sharp').
- **Avestan "hufsa"** is not Avestan: it is Gharib's Proto-Iranian *hufsa- (cf. Wikt. PIr *hufsati/*xʷafsati), the source of the Sogdian ʾwβs- of node #3. And "xwafsa" is an inchoative present stem, not a noun 'sleep'.
- **SOD:173** holds xwβn 'sleep, dream' (Gharib no. 4346) but not `wbs (that is no. 1856) — marked partial.
- **Pahlavi xwâb** strictly continues Ir. *hwāpa- (Benveniste/Buck), not xᵛafna- (whose MP reflex is xwamn).

Extraction errors: **none**. I rendered the printed page (pdftoppm 492) and the JSON matches it exactly, including the Persian script boxes and the Nezāmī quote.

Also saved for audit: `data/verification/sources/refs/ocr/FFD/50.vision.txt` (+ 50.png, 51.png) — the FFD p.50–51 scan read by eye, since `ref_page.py FFD:50` reports no scan coverage even though `FFD_asmaneketab.pdf` is on disk (possible `scans` misconfiguration in refs_online.json). 13 web sources archived via fetch_source.py.
