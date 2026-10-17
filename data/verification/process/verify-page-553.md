# Verification process log — verify-page-553


## [2026-10-17T00:00:15.704Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 553 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-553.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-553.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-553.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 553` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.802Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.450Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.526Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):
225	
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	In the shell, `ls` is aliased to `eza`, which can hang without a terminal and leave your
231	command stuck. List files with `command ls` or `find` instead.
232	
233	```json
234	{
235	  "pdf_page": 126,
236	  "book_page": 96,
237	  "verified_by": "claude-opus-5",
238	  "verified_on": "2026-09-05",
239	  "entries": [
240	    {
241	      "entry": 0,
242	      "root": "Dheigh, Dhigha",
243	      "verdict": "confirmed",
244	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
245	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
246	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
247	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
248	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
249	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
250	      "nodes": [
251	        {
252	          "id": 6,
253	          "lang": "Avestan",
254	          "words": "pairi-daeza",
255	          "verdict": "confirmed",
256	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
257	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
258	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
259	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
260	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
261	        }
262	      ]
263	    }
264	  ]
265	}
266	```
267	
268	Rules:
269	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
270	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
271	- `words` = the transliterations of the node joined by "; " (copy from the chart).
272	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
273	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
274	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
275	- If a node lists several words, cover each word; if they differ in verdict, use the worst
276	  verdict for the node and explain per word in `derivation`.
277	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
278	  scholarship takes.
279	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
280	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
281	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
282	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
283	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
284	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
285	  any extraction errors (JSON differs from the printed page) the owner must fix.
286	  Do not paste the JSON back into your reply.
287	
```


## [2026-10-17T00:00:18.956Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-553.txt"
}
```


### [2026-10-17T00:00:19.016Z] TOOL RESULT

```
1	=== PDF page 553 (book page 523) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wi : part, apart  (refs POK:1175,1176)  PART 1
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:1175; KNT:204 | wi, vî 2, vi 3 : apart, away, opposite
5	  #2 (parent #1) [Avestan] refs=HRN:205 | vî-čira, vîčâra : to judge ☞Kwer ; wi-čâr : to move, do ☞Kwer
6	    #3 (parent #2) [Pahlavi] refs=FFD:73 | vičir : judge ; wi-zârišn : to do, to translate
7	      #4 (parent #3) [Persian] refs=BQT:1809,2258; MON:4988 | vačar «وچر» : judgment ; vačargar «وچرگر» : judge ; gozârdan «گزاردن» : to translate | extra: گزارش ، گزیر ، ناگزیر
8	      #5 (parent #3) [Arabic] refs=KLN:1718 | vazîr
9	        #6 (parent #5) [Persian] refs=BQT:2279 | vazîr «وزیر» : minister
10	#7 (parent #0) [Avestan] refs=HRN:205 | vi-stâr : to spread out ☞Ster 1 ; vi-stâka : to stand against, rude ☞Stâ ; vi-saëd : to cut off ☞Sek ; vi-šâ, vi-sâ, vi-hây : to open ☞Sě 1
11	  #8 (parent #7) [Persian] refs=BQT:1800,1816,1818 | gostardan «گستردن (گسترش ، بستر)» ; gostâx «گستاخ» : "(one who) stands against" ; gosastan «گسستن (گسیختن ، گسیل)» : "cut apart" ; gošâdan «گشادن»
12	#9 (parent #0) [Avestan] refs=HUB:95 | vi-mad : to cure ☞Me ; vi-radh, vi-raiti : to set separate, edit ☞Ar ; vi-manah : think apart, guess ☞Men 1 ; vi-mar : to designate ☞Mer 1
13	  #10 (parent #9) [Persian] refs=BQT:437,834 | bîmâr «بیمار» ; vîrâstan «ویراستن (ویراستار)» : "to set apart", edit ; gomân «گمان» : "think apart", guess ; gomârdan «گماردن (گماشتن،گماشته)» : "to designate"
14	#11 (parent #0) [Avestan] refs=POK:1176; HRN:199,203 | vi-kâs : see apart ☞Kwek ; vi-raeč : run away ☞Leigh 2 ; vi-saiti : (two) separate tens ☞Dekm ; vi-tar : to go further, cross ☞Ter 1
15	  #12 (parent #11) [Persian] refs=BQT:1776,1778,1806 | govâh «گواه (گواهینامه)» ; gorixtan «گریختن (گریز)» : run away ; bîst «بیست» : two "separate" tens ; gozaštan «گذشتن (گذاشتن ، گذاردن)» | extra: گذشت ، گذر ، گذار ، گدار ، گذرنامه
16	#13 (parent #0) [Avestan] refs=NYB:217; FFD:75 | vi-čay, vi-kay : choose apart ☞Kwei 2 ; vi-žainti : to hit against, harm ☞Gwhen 2 ; vi-maik : mix different things ☞Meig
17	  #14 (parent #13) [Persian] refs=BQT:1813,1835; FFD:75 | gozîdan «گزیدن ۱ (گزینش،برگزیدن)» : "choose apart" ; gazîdan «گزیدن ۲ (گزند)» : "hit against" ; gomîxtan «گمیختن (گمیز)» : "mix different things"
18	
```


## [2026-10-17T00:00:19.412Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-553.json"
}
```


### [2026-10-17T00:00:19.602Z] TOOL RESULT

```
1	{
2	  "pdf_page": 553,
3	  "book_page": 523,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wi",
8	        "lang": "Indo-European",
9	        "refs": "POK:1175,1176",
10	        "gloss": "part, apart"
11	      },
12	      "part": 1,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Avestan / Old Persian",
18	          "refs": "POK:1175; KNT:204",
19	          "words": [
20	            {"translit": "wi, vî 2, vi 3", "gloss": "apart, away, opposite", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Avestan",
29	          "refs": "HRN:205",
30	          "words": [
31	            {"translit": "vî-čira, vîčâra", "gloss": "to judge", "script": null, "see": ["Kwer"]},
32	            {"translit": "wi-čâr", "gloss": "to move, do", "script": null, "see": ["Kwer"]}
33	          ],
34	          "note": null,
35	          "quote": null
36	        },
37	        {
38	          "id": 3,
39	          "parent": 2,
40	          "lang": "Pahlavi",
41	          "refs": "FFD:73",
42	          "words": [
43	            {"translit": "vičir", "gloss": "judge", "script": null},
44	            {"translit": "wi-zârišn", "gloss": "to do, to translate", "script": null}
45	          ],
46	          "note": null,
47	          "quote": null
48	        },
49	        {
50	          "id": 4,
51	          "parent": 3,
52	          "lang": "Persian",
53	          "refs": "BQT:1809,2258; MON:4988",
54	          "words": [
55	            {"translit": "vačar", "gloss": "judgment", "script": "وچر"},
56	            {"translit": "vačargar", "gloss": "judge", "script": "وچرگر"},
57	            {"translit": "gozârdan", "gloss": "to translate", "script": "گزاردن"}
58	          ],
59	          "script_extra": "گزارش ، گزیر ، ناگزیر",
60	          "note": null,
61	          "quote": {"text": "بوسه و نظرت حلال باشد ، باری - حجت دارم بر این سخن ز وچرگر", "poet": "Labîbî"}
62	        },
63	        {
64	          "id": 5,
65	          "parent": 3,
66	          "lang": "Arabic",
67	          "refs": "KLN:1718",
68	          "words": [
69	            {"translit": "vazîr", "gloss": null, "script": null}
70	          ],
71	          "note": null,
72	          "quote": null
73	        },
74	        {
75	          "id": 6,
76	          "parent": 5,
77	          "lang": "Persian",
78	          "refs": "BQT:2279",
79	          "words": [
80	            {"translit": "vazîr", "gloss": "minister", "script": "وزیر"}
81	          ],
82	          "note": null,
83	          "quote": null
84	        },
85	        {
86	          "id": 7,
87	          "parent": 0,
88	          "lang": "Avestan",
89	          "refs": "HRN:205",
90	          "words": [
91	            {"translit": "vi-stâr", "gloss": "to spread out", "script": null, "see": ["Ster 1"]},
92	            {"translit": "vi-stâka", "gloss": "to stand against, rude", "script": null, "see": ["Stâ"]},
93	            {"translit": "vi-saëd", "gloss": "to cut off", "script": null, "see": ["Sek"]},
94	            {"translit": "vi-šâ, vi-sâ, vi-hây", "gloss": "to open", "script": null, "see": ["Sě 1"]}
95	          ],
96	          "note": null,
97	          "quote": null
98	        },
99	        {
100	          "id": 8,
101	          "parent": 7,
102	          "lang": "Persian",
103	          "refs": "BQT:1800,1816,1818",
104	          "words": [
105	            {"translit": "gostardan", "gloss": null, "script": "گستردن (گسترش ، بستر)"},
106	            {"translit": "gostâx", "gloss": "\"(one who) stands against\"", "script": "گستاخ"},
107	            {"translit": "gosastan", "gloss": "\"cut apart\"", "script": "گسستن (گسیختن ، گسیل)"},
108	            {"translit": "gošâdan", "gloss": null, "script": "گشادن"}
109	          ],
110	          "note": null,
111	          "quote": null
112	        },
113	        {
114	          "id": 9,
115	          "parent": 0,
116	          "lang": "Avestan",
117	          "refs": "HUB:95",
118	          "words": [
119	            {"translit": "vi-mad", "gloss": "to cure", "script": null, "see": ["Me"]},
120	            {"translit": "vi-radh, vi-raiti", "gloss": "to set separate, edit", "script": null, "see": ["Ar"]},
121	            {"translit": "vi-manah", "gloss": "think apart, guess", "script": null, "see": ["Men 1"]},
122	            {"translit": "vi-mar", "gloss": "to designate", "script": null, "see": ["Mer 1"]}
123	          ],
124	          "note": null,
125	          "quote": null
126	        },
127	        {
128	          "id": 10,
129	          "parent": 9,
130	          "lang": "Persian",
131	          "refs": "BQT:437,834",
132	          "words": [
133	            {"translit": "bîmâr", "gloss": null, "script": "بیمار"},
134	            {"translit": "vîrâstan", "gloss": "\"to set apart\", edit", "script": "ویراستن (ویراستار)"},
135	            {"translit": "gomân", "gloss": "\"think apart\", guess", "script": "گمان"},
136	            {"translit": "gomârdan", "gloss": "\"to designate\"", "script": "گماردن (گماشتن،گماشته)"}
137	          ],
138	          "note": null,
139	          "quote": null
140	        },
141	        {
142	          "id": 11,
143	          "parent": 0,
144	          "lang": "Avestan",
145	          "refs": "POK:1176; HRN:199,203",
146	          "words": [
147	            {"translit": "vi-kâs", "gloss": "see apart", "script": null, "see": ["Kwek"]},
148	            {"translit": "vi-raeč", "gloss": "run away", "script": null, "see": ["Leigh 2"]},
149	            {"translit": "vi-saiti", "gloss": "(two) separate tens", "script": null, "see": ["Dekm"]},
150	            {"translit": "vi-tar", "gloss": "to go further, cross", "script": null, "see": ["Ter 1"]}
151	          ],
152	          "note": null,
153	          "quote": null
154	        },
155	        {
156	          "id": 12,
157	          "parent": 11,
158	          "lang": "Persian",
159	          "refs": "BQT:1776,1778,1806",
160	          "words": [
161	            {"translit": "govâh", "gloss": null, "script": "گواه (گواهینامه)"},
162	            {"translit": "gorixtan", "gloss": "run away", "script": "گریختن (گریز)"},
163	            {"translit": "bîst", "gloss": "two \"separate\" tens", "script": "بیست"},
164	            {"translit": "gozaštan", "gloss": null, "script": "گذشتن (گذاشتن ، گذاردن)"}
165	          ],
166	          "script_extra": "گذشت ، گذر ، گذار ، گدار ، گذرنامه",
167	          "note": null,
168	          "quote": null
169	        },
170	        {
171	          "id": 13,
172	          "parent": 0,
173	          "lang": "Avestan",
174	          "refs": "NYB:217; FFD:75",
175	          "words": [
176	            {"translit": "vi-čay, vi-kay", "gloss": "choose apart", "script": null, "see": ["Kwei 2"]},
177	            {"translit": "vi-žainti", "gloss": "to hit against, harm", "script": null, "see": ["Gwhen 2"]},
178	            {"translit": "vi-maik", "gloss": "mix different things", "script": null, "see": ["Meig"]}
179	          ],
180	          "note": null,
181	          "quote": null
182	        },
183	        {
184	          "id": 14,
185	          "parent": 13,
186	          "lang": "Persian",
187	          "refs": "BQT:1813,1835; FFD:75",
188	          "words": [
189	            {"translit": "gozîdan", "gloss": "\"choose apart\"", "script": "گزیدن ۱ (گزینش،برگزیدن)"},
190	            {"translit": "gazîdan", "gloss": "\"hit against\"", "script": "گزیدن ۲ (گزند)"},
191	            {"translit": "gomîxtan", "gloss": "\"mix different things\"", "script": "گمیختن (گمیز)"}
192	          ],
193	          "note": null,
194	          "quote": null
195	        }
196	      ]
197	    }
198	  ]
199	}
200	
```


## [2026-10-17T00:00:40.826Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','HRN','FFD','BQT','MON','KLN','HUB','NYB','PHD','BRT','WLD','AHD','CHEUNG','ARY']:\n  v=d.get(k);print(k, json.dumps(v,ensure_ascii=False)[:400] if v else None)\n\"; command ls data/verification/sources/refs/ | head -100; command ls data/verification/page-55*.json"
}
```


### [2026-10-17T00:00:41.259Z] TOOL RESULT

```
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
CHEUNG None
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
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
KNT_full.txt
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
SKT_dli_revised.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
data/verification/page-55.json
```


## [2026-10-17T00:00:46.572Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,200p tools/verify_check.py | grep -n -i -E \"PROBLEM|consult|matrix|lang|sources|archiv\" | head -60; command ls data/verification/page-5[0-9][0-9].json | tail -5; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['HRN','HUB','BQT','FFD','NYB','KNT','POK']:\n  v=d[k];print(k, v.get('page_offset'), v.get('lookup_hint','')[:600]);print()\n\""
}
```


### [2026-10-17T00:00:46.943Z] TOOL RESULT

```
22:    missing_pages, problems = [], []
46:            problems.append(f"page {pg}: invalid JSON ({ex})")
52:                problems.append(f"page {pg}: entry {i} ({e['root']['name']}) missing")
56:                problems.append(f"page {pg}: entry {i} root verdict {rv!r} invalid")
65:                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
69:                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
74:                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
79:                for c in vn.get("consulted") or []:
86:    print("books consulted:", dict(con_tally), "| by book:", dict(con_books.most_common(40)))
89:    for p in problems:
90:        print("PROBLEM:", p)
94:    return 1 if problems else 0
data/verification/page-534.json
data/verification/page-535.json
data/verification/page-536.json
data/verification/page-537.json
data/verification/page-538.json
HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

HUB leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh

FFD 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).

NYB Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

KNT leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.

POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
```


## [2026-10-17T00:00:49.912Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-538.json'))\nprint({k:v for k,v in d.items() if k!='entries'})\ne=d['entries'][0]; print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2500]); print(json.dumps(e['nodes'][-1],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-17T00:00:50.248Z] TOOL RESULT

```
{'pdf_page': 538, 'book_page': 508, 'verified_by': 'claude-opus-5.5', 'verified_on': '2026-10-16'}
{
 "entry": 0,
 "root": "Wekw, Weqw",
 "verdict": "confirmed",
 "modern_form": "PIE *wekʷ- 'to speak' (Pokorny 1135-1136 u̯ekᵘ-; LIV² 673f.; Watkins wekw-; o-grade root noun *wṓkʷs 'voice')",
 "note": "Root, label and gloss are correct: Pokorny 1135 u̯ekᵘ- 'sprechen' with Skt. vakti, vāc-, vacas-, Av. vac-, vacah-, vāxš, Gk. épos, ops, Lat. vōx, vocāre (WP I 245f.). Cheung 2007 (*u̯ač) and Wiktionary agree. The Latin/English branch and the Avestan vāč-/vacah-/uxδa- branches are textbook. The weaker parts of the chart are the Iranian compounds Nourai reconstructs or invents to reach particular New Persian words: 'paurvatâ-vac' (for pažvāk), 'hu-ni-vak' (for xonyā), Avestan 'vaxš-ô-bara' (only a reconstruction *vaxša-bara- behind MP waxšwar) and 'Old Persian wâk/wânk' (not attested). The derivation of xonyā (MP huniyāg) from *hu-ni-vāka- is opposed by the Middle Persian form, which has no -w- (see node 9). forūxtan 'sell' is linked to vac- by Justi/Horn/Mo'in, but Cheung puts it under *waxš- 'grow' (see node 4). The extraction matches the printed page (checked against site/pages/538.jpg).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *wekʷ- «سخن گفتن» با بالاگونهٔ o در نام‌واژهٔ *wṓkʷs «آواز، صدا» در پوکورنی (ص ۱۱۳۵-۱۱۳۶)، والده-پوکورنی (ج ۱، ص ۲۴۵)، واتکینز و چونگ آمده است. بازمانده‌های آن سنسکریت vāc- و vacas-، اوستایی vāč- (حالت فاعلی vāxš) و vacah- «سخن»، یونانی épos و لاتینی vōx و vocāre است. ریشه و زبان و معنایی که نورایی داده درست است. ولی چند ترکیب ایرانی در این نمودار ساختهٔ خود اوست و در متن‌ها نیامده، مانند paurvatâ-vac و hu-ni-vak و vaxš-ô-bara. پیوند «خنیا» با این ریشه هم با پژوهش امروزی سازگار نیست.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-"
 ],
 "ref_check": [
  {
   "ref": "POK:1135",
   "status": "supports",
   "note": "POK_full.txt l.90116ff. 'Root / lemma: ueḱ- (*hueḱᵘ-) / Meaning: to speak / Material: Old Indic vakti, vivakti says, talks, speaks ... Avestan vac- speak, uxta-. Old Indic vacas- = Avestan vacah (= gr. épos) discourse, word ... vāk = Avestan vāxš (= Latin vox) voice, discourse, word ... Latin vox, vocis voice, voco, -are call ... References: WP. I 245 f.' Page(s) 1135-1136."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 245-246 (WLD_Bd1_pages.txt l.22850ff., leaf 253)",
   "stance": "supports",
   "note": "'uekᵘ- „sprechen“. Ai. vákti, vivakti „sagt, redet, spricht“ ... av. vac- „sprechen“, uxta- ... ai. vacas- n. = av. vacah- (= gr. épos) „Rede, Wort“ ... ai. vāc-,
{
 "id": 16,
 "lang": "English",
 "words": "voice, vocabulary",
 "verdict": "confirmed",
 "derivation": "voice: Middle English vois, voice < Anglo-Norman/Old French voiz, vois (Mod. Fr. voix) < Latin vōcem, accusative of vōx. It came into English after the Norman Conquest (c. 1300). vocabulary (16th c.): a learned borrowing of Medieval Latin vocābulārium 'list of words', from Latin vocābulum 'appellation, name, word' = vocā(re) 'to call' + instrumental suffix -bulum.",
 "derivation_fa": "انگلیسی voice از انگلیسی میانه vois / voice آمده، و آن از فرانسوی کهن (و انگلو-نورمان) voiz / vois و سرانجام از لاتینی vōcem (حالت مفعولی vōx) است. این واژه پس از فتح نورمان به انگلیسی راه یافت. vocabulary در سدهٔ شانزدهم از لاتینی میانه vocābulārium «فهرست واژه‌ها» وام گرفته شده، و آن از vocābulum «نام، واژه» است که از vocāre «خواندن» و پسوند -bulum ساخته شده. ادعای نورایی درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/voice",
  "https://en.wiktionary.org/wiki/vocabulary",
  "https://en.wiktionary.org/wiki/vocabulum"
 ],
 "ref_check": [
  {
   "ref": "None",
   "status": "not_checked",
   "note": "Nourai gives no reference for this node."
  }
 ],
 "consulted": [
  {
   "src": "KLN",
   "where": "KLN_1971.txt l.263398, l.263481",
   "stance": "supports",
   "note": "'vocabulary, n. ... ML. vocabulārium, list of words, fr. L. vocābulum'; 'voice, n. — ME. vois, voice, fr. OF. voiz, vois (F. voix), fr. L. vōcem'."
  },
  {
   "src": "SKT",
   "where": "s.v. voice",
   "stance": "supports",
   "note": "SKT.txt l.21012 'voice. (F.-L.) M.E. vois. O.F. vois (F. voix). — L. uōcem, acc. of uōx, voice, sound'."
  },
  {
   "src": "AHD",
   "where": "Watkins s.v. wekw-",
   "stance": "supports",
   "note": "'Latin vox ...: VOCAL, VOICE, VOWEL; ... Latin vocare: VOCABLE, VOCATION'."
  }
 ]
}
```


## [2026-10-17T00:01:31.791Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FFD','BQT','MON','KLN','FVQ','CHEUNG','WLD']:\n  v=d.get(k) or {};print(k, v.get('local_file'), v.get('scans'), v.get('page_offset') if k in('KLN','FVQ','WLD') else '');print()\n\"; command ls data/verification/sources/refs/incoming/ data/verification/sources/refs/ocr/"
}
```


### [2026-10-17T00:01:32.168Z] TOOL RESULT

```
FFD ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] None 

BQT ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] [{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}] 

MON ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None 

KLN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt None KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>

FVQ ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt'] None printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)

CHEUNG None None 

WLD ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] None Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).

data/verification/sources/refs/incoming/:
ARY
BLY
BQT
FFD
IRN
MFL
MON
PLA
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf

data/verification/sources/refs/ocr/:
AFM
ARY
BLY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
SOD
TAD
```


## [2026-10-17T00:01:34.359Z] AGENT

Root first: Pokorny, WLD, AHD.


## [2026-10-17T00:01:36.163Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"lemma: (u|w)i-$|lemma: u̯i-|lemma: ui-\" POK_full.txt | head; n=$(grep -n -E \"lemma: (ui|u̯i)-\" POK_full.txt | head -1 | cut -d: -f1); [ -n \"$n\" ] && sed -n \"$((n-1)),$((n+40))p\" POK_full.txt"
}
```


### [2026-10-17T00:01:36.542Z] TOOL RESULT

```
Exit code 1
```


## [2026-10-17T00:01:39.988Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Page(s): 1175\" POK_full.txt | head; grep -n -i \"auseinander\\|asunder\" POK_full.txt | head -20"
}
```


### [2026-10-17T00:01:40.445Z] TOOL RESULT

```
92991:Page(s): 1175-1176 
5520:Church Slavic v-btor-t "second' s. £//-" asunder, apart '. 
22520:'hetze ab, ermijde', fatJsco, -o^'gehe auseinander; ermatte'; 
23949:With o'^/s- "twice' identical is o'^/s- "divided, asunder' in Gothic tm'sstandan'to divide' 
23969:"through' : Latin discindo " to tear asunder, cut apart, cleave, divide, rend, tear ' ("*split in 
38410:Ionian afjcpiapaTEw " dispute, argue, fight ' (" nach zwei Seiten auseinandergehend '), pnija 
66606:compare yO/'5i/a/e"springt auf, actually "auseinanderspringen'); 
75308:"auseinanderflieften'; Lithuanian s/r/a/io'^5 "zerstreuf, Latvian sk/a/d/s ^ e\r\ Herumtreiber, 
76820:hollow', vJkusra-, hankusra- "sich auseinander-, zusammenwolbend'; 
80127:Avestan spar{aiti) "tritt, stoftt', with /^5 "rushes, hastes', with i//"auseinandertreten, - 
80272:zum Auseinanderspannen'; 
81662:Auseinanderstochern the brennenden Scheite); 
84096:supo, -aAe "throw', dissipo, -a/'e"auseinanderwerfen, scatter', obsipo, -are 
89139:durchsehossen', /7/n//O(0'/7a"auseinanderstehend, voneinander apart, separated', vindhate 
92960:'afterbeiden (all) Seiten gewandt, auseinandergehend'. Old Indie i//5i/5-o'/y5/7/r'uberallhin 
92963:whole'; with the same meaning 'all' from 'after all Seiten auseinandergegangen,
```


## [2026-10-17T00:01:42.834Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92935,92995p POK_full.txt"
}
```


### [2026-10-17T00:01:43.412Z] TOOL RESULT

```
Note: {u7sk-l) 

See also: s. S. 1134 (ue/s-). 

Page(s):1177 

Root / lemma: uT-Rnrit-T{* hauT-RrQt-J) 
Meaning: twenty 

Note: actually Dual "two decades ' (to Indo Germanic oT-'two' and dRrpt- above S. 192) 
Material: Old Indie viifisatf-, Avestan vTsaiti, osset. insai, Armenian k'san, gr. eiKoai, Doric 
FiKQTi, hom. EsiKOGi for £(F)lKoai, alb. zet, Latin vTginti{see above S. 192), Old Irish fiche. 
Gen. fichet {*uiRmt-s, -os), acymr. i/ce//?/ (instead of *gwyca/ntirorr\ the compound *dou- 
viceint, cymr. deugaint^AQ" abstracted), corn, ugans, Tocharian A wiki, B ik9. 
References: WP. I 313, Wackernagel-Debrunner 3, 366 f., WH. II 788 f.. Frisk 453 f. 
Page(s):1177 

Root / lemma: u7-1 {*hauV) 
Meaning: separate from; both, two 
Note: (see uT-Rixit-fj 

Material: Old Indie k/- 'apart', Avestan i/7- 'apart; abseits, apart, separated from; entgegen; 
through and through ' (also vis-: v/s-pat-^go away, pass over'); Old Indie i//si/- 'after variant 
Seiten' in i//si//7a- 'verschiedenartig', iz/siz-zt/pa- 'verschiedengestaltig' , v/suva-n. 
'aequinoctium', visuvant- 'in the middle situated, after beiden Seiten gleich', visv-anc- 
'afterbeiden (all) Seiten gewandt, auseinandergehend'. Old Indie i//5i/5-o'/y5/7/r'uberallhin 
going', Avestan vispa&aMN. 'ringsum allenthalben' {*uisu- dw^, *uisuo-\ besides *uiso-\v\:) 
Lithuanian visas, Latvian viss. Old Prussian wissa-^aW; Old Church Slavic i/i.56 'all, 
whole'; with the same meaning 'all' from 'after all Seiten auseinandergegangen, 
umfanglich' and Indo Germanic A^-suffix: Old Indie visva- ' each, every, all', Avestan vfspa-. 



ap. vispa- "ds.'; Sg. also "whole' ( *uiRuo-\ out of it also Old pers. visa- with regular 
southwest - development from -si/-); 

to stem *uisu-, uisuo- presumably also gr. FiaFo(;, \qoc, " alike ' (for das on the other 
hand derivation from *uidsuos\.o *ueid- " behold ' erwogen wird); 

Latin v/t/umlau\t, error, disability, damage' as *i//-//-c»/r7"*Abweichung'; vitupero, -are 
"spoil, tadle' {vitium + parare); in addition Latin vitilTgoi. " skin rash '. 

comparative *uitero-. Old Indie i///a/'a- "further fijhrend', i///a/'5/77 "further, further', 
Avestan vTtaram^ sideways ', vTtara- "the weitere, spatere', d/^ra(\.e. vi&ra) Adv. " 
particularly, specially, especially, particular: in particular, peculiarly, separately, extra, 
notably, apart, separated', Gothic wiPraMv. and preposition m. Akk. "gegen, wider, 
compared with, vor'. Old Icelandic vidrMy. and preposition m. Dat. Akk. "gegen, wider, 
with, by' (also i//id' after Paaren as nordr: nord). Old English widMv. and preposition m. 
Gen. Dat. Akk. "gegen, compared with, wider, along, with', wider-\v\ compounds. Old High 
German widarMv. "gegen, back, against', preposition m. Dat. Akk. "gegen, compared 
with, wider'; Latin perhaps in i//?/7ici/s "Stiefvater', originally "the second ', or "the entferntere 
Vater' (but Old High German entrig, das an the einzigen Stelle, where es vorkommt (1 1 . 
Jh.), "transtiberinus' iJbersetzt, wird rather to e/70/7/" beyond' belong); Old Church Slavic 
vbtorb " alter, secundus ' (from *vbtorb). 

References: WP. I 312 f., WH. II 80, 808, Vasmer 1, 192 f., 237, Trautmann 362 f. 
Page(s): 1175-1176 

