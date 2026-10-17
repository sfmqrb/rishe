# Verification process log — verify-page-566


## [2026-10-17T00:30:14.366Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 566 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-566.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-566.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-566.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 566` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.433Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:20.067Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:20.089Z] TOOL RESULT

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


## [2026-10-17T00:30:20.573Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-566.txt"
}
```


### [2026-10-17T00:30:20.590Z] TOOL RESULT

```
1	=== PDF page 566 (book page 536) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Yeu 3 : to mix, blend  (refs POK:507)
4	#1 (parent #0) [Sanskrit] refs=POK:507 | yuš : juice, broth made by boiling in water
5	  #2 (parent #1) [Persian] refs=BQT:600; MON:1254 | jŭšîdan «جوشیدن» : to boil | extra: جوش ، جوشش
6	#3 (parent #0) [Avestan] refs=SOD:117 | yaěš : to boil
7	  #4 (parent #3) [Sogdian] refs=SOD:117 | byěš : to boil
8	#5 (parent #0) [Greek] refs=AHD | zumě : leaven ; en-zumě : leavened
9	  #6 (parent #5) [French] refs=None | ensyme : enzyme
10	    #7 (parent #6) [Persian] refs=AMD:57 | ânzîm «آنزیم» : enzyme
11	  #8 (parent #5) [English] refs=None | enzyme
12	#9 (parent #0) [Latin] refs=AHD | jŭs : juice
13	  #10 (parent #9) [English] refs=None | juice
14	#11 (parent #0) [Indo-European] refs=KLN:833; POK:512 | yeu-dh : shaken, active, fight ; yeug : ready to fight
15	  #12 (parent #11) [Avestan] refs=KLN:833; POK:512; IEC:446 | yaod, yaošti : active, searching ; yaoz, yaozaiti : search, fight
16	    #13 (parent #12) [Pahlavi] refs=BQT:571 | jôyšn : search
17	      #14 (parent #13) [Persian] refs=BQT:571; FFD:47 | jostan «جُستن» : search | extra: ( جوییدن )
18	جو ۲ ، جوی ۲ ( دانشجوی )
19	    #15 (parent #12) [Persian] refs=BQT:2457; MON:5272 | yŭz «یوز» : hunting dog, fighting ; yŭzpalang «یوزپلنگ» : a small fast leopard ☞Pard ; yŭzîdan «یوزیدن» : to be active, to search | extra: یوزه ، یوزک
20	    #16 (parent #12) [Sogdian] refs=SOD:15 | â-ywdy : to struggle, try
21	--- entry 1 ---
22	ROOT yeu-dh -> redirect to Yeu 3
23	--- entry 2 ---
24	ROOT Yeug -> redirect to Yeu 1
25	--- entry 3 ---
26	ROOT yeug -> redirect to Yeu 3
27	--- entry 4 ---
28	ROOT Yewo -> redirect to leuo
29	
```


## [2026-10-17T00:30:21.388Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-566.json"
}
```


### [2026-10-17T00:30:21.411Z] TOOL RESULT

```
1	{
2	  "pdf_page": 566,
3	  "book_page": 536,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Yeu 3",
8	        "lang": "Indo-European",
9	        "refs": "POK:507",
10	        "gloss": "to mix, blend"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Sanskrit",
17	          "refs": "POK:507",
18	          "words": [
19	            {"translit": "yuš", "gloss": "juice, broth made by boiling in water", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Persian",
28	          "refs": "BQT:600; MON:1254",
29	          "words": [
30	            {"translit": "jŭšîdan", "gloss": "to boil", "script": "جوشیدن"}
31	          ],
32	          "script_extra": "جوش ، جوشش",
33	          "note": null,
34	          "quote": null
35	        },
36	        {
37	          "id": 3,
38	          "parent": 0,
39	          "lang": "Avestan",
40	          "refs": "SOD:117",
41	          "words": [
42	            {"translit": "yaěš", "gloss": "to boil", "script": null}
43	          ],
44	          "note": null,
45	          "quote": null
46	        },
47	        {
48	          "id": 4,
49	          "parent": 3,
50	          "lang": "Sogdian",
51	          "refs": "SOD:117",
52	          "words": [
53	            {"translit": "byěš", "gloss": "to boil", "script": null}
54	          ],
55	          "note": null,
56	          "quote": null
57	        },
58	        {
59	          "id": 5,
60	          "parent": 0,
61	          "lang": "Greek",
62	          "refs": "AHD",
63	          "words": [
64	            {"translit": "zumě", "gloss": "leaven", "script": null},
65	            {"translit": "en-zumě", "gloss": "leavened", "script": null}
66	          ],
67	          "note": null,
68	          "quote": null
69	        },
70	        {
71	          "id": 6,
72	          "parent": 5,
73	          "lang": "French",
74	          "refs": null,
75	          "words": [
76	            {"translit": "ensyme", "gloss": "enzyme", "script": null}
77	          ],
78	          "note": null,
79	          "quote": null
80	        },
81	        {
82	          "id": 7,
83	          "parent": 6,
84	          "lang": "Persian",
85	          "refs": "AMD:57",
86	          "words": [
87	            {"translit": "ânzîm", "gloss": "enzyme", "script": "آنزیم"}
88	          ],
89	          "note": null,
90	          "quote": null
91	        },
92	        {
93	          "id": 8,
94	          "parent": 5,
95	          "lang": "English",
96	          "refs": null,
97	          "words": [
98	            {"translit": "enzyme", "gloss": null, "script": null}
99	          ],
100	          "note": null,
101	          "quote": null
102	        },
103	        {
104	          "id": 9,
105	          "parent": 0,
106	          "lang": "Latin",
107	          "refs": "AHD",
108	          "words": [
109	            {"translit": "jŭs", "gloss": "juice", "script": null}
110	          ],
111	          "note": null,
112	          "quote": null
113	        },
114	        {
115	          "id": 10,
116	          "parent": 9,
117	          "lang": "English",
118	          "refs": null,
119	          "words": [
120	            {"translit": "juice", "gloss": null, "script": null}
121	          ],
122	          "note": null,
123	          "quote": null
124	        },
125	        {
126	          "id": 11,
127	          "parent": 0,
128	          "lang": "Indo-European",
129	          "refs": "KLN:833; POK:512",
130	          "words": [
131	            {"translit": "yeu-dh", "gloss": "shaken, active, fight", "script": null},
132	            {"translit": "yeug", "gloss": "ready to fight", "script": null}
133	          ],
134	          "note": null,
135	          "quote": null
136	        },
137	        {
138	          "id": 12,
139	          "parent": 11,
140	          "lang": "Avestan",
141	          "refs": "KLN:833; POK:512; IEC:446",
142	          "words": [
143	            {"translit": "yaod, yaošti", "gloss": "active, searching", "script": null},
144	            {"translit": "yaoz, yaozaiti", "gloss": "search, fight", "script": null}
145	          ],
146	          "note": null,
147	          "quote": null
148	        },
149	        {
150	          "id": 13,
151	          "parent": 12,
152	          "lang": "Pahlavi",
153	          "refs": "BQT:571",
154	          "words": [
155	            {"translit": "jôyšn", "gloss": "search", "script": null}
156	          ],
157	          "note": null,
158	          "quote": null
159	        },
160	        {
161	          "id": 14,
162	          "parent": 13,
163	          "lang": "Persian",
164	          "refs": "BQT:571; FFD:47",
165	          "words": [
166	            {"translit": "jostan", "gloss": "search", "script": "جُستن"}
167	          ],
168	          "script_extra": "( جوییدن )\nجو ۲ ، جوی ۲ ( دانشجوی )",
169	          "note": null,
170	          "quote": null
171	        },
172	        {
173	          "id": 15,
174	          "parent": 12,
175	          "lang": "Persian",
176	          "refs": "BQT:2457; MON:5272",
177	          "words": [
178	            {"translit": "yŭz", "gloss": "hunting dog, fighting", "script": "یوز"},
179	            {"translit": "yŭzpalang", "gloss": "a small fast leopard", "script": "یوزپلنگ", "see": ["Pard"]},
180	            {"translit": "yŭzîdan", "gloss": "to be active, to search", "script": "یوزیدن"}
181	          ],
182	          "script_extra": "یوزه ، یوزک",
183	          "note": null,
184	          "quote": {"text": "زبهر طلایه یکی کینه توز - فرستاد بالشکری رزم یوز", "poet": "Ferdowsî"}
185	        },
186	        {
187	          "id": 16,
188	          "parent": 12,
189	          "lang": "Sogdian",
190	          "refs": "SOD:15",
191	          "words": [
192	            {"translit": "â-ywdy", "gloss": "to struggle, try", "script": null}
193	          ],
194	          "note": null,
195	          "quote": null
196	        }
197	      ]
198	    },
199	    {
200	      "root": {"name": "yeu-dh", "redirect": "Yeu 3"},
201	      "nodes": []
202	    },
203	    {
204	      "root": {"name": "Yeug", "redirect": "Yeu 1"},
205	      "nodes": []
206	    },
207	    {
208	      "root": {"name": "yeug", "redirect": "Yeu 3"},
209	      "nodes": []
210	    },
211	    {
212	      "root": {"name": "Yewo", "redirect": "Ieuo"},
213	      "nodes": []
214	    }
215	  ]
216	}
217	
```


## [2026-10-17T00:30:25.911Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; command ls sources/refs | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','BQT','MON','SOD','AHD','KLN','IEC','FFD','AMD','WLD','BRT','PHD','NYB','HRN','HUB','CHEUNG','ARY','SKT','KNT','SYN']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-17T00:30:26.565Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
AMD {"title": "Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf", "lookup_hint": "Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable."
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
```


## [2026-10-17T00:30:30.983Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,200p tools/verify_check.py | head -150; python3 -c \"\nimport json;d=json.load(open('data/verification/page-558.json'))\ne=d['entries'][0]; n=e['nodes'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]); print(json.dumps(n,ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-17T00:30:31.407Z] TOOL RESULT

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
{
 "entry": 0,
 "root": "Xac 1",
 "verdict": "plausible",
 "modern_form": "Skt. khac- 'shine through' (?) (Buck, after Uhlenbeck); modern view: Skt. kāca- probably a Nuristani loan, cognate with Skt. kāś- 'to shine'",
 "note": "The book files this chart under X because Nourai writes Skt. kh as X ('Xac' = Skt. khac-). The root and gloss come straight from Buck SYN 620, who gives it with a question mark: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' Wiktionary (after Mayrhofer) calls kāca- 'likely borrowed from a Nuristani language (*kāt's'a), cognate with Sanskrit kāś- to shine brightly'. Either way, a 'shining' root sits behind the glass word, so the chart is defensible, but the specific root khac- is uncertain. The extraction matches the printed page.",
 "note_fa": "نورایی ریشه را سنسکریت khac- «از درون درخشیدن» می‌گیرد (او kh سنسکریت را X می‌نویسد، از همین رو این مدخل زیر حرف X آمده). این ریشه را باک (SYN ص ۶۲۰) به پیروی از اولنبک، و خودش با علامت پرسش، آورده است. ویکی‌واژه به نقل از مایرهوفر سنسکریت kāca- «شیشه» را احتمالاً وام‌واژه‌ای از زبان‌های نورستانی (*kāt's'a) و هم‌ریشه با kāś- «درخشیدن» می‌داند. پس پیوند «شیشه» با ریشه‌ای به معنای درخشیدن پذیرفتنی است، اما خودِ ریشهٔ khac- قطعی نیست و ادعای نورایی را باید با احتیاط پذیرفت.",
 "sources": [
  "https://en.wiktionary.org/wiki/काच"
 ],
 "ref_check": [
  {
   "ref": "SYN:620",
   "status": "supports",
   "note": "SYN.txt (printed p. 620, section 9.74 GLASS), para 7: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' This is exactly Nourai's root and gloss, including Buck's hesitation."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "POK_full.txt grep 'kāca|kāś-|kāçat'",
   "stance": "silent",
   "note": "no Pokorny entry for Skt. kāca- or kāś-."
  },
  {
   "src": "WLD",
   "where": "WLD_Bd1/Bd2_pages.txt, WLD_band3.txt grep 'kāca'",
   "stance": "silent",
   "note": "no hit."
  },
  {
   "src": "AHD",
   "where": "AHD_watkins1985.txt",
   "stance": "silent",
   "note": "no IE root for Skt. kāca- (an Indo-Aryan word with no European cognates)."
  }
 ]
}
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


## [2026-10-17T00:30:55.953Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nfor k in ['POK','SOD','KLN','IEC','BQT','CHEUNG','WLD','AHD']:\n  v=d.get(k) or {}\n  print(k, v.get('page_offset'), '|', (v.get('lookup_hint') or '')[:600]); print()\n\"; grep -n -i 'i̯eu-\\|ieu-' POK_full.txt | head -40"
}
```


### [2026-10-17T00:30:56.245Z] TOOL RESULT

```
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config

SOD printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/Sog

KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh

CHEUNG None | 

WLD Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.

AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 

16874:^/-extension: deieu-{. dieu-, diu-, diu-) 'bright, divine revered sky and bright day: 
41583:Root / lemma: ieu-2, ieu9- ieu-g- 
51535:Note: extension RIeu-d-, Latvian also Rlou-k-. 
57857:mlh, mehlah-k-. mla-k-, mieu-. mlu-\ "to grind, hit; fine, ground'. 
58825:, mehlah-k- : mla-k-, mieu- : mlu- 
80563:Root / lemma: (s)p(h)ieu- : (s)pju-, (s)pTu- {*ps(hlieu- < -g"'hieu -)
```


## [2026-10-17T00:30:58.276Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'Root / lemma: ie' POK_full.txt | head -30"
}
```


### [2026-10-17T00:30:58.606Z] TOOL RESULT

```
40726:Root / lemma: ielo- jslo- 
40768:Root / lemma: ie-ro- 
41583:Root / lemma: ieu-2, ieu9- ieu-g-
```


## [2026-10-17T00:31:03.009Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'Page(s): 50[5-9]\\|Page(s): 51[0-3]' POK_full.txt; sed -n 41480,41760p POK_full.txt"
}
```


### [2026-10-17T00:31:03.394Z] TOOL RESULT

```
40778:Page(s): 506 
41218:Page(s): 505 
41277:Page(s): 505-506 
41338:Page(s): 506 
41388:Page(s): 506-507 
41473:Page(s): 511-512 
41581:Page(s): 507 
41750:Page(s): 508-510 
41826:Page(s): 510-511 
41843:Page(s): 511 
42720:Page(s): 513-514 
Material: 

Note: 

labialized laryngeal hre- > 0e-, ha^o- > hu-, h2"a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 
Avestan yaozaitT be moved, be excited, sprunt up (from the water, from restless lands) ', 
yaosti- " activity, wakefulness, agility, liveliness '; 

Armenian yuzem^ enrage' is Iran, loanword; 

Tocharian A yok-, A B yuk- "defeat, conquer'. 

Note: 

Reduplicated labialized laryngeal in h2"ah3"o- > Avestan yao- > Armenian yu-, Tocharian A 
yo-, B yu- 

Gothic y/i//ra "rage, fury, fight', y/i//ra/7 "fight'. Middle High German Jouchen, Jouchen 
"drive, push, hunt, chase' and Old English geocorluW of hardship', geocre My . "stern'; 

Note: 

Reduplicated labialized laryngeal in hreha^o- > Germanic (*yiu-) jiu-, jeo- > Old English 
jeo- > geo- 

References: WP. I 203, Feist 301 b. 
Page(s):512 

Root / \eT(\T(\a\jeu-1 

Meaning: to mix (of meal preparation) 

Note: {■.Jeu-,Jd[u]-,Ju-,Ju-\ latter due to the lengthened grade or from a heavy basis *ieua- 

), originally probably " set in motion '; s.^e^z-d^-. 

Material: 

Note: 

labialized laryngeal hre- > 0e-, ha^o- > hu-, h2"a- > ha- Hittite 



labialized laryngeal PIE h™- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 
Old Indie yauti, yuvati^ mixed ', ud-a-yauti^ agitates, stirs up ', pra-yauti^ stirs, mixes ', 
yutf-i. " mixture ', a-yavana-v\. " mixing spoon '; 

Lithuanian ya^/7^,yc»i//aZ/, Jauti^ pour hot water about ', Latvian ya^/" stir in, mix dough ', 
yai/s" mixture of cattle feed ', Lithuanian yioi/a/as" pig's food; waste, pigswill, grape marc'; 

Note: 

Reduplicated laryngeal in h2™ah3"o- > Old Indie yau- > Baltic jau- = h3"oh3"o- > Baltic jou- 

gr. ^OGoc;, ^uGoc; ' Egyptian barley beer '??; (lllyrian substrate g- > z-) 
Note: 
labialized laryngeal ha^o- > Proto Greek jou- > gou- > Greek zu- 

alb.-Tosc gjar^soup' {*Jd-no-), Geg gjane^svnuX, pond, pool, watering-place '; 

Note: 

labialized laryngeal h2"a- > Proto Albanian ja- > Albanian gja- 

Maybe alb. {*Jesla) gjella^ soup, dish ' (common Celtic lllyrian -si- > -II-) 

ablauteud gallorom. /utta^rom gall. *Ju-ta, Middle Latin /c»//a "broth', mcymr. /wt, ncymr. 
uwd, iwdrc\., acorn, abret. iot, nbret. ioud, /bo' 'porridge, mash'; Old Irish /'//? "porridge, 
mash, broth' /"probably is attributed to ///7"fat' (Thurneysen Gr. 39). 

Note: 

Reduplicated labialized laryngeal ha^ohs^o- > Celtic iou- 

s-s\.exx\jd(u)s-,jOs- " broth': 

Old Indie yi75 (only Nom.), yusa-, yusa-m. n. "broth', Latin /us, /z/r/s "broth, soup', 
Lithuanian yi/5e {*jus//a) " bad soup from sour dough mixed with water thoroughly ', Old 
Prussian yZ/5e "broth, meat broth'. Old Church S\ay\c juch a {* Jou sa) "broth, soup' (Modern 
High German Jaucheirom West Slavic); in addition to- derivative of New Swedish ost 



{*Justo), Old Norse c»s//'(secondary o) "cheese' and Finnish-Proto Horse Juusto, New 
Swedish dial, ustds.; 

Note: 

Reduplicated labialized laryngeal ha^oha^o- > Germanic juu- 

perhaps in addition gr. ^upn " sourdough' {*iusmaoxjuma) and ljji\x6c, "broth, soup' 
{*id[u]smos or *J^u\mos). 

References: WP. I 199, WH. I 734, Trautmann 110. 
Page(s): 507 

Root / lemma: ieu-2, ieu9- ieu-g- 

Meaning: to tie together, yoke 

Note: probably as ^.Jeu- " mix' evolved from " set in motion '; s. also^e^z-d^-and jeu-ni- 

Material: 

Note: 

labialized laryngeal hre- > 0e-, ha^o- > hu-, h2™a- > ha- Hittite 

labialized laryngeal PIE h™- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g'^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 
Old \n6\c yaut/, yuvat/"ban6s, joins together, harnesses, places a harness on a draft 
animal ' (also " mixed '), participle yuta-, yutf-i. "connection' (and " mixture '), ni-yut-i. 
"row, yoke, pair of harnessed oxen ', yutha-m. " association, troop, multitude, crowd', 
yotra-u. "rope, band', yuna- n. 'band, strap, cord', avayava-m. "limb, member, part'; 
Avestan yav- "occupy oneself with sth. ' (present yavayeiti, Inf. yuto, yuta), yaona-n. 
"occupation ', yav- (yu-) Adj. " holding, standing by somebody ' = Old Indie yu- " 
journeyman, fellow ' (see Bartholomae Airan. Wb. 1264 f., where also about yav- 
"duration'); 
Note: 
labialized laryngeal h2"a- > ya- Old Indie = hs^o- > yo- 

Latvian PI. yiJ/zs "joint (*connection), crossroads ', Lithuanian yai///5m. "ox' ("*strained 
before wagon, a beast used for drawing or carrying, draught-cattle ' = Lat\n Jumentunr, 
Baltic heavy root); here also Latvian yi//77/s " Doppelfrucht, Felddamon \jumt^ {roof) cover' 



(Muhlenbach-Endzelin II 177ff.). doubtably Armenian ya^o^'connection' because of 
vocalism (Iran, loanword?). 

Perhaps here Lat\njuvare' support, help; delight'; probably compatible with Old Indie 
yu-yo-t/" cuts off, protects from, separates, severs, defends, keeps away, it is separated ', 
vf-yavanta^ tending to repel, driving away ' merge to a particular family. 

Note: 

Reduplicated initial laryngeal in h3"oh2"a- > Lat\n juva- = ha^oha^o- > yu-yo- 

with as ^-derivative also Old English (*jeoc) geoc'\r\e\p, consolation, certainty ', geocian 
"preserve, protect, rescue'; see be\o\Njeu~4. (common Occidental Romance]- > g- ) 

Specht (KZ. 65, 207 f., 68, 52 ff.) places y^i/are to Old Indie avat/, whereat above S. 77; 
against it M. Leumann Gl. 29, 173 f. 

Ju-go-m " yoke ': 

Old Indie y^^a-n. "yoke; pair' (also "gender, sex, generation') = 

gr. ^uyov "yoke ' = 
Note: 
labialized laryngeal hreu- > Proto Greek yeu- > geu- > Greek zu- 

\-3X\T\ jugum 6s. (see also WH. I 728 f. about Umbrian Iguvium) = 

Gothic asachs.yi//rn.. Old English geoc, Old Norse ok' yoke ', Old High German yZ/c/?, 
joch yoke; also so much land when one can plow with an ox's pair during one day '; 

Lithuanian (with na^erjung/ujjungas' yoke '; 

Old Church Slavic /^o(Gen. /ga) " yoke ' (es-stem), Czech y/7c» ds. (Slavic Jbgo^rom 
*jbgo, see also Berneker421 f.; in addition Old Russian obbza' a land size; so much that 
a man plows with a horse ' from *ob-JbgJa, nowadays obzaan6 obga-d. j. *ob-Jbga- " 
beichselarme des Hakenpflugs '; Church Slavic PI. /zesa, sloven. Gen. /zesawith results 
of Indo Germanic stem *Jeugos-, see below); 

cymr. iaui., acymr. iou, acorn, ieu, bret. ieo, geo' yoke ', kazelye, kazelge' bondage, 
slavery ' = mcymr. kesseyl-yeu ' axxWaxy yoke' (Loth RC 40, 153 f.); gall. PN Ver-iugo- 



dumnus, see also Pedersen KG. I 98; Thurneysen lA. 26, 26 doubts the affiliation of Irish 
and proto relationship of brit. words; doubtful is also the assessment from Irish cuing^ 
yoke '; after Hessen ZceltPh. 9, 39 maybe from *uing {*iungis) through influence of the 
preposition com-, furthermore mcymr. kyn-iwng^ associa tion ' (Loth RC 38, 160); 

Armenian luc " yoke ' created not originally for aniaut //- root; influence of lucanem " 
unhitch, unharness'; (common Celtic Armenian j- > I- see acymr. Jud-gual, abret. lud-uuar 
tremendous fight ') 

Hittite i-u-ga-an {yugan) " yoke '; 
Note: 
labialized laryngeal ha^ou- > hyu- > iu- Hittite 

Tocharian f\ yokami. "door, gate' (Old Indie loanword?). 

without historical connection between them are Old \n6\c yuga/a-n. "pair', Lat\n jugu/um 
(Demin.) " cheekbone, collarbone', y^^^/ae" the three stars which form Orion's belt; also, 
the whole constellation ' 

Maybe alb. S\av\cjugu' south, southern night sky' 

Gr. ^£uyAr| " loop attached to the yoke, through which the beasts' heads were put, cross- 
bar of the double rudder '; with Hittite yugas "annual', dayugas " biennial ' compare 
Lithuanian dveigys^ biennial ' {treigys^ triennial ', etc.), above S. 229, 230. 

jeu-gos- es-stem: 

Maybe alb. Geg zgjedhe,-a^ yoke ', gjedhe^ (harnessed) oxen ', zgidh, zgjidh, Tosc zglidh 
" untie ', Geg zgjedh^ select' (common alb. -g > -dh). 

gr. TO ^Euyoq " yoke, pair of harnessed oxen ', PI. ^Euysa = LaWn Jugera {*/ougesa), 
wherefore a new Sg. jugerum " an acre, or rather measurement of land, measuring 28,800 
square feet, or 240 feet in length by 120 in breadth ' = Middle High German y/^c/7n. " 
measurement of land ', compare also above Church Slavic izesa, further perhaps (that 
certainly late) al,\)\iv\c, " not joined, unmarried ', as well as Latin iouxmenta, iOmentum {see 
S. 510); zero grade (as a^uYn(;, but from ^uyov could be a neologism from) probably 
Gothic yZ//ra?/f. " yoke, bondage, slavery ', compared with Old English gycer^ yoke ' 
{*Jukizi-), with i/the 2. syllable through assimilation? (common Occidental Romance Old 
English j->g-) 



verb stemjeu-g-: 

Old \n6'\c yunakt/{3. PI. yuhjanti= Lat\njungunt), yunjati^ harnesses, tightens, connects 
', compare full grade yojayati {*jeugeieti) ' joins '; Avestan yaoj-, yuj- ' harness an animal, 
yoke up; accustom '; 

gr. ^£UYvO|ji "harness, bandage ', ^su^ai ^uynvai; 

\-a!m jungo, -ere, -nxi, -nctus^ connect'; 

full grade Old High German untar-jauhta " subjugavi '; 

Lithuanian y^/7^/^,y^/7^//" connect, tighten in the yoke '; participle Old \n6'\c yukta-, 
Avestan yuxta-, with pras. -n- Lat\n Junctus, Old English geoht, iuktu. " yoke ', Lithuanian 
Jungtas, with the (as in present deriving from ^su^ai, ^suKirip etc.) lengthened grade 
^£ukt6(;; 

root nouns jug-\n\ 



Old Indie yJy-' Gefahrte, Genosse; geschirrt, bespannt mit ', ayuj-' without comrades, 
not in pairs ' = gr. a^u^ "unyoked, unpaired, unmarried, isolated ', au^u^ "of a wedded pair, 
united ', Latin conjux^ husband, wife'; Superl. *iugistos\v\ Latin y^A-Za "of several objects, 
near together, in close proximity, near at hand, near, near by, hard by, close to, by the side 
of, next to, immediately after, beside, on a par with ' {*Jugista, soil. K/a" via, byway of, by 
means of); in the strong Kas. analogical Old \v\6\c yunj-, Latin conjunx. 

Additional derivatives in: 

Old Indie yoga- m. " harnessing, connection '; yogya-m. " draft animal ', compare Old 
Norse eykr^ draft animal, horse' (Germanic *jaukiz, compare also Kaus. *jaukian' harness 
' assumed through Old Norse eykt\. " working hours between the meals ' from *jaukiPd) = 
Latin y^^/s "perpetual; bestandig flowing ' (besides /uges, -e//s"angespannt'); Old Indie 
yojana-n. " a road measure ', Avestan yujasti-i. ds.; Old Indie yukti-i. " harnessing ', gr. 
^sO^k; " harnessing, bandage', LaWu Juncti-m, juncti-o, compare of es^stem Avestan 
yaoAs//- "ability, capacity, skill, adroitness '; Old Indie yo/r/a/'-"harnesser', yoktra-n. "rope, 
belt', Avestan yaoxddra-n. " warlike strain, undertaking, attack', gr. ^£UKTf|p£(; "yoke 
straps', LaWn junctor, Junctura, Old Indie y^^/77a/7-" paired, coupled', gr. ^suyMa " that which 
is used for joining, a band, bond, yoke, a bridge of boats ', LaWn jug{u)mentum ^ jamb, 
crossbar, crossbeam', due to es-stem in addition Old Latin iouxmenta. Classical iOmentum 
" yoke, pair of harnessed oxen '. 



Perhaps \N\Vnjeu- are also related the families jeu{e)s- ' statute ' as " obligation, 
commitment, liability, bond' and Jos- " gird ' as *id[u]s-. 

References: WP. I 201 f., WH. I 261, 726 ff., Trautmann 109 f., Kuiper Nasalpras. 70 ff., 
109, Renou BSL. 41, 18ff. 
Page(s): 508-510 

Root / \eTnma\Jeu-3 
Meaning: young 
Material: 

Note: 

labialized laryngeal hre- > 0e-, ha^o- > hu-, h2"a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 01- West Germanic = y-, j- Old Indie = j- East
```


## [2026-10-17T00:31:06.642Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 41388,41480p POK_full.txt"
}
```


### [2026-10-17T00:31:06.969Z] TOOL RESULT

```
Page(s): 506-507 

Root / \eTnma\Jeu-&^- 
Meaning: to move swiftly, to fight 
Material: 

Note: 

labialized laryngeal hre- > 0e-, ha^o- > hu-, h2™a- > ha- Hittite 

labialized laryngeal PIE h™- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 

Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g'^- 

Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 

Old Indie ud-yodhati^ boils up (from the water); make someone angry ', Kaus. yodhayati^ 

involves in fight ', yudhyati, ydo'/?^// "fights', yudh-m. " combatant ', f. "fight, struggle, 

battle', yudhma-h^ warlike ', m. " combatant ', yodh/yas-' more pugnacious, combative, 

better fighting '; Pali yJ/?^// "fights'; 

Note: 

labialized laryngeal h3"o- > yo-, yu- Old Indie = h3"o- > yui- Avestan = hs^o- > yu- 

Tocharian 

Avestan yuidyeinti^ si^<ampfen ', yuidista- " he fights best of all '; 

Tocharian A yutk- "worry about'. 
Note: 
Reduplicated laryngeal in hs^ohre- > Avestan (*you-ei-) yui- 



changing through ablaut Lithuanian ya^o'af. "enticement, seduction ', \N\\ereoi jaudintr 
wake somebody's passion , entice somebody ', refl. " be agitated, get excited ', Latvian 
yaJo'a 'fortune, power \jaudaV have the necessary strength '; 

Note: 

Reduplicated laryngeal in h2"ah3"o- > Baltic (*ya-ou-) yau- 

Lat\njubed, -ere' order, give an order, bid, tell, command ' (= Lithuanian yi/o'e//),yi/ss/" 
(alt. /ouslj, Jussum actuaWy '* set in movement, rouse ', hence; y^it'af. "the flowing hair on 
the neck of an animal, the mane' ("*the shuddering, flowing ones ') ; {about Jubar, -aris' 
the radiance of the heavenly bodies, light, splendor, brightness, sunshine ' see WH. I 724); 

acymr. acorn, abret. y^^/- "fight, struggle' {*Jou6!"o-), " combatant ' {*iou(i!"Jos), in MN as 
acymr. Jud-gual, abret. lud-uuar tremendous fight '; this Jud-{= iud^ became later in 
aniaut polysyllabic names of mcymr. to ld-{= Id-), in all other positions to ud{= ud), so 
acymr. Mor-iud' sea fighter ' to mcymr. Mor-ud, independent cymr. ^o'o' "master, mister' 
{*jOLKi!^Jos); 



i 



Lithuanian y^/o'^, -et/'be shaking, trembling, move, quarrel, squabb\e' , Jundu Just/ 

r ~ 

zitternde Bewegung, in Aufruhr geraten ', Old Lithuanian yi/o'i/s "quarrelsome', yi/o'/'a 

"whirlwind'; 

po\n.Judz/c' stir, tease, irritate, incite, argue about something bad ' (: Old Indie 
yodhayati); perhaps Old Church Slavic ojbmin-b, PI. oyi>/77/ "warrior' (= Old \n6\c yudhma-h 
with prefix o-); (common Occidental Romance = Slavic prefix) 

also Bulgarian yZ/o'a" nymph '; 

Note: 

labialized laryngeal hre- > yei-, yi- Avestan, h2"a- > ya- Old Indie 

gr. hom. uapTvi Dat., uaplvr) " fight, battle, combat' {*/u6'^-s-m/h-, derivative from a Jud'^- 
s-mo-s, compare Old Indie y^o'/7/775-/7); (lllyrian substrate abbreviation) 

References: WP. I 203 f., WH. I 724 f., Trautmann 109. 
Page(s): 511-512 

Root / \evcvrc\a\jeug- 
Meaning: to wave, unsteady 



Material:
```


## [2026-10-17T00:31:11.978Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'jōš\\|još\\|jos\\b\\|ǰōš\\|ǰuš\\|jush\\|yau̯š\\|yausˇ\\|yauš' CHEUNG.txt | head -30; echo ----; grep -n -i 'yau̯d\\|yaud\\|ǰust\\|ǰōy\\|just-\\|jōy\\|yau̯z\\|yauz\\|yōz\\|yoz' CHEUNG.txt | head -40"
}
```


### [2026-10-17T00:31:12.319Z] TOOL RESULT

