# Verification process log — verify-page-389


## [2026-09-14T00:49:27.360Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 389 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-389.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-389.json. Write /home/sfmqrb/git/rishe/data/verification/page-389.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 389` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:49:28.255Z] AGENT

I'll start by reading the instructions and the input files.


## [2026-09-14T00:49:29.086Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:49:29.151Z] TOOL RESULT

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


## [2026-09-14T00:49:29.594Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-389.txt"
}
```


### [2026-09-14T00:49:29.621Z] TOOL RESULT

```
1	=== PDF page 389 (book page 359) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pel 1, Ple, Pelu : to fill; a quantity of, a group of  (refs POK:799)
4	#1 (parent #0) [Avestan] refs=POK:799 | par 1, perana : full ; ham-par : to fill together, store ☞Sem 1 ; perana-âyu : full of life ☞Aiw
5	  #2 (parent #1) [Persian] refs=BQT:163,264; FFD:31 | por «پُر» : full ; anbâr «انبار» : storage ; bornâ «برنا» : young | extra: انباردن ، انباشتن
6	#3 (parent #0) [Avestan] refs=AEF:175; BQT:180 | ava-par : fill down ☞Pel 1
7	  #4 (parent #3) [Persian] refs=BQT:180; AEF:175; FFD:31 | obârdan «اُباردن» : to swallow ; obâštan «اُباشتن» : to swallow ; obâsh «اوباش» : a tough or rowdy fellow, a gangster | extra: اوباردن ، اوباشتن
8	#5 (parent #0) [Avestan] refs=POK:800 | frâ 1, fra 1 : plenty ; frâ-yah : more ☞Yah 5 ; fra-ěšta : most ☞Isto
9	  #6 (parent #5) [Pahlavi] refs=SNS:126; BQT:1479; MON:2538 | frây, frěh : plenty ; frěh-est : most, plenty
10	    #7 (parent #6) [Persian] refs=BQT:1479; MON:2537,2538 | fereh, fareh «فِره ، فَره» : plenty, good ; farh-ast «فَرَهَست» : too much, magic
11	#8 (parent #0) [Avestan] refs=POK:800 | paoiry-aěnini : a cluster of stars
12	  #9 (parent #8) [Persian] refs=BQT:395; AEF:372 | parvin «پروین» : a cluster of stars | extra: پَرو ، پَرَن
13	#10 (parent #0) [Avestan] refs=KNT:196; POK:800; IEC:974 | pouru, paourus : much, many
14	  #11 (parent #10) [Persian] refs=IEC:956,974; MON:2508 | farâvân «فراوان» : plenty
15	#12 (parent #0) [Old Persian] refs=KNT:196; POK:800 | paru, parav : much, many ; paru-zana : many kinds of men ☞Gene 1
16	#13 (parent #0) [Germanic] refs=POK | ful-naz : to fill
17	  #14 (parent #13) [English] refs=AHD | full, to fill
18	#15 (parent #0) [Latin] refs=POK | pla-no : full ; pl-us : more
19	  #16 (parent #15) [English] refs=AHD | plenty, plus, manipulate
20	#17 (parent #0) [Greek] refs=None | pol-us : many
21	  #18 (parent #17) [French] refs=None | poly- : multiple, many
22	    #19 (parent #18) [Persian] refs=MON |  | extra: پلی کپی ، پلی تکنیک
23	  #20 (parent #17) [English] refs=AHD | poly-, polygon, polygamy, polynomial
24	
```


## [2026-09-14T00:49:32.463Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-389.json",
 "description": "Read source JSON for page 389"
}
```


### [2026-09-14T00:49:32.505Z] TOOL RESULT

```
{
  "pdf_page": 389,
  "book_page": 359,
  "entries": [
    {
      "root": {
        "name": "Pel 1, Ple, Pelu",
        "lang": "Indo-European",
        "refs": "POK:799",
        "gloss": "to fill; a quantity of, a group of"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:799",
          "words": [
            {"translit": "par 1, perana", "gloss": "full", "script": null},
            {"translit": "ham-par", "gloss": "to fill together, store", "script": null, "see": ["Sem 1"]},
            {"translit": "perana-âyu", "gloss": "full of life", "script": null, "see": ["Aiw"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:163,264; FFD:31",
          "words": [
            {"translit": "por", "gloss": "full", "script": "پُر"},
            {"translit": "anbâr", "gloss": "storage", "script": "انبار"},
            {"translit": "bornâ", "gloss": "young", "script": "برنا"}
          ],
          "script_extra": "انباردن ، انباشتن",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "AEF:175; BQT:180",
          "words": [
            {"translit": "ava-par", "gloss": "fill down", "script": null, "see": ["Pel 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:180; AEF:175; FFD:31",
          "words": [
            {"translit": "obârdan", "gloss": "to swallow", "script": "اُباردن"},
            {"translit": "obâštan", "gloss": "to swallow", "script": "اُباشتن"},
            {"translit": "obâsh", "gloss": "a tough or rowdy fellow, a gangster", "script": "اوباش"}
          ],
          "script_extra": "اوباردن ، اوباشتن",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:800",
          "words": [
            {"translit": "frâ 1, fra 1", "gloss": "plenty", "script": null},
            {"translit": "frâ-yah", "gloss": "more", "script": null, "see": ["Yah 5"]},
            {"translit": "fra-ěšta", "gloss": "most", "script": null, "see": ["Isto"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": "SNS:126; BQT:1479; MON:2538",
          "words": [
            {"translit": "frây, frěh", "gloss": "plenty", "script": null},
            {"translit": "frěh-est", "gloss": "most, plenty", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:1479; MON:2537,2538",
          "words": [
            {"translit": "fereh, fareh", "gloss": "plenty, good", "script": "فِره ، فَره"},
            {"translit": "farh-ast", "gloss": "too much, magic", "script": "فَرَهَست"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "اوی تنبل کند هست را نیست - فرهستش کند نیست را هست",
            "poet": "Abŭ-Nasr Marghzî"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:800",
          "words": [
            {"translit": "paoiry-aěnini", "gloss": "a cluster of stars", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT:395; AEF:372",
          "words": [
            {"translit": "parvin", "gloss": "a cluster of stars", "script": "پروین"}
          ],
          "script_extra": "پَرو ، پَرَن",
          "note": null,
          "quote": {
            "text": "به بالای تو در سمن سرو نیست - چو رخسارتو تابش پَرو نیست",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KNT:196; POK:800; IEC:974",
          "words": [
            {"translit": "pouru, paourus", "gloss": "much, many", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "IEC:956,974; MON:2508",
          "words": [
            {"translit": "farâvân", "gloss": "plenty", "script": "فراوان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:196; POK:800",
          "words": [
            {"translit": "paru, parav", "gloss": "much, many", "script": null},
            {"translit": "paru-zana", "gloss": "many kinds of men", "script": null, "see": ["Gene 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Germanic",
          "refs": "POK",
          "words": [
            {"translit": "ful-naz", "gloss": "to fill", "script": null}
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
            {"translit": "full, to fill", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK",
          "words": [
            {"translit": "pla-no", "gloss": "full", "script": null},
            {"translit": "pl-us", "gloss": "more", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "plenty, plus, manipulate", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Greek",
          "refs": null,
          "words": [
            {"translit": "pol-us", "gloss": "many", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "poly-", "gloss": "multiple, many", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "Persian",
          "refs": "MON",
          "words": [],
          "script_extra": "پلی کپی ، پلی تکنیک",
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 17,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "poly-, polygon, polygamy, polynomial", "gloss": null, "script": null}
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


## [2026-09-14T00:49:33.178Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:49:33.223Z] TOOL RESULT

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


## [2026-09-14T00:50:14.949Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','FFD','AEF','SNS','MON','KNT','IEC','AHD','BRT','PHD','HRN','HUB','ARY','CHEUNG','NYB','WLD','SYN','KLN']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:500])\n    print()\n\""
}
```


### [2026-09-14T00:50:16.021Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verific

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qat

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https:

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/veri

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = pri

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 6

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan m

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.t

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); op

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf onli

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qa

CHEUNG null

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/S

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the
```


## [2026-09-14T00:50:19.969Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pel-, pelə-, plē-\" POK_full.txt | head -20; echo ---; grep -n \"fraēšta\\|frāyah\\|frayah\" POK_full.txt | head -20"
}
```


### [2026-09-14T00:50:20.046Z] TOOL RESULT

```
---
65798:frayah-, Superl. fraesta-^\hQ meiste'; here Iran. *pelu-, *polu-\v\ Plejadennamen npers.
```


## [2026-09-14T00:50:21.364Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\ni=t.find('pel-1')\nprint(len(t))\n\" ; grep -n \"^pel-\" POK_full.txt | head; echo ===; grep -n \"799\\|800\" POK_full.txt | head -5"
}
```


### [2026-09-14T00:50:22.366Z] TOOL RESULT

```
Exit code 1
3967710
(eval):6: == not found
```


## [2026-09-14T00:50:24.584Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '65700,65900p' POK_full.txt"
}
```


### [2026-09-14T00:50:24.632Z] TOOL RESULT

```
etc. and Slavic po/zi. in russ. poloz^ Sledge skid ', slov. p/az'Pflugsohle, stripe'. 

WP. 1516, Trautmann218f., Vasmer2, 396, 397, Kluge-Gotze 197 f. 

References: W P. I 516. 
Page(s): 807, 850 

Root / lemma: pel-1, pela-, ple- 

Meaning: full, to fill; to pour; town (?) 

Note: 

Root/ lemma: pel-1, pels-, ple-\ full, to fill; to pour; town (?), derived from a prefixed pe- + 

Root/ lemma: laku-\ water basin (ditch, lake, sea). 

Material: A. Armenian helum^\ pour from' {*pel-nu-mi), zelum ( *z-helum) " allow to 

stream'. Pass. 'fliefteiJber'; 

cymr. Ilanwxw. 'flood', Verbalnom. Ilanw, llenwr plenitude, Flieften', Middle Breton lano, 
/a/71/ 'flood', corn. /5/7M/es 'fullness, wealth' {*plen-uo-); 

Lithuanian trans, pilu, p/lt/'pour, schijtten, aufschijtten, fijllen', intrans. 'flow', Latvian 
p/let'6np, trickle', p/le'6np', yO///'drip, trickle', pair inundation ', Lithuanian ampalas {*ant- 
palas) 'Aufwasser auf dem Else'; russ. vodo-pol-b(je), pol(n)o-vodbje^Hoc\\\N3iSsef , Old 
Church Slavic po/b ' a small bowl with handles '. 

B. /7e/'castle' in Old \u6\c pur. Gen. puras^ casWe, town, city', pura-u., newer purl-, purl 
ds., compare 5//7^a/0^/''Lowenstadt', gr. (Aeolic) ttoAk; 'castle, town, city, Staat' {*pell-s), 
hom. Cypriot htoAk; ds., Lithuanian pills, Latvian p/Ze 'castle, Schloft' (see Schwyzer, Gr. 
Gr. 1 , 325, 344, Specht KZ 59, 65f., 1 1 f., Trautmann 217). 

C. words for 'swamp, marsh' {pel-, pel-eu^, as osset. farwe, farer^ alder ', Old High 
German fel(a)wa. Modern High German F(9/fc'e/''Weidenbaum' (as 'Sumpfbaum'), and 
Latin palus, -udlsi. 'stehendes water, swamp, marsh, puddle, slop' {*pel-ou-d-), probably 
to Old Indie palvala- n. 'pond, pool' and palvalya- 'sumpfig'; in addition still peiek- : plak- in 



gr. TTakKoq TTr\K6q Hes., naAaaau) (*naAaKiu)) "besphtze', Lithuanian /7e//re'Moorbrucli', 
Old Prussian pe/ky ds., Latvian pe7ce'pudd\e, slop': yO/ac/s 'morass'; after W. Schuize Kl. 
Schr. 112 alle originally color name, also to pe/-8. 

Maybe alb. {*pe-lagu) pe//gu^poo\' see Root / lemma: /aku-: water basin (ditch, lake, sea), 
(common Slavic alb. pe- prefix). 

D. "fijllen, fullness, wealth': Old \nd\c p/part/: p/prma/r, prnati {prnati) 'fijllt, sattigt, 
nourishes, spendetreichlich, beschenkt', also prnoti ds., puryate, puryafe luWt sich', Aor. 
aprat{\ nAnro), Imp. purdhf, Perf. paprau{\ Latin plevl), participle prata-{= Latin -pletus, 
alb. plot, compare also pratf- : Latin com-pleti-d), purta-luW, prana-luW (= Latin plenus, 
Avestan /?'5/75-Tullung', Old lrish//77-a//77"fulle'), purna-^iuW (= Gothic fulls, litt. pilnas. Old 
Bulgarian pl-bni,. Old Irish Ian, from "pe"/- whereas Avestan pa/'a/7a-"gefullt'); pannahu. 
"fullness, wealth' (: Avestan pardnah-vant-'ncW), pan-man- luWness, wealth, Spende' 
( *peld-); Avestan par- "fiJIIen'; 

Armenian //; Gen. llogluW (from *ple-lo-s= gr. nAsux;? or from *ple-to-s= Old Indie 
prata-1), Inum luWe' {*llnum, neologism), Aor. ell-cl fiJIIte'; ///"(/-stem) "fullness, wealth'; 
presumably holom, holonem^hauie auf, sammie an'; 

gr. nipnAriMi "fiJIle' (originally ninAr||Ji, the nasal from niprrpriiJi), Fut. nAnau), Aor. nAr|TO 
"fiJIIte sich', nAriGu) "bin voll, fiJIle myself ', nAr|9oc; n., Ionian nAr|0U(; "bulk, mass', nAr|0uu) 
"bin or werde voll, swell an' (: Latin plebes), nAnapr) "flood', nAnapovr) "AnfiJIIung, satiation 
', TTAna[jiO(; "light fijllend, satiating', nAnpa "FiJIIung' Hes. (: Latin plemlnare^W); hom. 
nA£To(;, Attic nAsux;, Ionian -nktoc, "full' (*nAr|-Li]o-(;; = Armenian //?), nAnpr|<; "full', nAripooj 
"make voir (from *nAr|po-^ = Latin plerus, compare Armenian ///""fullness, wealth', /-stem); 
TTAr|-tJupa, -Mupi<; f. "flood', to pupu) S. 742; 

alb. p/c»/"fuir ( *ple-t-os); also yoye/" beget, gebare'? intrans. "full = pregnant sein'?? with 
formants -^o-here plok, plogu ^heap' {*ple-go-? compare Old High German folc'heap, 
Kriegshaufe, people'. Old English /o/c "troop, multitude, crowd, army, people'. Old 
Icelandic folk'troop, multitude, crowd, people' as *pl-go- or *pel9-go-); 

Latin pled, -e/'e mostly corn-pled, Im -pled luWe' , participle Pass, (com)pletus, plenus 
"full', Umbrian yC>/e'/7e/'"plenis'; plerus, -a, -um'zum groftten parts', plerusque, plerTque^e\r\e 
big, giant number, very much, a lot of, am moisten'; plebes, -e/and -/" plebs, -is 
"Volksmenge; die mass of people in contrast to den Adeligen' {*pled^ues), manipulus'e\r\e 
handful; bundle; Hantein the Turner; Soldatenabteilung' {*manl-plo-s); plemlnare^W to 
*plemen= gr. nAnpa; 



Old Irish ITn(a)im^\ fijlle' (from an Adj. 7/7?= *pleno-s), //77"numerus, pars'; Old Irish Ian, 
acymr. laun, ncymr. Ilawn, corn, luen, leun, len, bret. leun^iuW (= Old \v\6\c purna-eXc), 
Old Irish comalnur^\ fiJIle' (Denom. from comlan^iuW); ^^^/e 'whole', PI. "alle' {*polio-)\ 

Gothic fulls, Old Icelandic fullr. Old English Old Saxon full. Old High German fol{-ll-) 
"full' (= Old Indie /OJ/77a- etc., see above); = Lithuanian pilnas. Old Bulgarian pl-bp-b, Serbo- 
Croatian pun^iuW; about Old English folcetc. see above; Middle High German vlsejen' 
rinse ' to nAn-pOpa above S. 799. 

peA/'bulk, mass', single-linguistically also adjektivisch gewordenes neuter 'much, a lot 
of; besides Indo Germanic pe/u-M\. "much, a lot of; Kompar. ple-jos, -is-, Superl. pla-is- 
/'d-"more, mostly': 

Old Indie puru-, Avestan pouru-, ap. paru^xx\uc\\, a lot of (= gr. noAuc;, if these from 
*naAuc;, Lithuanian pllus), Kompar. Old \v\6\c prayas- My . "moistens, usually ', Avestan 
frayah-, Superl. fraesta-^\hQ meiste'; here Iran. *pelu-, *polu-\v\ Plejadennamen npers. 
parv, Avestan paolryaelnT{*parullainT-), ablaut, gr. flAsiaSsi;, hom. nAr|ia5£(; {*pleull-), 
originally "Sternhaufen'; 

gr. noAuq "much, a lot of (assimil. from *naAu(; = Old Indie puru-), iJbrige case of stem 
TT0AA6-, noAAa-, wohlausgegangen off. *noAFia Old \v\6\c purvf, Kompar. Superl. originally 
*nAr|[i]u)v > nAswv ( *plelsdn) : nAaTaroc; ( *plalsto-), das through influence of *nA£Tc; "more' 
{*plels= Old Irish I/a) and of Kompar. to nAsToTOc; wurde; from a Indo Germanic *pleu-es- 
"UberfluR), big, giant bulk, mass' wurde secondary the gr. Kompar. n. nAsov, wherefore the 
achaische Nom. PI. nAssc; neologism wurde; also wurde Old Latin pious, Latin plus to 
Kompar., and with p/zs- (older Kompar. *ple-les-\n Old Latin pleores, and *plels-\v\ 
Super\.pl/slma) to "yO/o/s- contaminated, from which Latin plurlmus ^{r\ost\y' (old ploirume, 
plouruma, pluslma); compare Benveniste Origines 1, 54 f., Schwyzer Gr. Gr. 1, 537 f., E.- 
M.2 783; 

Old Irish //"much, a lot of (= Gothic fllu), //5"plus, plures' ( *ple-ls); acymr. liaus, ncymr. 
///atys "multitude' {ple-los-fu-s or -to-); 

Gothic fllua6v. neuter m. Gen. (previous Subst.) as replacement from gr. noAu(;, also 
"very; um vieles (beim compounds)', similarly in den other Germanic Sprachen: Old High 
German Old Saxon fllu, fllo. Old English fela, feala, feola^xwuch, a lot of, very'. Old 
Icelandic figl- "much, a lot of, n. "bulk, mass'; compounds Sup. Old Icelandic flelrl, flelstr 
"more, most' {*pla-ls-, -Isto-, Avestan fraesta-); 



Lithuanian /7//^s "in Uberfluft'. 

E. pel-ed-\x\ gr. -nkdboc, n. " dampness, decay ', nAa5ap6(; "liumid, wet', nAaSaw, -av 
"damp sein'; Old High German flediron. Modern High German flattern. Old High German 
fledar-mOs^ba\!\ Latvian pe/det^swm', pe/def/es^ bathe', pe/d/nat^ bathe, schwemmen': 
pildinat {*pld-) ds.; pledinat^\N\tb den Flijgeln hit', pledins^ butterfly'; compare E. Fraenkel 
Mel. Boisacq 1, 357 ff. 

F. words for " butterfly': reduplicated Latin papilio, -onis m. ( *pa-pil-); Germanic *fffaldrdn- 
in Old Icelandic fffrildiu.. Old English fffealde. Old High German fffaltra. Middle High 
German fffalter. Modern High German Falter, Lithuanian peteliskeAs., Latvian peteltgs 
"flatterhaff ( *pel-tel-); 

from the same root the Balto-Slavic words ( *paipala-) for " quail ': Lithuanian pfepalat, 
Latvian pafpala. Old Prussian penpalo (in addition Old Prussian pepelis, PI. pippalins 
"bird'); Czech prepel, krepel, slov. prepelfca {a\so " butterfly') etc. 

G. words for "swing, shake, tremble, hin- and herbewegen' etc.: gr. TraAAco ( *pj-id), Aor. 
£TTr|Aa "swing, brandish, shake', Med. "spring, wriggle ', naAioq "geschwungen', naA|j6(; 
"Zucken, Vibrieren', -ndkoc, m. "lot, fate', naAaaao|jai " loose '; redupl. nainaAAoj Hes. 
"shake'; Old Icelandic /^/a "frighten'. Old English ea/-/^/c»"furchterlich'. Middle High 
German i/a/a/?/ "devil'; perhaps to Old Church Slavic plach-b "trembling, anxious ' ( *polso- 
?), yO/55/// "frighten' etc.; 

the extension pelem-\x\ gr. TTsAeiji^u) "swing, brandish, shatter'. Pass, "erbebe', n6A£|jO(;, 
nT6A£|jO(; "battle, war, fight' (PN N£0-nT6A£tJ0(;, nToA£|jaTo(;), Gothic i/s-/^//775"erschrocken', 
Old Icelandic felms-fullr6s., fe/mta'bange sein' {*falmatjan). Old High German Bavarian 
felm "fright'; 

da Old Icelandic falma likewise "iJberrascht become', as "tap, feel ' stands for, could 
here Latin palpor, -ari {a\so palpd) "streichle', palpito^ twitch ', palpebrae^ eyelids ', alb. 
y05/^/7 "fluttering, trembling' and " maple '. 

Maybe alb. {*palun) panje^ maple ' : Romanian paltin^ maple '. 

as well as West Germanic *fd//an{0\6 High German fuolen. Middle High German fuelen. 
Old English fselan etc.) " feel ' belong, also Middle Low German vlader' maple ', vladarn 
"flutter'. 

References: WP. II 63 ff., WH. 320 f., 322 f., 327 f., Trautmann 218; 



See also: die words under G. could also to pe/-2be\ong; here also p/eu- "flow". 
Page(s): 798-801 

Root / lemma: pel-2a, pelQ- : pla- 
Meaning: to cause to move, drive 

Material: Latin /7e//o (probably from *pel-nd), -ere, pepuli, *pultus^ to beat, strike, knock, 
push, drive, hurl, impel, propel ' (assumed from pultare^ to beat, strike, knock '), pulsus 
{after percu/sus : percelld) " a pushing, beating, striking, stamping, push, blow, impulse, 
stroke ', pulsus, -us^ to beat, strike, knock, push, drive, hurl, impel, propel ', Umbrian ar- 
peltu^ to drive to, move up, bring along, force towards, to move to, move towards, bring 
up, bring near, carry, conduct, drive ', Latin opilio {*oui-pilJd) ' shepherd ', Pales^ an Italian 
goddess of shepherds and pastures '; appello, -are " to drive to, move up, bring along, 
force towards, address, speak to'; 

Old Irish ad-ella {*pel-na-t} " visits ' (= Latin appellat), di-ella^ deviate '; the Futur. to agid 
"drives' : eblaid {*pi-plaseti) and brit. subjunctive with e/- (above S. 307); Old Irish /ae'day' 
( *plaJom), originally *" turn, change of direction or position; change in condition '; about Old 
Church Slavic popelt "ash' see below pel-2tr, 

probably based on o'-present *pel-d-d: Old High German anafalzxu.. Old English anfilte 
n. "anvil, incus'. Old English felt, m.. Old High German filzvn. " Filz ' (*"stomped woolen 
mass '), Old High German falzan ^aniugen, aniegen'. Modern High German falzen^ fold, 
plait, fold up, merge '; 

eine specific gr. meaning- development "anstoften' = "sich nahern, near' probably in 
-nzKac, "near', nsAa^w (Aeolic irAa^u)), n£Aaaaai "sich nahern'; trans, "naherbringen, 
heranbringen' (nsAaas xQovi "warf to bottom'), nsAaTnc; "neighbor, day labourer'; niAva|jai 
" nearer, closer myself ', nAnaiov, Doric nAariov "near, by', Ionian a-nAr|TO(;, Doric a- 
nAoToq "dem man nicht nahen kann, entsetzlich', nAaiK; "wife' (Aryan Ach. 132), £pnAr|v " 
totally near ', nApv, Doric nAav preposition "besides'. 

References: WP. II 57 f., WH. II 276 f.;
```


## [2026-09-14T00:50:33.483Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"parəna\\|parena-\\|pərəna\" BRT.txt | head -30; echo \"=== paoiryae\"; grep -n \"paoiryae\\|paoiryaē\\|paoiryaeinI\\|paoiryaein\" BRT.txt | head -20"
}
```


### [2026-09-14T00:50:33.553Z] TOOL RESULT

```
=== paoiryae
```


## [2026-09-14T00:50:34.964Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ham.par\\|hampar\" BRT.txt | head -20; echo \"=== avapar\"; grep -n \"ava-par\\|avapar\\|ava\\.par\" BRT.txt | head -20; echo \"=== pouru\"; grep -n \"pouru-\\b\" BRT.txt | head -10"
}
```


### [2026-09-14T00:50:35.043Z] TOOL RESULT

```
18334:Komp.;  *fra\*^lay-  f.,  lum  V.  qs-.  —  PQ.: ^u?  .  ,  bis  fräi  hamparsik  /täc  hamfursiin.  — ■)    Zur  Verslärkung   des   Verbalbegritfs ;    die Stelle  hat  geringen  Wert. g./ri^tä:  s.  qs-
=== avapar
15728:väiam  (sd.j  vazaUi  YL  ü.  33;  —  mmsu  (sd.) *°f^fl">(ADm.)a:"ak/?V./p.42.  2)9)  der Reihenfolge  (und  dem  Rang)  nach,  'der erslere':  ttaola  (sd.)  yanya  .  ,  'va/^^  vä naemat  aparät  vä  N._37;  —  yai  ki  avßi •rum'>  ubjyäite  (sA.)  V.j-sa  PQZ.;  —  cva^ haca  'rvaiibya*^  (läxcA.  majaHfya)?  ya%a %rig3im  V.p.  9;  Ä  39; —  aiwUa  apanm (sd.)  apäla  'voHbyai'i  V.iß.^S; — 'rvä^^ äätä  dämqn  aiaonXsY.iÖ.^;  —  upa  vä mq%r?m  sp^niitn  maraSa..  'rutiüa'^  naime asne  apanmca  ".  ,  die  erste  Hälfte  und die  zweite"  V.4.4S;  45;  —  'ruin*>  vä na^m^m  ^yän  apanm  väü.44; — mitAbl.: näirivaite..afimäi  •rum''>  {SSx\.)/ramraomi ya%a  May avB^sd.)^. 4.47.  A)iSTLpcururva als  Adv.  'zuerst';  'rva  hl  tamS  baraiti •n>a  oTannä  Yt/4^36.  3)9)  der  Zeit nach  'der  frühere,  erstere':  Xtyaiy  'ruvä xsäyähiyä  Eh.  4. 9;  —  anuzvarstä^  (sd.) paiü  'rvät^  V.4.  ao;  —  yafärS  *rvS^ uifhistaiti  "qui  prior  surgit"  V.iS.a6;  26, Yt  14.  44');  —  yatära  (sÄ)  vä  als  °rva'> (^Pm.) /räyatmU  Yt.rj.47;  lO.g  (NSf.); —  yahmal  hala  'rvS'ä  snao%S  (sd.)  .  . inalzät  V.2.  32;  —  'rvai'>  (NPol)  täyüm . .  bU^ySima&e  mä  Ä/  'rv5^''  büSiyaifa  nS Y.  p.  2 1 ;  a  I  \  F.  1 3»;  —  iaiärif  'rvö  (NPm.)J* amayäntei^)  V.7.36;37j  —  ava.jasnm (sd.)  -rvqm^  äpB  JaÜiyöt^  .  .  pasiaSa aiwyS  zaohrä  frabarOis  Y.  6^5. 1  o.  a)  Das Praesens  hat  dabei  den  Sinn  der  Ver- gangenheit"); j'?«  Toa^'f  (NPm.)  mihrwt druiinti  "die  zuvor  den  M.  belogen  haben" Yt  10. 45;  —  atibyS  .  .  ysi  vB  vanuhls  . . nHiJ  °rva^  (ASf.)")  äzärayente  "denen, die  euch,  ihr  guten, . .  nicht  zuvor  erzürnt haben"  YLy.30; — tä  sravä  ..yä'rva'^ al^rapalays  dnnjayan  (Sp.  773  o.)  V. 4.45;  —  ä  äim  aoxta..'rv3'*  asavapara.- iri^yB  (PPA.)  ". .  ein  früher  gestorbener Gläubiger"  H.  2.  16.  —  Aber:  ä  dim aoxta  .  .  'rv5''>  drvö  ava.mtrm  (PPfP.) ". .  ein   früher   gestorbener  Ungläubiger"
=== pouru
16221:pouru-baeftaza-
16248:•  j.  pouru-darätar-  m,  'der  vieles  sieht*: °ta  nqma  ahmt  Yt/.  la.
16320:•  ).  pouru-hazaura-  Adj,  {fem.  'rä-)  'viele  I Tausende  betragend':  äat  fralüstnti  .  , fravasayS  paoirll  pouru.sata  ,  .  'ra  .  .  \ pouru.daevans  Ytij.6$i  —  a&a  un}ara\ balsazyä  uzbanm  paoirjl  pouru^ala  . .  °rä  I . .  pouru.baevanS  V.  20. 4.
16325:•  j.  pouru-x^äSra- Adj .  Aavi.pourus.:i^a^ra- ; i)  von  Gottheiten:  'r^m  {statt  NSm.)  bavähi
```


## [2026-09-14T00:50:41.527Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Plejaden\" BRT.txt | head -10; echo \"=== parana\"; grep -n \"parana-\\|parsna\\|p3r3na\\|pjrjna\" BRT.txt | head -20; echo \"=== pouru Adj viel\"; grep -n \"pouru- *Adj\\|pouru-  Adj\" BRT.txt | head"
}
```


### [2026-09-14T00:50:41.630Z] TOOL RESULT

```
15787:•  j.  paoiiyaeini-  f.,  Plur.  Name  eines Sternbilds 'Plejaden':  'yaanyas^a  yazamaide YtÄi2.
15788:Fem.  lu  'yacna-  Adj.,  Ableit.  s.a.s  faoirya-.  — np.  farvin  'Plejaden';    s.  dazu  Hbm.  PSt.  40.
25924:*)  Vgl.  Bd.  2.  7,  5.  I,  j-j.  12,  Zs.  6.  16.  S. gilt  all  Gehilfe  des  Tütrya  bei  der  Reg«n- erieugung,  dem  er  an  Rang  zunichat  steht  (s. •ipa.paoirya-),  sowie  als  Anführer  des  südlichen iDsT.  ZA.  2.  417,  West  SBE.  4^.  161)  Fixstern- himmels  im  Kampf  gegen  den  Planeten  AnaAil iVcnus),  ferner  als  Wächter  der  südlichen  Seen. Vielleicht  ist  derAIdebaran  gemeint,  in  dessen Nähe  sich  die  Plejaden  befinden  (s.^imo'iiÄw-), Gor.  OK.  313  und  West  SBE.  34-  309  gehen von  der  irrigen  Annahme  aua,  S.  sei  der Anführer  des  Westens,  Wieder  ander*  Hi. 62.  12.
=== parana
5859:•  j.  asparana-  m.  Name  einer  Münze*>: °nS  F.  7;  —  duye  AazaaraAe  'nam  nidmat Vd.  6.
7721:•  j.  «rszifyö.parana-  Adj.  'mit  Adler- fedem  besetzt":  isavasca  'na  V.  77.9;  Yt. /0.39,   lOI.
9251:srayä  voumkaiaya  Y,  65. 4;  —  ys  haaiay-j  S/-'^v^'^'jU^'ond''zD"'"w',/irLter ...va  uruassayat  '«o»  Yt,5.  131;  —  ^-i  HriÄ^-^  No^T).  -  mp,  fl'ü.  Tu  V.'s  49" rasmanS  hqm.ststse  (sd.)  ^5  ^'na  ">  J'  karkäi,  vgl.  np.  (Npa,)  kargas. iHndayänti  Yt,  jj.  39;  —  yaoz)nH  »aA'«j.*kahrkäs5.parana-"  Adj. 'mit  Federn •«ff  (NP.)'>  rasmans  Ytio.36.  2)  zeitlich  ^  des  (Vogels)  Kakrklsa  versehen':  isunqm (nur  Komp.).  ^-paranum'^  Yt/o.isg.
15412:ASn.  aus  'parana-  Adj.  'vormalig';  s.  'para, parö.  —  ai.  vgl.  puräriä-  Adj.
15704:•  j.  parana-  n.  1)  'Feder":  mirrjahe  .  . vHrmßnaAe  (sd)    'tarn   ayasaisa   .  .  ana
16082:•parana-
16115:nach   vom    sich   wendend,   sich   weithin  •  j.,  g.  'parsna- Adj. 'gefiillt,  voll':  afriti
16127:rä.:pur  atäs  i  kar  i  däiasiän.  l  •  j.  'parana-  m.,  n.  i)  'Feder':  cataurS
16201:•  '].  pflSö-parana-  Adj.  'des  Federn  weit
17913:frasparana-  1 00a
17931:•  j.  fra-8parana-  Adj.  'mit  den  Füssen ausschlagend':  usirahe..  'noAe  \tl4-ii.
30304:Pü. :  mkirU. •  j.  hu-parana-  Adj,  'wohlbeflügelt':  th dim  ava  nifrävaymte  mqnaym  ahe  ydha nH  jmrr/S  'nS  ". .,  gerade  als  ob  man (es)  ein  wohlgeflügelter  Vogel  wäre"  Yt 13. 70.
=== pouru Adj viel
```


## [2026-09-14T00:50:42.471Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"frayah\\|fraësta\\|fraesta\\|fräyah\" BRT.txt | head -20"
}
```


### [2026-09-14T00:50:42.522Z] TOOL RESULT

```
17769:•  j.  baxsänti  raisla  . .  "frayaha^w8-«i aurvat.aspa^a  .  .  Vytj4-
18219:•  j.  fräyah-  Adj.  (fem.  •yehl-)  1)  'der mehrere,  plus':  nait  aevB  .  .  dva  . .  %rayS .  .  'yanAs  .  .  fra/md  (Sp.  360  u.)  P.  44'^ —  caiti  na  agvahe  pasvB  (sd.)  ..  a^a  dva aha  hryqm  .  .  an/qm  *kahyacit  tdoa *°yaaAqm  '*  ". .  ebenso  bei  zwei,  ebenso bei  drei  . .;  (je)  eins  dann  bei  jedem mthr"  N.  6y,  —  paniasatbl/c'a  . .  *'yJbTs- /a/(sd.).'o">  aAmäjVr.S.i.  a)  'mehr  als geaugiZnvieV :  daAmff  daUya  draona . .'^•yii^ draonä  s^arS  mdhatte  N.  30;  —  daitrm  gSui dragnS ..  *'y?^>  \daitlm\g3its  draonö^ups.- u^mns  N.  jj.  a)  n,  als  SubsL  'Überschuss, Überfluss':  tu  bairyeinte  yaisqm  dim  'ys voAunqm  ".  .  bei  denen  schon  Überfluss vongutenDingenist"  V.j.ag.  2)  ohne kompar.  Bedeutung  'sehr  viel,  sehr  zahl- reich': aal  dl/  ava^jayamahl  'yeAts{APL) Y.  4.  S-  a)  ASn,  °yS  als  Adv.  zur  Ver- stärkung des  Superlativs*':  yaiAe  aztm  *ys tbaysntqm  sraätim  susruye  va^m  "der unter  denen,  die  (mich)  rufen,  die  schönste
```