Root /lemma: u7-2, uoi- {* hau7-sl^ 

Meaning: expr. root
```


## [2026-10-17T00:01:49.742Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==321 || NR==322' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i -E \"auseinander|av\\. v|vīsaiti|zwanzig|u̯i|ui-\" | head -20; echo ---; grep -n -E \"^wi-|^wi-\\b|wi- \" AHD_watkins1985.txt | head; "
}
```


### [2026-10-17T00:01:50.098Z] TOOL RESULT

```
33:gellende", s. Kretschmer Gl. 4,350). Auf Grand eines *ui-to- „jubelnd“ hier-
66:Ui- „auseinander“.
67:   Ai. vi „auseinander‘’, av. vi- „auseinander; abseits, getrennt von; ent-
77:wandt, auseinandergehend u (aber verschieden ist av. vizv-anc- „nach ver-
79:ai. visva-driak „uberallhin gehend‘V'av. vispada Adv. „ringsum allenthalben“
85:m. Lit.);        mit derselben Bed. „all“’ aus „nach alien Seiten auseinander-
86:gegangen, umfanglich“ und idg. ^--Suffix ai. vigva- ,,jeder, all“, av. vispa-,
87:ap. vispa- „ds. sg. auch ganz“ ( *uikuo -; ap. auch visa- aus *ui-ko-, siehe
111: Schulze KZ. 40, 414 Anm. 1 als *ui-tio-m *Abweichung“ eine Bildung wie          ,
123:      Komparativ *uitero-         :   ai. vitaram       „weiter, ferner“, av. vitararn „seitwarts“,
148:durch idg. *ui-kmti „zwanzig", s. Sommer IF. 30, 403 f. (gegen Hirt IE. 1 7,
150:*ui- „auseinander“ nicht als „entzwei“ auf ein solches u- zu beziehen. Ai.
157:ul-kmti „zwanzig“.
158:      Ai. viiiigati-h, av. vlsaiti,           vtsqs,    arm. ksan                att.   el’xooi,   dor. boot, pfy.azi
163:Yerwandten von ai. vi „auseinander“ als „entzwei‘‘ (usw., s.                                                doch ist
---
147:LING (storo-), and, at least in some dialects, the SPARROW (sper-’), FINCH (sping-), and woodpecker ((s)peik-). The generic term for “bird” was awi- (Latin avis), and from this was derived the well-represented word for egg, *dOwyo-.
415:in: a. Old English twd, two (nominative feminine and neuter): Two; b. Old English fwégen, two (nominative and accusative masculine): TWAIN. 2. Germanic com- pound *twa-lif-, “two left (over from ten),” twelve (*-if-, left; see leik-), in Old English twelf, twelve, and twelfta, twelfth: TWELFTH, TWELVE. II. Adverbial form *dwis and combining form *dwi-. 1. Germanic *twi- in: a. Old English twi- (> Middle English twi-), two: TWIBIL, TWILIGHT; b. Old High German zwi- (> German zwie-), twice: ZWIEBACK, ZWITTERION. 2. Latin bis (combining form bi-), twice: BI-, BIS; BAROUCHE, BISCUIT. 3. Greek dis (combining form di-), twice: DI-!. 4. Germanic *twis in Middle English twisten, to twist: Twist. 5. Germanic *twiyes in Old English twige, twiga, twice: TWICE. 6. Ger- manic compound *twégentig, “twice ten” (*-tig, ten; see dekm), in Old English twéntig, twenty: TWENTY. 7. Ger- manic *twihna, double thread, twisted thread, in Old English twin, double thread: TWINE. 8. Germanic com- pounds “bi-twihna and *bi-twisk, “at the middle point of two” (*bi, at, by; see ambhi), in Old English betwéonum and betweohs, betwix, between: BETWEEN, BETWIXT, (TWIxT). 9. Germanic compound “twilic-, “two-threaded fabric” in Old English twilic, woven of double thread: TWILL. 10. Suffixed form *dwis-no- in: a. Germanic *twisnaz, double, in Old English twinn, getwinn, two by two, twin: TWIN; b. Latin bini, two by two, two each: BINAL, BINARY; COMBINE. 11. Suffixed form *dwi-ko- in Germanic *twig(g)a, a fork, in Old English twigge, a branch: Twic!. 12. Compound *dwi-plo-, twofold (*-plo-, -fold; see pel-3), in Greek diploos, diplous, twofold: DIPLO-, DIPLOE, DIPLOMA; ANADIPLOSIS. 13. Suffixed reduplicated form *dwi-du-mo- in Greek didumos, dou- ble, the testicles: (DIDYMIUM), DIDYMOUS; EPIDIDYMIS, TETRADYMITE. 14. Suffixed form *dwi-kha in Greek dikha, in two: DICHASIUM, DICHO-. III. Inflected form *duwo. 1. Latin duo, two: DEUCE}, DOZEN, DUAL, DUET, DUO-; DUODECIMAL, 2. Greek duo, dud, two: DUAD, DYAD; DODECAGON, HENDIADYS. IV. Variant form *du-. 1. Compound *du-plo-, twofold (*-plo-, -fold; see pel-%), in Latin duplus, double: DOUBLE, (DOUBLET), (DOU- BLOON), (DOUBLURE), DUPLE. 2. Compound *du-plek- (*-plek-, -fold; see plek-), twofold, in Latin duplex, double: DUPLEX, DUPLICATE, (DUPLICITY); CONDUPLI- CATE. 3. Suffixed form *du-bhw-io- in Latin dubius, doubtful (< “hesitating between two alternatives”), and dubitdre, to be in doubt: DOUBT, DUBIOUS; (REDOUBT- ABLE). [Pok. du6(u)- 228.]
597:b. suffixed Germanic form *hiwid6 in Old English higid, hid, a measure of land (< ‘household”): HIDE®. 2. Suf- fixed form *kei-wi- in Latin civis, citizen (< “member of a
655:kwo-. Also ki-. Stem of relative and interrogative pro- nouns. 1. Germanic *hwa-, hwi- in: a. personal pronouns *hwas, *hwasa, *hwam in Old English hwd, hwes, hwem, who, whose, whom: WHO, WHOSE, WHOM; b. pro- noun *hwat in Old English hwet, what: WHAT; c. adverb *hwi in Old English hwy, why: wHy; d. relative pronoun *hwa-lik- (*lik-, body, form; see lik-) in Old English hwilc, hwelc, which: WHICH; e. adverb *hwo6 in Old English hii, how: How!; f. adverb *hwan- in (i) Old English hwenne, hwanne, when: WHEN (ii) Old English hwanon, whence: WHENCE; g. adverb *hwithré in Old English hwider, whither: WHITHER; h. adverb *hwar- in Old English hwér, where: WHERE. 2. Germanic *hwatha- raz in: a. Old English hwether, hwether, which of two, whether: WHETHER; NEITHER; b. Germanic phrase *aiwo gihwatharaz, “ever each of two” (*aiwo, *aiwi, ever; see aiw-; *gi- from *ga-, collective prefix; see kom), in Old English €ghwether, &ther, either: EITHER. 3. Latin gui, who (genitive plural guérum): QUA, QUIB- BLE, QUORUM. 4. Latin quid, what, something: HIDALGO, QUIDDITY, QUIDNUNC, QuIP. 5. Latin quam, as, than, how, in quasi (quam + si, if; see swo-), as if: QUASI. 6. Latin quod, what: QUODLIBET. 7. Latin quot, how Many: QUOTE, QUOTIDIAN, QUOTIENT; ALIQUOT. 8. Latin quom, when: QUONDAM. 9. Latin quem, whom: CON- QUIAN. 10. Latin quantus, how great: QUANTITY. 11. Latin gudlis, of what kind: QuALITY. 12. Latin ut, that: (uT). 13. Latin uter, either of two: NEUTER. 14, Latin ubi, where, and ibi, there: ALIBI, UBIQUITY. 15. Persian chiz, thing: CHEESE, [Pok. k¥o- 644.] kwon-. Dog. 1. Greek kudn, dog: CYNIC; CYNOSURE, PROCYON, QUINSY. 2. Suffixed zero-grade form “kwn-to- in Germanic *hundaz in: a. Old English hund, dog: HOUND; b. Old High German Aunt (> German Hund), dog: DACHSHUND; c. Dutch hond, dog: KEESHOND. 3. Nominative form *kw6o in Welsh ci, dog: CORGI. 4. Variant *kan-i- in Latin canis, dog: CANAILLE, CA- NARY, CANICULA, CANINE, CHENILLE, KENNEL}, [Pok. Ruon- 632.]
736:Latin micturire, to want to urinate (desiderative of meiere, to urinate): MICTURATE. [Pok. meigh- 713.] meik-. To mix. 1. Variant form *meig- in Greek mig- nunai, to mix: AMPHIMIXIS, APOMIXIS, PANMICTIC, PAN- MIXIS. 2. Suffixed zero-grade form *mik-sk- in Latin miscére (past participle mixtus), to mix: MEDDLE, (MED- LEY), (MELANGE), MESTIZO, MISCELLANEOUS, MISCIBLE, MIX, MIXTURE; ADMIX, COMMIX, IMMIX, MISCEGENATION, (PELL-MELL), PROMISCUOUS. 3. Possibly a Germanic form *maisk- in Old English mdsc, macs, mdx, mashed malt: MASH. [Pok. meik- 714.] mei-no-. Opinion, intention. 1. Germanic *main- in Old English *mdn, opinion, complaint (> Middle English mone, complaint): MOAN; (BEMOAN). 2. Germanic *main- Jan in Old English ménan, to signify, tell, complain of, moan: MEAN}, [Pok. mei-no- 714.] mel-1, Soft; with derivatives referring to soft or softened materials of various kinds. I. Extended form *meld-. 1. Germanic *meltan in Old English meltan, to melt: MELT. 2. Possibly Germanic *miltja- in Old English milte, spleen, and Middle Dutch milte, milt: mit. 3. Possibly Germanic *malta- in Old English mealt, malt: MALT. 4. Suffixed variant form *mled-sno- in Greek blennos, slime, also a name for the blenny: BLENNY. 5. Suffixed zero-grade form *mid-wi- in Latin mollis, soft: MOIL, MOLLIFY, MOLLUSK, MOUILLE; EMOLLIENT; 6. Possibly nasalized variant form *mlad- in Latin blandus, smooth, caressing, flattering, soft-spoken: BLAND, BLANDISH. II. Variant form *smeld-. Germanic *smelt- in: a. Middle Dutch and Middle Low German smelten, to smelt: SMELT!; b. Old High German smalz, animal fat: SCHMALTZ; C. Italian smalto, melted glass: SMALT; d. Old French esmail, enamel: ENAMEL; e. perhaps Old English smelt, smylt, a marine fish, smelt: SMELT?. III. Extended form *meldh-. 1. Germanic *mildja- in Old English milde, mild MILD. 2. Possibly Greek maltha, a mixture of wax and pitch: MALTHA. IV. Suffixed form *mel-sko- in Ger- manic *mil-sk- in Old English melfi)sc, mylsc, mild, mellow (> Middle English melsche, friable): MULCH. V. Extended form *mfk- in Greek malakos, soft: CHON- DROMALACIA, MALACOLOGY, OSTEOMALACIA. VI. Possi- bly Celtic *molto-, sheep, in Old French moton, sheep: MUTTON. VII. Suffixed zero-grade form *()ml-u- in Greek amblus, blunt, dull, dim: AMBLYGONITE, AMBLY- opiA. [Pok. 1. mel- 716.] mel-2, Of a darkish color. 1. Greek melas, black: MEL- ANO-; MELANCHOLY, PSILOMELANE. 2. Greek mullos, a marine fish: MULLET; (SURMULLET). 3. Latin mulleus, reddish purple (used only to designate a ceremonial shoe worn by Roman magistrates): MULE. 4. Perhaps Ger- manic *mal- in Middle Dutch malen, to paint: MAUL- STICK. [Pok. 6. mel- 720.] mel-3. A limb. Greek melos, limb, hence a musical member or phrase, hence music, song, melody: MELISMA; ACRO- MELIC, MELODRAMA, MELODY. [Pok. 5. mel- 720.] mel-4. Strong, great. 1. Suffixed (comparative) form *mel-yos- in Latin melior, better: (AMELIORATE), MELIO- RATE, MELIORISM. 2. Suffixed zero-grade form *m/J-to- in Latin multus (neuter multum), much, many: MOLTO, MULTI-, MULTITUDE. [Pok. 4. mel- 720.] mel-5. Bad. Latin malus, bad, and male, ill (> malignus, harmful): MAL-, MALICE, MALIGN; DISMAL, MALADY, MALEDICT, MALEFACTOR, MALEVOLENT, MALVERSATION. [Pok. mélo- 724.] mel-€, Wool. Possibly suffixed zero-grade form *ml-no- in Greek mallos, wool. [Pok. 2. mel- 719.] mel-?. To miss, deceive. Germanic *mai- in Middle Dutch mal, foolish, silly: MALLEMUCK. [Pok. 2. mel- 719.] meldh-. To pray, speak words to a deity. Germanic *meld- in Old High German meldén, to proclaim, reveal: MELD}. [Pok. 1. meldh- 722.] mele-. Also mel-. To crush, grind; with derivatives referring to various ground or crumbling substances (such as flour) and to instruments for grinding or crush-
771:nau-', Death; to be exhausted. Contracted from *nasu-. 1. Suffixed zero-grade form *nau-ti- in Germanic *naudi- in Old English néod, néd, distress, necessity: NEED. 2. Suffixed form *ndw-i-, corpse, in Germanic *nawi- in Old Norse ndr, corpse: NARWHAL. 3. Slavic suffixed extended form *naud-d in: a. Polish nuda, boredom: NUDNIK; b. Russian nudnyi, tedious: NUDGE?. [Pok. 2. nédu- 756.]
812:os-. Ash tree. Germanic “aski- in Old English zsc, ash: ASH?2. [Pok. 6s- 782.] 6s-. Mouth. 1. Latin ds (stem 6r-), mouth, face, orifice, and derivative dstium (< suffixed form *6s-to-), door: ORAL, OS!, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. 2. Possibly Latin auriga, chari- oteer (< *6r-ig-, “he who manages the (horse’s) bit”; -ig-, driving, from *ag-; see ag-): AURIGA. [Pok. 1. 6us- 784.] ost-. Bone. 1. Latin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic *féd-, food, in Old English foda, food: Froop; b. Germanic denominative *fédjan, to give food to, in Old English fédan, to feed: FEED; Cc. suffixed form *pdt-tro- in Germanic *fdstra- in Old English fostor, food, nourishment: FOSTER. 4. Extended form *pds- in: a. suffixed form *pds-sko- in Latin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1. Lengthened-grade form *“pak- in Germanic *fogjan, to join, fit, in Old English fégan, to fit closely: FAY}. 2. Nasalized form *pa-n-g- in: a. Germanic *fangiz, seizure, in (i) Old English fang, feng, plunder, booty: FANG (ii) Dutch vangen, to catch: VANG; b. Latin pangere, to fasten: COMPACT!, IMPINGE. 3. Root form *pak- in: a. Latin pdx, peace (< “a binding together by treaty or agreement”): PACE?, PAY!, PEACE; APPEASE, PACIFIC, PACIFY; b. Latin pacisci, to agree: PACT. 4. Suf- fixed form *pak-sio- in: a. Latin pdlus, stake (fixed in the ground): PALE!, PALISADE, PEEL’, POLE?; IMPALE, TRA- VAIL, (TRAVEL); b. probably Latin pdla, spade: PALETTE, PEEL*. 5. Lengthened-grade form *pdg- in: a. Latin pdagus, “boundary staked out on the ground,” district, village, country: PAGAN, PEASANT; b. Latin pdgina, “trellis to which a row of vines is fixed,” hence (by metaphor) column of writing, page: PAGE?, PAGEANT; c. Latin prépdgés (pré-, before, in front; see per'), layer of vine, offspring (< “a fixing before”): PROPAGATE; d. Greek pégnunai, to fasten, coagulate: PECTIN, PEGMA- TITE. [Pok. pak- 787.] pan-. Fabric. 1. Germanic *fandn- in: a. Old English
832:pel-5. To sell. Lengthened o-grade form *pdl- in Greek p6lein, to sell: BIBLIOPOLE, MONOPOLY. [Pok. 5. pel- 804.] pel-6. To thrust, strike, drive. I. Suffixed form *pel-de-. 1. Germanic “*felt-, *falt-, to beat, in: a. Old English anfilt(e), anfealt, anvil (“something beaten on”): ANVIL; b. Germanic “*feltaz, *filtiz, compressed wool, in (i) Old English felt, felt: FELT! (ii) Medieval Latin filtrum, filter, piece of felt: FILTER. 2. Latin pellere (past participle pulsus), to push, drive, strike: POUSETTE, PULSATE, PULSE!, PUSH; COMPEL, DISPEL, EXPEL, IMPEL, PROPEL, REPEL. 3. Suffixed o-grade form *pol-o-, fuller of cloth, in Latin polire, to make smooth, polish (< “to full cloth”): POLISH. II. Extended form *peb-. 1. Present stem *pelna- in: a. Latin appelldre, “to drive to,” address, entreat, appeal, call (ad-, to; see ad-): APPEAL; b. Latin compellare, to accost, address (com-, intensive prefix; see kom): COMPELLATION; Cc. Latin interpellare, “to thrust between,” interrupt (inter-, between; see en): INTERPEL- LATE. 2. Suffixed zero-grade extended adverbial form *pla-ti, in pre-Greek *pldti in Greek plésios, near (< “pushed toward”): PLESIOSAURUS. [Pok. 2. a. pel- 801.] pel-7. Dish. Suffixed lengthened-grade form *pél-owi- in Latin pélvis, basin: PELVIS. [Pok. 4. pel- 804.] pele-1. 1. To fill; with derivatives referring to abundance and multitude. Variant “*p/é-, contracted from “pleo-. I. Suffixed zero-grade form “pls-no-. 1.Germanic *ful- naz, *fullaz, full, in Old English full, full: FULL’. 2. De- rivative Germanic verb *fulljan, to fill, in Old English fylian, to fill: FILL. 3. Latin root *pldno-, replaced by *pléno- (influenced by Latin verb plére, to fill; see III. 1. below) in Latin plénus, full: PLENARY, PLENITUDE, PLENTY, PLENUM; PLENIPOTENTIARY, REPLENISH, TERREPLEIN. II. Suffixed form *p(e)la-u-. 1. Possibly Latin paliis, marsh (? < “inundated”; but possibly rather from pel-?): PALUDAL, PALUDISM. 2. Obscure compara- tive form (Old Latin p/ous) in Latin plis, more: PIU, PLURAL, PLUS; NONPLUS, PLUPERFECT, SURPLUS. 3. O-grade form *pol()-u- in Greek polus, much, many: POLY-; HOI POLLOI. III. Variant form “p/é-. 1. Latin plére, to fill: (ACCOMPLISH), COMPLETE, COMPLIMENT, COMPLY, EXPLETIVE, IMPLEMENT, REPLETE, SUPPLY. 2. Possibly suffixed form *plé-dhw- in Latin p/lébs, plébés, the people, multitude: PLEBE, PLEBEIAN, PLEBS; PLEBISCITE. 3. Suffixed form *plé-dhwo- in: a. Greek pléthos (Ionic pléthus), great number: ISOPLETH; b. Greek derivative verb pléthein, to be full: PLETHORA; PLETHYSMOGRAPH. 4. Suffixed (comparative) form *plé-i(sjon- in Greek pledn, pleién, more: PLEO-, PLEO- NASM; PLEIOTAXY, PLEIOTROPISM, PLIOCENE. 5. Suffixed (superlative) form *p/é-isto- in Greek pleistos, most: PLEISTOCENE. IV. Possibly Sanskrit piirah, cake (< “that which fills or satisfies”): POORI. [Pok. 1. pel- 798.] pela-2, Flat; to spread. Variant *pld-, contracted from *plaa-. 1. Suffixed form *pel{a)-tu- in Germanic “felthuz, flat land, in Old English feld, open field: FIELD. 2. Suf- fixed form *pel{a)-t-es- (by-form of *pel)-tu-) in Ger- manic *feltha-, flat land, in: a. Old High German feild, field: FELDSPAR; b. Middle Dutch veld, velt, field: VELDT. 3. Variant form “pld- in: a. suffixed form
1135:Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
1167:wi-. Apart, in half. 1. Suffixed form *wi-itos in Germanic *widaz in Old English wid, wide (< “far apart”): WIDE. 2. Suffixed (comparative) form *wi-tero- in Germanic *withr6, against, in: a. Old English wither, against, with its derivative with, with, against: WITH, WITHERS; b. Old High German widar, against: GUERDON; WITHERSHINS. [Pok. 1. wi- 1175.]
```


## [2026-10-17T00:01:59.432Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==220' KNT.txt | grep -n -E \"^vi|vi-\" | head; echo ===HRN; for p in 199 203 205; do echo \"--- HRN p$p leaf $((p+21))\"; awk -v n=$((p+21+1)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | grep -E \"^ *[0-9]{3,4}\\. \" | head -30; done"
}
```


### [2026-10-17T00:01:59.984Z] TOOL RESULT

```
Exit code 1
(eval):1: ==HRN not found
```


## [2026-10-17T00:02:03.119Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^vi-|^vi- |^vi \" KNT.txt KNT_full.txt | head; echo \"=== HRN\"; for p in 199 203 205; do echo \"--- HRN p$p\"; awk -v n=$((p+21+1)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | grep -E \"^ *[0-9]{3,4}\\. \" | head -30; done"
}
```


### [2026-10-17T00:02:03.484Z] TOOL RESULT

```
KNT_full.txt:2858:vi-mardaliy, Skt. mrdáti. 
KNT_full.txt:12767:vi-, pref. w. verbs and nouns. 
KNT_full.txt:24895:vi- + kan- ‘dig apart, destroy’: viyakanam 1st 
KNT_full.txt:25820:vi- + jan- ‘shatter’: vijaná"tiy 3d pl. subj. ($208, 
KNT_full.txt:25961:vi- + tar- ‘go across’, caus. ‘put across’: viya- 
KNT_full.txt:26923:vi- + nab- caus. ‘injure, harm’: vindPayatiy 
KNT_full.txt:28292:vi- + mard- ‘destroy’: vimardatiy (830, $213) 
KNT_full.txt:28946:vi- prefix ‘away, apart’: Av. vi, Skt. vi; with 
KNT.txt:577:vi-mardaliy, Skt. mrdáti.
KNT.txt:2830:vi-, pref. w. verbs and nouns. hacà, prep. w. abl., loc., instr., adv. hadā, prep. w. instr.
=== HRN
--- HRN p199
889. ffäh *Ort (in Comp.) ; Thron*.
890. f/e^^Mörtel'.
891. (ßtidüften 'schmelzen', Praes. gudäz-em, gudäzclnlden
892. f/iidäre 'Brett (zum Dachdecken)' (unbelegt).
893. ffudästen hinüberführen, hinüberziehen', Praes. gu-
894. -ger '-tuend, -Macher', z. B. ähenger, dadger,
--- HRN p203
911. germ Varm*, gerniä 'Wärme', germJ, germis (AM. 54
912. girevtden glauben* jT^in; (Qiss. Dan., Merx' Archiv,
913. gire 'Hals , girebän 'Halsberge' (arab. LW. jirbän,
914. gureyten 'fliehen , Praes. gurBz-em,
--- HRN p205
919. gu^lr 'Hilfsmitter, guz^rden (Sahn. I, 61 Vers 519),
920. gustäx *kühn, frech', busta/ (nicht belegt), vergl.
921. gtisterden ausbreiten', guster, vergl. blster (No. 218).
922. guMMen 'zerbrechen, trennen', Praes. gmihem^ gml
923. gusäden offnen , sich öffnen ; Praes. gusay-em,
```


## [2026-10-17T00:02:06.226Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28946,28960p KNT_full.txt; echo ===; awk 'BEGIN{RS=\"\\f\"} NR==221||NR==225||NR==227||NR==228' HRN.txt | sed -n 1,400p | grep -v \"^\\s*$\" | head -220"
}
```


### [2026-10-17T00:02:06.585Z] TOOL RESULT

```
Exit code 1
vi- prefix ‘away, apart’: Av. vi, Skt. vi; with 
verbal roots kan-, jan-, iar-, nof-, mard-, and 
perhaps in sbb. Vidarna-, Vivdna-, Vistaspa-, and 
adj. Viyaxna-. 


við- sb. ‘house, royal house, royal clan, court’ 
(JNES 4232): Av. vis- ‘Herrenhaus’, Skt. vié- 
‘house, dwelling’, Gk. ofxos ‘house’, Lt. vicus 
‘village’ (§22, $87, $114, §142). Decl., §188.1V, 
V. иат asf. AsH 12f; DPe 24; DPh 10; DNa 
53; DSe 51; DSt 9°; DH 8; XPh 58; A'He 20. 
v'6am asf. DB 1.69, 71. véd-patiy isf. (Foy, KZ 
35.37-8, 37.556; Hz. Api 352-4) DB 2.16°; 3.26. 
vidiyd 18. CMb note: DPe; DPi; DNb 30; DSg 
(eval):1: == not found
```


## [2026-10-17T00:02:15.534Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *(9(0[0-9]|1[0-9]|2[0-9]))\\. \" HRN.txt | head -40"
}
```


### [2026-10-17T00:02:15.998Z] TOOL RESULT

```
7815:900. {lygird (Endung von Ortsnamen).
7826:901. {2)ffird rund; rings herum (begirdf , girde rundes
7831:902. (/ertl *Staub* (ursprünglich 'wirbelnd, sich drehend).
7834:903. ff er den 'Nacken, Hals', gerdene 'Gebirgspass'^).
7839:904. gerdün ^Firmament; Wagen.
7855:905. ffurde *Niere\
7861:906. ffuri^j gurze 'Keule', arab. LW. jurz,
7870:907. {\)gtir8 'Hunger, gursene, gursenegt; gtcsne, n22/}^
7878:908. {2)gur8 Xockenhaar (unbelegt).
7881:909. yiriften 'ergreifen*, Praes. glr-etn,
7887:910. gurg 'Wolf.
7894:911. germ Varm*, gerniä 'Wärme', germJ, germis (AM. 54
7903:912. girevtden glauben* jT^in; (Qiss. Dan., Merx' Archiv,
7908:913. gire 'Hals , girebän 'Halsberge' (arab. LW. jirbän,
7915:914. gureyten 'fliehen , Praes. gurBz-em,
7929:915. giristen, giristen *klagen, weinen', Impt. girl ^) girye,
7937:916. fße^endj guzend (AM. S. 38 Zeile 7) 'Schade Leid',
7941:917. gu^ärden 'auseinander setzen, darlegen, bezahlen ;
7948:918. guziden 'aussuchen, erwählen*, Praes. giizm-em, guzin
7963:919. gu^lr 'Hilfsmitter, guz^rden (Sahn. I, 61 Vers 519),
7968:920. gustäx *kühn, frech', busta/ (nicht belegt), vergl.
7973:921. gtisterden ausbreiten', guster, vergl. blster (No. 218).
7976:922. guMMen 'zerbrechen, trennen', Praes. gmihem^ gml
7993:923. gusäden offnen , sich öffnen ; Praes. gusay-em,
8012:924. fftisuften 'zerstreuen ; verwelken (Vis und RamTn,
8020:925. ffusn ^Männchen, männlich*.
8027:926. guften sprechen, Praes. göy-etn, guftar 'Rede', gep,
8033:927. fful *Kose*, arab. LW. jtdah 'Rosenwasser ^).
8045:928. guia, gelü (AM. 109 Zeile 1 v. u.) 'Kehle .
8051:929. ffuJüle 'Kugel', (/öle.
9993:909. girift * Verbrechen'.
```


## [2026-10-17T00:02:20.753Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7914,8012p HRN.txt; grep -n -E \"^ *(88[0-9]|89[0-9])\\. \" HRN.txt | head -25"
}
```


### [2026-10-17T00:02:21.127Z] TOOL RESULT

```
afy. griva, greva 'Hals; Halsband'.
914. gureyten 'fliehen , Praes. gurBz-em,
Kauk.-bergjüd. viri/de (!).
skr. vi + i/^reö' (s. No. 638), allerdings nur in der
Bedeutung leer machen , laxiren vorkommend ; doch
vergl. aw. ra^cayeMti (paiti) 'sie verlassen , ai. i^rec-
'räumen, preisgeben', oss. d. lejun , t. iTjin 'laufen,
fliehen' (167); phlv. v(i)rextan.
Eine ältere Bedeutung von np. gure/ten findet sich
wohl bei AM. 237 Zeile 6: 'Also ist das Bedürfniss
nach Wasser grösser als das nach anderen Dingen,
da weder ein Gesunder noch ein Kranker es ent-— 204 —
b ehren kann (ee ö biigrEzeö)\ Wenn man hier von
'fliehen* ausgehen wollte, so würde die Erklärung sehr
gezwungen sein.
915. giristen, giristen *klagen, weinen', Impt. girl ^) girye,
giryjden (Sahn. I, 107 Vers 837).
aw. [/^gar-, gerente 'anrufen*; phlv. grlstan 'weinen,
klagen (AV.), g(i)rt/TnUan (AV.) ; ai. [/^gar-, gpidti 'an-
rufen'.
kurd. girin weinen ; oss. d. yär, t. qär 'Geschrei,
Ton, Laut, Stimme* (88); bei. greag, n. girey 'lärmen,
schreien, heulen, weinen*, Impt. bigri (117)^).
916. fße^endj guzend (AM. S. 38 Zeile 7) 'Schade Leid',
bezendT 'Elend'.
aw. "^mjainti-, vergl. ai. vi -i- iXAa«-, vihanti- ; phlv.
agajand bezw. agazand (AV.).
917. gu^ärden 'auseinander setzen, darlegen, bezahlen ;
gtizäris, güzärisn (Wörterbücher)^), guzäre; vergl. vecer
(vejer) 'richterliche Entscheidung (unbelegt).
skr. vi + [/"car-, Caus. 'erwägen, in Betracht ziehen,
prüfen ; phlv. v(i)cartan (AV.), v(i)car(i)sn^)j v(i)cartar
'verständig (für aw. cazdönkvaM-, arm. LW. vcar 'Be-
zahlung*.
918. guziden 'aussuchen, erwählen*, Praes. giizm-em, guzin
'erwählt'.
aw. vi H- [/^öay- 'aussuchen* ; phlv. v{i)öUany v{i)cwet
(AV.), arm. LW. vöit 'rein, lauter*; skr. vi-^ i^cay-
'auslesen, aussuchen'.
bei. gicinag, n. gisainay auswählen, aussuchen* (104).
*) Im Reim bei Eth6, Morgenländische Forschungen, S. 59,
Zeile 5 v. u. (Dies Citat verdanke ich Herrn Prof. Nöldeke).
2) Hübsohmann, ZDMG. 44, 557.
3) Vu 11 er 8 8. V. menisn hat falsch gttSärisn; beide Stämme
sind nicht zu verwechseln, doch werden sie in den Wörterbüchern
immer zusammen geworfen.
*) Phlv. *v%närisn^ vltiärfan* ist wohl auch r{i)c" zu lesen (ein aw.
c ist eingedrungen, wie öfter); die Bezeichnung des i in der Praepo-
sition vi wäre sehr aufiPäUig.- 205 -
919. gu^lr 'Hilfsmitter, guz^rden (Sahn. I, 61 Vers 519),
ffuzer, guzerden; vergl. näguztr.
Etwa "^viöarija-, vergl. skr. vi -r- i^car- 'ausführen,
vollführen'.
Hat mit reztr (No. 1084) nichts zu tun.
920. gustäx *kühn, frech', busta/ (nicht belegt), vergl.
usta/ (ebenfalls unbelegt).
aw. *vistaka', vergl. stax^'a-, phlv. sta^mak (Darme-
steter. Et. ir. 62)0; P^lv. v{i)stax (Mgn.), arm. LW.
vstah unverzagt'.
921. gtisterden ausbreiten', guster, vergl. blster (No. 218).
ai. vi -f- [/'sfar- ausbreiten'; phlv. v{i)siarta)i aus-
breiten*.
922. guMMen 'zerbrechen, trennen', Praes. gmihem^ gml
kerden Verabschieden, entlassen' (Öähn. I, 74 Vers 236),
pin '^''Di: Verstössen (Jer. 3, 8), vergl. gusll (Vullers),
gtisilänlden (Öähn. I, 88 Vers 494).
phlv. v{i)sastan (Bund.), v{i)sastakih (PPGl.).
Darmesteter, Et. ir. I, 84 hat das Wort auf eine
\/^*Qard' zurückgeführt, die neben ai. gar^, gpidti *zer-
brechen' auf iranischem Boden existirt haben müsse.
Bartholomae (briefl. Mitteilung) denkt an eine Ver-
mischung der beiden synonymen Wurzeln sk^heid- (aw.
sa^d-, hisidyäf; ai. dhed-, chindtti; bei. sindag, n. sinday,
Hübschmann, ZDM6. 44, 559) und k\er- (ai. ^c/r-,
Cfnäti). Ifp. gusisten wäre ap. *visistanaig (aus *«^z-
sid'tanaiy), dagegen gtisilem ap. *visardann (aus sar-
mit dem d von sid-). Er verweist dazu auf die
Wochenschr. f. klass. Phil., 1892 Sp. 397.
Der Inf. guslxten ist ganz unklar.
923. gusäden offnen , sich öffnen ; Praes. gusay-em,
gusüden, gusäyis (Öähn. I, 169 Vers 734).
phlv. v{i)sätan oflfnen'.
Darmesteter, Et. ir. I, 59 Note 3 nimmt als
Grundbedeutung von np. gvsäden sich freuen , indem
') An *v%8taxf'(i' hatten schon Fr. Müller, Kuhn und Schleiclier's
Beiträge V, 139 und Spiegel, Kommentar T, 64 gedacht.— 206 —
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
3666:891. tek 'schnell, Lauf, tekiden, tekT,
7653:880. kes 'Religion .
7659:881. ktn 'Feindschaft, Hass, Zorn', Mne.
7700:886. ijästen Vendun, drehen' (8ähn. I, 368 Vers 8-1:9; 369
7715:887. (/am Schritt'.
7717:888. f/äv llind', gö, gög 'Kalb' {^gavaka-)'''), göban 'Hirte'.
7736:889. ffäh *Ort (in Comp.) ; Thron*.
7740:890. f/e^^Mörtel'.
7744:891. (ßtidüften 'schmelzen', Praes. gudäz-em, gudäzclnlden
7748:892. f/iidäre 'Brett (zum Dachdecken)' (unbelegt).
7752:893. ffudästen hinüberführen, hinüberziehen', Praes. gu-
7764:894. -ger '-tuend, -Macher', z. B. ähenger, dadger,
7774:895. ger, gerr (AM. 28 Zeile 4) ^Krätze.
7787:896. guräz *Eber .
7797:897. geräziden 'schreiten .
7800:898. girun 'schwer.
7806:899. gurd 'Held'.
```


## [2026-10-17T00:02:26.533Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7752,7764p HRN.txt; grep -n -E \"^ *[0-9]{2,4}\\. *(guvä|guwä|gumän|gumä|gumext|gumex|gumi|blmär|bimär|bist|blst|vez|viräs|veräs|gezid|gaz|guzar|guzas|gudas|bister|bistar)\" HRN.txt | head -30"
}
```


### [2026-10-17T00:02:27.011Z] TOOL RESULT

```
893. ffudästen hinüberführen, hinüberziehen', Praes. gu-
där-em; guöesten 'überschreiten, passiren', Praes. //m-
öer-em; guödr 'Furt -), gudäris, guderäniden.
g. veddrte; Käk V. heidornan, Q. baudernädin.
ap. vi + l^tar-, vigatarayäma 'wir überschritten' ; aw.
vUaretö.{tanU'; ^hlv, v(i)tärt an ^ v(i)tartan {A.Y.), v{i)tar(e)
'Furt*^); arm. LW. vtar; ai. vi + iX^ar-, vitirati 'er
durchläuft, durchzieht', vitärdyati 'er führt hinüber'.
kurd. buhürtin, behartin 'die Zeit hinbringen.
Vergl. oss. d. tarun, t. farjn, färin 'treiben, jagen,
entfernen' (245); bei. tarag, n. faray 'umwenden, um-
kehren' (381); vergl. wa/. türt 'Furt'.
894. -ger '-tuend, -Macher', z. B. ähenger, dadger,
2618:39. bimär 'krank^^ bimürJ.
8163:939. guvälfden, gevaltden (falsch k"*) wachsen* (unbelegt);
```


## [2026-10-17T00:02:30.301Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2618,2632p HRN.txt; grep -n -i -E \"gumän|gumärd|gumext|guväh|gugäy|gukäy|vist |vist'|virästen|vazir|vezir|bistar|bister\" HRN.txt | head -30"
}
```


### [2026-10-17T00:02:30.715Z] TOOL RESULT

```
39. bimär 'krank^^ bimürJ.
aw. v% ■-\;- v^war-) (vergl. vJ-merencalt^); phlv.
vimär, vlmärlh (Men.), virnärinltan (y. 30, 6 nach
Darmesteter's Correctur, Et. ir. II, 138).
Die Etymologie ist gewiss falsch, da altes vi- im
Neupersischen consequent zu gu- wird, und selbst bei
Annahme eines Ausnahmefalles (z. B. biüer^ No. 218)
das i völlig unerklärt bliebe. Dass das erste Glied
np. be- *ohne' sei, könnte man nach sar. LW. bhnar
(d. i. bemar) vermuten; doch erhält man bei dieser
Ableitung keinen guten Sinn. Bartholomae schlägt
mir die Etymologie upai (s. No. 247) + mära-y also
*am Tode' vor, aber dafür spricht nicht das phlv. v
(oder auch w),
30. bin *sehend', hin-em^ binä^ bmis,
2288:Da np. bister nicht *Kleid' bedeutet, so hat Fr.
7254:Mitteilung) stellt hierher np. kärdär 'Vezir .
8092:LW. kurd. afy. gumän 'Zweifel*; bei. gtarän (121).
9375:1084. ve^lr (arab. LW.) 'Vezir; Gelehrter ^), gezJr, gizlr*^),
9379:Im modernen Spaniscli ist der Vezir als alguacil, alvazil etc. zum
12461:guväh "938.
19259:gumän 932.
```


## [2026-10-17T00:02:38.076Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 9375,9392p HRN.txt; echo ====; grep -n -E \"^ *93[0-9]\\. \" HRN.txt; "
}
```


### [2026-10-17T00:02:38.555Z] TOOL RESULT

```
1084. ve^lr (arab. LW.) 'Vezir; Gelehrter ^), gezJr, gizlr*^),
talm. ns^T»!:.
*) So im indischen Persisch häufig, vergl. z, B. Maä»ir-i Mah-
wiidsähl Fol. 38 (Berliner Handschrift Ms. orient. Fol. 535).
Im modernen Spaniscli ist der Vezir als alguacil, alvazil etc. zum
'Häscher, Polizeidiener* (auch veraltet 'Scharfrichter' und im Schiffs-
wesen der Beamte, Mer auf einem Kriegsschiffe für alles sorgen muss,
was zum Wasserproviant gehört*, s. F. Boooh-Arkossy, Spanisch-
Deutsches Handwörterbuch^ s. v.J degradirt, vergl. Dozy -Engel-
mann, Glossaire des mots espagnols et portugais d6riv^s de Parabe*,
S. 129.
*) Nur in einem AbuM Ma*änl- Verse.- 243 -
aw. Vieira- 'Entscheider ; phlv. v(i)öfr 'Entscheidung ;
Entscheider, Richter ; arm. LW. vcir ^Entscheidung.
1085. veng, ving 'leer; arm'.
aw. vergl. wwa- *leer, mangelnd'^); ai. und- Voran
etwas fehlt, unzureichend'; arm. unain *leer' (H.
No. 236); got. van 'Mangel*; gr. bvvi^ ermangelnd'
(eval):1: === not found
```


## [2026-10-17T00:02:48.684Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -50"
}
```


### [2026-10-17T00:02:49.207Z] TOOL RESULT

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


## [2026-10-17T00:03:03.019Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in گزاردن گزارش ناگزیر وزیر گستردن بستر گستاخ گسستن گسیختن گسیل گشادن گشودن بیمار ویراستن گمان گماردن گماشتن گواه گریختن بیست گذشتن گذاشتن گزیدن گزند گمیز آمیختن; do python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/$w\" --note \"page 553, root Wi, Persian $w etymology\" ; done 2>&1 | tail -30"
}
```


### [2026-10-17T00:03:17.248Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2ff2f8733a6f51ec.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e3dc92c661860282.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3f7db2299b29dbb3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bc0cadc782b786a3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f61b2634086adfd6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/990522fab661dd7f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/34858ed7e90878e6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fc4f445d305ef8ab.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/88fb4170fcd85fa0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/61f4c4083fbdbd8d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f11d95d753a35820.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3d9b7359f760d8f8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9bdd698dbf218db3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2e6a0256f47ff365.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5caa849055e8d3da.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/61a4218f36cf53a5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ed902cb96c9844c2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5b194abd77be720f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6364ae8f34d0efd9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2f867610b64a81e2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/edb20513fd1b720e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b2c674dbf07adcf4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/076d440621d6879d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b79fd8f6af38b809.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/54ce5f1a21cf4d3b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5e92d127d61193b9.txt
```


## [2026-10-17T00:03:24.159Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for w in گزاردن گزارش ناگزیر وزیر گستردن بستر گستاخ گسستن گسیختن گسیل گشادن گشودن بیمار ویراستن گمان گماردن گماشتن گواه گریختن بیست گذشتن گذاشتن گزیدن گزند گمیز آمیختن; do u=\"https://en.wiktionary.org/wiki/$w\"; f=$(grep -F \"\\\"$u\\\"\" index.jsonl | tail -1 | python3 -c \"import sys,json;print(json.loads(sys.stdin.readline())['file'])\" 2>/dev/null); echo \"##### $w $f\"; [ -n \"$f\" ] && python3 - \"$f\" <<'EOF'\nimport sys,re,os\np=sys.argv[1]\nif not os.path.isabs(p): p=os.path.join('/home/sfmqrb/git/rishe-private',p)\nt=open(p).read()\nfor m in re.finditer(r'Etymology[^\\n]*\\n(.{0,700})',t,re.S):\n    s=re.sub(r'\\s+',' ',m.group(1))[:600]; print(' *',s)\nEOF\ndone 2>&1 | head -150"
}
```


### [2026-10-17T00:03:27.483Z] TOOL RESULT