```
14181:*NWIR: NP josidan/jos- (denomin.) ‘to boil [intr.]; to bubble’, jos ‘boiling’, Bal. 
16620:‘to seethe’, NP jos ‘boiling’, etc. go back to the redupl. formation of *iah ‘to boil, 
30564:*SANSKRIT: jos ‘to like, be pleased, to enjoy’ (RV+) = EWAia I: 599 
31272:Gippert 1993: Jos Gippert, Iranica, Armeno-Iberica. Studien zu den iranischen 
32039:Rekonstruktion: Robert Beekes, Alexander Lubotsky & Jos Weitenberg (eds.), 
41113:jos, 250 
41114:josidan/jos-, 210 
51612:Jos, 473 
----
7200:yaz-/yext-, Sangl. yuz-/yuzd, Ishk. yoz-/yozd, M. yaz-, Yi. yaz- ‘to run’, ? Oss. I. 
11825:(y)uz-, Ard. viyoste/viyoz-, Fariz. -juz-, Gz. yuz-/yus(s)-, Nn. yusse/yuz-, Tr. vósta/ 
11826:vöz-, Varz. ose/oz-, Yar. -just-/-juz- ‘to find’, Qohr. vüsta/vüz- ‘to find, obtain’, 
14628:(+ *a-) Pres.: SUBJ. 3sg. BMP ’ywe’t /ayozad/; Partic.: perf. pass. BMP ’ywht /ayuxt/ || (+ *upa-) Pres.: 
14629:IND. 3р1. BMP ’pyweynd /abyozend/; Partic.: perf. pass. BMP "pywht /abyuxt/ 
14703:*OLD PERSIAN: yaud- ‘to be in commotion’ — Kent: 204a 
14705:Pres. them.: impf. IND. Zeg. ayauda <a-y-u-d> (XPh 31), 3pl. "ayauda" <[a]-[y]-[u]-[d]> ([DSe 33 |); 
14706:Partic.: pres. (Asg. f.) *yauda" tim <y-u-[d]-[t]-[m]> (DNa 32) 
30091:yoz-/yozd-, Zit- ‘to bear [of animals]’ || (+ fra-) Sh. rizin, Khf. rizoen, Rosh. rizén, 
34139:yaud-, 218 
34947:*pywe- /abyoz-/, 217 
35010:"ywc- /ayoz-/, 217 
43551:viyoste/viyoz-, 172 
45149:~just-/-juz-, 172 
48543:yoz-/yozd, 96 
49943:yoZ-/yoZd-, Zit-, 466 
50038:yoz, 117
```


## [2026-10-17T00:31:14.515Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 14160,14200p CHEUNG.txt; echo =====; sed -n 16590,16640p CHEUNG.txt; echo ====; sed -n 14690,14740p CHEUNG.txt"
}
```


### [2026-10-17T00:31:14.816Z] TOOL RESULT

```
Exit code 1

turn’, OE wrencan ‘to wring, turn’, Engl. to wrinkle. (Pokorny: 1145; LIV: 290 f.) 
*REFERENCES: JIFL II: 263a; EVS: 91b; Hoffmann, Aufs. 2: 611, fn. 6; Benzing 1983: 661; Werba 1997: 
236 


)= 


*jah ‘to boil, bubble’ 

*AVESTAN: Y Av. yaés- ‘to boil’ = Liste: 47 
Partic.: pres. redupl. + ja- YAv. yaesiiant- (Y 9.11, F 4, P 20) 
*KHOTANESE: LKh. jis- ‘to boil = SGS: 35 f. 


210 *iaH 


*SOGDIAN: (+ *abi-) BSogd. By’ys’ntk, Bws’nty ‘boiling’ 

*NWIR: NP josidan/jos- (denomin.) ‘to boil [intr.]; to bubble’, jos ‘boiling’, Bal. 
Jus()t/fus-, Nn. yosaye/yos- ‘to boil’, Abyan., Abz. yus, Qohr. yüs, Varz. yos 
‘boiling’ || (+ *ui-) Asht. vis-/visä, Gz. yus-/yusa ‘to seethe’, Asht. visen-/visenä, 
Gz. yusn-/yusnä (caus./tr.) ‘to boil’, Khuns. vis-/visa ‘to boil [intr.], seethe’, Khuns. 
visn-/visna, vus-/vusa (caus.) ‘to boil [tr.]’ 

*NEIR: Pash. yas-, Yghn. es-, es-/éSta, ? Wa. yaks-/yakst- ‘to boil’ ("phonet. 
impossible", IFL П: 1.с.), Pash. уаёпа (Ё) ‘boiling, ebullition, coction’ 

*MISC: Orm. yas-ëk ‘to boil’ (< Pash.) 

*SANSKRIT: yas ‘to boil’ (RV+) = EWAia II: 406 

© The Ir. forms derive from a redupl. pres. stem *1a-13-a- (= Skt. yésa-), cf. EWAia, 
l.c. This redupl. formation has no IE parallels. 

«PIE *Тез- ‘to boil, seethe? = LIV: 312 f. | Pok.: 506 

*IE COGNATES: Gr. Céet ‘bubbles, boils, cooks’, Gr. Ceotdc ‘cooked, boiling, hot’, 
Toch. AB yäs- ‘to boil, to be turned on’, OHG jesan ‘to ferment, to foam’, OE giest, 
(eval):1: ==== not found
```


## [2026-10-17T00:31:21.826Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 14200,14215p CHEUNG.txt; echo =====; sed -n 16605,16630p CHEUNG.txt; echo ====; sed -n 14600,14760p CHEUNG.txt"
}
```


### [2026-10-17T00:31:22.176Z] TOOL RESULT

```
Exit code 1
Toch. AB yäs- ‘to boil, to be turned on’, OHG jesan ‘to ferment, to foam’, OE giest, 


Engl. yeast 

*REFERENCES: EVP: 100; IFL I: 413b; HFL II: 553b; Andreev — PeSéereva: 251a; WIM I: 73; WIM II/1: 
86; DKS: 110b f.; Werba 1997: 395; Steblin-Kamenskij 1999: 420; Lecoq 2002: 133, 588b, 605b, 657b, 
686a; NEVP: 100; Shahbakhsh: s.v. jus- 


*jaH ‘to demand, request’ 

*AVESTAN: yà- ‘to demand’ — Liste: 47 

Pres. {1} inch.: IND. Isg. OAv. yasa (Y 28.1, Y 28.8, Y 49.8, Y 51.21), YAv. yasami (Y 65.11, Yt 5.130 
f.), 3sg. YAv. yasaiti (Y 11.5, Y 65.11), 1р1. ҮАУ. yasamahi (Yt 10.33), INJ. 3sg. OAv. yasat (Y 32.1); 
(eval):1: ==== not found
```


## [2026-10-17T00:31:27.868Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 16605,16630p CHEUNG.txt; echo '----'; sed -n 14610,14760p CHEUNG.txt"
}
```


### [2026-10-17T00:31:28.177Z] TOOL RESULT

```
*REFERENCES: KPF I: 82a f., 145a, 208b; Ivanow 1926: 421; KPF II: 218; Christensen, Contributions II: 


58, 117; Lambton 1938: 42b; MacKenzie 1966: 100; WIM I: 70; WIM II/1: 78; WIM III: 112; Paul 1998: 
304a; Cabolov 2001: 570 f., 26; Lecoq 2002: 128, 130 f., 133, 135 (passim) 


*kaup? ? *to want something strongly? 

*KHOTANESE: ? jüh- (jvih-) ‘to long, yearn’. 0 Emmerick connects the Khot. forms to 
the Pth. verb ywb- ‘to suffer, complaint, lament’ (*raup'), which is semantically not 
evident. According to Bailey DKS: l.c. the Khot. forms rather derive from a root 
*jaus ‘to be agitated, passionate; love’, which is unknown in Ir. and, in addition, 
formally difficult: -h- hardly goes back to *s (the -h- of the pron. uhu ‘you’ has a 
different origin: < *Z, Sims-Williams 1983: 48). The cited cognate forms, Zef. yos 
‘to seethe’, NP jos ‘boiling’, etc. go back to the redupl. formation of *iah ‘to boil, 
bubble’, which is continued by Khot. jis-. Perhaps Khot. juh- goes back to *kufia-, 
which is subsequently contaminated with jis-? © SGS: 36 

*CHORESMIAN: (denomin. ?, with lost neg. *a- ?) kwby- ‘to abstain from (injustice) 
= Samadi: 106 

*NEIR: Oss. I. kuvyn/k,yvd, D. kovun/kuvd ‘to pray’, k,yvd/kuvd ‘prayer; ritual 
feast’, Pash. суар (m.) ‘longing, eagerness, mania, passion’ || (+ *ham-) ? Yi. guv-/ 
guvd, M. guv-/guvd- ‘to burn’ 

----

*AVESTAN: yüj- ‘to harness’ || (+ *apa-) ‘to yoke off, lay down’ || (+ *fra-) ‘to 
harness’ = Liste: 47 

Pres. {1} n- IND. 3р1. *yunjinti (F 252, cf. Kellens 1984: 165f.); Pres. {2} 1а-: IND. 35р. YAv. yujiieiti 
(Yt 10.52); Aor. athem.: INJ. 3sg. OAv. yaogot (Y 44.4), 1р1. med. YAv. fra(-ca) yaoxmaide (Yt 4.1), 
3pl. OAv. yüjan (Y 46.11, Y 49.9), SUBJ. 1sg. OAv. yaoja (Y 50.7), med. 3р1. OAv. yaojante (Y 30.10); 
Partic.: perf. pass. YAv. yuxta- (Y 49.9, Yt 5.50, Yt 9.2), YAv. apaiiüxta- (V 18.30), Y Av. fra.yuxta- (Yt 
10.125); Inf.: YAv. yuxta (Y 11.2) 


*MIDDLE PERSIAN: (+ *à-) BMP ’ywe- /ay6z-/ ‘to join; yoke; drive’ || (+ *upa-) BMP 
"pywc- /abyöz-/ ‘to join, mix’ || (+ *pari-) MMP pyrwz, BMP pylwc /peroz/ *victor- 
ious, victor’. Ф The Persian forms of ‘victory’ were thought to derive from *pari- 
aujah- (YAv. pairi.aojastara- ‘stronger’), cf. AIW: 862; Nyberg II: 160b. However, 
the Parthian cognate forms clearly point to a deverbal origin, e.g. ppp. prywxt. 
=> DMMPP: 290a 

(+ *a-) Pres.: SUBJ. 3sg. BMP ’ywe’t /ayozad/; Partic.: perf. pass. BMP ’ywht /ayuxt/ || (+ *upa-) Pres.: 
IND. 3р1. BMP ’pyweynd /abyozend/; Partic.: perf. pass. BMP "pywht /abyuxt/ 

*PARTHIAN: (+ *pari-) prywx- (pret. stem) ‘to conquer, overcome’, prywg, *prywj 
‘victory’ => Ghilain: 63 | DMMPP: 283a 

Partic.: perf. pass. prywxt; Inf.: prywxt 

*KHOTANESE: (+ *abi-) byumga- ‘bond’ 

*SOGDIAN: CSogd. ywxty (numv. n.) ‘yoke, pair, team’ 

*CHORESMIAN: yxs- (intr./inch.) ‘to be(come) in order; to prepare (oneself)’, ywzy- 
(caus.) ‘to prepare, make ready, carry out = Samadi: 259 

*NWIR: Kurd. (Kurm.) jot (m.), (Sor.) jut ‘pair; plough’, бетп. jua, Sang. jot 
‘plough’ || (+ *pari-) NP piröz ‘victorious’ 

*NEIR: (+ *aua-, *ui-) Sariq. wayewy ‘spine’ || (+ *pati-) ? Sh. pidyüc (m.), (Baj.) 
pedyoc, Sariq. padec ‘thread’ || (+ *fra-) Sh. Grün ‘willow band fastening yoke to 
plough-beam’, Ishk. эги? ‘collar of yoke’, Rosh. rayay ‘willow band fastening yoke 
to plough-beam’, Yi. friyo, М. foriya ‘yoke-rope’ 

*MISC: Georg. (LW) jog- ‘pair, group’ 


218 *jaup ? 


*SANSKRIT: yoj ‘to yoke, to harness’ (RV+) = EWAia П: 417 

© The well-known nominal derivative IE *jug6- ‘yoke’, Skt. yugá-, Hitt. /iuga-/, Gr. 
Cvyó v, Lat. iugum, OHG joh, Engl. yoke, etc. is also attested in Ir.: BMP уже /juy/, 
Pth. ywg, NP jug, Bal. jug, Sh. yuy, Rosh. yuy, etc. 

*PIE *Teug- ‘to yoke’ = LIV: 316 | Pok.: 508 ff. 

*IE COGNATES: Gr. Geóyvuoju ‘I harness, join’, Lat. iungere ‘to harness, to join, to 
build a pile-bridge’, Toch. B yaukk- ‘to employ, serve’, Lith. jüngti ‘to yoke, to 
unite’, Goth. jukuzi (f.) ‘yoke’, ON eykr ‘draught animal’, Engl. to yoke, etc. 
*REFERENCES: JIFL II: 208b; EVS: 95b, 54a, 33b, 71a; DKS: 309a; Werba 1997: 222 f.; Cabolov 2001: 
502 f.; Korn 2005: 104 


*jaup ? ‘to change’ 

*KHOTANESE: (+ *abi- ?) byu(h)- ‘to change; translate” = SGS: 106 

*SOGDIAN: (+ *pati-) CSogd. pcywfs- ‘to be changed, transformed’ 

Pres.: IND. 3sg. CSogd. pcywfsty; Impf.: IND. 3sg. CSogd. pcywps, CSogd. "pcywfs; Fut.: IND. 3sg. 
CSogd. peywfstyq’ 

*SANSKRIT: ? yop ‘to make unrecognizable, confuse’ (MS) = EWAia II: 420 

9 The evidence for this root is limited to Sogdian and Khotanese: the formally 
similar Skt. connection is semantically implausible (*raup?). The root *jaup may be 
a pseudo-root that has developed from *yab/f (A.L.) ? 

*PIE— > LIV: — | Pok.: 

*REFERENCES: Weber 1970: 175; DKS: 310a f.; Sims-Williams 1984: 219b; Gharib: 270b; Werba 1997: 
368 


*iauz ‘to undulate, wave; to be in commotion’ 

*AVESTAN: YAv. yaoz- ‘to set in motion; undulate, wave’ || (+ *a-) ‘to well up’ 
c» Liste: 48 

Pres. them.: IND. 3sg. Y Av. yaozaiti (Y 65.4, Yt 5.4, Yt 8.31, Yt 18.5), 3pl. YAv. yaozonti (Y 65.4, Yt 
5.4, Yt 8.31, Yt 10.36); Partic.: pres. YAv. yaozant- (Yt 5.38, Yt 13.95); Caus.: pres. IND. 3sg. YAv. 
yaozaiieiti (Yt 8.8, Yt 10.111, Yt 14.62) || (+ *4-) Pres. them.: IND. 35р. YAv. 2... yaozaiti (Y 65.4); 
Caus.: pres. IND. 359. YAv. äyaozaiieiti (Yt 8.31) 

*OLD PERSIAN: yaud- ‘to be in commotion’ — Kent: 204a 

Pres. them.: impf. IND. Zeg. ayauda <a-y-u-d> (XPh 31), 3pl. "ayauda" <[a]-[y]-[u]-[d]> ([DSe 33 |); 
Partic.: pres. (Asg. f.) *yauda" tim <y-u-[d]-[t]-[m]> (DNa 32) 

*MIDDLE PERSIAN: BMP ywd- /yöy-/ ‘to blow [of the wind]’ || (+ *2-) BMP ’ywc- ‘to 
trouble, disturb" > DMMPP: 290a 

Pres.: IND. 3sg. BMP ywdty /yoyet/ 

*PARTHIAN: ywz- ‘to agitate, set in motion, convulse; be agitated’ || (+ *a-) "ywz- 
‘to agitate’ — Ghilain: 64 | DMMPP: 375b, 6b 

Pres.: IND. 25р. ywzyy, ywzyh, 3р1. ywzynd; Partic.: perf. pass. ywst || (+ *a-) Pres.: IND. 3pl. "ywzynd; 
Partic.: perf. pass. ’’ywst, ’ywst, ’ywstg 


*laz 219 


*KHOTANESE: (+ *4-) Ayauys- ‘to be disturbed’ || (+ *ni-) nyauys- ‘to be defeated, 
overcome’ = SGS: 9, 61 

*SOGDIAN: (+ *a-) BSogd. "ywz- MSogd. ’yws (intr./pass.) ‘to be troubled’, 
BSogd. "y'wz- (caus.) ‘to trouble, torment’ || (+ *pati-) MSogd. ptyws ‘[+ ’yws] 
become excited’ 

(+ *4-) Pres.: IND. 35р. BSogd. ’’ywzt, ОРТ. 35р. BSogd. ’’ywzy; Pret.: IND. intr./pass. 3sg. BSogd. 
"y'wz't; Partic.: perf. pass. BSogd. ’’y’wst, BSogd. ’’y’wst’k; Inf.: pret. MSogd. *’ywst, Caus.: pres. 
IND. 3sg. BSogd. ”’y’wzt || (+ *pati-) Inf.: pret. MSogd. ptywst. 9 The forms ptywst, *’ywst are originally 
a participle, on which see Henning apud GMS: §929, fn. 

*NWIR: Bal. juzi@/juz- ‘to move, go, walk, leave’ 

*NEIR: Oss. I. uzyn/wyzt, D. ozun/uzt ‘to shake, rock (a baby) to sleep’ || (+ *ni-) 
Pash. niz, nyuz (m.) “flood, torrent’ 

*MISC: Arm. (LW) yuzem ‘I disturb’ 

© The root has no Skt. correspondence. An JE etymology is uncertain. With the 
exclusion of the ‘victory, battle’ forms (Toch. yuk-, etc., v. *iauy’), we are left with 
some rather unattractive Germanic forms: Goth. jiuka ‘rage, tantrum’, MHG jöuchen 
‘to drive, hunt’ (Pokorny: 512; LIV: 315 f.). 

*PIE ? > LIV: 315 f. | Pok.: 512 

*REFERENCES: KPF I: 80a; Nyberg II: 227; WIM I: 73 Ё; WIM II/1: 86; DKS: 20a; Abaev, Slovar’ IV: 
24; Shahbakhsh: s.v. juz-; NEVP: 60 


*jaz ‘to sacrifice, worship, venerate’ 

*AVESTAN: yaz- ‘to sacrifice, worship, venerate’ || (+ *fra-) ‘to sacrifice to’ = Liste: 
46f. 

Pres. them.: IND. med. Isg. YAv. yaze (Yt 8.25), YAv. fraiieze (Y 15.1, Vr 6.1), 350. YAv. yazaiti (V 
18.9), YAv. fra.yazaiti (N 81), med. 1р]. yazamaide (Y 35.1, YH 35.10, YH 36.6, etc.), yazamaidé (YH 
37.1 ff., Y 38.1 ff., Y 39.1, etc.), YAv. yazonti (Yt 8.23 f., Yt 10.54 f., Yt 10.74), med. 3pl. YAv. yazonte
```


## [2026-10-17T00:31:31.644Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'justan\\|jostan\\|juy-\\|joy-\\|jöy\\|jōy\\|‘to seek\\|to look for\\|\\*iaud\\|\\*iauy\\|\\*iaudh' CHEUNG.txt | head -30"
}
```


### [2026-10-17T00:31:32.267Z] TOOL RESULT

```
10959:*AVESTAN: аё$- ‘to desire’ || (+ *upa-) ‘to seek, look for’ || (+ *pari-) ‘to seek, look 
10987:*IE COGNATES: OCS iskati, Lith. (j)iesköti ‘to seek’, OHG eiscön ‘to desire, to 
11824:vis(s)/viz- (inch. ?) ‘to seek; [+ va] ‘to find’, Abyan., Abz. yösta/yüz-, Anar. usse/ 
12108:*NWIR: NP justan/jöy-, Delij. ba-jeuni, Abz. Züva/Züv-, Qohr. jügäda/jüg- ‘to search’ 
13387:preferable though to look for a provenance within (Dlr. rather than to rely on an 
14743:exclusion of the ‘victory, battle’ forms (Toch. yuk-, etc., v. *iauy’), we are left with 
15162:*MIDDLE PERSIAN: MMP jw- ‘to chew’, BMP ywd- /joy-/ ‘to chew; devour (daevic)’ 
15694:*NEIR: (+ *fra-) Oss. D. raegafeen (+ kænun ‘to quarrel; to offend; to look for a fight’) 
16666:indication. Note also Oss. I. ag,yryn/ag,yrd, D. agurun/agurd ‘to seek, demand’ (< 
16756:*CHORESMIAN: kwzy- ‘to ask for, plea, beg’; ? kwcy- ‘to seek, search; ask for’ (with 
16759:*NEIR: (+ *us-) ? M. wuskuj-/wuskujoy- ‘to seek’ (Zarubin) 
17166:*NWIR: ? Gil. (Rsht.) va-moeytoen/va-meej- ‘to seek’ 
22636:Xokor-/Xokord ‘to seek, search for’ (< LW ?, cf. EVS: 102a), Ishk. skarr-/skul ‘to 
22637:seek’, Wa. Skar-/Skard- ‘to mate [of animals]’, Wa. Skur(g)-/Skurd ‘to seek’, Yi. 
26614:‘to seek, look for’ 
26801:*SANSKRIT: ven- ‘to look for’ (RV+) = EWAia II: 582 
29721:9 An ablaut variant of *kauz ‘to seek’ ? 
35779:ywd- /joy-/, 226 
41120:Justan/jöy-, 176 
57004:to look for 
57005:to look for
```


## [2026-10-17T00:31:40.572Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 12070,12140p CHEUNG.txt"
}
```


### [2026-10-17T00:31:40.958Z] TOOL RESULT

```
*SANSKRIT: ya ‘to drive, speed’ (RV+) = EWAia II: 407 

© This root with the meaning ‘to remember’ is solely attested with the preverb *abi-. 
It is probably originally identical to *HiaH ‘to go, drive to’ (Skt. ya, etc.) that has 
acquired a specialized meaning with *abi-: > *‘to come to mind’ > ‘to remember’. 
The peculiar form OAv. “’yamang gen. sg. ‘course’ (Y 48.2) may actually contain 
*HiaH ‘to go, drive to’, on which see, for instance, Insler, Gathas: 286. 

*PIE *HJeH>- ‘to go, drive to’ = LIV: 319 f. | Pok.: 293 ff. 

*IE COGNATES: Toch. A ya- ‘to go, to travel’, Lith. joti ‘to drive, to go’, Latv. jat ‘to 
drive, go’, Lat. iānus (m.) ‘passage, gateway’ 

*REFERENCES: IFL I: 237a f.; DKS: 308a; Adams 1999: 89; Lecoq 2002: 657; Witczak 2005: 282; Korn 
2005: 105, 416 


*Hiaud ‘to fight, struggle (for something), strive, seek’ 

*AVESTAN: YAv. yuo- ‘fight, struggle’ — Liste: 47 

Pres. ia-: IND. 3sg. YAv. yuidiieiti (Y 57.17), 3du. ҮАУ. yüióiia00 (Yt 8.22, Yt 8.26, Yt 8.28), 3pl. ҮАУ. 
yüióiieinti (Yt 13.63, Yt 13.67) 

*PARTHIAN: ywdy- ‘to look after; to strive for’, yws- (inch.) ‘to battle’ — Ghilain: 
65, 87 | DMMPP: 375b 

Pres.: SUBJ. 15р. ywdy’m, 3pl. ywdynd, 258. ywdy’h, IMPV. 2pl. ywdyd; Inch.: pres. IND. 35р. "ywsyd 
*KHOTANESE: juv- (jv-) ‘to fight’ — SGS: 36 

*CHORESMIAN: (+ *abi-) ? m['bywzy- ‘to make angry, anxious, to upset’. 0 Samadi 
cautiously suggests a possible reconstruction *abi-jauj- for Chor. m/’bywzy-, which 
is semantically not compelling, cf. simplex Chor. ywzy- ‘to prepare, make ready, 
carry out’. > Samadi: 2! 

*BACTRIAN: 1@A- ‘to fight” = S-W, Bact.: 196b 

*NWIR: NP justan/jöy-, Delij. ba-jeuni, Abz. Züva/Züv-, Qohr. jügäda/jüg- ‘to search’ 
(< NP) ‘to strive for, seek’, ? Bal. jod ‘man’ (< Urdu ?). 9 Qohr. jugada/jug- 
contains a secondary -g-, which appears to be a hiatus filler, cf. Qohr. pigaz ‘onion’ 
< Pers. piyaz < *pidaz (Horn 1893: 77). 

*NEIR: Oss. I. udyn, D. odun/odt ‘to exert; be industrious; put effort into’ 

*SANSKRIT: yodh ‘to fight’ (RV+) = EWAia II: 418 

«PIE *Hieud"- ‘to fight, to set out, move (to fight)’ > LIV: 225 f. | Pok.: 511 f. 


*Hmai2 177 


*IE COGNATES: OLat. ioube-, Lat. iubere ‘to order, command’, Lith. judéti ‘to move 
[intr.]’, Lith. judus ‘belligerent’, Gr. donivn (Е) ‘battle, fight’ 

*REFERENCES: Horn 1893: 94; KPF I: 136b; DKS: 111b; Safari 1373: 97; Abaev, Slovar’ IV: 11; Werba 
1997: 222 f.; Lecoq 2002: 121, 124; Korn 2005: 104, 368 


DI n s = a 
*Hmai ‘to fix(ate), build, fashion 
*AVESTAN: YAv. mi- ‘to build, fashion’ 
Partic.: perf. pass. YAv. -mita- (Yt 10.28, Yt 10.30) 


«OLD PERSIAN: uz-maya-patiy (+ kr- ‘to do, make’) ‘to support, to prop (up) 
<u-z-m-y-a-p-t-i-y>, ? vahu-misa- PN lit. ‘Good Creator/Builder’, "Med." ? 
<v-u-mi-i-s>, (Asg.) <v-u-mi-i-s-m>.  uz-maya-patiy can be analysed as loc. sg. + 
postp. patiy. || In Elamite a personal name is attested: ЕІ-ОР Ma-u-mi-is-sa = 
vahu-misa-? = Kent: 178a
```


## [2026-10-17T00:31:44.627Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"ywδ\\|'ywd\\|ʾywd\\|\\\"ywd\\|ywdy\" SOD_pages.txt | head; grep -n -i \"y'ys\\|yʾyš\\|ys'ntk\\|boil\" SOD_pages.txt | head -20"
}
```


### [2026-10-17T00:31:45.082Z] TOOL RESULT

```
2179:      chapter of the Vendidad gives the list of countries              swYSfnk (MDiiX sYwSyk (MDiii) and sYwdyWk
4849:                                                                       ayo5y ? ©<*a-yaud; Av. yaod-\ Parth. ywdy
16165:            Yo5e (ywdy) ©<Av. gaoiSL, gaoSana
16215:      4369 Ywdy     C «* Yw5>k(h)                                           GMS 1410 n pi; VJ 1509
16234:      xune, xwane =»ywny, ywn-1, xw'n2                    4397 ywdy     B =± yvsrfy
5362:                                                            569 >py>s- => 'Py'ys-, py'ys-
5364:                                                                boiling
5368:                                                                 (o)pyesanc-   ©f. adj. ^Py'ys'ntk
5381:    (c/)scvcn jewels                                        573 'py'ys- B                                     0-^>r
5384:                                                                   ^Py'^ntcy, Py*ys*ntk, Py'ys-
5386:    apd-ratnene ©Skt. saptaraina                                OcOboil
7387:       (to)cook, (w)boil                                                         SCE 347, -w
10221:                                                                    boiling ?   yaesiya; Yaghn.es; Knot.; is.
10232:                                                               2237 boiling
11130:                                                                2567 PY'ystMn B, S             ji=_jJ *jUjl>- J^ <c~i#
11138:       Payan-xutaw =»pyJn 'xsyy6                                2568 py'yst B                                          jUj^
11245:        P(a)yo5, PoyoS <&^*abi-gauda                                             Payist (byyst) ©ob. pi. -y(y) ^Py'yst, Pyyct
11260:      Payyak (Pyy'q) ©*baga-yakd                                           2615 pyyyst'n M => Py'yst'n
11294:        ^Py'yst'n                                                               p(o)zaxutya (Pz'ywtyO    ^Pj'xwty'h
12171:      GMS 795, 801; AVS 227, 228                                        2960 py'ys-   B                           ox±j>-<tf*«
12172:                                                                              Pyaxs ? ©inf. -}y =^Py'ys-
12173:2945 bwz>xq C                                          1^                     (fo)boil, (to)cook
15252:4050 y'ysrc S               ^Sijj ^oO^j)^^    JaI^^U-
35320:                                                                  10894 y'ys B ^ yks-())
37762:(ro)be roasted  2715                      bit 6567                               (to)boil 573, 1251, 2960, 2970
```


## [2026-10-17T00:31:48.794Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4835,4860p SOD_pages.txt; echo '----'; sed -n 5355,5390p SOD_pages.txt; echo '---'; sed -n 12160,12180p SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"ayo5y\")) print NR-1}' SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"2960 py\")) print NR-1}' SOD_pages.txt;  awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"573 \\x27py\")) print NR-1}' SOD_pages.txt"
}
```


### [2026-10-17T00:31:49.355Z] TOOL RESULT

```
356 Ynp-     B                      jAb^tj<o*J'*->IJ-                GMS 1572; *ycw, MDii; Frag. Lcn.
15                                                                                                               Vntn'my


371 wy8 B                                                          381 ete
                                                                       »ytk ©pp.
                                                                             S
    c5 **»yc, »8c(w)
    something                                                           taken
      TSP 2.954                                                         MDii

372 "yScw S                                         j^j»<j*>?      382 "ytwS'r- =» 'yd'r-
    ecu =>*Sc(w)                                                   383 nyw8y- S                    jj^.^ tjxjL?*^**-
    something
                                                                       ayo5y ? ©<*a-yaud; Av. yaod-\ Parth. ywdy
      MDii                                                             OeOtrouble, (ro)takc pain
                                                                       Sund. MSP p40, b78
373 »yfs- M                           &J* j~~ *oJ±J~&
    ayafs ©impf. rriyfs =>*y*Pt— , »y)|3s-                         384 »ywst- =» »y>wst-
    Oo)be changed, (to)bc perverted
    GMS 827, 653; Hen. Tales. 473.4; AVS 74, 107                   385 »ywst}k => •y'wst'k

374 »yh      B                                                     386 "ywsty S => »y>wst)k
                                                                   387 »ywz B                                       v>i
     ay ©<*ayw         =>*y\ *yl                        j-'-r^
     life, age                                                          ayoz Oywz-) ^'y'wzkr'k, 'ywz(y)
----
    GMS 1331; TSP 3.89, 9.6; Hen. Cosm. 312.108;
                                                            568 'pyVt-      S                        jaL * jijjTc-i-u
      MSP b29, b99; -w, STii 1.18
                                                                 (o)Pyart ©pt. st. ^Py'rt-
556 'btmyq     C =» >Ptmyk                                       (ro)obtain
                                                                 STii p580; Hen. Miltelir. p63; AVS 104
557 ^tr'ync-     B       (0->jjT JJiS)o^J^^^^Jf^
                                                            569 >py>s- => 'Py'ys-, py'ys-
     (o)ptrenc Optrync-) ©<*abi-trnjaya-         ©impf. '
                                                                boiling
                                                            570 'py's'ntcy  B                                   oiij>-
       fiUrync =^ptr»ync-
     (/cOoppress, (fo)suppress, (/cOcontrol
                                                                 (o)pyesanc-   ©f. adj. ^Py'ys'ntk
     TSP 11078, 1100; AVS 123
558 >ptryt- ** ptryt-                                            SCE 235

559 }ptryty B                               (o^)^^          571 »py»tr => »py»tr
    (D)ptrayde ©inf. pp. =*ptryt-                           572 'py'tCw) S                                  c?->JT^<^
     oppresscd                                                  reminding
                                                                aPyat                                          .* .
     TSP 2.133

560 'ptrtn'ynch B                           >jfoiA               Anc. Lett. 4.8; Sund. A green leaf, AI 1988 pl8l,
    apd-ratnenc ©f. adj,
                                                                  byhqhc
    (c/)scvcn jewels                                        573 'py'ys- B                                     0-^>r
    VJ 18\ 345, 1422; GMS 1053; Gcrsh. Sogd. Cpds.
      146.3                                                      (o)Pycs ? 0PyJs-) ©Av. abi-aeh Yaghn. cs
                                                                   ^Py'^ntcy, Py*ys*ntk, Py'ys-
561 •ptrtnyn'k B, S                             ^/o*
    apd-ratnene ©Skt. saptaraina                                OcOboil
                                                                GMS 90; >pfYs 1 TSP 19.6 n p232
    (o/)seven jewels                                        574 »bynt- C
     BSTBL, Dhy. 198; >0t}rtnyn*kwt VJ 861-2; GMS                                                               jr"X$
                                                                 aPont/d =>Jbst-, >bnt(t)
---
     GMS 788, 819; AVS 229                                                   PT
                                                                             both? ©adv. =*wPyw, byw, }wPy
2941 pwwfi      M =» Pw5
                                                                             C2 gloss.
2942 bwwny       C => b'wwny
                                                                        2959 py»tr B                                     j^
2943 pwxs-      M =» pwys-
2944 pwy                                                                      fyatar
                                                                              more ^fy'tr, >Py*tr
      Pawe     ©2&3sg. pres. opt. =»Pw-, wPy(y)2, by1,                        SCE 299; GMS 321

      GMS 795, 801; AVS 227, 228                                        2960 py'ys-   B                           ox±j>-<tf*«
                                                                              Pyaxs ? ©inf. -}y =^Py'ys-
2945 bwz>xq C                                          1^                     (fo)boil, (to)cook
     P^zaxak by?3 =»bz}xwq, 'pyz'ywk^                                         TSP 19.6 n p232
     unfortunate
     Lentz. STii 1.46 n p580; BBB p90 a9                                2961 by'm- C                      o^Jtjjj, id^J'^jji
2946 bwzbr C                                                    e V H
                                                                             Pyam (bym) ©impf. b^m
                                -"'UU ^5 jj I /*-*^- j y* ^ *
                                                                             (/o)rear, (r<?)foster