## [2026-09-14T00:50:52.606Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '16075,16135p' BRT.txt"
}
```


### [2026-09-14T00:50:52.655Z] TOOL RESULT

```
KompE.    —    Zum  V.  'par-.  —  Vgl,  äpfr^tay-.
—  Fü.i  pes  hal  an  läk  ka  S  man  an  i  pa taniik  vilarak^')  äyil,  erl. ;  ras  i  vaAisl  «  döia:^,
—  ')  Beim  lelitcn  Gericht.  —  •)  Also  wie da  p^ilav:   Ganz  wunderlich  DsT.ZA.  7'.3I5.
•  i".  g-  P*ra3«v-  Adj.  (fem.  »äwr-)'* 'breit,  weit':  zqm  '%wim  Y.  lo.  4,  Yt  13. 9; —  yakmya  apS..°%wif(tfP.)..hwax%nü Yt/0. 14;  —  a/  vS  yacjs  zivllfySng  (sd.) aurvats  .  .  'isf  (AP.)  .  .  i^Sng  ".  .  die
dby  Google
893
para^
•parana-
894
Renner,  .  .  die  breiten,  die  starken  .  ." Y.jo,  7.  a)  ASn.  'S«  als  Adv.  'weit- hin': °hu  aipi  (sd.)  YL  8. 40, 10. 44.
KompA.  —  Vgl.  prArwT:  —  au  pi-thäv-  Adj., tfiÄu  Adv.  —  Pü.  (in  Y.  lo):  vitatatämaHä'), (lu  Y,  JO):  ö  vitarai');  aber  im  Komp.:  /ar (Sü, :  /ö^Aü/a^),  /räa*.  —  0  S,  auch  bes.  — *)  In  Folge  von  Verwechslung  mit  J»T>tav-,
■  j.  para^u  Adv.:  s.  pfr3%av;
•  j.  parvd'U.ainilca-,  paraihrainilEa- " Adj.  (fem.  °iä-)  'mit  breiter  Front',  vom Feindesheer:  Aaüiiayä  'kayh  Yt.  5.  131; /.  II,  4.3,Y.().i8.
Pd.  (lu  Y.y. /rä^  änÜ,  {z-aY\.  t):  /rd:^  äaJi (s.  Pol.)  nnd/räj"  ienU.  —  ')  So  nur  Yt  1; $  304  J],  13.
•  j.  par»9Ti.uz'g«r9pta-  Adj.  (fem.  °tä-) 'breit,  weit  entfEÜtet*:  Aa^a  draßayi  (sd.) -/oys  Yt4.3-
Wertlos;  es  b,^\  t>ri%u.ainiiay&  vorher:  s. YL  /.   11.
•  j.  p9r«9*u.drafSa-  Adj,  (fem.  'sä-)  'der ein  breites  Banner  führt':  haOtayaiHa  .  . 'sayä  Yt7.  II.
Pü.!  pur  drafs,  erl.:  tu  dtaß  vas  därind.
•  j.  p»ra9Ti.frava-  m.  'breiter  Klumpen, breite  Scholle':  aitalsqmca  (oäml.  tnaya- nam)  z»mS  °v3il  fra^avata  "und  mit breiten  Klumpen  von  deren  (der  Wasser-
den  Zugtieren  Mi%ras:  münm  . .  ylm  .. '/affiir  vazfrUi  Ytio.  47.
•  j.  p3r«9'u.sraoiiay-  Adj.  'mit  breiten Hüften':  vayuS  .  .  •nisYti5.54.
ai.  pflhiiircnay-  Adj.
•  j.  parvd'u.zrayah-  Adj.  (auch  fem.) 'Qber  weite  Wasserflächen  sich  erstreckend' : ap3mca  'yaahim  (ASf)  Yt  8.  2.
oi.  pfthujräyas-  Adj.
•  j.  paraiHwi-  £  'Oberfläche':  ■a'«(LS.)'> aifiha  amO  "auf  der  Oberfläche  der  Erde"
V.p.2.
Eig.  fem.  zu  firAav.  —  ai.  f^lkvt-  f.  (vgl. pflhivt-  f.) 'Erde'.  —  Pü. :  pa  an  i  vUaraternaiui (so!)  zainii;  vgl.  unter  piti%at/-,  —  ')  Für 'wya  IS  368.  32),  vgl.  ap.  har<J'itvatiyä  und aj.  fflAivydtn;  die  Form  fehlt  S  ■/OÄ
•  j.  par«9Tr'afsman- "  ra.  EN.  eines Gläubigen:  varPsmS.raocä  'afstnS  (statt Gen.)  asaonS  Yx.13.126.
Eig.  Bed.?  —  i)  Wegen  der  Zerlegung  ». pfrAu.i^s'  Mf3,
•  j.  pura^T^-ainika-  Adj.  (fem.  'ks-): s.  unter  pin%u.ainika:
•  j.  'parafrv-araätay-  Adj.  'des  Speer breit  ist  (d.  L  ein  breites  Blatt  hat)':  °lf''> ttqma  ahmt  'lis  nqma  ahmt  Yt.  i§.  48.
VgL  'f?rj%var!tay-  EN.  —   ')  Ktsusansgang  ?
•  j.  'pBraÄT/arätay-  m.  EN.  emes  Gläu-
löcher)  Erde»  soU  er  sich  abreiben"  V.  1  '"^5°  =  ;'^'/  '^^ff'^  ^^  '3-  '<>'■
'  I       Vgl.  'P>rAvar.siay..
Ei.j~Pi.:  m»/^  In  i^mii  pur  /rä^iamMAl'  i-  p9M*vira- Adj.  (fem.  'rä-)  'desEin-
/«(■  i  kanänd,    erL:    xüp  afe  e  kunänd.   —   sicht    weit   ist,    in    die  Weite    geht':    allm
>)   Est.  ZA,  2.  167:    'i  pleine  poignie  Ae\vaauhlm..badazyqm 'rqm  sürqmYX.i-].\.
'*"''•  I      Komp.:/wj^ai"+Wi-a-,'s  368.'\z\  s.  DsT.
.  j.  p»ra^.fräka-  Adj,  (fem.  -kä-)  'weit  I     ^A.  2.  600.    Unrichtiges  bei  Gdk.  3Vt.  95-
nach   vom    sich   wendend,   sich   weithin  •  j.,  g.  'parsna- Adj. 'gefiillt,  voll':  afriti
verbreitend':   andvTm   sBrqm  .  .  °kqm  V.  yä    ütum    (sd)    'mm    hnnaoUi    'nsmHi
05.  i');  —   damayäi  .  .  'kayai  Yt/0.64.   viyiarayeiH  {sA.)  V.  22. 5;  F.  ro;  —  sva.  'zu
*/räia-  n.,   Ableit.  Kai /rini-  wie  aX.  paräiä- ^  yoW^  ZU  reichlich':  zaota   anasava  ..°n?m(^a
a.j.\ii  pdräni-i   vgl./™*«-.  -  PQ.:/^/™.-,^  ,  j,   j/Bwn^  Yt.  JO.  138.        a)  mit
tdb,  erl.;  har  yai  l  andar  lavel.  ^ '1  Hier  u.    ^  ^      '       .  ,  ,..V.,,.,  .
o_  ...    ,,  ,   „       Gen.:  aai.,m  z3  ovat'n€(HSi.y'fiasj'amca
.  ,.  par»aTi.yaona-  Ad,   (fem. '«3-)  'der  ,^^^^„„^^^  v.2.8;  9; - unslnnhch:'««^
eme  breite  Stätte  haf :  ya  (uiml /rava/ayH)   _  _       -  J^^^^^,-^  (^j_    l^^^  y  ^
huyaonä   'nS   Yty.29'>.  KompA.  —   PPfP.  zum  V.  >/ar..  -  nf.  pur.
')  Vgl.  RV./O.  99.3:  prÜHmy6mm..tasa^a.         got./uih;     ai.  vgl.  pürnäÄ.  —   Pu.:  pHrr,  (zu
•  j.  par«9ii.vae8ayana- Adj. 'auf  breiter  '^■)-  ii' ■ .  patkärinä').  —  i)  j  2/2  aE.  — Warte bcfindhch':  tni>>nm..  'ramYLiO.T.       ''  ^-  ^^ ^'"'i'  Sp.  869  o.,  m.
rä.:pur  atäs  i  kar  i  däiasiän.  l  •  j.  'parana-  m.,  n.  i)  'Feder':  cataurS
•  j.  paradiLvarah-  Adj.  'mit  breiter '  °ni '*  vtoärayöis  avi  fa^am  kaiarascit Brust,  breitbriistig':  pay»/,.''z'iir^(NSm)""vier  Federn  sollst  du  verteilen  auf  den YLJ5.54.  ]Weg'*  nach  beiden  Seiten  hin"  Yt/4-44;
")  Nach  der  a-Dekl,    v^ärayeifi    ufastqm    mirr/ohe   *'m^'>
•  j.   para^u.safa-  Adj.   'breithufig',  von  |M?r^i7«aiw  "es  verleiht  Schutz  die  Feder.."
dby  Google
895  p3r«na-  —  'pvitana-  896
YL/4.36.  a)  'Flügel';  jaia    maxsya   — aniarfmar^hasi'a  '«(/w^j.^'' (als  AP.)
•tum  yaiia  vd  'nahe  \,8.22  E^iZ.  ^yasamaide  Yt/. 4.
VgL  fartna-.    —    ')  APn.  mit  fem.  Adj.  vei- '       mp.  (Pü.,V    np-'*  funuak;    u.   igl.  pürnämäs- bunden,  \  4t3.  jd.  —    >>  D.  L  uf  die  freie  I      m.  —  <)  Them.  —  ')  GltPh.  /  b.  196. Suecte    .««heu    den   beiden  Heeren;   e.  I ,  j^  p«r9iiin-  Adj.  'mit  einer  Feder  ver-
```


## [2026-09-14T00:50:57.796Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"füllen\" BRT.txt | head -30"
}
```


### [2026-09-14T00:50:57.844Z] TOOL RESULT

```
2783:xaA/rä  (frö)  i) 'forteilen,  entweichen': ,  Y.  43. 7;  —  kyat  '^wH  xsayqs  {^A^  °hm s.  Ini./rasstö.  2)  'zum  Forteilen,  Weichen  \dy,il  imavanitm  "weil,  wer  es  vermag, bringen":  tia^a  eil  raSva  masya  /«/«/'  deinen  des  mächtigen  Wunsch  erfüllen nasoa  fraeiyeiti  "kein  .  .  vermag  (ihn)  zu  möchte"  Y.4j.  ro";  ■ —  "Ü!  *kasu.draonö töten  noch  zum  Weichen  zu  bringen"  Vt.  (sd.)  jn^a  a^rava  V.J.  45. t4Z^-       3) 'impellere,  anspornen,  dringen      KompE.  —  Zum  V.  a-j-;  aus  ar.  »iwi/a- ;  vgl.
3479:langen zu  — ,  teilhaftig  werden',  mit  Al;k. : voAa  xsa^nm  toi  mazdJ ..  apaimä  vTspai yai'l  Y.41.2^'';  — yaiU  .  .  apan5  äangS.- Jyäinm  ä  xia^rnn  . .  Y.^.s  (s.  bei  ä)*i; —  yaha  aam  avat  3^ar»nS  apayemi  Yt. 5.43.  3)  'treffen', vom Geschoss:  yatUt (aHHf)  tanüm  apaynli\X.io.2\.  4)'(ei- nem  Gebot  usw.)  nachkommen',  sva.  'es erfüllen,  befolgen':  abmaoyahe  .  .  aiiihn äainay&  mas  (sd.)  vaca  da'isanakt  mit iyaohnäis  apayantaAei^  "der  die  Worte . .,  aber  in  seinem  Handeln  nicht  befolgt" Y.p-3i.  s)'(^'°^"i  Gegner,  Akk.)gleich- kommen,  sich  gewachsen  zeigen,  bemei- stem':  äal  mqm  aivs  zaraiustrS  anusm- hm  apayeiti  Yt.77. 19.  6)  '(einem  Ge- räusch usw.  mit  derStimme)  gleichkommen, es  gleichtun  können'  (ohne  Obj.) :  yS  gä'^ä srävayeiü  aps  v3  faiti^-sfatne  (sd.) . .  ye%i .  .  fisit  M>asibya  usibya  aiwisurunvaiU apayät  yezi  apffis(sd.)  ..  "..  wenn  er  (den Vortrag)  mit  seinen  eigenen  Ohren  nicht hören  kann,  soll  er  es  (dem  Geräusch) gleichzutun  versuchen  .  ."  N.  2Ö*'.
4054:Ableit.  —  Eig.  'der  beim  (zum)  Gegenstand seinesWunsches(gelangtlist''.— Pü.!fljafiin(?). --  I)  Zum  o  s.  S  ^94  Nlr. «  j.  afraslh'vant-,  äfrasäh'vant-  Adj. (fem.  'vaili-)  'den  Wunsch,  die  Hoffnung erfüllend,  selig  machend':  a/f«  .  .  afra- satihaitim  V.  52.  i.  a)  mit  Dat  comm.: dsyh  ml  Stars  puhra  ahurahe  mazd$  yS
4056:ml    atfhat    afrasätphä  .  .  vaAishm  ahlim "verleihe   mir,  o  ^.,    Sohn   des   AAM., womit    er  mir  den  Wunsch  erfüllen  soll, das  Paradies  . ."  V.62.6. Eig.  "beatum  (beatos)  babens'  sva.'reddens'').
7562:mit  uPa  'beachten,  (Bitte)  erfüllen'; surunuyä  nS  yasmm  . .  xsnuyä  ns  yasn>m .  .  upa  nS  yasrum  ahlsä  (2SOM-)  "hör auf  unser  Gebet  . .;  lass  dir  unser  Gebet gefaUen,  erfüll  unser  Gebet"  Y.ö'Äg;  Yt. /o.jz  (wo  ahiia^.
7759:•  g.  «razuxSan-  Adj.  'wahr  gesprochenes (Wort)  habend'  sva,  'sein  Wort  wahr  ge- sprochen machend,  es  erfüllend,  haltend': katuntl  (sd.)  ■  .  yi  U  akmai  ■'oil  (NS.)  IUI däiie  ".  .  dem  Mann,  der  es  (das  Ver- sprocJiene)  ihm,  sein  Wort  haltend,  leistet" Y.  44.19-
13369:•  j,   däS"-    V.,    nur    mit    us    'ausfüllen'.
13371:'(ein  Gefäss)  aus-,  bis  oben  anfüllen mit  — '  (Gen.) :  yezi  aahat  (näml,  das  Gefäss) zarmamis  hak?r)t  fi-asnääayfn  maismana gSui  hakint  s^mS  uzdä'kaym  hakirit  apö frasnähaysn  a%a  yaoidayqn  V.  7,  74'',
15309:•  j.,  g.  'par-  V.  'füllen'.  Praes.  3  'fra-^'', 1  pa/r-,  II  p)rm-;  Perf.  *pa/r-.  —  PPfP.
15312:Wunsch)  erfüllen':  aiibyS  ptrina  i,i^lKY>
15317:mit  iam  'füllen  mit  -'  (Gen.):  yS  gTus
17383:•  j.,  g.  buray-  Adj.  "reichlich;  völlig,  voll- kommen': 'uiri  gaos  'uiri  ^an^a  °u:ri vastra  'uiri  anyaHbyS  mazäayasnaübyöyyi. 4^ ;  —  masdä  dadat  ahurS  . .  'ärsis  ä  . . :^'apa^yai  (sd.) . .  Y.  ?7. 2 1.  a)  Akk.  mit 'kar-  'etwas  (Akk.)  völlig  machen  sva. (Erhofftes)  erfüllen  mit-'  (Instr.)":  mat- damüä  'airiiä  ksrt^ä  räitl  isi  xrapaitJ (sd.)  ahmat  hyat  aibl  hyat  mtzditn  . .  V. 40.J.  '        '
17652:•  j.  frat-äp-  Adj.  'die  Wasser,  Gewässer füllend':  mi^rvm  .  .  'Spam  savans.srBttm tat.Hp3m  uxyat.urvanm  Yi.I0.6i,
23012:verrichten, vollziehen,  betätigen;  (eine  Tat)  wendet  Vyt.  55  (wo  ^varShnttm),  3j  (wo begehen':  yaha  ta  f  mSnghUcä  vaocasfs  "varB.jiM);  —  kat  Az  vS  ahm{Sp.xj,Ztn.) dhs!a  vans{7.'Si.)ca  yJ  vohu  Y.j'p.4;  — I  Vj/vg-J/  N.ö";  ^'; — bes.  von  der  Verrieb' ahä  hai  vohü  lai  ffi>3da  (sd.)  wr^«yJ/i7Ä|  timglandwirtschaftlicherArbeit**;  «Ss/ awjw J/  aiifyd  (DaL  comm.)  /racä  vätSyStS  (sd.)  [gavästryJca  varPsnS  *v)r>gmtP^  N.tfo; — ySi Tl  akmäi  ySi  II  vgnzyqn  yahä  (?  astX  '^.\..*gav!lstryaca  vaninh  *v»r3syantB'^.^2. 35.6;  —  tardisuitrahe  ,  .  paoiryji  vohu  — atiqm.,gav3strya*var3ma*vir3*y< mümninäi  .  .  vaokuse  .  .  v3v^r?tuü  Yt.  /fl«"N,A5;  —  vüstre  vfrTzyeil^.ig.^iGL. 13.Z&;  —  vahiihm  .  ,  tat  at  VfifzySmaAl  —  *v?rfzyatqmca^'>  ila  vohu  västrya  Vr. Y.J57;  —  tat  at  vairtmaids  .  .  kyat  l  7j.i.  a)  mit  Dat  der  Person 'Jemandem mainimadila  vaoMmslä  vinztmäls  yä  etwas  antun,  zufügen':  yS  akpm  drpgvaitl gastsil>y3{sA.)var?saitT'^.33.2.  b)  mit praedik,  Akk.  aus  hat^ya-  Adj.  'etwas  wahr machen  sva.  es  leisten,  erfüllen""*:  y^ möi  aiät  Aaihlm  haca  variiaitf  tartüiuiträi hyat  vasnä  /^aiS.t>mim  "wer  mir,  dem Zar.,  gemäss  dem  heiligen  Recht  erfüllt. was  meinem  Willen  am  besten  entspricht" Y.46.  19.  3)  'zeugen':  frataintlmca  h5
23497:'  j'i  K-  "vära-  n.  i)  'Willen,  Belieben': masäa  aia  xsmäk^m  'nm  xinaostmnS  (sd.) Y.4Ö'.  18;  —  yasia  hdi  'rat  rädat  (sd.) y.  5/.  6 ;  —  tsi  'rät  räthntJ  ahurahyä  taosi matdh  "die  erfüllen  den  Willen  des  AhM. zu  seinem  Wohlgefallen"  Y.^.  a;  —  AS. mit  °a  (vanma)  als  Adv.  sbes.  a)  'Aus- lese' (nur  vAbleiL).  (Y.  to.  14:  lies vär7ma.\
25325:i)  'bereitmachen,  bereiten':  tnOimit,. ytiihe  daOta  . .  s^ite  (sd.)  pa%3  ralaiti  YL ro.  68;  —  yS  huäalnS  .  .  vTspa  kansS raoayatiYt.4-9-  a) 'sich  bereitmachen, stellen,  praesto  esse',  nur  mit  DS.  »JrJi'sva. 'Jemands  (Gen.)  Willen  erfüllen':  y!  vahyB vaahius  datdlyasca  fiSt  varäi  radaj  aAurS xia%ra   matda   "der   durch   seine  Macht
25451:•  g.  röid'Wfn  Inf.  'sich  zu  mengen,  zu  er- füllen mit— '(Instr.):^!««  manta*'paouniyB raolshi  r"  i^d^rS  "der  zu  Anfang  sich das  ausdachte:  es  sollen  die  wohligen Räume  sich  mit  Licht  erftiUen"  Y.ji.  7; benutzt  Y.  12.  i.
29175:•  j.,  g.  haiS-ya-,  p.  hasiya-  Adj.  1)  'der Wirkhchkeit  entsprechend,  walir,  echt, recht':  \ya^ä  ima'  's'iyam  naiy  duruxtam (sd.)  adam  akunavam  Bh.4.7;  —  '%im mq%r?m  yim  Aaurvaiäts  asahyä  avt?r3- tatas{&A.ya  Y.ji.ei  —  ai  Sjfj  minghi , . '%Im  asahyä  dqmJm  Y.ji.  8;  —  '^J-J Z'aahuda  (sd.)  yetikl  .  .  Y.  ^Ä  4;  —  yS Tili  >r)tas  savanAö  pa^ä  sisdit  .  .  '^ySng *a  *stl/  ySng  *ä.sai^tl  ahurS  ",  .  die rechten  Wege  . .,  die  wahren,  zu  den  Ge- schöpfen hin,  bei  denen  Ah.  wohnt"  Y. 43-  3 ;  —  drsjd  dtmänl  '%y3  atttan  astayS "im  Haus  der  Vmg  sind  das  die  rechten Gesellen"  \.4g.  11.  a)  praedikativ  mit den  V.  da-  und  ^var3t-  'etwas  (in  der  Zu- kunft liegendes)  wahr  machen,  bewirken, dass  etwas  erwartetes  zur  Wahrheit  wird, es  erfüllen':  ßraslm  (sd.)  vasnä  •'^ytm da  ahäm  \.34.  15;  —  yJ  •  ■  *��i'«  .  . vaniaiti  (Sp.  1376  m.)  .  .  hyaS  vama /»rasSAimtm  Y.  46.  19''.  2)  "wovon man  weiss,  dass  es  künftig  sein  wird,  ge- wiss, sicher':  tä  drygvatö  *mar3daiU  dama *ff7taas' (sd.)  '^fm  Y.jr.  13.  3)  'dem Recht  entsprechend,  recht,  rechtscbaffen':
29188:•  g.  haidyävants'ti-  f.  '(Wahrmachen sva.)  Leisten,  Erfüllen  (des  Geforderten)'; data  flw^Äj'*  arfdatvohü  manat»ha  'tarn hyat  vasnä  firasö.t^tn>m  "der  Schöpft der  Menschheit  fördere  durch  VM.,  da; sie''  erfülle,  was  seinem  Willen  am  besten entspricht"  Y,  50, 1 1 3>.
29190:•  j.  haiS-yä-varazya-  n.  '(Wahnnachen sva.)  Erfüllen':  masUta  ma%ra  .  .  Vimya
29629:.ausfüllen,  complere':  >'aSa  iaha/a  dahmB staota  yesfiya  'va  *daoaiii  "wie  immer  ein
```


## [2026-09-14T00:51:00.379Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '15300,15340p' BRT.txt"
}
```


### [2026-09-14T00:51:00.432Z] TOOL RESULT

```
•  j.  pavant-  Adj.  'hütend,  schirmend, schützend':  avä  °va  (NS.)  pasca  'vii  pars •vä  spa/  vT^aSa  ,  .  frä  *aähe  vJsaiti nivirS  .  .  yakmäi  .  .  Yt  10. 46.
Ableit  (mit  vanl^  aus  '"^pS^y)-  n.  Das  auf- fällige a  setzt  die  Existens  von  Fonnen  wie *kupi,  *kup3Bi  usw.,  nach  der  i-Dekt.,  voraus.
•  j.  *pavitajr-  f.  'Fäulnis,  Venvesung": cvat  antar>  *n)r3ui  aSsa  druxl  y3  nasus axtica  'ti^a  ahitica  fräsnaoiti  "wie  viel . , trifft  die  Drug  . .  mit  Krankheit,  Fäulnis und  Befleckung?"  V.5. 27,
Zum  V.  pav:  —  Vgl.  pülay;  zu  dem  sich *paviüiy'  verhalt  wie  im  Aind.  sämlay-  I.  zu sätäy-  i,  —  Pü.!  paiinjisn  'Bespiengung',  erl. : remanih.  —  i)  So  L  4,  K  1 ;  NA.  pivaf.
•  j.  'par-  V.  'gleich  machen'.  Praes.  4 psra-,  3$  (Pass.)  pairya-.
'vergleichen':  kva  iä  (föä/'j(sd.)  *pair- yeU'^  V.  ig.aj.
mit  aipi  'begleichen  (eine  Schtild)',  ohne Obj.  'Busse  tun':  Aa  hi  asti  B'ha  hä  hl asH  aptnHl  aipi.pänmnäi  ida  alaone nSil  anaipi.panmnäi  drujO  nmaw..  "..das ist  daiiir  die  Sühne  für  den  Gläubigen, der  hier  Busse  tut;  für  den  (aber),  der nicht  Busse  tut  (,  gilt  der  Spruch):  draß\ d^mämmw.  (Y.^i).  iidj"  V.  Ä  107.^
VgL  Sp>T}lay-,  anäp>ri%a-.  —  lat  vgl.^ar  Adj.  I
'gleich'.  —  Pü.  (in  V.  yp);  ku  Hält  däir  api raruiend,  erl. :  \kii)  iSn  äyiin  u  iavHit  tu  yäi, s,  No.;  (tu  V.  S):  ka  apar  pukrik  att,  erl.! ka  apta-  vicärel.  —  >)  So  nach  Jp  I,  Mr2. NA.  hat  pärayänii  (».  auch  Pü.);  doch  beachte man,  dass  kurz  lavOT  zweimal  nipätayania steht,  das  leicht /äi-iij''  vnanlasst  haben  kann. pairy'  ist  jedenfalls  die  lectio  diS".
•  j.,  g.  'par-  V.  'füllen'.  Praes.  3  'fra-^'', 1  pa/r-,  II  p)rm-;  Perf.  *pa/r-.  —  PPfP.
p?r3na'  (sbes.).
'Julien,  voll  machen' :*/r(2n/-".     a)'(einen
Wunsch)  erfüllen':  aiibyS  ptrina  i,i^lKY>
äpanäii{^A.)  käm?m  Y.  2tV.  10.        b)  '(ein
Werk)    vollständig    machen,    vollenden';
/anu.matsisd.)  sf  *aliamai  asayam  *pafre^
*yat  ..  T.iS.
mit  iam  'füllen  mit  -'  (Gen.):  yS  gTus
unihwan  Aqmpä/räiti*'>  "wer  den  Bauch
mit  Fleisch  füllt"  V.^48.
ttL  pptali,  pptiti  i  np.  anb^rad  'er  füllt  ein'.  — Pü.(iuV.3^:  ampa  diänpurr  kambärel kämak, (zu  P.):  ka  . .  kambärel,  erl.:  kuS  .  .  kart,  (lu V.  v)!  ke  pa  göit  unAwar  ö  kam  kambitit istel,  erl.!  jfr.  —  >)  la/raJ.äp-.  fra-  ist  Koinp- Form  zu  einem  al,  *purä-li.  —  »)  Them.;  ai, pfna.  —  i)  Hds.  p/rf.  —  4)  Them.
•  j.  3par-  V.  'verurteilen'.  Praes.  10 pmnav-,  27  (Pass,)  pirya-'\  —  PPfP. parita',  'pfnta',  p>Ia'.
'Jemanden  (Akk.)  zum  Verlust  von  - (Akk.)  verurteilen';  Pass.  'etwas  (Akk.) rechtskräftig  verlieren,  etwas  verwirken': puxtfmcit  (sd.)  ««  andusqm  tanUm  pir- yeHe''>  "..verwirkt  man  den  Leib"  V.4. 17; —  yö  gä'hä  asrävayS  *qsta{sA.)  va  tarS.- maiti  va  lanüm  *piryeiH  N.  .^'"'*;  42'', 45''. 7''j  —  pt^Janus  ianUm  *piryde*^^1 F.  25b;  —  ''piryäe^'i  F.  10.
mit  apa  dnwS.:  yn  ga%ä  asrsvayö  afa tansm  *piTynti^'^''*  N.42.
mit/iwV(dnwS.:/iMÄ  *Äa^ra  *q/rasruiti sl  paiti  tanüm  ^piryäte^  N.  7.
xlfrä  dnwS. :  myasdavh  ratui amyazda- vatt?m  ratunalm  yäUm  (sd.)  gaihanam frapirinaoiti  A.3.  ii^*;  10;  —  myazdava .  .  amyasdavamm  . .  ähsirim  tka^pm  /ra- pirmaoiH  ",  .  verurteilt  . .  den  I^en  zum Verlust  des  ah.  Richters"  .^._j.  12*';  — Pass.:  aaf  i^armö  frapiryäd^^ "^  V.  5.  9 PüZ.
Vgl.  MIO.  LW.  fariavorel  'vernrleilen'  (BB.7. 187)  usw.  (bei  Hbu.  AGt.  t.  22S).  —  Pü. (für  tanüm  firyiili  zu  V.,  N,,  F.);  tanäpuhr tttvit,  (für  piryiti  F.  lo):  apärf-');  Sü.  (für /rap»r>ncuiili):  viikinnayitum,    Npü.!  fari,  i/ür.
ob,Google
851  ^ar-  —  'para  II 2  c  852
/»flu  iatdoH.  —    ')  $  :68.  40.    A'"  steht  V. ' ,  g.  jpgr-  V.  'obstaie'.     Perf.  i  pa/r-.
N, /<.  —  II  Zu  J  jjj  Ko.  —  ii    Die  Worte    "ej^oa:  at  ml yaiä  bjtiävö pafrlmaiistö^'
r  P'  stellen  wohl  eine  erlänlenide  Umsctuei-   jJ  äuIfTTiris  (sA)  Oxsnusä  Y, 4:9.  1.
bnng    des   TOihergehenden /«VVaiwj  vor.  ~         Et?    Ob  in  arm.  ier,  kiL  si;,-ri  •Streit'?  —
•t)  Pü.  eiL:  ^a-wJi  x'i'lak  •  .:,-?!U  Aar  ei  a/är        Fa.:  pinatli,  Sü-;  raiiä.  —  H  Würll.  'Impe-
^Jtr/;  £.  No.6.  —  5>  D.  li.es  wird  ibm  du  Recht  I      diirit  maximns'  sia.  impedtmeDnim  est  maxi-
enlxogep,   einen   Richter   anzurufen,   d.  L  er       mum.
wird  lechtlos ;  Pü.  erl. :  /a  piSi'märän  afar  iti  „
kuti^t  (a    pasemäriH    djlaitin    n/    dahfl.    —    •    j-,     g.    "para    I)    Adv.    'fort,     weg,     ZUI
'^D.i.feni';s.No.4,Npa.undS*LeMA.s-sMAs.   Seite';    'rata   mraciiiis  (sd.)  aoräcä  ya^rä
9.244.     Die  np.  Glosse  wiU  aUerdings  äx',r.      ,„ai„yui  äfTgiatf    knqjal  (sd.)   farä    Y.
•  j.,  g. 'par- V. 'hindurch-,  hinübergehen*,  53-1-         a)}Aw.  in  der  Verbindung  «<-i((Sp.
```


## [2026-09-14T00:51:11.110Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"näyu\\|nayu-\\|p.r.nayu\\|burnä\\|barnä\\|burna\" BRT.txt | head -20"
}
```


### [2026-09-14T00:51:11.204Z] TOOL RESULT

```
8860:amanha  asti  masyd  gfurvaya  hl . .  zUvarp Y.p.28;  —  ai  .  .  mainyßm  zara%uströ v^jtttl  (sd.)  yaste  I  ascil  spSmstd  Y.  43.16; —  ySi  mffi  ahmii  s^rao/^m  dqn  I  cayasla (NP.) "'  upä.jimm  (sd.)  . .  ". .  die  mir  ihm Gehör  schenken,  all  die  .."  Y.415,5;  —  MiSl Spants  mainyti  ,  .  asäunl  cBÜ  (sd.)  yä  3i lelcä  vakistä  .  .  drvgvä  baxhitf  (sd.)  Y. 47.  S ;  verwend.  12.  i ;  — *spaydti  vispa  tä ^aobna  yä  I aca  (APn.)  virxyäti  V.J. 4)  in  negativen  Sätzen  'irgend einer",  mit  der  Negation  'keiner,  niemand, nichts';  im  Ap.  mit  folgendem  (iy\  nur substantivisch:  tnä  Icis  at  vi  dngvatS mq^rqscä  gs/tä  säsnas^ä  (sd.)  Y.31.1S; Mä  läfpaurvö  bäioyalfa  nS  Y.ff.21; 10.123,  /7.54; — mä  lafiars(sd^)  a:vs yat  tristem  V,j.i4;  —  nStt  zi  iü^  aAhä drujs  nyäsäite  (sd.)  FrW.  8.1;  ■ —  naioa jainti  na^a  fraSsyäti  (sd.)  "keiner vermag  . ,"  Hx.  14.^/6;  —  atvahe  . .  zänu.- asti  äfritiS  (sd.)  .  .  "israyqm  naiäa I tti  V.  iS.ii;  —  n3it  cahmi  sasva  (sd.) yS  .  .  FrD._j;  3;  —  mi^r^m  .  .  yü  nffii kahmili  ai7tii.draoxls  Yt.  io.  17;  —  II  mit kasäy  naiy  adari'naus  (sd.)  i  cilay (ASn.)  '^astanaiy  .  .  "wer  immer  es  war, er  wagte  nicht  irgendwas  zu  sagen  .  ." Bh. /.  13,  a)  mit  Gen,  part:  nöit  zt l  eis  asraosyanqm  tanunqm  asahe . ,  viaäiti P.  /j ;  —  mi^rjm  . .  yö  nöit  kahmät  mi'^rS.- drujqm  .  .  aojS  daiiäiti  Yt. /O.62;  62;  — yaiia  vli..yakmai  ttStt  cahmäi  naiitianqm karaiia  (sd.)  pairi.vasnei'^e  Yt. /_j,  3;  — nsit  iahmäi  ap>r»näyunqm  N. //;  —  D  mit Uy:  naiy  aha*  (sd.)  marttyJ'  naiy  pärsi^ .  .  naiy  amäxam  taumäyä  kalay  hyt^  .  . Bh. /.  13,  5)  gAw.  im  Nebensatz  mit yes%   'jeder',    substantivisch:    kadä    valdä
12430:V.  18.  \;  —  axstaäta  'naya  vaca framrü  Y.J.  i;  —  zara'ku/trahe  'nqm  .  . lannsmca  tka^jmca  Y.iÖ.a;  —  vaehä •nyä  FrB.;  —  'nqm'^  ..  dät>m  vTdsyBm  V. /p.  16;  —  mq'hraAe  spmtahe  .  .  'nayä  .  . staolanam  yesnyanqm  "Vt-O-T,  —  'nayä .  ,  dhaurunqs^  rähaßtäs^ä  västryqscä fhtyantd  Y,  y,  3 ;  Vr.  J.  5 ;  —  ytzi  'nyä  . . ai»Aai  (Sp.  270  o.)  Nik.  /;  2;  —  AäyaoidA yä  'na  V.5.21;  j.42,  Yt  JI.  3,  Vyt^j; —  °na  . .  nars  aiaonS  fram>maiti  vUpim dulmatimca  . ,  V.  j,  42;  —  'na  . .  p3r?näyul cihqm  %wfnsaiti  W.j.  41  (?).  a)  meist mit  einem  bestimmenden  Dem.-Proa  oder Adj.;  n)  'a-,  ^ada-,  ima-,  Y.  S.  7,  g.  31, 60.  2,  Vr.5. 3.  Yt  y.  99  (Sp.  2  u.,  3  0-); N.  ji  (Sp.  32  «.);  V.J.  30,  Yt  S.  59  (Sp. 368  u.,  369  u.).  ß)  ähuray-  und  sara-
13076:fi^n/^a-  (sd.):  'mff  zaota  taiiu.p>r3ia  upa.- jrao/ärii  {sd.)  N.j#;  jf)i;  —  y^  hmcU 'maiiqm  \_apjrynäyunqm]i>  aibm  (sd.)  dasli . .  nairiiqm  vä  * aptnnaysk^m  va  astsm dasti  .  .  daivayasnnn  vä  tanu.pirütgm  vä asbtrt  dasti  N. /05;  —  cvai  aisqm  upa.- manaym  (sd.)  . .  cval  "manqm  cvat  tanu.- p^nhanqm  V.  12.  i .
14237:•  j.  drvo.ap9r9näyuka-  Adj,  (fem.  'iä-) 'die  Kinder  gesund  erhaltend':  drväspqm .  .  'kam  Yt-p.  I.
15593:•  j.  pairLtaxtay-  f.  'Henimlaufcn':  °tS (LS.)  paurvaHlya  ya%a  apsrinäyus  "im HerunüaufeD  um  die  beiden  Vorausgehen- den (ist  der  Hund)  wie  ein  Kind"  V,  y.
16158:•  ].  p3r9nayu!9.har3irn-bav-  ItompV.  'der .     KompA. Unterhaltung,  Pflege  seitens  der  J',  teil-  
16748:gruenten praed.  Pron.  poss,  steht  der  Gen. des  Pron.  pers.:  fasava/'  dahyäus  manä abavc^  "drauf  wurde  die  Provinz  mein" Bh._j.2,  4,  12.11  b)  An  Stelle  des  praed. Nom.  steht  ein  Adv,:  axua  . .  bavaAi ya'ha  . .  "so  sollst  du  werden  wie  . ."  Az. 2;  —  i^m  . .  saohrä  bavainti  yas»  iava  . . "was  geschieht  mit  den  Z.,  wenn  .."  Yt. 5'94i  —  ftyat  fta%ra  (sd.)  wawi  bavat ya%rä  . .  Y.30.  9 ;  —  yäü  a  atthus  *paou- ruyU  bavat  'Vie  es  mit  dem  ersten  Leben werden  wird"  Y.  2<¥.  1 1 ;  —  I  adataiy  azdä (sd.)  bavatiy  D.6'.4'; — pasaved  draugc^ vasiy  (sd.)  abav<^  Bh.  i.io;  4-  lo»  16  {wo bly^);l\ —  a An  Aüwat (sd.)  abava/(AMgm.) Y. /p.  159',  c)  Statt  der  kongruenten Num.-Form  des  praed.  Adj.  steht  die  des Neutrums  im  Sing. :  ia'^a  aste  spana  3^ä.- xalmm  (sd.)  bavan  V.  15.  44;  43;  —  apirs- näyu  aAmi  (Sp.aj 6  u.)..yezi  baväm  p?r)- »^^»(sd.)  Yt/9.43(?); — yimS  ..jailyat avat..dazdi  ml ..yatbavani  s^annaiiuhas- ttmsm  tslanqm  Yt/5.  i6(?).  d)  Statt
19037:jAw.;  zu  1);  a)  das  Verbum  ist  indi-  n"^  . .  rta^a.äm  anyqm  . .  Y.  2.  ^y-  —  es kativisch:  n°  data  aAmt  «'  asts  (sd.)  ist  eine  Verbalform  entsprechend  der  des mpntS  .  .  V.  2. 3;  —  «•  As  ao^  pairi.-  vorhergehenden  positiven  Satzes  zu  er^ z'tfSiä»»' V,ip.3;  Yt5.93;  —  n°tatii^ar»nS\gä.ta.ta:  ap)rmäyu  aAmi  n'  p?r)näyu  (sA) pairi.abaom  Yt.7p.57;  —  "^"^  ^^l  n°  pairi.-\Yt  ig.43;  —  /W  äp^m  jainti..n'  avaha Jräsa  (sd.)  .,  *p3r>saAi  . .  Y.p.  25;  —  nava\  m3r>tS  V,5.  37;  38;  —  avi  ''ainyS  *'surun- Al  asti  ciha  .  .  n°  he  asti  yaozdühnm  V.  I  vaili  n'  ainys  N.  24;  P-i?;  —  nisriti 3-39',  —  "'  '?'"  ä^ravöpührim  (sd.) '^aStaAe  ästryeiti  n'  anisriti  N.ii; —  mosu nai^a  *daste  Aapu^nm  Y.70. 15; — na!cisca\tat  äs  n'  darrf>m  Yt5.  65;  —  sumnaoiti aitiAi  (Sp.  8  o.)  yasäiti  xyänäi  n'  snähai  ,*zaeta  upa.sraotara7tqm   n°  *upajraotärS
21571:mainyul,    *sp3ntö.mainyus ,  firinäyul.     -uj  ist
21772:Konj.  im  Sinn  des  lat  Fut  II;  im  über- geordneten Satz  steht  a)  Ind.:  isatv  hä nistata  kiryeiti  y  grantS  mstayeiii  (sd.)  Yt. /o.  109.  b)  Konj.:  y  bavani  ptn- näyu  sqm  caxr^m  kfrtnavane  Yt  ig, c)    Opt:  >"   para    *ha    vaxia^
30095:•  j.  hizu.dräjah-  Adj.  (auch  fem.)  i)  'die Zunge  herausstreckend':  "/?(NStn,",  näml. asti  spa)  ya^a  ap3r)näyus"ei  (der  Hund) streckt  die  Zunge  heraus  wie  das  Kind"
```


## [2026-09-14T00:51:12.594Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"burnâ\\|burnā\\|burna\\b\\|bumâ\" HRN.txt | head -20; echo \"=== HRN anbar\"; grep -n -i \"ambâr\\|ambār\\|anbâr\\|anbār\" HRN.txt | head -20"
}
```


### [2026-09-14T00:51:12.655Z] TOOL RESULT

```
=== HRN anbar
```


## [2026-09-14T00:51:19.564Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '16150,16175p' BRT.txt"
}
```


### [2026-09-14T00:51:19.609Z] TOOL RESULT

```
jährig;    wenn   ich   (erst)    ,  ."   YLjp.43;    —         Aus  •//■/-j*i.;Tgl.  aLa/j-a/a,  I»t./»?Äi>»insw.i
DP.)'I  a-hqm   >W>r>sattt   V.^.43.  |      „\'„    ,.  st.=   ia^n,   ^^  t.:    v<,^ai  (L  np!
KompE.,  A-tmyKomp.).  — Komp.:  'piri»a-Y  .  i^/a).  —  ■)  JusTls  abweichende  Fassone  des ^J,.flt.6).  — ai.vgL/w-wj.ü/-m.EN.(?>  — Pü.:'      Aw.  Worts,   2DMG.  49-  684   halle  ich  nicht
/»/■«äf,    (lU   V.  3):    ä/TcnaiänÜ.     —    ■)    Im :      ft,  richtig;  t.  BthU  IFAni.  S.  16.
J)  S^y.    Unticher.    Oder  auch  MSn.,  ...a.*.   *  *J.,  g- p9r»smana- Adj.,  PPM.:  S.Jras-.
Sp.  276  n.  —  4)  VgL  zu  ^flAu  Y.  13.  4.    S.  I         j.  pisialt  P.  44  -.  lies  pn-isin/e.
übrigens  Pü.  —  s)  VgL  lU  pir>r,ivayam-.    —  I  ,  :  ■*,/„.  Adi    PPfP  ■  s.  JA»/^         \ t>3Ümat
6|  VgL  aber  Bezzksbmgeb  GGS.  18^8.  268.  ,,1  '^  *;  Aaj.,rnr..  s.  par-,  \j>PSfmai _      y .        ft  .  L       .         TT  .j     I  Vt/4.36:  s.  unter  toÄJä«-.]
•  ].  p3r9nayu!9.har3irn-bav-  ItompV.  'der .     KompA. Unterhaltung,  Pflege  seitens  der  J',  teil-  
haftig  werden':  'buyS  . .  ätarl puira  ahu-  *  J"  f""'  ^^l-.  **««  ^ejnandergezogen, /•j>S.  Y.62.2.  -  ausgestreckt,  -  geofcef.
Komp.  -iar/^ra-  Adj.  ^-*ai^;  S  ^63.  -  PiL:         ^"!"F\  T.-k"  ^'  t'^w'    "'    '^^    *^''^' ^      r         ,-    ,     -  „J   ^      _;  '       -    jt  -  .■         Adi.  'aufgeblüht,  offen'.    Wegen  ir.  p  und  «1.
•  j.  paranävayam-  f.  'vollkommene  Ab-  •  ]■  'paäana-  n-,  p«äaiüi-  f.  'Kampf, Wendung,  Abbitte':  -^J  (NS.)  F./o.  Schlachf:  nivanäat(sd.)  apaydH  [..]  "«a
Komp.:    ifirina-^ava^yam:    —    Pü.:   äfrtna-    (IS.)   ^(/Ä  Yt. /rf.  57;  —   SOnSt  Plur.:   /'*
kän  i).  —  I)  VgL  tu  pirinäyii  V.  3.  42.  (näml.  fravasayö)  yüilyanti    'rtOAu   hai'e
■  j.  *p9r9n«inna-  Adj.,  PPM,:  s.  pargt-  osaAi  . .  Yt/^.  67;  23,  27;  —  li  (näml,
mit  No.  4.  fravasayö)   uyräAu   'nähu   upastqm  hmä
KompE.  dähistä  Yty.  17;  37;   —  Anfraaurvalsö
•  j.  p3nnö.mäh-  m.  Gottheit  des  Voll-  (sd.)  vüsi  "nasima  YL5. 131.  a)  mit monds, Vollmondstags: 'OTifwÄ^M  o/aj'fl/wOT  I^k.  'uro  (den  Preis  von)  —':  yat  baväni Oia/ie  ratüm  Y.  2.  8;  —  -mhuhäi''*  Y.  i.  8;   aiwi.vanyh  tii'irya^'antfm  . .  ahmi  (Sp.4  m.)
dby  Google
897
'psäana-
gai^e  'na/iuyts- 109;  "i3i  73-  A)Akk. mit  ae-  'Jemandem  (Dat.,  Gen.)  eine  (sieg- reiche) Schlacht  liefern':  yHi  .  .  dUnubyS at>n  °nä  YtJj.37;  —  yaha  azäni  'na (APn.)  äariiniiahe  YL5. 30;  30'.
KompA.    —    Vgl.  'fiisana-  EK.    —    Zum  V.
/a«/-,  —  ai.  fi/la»i.  f.;  S  Z/^-
•  j.  'pftäana-  m.  EN.  eines  Ungläubigen: iava  vistäspS  .  .  jaiiyat  .  .  bavilni  aiwi.- vanyä  .  .  'rumca  äa^vayasnam  Yt.  5.  log. Vgl. '/wann-?   Dann  Kurinome.    S.  aber  auch
H  3S..  u
```


## [2026-09-14T00:51:20.807Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"bârdan\\|bärdan\\|bardan\" HRN.txt | head -20; echo \"=== parwîn\"; grep -n -i \"parwin\\|parwîn\\|parvin\" HRN.txt HUB.txt | head -20"
}
```


### [2026-09-14T00:51:20.873Z] TOOL RESULT

```
=== parwîn
```


## [2026-09-14T00:51:26.591Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -c HRN.txt HUB.txt; echo \"=== HUB Plejaden\"; grep -n \"Plejaden\\|Plejad\" HUB.txt | head; echo \"=== HRN sample\"; sed -n '1,20p' HRN.txt"
}
```