```
##### گزاردن data/verification/sources/web/2ff2f8733a6f51ec.txt
 *  1.2 Pronunciation 1.3 Verb 1.3.1 Conjugation 1.3.2 Derived terms 1.4 Further reading Toggle the table of contents گزاردن 3 languages فارسی Magyar Malagasy Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Etymology [ edit ] From 
##### گزارش data/verification/sources/web/e3dc92c661860282.txt
 *  1.2 Pronunciation 1.3 Noun 1.3.1 Derived terms 1.3.2 Descendants 1.4 Further reading 2 Urdu Toggle Urdu subsection 2.1 Etymology 2.2 Pronunciation 2.3 Noun 2.3.1 Declension 2.4 References Toggle the table of contents گزارش 7 languages বাংলা فارسی ಕನ್ನಡ Kurdî Malagasy سرائیکی 中文 Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Pri
 *  [ edit ] From گزار ( gozâr- , present stem of گزاردن ( gozârdan , “ to announce ” ) ) +‎ ـش ( eš ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡu.zaː.ˈriʃ/ ( Dari, formal ) IPA ( key ) : [ɡʊ.zɑː.ɾɪʃ] ( Dari, formal ) IPA ( key ) : [ɡʊ.zɑː.ɾɪʃ] ( Kabuli ) IPA ( key ) : [ɡʊ.zɑː.ɾɪʃ] ( Hazaragi ) IPA ( key ) : [ɡu.zɔː.ɾiʃ] ( Iran, formal ) IPA ( key ) : [ɡ̥o.zɒː.ɹeʃ] ( Tajik, formal ) IPA ( key ) : [ɡu.zɔ.ɾiʃ] Rhymes: -iʃ Readings Classical reading ? guzāriš Dari reading ? guzāriš Iranian reading ? gozâreš Tajik reading ? guzoriš Homophone : گذارش ( gozâreš ) Noun [ edit ] Dari
 *  [ edit ] Borrowed from Classical Persian گزارش ( guzāriš ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /ɡʊ.zɑː.ɾɪʃ/ Rhymes: -ɪʃ Noun [ edit ] گُزارِش • ( guzāriś ) f ( Hindi spelling गुज़ारिश ) request Synonyms: عرض ( arz ) , درخواست ( darxvāst ) میری آپ سے ایک گزارش ہے۔ merī āp se aik guzāriś hai. I have a request for you. Declension [ edit ] Declension of گزارش singular plural direct گُزارِش ( guzāriś ) گُزارِشیں ( guzāriśẽ ) oblique گُزارِش ( guzāriś ) گُزارِشوں ( guzāriśõ ) vocative گُزارِش ( guzāriś ) گُزارِشو ( guzāriśo ) References [ edit ] “ گزارش ”, in اُردُو لُغَت ( urd
##### ناگزیر data/verification/sources/web/3f7db2299b29dbb3.txt
 *  1.2 Pronunciation 1.3 Adjective 1.4 Further reading Toggle the table of contents ناگزیر 4 languages فارسی Kurdî Malagasy Русский Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Etymology [ edit ] From ناـ ( nâ- ) +‎ گزیر ( gozir , “ he
##### وزیر data/verification/sources/web/bc0cadc782b786a3.txt
 *  1.2 Noun 1.2.1 Descendants 2 Persian Toggle Persian subsection 2.1 Etymology 2.2 Pronunciation 2.3 Noun 2.3.1 Related terms 2.3.2 Descendants 2.4 See also 3 Urdu Toggle Urdu subsection 3.1 Etymology 3.2 Pronunciation 3.3 Noun 3.3.1 Declension 3.3.2 Related terms 3.3.3 See also 3.4 References Toggle the table of contents وزیر 14 languages বাংলা Deutsch Ελληνικά فارسی Français Magyar Kurdî Malagasy Norsk bokmål Sängö سرائیکی Slovenščina اردو 中文 Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Rea
 *  [ edit ] Borrowed from Arabic وَزِير ( wazīr ) . Noun [ edit ] وزیر • ( vezir ) ( plural وزیرلر ( vezirler ) ) minister , cabinet minister vizier helper , assistant ( chess ) queen Descendants [ edit ] Turkish: vezir → Bulgarian: вези́р ( vezír ) → Middle French: visir French: vizir , visir → Catalan: visir → Dutch: vizier → English: vizier , vezir , vezîr ( stricter transliterations of Ottoman Turkish ) , vazir ( via Persian instead of Ottoman Turkish ) , wasir , wazir , wazīr ( directly from Arabic ) , vizir , vizeer , guazil ( less common forms ) → Irish: visír → Welsh: fisir → Italian: vi
 *  [ edit ] Borrowed from Arabic وَزِير ( wazīr ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /wa.ˈziːr/ ( Dari, formal ) IPA ( key ) : [wä.zíːɾ] ( Dari, formal ) IPA ( key ) : [wä.zíːɾ] ( Kabuli ) IPA ( key ) : [wä.zíːɾ] ( Hazaragi ) IPA ( key ) : [wä.zíɾ] ( Iran, formal ) IPA ( key ) : [væ.zíːɹ] ( Tajik, formal ) IPA ( key ) : [vä.zíɾ] Rhymes: -iːr Readings Classical reading ? wazīr Dari reading ? wazīr Iranian reading ? vazir Tajik reading ? vazir Noun [ edit ] وزیر • ( wazīr / vazir ) ( plural وزرا ( wuzarā / vozarâ ) , or وزیران ( wazīrān / vazirân ) , Tajik spelling вазир 
 *  [ edit ] Etymology tree Arabic وَزِير ( wazīr ) bor. Classical Persian وَزیر ( vazīr ) bor. Urdu وزیر Borrowed from Classical Persian وَزیر ( vazīr ) , borrowed from Arabic وَزِير ( wazīr ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /ʋə.ziːɾ/ Noun [ edit ] وَزِیر • ( vazīr ) m ( formal plural وُزَرا ( vuzarā ) or وَزِیران ( vazīrān ) , Hindi spelling वज़ीर ) ( government ) minister وَزِیرِ تِجارَت ― vazīr-i tijārat ― minister of commerce vizier ( chess ) queen / fers Synonym: فَرْزِین ( farzīn ) Declension [ edit ] Declension of وزیر singular plural direct وزیر ( vazīr ) وزیر ( 
##### گستردن data/verification/sources/web/f61b2634086adfd6.txt
 *  1.2 Pronunciation 1.3 Verb 1.3.1 Conjugation 1.3.2 Derived terms 1.4 References 1.5 Further reading Toggle the table of contents گستردن 3 languages فارسی Malagasy Русский Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Etymolo
##### بستر data/verification/sources/web/990522fab661dd7f.txt
 *  1.2 Noun 2 Ottoman Turkish Toggle Ottoman Turkish subsection 2.1 Etymology 2.2 Noun 2.2.1 Descendants 2.3 Further reading 3 Persian Toggle Persian subsection 3.1 Etymology 3.2 Pronunciation 3.3 Noun 3.3.1 Synonyms 3.3.2 Descendants 3.4 References 4 Urdu Toggle Urdu subsection 4.1 Etymology 4.2 Pronunciation 4.3 Noun Toggle the table of contents بستر 18 languages العربية Azərbaycanca বাংলা Ελληνικά فارسی Na Vosa Vakaviti Français Magyar Bahasa Indonesia 日本語 한국어 Kurdî Malagasy Polski Русский Gagana Samoa Türkçe 中文 Entry Discussion English Read 
 *  [ edit ] Borrowed from Pashto بستر , from Persian بستر . Noun [ edit ] بستر ( bastar ) the wooden base of a pillar ( plinth ) Ottoman Turkish [ edit ] Etymology [ edit ] Etymology tree Proto-Indo-European *h₂m̥bʰi Proto-Indo-Iranian *Habʰí Proto-Indo-European *ster- Proto-Indo-European *sterh₃- Persian بستر ( bestar ) bor. Ottoman Turkish بستر Borrowed from Persian بستر ( bestar ) . Noun [ edit ] بستر • ( bister ) bed , a piece of furniture on which to rest or sleep Synonym: یاتاق ( yatak ) ( in general ) anything spread out on which one may lie or sleep Synonyms: مرقد ( merkad ) , مهاد ( mih
 *  [ edit ] Etymology tree Proto-Indo-European *h₂m̥bʰi Proto-Indo-Iranian *Habʰí Proto-Indo-European *ster- Proto-Indo-European *sterh₃- Persian بستر From Middle Persian [script needed] ( wstl /⁠wistar⁠/ , “ bedding ” ) , from Proto-Iranian *Habí ( “ to, for ” ) + *starH- ( “ to spread ” ) , from Proto-Indo-Iranian *Habʰí ( “ to, for ” ) + Proto-Indo-European *sterh₃- ( “ to spread, stretch out ” ) . [ 1 ] Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /bis.ˈtar/ ( Dari, formal ) IPA ( key ) : [bɪs.t̪ʰäɾ] ( Dari, formal ) IPA ( key ) : [bɪs.t̪ʰäɾ] ( Kabuli ) IPA ( key ) : [bɪs.t̪ʰäɾ
 *  [ edit ] Etymology tree Proto-Indo-European *h₂m̥bʰi Proto-Indo-Iranian *Habʰí Proto-Indo-European *ster- Proto-Indo-European *sterh₃- Classical Persian بِسْتَر ( bistar ) bor. Urdu بستر Borrowed from Classical Persian بِسْتَر ( bistar ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /bɪs.t̪əɾ/ Noun [ edit ] بِسْتَر • ( bistar ) m ( Hindi spelling बिस्तर ) bed , mattress bedding pillow carpet Retrieved from " https://en.wiktionary.org/w/index.php?title=بستر&oldid=92979498 " Categories : Gawar-Bati terms borrowed from Pashto Gawar-Bati terms derived from Pashto Gawar-Bati terms deriv
##### گستاخ data/verification/sources/web/34858ed7e90878e6.txt
 *  1.2 Pronunciation 1.3 Adjective 1.3.1 Alternative forms 1.3.2 Derived terms 1.3.3 Descendants 1.3.4 References 2 Urdu Toggle Urdu subsection 2.1 Etymology 2.2 Pronunciation 2.3 Adjective 2.4 Further reading Toggle the table of contents گستاخ 6 languages فارسی Kurdî Malagasy سرائیکی Тоҷикӣ Türkçe Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Downl
 *  [ edit ] From Middle Persian wstʾhw' ( wistāx , “ confident, bold ” ) , from wistāxw , from Old Persian *vistāhuva- . Akin to Old Armenian վստահ ( vstah ) , an Iranian borrowing. Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡus.ˈtaːx/ ( Dari, formal ) IPA ( key ) : [ɡʊs.t̪ʰɑ́ːx] ( Dari, formal ) IPA ( key ) : [ɡʊs.t̪ʰɑ́ːx] ( Kabuli ) IPA ( key ) : [ɡʊs.t̪ʰɑ́ːx] ( Hazaragi ) IPA ( key ) : [ɡus.t̪ʰɔ́ːx] ( Iran, formal ) IPA ( key ) : [ɡ̥os.t̪ʰɒ́ːx] ( Tajik, formal ) IPA ( key ) : [ɡus.t̪ʰɔ́χ] Rhymes: -aːx Readings Classical reading ? gustāx Dari reading ? gustāx Iranian reading ?
 *  [ edit ] Borrowed from Classical Persian گُسْتاخ . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /ɡʊs.t̪ɑːx/ Adjective [ edit ] گُسْتاخ • ( gustāx ) ( Hindi spelling गुस्ताख़ ) rude , arrogant presumptuous , impudent Further reading [ edit ] “ گستاخ ”, in ریخْتَہ لُغَت ( rexta luġat ) - Rekhta Dictionary [ Urdu dictionary with meanings in Hindi & English ] , Noida, India: Rekhta Foundation, 2026 . Qureshi, Bashir Ahmad ( 1971 ), “ گستاخ ”, in Kitabistan's 20th Century Standard Dictionary , Lahore: Kitabistan Pub. Co. Retrieved from " https://en.wiktionary.org/w/index.php?title=گستاخ&
##### گسستن data/verification/sources/web/fc4f445d305ef8ab.txt
 *  1.3 Pronunciation 1.4 Verb 1.4.1 Conjugation 1.5 References Toggle the table of contents گسستن 3 languages فارسی Kurdî Malagasy Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Alternative forms [ edit ] گسیختن ( gosixtan ) ( less co
 *  [ edit ] From Middle Persian [Book Pahlavi needed] ( wsstn' /⁠wisistan⁠/ , “ to break, split ” ) , from Proto-Iranian *wi- + *said- , ultimately from Proto-Indo-European *skeyd- (Cheung 2007). Cognate with Baluchi سندگ ( sendag , “ to break, split ” ) , Latin scindo , and Ancient Greek σχίζω ( skhízō ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡu.sis.ˈtan/ , /ɡu.sas.ˈtan/ ( Dari, formal ) IPA ( key ) : [ɡʊ.säs.t̪ʰán] ( Dari, formal ) IPA ( key ) : [ɡʊ.säs.t̪ʰán] ( Kabuli ) IPA ( key ) : [ɡʊ.säs.t̪ʰán] ( Hazaragi ) IPA ( key ) : [ɡu.säs.t̪ʰán] ( Iran, formal ) IPA ( key ) :
##### گسیختن data/verification/sources/web/88fb4170fcd85fa0.txt
##### گسیل data/verification/sources/web/61f4c4083fbdbd8d.txt
 *  1.3 Pronunciation 1.4 Noun 1.4.1 Derived terms 1.5 Further reading Toggle the table of contents گسیل 1 language Malagasy Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Alternative forms [ edit ] گسی ( gusē ) Etymology [ edit ] T
##### گشادن data/verification/sources/web/f11d95d753a35820.txt
##### گشودن data/verification/sources/web/3d9b7359f760d8f8.txt
 *  1.3 Pronunciation 1.4 Verb 1.4.1 Usage notes 1.4.2 Conjugation 1.4.3 Derived terms 1.5 References Toggle the table of contents گشودن 6 languages فارسی Magyar Kurdî Limburgs Malagasy Русский Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Per
 *  [ edit ] Inherited from Middle Persian [script needed] ( wšʾtn' /⁠wišādan⁠/ , “ to open, loose, free ” ) , ultimately from Proto-Indo-European *sh₂ey- ( “ to bind, fetter ” ) with the preverb *wi- . "To conquer": semantic loan from Arabic فَتَحَ ( fataḥa , “ to open; to conquer ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡu.ʃuː.ˈdan/ ( Dari, formal ) IPA ( key ) : [ɡʊ.ʃuː.d̪án] ( Dari, formal ) IPA ( key ) : [ɡʊ.ʃuː.d̪án] ( Kabuli ) IPA ( key ) : [ɡʊ.ʃuː.d̪án] ( Hazaragi ) IPA ( key ) : [ɡu.ʃu.d̪án] ( Iran, formal ) IPA ( key ) : [ɡ̥o.ʃuː.d̪ǽn] ( Tajik, formal ) IPA ( ke
##### بیمار data/verification/sources/web/9bdd698dbf218db3.txt
 *  1.2 Pronunciation 1.3 Noun 1.3.1 Derived terms 1.4 Adjective 1.4.1 Inflection 1.5 Descendants 1.6 Further reading 2 Urdu Toggle Urdu subsection 2.1 Etymology 2.2 Pronunciation 2.3 Adjective 2.3.1 Derived terms 2.4 Further reading Toggle the table of contents بیمار 16 languages العربية Deutsch فارسی Na Vosa Vakaviti Magyar Bahasa Indonesia 日本語 한국어 Kurdî Кыргызча Malagasy Polski Русский سرائیکی Türkçe 中文 Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Rel
 *  [ edit ] From Middle Persian 𐭥𐭩𐭬𐭠𐭫 ( wēmār , “ sick, ill ” ) , from Proto-Indo-European *wemh₁- ( “ to spew, vomit ” ) + ār ( agent suffix ) . Cognate with Latin vomō ( “ be sick, vomit ” ) , Northern Kurdish bîvêr . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /beː.ˈmaːr/ , /biː.ˈmaːr/ ( Dari, formal ) IPA ( key ) : [beː.mɑ́ːɾ] ( Dari, formal ) IPA ( key ) : [beː.mɑ́ːɾ] ( Kabuli ) IPA ( key ) : [beː.mɑ́ːɾ] ( Hazaragi ) IPA ( key ) : [beː.mɔ́ːɾ] ( Iran, formal ) IPA ( key ) : [biː.mɒ́ːɹ] ( Tajik, formal ) IPA ( key ) : [be.mɔ́ɾ] Rhymes: -aːr Readings Classical reading ? bēmār, b
 *  [ edit ] Etymology tree Proto-Indo-European *wemh₁- Middle Persian -ār Middle Persian wymʾl Classical Persian بیمار ( bīmār ) bor. Urdu بیمار Borrowed from Classical Persian بیمار ( bīmār ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /biː.mɑːɾ/ Rhymes: -ɑːɾ Hyphenation: بی‧مار Adjective [ edit ] بِیمار • ( bīmār ) ( indeclinable , Hindi spelling बीमार ) ill ; sick Synonyms: مَرِیض ( marīẓ ) , روگی ( rogī ) ( figuratively ) in love , lover Derived terms [ edit ] بیمار خانہ ( bīmār xāna , “ hospital ” ) بیمارستان ( bīmāristān , “ hospital ” ) بیماری ( bīmārī , “ illness ” ) Further
##### ویراستن data/verification/sources/web/2e6a0256f47ff365.txt
 *  1.2 Pronunciation 1.3 Verb 1.3.1 Conjugation 1.3.2 Derived terms 1.3.3 Related terms 1.3.4 References Toggle the table of contents ویراستن 2 languages فارسی Malagasy Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Etymology [ e
##### گمان data/verification/sources/web/5caa849055e8d3da.txt
 *  1.2 Pronunciation 1.3 Noun 1.3.1 Descendants 2 Urdu Toggle Urdu subsection 2.1 Etymology 2.2 Pronunciation 2.3 Noun Toggle the table of contents گمان 9 languages বাংলা Bahasa Indonesia Kurdî Malagasy پښتو Русский سرائیکی Türkçe 中文 Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sideb
 *  [ edit ] Inherited from Middle Persian [script needed] ( gwmʾn' /⁠gumān⁠/ , “ doubt ” ) , from Proto-Iranian *wimānah , from Proto-Indo-Iranian . Compare Avestan 𐬬𐬍𐬨𐬀𐬥𐬋 ( vīmanō , one of the Ahrimanic plagues : doubt? ) , Sanskrit विमनस् ( vimanas , “ sad, disconsolate ” ) Northern Luri گمو ( gemo ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡu.ˈmaːn/ ( Dari, formal ) IPA ( key ) : [ɡʊ.mɑːn] ( Dari, formal ) IPA ( key ) : [ɡʊ.mɑːn] ( Kabuli ) IPA ( key ) : [ɡʊ.mɑːn] ( Hazaragi ) IPA ( key ) : [ɡu.mɔːn] ( Iran, formal ) IPA ( key ) : [ɡ̥o.mɒːn] , [ɡʲæ.mɒːn] ( Iran, formal ) 
 *  [ edit ] Borrowed from Classical Persian گُمان ( gumān ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /ɡʊ.mɑːn/ Noun [ edit ] گُمان • ( gumān ) m ( Hindi spelling गुमान ) mistrust , doubt ; uncertainty Synonyms: شَک ( śak ) , سَنْشَیَہ ( sanśaya ) , سَنْدیہ ( sandeh ) , شُبَہ ( śuba ) , رَیب ( raib ) , بھَرَم ( bharam ) Retrieved from " https://en.wiktionary.org/w/index.php?title=گمان&oldid=93354356 " Categories : Persian terms inherited from Middle Persian Persian terms derived from Middle Persian Persian terms inherited from Proto-Iranian Persian terms derived from Proto-Iranian
##### گماردن data/verification/sources/web/61a4218f36cf53a5.txt
##### گماشتن data/verification/sources/web/ed902cb96c9844c2.txt
 *  1.3 Pronunciation 1.4 Verb 1.4.1 Conjugation 1.4.2 References Toggle the table of contents گماشتن 3 languages فارسی Kurdî Malagasy Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Alternative forms [ edit ] گماردن ( gomârdan ) , گمار
 *  [ edit ] From Middle Persian [Book Pahlavi needed] ( gwmʾl-tn' /⁠gumārdan⁠/ ) , 𐫃𐫇𐫖𐫀𐫡𐫅𐫗 ( gwmʾrdn /⁠gumārdan⁠/ , “ to appoint, commission, entrust ” ) , ultimately from Proto-Indo-European *mere ( “ to delay, hinder ” ) . Cognate with Latin mora ( “ delay ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡu.maːʃ.ˈtan/ ( Dari, formal ) IPA ( key ) : [ɡʊ.mɑːʃ.t̪ʰän] ( Dari, formal ) IPA ( key ) : [ɡʊ.mɑːʃ.t̪ʰän] ( Kabuli ) IPA ( key ) : [ɡʊ.mɑːʃ.t̪ʰän] ( Hazaragi ) IPA ( key ) : [ɡu.mɔːʃ.t̪ʰän] ( Iran, formal ) IPA ( key ) : [ɡ̥o.mɒːʃ.t̪ʰæn] ( Tajik, formal ) IPA ( key ) : [ɡu.m
##### گواه data/verification/sources/web/5b194abd77be720f.txt
 *  1.2 Pronunciation 1.3 Noun 1.3.1 Related terms 1.3.2 Descendants 1.4 References Toggle the table of contents گواه 5 languages فارسی Kurdî Malagasy Norsk bokmål Türkçe Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Etymology [
##### گریختن data/verification/sources/web/6364ae8f34d0efd9.txt
 *  1.2 Pronunciation 1.3 Verb 1.3.1 Usage notes 1.3.2 Synonyms 1.3.3 Derived terms 1.4 References Toggle the table of contents گریختن 3 languages فارسی Kurdî Malagasy Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Etymology [ e
##### بیست data/verification/sources/web/2f867610b64a81e2.txt
 *  2.2 Pronunciation 2.3 Numeral 3 Persian Toggle Persian subsection 3.1 Etymology 3.2 Pronunciation 3.3 Numeral 3.3.1 Descendants 3.4 References Toggle the table of contents بیست 16 languages العربية Cymraeg Deutsch فارسی Français Magyar Bahasa Indonesia 日本語 کٲشُر Kurdî Lietuvių Malagasy Nederlands Polski Română 中文 Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export 
 *  [ edit ] From Proto-Iranian *HwiHcati , from Proto-Indo-Iranian *HwiHćati , Proto-Indo-European *h₁wih₁ḱm̥ti , from *dwih₁ḱm̥ti . Compare Persian بیست ( bist ) . Pronunciation [ edit ] IPA ( key ) : /biːst/ Numeral [ edit ] بیست ( bîst ) twenty ; 20 Persian [ edit ] Persian numbers ( edit ) 200 [a] , [b] ← 10 [a] , [b] ← 19 ۲۰ 20 21 → 30 → 2 Cardinal : بیست ( bist ) Ordinal : بیستم ( bistom ) Dari بیست Iranian Persian Tajik бист Etymology [ edit ] Etymology tree Proto-Indo-European *dwih₁ḱm̥ti Proto-Indo-Iranian *HwiHćati Proto-Iranian *HwiHcati Old Persian 𐎻𐎡𐎰𐎫 ( vi-i-θ-t ) Middle Persian wy
##### گذشتن data/verification/sources/web/edb20513fd1b720e.txt
 *  1.3 Pronunciation 1.4 Verb 1.4.1 Usage notes 1.4.2 Conjugation 1.4.3 Derived terms 1.4.4 Related terms 1.5 References Toggle the table of contents گذشتن 7 languages Azərbaycanca فارسی Magyar Kurdî Malagasy Русский Тоҷикӣ Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From
 *  [ edit ] From Middle Persian [script needed] ( wtštn' /⁠widaštan⁠/ ) , [script needed] ( wtltn' /⁠widardan⁠/ , “ pass, cross, die ” ) , [ 1 ] from Proto-Iranian *witárHati ( “ to pass by ” ) , from Proto-Indo-Iranian *wí + Proto-Indo-Iranian *tárHati ( “ to cross over ” ) , the prefix ultimately from Proto-Indo-European *wí ( “ apart ” ) . [ 2 ] The change -d- → classical -ð- → modern -z- is irregular, since following the second stage, it would be reverted again into the first one. Cognate with Baluchi گوزگ ( gwazag , “ to pass ” ) , Northern Kurdish bihurîn ( “ to pass ” ) , Central Kurdish 
##### گذاشتن data/verification/sources/web/b2c674dbf07adcf4.txt
 *  1.3 Pronunciation 1.4 Verb 1.4.1 Conjugation 1.4.2 Related terms 1.5 References Toggle the table of contents گذاشتن 11 languages Azərbaycanca فارسی Français Magyar Bahasa Indonesia Kurdî Lietuvių Malagasy Polski Русский Тоҷикӣ Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide 
 *  [ edit ] Causative transitive form of گذشتن ( guzaštan / gozaštan , “ to pass ” ) . [ 1 ] Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡu.ðaːʃ.ˈtan/ ( Dari, formal ) IPA ( key ) : [ɡʊ.zɑːʃ.t̪ʰán] ( Dari, formal ) IPA ( key ) : [ɡʊ.zɑːʃ.t̪ʰán] ( Kabuli ) IPA ( key ) : [ɡʊ.zɑːʃ.t̪ʰán] ( Hazaragi ) IPA ( key ) : [ɡu.zɔːʃ.t̪ʰán] ( Iran, formal ) IPA ( key ) : [ɡ̥o.zɒːʃ.t̪ʰǽn] ( Tajik, formal ) IPA ( key ) : [ɡu.zɔʃ.t̪ʰán] Rhymes: -an Readings Classical reading ? guḏāštan Dari reading ? guzāštan Iranian reading ? gozâštan Tajik reading ? guzoštan Verb [ edit ] گذاشتن • ( guzāštan / 
##### گزیدن data/verification/sources/web/076d440621d6879d.txt
 *  1.1.1 Pronunciation 1.1.2 Verb 1.1.2.1 Derived terms 1.2 Etymology 2 1.2.1 Pronunciation 1.2.2 Verb 1.2.2.1 Derived terms 1.3 References Toggle the table of contents گزیدن 6 languages فارسی Magyar Kurdî Malagasy Polski Русский Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hid
 *  [ edit ] From Middle Persian [Book Pahlavi needed] ( gzytn' /⁠gazīdan⁠/ ) . Cognate with Gilaki گشتن ( gaštən ) (present stem: گز ( gaz ) ), Central Kurdish گەستن ( gestin ) and Northern Kurdish gestin . Compare Old Armenian գազան ( gazan ) , an Iranian borrowing. Pronunciation [ edit ] Dari گزیدن Iranian Persian Tajik газидан ( Classical Persian ) IPA ( key ) : /ɡa.ziː.ˈdan/ ( Dari, formal ) IPA ( key ) : [ɡä.ziː.d̪án] ( Dari, formal ) IPA ( key ) : [ɡä.ziː.d̪án] ( Kabuli ) IPA ( key ) : [ɡä.ziː.d̪án] ( Hazaragi ) IPA ( key ) : [ɡä.zi.d̪án] ( Iran, formal ) IPA ( key ) : [ɡʲæ.ziː.d̪ǽn] ( Taj
 *  [ edit ] From Middle Persian [Term?] ( /⁠wizīdan⁠/ ) , ultimately from Proto-Indo-European *kʷey- ( “ to pay ” ) . Compare Baluchi گچین ( gechén , “ choice ” ) , Northern Kurdish bijartin and Old Armenian վճիտ ( včit ) , an Iranian borrowing. Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡu.ziː.ˈdan/ ( Dari, formal ) IPA ( key ) : [ɡʊ.ziː.d̪án] ( Dari, formal ) IPA ( key ) : [ɡʊ.ziː.d̪án] ( Kabuli ) IPA ( key ) : [ɡʊ.ziː.d̪án] ( Hazaragi ) IPA ( key ) : [ɡu.zi.d̪án] ( Iran, formal ) IPA ( key ) : [ɡ̥o.ziː.d̪ǽn] ( Tajik, formal ) IPA ( key ) : [ɡu.zi.d̪án] Rhymes: -an Readings Cl
##### گزند data/verification/sources/web/b79fd8f6af38b809.txt
 *  1.2 Pronunciation 1.3 Noun 1.3.1 Descendants 1.4 References Toggle the table of contents گزند 4 languages فارسی Malagasy Русский Türkçe Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Etymology [ edit ] Inherited from Middle Persi
##### گمیز data/verification/sources/web/54ce5f1a21cf4d3b.txt
##### آمیختن data/verification/sources/web/5e92d127d61193b9.txt
 *  1.2 Pronunciation 1.3 Verb 1.3.1 Conjugation 1.4 References Toggle the table of contents آمیختن 8 languages فارسی Magyar Bahasa Indonesia Kurdî Malagasy Русский Тоҷикӣ 中文 Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Etymolo
```