80
181
87
```


## [2026-10-17T00:31:57.916Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-10-17T00:31:58.405Z] TOOL RESULT

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


## [2026-10-17T00:31:59.936Z] AGENT

Good — I can fetch and archive in one step, then read the stored text.


## [2026-10-17T00:32:03.032Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/جوشیدن' 'https://en.wiktionary.org/wiki/جوش' 'https://en.wiktionary.org/wiki/یوز' 'https://en.wiktionary.org/wiki/جستن' 'https://en.wiktionary.org/wiki/ζύμη' 'https://www.etymonline.com/word/enzyme' 'https://www.etymonline.com/word/juice' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewH-' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewdʰ-' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yes-' 'https://en.wiktionary.org/wiki/یوزپلنگ' 'https://en.wiktionary.org/wiki/آنزیم' 'https://en.wiktionary.org/wiki/यूष'; do python3 tools/fetch_source.py \"$u\" --note \"page 566, root Yeu 3: etymology check\"; done"
}
```


### [2026-10-17T00:32:11.370Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0f0ab8afe554d970.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c3a97d203943c9ed.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d3cc5d47abcfbc4d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f69812821424ee36.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f74b80d0d6b89768.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/eb92ebbd69ec4595.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9a13337725f66280.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fcb188fac26dc863.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fbfe62b138171881.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/00af9c24694c8729.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ad2861b5f26c6a9d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7f8c58e710ff4357.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8a10933b7d8834cb.txt
```


## [2026-10-17T00:32:14.355Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 0f0ab8afe554d970 c3a97d203943c9ed d3cc5d47abcfbc4d f69812821424ee36 ad2861b5f26c6a9d 7f8c58e710ff4357; do echo \"## $f\"; wc -c < $f.txt; grep -n -i -A6 'Etymology' $f.txt | grep -v -i 'edit\\|^--$' | head -24; done"
}
```


### [2026-10-17T00:32:14.890Z] TOOL RESULT

```
## 0f0ab8afe554d970
16942
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
152: Etymology
154-
155- Derived from Classical Persian جوش ( jōš ) . [ 1 ] 
156-
157- Pronunciation
## c3a97d203943c9ed
5832
62: Etymology 
63-
64- 1.2 
65- Numeral 
66-
67- 1.3 
68- References 
76: Etymology 
77-
78- 2.2 
79- Pronunciation 
80-
81- 2.3 
82- Verb 
96: Etymology 
97-
98- 3.2 
99- Pronunciation 
100-
101- 3.3 
102- Noun 
110: Etymology 
111-
112- 4.2 
## d3cc5d47abcfbc4d
23094
62: Etymology 1 
63-
64- 1.1.1 
65- Numeral 
66-
67- 1.1.2 
68- Determiner 
77: Etymology 2 
78-
79- 1.2.1 
80- Noun 
81-
82- 1.2.1.1 
83- Derived terms 
97: Etymology 
98-
99- 2.2 
100- Noun 
101-
102- 2.3 
103- References 
111: Etymology 1 
112-
113- 3.1.1 
## f69812821424ee36
13436
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Verb 
74: Etymology 2 
75-
76- 1.2.1 
77- Pronunciation 
78-
79- 1.2.2 
80- Verb 
164: Etymology 1
166-
167- From Middle Persian [Book Pahlavi needed] ( ystn', yh- /⁠jastan, jah-⁠/ , “ to happen, occur, chance ” ) , [ 1 ] from Proto-Iranian *zgad- ( “ to go on, gallop, mount ” ) . Cognate with Northern Luri جستێ ( cestı ) , Baluchi جہگ ( jihag , “ to flee, escape ” ) , Pashto زغلېدل ( zğaledəl , “ to run ” ) , with no further cognates outside of Iranian.
168-
169- Pronunciation
522: Etymology 2
524-
525- From Proto-Iranian *Hyawd- ( “ to fight, struggle (for something), strive, seek ” ) , from Proto-Indo-Iranian *Hyawdʰ- ( “ to fight, struggle ” ) .
526-
527- Pronunciation
## ad2861b5f26c6a9d
3524
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
151: Etymology
153-
154- From یوز ( yuz , “ cheetah, hunting dog ” ) + پلنگ ( palang , “ panther, leopard ” ) .
155-
156- Pronunciation
227: Persian entries with etymology texts 
228- Pages using etymon with no ID 
229- Pages with entries 
230- Pages with 1 entry 
231-
233-
## 7f8c58e710ff4357
2611
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
141: Etymology
143-
144- Borrowed from French enzyme .
145-
146- Pronunciation
176: Persian entries with etymology texts 
177- Pages using etymon with no ID 
178- Pages with entries 
179- Pages with 1 entry 
180-
182-
```


## [2026-10-17T00:32:19.189Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i 'jōš\\|from\\|boil' c3a97d203943c9ed.txt | head; echo '--yuz'; grep -n -i 'Persian' d3cc5d47abcfbc4d.txt | head; sed -n '/Persian/,$p' d3cc5d47abcfbc4d.txt | grep -n -i 'from\\|cheetah\\|yūz\\|yōz' | head -20; echo '--zume'; grep -n -i 'from\\|PIE\\|leaven' f74b80d0d6b89768.txt | head -15; echo '--enz'; sed -n '/enzyme (n.)/,+12p' eb92ebbd69ec4595.txt | head -20; echo '--juice'; grep -n -i -m5 'juice (n.)' -A6 9a13337725f66280.txt | head -15"
}
```


### [2026-10-17T00:32:19.578Z] TOOL RESULT

```
183: From Wiktionary, the free dictionary
193: Inherited from Sanskrit दश ( daśa ) , from Proto-Indo-Iranian *dáća , from Proto-Indo-European *déḱm̥ .
205: Elena Bashir; Maula Nigah; Rahmat Karim Baig ( 2022 ), “ جوش ”, in A digital Khowar-English dictionary with audio ‎ [1] , second edition, Chicago, IL: South Asia Language and Area Center, University of Chicago , archived from the original on 19 January 2023 . 
213: Ultimately from Proto-Indo-European *yes- ( “ to foam, boil ” ) . [ 1 ] 
237: jōš
241: jōš
254: جوش • ( jōš  / juš ) ( Tajik spelling ҷӯш ) 
256: present stem of جوشیدن ( jōšīdan/jušidan ) 
261: جوش • ( jōš / juš ) ( Tajik spelling ҷӯш ) 
263: boiling of a liquid
--yuz
197: Persian 
199: Toggle Persian subsection 
710: Borrowed from Persian یوز ( yuz , “ cheetah ” ) , from Middle Persian ywc ( yōz ) 
741: Persian
744:   یوز on Persian Wikipedia
750: Iranian Persian
759: From Middle Persian ywc ( yōz ) ; see there for further information.
764: ( Classical Persian ) IPA ( key ) : /ˈjoːz/ 
818: Steingass, Francis Joseph ( 1892 ), “ يوز ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul 
847: Ottoman Turkish terms borrowed from Persian 
87: From Wiktionary, the free dictionary
107: Inherited from Proto-Turkic *yǖŕ ( “ hundred ” ) .
143: Inherited from Proto-Turkic *yǖŕ ( “ face ” ) .
207: From Sanskrit अवश्या ( avaśyā , “ hoarfrost ” ) .
219: Elena Bashir; Maula Nigah; Rahmat Karim Baig ( 2022 ), “ یوز ”, in A digital Khowar-English dictionary with audio ‎ [5] , second edition, Chicago, IL: South Asia Language and Area Center, University of Chicago , archived from the original on 19 January 2023 . 
237: Inherited from Proto-Turkic *yǖŕ ( “ hundred ” ) .
272: Inherited from Proto-Turkic *yǖŕ ( “ face ” ) .
335: Deverbal from یوزمق ( yozmaq , “ to erase, to make wild, to ruin ” ) .
379: Inherited from Old Anatolian Turkish یوز ( yüz ) , from Proto-Turkic *yǖŕ ( “ hundred ” ) .
433: Inherited from Old Anatolian Turkish یوز ( yüz ) , from Proto-Turkic *yǖŕ ( “ face ” ) .
514: Borrowed from Persian یوز ( yuz , “ cheetah ” ) , from Middle Persian ywc ( yōz ) 
524: cheetah , a distinctive member ( Acinonyx jubatus ) of the cat family, slightly smaller than the leopard 
563: From Middle Persian ywc ( yōz ) ; see there for further information.
587: yōz
591: yōz
606: cheetah 
624: Retrieved from " https://en.wiktionary.org/w/index.php?title=یوز&oldid=91033640 "
626: Categories : Chagatai terms inherited from Proto-Turkic 
627: Chagatai terms derived from Proto-Turkic 
633: Khowar terms inherited from Sanskrit 
--zume
183: From Wiktionary, the free dictionary
191: From Proto-Indo-European * yúHs -meh₂ ( “ fermentation, soup ” ) . [ 1 ] 
213: leaven 
214: c.  1st century A.D. , “ 1 Corinthians 5:6-8”, in New Testament : Οὐ καλὸν τὸ καύχημα ὑμῶν. οὐκ οἴδατε ὅτι μικρὰ ζύμη ὅλον τὸ φύραμα ζυμοῖ; ἐκκαθάρατε οὖν τὴν παλαιὰν ζύμην , ἵνα ἦτε νέον φύραμα, καθώς ἐστε ἄζυμοι. καὶ γὰρ τὸ πάσχα ἡμῶν ὑπὲρ ἡμῶν ἐτύθη Χριστός· ὥστε ἑορτάζωμεν μὴ ἐν ζύμῃ παλαιᾷ, μηδὲ ἐν ζύμῃ κακίας καὶ πονηρίας, ἀλλ’ ἐν ἀζύμοις εἰλικρινείας καὶ ἀληθείας. Ou kalòn tò kaúkhēma humôn. ouk oídate hóti mikrà zúmē hólon tò phúrama zumoî? ekkathárate oûn tḕn palaiàn zúmēn , hína ête néon phúrama, kathṓs este ázumoi. kaì gàr tò páskha hēmôn hupèr hēmôn etúthē Khristós; hṓste heortázōmen mḕ en zúmēi palaiāî, mēdè en zúmēi kakías kaì ponērías, all’ en azúmois eilikrineías kaì alētheías. Your boasting is not a good thing. Do you not know that a little yeast leavens all of the dough? Clean out the old yeast so that you may be a new batch of dough, as you really are unleavened. For our paschal lamb, Christ, has been sacrificed. Therefore, let us celebrate the festival, not with the old yeast , the yeast of malice and evil, but with the unleavened bread of sincerity and truth. 
288: ⇒ Greek: ζυμάρι ( zymári ) (from the Medieval diminutive ζυμάριον ( zumárion ) )
317: Woodhouse, S. C. ( 1910 ), English–Greek Dictionary: A Vocabulary of the Attic Language ‎ [2] , London: Routledge & Kegan Paul Limited . leaven idem, page 483.
327: From Ancient Greek ζῡ́μη ( zū́mē , “ leaven ” ) .
388: άζυμος ( ázymos , “ unleavened ” ) 
401: Retrieved from " https://en.wiktionary.org/w/index.php?title=ζύμη&oldid=92956311 "
403: Categories : Ancient Greek terms inherited from Proto-Indo-European 
404: Ancient Greek terms derived from Proto-Indo-European 
414: Greek terms inherited from Ancient Greek 
415: Greek terms derived from Ancient Greek 
--enz
--juice
```


## [2026-10-17T00:32:31.185Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 207,236p c3a97d203943c9ed.txt; wc -c eb92ebbd69ec4595.txt 9a13337725f66280.txt fcb188fac26dc863.txt fbfe62b138171881.txt 00af9c24694c8729.txt 8a10933b7d8834cb.txt; grep -n -i 'enzyme' eb92ebbd69ec4595.txt | head -5; grep -n -i 'juice' 9a13337725f66280.txt | head -5"
}
```


### [2026-10-17T00:32:31.566Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Ultimately from Proto-Indo-European *yes- ( “ to foam, boil ” ) . [ 1 ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈd͡ʒoːʃ/ 

 ( Dari, formal ) IPA ( key ) : [d͡ʒoːʃ] 

 ( Dari, formal ) IPA ( key ) : [d͡ʒoːʃ] 
 ( Kabuli ) IPA ( key ) : [d͡ʒoːʃ] 

 ( Hazaragi ) IPA ( key ) : [d͡ʒʊːʃ] 

 ( Iran, formal ) IPA ( key ) : [d͡ʒuːʃ] 

 ( Tajik, formal ) IPA ( key ) : [d͡ʒɵʃ] 

 Rhymes: -oːʃ 

 Readings

 Classical reading ? 

  133 eb92ebbd69ec4595.txt
  132 9a13337725f66280.txt
  166 fcb188fac26dc863.txt
  168 fbfe62b138171881.txt
 4980 00af9c24694c8729.txt
 8215 8a10933b7d8834cb.txt
13794 total
1:URL: https://www.etymonline.com/word/enzyme
1:URL: https://www.etymonline.com/word/juice
```


## [2026-10-17T00:32:39.839Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; cat fcb188fac26dc863.txt; grep -n -i 'boil\\|yeast\\|ζέω\\|Iranian\\|Persian\\|yásati' 00af9c24694c8729.txt | head -20; grep -n -i 'broth\\|soup\\|from\\|yūṣ' 8a10933b7d8834cb.txt | head"
}
```


### [2026-10-17T00:32:40.431Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewH-
FETCHED: 2026-10-17T00:32:06Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found138: to boil 
148: Proto-Indo-Iranian: *yáyasti 
153: Proto-Iranian: 
154: Avestan: 𐬫𐬀𐬉𐬱𐬌𐬌𐬈𐬌𐬙𐬌 ( yaēšiie i ti , “ to boil ” ) ( with *-ya- added to weak stem [ 1 ] ) 
171: Proto-Indo-Iranian: *yāsáyati 
182: Proto-Germanic: *jestuz ( “ yeast ” ) ( see there for further descendants )
189: Classical Persian: جوش ( jōš , “ boiling ” ) [ 4 ] 
190: ⇒ Classical Persian: جوشیدن ( jōšīdan , “ to boil ” ) 
197: ^ Beekes, Robert S. P. ( 2010 ), “ ζέω ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , pages 499-500 
201: ^ Cheung, Johnny ( 2007 ), “ *i̯ah ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , pages 209-210 
214: Persian terms with redundant transliterations 
142: From Wiktionary, the free dictionary
188: Thematised from यूस् ( yū́s ) , ultimately from Proto-Indo-European *yéwHs ( “ soup, broth ” ) . Cognate with Latin iūs ( “ gravy, broth, sauce ” ) (whence English juice ), Lithuanian jū́šė ( “ fish soup ” ) , Russian уха ( uxa , “ fish soup ” ) , Proto-Germanic *justaz ( “ cheese ” ) .
200: यू॒ष • ( yūṣá ) stem ,  m or n 
202: soup , broth 
204: pea soup , the water in which different pulses have been boiled 
219: यू॒षः ( yūṣáḥ ) 
221: यू॒षौ ( yūṣáu ) 
222: यू॒षा¹ ( yūṣā́¹ ) 
224: यू॒षाः ( yūṣā́ḥ ) 
225: यू॒षासः॑¹ ( yūṣā́saḥ¹ )
```


## [2026-10-17T00:32:55.505Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/𐭩𐭥𐭰' --note 'page 566, Yeu 3: MP yōz cheetah' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewH-_(mix)' --note x; grep -n -i 'Etymology' -A4 /home/sfmqrb/git/rishe-private/data/verification/sources/web/d3cc5d47abcfbc4d.txt | sed -n '1,0p'; sed -n 700,720p data/verification/sources/web/d3cc5d47abcfbc4d.txt"
}
```


### [2026-10-17T00:32:56.779Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dbc6ede511bd076e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6806bdb39cb33ebd.txt
62: Etymology 1 
 Meninski, Franciszek à Mesgnien ( 1680 ), “ یوز ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [15] , Vienna, column 5619 

 Nişanyan, Sevan ( 2002– ), “ yüz1 ”, in Nişanyan Sözlük 

 Redhouse, James W. ( 1890 ), “ یوز ”, in A Turkish and English Lexicon ‎ [16] , Constantinople: A. H. Boyajian, page 2214 

 Etymology 3
 [ edit ] 

 یوز 
 Borrowed from Persian یوز ( yuz , “ cheetah ” ) , from Middle Persian ywc ( yōz ) 

 Noun
 [ edit ] 

 یوز • ( yuz ) ( definite accusative یوزی ( yuzu ) , plural یوزلر ( yuzlar ) ) 

 panther , any mammal of the genus Panthera , which includes big cats such as the leopard , jaguar , tiger , etc.
 Synonyms: بارس ( “ bars ” ) , پلنك ( “ peleng ” ) 

 cheetah , a distinctive member ( Acinonyx jubatus ) of the cat family, slightly smaller than the leopard
```


## [2026-10-17T00:32:59.318Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; head -5 dbc6ede511bd076e.txt; grep -n -i 'from\\|cheetah\\|yōz\\|Iranian' dbc6ede511bd076e.txt | head -15; head -4 6806bdb39cb33ebd.txt; grep -n -i 'Iranian\\|ζύμη\\|iūs\\|mix' 6806bdb39cb33ebd.txt | head -20"
}
```


### [2026-10-17T00:32:59.651Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/𐭩𐭥𐭰
FETCHED: 2026-10-17T00:32:56Z
STATUS: -1
TITLE: 

URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewH-_(mix)
FETCHED: 2026-10-17T00:32:56Z
STATUS: -1
TITLE: 
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewH-_(mix)
```


## [2026-10-17T00:33:05.114Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo HRN; grep -n -i 'jōš\\|jôš\\|jos\\b\\|jöš\\|justan\\|jōstan\\|yūz\\|yuz\\b' HRN.txt | head -20; echo HUB; grep -n -i 'jōš\\|jōy\\|justan\\|yūz\\|jusidan\\|jôs' HUB.txt | head -20"
}
```


## [2026-10-17T00:33:06.683Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo PHD; grep -n -i 'jōy\\|jōš\\|yōz\\|ǰōy\\|ǰōš\\|jōyišn\\|joyišn' PHD.txt PHD_mackenzie.txt | head -20; echo NYB; grep -n -i 'jōy\\|yōz\\|jōš\\|ǰōš\\|ǰōy' NYB_vol2_glossary.txt | head -20"
}
```


### [2026-10-17T00:33:07.065Z] TOOL RESULT

```
HRN
15826:döpaiiitan JOS.
17102:miyJiiiauH -JOS.
21506:s. Jos< 567.
HUB
1387:np. justan, vgl. phi. vijustan WZKM. 8, 92) freilich
5288:trennt', zd. yuta-; Justan *suchen' von einer Wzl. "^i/udh?;
```


### [2026-10-17T00:33:07.075Z] TOOL RESULT

```
PHD
NYB
```


## [2026-10-17T00:33:11.553Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5282,5294p HUB.txt; sed -n 1382,1390p HUB.txt; echo HRN; grep -n -i 'ōšīdan\\|osidan\\|ösidan\\|ōstan\\|ustan\\b\\|ūz\\b\\|yöz\\|yōz\\|gösldan\\|söhtan' HRN.txt | head -20"
}
```


### [2026-10-17T00:33:11.870Z] TOOL RESULT

```
doch siehe oben § 35, a. Dazu np. arm 'Arm* = skr. irmd' ; sar 'Eopf
= skr. giras' ; har "Brust* = skr. tiros (aus *vura8) ; harra *Lamm' aus
^varn-ak, skr. tirana- (aus *t?Mrow(i-), gr. j^aQsr- (nom. urspr. *vren
und *vfrBn, gen. *vpio8) ; guSarad *geht vorbei* =: skr. vi-tirati ; sard
*kalt* = zd. sar eta- (skr. *girta'); arask, rask *Neid*, skr. irasyati
(oben p. 13 J.— 151 ~
trennt', zd. yuta-; Justan *suchen' von einer Wzl. "^i/udh?;
Jastan *springen, eilen' von einer Wzl. yas ? ; Jash 'Ungliick*,
zd. yaska-?; Jasn Test' = zd. yasna-; juy *Joch' = skr.
yuga- ; Juft 'Genosse, Gatte* = zd. yuxta- ; jigar *Leber =
zd. yakare ; Jau *6erste' = zd. yava- ; javan, juvan 'Jung-
ling' = skr. yuvan'\ jOsTdan *kochen, sieden', Wzl. Iran. yaus\
Joi, Jo 'Kanal' = ap. yauviyd-; Jam = Jammed = zd. yima
45, 106) auf *vizmurdan zuriickgeht. Damit fallt
Horn's Etymologic, insbesondere piz- aus patis.
314. Der Paragraph ist vollkommen verfehlt und zu streichen.
Vgl. Fr. Miiller, WZKM. 7, 371, dessen positive
Ausfiihrungen {piidh-tdan = pati + s + Wzl. von
np. justan, vgl. phi. vijustan WZKM. 8, 92) freilich
auch nicht einwandfrei sind. Ich lehne also np. piz-
aus patis (wie oben bis- aus abis) ab. Ich finde patis
auch nicht in np. paSkam^ {piskam^ baskam, biSkam)
HRN
5027:Vers 8), deryös, deryöz, deryöze.
5477:aw. |/>c/orf-, raoöahe 'wachsen'; phlv. rustan (bezw.
6790:phlv. sustan, söyBnd^ söy(i)sn; kurd. LW. sustin
7451:aw. l/ftaos-, kusaiti 'tödten'; phlv. kustan, vergl. asö]-
8494:meryözen (Darm es teter. Et. ir. II, 132).
9743:- 1129. yöz *Jagdleopard' (Vis und Kamin, Seite 40 Vers 12'^).
12009:./cryöz 6Öfl.
20101:yöz 508.
```