### [2026-09-14T00:51:26.649Z] TOOL RESULT

```
 688044 HRN.txt
 527491 HUB.txt
1215535 total
=== HUB Plejaden
4939:kahln *Mitgift* = arm. kapSnl?; parvln 'Plejaden' s. oben
=== HRN sample
Google
This is a digital copy of a book that was prcscrvod for gcncrations on library shclvcs bcforc it was carcfully scannod by Google as pari of a projcct
to make the world's books discoverablc online.
It has survived long enough for the Copyright to expire and the book to enter the public domain. A public domain book is one that was never subject
to Copyright or whose legal Copyright term has expired. Whether a book is in the public domain may vary country to country. Public domain books
are our gateways to the past, representing a wealth of history, cultuie and knowledge that's often difficult to discover.
Marks, notations and other maiginalia present in the original volume will appear in this flle - a reminder of this book's long journcy from the
publisher to a library and finally to you.
Usage guidelines
Google is proud to partner with libraries to digitize public domain materials and make them widely accessible. Public domain books belong to the
public and we are merely their custodians. Nevertheless, this work is expensive, so in order to keep providing this resource, we have taken Steps to
prcvcnt abuse by commcrcial parties, including placing technical restrictions on automatcd qucrying.
We also ask that you:
+ Make non-commercial use ofthefiles We designed Google Book Search for use by individuals, and we request that you use these files for
personal, non-commercial purposes.
+ Refrain from automated querying Do not send aulomated queries of any sort to Google's System: If you are conducting research on machinc
translation, optical character recognition or other areas where access to a laige amount of text is helpful, please contact us. We encouragc the
use of public domain materials for these purposes and may be able to help.
+ Maintain attributionTht GoogX'S "watermark" you see on each flle is essential for informingpcoplcabout this projcct andhclping them lind
additional materials through Google Book Search. Please do not remove it.
```


## [2026-09-14T00:51:28.817Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"parvln\\|parvin\\|parvXn\\|parvfn\" HUB.txt | head -20"
}
```


### [2026-09-14T00:51:28.885Z] TOOL RESULT

```
4939:kahln *Mitgift* = arm. kapSnl?; parvln 'Plejaden' s. oben
```


## [2026-09-14T00:51:32.875Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"parv\" HUB.txt | head -20; echo \"=== leaf 50\"; awk 'BEGIN{RS=\"\\f\"} NR==51' HUB.txt | head -60"
}
```


### [2026-09-14T00:51:33.942Z] TOOL RESULT

```
356:schieden) gehorte nicht zu d. Sperling^ got. sparva etc.,
458:patita-), das ich in np. past parvus, depressus, planus,
897:209. Np. barnl Vas parvuin (unbelegt^) ist natiirlich nicht
1333:Es gehort also nicht zu np. parvdr 1) 'Mastvieh*,
1335:sicher zu parv(lra^ parvdrl gemastet, fett*, parvardan
1337:deutung und Etymologie von hebr. parbdr, parvdrtm
1338:*) Dazu nach Fr. Miiller aram. parvara ^Vorstadt, Vorhof*
1344:im Neupersischen *barvez anstatt parvez Victor, felix,
1355:= ap. *paruviyaini' = np. parvm?
1610:tar *ein Vogel' (avis parva, parum quiescens et canora',
4939:kahln *Mitgift* = arm. kapSnl?; parvln 'Plejaden' s. oben
5135:ap. *prviya' = arisch *prvya' wie auch fiir ap. ^parviya- = arisch
5817:H. 262; bSva Wittwe H. 268; parvezan *Sieb' H. 249; paroar
5818:*Stair H. 304: parvus: 'Flug' H. 305; parvez *siegreich' H.
6271:np. Savur als Var. bei Vullers; parvez Victor, felix*
6321:Aprvez bei Sebeos = paz. awarvS^, phi. aparvBj Shk.
8253:Also np. parvez = arm. AprvSz (oben p. 40 und § 69)
10633:parvdr 39.
10634:parvez 40, 177.
=== leaf 50
— 40 —
ist unsicher; de Lagarde, Btrg. z. bactr. Lex. p. 55
ist schwerlich im Recht.
307. Fr. Muller WZKM. 6, 352 bemerkt mit Recht, dass
man fiir paz. awarvez Shk. 233 = arm. AprUSz (= Aprv^)
im Neupersischen *barvez anstatt parvez Victor, felix,
fortunatus' erwarten miisste. Ist es beeinflusst durch
p^rdz Victor, felix, faustus ?
308. Ich kann die ihrem Sinne nach zusammengehorigen
Worter (ZDMG. 44, 560) lautgesetzlich nicht ver-
einigen. Darmesteter liest mit Westergaard
paoirySnyaS' (von paoiry^i- aus *pdrvydni-^ vgl. afgh.
pSrune, Geiger, Etym. Nr. 170), das er mit ahuranfs
(von ahurani' ahurisch*) vergleicht und durch *die
(Wasser) des Paoirya (Zend-Avesta II, p. 418) iiber-
setzt. Aber Geldner liest paoirya^iny as- von paoirya^i-
= ap. *paruviyaini' = np. parvm?
309. Np. parhe» 'Enthaltsamkeit, Fasten', parMxtan *sich
enthalten' = paz. pahrez Min. GL 154, phi. pahrSd
'abstinence* GI. and Ind. 88, *Vorsicht* Yatk. i. Zar.
p. 62, Anm. 48, pClhredSnd *sie hiiten, pflegen ebenda
p. 51, Anm. 16. Von dieser Pehleviform fiihrt kein
Weg zu Fr. Muller' s (WZKM. 6, 185) zd. ^paiti-ra^d-
Verlassen*", dem doch nur np. *pairextan entsprechen
wiirde. — Arm. pahrez 'Fasten' ist einmal im 14. Jhd.
belegt.
310. Zd. pairika- schlechtweg durch *Hure' zu iibersetzen,
ist falsch. Die Pairika s sind Teufelinnen, die die
Frommen zu verfuhren und vom rechten Glauben ab-
wendig zu machen suchen; phi. parlk bose Fee'
Bdh. Gl. 108, arm. parik ein Fabelwesen' (Eznik 97, 98),
np. pari 'Fee, EngeF.
312. Die Form piSman u. s. w. ist verkiirzt aus paslman, das
auch ins Afgh. {pa§Tmcin Veuig') iibergegangen ist. Vgl.
paz. poSetnan repentant', paSSmam 'penitence' Shk. 263,
Min. Gl. 157, phi. paSSmdnlh 'Reue* Phi. Min. p. 5, Z. X5,
```


## [2026-09-14T00:51:50.739Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--HRN ambar\"; grep -n -i \"ambar\\|anbar\" HRN.txt | head; echo \"--HRN pur voll\"; grep -n \"pur '\\|pur \\*voll\\|pur Voll\\|'voll'\" HRN.txt | head -20; echo \"--HUB barn\"; grep -n \"barn\\|burn\" HUB.txt | head -20"
}
```


### [2026-09-14T00:51:50.888Z] TOOL RESULT

```
--HRN ambar
358:gegenüber hengäm ; qanbara (S. 227 Zeile 9) gegenüber
1387:anhüstan anhäufen', anhar , anbar(i)sn , anh(ä)rok\pat
1388:(Gemme), arm. LW. awbar, hamhar (davon hambarem),
1389:hambarakapet; ai. sam-r- V^par-.
2927:*) Dazu arm. amparist , ambarisf *unfpomm , gottlos* nach F r.
3303:pa/umpar, d, pexompar; hei, paiyam^ paiyambar (207).
4109:phlv. cambar head-fiUet' (Säy. näSäy. HI, 4).
22243:i hambarakapet 111.
22244:i hambarem 111.
--HRN pur voll
788:41. ägenden 'anfüllen', ägenis^ ägm 'voll'.
2865:LW. kurd. afy. bei. (210) pyr, wa/. sar. pur 'voir.
2871:Pchlevr zusammenfallen , aber pur 'viel' ist hier
3037:318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
6117:sar. spur 'Pflug .
--HUB barn
362:rue, the seed of which is burnt as a charm' = echt
363:afgh. spalanai 'a seed of the wild rue burnt to drive
897:209. Np. barnl Vas parvuin (unbelegt^) ist natiirlich nicht
4182:oder opecak?; burna 'Jiingling' = paz. awarnai Shk. 238,
5037:skr. brhant- ; burna *Jungling' = zd. aperenayii- ; bus 'Hals,
9258:a) rn bleibt in: burna, barnd *Jungling', zd. apere-
10316:barnt 28.
```


## [2026-09-14T00:52:02.674Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1380,1395p' HRN.txt; echo \"=== find leaf\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:1386])\nprint('leaf', t[:idx].count('\\f'))\n\""
}
```


### [2026-09-14T00:52:03.747Z] TOOL RESULT

```
(Bartholomae, ZDMG. 44, 553).
110. enhäz^) 'Genosse, Gemahl, Gemahlin, lumbäz.
Ursprünglich *Spielgenosse*, statt *henwaz? Dann
vergl. np. hä/ten (No. 150).
111. enhästen^) 'anfüllen, anhäufen', Praes. enbär-em,
enhärden, enbär^).
aw. hqm -\- l^par-^ hampäfraiti 'er mästet*; phlv.
anhüstan anhäufen', anhar , anbar(i)sn , anh(ä)rok\pat
(Gemme), arm. LW. awbar, hamhar (davon hambarem),
hambarakapet; ai. sam-r- V^par-.
112. enhoylden>^) 'duften'.
aw. hqm+V^bud', skr. sam -\- [^budh- , allerdings
nur in der Bedeutung wahrnehmen, merken*.
113. en^äm 'Ende', enjamlden, vergl. ferjam,
ap. *hanjäma' 'Ende, Abschluss' ; aw. vergl. henjas-
ente sie (die Conten) werden abgeschlossen* (Geld n er
=== find leaf
leaf 47
```


## [2026-09-14T00:52:10.678Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2855,2880p' HRN.txt"
}
```


### [2026-09-14T00:52:10.718Z] TOOL RESULT

```
kurd. per^ zaza pel 'F]ügel\ firin 'fliegen*; wa/. parr.
^) Auch vd. 5 (28) steht patlrak^ nicht patir, gegen Spiegel,
Trad. Lit. 412.
2J Suffix 'a?it, Partie. Praea.
Ilorn, QrundrisH d. neiip. Fitymolü^i<\ 5— m —
np. per7' soll auch *Blatt' bedeuten, wie ai. parnd- ;
vgl. ebenso g. par^ kurd. per, af;'. pur, bei. pan (442),
wa;^. paU^ sar. porÄ-, si/n. />arjr (aus "^parnaka-).
294. /mr Voll'.
aw. perena- Voll*; phlv. pur; ai. pmrid-,
LW. kurd. afy. bei. (210) pyr, wa/. sar. pur 'voir.
Ich sehe nicht ein , weshalb auch Geiger, Laut-
lehre des BalücT, np. piir 'v o 1 V statt von aw. perena-^
ai. pfirnd' VolF von ap. pan^-, aw. pouru-, ai. puni-
Viel' ableitet, deren Bedeutung nicht passt. Laut-
lich mussten ja allerdings beide Worte schon im
Pchlevr zusammenfallen , aber pur 'viel' ist hier
bereits aufgegeben. Wenn der Kommentar z. B. aw.
pouru.mahrku' mit pnrmarg wiedergiebt, so hat er
voll Tod\ nicht 'viele tödtend' gemeint ; denn anderen-
falls hätte er rasmarg übersetzen müssen.
295. perfuf enden zerstreuen; erschrecken, pergenden,
phlv. pargantan (Bund.).
ap. "^para -\~ y/kan- (?). Der Bedeutungswechsel ist
allerdings sehr auffällig. Vergl. efgenden (No. 103).
296. pertew 'Glanz*.
```


## [2026-09-14T00:52:11.877Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--PHD purr\"; grep -n \"purr\\|abarnāy\\|awarnāy\\|abarnay\\|frāy\\|freh\\|frehist\" PHD.txt | head -30"
}
```


### [2026-09-14T00:52:11.931Z] TOOL RESULT

```
--PHD purr
130:delete ozarak ... padist ... add threat. pad-nigerián ... for cared for, guarded read carefully. add  parisp [plsp | M prysp] wall. ?pid ... add (M pyt). purnay [pwin'd = Av. pərənayu-] adult. add  purr-marg |-mlg| deadly, baneful. raz ... add M rz. add rebas [lyp's | N ~] rhubarb. ?ristag ... add N rasta. add гох [lhw' | N <] rook, castle (chess). sahistan ... read (M shyd, P s‘y-). add sārwār [s ]w I helmet. add  sayistan, say- [ŠKBHWN-tn < A Vškb | P sy-] lie down.
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
365:freh [plyh | N firih] more, much, = fray. ~=biid(ih) [-bwt!, bwtyh] excess.
551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
601:*urwüzistan, urwāz- [”wlw?*c- = Av. urwaza-] rejoice. ~i8n: rejoicing, happiness. uskārdan, uskār- [wsk?l-tn' | J ~, (N sigāl-)] think, consider, discuss. -išn(ih): consideration, reflection. uspurrig (^wspwlyk!] = spurrig. us(t)dfrit Pzs(t)wplyt! = Av. usafriti-] offering. ušahin Pwšhyn! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. uzénag ['wcynk! | N hazina] expense, cost; exit. uzérin ['wz())ylyn! = Av. uzayeirina-] the evening gah. uzidan [wcytn! | M ?wzyd, *zozyh-] go out. uzmüdan, uzmāy- ['sozmwtn! , ”wzm'd-) prove, test, try. ~išn: testing. uzumburd ['wzmbwit! | N zumurrud] emerald. w uzwün [SNA < A If? ;^wzwn! | M ‘zw’n, (N zabdn)] tongue, language Ba ch uzwürdan, uzwār- Pwzw’l-tn! | M *zw'rdn] know, understand. ~išn: understanding; ‘huzwarish’.
1305:complete (a.) bowandag, hangirdig, (u)spurrig.
1307:completeness hangirdigih, spurrigih.
1718:dying purr-gah, widerān.
1779:entire bowandag, (u)spurrig; v. complete.
1829:excess frehbūd(īh).
2060:full purr.
2062:fullness purr-rawišnīh.
2391:imperfect anuspurrig.
2843:moon āyišm, mah; full ~ purrmah; new ~ andarmāh,
2844:more fray, freh, wēš.
2869:much abēr, frāy, freh, was, wasyār; as — as, however — and čand; so — and, čand.
3086:perfect (a.) bowandag, hangirdīg, (u)spurrig.
3089:perfection spurrigih.
4688:frahixtan frahixtag frayádisnig fravādišn frāy frādahišnīh frahist farroxīh farrox lxwah-I xwastant frārāst frārūnīh frārēn frāmēš frūmēš- frāmuštan frahist parrag frch pardāxtan frehbūdīh frehbūd pardāz-
4702:purrgāh EIN purrxwarraht «o 10) poryótkes ^x sv (39 1 pēryētkēšīh “(O ODA 10 purn��y "m 19
4703:purr-rawišnīh A$ y S 10)
4704:purrmāh Ku purrsardag 15 Qa» yes dahint roe to pusyān V 10 pusar ND 10 póstén V yen 10) póst we» 105 рап}, poz So panjah ay S ya) panjag, pēzag 13619 pos- = 74010 pūšīdan Wres“O ve pēšišn VUV puštībānīh «U ye) 43 «650105 pustiban т^” оу S ANA pušt VOU 199 puštag 1100010) püdagih ^t 5120
4709:pēr, purr
4773:spéd spēdag spēdbāg spenāg spóxtan spandan Spandarmad sabuk spul spurrigih spurrig spurdan spūz spēz- spinjānagīh spozgar spūzišn sabz spazg spazgīh spar spar- sprahm sprahmag
4892:māl-, mār- mārāg mārīg mālīdan purr! mārišnūmand mārišn mārdan mehmānīh mehmān
5078:zūr, zūr zoromand zūrgugāy zūrgugāyīh zorig Zurwün zofāy zofāyīh zofr zofrāy zofr-pāyag zanjīr zanišn zētīh, zūdīh zot, zūd wahīgt ant
```


## [2026-09-14T00:52:23.732Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"verschluck\\|verschlingen\" HRN.txt | head -20; echo \"--- HUB obar\"; grep -n -i \"obar\\|öbar\\|ubar\" HUB.txt | head -20"
}
```


### [2026-09-14T00:52:23.788Z] TOOL RESULT

```
744:36. üyärden, ayäriden Verschlingen*.
745:ai. ä + l/^gar- {jacjdrd) verschlingen' ; lat. coräre,
746:wa;^. nez-yar-am verschlingen*.
747:In der Bedeutung Verschlingen' vermag ich das Wort
1569:132. öbäSten anfüllen; verschlingen (d. i. sich anfüllen)*
1573:phlv. avpartan bezw. öpärtan 'verschlingen' (Men., AV.).
8047:gala-; lat. gula; arm. vergl. -kul '-verschlingend' (H.
--- HUB obar
4265:phi. datavar oder datuvar (geschrieben datubar), arm. da-
6327:aparanfan 'Arrnband* = np. abranjan ^), dasUbaranJan ; apa-
6949:dbdsfan *implere', 2) = obartdati 'deglutire', pr. obdraniy phi.
```


## [2026-09-14T00:52:25.366Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--CHEUNG bar\"; grep -n \"ōbārdan\\|obārdan\\|ōbārd\\|obard\" CHEUNG.txt | head -20; echo \"--PHD obardan\"; grep -n \"obard\\|ōbārd\\|ōbār\" PHD.txt | head"
}
```


### [2026-09-14T00:52:25.426Z] TOOL RESULT

```
--CHEUNG bar
881:Langobardian 
2026:"wp Itn /obardan/ 
53485:1.9.2 Langobardian 
--PHD obardan
```


## [2026-09-14T00:52:27.807Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1565,1585p' HRN.txt; echo \"=== HUB 6940-6960\"; sed -n '6940,6960p' HUB.txt"
}
```


### [2026-09-14T00:52:27.860Z] TOOL RESULT

```
von emö nicht ^kaufen*, sondern nehmen* ist (vergl.
lit. imü, ifriti nehmen', air. ein 'nehmen*, ksl. imq,
jpM 'nehmen'); zweitens weil lat. emö auch zu got.
tnman gehört, also seine Urform *^rwö lautet.
132. öbäSten anfüllen; verschlingen (d. i. sich anfüllen)*
Praes. obarem , öbärlden ; öbäs 'Gesindel*, "»JITll^NilN
(Jer. 51, 44).
ap. *6l^;a -f l/'^)ar- (vergl. skr. avapürna") anfüllen';
phlv. avpartan bezw. öpärtan 'verschlingen' (Men., AV.).
133. öreng 'Schmuck (z. B. Vis und Rämin S. 24 Vers 4
V. u.); Thron*.
ap. *avaranga- oder wohl besser '^abiranga- (vergl.
skr. ranga- Tarbe* und auch 'Schauplatz, Theater);
phlv. hil]aürank (statt avrang), AV. 14, 8. (Hörn).
134. euJzen (geschrieben evzen) 'tödtend*, in ser]ewzen
(Sahn. I, 100 Vers 714, 450 Vers 288), hezber\ewzen
(Sahn. I, 356 Vers 659).
aw. aiwi + l/^aw- 'tödten' ; phlv. afzatan (PPGL),
päz. awazadan.
Np. evzendlden der Wörterbücher ist nur eine gram-
matische gelehrte Bildung ; über die Emendation ewzen
=== HUB 6940-6960
Vullers) = zard'ob *Galle' vertreten ist. Siehe oben p. 71.
§ 90. In gewissen Fallen erscheint fiir rt im Paz. und
Np. §t. Diese sind :
angastan = angdrdan *glauben, halten fiir', pr. angdram,
ptc. angdrda (bei Vullers angefiihrt, ohne Beleg), paz. ptc.
angard^) Min. 57, 30 = phi. angart Phi. Min. p. 65, Z. 3,
zd. hanJcarayemi; anhastan — anbardan anftillen', pr. an-
baram^ ptc. anbarda repletus*, alt belegt JKAS. 1894, 443:
anbarda puffed. up with pride', skr. sam/;wraya^i *anfullen*;
dbdsfan *implere', 2) = obartdati 'deglutire', pr. obdraniy phi.
opart Wallowed' Gl. and Ind. 44 = paz. opard Min. kap.
27, 33, Shk. 251; iiber aubos, das nicht hergehort, siehe
oben p. 19; dastan 'halten', pr. daram, paz. ddstan, phi.
ddstan, ptc. dast Gl. and Ind. 182 — 183, nom. act. dastar
Phi. Min. 59, Z, 3 und 5, u. s. w., ap. daragdmig; gumastan
= gumaridan *anvertrauen, iibergebeu', pr. gumdram, ptc.
gumdsta *vicarius u. s. w., paz. gurnard Min. Gl. 93 = phi
gumdrt Phi. Min. p. 52, Z. 4, Bdh. Gl. 225; gudastan pas-
siren lassen (auch guddrdan^ vgl. bugdard Fird. I, 140, 204),
ipr, gnddram; gudastan vorbeigehen {Ruch gadaridan?), pr.
gudaram, ptc. gudasta Vergangen Fird. 1, 140,200, paz. vadard
```


## [2026-09-14T00:52:28.380Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2015,2040p' CHEUNG.txt"
}
```


### [2026-09-14T00:52:28.431Z] TOOL RESULT

```
*AVESTAN: YAv. as.baouruua- '(place) where there is a lot to chew he to eat]’ (Yt 
5.130, Yt 17.7), YAv. baoiriia- ‘chewable [of food]’ (Y 3.3) 

*OLD PERSIAN: ? Gaubaruva <gubr"uv-> PN 'cattle-eater' = Kent: 182b 

*MIDDLE PERSIAN: (+ *aua-) MMP ’wb’r-, BMP ’p’I- /öbär-/ (caus.) ‘to swallow’ 
c DMMPP: 65a f. 

Pres.: IND. 3sg. BMP ’p’lyt /obaréd/, 3р1. MMP ’wb’rynd, BMP ’wp’lynd /6barénd/; Partic.: perf. pass. 
MMP ’wb’rd, BMP ’wp’It /öbärd/, MMP *’wb’ryhyst, Caus.: pres. IND. 3р1. MMP *’wb’rynd; Inf.: BMP 
"wp Itn /obardan/ 

*NWIR: Bal. er-burt/er-bar- ‘to swallow’ (+ prev. er- ‘down’) || (+ *aua-) NP 
auburdan/aubar- ‘to swallow unmasticated’, NP aubäridan (caus.) ‘to ingulf, 
swallow, devour’, NP aubastan/aubar- ‘to devour, swallow’ 

*SANSKRIT: bharv ‘to chew, devour, eat’ (RV) = EWAia II: 252 

9 The Pers. and Bal. forms quoted above may not contain *bar ‘to bring, carry’. The 
semantic discrepancy between the Ir. continuations of *bar and the latter forms 
rather suggest a different root. The sparsely attested root *baru’ appears to be 
exclusively Ш., with no certain IE cognate forms. 


*PIE — > LIV: - | Pok.: 133 f.
```


## [2026-09-14T00:52:41.986Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==30' HUB.txt | head -70"
}
```


### [2026-09-14T00:52:43.231Z] TOOL RESULT

```
— 19 —
124. Vgl. Horn p. 254—256. Danach steht ein neup. ang
*Biene*') fest, aber der etym. Verknilpfung mit lat.
apis, gr. ^/ttntg, ahd. imbi stehen erhebliche Schwierig-
keiten im Wege. — Afgh. gahUna *Honig' halt Geiger
jetzt fiir original 2), im Kurdischen lautet das Wort
auch gwln Socin, kurd. Samml. II, p. 332.
126. Lies skr. Angara^,
128. Ich kann die Begriffe ^unsterblich' und *suss' nicht ver-
einigen und trenne^) daher die W5rter: 1) np. ndS
*grati saporis, suavis, dulcis', n^n *HebIich, wohl-
riechend*, arm. LW. anoi§ wohlriechend, schmackhaft,
angenehm, lieblich'; 2) np. noS 'aqua vitae', nOS^ddru,
nos-giyd antidotum', paz. anos antidote' Shk. 230, phi.
anOs ^Unsterblichkeitstrank' Art. Vlr. 10, 5, and§ak
unsterblich, unverganglich' BE. 4, 45, zd. anaoSa-
unsterblich', arm. LW. anusak unverganglich, unsterb-
lich, ewig*. Np. a/noSa *heir! urspriinglich wohl =
*sei unsterblich*!
131. Darmesteter's Etymologie (avdm *Schuld' = a^a
+ ama, lat. abemptum) brauchte kaum erwahnt zu
werden. Denn einmal liegt die Wzl. am nehmen' im
Arischen nicht vor, ferner passt die Bedeutung: *An-
lehen, Schuld' nicht zur Etymologie, endlich steht die
iranische Grundform nicht fest, da sowohl *apama
(— np. vam, bal. LW. vdm) wie dpama (np. avam,
paz. avam *Anlehen' Min. Cap. 2, 63 = phi. ipam Phi.
Min. p. 8, Z. 1) angesetzt werden kann. Wo findet
sich iibrigens np. ai?flm? Die Form fam siehe J HAS
1894, p. 432.
132. Np. ^obdS" liederlicher Kerl, Gesindel' liegt als LW.
im Afgh. in der Form aubos vor und wurde so wohl
auch im Persischen gesprochen. Dann ist es arabisirt
Oder aus dem Arabischen entlehnt. Vgl. bei Freitag:
*) Vgl. auch jiid. tat. heng *Hummer (Miller p. 85).
•) Vgl. daneben das LW. angalnn bei R a v e r t y und vgl. das L W.
angu§t 'Finger', angustdna *Ring, Fingerbut* neben orig. giUa *Finger*.
') Oegen Fr. M filler, WZKM. 5, 264.
2*
```


## [2026-09-14T00:52:48.743Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==31' HUB.txt | head -25"
}
```


### [2026-09-14T00:52:49.625Z] TOOL RESULT

```
— 20 --
vabaSf pi. aubas ^GesindeF. — Auch Noldeke halt
aubas fiir echt arabisch.
133. Np. . aurang (so , resp. jetzt durdng gesprochen,
Sal. Shuk. p. 7) 'Thron*, nach VuUers mit der
Nebenform afrang und zahlreichen Nebenbedeutungen
(Einsicht, Zierde, Freude, Leben, Betrug etc.) wird
durch ein ap. ^abiranga^ mit Hinweis auf skr. rafiga-
'Farbe, Theater, Schaubiihne nicht erklart.
135. Np. ostdm, ustam *fidus, securus' passt besser zu
skr. ava-sthcL (ptc. avasthita- standhaft, zuverlassig') als
das unter Nr. 83 ebenfalls dazu gestellte dstod^ ustad
'Lehrer, Meister . Aber das hier erwahnte phi. ostam
(Phi. Min. p. 59, Z. 4) scheint *Zuflucht' zu bedeuten
(West: ^support') und konnte verschrieben sein fiir
apastam (Phi. Min. p. 11, Z. 5; 37, 4 v. u.) = alterem
apastan (der Siegel), arm. apastan *Vertrauen, Zuflucht',
vieUeicht = skr. upasthdna- 'Aufwartung, Verehrung'
(Horn p. 266). Doch ist es wohl besser, an der iiber-
lieferten Lesart festzuhalten, das Wort durch *Stand-
ort' zu iibersetzen und mit Horn auf ^avastaman- (vgl.
skr. avasthana- *Verweilen, Verharren') zuriickzufiihren.
Hierher konnte auch paz. dstiyan *the faithful, stead-
fast', dstiydnl ^assurance' Shk. 261 = phi. ostlkdn,
Ganjeshayagan Gloss. 1 ; Dinkart I, Gloss, p. 13 ; V,
```


## [2026-09-14T00:52:56.345Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('AEF'),ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('FFD'),ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('SNS'),ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-14T00:52:57.713Z] TOOL RESULT

```
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
```


## [2026-09-14T00:53:08.317Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor w in ['انبار','اوباردن','اوباش','برنا','پروین']:\n    hits=[i for i,p in enumerate(pages) if w in p]\n    print(w, hits[:20])\nEOF"
}
```


### [2026-09-14T00:53:09.661Z] TOOL RESULT

```
777
انبار [74, 138, 183, 381, 382, 541, 570, 583, 742]
اوباردن [399]
اوباش [104, 134, 374, 460, 709, 722]
برنا [272, 273, 295, 448, 470, 484, 613, 644, 658]
پروین [115, 145, 299, 322, 323, 475, 530, 533, 558, 601, 603, 612, 613, 614, 618, 619]
```


## [2026-09-14T00:53:13.586Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in [381,382]:\n    print('==== leaf',n)\n    print(t[n][:2500])\nEOF"
}
```


### [2026-09-14T00:53:15.365Z] TOOL RESULT

