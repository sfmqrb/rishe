# Verification process log — verify-page-453


## [2026-09-14T01:56:18.951Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 453 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-453.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-453.json. Write /home/sfmqrb/git/rishe/data/verification/page-453.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 453` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:19.894Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-14T01:56:20.763Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:20.780Z] TOOL RESULT

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


## [2026-09-14T01:56:21.256Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-453.txt"
}
```


### [2026-09-14T01:56:21.278Z] TOOL RESULT

```
1	=== PDF page 453 (book page 423) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Skel 1 : bent, curved  (refs POK:928)
4	#1 (parent #0) [Persian] refs=HRN:175; BQT:1288 | šal 1 «شَل ۱» : leg, thigh ; šalvâr «شلوار» : "like legs", pants ☞Wel 3 ; šelang «شلنگ» : step, also a leg exercise ; šalpǔy «شلپوی» : sound from foot steps | extra: شکپوی، شگپوی
5	#2 (parent #0) [Greek] refs=POK:928 | skelos : leg
6	  #3 (parent #2) [English] refs=AHD | isosceles
7	#4 (parent #0) [Greek] refs=WLD:597; OEW:363 | skhelos, kellos : crooked
8	  #5 (parent #4) [Persian] refs=WLD:597; HRN:192; MON:3012 | kol «کَل» : crooked
9	#6 (parent #0) [Greek] refs=POK:928; AHD | kulindein : bend, roll up
10	  #7 (parent #6) [French] refs=None | 
11	    #8 (parent #7) [Persian] refs=MON | sîlandr «سیلندر» : cylinder
12	    #9 (parent #7) [English] refs=AHD | cylinder, calender
13	#10 (parent #0) [Greek] refs=AHD | kôlon : limb, part, member, large intestine
14	  #11 (parent #10) [Arabic] refs=TAD:59 | 
15	    #12 (parent #11) [Persian] refs=MON:2749; BQT:1548; ETM:45 | qǔlǔn «قولون» | extra: قولنج ، کولنج
16	  #13 (parent #10) [Latin] refs=AHD | 
17	    #14 (parent #13) [English] refs=AHD | colon, semicolon
18	--- entry 1 ---
19	ROOT Skel 2 -> redirect to Sek
20	--- entry 2 ---
21	ROOT Skend -> redirect to Skand
22	--- entry 3 ---
23	ROOT [Indo-European] Skeng : crooked, bent  (refs POK:930)
24	#1 (parent #0) [Avestan] refs=POK:930 | haxti : that which bends, leg, shank
25	  #2 (parent #1) [Pahlavi] refs=SNS:2 | haxt : thigh
26	    #3 (parent #2) [Persian] refs=HRN:279 | hax «هَخ» : foot sole (obsolete)
27	#4 (parent #0) [Sanskrit] refs=POK:930; SNS:2 | sâkthi : leg, shank
28	#5 (parent #0) [Germanic] refs=POK:930; AHD | skankô : that which bends, leg
29	  #6 (parent #5) [English] refs=AHD | shank
30	
```


## [2026-09-14T01:56:22.644Z] AGENT

I'll start by reading the source JSON and supporting infrastructure files.


## [2026-09-14T01:56:24.051Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-453.json",
 "description": "Read source JSON for page 453"
}
```


### [2026-09-14T01:56:24.088Z] TOOL RESULT

```
{
  "pdf_page": 453,
  "book_page": 423,
  "entries": [
    {
      "root": {
        "name": "Skel 1",
        "lang": "Indo-European",
        "refs": "POK:928",
        "gloss": "bent, curved"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "HRN:175; BQT:1288",
          "words": [
            {"translit": "šal 1", "gloss": "leg, thigh", "script": "شَل ۱"},
            {"translit": "šalvâr", "gloss": "\"like legs\", pants", "script": "شلوار", "see": ["Wel 3"]},
            {"translit": "šelang", "gloss": "step, also a leg exercise", "script": "شلنگ"},
            {"translit": "šalpǔy", "gloss": "sound from foot steps", "script": "شلپوی"}
          ],
          "script_extra": "شکپوی، شگپوی",
          "note": null,
          "quote": {
            "text": "توانگر بنزدیک زن خفته بود ـ زن از خواب شلپوی مردی شنود",
            "poet": "Bǔshakǔr Balkhî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:928",
          "words": [
            {"translit": "skelos", "gloss": "leg", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "isosceles", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "WLD:597; OEW:363",
          "words": [
            {"translit": "skhelos, kellos", "gloss": "crooked", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "WLD:597; HRN:192; MON:3012",
          "words": [
            {"translit": "kol", "gloss": "crooked", "script": "کَل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:928; AHD",
          "words": [
            {"translit": "kulindein", "gloss": "bend, roll up", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "sîlandr", "gloss": "cylinder", "script": "سیلندر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "cylinder, calender", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "kôlon", "gloss": "limb, part, member, large intestine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Arabic",
          "refs": "TAD:59",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "MON:2749; BQT:1548; ETM:45",
          "words": [
            {"translit": "qǔlǔn", "gloss": null, "script": "قولون"}
          ],
          "script_extra": "قولنج ، کولنج",
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 10,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
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
            {"translit": "colon, semicolon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Skel 2",
        "redirect": "Sek"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Skend",
        "redirect": "Skand"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Skeng",
        "lang": "Indo-European",
        "refs": "POK:930",
        "gloss": "crooked, bent"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:930",
          "words": [
            {"translit": "haxti", "gloss": "that which bends, leg, shank", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:2",
          "words": [
            {"translit": "haxt", "gloss": "thigh", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:279",
          "words": [
            {"translit": "hax", "gloss": "foot sole (obsolete)", "script": "هَخ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:930; SNS:2",
          "words": [
            {"translit": "sâkthi", "gloss": "leg, shank", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "POK:930; AHD",
          "words": [
            {"translit": "skankô", "gloss": "that which bends, leg", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "shank", "gloss": null, "script": null}
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


## [2026-09-14T01:56:24.808Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:56:24.884Z] TOOL RESULT

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


## [2026-09-14T01:56:27.154Z] AGENT

Now let me check the reference infrastructure and start looking up Pokorny.


## [2026-09-14T01:56:30.363Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','HRN','BQT','MON','TAD','SNS','OEW','ETM','IEC','SYN','KLN','SKT','BRT','PHD','NYB','ARY','PLA','AFM','FVQ','LKT','DEV','PHN','FSD','WEB','LEW','LAT','CHEUNG','HUB','RCH']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:600]); print()\n    else: print(k,'MISSING'); print()\n\""
}
```


### [2026-09-14T01:56:31.544Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

CHEUNG MISSING

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =
```


## [2026-09-14T01:56:36.338Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\nprint('---WLD'); print(d['WLD'].get('page_offset')); print(d['WLD'].get('lookup_hint'))\nprint('---TAD'); print(d['TAD'].get('page_offset')); print(d['TAD'].get('lookup_hint'))\nprint('---SNS'); print(d['SNS'].get('page_offset'))\nprint('---HRN'); print(d['HRN'].get('lookup_hint'))\nprint('---MON'); print(json.dumps(d['MON'],ensure_ascii=False))\n\""
}
```


### [2026-09-14T01:56:37.662Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
---WLD
Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
---TAD
86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
---SNS
242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
---HRN
Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
---MON
{"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"], "page_offset": null, "covers_etymology": true, "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).", "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"}
```


## [2026-09-14T01:56:40.617Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: \\(s\\)\\?kel\" POK_full.txt | head -40; echo ===; grep -n \"lemma: skeng\\|lemma: (s)keng\\|keng\" POK_full.txt | head -20"
}
```


### [2026-09-14T01:56:40.675Z] TOOL RESULT

```
Exit code 1
44616:Root / lemma: kelg- 
44630:Root / lemma: kel-1, kela- 
44697:Root / lemma: kel-2 
44745:Root / lemma: kel-3, kela-, A/a- extended klad- 
44927:Root / lemma: kel-5 
44963:Root / lemma: kel-6, k(e)le-, k(e)la-or 1(1-1 
45077:Root / lemma: kel-7{kol-, kj^ 
45105:Root / lemma: kel-7 
45113:Root / lemma: kelp-, l^lp- 
47147:Root / lemma: kel-, kol-, kal- 
93753:Root / lemma: keleu- 
(eval):1: == not found
```


## [2026-09-14T01:56:41.868Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 928\\|Page(s): 927-928\\|Page(s): 928-929\\|Page(s): 930\\|Page(s): 929-930\\|Page(s): 930-931\" POK_full.txt | head -20"
}
```


### [2026-09-14T01:56:41.975Z] TOOL RESULT

```
75440:Page(s): 928 
75455:Page(s): 930 
75493:Page(s): 929-930 
75527:Page(s): 930 
75542:Page(s): 930 
77326:Page(s): 930-933 
77873:Page(s): 928
```


## [2026-09-14T01:56:44.034Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '75400,75560p' POK_full.txt; echo '=====77873 region'; sed -n '77840,77890p' POK_full.txt"
}
```


### [2026-09-14T01:56:44.181Z] TOOL RESULT

```
base' (Frisl< iF. 49, 99 f.); about kAovk; " coccyx, smaii triangular bone at the base of the 
spinal column ' see above S. 608; 

alb. /5/7a/e"lame' {*skelno-)\ 

Maybe alb. shale^ thigh ' : gkeAo^ m. " thigh '. 

Note: 

common k- > sk- > s- kentum > satem. 

Latin scelus, -e/75 "malice, Verruchtheit, crime ' (formal = OKsAog); coluber, -brfsuake' 
("sich windend', *kelo-6!"ro-, *kolo-6'^ro-)\ calx {see be\ow); 

Old High German (with formants -ko-) scelah {*skelha-) "slant, skew, crooked'. Modern 
High German scheel{Dev\orr\. Middle High German schilhen. Modern High German 
schlelen). Old English sceolhds., Old Icelandic (m. gramm. variation) skjalgr {*skelk6-) 
"slant, skew, scheelaugig'; isl. 5/r^// "schiefer mouth'. Old Icelandic skaela s//r "den Mund 
verziehen'; with labiales extension: Old Icelandic sA/a//^ "tremble, quiver' = Old English 
sclelfan6s., engl. /o 5/7e/Ke "abschiJssigsein', Old Icelandic skjalfr, s/re//^"trembling'?; 

without aniaut. s-: Balto Slavic *ka!id {*kolJd) "lehne an' in Lithuanian at-si-kaltr s\dc\ 
aniehnen', a/-/r5/as "angelehnf; to Balto Slavic *klana-'(r\. {*kl9-no-) "leaning, tendency' in 
Lithuanian /r/a/7as "puddle, slop', ablaut, klonism. "valley' {*kla-ni-), /r/c»/7e "lowland, 
depression'; with Indo Germanic a Lithuanian kluonas, Latvian kluons m. "Dreschtenne'; in 
addition further above S. 509 *kla- "hinlegen'; 

with Balto Slavic -ul-= Latin -al- (Indie -ol[9-]) with /^-suffix: Lithuanian kulse, /r^/s/s "hip, 
haunch' (with /r-insertion: kulksis, kulksn/s ^ank\e, Sprunggelenk'), Old Prussian culczr\r\\p, 
haunch'; with -/r-suffix: Lithuanian kulnasm., kuln/st "hack, mattock, hoe, calcaneus ' 
{*kulk-n-), proto Slavic. *kulkai. "hip, haunch' in spatChurch Slavic A/b/ra"poples', bg. 
/rb7/ra"hip, haunch, thigh' (/5-/rb/cb"verrenke'); Serbo-Croatian kuk6s. etc.; 

Latin ca/v "calcaneus ' {calco, -SAe "tread, stomp', calcltrare^y\o\ev\\. ausschlagen', calcar 
" spur', calceus^ shoe ', tarent. kqAtIov ds. from Oscan *calc-tlo-)\ after Trautmann 145 
Indo Germanic root nouns *Aro/fr- besides koIR-. 



References: WP. II 597 ff., WH. 1144 f., 248, II 492, Trautmann 114, 135 f., 145. 
Page(s): 928 

Root / lemma: skend^- 

Meaning: to plunge 

Note: only gr. and Baltic 

Material: Gr. okivGoc; "untertauchend'; Lithuanian sk^stu, 5/r#5//"untersinken, drown ', 

causative skandinu, -dinti^ drown '; Old Prussian auskiendlai^er qo under'. 

Maybe alb. {^skendh-) /7eo'/7 'plunge, throw' [common alb. sk- > h-]. 

References: WP. II 565, Trautmann 265. 
Page(s): 930 

Root / lemma: (s)ken-(d-) 

Meaning: to rift; to flay 

Note: probably extension from seAr-'cut, clip'; only Celtic under german. 

Material: A. Bret, s/ra/?/ collective "Schuppen' {*sknto-), abret. anscantocionP\. 

"insquamosos', cymr. ys^y/^/i/'Schnitzen' {* sken-tr-)\ 

Old Icelandic skinnu. "skin, fell, fur' {*sken-to-, proto Germanic *skinl=>a-, compare lapp. 
loanword sk/dde and runisch ski[n]t^a-leubaR, Old English scinn, (under the influence of 
common Celtic -ns-, -nt- > -nn-), engl. sk/n6s. is loanword from Nord., also Middle Low 
German schin^a kind of russisches Ledergeld'), Middle High German schinti. " fruit bowl ', 
Modern High German Schind-mahre, -aas, Dutch dial. sch/nde'sk\n, fell, fur; bast, bark', 
abgel. verb Old Saxon b/sc/nd/an ^abnnden, peel ', Old High German scinten. Middle High 
German Middle Low Germansc/7/>7o'e/7"enthauten, auspliJndern, maltreat' (Modern High 
German sch/nden stem V.); Old Icelandic skant " bark ', nisi, also 'Hautchen', Middle Low 
German sc/7//7 'dandruff in Haar' (out of it Modern High German Schinn, Schinne), (under 
the influence of common Celtic -ns-, -nt- > -nn-), Middle Dutch sc/7e/7e"thin skin, bast'; 

B. besides Indo Germanic (s)kend-\n. 

Old Irish ceinn' scale, husk, bowl', cymr. cenn{*kend-n-), acorn, cenn-en Hautchen, 
skin', ys^e/7/7'Schinnen', Middle Breton quenn^sV\v\\ bret. kennm. "Schinnen', -/re/7 "skin' 
in /?^-^e/7"Rindshaut' etc.; bret. (Vannes) sk/gnanlrog' {*skenniano-); Old Icelandic hinna 
f. "thin skin. Membrane' {*skend-n-); (under the influence of common Celtic -ns-, -nt- > -nn- 

)■ 



compare with a-vocalism: Middle Irish sca/ndr/m 'zerspa\\.e\ scandrad, scaindred 
"dispersion", scainder^Qeiec\\\!. 

References: WP. II 563 f.; Loth RC. 41, 405 f. 
Page(s): 929-930 

Root / lemma: (s)keng- 

Meaning: lame; slant 

Material: Old Indie sakthi- n. (= Avestan haxti-) " thigh ' ( *skak-thi-, Indo Germanic *skng-ti- 

; das -th'h after Old Indie asth'h "bone', above S. 783); /r/75/ya//"hinkt' (Middle Indie for 

*skanj-), /r/75/^5-"hinkend', khanjana^m. " wagtail '; 

gr. OKa^oj (only present and Imp.) " limp ' {*skng^id)\ Middle Irish 5C//7^//77 "spring' is 
probably reshuffling from Old Irish sce/7o'- "spring' (see be\o\N ghengh-^ march, step, 
stride, strut'); 

Old Icelandic s/r5AAr"hinkend, slant, skew', Swedish dial, sk/nka' limp '; without ani. s-: 
Old High German hinkan^ limp ', Denomin. Middle High German hanken6s.\ 

Germanic *skanka-\n Norwegian skonk, skanki. " thigh, shinbone'. Old English scanca 
f. " shank, leg, shin bone ', Middle Low German schenke^ thigh ' (Demin. Middle High 
German Modern High German SchenkeF thigh '), ablaut. Old High German scinker thigh 
', scinchorw., scincai. "Beinrohre, thigh ', Modern High German Schinken, on the other 
hand Old Frisian skunka. Modern High German Dialectal schunke {* skng-) ds.; without s- 
Middle High German hanke' thigh, hip, haunch', Tirol HenkeF thigh '; also Late Middle 
High German schankm. " rack, cupboard for Trinkgerate' and Old Saxon skenkjan 
"einschenken' (from "das vessel schief halten'). Old High German scenkan6s., Middle 
High German schenken6s., also "give' Modern High German schenken, in addition 
postverbal Middle High German schanc\esse\ from = Geschenkt wird' and "gift'; 

a Germanic root skeh- in Old Icelandic s/radr "slant, skew'. Middle High German scheehe 
" squinting' etc. 

References: WP. II 564 f., F. Sommer Festschr. Debrunner425 ff. 
Page(s): 930 

Root / lemma: (s)kep-1 

Meaning: to cover 

Note: only gr. and Balto-Slavic 



Material: Gr. oKsnaq, -aoq n. 'cover, sleeve, wrapping, shelter', Ionian Attic aKsirn f. 
"cover, protection, shelter', OKsna^u), GKETrau), OKsnu) "bedecke, verhijlle, schijtze'; 
Lithuanian kepure^U\j{ze\ Latvian cepure ^Mutze, hat; Bedeckung the Kornhaufen auf 
dem Felde', russ. cepec' bonnet' etc. 
References: WP. II 559. 
Page(s): 930 

Root / lemma: (s)kert)(h)-, (s)kreb(h)-, nasalized (s)kremb- 

Meaning: to turn, curve 

Note: extension to (s)ker-\uxn' (see also sker-^ shrivel, shrink due to excess dryness, 

wrinkle up ') 

Material: Gr. Kap(po(; n. "dry deadwood, chaff' ( *kfd^-), Kopcpn f. " dry wood, hay', Kopcpu) " 

allow to shrivel, shrink due to excess dryness, wrinkle up, desiccate ', KapcpaAsoq "dry, 

hoarse', KopcpuvsaGai ^npa'vsoGai. cpGEipsaGai () Hes.; Kpappoq "eingeschrumpft, arid, 

dry', KpaiJpn f. " cabbage ', KpaMpaA£0(; "dry, roasted', Kpoppow "roast, roast' (assim. from 

*Kpaij(36u)); 
=====77873 region
slakstau, -y//"mehrfach spritzen, sprinkle ', slaku, -e//"drip, trickle', slekili, s/ekt/" spray' , 
Latvian 5/a/ra "Anfeuchtung', 5/ac/7"naftmachen, sprinkle, fine rain'. 

References: WP. II 602 f., 705; 

See also: compare also sresk- "drip'? 

Page(s): 957 

Root / lemma: (sj/ca/o-s 

Meaning: a large fish 

Note: or rather /cra/o-s? 

Material: Latin squalus^e'xu grofterer Meerfisch'; das 5- could but previously secondary 

from squatus ds., squama^ scale, husk ' attributed sein; 

Old Icelandic hvalrm. (besides -hveliu.) "whale' (/-stem). Old English hwael, engl. 
whale. Old Saxon Old High German hwalds., besides Old High German hwelira 
(Germanic *hvali-s-dn-). Modern High German Waller, i/Velleran6 Middle High German 
'H/e/s'(Germanic *hvali-s), wherefore also Old Prussian /ra/zis "Wels'; the mythische fish 
Avestan kora- is die Iran. Wiedergabe eines urmordwin. */ro/5 "fish', later kal, to tscherem. 
kol, lapp. guole, Finnish kalaetc; die ganze family also probably finno-ugr. origin. 

References: WP. II 541, WH. II 581 f.. Hoops, Engl. Stud. 28, 1 ff., Jacobsohn, Arierand 
Ugrofinnen 241 f. 
Page(s): 958 

Root / lemma: (s)k''el-5, (s)kel- 
Meaning: " sound, shout ' 
See also: see above S. 550 {kel-). 
Page(s): 928 



Root / lemma: (s)k''er- 

Meaning: ' make ' 

See also: see above S. 641 f. {k^er-). 

Page(s): 947 



Root / lemma: slak- 

Meaning: to hit, hammer
```


## [2026-09-14T01:56:48.129Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=75280 && NR<=75450' POK_full.txt | head -80"
}
```


### [2026-09-14T01:56:49.215Z] TOOL RESULT

```
Lithuanian kalpa^ transom am sled ', /r/ZyOa'Steigbugel, loop, noose, snare ', kilplnis 
'Armbrust', Old Prussian /ra/p^s 'Rungenstock'; 

Lithuanian sklemplu, sklemptr smooth behauen, polish'. 

root extension skel(e)-b-: 

Old Icelandic skalpr^s\\\^\ Danish dial. 5/ra//0 'Samenschote, husk'. Middle Low German 
schuipe, scholpe^ shell, scale, husk ', Danish skulp, skulpe^ pod, Fruchtbalg', Norwegian 
skolp^ pod, husk', engl. skalp{v\or6. loanword) 'cranium, skull'. Old Icelandic skelpai. 
'Grimasse', skolpr^ chisel '; Old Church Slavic sklablfl sg ^ 6en Mund aufmachen, smile ', 
Czech skleb 'Zahnefletschen'; 

/■extension: sk/e/-, sklei-d-, sklei-k-, sklei-p-: 



Old Icelandic s/Tta'tear, destroy, verbringen' {s//tna \ntr. "rump!'), Old English s/ftan 
"tear', Old Saxon s//?a/7"schleiR)en, split'. Old High German s//z5/7 "split, rend, 
aufbrauchen'. Modern High German versch/e/73en, schleilien. Old Icelandic s///"slit, crack, 
AbniJtzung', Old English ges//t'6as Bersten', Old High German s//z, Modern High German 
Schlitz, Middle High German sleize. Modern High German Sc/7/e/Z?e"Leuchtspan'; Old 
Icelandic sITdrari. PI., slTdrc\. PI. "sword- or Messerscheide' as *s(k)lei-tro-, -tra-irom the 
unerweit. root form sk/e/-, 

Lithuanian skleidziu, skleTsti, Latvian sk//esf' outspread, umblattern', Lithuanian 
sklaidau, -y//"hin and her blattern', refl. "sich scatter', /s-sk/a/dyt/" scatter, vertreiben', skl/st/ 
"auseinanderflieften'; Lithuanian s/r/a/io'^5 "zerstreuf, Latvian sk/a/d/s ^ e\r\ Herumtreiber, 
good for nothing, useless person'; without aniaut. s-: klaMt^s\c\\ herumtreiben', kli'stu, 
klfdu, k/fst'err', Lithuanian klystu, klydau, klysti^s\ch verirren' (without d. Lithuanian klajdju, 
-otr wander', Latvian klaijat, -udt6s. eineoriginally versch. family?); Old Prussian sc/a/f, 
schlait, schk/a/t' but; without', schklaitsMv. "sonderlich, particularly, specially, especially, 
particular: in particular, peculiarly, separately, extra, notably; otherwise ', Adj. 
"unsophisticated, simple, just'; 

Old English 5//7&/7"spleiR)en', engl. slive. Old English /c-s/^/&/7 "split'. Middle Low 
German slef, Norwegian 5/e/V "large spoon'. 

References: WP. II 590 f., WH. I 165, II 536 f., Trautmann 264. 
Page(s): 923-927 

Root / lemma: (s)kel-2 

Meaning: to be guilty, to owe 

Note: only Germanic and balto-Slavic 

Material: Gothic skulan. Old Icelandic skulu. Old English sculan. Old High German scolan 

"schuldig sein, miJssen, sollen', newer also solan. Modern High German sollen. Old 

English scy/di. "blame'. Old High German Old Icelandic sku/dds.; Gothic sku/am. 

"Schuldner'; 

Old Lithuanian ske/u ar\d Lithuanian skeliu, -e//"schuldig sein', skylu, {*sk/7u), s/r////"in 
Schulden geraten', s/ro/a "blame'; Old Prussian 5/re//5/7/s "culpable', ablaut. skallTsnant 
Akk. " obligation ', poskuITt {paskollet} "ermahnen'; 

without 5-.' Lithuanian /ra/Ze "blame', /ra/Zas "culpable'. 

References: WP. II 596, Trautmann 264 f.; 



See also: compare (s)kel-47 
Page(s): 927 



Root / lemma: (s)kel-3 
Meaning: to dry out 

Material: Gr. gksAAu) 'trockne from, desiccate ' (trans., Fut. gksAu), Aor. soKnAa; intr. Aor. 
eoKAnv, Perf. EOKAriKa), aKzKz^bo, 'ausgetrocknet', m. "Skeletf, n. 'Mumie', OKAripoq "dry, 
hard, rough, unbeugsam', aK£Ai(pp6(; 'ausgetrocknet, abgemagert', aKAr|cpp6(; 'small and 
agile', a-aKsAnc; 1. 'ohneWiderstandskraft' (without OKAripOTric;); 2. 'unablassig, of rage, 
fury, of Weinen' (actually 'unversieglich'); nEpi-OKEAng 'very dry, brittle, hartnackig', nspi- 
qkeAeiq f. ' stubbornness ';
```


## [2026-09-14T01:56:52.651Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=75340 && NR<=75410' POK_full.txt"
}
```


### [2026-09-14T01:56:53.601Z] TOOL RESULT

```
without 5-.' Lithuanian /ra/Ze "blame', /ra/Zas "culpable'. 

References: WP. II 596, Trautmann 264 f.; 



See also: compare (s)kel-47 
Page(s): 927 



Root / lemma: (s)kel-3 
Meaning: to dry out 

Material: Gr. gksAAu) 'trockne from, desiccate ' (trans., Fut. gksAu), Aor. soKnAa; intr. Aor. 
eoKAnv, Perf. EOKAriKa), aKzKz^bo, 'ausgetrocknet', m. "Skeletf, n. 'Mumie', OKAripoq "dry, 
hard, rough, unbeugsam', aK£Ai(pp6(; 'ausgetrocknet, abgemagert', aKAr|cpp6(; 'small and 
agile', a-aKsAnc; 1. 'ohneWiderstandskraft' (without OKAripOTric;); 2. 'unablassig, of rage, 
fury, of Weinen' (actually 'unversieglich'); nEpi-OKEAng 'very dry, brittle, hartnackig', nspi- 
qkeAeiq f. ' stubbornness '; 
Maybe alb. (sko/-) ho//e'\ean, thin' common alb. sk- > h-. 

Swedish ska/flean, thin, fade, sauerlich'. Low German sc/75/'dry, arid'. Middle Low 
German Middle High German schar schalirom taste; triJb, unclear', scha/n'trub become'. 
Middle English scha/owe'sc\r\a\, faint, languid, shallow, having little depth ', engl. shallow 
(also probably Old English sceald^ shallow, having little depth, not deep'. Low German 
schoir shallow water'); 

without aniaut. s-: Old Icelandic /7a//-^/7"Miftjahr', Old English /7a//-/7ec»/'/'erschrocken'; 
Middle High German hel{-ll-) 'weak', hellec^ tired ', Modern High German helllg la\nt, 
languid, exhausted from thirst ', Middle High German hellegen ^ exhaust, behelllgeii. Low 
German har^vj, lean '; lengthened grade (?) Low German hal, Dutch haar6ry\ Middle 
Dutch /7ae/' ausgetrocknet, arid, schal'; Danish dial. hgelm^sW\\\ Danish helme ^ cease' 
('*languish', originally vor Hitze or thirst); 

Latvian kaiss' lean ', kalstu, Aa/s/'vertrocknen, wilt', kaltet^Ary'. 

References: WP. II 597. 
Page(s): 927 

Root /lemma: ^s^AreM (extended kla-, kid-) 

Meaning: to bend; crooked 

Note: (compare also S. 61 1 f. /ro/a-'spinnen') 

Material: Gr. gksAoc; m. ' thigh ', gkzKxq,, -i5oc; 'Hinterfufl, hip, haunch' (Attic ax£Ai(;), 

aKzKKbc, ' bowlegged', OKohbc, 'crooked; improbus', aKakr\y6c, 'tubercular, slant, skew, 

crooked', OKcbAri^, -'(V^oc, m. 'worm', GKOjAunTEaGai 'crook, hin and her winden', keAAov 

GTpEpAov, TTAayiov Hes., redukt.-grade kuKKoc, ' writhed, crooked, humped, lamed ', kuAAo- 



no5i(jov Beiw. of Hephaistos (*k£A-, *kuA-v6(;), KuAiv5u), -su) "rolle, waize' (Ionian Attic 
kqAivSeu)), KuAivSpoc; "Waize, puiiey, Zyiinder'; kwAov "iimb, member', kwAeq, Attic KU)Ar| 
"Huftl<nochen, ham', KwAnv, -nvoq, kwAeoc; ds., KcbArmJ f. " popiiteus, anl<ie' (to 1. -ap- 
above S. 50 f.); KU)Au)Tr|<;, -ou m. "iizard' ("witli Giiedem versehen'); okAq^cjo 'hocl<e iow, 
base' (Frisl< iF. 49, 99 f.); about kAovk; " coccyx, smaii triangular bone at the base of the 
spinal column ' see above S. 608; 

alb. /5/7a/e"lame' {*skelno-)\ 

Maybe alb. shale^ thigh ' : gkeAo^ m. " thigh '. 

Note: 

common k- > sk- > s- kentum > satem.
```


## [2026-09-14T01:57:26.142Z] AGENT

Now let me grep the local reference library for the key nodes.


## [2026-09-14T01:57:29.320Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN shalwar/shal ===\"; grep -n -i \"salvâr\\|salwâr\\|schalwâr\\|šalvâr\\|salvar\\|shalwar\\|sal(w)\\|schalvar\" HRN.txt | head -20; echo \"=== HRN grep 'sarbâl' ===\"; grep -n -i \"sarbâl\\|sarbal\\|saraval\" HRN.txt | head"
}
```


### [2026-09-14T01:57:29.506Z] TOOL RESULT

```
=== HRN shalwar/shal ===
=== HRN grep 'sarbâl' ===
```


## [2026-09-14T01:57:31.284Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# leaf = printed + 21\nfor p in (175,192,279):\n    leaf=p+21\n    print('==== printed',p,'leaf',leaf,'====')\n    print(pages[leaf][:2600] if leaf<len(pages) else 'OOR')\nEOF"
}
```


### [2026-09-14T01:57:32.376Z] TOOL RESULT

```
412
==== printed 175 leaf 196 ====
- 175 -
in [/skar- dev PI), 'spähen, suchen, durchforschen,
Gegenden durchwandern, Iierumgehen', wa;^. sktlr-an},
sar. /kar-am. Die letzten Bedeutungen könnten auch
auf l/^rförr- (vergl. PW.) führen.
787. sikäften 'spalten', I^raes. sikäfeni i^Pgäf AM. S. 84
Zeile 7).
Ka§. vesköw (Inipt.).
phlv. skaft, y. 10 (29), vergl. patkaftan (AV.);
kurd. sikiwin, biskiwin aufblühen', sikeivf, askavf 'Höhle'
(H.-Sch.). LW. Sikaftm 'abtrennen, lostrennen, köpfen .
Zu gr. (Ty.d7iT(o 'graben, hacken (Nöldeke, münd-
liche Mitteilung). Durch diese schöne Entdeckung
wird die bisher nur für europäisch gehaltene Wurzel
slc^ap' bezw. sk-ah- 'schaben, graben* als indogermanisch
erwiesen. Die Bedeutung graben' ist bei np. käftev^
kämden (No. S:^^) noch erhalten^).
788. H'ikesten 'zerbrechen*, Praes. siken-ew,
aw. \^8caüd'^), scindai/^Urzerhrechen ; phlv. skastan
(Men.).
kurd. LW. sikestin, sikinändin (Causat.); oss. sädfjn,
sätfin 'brechen, bersten, zerbrechen' (221).
ap. *skanamij/ (aus ^skadnämiy)^ 9. Cl.; ai. [/'ched-
'spalten gehört nicht hierher, vergl. Hübschmann,
ZDMG. 38, 424.
sikuften, sikäften aufblühen* s. np. bisköfe (No. 223).
789. sei 'Schenkel', seieng (Sileng) ; vergl. selvär 'Hosen*.
gr. (jxfkog (Justi, Litbl. f. or. Phil. I, 65; aber
nicht gehört hierher arm. srwwÄ 'Schienbeine, Waden*,
srnapan '^vq^ii^^ vergl. Hübschmann, No. 260).
np. selvär ist weit entlehnt, vergl. öa(jäßapa (Photius,
Pollux u. ö.), arab. sarbäl, sarväl, kurd. selvär,
sarval, salval (H.-Sch.), af/. bei. (249) salvär, oss.
salbaro (H. S. 130), wa;^. savdlak, minj. soäl u. s. w.
*J Erst jetzt besteht Feistes kulturgeschichtliche Bemerkung
unter got. skahun (No. 499j zu Recht.
') So setze ich die Wurzel nach Barth olomae, Stadion II, 4,
97, 104 an.
==== printed 192 leaf 213 ====
800. kef \Schaiiin'.
aw. kafa- *SchaunV; phlv. kaf (AV., nicht kef)\ skr.
kapha- 'Schleim'.
kurd. kaf Schaum'; oss. d. /äfä, t. /äf Hotz,
Schleim' (299); bei. kap^) (188); wa/. ;^w/, sar. /^/.
861. kul *krnmm, gekrümmt'-).
Nach Nöldeke (mündliche Mitteilung) zu gv. y.vkhig
*krumm'. Dann vergl. auch gr. xt;(}rog gekrümmt', aw.
skarena- 'rund'. — Fortunatow stellt (BB. 6, 216)
gr. y.vXXog zu skr. kuni- *lahm am Arm' (aus "^kulni-),
862. keläy, kulüy liabe', ixiD (Is. 34, 11, etwa statt ixiD?).
aw. «;ära;72rt- (?) ; phlv. varäy^ varäk.
Das np. k könnte dann eben so wenig ursprünglich
sein wie in kiisüden statt gusciden. Anderenfalls würde
die Zusammenstellung unstatthaft sein. Nöldeke will
daher (mündliche Mitteilung) gr. v.ogai, etc. vergleichen
und auch phlv. rardy, varOk ganz aus dem Spiele
lassen; jüd.-pers. JIXID sei in jNHp zu emendiren, wie
auch das Gazophylacium schreibe (D und p seien
in hebräischen Handschriften oft nicht von einander
zu unterscheiden)-^). Diese Erklärung ist gewiss vor-
zuziehen, zumal die Bedeutung *Rabe' für das Avesta-
wort gar nicht passt (sie beruht zudem nur auf einer
Vermutung Destür Daräb's) *).
863. Ualäh \VIütze'; Helm (aus Stahl, Sahn. I, 100 Vers
711)', kidä, hdeli.
') Vergl. g. kaj).
^) Durch einen Vers des vorfirdusischen Dichters Abu Öekür
belegt.
^) Im Neupersischen wird das Wort aber nie mit q^ sondern stets
mit k geschrieben. Es müsste also ein Schnitzer im Gazophylacium
und in der jüd.-pers. Schreibung vorliegen.
*) Nachträglich sehe ich Hübsch mann's Bemerkungen in
KZ. 26, 607 folg., der auch aw. väi^ayun- nicht als *Rabe* gelten lassen
will und bei. f/nräy *crow\ köh-f/uräy Vaven' (Damea, S. 104) heran-
zieht ( Corrokturnoto ).
==== printed 279 leaf 300 ====
— 279 —
97. yrav (geschrieben yrüb), vd. 9 (41) (42); vielleicht
nur Transcription.
aw. grava- 'Rohr, Stab'. West, S. B. E., Vol. XVIII,
437 übersetzt strongly* und nimmt also phlv. grav
nicht als aw. grava- entsprechend.
98. gristak 'Loch, Höhle' (für aw. gereda-; Bund.).
99. ffuaftlh ^Gewinn, Erlangung (AV.), guaftak gain*
(West, Dät. din 8, 4).
ai. cyäpti' *das Erreichen, Erlangen*.
100. f/tii)astak Verflucht* (päz. gizasta, gajasfa etc.), Men.,
Guj. Abälis (ed. Barthelemy).
aw. ^eijasta-j vergl. HDüi: (oben No. 1081) und np.
xujeste {oben No. 470).
101. yunierftan 'sich vermischen*, Praes. gumejet (pAz.
gumßz"), gunidj(i)sn (Bund., Aw.-Komm. etc.).
Vergl. np. äme/tefi (oben No. 51); np. gumeze des
BQ ist nicht belegt.
102. yursltan 'hungern' (vd. 9 (182) Gl.).
Derartige Verba sind nicht wenige verloren ge-
gangen, die nicht besonders aufgeführt sind, wie
kam(i)8tan, man(i)stan 'bleiben* etc.
H.
103. häj vor dem Imperativ.
Vergl. Nöldeke, Tabarl-Übersetzung, 385 Note 2.
104. hax 'Fußsohle (vd. 8 (219) (221), 9 (107) GL).
aw. ha/a- 'Fußsohle*.
Da der Kommentator keine Glosse macht, so ist
phlv. ha/ vielleicht noch verstanden worden; doch
steht das Wort an der letzterwähnten Stelle in
Awestabuchstaben.
Dasselbe gilt für lia/t 'Schenkel' (vd. 8 (184), Zend-
buchstaben; 9 (82) ff.), aw. haxti-, ai. sdkthi-^ sakthdn
'Schenkel', oss. t. ayd 'Lende' (7).
105. hamestär Gegner, Widersacher, hamestärih (Men.,
Bund.).
```