## [2026-10-17T00:33:20.259Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 9735,9750p HRN.txt; grep -n -i 'josidan\\|jösidan\\|jusidan\\|jöüdan\\|jöy\\b\\|jöstan\\|jostan' HRN.txt | head"
}
```


### [2026-10-17T00:33:20.718Z] TOOL RESULT

```
C"--' ap. ^aivaka-, vergl. am/- 'ein'; aw. a^oa-; phlv.
rwak, ev, phlv.-päz. yak (PPGL), ai. eka-,
kurd. Iki jemand' (H.-Sch.), yek (LW.); af;'. yö;
oss. d. yeii, t. yu *ein' (146); bei. eyök einzeln (171);
wa/. li\ ^, sij n. ylv, yu, yä, yi, sar. iv, f, ivj 'einzig,
allein*, ya/n. 7, minj. yao, sangl. vak.
Aus a/?;a- *ein' ist auch das yä-l validet -e ent-
standen.
- 1129. yöz *Jagdleopard' (Vis und Kamin, Seite 40 Vers 12'^).
vergl. arm. yoizlc *das Suchen', yuzem 'suchen, unter-
suchen' (daneben luiben beide Worte noch die Be-
M Zu \ !/((m- ßartholomae, BB. X, 278J.
*) Im FU finden sich drei Belegvorse au8 Nizäri.
*) Scythisches *amalchius* — vergl. Plinius IV, 94: 'septentriotialis
oceanus, amalchiiim cum Hecalaeus appellat a Parapaniso amne, qua
Scythiam adluit^ (juod nomen eius gettfta linyua significat conyelaium*
3919:419. Junten 'suchen, verlangen', Praes. jöy-em.
3922:yat, yödhd' ; phlv. jöy(i)sn, jöy(i)sn7h (Men.) ; gr. vofiivTj.
3947:Pfluge befestigende Lederriemen' (H.-Sch.); bei. Jöy
11322:227. v{i)JuHtan (päz. vajöstan) ^forschen, untersuchen
11323:(MSn.), v(i)ßisfar, v{i)jöy{i)sn (AV.).
16190:\jöy(i)i«V, 419.
```


## [2026-10-17T00:33:23.169Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3915,3930p HRN.txt; sed -n 9750,9760p HRN.txt; grep -n 'jösidan\\|jöSidan\\|jösTdan\\|jösldan\\|josTdan' HRN.txt | head"
}
```


### [2026-10-17T00:33:23.653Z] TOOL RESULT

```
Käs. «/erfö akerün, yedöi (Qohrüd).
aw. yuta- getrennt' ; phlv. jutäk^ jiit hezw yyutak, yuf.
Darmesteter, Et. ir. I, 57 Note 1, Salemann, Mel.
asiat. IX, 247 Note 75.
419. Junten 'suchen, verlangen', Praes. jöy-em.
Käs. veyüst,
aw. [/'yaoä-, yüiöy^iti 'kämpfen'; ai. l/^yadh-, ayudh-
yat, yödhd' ; phlv. jöy(i)sn, jöy(i)sn7h (Men.) ; gr. vofiivTj.
Hörn, KZ. 32, 587 No. 22.
420. jesten 'springen, eilen; (auch vom Winde)*, Praes.
jeh-em; HV^* '•Jl^^^Di 'zum Ziele kommen (Is. 53, 10 u. ö),
Nn^r->.1 (Is. 14, 29).
ai. \/^yaS', ydsyati, yäsati 'sprudeln , skr. 's. abmühen,
s. anstrengen*; aw. [/^yah- 'sieden', vergl. yaesyantim
äpetn; phlv. Jastan, jahet (Men.) bezw. yastan,
bei. LW. jihag 'entkommen, entrinnen' (115).
Scythiam adluit^ (juod nomen eius gettfta linyua significat conyelaium*
— 80, wie das Wort dasteht, heranzuziehen, ist bedenklich.
*) Men. 7, 27; K 48 hat snehr *Schnec*, vergl. unter * Verlorenes
Sprachgut*.
^) Keimt auf röz. Felis jubata Schreb., Blanford, Seite 35.- 253 —
deutung *die Aufregung, das Wogen' bezw. *auf regen',
vergl. aw. l/^i/aoz-, yaozaiti sich bewegen, wogen,
wallen, Htibschmann, No. 214).
kurd. LW. yilz 'kleiner Jagdhund* (H.-Sch.); arm.
LW. (?) yovaz^ yavaz 'nuvifqQ.
Ursprünglich als Jagdtier *der Sucher (de Lagarde,
```


## [2026-10-17T00:33:28.815Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"sieden\\|kochen'\" HRN.txt | head; grep -n -i \"yaes\\|yaēš\\|yaeš\" BRT.txt | head; grep -n -i \"yaoz\\|yaošti\\|yaosti\" BRT.txt | head"
}
```


### [2026-10-17T00:33:29.199Z] TOOL RESULT

```
2798:aw. skr. [/^pac- 'kochen' ; phlv. pu^tan^ pazem, pazBt
2800:kurd. patin 'kochen', bepiz; afy. pa/avul; oss. d. ficun^
3492:Fieber*; ai. [^tap-, tdpati; phlv. täftan 'sieden' (vd. 4
3928:s. anstrengen*; aw. [/^yah- 'sieden', vergl. yaesyantim
3932:der V^yeS' ist 'sprudeln, kochen, sieden , vergl. auch
3988:430. jösTden *koehen, sieden, jös{pere), jösäk, jösänldtn,
3992:sieden; aufbrausen, zürnen' (181).
3557:•  j.  a-pantay-  m.  'Nichtweg,  Unweg":  a^i!\  '}■  «payaü,  apayäiü  (usw.):  s.  ap-,  'ay-  und /an/il  ya  asahe  vispe  anyaesam  °tam  "  "es  ■''"*■
6583:—  yet'ikh  vS  aisS  ultrSMäniS  anhal  V, '  (auch  mit  dat.  Inf.) ;  Bj  im  Aw, :  mahmai 75.24; —  am?^anqm  sp^ntanqm ..  yaEsqm\hyättt  *ava>ihl  Y.50.J;  —  s3raos5  ilä asti  hamtm  manB  Yty.Ss;  —  asit"^  sWastB  ahurahs  tnazds  yasnäiY.  ^6.\;  1—3, iaitn  y.i^a  apannSyliiaAe  V, /j,  44;  44*; ;  70.Ö,  Vr.p.  7,  15.2;    —    nil>ma  *haoma.-
13825:•  j,  duzäpya-  n.  'Schwer-,  Unbeikömm- lichkeit',  mit  Akk.  (des  Obj.):  yaesam anhat  'fim  änval.psntum  "für  welche  die (^-Brücke  schwer  (beikömmlich,  sva.)  _un- überschreitbar  sein  wird"  V.  y,  3.
17811:urunasca  •s'i/äi  yazamaiäe  N.  ~o;  — aläunqmcü  'i^ibyö  a^üunqmca  urvöibyB  Y. 4.2;  —  vispanqmta  . .  yaes'qm  *yah'i:'waca urvqnS  zaoyasia  'j-iiy?  Yt./J.i48;  —  haom urvän>m ..  Aavqm  's'mY.ji.  18;  —  kavahe uruns  "/Ä  Y.  j.  18;  —  mit  urvan-  gleich- gestellt: *iva.ahra  .  .  h?nti  iristanqm urvqrtS  ya  asäunqm  "sayö  FrW.  10.  39; Y.  26.  7 ;  —  asahe  virazd  (sd.)  .  .  yähu iristanqm    urvqnS  *iäyente  ya    aiaunqm
20018:•  g.  maraxtar-  m.  'Zerstörer,  Verderber*: atshsus  °tars  ahyä  yaeSa  mazdä  "und  die Verderber  dieses  Lebens,  o  M"  V.  J2. 1 3 ''.
20942:•  j.  yaeSant-')  Adj,  (fem.  *A«rt"-),  PPA.-. s.  yaA-.
21000:geht  dauernd  damit  um  zu  -,  bemüht  sich       mit  vi  Kaus.  'auseinander,  überwogen dauernd  zu-',  mit  Inf.;  *iijVa«?OTÄwAj«a  lassen':    hö   trayS   äyaesayelH   hs   zray5 («■Alf  j:r-o:i5»*j'"  aj/^(Sp.34om.)  "undm   vxvaozayät'i*^  YtÄ'.3i. ehrTürchtiger  Gerechtigkeit  soll  er  dauernd      nbaL^usiT '(sich) bewegen';  um.yuitl 'tapia- sich  bemühen,  seine  Weisheit  zu  mehren",     ""';  Wmi.  AGr.  /.  199.  —  Pä,.-  öfÄßa««,
27572:•  j.,  g.  zaoya-  Adj.  (fem.  'yä-)  'zu  rufen, der  sich  rufen  lässt,  invocandus',  von  Gott- heiten: yaesqm  *yahliwaca  urvqns  "yäsca
28836:me  slärS  .  .  halante  paraca  mi  twr^iyS i^arynS  *baxsprUa  yaesi  .  .  ".  .  dass  sich die  Sterne  mir  zusammentun  und  voran der  Mond,  um  den  Kriegern  Herrlichkeit zu  schenken,  will  ich  , ."  Yt  <S'.  i.  [ha- (imna  V.  44-  13:  lies  Aa^na;  —  kaxiaitt N.p:  lies  hä  xsayete.
29552:•  j.  havatmasah-  Adj.  '(von  gleicher Grösse  sva.)  ebenso  gehoben,  stolz';  yat kmnaoiti  driyaes  °s^  manS  ya%a  ,,  "weil er  des  Armen  Sinn  ebenso  stolz  macht, wie  .  ."  Y.  10,  13;  13.
2447:lausgesprochenen)  Gegensatz;  a}  adjekti- \Tsch,  mehrfach  sva,  'dieser  mein,  unser" ahmäicä  ahuyi  manaüyäicil  'Tilr  das  Leben hier  und  für  das  geistige"  V.  40. 2 ;  —  ahyil anhSus  asti<atö  manhrahasca  Y.  43. 3 ;  J2. '3.  34-6j  45-3t4i  —  aAe.'a  anhius  .  . ■ .  manahyeheta  ankiul  Vyt  $2;  —  ahum Tütümca  gaf^anqm  yaozdatlr?m  anham dämanqm  Vi.  70. 92J  —  aisqm  atthunqm hstam  Vyt.  JO;  —  kva  ..  aiiika  zimS  "wo auf  der  Erde  hier"    V._j.i,7;  15,  18,  34,
2463:paiti  vä  xsa/ne  . .  nöit  . .  aiähe  ayqn  nöit aiiihä  xiapö  .  .  Yti.iS;  —  asankatca iöi'irSatca  ..  kaoa  nö  ahmäii*  asarahaica läiiraiüi  ..V.ff.Sif.;  55'\  56i\Y.^S.2; — sraoi»m  .  .  yö  dalnöJiisö  *da?nayä  . .  aya dalnaya  . .  Y,  57. 24;  —  , .  parö  jbi^anbyö .  .  alsqm  tbifyaniqm  Yt-  io.T%i.;  —  yaoz- däiqm  saeirqm  . .  änhqm  zaoiranqm  Yt. io. lai f.;  Y.2(j. 2;  —  vä^^m  srJr^m  .. ahmya  väse  Yt/o.  12411;  5.11;  —  äp)m andvim  . .  *atihasca  mi  *aSva^hä  apö ¥.(75.1—5;  5,  V.ö,32  (aitiha);  —  nmS- mm  .  ,  äat  ahe  nmänahe  V.^.3;  14,  40; —  narö  . .  äat  aisam  naram  aivS  iri^yai (vat  antarp  *n3rius  .  .  V.j.z?;  5.43,  44, A.4.6,  Yt.iO,i37;  —  ygi  nmüni  hqm. barämahi  . .  äat  pascaeta  ahe  nmänahe , .
2733:holz  zum  mindesten  darbringend  ist  man  Inf-  <^t^^;  Absol.  'agi?m,  •iünbrn. r.f'  N.106;  —  iat  tä  °ma  (^V.)  yaoz-  i)  '(etwas)  suchen,  suchen  nach  -, dayqn  ar>h>n  V.  7. 28;  ■ — ■  pairi  urvarä-  aufsuchen':  yd  aüm  mainimnö  ahm byasca  varsoäbyasca  'tnaiil^ö  "abseits  von  isimnS  ahm  apa.rao'iayeiU  {sA.)  .  .  dru- Bäumen  und  Sträuchem,  die  Brennholz  jimca  vinasti  V.  7.78;  —  Med.  auch  in sind  (geben)"  V. /6'.  2;  —  Auskam  °m»m  reflex,  Sinn:  vSrrinahe  .  .  yS  vazaite  .  . Y.JI.8; — Auskanqm  ..  'manqm  ,.  nafi-  axsa/hi  {sä.)  xsa/hTm  tsfmnS  \'t  14.  20; tanqm  ..  xraozdvanam  ..  varidvanamY.    ao.  a)  mit  Dat.  comm.:  vlstäspahe  ..
2734:7. 3IJ/5.24,  /.^.  2j3;  —  'manqm  ..husatqm  yö  .  .  asäi  ravö  yaisa*''  .  .  ravö  t'TvaAa A.j.  5';  —  'manqm  yaozdätanqm  Y.t8.  "V.,  der  dem  Asa  ..  Raum  suchte,  .. 19;  22;  —  'mtmi'f  .  .  hüBs  *rat>cas.pai-  'Raxaa  fand"  Yty.gg;  —  äat /rasüspnie ristqm  Y.  62. 10;  —  'mgm^  däityS.aüman  \ .  .  fravalayö  .  .  ap>m  ais^mna^  haväi "Brennholz,  das  aus  den  gehörigen  Brenn-  käcit  näfai  (sd.)  ". .  um  Wasser  zu  suchen hSlzem  besteht"  N.  ioj;   —   aiUm  'mrm  jede  für  .  ."  Yt/_J.66.  b)  ohne  Obj.:
3143:•  j.  a-x§nüta-  Adj.  'nicht  zufrieden  ge- stellt': yezi  aesö  nn  yö  yaozdai:ryö ..tbistö "tö  paräili  V.  9. 40.
3326:•  j.  a-dbi§ta-'>,  a-tbiäta-'>  Adj.  (fem. °/p-)  'nicht  angefeindet,  gekränkt':  iitar/.. xsnStä  °tö  \.62.^;  Yt  lO.iio,  V.(j.39,  Yt. '3-^5'  —  xsnataheat  'tahe  mi>ra  manS yaozayeiti  "(aber)  auch  des  befriedigten, ungekränkten  Sinn  bringt  er  durch  M.  in Aufruhr"  Yt  /o.  1 1 1 ;  —  xsnUth  ainili  °t^ ..  fravaiayö  Yt/y.si;  34i  63;  —  "'"^ (VS.)  Yt/2.8.
3364:ahurö  mazda  A.4-  3.  b)  zurückweisend: kat  tl  aisma  yaoidayani  . .  aitiha  Z3mö niäai'iyan  . .  hak^ryt  dpö  vlsraslaym  'ia yaozdayqn  V.  7,28f.;  74,  N._<?j,  YL/0. 117;
3735:•  g-  *aipi.z^3'a-  '*  n.  'die  künftige  Geburt': yaoz^izA^  masyät  '%3m  vahUtH'H.4^.%; ziL  V,  j.ai,  wo  NA.  aipiji'.
4190:•  '].  a-ohvä-,  g.  a-hvä-"  f.  i)  'Antrieb des  Willens,  Schaffensdrang,  Lebenskraft' : pairika  yä  duzyäirya  vlspahe  atiksui  .  . ' faröit pairi'in^misA.)  anhvqm  avaAisiiyät\ (sd.)  Yt.Ä54;  —  ava  m!  3zis  .  .  par5it\ fairrbnpm  (sd.)  arihvqm  ava.d}nnqn  sada- 1 yäfi  (sd.)  V.  i5. 19.  2)  'Antrieb  derl Seele,  innerlicher  — ,  Gemütsdrang,  Ge-j müt'"':  kal..*manS  asti  vT/aymii'tfm{s±) anhvqm  vjmar3zist?m  (sd.)  VL  /.  2 ;  —  ' virtzvatca  (sd.)  mat^  vansvatica  attuAa  j 'W.  62,10;  —  ye  kvam  ankvam  yaozdaite\ humatsilia  .  .  V.  ^.2i^>;  si  *PÜZ.,  lO.  19  I PüZ.;  —  dusx'arpnä  . .  asH5  asti  auuhaya  \ (LS.)  ".  .  ist  unfroh  in  seinem  Gemüt"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"  Yt  /o.  9;  —  fora  vi  räki  am?sä spmtn  yasmmcä  rahmtmcä  firä  mana»hä ..  vaiaahä  ..  syat>^anä  ..  dw^iy«  (IS.) » Y.7/.18.
4851:•  j.  a-yao«day^n  Inf.  'nicht  zu  puri-'o^er .  .»■' V.&46;  —  gaomacsim  . .  ufia- fiziren':  kat  ta  nara  yaozdayan  anhm  ya  nhansim  (sd.)  'mm  v3  srum  vä  ". .  Ge- nasaum  franuharat  sünö  va...  ay  amAjn'^'^^  ^"s  Eisen"  V.p.14;  j6.6.
```


## [2026-10-17T00:33:36.699Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3926,3940p HRN.txt; sed -n 3986,3996p HRN.txt; grep -n \"yaoz-\\|yaozaiti\\|yaosti\\|yaoSti\\|yaoxti\" BRT.txt | head -5; grep -n -i \"yud-\\|yaod-\" BRT.txt | head -5"
}
```


### [2026-10-17T00:33:37.156Z] TOOL RESULT

```
Nn^r->.1 (Is. 14, 29).
ai. \/^yaS', ydsyati, yäsati 'sprudeln , skr. 's. abmühen,
s. anstrengen*; aw. [/^yah- 'sieden', vergl. yaesyantim
äpetn; phlv. Jastan, jahet (Men.) bezw. yastan,
bei. LW. jihag 'entkommen, entrinnen' (115).
Hörn, KZ. 32, 587 No. 22. Die Grundbedeutung
der V^yeS' ist 'sprudeln, kochen, sieden , vergl. auch
gr. 'Qsm.
421. jenk 'Unglück* (unbelegt).
aw. yaska- 'Krankheit'; phlv. yask (N. pr. Yaskdat
auf einer Gemme ZDMG, 44, 652 No. 7 ist zweifel-
haft), tsk (Bund.).
422. JeSn 'Fest, Gelage* »).
*) Im FJ durch einen Vers Euveri's belegt. Häufig im Sähname.— 95 -
aw. yaswa-; i^hlv.jfasn bezw. yasw Test* (West, Pahl.
eines Vierfüsslers'; ai. yüvan-,
LW. kurd. juvän; afy. javän; bei. javan (111).
430. jösTden *koehen, sieden, jös{pere), jösäk, jösänldtn,
Ka§. vöyösnaä, böyösad (Qohrüd).
ai. yüs-, yüsdn- 'Brühe*.
LW.(?) kurd, jüSverdin, jüsdnin; hei, jösenag 'kochen,
sieden; aufbrausen, zürnen' (181).
431. jöf, jö *Kanar.
ap. yauviyä'^); phlv. jöi bezw. yöl; ai. yavyd'.
LW. kurd. /i?; Sity,jova; bei. /ö * Wasserlauf, Kanal*
(117).
2463:paiti  vä  xsa/ne  . .  nöit  . .  aiähe  ayqn  nöit aiiihä  xiapö  .  .  Yti.iS;  —  asankatca iöi'irSatca  ..  kaoa  nö  ahmäii*  asarahaica läiiraiüi  ..V.ff.Sif.;  55'\  56i\Y.^S.2; — sraoi»m  .  .  yö  dalnöJiisö  *da?nayä  . .  aya dalnaya  . .  Y,  57. 24;  —  , .  parö  jbi^anbyö .  .  alsqm  tbifyaniqm  Yt-  io.T%i.;  —  yaoz- däiqm  saeirqm  . .  änhqm  zaoiranqm  Yt. io. lai f.;  Y.2(j. 2;  —  vä^^m  srJr^m  .. ahmya  väse  Yt/o.  12411;  5.11;  —  äp)m andvim  . .  *atihasca  mi  *aSva^hä  apö ¥.(75.1—5;  5,  V.ö,32  (aitiha);  —  nmS- mm  .  ,  äat  ahe  nmänahe  V.^.3;  14,  40; —  narö  . .  äat  aisam  naram  aivS  iri^yai (vat  antarp  *n3rius  .  .  V.j.z?;  5.43,  44, A.4.6,  Yt.iO,i37;  —  ygi  nmüni  hqm. barämahi  . .  äat  pascaeta  ahe  nmänahe , .
2733:holz  zum  mindesten  darbringend  ist  man  Inf-  <^t^^;  Absol.  'agi?m,  •iünbrn. r.f'  N.106;  —  iat  tä  °ma  (^V.)  yaoz-  i)  '(etwas)  suchen,  suchen  nach  -, dayqn  ar>h>n  V.  7. 28;  ■ — ■  pairi  urvarä-  aufsuchen':  yd  aüm  mainimnö  ahm byasca  varsoäbyasca  'tnaiil^ö  "abseits  von  isimnS  ahm  apa.rao'iayeiU  {sA.)  .  .  dru- Bäumen  und  Sträuchem,  die  Brennholz  jimca  vinasti  V.  7.78;  —  Med.  auch  in sind  (geben)"  V. /6'.  2;  —  Auskam  °m»m  reflex,  Sinn:  vSrrinahe  .  .  yS  vazaite  .  . Y.JI.8; — Auskanqm  ..  'manqm  ,.  nafi-  axsa/hi  {sä.)  xsa/hTm  tsfmnS  \'t  14.  20; tanqm  ..  xraozdvanam  ..  varidvanamY.    ao.  a)  mit  Dat.  comm.:  vlstäspahe  ..
5765:•  g.  a-siStay-"  f.  1) 'Verheissung  auf-' (Akk.):  iä^ä  mSt  yqm  yaoi  damam  yaoz- däm  yqm  *Aud3naos  paiüh  saüyat  xsa- %raAya  xnlvä  xsaira  %wSvqs  °tls  (AP.) mazda  "ob  mir  wohl  für  das  Ich  des  ein- sichtigen, das  ich  vervollkomnmen  will, der  Herr  des  Reichs  Verheissungen  auf  die sicheren  Reiche  machen  wird,  einer  (ein Gott)  wie  du,  o  M."  Y.  44. 9-  2)  'Gegen- stand der  Verheissung,  verheissener  Lohn': at  -tä  (LS.)  yao/an/l  (sd.)  il  /lusiUis  .  .  Y. _jo.io.         \\.34-A'  lies  astshm.]
7133:fraiatimea  .  .  g}us  *vTmitim  N.  tf5(?);  — hat  drajo  haca  ''iirat . .  apat  . ,  baraimn /rast jiryiltV. 3.1(1;  17,  16.^,  l-J.a,;-^  aal tum  nisAioOis  apasca  .  .  yazimnö  'tarimca H.  2. 1 3 ;  —  (7/;»«  ä  va  °trpm  ä  vä  V.  7. *S;  5-37.  *.i04-io6,  Y.7.12,  2.12;  — '^/r  .  ,  aiwyö  V, /<S'.  70;  —  yoi  nmaiia hamiaräntaki  'trimca  bansmaca  tastaca haomaca  hävanaca  V.5,39;  40;-—  'trsm yaxaita  bansma  st}r>na3a  V.  12. 2 ;  J.  1 5, Vt.;2.3,  A.4.5,  Y.f?.s6.  b)  von  dem beim  Gottesdienst  (im  atas  dan  'Feuerbe- liäiter')**'  dämmenden  Feuer:  Hat  ätra- vaxsake  (sd.;  nämL  kairim  atthat)  yat '■tr>mca  aiwi.vaxsayät  ''^rasca  Hlr5  iiraxtis yaoida'^al  N.  Jj;  ffi;  —  aal  frahratarS Isd.)  yat    'Tirasca    alfqm    %raxlim  yaoz-
15014:•  j.  patti  yaozday^  InC :  s.  unter  yaoz- dayqn.
20972:•  j,yaod-V. 'kämpfen'.  Praes,  %t ysCöya-. 'kämpfen';  a)  absol.:  fä  [y&JiA.fravasayB)
```


## [2026-10-17T00:33:45.401Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{0,30\\}yao[sS]ti.\\{0,200\\}\" BRT.txt | head -5; grep -n -o \"•  j.  yaoz-.\\{0,300\\}\" BRT.txt | head -3; grep -n -o \"j,yaod-V.\\{0,300\\}\" BRT.txt"
}
```


### [2026-10-17T00:33:48.661Z] TOOL RESULT

```
20972:j,yaod-V. 'kämpfen'.  Praes,  %t ysCöya-. 'kämpfen';  a)  absol.:  fä  [y&JiA.fravasayB)
```


## [2026-10-17T00:33:52.485Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{0,40\\}yaoz-  *V.\\{0,250\\}\\|.\\{0,20\\}yaoi-V.\\{0,200\\}\\|.\\{0,20\\}yaoz-V.\\{0,200\\}\" BRT.txt | head -5; grep -n -o \".\\{0,30\\}'Regsam.\\{0,150\\}\\|.\\{0,60\\}Rührigkeit.\\{0,100\\}\" BRT.txt | head -5"
}
```


### [2026-10-17T00:33:58.663Z] TOOL RESULT

```
ugrep: error: error at position 246
-\xbf][\x80-\xbf]*){0,200}
                          \___exceeds complexity limits


ugrep: error: error at position 169
x80-\xbf][\x80-\xbf]*){0,100}
exceeds complexity limits___/
```


## [2026-10-17T00:34:01.750Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='ignore').read()\nfor pat in [r'yaoz-\\s*V\\.', r'yaoi-\\s*V\\.', r'yaoxsti', r'yaos?ti-', r'Regsamkeit', r'yaoSti']:\n    for m in list(re.finditer(pat,t))[:3]:\n        print(pat,'|',t[max(0,m.start()-60):m.start()+220].replace('\\n',' '));print()\nEOF"
}
```


### [2026-10-17T00:34:02.220Z] TOOL RESULT

```
yaoxsti |   (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf yaoxstibyä ..Yti0.82;82'; — paiti  vä  asni'  vaa   sein  Hab   und  Gut"  Yt. 5.109;  113; paiti  vä  xsa/ne  . .  nöit  . .  aiähe  ayqn  nöit aiiihä  xiapö  .  .  Yti.iS;  —  asankatca iöi'irSatca  ..  kaoa  nö  ahmäi

yaoxsti | yahmäi  hazaitnm ^'■57-4j  —  allat  dim  vlspanqm  mazih?m\yaoxstinqm  fradd^at  °rS  mazda  Yt^.45; dazdyäi  (sd.)  ahUm^a  ratUmca  yim  °r}m\iQ.Z%; —  tistrim  ..yim  ratüm  frada'hat masdqm  Y.  27.  i;  Vr.  /;.  21;  —  imimca'  'ro  mazdä  YL<?.  44;  5-  89,  70.103,^5.

yaoxsti | ya  bäzvB  dannaca  V.?.  25;  —  afys dsikrabyS  aiwyasca  yaoxstibyB  Yt/o.  Sa; —  kava^bya  p^aHbya  x^a^diyäia  varsa V.  tf.  46;  —  zara%ustrMn  atnm  pairi.- yaozdd^snlim  gä^äsca  srävayanttm  Y.g.  1 ; I —  :^ar>nte  vahistS  urunaica  pa%mainyB.- '  timB  Y.Q.  1 6 ; 

Regsamkeit | Hds. /förJ/V-  — 3)  Hds.  fravaity. •  j.  {riranha-  n.  'Regsamkeit,  Munter- keit': kahmäi  . .  upav/tacayeni  (sA.)  'nhai haomanaahai^a  Yl  5.  8. Ableil.  aus  */rärah-  Adj.  'sich  regend',  Komp. 'frä-^*arah;  zum  V.  'ar-.     Unsicher. •  j.  ^frirayatraS-a-**  m. 

Regsamkeit | :   ünSi  ^apel  'er  schläft  wach'. •  g.  'zaeman-  n.  'Regsamkeit,  Munter-, Wachsein' :  ks  hvaph  c^afmmca  dät  'mäcä "wer  schuf  wohlwirkendSchlaf  und  Wachen" Y.  44. 5. Zum  ai.  V.  MnlH  'incitat'.  —  Vgl.  *tainak; 'toimaii',  viaSäla-,  —  ai.  aiu-htaian-  Adj
```


## [2026-10-17T00:34:07.623Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"jōy\\|joyisn\\|jöy\\|j[oō]y[iī]šn\\|jost\\b\\|jōšīdan\\|jōš\\b\\|yōz\\|yoz\\b\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20; grep -n -c . PHD.txt"
}
```


### [2026-10-17T00:34:08.054Z] TOOL RESULT

```
PHD.txt:225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
PHD.txt:1660:disturb āyozīdan, wišuftan,
PHD.txt:2665:loosen wiyoz-.
PHD.txt:3847:strive āyozīdan, kē(x)šidan, tuxšīdan.
NYB_vol2_glossary.txt:597:api-yuxtan Ppywwhtn'] api-yoz- ['pywwe-] to connect, to attach: "meč (v.s. v. mēx) be apiyuxt he (attached a pole to it =) he barred it with a pole (or, bolted it with a bar) 42%; — pres. api- yožend ['pywweynd] DkM 82, — upa- or api- (v. s. v. apa-) + Av. (1228 sq.) yaog-. As to the spelling -yw- for -iy- cf äyiyänak, giyäk, niyandar. — Bailey’s interpretation of 4210, ZP 112 n. 3, is untenable.
NYB_vol2_glossary.txt:1342:dräyän-jöyisneh [dPd?n ywdšnyh] the act of chewing performed by one who is chattering: ~ kartan to chew when chat- tering (we would prefer to say: to chatter when chewing) 691°. — drāyān pt. of the next w.; joyišneh det. v. n. of jütan (g. v.). Paz. dräeq jčišni. Skr. v. mauna- madhye jalpa ‘chatter in the midst of silence’, i.e. where silence ought to prevail.
NYB_vol2_glossary.txt:1926:han-tai [ZK D] until, on to: ~ 6 mtyān van to the middle of the tree 415; ~ hàn i veh Dāitī 564; peš hac ~ ka-män ... jöyät before he devours us 98%’ (as to man, v.s. v. man). — Olr *anu-tävat 'to- wards as far (as), cf Skr tāvat ‘so long, so far’ (yāvat ‘as’), v. tāt; hence Milr *(h)an-tàv, SW han-tai, later *(k)andāt, Paz. anda. Prth han < anu, KZŠPrth 1.2 hn prhš L = han fraxé 6, Gr fog čurpoo0ev, also han 6 ibd. and l. 19 = Prs l. 24 D = tai, Gr ac. Not found in MPrthPrs — Av. (127) anu, OP anuv.
NYB_vol2_glossary.txt:2034:hu-āyēzišn [hw'ywešn'] of good endeav- our, efficiently furthering the activities of the different classes of the community 5027, according to the gl.: ku kar i aparik veh dānēt kartan ‘that is: it knows how to do the work of the others [not only that of the cattle-breeders] in the best manner’. — To be read with -z-, not -ž-, v. dyoz-.
NYB_vol2_glossary.txt:2139:joyišn [ywdšn'] the act of swallowing, eating 53?. — V. jütan.
NYB_vol2_glossary.txt:2140:jöyisneh det. v. n., v. drüyàn-—.
PHD_mackenzie.txt:1392:AyOxtan, AyOz- ['ywhtn , Jywe _] join, yoke.
PHD_mackenzie.txt:1396:IAyOzidan, iiyOz- [Jywe-,'tn l I P uyu,It, Uywz_] trouble, disturb; strive,
PHD_mackenzie.txt:2054:drayan-Joyisn [d1'd'n ywdfn ] one who speaks while eating.
PHD_mackenzie.txt:5471:wiyoz- [wydwe-] loosen, undo.
PHD_mackenzie.txt:5710:yoz [ywc IN ......] cheetah, hunting leopard.
PHD_mackenzie.txt:6161:carpet bob.                             cheetah yoz.
PHD_mackenzie.txt:6476:eating xwarisnih; (daevic) Joyisn.           enthroned, be ,....., abar nisastan.
PHD_mackenzie.txt:6956:lamp ciray.                               leopard palang; hunting""'" yoz.
PHD_mackenzie.txt:7027:loosen wiyoz-.                             First - Gayomart; old - zarman;
PHD_mackenzie.txt:7867:undo wiyoz-.                             urine mesag, pesyar; bull's,..... gomez,
5579
```


## [2026-10-17T00:34:17.140Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"seek\\|search\" PHD_mackenzie.txt | head -20; grep -n -i \"wiǰ\\|wij[oō]y\\|wizōy\\|wizoy\\|wijust\" PHD_mackenzie.txt | head; grep -n -i \"^j[uū]tan\\|jūtan \\[\" NYB_vol2_glossary.txt | head -3"
}
```


### [2026-10-17T00:34:17.531Z] TOOL RESULT

```
342:   In seeking an unknown word, or one known only in another
5655:        xw'stn, xw)h-, N ""] seek, want, desire; attract, acquire.
7533:seek xwiistan.                            shallow tanuk.
```


## [2026-10-17T00:34:26.183Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 27 28 29; do echo \"### leaf $l\"; awk -v n=$((l+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n -i \"jōy\\|joy\\|jôy\\|justan\\|jostan\\|yaod\\|yud\\|جستن\\|جوی\" | head -20; done"
}
```


### [2026-10-17T00:34:26.651Z] TOOL RESULT

```
### leaf 27
68:         ‫چون جره باز ‪ .‬نظامی کنجوی ‪.‬‬        ‫ك‬
### leaf 28
36:           ‫نظاعی کنجوی‪ «.‬کنجینه ‪ 5‬ی‬
### leaf 29
```


## [2026-10-17T00:34:30.424Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:571 2>&1 | head -80"
}
```


### [2026-10-17T00:34:30.951Z] TOOL RESULT

```
no scan of BQT covers printed page 571 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:34:36.313Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"جستن\\|جوشیدن\" BQT_v2_pages.txt | head -20; awk 'BEGIN{RS=\"\\f\"} /جوشیدن/ {print NR-1}' BQT_v2_pages.txt | head; awk 'BEGIN{RS=\"\\f\"} /جستن/ {print NR-1}' BQT_v2_pages.txt | head"
}
```


### [2026-10-17T00:34:36.888Z] TOOL RESULT

```
1557:  ‫‪۷‬ق‪-‬ول هرن از ره هندی باستان ‪ ( 125۷, 2 52‬جوشیدن » فوران )»‬     ‫ب‬
1558:   ‫‪ « ۳1/0201562 0۳1602‬اسعق*‪ .»۲4‬برك این اشتقاق‬  ‫‪( # ۵۵‬جوشیدن) ›‬    ‫اوتا ‪-‬‬
3205:‫که از جوشیدن ‪ ۸‬و ازشورش وبهم برآمدن‬                  ‫من" بلغت زند وپازند (‪ )۱‬بمعتی‌استدن‪.‬و کرفتن‬
3225:                          ‫‪ ۸‬رك ‪ :‬جوشیدن ‪.‬‬               ‫‪ « :‬نشی» و رل ‪ :‬جوصق‬      ‫ره‬      ‫‪۲‬‬
3249: ‫حو شده مغر = کنابه ازمردم خشمناك‬                                                                 ‫جوشیدن باشد ‪.‬‬
3298:   ‫کردن» سر برآوردث کشت ‪ -‬حرارت بخرح دادن ‪« :‬دولت نه بکوشدن است‪ .‬چاره کم جوشیدن‬
3579:                                                       ‫‪ ۷‬د‬                ‫‪ - ۷‬رك ‪ :‬جستن ‪.‬‬
4684:                         ‫که اکزردن ک‬                                 ‫خصومت و جنگ وتعدی و کک جستنرا‬
4742:‫کسی جستن باشد ؛ وباین معنی‌بجای حرف ثالی‬                                                ‫هم آمده است ‪4.‬‬
5389:                 ‫چاره جستن ‪ -‬و دومدن باشد ‪.‬‬
7057:                                                        ‫بمعنی جستن وخیز کردن گ‪-‬رویختن باشد ‪.‬‬
13108:                                                                                ‫وجستن پهلو را کوبند ‪.‬‬
13347:‫بخوه‌روبان‪-‬‬        ‫وختن‌سوب‬    ‫از ملك خا‬    ‫شهر ست‬     ‫ومانند آن ‪ -‬وبه‌عنی جستن و یگخرتن هم مده‬
15429:‫هوز‪.‬بمعنی برخاستن وبرجستن باشد ‪۴٩‬‏ ‪ -‬وامر‬
20552:                                                           ‫جوشیدن اخزشم ‪۰‬‬  ‫نضب و‬   ‫روی فهر و‬
20608: ‫وبمعنی ازجای دآر‪.‬دن ‪ -‬وازخشم وقپرجوشیدن‬            ‫را لىز‬   ‫و تند براه رونده و دوفده‬        ‫هم همست‬
28747:‫برجستن باشد بر مثال آهو ‪ -‬و بمعنی آواز و‬                  ‫‪۰‬‬
30231:‫و بفتح اول وظهور ثانی‪ .‬مکان جوشیدن و بر‬                     ‫خوب وخوش هم هت ‪ -‬وزاییدنآ دمی‌وحیوانات‬
30360:                  ‫ودءوضع جوشیدن وآبر‬                               ‫رهر دادو ‏ زهر معلوم است » با‬
30372: ‫جستن باد سخت باشد ‪ ۰ ۸‬وبکر اول‌هم‌درست‬                                                                        ‫«لاگ گردد ‪.‬‬
29
57
58
347
348
508
510
525
63
82
83
93
121
222
226
262
485
510
```


## [2026-10-17T00:34:45.428Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==58' BQT_v2_pages.txt | head -120"
}
```


### [2026-10-17T00:34:45.825Z] TOOL RESULT

```
                                                                                           ‫‪644‬‬      ‫¬‬


                                          ‫باشد ‪.‬‬     ‫هردکان هندی است‬
                                                                   ‫جوز هندی ک‬
‫جوسق ‪ -‬بفتح اول بر وزن زورق ‪۰‬‬                                   ‫که ارگیل باد » معرب آن‬
‫معرب جوسه است که بمعنی کوشك باشد © ‪-‬‬                                              ‫‪١‬‏ ‪.‬‬     ‫لارجیل ست‬
      ‫و کنابه از دوازده برح فلکی هم هست ‪.‬‬                             ‫جوز یدن ‪ -‬بنتح‬
‫جو سك ‪ -‬بنتح اول و ثالك و سکون‬                                        ‫اول‌بروزن‌لرزیدن» غصه خوردن‬
 ‫ثانی وکاف ‪ ۰‬تکمه و گوی کریبان را کوبند ‪.‬‬                   ‫‪1‬‬         ‫و غمناك و اندوهگین گردیدن‬
  ‫عگن»ی‬
      ‫برن‬
        ‫‪ -‬بر وزن او‬            ‫چوسنگ‬                   ‫جوز هندی‬                        ‫باشد ‪. ۳‬‬
 ‫جو مقدار وهمچند جو درکوچکی ووزن ‪٩‬‏ ‪۰‬‬                ‫جوز لنه ‪ - ۴‬بر وزن لوزینه » معرب‬
 ‫کوشك‬
    ‫جوسه عبر وزن روضه ‪۰‬‬                               ‫باشد که امزغز‬        ‫لنوابی‬
                                                                                ‫کوزینه است وح آ‬
‫ویند » و معرب ‪.‬ان جوسق‬
                     ‫را‬‫‪.‬وبالا خانه گ‬                   ‫گردکات پزدد و‪ ۰‬بسنکوینداز سفزیوم ‏‬
                                        ‫ات ‪. ۷‬‬       ‫جوسبو نتن ‪ - ۴‬باسین‪.‬بی‌قطه وبای‬
‫است‬       ‫»وف‬
            ‫ه بورزن مموشعر‬         ‫جو س‬              ‫خوبروی‬    ‫ایجد و نون و تای قرشت بر وزن‬
      ‫‪0‬‬          ‫‪۰‬‬    ‫‪0‬‬            ‫اس‬




‫که از جوشیدن ‪ ۸‬و ازشورش وبهم برآمدن‬                  ‫من" بلغت زند وپازند (‪ )۱‬بمعتی‌استدن‪.‬و کرفتن‬

                                                                   ‫)‪ ۱‬چك ‪ :‬ژلد ویاژند ‪.‬‬

 ‫انارکیل که‌باشکر‬    ‫آمده ول‬     ‫‪( €‬ند*ه)‬   ‫در رسالة بپلوی «خسرو کواتان ورتك وی‬           ‫‪۱‬‬


  ‫خورند بهندوی اثارکیل خواننه و بپارسيك کوچ ی هیندوك ( کوزهندی ) خواند ‪« ».‬اوبوالا‬
                                                                                         ‫‪۵‬؟ ‪°٩‬‏ ‪:‬‬   ‫ص‬

          ‫چو حنظل هریکی زهری بشیشه‪.‬‬                       ‫دو رخ چون جوز هندی رشه رشه‬
          ‫نظامی کنجوی «کنجینه ‪.۳4‬‬
  ‫‪ ۴‬هز ‪natnubesoj .‬‏‬         ‫‪ ۴‬رك ‪ :‬گوزشه ‪.‬‬          ‫اك ‪.‬‬ ‫ز‪:‬‬‫جورك‬  ‫‪۴‬‬
  ‫»رفتن « لریبکه ج ‪ ۷‬ص ‪» ۷۸۷‬‬
                           ‫قرائتی ازکلمهٌ ‪ , 0818006501۷‬پهلوی ‪ » 021215‬ستدن گ‬
  ‫«راحذمای زبان‌پهلوی ‪ .‬آبراهامان ص ‪٩4‬‏ بوستی درفرهنك بندهش (س‪ )۷۱۱‬آرد ‪ :‬جوسبوتن»‬
  ‫قرائت پارسبان بجای « دسیون ؛ ودرشرح « دسیوتن * گوبد (ص ‪ : ) ۵۵۱‬بمعنی آوردن *‬
                                                     ‫رك ‪ :‬جوسه ‪.‬‬       ‫‪۵‬‬            ‫ها‬        ‫بردڻ »‬
            ‫کەجوسنکش بود فطای لوقا‪.‬‬                       ‫‏‪ ٩‬ب‪-‬قطاسی بنجم راز موبد‬
              ‫خ«اقانی شروآنی‪›»٤‬‏‬
                          ‫‪ ۸‬رك ‪ :‬جوشیدن ‪.‬‬               ‫‪ « :‬نشی» و رل ‪ :‬جوصق‬      ‫ره‬      ‫‪۲‬‬

                             ‫‪۱‬‬                                        ‫بقه ازصفحه ‪۸۹٥‬‏‬
          ‫‪ - °‬ونيز رك‪ :‬جوجن ‪.‬‬                ‫راجا»‬    ‫ک)ت«ر‬
                                                          ‫دندن‬
                                                             ‫(لغة خود راباتش افک‬                    ‫‪2‬‬
  ‫‪ «۴‬جوز هرچیت ‪٩‬‏ چون سطح فلك مابل بگراست‬                              ‫‪ -۱‬رك‪ :‬جوجه ‪.‬‬                ‫‪۱‬‬
  ‫ازسطح منطفة البروج بنرورت هردو دلیره بدوجای برابرتقاطع کردند» همچنادکه منطقة البروج‬
   ‫‪.‬س‌نام جوزهر براين هر دونقطه همی افتد ‏‬
                                         ‫بامعدل التهار بدو جای برابر تقاطع کرده احت پ‬
  ‫آنگه چون‌یکی‌را از دیگری‌جداخواهیکردن » بدانك آن تقاط که چون ساره از وی بگنرد‬
 ‫بشمالاوفتد از منطقة البروج رأی‌خوانند وآن دیگرنقاط که چون ازویسکنرد موب اوفتد از‬
  ‫منطقة البروج ذب خوانند‪ « »...‬التفهيم ‪ # . ۲۲۱‬جوژن ‪ -‬بفتح اول وسیم» رك‪. :‬جوجن‪.‬‬
```


## [2026-10-17T00:34:49.742Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==59' BQT_v2_pages.txt | grep -n \"جوش\\|[a-z]\\{3,\\}\" | head -40"
}
```


### [2026-10-17T00:34:50.146Z] TOOL RESULT

```
3:                                                                                                           ‫جوشاك‬
6:‫زره را ‪ -‬و دلشب بعنی لصف شب ‪ -‬و سینه را‬ ‫|‬ ‫ء‬ ‫و جوشن ‪ -‬و نامروز چپاردهم است از هر ما‬
11:                                                              ‫‪ -‬بر وزن بوشاك » بمعنی‬          ‫جوشاك‬
12: ‫حو شده مغر = کنابه ازمردم خشمناك‬                                                                 ‫جوشیدن باشد ‪.‬‬
13: ‫وغضب آلود باشد ‪ -‬و مردم هشیار را یز‬                          ‫بره ‪ - 0‬بفتح‌بای ابچد ورای‬            ‫جوش‬
23:                                                                                ‫جوشك ب‬
32:                                                                                     ‫‪ 4‬د‬           ‫جوشن‬
33: ‫جو کات ه باکاف بر وزن کوچك ‪.‬‬                                  ‫باشد بر زره چه زره تمام ازحلقه است وجوشن‬
37:                                                                              ‫(‪ )۱‬چك ‪ :‬جوشن بره ‪.‬‬
46: ‫روز رش ورام وجوش» روژخور وماه و باد‪.‬‬
48:                                                          ‫است‪« .‬تفس؟‪.‬‬        ‫‪ - ۴‬معرب آن حم جوشن‬
50:   ‫‪ - ۱‬افتابیع ‪18‬نا (بوغ گار‬                    ‫‪۰‬‬        ‫‪ ۳۳‬رك‪ :‬جوشر‪‎‬‬    ‫‪o‬‬
59:  ‫‪nidrevhsû‬ز‏ ‪nin .‬‏ ‪hsû‬ز‏ ‪ .‬بلرچی ‪ ( [8206050‬بختن ‪ ۰‬جوشدن » خشمگین شدن )‬
61:   ‫کردن» سر برآوردث کشت ‪ -‬حرارت بخرح دادن ‪« :‬دولت نه بکوشدن است‪ .‬چاره کم جوشیدن‬
```


## [2026-10-17T00:34:54.941Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==59' BQT_v2_pages.txt | sed -n 50,75p; echo; sed -n 1550,1562p BQT_v2_pages.txt"
}
```


### [2026-10-17T00:34:55.361Z] TOOL RESULT

```
   ‫‪ - ۱‬افتابیع ‪18‬نا (بوغ گار‬                    ‫‪۰‬‬        ‫‪ ۳۳‬رك‪ :‬جوشر‪‎‬‬    ‫‪o‬‬


   ‫‪« - ۷‬جوکك‪ .‬فروخ مکایان بود‪.‬‬                       ‫‪.‬‬    ‫آهن) دهوبشمان‪ »: ۳۲‬ورك‪ :‬جع ‪ ۰‬بوغ » جوه‪‎‬‬

                                                                                            ‫متوچهری کوبد ‪:‬‬
               ‫ج وکك با باز کی توالد پرید؟‬                              ‫آهو با شیر کی تواندکوشید؛‬
   ‫« لفت فرس ‪٤*۳‬‏ > رك ‪ :‬جوجه ‪.‬‬
   ‫٭ جودیدن ۔ بفتح پنجم › هندی باستان ‪( 0811501- ,1150-‬آبگوشت) ‪ ,‬کردی‬
  ‫‪nidrevhsû‬ز‏ ‪nin .‬‏ ‪hsû‬ز‏ ‪ .‬بلرچی ‪ ( [8206050‬بختن ‪ ۰‬جوشدن » خشمگین شدن )‬
   ‫* اسشق‪ » :۰۳‬حاصل شدن جرش بواسطهٌ حرارت و باتخمیر و انقلاب ‪ -‬غلیان کردن» فوران‬
   ‫کردن» سر برآوردث کشت ‪ -‬حرارت بخرح دادن ‪« :‬دولت نه بکوشدن است‪ .‬چاره کم جوشیدن‬
                                                                                        ‫>کلتان ‪.» ۳۱۱‬‬
                                                                                                    ‫است «‬


                                                                              ‫‪۴‬‬                  ‫و جز غ‬
  ‫‪٩‬‏ ‪ -‬جت بمعنی‌تقحص و تجسی و همچنین شعبه‌است‬                              ‫‪.‬‬      ‫ن‬
                                                                                  ‫ت‪.‬‬‫ج رك‬
                                                                                       ‫‪۵‬‬
   ‫از فن‌جدل » معرب آن نیزجست است ‪ :‬کان اما مافی فن‌الخلاف خصوصاً الجست وهواول من‌افرده‬
                                      ‫ص‪.» ۶۹‬‬
                                           ‫بالتصنیف ‪ .‬ابن خلکان « دزی ج ‪٩‬‏ ‪۱‬‬
  ‫‪۷‬ق‪-‬ول هرن از ره هندی باستان ‪ ( 125۷, 2 52‬جوشیدن » فوران )»‬     ‫ب‬
   ‫‪ « ۳1/0201562 0۳1602‬اسعق*‪ .»۲4‬برك این اشتقاق‬  ‫‪( # ۵۵‬جوشیدن) ›‬    ‫اوتا ‪-‬‬
            ‫را تپذیرفته آرا از ‪ 2‬للا ‪( ۵‬انداختن) مشتق داند «یبرك ‪ .5۱۱6‬پهلوی ‪1484‬ز‬
                                         ‫با ‪ 780521‬بلوچی ‪( 82211‬فرار کردن) « اسشق *‪.۲4‬‬
      ‫‪- ۸‬اوستا‪( 16۲۱۵۷) ۰ ۰ ۲۳0۵۵۷ -‬جنک کردن)‪ .‬هندی باسان الله‬
                                     ‫طلز ‪ .‬بهلوی ع‪9(1)۵‬ز ‪ « ,‬استق‪٩۱1‬‏ › ‪.‬‬
```


## [2026-10-17T00:35:01.456Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"جنک کردن\")) print NR-1}' BQT_v2_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR==30' BQT_v2_pages.txt | grep -n \"جستن\\|جوی\\|^ *[‫]*[0-9۰-۹]\\{3\\}\" | head -20; awk 'BEGIN{RS=\"\\f\"} NR==30' BQT_v2_pages.txt | head -5"
}
```


### [2026-10-17T00:35:02.079Z] TOOL RESULT

```
29
   ‫جى‬

 ‫جز لگ بنتح اول و انی و سکون‌کاف‪.‬‬                        ‫جزغال؟ س بکراول بروزن امثال‪,‬‬
‫نام علتی ومرضی است که مرغان و پرندکانرا‬                 ‫روی `‬   ‫دلبةً برشته کرد‬   ‫که‬   ‫بمعنی جزغ است‬
                                                                                             ‫آش باشد ‪۴‬‬
```


## [2026-10-17T00:35:06.043Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==30' BQT_v2_pages.txt | grep -n \"جست\\|جنک کردن\\|پهلوی\" | head"
}
```


### [2026-10-17T00:35:06.495Z] TOOL RESULT

```
18:                                                         ‫»ماض‬    ‫عبقتح اول بروزژهمست‬        ‫جست‪°‬‬
22:                                                                         ‫و جستجو کردن و بافتن " ‪۶.‬‬
38:   ‫از فن‌جدل » معرب آن نیزجست است ‪ :‬کان اما مافی فن‌الخلاف خصوصاً الجست وهواول من‌افرده‬
43:            ‫را تپذیرفته آرا از ‪ 2‬للا ‪( ۵‬انداختن) مشتق داند «یبرك ‪ .5۱۱6‬پهلوی ‪1484‬ز‬
45:      ‫‪- ۸‬اوستا‪( 16۲۱۵۷) ۰ ۰ ۲۳0۵۵۷ -‬جنک کردن)‪ .‬هندی باسان الله‬
50:                                                       ‫«سشق ‪. > ۱۲4‬‬  ‫پهلوی )‪54‬ل ا‬
51:   ‫‪ ۵‬جستار ‪ -‬بضم اول » از ‪ :‬جت ‪ ۳‬آر (پسوند ساختن |سم از فعل )؛ بحث ‪ .‬مبحت ‪:‬‬
```


## [2026-10-17T00:35:11.187Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:2457 --image 2>&1 | head -120"
}
```