```
==== leaf 381
یوتانی۱ وممنیآن‌بفارسی « سنگه زاییدن آمان
کن » باشد . وآن دانه ایست ساهرنگه بمقداو
جوژبوا. بغایت املی‌وصلب ودشوارشکن: وچون
بجنبانند مفز آن در درون وی صدا کند وآنرا
بشیرازی « کن ابلیس » خوانند نم کاف فارسی
ونون ۰ یعنی خایةٌ شبطان و بعربی حجرالولادة
گوبند . چه هرگاه در زیر زنان آستن دود
کنند زود بزایند و اکر باشیرزنان سح قکنند
وقدری پشم را بدان بیالایند و زنی‌ که نمی زاید
بوفت جماع بخود بر گیرد آستن قود.. گو یف
چونآنرا دردست گیرند وبا کسی مخاصمت کنند
برآ نکس غالب‌آیند .
| ناغاطسی - باغننقطه داربالفکفیده
وطای حطی مضموم بسین بی‌نقطه زده ۰ بونالی
سنکی باشد که چون آنرا بآب بسابند رنگی
مانند خون از آن برآید و با شیر زنان درچشم
چکانند ورم چشم و بیاری آب آمدن از چشم
رانافم‌است» وآن‌را بعربی‌حجر اناغاط یگویند .
افاغلس مه بن غین تقطه دار و لام
وسکون مین بی‌قطه ۰ بیونانی؟ دوایی است که
آنرا بفارسی مرذنگوش وبعربیآ ذان‌الفار گویند,
چه بر ک» آن بگوش موش میماند » باس رکه بر
کزیدگی عغرب مالنده نافم است
افا لیقی - با لام و قاف هر دو بتحتالی
رسیده . بلفت رومی دوابی که انرا انجرء
وتخم آنرا بذرالانجره گویندوبمربی قض‌خوانند.
انبارده
تخم آن مستعمل است . اکر مقدار سه درم از
آن باشیر گوسفند بخورند قوت‌باه دهد » ویضی
گویند انالیقی همان بذرالافجره است .
| ثاهیكف ؟ » با های‌تحتانی رسیدموبدال "
زده . بمعنی ناهمد است که ساره زهره باشد .
اب - بفتح اول و انی و سکون بای
ابجد . بادنجان را گوشد و آن ممروفست؟ »
بافراط خوردن آن جذام د ماع و بی‌خوایی
آورد» و بعضی گویند عرمی است ۱
ی رزن
افلاطون » حصار قلمه و جای محکم ر! کوشد -
انبار 1 ع بفتح‌اول‌بروزن زنگار «بمعی
لبریز و مملو و پر باشد - و فروربختن خانه
و افتادن دبوار و امثال الرا نیز گویندب ویمعنی
خی و خاشاله و فثلة اسان و س رکین خیوانات
دبگر باشد که توده کرده‌باشند و مزارعان‌برزمی
زراعت ریز ند واستخر وتالاب رائیز انبار گوینف
و بکر اول مخفف این بار است
انبادذ گی « بروزن و معنی انباششگی
اک ستتی. ود باه مت نب
| ثباددن ۱ « با دال ابجد بروژن‌وعنی
انباشتن است کهپر کردن و انبار کردن‌چیزی‌باشد
از چیزی دیگر
)۱ چك : ژند ویاژند .
۱ - بونانی2601185 «اشتبتگاس» ش بان 881021115 0استینگاس »0 202
«دزی»,
آلوده. جمما بعنی
داده‌اند ای کردند. ۶ بشت ۱
- بهلوی ۵2۸02۲ 0 از
۴ راك : لك ٩‏ ص۱۹۱ .
4 «مناس ۲۷۵ :
: : انبار) ۳ دن‌یسوند مصدری ۳
==== leaf 382
اتبارش
که پر کرده باشد - و بمعنی پرنسمت و با نعست
هم اجه ات ۵
نبادش! -بروزن‌افزایش. پر کردنی‌را
کوبند . و آن چیزی باشد که جوف درون
چیزبرا بان پر کنند. وأنرا بعربی حشوخوانند.
انبار "سیر وزن دمساز » خومات و رفیق
و همتا را گویند . "
نباشت ۱0 بروزن برداشت ۳ ماضی
انباشتن است ععنی کر و ممل و گرداند ۰
۶ ۵۸۱ ه ۳ > ۳
انباشتی ۲۷ " سبروزن برداشتن,بسنی
پر کردن و مملو گردانیدن و آنبار نمودن باشد .
افیا ۴ - باغی تقطم‌دار .دوزن‌را گوبند
دیگری‌را انباغ باشد .8
اثبان باد - بکر نون و با بای ابجد
بروزن می‌دان‌کار. مردم فربه - و بیکاره وهیجکاره
را گوند ۰
برمی آورند .
اثبر ب بنتح اول وضم الث وسکون‌انی
و رای فرشت » التی باشد از آهن که ز رکران
و مسکران طلا و مس تفته دا بدان گیرند ,وبه
عربی کلوب خوانند .
۱ 1 از انبار شش بوند آسم
و
] ذیر وت ده بروزن‌عنزروت , امیودباشد
و آن میومایست معروف ۵ .
افیره - ینم ات بروزن‌قنجفه «هرجیز
موی رنخته را کونند عموماً وشتر موی ریخثه را
خصوصا ‏ و اسب و شتر آبکش را نز گفتماس
و در عربی شکنبه را گویند - و بمعنی دره کوه
نیز حست ؛ و بفتح ثالث بر وزن حنجره هم
آمفه ات .
اثیست - بروزنک‌بت : نلیط و بته
شده را کومند ۷ .
| ثیسقه - بر وزن برجسته ,هر چي زکه
آن بته و سخت شده باشد و بدشواری وا شود
و حل گردد - و شبر و ماست و خون بستهرانیز
گوبتد ٩‏ .
اثبله - بنتح اول و الث بروزن‌حنظله,
تمر هندی رأگویند و بهندی ابلی خوانتد ۰۷
انیمی ۸ س بکسر ثالث وقتح میم‌بروزن
صف‌شکن , بلفت زند و بازند (۳) انگور باشد
و بعربی علب گویند .
افیق یه - بروزن میغوب . فرش وساط
و گتردنی را گومشه. :
اثبو 4 - بر وزن منصوبه . ماشوره را
گویند - و وله آشابه و مانئد آنرا نیز
کفته‌اند .
۴ - پهلوی ۵:۳۰98۵1, 20۵۵2۵۷
۲
۴ ات ود اون
ت۱۳ تم ستد.
۸ حز2(8021130),
```


## [2026-09-14T00:53:21.892Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor n in [399,484]:\n    p=t[n]\n    print('==== leaf',n, len(p))\n    print(p[:2600])\nEOF"
}
```


### [2026-09-14T00:53:23.117Z] TOOL RESULT

```
==== leaf 399 1949
رل اس
یفکن - و بشم اول ناله و زاربراگویند . *
او باریدن ۱ - بنتح اول بروزن سر
خاریدن ؛ ناجاویده فرو بردن را گویشد و بعری
پلع خوانند ‏ و بمعنی افگندن هم هست-ویضم
اول بممتی ناله و زاری کردن باشد .
5 ۱ ۳۹
او باش ‏ بر وزن افراش » مردم عامی
هیچ نافهمید: )۱( بی‌سرویا و جلف و بر خود
و هتعصصت را گوند ۴ ۰
شش رهپس
پر کردن و افگندن باشد .
او برث ۱ - ینم ناك بر وزن افترد .
بحئی ناجاویده فروبرد و پلع کرد .
او ببس - نم اول وکر الك بر وزن
مونن ؛ خوش و پیوند و قرابت را گونند .
او به شم اول و سکرن انی مجپول
کر ثالث و ظهورها » دام قربه است از فرای
هرات ,
اوج - بفتح اول بر وزن موج » معرب
او گه است که مقابل حضیض باشد ؛ و بلندترین
درجهٌ کوا کب بود و آن نقطهٌملافات سطح‌محدب
فلك باشد از افلاك جزئیةٌسبعة سیاره با حوامل
ایشان - و نام نفمه ایست از عوسیقی؛ و سنی
)۱( چش, چب ۱: نفهملده.
(۳) چك : ژند و یاژند .
آو چت هی - با جیم فارسی و فوفانی
و بای فار سی و میم بروزن تعزل نکن (۲) بلفت
زند و پازد (۳) بمعنی انگشت باشد مطلفًخواء
انگشت پا و خواء انگت دست ۳ .
نام شهر و مدننه‌است :
او چیز ی « بازای هوز بروزن+وسیفی»
بمعنی ماهت و چگونگی چیزی باشد ۴ ۰
او چیز بان- بضم‌اول بروزن‌نوشیروان»
کوه را کو,ند و بعربی جبل خوانند ۷ .
می‌نقطهُ بالف کشیده و کسرلام وتستانی بواورسیده
و بنون زده ۰ بیونانی کرفس کوهی باشد. چهاودا
بمعنی کوه ٩‏ وسالیونکرفس را کویند وتخمآترا
فطرا سالیون خوانند چه فطرا بیو:انی مطلق‌تخم
راگوتد ۸ . ِ"
اودد بقئح اول و سکون انی و کس
تال و دای بی نقطهٌ ساکن » برآدد مدر باشد که
محر نی م گوبند ۰
او دددن * - نم اول و ثاك بروزن
بوبردن » بلفت زند و بازند (۳) سه‌نی‌مردن واز
عالم رفتن باشد ,
: رك : اویر . ۴ عریی » جمع وبش » مقلوب بوش . « محیطالمحیط‎ - ٩
. ۰*۱ ان ۴ - حز ۵620۳۵0 , پپلوی ؛أ5لا208 , انگشت «بونکر‎
۴ - در دسانیر * اوجیژ» و * ارچیز » بمعنی حقیقت د ماهیت چیزی آعده « فرهنگه
۵ رك : او چزی.
۲ - صحیف بونانی
دسائیر ۷۲۳۳ » وآن مجمول «فاب4۷:۱» وترجمةٌ «ماهو» عربی‌است.
۹ ت_ مصحف 6۳۲۵ بونانی بسعنی کوه رك اوداسالبون
0 ه«اشتنکس» . ۸ رد : فطرامالون . ٩‏ - بهلوی۷2۸2۲120
۵ او بار دی رك : اوباردن اوجاق _ اجاق . زک مطخ ء کانون - خانواده‌قبلة
بز رگ «حفتابی ٩۶۷‏ .
==== leaf 484 1359
برحه
بر هه ۱ « بروزن کرعه: مثفب‌درود گری
باش که بدان چوب و نخته سوراخ کنند .
برن ‏ بروزن چمن . ام فصبه‌است در
فر فا ۴ ع بنتح اوز و سکون ثانی و نون
بالف کشیده . جوان و نوچة اول عمر و ظریف
را گونند - و بمعتی خوب و نيك هم هست -
و حنا را نیز کون دکه بردست و پا بندنده وضم
اول هم آمده است .
بر فاخی الستادن » کنابد از اطات
کردن و بلدب ایستادن باشد .
بر فاص ۴ - بروزن کربای, بمعنی‌غافل
و عادان - و غافلی و ناداتی باشد .
بر ناك ۴ « چختح اول بر وزن غمناله ۰
بمعنی برنا است که جوان و نوچةٌ اول عمر باشد
ور حنای دلت و بارا نیز گفته‌اند. و خ‌اوژهم
۱ رك : برماه.
1 نو ای
یعنی آدجه برس رکتابتهار نامها نویستد » وسسربی
القاب و عنوان گویند۷ .
بر ناه » بروزن حمراه » جوان و نوچة
اول عمر را گویشدب وحنای دست و پارا نیز
بر نایشتی - یکر بای حطیو سکون
شین فرشت و فوفانی‌بتحتانی رسیده ۰ بمعنی پشتی
و تعصب باشد چه برنایشتی کردن بمعنی پشتی
کردن و تسب نمودن است . #*
بر فج - فتح اول و انی و سکون نون
و جیم » آن‌باشد اکه سیب کوری‌با بجهت‌ناریکی
دست خور را مر دبوار با جابی بمالند تا وک
بیدا کاند ۷ ْ
پر فاد - بکس اود بر وزنکرفتار .
جوان اراده کنند . ناصر خسرو بلخی کوید :
داسفا ۱ : ۲ س ٩۹۳‏ . اه
۵ مرکب‌از: پیشوند بر (بار) ۳ نامه, ۷2۲-۲۵103
« اسفا ۱ : ۲ص ۱۹۰ . 1 - آمروز نمی دستورعملبکار
رود. ععرب آن «یر نامج». «رزی>.
غله‌است (3201۷3 ۳۷2۵()) که درمازندران. کلان » استراباد.
خوزستان؛ اسفهان وبرخی‌تقاط دیگر ابران ودر هندوسثان شرفی
و ژاين و چن میروید . « فرهنکگ روستابی ۲۶۵ » « کل کلاب
```


## [2026-09-14T00:53:42.614Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--HRN faravan\"; grep -n -i \"ferāwān\\|ferawan\\|firawan\\|frawan\\|fräwän\\|fravan\" HRN.txt HUB.txt | head; echo \"--IEC polu\"; grep -n \"polu-\\|pelu-\\|plēyos\\|plē-yos\" IEC.txt | head -20"
}
```


### [2026-09-14T00:53:42.685Z] TOOL RESULT

```
--HRN faravan
--IEC polu
12664:pelu ‘much, many’. Cf. polu, poluos, peluð, peln-. WP II, 65 Arm. cf. h-olov, i-st. adj. (much, many”, fr. *en-peleu-); Lat. cf. polleo, ere, v. (“be strong’, fr. *pelu- or *polu-, q.v.); OIr. il ‘many’ be- side s. ealbh, m. ‘flock’; W elw, pl. -oedd, m. ‘gain, profit, goods’; Alb. cf. pjellë, f. *pro- duce' (ambig. cf. peln-); Go. OHG. OS filu ‘much, many’; OE fela, Du. veel, id.; ON fjol-, cpds. id.
12665:pelu-, see peluos & pélouos
13233:pl- (radical) (2) “back, folded; turn, fold”. Cf. pol- (2). Variant: pol- Skt. cf. paré, adv. “later”; Romani pale ‘after’ (both fr. *pelai); Arm. cf. vay, u-st. (old, early’, perh. fr. *ay-polu-, *-plu); cf. also vayo, vayiv ('early, tomorrow', if fr. *au-pol-, -polibhi); Gk. pálin Chack again” fr. *polim or *plim) beside pálai, adv. ‘formerly’; Ir. cf. -al in du-al,
13263:pluos “pale, dim". All evidence ambig. Cf. pal- (1) with variants, & polu-, poluos (2) Arm. cf. (?) ayawt, i-st. ‘dim’ beside nvay, adj. dark’, a cpd.); Lat. palleo, Ere, v. ‘grow pale’; pallidus, adj. ‘pale’; pallor-, -oris, s. (Note: The equivalence of IE *-]u- and Lat. -all- is uncertain, see WH & EM on salvus & sollus, soll-; mollis, collum; pullus (1) & (2); pulvis, pulvinus, calvus, calva, etc. Cf. E Som- mer: HLLF: $ 46 & § 47; S. E. Mann: Czech Historical Grammar: $ 44 & § 89; S. E. Mann: Albanian Historical Grammar, pp. 36-37; S. E. Mann: Armenian and Indo-European, § 62 & $ 63)
13350:(poluis, a (pelu-) ‘dust, powder’, etc. See peluos & pélouos)
13351:poluos (1) (polus, polu) “big, full; much, many, abundant; spate’. Cf. pel-, pl-, plnos, pltos, plëtos, etc. WP II, 65 Skt. cf. parvami, v. "DI": Av. paourus, pourus, parus, adj. “abundant; full, big'; OPer. cf. parav, prn. ‘many’; Per. cf. farawan, adj. “abun- dant’; Oss. fír, Dig. fur, prn. ‘much, many’; Arm. cf. h-olov, adj. (much, many, great’, fr. *en-peluo-); Myc. poru- (for polu-); Gk. Hom. poulüs, beside Gk. pollós ‘abundant, strong’; polüs, f: pollé, adj. ‘many’; Lat. cf. pollens, gs. -entis, adj. “powerful, resourceful’;
13353:cf. pol-lex, Pollux, populus, mani-pulus, -plus, am-plus, pulvinus & polvinar, epulae, and pul- cer, -cher for possible relics of type *polu-); Olr. and Ir. oll, oll-, adj. & px. ‘great, huge"; R cf. polovodie, n. “high water’; Latv. cf. pali, mpl. id.
```


## [2026-09-14T00:53:44.315Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--MON faravan\"; grep -c \"فراوان\" MON_part1.txt MON_part2.txt 2>/dev/null; echo \"--AHD pele\"; grep -n -i \"^pelə\\|pele-1\\|pel[əe]-1\\|plē-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T00:53:44.381Z] TOOL RESULT

```
--MON faravan
MON_part1.txt:108
MON_part2.txt:190
--AHD pele
832:pel-5. To sell. Lengthened o-grade form *pdl- in Greek p6lein, to sell: BIBLIOPOLE, MONOPOLY. [Pok. 5. pel- 804.] pel-6. To thrust, strike, drive. I. Suffixed form *pel-de-. 1. Germanic “*felt-, *falt-, to beat, in: a. Old English anfilt(e), anfealt, anvil (“something beaten on”): ANVIL; b. Germanic “*feltaz, *filtiz, compressed wool, in (i) Old English felt, felt: FELT! (ii) Medieval Latin filtrum, filter, piece of felt: FILTER. 2. Latin pellere (past participle pulsus), to push, drive, strike: POUSETTE, PULSATE, PULSE!, PUSH; COMPEL, DISPEL, EXPEL, IMPEL, PROPEL, REPEL. 3. Suffixed o-grade form *pol-o-, fuller of cloth, in Latin polire, to make smooth, polish (< “to full cloth”): POLISH. II. Extended form *peb-. 1. Present stem *pelna- in: a. Latin appelldre, “to drive to,” address, entreat, appeal, call (ad-, to; see ad-): APPEAL; b. Latin compellare, to accost, address (com-, intensive prefix; see kom): COMPELLATION; Cc. Latin interpellare, “to thrust between,” interrupt (inter-, between; see en): INTERPEL- LATE. 2. Suffixed zero-grade extended adverbial form *pla-ti, in pre-Greek *pldti in Greek plésios, near (< “pushed toward”): PLESIOSAURUS. [Pok. 2. a. pel- 801.] pel-7. Dish. Suffixed lengthened-grade form *pél-owi- in Latin pélvis, basin: PELVIS. [Pok. 4. pel- 804.] pele-1. 1. To fill; with derivatives referring to abundance and multitude. Variant “*p/é-, contracted from “pleo-. I. Suffixed zero-grade form “pls-no-. 1.Germanic *ful- naz, *fullaz, full, in Old English full, full: FULL’. 2. De- rivative Germanic verb *fulljan, to fill, in Old English fylian, to fill: FILL. 3. Latin root *pldno-, replaced by *pléno- (influenced by Latin verb plére, to fill; see III. 1. below) in Latin plénus, full: PLENARY, PLENITUDE, PLENTY, PLENUM; PLENIPOTENTIARY, REPLENISH, TERREPLEIN. II. Suffixed form *p(e)la-u-. 1. Possibly Latin paliis, marsh (? < “inundated”; but possibly rather from pel-?): PALUDAL, PALUDISM. 2. Obscure compara- tive form (Old Latin p/ous) in Latin plis, more: PIU, PLURAL, PLUS; NONPLUS, PLUPERFECT, SURPLUS. 3. O-grade form *pol()-u- in Greek polus, much, many: POLY-; HOI POLLOI. III. Variant form “p/é-. 1. Latin plére, to fill: (ACCOMPLISH), COMPLETE, COMPLIMENT, COMPLY, EXPLETIVE, IMPLEMENT, REPLETE, SUPPLY. 2. Possibly suffixed form *plé-dhw- in Latin p/lébs, plébés, the people, multitude: PLEBE, PLEBEIAN, PLEBS; PLEBISCITE. 3. Suffixed form *plé-dhwo- in: a. Greek pléthos (Ionic pléthus), great number: ISOPLETH; b. Greek derivative verb pléthein, to be full: PLETHORA; PLETHYSMOGRAPH. 4. Suffixed (comparative) form *plé-i(sjon- in Greek pledn, pleién, more: PLEO-, PLEO- NASM; PLEIOTAXY, PLEIOTROPISM, PLIOCENE. 5. Suffixed (superlative) form *p/é-isto- in Greek pleistos, most: PLEISTOCENE. IV. Possibly Sanskrit piirah, cake (< “that which fills or satisfies”): POORI. [Pok. 1. pel- 798.] pela-2, Flat; to spread. Variant *pld-, contracted from *plaa-. 1. Suffixed form *pel{a)-tu- in Germanic “felthuz, flat land, in Old English feld, open field: FIELD. 2. Suf- fixed form *pel{a)-t-es- (by-form of *pel)-tu-) in Ger- manic *feltha-, flat land, in: a. Old High German feild, field: FELDSPAR; b. Middle Dutch veld, velt, field: VELDT. 3. Variant form “pld- in: a. suffixed form
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1387:COMMODITY med- COMMON mei-! COMMOTION meue- COMMUNE mei-1 COMMUNICATE mei-1 COMMUNISM mei-1 COMMUTE mei-1 COMPACT! pag- COMPANION pa- COMPANY pa- COMPARE pera-2 COMPART pere-2 COMPASSION pé(i)- COMPEL pel-6 COMPELLATION pel-6 COMPENDIUM (s)pen- COMPENSATE (s)pen- COMPETE pet- COMPLACENT plak-! COMPLAIN plak-2 COMPLECT plek- COMPLETE pele-1 COMPLEX plek- COMPLICATE plek- COMPLICE plek- COMPLIMENT pele-1 COMPLY pele-1 COMPONENT apo- COMPORT per-2 COMPOSE apo-, paus-, COMPOSITE apo- COMPOSITION apo- COMPOUND apo- COMPRADOR pere-1 COMPREHEND ghend- COMPRESS per-5 COMPRISE ghend- COMPROMISE (s)meit(9)- COMPUNCTION peuk- COMPURGATION peue- COMPUTE peu- COMRADE kamer- con! kom
1509:FicHu dhig¥- FICKLE pelg-2 FICTILE dheigh- FicTION dheigh- -FID_ bheid- FIDELITY bheidh- FIDUCIAL  bheidh- FIDUCIARY bheidh- FIELD pele-2 FIELDFARE wer-4 FIEND pé@(i)- FIERCE ghwer- Fiesta dhés- FIFE pipp- FIFTEEN penkWe FIFTH penkwe FIGHT pek-2 FIGMENT dheigh- FIGURE dheigh- FILAMENT gWhi- FILAR gWhi- FILARIA gWhi- FILE! gWhi- FILE? peig-1 FILES pu-2 FILIAL dh@(i)- FILIATE dhé(i)- FILIBUSTER pri- FILIFORM gWhi- FILIGREE gre-no-, g¥hi- FILL pele-1 FILLET gWhi- FILLY pau-
1544:FROLIC fik-, preu- FROM per? FRONTISPIECE spek- FROST preus- FROTTAGE bhréi- FROWARD per! FRUCTIFY bhrig- FRUGAL bhriig- FRUGIVOROUS bhrig- FRUIT bhriig- FRUITION bhriig- FRUMENTACEOUS _ bhrig- FRUMENTY bhriig- FRUSTULE bhreus-2 FRUSTUM bhreus-2 FRY! bher-4 FUGACIOUS bheug-1 -FUGE bheug-! FUGITIVE bheug-1 FUGLEMAN man-1, pleu- FUGUE bheug-! FUHRER per-2 FULCRUM bhelg- FULGENT bhel-1 FULGURATE bhel-1 FULIGINOUS dheu-1 FULL! pele-1 FULMAR pu-2 FULMINATE bhel-1 FUMARIC ACID dheu-1 FUMAROLE dheu-1 FUMATORIUM dheu-! FUMATORY dheu-1 FUME dheu-! FUMIGATE ag-, dheu-! FUMITORY dheu-1, ters- FUNAMBULIST al-2 FUNCTION bheug-2 FUND bhudh- FUNDAMENT bhudh- FUNDUS_ bhudh- FUNGIBLE bheug-2 FUNNEL gheu-
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
1691:Is es- ISALLOBAR gWere-2 ISCHEMIA segh- ISINGLASS bhié-2 ISLAND akwa- ISOBAR gWere-2 ISOCLINE klei- ISOGLOss glogh- ISOHEL sawel- ISOHYET seue-2 ISOMER (S)mer-2 ISOMETRIC mé-2 ISOPIESTIC sed-1 ISOPLETH pele-1 ISOSCELES skel-3 IsosTasy sta- ISSUE ei-1
1932:NONAGENARIAN dekm, newn NONAGON newn NONANOIC ACID newn NONCHALANT kela-1 NONE ne, oi-no- NONES newn NONJUROR yewes- NONPAREIL pera-2 NONPLUS_ pele-1 NOOK ken-5
2043:PALUDISM _pele-1 PALYNOLOGY pel-! PAM bhilo-
2099:PIU pele-1 PLACABLE plak-! PLACATE plak-1 PLACE plat- PLACEBO pilak-1 PLACENTA plak-1 PLACID plak-1 PLACOID plak-1 PLAGAL plak-1 PLAGIARY plak-1 PLAGIO- plak-1 PLAGIOCLASE kel-1 PLAGUE plak-2 PLAICE plat- PLAIN pela-? PLAINT plak-2 PLAIT plek-
2101:PLEA plak-1 PLEACH plek- PLEAD plak-! PLEASANT plak-1 PLEASE plak-1 PLEBE pele-1 PLEBEIAN pelo-1 PLEBISCITE pele-1, skei- PLEBS pele-1 PLECOPTERAN pet-, plek- PLECTOGNATH plek- PLECTRUM plak-2 PLEDGE plegan -PLEGIA plak-2 PLEIOTAXY pele-1 PLEIOTROPISM pele-1 PLEISTOCENE pele-1 PLENARY pele-1 PLENIPOTENTIARY pele-1 PLENITUDE pele-! PLENTY pele-1 PLENUM pele-1 PLEO- pela-1 PLEONASM pelo-1 PLESIOSAURUS pel-6 PLETHORA pelo-1 PLETHYSMOGRAPH pele-1 PLEUSTON pleu- PLEXOR plak-2 PLEXUS plek- PLIANT plek- PLICA plek- PLICATE plek- PLIGHT! plek- PLIGHT? plegan PLIOCENE pelo-1 PLISSE plek- -PLOID pel:? PLOVER pleu- PLUCK pilo- PLUMATE pleus- PLUMB plumbum PLUMBAGO plumbum
2103:PLUMBER plumbum PLUMBIFEROUS plumbum PLUMBISM plumbum PLUME pleus- PLUMMET plumbum PLUMOSE pleus- PLUMULE pleus- PLUNGE plumbum PLUPERFECT dhé-1, pela-1 PLURAL pele-1 PLUS pele-1
2114:POLICE pele-3 POLICLINIC pela-3 POLICY! pele-3 POLICY? deik- POLIOMYELITIS pel-2 POLIS pele-3 POLISH pel-6 POLITIC pele-3 POLITY pele-3 POLKA pele-2 POLLEN pel-1 POLLEX pol- POLLUTE leu-2 POLTERGEIST bhel-4, gheis- POLTROON pau- POLY- pele-1 POLYGALA melg- POLYGLOT glégh- POLYGYNY gWen- POLYHISTOR weid- POLYMATH mendh-! POLYNYA pele-2 POLYP ped-1 POLYPNEA pneu- POLYPOD ped-1 POLYTECHNIC teks- POLYTENE ten- POLYTHEISM dhés- POLYTOCOUS tek- POLYTROPHIC threph- POMACE pomum POMADE pomum POME pomum POND bend- PONDER (S)pen- PONDEROUS (S)pen- PONIARD peuk- PONS pent- PONTIFEX dhé-!, pent: PONTIFF pent- PONTIL peuk- PONTINE pent- PONTOON pent- PONY pau-
2118:POORI pele-1
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
2327:suP2 seue-2 SUPER- uper SUPERABLE uper SUPERANNUATED at- SUPERB uper SUPERCILIOUS kel-2 SUPERCILIUM kel-2 SUPEREROGATE reg-' SUPERFETATE dh@(i)- SUPERFLUOUS bhieu- SUPERIOR uper SUPERJACENT yé- SUPERLATIVE tele- SUPERNAL uper SUPERNATANT sna- SUPERNUMERARY _nem- SUPERSCRIBE skribh- SUPERSEDE sed-1 SUPERSTITION sta- SUPERVENE gWa- SUPERVISE weid- SUPINE! upo SUPINE? upo SUPPLANT plat- SUPPLE plek-, upo SUPPLICATE plek- SUPPLY pele-1 SUPPORT per-2 SUPPOSE apo- SUPPRESS per-5 SUPPURATE pu-2 SUPRA- uper SUPRALAPSARIAN leb-1 SUPREME uper SUPREMO uper SUR- uper SURCULOSE swer-3 SURD swer-2
2360:TERREPLEIN pele-1, ters- THRENODY dher-3 TORT terkw- TRICEPS kaput
```


## [2026-09-14T00:53:55.475Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"paruzana\\|paru-zana\\|paru- adj\\|paruv\" KNT.txt | head -20"
}
```


### [2026-09-14T00:53:55.529Z] TOOL RESULT

```
392:paru-zana- ‘having many men’, with z from j.
610:paruvam (and derivatives), corresponding to Skt.
631:Before enclitics, a final nasal which would otherwise be written, is retained: (батса = gaibām-cã; zXagam-Sim, paruvam-ciy, adam-&im.
964:*pruom, OP paruvam ‘formerly’, Skt. pürvam. $69. THe PIE 8новт DIPATHONGS IN 7, namely
1492:Other instances of z are largely the product of pIE ў and gh in Median ($88, $91), or in OP before consonants ($91, $95); such a 2 became s and then š before n: pIE 0: paruzana-, vispazana-, Varkazana-, vaz-
1594:61217. ErrNTHESIS is the insertion in a syllable, of ? or u or other vowel by the influence of a sound in the following syllable, the result being a modification of the sound of the vowel in the syllable suffering epenthesis. Ң is frequent in Avestan, as in patti for *pati, OP райу, or роити for *paru, OP paruv. The only certain example in OP is yäumainiš for "yüumani$ and its com- pound ayàu(ma)ini$ DNb 40, 59. It is less likely that PatSiyausida- is for "*pa&-d-heddd-, for *pat;-, with epenthesis (see Lex. s.v.).
1916:а. The prior element is an adjectival modifier: paru-zana- ‘having many men’; vispa-zana- ‘hav-
2040:Nom. Pl. martiyd, z$ayatiyà, hamiciyd, anuštyā, takabard, tigrazaudà, haumavargà, paruva, Mada, Вока, Mudrüyà, Yauna, Uvjiya; with double
2172:V. The nom.-acc. nt. sg. inherits the old end- ing; OP nom. paruv is the exact equivalent of Av. pouru, Skt. puri, Gk. rods.
2272:In abl. (pIE) *-tos: amata, paruviyata, fravata.
2672:K. To express time when, as їп the adverbs paranam and paruvam ‘formerly’, and with the postposition pakiy: DB 1.20 xsapavd raucapativà ava akunavayata ‘either by night or by day, that was done’; DB 2.61f Güravaharahya mahya jiyam- nam patiy avat sam hamaranam kartam ‘on the last of the month Thuravahara, then by them the battle was fought’.
2771:In DB 1.8 haca paruviyata, hyd amüxam tauma z5àyaBiyà aha, the probability is that rsdyaiyé 18 nom. pl. ‘kings’, in which case dha is plural, agreeing with its predicate; but if z$üya8iyü 18 taken аз nom. sg. adj. ‘royal’, aha is singular, agreeing with its subject taumd ‘family’.
2955:With an adverbial expression the present may, as in other languages, indicate time begun in the past and extending into the present, and the im- perfect stmilarly may express time begun їп a re- moter past and extending into a nearer past; the best examples are in DB 1.7 hacd paruviyata ётйй amahy һас paruniyata hya améxam taumā a Sdyahiyd cha ‘from long ago we are (= have been) noble, from long ago our family was (= had been) royal (or kings)’, and 9-11 VIII manā tawmaya tyaiy paruvam xsdyahiyd cha adam navama IX duviláparanam xsdyahiya amahy ‘8 of my family (there were) who were (= had been) kings; I (am) the ninth; 9 in succession we are (= have been) kings’.
3066:position, standing either at the beginning ог be- 4 tween the subject and the verb or at ће end: resp, = DB 1.8 hacà parwviyata, 1.45 hacà paruviyata, 1.82 5 Uvjam and abiy mam. The phrase тайпа Aura- — mazdüha ‘by the favor of Ahuramazda’ stands first in its clause in 63 of its 77 occurrences. Resump- tive pronouns (haw and forms of ava-) and ad- verbs (avadà, араба) stand first after a nominative phrase; pasdva ‘afterward’ leads off its clause in 77 of its 82 occurrences, standing last in DB 1.27, 4.5, 5.3, XSc 3, before yada ‘when’, while in DSe 48 the text is uncertain. Other adjuncts are vari- able in position; thus the goal may precede or follow the verb: DB 2.3 pasdva adam Babirum axtyavam ‘afterward I set forth to Babylon’, DB 2.30 avam adam früisayam. Arminam ‘him I sent forth to Armenia’.
3146:! More commonly without the preceding antecedent, as in DB 4.50f tyaiy paruvà zXüyabiya уйа аһа avaiSám avi (= avabd, §52.VI) тату astiy kartam ‘who (were) the former kings, as long as they were, by them thus has not been done ...". ?But in XPh 43-5 айа tya adam akuna- vam visam vasnd Auramazdahd akunavam I take aita as acc., since a resumptive аша is lacking.
3466:7 diy : vayam : Haximanisiya : 6ahy&mahy : hac : paruviyala : ümátà : ama
3467:8 hy : haeà : paruviyata : hyà : amáxam : taumá : xSdyasiyd: aha — :0
3468:9 апу: Darayavaus : xSdyaéiya : ҮШ : mana : taumayd : tyoty : paruvam
3493:45 à : Kabüjiyam : aita : xSagam : hacd : paruviyata : amaxam : taumaya : à
3517:63 và : avistàyam Jyafü : paruvamely : avafà : adam : akunavam : dyadan
```


## [2026-09-14T00:53:57.361Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find page markers near line 13351\nimport re\nfor i in range(13300,13360):\n    if re.search(r'\\[|page|\\f', lines[i]): print(i, lines[i][:120])\nprint('---pelu line 12664 context')\nprint(lines[12660][:200])\nEOF"
}
```


### [2026-09-14T00:53:58.331Z] TOOL RESULT

```
13300 e-grade in view of Arm. herk ‘ploughed field’, see peduom); of ambig. vocalism is Skt. pade pade (“step by step”, *pedei
13309 poiKos, is (2) ‘demon, devil; malignant’. Skt. cf. paisunam, n. ‘slander’ beside (z-gde) pisunah, adj. ‘malignant, vile’
13325 poios (poiios), -es- ‘drinking; drink’. Cf pt-, etc. Skt. páyas, n. “fluid, sap, juice, milk’ beside peyah, adj. & s. ‘
13335 polKos, à (2) ‘fallow’. See above, and WP I, 516 Gallo-Lat. olca, f. 'fallow-land' (phonol. cf. orco ‘pig’: farrow); MH
13346 poltis, os, ios, à (1) ‘side, fold, flap’. Cf. pol- (2). WP II, 56 Skt. (ambig. patah, m. “cloth, garment, screen, canva
13356 pondos, -es- “hanging object, heavy object, weight, stone'. Cf. pend- (1) Lat. pondus, gs. -eris, n. ‘weight’; MIr. ond,
---pelu line 12664 context
918
```


## [2026-09-14T00:54:04.302Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nlines=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\n')\ndef lastpage(n):\n    for i in range(n,0,-1):\n        if re.fullmatch(r'\\s*\\d{1,4}\\s*', lines[i] or ''): return i,lines[i].strip()\n    return None\nprint(lastpage(13351))\nprint(lastpage(12664))\nEOF"
}
```


### [2026-09-14T00:54:05.399Z] TOOL RESULT

```
(13351, '975')
(12660, '918')
```


## [2026-09-14T00:54:05.528Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"paru- 'much\\|paru-.*much, many\\|pouru\\b\" KNT.txt | head -20; echo ---; grep -n \"paruv-\" KNT.txt | head"
}
```


### [2026-09-14T00:54:05.586Z] TOOL RESULT

```
2172:V. The nom.-acc. nt. sg. inherits the old end- ing; OP nom. paruv is the exact equivalent of Av. pouru, Skt. puri, Gk. rods.
2644:baug- ‘free’, seen in Av. pouru-baorsna-; in OP
4956:Aéiydbausna- sb. ‘Athiyabaushna’, father of Arsaces ($168.11): cpd. of (Av.) ai- ‘destruction, misfortune’ + pass. pte. of d-baug- ‘to free’ ($248) with late -šn- from -aén- (Bv. BSLP 29.2.104, cf. Av. pouru-baozóna- ‘bringing abundant rescue, Bthl. AiW 901): ‘Freed from misfortune’ ($160.14; not active ‘bringing freedom from misfortune’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
5658:paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
---
```


