# Verification process log — verify-page-570


## [2026-10-17T00:30:14.527Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 570 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-570.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-570.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-570.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 570` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.590Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:17.516Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:17.546Z] TOOL RESULT

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


## [2026-10-17T00:30:18.025Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-570.txt"
}
```


### [2026-10-17T00:30:18.055Z] TOOL RESULT

```
1	=== PDF page 570 (book page 540) ===
2	--- entry 0 ---
3	ROOT [Arabic] Z.b.d : to extract butter from milk (or foam from liquid)  (refs FVA:176)
4	#1 (parent #0) [Arabic] refs=FVA:176 | zobd : butter or milk fat, best of anything ; zobdeh : best of anything, skilled, talented ; zabad : foam or froth on liquid
5	  #2 (parent #1) [Persian] refs=MON:1722 | zobdeh «زُبده» : milk fat, best of anything, talented ; zabad «زَبَد» : foam or froth on top of liquid
6	  #3 (parent #1) [Arabic] refs=KLN:293 | zabâd : musk cat and its foam like musk
7	    #4 (parent #3) [Persian] refs=MON:1718 | zabâd «زَباد» : musk cat and its musk
8	    #5 (parent #3) [Italian] refs=KLN:293 | zibetto : musk cat and its musk
9	      #6 (parent #5) [French] refs=KLN:293 | civette
10	        #7 (parent #6) [English] refs=KLN:293; TYL:568 | civet, zibet : musk cat and its musk
11	--- entry 1 ---
12	ROOT Zgwes -> redirect to Gwes
13	--- entry 2 ---
14	ROOT [Semitic] Z.h.k : he laughed  (refs KLN:816)
15	#1 (parent #0) [Arabic] refs=KLN:816 | z.h.k, zahika : he laughed ; mozhek : laughable, funny
16	  #2 (parent #1) [Persian] refs=FVA:239 | mozhek «مُضحک» : funny
17	#3 (parent #0) [Hebrew] refs=KLN:816 | tzâhaq : he laughed ; Yitzhâq, Yišâq : he laughs
18	  #4 (parent #3) [Arabic] refs=None | 
19	    #5 (parent #4) [Persian] refs=AKM:31 | Es-hâq «اسحاق ( اسحق )» : "he laughs", a biblical name
20	  #6 (parent #3) [Greek] refs=KLN:816 | Isaak
21	    #7 (parent #6) [Late Latin] refs=KLN:816 | Isaacus
22	      #8 (parent #7) [English] refs=KLN:816 | Isaac
23	--- entry 3 ---
24	ROOT Zi -> redirect to Zay
25	
```


## [2026-10-17T00:30:18.816Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-570.json"
}
```


### [2026-10-17T00:30:18.834Z] TOOL RESULT

```
1	{
2	  "pdf_page": 570,
3	  "book_page": 540,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Z.b.d",
8	        "lang": "Arabic",
9	        "refs": "FVA:176",
10	        "gloss": "to extract butter from milk (or foam from liquid)"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Arabic",
17	          "refs": "FVA:176",
18	          "words": [
19	            {"translit": "zobd", "gloss": "butter or milk fat, best of anything", "script": null},
20	            {"translit": "zobdeh", "gloss": "best of anything, skilled, talented", "script": null},
21	            {"translit": "zabad", "gloss": "foam or froth on liquid", "script": null}
22	          ],
23	          "script_extra": null,
24	          "note": null,
25	          "quote": null
26	        },
27	        {
28	          "id": 2,
29	          "parent": 1,
30	          "lang": "Persian",
31	          "refs": "MON:1722",
32	          "words": [
33	            {"translit": "zobdeh", "gloss": "milk fat, best of anything, talented", "script": "زُبده"},
34	            {"translit": "zabad", "gloss": "foam or froth on top of liquid", "script": "زَبَد"}
35	          ],
36	          "script_extra": null,
37	          "note": null,
38	          "quote": null
39	        },
40	        {
41	          "id": 3,
42	          "parent": 1,
43	          "lang": "Arabic",
44	          "refs": "KLN:293",
45	          "words": [
46	            {"translit": "zabâd", "gloss": "musk cat and its foam like musk", "script": null}
47	          ],
48	          "script_extra": null,
49	          "note": null,
50	          "quote": null
51	        },
52	        {
53	          "id": 4,
54	          "parent": 3,
55	          "lang": "Persian",
56	          "refs": "MON:1718",
57	          "words": [
58	            {"translit": "zabâd", "gloss": "musk cat and its musk", "script": "زَباد"}
59	          ],
60	          "script_extra": null,
61	          "note": null,
62	          "quote": null
63	        },
64	        {
65	          "id": 5,
66	          "parent": 3,
67	          "lang": "Italian",
68	          "refs": "KLN:293",
69	          "words": [
70	            {"translit": "zibetto", "gloss": "musk cat and its musk", "script": null}
71	          ],
72	          "script_extra": null,
73	          "note": null,
74	          "quote": null
75	        },
76	        {
77	          "id": 6,
78	          "parent": 5,
79	          "lang": "French",
80	          "refs": "KLN:293",
81	          "words": [
82	            {"translit": "civette", "gloss": null, "script": null}
83	          ],
84	          "script_extra": null,
85	          "note": null,
86	          "quote": null
87	        },
88	        {
89	          "id": 7,
90	          "parent": 6,
91	          "lang": "English",
92	          "refs": "KLN:293; TYL:568",
93	          "words": [
94	            {"translit": "civet, zibet", "gloss": "musk cat and its musk", "script": null}
95	          ],
96	          "script_extra": null,
97	          "note": null,
98	          "quote": null
99	        }
100	      ]
101	    },
102	    {
103	      "root": {"name": "Zgwes", "redirect": "Gwes"},
104	      "nodes": []
105	    },
106	    {
107	      "root": {
108	        "name": "Z.h.k",
109	        "lang": "Semitic",
110	        "refs": "KLN:816",
111	        "gloss": "he laughed"
112	      },
113	      "nodes": [
114	        {
115	          "id": 1,
116	          "parent": 0,
117	          "lang": "Arabic",
118	          "refs": "KLN:816",
119	          "words": [
120	            {"translit": "z.h.k, zahika", "gloss": "he laughed", "script": null},
121	            {"translit": "mozhek", "gloss": "laughable, funny", "script": null}
122	          ],
123	          "script_extra": null,
124	          "note": null,
125	          "quote": null
126	        },
127	        {
128	          "id": 2,
129	          "parent": 1,
130	          "lang": "Persian",
131	          "refs": "FVA:239",
132	          "words": [
133	            {"translit": "mozhek", "gloss": "funny", "script": "مُضحک"}
134	          ],
135	          "script_extra": null,
136	          "note": null,
137	          "quote": null
138	        },
139	        {
140	          "id": 3,
141	          "parent": 0,
142	          "lang": "Hebrew",
143	          "refs": "KLN:816",
144	          "words": [
145	            {"translit": "tzâhaq", "gloss": "he laughed", "script": null},
146	            {"translit": "Yitzhâq, Yišâq", "gloss": "he laughs", "script": null}
147	          ],
148	          "script_extra": null,
149	          "note": null,
150	          "quote": null
151	        },
152	        {
153	          "id": 4,
154	          "parent": 3,
155	          "lang": "Arabic",
156	          "refs": null,
157	          "words": [],
158	          "script_extra": null,
159	          "note": null,
160	          "quote": null
161	        },
162	        {
163	          "id": 5,
164	          "parent": 4,
165	          "lang": "Persian",
166	          "refs": "AKM:31",
167	          "words": [
168	            {"translit": "Es-hâq", "gloss": "\"he laughs\", a biblical name", "script": "اسحاق ( اسحق )"}
169	          ],
170	          "script_extra": null,
171	          "note": null,
172	          "quote": {
173	            "text": "همچو جرجیس شود کشتهٔ عشقش صد بار - یا چو اسحاق شود بسمل از آن خنجر او",
174	            "poet": "Molavî"
175	          }
176	        },
177	        {
178	          "id": 6,
179	          "parent": 3,
180	          "lang": "Greek",
181	          "refs": "KLN:816",
182	          "words": [
183	            {"translit": "Isaak", "gloss": null, "script": null}
184	          ],
185	          "script_extra": null,
186	          "note": null,
187	          "quote": null
188	        },
189	        {
190	          "id": 7,
191	          "parent": 6,
192	          "lang": "Late Latin",
193	          "refs": "KLN:816",
194	          "words": [
195	            {"translit": "Isaacus", "gloss": null, "script": null}
196	          ],
197	          "script_extra": null,
198	          "note": null,
199	          "quote": null
200	        },
201	        {
202	          "id": 8,
203	          "parent": 7,
204	          "lang": "English",
205	          "refs": "KLN:816",
206	          "words": [
207	            {"translit": "Isaac", "gloss": null, "script": null}
208	          ],
209	          "script_extra": null,
210	          "note": null,
211	          "quote": null
212	        }
213	      ]
214	    },
215	    {
216	      "root": {"name": "Zi", "redirect": "Zay"},
217	      "nodes": []
218	    }
219	  ]
220	}
221	
```


## [2026-10-17T00:30:22.620Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['FVA','MON','KLN','TYL','AKM','FVQ','AFM','PLA','LKT','SKT','HJB','BQT','ARY','FSD','WEB','PHN','DEV','DOZ']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-17T00:30:23.224Z] TOOL RESULT

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
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
TYL {"title": "W. Taylor, Arabic Words in English (S.P.E. Tract XXXVIII), Oxford 1933", "edition_found": null, "kind": "hathitrust_fullview", "url": "https://babel.hathitrust.org/cgi/pt?id=uc1.b4089843 (S.P.E. Tracts nos. 31-40 bound volume incl. Tract XXXVIII, rightsCode pdus = full view in the US; record 000519279) ; mdp.39015005310308 (nos. 36-58) search-only", "identifier": null, "local_file": ["/
AKM {"title": "Amir J. A'lam, Farhang-e A'lam-e Ketab-e Moqaddas (Dictionary of Proper Names in the Bible, English–Persian), Iran University Press 1988", "kind": "purchase", "url": "in print (Niloofar 1388); gisoom/iketab", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only."}
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. l
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe-private/data
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt", "page_offset
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git
```


## [2026-10-17T00:30:28.750Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['KLN','TYL','MON','LKT','SKT','FVQ','AFM','PLA','DEV','PHN','DOZ','LAM']:\n  v=d.get(k) or {}\n  print(k, v.get('local_file'), v.get('page_offset'), (v.get('lookup_hint') or '')[:300]);print()\n\"; sed -n 80,200p sources/SOURCE_MATRIX.md | grep -A12 -i 'arabic\\|semitic\\|english' | head -80"
}
```


## [2026-10-17T00:30:30.107Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; command ls page-5*.json | tail -5; python3 -c \"\nimport json;d=json.load(open('page-558.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in d.items() if k!='entries'}));print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-17T00:30:30.479Z] TOOL RESULT

```
KLN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

TYL ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_LeedsStudiesInEnglish_ArabicWordsInBenJonson_pp44-50.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_BenJonson_pages.txt'] None Not on IA (searched 'arabic words in english', 'society for pure english tract 38'); Google Books record has no view. Taylor's related 'Etymological List of Arabic Words in English' (1933) id QmBbAAAAIAAJ is snippet only.

MON ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe

LKT /home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.

SKT /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.

FVQ ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt'] printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).

AFM ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt'] 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').

PLA ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

DEV /home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> French headword in caps at line start.

PHN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHN.txt leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.

DOZ /home/sfmqrb/git/rishe-private/data/verification/sources/refs/DOZ.txt leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Dutch headword in caps at line start.

LAM /home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAM.txt leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> French headword in caps at line start with running heads like '2 ABRI'.

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
--
## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
```


### [2026-10-17T00:30:30.632Z] TOOL RESULT

```
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
{"pdf_page": 558, "book_page": 528, "verified_by": "claude-opus-5.5", "verified_on": "2026-10-16"}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "kâca",
 "verdict": "confirmed",
 "derivation": "Skt. kāca- m. 'glass, crystal, quartz' (classical, post-Vedic). Buck lists it as the Sanskrit word for GLASS and tentatively links it to khac- 'shine through'. Wiktionary instead suggests a Nuristani loan cognate with kāś- 'shine'. It continues in Pali kāca, Hindi kā̃c, Bengali kāc, Malay kaca. The gloss 'pearl' comes from Mo'in's BQT footnote, which cites Monier-Williams for 'شیشه، آبگینه، مروارید' (glass bead). The word and its sense 'glass' are secure.",
 "derivation_fa": "سنسکریت kāca- به معنای «شیشه، بلور، کوارتز» در سنسکریت کلاسیک به‌خوبی گواهی شده و در پالی kāca و هندی kā̃c (کانچ) و بنگالی kāc بازمانده است. باک آن را با تردید به ریشهٔ khac- «درخشیدن» می‌پیوندد و ویکی‌واژه آن را وامی از نورستانی می‌داند. معنای «مروارید» را معین در حاشیهٔ برهان قاطع به نقل از فرهنگ مونیر-ویلیامز آورده است (مهرهٔ شیشه‌ای). وجود واژه و معنای «شیشه» درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/काच"
 ],
 "ref_check": [
  {
   "ref": "SYN:620",
   "status": "supports",
   "note": "SYN p.620 GLASS table: 'Skt. kāca-'; para 7 'Skt. kāca- : khac- shine through (?)'."
  },
  {
   "ref": "BQT:1556",
   "status": "supports",
   "note": "BQT vol 3 p.1556 (pdf 349; vision file ocr/BQT/1556.vision.txt), footnote 9 to کاچ: 'قس: سانسکریت kâcá (شیشه، آبگینه، مروارید) «ویلیامز ۲:۲۶۸»'. Mo'in gives the Sanskrit word with these meanings."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "POK_full.txt grep 'kāca'",
   "stance": "silent",
   "note": "not in Pokorny."
  },
  {
   "src": "WLD",
   "where": "WLD Bd1/Bd2 grep 'kāca'",
   "stance": "silent",
   "note": "not in Walde-Pokorny."
  },
  {
   "src": "SYN",
   "where": "p.620 §9.74",
   "stance": "supports",
   "note": "'Skt. kāca-' as the Sanskrit word for 'glass'."
  }
 ]
}
```


## [2026-10-17T00:30:38.021Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^civet\\|^zibet\\|^Isaac' KLN_1966.txt | head; awk 'BEGIN{RS=\"\\f\"} NR>=157 && NR<=160' KLN_1966.txt | grep -n -i -A8 'civet' | head -40"
}
```


### [2026-10-17T00:30:38.404Z] TOOL RESULT

```
7794:civet,  n.,  1)  a  musklike  substance  obtained  from the  anal  glands  of  the  civet  cat;  2)  the  civet  cat. —  F.  civette,  fr.  It.  zibetto,  fr.  Arab,  zabdd, ‘civet’,  which  is  rel.  to  zabad,  ‘foam,  froth’, zubd,  ‘cream’.  Cp.  zibet.
19943:Isaac,  1)  masc.  PN;  2)  in  the  Bible,  one  of  the patriarchs,  son  of  Abraham  and  Sarah  and father  of  Jacob  and  Esau.  —  Late  L.,  fr.  Gk. ’Ioaax,  fr.  Heb.  Yitzhdq,  lit.  ‘he  laughs’,  prop, imperf.  of  tzdhdq,  ‘he  laughed’,  which  is  rel.  to Aram.-Syr.  glhekh,  Arab,  dahika,  ‘he  laughed’. Isabel,  fem.  PN.  —  Sp.  See  Isabella, isabelita,  n.,  an  angelfish.  —  American  Sp.,  lit. ‘little  Isabella’,  dimin.  of  Isabel,  ‘Isabel’.  See prec.  and  next  word.
```


## [2026-10-17T00:30:41.531Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 7794 19943; do head -n $n KLN_1966.txt | tr -cd '\\f' | wc -c; done; grep -n -i '^zibet' KLN_1966.txt KLN_1971.txt|head -3; grep -n -i 'zibet\\|zabad\\|zabād' SKT.txt LKT.txt DEV.txt PHN.txt DOZ.txt LAM.txt FSD_vol1.txt WEB_vol1.txt 2>/dev/null | head -30"
}
```