### [2026-10-17T00:35:18.536Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 540; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2457.png
REF: BQT:2457  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 540  OCR-lang: fas

۷0۷ یوسف روز
وجوینده وطلب کننده باشد۱ - ونام جانوری‌هم | شبیه به‌پلنگهه - ومعنی فلطیدن ومراغه کردن
هست شکاری کوچکتر ازیلنگه؟ - وسکه وله | جانوران هم هت - و اسکه تولهٌ شکاربرا نیز
شکاریرا نیز کویند که كبك وتیهو ودراج وامثال کوبند۷ 4.
آنرا بقوت خامه وبو پیداکند وازسوراخ وتراك وه - بروزن‌موژه. بمعنی بوزد‌است
سنگه وبوتةٌ خار بر میآوردگ۴ - و بمعنی جست | که سکه تولهٌ شکاری۸ - وفلطیدن جانوران ور
وخیز هم بنظر آمده است۴ . خاك باشد ‎٩‏ - و لام گدایی بوده است در لهایت

بوزلد « بفتح زای نقطه دار بر وزن ایرام وس..اجت*۱- وتنهٌ درخت را نیز کوبند۱۹.
خوبك(۱) » مصفر بوز است وآن جالوری باشد یو سف‌رو رز کنایه‌ا زآفتاب‌عالمتاست.
(69) چك, چش: چوبك. سس
۱ - مخفف «یوزنده» درتر کیبات : « ره‌یوز ورزم بوز» رك: حاشيهٌ قبل. ورك: فهرست
ولف: رزم بوز . ۲ - «بوز اسم فارسی فهداست وبت ر کی پاری بامند» حیوالی است مانند
پلنگه واو را رام نموده مانند سکان شکاری صیدوحوش باومیکنند.» «تحفةٌ حکیم مومن» و آرا
پوزپلنگه کویند. فس: اوستا - 7802 78028111 (حر کت کردن؛ سفر کردن)؛ کردی ع تالا

(سکه شکاری ) » ارمنی ع ‎)٩(‏ ۰90۷22 78۷22 «اسشق ۰۹۱۱۲۹

۴ * بوز4 * پوزه . ر4: ح ۱ ۴ - «جتن» (بم اول) را درمآخذی نظیر

لفت فری اسدی (رك : ح٩‏ صفحهٌ قبل ) جستن ( بفتح اول) خوانده‌اند (۱)

- از: بوز (ح۲) 4-۳ (پسوند تسفیر). کردی 866 (بوز) « ژاباس۲۹.
‎٩‏ - «یوزك ویوزه, مراغه وغلطیدن جاتوران باشد درخا4.» «جهانگیری».
۷ <بوزه * بوز. ر4: ح۲ . ۸ -« بوز * بوزك :

طمن نآدان صیحت داناست زدن بوزه عبرت بوزاست.

سعدی «رشیدی» .
‎٩‏ - ر4: یوزك (ح ‎)٩‏ ۰ *- ازین ببت سنائی غزدوی اسّتتباط کرده اند :
رشیدی گوید: * وازین بت سنائی بمعنی کدا لاهن میشود :

از پی آب و لان هن روزه طوف هر بوزه بر دربوزه.

لیکن سکه توله لیز توان کفت ؟* ۱ رشیدی بنقل ازسامی بمعنی ساق درخت آورده ۰

درسامی آمده (چاپ تهران‌م۱۳) : «الساق بوزة درخت.» بنابرین بوژه باین‌معنی مصحف«بوزه»

(و.م ) است .

0 بوزپلنگ - رك : ح۲ همین‌سفحه.

زیرا ره توز ورزم‌توز و کین‌نوز آمده, ولی ره بوز ورزم بوز دیده شده‌است » وقافيةٌ شمرفردوسی

نیز شاید «رزم سوز» باشد وبا قافیةٌ اول چیزدیگر وثانی «رزم توز» است. » اولا مرحوم بهار سند

استعمال «ره توز» رانداده‌اند. ایا امتعمال سه تن کیب مزبور با تاو مانع استعمال آ نپاپا پاء نیست.

(رك : فهرست ولف : رزم پوز) نالا درصحاح الفری (سخ طاعتی و دهشدا) که علاوه بر مرامات

حرف آخره «راعات حرف اولعم شده» «بوز» درین‌مورد بین «پاز» وباب «ژی» آمده. رایماً ولف

درفهرست شاهنامهٌ خود بنقل ازفرهنکه عبدالقادر « رزم پوز » را ضبط کرده . خاماً «چاه پوز»

برظرسي آمده (ر3: چاه پوز! ) , ماما بوز در زبانهای قدیم ربشه بارد. ر3: ح۸ (همین‌سفحه),
```


## [2026-10-17T00:35:26.990Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in جوشیدن یوز یوزیدن جستن آنزیم; do python3 tools/fetch_source.py \"https://vajehyab.com/moein/$w\" --note \"page 566, Yeu 3: Mo'in entry $w\"; done"
}
```


### [2026-10-17T00:35:29.336Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0d7a8034af183a00.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/48c4b6c9abf6069e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/71f9501094108728.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d4e24bce6c0cfc80.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8816cb3b12f03c29.txt
```


## [2026-10-17T00:35:34.859Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 0d7a8034af183a00 48c4b6c9abf6069e 71f9501094108728 d4e24bce6c0cfc80 8816cb3b12f03c29; do echo \"## $f\"; head -3 $f.txt | sed -n 3p; grep -n \"معین\" -A3 $f.txt | head -14; done"
}
```


### [2026-10-17T00:35:35.168Z] TOOL RESULT

```
## 0d7a8034af183a00
STATUS: 200
4:TITLE: معنی جوشیدن | فرهنگ انتشارات معین | واژه یاب
5-
6:معنی جوشیدن | فرهنگ انتشارات معین | واژه یاب 
7-
8- 26 فرهنگ 
9-
--
16: فرهنگ انتشارات معین
17- (دَ) (مص ل .) 1 - به جوشش آمدن . 2 - فوران کردن آب از زمین . 
18- جوشیدن در فرهنگ‌های دیگر
19- معنی جوشیدن در لغت‌نامه دهخدا 
## 48c4b6c9abf6069e
STATUS: 200
4:TITLE: معنی یوز | فرهنگ انتشارات معین | واژه یاب
5-
6:معنی یوز | فرهنگ انتشارات معین | واژه یاب 
7-
8- 26 فرهنگ 
9-
--
16: فرهنگ انتشارات معین
17- (اِ.) حیوانی است درنده شبیه پلنگ اما کوچکتر از آن که در قدیم آن را برای شکار تربیت می کردند.
18- یوز در فرهنگ‌های دیگر
19- معنی یوز در لغت‌نامه دهخدا 
## 71f9501094108728
STATUS: 200
4:TITLE: معنی یوزیدن | فرهنگ انتشارات معین | واژه یاب
5-
6:معنی یوزیدن | فرهنگ انتشارات معین | واژه یاب 
7-
8- 26 فرهنگ 
9-
--
16: فرهنگ انتشارات معین
17- (دَ) (مص ل .) جُستن ، جستجو کردن .
18- یوزیدن در فرهنگ‌های دیگر
19- معنی یوزیدن در لغت‌نامه دهخدا 
## d4e24bce6c0cfc80
STATUS: 200
4:TITLE: معنی جستن | فرهنگ انتشارات معین | واژه یاب
5-
6:معنی جستن | فرهنگ انتشارات معین | واژه یاب 
7-
8- 26 فرهنگ 
9-
--
16: فرهنگ انتشارات معین
17- (جُ تَ) (مص م .) 1 - طلب کردن . 2 - جستجو کردن . 3 - یافتن .
18- جستن در فرهنگ‌های دیگر
19- معنی جستن در لغت‌نامه دهخدا 
## 8816cb3b12f03c29
STATUS: 200
4:TITLE: معنی آنزیم | فرهنگ انتشارات معین | واژه یاب
5-
6:معنی آنزیم | فرهنگ انتشارات معین | واژه یاب 
7-
8- 26 فرهنگ 
9-
--
16: فرهنگ انتشارات معین
17- [ فر. ] (اِ.) گروهی از پروتئین های کاتالیزی که یاخته های زنده آن ها را تولید می کنند و حد واسط فرایندهای شیمیایی حیات هستند، زی مایه . (فره .) 
18- آنزیم در فرهنگ‌های دیگر
19- معنی آنزیم در فرهنگ فارسی عمید / قربان‌زاده
```


## [2026-10-17T00:35:39.691Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py \"https://vajehyab.com/amid/آنزیم\" --note \"page 566, Yeu 3: Amid entry anzim (AMD:57)\"; f=$(python3 -c \"import hashlib;print(hashlib.sha1('https://vajehyab.com/amid/آنزیم'.encode()).hexdigest()[:16])\"); grep -n \"عمید\" -A3 data/verification/sources/web/$f.txt | head -10"
}
```


### [2026-10-17T00:35:40.486Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/78042d9aa891ea0f.txt
4:TITLE: معنی آنزیم | فرهنگ فارسی عمید / قربان‌زاده | واژه یاب
5-
6:معنی آنزیم | فرهنگ فارسی عمید / قربان‌زاده | واژه یاب 
7-
8- 26 فرهنگ 
9-
--
18: فرهنگ فارسی عمید / قربان‌زاده
19- مادۀ آلی که توسط سلول‌های بدن ساخته و ترشح می‌شود و سبب تسریع فعل و انفعال شیمیایی مواد می‌شود.
20- آنزیم در فرهنگ‌های دیگر
```


## [2026-10-17T00:35:46.984Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=427 && NR<=431 {print \"### leaf \" NR-1; print}' KLN_1966.txt | grep -n \"^###\\|^[a-z]\\{3,\\}, \\|yeudh\\|ieudh\\|iudh\\|yudh\" | head -40"
}
```


### [2026-10-17T00:35:47.355Z] TOOL RESULT

```
1:### leaf 426
2:nquiet,  hostile’, lit.  ‘seized’,  rel.  to  manifestus,  ‘evident’,  lit.  ‘that which  can  be  seized  by  the  hand’,  and  prob. cogn.  with  OI.  dharsati,  ‘dares’,  Gk.  ffdpoo?, ffpdcro?,  ‘courage,  audacity’,  OE.  ic  dearr,  ‘I dare’.  See  dare  and  words  there  referred  to  and cp.  esp.  manifest.
3:infestation,  n.  —  Late  L.  infestdtio,  gen.  -onis, ‘a  troubling,  disturbing,  molesting’,  fr.  L.  in- festatus,  pp.  of  infestare.  See  infest  and  -ation. infeudation,  n.,  enfeoffment  {Engl.  law).  —  ML, infeudado,  gen.  -onis,  fr.  infeuddtus,  pp.  of  in- feudare,  ‘to  enfeoff’.  See  in-,  ‘in’,  feud,  ‘fief’,  and -ation.
4:infibulate,  tr.  v.,  to  fasten,  buckle  (esp.  the  sexual organs).  —  L.  infibulatus,  pp.  of  infibulare,  ‘to close  with  a  clasp’,  fr.  in-,  ‘in’,  and  fibula,  ‘clasp, buckle,  brooch’.  See  fibula  and  verbal  suff.  -ate. Derivative:  infibulat-ion,  n.
6:infidelity,  n.  —  F.  infidelite,  fr.  L.  infidelitatem, acc.  of  infidelitas,  ‘faithlessness’,  fr.  infidelis.  See prec.  word  and  -ity.
7:infinite,  adj.  —  L.  infinitus,  ‘boundless,  unlimited, endless’,  fr.  in-,  ‘not’,  and  finitus,  pp.  of  finire. See  finite.  Derivatives:  infinite,  n.,  infinite-ly, adv.,  infinite-ness,  n.
8:infinitesimal,  adj.,  immeasurably  small.  — Formed  with  adj.  suff.  -al  fr.  ModL.  infinitesi- mus,  which  was  coined  by  the  German  philos¬ opher  and  mathematician  Baron  Gottfried Wilhelm  von  Leibniz  (1646-1716)  fr.  L.  infinitus (see  prec.  word)  on  analogy  of  L.  centesimus , ‘the  hundredth’.
11:infinitude,  n.,  the  state  of  being  infinite.  —  Coined by  Milton  fr.  infinite  and  suff.  -ude. infinity,  n.  —  ME.  infinite,  fr.  OF.  infinite  (F.  in¬ finite),  fr.  L.  infinitatem,  acc.  of  infinitas, ‘boundlessness,  endlessness’.  See  infinite  and -ity.  L.  infinitas  is  prop,  a  loan  translation  of  Gk. arceipia,  ‘infinity’,  fr.  Sireipoi;,  ‘endless,  infinite’, infirm,  adj.  —  ME.  infirme,  fr.  L.  infirmus,  ‘weak, feeble,  infirm,  sick’,  fr.  in-,  ‘not’,  and  firmus, ‘strong,  firm’.  See  firm,  adj.
15:inflammable,  adj.  —  F.,  fr.  L.  inflammare.  See inflame  and  -able.
17:inflammatory,  adj.  —  Formed  with  adj.  suff.  -ory fr.  L.  inflammatus,  pp.  of  inflammare.  See  in¬ flame  and  cp.  F.  inflammatoire.
19:inflation,  n.  — -  L.  inflatio,  gen.  -onis,  ‘a  blowing or  puffing  up,  inflation’,  fr.  inflatus,  pp.  of  in- flare.  See  prec.  word  and  -ion.
21:inflect,  tr.  v.  —  L.  infledere  (pp.  inflexus),  ‘to bend,  curve;  to  change,  alter,  modulate’,  fr. in-,  ‘in’,  and  fledere ,  ‘to  bend’.  See  flex  and  cp. words  there  referred  to.
24:inflexible,  adj.  —  L.  inflexibilis,  ‘inflexible’,  fr. inflexus,  pp.  of  inflectere.  See  inflect  and  -ible. Derivatives:  inflexibil-ity,  n.,  inflexible-ness,  n., inflexibl-y,  adv.
25:inflict,  tr.  v.  —  L.  inflictus,  pp.  of  infligere,  ‘to strike  or  dash  against’,  fr.  in-,  ‘in',  and  fligere (pp.  flictus),  ‘to  strike’.  See  afflict  and  cp.  words there  referred  to.  Derivatives:  inflict-er,  n., infliction  (q.v.),  inflict-ive,  adj.
26:infliction,  n.  —  Late  L.  inflictio,  gen.  -onis,  ‘an inflicting’,  fr.  L.  inflictus,  pp.  of  infligere,  ‘to strike  or  dash  against’.  See  prec.  word  and  -ion. inflorescence,  n.,  1)  a  flowering;  2)  arrangement of  flowers  on  an  axis  (hot.)  —  ModL.  in- fldrescenda,  fr.  Late  L.  infldrescens,  gem  -ends. pres.  part,  of  inflorescere,  ‘to  begin  to  blossom, to  put  forth  blossoms’,  fr.  in-,  ‘in’,  and  L.  flore- scere,  ‘to  begin  to  blossom’.  See  florescence, inflorescent,  adj.,  flowering.  —  Late  L.  infldre¬ scens,  gen.  -ends.  See  prec.  word, inflow,  n.  —  Formed  fr.  in-,  ‘in’,  and  flow. Derivatives:  inflow-ing,  adj.  and  n. influence,  n.  —  F.,  fr.  Late  L.  influent ia,  ‘a  flowing in’,  fr.  L.  influens,  gen.  -ends.  See  influent  and -ce  and  cp.  influenza.  Derivative :  influence,  tr.  v. influent,  adj.,  flowing  in;  n.,  a  tributary  stream, —  L.  influens,  gen.  -ends,  pres.  part,  of  influere, ‘to  flow  in’,  fr.  in-,  ‘in’,  and  fluere,  ‘to  flow’. See  fluent.
27:influential,  adj.  —  Formed  with  adj.  suff.  -al  fr. Late  L.  influentia.  See  influence.
30:influxion,  n.  —  Late  L.  influxio,  gen.  -dnis,  ‘a flowing  in’,  fr.  L.  influx-(um),  pp.  stem  of  in¬ fluere.  See  prec.  word  and  -ion. inform,  adj.,  without  form,  shapeless.  —  F.  in¬ forme,  fr.  L.  informis,  ‘unformed,  shapeless’,  fr. in-,  ‘not’,  and  forma,  ‘form,  shape’.  See  form,  n. inform,  tr.  and  intr.  v.,  to  apprise,  notify.  — ME.  enformen,  fr.  OF.  enformer  (F.  informer), fr.  L.  informare,  ‘to  give  form  to,  to  shape’,  fr. in-,  ‘in’,  and  formare,  ‘to  form,  shape’.  See form,  v.
33:infra,  adv.,  under,  below.  —  L.  infra,  ‘below (adv.);  below  (prep.),  under’,  fr.  I.-E.  *gdher-.
41:infrequency,  infrequence,  n.  —  L.  infrequentia, ‘scantiness’,  fr.  infrequens,  gen.  -entis.  See  next word  and  -cy,  resp.  -ce.
42:infrequent,  adj.  —  L.  infrequens,  gen.  -entis,  ‘oc¬ curring  seldom,  unusual,  uncommon,  not  fre¬ quent’,  fr.  in-,  ‘not’,  and  frequens,  gen.  -entis.
48:### leaf 427
49:uriate,  ‘to  madden’,  fr.  L. in  furid,  ‘in  a  fury’,  fr.  in  (see  in-,  ‘in’)  and  abl. of  furia  (see  fury).  For  the  ending  see  adj.  suff. -ate.
60:ingenerate,  tr.  v.,  to  generate  within,  to  engender. —  L.  ingeneratus,  pp.  of  ingenerate,  ‘to  en¬ gender,  produce’,  fr.  in-,  ‘in’,  and  generare.  See generate  and  cp,  engender, ingenious,  adj.,  clever.  —  F.  ingenieux  (fern,  in- genieuse),  ‘ingenious,  clever’,  fr.  L.  ingeniosus, ‘intellectual,  clever’,  fr.  ingenium,  ‘nature;  dis¬ position’,  lit.  ‘that  which  is  inborn’,  fr.  in-,  ‘in’, and  I.-E.  base  *gen-,  ‘to  beget,  bear,  bring  forth, produce’.  See  genus  and  -ous  and  cp.  engine. Derivatives:  ingenious-ly,  adv.,  ingenious-ness, n. ingteue,  n.,  an  artless,  naive  girl.  —  F.,  fem.  of ingenu,  ‘ingenuous,  artless,  simple’,  fr.  L.  in- genuus.  See  ingenuous.
62:ingenuity,  n.,  ingeniousness.  —  L.  ingenuitas  (gen. -tatis),  ‘frankness,  nobility’,  fr.  ingenuus;  see next  word  and  -ity.  The  English  meaning  of  the word  is  due  to  a  confusion  with  ingenious. ingenuous,  adj.  —  L.  ingenuus,  ‘native;  freeborn, noble;  upright’,  fr.  in-,  ‘in’,  and  I.-E.  base  *gen-, ‘to  beget,  bear,  bring  forth,  produce’.  See  genus and  cp.  ingenue.  For  E.  -ous,  as  equivalent  to L.  -us,  see  suff.  -ous.
64:ingest,  tr.  v.,  to  take  into  the  body.  —  L.  in- gestus,  pp.  of  ingerere,  ‘to  bring  in,  carry  in’, fr.  in-,  ‘in’,  and  gerere,  ‘to  carry’.  See  gerent  and cp.  words  there  referred  to.
66:ingle,  n.,  fire ;  fireplace.  —  Scot.,  fr.  Gael,  aingeal, ‘fire’,  which  is  of  uncertain  origin, inglorious,  adj.  —  L.  ingloriosus,  ‘inglorious’,  fr. in-,  ‘not’,  and  gloriosus.  See  glorious. Derivatives :  inglorious-ly,  adv.,ingIorious-ness,n. ingluvies,  n.,  the  crop  (zool.)  —  L.  ingluvies,  ‘crop, maw’,  which  stands  for  in-gluv-ies,  fr.  in-,  ‘in’, and  I.-E.  base  *glu-,  ‘to  swallow’,  whence  also L.  gluttire,  ‘to  swallow,  gulp  down’.  See  glut and  cp.  words  there  referred  to. ingot,  n.,  a  mass  of  unwrought  metal.  —  ME., fr.  OE.  in  (see  in-,  ‘in’)  and  goten,  pp.  of  geotan, ‘to  pour’.  See  found,  ‘to  cast’,  and  cp.  lingot. ingrain,  tr.  v.,  1)  to  dye  in  grain;  2)  to  work  into the  texture.  —  See  engrain.
69:ingravescence,  n.  —  Formed  from  next  word  with suff.  -ce.
70:ingravescent,  adj.,  gradually  increasing  in  gravity. —  L.  ingravescens,  gen.  -entis,  pres.  part,  of  in- graviscere,  ‘to  grow  worse’,  fr.  in-,  ‘in’,  and gravescere,  ‘to  become  burdened,  grow  worse’.
72:ingredient,  n.,  that  which  enters  into  a  mixture; component.  —  L.  ingrediens,  gen.  -entis,  pres, part,  of  ingredi,  ‘to  go  into,  to  enter’,  fr.  in-, ‘in’,  and  gradi,  ‘to  step,  walk,  go’,  fr.  'gradus, ‘step’.  See  grade  and  -ent. ingress,  n.,  entrance.  —  L.  ingressus,  gen.  -us, ‘way  in,  entrance’,  fr.  ingressus,  pp.  of  ingredi. See  prec.  word.
74:ingression,  n.,  the  act  of  entering.  —  L.  ingressio, gen.  -onis,  ‘a  going  into’,  fr.  ingressus,  pp.  of ingredi.  See  prec.  word  and  -ion. inguen,  n.,  the  groin  (anat.)  —  L.,  ‘groin,  ab¬ domen’,  fr.  I.-E.  *i}gwen,  whence  also  Gk.  aSfjv, ‘gland’ ;  cogn.  with  ON.  dkkr,  ‘a  swelling’,  ok- kvinn,  ‘swollen’.  Cp.  adcno-. inguinal,  adj.  —  Medical  L.  inguindlis,  ‘of  the groin’,  fr.  L.  inguen,  gen.  -inis.  See  prec.  word and  adj.  suff.  -al.
76:ingurgitate,  tr.  v.,  to  swallow  greedily.  —  L.  in¬ gurgitates,  pp.  of  ingurgitare,  ‘to  pour  in  like  a flood;  to  flood,  fill’,  fr.  in-,  ‘in’,  and  gurges,  gen. gurgitis,  ‘whirlpool,  gulf’.  See  gurgitation  and cp.  words  there  referred  to. ingurgitation,  n.  —  L.  ingurgitatid,  gen.  -onis, ‘immoderate  eating  and  drinking’,  fr.  ingurgi- tatus,  pp.  of  ingurgitare.  See  prec.  word  and -ion.
77:inhabit,  tr.  v.  —  ME.  enhabiten,  fr.  OF.  enhabiter, fr.  L.  inhabitare,  ‘to  dwell  in’,  fr.  in-,  ‘in’,  and habitare,  ‘to  dwell’.  See  habit,  ‘to  dwell’. Derivatives:  inhabit-able,  adj.,  inhabitancy,  in¬ habitant,  inhabitation  (qq.v.) inhabitancy,  n.  — -  Formed  from  next  word  with suff.  -cy.
78:inhabitant,  n.  —  ME.  inhabitaunt ,  fr.  AF.  (=  OF.) enhabitant  (=  pres.  part,  of  enhabiter),  fr.  L. inhabitantem,  acc.  of  inhabitans,  pres.  part,  of inhabitare.  See  inhabit  and  -ant  and  cp.  habit¬ ant.
79:inhabitation,  n.,  the  act  of  inhabiting;  the  state of  being  inhabited.  —  Late  L.  inhabitatio,  gen. -onis,  ‘a  dwelling,  habitation’,  fr.  L.  inhabitatus, pp.  of  inhabitare.  See  inhabit  and  -ation. inhalation,  n.  —  Formed  with  suff.  -ion  fr.  L.  in- halatus,  pp.  of  inhalare.  See  next  word, inhale,  tr.  v.,  to  breathe  in;  intr.  v.,  to  inhale  air. —  L.  inhalare,  ‘to  breathe  upon’,  fr.  in-,  ‘in’, and  halare,  ‘to  breathe’.  See  exhale, inhere,  intr.  v.,  to  be  an  essential  part;  to  be  in¬ nate.  —  L.  inhaerere,  ‘to  cling  or  cleave  to,  be closely  connected  with,  inhere  in’,  fr.  in-,  ‘in’, and  haerere,  ‘to  stick,  cling,  hang,  adhere’.  See hesitate  and  cp.  adhere,  cohere, inherence,  inherency,  n.  —  Formed  from  next word  with  suff.  -ce,  resp.  -cy.
82:inherent,  adj.,  essential,  innate.  —  L.  inhaerens, gen.  -entis,  pres.  part,  of  inhaerere.  See  inhere and  -ent.
86:inhibition,  n.  —  OF.  inibicion,  inhibicion  (F.  in¬ hibition ),  fr.  L.  inhibitidnem ,  acc.  of  inhibitid,  ‘a restraining’,  fr.  inhibitus ,  pp.  of  inhibere.  See prec.  word  and  -ion.
88:### leaf 428
89:ory,  adj,  —  ML.  inhibitorius,  fr.  L.  in¬ hibitus,  pp.  of  inhibere.  See  inhibit  and  adj. suff.  -ory.
90:inhospitable,  adj.  —  OF.,  fr.  ML.  inhospitabilis (corresponding  to  L.  inhospitalis),  ‘inhospi¬ table’,  fr.  in-,  ‘not’,  and  ML.  hospitdbilis.  See
93:inhospitality,  n.  —  F.  inhospitable,  fr.  L.  in- hospitalitatem,  acc.  of  inhospitalitas,  ‘inhospi¬ tality’,  fr.  in-,  ‘not’,  and  hospitdlis,  ‘hospitable’. See  hospitality.
```


## [2026-10-17T00:35:54.090Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='ignore').read()\nleaves=t.split('\\f')\nfor pat in [r'(?m)(^|\\s)jussive,', r'(?m)(^|\\s)juice,\\s+n', r'(?m)(^|\\s)enzyme,\\s+n', r'(?m)(^|\\s)zymo-', r'(?m)(^|\\s)jubilant,',r'(?m)(^|\\s)joust,',r'yeudh|ieudh|\\*ieu-dh|\\*yeu-dh']:\n    for i,l in enumerate(leaves):\n        for m in re.finditer(pat,l):\n            print(pat,'leaf',i,'|',l[m.start():m.start()+600].replace('\\n',' '));print()\n            break\nEOF"
}
```