## [2026-10-17T00:03:36.276Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for w in گزاردن ناگزیر گستردن گسیل گشادن ویراستن گواه گریختن بیست گزند آمیختن گسیختن گماردن گمیز وزیر; do u=\"https://en.wiktionary.org/wiki/$w\"; f=$(grep -F \"\\\"$u\\\"\" index.jsonl | tail -1 | python3 -c \"import sys,json;print(json.loads(sys.stdin.readline())['file'])\"); echo \"##### $w $(wc -c < /home/sfmqrb/git/rishe-private/$f)\"; python3 - \"/home/sfmqrb/git/rishe-private/$f\" <<'EOF'\nimport sys,re\nt=re.sub(r'\\s+',' ',open(sys.argv[1]).read())\nfor m in re.finditer(r'Etymology \\[ edit \\](.{0,450})',t):\n    print(' *',m.group(1))\nEOF\ndone"
}
```


### [2026-10-17T00:03:38.648Z] TOOL RESULT

```
##### گزاردن 7944
 *  From Middle Persian [Book Pahlavi needed] ( wcʾltn' /⁠wizārdan, wizār-⁠/ , “ to separate; to explain, interpret; to perform, fulfil, redeem ” ) , from Proto-Iranian *wí ( “ apart ” ) + a causative formation from Proto-Iranian *čarH ( “ to come and go, wander ” ) , from Proto-Indo-Iranian *wí + Proto-Indo-Iranian *čálHati ( “ to move, wander ” ) , the prefix ultimately from Proto-Indo-European *wí ( “ apart ” ) . Compare Old Armenian վճար ( včar 
##### ناگزیر 3965
 *  From ناـ ( nâ- ) +‎ گزیر ( gozir , “ help, remedy ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /naː.ɡu.ˈziːr/ ( Dari, formal ) IPA ( key ) : [nɑː.ɡʊ.zíːɾ] ( Dari, formal ) IPA ( key ) : [nɑː.ɡʊ.zíːɾ] ( Kabuli ) IPA ( key ) : [nɑː.ɡʊ.zíːɾ] ( Hazaragi ) IPA ( key ) : [nɔː.ɡu.zíɾ] ( Iran, formal ) IPA ( key ) : [nɒː.ɡo.zíːɹ] ( Tajik, formal ) IPA ( key ) : [nɔ.ɡu.zíɾ] Rhymes: -iːr Readings Classical reading ? nāguzīr Dari readin
##### گستردن 11930
 *  Inherited from Middle Persian wstltn' ( /⁠wistardan⁠/ ) , [ 1 ] [ 2 ] [ 3 ] from Proto-Indo-Iranian *str̥náHti , ultimately from Proto-Indo-European *sterh₃- . Compare Avestan 𐬯𐬙𐬀𐬭- ( star- , “ to spread ” ) ), Latin sternō ( “ to bestrew, sprinkle ” ) , Sanskrit स्तृणाति ( stṛṇā́ti ) , Ancient Greek στόρνῡμι ( stórnūmi ) , Old Church Slavonic (о)строуити ( (o)struiti ) , Old English strewian (whence English strew ). Pronunciation [ edit ] ( Cla
##### گسیل 3117
 *  The additional 'l' phoneme most probably appeared due to influence from the present stem of گسستن ( gosastan , “ to separate, split, to disconnect, to take apart ” ) , i.e. گسل ( gosil ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡu.ˈsiːl/ ( Dari, formal ) IPA ( key ) : [ɡʊ.síːl] ( Dari, formal ) IPA ( key ) : [ɡʊ.síːl] ( Kabuli ) IPA ( key ) : [ɡʊ.síːl] ( Hazaragi ) IPA ( key ) : [ɡu.síl̥] ( Iran, formal ) IPA ( key ) : [ɡ̥o.
##### گشادن 16398
##### ویراستن 7683
 *  From Middle Persian wyrʾst, wyrʾy- ( wirāst, widrāy- , “ to arrange, prepare, cultivate, restore ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /wiː.raːs.ˈtan/ ( Dari, formal ) IPA ( key ) : [wiː.ɾɑːs.t̪ʰán] ( Dari, formal ) IPA ( key ) : [wiː.ɾɑːs.t̪ʰán] ( Kabuli ) IPA ( key ) : [wiː.ɾɑːs.t̪ʰán] ( Hazaragi ) IPA ( key ) : [wi.ɾɔːs.t̪ʰán] ( Iran, formal ) IPA ( key ) : [viː.ɹɒːs.t̪ʰǽn] ( Tajik, formal ) IPA ( key ) : [vi.ɾɔs.t̪
##### گواه 5268
 *  From Middle Persian gwk’dy ( gugāy ) . From Proto-Indo-European *wí ( “ apart ” ) + *kʷeḱ- ( “ to see ” ) ; literally meaning “to see apart, differentiate”. Compare Old Armenian վկայ ( vkay ) , an Iranian borrowing. Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡu.ˈwaːh/ ( Dari, formal ) IPA ( key ) : [ɡʊ.wɑ́ːʱ] ( Dari, formal ) IPA ( key ) : [ɡʊ.wɑ́ːʱ] ( Kabuli ) IPA ( key ) : [ɡʊ.wɑ́ː] ( Hazaragi ) IPA ( key ) : [ɡu.wɔ́ː] ( Iran,
##### گریختن 4413
 *  From Middle Persian OLYKWN-tn', wlyhtn' ( wirēxtan ) , ultimately from Proto-Indo-European *wí ( “ apart ” ) + *leykʷ- ( “ to leave ” ) ; whence also ریختن ( rixtan , “ to pour ” ) . Cognate with Avestan 𐬬𐬌𐬭𐬁𐬈𐬗 ( virāec , “ leave away, run away ” ) , Gilaki وروتن ( vörütən ) (present stem وروج ( vörüj ) ). Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡu.reːx.ˈtan/ ( Dari, formal ) IPA ( key ) : [ɡʊ.ɾeːx.t̪ʰán] ( Dari, formal ) IPA
##### بیست 6719
 *  From Proto-Iranian *HwiHcati , from Proto-Indo-Iranian *HwiHćati , Proto-Indo-European *h₁wih₁ḱm̥ti , from *dwih₁ḱm̥ti . Compare Persian بیست ( bist ) . Pronunciation [ edit ] IPA ( key ) : /biːst/ Numeral [ edit ] بیست ( bîst ) twenty ; 20 Persian [ edit ] Persian numbers ( edit ) 200 [a] , [b] ← 10 [a] , [b] ← 19 ۲۰ 20 21 → 30 → 2 Cardinal : بیست ( bist ) Ordinal : بیستم ( bistom ) Dari بیست Iranian Persian Tajik бист Etymology [ edit ] Etymol
##### گزند 3603
 *  Inherited from Middle Persian wsydy ( /⁠wizend⁠/ , “ hurt , harm , injury ” ) [ 1 ] , a prefixed form of Proto-Iranian *ǰán- . See زَدَن ( zadan ) for more. Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ɡa.ˈzand/ ( Dari, formal ) IPA ( key ) : [ɡä.zán̪d̪] ( Dari, formal ) IPA ( key ) : [ɡä.zán̪d̪] ( Kabuli ) IPA ( key ) : [ɡä.zán̪d̪] ( Hazaragi ) IPA ( key ) : [ɡä.zán̪d̪̥] ( Iran, formal ) IPA ( key ) : [ɡʲæ.zǽn̪d̪̥] ( Tajik, forma
##### آمیختن 12358
 *  Inherited from Middle Persian ʾmyhtn ( āmēxtan ) , ultimately from Proto-Indo-European *meyḱ- , whence also English mix . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ʔaː.meːx.ˈtan/ ( Dari, formal ) IPA ( key ) : [ʔɑː.meːx.t̪ʰán] ( Dari, formal ) IPA ( key ) : [ʔɑː.meːx.t̪ʰán] ( Kabuli ) IPA ( key ) : [ʔɑː.meːx.t̪ʰán] ( Hazaragi ) IPA ( key ) : [ʔɔː.meːx.t̪ʰán] ( Iran, formal ) IPA ( key ) : [ʔɒː.miːx.t̪ʰǽn] ( Tajik, formal ) IPA 
##### گسیختن 138
##### گماردن 138
##### گمیز 134
##### وزیر 9553
 *  Borrowed from Arabic وَزِير ( wazīr ) . Noun [ edit ] وزیر • ( vezir ) ( plural وزیرلر ( vezirler ) ) minister , cabinet minister vizier helper , assistant ( chess ) queen Descendants [ edit ] Turkish: vezir → Bulgarian: вези́р ( vezír ) → Middle French: visir French: vizir , visir → Catalan: visir → Dutch: vizier → English: vizier , vezir , vezîr ( stricter transliterations of Ottoman Turkish ) , vazir ( via Persian instead of Ottoman Turkish )
 *  Borrowed from Arabic وَزِير ( wazīr ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /wa.ˈziːr/ ( Dari, formal ) IPA ( key ) : [wä.zíːɾ] ( Dari, formal ) IPA ( key ) : [wä.zíːɾ] ( Kabuli ) IPA ( key ) : [wä.zíːɾ] ( Hazaragi ) IPA ( key ) : [wä.zíɾ] ( Iran, formal ) IPA ( key ) : [væ.zíːɹ] ( Tajik, formal ) IPA ( key ) : [vä.zíɾ] Rhymes: -iːr Readings Classical reading ? wazīr Dari reading ? wazīr Iranian reading ? vazir Tajik readi
 *  Etymology tree Arabic وَزِير ( wazīr ) bor. Classical Persian وَزیر ( vazīr ) bor. Urdu وزیر Borrowed from Classical Persian وَزیر ( vazīr ) , borrowed from Arabic وَزِير ( wazīr ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /ʋə.ziːɾ/ Noun [ edit ] وَزِیر • ( vazīr ) m ( formal plural وُزَرا ( vuzarā ) or وَزِیران ( vazīrān ) , Hindi spelling वज़ीर ) ( government ) minister وَزِیرِ تِجارَت ― vazīr-i tijārat ― minister of commerce vi
```


## [2026-10-17T00:04:19.516Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/وزير\" \"https://www.etymonline.com/word/vizier\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wí\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wi\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wíHcati\"; do python3 tools/fetch_source.py \"$u\" --note \"page 553, root Wi: wazir / PIE *wi- / bist\"; done; cd data/verification/sources/web; for u in \"https://en.wiktionary.org/wiki/وزير\" \"https://www.etymonline.com/word/vizier\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wí\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wi\" \"https://en.wiktionary.org/wiki/گشادن\"; do f=$(grep -F \"\\\"$u\\\"\" index.jsonl | tail -1 | python3 -c \"import sys,json;print(json.loads(sys.stdin.readline())['file'])\"); echo \"##### $u $(wc -c < /home/sfmqrb/git/rishe-private/$f)\"; python3 - \"/home/sfmqrb/git/rishe-private/$f\" <<'EOF'\nimport sys,re\nt=re.sub(r'\\s+',' ',open(sys.argv[1]).read())\nms=list(re.finditer(r'(Etymology \\[ edit \\]|vizier \\(n\\.\\)|Reconstruction|Etymology)(.{0,700})',t))\nfor m in ms[:4]: print(' *',m.group(2))\nEOF\ndone"
}
```


### [2026-10-17T00:04:22.692Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/837a8e0d0481e27b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/185fbf580ef8515f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ce45c9ba04e3cb57.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a9fcaea7de7aed7b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a3f9c6c8aab7502d.txt
##### https://en.wiktionary.org/wiki/وزير 10905
 *  1.2 Pronunciation 1.3 Noun 1.3.1 Declension 1.3.2 Derived terms 1.3.3 Related terms 1.3.4 Descendants 1.4 See also 1.5 References 2 Pashto Toggle Pashto subsection 2.1 Etymology 2.2 Pronunciation 2.3 Proper noun 3 South Levantine Arabic Toggle South Levantine Arabic subsection 3.1 Etymology 3.2 Pronunciation 3.3 Noun 3.3.1 See also Toggle the table of contents وزير 16 languages Čeština Deutsch Français Magyar Bahasa Indonesia Ido 한국어 Kurdî Malagasy Norsk bokmål Polski پښتو Português Русский اردو 中文 Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information
 *  The original attested meaning is “assistant”, and the political sense only arose in the Umayyad period . Likely related to the verb وَزَرَ ( wazara , “ to carry, to shoulder ” ) with the root و ز ر ( w z r ) , meaning “someone who carries a burden”, but owing to the idea of assistance by handmen this may be denominal. Likely borrowed from an Iranian term surfacing as Middle Persian [script needed] ( wcyl /⁠vičīr⁠/ , “ decision, judgment ” ) , Avestan 𐬬𐬍𐬗𐬌𐬭𐬀 ( vīcira , “ arbitrator, judge ” , literally “ deciding, one who is taking or has made a decision ” ) , Old Armenian վճիռ ( včiṙ ) . Pronunciation [ edit ] IPA ( key ) : /wa.ziːr/ Audio : ( file ) Noun [ edit ] وَزِير • ( wazīr ) m ( plu
 *  Borrowed from Arabic وَزِير ( wazīr , “ assistant ” ) . Pronunciation [ edit ] IPA ( key ) : /wəzir/ Proper noun [ edit ] وزير • ( Wëzír ) m Wazir , a Pashtun tribe a male given name , Wazir , from Arabic South Levantine Arabic [ edit ] Etymology [ edit ] Inherited from Arabic وَزِير ( wazīr ) . Pronunciation [ edit ] IPA ( key ) : /wa.ziːr/ , [waˈziːr] Audio ( al-Lidd ) : ( file ) Noun [ edit ] وزير • ( wazīr ) m ( plural وزرا ( wuzara ) ) minister ( chess ) bishop See also [ edit ] Chess pieces in South Levantine Arabic · قطع الشطرنج ( ʔuṭaʕ iš-šaṭranj ) ( layout · text ) ملك ( malik ) ملكة ( malike ) قلعة ( ʔalʕa ) وزير ( wazīr ) حصان ( ḥsān ) جندي ( jundi ) Retrieved from " https://en.w
##### https://www.etymonline.com/word/vizier 133
##### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wí 6842
 * :Proto-Indo-European/wí FETCHED: 2026-10-17T00:04:21Z STATUS: 200 TITLE: Reconstruction:Proto-Indo-European/wí - Wiktionary, the free dictionary Reconstruction:Proto-Indo-European/wí - Wiktionary, the free dictionary Jump to content Main menu Main menu move to sidebar hide Navigation Main page Community portal Requested entries Recent changes Random entry Help Glossary Contact us Special pages Search Search Appearance Donations Create account Log in Personal tools Donations Create account Log in Contents move to sidebar hide Beginning 1 Proto-Indo-European Toggle Proto-Indo-European subsection 1.1 Etymology 1.2 Adverb 1.2.1 Alternative reconstructions 1.2.2 Derived terms 1.2.3 Descendants 1.
 * :Proto-Indo-European/ wí Add languages Reconstruction Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Get shortened URL Print/export Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence. Proto-Indo-European [ edit ] Etymology [ edit ] Likely from *dwi- , [ 1 ] with *d dropped, or possibl
 * :Proto-Indo-European/wí&oldid=92151887 " Categories : Proto-Indo-European terms belonging to the word *dwóh₁ Proto-Indo-European lemmas Proto-Indo-European adverbs Hidden categories: Pages with etymon Proto-Indo-European entries with etymon Pages using etymon with no ID Pages with entries Pages with 1 entry Sanskrit terms with non-redundant manual transliterations Pages linking to anchors not found in Appendix:Glossary Requests for attention concerning Proto-Indo-Iranian Requests for attention concerning Proto-Iranian attention lacking explanation Requests for native script for Khotanese terms Sogdian term requests Sogdian terms with redundant script codes Parthian term requests Parthian ter
 * :Proto-Indo-European/ wí Add languages Add topic
##### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wi 157
 * :Proto-Iranian/wi FETCHED: 2026-10-17T00:04:21Z STATUS: -1 TITLE: FETCH FAILED: HTTP Error 404: Not Found
##### https://en.wiktionary.org/wiki/گشادن 16398
```


## [2026-10-17T00:04:29.572Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"wizIr|wizīr|wicīr|wizir\" \"wizārdan|wizardan\" \"wizārišn|wizarisn\" \"wistardan|wistar\\b\" \"wistāx|wistax\" \"wisistan|wisastan|wisist\" \"wišādan|wisadan|wišād\" \"wēmār|wemar\" \"wirāstan|wirastan\" \"gumān|guman\" \"gumārdan|gumardan|gumāštan\" \"gugāy|gukāy|gugay\" \"wirēxtan|wirextan|wirēz\" \"^wīst|wīst \" \"widardan|widaštan\" \"wizīdan|wizidan|wizīn\" \"wizend|wizand|gazand\" \"gazīdan|gazidan\" \"gumēxtan|gumextan|gumēz\" \"gōmēz|gomez\"; do echo \"## $w\"; grep -n -i -E \"$w\" PHD.txt | head -4; done"
}
```


### [2026-10-17T00:04:30.259Z] TOOL RESULT

```
<persisted-output>
Output too large (37.8KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bra9ouef9.txt

Preview (first 2KB):
## wizIr|wizīr|wicīr|wizir
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
...
</persisted-output>
```


## [2026-10-17T00:04:33.885Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"wizīr \\[\" \"wizārdan\" \"wistardan\" \"wistāx\" \"wisistan\" \"wišādan\" \"wēmār\" \"wirāstan\" \"gumān \\[\" \"gumārdan\" \"gugāy\" \"wirēxtan\" \"wīst \\[\" \"widardan\" \"wizīdan\" \"wizend|wizand\" \"gazīdan\" \"gumēxtan\" \"gōmēz\" \"wizīrgar|wizirgar\"; do echo \"## $w\"; grep -o -i -E \".{0,10}($w).{0,180}\" PHD.txt | head -2; done"
}
```


### [2026-10-17T00:04:36.558Z] TOOL RESULT

```
## wizīr \[
## wizārdan
lanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption.
fulfil wizārdan.
## wistardan
wistardan 92 wizürdan
wistardan, wistar- [wstl-tn! | N gustardan] spread. wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold. ~ih: confidence, boldness. wis [w(y)$ | M wyš, N gus] poison, venom, bil
## wistāx
] spread. wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold. ~ih: confidence, boldness. wis [w(y)$ | M wyš, N gus] poison, venom, bile. wišād [SLYTWNt', Р! | M wid, N gušād] open, wi
bold wistāx; v. brave.
## wisistan
despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twent
eak (vi.) wisistan; v. broken.
## wišādan
e, loose. wišādan, *wišāy- [SLYTWN-tn! < A У šrh; wPtn! | M шурап, (wys?h-), N gušādan, gušāy-) open, loose, free. wišād-dar [.SL Y TWNt! BBA] hospitable. wišād-dwārišnīh [zP??! dzb?lšnyh) going ab
išāy-, v. wišādan. wiškar [zo£hl | N bisgar(d)] hunting-ground, wilderness. wiškīdan, wiškin(n)- [wfkytn!, wškn-] divide, separate. ~išn: separation. wiskofag [wskwpk' | N biškēfa] blossom. wiškuft
## wēmār
 P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn
št(ag)īh, wēmārih, xindagih, yask.
## wirāstan
become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful 
nderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guré
## gumān \[
## gumārdan
 griftan, gumārdan,hištan.
espurdan, gumārdan.
## gugāy
tness zūr-gugāy.
witness gugāy; false — zūr-gugāy.
## wirēxtan
Лее wirēxtan.
g wircz-! wirēxtan! wircz- waranigih waranig wurróyisn waran
## wīst \[
## widardan
~ widardan: outstrip. andarag [adig] in, between, among. andarmāh [?ndim’h] new moon. andarón [?ndlwn! | M ?ndrwn, N —rün] inside, within, andarway [ndlw?d | (P ?ndrw'z)] air, atmosphere.
 passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N gu
## wizīdan
) wēxtan, wizīdan.
 wazīdan, wizīdan wizoh/y- wizoh/yisn wuzurg wuzurgih wizurdih wizurd wizóstan waččag wuzurg wuzurgih wačast wizistan wazišnig wazišn.
## wizend|wizand
nocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
 : merry. wizandag [wzndk'] quaking. wizandidan, wizand- [wznd-ytn'] tremble, quake. -išn: quaking. wizar [wc] | M wer] separation; explanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?
## gazīdan
dazīdan, gazīdan
## gumēxtan
## gōmēz
## wizīrgar|wizirgar
```


## [2026-10-17T00:04:41.455Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"wiz.r \\[\" \"wizirgar|wiz.rgar\" \"gum.n \\[\" \"gum.rdan, \" \"gug.y \\[\" \"wir.xtan, \" \"wist \\[\" \"wid.rdan, wid\" \"wiz.dan, \" \"wizend \\[|wizand \\[\" \"gaz.dan, \" \"gum.xtan|gum.zi\" \"g.m.z \\[\" \"wiz.r \\[wcy\" \"gazand\"; do echo \"## $w\"; grep -o -i -E \".{0,10}($w).{0,180}\" PHD.txt | head -2; done"
}
```


### [2026-10-17T00:04:43.300Z] TOOL RESULT

```
## wiz.r \[
aker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: th
 quaking. wizar [wc] | M wer] separation; explanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; red
## wizirgar|wiz.rgar
## gum.n \[
ed. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš,
## gum.rdan, 
## gug.y \[
## wir.xtan, 
, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis 
## wist \[
 trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
## wid.rdan, wid
 passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárda
## wiz.dan, 
ective. | wizidan, wizin- [weytn', wcyn- | M weyd, N guzīdan, guzīn-| choose, select, prefer, discriminate. wizihidan, wizīh- [w(y)cyh-ytn'] be separated. „išn(īh): separation; dawn(ing). wizin- , v.
e wéxtan, wizidan, wurróyistan.
## wizend \[|wizand \[
nocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
] choice. wizend [wz(y)nd | M wzynd, N guzand] hurt, harm, injury. wizéngar [wcynkl] chooser; selective. | wizidan, wizin- [weytn', wcyn- | M weyd, N guzīdan, guzīn-| choose, select, prefer, discrim
## gaz.dan, 
poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -
## gum.xtan|gum.zi
 mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund
 améxtan, guméxtan, srištan.
## g.m.z \[
## wiz.r \[wcy
## gazand
```


## [2026-10-17T00:04:48.329Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"wiz[iī]r [\\[(]|wizir \\[|wicir\" \"guman \\[|gumán|gumān\" \"gumardan|gumārdan, |gumárdan\" \"gukay|gugay|gugāy, |gugáy|guk[aā]y\" \"g[oō]m[eē]z\" \"wizirgar|wizir-gar\" \"wēmārīh|wemarih\"; do echo \"## $w\"; grep -o -i -E \".{0,20}($w).{0,160}\" PHD.txt | head -3; done"
}
```


### [2026-10-17T00:04:50.804Z] TOOL RESULT

```
## wiz[iī]r [\[(]|wizir \[|wicir
izin- , v. wizidan. wizir [weyl] decision, judgement. wiziristan, wizir- [wcyl-stn! | J bzyr-, N guzir-) be able to dispense with, avoid. ~iSnig : avoidable. wizistan [westn' | M weyst] t
## guman \[|gumán|gumān
 use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. 
certain a- | abē-gumān, ēwar, tāštīg.
certainty abēgumānih, tāšt.
## gumardan|gumārdan, |gumárdan
commission gumardan.
## gukay|gugay|gugāy, |gugáy|guk[aā]y
 ~ testimony — zür- gugayih; ~ witness zūr-gugāy.
testimony gugayih; false ~ zūr- кирау.
ust gowizar gozénag gugay gugay gugayih gugayih gugan- gokanig gokan doganag gugar- gugārīdan gugārdan dēk gēūgirdūmand gogird даг, рог, gul dol gurbag
## g[oō]m[eē]z
## wizirgar|wizir-gar
## wēmārīh|wemarih
rmad ncm, wem wūmār wēmārīh nēmasp wimand wimandómand wimandig wimustan nemag ncmroz ncmtan niság wisbed
```


## [2026-10-17T00:04:54.279Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==226' NYB_vol2_glossary.txt | head -80"
}
```


### [2026-10-17T00:04:55.108Z] TOOL RESULT

```
ul ~ the flaming up, the shining forth, of the dawn 44!?,
lyaxšitan to grow 40". — Av. (1337 sq.) Iyaxs-, v. also varšišn.
2vaxSitan to flame, to blaze 1%, — Av. (1338) *vaxš- ‘to sparkle’ (of fire), ‘to spurt’ (of water); MPrth was ‘to be kindled, blaze’ (MHC); v. ?vax$, vaxšiš- néh, vaxsénitan.
vaxš-var [whšwl] prophet 1115. — ‘Bearer of the Word, or the (divine) message’, v. lvaxš.
vaxšvarčh prophethood 454-7,
vāyēndak [w'yndk'] flying creature, pl. cas. obl. —-än, enumerated after murvān 802. — Pres. pt. of Av. (1356) Wvay- ‘to fly’.
vizčnitan [w’cynytn'] to bring, to take a p. to a place (andar) 49?’; to lead (a horse) up to (0) a p. 5413-15; à tē pat ulēh ul vāzēnēm we shall carry thee up in the air 60%. — Caus. of väzitan.
vāzēnītār one who draws, pulls: asp i rahy ~ a chariot-horse 581”.
vāzišn v.n. of vāzītan (g. v.), pred. 1211’: dast + vat nē ~ it is necessary not to play the game badly.
vazitan [wcytn'] to travel, to ride: tē... ké vazäh [subju. 2nd p. sg. = ind.] pat vài i dérang-x"atà$ thou ... who ridest on the long-dominating Wind 9914-15, — Av. (1386) vaz-; MPrth. pres. wz- ‘to blow’ of the wind’, ‘to move, to go’ (MHC); Ghilain 52.70, cf Verbum 170; Paz.
Vaz-var
vazidan (Aog.); NP vazidan, bazidan ‘to blow’. V. also vaz-var.
vazitan [w’cytn'] caus. of the preceding v., to move: 1. trans. catrang — to play at chess 11915, 121%, — 2. intrans. to travel, to ride (= vazitan) 519-14. 6019, — Cf MPrth pdw’z ‘suite, followers’, pres. prw’z- ‘to cause to fly’, Ghilain 70; NP bazidan, büxtan ‘to play; to fly’.
vazr [wzl] mace 851%, — Av. (1392) vazra-; Paz. vazr(a); NP gurz; also, with meta- thesis, varz (q. v.).
"| vazurg [LB”, Prth RB’; wewrg, inscr.
welk-] great, big, high, lofty, passim; regularly placed before its head w., seldom: after (41?. 724); in titles great, chief: ~ framatar (g. v.); ~ šahridar (q.v.); — subst., pl. cas. obl. ~-dn the magnates HajA:6 [RB’n]. B:6 [welk’n]. 42. 1133, 16? [wewlg'n'], v. Christensen, Sass. 100. 110sq. — OP vazrka-; MPrthPrs wzrg; Arm. lw. vzurk, vzork, vzruk; Paz. guzurg, guzarg; NP buzurg. No comp. and sup.; for these forms meh, mahist are used; v.s. v. mas.
vazurgakän [LB’-k’n'] pl. cas. obl. of vazurg: (0) Col xakan u ~ to the Khakan of C. and his magnates 11323. — Cf váspuhr : lydspuhrakan (g. v.).
vazurgēh [wewlgyh, LB’-yh] greatness 517.26, size 151.
vazurg-kunišn [LB’ kwnšn'] of great achievements, executor of grand achieve- ments; pl. cas. obl. —-än 1068.
Vazurg-mihr [wewlgmtr'] n. pr. the fa- mous Grand Vizier of Khösröi I (531— 579): 118-121.
vazurg-späs [LB? sp’s] of lofty service, performing high duties, pl. cas. obl. —-än 106!, v. späs.
| vazurg-x"arrah [LB’ GDH] of great glory,
of Yam 44%.
vaz-var [wcwl] safe for traffic: puhl 4 ~ 1147. — V. vazitan,
www.parsianjoman.org | ool wok
vecak
208
vét-varéh
[vēcak [wyck'] lot, share, portion ; combat (as if it were a casting of lots between the combatants): rasnik ~ pitched battle FrP 14; v. nem-vecak. — From !vertan; Arm. lw. vičak ‘lot (e. g. in casting of lots), portion; position; fate, possession, dio- cese’; Ps. wyc ‘priest’, wycyhy �
```


## [2026-10-17T00:04:59.025Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if ($0 ~ /\\n217\\n/) print NR}' NYB_vol2_glossary.txt | head; grep -n -E \"^(vičitan|vičit|vičir|vizir|vičīr|vizārtan|vizirišn|vimār|vēmār|gumān|vimāndan|guman|gumēxtan|gumēc|vi-)\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-10-17T00:04:59.561Z] TOOL RESULT

```
237
1733:guman [gwm'n'] doubt: ~ kartan pat to doubt 1074; ~ bütan pat to be doubtful of 108?. — = NP; MPrs. gwm?n, v. Sogd. 42; Paz. gumq. — V. a-gumān, apē-gumān. gumänöh scepticism, unbelief 1083.
1736:gumēcišn [gwmyešn'] the act of mixing, or the state of being mixed (andar with) 787.14. 899,
4113:vi-ear- [wel-] pres. to get on, to get through, 2nd p. pl. vicarét 41". — Av. (450) vi->kar- ‘to move about’; Skr car- ‘to move’, vi-car- ‘to go apart, to spread’, v. next w.
```


## [2026-10-17T00:05:02.226Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1733,1740p NYB_vol2_glossary.txt; echo ----; awk 'BEGIN{RS=\"\\f\"} NR==237' NYB_vol2_glossary.txt | grep -n -E \"^(vi|wi)\" | head -40"
}
```


### [2026-10-17T00:05:02.889Z] TOOL RESULT

```
guman [gwm'n'] doubt: ~ kartan pat to doubt 1074; ~ bütan pat to be doubtful of 108?. — = NP; MPrs. gwm?n, v. Sogd. 42; Paz. gumq. — V. a-gumān, apē-gumān. gumänöh scepticism, unbelief 1083.
gumärtak [gwm'ltk'] pt. of next w., coll. the staff of Royal commissioners 15. — Another interpretation by Pagliaro, RSO XXIII, 1948, 67.
gumärtan [gwm'Itn'] to entrust a p. with (pat), to commit a th. to a p.’s charge 705. 8714.19, 1155, 1178. — MPrs gwm’rdn gwm’r-, Verbum 193; NP gumaštan gu- mär-.
gumēcišn [gwmyešn'] the act of mixing, or the state of being mixed (andar with) 787.14. 899,
guméxtan [gwmyhtn'] guméc- [gwmyc-], shortened inf. gumext 1041’; pt. = pret. pass. 3d p. sg. gumčat (gumext hat 423-4), pres. pass. 3d p. sg. gumčatet (104!3.%), pl. gumertend 9615. 9813: to mix with:
apäk 971, andar 423, 6 42?5, andar 6 93"*. 10419-20, 116°; hakanén ~ to intermingle, to become blended 431; andar € giyäk gumēztēnd they will crowd together in one place 9615. 9812-13; apāc ~ with a pred. to mix so as to become again 10416-17, apāc 6 . apäc ~ id. 10417-18, — < *vi-maik-, vi-maic-; MPrth wmyxtn; MPrs gumyxtn, pres. intrans. gwmyas-, v.n. gwmyzysn (S), gwmyg ‘mixture’ (A-H II) confirming -k as the final cons. of the root; Paz. gumertan gumēž/z/-, gumežjzjašn. — V. ämecisn, ümek. gund [gnd] troop 8-18, — MPrth gwnd, Arm. lw. gund, Arab. lw. jund; cf Bailey, TPhS 1955, 73 sq.
gung [gwng, gng] dumb 11°. 127. 652°. — = NP. gurbak [gwlbk'] cat 101. — NP gurbah.
gurg [gwlg] wolf 4927, 505-13, 9615-18, 1028, — Av. (1418 sq.) vohrka-; NP gurg.
----
2:viturt [wtwlt'] v. vitartan.
3:viyak [wy’k; Prth ’TRH] place: õi ~ ku on the spot where HajB:8; space HajA:8. B:9. - P2:6 wy’k BYN: read wy’ wyt = u yávet (q. v.).— < *vi-vāha-ka from Av. (1394) ?vah- ‘to stay’, Junker, WuS XII, 1929, 148; elsewhere gyw’k = giyäk (q. v.).
6:viyiftan
11:viyäpänöh seduction, inveiglement 9024, from lvtyāpān.
13:viyapihistan [~-yhstn'] to let oneself be seduced 9074, v. !oiyüpàn.
14:viyiftan [wdyptn'] vihčp- [wyhyp-] to seduce: ke viyift vihepet he who seduces a seduced 82° according to Cod. K; it could also be translated: he who, himself being seduced, seduces (others), cf Arab dalla wa-adalla. The passage deals with the sin of male homosexual intercourse, for which the basic text is Vd. 832: arša- ca vaēpyē arša-ca vačpayo a male who is the passive partner, and a male who is the active partner in the intercourse. The Phl. translations show a remarkable
16:viyiftan
```


## [2026-10-17T00:05:09.464Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {print NR\": \"substr($0,1,0)}' /dev/null; for w in \"^vic[iī]r|^vičir|^vizir|^vičīr\" \"^vic[iī]tan|^vičitan|^vizitan\" \"^vicartan|^vizartan|^vičārtan|^vicārtan|^vizārtan\" \"^vimār|^vēmār|^vemar\" \"^vistartan|^vistāx|^vistax\" \"^vitartan\" \"^virēxtan|^virextan\" \"^vist \" ; do echo \"## $w\"; grep -n -E \"$w\" NYB_vol2_glossary.txt | head -3 | cut -c1-400; done; awk 'BEGIN{RS=\"\\f\"} NR==236 || NR==237 {print \"LEAF \"NR; print substr($0,1,200)}' NYB_vol2_glossary.txt"
}
```


### [2026-10-17T00:05:10.251Z] TOOL RESULT

```
## ^vic[iī]r|^vičir|^vizir|^vičīr
4123:vicīr [weyl] decision: hàn bun pursisn ~ the decision of these fundamental quest- ions 111? (delete the following tzāfat). — From vi-car- (g. v.). The Arm. lw. ver
4125:vicir
## ^vic[iī]tan|^vičitan|^vizitan
## ^vicartan|^vizartan|^vičārtan|^vicārtan|^vizārtan
## ^vimār|^vēmār|^vemar
## ^vistartan|^vistāx|^vistax
4212:vistartan [wstltn'], visturtan [wstwltn'] vistar-, to spread 45% (-urt). 11119 (-artan); pass.: ka-š fratom frasm vistarthét when its (viz. the sun’s) first dawn is spread, shines forth 4418, — < vt-+star-, v. start; NP gustardan, -ridan; Verbum 206.
4216:vistax4iha confidently, fearlessly 16°.
## ^vitartan
4235:vitartan
4240:vitartan [wtltn'], viturtan [wtwltn'], vi- taštan [wtštn'], vitir- [wtyl-] to pass: andar dašt bē vitart passed over the plain 318; pat kustak + deh vitart passed outside the village 619-17; to pass by 7!1.15.22; bē vitast drove ahead 71’; to cross a bridge 7225.27; to go through a stream 101%. 10323; kë vitīrēndv the passers-by 12815; — pt. vitart, viturt deceased: vitart coll. the deceased 
4244:vitartan
## ^virēxtan|^virextan
## ^vist 
4217:vist [figure] twenty, ordinal vistom [wys- twm; 20-wm] the twentieth.
LEAF 236
štāsp; as to the etymology ci Bailey, JRAS 1953, 101-103.
Vištāspān patr. of the preceding n. pr. 21-30 passim. 95!4. 11321,
višuftan [wšwptn'] višop- to ruffle (a p.s hair) 2627; to derange, to disso
LEAF 237
 [wtyst'] a linear measure, a span = 12 finger-breadth 93°. — Av. (1440) vitasti-
viturt [wtwlt'] v. vitartan.
viyak [wy’k; Prth ’TRH] place: õi ~ ku on the spot where HajB:8; space HajA:8. B:9. - P2:
```


## [2026-10-17T00:05:18.323Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4123,4127p NYB_vol2_glossary.txt | cut -c1-600; awk 'BEGIN{RS=\"\\f\"} NR==237 || NR==238' NYB_vol2_glossary.txt | grep -n -E \"^(viz|vič|vic|vim|vij|vīž|vizend|vizand|2[01][0-9]$)\" | head"
}
```


### [2026-10-17T00:05:18.802Z] TOOL RESULT

```
vicīr [weyl] decision: hàn bun pursisn ~ the decision of these fundamental quest- ions 111? (delete the following tzāfat). — From vi-car- (g. v.). The Arm. lw. ver
www .parsianjoman.org | ool wok
vicir
211
vihčžak
5:217
25:218
29:vizand [wznd] injury, damage 214. 1174. 3713 ete. — MPrthPrs wzynd, NP guzand. vizand-kar [-kl] causing injury, destruc- tion, destroyer 11013-14,
30:vizand-kar [-k’]] whose work is injury, harmful (pat) 144.
```


## [2026-10-17T00:05:29.135Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==238' NYB_vol2_glossary.txt | head -60 | cut -c1-500"
}
```


### [2026-10-17T00:05:29.639Z] TOOL RESULT

```
bum 173. 198; Ps. wydyptk’n "those who have gone astray’. BP wdypt >
xäk [h'k] dust 1123, = NP.
xakan [h’k’n'] the Turkish title of the King 17°. 11323, 1151-24, - V, Barthold in EI s. v. Khäkän.
xünak [h’nk'; BYT^] house 92%. 101, 205 (ideogr.). 3671. 44?3, 5320.25, 10915. — NP ranah.
xanditan [hndytn'; YHDHWN-tn'] to laugh 1513, 162? (ideogr.). 4715-22, 5115-16, — MPrth znd?dn (S); NP zandidan.
xar [HMR] donkey 2415. 303. — Av. (532) zara-; NP zar.
xüyak [h'dk'] egg 863-7. 922, — Av. aya- < *dya- Yt. 13?, v. Henning, Weller Vol. 1954, 291; NP zäyah (now ‘testicle’).
218
xirs
viyift or vihift, abstr. vihifiakéh ‘sodomy’ BdA p. 2078, pres. *vidēp- > viyép- > vihep- with the alternation of intervocalic -y-: -h-. This vb. has a so well defined Ablaut-series and ends so clearly in -p that it cannot be combined with Av. (670 sq.) !dab- ‘to deceive’ (against Ver- bum, l. e.). — Anklesaria's second MS has wdyptk w wyhypynytk = viyiftak u vihe- penitak = Paz. vehéfta u vehevnida, thus with two coordinated predicates (against Cod. K) as the Av. text has it, but not with the A
Vizak [Paz.] one of Zartuxšt's ancestors 473,
vizand [wznd] injury, damage 214. 1174. 3713 ete. — MPrthPrs wzynd, NP guzand. vizand-kar [-kl] causing injury, destruc- tion, destroyer 11013-14,
vizand-kar [-k’]] whose work is injury, harmful (pat) 144.
Vizarš [wyzlš] a dev, who pulls the soul of the wicked to Hell after his death 7421.24 752, — Av. (1471) Vizarasa- Vd. 1926,
| xäyak-dös [-dys] egg-shaped 862-3. — V.
S. v. des.
xem [hym] nature, disposition, temper 9018.19.23. v. also vat-xēm. — Cf Av. (1781) haya-, hya- ‘peculiarity’; hence Olr *haiman- or the like. Paz. NP xim.
Xion [hywn'] Turkish peoples in Central Asia and East Iran, pl. cas. obl. ~-dn, 18-30 passim. 613-22. — Av. (1858) hyao- na-; Paz. hayün Skr. v. turuska-samüha (Aog.); cf NP hayün a dromedary used by express messengers; Chin Hiung-nu = Huns.
*xirs [hls] "a ring, or the like: 20%. — Both reading and meaning are guite un- certain. Arab has virs-, xurg- ‘a ring
www.parsianjoman.org | ool wok
. xirs
running round the lowest part of the lanee', also other sorts of rings, or 'coat of mail’, which is possibly a lw.; but this is à mere guess.
Xösröi [hwslwd; hwslwd' 110!5 M, but hwslwd Cod. K 43b] n. pr. A. the 3d king of the Kayanian dynasty, mostly known as Kai-Xösröi [kdhwslwd, -Iwd'] 7133. 1138-17; with the patron. Siydvaxsan 116’; eschatological hero 887°. 99—100 passim. 1065; — ~ i Kavätän, founder of five cities 114? sqq., is probably the old Kayanian king of the heroic saga. — B. the Sassanid kings from Bahram I (273— 276) onwards assumed the title ka? (g.v.) and regarded themselves as Kayanians: Kai-Kavät (488—531), his son
```


## [2026-10-17T00:05:34.045Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"to choose\\|guzidan\\|guzīdan\" NYB_vol2_glossary.txt | head; grep -n -i \"vimār\\|vēmār\\|bēmār\\|bimār\" NYB_vol2_glossary.txt | head -3"
}
```


### [2026-10-17T00:05:34.616Z] TOOL RESULT

```
1149:citan [cytn'] cin-, to gather: 1. to put inlay- ers HajB : 12 (pt. cit" = pret. pass. 3d p. sg.). 10 (cit HWH. = hé cond.). - 2. apar ~ to pluck off, to remove (NP bar-cidan) 12019-20 (3d p. pl. eynnd = cinend). — MPrth pt. cyd, pres. cyn- ‘to collect, to fish ; to choose’ (S, A-H III); MPrs cyydn cyn- ‘to gather, to put in layers’ (A-H II); Paz. NP cidan cin-. Av. (441) kay- ‘to choose, to select’; cf Skr cinoti 1. to put together, in layers’, 2. ‘to discern, to search’. — V. also citak and vicitan.
2182:Kämak-süt [~-swt'] n. pr. one of the seven heroes who will usher in the fraš- kart (g. v.) 1069-14, — Av. (1431) Vouru.- savak- Yt. 13128; in Phl vouru- *wide(ly spread)’ was mistakenly combined with (1360) žvar- ‘to choose’, hence the ren- dering by kämak. i
3977:virom [w’lwm] mind, conscience 9425. — From Av. (1360) ?var- ‘to choose’; Bthl (zAirWb 222) identified it with Av. (1411) vāroma = vüàrom či ‘according to one’s wishes; arbitrarily’; Bailey, ZP 103 n. 1, derives it from *värma- from the same ?var-. Darmesteter had found the NP gl. dil for it (ad Y. 1014).
4131:vieitan vicin-, to separate = to pull off 294; to distinguish 63; *dö-cin [dwen ?] nē vicinend they do not even distinguish between the two 103°[? cf Av. (595) cina- and (762) dva-; cf PY 30%%?]; to choose 698. 11215 (hac from). — Av. (441) vi-kay-; MPrth wjyd (pt.), wjydg, weydg ‘chosen’ ; MPrs weydn wzy- (! A-H II); Paz. vajidan vajin- or vazidan vazin; NP guzidan guzin- Arm. lw. včit ‘clear, limpid’. Verbum 181-182; Ghilain 85.
7192:guzīdan, guzīn-: vicītan
```


## [2026-10-17T00:05:37.510Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==106' HUB.txt | head -90"
}
```


### [2026-10-17T00:05:38.020Z] TOOL RESULT

```
— 95 —
ksl. glava 'Kopf ', arm. glux 'Kopf etc. Zu merdle vgl.
Vullers, Grammatica linguae persicae p. 235, wo die
Formen auf le als Formen des Tat-Dialectes bezeichnet
sind. Darauf verweist auch Mann, ZDMG. 47, 705.
931. Np. gumaStan = pfiz. gumdrdan = phi. gumdrtan
'einsetzen, bestimmen, beauftragen, betrauen' Min. Gl.
93, Bdh. Gl. 225, afgh. gumdrql to consign*, arm.
LW. gumar-el 1) sammeln*, 2) 'schicken, iibergeben,
einsetzen* zeigt nirgends den Anlaut t?- und hat jeden-
falls mit ap. *m-inar = skr. vi-smar nichts zu thun.
932. Np. guman = ap. ^mmOna^ (statt zd. *vfmanah'),
Vgl. unten Nr. 965.
934. Vgl. KZ. 33, 165. Dazu nun auch afgh. yand^ql *Ekel
empfinden, nicht leiden, nicht mOgen' (Geiger). Afgh.
ganda 'stinkend' finde ich nicht bei Raverty.
935. Skr. gddhUma^ wird volksetymologische Anlehnung
von ^gandhUma- an die Composita mit gd- *Kuh* sein
{go-dhuma- gleichsam *Kuhrauch'; vgl. unsern Pflanzen-
namen Erdrauch, gr. xanvog^ mnvioc).
936. Dazu arm. LW. gund 'Kugel', gndak *Kugel, Ball,
KnoUen'. Ich halte die Etymologic fiir richtig.
937. Hochst unsicher.
938. Unsicher.
Hierher nach Fr. Miiller, WZKM. 8, 189 guvdrtdan ver-
dauen' = phi. gukar-Uan zu skr. vi-kar umwandeln .
940. Arm. vkay gehdrt nicht zu np. guvdh, vgl. meine
Abhandlung *Arisches und Armenisches*, Idg. Forsch. 4,
p. 119.
941. Ich fasse gosdla *Kalb* als Compos, von go- = np.
gav, gav *Kuh' und sdla *Jahrling (von sal *Jahr ab-
geleitet wie in den Zusammensetzungen mit Zahl-
wortern -sdla = jahrig' ist), also = 'Kuh-jahrling,
vgl. unser 'Jahrlingskalb'. Kurd. LW. gilsile ZDMG.
38, 85.
^4. Np. gost 'Fleisch' = ap. *gausta-?
946. Arm. goin ist Lehnwort, aber aus anderen Griinden.
Ebenso arm. gunak =n np. guna* Afgh. yuna f. 'Haare
[
```


## [2026-10-17T00:05:45.535Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"gumār|gumar\" \"guzārdan|guzar\" \"gusistan|gusastan|gus[iī]xtan\" \"gušādan|gusadan|gusādan\" \"gurēxtan|gurextan\" \"guzīdan|guzidan\" \"gazīdan|gazidan\" \"gumēxtan|gumextan|gumexta\" \"gustardan\" \"wirāstan|virāstan|wirāy\" \"guza.tan|guðaštan|guδaštan|guδar\"; do echo \"## $w\"; grep -n -o -i -E \".{0,200}($w).{0,200}\" CHEUNG.txt | head -3; done 2>&1 | cut -c1-500"
}
```


### [2026-10-17T00:06:16.271Z] TOOL RESULT

```
## gumār|gumar
ugrep: error: error at position 106
)r|gumar)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                 exceeds complexity limits___/


## guzārdan|guzar
ugrep: error: error at position 109
)rdan|guzar)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                    exceeds complexity limits___/


## gusistan|gusastan|gus[iī]xtan
ugrep: error: error at position 128
80-\xbf][\x80-\xbf]*){0,200}
                            \___exceeds complexity limits


## gušādan|gusadan|gusādan
ugrep: error: error at position 140
an)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
           exceeds complexity limits___/


## gurēxtan|gurextan
ugrep: error: error at position 112
)xtan|gurextan)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                       exceeds complexity limits___/


## guzīdan|guzidan
ugrep: error: error at position 110
)dan|guzidan)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                     exceeds complexity limits___/


## gazīdan|gazidan
ugrep: error: error at position 110
)dan|gazidan)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                     exceeds complexity limits___/


## gumēxtan|gumextan|gumexta
ugrep: error: error at position 120
[\x80-\xbf]*){0,200}
                    \___exceeds complexity limits