### [2026-10-17T00:30:42.082Z] TOOL RESULT

```
165
441
KLN_1971.txt:270597:zibet, also zibetb, n., the Asiatic or Indian civet. 
LAM.txt:331:sit, mulâtre, baldaquin, turbith,,luth(i), zibeth.
LAM.txt:3417:Civette. Esp: civeta. Ital: zibetto. Le mot civette (i)
LAM.txt:3435:he\Zibeth est une variété de civette vivant dans les
LAM.txt:3442:quadrupèdes de Hnde on trouve le zibeth ; il y est aussi
LAM.txt:3445:cieux parfum appelé lait de zibeth» (Prairies d'or, III. 57)
LAM.txt:7503:Zibeth. Viverra zibetha Linn. Nom d'uçe espèce in-
LAM.txt:9919:Zibeth
DEV.txt:1152:Civette.  Ital.  zibetto.  Zihct  ou  ziheth  est  le  même  nom appliqué  par  nos  naturalistes  à  un  animal  très-voisin  de la  civette  ^   C'est  l'arabe  :>l}yzcb(ld,  zoubâd,  qui,  connue
DEV.txt:1579:JuBis,  Terme  de  commerce.  Raisins  secs  en  caisse.  C'est une  altération  de  l'arabe  L^-y^'^  zebib,  raisin  sec,  comme  le prouvent  les  vieilles  formes  azebit,  auzibet  :  «  Pro  cargua de  azebits  seu  racemis,  ?5  dit  un  vieux  tarif  de  Carcassonne, cité  dans  Du  Gange.  Ces  dernières,  ainsi  que  l'espagnol nzebibe,  acebibr,  ont  gardé  l'article  al^  dont  le  l  s'assimile au  z  suivant  :  az~zebïb.  En  portugais,  acipipe  a  pris  une  si- gnification plus  générale,  celle  de  menues  friandises  propres à  aiguiser  rappétit,  à  rafraîchir.  Diverses  contrées  musul- manes, ne  buvant  pas  de  vin,  livraient  leurs  raisins  séchés au  commerce,  et  cet  aliment  était  fort  estimé  des  Arabes; Razi  le  regarde  comme  plus  nutritif  que  la  datte  :  «-.vH>y^ A^-o  t «xil^  ^^yï]  -«Oi  J^Xi  IX  ^ô^j^_  ^  ff  Le  raisin  sec  n'obstrue point  comme  fait  la  datte,  bien  que  plus  nourrissant qu'elle.:)?  (M an.  arabe  déjà  cité,  fol.  63  verso.)
DEV.txt:2862:Aupbin,  voy.  Fou. Auqnelon,  voy.  Hoqueton. Auzibet,  voy.  Jubis. Avania ,  pg.  ital.  voy.  Avanie.
DEV.txt:4516:Zibet,  voy.  Civette.
DEV.txt:4517:Zibeth ,  voy.  Civette.
DEV.txt:4518:Zibetto,  ital.  voy.  Civette.
PHN.txt:3825:Comparez aussi l'italien zibetto et l'anglais civet.
PHN.txt:10136:ZIBET, s. m. (a.)
PHN.txt:10139:BufTon dit que « le zibet diffère de la civette en ce qu'il a ie
PHN.txt:10152:zibet, civette, ou galia. Voyez ce dernier mot.
PHN.txt:10956:Zibet, s. m. (a.) 378
LKT.txt:582:'ümsonst,  gratis'  [Kelekian  233  b,  wohl aus  ar.  bädi-hawä  'Luft  verursachend'] ; hieraus  bulg.  badihawa,  badlawa  'dass.', serb.  badawad  'dass.',  slov.  badava  und mit  slav.  Präposition  zabadava  'verge- bens, umsonst'.    [Bern  SlEtWb  37.
LKT.txt:1614:'Parfüm  aus  Moschus  und  Ambra';  hier- aus sp.  algalia,  pg.  algälia  'dass.';  mlat. galia  muscata,  sp.  pg.  gato  de  algalia [Constancio  Dicc  50  b]  'Zibetkatze,  Vi- verra  civetta  Schreb.'.
LKT.txt:1691:'Zibetkatze'  [CHERBONNEAU  in  JAs 1849,  I,  541];  hieraus  frz.  genette,  sp. pg.  gineta  'Zibet-  oder  Risamkatze,  Vi- verra  genetta  L.'.  —  [*(.fa)gmetta  ist schon  von  DIEZ  als  Grundwort  zurück- gewiesen worden.]  [DE  276.  Eguilaz 413.    Devic  DEt  127.    ML  3949.
LKT.txt:4860:'Schaum';  hieraus  mit  Imäla  [ä  >  ej mlat.  zibethum  'Zibetkatze'  [so  genannt, weil  sie.  eine  stark  riechende  schaum- artige Flüssigkeit  absondert],  it  zibetto, frz.  civette;  ndl.  civet,  civetkat,  dts<-h. Zibetkatze,  engl,  civef.  [Dozy  Oost  31/32. ML  95SÖ.
LKT.txt:5892:2214 Zibetkatze  2173 Z«/f<?r  1894 Zinnober  1827 Z«Y<<.-er  2215
LKT.txt:7452:Zeduarium  2215 zibethum  2173 zingiber  1930 »iVftMs  2030 ziziphum  2228.
WEB_vol1.txt:60352:divrian, dt/rién, n. (Malay, from duri, thorn.| the oval, edible fruit of an East Indian tree, Duriozibethinus,also, the tree itself.
WEB_vol1.txt:60391:DURIAN (Durio zibetkinus}
FSD_vol1.txt:10753:A-Jodh'ya,  l   a-y0d'ya:  2   a-y0d'ya,  n.  An  ancient  city  In Faizabad,  India;  formerly  9G  eq.  m.  In  area;  100  temples, 36  mosques;  annual  fair  of  Ramnami,  500,000  pilgrims  at- tending. [pace.
FSD_vol1.txt:33584:Ba"dak-shan',  1   ba'dak-Shan';  2   ba'dak-shan',  n.  A   dis- trict in  N.  E.  Afghanistan;  capital,  Faizabad. Ba"da-Io'na,  1   bi'da-15'na;  2   ba'da-10'nii,  n.  A   seaport  In Barcelona  province,  Spain.
FSD_vol1.txt:67562:Clv'et1,  1   siv'et;  2   cfv'et,  n.  1.  An  unctuous  yellowish semiliquid  substance  of  musk-like  odor  and  bitterish taste,  secreted  by  glandular  follicles  of  certain  viverrine carnivores  in  a   pouch  between  the  anus  and  the  external genitalia:  used  as  a   perfume,  and  formerly  in  medicine. 2.  A   viverrine  carnivore  that  secretes  the  substance defined  above,  as  the  zibet  or  rasse;  especially  Viverra ciretta  of  tropical  Africa,  which  is  about  the  size  of  a   fox.
FSD_vol1.txt:73940:CoIo"neI-ganJ  %   l   kur'nel-gunj';  2   eur'ngl-gfinj',  n.  A   town In  Falzabad  division,  Oudh,  India. co-Ion 'gl-tude,  1   kO-len'Ji-tifld;  2   co-16n'gl-tQd,  n.  Astron. &   Geol.  The  complement  of  the  longitude  of  any  given meridian.  [   <   co-*  -f  longitude.] co-lo'nl,  1   ko-15'nal;  2   co-18'nl,  n.  Plural  of  colonus. Co-lo'nl-a,  La,  l   la  ko-15'nl-a;  2   la  co-16'nl-ii.  A   department in  Uruguay;  2,192  sq.  m.;  capital,  Colonia. co-lo'nl-al,  1   kp-15'm-al;  2   co-Io'ni-al,  a.  1.  Of,  per- taining to, or  being  a   colony or  colonies,  specifically  the transmarine  colonies  of Great  Britain  or  other European  states.
```