### [2026-10-17T00:35:58.143Z] TOOL RESULT

```
(?m)(^|\s)jussive, leaf 451 |  jussive,  adj.,  expressing  command.  —  Formed with  sutf.  -ive  fr.  L.  jussus.  pp.  of  inhere,  ‘to  bid. command’.  See  jube. Derivative:  jussive,  n.,  a  word  or  form  expres¬ sing  command. just,  adj.  —  ME.  just,  juste,  fr.  F.  juste,  fr.  L. justus,  ‘just,  right,  upright,  fair,  equitable’,  fr. jus,  ‘right,  law’.  See  jus  and  cp.  justice.  Cp.  also Justin,  Justina,  Justus,  adjust  and  the  first  ele¬ ment  in  juste-milieu. Derivatives:  just,  adv.,  just-ly,  adv.,  just-ness,  n. just,  v.  —  See  joust. juste-milieu,  n.,  the  golden  mean.  —  

(?m)(^|\s)juice,\s+n leaf 450 |  juice,  n.  —  ME.  jure,  juse,  fr.  MF.  (=  F.)  jus, fr.  L.  jus,  ‘broth,  soup’,  fr.  I.-E.  base  *yus-, whence  also  OL  yuy-,  ‘broth  ,  OSlav.,  Pol.,  etc., jucha,  ‘broth,  soup’,  OPruss.  iuse,  ‘broth,  soup’. Lith.  juie,  ‘fish  soup’,  Gk.  ‘leaven’  (G. Jauche,  ‘liquid  manure’,  is  a  loan  word  fr.  Pol. jucha),  ON.  ostr,  ‘cheese’.  Cp.  verjuice.  Cp.  also zyme.  Base  yus-  is  an  enlargement  of  base  *yeu-, ‘to  mix’,  which  represents  properly  a  special  use of  base  *yeu-,  ‘to  join,  unite’:  see  join  and  cp. jube. Derivatives:  juice-less,  

(?m)(^|\s)enzyme,\s+n leaf 287 |  enzyme,  n.,  a  chemical  ferment  ( biochem .)  — G.  Enzym,  coined  by  the  German  physiologist Wilhelm  Kiitme  (1837-1900)  in  1878  fr.  MGk. £v£i3|io<;,  ‘leavened’,  fr.  Gk.  h  (see  2nd  en-)  and ‘leaven’.  See  zymosis. Derivatives:  enzym-atic,  enzym-ic,  adjs. eo-,  combining  form  meaning  ‘dawn’.  • —  Gk. 7)<o-,  fr.  ‘dawn’,  which  stands  for  *ausos and  is  cogn.  with  OE.  east,  ‘in  the  east’.  See east  and  cp.  words  there  referred  to. eoan,  adj.,  pertaining  to  the  dawn.  —  Formed with  suff.  -an  fr.  L.  edits,  fr.  Gk.  7)6105,  ‘of  the dawn

(?m)(^|\s)jubilant, leaf 450 |  jubilant,  adj.  —  L .jubilans,  gen.  -antis,  pres.  part, of  jubilare.  See  next  word  and  -ant. Derivative :  jubilant-ly,  adv. jubilate,  intr.  v.,  to  exult.  —  Fr.  L.  jubilat-(um), pp.  stem  of  jubilare,  ‘to  shout  for  joy  (whence prop, — through  back  formation — jubilum,  ‘wild cry,  shout  of  joy’),  fr.  I.-E.  *yu-dhe-los,  lit.  one jubilate who  makes  yu',  compounded  of  the  imitative base  *yU -,  ‘to  shout  for  joy,  shout’,  and  base *dhe-,  ‘to  place,  make,  do’.  The  first  element appears  also  in  Gk.  Myt],  ‘outcry’,  !ov|coc;, ‘shout  of  

(?m)(^|\s)joust, leaf 25 |  joust,  v.,  and  cp.  juxta-. Derivatives:  adjust-able,  adj.,  adjust-er,  n.,  ad- just-ive,  adj.,  adjust-ment,  n. adjutancy,  n.  — •  Formed  fr.  next  word  with suff.  -cy. adjutant,  n.,  1)  an  officer  appointed  to  assist  a commanding  officer;  2)  a  large  stork  found  in East  India.  —  L.  adjutans,  gen.  -antis,  pres.  part, of  adjutdre,  ‘to  help,  assist’,  freq.  of  adjiivdre (pp.  adjutus).  See  next  word  and  -ant. adjutory,  adj.  and  n.,  helpful.  —  L.  adjutdrius, ‘helping,  helpful',  fr.  adjutus,  pp.  of  adjiivdre, ‘to  help,  assist’.  See  

(?m)(^|\s)joust, leaf 449 |  joust, Jugatinus,  jugular,  jugulate,  junction,  juncture, junta,  junto,  juxta-,  rejoin,  rejoinder,  subjoin, subjugate,  subjunctive,  and  the  second  element in  quadriga.  For  a  special  jse  of  base  *yeu-  in the  sense  ‘to  mix’,  see  juice  and  cp.  jube. Derivatives:  join-ing,  verbal  n.,  and  adj.,  join¬ ing -ly,  adv. joinder,  n.,  the  act  of  joining  (taw).  —  F.  joindre, ‘to  join’  (fr.  L.  jungere),  used  as  a  noun;  see join.  For  the  subst.  use  of  infinitives  in  law terms  see  attainder.  Cp.  rejoinder, joiner,  n.  ME.  joynour,  fr.  OF. 

(?m)(^|\s)joust, leaf 452 |  joust, adjust. juxtapose,  tr.  v.,  to  place  side  by  side.  —  Formed fr.  juxta-  and  pose,  ‘to  place’.  i juxtaposition,  n.  —  F.,  formed  fr.  juxta-  and position. juzail,  n.  —  A  var.  of  jezail.  I jynx,  n.,  i)  the  wryneck;  2)  a  charm  (from  the  use of  this  bird  in  witchcraft).  —  ModL.  jynx  (pi.  j jynges),  fr.  L.  iynx,  fr.  Gk.  EuyE  (gen.  Eoyyo?), ‘the  wryneck’.  Some  philologists  derive  toy!;  fr- iut^eiv,  ‘to  shout,  yell’,  so  that  Euy5  would  lit. mean  ‘the  shouting  bird’  (see  jubilate).  Accord¬ ing  to  others,  toy?  is  a  wo

yeudh|ieudh|\*ieu-dh|\*yeu-dh leaf 450 | yeudh-,  whence also  OI.  yodhayati,  ‘involves  in  a  fight’,  yudh-, ‘fight’,  yudhmah,  ‘warlike,  warrior’,  Avestic yuidyeinti,  ‘they  fight’,  yaoshti -, ‘activity,  agility’. Arm.  yuzem,  ‘I  stir  up’,  Gk.  uafxtvy]  (for  *yudh- s-mine),  ‘battle’  (prop,  ‘turmoil’),  Lith.  judit, judeti,  ‘to  move  trembling,  to  quarrel’,  L.juba, ‘mane’,  lit.  ‘that  which  waves,  flutters’.  All  these words  derive  fr.  I.-E.  base  *yeu-dh-,  "to  be moved,  to  be  shaken’,  which  seems  to  be  a dental  enlargement  of  base  *yeu-,  ‘to  mix,  stir’. The  rood  loft  is  called
```


## [2026-10-17T00:36:10.090Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^yeu\\|^yewə\\|^yeuə\\|^yeug\\|^yeudh\\|^yes-\" AHD_watkins1985.txt | head; "
}
```


### [2026-10-17T00:36:10.596Z] TOOL RESULT

```
1193:yes-. To boil, foam, bubble. 1. Germanic *jest- in Old English gist, yeast: YEAST. 2. Greek zeein, zein, to boil: ECZEMA, ZEOLITE. [Pok. jes- 506.]
1195:yeu-. Vital force, youthful vigor. Earliest form *ayeu-; variant of aiw-. Suffixed zero-grade form *yuwen- (< *yu-sen-), “possessing youthful vigor,” young. 1. Further suffixed form *yuwn-ti- in Germanic *jugunthi-, *jugun- tha- in Old English geoguth, youth: YOUTH. 2. Further suffixed form *yuwn-ko- in: a. Germanic *juwungaz becoming *jungaz in (i) Old English geong, young: YOUNG (ii) Old High German jung, young: JUNKER (iii) compound *jung-fréw6-, young lady (see per’); b. Old Irish 6ac, Irish Gaelic 6g, in oglach, soldier: GALLOW- GLASS. 3. Latin iuvenis, young: JUNIOR, JUVENILE; JUVE- NOCRACY, REJUVENATE. [Pok. 3. ieu- 510.]
1196:yeudh-. To move violently, fight. Zero-grade form *yudh-é- in Latin jubére, to command (< “to set in motion”): JUSSIVE. [Pok. ieu-dh- 511.]
1197:yeue-. To blend, mix food. Zero-grade form *yii- (< *yua-) in: a. Suffixed form *yi-s- in Latin jis, juice, broth: JUICE; b. suffixed form “yiis-md in Greek zumé, leaven: -ZYME, ZYMO-; ENZYME. [Pok. 1. iew- 507.]
1198:yeug-. To join. I. Zero-grade form *yug-. 1. Suffixed form *yug-o- in: a. Germanic *yukam in Old English geoc, yoke: YOKE; b. Latin jugum, yoke: JUGATE, JUGULAR, JUGUM; CONJUGATE, SUBJUGATE; C. Greek zugon, yoke, and zugoun, to join: ZYGO-, ZYGOMA, -ZYGOUS; (AZY- GOUS), SYZYGY; d. Sanskrit yugam, yoke: YuGA. 2. Suf- fixed (superlative) form *yug-istos in Latin *jugistd (vid), “on a nearby (road),” contracted to juxtd, close by: JOUST; ADJUST, JUXTAPOSE, (JUXTAPOSITION). 3. Nasal- ized form *yu-n-g- in Latin jungere, to join: JOIN, JUNC- TION, JUNCTURE, JUNTA; ADJOIN, CONJOIN, (CONJUGAL), (CONJUNCT), ENJOIN, INJUNCTION, SUBJOIN. II. Suffixed form *yeug-mn in Greek zeugma, a bond: ZEUGMA. III. Suffixed o-grade form *youg-o- in Sanskrit yogah, union: YoGA. [Pok. 2. ieu- 508.]
```


## [2026-10-17T00:36:26.867Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=236 && NR<=240 {print \"### leaf \" NR-1; print}' IEC.txt | grep -n \"^###\\|^i[eo]u\\|^i[ūu]\\|ieudh\\|ieuk\\|ieug\\|yaoz\\|yaož\\|yuzem\\|Ar. yaoz\" | head -30; grep -n \"^i[eo]u[a-z̯ʷh-]*[ -]\\|^ieu\\|^jeu\" IEC.txt | head -30"
}
```


### [2026-10-17T00:36:27.202Z] TOOL RESULT

```
1:### leaf 235
38:### leaf 236
65:### leaf 237
97:### leaf 238
129:### leaf 239
6400:ieu (ieu-ge, ieu-ghi, ieu-que, ieuo) “now, al- ready, then’. WP I, 101 Skt. cf. u, ü, encl. & procl. ‘whence, since, ag: Av. yava ‘ever, as, so long as’; Per. juz “beside, except ($-); Gk. eü-te ‘then, since, as’: LLat. cf. jū-ge (continuously, whence jügis, adj. cf. Av. yavaetat ‘duration’ and Per. javid *eternal) (£-); Go. OHG ju, OHG also jū ‘already’; be- side OHG joh ‘yet, also, and, or’; Go. cf. ju- ni ‘no longer’; OE geo “already, formerly”; Icel. jú (yes! after a negation); OCS ju-Ze, u, u-Ze “already”; Li. jaŭ, d: Latv. jau, id.; Finn. LW jo, jo-ko, id.
6402:ieudhos (ioudhos, us) “stir, movement, dash, gait; moving', etc. WP I, 203 cf. iudh-, ioudh- and ieudhó above Skt. yodháh ‘warrior’: Hitt. (7) hudak “at once’ beside hütas (queried: ‘agility’. IE i- normal- ly: Hitt. yc, cf. iugom); Gk. euthüs, euthú ‘straight; straightway’; cf. kél-euthos (^way, journey”. But züthos, m. n. “beer? seems to re- present an alternative IE i-, see iugom, etc.); Pol. cf. judziC 'incite'; Li. jaüdas ‘incitement’; jaudà ‘decoy’; jaudüs “luring, exciting’; Latv. jauda “ability”
6403:ieuglà (iugala, om) “link, join, yoke’. Cf. iugóm Gk. zeügle ‘thong of yoke’; Lat. jugula ‘Orion’; jugulum ‘throat’; full-gde. vowel in MHG jiuch “acre of land’. See next
6404:ieugmn- (iugmn-) “Join, link, pair”. Cf. iugóm, etc. Skt. cf. yugmah ‘even’; yugmam “pair, couple’; Gk. zeügma; lr. uaim pl. uama, uamanna *joint, link
6405:ieugð, ið (ieugnu-, iugā-, iüg-) “join, link, yoke'. Cf. ieug-, ioug-, iug-. WP I, 202 Vedic yojami; Av. yaoja, lsg. “join, a group’; Tokh. B yaukk- (queried: *use)); Gk. zeügnü-
6406:ieu (ieu-ge, ieu-ghi, ieu-que, ieu») — ieunis, os, à
6415:ieugos, -es- ‘yoke; acre; team of animals”. Cf. leug-, ieugó, ioug-, lug- and WP I, 202 Skt. yogah “join; yoke, team’. Isophonic w. yógas, n. “meditation”; Hitt. cf. yugas (“yearl- ing animal *fit for yoking’. Here EHS : HG); Myc. zeuk-; Gk. zeügos, n. ‘yoke, team’; Lat. jügus, n. ‘acre’; MHG jiuch ‘acre’ beside OE gēoc, id. (and ‘yoke’. Spg. ambig.); W cf. ie- wydd (*yoke-collar', fr. *iugiio; OCS cf. iZesa, npl. ‘yokes’: Lat. cf. jügera, Gk. zeügea)
6416:ieugo (ioug-, iug-) (1) ‘move, stir, drive; strive’. Cf. WP I, 201 Skt. cf. abhi-yujàmi ‘attack’; Av. yaoz-, intr. ‘stir; be roused’; Per. yüzam, -idan ‘jump’; LW in Arm. huzem ‘stir’; Tokh. AB yuk-, A (also) ok- “defeat; Go. ga-jiukan, id.; jiuka “passion, temper’; OE cf. geocor ‘awful’; (o-gde in) MHG jouchen, jóuchen 'chase'; SG jauken, id.; ON eykr, pl.-ir fdraught-animal; eyki ‘cart’; Sw. ök, n., pl. id. *draught-animaP. (Lat. -ügo in vesper-? and lan-" is of uncertain ori- gin)
6417:ieuo (2) ‘reinforce; be strong? Av. cf. yaoja, lsg. (‘bind myself. Ambig. cf. ieugo) beside yuxš "be strong"; cf. yüxóa, adj. ‘strong, firm’; OE geoc “help, safety’; geocian “help”
6418:ieul- ‘shout, exult; exultation’. Cf. iaul- (onomat.) and iāl-, id. Gk. cf. ioulos ‘hymn to Ceres’; Alb. zulë ‘exul- tation’; Lat. cf. é-julo, are 'exult'; Ir. cf. uaillim ‘howl, shout' (fr. *ieudhl- or sim.); Go. jiuleis *yuletide'; Sw. jul, id. (beside ON jól, and ýla *howl' w. variant vocalisms); Finn. LW juhla ‘festivity’ beside joulu ‘Yule’. (For Lat. ad-ülor, -ūlārī see eulo in Supt.)
6419:ieumi, see jeuð
6420:ieumos, is, io (ium-) den, cave’. Cf. ioma, ieunis Ir. uaimh, f. ‘cave, cellar; kiln’; Latv. cf. jums ‘roof, shelter, vault, clamp’; Go. (?) jumjo “pile?
6421:ieunis, os, à (1) “hole”, lair, den, bed Cf. ieum-, iðm-
6424:ieunis, os (2) ‘deficient; defect’. Cf. iünis and next Skt. cf. yünih ‘barren animal beside ünáh de- ficient’; Gk. eünis, gs -ios ‘bereft’; LW in Alb. 6jé (‘ewe or goat bereft of young’, fr. Lat. je- juna); Lat. cf. je-jünus ‘barren, fasting’ beside jün-ix, f. ‘heifer’ and jüni-perus ‘juniper’, lit. ‘barren of fruit’; Olr. cf. on, oin, f. “fasting, fast; oínaim, v. “fast”
6425:ieunos (ieunos, ieuonos, is) ‘young’. (Same as (2) ?). WP I, 200 Skt. yuvàn, obl: yün- ‘young’; s. ‘youth’; yau- vanam 'the youth'; Av. yava, acc: yavanom, gen: yüno “young man; Per. javan (£-); Lat. juvenis; Ir. (?) uaine ‘green’; OCS junáü, adi: OCz. jun, m.; R junyj; Srb. cf. june, pl. juneta ‘bullock; heifer’; Li. jáunas; Latv. jauns. Cf. ieuntà (ieuntà, ieunotà, iuunta) “early life, youth’: Skt. yuvata; Oss. zäväd ‘scion, young shoot”; Lat. juventa; Olr. cf. oitiu, coll. ‘the youth’; W ieuant, pl. ieuaint, m. ‘adolescent’; OHG jugund, OE geogop “the young? beside Go. junda, 1d.; ON jóð *baby'; OCS junota; Li. cf. jaunátve *young people'; Latv. jaunatne, id.
6426:ieuros (ieuruot-?) ‘filth’. Cf. ouros . Gk. cf. eurós, gs. eurótos ‘decay, squalor, mould"; Li. jáuras, -a, m. f. ‘swamp’
6427:ieus (iðus?) ‘good, right, proper; goodness”, etc. See jous and cf. WP I, 203. Cf. also ieuaio Skt. yós, n. or indecl. ‘goodness, health’; Av. cf. yaos *purely'; OLat. ious, Lat. jüs, gs jüris ‘common-law right
6428:ieusið (variant of type eus, q. v.) in Gk. heüo ‘singe’; Ukr. roz-ju$yty ‘inflame’ (ieusio or *jeusKo). (Latv. jaušu, jaut- = "senge!
6429:ieut- (1) (iŭt-) “join; link; mate; aid’. Cf. ieuàaio, ieuó Skt. cf. jutíh ‘union’, yünam ‘band, tie’; Av. yaoitis ‘connexion’ beside yaono (1) ‘link’; G cf. Jodi “bull *for breeding or yoking’; Li. jáu- tis, gs -čio ‘bull’; R cf. u-jut ‘comfort’; pri-jut ‘asylum’ (but cf. åut- for OE 1eóe “easy, plea- sant’; éaóe, id.) |
6430:ieut- (2) ‘surge, upsurge, feeling’, Cf. WP I, 17 & 216
6440:ieut- (3) (iout-) ‘shout, jubilate". (Forms am- big.) Br. iüda, id.; Latv. cf. jautrs ‘gay’
6441:ieutmos, à (ieusm-) ‘surge, sensation’. Cf. ieut- (2) and ieusio Ir. cf. uamhan, m. ‘fear’; Li. jaüsmas ‘feeling’; Latv. jausma ‘foreboding, rumour?
6442:ieuuó (iüuo) ‘shout, exult’ Br. iua, id., W cf. iewan, m. ‘scream’; iewin, adj. ‘noisy’; MHG jüwen ‘shout’
6443:ieuaio ‘ease, relax, benefit, aid’ Per. cf. yavar ‘helper’; yàvari, s. ‘help’; Gk. eåð “allow, leave’; Lat. cf. juvo, are ease, benefit, help, delight
6444:ieuios ‘of barley, spelt’. Cf. ieuos Skt. yávyah, id. cf. yavyá *barley-store'; Gk. zeiá 'spelt'; Li. cf. jáuja *drying-kiln'
6445:ieunkos (iounk-, iuunk-) ‘young creature, young person'. Cf. ieunos. WP I, 200 Skt. yuvakah, m.; yuvanakabh, adj.; Oss. wånig, onig, iwonig, jonág ‘bullock’; LW in Arm za- vag ‘child’ (Iran.); Lat. juvencus (fyoung, of animals’; s. 'steer); Umb. iuengar, fpl. "ber, fers’; Gaul. iovinco- (in names); MIr. ócc, Ir. óg ‘young’; ‘young person’; W ieuanc; Br. iauank; Cor. yowynk, adj. ‘young’; Go. juggs; OE geong; ON ungr, adj. ‘young’ & com. Gmc. Cz. cf. jun, junák ‘youngster’
6446:jeuntà, see ieunos
6447:ieuð, ið, ieumi ‘seethe, stir, surge, move. Cf. ieu-, ies-, ieus-. WP I, 199 Skt. yaumi, yuvámi (2) ‘mix, stir’; cf. dyaumi (synth. cpd. attack"); Tokh. AB yu- “strive, ply oneself”; Gk. cf. kel-eúð (exhort. A synthetic cpd. cf. kel-); án-eo, adv. ‘stil? may belong here; ON úa, ýja ‘swarm, teem’; Li. jáuju, jauti; Latv. jauju, jaut “stir, mix’
6448:ieuos, -es-, (ieuio) “a grain (barley, spelt)'. Cf. ieuð (?). WP I, 202 Skt. yávah "a grain, esp. barley”; yavasa, npl. 'grass-fodder'; yavyah “supply of crops’; Av. yavo, gs yavahe ‘barley’; Per. jav (&-), id.; Oss. jäw, jew ‘millet’; Gk. zeá, zeiá ‘spelt’; Li. jà- vas, javai ‘cereals, grain’; cf. jáuja *drying-kiln';
6451:ieuót a correlative. Cf. téuót (tóuot) Skt. yavat “how much, — great, — long’; Gk. héos 'so long as, till
```


## [2026-10-17T00:36:33.027Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"ieugo (ioug-, iug-) (1)\")) print \"ieugo leaf\", NR-1; if (index($0,\"ieudhos (ioudhos\")) print \"ieudhos leaf\", NR-1}' IEC.txt; grep -n \"^iūs\\|^ius\\|^iu̯s\\|^iūsm\\|^iūs-\\|^iusmā\\|^iūsmā\\|^iūsā\\|^iudh\" IEC.txt | head"
}
```


### [2026-10-17T00:36:33.409Z] TOOL RESULT

```
ieudhos leaf 256
ieugo leaf 257
6522:iudhlos (1) ‘twaddle, raving’ Hes. huthlós, id.; Lat. jübilum ('exultation'. Vowel-length infl. by Hebrew); G cf. jodeln (‘to yodel, but w. consonantism of LG. Late); Sw. cf. joller (*twaddle', fr. *iudhleso, npl.); (Hes. variant husthlós)
6530:iudhlos (2) ‘movement’. Cf. iudho, ieudh-, etc. Ir. iúl “direction, course’
6531:iudhmos (iudhmin-) ‘movement, action, battle’. Cf. ieudh-, iudho, etc. Skt. yudhmáh ‘warrior; battle’; Gk. husmineé ‘battle’; OCS cf. o-jminü, pl. oam “warrior” (for *o + *iudhm-, cf. igo ‘yoke’ for vocalism)
6532:iudho, ið “go, move, stir, rouse, excite’. Cf. ieudh-, ioudh- and next. WP I, 203 Skt. yüdhyàmi “go, move, fight’; Av. yüióyei (mi) ‘fight’; Gk. cf. él-uthon, aor. 1sg. ‘I came’; husmine ‘battle’; Ir. (ambig.) uidhe (2) “step; journey’, see pod-; Lat. jubeo order: move a resolution’; OCS ido, iti, R idü, idti ‘go’. Vo- calism as OCS igó, see iug-; cf. OCz. jide (“he went’: Gk. (él-)-uthe); Li. judü, éti ‘move’; cf. jundù, inf. jüsti ‘get going?
6533:iudhos, à ‘stir, movement, ferment, battle’. WP I, 203. Cf. iudho Skt. yudh, f. ‘battle’; Gk. (-ü-) züthos, m. & n. beer": Ir. (ambig.) uidhe, -e (journey, march’, but cf. pod-); Li. judà ‘movement’; cf. Latv. jauda 'strength'. (Isophonic: G Jute “sweet whey’. Gk. hussós ‘dart’, if related, in- dicates a secondary *i- in a type *iudhios. An extn. of type *iudht- is indicated in Skt. yud- dhah ‘subdued’, yuddhám, à and in Sw. yster, adj. ^wayward, wild")
6560:iustós ‘stirred, moved, fermented; uphea- val”, etc. Cf. ieuo, leus-, iüs and iudh- Oss. cf. dzüs, Dig. dzosá ‘saline solution’; ON ostr ‘cheese’, beside ysta, intr. ‘curdle’; Sw. etc. ost ‘cheese’; ysta, v. as ON; LW in Finn. juusto ‘cheese’. Cf. variant in Br. iud (‘broth’, brew’), fr. *iuto- (or *iouto-)
6561:iusuer- (iuuer-), poss. adj. cf. ius, iusme- Olr. for, far ‘your’; Go. izwar, pl. id., OHG iuwér, iuwar, iuér; OE Gower Cf. variant in OS euwa, iuwa; Du. uw; Fris. jou, id.
```


## [2026-10-17T00:36:40.394Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^juice\\|^enzyme\\|^zym\" SKT.txt | head; grep -n -A4 -i \"^Juice\" SKT.txt | head -12; grep -n -i \"iūs\\|jūs\\|yūṣ\" SYN.txt | head -8"
}
```


### [2026-10-17T00:36:40.774Z] TOOL RESULT

```
9540:JUICE.
21835:ZYMOTIC
9540:JUICE.
9541-Jolt,  to  jerk.  (E)  From/*/?.' the  Joie  or  head  ,  cf.  As  You  Lil
9542-Joy :  see  Gaud.
9543-Jubilation,  a    shouting Frr>m   L.   iubitatio^  ^b  —  L. of  itibilarey  to  shout  for  joy. ^X*  I a   shout   of  joy.     %    Quite   distill jubilu.
9544-Jubilee,  a  sea>on  of  great -Hcb.)  M.  ^.  jiibilt€.~U. jubilee;'  Cot.  — L,  itibiloHs, (Levit.  XXV.  ii);  masc.  of  adj.  t belonging  to  the  jubilee  i  Levit.  xxv Hcb.  jr66tt,  a  blast  of  a  trumpet  i joy.     %  Distinct  from  the  word  at
```


## [2026-10-17T00:36:44.929Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"Juice, sap\\|juice, \\|ius, broth\\|iūs, broth\\|jus, broth\" SKT.txt | head; grep -n -i \"broth\\|leaven\" SYN.txt | head -10"
}
```


### [2026-10-17T00:36:45.246Z] TOOL RESULT

```
972:Arrack,  an  ardent  spirit.  (Arab.)  Anb. 'amy.  sweat,  juice,  essence, riiitillcd  spirit.— Arab  root  'araqa,  to  sweat  %  f^onietiniM shortened  to  Ha(k\  cf.  Span.  ra<^ue,  arrack. ratafia,  a  liquor  (F.-Arab.iiM./ Ms- lay.)  V.ratafia\  cf.  tafia,  rum-arinck.* Malay  araq  tdfla,  the  spirit  called  A^; where  araq  is  borrowed  from  AnU *araq.
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
2552:Many of the words of relationship be- long to well-known groups of cognates pointing to specific words for these rela- tions existing in the parent speech. The most widespread are those which are represented by NE father, mother, son, daughter, brother, sister. Others for which there is sufficient agreement to indicate IE origin are words for ‘grand- son’ or ‘nephew’, for ‘paternal uncle’, and, in relationship by marriage, those for the ‘daughter-in-law’ and for her husband’s father, mother, brother, or sister, or even her husband’s brother’s wife. That is, the IE family was ob- viously not matriarchal. The wife be- came one of her husband’s family, and it was the relations between her and her husband’s family that were important. The relations between the husband and a ee relatives were remoter; and age es the ‘wife’s father’, etc.
2558:In the inherited group the suffix -ter- or in some cases -er-, -or-, is conspicuous (cf. Skt. pitar-, matar-, bhratar-, duhitar-, jamatar-, yatar-; devar-, svasar-). Owing to the well-known use of this suffix in agent-nouns, these words of relationship were also formerly interpreted as agent- nouns from certain roots, e.g. ‘father’ as ‘protector’, ‘mother’ as ‘measurer, thoughtful one’, or the like, ‘brother’ as ‘supporter’, ‘daughter’ as ‘milker’, either the ‘suckling’ or the ‘milkmaid’, etc. Most of these derivations now seem fan- ciful and pointless and are generally given up. The use of the suffix is not to be connected directly with its use in agent-nouns, but rather with the use of -tero- (-ero) in words of contrasted rela- tionship, like Lat. dexter vs. sinister, nos- ter vs. vester, etc., that is, it was used in words for ‘father’ and ‘mother’, etc. as contrasted terms. Cf. Streitberg, IF 35.196.
2908:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 107 2.44 2.45 BROTHER SISTER Grk. 4ded¢ds abehon NG abeAdeds, pop. Abephés 4deAH7, POP- d5epon s Lat. frdter soror It. fratello sorella Fr. frére se@ur Sp. hermano hermana Rum. frate sora Ir. brathir siur Nir.  dearbrathatr deirbhshiur W. brawd chwaer Br. breur c’hoar Goth. brépar swistar ON brddir systir Dan. _broder sdster Sw. broder syster (0) 0) brddor sweostor ME brother sister, suster NE brother sister Du. broeder zuster OHG  bruodar swestar MHG_bruoder swester NHG _ bruder schwester Lith.  brdlis sesuo Lett. bralis masa ChSl.  bratrii, brati sestra SCr. brat sesira Boh.  brair sestra Pol. brat siostra Russ. brat sestra Skt. bhratar- svasar- Av. bratar- x’ anhar-
2909:2.44. ‘Brother’. 1. IE *bhrater-, pos- sibly fr. *bher- ‘bear’, as ‘protector, sustainer’ of the sisters(?). Walde-P. 2.193. Ernout-M. 386. Walde-H. 1.542. Here belong all the words listed except the Greek and the Spanish; also Arm. etbair, Toch. A pracar, B procer. Grk. $parnp only as ‘member of the $parpla ‘brotherhood’. So Sp. fraire, fraile only for brother in religious sense, friar, monk’. NIr. brathair ‘friar’ or in ae sense ‘Telative, kinsman’, as ae eee by dear-bhrathair lit. Gr iets a ‘sister’ in religious s Hae an ae ae ri ie vs. deirbhshiur ee a . brolis, Lett. bralis
2912:2. Grk. a5eddés ‘brother’, adeAd7 ‘sis- ter’, dial. also ddeddeds, adeAged, fr. *4-Seddos (-cos) : Skt. sa-garbhya- ‘of the same womb’, cpd. of cop. sa- (Grk. 4-) and garbha- ‘womb’ (: Grk. deddis ‘womb’). Walde-P. 1.692. This was doubtless first used as an adj. defining oparnp, either more specifically as ‘frater uterinus’ (in contrast to brother by the same father only), or simply as ‘brother by blood’ after ¢parnp had come to be applied to the member of a phratry.
2913:Grk. xaciyvnros in Homer (where also xacvyynrn ‘sister’), and the reg. prose word for ‘brother’ in Cyprian, a epd. of
2917:3. Sp. hermano ‘brother’, hermana ‘sister’, fr. Lat. germdnus, germana (: germen ‘sprout, germ’) used with frater, soror and also alone for ‘own, full brother, sister’, more common than frater, soror in MLat. documents of Italy before a.p. 1000. Ernout-M. 417. Walde-H. 1.594. REW 3742. P. Ae- bischer, Z. rom. Ph. 57.211 f.
2925:2.452. Special expressions for ‘broth- er(s) and sister(s)’ are uncommon.
3098:monly used also to include ‘uncle’ or ‘aunt’? by marriage, that is ‘uncle-in- law’, etc. Specific expressions for such relation, as for ‘father’s brother’s wife’ in Slavic, are not included in the table.
```


## [2026-10-17T00:36:50.378Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{0,100\\}yūṣa.\\{0,200\\}\\|.\\{0,100\\}yusa-.\\{0,200\\}\" SYN.txt | head -3; echo ARY; grep -n \"جوشیدن\\|جستن\\|یوز\\|آنزیم\" incoming/ARY/ARY_pages.txt | head -15; grep -n -i \"JUSIDAN\\|JOSTAN\\|YUZ\\b\\|ANZIM\\|JUS\\b\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:36:53.140Z] TOOL RESULT

```
ugrep: error: error at position 165
\xbf][\x80-\xbf]*){0,200}
                         \___exceeds complexity limits