## gustardan
ugrep: error: error at position 90
\x80-\xbf][\x80-\xbf]*){0,200}
 exceeds complexity limits___/


## wirāstan|virāstan|wirāy
ugrep: error: error at position 146
:ā|Ā)y)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
               exceeds complexity limits___/


## guza.tan|guðaštan|guδaštan|guδar
ugrep: error: error at position 212
\n\x80-\xbf][\x80-\xbf]*){0,200}
   exceeds complexity limits___/
```


## [2026-10-17T00:06:22.664Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('CHEUNG.txt').read()\npats={'gumar':r'gum[āa]r','guzar':r'guz[āa]r','gusist':r'gus[ia]st|gus[iī]xt','gusad':r'guš[āa]d|gusād','gurex':r'gur[ēe]xt','guzid':r'guz[īi]dan','gazid':r'gaz[īi]dan','gumex':r'gum[ēe]xt','gustard':r'gust[ae]rdan','wiras':r'wir[āa]st|v[iī]r[āa]stan','guzast':r'gu[zδð]a[sš]tan'}\nfor k,p in pats.items():\n    ms=list(re.finditer(p,t,re.I))\n    print('##',k,len(ms))\n    for m in ms[:2]:\n        print('  ',re.sub(r'\\s+',' ',t[max(0,m.start()-300):m.end()+150]))\nEOF"
}
```


### [2026-10-17T00:06:23.531Z] TOOL RESULT

```
## gumar 6
   v. morongoidiiai (Y 46.11); Desid.: SUBJ. 3sg. med. mimaroxsäite (V 15.14), IMPV. 25р. med. YAv. mimaraxSar‘ha (V 15.14) *MIDDLE PERSIAN: BMP mwincyn- /murnjén-/ (caus.) ‘to destroy’, MMP mwrz(hy)- (sec. pass.) ‘to be harmed; to be persecuted’ || (+ *ui-) MMP wymrz- ‘to destroy’, ВМР gwmlc'k /gumarzag/ ‘the pernicious’ (Gershevitch 1977: 66) = DMMPP: 234b, 354a Caus.: pres. IND. 1sg. BMP mwlncynym /murnjéném/, 3р1. ВМР mwincynynd /murnjénén
   ba 1997: 312 f.; Cabolov 2001: 644; Lecoq 2002: 128, 130, 133, 135 (passim); Kiefer 2003: 201 *marH ‘to block, hinder *MIDDLE PERSIAN: (+ *ui-) MMP gwm’r- ‘to appoint’, ВМР gwm'l- /gumär-/ ‘to appoint, entrust, commission’? > DMMPP: 167a Pres.: IND. 3sg. MMP "gwm'ryd, IMPV. 2sg. BMP gwm’! /gumar/; Partic.: perf. pass. MMP gwm’rd, BMP gwm’Itk /gumardag/; Inf.: BMP gwm’Itn /gumardan/ *NWIR: (+ *ui-) NP gumästan/gumär- ‘to put someone to wor
## guzar 5
    čērīn/čēr-, Zaz. Cérayis/ ceren-, Tal. čarde, Abz. Cerowa/cer-, Khuns. ёіг-, Ham. čärayän/čär-, Siv. čar- ‘to pasture’, NP Caränidan/Carän-, Meim. bem-tfernä/a-tfern-, Qohr. cerna/ cern-, Tr. cernä/Cern- (caus.) ‘to graze’, Zaz. Carnayis/Carnen- ‘to lead around, let walk around’ || (+ *ui-) NP guzardan/guzar- ‘to accomplish [work, job, etc.], perform [e.g. prayer]; to pay; to explain, interpret’, Kurd. (Kurm.) bzartin/bzér-, (Sor.) bzardin/bZér-
   r-, Zaz. Cérayis/ ceren-, Tal. čarde, Abz. Cerowa/cer-, Khuns. ёіг-, Ham. čärayän/čär-, Siv. čar- ‘to pasture’, NP Caränidan/Carän-, Meim. bem-tfernä/a-tfern-, Qohr. cerna/ cern-, Tr. cernä/Cern- (caus.) ‘to graze’, Zaz. Carnayis/Carnen- ‘to lead around, let walk around’ || (+ *ui-) NP guzardan/guzar- ‘to accomplish [work, job, etc.], perform [e.g. prayer]; to pay; to explain, interpret’, Kurd. (Kurm.) bzartin/bzér-, (Sor.) bzardin/bZér- ‘to sel
## gusist 4
   ) Fut.: IND. 3sg. CSogd. psydtyq’ *BACTRIAN: (+ *apa-) oBouo- (pret. stem) ‘to finish, conclude, bring to an end’ c» S-W, Bact.: 176b *NWIR: Bal. sist/sid-, sind- ‘to break, split (cords, sim.)’ || (+ *apa-) Gz. fisisse ‘torn out, spread out’, Tr. fésés- (pret. stem) ‘to break’ || (+ *ui-) NP gusistan (supplet. gusil-) ‘to shatter, break’. 9 The initial fi- of Gz. fisisse is hardly from *ui-, cf. NP gusistan/gusil- (!) ‘to break off’, pace Eile
   end’ c» S-W, Bact.: 176b *NWIR: Bal. sist/sid-, sind- ‘to break, split (cords, sim.)’ || (+ *apa-) Gz. fisisse ‘torn out, spread out’, Tr. fésés- (pret. stem) ‘to break’ || (+ *ui-) NP gusistan (supplet. gusil-) ‘to shatter, break’. 9 The initial fi- of Gz. fisisse is hardly from *ui-, cf. NP gusistan/gusil- (!) ‘to break off’, pace Eilers, WIM П/2, l.c. *NEIR: Pash. slédal ‘to break’ || (+ *fra-) Ishk. fersend-/fersest- ‘to be torn apart’, Wa
## gusad 0
## gurex 1
   421 girami, 107 giramidan/giram-, 107 giriftan/gir-, 120 girih, 123 giristan/girty-, 112, 122 gos, 116 gosidan/gos-, 116 g0z, 117 gudaxtan/gudaz-, 376 guóastan/guóar-, 381-2 guftan/goy-, 113 gum, 258 guman, 263 gumästan/gumär-, 268 gunah, 283 gunj, 434 gunjidan/gunj-, 434 gurextan/gurez-, 307 gusil-, 338 gusistan, 327 gusi (guse ?), 327 gustardan/gustar-, 365 gusädan/gusäy-, 136 gusnah, 423 *eusuftan, 455 guvah, gav
## guzid 2
   ye/Cin-, Natan. čiä, Qohr. cida/cin-, Tr. Ciya/sn-, Varz. Cinde/éin- ‘to reap, gather’, Semn. -cinc- ‘to gather, pluck’ || (+ *pari-) NP parcidan/parcin- ‘to beat down the point of a driven nail so as to fix it; to rout’, Gur. (Kand.) párcin 'thorn-hedge', Bakht. parzin ‘bramble’ || (+ *ui-) NP guzidan/guzin-, Bal. gicint/gicin- ‘to choose, select, elect’ *NEIR: Sh. ci(y)-/cid, Rosh. cay-/cid, Bart. ciy-/cid, Sarig. cey-/cid ‘to reap, harvest’, Yg
   81-2 guftan/goy-, 113 gum, 258 guman, 263 gumästan/gumär-, 268 gunah, 283 gunj, 434 gunjidan/gunj-, 434 gurextan/gurez-, 307 gusil-, 338 gusistan, 327 gusi (guse ?), 327 gustardan/gustar-, 365 gusädan/gusäy-, 136 gusnah, 423 *eusuftan, 455 guvah, gavah, 404 guzärdan/guzär-, 34 guzidan/guzin, 27 garmidan, 122 gaStah, 110 gunav-/gunüdan, 119 gurunbidan, 122 hamär, 138 hamyan, 211 handasi, 64 hazinah, 156 hävan, 134 hém
## gazid 2
   lov 2001: 409 f.; NEVP: 8 *gaz ? ‘to bite, sting’ *MIDDLE PERSIAN: BMP gc- /gaz-/ ‘to sting’ (LW) Pres.: IND. 3sg. BMP асу! /gazéd/, SUBJ. 3sg. BMP gc't/gazad/; Partic.: perf. pass. BMP gcyt /gazid/ *PARTHIAN: “gst (pret. stem) ‘to bite” = Ghilain: 96 | DMMPP: 170b 118 *gaz *NWIR: NP gazidan, Kurd. gastin, gazin/gaz-, Nn. gisa/giz-, Siv. gäz-/gäze ‘to bite; sting’, Bal. gassit, gast/gass- (inch.) ‘to bite, sting, wear out’, NP -gaz ‘biti
   an/fisär-, afsurdan/afsär-, 93 furög, 316 furöxtan/furöz-, 316 gahülidan, 131 gand, 104 gandah, 104 gap, gab, 401 gardanidan/gardan-, 111 gardidan, 111 gardün, 425 garzah, 106 garzin, 108 gas, 471 gastan/gard-, 111 gauharidan, 131 -gaz, 118 gazand, 225 gaza, 118 gazidan, 118 gadan, gayidan/gay-, 94 538 gam, 100 вёў, 97 gévah, 96 gilah, 112 gimiz, 179 gimizidan/gimiz-, 179 giravidan, 421 girami, 10
## gumex 0
## gustard 2
    *SOGDIAN: (+ *pari-) BSogd. prstr- ‘to spread’, BSogd. prstrn ‘rug’ Inf.: pret. BSogd. prstrty *CHORESMIAN: (+ *upa-) bstn- ‘to make flat, spread (evenly) = Samadi: 27 *NWIR: (+ *abi- ?) NP bistar, Khuns. bistär ‘bed, mattress’ || (+ *upa- or *pari- ?) Bal. pastark ‘saddle’ || (+ *ui-) NP gustardan/gustar- ‘to spread’ *NEIR: Oss. I. steryn/sterd, D. (&)ster(n)un/&)stard ‘to spread out; to cover; to pave; to adorn’ || (+ *a-) Oss. I. astaeryn/
   23 giristan/girty-, 112, 122 gos, 116 gosidan/gos-, 116 g0z, 117 gudaxtan/gudaz-, 376 guóastan/guóar-, 381-2 guftan/goy-, 113 gum, 258 guman, 263 gumästan/gumär-, 268 gunah, 283 gunj, 434 gunjidan/gunj-, 434 gurextan/gurez-, 307 gusil-, 338 gusistan, 327 gusi (guse ?), 327 gustardan/gustar-, 365 gusädan/gusäy-, 136 gusnah, 423 *eusuftan, 455 guvah, gavah, 404 guzärdan/guzär-, 34 guzidan/guzin, 27 garmidan, 122 gaStah, 110
## wiras 1
    Sitáy/Sor-, 455 socnáy/soén-, 339 sotáy/soc-, 339 tarsáy/tars-, 393 tažná, 383 tasay/tas-, 385 INDICES [Gurani] taway/taw-, 387 tawiay/tawia-, 375 wanay/-wan-, 145 waray/waro, 406 wardáy/(-)war-, 148 wastay/waz-, 460 watay/wac-, 403 wetáy/wec-, 408 wiardáy/wiar-, 381 win-, 413 wirastay/wiraz-, 198 wistay/wiz-, 142 witáy/-us-, 146 wuratáy/wuras-, 429 wuriay/wuria-, 150 wurnay/wurn-, 150 xızäy/-xız-, 445 zanay/-zan-, 467 zäy
## guzast 0
```


## [2026-10-17T00:06:37.122Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('CHEUNG.txt').read()\npats={'gazand':r'NP gazand','guvah':r'NP guv[āa]h','gurextan':r'NP gur[ēe]xtan','gusadan':r'NP gu[sš][āä]dan','guman':r'NP gum[āa]n','guðaštan':r'NP gu[δóð]a[sš]tan','gimiz':r'NP gim[īi]z|gōmēz|gumēz|gumez','bist':r'NP b[īi]st\\b','bimar':r'b[īi]m[āa]r|w[ēe]m[āa]r','wirast':r'NP v[īi]r[āa]stan|wir[āa]stan|wyr.st'}\nfor k,p in pats.items():\n    ms=list(re.finditer(p,t,re.I))\n    print('##',k,len(ms))\n    for m in ms[:2]:\n        print('  ',re.sub(r'\\s+',' ',t[max(0,m.start()-500):m.end()+200]))\nEOF"
}
```


### [2026-10-17T00:06:38.270Z] TOOL RESULT

```
## gazand 1
    Jäj/jän- ‘to play (a string instrument), Fariz. -gan-/-gan- (denomin. ?), Yar. gon-/gon- (denomin. ?), Ard. jiye/ jin-, Gil. (Rsht.) zecen/zaen-, Ham. jiyän/jon-, Khuns. zin-, Anar., Lasg. -jas/-joen-, Nn. zeye/zin-, Qohr. jida/jin-, Sang. -Ze&Zenan-, Shamerz. -zi(n)-/-zänäm-, Soi zat, Sorkh. -jahan/-jan-, Varz. jinde/jin- ‘to hit, strike’, Gur. (Kand.) -Zinyan- (pass.) /-Zan- ‘to close the door’ || (+ *а-) Delij. адепт ‘to strike, beat (on the ground)’ (Safari 1373: 68, 229) || (+ *ui-) NP gazand ‘damage, injury’ *NEIR: Pash. -Zan-/-Zal ‘to chop, mince’, Oss. I. дап, D. бапа ‘wound, fracture; shortcoming; [also D.] guilt, transgression’, (NP >) Sh. zin-/zıd, Khf. zaen-/zöd, Rosh. zan-/zod
## guvah 1
   002: 176, 179 (passim); Kiefer 2003: 198; Shahbakhsh: s.v. gwas-, gwanjan-; Kom 2005: 137, 317, 398 *uadH ‘to slay’ *AVESTAN: ? OAv. vad- ‘to break through, hunt’, YAv. vada- (m.) ‘wedge’ (V 14.7), vadar- (n.) ‘murder weapon’ (Y 32.10, Y 9.30). % The (hapax) verbal form seems to be a denomin. (or caus. ?) form, which corresponds to Skt. vadhá-, Gr. ФӨёо. = Liste: 53 Pres. aja-: ОРТ. 3sg. OAv. vadaiidit (29.2) *KHOTANESE: OKh. bädära- ‘a weapon’ (Z 4.60, Z 24.280, Z 24.417) *NWIR: NP guvah, gavah, Gz. guve ‘wedge’ *NEIR: Sariq. wed, Wa. waó ‘handle (of axe, etc.)’ *SANSKRIT: vadh ‘to slay, to kill’ (RV+) = EWAia II: 496 *yah2 405 «PIE *ued'H,- ‘to strike’ > LIV: 660 | Pok.: 1
## gurextan 0
## gusadan 0
## guman 1
    CSogd. ’wm’ncn ‘doubtful’ Pres.: IND. 15р. SSogd. myn’m, 3sg. BSogd. туш, 3pl. CSogd. mynnt, OPT. 3sg. BSogd. myn’y; ’z-Impf.: IND. 3pl. CSogd. myn’znt *CHORESMIAN: m’ny- ‘to suspect, regard’ || (+ *a-) m/’m’nsy- (pass.) ‘to be led’, m['m'ny- (caus.) ‘to lead’ || (+ *uz-) ? "zmny- ‘to care for someone ?, grant someone's wish ?' || (+ *fra-) Smny- ‘to be arrogant, (?) opinionated’ = Samadi: 111, 5, 263 f., 196 *NWIR: Qohr. münoya/mün- ‘to believe’, man ‘mind, character’ || (+ *ui-) NP guman ‘doubt; belief, opinion’, Qohr. gemun ‘opinion, belief (< МР?) *NEIR: Oss. I. mat, D. mætæ ‘anxiety, restlessness’ || (+ *a-) Oss. I. amonyn/amynd, D. amonun/amund ‘to admonish’ *SANSKRIT: man 
## guðaštan 0
## gimiz 3
   pass. BMP myst /mist/ *PARTHIAN: (+ *ni-) nmyzysn ‘incitement, provocation, urging? > DMMPP: 244a *KHOTANESE: miysai ‘urine’ *CHORESMIAN: myz- ‘to urinate, piss’ = Samadi: 113 f. *NWIR: NP méxtan/méz-, Bal. mest, mezit/meZ-, méz-, Kurd. mistin/miz-, Gil. dimistan/dimiz- ‘to urinate’, Ard. mis/mes-, Gz. méz-/més, miss (tr.), Khuns. miz-/ mizä, mis(s)-, Lasg. demeston/demiz-, Nn. més/méz-, Semn. demestiyon/damiz-, Sorkh. demestan/demiz- ‘to defecate’, Zaz. mizi (f.) ‘urine’ || (+ *ui-) NP gimizidan/ gimiz- ‘to make water’, NP gimiz, (LW ?) Awrom. guméz (m.) ‘urine’ *NEIR: Oss. I. mizyn/myzt, D. mezun/mizt ‘to flow; to urinate’, Pash. mitol/mez-, Sh. mez-/mixt, Rosh. miz-/mixt, Sariq. me
   *ni-) nmyzysn ‘incitement, provocation, urging? > DMMPP: 244a *KHOTANESE: miysai ‘urine’ *CHORESMIAN: myz- ‘to urinate, piss’ = Samadi: 113 f. *NWIR: NP méxtan/méz-, Bal. mest, mezit/meZ-, méz-, Kurd. mistin/miz-, Gil. dimistan/dimiz- ‘to urinate’, Ard. mis/mes-, Gz. méz-/més, miss (tr.), Khuns. miz-/ mizä, mis(s)-, Lasg. demeston/demiz-, Nn. més/méz-, Semn. demestiyon/damiz-, Sorkh. demestan/demiz- ‘to defecate’, Zaz. mizi (f.) ‘urine’ || (+ *ui-) NP gimizidan/ gimiz- ‘to make water’, NP gimiz, (LW ?) Awrom. guméz (m.) ‘urine’ *NEIR: Oss. I. mizyn/myzt, D. mezun/mizt ‘to flow; to urinate’, Pash. mitol/mez-, Sh. mez-/mixt, Rosh. miz-/mixt, Sariq. meyz-/maxt, Yzgh. miz-/maxt, M. méz-/mizd
## bist 0
## bimar 0
## wirast 3
    353b, 48a (+ *ui-) Pres.: SUBJ. 2sg. wygr’s’, IMPV. 2sg. wygr’s, 2pl. wygr’syd, 2pl. wygr’syd; Partic.: perf. pass. wygr’d(g), Caus.: pres. IND. 3sg. wygr’nyd *SOGDIAN: BSogd. y’r ‘to watch, guard’ || (+ *ui-) SSogd. wyr’s, BSogd. wyy’r’s, CSogd. wyr’s (intr./inch.) ‘to wake’, CSogd. wyrys, Sogd. wyr’ys (caus.-inch.) ‘to wake up, arouse’ Pres.: IND. 3pl. BSogd. y’r’nt || (+ *ui-) Well attested: Pres.: SUBJ. 3sg. BSogd. wyy’r’s’, IMPV. 2sg. SSogd. wyr’s (Sogd. Tales: 478), 2р1. CSogd. wyr’stt, Pret.: IND. 3pl. intr. MSogd. wyyr’tnd, etc. *CHORESMIAN: y'r- ‘to protect, guard’, m/yr’s- (inch.) ‘to be awake, awake’ c» Samadi: 75, 78 f. *NWIR: Bal. gurit/gur- ‘to wake up with a start’ 
    put in order, arrange, array’, wyn’r’g ‘arranger’ (< MP) = Ghilain: 69 f., 52, 70, 75 | DMMPP: 293a, 270b, 356b, 344a, 354b f. (+ *pati-) Pres.: IND. 3sg. pdrzyd, 3pl. pdrzynd; Partic.: perf. pass. pdr’st, caus. H pdr’z’d; Caus.: pres. IND. 3sg. pdr’zyd, 3pl. pdr’zynd, SUBJ. 2sg. pdr’z’h || (MP LW ?) Pres.: IND. 3pl. pdr’ynd; Partic.: perf. pass. pdr’st, П pdr’y’d || (+ *ui-) Pres.: IND. 35р. “wyr’zyd, 3р1. *wyr’zynd, SUBJ. *wyr’z’, IMPV. 2pl. wyr’zyd; Partic.: pres. wyr’z’n, perf. pass. wyr'st; Inf.: *wyr'stn || Pres.: IND. 3pl. wyn’rynd, SUBJ. 2sg. wyn’r’h, 3р1. wnyr'nd; Partic.: perf. pass. "wyn’r’d *KHOTANESE: Khot. rras- (denomin. ?) ‘to rule’ || (+ *aua-) varas- (varas-) ‘to exper
```


## [2026-10-17T00:06:50.200Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"^v[iī]č[iī]ra|^vlč[iī]ra|^vicira|^vīčira|vīčira\" \"^vimanah|v[iī]manah\" \"^v[iī]saiti|vlsaiti\" \"^v[iī]-\" \"^vīspa\" ; do echo \"## $w\"; grep -n -E \"$w\" BRT.txt | head -5 | cut -c1-200; done"
}
```


## [2026-10-17T00:06:50.999Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1809 2>&1 | tail -40"
}
```


### [2026-10-17T00:06:51.616Z] TOOL RESULT

```
## ^v[iī]č[iī]ra|^vlč[iī]ra|^vicira|^vīčira|vīčira
## ^vimanah|v[iī]manah
## ^v[iī]saiti|vlsaiti
22154:nehmen':  vJsmU  aval  vlssnta^a  *mazyasat . .  fravaiayS  "sie  stellen  sich  dazu,  sie stellen  sich  auch  zu  noch  grösserem  be- reit . ."  YLiy.73;  —  at»m  aita  zaota  vUäi staotanq
28907:•  j-  (1  g-t  P)  haxay- :  Ariy-,  Aai'-^^,  m. i)  'Freund,  Genosse':  ^m  °xa  (NS.)  '1/ (DS.)  *baraiti  Y.  6'2.  8;  —  aa£  aosOe  'xa •sa  (IS.)  V.  18.  a6;  F.  24;  —  yaS:a  . 
30467:•  j.  huyä)Tia-  Adj,  'das  Lager  teilend, Lager-,  Stubengenosse';  vlsaitivä  asti miirS  aniar»  ha!a  suptioarynga  (sd.)  .  , pama.sa%wa  autark  'na  (AD.)  \t  10.116.
## ^v[iī]-
## ^vīspa
```


### [2026-10-17T00:06:51.750Z] TOOL RESULT

```
بربان پلاوجاییر! گوبند که‌محاذی کردن گوسفند گوبند ‎..٩‏
‏ن باشد #۰
بربان باشد از.۲ گریوه ۷ - بفتح اول و رابع » کوه
گریواده < با ثالك مجهول و واد | پت و پشتهٌ بلند را کوبند - و یکسر اول هم
و زای هوز بروزن دلیرانه » بمعنی هار است که | آمدهء است ۸ - و زمین بلند وپشتةٌ خا کیرالیز
مروارید ولمل وامثال آن باشد که بررشته کشیده | کوبند که باران آنرا رخنه کرده بزیر آهده
باشند . باشد. ۶

(۷) چش : باشد -

۱-اظ . مسحف « کریختن » با «کریفتن > ر4 :کریشتن ‎ .‏ .

۲ - رك :کری . ۴ - محیح برای مهمله است » مرک از: کری( کردن) +
واره (پوند نبت واتصاف) [رك .۰ رشیدی] با از :گربو (کردن )۳ واره (پسوند) با حذف يك
واو « فرهنگه نظام > جمماً یمنی لابق کردن (قس : کوشواره ) « رشیدی > :"

ز بژم مخنقةٌ یافت شاخ کل منظوم چو باد کرد کربواره شجر منثور .

انیراخیکتی ۸« رشیدی .

۴ -ظ . برساختهٌ فرقهٌ آذرکیوان . 8 - رك : پریون .

۹ - رد : رشیدی . - پپلوی رد (کردن ۰ پشت کردن). اوستا 871۷2
۶ بارتولمه ۰ نیب رگه ص ۸4 . رك دص ۱۸*۵ حخ۹ ۰

۸ - دیده‌اند از پی گربوة غیب رب خود را پبدیدغ لارب .

اوحدی « فرهنگه نظام > .

گربواره - رك : گریوازه .

گریه - بکسر اول » اسم مصدر از «کرستن > (۸.م.) ؛ اشك ربختن ,کرستن :
- اغك , سرشغك .

از پی هر کربه آخر خنده‌ایست مرد آخر بین مبارك بنده ایست .

«مولوی بلخی رومی . عثنوی چاپ عا(ءالدوله ص ۲۷

0 گرییدن - رك : گرستن .
```


## [2026-10-17T00:07:04.038Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; for w in \"گزاردن\" \"گزیر\" \"وچر\" \"وزیر\" \"گستردن\" \"گستاخ\" \"گسستن\" \"گشادن\" \"ویراستن\" \"گمان\" \"گماردن\" \"گواه\" \"گریختن\" \"گذشتن\" \"گزیدن\" \"گمیختن\" \"گمیز\" \"گزند\"; do echo \"## $w\"; for v in 3 4; do python3 - \"$v\" \"$w\" <<'EOF'\nimport sys,re\nv,w=sys.argv[1],sys.argv[2]\nt=open(f'BQT_v{v}_pages.txt').read().split('\\f')\noff={'3':1206,'4':1917}[v]\nhits=[]\nfor i,p in enumerate(t):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    pg=int(m.group(1)) if m else i+1\n    for mm in re.finditer(r'(^|\\n)\\s*'+w+r'\\s*[-–ـ]',p):\n        hits.append((pg,pg+off))\nprint(' v'+v, hits[:5])\nEOF\ndone; done"
}
```


### [2026-10-17T00:07:08.715Z] TOOL RESULT

```
## گزاردن
 v3 []
 v4 []
## گزیر
 v3 []
 v4 []
## وچر
 v3 []
 v4 []
## وزیر
 v3 []
 v4 []
## گستردن
 v3 []
 v4 []
## گستاخ
 v3 []
 v4 []
## گسستن
 v3 []
 v4 []
## گشادن
 v3 []
 v4 []
## ویراستن
 v3 []
 v4 []
## گمان
 v3 []
 v4 []
## گماردن
 v3 []
 v4 []
## گواه
 v3 []
 v4 []
## گریختن
 v3 []
 v4 []
## گذشتن
 v3 []
 v4 []
## گزیدن
 v3 []
 v4 []
## گمیختن
 v3 []
 v4 []
## گمیز
 v3 []
 v4 []
## گزند
 v3 []
 v4 []
```


## [2026-10-17T00:07:14.328Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; head -c 600 BQT_v3_pages.txt; echo; python3 - <<'EOF'\nimport re\nwords=[\"کزاردن\",\"کزیر\",\"وچر\",\"وزیر\",\"کستردن\",\"کستاخ\",\"کسستن\",\"کشادن\",\"ویراستن\",\"کمان\",\"کماردن\",\"کواه\",\"کریختن\",\"کذشتن\",\"کزیدن\",\"کمیختن\",\"کمیز\",\"کزند\",\"بیست\"]\nfor v,off in (('3',1206),('4',1917)):\n    t=open(f'BQT_v{v}_pages.txt').read().split('\\f')\n    for w in words:\n        hits=[]\n        for i,p in enumerate(t):\n            m=re.search(r'\\[pdf page (\\d+)\\]',p); pg=int(m.group(1)) if m else i+1\n            if re.search(r'(^|\\n)\\s*'+w+r'\\s*[-–ـ]',p.replace('گ','ک')): hits.append(pg+off)\n        if hits: print('v'+v,w,hits[:6])\nEOF"
}
```


### [2026-10-17T00:07:16.917Z] TOOL RESULT

```
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
7
Ub
sits k ge
AS ۱۰۶۲ ‏نتف‌بال‎
‏ومع‎ ‘oo ‏داي و‎ el Oe

far
en rotons ‘ ‘ ths ۰ ‏دیهان‎
‎۳ 2 7
۰ SF Ps
On Awe
۰
‏-ل‎ 9 ‘il
۱۳۴۳ ‏چاپ دوم فروردین‎
‏با تجدید نظر کامل‎
‏بسرمایه کتاپفروشی ابن سینا- تهران‎

|

چاپ افست ر شدیه
[pdf page 3]
اداره ‎“oes‏
‏ساره و6۷ ۲۰۹

pe ۰ ay sf s ‏ار بخ‎
‏سرام ودارت‌شسات‎

د انشمند محتر ,آقای‌د
```


## [2026-10-17T00:07:22.610Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nimport re\nwords=[\"کزاردن\",\"کزیر\",\"وچر\",\"وزیر\",\"کستردن\",\"کستاخ\",\"کسستن\",\"کشادن\",\"ویراستن\",\"کمان\",\"کماردن\",\"کواه\",\"کریختن\",\"کذشتن\",\"کزیدن\",\"کمیختن\",\"کمیز\",\"کزند\",\"بیمار\",\"بیست\"]\nfor v,off in (('3',1206),('4',1917)):\n    t=open(f'BQT_v{v}_pages.txt').read().split('\\f')\n    for w in words:\n        hits=[]\n        for i,p in enumerate(t):\n            m=re.search(r'\\[pdf page (\\d+)\\]',p); pg=int(m.group(1)) if m else i+1\n            n=p.replace('گ','ک').count(w)\n            if n: hits.append((pg+off,n))\n        hits.sort(key=lambda x:-x[1])\n        if hits: print('v'+v,w,hits[:5])\nEOF"
}
```


### [2026-10-17T00:07:23.457Z] TOOL RESULT

```
v3 کزاردن [(1811, 3), (1781, 2), (1813, 2), (1812, 1)]
v3 کزیر [(1546, 1), (1562, 1), (1635, 1), (1812, 1), (1814, 1)]
v3 وچر [(1485, 6), (1486, 2), (1789, 2), (1286, 1), (1294, 1)]
v3 وزیر [(1558, 4), (1330, 3), (1445, 2), (1367, 1), (1455, 1)]
v3 کستردن [(1461, 1), (1819, 1)]
v3 کستاخ [(1303, 1), (1819, 1)]
v3 کسستن [(1437, 1)]
v3 کشادن [(1646, 4), (1262, 2), (1821, 2), (1439, 1), (1450, 1)]
v3 کمان [(1691, 39), (1837, 7), (1692, 6), (1897, 5), (1398, 4)]
v3 کماردن [(1837, 2)]
v3 کواه [(1310, 1), (1849, 1), (1852, 1), (1865, 1)]
v3 کریختن [(1809, 2), (1810, 2), (1278, 1), (1576, 1), (1745, 1)]
v3 کذشتن [(1781, 3), (1812, 2), (1875, 2), (1520, 1), (1807, 1)]
v3 کزیدن [(1817, 3), (1811, 2), (1816, 2), (1313, 1), (1427, 1)]
v3 کمیختن [(1838, 1)]
v3 کمیز [(1696, 3), (1224, 2), (1838, 2), (1223, 1), (1693, 1)]
v3 کزند [(1813, 4), (1811, 3), (1397, 1), (1423, 1), (1435, 1)]
v3 بیمار [(1236, 1), (1333, 1), (1421, 1), (1641, 1), (1651, 1)]
v3 بیست [(1512, 3), (1552, 3), (1876, 3), (1323, 2), (1765, 2)]
v4 کزاردن [(2191, 1), (2333, 1)]
v4 کزیر [(2088, 2), (2103, 2), (2164, 2), (1927, 1), (2336, 1)]
v4 وچر [(2259, 3), (2216, 1), (2219, 1), (2252, 1), (2258, 1)]
v4 وزیر [(2124, 2), (2279, 2), (2310, 2), (1958, 1), (2003, 1)]
v4 کستردن [(2232, 1), (2346, 1)]
v4 کستاخ [(2252, 1)]
v4 کشادن [(2284, 1), (2466, 1)]
v4 کمان [(2234, 5), (2236, 3), (2364, 2), (2449, 2), (2465, 2)]
v4 کواه [(2044, 1)]
v4 کذشتن [(1982, 2), (1979, 1), (1983, 1), (1986, 1), (2017, 1)]
v4 کزیدن [(2084, 1)]
v4 کمیز [(2076, 1)]
v4 کزند [(1972, 2), (2121, 2), (1932, 1), (1984, 1), (1987, 1)]
v4 بیمار [(1935, 4), (2328, 3), (1937, 2), (2423, 2), (1959, 1)]
v4 بیست [(1931, 3), (2085, 3), (1936, 2), (2191, 2), (2241, 2)]
```


## [2026-10-17T00:07:31.615Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; mkdir -p $S/p553; for p in 1776 1778 1800 1806 1809 1813 1816 1818 1835 2258 2279 437 834; do python3 tools/ref_page.py BQT:$p --image > $S/p553/bqt-$p.txt 2>&1; echo \"== $p $(head -3 $S/p553/bqt-$p.txt | tr '\\n' ' ' | cut -c1-250)\"; done"
}
```


### [2026-10-17T00:07:39.179Z] TOOL RESULT

```
== 1776 IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1776.png REF: BQT:1776  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 573  OCR-lang: fas  
== 1778 IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1778.png REF: BQT:1778  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 575  OCR-lang: fas  
== 1800 (no exact page map; using offset -1205 -> pdf page 595; check the printed number and re-run with --pdf-page if off) IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1800.png REF: BQT:1800  PDF: data/verification/sources/re
== 1806 (no exact page map; using offset -1205 -> pdf page 601; check the printed number and re-run with --pdf-page if off) IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1806.png REF: BQT:1806  PDF: data/verification/sources/re
== 1809 (no exact page map; using offset -1205 -> pdf page 604; check the printed number and re-run with --pdf-page if off) IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1809.png REF: BQT:1809  PDF: data/verification/sources/re
== 1813 (no exact page map; using offset -1205 -> pdf page 608; check the printed number and re-run with --pdf-page if off) IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1813.png REF: BQT:1813  PDF: data/verification/sources/re
== 1816 (no exact page map; using offset -1205 -> pdf page 611; check the printed number and re-run with --pdf-page if off) IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1816.png REF: BQT:1816  PDF: data/verification/sources/re
== 1818 (no exact page map; using offset -1205 -> pdf page 613; check the printed number and re-run with --pdf-page if off) IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1818.png REF: BQT:1818  PDF: data/verification/sources/re
== 1835 IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1835.png REF: BQT:1835  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 632  OCR-lang: fas  
== 2258 (no exact page map; using offset -1917 -> pdf page 341; check the printed number and re-run with --pdf-page if off) IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2258.png REF: BQT:2258  PDF: data/verification/sources/re
== 2279 (no exact page map; using offset -1917 -> pdf page 362; check the printed number and re-run with --pdf-page if off) IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2279.png REF: BQT:2279  PDF: data/verification/sources/re
== 437 no scan of BQT covers printed page 437 (see 'scans' in refs_online.json) 
== 834 no scan of BQT covers printed page 834 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:07:43.933Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553; for p in 1776 1778 1800 1806 1809 1813 1816 1818 1835 2258 2279; do echo \"== $p\"; sed 's/گ/ک/g' bqt-$p.txt | grep -o -E \"(کزاردن|کزارش|کزیر|وچر|وزیر|کستردن|کستاخ|کسستن|کسیختن|کسیل|کشادن|کمان|کماردن|کماشتن|کواه|کریختن|کذشتن|کذاشتن|کزیدن|کمیختن|کمیز|کزند|اوستا|پهلوی|پپلوی)\" | sort | uniq -c | tr '\\n' ' '; echo; done"
}
```


### [2026-10-17T00:07:44.527Z] TOOL RESULT

```
== 1776
      1 اوستا       1 پهلوی       1 کمان 