## [2026-09-14T01:58:00.094Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT haxti ===\"; grep -n \"haxti\\|haxa-\" BRT.txt | head -20; echo \"=== SNS haxt ===\"; grep -n \"haxt\\|hax \" SNS_pages.txt | head -20"
}
```


### [2026-09-14T01:58:00.199Z] TOOL RESULT

```
=== BRT haxti ===
28837:mit  ä  'sich  heften,  haften  an  — '  (Aklc): ä  diiit  ä* hil.haxti''l  yava&a  .  .  "an  den heftet  er  sich  .  ."  V.5. 34.
28905:•  j.  haxa-  n.  'Fusssohle':  äruxs  yä  nasui .  .  alairi  'x>m  mvSiryde  V.&69;  F.Jg; —  daiitum  {bez.  hsyum)  'xam    V,  ü.  70*.
=== SNS haxt ===
999:\-                                                                                                      (TO ^lirVt&tS^'-^L.&i.Jj&jijijL .Jj'j^'obhaxt V**-*                                              1
1006:                                                                                                                                                  haxt- fc-
1008:                                                                     pas, *HR          >»                         f/U £ .c*-lj o'j haxt 1 dasn: c^«»W
15110:visa- 287/10             spanta. arraaiti- 176/11          haxt- 2/11               hudigh-, hucfaqh 77/1]
16157:                     ham/ham 5/20                           hara-zaman 54/11        haxt 2/10
16159:                     ham 46/14                              ham-zOrlh 50/20         haxt i dasn 2/12
```


## [2026-09-14T01:58:01.393Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD hax ===\"; grep -n \"^hax\\|haxt\\| hax \" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"haxt\\|hax\\b\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T01:58:01.471Z] TOOL RESULT

```
=== PHD hax ===
PHD.txt:396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
PHD.txt:1383:convert haxtan.
PHD.txt:2225:haunch haxt,
PHD.txt:2284:hip haxt.
PHD.txt:2578:lead (v.) anidan, franāftan, haxtan, nidan, rāyēnīdan, zaménidan, adēn-; ~ up ahrāftan.
PHD.txt:3977:thigh haxt, ran.
PHD_mackenzie.txt:2879:haxt [hC)ht l ] thigh, haunch, hip.
PHD_mackenzie.txt:2880:haxtan, haz- [h)htn', h)e-] lead, guide, persuade, convert.
PHD_mackenzie.txt:6243:confounded stard.                            convert haxtan.
PHD_mackenzie.txt:6735:guide (v.) haxtan, nimudan.              hateful gizistag, zist.
PHD_mackenzie.txt:6737:guilty, be""" of pesar budan.            haunch haxt.
PHD_mackenzie.txt:6803:hip haxt.                                        manig.
PHD_mackenzie.txt:7266:persuade haxtan.                           pleasing hudosag.
PHD_mackenzie.txt:7747: taken griftar.                           thigh haxt, ran.
PHD_mackenzie.txt:11281:haj, baz                                  haxt                   \lb'U' )
PHD_mackenzie.txt:12338:2hiid, haxt               \\Vl)t    pasdanisnihI    ~\4Jr--u~
PHD_mackenzie.txt:12367:                                              haxt                         \~
PHD_mackenzie.txt:12369:                                              ahixtan, haxtan              \\\(.J'VU'
=== NYB ===
1512:Paz. frahang farhang = NP. From fra- haxtan g. v.).
1513:frahangistän [plh'ngst?n'] school 48, frahaxtak [plhhtk'] educated, well-bred, skilled 33-5. 10811, — From
1514:frahaxtan [plhhtn'] to educate, to train, pt. = pret. pass. 3d p. sg. frahaxt 2*7. — Pres. frahanj-. MPrth pres. frhynj- ‘to teach’; NP farhaxtan, farhanjidan. From fra + Av. (784sg.) 0ang- ‘to draw’; Verbum 198; Ghilain 51.
1934:*hārēftan [h'lyptn'] *hārēf-; [h'lyp-] 1. to mix, referring to the coition 4315: after ēvak apar, apāk dit, apar ēstāt hend 6 én kar 4314-15 (v. ?apük 2) the narrator continues api-šan MDM hareft: as the construction is pass. we expect here a subj.; this is probably hidden in MDM which is, in that case, the wrong ideogr. for aw. ’pl = "pr or ?c] = "cr, or the like, signifying ‘the genital fluid’ : the fluids from their genital organs were mixed together, with the gl. kū-šān pat takoš (g. v.) frac grift ‘that is: they clasped tightly’. — 2. to infect: api-š 61 dit Zartuxst pas andarg haxt ka hārēft ēstāt purr gaz (etc.) and Z. saw her from behind, between her thighs, (and saw) that they were in- fected, full of snakes (ete.) 5726-581, — 3. to attach, to assign a th. to (6) a p,: whenever Pourušāsp desires to have a divine service ‘performed yazišn 6 yas- taran härefät he shall assign the service to (true) ministrants 5314-15, with the gl. ki 6 yazāt ke apāyet yastan that is: that one shall perform the divine service to whom it pertains to perform such service’, ef s. v. bahr. — (1483) ham.raedwayeiti ‘to mix, to mingle, to infect’, from which the signi- fication ‘to attach’ was easily derived (cf the simplex vb. in the expression kahrpam raēdwayeiti ‘assumes a visible shape’ Yt. 813); a den. of rae0wa- ‘mixture, muddle’. *ham-ra- > hara-, cf (1529) rgroma- < *ramrama- (the Av. spelling ham- is a compromise between hq- and ham-); *har- in Milr > har-. The Milr vb. be- longs to the NW linguistic area: raēdw- > réf- is a normal NW development. As the vb. is a den., the pres. st. kārēf- must be regarded as the primordial form, and
1967:haxt [hht'] thigh 5726. — Av. (1745) haat-.
1968:haxtan [h’htn'] to pull: api-m ... carm bē haxt and I stripped off his skin 3211-12, — Av. (784sg.) 6ang-. The pres. ähanj- (g. v.) and kanf- (v. hixtan) belong to this root.
1969:haxtan [h’htn'] häc- [h’c-], to cause to adhere to, to follow; to convert a p. to: i ka-š Vistäsp be 6 den hàxt because he had converted V. to the Religion 9513-14;
2208:kar [k'1] work, act, deed (also evil), busi- ness, errand, matter, case, task, cas. obl. kārē [k'ly], käreh [k'lyh] (ef s. v. karp); with indef. art. kār-ē [k'14-1] anything 1122, something 104°; pat kār-ē for some business 1417; 3511-14, 5027 etc., passim; — 6 butan i ham-ic kārē frahaxtak in order that all might be instructed in this matter (viz. in the new religion) 10811; pat martom käreh through human work (= as far is humanly possible) 1172; — ~ framiitan to bring about 19%; ~-om tō framāyē do thou thy duty to me! 2722; amāh dp i tč pat ~ né apäyet we do not need thy water 1423; 375-5; andar 6 ~ kartan to begin using regularly 9614; pat én ~ ku with the commission to ask: “.. — often coordinated with another notion so as to form a hendiadys expressing that the notion is put into practice: ~ u kirpak (work and religious virtue =) meritorious religious deeds 13% and passim; ~ u dätistän, v. this w.; ~ u räyenisn prac- tical function 87? (in this construction u is very often wanting in MSS and edi- tions); — šahrē -än (pl. cas. obl.) “‘state- work" — penal servitude, forced labour 92; zanč ~-dn 834 v.s.v. zan. — = NP. Av. only in the adj. kära-vant- (465); on OP kära- v. kürécür. — V. also a-kär, dast-kārēh, "ham-kär, kām-kār, kār-dāk, kàür-nàmak. ' > god
2704:nihaxtan
2712:nihaxtan [nh’htn'] "to coil, of snakes: apar gaz nihaxt hend (with the gl. kū Sut hend) apar 6 han + murv pus the snakes coiled upon the nestling 409-10, - Cf the name of the crocodile or alligator: MPrs nhng List 85, Arm. lw. nhang, NP nahang, in all probability < *ni-danga- ‘the dragger, the crawler’ from nt + Av. (784) 6ang- ‘to draw’, which may well have been used for the coiling movements of snakes. In NW (ni-dang-) nihaxtan signifies ‘to hold back, to restrain’ (A- H III, MHC, Ghilain 51).
2980:pas PHL; B’TL 5726], with -c: pas-ic PHL-c] adv. 1. behind: bē raft hend... Vahuman pes, Zartuxšt pas they went away, V. first, Z. behind 5712-33; ~ ~ one after the other 11012; ~ andarg haxt on her back between her thighs 572%; hac ~ from behind 25%. 2817; 6 peš... 6 ~ forwards ... backwards 6811-12; — hac ~ + prep. behind 31%; api-šan ... hac ~ behind them 717-18; õi . . . hac m in her footsteps 3718-19, — 2. afterwards, then: ~, or u ~, or ~-ic, pursuing a narration, passim; introducing the apo- dosis after a subordinate clause 243-8, 27273, 4411-13, 914-5; ka vas-ic ... ~ -ic however much yet 9112-13; apäk
3700:tài [D] a) until, b) as long as, as far as: A. prep., local and temporal: ~ [YM? =] rot danbY as far as to the bank of the River P 1:3; — nazd bam until daybreak 53; ~ nun until now 79; ~ sar carm bē haxt stripped his skin up to his head 321-1?; — ka? up to whom (does) Right- eousness (reach)? (— who is the origi- nator of Righteousness ?) 57! ; also govern- ing an inf.: 47M. 779; ~ 3 róc within three days 710; ~ zivandak drahnāt dur- ing the whole lifetime 6514; hac ... ~ from... to: hac pus ~ brat from son to brother, both sons and brothers 221; all men hac 10 säl — 80 sälak from ten to eighty years 20*; passim; — also ~ 6: ~ 6 drayäp 671; ~ 6 3 bar until three times 539-10. =. bē 6 asmün 9218; etc.; — han-tàa, v. this w.; — except(ed): sak ... u dalman ~ apārīk o apāyet xtartan dogs ... and eagles excepted, all the other (animals) may be eaten 9421-22; in frame preposi- tions: bé man ~ an kas nē except myself no one else 157; bē Zartuxšt ~ Z. ex- cepted 9313-14; apar 3 Sap ~ three nights ago 512-3, — B. conj. 1. final: in order that, with pres. ind. passim; with subju.: ~ rasāt 4125-26; m ... bavät 45"; governed by a vb.: framäyet ~ pätifräs . . . kunend
5392:tap-, tapa-, tapaya-: taftan (vi-)tar-: vitartan tarasca: turist tarsna-: tisnak taro: !tar, turist taš-: tašitan tašta-: tašt taOra-: tārīk taOrya-: tàrik tauruna-: tarr tav-: tuvan (pati-)!tav-: pattài, pattàn tavah-: stob tiyri-: tigr | Tird.nakaOwa-: Tir Tištrya-: Tistr tiži-: tēž tkaēša-: kēš tõi, to: -t türa-: Tur Tusa-: Tiis tušni-: tušn (fra)-Oang-: frahaxtan Oračtaona-: Fréton Orah-: sahm Orah-, terosa-: tarsitan Orisant-: !sih Orišva-: srišvātak Orita-: Srit Orita-: Oritak Oritya-: sitikar Owa-: to Owaxš-: tuxšitan
5611:fr'e: frac frhynj-: frahaxtan frm’n: framàn
6051:nhng: nihaxtan
7133:farāmēš: frāmēš faräx, frax": faraz: frac farda: fratak farhanjidan: frahaxtan Faridün: Fréton farjam: frazäm farman: framan farmudan, farmay-: framatan farrah: x"arrah farrux: farraxu farsang: frasang farsüdan, farsäy: apa- sutak farvardgän, faravardigän: fravartikän faryäd: friyät farzänah: frazänak farzand: frazand
```


## [2026-09-14T01:58:10.995Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hax\\(t\\|ti\\)\\b\\|haxti-\\|hayti\" BRT.txt | head -20; echo \"=== around 28905 ===\"; sed -n '28895,28925p' BRT.txt"
}
```


### [2026-09-14T01:58:11.062Z] TOOL RESULT

```
7035:yeü,  ß)  vorausgehendem  yen  'Svenn  aber, wenn  jedoch",  kondiz.:  a)  *yujyastis  hala *nmä>tat  . .  a°  yat  he  aoxte  .  .  dka  *hä *x!ayae  .  .  haxtöit{%A.)  N.A'f.;  V.7.3 äat  (s.  ?•)  yg  .  .  upairi  hunarain  (sd.)  maiiü barst  .  .  J'  yaj  .  .  faiti  barät  aat  (s.  z) yat  .  .  ava  baraite  "wer  .  .  aber  wenn  er .  .    und    wenn    er    .  ."    P.^jjf.;    —  yezi
13616:•  j.  dahiäta-  Adj.  'der  (in  Sachen  der Religion)  bestunterrichtete,  sachverstän- digste, im  Ritual  bewandertste';  zao/a  {sd.) anahaxtö  .  .  'tili  ars.vacasi>mäi  zao^rpm ragxiaiii  N.  Ä»;  —  srag^ävamim  ..  °tim *arl.vaca$fytn»m  Vr.j.  i;  —  °ta  (als  AP.) arLvacashma  A.,5.4;  —  saosyantascä  °iq ^ars-vaüastima  Y.  y.  3,  Vr._j.  5  (wo  'fS); —  *'laisva  Yyt.42''>.
17957:•  j.  fra-sraoäya-  n.  'lautes  Aufsagen'  spez, des  Ahunai^iryaGehets,  mit  Akk.  verb.: cvaiti  narqm  ^haxtö  aaota  (sd.)  ralufris ahun?m  vairltn  °syehe  N.  20.
28837:mit  ä  'sich  heften,  haften  an  — '  (Aklc): ä  diiit  ä* hil.haxti''l  yava&a  .  .  "an  den heftet  er  sich  .  ."  V.5. 34.
28868:5)  Auii er  Zusammenhang.  Y^.-.  haxt.  —  t)  Vgl.
28916:haxt-
28919:•  j.,  g.  haxt-**  n.  'der  innere  Teil  dea| Oberschenkels':  jieii^a  aps  .  .  'H  (AD.) paULjasaiti  V.ÄS9;  58,  p.ai';  —  */«'' F. Jg.  a)  to«ü»  'tayä  (GS.) 3*  sva.  'in Mark  und  Bein,  in  Fleisch  und  Blut': yavtst  aiul  (sd.)  *zrazciists  bSndi  'tayä "^■53- 7-
28921:—  Pü.:  -ijj/t),  ^<x  F.  mit  der  np.  Glosse: sarmgäh  i  sanan.  —  ')  haxt-  nnd  ai.  säklh-i decken  sich  nicht;  s.  S  3.  i,  3^8.  3.  Urir. haxl-  mag  sein  t  dem  Eintluis  van  tat-  'Kno- chen', mpUty-  'Hüfte'  Tcrdanlteo.  —  >)  Kasus?
28925:•  j.haxtöU"  Inf.  'sich anzuschliessen  an -
=== around 28905 ===
avoiy  AagmatSnaiy  a'iar  didäm  /rsAi^-
jam^l  Bh.2. 13",
ai.  säjaä  (lataSjä)  'er  hängt,  heftet  tut'.  — ')  Oder  auch  Fraes.  3  iaja-  (Jrähajam),  was genauer  lum  Ai.  »timmen  würde.  —  ")  Zuletzt iSt.  Fov  KZ,  j/.  547,  wo  weitete  Li».
•  j.  bak^nt^^tn-  Adj.  'auf  ein  Mal,  mit einem  Stoss  tötend';  'janö  varäzahe  Yt, 14- 15-
Vgl.  tüvo-gart'.  —  Npü.:  ka  ba  yak  baragi  ml rasad  a%  bulandt  u  düri.
•  j.  *ha-j'Äai»h«m ''  Adv.  'in  Erfüllung  der Bitte' :  ä  hlpasiaüa  frinaiti  atarl. .  xhiüto atbistö  •nhm:  Upa  äa/3  haxMt  . .  "ihm wünscht  Äf.  dann,  wenn  er  zu&ieden  ge- stellt, nicht  gekränkt  ist,  in  Erfüllung  der Bitte;  'es  möge  dir  zu  teil  werden  . .'" Y.52.9f.;  V.i&26.
■^tyayfWötaltomp.j  ans  *r.  *sa-gdAasa-  Adj, 'TOn  dem  Gegenstand  der  Bitte  begleitet''); *liavAa-  m.  "Bitte,  Gegenstand  der  Bitte' lum  V.  gaä-Ü.  —  Pii.:  lä-,  Sfi.:  (;^äA*}.  - I)  So  (mit -jw)  Pt4,  Mf4.  Ja,  Ks,  Mfa. Jpl;  NA.  -»Akoj.  —  ")  VgL  iBed.  ai.  id- iäma-  Adj.  —  1)  Vgl.  iBild.  «i.  Miydiam.  ~ 4)  Daher  Dst.  ZA.  z.  389  'bien  rassasij'. Aach  die  Dealongen  *□□  lia-fi'  bei  Roth  in Sp.  Komm.  /.  393,  Haug  SBayrAW.  rS6S. a.  36,  Gdn.  Stnd. /.4T  sind  unhaltbar.  Gdn.s Übersetiung  'reicher  Segen'  SPteuisAW.  igoj, 436  iit  mir  nicht  deutlich.
•  p.  ha°-gniata-  Adj.,  PPfP.:  s,  gam-, Sp.  501  m.
•  p.  ha^matäna-  m.  Name  einer  Stadt in  Medien,  Ekbatana:  fravartis  . .  haruv^- Sim  iära^  avaina*  pasäva''  adam  'naiy utmayapatiy  aiunavam  utä  fnarliyä  . . avaiy  'rtaty  a!'tar  ätäam  frisha''jam  Bh. 2.13.
Et.?  Am  ersten  allenfalls  noch  hagma-tän^', Bed.?  Vgl.  KZ.  j/.  Sil.  wo  weitere  Litt; dain  noch  Masquakt  Eranlahr  70.  Der  Name braucht  ja  aber  gar  nicht  iranisch   zu  sein.
•  j.  haxa-  n.  'Fusssohle':  äruxs  yä  nasui .  .  alairi  'x>m  mvSiryde  V.&69;  F.Jg; —  daiitum  {bez.  hsyum)  'xam    V,  ü.  70*.
Fü. :  Aax,  erl. :  hafaiar  i  fäi.
•  j-  (1  g-t  P)  haxay- :  Ariy-,  Aai'-^^,  m. i)  'Freund,  Genosse':  ^m  °xa  (NS.)  '1/ (DS.)  *baraiti  Y.  6'2.  8;  —  aa£  aosOe  'xa •sa  (IS.)  V.  18.  a6;  F.  24;  —  yaS:a  . .  mri Aamü.äaina  Jason  brn%ra  va  'xaya  (NP.) vä  V.  4.  44;  Vyt,  10;  —  vlsaitiva  asti mi^r5  atiian  'ia  (AD.)  suptiiiannga  (sd) Yt.  JO.  116;  —  Sxstim  kqm.vaintfm  .. 'xaya    (AD.)    sraosaAe    Yt  //.  16;     16',
a)  von  den  Genossen  des  Astvüt.- >rHa  (sd.):  aAhe  'xays  (NP.)  .  .  astvat- ?r>tahe  YL  15.95; —  saolyantatn  viriirä- JariPtn  uta  anyasHt  'xayä  (als  AP.)  Yt ig.&g.  a)  insbes.  'Genosse  der  Priester- zunft":  'lamca  Aävi.'tafiqm(sd.)ca  al'^ra- pailinqmca  ..  \.68.ix.
KompA.  {Anxä',  haii'\  E.  —  ai.  tdUay-  m-  — iFlex.  i.  S  406.  —  EL?  Vgl.  Beil.  GrCr.3 183.  —  Ffi.;  äSsl;  hamträliak),  erL:  träS  i döst.   —   ■)  S  (pO.  3  a.
•  p,  haxä'maniä-  m.  EN.  eines  vomehmeD Persers,  des  Stammvaters  der  Achaemeni- den"',  Achaemmes''' :  Hspäis  pitä  •«//Bh.
fünfte  Vorfahre  Zlo™«  L  ZumStttom- banm  »gl.  zuletzt  ANDBEASVerb/j.OiKongr.  94- Ableit.  —  Eig.  'der  die  Gesinnung  des  Freiw- des  hat',  Komp.  mit  NS.  im  i.  Glied');  »gl. kmia.'  und  S  26^  D.  —  ')  Zum  ai  in  'Axailän- vgl.  lulelit  FickBB.  3^.  31a,  HOsiNoZDMC. 54-  ia9,^Fov  KZ.  j/.  503.
•  p.  haxamaiiisiya-patr.Adj. 'vonÄi'-t* manis  abstammend,  dessen  Nachkomme'! därayJ'vi^u^  .  .  'yt^  Bh.  ;.  1,  D.  i,  2,  5.  i. 6.  a,  13,  13,  16,  ig,  *H.  1.  3  '>,  5,  Am.  i,3' Ao.  /.  a; —  avahyaradiy  vayam  'yä  "iahjä- maAy  "deshalb  werden  wir  Achacmeoide" genannt"  Bh.  i.  3.
Ableit.  aus  kaxämami-.  —  »  Hier  steht  i(üä*'> (.  NÖLDEKE  Persepolit  3.  1  b.
dby  Google
1745
haxt-
ha6a  Ul  i  t
1746
•  j.,  g.  haxt-**  n.  'der  innere  Teil  dea| Oberschenkels':  jieii^a  aps  .  .  'H  (AD.) paULjasaiti  V.ÄS9;  58,  p.ai';  —  */«'' F. Jg.  a)  to«ü»  'tayä  (GS.) 3*  sva.  'in Mark  und  Bein,  in  Fleisch  und  Blut': yavtst  aiul  (sd.)  *zrazciists  bSndi  'tayä "^■53- 7-
ai.  vgl.  sdkiMt)  'Schenkel';  oom.  ayrf  'Lende'.
—  Pü.:  -ijj/t),  ^<x  F.  mit  der  np.  Glosse: sarmgäh  i  sanan.  —  ')  haxt-  nnd  ai.  säklh-i decken  sich  nicht;  s.  S  3.  i,  3^8.  3.  Urir. haxl-  mag  sein  t  dem  Eintluis  van  tat-  'Kno- chen', mpUty-  'Hüfte'  Tcrdanlteo.  —  >)  Kasus?
—  3)  Stall  •»>•,  s.  die  Var.  haxlyi;  %  168. II.  Neubildung  zum  ND.,  Tgl.  J  32j  lu  ai. oi^J^.  —  «  Zu  Y.  und  V.  in  Aw,-Buchst.
•  j.  haxta-  Adj.  '(aus  innem  und  äussern Gründen  berechtigt,  d.  L)  geei genschaft el und  ermächtigt  (etwas  zu  tun)':  '"•/J''  saota "ein  (zu  ^<Tii/i7ramtllchen  Verrichtungen) qualißzirter  Zaoiar"  N.  20;  —  'ts  ..  ana- haxts  N.  6.
KompE.  —  PPfF.  einer  Basis  ir.  *ha»i-  oder 'hang:  —  np.  y^.  farhctilan,  farkang  {x. HbM.  AGr.  /.  iSl).  —  Pü.!  /3  äJrSs.  — i>  Hds.  Olli.
•  j.haxtöU"  Inf.  'sich anzuschliessen  an -
```


## [2026-09-14T01:58:12.533Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD skel ===\"; grep -n -i \"^skel\\|skel-\\|isosceles\\|kylindros\\|kyklos\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T01:58:12.594Z] TOOL RESULT

```
=== AHD skel ===
935:skel-'
936:form *sk(hjid-yo- in Greek skhizein, to split: SCHISM, SCHIST, SCHIZO-; C. nasalized zero-grade form *ski-n-d- in Latin scindere, to split: SCISSION; EXSCIND, PRESCIND, RESCIND. 5. Extended root *skeit- in: a. Germanic *skaith-, *skaidan in (i) Old English scéadan, to sepa- rate: SHED! (ii) perhaps Old English scéath, sheath (< “split stick”): SHEATH; b. Germanic *skidam in Old Norse skidh, log, stick, snowshoe: SKI; C. o-grade form *skoit- in Latin scittum, shield (< “board”): ECU, ES- CUDO, ESCUTCHEON, ESQUIRE, SCUDO, SCUTUM, (SQUIRE). 6. Extended root *skeip- in Germanic *skif- in: a. Middle English sheve, pulley (< “piece of wood with grooves”): SHEAVE?; b. Old Norse skifa, to slice, split, akin to the Scandinavian source of SKIVE; c. Middle Low German schever, splinter, akin to the possible Low German source of Middle English schivere, scivre, splinter: SHIVER?. [Pok. skei- 919.] skel-'. Also kel-. To cut. 1. Germanic *skalj6, piece cut off, shell, scale, in: a. Old English scell, sciel, shell: SHELL; b. Italian scaglia, chip: SCAGLIOLA. 2. Germanic *skalé in: a. Old English sc(e)alu, husk, shell: SHALE; b. Old French escale, husk, shell: scALE!. 3. Germanic *skal- in: a. Old Norse skalli, bald head (< “closely shaved skull”): SCALL; b. Old Norse skalpr, sheath, shell, akin to the source of Middle English scalp, scalp: SCALP. 4. Germanic *skél6é in Old Norse skal, bowl, drinking vessel (made from a shell): SCALE’, SKOAL. 5. Germanic *skelduz in Old English scield, shield (< “board’’): SHIELD. 6. Germanic *skeli- in: a. Old Norse skil, reason, discernment, knowledge (< “‘incisiveness”): SKILL; b. Middle Dutch schillen, to diversify, with past partici- ple schillede, separated, variegated, akin to the Low German source of Middle English scheld, variegated: SHELDRAKE. 7. Germanic skulé, a division, in Middle Low German schdle, troop: SCHOOL?, SHOAL’. 8. Suffixed variant form *kel-tro- in Latin culter, knife: COLTER, CULTRATE, CUTLASS. 9. Suffixed zero-grade form “skl-yo- in Greek skaillein, to stir up, hoe (> skalenos, uneven): SCALENE. 10. Extended root *skelp- in: a. Germanic *skelf- in Middle Low German schelf, shelf (< “split piece of wood”): SHELF; b. possibly Germanic *halbaz (< variant root *kelp-), divided, in Old English healf, half: HALF; C. perhaps variant *skalp- in Latin scalpere, to cut, scrape, with derivative sculpere (originally as the combining form of scalpere), to carve: SCALPEL, SCULP- TURE. [Pok. 1. (s)kel- 923.] skel-2. To be under an obligation. O-grade (perfect) form *skol- in Germanic *skal-, I owe, hence I ought, in Old English sceal (used with the first and third person singular pronouns), shall: SHALL. [Pok. 2. (s)kel- 927.] skel-3. Also kel-. Crooked. With derivatives referring to a bent or curved part of the body, such as a leg, heel, knee, or hip. 1. Suffixed form *skel-ko- in Germanic *skelha- in Old High German scilihen, to wink, blink (> German Schiller, iridescence): SCHILLER. 2. Suffixed form *skel-es- in Greek skelos, leg: ISOSCELES, TRISKELION. 3. Suffixed o-grade form “skol-yo- in Greek skolios, crooked: sco.iosis. 4. Lengthened o-grade form *skol- in Greek skéléx, earthworm, grub (< “that which twists and turns”): SCOLEX. 5. Suffixed lengthened-grade form *k6l-o- in Greek kélon, limb, member: COLON}. 6. Attrib- uted (quite doubtfully) by some to this root is Greek kulindein, to roll: CALENDER, CYLINDER. [Pok. 4. skel- 928.] skele-. To parch, wither. Variant *sk/é-, contracted from *skleo-. 1. Greek skellesthai, to dry, whence skeletos (< suffixed form *skeb-to-), dried up (body), mummy: SKELETON. 2. Suffixed variant form *sk/é-ro- in Greek skléros, hard: SCLERA, SCLERO-, SCLEROMA, (SCLEROSIS), (SCLEROTIC), SCLEROTIUM, SCLEROUS; SCLEROTIZATION. [Pok. 3. (s)kel- 927.] skeng-. Crooked. Germanic *skank6n-, “that which bends,” leg, in Old English sc(e)anca, shinbone: SHANK. [Pok. (s)keng- 930.]
1329:CAKE kak-2 CALAMITE kolem- CALAMITY kel-1 CALAMUS kolem- CALANDO ghé- CALDRON kele-1 CALENDAR kele-2 CALENDER skel-3 CALENDS kel@-2 CALENTURE kele-1 CALIBER ped-! CALIX kal-1
1383:COLE kaul- COLEOPTERA kel-2, pet- COLEOPTERAN kel-2 COLEOPTILE kel-2, pet- COLEORHIZA kel-2, wrad- COLESLAW kaul- COLEUS kel-2 COLLABORATE leb-1 COLLAGE koli- COLLAPSE leb-1 COLLAR kwel-1 COLLATE tele- COLLEAGUE leg-1 COLLECT! leg-1 COLLEGIALITY leg-! COLLET kwel-1 COLLIE g(e)u-lo- COLLIER g(e)u-lo- COLLIGATE leig-' COLLIGATIVE |leig-1 COLLO- koli- COLLODION koli- COLLOQUIUM tolkw- COLLOQUY tolkw- COLLUDE leid- COLLUVIUM leu(a)- COLOBOMA kel-1 COLON! | skel-3 COLONEL kel-6 COLONNADE kel-8 COLONY kWel-1 COLOPHON kel-6 COLOR kel-2 -COLoUS kWel-1 COLPITIS kwelp- COLPOSCOPE kwelp- COLPOSCOPY kwelp- COLTER skel-1 CoLuMBA kel-5 COLUMBARIUM kel-5 COLUMBINE kel-5 COLUMN kel-6 COLZA sé-1
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
1691:Is es- ISALLOBAR gWere-2 ISCHEMIA segh- ISINGLASS bhié-2 ISLAND akwa- ISOBAR gWere-2 ISOCLINE klei- ISOGLOss glogh- ISOHEL sawel- ISOHYET seue-2 ISOMER (S)mer-2 ISOMETRIC mé-2 ISOPIESTIC sed-1 ISOPLETH pele-1 ISOSCELES skel-3 IsosTasy sta- ISSUE ei-1
1975:OMNIBUS op-! OMNIFARIOUS dhé-1 OMNISCIENT skel- OMNIUM-GATHERUM op-! OMPHALOS nobh-
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
2222:SCAB skep- SCABBARD sker-1 SCABBLE skep- SCABIES skep- SCABROUS_ skep- SCAGLIOLA skel-1 SCALD! kele-1 SCALE! skel-1 SCALE? skand- SCALE’ skel-1 SCALENE skel-! SCALL_ skel-!
2223:SCALP skel-1 SCALPEL skel-1 SCAN skand- SCANDAL skand- SCANDENT skand- SCANSION skand- SCANSORIAL skand- SCANT kem-1 SCAPHOID skep- SCAPULA skep-, sker-1 SCAR? sker-1 SCARCE kerp- SCARIFY!  skribh- SCARP_ sker-! SCATHE skét(o)- SCATO- sker-4 SCAVENGER keu-! SCENT sent- SCHADENFREUDE preu-, skét(e)- SCHEME segh- SCHERZO sker-2 SCHILLER skel-3 SCHIPPERKE skipam
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
2252:SEXTUPLE pel-3 SHABBY skep- SHADE skot- SHADOW skot- SHAFT! skep- SHAH tké- SHAKO dek-2 SHAKTI kak-1 SHALE skel-1 SHALL skel-2 SHAMBLES skabh- SHANK skeng- SHAPE skep- SHARD  sker-1 SHARE! | sker-1 SHARE? sker-1 SHARP sker-1 SHATTER sked- SHAVE skep- SHAWM kolem- SHE so- SHEAF skeup- SHEAR sker-1 SHEARS sker-! SHEATH skei- SHEAVE? skei- SHED! skei- SHEEN keu-1 SHEET! skeud- SHEET2 skeud- SHELDRAKE skel-1 SHELF skel-1 SHELL skel-1 SHIELD skel-1 SHIMMER skesi- SHIN! skei- SHINE skeei- SHINGLE! sked- SHINGLES kenk-! SHIP skipam SHIP skep- SHIRT sker-1 SHIT skei- Suiva_ kel-1 SHIVER? skei- SHOAL? skel-1 SHOOT skeud- SHORT sker-1 SHOT! skeud- SHOVE skeubh- SHOVEL skeubh- sHow keu-! SHOWER! kéwero-
2268:SITZMARK sed-1 SIX s(w)eks SKALD sekw-3 SKATOLE sker-4 SKEAN skei- SKEET skeud- SKELETON skele- SKEPTIC spek- SKI skei- SKIAGRAM skeei- SKIASCOPE skeei- SKIFF skipam SKIJORING geue- SKILL skel-1 SKIN sek- SKIPPER! skipam SKIRMISH sker-1 SKIRT sker-1 SKIVE skei- SKOAL skel-1 SKY (s)keu- SLAB? leb-1 SLACK! slég- SLAG slak- SLAM! leb-1 SLAP leb-1
2411:TRIO trei- TRIOECIOUS weik-1 TRIP der-1 TRIPEDAL ped-1 TRIPLE pel-3, trei- TRIPLEX trei- TRIPLOBLASTIC pel-3 TRIREME ere-1 TRISKELION skel-3 TRISMUS | strei- TRISOCTAHEDRON trei- TRITANOPIA ei- TRITE ter * TRITIUM trei- TRITONE trei- TRITURATE tere-1 TRIUMVIR trei-, wi-ro- TRIUNE oi-no- TRIVET ped-1 TRIVIAL wegh- TRIVIUM wegh- TROCAR kwetwer-, trei- TROCHAL dhregh- TROCHANTER dhregh- TROCHE dhregh- TROCHEE dhregh- TROCHLEA dhregh- TROCHOPHORE dhregh- TROGON tere-1 TROIKA trei- TROPE trep-2 TROPHALLAXIS al-1 TROPHIC- threph- TROPHO-  threph- -TROPHY threph-, trep-2 TROPIC trep-2 TROPO- trep-2 -TROPOUS  trep-2 TROT der-1
```


## [2026-09-14T01:58:32.494Z] TOOL CALL #18: Bash

```json
{
 "command": "pdftoppm -f 453 -l 453 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg453 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg453.png"
}
```


## [2026-09-14T01:58:33.642Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor leaf in (601,602,603):\n    print('==== leaf',leaf,'(printed ~',leaf-5,') ====')\n    print(pages[leaf-1][:1800])\nEOF"
}
```


### [2026-09-14T01:58:34.552Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 78966 Sep 13 21:58 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg453.png
```


### [2026-09-14T01:58:35.993Z] TOOL RESULT

```
leaves 725
==== leaf 601 (printed ~ 596 ) ====
                                                                                                                    ;




596                                                  sqel-



gedit „das Bersteii“, ahd.               5%,          Dhd. ScJiUt^, mhd.                slei^e^   nhd. schleipe
„Leuchtspan“;
     lit.   sldeidHu,    sMdsti     5
                                        ,ausbreiten    was         zsgefaltet        oder zsgehauft war“,
sklaidaii, -yti     ,.hin     und her blattern,           refl.        sich zerstreuen“, issMaidSiojui^)
„werfe auseinander, zerstreue'S shllsti jjauseinanderfliefien^^; lett. sklaidis
„eiii Herumtreiber, Taugenichts“, ohne anl, s- JclaidU 5 ,zerstreuen, sich her-
umtreiben^^, klistu, klidti, kUst ,,sich verstreuen, umherirren^*, lit. klystu,
klydaUj kJysti „sich verirren^' (ohne d lit. klajoju, -oti „heruinirren“, lett.
kjaijdt, -not ds.; diese s-losen               Pormen eine ursprgl. versch. Sippe?);                             apr.
sclait, schJaitj schklait ^sondern; ohne‘", scliklalts Adv. „sonderlich, besonders
sonst'^, adj. „schlichtj         einfach^*,

     Vgl. Persson Wzerw. 107a                  b,    Schroder IF. 22, 194,                   Fick III^ 538f.,
Trautmann Apr. 429.
     Lat. laedo    (Johansson PBrB. 14, 316,                     auch Vf. LEWb.^ s. v.} wider-
                                                                  s.

strebt      im Vok.     (s.   *laidh-);    aisl.    sl^drar       f. slldr n. pi. „Schwert~ oder
                                                                       pi.,

Messerscheide'^ ^kaum              als    s{k)lei-tro-,      -ira~ von der unerw. Wzf.
(Johansson aaO. 315 f.), sondern aus ^slmprd, -pra- (s, u. lot- „Latte‘').                                        —
And
==== leaf 602 (printed ~ 597 ) ====
           ;                 ;       ;




                                                               sqel-                                        597

3. 8q[el“ „austrockiien, dorren^.
   Gr. ayJXkio „trockne aus, dorre'^ (trans.,                              Fut oxeX^^ aor, eoxrjXa W. 191;
intr.,    aor. eoxXrjv,            pf.    eoHXrjxa)^        oxsXezog ^auagetrocknet", m. „Skelett‘‘, n,
„Mumie‘‘, oxXtjqoq „trocken, diirr, hart, rauh, unbeugsam^, oxeXicpQog „aus-
getrocknet, abgemagert‘‘, oxXrjfpgog „klein und flink*", aoxeX^g 1. „ohne
Widerstandskraft“ (ohne oxXrjQorrjg); 2. „unablassig, vom Zorn, vom Weinen"
(eig, „mcht yertrocknend, unversieglich'*        s. Boisacq 88  und bes. Bechtel
                                                                       ;


Lex. 66), JieQioxsXiqg „sehr trocken, hart, sprode, hartnackig", JtEQioxiXsia
„Hartnackigkeit“
   [fern bleibt mir. sceile „niiseria“ (Stokes BB. 21,1 36)] schwed. skdll „mager,  ;


diinn,     fade,        sauerlich‘‘,        nd.   schal „trocken, durr“,           mnd. mhd. schal „schal
von Geschmack;                   triib,   unklar,     vom Gesicht“, mengl. schalowe „schal, matt,
seicht^S engl. shallow (auch                      wohl ags, sceald „8eicht, nicht tief‘‘, nd. scholl
„seichtes Wasser^);
   aber ahd. scalmo „Pest, Seuche“ usw., v^ahrscheinlich zu sqel- „schneiden“.
   Ohne anl. s-: mhd. hel {-11-) „schwach“  hellec „mude“, nhd. Jiellig „matt,
erschopft   von Durst“ (dies die urspriingliche Bed. des Wortes „ausge-                           :


trocknet^^, worauf andrerseits auch „seicht zuruckgeht), mhd. hellegen „er-
miiden, plagen,                       nd. /mZZ „trocken, mager'^; dehn8tufig(?) nd. hdl^
                             behelligen^',
ndl. haal „trocken“,            mndl. ha
==== leaf 603 (printed ~ 598 ) ====
698                                              sqel‘



     sehr imsicher        ai.   kalaniba-h,   kalamhi „Convolvulus               repens"*,        kalambilce
f.   du. „die beiden       Sehnen im Nacken** (Petersson IF. 34, 231);
   np. kul „krumm, gekrummt** (s. Hubschmann Arm. Grr. I 457).
   Arm. sel „obIiquo, storto"*, woven selim „torcersi; trasgredire, prevaricate"*
(Bugge KZ. 32, 57, Pedersen KZ. 38, 205; 39, 396: = o>tB,oq\ abet xd „stor“
piato, perverse, pravo"", Bugge IP. 1, 447 f. zw., Pedersen KZ. 39, 394 zw,, kann
nicht derselben Gdf. entstammen und ist wohl nacb Bugge-Pedersens Alter-
native und Scheftelowitz BB. 28, 291, 312; 29, 48, 61 als ^qhelos mit gr. xoyAog
„labm"" zu verbinden; in o??^„Ruckenwirbel, Rticken"", Pedersen KZ. 39, 387,
begegnet die Zuruckfiibrung von e- iiber                  auf qo- denselben Be-
denken wie bei holovem „rolle"", s. u. q'^el- „drehen"‘ und Liden Arm. St.
127 f.).
     Lautlich unvereinbar arm. kal „lahm"" (Bugge KZ. 32, 50,                                s.    dagegen
Pedersen KZ. 38, 203;             39, 280).
  Gr. otceIoq „Schenkel"", axeXig „Hinterfu6, Hufte bei Tieren"" (att. ox£Ug\
                          pandus, scaurus"" (s. Witkowski Eos 17, 143—152),
G}C£kX6g .ydiEGrQafijusvog,
GxoXiog           improbus"", oxaXrivog             schief, krumm"" (dies nicht
nach Preilwitz^ 413 zw. zu GxdXXay „behacke, grabe""), gxcoXt]^ „Wurm"",
GxcoXvTiTEG&ai „krummen, bin und her winden"", xeXXov gtqePXov, jtXdyiov Hes.,
xvXXog „gekrummt, gelahmt"", TivXXonodtoyv Beiw. des Hephaistos (^xEl-y
xvX-vog', nicht besser nach Sommer Gr. Ltst. 63 mit -XXo- aus -r-lo- zu
{s)qer- „drehen"", wie auch lat. coluber wohl nicht aus ^comber diss. ist;
zur M-Parbe von xvXXog, y.vXtvdoy s. o., und Brgm.-Thumb GrGr.^ 99 m. Lit.),
Tcv
```


## [2026-09-14T01:58:47.208Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg453.png"
}
```


### [2026-09-14T01:58:48.067Z] TOOL RESULT

```

```


## [2026-09-14T01:58:48.051Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T01:59:07.096Z] AGENT

Extraction is faithful to the printed page. Now let me check the Persian and Arabic sources.


## [2026-09-14T01:59:10.747Z] TOOL CALL #21: Bash

```json
{
 "command": "cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg453.png data/verification/sources/refs/ocr/BOOK/453.png 2>/dev/null || { mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg453.png data/verification/sources/refs/ocr/BOOK/453.png; }; ls -la data/verification/sources/refs/ocr/BOOK/453.png"
}
```


## [2026-09-14T01:59:11.781Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD qulun/qulanj ===\"; grep -n \"قولون\\|قولنج\\|كولنج\\|قولن\" TAD.txt TAD_pages.txt | head -20"
}
```


### [2026-09-14T01:59:11.834Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 78966 Sep 13 21:59 data/verification/sources/refs/ocr/BOOK/453.png
```


### [2026-09-14T01:59:11.894Z] TOOL RESULT

```
=== TAD qulun/qulanj ===
TAD.txt:453:)١(‏ ويقولون انما افرنية واصابا بأسبور وهى ا اكلتين وها باس ومعناها مر" وبور 
TAD.txt:1208:0 قولون دوزت الغنى القا نون ونخوءط شد * ما ارنخى من اوثاره لبجحرى عسلية اللحن 
TAD.txt:1744:6 ا الفصيح الفاسول” والعامة تسمها لوحا ونون مية فالا كيقولون -وبن 
TAD.txt:1866:والطاولة عند المامة اسم مطنق بقولون طاولة الجزار وطاو 1 الاسكاف وطاولة المراف وتحوذاث 
TAD.txt:2433:قوأنج بست مرض تصيب القولون ممامعآ1 اليونابى الذي معثاه شعية من الأمعاء 
TAD_pages.txt:465:                  ‫اكلتين وه‬      ‫‏(‪ )١‬ويقولون انما افرنية واصابا بأسبور وهى ا‬
TAD_pages.txt:1167: ‫اوثاره لبجحرى عسلية اللحن‬   ‫‪ 0‬قولون دوزت الغنى القانون ونخوءط شد * ماارنخى من‬
TAD_pages.txt:1681:‫مية فالا كيقولون ‪-‬وبن‬      ‫الفصيح الفاسول” والعامة تسمها لوحا ونون‬         ‫ا‬       ‫‪6‬‬
TAD_pages.txt:1780: ‫والطاولة عندالمامة اسم مطنق بقولون طاولة الجزار وطاو‪1‬الاسكاف وطاولة المراف وتحوذاث‬
TAD_pages.txt:2302:‫قوأنج بست مرض تصيب القولون ممامعآ‪ 1‬اليونابى الذي معثاه شعية من الأمعاء‬
```


## [2026-09-14T01:59:17.304Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf tags\nimport re\ncur=None\nfor i,l in enumerate(lines):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: cur=m.group(1)\n    if 2295<=i<=2315:\n        print(i,'|pdfpage',cur,'|',l)\nEOF"
}
```


### [2026-09-14T01:59:18.540Z] TOOL RESULT

```
2295 |pdfpage None |                                                    ‫وار ‪ 3‬امأقبرماج‬
2296 |pdfpage None | 
2297 |pdfpage None | 
2298 |pdfpage None |            ‫وهو هب للشاه أ‪,‬ضنا‬          ‫وهو مستعمل عندثم تهى غالب وظافر ‪0‬‬
2299 |pdfpage None | 
2300 |pdfpage None | 
2301 |pdfpage None | ‫قوأنج بست مرض تصيب القولون ممامعآ‪ 1‬اليونابى الذي معثاه شعية من الأمعاء‬
2302 |pdfpage None | 
2303 |pdfpage None | 
2304 |pdfpage None |                                           ‫في الاعور واللستقم‬       ‫الغلاظط ا مشحمة وهو‬
2305 |pdfpage None | 
2306 |pdfpage None | 
2307 |pdfpage None | ‫قومندان ايطالي ‪6631‬ة‪«002‬امء بعال لاس امرم أي ءمن م الحنود‬
2308 |pdfpage None |                                      ‫ويدبر السفينة مرادفه أمير وإمام وقائد وريّان‬
2309 |pdfpage None |                                                                ‫ع‬
2310 |pdfpage None | 
2311 |pdfpage None | 
2312 |pdfpage None | 
2313 |pdfpage None | 
2314 |pdfpage None | ‫وهو'لة عار ب ذا تستة وتاك توافق كثارة العيرادة‬               ‫وونانى ‪0‬‬         ‫قيثار‬
2315 |pdfpage None |
```


## [2026-09-14T01:59:21.530Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'قوأنج' in p or 'قولنج' in p:\n        print('LEAF',i)\n        print(p[:1500])\nEOF"
}
```


### [2026-09-14T01:59:22.607Z] TOOL RESULT

```
leaves 87
LEAF 62
                                      ‫د‬    ‫سابةاجم‬




   ‫عمعناه شمعة يستضاء مهامرادفه مصصباح وسراج‬            ‫قنديل ‪ -‬لانيى ‪84‬‬
                                                                              ‫‪1‬‬     ‫‪01‬‬

‫قعل ‪ 5‬ب لاتيبى امه معثاه مشتكاد وراد به فى زماننا تمثل الدولة‬

              ‫«الالنةرعاتون معناه مئوي من «اتاأهعء مائة‬            ‫قنطار لاتينى‬

 ‫متسوب الى ‪80:00212‬و]آ‬             ‫قنطارون وقنطورون ‪ -‬لاتق ‪82‬‬

‫قنطورس اليوناني وهو هولة اي هسك نصفه اسان ونصقه فرص ومعنى قنطورس‬

                             ‫افلييونانية تاخز الفرس وهو ابيحشيشة مر الطم‬
                  ‫قال ‪ 3-3‬لاسى ماله معذأه خجرى الماء مر أدقه وناة وبرعة‬

‫‪0‬قت ‪ -‬وون‪.‬انى وهو ‪1‬خادم الكنيس ‪1‬ة وعرببه ا ‪1‬لنصيح الجللازي وهو‬
                                                             ‫‪0‬لف‬
                                                                                    ‫اه‬
    ‫طًُ‬

                                                               ‫قد‬
                                                                           ‫خادم البيعة‬


‫معناه مدر اأبيت وبراد به أمين الدخل‬                   ‫وونابى ‪5‬‬              ‫قبرمان‬
 ‫ن الفارسيفبو متحوت مقر العرنى ومانالفارسىي ععى صاحت‬
                                                   ‫وار ‪ 3‬امأقبرماج‬


           ‫وهو هب للشاه أ‪,‬ضنا‬          ‫وهو مستعمل عندثم تهى غالب وظافر ‪0‬‬


‫قوأنج بست مرض تصيب القولون ممامعآ‪ 1‬اليونابى الذي معثاه شعية من الأمعاء‬
```


## [2026-09-14T01:59:26.198Z] TOOL CALL #25: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py TAD:59 --image 2>&1 | tail -40"
}
```


### [2026-09-14T01:59:27.293Z] TOOL RESULT

```
no scan of TAD covers printed page 59 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:59:37.329Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON qulun ===\"; grep -n \"قولون\\|قولنج\" MON_part2.txt | head -20; echo \"=== MON kol کل crooked ===\"; grep -n \"کَل\" MON_part2.txt MON_part1.txt | head -10"
}
```


### [2026-09-14T01:59:37.413Z] TOOL RESULT

```
=== MON qulun ===
15806:قولون‌ها حاصل شود و در صورت شدت 
15808:قولنج بطور کلی مربوط ضایعات قسمتهای 
15819:قولنج‌ها در صورت تشخیص ضایعه نام 
15820:مربوط را می‌برند. در هر حال قولنج با دردی 
15826:فراخ‌قولون افقی: (پز.) قسمیت از رودة فراخ 
15830:معده صدای قولون افقی شنیده می‌شود. 
15831:قولون افقی به وسيلهة قسمتی از صفاق بنام بند 
15832:قولون عرضی به سطح خلفی شکم متصل 
15839:طرف چپ قولون که ابتدای قولون نازل 
15840:است ختم می‌گردد. قولون مزبور مانند خطی 
15844:راست تولون که در انتهای قولون صاعد 
15847:دنبالچه‌اش قولون نازل قرار گرفته؛ قولون 
15848:عرضی» قولون سطحی. قولون بالارو: (پز.) 
15849:تولون صاعد. قولون پایین‌رو: (پز.) قولون 
15850:نازل. قولون چپ: (پز.) قولون نازل. قولون 
15851:قاصره‌یی لگنی: (پز.) قولون سینی شکل. 
15852:تولون راست: (پز.) قولون صاعد. قولون 
15853:سطحی: (پز.) قسولون افقی. قولون 
15855:که در دنبالهةٌ قولون نازل قرار دارد. این قولون 
15861:خاصره‌یی لگنی. قولون صاعده: (پز.) 
=== MON kol کل crooked ===
```


## [2026-09-14T01:59:39.657Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQTv3 shalang/shalpuy ===\"; grep -n \"شلپوی\\|شکپوی\\|شگپوی\\|شلنگ\" incoming/BQT/BQT_v3_pages.txt BQT_v2_pages.txt 2>/dev/null | head -20; echo \"=== BQT qulanj ===\"; grep -n \"قولنج\\|قولون\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -20"
}
```


### [2026-09-14T01:59:39.750Z] TOOL RESULT

```
=== BQTv3 shalang/shalpuy ===
incoming/BQT/BQT_v3_pages.txt:1058:9 قی : شلنگه .
incoming/BQT/BQT_v3_pages.txt:4950:‎ima ۷‏ «شلپوی» (ه.م ) ‎Boy‏ شکیوی ۳
incoming/BQT/BQT_v3_pages.txt:5922:‏زن ازخواب شلپوی‌مردی(مردم.دهخدا)شنود.»
incoming/BQT/BQT_v3_pages.txt:6014:- شلنگ ‎cee’‏ ارل و ثالی بروزن
incoming/BQT/BQT_v3_pages.txt:45613:‏نواختن و شلنگه‎ oft ‏و عم که کیران در وفت‎
=== BQT qulanj ===
incoming/BQT/BQT_v3_pages.txt:38974:‎ST‏ - بروزن و معنی قولنج باشد.
incoming/BQT/BQT_v3_pages.txt:38976:کند و بیم هللاکت باشد وقولنج معرب ‎CIS‏
incoming/BQT/BQT_v3_pages.txt:39002:و مقز بادام با فندق پزند » وآنرا ‎AY?‏ یز کویند © ۴ ‎Sa‏ (« م.) ‏ قولنج.
incoming/BQT/BQT_v3_pages.txt:39016:‎٩‏ - رد : قولنج . ‎NE‏ ظ. مصحف «کولح» (ه.م.) ‎Dy‏ : رشیدی .
```


## [2026-09-14T01:59:45.598Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ncur='?'\nfor i,l in enumerate(lines):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: cur=m.group(1)\n    if (5900<=i<=5935) or (6008<=i<=6030) or (4940<=i<=4960) or (38965<=i<=39020):\n        print(i,'|p',cur,'|',l)\nEOF"
}
```


### [2026-09-14T01:59:46.810Z] TOOL RESULT

```
4940 |p 67 | ‏۴ هت شکال (هم.) ‏ شکیل(«.م.)(عر) پای بند ستور (منتهی‌الارب):
4941 |p 67 | 
4942 |p 67 | ‎JK‏ پای ستوران شده سر زلفی
4943 |p 67 | 
4944 |p 67 | ‏۴ شکیل (هم).
4945 |p 67 | 
4946 |p 67 | ‏لایق این تشبیب است.
4947 |p 67 | 
4948 |p 67 | ‏« کلیله‌ورمته مصحح قریب چاپ پنجم ص۲۳۷ .
4949 |p 67 | ‎ima ۷‏ «شلپوی» (ه.م ) ‎Boy‏ شکیوی ۳
4950 |p 67 | 
4951 |p 67 | ‏۰۱ - رگ:شکاونده .
4952 |p 67 | 
4953 |p 67 | ‏.. برهمن گفت: آورده‌اند که درزمین هند شکالی بودازدلیا روی,
4954 |p 67 | 
4955 |p 67 | ‏کزوکره بجز از دست شانه لکشوده.
4956 |p 67 | 
4957 |p 67 | ‏کمالاسه‌عیل. (دبوان‌چاپ‌هندص۱*۸).
4958 |p 67 | 
4959 |p 67 | ‏۴ -وبفتح‌اول = شکال ‏ شقال(ه م.):«وداستان‌شر وشکال
4960 |p 67 | 
5900 |p 79 | وغضب هم میزلند ۴ ۰
5901 |p 79 | 
5902 |p 79 | ‏شلف = بنتح اول و سکون ‎gE‏ فا .
5903 |p 79 | زن بدکاره و فاحثه رااگویند ۴ - ونامرودغاله
5904 |p 79 | ‎Cul‏ در زمین افریفیه ۴ .
5905 |p 79 | 
5906 |p 79 | ‏شلفنه *- پفتح اول بروزن چرمینه ۰
5907 |p 79 | فرج زتالراگویند ؛ ‎ging‏ اول هم گفته‌اند.
5908 |p 79 | 
5909 |p 79 | ‏شلفیه = بفتح اول بر وزن الفیه, بمعنی
5910 |p 79 | ‎aul‏ است که فرج زنان و موضم جاع‌ایشان
5911 |p 79 | باشد ۱ - و ام کتابی هم هست که آدرا القیه
5912 |p 79 | ‎wile‏ میگویند ۷ ؛ و ‎ge‏ اول بجای تحتالی‌نون
5913 |p 79 | هم‌آمده است .
5914 |p 79 | 
5915 |p 79 | ‎٩‏ «دلیوی ‎GL.‏ پای بود درم لرم و عوام کویند ‎GL‏ کلوی خفته بود. بوشکور
5916 |p 79 | 
5917 |p 79 | ‎: ‏کوید‎ (ab)
5918 |p 79 | 
5919 |p 79 | ‏توانگر ‎OF chase‏ خفته بود
5920 |p 79 | 
5921 |p 79 | ‏زن ازخواب شلپوی‌مردی(مردم.دهخدا)شنود.»
5922 |p 79 | « لت فرس ‎COW‏ و رگ : شکیوی » شگیوی .
5923 |p 79 | 
5924 |p 79 | ‏۴ - در تداول امروز «شلخته» شخص بد سلیقه ولاابالی را گویند .
5925 |p 79 | ۴ - ریش نو در کشاکش آن کنده ‎Gh,‏ سبلت بدست ‎oT‏ جلب کس فروش‌شنگه.
5926 |p 79 | 
5927 |p 79 | ‏سوزلی سمرقندی.هفرهنگه نظام» +
5928 |p 79 | 
5929 |p 79 | ‏۴ - در معجم البلدان و حدود نيامده ‎be‏ . مراد شلب ‎dy)‏ حلل الندسية. شکیب
5930 |p 79 | ارسلان ج۱ ص ۱۳6۵ قمری فهرست) وشلیب — ‎Sylves‏ (شپری درپر تقال) ‎dy. ath‏ :
5931 |p 79 | 
5932 |p 79 | ‎. ‏الدهر: فهرست‎ bas
5933 |p 79 | ‏بجان الفیه غلام اورا‎ ae
5934 |p 79 | 
5935 |p 79 | ‏6 رك: شلفیه .
6008 |p 80 | 
6009 |p 80 | see ES ‏بنتح اول بروزن‎ » pols.
6010 |p 80 | ‏حلبه است وآن رستنیی‌باشد محرو ف که شتبلیله‎
6011 |p 80 | ‏لیز گویند وبیونانی فربقه خوانند.‎
6012 |p 80 | 
6013 |p 80 | - شلنگ ‎cee’‏ ارل و ثالی بروزن
6014 |p 80 | پلنکه » برجستن وفروجستن شاطران باشد.جهت
6015 |p 80 | ورزش و مشق راء رفتن بیار برتهجی که ‎By‏
6016 |p 80 | ‏پای ‎OLE!‏ بسرین ابشان میرسد ؛ و بکر اول
6017 |p 80 | و ثانی‌هم ‎aha‏ :
6018 |p 80 | 
6019 |p 80 | ۰ شلوار ‎che a‏ اول بر وزن همواره
6020 |p 80 | آزار و تنبان پاچه کوتاء راکوبند . و منم ‎PIS‏
6021 |p 80 | ‏آهده است.
6022 |p 80 | 
6023 |p 80 | ‎٩ D ght:‏ 2 بنتح اولوضم ثالی‌وسکون
6024 |p 80 | واو و کاف » بمعنی زلو باتد و ‎OT‏ کرمی است
6025 |p 80 | سیاه ‎TES,‏ خون ازیدن یمکد.
6026 |p 80 | 
6027 |p 80 | ‎IS) cal as ۲‏ چبنده ) ورك:شلکا.
6028 |p 80 | ۴ رك : ‎pe‏ (ح) . 4-2 ‎bet:‏ +
6029 |p 80 | 
6030 |p 80 | ‏۱ - از : شلم )= شلفم) + آب+. ‎(eo)‏ رك: شلماب (ح) .
38965 |p 533 | [pdf page 533]
38966 |p 533 | کولاوبان -۱۷۳۹-
38967 |p 533 | کوند که زان ‎ke‏ رشتن شتن را درآن نهند .
38968 |p 533 | 
38969 |p 533 | کولم 4- بقتح اول و ثالث و ‎BU‏
38970 |p 533 | ‏و میم , قلفل ‎ole‏ با کوش ‎Sunol‏
38971 |p 533 | ‏است: .
38972 |p 533 | 
38973 |p 533 | ‎ST‏ - بروزن و معنی قولنج باشد.
38974 |p 533 | ‎oT‏ بادی است که سیب آن شکم و پهلو درد
38975 |p 533 | کند و بیم هللاکت باشد وقولنج معرب ‎CIS‏
38976 |p 533 | ‎clas, - My‏ را نیز گوبند*٩-‏ ونام‌نوایست
38977 |p 533 | از موسیقی .
38978 |p 533 | 
38979 |p 533 | ‎QU be SS‏ مجهول بر وزن
38980 |p 533 | هوشنکه . حیزومخنث و پشت ‎Maa Stal‏
38981 |p 533 | 
38982 |p 533 | ‏کوله - با الی مجهول بروزن ‎ds)‏
38983 |p 533 | ‎aa SLT‏ صیادان در ‎OT‏ نثینند نا سید
38984 |p 533 | 
38985 |p 533 | ‏ممتی ‎GE‏ فارسی هم آمده است ‎٩‏ - و بادی
38986 |p 533 | باشد که آنرا فولنج خوانند ۴ .
38987 |p 533 | کولاویان ‎cee‏ اول و کرواو دویم
38988 |p 533 | ‎olsly Or»‏ + پهلوانان و گردانرا کویند۴ .
38989 |p 533 | کف لح - بروزن ‎ie‏ بععنی‌آعشدان
38990 |p 533 | و منقل باشد ۴ - و با ثالی مجهول دام مردی
38991 |p 533 | بوده تورالی که اسفندیار را از رام هفت خوان
38992 |p 533 | برویینه دز رسالید ‎٩‏ .
38993 |p 533 | کو لغنچه ۱ - بن ‎Jol‏ وغین‌شطه‌دار
38994 |p 533 | وفتح جیم فارسی, ‎Be‏ زنالرا کوبند وآن‌سرخیی
38995 |p 533 | پاش د که برروی مالند ؛ ‎oly‏ معنی باکاف‌فارسی
38996 |p 533 | هم‌آمده است واصح آن است.
38997 |p 533 | کول ۲ - بروزن کودك , کدویرا
38998 |p 533 | 
38999 |p 533 | ‎w= ۱‏ کولاج ۳ کلاج . در فهرست ‎old‏ دیوان بسحاق اطعمه (چاپ‌استانبول
39000 |p 533 | ص ۱۸۲ )آمده : «کلاج » بر کهای پهن که از تشاسته سازند و بهم پیچند و بعد از آن با شکر
39001 |p 533 | و مقز بادام با فندق پزند » وآنرا ‎AY?‏ یز کویند © ۴ ‎Sa‏ (« م.) ‏ قولنج.
39002 |p 533 | - > کولاوبان » پهلوالان کردان باشند از جنس نیکو [کذا] » بارانی گوید :
39003 |p 533 | در بیابان بدید قومی کرد کرده از موی ‎OVS Ge‏ « لفت فری ص ۳۹۵ *.
39004 |p 533 | آقای اقبال در ‎VLE‏ همین صفحه لوشته‌اند: > سابقاً مفرد این لغت بعنی کولارا از همین نسشه
39005 |p 533 | ‎Sai‏ کردیم ( ‎۱٩ bate‏ ) و بازهم ممنی درست این کلمه معلوم نشد .» مولف لفت قری در ذ کر
39006 |p 533 | «کولا» لوبد ‎VS: (VV)‏ زبان کردان ‎‘om‏ بارالی کوید : در بیابان ... » ‎GET‏ دهضدا
39007 |p 533 | دوشته‌اند : این کلمه «شولای امروز است و ظاهراً عبارت این بوده که.« کولا بزبان کردان‌باراتی
39008 |p 533 | بود » و نام ‎ple‏ افتاده است میان « بود » و گوید » و نیز عبارت ص ۳۹4 لفت فرس را چنین
39009 |p 533 | تصحیح کرده‌اند : ‎YS‏ وین باراتی که پهلوانان کردان پوشند از جنس نیکو .»
39010 |p 533 | ۴ - ظ. کولخ است مخفف «کولخن» « ‎pouty‏ » وق سکیلکی ‎kala‏ (متقل).
39011 |p 533 | 6 - در فهرست ولف ‎IS?‏ و «کولخ» نيامده و شخصی که اسفندبار را درهفت خوان
39012 |p 533 | رهنمایی کرد «ک رکار» بود . رك : شاهنامةٌ ‎pe‏ ج ‎٩‏ ص ‎۱۵۸٩‏ بیعد .
39013 |p 533 | 1 رك : گولفنچه . ۲ - در لهچ کرمانی 6018 ( غوزء پنبه ) ‎King?‏
39014 |p 533 | ‎٩ els‏ . 3-4 : طبری ‎tara‏ 801۳2 (خردل) > واژهنامه ‎٩۵4‏ * .
39015 |p 533 | ‎٩‏ - رد : قولنج . ‎NE‏ ظ. مصحف «کولح» (ه.م.) ‎Dy‏ : رشیدی .
39016 |p 533 | ‎MY‏ آن مرد مردگای که کولنک گنک را
39017 |p 533 | در خن فرو برد بکلیدان کون مدنگه
39018 |p 533 | کولنگه پیش او چو نهد سینه برزمین
39019 |p 533 | فرباد و ‎opt‏ دارد چون برهوا کلنگه .
39020 |p 533 | موزلی سمرقندی « رشیدی » ورگ : فرهنگهه نظام -
```


## [2026-09-14T02:00:01.320Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('[pdf page ')\nfor want in ('79]','80]','81]','82]','342]','343]'):\n    for ch in leaves:\n        if ch.startswith(want):\n            head=ch[:400]\n            print('--- pdf page',want, repr(head[:260]))\n            break\nEOF"
}
```


### [2026-09-14T02:00:02.479Z] TOOL RESULT

```
--- pdf page 79] '79]\nos\n\nving \u200fبا بای حظی\u200e - Wd\n\u200fشخصی راکوند که در ابرام افراط کند.\u200e\n\nشلیو ی \u200ebe\u200f بای فارسی بروزن\u200cحفگوی,\nآراز پای را کوبند که بهتگلم راه رفتن بگوش\nآید ۱ .\n\n\u200eSgt\u200f » با واومجهول بروزن مفلولد؛\n\u200ete\u200f راگوبند که هنوز از پوست بر نیاورده\nباشتد و بهندی شالی خوانند.\n\n\u200fشل'
--- pdf page 80] '80]\n۲4 اس\n\nشلك ۱ \u200ecee\u200f اول وسکون الیو کاف»\nزلو را کویند وآن کرمی\u200cباشد سیاء رنگه . چون\nبر \u200eyee\u200f بچسبانند خون از \u200eOT\u200f عضو بمکد -\nو پکسر اول کل \u200eole ta\u200f چسبنده را کویند\nکه چون \u200ech\u200f در آن \u200eat\u200f شودیدشواری\u200cبرآید ۴ .\n\nشلک * = بفتح اول و سکون تانی وکاف\nبالف کشیده. بمه'
--- pdf page 81] '81]\nعلرن\n\nشلون = بنتح اولبروزن زبون ,جالوری\nاست ازجنس شفال - ودر عربی چاروابی را کویشد\nکه کرسته ولافر باشد . و بعضی چاروای فربه\n\u200eys wile,\u200f بعضی چاروابیرا کونند که له فربه\nو له لاغر باشد ۱ .\n\nشله \u200f بنتح اول و نالی مخف . کشتن\nقاتل را \u200eaS\u200f در عوش مقتول و بمربی فص'
--- pdf page 82] '82]\nاد\n\nاست که کنابه از زبان باشد و بعربی \u200eOS\u200f\n\u200eFass\u200f\n\nشمع\u200cزدین لگی «کنابه از خورشیه\nالور باشد .\n\nشمع سچر «کنابه از عمود صبح اول\nاست که\u200cصبححکاذب. باشد- و کنایه از آ فتاب\u200cعالمتاب\nی همست .۰\n\u200eule Che\u200f از خورشید\n\n\u200eple\u200f آراست\n\n\u200eGat inn © SH? “\u200f صباح است\nکه کنابه از'
--- pdf page 342] '342]\n—N\\eta—\n\n\u200eogee gs\u200f ۰ با اول بثانی رسیده\nو میم پالف کشیده وکسر رای فرشت ونای\u200cمثلثه\n\u200eoly\u200f رسیده و پنون زده ؛ بلفت \u200egy\u200f رازبانة\nصحرایی را گویندکه بادبان دشتی است.\n\n\u200fقوم فیل ه اارهباصعاب\u200cالفیلاست؟ .\n\n\u200fقومنی ۴ ۰ با اول بثانی رسیده و کر\nمیم و نون بتحتانی کشیده '
--- pdf page 343] '343]\nبیان نوزدهم\n\nدر \u200eGE\u200f بایای حطی مشتمل بر بیست وشش لفت و کنایت\n\nقیامت کر دن = کنابه از کارهای | که برشتران\u200cگر کین مالند » و صمفی هم هست\nعجیب کردن وکارهای عجایب انگیختن باشد . \u200eole\u200f و چسبنده که ب رکشتی وجهاز مالند تا آب\n\nقیاواد ۱ - با واو بر وزن سزاوار , | ب'
```


## [2026-09-14T02:00:17.766Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('[pdf page ')\nfor want in ('340]','341]','78]','79]'):\n    for ch in leaves:\n        if ch.startswith(want):\n            print('==== pdf page',want,'====')\n            print(ch[:2500])\n            break\nEOF"
}
```


### [2026-09-14T02:00:18.881Z] TOOL RESULT

```
==== pdf page 340] ====
340]
‎oly‏ هفدهم

‏درقاف با ‎gly‏ مشتمل بربست و نه لغت و کنایت

‏قواده ۱ = بنتح ‎Jot‏ و دال بی نقطه
‎tty‏ بالفکشیده , زنیرا گوبشد که بجاها رود
وزنان بجهت مردان بهم رساند » ومرد این کاره
رااکس کش کونند .

‏قواره بر وژن شراره .
که خباط ‎Oly Sj]‏ جامه و پیراهن ‎OT Sealy‏
‎Foyle,‏ - و بمعنی پاره هم آمده است چه
‎LS >‏ کویند ‎old‏ قواره ‎oe‏ پاره پاره
- وانگشتان دست رانیز گفته‌اند ؛ و گوبند ‎wep‏

‎colar sh

‏است,
‏قوت مصیح ‎l=‏ ازشراب ‎eG‏
‏پاشد ۳ . . +
قوت مسیح یکشبه ۴ (۱)-کنابه‌از
خرماست که عربان تعر ‎Arak‏
‎as‏ ۲
99 فر ع با اول ‎i‏ رسیده وای ‎he‏
‏مکور ‎ly‏ قرشت زده ۰ درخت وج باشد ۵
و آنرا ‎ee‏ عودالوج و بفارسی اکر(۳) ترکی
خوانند .
‎VES‏ » بروزن کوچ» کوسفند شاخ

‏(۱) چش:بکشنبه

‎. ‏عربی است‎ - ٩

‎. ‏چش : گویند‎ (x)
> OT ‏اول) » جامه و جز‎ gin) ‏(عر) « فواره کثمامة‎ - ۴

‏دار ‎Se‏ را
کویند .

‏قود -
پروژن مور »
پتبه رااگویند
و بعربی قطن
خوانند ۷ - ِ قوج
ویمعنی خصبه‌هم آمد. است ۸-وکره وبرآهدگی
در ‎Lael‏ و غیر آترا نیز کفته‌الد ‎٩‏ .

‏قودسا بطم اول و سکون ‎att‏ ورای
فرشت و سین بی نقطه بالف کشیده » بیونانی
عود ‎OL‏ کوبند ؛ وبجای سین ای مثلثه هم
‎eae Tl‏ است ..

‏قوریون ‎GV‏ اول ‎gs‏ رسیده
وتحتانی بواو ‎ALT‏ وبنون زده , گشنیزرا گویند
وکزیره همان است .

‏وس » نم اول و سکون ثانی و سین
بی‌نقطه , صومعةٌ ترسابان را کوبند ‎-٩۱‏ و بفتح
اول درعربی کمان باشد ‎MW‏

‏قوسه رز

‏اولوسین بی‌نقطه,بمعنی

‏(۳) خم۱ : اکیر .

‏بریده . او خاص بالادیم - و آنچه از اطراف چیزی بربده باشند - با چیزی اطراف بربده . از

‎ots‏ اضداد است.» «منتی‌الارب».

‏بکشبه. بمنی خرما ونیز می بکشبه » رك : فوت مسیح

‎V‏ فم(هم.). ‎a‏ کیش(معرب).

‏۸ -ظ. محرف غور ‏ غر ( دبه ‎Gee) Cale‏

‏0 ه«اشتینگاس» .

‏ی — ‎ity‏ رشیدی .

‏۴ - دررشیدی « قوت‌مسیح
۵ _ ره : ‎bes‏ حکیم مومن.

‏۲ - (عر) «قوربالفتح» رسن ‎SLs!‏ ولو6«منتهی‌الارب».

‎tty ‏از‎ -* . ac ‏رگ‎ =)

‏۱- (عر) «قوس ‎oll‏ عبادت ‎ME‏ راهبان» «متتهی الارب» .

‏۴- (عر) «قوس بالفتح. کمان .» «منتهی‌الارب *. ‎ep Hagel WF‏ .

==== pdf page 341] ====
341]
es

قوس قرح (۱) است وآنرا کمان رستم و کمان
شیطان هم میگونند .

قووسیا - بر وزن طوطیا . بلفت ‎Bhp‏
‏نام داروست که آنرا بعربی قسط خوانند ۱
وبوی صبر از وی )8( میآید . بغورکردن ‎OT‏
‏در زیر دامن درد رحم را نافع باشد.

قوطولیدون ۴ « با اول وثالث‌بواو
و لام بتحتانی رسیده و دال بی نقطه ‎sly‏ کشیده
و بنون زده » بیونانی ‎ge‏ از رباحین بود
و ‎OT‏ پیوسته سبز میباشد و در بیخهای دبوارها
وجایگاه سایمدار مپروید. گویند نوعی‌ازحی‌المالم
است وبعربی آذان‌القصیس خوانند. وقدح مریم
همان است .

قوطوما -با اون ‎ )۳(‏ فك ‎aly‏
‏رسیده ومیم بالف کشیده ؛ بیونانی بععنیآذربون
ات ۴ ‎ol,‏ بخ خاری‌است که بشیرازی‌چوبك
آشنان خوانشد .

قوفا ؟ با ‎Jy!‏ بثانی رسیده و فای
بالف کشیده ۰ نوعی از صمغ صنوبر باشد وآترا
بعربی علك ‎gal‏ خوانند و بفارسی ‎CASES‏
‏گونند .

قوقالس ۰ با اول بثانی رسیده و قاف
پالف کشیده و کسرلام ر سکون سین پی ‎cadet‏

(۱) چش: قوی وقرح.

‎dle )۷(‏ . چش : او .

‎—\ota—

‎By, ah‏ بمعنی ترخر است که لوعی از ترب
صحرایی باشد ۵ . خوردن ‎OT‏ بادها رابشکند.

‎ne Vp‏ اول و سکون تانی
و اف و نون مضموم بین بی ‎Ha‏ زده ۰ بمعنی
قفنس است وآن مرفی باشد بغابت عجیب‌وغریب.
گویند هزار ‎wy JE‏

‏قوقنوس ۱ ‎b=‏ زبادتی واو بعد از
نون ۰ بمعتی قوقتس است که بققنس‌شهرت‌دارد.

‎«aly ‏نم دو قاف وسکون دو‎ - SP
‏وامثال‎ gla Sy WSLS ‏فوقه است که‎ cae
. ‏باشد‎ ot

‎OP‏ - منم اول و فتح ‎SU‏ بمعنی
قوقو است که ‎WT LG‏ و پیراهن و امثال ‎OF‏
‏باشد .

‎NS ‏اول بثانی رسیده و‎ Le gh
‏بتحتانی کشیده .گویند حیوانی است دریابی که‎
‏اوست و اورا ببدستس‎ Lat ‏جند یعنی آش بچها‎
‏کوبند ۷ . کوشت آن حیوان صرع را نافع‌است.‎

‏قول کاسه گر - نام تولیاست ازتولبای
موسیقی, یمنی تصلیقی است .

‎A Gal gh‏ »ینم اول و کسرلام وسکون
نون وجیم » معرب گولنج است که دردشکم‌ودرد
پهلو باشد.

‏(۳) چش : باول .

‏٩-ظ: ‎Les‏ (عر) ‎costus=‏ . رك : انتینگاس و رله : ‎bins‏ حکیم مومن.

‏۴ از بوتانی 000010060 « ائتیشگاس >.

‎lane 4)"‏ حکیم مژمن.

‎+ ‏ازربة ممری‎ KOPHE yi! ‏و کسر سوم وبای مشدد)‎ dale) ‏قوفی‎ DF
FANE AVG ‏نوعی بخور مر کب از مواد متعدد از جمله صنوبر , بسیب بوی خوش‌آن * دزی‎

‏رك: ‎tes‏ حکیم ممن .
‎bins»‏ حکیم مومن > .

‎٩‏ _ « فوفالس نوعی از دوقواست و نزد بسنی تخم کرفی است.*
‎ay‏ - رك : ققنس -

‏۷ - رك : ‎tins‏ حکیم مومن .

‏۸ ح کولنج ‎Cpe)‏ معرب ازبونانی 1۵11845 «زابا س‌م۳۱» ‎(colon = kdlon}))‏
(فر) ‎clans)‏ ازامعاء‌غلاظ بیناءورومتقيم «نفس») فولنج مرضی است آلی که درامعاء غلاظ بجهت
احتباس غیر طبیمی حاصل شود و درد آرد وگاه قوی کردد و بکقد بخلاف صداع «بحرالجواهر»

‎. (4) colique = «ste»

==== pdf page 78] ====
78]
را
شگفت ۰۱ ,کر ‎Js)‏ والی بر وزن

کرفت » بمعنی عجب و تهعجب باشد ۴ .

شگل ۴ - بکر اول و انی و سکون
لام « چداری باشد کوچك که هر دو دست اسب
و استر را بدان محکم بنداد - و ریسمالیرا بیز
کویند که بریای ‎Ciel‏ بندند.

شگن © بنم اول و ثالی وسکون دون 6

مخفف شگون‌است ۴ که فايك و بفال برداشتن
و میمنت داستن چیز ها بائد مثل پرواز وآواز
مرغان و حرکات و سکنات آدمیان و رحوش
وامنال اسان

شگون ۱ - بنم ال بر وزن سکون »
بمعنی شگن است که فال ليك - و بفالبرداشتن
ومبارك دالتن چیزها ,اشد .

بیان هبحدهم

در شین لقطه دار با لام مشتمل بر بیست وشش لفت

شل = ‎ch‏ اول و سکون نالی » پوست
‎Ash‏ رنگیتی را کوبند که در ‎Ole‏ درز کفش
و موزه و براق زين اسب نهاده بدوزند بجهت
خوشآبند کی و بمضی از براق اسب را نیز ‎OF‏
‏دوزدد - و رانآدمی راگویند خصوصاً وران‌سابر
حیوانات را ءموماً ۷ - و بعربی دست و-یای را
گویند که از کار پازمانده باشد ۸ - و ‎pin‏ اول

‎Oar‏ لرم ر ست را کوبند ‎٩‏ - و بکر اول
بیزة کوچکی است که آبراکاهی دویرء و سهیره
سازند و پنج و ده آلرا بردست گیرند و يك يلك
را بجالب دشمن اندازند*٩‏ - ومیوه‌ای باشد گرد
و مدور ‎asl‏ بهی وطمم آن نیز باتلخی آميخته
‎ack‏ وآترابهندی بیل کویند واز آن مربامازند؛
و باین معنی بضم اول هم آمده است.

‎shigift ‏حبرت انگیز) رفدشکفتن.‎ + cme) 560/8 ‏(هم.) پهلوی‎ cae ٩
‏«پارتولمه‎ skapta - ‏همربشه است . قس:ريشة اوستابی‎ Lan. shkuft ‏با‎ ۶ shiguft ‏از‎
‎: ‏ممجزه‎ gam - ۴ . ۰۷۱۹ ‏«یب رکه‎ (Come) 510811 ‏ایرانی میاله‎ ۹
۰ ۸۸ ‏آورید ...۰ «انجیل فلرسی‎ gat Olea ‏بدوکفت نا آبتها و شگنتها دی بینید‎ ae?

‏۴ شگال ‎See‏ , شکیل .
‎gel - ©‏ زهره خیره‌بن ازحسنشان

‏۴ رك : شگون .

‏مشتری از ‎Clery,‏ گیرد شگن ۰
مولوی بلخی. «فرهنگه‌ظام».

‎Shkund ©, Sol. ۱‏ ( پرنده, مخصوصاً پرنده‌ای که خوش یمن با شوم باشد)

‎SEENON ‏وبلیامز‎ >

‏۲ - فی: ‎Sais‏ , شلوار . «اسشق - هوبشمان ۰۷۸۹ .

‏۸ - شل (بفتح‌اول‌ونشدید دوم) مصدراست بمعنی نباء شدن دست‌وخدك کردیدن ,واشل
یفتح اول ودوم وندید سوم , مردتباه دست (منتهی الاب ) و شل بمعنی آخیر صرفنی است اژ
ایرایان ‎LB»‏ اشل عربی ‎Guilty‏ هم مسدر جعلی آنست .

‎٩‏ - چون‌بدیدآن روی هچون بر که کل

‏متطرب گردید و شد پاهاش شل .
مولوی بلخی «عثنوی».

‏۴ - درهند سیل کویند بسین مپمله وبای مجپول «بپارعجم» :

‏1246 اففایان ‎cap‏ وتیز

‏چودسته بسته بهم‌نپر‌هاي بی‌سوفار

‏« فرخی.-رستانی۱۳* .


==== pdf page 79] ====
79]
os

ving ‏با بای حظی‎ - Wd
‏شخصی راکوند که در ابرام افراط کند.‎

شلیو ی ‎be‏ بای فارسی بروزن‌حفگوی,
آراز پای را کوبند که بهتگلم راه رفتن بگوش
آید ۱ .

‎Sgt‏ » با واومجهول بروزن مفلولد؛
‎te‏ راگوبند که هنوز از پوست بر نیاورده
باشتد و بهندی شالی خوانند.

‏شلته = با اول مفتوح و سکون ‎Carel‏
‏فوقالی .جای مردار وناپاك را گوبند .منی‌موضعی
که در آن سرکن و ‎sol‏ و خاکروبه وامثال
آن ریز لد -

‏شلخته - با اول و ثالی مفتوح وسکون
خای قطمدار و قتح ‎ol‏ قرشت » لگدی باشد

‏سیر ات

‏که مردم دروفت بازی کردن با پشت پای با سر
‎gis‏ بر نرمگاه و شتگاه مکدیگر زشدوآترا
شلخت بحذف‌ها نیز گفته اند و کاهی ازروی‌قپر
وغضب هم میزلند ۴ ۰

‏شلف = بنتح اول و سکون ‎gE‏ فا .
زن بدکاره و فاحثه رااگویند ۴ - ونامرودغاله
‎Cul‏ در زمین افریفیه ۴ .

‏شلفنه *- پفتح اول بروزن چرمینه ۰
فرج زتالراگویند ؛ ‎ging‏ اول هم گفته‌اند.

‏شلفیه = بفتح اول بر وزن الفیه, بمعنی
‎aul‏ است که فرج زنان و موضم جاع‌ایشان
باشد ۱ - و ام کتابی هم هست که آدرا القیه
‎wile‏ میگویند ۷ ؛ و ‎ge‏ اول بجای تحتالی‌نون
هم‌آمده است .

‎٩‏ «دلیوی ‎GL.‏ پای بود درم لرم و عوام کویند ‎GL‏ کلوی خفته بود. بوشکور

‎: ‏کوید‎ (ab)

‏توانگر ‎OF chase‏ خفته بود

‏زن ازخواب شلپوی‌مردی(مردم.دهخدا)شنود.»
« لت فرس ‎COW‏ و رگ : شکیوی » شگیوی .

‏۴ - در تداول امروز «شلخته» شخص بد سلیقه ولاابالی را گویند .
۴ - ریش نو در کشاکش آن کنده ‎Gh,‏ سبلت بدست ‎oT‏ جلب کس فروش‌شنگه.

‏سوزلی سمرقندی.هفرهنگه نظام» +

‏۴ - در معجم البلدان و حدود نيامده ‎be‏ . مراد شلب ‎dy)‏ حلل الندسية. شکیب
ارسلان ج۱ ص ۱۳6۵ قمری فهرست) وشلیب — ‎Sylves‏ (شپری درپر تقال) ‎dy. ath‏ :

‎. ‏الدهر: فهرست‎ bas
‏بجان الفیه غلام اورا‎ ae

‏6 رك: شلفیه .

‎: ‏شلف‎ : GGT
. ‏او را‎ plas ‏نخورد. شلفیه‎

‎. ‏اییوردی در متایشآلت قاضی کیراکه «فرهنگگ نظام»‎ ergs!
‏الفیه وشلفیه , از حکیم ازرقی شاعر » که آلرا برای پادشاه نبشابور طوغان شاه‎ —

‏(طفان شاء ) یس ‎pls‏ طوغرل ‎(Sab)‏ سلجوفی
که وی مبتلا ‎inn‏ باه‌شده بودتاوی از آن کتاب بهره مند شود و کتاب

‎op je‏ شامل ‎oop able‏ درباب زلی که کوبی هزارمرد با اوآ ميزش کردند

‏تألیف کرد آنگاه

‎3

‏و کتایرا بااشکال مختلف مصور کرد. ودرعلم باه آمده که ظربامثالاین
کتاب محر کی‌است قوی برای‌باء « کذف‌الظنون»: الفیه وشلفیه» -

‎ce ‏هاغم‎ 0
shalam ‏طیری‎

‏بفتح اولوسوم = شملغ ‎glass‏ مخفف‌آن « ‎AG “¢- meer‏

‏> واژه نامه 4۸۳ » معرب ‎oF‏ شلجم « نفی © =

‎pe ‏وربشة‎ OVA CIT IS? ‏کیاهی $5551 چلیپائیان‎ Brassica napus
. ۱۰۹ ‏شکلی دار دکه خوراکی است . رك : ستوده‎ Sp
```


## [2026-09-14T02:00:54.467Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON1 کل ===\"; grep -n \"^کل \\|کل (\\|کل\\b.*کج\\|کل .*خمیده\" MON_part2.txt | head -20; echo \"--- search kaj/khamide near کل\"; grep -n \"کج و خمیده\\|خمیده و کج\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-14T02:00:54.562Z] TOOL RESULT

```
=== MON1 کل ===
418:مشکل (سخ؛ کلام)؛ مة. واضح)؛ ج 
3006:کل گوسفند (از لفظ خود واحد ندارد. یکی 
4293:کل 
7242:کل خود. نوعی طعام زچه که از دانه شنبلید 
13103:کل تهی کردن شکم. قصاء حاجت رفتن: 
16061:حتی الکل (هنگام مستی) بکار می‌رود. قهوة 
21111:کلاه خود را کج بر سر می‌گذارد. (کن.) 
21113:یا ناز و ادا کلاه را کج بر سر نهد. 
22864:کلیدان افتد و محکم شود. پری سیاه و کج بر 
24400:کل ها (یز نره گاو و گوسفند نر) (.) نرینة 
24408:کل: ۲0۱ (کج؛ منحنی] (ص.) منحنی» کج. 
24417:کل کسی شدن: طفیلی وی شدن» انگل وی 
24432:کل است؛ موجود در خارج است اما کلی از 
24660:کلاک: ۲۵ (.) چوب دراز سر کجی که 
26849:قوی هیکل (فیل). ضح.- در فهرست و لف 
26893:بزرگ جثه (فیل)» وی هیکل (پیل). 
27055:کل که زر و نارس رآسته که نوش 
28319:کل 
29134:کل زو تست بانید: رگک» گس مکر؛ خن خنگک 
32781:کل راطخا کسردون: 
--- search kaj/khamide near کل
MON_part2.txt:26258:سوراخ کند. چوب کج و خمیده‌ای به شکل
```


## [2026-09-14T02:00:57.052Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== silandr ===\"; grep -n \"سیلندر\\|سیلندر\" MON_part2.txt MON_part1.txt | head; echo \"=== BQT hax هخ ===\"; grep -n \"هَخ\\|^هخ\" incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head; echo \"=== FRS shalpuy ===\"; grep -n \"شلپوی\\|شکپوی\" FRS_pages.txt FRS.txt 2>/dev/null|head"
}
```


### [2026-09-14T02:00:57.164Z] TOOL RESULT

```
=== silandr ===
MON_part2.txt:17546:بنزین و هوا را برای اشتعال در سیلندرها تهیه . 
MON_part2.txt:29255:و تبدیل شدن به بخار و ورود در سیلندر و 
MON_part2.txt:88582:از یکساعت ویروس سیلندر اکس‌های 
MON_part1.txt:29632:داخل سیلندرها می‌شود زیاد و کم نماید. 
MON_part1.txt:34604:با اصطکاک در لول تلمبه پا سیلندر ماشین 
MON_part1.txt:34609:توپری است داخل لولةٌ دیگری بنام سیلندر 
MON_part1.txt:34611:هوا و بنزین) در ناحیة سر سیلندر (قسمت 
MON_part1.txt:34612:فوقانی پیستون) بستون در داخل سیلندرها 
MON_part1.txt:34623:داخل لولةً سیلندر به نوبةٌ خود به حرکت 
MON_part1.txt:60948:که در سیلندرهای اتومبیل داخل می‌شود 
=== BQT hax هخ ===
incoming/BQT/BQT_v4_pages.txt:16180:هخامنشی(ه.م.) وجد اعلای کورش ودارپوش امت .
=== FRS shalpuy ===
```


## [2026-09-14T02:01:02.713Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24395,24420p' MON_part2.txt; echo \"=== qulun MON context ===\"; sed -n '15795,15812p' MON_part2.txt"
}
```


### [2026-09-14T02:01:02.818Z] TOOL RESULT

```
ککه‌ناک: ۲-2 (ص‌مر.) آلوده به فضلهة 
آدمی. 

کل: ۱ [قس. کچل] (ص.) کچل. 

کل ها (یز نره گاو و گوسفند نر) (.) نرینة 
حسوانات غو ما . گاومیش نر. (جاد.) 
پستانداری است از راستةٌ نشخوا رکنندگان از 
دستةً تهی‌شاخان و از نوع آهو. برخی از 
گونه‌های این حبوانات فاقد شاخند ولی اکثر 
گو نه‌های آن دارای شاخه‌های طویل و پیج 
و خم‌دار می‌باشند؛ ذب الریاد» کلاهو. 

کل: ۲0۱ (کج؛ منحنی] (ص.) منحنی» کج. 
کجیی انحناه. 

کل: ام (۱.) ده» روستا. 

کل: ا۲ | - کله. کو تاه» کند] (ص.) کو تاه. 
ناقص. کند) مق. تیز. 

کل: (0اه! [ع.] (.) گرانی» گرانجان بی‌خیر. 
کل کسی شدن: طفیلی وی شدن» انگل وی 


۱۳ «۴ 
=== qulun MON context ===
(امر.) مهتر غلامان» رئیس غلامان. 
فول‌نامه: (م)مقه(اجممآنتهر (ع. ف.] 
(امر.) ورقه‌ای که خریدار و فروشنده به 
یکدیگر دهند پیش از معاملةٌ قطعی تا در 


۷۴ ۱ 
فاصلهً بين قول و معاملة قطعی فروشنده مورد 
مطالعه را به دیگری نفروشد و خریدار سر 
فو لنج : (لها«مآمهاتا (معر.] (۱.) (بز.) 
دردی که غفلتاً در ناحیهٌ شکم خصوصاً 
قولون‌ها حاصل شود و در صورت شدت 
ممکن است به مرگ منتهی گردد. عارضة 
قولنج بطور کلی مربوط ضایعات قسمتهای 
مختلف احشاء است و ممکن است مربوط به 
عفونت يا سوراخ شدن آپاندیس باشد که در 
این صورت دردها بیشتر در ناحیه تحتانی 
راست شکم و حول و حوش ناف است و
```


## [2026-09-14T02:01:10.180Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T02:01:10.188Z] TOOL RESULT

```


```


## [2026-09-14T02:01:14.231Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%84%D9%88%D8%A7%D8%B1",
 "prompt": "Give the full etymology section for Persian شلوار (šalvâr) 'trousers': the Middle Persian / Old Iranian forms, any connection to a word for 'leg/thigh', Greek σαράβαρα, Arabic سروال, and cited sources."
}
```


## [2026-09-14T02:01:16.233Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%E1%BF%B6%CE%BB%CE%BF%CE%BD",
 "prompt": "Give the etymology of Ancient Greek κῶλον 'limb, member' and also what it says about κόλον 'large intestine' — are they the same word or separate? Any PIE root given?"
}
```


### [2026-09-14T02:01:20.139Z] TOOL RESULT

```
# Persian Etymology of شلوار (šalvâr)

## Middle Persian and Proto-Iranian Origins

According to the Wiktionary entry, Persian شلوار derives from Middle Persian with the form "šlwʾl /⁠šalwār⁠/, meaning 'trousers'". This Middle Persian term was itself a borrowing from Proto-Scythian *šalawāri.

## Ancient Language Connections

The entry does not provide information about connections to words meaning "leg" or "thigh" in the reconstruction. However, it does document the word's widespread adoption across multiple language families through historical contact.

## Related Forms in Other Languages

The Wiktionary article lists several related terms appearing in neighboring linguistic systems, including Greek σαλβάρι (salvári) and Arabic سِرْوَال (sirwāl), though it doesn't explicitly connect these to a common etymon beyond the Persian source.

## Cited Sources

The Persian section references works by David Neil MacKenzie's *Concise Pahlavi Dictionary* (1971) and Johnny Cheung's *Etymological Dictionary of the Iranian Verb* (2007), which provide historical documentation of the term's development within Iranian language families.
```


### [2026-09-14T02:01:21.301Z] TOOL RESULT

```
# Etymology of Ancient Greek κῶλον

## Etymology and PIE Root

According to the Wiktionary entry, the word has traditionally been traced to Proto-Indo-European **(s)kel-**, though this attribution is disputed. The entry notes: "Traditionally derived from Proto-Indo-European _(s)kel-_, but Beekes favors a Pre-Greek origin."

## Regarding κόλον (colon/large intestine)

The page does not discuss κόλον meaning "large intestine" at all. It only covers κῶλον meaning "limb" or "member." However, the entry does list an alternative form **κόλων** (kólōn) at the top, suggesting these may be variant spellings of the same word rather than distinct terms.

The descendants section indicates the term evolved into Latin **cōlon**, which would eventually give rise to the anatomical term for the large intestine in modern languages—but this semantic shift is not explained in the provided content.
```


## [2026-09-14T02:01:27.849Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CE%BB%CE%BF%CE%BD",
 "prompt": "Etymology of Ancient Greek κόλον 'large intestine, colon': what origin is given, is it related to κῶλον 'limb', and what descendants (Latin colon, Arabic) are listed?"
}
```


## [2026-09-14T02:01:29.255Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/colon",
 "prompt": "Give the full etymology entries for colon (punctuation mark) and colon (large intestine), including the Greek words kolon / kōlon and any note about whether they are the same word."
}
```


### [2026-09-14T02:01:32.899Z] TOOL RESULT

```
# Etymology of Ancient Greek κόλον

**Origin:** The etymology is uncertain. Modern scholars like Beekes propose connections to words meaning "guts" or "bowels," while Furnee links it to various related intestinal terms. Hellenistic grammarians suggested connections to unrelated words like "flatterer" and "crooked."

**Relation to κῶλον:** The entry explicitly states: "No relation to κῶλον (kôlon, 'limb')."

**Descendants:** The Wiktionary article lists three main descendants:
- Modern Greek κόλον (learned borrowing)
- Latin *colon* (with further descendants noted elsewhere)
- Classical Syriac ܩܘܠܘܢ (qōlōn)

Notably, no Arabic descendant is mentioned in this entry, though the Latin term spawned numerous Romance language descendants through separate documentation.
```


### [2026-09-14T02:01:34.821Z] TOOL RESULT

```
# Etymology of Colon

## Colon (Punctuation Mark)

From the 1540s, this term derives from Latin *colon* meaning "part of a verse or poem," which came from Greek *kōlon* literally meaning "limb, member" (particularly a leg or tree limb). The Greek word also had a figurative sense of "a clause of a sentence," though its ultimate origin remains uncertain. The meaning evolved from "independent clause" to the punctuation mark that sets one off.

## Colon (Large Intestine)

Dating to the late 14th century, this anatomical term comes from Latin *colon*, a Latinized form of Greek *kolon* (with a short initial *o*) meaning "large intestine." The source notes this Greek word's origin is "unknown."

## Same Word or Different?

While both English terms share the name "colon," they appear to derive from related but distinct Greek origins: *kōlon* (with a macron) for the punctuation mark versus *kolon* (with short *o*) for the anatomical structure, though both passed through Latin before entering English.
```


## [2026-09-14T02:02:05.102Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Scythian/%C5%A1alaw%C4%81ri",
 "prompt": "What does this reconstruction page say about Proto-Scythian *šalawāri 'trousers' — its internal etymology (any element meaning 'leg/thigh'?), descendants (Middle Persian, Greek σαράβαρα, Arabic sirwāl), and sources cited?"
}
```


## [2026-09-14T02:02:08.072Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index skel/shal/kol ===\"; grep -n -i \"SKEL\\|SKENG\\|KOLON\\|KULINDEIN\\|SKELOS\" incoming/ARY/ARY_latin_index_pages.txt | head -20; echo \"=== ARY persian شلوار شل کل ===\"; grep -n \"شلوار\\|شلنگ\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-14T02:02:08.147Z] TOOL RESULT

```
=== ARY latin index skel/shal/kol ===
10324:(DROP) 111, (TEAR) 136 SRSKEL ARMENIAN) go \
13543:MUSKEL (GERMAN) git (GREER)-Jhiy « gl
13547:MUSKEL SWEDISH) (628 yo MUSCULO SPANISH) glee!
13548:MUSKEL :(NORWEGIAN) «$39 5 MUSCULO. A(ITALIAN) git
=== ARY persian شلوار شل کل ===
13476:چم این واژه در زبان پروسی کهن: شلوار ۰
```


### [2026-09-14T02:02:10.616Z] TOOL RESULT

```
# Proto-Scythian *šalawāri Analysis

**Internal Etymology:**
The page notes the etymology is "Uncertain; possibly from *šali ('leg, thigh')" (cognate with Persian šal) plus "*wāri ('covering, enclosure')" from Proto-Iranian *wā́rah. The word is thus theorized as a compound meaning "leg covering."

**Descendants:**
The term produced a rich linguistic legacy:
- Achaemenid Elamite: šá-ir-ba-la-ad-da
- Ancient Greek: σαράβαρα (sărắbāră, described as "Scythian loose trousers")
- Middle Persian: šalwār (via Book Pahlavi)
- Classical Persian: شلوار (šalwār)
- Aramaic and Syriac variants
- Arabic: سِرْبَال (sirbāl)

**Sources Cited:**
The page references Johnny Cheung's 2017 work on Iranian borrowings in Qurʾānic Arabic and his 2007 *Etymological Dictionary of the Iranian Verb* published by Brill, which discusses the root meaning "to cover."
```


## [2026-09-14T02:02:18.546Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN isosceles ===\"; grep -n -o \"isosceles.\\{0,320\\}\" KLN_1971.txt | head -3; echo \"=== KLN cylinder ===\"; grep -n -o \"cylinder, n\\..\\{0,400\\}\" KLN_1971.txt | head -3; echo \"=== KLN calender ===\"; grep -n -o \"calender.\\{0,400\\}\" KLN_1971.txt | head -4; echo \"=== KLN colon ===\"; grep -n -o \"colon, n\\..\\{0,450\\}\" KLN_1971.txt | head -4; echo \"=== KLN shank ===\"; grep -n -o \"shank, n\\..\\{0,350\\}\" KLN_1971.txt | head -3"
}
```


### [2026-09-14T02:02:19.739Z] TOOL RESULT

```
=== KLN isosceles ===
127405:isosceles, adj., having two equal sides (said of a 
244859:isosceles-triangular faces {geom.) — Com- 
253663:isosceles, 
=== KLN cylinder ===
62639:cylinder, n. — F. cylindre, fr. L. cylindrus, fr. Gk. 
=== KLN calender ===
37227:calender, n., a mendicant dervish. — Pers. 
37230:calender, n., machine with rollers for pressing 
37231:calender, roller, mangle’, 
37234:calender, tr. v. — F. calandrer, fr. calandre. See 
=== KLN colon ===
51054:colon, n., that part of the larger intestine, which 
51060:colon, n., the punctuation mark: — L. colon, fr. 
51070:colon, n., the monetary unit of Costa Rica. — 
217525:colon, n., a punctuation mark (;). — A hy- 
=== KLN shank ===
219866:shank, n. — ME. schanke, shanke , fr. OE. scanca,
```


## [2026-09-14T02:02:21.952Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 127405 62639 37227 51054 219866; do echo \"===== line $n =====\"; sed -n \"${n},$((n+12))p\" KLN_1971.txt; done"
}
```


### [2026-09-14T02:02:23.056Z] TOOL RESULT

```
===== line 127405 =====
isosceles, adj., having two equal sides (said of a 
triangle). — L., fr. Gk. Eoomc eXifc, ‘equal- 
legged’, fr. Eao?, ‘equal’, and ax£Xoc, ‘leg’. For 
the first element see iso-, for the second see 
scalene and cp. triskelion. 
isothere, isotheral, n., a line connecting places on 
the earth’s surface having the same mean sum- 
mer temperature (phys. geogr.) — Compounded 
of iso- and Gk. &£po<;, ‘summer, harvest’, which 
is rel. to ^epp.6;, ‘warm’, &6pp.v), ‘heat’. See 
therm. 

isotherm, n., a line connecting places on the 
===== line 62639 =====
cylinder, n. — F. cylindre, fr. L. cylindrus, fr. Gk. 
xuXtvSpoo, Toller, roll, cylinder’, fr. xuAlvSeiv, 
‘to roll’, which prob. derives fr. I.-E. base 
*(s)qel ‘to bend, twist’, whence also Gk. 
xuAA6<; (for *xuX-vo?, *xsXvo?), ‘crooked, crippl- 
ed’, xg5Aov, ‘limb, member; member of a clause 
or a sentence’. See colon, ‘punctuation mark’, 
and cp. calender. Base *q w e-q w los , reduplication 
of base *qel~, ‘to bend, twist’, appears in OI. 
cakrah, Gk. xuxXos, ‘cycle’. OE. hweogol, hweol , 
‘wheel’. See wheel and cp. cycle. 

Derivatives: cylinder , tr. v., cylinder-ed, adj., 
===== line 37227 =====
calender, n., a mendicant dervish. — Pers. 
qalender. 

calender, n., machine with rollers for pressing 
cloth. — F. calandre, ‘calender, roller, mangle’, 
fr. earlier *colandre, fr. VL. *colendra , fr. Gk. 
xuXiv&pog, ‘roller, cylinder’. See cylinder, 
calender, tr. v. — F. calandrer, fr. calandre. See 
prec. word. 

Derivative: calender-er, n. 
calends, kalends, n. pi., the first day of the an- 
cient Roman month. — ME. kalendes, fr. OE. 
===== line 51054 =====
colon, n., that part of the larger intestine, which 
extends from the caecum to the rectum (anat.) 

— L., fr. Gk. x6Xov, ‘large intestine*, which is 
of uncertain origin. 

colon, n., the punctuation mark: — L. colon, fr. 
Gk. xa>Xov, ‘limb, member; member of a clause 
or a sentence*, which is rel. to xtdXid, xa>X^, 
‘thighbone’, and cogn. with OSlav. koUno, ‘knee*, 
*dlinu (fr. *£elnti), ‘limb, member’ (whence 
Russ., Czech (den, of s.m.),'Liih. kelps, Lett .-cells, 
‘knee*, fr. I.-E. base *(s)qel -, ‘crooked, bent’, 
===== line 219866 =====
shank, n. — ME. schanke, shanke , fr. OE. scanca, 
sceanca, ‘leg’, rel. to MLG. schenke, to the 
diminutives MDu. scenkel , Du. schenkel, MHG. 
G. schenkel, ‘shank, leg’, and to Du. schonk , ‘a 
bone’, G. Schinken, ‘ham’ ; fr. I.-E. base * sqeqg -, 
‘slanting, obljque, tq limp’, whence also OI. 
khdhjati, ‘limps’, Gk. oxa^ctv (for *sqygyein), 
‘to limp’, ON. skakkr , ‘lame, crooked’, ON. 
hinka , OHG. hinkan , MHG., G. hinken , ‘to 
limp’. Cp. scazon, skate (for gliding over ice), 
skink, ‘to serve’. Cp. also the second element in 
nuncheon.
```


## [2026-09-14T02:02:46.406Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM qulanj ===\"; grep -n \"قولنج\\|القولنج\\|قولون\" AFM.txt AFM_pages.txt 2>/dev/null | head -6; echo \"=== LAT colon ===\"; grep -n -o \"colon .\\{0,300\\}\\|cōlon.\\{0,250\\}\" LAT.txt | head -5; echo \"=== SKT shank/colon ===\"; grep -n -o \"Shank.\\{0,260\\}\\|Colon.\\{0,260\\}\\|Cylinder.\\{0,260\\}\\|Calender.\\{0,200\\}\" SKT.txt | head -8"
}
```


### [2026-09-14T02:02:47.600Z] TOOL RESULT

```
=== AFM qulanj ===
AFM.txt:282:وقد سحل من ܝ واهل ܦ يقولون بازاناً الحوض الذي 5 العين عند 
AFM.txt:1093:(اللقار )وهر ات ف بلخشان ٠‏ والعجم يقولون له بدخشان (شفاء الغليل) ٠‏ 
AFM.txt:1107:( البالنَاء) الأكارع في لغة اهل الديئة يقولون أكلنا البالغاء وهو معرب ` 
AFM_pages.txt:173:وقد سحل من ܝ واهل ܦ يقولون بازاناً الحوض الذي 5 العين عند
AFM_pages.txt:672:(اللقار )وهر ات ف بلخشان ٠‏ والعجم يقولون له بدخشان (شفاء الغليل) ٠‏
AFM_pages.txt:681:( البالنَاء) الأكارع في لغة اهل الديئة يقولون أكلنا البالغاء وهو معرب `
=== LAT colon ===
=== SKT shank/colon ===
2629:Calender,  a  mathme  for  preiiing  cloth; lee  Oy Under.
3714:Colon.
3733:Colon  (i).  a  mark   (:)   in  writing  ud printing.    (Gk.)      Gk.  jruXof,   a    daoKj hence  a  stop  marking  on*  a  clause- Colon  (2),  part  o?  the  intestines.  (GLj Glc  KoiKov,  the  same.
3735:Colonel,  Colonnade ;  «ee  Column.
3736:Colony.    (F.  -  L.)      F.   c^lank. cohnia,   a   colony,  band   of   bus' —  L.  ccionuj,  a  husbandman.  wLk till.
4494:Colony. Onlv«r  •  d"^
12308:Shank. ITimxy,  a  simpleton.  (Ital.)  Ital.  m'lifw, .1  child  (I)iez).  Cf.  Span.  niAo,  a  child, one  of  little  experience.  —  Ital.  ninna,  a lullaby,  nnrse's  song  to  lull  children  to sleep,  also  written  nattna.  Of  imitative origm.
17377:Shank.  Thus  scotches  or  skates  are '  shanks,'  contrivances  for  lengthening  the stride ;  cf.  F.  khasse,  a  slilt,  also  from  Du schaats.
```


## [2026-09-14T02:02:47.934Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in (569,570):\n    print('==== leaf',leaf,'printed ~',leaf-5,'====')\n    print(pages[leaf-1][:1800])\nEOF"
}
```


### [2026-09-14T02:02:49.142Z] TOOL RESULT

```
==== leaf 569 printed ~ 564 ====
564                                           S(q)en, (s)qan    — sqeng-
Haut, Membrane*'                   Av, scandayeiti „zerbricht, vernichtet (die
                                   {sg[end-n-).
Schlachtreihen)**, slcdnda--m. „Zerspaltung, zerstoren**;
   gr. vermutlich in oxevdvkrj, ox^vdvlri wahrscheinlich ,,ZaDge“ (LidenaaO.;
anders, aber verfehlt Ifiedermann IF. 15, 108f.).
   Ygl. mit a-Vokalismus mir. scandraim „zerspalte‘*, scandrad, scaindred
„dispersion**, scainner, PL scaindrecha etwa ^Yernichtungskampfe** (: cymr.
ysgytJim „to lop**; Stokes BB. 23, 59, Zupitza aaO.; Zweifel bei Giintert
Abl. 56); aksL skqda „defectus** (Johansson PBrB. 14, 337; idg. a? aksl.
skqd^ „arm, klein**, UqdUi „sparen, schonen**, Persson aaO., liegen in der
Bed, recht weifc ab c^sth „Teir* zu lit. hdndu „bei6en**, dessen Sippe nieht
                                   ;


aus „spalten‘*, sondern aus „nagen, kratzen** entwickelt scheint); lat. scan-
dula „Schindel** (aEeduktionsvokalo); iiber gr* oxivdaXyog s. Yf. LEY^b.^ u.
scandula^ Giintert aaO,).                    —
                             Dafi sqen- aus seq- „schneiden** erweitert sei
(Persson Beitr. 813, 882 Anm, 2), ist eine Moglichkeit.

(s)qen -5 (s)qan-' „stofien, schlagen**?
      Arm. Tcasiim „dresche** {^qan-s-)^ sks-anim „fange an“, avr. sicsay, Subst.
skizbn „Anfang**               (^sTzis-     aus idg.     "^sqen-s-)^air. fo-scann- „werfen, stofien,
worfeln**          (z.   B.   3.   PL foscannat „sie           stoBen mit Hornern**), ioAnd-scann-
(z.    B.    3. sg.      do-in-scann) „beginnen**.              Pedersen KZ. 39, 427, KG. II 618
(lit,   slSiyiti     „pflucken**       s.    aber unter sqen- „abspalten**)     ;
                                                                                    sehr 
==== leaf 570 printed ~ 565 ====
                                          sqendh         (s)qer-                                 565

schenJcen ds., auch „geben‘^ nhd. schenJcen (Wadstein ZfdPh. 28, 528, Ficklll^
und Falk-Torp aaO. m. Lit. liber andere Deutungen Kluge® unter schenJcen),
  tJber eine germ. Wz. sJceh- (mhd. sch^he „scliielend‘' usw.) s. Fick III*
448, Falk-Torp u. sjangJe, sTcaasig,

sqendh- „untertaucheii“.
     Gr. oxiv'&og ,untertauchend‘‘;
                  5
                                             lit.   sJc^stu^ sTcendaii,   sJcPsti   „untersinken, er-
trinken^,                 -cZh 2 ^/„ertranken'‘.       Fick KZ. 22, 111, Wb.I*566, Bechtel
BB. 23, 250, Persson Beitr. 155.

1. (s)qer- als Basis  von Wortea fur „einschrumpfen, runzeln; rauhe Haut,
       Schorf, Kruste vertrocknet, mager, Yerkumme^t‘^ Beziehung zu sqer-
                          ;


    „drehen“ („schrumpfen == sich einkriimmen^) ist im allgemeinen wahr-
    scheinlicher als solche zu sqer- „schneiden‘‘ (^rissige Haut'*), dock steht
    einheitlicher Ursprung der hier zsgestellten Worte nicht au6er Zweifel
    (z. B. Persson Beitr. 864 f. Anm. 2).

  Unerweitert in ijorw. sch^ved. sJcare „hart gefrorene Kruste auf dem
Schnee“? (Falk-Torp s. v. unter Ablehnung von Noreens Ltl. 205, Hirts
PBrB. 22, 232 f. Yerbindung mit an. hjarn n. „fest gefrorener Schnee“,
aber selber unter Ankniipfung an sqer- „8chneiden“, wie auch fxir anord.
shyr „geronnene Milch“).
  Mit Gutt.-Erw. ags. scrincan „sich zusammenziehen, verschrumpfen, ver-
                      :



welken“ usw. (s. u. sqer-^ sqer-g- „drehen‘') unnasaliert norw. mdarti. skarJca
 gefrorene Kruste“, skjerJcna „durch Kalte hart werden"‘; anord. Lw. ist
,,


mengl. scorcnen „trocken und hart werden'^ (Falk-Torp aaO., s. auch norw.
horJc usw., russ. korgd^korzavy
```


## [2026-09-14T02:02:59.002Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"Cylinder,.\\{0,300\\}\" SKT.txt | head -3; echo \"---shank\"; grep -n -o \"Shank,.\\{0,300\\}\" SKT.txt | head -3; echo \"=== WLD sqeng text ===\"; python3 -c \"\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')[568]\ni=p.find('sqeng')\nprint(p[i-200:i+1800] if i>=0 else p[-2200:])\n\""
}
```


### [2026-09-14T02:03:00.203Z] TOOL RESULT

```
---shank
=== WLD sqeng text ===
```


## [2026-09-14T02:03:03.944Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -i \"cylinder.\\{0,260\\}\" SKT.txt | head -4; echo \"--- shank\"; grep -n -o -i \"shank\\..\\{0,300\\}\\|Shank\\b.\\{0,300\\}\" SKT.txt | head -4; echo \"=== WLD leaf569 tail ===\"; python3 -c \"\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npp=t.split('\\f')\np=pp[568]\nprint(repr(p[-2500:]))\n\""
}
```


### [2026-09-14T02:03:05.143Z] TOOL RESULT

```
7168:cylinder. (L.)^  h.frustum,  a  piece  cut  off.  Cf.  Gk, 9po.vap^  a  Cragment,  from  ^peiiiup^  to  break inpicces.
7746:cylinder.  Allio Volute,  and  lo  'Walo.
11037:cylinder  for  smoothing  Una corresponding  Ital.  word  is  sMiV kind  of  pressc  to  prcssc  buckiom/ Both  Du.  and  Ital.  words  are  trom mamganum,  mangona,  a  military  ins) for  throwing  stones,  worked  with and  winch.  Indeed,  the  Ital.  mtitg^ means
21156:cylinder,  vaiiatt,  to  roll.     p.
--- shank
11029:shank  in  which /umers  fix  their  work  in  a  lathe.  (F.-»Gk.  ?) h'rom    F.   fuandn/if  1  punch,  a  naadrd.
12308:shank,  hollow bone,  pipe ;  see  Shank. ITimxy,  a  simpleton.  (Ital.)  Ital.  m'lifw, .1  child  (I)iez).  Cf.  Span.  niAo,  a  child, one  of  little  experience.  —  Ital.  ninna,  a lullaby,  nnrse's  song  to  lull  children  to sleep,  also  written  nattna.  Of  imitative origm.
17005:shank,  lower  part  of  the  leg.  <E.) A.  S.  tieanra,  scatua,  bone  of  the  leg  ; named  from  its  motion  in  running;  lit. •ruancr.'  — A.S.  sceacan,  to  shake,  also  to ran,  Aee.  hasten. -f-Du.  srhonk.  Dan.  tkank, Swed.  skatik.  Low  G.  Khmkt,  leg.
17011:shank,  shank-booe,  bol- low  bone  (hence,  a  pipe).  So  also  Do. sthenktfh  Icel.  skenkjOf  Dan.  tkunke^  GL schenken,  to  skink.     See  Nunchion.
=== WLD leaf569 tail ===
".    B.    3. sg.      do-in-scann) „beginnen**.              Pedersen KZ. 39, 427, KG. II 618\n(lit,   slSiyiti     „pflucken**       s.    aber unter sqen- „abspalten**)     ;\n                                                                                    sehr zweifelhafte\nYerbindung.               Ir. scann-        aus ^skan-d-na-^,\n\nsqeng- hinken;                schief, schrag**.\n      Ai. khdnjati „hinkt**, khanja-li „hinkend**, khanjana-h „Bachstelze** ;                     gr.\noxdCco (nur Praes.                 und Impf.) „hinke‘* C^sqng-id);\n      aisL    sJcakkr „hinkend,              schief**,   schwed. mdartl. skinka „hinken**; ohne\nanl.    s-    aisL Jiinka „hinken, lahmen**,                   ahd. Jiinkan „hinken*',   mhd. lianken\nds.  Ygl. Curtius 380; Pick BB. 6, 214, Wb. I^ 567, Zupitza Gutt. 23; fern\nbleiben gr, oniju^og „lahm**, wofur Solmsen Beitr. 215) und die iautliche\nEechtfertigung unter einer Gdf. ^sqeng-uo-s sucht (besser zu sqeibh-^ sqi-m-h-\n„schief** nach Persson Beitr. 156) und gr. oxajLi^og (s. u. skambh „krummen**);\nmir. schigim ,, springe** liegt in der Bed. recht ab und ist wohl Umbildung\nvon air. scend- „springen** (s. u. gkengh- „schreiten**).\n   DaB der Sippe gewiB der Begriff des Gekriimmtseins, Schiefseins zu-\ngrunde liegt {viie in sqeihh-, sqamb-) darf nach Bed.- Yerh. wie oxeXogioxo-\nXiog^ langob. lagi „Schenkel** leq- „biegen     GliedmaBen** auch angereiht\n                                                  :\n                                                                       ;\n\n\nwerden; norw. skonk, skank f. „Schenkel, Schienbein**, dan. skank „Unter-\nschenkel**, schwed. skank^ skank „Schenkelbein       Schienbein**, ags. scanca\n                                                                           ;\n\nf.  „Unterachenkel**, mnd. schenke „Schenkel**, mhd. nhd. schenkel. ahd.\nscincho m., scincha „Beinr6hre, Schenkel**, nhd. Schinken^ afries. skunka,\nnhd. mdartl. schimke ds. (Pick 111^ 450, Falk-Torp u. skank; die Formen\nmit a und u sprechen gegen Brgm. IF. 9, 352 Yerb. von Schinken mit\nahd. scina „Schiene**); ohne s- (Ehrismann PBrB. 20, 53 f.) mhd. hanke\n„Schenkel, Hiifte**, tiroL Henkel - Schenkel; weiteres (wie dt. Schrank zu\ngerm, skrenk- „schief stellen**) auch spatmhd. schank m. „Gestell, Schrank\nfur Trinkgerate** und (wie aisL heJla ;,ausgie6eii**, eig.\n                                                           „ein GeKB neigen**,\nzu hallr „geneigt*‘) as. skenkjan „einschenken**, ahd. scenkan ds., mhd.\n"
```


## [2026-09-14T02:03:17.600Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cylinder",
 "prompt": "Give the etymology of cylinder and, if present on the page, calender (the cloth-pressing machine): Greek kylindros, kylindein, French, Latin forms."
}
```


## [2026-09-14T02:03:19.326Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%84",
 "prompt": "What does Wiktionary give for Persian شل — the senses (including 'leg/thigh' and 'lame/paralysed') and the etymology of each?"
}
```


### [2026-09-14T02:03:22.022Z] TOOL RESULT

```
# Etymology of Cylinder and Calender

## Cylinder

The word traces back to Greek *kylindros* meaning "a cylinder, roller, roll," derived from the verb *kylindein* "to roll," whose origin remains unknown. It passed through Latin *cylindrus* and Old French *cylindre* before entering English in the late 14c. Initially referring to "a portable sundial in the shape of a cylinder," the term later acquired specialized meanings in engineering and mechanics.

## Calender

The cloth-pressing machine shares the same ultimate origin. Dating to the 1510s, *calender* comes from Old French *calandreur* and Medieval Latin *calendra*, a "cloth-pressing machine" named "from the shape of the machine used, from Latin *cylindrus*, from Greek *kylindros*." This device's name directly references its cylindrical rolling components.

Both words demonstrate how the Greek root for "roller" became embedded in English technical vocabulary through Romance language intermediaries.
```


### [2026-09-14T02:03:24.799Z] TOOL RESULT

```
# Persian شل - Senses and Etymologies

Based on the Wiktionary entry, Persian شل has four distinct etymological entries:

**Etymology 1** (Adjective):
- Senses: "soft, limp" and "loose, lax"
- Etymology: Missing/incomplete (possibly from PIE *(s)kelh₁-)

**Etymology 2** (Noun):
- Senses: "thigh of a man" and "thin, colored leather"
- Etymology: Cognate with Mazanderani, from PIE *skelo-
- Derived term: شلوار (šalvâr)

**Etymology 3** (Noun):
- Senses: "spear, javelin" and "trident, harpoon"
- Etymology: Missing/incomplete

**Etymology 4** (Adjective):
- Sense: "lame"
- Etymology: "Borrowed from Arabic أشل"

The entry notably distinguishes between homographs with different pronunciations: /ʃol/, /ʃal/, and /ʃil/, each carrying different meanings despite identical spelling in Persian script.
```


## [2026-09-14T02:03:31.780Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%84%D9%88%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Scythian/%C5%A1alaw%C4%81ri\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%CE%BA%E1%BF%B6%CE%BB%CE%BF%CE%BD\" \\\n \"https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CE%BB%CE%BF%CE%BD\" \\\n \"https://www.etymonline.com/word/colon\" \\\n \"https://www.etymonline.com/word/cylinder\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 453, roots Skel 1 / Skeng: shalvar, shal, Greek kolon vs kolon, colon, cylinder/calender\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T02:03:35.139Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/25c65992450a86cf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e2f9cce2c7b86836.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/800888b2697f0e21.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/98281e7f793d334f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9788827c53d639a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/29e803056113586a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a322eb65d9e34bd4.txt
```


## [2026-09-14T02:03:39.813Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/shank",
 "prompt": "Give the etymology of shank: Old English sceanca, Proto-Germanic form, and the PIE root cited."
}
```


## [2026-09-14T02:03:41.812Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/shank",
 "prompt": "Give the English noun 'shank' etymology: Middle English, Old English sceanca, Proto-West Germanic / Proto-Germanic *skankô, and the PIE root (*skeng- ?) with cognates (Sanskrit khañjati, Greek skazein, Avestan haxti?)."
}
```


### [2026-09-14T02:03:43.639Z] TOOL RESULT

```
# Etymology of Shank

**Old English Origin:** The word derives from Old English *sceanca*, meaning "leg, shank, shinbone," specifically the part between knee and ankle.

**Proto-Germanic Form:** The Old English term comes from Proto-Germanic *\*skunkia-*, which etymologists believe literally means "that which bends."

**PIE Root:** The ultimate source is the Proto-Indo-European root *\*skeng-*, meaning "crooked." This same root also produced Old Norse *skakkr* ("wry, distorted") and Greek *skazein* ("to limp").

The semantic progression reflects the body part's characteristic bent or curved appearance when walking.
```


### [2026-09-14T02:03:47.048Z] TOOL RESULT

```
# Etymology of "Shank"

Based on the Wiktionary entry, here's the etymological path:

**Linguistic Lineage:**
The word derives from Middle English forms like "shanke" and "schank," which came from Old English *sċanca* and *sċeanca* (meaning "leg"). These descended from Proto-West Germanic *skankō* and Proto-Germanic *skankô* ("shank; thigh"), ultimately tracing back to Proto-Indo-European *(s)keng-* ("to hobble, limp; to tilt").

**Related Languages:**
The entry documents cognates across Germanic languages—West Frisian *skonk*, Dutch *schenkel*, and Danish *skank*—as well as Celtic (Irish *céim*, Welsh *cam*) and other language families sharing the same root.

This etymology reflects how the term's core meaning relating to the leg or a protruding part has remained stable across millennia and language groups, with the word's structure preserving its ancient Indo-European origins through regular sound changes.
```


## [2026-09-14T02:03:50.954Z] TOOL CALL #52: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/shank\" \"https://en.wiktionary.org/wiki/shank\" \"https://www.etymonline.com/word/isosceles\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 453, root Skeng: shank < PGmc *skankô < PIE *(s)keng-; and Skel 1 isosceles\" 2>&1|tail -1; done; echo \"=== verify_check help ===\"; sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-14T02:03:53.222Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/32934e420395850a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a0f8119423d31726.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/41c003dffa81f4e8.txt
=== verify_check help ===
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


## [2026-09-14T02:03:57.789Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False,indent=1))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:1500])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2000])\n\""
}
```


### [2026-09-14T02:03:58.871Z] TOOL RESULT

```
{
 "pdf_page": 385,
 "book_page": 355,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-07"
}
{
 "entry": 0,
 "root": "Peg",
 "verdict": "plausible",
 "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
 "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
 "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ر
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
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW 792 (POK_03 leaf 25)",
   "stance": "partial",
   "note": "'Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"' — shoulder/wing/side, not breast."
  },
  {
   "src": "KLN",
   "where": "1966 ed. p.1272 s.v. punka (leaf 678)",
   "stance": "partial",
   "note": "'fr. OI. pakṣaḥ, pákṣas, \"wing, side, half\", which is possibly cogn. with Lett. paksis, \"corner of a house\", Russ. pach, \"flank\".' Klein too has no 'breast'."
  },
  {
   "src": "WLD",
   "where": "WP II 3-4",
   "stance":
```


## [2026-09-14T02:04:07.416Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"سیلندر:\" MON_part1.txt MON_part2.txt | head; echo \"--- context\"; sed -n '34600,34615p' MON_part1.txt; echo \"=== silandr headword search ===\"; grep -n \"سیلندر\" incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -5"
}
```


### [2026-09-14T02:04:07.531Z] TOOL RESULT

```
MON_part1.txt:77028:سرسیلندر: 6 اف. فر.] (امر.) 
MON_part1.txt:82346:سیلندر: 1:07[ (.) استوانه. ضح. به این 
--- context
برصء ابر ص» پیس. 
پیست. ۱ (.) محوطه با میدان آماده 
برای ورزش مسابقه» رقص؛ تاختگاه (فره.) 
پیستودن: «ماعام (فز.) استوانه متحرکی که 
با اصطکاک در لول تلمبه پا سیلندر ماشین 
بخار حرکت کند. تکمةٌ فنری» دکمهٌ فشاری. 
کسی که از شخصی جانبداری کند؛ حامی» 
پارتی (در فرانسوی به معنی سفارش و 
توصیه است.) (مکن.) در اتومبیل لولةً فلزی 
توپری است داخل لولةٌ دیگری بنام سیلندر 
که در نتیجةٌ انفجار گاز مترا کم (مخلوط گاز 
هوا و بنزین) در ناحیة سر سیلندر (قسمت 
فوقانی پیستون) بستون در داخل سیلندرها 
شدیداً حرکت کند و این حرکت به وسیله 
آلت دیگری بنام دستة پیستون به میل‌لنگ 
نتقل شود و بالاخره رفت و آسد آن به 
=== silandr headword search ===
29632:داخل سیلندرها می‌شود زیاد و کم نماید. 
34604:با اصطکاک در لول تلمبه پا سیلندر ماشین 
34609:توپری است داخل لولةٌ دیگری بنام سیلندر 
34611:هوا و بنزین) در ناحیة سر سیلندر (قسمت 
34612:فوقانی پیستون) بستون در داخل سیلندرها
```


## [2026-09-14T02:04:16.123Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '82340,82352p' MON_part1.txt; echo \"---\"; sed -n '77024,77032p' MON_part1.txt"
}
```


### [2026-09-14T02:04:16.234Z] TOOL RESULT

```
سیلک: اه (.) حریر» ابریشم. ضح. 


۹« 
احتراز از استعمال این کلم بیگانه اولی 
سیلندر: 1:07[ (.) استوانه. ضح. به این 


معنی احتراز از استعمال این کلمة بیکانه اولی 
است. (مکد.) لوله‌ای است استوانه‌یی شکل 
که در موتور اتومبیل تعبیه شده در داخل 
موجود در سیلندر را به سمت ته سیلندر - که 
---
سرسری: ۵.927 (ص‌نسب.) کار بی‌تأمل» 
سطحی. بهوده و نسنجیده. فرومایه. (ق‌مر.) 
از روی عدم تأمل. 

سرسیلندر: 6 اف. فر.] (امر.) 
(مکد.) سرپوشی که انتهای فوقانی سیلندرها 
را می پوشاند. 

سسر شاخ شدن: 42-10027-.: (مسص‌ل.)
```


## [2026-09-14T02:05:25.797Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n -o \"sakthi.\\{0,180\\}\\|skelos.\\{0,180\\}\\|skeng.\\{0,180\\}\\|skank.\\{0,180\\}\" IEC.txt | head -10; echo \"=== SYN leg/thigh ===\"; grep -n -o \"sakthi.\\{0,200\\}\\|σκέλος.\\{0,120\\}\\|skélos.\\{0,150\\}\" SYN.txt | head -8"
}
```


### [2026-09-14T02:05:26.948Z] TOOL RESULT

```
=== IEC ===
8160:skeng-, skng-) limp, pace, amble’. Cf. WP I, 588 & II, 564 Skt. kháfijami ((limp', fr. *ksen$-); Per. cf. xing ‘white horse’; xinga, adj. ‘able-bodied’; (zero-gde in) xazidan, inf. ‘cra
8167:skeng-, skng-) — kseubh-
8211:skengio Skt. khanjah “limping, lame’; cf. khanj-, cpds. ‘restless’; khanjanabh, m. ‘wagtail’; OE cf. scanca, wm. ‘shank’; ON cf. shakkr ‘wry, askew’ beside skakka ‘abet
15560:skelos, see skhelos and cf. skel- (3) (^wrong, crime', etc.)
15732:skeng- Oss. (variant) Küdz, adj. ‘bent; (e-gde in) Arm. xinc, gs: xnco, o-st, s. ‘fold, bosom’; OFris. skunka, wm. ‘shank, thigb’; Du. schonk, f. “large bone, knuckle-bone'; ON skukka, 
16631:sakthih, f. sákthi, n. id.; Av. haxtis, f. ‘Join’; LW in Oss. agd, id.; phonol. obscure in Arm. azdr, id.; (Gk. ókhthos, okhthe ‘hill; bank? lit.? ‘side’, here?). (Isophone: Li. sagtis, 
=== SYN leg/thigh ===
```


## [2026-09-14T02:05:27.448Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD colon ===\"; grep -n -o \"kolon.\\{0,200\\}\\|kōlon.\\{0,200\\}\" FSD_vol1.txt | head -5; echo \"=== WEB colon ===\"; grep -n -o \"Gr. kolon.\\{0,200\\}\\|kolon,.\\{0,200\\}\" WEB_vol1.txt | head -5"
}
```


### [2026-09-14T02:05:28.617Z] TOOL RESULT

```
=== FSD colon ===
73877:kolon, colon,  +   kolon,  colon.)
73878:kolon,  colon, +   kolon,  +   stoma,  mouth.l
73887:kolon,  colon,  -f  lithos,  stone.J       
73899:kolon,  membor)  +   metron,  measuro.]
73912:kolon, member.]
=== WEB colon ===
36939:Gr. kolon, the colon.] inflammation of the mucous membrane of the large intestine.
37353:Gr. kolon, the colon, and lithos, a stone.] an oGlite resembling the fossil intes- tines of fishes.
37358:Gr. kolon, the large intestine, colon.] that part of the large intestine extending from the caecum to the rectum.
37536:Gr. kolon, the colon, and tomé, a cutting, from temnein, to cut.] the surgical operation of forming an artificial anal opening in the colon.
37538:Gr. kolon, the colon, and tomé, a cutting, from temnein, to cut.] a surgical incision of the colon.
```


## [2026-09-14T02:05:36.002Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"skhelos.\\{0,400\\}\" IEC.txt | head -6; echo \"---\"; sed -n '15555,15570p' IEC.txt; echo \"=== 16625-16640 ===\"; sed -n '16625,16640p' IEC.txt"
}
```


### [2026-09-14T02:05:37.601Z] TOOL RESULT

```
15560:skhelos and cf. skel- (3) (^wrong, crime', etc.)
16052:skhelos, om ^wrong, fraud'. Cf. skel- (3). Cf. WP II, 598 Skt. Chalah, am. mn. id.; (o-gde in) khálah, m. ‘rogue’; Lat. scelus, gs: -eris, n. *wicked- ness; villain; MHG schél, m. 'deceiver'; (z- gde in) schülle, wm. id.; (long-gde in) Icel. skæla, v. ‘distort’ and in Fris. skeel, n. (2) ‘wrong, blemish, defect, evil
---
1156
MHG schilf (reed, rush"). (E scallop is fr. MFr. escalope, and this fr. Gmc., cf. skolb- below)
skelbio (skolbió) “pull a face, grin” ON skelpa, f. ‘grimace’; Cz. (dial. 3-) Skleb, m. ‘grin’; Sklebit se, v. id. beside OCS (o-gde) sklabiti se, inf. ‘smile’; (isophonic: Li. skelbti, inf. *declare")
skelbh-, see skolbh-, and cf. skol-. Ir. ambig. Thus only in It. scealb, f. ‘splinter, fragment, slice, shred’; G cf. schelbern, v. “form a crust, esp. of ice’. Ir. also (o-gde in) scolb, mf. (splinter, peg, thorn, spar’: Latv. skalbi, mpl. ‘crossbars on plough-fork. Apparent isophones in OE scielf ‘pinnacle’; ON skjolf, f. 'height")
skeldh- ‘separation; separator’. Cf. skel- (1) Go. skildus, m. ‘shield’; MHG schilt, gs: des, m. id.; OE scild, scield, m. id.; ON skjoldr, ds: skildi, m. id.; cpds: skjald-; OCS (?) *xlédü, m. ‘weeds’; Li. skéldena, f. ‘split leather’; Latv. šķelda, f. “split, chip’. (ISophonic: Arm. xeyd, i-st. 'stranglehold, noose'; xydem, xey- dem, v. ‘strangle’; xyduk, adj. ‘sultry; MHG schélten ‘scold; repulse’; Icel. skjalla *flatter")
skelos, see skhelos and cf. skel- (3) (^wrong, crime', etc.)
skeluos, skelquos, see kseluos. This form is explicit only in MHG schilwen (beside schilhen), v. ‘squint and (perhaps) in Skt. kharváh ('crippled, lame”, fr. *skheluo-? Cf. MHG schál, gs: -wes ‘crooked, crosseyed'; Arm. xey “lame” and Gk. skoliós *crooked")
skemb- Ir sceamh, f. (3) eut: ME (from Norse) skimp, adj. ‘scanty’, but cf. skmb-; R cf. u- SCemit, inf. ‘trap, pinch’; Li. cf. skembras ‘shrivelled, hardened"; Latv. cf. šķembas, fpl. beside (o-gde) skambas 'road-flints'
skendoó, ið “dash, rise, fall. (Cf. the seman- tics of type pad-). (Variant w. *-o- in Av. and Lat. Cf. skand-, with shva-variant also in Ir.). Cf. WP II, 565 Skt. skándami, v. “dash, bound, spurt, drop’; a-skandami, v. ‘attack’; Av. cf. skond-, v. “smash”; skendo, m. (fruin', lit. "allt: a-skon- da, adj. f. ‘virgin’; (Lat. -e- in dé-scendo is
1157
secondary. See skand- but possibly a form *sknd- is implied for scando); Olr. scendim, aor. 3s: sescaind; mod. Ir. sceinnim, scinnim, v. ‘leap, start, bud, shoot'; Li. skendiu, eti & Skestu, skgsti, pf: skendau, v. ‘sink, drown’ beside skandinti, inf. tr. id. (o-gde); OCS cf. (Ð stedije, n. (generation, tribe’, lit. *des- cent^?); cf. Ukr. naSCad-ok, m. “origin”. (For a possible long-zero grade to account for Lat. scando, cf. planta, plantago, prandium, fr. *plm-tà, *prm-edio-, etc. The background of Gk. skinthós, adj. (diving! is problematical. Cf. písures, piítnemi, skídnamai)
sken£- (skn£-) “bend, curve, hook; be bent, be crippled, hobble’. WP II, 564 Skt. kháfijami, v. ‘limp (ambig.? *kseng-); Sw. skinka, v. id.; Arm. cf. xinc, gs: xnco, ab. s. xncov, s. ‘fold, bosom, hollow’; OE scincio “renal fat”; (z-gde in) Per. xazam, -idan, v. ‘creep’; Gk. skázo, v. ‘limp’; Oss. Kádz, adj. ‘bent’; OFris. skunka, wm. ‘shank, thigh’; Du. schonk, f. *bigbone'; ON skukka, f. “fold, crease, wrinkle’: Sw. skunk, pl. ar m. id.; cf. G schunkeln, v. ‘rock’; ON skykkjum, dat. pl. as adv. ‘tottering’. Cf. skn$- as a separate entry, and WP I, 588. Per. from a variant "ksng-.
skénis, à ‘skin, film, covering’. (Variant of sKiiàn-, q.v.) Alb. hue, gs: honi, m. ‘honeycomb’; W ysgin, pl. -au, f. “skin cloak, pelisse’
(skép-, see sKép- “covering, wrap”, etc.)
skép- “chip, chop, slice”, etc. cf. WP II, 581 Gk. sképarnon, n. ('adze'. A synth. cpd?, cf. ON arn-ing ‘tillage’, radical: ar- "do. make"); R ščepà, f. ‘chip’; MLG schéver, schiver, sm. *chip, splinter': E shiver, id.; (long-gde in) Latv. Skëpele, f. ‘chip’
skēpið “dash, rush, fal Gk. sképtó, v. ((2) “dash, hurl, attack’; intr. *fall); cf. skeptós, m. ‘thunderbolt’; Alb. hop, v. jump’; m. id. (a formal equivalent only, prob. onomat. cf. Fr. hop! Cz. hop! etc.); Blg. ščapam, v. ‘stumble’; OCS cf. stapljo, Stapati, v. ‘revel, luxuriate'
=== 16625-16640 ===
40
45
1240
segh-, segh-). WP II, 481 Arm. agi, gs: agvo, s. (tail, lit. "holder", cf. also agujc, gs: aguci, s. “holder, setting, clasp, joint, staple’ beside (?) b-ognim, v. ‘be tired”; MHG sacke, sagge, wm. (“common land”, lit. ‘holding’, but see sogh-); Slovak cf. o-soh m. ‘use’; Li. saga, f. “button, clasp, buckle’; sage, f. ‘brooch’. Ambig. are Skt. sahah, adj. “mighty”; sahyam, n. ‘help’, but prob. *sogh- in view of Av. hazaoSo, adj. (agreed', fr. *sogheusio-); cf. however soghuros below. Long-gde in OCS po-sagü, m. ‘fetter; marriage’; po-sag- noti, inf. join; marry’. Ambig. also in Myc. -oko-, cpds. ‘holder’; Gk. okheüs, m. “holder, clasp, thong, bar’; okhós, adj. ‘firm, secure?
soghuros (soghuros) ‘firm, stable’. WP II, 481. Cf. segh-, segh-; sogh-, sogh- Skt. (ambig.) sáhurih, adj. (mighty, victor- ious'; Arm. agur, adj. ‘hard’; Gk. (ambig.) okhurós, adj. ‘strong
soghlos, soghelos (sogh-) “hold, holder Hitt. saklais (for *saglis), s. law, custom’; W hoel, pl. ion, f. ‘nail’
soghtis ‘thigh’ Skt. sakthih, f. sákthi, n. id.; Av. haxtis, f. ‘Join’; LW in Oss. agd, id.; phonol. obscure in Arm. azdr, id.; (Gk. ókhthos, okhthe ‘hill; bank? lit.? ‘side’, here?). (Isophone: Li. sagtis, gs: -ies, f. ‘clasp, buckle")
sogh- (alternative form of type sogh-, sce segh- and segh-). Cf. songh- Skt. cf. sahyam, n. ‘help’; Av. cf. hazao$o, adj. ‘agreed’, Myc. oko-, m. “holder? beside Gk. ókhma, n. & okhmé, f. id.; ókhanon, okháne ‘handle’; MHG sagge, sacke, wm. (common lang’, lit. holding")
soib- 'dripping, liquid fat, liquid resin, cream. Cf. seib-. WP II, 468 Gk. cf. (e-gde) eibo, v. "let drip’; eíbomai, v. ‘drip’, OHG sifen, v. id.; Tokh. sep-, sip-, v. ‘grease’; OE sipian, v. (^wane'. See seib-) beside (o-gde) OHG seipfa, f. ‘soap’; seifa, f. resin; OE sap, s. (amber, unguent and sape, f. ‘soap’; (Gmc. LW in) Lat. sebum, sē- vum, n. ‘tallow; suet’; W hufen, f. cream’, fr. *soiben-: OE sāpe); (Gmc. LW in) Finn. saippio, as OHG. (NB. Baltic Ger. siepen, v. ‘to seep’ is e-gde; E to seen o-gde fr. *soi-
1241
beið). Extn. in MHG seifel, sm. ‘spittle’
(soidh-, see Supt: S)
soighos, us (?), soighros (?) Skt. sehub, m. (an unidentified substance; an organ of the body); Sw. seg, adj. 'tough'; MHG cf. seiger, adj. ‘viscous, clotted’; ON seigr, adj. ‘tough, stubborn; ponderous'.. (Li. Saizüs ‘keen, heavy, severe’ suggests a pos- sible variant *qusoigh-)
(soik-, cf. soiqu- and seik- (1), seiquo, siqu-. Ambig. in Skt. & Li.) MHG seihen, v. “strain, filter’; Skt. cf. sekah, m. 'outpour; libation'; sektram, n. ‘ladle’; Li. saikaü, ýti, v. and saikuoju, uoti, v. ‘bale out?
soik- (2) (?) “go, reach’. Evidence ambig. Variant: seik- in Skt. & Gk. Skt. cf. seke, mp. ‘go’; Gk. eko id.; Li. sáikau, yti, v. “try to reach"
soilos (soiolos) ‘cord’. Cf. seio. WP II, 464 Br. hual, pl. -u, m. ‘fetter’; pl. ‘chain’; W hual, pl. -au, m. as Br.; OHG seil, sn. ‘rope’; OE sal, mf. id.; Du. zeel, n. “strap; traces; girth- belt; LG seel, n. “handle of pail’; ON seil, f. “string, line'; Li. sailas, m. “rope, string, bond, tether `
```


## [2026-09-14T02:05:58.578Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%95%E0%A5%8D%E0%A4%A5%E0%A4%BF",
 "prompt": "Sanskrit सक्थि (sakthi): give the meaning(s) and the etymology — Proto-Indo-Iranian form, Avestan cognate, PIE root, and any note on the -th-."
}
```


### [2026-09-14T02:06:04.176Z] TOOL RESULT

```
# Sanskrit सक्थि (sakthi)

## Meanings
The word has three primary definitions:
1. "The thigh, thigh-bone"
2. "The pole or shafts of a cart"
3. (Euphemistic, dual form) "The female genitals"

## Etymology

**Proto-Indo-Iranian form:** The term derives from "*sáktʰi," which is the reconstructed Proto-Indo-Iranian ancestor.

**PIE root:** It traces back to Proto-Indo-European "*sokʷHt-i-s" meaning "thigh."

**Avestan cognate:** The related Avestan word is "haxti," also meaning "thigh," demonstrating the cognate relationship across Indo-European languages.

**Note on -th-:** The "-th-" (aspirated dental stop) is preserved across these linguistic stages, reflecting the original Proto-Indo-European laryngeal element (represented as "H" in PIE reconstruction) that manifested as aspiration in the daughter languages. This aspiration feature appears consistently in Sanskrit, Avestan, and other cognate forms.
```


## [2026-09-14T02:06:09.953Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sok%CA%B7Ht-i-s",
 "prompt": "What does this page say about PIE *sokʷHt-i-s 'thigh' — cognates (Sanskrit sakthi, Avestan haxti, Greek?, Armenian?), and does it mention any connection to *(s)keng- 'crooked' or Germanic shank?"
}
```


## [2026-09-14T02:06:11.669Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)keng-",
 "prompt": "What does Wiktionary reconstruct for PIE *(s)keng-? Give the meaning and the list of descendants/derived terms (Sanskrit khañjati, Greek skazein, Germanic *skankô, Avestan?)."
}
```


### [2026-09-14T02:06:11.746Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:06:16.250Z] TOOL RESULT

```
# PIE *(s)keng- Reconstruction

## Meaning
According to Wiktionary, *(s)keng- means: "to limp, hobble" or "to tilt, be askew."

## Documented Descendants

The article lists these key derived terms:

- **Sanskrit**: खञ्जति (kháñjati, "to limp")
- **Greek**: σκάζω (skázō, "to limp")
- **Germanic**: *skankô ("that which is bent; thigh, shank")
- **Celtic**: *kengeti ("to step, tread")
- **Slavic**: *šęgati ("to joke")

The page does not mention Avestan descendants. The reconstructions derive from Helmut Rix's *Lexikon der indogermanischen Verben* (2001).
```


## [2026-09-14T02:06:26.070Z] TOOL CALL #62: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%95%E0%A5%8D%E0%A4%A5%E0%A4%BF\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)keng-\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 453, root Skeng: sakthi/haxti under PIE *sokwHt-i-s not (s)keng-\" 2>&1|tail -1; done"
}
```


### [2026-09-14T02:06:28.151Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/411cd210239b475c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d5420024ba0d5b4f.txt
```


## [2026-09-14T02:07:00.377Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB salvar ===\"; grep -n -i \"salvär\\|selvär\\|šalvār\\|sarbâl\\|sarbäl\\|saravara\\|σαράβαρα\" HUB.txt | head; echo \"=== MON shal thigh ===\"; grep -n \"شل: \\|شل:\" MON_part2.txt MON_part1.txt | head -8; echo \"=== PLA sirwal ===\"; grep -n -o \"sirwāl.\\{0,200\\}\\|Sirwāl.\\{0,200\\}\\|سروال.\\{0,150\\}\" incoming/PLA/PLA_pages.txt | head -5"
}
```


### [2026-09-14T02:07:01.494Z] TOOL RESULT

```
=== HUB salvar ===
=== MON shal thigh ===
MON_part2.txt:7482:فشل: ا25] [ع.] (.) مرد بد دل و ترسنده و 
MON_part2.txt:7485:فشل: اه [ع.] (مصل.) کاهلی کردن؛ 
MON_part2.txt:7488:فشل: (ع25] [ع.] یت و سست و 
MON_part2.txt:7491:فشل: ۳ پرده هودج. فرشی که 
MON_part2.txt:30627:تعان اسب 9 مانشل: ان کب کرفبت رون وا 
MON_part2.txt:81424:نهشل: ۳۵۷5 (ع.] (.) گ رگد ذئب. چرغ. 
MON_part2.txt:85607:ورمیشل: [۹۵] ۷۰۳ (.) نوعی رشته فرنگی 
MON_part1.txt:13578:اشل: 8 (.) واحدی است برای طول 
=== PLA sirwal ===
```


## [2026-09-14T02:07:11.574Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:16:56.418Z] TOOL CALL #64: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-453.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_SHAL   = \"https://en.wiktionary.org/wiki/%D8%B4%D9%84\"\nW_SHALV  = \"https://en.wiktionary.org/wiki/%D8%B4%D9%84%D9%88%D8%A7%D8%B1\"\nW_SCYTH  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Scythian/%C5%A1alaw%C4%81ri\"\nW_KOLON_L= \"https://en.wiktionary.org/wiki/%CE%BA%E1%BF%B6%CE%BB%CE%BF%CE%BD\"\nW_KOLON_S= \"https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CE%BB%CE%BF%CE%BD\"\nE_COLON  = \"https://www.etymonline.com/word/colon\"\nE_CYL    = \"https://www.etymonline.com/word/cylinder\"\nE_SHANK  = \"https://www.etymonline.com/word/shank\"\nW_SHANK  = \"https://en.wiktionary.org/wiki/shank\"\nE_ISO    = \"https://www.etymonline.com/word/isosceles\"\nW_SAKTHI = \"https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%95%E0%A5%8D%E0%A4%A5%E0%A4%BF\"\nW_SKENG  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)keng-\"\n\nPOK928 = {\"src\":\"POK\",\"where\":\"IEW 928, lemma '(s)kel-4 (extended klā-, klō-)' (POK_full.txt line 75386)\",\"stance\":\"supports\",\"note\":\"\\\"Root / lemma: (s)kel-4 ... Meaning: to bend; crooked\\\"; material: \\\"Gr. skelos m. 'thigh', skelis 'Hinterfuss, hip', skellos 'bowlegged', skolios 'crooked', ... kellon streblon, plagion Hes., kullos 'writhed, crooked, humped, lamed', kulindo, -eo 'rolle, walze', kulindros 'Walze, pulley, Zylinder', kolon 'limb, member', koleos, Attic kole 'Hueftknochen, ham'.\\\" References: WP. II 597 ff.\"}\nAHDSKEL = {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. skel-3 (AHD_watkins1985.txt line 935)\",\"stance\":\"supports\",\"note\":\"\\\"skel-3. Also kel-. Crooked. With derivatives referring to a bent or curved part of the body, such as a leg, heel, knee, or hip. ... 2. Suffixed form *skel-es- in Greek skelos, leg: ISOSCELES, TRISKELION. ... 5. Suffixed lengthened-grade form *kol-o- in Greek kolon, limb, member: COLON(1). 6. Attributed (quite doubtfully) by some to this root is Greek kulindein, to roll: CALENDER, CYLINDER. [Pok. 4. skel- 928.]\\\"\"}\nWLD597 = {\"src\":\"WLD\",\"where\":\"Walde-Pokorny II 597-598 (WLD_Bd2_pages.txt leaves 602-603)\",\"stance\":\"supports\",\"note\":\"The root '4. sqel- krumm' runs 597-598; p.598 lists \\\"Gr. skelos 'Schenkel', skelis 'Hinterfuss, Huefte bei Tieren', skellos 'diestrammenos, pandus, scaurus', skolios 'improbus', skalenos 'schief, krumm', skolex 'Wurm', kellon streblon, plagion Hes., kullos 'gekrummt, gelaehmt'\\\" and, three lines above, \\\"np. kul 'krumm, gekrummt' (s. Huebschmann Arm. Gr. I 457)\\\".\"}\n\ne0_nodes = []\n\ne0_nodes.append({\n \"id\":1,\"lang\":\"Persian\",\"words\":\"šal 1; šalvâr; šelang; šalpǔy\",\"verdict\":\"plausible\",\n \"derivation\":\"شل šal 'thigh, (upper) leg' is the Persian member of the root: Wiktionary's Etymology 2 for شل ('thigh of a man; thin coloured leather') takes it back to PIE *skelo-, i.e. exactly Pokorny's (s)kel- 928, and names شلوار as its derivative. Horn, Grundriss no. 789 (p.175) heads the entry \\\"šal 'Schenkel', šeleng (šileng); vergl. šalvār 'Hosen'\\\" and equates it with Gk. σκέλος (after Justi), while warning that Armenian srunk 'shins' does NOT belong here. شلنگ šelang 'stride, leap' is šal + the denominal suffix -ang; Borhan-e Qate' (printed 1286) defines it 'برجستن و فروجستن شاطران ... جهت ورزش و مشق راه رفتن' — the leaping and striding of couriers done as exercise, which is precisely Nourai's double gloss 'step, also a leg exercise'. شلوار is the weak link: Horn himself says 'np. šalvār ist weit entlehnt' and lists Gk. σαράβαρα (Photius, Pollux), Arab. sarbāl/sirwāl, Kurd. šelvār, Oss. salbaro, Wakhi savālak; modern work (Cheung, Iranian Borrowings in Qur'ānic Arabic, 2017, via Wiktionary) derives NP شلوار from MP šalwār (Book Pahlavi šlwʾl), itself a borrowing from Proto-Scythian *šalawāri, tentatively analysed *šali 'leg, thigh' (the cognate of Persian šal) + *wāri 'covering' (< PIr. *wā́rah-). So Nourai's paraphrase '\\\"like legs\\\", pants' matches the modern internal analysis of the compound, but the word reached Persian from Scythian/Saka — via Achaemenid Elamite šá-ir-ba-la-ad-da and Aramaic/Syriac — rather than being built inside Persian from šal. شلپوی šalpǔy 'the sound of footsteps' is real (Asadi, Loghat-e Fors p.207; the Bū-Shakūr Balkhī couplet the chart quotes), but Borhan records it beside the variants شکپوی and شگپوی, so its first element is not securely šal 'leg'; attaching it to this root is Nourai's own step and is unsupported.\",\n \"derivation_fa\":\"«شَل» به معنی ران و پای، بازماندهٔ ایرانی باستان *šala- و از ریشهٔ هندواروپایی آغازین *skelo- «کج، خمیده؛ اندام خمیدهٔ تن» است و هم‌ریشهٔ σκέλος یونانی «ران» شمرده می‌شود (هرن، شمارهٔ ۷۸۹؛ ویکی‌واژه). «شلنگ» از شل + پسوند ـنگ ساخته شده و برهان قاطع (ص ۱۲۸۶) آن را «برجستن و فروجستن شاطران ... جهت ورزش و مشق راه رفتن» تعریف می‌کند که درست همان معنای دوگانهٔ نورایی است. اما «شلوار» وام‌واژه است نه ساختِ درونیِ فارسی: خودِ هرن می‌نویسد که این واژه «بسیار وام داده شده» (σαράβαρα یونانی، سِروال/سِربال عربی، شلوار کردی، salbaro آسی) و پژوهش امروزی (چونگ ۲۰۱۷) آن را از فارسی میانهٔ šalwār و آن را وام‌گرفته از سکایی آغازین *šalawāri می‌داند که احتمالاً از *šali «ران» + *wāri «پوشش» ساخته شده است؛ یعنی تحلیل معناییِ نورایی («مانندِ پاها») درست است ولی راهِ ورود واژه به فارسی از راه سکایی بوده است. «شلپوی» نیز در لغت فرس (ص ۲۰۷) و برهان با گونه‌های «شکپوی» و «شگپوی» آمده، پس جزء نخست آن به‌یقین «شل» نیست و پیوند دادنش به این ریشه از خودِ نورایی است. نتیجه: ادعای نورایی دربارهٔ «شل» و «شلنگ» درست است و دربارهٔ «شلوار» و «شلپوی» با احتیاط پذیرفتنی است.\",\n \"sources\":[W_SHAL,W_SHALV,W_SCYTH],\n \"ref_check\":[\n  {\"ref\":\"HRN:175\",\"status\":\"supports\",\"note\":\"Horn, Grundriss p.175 no. 789 (HRN.txt leaf 196): \\\"789. šel 'Schenkel', šeleng (šileng); vergl. šelvär 'Hosen'. gr. skelos (Justi, Litbl. f. or. Phil. I, 65; aber nicht gehört hierher arm. srunk 'Schienbeine, Waden' ...). np. šelvär ist weit entlehnt, vergl. sarabara (Photius, Pollux u. ö.), arab. sarbāl, sarvāl, kurd. šelvār, sarval, salval, af. bel. salvār, oss. salbaro, wakhi savālak, minj. soāl u. s. w.\\\" — the page carries exactly Nourai's šal / šelang / šalvār group and the Greek comparison.\"},\n  {\"ref\":\"BQT:1288\",\"status\":\"partial\",\"note\":\"All four words are in Borhan-e Qate', but a couple of pages earlier in the scan used here (BQT_v3_pages.txt, printed = pdf page + 1206): شل at printed 1284 ('ران آدمی را گویند خصوصاً و ران سایر حیوانات را عموماً') with Mo'in's footnote 7 'قس: شلنگ، شلوار. «اشتقاق - هوبشمان ۷۸۹»' — i.e. Mo'in cross-references the same Horn/Hübschmann entry no. 789 that Nourai relies on; شلپوی at printed 1285 with Mo'in's footnote quoting the Bū-Shakūr couplet from 'لغت فرس ۲۰۷' and the variants شکپوی، شگپوی; شلنگ and شلوار at printed 1286. Content supports Nourai; the printed page number is 1284-1286 here, not 1288.\"}],\n \"consulted\":[\n  {\"src\":\"HRN\",\"where\":\"no. 789, p.175\",\"stance\":\"supports\",\"note\":\"see ref_check; Horn groups šal, šelang, šalvār and compares Gk. skelos.\"},\n  {\"src\":\"BQT\",\"where\":\"printed 1284-1286 (v3 scan pdf pages 78-80)\",\"stance\":\"supports\",\"note\":\"شلنگ: 'برجستن و فروجستن شاطران باشد. جهت ورزش و مشق راه رفتن'; شلوار: 'ازار و تنبان پاچه کوتاه را گویند'; شلپوی: 'آواز پای را گویند که به هنگام راه رفتن بگوش آید'.\"},\n  {\"src\":\"MON\",\"where\":\"2-vol Adena condensation (MON_part1/2)\",\"stance\":\"silent\",\"note\":\"grep of 'شل:' in MON_part1.txt / MON_part2.txt returns only فشل، نهشل، اشل — the headword شل is not recoverable from this OCR, and the 6-volume pagination Nourai cites is not online.\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt / ARY_latin_index_pages.txt\",\"stance\":\"silent\",\"note\":\"grep 'شلوار' returns only one incidental line (13476, a Old Prussian gloss); Aryanpur has no entry for شل / شلوار under this root.\"},\n  {\"src\":\"POK\",\"where\":\"IEW 928\",\"stance\":\"silent\",\"note\":\"Pokorny's (s)kel-4 lists Greek, Albanian, Latin, Germanic, Baltic and Slavic reflexes but no Iranian ones at all — the Persian branch is Horn's, not Pokorny's.\"}]})\n\ne0_nodes.append({\n \"id\":2,\"lang\":\"Greek\",\"words\":\"skelos\",\"verdict\":\"confirmed\",\n \"derivation\":\"Ancient Greek σκέλος (skélos), n., 'leg, thigh' (Homer onwards), is a s-stem *skel-es- built directly on the root: Watkins reconstructs \\\"Suffixed form *skel-es- in Greek skelos, leg\\\", and Pokorny 928 opens the Greek material of (s)kel-4 with \\\"Gr. skelos m. 'thigh'\\\" beside σκελίς 'hind foot, haunch' and σκολιός 'crooked'. The semantics are the root's own: the leg is named as the bending limb.\",\n \"derivation_fa\":\"واژهٔ یونانی باستان σκέλος «ساق، ران» ستاکی است با پسوند ـes (*skel-es-) که مستقیم بر همین ریشه ساخته شده است؛ واتکینز آن را «صورت پسونددارِ *skel-es-» می‌خواند و پوکورنی (ص ۹۲۸) نخستین شاهدِ یونانیِ ریشهٔ *(s)kel- را همین واژه می‌آورد. انگیزهٔ نام‌گذاری نیز همان معنای ریشه است: پا اندامی است که خم می‌شود. ادعای نورایی درست است.\",\n \"sources\":[W_KOLON_L],\n \"ref_check\":[{\"ref\":\"POK:928\",\"status\":\"supports\",\"note\":\"IEW 928: \\\"Gr. skelos m. 'thigh', skelis, -idos 'Hinterfuss, hip, haunch' (Attic skelis)\\\" — first item of the Greek material under (s)kel-4.\"}],\n \"consulted\":[POK928,AHDSKEL,WLD597,\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.v. isosceles\",\"stance\":\"supports\",\"note\":\"\\\"fr. Gk. isoskeles, 'equal-legged', fr. isos, 'equal', and skelos, 'leg'\\\" — Klein's gloss for skelos is 'leg', as in the chart.\"}]})\n\ne0_nodes.append({\n \"id\":3,\"lang\":\"English\",\"words\":\"isosceles\",\"verdict\":\"confirmed\",\n \"derivation\":\"English isosceles (1550s, of a triangle with two equal sides) is Latin isoscelēs, a straight borrowing of Greek ἰσοσκελής isoskelḗs 'equal-legged' = ἴσος 'equal' + σκέλος 'leg' — the triangle's two equal sides being felt as its two legs. Klein: \\\"isosceles, adj. ... L., fr. Gk. isoskeles, 'equal-legged', fr. isos, 'equal', and skelos, 'leg'\\\"; Watkins lists ISOSCELES (with TRISKELION) under skel-3 §2. A learned borrowing through Latin, with no intermediate vernacular stage.\",\n \"derivation_fa\":\"واژهٔ انگلیسی isosceles «مثلث متساوی‌الساقین» (از میانهٔ سدهٔ شانزدهم میلادی) وام‌واژهٔ لاتینیِ isoscelēs است که خود عیناً از یونانی ἰσοσκελής گرفته شده: ἴσος «برابر» + σκέλος «ساق، پا»؛ دو ضلعِ برابرِ مثلث در یونانی «دو پا» انگاشته می‌شده است. کلاین و واتکینز هر دو همین زنجیره را می‌آورند. این وام‌گیری دانشورانه و مستقیم از راه لاتین است، بی‌هیچ میانجی مردمی. ادعای نورایی درست است.\",\n \"sources\":[E_ISO],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. skel-3 §2: \\\"Suffixed form *skel-es- in Greek skelos, leg: ISOSCELES, TRISKELION\\\"; the AHD index line also reads \\\"ISOSCELES skel-3\\\".\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.v. isosceles (KLN_1971.txt line 127405)\",\"stance\":\"supports\",\"note\":\"\\\"isosceles, adj., having two equal sides (said of a triangle). — L., fr. Gk. isoskeles, 'equal-legged', fr. isos, 'equal', and skelos, 'leg'. ... cp. triskelion.\\\"\"},\n  AHDSKEL,\n  {\"src\":\"SKT\",\"where\":\"Skeat, Concise Etym. Dict.\",\"stance\":\"silent\",\"note\":\"grep of 'isosceles' in SKT.txt returns nothing — Skeat's concise edition has no entry for this technical term.\"}]})\n\ne0_nodes.append({\n \"id\":4,\"lang\":\"Greek\",\"words\":\"skhelos, kellos\",\"verdict\":\"transcription_suspect\",\n \"derivation\":\"Both words are real Greek, but the first is misspelt. Walde-Pokorny II 598 — the page Nourai cites as WLD:597, where the root '4. sqel- krumm' begins — lists, side by side, σκελλός (skellós) glossed 'διεστραμμένος, pandus, scaurus' (twisted, bandy-legged) and the Hesychian gloss κελλόν· στρεβλόν, πλάγιον (kellón 'crooked, slanting'); Pokorny 928 repeats both (\\\"skellos 'bowlegged' ... kellon streblon, plagion Hes.\\\"). There is no Greek word *σχελος / skhelos meaning 'crooked'; the printed page of Nourai shows 'skhelos, kellos', so the -h- is the book's own slip for skellos (the doubled -ll- misread or mistyped as -lh-). The chart's second form 'kellos' is the Hesychian neuter κελλόν cited in the masculine nominative, which is a normalisation rather than an error. With those two corrections the node is sound: both are o-grade/zero-grade adjectives of *(s)kel- meaning 'bent, crooked'. Note also that S. E. Mann's Indo-European Comparative Dictionary does have a lemma spelt 'skhelos', but it means 'wrong, fraud' (Lat. scelus, Skt. chalaḥ) and belongs to a different (s)kel- root — so that lemma cannot rescue the chart's gloss 'crooked'.\",\n \"derivation_fa\":\"هر دو واژه یونانی‌اند اما صورتِ نخست غلط چاپ شده است. والده-پوکورنی (جلد دوم، ص ۵۹۸ — همان بخشی که نورایی با ارجاع WLD:597 به آن اشاره می‌کند) در کنار هم σκελλός «کج، کمان‌پا» و گلوسهٔ هزیخیوسی κελλόν «کج، اریب» را می‌آورد و پوکورنی (ص ۹۲۸) نیز همین دو را تکرار می‌کند. در یونانی واژه‌ای به صورت *σχελος / skhelos با معنای «کج» وجود ندارد؛ پس «skhelos» دگرگونهٔ نادرستِ skellos است (دو لامِ مشدّد به «لـه» بدخوانده یا بدچاپ شده). صورت دوم، «kellos»، همان κελλόν است که به حالت فاعلیِ مذکر هنجارین شده و ایرادی بر آن نیست. با این دو اصلاح، گرهٔ چارت درست است: هر دو صفت‌هایی از ریشهٔ *(s)kel- به معنی «خمیده، کج»‌اند. یادآوری: در فرهنگ مان (IEC) سرواژه‌ای به املای skhelos هست، اما معنای آن «نادرستی، فریب» (لاتین scelus) است و به ریشهٔ دیگری می‌رسد، پس معنای «کج» را توجیه نمی‌کند. داوری: خطای چاپی کتاب، نه خطای خوانش اسکن.\",\n \"error_in\":\"book\",\"book_prints\":\"skhelos, kellos\",\"correct_form\":\"skellos (σκελλός), kellon (κελλόν)\",\n \"sources\":[W_KOLON_L],\n \"ref_check\":[\n  {\"ref\":\"WLD:597\",\"status\":\"supports\",\"note\":\"WP II 597-598 is the root '4. sqel- krumm'; the Greek material on p.598 (WLD_Bd2_pages.txt leaf 603) reads \\\"skellos 'diestrammenos, pandus, scaurus' ... kellon streblon, plagion Hes., kullos 'gekrummt, gelaehmt'\\\". The forms are there; the transliteration 'skhelos' is not.\"},\n  {\"ref\":\"OEW:363\",\"status\":\"not_checked\",\"note\":\"J. T. Shipley, The Origins of English Words (1984) is lending-only on archive.org and has no local copy (refs_online.json: local_file null, 'Borrow via IA lending; djvu.txt returns 401/403').\"}],\n \"consulted\":[WLD597,POK928,\n  {\"src\":\"IEC\",\"where\":\"Mann, IEC col. 1240-ish, lemma 'skhelos' (IEC.txt line 16052)\",\"stance\":\"contradicts\",\"note\":\"\\\"skhelos, om 'wrong, fraud'. Cf. skel- (3). Cf. WP II, 598: Skt. chalah id.; khalah 'rogue'; Lat. scelus 'wickedness; villain'; MHG schel 'deceiver'\\\" — Mann's skhelos is the 'crime' root, not the 'crooked' one; his cross-reference at line 15560 reads \\\"skelos, see skhelos and cf. skel- (3)\\\".\"}]})\n\ne0_nodes.append({\n \"id\":5,\"lang\":\"Persian\",\"words\":\"kol\",\"verdict\":\"plausible\",\n \"derivation\":\"The Persian word is genuine and does belong to this root, but not as a descendant of Greek. کَل kol/kul 'crooked, curved' is listed by Walde-Pokorny II 598 inside the sqel- 'krumm' article itself — \\\"np. kul 'krumm, gekrümmt' (s. Hübschmann Arm. Gr. I 457)\\\" — i.e. as an independent Iranian cognate; Horn no. 861 (p.192) does the same: \\\"861. kul 'krumm, gekrümmt'. Nach Nöldeke zu gr. κυλλός 'krumm'\\\", adding that Fortunatov instead linked κυλλός to Skt. kuṇi- 'lame in the arm' (< *kulni-), which would loosen the tie. Moʿin's Farhang has the headword کل with the bracketed etymological gloss '[کج؛ منحنی]' and the definition 'منحنی، کج. کجی، انحنا'. So the word, the meaning and the root membership are all confirmed; what is wrong is the arrow: the chart hangs Persian kol under the Greek box, which would make it a Greek loanword, whereas every source treats it as a sister form inherited in Iranian (PIE *kul-no- / *kel- beside Gk. κυλλός). Nourai's own layout elsewhere uses this position for cognates, so this is probably a diagram artefact rather than a claim of borrowing — but as drawn it is wrong.\",\n \"derivation_fa\":\"واژهٔ فارسی درست است و به همین ریشه می‌رسد، اما نه از راه یونانی. والده-پوکورنی (ج۲ ص۵۹۸) خودِ «کل» فارسی را درونِ مقالهٔ ریشهٔ sqel- «کج» می‌آورد: «np. kul 'krumm, gekrümmt'» — یعنی همتای مستقلِ ایرانی، نه وام‌واژه. هرن نیز (شمارهٔ ۸۶۱، ص ۱۹۲) می‌نویسد «کل: کج و خمیده؛ به گفتهٔ نولدکه با κυλλός یونانی مربوط است»، و می‌افزاید که فورتوناتف κυλλός را به‌جای آن با kuṇi- سنسکریت «شل‌دست» سنجیده است. معین نیز سرواژهٔ «کل» را با یادداشت «[کج؛ منحنی]» و معنای «منحنی، کج؛ کجی، انحنا» ثبت کرده است. پس واژه، معنا و تعلق آن به ریشه تأیید می‌شود و تنها ایراد، جهتِ پیکان است: چارت «کل» را زیرِ جعبهٔ یونانی نشانده که یعنی وام‌گیری از یونانی، حال آنکه همهٔ منابع آن را هم‌ریشه (cognate) می‌دانند نه وام‌واژه. با احتیاط پذیرفتنی است.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"WLD:597\",\"status\":\"supports\",\"note\":\"The word stands in the sqel- 'krumm' article, WP II 598 (leaf 603): \\\"np. kul 'krumm, gekrummt' (s. Huebschmann Arm. Gr. I 457)\\\" — but as an Iranian cognate listed beside Gk. skellos/kullos, not as derived from Greek.\"},\n  {\"ref\":\"HRN:192\",\"status\":\"supports\",\"note\":\"Horn p.192 no. 861 (HRN.txt leaf 213): \\\"861. kul 'krumm, gekruemmt'. Nach Noeldeke (muendliche Mitteilung) zu gr. kullos 'krumm'. Dann vergl. auch gr. kurtos 'gekruemmt', aw. skarena- 'rund'. — Fortunatow stellt (BB. 6, 216) gr. kullos zu skr. kuni- 'lahm am Arm' (aus *kulni-).\\\" Footnote: the word is attested in a verse of the pre-Ferdowsi poet Abū Shakūr.\"},\n  {\"ref\":\"MON:3012\",\"status\":\"partial\",\"note\":\"Mo'in's 6-vol pagination cannot be checked (no scan online). The 2-vol Adena condensation (MON_part2.txt line 24408) has the headword: 'کل: [کج؛ منحنی] (ص.) منحنی، کج. کجی، انحنا' — word and gloss confirmed, page not verifiable.\"}],\n \"consulted\":[WLD597,\n  {\"src\":\"HRN\",\"where\":\"no. 861, p.192\",\"stance\":\"supports\",\"note\":\"see ref_check; Horn treats NP kul as a cognate of Gk. kullos, not a loan.\"},\n  {\"src\":\"MON\",\"where\":\"MON_part2.txt line 24408\",\"stance\":\"supports\",\"note\":\"'کل: [کج؛ منحنی] (ص.) منحنی، کج.'\"},\n  {\"src\":\"POK\",\"where\":\"IEW 928\",\"stance\":\"silent\",\"note\":\"Pokorny lists kullos and kellon but no Iranian form; he cites no Persian reflex of (s)kel-4.\"}]})\n\ne0_nodes.append({\n \"id\":6,\"lang\":\"Greek\",\"words\":\"kulindein\",\"verdict\":\"plausible\",\n \"derivation\":\"Greek κυλίνδειν (kylíndein) 'to roll, roll up' (with the nouns κύλινδρος 'roller, cylinder', κυλίνδρα) is a real and well-attested verb, but its attachment to *(s)kel- is precisely the doubtful link of this article, and Nourai's chart gives no hint of that. Watkins states it with an explicit warning: \\\"6. Attributed (quite doubtfully) by some to this root is Greek kulindein, to roll: CALENDER, CYLINDER.\\\" Pokorny 928 does list \\\"kulindo, -eo 'rolle, walze' (Ionian Attic kalindeo), kulindros 'Walze, pulley, Zylinder'\\\" under (s)kel-4, and Klein says only \\\"prob. derives fr. I.-E. base *(s)qel 'to bend, twist'\\\". Etymonline/Beekes call the verb's origin simply unknown, and a rival tradition connects it to *kʷel- 'turn' (the κύκλος family). Formally the ku- vocalism is the same problem as in κυλλός, for which Pokorny has to posit a 'reduced grade' *kul-. So: root, language and gloss are right; the edge root→kulindein is accepted by some and doubted by others.\",\n \"derivation_fa\":\"فعل یونانی κυλίνδειν «غلتاندن، لولیدن» (با اسم κύλινδρος «غلتک، استوانه») واژه‌ای اصیل و پرکاربرد است، اما پیوند آن به ریشهٔ *(s)kel- همان حلقهٔ مشکوکِ این مقاله است و چارت نورایی هیچ نشانی از این تردید نمی‌دهد. واتکینز صریحاً هشدار می‌دهد: «برخی — با تردیدِ بسیار — kulindein یونانی را به این ریشه بازمی‌گردانند». پوکورنی (ص ۹۲۸) آن را زیر *(s)kel-4 می‌آورد و کلاین تنها می‌نویسد «احتمالاً از پایهٔ *(s)qel-». در برابر، اتیمانلاین و بیکس خاستگاه این فعل را ناشناخته می‌دانند و سنتی دیگر آن را به *kʷel- «چرخیدن» (خانوادهٔ κύκλος) می‌بندد. مشکل آوایی نیز همان واکهٔ u است که پوکورنی ناچار می‌شود برای آن «درجهٔ کاهیده» *kul- بازسازی کند. پس ریشه، زبان و معنا درست است ولی پیکانِ «ریشه ← kulindein» را همه نپذیرفته‌اند: با احتیاط پذیرفتنی است.\",\n \"sources\":[E_CYL],\n \"ref_check\":[\n  {\"ref\":\"POK:928\",\"status\":\"supports\",\"note\":\"IEW 928 under (s)kel-4: \\\"kulindo, -eo 'rolle, walze' (Ionian Attic kalindeo), kulindros 'Walze, pulley, Zylinder'\\\" — Pokorny does put the verb here, without a caveat.\"},\n  {\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. skel-3 §6: \\\"Attributed (quite doubtfully) by some to this root is Greek kulindein, to roll: CALENDER, CYLINDER.\\\" The reference supports the words but flags the derivation as very uncertain — a caveat the chart drops.\"}],\n \"consulted\":[POK928,AHDSKEL,\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.v. cylinder (KLN_1971.txt line 62639)\",\"stance\":\"partial\",\"note\":\"\\\"Gk. kulindros, 'roller, roll, cylinder', fr. kulindein, 'to roll', which prob. derives fr. I.-E. base *(s)qel 'to bend, twist', whence also Gk. kullos ... kolon, 'limb, member'.\\\" — 'prob.', i.e. hedged.\"}]})\n\ne0_nodes.append({\n \"id\":7,\"lang\":\"French\",\"words\":\"\",\"verdict\":\"confirmed\",\n \"derivation\":\"Pass-through node for the French stage that both English words go through. Latin cylindrus (borrowed from Gk. κύλινδρος) gave Old/Middle French cylindre, the source of English cylinder (late 14c.); and, by a separate popular route, Vulgar Latin *colendra > Medieval Latin calendra > Old French calandre 'a roller, mangle, cloth-press', whence French calandrer 'to calender' and English calender (1510s). Klein sets both out: \\\"cylinder, n. — F. cylindre, fr. L. cylindrus, fr. Gk. kulindros\\\" and \\\"calender, n., machine with rollers for pressing cloth. — F. calandre, ... fr. earlier *colandre, fr. VL. *colendra, fr. Gk. kulindros.\\\" Modern Persian سیلندر comes through the same French word.\",\n \"derivation_fa\":\"این گره، گرهِ گذرِ فرانسوی است که هر دو واژهٔ انگلیسی و نیز واژهٔ فارسی از آن می‌گذرند. لاتینِ cylindrus (وام از یونانی κύλινδρος) در فرانسهٔ کهن به cylindre بدل شد و انگلیسی cylinder را از آن گرفت؛ و از راهی جداگانه و مردمی، لاتینِ عامیانهٔ *colendra > لاتینِ میانهٔ calendra > فرانسهٔ کهنِ calandre «غلتک، دستگاه فشردن پارچه» پدید آمد که فعل calandrer و انگلیسیِ calender از آن است. کلاین هر دو زنجیره را می‌آورد. «سیلندر» فارسی نیز از همین واژهٔ فرانسوی گرفته شده است. ادعای نورایی درست است.\",\n \"sources\":[E_CYL],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the chart gives this node no reference of its own; it is covered by the AHD citation on the daughter node #9.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.vv. cylinder, calender (KLN_1971.txt lines 62639, 37230)\",\"stance\":\"supports\",\"note\":\"\\\"cylinder, n. — F. cylindre, fr. L. cylindrus, fr. Gk. kulindros\\\"; \\\"calender, n., machine with rollers for pressing cloth. — F. calandre, 'calender, roller, mangle', fr. earlier *colandre, fr. VL. *colendra, fr. Gk. kulindros.\\\"\"},\n  {\"src\":\"SKT\",\"where\":\"Skeat s.v. Calender (SKT.txt line 2629)\",\"stance\":\"supports\",\"note\":\"\\\"Calender, a machine for pressing cloth; see Cylinder.\\\" — Skeat too routes calender through the cylinder word.\"},\n  {\"src\":\"DEV\",\"where\":\"Devic, Dict. étym. des mots français d'origine orientale\",\"stance\":\"silent\",\"note\":\"grep finds no entry — Devic covers only Oriental-origin French words, and calandre/cylindre are Greek, so his silence is expected and confirms the word is not an Arabism.\"}]})\n\ne0_nodes.append({\n \"id\":8,\"lang\":\"Persian\",\"words\":\"sîlandr\",\"verdict\":\"plausible\",\n \"derivation\":\"سیلندر sīlandr 'cylinder (of an engine)' is a 20th-century European technical loan in Persian, not an inherited word, and Mo'in treats it as such: his headword reads 'سیلندر: ... (ا.) استوانه. ضح. به این معنی احتراز از استعمال این کلمهٔ بیگانه اولی است' (\\\"better to avoid this foreign word\\\"), followed by the mechanical sense 'لوله‌ای است استوانه‌یی شکل که در موتور اتومبیل تعبیه شده'; the compound سرسیلندر 'cylinder head' carries the origin tag '[اف. فر.]'. French cylindre [silɛ̃dʁ] explains the Persian initial سی- s-ī- (English 'cylinder' would give سیلیندر), so Nourai's routing through French is the likelier of the two, and matches the general pattern of Persian automotive vocabulary (پیستون, کاربراتور, دلکو), which came in through French in the Reza Shah period. It is 'plausible' rather than 'confirmed' only because Mo'in's own tag leaves English open.\",\n \"derivation_fa\":\"«سیلندر» وام‌واژه‌ای اروپایی و نوپدید (سدهٔ چهاردهم خورشیدی) است، نه واژه‌ای موروثی. معین آن را چنین ثبت کرده است: «سیلندر: ... (ا.) استوانه. ضح. به این معنی احتراز از استعمال این کلمهٔ بیگانه اولی است» و سپس معنای مکانیکی «لوله‌ای است استوانه‌یی شکل که در موتور اتومبیل تعبیه شده»؛ ترکیب «سرسیلندر» نیز با نشانِ خاستگاه «[اف. فر.]» آمده است. تلفظ فرانسویِ cylindre («سیلَندْر») توضیح‌دهندهٔ صورتِ فارسی است — اگر از انگلیسی می‌آمد «سیلیندر» انتظار می‌رفت — و این با الگوی کلیِ واژگان خودروییِ فارسی (پیستون، کاربراتور، دلکو) که در دورهٔ رضاشاه از فرانسه وارد شد همخوان است. پس مسیرِ فرانسویِ نورایی محتمل‌تر است، هرچند نشانِ معین راهِ انگلیسی را هم باز می‌گذارد: با احتیاط پذیرفتنی است.\",\n \"sources\":[E_CYL],\n \"ref_check\":[{\"ref\":\"MON\",\"status\":\"partial\",\"note\":\"Mo'in (2-vol Adena condensation, MON_part1.txt line 82346): 'سیلندر: ... (ا.) استوانه. ضح. به این معنی احتراز از استعمال این کلمهٔ بیگانه اولی است. (مکد.) لوله‌ای است استوانه‌یی شکل که در موتور اتومبیل تعبیه شده'; line 77028 'سرسیلندر: [اف. فر.] (امر.) (مکد.) سرپوشی که انتهای فوقانی سیلندرها را می‌پوشاند.' Mo'in marks it a foreign loan but the citation carries no page number, and the 6-vol pagination is not online.\"}],\n \"consulted\":[\n  {\"src\":\"MON\",\"where\":\"MON_part1.txt lines 77028, 82346\",\"stance\":\"supports\",\"note\":\"see ref_check — headword present, explicitly flagged 'کلمهٔ بیگانه'.\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt\",\"stance\":\"silent\",\"note\":\"grep 'سیلندر' returns nothing; Aryanpur's Indo-European roots dictionary does not treat modern technical loans.\"},\n  {\"src\":\"BQT\",\"where\":\"BQT_v3_pages.txt\",\"stance\":\"silent\",\"note\":\"as expected — Borhan-e Qate' is a 17th-century dictionary and cannot contain a 20th-century loan.\"}]})\n\ne0_nodes.append({\n \"id\":9,\"lang\":\"English\",\"words\":\"cylinder, calender\",\"verdict\":\"confirmed\",\n \"derivation\":\"Two words, one Greek source, two routes. cylinder (late 14c., first of a cylindrical portable sundial) < Old French cylindre < Latin cylindrus < Greek κύλινδρος 'roller, cylinder', from κυλίνδειν 'to roll'. calender 'machine with rollers for pressing cloth' (1510s) is the same Greek word taken through a popular Latin chain: Greek κύλινδρος > Vulgar Latin *colendra > Medieval Latin calendra > Old French calandre, whence the agent-noun calandreur and the verb calandrer; the vowel changes (ky- > co- > ca-) are the ordinary reductions of an unstressed opening syllable in Vulgar Latin. Watkins lists both under skel-3 §6 (\\\"CALENDER, CYLINDER\\\"), and Klein and Skeat agree. This calender must not be confused with English calendar (< Latin kalendae) nor with the other calender 'mendicant dervish' (< Persian قلندر qalandar), both unrelated.\",\n \"derivation_fa\":\"دو واژه با یک خاستگاه یونانی و دو مسیر. cylinder (اواخر سدهٔ چهاردهم میلادی، نخست به معنی ساعت آفتابیِ استوانه‌ای) از فرانسهٔ کهنِ cylindre < لاتینِ cylindrus < یونانیِ κύλινδρος «غلتک، استوانه» از κυλίνδειν «غلتاندن». اما calender «دستگاه غلتکیِ فشردنِ پارچه» (سدهٔ شانزدهم) همان واژهٔ یونانی است که از راهی مردمی آمده: κύλινδρος > لاتینِ عامیانهٔ *colendra > لاتینِ میانهٔ calendra > فرانسهٔ کهنِ calandre؛ دگرگونی واکه‌ها (ky- > co- > ca-) همان کاهشِ معمولِ هجای بی‌تکیهٔ آغازین در لاتینِ عامیانه است. واتکینز هر دو را زیر skel-3 آورده و کلاین و اسکیت نیز همین را می‌گویند. این calender را نباید با calendar «تقویم» (از kalendae لاتین) یا با calender «درویشِ قلندر» (از «قلندر» فارسی) اشتباه گرفت. ادعای نورایی درست است.\",\n \"sources\":[E_CYL],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. skel-3 §6 lists both words: \\\"CALENDER, CYLINDER\\\"; the index lines read \\\"CALENDER skel-3\\\" and \\\"CYLINDER skel-3\\\".\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.vv. cylinder, calender (lines 62639, 37230, 37234)\",\"stance\":\"supports\",\"note\":\"\\\"cylinder, n. — F. cylindre, fr. L. cylindrus, fr. Gk. kulindros\\\"; \\\"calender ... — F. calandre ... fr. VL. *colendra, fr. Gk. kulindros\\\"; \\\"calender, tr. v. — F. calandrer\\\". Klein keeps the dervish word ('calender, n., a mendicant dervish. — Pers. qalender') strictly separate.\"},\n  {\"src\":\"SKT\",\"where\":\"Skeat s.v. Calender (line 2629)\",\"stance\":\"supports\",\"note\":\"\\\"Calender, a machine for pressing cloth; see Cylinder.\\\"\"},\n  AHDSKEL]})\n\ne0_nodes.append({\n \"id\":10,\"lang\":\"Greek\",\"words\":\"kôlon\",\"verdict\":\"disputed\",\n \"derivation\":\"The chart merges two different Greek words into one box. (a) κῶλον kōlon (long o, omega) 'limb, member (of a body); member of a clause' is the one Watkins and Pokorny put here — \\\"Suffixed lengthened-grade form *kōl-o- in Greek kōlon, limb, member: COLON(1)\\\" — and it is the source of the punctuation colon of node #14; Klein adds the related κωλέα, κωλῆ 'thighbone' and cognate OCS koleno 'knee'. Even that much is now contested: Beekes (via Wiktionary) prefers a Pre-Greek origin for κῶλον. (b) κόλον kólon (short o, omicron) 'large intestine' is a wholly separate word: Wiktionary states flatly \\\"No relation to κῶλον (kôlon, 'limb')\\\", its origin is uncertain (Beekes links it to words for 'guts'), and it is the word that gave Latin cōlon 'colon (anatomy)', Syriac ܩܘܠܘܢ qōlōn and hence Arabic قولون. Klein and Skeat both keep the two apart in separate entries (Klein: \\\"colon, n., that part of the larger intestine ... fr. Gk. kolon, 'large intestine', which is of uncertain origin\\\"). So the gloss 'limb, part, member' is supported by Nourai's own reference AHD, but the added 'large intestine' imports an unrelated homonym — and that sense is what carries the whole Arabic/Persian branch below.\",\n \"derivation_fa\":\"چارت دو واژهٔ متفاوتِ یونانی را در یک جعبه درهم آمیخته است. الف) κῶλον (با اُمگا، یعنی ō) «اندام، عضو؛ بندِ جمله» همان است که واتکینز و پوکورنی زیر این ریشه می‌آورند («صورت کشیدهٔ پسونددارِ *kōl-o-: یونانی kōlon 'اندام، عضو' ← COLON») و همان است که «کولن» نشانهٔ نقطه‌ویرگول از آن آمده؛ کلاین نیز κωλέα/κωλῆ «استخوان ران» و هم‌ریشهٔ اسلاویِ koleno «زانو» را کنار آن می‌گذارد. حتی همین اندازه هم امروز مناقشه‌آمیز است: بیکس خاستگاه پیشایونانی (Pre-Greek) را ترجیح می‌دهد. ب) κόλον (با اُمیکرون، یعنی o کوتاه) «رودهٔ بزرگ» واژه‌ای یکسره جداست؛ ویکی‌واژه صریحاً می‌نویسد «هیچ نسبتی با κῶλον ندارد»، خاستگاهش نامعلوم است، و همین واژه است که به لاتینِ cōlon، سریانیِ ܩܘܠܘܢ و از آنجا به «قولون» عربی رسیده است. کلاین و اسکیت نیز این دو را در دو مدخل جدا نگه داشته‌اند. پس معنای «اندام، عضو» را منبعِ خودِ نورایی (AHD) تأیید می‌کند، ولی افزودنِ «رودهٔ بزرگ» هم‌آواییِ بی‌ربطی را وارد کرده است — و درست همین معنای افزوده است که کل شاخهٔ عربی و فارسیِ زیرِ آن را بر دوش می‌کشد. پژوهش امروزی این بخش را رد می‌کند.\",\n \"sources\":[W_KOLON_L,W_KOLON_S,E_COLON],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. skel-3 §5: \\\"Suffixed lengthened-grade form *kol-o- in Greek kolon, limb, member: COLON(1).\\\" Watkins gives only the 'limb, member' sense and only COLON(1) (the punctuation mark); the AHD index line reads \\\"COLON! | skel-3\\\" — COLON(2), the intestine, is in no IE-root entry at all.\"}],\n \"consulted\":[\n  POK928,\n  {\"src\":\"KLN\",\"where\":\"Klein 1971, two separate entries s.v. colon (KLN_1971.txt lines 51054, 51060)\",\"stance\":\"partial\",\"note\":\"\\\"colon, n., that part of the larger intestine, which extends from the caecum to the rectum (anat.) — L., fr. Gk. kolon, 'large intestine', which is of uncertain origin.\\\" vs. \\\"colon, n., the punctuation mark: — L. colon, fr. Gk. kolon, 'limb, member; member of a clause or a sentence', which is rel. to kolea, kole, 'thighbone', and cogn. with OSlav. koleno, 'knee' ... fr. I.-E. base *(s)qel-, 'crooked, bent'.\\\" Klein supports the second half of the chart's gloss and contradicts the first.\"},\n  {\"src\":\"SKT\",\"where\":\"Skeat s.vv. Colon (1), Colon (2) (SKT.txt line 3733)\",\"stance\":\"partial\",\"note\":\"\\\"Colon (1), a mark (:) in writing and printing. (Gk.) Gk. kolon, a clause, hence a stop marking off a clause. Colon (2), part of the intestines. (Gk.) Gk. kolon, the same.\\\" — again two entries, two Greek words.\"},\n  {\"src\":\"WEB\",\"where\":\"Webster's New Twentieth Century Dict., 2nd ed., medical compounds (WEB_vol1.txt lines 36939, 37358)\",\"stance\":\"partial\",\"note\":\"\\\"Gr. kolon, the large intestine, colon\\\" is the etymon given for colon, colitis, colotomy etc. — the medical family goes back to the short-o word throughout.\"}]})\n\ne0_nodes.append({\n \"id\":11,\"lang\":\"Arabic\",\"words\":\"\",\"verdict\":\"plausible\",\n \"derivation\":\"Pass-through node for the Arabic medical vocabulary. The Arabic forms are قُولُون qūlūn 'the colon' and قُولَنْج qūlanj 'colic', both Greek loans that entered Arabic with the ninth-century Baghdad translations of Galen and Hippocrates — normally through Syriac, where Classical Syriac ܩܘܠܘܢ qōlōn is attested as the direct descendant of Greek κόλον; qūlanj renders Greek κωλικός/κολικός 'of the colon, colic'. Al-ʿUnaysī's Tafsīr al-alfāẓ al-dākhila (TAD), the reference Nourai cites, has the entry: 'قولنج ... مرض يصيب القولون ... [من] اليوناني الذي معناه شعبة من الأمعاء الغلاظ ... وهو في الأعور والمستقيم' — a disease affecting the colon, from the Greek word meaning a section of the thick intestines. So the Greek→Arabic arrow is real; what fails is the box above it, since the Greek source is κόλον, not the κῶλον 'limb' of the root. Nourai's Arabic box is left empty on the printed page, so no Arabic form of his own is being asserted.\",\n \"derivation_fa\":\"این گره، گرهِ گذرِ عربی است. صورت‌های عربی «قُولُون» (رودهٔ بزرگ) و «قُولَنْج» (درد قولون) هر دو وام‌واژه‌های یونانی‌اند که در سدهٔ سوم هجری، همراه با ترجمهٔ آثار جالینوس و بقراط در بغداد، و معمولاً از راهِ سریانی وارد عربی شدند؛ در سریانی ܩܘܠܘܢ (qōlōn) بازماندهٔ مستقیم κόλον یونانی گواهی شده است، و «قولنج» برگردانِ κωλικός/κολικός «مربوط به قولون» است. کتابِ «تفسیر الألفاظ الدخیلة» اثر طوبیا العنیسی — همان مرجعی که نورایی به آن ارجاع می‌دهد — چنین دارد: «قولنج ... مرض یصیب القولون ... [من] الیونانی الذی معناه شعبة من الأمعاء الغلاظ». پس پیکانِ «یونانی ← عربی» درست است؛ آنچه نادرست است جعبهٔ بالای آن است، زیرا خاستگاهِ یونانی κόλον است نه κῶλον («اندام») که به ریشهٔ Skel می‌رسد. در صفحهٔ چاپی، جعبهٔ عربی خالی است و نورایی صورتِ عربیِ مشخصی را ادعا نکرده است.\",\n \"sources\":[W_KOLON_S,E_COLON],\n \"ref_check\":[{\"ref\":\"TAD:59\",\"status\":\"supports\",\"note\":\"al-'Unaysi, Tafsir al-alfaz al-dakhila, leaf 62 of the 87-leaf scan (printed page ≈57-59; TAD_pages.txt line 2301, TAD.txt line 2433): 'قوأنج [=قولنج] ... مرض تصيب القولون ... اليوناني الذي معناه شعبة من الأمعاء الغلاظ ... وهو في الأعور والمستقيم'. The Greek origin of the Arabic medical term is exactly what the arrow claims; only the printed page number could not be read (no scan of TAD is registered in refs_online.json for ref_page.py, which answered 'no scan of TAD covers printed page 59').\"}],\n \"consulted\":[\n  {\"src\":\"TAD\",\"where\":\"leaf 62 (printed ≈57-59)\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n  {\"src\":\"AFM\",\"where\":\"Addi Shir, Kitab al-Alfaz al-Farisiyya al-Mu'arraba\",\"stance\":\"silent\",\"note\":\"grep of 'قولنج' / 'قولون' in AFM.txt and AFM_pages.txt returns only the verb يقولون — Addi Shir has no entry, which is expected: his book collects PERSIAN loans in Arabic, and this one is Greek.\"},\n  {\"src\":\"FVQ\",\"where\":\"Jeffery, Foreign Vocabulary of the Qur'an\",\"stance\":\"silent\",\"note\":\"no entry (the word is not Qur'anic).\"},\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.v. colon (intestine)\",\"stance\":\"partial\",\"note\":\"\\\"L., fr. Gk. kolon, 'large intestine', which is of uncertain origin\\\" — confirms the Greek word behind the Arabic borrowing but denies it an IE root.\"}]})\n\ne0_nodes.append({\n \"id\":12,\"lang\":\"Persian\",\"words\":\"qǔlǔn\",\"verdict\":\"plausible\",\n \"derivation\":\"قولون qūlūn 'colon (large intestine)' and its doublets قولنج / کولنج qūlanj, kūlanj 'colic' are in Persian as Arabic-mediated Greek medical terms, taken over with the Arabic medical literature (Rāzī, Ibn Sīnā) and standard in Persian medicine ever since. Borhan-e Qate' itself has the native-sounding headword کولنج and claims the opposite direction — 'بروزن و معنی قولنج باشد ... و قولنج معرب [کولنج] است' (qūlanj is the Arabicised form of Persian kūlanj) — but Moʿin's editorial footnote on the same page corrects it, writing: 'کولنج (معرب) معرب از یونانی κωλικός ... (colon = kōlon) (فر) colique ... [قولنج] مرضی است آلی که در امعاء غلاظ ... حاصل شود'. Moʿin's own Farhang likewise tags the headword 'قولنج: [معر.] (ا.) (پز.) دردی که غفلتاً در ناحیهٔ شکم خصوصاً قولون‌ها حاصل شود'. So the route Greek → Arabic → Persian that Nourai draws is right, and Moʿin explicitly names the Greek etymon; the reservation is again the box two levels up, since the Greek source is κόλον/κωλικός (intestine, colic), not the κῶλον 'limb' of PIE *(s)kel-. The variant کولنج with k- is the ordinary Persian de-Arabicisation of a q- that was itself only a transcription of Greek κ.\",\n \"derivation_fa\":\"«قولون» و دوگانه‌های آن «قولنج / کولنج» اصطلاحاتی پزشکی‌اند که از یونانی از راه عربی به فارسی رسیده‌اند و همراه با طبّ عربی (رازی، ابن‌سینا) در فارسی جا افتاده‌اند. خودِ برهان قاطع سرواژهٔ «کولنج» را فارسی می‌انگارد و جهت را وارونه می‌کند: «بروزن و معنی قولنج باشد ... و قولنج معرب [کولنج] است»؛ اما حاشیهٔ ریشه‌شناختیِ معین در همان صفحه آن را تصحیح می‌کند: «کولنج (معرب): معرب از یونانی κωλικός ... (colon = kōlon) (فر) colique». در فرهنگ فارسیِ معین نیز مدخل چنین است: «قولنج: [معر.] (ا.) (پز.) دردی که غفلتاً در ناحیهٔ شکم خصوصاً قولون‌ها حاصل شود». پس مسیرِ «یونانی ← عربی ← فارسی» که نورایی کشیده درست است و معین نیز صریحاً ریشهٔ یونانی را نام می‌برد؛ تنها ایراد، همان جعبهٔ دو رده بالاتر است، چون خاستگاهِ یونانی κόλον/κωλικός («روده»، «قولنجی») است نه κῶλον («اندام») که به ریشهٔ هندواروپاییِ *(s)kel- می‌رسد. گونهٔ «کولنج» با کاف نیز همان فارسی‌شدنِ معمولِ قافی است که خود تنها آوانگاریِ κ یونانی بوده است.\",\n \"sources\":[W_KOLON_S,E_COLON],\n \"ref_check\":[\n  {\"ref\":\"BQT:1548\",\"status\":\"supports\",\"note\":\"Borhan-e Qate', printed 1547 in the scan used here (BQT_v3_pages.txt pdf page 341; printed = pdf + 1206): headword 'قولنج ... معرب گولنج است که درد شکم و درد پهلو باشد', with Mo'in's footnote 8: 'ح کولنج (معرب) معرب از یونانی κωλικός «زابا ص۳۱» (colon = kōlon) (فر) colique ... از امعاء غلاظ بین الأعور و المستقیم «نفیس»؛ قولنج مرضی است آلی که در امعاء غلاظ بجهت احتباس غیر طبیعی حاصل شود'. That footnote is precisely Nourai's claim. The related entry کولنج (with Borhan's contrary claim of a Persian origin) is at printed 1739 (pdf 533).\"},\n  {\"ref\":\"MON:2749\",\"status\":\"partial\",\"note\":\"Mo'in's 6-vol pagination cannot be checked (no scan online). The 2-vol Adena condensation (MON_part2.txt lines 15806-15861) has both headwords: 'قولنج: [معر.] (ا.) (پز.) دردی که غفلتاً در ناحیهٔ شکم خصوصاً قولون‌ها حاصل شود' and a long anatomical article on قولون (قولون صاعد، نازل، عرضی ...). Word, Arabic-loan tag and sense confirmed; page not verifiable.\"},\n  {\"ref\":\"ETM:45\",\"status\":\"not_checked\",\"note\":\"Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374 — refs_online.json records 'no digital copy on any permitted platform; catalogue/purchase only' (re-searched 2026-09).\"}],\n \"consulted\":[\n  {\"src\":\"BQT\",\"where\":\"printed 1547 (Mo'in's footnote 8) and 1739 (کولنج)\",\"stance\":\"supports\",\"note\":\"see ref_check; Mo'in's footnote states the Greek origin outright and even prints 'colon = kōlon'.\"},\n  {\"src\":\"MON\",\"where\":\"MON_part2.txt lines 15806ff\",\"stance\":\"supports\",\"note\":\"'قولنج: [معر.]' — Mo'in tags it an Arabic loan.\"},\n  {\"src\":\"TAD\",\"where\":\"leaf 62\",\"stance\":\"supports\",\"note\":\"'قولنج ... مرض تصيب القولون ... اليوناني' — the Arabic stage of the same chain.\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt\",\"stance\":\"silent\",\"note\":\"no entry for قولون/قولنج; Aryanpur treats only Indo-European inherited vocabulary.\"}]})\n\ne0_nodes.append({\n \"id\":13,\"lang\":\"Latin\",\"words\":\"\",\"verdict\":\"confirmed\",\n \"derivation\":\"Pass-through node for the Latin stage. Latin cōlon, -ī n. is a learned borrowing of Greek κῶλον, taken into Roman rhetorical writing (Cicero, Quintilian) in the technical sense 'a member of a period, a clause of a sentence' — and, as the metrical term, 'part of a verse'. (Latin also has the homonym colon 'large intestine', separately borrowed from Greek κόλον; that one feeds the medical vocabulary, not the punctuation word.) From the rhetorical Latin word, via the sixteenth-century printers' use of the term for the mark that sets off such a clause, comes English colon at node #14.\",\n \"derivation_fa\":\"این گره، گرهِ گذرِ لاتین است. واژهٔ لاتینِ cōlon وام‌واژه‌ای دانشورانه از κῶλον یونانی است که در نوشته‌های بلاغیِ رومی (سیسرون، کوئینتیلیانوس) در معنای فنیِ «بندِ یک دورهٔ کلام، جملهٔ پیوسته» و نیز «بخشی از بیت» به‌کار رفته است. (لاتین هم‌آوایِ دیگری نیز دارد: colon «رودهٔ بزرگ» که جداگانه از κόλον یونانی وام گرفته شده و واژگانِ پزشکی از آن می‌آید، نه نشانهٔ سجاوندی.) از همین واژهٔ بلاغیِ لاتین، و از کاربردِ چاپگرانِ سدهٔ شانزدهم برای نشانه‌ای که چنین بندی را جدا می‌کند، انگلیسیِ colon در گرهٔ بعد پدید آمده است. ادعای نورایی درست است.\",\n \"sources\":[E_COLON],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. skel-3 §5 ends the chain at \\\"COLON(1)\\\"; the AHD's own dictionary entry for colon(1) routes it 'Latin colon, from Greek kolon, limb, member, clause'.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.v. colon, the punctuation mark (line 51060)\",\"stance\":\"supports\",\"note\":\"\\\"colon, n., the punctuation mark: — L. colon, fr. Gk. kolon, 'limb, member; member of a clause or a sentence'.\\\"\"},\n  {\"src\":\"SKT\",\"where\":\"Skeat s.v. Colon (1) (line 3733)\",\"stance\":\"supports\",\"note\":\"\\\"Colon (1), a mark (:) in writing and printing. (Gk.) Gk. kolon, a clause, hence a stop marking off a clause.\\\" (Skeat compresses the Latin stage.)\"},\n  {\"src\":\"LAT\",\"where\":\"Ernout-Meillet, Dict. étym. de la langue latine\",\"stance\":\"silent\",\"note\":\"grep 'colon' / 'cōlon' in LAT.txt returns nothing usable from this OCR.\"}]})\n\ne0_nodes.append({\n \"id\":14,\"lang\":\"English\",\"words\":\"colon, semicolon\",\"verdict\":\"confirmed\",\n \"derivation\":\"colon (the punctuation mark) is first recorded in the 1540s, from Latin colon 'part of a verse or poem, clause', from Greek κῶλον 'limb, member; clause of a sentence'; the sense went 'limb' > 'clause' > 'the mark that sets a clause off'. semicolon (1640s) is a hybrid formed in English by prefixing Latin semi- 'half' to that colon, for a stop half as strong. Both are covered by Watkins's \\\"COLON(1)\\\" under skel-3. The English anatomical colon (late 14c.) is a different word and belongs to Greek κόλον — see node #10.\",\n \"derivation_fa\":\"واژهٔ انگلیسی colon در معنای نشانهٔ «دونقطه» نخستین‌بار در دههٔ ۱۵۴۰ میلادی ثبت شده و از لاتینِ colon «بخشی از بیت، بندِ کلام» و آن از یونانیِ κῶλον «اندام؛ بندِ جمله» می‌آید؛ سیرِ معنایی چنین بوده است: «اندام» ← «بندِ جمله» ← «نشانه‌ای که بندِ جمله را جدا می‌کند». واژهٔ semicolon (دههٔ ۱۶۴۰) ترکیبی دورگه است که در خودِ انگلیسی با افزودنِ پیشوندِ لاتینِ semi- «نیم» به همان colon ساخته شده، برای درنگی که نیمی از قوّتِ دونقطه را دارد. واتکینز هر دو را زیر COLON(1) و ریشهٔ skel-3 می‌آورد. اما colon انگلیسی در معنای «رودهٔ بزرگ» (اواخر سدهٔ چهاردهم) واژهٔ دیگری است و به κόλον یونانی بازمی‌گردد — نگاه کنید به گرهٔ ۱۰. ادعای نورایی درست است.\",\n \"sources\":[E_COLON],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. skel-3 §5: \\\"Greek kolon, limb, member: COLON(1)\\\"; AHD index: \\\"COLON! | skel-3\\\".\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.vv. colon (punctuation), semicolon (lines 51060, 217525)\",\"stance\":\"supports\",\"note\":\"\\\"colon, n., the punctuation mark: — L. colon, fr. Gk. kolon, 'limb, member; member of a clause or a sentence'\\\"; \\\"colon, n., a punctuation mark (;). — A hy[brid coinage]\\\" (Klein's semicolon entry: semi- + colon).\"},\n  {\"src\":\"SKT\",\"where\":\"Skeat s.v. Colon (1)\",\"stance\":\"supports\",\"note\":\"\\\"Gk. kolon, a clause, hence a stop marking off a clause.\\\"\"},\n  AHDSKEL]})\n\nentry0 = {\n \"entry\":0,\"root\":\"Skel 1\",\"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *(s)kel- 'to bend; crooked' (Pokorny 928, lemma '(s)kel-4'; Watkins/AHD 'skel-3. Also kel-. Crooked')\",\n \"note\":\"The root is real and correctly labelled. Pokorny IEW 928 has \\\"Root / lemma: (s)kel-4 (extended klā-, klō-) / Meaning: to bend; crooked\\\", with the Greek family σκέλος, σκελλός, σκολιός, σκώληξ, κελλόν, κυλλός, κυλίνδω, κῶλον; Walde-Pokorny II 597-598 is the same article ('4. sqel- krumm', which is Pokorny's own cross-reference 'WP. II 597 ff.'); Watkins prints \\\"skel-3. Also kel-. Crooked. With derivatives referring to a bent or curved part of the body, such as a leg, heel, knee, or hip. [Pok. 4. skel- 928.]\\\" Nourai's numbering 'Skel 1' is his own (it is Pokorny's fourth (s)kel-); his gloss 'bent, curved' is right, and his redirect 'Skel 2 -> Sek' takes care of the homonymous 'cut' root. Two weaknesses run through the chart rather than the root box: (i) the Greek reflexes κυλίνδειν and κῶλον are attached to this root only 'quite doubtfully' (Watkins) or 'probably' (Klein), and Beekes prefers Pre-Greek for κῶλον; (ii) the box for Greek 'kôlon' silently merges the unrelated homonym κόλον 'large intestine', which is what carries the Arabic/Persian قولون branch. One printing error: the Greek node #4 'skhelos' should read skellos (σκελλός).\",\n \"note_fa\":\"ریشه اصیل است و برچسبِ زبانی و معنای آن درست. پوکورنی (فرهنگ ریشه‌شناختی هندواروپایی، ص ۹۲۸) سرواژهٔ «(s)kel-4 (با گسترشِ klā-, klō-)» را با معنای «خم شدن؛ کج» می‌آورد و خانوادهٔ یونانیِ σκέλος، σκελλός، σκολιός، σκώληξ، κελλόν، κυλλός، κυλίνδω و κῶλον را زیر آن می‌نشاند؛ والده-پوکورنی (ج۲ صص ۵۹۷–۵۹۸) همان مقاله است (خودِ پوکورنی به «WP. II 597 ff.» ارجاع می‌دهد) و واتکینز در پیوستِ AHD می‌نویسد: «skel-3، همچنین kel-. کج. با مشتقاتی که به اندامِ خمیدهٔ تن — ساق، پاشنه، زانو، ران — اشاره دارند». شمارهٔ «Skel 1» از خودِ نورایی است (نزد پوکورنی چهارمین (s)kel- است) و ارجاعِ «Skel 2 ← Sek» هم‌آواییِ «بریدن» را جدا می‌کند. دو سستی در بدنهٔ چارت هست نه در جعبهٔ ریشه: نخست آنکه κυλίνδειν و κῶλον تنها «با تردیدِ بسیار» (واتکینز) یا «احتمالاً» (کلاین) به این ریشه بسته شده‌اند و بیکس برای κῶλον خاستگاهِ پیشایونانی را ترجیح می‌دهد؛ دوم آنکه جعبهٔ «kôlon» هم‌آوایِ بی‌ربطِ κόλον «رودهٔ بزرگ» را در خود ادغام کرده و همین معنا است که شاخهٔ «قولون» عربی و فارسی را حمل می‌کند. یک خطای چاپی نیز هست: در گرهٔ ۴ باید skellos (σκελλός) خوانده شود نه skhelos.\",\n \"sources\":[W_KOLON_L,E_COLON],\n \"ref_check\":[{\"ref\":\"POK:928\",\"status\":\"supports\",\"note\":\"IEW 928 is exactly the root: \\\"Root / lemma: (s)kel-4 (extended kla-, klo-) / Meaning: to bend; crooked\\\", ending \\\"References: WP. II 597 ff., WH. I 144 f., 248, II 492, Trautmann 114, 135 f., 145. Page(s): 928\\\" (POK_full.txt lines 75386-75440).\"}],\n \"consulted\":[POK928,WLD597,AHDSKEL,\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.v. cylinder\",\"stance\":\"supports\",\"note\":\"\\\"I.-E. base *(s)qel 'to bend, twist', whence also Gk. kullos ... 'crooked, crippled', kolon, 'limb, member'.\\\"\"},\n  {\"src\":\"IEC\",\"where\":\"Mann, IEC, lemmata 'skelos'/'skhelos' (IEC.txt lines 15560, 16052)\",\"stance\":\"partial\",\"note\":\"Mann's cross-reference \\\"skelos, see skhelos and cf. skel- (3)\\\" routes the Greek leg-word to a lemma he glosses 'wrong, fraud' — his arrangement of the (s)kel- homonyms differs from Pokorny's and does not support the chart's gloss.\"}],\n \"nodes\":e0_nodes}\n\n# ---------------- entry 3: Skeng ----------------\nPOK930 = {\"src\":\"POK\",\"where\":\"IEW 930, lemma '(s)keng-' (POK_full.txt line 75493ff)\",\"stance\":\"supports\",\"note\":\"\\\"Root / lemma: (s)keng- / Meaning: lame; slant. Material: Old Indic sakthi- n. (= Avestan haxti-) 'thigh' (*skak-thi-, Indo Germanic *skng-ti-; the -th- after Old Indic asthi- 'bone', above S. 783); khanjati 'hinkt' ... gr. skazo 'limp' ... Old Icelandic skakkr 'hinkend, slant', Swedish dial. skinka 'limp'; without anl. s-: Old High German hinkan 'limp' ... Germanic *skanka- in Norwegian skonk, skanki 'thigh, shinbone', Old English scanca f. 'shank, leg, shin bone'. References: WP. II 564 f. Page(s): 930\\\"\"}\nAHDSKENG = {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. skeng- (AHD_watkins1985.txt line 935, end)\",\"stance\":\"supports\",\"note\":\"\\\"skeng-. Crooked. Germanic *skankon-, 'that which bends,' leg, in Old English sc(e)anca, shinbone: SHANK. [Pok. (s)keng- 930.]\\\" — Watkins's entry is confined to the Germanic branch; he lists no Indo-Iranian reflex.\"}\nWLD564 = {\"src\":\"WLD\",\"where\":\"Walde-Pokorny II 564 (WLD_Bd2_pages.txt leaf 569)\",\"stance\":\"partial\",\"note\":\"\\\"sqeng- 'hinken; schief, schraeg'. Ai. khanjati 'hinkt', khanjalih 'hinkend', khanjanah 'Bachstelze'; gr. skazo (nur Praes. und Impf.) 'hinke' (*sqng-io); aisl. skakkr 'hinkend, schief', schwed. mdartl. skinka 'hinken'; ohne anl. s- aisl. hinka, ahd. hinkan ... norw. skonk, skank f. 'Schenkel, Schienbein', ags. scanca f. 'Unterschenkel', mnd. schenke, mhd. nhd. schenkel, ahd. scincho.\\\" The root and the Germanic material are there, but Walde-Pokorny does NOT list Av. haxti- or Skt. sakthi- under it — those were added only in Pokorny's 1959 revision.\"}\n\ne3_nodes = []\n\ne3_nodes.append({\n \"id\":1,\"lang\":\"Avestan\",\"words\":\"haxti\",\"verdict\":\"disputed\",\n \"derivation\":\"The Avestan word is real but its root is not this one on the modern view. Bartholomae, Altiranisches Wörterbuch col. 1745, gives \\\"j., g. haxt- n. 'der innere Teil des Oberschenkels'\\\" (the inner part of the thigh, Vd. 8.59, F. 3g), citing Skt. sakthi- and Ossetic aγd 'loin' — note that the stem is haxt-, and that Bartholomae's own footnote warns \\\"haxt- und ai. sakthi- decken sich nicht\\\" and suggests the Iranian -t- may be due to the influence of ast- 'bone' and srōni- 'hip'. Pokorny 930, the reference Nourai cites, does equate them and reconstructs *skn̥g-ti- ('Old Indic sakthi- n. (= Avestan haxti-) \\\"thigh\\\" (*skak-thi-, IE *skng-ti-)'), so Nourai reproduces his source faithfully. But that equation is now abandoned: Walde-Pokorny II 564 did not have it; Mann's Indo-European Comparative Dictionary puts the pair under a different lemma *soghtis 'thigh' (root segh-/sogh- 'hold'); Wiktionary's own (s)keng- page lists only khañjati, skázō, Germanic *skankô, Celtic *kengeti and Slavic *šęgati — no Iranian — while sakthi-/haxti- are placed under PIE *sokʷHt-i-s 'thigh'. The chart's gloss 'that which bends, leg, shank' is likewise not the Avestan sense: the word means 'thigh', and 'that which bends' is Watkins's gloss for the Germanic *skankōn- carried over.\",\n \"derivation_fa\":\"واژهٔ اوستایی اصیل است اما به باورِ امروزی به این ریشه نمی‌رسد. بارتولومه در فرهنگ ایرانی باستان (ستون ۱۷۴۵) می‌آورد: «haxt- (خنثی): بخشِ درونیِ ران» و آن را با sákthi- سنسکریت و aγd آسی «کپل» می‌سنجد؛ اما در پانوشتِ خود هشدار می‌دهد که «haxt- و sákthi- سنسکریت کاملاً بر هم منطبق نیستند» و احتمال می‌دهد که t در ایرانی وام‌دارِ تأثیرِ ast- «استخوان» و srōni- «ران» باشد. پوکورنی (ص ۹۳۰) — همان مرجعی که نورایی به آن ارجاع می‌دهد — این دو را برابر می‌گیرد و *skn̥g-ti- بازمی‌سازد؛ پس نورایی منبعش را درست نقل کرده است. ولی امروز این برابرنهاد کنار گذاشته شده: والده-پوکورنی (ج۲ ص۵۶۴) اصلاً این دو را زیر sqeng- نیاورده بود؛ مان در فرهنگ تطبیقیِ هندواروپایی آنها را زیر سرواژهٔ دیگری (*soghtis «ران»، از ریشهٔ segh- «گرفتن») می‌نشاند؛ و ویکی‌واژه در صفحهٔ *(s)keng- تنها khañjati، skázō، ژرمنیِ *skankô، سلتیِ *kengeti و اسلاویِ *šęgati را می‌آورد و هیچ صورتِ ایرانی ندارد، در حالی که sakthi-/haxti- را زیر ریشهٔ جداگانهٔ *sokʷHt-i-s «ران» می‌گذارد. معنای «آنچه خم می‌شود، ساق» نیز معنای اوستاییِ واژه نیست؛ معنای آن «ران» است و «آنچه خم می‌شود» ترجمهٔ واتکینز برای *skankōn- ژرمنی است که به اینجا منتقل شده. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n \"sources\":[W_SAKTHI,W_SKENG],\n \"ref_check\":[{\"ref\":\"POK:930\",\"status\":\"supports\",\"note\":\"IEW 930 opens (s)keng- with \\\"Old Indic sakthi- n. (= Avestan haxti-) 'thigh' (*skak-thi-, Indo Germanic *skng-ti-; das -th- after Old Indic asthi- 'bone')\\\" — Nourai's citation is accurate; it is Pokorny's equation that modern work rejects.\"}],\n \"consulted\":[POK930,\n  {\"src\":\"BRT\",\"where\":\"Bartholomae, AiW col. 1745 (BRT.txt lines 28916-28921)\",\"stance\":\"partial\",\"note\":\"\\\"j., g. haxt- n. 'der innere Teil des Oberschenkels': ... V.8.59; F.3g ... ai. vgl. sakthi 'Schenkel'; oss. agd 'Lende'. — Pu.: haxt ... mit der np. Glosse: sarangah i saran.\\\" Footnote: \\\"haxt- und ai. sakthi- decken sich nicht ... Urir. haxt- mag sein t dem Einfluss von ast- 'Knochen', sroni- 'Huefte' verdanken.\\\" Bartholomae has the word and the Indic comparison, with the stem haxt- and the sense 'thigh', but no *(s)keng- and an explicit caveat.\"},\n  WLD564,\n  {\"src\":\"IEC\",\"where\":\"Mann, IEC, lemma 'soghtis' (IEC.txt line 16631)\",\"stance\":\"contradicts\",\"note\":\"\\\"soghtis 'thigh'. Skt. sakthih f., sakthi n. id.; Av. haxtis f. 'joint'; LW in Oss. agd, id.; phonol. obscure in Arm. azdr, id.\\\" — Mann assigns the pair to *segh-/*sogh- 'hold', not to skeng-; his own skeng- lemma (line 15732) lists no Iranian form.\"},\n  AHDSKENG]})\n\ne3_nodes.append({\n \"id\":2,\"lang\":\"Pahlavi\",\"words\":\"haxt\",\"verdict\":\"confirmed\",\n \"derivation\":\"Middle Persian (Book Pahlavi) haxt 'thigh, haunch, hip' is the regular continuant of Avestan haxt-: Avestan haxt- > MP haxt with no change at all beyond the loss of the neuter inflection, the cluster -xt- being wholly stable in Middle Persian. MacKenzie's Concise Pahlavi Dictionary p.43 has \\\"haxt [h(ʾ)ht'] thigh, haunch, hip\\\"; Nyberg's Manual of Pahlavi II glossary gives \\\"haxt [hht'] thigh 5726. — Av. (1745) haxt-\\\", quoting the Zoroastrian text passage and citing Bartholomae's column 1745 — i.e. exactly this arrow. Tavoosi's glossary of Šāyast nē Šāyast, which is Nourai's reference SNS:2, has haxt on its p.2 (also the phrase haxt ī dašn 'the right thigh'). Horn p.279 no.104 adds the Vendidad references: \\\"haxt 'Schenkel' (vd. 8 (184), Zendbuchstaben; 9 (82) ff.), aw. haxti-, ai. sákthi-, sakthán 'Schenkel', oss. t. aγd 'Lende'\\\". The gloss 'thigh' is right.\",\n \"derivation_fa\":\"«haxt» فارسی میانه (پهلویِ کتابی) به معنی «ران، کپل، لگن» بازماندهٔ قاعده‌مندِ haxt- اوستایی است: صورتِ اوستایی بی‌هیچ دگرگونیِ آوایی — جز افتادنِ صرفِ خنثی — به فارسی میانه رسیده، زیرا خوشهٔ ـxt در فارسی میانه یکسره پایدار است. مکنزی در فرهنگ کوچک پهلوی (ص ۴۳) می‌آورد: «haxt [hʾht'] ران، کپل، لگن»؛ نیبرگ در واژه‌نامهٔ راهنمای پهلوی (ج۲) می‌نویسد: «haxt [hht'] ران ۵۷۲۶ — اوستایی (۱۷۴۵) haxt-» و مستقیماً به ستون ۱۷۴۵ بارتولومه ارجاع می‌دهد، یعنی درست همین پیکان. واژه‌نامهٔ شایست نه شایستِ طاووسی — همان مرجعِ SNS:2 نورایی — نیز haxt را در ص ۲ دارد (و نیز ترکیبِ haxt ī dašn «رانِ راست»). هرن در ص ۲۷۹ شمارهٔ ۱۰۴ شواهدِ وندیداد را می‌افزاید. معنای «ران» درست است و ادعای نورایی تأیید می‌شود.\",\n \"sources\":[],\n \"ref_check\":[{\"ref\":\"SNS:2\",\"status\":\"supports\",\"note\":\"Tavoosi, Vazhe-name-ye Shayast ne Shayast: the glossary's index (SNS_pages.txt lines 15110, 16157-16159) gives 'haxt- 2/11', 'haxt 2/10', 'haxt i dasn 2/12' — i.e. page 2, lines 10-12; the page text itself (lines 999-1008) shows 'haxt' and 'haxt i dasn'. The cited page is right.\"}],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, CPD p.43 s.v. haxt (PHD_mackenzie.txt line 2879)\",\"stance\":\"supports\",\"note\":\"\\\"haxt [h(ʾ)ht'] thigh, haunch, hip.\\\" (English-Pahlavi side: 'thigh haxt, rān'; 'haunch haxt'; 'hip haxt'.) Kept strictly apart from haxtan 'to lead, persuade'.\"},\n  {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt line 1967)\",\"stance\":\"supports\",\"note\":\"\\\"haxt [hht'] thigh 5726. — Av. (1745) haxt-.\\\" Nyberg derives MP haxt from Av. haxt- and cites Bartholomae col. 1745 — the very arrow drawn here.\"},\n  {\"src\":\"HRN\",\"where\":\"Horn p.279 no. 104 (Pahlavi section)\",\"stance\":\"supports\",\"note\":\"\\\"Dasselbe gilt fuer haxt 'Schenkel' (vd. 8 (184), Zendbuchstaben; 9 (82) ff.), aw. haxti-, ai. sakthi-, sakthan 'Schenkel', oss. t. agd 'Lende'.\\\"\"},\n  {\"src\":\"SNS\",\"where\":\"p.2 lines 10-12\",\"stance\":\"supports\",\"note\":\"see ref_check.\"}]})\n\ne3_nodes.append({\n \"id\":3,\"lang\":\"Persian\",\"words\":\"hax\",\"verdict\":\"disputed\",\n \"derivation\":\"Two things go wrong here. (1) The parent: hax is not a continuation of haxt 'thigh' but reflects a different Avestan word, haxa- 'sole of the foot'. Horn p.279 no.104 — the page Nourai cites — reads \\\"104. hax 'Fußsohle' (vd. 8 (219) (221), 9 (107) Gl.). aw. haxa- 'Fußsohle'. Da der Kommentator keine Glosse macht, so ist phlv. hax vielleicht noch verstanden worden\\\", and only THEN adds \\\"Dasselbe gilt für haxt 'Schenkel' ... aw. haxti-\\\" — i.e. Horn presents hax < haxa- and haxt < haxti- as two parallel survivals, not as a chain. Bartholomae col. 1745 confirms the separate Avestan lemma: \\\"j. haxa- n. 'Fusssohle': ... V.8.69; F.3g ... Pü.: hax, erl.: pāšnag ī pāy\\\". So the arrow haxt → hax is unsupported by Nourai's own reference. (2) The language label: Horn's no.104 stands in the Pahlavi section of the Grundriss, and hax is a Zand gloss word in Book Pahlavi, not New Persian; هخ is absent from Borhan-e Qate' (grep of BQT_v3-v5 returns only هخامنشی) and from Moʿin. Nourai's parenthesis '(obsolete)' half-acknowledges this, but the box is labelled Persian and given a Persian-script form. The word and its gloss 'foot sole' are real; the parentage and the language are wrong.\",\n \"derivation_fa\":\"دو نکته در اینجا نادرست است. نخست، پدرِ گره: «hax» دنبالهٔ haxt «ران» نیست، بلکه بازماندهٔ واژهٔ اوستاییِ دیگری است: haxa- «کفِ پا». هرن در همان صفحهٔ ۲۷۹ که نورایی به آن ارجاع می‌دهد می‌نویسد: «۱۰۴. hax «کفِ پا» (وندیداد ۸(۲۱۹)(۲۲۱)، ۹(۱۰۷) گلوسه). اوستایی haxa- «کفِ پا»» و تنها پس از آن می‌افزاید «همین دربارهٔ haxt «ران» نیز صادق است ... اوستایی haxti-» — یعنی هرن این دو را دو بازماندهٔ موازی می‌داند نه یک زنجیره. بارتولومه (ستون ۱۷۴۵) نیز سرواژهٔ جداگانهٔ «haxa- (خنثی): کفِ پا» را با گلوسهٔ پهلویِ hax و شرحِ pāšnag ī pāy ثبت کرده است. پس پیکانِ haxt ← hax را حتی مرجعِ خودِ نورایی تأیید نمی‌کند. دوم، برچسبِ زبانی: شمارهٔ ۱۰۴ هرن در بخشِ پهلویِ کتاب است و hax واژه‌ای است از گلوسه‌های زندِ پهلوی، نه فارسی نو؛ «هخ» نه در برهان قاطع هست (جست‌وجو در جلدهای ۳ تا ۵ تنها «هخامنشی» را می‌یابد) و نه در فرهنگ معین. قیدِ «(منسوخ)» نورایی نیمی از این را می‌پذیرد، اما جعبه همچنان «فارسی» برچسب خورده و صورتِ فارسیِ «هَخ» به آن داده شده است. خودِ واژه و معنای «کفِ پا» درست است؛ پدرِ گره و زبانِ آن نادرست است.\",\n \"sources\":[],\n \"ref_check\":[{\"ref\":\"HRN:279\",\"status\":\"partial\",\"note\":\"Horn, Grundriss p.279 no. 104 (HRN.txt leaf 300): \\\"104. hax 'Fusssohle' (vd. 8 (219) (221), 9 (107) Gl.). aw. haxa- 'Fusssohle'. Da der Kommentator keine Glosse macht, so ist phlv. hax vielleicht noch verstanden worden; doch steht das Wort an der letzterwaehnten Stelle in Awestabuchstaben. Dasselbe gilt fuer haxt 'Schenkel' (vd. 8 (184) ...), aw. haxti-, ai. sakthi-.\\\" The page has the word and the gloss Nourai gives, but derives it from Av. haxa-, and the entry is in Horn's PAHLAVI list, not his New Persian one.\"}],\n \"consulted\":[\n  {\"src\":\"HRN\",\"where\":\"p.279 no. 104\",\"stance\":\"partial\",\"note\":\"see ref_check — hax < Av. haxa-, parallel to (not descended from) haxt < Av. haxti-.\"},\n  {\"src\":\"BRT\",\"where\":\"Bartholomae, AiW col. 1744-45 s.v. haxa- (BRT.txt line 28905)\",\"stance\":\"contradicts\",\"note\":\"\\\"j. haxa- n. 'Fusssohle': aruxs ya nasus ... V.8.69; F.3g; — daitum (bez. hoyum) haxam V.8.70. Pu.: hax, erl.: pasnag i pay.\\\" A separate Avestan headword from haxt- (col. 1745), with its own Pahlavi gloss hax.\"},\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, CPD\",\"stance\":\"silent\",\"note\":\"grep of PHD.txt/PHD_mackenzie.txt finds haxt, haxtan, hixtan, hixr — but no simplex hax; the Zand gloss did not make MacKenzie's selection.\"},\n  {\"src\":\"BQT\",\"where\":\"BQT_v3/v4/v5_pages.txt\",\"stance\":\"silent\",\"note\":\"grep 'هَخ' / '^هخ' returns only هخامنشی (v4 line 16180). Borhan-e Qate' has no headword هخ, confirming the word is not New Persian.\"}]})\n\ne3_nodes.append({\n \"id\":4,\"lang\":\"Sanskrit\",\"words\":\"sâkthi\",\"verdict\":\"disputed\",\n \"derivation\":\"Sanskrit सक्थि sákthi- n. (also sakthán-) is a real and ancient word (Rigveda onwards), but its meaning is 'the thigh, thigh-bone' (and, transferred, 'the pole/shafts of a cart'), not the chart's 'leg, shank'; and its root is disputed exactly as at node #1. Pokorny 930 and hence Nourai derive it from *skn̥g-ti- beside Av. haxti-, explaining the -th- as analogy after asthi- 'bone'. Modern reconstruction abandons that: Wiktionary derives sákthi- from Proto-Indo-Iranian *sáktʰi and PIE *sokʷHt-i-s 'thigh' (with the aspiration from the laryngeal, not from asthi-), and puts no Indo-Iranian form under *(s)keng-; Mann had already filed the pair under *soghtis 'thigh'; Walde-Pokorny II 564 did not have them under sqeng- at all; and Bartholomae states outright that Av. haxt- and Skt. sakthi- 'decken sich nicht'. Note also that Nourai's second reference for this node, SNS:2, is Tavoosi's Šāyast nē Šāyast glossary — a Pahlavi word-list, which cannot be an authority for a Sanskrit form; what its p.2 supports is the Pahlavi haxt of node #2.\",\n \"derivation_fa\":\"واژهٔ سنسکریتِ sákthi- (و نیز sakthán-) اصیل و کهن است (از ریگ‌ودا به بعد)، اما معنای آن «ران، استخوانِ ران» (و به‌طورِ مجازی «مالبندِ گردونه») است نه «ساق» که چارت می‌گوید؛ و ریشهٔ آن دقیقاً به همان دلیلِ گرهٔ نخست محلِ اختلاف است. پوکورنی (ص ۹۳۰) و به پیروی از او نورایی آن را از *skn̥g-ti- در کنارِ haxti- اوستایی می‌گیرند و th را قیاس با asthi- «استخوان» می‌دانند. بازسازیِ امروزی این را کنار گذاشته است: ویکی‌واژه sákthi- را از هندوایرانیِ آغازینِ *sáktʰi و آن را از هندواروپاییِ *sokʷHt-i-s «ران» می‌گیرد (دمیدگی از حنجره‌ای است نه از قیاس با asthi-) و هیچ صورتِ هندوایرانی را زیر *(s)keng- نمی‌آورد؛ مان نیز پیش‌تر این جفت را زیر *soghtis «ران» گذاشته بود؛ والده-پوکورنی (ج۲ ص۵۶۴) اصلاً آنها را زیر sqeng- نداشت؛ و بارتولومه صریحاً می‌نویسد که haxt- اوستایی و sákthi- سنسکریت بر هم منطبق نمی‌شوند. نکتهٔ دیگر: مرجعِ دومِ این گره، یعنی SNS:2، واژه‌نامهٔ شایست نه شایستِ طاووسی است — فهرستی از واژگانِ پهلوی — که نمی‌تواند سندی برای صورتی سنسکریت باشد؛ آنچه ص ۲ آن تأیید می‌کند haxtِ پهلویِ گرهٔ ۲ است. پژوهش امروزی این ریشه‌یابی را رد می‌کند.\",\n \"sources\":[W_SAKTHI,W_SKENG],\n \"ref_check\":[\n  {\"ref\":\"POK:930\",\"status\":\"supports\",\"note\":\"IEW 930: \\\"Old Indic sakthi- n. (= Avestan haxti-) 'thigh' (*skak-thi-, Indo Germanic *skng-ti-; das -th- after Old Indic asthi- 'bone', above S. 783)\\\" — Pokorny does put sakthi- here, with the gloss 'thigh'.\"},\n  {\"ref\":\"SNS:2\",\"status\":\"not_found\",\"note\":\"SNS is Tavoosi's glossary of the Pahlavi Shayast ne Shayast; its p.2 has the Pahlavi haxt / haxt i dasn (index: 'haxt 2/10', 'haxt i dasn 2/12'), but there is no Sanskrit sakthi anywhere in SNS_pages.txt. The reference is misapplied to this node.\"}],\n \"consulted\":[POK930,\n  {\"src\":\"BRT\",\"where\":\"Bartholomae, AiW col. 1745 footnote\",\"stance\":\"partial\",\"note\":\"\\\"ai. vgl. sakthi 'Schenkel'\\\" in the entry, but the footnote adds \\\"haxt- und ai. sakthi- decken sich nicht; ... Urir. haxt- mag sein t dem Einfluss von ast- 'Knochen', sroni- 'Huefte' verdanken.\\\"\"},\n  {\"src\":\"IEC\",\"where\":\"Mann, IEC, lemma 'soghtis' (line 16631)\",\"stance\":\"contradicts\",\"note\":\"\\\"soghtis 'thigh'. Skt. sakthih f., sakthi n. id.; Av. haxtis f. 'joint'; LW in Oss. agd\\\" — a different root from Mann's own skeng- lemma.\"},\n  WLD564]})\n\ne3_nodes.append({\n \"id\":5,\"lang\":\"Germanic\",\"words\":\"skankô\",\"verdict\":\"confirmed\",\n \"derivation\":\"Proto-Germanic *skankô(n)- 'shank, leg, thigh' is the core of this root and the one reflex nobody disputes. Pokorny 930: \\\"Germanic *skanka- in Norwegian skonk, skanki 'thigh, shinbone', Old English scanca f. 'shank, leg, shin bone', Middle Low German schenke 'thigh' ... ablaut. Old High German scinko 'thigh', scinka 'Beinröhre'\\\"; Walde-Pokorny II 564 the same; Watkins prints \\\"Germanic *skankōn-, 'that which bends,' leg\\\" — which is precisely the chart's gloss, evidently taken straight from AHD. The nasal-infixed *skenk-/*skank- is the zero- and o-grade of *(s)keng- 'to limp, be askew', the motivation being the bent leg; the same root without s- gives OHG hinkan 'to limp'. Klein reaches the same base from the English side: shank \\\"fr. I.-E. base *sqeng-, 'slanting, oblique, to limp', whence also OI. khañjati, 'limps', Gk. skazein, 'to limp', ON. skakkr, 'lame, crooked'\\\".\",\n \"derivation_fa\":\"ژرمنیِ آغازینِ *skankô(n)- «ساق، پا، ران» هستهٔ این ریشه و تنها بازمانده‌ای است که کسی در آن تردید نکرده است. پوکورنی (ص ۹۳۰) می‌آورد: «ژرمنیِ *skanka- در نروژیِ skonk، skanki «ران، استخوانِ ساق»، انگلیسیِ کهنِ scanca «ساق، پا»، آلمانیِ میانهٔ سفلای schenke «ران» ... و با تناوبِ واکه آلمانیِ علیای کهنِ scinko «ران»». والده-پوکورنی (ج۲ ص۵۶۴) نیز همین را دارد، و واتکینز دقیقاً همان معنایی را می‌نویسد که در چارت آمده است: «ژرمنیِ *skankōn-، «آنچه خم می‌شود»، پا» — که پیداست یکراست از AHD گرفته شده. صورتِ نون‌افزودهٔ *skenk-/*skank- درجهٔ صفر و درجهٔ o ریشهٔ *(s)keng- «لنگیدن، کج بودن» است و انگیزهٔ نام‌گذاری همان پای خمیده است؛ همین ریشه بدونِ s- در آلمانیِ علیای کهن hinkan «لنگیدن» را داده است. کلاین نیز از سمتِ انگلیسی به همین پایه می‌رسد. ادعای نورایی درست است.\",\n \"sources\":[W_SHANK,E_SHANK],\n \"ref_check\":[\n  {\"ref\":\"POK:930\",\"status\":\"supports\",\"note\":\"IEW 930: \\\"Germanic *skanka- in Norwegian skonk, skanki f. 'thigh, shinbone', Old English scanca f. 'shank, leg, shin bone', Middle Low German schenke 'thigh' (Demin. MHG NHG Schenkel 'thigh'), ablaut. Old High German scinko 'thigh', scincho m., scinca f. 'Beinroehre, thigh', NHG Schinken.\\\"\"},\n  {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. skeng-: \\\"Germanic *skankon-, 'that which bends,' leg, in Old English sc(e)anca, shinbone: SHANK.\\\" The chart's gloss 'that which bends, leg' is verbatim Watkins.\"}],\n \"consulted\":[POK930,AHDSKENG,WLD564,\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.v. shank (KLN_1971.txt line 219866)\",\"stance\":\"supports\",\"note\":\"\\\"OE. scanca, sceanca, 'leg', rel. to MLG. schenke, ... MHG., G. schenkel, 'shank, leg', and to Du. schonk, 'a bone', G. Schinken, 'ham'; fr. I.-E. base *sqeng-, 'slanting, oblique, to limp'.\\\"\"}]})\n\ne3_nodes.append({\n \"id\":6,\"lang\":\"English\",\"words\":\"shank\",\"verdict\":\"confirmed\",\n \"derivation\":\"English shank is inherited, not borrowed: Old English sc(e)anca 'leg, shin, shank (the part between knee and ankle)' > Middle English schanke, shanke > shank, with the regular Old English palatalisation of sc- to /ʃ/ before a front vowel and the loss of the weak final -a. Old English sceanca continues Proto-West Germanic *skankō < Proto-Germanic *skankô, and so goes back to *(s)keng- 'to limp, be askew'; the cognates are Dutch schenkel, German Schenkel, Danish/Swedish skank, West Frisian skonk. Watkins and Klein both give exactly this line, and Etymonline adds the semantic note that the Germanic noun literally means 'that which bends'. Worth recording as a historical curiosity: Skeat's Concise Dictionary (1911 ed.) still derived shank from A.S. sceacan 'to shake' — \\\"named from its motion in running; lit. 'shaker'\\\" — a folk-etymological explanation that no modern authority keeps.\",\n \"derivation_fa\":\"واژهٔ انگلیسیِ shank موروثی است نه وام‌واژه: انگلیسیِ کهنِ sc(e)anca «ساق، پا، بخشِ میانِ زانو و قوزک» ← انگلیسیِ میانهٔ schanke/shanke ← shank، با کام‌شدگیِ قاعده‌مندِ sc- به /ʃ/ پیش از واکهٔ پیشین و افتادنِ ـa پایانی. صورتِ انگلیسیِ کهن بازماندهٔ ژرمنیِ باختریِ آغازینِ *skankō و ژرمنیِ آغازینِ *skankô است و از این راه به ریشهٔ *(s)keng- «لنگیدن، کج بودن» می‌رسد؛ هم‌ریشه‌های آن schenkel هلندی، Schenkel آلمانی، skank دانمارکی و سوئدی و skonk فریزیِ باختری‌اند. واتکینز و کلاین همین زنجیره را می‌آورند و اتیمانلاین می‌افزاید که معنای تحت‌اللفظیِ نامِ ژرمنی «آنچه خم می‌شود» است. یک نکتهٔ تاریخی شایانِ ثبت: اسکیت در ویراستِ ۱۹۱۱ فرهنگ فشردهٔ خود هنوز shank را از sceacan «لرزیدن، تکان دادن» می‌گرفت («از حرکتش هنگام دویدن نام گرفته؛ به‌معنی تحت‌اللفظی: لرزاننده») — ریشه‌شناسیِ عامیانه‌ای که هیچ مرجعِ امروزی آن را نگه نداشته است. ادعای نورایی درست است.\",\n \"sources\":[W_SHANK,E_SHANK],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. skeng-: \\\"... in Old English sc(e)anca, shinbone: SHANK\\\"; AHD index line \\\"SHANK skeng-\\\".\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein 1971 s.v. shank (line 219866)\",\"stance\":\"supports\",\"note\":\"\\\"shank, n. — ME. schanke, shanke, fr. OE. scanca, sceanca, 'leg' ... fr. I.-E. base *sqeng-, 'slanting, oblique, to limp'.\\\"\"},\n  AHDSKENG,\n  {\"src\":\"SKT\",\"where\":\"Skeat, Concise Etym. Dict. s.v. shank (SKT.txt line 17005)\",\"stance\":\"contradicts\",\"note\":\"\\\"shank, lower part of the leg. (E.) A.S. sceanca, scanca, bone of the leg; named from its motion in running; lit. 'shaker'. — A.S. sceacan, to shake, also to run. + Du. schonk, Dan. skank, Swed. skank, Low G. schunke, leg.\\\" Skeat's derivation from 'shake' is superseded; his cognate list is the same as everyone else's.\"}]})\n\nentry3 = {\n \"entry\":3,\"root\":\"Skeng\",\"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *(s)keng- 'to limp, hobble; to tilt, be askew' (Pokorny 930; Watkins/AHD 'skeng-. Crooked')\",\n \"note\":\"The root box is right. Pokorny IEW 930 has \\\"Root / lemma: (s)keng- / Meaning: lame; slant\\\"; Walde-Pokorny II 564 the same as 'sqeng- hinken; schief, schräg'; Watkins prints \\\"skeng-. Crooked. Germanic *skankōn-, 'that which bends,' leg ... [Pok. (s)keng- 930.]\\\"; Wiktionary reconstructs *(s)keng- 'to limp, hobble; to tilt, be askew'. The language label 'Indo-European' and the gloss 'crooked, bent' are both acceptable, though 'to limp' is the primary verbal sense. Where the chart goes wrong is the Indo-Iranian half of it: Nourai follows Pokorny 930 in equating Skt. sakthi- / Av. haxti- 'thigh' with this root, but Walde-Pokorny never had them here, Bartholomae warned that the two forms 'decken sich nicht', Mann files them under *soghtis, and current reconstruction gives them a root of their own, *sokʷHt-i-s 'thigh' — so nodes 1 and 4 are disputed and node 3 (Persian hax) rests on a further mis-parenting. The Germanic branch (nodes 5-6) is solid.\",\n \"note_fa\":\"جعبهٔ ریشه درست است. پوکورنی (ص ۹۳۰) سرواژهٔ «(s)keng-» را با معنای «لنگ؛ کج» می‌آورد؛ والده-پوکورنی (ج۲ ص۵۶۴) همان را با عنوانِ «sqeng- لنگیدن؛ کج، اریب»؛ واتکینز می‌نویسد «skeng-. کج. ژرمنیِ *skankōn- «آنچه خم می‌شود»، پا»؛ و ویکی‌واژه آن را «لنگیدن؛ کج شدن» بازمی‌سازد. پس برچسبِ «هندواروپایی» و معنای «کج، خمیده» هر دو پذیرفتنی‌اند، هرچند معنای اصلیِ فعلی «لنگیدن» است. آنچه در چارت نادرست است نیمهٔ هندوایرانیِ آن است: نورایی به پیروی از پوکورنی sákthi- سنسکریت و haxti- اوستایی («ران») را به این ریشه می‌بندد، حال آنکه والده-پوکورنی هرگز آنها را اینجا نیاورده بود، بارتولومه هشدار داده بود که این دو صورت بر هم منطبق نیستند، مان آنها را زیر *soghtis نشانده، و بازسازیِ امروزی ریشهٔ مستقلی برایشان قائل است: *sokʷHt-i-s «ران». بنابراین گره‌های ۱ و ۴ رد می‌شوند و گرهٔ ۳ («هخ» فارسی) افزون بر آن پدرِ نادرست هم دارد. شاخهٔ ژرمنی (گره‌های ۵ و ۶) استوار است.\",\n \"sources\":[W_SKENG,W_SAKTHI,E_SHANK],\n \"ref_check\":[{\"ref\":\"POK:930\",\"status\":\"supports\",\"note\":\"IEW 930: \\\"Root / lemma: (s)keng- / Meaning: lame; slant ... References: WP. II 564 f., F. Sommer Festschr. Debrunner 425 ff. Page(s): 930\\\" (POK_full.txt lines 75493-75527).\"}],\n \"consulted\":[POK930,WLD564,AHDSKENG,\n  {\"src\":\"IEC\",\"where\":\"Mann, IEC, lemma 'skeng- (skng-)' (IEC.txt lines 8160, 15732)\",\"stance\":\"partial\",\"note\":\"\\\"skeng- (skng-) 'bend, curve, hook; be bent, be crippled, hobble'. WP II 564. Skt. khanjami 'limp'; Sw. skinka; Gk. skazo 'limp'; Oss. kadz 'bent'; OFris. skunka 'shank, thigh'; Du. schonk 'bigbone'; ON skukka 'fold'.\\\" Mann has the root but, like WP, no Av. haxti- / Skt. sakthi- under it.\"}],\n \"nodes\":e3_nodes}\n\ndoc = {\"pdf_page\":453,\"book_page\":423,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-13\",\"entries\":[entry0,entry3]}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-453.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-453.py"
}
```


### [2026-09-14T02:16:57.796Z] TOOL RESULT

```
written
```


## [2026-09-14T02:17:01.937Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-453.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 453"
}
```


### [2026-09-14T02:17:03.120Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'plausible': 6, 'confirmed': 9, 'transcription_suspect': 1, 'disputed': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 18, 'partial': 7, 'not_checked': 3, 'not_found': 1}
books consulted: {'supports': 43, 'silent': 14, 'contradicts': 5, 'partial': 11} | by book: {'KLN': 11, 'POK': 9, 'AHD': 8, 'SKT': 7, 'WLD': 6, 'HRN': 4, 'BQT': 4, 'MON': 4, 'ARY': 3, 'IEC': 3, 'BRT': 3, 'TAD': 2, 'PHD': 2, 'DEV': 1, 'WEB': 1, 'AFM': 1, 'FVQ': 1, 'LAT': 1, 'NYB': 1, 'SNS': 1}
```


## [2026-09-14T02:17:23.804Z] AGENT

Verification of PDF page 453 (book page 423) is complete — `verify_check.py 453` reports 20/20 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed. Nodes: 9 confirmed, 6 plausible, 4 disputed, 1 transcription_suspect. Ref checks: 18 supports, 7 partial, 3 not_checked, 1 not_found.

**Flagged items**

- *transcription_suspect* — Skel 1, node 4, Greek "skhelos": no such Greek word; Walde‑Pokorny II 598 (the page Nourai cites as WLD:597) has σκελλός *skellos* 'bandy-legged' beside the Hesychian κελλόν. `error_in: book` — the printed page really reads "skhelos", so it is Nourai's misprint, not an extraction error.
- *disputed* — Skel 1, node 10, Greek "kôlon": the box merges two unrelated Greek words. κῶλον 'limb, member' (→ Latin colon → punctuation colon) is Watkins's item under skel‑3; κόλον 'large intestine' is a separate word of unknown origin (Wiktionary: "No relation to κῶλον"; Klein and Skeat keep two entries) — and it is that sense which carries the whole Arabic/Persian قولون branch below.
- *disputed* — Skeng, node 1 (Avestan haxti) and node 4 (Sanskrit sâkthi): Pokorny 930 does equate them under *(s)keng‑, so Nourai cites accurately, but Walde‑Pokorny never had them there, Bartholomae (col. 1745) warns "haxt- und ai. sakthi- decken sich nicht", Mann files them under *soghtis, and current reconstruction gives them their own root PIE *sokʷHt‑i‑s 'thigh'.
- *disputed* — Skeng, node 3, Persian "hax": wrong parent and wrong language. Horn p.279 no.104 (Nourai's own reference) derives hax 'foot sole' from Avestan **haxa‑**, a separate word from haxti‑, and the entry sits in Horn's **Pahlavi** list; هخ is absent from Borhan‑e Qate' and Mo'in.

**Notable positives** — Mo'in's footnote in Borhan‑e Qate' (printed 1547 = BQT_v3 pdf p.341) states the Greek origin of قولنج outright, even printing "colon = kōlon", against Borhan's own claim that it is معرّب of Persian کولنج; Horn no.789 (p.175) and Mo'in's footnote on شل (printed 1284, citing "هوبشمان ۷۸۹") back the whole šal/šelang/šalvār group.

**Citation page drift (not extraction errors)** — BQT:1288 → the four شل words are at printed 1284–1286 in the picofile scan; BQT:1548 → the قولنج footnote is at printed 1547; TAD:59 → the قولنج entry is on leaf 62, printed ≈57–59 (no scan registered for `ref_page.py`). SNS:2 is correct for Pahlavi *haxt* but is misapplied to the Sanskrit node (marked `not_found` there). ETM:45 and OEW:363 are not obtainable.

**No extraction errors found** — the JSON matches the printed page exactly, including the Persian scripts and the `script_extra` variants (شکپوی، شگپوی / قولنج، کولنج). Page image saved to `data/verification/sources/refs/ocr/BOOK/453.png`; 12 web sources archived via `fetch_source.py`.