ARY
6305:جوشیدن, جوش / ۲۱۵ ۱
16164:مها پرسور میور چیوز جم جوزرمتی‌زد بش00 ۸ بت۸ ,18082 و
12:JUS ay
1489:ONIONS: (ALVEOUS) 29 ALVEOLO (PORTUGUESE) Jus 4
4062:BARNHART: (TWENTY) 1178 TIGJUS, AGOTHIC) SE
4063:DELAMARRE: (VINGT) 215 TWAITIGJUS
6638:FIDWOR, TIGJUS (GOTHIC) eS
8853:ROZGA (BULGARIAN) (§ js RAJJUS SANSKRIT) 24 Sale
11772:LAS Sha gay Cau“ Gighl “ia pp dy) aud JUS WBS APERSTAN) yuaslb
13018:Ad Lh foo dly KJUSA, KJUS SWEDISH) (So yo
```


## [2026-10-17T00:36:57.110Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"جوشیدن, جوش\")) {print \"leaf\",NR-1; print}}' incoming/ARY/ARY_pages.txt | grep -n \"leaf\\|pdf page\\|جوش\\|[A-Z]\\{3,\\}\" | head -30"
}
```


### [2026-10-17T00:36:57.583Z] TOOL RESULT

```
1:leaf 213
2:[pdf page 214]
5:جوشیدن, جوش / ۲۱۵ ۱
```


## [2026-10-17T00:37:09.943Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==214' incoming/ARY/ARY_pages.txt | head -60; grep -n \"pdf page 214\\]\" -A60 incoming/ARY/ARY_latin_index_pages.txt | head -70"
}
```


### [2026-10-17T00:37:10.259Z] TOOL RESULT

```
[pdf page 214]
ی
۱
جوشیدن, جوش / ۲۱۵ ۱
۱
کردی (۷0021570: 79200[ ,1ل1۷۷۸[ سرئدی (8580150): 6 :
بلوچی (71ل/انآ8۸): 31۸ نروژی (/(۸08۳01۸): 16
افغانی (پشتو) (/۸۳0//۸(۷): 1۸۷۸0۲ ,2/80 هلدی (4ل007): 706
سانسکریت (54(877): ب۸8 7۷ اسلاوی کهن (102شا؟ ل#نابل) صا0):
۸8 ,۸۸8 ,0۷۸ بکم۷107۸8 3
آرمنی (۸745/14): روسی (۲75514/۷): زفداره
۷0۷۸۸ ,۸۷۸۸۲۸6 یتوانی (71۸4/۷ل۸نا77ا):
لاتین (/7/0ل): 0۷8018[ ,8ن1۷8161[ 85 ,۸5 اناه[
فرانسه (88۸/0/4): انار نونی (لتی) (47714(7ا): 115
اسپانیایی (8۳۸(187): 31.0 ایرلندی کهن (لاکلها صا0):
ایتالبایی ((74/۸): 00 17 0۸6 ,0۸85 ,0۸
رومانی (۸/۸(/۸۵تا۸): 3118 ولزی (7/فاق#): ۰ 1817۴ ,ناش بت االشن81[
پرتغالی (۳0701582): برتونی (8770۸7): ل ۱
8 0۷826[
گنیک (0077//0): 0008[ ,0305[ پسگشت‌ها انش دا
ایسلندی کهن ((4(01۸۸۷1۸ی5 صا0): 510 ۸0020
10 5 (0001736 84047
نررس کهن (۸0782 ص0): 1 4 (816[) :هام02
ساکسونی کهن (242:0۸ 0ا0): زاره 41 (01-36) بدا اد ها
فریزی کهن ((51۸ل۲# طاه): انز 95958 اه
آلمانی ,کهن (/088/40 ۲۱0۶ صام: 00۵[ 1 (000136 :005
آلمانی (4/ل057): 116 9 (0001-36 وا ده
انگلیسی کهن (20/0158 صام: 050۳6 2 (06ت۷01) ۸0
انگلیسی (8۸0150). ید۱ برهان قاطع + ۹۵
4۳ دانمارکی: 87اب( 0): 6
"۰ تً :۳
5۹
اوستایی (4۲28744): ۷۸5178171 ,-۷۸3 7 11511۸811[
کردی (80150(): بلوچی (01)تاملم8): 0۸0(

6167:[pdf page 214]
6168-os
6169-| NNO | tse het ye
6170-| UNG (SWEDISH) 5-8 y= JIWAN, JUVAN (KURDISH) 62,5
6171-UNG (NORWEGIAN) 8335 JAVAN X(BALUCHI) gz sh
6172-JONG DUTCH) gala = ZWAN, JAVAN. (AFGHAND) (+4) gsi
6173-:(OLD CHURCH SLAVIC) 34S 5.33! yuvas, (SANSKRIT) <4 Site
6174-JUNT YUVASAS, YUVAN, YONAS, JUVACAS
6175-JUNYJ (RUSSIAN) 53 ARMENIAN) gs,
6176-(LITHUANIAN) gly YAVANAK, YOVANAK,
6177-JAUNAS, JAUNIKIS JUVENCUS, JUVENIS (LATIN) 53
6178-JAUNS (LATVIAN) (3) 3 JEUNE FRENCH) «i
6179-(OLD IRISH) gS 54) 3) JOVEN SPANISH) gles
6180-Ba, GAM, GAC, OITIU GIOVANE HUTALIAN) g\dta}
6181-JEUANE, IAU, IEUF (WELSH) 635 JUNE RUMANIAN) slay,
6182-YAOUANK HBRETON) 35 2 PORTUGUESE) J
6183-JOVEM, JOVENS
6184-‘REFERENCES beth JUNGS, JUGGS — (GOTHIC) SF
6185-poKomy, OSO~*~CS~*~S*~S~«S OLD SCANDINAVIAN) iff 6he\
6186-BARNHART: _ (YOUNG) 1255 UNGR
6187-DELAMARRE: (JEUNE) 224 UNGER (OLD NORSE) 95 33
6188-MACKENZIE: (YOUNG) 141 JUNG (OLD SAXON) oS iS
6189-BUCK: 957-988 JUNG HOLD FRISIAN) S523
6190-ONIONS: (YOUNG) 1021 JUNG (OLD HIGH GERMAN) yf glut
6191-SKEAT: (YOUNG) 729 JUNG (GERMAN) gist
6192-AMINDAROV: (YOUNG) 312, GEONG (OLD ENGLISH) 35, lil
6193-04d igbG ub, YOUNG ENGLISH) lS
6194-UNG DANISH, Sala
6195-“ht
6196-ua
6197-JUSHANIN, JUSHVERDIN ‘YAH-, YAESHYEITI :(AVESTAN) pl!
6198-JOSHENAG MBALUCHI) gh (KURDISH) (53,5
6199-[pdf page 215]
6200-Olsle aye | VE
6201-JAST (SWEDISH) 54 yo YESHA- 4AFGHANI) (3-4) git
6202-GIST (DUTCH) gocha YAS :(TOKHARIAN A) A 6 ,\55
6203-ws yh AGAULISH) IF Yis (TOKHARIAN B) B s,s
6204-we » 8 * YAS-, YESATI (SANSKRIT) cy Suit
6205-| REFERENCES Denthey yAsaTI, YOSH, YUSHAN
6206-POKORNY, —~SS*~*~*~S~S*~*« EO, ZEIN GREEK) ghiy
6207-BARNHART: ~ (vEAST) 1252 {OLD SCANDINAVIAN) pS Suche!
6208-DELAMARRE: JosTR
6209-(BOUILLIR, BOUILLONNER) 261 JOSTR (OLD NORSE) aS e335
6210-BUCK: 676 JESAN:(OLD HIGH GERMAN) pS gas
6211-ONIONS: (YEAST) 1019 GAREN, GISCHT — (GERMAN) ,glT
6212-SKEAT: (YEAST) 728 GIEST — (OLD ENGLISH) oS 3S!
6213-Foe : ieboby YEAST ENGLISH) gutS3h
6214-> leetloal
6215-: wpb ni ay} SUN; 029) glisal a He GHOL) F293 oll
6216-KIUWAN JUDAN, JOYITAN — :(PAHLAVI) 5 4
6217-KAUEN GERMAN) gilt JUTIN, JON, JOIN (KURDISH) 52,5
6218-CBOWAN (OLD ENGLISH) pS pK! ‘ZHIYAG (BALUCHI) gs
6219-CHEW HENGLISH) goulSs AFGHAN) (54) gilts!
6220-KAUWEN (DUTCH) «sicla ZHOVAL, ZHOYAL
6221-(OLD CHURCH SLAVIC) pS g3%=i + ZWATSI :(TOKHARIAN A) A ($55
6222-ZHIVATI, ZHUJU ZWATSI, SWA.:(TOKHARIAN B) B 3 \%5
6223-ZHUCIA POLISH) long) KIV, KVENI ARMENIAN) gs,
6224-ZHIVAT, ZHUJU (RUSSIAN) ys) GINGIVA LATIN) 53
6225-7AUI CZECH) Soy (OLD SCANDINAVIAN) 4S $-th-5\
6226-ZHONA (BULGARIAN) «5 )\ih, TYGGVA
6227-ZHUVAT (SLOVAK) 5 shal TYGGVA OLD NORSE) oS 393
```


## [2026-10-17T00:37:15.749Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"YAOD\\|YUIDY\\|YUDH\\|YAOZ\\|YUDHYATI\\|JOSTAN\\|JUSTAN\" incoming/ARY/ARY_latin_index_pages.txt | head; grep -n \"جستن\\|یوز\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-10-17T00:37:16.063Z] TOOL RESULT

```
16164:مها پرسور میور چیوز جم جوزرمتی‌زد بش00 ۸ بت۸ ,18082 و
```


## [2026-10-17T00:37:20.138Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; for n in 208 209 212 213; do echo \"### leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' WLD_Bd1_pages.txt | grep -n -i \"ieu\\|jeu\\|i̯eu\\|yüs\\|iüs\\|zum\\|yaoz\\|yuidy\\|yudh\\|mischen\\|kämpf\" | head -12; done"
}
```


### [2026-10-17T00:37:20.538Z] TOOL RESULT

```
### leaf 208
1:                                                                 iaro-    — ieu-                                                 199
39:1.   ieu-      „vermengen, bei der Speisezubereitung"                                    (:        ieu-.             ;
41:        letzteres auf Grund der Dehnstufen, oder vor einer set-Basis *ieu ri x -)
42:        vermutlich eine Sonderanwendung von ieu- „vcrbinden“.
47:„heifies Wasser dariiber gieBen", lett. jdut „Teig einriihren. mischen", jaws
50:ieu-to- ? s. Fick II 4 224, Pedersen KG. 165. Sommer Gr. Ltst. 142); gr.
### leaf 209
1:200                                                                                      ieu-
4:2.   ieu- „jung‘\ Positiv iuw-n-                                         f
5:                                                                             :   i"ii-),                Komp. ieu-ius-.
35:     air.    0a ..junger". Omn ..jiingst". meymr. ieu (ncymr. uni) ..jiinger", ieuaf (so
79:zum LiebesgenuB geeignetes \Yeib. Gattin“; das lat. Juno nach Ehrlich
### leaf 212
6:                                                            ieuos     — ieudh-                                                       203
74:ieug- ,,aufregen. unruhig“ (oh'! s. u.i.
75:  Av. yaoza.it ,.regt sich auf (vom Yasser, von unruhigen Landern“), yco.di-
78:(vgl. zur Bed. gr. voump ai. yudh- „kampfen“ udijodlmti  ,,wallt auf“). jiufom:                         =
88:Wb. 161),               muf.ite av. yaozti-             Entgleisung          fiir         *yaozdi-.         und germ. Jc durch
90:auch h aus dJt haben und zur         verwandten                   —                         — Wz. *ieu-dh- gehoren.
94:yati „verwiekelt in Kampf“, yudhyati, yodhali „kampft“. yiidh- m. „Kampfer“.
95:t.   j.Kampf, Schlacht“,                          yudhmd-h „kriegerisch“, m. „Kampfer“.                                yodhija.s-
### leaf 213
6:204                                                                             ieudli-
10:„streitbarer,                         besser kiimpfend" (wie aor aijodlat aus *ieudhi-    .                              :   iuclhc\i]-   in
12:  av. yuidycinti „sie kiimpfen“, yuidista- „der am besten kampft"; dazu
13:aus *ieudJi-s- (s. Johansson IF. 19, 137 und unten gr. vo/uvrj), av. yaosti-
59:mim. PI. o/bmi „Krieger‘- (= ai. yudhmA-h mit Praefixo-). Anders IF. 21, 196.
66:ieu-ni- oder ioutii- etwa „angewiesene Stiitte, richtiger Platz“.
```


## [2026-10-17T00:37:30.366Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/566.jpg 2>/dev/null; pdftoppm -f 566 -l 566 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg566 && echo ok"
}
```


### [2026-10-17T00:37:31.284Z] TOOL RESULT

```
site/pages/566.jpg
ok
```


## [2026-10-17T00:37:34.253Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg566.png"
}
```


### [2026-10-17T00:37:34.666Z] TOOL RESULT

```

```


## [2026-10-17T00:37:34.661Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:37:48.459Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg566.png data/verification/sources/refs/ocr/BOOK/566.png && echo ok; python3 -c \"import json;print(json.load(open('data/verification/sources/refs_online.json')).get('FFD',{}).get('local_file'))\""
}
```


### [2026-10-17T00:37:48.828Z] TOOL RESULT

```
ok
['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt']
```


## [2026-10-17T00:37:53.691Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; grep -n \"جستن\\|جوی\" FFD_pages.txt | head -8; grep -n -i \"yaud\\|ǰōy\\|jōy\\|joy-\" FFD_pages_faseng.txt | head -8"
}
```


### [2026-10-17T00:37:54.009Z] TOOL RESULT

```
1316:بجستن
1322:جوی < ایرانی باستان 7۵00-2*. برای 2 -> آرای.
1323:«جور؛»» دیگر ماد مضارع «جستن»» جدید است > شستن.
1331:جویدن
1332:جوید ماده ماضی جعلی و از ماده مضارع ساخته شده است. در قارسی میانه 00[
1334:0[ است» «جویدن) معنی می‌دهد.
1374:خای چ ایرانی باستان 304-2 برای 3 > آرای. ريشةٌ 40 به معنی «جویدنُ» است.
1716:اشوی» جدید است > جستن.
ugrep: warning: FFD_pages_faseng.txt: No such file or directory
```


