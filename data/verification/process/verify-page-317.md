# Verification process log — verify-page-317


## [2026-09-07T01:37:09.435Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 317 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-317.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-317.json. Write /home/sfmqrb/git/rishe/data/verification/page-317.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 317` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T01:37:11.919Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T01:37:12.621Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T01:37:12.634Z] TOOL RESULT

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


## [2026-09-07T01:37:13.211Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-317.txt"
}
```


### [2026-09-07T01:37:13.228Z] TOOL RESULT

```
1	=== PDF page 317 (book page 287) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Mad : wet, also food  (refs POK:694)
4	#1 (parent #0) [Avestan] refs=POK:694; SYN:184 | masya 1 : fish ; mada : having too much liquid, drunk ; mad : a water bird, mina
5	  #2 (parent #1) [Persian] refs=BQT:1961,2007; FRS:137 | mâhî «ماهی» : fish ; mast «مست ۱» : drunk ; mâğ «ماغ» : a black water bird, mina
6	#3 (parent #0) [Sanskrit / Armenian] refs=POK:694 | mâstu, maccum : yogurt, sour cream
7	  #4 (parent #3) [Persian] refs=HRN:215; POK:694; BQT:1941 | mâst «ماست» : yogurt | extra: ماسیدن
8	#5 (parent #0) [Sanskrit] refs=AHD:867 | madati : a water bird, mina
9	  #6 (parent #5) [Hindustani] refs=None | mainâ : mina
10	    #7 (parent #6) [English] refs=None | mina, myna : a bird
11	#8 (parent #0) [Germanic] refs=AHD | 
12	  #9 (parent #8) [English] refs=None | meat, mate 1 : companion
13	#10 (parent #0) [Latin] refs=POK:694; AHD:805 | mattus : drunk, not sober, dull | NOTE: FSD:1526 derives Latin "mattus: drunk" from Persian "mât: confused" which is borrowed from Arabic. See "M.v.t:to die".
14	  #11 (parent #10) [French] refs=None | 
15	    #12 (parent #11) [English] refs=AHD:805 | mat, matte : dull, also picture frame | NOTE: KLN:946 derives these words from a Semitic root. See root "M.v.t".
16	--- entry 1 ---
17	ROOT [Avestan / Old Persian] Madhaxa, Mazaxa, Madika : Madhaxa, Mazaxa: grasshopper. Madika: grasshopper. Page 18 in the introduction of BQT indicates that all these words are from a Sogdian root and cognate with Armenian "marax".  (refs HRN:227; HUB:100)
18	#1 (parent #0) [Pahlavi] refs=HRN:222,227; BQT:2031 | madhax, mazax, matax : grasshopper ; maig : a kind of grasshopper, shrimp
19	  #2 (parent #1) [Persian] refs=HRN:222,227; BQT:2031; MON:4503 | malax «ملخ» : grasshopper ; mayg «میگ» : shrimp | extra: میگو
20	--- entry 2 ---
21	ROOT Madika -> redirect to Madhaxa
22	--- entry 3 ---
23	ROOT [Avestan] Mağa : hole, recess  (refs HRN:221; MPP:85)
24	#1 (parent #0) [Persian] refs=BQT:2021; MPP:85; FRS:145 | mağ «مَغ ۲» : hole, a place dug in ground | extra: مَغاک ، مُغاک
25	
```


## [2026-09-07T01:37:17.002Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-317.json",
 "description": "Read source JSON"
}
```


### [2026-09-07T01:37:17.067Z] TOOL RESULT

```
{
  "pdf_page": 317,
  "book_page": 287,
  "entries": [
    {
      "root": {
        "name": "Mad",
        "lang": "Indo-European",
        "refs": "POK:694",
        "gloss": "wet, also food"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:694; SYN:184",
          "words": [
            {"translit": "masya 1", "gloss": "fish", "script": null},
            {"translit": "mada", "gloss": "having too much liquid, drunk", "script": null},
            {"translit": "mad", "gloss": "a water bird, mina", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1961,2007; FRS:137",
          "words": [
            {"translit": "mâhî", "gloss": "fish", "script": "ماهی"},
            {"translit": "mast", "gloss": "drunk", "script": "مست ۱"},
            {"translit": "mâğ", "gloss": "a black water bird, mina", "script": "ماغ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "همچو هندو که او بود غوّاص - ماغ درآب درّجوی شدست",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit / Armenian",
          "refs": "POK:694",
          "words": [
            {"translit": "mâstu, maccum", "gloss": "yogurt, sour cream", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "HRN:215; POK:694; BQT:1941",
          "words": [
            {"translit": "mâst", "gloss": "yogurt", "script": "ماست"}
          ],
          "script_extra": "ماسیدن",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD:867",
          "words": [
            {"translit": "madati", "gloss": "a water bird, mina", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Hindustani",
          "refs": null,
          "words": [
            {"translit": "mainâ", "gloss": "mina", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "mina, myna", "gloss": "a bird", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "meat, mate 1", "gloss": "companion", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:694; AHD:805",
          "words": [
            {"translit": "mattus", "gloss": "drunk, not sober, dull", "script": null}
          ],
          "script_extra": null,
          "note": "FSD:1526 derives Latin \"mattus: drunk\" from Persian \"mât: confused\" which is borrowed from Arabic. See \"M.v.t:to die\".",
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "AHD:805",
          "words": [
            {"translit": "mat, matte", "gloss": "dull, also picture frame", "script": null}
          ],
          "script_extra": null,
          "note": "KLN:946 derives these words from a Semitic root. See root \"M.v.t\".",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Madhaxa, Mazaxa, Madika",
        "lang": "Avestan / Old Persian",
        "refs": "HRN:227; HUB:100",
        "gloss": "Madhaxa, Mazaxa: grasshopper. Madika: grasshopper. Page 18 in the introduction of BQT indicates that all these words are from a Sogdian root and cognate with Armenian \"marax\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "HRN:222,227; BQT:2031",
          "words": [
            {"translit": "madhax, mazax, matax", "gloss": "grasshopper", "script": null},
            {"translit": "maig", "gloss": "a kind of grasshopper, shrimp", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:222,227; BQT:2031; MON:4503",
          "words": [
            {"translit": "malax", "gloss": "grasshopper", "script": "ملخ"},
            {"translit": "mayg", "gloss": "shrimp", "script": "میگ"}
          ],
          "script_extra": "میگو",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Madika",
        "redirect": "Madhaxa"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Mağa",
        "lang": "Avestan",
        "refs": "HRN:221; MPP:85",
        "gloss": "hole, recess"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:2021; MPP:85; FRS:145",
          "words": [
            {"translit": "mağ", "gloss": "hole, a place dug in ground", "script": "مَغ ۲"}
          ],
          "script_extra": "مَغاک ، مُغاک",
          "note": null,
          "quote": {
            "text": "ابله و فرزانه را فرجام خاک - جایگاه هر دو اندر یک مغاک",
            "poet": "Rŭdakî"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-07T01:37:17.620Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && ls data/verification/sources/refs/ | head -80",
 "description": "List verification dirs"
}
```


### [2026-09-07T01:37:17.675Z] TOOL RESULT

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
----
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


## [2026-09-07T01:37:23.455Z] TOOL CALL #5: Bash

```json
{
 "command": "head -60 data/verification/page-309.json && echo \"=== matrix ===\" && sed -n 1,80p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Sample verification file and matrix"
}
```


### [2026-09-07T01:37:23.519Z] TOOL RESULT

```
{
  "pdf_page": 309,
  "book_page": 279,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-06",
  "entries": [
    {
      "entry": 0,
      "root": "Lěk, Lak; Lakt, Lakat",
      "verdict": "confirmed",
      "modern_form": "PIE *leh₂k- (traditional *lēk- : *lək-) 'to tear, rend', with a t-extension *lakt-/*lakat- 'rag, scrap'",
      "note": "The root itself is standard. Pokorny 674 has 'lēk-2 : lak-, Meaning: to tear, fell, fur, leather, bark' with Gr. λακίς, λακίζω and Lat. lacer, lacerna, lacinia; Walde-Pokorny II 419 f. has the same as 'lēq- : lǝq- zerreißen'; Watkins/AHD has 'lēk-. To tear. Zero-grade form *lək- becoming *lak- … Latin lacer, torn: LACERATE. [Pok. 2. lēk- 674]'. The language label 'Indo-European' and the gloss 'to tear; rag, scrap' are right. The second half of the root box, the t-stem 'Lakt, Lakat', is Mann's alone (IEC 660-661 'lakt-, lakot- rag, scrap, tatter'), built on Lith. lãkatas, Latv. lakats, Pers. laxt, Arm. latʿ and Skt. laktaka-; Pokorny and Walde-Pokorny do not set up such a stem, and WP II 420 explicitly rejects the Sanskrit member. Modern laryngealist handbooks (de Vaan, EDL 320-1) reconstruct the root as *leh₂(k)- 'bark, tear'.",
      "note_fa": "ریشهٔ بازسازی‌شدهٔ هندواروپایی آغازین *leh₂k- (در سنت قدیم *lēk-/*lək-) به معنی «دریدن، پاره کردن» ریشه‌ای شناخته و پذیرفته است: پوکورنی (ص ۶۷۴) آن را با یونانی λακίς «پاره، ژنده» و لاتینی lacer «دریده» می‌آورد و واتکینز در پیوست فرهنگ American Heritage نیز همان را دارد. برچسب زبانی و معنای ریشه در نمودار نورایی درست است. اما بخش دوم جعبهٔ ریشه، یعنی ستاک *lakt-/*lakat-، تنها از آنِ مان (فرهنگ تطبیقی هندواروپایی، ص ۶۶۰–۶۶۱) است و پوکورنی و والده-پوکورنی چنین ستاکی نمی‌سازند؛ والده-پوکورنی (ج ۲ ص ۴۲۰) حتی واژهٔ سنسکریت laktaka- را به دلیل ناسازگاری در نظام آواگردان (ablaut) از این خانواده بیرون می‌گذارد. رویِ‌هم ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://www.etymonline.com/word/lacerate",
        "https://en.wiktionary.org/wiki/lacer"
      ],
      "ref_check": [
        {"ref": "POK:674", "status": "supports", "note": "POK_full.txt line 56672 ff.: 'Root / lemma: lek-2 : lak-  Meaning: to tear, fell, fur, leather, bark…  Material: Gr. λακίς \"scrap, shred\" … Latin lacer, -era, -erum \"to tear to pieces, mangle, rend\" … References: WP. II 419 f., WH. I 742 f.  Page(s): 674'. The printed page number Nourai cites is exactly right."},
        {"ref": "IEC:660,661", "status": "supports", "note": "IEC.txt, form-feed leaf 372 (awk NR==373; the leaf carries printed pp. 660-661): 'lak- (1) \"tear, rag\". Cf. lakt- (1)  Gk. lakís, f. \"rag, rip, tear\"; Lat. cf. lacer …' and 'lakt-, lakot- \"rag, scrap, tatter\". Cf. lak- (1)  Skt. (dim. type) laktakah \"rag\"; Per. laxt, laxd \"scrap\"; Arm. latʿ \"garment, cloth, rag\" beside lati \"scrap\"; Li. lákatas \"rag\"'. Every node of the chart comes from these two Mann entries."}
      ],
      "consulted": [
        {"src": "WLD", "where": "Bd. II 419-420 s.v. 'lēq- : lǝq- zerreißen'", "stance": "supports", "note": "grep 'lacer,' in incoming/WLD/WLD_Bd2_pages.txt line 27845: 'Gr. λακίς \"Fetzen\", λάκος n. ds. …, λακίζω \"zerreiße\" …; lat. lacer, -era, -erum \"zerfetzt, zerrissen, zerfleischt\" …'. Same root, same members — but line 27865 adds 'Ai. laktaka- m. \"Lappen\" (Prellwitz² 258) widerspricht im Ablaut.'"},
        {"src": "AHD", "where": "Watkins 1985 p. 33 (AHD_watkins1985.txt line 680) s.v. lēk-", "stance": "supports", "note": "'lēk-. To tear. Zero-grade form *lək- becoming *lak-. 1. Latin lacinia, flap of a garment: LACINIATE. 2. Suffixed form *lak-ero- in Latin lacer, torn: LACERATE. [Pok. 2. lēk- 674.]'"},
        {"src": "SYN", "where": "Buck, ch. 6.21 'rag' (SYN.txt line 10391)", "stance": "partial", "note": "'…erh. fr. lacer \"torn\" … λακίς \"rag\", λακίζω \"tear\" … WaldeP. 2.419 f.' — Buck cites the same root for Latin lacinia/lacer but discusses no Iranian or Indic member."},
        {"src": "KLN", "where": "vol. 2 s.v. 'lacerate' (KLN_1966.txt line 20950)", "stance": "supports", "note": "'fr. lacer, \"torn\", fr. I.-E. base *leq-, *lq-, \"to rend\", whence also Gk. λακίς, \"tatter, rag\", λακίζειν, \"to tear to pieces\", Alb. lakur, \"naked\"…'"}
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Persian",
          "words": "laxt «لَخت ( لَت )»",
          "verdict": "plausible",
          "derivation": "NP لَخت laxt 'piece, portion, fragment, scrap' is a real and old word — Ferdowsi's line quoted in the chart (deh laxt 'ten pieces') is genuine, and Borhan-e Qateʿ s.v. لخت glosses it 'و بمعنی پارچه و حصه و برخ و جزو و پاره است همچو لخت کوه و لخت جگر' (v. 3, pdf p. 688), Moʿin 'جزو، نوع، قسم'. The variant لَت lat printed in parentheses is the short doublet ('a piece; a blow'), cf. Borhan v. 3 p. 686 'لت لت بمعنی پاره پاره و لخت لخت'. Formally Nourai's derivation is unobjectionable: an Old Iranian *lakta- would give Middle/New Persian laxt regularly (Ir. *-kt- > *-xt-, as in *saxta- > saxt, *duxta- > duxt), and Mann (IEC 661) lists 'Per. laxt, laxd \"scrap\"' beside Lith. lãkatas and Arm. latʿ under *lakt-. But there is no Avestan, Old Persian or attested Middle Persian antecedent (MacKenzie's CPD has no laxt), Pokorny records no Iranian reflex of *lēk- at all, and en.wiktionary, following Monchi-Zadeh 1990 p. 115 no. 336, calls laxt 'an imitative element borrowed from dialects', i.e. denies the inherited IE pedigree. So: right word, right meaning, derivation accepted by Mann (and hence by Nourai) but not independently established.",
          "derivation_fa": "واژهٔ «لَخت» به معنی «پاره، تکه، جزء» واژه‌ای اصیل و کهن در فارسی دری است؛ بیت فردوسی که نورایی آورده («همان تخت پیروزه ده لَخت بود») درست است و برهان قاطع (چاپ معین، ج ۳) ذیل «لخت» می‌نویسد: «و بمعنی پارچه و حصه و برخ و جزو و پاره است همچو لخت کوه و لخت جگر»؛ معین نیز «جزو، نوع، قسم» آورده است. صورت «لَت» که در پرانتز آمده دوگانهٔ کوتاه‌شدهٔ همان واژه است. از نظر آوایی هم اشکالی در کار نیست: خوشهٔ ایرانی باستان ‎*-kt-‎ در فارسی میانه و نو به ‎-xt-‎ بدل می‌شود (مانند *saxta- > سخت)، پس *lakta- ← لخت پذیرفتنی است و مان (IEC ص ۶۶۱) نیز همین را کنار لیتوانیایی lãkatas و ارمنی latʿ آورده است. با این حال هیچ صورت اوستایی یا پهلوی گواهی‌شده‌ای در دست نیست (مکنزی «laxt» ندارد) و پوکورنی هیچ بازماندهٔ ایرانی برای این ریشه نمی‌آورد؛ ویکی‌واژه به پیروی از مونشی‌زاده آن را عنصری «آوابنیاد و برگرفته از گویش‌ها» می‌داند. بنابراین ادعای نورایی با احتیاط پذیرفتنی است.",
          "sources": [
            "https://en.wiktionary.org/wiki/%D9%84%D8%AE%D8%AA",
            "https://abadis.ir/fatofa/%D9%84%D8%AE%D8%AA/"
          ],
          "ref_check": [
            {"ref": "IEC:661", "status": "supports", "note": "IEC.txt leaf 372 s.v. 'lakt-, lakot-': '… Per. laxt, laxd \"scrap\"; Arm. latʿ \"garment, cloth, rag\" beside lati \"scrap\" …' — exactly Nourai's arrow."},
            {"ref": "MON:3563,3573", "status": "partial", "note": "Only the online Moʿin text (abadis.ir/fatofa/لخت) is accessible and it has both headwords with Nourai's senses — لَخت (اِ.) 'جزو، نوع، قسم' and لُخت 'برهنه، عریان' — but the online version carries no page numbers, so pp. 3563/3573 of the 6-vol. print could not be verified."}
          ],
          "consulted": [
            {"src": "BQT", "where": "vol. 3 (Moʿin ed.), pdf p. 688 s.v. لخت", "stance": "supports", "note": "grep 'لخت' in incoming/BQT/BQT_v3_pages.txt line 50920: 'و بمعنی پارچه و حصه و برخ و جزو ‌و پاره است همچو لخت کوه و لخت جگر' — the sense 'scrap, piece' that Nourai gives; the footnotes give only Persian cross-references, no IE etymology."},
            {"src": "MON", "where": "abadis.ir Moʿin s.v. لخت", "stance": "supports", "note": "'(لَ) (اِ.) جزو، نوع، قسم' and separately '(لُ) برهنه، عریان' — no origin tag ([په.] etc.), i.e. Moʿin claims no Pahlavi antecedent."},
            {"src": "PHD", "where": "MacKenzie, CPD — searched PHD.txt / PHD_mackenzie.txt for 'laxt', 'lht'", "stance": "silent", "note": "no Middle Persian laxt is recorded; the only l-a-b/l-a-h entries are lab 'lip', lābag 'supplication', šahr etc. So the word first surfaces in New Persian."},
            {"src": "HRN", "where": "Horn, Grundriss (HRN.txt), searched 'laxt', 'lacht'", "stance": "silent", "note": "Horn has no entry for laxt (his L-section, nos. 952-954, covers only lābe/lāf, leb, lēstan)."},
            {"src": "ARY", "where": "incoming/ARY/ARY_pages.txt, grep 'لخت'", "stance": "silent", "note": "Aryanpur's IE-roots dictionary has no headword لخت."}
          ]
        },
        {
          "id": 2,
          "lang": "Armenian",
          "words": "lat",
          "verdict": "plausible",
          "derivation": "Armenian լաթ latʿ 'cloth, rag, garment, tatter' (beside լաթի latʿi 'scrap') is a real word with exactly the meaning given, and Mann (IEC 661) lists it under *lakt- as a cognate of Persian laxt. Armenian lexicography, however, treats it as a loan rather than an inheritance: hy.wiktionary s.v. լաթ says flatly 'Փոխառություն՝ պարսկերեն lat' ('a borrowing from Persian lat'), which is also what the form suggests — an inherited *lakto- should have left a trace of the velar, whereas the bare latʿ matches New Persian lat one-for-one, in the same way as the many Persian textile terms borrowed into Armenian. Pokorny and Walde-Pokorny record no Armenian member of this root. So the word belongs to the family, but the arrow 'straight from the IE root' is probably an arrow through Persian.",
          "derivation_fa": "واژهٔ ارمنی լաթ (latʿ) به معنی «پارچه، کهنه، جامه» واقعی است و معنایی که نورایی داده درست است؛ مان (IEC ص ۶۶۱) آن را همراه با «لخت» فارسی زیر ستاک *lakt- آورده است. اما فرهنگ‌های ارمنی آن را وام‌واژه می‌دانند نه میراث مستقیم: ویکی‌واژهٔ ارمنی ذیل լաթ می‌نویسد «وام‌گرفته از فارسی lat». صورت واژه هم همین را تأیید می‌کند، زیرا اگر از *lakto- به ارث رسیده بود انتظار بازتابی از همخوان کامی می‌رفت، حال آنکه latʿ دقیقاً برابرِ «لَت» فارسی است — همانند بسیاری از نام‌های پارچه و جامه که از ایرانی به ارمنی رفته‌اند. پوکورنی و والده-پوکورنی هیچ عضو ارمنی برای این ریشه نمی‌آورند. پس واژه به همین خانواده تعلق دارد، ولی پیکان نمودار (مستقیم از ریشه) به احتمال زیاد باید از راه فارسی بگذرد.",
          "sources": [
            "https://hy.wiktionary.org/wiki/%D5%AC%D5%A1%D5%A9"
=== matrix ===
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
```


## [2026-09-07T01:37:26.315Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','BQT','FRS','HRN','AHD','FSD','KLN','HUB','MON','MPP','PHD','NYB','BRT','KNT','WLD','IEC','SKT','WEB','HJB','AID','LKT','TTS','CHEUNG','ARY','SOD']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-07T01:37:27.945Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_p
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
MPP {"title": "W. B. Henning, \"A List of Middle-Persian and Parthian Words\", Bulletin of the School of Oriental Studies IX (1937–39), pp. 79–92", "edition_found": "1958", "kind": "archive_djvu", "url": "https://archive.org/details/henning-1958-mitteliranisch", "identifier": "henning-1958-mitteliranisch", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/MPP.txt", "page_offset": "l
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in
```


## [2026-09-07T01:37:58.951Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 69[45]\" POK_full.txt | head; echo ===; grep -n \"^Root / lemma: mad\" POK_full.txt | head",
 "description": "Find Pokorny page 694"
}
```


### [2026-09-07T01:37:59.004Z] TOOL RESULT

```
Exit code 1
57111:Page(s): 694-695 
57192:Page(s): 695 
57791:Page(s): 694 
(eval):1: == not found
```


## [2026-09-07T01:37:59.737Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"mattus\" *.txt | head -30",
 "description": "Grep mattus"
}
```


### [2026-09-07T01:37:59.803Z] TOOL RESULT

```
ISS_alt_DKS.txt:6058:máni-— malaiga 329 heated’. From base mad-, present mád-, participle masta- ‘drunken’; másta- ‘thick milk'; 10 Ау. mad-, maéaya-, masta-, maài-masta(t2)ma-; Zor.P. ma&enitan, mat ' wine (i£ not *mad(h)u- see s.v. mau), mast, N.Pers. mat, mast ‘drunk; in heat’, Sogd. Bud. mst- (mst-kr'k, mst-&'r &), mst'wny, myst'h 'intoxicated', Man, omst-A'ryy 'intoxi- cating’; M.Parth.T. mstyft ' drunkenness’. IE Pok. 694-5 mad- ' moist; drip; drip with fat; fodder’, O.Ind. тайа -te, mádyati, татай, mdndati ; mada- ' intoxicant drink’, mattd-, Greek рабйсо ‘dissolve’, робарёс ‘moist’, Lat. madeó “е moist’, mattus ‘drunk’, Celtic O.Ir. maid in intr. ‘ро to pieces’, O.Engl. más 'mash' < *madso-. The base mad- 'coagulate' may be homonyrnous or the same base mad- t be moist’ (so assumed IE Рок. 694), Khotan Saka müsta- 'coagulated', amüsta- ‘not coagulated’, Zor.P., N.Pers. mast ‘thick milk', O.Ind. mdstu- 'thick cream’ (-d-t-, or -dst-), N.Pers. masidan ‘to coagulate’ (-ds- ог -df-), Ва1б& mastay ' curds', Магу Balöčī bastag 'sour milk’, badag, тадау ‘о coagulate’, Waxi т08-, 1188: ' curdled', Kurd. main 'to coagulate’, Yayn. mayd-, maydta, mayt ' hard* (of milk), Sarikoli znád, тоб butter- milk’, See maya-, meua, mada-, masta-, maitti, hamatte.
POK_full.txt:57091:Latin madeo, -ere" to be wet, be moist, drip, flow ', mattus' drunk, intoxicated ' {*madi- 
LAT.txt:35625:Cf. peut-etre aussi matus, *mattus , M. 1.5428; madulsa,-ae f.: raot
LAT.txt:36870:mattus: v. matus.
LAT.txt:36911:On lit aussi mattus (natus): tristis, CGL IV 114,4; 337,5; 536,31;
LAT.txt:36914:*mattus, 5438.
LAT.txt:36915:Mattus peut reprdsenter une prononciation vulgaire (dialectale)
POK_02.txt:5653:lat.  madeö,  -ere  ^naß  sein,  von  Nässe  triefen,  reifen,  voll  sein%  mattus trunken'  {*madi-to-s)'^
SKT.txt:11272:treat ;     Gk.    ftiyat,    prat  ;    L.    mattus, ODOured;  Gk.  /n/xar^,  means;  Ski,  moK, to  hoDoor.     ;V  ^0H.>
FSD_vol3.txt:15877:mas'lio-don, 1 rnus'to-don, 2 iiifts'tti-dAii, ti 1. An ex- ( (* matt, dim < I 2 I. mattus, see juatb^, » J *>**!«. #*?*•«**** “*****?
FSD_vol1.txt:59108:feeble,  false,  <   LL.  mattus,  dull,  <   Per.  mat,  confounded.)
KLN_1971.txt:147403:mattus, ‘intoxicated’, OE. mxst, ‘mast (of 
KLN_1966.txt:23156:Derivative:  mattock,  tr.  v. mattoid,  n.,  a  person  of  abnormal  mind  verging on  insanity.  —  It.  mattoide,  a  hybrid  coined  fr. It.  matto,  ‘mad’,  and  Gk.  -octS-i)?,  ‘like’,  fr. elSo?,  ‘shape,  form’.  The  first  element  derives fr.  L.  mattus,  intoxicated’,  fr.  mad(i)dus,  ‘moist, wet;  drunk,  intoxicated’,  fr.  madere,  ‘to  be  wet; to  be  drunk  or  intoxicated’,  fr.  I.-E.  base  mad-, ‘wet,  moist,  dripping;  to  drip’.  See  meat  and  cp. mast,  ‘fruit  of  beech’.  For  the  second  element  in mattoid  see  -oid.
KLN_1966.txt:23247:paSapop,  ‘wet,  watery’,  paSaptomp,  ‘baldness’, L.  madere,  ‘to  be  wet;  to  be  drunk,  to  be  intoxi¬ cated’,  rnadidus,  ‘moist,  wet,  drunk ;  intoxicated’, mattus,  ‘intoxicated’,  OE.  mxst,  ‘mast  (of beech)’,  msestan,  ‘to  fatten’,  OIr.  mat,  ‘pig, swine’  (prop,  ‘a  fattened  animal'),  Oir.  maisse (for  *mad-tja),' food’.  Cp.  the  second  element  in laemus.  Cp.  also  madarosis,  mast,  ‘fruit  of beech’,  masto-,  mastoid,  mate,  ‘companion’, mattoid,  must,  ‘frenzied’.  For  sense  develop¬ ment  of  OE.  mete,  etc.,  ‘food’,  into  E.  meat,  etc., ‘flesh  of  animals’,  cp.  Heb.  lehem,  ‘bread,  food’, with  Arab,  lahm,  ‘flesh’.
SYN.txt:8297:7. Skt. matta- ‘drunk’, pple, of mad- ‘be drunk, rejoice’ = Ay. mas- ‘pet drunk’ (pple. masta- happens not to be quotable in this sense, but ef. NPers, mast ‘drunk’) : Lat. madére ‘be wet? also ‘be drunk’ (whence madidys vet, soaked, drunk’; mattus, Petr, Sat. 41 and in glosses ‘drunk’ fr. *maditus), Grk. Hadaw ‘be moist, flaccid’ (of a disease of fig trees), ‘fall out’ (of hair), padapss ‘wet’. Walde-P. 2.230f. Walde-H, 2.6 f.
```


## [2026-09-07T01:38:05.487Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '57060,57115p' POK_full.txt",
 "description": "Print Pokorny mad- entry"
}
```


### [2026-09-07T01:38:05.538Z] TOOL RESULT

```
Germanic *mad-do-or *mad[e]z-do-= Old High German masV fattening '; the specific 

meaning " fattening ' also in this formation previously Indo Germanic); mastu- n. "sour 

skimmings' {*mad-stu-), npers. /77as/ra/7 'frische butter' {*mad-sk-7); Old Indie madya-, 

madira- " intoxicating '; 

skyth. Maroaq " Danube, river in Europe ', PN Ma5uri<;, VN MaTUKerai " Danube resident 



Armenian mataF young, fresh, tender'; macun^sour, coagulated milk' {*mad/o- + 
Armenian Suff. -un), macanim, macnum ' stick, adhere, cling to, coagulate '; additional 



iran. words for Dickmilch , so npers. mast' sow milk', masTdan' curdle, coagulate, harden 
', etc.; 



gr. |ja5acb "zerfliefle, lose myself auf, verliere die hair'; |ja5ap6(; "humid, wet'; against it 
Ma^6(; " nipple ' (= Old High German mast, *mad^-dos), \xaai6c, "breast' ( *mad-tds), \xaGQ6c, 
ds. (reshuffling after aTr|9o(; "breast'); 

alb. manj {*madnid) "fatten', ma/m lat', maze' skimmings, cream, skin in milk' {*madja)\ 
madh' cornmeal mash ', changing through ablaut module, motu/e'pea', modhe' ryegrass 



Latin madeo, -ere" to be wet, be moist, drip, flow ', mattus' drunk, intoxicated ' {*madi- 
to-s); 

Old Irish ma/d/m'break (intr.), break in pieces ' (actually " dissolve, melt ', formal = Latin 
madeo); in-madae' in vain, without success ' (in addition probably c. /77ao'o'e^ "legislate, 
pass, approve, forgive ', abret. in madau' to the ground, to the bottom '; Gaelic maistir 
"urine ' {* mad-tri-)\ Middle Irish mati. "swine' {*madda' fattened pig '); 

Old High German /775s/"food, fattening, acorn mast ', Modern High German Mast, 
Mastung, Old English msest' beechnut'; Gothic mats'6\s\\, food'. Old Icelandic matrm., 
Old English metem., Old High German maz n. ds. (Modern High German still in Messer 
from Old High German mezzi-rahs), as well as Gothic matjan'eat, devour ', Old Icelandic 
met/a' slurp ', Old English mettanleed', Middle Low German mat{e) "buddy, friend, esp. 
in the nautical slang ' (Maat), Old High German gamazzo' buddy, friend '; in addition also 
Middle Low German met' pork ', nnd. mett' chopped flesh'. Old High German (actually 
ndd.) Mettwurst {irom andd. *matja-)\ changing through ablaut Old English Old Saxon mos 
"porridge, mash, dish, food'. Old High German muos' cooked, esp. mushy dish, food, 
eating generally ', Modern High German Mus, Gemiise {*madso-). 

References: WP. II 231 f., WH. II 6 f.; Kuiper Nasalpras. 140. 
Page(s): 694-695 

Root / lemma: mahghos, -a 

Meaning: young, servant, servant of god
```


## [2026-09-07T01:38:05.764Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '57760,57800p' POK_full.txt",
 "description": "Print Pokorny page 694 second hit"
}
```


### [2026-09-07T01:38:05.817Z] TOOL RESULT

```
Meaning: mother (expr. root) 

Note: redupl. mahma, mahmma, partly (dissimilation?) mahna, /77a/7/7a of dubious age 

Material: Old Indie /77a 'mother'; 



Doric pa '|jr|T£p!' (in pa ya "o mother eartli', Aisch.), wliereof Ionian Attic paTa "motlier, 
wet nurse, midwife ', Doric 'grandmother'; derived Middle Low German moje^ mother's 
sister ', Old High German holz-muoja " witch '; 

Old Indie mama-vocatWe m. "uncle' (from *mama^ mother's sister'); npers. mam, 
mama, mamfmoihex'; 

Maybe vocative alb. mami^ mother', mamia' midwife '. 

Armenian /775/77 "grandmother' (gr. loanword as papl); gr. papipa baby word vocative, 
whereof Ionian Attic MOMMH mother', pappia "mother'; Latin 7775/77/775 nickname of affection 
"mama, ma, mommy, mom, mother', also " brisket ', mamilla^ nipple '; alb. meme Geg 
mame' mother'; Irish cymr. corn. bret. /775/77 "mother'. Old Irish mu/mmeloster mother' 
{*mammia)\ Modern High German Alemannian /775/77/77e "mother', changing through ablaut 
Old High German muoma' mother's sister'. Modern High German Muhme, Lithuanian 
mama, moma, Latvian mama ds.; russ. (etc.) /775/77a"mama, ma, mommy, mom, mother'; 
Hittite divinity Mamma; compare Asia Minor Mr|vr|, ngr. pavva "mother'. Old Icelandic 
/770/75 "mother', Middle Low German *mdne, mome^ mother's sister '. 

References: WP. II 221 f., WH. II 21 f., Traulmann 168; ma\s (?) base from mater- {see 

there). 

Page(s): 694 

Root / lemma: meM^i- meMNo- 

Meaning: middle 

Material: Old Indie madhya-, Avestan maidya-^ medial', Superl. Old Indie madhyama-, 

Avestan madema-' medial' (= Gothic miduma);
```


## [2026-09-07T01:38:10.643Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '57030,57062p' POK_full.txt",
 "description": "Print Pokorny mad- head"
}
```


### [2026-09-07T01:38:10.704Z] TOOL RESULT

```
o/k/" "animal' and "louse'; or to Old Church Slavic /okb above S. 655? 

References: WP. II 443, Specht Indo Germanic Dekl. 44, Trautmann 336, Lohmann 
ZceltPh. 19, 62ff. 
Page(s): 692 

Root / lemma: mahd- 

Meaning: wet; glossy, fat, well-fed, intoxicating 

Note: 

Root/ lemma: mad-: wet; glossy, fat, well-fed, intoxicating : Root/ lemma: meA^w. honey, 

intoxicating. 

Material: Old Indie madati, madate'boW, effervesce, be cheerful', madyati, mamatti, 

mandati6s., mada-m. " Rauschtrank ' = Avestan mada-' Rauschtrank, 

Rauschbegeisterung ', Old Indie matta-^ intoxicated, gleeful, excited, aroused ', Avestan 

mad- {madaite, madayaijha) " become intoxicated, get amused '; Old Indie madgu-^ a 

certain water bird, a fish '= np. may^a water bird ', Old Indie matsya- m., Avestan masya 

"fish' (" the wet '; derivative from an -e5-stem *mades-)\ Old Indie medas-v\. "fat', medana- 

n. " fattening ', medyati, medate^ becomes fat ', medya-la\! {meda-irom *mazda-, Indo 

Germanic *mad-do-or *mad[e]z-do-= Old High German masV fattening '; the specific 

meaning " fattening ' also in this formation previously Indo Germanic); mastu- n. "sour
```


## [2026-09-07T01:38:28.678Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -A14 \"^mad-\" AHD_watkins1985.txt | head -40",
 "description": "Watkins mad-"
}
```


### [2026-09-07T01:38:28.724Z] TOOL RESULT

```
708:mad-. Moist, wet; also refers to various qualities of food. 1. Sanskrit madati, “it gladdens, it bubbles,” hence madana-, delightful, joyful, hence madanah, a myna bird: MYNA. 2. Suffixed form *mad-i- in Germanic *mati- in: a. Old English mete, food: MEAT; b. Middle Low German (ge)mate (ge-, together, from Germanic *ga-; see kom), “he with whom one shares one’s food,” compan- ion: MATE}, 3. Suffixed form *mad-sto-, becoming *mazdo-, in Germanic *masta- in Old English mest, fodder: MasT?. [Pok. mad- 694.]
709-mag-. Also mak-. To knead, fashion, fit. 1. Germanic *mak- in: a. Germanic verb *makén, to fashion, fit, in (i) Old English macian, to make: MAKE (ii) Old French mason, mason: MASON; b. Germanic compound noun *ga-mak-(j)6n (*ga-, with, together; see kom), “he who is fitted with (another),” in Old English gemzcca, mate, spouse: MATCH}, 2. Germanic nasalized form *mangjan, to knead together, in: a. Old English mengan, to mix: MINGLE; b. Old English gemang (ge-, together; see kom), mixture, crowd: AMONG, MONGREL. 3. Suffixed form *mak-yo- in Greek massein (aorist stem mag-), to knead, hence magma, unguent: MAGMA. 4, Suffixed length- ened-grade form *mdg-ya- in Greek maza, a (kneaded) lump, barley cake: MASS; (AMASS), MAZAEDIUM. 5. Suf- fixed lengthened-grade form *mék-ero- in Latin macerdre, to tenderize, to soften (food) by steeping: MACERATE. [Pok. mag- 696, 2. madk- 698, men(a)k- 730.]
710-magh-'. To be able, have power. 1. Germanic *snag- in: a. Old English magan, to be able: May; b. Old French esmaier, to frighten: DISMAY. 2. Germanic suffixed form *mah-ti-, power, in Old English miht, power: MIGHT!. 3. Germanic suffixed form *mag-inam, power, in Old English mzgen, power: MAIN}. 4. Suffixed length- ened-grade form *magh-and-, “that which enables,” in Greek (Attic) mékhané, (Doric) madkhand, device: MA- CHINE, MECHANIC, (MECHANISM), (MECHANO-). 5. Possi- bly suffixed form *magh-u- in Old Persian magus, member of a priestly caste (< “mighty one”): (MAGI), (MAGIC), MAGUS; ARCHIMAGE. [Pok. magh- 695.]
711-magh-. To fight. Hypothetical Old Iranian *ha-maz-an-,
712-“warrior” (*ha-, with < *sm-; see sem-'), possibly borrowed into Greek as Amazén, Amazon: AMAZON. [Pok. magh- 697.]
713-maghu-. Young person of either sex. Suffixed form *magho-ti- in Germanic *magadi-, with diminutive *ma- gadin-, in Old English mezgden, virgin: MAID, MAIDEN. [Pok. maghos 696.]
714-mai-'. To cut. 1. Suffixed form *mai-d- in Germanic *mait- in: a. Germanic *é-mait-jon, “the biter” (prefix *6., meaning uncertain, from Indo-European @, 6; see Pok. é, 6 280), a small biting insect, in Old English #mette, ant: ANT, EMMET; b. Germanic *mitén-, “the
715-mas
716-biter,” a small biting insect, in (i) Old English mite, mite: MITE! (ii) Middle Dutch mite, insect, small object, small coin: MITE?; c. possibly Old French mahaigner, to maim (> Anglo-Norman mangler, to hack): MAIM, MANGLE!, MAYHEM. 2. Suffixed form *mai-lo- in Old Irish méel, shorn, bald, hornless, akin to the source of MULEY. [Pok. 1. mai- 697.]
717-mai-2. To soil, defile. Possible root. 1. Suffixed form *mai-lo- in Germanic *mail- in Old English mdi, spot, blemish: MOLE!, 2. Suffixed variant form *mi-an-yo- in Greek miainein, to pollute: MIASMA; AMIANTHUS. [Pok. 2. mai- 697.]
718-mak-'. Poppy. Probably borrowed into Indo-European, as the plant is of Mediterranean origin. Lengthened-grade form *mék- in Greek mékén, poppy: MECONIUM. [Pok. mak(en)- 698.]
719-mak-2. (Leather) bag. Germanic form *magon-, bag, stomach, in Old English maga, stomach: Maw. [Pok. mak- 698.]
720-mak-. Long, thin. 1. Zero-grade form *mak- becoming *mak- in suffixed form *mak-ro- in: a. Latin macer, thin: MAIGRE, MEAGER; EMACIATE; b. Greek makros, long, large: MACRO-, MACRON; AMPHIMACER. 2. Suffixed form *mdk-es- in Greek mékos, length: MECOPTERAN, PARA- MECIUM. [Pok. mak- 699.]
721-[malakhé. Mallow. Greek noun, akin to Latin malva, mallow, both probably borrowed from a pre-Indo-Euro- pean Mediterranean language. 1. Greek malakhé, molo- khé, mallow: MALACHITE. 2. Latin malva, mallow: MALLOW, MAUVE.]
722-man-'. Also mon-. Man. 1. Extended forms *manu-, *manw- in Germanic *manna- (plural *manniz), in: a. Old English man(n) (plural menn), man: MAN; Nor- MAN; b. Old High German man (> Middle High German man > German Mann), man: FUGLEMAN, LANDSMAN?; c. Middle Dutch man, man: MANIKIN, (MANNEQUIN); d. Old Norse madhr, mannr, man: NORMAN, OMBUDS- MAN. 2. Germanic adjective *manniska-, human, in Old High German mennisco, human: MENSCH. 3. Slavic suf- fixed form *mon-gyo- in Russian muzh, man: MUZHIK. [Pok. manu-s 700.]
```


## [2026-09-07T01:38:30.610Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"madgu\" *.txt incoming/*/*.txt 2>/dev/null | head -20; echo ====; grep -n -i \"mainā\\|maina\\b\\|mynah\\|myna\\b\" KLN_1966.txt SKT.txt HJB.txt AID.txt 2>/dev/null | head -20",
 "description": "Grep madgu and myna"
}
```


### [2026-09-07T01:38:30.687Z] TOOL RESULT

```
Exit code 1
ARP.txt:1717:mani  80. mati  96. matsya  59. math  68. mad  42. mada  42. madgu  58. madhu  81. madhya  63.  65. man  96. manas  96, manu  276  fg. m antra  230. mastu  68. raahimagha  231. mätar  84. mätula  86. mäyä  96.  231. mäsha  45.  59. mäs,  mäsa  98. mitra  178  fg. mithradruh  217. mithas  93. miyedha  67.  82. mishta  67. mushiti  64.  65. mürdhaja  61. müsh  53.  235. müshä  53. müshi  53. mriga  57. medh  96  . medhas  96. medhä  96. medhira  96. mesha  50.  59. mainäka  111. mlecchabhojana  43. yakrit  65. yakshman  97. yaj  228. ya^ata  179.  225. yajüa  228, yajüya  228. yam  84. yama  243  fg. yava  43. yavasa  44. yavyä  28. yavyAfVati  107. yatar  88. yatumant  218. yamätar  87.
HJB.txt:15408:1548.— "With  these  four  captains  there are  12  naiques,  who  receive  as  follows — to wit,  for  7  naiqUM  who  have  37  pcuxlaos and^  1  tanga  a  year  .  .  .  11,160  reis.  For Cidi  naique,  who  has  30  pardaos,  4  tangas .  .  .  and  Madguar  naique  the  same  .  .  . and  Siilgy  naique  24  pardaos  a  year,  and two  Tia/arei  [Ar.  nc^r,  *  servant']  who  have 8  vintens  a  month,  equal  to  12  pardaos  4 tangas  a  year."— <S.  Botdho,  Tombo,  215.
POK_full.txt:57052:mad- {madaite, madayaijha) " become intoxicated, get amused '; Old Indie madgu-^ a 
LEW_1910.txt:1055:madgu-, madgura-h IME
HUB.txt:7170:Wasservogel*, skr. madgu-, ap. *maJyw-?; «?ifm 'Nest* =
HUB.txt:8851:Np. may ein Wasservogel* = skr. madgu- kann auf
POK_02.txt:5647:Ai.  mddati,  mddate  ,wallen,  sprudeln,  fröhlich  sein',  mädyati,  mamdtti, mdndati  ds.,  mdda-  m.  ,Rauschtrank'  =  av.  maSa-  , Rauschtrank,  Rausch- begeisterung', ai.  mattd-  ,trunken,  freudig,  erregt',  av.  mad-  {maöaitlj madayaTdha)  ,sich  berauschen,  sich  ergötzen  an' ;  ai.  madgu-  ,ein  bestimmter Wasservogel,  ein  Fisch'  =  np.  mäy  ,ein  Wasservogel',  ai.  mdtsya-  m.,  av. masya  ,Fisch'  (,der  nasse' ;  Ableitung  von  einem  -es-St.  *mades-) ;  ai.  medas- n.  ,Fett',  medana-  n.  ,Mästung',  mBdyati^  midate  ,wird  fett',  medya-  ,fett' (meda-  aus  *mazda-,  idg.  *mad-do-  oder  *mad[e\z-do-  und  =  ahd.  mast ,Mästung';  die  spez.  Bed.  ,Mästung'  also  in  dieser  Bildung  bereits  idg.); mdstu-  n.  ,saurer  Rahm'  (^mad-stu-),  npers.  maskah  ,frische  Butter' (*mad-sk-?)-  ai.  mddya-,  madird-  ,berauschend';
IEC.txt:10687:mesgus, os ‘diving bird’. Cf. mesgó (2). (mezg-) Skt. madgub, m.id.; Lat. mergus, m., LLat. mergulus ‘cormorant’. (For Lat. mergus (2) *vine-tendril for propagation' cf. mesgo (1))
(eval):1: === not found
```


## [2026-09-07T01:38:42.499Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7160,7175p' HUB.txt; echo ====; sed -n '8840,8860p' HUB.txt",
 "description": "Hübschmann māγ context"
}
```


### [2026-09-07T01:38:42.549Z] TOOL RESULT

```
Exit code 1
Das Pehlevi der Biicher unterscheidet ?, y und d nicht,
wohl aber h und y = d, Es hat h und wohl auch y fiir
altes J. Ebenso das Pazend bei richtiger Lesung.
Die Syrer haben d (J) in alten LW. (vgl. NTIT *lorica*
= zd. zrdSa-), in jiingeren y (NJ^5 = skr. padikor-). Aus
jenen ist d auch ins Arabische eingedrungen, vgl. zarad
*Kettenpanzer' = syr. NHIT, zd. zrada--^ xudat, pi. xuvad
*Helm* = syr. NTIH 'diadema', Brockelmann p. 105, arm.
xoir, ap. xaxiSa-.
§ 94. Ap. d vor y, m, n ist geschwunden: may ein
Wasservogel*, skr. madgu-, ap. *maJyw-?; «?ifm 'Nest* =
ap. *tiistdman'? (oben p. 101); siJcanam *zerbreche' = ar.
^skadnami, siehe Kap. 27.
Ap. anlaut. dv = d, dialekt. b siehe § 57, c.
Ap. zd = idg. zd^ zdh (= 5, ^, d, rfA + ^» ^A) =
np. zdf siehe § 91, b.
(eval):1: === not found
```


## [2026-09-07T01:38:44.100Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"malax\\|malaḫ\\|malach\\|Heuschrecke\" HRN.txt HUB.txt BRT.txt PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt 2>/dev/null | head -30",
 "description": "Grep grasshopper words"
}
```


### [2026-09-07T01:38:44.157Z] TOOL RESULT

```
HUB.txt:7081:*muda' ? ; sSi 'Gatte = ap. *xSauSa- ? ; maig *Heuschrecke
HUB.txt:7082:(neben malax) = phi. maig (und malak Bdh. 47, 10), bal.
HUB.txt:7127:auf *JtfilJ == ap. Mdda-; niarax 'Heuschrecke' auf *madax
HUB.txt:7180:Fiir altes J erscheint ausnahmsweise I in malax *Heu-
HUB.txt:9466:/ aus d in malax 'Heuschrecke* Fird. I, 252, 148 = zd.
HRN.txt:8611:niele% 'Heuschrecke' (Öähn. I, 188 Vers 1059) s. meig
HRN.txt:8787:1010. vfieig 'Heuschrecke, ^''^D (Is. 33, 4).
HRN.txt:8788:aw. madaxa- 'Heuschrecke' (D armestet er, Et. ir.
HRN.txt:8792:kurd. mala (H.-Sch.), wa;^'- wila/, sar. malax sind
HRN.txt:8810:') Falsch statt malax-
HRN.txt:14368:kamalaxiaiu 877, 2(X>.
HRN.txt:21678:s. malax lOlO.
NYB_vol2_glossary.txt:3599:šāk [š*k'] branch 3118; pl. cas. obl. šākān (or šārān) [š*hn'] 40%, — NP sax; an alternation -k: -x, -h is found in several ws: BP sūlāk (q.v.): NP siuldr; BP malak (FrP 8): NP malax ‘locust’; Av. (1114) maóaxa-, Arm. lw. marax id.: NP maig < *maóaka-; BP zanak (q. v.): NP zanax. — Bal šah ‘horn’. (Not identical with Skr säkhä).
NYB_vol2_glossary.txt:7256:malax: Sak malidan: malitan mana: mānākēh mānistan: mānākēh māndagī: māndakēh mary: *murv marzbàn: marz-pàn mäyah: mātakēh mazah: micak
BRT.txt:10881:•  j.  "xSt^mla^i-a  malaxaheca  [tan]"  V. /.14  Gl.
BRT.txt:19409:—  imaiy  matiiyä  hamataxsa'iä  anuHyä mann  BIL4.1S.  zu  b);  a)  der  Gen. steht  für  den  Dat.:  adamsam  *paHy- axsayaiy  manä  bäßm  abara'  "ich  führte die  Herrschaft  Über  sie,  sie  brachten mir  Tribut"  D.  6'.  2;  —  dahyavt^  .  . lyä  kalamel^  atars^  manä  baßm  abar^ D.j.a;  Bh.i.  7.  ß)  der  Gen.  ist  possessiv: 8  manä  taumäya  .  .  xfäya%iyä  aAc^  Bh. /.  4;  —  äadaHii  näme^  pärs(^  manä ba'dakJ'  Bh.  j,  3;  6,  9,  14,  2. 6,  7,  10,  14, 5.1;  —  viitäsm'  manä  pitä  ^h.i.ib; — Pasävn^dis  ^urc^mazdä  mana  dastaya akunaus  Bh.  4.^;  —  ^**  Aamalaxlatä manä  vi^iyä  Bh..^  13.  b)  nur  u)  im jAiw.;  der  Gen.  ist  possessiv;  zui):  variöa- yofJuAa  mana  vaca  Y. /O.  5*>;  V. /(>.  8, 9;  —  nSil  mana  xiaäire  bval  .  .  V. 2.5.  zu  3):  0ia  asti  voAu  manS mana äami  Yt /.  35;  25*.  5)  Gen.-Dat; zur  Wiedergabe  des  Gen.  s.  bei  4;  a)  im Ap.;  zu  a  1):  tyj'maiy  pih''(^  iartam X.  I-  4;  3.  3;  —  Uta  tyi^maiy  kartam X.  3.  3,  3.  3,  4~  3;  2.  3;  —  hauvmaiy hamiä^iy^  abav<^  Bh.2.  i4;_5.'3;  —  ait<r- maiy  akurJ'matdä  dadatuv  D.  ^.  5;4>3;
BRT.txt:19588:•  j.  tnaSaxa-  m.,  'xä-  f.  Ileuschrecke', ein  i/dA^sches  Tier:  ti  sUnS  'xaySsia aogasdast>ma  bavainti  "die  verleihen  der Spinne  und  der  Heuschrecke  am  meisten
BRT.txt:26438:•  j.  skatay-  f.  'Heuschrecke"  (?) ",  als  Land- plage von  Gava  (Sogdiane):  gilum  yim suyös.sayanfm  aal  ahe  paityär^m  fräkiryii- tat  anrö  mainyus  .  .  'ilim  yqm  gavaca daya(sd.)ca  pouru.mahrk>m  V.  r.  4,
BRT.txt:26439:Der  Text  ist  inkorrekt  und  inhaltlich  unklar.  — Pu. :  knrkn  maW  ('Heuschrecke')  i  gSspan- dän  dadtrii  i pur  mark;  erl.:  ma\ak  ape  äyil iiirläk  -  ku  ape  vSitr  apt  äyil  —  gäv  baslan HC  säytt  gäspandma  mariih  bavel.  AuchOrBd. (s.DST.ZA.2.8)  bietet  'Heuschrecke'  -  kmca; s.  PPGI.  ff.  3  -  für  skailJm.  —  0  So  nach der  Tradition;  s.  oben.  Anders  FkMOllek WZKM.  3.  366,  6.  183.
```


## [2026-09-07T01:38:55.070Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8780,8815p' HRN.txt; echo === 8605; sed -n '8600,8615p' HRN.txt",
 "description": "Horn 1010 meig"
}
```


### [2026-09-07T01:38:55.120Z] TOOL RESULT

```
Exit code 1
meghä-; arm. m^g 'Nebel* (H. No. 197).
oss. d. meyä, t. 7nty *Nebel, Wolke' (185).
Dass mey mit l^meig^h- 'harnen' (1006) zusammen
gehört, scheint sicher zu sein, vergl. zuletzt Bechtel,
Hauptprobleme S. 373.
') Das l Hesse sich allerdings als Ablaut erklären.
') Seifenkraut; Ochsenurin.— 227 —
1010. vfieig 'Heuschrecke, ^''^D (Is. 33, 4).
aw. madaxa- 'Heuschrecke' (D armestet er, Et. ir.
n, 197); phlv. waig (kaum madag),
bei. madag, n. mada/, maöay (221).
Np. melex, phlv.-päz. tnalak ^) (PPGl.), arm. mara/,
kurd. mala (H.-Sch.), wa;^'- wila/, sar. malax sind
LW. (als Entlehnungsgebiet bleibt allerdings nur das
Afghanische [mlax) übrig) oder setzen eine arische
Dialektspaltung voraus ; g. watah und oss. mäfix sind
wohl erst sekundär (an ein phlv. *mata/, wie von
Stackeiberg, ZDMG. 43, 672 es zu tun scheint,
glaube ich nicht).
1011. niTnö {*menö) Himmel, Paradies; Smaragd', vergl.
mlfiä Emair^).
aw. mainyava- geistig, himmlisch' (NB. heisst
aw. mainyU' nie 'Himmel'); aw. menö^^) 'Geist;
Himmel'.
1012. niehen 'Haus'.
aw. maedana- 'Wohnung; phlv. mShan, vergl.
Artaky§]midan, Stadt in Chorasmien (Yäqüt), Xas-
mi&an^) ib., KvS\mthan, ib. (Nöldeke, ZDMG. 33,
153, de Lagarde, Purim 40, Note 2) 5).
bei. metag 'Haus, Wohnung' (241).
') Falsch statt malax-
2) Np. mwö *Smaragd', minä *Emair (kurd. LW. mtnä)^ *hiinmel-
blau' gehören nicht zu aw. mimt' 'Geschmeide' (yt. 5, 127), wie Geld-
ner, KZ. 24, 400 Note 7 nach de Lagarde's Vorgang (Beiträge zur
altb. Lexicographie 47) annimmt.
^) So lese ich mit Dr. Andreas; Fr. Mülle r's minölg hhrat
(eval):1: == not found
```


## [2026-09-07T01:38:58.072Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"\\[pdf page\" HRN.txt | head -3; echo ===; grep -c \"\" HRN.txt; echo === formfeeds; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# find which page contains line with '1010. '\nfor i,p in enumerate(pages):\n    if 'Heuschrecke' in p and 'meig' in p:\n        print('leaf',i+1,'printed',i+1-21)\nEOF",
 "description": "Locate Horn page"
}
```


### [2026-09-07T01:38:59.206Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-07T01:39:14.469Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -- \"— 22[12] —\\|— 21[45] —\" HRN.txt | head",
 "description": "Find Horn printed page markers"
}
```


### [2026-09-07T01:39:14.535Z] TOOL RESULT

```
8297:*J Wohl *müdkiyän^ vergl. kurd. mük.— 214 —
8563:auch muybece^ muyän u. a. m.— 221 —
```


## [2026-09-07T01:39:19.172Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8563,8600p' HRN.txt",
 "description": "Horn p222 region"
}
```


### [2026-09-07T01:39:19.217Z] TOOL RESULT

```
auch muybece^ muyän u. a. m.— 221 —
Ved. Stud. II, 19); phlv. magu, magupat (arm. LW.
mog^ mogpet, movpetan movpet), daneben maupat (syr.
LW. NtOSID, daraus gr. Mavlnväg d. i. Mavmxäg und
Mavinvüv&d d. i. Mavmvovx^ä, Nöldeke, Karnämak
59 Note 4); ar. LW. majüs (Plur.).
985. mey 'Tiefe, Fluss''), meyak 'Graben, Grube* (Sahn. I,
174 Vers 817).
aw. maya- 'Loch'; phlv. may,
986. meyz 'Gehirn*.
Kä§. magz, magzL
aw. mazga- 'Gehirn'; phlv. mazg; ai. majjdn- 'Mark*.
af;'. mayz, Plur. mayza 'Gehirn'; oss. (LW.?) mayz
(174); bei. mazg (229); sar. muig 'Knochenmark', da-
gegen sar. moyz, siyn. mayz 'Gehirn' wohl LW.
987. unuft unbedeutend, umsonst erhalten'.
ai. l/'möC' ^befreien, wegwerfen* (also mtikta- etwas
Weggeworfenes', wie np. Juft aus yuktd-), Darme-
steter, Et. ir. I, 88 Note 2.
Die entlehnten nslov. muhte 'sorglos', serb. mukte,
muktice 'umsonst', ^wwiton^i 'schmarotzen' (Miklosich,
SWAW. Band 35, 129; 37, 86; 38, 176) würden die
ursprüngliche Form dann nachträglich wieder ent-
wickelt haben.
Unsicher.
988. meger 'wenn nicht, ausser, vielleicht'.
me nicht' + eger (No. 106), päz. ma agar (Aog.).
989. meges 'Fliege', jüd.-pers. Mo (Is. 7, 18)«).
aw. vergl. ma/si- 'Fliege, Mücke' ; phlv. magas (vd. 1
^) Den aus dem F§ bei Vullers abgedruckten Sahnämevers
konnte mir Herr Dr. Landauer nicht nachweisen.
') Z statt 8 findet sich dialektisch häufig: z. B. besbäs (AM. 55),
bezhäz oder semärüy, zemärüy oder kusbura^ kuzbura(YvL\\eT8); sepes
(jüd.-pers.) statt zi pes, vergl. si pester (Vullers); Käs. üzü d. i. an
8än; kauk.-bergjüd. zürnai sonst sürnm u. v. a. m. Umgekehrt steht
8 für z im ar. LW. sauswjird *ein Tuch', wörtlich *nadelgefertigt*
(sözengird), de Goeje, Bibl. geogr. arab. IV, 266. Ebenso wechseln
z und s, z. B. /äksi^ -/äkkl (Vullers, vergl. auch ebenda s. v. j^vhe und— 222 ~
```


## [2026-09-07T01:39:20.326Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"mast '\\|mast \\x27\\|mäst\\|mäsldan\\|masidan\\|Dickmilch\" HRN.txt | head -20",
 "description": "Horn mast/māst"
}
```


### [2026-09-07T01:39:20.374Z] TOOL RESULT

```
1386:aw. hqm -\- l^par-^ hampäfraiti 'er mästet*; phlv.
8087:vi- r smav' 'vergessen' ; phlv. gumästan, gumür.
8298:959. mäst saure Milch*, mäsiden gerinnen*.
```


## [2026-09-07T01:39:32.148Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8298,8320p' HRN.txt; echo \"=== mahi\"; grep -n \"mähi\\|mahi 'Fisch\\|Fisch'\" HRN.txt | head -20",
 "description": "Horn 959 māst and māhī"
}
```


### [2026-09-07T01:39:32.209Z] TOOL RESULT

```
959. mäst saure Milch*, mäsiden gerinnen*.
skr. mdstU' 'saurer Rahm*.
arm. macum saure Milch', macanhn 'ankleben (intr.),
anhangen, gerinnen* (Hübschmann, No. 184), sowie
bei. maiay, pp. masfa *to freeze, curdle', mastay curds
(Dames), die Hübschmann ZDM6. 44, 561 ver-
gleicht, stimmen lautlich nicht genau.
960. mäS 'Erbse, Wicke'.
ai. mäsa- 'Bohne'; sar. ma/ Erbse*.
Kann im Indischen oder Iranischen (doch eher in
ersterem) Lehnwort sein.
961. fnäy 'Wasservogel' (Öähn. I, 444 Vers 191).
ai. madgü' , 'ein Wasservogel* (Hübschmann,
ZDMG. 38, 423).
962. mäliden 'reiben, glätten*, -mal (vergl. destmäV)
'Handtuch*); vergl. musten (No. 983).
aw. [/^marz-, marezaiti 'fegt*; phlv. ktin\marz,
dastän[marz, dösak[marz vd. 1 (18), marz(i)sn, 'Coitus*
(Bund.) 2), marzUan 'coitiren*, mälUan, mCU(i)8n; ai.
I/"7war/-, märsti 'abwischen*.
kurd. LW. malin 'fegen*; bei. LW, malay, malBnay (223)
reiben, mischen, streichen'; oss. märzin 'fegen* (180).
Vergl. Hübschmann, ZDMG. 44, 558; phlv. -marz
=== mahi
8402:969. mahl 'Fisch'.
8405:aw. masya- 'Fisch'; phlv. mählk; ai. mätsya- 'Fisch*.
20532:n. mähiy 969.
```


## [2026-09-07T01:39:42.634Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8400,8412p' HRN.txt; echo \"=== SYN fish\"; grep -n \"3.65\\|‘fish’\\|matsya\" SYN.txt | sed -n 1,20p",
 "description": "Horn mahi + Buck fish"
}
```


### [2026-09-07T01:39:42.707Z] TOOL RESULT

```
Daneben erscheint auch eine Form mit Nasal: np.
mäng 'Mond', g. mäm, kauk.-bergjüd. meng,
969. mahl 'Fisch'.
g. müsü (d. i. mäsü), vergl. mäs mäht (AM. 24
Zeile 4).
aw. masya- 'Fisch'; phlv. mählk; ai. mätsya- 'Fisch*.
I) In Yls und Bämln kann man manchmal auf einer Seite die
vier Bedeutungen : 'Mond, Monat, Mondgesicht, Medien' lesen.
Ar. mäSiy 'weisser Honig', moMyat 'glatter Panzer; "Wein* (dazu
wohl auch mär^ *good natured, gay, jovial* bei Johnson) erklärt
Nöldeke bei Weber, Monatsber. BAW. 1879 S. 812 als 'raedisch*;
daraus sind entlehnt skr. ntädhi', mafhi- 'Ringelpanzor*.— 217 —
kurd. mOsT Tisch*; LW. bei. muhi, n. mdhhj, mahty
=== SYN fish
3768:Y A few were first applied to the meat of an animal as food and then to the liy- ing animal (the opposite of the usual re- lation, cf. 5.62), as NG Wap ‘fish’ (3.65), ON saudr ‘sheep’ (3.25).
4756:NE fowl, orig. ‘bird’ (3.65), now most- ly for domestic birds, esp. ‘cock’ or ‘hen’, but in US., at least, includes ducks, geese, etc.
4919:184 3.65 FISH
4920:f ii Goth. fisks Lith.  Zuvis eee ON | jiskr Lett. zivs Lat. piscis Dan. fisk ChSl. ryba It. —_-pesce Sw. _fisk SCr. riba Fy. poisson OE fisc Boh. ryba Sp pez ME fisch Pol. = ryba Rum. peste NE fish Russ. ryba Ir. tase u.  —-visch Skt.  matsya- Nir.  iasg OHG  fisc Av. —_masya- W. pysgodyn MHG visch Br. pesk NHG fisch
4925:dyor ‘dainty’, at Athens especially ‘fish food’ (cf. dpwy movriwy Tur.). édvdpiov for ‘fish’ as food in NT in Jn. (6.9, 11; 21.9, 10, 13; but txts for fish in the sea 21.6, 9, 11; in the other gospels only xis in both senses) and often in the pap. The definite extension to the living fish is later.
4927:5. Skt. matsya-, Av. masya-, fr. an TE *mad- ‘be wet’ in Grk. paddw, Lat. madére, etc.? Walde-P. 2.230.
4935:Ir. tascach Du. _—visscher Skt.  kaivarta-, dhivara-, Nir. iascaire OHG fiscari matsyajivat-, etc. W. pysgolwr MHG vischere
4937:Nearly all the words for ‘fisherman’ are derivatives of the words for ‘fish’ (2.65) through the corresponding verbs, or in some cases compounds, like NE fisherman which has displaced fisher in current use, Russ. rybolov ‘fish-catcher’.
4941:Grk. adtebs, fr. ads ‘sea’ and in Homer also ‘sailor’. But NG pop. apis ‘fisher- man’ and ‘fishmonger’, fr. Wapu ‘fish’.
4942:Skt., beside occasional matsya-jivat- lit. ‘one who makes a living from fish’, matsya-bandha- (bandh- ‘bind, catch’), and mdtsyika- (Pan.), more commonly kaivaria-, prob. orig. a term of oppro- brium (ef. kev- ‘serve’ Dhatup.), and dhivara-, prob. : dhivan- ‘skilful’.
5080:idim (also ‘fish’), epd. of Pedersen 2.492. NIr. fadhachawm, fiadhuighim, fr. ie
5275:There are a few instances (some of the words for ‘liver’, 4.45) in which the name of the organ was originally one applied to it only as an article of food, parallel to the case of ‘fish’ as an animal from ‘fish food’ (NG api, 3.65).
14517:Studi baltici 3.65 ff. Trautmann 31.
15211:of ‘hollow or curved +i ed tile’. ‘ Neugr. Stud. 3.65, Cans
24108:For other words formerly used in such phrases, as Fr. voie, coup, bout, etc., cf, Meyer-Liibke, Rom. Gram. 3.65. Tob- ler, Verm. Beitr. 183 ff.
24155:NE threefold, OHG drifalt, MHG dri. vali(ec), NHG dreifaltig, Du. drievoudig, 2. A recurring phenomenon is the use of words for ‘twofold, double’ to indicate any degree of multiplication, that is simply ‘fold’. Thus NG pop. rpl-5umdos ‘threefold’, rerpa-durdos ‘fourfold’, ete, Lat. duplus must have come to be used the same way in VLat., as indicated by phrases like It. a tre doppj ‘threefold’, etc. (numerous quots. in Voc, degli Accad. della Crusca 863), OFr. a cent doubles ‘hundred fold’, Sp. al tres doble ‘threefold’, etc. Cf. Meyer-Liibke, Rom, Gram. 3.65, Tobler, Verm. Beitr, 1.148 ff. The idiom, as well as the word passed into the Celtic and Gme. lan- guages. Ir. cdic-diabuil ‘fivefold’ (K. Meyer, Contrib. 412), W. tridyblyg ‘three-fold’ (dyblyg fr. Lat. duplicem; Loth, Mots lat. 162), Du. driedubbel, Dan. tredobbelt, Sw. tredubbel, NHG drei(ge)doppelt (poet. or dial.), NE three- double (NED quots. fr. 16th, 17th cent.; said to be still in use locally in U.S.).
24161:4. In the Romance languages (be- side forms cited above, 1 and 2) the proportional sense is commonly ex- pressed by phrases like It. tre volte tanto, Fr. trois fois autant, formerly also It. tre tante, Fr. trois tanz, as still Sp. tres tanto. Meyer-Liibke, Rom. Gram. 3.65.
```


## [2026-09-07T01:39:43.398Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"maγ\\|mag '\\|magak\\|hole\" MPP.txt | head -20",
 "description": "Henning MPP maγ"
}
```


### [2026-09-07T01:39:43.446Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T01:39:50.239Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l MPP.txt; head -20 MPP.txt; echo ===; grep -n \"mag\\|maγ\\|may\" MPP.txt | head -20",
 "description": "Inspect MPP"
}
```


### [2026-09-07T01:39:50.291Z] TOOL RESULT

```
Exit code 1
7737 MPP.txt
HANDBUCH DER ORIENTALISTIK
Herausgegeben von B. Spuler unter Mitarbeid von H. Franke, J. Gonda
H. Hammitzsch, H Kees und J. E. van Lohuizen-de Lee uw
ERSTE ABTEILUNG
DER NAHE UND DER MITTLERE OSTEN
HERAUSGEGEBEN VON B. SPULER UND H. KEES
VIERTER BAND
c
IRANISTIK
ERSTER ABSCHNITT
LINGUISTIK
MIT BEITRÄGEN VON
KARL HOFFMANN . W. B. HENNING
H. W. BAILEY • G. MORGENSTIERNE • W. LENTZ
E. J. BRILL
LEIDEN — KÖLN
1958HANDBUCH DER ORIENTALISTIK
HERAUSGEGEBEN VON BERTOLD SPULER
unter Mitarbeit von: H. Franke, J. Gonda,
H. Hammitzsch, H. Kees und E. J. van Lohuizen-de Leeuw
(eval):1: == not found
```


## [2026-09-07T01:40:01.518Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"maγ\\|mayg\\|malax\\|mast\\b\" MPP.txt | head -20; echo \"--- pages\"; python3 -c \"\nt=open('MPP.txt',encoding='utf-8',errors='replace').read(); p=t.split(chr(12)); print(len(p))\n\"",
 "description": "MPP grep"
}
```


### [2026-09-07T01:40:02.741Z] TOOL RESULT

```
6360:mast-i mast 211
6361:mast-i mast-än 211
--- pages
140
```


## [2026-09-07T01:40:07.663Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json; d=json.load(open('data/verification/sources/refs_online.json'));\nprint(json.dumps(d['MPP'],ensure_ascii=False,indent=1)); print(json.dumps(d['FRS'],ensure_ascii=False,indent=1)); print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"",
 "description": "Full refs entries MPP FRS BQT"
}
```


### [2026-09-07T01:40:08.911Z] TOOL RESULT

```
{
 "title": "W. B. Henning, \"A List of Middle-Persian and Parthian Words\", Bulletin of the School of Oriental Studies IX (1937–39), pp. 79–92",
 "edition_found": "1958",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/henning-1958-mitteliranisch",
 "identifier": "henning-1958-mitteliranisch",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/MPP.txt",
 "page_offset": "leaf = printed - 14 (e.g. leaf 7 = p.21). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's Table IV entry for MPP is garbled in the OCR (reads like a Persian title, 'Honari darbareh Zaban Farsi ... 1961'); Table III credits MPP to Henning, so this is most likely 'Mitteliranisch'. Treat identification as tentative and verify that cited page numbers fall in 20-130.",
 "notes": "CORRECTED 2026-09-05: Nourai's Table IV no. 66 identifies MPP as Henning's BSOS IX word-list (pp. 79–92), not \"Mitteliranisch\". The local file labelled MPP.txt is Mitteliranisch and does NOT contain the cited material; MPP:79 is simply the article's first page. The article itself is not on disk (JSTOR/Cambridge Core).",
 "cites": "page number of Henning's BSOS IX (1937–39) article, pp. 79–92"
}
{
 "title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')",
 "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt"
 ],
 "page_offset": "different edition — no mapping",
 "covers_etymology": false,
 "notes": "Persian OCR fair. Ganjoor does not host Loghat-e Fors."
}
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
```


## [2026-09-07T01:40:13.783Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; for p in 24 44 90 104 114; do echo \"##### pdf page $p (printed $((p+1917)))\"; awk -v n=$p 'BEGIN{RS=\"\\f\"} NR==n' BQT_v4_pages.txt | head -60; done",
 "description": "Print BQT v4 cited pages"
}
```


### [2026-09-07T01:40:14.979Z] TOOL RESULT

```
##### pdf page 24 (printed 1941)
[pdf page 24]
-۱۹۸۱- 1 ماست
مرکب همست ۱ - و بمعنی‌مازن هم‌آمده‌است نسخه بحذف دال‌آخر نوشته شده بود که مازمدر
که(۱) استخوان میان پشت باشد که عربان‌صلب | باشده ال اعلم .
خوانند ۴ - و مالةٌ برزیگران را نیز گفته اند مازیاده « بر وزن آشکاره . نوعی
وآن تخته‌ای باشد که بر روی زمین شیار کرده از خوردنی و طمام باشد و معرب آن مازیارج
بکشند تا کلوخهای آن بشکند و زمین هموار | است . ۰
شود ۳ ۰ ۹ مازینه بروزن آدینه » نام زنی‌است

ماژ ومولٌ ؟- با دو زای فارسی‌ومیم که باتفاق مردی مازنین نام همارت اسنگويةٌ

بروزن‌ساز وسوز » این لغفت از توابع است‌بمعنی | هندوستان را ساجت ۸ .
فی‌بادی باشد که موش در وقتی که گربه را بیند ماس - بروزن طای » مخق فآمای‌است
با ماری قصد کرفتن اوکرده باش دکند - که ورم باشد ‎٩‏ - و بزبان هندی آماه راگویند

مازون * - بر وزن هامون . مازو دا | ک» عربان قمرخوانند*۱- و الماس رالیز گفته‌اند
گوبند و آن چیزی باشد که پوست را بدان | اوآن جوهریست معروف؛ و بعتی گفته‌اند بمعتی
دباغت کنند وزنان هم کاهی بجهت تنگی موضع | المای عربی است ۱۹
مخصوص بکار برند - ماسای - مخقف میاسای باشد () که

مازه ‎٩‏ < بروزن غازه » استخوان میان | منم ازآسوده بودن باشد بعنی آسوده مباشی۱۳.
پشت راکوبند که عربان صلب خوانند ؛ و بعضی ماست - بروزن راست » معروف است
ناوبرا آنه در میان پشغت افت دگوبند . که جغرات‌باشد؛ وبعی‌جغرات‌چکیده‌را؛ وبعتی

مازه درد ۷ - درد پشت راکویند . | دیگر مایه ای که بر شپرزند ماست گویند ۱۴
چه مازه استخوان پشت است؛ وباین‌معنی درچند | و علك رومی‌را نیز ماست میگوبن دکه مصطکی

() چش : و - () چش : است . :

۱ سماز. (ه.م.) ۳ مازون . مازو (در کیلان و مازسران : بلند مازو) ۳ 0670108
18 درلرستان مازو » ببلوط 067812 067015) اطلاق شود « ثابتی 4۲۱۳
طبری 13021 ( بلوط ) « واژه نامه ۷۳۵ > رل : تحفة حکیم موّمن « مازو > و ار : فرهنگه
روستائی ص ۹4۱ .۰ ۴ «<مازن * مازه . ۴ - ر4 : رشیدی .

۴ - ام سوت . مازو (ه.م.) < ماز . ۹ مازو* مازن (هم.)
رك : مازه درد . ۷ - رد : مازه . ۸ - رك : مازنین -

. ‏رك : آمای . ۴ رد4 : ماه . ۹۱ رك : المای‎ - ٩

۴۳ رك : آسودن . ۴ ساننکربت -132511 ( سرشیر حامض ) ۰ ارمنی
0 ( غیرترش ) , 13862711 (چبانیدن, بتن . منجمد شدن )» بلوچی(32800881.
48 (بتن » منجید شدن ) , 13881880 (ماست ) ۸« اسشق ۹۵۹ * » افغانی 122918
( شیر دلمه شده ) «کردی 13224 ( شیر.دلمه ) « خوبشمان ۹۵۹ ۰ ایا کردی 13881 (شیر
بته ) « ژابا ۳۸۹ ؛گیلکی ۰ برنی و نطنزی 33251 » فریزندی 77228 9 4. ۱ ۰۳۲۹۱
سمنای 13281 , ساگسری 13)(081 ۰ سرخه‌یی , لاسگردی و شهمیرزادی 32281 49 .۰ ۲
س ۱۹۰ بعی پنداشته‌اند که ماست عربی‌است و از « ماس » مأخون است . در قاموس آهده :
« ماأست‌الناقة ‏ یعنی سخت شد بشترگردآمدن شیر درپستان او» این معنی‌ریطی‌به «ماست» فارمی
ندارد , و باید دانست که ۶ ماست» بقیه در حاشیهٌ صفحهةٌ ۱۹۶۴

##### pdf page 44 (printed 1961)
[pdf page 44]
-۱۹۹۱- ماهیان
ولیم اس ت که نود وشش حبه باشد ۱ .48 آورند وماهیابه را ازآن سازند و معنی ترکیبی
ماهیابه ۲ - با ستابی بالف کنید. | آن ماهی نارس باشد چه اشنه بممتی ناری‌آمده
وفتح بای ابجد » خوردنیی باشد که درلاروشیراز | است. .
ازماهی اشنه سازند وآنرا بعربی صحنات کویند. ماهیان - بر وزن ماکیان » جمع
گرم وخشك است در دویم . ماهی است که حوت باشد - و جمع ماه همست
ماهی اشنه - بفتح همزه . نوعی از بر خلاف قیای همچو سالیان که جمع سال
ماهی باشد یار كوچك و آنرا از جالب هرموز | است ۴ .
۱ - بان معنی * ماشه (ه.م.) * ماهچه (ه.م.)
کر پذبرد زبیق ز صفر هم غلی ز مس دوازده ماهه عیار بگشاید .
مقبث هانوی « جهانگیری ».

۴ *مهیابه (مغفف) * ماهیاوه < مهیاوه ( مشفف ) (ه.م.)

۴ - ر4 : قاعده های جمع بقلم نگارنده ۰۲۵-۲4

2 ماهی - اوستا -۳3388[8 (ماهی) » پهلوی 178111 . هندی باستان - 171418[/8
(ماهی) ۰ کردی 7291 ۰ بلوچیع 81 , ۳۳2018 ۰ 80طظ8 ۰ افنانی 138881 «اسشق
۵۹ لری ۲081 . زازا اقق۳۳ , کیلکی 13۵۳1 , مازسرانی و طالغی ۰172۵1 کبری

۱ ۰
ی ۴ 1 قاهد ی چسیم پ ۹
7 ۷۷۱۳۸ 2 سح ۴۳
ار
۱
جک ۲ کمن
۹ هر ی 27 و ۲۳۳۹و
جر ۳ رن 8 1 0
رنه ره ! ی و .جج<سته
0 ریت تک کچ
زد ه 1 ی
ملس 9 1 : هه
ای ی هم باه ری
ها ی سک هی دض ۱ ش
انواع ماهی
40 : ژابا ص ۳۸۹ ۰۶ اورامانی (13389)2۷:1 « 4 . اورامان ۱۲۸ » ؛ جانورانی ذی‌فقا رکه
درآب زیت کنند. شکل ماهیان غالباً دو کی است وازاین جهت برای حر کت درآب‌کاملامتناب
است . بدن‌آنها از پولکهای كوچك متور است . انواع ماهی بسیار است .

##### pdf page 90 (printed 2007)
[pdf page 90]
-۰۰۷- متمند
دیگه و طبق و غیره از آن سازد ‎٩‏ ۰ و ارباب | هم هست او درست است چه درفارسی سین واشین
سنمت که کیمیا کران باشند آن را طلاکنند. ‏ ۱ بهم تبدیل می‌باید چنانکه در فواید کفته شد۷ .
مسافران والا - یکی نون . اشاره هستیند » بر وزن متمند » شخصی را
باولیاال و سالکان وطالبان دین حق است ۳ . کوبن د که کرفتار محنت و راج وغم باشد ۸ -
هس بند - بنتح اول بروزن پی بند ,| و بمعنی مس‌بند هم بنظر آمده است اوآ نکسی
شخصی راکوبند که پای بند کی پا چیزی شده | باشدکه پای بند چیزی شده باشد وشواند بجایی
باشد که بواسطةٌ آنکس یاآن چیز بجابی تواند | ارفت ‎٩‏ -
رفت ؛ و بم اول هم باین هعنی آمده است۴ . محقّرو « با رای قرشت بروزن لبلیو ,
همست - بنم اول وسکون ثانی وفوقانی, | بمعنی خامالا است که نوعی‌از ماذربون باشد ویر
کله و شکوه و شکایت باشد ۴ - و بیخ کیاهی | برص وبهق طلاکنندنافع باشد. وبا عل‌پربشهای
هم هت خوشبو ی که بعربی سعد کوبند و تشم | خعك مالند سودمند بود -
آبرا نودری خوانند ۴ - و بمعنی غم واندوه نیز مستمنف *۱- بنم اول‌وفتح میم» بمعنی
آمده است وازین است که غمگین واندوهناك را صاحب غم و رنج و محنت واندوه باشد چه مت
متمند میگوبند ۴ . ‎٩‏ بمعنی غم و اندوه و هند بمعنی صاحب وخداوند
مستال - بر وزن دستار »نام گیاهی | باشد و او را غمگین و اندوهناك هم میگویند -
است دوائی و بوی خوشی دارد و در غابت تلخی | و محتاج ونیازمند - و کله‌مند وشکوه‌ناك را نیز
هم هست وآنرا مرو نی زکوبند؛ وباشین نقطه‌دار | گفته اند .

۹ - کردی ه[1327 ( مس ) « ژابا س ۳۹۳ 8لا32 ( مس ) » مازدرانی 118 ۰
5 کیلکی 831۳8 « ژابا س ۳۹۸ * فلزی برنگك سرخ اسمر ( آنگاه که خالس باشد) <
نحای (عر) ۳ 2۷1۷۳6 (فر) ( 60۳80 لانینی ).۰ .۴ - رك : رشیدی .

۴ - شاهدی .در فرهنگها نیاورده اند » ظ . این کلمه را از « مس > ( «.م. ) م رکب
ساخته آند. ۴ - پپلوی 1351 (کله . شکایت . ناله وزاری) . ایرانی باستانی-01810841
از -01800-1 از 120002۴ * نیب رکه ص ۰۱۵۳ از همین‌کلمه است : هی » هستمند :
ای از ستیهش تو «مه مردمان بست دعوبت صعب و هنکن و معلیت خام و امست-

لبیبی ۶« لغت فریس ‎2٩‏ * ۰

* - جهانگیری و رشیدی باین معنی آورده‌اند . ولی درفرابادینها «مست» و«هشت» له
مستقا( ونه‌درذدل سعد ومروة - باد شده است. رد فرهنگه‌نظام؛ ورك: هستار» مستهءمشت,وقس:
مستار. ۹ - مت بفتح اول. قس: اوستایی -1384112 (مسکر). پهلوی 1881 ۰ هندی
باستان - 338114 ( مت ) ۰ فن : - ۰380 1384211 ( شاد بودن » مست شدن ) « اسشق
۹۱ کردی 13681 ( مت ) « ژابا ص ۲۳۹۸ ؛ کی که از نوشیدن مسکر از حال طبیعی
بیرون رود - کی که بعلت داشتن مال و جاه وغیر آلها بسیار مفرور باشد.

۷ - اکر خواهی ز تب زنهار ۰ زبهار کفی از داروی مستار دست آر .

محمود تانیسری ۶ جهانگیری » « رشیدی؟ .
در تحفةٌ حکیم مومن « مستار » بهندی افنتین است » رك : مست .
۸ - باین معتی ظ . مصحف « متمند > . ‎٩‏ -رك : مس بند .
*- از : مست ( پم اول ) (۸.م.) ۳ هند ( پنوند اتصاف ).

##### pdf page 104 (printed 2021)
[pdf page 104]
-۰۱- مغز در سرکردن
مغاك ۱ - بنتح اول بر وزن هلاکه . کونند .
بمعنی گودال است خواء درزمین وخواه غیرزمن مغل - بفتح اول و سکون نانی و دال
باشد . . ابجد , علف شیرانر! کوبند و بعربی . لفا
مغالد ظلمت - کنایه از زمین است | البری(۳)خوانند ی ی کویت
- وکنایه از جد وقالب آدمی همست و آلر! | مغد پادنجان است 9 ؛ وبستی دیگ رگوبند نوعی
مغفالد ظلمت خالك (۱) میگویند. کماه كوچك باشد ‎٩‏ .
مغاك غار - بکرئاك وغن نقطه‌دار مغر - با رای قرشت بروزن محمود,
بالف کشیده وبرای قرشت(۲) زده ,کنایه ازکور | بلفت بربری نوعی از کماه كوچك باشد .38
وقبن باشد. . مغز بردن - بنم بای ابجد , کنایه از
مغان - یم اول جمع مغ است یمنی بسیا رکفتن ودرد سر دادن باشد .
آتش‌پرستان۴ سو نام ولایمی‌هم‌هست از آذربایجان مغز آر کردن - بفتح تای قرشت .
وموغان نام شهر آن ولایت است ۳ . کنایه از حرف زدن و سخن کردن باشد .
مغانه ۴ - بنم اول بر وزن دوکانه ۰ مغز در در کردن - کدابه از
طرز و روش وقاعده و قانون وآدابآتش‌پرستادر! | خاموش شدن و سکوت ورزیدن باشد.
‎٩([‏ خم۲:۱ج هم : () خم۱: برای‌بی‌قطه - ۳( خم۱: تفاح‌البری .
۹ - از : مغ ( بفتح اول ) (ه.م.) ۳ آ که ( پسوند ) . رك : اسشق ۹۸۵ . در اوراق
مانوی ( پارتی ) 28148 ( سوراخ, غار ) ۳ 13288848 ۰ در فارسی 6اه طق228 ( تبدیل کل
فارسی به 18 - , رك : 3837722 از اوستا -331080]2 ( هر چند که معنی فرق میکند )
(85. 0 را و 13 , 35085 ...86۲828 6ا۵ ۸۸:۵ 01 اعزا ۸ معصندع0)
۲ -رك :مق ای - مغان ازنوابع اردبیل در کنار رود ارس واقع ومکن‌طوایف
شاهون است. نادرشاه افشار درین‌محل بلطنت انتخاب‌شد « کیهان . جغرافیای‌طبیمی ص۱۹۷ ۹ +
رك: موغان . ۴ - از : مغ(ه. م.) ۳ آنه ( پوند دسبت ). می‌مغانه » باده پروردة مغان :
در خانقه نگنجد اسرار عفقبازی جام می مغانه هم با مغان توان زد .

« حافظ شیرازی ص ۱*۶۵ *.

رك : مزدسناص ۲۹۹ ببعد - 9 - (عر) «المغذ » البانجان » « اقرب‌الموارد» «مشد,
بادنجانت. وثمرلفاح بری‌را نیز نامند.» «تحقةٌ خکیم‌مومن » . ‎٩‏ - رك : هفرود.

مغر - بفتح اول » اوستا -1332288 ( دماغ ) « بارتولمه ۱۵۹ > ۰ پهلوی 32828
« بر که س ۱4۸ > هندی‌باستان 13880 (مغز), استی (ع؟) ۳8802 ۰ بلوچی328208.
سریکلی 21208 ( استخوان مغز ) » 130802 , شغنی 132807 ( مغز ) که همه عازیتی
هستند « اسشق ۹۸۹ ۰ ۰ افقانی 33881028 ( مغز ) (مفردوجمع) « «وبشمان ۹۸۹ > ؛کردی‌ع
2 * ژابا س 2*۲ > ؛ در اوراق عمانوی ( پارتی ) 17388 (مغز) . رك : پارسی میانه زع880»
ازاوستا 508788 (1,0.85 ,83505,126 ...۳۵۲5128 ۸۸104016 0۶ 191 ۸ ,ق2(5ع11)
ماد عسبی ارمی که در جمجمه قرار دارد و مرکز احاسات و مبداً حرکات آرادی میباشد +

روز کی چند پاش » تا بخورد خاك مغز سر خیال اندیش. «کلتان س ۵۱ >
- مادهٌ لرمی که در درون چیزی مخت باشد مانند منز کردو » مغز باام .

##### pdf page 114 (printed 2031)
[pdf page 114]
لافس نلظه:
هلان ۱ « بنتح اول و سکون آخر که | کوبند که در فلاخن گذاردد واندازند.
نون باشد » منم از افغالیدن و جنبالیدن باشده ملچکا ؟ - با جیم فارسی برون کربلا
یعنی‌میفشان ومجنبان‌چه لان بمعنی‌جنبان وافشان | بمعنی قسد و آراده باشد .
است . شم ۰۱
ملای ؟ شا ن 27۲ که ملحم * - باحای‌بی‌ضله پروزن مرهم؛
ن < بح اول دسکون آخر جامه وباقتةٌ اپربشمیرا گویند .
تحتانی باشد » منم از لابیدن است که بممنی ددم 8
گفتن ونالیدن وآلوده کردن باشد ‏ پعنی حرف ملخآبی نوعی ازماه ی كوچك باشد
: 0 َ که آنرا بعربی ارییان گوبند ‎٩‏ -
مزن وناله مکن وآلوده ماز یمنی میالای . ملخ پیاد چیه دا وه
هلائلت پی -کنایه ازمبارة پی‌وخوش | پچ : یا ۵۵ < ملع جهند را گوبند
قدم ومبارك قدم باشد . وآن غیر ملخ پرداراست؛ و بی کوبند ملخی
ی بط | است که هنوز پر بر نیاورده است و آثر| بعریی
مل ی پسی ن شراب | دبی (۳) خوانند .
مورا مه روف خرس 0 هلو - پنتع اولر رای وسکون ثالت
کش رد | وجیم فارسی . کیاهی باشد که چون چهار پایان
ملجای نوح - کایهازکیه جر | وله کر رون دا
است که کشتی لوح علیه اللام در آنچا فرود | اقا - با عین بی‌نقطه وقاف بروزن
آمد ۴ 4 دغدغه, کفچهٌ آهنیر!
ملچخ (۲) * بکر اول وسکون انی گوبند ودر خراسان نت
وفتح جیم فارمی‌وخای نقطه‌دار ساکن . سنگیرا | ملاقه خواشد ۸ . ملمقه
() خم۱: خرسند . (7) چش : ملخج (:) (۳) خما : دبا -
۱- بهی از «لاندن » (ه.م.) و ۶ لانیدن » (ه.م.) ۴ - هی ازهلایدن» (هم.)
۴ - رك : واستوت علی‌الجودی ( سورة ۱۱ [ هود ] آیةٌ ‎4٩‏ » بعنی (کشتی) بر(رکوه)
جودی قرارکرفت ( پس از طوفان ) + ۴ -اظ . مصحف « مچلکا » ۳ موچولک:» ترکی
ومفولی بمعنی الزام » حکم قضائی « جفتابی 0*۰ ۲ , عهد نامة مجرمان « غیات >"
- (عر) ۶ ملحم بروزن مکرم » جنسی است از جامه ها » (شرح قاموس):
خز بجای ملحم و خرکاه بدل باغ و بوستان آمد .
رود کی سمرقندی « المعجم شمس قیس چاپ مدری ص ۰۲۲۹
۹ - ر4: آربیان » ورك : لغت نامه «ارپیان». ۷ - (عر) ملمقه‌یکراول وقتح‌سوم
و چهارم » آلتی که بدان طعام چشند و تناول کنند - ۸ - اکنون در غالب نواحی آبران
«ملاقه» متعمل است .
ملخ - بفتح اول ودوم , دراوستا ۰132413878 ودر کزارش پهلوی0۸1 12841 » در
زبان ارمنی 12278 «فاب۱ ۴۱۹۹ و رك : اسشق ص۲۲۷. ود
درباب این کلمه توضیح کافی در مقدمةٌ کتاب حاضر ص هفده - یه
هیجده داده شده است؛ نام حشرات بالداری که بالپای‌مقدمآ نها سوت معی 0
روی یکدیگر صلیبی وار قرار کرفته و بالپای موّخر در جهت ما
طول‌خمیده شده است. وآنپا جهش وپروازمیکنند؛ جراد(ص). ملج-.:
```


## [2026-09-07T01:40:56.142Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; grep -n \"ماغ\" BQT_v4_pages.txt | head -10; echo \"--- mig\"; grep -n \"میگو\\|میگ \" BQT_v4_pages.txt | head -10",
 "description": "BQT v4 grep māğ, mīgū"
}
```


### [2026-09-07T01:40:56.209Z] TOOL RESULT

```
314:ماغذ های اضافی
487:ازپهلوانان‌چین؟ - وحاکم چین‌را نیز کویشد۴ | اس ت که خلل وکوفت دماغی و سودا وخیال خام
898:-۱۹/۳- ماغه
920:حادت در مروگاه برفلغمونی حادث در جوف دماغ » وشیخ‌الرئیی بر ورم صفراوی حادث درکید
948:ماشیا > بروزن باقیا. حشیش ارتغامونی۲ و بمعنی میخ ولزم هم ماغ
952:بر وزن نادیده ۰ بممنی ماشوء باشد که پرویزن | اوسرخ‌میباشد وسپزهم میشود و اسیزآ تراسپزماغع
953:وترشی پالا باشد . و سرخ آنرا سرخ ماغ میگوبند .
963:( عوبشمان 210۸460 . ۰۳۸ ۳) اسشق ۹۹۱ *. «ماغ ‏ هرغی باشد سیاه فام و بیشتن
965:ای خرو مبارك باراکجا بود جایی که باز باشد پرید ماغ را >
967:و در تغةٌ لفت فری چاپ هرن (ص ‎0٩‏ ) : « ماغ . مرغی باشد سپاگون, بیشتردرآ بگیرها
--- mig
433:هم میگورند و در عربی لیز همین معنی‌دارد چه بوده است ۸ .
492:هم میگوبند و بعربی مجتس 9 خوانند و بسنی | که عربان والده و ام کویند 3.۱۶
644:بمعتی مار افضا است که افودگر مار و مار | باشد وآترا بادیان هم میگونند .
684:ماد در پیزاهن - کنایه ازدشین ونوبهار» آتشکده را میگوبند ۷ .
839:چه مازه استخوان پشت است؛ وباین‌معنی درچند | و علك رومی‌را نیز ماست میگوبن دکه مصطکی
908:میباشد . نهند و بمکند - و مطلق لوله را هم میگوبند-
953:وترشی پالا باشد . و سرخ آنرا سرخ ماغ میگوبند .
955:ماه است که بعربی قمن میگوبند , لیکن معلوم | که در پس در خانه نهند تا درکشوده انگردد.
1044:باشد . میگوبند .
1069:هالّه ۱ - بروزن‌خاله. تخته‌ای راکوبند | را مالی میگویند .
```


## [2026-09-07T01:40:57.192Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ملخ\" MON_part1.txt MON_part2.txt | head -10; echo \"--- migu\"; grep -n \"میگو\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Mo'in grep malax/migu"
}
```


### [2026-09-07T01:40:57.262Z] TOOL RESULT

```
MON_part1.txt:27777:ساعت‌سازان) مقابل پاملخ. 
MON_part1.txt:28811:پاملخ: 02-22 [ < پای‌ملخ ] (امر.) چبزی 
MON_part1.txt:28812:که شبیه به پای ملخ باشد. (ساعت‌سازی) 
MON_part1.txt:28893:گلبن. پای ملخ: (کد.) چیزی اندک و 
MON_part1.txt:31139:بکار می‌رود. پروانة اتومبیل منند ملخ طیار 
MON_part1.txt:31147:جریان دارد خنکك می‌سازد. (هوا.) ملخک 
MON_part1.txt:31148:هواییما. ملخک کشتی. تفه بروانه: (ا.) 
MON_part1.txt:33844:باشند؛ مق. سواره. پر نیاورده: ملخ پیاده» ملخ 
MON_part1.txt:39185:تخم خوابیدن مرع. تخم‌اش را ملخ خورده: 
MON_part1.txt:47434:منتشر : ملخ پرا کنده. 
--- migu
MON_part2.txt:15929:است که اصطخری میگوید ار فهستان 
MON_part2.txt:43893:جراد البحر را گویند و به فارسی میگو نام 
MON_part2.txt:48074:مستقیمی را مجانب یک منحنی میگو یند که 
MON_part2.txt:64689:(جاد.) میگو. ملخ ایتالیایی: (جان.) کُونه‌ای 
MON_part2.txt:64710:دریایی: (جان.) میگو. (جاد.) خرچنگ 
MON_part2.txt:70560:میگو: 0۱2۷۵-۵0۵ (.) (جان.) جانوری 
MON_part2.txt:70566:جلو یش فاقد انبرک است. میگو در دریاها 
MON_part2.txt:70574:می‌گون میگون: «تو(و) رده (ص.) 
MON_part2.txt:76647:نصیحت: (عم.) به شما نصیحت میگویم» به 
MON_part2.txt:87129:نیز میگو بند. وکالت دیوان (اعلی): مقامی
```


## [2026-09-07T01:41:04.991Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '64680,64715p' MON_part2.txt; echo \"---- migu\"; sed -n '70555,70580p' MON_part2.txt",
 "description": "Mo'in malax and migu entries"
}
```


### [2026-09-07T01:41:05.055Z] TOOL RESULT

```
۱۳۸۰۱۳ 
ملخ‌های ماده و لا و انتهای شکم خود 
دنبالةٌ باریکی جهت سوراخ کردن زمین 
دارند که به این و سیله در سوراخی که در 
زمین تعبیه می‌کنند تخم‌ریزی می‌نمایند و 
روی تخم‌ها را با خاک می بوشانند و تخم‌ها 
در فصل مناسب تبدیل به نوزادهای بدون 
بال شده و از سوراخ خارج می‌شوندو به 
مزارع حمله می‌کنند؛ جراد. ملخ آبی: 
(جاد.) میگو. ملخ ایتالیایی: (جان.) کُونه‌ای 
ملخ که زرد روشن و یا زرد تیره است و 
طول نر آن در حدود ۵ سانتیمتر و طول 
ماده‌اش در حدود ۳ سانتیمتر است. این ملخ 
در اواخر تاستان در ن قاط مرطوب و 
علف زار تخمگذاری می‌نمابد. نو زاد ۳ 
اوایل بهار از تخم خارج می‌شود و به 
جوانه‌های نباتات و غلات و بقولات و پنبه و 
ِ مبوه حمله می‌کند. ملخ بی‌بال: (جان.) 
شک ملخ پیاده: ی 
بدون بال است؛ پورة ملخ. ملخ دریایی: 
نخان ) گونه‌ای ملخ که زرد رنگ است و 
طول بدن ماده‌اش ۱ تا ۸ سانته 0 

تسا سانه تیمتر است و عسظیم‌الجهتر ۱ 
ملخ‌های شرا تس و ایتالیایی سی‌باشد. 
ملخ‌های دریایی عموما در اواخر بهار و 
اوایل تاستان در نقاط مرطوب و کنار 
جوی‌ها تخم‌گذاری می‌کنند. این نوع ملخ 
خصوصا نوزاد آن آفت صیفی‌کاری و پنبه 
و غلات و برک اشجار می‌باشد. ملخ 
دریایی: (جان.) میگو. (جاد.) خرچنگ 
دریایی. ملخ مراکشی: (جان.) گو نه‌ای ملخ که 
خاکستری رنگ و دارای لکه‌های سباه است 
و بال‌های زرینش بی‌رنگ می‌باشد. طول 
بدن مادة آن پین ۳ تا ۳ سانتیمتر تر و طول دن 
فرش ۲ تا ۳ سانتیمتر است. اين گونه ملخ 
---- migu
میگرن: 0 زر ] (۱.) (بز.) صدای شقی. 
می‌گسار تک ۲ )۱۱۵۷ [ < 
میگسارنده] (ص‌فا.) می‌خوار» باده‌نوش؛ 
شراب‌خور. باده‌دهنده» ساقی. 

میگو: 0۱2۷۵-۵0۵ (.) (جان.) جانوری 
است از -اخه بسندباییان و از رده 


سخت بوستان و از دسته 4 خرچنک‌های دراز 
که دارای جنة کوش است. باهای 
جلو یش فاقد انبرک است. میگو در دریاها 
می‌زید. گونه‌ای از این حیوان در خلیج 
فارس و بحر عمان فراوان است و چون 
هو کن انیت سار سار آن بر مسا 
می‌کنند: ملخ دریای؛: جرادالبحره اربسیان؛ 
ماهی ربیان» خرجل, ملخ بی‌بال» مخل آبی؛ 
مر ی تن 

می‌گون میگون: «تو(و) رده (ص.) 
آنچه رنگ شراب دارد؛ به رنگ می» سرخ 
رنگ. (ا.) نوعی اسب. 

میل: 7« (ع.] (.) آلتی چوبی یا فلزی که به 
وسیلةٌ آن سرمه و توتیا به چشم کشند؛ چوب
```


## [2026-09-07T01:41:07.441Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; awk 'BEGIN{RS=\"\\f\"} /ماغ  ‏ هرغی/ || /اسشق ۹۹۱/ {print NR\": \"; print substr($0,1,20)}' BQT_v4_pages.txt | head; echo ----; sed -n '940,975p' BQT_v4_pages.txt",
 "description": "BQT māğ page"
}
```


### [2026-09-07T01:41:08.742Z] TOOL RESULT

```
27: 
[pdf page 27]
ماش
118: 
[pdf page 118]
۳و 
----
که فتبلةٌ تفنگه را در آن محکم‌کنند و آنش | درخت است وآن صمخ را بعربی قنه کویند.
پرنفنکه زنند - و يك حصه ازدوازده حص‌تولچه ماع -بر وزن زاغ » نوعی از مرغابی
را نی زکوبند و تولچه دو مثفال ونیم است ۱ - | اس وآن سیاه میباشد
دمرچیز را یز کویند که بقدر مان باشد. و بعربی مایکون (۱) ۵
ماش هندی - غلهایست عودی رنگه 1 ی تن
8 و بترکی نننلداق ‏ ون
پاندام کندم کوجچکی و. آترا بسربی حب الفلت | میکوبند؟ و ازکوشت اک و پر هش
خوانند بکس قاق . او بوی لجن میآیید -
ماشیا > بروزن باقیا. حشیش ارتغامونی۲ و بمعنی میخ ولزم هم ماغ
است وآن رستنیی باشد مانند خشخاش وپشیرازی | گفته‌اند ‎٩‏ وآن‌بخاری باشد بیارتیره و ملاصق
مامیای سرخ کویندش . بروی زمین وآنرا بمربی زباب خوانند - وئوعی
ماشیوه - با تتابی مجهول وفتح واو ا زکبوتر هم هست که هردو بال وکردن و سینةٌ
بر وزن نادیده ۰ بممنی ماشوء باشد که پرویزن | اوسرخ‌میباشد وسپزهم میشود و اسیزآ تراسپزماغع
وترشی پالا باشد . و سرخ آنرا سرخ ماغ میگوبند .
ماص ۲ < بسکون صاد بی‌لقطه »بمعنی ماقه - بر وزن شافه » چوبی را کویند
ماه است که بعربی قمن میگوبند , لیکن معلوم | که در پس در خانه نهند تا درکشوده انگردد.
نیت که پلفت کجا است . ماقوت - بروزن باقوت . نام نوعی از
ماطو نیون - با طای حطی‌بواورسیده | حلوا (7) باشد وآیرا هاقوآی هم میکویند۹ -
() چك » چش : مالیکون - () چش : نام حلوائی .
۱- يك حصه از دوازده حصة تولةٌ هندی (دو متقال ونیم) . درین معنی هندی است
که در طب فارسی داخل شده « فرهنگه نظام > . رك : ماهه . ۴ - رك4 : ارغاموتی .
۴ - بدانکه ماس پمعنی‌قمرسنسکرت است«چك ۹۸۳ ح» . صحیح «مای» (مانسکربت
5) « وبلیامز ۶ ۳:۸۱ > است . ۴ - هندی باستان - 22081 ( نوعی پرنده آبی )
( عوبشمان 210۸460 . ۰۳۸ ۳) اسشق ۹۹۱ *. «ماغ ‏ هرغی باشد سیاه فام و بیشتن
درآب نعیند . دقیقی (طوسی) کوید :
ای خرو مبارك باراکجا بود جایی که باز باشد پرید ماغ را >
« لغت فری ص ۲۳۵ ۰ .
و در تغةٌ لفت فری چاپ هرن (ص ‎0٩‏ ) : « ماغ . مرغی باشد سپاگون, بیشتردرآ بگیرها
باشد . دقیقی گفت : ای خرو ... » واظ . همین جمله است که جهانگیری - با مأُخذ او -
آنرا بدین صورت درآورده : « نوعی آزمرغایی راکوبند وآنرا بتازی مایکون وبتر کی قعقلداغ
خوانند > و برهان ازو تبعیت کرده است و « مایکون » مصحف « سیاهگون » است وعربی نیست-
عمیغ دمع ( بکر )مه (بکر).
۹ - مکمل چو پوشید رخت نبرد ز ماقوت سرخ وز لیمی زرد .
باق اطعمه « فرهنگه نظام *.
[pdf page 28]
-۱۹۶۵- ما کول
```


## [2026-09-07T01:41:24.603Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pdf page\\|^\\[page\" MON_part1.txt | head -3; python3 -c \"\nt=open('MON_part2.txt',encoding='utf-8',errors='replace').read(); print('formfeeds',t.count(chr(12)))\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['MON'],ensure_ascii=False,indent=1))\"",
 "description": "MON page structure"
}
```


### [2026-09-07T01:41:26.238Z] TOOL RESULT

```
formfeeds 0
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


## [2026-09-07T01:41:41.498Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"MATTE\\|MAT\\b\\|matte\" AHD_watkins1985.txt | head -10; echo \"-- kln matte\"; grep -n \"matte, adj\\|mat,  adj\\|^mat\\b\" KLN_1966.txt | head",
 "description": "Watkins matte, Klein mat"
}
```


### [2026-09-07T01:41:41.566Z] TOOL RESULT

```
558:[hulé. Forest, timber, hence stuff, matter. Greek noun of unknown origin. -YL, YLEM; HYLOZOISM, METHYLENE.]
730:tive masculus, male, manly: MACHO, MALE, MASCULINE; EMASCULATE.] mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 700.] mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS. 4, Latin mdteriés, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard timber used in carpentry, hence (by a calque on Greek Aulé, wood, matter) substance, stuff, matter: MATERIAL, MATTER. 5. Greek compound Démétér, name of the goddess of produce, especially cereal crops (dé-, possibly meaning “earth”): DEMETER. [Pok. mdter- 700.] math-. Worm. With uncertain preform, but clearly re- lated, is Old English moththe, moth: motu. [Pok. 1. math- 700.] [Mawort-. Name of an Italic deity who became the god of war at Rome (and also had agricultural attributes), hence also the name of the planet Mars (doubtless from its red color, the color of blood). Latin Mars (stem Mart-), Mars: MARCH, MARS, MARTIAL, MARTIAN.] mazdo-. Pole, rod, mast. Germanic *mastaz in Old Eng- lish mest, mast: MAST}. [Pok. mazdo-s 701.] me-1. Oblique form of the personal pronoun of the first person singular. For the nominative see eg. 1. Germanic *mé- in Old English mé (dative and accusative): ME, MYSELF. 2. Possessive adjective “mei-no- in Germanic *min- in: a. Old English min, my: MINE?, My; b. Middle Dutch mijn, my: MYNHEER. [Pok. 1. me- 702.] me-2, In the middle of. 1. Suffixed form *me-dhi in Germanic *mid- in Old English mid, among, with: MID- WIFE. 2. Suffixed form *me-ta in Greek meta, between, with, beside, after: META-. See also medhyo-. [Pok. 2. me- 702.] mé-1, Expressing certain qualities of mind. Contracted from *meo-. 1. Suffixed o-grade form *mé6-to- in Ger- manic *méthaz in (i) Old English méd, mind, disposition: MooD! (ii) Old High German muot, mind, spirit, in German Gemiit, spirit, feelings, temperament: GEMUT- LICH, GEMUTLICHKEIT. 2. Perhaps Latin més (< *mé-s-), wont, humor, manner, custom: MORAL, (MORALE), MORES, MOROSE. [Pok. 5. mé- 704.] m6-2, To measure. Contracted from *meo-. I. Basic form mé-. 1. Suffixed form *mé-lo- in Germanic *mélaz in Old English m#l, “measure, mark, appointed time, time for eating, meal”: MEAL?; PIECEMEAL. 2. Suffixed form *mé-ti- in Latin métiri, to measure: MEASURE, (MEN- SURAL); (COMMENSURATE), DIMENSION, IMMENSE. 3. Possibly Greek metron, measure, rule, length, propor- tion, poetic meter (but this is referred by some to med-): METER!, METER?, (METER?), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRO- NOME. 4, Suffixed form *mé-trd- in Sanskrit mdtrd, a measure: MAHOUT. II. Extended and suffixed forms *mén-, *mén-en-, *mén-s-, *mén-dt-, moon, month (an ancient and universal unit of time measured by the moon). 1. Germanic *ménén- in Old English ména, moon: Moon; (Monpay). 2. Germanic *ménéth- in Old English ménath, month: MONTH. 3. Greek mén, méné, month: AMENORRHEA, CATAMENIA, DYSMENORRHEA, (MENARCHE), MENISCUS, MENOPAUSE. 4. Latin ménsis, month: MENSES, MENSTRUAL, (MENSTRUATE); BIMES- TRIAL, SEMESTER, TRIMESTER. [Pok. 3. mé- 703, ménot- 731. fen Big. Contracted from *meo-. 1. Suffixed (compara- tive) form *mé-is- in Germanic *maiz6n- in Old English mara, greater, and madre (adverb), more: MORE. 2. Suf- fixed (superlative) form *mé-isto- in Germanic *maista- in Old English m&st, most: Most. 3. Suffixed o-grade
749:men-2. To project. 1. Suffixed zero-grade form *mn-to- in a western Indo-European word for a projecting body part, variously “chin, jaw, mouth,” in Germanic *mun- thaz in Old English mith mouth: mouTu. 2. Latin mi- nae, projecting points, threats (> mindri, to threaten): MENACE, MINACIOUS; AMENABLE, DEMEAN!, PROME- NADE. 3. Latin -minére, to project, jut, threaten: EMI- NENT, IMMINENT, PROMINENT. 4. Suffixed o-grade form *mon-ti- in Latin méns (stem mont-), mountain: MONS, (MONTAGNARD), MONTANE, MONTE, MONTICULE, MOUNT!, MOUNT?, MOUNTAIN; AMOUNT, ULTRAMONTANE. [Pok. 1. men- 726, 2. menth- 732.] men-3, To remain. Variant suffixed (stative) form *man-é- in Latin manére, to remain: MANOR, MANSE, MANSION, (MENAGE); IMMANENT, PERMANENT, REMAIN. [Pok. 5. men- 729.] men-‘. Small, isolated. 1. Greek manos, rare, sparse: MANOMETER. 2. Suffixed o-grade form *mon-wo- in Greek monos, alone, only, single, sole: MONAD, MONAS- TERY, MONK, MONO-; PSEUDOMONAD. 3. Possibly also suffixed form *men-i-, a small fish, in Old English myne, mynwe, minnow, perhaps the source of Middle English meneu, a small fish: MINNOW. [Pok. 4. men- 728, meni- 731.] mend-. Physical defect, fault. 1. Latin mendum, menda, defect, fault: MENDICANT; AMEND, EMEND, (MEND). 2. Latin mendax, lying, liar: MENDACIOUS. [Pok. mend(a) 729.) mendh-'. To learn. Zero-grade form *mndh- in Greek manthanein (aorist stem math-), to learn: MATHEMAT- ICAL, (MATHEMATICS); CHRESTOMATHY, POLYMATH. [Pok. mendh- 730.] mendh-?. To chew. 1. Latin mandere, to chew: MANDI- BLE, (MANGE), MANGER. 2. Zero-grade form *mndh- in: a. Greek masasthai (< *math-ya-), to chew: MASSETER; b. Greek mastax, mouth, the model for expressive Greek (Doric) mustax, upper lip, mustache: (MOSTACCIOLI), MUSTACHE; Cc. Greek mastikhan, to grind the teeth: MASTICATE. [Pok. 2. menth- 732.] menegh-. Copious. Germanic *managa- in Old English manig, menig, many: MANY. [Pok. men(e)gh- 730.] meng-. To furbish. 1. Latin mango, furbisher, gem pol- isher, swindler: MONGER. 2. Greek manganon, magic
1829:MATCH2 meug-2 MATE! mad- MATELOTE neud- MATER miater- MATERIAL miater- MATERNAL miater- MATERNITY méater- MATHEMATICAL mendh-1 MATHEMATICS mendh-! MATINEE méa-1 MATINS ma-1 MATRICLINOUS  klel- MATRICULATE miter- MATRIMONY miater- MATRIX miater- MATRON miater- MATTER méater- MATTOCK mat- MATURE ma-1 MATUTINAL ma-1 MAUL mele- MAULSTICK mel-2 MAUVE malakhé MAW mak-2
-- kln matte
23101:mat,  n.,  a  coarse  fabric  made  of  straw,  hemp, rushes,  etc.  —  ME.  matte,  fr.  OE.  matt,  fr.  Late L.  matta,  ‘mat  made  of  rushes’  (whence  also OHG.  matta,  MHG.,  G.  matte),  fr.  Phoem- Punic  matta,  corresponding  to  Heb.  mitta  , ‘bed’,  which  is  formed  from  the  stem  of  natd  , ‘he  bent’  (for  sense  development  cp.  Gk.  xXfvr„ ‘bed’,  fr.  xXtvEtv,  ‘to  bend’).  From  Late  L. natta,  a  secondary  form  of  Late  L.  matta,  which occurs  in  the  writings  of  Gregoire  de  Tours,  de¬ rives  F.  natte,  ‘mat,  matting’.  For  the  change of  Heb.-Punic  initial  m  to  n  cp.  F.  nappe, ‘tablecloth’,  fr.  L.  nappa,  which  derives  fr.  Heb.- Punic  mappdh  (see  napery,  napkin).
23103:mat,  adj.,  dull  (said  of  color  or  a  surface).  —  F., ‘dull,  lusterless,  unpolished’,  fr.  OF.  mat,  ‘de¬ feated,  afflicted,  depressed,  dejected;  dull’,  fr. Arab,  mat  in  the  sentence  mat  ash-shah,  ‘the king  has  died’.  The  word  mat,  orig.  used  only as  a  term  of  chess,  gradually  developed  also  the meanings  ‘faint,  feeble,  dull-colored .  See checkmate  and  cp.  matador,  mate,  adj. matador,  n.,  1)  the  man  who  kills  the  bull  in  the bullfight ;  2)  one  of  the  three  chief  cards  in  the game  of  ombre  and  quadrille.  —  Sp,,  ‘killer, murderer’,  fr.  matar,  ‘to  kill,  murder’,  fr.  Arab. mdta,  ‘he  died’.  Cp.  checkmate.  Cp.  also  mat, ‘dull’.
```


## [2026-09-07T01:41:44.038Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\np=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(p))\nfor i,pg in enumerate(p[:230]):\n    if 'ملخ' in pg or 'سغدی' in pg and 'ملخ' in pg:\n        print('LEAF',i, pg[:1500].replace('\\n',' | ')[:1500])\n        print('-----')\nEOF",
 "description": "BQT intro malax search"
}
```


### [2026-09-07T01:41:45.352Z] TOOL RESULT

```
777
LEAF 25 هقد م زبانبای ایرانی | ۰ , 02:10 . 540۵016 وعاهو , 1000۲۲۷ 5۲۳ | )0 10 ۲۵ :۱۲60 ۸ , 10۳0۷۷ 57 | ۰ 1 0۵10 .6و6 | ٩۲۲,۱۷۲ ۲۵۱۱۲۷ 2۷۵1۶ ۳8166۲ 6۱۵۵۲ ۵۲0‏ | ۰و0و1 صز مج ععععطط موه ول یه فمل 66۲۱۲۲ | . 1 ,1935 ,۲۲۰ ۸ 8۳ | ٩5۵8 - 0 ۰‏ عمط من ر 16۵۳۷۲۵۲۲ ۳ ٩1‏ | ۰ .۲۲ ۸ 5۳ | ۰ 180۱6 »1 وص وه 0 1 , ۱۷۷ 6۳۱۲۵ ۷( ٩‏ | ۰ 2 :1,1۳2 | 0( ۲۵ ۱۲۶ معل ,۲۱2 )مزع م5 ,۱۷ ۱۷ ۷۸ اب۷1 | ۰ :2:۳0 | - ۵۲ ۱۰ .1648 عهم‌صوامطظ ,]4۸1 ۰ ۰۱۷ ۲۲ | ۰ 5 ۲:۱2۶ظ | مها ۵ نز م۲۱۵6 ده ولا نا ۱۱۰۱۷۰31۸ | ۰ ۲۷۸ ,4۳۱6۱۵8۸118 ۸۵) .ههد | تمه 016 0صته فدعامد 1۲:6 ,۱۳,۲۳۵ /۲۲.۲,۱۱ | ,3 .۳۸۲۲۷۲۰ ط5 .5۴۲۵66 | سغد ۱ سرزمینی است در سیای مر کزی . کلمة | سغدی سغددر بارسی باستان8 5۱6۱10 یا 580 در | اوستای متأخر ٩09‏ ( کشور سغدیان ) | و 1۱6۵۵۳9۲۵۵ 0عی5 (مقر سغدیان) :در بوتانی 5080101 با | 03 (مده . | سغدیان. یاسا کنان سغد-قومی از نژاد ایرانی بودندنایم دولت‌پارس | هخامنشی ۰۳ وسرزمین آنان؛ قول نویسند گان یو نانی؛ازجیحون( آمودریا) | تاسیعون (سیر دریا) امتداد داشته است ؟ . | دراوستا هیچگو نه شرح وتوضیحی درباب سغدیان مندرج نیست.تنها | موضوع محقق آسیبی است که برسرزمین سفد مسلط بوده» و آن وجودملخ | بود.اين آسیب‌در ناحبه‌ای که | کنون تر کستان روس گویند- امری‌طبیعی | است.قابل توجه است در یتخصوص باد آور شویم که سه نام مختلف بر ای‌ملخ | 0- در منابم عربی < السفد > . ۲ - لاقل از زمان داربوش اول (۵۲۲- ۵۸٩‏ | ق.م) بسفد, رژگ: دائرةا لمعاریاسلام: صقد. بقلم بارتولد.
-----
LEAF 26 ۰ عمقدمه هد ه | در زبانپای ایر انی وجود دارد : اول مذخ 8 1080 4 ) در قدیم مد خه | ۵ ) که مختص زبان‌شمال ایران-یعنی «اشکانی >- است‌ووجود | آن مانند تلفظ وی از کلم دخیل ارمنی مرخ:108۳82 تأید میشود ۱. دوم | میگ م81 ۴ متملق بز بان پارسی بمعنی اخس- یعنی لپجه‌جنوب غر بی- | و آن در اصل‌مذ که 8 ۰ مذیکه 8 ۹ وده‌است. | سوم لفتی که‌در ز بان فارسی کنو نی نیز استعمال میشود- و لی‌قطما دخیلاست- | ملخ ۲912 است»و آن ازلفت باستانی‌مذخه وولو ۶ ]مده. کلیة | ملخ برهمان شکل اصلی ارمنی مرخ 08۲8 استوار است ‏ و بدین وجه | با لپجه‌های شمالایر آن‌نز ديك میشوده اماتبدیل ذ 4 به‌ل [ز بان مز بوررا | از آنها جدامیکند. هرن ۴ کلم مز بوررا بالفت‌افتانی ملخ <10818مقایسه | کرده است. اما اطلاعی که ازاوستا رسیده موّید آنست که اصل‌کلمه سفدی | است» چها کنون میدا نیم که يك لهحه ههم‌سخدی و جود داشته که در آن‌ذ 0 | ازقر ائن‌دیگر ثابت‌شده که عاریت کر فتن کلمات‌سندی درز بان‌فارسی | دورةٌ اسلامی معمول بوده است ۴ . در قدیمترین فرهنک موجود فارسی - | لفت فرس اسدی -کلماتی آهده است که موّلف [نها را «سفدی» میخو اند | ولی نظر مبرسد که ای نکلمات بشتر تلفظهای محلی باشند تالغات دخیل از | سفدی ۵ | ژ بان یرانق سمر قند است.اینز بان بوسبله اسناد وادیات | و سیم خود - که‌هم در سر زمین اصلی سفد بدست آمده وهم در بسیاری از | مستص ات ستدی که دز همه 4 ۲سیای خر کری ی چین امتداد داشته- | بحو یی شناخته میشود ۱ . | بعضی اسناد که در آسیای مر کزی» مق ما درایالت چینی کان سو | و اخبر ید اشده؛» زبا تشناسانر ا بوجودز بان سقفی] گاه | ۳ یش از کقف این اسناد کلمهٌ «سفدی» ۷ درمورد زبان بکار نیع فت | ۳۳ ,۷611/6( ونژ 100 .۵ ,. ٩4‏ .۳6۲5 و ۲۱1004600۳0301 .۶ -۱
-----
LEAF 119 صد ویازده اقتباس وقهلید وترجمه ورد برهان | مقدورو دشوار و لفت‌های مختصر ناتمام وماه انتظار است ومعپذا بر هان | که جامعتر ین کتب این فن است » باآن بسط وتطویل اين عیب را دارد | که خالی ازشواهد است. وهريك از کنایات رالغت علیحده نوشته ومشتمل | است بر لفت های غیر سمل و ماًنوس از یونانی وسریانی و زند وپازند | و ترکی .که اصلا مستعمل نیست » وهمه موجب طول لاطایل ؛ و فرهنگ | جپانگری نیز باآن طول وصیل بیاری از لغت ها را ترك کرده و آنچه | نوشته معانی ]نپا را تمام ننوشته مثلا لفتی که بنج معنی دارد » سه یاچپارش | نوشته» لپذا توفیق‌سیحانی همت‌نموده محموع لغات مستعملة بر هانر | | ملخص و مختصر و قدری از شواهد فرهنگ جپانگیری در حاشیه » | وکنایات هر لفظ را در ذیل آن درح نموده و حشو وزواید را ترك کرده | بحدالُ کتایی شد مفید و مختصر و جامع و سپل المأخذ و مقبول الکل | ونافع ...> | اما جامم< برهان جامم > بتقلید جپانگیری ؛ حرف دوم هر کلمه را | مأخذ باب قرارداده وسپبس حرف‌اول را مأأغذ فصل دانسته است ! | قاطع بر هان ۱ | قاطم برهان تألیف میرزا اسدال غالب خان دهلوی شاعر معروف | ( تولد ۱۷۲۱۲ - وفات ۱۲۸۵ هجری قمری ) است ؛ و آن انتقادی است | بر برهان قاطم . | غالب در مقدمه قاطم برهان گو ید : | <... هر گاه غم‌تنبائی رو آوردی » برهان قاطم رانگرستمی » چون | آن سفینه گفتار های ادر ست داشت و مردم را از راه می‌برد » و من آئین | آموز گاری داشتم » بربیروان خودم دل سوخت » جاده نمایان ساختم تا | براهه نبویند ... با اینهمه کوش شکه درجدا کردن راست از کاست مرابود » | ننوشته ام مگراز بسیاری اندکی » چنانکه بی مبالنه میگویم از صد یکی | هما نامیغو استم نوشت ومیدانستم نوشت » اما بسیب انبوهی بیان های ژو لیدة | جامم‌مجموع نتو
-----
LEAF 220 نواحی باشند از دنبال شخصي که آب میبرد روان | شوند تا بهرجا که ملخم آمده باشد آن سارها | تام آن ملخها را بکشند و پراکنده سازندوآن | چشمه را چشمةٌ سار هم میگوشد . | آب مر وار یف «- کنایه از روشنی | و روتق مروارید باشد - و نام علتی جم‌هست که | در چشم آدمی )۱( بیدا میشود . | آب هریم - بکس ثالك » جایوسلاح | حترت (۲) مریم مادر عنمی علیهاللام (۳) را | کوه شدب وکنابه آزشیر #ادگوروشرا اب‌انگوری(4) | ی | ] ب‌هنجهد » پکتر تاكث , کنابه از | تیخ و شمشبر و خنجر وامثال آن باشد س و کتابه | از شيثه و آبگینه و بلور هم حست - و بخ | و تگرك را یز کویند . | آب هنال - یک ؟الث » بیعنی آب | منجمد است که کنابه از شيشه و آبگینه وبلور- | و یخ و نگ رکه - و نی و خنجر باشد . | آآب ام ه یکس #الت و نون بالف | کشیده و برای قرشت زده » کنابه از شراب | باشد ٩‏ . | آب نافع - بکسر الث وفا » کنابه | از شراب انگوری باشد . | اب ثتخوردن « کنابه از درنگه با | کردن و توقف تمودق پلشد ۰ _ ۱ | آ نوس - بس وزن خاکبوی درختی | باشد سیاه ۴ و مشهور است و آنرا سربی نیز | آبنوی خوانند . اکر بر آتش نهند مانند عود | بکدازد و بوی خوی دهد . و اکر با آب (ه) | بسابند و در چشم کشند شب کوری را برد | و خوردن آن سنکگ مثانه را بریزاند - و نوعی | از ماهی حم‌هست بسیار لذمف - | آبنوسی شاخ ) » سوری () | را گوند و آن را شهنای هم خوانند - و نایی | را ی زگویند که از چوب آبنوی ساخته باشند . | ]بو « ین ثاك و سکون واو » کل | یلوفر را گویند . | - آب ودد ه بح واد و سکون ثالث | و رای بی هطه و زای قطمدار + شناور و شنا | کننده را گویند. | آ وق بضم بای فارسی و سکون واو | و فاف » آنت که کسی دهان خود را برباد کند | و دیگری چنان دستی بر آن زند که آن باد با | ص
-----
```


## [2026-09-07T01:42:21.958Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '36860,36920p' LAT.txt",
 "description": "Ernout-Meillet matus"
}
```


### [2026-09-07T01:42:22.011Z] TOOL RESULT

```
de Manicheens); mattula. Panroraan, sauf roumain. M.L.5484 matta et
*natta~, et germ.: v.angl .matte, meatta "Matze". Sans doute mot d'em-
prunt, comme mappa.
mattea: v. matia.
*mattia: non attest^ isol<$raent: figure dans mattiobarbulus "sorte
de javelot",et nat (t) iarius "soldat arme de ce trait". Tardif (V4g. ).
- Non latin.
mattlci: — cognominantur homines magnarum malarum atque oribus
late patentibus, P.F.115,3. A rapprocher peut-etre de gr. p,a9uuxi, •
yvaGou Hes. Geminae interieure expressive.
mattus: v. matus.
matula, -ae f. : vase, pot (employe aussi comme terme d'injure,
cf. fr. cruche), pot de chambre. Attest4 depuis Plaute. Populaire. M.L.
5489. Diminutif: matella f., d'ou matellis, -Unis . Sans ^tymologie.
mSttlrus, -a, -um: i° qui se produit au bon monent, A 1'heure fa-
vorable, topoaoc, cf. Geli.10,11,8-4; 8° qui se produit de bonne heure
(par la meme acception de "bon" que dans mane, matutinus). De IA deux
sens qui, en se developpant, sont devenus contradictoires:
1° mur, muri; qui arrive A son plein developpement, par suite
"opportun" (syn. de tempestiuus) et aussi par litote, "age, vieux":
poma matura et cocta, Cic.C.M.19,71; filia matura uiro, Vg.Ae.7,53;
animo maturus et aeuo, Ov. M.0,67; uiridis aeui, maturus animi Claud.
Mamert.anim.89,p.i35,is; natura imperia "ordres vieillis", Just.n,5,7.
"Comme un dessein muri est un dessein qui a demande du temps, maturus
se prend quelquefois dans le sens de "reflechi, preparf? A loisir";
maturum consilium, Cic. Diu. 1, 18 . " (B.B.).A ce sens se rattachen*t
im-natUrus (= ounpog) et praendturus , tous deux anciens (Pl.) et clas-
siques; per-, rudi-, semi-maturus , tardifs; maturesco, ematuresco',matus
6 y6
nature/aci 5 .
3 ° qui se produit de bonne heure, d'ou, hatif, precoce: naturae
Menes "hivers pr< 5 coces", Ces. BG 4,30,1; mature fieri senem, Cic.
C.M.10,33; quibus rebus quam maturrime occurrendum putabat, Ces. BG
1,33 fin.
Les deux sens se retrouvent dans naturo, - 5 s "murir" et "faire
murir"; "hater" et "se hater". Par contre maturitas n'a guere que
le sens de "maturite" (d'ou immdturitds) ; le sens de "hate, prompti-
tude" est rare et seulement d'epoque imperiale; 1'auteur de la Rhet.
a Herennius emploie dans ce cas maturatio, la langue ayant differencie
dans 1'emploi le nom deriv£ de 1’adjectif et le non deriv^ du verbe.
Ancien (Pl.), usuel, classique. Maturus est deriv^ d'un thome en
-u-, natu- non atteste; cf. mdtuta, matutinus . II est demeure dans
les 1 . romanes, M.L.5433 (panroman), comae maturitas id.5433, maturare
5430 (panroman, sauf roumain), maturescere S430a, * naturicdre 5431,
mais seulement avec le sens de "mur".
Cf. mane, au sens de "de bonne heure".
La notion de "mur" est exprimee de maniores diverses suivant les
langues; les expressions ne concordent pas, meme quand elles appar-
tiennent a une meme racine, ainsi skr. pakvah et gr.ueroxV.
matus, -a, -um: ivre. Mot vulgaire (Petr .41), qu 1 on retrouve dans
les gloses: matum est, hunectum est, emollitum, infestum, CGL V 604,41.
On lit aussi mattus (natus): tristis, CGL IV 114,4; 337,5; 536,31;
V 465,6; .543,40. Mais peut-etre sont-ce deux mots differenta. Le
rapprochement de 1 'ital. matto est aujourd'hui conteste; cf.M.L. s.u.
*mattus, 5438.
Mattus peut reprdsenter une prononciation vulgaire (dialectale)
de *naditus', toutefois le rapprochement de nitidum, ital.netfo ne
prouve rien, si l'adj. italien est empruntd au gallo-roman net, comme
l'indique, sana preuve, M.L. s.u. nitidus, 5y3y.
Matuta, -ae f. : ancienne deesse italique, identifide avec l'Au-
rore (Lucr.5,656), puis avec Leucothea. Mdtuta est le f^minin d’un
```


## [2026-09-07T01:42:24.136Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\np=open('FRS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(p))\nfor i,pg in enumerate(p):\n    for w in ('ماغ','مغاک','مغاك'):\n        if w in pg:\n            print('LEAF',i,w)\n            print(pg[:800].replace('\\n',' | '))\n            print('---')\n            break\nEOF",
 "description": "Loghat-e Fors grep"
}
```


### [2026-09-07T01:42:25.396Z] TOOL RESULT

```
leaves 568
LEAF 93 مغاك
                                  ‫‪۷‬‬ |  |  ‫غرنج‪ :‬ارزن کوفته باشد» (چ دیکر‪ :‬لکد کوب‌باشدبزبان پارسی»کو ج ‏‬ |  ‫جفدبودیعنی کوف» کابلیچ ‪ :‬انگشت کوچك بود» غلج ‪ :‬بندی بودچون‬ | ‫شلوار بندوغیره » غفج ‪ :‬مغاك » فخوج [ ص ‪ -‬خوج ] ‪ :‬اسر دولت‪.‬‬ |  ‫‪:‬است بود یعنی ببای کرده »‬ |                          ‫بود » کشتج ‪ :‬گیاهی بودخوشبوی » هچ ر‬ |  | ‫نمچ ‪ :‬تری بود که از سنك ياازجای نم بر آید » ‪#‬مساح نهنگ بود‬ |                                              ‫چنانکه شاعر کود ‪:‬‬ |        ‫و البحر غیرناتمساح‬ |                         ‫ی‬   ‫اس‬     ‫رز‬   ‫اهنا‬ |  |                    ‫سیم‬   ‫تست‬ |                            ‫‪6 0> 06‬‬      ‫سس‬ |                                          ‫صمست‬ |  |  |                             ‫تب الحاء‬ |  |                                  ‫یامد‬ | 
---
LEAF 218 ماغ
                                         ‫‪۱۹۹‬‬ |  |  |                                     ‫(‬            ‫تین‬ |                                                     ‫ترش ترش‌باشد خاشالك خورد() ‪.‬‬ |  |                                     ‫کهوش! )‪(۹‬‬ |  |                                                                          ‫لختها (‪ ):‬باشد ؛‬ |                                             ‫‪۲۳‬‬ |                                                  ‫کاس‬ |  |                                                                 ‫خولد‪ ۴‬بود|فرخی گفت ‪:‬‬ |  |                                         ‫چو کاس موی گاهان او برهنه ز برك‬ | ‫چو شاخ کاو درختارن او تهی از بار ]‬ |  |  |  |   ‫را نسجخهٌ اساس ندارد ولی سمخ دیگر هر کدام بر بعضی از ‪۳‬‬ |                                                                                   ‫لغات
---
LEAF 230 ماغ
                                                 ‫‪۳۱‬‬ |  |                                    ‫گوهر فروش‬                        ‫یأسمن لعل پبوش سوسن‬ |          ‫د ‪۱‬‬ |            ‫‪:‬بر زنخ ِماغو ش ن‪2‬طه زد و ‪۳‬شکش ‪0‬‬ |                                ‫‪۲‬‬     ‫‪۰‬‬       ‫‪۵‬‬        ‫ما‬   ‫و‬   ‫هي‬ |                                     ‫مد ه جر شس‬ |  |                              ‫بود |فرخی ‪ ۳‬گو ید ‪:‬‬                         ‫خند بدن و چولن هسحره‬ |  |  |                                      ‫ای کرده مرا خنده خریش همه کس‬ |  |         ‫ماراز تو بس جاناما رازتو بس‬ |                                          ‫ء‬       ‫هو‬        ‫‪۶‬‬ |  |                                              ‫هو سس‬ |                                    ‫»ردو سی گوید ‪:‬‬ |                                                 ‫بزبان بهل
---
LEAF 254 ماغ
                                       ‫‪۳۳۵‬‬ |  |   ‫‪.‬کی بنمتاسیر ‪ ۱‬بغور اندر‪۲‬‬                  ‫ای چون مغ سه روز بگور اندر‬ |                                          ‫‪۳‬‬ |                                          ‫‪0‬‬ |  |  |  |  |                                         ‫سروی کاو‌باشد ف|ردوسی گوید ‪]:‬‬ |         ‫شخ کاوو دنبال گر کی بدست ‪٩‬‏‬              ‫ببازی‌و خنده گرفت و نشست؛‬ |  |                                         ‫‪1‬‬ |                                         ‫ب‬ |    ‫معشوق بود » دیگربعبارت فرغانیان‌صنم و بت بوذ [عنصر ی گوید‪:‬‬ |                                ‫گفتم فغان کنسم ز تو ای بت‪ .‬هزار بار‬ | ‫گفتا که از فغات بود اندر جهان فنان ]‬ |                                        ‫م‪۷‬ا‪۰‬‬ |  |                 ‫مرغی باشد سیاه فام و بیشتر در آب نشیند [دقیقی گوید ‪:‬‬ |         ‫جایی که‌باز باشدپ
---
LEAF 256 ماغ
                                      ‫‪۳۳۷‬‬ |  |                                     ‫ستاغ‬ |                                         ‫اسب‌زین ناکرده [ خفاف ‪ ۲‬گفت ‪:‬‬ |  |  |     ‫توچون ستاغ "جکهری‌ازمن"‬                 ‫مس بتاوال باشم همواره‬ |                                                                   ‫شهید گوید‬ |     ‫چون‌بزینو لکام تند ستاغ ]‬               ‫شوی نرم هم بصیر و درم‬ |  |                                         ‫‪9‬‬ |                                         ‫‪۳‬‬ |                                     ‫همچون قفیزی باشد [ابوالعباس گفت ‪:‬‬ |   ‫بانغنکی چند ترا منانبازم*]‬              ‫ای مبرترا کندم دشتیست استده‬ |  |  |                                        ‫‪2‬‬ |  |                                               ‫کریز باشد [ عنصر ی گفت ‪: ۷‬‬ |     ‫تا‬           ‫‪.‬مهرجمداردات‬             
---
LEAF 316 ماغ
                                        ‫‪۳۹۷‬‬ |  | ‫همه درو غزن و خر بطند و خبره سرند‬               ‫گروهی‌اند کهندانندبازسیم ز سرب‬ |  | ‫نمتك و نبزددیکشان یکی باشد اآزنکه‌هردوبکونه شیه بکدبکرند‬ |                                         ‫مك"‬ |                              ‫‪۲‬فت ‪:‬‬ |                                  ‫سپیدی بن ناخن باشد ؛ احمد برمك گ‬ | ‫مالش ازناخن همی جدا خواهی کرد دردت کندای‌دو ست خطاخواهی کرد‬ |  |                                         ‫جوك‬ |                                      ‫ء ‪۴‬‬         ‫‪9‬‬ |  |  |  |                ‫‪:‬‬   ‫مرغیست کهخویشتن از درخت بیاویزد ؛ پهرامی کت‬ |                                   ‫‪۳۱‬چو من ز غم عشق زرد گشت‬ |  | ‫وز شاخ همچو حو لمبیاویخت خویشتن ؛‬ |                                                               ‫[نوچهر ی کوید]‪:‬‬ | ‫جولمزشاح در خت‌خویشتن آو يخته 
---
LEAF 334 ماغ
                                     ‫‪۵۱۳‬‬ |  | ‫دیر‪.‬ست باغ اندر بر زر ینقندیل]‬             ‫ای‌ماهی‌زر ین‪ ۱‬بومه برزده نشییل‬ |  |                                    ‫چشماغیا‬ |                        ‫بخشم بکوشة چشم نگریستن بود [ حکالم گوید ‪:‬‬ |   ‫نرمك او را بکی سلام زدم کرد زی من نک» بحشه‌اغیل ]‬ |                                    ‫حول"‬ |         ‫فندان و چهاربایان بود چون خباك [بوشکو رگوید ‪:‬‬ |                                                     ‫کبوگساه‬ |                                                           ‫ش‬ |                                   ‫کاهیکوچسوفندان در غول جای من‬ | ‫کاهی چو غول کرد بیابان دوان دوان ]‬ |  |                                   ‫اسیفو ل‬ |                                             ‫بذرقطونا بود [بهرامی گوید ‪۱‬‬ |                                        ‫نیارمبخانه هیچ 
---
LEAF 352 ماغ
                                 ‫‪۳۳۳‬‬ |  |     ‫تابرد مراسب را اگورم گرم‬            ‫اسپیل آمد آنکه نرم رم‬ |                                 ‫صندل‬ |  |                                           ‫چندن ‪ ۲‬بود» لولوی کوید ‪:‬‬ |  |                               ‫بریل ‏(‪)٩‬‬ |                                        ‫کوهی است عظیم » رفیهی گوید ‪:‬‬ |                        ‫رودست همچو جبحون‬              ‫ت‬‫دز‬ |                                                        ‫وه ای‬ |                                                            ‫جفقطر‬ |                                                                ‫هر‬ |  | ‫هر ذه‌رای حزلمت کوهیست چون بزیل )‪(٩‬‏‬ |  |                                  ‫برطایل‬ |  | ‫جز بری همه جای شادی و کام‬              ‫که خوانند بر طایل آنرا بنام‬ |  |  |                                  ‫رل‬ |     
---
LEAF 419 مغاك
                              ‫‪۰۶.‬‬   ‫ف‬ |  |  |  |  |                         ‫" کنون باشد که برخوانم بپیش تو بشعر آندر‬ | ‫هر آنچه تو بخافانان وطرخااند خان کردی‬ |  |                          ‫طفاج خات‬ |                                                     ‫یادشاده سمرقند نود‬ |  |  |                               ‫عمقان‬ |                                            ‫نامکیراست » عسحدی کوید‪:‬‬ |                             ‫بجنبانم علم چندان درون گدنربد سیمین‬ | ‫فروریزدش درتله‬    ‫که سیماب از سر حمدان‬ |  |                                 ‫سن‬ |  | ‫عشقه بود که بر درخت بیچد » _سر ند و کشو ر نیزگویند» رودکی‬ |  |                                                                ‫گوید ‪:‬‬ |  |  |   ‫بیچد سن‬   ‫راست چون بدررخت‬             ‫بر خواجه بیچده رفتن‬    ‫هست‬ | ‫چشم را از خن‬     ‫شعر از شعر و‬           ‫تر که می نداند او‬ 
---
LEAF 539 ماغ
                                       ‫‪۰۴۱‬‬ |  |  ‫وتش بخار‬ |         ‫سمن بوی شد باد آ‬                              ‫کل انبوی شد لاله ایدر مکر‬ |  |  | ‫‌انخكفته بود [ بوشکور کوید |‪:‬‬ |                             ‫یندب‬ |                                ‫لموکوب‬ |                                     ‫کعوا‬ |                                        ‫بانك پای‌بودنرم نرم و‬ |  ‫زن‌از خواب شلیوی م‌دی‌شنود‬                               ‫توانگربنزدیك زن خفته‌بود‬ |                                                             ‫یعنی آواز نرمپایشنود ‪.‬‬ |  |                                        ‫‪۲‬‬ |                                            ‫کی‬ |                     ‫پیهبودکهوزد گویند و بتازی شحم [ خحرته گوید ‪:‬‬ |   ‫بپی گرپیختی توبی روسپی ]‬                           ‫ماغرمج آبی؟ ببختی بیی‬ |                        
---
LEAF 558 ماغ
                                          ‫‪۶:۰‬‬ |  |              ‫حنیور ‪۰۰۱‬‬                       ‫! حفغان ‪۸۹۳‬‬ |                                                             ‫س‬                 ‫حال ‪۸۱۳‬‬ |                  ‫‪ .‬حول ‪۲۳۲‬‬                  ‫| حغائه ‪۸۹41‬‬                    ‫حالاق ‪۰:۲‬‬ |             ‫ا حوک ‪۷۹۲‬‬                                ‫حغْد ‪۱۸‬‬        ‫حالاک ‪۰۲۰۱۹۲۰۰۰۴ ۰‬‬ |                   ‫چینه‪۰۰۰‬‬                   ‫حغز ‪۱۷۱.۰‬‬                       ‫حالندر ‪۱۰۱‬‬ |  |                                                                          ‫حام‌حام ‪۹۹۳‬ص‬ |                                                             ‫ب‬   ‫‪۱‬‬ |                                                 ‫‪۱۰‬‬      ‫ی‬       ‫(‬ |             ‫ح‌‬ |                   ‫‪ .‬حالا ه ‪۱‬ء‬     
---
```


## [2026-09-07T01:42:43.526Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,60p tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-07T01:42:43.568Z] TOOL RESULT

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


## [2026-09-07T01:42:53.465Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://en.wiktionary.org/wiki/ماست\" \"https://en.wiktionary.org/wiki/ماهی\" \"https://en.wiktionary.org/wiki/مست\" \"https://en.wiktionary.org/wiki/ملخ\" \"https://en.wiktionary.org/wiki/میگو\" \"https://en.wiktionary.org/wiki/مغاک\"; do python3 tools/fetch_source.py \"$u\" --note \"page 317, roots Mad / Madhaxa / Maga: Persian nodes mast, mahi, mast(yogurt), malax, migu, magak\" ; done",
 "description": "Fetch Persian Wiktionary pages"
}
```


## [2026-09-07T01:42:55.547Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://en.wiktionary.org/wiki/myna\" \"https://en.wiktionary.org/wiki/mate\" \"https://en.wiktionary.org/wiki/meat\" \"https://en.wiktionary.org/wiki/matte\" \"https://en.wiktionary.org/wiki/mattus\" \"https://www.etymonline.com/word/myna\" \"https://www.etymonline.com/word/matte\" \"https://www.etymonline.com/word/mate\"; do python3 tools/fetch_source.py \"$u\" --note \"page 317 root Mad: English nodes myna, mate, meat, matte; Latin mattus\"; done",
 "description": "Fetch English etymology pages"
}
```


### [2026-09-07T01:42:57.799Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/275e17911d3fcb06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1f14c54e7af76820.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a24ba24e721da4b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6a3648c5420df193.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1fdae5615eafe1e8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1b63b301fad72a0b.txt
```


### [2026-09-07T01:43:06.487Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8ea1ce126adb563f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/db0fffadd67848d8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/263fec1bd1a25f3b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b0a09fc32011b708.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c2393ed42c12686b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f75bf21881ed561e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb43af56372afc0f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a2df186535c20fce.txt
```


## [2026-09-07T01:43:10.164Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 275e17911d3fcb06 1f14c54e7af76820 a24ba24e721da4b7; do echo \"########## $f\"; grep -n -A6 -m3 \"Etymology\" $f.txt | head -60; done",
 "description": "Read wiktionary mast/mahi/mast"
}
```


### [2026-09-07T01:43:11.334Z] TOOL RESULT

```
########## 275e17911d3fcb06
62: Etymology 1 
63-
64- 1.1.1 
65- Noun 
66-
67- 1.1.1.1 
68- Declension 
--
71: Etymology 2 
72-
73- 1.2.1 
74- Verb 
75-
76- 2 
77- Central Kurdish 
--
82: Etymology 
83-
84- 2.2 
85- Noun 
86-
87- 2.2.1 
88- Descendants 
########## 1f14c54e7af76820
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 2 
68- Ottoman Turkish 
--
73: Etymology 
74-
75- 2.2 
76- Noun 
77-
78- 2.2.1 
79- Derived terms 
--
93: Etymology 
94-
95- 3.2 
96- Noun 
97-
98- 3.3 
99- References 
########## a24ba24e721da4b7
70: Etymology 
71-
72- 2.2 
73- Noun 
74-
75- 2.3 
76- References 
--
84: Etymology 1 
85-
86- 3.1.1 
87- Adjective 
88-
89- 3.1.1.1 
90- Descendants 
--
93: Etymology 2 
94-
95- 3.2.1 
96- Noun 
97-
98- 3.2.1.1 
99- Descendants
```


## [2026-09-07T01:43:16.723Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 275e17911d3fcb06 1f14c54e7af76820 a24ba24e721da4b7 6a3648c5420df193 1fdae5615eafe1e8 1b63b301fad72a0b; do echo \"########## $f\"; grep -n \"From \\|Borrowed\\|Proto-Iranian\\|Proto-Indo\\|Middle Persian\\|Avestan\\|Sanskrit\\|inherited\" $f.txt | head -25; done",
 "description": "Extract etymology lines"
}
```


### [2026-09-07T01:43:18.160Z] TOOL RESULT

```
########## 275e17911d3fcb06
211: From Wiktionary, the free dictionary
221: Borrowed from Classical Persian مَاسْت ( māst ) , from Middle Persian [Book Pahlavi needed] ( m’st' /⁠māst⁠/ , “ yoghurt ” ) , ultimately from Classical Syriac ܡܣܬܐ ( mastā ) .
308: From Classical Syriac ܡܣܬܐ ( mastā ) .
328: Borrowed from Classical Persian مَاسْت ( māst ) , from Middle Persian [Book Pahlavi needed] ( m’st' /⁠māst⁠/ , “ yoghurt ” ) , ultimately from Classical Syriac ܡܣܬܐ ( mastā ) .
410: Inherited from Middle Persian [Book Pahlavi needed] ( m’st' /⁠māst⁠/ , “ yoghurt ” ) , from Classical Syriac ܡܣܬܐ ( mastā ) . 
461: Arabic terms derived from Middle Persian 
478: Ottoman Turkish terms derived from Middle Persian 
487: Persian terms inherited from Middle Persian 
488: Persian terms derived from Middle Persian 
499: Hidden categories: Requests for Book Pahlavi script for Middle Persian terms 
########## 1f14c54e7af76820
215: From Wiktionary, the free dictionary
225: From Proto-Indo-Iranian *mátsyas . Cognate with Persian ماهی ( māhī ) . 
240: Borrowed from Persian ماهی ( mâhi ) .
293: Borrowed from Classical Persian مَاهِی ( māhī ) .
357: Proto-Indo-Iranian *mátsyas 
358: Proto-Iranian *mácyah 
359: Middle Persian [script needed] ( mʾhyk' /⁠māhīg⁠/ ) 
362: Inherited from Middle Persian [script needed] ( mʾhyk' /⁠māhīg⁠/ ) , from Proto-Iranian *mácyah , from Proto-Indo-Iranian *mátsyas , possibly borrowed from the BMAC substrate . Cognate with Younger Avestan 𐬨𐬀𐬯𐬌𐬌𐬀 ( masiia ) , Sanskrit मत्स्य ( mátsya ) .
402: Proto-Indo-European *meh₁- ? 
403: Proto-Indo-European *mḗh₁n̥s 
404: Proto-Indo-Iranian *mā́Has 
405: Proto-Iranian *mā́Hah 
407: Middle Persian 𐭡𐭩𐭥𐭧 ( byʿḥ ) 
410: Middle Persian yḥ ( īh ) 
412: Middle Persian ig 
418: From ماه ( mâh ) + ـی ( -i , suffix forming adjectives ) .
439: Categories : Laki terms derived from Proto-Indo-Iranian 
458: Persian terms inherited from Proto-Iranian 
459: Persian terms derived from Middle Persian 
461: Persian terms derived from Proto-Indo-Iranian 
462: Persian terms inherited from Proto-Indo-Iranian 
463: Persian terms derived from Proto-Iranian 
464: Persian terms inherited from Middle Persian 
469: Persian terms derived from the Proto-Indo-European root *meh₁- 
470: Persian terms derived from the Proto-Indo-European word *mḗh₁n̥s 
########## a24ba24e721da4b7
232: From Wiktionary, the free dictionary
254: From Ottoman Turkish مست ( mest ) .
279: Borrowed from Classical Persian مست ( mast ) .
296: Borrowed from Arabic مِسْح ( misḥ , “ haircloth ” ) .
329: Proto-Indo-European *meh₂d- 
331: Proto-Indo-European *-tós 
333: Proto-Indo-Iranian *matˢtás 
336: Inherited from Middle Persian 𐭬𐭮𐭲 ( mst /⁠mast⁠/ , “ drunk, bemused ” ) , from Proto-Indo-Iranian *matˢtás ( “ drunk, intoxicated ” ) , from Proto-Indo-European *meh₂d- ( “ wet ” ) . Cognate with Sanskrit मत्त ( matta ) .
505: Borrowed from Classical Persian مست ( mast ) .
571: Persian terms derived from Proto-Indo-Iranian 
572: Persian terms inherited from Proto-Indo-Iranian 
573: Persian terms derived from Proto-Indo-European 
574: Persian terms derived from the Proto-Indo-European root *meh₂d- (wet) 
575: Persian terms inherited from Middle Persian 
576: Persian terms derived from Middle Persian 
577: Persian terms inherited from Proto-Indo-European 
########## 6a3648c5420df193
150: From Wiktionary, the free dictionary
164: From Middle Persian *malax (written as Pazend 𐬨𐬀𐬮𐬀𐬐 ( malak ) ), borrowed from Bactrian μαλαχο ( malakho ) , from Proto-Iranian *madaxa , itself probably related to Sanskrit मटची ( maṭacī , “ locust ” ) . Compare Avestan 𐬨𐬀𐬜𐬀𐬑𐬀 ( maδaxa , “ grasshopper ” ) , Baluchi مدگ ( madag ) , مذغ ( maδaγ ) , Pashto ملخ ( malax , “ locust ” ) , Old Armenian loanword մարախ ( marax ) , Ossetian мӕтых ( mætyx ) , Khwarezmian مثخ ( mθx ) . The inherited Southwestern Iranian form is میگ ( meyg ) (> میگو ( meygu , “ shrimp, prawn ” ) ); the wide phonetic variation in the word's relatives is induced by the taboo of the inauspicious locust.
242: Categories : Persian terms inherited from Middle Persian 
243: Persian terms derived from Middle Persian 
245: Persian terms derived from Proto-Iranian 
254: Hidden categories: Middle Persian terms with redundant transliterations 
########## 1fdae5615eafe1e8
133: From Wiktionary, the free dictionary
141: From Middle Persian [script needed] ( mdk' /⁠ma(y)ik⁠/ ) , from Proto-Iranian *madika , a variant of Proto-Iranian *madaxa ( “ locust, grasshopper ” ) , and thus related to ملخ ( malax ) ; see there for further information.
143: The second component is from Middle Persian [Term?] ( /⁠-ūg⁠/ , “ -like ” ) .
161: Categories : Persian terms inherited from Middle Persian 
162: Persian terms derived from Middle Persian 
163: Persian terms inherited from Proto-Iranian 
164: Persian terms derived from Proto-Iranian 
170: Hidden categories: Requests for native script for Middle Persian terms 
171: Middle Persian term requests 
########## 1b63b301fad72a0b
141: From Wiktionary, the free dictionary
149: From مَغ ( maġ , “ hole ” ) +‎ ـاک ( -âk ) , from Middle Persian mγ ( maγ , “ hole, pit ” ) .
236: Persian terms inherited from Middle Persian 
237: Persian terms derived from Middle Persian
```


## [2026-09-07T01:43:37.855Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '395,440p' 275e17911d3fcb06.txt; echo \"#### syriac mastā\"; sed -n '300,320p' 275e17911d3fcb06.txt",
 "description": "Read Wiktionary Persian māst"
}
```


### [2026-09-07T01:43:37.906Z] TOOL RESULT

```
 Dari reading ? 

 māst

 Iranian reading ? 

 mâst

 Tajik reading ? 

 most

 Etymology 1
 [ edit ] 

 Inherited from Middle Persian [Book Pahlavi needed] ( m’st' /⁠māst⁠/ , “ yoghurt ” ) , from Classical Syriac ܡܣܬܐ ( mastā ) . 

 Noun
 [ edit ] 

 ماست • ( māst / mâst ) ( plural ماست‌ها ( māst-hā / mâst-hâ ) , Tajik spelling мост ) 

 yoghurt 
 ماست و خیار ― māst u xiyār  / mâst o xiyâr ― mast-o-khiyar , a cucumber and yoghurt side dish 

 Derived terms
 [ edit ] 

 ماستابه ( māstāba  / mâstâbe ) 
 ماستبا ( māstbā  / mâstbâ ) 
 ماست‌بند ( māst-band  / mâst-band ) 
 ماست‌مالی ( māst-mālī  / mâst-mâli ) 
 ماست‌موسیر ( māst-mūsīr  / mâst-musir ) 

 Related terms
 [ edit ] 

 ماسیدن ( māsīdan  / mâsidan ) 

 Descendants
 [ edit ] 

 → Arabic: مَاسْت ( māst ) 

 ‌ → Ottoman Turkish: ماست ( mast ) Turkish: mast 

#### syriac mastā
 third-person feminine singular past active of مَاسَّ ( māssa ) 

 Central Kurdish
 [ edit ] 

 Etymology
 [ edit ] 

 From Classical Syriac ܡܣܬܐ ( mastā ) .

 Noun
 [ edit ] 

 ماست ( mast ) 

 yogurt 

 Descendants
 [ edit ] 

 → Hulaulá: מַסְתַא ( masta )
```


## [2026-09-07T01:43:38.886Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"maya-\\|maγa-\\|mağa\" BRT.txt | head -20; echo \"-- Loch\"; grep -n \"'Loch'\\|,Loch'\" BRT.txt | head -20",
 "description": "Bartholomae maγa- hole"
}
```


### [2026-09-07T01:43:38.993Z] TOOL RESULT

```
4494:anumaya-  rsS
4509:•  j.  anu-maya-  Adj.  'mäh  machend,  blö- kend', vom  Schaf;  mit  pasaf-:  bis  kapta pasvS  °ya  .  .  nisirinuyHt  V.  14~  16;  — pasius  *g3r>bul  'yiie  V.5. 38;  —  koU. 'pecus  ovillum':  pasiui  °yche  pawm  Y.  2. 24.  A)  als  Subst  'Schaf:  hazanram "yanqm  frSvinuyJl  vtspanqmca  aitaisqm pasvqm  ,.  V./Äyo;  —  saUm  aspanqm.. /lazaanm  gavqm  ba^oarj  "yanqm  Yt  5. 2i;  0.3,  V.i'2.4;  —  niiinmn  staor?m bisazy.lt  "malm  anj5  V.  7. 43;  43;  — 'yanqm  arsnqmV  .22.20.  a)  sva. 'Schaf- fleisch': hazat3nm  gSus  j^anüiiiqm  (sd.) baivan  'yanqm  H.;.s'*.
10007:jam-^^,  ^w-'',  j}m-^'>  :  gtn-,  g»m-.  ga-, 3  'gtma-,  "jma-,  4  b  (Kaus.)  jama-"'', 14  jasa-,  16  (Des.)  *jiha-^l,  30  (Kaus.) jämaya-;s- k.01.  i  jingh-, jatgA-*^ ;  Perf.  i >)■«-,  PfPr.  jajma-i\  —  PPfP.  jo/a-, gmata-''^,  yfmala-^'>;  lai.gatse,  *gat.tf,  *gai.- tsi,  °jime.  [S.  noch  "ttpaJanärsAa.]
10060:mit  «r  1)  'herab-,  herunterkommen'; a)  absolut:  yat  lialna  (sd.)  nijasäni  ax»tn bri^rS  Yt,  15.28;  —  ya%a  nä  snaiüis asne  niymat»m"^  paiti  vaSnSit  .  .  "wie wenn  einer  eine  Waffe  nahe  (auf  sich) herunterkommen  sieht . .''  P.  21,  b)  mit Dat.  'zu  . ,':  fravasayü  . .  yä  ..  pisanithu taoa  nijas»ti  xsttvtwyd  ".  .  die  damals  zu den.W,  ..herabkamen"  Yt./y.37.  2) 'in einen  Zustand  (Akk.)  gelangen':  aet^a  .. näirika  .  .  apu'^rTmlsÄ.)  nijasät  usustana V.5.45;  Vd,  ;p.  3)  absolut  'zu  Ende kommen,  den  Abschluss  erreichen':  akra mäi  fra/asaiti  baxia  (sd.)  <^at  nijasaiü V,5.8"'.        [S.  noch  nijämaya-,  No.  i.]
14683:•  j.  9-ri.zar9maya-  i)  Adj.  'drei  Frühlinge umfassend':  yS  'malm  ratüm  aiwyänkqm (sd.)  nBit  aiwyästi  V,  s8. 9.  a)  n.  'Zeit- raum von  drei  FrUblingen  (sva.  Jahren)': 'maOn  xratOm  asavanfm  aiwyäiahal  (sd.) N.Ji.
15856:•  j.,  g.  pasav-  -.ßav-  m.  'Vieh,  domestizirtes vierfüssigcs  Tier,  Haustier',  Sing,  auch  kolL : azsm  .  .  tJ  nipayanl .  .  ya^a  'sßm  pasa.- vastr?m  (sd.)  Vtj.  89;  —  ki  mH  'sSui ^ mS  nä  >rat3  vists  .  .  axdä  (sd.)  .  .  Y. 50.1;  — /su  F.5(?)";  —  im  Gegensatz 2U  nar-  oder  vira-:  'svamca  naramca  Y. 4-  S  i  —  y^  "^J  'P^  •  ■  °fli»t  vä  narim vä  raiiyät  W. 13.^1;  32;  —  västryehys •sSui  vTräatiä  (sd.)  Y.  JJ.  1 5 ;  —  va/  virpt^ ahmäksng  frada^ai  (sd.)  J  Y.  4:5.  9;  — pairT  'sUs  pain  vlrSng  dadtmahl  Y.  JÄ 6.  a)  in  Dual  Verbindung  mit  vJra-  (sd., audi  fdSt):  -j*  vlra  *Yt.  y.  iz  usw.;  — 'Tirä  Wrayi  Vr.7.3usw,;  —  'subya  vTraäbya V.6.^2.  A)  insbes.  vom  Kleinvieh,  den Schafen  und  Ziegen,  im  Gegensatz  zu staora-  (sdj:  -svamca  staoranameä  masyl- nqmca  sünqmla  vayqmca  V.  2.8;  10,  Äiz, 13;  —  °vasca  (als  NP.)  staoräea . .  masyäca bmngra  Yt.5.89;  Äs,  V.2.8,  9,  11,5.5, 6,  15;  —  °sv5  (AP.)  staeräca  V.  p.  39=;  — •subya  staoralibya  vayafibya  patantaäbya (sd,)  YL  /o.  119;  —  's}ul*g?ribui  ysistahe (sd.)  A.J.  3;  — -pania-dasa  °svs  sraoni.masa F. 25b(?); —  *hvBiSa^a{&A.)  'sus./iva^'> N.  5>V;  —  mit  anumaya-  (sd.):  ustrahe  . . aspahe  .  .  gSuI .  .  mtfnumat  ap?r3näyBk»in yaoida^S  °sSul  ^g^nbus  anumayeke  V.  9. 38 ; 2.  24;  —  bis  hapta  "vö  (AP.)  anumaya  . . fiissrinuyäi  V,  i4- 16.  a)  spez.  als  Opfer- tier: zadhrä  hE ushärayfti .,'sum  hl pacaym
17259:•  j.  bi.xiapar-''  n.  'Zeit  von  zwei  Näch- ten', wobei  i)  Nacht  im  Gegensatz  zu Tag  gilt:  bi.ayarsm  •rpm'''  tanäm  framaya- yanta  "während  zweier  Tage  und  Nächte  .." Yt.  jo,  132.  2)  Nacht  als  Zeit  von Sonnenuntergang  bis  Sonnenuntergang: agta^a  .  .  tanüm  nidai^yqn  °r^m'*  vä %ri.xSapar?m  vä  ". .  auf  die  Dauer  von zwei  oder  drei  Tagen"  V.5. 12.
18586:•  j.,  g.namV,'sich(weg)beugen'.  Praes.3 tuma-,  3  °nma-,  4  näma-,  30  (Kaus.)  »3- maya-.  —  PPfP.  *'nala-;  Inf.  nsinSi.
19126:*ni-)äma'  m.  •puerperium' ') ;  vgl.  lit.  gimli 'geboren  werden',  apr.  gemlon  'gehären'.  — ')  Mm  kann  nijämaya-  auch  als  Pries.  30 (Kaus.)  lu  »fam-  (apr.  gtm-ton)  mit  ni  fassen. Der  Zusammenstellung  mit  si.  nigäahät  RV. /O.  10.  \3.  widerspricht  die  Bedeutung.
19658:•  j.  mai8yöi.zar9maya-')  m,  Name  der Gottheit  der  ersten  Jahreszeit  und  des  an deren  Ende  gefeierten  fünftägigen  Fests*> (mit  dem  letzten,  45.  als  Haupttag):  'maem Payanhim  (sd.)  alavansm  alahe  ratäm  Vr. 2.3;  Y.2.9,  A.^,  3;  —  'mayehe  payaahö Vr.  1.  3;  A.3.  a;  —  'mayäi  Y.  J.  9;  — pagiryeheca  na  myazdahe  a&siti  (sd)  .  .yai •mayehe  A.^.  7;  — pan^^a  ^a%war)iafom •mayehe  alaAe  vaAistahe  da%usö  "45  [Tage sin<^  bis  zum  (Haupt)tag]  des  M.  [im Monat]  AV.  [am  Tag]  des  Schöpfers" A.^.?.
20271:•  j.,g.  (,p.)  'mä(y)- V,  'messen'.  Fraes. 27 maya-;  Perf.  i  mim-.  —  PPfP,  'mita-, •mlta-,  maia-,  PFP.  'mi^wa-,
24830:•  j.  rao^a-  n.  'Butter',  mit  *taramaya- Adj.  'Friihlingäbutter',  Bezeichnung  der Speise  der  Seligen:  i^ari%aiiqm  hi  barg- tqm  (sd.)  *zaramayeAe  "nahe  tal  atti  yünS ..  hudalnahe  ifarüim  pasca  para.iristjm H.  2.18".
25031:rat,  erl,:  tut  m  djiasiän  eigön  und  kul  ral  , gespandän  ke.  —  J)  Pü.;  ratlh  (erl.;  awdiK)  , öhrmaid.  —  4)  Vgl.  zu  st3tä.ratav:  —  !)  Pü. ral,  erl.:  tardär  i  muri  kisän.  —  6)  PüErL dailawar  *ie  an  gu/t  iartan  Säyet.  —  7)  Pü. : raiihj,  erl.:  frärömhi;  a.  zu  ri^wyor.  — ^)  Uzw,  zu  A.  im  Gegensatz  zu  den  beim GäiäHiärfest  beteiligten  Laien  (raiimaya-),  zu N.  -  als  Zelebrant  -  im  Gegensatz  zu  dem  - als  Ministranten  -  verwendeten  Knaben.  — 9)  Pü.  (ta  Vr.  /.  i)  gibt  an,  wer  die  Ä.  der sieben  Klassen  sind;  nimlicb:  Birmazd-sara- luSl  -  iar  I  mäAii  -  iäiumai  -  iarsift  -  fehlt (Bd.  14.  9:  xargSl  i  Sär)  -  xariiiz.  —  »)  An den  Parallelstellen  S.  2.  6,  7  steht  amihm spitiUm  statt  wie  lu  erwarten™//;™. —  i')  Es ist  nicht  deutlich,  wer  damit  gemeint  isL  — ■»  S.  zu  den  33  R.  DsT.  ZA.  /.  13.  — I])  Pü.:  katär  ratikän  SSmurilnTk.  —  M)  Pü.: ahräklh  ral,  %\s..:  puayaguruh.
25168:•  j.  ram-  V.  'ruhen'.  Fraes.  4  räma-, 38  rSmya-,  30  (Kaus.)  rämaya-,
26542:Ytio.iig; —  myatdavä  ratui  amyasda- vamtit  ratunaim  vänmtum  (sd.)  ^rtm  fra- ptnnaoiti  h.3. 10;  —  mtjmfm  (bz.  mah»- mam,  ayrTm)  'r?m  anjd  "um  den  Preis eines  Stücks  Gross vieh  vod  geringster (mittlerer,  bester)  Qualität)"  V.7.413,  43^ •)  Im  Gegensatz  lum  Kleinvieh  {pasmi-,  anu- maya-)  auch  zum  Ziehen.  Reiten  und  Lasten- tragen  lu  verwenden.  —  ••)  Sonach  derReihen- folEe  ihres  Werts,   s.  V.  /.  4a.
27971:•  j.  *zannaya-'',  zarjmaya-  m.  'Früh-' ling':  misti  urvaranam  xatri^aonanam °malm  paiti  ztm^a  *uzuxsyänti  Yt.7.4.
27973:•  j.  ■'"zaramaya-''  Adj.  'venius':  :far3~ %anam  hi  bantam  'yehe  raofnahe  (sd.) H.2'i8.
27974:Ableit.  au»  'xarmaya-  (mit  Verschiebung  des
30425:•  j.  'humayä-  f.  EN.:  s.  \mX.ex  humaya-,
-- Loch
26286:Zum  V.  jflÄ/.;  Bthl.IF.A2S3').  — Pü.:*ji;j^J* 'Loch'.  —  ")  Ich  nehme  jetzt  an,  <3ass  ir.  dm im  jAw.  «llgemein  m  nm  geworden  ist  (vgl, %  302.  2)  und  zwar  nach  der  Witkungsfrist des  Gesetzes  J  ^93-  !'»■  s.  sanman-.  ■*daii- mahi  läs^l  sich  als  Neubildung  nach  daiqaii usw.  fassen;  für  maimya-  kommt  der Einlluss von  ntaiitna-  in  Anschlag.  [Np.  Alma  ist jedenfalls  nicht  nach  GIrPh.  /  b.  92  ent- standen.]
```


## [2026-09-07T01:43:51.555Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"maga-\\|ma5a-\\|maSa-\\|ma6a-\" BRT.txt | head -20; echo \"-- Grube\"; grep -n \"Grube\" BRT.txt | head",
 "description": "Bartholomae maga/maδa"
}
```


### [2026-09-07T01:43:51.616Z] TOOL RESULT

```
19523:•  g.  maga-  m.  'Bund,  Geheimbund' '',  spez, von  der  mra^wZ/Hschen  Religionsgemein- schaft: aila  v3  mlzdim  (sd.)  anAal  aAya 'gahyä  Y.55, 7;  —  (wrayaäJ  (sd.)  'gitn tJm  y.53-T,  —  tarn  kavä  vT/dJs/S  'gahyä xsa^rä  nasal  •■yqm  ästJm  (sd.) . .  ". .  zu- gleich mit  der  Obherrschaft  über  den Bund.,"  Y.  51,  i6;  —  is  vä  vatahSus manaaks  aastä  'gäi  ^r^ivlf  (sd.)  Y.  57. 11; —  bes.  mit  mat-:  aj  mä  masa  ySzSm matdä  fräxsnTtß  rnaesi  'gäi  S  faHl.tänaiä (sd.)  Y.  2p.  1 1 ;  —  zara'hustra  kastS  asavä
19595:Zum  V.  ^mad:  —  ai.  soma-mäd-  Adj.  —  Pü.: mn^Ä^R  (Hds.  madd   und  mdndan   ann); Sa.i  vidyä. •  g.  *mada-,  j.  maSa-  m.  i)  'Rauschbe- geisterung' durch /fdOMJgenuss':  nXti  säire
19634:Ableit.  aus  maSa-;  ei g.  Adj,  —  i\.madya-n. — Pü. ;  kac  mai  ^atSn;  erl. :  miä  Garend  mast afi  bavind.
20567:'  wenn  sie  ins  künftige  Leben  kommen" Ylj.  25;  V.p.44;  —  cvat  aßimäi  naire 'dim  aakat  pas'a  astasca  baooattkasca vi.urvistim  "wie  grosser  Lohn  wird  dem Maime  werden  .  ."  V.  Ä  8 1 ;  A.  ^  4,  6;  — —  Ayai  'dim  *mavai'i:3M  (sd.)  /radadä^ä dam^byB  Y. 40.  \;  —  hyat  dairiä  vaMstl yli/^(sd.)  'dt  y.4g.g;  —  ..  iyat  *cfi,i/ts *'hudaby5  'dim  mazdä  yehyä  tu  dähnm I ".  .  zu  dem  Lohn,  der  den  Verständigen versehen  ward,  den  du,o  J/.,  festgesetzt  hastT V,^4.  13; —  hyat  'dim  zarä^ustrS  maga- vabyö  {&A.)  cdisf  para  Y.  5/.  15.  a)  mit Gen.  obj.:  yä  damä  vairJm  hanäi  'dim asahyä  yäsä  (sd.)  aslm  Y.  54. 1 ;  —  aicä vs  'dim  aahat  ahyä  magahyä  .  .ya'irä  . . "und  es  wird  euch  der  Lohn  dieses  Bundes werden . .  dort  wo  . ."  Y,  3^.  7 ;  —  disyät Ai  anAe  avat  'dim  parS.asnai  anuAe ya'ka  . .  "es  soll  ihm  dafUr  ein  so  grosser Lohn  Tür  das  künftige  Leben  zugesichert werden,  als  ob  . ."  A._j.  7,  aa)  zugleich
20592:•  j.  mustamaSa-  m.  'Myrte*:    'Id  F.  11. Ir.  *tnustainj-ta-1  Schwerlich  richtig  beieugf
-- Grube
2092:Chants  populaires ;  Chants  populaires  des  Afghans.     Paris   1890. Ersch-Gruber  Eniykl.;  ,.  Allgemeine  Encyklopidie  der  Wissenschaften  und  Kiinste.     Halle  und
6752:•  ).  a-ham.baoS^mna-  Adj,  'nicht  wahr-  Oberherm  und  Richter  und  als  den nehmend'  sva,  'der  seine  Sinne  nicht  zu  ersten  Lehrer  der  Menschheit"  Yt. /_J.  1 5  a ; brauchen  weiss'  (vom  Hund):  yat  ..  sfä\ —  ya^a  fr3  loa  (sd.)  ämraot  yat  dim •n<s  Tä  haiat  aoäitySjxratus  "wenn . .  ander- '  ahümca  ratutn^a  ääadat  "'ya^a'  sagt  aus, seits  ein  Hund  seine  Sinne  nicht  zu '  dass  sie  ihn  (näml.  Zar^  als  A.  und  R. brauchen  weiss,  der  (weil  er)  nicht  recht  eingesetzt  haben"  Y.Jfj.u;  Yt  7^.92;  — bei  Verstand  ist"  V.  /_J,  35;  —  yesi  nnl<yailqm  ns  ahurS  maeäh  .  .  vatsks  valaa spS  'nS  mafye  v3  .  .pai'jyäite  aAmai(sA.)\{sA.)  atiqm  zaraiustr5  ankuca  (NS.)'' heüa  irisylt  "sonst  könnte  der  Hund,  der  ratu^ca  Vi.iö.i;  Yt./j.gi;  —  allai  dim seine  Sinne  nicht  recht  zu  brauchen  weiss,  lUsfanam  maziit?m  dazäyli  (sd.)  ahümca in  eine  Grube  ..  geraten"  V.  j_j.  37.  .^ratämca  yim    ahunm    mazdqm    Y.  27.  i;
12787:a)  als  Akk.  ohne  Kiicksicht  auf  Numerus  und Genus*',  zurückweisend:  y5  .  .  vamäsca hqm.räzayäti  . .  srvaiia  . .  a%a  'im  *upa.- tagsayäH  *unähva  dim  rat?aya{%A^ca  V. 17,2; — srväbya  may>m  ava-kansis  ..paiti 'im  äbarsii  ".  .  für  die  Nägel  sollst  du eine  Grube  graben  . .  du  sollst  sie  hin- bringen" y.ij.T,  5;  —  sao%rä  ..  a%a yS  'im  *frahinHn  (sd.)  N.  68-,  —  hqm.- vaniflm  .  .  framm.narqm  .  .  yä  d°  (näml. narSuil)  jasaiti  bafs'baxttmcii  (sd.)  yä narqm .  .Nt.-j  .^.  b)  alsGen.'';  a)  zurück- weisend auf  ein  Relativ:  yas^a  ..  aparao- oayete . . pairi  'im  lanava  anm..urvän3m haca  vahistat  a»haoi  ".  .  procul  eius dislinebo..animama.."Y.jp.7">.  ß)  vor- ausweisend :  ÄS  ba  aisS  äs  .  .  yS  .  .  paiti.- hincaiti  ä  'im  nBit  apivatäite  dainayh  ,  .
19439:•  j,  "maeya-  m.  'Grube,  Kuhle"':  yai  nsii spa..'-]e  vä  iäili  vä . . paS>yäite  V.y.37,
19526:•  j.  'maj^-  m.,  mayä-  f.'>  'Loch  im  Erd- boden, Grube':  srvabya  (sd.)  'f»m  ava.- kanöis'V.iy.T,  5,  F.i7; —  baTvari  'yanqin (GPf)  irimaitinqm  aiühh  z?mö  aipt.kan- yät  V.  14. 6.  a)  insbes.  von  den  zu Zwecken  ritueller  Reinigung  gegrabenen Lochern":  mazdayasna  aiäAa  z?md  %rii (sd.)  'yjm  ava.kanay>n  dva  'fa  frasnä^aym malsmana  giul  *Bim  äp3  "die  Mazday. sollen  in  der  Erde  drei  Löcher  graben, zwei  Löcher  —  da  sollen  sie  mit  Rindsurin waschen  — ,  eins  —  mit  Wasser  — "  V.  76'.  1 2 ; Ä37; — paoirtm  upa  'fim  nt^w^>söis . . iitim  Ufa  . .  xltUm  upa  . .  "hrayS  anya  'ya ni^TVinssis  "ein  erstes  Loch  sollst  du  aus- stechen, ein  zweites  . .  ein  sechstes  . .  drei weitre  Löcher  sollst  du  ausstechen"  V. p.  6  ff.;  70. 18;  —  ^rJyS  yim  antari  vlta (sd.)  atitan  %räyS  {xh/as,  novo)  'ya  fra^ iärayBisY.g.  ii>;  11',  12,31; — arttanca (sd.)  .  .  'ya  (NP.)  V.p.  11;  —  karsascit frakäraySiS . .  ^ai  hala  'yaHbya  V.p.io; 29;  — paoirJfn  upa  *yim  frä.nasui  nanm (statt  NS.)  bavaiii  "am  ersten  Loch  . ." V.p.  28;  3iJ;  —  US  tansm  snayaSa  us vasirät  (statt  AP.)  gius  maSsmana  qpäca nava  (sd.)  upa  °ypm  "er  soll  seinen  Leib und  seine  Kleider  bei  den  neun  Löchern , .  waschen"  V.5.  54.
19528:Abieil.  —  np.  mal  'Tiefe',  vgl.  ma-ßk  'Grube'.
23999:•  j.  vi-tastay-')  f.  'Spanne'  als  Längen- mass'h  may?m  avaJeanBtl dl^lm  xrttidisme °tlm  vandusme  "eine  Grube  sollst  du graben,  eine  D.  tief  in  harter,  ebe  V. tief  in  weicher  Erde"  V.  /?.  S ;  —  'H  F.  8, 27a;  —  avaval  kaca  S^rat..ya%a  *fra- tara  *'tii*i  "soweit  weg  von  dem . .  Feuer als  eine  besonders  grosse  Spanne  ^  beträgt" V.  8.  76.
25264:KompE.—  Pü.:  veiak.  —  ')  'Wald'  von  den herningeiteckten  und  übergedeclclen  Banm- zwcigen,  die  die  Grube  verdecken  sollen;  ans der  JägerEpricbe.  -~  *)  Indem  er  im  Zng  der Rennbahn  jene  Fallgrube  anlegte.
```


## [2026-09-07T01:43:54.388Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/مغ\" --note \"page 317 root Maga: Persian mağ 'hole'\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/madaxa\" --note \"page 317 root Madhaxa: PIr *madaxa locust\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mátsyas\" --note \"page 317 node masya/mahi: PII *matsyas fish\"",
 "description": "Fetch more wiktionary"
}
```


### [2026-09-07T01:43:57.588Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6c3f3901f116afd0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7aedf4e5f987e146.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ce9e89debb89d082.txt
```


## [2026-09-07T01:44:08.431Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"###### مغ\"; grep -n \"From \\|Avestan\\|Proto-Iran\\|hole\\|Etymology\" 6c3f3901f116afd0.txt | head -30; echo \"###### PIr madaxa\"; sed -n '120,200p' 7aedf4e5f987e146.txt; echo \"###### PII matsyas\"; grep -n \"From \\|substrate\\|Descend\\|Avestan\\|Sanskrit\\|mad\" ce9e89debb89d082.txt | head -25",
 "description": "Read fetched pages"
}
```


### [2026-09-07T01:44:08.506Z] TOOL RESULT

```
###### مغ
62: Etymology 1 
77: Etymology 2 
147: From Wiktionary, the free dictionary
154: Etymology 1
157: From Middle Persian 𐭬𐭢𐭥 ( mgw /⁠mow⁠/ ) , from Old Persian 𐎶𐎦𐏁 ( m-gu-š /⁠maguš⁠/ ) .
214: Etymology 2
217: From Middle Persian mγ ( maγ , “ hole ” ) . Compare مغاک (mağâk, “hole, pit).
###### PIr madaxa
###### PII matsyas
71: Descendants 
130: From Wiktionary, the free dictionary
140: Unknown; possibly borrowed from the BMAC substrate , compare the lack of similarity with Western Indo-European *peysk- ( “ fish ” ) and Eastern Indo-European *dʰǵʰu- ( “ fish ” ) . [ 1 ] [ 2 ] Alternative theories link the term to Proto-Germanic *matiz ( “ food ” ) [ 3 ] , ultimately from Proto-Indo-European *meh₂d- ( “ to drip, ooze; grease, fat ” ) .
224: Descendants
228: Sanskrit: मत्स्य ( mátsya ) ( see there for further descendants )
232: Younger Avestan: 𐬨𐬀𐬯𐬌𐬌𐬀 ( masiia ) 
301: ^ Martínez García, Javier; de Vaan, Michiel ( 2014 ), Introduction to Avestan (Brill Introductions to Indo-European Languages; 1)‎ [3] , Brill, →ISBN , page 32 : “ *matsia̯- ‘fish’ ” 
307: Categories : Proto-Indo-Iranian terms borrowed from the BMAC substrate 
308: Proto-Indo-Iranian terms derived from the BMAC substrate 
321: Sanskrit terms with non-redundant manual transliterations
```


## [2026-09-07T01:44:17.245Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 8ea1ce126adb563f db0fffadd67848d8 263fec1bd1a25f3b b0a09fc32011b708 c2393ed42c12686b; do echo \"########## $f\"; grep -n \"From \\|Borrowed\\|Sanskrit\\|Proto-Germanic\\|Latin\\|mad\\|Etymology 1\\|Hindi\" $f.txt | sed -n 1,18p; done",
 "description": "Read myna/mate/meat/matte/mattus"
}
```


### [2026-09-07T01:44:18.430Z] TOOL RESULT

```
########## 8ea1ce126adb563f
157: From Wiktionary, the free dictionary
177: Borrowed from Hindi मैना ( mainā ) / Urdu مینا ( mainā ) , from Sanskrit मदन ( madana ) .
264: Hindi: मैना   (hi)   f ( mainā ) 
301: Sanskrit: शलाका   (sa)   f ( śalākā ) , शारिका   (sa)   f ( śārikā ) , सारिका   (sa)   f ( sārikā ) , मदन   (sa)   m ( madana ) 
331: Categories : English terms borrowed from Hindi 
332: English terms derived from Hindi 
335: English terms derived from Sanskrit 
368: Terms with Hindi translations 
386: Terms with Sanskrit translations 
########## db0fffadd67848d8
65: Etymology 1 
238: Etymology 1 
290: Etymology 1 
423: Etymology 1 
530: Etymology 1 
606: Etymology 1 
756: Etymology 1 
941: From Wiktionary, the free dictionary
969: Etymology 1
976: Proto-Germanic *ga- 
979: Proto-Germanic *matiz 
980: Proto-Germanic *matjô 
988: From Middle English mate , a borrowing from Middle Low German mate ( “ messmate ” ) (replacing Middle English mett , mette ( “ table companion, mate, partner ” ) , from Old English ġemetta ( “ sharer of food, table-guest ” ) ), from Old Saxon gimato , derived from Proto-Germanic *gamatjô , itself from *ga- ( “ together ” ) (related to German and Dutch ge- ) + *matjô (from *matiz ( “ food ” ) ), related to Old English mete ( “ food ” ) ). From the same Middle Low German source stems German Low German Maat ( “ journeyman, companion ” ) , German Maat ( “ naval non-commissioned officer ” ) . Cognates include Saterland Frisian Moat ( “ friend, buddy, comrade, mate ” ) , Dutch maat ( “ mate, partner, colleague, friend ” ) . More at Old English ġe- , English co- , English meat . Doublet of maat .
990: Compare typologically Latin compāniō (whence companion ) (< con- + panis + -ō ), Russian однока́шник ( odnokášnik ) (< одно- ( odno- ) + ка́ша ( káša ) + -ник ( -nik ) ).
1194: Hindi: साथी   (hi)   m ( sāthī ) , सहवासी   (hi)   m ( sahvāsī ) 
1307: Hindi: मित्र   (hi)   m ( mitra ) , सखा   (hi)   m ( sakhā ) , साथी   (hi)   m ( sāthī ) , बंधु   (hi)   m ( bandhu ) 
1350: Hindi: साथी   (hi)   m ( sāthī ) 
1444: Hindi: सम्भोग   (hi)   m ( sambhog ) 
########## 263fec1bd1a25f3b
86: Latin 
88: Toggle Latin subsection 
248: From Wiktionary, the free dictionary
265: Proto-Germanic *matiz 
271: Inherited from Middle English mete ( “ food ” ) , from Old English mete ( “ food ” ) , from Proto-West Germanic *mati ( “ food ” ) , from Proto-Germanic *matiz ( “ food ” ) , from Proto-Indo-European *meh₂d- ( “ to be wet; grease, fat ” ) .
275: Cognate with North Frisian Miit ( “ meat ” ) , Danish mad ( “ food ” ) , Faroese and Icelandic matur ( “ food, meal ” ) , Norn mader ( “ food ” ) , Norwegian Bokmål , Norwegian Nynorsk , and Swedish mat ( “ food ” ) , Gothic 𐌼𐌰𐍄𐍃 ( mats , “ food ” ) .
455: mad as a meat axe 
836: Hindi: गोश्त   (hi)   m ( gośt ) , मांस   (hi)   m ( māns ) , माँस   (hi)   m ( mā̃s ) , लहम   (hi)   m ( laham ) 
919: Latin: carō   (la)   f 
1083: Sanskrit: मांस   (sa)   n ( māṃsá ) 
1084: Vedic Sanskrit: मांस्   (sa)   n ( mā́ṃs ) , मास्   (sa)   n ( mā́s ) 
1094: Latin: mȇso   (sh)   n 
1292: Hindi: माँस   (hi)   m ( mā̃s ) , गोश्त   (hi)   m ( gośt ) , लहम   (hi)   m ( laham ) 
1306: Latin: carnis   f , carō   (la)   f 
1334: Latin: meso   (sh)   n 
1398: Hindi: गोश्त   (hi)   m ( gośt ) , माँस   (hi)   m ( mā̃s ) , लहम   (hi)   m ( laham ) 
1410: Latin: carnis   f , carō   (la)   f 
1438: Latin: meso   (sh)   n 
########## b0a09fc32011b708
184: Etymology 1 
216: Etymology 1 
270: Etymology 1 
390: From Wiktionary, the free dictionary
400: Borrowed from French mat .
679: From Old English meatte , meatta , from Late Latin matta , from Punic or Phoenician .
714: Etymology 1
717: Borrowed from Norwegian Nynorsk matte , from Middle Low German matte , from Latin matta . Displaced Danish måtte .
777: Etymology 1
876: Etymology 1
1069: Middle English terms derived from Late Latin 
1080: Norwegian Bokmål terms derived from Latin 
1102: Pali adjective forms in Latin script 
########## c2393ed42c12686b
57: Latin 
59: Toggle Latin subsection 
145: From Wiktionary, the free dictionary
147: Latin
161: Proto-Italic *madēō 
162: Latin madēre 
163: Latin *maditus 
164: Latin mattus 
166: Syncopated from *madĭtus (with subsequent assimilation of /dt/ to /tt/), from madēre ( “ be drunk, be wet ” ) , itself from Proto-Italic *madēō , from Proto-Indo-European *meh₂d- ( “ wet ” ) . Cognate of Sanskrit मत्त ( mattá , “ drunk ” ) .
171: ( Classical Latin ) IPA ( key ) : [ˈmat.tʊs] 
295: “ mattus ”, in Charlton T. Lewis and Charles Short ( 1879 ), A Latin Dictionary , Oxford: Clarendon Press 
303: Categories : Latin terms derived from the Proto-Indo-European root *meh₂d- (wet) 
304: Latin terms derived from Proto-Italic 
305: Latin terms inherited from Proto-Italic 
306: Latin terms derived from Proto-Indo-European 
307: Latin 2-syllable words 
308: Latin terms with IPA pronunciation 
309: Latin lemmas
```


## [2026-09-07T01:44:32.396Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in f75bf21881ed561e cb43af56372afc0f a2df186535c20fce; do echo \"########## $f\"; sed -n '1,10p' $f.txt; grep -n -i \"mattus\\|Arabic\\|Sanskrit\\|Old French\\|Hindi\" $f.txt | head -12; done",
 "description": "Read etymonline pages"
}
```


### [2026-09-07T01:44:34.107Z] TOOL RESULT

```
########## f75bf21881ed561e
URL: https://www.etymonline.com/word/myna
FETCHED: 2026-09-07T01:43:05Z
STATUS: 200
TITLE: Etymonline - Online Etymology Dictionary

Etymonline - Online Etymology Dictionary 

 Search 
 Log in 

########## cb43af56372afc0f
URL: https://www.etymonline.com/word/matte
FETCHED: 2026-09-07T01:43:06Z
STATUS: 200
TITLE: Matte - Etymology, Origin & Meaning

Matte - Etymology, Origin & Meaning 

 Search 
 Log in 

25: also matt, mat , 1640s, "lusterless, dull" (of a color or surface), from French mat "dull, dead surface," from Old French mat "beaten down, withered, afflicted, dejected; dull," which is perhaps from Latin mattus "maudlin with drink," from madere "to be wet or sodden, be drunk," from PIE root *mad- "to be wet, drip" (see mast (n.2)). Or the French word might represent a transferred use from chess of mater "to checkmate, defeat," from Arabic (see mate (v.2)).
32: "sheet of backing material," 1845, from French mat "dull surface or finish" (15c.), noun use of Old French mat (adj.) "dull, beaten down," for which see matte (adj.). The word has been confused with mat (n.1), especially as the latter was used late 19c. for "piece of thick paper or other material placed for ornament or protection immediately under the glass of a picture-frame, with the central part cut out, for the proper display of the picture." As a verb, "to mount (a print) on a cardboard backing," by 1965. Related: Matted; matting .
53: "fallen nuts or acorns serving as food for animals." Old English mæst , the collective name for the fruit of the beech, oak, chestnut, and other forest trees, especially serving as food for swine, from Proto-Germanic *masto (source also of Dutch, Old High German, German mast "mast;" Old English verb mæsten "to fatten, feed"), perhaps from PIE *mad-sta- , from root *mad- "moist, wet," also used of various qualities of food (source also of Sanskrit madati "it bubbles, gladdens," medah "fat, marrow;" Latin madere "be sodden, be drunk;" Middle Persian mast "drunk;" Old English mete "food," Old High German muos "meal, mush-like food," Gothic mats "food").
95: mid-14c., "marshal (troops), arrange (an army for battle);" late 14c., "put (things) in order, arrange; get (something) ready, prepare; equip, fit out, put clothing on; adorn, decorate," from Old French areyer, earlier areer "to put in order," from Vulgar Latin *ar-redare "put in
103: late 14c., salade, "raw herbs cut up and variously dressed," from Old French salade (14c.) and Medieval Latin salata, both from Vulgar Latin *salata, literally "salted," short for herba salata "salted vegetables" (vegetables seasoned with brine, a popular Roman dish), from fem. p
########## a2df186535c20fce
URL: https://www.etymonline.com/word/mate
FETCHED: 2026-09-07T01:43:06Z
STATUS: 200
TITLE: Mate - Etymology, Origin & Meaning

Mate - Etymology, Origin & Meaning 

 Search 
 Log in 

37: "to checkmate," c. 1300, from Old French mater "to checkmate, defeat, overcome," from mat "checkmated" (see checkmate (v.)).
42: in chess, "a condition of checkmate, the state of the king when he is in check and cannot move out of it," c. 1300, mat , from Old French mat , from mater "to checkmate" (see mate (v.2)).
56: c. 1300, "one who accompanies or associates with another," from Old French compagnon "fellow, mate, friend, partner" (12c.), from Late Latin companionem (nominative companio ), etymologically "bread fellow, messmate," from Latin com "with, together" (see com- ) + panis "bread" (from PIE root *pa- "to feed").
92: 1765, in chess, "position in which a player not in check has no available moves in his turn," from stale "stalemate" (mid-15c.) + mate (n.2) "checkmate." Middle English stale probably is from Anglo-French estaler "to stalemate" "standstill," which is related to Old French estal "
116: c. 1300, partiner, "a sharer or partaker in anything," altered from parcener (late 13c.), from Old French parçonier "partner, associate; joint owner, joint heir," from parçon "partition, division. portion, share, lot," from Latin partitionem (nominative partitio) "a sharing, part
120: "causing or attended by great fear, dreadful, awful," 1560s, from Latin dirus "fearful, awful, boding ill," a religious term, which is of unknown origin. Apparently a dialect word in Latin; perhaps from Oscan and Umbrian and perhaps cognate with Greek deinos "terrible," Sanskrit
```


## [2026-09-07T01:44:51.644Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### PHD\"; grep -n -i \"mast\\b\\|m'st\\|mahig\\|mʾhyg\\|malax\\|madag\\|maγ\\|mgw\" PHD_mackenzie.txt | head -20; echo \"### NYB mast\"; grep -n \"mast \\|māst\" NYB_vol2_glossary.txt | head -10",
 "description": "MacKenzie and Nyberg"
}
```


### [2026-09-07T01:44:51.709Z] TOOL RESULT

```
### PHD
2327: frasp [plsp I N farasp] roof·tree, bc:ull, mast.
2750: ham-gOhr [hmgwhl I M hmgwhr] of the same substance or nature,
2752:ham-aOnag [hmgwnk' I M hmgwng] likewise, so.
2911: h6mast [hwm)st ] various series of prayers.
3396:Imadag [NK[J < A nqb; m'tk l I (M m'yg), N mada] female.
3398:2madag [m'tk l I (M m'yg, N maya)] essence, substance.
3415:mahig [m'hyk I. M m'hyg, N mahi] fish; astr. Pisces.
3417:mahigan [B YRH-, m'hyk'n I M m'hyg'n, N miihiyan] month.
3435:mind                            54                           mast
3491:mast [mst l I = M, N ......,] bemused, intoxicated.
3492:mAst                             55                          mewag
3493:mAst [m'st IN . . . . ] curds, sour milk.
3588:·mowbed [mgwpt l I N mobad] Mazdean priest.
4697:stOn(ag) [stwn(k) , I M (stwn, N sutUn] colwnn, pillar, mast.
6062:bemused mast(og).                           blood xon.
6332: curds mast.                               decay pohisn.
6444:   widang.                              drunken mast(og).
6498:embrace agos, kanar.                         especial madagwar; v. special.
6501:empty tuhig.                                    madag, madayan, xwadih, uruspar.
6502:enchant afsudan.                             essential gohrig, madagig, madagwar,
### NYB mast
371:almast [°lm’st'] the hardest of the metals, possibly steel 7812. — Borrowed from Gr. &ókuxc; MPrs ’rm’s ‘steel’ (List 80); Paz. almäst, Skr v. pāņdarasika, accord- ing to West pändara-siksya *yellow-white erystal’; NP almäs ‘a diamond; a glass; sharp iron'. Bailey, ZP 134; Henning, BSOAS XII, 1947, 45.
1838:hamist [KHDH] 1. adj. all, total: Paz. xamast SGV IV,76. 89. XVI, 8.96, Skr. v. -prabhrti, -ādi in composition with the preceding w. *. . . and so forth’, denoting an undefined totality; v. the adv. — 2. to- gether, combined with hac to form a frame preposition: han yam hac pist ~ this cup together with its dish 92%; Dar- asrav hac Brdtroreš ~ D. together with B. 52%, — 1. Sup. of Av. (1773, 1803)
2421:a-mast ‘not intoxicated’ and (1447) vi- bayha-, explained in Phl by yuvat hac has mast ‘intoxicated without wine’; NP bang borrowed in Arab as banj. I main- tain my former interpretation, which Bthl. also had, seeing in this narcotic some sort of hemp, i.e. hashish. The full treatment of the question must be reserved for a special paper.
6339:almāst: ~
```


## [2026-09-07T01:44:52.809Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### HJB myna\"; grep -n -i \"mynah\\|myna,\\|maina\" HJB.txt | head -10; echo \"### AID\"; grep -n -i \"myna\\|maina\" AID.txt | head -5; echo \"### SOD locust\"; grep -n -i \"locust\\|ملخ\" SOD.txt | head -10",
 "description": "Hobson-Jobson myna, Sogdian locust"
}
```


### [2026-09-07T01:44:52.885Z] TOOL RESULT

```
### HJB myna
13674:MAINATO,s.  Tam.  Mai.  Afatn^^^ a  washerman  or  dhotay  (q.v.).
13675:1616.— "There  is  another  sect  of  GentUes which  they  call  Mainatoe,  whose  business it  is  to  wash  the  clothes  of  the  Elings, Bramins,  and  Naires;  and  by  this  they get  their  living ;  and  neither  they  nor  their
13677:0.  1542.— "In  this  inclosure  do  likevrise remain  aU  the  Landressesi  by  them  called Miqnuttea,  which  wash  the  linnen  of  the City  (Pequin),  who,  as  we  were  told,  are above  an  hundred  thousand."— Piato,  in Coaan,  p.  138.  The  original  (cap.  cv.)  has toao*  OS  mainatot,  whose  sex  Oogan  has changed.
13678:1564.— "And  thefarm  (reiula)of  mainatoa, which  farm  prohibits  any  one  from  washing clothes,  which  is  the  work  of  a  mainato, except  by  arrangement  with  the  farmer (Rendeuro).  .  .  .-^Tombo,  &c.,  53.
14317:1554. — "E  a  hum  naique,  com  seys  piaes (peons)  e  hum  mooad&o,  com  seys  tochas, hum  boy  de  sombreiro,  dous  mainatOB,"  &c. —Bctelhoy  Tanibo,  57.
15231:MYNA,  MINA.
15241:MTNA,  MIKA,  &c.  s.  Hind. maina.  A  name  applied  to  several birds  of  the  family  of  starlings.  The common  myna  is  the  Acridotheres  tristis of  Linn. ;  the  southern  Hill-Myna  is  the Gracula,  also  Euldbes  religiom  of  Linn. ; the  Northern  Hill-Myna,  Eulahes  inter- media  of  Hay  (see  Jerdon*s  Birds,  ii. Pt.  i.  325,  337,  339).  Of  both  the first  and  last  it  may  be  said  that  they are  among  the  most  teachable  of imitative  birds,  articulating  words with  great  distinctness,  and  without PollVs  nasal  tone.  We  have  heard  a wild  one  (probably  the  first),  on  a tree  in  a  field,  spontaneously  echoing the  very  peculiar  call  of  the  black partridge  from  an  adjoining  jungle, with  unmistakable  truth.  There  is a  curious  description  in  Aelian  {De Nat,  An.  xvi.  2)  of  an  Indian  talking bird  which  we  thought  at  one  time to  he  the  Myna;  but  it  seems  to  be nearer  the  81lftm&,  and  under  that head  the  quotation  will  be  found. [Mr.  M*Chrindle  (Invasion  of  India,  186) 18  in  favour  of  the  Myna,']
15247:S 664.—"  In  the  Duke's  chamber  there  is rd,  given  him  by  Mr.  Pierce,  the  surgeon, comes  from  the  East  Indys,  black  the greatest  part,  with  the  finest  collar  of  white about  the  neck  ;  but  talks  many  things  and neyes  like  the  horse,  and  other  things,  the best  almost  that  ever  I  heard  bird  m  my life."— Pepy#,  Diary ^  April  26.  Prof.  Newton in  Mr.  Wheatley's  ed.  nv.  118)  is  inclined  to identify  this  witl^he  Myna,  and  notes  that one  of  the  earliest  figures  of  the  bird  is  by Eleazar  Albin  (Nat,  Hist,  of  Birds,  ii.  pi.  88) in  1738.
19467:Prior  to  1419.  — "Et  debent  ad  dictum Wardemotum  per  Aldermannum  et  probos Wardae,  necnon  per  juratores,  eligi  Con- -stabnlarii,  Scayegeonn,  Aleconners,  Be- delle,  et  alii  Officiarii."— Zi6«r  AUnu,  p.  38. „  ''Sbrbmbnt  db  Soawageonn. Vona  jurrez  qe  vous  surverrez  diligientie- ment  qe  lez  pavimentz  danz  vostre  Garde «oient  bien  et  droiturelement  reparaillez  et nyent  enhanasez  a  nosance  dez  veysyns  ;  et <\Q  lez  chemyna,  ruwes,  et  yenelles  soient nettez  dez  nens  et  de  toutz  roaners  dez ordures,  pur  honestee  de  la  citee ;  et  qe tonts  les  chymyneys,  foumes,  terrailles soient  de  piere,  et  suffiaantement  defens- ■ables  encontre  peril  de  few ;  et  si  vous troYez  rien  a  oontraire  yous  monstrez  al Alderman,  issint  qe  I'Alderman  ordeigne pur  amendement  de  celle.  Et  ces  ne lerree— si  Dieu  vous  eyde  et  lez  Saintz."— Ihid.  p.  818.
25864:607a Maini^  6076 Mainato,  538a,  569a Mai's,  5366 Maistry,  5386,  1466 Maitre,  566a Maji,  6586 Majoon,    Maju,   Ma-
### AID
4553:Mina.  More  commonly  Myna.
4815:Myna.  [The  Mardthi  matna.]  The name  of  a   very  common  Indian  bird, a   kind  of  starling,  the  acridotheres tristis.  Other  varieties  are  the  dusky myna  (acridotheres  fuscus)  and  the Brdhmani  myna  (temenuchus  pago- darum).  The  eggs  of  all  three  are glossy  blue  or  greenish  blue,  and holes  are  used  for  nests  (S.  B.  Fair- bank).
### SOD locust
7256:Locust's  Leg.    Henning,  W.  B.  (ed).  A  Locust's  Leg; 
24288:VJ  1092;  Gersh.  Locust's  leg  83 
86384:TSP  13.22  n  p228,  14.10;  Gersh.  Locust's  leg
```


## [2026-09-07T01:45:08.428Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"madgu\\|mastu\\|Dickmilch\\|macun\" incoming/WLD/WLD_Bd2_pages.txt | head -20",
 "description": "Walde-Pokorny mad-"
}
```


### [2026-09-07T01:45:08.495Z] TOOL RESULT

```
15104:weitere iran. Worte fiir Dickmilch u. dgl., so np. mast „saure Milch", masl-
15558:wegen lit. mastuvas^ mdstas          meszczias „modicus", s. Trautmann 376,
```


## [2026-09-07T01:45:10.504Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### IEC mad\"; grep -n \"^mad-\\|mad- (1)\\|mastu\\|mad-, \\|madh-\" IEC.txt | head -20; echo \"### CHEUNG mad\"; grep -n \"\\*mad\\|mast-\\|masidan\" CHEUNG.txt | head -15",
 "description": "Mann and Cheung"
}
```


### [2026-09-07T01:45:10.572Z] TOOL RESULT

```
### IEC mad
10227:mad- (1) “feed; food". WP II, 232, 262-70, 689 Gk. cf. máza, Doric mádda, f. ‘cake’; Alb. cf. maj, pp: majmë “feed, fatten’ beside gur-máz, -mac, m. ('throat, jaws’, if. fr. *gur-, cf. guer-, and *madio-); Go. mats, Let, m. “food, meal’; MEG maz, gs mazzes, sn. id.; LG & Sw. mat, m. id.; ON matr, pl. matir, m. id. beside mata, f. id. C£. the extn. of type *madito- in W maeth, pl. -ion, m. ‘food’; Cor. meth, maid, m. id.: ON mettr, pp. ‘sated’, and the type *madmn- in MIr. mann, mand, s. ‘fodder’. Cf. madtos
10228:mad- (2) 'cut, break
10237:mad- (3) (madaio, eio, io) “get wet; be wet. WP II, 230 Skt. mádàmi, pp. mattáh “get drunk’; Gk. madáo, adj. mastós (1) “be wet"; hík-mas, gs -mados, f. ‘moisture’; hík-mazo ‘moisten’; Lat. madeó, ere "be wet; be drunk’; LG cf. matsch, m. ‘brew, mire’. (Uncertainly Arm. tamuk, adj. “damp”, if for metathetized *ma- tuk)
10238:mad- (? or mód-?) “sign, mark, shape, mould, stamp' Ir. (7) mádh, m. “luck, trump-card'; OE cf. metan, v. (2) ‘paint, design’; ON mót, n. (2) ‘figure, form, image, sign, mode’; Du. moet, f. mark scar’; Slovene cf. mad-lo, mad-ez ‘stain’; Srb. mad-ez ‘birthmark’
10239:madtós (maditós, mastos) ‘fed, fattened; food, fattening’. Cf. mad- (1) Skt. cf. mástu, n. ‘sour cream, whey’; Hind. mafthā, m. ‘buttermilk’; Per. māst ‘sour milk’; Arm. mať, o-st. ‘molasses, mash of grapes’; Alb. cf. i majtun ‘fattened, well-fed’; Gk. máza, mádda, f. ‘mash, cake’; Lat. mattea, f. ‘fodder, mast, fattening’: LLat. matteola, dim. ‘stitbit; W maeth, pl. ion, m. ‘nuture’; Cor. méth, maid, mat, m. id.; MHG mast, smfn. ‘fructification, fodder, mast’; OE mæst, m. (2) ‘mast, beechnuts, acorns’; Sw. mätt, adj. ‘sated’; mätta, v. ‘sate’. (The Gk. forms in- dicate a variant of type *masd- which may have given rise to Lat. mattea as a LW via Etruscan, with -tt- for Gk. -dd-, cf. sporta, palatium, cotoneus, *buxita; & -ittu-, dim. fr. -idion as a dim. suffix in Late Lat.)
10299:manà, o(n) ‘moon’. Cf. mens, menó, món-. WP II, 271 Gk. mëng, Doric mána, id. (OS màno, wm. id.; MHG mane, id.) mánà (2), see manos (1) mand- infixed form of mad- (1), q. v.
10364:mast- ‘food’, etc. see madtós, mad- (1) Maced. cf. mattue, f. “hash?
10427:medo (2) ‘treat, remedy’. Same as (1) (?). Cf. medos Av. mad-, mað- ‘treat, cure’; maóo0, m. *medi- cine, science’; Lat. medeor -éri ‘heal, remedy’; cf. re-medium ‘remedy’.
10689:mestos, à (variant of type madtós, mast-? Cf. mad- (1)) ‘food, fattening; fattened’. WP IT, 231 Gk. mestós ‘crammed’; MIr. mess ‘beech and oak mast’; Ir. meas, pl. -a m. ‘fruit, crop’; W mes, fpl. ‘acorns’; Br. méz, m. & coll. ‘acorn, acorns’; Cor. mes, f. as W; W cf. also mest, m. “portion of food’; Myc. cf. (queried) me(s)- tura(i) or me(s)tula(i) ‘farm-animals’. With variant vocalism MHG mast, usu. f. ‘fruit; rich soil; fodder, masť; masten, v. ‘grow
11139:monus “thinking, wise, intelligent; thought. Cf. mend (1) Skt. mánuh ‘wise; Li. manus ‘intelligent, thoughtful; cf. mastis, f. thought; mastus, maslus ‘pensive’
11219:mot-tis, mot-tos (analytical prototype of mostis, mostos, q.v. Cf. motos 1 & 2) Li. mastis, gs -ies, f. 'braid'; mastas, m. *yard- stick'. Cf. mastuvai, pl. (^weaver's frame”. To motos (1))
16035:skhadið ‘split, divide’. Cf. sKhaio. (Gk. & Alb. ambig.) Skt. skhade, mp. ‘cut, téar, kill; Gk. (ambig.) skházo, v. “slit, release, open up’; Alb. (am- big.) çaj, v. split". Phonol. either of maj, see mad-, or of daj, see dai-); E cf. shatter, v.; Latv. cf. skadrs, adj. ‘fissile’; (uncertainly to) MHG schetzen, v. “assess, tax’; schaz, sm. 'tri- bute, stint, quota’; OE sceatt, m. ‘property; tribute; wealth; rent’; ON skattr, m. (“proper- ty; tax’; -tt- unexplained)
### CHEUNG mad
12152:*NWIR: ? Tt. (Cha.) demas, (Ebr.) mäs/mas ‘to stick’ (or from *mad?) 
16779:*mad2 253 
16801:*mad! ‘to become intoxicated, joyous’ 
16813:*KHOTANESE: *mad- ‘to be intoxicated’ = SGS: 108 
16828:*mad ‘to curdle, coagulate’ 
16861:*SANSKRIT: Skt. mástu- (n.) ‘sour cream’ (< *mad-stu-) = EWAia П: 336 
37546:*mad-, 253 
41252:parmasidan, 180, 256 
55648:*mad 
55656:*mad', *yrad 
56026:*gar*, *Hané (s.v.), *mad’, 
56184:*mad
```


## [2026-09-07T01:45:18.542Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '16801,16880p' CHEUNG.txt",
 "description": "Cheung mad1 mad2"
}
```


### [2026-09-07T01:45:18.596Z] TOOL RESULT

```
*mad! ‘to become intoxicated, joyous’ 


*AVESTAN: Y Av. maö- ‘to become intoxicated, joyous’ — Liste: 42 
MED.; Pres. them.: INJ. Zeg YAv. madaite (N 30); Aor. s-: INJ. 35р. ? OAv. masata (Y 54.1); Caus.: 
pres. IMPV. 25р. YAv. maöaiian'ha (Vr 8.1) 


*MIDDLE PERSIAN: MMP mst ‘drunk, bemused; in rut (of animals)’ = DMMPP: 
232b 

*PARTHIAN: mst ‘drunk, bemused; in rut (of animals)’ > DMMPP: 232b 
*KHOTANESE: *mad- ‘to be intoxicated’ = SGS: 108 

*SOGDIAN: BSogd. mst’wny ‘drunkenness’, BSogd. mst-k’r’k ‘intoxicating’, MSogd. 
mst-k’ryy ‘intoxicating’ || (+ *us-) ? BSogd. am "ën ‘scent, perfume’ 

*NWIR: NP mast, Kurd. mast, Sang. mast, Nn. mas, Siv. mass (ppp.) ‘drunk’ 
*SANSKRIT: mad ‘to become exhilarated, intoxicated’ (RV+) = EWAia II: 299 

«PIE *med- ‘to be intoxicated, exhilarated’ (cf. Harðarson 1995: 225 ff.) = LIV: 423 
f. | Pok.: 694 f., 706 

*IE COGNATES: Gr. рестбс ‘saturated, full’, Lat. madeo ‘I am intoxicated’ 
*REFERENCES: DKS: 329, 339b; Werba 1997: 361; Cabolov 2001: 622 


*mad ‘to curdle, coagulate’ 
*MIDDLE PERSIAN: MMP m’s- ‘to coagulate, become hard’ = DMMPP: 227a 
Pass.: pres. SUBJ. 1sg. MMP m’syh’n 


*PARTHIAN: m’s- ‘to coagulate, become hard’. > A different meaning is also 
possible: ‘to swell up’ ?, cf. Kurd. (Sor.) masan/mase- ‘to swell up, inflate [intr.]’, 


Zaz. masayis ‘to swell up, become fat’ (*damH?). > DMMPP: 227a 
Perf.: SUBJ. 3sg. m’s’d 


*CHORESMIAN: Q The Chor. form. ’nb’zy- ‘to cause to curdle?’ (cf. Henning 1971: 
28b) is probably unrelated (s.v. *bad). 


254 *mag ? 


*NWIR: NP mäsidan/mäs- ‘to coagulate’, Bal. mast/mad-, (?) Kurd. mayin ‘to 
curdle’, (LW) Gz. mäs-/mäsä ‘to coagulate’, Khuns. mäs-/mäsidan ‘to become 
solid’, mäsn-/mäsnä (caus.) “to solidify, harden’, NP mäst ‘yoghurt’, Ard. maske 
‘butter’, Anar. maske, Soi mäsgä ‘fresh butter’, ? Tt. (Xoz.) mäs- ‘to stick [intr.]’, 
(Esh.) mäs- ‘to stick [tr.] 

*NEIR: Yghn. mayd- ‘to curdle’, Wa. moö-, mod-/mo6t- ‘to turn sour, curdle’, Oss. 
mast ‘bitter(ness)’, I. mæstæg ‘thick’, Pash. masts (pl. f.) ‘curds’, ? matar (m.) 
‘coagulated milk’ (-t- < ?), war-moláy ‘fermentation’, Ishk. mid ‘cream’, Sariq. moo 
‘buttermilk’ || (+ *ni-) Sh. (Baj.) nimäö-/nimost ‘to prepare cream and sour milk’, 
Sariq. патиӨ-/патиӨ ‘to turn sour’, Khf. nimöö ‘cream coagulated in a trough’, 
Yghn. nimodin ‘freshly fermented, boiling milk’ 

*SANSKRIT: Skt. mástu- (n.) ‘sour cream’ (< *mad-stu-) = EWAia П: 336 

9 The root is apparently Ш. It may be cognate with Arm. mac- ‘to coagulate’, except 
that -c- would need an explanation. 


*PIE — = LIV: – | Pok.: 694 f. 

*REFERENCES: KPF I: 253b; EVP: 48; IIFL II: 529a; Abaev, Slovar’ I: 103; Abaev, Slovar’ II: 76 f., 103; 
Yarshater 1969: 191; EVS: 43a, 49а; WIM I: 71; WIM II/1: 79; DKS: 329; Steblin-Kamenskij 1999: 235; 
Lecoq 2002: 609b, 619a; NEVP: 52; Shahbakhsh: s.v. mad- 


*mag ? ‘to offer, worship, glorify (vel sim.)’ 


*AVESTAN: OAv. mag- ‘to offer, worship (vel sim.)’ — Liste: 43 
Partic.: desid. OAv. mimayZo (Y 45.10)
```


## [2026-09-07T01:45:40.570Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/317.jpg 2>/dev/null; pdftoppm -f 317 -l 317 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg317 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render pdf page 317"
}
```


### [2026-09-07T01:45:42.630Z] TOOL RESULT

```
site/pages/317.jpg
total 316
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 21:45 .
drwx------ 3 sfmqrb sfmqrb  4096 Sep  6 21:35 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   175 Sep  6 21:37 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 50563 Sep  6 21:41 crop_boxes.png
-rw-rw-r-- 1 sfmqrb sfmqrb     0 Sep  6 21:39 iec_pages.json
-rw-rw-r-- 1 sfmqrb sfmqrb 56809 Sep  6 21:41 pg313.png
-rw-rw-r-- 1 sfmqrb sfmqrb 64584 Sep  6 21:40 pg314.png
-rw-rw-r-- 1 sfmqrb sfmqrb 49502 Sep  6 21:37 pg315.png
-rw-rw-r-- 1 sfmqrb sfmqrb 80390 Sep  6 21:45 pg317.png
```


## [2026-09-07T01:45:44.755Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg317.png"
}
```


### [2026-09-07T01:45:45.133Z] TOOL RESULT

```

```


## [2026-09-07T01:45:45.130Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T01:46:21.687Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '59100,59115p' FSD_vol1.txt; echo \"#### search FSD for mat: confused\"; grep -n \"mat,  confounded\\|mat, confounded\" FSD_vol*.txt | head",
 "description": "FSD mattus note"
}
```


### [2026-09-07T01:46:21.765Z] TOOL RESULT

```
The  casein-bearing  protelds  of  milk.  [<  L.  caseus,  cheese,  -f inogen.]
caseMaw",  etc.  See  under  case*,  n.
case'IIng,  1   kgs'lin;  2   cSs'IJng,  n.  (Prov.  Eng.]  A   skin  from an  animal  that  has  died  by  accident  or  violence.
Ca-scHa,  I   ka-zel'e;  2   ca-s61'a,  n.  A   musician,  friend  of Dante,  who  Introduced  him  in  his  Purgatory  as  one  of  a freight  of  souls  disembarked  In  purgatory  during  his  stay. cascMock",  etc.  See  under  case*,  n. case'matc,  1   kes'mSt;  2   cas'mat,  n.  1.  A   vaulted chamber  in  a   fortification  for  the protection  of  troops  or  ammuni- tion, etc.;  especialb’-,  a   bomb< proof  arch  in  the  masonry, with  embrasures  for  guns; also,  an  armored  screen or  bulkhead  on  ship- board, pierced  for broadside  guns.
2.  Arch.  See casement,  2:  er- roneous use.  [F.r
<   It.  casamatla,
<   casa,  (< casa),  house,  -fr
matta,  I.  of  malto.  Casemate  (sectional  view),
feeble,  false,  <   LL.  mattus,  dull,  <   Per.  mat,  confounded.)
—   case'matc«cat',riagc,  c.«gln,  or  c.«truck,  n.  A   car- riage, gin,  or  truck  for  use  with  a   casemate-gun.— c.*gunf n.  A   gun  mounted  In  a   casemate.
case'mat^cd,  1   kSs'met-ed;  2   cas'm&t-£d,  a.  Furnished with  a   casemate  or  casemates, casc'ment*,  1   kgs'ment  or  -mant;  2   cas'ment  (xiii),  n.
1.  The  sash  of  a   window  when  arranged  to  open  on hinges  at  the  side,  or  a   window’  arranged  with  such sashes;  also,  a   long  narrow  window’  or  light,  os  between tW’O  mullions;  loosely,  any  window.
Soul,  from  thy  casement  look.
Lope  de  Veoa  To-Morrow  tr.  by  Loncfellow,  1.  10.
2.  A   hollow  molding,  or  cavetto.  3.  A   case;  covering; incasemcnt.
Althouch  wheels,  axles,  levers,  move  within  tho  old  casements, tho  watch,  in  fact,  is  now.  ...
#### search FSD for mat: confused
FSD_vol1.txt:59108:feeble,  false,  <   LL.  mattus,  dull,  <   Per.  mat,  confounded.)
```


## [2026-09-07T01:46:23.103Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=23060 && NR<=23110' KLN_1966.txt | grep -n -o \"94[0-9]\" | head; echo \"--- markers\"; grep -n \"^94[0-9]$\\|  94[0-9]  \" KLN_1966.txt | sed -n 1,10p",
 "description": "Klein page markers"
}
```


### [2026-09-07T01:46:24.299Z] TOOL RESULT

```
31:946
32:947
--- markers
22961:940
22968:941
22996:942
22997:943
23042:944
23043:945
23090:946
23091:947
23142:948
23155:949
```


## [2026-09-07T01:46:34.366Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Per.  mat\\|Per. mat\\|matte\" FSD_vol2.txt | head -10; echo \"--- vol2 range\"; head -3 FSD_vol2.txt; grep -n \"^152[0-9]$\" FSD_vol2.txt | head",
 "description": "FSD vol2 mat entry"
}
```


### [2026-09-07T01:46:35.585Z] TOOL RESULT

```
420:doc'tor-ate,  1   dek'tsr-gt;  2   dac'tor-st,  v.  [-at'ed;  -ai'ing/  doc'u-ment,  n.  1.  A   manuscript  or  piece  of  printed h   t.  To  make  a   doctor  of  by  conferring  a   degree.  II.  i.  matter  regarded  as  conveying  information  or  evidences
441:Benton  . . .   was  an  enthusiastic  believer  in  the  extreme  Jeffer- sonian doctrinaire  views  as  to  the  will  of  the  majority  being  always right.  :   T.  Roosevelt  y.  if.  Benion  p.  121.  Ik.  la.  *   co,  1887.1 doc"tri-nalre',  ti.  1.  One  whose  views  concerning  po- litical and  other  matters  are  derived  from  theories, rather  than  from  facts;  one  who  arrit'es  at  a   conclusion
460:lively  short  period  owing  to  hostile  environment.— <1.  of  dod'ders,  1   dod'arz;  2   dOd'era,  n.  See  maliasmu.s:  an  old two  aspects  (Philos.),  an  ultimate  tlieory  respecting  the  dod'dlc,  1   dod'l;  2   dcid'l,  vi.  [Scot.]  To  walk  unsteadily;  tod- relation  of  mind  and  matter  which  assumes  that  the  mental  die.—  dod'dllsb,  a.
477:matter  regarded  as  conveying  information  or  evidence; as,  legal  or  political  documents.  From  a   special  point  of  view or  hi  inexact  use,  anything  that  contains  or  exhibits  record or  testimony  of  facts  or  events  In  the  form  of  marks,  signs, inscriptions,  or  the  like,  as  the  pictured  walls  of  an  ancient temple,  may  be  considered  or  spoken  of  as  a   document.
478:A   'document  ’   .   .   .   ia  an  instrument  on  which  is  recorded,  by means  of  letters,  fieurcs,  or  marks,  matter  which  may  bo  eviden- tially used.  F.  Wharton  Law  0/  Evidence  vol.i,  bk.  ii.  5   614,  p. 686.  Ik.  *   DRO.  1877,1
896:PoJii'boc,  1   dom'bok;  2   dunr'boc,  n.  Eng.  Hist.  A   code of  law’s  among  the  Saxons;  specif.,  tlie  compilation made  by  Alfpid  the  Great,  aljout  A.  D.  S.*38-h90,  from the  Bible  and  the  laws  t>£  former  Christian  kings  of England  with  .some  additions  of  hia  own,  relating  to matterg  both  civil  and  eriininal;  not  to  be  confounded with  DoMi3.SD.ty  Book,  IAS.,  doom=book,  <   dom,  doom, T- f/«r,  book.]  Donifin'ct;  lloine'boakf;  Hoom'bookf.
1369:Dos'si,  1   des'sl;  2   dds's'i,  Dosso  (1479?-1542).  An  Italian painter  of  Ferrara;  The  Four  Doctors  of  the  Church. aos"sler',  1   dos'’ye';  8   dOa''ye',  re.  [E.l  1.  A   brief.  3.  A collection  of  memoranda  and  documents  relating  to  some matter;  aa,  a   lawyer's  dossier  of  a   ease  in  court. dos"si-ere,  1   des'i-yar';  2   d6s''i-yar',  n,  (P.l  That  part  of  a suit  of  plate  armor  which  covers  the  back  from  the  neck  to the  waist.
1422:Pope  Imilations  of  Ueracc  satire  i,  I.  4S. 3.  To  turn  and  go  back  on  the  same  or  a   parallel  track; as,  the  fox  doubted  on  the  hunter.s;  the  .stream  doubles frequently.  3.  Print.  To  set  up  matter  a   second  time by  mistake;  make  a   doublet.  4.  To  apply  increased force  or  effort;  as,  he  doubles  to  his  work.  5.  Mil.  To proceed  at  doiible*quick  time.  G.  To  play  tricks;  prac- tise sleight  of  hand.  7.  [Eng.]  To  rebound:  said  of  a billiard-ball.  8.  Baseball.  To  make  a   two*base  hit. [   <   F.  doubler,  <   LL.  duplo,  <   L.  duplus;  .see  under noi’Bi.B,  a.l— to  double  up.  1.  To  share  with  another one's  qu.arters,  bed,  etc.  2.  To  double  a   stake  after  lo.ss. 3.  To  stoop  or  bend,  as  In  laugbter.  4.  Baseball.  To  com- plete a   double  play  upon.—  to  d.  upon.  A/il.  1.  To enclose  between  two  fires.  2.  To  turn  back  in  order  to
1517:2.  An  uncertain  or  unsettled  opinion;  a   matter  or  case of  dubitation;  hence,  also,  uncertainty  as  pertaining  to an  event  or  state  of  things:  question;  as,  I   shall  go  with- out a   doubt ;   there  was  a   doubt  in  his  mind.
1521:Syn2  disbelief,  distrust,  hesitancy,  hesitation,  InoreduUty, indecision,  irresolution,  misgiving,  perplexity,  question, scruple,  skepticism,  suspense,  suspicion,  unbelief,  uncertain- ty. Doubt  may  refer  either  to  matters  of  belief  or  to  matters of  practise.  As  regards  belief,  doubt  Is  lack  of  conviction:  dis~ belief  is  conviction  to  the  contrary;  unbelief  votera  rather  to  a settled  state  of  mind,  generally  accompanied  with  opposi- tion of  heart.  Perplexity  is  active  and  painful;  doubt  may  be quiescent.  Perplexity  presses  toward  a   solution;  doubt  may be  content  to  Unger  unresolved.  Any  Improbable  statement awakens  incredulity.  In  theological  usage  unbelief  saxd  skep- ticism have  a   condemnatory  force,  as  implying  wilful  rejec- tion of  manifest  truth.  As  regards  practical  matters,  uncer- tainty applies  to  the  unknown  or  undecided:  doubt  implies some  negative  evidence.  Suspense  regards  the  future,  and  is eager  and  anxious;  uncertainty  may  relate  to  any  period,  and be  quite  indifferent.  Misgiving  is  ordinarily  in  regard  to  the outcome  of  something  already  done  or  decided;  hesitation, indecision,  and  irresolution  have  reference  to  something  that remains  to  be  decided  or  done,  and  are  due  oftener  to  infir- mity of  will  than  to  lack  of  knowledge.  Distrust  and  suspi- cion apply  especially  to  the  motives,  character,  etc.,  of others,  and  are  more  decidedly  adverse  than  doubt.  Scruple relates  to  matters  of  comsoienee  and  duty.—  Ant.:  assurance, belief,  certainty,  conviction,  decision,  determination,  resolu- tion, resolve.—  In  doubt,  subject  to  doubt:  in  uncertainty. —   no  d.,  unquestionably.-  out  of  d.,  beyond  doubt.- without  d.,  with  certainty;  decidedly, doubt'ancet,  M.  Uncertainty.
--- vol2 range
FUNK  &   WAGNALLS
New  Standard  Dictionary
[Reg.  U.  S.  Pat.  Ofi.l  ■   J
6656:1525
```


## [2026-09-07T01:46:45.484Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6650,6660p' FSD_vol2.txt | cut -c1-300; echo \"#### grep mat entries vol2\"; grep -n \"^152[6-9]$\\|^15[0-9][0-9]$\" FSD_vol2.txt | head -20",
 "description": "FSD vol2 page 1525 context"
}
```


### [2026-09-07T01:46:46.674Z] TOOL RESULT

```
S.G
12.20
12.1
11.4
22.48
21 '.5
1525
14.52
1490
About  2400 4950 1549
About  2700 2375 1755
#### grep mat entries vol2
6656:1525
```


## [2026-09-07T01:47:03.068Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for w in matte myna mate; do python3 tools/fetch_source.py \"https://www.ahdictionary.com/word/search.html?q=$w\" --note \"page 317: AHD entry for $w (Nourai cites AHD:805 / AHD:867)\"; done",
 "description": "Fetch AHD entries"
}
```


### [2026-09-07T01:47:05.431Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/67cd3ea6f6278d25.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/72c584622c6ab927.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b08ceaf43b76a2e9.txt
```


## [2026-09-07T01:47:09.216Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 67cd3ea6f6278d25 72c584622c6ab927; do echo \"##### $f\"; grep -n -i \"French\\|Sanskrit\\|Hindi\\|Latin\\|Origin\\|mad\" $f.txt | head -12; done",
 "description": "Read AHD pages"
}
```


### [2026-09-07T01:47:10.487Z] TOOL RESULT

```
##### 67cd3ea6f6278d25
63: [French, curdled milk, matte, from feminine of obsolete mat , compact, from Old French, dull, from Latin mattus , stupefied; see MAT 2 .]
68: Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
##### 72c584622c6ab927
48: [Hindi main ā , perhaps from Sanskrit madana ḥ , from madana- , delightful, joyful, from madati , it bubbles.]
53: Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
```


## [2026-09-07T01:47:55.615Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\n# find page markers\nfor i,l in enumerate(lines[6950:7250],start=6951):\n    if re.search(r'—\\s*\\d{2,3}\\s*—|-\\s*\\d{2,3}\\s*-$', l):\n        print(i, l[-60:])\nEOF\necho \"--- context 7075\"; sed -n '7070,7090p' HUB.txt; echo \"--- 7120\"; sed -n '7120,7135p' HUB.txt; echo \"--- 7175\"; sed -n '7175,7190p' HUB.txt",
 "description": "Hübschmann page and context"
}
```


### [2026-09-07T01:47:57.095Z] TOOL RESULT

```
7005 zt wahrscheinlicher als die oben gegebene Grklarung.— 198 —
7078 Geiger, Idg. P. IV, Anz. p. 23.— 200 —
7194 lS^,*nuvai lauten sollte. Vgl. H. 1053, oben p. 103,— 208 —
7229 , u, at, an etc. auf t folgten) siehe ZDMG. 44, 555.— 204 —
--- context 7075
= zd. pada- ; -ra Casuspartikel = paz. ra, phi. rai wegen',
ap. radiy Vegen*; x^ai {x^a) *Wohlgeschmack' = skr. svada-;
boi {ho) *Geruch* = zd. baoidi- (arm. buidenik Moses, Geogr.
616, wohl boyicenik zu lesen = np. boy i ctnt 'chinesisches
Parfum'); roi {ro) 'aes vel stannum fusum' = bal. rDd 'Kupfer ,
arm. avoir 'Messing, skr. loha-; roi {rd) 'Gesicht' = zd.
raoda-; xoi *Helm' (unbelegt) neben xDd, arab. xudat, arm.
^) Dazu np. kahar = skr. kadrxi- *rotlibraun*, zd. kadrv0'{a3pa')^
Geiger, Idg. P. IV, Anz. p. 23.— 200 —
xoir '^DiademV ^p. xaudc^, zd. xaoda-; mOi *Haar = paz.
mU Min. Gl. 140, g. frnd, bal. mUd^ mid, nb. mldy also ap.
*muda' ? ; sSi 'Gatte = ap. *xSauSa- ? ; maig *Heuschrecke
(neben malax) = phi. maig (und malak Bdh. 47, 10), bal.
maday, madax, arm. marax, zd. mataxd-; patg *Bote* =
syr. W^B, phi. paik, arm. payik, skr. padika- (s. oben p. 45
— 46)Vjp»y^rfa *Pussganger' = skr. paddti-y padatika-; miyan
'Mitte' = paz. phi. miyan, zd. maiSyqna^ ; bayd, bayog 'Braut'
= skr. vadhu^; beva 'Wittwe == phi. vevak, zd. Mava,
skr. vidhavd-; zBr unten* = paz. ai-er, phi. Sr- in Srtany
Ertkan PPGl. p. 9 aus "^ayar = zd. adairi (s. § 58, b)';
drdstan *in Ordnung bringen, schmticken', pr. arayam, pai-
--- 7120
ibren altesten Lehnwortern durch r wiedergeben, was im
Persischen ein d, nicht aber d oder h oder y voraussetzt,
wie ja die Armenier auch spater noch gr. J durch r {lam-
har^Jt = hx/undSec; kalapar = itaXonodioy) wiedergaben. So
deutet arm. xoir 'Diadem* auf parth. *a*5tT = ap. xauda-
boir (in burem *dufte* u. s. w.) aut *h6d = zd. baoidi-
aroir 'Messing, auf *r5J == bal. rOd 'Kupfer; Mar-K 'Meder
auf *JtfilJ == ap. Mdda-; niarax 'Heuschrecke' auf *madax
= bal. maSay, madax == zd. madaxa-; aparan/c Talast' auf
*apaMn =^ ap. apaSana-, syr. afaSnd ; sparapet 'dg/taTQdrfjyog'
auf ^spadapat = ap.*.spaJa/?a<j-, phi. spohpat (ZDMG. 36, 133) ;
harazat *leiblicher Bruder' auf "^hadazat = zd. hadozdta-. ^)
Steht ^gadrpjg fUr [Uteres OgvLddxrjq = zd. fradafa-,
arm. Hrahat, np. Farhdd, so ware der Uebergang von J
in 7& aus dem 1. Jhd. a. Chr. bezeugt. Giebt dagegen das
AiJnddava des Ptolemaeus = np. Ispahan (= ap. ^spa-
--- 7175
np. zdf siehe § 91, b.
Iran, zd (=? idg. zdh = dh -}- t) nach Analogie = ap.
np. st in ias^ = ap. basta gebunden', iran. *bazda', skr.
baddha. Vgl. § 109, d.
Ap. rd = np. I siehe § 9, a und § 34, a und b.
Fiir altes J erscheint ausnahmsweise I in malax *Heu-
schrecke* (neben regelmassigem maig § 92, b) == zd, madaxa-;
almas 'Diamant', griech. LW. = a^d/nag. Vgl. I aus t in
(afgh.) Hilmand § 88, c.
Zu z ist c/ nicht geworden; iiber garzmdn 'Himmer
s. oben p. 92.
Unklar sind die Fallo, wo im Np. y und d nach
Vokalen neben eiuander liegen. Fiihrt man sie auf ap. t
zuriick, so befremdet der Uebergang in y (wie bei pdy^z
und mdya § 88); fiihrt man sie aber auf ap. d zuriick, so
verstosst die Erhaltung des d ira Np. gegen die Kegel (wie
```


## [2026-09-07T01:48:13.130Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -- \"— 99 —\\|— 100 —\\|— 101 —\" HUB.txt | head; ",
 "description": "Hübschmann p100 marker"
}
```


### [2026-09-07T01:48:13.178Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T01:48:17.547Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -- \"-\\s*10[01]\\s*-\\|— 10[01] —\\|~ 10[01] ~\" HUB.txt | head; echo \"--- search page markers generally\"; grep -n -oE \"— [0-9]{2,3} —\" HUB.txt | sed -n 1,40p",
 "description": "Hübschmann markers list"
}
```


### [2026-09-07T01:48:18.759Z] TOOL RESULT

```
3513:7*- 100 -
--- search page markers generally
332:— 13 —
484:— 17 —
558:— 19 —
894:— 28 —
1079:— 33 —
1117:— 34 —
1154:— 35 —
1193:— 36 —
1266:— 38 —
1302:— 39 —
1339:— 40 —
1374:— 41 —
1410:— 42 —
1480:— 44 —
1552:— 46 —
1625:— 48 —
1662:— 49 —
1700:— 50 —
1848:— 54 —
1994:— 58 —
2030:— 59 —
2176:— 68 —
2213:— 64 —
2287:— 66 —
2399:— 69 —
2437:— 70 —
2472:— 71 —
2546:— 73 —
2582:— 74 —
2655:— 76 —
2690:— 77 —
2835:— 81 —
2911:— 83 —
2949:— 84 —
2985:— 85 —
3058:— 87 —
3208:— 91 —
3245:— 92 —
3281:— 93 —
3325:— 95 —
```


## [2026-09-07T01:48:21.804Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3505,3545p' HUB.txt",
 "description": "Hübschmann p100-101"
}
```


### [2026-09-07T01:48:21.848Z] TOOL RESULT

```
nend, befindlich' Bdh. 61. 241, Min. 61. 132, Shk. 257.
Afgh. melmq '6ast*, plur. melmana *6aste', melmana ein
weibl. 6ast' (nach Raverty).
1003. Darmesteter, der Tradition folgend, iibersetzt zd.
madu' durehweg mit 'Wein'. Die Bedeutung *Honig'
bewahrt osset. mudy mid.
1005. Ich kann die 61eichung : mex 'Pfloek, Nagel' = skr.
sumeka- *festgegrundet' nicht fiir sicher halten und
7*- 100 -
die Zusammenstellung von mSx (= ap. *maixa' =
arisch *maikha') mit skr. mayukha' *Pflock* nicht ver-
werfen.
1007. „Ursprunglichrituell%Horn, p.IX. Nach Noldeke
miyaxd zu sprecben.
1008. Dazu afgh. mai *a ram'.
1010. Arm. marax ist LW. und = arsacidisch-persisch madax
ZDMG. 36, 133, gehQrt also unmittelbar zu zd. ma--
daxd-. Np. maig ware = ap. *madika' {= zd. *ma-
dika-), vgl. paig.
1011. Ich glaube, dass im Phi. m^ukf pi. menukan (geschrieben
wie mSnug^ mSnugan^ Phi. Min. 10, 10) zu lesen ist,
da nur menuk einem ap. *fnamyu' = zd. mainyu-
'Geist* entspricht. Vgl. phi. zanuk = zd. zanu-- etc.
Paz. mainyo *Geist' stammt aus dem Avesta. Das in-
schriftliche phi. minU (geschrieben mm) stimmt so
wie so nicht und gehSrt wohl gar nicht hierher. Np.
mvno setzt Horn mit Recht = zd. mainyava-.
1012. Noldeke, Tabari 101 hat Km-mihan.
1014. Fiir na^ (in Comp.) und na nicht' steht im PSz.
durchweg wg = ap. waiy, vgl. Min. 61. 143 und Shk.
259. Daraus ist np. na, alter noch ne (vgl. nest 'ist
nicht' und nay-amad er kam nicht', Salem. Shuk.
Gram. p. 16 und 59) entstanden. Die nachdriickliche
Form nai reimt nach NSldeke auf kaL
1015. Dazu arm. LW. anapak ungemischt, rein (vom Wein).
1017. Dazu arm. LW. naz-i-m *thue stolz , briiste mich,
liebkose' (5. Jhd.). Im Phi. ist ndzuU zu lesen.
Afgh. nazuk (mit u) bei Raver ty; nazaka, nenzdka f.
heisst *Puppe*.
1019. Vgl. gr, v^OTig 'niichtern', das aber zur Wzl. ed essen'
gehSrt.
```


## [2026-09-07T01:48:38.368Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### KNT\"; grep -n -i \"madika\\|locust\\|grasshopper\" KNT.txt | head; echo \"### SYN mastu/curdle\"; grep -n \"mastu\\|curdled milk\\|5.88\\|locust\" SYN.txt | head -8; echo \"### BRT madaxa full\"; sed -n '19586,19594p' BRT.txt",
 "description": "Kent, Buck, Bartholomae locust"
}
```


### [2026-09-07T01:48:38.453Z] TOOL RESULT

```
### KNT
### SYN mastu/curdle
4914:Br. ae ee on Skt. paksin-, deriv. of paksa- ‘wing’ algo “infutions Br. lapous ‘bird’ but | (4.392). at. a eet and so prob. fr. Av. maraya- used of large birds ‘locust’, with us. locusta (‘lobster’ and) | (Barth. 1172), NPers. murgh ‘bird? :
7406:Lat. occidere (>It. uccidere, OF. ocire, Rum. ucide), cpd. of ob- and cae- dere ‘cut, strike’, also ‘kill’, perh. : Skt. khid- ‘strike, tear, press’, Walde-P. 2.5388. Ernout-M. 128f. Walde-H. 1.129.
8314:CHAPTER 5 FOOD AND DRINK; COOKING AND UTENSILS 5.11 Eat 5.57 Minn 5.12 Foop 5.61 Mezar 5.13 Drink (vb.) 5.612 Burcurr 5.14 Hunexr (sb.) 5.62 Brrr 5.15 Turrsrt (sb.) 5.63 Sausace 5.16 Suck (vb.) 5.64 Sour, Brots 5.17 Mrx 5.65 VEGETABLES ' 5.21 Cook (vb.) 5.66 Bran ? 5.22 Bor 5.67 Pra 5.23 Roast, Fry 5.68 Onion 5.24 Baxe 5.69 CaBBAGE 5.25 Oven 5.70 Porato 5.26 Por 5.71 Fruir 5.27 Kerrin 5.72 APPLE 5.28 Pan 5.73 PEAR 5.31 Disx 5.74 Pracu 5.32 Prats 5.75 Wie : 5.33 Bown 5.76 Grape 5.34 Pircuer, Jue 5.77 Nur 5.35 Cup 5.78 OLIvE 5.36 Saucer 5.79 Om 5.37 Spoon 5.80 Berry 5.38 Kyire 5.81 Saur 5.39 Fork 5.82 Prpprr 5.41 A Mua, 5.83 VINEGAR 5.42 BReakFast Bi Rdeer ona 5.43 Luncx 585 § 544 Dinner een Base Sucnbn. 5.86 Mixx (sb.) 5.51 Breap 5.87 Minx (vb.) 5.52 Caxn 5.88 CHEESE 5.58 Dover 5.89 Burrer 5.54 Kwrap 5.91 Merap 5.55 Mzau, Frour 5.92 Wine 5.56 Grinp 5.93 Brrr
25881:15.88 Dirty, SoILED
26711:1, Grk. pétas (NG perdu ‘ink’, peda- yos ‘blue-black, livid’) : Lett. melns ‘black, dirty’, Skt. mala- ‘dirt, filth’, malina- ‘dirty’, etc. (15.88).
26720:4, Goth. swarts, ON svarir, etc., gen- eral Gmc. (NE swart only rhet., poet., or dial.) : Lat. sordés ‘filth’, sordidus ‘dirty’ (15.88), sudswm, a kind of dark color. Walde-P. 2.535. Falk-Torp 1109. Ernout-M. 958, 991.
27364:15.88 DIRTY, SOILED ¥ Goth. wnhrains Lith. purvinas, suterstas Grk. purapsy ee age ON saurigr, uhreinn Lett. netirs, melns NG depbsy Dra ur, us Dan.  smudsig, snavset, uren ChSl. netistic Game squalidus, Sw. smutsig, oren SCr. — prijav [at 80" ae immundus OE fal, horig, uncl@ne — Boh.  Spinavy Ne sudicio ME unclene, foul, hori, Pol. brudny ; ET SS UntOr A filthi — Russ. grjaznyj bey a NE dirty, soiled Skt.  malina-, etc. ; ae Du. vuil, smerig Av. ahita- Rum. eh OHG  unreini, unstibar Nir salach MHG unreine, unsiber, hor- * bdr, brwnt Wee: re NHG = schmutzig, schmierig
28104:‘caress’ to ‘love’. Berneker 5388 : , O81 f
### BRT madaxa full
Haomai  vTipe  zi  anyg  *°SawAj  aaftwa fiaSnte  .  .  äat  hs  ys  kaomahe  '%6  aiä AacaiU . .  rmjaiü  (sd.)  hasmake  °%3  "denn alle  andern  Rauschtrinke  sind  von  . .  A. begleitet,  aber  er,  der  Rauschtrank  des H.  . ."  Y.  10.  8;  Yt  17.5'.  b)  sonst: dahms  hurqm  (sd.)  ifaraiti  'S?  ^asfya.- paya/ahü  N.  jo;  —  kada  ajSn  mB%r>m ahya  *°äahyä''>  yä  . .  "wann  wirst  du  den Unflat  dieses  Rauschtranks  treffen,  mit dem.."  Y-^i".!©!).  [N.jo:  lies  mi^Ue statt  mähB  ^araiti;  s.  Pü.]
Ableit.  —  Zam  V.  tmaä-.  —  ai.  mäda-  m., np.  mai.  —  Pü.  (»u  N.):  mai,  (lu  Y,  9,  lO): maiiin,  (lu  V.  //):  undeutlich.  S.  noch  No. I.  3-  —  '•  Pü.:  fall.,  tnaiHn  gdw  -  ha! *en  mai  pa  ftahang  göüt  —  /tum  dänäiik  bavät, —  »»  NA.  magaJiyä.  So  liest  aber  nur  iine bessere  Hds.  Pt4,K5,  J2,  Mfz  haben  mad; wogegen  Fü.3)  nicht  aufkommen  kann. Gegenüber  Gdn.  KZ.  30,  534  s.  Gdn.  KZ.  sS. 19S.  Seine  Einwendungen  entbehren  der  Be- gründung, leine  eigene  Oberseltnng  ist  un- haltbar. Vgl.  lu  urväxi.iixlay:  —  S  Pü.!  ia an  dahisn  iaSän  stänenJ  muhrdän  S!än  pa ma-fik  -  pa  an  i  apecai  vattarVi,  vgl.  lu  Y.  JJ. 7,  wo  richtig  ahyä  magahyä  steht.
•  j.  tnaSaxa-  m.,  'xä-  f.  Ileuschrecke', ein  i/dA^sches  Tier:  ti  sUnS  'xaySsia aogasdast>ma  bavainti  "die  verleihen  der Spinne  und  der  Heuschrecke  am  meisten
Macht"  V. 7, 26;  —  ..'"xstamicalca  °xaheh v.r.  MGI.  ■       "
np.  maJax;  vgl.  tnaig;  s.  dain  DsT.  Etlr.  3. 195,   Hbu.  PSt.  100,  302,  364,   HoKN  GlrPh.
/  b.  44,  57.  —  Pü. :  rnatag-,
•  j.  iiiaSav  n.  '(Wein  uzw.)  Beerenwein'  '* : gqm^a  ..yaom?a  . .  ''iula  ansptm  V.5. 52; 53>  54iF.  7/;    —    duye  navaiti  narqm  .
%äsXaYA&D.'-\mAQzTi.xft-alafrayantuts{v^'*'7<'^<^  g^'^  ^^  ^ar^%ahe  vS  huraya (näml.  haomahi)  =S?(NP.)  vin^attukktihs  »^  *°öÄ/'>  vä  Y.  14.^1. jasmtu     stracks  vorwärts  sollen  sie  gehen, die  sich  an  dir  (dem  Haomä)  begeistern,
Y.  /0. 1 4 ;  19;  —  raoxma  frayantu  tl  (näml. haomahe)  '%s  nnfys  (sd.)  *vasainU  °\s (näml.  ti)  Y. /o.  19.
```


## [2026-09-07T01:50:10.902Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,80p tools/verify_check.py",
 "description": "Inspect verify_check.py"
}
```


### [2026-09-07T01:50:10.941Z] TOOL RESULT

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


## [2026-09-07T01:50:14.062Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 80,140p tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-07T01:50:14.111Z] TOOL RESULT

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


## [2026-09-07T01:50:30.140Z] AGENT

Now I'll write the verification file.


## [2026-09-07T01:50:32.457Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg317.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/317.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page image for audit"
}
```


### [2026-09-07T01:50:32.552Z] TOOL RESULT

```
total 14212
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 21:50 .
drwxrwxr-x 12 sfmqrb sfmqrb   4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-07T02:00:07.659Z] TOOL CALL #70: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-317.json <<'JSONEOF'\n{\n  \"pdf_page\": 317,\n  \"book_page\": 287,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Mad\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *mad- (laryngealist *meh₂d-) 'wet, dripping; fat, well-fed', with the derived sense 'food, fattening' — Pokorny 694-695\",\n      \"note\": \"The root is genuine and standard. Pokorny 694-695 has 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating', and Watkins/AHD (1985 ed., p. 38) has 'mad-. Moist, wet; also refers to various qualities of food' — Nourai's gloss 'wet, also food' is essentially Watkins' wording, and the language label 'Indo-European' is right. Walde-Pokorny II 230-232 is the same article. What is remarkable is that Pokorny's article contains almost the whole of Nourai's chart in the same order: 'ai. madati, madate … mada- m. Rauschtrank = av. maδa-; ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ ein Wasservogel; ai. matsya- m., av. masya Fisch (der nasse; Ableitung von einem -es-St. *mades-); mastu- n. saurer Rahm (*mad-stu-) … arm. macun sauer, geronnene Milch … iran. Worte für Dickmilch, so npers. mast, masīdan … lat. madeō, mattus trunken (*madi-to-s) … ahd. mast Futter, got. mats Speise, ags. mete, mnd. mat(e) Kamerad'. Two modern caveats: (a) Cheung (2007) and LIV split the family into *mad¹ 'to become intoxicated' (PIE *med-) and a separate Indo-Iranian *mad 'to curdle', for which no PIE root is set up; (b) the 'fish' member is no longer taken as certain (see node #1).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *mad- (در نگارش امروزی *meh₂d-) به معنی «خیس، تر، چکه‌کننده؛ فربه و پرورده» و از همین‌جا «خوراک»، ریشه‌ای شناخته و پذیرفته است: پوکورنی (ص ۶۹۴–۶۹۵) آن را با معنی «تر؛ چرب، فربه، مست‌کننده» می‌آورد و واتکینز در پیوست فرهنگ American Heritage نیز «mad-. نمناک، تر؛ همچنین دربارهٔ کیفیت‌های خوراک» دارد؛ پس برچسب زبانی و معنای «wet, also food» در نمودار نورایی درست است. نکتهٔ چشمگیر آنکه تقریباً همهٔ شاخه‌های نمودار — سنسکریت madati و mada-، اوستایی maδa-، سنسکریت madgu- برابر «ماغ» فارسی، سنسکریت mastu- و ارمنی macun برابر «ماست» و «ماسیدن»، لاتینی mattus و واژه‌های ژرمنی mast/mats/mete/mate — همه در همان مقالهٔ پوکورنی و به همان ترتیب آمده‌اند، یعنی نورایی مستقیماً از پوکورنی و واتکینز برداشته است. دو نکتهٔ احتیاطی: نخست آنکه چونگ (۲۰۰۷) و فرهنگ LIV دو ریشهٔ *mad «مست شدن» و *mad «بستن، دلمه شدن» را از هم جدا می‌کنند و برای دومی ریشهٔ هندواروپایی نمی‌سازند؛ دوم آنکه پیوند واژهٔ «ماهی» با این ریشه امروز قطعی دانسته نمی‌شود (بنگرید به گرهٔ ۱).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/mattus\",\n        \"https://en.wiktionary.org/wiki/meat\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:694\", \"status\": \"supports\", \"note\": \"POK_full.txt line 57036 ff. (= POK_02.txt line 5645 ff., German original): 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating … References: WP. II 231 f., WH. II 6 f.  Page(s): 694-695'. The page number Nourai cites is exactly right, and the article's material list is the source of his whole chart.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 230-232 s.v. 'mad-'\", \"stance\": \"supports\", \"note\": \"incoming/WLD/WLD_Bd2_pages.txt line 15104: 'weitere iran. Worte für Dickmilch u. dgl., so np. mast \\\"saure Milch\\\", masī[dan]' — the article Pokorny cites as WP. II 231 f., same members.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 38 (AHD_watkins1985.txt line 708) s.v. mad-\", \"stance\": \"supports\", \"note\": \"'mad-. Moist, wet; also refers to various qualities of food. 1. Sanskrit madati, \\\"it gladdens, it bubbles,\\\" hence madana-, delightful, joyful, hence madanah, a myna bird: MYNA. 2. Suffixed form *mad-i- in Germanic *mati- in: a. Old English mete, food: MEAT; b. Middle Low German (ge)mate … MATE. 3. Suffixed form *mad-sto- … Old English mest, fodder: MAST. [Pok. mad- 694.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, leaves 553-556: 'mad- (1) feed; food', 'mad- (3) get wet; be wet', 'madtós (maditós, mastos)'\", \"stance\": \"partial\", \"note\": \"IEC.txt lines 10227, 10237, 10239: Mann splits the family into three lemmas — 'mad- (1) \\\"feed; food\\\". WP II, 232 …', 'mad- (3) … \\\"get wet; be wet\\\". WP II, 230  Skt. mádāmi, pp. mattáh \\\"get drunk\\\"; Lat. madeó …', and 'madtós … \\\"fed, fattened; food, fattening\\\" … Skt. cf. mástu, n. \\\"sour cream, whey\\\" … Per. māst \\\"sour milk\\\"' — the same words, but no single root box.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck ch. 3.65 'Fish', p. 184 (SYN.txt line 4927)\", \"stance\": \"partial\", \"note\": \"'Skt. matsya-, Av. masya-, fr. an IE *mad- \\\"be wet\\\" in Grk. madáō, Lat. madēre, etc.? Walde-P. 2.230.' — Buck knows the root but puts a question mark on the fish member.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"pp. 253-254, s.v. *mad¹ and *mad\", \"stance\": \"partial\", \"note\": \"CHEUNG.txt line 16801: '*mad¹ \\\"to become intoxicated, joyous\\\" … «PIE *med- … = LIV: 423 f. | Pok.: 694 f.'; line 16828: '*mad \\\"to curdle, coagulate\\\" … Skt. mástu- (n.) \\\"sour cream\\\" (< *mad-stu-) … The root is apparently IIr. … PIE — = LIV: – | Pok.: 694 f.' Cheung keeps Pokorny's page but treats the two senses as two roots.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"masya 1 : fish; mada : having too much liquid, drunk; mad : a water bird, mina\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two of the three items are real Avestan words. (a) masiia- 'fish' (Y. 2.8, Vd. 2.8 etc.) is well attested, and Pokorny 694 derives it, with Skt. matsya-, from an -es-stem *mades- 'the wet one' — this is precisely Nourai's arrow; but Buck (p. 184) already marks it with a question mark, and current handbooks (Martínez García & de Vaan, Introduction to Avestan, p. 32; en.wiktionary s.v. Reconstruction:Proto-Indo-Iranian/mátsyas) call PII *mátsyas 'unknown; possibly borrowed from the BMAC substrate', citing the lack of any relation to *peysk- or *dʰǵʰu-, with the *meh₂d- connection only as an 'alternative theory'. (b) maδa- m. 'intoxicating drink, intoxicated ecstasy' (Bartholomae AiW 1112 'Rauschbegeisterung durch Haoma-Genuss', beside the verb maδ- 'to become intoxicated', Y. 10.8, N. 30) is exactly Pokorny's 'av. maδa- Rauschtrank' — Nourai's gloss 'having too much liquid, drunk' is a loose paraphrase but the derivation is right. (c) 'mad : a water bird, mina' is not an Avestan word at all: Bartholomae records only the verb maδ-, and the water-bird word Nourai wants is Sanskrit madgu-, which Pokorny equates with New Persian māγ ('ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ'). The printed page (see refs/ocr/BOOK/317.png) has exactly what the JSON has, so this is Nourai's own slip — he moved the Sanskrit/Persian bird word up into the Avestan box to give māγ a parent.\",\n          \"derivation_fa\": \"از سه واژهٔ این گره دو تا اوستایی راستین‌اند. یک: masiia- «ماهی» گواهی‌شده است و پوکورنی (ص ۶۹۴) آن را همراه سنسکریت matsya- از ستاکِ ‎*mades-‎ «آنِ تر» می‌گیرد، یعنی همان پیکان نورایی؛ اما باک (ص ۱۸۴) همان‌جا علامت پرسش گذاشته و پژوهش امروزی (مارتینس گارسیا و دِ فان، ص ۳۲؛ ویکی‌واژه ذیل *mátsyas) خاستگاه این واژه را ناشناخته و شاید وام‌واژه‌ای از زیرلایهٔ باکتریا-مرو (BMAC) می‌داند و پیوند با *meh₂d- را تنها «نظری دیگر» می‌شمارد. دو: maδa- «نوشابهٔ مست‌کننده، سرمستی» (بارتولومه، فرهنگ ایرانی باستان ستون ۱۱۱۲) دقیقاً همان «maδa- = Rauschtrank» پوکورنی است و اگرچه معنایی که نورایی داده («دارای مایع بسیار، مست») دقیق نیست، اشتقاق درست است. سه: «mad» به معنی «پرندهٔ آبی، مینا» هیچ گواهی اوستایی ندارد؛ بارتولومه فقط فعل maδ- را ثبت کرده و واژهٔ پرندهٔ آبی در واقع سنسکریت madgu- است که پوکورنی آن را برابرِ «ماغ» فارسی می‌گذارد. تصویر صفحهٔ چاپی (refs/ocr/BOOK/317.png) نشان می‌دهد متن استخراج‌شده امانتدار است؛ پس این لغزش از خودِ نورایی است که واژهٔ سنسکریت/فارسی را به جعبهٔ اوستایی برده تا برای «ماغ» پدری بسازد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/m%C3%A1tsyas\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%87%DB%8C\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:694\", \"status\": \"supports\", \"note\": \"POK_02.txt line 5647: 'ai. madgu- \\\"ein bestimmter Wasservogel, ein Fisch\\\" = np. māγ \\\"ein Wasservogel\\\", ai. mātsya- m., av. masya \\\"Fisch\\\" (\\\"der nasse\\\"; Ableitung von einem -es-St. *mades-)' and 'av. maδa- \\\"Rauschtrank, Rauschbegeisterung\\\"' — all three of Nourai's items, but the bird is Sanskrit/Persian, not Avestan.\"},\n            {\"ref\": \"SYN:184\", \"status\": \"supports\", \"note\": \"SYN.txt line 4919 ff.: page 184 is Buck's ch. '3.65 FISH', whose table lists 'Skt. matsya- / Av. masya-' and whose note 5 (line 4927) reads 'Skt. matsya-, Av. masya-, fr. an IE *mad- \\\"be wet\\\" in Grk. madáō, Lat. madēre, etc.? Walde-P. 2.230.' Nourai's page is right; the question mark is his to answer.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1112 s.v. maδa- (BRT.txt line 19595); no bird lemma 'mad-'\", \"stance\": \"partial\", \"note\": \"'g. *mada-, j. maδa- m. 1) \\\"Rauschbegeisterung\\\" durch Haoma-Genuss … Ableit. — Zum V. maδ-. — ai. mada- m., np. mai.' Bartholomae has maδa- and the verb maδ-, and masiia- 'Fisch', but no Avestan water-bird word — confirming that Nourai's third item is misplaced.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 253 s.v. *mad¹\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: Y Av. maδ- \\\"to become intoxicated, joyous\\\" — Liste: 42 … *SANSKRIT: mad \\\"to become exhilarated, intoxicated\\\" (RV+) = EWAia II: 299' — the Avestan verb and its Indic cognate as Nourai draws them.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien § 94, p. 101 (HUB.txt line 7170)\", \"stance\": \"supports\", \"note\": \"'§ 94. Ap. d vor y, m, n ist geschwunden: māγ \\\"ein Wasservogel\\\", skr. madgu-, ap. *maδgu-?' — Hübschmann derives the bird from an Old Persian, not Avestan, form.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. 'mesgus, os \\\"diving bird\\\"' (IEC.txt line 10687)\", \"stance\": \"contradicts\", \"note\": \"'mesgus, os \\\"diving bird\\\". Cf. mesgó (2). (mezg-)  Skt. madguḥ, m. id.; Lat. mergus, m., LLat. mergulus \\\"cormorant\\\"' — Mann assigns the water-bird word to *mezg- 'to dive' (Lat. mergus), not to *mad-.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"mâhî «ماهی» : fish; mast «مست ۱» : drunk; mâğ «ماغ» : a black water bird, mina\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All three Persian words are real and the two central ones are textbook cases. ماهی māhī 'fish' < Middle Persian māhīg [m'hyk] (MacKenzie, CPD p. 54 'mahig … fish; astr. Pisces') < Proto-Iranian *mácyah < PII *mátsyas, cognate with Av. masiia-, Skt. mátsya-; the MP -g of māhīg is regularly lost in New Persian (cf. MP xānag > NP xāna). مست mast 'drunk' < MP mast [mst] 'bemused, intoxicated' (MacKenzie p. 54; Manichaean MP/Parthian mst, Cheung *mad¹), from Old Iranian *mad-ta-, the participle of maδ- — the Old Iranian cluster -dt- gives -st- (cf. *basta- > baste), exactly parallel to Skt. matta- and to Lat. mattus < *maditus in node #10. ماغ māγ 'a black water bird' is attested from the 10th c. (Loghat-e Fors, printed p. 235 of the Eqbal ed., quotes Daqīqī 'مرغی باشد سیاه فام و بیشتر در آب نشیند'), and Pokorny 694, Horn no. 961 and Hübschmann § 94 all equate it with Skt. madgu-, Hübschmann positing an Old Persian *maδgu- with loss of δ before g/m; that is Nourai's arrow, but Mann (IEC, s.v. mesgus) instead puts Skt. madgú- with Lat. mergus under *mezg- 'to dive', so the last word is only plausible. The Rudakī line in the chart is the verse Borhān-e Qāteʿ quotes for ماغ (Mo'in's edition attributes it to Daqīqī, not Rudakī).\",\n          \"derivation_fa\": \"هر سه واژهٔ این جعبه فارسی راستین‌اند و دو تای نخست از نمونه‌های درسی‌اند. «ماهی» از فارسی میانهٔ māhīg (مکنزی، فرهنگ کوچک پهلوی ص ۵۴: mahig «ماهی») و آن از ایرانی باستان *mácyah و هندوایرانی *mátsyas، هم‌ریشه با اوستایی masiia- و سنسکریت mátsya-؛ ‎-g‎ پایانی فارسی میانه در فارسی نو به‌قاعده افتاده است (مانند xānag > خانه). «مست» از فارسی میانهٔ mast (مکنزی؛ مانوی و پارتی mst)، از ایرانی باستان *mad-ta-، صفت مفعولی ستاک maδ-؛ خوشهٔ ‎-dt-‎ ایرانی باستان به ‎-st-‎ بدل می‌شود (مانند *basta- > بسته)، درست همانند matta- سنسکریت و mattus لاتینی (گرهٔ ۱۰). «ماغ» از سدهٔ چهارم گواهی دارد (لغت فرس، ص ۲۳۵ چاپ اقبال، از دقیقی: «مرغی باشد سیاه فام و بیشتر در آب نشیند») و پوکورنی (۶۹۴)، هرن (شمارهٔ ۹۶۱) و هوبشمان (بند ۹۴) هر سه آن را برابر madgu- سنسکریت می‌دانند و هوبشمان صورت پارسی باستان *maδgu- را با افتادن ذ فرض می‌کند؛ ولی مان واژهٔ سنسکریت را با mergus لاتینی زیر ریشهٔ *mezg- «شنا رفتن، فرو رفتن» می‌گذارد، پس این یکی تنها پذیرفتنی‌است نه قطعی. بیتِ نمودار همان بیتی است که برهان قاطع ذیل «ماغ» آورده و در چاپ معین به دقیقی نسبت داده شده، نه رودکی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%87%DB%8C\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1961\", \"status\": \"supports\", \"note\": \"BQT vol. 4 pdf p. 44 = printed 1961 (incoming/BQT/BQT_v4_pages.txt): the ماهی page, whose Mo'in footnote reads 'ماهی - اوستا masya- (ماهی)، پهلوی māhīk، هندی باستان mātsya- (ماهی)، کردی māsi، بلوچی … اسشق ۹۶۹' (اسشق = Horn's Grundriss no. 969) — exactly Nourai's chain.\"},\n            {\"ref\": \"BQT:2007\", \"status\": \"supports\", \"note\": \"BQT vol. 4 pdf p. 90 = printed 2007: the مست page, footnote 6 'مست بفتح اول. قس: اوستایی maδa- (مسکر)، پهلوی mast، هندی باستان matta- (مست)، فن: mad-، madati (شاد بودن، مست شدن)، اسشق … کردی mast' — Mo'in's own note on mast, again with Horn.\"},\n            {\"ref\": \"FRS:137\", \"status\": \"partial\", \"note\": \"Loghat-e Fors does have the ماغ entry — FRS_pages.txt leaf 254 (printed p. 235 of the Eqbal 1319 ed.): 'مرغی باشد سیاه فام و بیشتر در آب نشیند [دقیقی گوید …]' — but Nourai cites the Mojtaba'i-Sadeqi (Kharazmi 1365) edition, whose pagination differs from the copy on disk, so p. 137 itself cannot be checked. Note also that neither BQT page Nourai gives covers ماغ: that entry stands at printed p. 1944 (pdf p. 27).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp. 54-55 (PHD_mackenzie.txt lines 3415, 3491, 3493)\", \"stance\": \"supports\", \"note\": \"'mahig [m'hyk | M m'hyg, N mahi] fish; astr. Pisces'; 'mast [mst | = M, N ~] bemused, intoxicated'; 'māst [m'st | N …] curds, sour milk'. The Middle Persian antecedents of two of Nourai's three words (and of node #4); no MP *māγ.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss nos. 961 and 969, pp. 215-216 (HRN.txt lines 8310, 8402)\", \"stance\": \"supports\", \"note\": \"'961. māγ \\\"Wasservogel\\\" (Šāhn. I,444 V.191). ai. madgū- \\\"ein Wasservogel\\\" (Hübschmann, ZDMG. 38,423)'; '969. māhī \\\"Fisch\\\" … aw. masya- \\\"Fisch\\\"; phlv. māhīk; ai. mātsya- \\\"Fisch\\\"'.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 4 printed p. 1944 (pdf p. 27) s.v. ماغ\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote 4: 'هندی باستان mad-gu- (نوعی پرندهٔ آبی) (هوبشمان …) اسشق ۹۶۱' plus the Loghat-e Fors quotation; he adds that Borhān's Arabic gloss «مایکون» is a corruption of «سیاهگون» and not Arabic at all.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 253 s.v. *mad¹\", \"stance\": \"supports\", \"note\": \"'*NWIR: NP mast, Kurd. mast, Sang. mast … \\\"drunk\\\"' beside MMP/Parthian mst — the Iranian verb dictionary confirms mast as the inherited participle.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang (2-vol. condensation, MON_part2.txt) s.v. ماهی/مست\", \"stance\": \"silent\", \"note\": \"The abridgement carries the definitions without the origin tags or Latin etyma of the six-volume print, so it adds nothing on etymology here.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit / Armenian\",\n          \"words\": \"mâstu, maccum : yogurt, sour cream\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The two words meant are real, but neither is printed correctly. Sanskrit is mástu- n. 'sour cream, whey' (short a; Pokorny 694 'mastu- n. saurer Rahm (*mad-stu-)'; Mayrhofer EWAia II 336 via Cheung), not 'mâstu' with the long â Nourai's system marks. The Armenian word is մածուն macun 'sour, coagulated milk' (with the verb macanim 'to coagulate'), which is what Pokorny prints ('arm. macun \\\"sauer, geronnene Milch\\\" (*madi̯o- + arm. Suff. -un)') and what Horn no. 959 prints; 'maccum', with -cc- and final -m, is no attested form. I rendered the printed page (refs/ocr/BOOK/317.png): the book itself has 'mâstu, maccum', so the extraction is faithful and the error is Nourai's (most likely a misreading of Horn's macun). With the forms corrected, the derivation is sound and standard: an Indo-Iranian *mad-stu- 'that which has curdled' gives Skt. mástu-, and the Armenian noun is built on the same *madi̯o-/mac- stem, both under Pokorny's mad-; Cheung, however, files them under a separate root *mad 'to curdle' for which no PIE ancestor is reconstructed, and notes that Armenian mac- 'to coagulate' fits 'except that -c- would need an explanation'.\",\n          \"derivation_fa\": \"هر دو واژه‌ای که در این جعبه آمده واقعی‌اند، ولی هیچ‌یک درست چاپ نشده است. صورت سنسکریت mástu- (با الفِ کوتاه) به معنی «سرشیر ترش، آب‌پنیر» است — پوکورنی ص ۶۹۴: «mastu- n. سرشیر ترش (*mad-stu-)» — نه mâstu با آی کشیده. واژهٔ ارمنی نیز مացուն macun «شیر دلمه و ترش» است (با فعل macanim «بستن، دلمه شدن») که هم پوکورنی و هم هرن (شمارهٔ ۹۵۹) همان را می‌آورند؛ «maccum» با دو c و م پایانی هیچ گواهی ندارد. تصویر صفحهٔ چاپی (refs/ocr/BOOK/317.png) را دیدم: در کتاب نیز «mâstu, maccum» چاپ شده است، پس خطای خوانش اسکن نیست بلکه خطای خودِ کتاب است (به احتمال زیاد بدخوانی macun در هرن). با اصلاح صورت‌ها، اشتقاق درست و متعارف است: هندوایرانی *mad-stu- «آنچه بسته شده» به mástu- سنسکریت می‌رسد و اسم ارمنی بر همان ستاک *madi̯o-/mac- ساخته شده است؛ چونگ اما این‌ها را زیر ریشهٔ جداگانهٔ *mad «دلمه شدن» می‌گذارد که برای آن نیای هندواروپایی بازسازی نشده، و می‌افزاید که پیوند ارمنی macun پذیرفتنی است «جز آنکه -c- توضیح می‌خواهد».\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"mâstu, maccum : yogurt, sour cream\",\n          \"correct_form\": \"Sanskrit mástu- 'sour cream, whey'; Old Armenian մածուն macun 'coagulated milk'\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%B3%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:694\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 57062-57070: 'mastu- n. \\\"sour skimmings\\\" (*mad-stu-) … Armenian macun \\\"sour, coagulated milk\\\" (*mad/o- + Armenian Suff. -un), macanim, macnum \\\"stick, adhere, cling to, coagulate\\\"' — the two words of the node, with the correct spellings.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. 'madtós (maditós, mastos)' (IEC.txt line 10239)\", \"stance\": \"supports\", \"note\": \"'madtós … \\\"fed, fattened; food, fattening\\\". Cf. mad- (1)  Skt. cf. mástu, n. \\\"sour cream, whey\\\"; Hind. maṭṭhā, m. \\\"buttermilk\\\"; Per. māst \\\"sour milk\\\"; Arm. matʿ, o-st. \\\"molasses, mash of grapes\\\"' — Sanskrit and Persian together, though Mann's Armenian comparandum is matʿ, not macun.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 254 s.v. *mad 'to curdle, coagulate'\", \"stance\": \"partial\", \"note\": \"'Skt. mástu- (n.) \\\"sour cream\\\" (< *mad-stu-) = EWAia II: 336 … The root is apparently IIr. It may be cognate with Arm. mac- \\\"to coagulate\\\", except that -c- would need an explanation. PIE — = LIV: – | Pok.: 694 f.'\"},\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka, s.v. māsta- (ISS_alt_DKS.txt line 6058)\", \"stance\": \"supports\", \"note\": \"'The base mad- \\\"coagulate\\\" may be homonymous or the same base mad- \\\"to be moist\\\" (so assumed IE Pok. 694), Khotan Saka māsta- \\\"coagulated\\\", amāsta- \\\"not coagulated\\\", Zor.P., N.Pers. mast \\\"thick milk\\\", O.Ind. mástu- \\\"thick cream\\\" (-d-t-, or -dst-), N.Pers. masīdan \\\"to coagulate\\\"'.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 959, p. 215 (HRN.txt line 8298)\", \"stance\": \"partial\", \"note\": \"'959. māst \\\"saure Milch\\\", māsīden \\\"gerinnen\\\". skr. mástu- \\\"saurer Rahm\\\". arm. macun \\\"saure Milch\\\", macanim … (Hübschmann, No. 184), sowie bal. masay, pp. masta \\\"to freeze, curdle\\\" … die Hübschmann ZDMG. 44, 561 vergleicht, stimmen lautlich nicht genau.' Horn prints macun and warns that the comparanda do not match phonetically in detail.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"mâst «ماست» (+ ماسیدن) : yogurt\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"ماست māst 'yogurt' and the verb ماسیدن māsīdan 'to curdle, set' are inherited Iranian: Middle Persian māst [m'st] 'curds, sour milk' (MacKenzie CPD p. 55) beside Manichaean MP/Parthian mās- 'to coagulate, become hard' (Cheung p. 254), with cognates right across Iranian (Khotanese māsta- 'coagulated', Ossetic mast, Pashto māsta 'curds', Balochi mastag, Wakhi maδ-). The relation to Sanskrit mástu- is therefore one of cognacy, not of descent: Nourai's arrow 'Sanskrit/Armenian → Persian' should be read as 'same Indo-Iranian stem', since Persian māst cannot come out of Sanskrit mástu- (an Iranian *mād-/*mas-ta- is required for the ā and the -st-). Modern opinion is otherwise split: Cheung, Bailey, Horn, Mann, Pokorny and Mo'in all treat māst as native Iranian from *mad 'to curdle', while en.wiktionary (s.v. ماست) makes MP māst a loan from Classical Syriac ܡܣܬܐ mastā — a claim it leaves unsourced and which is more plausibly the reverse direction, given the Iranian verb mās- and the wide Iranian spread of the noun. Mo'in, in the footnote on the very page Nourai cites, rebuts a different rival etymology: 'بعضی پنداشته‌اند که ماست عربی است و از «ماس» مأخوذ است … این معنی ربطی به «ماست» فارسی ندارد'.\",\n          \"derivation_fa\": \"«ماست» و فعل «ماسیدن» واژه‌هایی ایرانی و میراثی‌اند: فارسی میانهٔ māst «شیر بسته، ماست» (مکنزی ص ۵۵) در کنار ستاک mās- «بستن، سخت شدن» در فارسی میانهٔ مانوی و پارتی (چونگ ص ۲۵۴)، با هم‌ریشه‌های فراوان در سراسر زبان‌های ایرانی: ختنی māsta-، آسی mast، پشتو māsta، بلوچی mastag، وخی maδ-. پس نسبت آن با mástu- سنسکریت نسبت هم‌ریشگی است نه فرزندی؛ پیکان نورایی («از سنسکریت/ارمنی به فارسی») را باید «برخاسته از همان ستاک هندوایرانی» خواند، زیرا «ماست» را آواشناسی از mástu- سنسکریت نمی‌توان بیرون آورد و صورت ایرانی *mād-/*mas-ta- لازم است. دیدگاه امروزی یکدست نیست: چونگ، بیلی، هرن، مان، پوکورنی و معین همه آن را ایرانی اصیل از ریشهٔ *mad «دلمه شدن» می‌دانند، ولی ویکی‌واژه فارسی میانهٔ māst را وام‌واژه‌ای از سریانی کلاسیک mastā می‌شمارد؛ این ادعا بی‌سند است و با توجه به ستاک ایرانی mās- و گسترهٔ ایرانی واژه، وام‌گیری در جهت وارونه محتمل‌تر است. معین در همان صفحه‌ای که نورایی ارجاع می‌دهد ادعای دیگری را رد می‌کند: «بعضی پنداشته‌اند که ماست عربی است و از «ماس» مأخوذ است … این معنی ربطی به «ماست» فارسی ندارد».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%B3%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:215\", \"status\": \"supports\", \"note\": \"Horn's no. 959 stands at the top of printed p. 215 (HRN.txt line 8298, immediately after the '— 214 —' page footer): 'māst \\\"saure Milch\\\", māsīden \\\"gerinnen\\\". skr. mástu- \\\"saurer Rahm\\\". arm. macun …' — Nourai's page is exact, and Horn gives both the noun and the verb ماسیدن that the chart adds.\"},\n            {\"ref\": \"POK:694\", \"status\": \"supports\", \"note\": \"POK_full.txt line 57065: 'iran. words for Dickmilch, so npers. mast \\\"sour milk\\\", masīdan \\\"curdle, coagulate, harden\\\", etc.' (POK_02.txt line 5651 in the German original) — Pokorny lists the Persian pair explicitly under mad-.\"},\n            {\"ref\": \"BQT:1941\", \"status\": \"supports\", \"note\": \"BQT vol. 4 pdf p. 24 = printed 1941: the ماست entry, with Mo'in's footnote 14 'سانسکریت mastu (سرشیر حامض)، ارمنی macun (غیرترش)، macanim (چسبانیدن، بستن، منجمد شدن)، بلوچی mastag …، اسشق ۹۵۹، افغانی māsta (شیر دلمه شده)، کردی māst …، هوبشمان ۹۵۹', followed by the rebuttal of the Arabic etymology quoted in the derivation. Exactly Nourai's claim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"p. 254 s.v. *mad 'to curdle, coagulate'\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: MMP m's- \\\"to coagulate, become hard\\\" … *NWIR: NP māsidan/mās- \\\"to coagulate\\\" … NP māst \\\"yoghurt\\\", Ard. maske \\\"butter\\\" … *SANSKRIT: Skt. mástu- (n.) \\\"sour cream\\\" (< *mad-stu-)' — the whole Iranian family, with no hint of a Semitic loan.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 55 (PHD_mackenzie.txt line 3493)\", \"stance\": \"supports\", \"note\": \"'māst [m'st | N …] curds, sour milk' — the Middle Persian antecedent Nourai's arrow needs.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. madtós (IEC.txt line 10239)\", \"stance\": \"supports\", \"note\": \"'Skt. cf. mástu, n. \\\"sour cream, whey\\\" … Per. māst \\\"sour milk\\\"' under the same lemma.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in via BQT vol. 4 p. 1941 footnote (the six-volume Farhang is not online)\", \"stance\": \"supports\", \"note\": \"Mo'in's own etymological note is the BQT footnote quoted above; the 2-vol. condensation on disk (MON_part1/2.txt) gives only definitions.\"},\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey s.v. māsta- (ISS_alt_DKS.txt line 6058)\", \"stance\": \"supports\", \"note\": \"'Zor.P., N.Pers. mast \\\"thick milk\\\", O.Ind. mástu- \\\"thick cream\\\" (-d-t-, or -dst-), N.Pers. masīdan \\\"to coagulate\\\" (-ds- or -dt-)' — Bailey works out precisely the cluster development.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"madati : a water bird, mina\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"Sanskrit madati is a verb, 'it bubbles, it gladdens, it is exhilarated' (RV+; EWAia II 299), and it never means 'a water bird'. The gloss has been carried down from the box above it (node #1) and the intermediate step has been dropped: the source Nourai is following, AHD, spells the chain out — 'myna: [Hindi mainā, perhaps from Sanskrit madanaḥ, from madana-, delightful, joyful, from madati, it bubbles]' (AHD online s.v. myna; identically Watkins 1985 p. 38 s.v. mad-: 'Sanskrit madati, \\\"it gladdens, it bubbles,\\\" hence madana-, delightful, joyful, hence madanaḥ, a myna bird: MYNA'). So the derivation drawn (Sanskrit → Hindustani mainā → English myna) is exactly AHD's, but the form that belongs in the box is madanaḥ 'myna bird', with madati as its base. I checked the printed page (refs/ocr/BOOK/317.png): the book prints 'madati : a water bird, mina', so the extraction is faithful and the fault is the book's — a compression error, plus the same water-bird gloss that was misplaced in node #1.\",\n          \"derivation_fa\": \"madati در سنسکریت فعل است: «می‌جوشد، شاد می‌کند، سرمست می‌شود» (از ریگ‌وداا؛ مایرهوفر، ج ۲ ص ۲۹۹) و هرگز معنی «پرندهٔ آبی» ندارد؛ این معنی از جعبهٔ بالاتر (گرهٔ ۱) پایین آمده و حلقهٔ میانی افتاده است. منبع نورایی، یعنی فرهنگ American Heritage، زنجیره را کامل می‌آورد: «myna: از هندی mainā، شاید از سنسکریت madanaḥ، از madana- «دلپذیر، شادی‌بخش»، از madati «می‌جوشد»» و واتکینز نیز (۱۹۸۵، ص ۳۸) همین را دارد. پس پیکانِ کشیده‌شده (سنسکریت ← هندوستانی mainā ← انگلیسی myna) درست و همان چیزی است که AHD می‌گوید، ولی صورتی که باید در جعبه می‌نشست madanaḥ «پرندهٔ مینا» بود و madati پایهٔ آن است. صفحهٔ چاپی را دیدم (refs/ocr/BOOK/317.png): در کتاب هم «madati : a water bird, mina» چاپ شده؛ پس خطای خوانش اسکن نیست، خطای فشرده‌سازی خودِ کتاب است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"madati : a water bird, mina\",\n          \"correct_form\": \"Sanskrit madanaḥ 'a myna bird' (from madana- 'delightful', from madati 'it gladdens, bubbles')\",\n          \"sources\": [\n            \"https://www.ahdictionary.com/word/search.html?q=myna\",\n            \"https://en.wiktionary.org/wiki/myna\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:867\", \"status\": \"supports\", \"note\": \"The 1975 New College body volume is not on disk, but its etymology survives verbatim in the current online AHD s.v. myna: '[Hindi mainā, perhaps from Sanskrit madanaḥ, from madana-, delightful, joyful, from madati, it bubbles.]' (archived data/verification/sources/web/72c584622c6ab927.txt), and the same chain is in Watkins' appendix to the very edition Nourai cites (AHD_watkins1985.txt line 708). p. 867 is where 'myna' falls in the m-range of that edition, so the citation is consistent; the wording, not the page, is what I could verify.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 38 s.v. mad- (AHD_watkins1985.txt line 708)\", \"stance\": \"supports\", \"note\": \"'1. Sanskrit madati, \\\"it gladdens, it bubbles,\\\" hence madana-, delightful, joyful, hence madanah, a myna bird: MYNA.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein, s.v. mad-/madarosis material (KLN_1966.txt line 23247)\", \"stance\": \"silent\", \"note\": \"Klein lists the *mad- family ('L. madere … mattus … OE. mæst … Cp. madarosis, mast, masto-, mastoid, mate, mattoid, must') but has no myna entry, so he neither supports nor contradicts the bird.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. MYNA, MINA (HJB.txt line 15241)\", \"stance\": \"partial\", \"note\": \"'MYNA, MINA, &c. s. Hind. mainā. A name applied to several birds of the family of starlings. The common myna is the Acridotheres tristis of Linn. …' — confirms the Hindi source of the English word but offers no Sanskrit etymon.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Hindustani\",\n          \"words\": \"mainâ : mina\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Hindi/Urdu मैना / مینا mainā is the ordinary Indian name of the starling Acridotheres tristis, and both AHD ('Hindi mainā, perhaps from Sanskrit madanaḥ') and en.wiktionary ('Borrowed from Hindi मैना (mainā) / Urdu مینا (mainā), from Sanskrit मदन (madana)') derive it from the Sanskrit word of node #5, the vowel ai reflecting Middle Indic development of madana- through a Prakrit *maïṇā with loss of intervocalic -d- (a regular Prakrit change) and contraction. Hobson-Jobson s.v. MYNA gives 'Hind. mainā' as the immediate source of the English form; Whitworth's Anglo-Indian Dictionary adds the Marathi variant maina.\",\n          \"derivation_fa\": \"«مینا» (हिन्दी मैना) نام معمول سارِ هندی (Acridotheres tristis) است و هم فرهنگ American Heritage («از هندی mainā، شاید از سنسکریت madanaḥ») و هم ویکی‌واژه («وام‌گرفته از هندی मैना، از سنسکریت मदन») آن را از همان واژهٔ سنسکریت گرهٔ ۵ می‌گیرند؛ مصوت ai بازتاب تحول هندی میانه است: در پراکریت دالِ میان‌واکه‌ای می‌افتد (*maïṇā) و سپس دو واکه به هم می‌رسند. هابسن-جابسن ذیل MYNA همین «هندی mainā» را سرچشمهٔ بی‌واسطهٔ واژهٔ انگلیسی می‌داند و ویتورث گونهٔ مراتی maina را نیز می‌افزاید.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/myna\",\n            \"https://www.ahdictionary.com/word/search.html?q=myna\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the parent box carries AHD:867, whose etymology (Hindi mainā < Skt. madanaḥ) is quoted in node #5.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson (2nd ed. 1903), s.v. MYNA, MINA (HJB.txt lines 15231, 15241)\", \"stance\": \"supports\", \"note\": \"'MYNA, MINA, &c. s. Hind. mainā. A name applied to several birds of the family of starlings … among the most teachable of imitative birds, articulating words with great distinctness.'\"},\n            {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary (1885), s.v. Myna (AID.txt line 4815)\", \"stance\": \"supports\", \"note\": \"'Myna. [The Marāthi maina.] The name of a very common Indian bird, a kind of starling, the acridotheres tristis.' — and line 4553 'Mina. More commonly Myna.'\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"mina, myna : a bird\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English myna (also mina, mynah) is an 18th-c. Anglo-Indian borrowing of Hindi mainā, taken over by British residents in India — Hobson-Jobson's earliest naturalists' notices are Eleazar Albin's plate of 1738 and Pepys's talking bird of 1664 (which Newton was inclined to identify as the myna) — and the spelling with -y- and final -h is the usual English orientalising of Hindi ai. The chart's chain Sanskrit → Hindustani → English is exactly the one AHD and en.wiktionary give; only the Sanskrit form in node #5 is misprinted.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی myna (و گونه‌های mina، mynah) وام‌واژه‌ای انگلیسی-هندی از سدهٔ هجدهم است که بریتانیایی‌های ساکن هند از هندی mainā گرفتند؛ هابسن-جابسن کهن‌ترین گواهی‌های طبیعی‌دانان را تصویر الیزار آلبین (۱۷۳۸) و پرندهٔ سخنگوی پپیس (۱۶۶۴) می‌شمارد. نگارش با y و h پایانی همان شیوهٔ رایج انگلیسی در نوشتن ai هندی است. زنجیرهٔ نمودار (سنسکریت ← هندوستانی ← انگلیسی) دقیقاً همان است که AHD و ویکی‌واژه می‌آورند؛ تنها صورت سنسکریت در گرهٔ ۵ نادرست چاپ شده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/myna\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference given for this node; covered by AHD:867 on the grandparent box (quoted at node #5).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. MYNA (HJB.txt lines 15241-15247)\", \"stance\": \"supports\", \"note\": \"The article treats myna as an English word of Hindi origin and cites Pepys, Diary, 26 April 1664, with Prof. Newton's identification, and Albin's 1738 plate as the earliest figure.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966, m-section\", \"stance\": \"silent\", \"note\": \"Grep of KLN_1966.txt / KLN_1971.txt for 'myna', 'mynah', 'maina' returns nothing — Klein has no entry for the bird.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Germanic\",\n          \"words\": \"(no words given)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty pass-through box stands for Proto-Germanic *matiz 'food' (< PIE *mad-i-) and its derivative *ga-matjô 'one who shares food', the two forms that yield the English words in node #9. Both are standard: Watkins 1985 s.v. mad- has 'Suffixed form *mad-i- in Germanic *mati- in: a. Old English mete, food: MEAT; b. Middle Low German (ge)mate … companion: MATE', and Pokorny 695 lists 'got. mats \\\"Speise\\\", aisl. matr, ags. mete, ahd. maz … mnd. mat(e) \\\"Kamerad\\\"'. The semantic core is the root's 'food/fattening' branch, seen also in OHG mast 'mast, fodder' and Gothic matjan 'to eat'.\",\n          \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ ژرمنی آغازین *matiz «خوراک» (از هندواروپایی *mad-i-) و مشتق آن *ga-matjô «هم‌خوراک، آن‌که خوراک را با کسی شریک است» است؛ همین دو صورت‌اند که واژه‌های گرهٔ ۹ از آنها می‌آیند. هر دو در منابع معیارند: واتکینز ذیل mad- می‌آورد «صورت پسوندی *mad-i- در ژرمنی *mati-: الف) انگلیسی کهن mete «خوراک» ← MEAT؛ ب) آلمانی سفلای میانه (ge)mate … «همراه» ← MATE» و پوکورنی (ص ۶۹۵) نیز got. mats، aisl. matr، ags. mete، ahd. maz و mnd. mat(e) «رفیق» را برمی‌شمارد. هستهٔ معنایی همان شاخهٔ «خوراک/پرورده کردن» ریشه است که در ahd. mast «علوفه» و گوتیک matjan «خوردن» هم دیده می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/meat\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Nourai cites AHD without a page; Watkins 1985 p. 38 s.v. mad- (AHD_watkins1985.txt line 708) has exactly this Germanic branch: '*mad-i- in Germanic *mati- … Old English mete, food: MEAT … Middle Low German (ge)mate, \\\"he with whom one shares one's food,\\\" companion: MATE'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny 695 (POK_full.txt lines 57082-57090)\", \"stance\": \"supports\", \"note\": \"'Old High German mast \\\"food, fattening, acorn mast\\\" … Gothic mats \\\"dish, food\\\", Old Icelandic matr m., Old English mete m., Old High German maz n. … Middle Low German mat(e) \\\"buddy, friend, esp. in the nautical slang\\\" (Maat), Old High German gamazzo \\\"buddy, friend\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. meat (KLN_1966.txt line 23247)\", \"stance\": \"supports\", \"note\": \"'… OE. mæst \\\"mast (of beech)\\\", mæstan \\\"to fatten\\\" … Cp. also … mate, \\\"companion\\\" … For sense development of OE. mete, etc., \\\"food\\\", into E. meat, etc., \\\"flesh of animals\\\", cp. Heb. leḥem \\\"bread, food\\\", with Arab. laḥm \\\"flesh\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"meat, mate 1 : companion\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"meat < Middle English mete < Old English mete 'food' < Proto-West Germanic *mati < PGmc *matiz < PIE *meh₂d-; the narrowing from 'food' generally to 'flesh' is a late Middle English/Early Modern development (still 'food' in 'meat and drink'). mate 'companion' < Middle English mate, borrowed from Middle Low German mate 'messmate' (which displaced native Middle English mett(e) < OE ġemetta 'sharer of food, table-guest'), from Old Saxon gimato < PGmc *ga-matjô, literally 'he with whom one shares one's food' — the same formation as Latin com-pāniō 'bread-fellow' and Russian odnokášnik. Both are the standard etymologies (Wiktionary, Klein, Watkins) and both belong under *mad-; note that this mate is a different word from mate 'to checkmate' (node #12's neighbour), which is the Arabic one.\",\n          \"derivation_fa\": \"meat از انگلیسی میانهٔ mete و آن از انگلیسی کهن mete «خوراک»، از ژرمنی باختری *mati و ژرمنی آغازین *matiz، از هندواروپایی *meh₂d-؛ تخصیص معنایی از «خوراک» به «گوشت» تحولی متأخر (پایان انگلیسی میانه و آغاز دورهٔ نو) است و در ترکیب meat and drink هنوز معنی کهن مانده است. mate «همراه» از انگلیسی میانهٔ mate، وام‌گرفته از آلمانی سفلای میانه mate «هم‌سفره» (که جای صورت بومی mett(e) از ġemetta انگلیسی کهن را گرفت)، از ساکسون کهن gimato و ژرمنی آغازین *ga-matjô، تحت‌اللفظ «آن‌که خوراک خود را با او شریک می‌شوی» — ساختی همانند com-pāniō لاتینی («هم‌نان») و одноќашник روسی. هر دو اشتقاق معیارند (ویکی‌واژه، کلاین، واتکینز) و هر دو به همین ریشه می‌رسند؛ توجه شود که این mate با mate «مات کردن (در شطرنج)» — که واژه‌ای عربی است — یکی نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/meat\",\n            \"https://en.wiktionary.org/wiki/mate\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on the node; the parent box's bare 'AHD' citation covers it (Watkins 1985 p. 38 lists both MEAT and MATE under mad-).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. meat/mate (KLN_1966.txt line 23247)\", \"stance\": \"supports\", \"note\": \"The *mad- article cross-refers to 'mast, \\\"fruit of beech\\\", masto-, mastoid, mate, \\\"companion\\\", mattoid, must' — i.e. Klein files mate 'companion' under this root, as Nourai does.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.v. meat/mate\", \"stance\": \"supports\", \"note\": \"SKT.txt has the same Germanic derivation of meat from OE mete and of mate from Low German; his entry for L. mattus (line 11272) shows he keeps the two mate words apart.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index p. 91 (AHD_watkins1985.txt line 1829)\", \"stance\": \"supports\", \"note\": \"The index line reads 'MATCH2 meug-2 | MATE1 mad- | MATELOTE neud- …' — MATE1 (the companion) is assigned to mad-, while MAT/MATTE appear nowhere in the appendix (see node #12).\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Latin\",\n          \"words\": \"mattus : drunk, not sober, dull\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin mattus 'drunk, maudlin' (Petronius, Sat. 41 matus; the glossaries mattus 'tristis') is regularly explained as a syncopated *maditus, participle of madēre 'to be wet, to be drunk', with assimilation dt > tt: Pokorny 694 'lat. madeō, -ēre \\\"naß sein\\\", mattus \\\"trunken\\\" (*madi-to-s)'; en.wiktionary s.v. mattus 'Syncopated from *madĭtus (with subsequent assimilation of /dt/ to /tt/), from madēre … from PIE *meh₂d-'; Buck p. 184 'mattus, Petr. Sat. 41 and in glosses \\\"drunk\\\" fr. *maditus'. Ernout-Meillet are more cautious ('Mattus peut représenter une prononciation vulgaire (dialectale) de *maditus'; they even wonder whether matus 'ivre' and mattus 'tristis' are two words). Nourai's NOTE reports FSD's derivation of mattus from Persian māt 'confused' via Arabic; that is untenable and modern scholarship rejects it — matus is already in Petronius in the 1st century CE, centuries before any Arabic or New Persian influence on Latin, and the Latin form is fully accounted for within the language. Funk & Wagnalls does hold that view (the claim appears s.v. casemate: 'feeble, false, < LL. mattus, dull, < Per. mat, confounded'), so Nourai reports his source faithfully; the source is simply wrong.\",\n          \"derivation_fa\": \"mattus لاتینی «مست، خمار» (در پترونیوس، ساتیریکون ۴۱ به صورت matus؛ در واژه‌نامه‌های کهن mattus «اندوهگین») به‌قاعده از *maditus بازسازی می‌شود، یعنی صفت مفعولی madēre «تر بودن، مست بودن» با افتادن واکهٔ میانی و همگونی dt > tt: پوکورنی ص ۶۹۴ «lat. madeō، mattus «مست» (*madi-to-s)»؛ ویکی‌واژه ذیل mattus همین را دارد؛ باک نیز (ص ۱۸۴) «mattus … از *maditus». ارنو-مِیه محتاط‌ترند («mattus می‌تواند تلفظ عامیانهٔ *maditus باشد») و حتی احتمال می‌دهند matus و mattus دو واژهٔ جدا باشند. یادداشتِ نورایی از FSD نقل می‌کند که mattus لاتینی از «مات» فارسی (وام از عربی) آمده است؛ این ادعا پذیرفتنی نیست و پژوهش امروزی آن را رد می‌کند، زیرا matus در سدهٔ یکم میلادی در پترونیوس گواهی دارد، یعنی سده‌ها پیش از هر تأثیر عربی یا فارسیِ نو بر لاتین، و صورت لاتینی درون خودِ زبان توضیح‌پذیر است. فرهنگ Funk & Wagnalls واقعاً چنین نظری دارد (این ادعا ذیل casemate آمده: «< LL. mattus، dull، < Per. mat، confounded»)، پس نورایی منبع خود را درست نقل کرده؛ خودِ منبع نادرست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/mattus\",\n            \"https://www.etymonline.com/word/matte\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:694\", \"status\": \"supports\", \"note\": \"POK_full.txt line 57091 / POK_02.txt line 5653: 'Latin madeō, -ere \\\"to be wet, be moist, drip, flow\\\", mattus \\\"drunk, intoxicated\\\" (*madi-to-s)' — on the page Nourai cites.\"},\n            {\"ref\": \"AHD:805\", \"status\": \"supports\", \"note\": \"The 1975 body volume is not on disk, but the AHD etymology is unchanged online s.v. matte: '[French, curdled milk, matte, from feminine of obsolete mat, compact, from Old French, dull, from Latin mattus, stupefied; see MAT2.]' (archived data/verification/sources/web/67cd3ea6f6278d25.txt) — i.e. AHD's own entry gives exactly the Latin mattus > (Old) French > English route the chart draws, and p. 805 is where mat/matte falls in that edition.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. matus (LAT.txt lines 36908-36917)\", \"stance\": \"partial\", \"note\": \"'matus, -a, -um: ivre. Mot vulgaire (Petr. 41) … On lit aussi mattus (natus): tristis, CGL IV 114,4 … Mais peut-être sont-ce deux mots différents. Le rapprochement de l'ital. matto est aujourd'hui contesté … Mattus peut représenter une prononciation vulgaire (dialectale) de *maditus.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck ch. 4.76 'drunk', p. 265 area (SYN.txt line 8297)\", \"stance\": \"supports\", \"note\": \"'Skt. matta- \\\"drunk\\\", pple. of mad- … = Av. mad- \\\"get drunk\\\" … : Lat. madēre \\\"be wet\\\" also \\\"be drunk\\\" (whence madidus …; mattus, Petr. Sat. 41 and in glosses \\\"drunk\\\" fr. *maditus), Grk. madáō … Walde-P. 2.230f.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. mattoid (KLN_1966.txt line 23156)\", \"stance\": \"supports\", \"note\": \"'The first element derives fr. L. mattus, \\\"intoxicated\\\", fr. mad(i)dus, \\\"moist, wet; drunk, intoxicated\\\", fr. madēre … fr. I.-E. base mad-, \\\"wet, moist, dripping; to drip\\\". See meat and cp. mast, \\\"fruit of beech\\\".' Klein derives Latin mattus from mad- — it is only the French/English mat 'dull' that he takes from Arabic (node #12).\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. casemate (FSD_vol1.txt line 59108)\", \"stance\": \"supports\", \"note\": \"Verifies that FSD really holds the view Nourai's NOTE reports: '[F. … < It. casamatta, < casa … + matta, f. of matto, feeble, false, < LL. mattus, dull, < Per. mat, confounded.]' The cited page 1526 could not be located — the FSD OCR on disk carries no usable page markers — but the claim is FSD's.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"French\",\n          \"words\": \"(no words given)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The empty box stands for Old French mat 'beaten down, withered, afflicted, dejected; dull' > French mat 'dull, lusterless' (and its feminine matte 'curdled milk, matte'), the immediate source of the English words in node #12. AHD asserts the Latin descent ('French … from feminine of obsolete mat, compact, from Old French, dull, from Latin mattus, stupefied'), and Etymonline gives it first but hedges: OF mat 'is perhaps from Latin mattus \\\"maudlin with drink\\\" … Or the French word might represent a transferred use from chess of mater \\\"to checkmate, defeat\\\", from Arabic'. The homonymy is real and old — OF mat 'checkmated' (from Arabic māt, in šāh māt) is attested in the chess sense from the 12th c. — so the French link in the chain cannot be called established, only plausible.\",\n          \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ فرانسهٔ کهن mat «شکست‌خورده، پژمرده، افسرده؛ بی‌فروغ» و فرانسهٔ mat «بی‌درخشش» (و مؤنث آن matte) است، یعنی سرچشمهٔ بی‌واسطهٔ واژه‌های گرهٔ ۱۲. فرهنگ American Heritage همان تبار لاتینی را قاطعانه می‌آورد («از مؤنث mat کهن … از فرانسهٔ کهن، از لاتینی mattus»)، ولی Etymonline آن را نخست و با احتیاط می‌آورد: «شاید از mattus لاتینی … یا شاید کاربردی گسترش‌یافته از mater شطرنجی «مات کردن» که از عربی است». این هم‌آوایی واقعی و کهن است — mat «مات» در فرانسهٔ کهن از سدهٔ دوازدهم در معنی شطرنجی گواهی دارد — پس حلقهٔ فرانسه در این زنجیره را نمی‌توان اثبات‌شده دانست و تنها «پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/matte\",\n            \"https://www.ahdictionary.com/word/search.html?q=matte\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for the French box; the flanking boxes carry POK:694 and AHD:805, both quoted at nodes #10 and #12.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. mat, adj. (KLN_1966.txt line 23103, printed p. 946)\", \"stance\": \"contradicts\", \"note\": \"'mat, adj., dull (said of color or a surface). — F., \\\"dull, lusterless, unpolished\\\", fr. OF. mat, \\\"defeated, afflicted, depressed, dejected; dull\\\", fr. Arab. māt in the sentence māt ash-shāh, \\\"the king has died\\\". The word mat, orig. used only as a term of chess, gradually developed also the meanings \\\"faint, feeble, dull-colored\\\".' Klein routes the French word through Arabic, not Latin.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. matus (LAT.txt line 36913)\", \"stance\": \"partial\", \"note\": \"'Le rapprochement de l'ital. matto est aujourd'hui contesté; cf. M.L. s.u. *mattus, 5438' — the Romance descendants of Latin mattus are themselves disputed in Romance philology.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"mat, matte : dull, also picture frame\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English mat/matt/matte 'lusterless, dull' is first recorded in the 1640s and comes from French mat 'dull, dead surface'; the noun matte 'sheet of backing material, picture-frame mount' (1845) is the French noun mat 'dull surface or finish' (15th c.), later confused with the unrelated mat 'woven fabric' (< Late Latin matta, a Punic loan — Klein, s.v. mat, n.). So the chart's last step, French → English, is certain; what is uncertain is the step above it. Nourai's own NOTE flags this correctly: KLN:946 does derive these words from Arabic māt (šāh māt 'the king is dead'), i.e. from a Semitic root, and AHD:805 derives them from Latin mattus. Modern scholarship has not settled it: Etymonline sets out both options side by side, with the Latin one first ('perhaps from Latin mattus …  Or the French word might represent a transferred use from chess'), while AHD backs Latin and Klein backs Arabic. The chart and its own note between them represent the state of the art, so the node is plausible rather than confirmed; and it is worth noting that Watkins' appendix, the part of AHD that assigns words to roots, lists MATE1 under mad- but neither MAT nor MATTE anywhere.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی mat/matte «بی‌درخشش، مات» از دههٔ ۱۶۴۰ گواهی دارد و از فرانسهٔ mat «سطح مات» آمده است؛ اسمِ matte «مقوّای پشت‌کار، حاشیهٔ قاب عکس» (۱۸۴۵) نیز همان اسم فرانسهٔ mat (سدهٔ پانزدهم) است که بعدها با mat «حصیر» (از لاتینی متأخر matta، وام‌واژه‌ای فنیقی) درآمیخته است. پس آخرین گام نمودار — فرانسه به انگلیسی — قطعی است؛ آنچه قطعی نیست گام بالاتر است. خودِ نورایی در یادداشت درست اشاره کرده: کلاین (ص ۹۴۶) این واژه‌ها را از «مات» عربی (شاه مات) و ریشه‌ای سامی می‌گیرد و AHD (ص ۸۰۵) از mattus لاتینی. پژوهش امروزی میان این دو داوری نکرده است: Etymonline هر دو را کنار هم می‌آورد و لاتینی را نخست می‌گذارد، AHD جانب لاتین را می‌گیرد و کلاین جانب عربی را. بنابراین نمودار همراه یادداشتش وضع کنونی دانش را نشان می‌دهد و این گره «با احتیاط پذیرفتنی» است؛ گفتنی است که پیوستِ واتکینز — همان بخشی از AHD که واژه‌ها را به ریشه‌ها نسبت می‌دهد — MATE1 را زیر mad- آورده ولی MAT و MATTE را در هیچ ریشه‌ای جای نداده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/matte\",\n            \"https://www.ahdictionary.com/word/search.html?q=matte\",\n            \"https://en.wiktionary.org/wiki/matte\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:805\", \"status\": \"supports\", \"note\": \"Current AHD s.v. matte: '[French, curdled milk, matte, from feminine of obsolete mat, compact, from Old French, dull, from Latin mattus, stupefied; see MAT2.]' — the chart's route exactly, with AHD's own cross-reference to its MAT2 entry (the adjective), which is what p. 805 of the 1975 edition carries.\"},\n            {\"ref\": \"KLN:946\", \"status\": \"supports\", \"note\": \"Verified for Nourai's NOTE: KLN_1966.txt has the page footers '946' at line 23090 and '947' at 23091, and the entry at line 23103 (i.e. on that leaf) reads 'mat, adj., dull … fr. OF. mat … fr. Arab. māt in the sentence māt ash-shāh, \\\"the king has died\\\"'. Nourai's page and his characterisation of Klein's view are both correct.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966, printed p. 946, s.v. mat (n.) and mat (adj.)\", \"stance\": \"partial\", \"note\": \"Klein separates three words: mat, n. 'coarse fabric' < Late Latin matta < Phoenician-Punic matta; mat, adj. 'dull' < French < Arabic māt; and (s.v. mattoid) Latin mattus < madēre. He thus supports the Latin origin of mattus but not of the English adjective.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary, vol. 1 only (A-?) on disk\", \"stance\": \"silent\", \"note\": \"The m-range is in the missing second volume, so Webster could not be consulted for mat/matte.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, s.v. mat / checkmate (SKT.txt line 11272)\", \"stance\": \"partial\", \"note\": \"Skeat's line 'L. mattus, [dull]' appears in a list of Greek/Latin comparanda; he treats chess mate from Arabic and does not connect the 'dull' adjective to Latin, leaving the question open as Etymonline does.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Madhaxa, Mazaxa, Madika\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Avestan maδaxa- m. / maδaxā- f. 'locust, grasshopper' (Bartholomae AiW 1114); Arsacid Middle Persian maδax; beside a variant *madika- / *maδika- (Hübschmann's reconstruction) that gives NP mēg/mayg\",\n      \"note\": \"The root box is right, and unusually well documented. Bartholomae AiW s.v. records 'j. maδaxa- m., -xā- f. \\\"Heuschrecke\\\", ein xrafstra-sches Tier' (Vd. 7.26), and closes with 'np. malax; vgl. maig; s. dazu Dst. Etlr. 3.195, Hbn. PSt. 100, 302, 364, Horn GIrPh. I b. 44, 57' — Bartholomae cites Hübschmann p. 100, the very page Nourai's HUB:100 points to. Hübschmann's note there ('1010. Arm. maraχ ist LW. und = arsacidisch-persisch maδax …, gehört also unmittelbar zu zd. maδaxā-. Np. maig wäre = ap. *madika- (= zd. *maδika-), vgl. paig') is the source of all three head-forms in the box, including 'Madika'. Two corrections: (a) the label 'Avestan / Old Persian' overstates the case — no Old Persian form is attested (Kent's lexicon has nothing), *madika- is a reconstruction; (b) the note about BQT's introduction is accurate as a report (Mo'in, Borhān-e Qāteʿ, introduction pp. 17-18, argues that the ultimate source is Sogdian and that malax rests on the same shape as Armenian maraχ), but that hypothesis has been superseded: current work (en.wiktionary s.v. ملخ, following Sims-Williams' Bactrian material) makes NP malax a loan from Bactrian μαλαχο, and Gharib's Sogdian dictionary has no locust word to offer. Nourai's 'Mazaxa' is simply the same maδaxa with the Book-Pahlavi convention of writing δ as z, as Mo'in's introduction also does (مذخ / maδax).\",\n      \"note_fa\": \"جعبهٔ ریشه درست است و به‌طور استثنایی خوب مستند. بارتولومه در فرهنگ ایرانی باستان می‌آورد: «maδaxa- (نرینه)، maδaxā- (مادینه) «ملخ»، از جانوران خرفستر» (وندیداد ۷.۲۶) و در پایان می‌نویسد «np. malax؛ قس maig؛ بنگرید به هوبشمان، مطالعات فارسی، ص ۱۰۰ …» — یعنی خودِ بارتولومه به همان صفحهٔ ۱۰۰ هوبشمان ارجاع می‌دهد که نورایی آورده است. یادداشت هوبشمان در آن‌جا («۱۰۱۰. maraχ ارمنی وام‌واژه است و برابر maδax فارسیِ اشکانی، پس بی‌واسطه به maδaxā- اوستایی می‌پیوندد. maig فارسی نو باید برابر *madika- پارسی باستان [= *maδika- اوستایی] باشد، قس paig») سرچشمهٔ هر سه صورتِ جعبه، از جمله «Madika»، است. دو اصلاح: نخست آنکه برچسب «اوستایی/پارسی باستان» گزافه است، زیرا هیچ صورت پارسی باستانی گواهی ندارد و *madika- بازسازی است (کنت هیچ ندارد)؛ دوم آنکه یادداشت نورایی دربارهٔ مقدمهٔ برهان قاطع نقلِ درستی است (معین در مقدمه، ص هفده–هیجده، اصل واژه را سغدی می‌داند و می‌گوید «ملخ» بر همان شکل ارمنی «مرخ» استوار است)، ولی این فرضیه امروز کنار گذاشته شده: پژوهش کنونی (ویکی‌واژه ذیل «ملخ»، بر پایهٔ مواد باکتری سیمز-ویلیامز) «ملخ» را وام‌واژه‌ای از باکتری μαλαχο می‌داند و فرهنگ سغدی قریب هیچ واژه‌ای برای ملخ ندارد. «Mazaxa» نورایی هم همان maδaxa است با شیوهٔ پهلوی که ذ را ز می‌نویسد، چنانکه مقدمهٔ معین نیز «مذخ / maδax» می‌آورد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%85%D9%84%D8%AE\",\n        \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%DA%AF%D9%88\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"HRN:227\", \"status\": \"supports\", \"note\": \"Horn's no. 1010 stands at the head of printed p. 227 (HRN.txt line 8787, right after the '— 227 —' footer): '1010. meig \\\"Heuschrecke\\\" … aw. maδaxa- \\\"Heuschrecke\\\" (Darmesteter, Et. ir. II, 197); phlv. maig (kaum maδag), bal. maδag, n. maδaχ, maδaγ (221). Np. melex, phlv.-pāz. malak (PPGl.), arm. maraχ, kurd. mala …, sar. malax sind LW. … oder setzen eine arische Dialektspaltung voraus'. Exactly Nourai's forms.\"},\n        {\"ref\": \"HUB:100\", \"status\": \"supports\", \"note\": \"Hübschmann, Persische Studien, note to Horn's no. 1010 on the p. 100/101 opening (HUB.txt line 3513 carries the '7*- 100 -' footer, the note follows at line 3518): 'Arm. maraχ ist LW. und = arsacidisch-persisch maδax ZDMG. 36, 133, gehört also unmittelbar zu zd. maδaxā-. Np. maig wäre = ap. *madika- (= zd. *maδika-), vgl. paig.' Bartholomae himself cites this as 'Hbn. PSt. 100', so Nourai's page number is the standard one.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 1114 s.v. maδaxa- (BRT.txt lines 19588-19592)\", \"stance\": \"supports\", \"note\": \"'j. maδaxa- m., -xā- f. \\\"Heuschrecke\\\", ein xrafstra-sches Tier: tē sūnō maδaxaγaēsa aogas.dastəma bavainti \\\"die verleihen der Spinne und der Heuschrecke am meisten Macht\\\" V. 7.26 … np. malax; vgl. maig; s. dazu … Hbn. PSt. 100 … — Pü.: matag-.' Note the Pahlavi-version form matag-, which is Nourai's 'matax'.\"},\n        {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. šāk (NYB_vol2_glossary.txt line 3599)\", \"stance\": \"supports\", \"note\": \"'an alternation -k : -x, -h is found in several ws … BP malak (FrP 8): NP malax \\\"locust\\\"; Av. (1114) maδaxa-, Arm. lw. maraχ id.: NP maig < *maδaka-' — Nyberg gives the Avestan column number (1114) and derives both NP forms as Nourai does.\"},\n        {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon\", \"stance\": \"silent\", \"note\": \"Grep of KNT.txt for 'madika', 'locust', 'grasshopper' returns nothing: there is no attested Old Persian word, so the box's 'Old Persian' rests entirely on Hübschmann's reconstruction *madika-.\"},\n        {\"src\": \"BQT\", \"where\": \"Mo'in's introduction to Borhān-e Qāteʿ, pp. 17-18 (BQT_v1_pages.txt leaves 25-26)\", \"stance\": \"supports\", \"note\": \"Leaf 26: 'در زبان‌های ایرانی وجود دارد: اول مذخ maδax (در قدیم مذخه maδaxa) که مختص زبان شمال ایران — یعنی اشکانی — است و وجود آن … از کلمهٔ دخیل ارمنی مرخ maraχ تأیید می‌شود. دوم میگ mayg متعلق به زبان پارسی به معنی اخص — یعنی لهجهٔ جنوب غربی — و آن در اصل مذکه maδaka، مذیکه maδika بوده است. سوم لغتی که در زبان فارسی کنونی نیز استعمال می‌شود — ولی قطعاً دخیل است — ملخ malax است … اما اطلاعی که از اوستا رسیده مؤید آنست که اصل کلمه سغدی است'. This is precisely the passage Nourai's root note reports, and it is also where his three head-forms (maδaxa / maδax / maδika) come from.\"},\n        {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary\", \"stance\": \"silent\", \"note\": \"Grep of SOD.txt for 'locust' and 'ملخ' returns only the title of Henning's Festschrift 'A Locust's Leg' — Gharib records no Sogdian locust word, so Mo'in's Sogdian hypothesis cannot be checked against the Sogdian lexicon.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"madhax, mazax, matax : grasshopper; maig : a kind of grasshopper, shrimp\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Middle Iranian layer is real but the four forms belong to different dialects and different degrees of attestation. maδax is the Arsacid (Parthian/north-west) form, reconstructed by Hübschmann from Armenian maraχ (Armenian renders Iranian δ by r, cf. Mar-kʿ 'Medes' < *Māδ) — 'arsacidisch-persisch maδax', HUB p. 100; 'madhax' and 'mazax' are just two ways of writing that δ (dh in Avestan transcription, z in Book Pahlavi convention). matax is genuinely attested, as the Pahlavi rendering of Avestan maδaxa- in the Pahlavi Vendidad (Bartholomae 'Pü.: matag-'), beside malak in the Bundahišn (47.10, per Hübschmann) and in Frahang ī Pahlavīg 8 (per Nyberg). maig is the south-western (Persian proper) form, from *maδika-/*maδaka- with loss of intervocalic δ before the front vowel and diphthongisation — Horn 'phlv. maig (kaum maδag)'. MacKenzie's Concise Pahlavi Dictionary has none of these words, so all rest on the older literature; and the shrimp sense belongs to the New Persian stage (node #2), not to Pahlavi.\",\n          \"derivation_fa\": \"لایهٔ ایرانی میانه واقعی است، ولی این چهار صورت به گویش‌های مختلف و درجات گواهی مختلف تعلق دارند. maδax صورت اشکانی (پارتی/شمال‌غربی) است که هوبشمان از ارمنی maraχ بازسازی کرده — ارمنی ذِ ایرانی را با r می‌نویسد، مانند Mar-kʿ «مادها» از *Māδ — و «madhax» و «mazax» تنها دو شیوهٔ نوشتن همان ذ است (dh در آوانگاری اوستایی، z در سنت پهلوی). matax گواهی راستین دارد: برگردان پهلویِ maδaxa- اوستایی در وندیداد پهلوی (بارتولومه: «Pü.: matag-») در کنار malak در بندهش (۴۷.۱۰ به گفتهٔ هوبشمان) و در فرهنگ پهلویگ ۸ (به گفتهٔ نیبرگ). maig صورت جنوب‌غربی (پارسیِ خاص) است، از *maδika-/*maδaka- با افتادن ذِ میان‌واکه‌ای پیش از واکهٔ پیشین و پیدایش مصوت مرکب — هرن: «phlv. maig (kaum maδag)». فرهنگ کوچک پهلوی مکنزی هیچ‌یک از این واژه‌ها را ندارد، پس همه بر ادبیات کهن‌تر تکیه دارند؛ معنی «میگو» نیز به مرحلهٔ فارسی نو تعلق دارد (گرهٔ ۲) نه به پهلوی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%84%D8%AE\",\n            \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%DA%AF%D9%88\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:227\", \"status\": \"supports\", \"note\": \"Horn no. 1010 (p. 227): 'phlv. maig (kaum maδag), bal. maδag, n. maδaχ, maδaγ … Np. melex, phlv.-pāz. malak (PPGl.)' — the Pahlavi maig and malak of this node.\"},\n            {\"ref\": \"HRN:222\", \"status\": \"not_found\", \"note\": \"Printed p. 222 of Horn's Grundriss (HRN.txt lines 8564-8600, between the '— 221 —' and '— 222 —' footers) carries nos. 985-989 (meγ, meγz, muft, meger, meges) and nothing about locusts. The '222' looks like a mis-citation of the internal cross-reference '(221)' inside no. 1010 (Geiger's Balochi number), or a slip for 227.\"},\n            {\"ref\": \"BQT:2031\", \"status\": \"supports\", \"note\": \"BQT vol. 4 pdf p. 114 = printed 2031: the ملخ page, whose footnote reads 'ملخ - بفتح اول ودوم، در اوستا maδaxa-، و در گزارش پهلوی maδax، در زبان ارمنی maraχ …، و رك: اسشق ص ۲۲۷ [= Horn p. 227]. درباب این کلمه توضیح کافی در مقدمهٔ کتاب حاضر ص هفده-هیجده داده شده است' — Avestan, Pahlavi and Armenian forms plus the pointer to the introduction that Nourai's root note reports.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 100-101 (note to Horn 1010) and § 92 b, p. 201 (HUB.txt lines 3518, 7081)\", \"stance\": \"supports\", \"note\": \"p. 201: 'maig \\\"Heuschrecke\\\" (neben malax) = phl. maig (und malak Bdh. 47,10), bal. maδaγ, madax, arm. maraχ, zd. maδaxā-'; pp. 100-101: 'Np. maig wäre = ap. *madika- (= zd. *maδika-), vgl. paig.'\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg II, glossary (NYB_vol2_glossary.txt line 3599)\", \"stance\": \"supports\", \"note\": \"'BP malak (FrP 8): NP malax \\\"locust\\\"; Av. (1114) maδaxa-, Arm. lw. maraχ id.: NP maig < *maδaka-' — Book Pahlavi malak is attested in the Frahang, and maig goes back to *maδaka-.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (PHD_mackenzie.txt), searched 'malax', 'malak', 'matag', 'maig', 'maδ'\", \"stance\": \"silent\", \"note\": \"No locust word at all; the only m-a-d entries are '1madag … female' and '2madag … essence, substance', unrelated. So the Pahlavi forms of the chart are not in the standard concise dictionary.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1114, end of the maδaxa- article (BRT.txt line 19592)\", \"stance\": \"supports\", \"note\": \"'— Pü.: matag-' — the Pahlavi-version form, i.e. Nourai's 'matax', attested as the gloss of Avestan maδaxa-.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"malax «ملخ» : grasshopper; mayg «میگ» (میگو) : shrimp\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both New Persian words are real and modern scholarship draws exactly the two lines the chart draws, with one refinement. ملخ malax 'locust' continues *maδaxa- but not by regular inheritance: the change δ > l is foreign to Persian (Hübschmann § 96: 'Für altes δ erscheint ausnahmsweise l in malax \\\"Heuschrecke\\\" (neben regelmässigem maig § 92 b) = zd. maδaxa-'), so Horn already declared malax a loanword, Mo'in's introduction thought the donor Sogdian, and en.wiktionary now identifies it as a borrowing from Bactrian μαλαχο (malakho) via a Middle Persian *malax, written Pazand malak; Pashto malax, Armenian maraχ, Ossetic mætyx and Khwarezmian mθx belong to the same much-varied set, the variation itself being ascribed to the taboo on naming the locust. میگ mayg (whence میگو mīgū 'shrimp, prawn') is the inherited south-western form, from MP mdk' /ma(y)ik/ < *madika-, with میگو = mayg + the MP suffix -ūg '-like'; the semantic shift 'locust' > 'shrimp' is the familiar 'locust of the sea' metaphor, and it is documented inside Persian itself: Borhān-e Qāteʿ s.v. ملخ آبی glosses it 'نوعی از ماهی کوچک … که آنرا بعربی اربیان گویند' (Arabic irbiyān = shrimp), and Mo'in's Farhang s.v. میگو gives the synonyms 'ملخ دریایی؛ جرادالبحر، اربیان … ملخ بی‌بال، ملخ آبی'.\",\n          \"derivation_fa\": \"هر دو واژهٔ فارسی نو راستین‌اند و پژوهش امروزی دقیقاً همان دو خطی را می‌کشد که نمودار کشیده است، با یک اصلاح. «ملخ» بازماندهٔ *maδaxa- است اما نه از راه میراث قاعده‌مند: بدل شدن ذ به ل در فارسی قاعده نیست (هوبشمان، بند ۹۶: «برای ذِ کهن به‌طور استثنایی l در malax «ملخ» ظاهر می‌شود، در برابر maig که قاعده‌مند است»)، از این‌رو هرن آن را وام‌واژه خوانده، معین در مقدمهٔ برهان قاطع خاستگاه را سغدی پنداشته، و ویکی‌واژه امروز آن را وام‌واژه‌ای از باکتری μαλαχο می‌داند که از راه فارسی میانهٔ *malax (به پازند malak) آمده است؛ پشتو malax، ارمنی maraχ، آسی mætyx و خوارزمی mθx نیز به همان مجموعهٔ پرگونهٔ واژه‌ها تعلق دارند و این پرگونگی را به تابوی نام‌بردن از ملخ نسبت می‌دهند. «میگ» (و از آن «میگو») صورت میراثی جنوب‌غربی است، از فارسی میانهٔ mdk‌ / ma(y)ik از *madika-، و «میگو» = میگ + پسوند ‎-ūg‎ فارسی میانه به معنی «مانند»؛ تحول معنایی «ملخ» به «میگو» همان استعارهٔ «ملخ دریا» است و در خودِ فارسی سند دارد: برهان قاطع ذیل «ملخ آبی» می‌نویسد «نوعی از ماهی کوچک … که آنرا بعربی اربیان گویند» و فرهنگ معین ذیل «میگو» برابرهای «ملخ دریایی، جرادالبحر، اربیان، ملخ بی‌بال، ملخ آبی» را می‌آورد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%84%D8%AE\",\n            \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%DA%AF%D9%88\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:227\", \"status\": \"supports\", \"note\": \"Horn no. 1010 (p. 227) lists 'Np. melex' with arm. maraχ, kurd. mala, sar. malax and calls them loanwords, and gives 'meig' as the head-word of the entry — both of Nourai's Persian forms, though Horn dissents about malax being inherited.\"},\n            {\"ref\": \"HRN:222\", \"status\": \"not_found\", \"note\": \"As at node #1: printed p. 222 has Horn nos. 985-989 (meγ 'Tiefe', meγz, muft, meger, meges) and no locust material.\"},\n            {\"ref\": \"BQT:2031\", \"status\": \"supports\", \"note\": \"BQT vol. 4 printed p. 2031 is the ملخ page: the entry proper ('نام حشرات بالداری که …؛ جراد') with Mo'in's etymological footnote (Avestan maδaxa-, Pahlavi maδax, Armenian maraχ, Horn p. 227, introduction pp. 17-18), and on the same page 'ملخ آبی نوعی از ماهی کوچک باشد که آنرا بعربی اربیان گویند' — the locust/shrimp link inside Borhān itself.\"},\n            {\"ref\": \"MON:4503\", \"status\": \"partial\", \"note\": \"The six-volume Farhang-e Fārsi is not online and not on disk (only the 2-vol. Adena condensation), so p. 4503 cannot be checked; the entry content is verifiable there: MON_part2.txt line 64689 'ملخ آبی: (جاد.) میگو', line 64710 'ملخ دریایی: (جان.) میگو. (جاد.) خرچنگ دریایی', line 70560 'میگو … ملخ دریایی؛ جرادالبحر، اربیان؛ ماهی ربیان، خرجل، ملخ بی‌بال، ملخ آبی'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien § 96, p. 207 f. (HUB.txt line 7180)\", \"stance\": \"partial\", \"note\": \"'Für altes δ erscheint ausnahmsweise l in malax \\\"Heuschrecke\\\" (neben regelmässigem maig § 92, b) = zd. maδaxa-' — supports the equation but marks the l as irregular, hence the loanword hypothesis.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 4 p. 2031 s.v. ملخ and ملخ آبی\", \"stance\": \"supports\", \"note\": \"Quoted above; also 'ملخ پیاده … ملخی است که هنوز پر برنیاورده است' — the wingless nymph, the sense Mo'in's Farhang equates with میگو.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang, s.v. ملخ / میگو (MON_part2.txt lines 64689, 70560)\", \"stance\": \"supports\", \"note\": \"'ملخ آبی: (جاد.) میگو' and, s.v. میگو, 'ملخ دریایی؛ جرادالبحر، اربیان؛ ماهی ربیان، خرجل، ملخ بی‌بال، ملخ آبی' — Mo'in gives no origin tag for میگو, so he documents the equation but not the etymology.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD\", \"stance\": \"silent\", \"note\": \"No malax, malak or maig; the Middle Persian mdk' /ma(y)ik/ that Wiktionary cites for میگو is not in the concise dictionary.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Mağa\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Avestan maγ- m. / maγā- f. 'hole in the ground, pit' (Bartholomae AiW 1111)\",\n      \"note\": \"Correct in every part. Bartholomae's article reads 'j. maγ- m., maγā- f. \\\"Loch im Erdboden, Grube\\\": srvabya maγəm ava.kanōiš \\\"für die Nägel sollst du eine Grube graben\\\" V. 17.7 … a) insbes. von den zu Zwecken ritueller Reinigung gegrabenen Löchern: mazdayasna aiθa zəmō θrī maγəm ava.kanayən \\\"die Mazdayasnier sollen in der Erde drei Löcher graben\\\" V. 16.12 … V. 9.6 ff.', and it closes with 'Ableit. — np. maγ \\\"Tiefe\\\", vgl. maγāk \\\"Grube\\\"' — that is, Bartholomae himself draws Nourai's arrow to the Persian words. The language label (Avestan), the gloss ('hole, recess') and the citation HRN:221 are all right; the only thing to keep separate is Gathic maga- 'Bund, Geheimbund' (AiW 1111 also), a different word, which is why Mo'in's footnote on the Persian side adds the caveat 'هر چند که معنی فرق می‌کند'. Nourai spells the Avestan with -a because he cites Horn's 'aw. maγa-'.\",\n      \"note_fa\": \"این جعبه از هر نظر درست است. بارتولومه می‌آورد: «maγ- (نرینه)، maγā- (مادینه) «سوراخ در زمین، گودال»: srvabya maγəm ava.kanōiš «برای ناخن‌ها گودالی بکن» وندیداد ۱۷.۷ … و به‌ویژه دربارهٔ گودال‌هایی که برای پاکیزگی آیینی می‌کنند: «مزداپرستان باید در زمین سه گودال بکنند» وندیداد ۱۶.۱۲ و ۹.۶ به بعد»، و در پایان می‌نویسد «مشتق — np. maγ «تیرگی/گودی»، قس maγāk «گودال»» — یعنی خودِ بارتولومه همان پیکانی را می‌کشد که نورایی کشیده است. برچسب زبانی (اوستایی)، معنی («سوراخ، گودی») و ارجاع HRN:221 همه درست‌اند؛ تنها باید maga- گاهانی به معنی «انجمن، پیمان» را از این واژه جدا نگه داشت — و همین است که معین در پانوشت خود می‌افزاید «هر چند که معنی فرق می‌کند». نورایی صورت اوستایی را با ‎-a‎ نوشته چون از هرن نقل کرده که «aw. maγa-» دارد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%85%D8%BA%D8%A7%DA%A9\",\n        \"https://en.wiktionary.org/wiki/%D9%85%D8%BA\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"HRN:221\", \"status\": \"supports\", \"note\": \"Horn's no. 985 (HRN.txt line 8569, on the p. 221/222 opening — the '— 221 —' footer is at line 8563 and no. 984 magu runs over the break): '985. meγ \\\"Tiefe, Fluss\\\", meγak \\\"Graben, Grube\\\" (Šāhn. I,174 Vers 817). aw. maγa- \\\"Loch\\\"; phlv. maγ.' Both the Avestan gloss and the two Persian words of the chart, on the page Nourai cites (possibly one line into p. 222 in this scan).\"},\n        {\"ref\": \"MPP:85\", \"status\": \"not_checked\", \"note\": \"Nourai's MPP is Henning's word-list 'A List of Middle-Persian and Parthian Words', BSOS IX (1937-39) 79-92, which is not on disk (the local MPP.txt is Henning's 'Mitteliranisch', a different work, and a grep of it for maγ/mγ'k finds nothing). Indirect support: Mo'in's footnote on BQT p. 2021 cites, for Parthian mγ'k, an English reference whose OCR preserves '… A [L]ist of Mi[ddle-Persian and Parthian Words] … 85', so p. 85 of that list is almost certainly where Nourai (following Mo'in) got the Middle Iranian form.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 1111 s.v. maγ- (BRT.txt lines 19526-19528)\", \"stance\": \"supports\", \"note\": \"'j. maγ- m., maγā- f. \\\"Loch im Erdboden, Grube\\\" … V. 17.7, V. 14.6, V. 16.12, V. 9.6 ff. … Ableit. — np. maγ \\\"Tiefe\\\", vgl. maγāk \\\"Grube\\\".' Note also, three columns earlier, 'j. maēγa- m. \\\"Grube, Kuhle\\\" V. 13.37' (line 19439), a different word, and 'g. maga- m. \\\"Bund, Geheimbund\\\"' (line 19523), the Gathic homonym.\"},\n        {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD\", \"stance\": \"silent\", \"note\": \"Grep for 'maγ', 'mg', 'magak' yields only mowbed 'Mazdean priest' (< maguš) — the pit word is not in MacKenzie, though Parthian mγ'k is known from the Manichaean fragments (see BQT below).\"},\n        {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"Hübschmann has no note on Horn's no. 985; his m-notes jump from 1005 (mēx) to 1007-1011.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"mağ «مَغ ۲» : hole, a place dug in ground (+ مَغاک ، مُغاک)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"مغ maγ 'hole, pit' and its extended form مغاک maγāk (also pronounced moγāk) continue Avestan maγ-/maγā- 'hole in the ground' directly through a Middle Persian maγ: Bartholomae ends his Avestan article with 'np. maγ \\\"Tiefe\\\", vgl. maγāk \\\"Grube\\\"', Horn no. 985 gives 'phlv. maγ', and the Parthian Manichaean texts have mγ'k 'hole, cave' (quoted in Mo'in's footnote), which is the same -āk formation. The suffix is the ordinary Middle/New Persian -āk (as in خاک/سوراخ-type nouns; Mo'in analyses 'از: مغ (بفتح اول) + آک (پسوند)'), and en.wiktionary s.v. مغاک has exactly 'From مغ (maġ, \\\"hole\\\") + ـاک (-âk), from Middle Persian mγ (maγ, \\\"hole, pit\\\")'. The word is old in Persian poetry — the Rudakī line the chart quotes ('ابله و فرزانه را فرجام خاک، جایگاه هر دو اندر یک مغاک') and Ferdowsī's meγak in Horn's citation — and must be kept apart from the homophone مغ moγ 'Magus, fire-priest' (< MP mow, OP maguš), which is Nourai's «مَغ ۱» and Borhān's separate entry.\",\n          \"derivation_fa\": \"«مَغ» به معنی «سوراخ، گودال» و صورت گسترش‌یافتهٔ آن «مَغاک/مُغاک» بی‌واسطه از اوستایی maγ-/maγā- «سوراخ در زمین» و از راه فارسی میانهٔ maγ می‌آید: بارتولومه مقالهٔ اوستایی خود را با «np. maγ «گودی»، قس maγāk «گودال»» به پایان می‌برد، هرن (شمارهٔ ۹۸۵) «phlv. maγ» می‌دهد، و در متون مانوی پارتی mγ'k «سوراخ، غار» آمده است (به نقل پانوشت معین) که همان ساخت با پسوند ‎-āk‎ است. پسوند همان ‎-اک‎ معمول فارسی میانه و نو است (معین تجزیه می‌کند: «از: مغ (بفتح اول) + آک (پسوند)») و ویکی‌واژه ذیل «مغاک» می‌نویسد: «از مغ «سوراخ» + ـاک، از فارسی میانهٔ maγ «سوراخ، گودال»». واژه در شعر فارسی کهن است — بیت رودکی که در نمودار آمده و «مغک» فردوسی که هرن نقل می‌کند — و باید آن را از هم‌آوایش «مُغ» (موبد آتش، از فارسی میانهٔ mow و پارسی باستان maguš) جدا داشت که همان «مَغ ۱» نورایی و مدخل جداگانهٔ برهان است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%BA%D8%A7%DA%A9\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%BA\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2021\", \"status\": \"supports\", \"note\": \"BQT vol. 4 pdf p. 104 = printed 2021: 'مغاک - بفتح اول بر وزن هلاک، بمعنی گودال است خواه در زمین و خواه غیر زمین باشد' with footnote 1 'از: مغ (بفتح اول) (ه.م.) + آک (پسوند). رك: اسشق ۹۸۵ [= Horn no. 985]. در اوراق مانوی (پارتی) mγ'k (سوراخ، غار) … در فارسی maγāk … رك: maγ از اوستا maγa- (هر چند که معنی فرق میکند)'. Nourai's node is this footnote.\"},\n            {\"ref\": \"MPP:85\", \"status\": \"not_checked\", \"note\": \"Same as at the root: Henning's BSOS IX word-list is not on disk. Mo'in's footnote on BQT p. 2021 cites it (OCR '… A [L]ist of Mi… 85') for the Parthian mγ'k, which is presumably Nourai's route to the page number.\"},\n            {\"ref\": \"FRS:145\", \"status\": \"partial\", \"note\": \"Loghat-e Fors does use مغاک as a gloss — FRS_pages.txt leaf 93 'غفج: مغاک' and leaf 419 in the م section — so the word is in Asadi's dictionary, but the copy on disk is the Eqbal 1319 edition, whose pagination differs from the Kharazmi 1365 edition Nourai cites, so p. 145 itself is not checkable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1111, end of the maγ- article (BRT.txt line 19528)\", \"stance\": \"supports\", \"note\": \"'Ableit. — np. maγ \\\"Tiefe\\\", vgl. maγāk \\\"Grube\\\".' — Bartholomae states the very derivation the node draws.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 985, pp. 221-222 (HRN.txt line 8569)\", \"stance\": \"supports\", \"note\": \"'985. meγ \\\"Tiefe, Fluss\\\", meγak \\\"Graben, Grube\\\" (Šāhn. I,174 Vers 817). aw. maγa- \\\"Loch\\\"; phlv. maγ.'\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in via the BQT p. 2021 footnote (the 6-vol. Farhang is not accessible)\", \"stance\": \"supports\", \"note\": \"Mo'in's own analysis 'از: مغ + آک (پسوند)' with the Parthian mγ'k comparison, quoted above.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD\", \"stance\": \"silent\", \"note\": \"No maγ 'hole' entry; only mowbed and mow (the Magus word), so the Middle Persian antecedent comes from the Manichaean Parthian material rather than from Book Pahlavi.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-317.json > /dev/null && echo \"JSON OK\"; python3 /home/sfmqrb/git/rishe/tools/verify_check.py 317",
 "description": "Write and validate verification file"
}
```


### [2026-09-07T02:00:09.382Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'plausible': 6, 'transcription_suspect': 2, 'confirmed': 7}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 19, 'partial': 3, 'not_checked': 5, 'not_found': 2}
books consulted: {'partial': 9, 'supports': 33, 'contradicts': 2, 'silent': 7} | by book: {'KLN': 7, 'PHD': 5, 'CHEUNG': 4, 'MON': 4, 'BRT': 3, 'HUB': 3, 'IEC': 3, 'HRN': 3, 'HJB': 3, 'BQT': 2, 'ISS_alt_DKS': 2, 'AHD': 2, 'SKT': 2, 'LAT': 2, 'AID': 1, 'POK': 1, 'SYN': 1, 'FSD': 1, 'WEB': 1, 'NYB': 1}
```


## [2026-09-07T02:00:32.198Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%87%DB%8C\" \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA\" \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%B3%D8%AA\" \"https://en.wiktionary.org/wiki/%D9%85%D9%84%D8%AE\" \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%DA%AF%D9%88\" \"https://en.wiktionary.org/wiki/%D9%85%D8%BA%D8%A7%DA%A9\" \"https://en.wiktionary.org/wiki/%D9%85%D8%BA\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/m%C3%A1tsyas\"; do python3 tools/fetch_source.py \"$u\" --note \"page 317 (Mad / Madhaxa / Maga): percent-encoded form of the page cited in data/verification/page-317.json\" >/dev/null; done; python3 - <<'EOF'\nimport json\nidx=[json.loads(l) for l in open('/home/sfmqrb/git/rishe/data/verification/sources/web/index.jsonl')]\nhave={e['url'] for e in idx}\nv=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-317.json'))\nurls=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,x in o.items():\n            if k=='sources': urls.update(x)\n            else: walk(x)\n    elif isinstance(o,list):\n        for x in o: walk(x)\nwalk(v)\nmissing=[u for u in sorted(urls) if u not in have]\nprint('sources in file:',len(urls),'| missing from archive:',missing)\nEOF",
 "description": "Archive encoded URLs and verify index coverage"
}
```


### [2026-09-07T02:00:36.382Z] TOOL RESULT

```
sources in file: 16 | missing from archive: []
```


## [2026-09-07T02:00:58.778Z] AGENT

Done. `verify_check.py 317` → 15/15 nodes, 0 PROBLEM lines.

**Page 317 (book p. 287) — roots Mad, Madhaxa/Mazaxa/Madika, Mağa (+1 redirect skipped)**
- Roots: 3 confirmed. Nodes: 7 confirmed, 6 plausible, 2 transcription_suspect.
- Ref checks: 19 supports, 3 partial, 2 not_found, 5 not_checked; 47 `consulted` entries (33 supports, 9 partial, 2 contradicts, 7 silent).

transcription_suspect (both **book** errors — the JSON is faithful to the printed page, checked against a 200 dpi render copied to `sources/refs/ocr/BOOK/317.png`):
- Mad #3 "mâstu, maccum" — Sanskrit is *mástu-* (short a) and Armenian is մածուն *macun* (so Pokorny 694 and Horn 959); "maccum" is no attested form, apparently Nourai misreading Horn's *macun*.
- Mad #5 "madati : a water bird, mina" — *madati* means 'it gladdens, bubbles'; AHD's chain (which Nourai is following) is *madati* → *madana-* → *madanaḥ* 'myna bird', so the box should read *madanaḥ*. The gloss was carried down from node #1.

Other findings worth the owner's eye (no data fix needed):
- Mad #1: the third item "mad : a water bird" is not Avestan at all — Pokorny's bird is Skt *madgu-* = NP *māγ*; Nourai moved it up a box to give *māğ* a parent. Also the fish member (*masya*/*mātsya*) is now treated as unknown/BMAC-substrate (de Vaan; Buck already put a "?"), hence "plausible".
- Mad #10 NOTE evaluated: FSD's Latin *mattus* < Persian *māt* is untenable (*matus* is in Petronius, 1st c. CE); *mattus* < *\*maditus* (Pokorny, Wiktionary, Buck, Ernout-Meillet). #12 NOTE: Klein p. 946 (page verified) really does route *mat/matte* through Arabic *māt*, AHD p. 805 through Latin *mattus*, and Etymonline leaves both open → "plausible".
- Mad #4 *ماست*: Cheung, Bailey, Horn, Mann, Mo'in all make it inherited Iranian (*mad* 'curdle'); en.wiktionary's unsourced Syriac-loan claim is the outlier; the chart's arrow is really cognacy, not descent.
- Madhaxa root: HUB:100 is exactly right (Bartholomae himself cites "Hbn. PSt. 100"), and BQT intro pp. 17-18 says what Nourai reports — but the Sogdian donor is superseded: NP *ملخ* is now taken as a Bactrian loan (μαλαχο), while *میگ/میگو* is the inherited SW form (< \*madika-), which is where the box's "Madika" comes from. "Old Persian" in the label is a reconstruction only (Kent silent).
- Mis-citations: HRN:222 (both locust nodes) `not_found` — Horn p. 222 has nos. 985-989, no locust; the locust is no. 1010 on p. 227. BQT:1961/2007 cover *ماهی* and *مست* but not *ماغ* (that is p. 1944). MON:4503 and FRS:137/145 unverifiable by page (edition/pagination not on disk); MPP:85 not on disk (local MPP.txt is Henning's *Mitteliranisch*, not the BSOS IX word-list).