== 1778
      2 اوستا       1 پپلوی       1 پهلوی       1 کذاشتن       3 کذشتن       1 کزاردن       1 کزارش 
== 1800
      1 اوستا 
== 1806
      1 کذشتن 
== 1809
      1 اوستا       1 پپلوی       1 کریختن 
== 1813
      1 کزارش       1 کزند       2 کزیدن       2 کزیر 
== 1816
      3 کذاشتن 
== 1818
      3 اوستا       1 پپلوی       1 پهلوی       3 کستاخ 
== 1835
      1 پپلوی       2 کمیختن       4 کمیز 
== 2258
      5 اوستا       3 پپلوی       1 پهلوی       3 کزارش       2 وچر 
== 2279
      3 اوستا       1 پپلوی       1 پهلوی       1 وزیر
```


## [2026-10-17T00:07:48.332Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; command ls | grep -E \"^(1776|1778|1800|1806|1809|1813|1816|1818|1835|2258|2279)\\.\" "
}
```


### [2026-10-17T00:07:48.814Z] TOOL RESULT

```
1776.png
1776.txt
1778.png
1778.txt
1800.png
1800.txt
1806.png
1806.txt
1809.png
1809.txt
1813.png
1813.txt
1816.png
1816.txt
1818.png
1818.txt
1835.png
1835.txt
2258.png
2258.txt
2279.png
2279.txt
```


## [2026-10-17T00:07:50.918Z] TOOL CALL #48: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2258.png"
}
```


### [2026-10-17T00:07:51.396Z] TOOL RESULT

```

```


## [2026-10-17T00:07:51.390Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:07:58.742Z] TOOL CALL #49: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2258.vision.txt <<'EOF'\n[BQT p. 2258, read from image 2258.png]\nوجر - بفتح اول وثانی وسکون رای قرشت، بمعنی فتوی باشد ... دستور حاکم شرع در مسئلهٔ شرعی نوشته بودند، و باین معنی با جیم فارسی هم آمده است.\nوجرگر - بفتح کاف فارسی وسکون رای قرشت، مفتی و فتوی دهنده را گویند چه وجر بمعنی فتوی آمده است.\nوچر - بفتح اول وثانی وسکون رای قرشت، بمعنی فتوی باشد و آن دستور حاکم ...\nFootnotes (Mo'in):\n۲ = «وچر» (ه.م.) قس: وجارش، گزاره، گزارش «خرده اوستا ص۷۸».\n۳ = «وچرگر» (ه.م.) ورک: خرده اوستا ص۷۸.\n۵ - دراوستا vîcîra بمعنی فتوی دهنده است. ازهمین لغت است کلمهٔ «وزیر» (ه م) که عرب از ایرانی بعاریت گرفته. در فرهنگها لغات «وجر» و «وجارش» و «وجرگر» بمعانی گزاره یا گزارش (شرح وتفسیر) وفتوی ودستور وفتوی دهنده یا مفتی ضبط شده، و با «چ» نیز آمده است. وچرکرت دینیک Vicarkart i Dênîk نام کتابی است زرتشتیان را ... وجزء اول این نام همین «وچر» است وجزء دوم kareta بمعنی فصل است ... رك: پورداود. خرده اوستا ص۷۸؛ ورك: وچرگر.\nEOF"
}
```


## [2026-10-17T00:07:59.326Z] TOOL CALL #50: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2279.png"
}
```


### [2026-10-17T00:07:59.435Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-17T00:07:59.940Z] TOOL RESULT

```

```


## [2026-10-17T00:07:59.936Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:08:04.714Z] TOOL CALL #51: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2279.vision.txt <<'EOF'\n[BQT p. 2279, read from image 2279.png]\nوزیر - با ثالث مجهول بروزن زریر، زردچوبه را گویند - وبا ثالث معروف درعربی بمعنی دستور باشد.\nFootnote ۷ (Mo'in): کلمه معرب است «اشتق ۱۰۸۴» از vicîr (یا vajîr) پهلوی «باروچا ۲۳۴» از اوستایی vîcira فتوی دهنده «پورداود. خرده اوستا ص ۷۸»، ارمنی vcir، نیز ارمنی gzir = فارسی gizîr (دهخدا، ریش‌سفید ده، محصل مالیات)، سریانی gezîrâyê (زاندارم) (Hoffmann, Auszüge, p. 62, Nr. 542) در خصوص «وزیر» رك: Nöldeke, Tab. 53, 444. «هوبشمان ۱۰۸۴» در فارسی gizîr، gezîr فقط در یك بیت ابوالمعالی آمده «اشتق شمارهٔ ۱۰۸۴، ص ۲۴۲ ح۲».\nEOF"
}
```


## [2026-10-17T00:08:05.229Z] TOOL CALL #52: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1818.png"
}
```


### [2026-10-17T00:08:05.282Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-17T00:08:05.831Z] TOOL RESULT

```

```


## [2026-10-17T00:08:05.826Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:08:13.066Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553; python3 tools/ref_page.py --help 2>&1 | head -20; for p in 1800 1806 1809 1813 1816 1818; do python3 tools/ref_page.py BQT:$p --image --pdf-page $((p-1203)) > $S/bqt2-$p.txt 2>&1; head -2 $S/bqt2-$p.txt; done"
}
```


### [2026-10-17T00:08:14.164Z] TOOL RESULT

```
Fetch ONE cited page of a scanned reference, on demand.

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

IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1800.png
REF: BQT:1800  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 597  OCR-lang: fas
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1806.png
REF: BQT:1806  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 601  OCR-lang: fas
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1809.png
REF: BQT:1809  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 604  OCR-lang: fas
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1813.png
REF: BQT:1813  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 608  OCR-lang: fas
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1816.png
REF: BQT:1816  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 612  OCR-lang: fas
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1818.png
REF: BQT:1818  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 613  OCR-lang: fas
```


## [2026-10-17T00:08:20.809Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553; for q in 597 603 606 610 632 573 575; do pdftoppm -f $q -l $q -r 110 -png -singlefile -gray data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $S/bqt-pdf$q; done; command ls $S"
}
```


### [2026-10-17T00:08:24.105Z] TOOL RESULT

```
bqt-1776.txt
bqt-1778.txt
bqt-1800.txt
bqt-1806.txt
bqt-1809.txt
bqt-1813.txt
bqt-1816.txt
bqt-1818.txt
bqt-1835.txt
bqt2-1800.txt
bqt2-1806.txt
bqt2-1809.txt
bqt2-1813.txt
bqt2-1816.txt
bqt2-1818.txt
bqt-2258.txt
bqt-2279.txt
bqt-437.txt
bqt-834.txt
bqt-pdf573.png
bqt-pdf575.png
bqt-pdf597.png
bqt-pdf603.png
bqt-pdf606.png
bqt-pdf610.png
bqt-pdf632.png
```


## [2026-10-17T00:08:26.081Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553/bqt-pdf610.png"
}
```


### [2026-10-17T00:08:26.104Z] TOOL RESULT

```

```


## [2026-10-17T00:08:40.277Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cat > 1813.vision.txt <<'EOF'\n[BQT printed p. 1813 = BQT_v3_picofile.pdf page 610 (offset -1203 here; the cached 1813.png was rendered from pdf 608 and is NOT this page)]\nگزیدن (بفتح اول، بر وزن وزیدن) - بمعنی نیش زدن است خواه بالآلت باشد و خواه بزبان ... و بدندان گرفتن را هم میگویند ...\nگزیدن (بضم اول) - ... بمعنی برگزیدن و انتخاب کردن باشد.\nFootnote ۹ (Mo'in, on gazīdan 'bite'): از: گز (بفتح اول) + یدن (پسوند مصدری)، پهلوی gazītan ... کردی ghezāndin، gazhdum ... ghezin (زازا ص ۳۶۲).\nFootnote ۱۰ (Mo'in, on gozīdan 'choose'): از: گز (بضم اول) + یدن (پسوند مصدری)، پهلوی vicītan (انتخاب کردن، تعیین کردن)، اوستا vikay (distinguere) «بارتولمه ۴۴۱»، ارمنی ع vcit (پاک، خالص)، سانسکریت vi+cay (انتخاب کردن)، بلوچی gicinag، gishainagh (انتخاب کردن) «اشتق ۹۱۸».\nAlso on this page: گزیت (معرب آن جزیه) ... گزیر.\nEOF\ncat > 1816.vision.txt <<'EOF'\n[BQT printed p. 1816 = BQT_v3_picofile.pdf page 613 (the cached 1818.png shows this page; printed number ۱۸۱۶ in the running head)]\nگستاخ - بضم اول، بروزن ومعنی بستاخ است که بی ادب و دلیر و تند باشد.\nگستر - ... بمعنی پهن کننده و افرازنده باشد ...\nگستردن - بفتح دال و سکون نون، بمعنی پهن کردن و فرو چیدن و فراز کردن باشد.\nFootnote ۱ (gostāx): پهلوی vistâxv، ارمنی ع vstah «نیبرگ ص ۲۴۵»، پارسی باستان vistâ(h)uva-? «هوبشمان ۹۲۰» و رك: اشتق ایضاً.\nFootnote ۶ (gostardan): از: گستر (ه.م.) + دن (پسوند مصدری)، گستر، قس: بستر. هندی باستان vi+star (پهن کردن)، پهلوی v(i)startan (پهن کردن) «اشتق ۹۲۱».\nFootnote (گسستن): بضم اول و کسر ... یا فتح دوم و فتح چهارم، از ریشهٔ اوستایی sid = سانسکریت chid = پارسی باستان visdrâmiy «هوبشمان ۹۲۲»، پهلوی v(i)sastan. رك: اشتق ۹۲۲؛ دارمستتر. تتبعات ۸۴،۱؛ قطع کردن، بریدن، جدا کردن - منقطع گشتن، پاره شدن، شکسته شدن - رها شدن. رك: گسلیدن.\nEOF"
}
```


## [2026-10-17T00:08:41.425Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553/bqt-pdf632.png"
}
```


### [2026-10-17T00:08:41.490Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-17T00:08:41.511Z] TOOL RESULT

```

```


## [2026-10-17T00:08:50.161Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cat > 1835.vision.txt <<'EOF'\n[BQT printed p. 1835 = BQT_v3_picofile.pdf page 632]\nگمیز - بکسر اول و ثانی بتحتانی کشیده و بزای نقطه‌دار زده، پیشاب را گویند که شاش باشد و بعربی بول خوانند.\nFootnote ۴ (Mo'in): پهلوی gumêc، رك: گمیختن. در فارسی «گمیز» با کاف ضبط کرده‌اند و اصح با گاف است.\nFootnote ۵ (گمیختن): بضم اول و فتح پنجم، از گمیخ (= گمیز [ه.م.]) + تن (پسوند مصدری)، پهلوی gumêxtan (مخلوط کردن)، ایرانی باستان vi-maik، سانسکریت miksh «نیبرگ ص ۸۶»؛ جزء اول پیشوند است بمعنی بد، ضد؛ وجزء دوم بمعنی آمیختن، لفظاً بمعنی بدآمیختن؛ مخلوط کردن، قاتی کردن - پیشاب ریختن.\nEOF"
}
```


## [2026-10-17T00:08:51.501Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553/bqt-pdf575.png"
}
```


### [2026-10-17T00:08:51.574Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-17T00:08:51.645Z] TOOL RESULT

```

```


## [2026-10-17T00:08:59.449Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cat > 1778.vision.txt <<'EOF'\n[BQT printed p. 1778 = BQT_v3_picofile.pdf page 575 (bayān-e haštom: گاف فارسی با ذال)]\nگذاردن - بضم اول بروزن شماردن، بمعنی گذاشتن باشد و بمعنی ادا کردن ...\nگذارش - بضم اول وکسر رابع ... بمعنی گذشتن و ترک دادن ...\nگذاشتن - ... بمعنی گذاردن است ...\nگذرنامه - بضم اول، خط جواز باشد ...\nگذشت - بضم اول وفتح ثانی ... ماضی گذشتن ...\nFootnote ۳ (گذاشتن): = گذاشتن، پهلوی vitârtan، ارمنی vtar، هندی باستان vi+tar «اشتق ۸۹۳»، اوستا vi.tar «بارتولمه ۶۴۰» «نیبرگ ص ۲۴۶» ... در فارسی بمعنی متعدی آمده.\nFootnote ۵ (گذشتن): بضم اول و فتح دوم و چهارم، پهلوی vitashtan = vitartan، اوستا vi.tar «بارتولمه ۶۴۰، نیبرگ ۲۴۶» ورك: تاوادیا ص ۱۶۷؛ عبور کردن، مرور کردن، قطع کردن، پیش رفتن، مقدم شدن، تجاوز کردن، ترک کردن، بخشیدن.\nEOF"
}
```


## [2026-10-17T00:09:00.616Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553/bqt-pdf606.png"
}
```


### [2026-10-17T00:09:00.675Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-17T00:09:00.701Z] TOOL RESULT

```

```


## [2026-10-17T00:09:09.461Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cat > 1809.vision.txt <<'EOF'\n[BQT printed p. 1809 = BQT_v3_picofile.pdf page 606 (the cached 1809.png is pdf 604 = printed 1807, NOT this page)]\nگزاردن - بضم اول وفتح دال ابجد، بمعنی ادا کردن باشد چنانکه گویند «قرض خود را گزارد» و «نماز گزارد» یعنی ادای دین نمود ...\nگزارش - بضم اول وکسر رابع وسکون شین نقطه‌دار، تعبیر خواب را گویند - و بمعنی شرح و تفسیر و ادا کردن سخن ...\nگزارشگر - ... معبر و تعبیر کنندهٔ خواب ...\nFootnote ۲ (Mo'in, گزاردن): از: گزار + دن (پسوند مصدری) = گزاردن، گزاشتن؛ جزء اول vi + câr (شرح کردن، توضیح دادن)، سانسکریت vicârayati (سنجیدن، تأمل کردن، وارسی کردن)، vicâra (تأمل، سنجیدن)، vicârana (تأمل و شرح دادن)، پهلوی vicârishn «نیبرگ ص ۲۴۱-۲۴۲»، vicârtan «اشتق ۹۱۷»؛ ورك: هوبشمان ایضاً.\nEOF"
}
```


## [2026-10-17T00:09:10.715Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553/bqt-pdf603.png"
}
```


### [2026-10-17T00:09:10.776Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-17T00:09:10.793Z] TOOL RESULT

```

```


## [2026-10-17T00:09:15.091Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cat > 1806.vision.txt <<'EOF'\n[BQT printed p. 1806 = BQT_v3_picofile.pdf page 603 (the cached 1806.png is pdf 601 = printed 1804, NOT this page)]\nگریز - بفتح اول ... گریختن و گریزیدن ...\nFootnote ۹ (گریغ): پهلوی virêk (طرد، نفی بلد)، ایرانی باستان vi-raika (رك: گریختن) ...\nFootnote (گریختن): بضم اول و فتح پنجم، پهلوی virêxtan از virêc (فرار کردن)، از ایرانی باستان raik+vi، از raêk (linquere) «بارتولمه ۱۴۷۹» «نیبرگ ص ۲۴۴»، ورك: اشتق ۹۱۴؛ فرار کردن، بسرعت دور شدن.\nFootnote (گریز): بضم اول، اسم از گریختن (ه.م.) [رك: گریغ]؛ فرار، دور شدن بسرعت.\nEOF"
}
```


## [2026-10-17T00:09:16.357Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553/bqt-pdf573.png"
}
```


### [2026-10-17T00:09:16.407Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-17T00:09:16.427Z] TOOL RESULT

```

```


## [2026-10-17T00:09:21.670Z] TOOL CALL #66: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553/bqt-pdf597.png"
}
```


### [2026-10-17T00:09:21.691Z] TOOL RESULT

```

```


## [2026-10-17T00:09:25.365Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553; pdftoppm -f 615 -l 615 -r 110 -png -singlefile -gray data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $S/bqt-pdf615"
}
```


## [2026-10-17T00:09:26.548Z] TOOL CALL #68: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553/bqt-pdf615.png"
}
```


### [2026-10-17T00:09:26.948Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-17T00:09:26.963Z] TOOL RESULT

```

```


## [2026-10-17T00:09:32.112Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cat > 1818.vision.txt <<'EOF'\n[BQT printed p. 1818 = BQT_v3_picofile.pdf page 615 (bayān-e sizdahom, گاف با شین; the cached 1818.png is pdf 613 = printed 1816, NOT this page)]\nگشاد - بضم اول بروزن مراد، بمعنی فراخ است که در برابر تنگ باشد - و ماضی گشادن هم هست ...\nFootnote ۵ (Mo'in, گشادن): بضم اول و فتح چهارم، از گشا (ه.م.) + دن (پسوند مصدری)، پهلوی vishâtan (آزاد کردن، باز کردن)، سانسکریت vi-sâ؛ رك: هوبشمان ۹۲۳؛ جزء اول در پهلوی vishât، از vi-shâ، اوستایی hây + vi «بارتولمه ۱۸۰۰» (باز کردن، آزاد کردن) «نیبرگ ص ۲۴۵»؛ اشتق ۹۲۳؛ کردی veshiian ...؛ باز کردن، آشکار کردن، رها ساختن. رك: گشودن.\nEOF"
}
```


### [2026-10-17T00:09:32.583Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:09:36.216Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -A6 \"^vizier\\|vizier, n\" KLN_1966.txt | head -20; grep -n -i \"wazir\\|vizier\" FVQ_pages.txt | head; grep -n -i -B2 -A8 \"vizier\" SKT.txt | head -15"
}
```


### [2026-10-17T00:09:36.713Z] TOOL RESULT

```
10318:jljj (Wazir).
10321:Both passages refer to Aaron being given to Moses as his Wazir,
20984-visual  (F.-L.)  F.  v^mi/.-L.  miim- a/i>,  belonging  to  the  sight.  —  L.  uiiu-, crude  form  ol  ttisus,  sight.  —  L.  uisMj,  pp. of  uidere^  to  see.
20985-vitreous.  {L.)  L.  uitnm,  ai/riw. glassy. —  L.  uttri;  for  uitn-,  crude  form of  uitrum,  glass.  The  »  in  uitrum  was originally  long ;  so  that  uitrum  =  uid'trum  •. —  ll.  uiiiere,  lo  see.
20986:vitnol.  tF.-L)    F.CT/rw/.  ' vitriol!;' Cot.     Said  to  be  so  called  from  its  trans- parency. —  Low  L.  uitrio/us  •  =  L.  Mttreoius, glassy.  —  L.  uitreus,  glassy.  —  L.  uitrum, glii:>s  (above). Visit.  Visor ;  see  Viaion. Vista.  Visual;  see  Viaion. Vital;  see  Victuals. Vitiate;  seeVioe  (i). Vitreous.  Vitriol :  see  Vision. Vituperation;  see  Vice  (i). Vivacity  .Vivid.  Vivify;  sec  Viotnals. Viviparous,  Viviseotion  \  see  Vic- tuals. Vixen ;  see  Fox. Vis. ;  see  videlioet,  under  VUlon. Vizard;  sec  viaor.  tinder  Viaion. Vizier,   Visier,  a  councillor  of  state. (Arab.)       Arab,    wtuir,   a    counsellor    of state;  orig.  a  porter,  one  who  bears  Che burden  of  stale  alTairs  —Arab,  root  cmsa/v, to  bear  a  burden,  sustain.
20987-al^ruazil,    a    police    officer.     (Span.— Amh.)     Span,  a/iuati/.  —  Arab,  a),  the; UHitir,  a  viricr,  officer. Vooable;  see  Vocal. Vooal*    ullchng    *o^?^A-    0?  -^-'^     ^ Mioi, »  L.  %m<Uu ,  adi.»  Irotft  «c-
20988-I
20989-I
20990-548
20991-VOGUE.
20992-ttox,    voice,    wund.  +  Gk.  ttot,  ft   word  f Skt.  vacMas,  speech,  frum  v<uk,  to  speak.
20993-advocate,  sb.  (F.-U)    O.  F.  aJvocat,
20994-'  an  advocate ; '    Cot.  »  I^  atiaocaius,   an
--
23362-vade — fade, valtt — varlet. vast — waste. veal — wether, veneer— furnish. venew.  veiiey — venue, verb — woid vertex— voncK.
23363-DS,  ETC
23364:vi  a  ti  cu  m  — voy  age. viper — wyvern.  wivem. visor — vizard, vizier,  visier— algxiafU. vocal — vowel.
```


## [2026-10-17T00:09:38.535Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 10300,10340p FVQ_pages.txt; grep -n -i \"vizi[e]r\\|vizir\" KLN_1966.txt KLN_1971.txt | head"
}
```


### [2026-10-17T00:09:39.224Z] TOOL RESULT

```
as a term of abuse.
(Warda).
Iv, 37. "
Rose.
The passage is eschatological and a^J means rose-red, referring
to the colour of the sky, a meaning derived, of course, from the original
sense of rose.
It was very commonly recognized that it was a loan-word, 1 though
it is curious that the philologers make no suggestion as to its origin,
for it is obviously a borrowing from Persia. The primitive Indo-
European root *urdho means a spiny tree, from which comes the Gk.
poSov = Fpo8ov, and the Av. jjgjJi> vawSa (Bartholomae,
AIW, 1369), whence Arm. '/_"/?. rose, 2 and Phlv. jjqo)> varta
(PPGl, 228). 3 From the Iranian it was borrowed into Semitic, 4 where
we find Aram. XTll, Syr. }jio, 5 and from the Aram., as Fraenkel,
Vocab, 11, noted, it passed into Arabic. As a proper name Ovdpda,
QvapSi]? is found in the N. Arabian inscriptions. 6
*> ^
jljj (Wazir).
xx, 30 ; xxv, 37.
A minister, counsellor.
Both passages refer to Aaron being given to Moses as his Wazir,
where the reference is obviously to Ex. iv, 16.
1 as-Suyuti, Itq, 325 ; Muzhir, i, 137 ; al-Jawaliqi, Mu'arrab, 151 ; TA, ii, 531.
2 Hubschmann, Arm. Gramm, i, 244. So Sogd. wrd (Henning, Manichdisches
Beichtbuch, 1937, p. 137) and Parthian u>V (Kenning, BSOS, ix. 88).
8 Though some suspect the Phlv. form of being a reborrowing from Semitic, vide
Horn, Grundriss, 207 ; Frahang, Glossary, 77. Mod. Pers. borrowed back jj) from
Arabic in Islamic times.
4 Of. Telegdi in JA, ccxxvi (1935), p. 241.
5 Cf. also the Mand. NT1N1, Noldeke, Mand. Gramm., 56, and cf. Zimmern,
Akkad. Fremdw., 65, for an even earlier borrowing.
8 Wuthnow, Die semitischen Menschennamen ingriechischenlnschriflen und Papyri
des vorderen Orients, 1930, p. 92 ; Ryckmans, Noms propres, i, 81.288 FOREIGN VOCABULARY OP THE QUR J AN
The usual explanation of the word is that it is a form Ju,* from
J j J to bear or carry, and thus means one who carries the burdens of the
Prince (cf. Kaghib, Mufraddt, 542). Lagarde, Ubersicht, 177, n.,
however, pointed out that it is an Iranian word, and in his Arm.
Stud, 2155, he derives it from the Phlv. JSg) weir, which originally
meant a decree, mandate, command, but which later, as in the Dinkard,
came to mean judge or magistrate. 1 This word, of course, is good Iranian,
KLN_1971.txt:11118:‘the’, and waztr, ‘vizier’. See vizier, 
KLN_1971.txt:263376:vizier, more correctly vizir, n. — Turk, vezir, 
KLN_1971.txt:263384:vizierate, vizirate, n., the office or dignity of a 
KLN_1971.txt:263385:vizier. — A hybrid coined from prec. word and 
KLN_1966.txt:2189:algology,  n.,  the  study  of  algae.  —  A  hybrid  coin¬ ed  fr.  L.  alga  and  Gk.  -Xoyla,  fr.  -Xoyo;,  ‘one who  speaks  (in  a  certain  manner) ;  one  who  deals (with  a  certain  topic)’.  See  alga  and  -logy. Derivatives:  algolog-ical,  adj.,  algolog-ist,  n. algor,  n.,  cold;  chill.  —  L.,  fr.  algere,  ‘to  be  cold’. See  algid  and  -or.  For  the  mode  of  formation cp.  terror,  ‘fright’,  fr.  terrere,  ‘to  frighten’,  albor, ‘white  color’,  fr.  albere,  ‘to  be  white’, algorism,  n.,  the  Arabic  system  of  numerals.  — ME.  algorisme,  fr.  OF.  algorisme  (F.  algorith- me),  fr.  ML.  algorismus ,  from  the  inexact  trans¬ literation  of  Arab.  al-Khowarizmi,  ‘the  man  of Khowarizm  (the  modern  Khiva),  surname  of Abu  Jafar  Mohammed  ibn  Musa,  great  mathe¬ matician  of  the  9th  cent.  His  famous  work  Al- jabr  w’al  muqdbalab  (‘Reunion  and  compar¬ ison’),  introduced  the  use  of  Arabic  numerals  in Europe,  which  denoted  a  turning  point  in  the history  of  mathematics.  Cp.  algebra, algous,  adj.,  pertaining  to  algae.  —  L.  algosus, fr.  alga,  ‘seaweed’.  See  Alga  and  -ous. alguazil,  n.,  peace  officer  in  Spain.  —  Sp.  alguacil, fr.  earlier  alguazil,  fr.  Arab,  al-wazfr,  fr.  al-, ‘the’,  and  waztr,  ‘vizier’.  See  vizier, algum,  n.  —  See  almug.
```


## [2026-10-17T00:09:41.520Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 263376,263384p KLN_1971.txt; grep -n \"This word, of course, is good Iranian\" -A14 FVQ_pages.txt | head -16; grep -o -i \".\\{0,100\\}vezir.\\{0,300\\}\" KLN_1966.txt | head -3"
}
```


### [2026-10-17T00:09:44.552Z] TOOL RESULT

```
vizier, more correctly vizir, n. — Turk, vezir, 
‘counsellor’, fr. Arab, wazir (in vulgar pronun- 
ciation wezir), fr. Avestic vicira, ‘arbitrator, 
judge*. In Arabic wazir superseded katib (lit. 
‘writer’) in the meaning of ‘secretary of state’. 
The ‘Arabic’ word was ‘re-borrowed’ by the 
Persians under the Ommiads; see The Encyclo- 
pedia of Islam, IV, 1229. Cp. alquacil. 
vizierate, vizirate, n., the office or dignity of a 
10340:came to mean judge or magistrate. 1 This word, of course, is good Iranian,
10341-being from the Av. .ujj^j/? vicira meaning deciding,* which was
10342-borrowed into Arm. as *t&bn-? and is related to the form behind the
10343-Mod. Pers. j>-$ or ^>-J judge*', J^J or prefect* and jjjj, which is
10344-generally regarded as a loan-word from Arabic but which Bartholomae,
10345-AIW, 1438, rightly takes as a genuine derivative from the older
10346-Iranian word.
10347-The borrowing was doubtless direct from the Middle Persian, for the
10348-Syr. }^1O seems to be late and a borrowing from Arabic (PSm, 1061).
10349-> > i ^ ^ > > i .-
10350-tr J>\-A } r j>\-s (Ycijuj wa Mdjuj).
10351-xviii, 93 ; xxi, 96.
10352-Gog and Magog.
10353-Both passages are reflections of Syriac legends concerning Alexander
10354-the Great.
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,300}
                        \___exceeds complexity limits
```


## [2026-10-17T00:09:48.527Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; for p in 78 80; do echo \"=== pdf $p\"; awk -v n=$p 'BEGIN{RS=\"\\f\"} $0 ~ \"\\\\[pdf page \"n\"\\\\]\"' FFD_pages.txt | head -60; done"
}
```


### [2026-10-17T00:09:49.041Z] TOOL RESULT

```
=== pdf 78
[pdf page 78]
ماده‌های ماضی و مضارع قارسی دری ۷۳
است. «گله» فارسی دری از 81188 فارسی میانه آمده است و 8128 از 874-42* فارسی
باستان. 874 صورت ضعیف ريش 8۵74 / 8720 است. 218 پسوند بوده است.
۱ گزاردن
گزارد + فارسی میانه ۷12274 < ایرانی باستان 3۳-1۵.-۷*. برای ۵ -> آراست. ۷:۱
پیشوند فعلی است. لَن صورت بالاندةٌ ريشهٌ 27 به معنی «حرکت کردن» است.
«(چریدن) از ریشهٌ 47 آمده است > چریدن.
گزار < فارسی میانه ۷1237 < ایرانی باستان 2۲-۵.-۷۷*. برای 2 > آرای.
گُزیدن
گُزید ج فارسی میانه ۷127۵ < ایرانی باستان ۶۷-6۲-1۵ برای ۵ > آراست. ۷
پیشوند فعلی است. آت صورت ضعیف ریشةٌ له به معنی «گزیدن» است.
گزین ج فارسی میانه ۷۵217 < ایرانی باستان ۹1-61-۵*. 120 نشانه‌ای بوده که برای
ساختن ماده مضارع از ريشه به کار می‌رفته است.
گزیدن
۰ کِ شت.+
گستردن
گسترد < فارسی میانه ۷181۵74 < ایرانی باستان ۴۷۷1-81۵۳-12. برای ۵ -> آراست. ۷1
پیشوند فعلی است. ريشهٌ 5187 به معنی «پاشیدن» است.
گستر < فارسی میانه ۷۷۶17 < ایرانی باستان ۷1-۹1۵۳-۵*. برای 2 -> آرای.
ا گسست < فارسی میانه ۷9181 < ایرانی باستان ۷:1-918-1۵*. برای 2 > آراست. ۷:1
؛ پیشوند فعلی است. 814 صورت اصلی ريشه به معنی «بریدن» است و 4 پیش از ]به بدل

=== pdf 80
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
```


## [2026-10-17T00:09:53.519Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 79\\]/' FFD_pages.txt | head -60; grep -n \"گذشتن\\|گذاشتن\\|گریختن\\|گمیختن\\|ویراستن\\|گشادن\\|گشودن\" FFD_pages.txt | head"
}
```


### [2026-10-17T00:09:54.112Z] TOOL RESULT

```
[pdf page 79]
4۳ نفعلهای فارسی دری
شده است. 814 صورت ضعیف ريشهٌ ۶210 است.

«گسل» در فارسی دری مادهٌ مضارع «گسستن) است. در فارسی میانه مادةٌ مضارع

: اقا ملع آمده است و آن از ۷۷۹-۹18۵* ایرانی باستان آمده است. ۶104 از ادخال 8

پیش از آخرین صامت ريشه برای ساختن مادهٌ مضارع از ريشه به کار رفته است.

در فارسی دری «گسیخت» به جای «گسست» به کار رفته است.

گشادن, گشودن

گشاد < فارسی میانه ۴834 < ایرانی باستان ۷1-33-1۵*. برای 1۵ > آراست. ۷۷
پیشوند فعلی است. ۳3 صورت اصلی 3 است» « پس از ابه 5 بدل شده است. ريشة ۲3
به معنی «بستن» است. «گشود» در فارسی دری به قباس با «سرود»» «سرای» به وجود
آمده است.

گشای + فارسی میانه 152 < ایرانی باستان ۳-52-78*. # برای ساختن ماده از
ريشه به کار می‌رفته است.

گید(

گشت < فارسی میانه ۷251 < ایرانی باستان ۹279-12*. برای 1۵ -> آراست. ۷۷۸۲۲
صورت اصلی ۷۷279 است. 1 پیش از ۲ به 8بدل شده است. ‏ -

گرد + فارسی میانه ۷۷۵۲ < ایرانی باستان ۳:۵۳-۵*. برای 2 -> آرای,

گاشت. مادةٌ ماضی گاشتن» از ۷37۳-۲۵ آمده است. ۷371 صورت بالاندةٌ 8۶۲ است.

گشت. ()

گشت < پهلوی اشکانی 8281 < ایرانی باستان 8۵3-12*. برای 1۵ -> آراست. 8۵7
صورت اصلی 825 است» 2 پیش از + به 5بدل شده‌است.ريشةٌ 822 به‌معنی «گزیدن» است.

گز + فارسی میانه 822 < پهلوی اشکانی 82۵7 < ایرانی باستان 827-2" برای ۵ ->
آرای.

1255:78 (۷۲3 را به صورتهای «ویراستن)» «ویرای» به فارسی دری آورده‌اند.
1519:باستان 182: گریختن.
1554:«گریختن» هم از ريشةٌ له آمده است > گریختن.
1918:گذاردن, گذاشتن
1928:گذردن, گذشتن
1957:گریختن ۱
2001:گشادن, گشودن
2165:پیشوند فعلی است. ريشهٌ 13 به معنی «گذاشتن» است.
2183:ویراستن
2334:83 : (ريشه < نهادن, گذاشتن) ۵۲ ۸۰ 2 و۶۶
```


## [2026-10-17T00:09:58.930Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; sed -n 1918,1965p FFD_pages.txt; sed -n 2183,2192p FFD_pages.txt; grep -n \"pdf page\" FFD_pages.txt | awk -F: '$1<1965' | tail -2; grep -n \"pdf page\" FFD_pages.txt | awk -F: '$1<2190' | tail -1"
}
```


### [2026-10-17T00:09:59.528Z] TOOL RESULT

```
گذاردن, گذاشتن

گذارد. گذاشت < فارسی میانه 14374 ۷14331 . ۷14370 از ایرانی باستان
-۳۷۷-137. برای 1۵ -> آراست. ۷1 پیشوند فعلی است. 137 صورت بالاندةٌ ریشهٌ 1۵7 به
معنی «عبورکردن» است. 137 صورت بالاندهٌ ريشه در معتی واداری به کار رفته است و
7 صورت افزودهٌ ریشه در معنی لازمی > گذردن. ۷1۵0351 به قیاس با 137 و 381 به
وجود آمده است. َ

گذار < فارسی میانه ۷1۵27 < ایرانی باستان 9۷-13۳-۵*. برای ۵ > آرای.

گذردن, گذشتن

گذرد., گذشت < فارسی میانه ۳1427۵ ۷1۵۵51 .۷14276« ایرانی باستان ۷:1-1۵7-1۵*.
برای ۵ > آراست. پیشوند فعلی است. ريشهٌ 187 به معنی «عبور کردن» است. ۲۷۷1۵۵51
به قیاس با 137و 1351 به وجود آمده است.

گذر < فارسی میانه ۷1۵1۲ + ایرانی باستان ۷1-1۵7-78*. 98 نشانه‌ای بوده که برای
ساختن مادهٌ مضارع از ريشه به کار می‌رفته است.

گراییدن

گرایید < فارسی میانه 70ر8۲3. مادةٌ ماضی جعلی استء از ماده مضارع ساخته شده ۱
است.

گرای < فارسی میانه 8739 + ایرانی باستان 872-78*. ۷8 نشانه‌ای بوده که برای
ساختن مادهٌمضارع از ريشه‌به کار می‌رفته است. ریشةٌ 8۲3 به معنی «خم‌شدن) است.
[pdf page 77]
کچ یا ی فعلهای فارسی دری
گرفتن
گرفت + فارسی میانه 878 < ایرانی باستان 87۳-4۵ *. برای 13 > آراست. 870 صورت
: اصلی 871 است» ۳ پیش از ۲ به / بدل شده است. 870 صورت ضعیف ريشةٌ 8780 به
معنی «گرفتن» است.
گیر + فارسی میانه 8۲3 < ایرانی باستان 8۲8-72*. 72 نشانه‌ای بوده که برای ساختن
ماده از ريشه به کار می‌رفته است.
گروستن, گرویدن
گروست + فارسی میانه ۷۷07۲2۷۷181. ۱۷۷۵۳۷۷/۶1 مادةٌ ماضی جعلی از مادهٌ مضارع
است. «گروید» در فارسی دری مادهٌ ماضی جعلی است. از مادهٌ مضارع.
گرو + فارسی میانه ۷۷۵۶۶۷۷ + ایرانی باستان ۴۷۶۵۷ ۷۲ صورت ضعیف ريشةٌ
57 به معنی «گُزیدن) است. 1820 برای ساختن ماده مضارع از ريشه به کار می‌رفته است.
گریختن ۱
گریخت + فارسی میانه ۷۷788 + ایرانی باستان ۷۷1-۵0-1۵*. برای 18 -> آراست. ۷:1
پیشوند فعلی است. 7211 صورت اصلی 731 است» 1 پیش از 1 به تابدل شده است. ريشةٌ
جه به معنی «ترک کردن» است. (ریختن» از ریشةٌ انة7 آمده است + «ریختن».
گریز + فارسی میانه ۷762« ایرانی باستان ۷1-۵16-2*. برای ۵ -> آرای. ابه جای ۸
آمده است.
گریست < فارسی میانه افاولاع. 81اررزتع ماده مأضی جعلی است» از مادهٌ مضارع
ساخته شده است.
گری + فارسی میانه 1تع + فارسی باستان 8۲4-78* « ایرانی باستان 8۳۵2-78 *. 2
ویراستن
> پیراستن
۱ هراسیدن

«هراسید» مادةٌ ماضی جملی است: از ماده مضارع ساخته شده است.

هراس + پهلوی اشکانی 21739 < ایرانی باستان ۵:392* + ۵73-9-8*. برای 2۵ >
آرای. ۶ برای ساختن مادهٌ آغازی به کار می‌رفته است. 073۳ صورت بالاندةٌ ریشه 17۳
است, با ابدال 1 به ۰0 ريشهٌ 1۳8 به معنی «ترسیدن» است» ۰28739 که از صورت بالاندهٌ
ريشةٌ 12 آمده به معنی «ترساندن» است. «ترسیدن) هم از 15 آمده است > ترسیدن.
1910:[pdf page 76]
1944:[pdf page 77]
2181:[pdf page 86]
```


## [2026-10-17T00:10:05.060Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/extracted/batch; grep -l '\"name\": \"Leigh 2\"\\|\"name\": \"Me\"\\|\"name\": \"Kwek\"\\|\"name\": \"Gwhen 2\"\\|\"name\": \"Meig\"\\|\"name\": \"Ar\"\\|\"name\": \"Mer 1\"\\|\"name\": \"Kwer\"' page-*.json | head; python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('page-*.json')):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        r=e.get('root') or {}\n        if r.get('name') in ('Leigh 2','Me','Kwek','Gwhen 2','Meig','Ar','Mer 1','Kwer','Sě 1','Dekm'):\n            print(f, r.get('name'), r.get('gloss'), r.get('refs'))\nEOF"
}
```


### [2026-10-17T00:10:05.705Z] TOOL RESULT

```
page-215.json
page-114.json Dekm ten POK:191
page-115.json Dekm ten POK:191
page-215.json Gwhen 2 to strike, hurt POK:492
```


## [2026-10-17T00:10:34.213Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"v[iīl]ma[δd8S]|vlmaS|vlmad|vimaS|v[iīl]manah|vimano|vlmano\" BRT.txt | head -8 | cut -c1-250; grep -n -E \"^ *[0-9]+\\. *gum\" HRN.txt | head; grep -c . BRT.txt"
}
```