## [2026-10-17T00:37:57.125Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; sed -n 1310,1330p FFD_pages.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"جوی < ایرانی باستان\")) print \"leaf\",NR-1}' FFD_pages.txt"
}
```


### [2026-10-17T00:37:57.466Z] TOOL RESULT

```
توخت + فارسی میانه 1574 < ایرانی باستان 1۵-:120*. برای 12 > آراست. 1208
صورت اصلی 120 است» 8 پیش از 1 به #بدل شده است. ريشهٌ 1308 به معنی «پرداختن»
توز « فارسی میانه 132 < ایرانی باستان ۵-[1۵*. برای 2 -> آرای. [به جای 8 آمده
در فارسی میانه به معنی «پرداختن» و «توبه و جبران کردنْ» است. در فارسی
دری به معنی «فرو کردن و کشیدن و پرداختن» آمده است. شاهنامه:
چو وامش بتوزی درم صد هزار بده تا بدارد زماینادگار
بجستن
جست < ایرانی باستان 7۶-1*. برای 12 -> آراست. 104 صورت اصلی فا است» ‎٩‏
‏پیش از ۶ به 8 بدل شده است. 04 که صورت ضعیف 7204 است» «نبرد کردنْ» معنی
می‌دهد.
[pdf page 53]
ال فعلهای فارسی دری
جوی < ایرانی باستان 7۵00-2*. برای 2 -> آرای.
«جور؛»» دیگر ماد مضارع «جستن»» جدید است > شستن.
از 12040 در پهلوی اشکانی 7047 به معنی «نبرد کردن» آمده است. از ایرانی باستان
۱ 1-82 12 نشانه‌ای بوده که برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است.
جستر
جست < فارسی میانه 281[. 29122[ در فارسی میانه به معنی «اتفاق‌افتادن» است و
اسم مصدرش 28150[ «بخت) معنی می‌دهد. «جهشیار»» نام خاص, در فارسی میانه
7- 20158[ است به معنی «بختیار).
ججه « فارسی میانه ۵0[.
leaf 52
```


## [2026-10-17T00:40:43.398Z] TOOL CALL #67: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-566.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nS_JOSH=[W+\"جوش\", W+\"Reconstruction:Proto-Indo-European/yes-\", W+\"جوشیدن\", \"https://vajehyab.com/moein/جوشیدن\"]\nPOK507={\"src\":\"POK\",\"where\":\"POK_full.txt 'Root / lemma: jeu-1', Page(s): 507\",\"stance\":\"supports\",\"note\":\"'jeu-1 Meaning: to mix (of meal preparation) ... Old Indie yūṣ (only Nom.), yūṣa- \\\"broth\\\", Latin iūs, iūris \\\"broth, soup\\\" ... perhaps in addition gr. zūmē \\\"sourdough\\\"'.\"}\nWLD199={\"src\":\"WLD\",\"where\":\"WLD_Bd1_pages.txt leaf 208 = Bd. I p. 199\",\"stance\":\"supports\",\"note\":\"'1. ieu- \\\"vermengen, bei der Speisezubereitung\\\"' with the *iūs- 'broth' derivatives.\"}\nAHDyeue={\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt line 1197 'yeuə-'\",\"stance\":\"supports\",\"note\":\"'yeuə-. To blend, mix food. ... *yū-s- in Latin jūs, juice, broth: JUICE; ... *yūs-mā in Greek zūmē, leaven: -ZYME, ZYMO-; ENZYME. [Pok. 1. ieu- 507.]'\"}\nKLNjuice={\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 450 s.v. juice\",\"stance\":\"supports\",\"note\":\"'juice, n. — ME. jus, juse, fr. MF. (= F.) jus, fr. L. jūs, \\\"broth, soup\\\", fr. I.-E. base *yūs-, whence also OI. yūṣ-, \\\"broth\\\" ... Gk. zūmē \\\"leaven\\\" ... Base yūs- is an enlargement of base *yeu-, \\\"to mix\\\"'.\"}\nCHEUNG_iah={\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt pp. 209-210 s.v. *i̯ah 'to boil, bubble'\",\"stance\":\"contradicts\",\"note\":\"'*AVESTAN: YAv. yaēš- \\\"to boil\\\" ... *SOGDIAN: (+ *abi-) BSogd. βy’ys’ntk \\\"boiling\\\" ... *NWIR: NP jōšīdan/jōš- (denomin.) \\\"to boil\\\", jōš \\\"boiling\\\" ... PIE *i̯es- \\\"to boil, seethe\\\" | Pok.: 506'. Also p.~225 (s.v. *kaup?): 'NP jōš \\\"boiling\\\", etc. go back to the redupl. formation of *i̯ah'.\"}\nARYjosh={\"src\":\"ARY\",\"where\":\"ARY_pages.txt [pdf page 214] = printed p. 215, s.v. جوشیدن، جوش; Latin index pdf p. 214-215\",\"stance\":\"contradicts\",\"note\":\"Aryanpur files جوشیدن under the 'yeast' root (*yes-): 'YAH-, YAESHYEITI (AVESTAN) ... YAS-, YESATI (SANSKRIT) ... ZEO, ZEIN (GREEK) ... YEAST (ENGLISH)'; Kurdish JUSHANIN, Baluchi JOSHENAG are given as cognates. He does not link it to Skt. yūṣ.\"}\n\nentry={\n \"entry\":0,\"root\":\"Yeu 3\",\"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *yewH- 'to mix (food)' (Pokorny 1. i̯eu- 507; AHD yeuə-); nominal *yúHs 'broth'\",\n \"note\":\"The root, its language label and its gloss are correct: Pokorny p. 507 'jeu-1 to mix (of meal preparation)', Walde-Pokorny I 199 'vermengen, bei der Speisezubereitung', AHD yeuə- 'to blend, mix food'. Its standard derivatives, Skt. yūṣ-, Latin iūs (→ juice) and Greek zūmē (→ enzyme), are in the chart. Two branches go beyond the standard picture. (1) The 'boil' branch (Persian jōšīdan, Av. yaēš-, Sogd. βyʾys-): Horn (no. 430), Hübschmann and Mo'in tie jōšīdan to Skt. yūṣ-, but Cheung 2007, Wiktionary and Aryanpur put Av. yaēš- and the Sogdian verb under PIE *yes- 'to boil' (Pokorny 506), a different root, and most also put jōš there. (2) *yeudh-/*yeug- 'move, fight': Pokorny and Walde-Pokorny list it as a separate root. Klein (s.v. jube) and Pokorny's own note to jeu-1 suggest it is an enlargement of *yeu-, so attaching it here is defensible but speculative. The French box prints 'ensyme', a misprint in the book for enzyme. The extraction is faithful. (The redirect 'Yewo → leuo' is printed 'leuo' on the page, while the JSON has 'Ieuo'. This is only a capital I/lower-case l reading.)\",\n \"note_fa\":\"ریشهٔ هندواروپایی آغازین *yewH- «آمیختن (خوراک)» در پوکورنی (ص ۵۰۷)، والده-پوکورنی و فرهنگ آمریکن هریتیج آمده است، و واژه‌های سنسکریت yūṣ- «آبگوشت»، لاتین iūs «آبگوشت، شوربا» (← juice) و یونانی zūmē «خمیرمایه» (← enzyme) به‌درستی از آن شمرده شده‌اند. پس ادعای نورایی دربارهٔ خودِ ریشه درست است. اما شاخهٔ «جوشیدن» (اوستایی yaēš-، سغدی βyʾys-) را چونگ، ویکی‌واژه و آریان‌پور به ریشهٔ دیگری، *yes- «جوشیدن، کف کردن»، می‌برند. شاخهٔ *yeudh-/*yeug- «جنبیدن، جنگیدن» نیز در پوکورنی ریشه‌ای جداگانه است و پیوند آن با *yeu- تنها حدسی است. «ensyme» در جعبهٔ فرانسوی خطای چاپی کتاب به جای enzyme است.\",\n \"sources\":[\"https://en.wiktionary.org/wiki/ζύμη\",\"https://en.wiktionary.org/wiki/यूष\",\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yes-\"],\n \"ref_check\":[{\"ref\":\"POK:507\",\"status\":\"supports\",\"note\":\"POK_full.txt 'Root / lemma: jeu-1 / Meaning: to mix (of meal preparation) ... originally probably \\\"set in motion\\\"; s. jeu-dh-' — Page(s): 507.\"}],\n \"consulted\":[WLD199,AHDyeue,KLNjuice,{\"src\":\"IEC\",\"where\":\"IEC.txt line 6447 s.v. ieuō\",\"stance\":\"supports\",\"note\":\"'ieuō ... \\\"seethe, stir, surge, move\\\". Cf. ieu-, ies-, ieus-. WP I, 199 Skt. yaumi, yuvāmi \\\"mix, stir\\\"; ... Latv. jauju, jaut \\\"stir, mix\\\"'.\"}],\n \"nodes\":[]}\nN=entry[\"nodes\"]\nN.append({\"id\":1,\"lang\":\"Sanskrit\",\"words\":\"yuš\",\"verdict\":\"confirmed\",\n \"derivation\":\"Skt. yūṣ- (nom. yūḥ, Vedic) and thematic yūṣa- m./n. 'soup, broth, pea-soup' come from PIE *yúHs 'broth', an s-noun to *yewH- 'mix'. The direct cognates are Latin iūs, Lithuanian jū́šė 'fish soup' and OCS jucha 'broth'. The book's 'yuš' leaves out the long ū and the retroflex ṣ (Nourai's usual simplification). The gloss 'broth made by boiling in water' matches Monier-Williams and Wiktionary ('the water in which pulses have been boiled').\",\n \"derivation_fa\":\"سنسکریت yūṣ- و yūṣa- به معنای «آبگوشت، آش، آبی که حبوبات در آن پخته شده» از هندواروپایی آغازین *yúHs «آبگوشت» است. این واژه اسمی است با پسوند -s از ریشهٔ *yewH- «آمیختن» و هم‌ریشهٔ لاتین iūs و لیتوانیایی jū́šė «شوربای ماهی» است. نگارش «yuš» در کتاب کشیدگی و برگشتگیِ صامت را نشان نمی‌دهد. ادعای نورایی درست است.\",\n \"sources\":[W+\"यूष\"],\n \"ref_check\":[{\"ref\":\"POK:507\",\"status\":\"supports\",\"note\":\"POK_full.txt p.507 jeu-1: 'Old Indie yūṣ (only Nom.), yūṣa-m. n. \\\"broth\\\", Latin iūs, iūris \\\"broth, soup\\\"'.\"}],\n \"consulted\":[WLD199,AHDyeue,KLNjuice]})\nN.append({\"id\":2,\"lang\":\"Persian\",\"words\":\"jŭšîdan\",\"verdict\":\"disputed\",\n \"derivation\":\"NP jōšīdan (Iran. jušidan) 'to boil, bubble' is a denominative of jōš 'boiling'. Its cognates are Baluchi jōšag, Kurdish jūšīn and Zefre yōs-. Horn (no. 430: 'jōšīden kochen, sieden ... ai. yūṣ-, yūṣán- Brühe'), Hübschmann ('Wzl. Iran. yauš') and Mo'in (BQT s.v.) link it to Skt. yūṣ-. Nourai's arrow follows them, and an OIr. *yauš- would give NP jōš regularly (au > ō). Cheung 2007 (*i̯ah, pp. 209-210), Wiktionary (جوش 'ultimately from PIE *yes- to foam, boil', after Cheung) and Aryanpur instead put jōš/jōšīdan with Av. yaēš- 'to boil' under PIE *yes- (Pokorny 506), a different root. The arrow is also really a cognate relation: no Persian word comes from Sanskrit. Modern scholarship prefers *yes-, so the node is disputed. The older view is phonologically neat, though, and is not absurd.\",\n \"derivation_fa\":\"«جوشیدن» فعلی است ساخته‌شده از اسم «جوش»، و هم‌ریشه با بلوچی jōšag و کردی jūšīn است. هرن (شمارهٔ ۴۳۰)، هوبشمان و معین در حاشیهٔ برهان قاطع آن را با سنسکریت yūṣ- «آبگوشت» هم‌ریشه دانسته‌اند و نورایی از آنان پیروی کرده است. از نظر آوایی نیز ایرانی باستان *yauš- به‌آسانی به jōš می‌رسد (au → ō). اما چونگ، ویکی‌واژه و آریان‌پور «جوش» را همراه اوستایی yaēš- «جوشیدن» از ریشهٔ هندواروپایی *yes- «جوشیدن، کف کردن» می‌دانند. افزون بر این، فارسی از سنسکریت نیامده و این دو تنها هم‌ریشه‌اند. پژوهش امروزی ادعای نورایی را نمی‌پذیرد.\",\n \"sources\":S_JOSH,\n \"ref_check\":[{\"ref\":\"BQT:600\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 58 (≈ p. 600-601), footnote to جوشیدن: 'هندی باستان yūṣ-, yūṣa- (آبگوشت)، کردی jūšīn، jūšverdin، بلوچی jōšag (پختن، جوشیدن، خشمگین شدن)'. Mo'in gives Nourai's Sanskrit link (after Horn).\"},\n  {\"ref\":\"MON:1254\",\"status\":\"partial\",\"note\":\"Mo'in, Farhang-e Farsi via vajehyab.com/moein/جوشیدن: '(دَ) (مص ل.) ۱ - به جوشش آمدن. ۲ - فوران کردن آب از زمین'. This confirms the word and its meaning. The online text gives no etymology.\"}],\n \"consulted\":[{\"src\":\"HRN\",\"where\":\"HRN.txt no. 430, p. 96\",\"stance\":\"supports\",\"note\":\"'430. jōšīden \\\"kochen, sieden\\\", jōš (pere) ... ai. yūṣ-, yūṣán- \\\"Brühe\\\". LW.(?) kurd. jūšverdin ... bel. jōšenag'.\"},\n  {\"src\":\"HUB\",\"where\":\"HUB.txt p. ~151 (line 5288 ff.)\",\"stance\":\"supports\",\"note\":\"'jōšīdan \\\"kochen, sieden\\\", Wzl. iran. yauš'.\"},\n  CHEUNG_iah, ARYjosh]})\nN.append({\"id\":3,\"lang\":\"Avestan\",\"words\":\"yaěš\",\"verdict\":\"disputed\",\n \"derivation\":\"YAv. yaēš- 'to boil' (pres. part. yaēšiiant-, Y 9.11, V 4; yaēšiieiti) is a real, well-attested verb, so the word and its meaning are confirmed. It continues a reduplicated present *ya-iš- of PIE *yes- 'to boil, foam' (Skt. yásati, yéṣati; Gk. zéō; OHG jesan; Engl. yeast). It does not come from *yewH- 'mix'. Cheung, Wiktionary, Bartholomae (who lists yaēšyant- under yah- 'sieden') and Horn (no. 420: 'aw. yah- \\\"sieden\\\", vergl. yaēšyantīm āpəm') all agree on this. Nourai attaches it to the wrong root.\",\n \"derivation_fa\":\"اوستایی yaēš- «جوشیدن» (صفت فاعلی yaēšiiant-) واژه‌ای واقعی و به‌خوبی گواهی‌شده است. اما از ستاک دوگانه‌شدهٔ *ya-iš- از ریشهٔ هندواروپایی *yes- «جوشیدن، کف کردن» می‌آید که هم‌ریشهٔ سنسکریت yásati، یونانی zéō و انگلیسی yeast است. پیوندی با *yewH- «آمیختن» ندارد. چونگ، بارتولومه، هرن و ویکی‌واژه هم‌داستان‌اند که نورایی این واژه را زیر ریشهٔ نادرستی آورده است.\",\n \"sources\":[W+\"Reconstruction:Proto-Indo-European/yes-\"],\n \"ref_check\":[{\"ref\":\"SOD:117\",\"status\":\"partial\",\"note\":\"SOD_pages.txt leaf 181 (≈ p. 115-117) entry 2960 'βy'ys- B βyaxs? (to)boil, (to)cook' and entry 573 'βy'ys- ... ©Av. abi-aēš; Yaghn. es ... (to)boil'. Gharib gives the Avestan verb as source of the Sogdian one, but says nothing about the IE root.\"}],\n \"consulted\":[CHEUNG_iah,{\"src\":\"BRT\",\"where\":\"BRT.txt line 20942\",\"stance\":\"partial\",\"note\":\"'yaēšant- Adj., PPA.: s. yah-'. Bartholomae files the boiling verb under yah- 'sieden' (= *yes-), not under a *yu- root.\"},\n  {\"src\":\"HRN\",\"where\":\"HRN.txt no. 420\",\"stance\":\"contradicts\",\"note\":\"'ai. yas-, yásyati ... aw. yah- \\\"sieden\\\", vergl. yaēšyantīm āpəm ... Die Grundbedeutung der Wz. yes- ist \\\"sprudeln, kochen, sieden\\\", vergl. auch gr. zéō'. Horn puts the Avestan verb under *yes-.\"},\n  {\"src\":\"POK\",\"where\":\"POK_full.txt p.506 (ies-)\",\"stance\":\"contradicts\",\"note\":\"Pokorny's jeu-1 (p.507) has no Iranian 'boil' forms. The boiling words are under ies- 'wallen, schäumen' (p.506).\"}]})\nN.append({\"id\":4,\"lang\":\"Sogdian\",\"words\":\"byěš\",\"verdict\":\"confirmed\",\n \"derivation\":\"Buddhist Sogdian βyʾys- 'to boil, cook' (pres. part. βyʾysʾntk 'boiling') < OIr. *abi-yaiša- = Av. aibi + yaēš-. Old Iranian *abi- became Sogdian βy-. The Avestan → Sogdian link as drawn is right (both continue the same Old Iranian verb). Like node 3, it really belongs to PIE *yes- 'boil', not to *yewH- 'mix'. The book's 'byěš' is Nourai's rendering of βyʾys- / βyēš.\",\n \"derivation_fa\":\"سغدی بودایی βyʾys- «جوشیدن، پختن» (صفت فاعلی βyʾysʾntk «جوشان») از ایرانی باستان *abi-yaiša- است، یعنی پیشوند *abi- همراه با همان فعل اوستایی yaēš-. پیشوند *abi- در سغدی به βy- بدل شده است. پس پیوند اوستایی و سغدی درست است و هر دو از یک فعل ایرانی باستان‌اند، اما این شاخه، چنان‌که در گره ۳ گفته شد، به ریشهٔ *yes- «جوشیدن» تعلق دارد.\",\n \"sources\":[W+\"Reconstruction:Proto-Indo-European/yes-\"],\n \"ref_check\":[{\"ref\":\"SOD:117\",\"status\":\"supports\",\"note\":\"SOD_pages.txt leaf 181 entry 2960 'βy'ys- B ... (to)boil, (to)cook'; leaf 87 entry 573 ''βy'ys- B (ə)βyēs? ©Av. abi-aēš; Yaghn. es ... (to)boil'.\"}],\n \"consulted\":[{\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt p.210 *i̯ah\",\"stance\":\"supports\",\"note\":\"'*SOGDIAN: (+ *abi-) BSogd. βy’ys’ntk, βws’nty \\\"boiling\\\"', under the same root as YAv. yaēš-.\"},\n  {\"src\":\"SOD\",\"where\":\"SOD_pages.txt entries 569-573, 2960\",\"stance\":\"supports\",\"note\":\"''py'ys- ... boiling', 'py'ys'ntcy ... f. adj.' and 'βy'ys- (to)boil, (to)cook'.\"}]})\nN.append({\"id\":5,\"lang\":\"Greek\",\"words\":\"zumě; en-zumě\",\"verdict\":\"confirmed\",\n \"derivation\":\"Ancient Greek zū́mē 'leaven, yeast' < *yuHs-meh₂ (*yūs-mā), built on the same *yuHs- 'broth' stem as Latin iūs. Greek initial *y- became z-. The adjective énzȳmos 'leavened' (en- 'in' + zūmē) is attested in Byzantine Greek, where it was used for leavened Eucharistic bread in the azyme controversy. Nourai's 'en-zumě: leavened' is this adjective. Both words are real and correctly derived.\",\n \"derivation_fa\":\"یونانی باستان zū́mē «خمیرمایه، مایه» از *yūs-mā است که بر همان ستاک *yuHs- «آبگوشت» ساخته شده که لاتین iūs از آن است. در یونانی y آغازی به z بدل شده است. صفت énzȳmos «مایه‌دار، ورآمده» از en- «در» و zūmē ساخته شده و در یونانی بیزانسی برای نان ورآمدهٔ عشای ربانی به کار رفته است. ادعای نورایی درست است.\",\n \"sources\":[W+\"ζύμη\"],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt 'yeuə-': 'suffixed form *yūs-mā in Greek zūmē, leaven: -ZYME, ZYMO-; ENZYME. [Pok. 1. ieu- 507.]'\"}],\n \"consulted\":[POK507,KLNjuice,{\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 287 s.v. enzyme\",\"stance\":\"supports\",\"note\":\"'MGk. énzymos, \\\"leavened\\\", fr. Gk. en (see 2nd en-) and zýmē \\\"leaven\\\"'.\"}]})\nN.append({\"id\":6,\"lang\":\"French\",\"words\":\"ensyme\",\"verdict\":\"transcription_suspect\",\n \"derivation\":\"The French word is enzyme (attested in French from the 1880s). It was taken over from German Enzym, coined in 1877/78 by the physiologist Wilhelm Kühne from Medieval Greek énzymos 'leavened' (Klein). So the Greek → French arrow skips the German coinage, but French is a correct intermediary for Persian. The book prints 'ensyme' with an s. No such French form exists, so this is Nourai's misprint for enzyme. The JSON reproduces the page faithfully.\",\n \"derivation_fa\":\"واژهٔ فرانسوی enzyme است. آن را فیزیولوژیست آلمانی ویلهلم کونه در ۱۸۷۷-۱۸۷۸ به صورت آلمانی Enzym از یونانی میانه énzymos «مایه‌دار» ساخت و از آن‌جا به فرانسه و انگلیسی رسید. پس میان یونانی و فرانسه حلقهٔ آلمانی افتاده است. صورت «ensyme» در کتاب خطای چاپی نورایی به جای enzyme است و خوانش اسکن درست است.\",\n \"error_in\":\"book\",\"book_prints\":\"ensyme\",\"correct_form\":\"enzyme\",\n \"sources\":[\"https://vajehyab.com/moein/آنزیم\"],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference cited for this node.\"}],\n \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 287 s.v. enzyme\",\"stance\":\"partial\",\"note\":\"'G. Enzym, coined by the German physiologist Wilhelm Kühne (1837-1900) in 1878 fr. MGk. énzymos'. The coinage is German, not French.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt grep '^Enzyme|^Zym'\",\"stance\":\"silent\",\"note\":\"Skeat has ZYMOTIC but no enzyme entry.\"},\n  {\"src\":\"BOOK\",\"where\":\"data/verification/sources/refs/ocr/BOOK/566.png\",\"stance\":\"supports\",\"note\":\"The printed French box reads 'ensyme : enzyme'. The misprint is in the book.\"}]})\nN.append({\"id\":7,\"lang\":\"Persian\",\"words\":\"ânzîm\",\"verdict\":\"confirmed\",\n \"derivation\":\"NP ânzim آنزیم 'enzyme' is a 20th-century scientific loan from French enzyme. The French nasal en [ɑ̃] is rendered ân, and the final -e is dropped. Mo'in tags the word '[فر.]' (French). The Academy equivalent is زی‌مایه.\",\n \"derivation_fa\":\"«آنزیم» وام‌واژه‌ای علمی از فرانسوی enzyme در سدهٔ بیستم است. واکهٔ خیشومی فرانسوی en به «آن» برگردانده شده است. معین آن را با نشان [فر.] آورده و فرهنگستان «زی‌مایه» را به جایش نهاده است. ادعای نورایی درست است.\",\n \"sources\":[\"https://vajehyab.com/moein/آنزیم\",\"https://vajehyab.com/amid/آنزیم\",W+\"آنزیم\"],\n \"ref_check\":[{\"ref\":\"AMD:57\",\"status\":\"partial\",\"note\":\"Amid via vajehyab.com/amid/آنزیم: 'مادهٔ آلی که توسط سلول‌های بدن ساخته و ترشح می‌شود و سبب تسریع فعل و انفعال شیمیایی مواد می‌شود'. This confirms the word. The online text shows no origin tag, and the page number of the print edition cannot be mapped.\"}],\n \"consulted\":[{\"src\":\"MON\",\"where\":\"vajehyab.com/moein/آنزیم\",\"stance\":\"supports\",\"note\":\"'[فر.] (اِ.) گروهی از پروتئین‌های کاتالیزی ... زی‌مایه'.\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt grep آنزیم\",\"stance\":\"silent\",\"note\":\"not in Aryanpur.\"}]})\nN.append({\"id\":8,\"lang\":\"English\",\"words\":\"enzyme\",\"verdict\":\"confirmed\",\n \"derivation\":\"English enzyme (1881) comes from German Enzym, coined by W. Kühne in 1877/78 from Medieval Greek énzymos 'leavened' (en- + zūmē). It names the ferment 'in yeast' as opposed to organised ferments. The chart's direct Greek → English arrow is right in substance, with German as the unshown coining language.\",\n \"derivation_fa\":\"انگلیسی enzyme (۱۸۸۱) از آلمانی Enzym است. کونه این واژه را از یونانی میانه énzymos «مایه‌دار» (en- + zūmē) ساخت تا مادهٔ تخمیرکنندهٔ «درون مایه» را نام نهد. پیوند یونانی ← انگلیسی در نمودار در اصل درست است، تنها حلقهٔ آلمانی نشان داده نشده است.\",\n \"sources\":[W+\"ζύμη\"],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference cited for this node.\"}],\n \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 287 s.v. enzyme\",\"stance\":\"supports\",\"note\":\"'enzyme, n., a chemical ferment (biochem.) — G. Enzym, coined by ... Wilhelm Kühne ... in 1878 fr. MGk. énzymos, \\\"leavened\\\"'.\"},AHDyeue]})\nN.append({\"id\":9,\"lang\":\"Latin\",\"words\":\"jŭs\",\"verdict\":\"confirmed\",\n \"derivation\":\"Latin iūs, iūris n. 'broth, soup, sauce' < *yuHs (rhotacism of intervocalic -s- in the oblique iūris). It is a direct cognate of Skt. yūṣ- and OCS jucha, and is distinct from the homonym iūs 'law'. The breve in 'jŭs' is Nourai's typography: the vowel is long (iūs).\",\n \"derivation_fa\":\"لاتین iūs (iūris) «آبگوشت، شوربا، سُس» از *yuHs است و s میان‌واکه‌ای در حالت‌های دیگر به r بدل شده (iūris). این واژه هم‌ریشهٔ سنسکریت yūṣ- است و با iūs «قانون» هم‌آواست ولی یکی نیست. واکهٔ آن در اصل کشیده است. ادعای نورایی درست است.\",\n \"sources\":[W+\"यूष\"],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD 'yeuə-': 'Suffixed form *yū-s- in Latin jūs, juice, broth: JUICE'.\"}],\n \"consulted\":[POK507,WLD199,KLNjuice]})\nN.append({\"id\":10,\"lang\":\"English\",\"words\":\"juice\",\"verdict\":\"confirmed\",\n \"derivation\":\"Latin iūs 'broth' gave Old French jus 'juice, sap' (12th c.), which was borrowed into Middle English c. 1300 as jus/juse. The spelling -ice is later. The meaning widened from 'broth' to 'liquid extracted from fruit, plants'.\",\n \"derivation_fa\":\"لاتین iūs «آبگوشت» در فرانسوی کهن jus «آب میوه، شیره» شد. این واژه حدود سال ۱۳۰۰ به صورت jus/juse وارد انگلیسی میانه شد و بعدها juice نوشته شد. معنا از «آبگوشت» به «آب میوه و گیاه» گسترش یافت. ادعای نورایی درست است.\",\n \"sources\":[W+\"यूष\"],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference cited for this node.\"}],\n \"consulted\":[KLNjuice,{\"src\":\"SKT\",\"where\":\"SKT.txt line 9540 (JUICE)\",\"stance\":\"silent\",\"note\":\"Skeat's OCR around JUICE is garbled. No usable quote.\"}]})\nN.append({\"id\":11,\"lang\":\"Indo-European\",\"words\":\"yeu-dh; yeug\",\"verdict\":\"plausible\",\n \"derivation\":\"PIE *yewdʰ- 'to move violently, fight' (Pokorny 511-512 'jeu-dh- to move swiftly, to fight'; LIV *Hi̯eu̯dʰ-) and *yewg- 'to agitate, be unsteady' (Pokorny 512 'jeug- to wave, unsteady') are both genuine reconstructions. Klein (s.v. jube) and Pokorny's own note to jeu-1 ('originally probably \\\"set in motion\\\"; s. jeu-dh-') treat *yeu-dh- as an enlargement of *yeu- 'mix, stir'. That supports Nourai's arrow from Yeu 3, but Pokorny, Watkins and LIV list them as independent roots, and Cheung finds no IE etymology for *i̯auz at all. Nourai's glosses 'shaken, active, fight' / 'ready to fight' compress these meanings acceptably.\",\n \"derivation_fa\":\"ریشه‌های هندواروپایی *yewdʰ- «به‌تندی جنبیدن، جنگیدن» (پوکورنی ۵۱۱-۵۱۲) و *yewg- «آشفته شدن، موج زدن» (پوکورنی ۵۱۲) هر دو ساخته‌های پذیرفته‌شده‌اند. کلاین و یادداشت خود پوکورنی *yeu-dh- را گسترش‌یافتهٔ *yeu- «آمیختن، به‌هم زدن» می‌دانند، که پیوند نورایی را تأیید می‌کند. اما در فهرست پوکورنی، واتکینز و LIV این‌ها ریشه‌های جداگانه‌اند. پس این پیوند را با احتیاط می‌توان پذیرفت.\",\n \"sources\":[W+\"جستن\"],\n \"ref_check\":[{\"ref\":\"KLN:833\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 450 s.v. jube (page mapping approximate): '... Avestic yuidyeinti, \\\"they fight\\\", yaoshti-, \\\"activity, agility\\\". Arm. yuzem, \\\"I stir up\\\" ... All these words derive fr. I.-E. base *yeu-dh-, \\\"to be moved, to be shaken\\\", which seems to be a dental enlargement of base *yeu-, \\\"to mix, stir\\\"'. This is exactly Nourai's claim.\"},\n  {\"ref\":\"POK:512\",\"status\":\"supports\",\"note\":\"POK_full.txt 'jeu-dh- Meaning: to move swiftly, to fight' Page(s): 511-512; next entry 'jeug- Meaning: to wave, unsteady' (Av. yaozaitī, yaošti-) Page(s): 512.\"}],\n \"consulted\":[{\"src\":\"WLD\",\"where\":\"WLD_Bd1_pages.txt leaves 212-213 = Bd. I pp. 203-204\",\"stance\":\"supports\",\"note\":\"'ieug- \\\"aufregen, unruhig\\\" Av. yaozaiti \\\"regt sich auf (vom Wasser, von unruhigen Ländern)\\\"' and 'ieudh- ... av. yuidyeinti \\\"sie kämpfen\\\"'. They are separate entries, but WP notes that yaošti- may belong with *ieu-dh-.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt line 1196\",\"stance\":\"partial\",\"note\":\"'yeudh-. To move violently, fight. Zero-grade form *yudh-ē- in Latin jubēre, to command ... [Pok. ieu-dh- 511.]'. Listed as its own root, not as an extension of yeuə-.\"},\n  {\"src\":\"IEC\",\"where\":\"IEC.txt leaves 256-257 s.vv. ieudhos, ieugō (1)\",\"stance\":\"supports\",\"note\":\"'ieudhos ... \\\"stir, movement, dash\\\"' and 'ieugō (1) \\\"move, stir, drive; strive\\\" ... Av. yaoz- intr. \\\"stir; be roused\\\"'.\"}]})\nN.append({\"id\":12,\"lang\":\"Avestan\",\"words\":\"yaod, yaošti; yaoz, yaozaiti\",\"verdict\":\"plausible\",\n \"derivation\":\"All the forms are real Avestan, but Nourai's glosses are loose. (a) YAv. yud-/yaod- 'to fight' (yūiδiieiti 'fights', yūiδišta- 'best fighter'; Bartholomae: 'yaod- kämpfen') < *yewdʰ-. (b) yaošti-/yaoxšti- f. 'activity, agility, liveliness' (Pokorny, Klein). (c) YAv. yaoz- 'to be agitated, surge, well up' (yaozaiti, of waters and restless lands; causative yaozaiieiti 'stirs up') < *yewg- (Pokorny 512; Cheung *i̯auz). The senses 'searching' and 'search' are not Avestan. They are carried back from Persian jostan and yūzīdan. Avestan has only 'fight' and 'be agitated'. The forms are right, but two separate verbs are merged and given glosses taken from the Persian.\",\n \"derivation_fa\":\"صورت‌ها همه اوستایی واقعی‌اند، اما معنی‌ها دقیق نیستند. yud-/yaod- (yūiδiieiti «می‌جنگد») به معنای «جنگیدن» و از *yewdʰ- است. yaošti- به معنای «چالاکی، کوشایی» است. yaoz- (yaozaiti) یعنی «به جنبش و آشوب درآمدن، موج زدن» (دربارهٔ آب‌ها و سرزمین‌های ناآرام) و از *yewg- است. معنای «جستجو» در اوستایی دیده نمی‌شود و نورایی آن را از فارسی «جستن» و «یوزیدن» به اوستا بازتابانده است. پیوند کلی پذیرفتنی است ولی معنی‌ها با احتیاط باید خوانده شوند.\",\n \"sources\":[W+\"جستن\"],\n \"ref_check\":[{\"ref\":\"KLN:833\",\"status\":\"supports\",\"note\":\"KLN leaf 450 s.v. jube: 'Avestic yuidyeinti, \\\"they fight\\\", yaoshti-, \\\"activity, agility\\\"'.\"},\n  {\"ref\":\"POK:512\",\"status\":\"supports\",\"note\":\"POK_full.txt p.512 jeug-: 'Avestan yaozaitī \\\"be moved, be excited, spurt up (from the water, from restless lands)\\\", yaošti- \\\"activity, wakefulness, agility, liveliness\\\"'.\"},\n  {\"ref\":\"IEC:446\",\"status\":\"partial\",\"note\":\"Mann's relevant entries are at IEC.txt leaves 256-257 (≈ pp. 482-485, not 446): 'ieugō (1) ... Av. yaoz-, intr. \\\"stir; be roused\\\"'; 'iudhō ... Av. yūiδyei(mi) \\\"fight\\\"'.\"}],\n \"consulted\":[{\"src\":\"BRT\",\"where\":\"BRT.txt line 20972\",\"stance\":\"supports\",\"note\":\"'yaod- V. \\\"kämpfen\\\". Praes. yūiδya- \\\"kämpfen\\\"'. The OCR of the yaoz- and yaoxšti- entries is unreadable.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt pp. 176, 218-219 (*Hi̯aud, *i̯auz)\",\"stance\":\"partial\",\"note\":\"'*Hi̯aud \\\"to fight, struggle (for something), strive, seek\\\" ... YAv. yud- \\\"fight\\\"' and '*i̯auz \\\"to undulate, wave; to be in commotion\\\" ... YAv. yaoz- \\\"to set in motion; undulate, wave\\\"'. These are two separate roots, and neither means 'search' in Avestan.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I pp. 203-204\",\"stance\":\"supports\",\"note\":\"'Av. yaozaiti \\\"regt sich auf\\\"', 'av. yuidyeinti \\\"sie kämpfen\\\"', 'av. yaošti-'.\"}]})\nN.append({\"id\":13,\"lang\":\"Pahlavi\",\"words\":\"jôyšn\",\"verdict\":\"plausible\",\n \"derivation\":\"Pahlavi jōyišn [ywdšn'] is attested. MacKenzie and Nyberg, however, gloss it only as 'eating, swallowing (daevic)', the verbal noun of jūdan/jōy- 'to chew', a different verb. MacKenzie has no Middle Persian simplex 'to seek' (he gives xwāstan). Wiktionary and Cheung trace Persian jostan/joy- straight from Proto-Iranian *Hyawd-, with a Parthian (not Persian) intermediate ywdy- 'to strive for'. Nourai's 'jōyišn: search' rests on Horn no. 419 ('phlv. jōy(i)šn, jōy(i)šnīh (Men.)', from Menant's glossary), repeated by Mo'in. The Middle Persian stage is plausible (cf. Pahlavi wijōyišn 'investigation', Horn's vijōyišn), but the specific form with this meaning is not in the standard modern dictionaries.\",\n \"derivation_fa\":\"پهلوی jōyišn [ywdšn'] گواهی شده است، اما مکنزی و نیبرگ آن را «خوردن، بلعیدن (دیوی)» معنی کرده‌اند و از فعل دیگری، jūdan «جویدن»، دانسته‌اند. معنای «جستجو» برای آن تنها از هرن (شمارهٔ ۴۱۹، به نقل از منان) و معین در حاشیهٔ برهان می‌آید. چونگ و ویکی‌واژه «جستن» را مستقیم از ایرانی باستان *Hyawd- می‌دانند و صورت میانه را پارتی ywdy- «کوشیدن برای» می‌آورند. پس وجود صورتی پهلوی به معنای «جستجو» (مانند wijōyišn «پژوهش») پذیرفتنی است، اما واژهٔ ویژهٔ نورایی در فرهنگ‌های امروزی با این معنی نیامده است.\",\n \"sources\":[W+\"جستن\"],\n \"ref_check\":[{\"ref\":\"BQT:571\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 29 (≈ p. 571-572), footnote 8 to جستن 'جستجو کردن، یافتن': 'اوستا yaod-, yūidyeiti (جنگ کردن). هندی باستان yudh-. پهلوی j…(i)šn «اسشق ۴۱۹»'. Mo'in cites Horn 419 for the Pahlavi form. The OCR of the Latin is partly garbled.\"}],\n \"consulted\":[{\"src\":\"PHD\",\"where\":\"PHD_mackenzie.txt line 2054, 6476; grep 'seek'\",\"stance\":\"contradicts\",\"note\":\"'drāyān-jōyišn [drʾdʾn ywdšn] one who speaks while eating'; English index 'eating ... (daevic) jōyišn'; 'seek xwāstan'. There is no jōyišn 'search'.\"},\n  {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt line 2139\",\"stance\":\"contradicts\",\"note\":\"'jōyišn [ywdšn'] the act of swallowing, eating 53. — V. jūtan.'\"},\n  {\"src\":\"HRN\",\"where\":\"HRN.txt no. 419; no. 227\",\"stance\":\"supports\",\"note\":\"'419. justan \\\"suchen, verlangen\\\", Praes. jōy-em ... aw. yaod-, yūiδy-eiti \\\"kämpfen\\\"; ai. yudh- ... phlv. jōy(i)šn, jōy(i)šnīh (Men.)'; '227. v(i)justan (päz. vajōstan) \\\"forschen, untersuchen\\\" ... v(i)jōy(i)šn'.\"}]})\nN.append({\"id\":14,\"lang\":\"Persian\",\"words\":\"jostan\",\"verdict\":\"confirmed\",\n \"derivation\":\"NP jostan/joy- (جستن، جوی-) 'to seek, search' comes from Proto-Iranian *Hyawd- 'to fight, strive (for), seek'. The present stem is *yaud-ya- > joy-; the past stem is *yud-ta- > just- (d + t > st). Old Iranian initial y- became j- in Persian. Cognates are Av. yūiδiieiti 'fights', Parthian ywdy- 'to strive for', Bactrian ιωλ- 'fight' and Skt. yudh-. The meaning shifted from 'fight, strive for' to 'seek'. The derived forms juyidan (secondary), -ju/-juy as in dânešju 'student, lit. knowledge-seeker', are correctly listed.\",\n \"derivation_fa\":\"«جستن / جوی-» به معنای «طلب کردن، جستجو کردن» از ایرانی باستان *Hyawd- «جنگیدن، کوشیدن برای چیزی، جستن» است. مادهٔ مضارع از *yaud-ya- به «جوی» و مادهٔ ماضی از *yud-ta- به «جست» رسیده است (d+t → st)، و y آغازی ایرانی باستان در فارسی به ج بدل شده است. هم‌ریشه‌هایش اوستایی yūiδiieiti «می‌جنگد»، پارتی ywdy- «کوشیدن» و سنسکریت yudh- «جنگیدن» است. تحول معنایی «کوشیدن، جنگیدن برای چیزی» → «جستن» روشن است. ادعای نورایی درست است و «دانشجو» و «جوییدن» نیز به‌درستی از آن ساخته شده‌اند.\",\n \"sources\":[W+\"جستن\",\"https://vajehyab.com/moein/جستن\"],\n \"ref_check\":[{\"ref\":\"BQT:571\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 29 (≈ p. 571-572) s.v. جستن 'جستجو کردن و یافتن', footnote: 'اوستا yaod-, yūidyeiti (جنگ کردن). هندی باستان yudh- ...'.\"},\n  {\"ref\":\"FFD:47\",\"status\":\"supports\",\"note\":\"FFD_pages.txt [pdf page 52-53] s.v. جستن: 'جست < ایرانی باستان *yud-ta- ... «نبرد کردن» معنی می‌دهد'; 'جوی < ایرانی باستان *yaud-ya- ... در پهلوی اشکانی ywd به معنی «نبرد کردن» آمده است'. The pdf page is not printed p. 47 (offset unknown).\"}],\n \"consulted\":[{\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt p.176 *Hi̯aud\",\"stance\":\"supports\",\"note\":\"'*NWIR: NP justan/jōy- ... \\\"to search\\\" ... PIE *Hi̯eudʰ- \\\"to fight, to set out, move (to fight)\\\" | Pok.: 511 f.'; 'REFERENCES: Horn 1893: 94'.\"},\n  {\"src\":\"HRN\",\"where\":\"HRN.txt no. 419, p. 94\",\"stance\":\"supports\",\"note\":\"'justan \\\"suchen, verlangen\\\", Praes. jōy-em ... aw. yaod-, yūiδyeiti \\\"kämpfen\\\"; ai. yudh-'.\"},\n  {\"src\":\"HUB\",\"where\":\"HUB.txt p. ~151\",\"stance\":\"supports\",\"note\":\"'justan \\\"suchen\\\" von einer Wzl. yudh?'.\"},\n  {\"src\":\"MON\",\"where\":\"vajehyab.com/moein/جستن\",\"stance\":\"supports\",\"note\":\"'(جُ تَ) (مص م.) ۱ - طلب کردن. ۲ - جستجو کردن. ۳ - یافتن'.\"}]})\nN.append({\"id\":15,\"lang\":\"Persian\",\"words\":\"yŭz; yŭzpalang; yŭzîdan\",\"verdict\":\"plausible\",\n \"derivation\":\"NP yuz یوز 'cheetah, hunting leopard' < MP yōz [ywc] 'cheetah, hunting leopard' (MacKenzie). It was borrowed into Ottoman/Chagatai yuz. yuzpalang 'cheetah' = yuz + palang 'leopard' (Wiktionary). yuzidan 'to seek, search' (Mo'in: 'جستن، جستجو کردن') and -yuz 'seeker' in Ferdowsi's razm-yuz 'battle-seeker' (the quoted verse) show a living verb *yōz- 'search, roam'. Horn (no. 1129) and Mo'in compare Av. yaoz- 'be agitated', Arm. (loan) yuzem 'I seek' and Kurd. yūz 'small hunting dog', and explain the animal as 'the seeker' (de Lagarde). That supports the chart. Cheung (*i̯auz) lists the Iranian verb (Parthian ywz- 'agitate', Sogd. ʾʾywz- 'be troubled', Bal. juz- 'move') but neither the cheetah word nor yuzidan, and calls the IE etymology uncertain. Wiktionary stops at MP yōz. The words and meanings are secure. The link to Av. yaoz- is a traditional etymology that is accepted but not proven.\",\n \"derivation_fa\":\"«یوز» (جانور شکاری مانند پلنگ، کوچک‌تر از آن) از فارسی میانهٔ yōz [ywc] «یوز، پلنگ شکاری» است و به ترکی عثمانی نیز رفته است. «یوزپلنگ» از «یوز» و «پلنگ» ساخته شده است. «یوزیدن» به معنای «جستن، جستجو کردن» و «یوز» در ترکیب «رزم‌یوز» فردوسی («جویندهٔ رزم») فعلی زنده به معنای «جستن» را نشان می‌دهند. هرن (شمارهٔ ۱۱۲۹) و معین در حاشیهٔ برهان قاطع آن را با اوستایی yaoz- «به جنبش درآمدن»، ارمنی yuzem «می‌جویم» و کردی yūz «سگ شکاری» سنجیده‌اند و یوز را «جوینده» (جانور شکاری) معنی کرده‌اند. چونگ این واژه‌ها را نمی‌آورد و ریشهٔ هندواروپایی را نامطمئن می‌داند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\":[W+\"یوز\",W+\"یوزپلنگ\",\"https://vajehyab.com/moein/یوز\",\"https://vajehyab.com/moein/یوزیدن\"],\n \"ref_check\":[{\"ref\":\"BQT:2457\",\"status\":\"supports\",\"note\":\"ref_page.py BQT:2457 (vol 4 pdf 540; ocr/BQT/2457.png), s.v. یوز: '... جوینده وطلب کننده باشد - ونام جانوری هم هست شکاری کوچکتر از پلنگ'; footnote 2: '«یوز اسم فارسی فهد است ...» ... قس: اوستا yaoz-, yaozaiti (حرکت کردن ...)؛ کردی yūz (سگ شکاری)، ارمنی yoyz, yuzem «اسشق ۱۱۲۹»'.\"},\n  {\"ref\":\"MON:5272\",\"status\":\"supports\",\"note\":\"Mo'in via vajehyab.com/moein/یوز: 'حیوانی است درنده شبیه پلنگ اما کوچکتر از آن که در قدیم آن را برای شکار تربیت می کردند'; /یوزیدن: 'جُستن، جستجو کردن'. (MON:5272 is in the a'lam volume numbering, which cannot be mapped.)\"}],\n \"consulted\":[{\"src\":\"HRN\",\"where\":\"HRN.txt no. 1129, pp. 252-253\",\"stance\":\"supports\",\"note\":\"'1129. yōz \\\"Jagdleopard\\\" ... vergl. arm. yoyz \\\"das Suchen\\\", yuzem \\\"suchen, untersuchen\\\" (... \\\"die Aufregung, das Wogen\\\" bezw. \\\"aufregen\\\", vergl. aw. yaoz-, yaozaiti sich bewegen, wogen, wallen, Hübschmann No. 214) ... kurd. LW. yūz \\\"kleiner Jagdhund\\\" ... Ursprünglich als Jagdtier \\\"der Sucher\\\" (de Lagarde)'.\"},\n  {\"src\":\"PHD\",\"where\":\"PHD_mackenzie.txt line 5710\",\"stance\":\"supports\",\"note\":\"'yōz [ywc] cheetah, hunting leopard'. MacKenzie gives no etymology.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt pp. 218-219 *i̯auz\",\"stance\":\"partial\",\"note\":\"Cheung lists YAv. yaoz-, Parthian ywz-, Sogd. ʾʾywz-, Bal. juz-, Arm. (LW) yuzem, but no NP yōz/yūzīdan: 'The root has no Skt. correspondence. An IE etymology is uncertain'.\"},\n  {\"src\":\"IEC\",\"where\":\"IEC.txt line 6416 s.v. ieugō (1)\",\"stance\":\"supports\",\"note\":\"'Av. yaoz-, intr. \\\"stir; be roused\\\"; Per. yūzam, -īdan \\\"jump\\\"; LW in Arm. yuzem \\\"stir\\\"'.\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt grep یوز\",\"stance\":\"silent\",\"note\":\"no entry.\"}]})\nN.append({\"id\":16,\"lang\":\"Sogdian\",\"words\":\"â-ywdy\",\"verdict\":\"confirmed\",\n \"derivation\":\"Sogdian ʾʾywδy- (Gharib no. 383, reading ayōδy-?) 'to trouble, take pains' < OIr. *ā-yaud(a)ya-, from *Hyawd- 'to fight, strive'. Old Iranian intervocalic d became Sogdian δ. It is cognate with Parthian ywdy- 'to strive for' and Av. yaod-. Gharib himself gives '<*a-yaud; Av. yaod-; Parth. ywdy', so the Avestan link and the gloss 'struggle, try' match.\",\n \"derivation_fa\":\"سغدی ʾʾywδy- (قریب، شمارهٔ ۳۸۳) به معنای «رنج بردن، کوشیدن» از ایرانی باستان *ā-yaud-ya- و از ریشهٔ *Hyawd- «جنگیدن، کوشیدن» است. d میان‌واکه‌ای ایرانی باستان در سغدی به δ بدل شده است. این واژه هم‌ریشهٔ پارتی ywdy- «کوشیدن» و اوستایی yaod- است. قریب خود همین ریشه‌شناسی را آورده و ادعای نورایی درست است.\",\n \"sources\":[W+\"جستن\"],\n \"ref_check\":[{\"ref\":\"SOD:15\",\"status\":\"supports\",\"note\":\"SOD_pages.txt leaf 80 (≈ p. 14-15) entry 383: ''ywδy- S ... ayoδy ? ©<*a-yaud; Av. yaod-; Parth. ywdy (to)trouble, (to)take pain'.\"}],\n \"consulted\":[{\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt p.176 *Hi̯aud\",\"stance\":\"partial\",\"note\":\"Cheung lists Parthian ywdy- 'to look after; to strive for', Khot. juv-, Bactrian ιωλ-, but not this Sogdian verb under *Hi̯aud.\"},\n  {\"src\":\"SOD\",\"where\":\"SOD_pages.txt line 4849\",\"stance\":\"supports\",\"note\":\"'ayoδy ? ©<*a-yaud; Av. yaod-; Parth. ywdy (to)trouble, (to)take pain'.\"}]})\nout={\"pdf_page\":566,\"book_page\":536,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":[entry]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-566.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-566.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-566.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 566"
}
```


### [2026-10-17T00:40:44.178Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'confirmed': 9, 'disputed': 2, 'transcription_suspect': 1, 'plausible': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 15, 'partial': 4, 'not_checked': 3}
books consulted: {'supports': 31, 'contradicts': 7, 'partial': 6, 'silent': 4} | by book: {'KLN': 7, 'CHEUNG': 7, 'HRN': 5, 'WLD': 4, 'AHD': 3, 'ARY': 3, 'POK': 3, 'HUB': 2, 'BRT': 2, 'SOD': 2, 'SKT': 2, 'MON': 2, 'IEC': 2, 'PHD': 2, 'BOOK': 1, 'NYB': 1}
```


## [2026-10-17T00:41:01.084Z] TOOL CALL #68: SubagentHandback

```json
{
 "message": "I verified page 566 (book page 536) and wrote `/home/sfmqrb/git/rishe-private/data/verification/page-566.json`. `verify_check.py 566` reports 0 PROBLEM lines, with all 16 nodes verified.\n\n**Verdicts:**\n- **Root (Yeu 3):** 1 entry, confirmed: PIE *yewH- \"mix food\" (Pokorny 507, Walde-Pokorny I 199, AHD yeuə-).\n- **Nodes:** 9 confirmed, 4 plausible, 2 disputed, 1 transcription_suspect.\n- The four redirect entries were skipped.\n\n**Disputed:**\n- **Persian jŭšîdan (#2):** Horn (no. 430), Hübschmann and Mo'in (Borhan-e Qate' p. 600) link it to Skt. yūṣ- \"broth\", which is where Nourai gets it. Cheung (*i̯ah), Wiktionary and Aryanpur put jōš/jōšīdan under PIE *yes- \"to boil\", a different root. The arrow from Sanskrit is also only a cognate relation.\n- **Avestan yaěš (#3):** the word yaēš- \"to boil\" is real, but it belongs to *yes- (Cheung, Bartholomae, Horn no. 420), not to *yeu- \"mix\". The Sogdian child βyʾys- (#4) is a correct derivation from it, so that edge is confirmed, but it sits under the wrong root too.\n\n**Transcription_suspect:**\n- **French \"ensyme\" (#6):** the printed page shows \"ensyme\", so this is Nourai's misprint for \"enzyme\" and the JSON is faithful. The French word itself comes from German Enzym, coined by Kühne in 1878. The page PNG is saved at `data/verification/sources/refs/ocr/BOOK/566.png`.\n\n**Plausible, worth a look:**\n- **Pahlavi jôyšn \"search\" (#13):** MacKenzie and Nyberg gloss jōyišn only as \"eating (daevic)\". The \"search\" meaning rests on Horn no. 419 and Mo'in.\n- **Persian yūz / yūzīdan (#15):** the link to Avestan yaoz- comes from Horn no. 1129 and Mo'in. Cheung does not include these words and calls the IE etymology uncertain.\n- **Avestan glosses (#12):** \"search\" is carried back from Persian; Avestan has only \"fight\" and \"be agitated\".\n- **yeu-dh / yeug as offshoots of Yeu 3 (#11):** this follows Klein and Pokorny's own note, but Pokorny, Watkins and LIV list them as separate roots.\n\n**Extraction errors:** none in the nodes. One small thing for the owner: the redirect \"Yewo\" is printed \"→ leuo\" on the page, but the JSON has \"Ieuo\" (capital I read for lower-case l). It is a redirect, so nothing there needed verifying."
}
```


### [2026-10-17T00:41:01.534Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