## [2026-09-14T00:54:13.959Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5655,5670p' KNT.txt; echo \"=== page markers\"; python3 - <<'EOF'\nimport re\nlines=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i in range(5600,5680):\n    if re.search(r'\\[pdf page|^\\s*\\d{2,3}\\s*$', lines[i] or ''): print(i, repr(lines[i][:80]))\nEOF"
}
```


### [2026-09-14T00:54:15.140Z] TOOL RESULT

```
pariy prep. and prefix ‘around, about’: Av. pairi, Skt. pári, Gk. тері, Lt. per ‘through’, pIE *peri ($64, §75.1, $113, §140.1). Prep. with aec. ‘about’ DB 1.54. Prefix-with ay-, bar-; ef. also pariyana-.
196 OLD PERSIAN
pariyana- sb. ‘superiority’: deriv. ($147.IT) of pariy, in meaning seen in Ау. pairi ‘vorne, über ... hin’, Skt. pári as prefix ‘much, excessively’, cf. Gk. meptoads ‘excessive’ (otherwise Hz. ApI 273, Sen 250). pariyanam nsn. DNb 52.
paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
paruva- adj. ‘being before in time or place’ (§35.1[): Av. paurva-, Skt. pürva-, pIE *pruos (868, $150), ef. Gk. Ion. трохоѕ ‘early’. See also paruviyata, paruviyaüd. parwā npm. ‘former’ DB 4.51. parwam asn. as adv. ‘formerly’ DB 1.9; DBa 15f; DSe 43°, 47; XPh 36, 39; paruvam- ciy DB 1.63, 67, 69.
parwnyata, adv. with preceding hacd, ‘from long ago’: *paruviya- (ie. *parvya-, deriv. of paruva-), Av. paouruya-, Skt. pürvyd-, + adv. suffix -la^, Av. -£ó, Skt. -tas, Gk. -ros, Lt. -tus asin funditus, pIE *-los ($191.11). C£. also paruviyatà. DB 1.7, 8, 45; DBa 11, 12.
[paruv|iyafà adv. ‘at first attempt’: *paruviya- (see paruviyala) + adv. suffix -0à, Av. -fa, Skt. -ihà ($191.ID). DSj 3 (conj. of Brandenstein, WZKM 39.49-51; ef. note ad loc.).
paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.
Parga- sb. ‘Parga’, a mountain in Persia: Elam. par-rak-qa, NPers. Purg ($30). Parga лет. DB 3.44. |
partara- sb. ‘battle’ (as in Elam. and АКК. versions): extension of -r/n- stem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’, to root in Av. poral-onie ‘they fight’? (Bv. TPS 1945.69-4; not agency noun
‘fighter, foe’ as taken by Wb. KIA 90-1, Bv. Gr. $277; not paratara- ‘foe’, with Wackernagel, KZ 59.29-30, as compar. to [Skt.] pára- ‘distant’ = RV ‘enemy’). partaram asn. DNa 47.
Ратдата- (§29.n2, $31) adj. ‘Parthian’, also тазе, as sb. ‘Parthia’, a province of the Persian Empire: Elam. par-tu-ma, АКК. pa-ar-tu-á, Gk. IIapóià. Extension ($150) of stem seen with vriddhi in Pársa-, but with dialectal difference in the 0/s ($9. VT, 887).
(1) ‘Parthian’: Paréava nsm. DN iv; A?P 4. Par&avaibi$ ipm. DB 2.96. (2) ‘Parthia’: Paréava nsm. DB 1.16; 2.7, 92;
DPe 15; DNa 22; DSe 21°; DSm 8°; XPh 20.
Par8avai ism. DB 2.94° 96°; 3.5, 10. parna-, see duildparanam, parana-. ‘parsa- vb., see fraó-.
?parsa- sb. ‘court’, only in Hz. ApI 278; for his pa[r|saiy lsm. DNb 22, see under patiy.
=== page markers
```


## [2026-09-14T00:54:31.734Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"fraesta-\\|fraeSta\\|fraèsta\" BRT.txt | head -5; echo \"--- SNS\"; grep -n -i \"freh\\|frah\\|fray\" SNS.txt SNS_pages.txt 2>/dev/null | head -20"
}
```


### [2026-09-14T00:54:31.808Z] TOOL RESULT

```
17499:•  g.  'fraeSta-  m.  'Gesandter,  Bote':  yavsi vTspsi  'tänhs  hr^hämä  "fiir  alle  Zeit  wollen wir  (deine)  Gesandten  sein"  V-^j?.  8".
--- SNS
SNS.txt:1035:FrO. : H. Reichelt, Ver Frahang; dim. Wien 1900. 
SNS.txt:1473:Reichelt, H.: ber Frahang i dim, Wien, 1900. 
SNS.txt:1520:Junker, H.F.J. : The Frahang i Pahlavik, Heidel- 
SNS.txt:6866:..a jS radak + ^:Svak tjhft-1 ^4> ^ ^ .fcfray* 
SNS.txt:8039:•*«** '>^'*l>^.*>ag:padafrah: -t^>o*><L> 
SNS.txt:8041:->T-n-V-6/A^.l/Y^. / ' J>>>v ; padafrah: V 163) 
SNS.txt:8527:.\>:^ .jMO'J**" :frSh/fray:_^0 
SNS.txt:8530:.«tf <jili<t>*j*Wj» :frayadarX*i«^«J 
SNS.txt:10423:• VY/Y^S [3W tfM'j : *&) j-^.Ujjrzufray 
SNS.txt:29425:frayah- 126/7 
SNS.txt:30655:zufray 168/9 
SNS.txt:31953:padafrah 116/12 
SNS.txt:32711:frayadar 129/9 
SNS.txt:32719:freh/fray 129/5 
SNS.txt:33025:fray 126/6 
SNS.txt:33026:frayist 127/7 
SNS.txt:33043:frahang 126/1 
SNS_pages.txt:545:                                                                              FrO. :    H. Reichelt, Ver Frahang; dim. Wien 1900.
SNS_pages.txt:881:                                                                       Junker, H.F.J.        :   The Frahang i Pahlavik, Heidel-
SNS_pages.txt:892:Reichelt, H.: ber Frahang                                                                :   K.R. Cama Oriental Institute. Golden
```


## [2026-09-14T00:54:33.761Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nimport re\nfor i,p in enumerate(t):\n    if 'فرهست' in p or 'فره‌ست' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print('HIT leaf',i, m.group(1) if m else '?')\nEOF"
}
```


### [2026-09-14T00:54:35.225Z] TOOL RESULT

```
721
HIT leaf 272 273
```


## [2026-09-14T00:54:40.484Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[272][:2500])\nEOF"
}
```


## [2026-09-14T00:54:41.076Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8520,8535p' SNS.txt"
}
```


### [2026-09-14T00:54:41.685Z] TOOL RESULT

```
[pdf page 273]
ob ‏بر وزن شرت » بمعنی‎ ODS
. ‏وشوکت وشکوممندی باشد‎

فر‌هحت ۱ - بروزن‌سرسخت. ماضی
فرهختن است یمنی ادب کرد وتادیب فرمود.

‎oe J‏ ۲ - بفتح اول والث بروزن
برجتن » بمعنی تربیت کردن و ادب آموختن
وتأدیب لمودن ‎ath‏ و بمعنی آویختن هم‌آمده
است؛ ‎Say‏ ثالث هم درست است .

‏فرهخته۴ - بر وزن برجسته, بمعنی
ادب کرده و تادیب تموده باشد .

‏فرهست ۴ بر وزن بدست ؛ ‎eae‏
‏جادو وجادوبی ‎es‏ وساحری باشد .

‏فر همنك = بنتح اول ‎ky‏ بروزن‌سك
لوند ۰ ‎ew‏ قرربب ونزديك ‎Path‏ - ویمعنی
صاحب عقل و خردمند هم آمده است ۷ ؛وبة
‎Syl‏ و سکون ثانی هم کفته‌الد که پروژن ‎AAS‏

‏باشد .
فرهنج ‎ones‏ شطرنج ۰ بمعنی علم
(۱) چك : کشو:

‏۱ - رك:فرهختن.
ای شمن اهسته باش زان بت بدخو

‏۴ - پپلوی ‎fr@hest‏ ( صيقة تفضیلی از « فره » بمنی ‎(he‏ بمعتی ب

‏مرو اعد

‎bss‏ و داتس و عقل وادب است ۷ - وکناییرا
نیز گونند که مشتمل باشد برلغات فارسی ۷ -
و نام ماد رکیکاوی هم هست ۴ - وشاخ درختیر!
کوبند که آنرا بخوابانند و ‎SE‏ بر بالای ‎OF‏
‏بربز ند تابیخ‌بگیرد و از آنجا ب رکنده بجای‌دیگر
نهال‌کنند ۸ - و نام دوایی نیز هست که آنرا
کشوث (۱) ‎aay‏ و تخم آنرا بزرالکشوث
خوانند ‎٩‏ .

‏فرهنجد - مضارع فرهنجیدن است
‎on‏ ارب کند ‎aly‏ تماید .

‏فر ‎p= OD‏ وزن سر پنجه . مردم
با ادب و خوش روی و ‎SS‏ صورت و سیرت را
گوند .

‏فرهنجیدن *۱- بروزن‌برهم‌چیدن .
پمعنی اد بکردن و تأدیب نمودن باشد .

‏فر هنجیك۱۵ ‎po‏ وزن برهم چیده .

‏بمعنی ادب کرده شده و تأدیب پذی‌نده باشد.

‏۴ - رك : فرهیشتن . ۴ اسم مفعول از * فر‌ختن * :

‎OW‏ بت فرهشته تست , هست نوآموز.
دقیقی طوسی « لفت فرس 45۷ > ۰
نشر ‎ule?‏

‏۷۶ . صادق هدایت درمجلةٌ موسیقی ‎Tl‏ : ۸ در ‎rth‏ فرهست 4 ‎oad‏ فرس نوشته : « پازند
«فرایت * بمعنی فراوانتر و ‎forks‏ میباشد و ربعلی بجادوئی ندارد , چنانکه در تعریف لفت‌فره
(س4۲6) و لفت فرابته « فراسته » ( ص۰٩4‏ ) همین کتاب ‎cal)‏ فرس ) اشار» شده است.»
ممهذا اسدی این شاهد را از ابوضرمرغزی برای معنی جادوبی آوردء :

‏نست را هست کند تنبل اوی
‎cil?‏ فری ص ۰۱۹ .

‏© - فرهمند بدکنش ‎Sp‏ مرو

‏۹ - رك : جهانگیری .
فرهنگه, فرنج .
مرو را در هتر بفرهنجد

‏۷ رك : فرهنگ . ‎A‏
‎ae ۰‏ : افرهنج .
توسنی از سرش یداهنجد ‎ .‏ سنائی غزنوی «جهانگیری».

‏هست را نیست کند فرهستش .» و قس : هست واستا

‏تا نگردی دردهند و آهمند .

‏« ناصرخرو بلخی ۱۲۳* «جپانگیری».
- رك: فرهانج ۰
۶ از: فرهنج ‎Cadet‏ (پوندمسدری):

‏۱ اسم مقعول از «فرهنجیدن» («م.) +
```


### [2026-09-14T00:54:41.743Z] TOOL RESULT

```
Lu c--U *.u .j 1 ? 



,^j» <i&«> rfrasang: 3V->^0 

U/T^ •(&&*) frasang :^ | 
.\>:^ .jMO'J**" :frSh/fray:_^0 
hfj*Hxt£By kirfag handOzih: -DW 5t»3_JSt> 

.«tf <jili<t>*j*Wj» :frayadarX*i«^«J 

fryadCatD : V ^hw. 214/8 -pryM:^ ■ (W
```


## [2026-09-14T00:54:55.801Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[613]\ni=p.find('پروین')\nprint(p[max(0,i-1200):i+1500])\nEOF"
}
```


### [2026-09-14T00:54:56.952Z] TOOL RESULT

```
- و۳ -
منازل قمرحم هت۱ سویمعتی دیروز عم گفته‌اند
که روز گذخته باشد ار ؟ر ۴ ۰
پر نا بر وزن رعنا, دبای منقش لطیف
و تازكگ را گویند -
پر فالك ه بنم اول وسکون ثانی و نون
بالف کشیده ویکاف زده ءآدم جوان و اول مرا
کوننده - ونام‌طایفه ای حم‌هست از ترکان ۰۷
ر فج - ختح اول و ثانی ۷وسکون‌نون
وجیم . غلهای: باشد شبیه بگندم لیکن از کندم
باریکتر وضعیف تراشت.:
پر فف - بر وزن کمند.» بافتٌ ابربشمی
وحریر ساده را کونند ۵و پرتبان منفش‌رائیز
کفته اند و بمعتی زین پوش هم آهده
است - و بمعنی پروین هم حست که ناره های
پر داد
کوهان ئور باشد ٩‏ - .و ایغ وشمشیر و" جوهر
تیغ وشمشیر وامثالآنرا یز کویند*۱ - وبمعنی
خیار صحرابی هم هست - و مرغ و فربز را حم
کفته‌اند وآن سبزء نورسته باشد که دواب آنرا
برغبت تمام خورند۱9 .
پر نداخ ه ختح اول و انی وسکون
؟الث و دال بی نقطه بالف کشیده و بضای‌شطه‌دار
بر نداور ۱۴ « بفتح اول و واو بروزن
حسن ساغی » تيغ وشمشیر جوهودار را گونند.
ی
پر ند بفتح اولوئانی ورابم‌وسکون
تالث وکاف » يشته و کوه کوچك را گویند که دد
میان صحرا وافم شده باشد .
مرز ضبط کرده است.»
ار کس عازه چو چاء ذقنی شد بمثل
چونکه زرن قدحی در کف حسمین صنمی
۵ رک : ابر .
گر بود چاه ز دینار وز نقره ذفنا
با درخشنده چراغی ممبان برنا .
«منوچهریدامغانی۳؟.
. رل: پرن وپروین‎ - ٩
مبارزان فدر قدرت قنا قوت‎ ۰
ات او مت جک
ازرقی هر وی. «لفت نامه».
بامن هححنی ممرب آن «فر ند» (بکسراود ودوم) وأفر ندنیز آهله. دتشس؟. ۱-نیزه
سد دستی. ركك : برن (حاشیه) . ۴ رك : پراداخ و برنداق . ۴- از : بر ند
( جر شمشیر ).۲+ آور ( پسوید اصلف ) .
```


## [2026-09-14T00:55:01.971Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in [614,618,619]:\n    p=t[n]\n    if 'پروین' in p:\n        print('==== leaf',n)\n        print(p[:2200])\nEOF"
}
```


### [2026-09-14T00:55:03.237Z] TOOL RESULT

```
==== leaf 614
پرعدوار
و ثل وار ۱ نتمولنانی‌وسکون
مه بش فب ریز کته که ریخب
۰ ۵
بر ندوش ؟- با واومجپول بروزن
کمن وش » بعضی برتدوار است ت که شب روز
گذشته باشد معنی پربشب ۰ چه شب گذشته را
دوش میکوند و بعربی یارحذالاولی خوانند,منی
یش از دوشء چه بارحه ممعنی دوش‌است داولی
بمعنی پیش .۶
هر فدلن ؟ » بروزن 9 هرچیز
که از حربر سازند ۰
تون و کاق فارسی » فروغ و برق شمشیر و تیغ
جوهردار را گومنه وحریی‌فرنه خوانند بکسر فا
ورا وسکون نون ودال امد - ویکر اوژوئانی
برتح را وآن توعی اژ فلزات باشد ۴ .
فر ثر ‏ بر وزن بدکو » دیبای منقشس
در تهایت تراکت ولطاقت را گونده .
فر لین - بر وز نکردون » بمعنی پرتو
پر نهادن - کابه از بروت کردن
۹
باشد کسی را از جابی ودفع تمودن - و آواره
ساختن - واژ سر خود بلطایف الحیل وا کردن.
پر نیان ۲ - بر ون سختبان » حر سر
گووتد وسضی با بای ابجد آورده‌اند و گفته‌اند
پوششی بوده که پادشاهان قدم آترا بفال نك
داشتندی ودر روژهای حجشن بوشدندی‌و گفتندی
که این را جبرئیل از بهشت آورده است؛ وبعضی
گوبند جامه رزم رستم زال بوده که از پوست
پانگه دوخته .وده اف وگل ح و اک
آن مرفوم شده بوده است۸ .
بر نیان خوی « کنامه از خوشدل
ونرم دل وخوشحال - و خوشخوی ؛ و نرم‌خوی-
و صاحبدل باشد .
پر بخ بروزن زرنیخ» نخته
گونند بعنی متشگ ممطح هموار .
پرو * بفتح‌اول وسکون ثاني و واو»
ببحتی هروین است و آن چند متاره ابست در
کوحان ور .
روا بفتح اول و سکون ثانی و واو
بالف کشیده . بمعنی طافت و آرام و صبرباشد -
و بمعتی نوجه و التفات‌ورعبت ومیل هم‌هست*۷-
گرا
رك : تون .۰
۶ »> ممرب‌آن» برنکان «اين درید».
٩‏ - رك » پروین .
یز 5 یکوی عاشقان‌آی ار صرسودای ما داری
۴ - راثد: برنج و برنگه .
۲ پهلوی 08۲0130 تاوادبا
سیف اسفرنك «لنت ناعه».
1 ۷۲۸۷ ‌
منگری ع ی « 4 . ۲ یس ۱۸ ۲ , زباکی 021002 « کربرس ۱ * ؛ خوانساری
0 , دزفولی 216042 سالنامةٌ فرهنکه کلپایگان 45؛ مرغ » طائر» مقابل چرنده ؛
و در شم رکله بتشدید آید:
خمانف قد سیاز واندك سای ر‌ بر نله وهردم چاریای. فردوسی طوسی. «لفت. نلمه».
==== leaf 618
پروش :
روش < بر وزن خموش » جوششی
است که از اعضای‌آدمی بر می‌آید و آنرا بعربی
بثر گویند .
روت بر وزن آرزن . مخفف پروان
است وآن شهری‌باشد تزديك بقزنین ٩‏ - وچرخ
ابرشم را نیز گوبندکه آنرا بپای کردانند .٩‏
پر و ند ۲ بروزن فرزند ؛ نام مزرعه
ایست‌از مضافات قزوین؟ -و بمنی امر دهم آمده
ان که پسر مساده باشد . و ی یممنی امرود
نوشته اند که آن میوه ابست مشهور و هیچ بك
خاهدندار ند افه اعل؟ ۱
فر و ۵ ه بسکون تانی بر وزن‌ارژنده,
بته قماش واسباب را گویندوبعرمی رزمه‌خوانشد.
وبسنی لْفافةٌ ماش و اسباب را کفته الد نی
۱ ره : پروان .
۳
پارچه‌ای که قمای را بدان پیچند - وبسنی‌جوان
مانندی‌را کون دکه «هن آن از بهلوی آن باشد-
واستادان بزاز اسباب د کان خود را در آن هند
و با دبسمالها بندند - وبضم ثانی وسکون ثالث
ورابع جم آمفه است* .
بر وه « بفتح اول وثالث بر وزن‌مروه .
هر چیز که در ناخت وتاراج » وجنگ‌وشییشون
از دشمن بدست آیدا" - و بممنی چادر شب عم
آمده است - و پروین را نیز گویند, وآن چند
سناره است در کوهان ثور۷ .
پروهان > باهای‌هوزبروزن‌خ رکمان,
بمعتی ظاحر وآشکرا باشدش .
پرو یز ٩‏ با بای مجهول بر وزن
شبدیز ۰ بمعتی مظفر و عتصور و سعیدب و عزیز
اشکنان.« لت نامه ».
گل بروند دسته بمته مود
۴ - بده فرسنگه شرقی -
معنی امرود و هم
ت. کل امرود 23 میگوید
* ماهروژ
۹ -آن چگ کوشهة باقوت که ازکان خیزد
۷ - رگ پرو و پرون.
۸ زویشت روز کار قوی کشت و این سخن
ابن لفط ظاحر ۱ پزدهان ( ,
دربیت ذبل :
0 تقو بملء فیپا
ي ۰ «لفت نامد» .
جر روی روز گلر بکوم پروحان .
۷۳ 22
( تراع » متاجره ) « تب رکه ۱۵ * .
==== leaf 619
همت و مضاوت وخوش رفتاری و جلوه کردن‌هم
اه اطع
پر و یز قلاك «کنایه از خورشیداست.
رو لزان ه
بروزن گردبدن » آلتی
باشد که‌بدان! ردوشکر
و ادوبة حارة کوفته پرومزن
و امثارآن بیژ ند .
روش - با بای مجپول بر وزن
| دروش ؛ تقصیر وکاهلی درکارها کردن باشد .
رو لین ؟ ‏ بروزن ضمین ۰ چندستارء
کوچك باشد یکجا جمم شده در کوهان تور .
و آنرا بعربی ربا خوانند - و نام مئزلست از
جملهٌ بیست و هشت منزل غمرء و بضی کوند
اين ستاره ها دئبة حمل است‌نه کوهان نور. واول
اسح است .
ره ٩‏ بفتح اول و ثانی مشدد .حلقه
زدن لشکر باشد از سوار و پیاده بجهت شکار
وفیره - وخطی را نیز کویند که از سوار و پیاده
کشیده شود وآنرا بمربی صف خوانند؟" سودامن
وطرف و کنار؛ هرچیز را بیز گوند حمچو پرة
بیابان و پر بینی و پر کوه - و جزوی از ففل
که بدان محکم شود - وب رگکاه راهم کقده‌اند.
ر گرامی باشد - ویزبان پهلوی ماهی را گوشد.
و لقب پسر انوشیروان‌هم هست او چون‌اوماهی
خسرو دوم(یرویز) درشکار ( جلم نقره )
( زاره : صنایع امران ماستان)
بمپار دوست میداشت بدین سیب او دا پرویز
میگفنند. و مضمه پرویزن است؟ .وآن آلتی
باشد که بدان آرد + شکر و امتال آن بز ند »
و بستی کویند آلتی است مخصوص شکر بیختن
سو بیختن را نیز گوبند- وپروین را هم گفته‌اند
وآن سناره‌ای چنداست‌در کوحان ور - وبمعنی
۱ . نام نواده انوشیروان بر هرمزد چهارم ( ۵4۰ - ٩۷۷‏ مُ 3
۴ راك : پرویزن ۰ ۴ رگ : پروین . ناوت
0201۳5 صیغ جمم آمده (نیربشت بند۱۷). برخی‌از خاور شناسان آنرا به‌پروین ترجمه
کرده‌اند (رك : بعتها اس ۳4۵ ؛ ۲ ص ۳۵۵)» افنانی ۳6۲۵196 . بلوچی 020۷2۲ « اسشق
۳۰۸ » درسفدی : بروی» خوارزمی: بروی» عربی: ثرباء فرانمه ۳۱6۱206 ونیز مثزل اول از
منازل قمرترد ابرانیان « گاه شماری می۲۰4 (بنقل‌از بندهش بوستی) و ص ۳۳۵ *.
 *‏ پهلوی۳۵۸۲۳2 (حاشیه - لبه ‏ کناره) «ناوادیا ۱۹۶ نیز بمعنی بال‌ویر « اونوالا
۰4 3 َ #
۷ آنکه آرندکته (انگور) رابکواره مت باارغان مینک لح
نه بتصاصتی کنند خلق اشاره نه‌یدیت یادشه مخواهد ازومال:
«منوچهری داعغانی ۱۳۶*.
```


## [2026-09-14T00:55:15.289Z] TOOL CALL #50: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T00:55:15.294Z] TOOL RESULT

```


```


## [2026-09-14T00:55:18.688Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pleh%E2%82%81-",
 "prompt": "Give the reconstructed root, its meaning, and the list of derived terms/descendants (especially Indo-Iranian, Avestan, Old Persian, Greek, Latin, Germanic)."
}
```


## [2026-09-14T00:55:20.417Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%A7",
 "prompt": "What is the Persian etymology given for برنا (barnâ) 'young'? Quote the Middle Persian and Avestan forms and any cited sources."
}
```


### [2026-09-14T00:55:24.680Z] TOOL RESULT

```
# Proto-Indo-European Root *pleh₁-

## Reconstructed Root and Meaning

The root is **\*pleh₁-** (perfective aspect), meaning **"to fill."**

## Key Derived Terms and Descendants

**Indo-Iranian:**
- Sanskrit: पॄ (pṝ)
- Proto-Indo-Aryan forms like píparti (present)

**Greek:**
- Ancient Greek πίμπλημι (pímplēmi) from reduplicated present
- πληρός (plērós) "full" → πλήρης (plḗrēs)

**Latin:**
- pleō and related forms
- plērus "full"

**Germanic:**
- Proto-Germanic \*fulką "folk" (from \*pl̥h₁-go-m)
- \*felu (from \*pélh₁-u-)

**Other Notable Descendants:**
- Old Irish ler "sea, ocean"
- Old Armenian ելից (elicʻ) "fill"
- Lithuanian pilti, Latvian pilt
- Ancient Greek πολύς (polús) "much" (from \*polh₁-ú-s)

The root exhibits multiple morphological formations including reduplicated presents, nasal-infix presents, and s-aorists across Indo-European language families.
```


### [2026-09-14T00:55:25.706Z] TOOL RESULT

```
# Persian Etymology of برنا (barnâ)

According to the Wiktionary entry, the Persian word برنا derives from Middle Persian with the following etymology:

**Middle Persian form:** The entry indicates a form needing Book Pahlavi script (ʾpwlnʾd /⁠aburnāy⁠/), described as "underage, youth" and identified as a Zoroastrian legal term.

**Avestan form:** The word was borrowed from Avestan 𐬀𐬞𐬆𐬭𐬆𐬥𐬁𐬌𐬌𐬎 (apərənāiiu, "underage"), which represents "the negative of" the Avestan pərənāiiu ("adult").

**Ultimate source:** Both derive from Proto-Iranian *pr̥Hnáh ("full, filled").

The entry notes this is "a Zoroastrian legal term borrowed from Avestan," indicating its religious and legal significance in ancient Persian culture. No specific published sources are cited beyond the linguistic reconstruction itself.
```


## [2026-09-14T00:55:33.735Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%88%D8%A8%D8%A7%D8%B4",
 "prompt": "What etymology is given for اوباش in Persian and in Arabic? Is it an Arabic plural (of وبش)? Quote."
}
```


## [2026-09-14T00:55:35.795Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D9%88%DB%8C%D9%86",
 "prompt": "What etymology is given for Persian پروین 'Pleiades'? Quote the Middle Persian and Avestan forms and any note about the root (paoirya- 'first' vs pouru- 'many')."
}
```


### [2026-09-14T00:55:36.736Z] TOOL RESULT

```
# Etymology of اوباش

According to the Wiktionary entry, اوباش is "Borrowed from Arabic _أَوْبَاش_ (ʔawbāš), plural of _وَبَش_ (wabaš)."

Yes, it is an Arabic plural. The etymology section explicitly states that the Persian word derives from the Arabic plural form, which is itself the plural of the singular Arabic word وبش (wabaš).
```


### [2026-09-14T00:55:40.088Z] TOOL RESULT

```
# Etymology of Persian پروین

Based on the Wiktionary entry, the etymology states that پروین derives from Middle Persian *plwyc* (/Parwēz/) in Pazand texts, with the Avestan form given as *paoiriiaeni*.

The entry does not explicitly discuss the root meaning or distinguish between theories about *paoirya-* ('first') versus *pouru-* ('many'). It simply presents the comparative forms across related languages:

**Quoted comparison:** "Compare with Avestan _paoiriiaeni_, Northern Kurdish _pêwir_, Central Kurdish _پێروو_ (pêrû)"

The entry provides the etymological chain but omits detailed analysis of the semantic root or competing etymological theories you've referenced.
```


## [2026-09-14T00:55:44.131Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D9%88%D8%A7%D9%86",
 "prompt": "What etymology is given for Persian فراوان 'abundant'? Quote the Middle Persian / Proto-Iranian forms and any cited sources."
}
```


## [2026-09-14T00:55:45.401Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1#Persian",
 "prompt": "What etymology is given for Persian پر (por) 'full'? Quote the Middle Persian, Avestan, Proto-Iranian and PIE forms."
}
```


### [2026-09-14T00:55:46.833Z] TOOL RESULT

```
Based on the Wiktionary page provided, **no etymology is given** for the Persian word فراوان (farâvân). 

The Etymology section explicitly states: "(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)"

Therefore, no Middle Persian or Proto-Iranian forms are cited, nor are etymological sources provided for this entry.
```


### [2026-09-14T00:55:49.886Z] TOOL RESULT

```
# Etymology of Persian پر (por) 'full'

Based on the Wiktionary entry, here are the etymological forms provided:

**Middle Persian:** The entry states it comes from Middle Persian /⁠purr⁠/, though the specific Middle Persian term is marked as requiring verification.

**Proto-Iranian:** "*pr̥Hnáh"

**Avestan:** "𐬞𐬆𐬭𐬆𐬥𐬀" (pərəna) - listed as Old Avestan

**Proto-Indo-European:** "*pl̥h₁nós"

The entry notes cognates in multiple languages including Russian полный (pólnyj), Lithuanian pilnas, Italian pieno, Welsh llawn, and English "full" to demonstrate the PIE root's widespread influence.
```


## [2026-09-14T00:55:57.148Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"frawān\\|frawan\\|frāwān\\|fra[wv]ān\" PHD.txt NYB_vol2_glossary.txt | head -10; echo \"--- MON faravan entry\"; grep -n -o \".\\{0,200\\}فراوان.\\{0,200\\}\" MON_part1.txt | head -3"
}
```


## [2026-09-14T00:55:58.256Z] TOOL CALL #58: WebSearch

```json
{
 "query": "فراوان ریشه‌شناسی حسن‌دوست فارسی میانه frawān etymology"
}
```


### [2026-09-14T00:56:01.212Z] TOOL RESULT

```
PHD.txt:219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
--- MON faravan entry
ugrep: error: error at position 90
\x80-\xbf][\x80-\xbf]*){0,200}
 exceeds complexity limits___/
```


### [2026-09-14T00:56:08.673Z] TOOL RESULT

```
Web search results for query: "فراوان ریشه‌شناسی حسن‌دوست فارسی میانه frawān etymology"

Links: [{"title":"فراوان - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%81%D8%B1%D8%A7%D9%88%D8%A7%D9%86/"},{"title":"محمد حسن دوست","url":"https://ensani.ir/fa/article/author/73236"},{"title":"بررسیِ «فرهنگِ ریشه‌شناختیِ زبانِ فارسی","url":"http://parsianjoman.org/?p=6278"},{"title":"حسن‌دوست: نوشتن «فرهنگ ریشه‌شناختی زبان فارسی» 16 سال زمان برد - ایبنا","url":"https://www.ibna.ir/news/232985/%D8%AD%D8%B3%D9%86-%D8%AF%D9%88%D8%B3%D8%AA-%D9%86%D9%88%D8%B4%D8%AA%D9%86-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87-%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-16-%D8%B3%D8%A7%D9%84-%D8%B2%D9%85%D8%A7%D9%86-%D8%A8%D8%B1%D8%AF"},{"title":"محمد حسن‌دوست - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86%E2%80%8C%D8%AF%D9%88%D8%B3%D8%AA"},{"title":"کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) اثر محمد حسن دوست | ایران کتاب","url":"https://www.iranketab.ir/book/40213-farsi-language"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"},{"title":"بررسیِ «فرهنگِ ریشه‌شناختیِ زبانِ فارسی - پارسی انجمن","url":"https://parsianjoman.org/6278/%D8%A8%D8%B1%D8%B1%D8%B3%DB%8C%D9%90-%D9%81%D8%B1%D9%87%D9%86%DA%AF%D9%90-%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C%D9%90-%D8%B2%D8%A8%D8%A7%D9%86%D9%90-%D9%81%D8%A7/"}]

I found search results related to your query. Here's what I found:

The search results provide information about the word "فراوان" (frawān) and Muhammad Hasandust's etymological dictionary work:

**About the word "فراوان" (frawān):**
The word means abundant, plentiful, or copious (بسیار, کثیر), and can also mean deep/profound (عمیق).

**About Muhammad Hasandust's Etymology Dictionary:**
Muhammad Hasandust is a researcher and specialist in ancient Iranian languages and an affiliated professor at Shahid Beheshti University. Hasandust is the author of the "Etymological Dictionary of Persian Language," which won the 33rd Book of the Year Award in the "Ancient Languages" category in 1394/2015, and was published in five volumes by the Academy of Persian Language and Literature in 1393/2014.

In this work, Hasandust traces the origin of each Persian word through Middle Persian/Pahlavi and its older forms in ancient Iran, and then refers to the word's roots.

However, the search results do not contain specific etymological information about "فراوان" from Hasandust's dictionary. To find that specific entry, you would need to access the dictionary directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T00:56:13.696Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%D8%B1%D8%A7%D9%88%D8%A7%D9%86/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for فراوان, including any bracketed origin tag such as [په.] (Pahlavi) or a Pahlavi/Avestan form, and the Dehkhoda entry's etymological remarks."
}
```


## [2026-09-14T00:56:15.002Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/plenty",
 "prompt": "Give the etymology chain for 'plenty' (Old French, Latin plenus/plenitas, PIE root) and any mention of the PIE root *pele-."
}
```


### [2026-09-14T00:56:19.505Z] TOOL RESULT

```
# Lexicographic Entry for فراوان

## Farhang-e Mo'in (معین) Entry

According to Mo'in's dictionary: "(فَ) (ص .) بسیار، زیاد" — meaning "abundant, much" with the phonetic marker (fă) and grammatical tag (adjective).

## Dehkhoda Etymology

The Dehkhoda dictionary notes the word's origins: "در زبان اوستایی فرونگ و در کردی فراون است" — tracing the term to Avestan *frōng* and Kurdish *faravan*, establishing its ancient Indo-Iranian roots.

The entry further explains that in Kurdish dialects, the suffix "-van" is added to words to indicate abundance, with examples like *ganjvan* (a region) and *marivan* (a Kurdish city), where the base root conveys the primary meaning and "-van" intensifies it.

This suggests **فراوان** comprises *frā-* (meaning "much/abundant") plus the suffix *-van*, a common Persian construction for adjectives denoting abundance or intensity.
```


### [2026-09-14T00:56:19.645Z] TOOL RESULT

```
# Etymology Chain for "Plenty"

**Old French → Latin → PIE Root**

The word "plenty" traces back through Old French *plentee* (from the 12th century) to Latin *plenitatem* (nominative *plenitas*), meaning "fullness."

**Latin Foundation**

The Latin root *plenus* means "full, filled, greatly crowded; stout, pregnant; abundant, abounding; complete."

**Proto-Indo-European Origin**

This ultimately derives from the PIE root *\*pele-* (1), which means "to fill." The etymological dictionary notes this as the foundational source underlying the entire word family.

**Semantic Development**

The meaning evolved from mid-13c. usage denoting "abundance; as much as one could desire; an ample supply," later expanding to mean "a large amount, a great deal" by the early 14th century, and eventually "condition of general abundance" by the late 14th century.
```


## [2026-09-14T00:56:32.767Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor w in ['فراوان','پروین','برنا','انبار','اوباش']:\n    for i,p in enumerate(t):\n        if w in p:\n            m=re.search(r'\\[pdf page (\\d+)\\]',p)\n            print(w,'leaf',i,m.group(1) if m else '')\n            break\nEOF"
}
```


### [2026-09-14T00:56:33.862Z] TOOL RESULT

```
فراوان leaf 4 5
برنا leaf 54 55
```