## [2026-10-17T00:30:48.011Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==166' KLN_1966.txt | head -5; echo ----; awk 'BEGIN{RS=\"\\f\"} NR==442' KLN_1966.txt | head -5; echo; grep -n -A6 '^CIVET' SKT.txt | head; awk 'NR>=4855 && NR<=4862' LKT.txt; sed -n 1150,1156p DEV.txt; sed -n 3415,3436p LAM.txt; sed -n 3815,3826p PHN.txt"
}
```


### [2026-10-17T00:30:48.595Z] TOOL RESULT

```
der  was founded  (in  1098).
Derivative:  Cistercian,  adj. cistern,  n.  —  ME.  cisterne,  fr.  OF.  cisterne  (F.  ci- terne),  fr.  L.  cisterna,  ‘a  reservoir  for  water, cistern’,  formed  fr.  cista,  ‘chest’,  with  suff.  -erna. See  chest.  For  the  suff.  see  cavern.
Derivative:  cistern-al,  adj. cisterna,  n.,  cistern  (anat.)  —  See  prec.  word. Cistus,  n.,  the  genus  of  rockroses  (bot.)  —  ModL., fr.  Gk.  xtctToc,  xiaScx;,  ‘rockrose’,  which  is  of unknown  origin.
cistvaen,  kistvaen,  n.,  a  stone  coffin.  —  W.  cist- faen,  lit.  ‘stone  chest’,  fr.  cist,  ‘chest’  (see  cist, ‘stone  chest’),  and  faen,  aspirated  form  of  maen, ‘stone’.
cit,  n.  —  Contraction  of  citizen, citadel,  n.  —  F.  citadelle,  fr.  It.  cittadella,  dimin. of  Olt.  cittade  (It.  cittd),  fr.  L.  civitatem,  acc.  of civitas,  ‘city’.  Cp.  Port,  citadella,  Sp.  ciudadela, and  see  city.
----
timulate,  stir  up,  provoke’, prob.  freq.  of  *ir-ri-re,  ‘to  stir  up,  excite’,  fr. in-,  in’,  and  I.-E.  base  *erei-,  ‘to  set  in  motion, stir  up’,  whence  also  Gk.  ipfvciv,  ‘to  raise, stir,  excite’,  ipvuvai,  ‘to  rise’,  L.  orior,  oriri, ‘to  rise’.  See  orient  and  cp.  rivulet.  Cp.  also  ran. Derivatives:  irritat-ing,  adj.,  irritat-ing-ly,  adv., irritation  (q.v.),  irritat-ive,  adj.,  irritat-ory,  adj. irritate,  tr.  v.,  to  make  null  and  void  (law).
L.  irritatus,  pp.  of  irritare,  ‘to  make  void,  in¬ validate’,  fr.  irritus,  ‘invalid,  void’,  formed  fr.
816
817
ir-,  ‘not’,  and  rat  us,  ‘fixed’,  pp.  of  rear,  reri,  ‘to think,  count’.  See  rate,  ‘amount’,  and  verbal suff.  -ate.  For  the  change  of  Latin  &  (in  rdtus) to  i  (in  in-ritus,  ir-ritus)  see  abigeat  and  cp. words  there  referred  to.