### [2026-10-17T00:10:34.837Z] TOOL RESULT

```
21254:•  j-  yat-£it  Konjn.  i }  konzessiv  'auch  wenn, wenn  schon';  das  Verbum  {'aA-)  ist  weg- gelassen: y  usas/aire  Aimivs(sd.)  *ag»urva- yeiti  Y.57.  29;  29,  Yt /o.  104';  —  mit Praes.:  hs ..  iiva.vasmai^A^  apayeifi  ..y° vazai
24192:Bt.  vimadhya-  n.  'Mitte'").  —  ')  Hds.  'iim; s.  die  Var.  lu  Yt.  10.  104.  Doch  TgL  auch fatay-  No.  2.  —  ')  Wegen  tnp.  n  d  mn  d  (/Si.  I
30725
```


## [2026-10-17T00:10:38.620Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; n=$(grep -n \"gumän 932\" HRN.txt|head -1); grep -n -E \"^ *93[0-9]\\.\" HRN.txt | head; sed -n 8080,8100p HRN.txt; grep -n \"^ *218\\. \" HRN.txt; "
}
```


### [2026-10-17T00:10:39.156Z] TOOL RESULT

```
8079:930. gile 'Klage .
8085:931. f/ii^ii«/Sfeii/an vertrauen, übergeben', Praes. gumär-em.
8089:932. gtitnän 'Zweifel; Meinung'.
8093:933. f/unäh 'Sünde'.
8099:934. yend 'Gestank', gmda stinkend', gendah 'Pfuhl*, gend-
8122:935. gend/um *Weizen', ar. LW. jandum in jauz-i jandum.
8129:936. gunde *Hefenballen (für ein BrotV.
8133:937. gv/ng 'stumm' 8).
8139:938. gor 'Wildesel*, gür/er,
8163:939. guvälfden, gevaltden (falsch k"*) wachsen* (unbelegt);
aw. gerezü" 'Klage', vergl. [/^gar2-, gerezaiti 'klagen';
plilv. garzTtan j garz{i)s7i, gilak (Men.); ai. l^garh-,
garhate 'klagen, anklagen' ^).
kurd. gilt 'Klage', gire 'Streit'; oss. d. yärziin, t.
gärzin stöhnen* (89).
931. f/ii^ii«/Sfeii/an vertrauen, übergeben', Praes. gumär-em.
ap. *»/ -r V^mar- mit Bedeutungswechsel, vergl. skr.
vi- r smav' 'vergessen' ; phlv. gumästan, gumür.
Unsicher.
932. gtitnän 'Zweifel; Meinung'.
aw. '^vwianah' 'Zweifel', vergl. mmiwöhya-; phlv.
gnmän,
LW. kurd. afy. gumän 'Zweifel*; bei. gtarän (121).
933. f/unäh 'Sünde'.
g. venall.
skr. vinäga- 'das Verlorengehen, Vernichtung, Unter-
gang (m + iXwa^r-) ; phlv. v{i)ncLskary v{i)na8karth, arm.
LW. vnas, vnasakar,
LW. kurd. gmiäh 'Sünde*; bei. gunas (119).
934. yend 'Gestank', gmda stinkend', gendah 'Pfuhl*, gend-
egl, gende, gendamden (AM. 45 Zeile 1; 78 Zeile 3
2283:218. hister Xager (Vis und Kämm S. 69 Vers 3); guster
9898:218. Dazu arDi. LW. pastar, Hübschmann, KZ. 26, 605.
11238:218. varöniand zweifelnd', varömandth 'Zweifel' (AW.-
11281:218. vem Talle .
```


## [2026-10-17T00:10:41.616Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2283,2295p HRN.txt; grep -n \"^ *94[0-9]\\.\\|guvah\\|guväh\" HRN.txt | head -5; grep -n -i -E \"^ *[0-9]+\\. *b[iīl]st \" HRN.txt | head"
}
```


### [2026-10-17T00:10:42.170Z] TOOL RESULT

```
218. hister Xager (Vis und Kämm S. 69 Vers 3); guster
(fehlt bei Vullers).
g. vistara 'Bett, Bettzeug .
vi-\- [/^star- 'ausbreiten, *vistarana-; vergl. gusf erden
(No. 921).
Da np. bister nicht *Kleid' bedeutet, so hat Fr.
Müller (WZKM. 4, 259) kein Recht, es — abgesehen
von der Nebenform guster — von aw. vastra- ab-
zuleiten.
219. besten 'binden', Praes. bend-em., bend,
ap. basta^ gebunden'; aw. [/"band- 'binden', banda^
'Band'; phlv. bastan, band; ai. [/"bandh- , badhndü,
bandhd",
8167:940. guvah, guva *Zeuge'.
8171:941. gösäle 'Kalb'.
8176:942. göspendj gösfend 'Kleinvieh, Schaaf, Widder, Ziege'.
8178:943. gas 'Ohr*.
8185:944. gast 'Fleisch*.
```


## [2026-10-17T00:10:44.520Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 8167,8171p HRN.txt; grep -n -E \"^ *2[0-9]{2}\\. *b[iīl1]st\" HRN.txt | head -3; grep -n \"zwanzig\" HRN.txt | head -3"
}
```


### [2026-10-17T00:10:45.059Z] TOOL RESULT

```
940. guvah, guva *Zeuge'.
ai. vi + \/^ka^- Intens, ausschauen, erschauen, wahr-
nehmen'; phlv. gukäs 'Zeuge', gtikasih (M^n.), arm. LW.
vkay *Zeuge', vkayem 'ich bezeuge* 2).
941. gösäle 'Kalb'.
2585:254. bfst 'zwanzig. /^
2587:aw. vTsaiti- 'zwanzig ; phlv. vist;{ai, vingati-j arm.
```


## [2026-10-17T00:10:50.347Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; for w in بیمار گمان گواه بیست گستاخ گزیدن; do echo \"## $w\"; grep -n -E \"^$w|^ *$w *[:：-]\" ARY_pages.txt | head -2; done; grep -n -i -E \"^(BIMAR|GOMAN|GOVAH|BIST|GOSTAX|GOSTAKH|GOZIDAN)\" ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:10:51.019Z] TOOL RESULT

```
## بیمار
## گمان
## گواه
## بیست
4137:بیست / ۱۴۳
## گستاخ
## گزیدن
```


## [2026-10-17T00:10:53.155Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 4125,4150p ARY_pages.txt; grep -n \"BIMAR\\|BIST\\|GOMAN\\|GOVAH\" ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:10:53.707Z] TOOL RESULT

```
آلمانی کهن (/(028014 0[4اتز صاه): 3 (810) :0/708
,8107۸ 9 (8(0) ,752 (8178101) +57
آلمانی (087/4۸0۷): ۰ 818788 ,817780 فرهنگ معین + ۶۱
انگلیسی کهن (#ا5ل0 2 صا۵): ,8500۸0 لغت‌نامه دهخدا: ۶۳
3
بادداشت:
۱ پیگیری واجريشه‌ها و واژه‌های فهرست فوق احتمالی است و واژه‌ی "شاید" که در صدر فهرست بکار رفته باید
شامل همه‌ی واژه‌های فهرست(به جز پهلوی) گردد.
۲- 8۸182015۸87 واجریشه‌های 8711001*, 813817011* را به طور توام داده است ولی 07۳0و دیگران
آنها را جداگانه داده‌اند.
[pdf page 142]
۹
بیست / ۱۴۳
ٍ
ٍ
اوستایی (487۷): ۳ آلمانی (052701۸۷): نان
پهلوی (/ا3ل۸): 7 ,۷۷181 انگلیسی کهن (8:0/37 ۵۵): 1۷78۸۲۲16 :
اوستی (0535716): 150 انگلیسی (5/4لا8(/0): دنا ردب ۱
کردی (80[87(): 57 دانمارکی (0۸(۷188): 7۳2 1
تخاری ۸ (۸ فلا 707۸): اه انا نروژی ((4ا۸08۲۷80: 7۷83۲08 ب8لا[7
تخاری 8 (8 (7۸۸ل705). لد۱4 هلندی (7ع776ا0): . نیا نان ها ۷
سانسکریت (5(/5777): 1 لهستانی (0./380): 2۲7۸371850۸
ری ((۸۵/5(/1): 8۸ چکه (280/7)): 2۸7
برنانی 08820): ۱ 81613087 ,ق080۸ اسلواکی (5]0(40): لا را
لانین نس سس یه دنا ایرلندی کهن (4ل1873 010): ای دا
فرانسه (۱)۳۴۵۸/677 ادا زاین ی ان
1911:“de AT BIST 9 AS go 2 Sls cal oe
4050:q TYVE (DANISH) Sails BIST (KURDISH) «53,5
4089:BITIES BIJUOS, BISTUOS PIGOS, PIGON —(.y\t)(GREEK) sli»
4794:PIERS. _ (POLISH) gd BISTAN, PESIR (KURDISH) 53,5
```


## [2026-10-17T00:11:10.910Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; python3 - <<'EOF'\nimport json\nok=[]\nfor l in open('index.jsonl'):\n    try: j=json.loads(l)\n    except: continue\n    if 'page 553' in (j.get('note') or ''): print(j.get('status'), j.get('bytes'), j['url'])\nEOF"
}
```


### [2026-10-17T00:11:11.549Z] TOOL RESULT

```
200 6738 https://en.wiktionary.org/wiki/گزاردن
200 5633 https://en.wiktionary.org/wiki/گزارش
200 3491 https://en.wiktionary.org/wiki/ناگزیر
200 8598 https://en.wiktionary.org/wiki/وزیر
200 9865 https://en.wiktionary.org/wiki/گستردن
200 8148 https://en.wiktionary.org/wiki/بستر
200 5197 https://en.wiktionary.org/wiki/گستاخ
200 9157 https://en.wiktionary.org/wiki/گسستن
-1 39 https://en.wiktionary.org/wiki/گسیختن
200 2885 https://en.wiktionary.org/wiki/گسیل
200 12566 https://en.wiktionary.org/wiki/گشادن
200 14577 https://en.wiktionary.org/wiki/گشودن
200 6560 https://en.wiktionary.org/wiki/بیمار
200 6018 https://en.wiktionary.org/wiki/ویراستن
200 4300 https://en.wiktionary.org/wiki/گمان
-1 39 https://en.wiktionary.org/wiki/گماردن
200 14540 https://en.wiktionary.org/wiki/گماشتن
200 4753 https://en.wiktionary.org/wiki/گواه
200 4007 https://en.wiktionary.org/wiki/گریختن
200 6227 https://en.wiktionary.org/wiki/بیست
200 11406 https://en.wiktionary.org/wiki/گذشتن
200 11768 https://en.wiktionary.org/wiki/گذاشتن
200 5461 https://en.wiktionary.org/wiki/گزیدن
200 3343 https://en.wiktionary.org/wiki/گزند
-1 39 https://en.wiktionary.org/wiki/گمیز
200 9988 https://en.wiktionary.org/wiki/آمیختن
200 9622 https://en.wiktionary.org/wiki/وزير
-1 39 https://www.etymonline.com/word/vizier
200 6297 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wí
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wi
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wíHcati
```


## [2026-10-17T00:14:14.240Z] TOOL CALL #84: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553/build-553.py",
 "content": "import json\nW = \"https://en.wiktionary.org/wiki/\"\nNS = lambda ref, note=\"no online or local copy of this page consulted\": {\"ref\": ref, \"status\": \"not_checked\", \"note\": note}\n\nnodes = []\n\nnodes.append(dict(\n id=1, lang=\"Avestan / Old Persian\", words=\"wi, vî 2, vi 3\", verdict=\"confirmed\",\n derivation=\"The Indo-Iranian preverb *wi- 'apart, asunder, away' (PIE *wi-) is attested as Avestan vī-, vi- (used as a preverb and as an adverb/preposition 'apart; away from; against'), Old Persian vi- (in vi-kan- 'dig apart, destroy', vi-jan-, vi-tar- 'go across', vi-mard-) and Sanskrit vi-. The glosses 'apart, away, opposite' match Bartholomae's and Kent's 'auseinander; abseits; entgegen' / 'away, apart'. In Middle Persian the preverb appears as wi-/gu- and in New Persian regularly as gu-/go- (gostardan, gozīdan, gomān), which is the basis of the whole chart.\",\n derivation_fa=\"پیشوند هندوایرانی *wi- «جدا، از هم، دور» (از هندواروپایی آغازین *wi-) در اوستایی به صورت vī- / vi- و در پارسی باستان به صورت vi- (در vi-kan- «کندن و ویران کردن»، vi-tar- «گذشتن») و در سنسکریت vi- آمده است. همین پیشوند در فارسی میانه wi- است و در فارسی نو به قاعده «گُ» شده، چنان‌که در «گستردن، گزیدن، گمان». ادعای نورایی درست است.\",\n sources=[W+\"Reconstruction:Proto-Indo-European/wí\"],\n ref_check=[\n  {\"ref\":\"POK:1175\",\"status\":\"supports\",\"note\":\"POK_full.txt l.92954ff. 'Root / lemma: ui-1 ... Meaning: separate from; both, two ... Material: Old Indic vi- apart, Avestan vi- apart; abseits, apart, separated from; entgegen ...' Page(s): 1175-1176.\"},\n  {\"ref\":\"KNT:204\",\"status\":\"supports\",\"note\":\"KNT_full.txt l.28946 'vi- prefix ‘away, apart’: Av. vi, Skt. vi; with verbal roots kan-, jan-, tar-, naθ-, mard-'.\"}],\n consulted=[\n  {\"src\":\"WLD\",\"where\":\"Bd. I 312 (WLD_Bd1_pages.txt leaf 321)\",\"stance\":\"supports\",\"note\":\"'ui- „auseinander“. Ai. vi „auseinander“, av. vi- „auseinander; abseits, getrennt von; ent-[gegen]“'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins s.v. wi- (AHD_watkins1985.txt l.1167)\",\"stance\":\"supports\",\"note\":\"'wi-. Apart, in half. ... [Pok. 1. wi- 1175.]'\"},\n  {\"src\":\"BRT\",\"where\":\"BRT.txt (grep vī-)\",\"stance\":\"silent\",\"note\":\"OCR of the vī- article is too damaged to quote; no contrary statement found.\"}]))\n\nnodes.append(dict(\n id=2, lang=\"Avestan\", words=\"vî-čira, vîčâra; wi-čâr\", verdict=\"plausible\",\n derivation=\"Avestan vīčira- 'deciding, arbiter, judge' is a real word (Bartholomae, quoted by Horn no. 1084 'aw. vīčira- Entscheider' and by Mo'in 'دراوستا vîcîra بمعنی فتوی دهنده'); it is vi- + a derivative of čar-/kar- 'move, turn', i.e. 'one who separates (cases)'. 'vîčâra' is not Avestan but the Sanskrit noun vicāra- 'deliberation' (Skt vi-car- caus. 'to consider'), which Horn and Mo'in quote as a cognate; the language label is therefore loose for that form. 'wi-čâr' = Av. vi-čar- 'to move about' (Nyberg: 'Av. vi-kar- to move about; Skr vi-car- to go apart, to spread'), whose causative *wi-čāraya- is the source of MP wizārdan/NP gozārdan (Cheung s.v. *čarH). The derivations are correct; only the labelling of vīčāra as Avestan is inaccurate.\",\n derivation_fa=\"اوستایی vīčira- «داور، داوری‌کننده» واژه‌ای واقعی است و از پیشوند vi- و ریشهٔ čar- «گشتن، جنبیدن» ساخته شده، یعنی «کسی که کارها را از هم جدا و داوری می‌کند». اما vīčāra اوستایی نیست و واژهٔ سنسکریت vicāra- «سنجش، تأمل» است که هرن و معین آن را هم‌ریشه آورده‌اند. wi-čār همان اوستایی vi-čar- «این سو و آن سو رفتن» است که سببی آن، *wi-čāraya-، به فارسی میانه wizārdan و فارسی «گزاردن» رسیده است. ریشه‌شناسی درست است ولی برچسب زبانی vīčāra دقیق نیست.\",\n sources=[W+\"وزير\", W+\"گزاردن\"],\n ref_check=[{\"ref\":\"HRN:205\",\"status\":\"supports\",\"note\":\"HRN p.204-205 no. 917 'guzārden ... skr. vi + car-, Caus. erwägen, in Betracht ziehen, prüfen; phlv. v(i)cārtan' and no. 1084 (p.243) 'aw. vīčira- Entscheider; phlv. v(i)čīr Entscheidung; Entscheider, Richter'.\"}],\n consulted=[\n  {\"src\":\"NYB\",\"where\":\"Part II, s.v. vi-car- (NYB_vol2_glossary.txt l.4113) and vicīr (l.4123)\",\"stance\":\"supports\",\"note\":\"'vi-car- pres. to get on, to get through ... — Av. (450) vi-kar- to move about; Skr car- to move, vi-car- to go apart'; 'vicīr decision ... — From vi-car-'.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *čarH\",\"stance\":\"supports\",\"note\":\"'(+ *ui-) NP guzārdan/guzār- to accomplish, perform; to pay; to explain, interpret, Kurd. bzartin'.\"},\n  {\"src\":\"BQT\",\"where\":\"p.2258 n.5 (Mo'in)\",\"stance\":\"supports\",\"note\":\"'دراوستا vîcîra بمعنی فتوی دهنده است. ازهمین لغت است کلمهٔ «وزیر»'.\"}]))\n\nnodes.append(dict(\n id=3, lang=\"Pahlavi\", words=\"vičir; wi-zârišn\", verdict=\"confirmed\",\n derivation=\"Book Pahlavi wcyl = wizīr (older reading vičīr) 'decision, judgement' (MacKenzie), Nyberg vicīr 'decision', from OIr *wi-čīra- (Av. vīčira-); Horn gives both senses 'Entscheidung; Entscheider, Richter'. wizārišn 'decision; explanation, redemption' is the action noun of wizārdan, wizār- 'separate; explain, interpret; perform, fulfil' < *wi-čāraya-. Intervocalic OIr -č- became MP -z- (wizīr, wizār-), whence NP guzīr, guzār-. Nourai's glosses ('judge'; 'to do, to translate') are free renderings of 'decision' and 'explanation/performance' but the forms and descent are right.\",\n derivation_fa=\"پهلوی wizīr (خوانش کهن‌تر vičīr) «داوری، فیصله» در مکنزی و نیبرگ آمده و از ایرانی باستان *wi-čīra- (اوستایی vīčira-) است. wizārišn «گزارش، تفسیر، فیصله» اسم مصدر از wizārdan «جدا کردن، شرح دادن، به جای آوردن» است که از سببی *wi-čāraya- آمده. چ میان دو واکه در فارسی میانه به ز بدل شده و از همین‌جا «گزیر» و «گزار» فارسی پدید آمده‌اند. معنی‌هایی که نورایی داده آزادانه است ولی صورت‌ها و پیوندها درست است.\",\n sources=[W+\"گزاردن\", W+\"وزير\"],\n ref_check=[NS(\"FFD:73\",\"FFD p.73 (pdf 78) covers the NP verbs (گزاردن < MP wizārd- < OIr *vi-čāra-), not a Pahlavi lemma vičir; see node 4. The Pahlavi forms themselves were checked in PHD/NYB.\")],\n consulted=[\n  {\"src\":\"PHD\",\"where\":\"s.v. wizīr, wizārdan (PHD.txt)\",\"stance\":\"supports\",\"note\":\"'wizir [wcyl] decision, judgement'; 'wizārdan, wizār- [wcʾl-tn' | M wycʾrd, N guzārdan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption'.\"},\n  {\"src\":\"NYB\",\"where\":\"Part II p.211 s.v. vicīr (NYB_vol2_glossary.txt l.4123)\",\"stance\":\"supports\",\"note\":\"'vicīr [wcyl] decision ... — From vi-car-'.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 1084, p.243\",\"stance\":\"supports\",\"note\":\"'phlv. v(i)čīr Entscheidung; Entscheider, Richter; arm. LW. včir Entscheidung'.\"}]))\n\nnodes.append(dict(\n id=4, lang=\"Persian\", words=\"vačar; vačargar; gozârdan\", verdict=\"plausible\",\n derivation=\"gozārdan 'to perform, pay, explain, translate' < MP wizārdan < OIr *wi-čāraya- (causative of *čar- 'move'), with OIr wi- > NP gu- and intervocalic č > z; gozāreš < MP wizārišn; gozīr 'remedy' and nāgozīr 'inevitable' < MP wizīr/a-wizīrīg (*wi-čīra-). These are confirmed by MacKenzie, Horn, Cheung and Abolghasemi. vačar 'fatwa, judgement' and vačargar 'mufti, judge' are dictionary words (Borhan; one verse of Labibi) that Mo'in links to Av. vīčira-/Pahlavi wcyl; Horn calls vecer 'unbelegt'. Their -č- and a-vocalism do not follow the regular NP development (which gives gozīr), so they are best taken as learned readings of the Pahlavi spelling wcyl/wcl rather than inherited forms. The family relationship is right; the inherited status of vačar is doubtful.\",\n derivation_fa=\"«گزاردن» از فارسی میانه wizārdan و آن از سببی ایرانی باستان *wi-čāraya- (از ریشهٔ čar- «جنبیدن») است؛ پیشوند wi- در فارسی به «گُ» و چ میانی به ز بدل شده. «گزارش» از wizārišn و «گزیر/ناگزیر» از wizīr پهلوی است. اما «وَچَر» و «وَچَرگر» واژه‌های فرهنگی‌اند (برهان قاطع و یک بیت لبیبی) که معین آن‌ها را با اوستایی vīčira- و پهلوی wcyl پیوند داده؛ صورت آوایی آن‌ها با تحول قاعده‌مند (که «گزیر» به دست می‌دهد) نمی‌خواند و به احتمال زیاد خوانش کتابی همان املای پهلوی است. پیوند خانوادگی درست است ولی موروثی بودن «وچر» محل تردید است.\",\n sources=[W+\"گزاردن\", W+\"گزارش\", W+\"ناگزیر\"],\n ref_check=[\n  {\"ref\":\"BQT:1809\",\"status\":\"supports\",\"note\":\"BQT p.1809 (pdf 606; 1809.vision.txt) n.2 on گزاردن: 'جزء اول vi + câr (شرح کردن، توضیح دادن)، سانسکریت vicârayati ... پهلوی vicârishn «نیبرگ ص ۲۴۱-۲۴۲»، vicârtan «اشتق ۹۱۷»'.\"},\n  {\"ref\":\"BQT:2258\",\"status\":\"supports\",\"note\":\"BQT p.2258 (2258.vision.txt): 'وچرگر - ... مفتی و فتوی دهنده'; n.5 'دراوستا vîcîra بمعنی فتوی دهنده است ... در فرهنگها لغات «وجر» و «وجارش» و «وجرگر» بمعانی گزاره یا گزارش ... وفتوی دهنده یا مفتی ضبط شده'.\"},\n  NS(\"MON:4988\",\"Mo'in Farhang page 4988 (vol. 4/5 range) not checked; MON_part1/2 OCR not searched for this page.\")],\n consulted=[\n  {\"src\":\"PHD\",\"where\":\"s.v. wizārdan\",\"stance\":\"supports\",\"note\":\"'wizārdan, wizār- ... N guzārdan ... ~išn: decision; redemption'.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 917, p.204\",\"stance\":\"supports\",\"note\":\"'guzārden auseinander setzen, darlegen, bezahlen; guzāriš ...; vergl. vecer (vejer) richterliche Entscheidung (unbelegt)'.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *čarH\",\"stance\":\"supports\",\"note\":\"'(+ *ui-) NP guzārdan/guzār- ... to explain, interpret'.\"},\n  {\"src\":\"FFD\",\"where\":\"p.73 (pdf 78)\",\"stance\":\"supports\",\"note\":\"OCR: 'گزاردن — گزارد < فارسی میانه wizārd < ایرانی باستان *vi-čār-ta-; vi پیشوند فعلی است؛ čār صورت بالاندهٔ ریشهٔ čar به معنی «حرکت کردن» است'.\"}]))\n\nnodes.append(dict(\n id=5, lang=\"Arabic\", words=\"vazîr\", verdict=\"plausible\",\n derivation=\"Arabic wazīr (Qur'an 20:29, 25:35, of Aaron as Moses' helper; political 'minister' only from the Umayyad/Abbasid period). Two explanations compete: (a) native Arabic faʿīl from w-z-r 'to carry a burden' ('one who bears the prince's burden'), the traditional Arab view (Skeat); (b) a loan from Middle Persian wizīr/vičīr 'decision; arbiter' < Av. vīčira-, proposed by Lagarde and Bartholomae and accepted by Horn, Jeffery, Klein and Mo'in; Wiktionary today says 'likely borrowed from an Iranian term surfacing as MP vičīr'. Nourai follows (b); it is a respectable but not unanimous view, hence plausible.\",\n derivation_fa=\"عربی «وزیر» در قرآن (طه ۲۹، فرقان ۳۵) به معنی «یاور» هارون آمده و معنی سیاسی آن بعدها پدید آمد. دو نظر هست: یکی آن‌که عربی اصیل بر وزن فعیل از ریشهٔ و-ز-ر «بار برداشتن» است؛ دیگر آن‌که از پهلوی wizīr / vičīr «داوری، داور» و اوستایی vīčira- وام گرفته شده (لاگارد، بارتولومه، هرن، جفری، کلاین و معین). ویکی‌واژه هم وام‌گیری از ایرانی را محتمل می‌داند. نظر نورایی با احتیاط پذیرفتنی است، ولی همهٔ پژوهشگران آن را نمی‌پذیرند.\",\n sources=[W+\"وزير\"],\n ref_check=[{\"ref\":\"KLN:1718\",\"status\":\"supports\",\"note\":\"Klein s.v. vizier (KLN_1971.txt l.263376; = KLN 1966 p.1718): 'vizier ... fr. Arab. wazīr ..., fr. Avestic vicira, arbitrator, judge ... The Arabic word was re-borrowed by the Persians'.\"}],\n consulted=[\n  {\"src\":\"FVQ\",\"where\":\"pp.287-288 s.v. Wazīr (FVQ_pages.txt l.10318-10348)\",\"stance\":\"supports\",\"note\":\"'The usual explanation ... from w-z-r to bear or carry ... Lagarde ... derives it from the Phlv. vcīr ... This word, of course, is good Iranian, being from the Av. vicira meaning deciding ... The borrowing was doubtless direct from the Middle Persian'.\"},\n  {\"src\":\"SKT\",\"where\":\"s.v. vizier (SKT.txt l.20986)\",\"stance\":\"contradicts\",\"note\":\"'Arab. wazir, a counsellor of state; orig. a porter, one who bears the burden of state affairs — Arab. root wazara, to bear a burden'.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 1084, p.242-243\",\"stance\":\"supports\",\"note\":\"'vezīr (arab. LW.) Vezir ... aw. vīčira- Entscheider; phlv. v(i)čīr'.\"}]))\n\nnodes.append(dict(\n id=6, lang=\"Persian\", words=\"vazîr\", verdict=\"confirmed\",\n derivation=\"NP vazīr 'minister, vizier' is borrowed from Arabic wazīr (Wiktionary, Horn 'arab. LW.'), so if (b) in node 5 is right it is a Persian → Arabic → Persian round-trip; the inherited Persian reflex of the same MP word is gozīr/gizīr (village headman, Mo'in). From Persian/Ottoman vezir come English vizier, Spanish alguacil (al-wazīr).\",\n derivation_fa=\"فارسی «وزیر» از عربی «وزیر» وام گرفته شده است. اگر عربی خود از پهلوی wizīr آمده باشد، این واژه رفت‌وبرگشتی است: از فارسی میانه به عربی و دوباره از عربی به فارسی. بازماندهٔ موروثی همان واژهٔ پهلوی در فارسی «گُزیر / گِزیر» (کدخدا، محصل مالیات) است. انگلیسی vizier و اسپانیایی alguacil هم از همین واژه آمده‌اند. ادعای نورایی درست است.\",\n sources=[W+\"وزیر\", W+\"وزير\"],\n ref_check=[{\"ref\":\"BQT:2279\",\"status\":\"supports\",\"note\":\"BQT p.2279 (2279.vision.txt): 'وزیر - ... وبا ثالث معروف درعربی بمعنی دستور باشد'; n.7 'کلمه معرب است «اشتق ۱۰۸۴» از vicîr (یا vajîr) پهلوی ... از اوستایی vîcira فتوی دهنده ... ارمنی vcir، نیز ارمنی gzir = فارسی gizîr'.\"}],\n consulted=[\n  {\"src\":\"HRN\",\"where\":\"no. 1084, p.242\",\"stance\":\"supports\",\"note\":\"'vezīr (arab. LW.) Vezir; Gelehrter, gezīr, gizīr'.\"},\n  {\"src\":\"KLN\",\"where\":\"s.v. vizier\",\"stance\":\"supports\",\"note\":\"'The Arabic word was re-borrowed by the Persians under the Ommiads'.\"}]))\n\nnodes.append(dict(\n id=7, lang=\"Avestan\", words=\"vi-stâr; vi-stâka; vi-saëd; vi-šâ, vi-sâ, vi-hây\", verdict=\"plausible\",\n derivation=\"vi-star- 'spread out' = Av./Skt vi + star- (PIE *sterh3-), attested in Indic and well reconstructed for Iranian (Horn no. 921 'ai. vi + star- ausbreiten'). vi-stāka is not attested in Avestan: it is Horn's reconstruction *vistāka-/*vistāxva- behind MP wistāx 'bold' (Old Persian *vistāhuva- in Wiktionary/Mo'in), so Nourai's 'stand against' (from stā-) is an interpretation. vi-saēd 'cut off' is the root *said-/*sid- 'split' (PIE *skeyd-), Av. saēd-, with vi- reconstructed (Cheung *ui- + *said-). vi-šā/vi-hāy is Av. hā(y)- 'bind' with vi- 'unbind, open' (Bartholomae 1800 per Mo'in; OP/Skt vi-sā-). The preverb analyses are right, but several of the 'Avestan' compounds are reconstructions, not attested words.\",\n derivation_fa=\"vi-star- «گستردن» از پیشوند vi- و ریشهٔ star- (هندواروپایی *sterh3-) است و در سنسکریت گواه دارد. vi-stāka در اوستا نیامده و بازسازی هرن برای پهلوی wistāx «گستاخ» است (ویکی‌واژه و معین آن را پارسی باستان *vistāhuva- می‌دانند). vi-saēd از ریشهٔ *said- «شکافتن» با پیشوند vi- است و vi-hāy / vi-šā «گشودن» از hā(y)- «بستن» با پیشوند vi- به معنی «باز کردن». تحلیل پیشوندی درست است، اما چند صورتِ «اوستایی» در متن‌ها نیامده و بازسازی است؛ پس ادعا با احتیاط پذیرفتنی است.\",\n sources=[W+\"گستردن\", W+\"گستاخ\", W+\"گسستن\", W+\"گشودن\"],\n ref_check=[{\"ref\":\"HRN:205\",\"status\":\"supports\",\"note\":\"HRN p.205 nos. 920-923: 'gustāx ... aw. *vistāka-, vergl. staxra-'; 'gusterden ausbreiten ... ai. vi + star-'; 'gusisten ... aw. saēd-, hisiδyāt'; 'gušāden öffnen ... phlv. v(i)šātan' (Bartholomae: vi + šā-/sā-).\"}],\n consulted=[\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *star, *said\",\"stance\":\"supports\",\"note\":\"'(+ *ui-) NP gustardan/gustar- to spread'; '(+ *ui-) NP gusistan (supplet. gusil-) to shatter, break'.\"},\n  {\"src\":\"BRT\",\"where\":\"BRT.txt (grep vī-star/vī-hā)\",\"stance\":\"silent\",\"note\":\"OCR too noisy to locate the vī- compounds; Mo'in (BQT 1818) cites 'اوستایی hây + vi «بارتولمه ۱۸۰۰»'.\"}]))\n\nnodes.append(dict(\n id=8, lang=\"Persian\", words=\"gostardan; gostâx; gosastan; gošâdan\", verdict=\"plausible\",\n derivation=\"gostardan (gostareš) < MP wistardan, wistar- < *wi-starnā- 'spread' — confirmed. bestar 'bed' (given in parentheses) continues MP wistar(ag) 'bedding' per MacKenzie and Horn (vi- + star-), but Wiktionary and Cheung prefer *abi-/*upa- + star-; either way it is from star- 'spread'. gostāx 'bold, rude' < MP wistāx 'confident, bold' (Arm. loan vstah) < *vi-stāxva-, with the meaning 'bold' > 'insolent'. gosastan/gosestan (gosīxtan) < MP wisistan, wisin- < *wi-said- 'split apart' (Cheung); gosīl 'dispatch' got its -l from the present stem gosil- (Wiktionary). gošādan < MP wišādan < *wi-šā- 'unbind' (Av. hā(y)-/Skt sā- 'bind'). All show OIr *wi- > MP wi- > NP gu-/go-.\",\n derivation_fa=\"«گستردن» و «گسترش» از فارسی میانه wistardan و آن از *wi-star- «پهن کردن» است. «بستر» به گفتهٔ مکنزی و هرن از پهلوی wistar «بستر، رختخواب» است، ولی ویکی‌واژه و چونگ آن را از پیشوند *abi- / *upa- با همان ریشهٔ star- می‌دانند. «گستاخ» از پهلوی wistāx «دلیر، بی‌پروا» است. «گسستن / گسیختن» از پهلوی wisistan و ایرانی باستان *wi-said- «از هم شکافتن» است، و «گسیل» ل خود را از ستاک مضارع «گسل» گرفته. «گشادن» از wišādan و *wi-šā- «باز کردن بند» است. در همهٔ این‌ها wi- به «گُ» بدل شده. جز تردید در «بستر»، ادعای نورایی درست است.\",\n sources=[W+\"گستردن\", W+\"بستر\", W+\"گستاخ\", W+\"گسستن\", W+\"گسیل\", W+\"گشودن\"],\n ref_check=[\n  {\"ref\":\"BQT:1816\",\"status\":\"supports\",\"note\":\"BQT p.1816 (pdf 613; 1816.vision.txt): n.1 gostāx 'پهلوی vistâxv، ارمنی vstah ... پارسی باستان vistâ(h)uva-? «هوبشمان ۹۲۰»'; n.6 gostardan 'قس: بستر. هندی باستان vi+star (پهن کردن)، پهلوی v(i)startan'; gosastan 'از ریشهٔ اوستایی sid = سانسکریت chid ... پهلوی v(i)sastan'.\"},\n  {\"ref\":\"BQT:1818\",\"status\":\"supports\",\"note\":\"BQT p.1818 (pdf 615; 1818.vision.txt) n.5 گشادن: 'پهلوی vishâtan (آزاد کردن، باز کردن)، سانسکریت vi-sâ ... اوستایی hây + vi «بارتولمه ۱۸۰۰»'.\"},\n  {\"ref\":\"BQT:1800\",\"status\":\"not_found\",\"note\":\"Printed p.1800 (pdf 597, read from image) has گرگوی، گرم، گرمابه — none of this node's words; probably a misprint for another page.\"}],\n consulted=[\n  {\"src\":\"PHD\",\"where\":\"s.v. wistardan, wistāx, wisistan, wišādan, wistar(ag)\",\"stance\":\"supports\",\"note\":\"'wistardan, wistar- [wstl-tn' | N gustardan] spread. wistāx [... | N gustāx, bistāx] confident, bold'; 'wisistan, wisin(n)- [... | N gusistan, (gusil-)] break, split'; 'wišādan ... N gušādan, gušāy- open, loose, free'; 'wistar(ag) ... N bistar bedding, cover'.\"},\n  {\"src\":\"HRN\",\"where\":\"nos. 218, 920-923, pp.205-206\",\"stance\":\"supports\",\"note\":\"'bister Lager ... vi + star- ausbreiten'; 'gustāx kühn, frech ... phlv. v(i)stāx'; 'gusisten zerbrechen, trennen ... phlv. v(i)sastan'; 'gušāden öffnen ... phlv. v(i)šātan'.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *star\",\"stance\":\"partial\",\"note\":\"'(+ *abi- ?) NP bistar ... bed, mattress || (+ *ui-) NP gustardan/gustar- to spread' — bistar not from *ui-.\"},\n  {\"src\":\"FFD\",\"where\":\"pp.73-74 (pdf 78-79)\",\"stance\":\"supports\",\"note\":\"OCR: gostardan < MP wistard < OIr *vi-star-; gosastan < MP wisist < *vi-sid-; 'گشادن، گشودن — گشاد < فارسی میانه wišād < ایرانی باستان *vi-šā-ta-؛ vi پیشوند فعلی است ... ریشهٔ sā به معنی «بستن»'.\"}]))\n\nnodes.append(dict(\n id=9, lang=\"Avestan\", words=\"vi-mad; vi-radh, vi-raiti; vi-manah; vi-mar\", verdict=\"plausible\",\n derivation=\"vi-manah- 'doubt' is attested (Av. vīmanō, Skt vimanas-; Wiktionary, Horn 'aw. vīmanah- Zweifel'). vi-rad-/vi-rāy- 'arrange' (root rād-/rāz- 'arrange, prepare') with vi- underlies MP wirāstan/wirāy- (Parthian wirāz-), so 'vi-radh' is a fair reconstruction though Nourai's gloss 'set separate' is etymologising. vi-mar 'designate' is a reconstruction: Horn derived gumāštan from *vi-smar- 'forget' (unsicher), Hübschmann rejected it, and Cheung puts MP gumār- under *marH 'to block, hinder' + *ui-, so the preverb is right but the root and meaning differ. vi-mad 'to cure' (from mad- 'measure, heal') is not a recognised source of NP bīmār (see node 10).\",\n derivation_fa=\"vi-manah- «تردید» در اوستا (vīmanō) و سنسکریت (vimanas-) گواه دارد. vi-rad- از ریشهٔ rād- / rāz- «آراستن» با پیشوند vi- ساخته شده و پشتوانهٔ پهلوی wirāstan است؛ معنی «جدا نهادن» که نورایی داده تفسیر خود اوست. vi-mar «گماشتن» بازسازی است: هرن آن را از *vi-smar- «فراموش کردن» می‌دانست و هوبشمان این را رد کرد. چونگ «گماردن» را از *marH «بازداشتن» با پیشوند *ui- می‌گیرد، پس پیشوند درست است ولی ریشه دیگر است. vi-mad «درمان کردن» هم سرچشمهٔ پذیرفته‌ای برای «بیمار» نیست.\",\n sources=[W+\"گمان\", W+\"ویراستن\", W+\"گماشتن\"],\n ref_check=[{\"ref\":\"HUB:95\",\"status\":\"partial\",\"note\":\"HUB p.95 no. 931: 'Np. gumāštan = pāz. gumārdan = phl. gumārtan ... zeigt nirgends den Anlaut v- und hat jedenfalls mit ap. *vi-mar = skr. vi-smar nichts zu thun' (rejects vi-mar); no. 932 'Np. gumān = ap. *vimāna- (statt zd. *vīmanah-)' (supports vi-manah).\"}],\n consulted=[\n  {\"src\":\"HRN\",\"where\":\"nos. 931-932, p.207\",\"stance\":\"partial\",\"note\":\"'gumāšten vertrauen, übergeben ... ap. *vi + mar- mit Bedeutungswechsel, vergl. skr. vi + smar- vergessen ... Unsicher'; 'gumān Zweifel; Meinung. aw. *vīmanah- Zweifel'.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *marH 'to block, hinder'\",\"stance\":\"partial\",\"note\":\"'(+ *ui-) MMP gwmʾr- to appoint, BMP gwmʾl- /gumār-/ to appoint, entrust, commission ... NP gumāštan/gumār-'.\"},\n  {\"src\":\"BRT\",\"where\":\"BRT.txt grep vīmanah/vīmaδ\",\"stance\":\"silent\",\"note\":\"OCR did not yield the entries.\"}]))\n\nnodes.append(dict(\n id=10, lang=\"Persian\", words=\"bîmâr; vîrâstan; gomân; gomârdan\", verdict=\"disputed\",\n derivation=\"gomān 'doubt, guess' < MP gumān < *wi-manah- 'thinking apart' — confirmed (Horn, Hübschmann, Nyberg, Cheung, Wiktionary). vīrāstan 'edit' (vīrāstār is a 20th-c. coinage) < MP wirāstan, wirāy- 'arrange, prepare' (MacKenzie, Wiktionary); the v- instead of gu- shows it is a learned/literary continuation of the MP form, so the vi- analysis is right. gomārdan/gomāštan 'appoint' < MP gumārdan < *wi-māraya-, but the root is *marH 'hinder' (Cheung) and Hübschmann denies the vi-mar 'designate' etymology: plausible at best. bīmār 'sick' < MP wēmār (wymʾl): Horn already pointed out that old vi- regularly gives NP gu- and that the ī is unexplained, so *vi-mad- 'cure' is phonetically impossible; Wiktionary connects wēmār with *wemh1- 'vomit'. bīmār is therefore disputed.\",\n derivation_fa=\"«گمان» از فارسی میانه gumān و ایرانی باستان *wi-manah- «اندیشهٔ دوسویه، تردید» است و درست است. «ویراستن» از پهلوی wirāstan «آراستن، آماده کردن» است. ماندن «و» به جای «گ» نشان می‌دهد که صورتی ادبی و کتابی است، و «ویراستار» ساختهٔ سدهٔ اخیر است. «گماردن / گماشتن» از پهلوی gumārdan است، ولی چونگ ریشهٔ آن را *marH «بازداشتن» می‌داند و هوبشمان پیوند آن با vi-mar را رد کرده. «بیمار» از پهلوی wēmār است. هرن یادآور شده که vi- کهن در فارسی همیشه «گُ» می‌شود و «ی» آن هم توضیحی ندارد، پس ریشه‌شناسی *vi-mad- «درمان» پذیرفتنی نیست. ویکی‌واژه آن را با *wemh1- «قی کردن» می‌سنجد. پژوهش امروزی این بخش از ادعای نورایی را رد می‌کند.\",\n sources=[W+\"بیمار\", W+\"ویراستن\", W+\"گمان\", W+\"گماشتن\"],\n ref_check=[\n  NS(\"BQT:437\",\"BQT vol. 1-2 printed p.437 (بیمار) lies in vol. 1, where the OCR text has no reliable page mapping; ref_page.py reports no scan for this page.\"),\n  NS(\"BQT:834\",\"BQT printed p.834 (vol. 2) — ref_page.py reports no scan; not checked.\")],\n consulted=[\n  {\"src\":\"HRN\",\"where\":\"no. 39 (bīmār), p.? ; nos. 931-932\",\"stance\":\"contradicts\",\"note\":\"No. 39 'bīmār krank ... aw. vi + mar- ...; phlv. vimār ... Die Etymologie ist gewiss falsch, da altes vi- im Neupersischen consequent zu gu- wird, und ... das ī völlig unerklärt bliebe'.\"},\n  {\"src\":\"PHD\",\"where\":\"s.v. wēmār, wirāstan\",\"stance\":\"partial\",\"note\":\"'wēmār [wymʾl | M wymʾr, N bēmār] ill, sick' (wē-, not wi-); 'wirāstan, wirāy-, (P wirāz-) ... arrange, prepare, cultivate, restore'.\"},\n  {\"src\":\"NYB\",\"where\":\"Part II s.v. gumān, gumārtan (l.1733-1735)\",\"stance\":\"supports\",\"note\":\"'gumān doubt ... = NP'; 'gumārtan to entrust a p. with ... NP gumāštan gumār-' (no etymology for gumārtan).\"},\n  {\"src\":\"HUB\",\"where\":\"p.95 nos. 931-932\",\"stance\":\"partial\",\"note\":\"rejects *vi-mar for gumāštan; supports *vimāna- for gumān.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *man, *marH\",\"stance\":\"supports\",\"note\":\"'(+ *ui-) NP gumān doubt; belief, opinion'; gumāštan under *marH.\"}]))\n\nnodes.append(dict(\n id=11, lang=\"Avestan\", words=\"vi-kâs; vi-raeč; vi-saiti; vi-tar\", verdict=\"plausible\",\n derivation=\"vi-raēk- 'leave, run away' (Av. raēk- 'leave', PIE *leikʷ-; Wiktionary cites Av. virāec 'leave away, run away') and vi-tar- 'go across' (Av. vītar-, OP vi-tar-, Skt vi-tar-) are correct; note that the root is *leikʷ- 'leave', not a 'leap' root. vi-kās- 'look out, perceive' is Skt vi + kāś- (Horn no. 940) reconstructed for Iranian (PIE *kʷek- 'see'). vīsaiti 'twenty' is a real Avestan word but not vi- + saiti: it is the dual compound PIE *(d)wi-dḱm̥ti 'two tens' (Pokorny lists it as a separate lemma 'uī-k̂m̥tī ... Dual two decades, to IE ui- two'); whether *wi- 'apart' itself goes back to *dwi- 'two' is debated (Wiktionary: 'likely from *dwi-').\",\n derivation_fa=\"vi-raēk- «رها کردن، گریختن» از ریشهٔ اوستایی raēk- «ترک کردن» (هندواروپایی *leikʷ-) و vi-tar- «گذشتن» (اوستایی، پارسی باستان و سنسکریت) درست‌اند. vi-kās- «دیدن و تشخیص دادن» از سنسکریت vi + kāś- برای ایرانی بازسازی شده است. اوستایی vīsaiti «بیست» واژه‌ای واقعی است ولی از vi- «جدا» و saiti ساخته نشده. این واژه دوگانهٔ *(d)wi-dḱm̥ti «دو ده» است و پوکورنی آن را مدخل جداگانه آورده. اینکه خود *wi- «جدا» از *dwi- «دو» آمده باشد هنوز محل بحث است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n sources=[W+\"گریختن\", W+\"گواه\", W+\"بیست\", W+\"Reconstruction:Proto-Indo-European/wí\"],\n ref_check=[\n  {\"ref\":\"POK:1176\",\"status\":\"partial\",\"note\":\"POK_full.txt l.92940ff.: vīsaiti is under the separate lemma 'uī-k̂m̥tī twenty. Note: actually Dual \\\"two decades\\\" (to Indo Germanic ui- two and dek̂m̥t-)', Page 1177; ui-1 (pp.1175-1176) itself gives 'separate from; both, two'.\"},\n  {\"ref\":\"HRN:199\",\"status\":\"supports\",\"note\":\"HRN p.199 no. 893 'gudāšten hinüberführen ... guδešten überschreiten ... ap. vi + tar-, viyatarayāma wir überschritten; phlv. v(i)tārtan, v(i)tartan'.\"},\n  {\"ref\":\"HRN:203\",\"status\":\"supports\",\"note\":\"HRN p.203 no. 914 'gurēxten fliehen ... skr. vi + rec- ... vergl. aw. raēcayeinti (paiti) sie verlassen ... phlv. v(i)rēxtan'.\"}],\n consulted=[\n  {\"src\":\"WLD\",\"where\":\"Bd. I 312-313 (leaf 321-322)\",\"stance\":\"partial\",\"note\":\"'idg. *ui-kmti „zwanzig“ ... *ui- „auseinander“ nicht als „entzwei“ auf ein solches u- zu beziehen'; 'Ai. viṃśati-, av. vīsaiti'.\"},\n  {\"src\":\"KNT\",\"where\":\"lexicon s.v. vi- + tar- (KNT_full.txt l.25961)\",\"stance\":\"supports\",\"note\":\"'vi- + tar- go across, caus. put across: viyatarayāma'.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 940 (guvāh)\",\"stance\":\"supports\",\"note\":\"'ai. vi + kāś- Intens. ausschauen, erschauen, wahrnehmen; phlv. gukās Zeuge'.\"}]))\n\nnodes.append(dict(\n id=12, lang=\"Persian\", words=\"govâh; gorixtan; bîst; gozaštan\", verdict=\"plausible\",\n derivation=\"govāh 'witness' < MP gugāy (older gukās) < *wi-kāsa- 'one who looks out, discerns' (Wiktionary, Horn no. 940; Hübschmann doubts the Armenian vkay link). gorīxtan 'flee' (gorīz) < MP wirēxtan, wirēz- < *wi-raik- 'leave apart' (Horn, MacKenzie, Wiktionary, Abolghasemi; rīxtan 'pour' is the same root). gozaštan 'pass' < MP widardan/widaštan < *wi-tar- 'cross', with irregular d > δ > z (Wiktionary); gozāštan/gozārdan are causatives (MP widārdan), gozar/gozār/godār ('ford', MP widarg) and gozarnāme are derivatives. bīst 'twenty' < MP wīst < Av. vīsaiti < PIE *(d)wi-dḱm̥ti 'two tens': the descent is right, but the first element is 'two', not the preverb 'apart', and bīst shows b- (from long *wī-) rather than the gu- of the preverb. Only the 'separate tens' interpretation of bīst is doubtful.\",\n derivation_fa=\"«گواه» از پهلوی gugāy (کهن‌تر gukās) و ایرانی باستان *wi-kāsa- «کسی که می‌بیند و تشخیص می‌دهد» است. «گریختن / گریز» از پهلوی wirēxtan، wirēz- و *wi-raik- «ترک کردن» است و «ریختن» هم از همین ریشه است. «گذشتن» از پهلوی widardan / widaštan و *wi-tar- «گذر کردن» است، با دگرگونی نامنظم د → ذ → ز. «گذاشتن / گذاردن» سببی آن‌اند و «گذر، گذار، گدار، گذرنامه» از آن ساخته شده‌اند. «بیست» از پهلوی wīst و اوستایی vīsaiti است، ولی جزء نخست آن «دو» است (*dwi-) نه پیشوند «جدا»، و «ب» آغازی آن هم با «گُ» پیشوندی فرق دارد. جز تفسیر «دو دهٔ جدا» برای «بیست»، ادعای نورایی درست است.\",\n sources=[W+\"گواه\", W+\"گریختن\", W+\"بیست\", W+\"گذشتن\", W+\"گذاشتن\"],\n ref_check=[\n  {\"ref\":\"BQT:1778\",\"status\":\"supports\",\"note\":\"BQT p.1778 (pdf 575; 1778.vision.txt): گذاشتن 'پهلوی vitârtan، ارمنی vtar، هندی باستان vi+tar «اشتق ۸۹۳»'; گذشتن 'پهلوی vitashtan = vitartan، اوستا vi.tar «بارتولمه ۶۴۰، نیبرگ ۲۴۶»'.\"},\n  {\"ref\":\"BQT:1806\",\"status\":\"supports\",\"note\":\"BQT p.1806 (pdf 603; 1806.vision.txt): گریختن 'پهلوی virêxtan از virêc (فرار کردن)، از ایرانی باستان raik+vi، از raêk (linquere) «بارتولمه ۱۴۷۹» «نیبرگ ص ۲۴۴»'.\"},\n  {\"ref\":\"BQT:1776\",\"status\":\"not_found\",\"note\":\"Printed p.1776 (pdf 573, read from image) has گجیل، گچ، گچک، گدا — none of this node's words (گواه is ~p.1849).\"}],\n consulted=[\n  {\"src\":\"PHD\",\"where\":\"s.v. wirēxtan, wīst, widardan, gugāy(īh)\",\"stance\":\"supports\",\"note\":\"'wirēxtan, wirēz- ... N gurēxtan, gurēz- flee, escape'; 'wist [20; wyst | = M, N bist] twenty'; 'widardan, wider- ... N guδar- pass (by, away), cross, die'; English index 'witness gugāy'.\"},\n  {\"src\":\"HRN\",\"where\":\"nos. 254, 893, 914, 940\",\"stance\":\"supports\",\"note\":\"'bīst zwanzig. aw. vīsaiti- zwanzig; phlv. vīst'; 'guvāh Zeuge. ai. vi + kāś-'; gurēxten < vi + raik-; guδešten < vi + tar-.\"},\n  {\"src\":\"NYB\",\"where\":\"Part II p.217 s.v. vist, vitartan (l.4217, 4240)\",\"stance\":\"supports\",\"note\":\"'vist twenty'; 'vitartan ... vitaštan ... to pass'.\"},\n  {\"src\":\"HUB\",\"where\":\"p.95 no. 940\",\"stance\":\"partial\",\"note\":\"'Arm. vkay gehört nicht zu np. guvāh'.\"},\n  {\"src\":\"ARY\",\"where\":\"s.v. بیست p.143 (ARY_pages.txt l.4137, pdf 142)\",\"stance\":\"partial\",\"note\":\"entry 'بیست / ۱۴۳' lists Avestan, Pahlavi and Germanic 'twenty' cognates (OCR garbled), i.e. treats bīst under the numeral root, not under 'apart'.\"}]))\n\nnodes.append(dict(\n id=13, lang=\"Avestan\", words=\"vi-čay, vi-kay; vi-žainti; vi-maik\", verdict=\"plausible\",\n derivation=\"vi-či-/vi-kay- 'choose, discern' = Av. vī-či- (Bartholomae 441 'kay- with vī', Nyberg 'Av. (441) vi-kay-'), Skt vi-ci- — correct (Nourai's ☞Kwei 2 'pay' is the Wiktionary root *kʷey-). vi-jan-/vi-žainti 'strike apart, harm' (Av. jan- 'strike', PIE *gʷʰen-; cf. Horn 'aw. *vi-jainti-') is the source of MP wizend/NP gazand, not of gazīdan 'bite'. vi-maik 'mix' is OIr *wi-maik- reconstructed by Nyberg for MP gumēxtan 'mix' (PIE *meyḱ-); it is not an attested Avestan word. The forms are sound as Old Iranian (partly reconstructed) compounds; their attachment to NP words is checked in node 14.\",\n derivation_fa=\"vi-či- / vi-kay- «برگزیدن، تشخیص دادن» در اوستا (بارتولومه ۴۴۱) و سنسکریت (vi-ci-) آمده است. vi-jan- «زدن و آسیب رساندن» از ریشهٔ jan- «زدن» (هندواروپایی *gʷʰen-) سرچشمهٔ پهلوی wizend و فارسی «گزند» است، نه «گزیدن» به معنی نیش زدن. vi-maik «آمیختن» را نیبرگ برای پهلوی gumēxtan بازسازی کرده و در اوستا نیامده است. صورت‌ها به عنوان ترکیب‌های ایرانی باستان پذیرفتنی‌اند، ولی برخی بازسازی‌اند.\",\n sources=[W+\"گزیدن\", W+\"گزند\", W+\"آمیختن\"],\n ref_check=[\n  {\"ref\":\"NYB:217\",\"status\":\"supports\",\"note\":\"NYB p.217 (leaf 238): 'vizand [wznd] injury, damage ... MPrthPrs wzynd, NP guzand' (the vi-jan- reflex). vicītan (p.211, l.4131): 'Av. (441) vi-kay-; ... NP guzīdan guzīn-'.\"},\n  {\"ref\":\"FFD:75\",\"status\":\"not_found\",\"note\":\"FFD p.75 (pdf 80) treats گفتن، گماردن، گواردن، لرزیدن — not this node's verbs; gazīdan is on p.74 (see node 14).\"}],\n consulted=[\n  {\"src\":\"NYB\",\"where\":\"Part II s.v. gumēxtan (l.1736)\",\"stance\":\"supports\",\"note\":\"'gumēxtan ... to mix with ... — < *vi-maik-, vi-maic-; MPrth wmyxtn; MPrs gumyxtn'.\"},\n  {\"src\":\"HRN\",\"where\":\"nos. 916, 918\",\"stance\":\"supports\",\"note\":\"'guzend Schade, Leid. aw. *vi-jainti-, vergl. ai. vi + han-'; 'guzīden aussuchen ... aw. vi + čay- aussuchen'.\"},\n  {\"src\":\"BRT\",\"where\":\"col. 441 (cited by HRN/BQT)\",\"stance\":\"silent\",\"note\":\"local OCR could not locate the vī-kay- article; cited second-hand via Horn and Mo'in.\"}]))\n\nnodes.append(dict(\n id=14, lang=\"Persian\", words=\"gozîdan; gazîdan; gomîxtan\", verdict=\"disputed\",\n derivation=\"gozīdan 'choose' (gozīneš, bargozīdan) < MP wizīdan, wizīn- < *wi-či- — confirmed by all sources. gazand 'harm' (in Nourai's parentheses) < MP wizend < *wi-jan-ti- (Nyberg, Cheung, Wiktionary) — confirmed. But gazīdan 'to bite, sting' is a different verb: MP gazīdan, gaz-, Parthian gast, Kurdish gestin, from Iranian *gaz- 'bite' (Cheung *gaz; Abolghasemi; Mo'in 'از گز + یدن'), with initial ga-, not the preverb; Nourai's 'hit against' derivation from vi-žainti is rejected. gomīxtan/gomīz: MP gumēxtan 'mix' < *wi-maik- is real (Nyberg), and Mo'in links NP gomīxtan 'to urinate', gomīz 'urine' to it ('بدآمیختن'), but Cheung derives NP gimīz, gimīzīdan from *ui- + *maiz- 'urinate' (cf. NP mīz, mīxtan), which fits the meaning far better. Worst verdict: disputed (gazīdan; gomīz doubtful).\",\n derivation_fa=\"«گزیدن» (برگزیدن، گزینش) از پهلوی wizīdan، wizīn- و ایرانی باستان *wi-či- است و درست است. «گزند» هم از پهلوی wizend و *wi-jan-ti- «آسیب زدن» آمده و درست است. اما «گَزیدن» به معنی نیش زدن فعلی جداست: پهلوی gazīdan، پارتی gast، کردی gestin، از ریشهٔ ایرانی *gaz- «گاز گرفتن». ابوالقاسمی و چونگ و معین («از گز + یدن») همین را می‌گویند، پس پیوند آن با vi-žainti رد می‌شود. «گمیختن / گمیز» را معین از پهلوی gumēxtan «آمیختن» (*wi-maik-) و به معنی «بدآمیختن» گرفته، ولی چونگ «گمیز» و «گمیزیدن» را از *ui- + *maiz- «ادرار کردن» (هم‌ریشه با «میز، میختن») می‌داند که با معنی سازگارتر است. پژوهش امروزی بخشی از این گره را رد می‌کند.\",\n sources=[W+\"گزیدن\", W+\"گزند\", W+\"آمیختن\"],\n ref_check=[\n  {\"ref\":\"BQT:1813\",\"status\":\"partial\",\"note\":\"BQT p.1813 (pdf 610; 1813.vision.txt): gozīdan n.10 'پهلوی vicītan (انتخاب کردن)، اوستا vikay (distinguere) «بارتولمه ۴۴۱» ... «اشتق ۹۱۸»' supports; but gazīdan n.9 'از: گز (بفتح اول) + یدن ...، پهلوی gazītan ... کردی ghezāndin' contradicts the vi-žainti link.\"},\n  {\"ref\":\"BQT:1835\",\"status\":\"supports\",\"note\":\"BQT p.1835 (pdf 632; 1835.vision.txt) n.5 گمیختن: 'از گمیخ (= گمیز) + تن، پهلوی gumêxtan (مخلوط کردن)، ایرانی باستان vi-maik ... «نیبرگ ص ۸۶» ... لفظاً بمعنی بدآمیختن؛ مخلوط کردن ... پیشاب ریختن'.\"},\n  {\"ref\":\"FFD:75\",\"status\":\"not_found\",\"note\":\"p.75 (pdf 80) has گماردن etc.; the relevant entry is on p.74 (pdf 79): 'گشت (= گزید) < پهلوی اشکانی gast < ایرانی باستان *gaz-ta- ... ریشهٔ gaz به معنی «گزیدن» است' — which contradicts Nourai.\"}],\n consulted=[\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *gaz, *ǰan, *maiz, *čai\",\"stance\":\"contradicts\",\"note\":\"'*gaz ? to bite, sting ... BMP gc- /gaz-/ ... NP gazīdan, Kurd. gastin'; '(+ *ui-) NP gazand damage, injury' (under *ǰan); '(+ *ui-) NP gimīzīdan/gimīz- to make water, NP gimīz' (under *maiz 'urinate'); '(+ *ui-) NP guzīdan/guzīn-' (under *čai).\"},\n  {\"src\":\"PHD\",\"where\":\"s.v. wizīdan, wizend, gazīdan, gumēxtan\",\"stance\":\"partial\",\"note\":\"'wizidan, wizin- ... N guzīdan, guzīn- choose, select'; 'wizend [wz(y)nd | M wzynd, N guzand] hurt, harm, injury'; 'gazidan, gaz- [gc-, gz-ytn' | N ~] bite, sting'; 'gumēxtan, gumēz- ... mix'.\"},\n  {\"src\":\"HRN\",\"where\":\"nos. 916, 918\",\"stance\":\"supports\",\"note\":\"guzend < aw. *vi-jainti-; guzīden < aw. vi + čay-.\"},\n  {\"src\":\"NYB\",\"where\":\"Part II s.v. vicītan, gumēxtan\",\"stance\":\"partial\",\"note\":\"'vicītan ... Av. (441) vi-kay- ... NP guzīdan'; gumēxtan 'to mix' < *vi-maik- (meaning 'mix', not 'urinate').\"}]))\n\nentry = dict(\n entry=0, root=\"Wi\", verdict=\"confirmed\",\n modern_form=\"PIE *wi- 'apart, asunder' (Pokorny 1175-1176 u̯i- 'auseinander'; Watkins wi- 'apart, in half'); Indo-Iranian *wi- > Av. vī-, OP vi-, Skt vi-, MP wi-, NP gu-\",\n note=\"Root, label and gloss are correct (Pokorny 1175-1176, WP I 312f., Watkins wi-; Wiktionary *wí, 'likely from *dwi-'). The chart is a survey of Persian words with the preverb *wi- > NP gu-/go-, and most of them hold: gostardan, gostāx, gosastan, gošādan, gomān, govāh, gorīxtan, gozaštan, gozārdan, gozīdan and gazand are all standard (Horn, Hübschmann, MacKenzie, Nyberg, Cheung). The weak points are: bīmār (MP wēmār; vi- would give gu-, Horn already rejected it); gazīdan 'bite' (from *gaz-, not *wi-jan-); bīst (Av. vīsaiti = 'two tens', the first element is 'two'); gomārdan (root *marH 'hinder', not 'designate'); gomīz (Cheung: *wi-maiz- 'urinate'); and the Iranian origin of Arabic wazīr, which is a respectable but not unanimous view. Several 'Avestan' compounds (vi-stāka, vi-mar, vi-kās, vi-maik) are reconstructions, and vīčāra is Sanskrit. The extraction matches the printed chart text; no transcription problems found. BQT page note: in this part of vol. 3 the scan offset is pdf = printed − 1203 (not −1205), and Nourai's BQT:1800 and BQT:1776 do not contain the words cited.\",\n note_fa=\"ریشهٔ هندواروپایی آغازین *wi- «جدا، از هم» در پوکورنی (ص ۱۱۷۵-۱۱۷۶)، والده-پوکورنی و واتکینز آمده و بازمانده‌هایش اوستایی vī-، پارسی باستان vi-، سنسکریت vi- و فارسی میانه wi- است. همین پیشوند در فارسی نو به قاعده «گُ» شده است. ریشه و زبان و معنایی که نورایی داده درست است. بیشتر واژه‌های این نمودار به گواهی هرن، هوبشمان، مکنزی، نیبرگ و چونگ درست‌اند، مانند گستردن، گستاخ، گسستن، گشادن، گمان، گواه، گریختن، گذشتن، گزاردن، گزیدن و گزند. ولی «بیمار» (پهلوی wēmār)، «گَزیدن» به معنی نیش زدن (از ریشهٔ *gaz-) و «گمیز» (به نظر چونگ از *wi-maiz- «ادرار کردن») از این ریشه نیستند. «بیست» هم از «دو ده» است، نه از «جدا». ایرانی بودن عربی «وزیر» نظری پذیرفتنی است، ولی همه آن را نپذیرفته‌اند.\",\n sources=[W+\"Reconstruction:Proto-Indo-European/wí\"],\n ref_check=[\n  {\"ref\":\"POK:1175\",\"status\":\"supports\",\"note\":\"POK_full.txt l.92954ff. 'Root / lemma: ui-1 ... Meaning: separate from; both, two ... Old Indic vi- apart, Avestan vi- apart; abseits ... References: WP. I 312 f.' Page(s): 1175-1176.\"},\n  {\"ref\":\"POK:1176\",\"status\":\"supports\",\"note\":\"Same lemma continues on p.1176 (comparative *uitero-: Av. vītaram 'sideways', Goth. wiþra, OE wiþ).\"}],\n consulted=[\n  {\"src\":\"WLD\",\"where\":\"Bd. I 312-313 (WLD_Bd1_pages.txt leaf 321-322)\",\"stance\":\"supports\",\"note\":\"'ui- „auseinander“. Ai. vi „auseinander“, av. vi- „auseinander; abseits, getrennt von; ent-[gegen]“'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins s.v. wi- (AHD_watkins1985.txt l.1167)\",\"stance\":\"supports\",\"note\":\"'wi-. Apart, in half. 1. ... *wi-itos ... WIDE. 2. ... *wi-tero- ... WITH. [Pok. 1. wi- 1175.]'\"},\n  {\"src\":\"IEC\",\"where\":\"IEC.txt\",\"stance\":\"silent\",\"note\":\"not consulted in detail; root is uncontroversial.\"}],\n nodes=nodes)\n\nout = dict(pdf_page=553, book_page=523, verified_by=\"claude-opus-5.5\", verified_on=\"2026-10-16\", entries=[entry])\njson.dump(out, open(\"/home/sfmqrb/git/rishe-private/data/verification/page-553.json\", \"w\", encoding=\"utf-8\"), ensure_ascii=False, indent=1)\nprint(\"ok\")\n"
}
```


### [2026-10-17T00:14:14.278Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553/build-553.py (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:14:19.750Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p553; python3 - <<'EOF'\np='build-553.py'; s=open(p).read()\ns=s.replace('\"no. 39 (bīmār), p.? ; nos. 931-932\"','\"no. 39 (bīmār); nos. 931-932\"')\ns=s.replace(''',\n  {\"src\":\"IEC\",\"where\":\"IEC.txt\",\"stance\":\"silent\",\"note\":\"not consulted in detail; root is uncontroversial.\"}]''',']')\nopen(p,'w').write(s)\nEOF\npython3 build-553.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-553.json > /dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 553"
}
```


### [2026-10-17T00:14:20.561Z] TOOL RESULT

```
ok
nodes verified: 14/14
node verdicts: {'confirmed': 3, 'plausible': 9, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 16, 'not_checked': 4, 'not_found': 4, 'partial': 3}
books consulted: {'supports': 30, 'silent': 4, 'contradicts': 3, 'partial': 10} | by book: {'HRN': 11, 'CHEUNG': 7, 'NYB': 6, 'PHD': 6, 'BRT': 4, 'WLD': 2, 'FFD': 2, 'HUB': 2, 'AHD': 1, 'BQT': 1, 'FVQ': 1, 'SKT': 1, 'KLN': 1, 'KNT': 1, 'ARY': 1}
```


## [2026-10-17T00:14:31.030Z] TOOL CALL #86: SubagentHandback

```json
{
 "message": "I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-553.json` for root Wi (1 entry, 14 nodes). The JSON is valid and `verify_check.py 553` shows 0 PROBLEM lines.\n\n**Verdicts:** root confirmed. Nodes: 3 confirmed, 9 plausible, 2 disputed, 0 transcription_suspect.\n\n**Disputed:**\n- **#10, bîmâr «بیمار»:** it comes from Middle Persian wēmār. Horn no. 39 already rejected a *vi- origin, because old vi- always becomes gu- in New Persian and the ī is left unexplained. Wiktionary instead links it to *wemh₁- \"vomit\". In the same node, gomârdan is real *ui- + *marH \"hinder\" (Cheung); Hübschmann p.95 rejects the vi-mar \"designate\" link Nourai gives.\n- **#14, gazîdan «گزیدن ۲» \"bite\":** it comes from Iranian *gaz- \"bite\" (MP gazīdan, Parthian gast), not from *vi-jan-; Cheung, Abolghasemi (FFD p.74) and Mo'in's own footnote (BQT 1813) all say so. Only gazand «گزند» descends from *wi-jan-. gomîz/gomîxtan is also doubtful: Cheung derives it from *wi-maiz- \"urinate\", while Mo'in supports Nourai's *vi-maik \"mix\".\n\n**Notable plausible items:**\n- bîst \"twenty\" is from Avestan vīsaiti, i.e. \"two tens\"; its first element means \"two\", not the preverb \"apart\".\n- Arabic wazîr as a loan from MP vičīr/wizīr is backed by Klein, Jeffery, Horn, Mo'in and Wiktionary. Skeat and the traditional Arabic view derive it natively from w-z-r \"carry\".\n- vačar/vačargar look like learned readings of the Pahlavi spelling rather than inherited words.\n- vîčâra is Sanskrit, not Avestan as labelled.\n- Several of the \"Avestan\" compounds (vi-stâka, vi-mar, vi-kâs, vi-maik) are reconstructions, not attested words.\n\n**Extraction errors:** none found; the JSON matches the chart.\n\n**Other findings:**\n- **BQT page offset:** in this part of volume 3 the scan offset is pdf = printed − 1203, not −1205. As a result the cached PNGs for BQT 1806, 1809, 1813 and 1818 show neighbouring pages. I read the correct pages from fresh renders and saved transcriptions as `.vision.txt` files for 1778, 1806, 1809, 1813, 1816, 1818, 1835, 2258 and 2279 in `data/verification/sources/refs/ocr/BQT/`. The tool now returns the right text for those pages, but the stale `.png` files are still there.\n- **Citations that don't match:** BQT:1800 and BQT:1776 don't contain the cited words (marked not_found). FFD:75 doesn't have the node 13/14 verbs; they are on p.74.\n- **Not checked:** BQT:437, BQT:834 and MON:4988 (no scan or page mapping available)."
}
```


### [2026-10-17T00:14:31.677Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