## [2026-09-14T00:56:37.177Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'فراوان' in p:\n        j=p.find('فراوان')\n        print('leaf',i, re.search(r'\\[pdf page (\\d+)\\]',p).group(1) if re.search(r'\\[pdf page (\\d+)\\]',p) else '')\n        print(p[max(0,j-600):j+600])\n        print('-----')\nEOF"
}
```


### [2026-09-14T00:56:38.323Z] TOOL RESULT

```
leaf 4 5
37۸3) بکار می‌رود.
علت از رونق افتادن واژه‌های «آریا» و «آرین» و (آریایی» چه بود؟
در چند دهه‌ی قبل از جنگك جهانی دوم» برخی از دانشمندان اروپایی واژه‌ی» «آریایی» را نه
تنها در اشاره به یک خانواده‌ی بزرگك زبانها بلکه در اشاره به تیره‌ی بخصوص از نژاد سفید بکار
می‌بردند و وپژگی‌های بدنی و اجتماعی و فرهنگی آنان را مورد ستایش قرار می‌دادند. در دوران
تسلط نازی‌ها در آلمان» واژه‌ی «آریای؛ 2۸/۹۸۵ اهمیت ریژه‌ای پیداکرد. نازی‌ها ‏ فاشیست‌ه
باور می‌کردند که آریایی‌های راستین مردمی بلند قامت با چشمان آبی ر موی طلایی بودند که از نظر
نژادی بر سایرین برتری کامل داشتند. چون در آلمان و اسکاندیناوی اینگونه مردم فراوان ترند؛ آنها
معتقد بودند که گهواره‌ی آریایی‌های ابرنژاد شمال باختری اروپا بوده و از آنجا به سرزمین‌های دیگر
کوج کردهاند. طی این کوج‌های متوالی؛ آریایی‌ه با بومیان هر محل درآمیختند و در نتیجه پاک و
برتری نژادی آنها کم شد. هر چه اين کوچگران از آلمان دورتر شدند؛ میزان آمیختگی خون آنها با
نژادهای «پست‌تر» بیشتر شد. بهمین دلیل در سرزمین‌های دور از آلمان درصد مردم چشم آبی و
موطلایی بسیار کمتر است.
به عبارت دیگر» نازی‌ها واژه‌ی «آریایی» راکه قبلاً په خانواده‌ای از زبانها اطلاق می‌شد به
عنوان یک برچسب نژادی و به منظور تأ کید برتری خودشان مورد تحریف قرار دادند. مثلاً در نظر
این نوادپرستان حتی «اسل
-----
leaf 13 14
ند؟ . .. :

این پرسش منطقی نیاز به جواب دارد: کاوش‌های باستانشناسی و واژگان غیر هند و اروپایی
قدیمی که در زبان‌های هند و اروپایی باستانی دیده شده نشان می‌دهد که قبل از ورود هند و
اروپائیان» بسیاری از بخش‌های اروپا و آسیا دارای بومیان اولیه بوده‌اند. در آبخست‌سانه‌ی (شبه
جزیره) ایبری (اسپانیا و پرتغال) سنگك نیشته‌هایی پدست آمده که به یکك زبان غیر هند و اروپایی قبل
از دوران آهن تعلق دارد.
(290-299 .77 ,8 تا تاه 700-817075۸1 0۳ ها52 موی (2)
زبان «باسکك» (8۸80178) که امروزه در بخش کوچکی از شمال خاوری اسپانیا و جنوب
باختری فرانسه تکلم می‌شود در گذشته بخش عمده‌ی اسپانیا را زیر پوشش داشته است. شواهد فراوان
نشان می‌دهد که پس از آمدن هند و اروپائیان» دامنه‌ی گسترش این زبان غیر هند و اروپایی به تدریج
کم شده است. در شمال و مرکز ایتالیا «اتروسکان‌هاء (177741780۸1758) تمدن درخشانی را به وجود
آورده بودند که آثار هنری آن در بسْیاری از موزه‌ها دیده می‌شود. ورود هند و اروپائیان از شمال.
باعث شد که این زبان و فرهنگك غیر هند و اروپایی نابود گردد. مدارکك موجود نشان می‌دهد که در
آسپای صغیر نیز اقوام غیر هند و اروپایی ("هوریان‌ها" 131771۸18 و "هتیک‌ها" ۳7108 ۸)
توسط هند و اروپائیان تازه وارد (هتیت‌ها" 111۳77188 و «فریجیان‌ها» 711۷01۸775 و
«ارمنی‌ها» و «یوتانی‌ها»)پرانداخته شدند.
در جنوب هندوستان نیز زبا
-----
leaf 16 17
[pdf page 17]
۸ ریشه‌های هندو اروپایی زبان فارسی ۰
فرانسه کهن اسپانیایی کهن .
4 را اه
فرانسه اسپانیای
موضوع دیگری نی زکه به تدریج برایشان مشهود شد این بود: خانواده‌های زبان‌های اروپایی با
هم شباهت‌های فراوان دارند در صورتیکه شباهتی میان این زبان‌ها و عبری (/218151#) وجود
ندارد. ولی چون هنوز پایبند داستان برج بابل بودند این عدم شباهت را ناشی از دانحراف» و «پستی»
زبان‌های معاصر می‌دانستند.
تسلط انگلستان بر هندوستان و یافت نوشتارهای کهن هندی
در سده‌ی هیجدهم میلادی انگلستان هندوستان را تصرف کرد. یکی از پیامدهای تماس
نزدیک شرق ر غرب در هند برخورد انگلیسی‌ها با نوشتارهای کهن هندی به ویژه سانسکریت بود. ."
برخی از آنان که فرهیخته تر بودند با شگفتی دریافتند که شباهت عجیبی میان سانسکریت و زبانهای
عجیی ال رس دس
اروپایی به ویژه زبان‌های کهن اروپایی وجود دارد. کمی بعد که به بررسی نوشتارهای کهن ابراني (ب
-----
leaf 26 27
وشتار در جزیره‌ی کرت و :
جنوب آبخست سان‌ی ونان پیدا کردند؛ شماری از این خشت‌هاکه قدیمی‌ترند (بنام ۸ 003۸13 ٍ
هنوز بطور قطعی خوانده و تفسیر نشده‌اند و احتمال مي‌رود که اصلاً هند و اروپایی نباشند. تعداد .|
دیگری از ان خشت‌ها (8 ج1.13773۸) که قدمت آنها به حدود ۱۲۰۰ سال پیش از میلاد می‌رسد به ۱
یکی از گویش‌های یونانی کهن به نام «مایمینی» (۸]۷253۸۳۸۵۷) نوشته شده‌اند. این نوشته‌ها و ۱
آثار باستانشناسی و وجود واژه‌های غیر هند و اروپایی (به ویژه نام مکان‌ها) در زبان یونان ی کهن نشان ..
می‌دهد که یونانیان بومیان اصلی آن سرزمین نبوده و به آنجا کوج کرده‌اند.
بعد از حدود ۸۰۰ سال پیش از میلاد به نوشته‌های فراوانی به زبان یونانی کلاسیک
05880 بل8510۸شا)) برمی‌خوریم. این منون تصویر کاملی از زبان و فرهنگك و ساختار

-----
leaf 30 31
) و مردمان ناشناخته دیگر به وجود
آمدند. ولی رشد آنها آنقدر سریع بود که از قرن چهارم تا قرن نهم میلادی از خاور تاکوه‌های اورال
و از باختر تا مرز باختری لهستان و از جنوب تا بلفارستان و مقدونیه را تصرف کردند. تاریخ احتمالی
انشعاب زبانهای نوین اسلاوی از زبان اسلاوی کهن» فرن پنجم میلادی یعنی همان دورانی است که.
آمپراتوری روم فروریز شد و زبانهای رومانس کم کم از لاتین جدا شدند.
زبان‌های اسلاوی با زبان‌های ایرانی خویشی نسباً نزدیکی دارند. بسیاری از واژه‌های
آسلاوی (مثلاً پارسی کهن "3۸0۸" به معنی و خدا اسلاوی کهن "8001 و با اوستایی
۰ به معنی مقدس اسلاوی کهن "81۷7770 از ایرانی اخذ شده‌اند. نام‌های محلی فراوانی
نیز از ریشه‌ی ایرانی هستند. مثلاً نام رودهای «دن» (00/1) و «دونتز» (0027875) و «دونپر)
(0۸(118758) و شاید «دانرب» (0۸/17288) از واژه‌ی ایرانی کهن - []2۸81 به معنی رودخانه
گرفتبه شده‌اند.
زبانهای بالتیک (۸615تآجکشاآ ۸771۳ 8)
: نوشتارهای وابسته به این زبان‌ها فقط حدود پانصد سال قدمت دارند ولی جالب این است که
این زبانها از نظر آوایی و واژگانی دستخوش دگرگونی زیادی نشده‌اند و شباهت آنها با زپانهای هند و.
اروپایی کهن به ویژه سانسکریت و اوستایی چشمگیر است. بهمین دلیل در همسنجی‌های زبانشناسی
تاریخی» وجود همریشه‌های بالتیکی (به ویژه لیتوانی) از اهمیت خاصی پرخوردار است.
از میان سه زبان بالتبگی» 
-----
leaf 37 38
ی نسبت به رئیس
ایل بود. تبعید پا طرد از ایل شدیدترین نوع تثبیه محسوب می‌شد.
یکی از بارزترین ره آوردهای زبانشناسی» شناخت نقش شاه در جامعه‌ی هند و اروپایی
نخستین بود. شاه پا پادشاه نقش نظامی عمده‌ای نداشت. مهمترین نقش او میانجیگری میان انسانها و
خدایان بود. او نیاز انسان‌ها را (همراه با نیایش و قربانی) به خدایان اظهار می‌کرد و آنان در مقابل
برکات و عنایات خود را بر انسانها ارزانی می‌داشتند. متون ایرلندی و یونانی و هندی باستان نه تنها
موضرع فوق را تأیید می‌کنند بلکه حاکی از آنند که شاه با سرپرستی مراسم نیایش و دار ببودن
ویژگی‌های ابر انسانی ضامن خوبی محصول و زایندگی دام‌ها و پر ماهی بودن رودها و فراوانی
فرزندان و دوردازی دشمنان و پیماری‌ها هم بود. نیمه خدایی بودن شاه (معمولاً با مادرش الهه بود یا
هسرش) پیامد دیگری نیز داشت: مقام او والاتر از مقام پدر و رئیس ابل بود ولی آنها راکاملاً
تحت‌الشعاع قرار نمی‌داد. شاه در بالای هرم قدرت قرار داشت ولی پدر و رئیس ابل نیز هر یک
اختبارات ویژه‌ی خود را داشتند و در رأُس هرم‌های کوچکتری قرار داشتند.
هند و اروپائیان محتملاً دارای جرگه يا شوراهای مرکب از ریش سفیدان يا اعیان و اشراف
پردندکه نه تنها در بسیاری از امور مورد مشورت شاه قرار می‌گرفتند بلکه گهگاه نیز در برکنار سازی
شامان بی لیاقت نقش اساسی داشتند. مجلس سنای روم باستان (57381۸7 173۳) و شورای گ
-----
leaf 44 45
ماً به عهده‌ی من است. البته هرکجا که کاملاً مطمشن 8
نبوده‌ام با بکار بردن «شاید؛ در جلو واژه به خواننده هشدار داده‌ام. امید غایی من این است که دراین 8
زین هم پژوهشگران آینه بناندکاری راک این کتاب آغازکرده است دابا لکند و جایگاه استین
زبان فارسی در درخت خانوادگی زبان‌های هند و اروپایی را مشخص‌تر و کامل تر نمایند. این کتاب:
فقفط‌گامی در این سفر دراز و پر شگفتی است.
برخی از ویژگی‌های دیگر این کتاب ۱
۱-در این کتاب از ذ کر معنی(های) هر واژه خودداری شده است. علت این است: واژه‌های و
هند و اروپایی نخستین (مانند واژگان هر زان دیگر) هر یک دارای معنی (یا معانی) خاصی بودند.
ولی تعیین این معنی‌ها با ابهام فراوان همراه است چون اگر در زبان‌های هند و اروپایی امروزین
واژه‌های همریشه همه دارای معنی همسانی بودند آنگاه می‌توانستیم با اطمینان پیشتر ننیجه بگبریم؟ و
در هند و اروپایی نخستین هم همین معنی را داشته‌اند. ولی په استتای موارد معدود (مثلاً واژه‌ی
«مادر) یا «گاوه با «بوغ) معنی واژه‌های همریشه در زیانهای هند و اروپایی امروزی کاملدً یکی و
نیست. گذشت زمان و برخورد با پرگیرها وگیاهان و جانوران متفاوت موجب دگرگونی واژه‌ها شده
است. مثلاً ریشه‌ی هند و اروپایی 1۳87" با 1۸" در فارسی نوین شده است «سخت»؛ در

-----
leaf 46 47
 عهد کهن نیز امکان هر گونه
ا همریشگی رانفی می‌کند.
۳-پاید اصول آوایی و قوانین دگرگونی آوایی در زبان‌های گوناگون را مد نظر داشت. مثلاً
چون حرف آغازین ۲ در واژه‌های انگلیسی کهن تبدیل به 13 شده است می‌توان نتیجه گرفت که
واژه‌ی لاتین ۳1۸7 و واژه انگلیسی کهن 118100 (به چم «پنهان کردن») همریشه‌اند ولی
: راژه‌ی لانین 217۸ با واژه‌ی انگلیسی کهن 23۸17 (انگلیسی نوین 0۸۹78) علیرغم شباهت
ظاهری» همریشه نیست.
۴ در همسنجی و ریشه‌یابی واژه‌ها باید تمام اجزاء واژه را مورد بررسی قرار داد و هرگونه:
دگرگونی آوایی را طبق قوانین فونتیک توجیه کرد.
۵ توضیحات افسانه مانند درباره‌ی ریشه‌ی واژه‌ها را باید با شک و تردید فراوان مورد

-----
leaf 158 159
رانا
ساکسونی کهن (542)01 ص01): ات5 گالی (4ل5لانا0۸): ۷ه1
فریزی کهن (/(54ل7# 010): ات5 م50 ولزی (4کا): #تاهاآ
آلمانی کهن (۷ل02704۸ 104 00): ,301 آلبانی (4(0/لمقتم: 8۲307 ,۵7
آلمانی ((057۵14): ۷0
انگلیسی کهن (ن8الا20 00): ۰ ات۲ پسگشت‌ها اشگررت تن
۱ انگلیسی (130ا8(0): ات5 99 ۶0/0800
دانمارکی (0۸(184): ۲1۵ 3 (تات#) ری ای نا
سوئدی (5(7/515): قالا5۲ 1 (۴]213) بقتق ما0۸
نروژی (۸/07۳20۵(۷): ب۴013 8 (53) :24۸6522
هلندی (00762): ۷ 931 لاه
اسلاوی کهن (ع1/اما5 نان صا): 8 (۲) :010۸/3
7 .. |[ 228 (لاه) وا دی رم
لهستانی (57ل/0): 21 43 +247
روسی (/8554): ۰ ۳0۵۲۷۲۲۲ ,80127 برهان قاطع : ۳۷۵
یادداشت,
بازگشت به: فراوان
اوستایی (۷ل۸587۸): سانسکریت (84(/57077):
۸۵۸ ,۳۸35۲۳۸ ۸ ۳۸3۵۷2
پهلری (۲1اماتلم۳): 8۸ ,817 آلمانی کهن (/(0272/۸ لها صا): 7۸3۵
کردی (0/57م): 3 انگلیسی کهن (نز5ابا8(0 010): 78۸0
بلوچی (/[علالم8): 3زا لیترانی (1۸(لهلا7/): ۸5
افغانی (پشتی) (//7۸۸ل470): 5/0۸ لنرنی (لتی) (۸7۵24ت): نییان

-----
leaf 388 389
[pdf page 389]
ااا ا ‏ گ 6
۰ /_فراوان
سانسکریت (5(/5777): لنونی (لتی) (77۸2ما): ختاقق۸+.
,۸۵۸5 +1678 ۰
37 ۱1۸8117۸75 ب[۸5لا۸تاکن۸ 26 پسگشت‌ها 1۸۰ 1
ارمنی (۸(4071401): ۱/0۸۸۵ مارد و رورم هه
گوتیک (00771/0), ۸ 9 (13اهنام) :قت#مازم 02
آلمانی کهن (0270440 بلواتز صان): َ :28 اهر
داز ی دا 5 (۲0۳00177183 ,۲07657)
انگلیسی کهن 20/080 صا۵): انمق ۲2 131 ناه
لیتوانی (/۸امتا 2 7/): انا برهان قاطع + ۱۳۴۸
یادداشت:
چم این واژه در زبان‌های ژرمنی: آزردن» دردسر و نگرانی. :
اوستایی (/۸۲25742): ۳3۸۸3۰ ,8010180۰ 780۸ بش78
پارسی باستان (2588/۵07 صان): ای هلندی (ل0070م: ۷8
پهلوی (۷1هاتله): 7 ,لا 57 لینوانی (/(4الههتا7#لرم. ۳05
کردی (54ا80). ۳ ایرل
-----
```


## [2026-09-14T00:56:53.258Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; python3 - <<'EOF'\nt=open('FFD_pages_faseng.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nprint(t[35][:1800])\nEOF"
}
```


### [2026-09-14T00:56:54.405Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'FFD_pages_faseng.txt'
```


## [2026-09-14T00:56:56.861Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; ls; python3 - <<'EOF'\nt=open('FFD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nprint(t[35][:1800])\nEOF"
}
```


### [2026-09-14T00:56:57.914Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
115
[pdf page 36]
ماد»‌های ماضی و مضارع قارسی دری سس ۲۱
4 پیشوند فعلی است. ريشهٌ 128 به معنی «نهادن» و «افگندن» است. از 127 در فارسی
دری «آگندن» و «پراگندن» هم آمده‌اند > آگندن و پراگندن. در ایرانی باستان 8۵8
دیگری هم بوده است که از آن «کندن» آمده است > کندن.

افگن < فارسی میانه 20827 < ایرانی باستان ۳۵08-۵-۵. برای ۵ -> آرای.

انباردن.» انباشتن

انبارد < فارسی میانه ۳۵۳0276* < ایرانی باستان 82-037-12*. برای 2 > آراست.
0 پیشوند فعلی است. 037 صورت بالاندةٌ ریشهٌ 07 است» به معنی «پرکردن». از 087
«اوباردن» هم آمده است > اوباردن. «انباشت» در فارسی دری به قیاس با «کار»
«کاشت)» به وجود آمده است.

انبار + فارسی میانه 127003 < ایرانی باستان 1۵:۳-037-2*. برای 2 -> آرای.

انجامیدن

«انجامید» مادةٌ ماضی جعلی است» از مادهٌ مضارع ساخته شده است. مادةٌ ماضی
«انجام» در فارسی میانه 1272[311 بوده است.

بازماندةٌ 31-12[-82۳* ایرانی باستان است. برای 1۵ -> آراست. 1470 پیشوند
فعلی است. 31[ به جای 370[ آمده است. در فارسی میانةٌ مانوی 18۳831۲ و 82۳2211
به‌جای 1۵0[311 آمده است.

انجام ج فارسی میانه 822[370 + ایرانی باستان 370-8[-822*. برای 2 -> آرای. 1
پیشوند فعلی است. 8/[370 صورت بالاندهٌ ریشهٌ 8/1270 به معنی «حرکت کردن» است.
صورت بالاندةُ ريشهٌ 8/[87 معنی واداری دارد و با پیشوند فعلی 1۵70 به معنی
«به‌هم آوردن») است. «آمدن» و «فرجامیدن) هم از 8/1370 آمده‌اند > «آمدن؛ و
«فرجامیدن».

انداختن
انداخت + فارسی میانه 8228371: طرح کردن» برنامه‌ریزی کردن. سعدی در بوستان
```


## [2026-09-14T00:57:08.074Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; python3 - <<'EOF'\nt=open('FFD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'اوباردن' in p:\n        print('=== leaf',i)\n        j=p.find('اوباردن')\n        print(p[max(0,j-300):j+900])\nEOF"
}
```


### [2026-09-14T00:57:09.182Z] TOOL RESULT

```
=== leaf 35
استان 8۵8
دیگری هم بوده است که از آن «کندن» آمده است > کندن.

افگن < فارسی میانه 20827 < ایرانی باستان ۳۵08-۵-۵. برای ۵ -> آرای.

انباردن.» انباشتن

انبارد < فارسی میانه ۳۵۳0276* < ایرانی باستان 82-037-12*. برای 2 > آراست.
0 پیشوند فعلی است. 037 صورت بالاندةٌ ریشهٌ 07 است» به معنی «پرکردن». از 087
«اوباردن» هم آمده است > اوباردن. «انباشت» در فارسی دری به قیاس با «کار»
«کاشت)» به وجود آمده است.

انبار + فارسی میانه 127003 < ایرانی باستان 1۵:۳-037-2*. برای 2 -> آرای.

انجامیدن

«انجامید» مادةٌ ماضی جعلی است» از مادهٌ مضارع ساخته شده است. مادةٌ ماضی
«انجام» در فارسی میانه 1272[311 بوده است.

بازماندةٌ 31-12[-82۳* ایرانی باستان است. برای 1۵ -> آراست. 1470 پیشوند
فعلی است. 31[ به جای 370[ آمده است. در فارسی میانةٌ مانوی 18۳831۲ و 82۳2211
به‌جای 1۵0[311 آمده است.

انجام ج فارسی میانه 822[370 + ایرانی باستان 370-8[-822*. برای 2 -> آرای. 1
پیشوند فعلی است. 8/[370 صورت بالاندهٌ ریشهٌ 8/1270 به معنی «حرکت کردن» است.
صورت بالاندةُ ريشهٌ 8/[87 معنی واداری دارد و با پیشوند فعلی 1۵70 به معنی
«به‌هم آوردن») است. «آمدن» و «فرجامیدن) هم از 8/1370 آمده‌اند > «آمدن؛ و
«فرجامیدن».

انداختن
انداخت + فارسی میانه 8228371: طرح کردن» برنامه‌ریزی کردن. سعدی در بوستان

=== leaf 37
 + فارسی میانه 12888 + ایرانی باستان ۸۵۳-۴۵۵۳1۵*. برای 1۵ >
آراست. 1800 پیشوند فعلی است. ان صورت اصلی 8۳ است» 1 پیش از 1 به # بدل
شده است. ريشةٌ 8۷« ریشه‌ای است فرضی و معنی فرضی آن هم می‌تواند
«حرکت‌کردن» باشد.
انگیز ج فارسی میانه 128857 < ایرانی باستان ۵-:-82۵*. برای 8 - آرای. ‏
به‌جای ۴ آمده است.
اوباردنء اوباشتن
اوپارد + فارسی میانه 60370 < ایرانی باستان 3۷۵-037-12*. برای 1۵ -> آراست. 48
پیشوند فعلی است. 037 صورت بالاندهٌ ريشهٌ 087 است. 087 به معنی «پر کردنْ» است.
انباردن هم از ريشهٌ 0۵7 به معنی «پر کردن» آمده است > انباردن. «اوباشت» به قیاس با
7 و 331 به وجود آمده است.
اوبار < فارسی میانه 6037 < ایرانی باستان ۴*۵۷/۵-037-8. برای ۵ -> آرای.
```


## [2026-09-14T00:57:21.834Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/poly-",
 "prompt": "Give the etymology of the prefix poly-: Greek polys, PIE root, and how it entered English/French. Also note polygon, polygamy."
}
```


## [2026-09-14T00:57:22.966Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/full",
 "prompt": "Give the etymology of 'full' (adj) — Old English full, Proto-Germanic *fullaz, PIE root — and of the verb 'fill'."
}
```


### [2026-09-14T00:57:26.846Z] TOOL RESULT

```
# Etymology of Poly-

**Origin:** The prefix derives from Greek *polys* meaning "much" (plural *polloi*), ultimately tracing to the PIE root *\*pele-* "(1) to fill," which carries connotations of abundance and multitudinousness.

**Entry into English:** It functions as a word-forming element meaning "many, much, multi-, one or more." The prefix is considered equivalent to Latin *multi-* and is properly applied to compounds with Greek-origin words.

**Chemical Usage:** In scientific nomenclature, it typically designates compounds containing a large number of identical atoms or molecular units.

**Related Words:** Two notable examples mentioned in the source include:
- **Polygon:** While not explicitly detailed, this combines *poly-* with the Greek element for "angle"
- **Polygamy:** Pairs *poly-* with the Greek element for "marriage"

The source confirms this prefix became established in English through Greek-origin scientific and technical terminology, particularly in chemistry and botany, where compounds like "polymer" (1855) and botanical classifications emerged.
```


### [2026-09-14T00:57:28.337Z] TOOL RESULT

```
# Etymology of "Full" (Adjective) and "Fill" (Verb)

## Full (Adjective)

**Full** traces back to Old English *full*, meaning "containing all that can be received; filled; perfect, entire." It derives from Proto-Germanic *fullaz, which appears across related languages (Old Saxon *full*, Dutch *vol*, German *voll*, Old Norse *fullr*). The ultimate origin is the Proto-Indo-European root *pele- (1), signifying "to fill."

## Fill (Verb)

**Fill** has a distinct pathway. The noun *fill* emerged in the mid-13th century from Old English *fyllu*, denoting "fullness" and "satiety." This noun derives from Proto-Germanic *full-ino- ("fullness"), itself a noun of state formed from *fullaz* ("full"). The related verb *fill* shares this same Germanic root system, ultimately connecting back to the PIE *pele- root meaning "to fill."

Both words thus belong to the same etymological family centered on the concept of fullness and filling, though they developed somewhat differently across Old English and Germanic languages before entering Middle English.
```


## [2026-09-14T00:57:44.560Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pleh%E2%82%81-\" \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%A7\" \"https://en.wiktionary.org/wiki/%D8%A7%D9%88%D8%A8%D8%A7%D8%B4\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D9%88%DB%8C%D9%86\" \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D9%88%D8%A7%D9%86\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1\" \"https://abadis.ir/fatofa/%D9%81%D8%B1%D8%A7%D9%88%D8%A7%D9%86/\" \"https://www.etymonline.com/word/plenty\" \"https://www.etymonline.com/word/poly-\" \"https://www.etymonline.com/word/full\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 389, root Pel 1/Ple/Pelu: verification of por/anbar/borna/obash/parvin/faravan/full/plenty/poly-\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T00:57:50.356Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7f96bc1b8091524b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5660da974237acbf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a627c875489b277b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0f759a3c8f426920.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9dd188300eba7cda.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1a7bf5274f408ee0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ef02b841b51c0b62.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/512edd9af607d672.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4bb103de72947fea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0a99638fcef3bf5b.txt
```


## [2026-09-14T00:57:58.232Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--WLD Bd2\"; grep -n \"pouru\\|paourus\\|pərəna\\|parəna\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"--SYN full/many\"; grep -n \"19.43\\|'much, many'\\|13.15\" SYN.txt | head -5"
}
```


### [2026-09-14T00:57:58.310Z] TOOL RESULT

```
--WLD Bd2
3154:par usd-,      av.   paourusa-   u. pel „grau“).
3573:             av.             paourusa- „grau, greis“ (Bartholomae Wb. 903;
4339:     Ai. punl-.y av. pouru-^                     ap. paru ..viek'
--SYN full/many
2299:‘servant’ = W. gwas, Ir. foss ‘servant’, etc. (19.438).
2520:Russ. rebenok, deriv. of rob, Chil. rabu ‘servant’ (19.43).
3724:Lat. familia, orig. the ‘body of serv- ants, household’, then also ‘family’, deriv. of famulus ‘servant’ (19.43). Hence the Romance words, those of the modern Gme. languages, also Lett. familija and similar forms more or less
7864:Grk. Oeparebw ‘attend, do service, take care of’, hence esp. ‘treat medical- ly, cure’ : Grk. @epdwv ‘servant, attend- ant’ (19.43). Walde-P. 1.857. Boisacd 340 f.
14737:Du. ambacht, with preservation of the older form (the reg. development in Du. ambt ‘office’) : OHG ambahti, OF am- biht, Goth. andbahti ‘service, office’, derivs. of OHG ambaht, OF ambeht, Goth. andbahts ‘servant’ (19.43). Falk- Torp 189. Franck-v. W. 16.
```


## [2026-09-14T00:58:00.226Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4330,4350p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-14T00:58:00.285Z] TOOL RESULT

```
MU. YI 271 m. Lit.).
     Qotfidls^             edsl. fidlr^        ags. as. full, ahd. fol (-11-             .yVolU    ai. purnd-   nsw.,
s. o.);     =      lit.   pdnaSj abg. phm^ skr. piin                  „voli'*.

     pehi „Menge“ (und poluf) einzelsprachlich auch adjektivisch geworden
„Yiek‘   (s. J. Schmidt KZ. 32, 382, Bgm.  272, II‘^ 1, 177); daneben idg.
Pe?«-Adj. „Yiel“; Komp. ple-los,     Sup. ph-is-to- ,,mehr, meist“ woriiber
eingehendst Osthotf MU. YI S3 f.. 124ff. (zum Gr.), 251 ff. (zum Lat.), 269 f.
(zum Kelt.).
     Ai. punl-.y av. pouru-^                     ap. paru ..viek'
                                         (= gr. jxo?.vg, ^venn dies aus
Xvg,    lit.   pihis)y Komp. ai. prayah
                                Adv. „meistens, gewohnlich“ (s. auch Brug-
mann II- 2, 688, und zn prdyena, praijarali ds. Uhlenbeck AiWb. 180), av.
frayah-f sup. fraesta-,                   „-   de)r mehr(ere), meiste".
                                                    pelaq-                                                               65

  Gr. noXvg         (noXv^ noXvv: diese Beschrankung des St. noXv-, analog
der von fieyag, fieyav, jjLsya, deutet Brugmann 272, IP 1,177 aus ursprgl.
substantivischem ^nolv mit Yok. wie yovv, doqv', doch ist noXvg eher
nach J. Schmidt aaO. assim. aus Adj. "^jiaXvg                         =
```


## [2026-09-14T00:58:09.744Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"plenty, n\\..\\{0,260\\}\" KLN_1966.txt | head -3; echo ---; grep -n -o \"poly-, combining form.\\{0,240\\}\" KLN_1966.txt | head -3; echo ---; grep -n -o \"full, adj\\..\\{0,240\\}\" KLN_1966.txt | head -3; echo ---; grep -n -o \"manipulate.\\{0,220\\}\" KLN_1966.txt | head -2"
}
```


### [2026-09-14T00:58:10.835Z] TOOL RESULT

```
---
---
32384:full, adj.,  and  cp.  replum,  complete,  deplete, repletion,  n.,  surfeit;  fullness.  —  ME.  replecioun, ‘surfeit’,  fr.  OF.  (=  F.)  riplition,  of  s.m.,  fr.  Late L.  repletionem,  acc.  of  repletio,  ‘a  filling  up’,  fr. repletus,  pp.
---
15513:manipulate,  plebeian,  pleio-,  Pleisto¬ cene,  plenary,  plenty,  plenum,  pleonasm,  ple- rome,  plethora,  plethysmograph,  plural,  plus, plutarchy,  plutocracy,  poly-,  replenish,  replete, replum,  supplement,  supply,  te
22823:manipulate  and  -able, manipulate,  tr.  v.  —  Back  formation  fr.  manipul¬ ation.
```


## [2026-09-14T00:58:12.637Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '15505,15520p' KLN_1966.txt"
}
```


### [2026-09-14T00:58:12.687Z] TOOL RESULT

```
Fuirena,  n.,  a  genus  of  plants,  the  umbrella  grass (bot.)  —  ModL.,  named  after  the  Danish physician  and  botanist  Jorgen  Fuiren  (1581- 1628).
-ful,  adj.  suff.  meaning  ‘full  of’.  —  See  full,  adj. fulcrum,  n.,  the  support  on  which  a  lever  turns. —  L.,  ‘bedpost’,  fr.  fulcire,  ‘to  prop’,  which  is cogn.  with  Gk.  90)00]?,  ‘beam’,  9aXayL  ‘trunk, log,  line  of  battle,  battle  array’,  OE.  balca, ‘ridge’.  See  balk,  n.,  and  cp.  words  there  re¬ ferred  to.
fulfill,  fulfil,  tr.  v.  —  ME.  fulfitlen,  fr.  OE.  full- fyllan,  ‘to  fulfill’,  lit.  ‘to  fill  full’,  fr.  ful,  ‘full’, and  fyllan,  ‘to  fill’.  See  full,  adj.,  and  fill. Derivatives :  fulfill-er,  n.,  fulfil(l)-ment,  n. fulgent,  adj.,  shining.  —  L.  fulgens ,  gen.  -entis, pres.  part,  of  fulgere,  ‘to  shine’,  rel.  to  fulgur, ‘lightning’,  fulmen  (for  *fulg-men),  of  s.m., ft agrdre,  ‘to  blaze,  glow,  burn’.  See  black,  and cp.  effulgent,  refulgent,  fulminate.  Cp.  also flagrant.  For  the  ending  see  suff.  -ent. Derivatives:  fulgent-ly,  adv.,  fulgent-ness,  n. fulgid,  adj.,  glittering,  shining.  —  L.  fulgtdus,  fr. fulgere,  ‘to  shine’.  See  prec.  word  and  adj. suff.  -id.
Fulgora,  n.,  a  genus  of  insects,  the  lantern  fly (entomol.)  —  L.,  name  of  the  goddess  of  light¬ ning,  rel.  to  fulgus,  gen.  fulguris,  ‘lightning’.  See fulgent  and  cp.  next  word, fulgurant,  adj.,  flashing.  —  L.  futgurans,  gen. -antis,  pres.  part,  of  fulgurare,  ‘to  lighten',  fr. fulgur,  ‘lightning’,  which  is  rel.  to  fulgere,  ‘to shine’.  See  fulgent  and  -ant  and  cp.  foudroyant. fulgurite,  n.,  glassy  substance  produced  by  the passage  of  lightning  (geol.)  —  A  hybrid  coined fr.  L.  fulgur,  ‘lightning’  (see  fulgent),  and  -ite, a  suff.  of  Greek  origin.
fulham,  also  fullam,  fullom,  n.,  a  loaded  die.  — From  Fulham  in  London,  formerly  a  resort  of crooks.
Fulica,  n.,  a  genus  of  birds,  the  true  coot  (or- nithol.)  —  L.  fulica,  ‘coot’,  lit.  meaning  ‘having
a  white  spot  (scil.  on  the  head)’,  and  cogn.  with Gk.  9aXo?,  ‘white’.  See  full,  ‘to  thicken’, fuliginous,  adj.,  sooty.  —  Late  L.  fuliginbsus,  fr. L.  fuUgd,  gen.  fuliginis,  ‘soot’;  cogn.  with  OI. dhulih,  ‘dust’,  dhulika,  ‘fog’,  Lith.  dulis,  ‘fog, vapor',  fern.  pi.  ditlkes,  ‘dust’,  Lith.  dulsvas, ‘smoke-colored’.
Derivatives:  fuliginous-ly,  adv.,  fuliginous¬ ness,  n.
full,  adj.  ME.,  fr.  OE.  full,  rel.  to  OS.  full , OFris.  ful,  ON.  fullr,  Swed.  full,  Dan.  fit  Id, OHG.  fol,  MHG.  vol,  G.  roll,  Goth  .fulls,  ’full’, and  cogn.  with  OSlav.  plunu,  Lith.  pilnas,  OIr. Ian ,  W.  Hawn,  Bret,  leun,  L.  plenus,  OI.  purndlf, ‘full’,  Avcstic  plrena-,  ‘full’,  fr.  I.-E.  base  *pjnd-, ‘filled,  full’.  This  base  is  a  participial  derivative of  base  *pele-,  *ple-,  ‘to  fill’,  whence  Gk.  rz/ft- •9-eiv,  ‘to  be  full’,  7up,7rXavai,  ‘to  fill’,  7tXr]p7)?, ‘full’,  L.  plere,  ‘to  fill’.  Cp.  also  OE.  fela,feala, feola,  OFris.  felo,  fel,  OS.,  OHG.  filu,  MHG. v/V,  G.  viel,  Goth,  filu,  ‘much’,  OI.  purtih,  Gk. tioXu?,  ‘much’,  L.  plus,  ‘more’,  Lith.  pilus,  OIr. il,  ‘plenty’.  E.  folk  is  not  cognate.  Cp.  fill.  Cp. also  flow.  Cp.  also  accomplish,  complement, complete,  comply,  deplete,  expletive,  implement, maniple,  manipulate,  plebeian,  pleio-,  Pleisto¬ cene,  plenary,  plenty,  plenum,  pleonasm,  ple- rome,  plethora,  plethysmograph,  plural,  plus, plutarchy,  plutocracy,  poly-,  replenish,  replete, replum,  supplement,  supply,  terreplein. Derivatives:  full,  n.,  tr.  and  intr.  v.  and  adv., ful-ly,  adv.,  ful(l)-ness,  n.
full,  tr.  v.,  to  thicken  (cloth).  —  ME.  fullen,  fr. OE.  fullian,  ‘to  whiten,  full’,  fr.  OF .  foler,  fouler (F.  fouler),  ‘to  tread,  trample  on,  to  full’,  fr.  VL. *fullare,  fr.  L.  fulld,  ‘fuller’,  which  is  of  uncer¬ tain  origin.  It  is  perh.  cogn.  with  Gk.  9a Xo?, ‘white’,  ME.  balled,  ‘bald’,  orig.  ‘white’.  See bald  and  cp.  words  there  referred  to.  Proven?., Catal.  folar,  Sp.  hollar,  ‘to  full’,  also  derive  fr, VL.  *  ful Idre.  Cp.  foil,  ‘to  baffle’,  foulard. Derivative:  full-ing,  n.
fuller,  n.,  one  who  fulls.  —  ME.,  fr.  fullere ,  fr.
L.  fulld,  ‘a  fuller’.  See  full,  ‘to  thicken  (cloth)’, fuller,  n.,  a  grooving  tool.  —  Formed  fr.  full,  ‘to make  full’  (see  full,  adj.),  with  agential  suff.  -er. fulmar,  n„  an  arctic  sea  bird  resembling  a  gull. —  Compounded  of  ON.  full,  ‘foul’,  and  mar, ‘sea  mew’.  See  foul,  adj.,  and  mew. fulminant,  adj.,  fulminating.  —  L.  fulminans,  gen. -antis,  pres.  part,  of  fulmindre.  See  next  word and  -ant.
fulminate,  intr.  v.,  to  explode;  tr.  v„  to  cause  to explode;  to  denounce.  —  L.  fulmindtus,  pp.  of fulmindre,  ‘to  lighten,  to  hurl  lightnings’,  fr. fulmen,  gen.  fulminis,  ‘lightning’,  which  stands for  *fulg-men  and  is  rel.  to  fulgere,  ‘to  shine’.  See fulgent  and  verbal  suff.  -ate  and  cp.  fulmine. Derivatives:  fulminat-ing,  adj .  ,fulmination  (q.v), fulminatory  (q.v.)
fulminate,  n.,  a  salt  of  fulminic  acid  (chem.)  — See  fulminic  and  chem.  suff.  -ate.
fulmination
628
```


## [2026-09-14T00:58:18.055Z] TOOL CALL #73: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T00:58:18.110Z] TOOL RESULT

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


## [2026-09-14T00:58:20.541Z] TOOL CALL #74: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T00:58:20.596Z] TOOL RESULT

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


## [2026-09-14T00:58:51.107Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:06:34.912Z] TOOL CALL #75: Bash

```json
{
 "command": "mkdir -p \"/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\" && cat > \"/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-389.py\" <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pleh%E2%82%81-\"\nW_BARNA = \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%A7\"\nW_OBASH = \"https://en.wiktionary.org/wiki/%D8%A7%D9%88%D8%A8%D8%A7%D8%B4\"\nW_PARVIN= \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D9%88%DB%8C%D9%86\"\nW_FARAV = \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D9%88%D8%A7%D9%86\"\nW_POR   = \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1\"\nA_FARAV = \"https://abadis.ir/fatofa/%D9%81%D8%B1%D8%A7%D9%88%D8%A7%D9%86/\"\nE_PLENTY= \"https://www.etymonline.com/word/plenty\"\nE_POLY  = \"https://www.etymonline.com/word/poly-\"\nE_FULL  = \"https://www.etymonline.com/word/full\"\n\nPOK_NOTE = (\"POK_full.txt s.v. 'Root/lemma: pel-1, pelə-, plē-', Meaning 'full, to fill; to pour; town (?)', \"\n            \"Page(s): 798-801: 'Avestan par- \\\"füllen\\\"', 'purna- \\\"voll\\\" (= Gothic fulls ... whereas Avestan parana- \\\"gefüllt\\\")', \"\n            \"'Old Indic puru-, Avestan pouru-, ap. paru \\\"much, a lot of\\\" ... Avestan frayah-, Superl. fraesta- \\\"the meiste\\\"; \"\n            \"here Iran. *pelu-, *polu- in Plejadennamen npers. parv, Avestan paoiryaeini (*paruḭaini-)'.\")\nWLD_NOTE = (\"WLD_Bd2_pages.txt around p.64 f.: 'Gotisch fulls, ags. as. full, ahd. fol ... = ai. purnd- ...'; \"\n            \"'pelu-Adj. \\\"viel\\\"; Komp. ple-ios, Sup. ple-is-to-'; 'Ai. purú-, av. pouru-, ap. paru \\\"viel\\\" (= gr. πολύς) ... \"\n            \"av. frayah-, sup. fraesta- \\\"(der) mehr(ere), meiste\\\"'.\")\nAHD_NOTE = (\"AHD_watkins1985.txt s.v. 'pelə-1. To fill; with derivatives referring to abundance and multitude. Variant *plē- ...': \"\n            \"'Suffixed zero-grade form *pl̥-no-. 1. Germanic *fulnaz, *fullaz, full, in Old English full: FULL. 2. Derivative Germanic verb \"\n            \"*fulljan, to fill: FILL. 3. Latin root *plāno-, replaced by *plēno- ... plēnus, full: PLENARY, PLENITUDE, PLENTY ... \"\n            \"Old Latin plous in Latin plūs, more: PLUS ... O-grade form *pol(ə)-u- in Greek polus: POLY-'. [Pok. 1. pel- 798.]\")\nKLN_FULL = (\"KLN_1966.txt s.v. 'full, adj.': 'ME., fr. OE. full, rel. to OS. full ... Goth. fulls, \\\"full\\\", and cogn. with OSlav. plunu, \"\n            \"Lith. pilnas, OIr. lan, L. plenus, OI. purnah, \\\"full\\\", Avestic pərəna-, \\\"full\\\", fr. I.-E. base *pl̥nó- ... a participial \"\n            \"derivative of base *pele-, *plē-, \\\"to fill\\\" ... Cp. also ... manipulate, plebeian ... plenary, plenty, plenum ... plural, plus ... poly-'.\")\n\nentry = {\n \"entry\": 0,\n \"root\": \"Pel 1, Ple, Pelu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *pelh₁- / *pleh₁- 'to fill', with the u-stem *pelh₁u- 'much, many' (Pokorny pel-1, pelə-, plē-, pp. 798-801)\",\n \"note\": (\"Pokorny's lemma 'pel-1, pelə-, plē-' (IEW 798-801) is exactly Nourai's root box: section D is headed \"\n          \"'füllen, Fülle' and section 'pelu- Menge ... daneben idg. pelu- Adj. viel' covers his third variant Pelu. \"\n          \"Watkins/AHD writes the same root pelə-1 'To fill; with derivatives referring to abundance and multitude', \"\n          \"with the variant *plē-; in laryngeal notation it is *pelh₁- / *pleh₁-. Language label ('Indo-European') and \"\n          \"gloss ('to fill; a quantity of, a group of') are both right, the second half of the gloss being the *pelu- \"\n          \"'Menge/multitude' branch. Cross-cutting comment: the page mixes two sub-branches that modern handbooks keep \"\n          \"apart in detail but not in origin — the *pl̥h₁-nó- 'full' adjective (Av. pərəna-, NP por, Goth. fulls, L. plēnus) \"\n          \"and the *pelh₁u- 'much' quantifier (Av. pouru-, OP paru-, Gk. polús, comparative *pleh₁-yos > Av. frāyah-, MP frēh). \"\n          \"Horn (no. 294) insists on that distinction for Persian por. Two Persian items under the root are doubtful: \"\n          \"اوباش is an Arabic plural, and برنا goes back to the NEGATED Avestan apərənāyu-.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *pelh₁-/*pleh₁- «پر کردن» است که پوکورنی آن را زیر سرواژهٔ pel-1, pelə-, plē- در صفحه‌های ۷۹۸ تا ۸۰۱ \"\n             \"آورده و واتکینز (AHD) نیز همان را با معنی «پر کردن؛ با مشتقاتی به معنی فراوانی و انبوهی» ثبت کرده است. بنابراین نام، زبان و \"\n             \"معنی ریشه در نمودار نورایی درست است و بخش دوم معنی («مقدار، گروه») به شاخهٔ *pelh₁u- «بسیار» بازمی‌گردد. یادآوری کلی: در این \"\n             \"صفحه دو شاخه به هم آمیخته است؛ صفت *pl̥h₁-nó- «پر» (اوستایی pərəna-، فارسی «پُر»، گوتی fulls، لاتین plēnus) و کمیت‌نمای \"\n             \"*pelh₁u- «بسیار» (اوستایی pouru-، پارسی باستان paru-، یونانی polús و برترِ *pleh₁-yos > اوستایی frāyah- و پهلوی frēh). \"\n             \"دو مدخل فارسی این صفحه پذیرفتنی نیست: «اوباش» معرّب/عربی است و «برنا» از صورت منفیِ apərənāyu- آمده است.\"),\n \"sources\": [W_PIE, E_FULL],\n \"ref_check\": [\n   {\"ref\": \"POK:799\", \"status\": \"supports\",\n    \"note\": POK_NOTE + \" Nourai's page 799 falls inside the lemma's range 798-801.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 63 ff. (printed p. 64-65)\", \"stance\": \"supports\", \"note\": WLD_NOTE},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. pelə-1\", \"stance\": \"supports\", \"note\": AHD_NOTE},\n   {\"src\": \"IEC\", \"where\": \"Mann, p. 918 (pelu-) and p. 975 (poluos 1)\", \"stance\": \"supports\",\n    \"note\": \"IEC.txt: 'pelu \\\"much, many\\\". Cf. polu, poluos, peluð, peln-. WP II, 65'; and 'poluos (1) (polus, polu) \\\"big, full; much, many, abundant\\\" ... Av. paourus, pourus ... OPer. cf. parav ... Per. cf. farawan'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. 'full, adj.' (vol. 1, p. 627)\", \"stance\": \"supports\", \"note\": KLN_FULL}\n ],\n \"nodes\": []\n}\nN = entry[\"nodes\"]\n\ndef node(i, lang, words, verdict, der, der_fa, sources, refs, cons):\n    N.append({\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n              \"derivation\": der, \"derivation_fa\": der_fa, \"sources\": sources,\n              \"ref_check\": refs, \"consulted\": cons})\n\n# ---------------- node 1\nnode(1, \"Avestan\", \"par 1, perana; ham-par; perana-âyu\", \"confirmed\",\n \"Avestan has a verb 1par- 'to fill' (Bartholomae AiW col. 850: \\\"j., g. 1par- V. 'füllen'\\\", present pərəna-/pipar-) whose \"\n \"perfect passive participle is pərəna- 'gefüllt, voll' (AiW col. 894, from *pl̥h₁-nó-, = Skt. pūrṇá-, Goth. fulls). \"\n \"The compound with the preverb hąm- is attested: hąm.pāfrāiti 'he fills (the belly) with' (Vd. 5.48), which Bartholomae \"\n \"himself glosses by citing 'np. anbārad \\\"er füllt ein\\\"'. pərənāyu- is the u-stem 'of full life/age, adult' (MacKenzie's \"\n \"MP purnāy [pwln'd] '= Av. pərənayu-, adult'); its a-privative apərənāyu- 'under age, minor' is the far commoner Avestan \"\n \"word. Nourai's gloss 'full of life' is a literal rendering of pərəna- + āyu- 'lifetime'; the idiomatic sense is 'of full age'. \"\n \"Loss of the laryngeal and the Iranian outcome *pr̥Hna- > Av. pərəna- are regular.\",\n \"در اوستایی ریشهٔ par- «پر کردن» (بارتولومه، ستون ۸۵۰) با اسم مفعول pərəna- «پُر، پرشده» (ستون ۸۹۴، از ایرانی باستان *pr̥Hna-، \"\n \"هم‌ریشه با سنسکریت pūrṇá- و گوتی fulls) به کار رفته است. صورت پیشونددار hąm-par- در وندیداد ۵:۴۸ به شکل hąm.pāfrāiti «شکم را \"\n \"پر می‌کند» آمده و خودِ بارتولومه در ذیل آن به «انبارد» فارسی نو ارجاع داده است. pərənāyu- نیز «به سنّ کمال رسیده، بالغ» است \"\n \"(مکنزی: پهلوی purnāy «بالغ» = اوستایی pərənayu-) و صورت منفی آن apərənāyu- «نابالغ، صغیر» بسامد بیشتری دارد. برگردان نورایی \"\n \"(«سرشار از زندگی») ترجمهٔ تحت‌اللفظی pərəna- + āyu- است. ادعای نورایی در این گره درست است.\",\n [W_PIE],\n [{\"ref\": \"POK:799\", \"status\": \"supports\", \"note\": POK_NOTE + \" Pokorny explicitly lists 'Avestan par- \\\"füllen\\\"' and 'Avestan parana- \\\"gefüllt\\\"' in section D on p. 799.\"}],\n [{\"src\": \"BRT\", \"where\": \"AiW col. 850 (1par-), col. 894 (pərəna-), col. 858 (pərənāyu-/apərənāyu-)\", \"stance\": \"supports\",\n   \"note\": \"BRT.txt: \\\"j., g. 1par- V. 'füllen'. Praes. ... mit ham 'füllen mit -' (Gen.): yō gə̄uš unhwąn hąm.pāfrāiti 'wer den Bauch mit Fleisch füllt' V.5.48 ... ai. pṛṇāti; np. anbārad 'er füllt ein'\\\"; and \\\"j., g. 1pərəna- Adj. 'gefüllt, voll' ... PPfP. zum V. 1par-. — np. pur. got. fulls; ai. vgl. pūrṇá-. — Pü.: purr\\\".\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie p. 70 / addenda\", \"stance\": \"supports\",\n   \"note\": \"PHD.txt: 'purnāy [pwln'd = Av. pərənayu-] adult'; 'purr (MALE < A mlh; pul | M pur, N ~) full'. The Pahlavi reflexes of both Avestan items are in place.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 64 f.\", \"stance\": \"supports\", \"note\": WLD_NOTE}])\n\n# ---------------- node 2\nnode(2, \"Persian\", \"por «پُر»; anbâr «انبار»; bornâ «برنا» (+ انباردن، انباشتن)\", \"plausible\",\n \"por «پُر» 'full': Av. pərəna- > MP purr [pul] (MacKenzie) > NP por; the geminate -rr- of Pahlavi comes from *-rn- (assimilation \"\n \"of *pr̥Hna-), and Horn no. 294 explicitly derives np. pur from aw. pərəna-, skt. pūrṇá- and argues AGAINST Geiger's derivation \"\n \"from Av. pouru- 'much' ('deren Bedeutung nicht passt') — confirmed. \"\n \"anbâr «انبار» 'store, granary' + انباردن/انباشتن: from OIr. *ham-pāra- / *ham-pār-ta- 'filled up together', MP hambārdan/ambāštan; \"\n \"Horn no. 111 gives 'enbāštan \\\"anfüllen, anhäufen\\\", Praes. enbār-em, enbārden, enbār; aw. hąm + √par, hampāfrāiti; phlv. anbārtan, \"\n \"anbār' and Abolqasemi (FFD p. 31) 'انبارد < فارسی میانه *hambārd < ایرانی باستان *ham-pār-ta ... PĀR صورت بالاندهٔ ریشهٔ PAR ... به معنی پر کردن' \"\n \"— confirmed; انباشتن is a later Dari analogical past stem (Abolqasemi: 'به قیاس با کار/کاشت'). \"\n \"bornâ/barnâ «برنا» 'young' is the weak link: the word does NOT continue pərənāyu- 'adult' but its a-privative apərənāyu- 'under age', \"\n \"MP abarnāy/awarnāy [ʾpwlnʾd] 'minor, youth' > NP burnā/barnā, with *rn preserved (Hübschmann, Pers. Stud. §§ on rn: 'burna, barnā \"\n \"\\\"Jüngling\\\", zd. apərənāyu-'). Semantically 'not yet of full age' → 'young man'. So the root is right but the parent form is the \"\n \"negated one, not the positive perana-âyu of the chart.\",\n \"«پُر» از فارسی میانهٔ purr (مکنزی: pul) و آن از اوستایی pərəna- «پر» می‌آید؛ خوشهٔ *rn در پهلوی به rr همگون شده است. هرن (شمارهٔ ۲۹۴) \"\n \"همین را می‌گوید و صریحاً نظر گایگر را که «پُر» را از pouru- «بسیار» می‌گرفت رد می‌کند، زیرا معنی سازگار نیست. «انبار» و «انباردن» \"\n \"بازماندهٔ ایرانی باستان *ham-pāra-/*ham-pār-ta «با هم پر کرده» است؛ هرن (شمارهٔ ۱۱۱) و ابوالقاسمی (مادّه‌های فعل‌های فارسی دری، ص ۳۱) \"\n \"هر دو آن را از پیشوند ham- و ریشهٔ par «پر کردن» گرفته‌اند و «انباشتن» ماضیِ قیاسی متأخرِ دری است. اما «برنا» چنان‌که نورایی آورده از \"\n \"pərənāyu- «بالغ» نیست، بلکه از صورت منفیِ apərənāyu- «نابالغ» و پهلوی aburnāy/awarnāy است (هوبشمان، مطالعات فارسی؛ ویکی‌واژه). \"\n \"پس ریشه درست است ولی صورت مادر در نمودار نادرست است؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n [W_POR, W_BARNA],\n [{\"ref\": \"BQT:163,264\", \"status\": \"supports\",\n   \"note\": \"BQT_v1_pages.txt leaf 381-382 (printed pp. 163-164): headwords «انبار ... بمعنی لبریز و مملو و پر باشد»، «انباردن ... بمعنی انباشتن است که پر کردن و انبار کردن چیزی باشد» with Mo'in's footnotes giving the Pahlavi forms (OCR 'بهلوی ...' ambār/hambār). Leaf 484 (printed p. 264): «برنا ... جوان و نوچهٔ اول عمر و ظریف را گویند». Both headwords are where Nourai says they are.\"},\n  {\"ref\": \"FFD:31\", \"status\": \"supports\",\n   \"note\": \"FFD_pages.txt pdf p.36 = printed p.31, s.v. «انباردن، انباشتن»: «انبارد < فارسی میانه *hambārd < ایرانی باستان *ham-pār-ta ... PĀR صورت بالاندهٔ ریشهٔ PAR است، به معنی «پرکردن». از PĀR «اوباردن» هم آمده است ... «انباشت» در فارسی دری به قیاس با «کار/کاشت» به وجود آمده است.»\"}],\n [{\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 111 (p. 26) and no. 294 (p. 71)\", \"stance\": \"partial\",\n   \"note\": \"HRN.txt: '111. enbāštan \\\"anfüllen, anhäufen\\\", Praes. enbār-em, enbārden, enbār. aw. hąm + √par, hampāfrāiti \\\"er mästet\\\"; phlv. anbāstan, anbār, anbār(i)šn ...; arm. LW. ambar, hambar ...; ai. sam-ṛ- √par-' — supports anbār. '294. pur \\\"voll\\\". aw. pərəna- \\\"voll\\\"; phlv. pur; ai. pūrṇá-' — supports por, and adds that Horn rejects deriving pur from aw. pouru-. Horn does not treat barnā here.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 174 (§ on rn) and p. 125\", \"stance\": \"contradicts\",\n   \"note\": \"HUB.txt: 'burna \\\"Jüngling\\\" = zd. apərənayu-' and 'a) rn bleibt in: burna, barnā \\\"Jüngling\\\", zd. apərə[nāyu-]' — i.e. from the NEGATED Avestan form, not from pərənāyu- as the chart draws it.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. purr, purnāy, hambār\", \"stance\": \"supports\",\n   \"note\": \"PHD.txt: 'purr ... full'; 'purnāy [pwln'd = Av. pərənayu-] adult' — the Middle Persian stage of por and of the bornā family.\"},\n  {\"src\": \"ARY\", \"where\": \"ARY_pages.txt leaf 158 (cross-reference to فراوان)\", \"stance\": \"supports\",\n   \"note\": \"Aryanpur's Persian IE-roots dictionary files «پر» with Avestan PĀRENA/PERENA, Pahlavi, Kurdish, Baluchi, Afghan cognates and cross-refers to فراوان under the same PIE root.\"}])\n\n# ---------------- node 3\nnode(3, \"Avestan\", \"ava-par\", \"plausible\",\n \"Not an attested Avestan lemma: Bartholomae's AiW lists no ava+1par-. It is a reconstruction, and it is Horn's: Horn no. 132 sets up \"\n \"'ap. *ava + √par (vgl. skr. avapūrṇa- \\\"anfüllen\\\")' as the source of NP ōbāštan/ōbārdan, and Abolqasemi (FFD, s.v. اوباردن) writes \"\n \"'اوبارد < فارسی میانه ōbārd < ایرانی باستان *ava-pār-ta ... ava پیشوند فعلی است ... PAR به معنی پر کردن است'. The semantics \"\n \"('fill downwards' → 'swallow, gulp down') is the weak point, and Cheung's Etymological Dictionary of the Iranian Verb (2007) places \"\n \"MP ōbār-/NP aubārdan under a different root *baru̯ 'to chew, devour' (Skt. bharv-), noting that these forms 'may not contain *bar \"\n \"\\\"to bring, carry\\\"'. So the node reflects Horn/Abolqasemi faithfully but is not the current consensus.\",\n \"ترکیب ava-par در اوستا گواهی نشده است و در فرهنگ بارتولومه چنین مدخلی نیست؛ این صورت بازسازی‌شدهٔ هرن است. هرن (شمارهٔ ۱۳۲) \"\n \"ایرانی باستان *ava + par «پر کردن» را (با مقایسهٔ سنسکریت avapūrṇa-) سرچشمهٔ «اوباشتن/اوباردن» می‌داند و ابوالقاسمی نیز همین را \"\n \"می‌آورد: «اوبارد < فارسی میانه ōbārd < ایرانی باستان *ava-pār-ta». نقطهٔ ضعف، تحول معنایی «فروپر کردن» به «فروبردن/بلعیدن» است و \"\n \"چونگ (۲۰۰۷) این فعل‌ها را زیر ریشهٔ دیگری، *baru̯ «جویدن، بلعیدن» (سنسکریت bharv-) می‌گذارد. بنابراین نمودار با احتیاط پذیرفتنی است.\",\n [],\n [{\"ref\": \"AEF:175\", \"status\": \"supports\",\n   \"note\": \"AEF (Khaleqi-Motlaq's Persian version of Horn) is not online; checked its German original instead — HRN.txt no. 132: 'ōbāštan \\\"anfüllen; verschlingen (d. i. sich anfüllen)\\\" ... ap. *ava + √par (vergl. skr. avapūrṇa- \\\"anfüllen\\\"); phlv. avpartan bezw. ōpārtan \\\"verschlingen\\\"'. Exactly Nourai's arrow.\"},\n  {\"ref\": \"BQT:180\", \"status\": \"partial\",\n   \"note\": \"BQT_v1_pages.txt leaf 399 (printed p.180) has the headwords «اوباریدن ... ناجاویده فرو بردن را گویند» and «اوبردن»; Mo'in's footnote gives a Pahlavi form (OCR 'بهلوی ...' = ōbārtan) but Borhan/Mo'in do not reconstruct an Avestan ava-par.\"}],\n [{\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *baru̯ 'to chew, devour'\", \"stance\": \"contradicts\",\n   \"note\": \"CHEUNG.txt: 'MIDDLE PERSIAN: (+ *aua-) MMP ʾwbʾr-, BMP ʾpʾl- /ōbār-/ (caus.) \\\"to swallow\\\" ... NP auburdan/aubar- \\\"to swallow unmasticated\\\", NP aubāridan ..., NP aubāstan/aubar- \\\"to devour, swallow\\\"'; footnote: 'The Pers. and Bal. forms quoted above may not contain *bar \\\"to bring, carry\\\" ... rather suggest a different root'.\"},\n  {\"src\": \"BRT\", \"where\": \"AiW cols. 850-852 (1par- ... 5par-)\", \"stance\": \"silent\",\n   \"note\": \"Bartholomae lists five roots par- (füllen / gleich machen / verurteilen / hindurchgehen / obstare) and records no compound ava+par-; the only preverbal compound under 1par- is hąm-.\"},\n  {\"src\": \"FFD\", \"where\": \"Abolghasemi, printed p. 33 (pdf 38), s.v. اوباردن، اوباشتن\", \"stance\": \"supports\",\n   \"note\": \"FFD_pages.txt: «اوبارد < فارسی میانه ōbārd < ایرانی باستان *ava-pār-ta ... PĀR صورت بالاندهٔ ریشهٔ PAR است. PAR به معنی «پر کردن» است. انباردن هم از ریشهٔ PAR ... آمده است».\"}])\n\n# ---------------- node 4\nnode(4, \"Persian\", \"obârdan «اُباردن»; obâštan «اُباشتن»; obâsh «اوباش» (+ اوباردن، اوباشتن)\", \"disputed\",\n \"The two verbs are fine as Persian words and as descendants of MP ōbār-/ōbārdan 'to swallow' (Hübschmann §90 lists 'ōbāštan \\\"implere\\\", \"\n \"2) = ōbārdan \\\"deglutire\\\", pr. ōbāram, phl. ōpart \\\"swallowed\\\"'; the -rt- > -št- change is the regular Pazand/NP pair angārdan~angāštan, \"\n \"gumārdan~gumāštan). Their root, however, is contested: Horn/Abolqasemi = *ava-par- 'fill down', Cheung 2007 = *aua-baru̯- 'devour'. \"\n \"The third word breaks the node: اوباش 'rabble, rowdy' is not Iranian at all but the Arabic plural أوباش awbāš of وَبَش wabaš 'riff-raff' \"\n \"— Hübschmann §132 says so ('Dann ist es arabisirt oder aus dem Arabischen entlehnt ... vabaš, pl. aubāš \\\"Gesindel\\\". Auch Nöldeke hält \"\n \"aubāš für echt arabisch') and Mo'in says so in the very footnote on the page Nourai cites (BQT p.180): «عربی، جمع وبش، مقلوب بوش»; \"\n \"Wiktionary: 'Borrowed from Arabic أَوْبَاش (ʔawbāš), plural of وَبَش (wabaš)'. The resemblance to اوباردن is folk etymology.\",\n \"«اوباردن/اوباشتن» در فارسی نو از فارسی میانهٔ ōbārdan «فروبردن، بلعیدن» است و جفت -rt-/-št- همان دگرگونی آشنای «انگاردن/انگاشتن» و \"\n \"«گماردن/گماشتن» است (هوبشمان، بند ۹۰). دربارهٔ ریشهٔ آن دو دیدگاه هست: هرن و ابوالقاسمی *ava-par «فروپر کردن» و چونگ *aua-baru̯ «بلعیدن». \"\n \"اما «اوباش» ایرانی نیست: عربی است، جمعِ «وَبَش»، و همین را معین در حاشیهٔ همان صفحهٔ برهان قاطع که نورایی به آن ارجاع داده آورده است: \"\n \"«عربی، جمع وبش، مقلوب بوش. محیط‌المحیط». هوبشمان (بند ۱۳۲) نیز به نقل از نولدکه آن را عربی اصیل می‌داند. پس پژوهش امروزی این پیوند را \"\n \"رد می‌کند و آن را ریشه‌شناسی عامیانه می‌شمارد.\",\n [W_OBASH],\n [{\"ref\": \"BQT:180\", \"status\": \"contradicts\",\n   \"note\": \"BQT_v1_pages.txt leaf 399 = printed p.180, Mo'in's footnote to «اوباش»: «عربی، جمع وبش، مقلوب بوش. «محیط‌المحیط»» — the cited page says اوباش is Arabic, the opposite of Nourai's arrow. The same page's «اوباریدن/اوبردن» entries do support the verbs.\"},\n  {\"ref\": \"AEF:175\", \"status\": \"partial\",\n   \"note\": \"Checked through Horn (HRN.txt no. 132), of which AEF is the Persian version: Horn derives ōbāštan/ōbārdan from *ava+par but lists 'ōbāš \\\"Gesindel\\\"' merely alongside, without argument; Hübschmann, revising exactly this number (PSt. §132), removes اوباش from the entry.\"},\n  {\"ref\": \"FFD:31\", \"status\": \"supports\",\n   \"note\": \"FFD_pages.txt printed p.31 (s.v. انباردن) and p.33 (s.v. اوباردن): «از PĀR «اوباردن» هم آمده است» — Abolqasemi puts اوباردن under the 'fill' root, as Nourai does (verbs only).\"}],\n [{\"src\": \"HUB\", \"where\": \"Persische Studien §132 (pp. 19-20) and §90 (p. 174)\", \"stance\": \"contradicts\",\n   \"note\": \"HUB.txt p.19-20: 'Np. ōbāš \\\"liederlicher Kerl, Gesindel\\\" liegt als LW. im Afgh. in der Form aubōs vor ... Dann ist es arabisirt oder aus dem Arabischen entlehnt. Vgl. bei Freitag: vabaš, pl. aubāš \\\"Gesindel\\\". — Auch Nöldeke hält aubāš für echt arabisch.' For the verbs §90 is neutral-supportive: 'ōbāštan \\\"implere\\\", 2) = ōbārdan \\\"deglutire\\\", pr. ōbāram, phl. ōpart \\\"swallowed\\\" ... = paz. ōpard'.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *baru̯\", \"stance\": \"contradicts\",\n   \"note\": \"Cheung assigns MMP ʾwbʾr- /ōbār-/, NP aubārdan, aubāštan to *aua-baru̯ 'chew, devour' (Skt. bharv-), not to 'fill'.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, no entry\", \"stance\": \"silent\",\n   \"note\": \"PHD.txt has no ōbārdan headword (grep 'ōbār', 'obard': nothing); MacKenzie's glossary simply does not carry the verb.\"}])\n\n# ---------------- node 5\nnode(5, \"Avestan\", \"frâ 1, fra 1; frâ-yah; fra-ěšta\", \"plausible\",\n \"frāyah- and fraēšta- are certainly here: they are the suppletive comparative and superlative of pouru- 'much', from *pleh₁-yos- and \"\n \"*pleh₁-isto-, and Bartholomae glosses frāyah- 'der mehrere, plus; mehr als genug, zu viel; n. als Subst. Überschuss, Überfluss' \"\n \"(AiW col. 1017) with fraēšta- 'der meiste'. Pokorny (800) and Walde-Pokorny (II 64 f.) list exactly 'av. frayah-, sup. fraēšta-' \"\n \"beside Skt. práyas-. What is not attested is a free Avestan stem 'frā 1 / fra 1 = plenty': Avestan frā/fra- is the preverb 'forth, \"\n \"forward' (< *pro-, a different root), and the frā- of frāyah- is only the phonetic outcome of *plē- before -yah-. Nourai's box thus \"\n \"back-forms a lemma that exists only in Middle Persian (frāy 'much, more'). The two comparatives are confirmed; the head-form is not.\",\n \"دو صورت frāyah- «بیشتر» و fraēšta- «بیشترین» بی‌گمان از همین ریشه‌اند: آن‌ها صورت‌های برتر و برترینِ مکمّلِ pouru- «بسیار» و بازماندهٔ \"\n \"*pleh₁-yos- و *pleh₁-isto- هستند؛ بارتولومه (ستون ۱۰۱۷) frāyah- را «بیشتر، افزون، فزونی» و fraēšta- را «بیشترین» معنی کرده و \"\n \"پوکورنی (ص ۸۰۰) و والده‌ـ‌پوکورنی نیز همین‌ها را آورده‌اند. اما ستاکِ آزادِ «frā ۱/fra ۱ به معنی فراوانی» در اوستا گواهی ندارد: \"\n \"fra-/frā- در اوستا پیشوندِ «پیش، فرا» (از *pro-) است و frā- در frāyah- تنها برآیند آوایی *plē- پیش از پسوند است. این سرواژه در حقیقت \"\n \"از روی فارسی میانهٔ frāy «بسیار» بازساخته شده است. پس بخشی از گره درست و بخشی با احتیاط پذیرفتنی است.\",\n [W_PIE],\n [{\"ref\": \"POK:800\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt p.800: 'Kompar. Old Indic prayas- ..., Avestan frayah-, Superl. fraesta- \\\"the meiste\\\"' — the comparative/superlative pair, but Pokorny sets up no Avestan 'frā = plenty'.\"}],\n [{\"src\": \"BRT\", \"where\": \"AiW col. 1017 s.v. frāyah-; col. 1018 fraēšta-\", \"stance\": \"partial\",\n   \"note\": \"BRT.txt: \\\"j. frāyah- Adj. (fem. °yehī-) 1) 'der mehrere, plus' ... 2) 'mehr als genug, zu viel' ... n. als Subst. 'Überschuss, Überfluss' ... 2) ohne kompar. Bedeutung 'sehr viel, sehr zahlreich'\\\". Bartholomae has no lemma frā- 'plenty'; his frā/fra is the preverb.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 64 f.\", \"stance\": \"supports\",\n   \"note\": WLD_NOTE + \" The comparative series 'Komp. plē-ios, Sup. plē-is-to-' is set up exactly for av. frayah-/fraēšta-.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pelə-1, III.4-5\", \"stance\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt: 'Suffixed (comparative) form *plē-i(s)on- in Greek pleōn ... 5. Suffixed (superlative) form *plē-isto- in Greek pleistos, most' — the same two formations that give Av. frāyah-/fraēšta-.\"}])\n\n# ---------------- node 6\nnode(6, \"Pahlavi\", \"frây, frěh; frěh-est\", \"confirmed\",\n \"MacKenzie's Concise Pahlavi Dictionary has all three: 'frāy [pl'd] more, much', 'freh [plyh | N firih] more, much, = frāy' and \"\n \"'frahist [plh(y)st' | (M pryst)] most (superlative of freh)'. frāy continues Av. frāyah- (loss of the final -h and of intervocalic \"\n \"-y- contraction), frēh is its by-form with the regular MP raising ā > ē before the lost *-ah, and frēhist/frahist is the MP \"\n \"superlative in -ist, the direct counterpart of Av. fraēšta-. Nourai's citation SNS:126 is right on target: Tavoosi's glossary of \"\n \"Shāyast nē Shāyast indexes 'fray 126/6', 'frayah- 126/7', 'frayist 127/7', 'freh/fray 129/5'.\",\n \"در فارسی میانه هر سه صورت گواهی شده‌اند: مکنزی frāy «بیشتر، بسیار»، frēh «بیشتر، بسیار، = frāy» و frahist/frēhist «بیشترین \"\n \"(صیغهٔ برترینِ frēh)» را ثبت کرده است. frāy دنبالهٔ اوستایی frāyah- است (با افتادن -h پایانی)، frēh گونهٔ آن با کشش/ارتقای واکه، و \"\n \"frēhist صورت برترین با پسوند -ist که برابر مستقیم اوستایی fraēšta- است. ارجاع نورایی به «واژه‌نامهٔ شایست نشایست» ص ۱۲۶ درست است: \"\n \"نمایهٔ آن کتاب fray و frayah- را در ص ۱۲۶، frayist را در ص ۱۲۷ و freh/fray را در ص ۱۲۹ نشان می‌دهد. ادعای نورایی درست است.\",\n [],\n [{\"ref\": \"SNS:126\", \"status\": \"supports\",\n   \"note\": \"SNS.txt index: 'fray 126/6', 'frayah- 126/7', 'frayist 127/7', 'freh/fray 129/5'; the glossary body has the entry 'frēh/fray'. Page 126 of Tavoosi's Shāyast nē Shāyast glossary is indeed where fray/frayah- stand.\"},\n  {\"ref\": \"BQT:1479\", \"status\": \"supports\",\n   \"note\": \"BQT_v3_pages.txt pdf p.273 = printed p.1479, Mo'in's footnote to «فرهست»: «پهلوی frēhest (صیغهٔ تفضیلی از «فره» بمعنی [بیش])».\"},\n  {\"ref\": \"MON:2538\", \"status\": \"not_checked\",\n   \"note\": \"Mo'in's Farhang-e Fārsi vol. 3 p. 2538 not accessible as page-numbered text; the same author's footnote in BQT p.1479 was used instead.\"}],\n [{\"src\": \"PHD\", \"where\": \"MacKenzie pp. 33-34 s.vv. frāy, freh, frahist\", \"stance\": \"supports\",\n   \"note\": \"PHD.txt: 'freh [plyh | N firih] more, much, = fray. ~-būd(īh) [-bwt', bwtyh] excess'; 'frahist [plh(y)st' | (M pryst)] most (superlative of freh)'; English index: 'more fray, freh, wēš', 'much abēr, frāy, freh, was, wasyār'.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n   \"note\": \"NYB_vol2_glossary.txt: grep for 'frāy', 'freh', 'frawān' returns no usable hit (the OCR of the glossary's Latin transliterations is patchy here); no contrary evidence.\"}])\n\n# ---------------- node 7\nnode(7, \"Persian\", \"fereh, fareh «فِره ، فَره»; farh-ast «فَرَهَست»\", \"confirmed\",\n \"NP فره fer(a)h 'much, abundant; good' continues MP frēh directly (MP frēh > NP fereh, with the prothetic-free fa-/fe- vowel of the \"\n \"Dari reflex), and فرهست farhast/frahast is MP frēhist, the superlative. Borhan-e Qāte' (p. 1479) glosses فرهست as 'جادو و جادویی و \"\n \"ساحری' ('magic, sorcery'), which is exactly the second half of Nourai's gloss 'too much, magic' — and Mo'in's footnote on that very \"\n \"page corrects it: the Pahlavi is frēhest, comparative of فره 'more', and Asadi's Loghat-e Fors already glossed فرایت/فراسته as \"\n \"'فراوان‌تر، بیشتر' with no connection to sorcery; Borhan's 'magic' comes from misreading Abū-Naṣr Marghzī's line. That line is the \"\n \"quote in the JSON: «اوی تنبل کند هست را نیست / فرهستش کند نیست را هست» ('his sorcery makes what is, not-be; his abundance makes what \"\n \"is-not, be') — printed in Mo'in's note in the form «تنبل اوی هست را نیست کند ... هست را نیست کند فرهستش». Root and route confirmed; \"\n \"the 'magic' sense is a lexicographers' error the chart repeats.\",\n \"«فِره/فَره» در فارسی نو دنبالهٔ مستقیم فارسی میانهٔ frēh «بیشتر، بسیار» است و «فرهست» همان frēhist، صیغهٔ برترینِ آن. برهان قاطع (ص ۱۴۷۹) \"\n \"«فرهست» را «جادو و جادویی و ساحری» معنی کرده است — همان نیمهٔ دوم معنیِ نورایی — ولی معین در حاشیهٔ همان صفحه آن را تصحیح می‌کند: \"\n \"«پهلوی frēhest، صیغهٔ تفضیلی از فره»، و می‌افزاید که اسدی در لغت فرس «فرایت/فراسته» را «فراوان‌تر و بیشتر» دانسته و «ربطی به جادویی \"\n \"ندارد»؛ معنی «جادو» از بدخوانیِ بیت ابونصر مرغزی پدید آمده است، همان بیتی که در داده‌ها نقل شده است. پس ریشه و مسیر درست است و تنها \"\n \"معنیِ «جادو» خطای فرهنگ‌نویسان است که نمودار آن را تکرار کرده.\",\n [],\n [{\"ref\": \"BQT:1479\", \"status\": \"supports\",\n   \"note\": \"BQT_v3_pages.txt pdf page 273 (printed 1479): «فرهست ... بر وزن بدست، بمعنی جادو و جادویی و ساحری باشد» + footnote: «پهلوی frēhest (صیغهٔ تفضیلی از «فره» بمعنی بیش)» and the long note: «اسدی در لغت فرس نوشته: پازند «فرایت» بمعنی فراوانتر و بیشتر می‌باشد و ربطی به جادوئی ندارد ... مع‌هذا اسدی این شاهد را از ابونصر مرغزی برای معنی جادویی آورده: ... هست را نیست کند فرهستش».\"},\n  {\"ref\": \"MON:2537,2538\", \"status\": \"not_checked\",\n   \"note\": \"Mo'in Farhang-e Fārsi vol. 3 pp. 2537-2538 (the ف section) is not available as page-indexed text locally; Mo'in's own footnote in BQT p.1479 covers the identical claim.\"}],\n [{\"src\": \"BQT\", \"where\": \"Mo'in's footnote, printed p. 1479\", \"stance\": \"supports\", \"note\": \"see ref_check — Mo'in explicitly equates فرهست with Pahlavi frēhest, superlative of فره.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. freh\", \"stance\": \"supports\",\n   \"note\": \"PHD.txt: 'freh [plyh | N firih] more, much, = fray' — MacKenzie himself gives the New Persian continuant as firih (فره).\"},\n  {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors, s.vv. فره / فراسته (quoted by Mo'in)\", \"stance\": \"supports\",\n   \"note\": \"Cited in Mo'in's footnote: Asadi glosses «فرایت»/«فراسته» as «فراوان‌تر، بیشتر» — the abundance sense, not 'magic'.\"}])\n\n# ---------------- node 8\nnode(8, \"Avestan\", \"paoiry-aěnini\", \"plausible\",\n \"The Avestan word is real: paoiryaēinī- f., plural, the name of a constellation, 'Plejaden' (Tištar Yašt 12/17). The dispute is over \"\n \"which root it belongs to. Bartholomae files it as the feminine of °yaēna-, 'Ableitung aus paoirya-' ('first'), i.e. to OP paruva-/\"\n \"paruviya- 'former, first' < *pr̥H-wo- — a DIFFERENT root (PIE *per-) — and refers to Hübschmann PSt. 40, where Geldner's reading \"\n \"paoiryaēini- = OP *paruviyaini- = np. parvīn is discussed. Pokorny 800, on the other hand, puts it squarely here: 'here Iran. *pelu-, \"\n \"*polu- in Plejadennamen npers. parv, Avestan paoiryaēinī (*paruḭaini-), ablaut. Gk. Pleiádes ... originally \\\"Sternhaufen\\\"' — a \"\n \"'star-heap', matching Greek Πλειάδες from the same 'many' root. Nourai follows Pokorny (his cited page), which is defensible; \"\n \"Bartholomae/Hübschmann prefer 'the first ones'. Both readings are current, hence plausible rather than confirmed.\",\n \"واژهٔ اوستایی واقعی است: paoiryaēinī- مؤنث و جمع، نام صورت فلکی «ثریا/پروین» (تیریشت، بند ۱۲/۱۷). اختلاف بر سر ریشهٔ آن است. \"\n \"بارتولومه آن را مؤنثِ °yaēna- و مشتق از paoirya- «نخستین» می‌داند (هم‌ریشه با پارسی باستان paruva-/paruviya- «پیشین» از *pr̥H-wo-، \"\n \"یعنی ریشه‌ای دیگر) و به هوبشمان، مطالعات فارسی ص ۴۰ ارجاع می‌دهد. در برابر، پوکورنی (ص ۸۰۰) آن را صریحاً زیر همین ریشه می‌آورد: \"\n \"«ایرانی *pelu-، *polu- در نام پروین: فارسی نو parv، اوستایی paoiryaēinī (*paruḭaini-)، هم‌پایهٔ یونانی Pleiádes، در اصل «انبوهِ \"\n \"ستارگان»». نورایی از پوکورنی پیروی کرده که پذیرفتنی است، ولی دیدگاه «نخستین‌ها» نیز همچنان رایج است؛ پس با احتیاط پذیرفتنی است.\",\n [W_PARVIN],\n [{\"ref\": \"POK:800\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt p.800: 'here Iran. *pelu-, *polu- in Plejadennamen npers. parv, Avestan paoiryaeini (*paruḭaini-), ablaut. gr. Pleiades, hom. Plēiades (*pleu-ii-), originally \\\"Sternhaufen\\\"'. Nourai's arrow is Pokorny's.\"}],\n [{\"src\": \"BRT\", \"where\": \"AiW col. 885 s.v. paoiryaēinī-\", \"stance\": \"contradicts\",\n   \"note\": \"BRT.txt: \\\"j. paoiryaēinī- f., Plur. Name eines Sternbilds 'Plejaden' ... Fem. zu °yaēna- Adj., Ableit. aus paoirya-. — np. parvīn 'Plejaden'; s. dazu Hbm. PSt. 40.\\\" — derived from paoirya- 'first', not from pouru- 'many'.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien § 308, p. 40\", \"stance\": \"contradicts\",\n   \"note\": \"HUB.txt p.40: 'Aber Geldner liest paoiryaēinyas- von paoiryaēini- = ap. *paruviyaini- = np. parvīn?' — i.e. built on *paruviya- 'first/former' (Kent's paruva-, pIE *pr̥uos), a separate root from paru- 'many'.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, p. 196\", \"stance\": \"partial\",\n   \"note\": \"KNT.txt keeps the two apart on one page: 'paru- adj. \\\"much, many\\\": Av. pouru-, Skt. purú-, Gk. polús, Gt. filu, pIE *pl̥u-' vs. 'paruva- adj. \\\"being before in time or place\\\": Av. paurva-, Skt. pūrva-, pIE *pr̥uos'. Which of the two underlies paoiryaēinī- is precisely the open question.\"}])\n\n# ---------------- node 9\nnode(9, \"Persian\", \"parvin «پروین» (+ پَرو، پَرَن)\", \"confirmed\",\n \"Av. paoiryaēinī- (with the Avestan diphthong ao rendering *aru) > *parwēn > MP parwēn > NP پروین parvīn, the Pleiades; the by-forms \"\n \"پَرو parv and پَرَن paran are the shorter stem, and Borhan-e Qāte' defines پرو as 'بمعنی پروین است و آن چند ستاره‌ای است در کوهان ثور' \"\n \"('the same as parvīn, several stars in the hump of Taurus'), with the Ferdowsi line the JSON quotes. Mo'in's footnote to پروین \"\n \"(printed p. 395) gives the Avestan plural attested in the Tištar Yašt § 17, and the cognate series Afghan pərune, Baluchi parwēn/\"\n \"parwār, Sogdian parwī, Khwarazmian parwī, Arabic ثریا, French Pléiade. The Avestan→New Persian route itself is not in dispute (only \"\n \"the deeper root is, see node 8), so the node is confirmed.\",\n \"«پروین» از اوستایی paoiryaēinī- می‌آید: *parwaini- > فارسی میانهٔ parwēn > فارسی نو «پروین»، نام خوشهٔ ثریا؛ گونه‌های کوتاه‌ترِ «پَرو» و \"\n \"«پَرَن» نیز همین‌اند و برهان قاطع «پرو» را «بمعنی پروین است و آن چند ستاره‌ای است در کوهان ثور» معنی کرده و همان بیت فردوسی را که در \"\n \"داده‌ها آمده شاهد آورده است. معین در حاشیهٔ «پروین» (ص ۳۹۵) صورت جمع اوستایی را در تیریشت بند ۱۷ و هم‌ریشه‌های افغانی pərune، بلوچی \"\n \"parwēn، سغدی و خوارزمی parwī، عربی «ثریا» و فرانسهٔ Pléiade را آورده است. مسیر اوستایی ← فارسی نو مورد اختلاف نیست (اختلاف بر سر \"\n \"ریشهٔ کهن‌تر است، بنگرید به گرهٔ ۸)؛ ادعای نورایی درست است.\",\n [W_PARVIN],\n [{\"ref\": \"BQT:395\", \"status\": \"supports\",\n   \"note\": \"BQT_v1_pages.txt leaf 619 (printed p.395): «پروین ... چند ستارهٔ کوچک باشد یکجا جمع شده در کوهان ثور. و آنرا بعربی ثریا خوانند», with Mo'in's footnote citing the Avestan plural in Tīr Yašt §17, «افغانی pərune، بلوچی parwēn/parwār ... در سغدی: پروی، خوارزمی: پروی، عربی: ثریا، فرانسه Pléiade». Leaf 614 (p.~390) has «پَرو ... بمعنی پروین است» with a Pahlavi form in the footnote.\"},\n  {\"ref\": \"AEF:372\", \"status\": \"not_checked\",\n   \"note\": \"AEF (Khaleqi-Motlaq's Persian Horn) not online; the corresponding German discussion is Hübschmann PSt. §308 p.40 (consulted below), since Horn's own Grundriss has no parvīn number reachable by grep.\"}],\n [{\"src\": \"BRT\", \"where\": \"AiW col. 885\", \"stance\": \"supports\",\n   \"note\": \"BRT.txt: 'paoiryaēinī- ... Plejaden ... — np. parvīn \\\"Plejaden\\\"' — Bartholomae himself makes the Avestan → New Persian identification.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien § 308 p. 40 and index ('parvīn \\\"Plejaden\\\" s. oben')\", \"stance\": \"supports\",\n   \"note\": \"HUB.txt: 'paoiryaēini- = ap. *paruviyaini- = np. parvīn?' — same equation, different deeper root.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in's footnote in BQT p.395 (same author)\", \"stance\": \"supports\",\n   \"note\": \"The footnote is Mo'in's own etymological note in his edition of Borhan; it lists the Iranian cognates and the Avestan source.\"}])\n\n# ---------------- node 10\nnode(10, \"Avestan\", \"pouru, paourus\", \"confirmed\",\n \"Av. pouru- (nom. sg. m. paouruš) 'much, many' < Proto-Iranian *paru- < PIE *pelh₁u- (zero grade *pl̥h₁u-, with the Avestan epenthetic \"\n \"-ou- of *paru- noted by Kent § 121: 'pouru for *paru'). It is the exact cognate of Skt. purú-, Gk. polús and Goth. filu, as Pokorny \"\n \"(800), Walde-Pokorny (II 64) and Mann (IEC s.v. poluos) all state. The u-stem forms hundreds of Avestan compounds (pouru-sata-, \"\n \"pouru-hazaŋra-, pouru-daēva-). Nourai's node is standard.\",\n \"اوستایی pouru- (نهادی مفرد مذکر paouruš) «بسیار، فراوان» از ایرانی آغازین *paru- و آن از هندواروپایی *pelh₁u- است؛ گونهٔ -ou- برآیند \"\n \"«اِپنتز» اوستایی در *paru- است (کنت، بند ۱۲۱: «pouru به جای *paru»). این واژه هم‌ریشهٔ دقیقِ سنسکریت purú-، یونانی polús و گوتی filu \"\n \"است، چنان‌که پوکورنی (ص ۸۰۰)، والده‌ـ‌پوکورنی (ج ۲ ص ۶۴) و مان همگی آورده‌اند و در ده‌ها ترکیب اوستایی مانند pouru-sata- و \"\n \"pouru-hazaŋra- دیده می‌شود. ادعای نورایی درست است.\",\n [W_PIE],\n [{\"ref\": \"POK:800\", \"status\": \"supports\", \"note\": \"POK_full.txt p.800: 'Old Indic puru-, Avestan pouru-, ap. paru \\\"much, a lot of\\\" (= gr. polús ...)'.\"},\n  {\"ref\": \"KNT:196\", \"status\": \"supports\", \"note\": \"KNT.txt p.196: 'paru- adj. \\\"much, many\\\": Av. pouru-, Skt. purú-, Gk. polús, Gt. filu, pIE *pl̥u- (§63.I, §107)'. Kent is cited for the Old Persian side but states the Avestan equation on the same page.\"},\n  {\"ref\": \"IEC:974\", \"status\": \"supports\", \"note\": \"IEC.txt, entry 'poluos (1) (polus, polu) \\\"big, full; much, many, abundant; spate\\\"' on p.975 (entry running from p.974): 'Av. paourus, pourus, parus, adj. \\\"abundant; full, big\\\"'.\"}],\n [{\"src\": \"BRT\", \"where\": \"AiW cols. 895 ff. (pouru- and its compounds)\", \"stance\": \"supports\",\n   \"note\": \"BRT.txt has a long series of pouru- compounds ('pouru-hazaŋra- Adj. \\\"viele Tausende betragend\\\"', 'pouru-darətar-', 'pouru-x\\\"āθra-'), i.e. the stem is amply attested with the sense 'many'.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 64\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt: 'Ai. purú-, av. pouru-, ap. paru \\\"viel\\\" (= gr. polús ...)'.\"}])\n\n# ---------------- node 11\nnode(11, \"Persian\", \"farâvân «فراوان»\", \"plausible\",\n \"Mann's Indo-European Comparative Dictionary does list 'Per. cf. farawan, adj. \\\"abundant\\\"' in the entry poluos (1) beside Av. pourus \"\n \"and OP parav, so Nourai's cited reference really does draw the arrow he draws. But the Iranian-internal analysis is contested: NP \"\n \"فراوان is normally segmented farā- + -vān, the first element being the preverb/adverb فرا farā 'forth, beyond' (< OIr. *frā-, PIE \"\n \"*pro-), the second the productive adjectival suffix -vān (Dehkhoda, quoted by Abadis, compares Kurdish formations in -van that \"\n \"intensify the base). If so the word does not continue pouru- at all, and belongs to *per- 'forward' rather than *pelh₁u- 'much' — \"\n \"unless the base is rather MP frāy 'much' (< Av. frāyah-, node 6), which is the same root as the chart's but a different branch of it. \"\n \"Wiktionary leaves the etymology explicitly blank. Direct descent from pouru- would require *paru- > farā-, which is not a Persian \"\n \"sound law. Accepted with reservation.\",\n \"مان در «فرهنگ تطبیقی هندواروپایی» زیر مدخل poluos در کنار اوستایی pourus و پارسی باستان parav، «فارسی farawān» را هم آورده است؛ پس \"\n \"مأخذی که نورایی به آن ارجاع داده واقعاً همین پیوند را می‌کشد. اما تحلیل ایرانی‌شناسانه‌اش محل بحث است: «فراوان» را معمولاً به «فرا» \"\n \"(پیشوند/قید «پیش، فراتر»، از ایرانی باستان *frā- و هندواروپایی *pro-) به‌اضافهٔ پسوند صفت‌سازِ «-وان» تجزیه می‌کنند (دهخدا، با مقایسهٔ \"\n \"ساخت‌های کردی با «-وان»). در این صورت واژه اصلاً دنبالهٔ pouru- نیست، مگر آنکه پایهٔ آن فارسی میانهٔ frāy «بسیار» (< اوستایی frāyah-) \"\n \"باشد که شاخهٔ دیگری از همین ریشه است. ویکی‌واژه ریشه‌شناسی آن را ناتمام گذاشته است. گذارِ مستقیم *paru- > farā- قانون آوایی فارسی \"\n \"نیست؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n [W_FARAV, A_FARAV],\n [{\"ref\": \"IEC:956,974\", \"status\": \"supports\",\n   \"note\": \"IEC.txt, entry poluos (1) (running p.974-975): 'Av. paourus, pourus, parus ...; OPer. cf. parav, prn. \\\"many\\\"; Per. cf. farawan, adj. \\\"abundant\\\"' — Mann files farāvān under the *poluos entry exactly as Nourai does.\"},\n  {\"ref\": \"MON:2508\", \"status\": \"partial\",\n   \"note\": \"Mo'in's entry, read via abadis.ir: «(فَ) (ص.) بسیار، زیاد» — the meaning is confirmed but Mo'in supplies no origin tag, so the page does not support the Avestan arrow.\"}],\n [{\"src\": \"ARY\", \"where\": \"ARY_pages.txt pdf p. 389 s.v. فراوان\", \"stance\": \"supports\",\n   \"note\": \"Aryanpur's entry فراوان lists as cognates Avestan FRĀ/FRAYAH/POURU/PAOURUŠ, Pahlavi FRĀY, FRĒH and Old Persian PARU alongside Gothic/Old English/Lithuanian forms — i.e. the same grouping as the chart (Aryanpur is a modern popular cross-check, not a primary authority).\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss — no entry\", \"stance\": \"silent\",\n   \"note\": \"HRN.txt: grep for 'frawan', 'ferāwān', 'fravan' returns nothing; Horn does not treat فراوان.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie — no entry\", \"stance\": \"silent\",\n   \"note\": \"PHD.txt has no *frawān headword (grep 'frawān|frawan|frāwān': nothing), so no Middle Persian ancestor is documented in the standard MP dictionary; only frāy/freh are.\"}])\n\n# ---------------- node 12\nnode(12, \"Old Persian\", \"paru, parav; paru-zana\", \"confirmed\",\n \"Kent's lexicon, on exactly the cited page 196, has 'paru- adj. \\\"much, many\\\": Av. pouru-, Skt. purú-, Gk. polús, Gt. filu, pIE *pl̥u-' \"\n \"with the attested nom.-acc. n. sg. paruv (DB 4.49, DSf 56) and the gen. pl. parūnām; and 'paruzana- adj. \\\"having many men, or many \"\n \"kinds of men\\\": paru- \\\"many\\\" + zana- \\\"man\\\"', attested as paruzanānām / paruvzanānām in the Achaemenid titulature \"\n \"(xšāyaθiya dahyūnām paruzanānām, 'king of lands containing many kinds of men', Xerxes' and Darius' inscriptions). Nourai's two \"\n \"spellings paru/parav are Kent's paru-/paruv. The OP form is the un-epenthesised *paru- beside Avestan pouru-.\",\n \"کنت در همان صفحهٔ ۱۹۶ که نورایی به آن ارجاع داده آورده است: «paru- صفت «بسیار، فراوان»: اوستایی pouru-، سنسکریت purú-، یونانی polús، \"\n \"گوتی filu، هندواروپایی *pl̥u-»، با صورت گواهی‌شدهٔ paruv (کتیبهٔ بیستون ۴:۴۹ و DSf ۵۶) و جمع اضافیِ parūnām؛ و نیز «paruzana- صفت «دارای \"\n \"مردمان بسیار یا گونه‌گون»: paru- «بسیار» + zana- «مرد»» که در لقب شاهانهٔ هخامنشی «xšāyaθiya dahyūnām paruzanānām» (شاهِ سرزمین‌های \"\n \"پرگونه‌مردم) آمده است. دو املای نورایی (paru، parav) همان paru-/paruv کنت است. ادعای نورایی درست است.\",\n [],\n [{\"ref\": \"KNT:196\", \"status\": \"supports\",\n   \"note\": \"KNT.txt, running head '196 OLD PERSIAN': 'paru- adj. \\\"much, many\\\": Av. pouru-, Skt. purú-, Gk. polús, Gt. filu, pIE *pl̥u- (§63.I, §107). See also paruzana-. paruv nsm. DB 4.49; DSf 56 bis. parūnām gpm. ...'; and 'paruzana- adj. \\\"having many men, or many kinds of men\\\" ... paru- \\\"many\\\" + zana- \\\"man\\\" ... paruzanānām gpf. DE 15f; XE 15f; A¹Pa 12'.\"},\n  {\"ref\": \"POK:800\", \"status\": \"supports\", \"note\": \"POK_full.txt p.800: '... ap. paru \\\"much, a lot of\\\"'.\"}],\n [{\"src\": \"IEC\", \"where\": \"Mann p. 975 s.v. poluos (1)\", \"stance\": \"supports\", \"note\": \"IEC.txt: 'OPer. cf. parav, prn. \\\"many\\\"' — the source of Nourai's second spelling parav.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 64\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt: 'Ai. purú-, av. pouru-, ap. paru \\\"viel\\\"'.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent § 121 (epenthesis), p. 39\", \"stance\": \"supports\",\n   \"note\": \"KNT.txt: 'Epenthesis ... is frequent in Avestan, as in ... pouru for *paru, OP paruv' — the OP form is the older one.\"}])\n\n# ---------------- node 13\nnode(13, \"Germanic\", \"ful-naz\", \"confirmed\",\n \"Proto-Germanic *fulnaz > *fullaz 'full', from the PIE verbal adjective *pl̥h₁-nó- (the same formation as Skt. pūrṇá-, Av. pərəna-, \"\n \"Lith. pilnas, OCS plъnъ, Latin plēnus with a different grade). Watkins writes the reconstruction exactly as Nourai does: 'Suffixed \"\n \"zero-grade form *pl̥-no-. 1. Germanic *fulnaz, *fullaz, full'. Klein adds the descendants Goth. fulls, ON fullr, OHG fol. One small \"\n \"slip: Nourai glosses ful-naz 'to fill', but *fulnaz is the adjective 'full'; the verb is the derived *fulljaną (see node 14).\",\n \"ژرمنی آغازین *fulnaz > *fullaz «پر»، از صفت فعلیِ هندواروپایی *pl̥h₁-nó- — همان ساختی که سنسکریت pūrṇá-، اوستایی pərəna-، لیتوانیایی \"\n \"pilnas و اسلاوی کهن plъnъ دارند. واتکینز دقیقاً به همین شکل بازسازی کرده است: «صورت درجهٔ صفرِ پسونددار *pl̥-no-: ژرمنی *fulnaz, \"\n \"*fullaz». کلاین نیز گوتی fulls، نورسی کهن fullr و آلمانی علیای کهن fol را می‌آورد. تنها لغزش کوچک: نورایی معنی ful-naz را «پر کردن» \"\n \"نوشته، حال آنکه *fulnaz صفت «پر» است و فعل، مشتقِ *fulljaną است. ادعای نورایی در اصل درست است.\",\n [E_FULL],\n [{\"ref\": \"POK\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt p.799: 'Gothic fulls, Old Icelandic fullr, Old English Old Saxon full, Old High German fol (-ll-) \\\"full\\\" (= Old Indic pūrṇa- etc.) = Lithuanian pilnas, Old Bulgarian plъnъ'. Nourai gives no page for this node; the claim is on the lemma's own pages.\"}],\n [{\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pelə-1, I.1-2\", \"stance\": \"supports\", \"note\": AHD_NOTE},\n  {\"src\": \"KLN\", \"where\": \"s.v. 'full, adj.'\", \"stance\": \"supports\", \"note\": KLN_FULL},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 63 f.\", \"stance\": \"supports\",\n   \"note\": \"WLD_Bd2_pages.txt: 'Gotisch fulls, ags. as. full, ahd. fol (-ll- ...) \\\"voll\\\": ai. pūrṇá- usw.; = lit. pilnas, abg. plъnъ'.\"}])\n\n# ---------------- node 14\nnode(14, \"English\", \"full, to fill\", \"confirmed\",\n \"OE full 'containing all that can be received' (< PGmc *fullaz) > ME ful > NE full; the verb is OE fyllan (< PGmc *fulljaną, a \"\n \"ja-denominative of *fullaz, with i-umlaut u > y) > ME fillen > NE fill. Watkins lists both under pelə-1 ('Old English full: FULL; \"\n \"... Old English fyllan, to fill: FILL'), as does Etymonline ('full ... from Proto-Germanic *fullaz ... from PIE root *pele- (1) \"\n \"\\\"to fill\\\"'; 'fill ... Old English fyllu \\\"fullness\\\" ... Proto-Germanic *full-ino-'). Nourai's AHD citation is the standard \"\n \"modern authority for this arrow.\",\n \"انگلیسی کهن full «پر» (از ژرمنی *fullaz) > انگلیسی میانه ful > انگلیسی نو full؛ و فعل آن انگلیسی کهن fyllan (از *fulljaną، فعلِ \"\n \"برساخته از همان صفت، با اماله/دگرگونی واکهٔ u به y) > fillen > fill. واتکینز هر دو را زیر pelə-1 آورده است و اتیمانلاین نیز همین \"\n \"زنجیره را تأیید می‌کند. ارجاع نورایی به AHD در اینجا خودِ مرجعِ معیار امروزی است؛ ادعای او درست است.\",\n [E_FULL],\n [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_NOTE + \" Nourai's 'AHD' without a page is the Indo-European appendix entry itself.\"}],\n [{\"src\": \"KLN\", \"where\": \"s.v. 'full, adj.' and 'fill'\", \"stance\": \"supports\", \"note\": KLN_FULL},\n  {\"src\": \"SKT\", \"where\": \"Skeat, s.v. full / fill\", \"stance\": \"supports\",\n   \"note\": \"SKT.txt s.v. FULL derives it from AS. full, cognate with Goth. fulls, Lat. plenus, Skt. pūrṇa, and FILL from AS. fyllan, a derivative of full — the same two-step chain.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, index: 'FULL¹ pelə-1', 'FILL pelə-1'\", \"stance\": \"supports\", \"note\": AHD_NOTE}])\n\n# ---------------- node 15\nnode(15, \"Latin\", \"pla-no; pl-us\", \"confirmed\",\n \"Nourai's 'pla-no' is Watkins' notation verbatim: 'Latin root *plāno-, replaced by *plēno- (influenced by Latin verb plēre, to fill) \"\n \"in Latin plēnus, full'. plēnus 'full' therefore continues *pl̥h₁-no-/*pleh₁-no-, the same adjective as Germanic *fullaz. 'pl-us' is \"\n \"Latin plūs 'more' < Old Latin plous < an obscure comparative of the *plē- branch (Watkins: 'Obscure comparative form (Old Latin plous) \"\n \"in Latin plūs, more'), contaminated in the paradigm with *plēis- (superl. plūrimus, old ploirume/plūsima). Both Latin forms are \"\n \"textbook members of the root.\",\n \"صورت «pla-no» در نمودار عیناً نگارش واتکینز است: «ستاک لاتین *plāno- که زیر تأثیر فعل plēre «پر کردن» جای خود را به *plēno- داد و \"\n \"plēnus «پر» شد». پس plēnus دنبالهٔ همان صفت *pl̥h₁-no-/*pleh₁-no- است که ژرمنی *fullaz را هم ساخته است. «pl-us» نیز لاتین plūs \"\n \"«بیشتر» است، از لاتین کهن plous، صورت برترِ شاخهٔ *plē-، که در صرف با *plēis- درآمیخته و plūrimus (کهن ploirume, plūsima) را داده \"\n \"است. هر دو صورت لاتین از نمونه‌های کلاسیک این ریشه‌اند و ادعای نورایی درست است.\",\n [E_PLENTY],\n [{\"ref\": \"POK\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt p.799: 'Latin pleō, -ēre mostly com-pleō ... participle (com)pletus, plēnus \\\"full\\\" ... plūs ... to Komparativ, and with plēis- ... plūrimus \\\"mostly\\\" (old ploirume, plouruma, plusima)'.\"}],\n [{\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pelə-1, I.3 and II.2\", \"stance\": \"supports\", \"note\": AHD_NOTE},\n  {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch s.v. plēnus, plūs\", \"stance\": \"supports\",\n   \"note\": \"LEW_1910.txt files plēnus with ai. pūrṇás, got. fulls, and plūs with the comparative of the same root — the standard Latin-side account (WH 320 f., 322 f., cited by Pokorny at the end of the lemma).\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 63 ff.\", \"stance\": \"supports\", \"note\": WLD_NOTE}])\n\n# ---------------- node 16\nnode(16, \"English\", \"plenty, plus, manipulate\", \"confirmed\",\n \"plenty: Latin plēnitās, -tātem 'fullness' > Old French plentee/plenté (12th c.) > Middle English plentee (mid-13th c.) 'abundance' > \"\n \"plenty. plus: taken directly from Latin plūs 'more' (mathematical use from the 16th c.). manipulate: a 19th-c. back-formation from \"\n \"manipulation, from French manipulation, from Latin manipulus 'a handful, a company of soldiers' = manus 'hand' + the zero-grade \"\n \"*-plus of this root ('that which fills the hand'), Watkins' *manī-plo-s. Klein lists all three among the derivatives of base \"\n \"*pele-, *plē- under 'full'. Well-known Latin → Old French → English chain.\",\n \"«plenty» از لاتین plēnitās/plēnitātem «پری» > فرانسهٔ کهن plentee (سدهٔ دوازدهم) > انگلیسی میانه plentee «فراوانی» (میانهٔ سدهٔ سیزدهم) > \"\n \"plenty؛ «plus» وام‌گیری مستقیم از لاتین plūs «بیشتر» است (کاربرد ریاضی از سدهٔ شانزدهم)؛ و «manipulate» بازساختی از manipulation \"\n \"(فرانسه manipulation) از لاتین manipulus «یک مشت، دستهٔ سرباز» یعنی manus «دست» + جزء *-plus از همین ریشه («آنچه دست را پر می‌کند»؛ \"\n \"بازسازی واتکینز *manī-plo-s). کلاین هر سه را در فهرست مشتقات همین ریشه ذیل full آورده است. زنجیرهٔ لاتین ← فرانسهٔ کهن ← انگلیسی \"\n \"شناخته‌شده است و ادعای نورایی درست است.\",\n [E_PLENTY],\n [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_NOTE + \" Watkins' index lists PLENTY, PLUS and MANIPULATE (via maniple) under pelə-1.\"}],\n [{\"src\": \"KLN\", \"where\": \"s.v. 'full, adj.' cross-reference list\", \"stance\": \"supports\", \"note\": KLN_FULL},\n  {\"src\": \"SKT\", \"where\": \"Skeat s.vv. plenty, plus, maniple\", \"stance\": \"supports\",\n   \"note\": \"SKT.txt derives plenty < O.F. plente < L. plenitatem, and maniple < L. manipulus 'a handful' (manus + root of plere) — the same two chains.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, index\", \"stance\": \"supports\", \"note\": AHD_NOTE}])\n\n# ---------------- node 17\nnode(17, \"Greek\", \"pol-us\", \"confirmed\",\n \"Greek πολύς 'much, many' < *pol(h₁)-u-s, the o-grade of the u-stem *pelh₁u- that also gives Av. pouru-, OP paru-, Skt. purú- and \"\n \"Goth. filu. Pokorny (800) notes that the classical form is assimilated from *palus (< *pl̥h₁u-), the other cases being built on the \"\n \"stem πολλο-/πολλα-; Watkins simply writes 'O-grade form *pol(ə)-u- in Greek polus, much, many: POLY-; HOI POLLOI'. The node carries \"\n \"no refs in the book, but the claim is entirely standard.\",\n \"یونانی πολύς «بسیار» از *pol(h₁)-u-s، یعنی درجهٔ o همان ستاک *pelh₁u- که اوستایی pouru-، پارسی باستان paru-، سنسکریت purú- و گوتی \"\n \"filu را هم داده است. پوکورنی (ص ۸۰۰) یادآور می‌شود که صورت کلاسیک از *palus (< *pl̥h₁u-) همگون شده و حالت‌های دیگر بر ستاک πολλο- \"\n \"ساخته شده‌اند؛ واتکینز نیز می‌نویسد «درجهٔ o یعنی *pol(ə)-u- در یونانی polus». این گره در کتاب ارجاعی ندارد، ولی ادعا کاملاً معیار است.\",\n [E_POLY],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; checked against Pokorny, Walde-Pokorny, Watkins and Klein independently (all support it).\"}],\n [{\"src\": \"POK\", \"where\": \"IEW 800\", \"stance\": \"supports\",\n   \"note\": \"POK_full.txt: 'gr. polús \\\"much, a lot of\\\" (assimil. from *palus = Old Indic purú-), übrige case of stem pollo-, polla-'.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pelə-1, II.3\", \"stance\": \"supports\", \"note\": AHD_NOTE},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 65\", \"stance\": \"supports\",\n   \"note\": \"WLD_Bd2_pages.txt: 'Gr. polús (polú, polún ...) ... ist polús eher nach J. Schmidt assim. aus Adj. *palus ='.\"}])\n\n# ---------------- node 18\nnode(18, \"French\", \"poly- : multiple, many\", \"confirmed\",\n \"French poly- is the learned combining form taken from Greek πολυ-, transmitted through Latin poly- in scientific and medical \"\n \"terminology; it is productive in French from the 16th century (polygone, polygamie) and explodes in 19th-century technical coinages \"\n \"(polytechnique 1794, polycopie/polycopier late 19th c.), which is what makes node 19 possible. The element carries the Greek sense \"\n \"'many, several' unchanged.\",\n \"پیشوندِ عالمانهٔ poly- در فرانسه وام‌گرفته از یونانی πολυ- است که از راه اصطلاح‌های علمی و پزشکی لاتین به فرانسه رسیده و از سدهٔ شانزدهم \"\n \"زایا شده است (polygone، polygamie) و در سدهٔ نوزدهم در واژه‌سازی فنی فراوان به کار رفته (polytechnique ۱۷۹۴، polycopie اواخر سدهٔ \"\n \"نوزدهم) — همان راهی که گرهٔ ۱۹ را ممکن کرده است. معنی یونانیِ «بسیار، چند» بی‌تغییر مانده است؛ ادعای نورایی درست است.\",\n [E_POLY],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference given in the book for this node; checked against Etymonline s.v. poly- and Klein.\"}],\n [{\"src\": \"KLN\", \"where\": \"Klein s.v. poly- (listed among the derivatives under 'full, adj.')\", \"stance\": \"supports\", \"note\": KLN_FULL},\n  {\"src\": \"DEV\", \"where\": \"Devic / French Orientalisms — not applicable\", \"stance\": \"silent\",\n   \"note\": \"DEV.txt covers French words of Oriental origin only; poly- is Greek, so the book is silent (checked as the matrix's French reference).\"}])\n\n# ---------------- node 19\nnode(19, \"Persian\", \"(no transliteration given) — پلی کپی ، پلی تکنیک\", \"confirmed\",\n \"Twentieth-century French loans into Persian: پلی‌کپی pulikopi from French polycopie 'stencil/duplicated copy' (with پلی‌کپی کردن \"\n \"'to duplicate'), and پلی‌تکنیک politeknik from French polytechnique, the name adopted for دانشگاه پلی‌تکنیک (Tehran Polytechnic, \"\n \"founded 1928/1307 as هنرسرای عالی, later دانشگاه صنعتی امیرکبیر). Both entered Persian through the French-language schooling and \"\n \"technical vocabulary of the Qajar/early Pahlavi period, not through Greek or English; Mo'in's Farhang-e Fārsi vol. 4 is precisely \"\n \"the volume of foreign compounds where such items are tagged [فر.] (French). The node is a modern re-borrowing of the same PIE \"\n \"element, three thousand years after Old Persian paru-.\",\n \"این دو، وام‌واژه‌های فرانسویِ سدهٔ بیستم‌اند: «پلی‌کپی» از polycopie فرانسه (و ترکیب «پلی‌کپی کردن») و «پلی‌تکنیک» از polytechnique، \"\n \"که نام «دانشگاه پلی‌تکنیک تهران» (بنیادگذاشته در ۱۳۰۷، بعدها دانشگاه صنعتی امیرکبیر) از آن گرفته شده است. راه ورود، آموزش و \"\n \"واژگان فنیِ فرانسوی‌مآبِ اواخر قاجار و آغاز پهلوی بوده است، نه یونانی یا انگلیسی؛ جلد چهارم فرهنگ فارسی معین که ویژهٔ ترکیبات \"\n \"خارجی است همین‌گونه واژه‌ها را با نشانهٔ [فر.] می‌آورد. نکتهٔ جالب آنکه این عنصر هندواروپایی، سه هزار سال پس از paru- پارسی باستان، \"\n \"بار دیگر و این‌بار از راه فرانسه به فارسی بازگشته است. ادعای نورایی درست است.\",\n [E_POLY],\n [{\"ref\": \"MON\", \"status\": \"partial\",\n   \"note\": \"Nourai cites MON without a page; Mo'in's vol. 4 (ترکیبات خارجی) is the volume that carries such French compounds with the tag [فر.]. That volume is not available locally as page-indexed text, so the specific entries could not be quoted; the French origin itself is not in doubt.\"}],\n [{\"src\": \"MON\", \"where\": \"Farhang-e Fārsi vol. 4 (foreign compounds)\", \"stance\": \"partial\",\n   \"note\": \"Not readable locally page by page; the volume's purpose (foreign compounds with origin tags such as [فر.]) is what Nourai is invoking.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. poly-\", \"stance\": \"supports\",\n   \"note\": \"Klein lists poly- among the derivatives of *pele-, *plē-; the Persian items are French transmissions of that same element (polycopie, polytechnique).\"}])\n\n# ---------------- node 20\nnode(20, \"English\", \"poly-, polygon, polygamy, polynomial\", \"confirmed\",\n \"poly- 'many, much' in English is Greek πολυ-, mostly via Latin and French scientific vocabulary. polygon: Late Latin polygōnum < Greek \"\n \"polygōnon 'many-angled' (polus + gōnia 'angle'), in English from the 1570s. polygamy: Late Greek polygamia 'plurality of marriages' \"\n \"(polus + gamos 'marriage'), via Late Latin, in English from the 1590s. polynomial: a 17th-century hybrid coined on the model of \"\n \"binomial, poly- + Latin nomen/nomin- 'name, term'. Watkins' index files POLY-, POLYGON, POLYGAMY under pelə-1, and Klein lists poly- \"\n \"among the derivatives of the same base.\",\n \"پیشوند poly- در انگلیسی همان πολυ- یونانی است که بیشتر از راه لاتین و فرانسهٔ علمی وارد شده است. «polygon» از لاتین متأخر polygōnum \"\n \"و یونانی polygōnon «چندگوشه» (polus + gōnia «زاویه») و از دههٔ ۱۵۷۰ در انگلیسی؛ «polygamy» از یونانی متأخر polygamia «چندهمسری» \"\n \"(polus + gamos «زناشویی») از راه لاتین متأخر و از دههٔ ۱۵۹۰ در انگلیسی؛ و «polynomial» ساختِ دورگهٔ سدهٔ هفدهم به قیاسِ binomial، \"\n \"یعنی poly- + لاتین nomen «نام، جمله». نمایهٔ واتکینز POLY-، POLYGON و POLYGAMY را زیر pelə-1 آورده و کلاین نیز poly- را از مشتقات \"\n \"همین ریشه می‌شمارد. ادعای نورایی درست است.\",\n [E_POLY],\n [{\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt index: 'POLY- pelə-1', 'POLYGAMY gʷen-' [second element], 'POLYGON gōniā' [second element] — the poly- element is filed under pelə-1, as Nourai says; the root entry itself reads 'O-grade form *pol(ə)-u- in Greek polus, much, many: POLY-; HOI POLLOI'.\"}],\n [{\"src\": \"KLN\", \"where\": \"s.v. 'full, adj.' derivative list ('... plutocracy, poly-, replenish ...')\", \"stance\": \"supports\", \"note\": KLN_FULL},\n  {\"src\": \"SKT\", \"where\": \"Skeat s.v. poly-\", \"stance\": \"supports\",\n   \"note\": \"SKT.txt s.v. POLY- : 'Gk. polu-, crude form of polus, much, many', cognate with L. plus and E. full — the same derivation.\"}])\n\nout = {\n \"pdf_page\": 389,\n \"book_page\": 359,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry]\n}\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-389.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"nodes:\", len(N))\nPYEOF\npython3 \"/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-389.py\""
}
```


### [2026-09-14T01:06:36.330Z] TOOL RESULT

```
nodes: 20
```


## [2026-09-14T01:06:39.958Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-389.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 389"
}
```


### [2026-09-14T01:06:41.467Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'confirmed': 14, 'plausible': 5, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 22, 'partial': 4, 'contradicts': 1, 'not_checked': 5}
books consulted: {'supports': 40, 'partial': 4, 'contradicts': 6, 'silent': 6} | by book: {'WLD': 7, 'BRT': 6, 'PHD': 6, 'AHD': 6, 'KLN': 6, 'HUB': 4, 'SKT': 3, 'HRN': 2, 'ARY': 2, 'CHEUNG': 2, 'KNT': 2, 'MON': 2, 'FFD': 1, 'NYB': 1, 'BQT': 1, 'FRS': 1, 'IEC': 1, 'LEW': 1, 'POK': 1, 'DEV': 1}
```


## [2026-09-14T01:06:59.019Z] AGENT

Page 389 verified — `/home/sfmqrb/git/rishe/data/verification/page-389.json`, `verify_check.py 389` shows **0 PROBLEM lines** (20/20 nodes).

**Counts** — root: 1 confirmed. Nodes: 14 confirmed, 5 plausible, 1 disputed. Ref checks: 22 supports, 4 partial, 1 contradicts, 5 not_checked. 20 books consulted (POK, WLD, AHD/Watkins, IEC, KLN, SKT, LEW, BRT, KNT, PHD, NYB, HRN, HUB, CHEUNG, BQT, MON, FRS, FFD, ARY, DEV).

**Disputed**
- Pel 1 · #4 اوباش obāš "rowdy, gangster" — not Iranian: Arabic plural أوباش of وَبَش. Mo'in says so in the very footnote on the page Nourai cites (BQT p.180: «عربی، جمع وبش، مقلوب بوش»), Hübschmann §132 says so ("Auch Nöldeke hält aubāš für echt arabisch"), Wiktionary agrees. The verbs اوباردن/اوباشتن in the same node are fine, so the node is disputed on that one word.

**Plausible (with the divergence explained in the file)**
- #2 برنا bornā — comes from the *negated* Av. apərənāyu- "under age" (MP aburnāy), not from pərənāyu- "full of life" as drawn; por and anbār are confirmed (Horn 111 and 294, FFD p.31).
- #3 ava-par — unattested in Bartholomae; it is Horn's/Abolqasemi's reconstruction, while Cheung 2007 assigns ōbārdan to *baru̯ "devour".
- #5 "frā 1 = plenty" — frāyah-/fraēšta- are solid, but no free Avestan stem frā- "plenty" exists (fra- is the preverb "forth"); back-formed from MP frāy.
- #8 paoiryaēinī- — Pokorny 800 files it here ("Sternhaufen"), Bartholomae/Hübschmann derive it from paoirya- "first" (a different root).
- #11 فراوان farāvān — Mann (IEC p.974-5) does list it under *poluos, but the usual Iranian analysis is farā- + -vān, and *paru- > farā- is no Persian sound law.

**Extraction errors:** none — the JSON matches the chart faithfully. Two things worth knowing are the *book's* own looseness, not extraction: #13 glosses Germanic *ful-naz "to fill" (it is the adjective "full"), and #7's gloss "magic" for فرهست reproduces Borhan's error that Mo'in corrects in his footnote on the cited page.