2172.  Pers.  'ytr-i-§ähl: 'Königliches  Parfüm'  [aus  ar.  'itr  'Par-
Ar.  zabäd.]
170
fäm'  und  pers.  säht,  s.  hier  Nr.  1762; Tielleichl  ist  auch  ytyr  tk.  Wort  mit  der Bedeutung  'Geranium']  oder  'Geraniunr, so  auch  tk.  (Kelekian  KämOs  851  h] : hieraus  rum.  indi-i^aim,  andri^ea  'Ge- ranium'.
2173.  Ar.  zabäd :
'Schaum';  hieraus  mit  Imäla  [ä  >  ej mlat.  zibethum  'Zibetkatze'  [so  genannt, weil  sie.  eine  stark  riechende  schaum- artige Flüssigkeit  absondert],  it  zibetto, frz.  civette;  ndl.  civet,  civetkat,  dts<-h. Zibetkatze,  engl,  civef.  [Dozy  Oost  31/32. ML  95SÖ.
2174.  Pers.  zäbän:
'Zunge'  [Horn  NpEt.  S.  144.  Nr.  6.Ö0], zäbänä  'Pfeifenzunge':  ebenso  tk.zywane 'Mundstück  der  Pfeife'  [Kelekian  Kämas 649 b];  hieraus  luin.  ghivanea  'dass ' [Löbel  EITAP  49].
CiNNOR  ou  KiNNOR.  Instrument  de  musique  chez  les  Hé- breux. Transcription  de  l'hébreu  li^D  kinnôr,  qu'on  inter- prète par  le  latin  cithara,
CiPAYE.  Nom  donné  dans  l'Inde  aux  indigènes  qui  ser- vent dans  les  troupes  européennes.  Du  persan  j^Lw  sipâlû, cavalier,  soldat.  C'est  le  même  mot  que  spahi.  Sipâhï  vient de  c-MA<)  asp,  cheval.
Civette.  Ital.  zibetto.  Zihct  ou  ziheth  est  le  même  nom appliqué  par  nos  naturalistes  à  un  animal  très-voisin  de la  civette  ^   C'est  l'arabe  :>l}yzcb(ld,  zoubâd,  qui,  connue
'   Cf.  Defrémery,  Mém.  d'hist.  orient,  p.  3.") 5,  ii.  i .
DES  MOTS  D'ORIGINE  ORIENTALE.  97
clio/  nous  le  mol  civetle,  s'a|)|)liquo  a  la  substance  onc- fueuso  et  parrumée  que  fournit  l'animal.  Les  Arabes  sem- blent vouloir  rapprocber  zonhâil  de  Jy)  zouhd,  crème  de lait.  Mais  je  suis  perlé  à  croire  que  c'est  là  une  sim[)le coïncidence  avec  le  nom  du  quadrupède  :  la  civette  est originaire  de  l'Afrique  équatoriale;  les  nègres  du  Congo la  nomment  mimé.
CoLBACK.  Sorte  de  bonnet  à  poil  en  usage  dans  quelques corps  de  notre  cavalerie.  Il  date  chez  nous  de  l'expédition (le  Bonaparte  en  Egypte.  C'est  le  turc  dLXi  qaJpak,  bon- net tartare  en  fourrures,  mot  qui  figure  aussi  chez  nos écrivains  sous  la  forme  calpah  ou  haJpak  et  tnlpack.
ment le persan schimschir s'est métamorphosé en cime-
terre ».
Civette. Esp: civeta. Ital: zibetto. Le mot civette (i)
ne date que du 1 6°^® siècle. Il vient de ^l> j , :{abâd (2) qui
désigne la substance parfumée que sécrète l'animal de
même nom, appelé par les Arabes ^l»jl Jaï , ^att a:{-
:{abâd^ chat qui fournit la civette, le gatto :[ibetto du P.
Ange de S. Joseph. L'auteur du Qâmoûs veut absolument
(1) Ou plutôt Civetta, qae Belon aurait employé le premier en 1553.
(2) M. deEguil. dérive civeta de ««a^j) zebeda, muscum». ^ous ne con-
naissons pas ce sens à ;jl{ j , zoubda. Ce mot signifiant crème de lait, éco-
mei beurre frais. Aux Indes «outre les chats ordinaires, il y en a d^autrea
entièrement semblables à eux, qui produisent cette matière odoriférante
que nous appelions en France Civette et que les Portugais nomment algalia.»
(R. P. Philippe, p. 374 ) de sJUI.COIF 89
■ — ■ ■_ _^ ^^ ^-^__^.^^_^^^__-
que ce soit le chat vulgaire. Le Chérif el-Edrîsî dit positi-
vement que la civette est plus grande que notre chat
domestique. Dans Aghânî (II, 5 2. Salh.) ^l 3 est expliqué
par peaux parfumées. <^ ï^lj U :^ y^j ^Ij
he\Zibeth est une variété de civette vivant dans les
Indes et dans les îles de l'archipel Indien. Ce nom imposé
tionnaire turc-français de M. Bianchi, t. Il, p. 56, col. â.
CIVETTE, s. f. (a.)
^\âj [zébâd] sécrétion odorante, sorte de musc. — La civette, ori-
ginaire de l'Orient, est assez semblable au renard; elle pos-
sède une poche profonde où se forme une espèce de liqueurCLA 121
appelée zébâd, dont l'odeur est très-forte. — 11 peut paraître
difficile, au premier abord, de faire concorder civette avec
Tarabe zââd; mais le même animal s'appelle aussi ztbet en fran-
çais, quoique plus rarement, et dès lors il ne reste plus de
doute : le dernier mot confirme Tétymologie du premier. —
Comparez aussi l'italien zibetto et l'anglais civet.
GLABAUD,s. m. (a.)
```


## [2026-10-17T00:30:52.208Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==166' KLN_1966.txt | grep -n '^[0-9]\\{3\\}$'; grep -n -B2 -A8 '^CIVET\\|^Civet' SKT.txt | head -20; grep -n -i 'isaac' SKT.txt FSD_vol*.txt LKT.txt | head; sed -n 67560,67566p FSD_vol1.txt | grep -o '\\[.*\\]' | head"
}
```


### [2026-10-17T00:30:52.595Z] TOOL RESULT

```
28:294
29:295
LKT.txt:4353:1928.  Sskr.  sranianä: 'Bettelmönch,  Asket'  [eigentlich  'Selbst- peiniger', vgl.  sram  'defatigari !'],  präkr. samana ;  hieraus  tungusisch  saman 'Geisterbeschwörer';  dieses  Wort  ist  in alle  europäischen  Sprachen  zur  Be- zeichnung des  ostasiatischen  Zauberers und  Geisterbeschwörers  übergegangen: russ.  saman,  bulg.  saman,  öech.  samän, poln.  szamcm;  frz.  chaman,  samanien; dtsch.  Schamane,  engl,  shaman.  Vgl. Geschichten  der  Ost-Mongolen  von Ssanang  Ssetzen  Chuntaidschi.  Aus  dem Mongolischen  von  Isaac  Jacob  Schmidt. St.  Petersburg  1829.  S.  416;  W.Schott, Über  den  Doppelsinn  des  Wortes  Scha- mane und  über  den  tungusischen  Scha- manen-Gultus  am  Hofe  der  Mandju-Kai- ser.  Berlin  1842.  Auf  altaischen  Ur- sprung soll  tungus.  sam  <  tk.  kam zurückgehen  nach  J.  N6meth,  Über  den Ursprung  des  Wortes  saman  in  KSz
FSD_vol4.txt:17:Isaac  K.  Funk,  D.D.,  LL.D.,  Editordn-Chief
FSD_vol4.txt:303:Sa"cy'*  1   sa'sr,  2   si'cy'.n  1.  Baron  de  (»/nl758- Vm1838),  Antoine  Isaac  Sllvestre,  a   French  Orien- tal scholar,  A   rabic  Grammar  2   Samuel  Ustazade SUvestre  de  son  of  Antoine,  a
FSD_vol4.txt:9911:present  words  and  sentences  in  graphic  outline  an  art employed  in  some  form  even  in  the  time  of  the  ancient Romans:  opposed  to  longhand  See  stenography In  the  English  language  the  number  ol  simplified  alpha- bets used  to  facilitate  such  abbreviation  has  been  very  great —   201  having  been  Invented  and  more  or  less  used  from  the beginning  of  the  17th  century,  when  the  art  was  revived after  having  been  for  centuries  disused,  to  the  year  1837, when  Isaac  Pitman  introduced  his  system,  called  by  him at  first  stenographic  sound^hand,  and  later  phonography Since  then  about  300  more,  many  of  them  based  upon Pitman's  or  proceeding  along  similar  lines,  have  been  de- vised In  modem  classifications  of  shorthand  a   system  in which  the  abc  alphabet  Is  used,  and  the  shortening  effected by  arbitrary  contractions  and  symbols,  Is  properly  stenosh raphy,  while  a   system  In  which  elementary  sounds  are  ex- pressed phonetically  by  arbitrary  signs,  used  singly  or  In combinations,  is  called  phonography  A   Joined  and  sim- plified form  of  phonography  Is  also  known  os  taehygraphy (See  these  words  )   The  Illustration  shows  the  signs  for several  consonants  used  in  eight  English  systems,  one French,  and  one  German  As  to  these  systeins  and  their authors  Willis  was  the  second  author  who  published  a   book on  shorthand  (Bright,  1588.  being  the  first) .   Fepys  used Shelton's  system  In  writing  his  Diary,  Gurney's  system  was founded  on  Mason's  and  used  in  parliamentary  reporting, Towndrow  used  stroke  vowel-eigns.  and  Cossard’s  system  Is still  the  basis  of  French  stenography,  which  dlirers  widely from  English  systems  The  German  systems  are  mainly cursive  In  the  United  States,  a   modification  of  the  Isaac Pitman  system  was  Introduced  by  his  brother  Benn  Pitman A   non-Pltmanlc  system  was  devised  by  John  R   Gregg  In 188*^  lA  writer  of  shorthand
FSD_vol4.txt:12611:Isaac  K   Fom  The  TTufetc’s  p   3C9  [r  a   w   co  Mj
FSD_vol4.txt:18602:Isaac  Barrow  5«miOTM  vol  i   scr  iv  p   33  1/  c   R   1845  J
FSD_vol4.txt:18970:Isaac  K   Fns'a  TAe  ITuioie’A  Jlife  p   CS  [r  atv  ’MI  Church  revenues  tithes  4   The  Pope  a
FSD_vol4.txt:19036:Isaac  K   Fcjfx  TAc  TTidotc  «   p   36  Ir  *   w   *04  1   ®Pl  ro-graphn-din,  n   Chem  A   hyalin  ^dc  from  sphog- 2   An  adherent  of  the  spiritual  philosophy  See  spir-  raphin -spi-rog'ra-pliln,  n   Cftm  A   l^yalogen  obtained
FSD_vol4.txt:21733:It  would  be  m&doess  for  &   s   ouog  atatucrv  to  attenipt  at  first  to car\e  a   Venus  or  a   Mercury  Isaac  Watts  Jmprtnemtnt  of  the Aftnd  pt  i   p   18-1  (w  p   N   1868  \
FSD_vol4.txt:22497:(2A9l833-3/isl902k  an  American  bibliographer,  publisher, and  author  2   Edwin  Augustus  C/s«1795-*/8l86S),  an American  Inventor  and  naval  constructor,  founded  Stevens Institute,  Hoboken,  N   J   3   Isaac  Ingalls  (VsslSlS- V>1862)  a   United  States  general,  killed  at  Chantilly  4. lhaddeus  (V4I792-8/11I868),  an  American  statesman, abolitionist  a   Republican  leader  In  Congress  5.  A   county in  S   W   Kansas,  7^9  sq  m   county-seat,  Hugoton  G.  A county  In  central  W   Minnesota,  576  sq  m   county-seat, Morris  7.  A   county  In  N   E   Washington,  3,866  sq  m   , county-seat,  Colville
[Archaic.]
[or-sa']
```


## [2026-10-17T00:30:57.769Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'civet' SKT.txt | head -5; grep -n -i 'zobd\\|zubd\\|zabad\\|zubda' FVQ_pages.txt AFM_pages.txt incoming/PLA/PLA_pages.txt | head; grep -n 'زبد\\|زباد' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null| head -20; grep -n -i 'TYL\\|taylor' ../refs_online.json | head -3; grep -n -i 'civet\\|zibet' incoming/TYL/TYL_Taylor1934_BenJonson_pages.txt | head"
}
```


### [2026-10-17T00:30:58.156Z] TOOL RESULT

```
3483:^F.  -  AiaK)  P.  €h^m, Un  civet  «ftt:  bemwdfc
23702:French  from  Arabic:  admiral,  alcohol, assassin,  barberry  (berberry),  bedouin,  calif (caliph),  cipher,  civet,  fardel?,  furl?,  ga- zelle, lute  (1),  Mamaloke  (Mameluke), mattress,  mohair  (moiic),  saflron,  sultaa.
incoming/PLA/PLA_pages.txt:11976:Sııl,s.                  - firuzabadi:                    Nisba     v.        >11,,,»      firuzabad           q. v.
incoming/MON/MON_2vol_Adena_v2_djvu.txt:374:قاهر» بیروز. بخش زباد؛ سمت اعظم؛ اغلب 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:3861:به خیزبدن وا داشتن. به حرکت آوردن. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:3862:غیزیدن: 7]2-0 [- غیز بدن - خبزبدن - 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4075:آنجه از حد تحاوز کند؛ زباده از حد؛ سبار؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4076:و تفاوت فاحش: تفاوت زباد. علط 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4335:رودها و نهر ها نلروده آب زباد. ( تد.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:6980:خزیدن و لغزبدن. درنکک کردن؛ دیر ماندن. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:7269:فزوده: (۵-)02-10۸] (امسف.) زباده شده» 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:13547:ابری است که باران زبادی داشته باشد و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:16425:نفت در نه دیگ‌های تصفبه مقادیری زبادی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:17858:محر ب» ورزبده» آزموده؛ ج. . کا رکشتگان. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:21712:آنکه درجهٌ حرارت زباد شود (در حدودی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24115:کفران کردن. الحاد ورزبدن» بی‌دین بودن. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:26017:این: لااقل» حداقل. کم و پیش: کم و زباد» 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:31803:#4 سبار زباد» فراوان. بشت سر هم 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:32117:گریختن: ببلتاه اوزی ۱۳ - گریزبدن] (مص‌ل.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:34686:ِ (عم.) بسیار مدیون بودن» قرض زباد 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:39396:لسیع: ات۳ [ع.] (ص.) کزبده (مار و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:39767:(لغزبدء لغزد» خواهد لغزید؛ بلغزء لغزنده» 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:39768:لغزان؛ لغزبده» لغزش) سر خوردن؛ لیز 
571:  "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
589:  "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
1034: "TYL": {
119:  civet (4) 1599 (1532), and civet-wit 1600.
```


## [2026-10-17T00:31:04.200Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /tmp; for w in civet zibet Isaac %D8%B2%D8%A8%D8%A7%D8%AF %D8%B2%D8%A8%D8%AF %D8%B2%D8%A8%D8%AF%D8%A9 %D8%B6%D8%AD%D9%83 %D7%99%D7%A6%D7%97%D7%A7 %D8%A7%D8%B3%D8%AD%D8%A7%D9%82 %D9%85%D8%B6%D8%AD%DA%A9 %D8%B2%D8%A8%D8%AF%D9%87; do echo \"=== $w\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$w&action=raw\" | grep -i -A3 'etymology\\|{{bor\\|{{der\\|{{inh\\|root' | grep -v '^--$' | head -25; done"
}
```


### [2026-10-17T00:31:06.768Z] TOOL RESULT

```
=== civet
===Etymology===
From {{der|en|fr|civette}}, from {{der|en|it|zibetto}}, from {{der|en|la-med|zibethum}}, from {{der|en|ar|زَبَاد}}.

===Pronunciation===
* {{IPA|en|/ˈsɪ.vɪt/}}
===Etymology===
Compare {{cog|it|civetta}}, {{cog|rm|tschuetta}}, {{cog|fr|chouette}}.

===Noun===
===Etymology===
{{ety|fr|:af|cive|-et}}
From {{af|fr|cive|-et}}.

=== zibet
=== Isaac
===Etymology===
From {{inh|en|enm|Ysaac}}, from {{der|en|la|Isaac}}, from {{der|en|grc|Ἰσαάκ}}, from {{der|en|he|יצחק|lit=he laughs, he will laugh|tr=Yiṣḥāq}}. Explained in {{w|Book of Genesis|Genesis}} as referring to his mother [[Sarah]]’s laughing when she was told she would have a son at her old age. The verb is masculine, however, perhaps due to its use as a boy’s name.

===Pronunciation===
* {{IPA|en|/ˈaɪzək/}}
===Etymology===
{{ety|la|title=Isaāc|:bor|grc:Ἰσαᾱ́κ<ety:uder<hbo:יִצְחָק<tr:Yiṣḥāq><lit:he laughs>>>|text=2|tree=1}}

===Pronunciation===
===Etymology===
Borrowed from {{bor|ang|la|Isaāc}}, from {{der|ang|grc|Ἰσαάκ}}, from {{der|ang|hbo|יצחק|tr=Yiṣḥāq|lit=he laughs}}.

===Pronunciation===
* {{ang-IPA|Isaāc}}
=== %D8%B2%D8%A8%D8%A7%D8%AF
=== %D8%B2%D8%A8%D8%AF
===Etymology 1===
{{ar-rootbox|ز ب د}}
{{ety|ar|id=butter|:root|ز ب د<id:root>|tree=1}}

====Verb====
{{ar-verb|I/a~u.pass.vn:زَبْد}}
===Etymology 2===
{{ety|ar|nl=1}}

====Noun====
{{shu-root|ز ب د}}

===Etymology 1===
{{ety|shu|:inh|ar:زَبَّدَ|text=+|tree=1}}

====Verb====
===Etymology 2===
{{ety|shu|:inh|ar:زَبَد|text=+|tree=1}}

====Noun====
=== %D8%B2%D8%A8%D8%AF%D8%A9
{{ar-rootbox|ز ب د}}
{{ety|ar|id=butter|:root|ز ب د<id:root>|tree=1}}

===Pronunciation===
{{ar-pr|زُبْدَة}}
{{shu-root|ز ب د}}
[[File:2023 Masło w maselniczce.jpg|thumb|{{lang|shu|زبدة}}]]

===Etymology===
{{ety|shu|:inh|ar:زُبْدَة|text=+|tree=1}}

===Noun===
{{acw-root|ز ب د}}

===Etymology===
{{ety|acw|:inh|ar:زُبْدَة|text=+|tree=1}}

===Pronunciation===
{{ajp-root|ز ب د}}

===Etymology===
{{ety|ajp|:inh|ar:زُبْدَة|text=+|tree=1}}

===Pronunciation===
=== %D8%B6%D8%AD%D9%83
{{ety|ar|:root|ض ح ك<id:root>}}
{{ar-rootbox|ض ح ك}}

===Etymology 1.1===
Compare {{cog|he|צָחַק|tr=ṣāḥaq|t=to laugh}}.

====Pronunciation====
===Etymology 1.2===

====Pronunciation====
{{ar-pr|ضَحِكَ}}
===Etymology 1.3===

====Pronunciation====
{{ar-pr|ضَحَّكَ}}
{{shu-root|ض ح ك}}

===Etymology===
{{ety|shu|:inh|ar:ضَحِكَ|text=+|tree=1}}

===Verb===
{{arz-root|ض ح ك}}

===Etymology 1===
{{ety|arz|:inh|ar:ضَحِكَ|text=+|tree=1}}
=== %D7%99%D7%A6%D7%97%D7%A7
{{he-rootbox|צ־ח־ק}}

===Alternative forms===
* {{alt|he|יִשְׂחָק<tr:yiskhák, yiśḥāq>}}
===Etymology===
{{ety|he|id=prophet|:from|צָחַק<tr:tsakhák>}}
Grammatically, the third person singular imperfect of {{m|he|צָחַק|tr=tsakhák|t=to laugh}}.

===Etymology===
From {{bor|yi|he|יִצְחָק|tr=yitskhák}}. {{root|yi|he|צ־ח־ק}}

===Proper noun===
{{yi-proper noun|g=m|tr=yitskhok}}
=== %D8%A7%D8%B3%D8%AD%D8%A7%D9%82
===Etymology===
{{ety|ota|:bor|ar:إِسْحَاق|tree=1|text=++}}

===Proper noun===
===Etymology===
{{ety|fa|:bor|ar:إِسْحَاق<id:prophet>|id=prophet|text=+|tree=1}}

===Pronunciation===
===Etymology===
{{etymon|ur|:bor|fa-cls:اِسْحَاق<id:prophet>|id=prophet|text=++}}

===Pronunciation===
=== %D9%85%D8%B6%D8%AD%DA%A9
===Etymology===
{{bor+|fa|ar|مُضْحِك}}.

===Pronunciation===
{{fa-IPA|muzhik}}
=== %D8%B2%D8%A8%D8%AF%D9%87
```


## [2026-10-17T00:31:14.898Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'Ish[aā]q\\|Isaac' FVQ_pages.txt | head; grep -n -i 'zabad\\|zibet\\|civet' AFM_pages.txt LKT.txt DOZ.txt | head -5; curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%B2%D8%A8%D8%AF&action=raw\" | sed -n 1,60p | grep -i 'sense\\|^#' | head -20; curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%A5%D8%B3%D8%AD%D8%A7%D9%82&action=raw\" | grep -i -A3 'etym' | head"
}
```


### [2026-10-17T00:31:15.818Z] TOOL RESULT

```
2498:Isaac.
DOZ.txt:1031:ment civette, du mot arabe zebêd, qui signifie écume,
DOZ.txt:1036:Ducange), Ital. zihettOy Fr. civette. Wg hebben het
LKT.txt:582:'ümsonst,  gratis'  [Kelekian  233  b,  wohl aus  ar.  bädi-hawä  'Luft  verursachend'] ; hieraus  bulg.  badihawa,  badlawa  'dass.', serb.  badawad  'dass.',  slov.  badava  und mit  slav.  Präposition  zabadava  'verge- bens, umsonst'.    [Bern  SlEtWb  37.
LKT.txt:1614:'Parfüm  aus  Moschus  und  Ambra';  hier- aus sp.  algalia,  pg.  algälia  'dass.';  mlat. galia  muscata,  sp.  pg.  gato  de  algalia [Constancio  Dicc  50  b]  'Zibetkatze,  Vi- verra  civetta  Schreb.'.
LKT.txt:1691:'Zibetkatze'  [CHERBONNEAU  in  JAs 1849,  I,  541];  hieraus  frz.  genette,  sp. pg.  gineta  'Zibet-  oder  Risamkatze,  Vi- verra  genetta  L.'.  —  [*(.fa)gmetta  ist schon  von  DIEZ  als  Grundwort  zurück- gewiesen worden.]  [DE  276.  Eguilaz 413.    Devic  DEt  127.    ML  3949.
# to [[feed]] (someone) [[butter]]
# to [[churn]] (milk)
# to [[give]] (someone) a [[gift]]
# to make [[creamy]]
# to add [[cream]] to something
# to [[cause]] to [[foam]]
# [[butter]]
# [[cinder]]
# [[foam]]
# [[scum]]
# [[liquid]]
# {{ar-verbal noun of|زَبَدَ|form=I}}
===Etymology===
{{ety|ar|:bor|id=prophet|hbo:יִצְחָק<id:prophet><tr:yiṣḥāq>|text=+|tree=1}} Comparable to {{cog|ar|يَضْحَكُ}}.

===Pronunciation===
```


## [2026-10-17T00:31:18.254Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2485,2505p FVQ_pages.txt; head -n 2498 FVQ_pages.txt | tr -cd '\\f' | wc -c; sed -n 1026,1040p DOZ.txt; head -n 1031 DOZ.txt | tr -cd '\\f'|wc -c"
}
```


### [2026-10-17T00:31:18.578Z] TOOL RESULT

```
Mu'awiya I. Cf. Stackelberg in ZDAIG, xlviii, 490.
8 Fraenkel, Vocab, 25, quotes this as L. JI^AcD |, which is copied by Dvorak, Fremdw,
42, and Horovitz, Parodies, 16, but neither this form nor the (l^AflOl quoted by Addai
Sher, 10, is to be found in the Syriae Lexicons.
9 Mingana, Syriac Influetice, 88, however, claims that the borrowing was from Syr.
into Arabic.
10 The philologers had recognized, however, that Pers. <il did sometimes become ^
in Ar. Cf. SIbawaih in Siddiqi, 21.60 FOREIGN VOCABULARY OF THE QUR*AN
as Phlv. ^-utf)3O* avistak (= Pers. lx*%j| or lu*^!), 1 which in
Syr. is ^Afioaj^ an d in Ar. v3^l (Ibn al-Athlr, Nihaya, i, 38).
(Ishdq).
ii, 127-134 ; iii, 78 ; iv, 161 ; vi, 84 ; xi, 74 ; xii, 6, 38 ; xiv, 41 ;
xix, 50 ; xxi, 72 ; xxix, 26 ; xxxvii, 112, 113 ; xxxviii, 45.
Isaac.
The Biblical Patriarch, who is never mentioned save in connection
with one or more of the other Patriarchs, and never in an early passage.
It was early recognized by the philologers that it was a foreign
name, cf. Slbawaih in Siddiqi, 20, and LA, xii, 20 ; al-Jawallqi, Mu'ar-
rab, 9; as-Suyutl, Muzhir, i, 138; though it was not uncommon in some
quarters to regard it as an Arabic word derived from ^*~*>> for as-
Suyutl, Muzhir, i, 140, goes out of his way to refute this. It was even
77
Ën Maghten enx.
In hetzelfde treurspel gebruikt Vondel ook serafijn32
marchands de GhdameS; on excite ranimal; sou corps
se couvre alors d'une écume épaisse et blanche qu'on
recueille. Cette sécrétion odorante, appelée communé-
ment civette, du mot arabe zebêd, qui signifie écume,
prend k Fair une teinte noirStre. On renouvelle cette
opération tous les huit jours." Zie ook Lyon en Testa
op de aangeh. pi.
Reeds het Middeleeuwsche Latgn had zihethum (zie
Ducange), Ital. zihettOy Fr. civette. Wg hebben het
woord van de Franschen.
CXJBCTJMA.
Dit woord ^is ongetwijfeld door de Arabieren tot de
Europeanen gekomen, daar zg aan denzelfden geelen
43
```


## [2026-10-17T00:31:21.417Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2505,2520p FVQ_pages.txt"
}
```


### [2026-10-17T00:31:21.720Z] TOOL RESULT

```
Suyutl, Muzhir, i, 140, goes out of his way to refute this. It was even
known that it was Heb. (cf. ath-Tha'labi, Qisas, 76), and indeed Sura,
xi, 74, seems to show acquaintance with the popular Hebrew derivation
from pH2J.
The Arabic form which lacks the initial ** of the O.T. forms priX**
and pH2T would seem to point to a Christian origin, 2 cf. Gk. 'IcraaK,
Syr. t-QiAttLilor Q**CDl, 3 though it is true that in the Talmud we come
across a pO^K *12 "HO (Baba Mezi'a, 39 b ), showing a form with
initial vowel among the Babylonian Jews of the fourth century A.n. 4
The name >z*\ must have been known before the Qur'an, but no
pre-Islamic instances of it seem to occur, for those quoted by Cheikho,
Nasrdniya, 229, 230, are rightly rejected by Horovitz, K U, 91.
(Israil).
Occurs some 43 times. Cf. ii, 38.
1 West, Glossary, 13.
2 Spronger, Leben, ii, p. 336; Fraenkel, ZA, xv, 394; Horovit/., JPA T , 155, and
```


## [2026-10-17T00:31:31.224Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /tmp; for w in زبده زبد زباد مضحک اسحاق; do echo \"=== $w\"; curl -sL \"https://vajehyab.com/moein/$w\" | python3 -c \"\nimport sys,re,html;t=sys.stdin.read();t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S);t=html.unescape(re.sub(r'<[^>]+>',' ',t));t=re.sub(r'\\s+',' ',t)\ni=t.find('معین');print(t[:0]);\nfor m in re.finditer(r'.{0,30}(\\[ع\\.\\]|\\[ معر\\.\\]|\\[ ع \\.\\]|\\[ع \\.\\]).{0,250}',t): print(m.group(0)); break\nelse: print(t[1500:2300])\n\"; done"
}
```


### [2026-10-17T00:31:33.408Z] TOOL RESULT

```
=== زبده


=== زبد


=== زباد


=== مضحک


=== اسحاق
```


## [2026-10-17T00:31:38.617Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp; curl -sL -o vj570.html -w '%{http_code} %{url_effective}\\n' \"https://vajehyab.com/moein/%D8%B2%D8%A8%D8%A7%D8%AF\"; wc -c vj570.html; curl -sL -o ab570.html -w '%{http_code}\\n' \"https://abadis.ir/fatofa/%D8%B2%D8%A8%D8%A7%D8%AF/\"; wc -c ab570.html; grep -o 'معین.\\{0,400\\}' ab570.html | head -3"
}
```


### [2026-10-17T00:31:40.698Z] TOOL RESULT

```
200 https://vajehyab.com/moein/%D8%B2%D8%A8%D8%A7%D8%AF
10430 vj570.html
200
63142 ab570.html
معین و عمید، مترادف و متضاد و ... در فرهنگ لغت آبادیس - برای مشاهده کلیک کنید" />
معین,فارسی,انگليسی,عربی,اسم,رایگان,تلفظ" />
معین و عمید، مترادف و متضاد و ... در فرهنگ لغت آبادیس - برای مشاهده کلیک کنید"><meta itemprop="image" content="//img.abadis.ir/words/ز/زباد.webp">
```


## [2026-10-17T00:31:45.282Z] TOOL CALL #18: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-17T00:31:45.293Z] TOOL RESULT

```

```


## [2026-10-17T00:31:51.407Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /tmp; python3 - <<'EOF'\nimport re,html\nt=open('ab570.html',encoding='utf8').read()\nt=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S);t=html.unescape(re.sub(r'<[^>]+>',' ',t));t=re.sub(r'\\s+',' ',t)\nfor m in re.finditer(r'.{0,60}\\[ ?ع ?\\.? ?\\].{0,250}',t): print(m.group(0)); print('--')\nEOF"
}
```


### [2026-10-17T00:31:51.898Z] TOOL RESULT

```
سنور الزباد رباح . گویند دارویی خوش بو است فرهنگ معین (زَ ) [ ع . ] (اِ. ) مادة معطری که از حیوانی به همین نام گرفته می شود. فرهنگ عمید ۱. پستانداری شبیه گربه که از درون کیسه ای در زیر شکمش ماده ای خوش بو به دست می آید. ۲. روغن معطر و سیاه رنگی که از این حیوان به دست می آید. پیشنهاد کاربران بررسیِ واژگانِ "زبودن/زبا
--
```


## [2026-10-17T00:31:55.847Z] AGENT

Abadis works via curl. Fetching the others.


## [2026-10-17T00:31:57.494Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /tmp; for w in زبده زبد مضحک اسحاق; do echo \"=== $w\"; curl -sL \"https://abadis.ir/fatofa/$w/\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read()\nt=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S);t=html.unescape(re.sub(r'<[^>]+>',' ',t));t=re.sub(r'\\s+',' ',t)\ni=t.find('فرهنگ معین');print(t[i:i+350] if i>=0 else 'NO MOEIN')\n\"; done"
}
```


### [2026-10-17T00:32:03.993Z] TOOL RESULT

```
=== زبده
فرهنگ معین (زُ دِ ) [ ع . زبدة ] (اِ. ) ۱ - برگزیده از هر چیز. ۲ - خلاصه . فرهنگ عمید ۱. پسندیده از هرچیز. ۲. (اسم، صفت ) [قدیمی] خلاصه، برگزیده. واژه نامه بختیاریکا ( زِبده ) کره گاو مترادف ها compendium (اسم) اختصار، خلاصه، کوتاهی، زبده abstract (اسم) خلاصه، مجمل، چکیده، جدا کردن، زبده، معنی، رساله elite (اسم) زبده، نخبه، گلچین cream (اسم) زبده، 
=== زبد
فرهنگ معین (زَ بَ ) (اِ. ) کف . فرهنگ عمید کف روی آب یا شیر، کف. واژه نامه بختیاریکا ( زِبد ) زبر؛ رک و پوست کنه؛ صریح دانشنامه اسلامی [ویکی الکتاب] معنی زَبَدٌ : کف جوشان و کثافتی که روی مایع جوشیده مینشیند ریشه کلمه: زبد (۳ بار) «زَبَد» به معنای کف های روی آب و یا هر گونه کف می باشد و می دانیم بر روی آب زلال، کمتر کف آشکار می گردد، چرا که کف ها ب
=== مضحک
فرهنگ معین (مُ حِ ) [ ع . ] (اِفا. ) خنده آور. فرهنگ عمید ۱. خنده آور، خنده دار. ۲. (اسم، صفت ) [قدیمی] دلقک. دانشنامه عمومی مضحک (فیلم). مضحک ( انگلیسی: Foolish ) فیلمی در ژانر کمدی به کارگردانی دیو میرز است که در سال ۱۹۹۹ منتشر شد. از بازیگران آن می توان به مستر پی و ادی گریفن اشاره کرد. wiki: مضحک (فیلم) این نوشته برگرفته از سایت ویکی پدیا می با
=== اسحاق
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. لینک ها ح
```


## [2026-10-17T00:32:12.168Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c '' BQT_v2_pages.txt; grep -n 'زباد\\|زبده' BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt | head -5; grep -n 'مضحک\\|اسحاق' incoming/BQT/BQT_v4_pages.txt BQT_v1_pages.txt | head -5; grep -n -i 'zabad\\|zubd\\|ishak\\|ishāq' HRN.txt HUB.txt | head; grep -n 'زباد\\|زبده\\|اسحاق\\|مضحک' incoming/ARY/ARY_pages.txt | head -3; grep -n -i 'laugh' SYN.txt | head -3"
}
```


### [2026-10-17T00:32:12.513Z] TOOL RESULT

```
41071
incoming/BQT/BQT_v3_pages.txt:370:را زباد میگوبند ۱ » وچون زباد را در ‎es‏
incoming/BQT/BQT_v3_pages.txt:381:وخورند ‎Vo.‏ نام جانوری که زباداز آن‌حاسل
incoming/BQT/BQT_v3_pages.txt:422:1 - رك : زباد .
incoming/BQT/BQT_v3_pages.txt:1877:‏زباده بريك محل ‎ple‏ نداشته‌اند ۷ - و بمعنی
incoming/BQT/BQT_v3_pages.txt:2742:چشم کشیدن روشتابی چشم را زبادء کند و قوت
incoming/BQT/BQT_v4_pages.txt:22523:«اسحاق» ودرفقه» وجفت و توا «عیسو» بود . اسم وی از وافعه‌ای که در وقت ولادتش روی داد »
BQT_v1_pages.txt:3148:حقیفت آنست که مولانا بسحق‌اطممه (ابواسحاق علاح شیراژی) ۴ دریابان دیوان لطعمةً
BQT_v1_pages.txt:4499:۷.- مسا لك المما لك.( کتاب). ابو اسحاق | بر اهیم بن‌مصدفارسی
BQT_v1_pages.txt:21548:وبواسحاقی هردو میگوبند ۴ -وبسحاق اطعمه را
BQT_v1_pages.txt:32306:تقیز گو نه - سوداوی ۰ عبی , تندخری : «منصور بن اسحاق را برادر زاده‌ای بودیرنا
HUB.txt:5883:Ap. v ist zu b geworden in zaban^ zubdn *Zunge' =-
201:۱ ۱ سیار زباد باشد (تارد یخ‌های فوق میلادی هستند).
5292:به احتمال زباد واژه‌ی "پوده" (برهان قاطع :: ۴۲۵) هم از همین واجربشه است.
10294:به احتمال زباد واژه‌های "استر" (به چم "قاط" که جانوری" مقطوع اللسل است) و سترون" (به چم" پا کر د(وارييي.
3935:NG c¢gaxz7a, lit. ‘for slaughter’ (: o¢atw ‘slaughter’), used mainly for sheep and goats.
4407:8. SCr. krme ‘swine’ (with krmaca ‘sow’), deriv. of krma ‘fodder’ (5.12), krmiti ‘feed animals’, hence orig. the animal fattened for slaughter, but com- pletely specialized to ‘swine’. Berneker 668.
6059:Grk. cgay or pl. cdayat (both in Aristot.) ‘throat’, this prob. the earliest meaning of the word, whence o¢étw ‘cut the throat, slay’ (cf. Lat. iugulare ‘slay’ fr. cugulum ‘throat’) and the re- sulting common use of c¢ay as ‘slaugh- ter’. No accepted etym., but prob. con- nected, by a series of parallel root-forms, with o¢yt, Dor. opat (gen. -xés) ‘wasp’, o¢yv, Dor. cpav ‘wedge’, odiyyw ‘bind tight, constrict’, all with common notion of ‘narrow’. Cf. Dan. strube, etc., below, 4. (Different combinations in Walde-P, 2.651-53, 658.)
```


## [2026-10-17T00:32:15.491Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 365,385p incoming/BQT/BQT_v3_pages.txt; awk 'NR<=370' incoming/BQT/BQT_v3_pages.txt | grep -o '\\[pdf page [0-9]*\\]' | tail -1; sed -n 22518,22526p incoming/BQT/BQT_v4_pages.txt; awk 'NR<=22523' incoming/BQT/BQT_v4_pages.txt | grep -o '\\[pdf page [0-9]*\\]' | tail -1"
}
```


### [2026-10-17T00:32:15.878Z] TOOL RESULT

```
‎Kiel. 1937, 8. 36.
[pdf page 11]
شاخابه <۷۲۰ ۷

را زباد میگوبند ۱ » وچون زباد را در ‎es‏
‏شاخ کار میکنند وازجاتب زیرباد می‌آورندسبب
آن شاخ کاو میگوبند ۰۷ 1۱ ‎Sd‏ پا را
میگوبند» رآن
از سر انگفتان
پاست‌تاییخ ران
۲-بمعنی‌مطلق
بررسته‌ولمو کرده شاخ کاو
باشد خراه اسان وخواه ‎ols‏ وجماد که بتدریج
بز رک شوند ‎ .‏ ۱۳- استخوان پهلورا گویند .
‎VE‏ شرابی ‎ash‏ که با کلاب ‎aT‏ کنند
وخورند ‎Vo.‏ نام جانوری که زباداز آن‌حاسل
میشود ۸ .

شاخابه * - با اك بالف کنید» رت
بای ابجد » جوی کوچکی را کوبند که از رود-
[pdf page 11]
5 «لفت فرس ۰۹۹۷-۹۹

* هج , راست بود یعنی بیای کرده» «ایضاً ص۷8 . ‎٩‏ اسم صوت .

۷ 78000۳ (بسبری یمنی پاشنه را میگیرد) یکی از اجداد عبرانیان است . وی‌پسس
«اسحاق» ودرفقه» وجفت و توا «عیسو» بود . اسم وی از وافعه‌ای که در وقت ولادتش روی داد »
مشتق شده است «سفر پیدایش ۲۹:۲۵ این دوبرادر باهم اختلافی داءتند . پنقوب چون به لوز
(بیت ابل) رسید ء الهام یافت واز چانب خدا به «اسرائیل» مللب کردید . چون پر وی پوس
درمصر فدرت بافت اور بمصر طلبید و او بدانجا درگذفت و بنی اسرائیل هنگام رحلت از مصر
[pdf page 552]
```


## [2026-10-17T00:32:24.166Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; T=tools/fetch_source.py; \npython3 $T 'https://en.wiktionary.org/wiki/civet' --note 'page 570, root Z.b.d, civet < F civette < It zibetto < ML zibethum < Ar zabad' ;\npython3 $T 'https://en.wiktionary.org/wiki/زبد' --note 'page 570, root Z.b.d, Arabic zabada/zabad/zubd senses' ;\npython3 $T 'https://en.wiktionary.org/wiki/زبدة' --note 'page 570, root Z.b.d, Arabic zubda butter' ;\npython3 $T 'https://en.wiktionary.org/wiki/Isaac' --note 'page 570, root Z.h.k, Isaac < Latin < Greek < Hebrew Yishaq' ;\npython3 $T 'https://en.wiktionary.org/wiki/יצחק' --note 'page 570, root Z.h.k, Hebrew Yitzhak imperf. of tsahaq; alt Yishaq' ;\npython3 $T 'https://en.wiktionary.org/wiki/ضحك' --note 'page 570, root Z.h.k, Arabic dahika cognate Hebrew tsahaq' ;\npython3 $T 'https://en.wiktionary.org/wiki/إسحاق' --note 'page 570, root Z.h.k, Arabic Ishaq borrowed from Hebrew' ;\npython3 $T 'https://en.wiktionary.org/wiki/اسحاق' --note 'page 570, root Z.h.k, Persian Eshaq borrowed from Arabic' ;\npython3 $T 'https://en.wiktionary.org/wiki/مضحک' --note 'page 570, root Z.h.k, Persian mozhek borrowed from Arabic mudhik' ;\nfor w in زباد زبده زبد مضحک; do python3 $T \"https://abadis.ir/fatofa/$w/\" --note \"page 570, Moin entry for $w\"; done 2>&1 | tail -30"
}
```


### [2026-10-17T00:32:41.426Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ec4b3f68efa88177.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c1bc2128ee9d348e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ef6bcc847f618ecb.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6dc8112d486d6268.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3549dc27f660c164.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/12a3b8f19d111a60.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3073ff0b742fa91e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9ac20bbb287d89d0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d11f273ea062a0e9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1ca0658c637da942.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8efa9b8f625120de.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/49c7e462fc590e9f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dd6a371c65dff0db.txt
```


## [2026-10-17T00:34:27.157Z] TOOL CALL #24: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-570.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nAB=\"https://abadis.ir/fatofa/\"\nKLNciv={\"ref\":\"KLN:293\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 165 (printed pp.294-295; Nourai's 293 is one page off), grep '^civet,': 'civet ... F. civette, fr. It. zibetto, fr. Arab. zabād, ‘civet’, which is rel. to zabad, ‘foam, froth’, zubd, ‘cream’. Cp. zibet.'\"}\nLKT={\"src\":\"LKT\",\"where\":\"no. 2173, p.170 (LKT.txt line 4859)\",\"stance\":\"supports\",\"note\":\"'2173. Ar. zabād: Schaum; hieraus mit Imāla [ā > e] mlat. zibethum Zibetkatze [so genannt, weil sie eine stark riechende schaumartige Flüssigkeit absondert], it. zibetto, frz. civette; ndl. civet ... engl. civet.'\"}\nDEV={\"src\":\"DEV\",\"where\":\"pp.96-97 s.v. Civette (DEV.txt line 1152)\",\"stance\":\"partial\",\"note\":\"'Civette. Ital. zibetto ... C'est l'arabe zoubâd'; Devic notes the Arabs connect it with zoubd 'crème de lait' but thinks this 'une simple coïncidence' (animal from equatorial Africa).\"}\nLAM={\"src\":\"LAM\",\"where\":\"s.v. Civette (LAM.txt line 3417)\",\"stance\":\"supports\",\"note\":\"'Civette. Esp: civeta. Ital: zibetto. Le mot civette ne date que du 16e siècle. Il vient de zabâd qui désigne la substance parfumée'; footnote: zoubda 'crème de lait'.\"}\nPHN={\"src\":\"PHN\",\"where\":\"p.120-121 s.v. CIVETTE (PHN.txt line 3815)\",\"stance\":\"supports\",\"note\":\"'CIVETTE ... [zébâd] sécrétion odorante, sorte de musc ... le même animal s'appelle aussi zibet ... Comparez aussi l'italien zibetto et l'anglais civet.'\"}\nDOZ={\"src\":\"DOZ\",\"where\":\"p.31-32 s.v. CIVET (DOZ.txt line 1031, leaf 43)\",\"stance\":\"supports\",\"note\":\"'civette, du mot arabe zebêd, qui signifie écume ... Reeds het Middeleeuwsche Latijn had zibethum (zie Ducange), Ital. zibetto, Fr. civette.'\"}\nSKT={\"src\":\"SKT\",\"where\":\"appendix list (SKT.txt line 23702)\",\"stance\":\"supports\",\"note\":\"'French from Arabic: admiral, alcohol, assassin, ... civet ...' (main entry not OCR-greppable).\"}\nFSD={\"src\":\"FSD\",\"where\":\"vol.1 s.v. civet (FSD_vol1.txt line 67562)\",\"stance\":\"silent\",\"note\":\"'Civ'et ... An unctuous yellowish semiliquid substance of musk-like odor ... as the zibet or rasse'; etymology bracket not legible in OCR.\"}\nTYL={\"ref\":\"TYL:568\",\"status\":\"not_checked\",\"note\":\"Taylor 1933 SPE tract not available; local TYL file is Taylor 1934 (Ben Jonson) which lists 'civet (4) 1599 (1532), and civet-wit 1600' (TYL_Taylor1934_BenJonson_pages.txt line 119) — confirms early English use, not the cited page.\"}\nMONnc=lambda r,w,q: {\"ref\":r,\"status\":\"supports\",\"note\":f\"Mo'in via abadis.ir/fatofa/{w}/ (page number not shown online): '{q}'\"}\nFVA={\"ref\":\"FVA:176\",\"status\":\"not_checked\",\"note\":\"Nahvi, Farhang-e vazheha-ye arabi: no digital copy (refs_online.json).\"}\nAKM={\"ref\":\"AKM:31\",\"status\":\"not_checked\",\"note\":\"A'lam, Farhang-e a'lam-e ketab-e moqaddas: purchase only, no digital copy.\"}\nFVA2={\"ref\":\"FVA:239\",\"status\":\"not_checked\",\"note\":\"Nahvi, Farhang-e vazheha-ye arabi: no digital copy (refs_online.json).\"}\nKLNis={\"ref\":\"KLN:816\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 441 (printed pp.816-817), grep '^Isaac,': 'Isaac ... Late L., fr. Gk. Isaak, fr. Heb. Yitzhāq, lit. ‘he laughs’, prop. imperf. of tzāhāq, ‘he laughed’, which is rel. to Aram.-Syr. gĕhekh, Arab. dahika, ‘he laughed’.'\"}\nFVQis={\"src\":\"FVQ\",\"where\":\"pp.60-61 s.v. Ishāq (FVQ_pages.txt leaf 77, line 2496)\",\"stance\":\"supports\",\"note\":\"'Ishāq. Isaac ... early recognized by the philologers that it was a foreign name ... known that it was Heb. ... The Arabic form which lacks the initial y of the O.T. forms ... would seem to point to a Christian origin, cf. Gk. Isaak, Syr. Ishaq.'\"}\nHRNs=lambda w: {\"src\":\"HRN\",\"where\":\"HRN.txt grep\",\"stance\":\"silent\",\"note\":f\"Horn treats only inherited Persian words; no entry for {w} (Arabic loan).\"}\nHUBs=lambda w: {\"src\":\"HUB\",\"where\":\"HUB.txt grep\",\"stance\":\"silent\",\"note\":f\"no entry for {w} (Arabic loan).\"}\nARYs=lambda w: {\"src\":\"ARY\",\"where\":\"ARY_pages.txt grep\",\"stance\":\"silent\",\"note\":f\"{w} not in Aryanpur (IE roots only); only unrelated OCR hits 'زباد' (=زیاد).\"}\nAFMs=lambda w: {\"src\":\"AFM\",\"where\":\"AFM_pages.txt grep\",\"stance\":\"silent\",\"note\":f\"{w} absent: Addi Shir lists Persian loans in Arabic; this is native Arabic.\"}\n\ne0nodes=[\n dict(id=1,lang=\"Arabic\",words=\"zobd; zobdeh; zabad\",verdict=\"confirmed\",\n  derivation=\"All three are regular nominal derivatives of Arabic root z-b-d (verb zabada 'to churn; feed butter; foam'): zubd 'fresh butter, cream' (Nourai's zobd is the Persian-style reading of zubd), zubda (zubdah) 'butter, cream' and figuratively 'the best, quintessence of anything' (Persian zobde), and zabad 'foam, froth, scum'. The semantic core is the substance that rises to the top of churned milk or of a boiling liquid; 'best part' is the metaphorical extension ('cream of the crop'). 'Skilled, talented' is a Persian usage (zobde-ye ostâdân), not a primary Arabic sense.\",\n  derivation_fa=\"«زُبد» (زُبد، خوانش عربی zubd «کرهٔ تازه، سرشیر»)، «زُبدة» (zubda «کره؛ برگزیدهٔ هر چیز») و «زَبَد» (zabad «کف روی آب یا شیر») همه از ریشهٔ سه‌حرفی عربی ز-ب-د ساخته شده‌اند که فعل زَبَدَ به معنای «کره گرفتن، کف کردن» از آن است. هستهٔ معنایی، چیزی است که بر روی شیرِ زده یا مایعِ جوشیده بالا می‌آید؛ معنای «برگزیده» تحول معنایی استعاری همین است (مانند cream انگلیسی). معنای «ماهر، کاردان» کاربرد فارسی است. ادعای نورایی درست است.\",\n  sources=[W+\"زبد\",W+\"زبدة\"],ref_check=[FVA],\n  consulted=[{\"src\":\"KLN\",\"where\":\"leaf 165, s.v. civet\",\"stance\":\"supports\",\"note\":\"'zabad, ‘foam, froth’, zubd, ‘cream’' as Arabic words of the same root.\"},\n   {\"src\":\"DEV\",\"where\":\"p.97 s.v. Civette\",\"stance\":\"supports\",\"note\":\"'zoubd, crème de lait'.\"},\n   {\"src\":\"LAM\",\"where\":\"s.v. Civette footnote 2\",\"stance\":\"supports\",\"note\":\"'zoubda. Ce mot signifiant crème de lait, écume, beurre frais'.\"},AFMs(\"zubd/zabad\")]),\n dict(id=2,lang=\"Persian\",words=\"zobdeh; zabad\",verdict=\"confirmed\",\n  derivation=\"Persian zobde < Arabic zubda(h) with the Persian rendering of final tā' marbūṭa as -e and of short u as o; meaning narrowed to 'the choice, best part; summary' (zobde-ye ... 'the elite of ...'). Persian zabad < Arabic zabad 'foam' kept as a literary word (Qur'anic zabad, Sura 13:17). Mo'in tags zobde as [ع. زبدة] and glosses zabad 'کف'.\",\n  derivation_fa=\"«زُبده» وام‌واژه‌ای از عربی «زُبدة» است: تای گرد پایانی عربی در فارسی به -ه (e) بدل شده و ضمهٔ کوتاه u در فارسی o خوانده می‌شود؛ معنای آن در فارسی به «برگزیده، خلاصه» محدود شده است. «زَبَد» نیز از عربی zabad «کف» است و در زبان ادبی (و قرآن، رعد ۱۷) به کار رفته. معین زبده را [ع. زبدة] و زبد را «کف» معنی کرده است. ادعای نورایی درست است.\",\n  sources=[AB+\"زبده/\",AB+\"زبد/\"],\n  ref_check=[MONnc(\"MON:1722\",\"زبده\",\"زُبده (زُ دِ) [ع. زبدة] (اِ.) ۱- برگزیده از هر چیز. ۲- خلاصه\")],\n  consulted=[{\"src\":\"MON\",\"where\":\"abadis.ir s.v. زبد\",\"stance\":\"supports\",\"note\":\"'زَبَد (زَ بَ) (اِ.) کف.'\"},HRNs(\"zobde\"),HUBs(\"zobde\"),ARYs(\"zobde\")]),\n dict(id=3,lang=\"Arabic\",words=\"zabâd\",verdict=\"plausible\",\n  derivation=\"Arabic zabād 'civet (the musky secretion)' and sinnawr az-zabād / qiṭṭ az-zabād 'civet cat'. Klein, Lokotsch, Lammens and Pihan relate it to zabad 'foam' (the secretion is a frothy unctuous substance, scraped off the animal's pouch); Devic (1876) considered the link with zubd a mere coincidence, but no rival etymology is known, and the word is formally a regular fa'āl derivative of z-b-d. The secretion sense is primary, the animal sense secondary.\",\n  derivation_fa=\"عربی «زَباد» نام مادهٔ خوشبوی مُشک‌مانندی است که از کیسهٔ زیر دم گربهٔ زباد (سِنَّور الزَباد) گرفته می‌شود و سپس نام خود جانور شده است. کلاین، لوکوچ، لامنس و پیهان آن را از همان ریشهٔ ز-ب-د و هم‌خانواده با «زَبَد» (کف) می‌دانند، چون این ماده کف‌مانند و چرب است؛ ولی دویک (۱۸۷۶) این پیوند را تصادفی شمرده است. ریشه‌شناسی دیگری پیشنهاد نشده، پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[W+\"civet\"],ref_check=[KLNciv],consulted=[LKT,DEV,LAM,PHN]),\n dict(id=4,lang=\"Persian\",words=\"zabâd\",verdict=\"confirmed\",\n  derivation=\"Persian zabâd 'civet (perfume); civet cat' is a direct loan of Arabic zabād, used in classical medicine and perfumery texts; Mo'in tags it [ع.] 'ماده معطری که از حیوانی به همین نام گرفته می‌شود'. Borhan-e Qate' (s.v. شاخ) also uses zabâd for the perfume and 'the animal from which zabâd is obtained'.\",\n  derivation_fa=\"«زَباد» فارسی وام‌واژهٔ مستقیم از عربی «زَباد» است و در متون پزشکی و عطرسازی کهن به معنای مادهٔ خوشبوی گربهٔ زباد و خود این جانور به کار رفته است. معین آن را [ع.] و «مادهٔ معطری که از حیوانی به همین نام گرفته می‌شود» آورده و برهان قاطع نیز ذیل «شاخ» از «جانوری که زباد از آن حاصل می‌شود» یاد می‌کند. ادعای نورایی درست است.\",\n  sources=[AB+\"زباد/\"],\n  ref_check=[MONnc(\"MON:1718\",\"زباد\",\"زباد (زَ) [ع.] (اِ.) مادة معطری که از حیوانی به همین نام گرفته می شود\")],\n  consulted=[{\"src\":\"BQT\",\"where\":\"vol.3 s.v. شاخ (BQT_v3_pages.txt line 370-382, pdf page 11)\",\"stance\":\"supports\",\"note\":\"'... را زباد میگویند ... نام جانوری که زباد از آن حاصل میشود' — zabâd used as perfume and animal name.\"},HRNs(\"zabâd\"),ARYs(\"zabâd\")]),\n dict(id=5,lang=\"Italian\",words=\"zibetto\",verdict=\"confirmed\",\n  derivation=\"Italian zibetto 'civet' < Medieval Latin zibethum (attested in Ducange), from Arabic zabād with imāla (ā > e, i.e. colloquial zebēd), and Romance reduction of the unstressed first vowel to i; Venice and Genoa were the conduits of the Levantine musk trade. Lokotsch and Dozy give this exact chain.\",\n  derivation_fa=\"ایتالیایی zibetto «گربهٔ زباد و مشک آن» از لاتین سده‌های میانه zibethum (گواهی‌شده در دوکانژ) و آن از عربی «زَباد» با امالهٔ ā به e (تلفظ عامیانهٔ zebēd) آمده است؛ بازرگانی مشک از راه ونیز و جنوا این واژه را به ایتالیا رساند. لوکوچ و دوزی همین زنجیره را می‌دهند. ادعای نورایی درست است.\",\n  sources=[W+\"civet\"],ref_check=[KLNciv],consulted=[LKT,DOZ,LAM]),\n dict(id=6,lang=\"French\",words=\"civette\",verdict=\"confirmed\",\n  derivation=\"French civette (16th c.; Belon 1553 has civetta) < Italian zibetto (or its variant civetta), with z- > c- [s] and the French diminutive-looking suffix -ette replacing -etto; French also has the doublet zibet(h) for the Asian species. Lammens, Devic, Pihan and Dozy all derive civette from Arabic zabād via Italian.\",\n  derivation_fa=\"فرانسوی civette (سدهٔ شانزدهم؛ بلون ۱۵۵۳ civetta) از ایتالیایی zibetto/civetta گرفته شده، با بدل شدن z آغازی به c (س) و جانشینی پسوند ‎-ette‎ به جای ‎-etto‎؛ فرانسوی دوگانهٔ zibet(h) را نیز برای گونهٔ آسیایی دارد. لامنس، دویک، پیهان و دوزی همگی civette را از عربی «زَباد» از راه ایتالیایی می‌دانند. ادعای نورایی درست است.\",\n  sources=[W+\"civet\"],ref_check=[KLNciv],consulted=[LAM,DEV,PHN,DOZ]),\n dict(id=7,lang=\"English\",words=\"civet, zibet\",verdict=\"confirmed\",\n  derivation=\"English civet (1532 for the perfume, Taylor; later the animal, 'civet cat') < French civette; zibet (zibeth) 'Asiatic civet, Viverra zibetha' is the doublet taken directly from Italian zibetto / Medieval Latin zibethum. Klein: 'F. civette, fr. It. zibetto, fr. Arab. zabād ... Cp. zibet'; Klein 1971 has 'zibet, also zibeth, n., the Asiatic or Indian civet'.\",\n  derivation_fa=\"انگلیسی civet (۱۵۳۲ برای مادهٔ خوشبو و سپس برای جانور) از فرانسوی civette است، و zibet (zibeth) «گربهٔ زباد آسیایی» دوگانهٔ آن است که مستقیم از ایتالیایی zibetto یا لاتین میانه zibethum گرفته شده. کلاین هر دو را به عربی «زَباد» می‌رساند. ادعای نورایی درست است.\",\n  sources=[W+\"civet\"],ref_check=[KLNciv,TYL],\n  consulted=[SKT,FSD,{\"src\":\"KLN\",\"where\":\"KLN_1971.txt line 270597\",\"stance\":\"supports\",\"note\":\"'zibet, also zibeth, n., the Asiatic or Indian civet.'\"},LKT]),\n]\ne0=dict(entry=0,root=\"Z.b.d\",verdict=\"confirmed\",modern_form=\"Arabic root z-b-d (زبد): zabada 'to churn butter; to foam'; zubd/zubda 'butter, cream', zabad 'foam'\",\n note=\"Arabic triliteral root z-b-d is correctly labelled and glossed (Wiktionary: zabada 'to churn (milk), to feed butter, to cause to foam'). The civet branch (zabād > It. zibetto > F. civette > E. civet) is standard (Klein, Lokotsch 2173, Dozy, Lammens, Pihan); only the semantic link zabād 'civet' ~ zabad 'foam' was doubted by Devic.\",\n note_fa=\"ریشهٔ سه‌حرفی عربی ز-ب-د با فعل زَبَدَ «کره گرفتن، کف کردن» و اسم‌های زُبد/زُبدة «کره، سرشیر» و زَبَد «کف» درست ثبت شده است. شاخهٔ «زَباد» (مشک گربهٔ زباد) و رسیدن آن از ایتالیایی zibetto و فرانسوی civette به انگلیسی civet را کلاین، لوکوچ، دوزی، لامنس و پیهان تأیید می‌کنند؛ تنها دویک پیوند زباد با زبد را تصادفی دانسته است. ادعای نورایی درست است.\",\n sources=[W+\"زبد\",W+\"civet\"],ref_check=[FVA],\n consulted=[{\"src\":\"KLN\",\"where\":\"leaf 165 s.v. civet\",\"stance\":\"supports\",\"note\":\"'zabad, foam, froth, zubd, cream'.\"},LKT,AFMs(\"root z-b-d\")],nodes=e0nodes)\n\ne2nodes=[\n dict(id=1,lang=\"Arabic\",words=\"z.h.k, zahika; mozhek\",verdict=\"confirmed\",\n  derivation=\"Arabic ḍaḥika (ضحك) 'he laughed', root ḍ-ḥ-k; Nourai writes the root Z.h.k because ض is pronounced z in Persian (Klein spells 'dahika'). mozhek is the Persian reading of Arabic muḍḥik, active participle of form IV aḍḥaka 'to make laugh', i.e. 'laughable, funny'. Arabic ḍ (< Proto-Semitic *ṣ́) corresponds regularly to Hebrew ṣ (tsade), so ḍaḥika is cognate with Hebrew ṣāḥaq.\",\n  derivation_fa=\"عربی «ضَحِکَ» (ḍaḥika) «خندید» از ریشهٔ ض-ح-ک است؛ نورایی ریشه را Z.h.k نوشته چون «ض» در فارسی «ز» تلفظ می‌شود. «مُضحِک» (muḍḥik) اسم فاعل باب اِفعال (أضحَکَ «خنداندن») و به معنای «خنده‌آور» است. ض عربی (از سامی آغازین *ṣ́) به‌طور منظم با صاد عبری (ṣ) برابر است، پس ضحک هم‌ریشهٔ عبری ṣāḥaq است. ادعای نورایی درست است.\",\n  sources=[W+\"ضحك\"],ref_check=[KLNis],\n  consulted=[{\"src\":\"FVQ\",\"where\":\"p.61 s.v. Ishāq\",\"stance\":\"supports\",\"note\":\"Jeffery notes that some Arab philologers derived Ishāq from Arabic (refuted by as-Suyūṭī), and that Sura xi 74 'seems to show acquaintance with the popular Hebrew derivation' from the 'laugh' root.\"},AFMs(\"ḍaḥika\")]),\n dict(id=2,lang=\"Persian\",words=\"mozhek\",verdict=\"confirmed\",\n  derivation=\"Persian mozhek 'funny, ridiculous' (also older 'jester') < Arabic muḍḥik, with Persian z for ḍ and o for short u; Mo'in tags it [ع.] (اِفا.) 'خنده‌آور'.\",\n  derivation_fa=\"«مُضحِک» فارسی (مُزحِک تلفظ می‌شود) وام‌واژه از عربی «مُضحِک» است: ض در فارسی ز و ضمهٔ کوتاه o خوانده می‌شود. معین آن را [ع.] اسم فاعل به معنای «خنده‌آور» آورده است. ادعای نورایی درست است.\",\n  sources=[W+\"مضحک\",AB+\"مضحک/\"],ref_check=[FVA2],\n  consulted=[{\"src\":\"MON\",\"where\":\"abadis.ir s.v. مضحک\",\"stance\":\"supports\",\"note\":\"'مضحک (مُ حِ) [ع.] (اِفا.) خنده آور.'\"},HRNs(\"mozhek\"),HUBs(\"mozhek\"),ARYs(\"mozhek\")]),\n dict(id=3,lang=\"Hebrew\",words=\"tzâhaq; Yitzhâq, Yišâq\",verdict=\"confirmed\",\n  derivation=\"Hebrew ṣāḥaq (צחק) 'he laughed' (root ṣ-ḥ-q); Yiṣḥāq (יצחק) is formally its 3rd masc. sg. imperfect 'he laughs / will laugh', explained in Genesis 17-21 by Abraham's and Sarah's laughter. The variant Yiśḥāq (ישחק, Jer 33:26, Amos 7:9, Ps 105:9) shows the by-form śāḥaq 'laugh'; Nourai's 'Yišâq' renders this śin-form (with the ḥ omitted). Cognate with Arabic ḍaḥika and Aramaic-Syriac g'ḥek.\",\n  derivation_fa=\"عبری ṣāḥaq (צחק) «خندید» است و Yiṣḥāq (یصحاق، יצחק) از نظر دستوری سوم‌شخص مفرد مذکر مضارع آن، یعنی «می‌خندد»؛ سِفر پیدایش این نام را با خندهٔ ابراهیم و سارا هنگام مژدهٔ فرزند توضیح می‌دهد. گونهٔ Yiśḥāq (ישחק) در ارمیا و عاموس و مزامیر از صورت دیگر فعل śāḥaq است. این ریشه هم‌ریشهٔ عربی «ضحک» و آرامی-سریانی g'ḥek است. ادعای نورایی درست است.\",\n  sources=[W+\"יצחק\",W+\"Isaac\"],ref_check=[KLNis],consulted=[FVQis,{\"src\":\"SKT\",\"where\":\"SKT.txt grep 'Isaac'\",\"stance\":\"silent\",\"note\":\"no entry for the proper name.\"}]),\n dict(id=4,lang=\"Arabic\",words=\"\",verdict=\"confirmed\",\n  derivation=\"Pass-through node for Arabic Isḥāq (إسحاق), the Qur'anic form of Isaac (17 occurrences). Jeffery: the Arabic form, lacking initial y-, points to a Christian (Syriac/Greek) intermediary; Wiktionary gives it as a borrowing from Biblical Hebrew Yiṣḥāq. Either way it ultimately continues the Hebrew name.\",\n  derivation_fa=\"این گره گذرگاه عربی «إسحاق» است که صورت قرآنی نام اسحاق است. جفری می‌گوید نبودِ «ی» آغازی در صورت عربی نشان می‌دهد که نام از راه مسیحیان (سریانی یا یونانی) به عربی رسیده است؛ ویکی‌واژه آن را وام از عبری Yiṣḥāq می‌داند. در هر حال ریشهٔ نهایی همان نام عبری است. ادعای نورایی درست است.\",\n  sources=[W+\"إسحاق\"],ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference.\"}],\n  consulted=[FVQis,AFMs(\"Isḥāq\")]),\n dict(id=5,lang=\"Persian\",words=\"Es-hâq\",verdict=\"confirmed\",\n  derivation=\"Persian Eshâq (اسحاق, also written اسحق with dagger alif) < Arabic Isḥāq, the Islamic form of the patriarch's name, used as a personal name (Abu Eshâq) and in poetry (the quoted Molavi verse refers to the sacrifice story). Persian e- for Arabic i- and h for ḥ are regular.\",\n  derivation_fa=\"«اسحاق» (و «اسحق» با الف مقصوره) در فارسی از عربی «إسحاق» آمده و صورت اسلامی نام پیامبر است که در نام‌هایی مانند «ابواسحاق» و در شعر (بیت مولوی دربارهٔ داستان قربانی) به کار رفته. کسرهٔ عربی در آغاز به e فارسی و ح به h بدل شده است. ادعای نورایی درست است.\",\n  sources=[W+\"اسحاق\"],ref_check=[AKM],\n  consulted=[{\"src\":\"BQT\",\"where\":\"vol.4 s.v. یعقوب (BQT_v4_pages.txt line 22523, pdf page 552)\",\"stance\":\"supports\",\"note\":\"'... پسر «اسحاق» و رفقه، و جفت و توأم «عیسو» بود' — Mo'in uses اسحاق for the biblical patriarch.\"},HRNs(\"Eshâq\"),ARYs(\"Eshâq\")]),\n dict(id=6,lang=\"Greek\",words=\"Isaak\",verdict=\"confirmed\",\n  derivation=\"Septuagint and New Testament Greek Isaák (Ἰσαάκ) transcribes Hebrew Yiṣḥāq: initial yi- > i-, ṣ > s, the pharyngeal ḥ is dropped (Greek had no such sound), giving Isa-ák; undeclined.\",\n  derivation_fa=\"یونانی Isaák (Ἰσαάκ) در ترجمهٔ هفتادی و عهد جدید آوانویسی عبری Yiṣḥāq است: yi- آغازی به i-، ص به s، و ح حلقی که یونانی نداشت افتاده است؛ این نام صرف نمی‌شود. ادعای نورایی درست است.\",\n  sources=[W+\"Isaac\"],ref_check=[KLNis],consulted=[FVQis,{\"src\":\"SKT\",\"where\":\"SKT.txt grep 'Isaac'\",\"stance\":\"silent\",\"note\":\"no entry.\"}]),\n dict(id=7,lang=\"Late Latin\",words=\"Isaacus\",verdict=\"confirmed\",\n  derivation=\"Late/Church Latin Isaac, declined Isaacus in some texts (Vulgate keeps indeclinable Isaac), taken from Greek Isaák in the Vetus Latina and Vulgate.\",\n  derivation_fa=\"لاتین متأخر و کلیسایی Isaac (و در برخی متن‌ها صورت صرف‌شدهٔ Isaacus) از یونانی Isaák در ترجمه‌های لاتین کتاب مقدس (وتوس لاتینا و ولگاتا) گرفته شده است. ادعای نورایی درست است.\",\n  sources=[W+\"Isaac\"],ref_check=[KLNis],consulted=[FVQis,{\"src\":\"LAT\",\"where\":\"LAT.txt (Ernout-Meillet)\",\"stance\":\"silent\",\"note\":\"proper names of the Bible not treated.\"}]),\n dict(id=8,lang=\"English\",words=\"Isaac\",verdict=\"confirmed\",\n  derivation=\"English Isaac (Old English Isaāc, Middle English Ysaac) from Latin Isaac, with the spelling-pronunciation /ˈaɪzək/ after the Great Vowel Shift; masculine given name and the patriarch.\",\n  derivation_fa=\"انگلیسی Isaac (انگلیسی کهن Isaāc، میانه Ysaac) از لاتین Isaac گرفته شده و پس از دگرگونی بزرگ واکه‌ها /آیزِک/ تلفظ می‌شود؛ نام پیامبر و نام مردانه است. ادعای نورایی درست است.\",\n  sources=[W+\"Isaac\"],ref_check=[KLNis],consulted=[{\"src\":\"SKT\",\"where\":\"SKT.txt grep 'Isaac'\",\"stance\":\"silent\",\"note\":\"no entry for the proper name.\"},{\"src\":\"FSD\",\"where\":\"FSD_vol4 grep 'Isaac'\",\"stance\":\"silent\",\"note\":\"only as personal names (Isaac K. Funk, Isaac Pitman); no etymology.\"}]),\n]\ne2=dict(entry=2,root=\"Z.h.k\",verdict=\"confirmed\",modern_form=\"Proto-Semitic *ṣ́-ḥ-k 'to laugh': Arabic ḍ-ḥ-k (ضحك), Hebrew ṣ-ḥ-q (צחק), Aramaic g-ḥ-k\",\n note=\"The root is real; 'Z.h.k' is the Persian-style rendering of Arabic ḍ-ḥ-k (ض pronounced z in Persian), not a transcription error. Klein 816 gives the whole Isaac chain and the Arabic cognate dahika. Hebrew ṣ = Arabic ḍ = Aramaic ʿ/g reflects Proto-Semitic *ṣ́.\",\n note_fa=\"ریشهٔ سامی «خندیدن» واقعی است: عربی ض-ح-ک، عبری ص-ح-ق و آرامی گ-ح-ک، همه از سامی آغازین *ṣ́-ḥ-k. نوشتن آن به صورت Z.h.k از آن روست که «ض» در فارسی «ز» تلفظ می‌شود و خطای چاپی نیست. کلاین (ص ۸۱۶) زنجیرهٔ Isaac را از عبری Yiṣḥāq «می‌خندد» تا انگلیسی می‌دهد. ادعای نورایی درست است.\",\n sources=[W+\"ضحك\",W+\"יצחק\"],ref_check=[KLNis],consulted=[FVQis,AFMs(\"root ḍ-ḥ-k\")],nodes=e2nodes)\n\nout=dict(pdf_page=570,book_page=540,verified_by=\"claude-opus-5.5\",verified_on=\"2026-10-16\",entries=[e0,e2])\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-570.json','w',encoding='utf8'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-570.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-570.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 570"
}
```


### [2026-10-17T00:34:27.697Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'confirmed': 14, 'plausible': 1}
root verdicts: {'confirmed': 2}
ref checks: {'not_checked': 5, 'supports': 11}
books consulted: {'supports': 24, 'silent': 19, 'partial': 2} | by book: {'FVQ': 5, 'LAM': 4, 'HRN': 4, 'ARY': 4, 'SKT': 4, 'DEV': 3, 'AFM': 3, 'LKT': 3, 'KLN': 2, 'MON': 2, 'HUB': 2, 'PHN': 2, 'BQT': 2, 'DOZ': 2, 'FSD': 2, 'LAT': 1}
```


## [2026-10-17T00:34:36.963Z] TOOL CALL #25: SubagentHandback

```json
{
 "message": "I verified PDF page 570 (book page 540) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-570.json. The JSON is valid and `verify_check.py 570` shows 0 PROBLEM lines.\n\n- **Coverage:** 15 nodes across 2 roots. I skipped the redirects Zgwes → Gwes and Zi → Zay.\n- **Roots:** both confirmed (Z.b.d and Z.h.k).\n- **Nodes:** 14 confirmed, 1 plausible, none disputed or transcription_suspect.\n- **Plausible node:** Z.b.d #3, Arabic zabâd \"civet\" from the root of zabad \"foam\". Klein, Lokotsch no. 2173, Lammens and Pihan support this link. Devic (1876) calls the link to zubd \"une simple coïncidence\". No other etymology exists.\n- **Z.h.k label:** \"Z.h.k\" is Nourai's Persian-style spelling of Arabic ḍ-ḥ-k (ضحك), because ض is pronounced z in Persian. It is not a misprint. Klein spells it \"dahika\".\n- **Nourai's references:**\n  - KLN:816 (Isaac) supports the arrows exactly.\n  - KLN:293 (civet) also supports them, but the local 1966 copy has the entry on the leaf for pp. 294–295, so the citation is about one page off.\n  - Mo'in (MON:1718/1722) supports, checked on abadis.ir.\n  - FVA, AKM and TYL could not be checked; no copies are available.\n- **Extraction errors:** none. The JSON matches the chart text. I didn't render the printed page because no node needed a transcription flag.\n\nI archived all the web sources I used with fetch_source.py: 9 Wiktionary pages and 4 Mo'in entries on abadis.ir."
}
```


### [2026-10-17T00:34:37.274Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
