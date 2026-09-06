# Verification process log — verify-page-206


## [2026-09-06T14:51:41.967Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 206 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-206.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-206.json. Write /home/sfmqrb/git/rishe/data/verification/page-206.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 206` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:51:43.375Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:51:44.090Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:51:44.107Z] TOOL RESULT

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


## [2026-09-06T14:51:44.622Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-206.txt"
}
```


### [2026-09-06T14:51:44.646Z] TOOL RESULT

```
1	=== PDF page 206 (book page 176) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gweie, Gweye : to over power, defeat  (refs POK:469)
4	#1 (parent #0) [Avestan] refs=POK:469; SOD:470 | zinât : to injure ; zyâ 3, zyâni : injury
5	  #2 (parent #1) [Persian] refs=BQT:1050 | zîyân «زیان» : loss, damage
6	#3 (parent #0) [Avestan] refs=POK:470; HRN:197; FFD:70 | gâ 2 : to rape ; gâmô : sexual intercourse, rape
7	  #4 (parent #3) [Pahlavi] refs=HRN:197 | gâtan : to engage in sexual intercourse
8	    #5 (parent #4) [Persian] refs=HRN:197; FFD:70 | gâdan «گادن (گاییدن)» | extra: گاد ، گای
9	#6 (parent #0) [Avestan] refs=POK:469 | žayâi : to defeat. ; žya 4 : defeated, diluted
10	  #7 (parent #6) [None] refs=None | 
11	#8 (parent #0) [Old English] refs=AHD:1070 | âcwencan : to quench
12	  #9 (parent #8) [English] refs=AHD | quench
13	--- entry 1 ---
14	ROOT [Indo-European] Gwel 1 : to throw, reach  (refs POK:472)
15	#1 (parent #0) [Avestan] refs=POK:472; KLN:143 | ni-ğrâ-ire : they are thrown down ☞Nî 1 ; ni-gar
16	  #2 (parent #1) [None] refs=None | 
17	#3 (parent #0) [Greek] refs=AHD | ballein : to throw ; para-ballein : to throw (set) beside, to talk to a group ☞Per 1 ; sum-ballein : throw together, compare ☞Sem 1 ; dia-ballein : to throw across, slander ☞Dwo ; dia-bolos : slanderer, devil ☞Dwo
18	  #4 (parent #3) [French] refs=AHD | parler : to talk ; symbole : signs (used for comparison)
19	    #5 (parent #4) [Persian] refs=MON:1981 |  | extra: پارلمان ، سمبول
20	    #6 (parent #4) [English] refs=None | parliament
21	  #7 (parent #3) [Latin] refs=AHD | 
22	    #8 (parent #7) [English] refs=None | ballistic, parabola, hyperbola, metabolism, problem, symbol, devil
23	  #9 (parent #3) [Arabic] refs=FVQ:47; KLN:496 | eblis, iblis : devil
24	    #10 (parent #9) [Persian] refs=BQT:83 | eblîs «ابلیس» : devil
25	  #11 (parent #3) [Greek] refs=AHD | ballizein : to dance
26	    #12 (parent #11) [French] refs=None | bal, ballet : dance
27	      #13 (parent #12) [Persian] refs=MON:466 | bâlet «بالت» : ballet
28	      #14 (parent #12) [English] refs=None | ballet
29	    #15 (parent #11) [English] refs=None | ballroom, ballad
30	
```


## [2026-09-06T14:51:48.905Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-206.json",
 "description": "Read source JSON for page 206"
}
```


### [2026-09-06T14:51:48.958Z] TOOL RESULT

```
{
  "pdf_page": 206,
  "book_page": 176,
  "entries": [
    {
      "root": {
        "name": "Gweie, Gweye",
        "lang": "Indo-European",
        "refs": "POK:469",
        "gloss": "to over power, defeat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:469; SOD:470",
          "words": [
            {"translit": "zinât", "gloss": "to injure", "script": null},
            {"translit": "zyâ 3, zyâni", "gloss": "injury", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1050",
          "words": [
            {"translit": "zîyân", "gloss": "loss, damage", "script": "زیان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:470; HRN:197; FFD:70",
          "words": [
            {"translit": "gâ 2", "gloss": "to rape", "script": null},
            {"translit": "gâmô", "gloss": "sexual intercourse, rape", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "HRN:197",
          "words": [
            {"translit": "gâtan", "gloss": "to engage in sexual intercourse", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "HRN:197; FFD:70",
          "words": [
            {"translit": "gâdan", "gloss": null, "script": "گادن (گاییدن)"}
          ],
          "script_extra": "گاد ، گای",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:469",
          "words": [
            {"translit": "žayâi", "gloss": "to defeat.", "script": null},
            {"translit": "žya 4", "gloss": "defeated, diluted", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Old English",
          "refs": "AHD:1070",
          "words": [
            {"translit": "âcwencan", "gloss": "to quench", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "quench", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gwel 1",
        "lang": "Indo-European",
        "refs": "POK:472",
        "gloss": "to throw, reach"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:472; KLN:143",
          "words": [
            {"translit": "ni-ğrâ-ire", "gloss": "they are thrown down", "script": null, "see": ["Nî 1"]},
            {"translit": "ni-gar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "ballein", "gloss": "to throw", "script": null},
            {"translit": "para-ballein", "gloss": "to throw (set) beside, to talk to a group", "script": null, "see": ["Per 1"]},
            {"translit": "sum-ballein", "gloss": "throw together, compare", "script": null, "see": ["Sem 1"]},
            {"translit": "dia-ballein", "gloss": "to throw across, slander", "script": null, "see": ["Dwo"]},
            {"translit": "dia-bolos", "gloss": "slanderer, devil", "script": null, "see": ["Dwo"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "parler", "gloss": "to talk", "script": null},
            {"translit": "symbole", "gloss": "signs (used for comparison)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1981",
          "words": [],
          "script_extra": "پارلمان ، سمبول",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "parliament", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "ballistic, parabola, hyperbola, metabolism, problem, symbol, devil", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 3,
          "lang": "Arabic",
          "refs": "FVQ:47; KLN:496",
          "words": [
            {"translit": "eblis, iblis", "gloss": "devil", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "BQT:83",
          "words": [
            {"translit": "eblîs", "gloss": "devil", "script": "ابلیس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 3,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "ballizein", "gloss": "to dance", "script": null}
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
            {"translit": "bal, ballet", "gloss": "dance", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:466",
          "words": [
            {"translit": "bâlet", "gloss": "ballet", "script": "بالت"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "ballet", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "ballroom, ballad", "gloss": null, "script": null}
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


## [2026-09-06T14:51:49.051Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T14:51:49.106Z] TOOL RESULT

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
```


## [2026-09-06T14:52:00.508Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','BQT','HRN','FFD','AHD','KLN','FVQ','MON']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\""
}
```


## [2026-09-06T14:52:01.806Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"g\\*\\?ṷei\" POK_full.txt | head -30; echo ---; grep -n \"469\\|470\" POK_full.txt | head -5"
}
```


### [2026-09-06T14:52:02.403Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
```


### [2026-09-06T14:52:02.477Z] TOOL RESULT

```
---
9976:References: WP. II 112f., WH. 1111, 119, 124,470. 
10288:References: WP. 11127 f., W. Schuize KZ. 60, 138 = Kl. Schr. 469. 
18958:dirst' defecate ', difsa' buttocks ', MiJhlenbach-Endzelin I 470, and of a guttural extension 
19079:field ' (MiJhlenbach-Endzelin I 470, 505), russ. (see Berneker 186) derevnja^ village 
20028:References: WP. I 849 f., WH. I 466 f., 469, 471 f., 864, Trautmann 49, Pedersen
```


## [2026-09-06T14:52:06.631Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Pages\\?(s)\\?:\" POK_full.txt | head -5; echo \"=== search 469\"; grep -n \"469\" POK_full.txt | grep -i \"page\" | head -10"
}
```


### [2026-09-06T14:52:06.696Z] TOOL RESULT

```
1549:Page(s): 2 
1574:Page(s): 2 
1607:Page(s): 2-3 
1637:Page(s): 1 
1679:Page(s): 3 
=== search 469
38571:Page(s): 469 
38675:Page(s): 469-470 
39074:Page(s): 467-469 
39836:Page(s): 469
```


## [2026-09-06T14:52:06.863Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -60 POK_full.txt"
}
```


### [2026-09-06T14:52:06.904Z] TOOL RESULT

```
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN
```


## [2026-09-06T14:52:08.870Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '38500,38720p' POK_full.txt"
}
```


### [2026-09-06T14:52:08.919Z] TOOL RESULT

```
together, circuit, congress, assembly, union, session '; Old High German biquami^ 
bequem ' (compare ' digestible '), Old English ^ecu/e/ne "pleasant, fitting'. Old Norse 
kvsemr^ capable or allowed to come '; kvamat ' coming, visit, dropping by; inspection ', 
koma ds.; 

Tocharian A kum-, AB kam-, A kam-, B se/77-"come', A kumnas, Med. kumnastar^ 
comes ', A kakmu, B kekamu^ arrived; resulted '. 

With a meaning- development ' come (to the world) ' = ' be born ': 

Avestan n'hjamayeinti^ be born ' {*ni-Jama- 'birth'); 

gr. £-pa0r| syEvvEGri Hes.; 

alb. pre-gjim " feast in the first birth '; (common pronunciation alb. gj- = Slavic dz-) 

Lithuanian gemu, gimti^ be born ' = Latvian dzemu, dzimtds., Lithuanian g/mstu{ior 
pronunciation see Schuize KZ. 45, 230) = Latvian dzimstu 6s., Lithuanian gimine^ family ', 
^j7/77/5 "birth', gamas^ the innate ', causative gaminti^ generate children, breed cattle ', 
Latvian dzimts^ congenital, existing from birth, innate, inherited ', o'z//775a "birth' = Old 
Prussian gimsenin kVk. Sg. "birth'. Old Prussian gemton^ to give birth to children ', 
^e/77/77c»/7s participle Perf. " born '. 

References: WP. I 675 ff., Meillet Esquisse2 134 f., Schwyzer Gr. Gr. I 309, 689, 7423, 
7072, Trautmann 76, Pedersen Tocharian 170 ff., 221, 234. 
Page(s): 463-465 

Root / lemma: g'^eA^- 
Meaning: to push, hit, harm 

Material: Old Indie gandh-^bump, poke, prick, injure, destroy' (by grammarians), gandha-h 
m. "smell, odor, fragrance ', Avestan gantay- " fetidness ', Middle Persian gand^ fetidness 
', Old pers. gasta-^ disgusting, unsavory, distasteful', afgh. yandar disgust, repulsion, feel 
loathing ', Baluchi gandag^evW, bad', (to meaning development "bump, poke, prick' > 
"smell, odor' compare e.g. Old High German 5///7/ra/7 "smell, stink' against Gothic stigqan^ 
clash, bang together, collide, crash ' and gr. Kviari " steam and odour of fat which exhales 
from roasting meat, smell or savour of a burnt sacrifice ' compared with Old Icelandic hmta 
"bump, poke, prick'.) 



Gr. btvvoq " vituperation, sliame' {*g"'en6'"no-); after Kuiper Nasalpras. 65 liere cpGovoq 
m. " envy ' (present *(p9£vu) from *g"&'-en-); 

Note: 

comnnon lllyrian g"- > d- ; g"- > b-. 

about Middle Higli German quetsen, quetschen^hW., bump, pol<e, squeeze' s. Kluge s. v. 
quetscherr, 

Litlnuanian gendu, gestr be damaged, spoil, be destroyed, perish; wither, wilt, die ', 
gadinu, gad/nt/'spoW, damage, disturb, bother', pagadas 'ru'\r\\ Latvian ginstu, ginV be 
destroyed, perish; wither, wilt, die '. 

Maybe alb. godas^ hit' a Slavic loanword. 

References: WP. I 672 f., Benveniste BSL. 38, 143. 
Page(s): 466-467 

Root / lemma: g''eid(h)- 
Meaning: mud 

Material: Gr. SeToa " filth, slime, mud ' {*g"ei6\iao'c -sa, or *g"eid-s-a)\ perhaps Old Norse 
kveisai. "swelling, blister, lump, growth'. Middle Low German quese' blood blister, blood 
pustule', besides Norwegian kvisa, Swedish kvissla6s.\ 

Old Church Slavic zidtk-b " succous, succulent, sappy, sapful, juicy, rich, opulent ', russ. 
etc. zfdkij^ fluid, liquid, runny; soft, pliable'. 

References: W P. I 671. 
Page(s): 469 

Root / lemma: g^ei-l 
Meaning: to cry, weep 

Note: Beyond the Germanic only unsafe comparisons; probably onomatopoeic. 
Material: Gothic qa/ndn^\Neep, cry, grieve ', Old Norse kveina^ lament'. Old English 
cwanian^ wail, be sad ', Old Norse kveinka^ wail, lament' and with other derivative Old 
Icelandic stem Verb. kvTda' be frightened ', kvTda\. ' trembling, quaking, shaking, terror, 
anxiety, fear, dread, alarm ', kvTdixw. ds.; Old English cwTdan, schw. Verb. " wail, bemoan ', 
Old Saxon c/^/lJ/a/? 'lament'; 



here recalled formally Lithuanian g/edu and gfestu, g/edot/" s\ng, crow ', etc., to the only 
registered root in Satem languages *gef- 'sing' (see there); it is not listed because of 
meaning in question. 

References: WP. I 665 f. 
Page(s): 467 

Root / lemma: g''ei-2 

Meaning: to put together, enclose 

Material: Umbrian bio, Paelignian Akk. biam^ enclosed district, region, area '; Note: 

common lllyrian g"- > b-. 

Old Norse kve\. " pen, fold, narrow enclosed passage ', kvJa^ coop, place in a pen or 
coop, pen '. 

References: WP. I 666. 
Page(s): 467 

Root / lemma: g'^eja- 

Meaning: to prevail, be mighty 

Material: Old Indie y>a,y/y^f. " suzerainty, sovereignty, political control ' (= gr. pia) = alb. f. 

{*g"eia) zija^ mourning, grieving, lamentation; act of feeling sorrow for someone's death; 

period of mourning; clothes worn by mourners; signs of mourning '. 

Old \r\d\c Jyana-m, JyanF-h ^ oppression, depression, exploitation, suppression \Jyayan' 

mightier, more prepotent \ jyestha-, Jyestha- " most incredible, strongest '■,Jayat/ {Peri. 

jigaya) " overmatched, overpowered, defeated ' (Avestan \v\t Jayai, full grade I the root, 'to 

defeat, conquer'), yay/s/7^- ' victorious \jetar- " defeating '; jinati {Vut jyasyati. Pass, jTy ate, 

participle y/7a-) ' beaten, overpowered, oppressed'; y/^/sa//" will defeat, conquer ' ( : Avestan 

Jijisaiti^ tries to attain for himself, cause to be found '), jigy'u- " victorious '; 

Old Indie y»7a// stands also for " bring about sth ', jyani-h a\so " decrease, loss' and is so 
both the extender of the palatal aniaut. root from Avestan zinat^ damages ', Old pers. 
adinat^buuQ about, take away, take off, remove ', participle Perf. Pass. dTta-, Avestan 
zyana, zyani-i. " damage, harm ', Inf. zyana/^to harm', Baluchi zinay^ seize, take forcibly; 
grasp, snatch, take abruptly, seize hastily, take away by force ' (external Aryan 
correspondences not known); 

Maybe alb. Geg mezane^ to gripe, capture ', Geg me uzane, Tosc zihem^ quarrel '. 



gr. pia " force, might, power ' Note: common lllyrian g"- > b-. (= Old Indie y/ya), piaco, 
pia^u) " force, coerce ', piaiO(; ' violent, brutal ', AvTi5iO(; probably = AvTipiO(;; pTvsTv ' futuerl 
', ^a£i pivsT Hes. " rape ' (whereas pTvsTv would have derived from a participle *pT-v6-(; = Old 
lndicy/-/7a-, Gramm.,); after Liden IF. 19, 328 with npers. gayad^ futuit ', Inf. gadan, gan, 
from a root *g"'ai- or (?) *g"'di-, which would be compatible only with the latter beginning 
with g^ei-as lengthened grade of the ogradation at most theoretically; 

Maybe alb. {*zyana) dhune^ force, violence, forcing, viciousness, rape ' : Old pers. adinat 
'bring about, take away, take off, remove ', participle Perf. Pass. 07?^-. 

with g'^eja-^ suppress, crush; repress ' appear also the following words for " exhaust, 
weaken, make feeble ', Intr. Pass. " go altogether, grow old, dwindle ' originally belonged 
together: 

Old Indie y//7a// also ' grows old \ jyan'hh^ senility ', ajyani-h^ immortality ',jTna-'age6, 
old', a-j7ta-' unbroken, unmarred, unscathed, undamaged ', a-jTti-h^ intactness, 
completeness, entireness, wholeness ',y/V/7-'old, fragile, easily broken; unstable, 
dilapidated, helpless ', Avestan yya-, present J/'na/t/" exhausts, weakens ', ajyamna-' not 
decreasing, inexhaustible ', wherefore Middle High German verquTnen, preterit quein^ 
dwindle away, decrease ', Old English cwTnan, a-cwTnan, preterit cwan' dwindle away, 
decrease, abate, pain, feel ill ', extended Old English cwincan, acwincan^ disappear, 
abate ' (Kaus. with ablaut neologism acwencan, engl. quench^ extinguish, put out '), and 
with /77-forms wfal. kwTmen^ pain, feel ill ', kwTmelig' softened, made soft; overindulged '. 

From Germanic seem in both meaning of colouring addable: 

Old Norse kveita^ dazzle, blind with bright light ' (o'-present); s-extensions Middle Low 
German quisten^ let perish, waste ', (7^/s/ "damage, loss', mnl. quisten^ rub, rub away, 
wear away, bruise, grind, bray triturate, rub against, wear', Gothic q/stjan ^spoW, Old High 
German quisti. " annihilation ', archwistan, f/rqu/stan 'spoW, destroy'. Old English cmesan' 
crush, squeeze hard, squash ', jut. /riws 'press, extract, squeeze ', nisi, kveisa^ stomach 
ache '; Norwegian kveisa^ verkummertes Geschopf ', kvisla^ dwindle away, decrease '; g- 
extension (fragmented reduplication?) Frisian kwTke, kwikken^ pinch, tweak, nip ', in the 
reduced meaning in Prussian queicheln^ fondle '. 

References: WP. I 666 ff., Schwyzer Gr. Gr. I 300, 694. 
Page(s): 469-470 

Root / lemma: 5'"&/-5and g^eia-: g^fijie-: g^Olio-: gl"-, frequent, often with -:/- extended 



Meaning: to live 
Material: A. from *g''eid: 

Old Indie y7i/a/i/-/7 "life' (see below), gaya-h^ house, courtyard, Hauswesen ' (see below); 

AvestanJ/'yaesa' you should live ' (2. Sg. present Med., orthemat. 2. Sg. Opt. for 
y/gayaesa); Jljf/sdnt/ {ong\na\\Y subjunctive) " be refreshed, nourished \Jaya- m. " incitation 
'; gaydxr\. 'life, lifetime, lifestyle ' (= Old Indie gaya-h^ house and courtyard, Hausweser^ ' = 
russ. ^oy "peace; salvation!'); Avestan gaeda. Old pers. ^a/z?a "entity, house and courtyard 



Armenian keam^ live ' {*gl'ya-ye-mi); Meillet Esquisse 110, 176. 

gr. hom. psoijai " I will live ' {*^z\zao\\a\\ SchwyzerGr. Gr. I 780, 788''); Note: common 
I Nyhan g"'- > b-. 

Lithuanian gajus' slightly healing '; Lithuanian gyju, gyti{*gTti-) " revive, recover, 
become healthy ' (in addition i-gyti-^ attain ', actually " live there '), Latvian dz?t^ heal; 
become healthy ', gydau^heaX, Latvian dziedet^\\ea\, cure' (MiJhlenbach-Endzelin I 559), 
Old Church Slavic z///" live ' (present zivgsee below); in addition Old Church Slavic zitb 
"life' ( *gft/s), pa-zitb " pasturage, food, fodder, provender, esp. for cattle, grass, generally, 
any feeding-ground, any moist, grassy place, meadow '; 

Slavic *gojb " life' {*g"'q/o-s) in Old Russian ^oy"peace', old Serbo-Croatian goj ds., Old 
Czech /7oy "fullness, wealth' (: Old \nd\c gaya-h), causative Slavic *gq/7t/' make live ', 
Serbo-Croatian gdj/'t/^ care, fatten, overfeed ', etc.; 

Tocharian B sa/- " live ', Van Windekens Lexique 127. 

'^'^o-in: 

Avestan -Jyaiti- f. (in compounds) 'Wie' , Jyatus Gen., Jyatum Akk. "life' (in Old Indie if this 
became *Jya-tu-h aftery7i/5//to jTvatu-h)\ 

ep. Ionian ^cbw, gort Scbu) " live ' (from *^(ji)-i(ji), Indo Germanic *gzid-id), Aor. Epiwv 
( "(g^/io-zT? with vokal. /; which was presumably supported by piow), Attic ^w, ^pq, ^p (*^n,'£'. 
Indo Germanic *gZie-), ^w6q " living ', ^cbn "life', ^coov "animal'; gr. uyinc; "fit, healthy' {*su- 
g"lies " living well ');
```


## [2026-09-06T14:52:30.668Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=39700 && NR<=40100' POK_full.txt | grep -n \"Root / lemma\\|Page(s)\\|Meaning\" | head -40"
}
```


### [2026-09-06T14:52:32.419Z] TOOL RESULT

```
10:Page(s): 479-480 
12:Root / lemma: g^et-l 
14:Meaning: resin 
29:Page(s): 480 
31:Root / lemma: g''et-2 
33:Meaning: to speak 
55:Page(s): 480-481 
57:Root / lemma: g''§o^-1 (or g''§o^-l), g^do^- 
59:Meaning: to sink, submerge, plunge 
86:Page(s): 465-466 
88:Root / lemma: g''eb(h)-2 
90:Meaning: slimy; toad 
119:Page(s): 466 
121:Root / lemma: g^ei- (or g^eia^. gl"- 
123:Meaning: skin 
137:Page(s): 469 
139:Root / lemma: g''ena {* ghfenS) 
141:Meaning: woman, wife, *goddess 
199:Page(s): 473-474 
201:Root / lemma: g^heA^- 
203:Meaning: to beg, wish for 
233:Page(s): 488 
235:Root / lemma: g^heia- : g^hT- 
239:Meaning: vein, sinew 
266:Page(s): 489 
268:Root / lemma: g^hel- 
270:Meaning: to wish 
284:Page(s): 489 
288:Root / lemma: g'^hemb- 
289:Meaning: to spring, hop 
301:Page(s): 490 
303:Root / lemma: g''hen-1 
305:Meaning: to swell, abound 
334:Page(s): 491 
338:Root / lemma: g''hen-2(a)- 
340:Meaning: to hit
```


## [2026-09-06T14:52:32.735Z] TOOL CALL #11: Bash

```json
{
 "command": "pdftoppm -f 206 -l 206 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg206 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T14:52:36.394Z] TOOL RESULT

```
total 88
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 10:52 .
drwx------ 4 sfmqrb sfmqrb  4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 77858 Sep  6 10:52 pg206.png
```


## [2026-09-06T14:52:41.204Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 47[12]\" POK_full.txt | head; echo ===; grep -n \"^Root / lemma: g''el\\|^Root / lemma: g\\^el\" POK_full.txt | head"
}
```


### [2026-09-06T14:52:41.256Z] TOOL RESULT

```
Exit code 1
39249:Page(s): 471-472 
39288:Page(s): 472-473 
(eval):1: == not found
```


## [2026-09-06T14:52:43.268Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39200,39300p' POK_full.txt"
}
```


### [2026-09-06T14:52:43.352Z] TOOL RESULT

```
Danish /ri/a/'vapor, haze, mist'; Modern High German Qualle, Dutch kwal, kwalle^ 
medusae '. 

In connecting meaning (perhaps from " cave in, crumple, collapse inward ') Old Indie 
gla-ti, glayati^ feels tired, is irritated, dwindles ', participle glana-, glana-m, glan'hh^ 
exhaustion, feebleness, decline, reduction ', Kaus. glapayati^ exhaust, press; allow to 
decay '? 

IS) Avestan niyraire " they are flung down ' {ni-gar-)\ 

gr. paAAu) 'throw, cast, hit, strike ' ( *g"'eln-o), zero grade Arcadian egSeAAovte^ = 
£KpaAAovT£(;, ^sAAsiv paAAsiv Hes., Aor. paAsTv, Perf. p£-pAr|-Ka, Aor. £pAr|v ' received a 
shot, was offended, hurt ', £pAr|TO, pAr|T6(;; pAr||ja " throw, cast, of dice, of a missile, shot, 
wound, coverlet ', poArj, p6Ao(; m. ds., poAi(;, Aboq, ' missile ', ^zKoc,, psAs-pivov 'projectile', 
'QEKaTr|-p£A£-Tr|q; 

Note: common lllyrian g"- > b-. 

From New Testament Greek Trapa-paAAu) " to throw beside or by ' > TrapapoAn " juxta- 
position, comparison, a comparison, illustration, analogy, a parable, i. e. a fictitious 
narrative by which some religious or moral lesson is conveyed, a by-word, proverb ' > Latin 
yoa/'ait'o/a 'parable ' > Italian parlare : Spanish hablar: French parler: Bergamasco 

baia : Ladin bale : Bresciano paria : Calabrese paria : Catalan parlar: Catanese parari: 
Furlan sfevela: Galician falar: Portuguese falar: Albanian geg mefole' to speak', 
Albanian tosk flas ' speak', Aorist fola ' spoke'. 

Also Spanish hablar: French parler: Galician falar: Portuguese falar: Albanian tosk flas^ 
speak', Aorist fola ' talk '. 

from Celtic perhaps cymr. bllf^ catapult ' ( *g"'le-mo-, compare gr. pAr|-|ja); about Old 
Irish at-balir dies ' s. g^el- 'prick'; 

Tocharian AB kla- 'fall'. Van Windekens Lexique 40. 



With a meaning development ' sich im Geiste auf etwas werfen, paAAsoGai £v Gupco, 
psTQ cppsoi' places one to paAAoo also (?) the gr. family of pouAo|jai ' will, wish, be willing ' 
(*poAao|jai, Konj. of s-Aor. to paAAw); pouArj, Doric pwAa: f. ' resolution, decision, advice, 
counsel '; but Thessalian p£AA6p£V0(;, Doric 5r|A- from *g"'elso-\ here also paAs ' prevail 
god, O that! Would God!'. 

References: WP. I 690 ff., Schwyzer Gr. Gr. I 284, 693 under Anm. 9. 



Page(s): 471-472 



Root / lemma: g''el-3, gV- g'^la- 

Meaning: acorn; oak? 

Note: only in derivatives with the meaning ' acorn ' receive (after Specht Indo Germanic 

Dekl. 60 f. previous noun g^el-s, secondary g'^-s. Gen. g''J-6s) 

Material: Armenian kaHn, Gen. kal-noT acorn ' {*g"'el(9)-eno-, /from dem Gen.); kai^ni 

"oak"; 

gr. paAavoc; m. " acorn ' {g^el-ono-); Note: common lllyrian g'^- > b-. 

Proto Baltic *gTls{*g'^-s), Gen. *gJIes, what from *gTI'na\x\ Latvian (d)zTle, Lithuanian gyfe, 
and *gWna\x\ Lithuanian g'lle^ acorn ', Old Prussian gile' acorn, oak'; 

extension -n-d-'w^: 

Latin glans, glandist " acorn '; 

Maybe alb. Geg lande, tosk {*glandis) lende : Galician landra " acorn ' [Italian ghianda, 
French gland, Albanian geg lande, Catalan gla, Galician landra, Romagnolo, genda, 
Roman ghianna, Romanian ghinda, Umbro-Sabino ghianna, Venetian gianda, Zeneize 
glanda, Bolognese gianda, Bresciano gianda.] 

Lithuanian gilendra, gilendre^ rich harvest in fruits (originally acorn '); 

russ. -Church Slavic ze/i/^yi. (Slavic *zelgd'b) m. " acorn ', Serbo-Croatian zeludm., russ. 
zoludbm. ds. 

References: WP. I 692, WH. I 604 f., Trautmann 82, Specht KZ. 66, 56, Indog. Dekl. 60 f., 

173,230. 

Page(s): 472-473 

Root / lemma: g^em- 
See also: see above g^'a-. 
Page(s): 473 

Root / lemma: g''er(a)-4 

Meaning: to raise the voice; praise 

Material: Old \x\(ii\c grnati, grnJte^ sings, praises, praises, announces ' (Fut. garisyati, Abs. 

abhigurya), sam-girate^ promises, pledges ', gurate^ greets', gTri., Gen. girah^ laudation.
```


## [2026-09-06T14:52:47.618Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39140,39200p' POK_full.txt"
}
```


### [2026-09-06T14:52:47.665Z] TOOL RESULT

```
/r/7"wedge' and Middle High German /r/e/"ship'. 

2. With the meaning "pain - sorrow - death': 

Armenian keiem^ afflict ' (Meillet Msl. 8, 165); 

Old Irish at-bailF dies ' {ess-^ bain- from *^7-/7-with prefixed object pronoun "if; 
nevertheless barely after Pedersen KG. II 459 as namely "it throws life away ' to £K-paAAco, 
because of the meaning "die' returns also out of Celtic; compare also corn, bar^i deadly, 
esp. an infectious or contagious disease, a plague, pest, pestilence', cymr. aballu{*ad- 
ballu), ba//u'6\e' {*g'?-n-), ad- fe/7/o {*ate-ba/- irom *g"el-) ds.; Note: common lllyrian g"- > b- 



perhaps Latin vallessiV penenT ' (placed as Celtic verb, a present *(g"'a/-/7o ahead; 
different EM2 1129); 

Old High German Old Saxon quelan, guar endure sorrow ', Old English cwelan^AW; 
Old Norse kvelia^ afflict ', Old Saxon quellian. Old High German quellenAs., Old English 
cwellan^s\aY\ Old Norse kvgli. " torment, pain, agony'. Old English c/Va/i/ "killing, violent 
murder'; Old Saxon quala^ agony, torture ', Old High German qua/ads., "violent death'. 
Modern High German 0^5/ (lengthened grade as Lithuanian ge/a, Old Church Slavic za/b); 
Old High German, Old Saxon qua/m' death, devastation ', Old English cwea/m6s., 
Swedish kva/m' abrupt indisposition, minor illness, nausea '; Old English cuvie/c/ "death' 
{g^el-th), cwieldtTd^ eventide (*end of day'). Old High German quiltiwerk^ evening work ', 
Old Norse kveldu. {*g"'el-t6-) "evening'. 

About " aniaut variations ' (probably at best rhyme meaning) s. Siebs KZ. 37, 315, Lewy 
KZ. 40, 420. 

References: WP. I 689 f., Trautmann 83, Vendryes RC 40, 433 ff. 
Page(s): 470-471 

Root / lemma: g''el-2, g^ela- g^le- 

Meaning: to drip, flow; to throw, *boil over 

Note: though after Wackernagel KZ. 67, 159 belong a) and tS) variant verbs. 

Material: a) Old Indie galati^ trickles down, falls down, disappears ', galita-h^ vanishes, 

retreats, withdraws ', Kaus. galayati^ pours away, makes flow, strains off '; Old Indie 

galana-^ dribbling, running ' (Lex.), n. " the trickling, gully, trench, ditch, small ravine, 

runnel ' = ga-rana-m (Gramm.); 

gr. paAavEuq " bath attendant ', paAavsTov "spa, bath' (> Latin balneum); pAuu), pAu^u) " 
gush forth ' (formation after cpAuu)), pAu5iov "humid, wet' Hes., and from the family of 
paAAu) in similar meaning appoAaSnv " bubbling up (of water)', AsAAoi " bubbling fountain 
in Eryke', compare also z\c, aha paAAsiv " flow '; Note: common lllyrian g"'- > b-. 

In e- grade: 

Hittite: kweluwana- {kuluwana-) c. ' washbasin, bowl ' (Tischler 604) 

Old High German quellan {quail) "spring up, bubble, to swell' (//probably from In), Old 
English (gejcollen ' s\i\/o\\en' , Old High German quella. Modern High German Quelle, 
Middle Low German qualm (*t\r\e gushing forth ' =) "fume, smoke, vapor, smoke'. Old
```


## [2026-09-06T14:53:01.944Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg206.png"
}
```


### [2026-09-06T14:53:02.297Z] TOOL RESULT

```

```


## [2026-09-06T14:53:02.293Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T14:53:13.418Z] TOOL CALL #16: Bash

```json
{
 "command": "sed -n 1,160p tools/verify_check.py"
}
```


### [2026-09-06T14:53:13.457Z] TOOL RESULT

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


## [2026-09-06T14:53:26.851Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD gweie/gwela\"; grep -n -i \"^g[wʷ]e[il]\" AHD_watkins1985.txt | head -30; echo \"=== AHD quench\"; grep -n -i \"quench\" AHD_watkins1985.txt | head -10; echo \"=== AHD ballistic\"; grep -n -i \"ballistic\\|parabola\\|ballizein\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T14:53:26.928Z] TOOL RESULT

```
=== AHD gweie/gwela
=== AHD quench
1010:steig-. To stick; pointed. Partly blended with stegh-. I. Zero-grade form *stig-. 1. Germanic suffixed form *stik-ilaz in Old English sticel, a prick, sting: STICKLE- BACK. 2. Suffixed form *stig-i- in Germanic *stikiz in Old English stice, a sting, prick: STITCH. 3. Germanic expres- sive form *stikk6n- in Old English sticca, stick: sTICK. 4. Germanic blended variant *stekan in Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET; SNICKERSNEE. 5. Nasalized form “sti-n-g- in Latin stinguere, to quench, perhaps originally to prick, and its apparent derivative distinguere, to separate (semantic transitions obscure): DISTINGUISH, EXTIN- GUISH, INSTINCT. 6. Suffixed form *stig-yo- in Greek stizein, to prick, tattoo: STIGMA; ASTIGMATISM. 7. Suf- fixed reduced form “*tig-ro- in Old Persian tigra-, sharp, pointed, and Avestan fighri-, arrow, in Greek tigris, tiger (from its stripes): TIGER. II. Basic form *séeig- in Latin -stigdre, to spur on, prod, in instigdre, to urge: INSTI- GATE. III. Suffixed o-grade form *stoig-d- in Germanic *staikd in Old Norse steik, roast, steak, and steikja, to roast (on a spit): STEAK. [Pok. steig- 1016.]
=== AHD ballistic
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABOLISM, DEVIL, (DIABOLIC), (EBLIS), ECBOLIC, EMBLEM, EPIBOLY, (HYPERBOLA), HYPERBOLE, METABOLISM, (PALAVER), PARABLE, (PARABOLA), (PARLEY), (PARLIAMENT), (PAR- LOR), (PAROL), (PAROLE), PROBLEM, SYMBOL; b. Greek ballizein, to dance: BALL?, (BALLAD), (BALLET), BAYA- DERE. 2. Suffixed o-grade form *gvols-d in Greek bolé, beam, ray: BOLOMETER. 3. Suffixed o-grade form *gwolo-sdé in Greek boulé, determination, will (< “throw- ing forward of the mind”), council: BOULE!; ABULIA. 4. Suffixed variant zero-grade form *gvele-mno- in Greek belemnos, dart, javelin: BELEMNITE. [Pok. 2. g¥el- 471.] gwela-2, An acorn. 1. Suffixed zero-grade form *g¥/o-nd- in Latin gldns (stem gland-), an acorn: GLAND, GLAN- DERS, (GLANDULAR), GLANS. 2. Suffixed zero-grade form *gulg-no- in Greek balanos, acorn, date: VALONIA; MYRO- BALAN. [Pok. 3. gvel- 472.] gven-. Woman. 1. Suffixed form *gven-d- in: a. Germanic *kwen6n- in Old English cwene, woman, prostitute, wife: QUEAN; b. Old Irish ben (> Irish Gaelic bean), woman: BANSHEE; C. Persian zan, woman: ZENANA. 2. Suffixed lengthened-grade form *gvén-i- in Germanic *kwéniz, woman, wife, queen, in Old English cwén, woman, wife, queen: QUEEN. 3. Suffixed zero-grade form *g“n-d- in Greek guné, woman: GYNO-, -GYNOUS, -GYNY; GYNAE- CEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gvend 473.) g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far north, variously explained as “they who live beyond the north wind” and “they who live beyond the mountains” (hu- per-, beyond; see uper): HYPERBOREAN. [Pok. 3. gver- 477.) gvere-2. Heavy. I. Zero-grade form *gra-. 1. Suffixed form “g“ra-u-i- in Latin gravis, heavy, weighty: GRAVE?, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE. 2. Suffixed form “gro-u- in: a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA; b. Sanskrit guru-, heavy, venerable: GURU. 3. Suffixed form *gro-es- in Greek baros, weight: BAR?, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR. 4. Possibly *guri- in Greek bri- in compound *u(d)-bri- (see ud-). II. Suffixed extended form *g-rii-to- in Latin britus, heavy, unwieldy, dull, stupid, brutish: BRUT, BRUTE. III. Suffixed extended form *g»ri-g- in: a. Celtic *brig-o-, strength, in Italian brio, vigor: BRIO; b. Germanic *krig- in Old High German krég, chrég, stubbornness (> Ger- man Krieg, war): BLITZKRIEG, SITZKRIEG. IV. Suffixed full-grade form *gvero-nd-, millstone, in Old English cweorn, quern: QUERN. [Pok. 2. g¥er- 476.] gvere-*. To praise (aloud). 1. Suffixed zero-grade form *gvra-to- in Latin grdtus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, IN- GRATE, INGRATIATE. 2. Suffixed zero-grade form *gwro-do-, “he who praises,” in Celtic bardo-, bard, in Welsh bardd and Scottish and Irish Gaelic bard, bard: BARD}. [Pok. 4. gver(a)- 478.] gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
2059:-PARA pere-1 PARABLE gWelg-1 PARABOLA gW¥ele-1 PARACHUTE pere-1 PARACLETE kele-2 PARADE pere-1 PARADIGM deik- PARADISE dheigh-, pert PARADOX dek-! PARAFFIN pau- PARAGRAPH gerbh- PARALLAX al-1 PARALLEL al-1 PARALLELEPIPED ped-! PARALOGISM leg-1 PARALYSIS leu PARAMECIUM mak- PARAMOUNT ad-, per! PARAMOUR amma, pert PARANOIA nous PARAPET peg- PARAPHERNALIA bher-1 PARAPHRASE gWhren- PARAPLEGIA plak-2 PARASOL pere-1, sawel- PARATAXIS tag- PARBOIL beu-! PARCAE pera-1 PARCEL pere-2 PARCENER pere-2 PARDON d6-
```


## [2026-09-06T14:53:27.278Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf for p.197 (leaf=printed+21 => 218)\"; awk 'BEGIN{RS=\"\\f\"} NR==219' HRN.txt | head -60"
}
```


### [2026-09-06T14:53:29.012Z] TOOL RESULT

```
=== HRN leaf for p.197 (leaf=printed+21 => 218)
— 197
G.
882^ gU" Praefix.
ap. vi-, vii/"; aw. ai. vi- 'auseinander; phlv. t?(00>
paz. «?a-.
kurd. 60-, ftw-, be~.
88 ^i. ffoden 'coitiren*, Praes. gäy-em, gaylden, gäye^ gün
'Coitus.
aw. gßmö\bereiti~ 'Coitus* (nach Geiger, Ostiran.
Kultur, 341 Note 2); phlv. gätan (y. 48, ö, vergl. Hörn,
ZDMG. 43, 36 Note 32; vd. 15 (29) GL).
kurd. gäyin 'sich paaren'; af/. yö, yömd; oss. d.
qäyun, t. qäin 'coitiren (165); bei. gäy (102).
Bartholomae stellt hierzu nach briefl. Mitteilung
auch gr. ya^iscj.
^^4. -gär '-tuend, -verfertigend* z. B. sitemgdr^ perhBzgar,
ai. "kära-; phlv. -kär,
Vergl. np. -kär (No. 832).
^S5. gäz *Zange, Scheere' (Sahn. I, 54, 391), falsch kdz,
aw. vergl. atare.^vaza'tia- Teuerzange' (Geld n er,
Studien I, 50).
Zweifelhaft^). Jedenfalls gehören zu np. gäz *Beiss-
zange; Biss* (AM. 30 Zeile 4 v. u.) noch gezlden 'beissen
(ein interessanter Infinitiv gelten findet sich AM. S. 13
Zeile 8, vergl. Kä§. Q. gasten, sowie märgeste schlangen-
gebissen , AM. 217 Zeile 3 v. u.), gezdum 'Scorpion
(wörtl. 'Beissschwanz*) ; vielleicht auch gezne 'Brenn-
essel', kaum aber ar. kuzüda 'kleine Scorpionsart' (de
Goeje, Bibl. geogr. arabic. IV, 340).
^) Meine Bemerkung KZ. 32, 581 war verfehlt, vergl. Hübsch-
mann, ZDMG. 46, 328 Anm. 1.
«) Hübsohmann'fl begründeter Einspruch (KZ. 26, 604 folg.)
gegen Geldner' s Regel über das Suffix -ana- im Neupersischen
(Studien I, 50) war mir leider bisher entgangen, sonst hätte ich nicht
öfter oben dagegen Verstössen (s. Nachträge).
```


## [2026-09-06T14:53:40.345Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"cwencan\\|QUENCH\" AHD_watkins1985.txt | head; echo \"=== gwei roots in AHD\"; grep -o \"g[wv”“]*ei[eəa][-–][0-9]*\\. [A-Za-z ,.]*\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T14:53:40.433Z] TOOL RESULT

```
1010:steig-. To stick; pointed. Partly blended with stegh-. I. Zero-grade form *stig-. 1. Germanic suffixed form *stik-ilaz in Old English sticel, a prick, sting: STICKLE- BACK. 2. Suffixed form *stig-i- in Germanic *stikiz in Old English stice, a sting, prick: STITCH. 3. Germanic expres- sive form *stikk6n- in Old English sticca, stick: sTICK. 4. Germanic blended variant *stekan in Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET; SNICKERSNEE. 5. Nasalized form “sti-n-g- in Latin stinguere, to quench, perhaps originally to prick, and its apparent derivative distinguere, to separate (semantic transitions obscure): DISTINGUISH, EXTIN- GUISH, INSTINCT. 6. Suffixed form *stig-yo- in Greek stizein, to prick, tattoo: STIGMA; ASTIGMATISM. 7. Suf- fixed reduced form “*tig-ro- in Old Persian tigra-, sharp, pointed, and Avestan fighri-, arrow, in Greek tigris, tiger (from its stripes): TIGER. II. Basic form *séeig- in Latin -stigdre, to spur on, prod, in instigdre, to urge: INSTI- GATE. III. Suffixed o-grade form *stoig-d- in Germanic *staikd in Old Norse steik, roast, steak, and steikja, to roast (on a spit): STEAK. [Pok. steig- 1016.]
=== gwei roots in AHD
gveia-. To live. I. Suffixed zero
g”eia-. To press down, conquer. Sanskrit jayati, he con
```


## [2026-09-06T14:53:41.940Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN quench\"; grep -n -i \"quench\" KLN_1966.txt | head -5; echo \"=== KLN Iblis\"; grep -n -i \"iblis\\|Eblis\" KLN_1966.txt | head -8; echo \"=== KLN ballistic/ballad/ballet\"; grep -n -i \"ballizein\" KLN_1966.txt | head -8"
}
```


### [2026-09-06T14:53:42.026Z] TOOL RESULT

```
=== KLN quench
2395:(whence  Siapav,  ‘to  cut  through,  clear  away’), and  cogn.  with  OSlav.  jama,  ‘a  pit’, amaranth,  n.,  1)  a  mythical  plant  that  never  fades; 2)  any  plant  of  the  genus  Amaranthus;  3)  purple color.  —  Gk.  apapavTO?,  ‘unfading ;  amaranth’, fr.  A-  (see  priv.  pref.  a-),  and  the  stem  of  pocpod- veiv,  ‘to  put  out,  quench,  extinguish,  to  make to  waste  away’,  fr.  I.-E.  base  *m'er-,  ‘to  rub, consume,  wear  away’;  see  smart,  v.,  and  cp. marasmus.  The  ending  of  amaranth  (for  amarant) is  due  to  the  influence  of  plant  names  formed with  Gk.  avffo;,  ‘flower’.
3580:asbestos,  n.  —  L.  asbestos,  fr.  Gk.  Sapearoc,  lit. ‘unquenchable,  inextinguishable’,  fr.  A-  (see priv.  pref.  a-)  and  opeaT^c,  verbal  adj.  of oPewivai,  ‘to  quench,  extinguish’,  which  derives fr.  I.-E.  base  *gwes-,  ‘to  quench,  extinguish’, whence  also  Lith.  gestu,  gisti,  ‘to  go  out,  be extinguished'.  OSlav.  gaSp,  gasiti,  of  s.m.,  Hitt. kishtari,  ‘is  being  put  out’,  Toch.  A  kas-,  B  kes-, kas-,  ‘to  go  out,  be  extinguished’, asbolite,  n.,  a  mineral  containing  oxide  of  cobalt.
5160:blench,  intr.  v.,  to  shrink.  —  MF.  blenchen,  fr. OE.  blencan,  ‘to  deceive’,  prob.  causative  of blink,  and  orig.  meaning  ‘to  make  to  blink’. ( Blench  stands  to  blink  as  drench  to  drink.)  Cp. also  OE.  cwencan,  causative  of  OE.  cwincan,  ‘to disappear’  (see  quench),  so  that  quench  prop, means  ‘to  cause  to  disappear’, blend,  tr.  and  intr.  v.,  to  mix.  —  ME.  blenden,  fr.
14197:extinguish,  tr.  v.  —  L.  exstinguere,  extinguere, ‘to  put  out  (fire),  quench,  extinguish’,  fr.  ist  ex- and  I.-E.  *steig-,  ‘to  prick,  stick,  pierce’,  whence also  L.  Instinguere,  ‘to  incite,  impel’,  instigare, ‘to  goad’.  See  stick,  v.,  and  cp.  words  there referred  to.  For  the  use  of  the  suff.  -ish  in  ex¬ tinguish  see  distinguish.
22875:L.  macula,  ‘spot’.  See  macula, mar,  tr.  v.,  to  injure.  —  ME.  merren,  marren,  fr. OE.  merran,  mierran,  ‘to  hinder,  obstruct, squander,  waste’,  rel.  to  OFris.  meria,  OHG. marren,  merren,  ‘to  hinder,  obstruct ,  Goth. marzjan,  ‘to  hinder,  offend  ,  OFris.  mere,  tie, fetter’,  and  prob.  to  ON.  merja,  ‘to  crush, bruise’,  and  cogn.  with  OI.  mrnati,  ‘he  crushes, bruises’,  Gk.  p-apatvstv,  ‘to  put  out,  quench, extinguish’,  fr.  I.-E.  base  *mer-,  'to  rub,  con¬ sume,  wear  away’.  See  smart,  v.,  and  cp.  words there  referred  to.  OF.  marrir,  ‘to  afflict  (whence F.  marri,  orig.  pp.,  ‘sorry,  grieved’),  OProveng. marrir.  It.  s marrir e,  'to  lead  astray  ,  are  Teut. loan  words.
=== KLN Iblis
4331:ballista,  n.,  an  ancient  military  engine  ( Roman antiq.)  —  L.,  fit.  ‘a  throwing  machine’,  fr.  Gk. piXXeiv,  ‘to  throw’.  See  next  word ballistic,  adj.,  pertaining  to  projectiles.  — Formed with  suff.  -istic  fr.  Gk.  fiaXXetv,  ‘to  throw’, which  stands  in  gradational  relationship  to (JoXfj,  floXoc,  ‘a  throw’,  fisXo?,  ‘bolt,  arrow, dart’,  lit.  ‘something  thrown’,  fr.  I.-E.  base *gwel-,  whence  also  OI.  apa-gurya-,  ‘swinging’, Avestic  ni-yra-'re,  ‘they  are  being  hurled  down’, Toch.  AB  kla-,  ‘to  fall’,  and  perhaps  also  OI. galati,  ‘trickles’,  OHG.  quellan,  MHG.,  G.  quel- len,  ‘to  well  up’.  Cp.  ball,  ‘party  for  dancing’, ballista,  amphibole,  amphibology,  anabolism, bdemnite,  Belostoma,  bolide,  bolometer,  boule, ‘council’,  catabolism,  devil,  diabolic,  discobolus, Eblis,  ecbolic,  Elaphebolion,  emblem,  embolism, emboly,  hyperbola,  hyperbole,  metabolism,  pa¬ rable,  parabola,  parlance,  parley,  parliament, parlor,  parol,  parole,  periblem,  problem,  scy- balum,  symbol,  Tribolium,  Tribulus. ballistics,  n.,  the  study  of  projectiles.  —  See  prec. word  and  -ics.
11155:devil,  n.  —  ME.  devel,  fr.  OE.  deofol,  deoful,  fr. Eccles.  L.  diabolus,  fr.  Eccles.  Gk.  SixpoXo;, ‘devil’,  fr.  Gk.  SixfioXo;,  ‘slanderer’,  fr.  Stoc- [JxXXeiv,  ‘to  throw  across;  to  attack;  to  calum¬ niate,  slander’,  fr.  Six  (see  dia-)  and  (SxXXeiv, ‘to  throw’.  See  ballistic  and  cp.  diablerie,  dia¬ bolic,  Eblis.  Cp.  also  It.  diavolo.  Proven?.,  F., Catal.  diable,  Sp.  diablo.  Port,  diabo,  Goth. diabaulus,  which  all  derive  fr.  Eccles.  L.  dia¬ bolus.  OHG.  tiufal  (whence  MHG.  tiuvel,  G. Teufel,  prob.  also  MDu.  duvet,  Du.  duivel,  OS. diuVal,  ON.  djofull,  Dan.  djievel,  Swed.  djdvul) is  a  Goth,  loan  word.
12577:Eblis,  n.,  the  prince  of  the  fallen  angels  ( Arabian religion).  —  Arab.  Iblts,  aphetic  for  Gk.  810c- (3oXo<;,  ‘slanderer’,  in  Eccles.  Gk.  ‘devil’.  It  is very  probable  that  Gk.  StafloXo?  came  into Arabic  through  the  medium  of  Syriac  and  that the  first  syllable  of  the  Greek  word  was  mis¬ taken  for  the  Syriac  genitive  particle  di  and  sub¬ sequently  dropped.  See  devil, ebon,  n.,  ebony  (poetic).  —  ME.  eban,  fr.  L.  ebe¬ nus.  See  ebony.
=== KLN ballistic/ballad/ballet
```


## [2026-09-06T14:53:51.162Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"g”eia-. To press down, conquer.\\{0,900\\}\" AHD_watkins1985.txt"
}
```


## [2026-09-06T14:53:52.429Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=12500 && NR<=12600' KLN_1966.txt | grep -n \"^[0-9]\\{2,4\\}$\\|page\" | head; echo \"=== page markers sample\"; grep -n \"^[0-9]\\{3\\}$\" KLN_1966.txt | awk -F: '$1>12000 && $1<12800' | head -20"
}
```


### [2026-09-06T14:53:53.494Z] TOOL RESULT

```
g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliiti
```


### [2026-09-06T14:53:55.939Z] TOOL RESULT

```
74:497
=== page markers sample
12009:473
12033:474
12034:475
12104:476
12121:477
12210:480
12226:481
12248:483
12299:484
12300:485
12347:486
12372:487
12409:488
12422:489
12452:490
12453:491
12573:497
12650:501
12681:502
12682:503
```


## [2026-09-06T14:54:19.935Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT zinā/zyā\"; grep -n \"zinā\\|zyā-\\|zyāni\\|zyānay\" BRT.txt | head -20; echo \"=== BRT jay/ǰay\"; grep -n \"ǰay\\|jayāi\\|ǰi-\\|jyā-\" BRT.txt | head -20"
}
```


### [2026-09-06T14:54:20.006Z] TOOL RESULT

```
=== BRT zinā/zyā
=== BRT jay/ǰay
```


## [2026-09-06T14:54:21.736Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT gā/gam gāmō\"; grep -n \"gāmō\\|gā-\\b\\|gav-\" BRT.txt | head -20; echo \"=== BRT nigar/ni-γrāire\"; grep -n \"γrāire\\|nigraire\\|ni-γra\\|gar-\" BRT.txt | head -20"
}
```


### [2026-09-06T14:54:21.817Z] TOOL RESULT

```
=== BRT gā/gam gāmō
5127:•  j.  avar«'gav-  m.  EN.  eines  Gläubigen: "gSuH  fnzavaiö  *öiymatastura/ie  asaonö "des  Ä.,  Sohns  des  ^.,  Sohns  des  Ö."  Yt
5746:j.  asfnga-,  p.  a^a'ga-  m.  'Stein">. KompA.;  Abtrat.  —  Vgl.  np.  mult-äsaiii;,  mp., np.  lanf.  —  VgL  auch  asman-.  —  1)  Im  Iran, muss  äi',  as'  und  1'  vorhanden  gewesen  sein, E.  dRn.  np.  niiist-äiang,  j.  asingS',  mp.  sangi vgl.  zum  Ablaut  gr.  üap,  iap  und  Ut.  sniii;iiis; Bthl.  IF.  a.  z68;  Hbm.  PSt.  76.  Das  p.  Wort kann  auch  ä%'  gelesen  werden. j.  as«ngö.gav-  Adj.  'mit  Händen  aus
8620:Aus  'uz-ziilay-,  %  J04  IL  36.  —  sbal.  vgl.  sul 'schnell';  s.  'gav-  No.  1.  —  Pü.:  buland uziitiömand.
9770:Ablcit.  aub  *'mjr>nrya;  vermuilich  Name  eines  |         j.  gao',  KompA.  (vor  Kons.):  s.  sgav-. ßana;  lEt.  s.  SiB,  3.  '       -  n  xt  ■  t-
9855:Ableit.  aus  igav-,  —  ai.  gäz-ya-,  gavyä-  Adj.  — PS.  (lu  V.):  fnSlaii  gäv  pim.  —  D  iSchr. ävaya  (vor  A)  statt  a^ya  s.  S  26e.    13  c.
10085:jgav-
10098:meist  mit  mantan-  'menschlich'  verbun- den": 'am  F.  21;  —  'yeÄe  marii!tüS  .  . yS  paoiryS  ahuräi  mazääi  manasca  *gulta silsnifsca  yahmat  haca  fr^W3r?sai  näfö airyanqm  dahyunqm  Yt/_J.  87;  V.  2  j.  2, 2Ö.  5;  —  haca  "yJt  mari^nat  ä  saosyantäi Y.  26.  10;  —  'yehylcä  mnra>nö  \.  13. 7.  a)  neben  ^gav-  (III):  tams  gsui  .. 'yehe  Y.öVi'.aa;  Vr.2;.2;  — fravaiayS.. yqmca  gSui yqm^a  'yehe  Yt  13.86.  Vu- deutlich:  _j'ar«/o  "yehe  maraia"  F.  ^e", ')  Vgl.  Yt  IJ.  87:  "OJH.,  der  als  erster  des AhuraM.  Willen  und  Gebole  annahm,  aus  dem er  schnf  die  Familie  der  ariBchcn  Länder,  den Stamm  der  arischen  Länder".  GM.  ist  der  ersle. Saesyant  der  letzte  Mensch,  Y.  26.  10.  Vgl. noch  Bd.  24.  1,  j,  igff.,  31.  1,  10.  7;  s.  Justi NB.   108.
10105:•  j.  'gav-  V.   'verschaffen'.     Praes.  10
10109:j.  'gav-  V.  'eilen'.     Praes.  i  Java-. mit  Inf.:  mosu  ml  Java  diiawÄ«  "eil  mir rasch  zu  Hilfe"  Yt  5. 63.
10111:•  j.  ^gav-  Adj.  'rufend,  schreiend':  yeäie (näml.  mihrahe)  växs"  .  ,  yatat  fumaaha vä(im  baraiti  yat  gaosHt  (NS.)  ". .  sei  es dass  er  betend  seine  Stimme  erhebt  oder (laut)  rufend"  Yt/o.  85''.
10114:sgav-  I
10116:•  j.  *gav-  m.  'Hand',  uzw.  dariA&chtr Wesen " :  am  aus  'va  (AD.)  paiii  apa.- gmrvayal  Yt.jp. 50;  11. z,  F.2i''>;  —  Aqm •va^^  nidar^zayatAü^m  Yl.j.27(?);  —  ma abara^alibya  fraluyh  mS  'vaeifya*''  aiwi.- tütuya  ¥.5,29;  —  d^ra  ..  mihröMru/am aptts  'vSiAP.)  darfzayeiti  Yt.  10. 48,  [n. 18:  lies  gavästryavar>i\
10119:•  h  g-  G  P-)  *gav-''  m.,  f."  I)  'Rind^'; Stier,  Kuh'*'i  °Susca  nqina  mazdaöähm Yt.  tV.  2;  —  %räyi!  *häi%Im.a^azianS  .. zavainli  'äusta  aspasca  haomasca  *äui zaoiänm  tavaiü  V.  //.  i ;  —  pqsnu!  °avö (NP.)  ,  .  aspa  Aog,  84;  —  yaha  drva 'aom  *viste  .  .  asptm  Aog.  82;  —  'Sus  vä aspahe  va   vansake  ü.  58;  Vd.  j,  8, 16;
10138:—  tistryS ..vaz»mnö  -Jus  k)hrpa  zaranyS.-  bagä  x^ar^mnif  (sd.)  Y. 32. 8;  —  "Su/x'ar»- srvahe  YLÄ16;  i4-l,  Y.ig.yi.  A)  Das  \%ahe  nr^yJ  V.7.  43; — 'Sul  vä  s^var3%ahe Rind  gilt  als  Repräsentant  aller  nützlichen  j  (sd.)  vä  W.14.1T,  —  '!us  i^ar/itinqm {ahumohtn)  Tiere,  daher  ^gav-  auch  inJH, /.  5;  —  yasca  ..  lanumazs {^A.)  'Jui weiterem  Sinn  gebraucht  wird*"':  para\da%at  "W-iS.!!);  —  °amla  ifsst)m  anäp»m •Su^  ca^war).paitistanaya  dänheit  para\{%d.)  V.5,  52;  S3f.',  7.55;  —  buiri 'aas  ,  . nars  asaotiB  bipaittstänahe  zq%st  Y.  /p.  8 ;  j  3far>^a  . .  VyL  4:5.  3)  'Milch',  bes.  zur
10151:KompA.,  E.  ().  auch  'gva-,  'fa-);  Ableit.  — aip  s^^  '^'v  ''■  i  ^P'  ^^  i  ^^  ^P-  f^spand  S' Xo.  8.  —  Pü. :  gäv,  götpand,  göspandän,  - Sü. :  gOMk,  gopaiavak,  ^vah  paiavah  ~  \  (zu  II *i3)=  g^  -  Sü.:  /aJava A  -,  aber  vor  hiidäh- wie  %\^\%  gesfand;  %.  noch  No.  6,  11, 14  und  zu Jhya-,  baoirya;  —  •)  iFlex.  %  411,  —  ')  Im Allgemeinen,  s.  zB.  Y.  /p,  8,  4S.  5,  //.  9, Yt,  /J.  10  (unter  I),  Y.  3.  3  (unter  II  3);  da- gegen Y.  8.  16  (unter  IJ,  V,  5.  51  [unlet  II  2) usw.  —  ))  Unter  den  ttiu>ra-  (sd.)  an  dritter Stelle  gewertet.  —  *)  Hds.  gSvanqm.  —  5>  'Ein Paar  trächtiger  Kühe',  die  als  Zugtiere  zu- sammengehören; s.  dazu  Bbr.  VglS.  i.  136. —  ^)  Pü,:  it  fa  gispandSmandih  (Sü.;  gepaiu- mallS)  mätüiiä.  —  7)  hudäh-,  haiäh-  Adj.  (sd.) erscheint  im  jAw.  häuüg  neben  igav-  in  ^len seinen  Bedeutungen.  —  B)  Sandhiia^ia  für •(■p(VS.)+^',  hui';  zuSjOrfll.  15.  Das  mp., np.  gisfand  \%i  LW.  aus  der  relimösen  Litt. S.  noch  No.  7.  —  9)  NA.  gaos  kaii;  s.  aber Jp  1,  Mf  3  und  P.  34.  —  "*)  Die  Bed.  1  und 1 A  sind  nicht  immer  scharf  auseinanderzu- halten; s.  auch  a.  —  ")  Pu, :  geil,  aber  erl. : jiu  (in  Aw.-BuchsC).  —  ")  Das  Yt.  ;-.  o  in mask.,  S.  3,  13  in  fem.  Form  auftritt;  s.  noch  1 No.  13.  —  'j)  Statt  des  bitten  Urrinds  (s.  auch No.  13)  erscheint  V.  39.  5  ein  Urrindeipaai;  s.  I auch  Y.  2$.  7  {>>ävä).  —  >*)  Pü.  (für  f  urV) : göhiran,  Sü. :  ger  ätmä,  gopaiünäm  älmä.  — >i)  Auf  den  Inhalt  von  Y.  29  spielt  Y.  46.  9 an.  —  ")  Ebd.  auch  zu  ^uS  im  Kalender,
10167:Ableit.  aus  igav-;  Tgl.  zSuff.  got.  meepi,  ags. icfuide  'Schafheerde'.
10175:•  j.  gav-a'äayana-  Adj.  'die  Wohnstätte [  der  Rinder  bildend,  von  Rindern  bewohnt':
10176:avi  imitt  karh-arf  yat  x^anira%3m  ..  'tum ' .  .  mi^r^  .  .  ädmäiti  Yt.  lo.  15, '  •  j.  gav-a'äitay-  f.  'Wohnstätte  der  Rin- der': avi  imai  karrvar>  yat  x''anira>:>m.. gavasayaramisA.)  'lliiica  bassatyqm  mi^rö . .  ädi'jiiiti  Yt  10. 15.
10178:KompA.  —  Ableit.  aus  *gmiislra-  n.,  Komp. igav-'c'^aslra-,%268.ll.  —  '^'X.:  s.  i\yvai}inah:
10188:•  j.  gav-äza-  m.  'Gerät  zum  Antreiben des  Viehs',  Du.  'die  beiden  Geräte  z.  A, d.  V.',  d.  i,  'Stachel  und  Peitsche':  yalsqm
=== BRT nigar/ni-γrāire
2882:ßr.  i^x?/""'  ai-  öia/e;  BtHL.  AF.  /.  II,  Gdn. VSt.j.  59.  — Zum  Laulliclien  s.  S  S3  I>  U- — Pü.:  gii/lan;  s.  rocb  No.  4t.  —  O  Unsicher (Vyt.  ir);  vll.  Opt.  —  ')  %  304  l.  i.  —  i)  S. mit  a^-i  fl.  —  4)  PÖ.:  öi,  Sü,:  ialam.  DST. ZA.  r.  328  meint:  "siaolä  aojäi  'j'ai  force comme  cbnntre'".  —  5)  Pü.:  apat  rasllan.  — 6)  Hds.  uxla. ').  aogar-  n.  'Kraft,  Stärke':  drujtf  'gar?
2891:KompA.  —  Vgl.  a^gar-  und  'aryah-.  —  Pü.: ayäwärVi.  —  ■)  Vgl.  iSt.  Cld.  KZ.  ,jo.  546 und  YL   13.   11  (s.  lagar-  No.   I).
3776:aibi-gar-  88
3788:•  j.  aibi-gar-  f.  'Preis,  Lobgesang':  aya °gara  aya  aibijar?ta  yS  amfianam  ..  "mit diesem  Preis,  mit  dieser  Preisung  der  A. .."
3796:Zum  V.  'gar-.  —  Pü. :  ap:  girisnJA. j.  aiaii^äld  V.  8.  4;  li«s  'galB.
3816:Zum  V.  'gar-,  —  ai.  jaritär-  m. ;  s,  dazu  Bthi. IF.  7.  51,  70.  —  Pü.  (zu  Y.  14):  apar  giriinih, (inVr.J:  apat  rasiinlA,  (zmY.  35).    apar  grijtär. Vgl.  vi  ailnjanlay-. j.  arwilim  H.  a.  171  s.  ^ay-  mit  aäiii.
4423:•  j.  an-äpa-  Adj.  ('wo  kein  Wasser  ist' sva.)  'trocken'  von  Speisen,  'ungemischt' vom  Wein:  gqmla  a^astsm  °apim  yaomca ahm  °äppm  maoula  "Spim  "trockenes  gar- gekochtes Reisch  .  .  und  ungemischten Wein"  V,  5.  52,  A)  als  ncutr.  Subst "Wüste,  17  änuhpoi':  yal  vä  '3p>m  ai  api kpfinaoiii  \yat  vS  3p3m  ai  °äppm  iir)- naoift]^^  "wo  man  zur  Wüste  hin  Wasser schafft"  V.J. 4.
5327:'Arabien':  imH  dahyavc^  tyä  adam  agar- bäyam , ,  'y^  0,6.3;  5-'i  Bh.r.6.
5705:•  p.  asagartiya-  '^Adj.  'sagartisch,  Sagar-
5878:•  j.  aspö.gar-  Adj.  'Rosse  verschlingend': azTm  . .  yim  °gar»n  mn^anm  \.q.\i.
9689:'Kusif^'':    imä  dakyavJ'  tyä  adam    agar-  /.  14- — '' Dbr-  VglS, /.  336.  —  »  Wo  davor
10194:•jC  g)  'gar- V. 'wachen'.  Praes.  22  +  14J
10200:'gar-  A  a
10203:•  j.  'gar-  V.  'preisen',  nur  mit  Praev. Praes.  11  g^nn-,  a6  gairya-  (Pass.)  — Int  °gairyä.
10209:•  j.  3gar-  V.  'schlucken'.  Praes.  ^jara-'^. *}arSil  *haom3m  .  .  bisanmta    *iristi-
10212:•  j.  ^gar-  V.,  nur  mit  «r  'niederschleu- dem'.     Praes.  zi  grä-.
10216:•  gl  j-  ^gar-  f.  'Lob,  Preis;  Loblied'; stBlö  'rü  {AP.)  vahmSng  ahursi  mazdai.. dadfmakÜa  .  .  \.4i.  i.  A)  GS.  garif mit  g.  dimäna-,  j.  nmäua-  n.  'Haus  des Lobs' "  als  Bezeichnung  für  den  Aufenthalt Masdah^  und  der  Seligen,  sva.  Paradies*'; a)  im  gAw,:  at  hsi  vahmStig  d?mSn!  °rö »idümii  "lasst  uns  ihm  Preislieder  im  Haus des  Lobs  niederlegen"  Y.  ^5. 8;  —  a  ^i^l
10218:S'3  *gar-  Ab
10221:Zum  V.  'gar-i').  —  ai.  ^-  f.'),  —  PQ.  (lu  Y.  V)i girihi,  (zu  A):  ^iv/m4iB(Transskr,). —  ■)  Nicht völlig  sicher.  Vgl.  SAderbloh  La  vie  future 98.  —  >)  NA.  schreibt  ohne  erkennbaren Gmnd  bald  gatS  um',  bald  garS.nm'  (s.  *).
10222:•  j.*gar-  i)  Adj. 'schluckend,  verschlingend' (nur  Komp.).  2)  f.,  Plur.  ■>  'Kehle,  Hals'  '> : aictl  ai3in  (näml. o^/)  tanUn  aguze  aiairi maisahe  -rö  Yt.  J7.  56.
```


## [2026-09-06T14:54:32.002Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10205,10216p' BRT.txt; echo \"=== grep zyani variants\"; grep -n \"zyäni\\|zySni\\|zyani\\|zinä-\\|zinä\\b\" BRT.txt | head -20"
}
```


### [2026-09-06T14:54:32.074Z] TOOL RESULT

```
lobend  einstimmen  in  — '  (Akk.):  s.  Inf.
mit  avi  'preisen'(?):  avi  ratüs  aii rahwya  ginnle  (3SPM.)  Vr.  4-  t(?)  ''■
mit  ä  'preisen':  iaAe'^  ng  ila  ni>ma ayairyüp''  kaAe''>  V5  urva  frayezyst  "von wem  wird  nun  unser  Name  gepriesen, von  wem  von  euch  unsere  Seele  verehrt werden?"  Yty.  50,
ai.  gi^^lii  abhigirya  (Absol.)*).  —  VgL  fjnr-, aibijarilay-,  ägrimalay:  —  PQ.  (lu  V.  /O):  ö öi  apar  girem,  (lU  Vr.  4):  elön  pa  an  raOk  u fISn  fa  an  ralih  radimh ;  vgl.  zu  aibijat/lay- mit  No.  2.  —  1)  Anscheinend  verderbt.  — '}  Der  Gen.  des  Agens  beim  Passiv  ist  auf- fällig; doch  vgl.  DbK.  AiS,  396,  —  3)  Pass. mit  akt.  Endung,  S  J2J,  —  4»  Das  ooss.  zarin 'singen'  iveist  weist  auf  7  als  idg.  Anlaut  hin; %55-
•  j.  3gar-  V.  'schlucken'.  Praes.  ^jara-'^. *}arSil  *haom3m  .  .  bisanmta    *iristi-
rftncai^A.)  P.25.
ai.  niroli,  gilali  'voial',  PDw.  nei-jaram  'voro'. -  Vgl-  V-"^  Adj.  —  Pü. :  j^artan.  —  ')  So nach  dem  Ai.  —  •)  Hds.  jaraöii  haan^m,  aber Pü,;  i"«!-  hörn.
•  j.  ^gar-  V.,  nur  mit  «r  'niederschleu- dem'.     Praes.  zi  grä-.
'nieder,  herabschleudern  auf-'  (Lok.):
karitaät  . .  vmraät  aSsqm  . .  ysi  niymire (3PPM,)  iarahu  mafyskanqm  Vt.  (O.  40.
Vgl.  gr.päM.«,  «^ijro;  %  14;.  's.  noch  NeISSEK ÜB,  13.   »91.
•  gl  j-  ^gar-  f.  'Lob,  Preis;  Loblied'; stBlö  'rü  {AP.)  vahmSng  ahursi  mazdai.. dadfmakÜa  .  .  \.4i.  i.  A)  GS.  garif mit  g.  dimäna-,  j.  nmäua-  n.  'Haus  des Lobs' "  als  Bezeichnung  für  den  Aufenthalt Masdah^  und  der  Seligen,  sva.  Paradies*'; a)  im  gAw,:  at  hsi  vahmStig  d?mSn!  °rö »idümii  "lasst  uns  ihm  Preislieder  im  Haus des  Lobs  niederlegen"  Y.  ^5. 8;  —  a  ^i^l
=== grep zyani variants
6039:^ä'sina'  m.,  Sva.  sainak',  vgl.  taenahvanl'^  — 1)  Tahmüraf  führt  später  den  Beinamen  zinä- vand  (so  bei  richtiger  Punktitung,  d.  i.  mp. tenäiiand,  womit  lainanhan-  übersetzt  wird), dervolkseL  an  Eni'WalTe' angeschlossen  wurde: an  ki  siläk  i  lamäm  dörad.  Vgl  Windisch- MANN  ZStI  197.  Sf.  Komm.  2. 635,  EA.  /.  518, JusTi  NB.  320.
7548:j,  ahmäi  äsySnim  Y. /3.  l;  lies  a' ä  zyänim (sd.).
```


## [2026-09-06T14:54:32.100Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'schädigen'\\|Schädigung\" BRT.txt | tail -30"
}
```


### [2026-09-06T14:54:32.147Z] TOOL RESULT

```
4105:—  ')  D.  i.  die  Nachteile,  Schädigungen,  die
9473:'  sOnahe  ratsS  baohs.varitahe  (sd.)  cikaya '  "die  Schädigung  des  Hunds  soll  er  ab- I  büssen  mit  der  Strafe  .."  V. /j,  10;  F.ac;
9486:pä/ixm-h  asi.  «f^j.  ^gg  geschädigten  Schädigung  büsse
9488:Nach  Jus'H  ZDMG.  57. 246  Tärberdistelborn' ;   vaktahe  a^aya  "die  Schädigungen  der  ge- *h,ti'a-  ("P- ^''*"''.  *'!/'"  Bl""  des  Cariha-  schädigten  bestrafe  man  mit  der  Strafe  .  ."
16059:Eig.  Bed.?  Ob  pä-änah-  (lum  V.  »fä-)  eig. 'frei  Ton  Schädigung'?
16371:irifyeiti  pt>r?byS*'>  astryäti  ptaribyS^'^ iri^fiti  ptpribys  irisintam  ralä  cikam baodS.varstahe  Whaya  ".  .  so  fällt  auf  die (envachsenen)  Familienangehörigen  die Sünde,  die  sie  tut,  und  der  Schaden,  den sie  zufilgt;  an  den  erwachsenen  Familien- angehörigen soll  man  die  Schädigungen der  Geschädigten  strafen  mit  . ,"  V.  75. la.  Wertlos:  yesi  narS..pairi  in%yHti
19993:mit /dm 'schädigen':  navanaptya^sA.)Si hl  urvSnsm  para.m3rMlaite  (3SPM.)    V,
24803:"  J,  'raesa-  m.,  raesah-  n.  'Schädigung'; A)  körperliche  Schädigung  überhaupt; a)  in  Bezug  auf  den  Fötus;  yeHi^a  . .  kaine . .  3^atö  garnuim  irisyeiti  .  .  ptinbyS  (sd.) irisintqtn  ralli  Hkain  baoiiS.varltahe  ci- %aya  V.  75. 1 3.  b)  in  Bezug  auf  Hunde: yS  süne  piilrtm  jainti  ..  us  va  hl  gaohm 'hwirisaiti  apa  va  ks  pathyqm  kintUaiti . .  cikayat  sBnahe  °l5  (ASn.)  baob5.varHahe üfhaya  V.ij.io;  'Vyt.44;  —  ym..spiina ahaiiyS.at»/iar3^r>m  (sd.J  irisyqn  para  as- iqm  iriHntqm  'h  cikaen  baoZs.var^iahe Hhaya   V,  75.  22,  40.  2)  Rechtsaus-
24804:druck fiir  jede  einem  Menschen  indirekt diu'ch  Fahrlässigkeit  zugefügte  körperliche Schädigung,  fahrlässigeKörperverletzung*': yai  .  .  vlmaaascit  vtmahayänie  .  .  yai "k^ritu  (sd.)  iriSyat  para  hi  trismtB  'stm cikayat  bao'üö.varstaht  a^aya  V.  7.  38;  — yezi  .  .  apirmäyüks  doaityS.ajiharihnm (sd.)  iriiyäi  para  hl  iriüntS  °s)m  Hkayal bao*>S.varstahe  ii'haya  Y.15.16;  —  nabä- nazdistim  h!  .  .  para  .  .  *'/aäi ''  *aowa- oaityacd  *ästäraiti  (sd.)  N.  g.  B)  peku-
25265:j.  TOitiadäi  P,  3:  lies  aw*. j.  (,  g.)  raä-   V.   'schädigen'.     Praes. 30  (Iter.)  raiaya-^l.   —  Inf.  rasaytrihi.
25269:•  g.  raäah-  n.  'Schädigung,  Schaden',  ins- bes.  der  im  andern  Leben":  ^itica  smits (Sp.  367  m.)  Ayalca  dar?gSm  *drs^-6jbbyi 'Is  savaUa  aiavabyS  "..  der  lange  Schaden für  die  Z>n/^enossen  und  der  Nutzen  für die  v^/aanhänger"  Y.  ^o.  11.
28278:•  j.  zyä.;  p.diyä- V.  'schädigen'.  Praes.  1 1 \sina-,älf^ä•■.äln''^,3^  (Pass.) ya-";  Perti \*üy.  —  PPfP.  äOa-'^i  Int  syänai.         S.
28291:!  •  j.  zyänay-  t  'Schädigung':  aSif  akmai \ä  *'nlm'^  nsit  vtesptm  xsta  mätdayatmti
28297:aoi  vUS  "ich  werde  von  nun  an  mich  nicht mehr  der  Schädigung  noch  Verwüstung  an den  masd.  Gemeinden  schuldig  machen" V.  72. 3;  —  US  (näml.  j/(y^  matdayasna- rtqm  vJsqm  °nayaicä''>  vlväpai^ä  "(ich schwöre)  ab  der  Schädigung  und  Ver- wüstung . ."  Y.  72.  3.
28299:•  j.  zyänä-  f.  'Schädigung,  Schaden':  mä duibirgt^  (sd.)  'nam  . .  yasBü  aom  nanm YL  /.  24.
```


## [2026-09-06T14:54:47.583Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'siegen'\\|jinäiti\\|jinaiti\\|'schwächen'\\|jyä-\\|jyä\\b\" BRT.txt | head -20"
}
```


### [2026-09-06T14:54:47.664Z] TOOL RESULT

```
6467:•  j.  "aätay-  m.  'Pfeil':  yat .  .  jyä  navi- >jqn  (sd.)  tiyrar?hs  "tayS  Yt  10.  113.
11582:Zum  \.  jyä-  (aus  der  volleren  Form;  s.  dazu HlBT  Ablaut  97).  —  Pü-!  *afashtisn')  kämak pa  yin.  —  i)  S.  zu  saed-  No,  2.  So  ist  lU lesen,  gegen  Haug  Essays'  366;  vgl  Pu.  zu
11691:jinäiti  'debilitat'  F-J5;  —  'jyamna-. xä\t  frä  dnwS.:  'frajyamna- .
13843:•  g.  duz-Jyätay-  f.  'das  schlechte,  pein- volle Leben'  (in  der  Hölle):  y<l  im  hujyä- töii  (sd.)  päyat  nHt  'töis  Y.46.8.
16526:ai.  bh4iajyä-   Adj.    —    Pü. :    beiaiiitüSr,    So. :
21575:Fö.i/j  luvän,  Sü.!  iaityä.  —  ')  Deotungs- vertuche  bei  Gdn.  KZ.  3/.  586,  Bn.  Stud.  /. 363,  JuSTI  PrJ,  S8.  85  [der  offenbar  yöli  yä liest).  Die  Hds.  haben  überwiegend  yä  tjyä. Eine  Verbalform  (so  Gd.v.)  halte  ich  für  aus- geschlossen.
22095:'pedicare  aliquem,  Päderastie  treiben mit  — '  (Akk.)":  yat  anusS  *vijyä/e^'^ vifyätica  "si  (quis)  invitus  pedicatur  et peÄcat"  V.  Ä  26;  27;  —  arsaca  vipts arlaca  valpayS  "ein  Mann  der  der Päderastie  dient  und  ein  Mann  der  ihr fröhnt"  V,  iS'.  32;  —  yas^a  dim  janat  .  . yim  vipt»m  m  V.  7.  55  PüZ,
```


## [2026-09-06T14:54:50.867Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11670,11700p' BRT.txt"
}
```


### [2026-09-06T14:54:50.908Z] TOOL RESULT

```
•  j.  3ivya-,  Jvaya-'',  Juya-''  Adj.  (fem. °y3-)  'lebend,  lebendig':  yai  ..JasäijvayS amiraxtii'  (sd.)  Yt.  z^-  1 1 ;  —  ayar-7  ami'k- näiti  (sd.) /a/ff  (NSf)''  /an«/ Aog.  53; — avaval  sätöis(sd.)  urva  *isaiii  ydäta  vlspim imat  yal  juyS  afthui  ".  -  soviel  (an)  Freude als  all  das  (ist),  was  die  Menschheit  im Leben  (an Freude  erfährt)"H.2. 2.  a)  als Beiwort  von  ^gav-Tl-^  'queck  sva,  beweglich, ^zix^ :  gqm  jlvyqm  'die  flüssige-'*  Nahrung, die  das  Rind  liefert,  d.  i.  die  Milch  des Rindes'  Y.^.  3,  22.  i.
Ableit.  aus  jtva-,  —  ai.  fevya-  n-  'Mittel  tum Leben'.  —  Pü.  (lu  Aog.);  üvanJai,  (lu  H.): pa  ihiandakih;  (lua):  gSsl  iiivand,  inSü.erl.: dugdham.  —  ")  Statt ynya-j  S  ^S.  II,  I7.  — »)  D.  \.jriya;  -c  statt  -ya  ($  268.  32),  -uy Statt  -ru-  (S  268.  19).  —  ))  Im  Gegen»,  in baekya-.
•  j.  Jira-  Adj.  lebhaft,  rasch'  an  Verstand, 'intelligent,  schlau':  anzSJamamm  ..  finrn sbanmnim  ßyäurum  Yt  II).  42.
KompA-,  E.  —  Zum  V.  'gay-,  —  VgL  garva- nay:  —  ai.  Jirä-  Adj.  'rasch,  lebhaft',  afy. £i>  'lebhaft',   np.  lö-aJk  'schlau,  scharfsinnig'.
•  j.  Jirö.sära-  Adj.  'mit  intelligentem, klugem  Kopf:  uiträ  .  .  'rö  Yt.  14. 12.
Npü. :  nriar,  ert. :  sar  .  .  iisyär  täÜi  ast,
•  j.  Jistayana-"  patr.  Adj.  Von  Jlltay stammend,  dessen  Nachkomme :  asähurahe (sd.)  "nahe  asaonS  \t.  ij.  113.
Ableit.  aus  */u/ay-  m.  EN.  (s.  No.  l);  Et. und  Bed.  ?  —  >)  F 1  hat /Styan' i  dann  läge *jiilya-  zu  Grunde.
•  j.  jiStayamiia-  Adj.  'sich  fälschlich  aus- gebend für  — '  (Nom.):  yS  .  .  mazdayasta aojanS  asahe  rahma  (sd.)  'nS  Y.  8.  3.
PPM.,  lU  ''jma\ya-  Praes.  3l(?).  —  Et.?')  — Pü. :  ie  . .  pa  an  i  airäili  bahr  iä/ät,  — I)  Falsch  Gdn.  3Yt.  128;  a.  zu  zaisa-,
•  j.  Jum  AbsoL  'bei  Leben'  sva.  'leben- digen Leibes,  lebend';  yai  j°  frapayemi aoi  sqm  . .  "wenn  ich  lebend  hingelange zur  . .  Erde"  YL5. 63.
Statt  */h-iini  geschr.,  S  368. 25.  —  Zum  Praes.
dby  Google
6ii  Juya-
ao  des  V,  'gay-,  Bthu  IF.  13.  143.  —  «i.  vgl, yävnijivam,
l.Jum  Yl  13.  9,  F.  /J:  %.  ßva-.
•  j.  Juya-  Adj.  (fem.  °yS')'.  s.  unter /fö,^^-.
•  j.  Jya-Jata-  Adj,  Von  der  (Bogen)sehoe getroffen,  geschnellt:  isavasal  . .  'tanhi vaamna  "die  Pfeile,  die  von  der  Sehne geschnellt  dahinfliegen"  Yt.  10. 39.
•  j-  jyamna-  Adj.  (fem.  °«a-),  PPM. s.  'y>är-.
KompE.
•  j-  "^y^-  V.  'debilitare,  minuere*.  Praes. \\  jina-,  »7  (Pass.)  j^'o-'',  —  Inf /oyat'*.
jinäiti  'debilitat'  F-J5;  —  'jyamna-. xä\t  frä  dnwS.:  'frajyamna- .
ttt. _/V«ätf 'altert'.  —  \g\.jGJä.ar>la-.  —  Pü.: ofaiiAtnltä.  —  ')  D.  i.  Jiy-,  daher  auch  Jay° gescbneben,  S  *S#.  n.  —  «  sd.,  mit  No,  — 3ä  Vgl.  zu  ,taÄ/<  mit  No.  3.
•  j.  ^yä-'>,  p.  _;t)'J-»>  £  'Sehne';  a)  im Fleisch  (nur  Komp.).  b)  des  Bogens: yat..'yä{^.)  navi^yan  (sd.)  Yt/0.ii3i —  as(i  yS  gavasnahe  (sd.)  snäuya  -ya (NS.)  Yt70.  laS.
KompA.,  E.  —  ai.  /ya-  f.,  »p.  vgl.  ä  (woiu Hbm.  IFAnt.  /a  21).  —  ■)  D.  i,  Jiyä-,  s,  den NS.  >a   und   S  ?ä*  8.    —    >)  Unaicher;    s.
"  j-t  g-  jyätay-  f.  'Leben'.
KompE.  —  Zur  ä-'Erweiterung'  des  V.  'gay-; ^E'-  et-  Wv  mit  Hbm.  AGr.  /.  459  0.  —  Vgl. Jyälav;  —  I)  Gmi  abweichend  Hibt  Ab- iaul  113.
•  g.  Jyätav- :y>T/»-''  m.  'Leben':  talclt ma  mSnndm  (sd.)  JyStüm  Y.  J2.  11;  — ySi  gSus  mBrmdm  urvSxs.uxl{{&A^  jyötüm Y.J2. 12;  —  dus.sasti!  .  .  mSrindai  (sd.) .  .  jyatSus  .  .  xratOm  Y.  J2,  9 ;  —  yastim xia%raf  .  .  msi^at  (sd.)  jyätSui  vä  Y. 46- a;  —  ys  is  fymiä  hlmi^yai  (sd.) vas7.itSiscä  Y.  5^.  9 ;  —  avais  aibl  ying dairüT  nSitjyätJm  xiayamnfng  vasS  "durch die  (gerade),  die  sie  nicht  nach  Gefallen über  ihr  Leben  schalten  lassen"  Y.^2. I S-  2)  'Lebensunterhalt' :  y!  nsitjyötäm hanarf  (sd.)  vinastJ . .  "der  seinen  Lebcns- miterhalt  nicht  findet  ohne  .  ."  Y._j/.  15.
VgL  jyälay.  —  ai.  vgl.  jh.-ila'i^  m.,  f.  (eine Umgeitaltung  nach  dem  Vra,t%.Ja-ati;  JSchmidt KZ.  j».  378.  Falsch  MlLLs  G.XXiv,478i. — Pfl.:  iBiimöniaHd^ih\ia:aniiakih,  {yi\. 53^46): iana,  iam'Sn  ielid'i.  —  i)  S  39^-  6.  —  '}  Öber- seliung,  nicht  Erläuterung  wie  MlLLS  G.  H5 annimmt;  Sü.i  fmnldra^.  I
•  j-i  g-  J'***  Adj.:  s.  unter /rfn-.
ti  611
```


## [2026-09-06T14:55:15.078Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN ziyan\"; grep -n \"zijän\\|zijan\\|ziyän\\|zyän\" HRN.txt | head -10; echo \"=== HUB ziyan\"; grep -n \"zijän\\|ziyän\\|zyänay\\|zijan\" HUB.txt | head -10; echo \"=== PHD zyan/gad\"; grep -n \"^zyʾn\\|zyān\\|ziyān\\|gʾd\\|gād\" PHD_mackenzie.txt PHD.txt | head -20"
}
```


### [2026-09-06T14:55:15.165Z] TOOL RESULT

```
=== HRN ziyan
3455:täz^ täziSj taziyän.
5803:t. sizyänn 'Gold, golden (234); bei. LW. zar (302).
5995:LW. kurd. af/. ziyän; bei. ziyänl (307); oss. ziän,
8492:976. meryzenf merzyen, merzyän 'Kirchhof (Beleg bei SF).
10150:die katüziyän, Calc, (imäziyan, Par., das Rückert,
13813:1 tOziyän 368.
19709:ziyän 679.
20125:' ziyän 679.
20940:ziyäni 679.
=== HUB ziyan
=== PHD zyan/gad
PHD.txt:376:gabr [gpl, gwbl | M gbr, N ? gór] hollow, cavity, womb. ~ih: hollowness. баё [gc | N ~] plaster, gypsum. -ёп [-yn!] (made of) plaster. gad [gt! = Av. gada-] club, mace. gādan, gày- [SL Y TWN-tn! < А V sry ?; g'tn! | N ~] copulate with. gadar [g??]] husband. gadwar [gtwl = Av. gaóawara-] bearing a club. 1gàh [gs | M ek, N ~] place, throne, bed. ?6àh [g’s | N ~] time; a fifth division of the day; = ģāhānbār. збаһ [gs] а Gatha, hymn. gah4n [g’s’n'] the Gathas; those scriptures dealing with spiritual and theological matters. ģāhānbār [gnb] | N gáhanbár] the six divisions of the year, the five-day festivals celebrated at the ends of these. ģāhānīg [g?snyk!] relating to the Gathas; spiritual; the five epact days at the end of the year. gahbed [g’spt' | N *gahbad] treasurer, banker. ~ih: treasurership. gahl [г()А | N gal] sorghum, giant millet. gāhüg [p hwk'] bier. gāhwārag [g’swlk' | N gāhwāra] cot, cradle. ģāl [2° household, following.
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
PHD.txt:681:Zür-gugày тоо zyānūmand
PHD.txt:686:zyān [zyd?n! | M zyy?n, N ziyan] loss, harm, damage. ~par, —-ómand LEI, 2wmnd] harmful.
PHD.txt:2209:harmful pad-zyàn, rëškën, zyāngar, zyanomand.
PHD.txt:2345:husband gādār, mérag, Soy.
PHD.txt:3067:peak balën, bašn, čagād, tērag.
PHD.txt:3887:summit bālist, čagād, sar, térag.
PHD.txt:4708:padzyān purs- pursīdan pursišnīg pursišn padpānag pa(č)čībāy- pa(č)čībāgīh frazand
PHD.txt:4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
PHD.txt:5108:[109] wadtóhm 22112101 wattom „6112 RI zahá ` PES zyānūmand "ген POS zyān tros S zyüngar Ë 9455 ziyānag 1414045 zahā, zahag, zahag 1S4 XS zahar, zahr Ms zahrag JS zaxm «xS zahübag WS zay _ ys zatrī pud wi? zarrënt L My ya S zdy- — S zahīh 948 zayistan uw tress-xS zāyč eS
PHD.txt:5542:[66] dāštan nh moo dādār, gādār `> və O dādārīh ANS t€. X5 dādgāh Tr хэ dādīg 155 t$ dad, jad, yat, yazd weno
PHD.txt:5543:dādwar Sy тех dādwarīh xD у мехо Чачап, gādan 19545 āy-! - ot āmadan! VV Wrens jādūgīh AD SAMA jādūg VS MAT jādag-gūwīh A yr SU jadag-gow — SP 5tex5 jadag (EI EI dādmeh +36 ONS dādestān w^ FO) Per
```


## [2026-09-06T14:55:15.814Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD zyan\"; grep -n \"zyʾn\\|zyān\\|damage\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T14:55:15.866Z] TOOL RESULT

```
=== SOD zyan
4971:    GMS 570, 612; AVS 94                                                       damage, harm
4978:                                                                              damage, trouble, harm
13779:      0<?)give                                                       harm, damage
13791:                                                                    damager
15944:                                                                   damage
16630:       xwezakastar                                                damage
16682:                                                                      damage
16896:                                                                  damage            =^zykh, zyq}
21682:     damage                                                    6254 nyj(y)- M                        ^joj^- <u^£>-
24069:                                                                 damage, danger
32303:     harm, damage
32765:                                                                                 OcOdamage, Go)destroy, (to)violate
32767:                                                                                 SCE 217; "damage" noun. TSP 6.13, 9.15, 11.22;
33590:       harm, damage
37258:                                                                     damage
37263:                                                                     damage
37984:crupper      6468                        damage 420, 421, 3520, 4288,             7093
37987:cry 4574                                 (to)damage      10067                  deception     242, 2180, 2730, 3857
37988:(to)cry 2033, 7330, 8437, 8445,          damager     3522                       deceptive     5780, 7080
```


## [2026-09-06T14:55:26.161Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4960,4985p' SOD_pages.txt; echo \"=== which pdf page\"; awk 'NR<=4985 && /\\[pdf page/' SOD_pages.txt | tail -2"
}
```


### [2026-09-06T14:55:28.003Z] TOOL RESULT

```
     birth                                                                419 Mznd M
     TSP 2.1174                                                                aza/and ©ob. -yy      =>*zynd, Vnt
                                                                                                                        (U--«J <^jU^|j


405 Vy-     B, S          (j^ ^^ jj>)j>\j 0-^jJ>>                              tale, parable
                                                                               BBB d8                                        -l0ijl
    azay (*zy-, *zy-, Vy-) ©<*d-zaya ^z'yt-,
      *z>t-> *jy-, }zy-                                                   420 »zr B
    Go)be born
                                                                               azar Opw »zr) ^Vyr-1, Vyr-2
    GMS 570, 612; AVS 94                                                       damage, harm
                                                                               TSP 2.29; GMS 1093
406 Vy =» Bz>y
                                                                          421 »zrm      M
407 Vy- =» Vy-
                                                                              azarm ^^zrmy^                         fjj' <V^' 'j'J'
408 Vy myry =» *zy myry
                                                                              damage, trouble, harm
409 Vyr-' B                                              0^7                  BBB 483, 528, f69; GMS 1093
                                                                                                                        "1 iOL-jjIjI
    azer ©<*d-zaraya ©trans, v.                                           422 Hzrmkry(y)         M
    GcOhurt
                                                                              azarmkare ©pi. -/
     GMS 548; BSTBL, Dhy. 10; TSP 2.392; AVS 82
                                                                              trouble-maker
=== which pdf page
```


## [2026-09-06T14:55:30.579Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^4[67][0-9] \" SOD_pages.txt | head -20"
}
```


### [2026-09-06T14:55:30.623Z] TOOL RESULT

```
5110:460 >pS>ymtyh B                      ^J^O^                  471 'pn'w-      B                      Jjjy^ j&" < JJijjJ
5117:461 >p«>yp<>} B                                 j^y         472 >bnt(t) C                               J^^
5122:462 >p6>ys B                                                      14R20
5130:463 >pY>n B                                           uU3       Go)bring together, (fo)compose
5142:477 >br-3 C ^ 6>br-
5144:478 'br'mnty C
5151:479 'pr't'r B                                            ^          aParte, arhbarte ? ©pp.; pi. -/ ^nPrt'kw
45246:471      +                       ; Cosm. 307.26                  1682                                                         3249                           casande
45249:478      afkramande              aparaniancie                                                                                 3273
```


## [2026-09-06T14:55:32.787Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5125,5150p' SOD_pages.txt"
}
```


### [2026-09-06T14:55:32.838Z] TOOL RESULT

```
    appearance, vision, region
    BSTBL, Dhy. 354, 371.159(N); GMS 3l5A; AVS              474 >pnw M =» >Pn>w-
      125                                                   475 >br-' C                               0>J-C
                                                                                                      0>J ^SJ3 ] £**r
                                                                aPar, arhbar =Vbrty
463 >pY>n B                                           uU3       Go)bring together, (fo)compose
    sfyan ©ob. pi. -ty ^Py'h1
    lament                                                      C2 gloss, n p 76-7
    VJ 533 n p97                                            476 >br-2 C                                        o^jT
19
                                                                                                                 'ps"c-

      a[3ar =>»pr-                                              490 >prsr =* 'prs'r
      0<?)bring                                                 491 >brt- C                              Ui^jjT^-*-
      STi 49.12, 73.8; STii 6.19; AVS 139
                                                                     aPart, ambart ? ®pt. st. ^'br-1
                                                                     (/cObring together
477 >br-3 C ^ 6>br-
                                                                     C2 gloss.
478 'br'mnty C
                                            lAV *<j jj '£^r     492 *prtr S                                  o^ jj <cri
      aparamande, arhbaramande ©abl. -/\ ace. -*>v
                                                                     (o)fratar =*frtr, prtr1
      bringing, presentation                                         then
      BSTii 910, 48; Benv. JA 1955, 318; C2, 61V18,                  MDii pl44.6 n pl46; MDiii p80
        19,29, 31V1                                             493 'brty C             4^^<oJLi-^-<jf^^^jjT*^
```


## [2026-09-06T14:55:40.992Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\\[pdf page\" SOD_pages.txt; grep -n \"\\[pdf page 53[0-9]\\]\" SOD_pages.txt | head"
}
```


### [2026-09-06T14:55:41.079Z] TOOL RESULT

```
0
```


## [2026-09-06T14:55:44.321Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zy>n\\|zy'n\\|zyn>k\\|zyʾn\" SOD_pages.txt | head -20; echo \"=== 10000s entries z\"; grep -n \"^1[01][0-9][0-9][0-9] zy\" SOD_pages.txt | head"
}
```


### [2026-09-06T14:55:44.408Z] TOOL RESULT

```
10461:       pl32 S =» 'zy'nt
28757:8688 ryzy>n B, S                                    J^U~                 excellent ?
36408:                                                                         11253 zy'ntCt) B                              ^j.JtJL
36456:                                                                      z(i)yand ©pi. -t ^'zy'nt, zyJnt(t)
=== 10000s entries z
36530:11285 zy-w       C =» zwyt, zwy, zy-w
36533:11286 zywsk- B                               3^^f\^
36540:11287 zywsktyh B                                   v^C^jj/T
36546:11288 zywttr S
36553:11289 zyyr- =» zy'yr-                                                    SCE p76; BSTBL p77; KG 193; MSP p56; Frag.
36554:11290 zyyr- C                                j^TfjU? tCyX>\y>-             Len. pi 13
36569:11291 zyyr'mnty C                   lp><c-,l^oyj
37232:11519 zy =» z>y-                                                     chewed
37234:11520 zy})m- B          &£ JL" i j^bjOA ij^^^r^
37246:11521 zyMn    B                                         Jij    11531 zyY*yr-   B                       j^f Ijl* <»>Up-
```


## [2026-09-06T14:55:49.262Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '36400,36470p' SOD_pages.txt | grep -v \"^\\s*$\" | head -40"
}
```


### [2026-09-06T14:55:50.985Z] TOOL RESULT

```
11238 zp}p- B                                                pLi^r              (a)zyam -^zy'm, wzyto
                                                                                entirely, completely
      zpaP (zP»P-) -4>zP»0-
      (rc)taste                                                                 Benv. JA 1955, 313; TSP 3.42.119 n pl93; BSTii
      TSP 2.711,794                                                               857.16, 860.46, C2, gloss. 22V16, 23V16; ms
                                                                                  nyzY'm "not even", C2, 60V5, 31R5 p59.60;
11239 2p>k B, M                             (Jtfj)jtJ                             BSTii 890.37, 892.5
      zPak (zp»k) ©ob. -y; pi. -f =»swnt>k, zp»k,
                                                                         11253 zy'ntCt) B                              ^j.JtJL
          zb>ueq,, >zp >k(,)
       tong         language                                                   (a)zyand
                                                                               messenger ©<*zgnd- =»zynt, ^y'nt
       GMS 93, 240, 397, 378, 979; Sogdica. 6125, 64.
                                                                                VJ 1389, 1398, 1399; GMS 342 n 1; Hen.
         10; SCE 550; TSP 2.387, 1093, 7.55, 25.1; -y,
         STii 8.10; zpk\ Frag. 6.3, zfi'k, 6.6 apud.                              Sogdica. 3528
         S W, HJ 1976 p49                                                11254 zy'r C                    (j^J'-J^^Jt^r^^^.j^j
11240 zp}k -» zP>k                                                              zyar ©Khwar. >zYr ^zy'r
                                                                                moisture
11241 zb>q C                                       juj                          Benv. J A 1955, 329; BSTii 857.16: C2. 22V 16
      zPak ©pi. -/; ob -y =»zP>k
      tongue, language                                                            n p60
      STi 30.4; Sund. AoF 1974, 233; BSTii 867.41,                       11255 zyVs-      B              ? J^^y. <cf^f io>Jt£j>-
        895.49, 50, 904.24; C2 gloss. p237
                                                                                zxars ? =»*ny}rs-
    459
           (remove, 0<?)happen, Oo)arise                                 "taking" C2 p99.26
           TSP 6.145, 169 n p206; Mack. BSTBL, *uz-Yrl           11267 zyn^sy =^ zym^k
             Dhy23l                                              1 1268 zym'sy C -* zym's'k
                                                                 11269 zymWpy     S                                 p,3^
    11256 zy'rt B, S                               >3*£.s-                                                                   zyt-
                                                                        lying
          zyart ©<*zgaru =>zy>rt, zyrt, jyrt, 'zy'rt                    zayma- waPe ^zrys-*sy
          quick, speedy
          VJ pl23; TSP 2.216, 739, 13.26 114, Frag 2a.21,             Frag. 6.3 apud. S W, IIJ 1976 p49, 50n36
            25; Frag. Len. pi 13; MSP bl63; Bailey. HMV         11270 zymh B                                           ^J-P
            23; zVrU BSTBL
                                                                       zayma     (zymO ©dragma-      =*zym}, 8rymh?,
    11257 zy'rt B                                   ^y^^
          zyart =*zyrt, jyrt, zy}rt, 'zy'rt                            lie
```


## [2026-09-06T14:55:59.235Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\s*4[67][0-9]\\s*$\" SOD_pages.txt | tail -20"
}
```


### [2026-09-06T14:56:00.822Z] TOOL RESULT

```
36499:                                                                                                                           460
36573:461
36644:                                                                                                                                 462
36715:    463
36789:                                                                                                                           464
36860:465
36934:                                                                                                                    466
37011:467
37081:                                                                                                                           468
37156:469
37305:    471
37374:                                                                                                                         472
37449:    473
37569:                                                                                                                          476
37684:                                                                                                                      478
37738: 479
```


## [2026-09-06T14:56:03.162Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37156,37305p' SOD_pages.txt | grep -v \"^\\s*$\" | head -60"
}
```


### [2026-09-06T14:56:04.772Z] TOOL RESULT

```
469
       102R21, fut. 51R10, pret. 87V 12; impf. zywrt,                          pi. -tl}\ ob. pi. -fy> =»?Ywsk-, jwxsk/q          ?y
                                                                             disciple
         C2, 105R7; BSTii 835.7; BSTii 835.7
                                                                             STi 8.10, 12, 6.6, 17.1, 13.7, 22.15, 33.12, 21 34.2,
11496 zwrt'mnty C                                ^Jt<cJf
      zwart-amande                                                             53.3, 54.10, 75.11, 797 pl07-8; Sund. AoFviii
      turning, conversion                                                      1981, p220; STii 4.25, 32; C2, 57V 14; Sund.
                                                                               AI 28, 186
      BSTii 904.3ft C2, 57R30                                   ji
                                                                      11509 zwy pwny       B                              ^e1^
11497 zwrt prwrt =» zw*rt prw>rt
                                                                             zwe- pune ? =*zw-
11498 zwst- C =» zywst-, ,zw,st-                                             hair pore
11499 zwstmbkyu M                                                           BSTBL, Dhy. 151, 210, 332, 381
      zG-stambakya ©<*zuf-stambakya ?
      tyrany                                                          11510 zwy 6-    C                                  a^Tjuj^-
                                                       ^jP^+Z-M
      Hen. BSOAS 11.70 Giants. I. 2                                         zwe5     =* zwy dm*
                                                         ■5-**Ji**          (r^)threat
11504 zwstmby        M                                                      Schwartz. STSC 134.33 n pl44
      zu-stambe          ©pi. -t ^zwP'st'npy                         11511 zwydm* C                                           jojl^j
      tyrant                                                               zwe8ma ©<*uz-vaedaya            ©f. n. =»zwy5-
      Hen. BSOAS 11.66.8                                                   threat
11501 zws    B                                                              C2, 4V3, 66V4, 104R8, 111V1; Benv. IIJ 1959,
      n/zus ? =»nws2 ?                            J,j9 «■jjAli,                132-6, JA 1955, 330.23
      falcon
                                                                     11512 zwyn»kh M                          (^^y-^/oj
      SCE 226, 359; Hen. Texts. 722 n 1                                    zwinak ?
                                               J**0**. <t5^-^
11502 zwsy       C                                                          {a kind of )dress
      zose (jwsy) ©<*zau0raka           -»8r>wsy(h)                         Sogd. Cpds. 1945, 15 If
      sacrifice
                                                                     11513 zwyrt-      C                                  &&>£ ji
      BSTi 213, 223, 293 A24; BSTii 849.12: C2, 12R
                                                                            zwert ©<*uz-wartaya- ^zw'rt-, zw»yrt-
        12, ace. p84 n 62; GMS 229 A; Ben v. J A
                                                                            (to)make return
        1951,119                                                            STi 5.7 apud. Sund. AoFiii 85.7 nl44; C2, pres.
11503 zwt'k B, S               J<«vj^(u^>)«>wT                                102R19, 68V16, fut. 68R15; impv. 69V24
      zute ? (zwtk, z'wy* ?) ^jwty*                                  11514 zwyz-     C                             o>fSs\tj*~
      beer, liquor
      TSP 2.388, 599, 607, 664, 890, 959, 988, 1001,                        zwez ©<*uz-waija; S"waik          «»wyc
                                                                            (to)sift, OcOwinnow
        1010, 1024, 1035, 1049, 1118, 1188, 1202,
                                                                           S W, C2, 40R11 p84-5
        1217, 21 iii 8, 10, 14; SCE 412; Frag. Len.
                                                                     11515 zwz- C                                       o^Xj'j^
        48.6, -w, TSP 2.969; Hen. BSOAS 11.719; BBB
                                                                            zwaz, zuz ©<*uz-waza         =»zywz
        514; Texts 719-20                                                   (to)fly up
11504 zwt'k ywVy B             j'>yj>'M'>                                   3sg. opt. zwzy, C2, 31R 21n p74; Benv. JA 1955,
      zute-xware (zwtyw'rOkh)) ^zwt'k, jwty}                                  301: BSTii 892.21
      drinker
                                                                     11516 ZY B,S                 (Oj* *<** j>Xj*X<sk)S tJ
      SCE 238; TSP I960, 21 iii 5
                                                                           ti ©Idg. =»ty2, >t\ >ty, rty
11505 zwtywVOkh) =» zwt>k ywVy                                             and, that
11506 zwtk =» zwt'k                                                        Sund. KG pl93; Weber. IF76, 1971, 77 ff.;
                                                                             Mack. BSTBL pl48
```


## [2026-09-06T14:56:09.663Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37232,37270p' SOD_pages.txt | grep -v \"^\\s*$\""
}
```


### [2026-09-06T14:56:11.604Z] TOOL RESULT

```
11519 zy =» z>y-                                                     chewed
                                                                     TSP 3.87; GMS 536
11520 zy})m- B          &£ JL" i j^bjOA ij^^^r^
      zyam Ozy'm) ©<*uz-yam; Khwar. ^ym-                       11530 zy8n(h) B                             W$J£;
                                                                     ze5sn ©<*zrdduni
                   -
                msme,
             y'nsu
       (fo^z
           )co          (r<?)spend                                   hail
       VJ 244 n p92 zyWJfc, 3sg. opt. for zyWy; SCE
                      ,
                                                                     TSP 13.22 n p228, 14.10; Gersh. Locust's leg
          167 336, 349; STi 36.7; AVS 74                               p81; BSTBL, Padm. 57
11521 zyMn    B                                         Jij    11531 zyY*yr-   B                       j^f Ijl* <»>Up-
       zyan                                                          ziyer (zyy'yr-) ©impf. ^zy'yr-
       harm
       TSP 17.36                                                     (to)call
                                                                     VJ; Frag. Len. 38.24; KG 403
11522 zy^s-      B              OJ&fU; ^OJLioL; < jjii-o^^^*   11532 zyy'yr- B =* zyy'yr-, zyyr-
      zyams Ozytas-) =»zy*m-                                   11533 zyyyr- =» jyyyr-
      0<?)be consumed, (ro)be spent, (ro)be
                                                               11534 zyq> C                                  ulij«j>
        exhausted
                                                                     zlka (zykh) =^zykh, jyk*
                                                                     damage
       BSTBL; 3sg. pres. zfmsty, Intox. 24; 3sg. opt.
        zy}msyy . Intox. 25; zymsH, TSP 6.147, Hen.                  GMS 205; STii 3.76
        Texts. 715 "reads" nymsH                               11535 zykh   B                                j^^j
11523 zyV B                                         ^j               zika (zykh) ©*ziyaka <Av. zya =*zyq\ jyk}
                                                                     damage
      zar, zyar ^z^2
      poison                                                         TSP 2.85, 237, 486, 496; SCE 440; GMS 205;
      BSTBL, Vim. 132; Mack, n p23; Hen. BBB b36                       BSTBL, Intox. 17, 30
11524 zyNvr C                                        U3<j>
                                                               11536 zykh B =» zyq>
      zyawar ©<jyawar <*Szyawar <Srzyawar                      11537 zy-qnty C                              J>f <j/
        ©ob. -y; pi. -t ^Srjy^vr, Srzy^r
```


## [2026-09-06T14:56:20.607Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['BQT','MON','FVQ','FFD','ARY','HRN','KLN','AHD']:\n  e=d[k]; print(k,'|offset:',e.get('page_offset'),'|hint:',str(e.get('lookup_hint'))[:400]); print('---')\n\""
}
```


### [2026-09-06T14:56:22.639Z] TOOL RESULT

```
BQT |offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada
---
MON |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
---
FVQ |offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) |hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
---
FFD |offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). |hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
---
ARY |offset: printed page = pdf page + 1 |hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image
---
HRN |offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
---
KLN |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
---
AHD |offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
---
```


## [2026-09-06T14:56:31.147Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN page marker near ballistic (line 4331)\"; grep -n \"^[0-9]\\{2,4\\}$\" KLN_1966.txt | awk -F: '$1>4200 && $1<4400' | head; echo \"== FVQ leaf 64 (p.47)\"; awk 'BEGIN{RS=\"\\f\"} NR==65' FVQ_pages.txt | head -50"
}
```


### [2026-09-06T14:56:33.133Z] TOOL RESULT

```
== KLN page marker near ballistic (line 4331)
4256:140
4257:141
4313:142
4320:143
4349:144
4350:145
4396:146
== FVQ leaf 64 (p.47)
FOREIGN VOCABULARY OF THE QUR'AN 4:7
It would be derived from i^\ water (=- Phlv. o> /?, i.e. OPers. dpi l =-
Av. gp or jjuj ; Skt. TR agwa), and (jj to jxwr ( = Phlv. U^OO^
from an old Iranian root *raek = linquere), 2 as was suggested
by Castle 3 and generally accepted since his time. It was from the
Phlv. form that the word was borrowed into Arabic, the shortening
of the I being regular. 4 The word occurs in the early poetry, in verses
of 'Adi b. Zaid, 'Alqama, and Al-A'sha, and so was doubtless an early
borrowing among the Arabs who were in contact with the court at
al-Hira.
ii, 32 ; vii, 10 ; xv, 31, 32 ; xvii, 63 ; xviii, 48 ; xx, 115 ; xxvi,
95 ; xxxiv, 19 ; xxxviii, 74, 75.
Iblis. 6 &a/3oAoy the Devil par excellence.
The tendency among the Muslim authorities is to derive the name
from .-Jl) to despair, he being so called because God caused him to
despair of all good so Raghib, Mufraddt, 59, and Tab. on ii, 32. The
more acute philologers, however, recognized the impossibility of this
(an-NawawT, 138), and Zam.on xix, 57, says- ^
j v* jj*}\) 2M. al-Jawallql, Mu'arrab, J7, also justly argues
against an Arabic derivation.
That the word is a corruption of the Gk. StajSoAos 1 has been
recognized by the majority of Western scholars. 5 In the LXX SidfioXos
represents the Heb. *|B2? in Zcch. iii, but in the N.T. 6 5*a/3oAoy is
1 Ta tho Beliistun inscription, sec Spiegel, Die aUpersischen Keilinschriftcn. p. 205.
2 West, Glossary, 136; Bartholomae, Al W, 1479; and see Horn, Grundrias,
141 ; Sayast, (Hossaty, p. 104 ; iShikand, Glossary, 265.
3 Lexicon Jleptaglotton, p. 23. See Vallers, op. cit.: I^agarde, GA, 7; Horn,
Grundriss, 141 ; but note Vollers, 7M1G, 1, 627.
4 Siddiqi, 69. On the ground of this change from a to i, Grimmo, ZA, xxvi, 164,
looks for IS. Arabian influence, but there is nothing in favour of this.
5 Geiger, 100 ; von Kremer, Ideen, 226 n. ; Fracnkel, Vocab, 24 ; Sprenger, Leben,
ii, 242 ; Wcnsinck, El, ii, 351 ; Rudolph, Abh&ngiylceit, 35 ; Vollers, ZDMG, 1, 620 ;
Sacco, Credenze, 61. However, Pautz, Offenbarung, 69, n. 3, and Eickmann, Angelologie,
26, hold to an Arabic origin, though Sprcnger, Leben, ii, 242, n. 1, had pointed out
that words of this form are as a rule foreign.
```


## [2026-09-06T14:56:38.338Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for l in 505 506 507 508; do echo \"--- v2 leaf $l\"; awk -v n=$((l+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -6; done"
}
```


### [2026-09-06T14:56:40.185Z] TOOL RESULT

```
--- v2 leaf 505
  ‫زورق‬                                                                                                    ‫ت‬
                                                                                                          ‫اع‬‫سم‬
 ‫زود خیز‪ -‬زود مملوم است » با خای‬                            ‫کسی‌است که حیزی و مخنشی را اوبنانهاد و ازو‬
‫نقطمدار بتحتاتی‌رسیده ویزای اقطهدار زده‪ ,‬کنابه‬                                                   ‫رانیده شد ‪۱‬‬

                  ‫از فرمانبردار وخدمتکار باشد‪.‬‬              ‫رو به = صم اول وفتح مای‌فارسی‪ .‬بلفت‬
--- v2 leaf 506
 ‫‪٩۰ 6‬‬                                                                                              ‫زور زرین‬
 ‫وغرورباشد واین‌لفت‌را درفرهنگه جهانگیری‌زور‬                                                ‫کشتی کوچك را‬
‫دوم اصحیح کرده‌ا ندکهتقدیم‌دال باشدبواو‪ .‬له اعلم‪.‬‬
                                                                                            ‫و کلاحی‬    ‫گومند‬


--- v2 leaf 507
  ‫زوترگ‬
                                                                                                               ‫ات‬   ‫ی و ه‬




--- v2 leaf 508
‫—‬        ‫‪4 6٩‬‬
                                                                                                               ‫زو‬
‫دیگر وعربان کربه خوانند‪.‬وبلفت زندویازنه(‪)۱‬‬                                    ‫رزبون وحقیر جثه راکونند ‪.‬‬
                               ‫لسر همین معنی دارد‬
                                                           ‫» بمعنی‬     ‫دننگ‬
                                                                          ‫روز‬
```


## [2026-09-06T14:56:45.062Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"زیان\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-06T14:56:45.127Z] TOOL RESULT

```
2389:  ‫قروغی ‪ .‬فون زیانهای میگانه در زبان فارسی ‪ .‬آموزش ویرورش ‪٥: ۵۲‬ص‏ ‪ »۸۳‬؛ جامة کوتاه‬
2962:                            ‫(‪ )۲‬چش ‪ .‬زبنان (رك‪ :‬زیان ) ‪.‬‬                       ‫(‪ )۱‬چك‪ :‬ژند وپاژند ‪.‬‬
5310:‫جر نداب = بادال ابچد بروزن رسن‬                       ‫جر" شمر ‪ -‬بکسر میم کنابه ازتازیانه‬
5608:                                                           ‫مافتد وزیان‌آن رامانندقاب ازیش چشم آویز فد‬
9637:                                ‫تابستالی راکویند‪#. .‬‬       ‫خاناده ‪ - 4‬بروزنآماده »بزیان اهل‬
13585:                                                                 ‫مردم باشد بمتوان تمسخر و شیرازیان آنرا‬
17954: ‫کاینات است که بیغمیر ما صلوات الهعله وآله‬                     ‫اول بده‌ذهب ونامقید وفاق‌را گویند بزیان زند‬
25709:   ‫*‪ -‬زیان روسی یکی از زبانهای هند و ارویامی و ازشعب زبانهای اسلاوی است وزبان‬
25929:‫سمرقند‬          ‫بافا » بزیان سغدی‬     ‫‪-‬‬    ‫روف‬                                     ‫است از مذهب ودین خود ‪.‬‬
30003:  ‫‪۰‬‬     ‫‪ °‬رك‪ :‬لفت فرس ص‪41‬‬                     ‫رك‪ :‬زاووق‪. ‎‬‬              ‫‪٩‬‬            ‫زیانه (ه‪.‬م‪‌ ).‬‬       ‫ص‬   ‫‪۸‬‬
39239:             ‫است ‪ -‬و درعربی کرمی رگاگ‬            ‫سوزیان ‪ ۴‬با زای هوز بر وزن‬
40610:  ‫‪ - ۴‬درزیان کنولی بمعنی طیااحه استعمال‌شود‪.‬‬                 ‫«شاهنامة بخ ج ‪۹‬ص ‪۵۲۸۲٩‬‏ ‪.‬‬
```


## [2026-09-06T14:56:50.412Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=30003{n+=gsub(/\\f/,\"\")} END{print \"leaf index:\",n}' BQT_v2_pages.txt; echo \"--- print that leaf\"; awk -v n=511 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -40"
}
```


### [2026-09-06T14:56:51.998Z] TOOL RESULT

```
leaf index: 504
--- print that leaf
                                                                                              ‫ات‬     ‫‪0‬‬


‫ودرا دجاگنجی است و من برآن اعتماد دکردم‬                ‫دوابی است در عربی که بفارسی زرلباد گوشد‪.‬‬
‫زهی سلیم دل کهتوباشی ‪ .‬چون این بشنیدباز‬               ‫رهمت = بکر اول بروزن لعمت؛بوی‬
‫زمین میکند‬   ‫آمد ‪۳‬‬     ‫بخالة خود‬    ‫گردید و‬                            ‫شت وبوی ماهی‌خام باشد‪.‬‬
‫تا هاولی زرین بیافت بوزن سی من و از آن‬              ‫زهمن ‪ -‬بفتح اول بروزن بهمن » نام‬
                                   ‫توادگر کف‬
                                                     ‫صاحب آن‬     ‫‪ .‬وتف‬     ‫خانه‌ای بوده در شهر ری‬
‫رهنحه د بکس اول بروزن شکنجه‪,‬‬                         ‫خانه مردی درویش بود ‪ .‬شبی درخراب دید که‬
           ‫بمعنی رباضت وسختی وآزار باشد‪.‬‬             ‫در دمشق گنجی خواهد بات بنایر آن «سدمشق‬
  ‫چور‪.‬ك‬
      ‫ورزن عد‬
            ‫رهو ‏ بفتح اول ب‬                         ‫رفت و سر کردان وحیران بر گرد کوچه و بازار‬
                      ‫کوش راگویند ‪.‬‬                  ‫میگثت تاگاه مردی دوچار اوشد ‪ .‬برسید که از‬
‫بکر اول وزای شله‬           ‫زه وراد‬                   ‫کجابی و دربن شهر سر کشته وحیران چرابی ؟‬
‫دار(‪ )۱‬بالف کشیده وبدال بی‌نقطة(‪ )۲‬زده » این‬         ‫کفت ‪ :‬مرنازی ام و از ملك ری هی یم ودر‬
‫لفت از توابم است بمعنى زن وفرزلد و اهل‬               ‫خواب دیده‌ام که در دمشق گنجی بیابم باین‌شهر‬
                            ‫وعیال و نل‪.‬‬               ‫بطلب گذجآمده‌ام وکنج را میجویم ‪ .‬آن شخص‬
 ‫زیدن ‪ « ۴‬بکسر اولبروزن شیمن‪,‬‬
                            ‫ه‬                         ‫کق‪ : -‬چندین سال است کهمن بخواب‬               ‫بخندیدو‬
‫بمعنی زاییدن باشد ‪ -‬وفتح اول بمعنی‌افتادن ‪-‬‬          ‫انست نامآن رهمن‬   ‫خانه‬     ‫ری‬    ‫دیده‌ام که در شهر‬




                                        ‫بیان هیحدهم‬

           ‫درزای نقطه‌دار تابای حطی مشتمل برستجاه ونه لعت و کنات‬

‫خود بدرون رفته امت ‪٩‬‏ ععنی ازحد واندازءخود‬            ‫زی ‪ » ۴‬بفتح اول وسکون الی " جان‬
 ‫بیرون رفته است ‪ -‬بومعئی سوی وطرف‌وجاب‬                ‫و حبات و زد کی را گوند که نفی وروح‌است»‬
‫چنانکه گوند « زی فلان »‬      ‫وترديك هم هت‬
‫یعنی طرف فلان وسوی فلان وجاب‌فلانو ترديك‬              ‫درار باین معانی گوبندکه «دیرزی» یمنی بيار‬
‫فلان ‪ -‬و بناشدید ثالی در عربی بمعنی شعار‬              ‫بمان و پیوسته زنده باش ‪ -‬وبکر اول بمعنی‬
                                     ‫باشد ‪. ۴‬‬         ‫اندازه و حد باشد همچنانکه گویند « از زی‬

                                   ‫یی لقطه ‪.‬‬    ‫‪-‬‬   ‫(‪ )۲‬چك ‪:‬‬            ‫‪.‬‬
                                                                        ‫ا‪-‬‬‫ك ‪:‬‬
                                                                            ‫ز‬ ‫و چ‬
```


## [2026-09-06T14:57:11.750Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 512 513 514; do echo \"===== leaf $i\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | grep -n \"زیان\\|زیانه\\|^\" | head -45; done"
}
```


### [2026-09-06T14:57:13.542Z] TOOL RESULT

```
===== leaf 512
===== leaf 513
===== leaf 514
```


## [2026-09-06T14:57:16.659Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v2_pages.txt; awk 'NR<=29900{n+=gsub(/\\f/,\"\")} END{print \"leaf at line 29900:\",n}' BQT_v2_pages.txt"
}
```


### [2026-09-06T14:57:18.610Z] TOOL RESULT

```
683
leaf at line 29900: 503
```


## [2026-09-06T14:57:23.363Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for r in 506 507 508; do echo \"===== record $r (leaf $((r-1)))\"; awk -v n=$r 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -45; done"
}
```


### [2026-09-06T14:57:24.910Z] TOOL RESULT

```
===== record 506 (leaf 505)
  ‫زورق‬                                                                                                    ‫ت‬
                                                                                                          ‫اع‬‫سم‬
 ‫زود خیز‪ -‬زود مملوم است » با خای‬                            ‫کسی‌است که حیزی و مخنشی را اوبنانهاد و ازو‬
‫نقطمدار بتحتاتی‌رسیده ویزای اقطهدار زده‪ ,‬کنابه‬                                                   ‫رانیده شد ‪۱‬‬

                  ‫از فرمانبردار وخدمتکار باشد‪.‬‬              ‫رو به = صم اول وفتح مای‌فارسی‪ .‬بلفت‬
‫زود سبره کنابه کایز‌است که از‬                                ‫نزدوپازند(‪)۱‬؛به‌عنی‌قرض بباشید‌ودبعنر‌خوانند‪.‬‬
             ‫زودسر شود ودلگر کردد‪.‬‬         ‫صصت‬
                                                            ‫‪ = ۴‬با ثالی مجپول‌وبای‌فارسی‬         ‫دون‬
                                                            ‫‪ ۰‬حربة مردم گیلان است» وان‬           ‫بر ورن چوبین‬
                        ‫وصاحب جمعیت باشد ‪.‬‬                  ‫ران دوشاخ باشد و در‬          ‫کده‬
                                                                                           ‫نیز کوچکی بو‬
 ‫رور = بفتح‌اولوثانی بروزن نظرءیمعنی‬                        ‫و نام سرکاوی‬    ‫‪-‬‬   ‫فدرم بدان جنگ مکرده‌اند‬


‫زبر است ‪ ۱‬که بالا باشد چه درفارسی بای ابجد‬                                                            ‫‪.‬‬   ‫هم هت‬


                  ‫و واو بهم تبدیل مییابند ‪. ۷‬‬               ‫روخ ‪ - ۴‬بروزن شوخ ‪ .‬کوشت‌پاره‌ای‬
‫رورا = بفتح اول وسکون انی و وای‬                             ‫که بر تن مردم بروید و آن را بسربی ولول‬
‫کشده ‪ ۳‬دح له بغداد ‪۳‬‬       ‫(( بالف‬      ‫بی نقطه‬                                                       ‫خوانند ‪۲#.‬‬
‫کوبندو بعضیکوبند زورا‪,‬فداداست وعربی‌است‪. ۷‬‬                  ‫دواشنا ؟ ‪ -‬باشین نقطه‌دار ونون بر‬‫‪ ۱‬ز‬
‫رورانه* = فبتحر‌وآوزلن‌همخانه‪ ,‬بندی‬                         ‫وزن زود ار جا » نذر و نذوراتیرا کونند که‬
          ‫باشد آهنین که بر پای بندبان گذارند‪.‬‬                                   ‫خاتها اور لد ِ‬    ‫فارسان بش‬


‫زودفین ‪ ۳‬با فا بر وزن دوربین ‪.‬‬                              ‫رود‪۵‬اندار * ‪-‬زود معلوم است »‬
                                                            ‫باهمزة مفتوح و نون ساکن و دال بی‌نقطه‬
‫چارچوب در وصندوق وامتال آن زلند وزنسصر بر‬                   ‫بالف کشیده و بزای نقطه‌دار زده › لففای است‬
                      ‫آن اندازند وقفل کنند ‪.‬‬            ‫که حربی بدیپه گوبند و تفیر آن سخن بی‬
 ‫رورگ = بفتح اولونالك وسکون قاف»‬                                                                  ‫اندیشه است‪.‬‬

                                 ‫‪.‬‬   ‫بی نقطه‬   ‫‪-‬‬   ‫‪:‬‬   ‫چك‬     ‫(‪)۲‬‬           ‫(‪ )۱‬چك زد ویاژند‬
         ‫ژوبن = ژوین ‪٠‬‏ رك ‪ :‬اسشق ‪. ۹۸۱‬‬                ‫‪-‬‬‫‪۴‬‬           ‫‪.‬‬   ‫رك ‪ :‬لغت فرس ‪۶ ۲‬‬          ‫‪۱‬‬


   ‫‪ - ۴‬جزو اول کلمه رقاای پورداود «زور»‬                       ‫رك ‪:‬رح ‪ ۰‬رخ »آزخ ‪ ۰‬آژخ‬              ‫‪۳‬‬

   ‫بفتح اول(اوستا‪ )2]211022‬دانندبمعنی آب مقدس که درجشنهای‌زردشتیان بکارروده وشابد جزودوم‬
    ‫® ‪ -‬ازدساتیر«فرهنك دساتیر ‪۹۶۲‬‬          ‫مصحف «اشتنام» (دعایی که دارسممر‌زورخوانند) باشد‪.‬‬
   ‫‪ - ۷‬زور (درزبان کتولی‌بض‌اول ودرقدیم با واومجهول) پهلوی‬                        ‫‪ - ۱‬رك ‪ :‬زر ‪.‬‬
  ‫(قوت) ‪ .‬از اوستا ‪ ( 12۷82-‬قوت) « بارنولمه ‪ ۹۸5۱۰‬آرمنی ع تلا‪ 22‬دیبرک ‪»۵۲۷‬‬                                   ‫‪۲‬‬
                            ‫توالابی ‪:‬‬    ‫در فارسی « زاور؟ («‪.‬م‪ ).‬بهمن معنئی آمده ؛ قوت » نبرو ‏‬
         ‫«کلتان ‪. ۸4‬‬           ‫با خداوند غيب دان لرود ‪.‬‬                    ‫زورت ار بیش مهرود با ما‬
                                       ‫مرجم البلدان *زوراء » نام بفداد است ‪.‬‬     ‫‪-‬د‬
===== record 507 (leaf 506)
 ‫‪٩۰ 6‬‬                                                                                              ‫زور زرین‬
 ‫وغرورباشد واین‌لفت‌را درفرهنگه جهانگیری‌زور‬                                                ‫کشتی کوچك را‬
‫دوم اصحیح کرده‌ا ندکهتقدیم‌دال باشدبواو‪ .‬له اعلم‪.‬‬
                                                                                            ‫و کلاحی‬    ‫گومند‬



                                                                                            ‫رانیزکویند باندام‬
‫بقتح اول ‪ 1۳‬تالث ‪ 0‬تمعتی‬      ‫روره؟‪-‬‬

 ‫فقره است و فقره درعربی‌مهرهای پشت‌را گویند‬                                                  ‫کشتی که قلندران‬
 ‫سخنان شراستعمال کنند ‪-‬‬        ‫رات‬
                                 ‫قاز‬
                                   ‫رقفمج‬
                                       ‫بطرب‬
                                          ‫وب‬
                                                             ‫بگرذساررند و انرا کپکاهی‌هم میگوند ‪. ۱‬‬
 ‫دورن = بنالی مجهول وفتح ثالث بر‬                              ‫ردودق ددلی ک=نابه از خورشيد‬
‫ونام یادشاهی‬   ‫_‬   ‫‪ ۰‬نام ولامی اسخ ‪۵‬‬           ‫وزن سوزن‬
                                                                                                  ‫عالم آراست‪.‬‬

 ‫لیزبوده ‪-۷‬وبکسرئالث بروزن»ومن؛بمه‌نی‌درم‌باشد‬
‫‪.۷‬‬      ‫است‬
          ‫‌هشت‬
             ‫هو‬‫بچهل‬
                  ‫حن‌‬
                    ‫کهبعربی‌درهمکوبند وآ‬
                                                              ‫زورق سیمیی» کنابه از ماه یکب‬
‫اول و سکون الی‬          ‫م‬    ‫رور نی =‬
‫وئالت ونون بتحتالی کشنده ‪٩‬‏ بلفت‌ز اد ویازاد (‪)۱‬‬
                                                             ‫رورفی‪ ۲‬حنوعی اکزلاه قلندران ‪.‬اعد‬
                                                                                     ‫وآن شیبه است مکشتی ‪۱‬‬
‫وبفتح‬    ‫رکبه خوانند ‪- ۸‬‬    ‫و هر ی‬       ‫را گوند‬      ‫زاو‬


         ‫الث بروزن سوزنی هنوب بزوزن باشد‪.‬‬
 ‫زوره = بروزن کوزه »‪.‬گربه وموبه‬
                              ‫ر‬                               ‫‪:‬ممنی صاحب فوت و توانا باشد چه‌مند بمعنی‬
                               ‫و توحده زا گویتن ً‬


                                                              ‫ه با نون ومیم‌بروزن نبرزین»‬        ‫رلوبدم‬
                                         ‫‪۲ ٩‬‬     ‫‪۰‬‏‬


===== record 508 (leaf 507)
  ‫زوترگ‬
                                                                                                               ‫ات‬   ‫ی و ه‬




 ‫و صندوق‬        ‫زورفین است که زرفین در خانه‬                                               ‫وصاحب قوت را گیفزته‌اند‪.‬‬
                                                    ‫باشد ‪.‬‬        ‫روع = بر وزن دوع ‪ ۰‬نهر و رودخانه‬
 ‫رولالی = بروزن دولابی ‪ ۰‬ام‌جاسوی‬                                                               ‫کون ‪:‬‬
                        ‫‪۱‬‬                  ‫اپوسلم بوده ‪.‬‬
                                                                  ‫خشاثاوتر‪.‬خشك‬       ‫دونوع میباشد‪:‬‬        ‫دوایی است‌وآن‬

‫باشد که بربای‬         ‫و آن‌آهنی‬   ‫زاولانه است؛‪:‬‬       ‫ممعي‬         ‫سای‬   ‫بر کے‬    ‫توان‬          ‫کر‬       ‫باس ‪۳‬‬      ‫‪ ۱‬زوفای‬


 ‫گنه کاران لهند و بر بای ستوران بیز کنند‬
                                                                  ‫‪1‬‬              ‫‪۸‬‬          ‫مکی میماند و به‌ترین دک‬
‫مجمد وییجینه را‬              ‫ی‬
                             ‫و‪-‬‬‫میند‬
                                  ‫ووگو‬‫وبتر کی بخا‬
                                     ‫لگىفزته‌آند ‪۰‬‬
 ‫زولزده = بازای نقطمدار برورن‌غول‬                                                          ‫شهرت دارد ‪ .‬گرم و خشاك‬

                                                                                            ‫است‌درسیم ؛ وتررا زوفای‬
                                             ‫گونند (‪.)۱‬‬                                    ‫که‬   ‫وآن چر کی‌است‬           ‫رطبه‬


‫زلوهین ‪ - ۴‬با لام » بروزن و معنی‬                                                            ‫برزبر دلب گوسفند ارمن‬
    ‫زورفین است که زرفین درصندوق زر باشد‪.‬‬                                 ‫زوفا‬               ‫جمم میشود‪ .‬وئوع دیگر‬
‫و هره‬     ‫حصه‬     ‫»‬    ‫چون‬    ‫بر وزن‬   ‫‪-‬‬     ‫رون‬                   ‫نیزدر اختبارات گفته‌اند ‪ .‬طبیمت آنکرم‌است‬
                                           ‫باشد ‪۳‬‬   ‫وقسمت‬                       ‫درسیم ‪ .‬استفقا را نافع باشد‪.‬‬
 ‫روج ‪ = ۱‬بقتح اولرئانی وسکون‌نون‬                                  ‫روفر!) = بفتح ثالث‌ورای بی‌نقطه‌بر وزن‬
‫وجیم ‪ .‬رودهای گوسفند باشد که باگوشت وپیه‬                           ‫مشیرازی‬    ‫آنرا‬        ‫رونما » تخم دارویی است که‬
 ‫بر کرده قاق کنند ودروقت حاحت یلزدوخورند؛‬                          ‫آهودوستك خوانند ‪ ۳‬ویر که آن ماد کرفی‬

 ‫وبکر اول حم گفته‌اند؛وباین‌معنی‌بجای لون‌بای‬                                    ‫باشد‪ .‬گزندکیعقرب را فافع است‪.‬‬
                                                                   ‫رو فرن ِ = پروزن‌دور‪,‬ین» ژرفین‌در‬
‫زو نز که ‪ - ۲‬بنتح اول وئالی و زای‬                                                           ‫خانه وصندوق را گونند‪.‬‬
 ‫قطمدار ودکون تالث وکاف » مردم کوزیشت ت‬                           ‫معنی‬   ‫و‬   ‫‪ -‬بالام ‪ ۰‬بر ورن‬        ‫‪۴‬‬    ‫روفلسی‬



                                                        ‫(‪ )۲‬چك ‪ :‬با‪.‬‬                 ‫‪ :‬خوانند ِ‬      ‫جك‬       ‫)‪۱‬‬
```


## [2026-09-06T14:57:33.557Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for r in 513 514; do echo \"===== record $r (leaf $((r-1)))\"; awk -v n=$r 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -50; done"
}
```


### [2026-09-06T14:57:35.348Z] TOOL RESULT

```
===== record 513 (leaf 512)
   ‫—‬       ‫‪9‬و‬   ‫=‬




 ‫بزان = بروزن میزان‪.‬به‌عنی‌زبباوخوش‬                            ‫ریاد ‪ -‬یکسر اول » بمعنی آفزولی و‬
                                               ‫آینده باشد ‪.‬‬    ‫از بازبهای ارد‬         ‫ی‬
                                                                                      ‫کنام‬
                                                                                         ‫ی‪-‬و‬
                                                                                           ‫زبلدنی باشد ‪٩‬‏‬
                                                                ‫است ‪ - ۴‬وبمعنی‌زندکال یکند بعنی‌همیشهزنده‬
                                               ‫کردن باشد ‪.‬‬     ‫باشد» هم هت ‪ - ۴‬وشخصی را نیز گوبند که‬
 ‫لین = بکر اول بروزن بیجن؛شخصی‬                                                              ‫کواهی بتاحق دهد ‪.‬‬
‫دیا داده‬        ‫را کونن که عالم را بشت یا زده ورك‬              ‫ریاده سره کنابه از کسی است که‬
                      ‫باشد ؛ وبقتح اگوفلتههم‌اند ‪.‬‬             ‫مسقد خود باشد و کاری‬               ‫زباده بر حالت خود‬

 ‫ر تار » بفتح اول وتای فرشت بروزن‬                              ‫پیش کیرد‬         ‫دنآمد‬
                                                                                    ‫نآ‬‫اعپد‬
                                                                                         ‫واز‬
                                                                                           ‫تکه‬
                                                                                             ‫ر را‬
                                                                                                ‫بهمی‬
                                                                                                   ‫وم‬
 ‫بی‌زار ‪ ۰‬ثفل زتوای که روغنآنراکشيده باشند‬                                                          ‫وباتجام برساند ‪.‬‬
                    ‫وبعربی حکر الزیت (‪ )۱‬خوانند‪.‬‬               ‫فان د بر وزن میان ‪ .‬بمعنی قان‬
‫ریت بنی اسرائیل ‪ -‬سنگی است‬                                      ‫وزبینده ® و زندگالی کننده ‪۷‬‬
                                                                ‫ادم‪-‬ر بابن‌معنی‬     ‫ووبن‬
                                                                                       ‫وزید گانیکردن را نیز گ‬
                                                                                                                ‫باشد ‪۴‬‬

 ‫برنگه و اندام زیتون و خطوط بسیاری موازی‬
                                                                        ‫هم هت یعنی زند کی بده وزنده بدار‪.‬‬
 ‫بکډیگر دارد و آرا بعربی حجرالیهود وحجر ‪-‬‬
                                          ‫الزیتون گوبند ‪.‬‬          ‫بیاوی‬
                                                                       ‫رلب = بکر اول وسکون ان‬
                                                                ‫اد ‪ .‬بممنی زینت و تیکوبی و آراش‬
‫و سکن ثالی‬                 ‫سور‬
                             ‫ربج ‪ -‬بمااکول‬                                                                  ‫اشد ‪. ۷‬‬
 ‫و جیم ابجد » معرب زیگه‌است» کوتآانبی‌باشد‬
 ‫ورکات افلاك و کوا کب‌را‬
                       ‫که منجمان احوار ح‬                        ‫لیا *‪ -‬بروزن‌دیباءبسمنی ییکووخوب‬
‫از آن‌مملوم کنند *‪ -9‬ونختَة بنابان ومعماران که‬                   ‫وعنی‬‫‪-‬م‬
                                                                      ‫امت که نقیض زشت و بد باشد ‪٩‬‏ ب‬
                                                                                                    ‫زیتله هم هست‪.‬‬
 ‫بناییرا‬        ‫تة‬
                 ‫‪-‬و‬‫ر‏ش‬
                     ‫در آن طرح عمارت کشند ‪٩۱‬‬
 ‫نیزگفته‌اند ‪۴۱‬؛ و بستی گوبند باين دو معنی‬                      ‫ریبال ‪ -‬با بای ابجد بر وزن قیقال »‬
 ‫اما اصممی‌میگوید‪ :‬من نمیدانم‌این‬                 ‫عربی است ‏‬       ‫تندروباشد‪.‬‬    ‫لی‬
                                                                                  ‫او‬‫وشتر‬
===== record 514 (leaf 513)
     ‫زبرزبان گفتن‬
                                                                                                                ‫تب ای ‪ ۵‬ات‬




     ‫زرا ‪ ۴‬بکر اولوثاك بالف کشبده‪.‬‬                                  ‫لفظ فارسی است‌یا عربی ‪ -‬وبا جیم فارسی‌بمعنی‬
                        ‫‪.‬‬    ‫ازبر ای آن و آزین جهت‬       ‫سی‬         ‫بیرون آوردن و بیرون کشیدن باشد ‪ -‬و خوش‬
                                                                    ‫وچايك وجلد وخوش وضع را نگیوزبند ‪-‬ونومی‬
     ‫کنابه اززبون بودن‬           ‫زير از میانه =‬
                                                                    ‫از انگور بقایت خوش لذت باشد ‪ -‬وبمعنی لاغ‬
                                       ‫و بد بودن باشد ‪.‬‬
                                                                    ‫وم‌خر ‪ 3۳‬همآمده است ‪ -‬وزهوار کفش وموزه‬
     ‫شیر افکن ‪.‬‬             ‫وبزرن‬
                                ‫زیرافکی * =‬                         ‫را هم میگوبند ‪ -‬و ربه‌انهاییکه استادان نقش‬
     ‫ووشك و آنچه در زیر افکنده‬
                             ‫بمعنی نهالی ت‬                                              ‫ند لش جامها را بدان نندلد‪.‬‬

                                                  ‫خوالند ‪.‬‬          ‫ر بجك = باجیم فارسی بروزن ميخك"‬
                                                                    ‫رگوودسفند راگونندکهبگاوشت وبرنج‌ودیگر‬
     ‫زير افکند * = بسکون‌نون ودالابجد‪.‬‬
                                                                ‫باشند و بگذارند تا خشك شود‬                     ‫دره‬
                                                                                                                 ‫رپ‬‫کالح‬
                                                                                                                      ‫مص‬
     ‫بممنی زبر افکن است کهنهوالتیوشك و آله‬                          ‫و در زمستان بپزند وبخورند ؛ ویعطی گوبندرور‪:‬‬
     ‫در زبرافکنده باشد ‪ -‬و نام مقامی‌است ازموسیقی‬
                              ‫کنرچك است ‪.‬‬  ‫که آ‬
                                                                    ‫بر شیر خواره است که آلرا پاکیزه کنند و در‬
                                                                    ‫هم بیچند مالند نارئجی و چندی از آن را بر‬
     ‫در بر = بضم بای ایجد (‪ )۱‬وسکون‬                                 ‫فقرا‬          ‫ان‬
                                                                                   ‫بارا‬
                                                                                      ‫بندرو"‬
                                                                                           ‫کن‬             ‫ب‬
                                                                                                          ‫او‬‫بند‬
                                                                                                              ‫کخ کش‬
                                                                                                                  ‫سی‬
     ‫رای فرشت )‪ » (۱‬کتابه‌از که برباشد‪ .‬وشخصی‬
                                                                                                                    ‫خوانند ‪.‬‬
     ‫والماید‬     ‫را نکیفزته‌اند که بظاهر خود را دوست‬
                                  ‫و در باطن دشمن باشد ‪.‬‬             ‫زید لك ‪ = ۱‬با دال بروزن زبرلك ‪.‬غلام‬
                                                                                           ‫بچة نرك مقبول کروابند ‪.‬‬
      ‫زیر بزر گان ب=ائانی مجهول‌رسکون‬
‫‪.1٩۰‬‬
   ‫‪««۹‬ظ_ظ_ظ_ظ______ظش_س ‏‬
                        ‫ا‪۰‬‬
                         ‫‪«-٩--‬‏‬
                              ‫‪۰‬‬
                              ‫‪.‬‬
                              ‫‪:‬‬
                              ‫‪«۰‬‬
```


## [2026-09-06T14:57:48.416Z] TOOL CALL #49: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:1050 --image 2>&1 | head -60"
}
```


### [2026-09-06T14:57:50.054Z] TOOL RESULT

```
no scan of BQT covers printed page 1050 (see 'scans' in refs_online.json)
```


## [2026-09-06T14:57:55.046Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==513' BQT_v2_pages.txt | tail -25"
}
```


### [2026-09-06T14:57:56.906Z] TOOL RESULT

```
                                                                                           ‫رازا‬
                                                                                              ‫هایه‬
                                                                                                 ‫کت‬
                                                       ‫(‪ )۱‬خم‪ : ۱‬عکرالزیت ؛ چش ‪ :‬حکرالزنته ‪.‬‬

   ‫‏‪( - ٩‬عر) « زبادة بالکر‪ .‬افزونی» «منتهی الارب» و درفارسی فصیح نیز زیادت وژباده‬
   ‫‪ - ۴‬صیغة دعابی از «زید» سوم شخص عفرد‬                                ‫‪ :‬خاله گیر ‪.‬‬   ‫رك‬    ‫‪- ۴‬‬             ‫‪۰‬‬   ‫آورید‬


   ‫‪ - ۴‬پهلوی ‪ , 02112‬اوستا ‪ ( 80822 - ۰ 88872 -‬ضرر )‬                                       ‫مضارع از د زستن > ‪.‬‬
    ‫‪anayj -‬‏ ) طلم ) * کردی ع‬                       ‫ساسکرت‬              ‫« بارتولمه ‪۱۰۷۱٩ ۰ ۰۰۷۱‬‏ لیر گے‬
    ‫اقنانی ع ‪ ۳7132‬؛ باوچیع ‪ 102712‬استىع ‪ . ۳41012. 0812‬ارمنی ع ‪«0262‬اسشق‪.*۹۷۹‬‬
   ‫راسم فاعل از «زستن» ‪ « :‬زردشت را کفتند ‪:‬‬                    ‫‪۱‬‬           ‫سحیح «زینده» است ‪.‬‬           ‫‪6‬‬

   ‫جانور چندنوع است؟ ‪.‬گ‪..‬فت ‪ :‬زبائی کوبا وزبالی کوبا مرا وزبانی‌میرا » رك‪ :‬قابوسنامه باهتمام‬
    ‫سی ص ‪ ۱۲۷‬بامقابلة‪ :‬عبارتی‌از قابوسنامه بنقگلمارنده ‪ .‬مجلهٌیما سال‪ ۱‬شمارة ‪ 4‬ص*‪.۰۸۱-۵۸۱‬‬
                    ‫ندارد برآن روی لاله زب‬                           ‫بوی‬    ‫دارد مر آن زلف مك‬               ‫‪۲‬‬

       ‫«لفت فر ی ‪۷۲‬‬        ‫‪۰‬‬   ‫مروزی‬   ‫عمارء‬



  ‫دروی زیا‬            ‫‪٩‬‏‬                 ‫از ‪ :‬زب ‪ (۱ ۳‬فاعلی وصفت مشبهه) = زیبنده ‪.‬‬                      ‫‪۵‬‬
           ‫‪ °‬رك ‪ :‬زیگه ‪.‬‬                         ‫مرحم دلهای خسته‌است وید درهای‌بته‪« » .‬کلتان ‪. 6۱۱‬‬
```


## [2026-09-06T14:58:11.216Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ابلیس\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-06T14:58:11.274Z] TOOL RESULT

```
3504:گل گاوچشم (ذیل : آذریون) .گل گیری (ذیل :کانی ) »گن ابلیس (ذیل :
6529:۱ - اثاره بخلقت ابلیس از آنتن-ب< سوره ۷ ( اعراف ) یه ۰.0۱۱ ۴ - مراد سال
9788:۵ ابلیس - این‌درید نوخته : « اکر ابلسی عربی باشد اشتفاق‌آن از ابلس یبلی بمعنی
9790:آورده . ابلیس ا زکلمةٌ بونانی 121۵00105 بمعنی کذاب ونمام که از نامهای شیطان است گرفته
13843:بشیرازی « کن ابلیس » خوانند نم کاف فارسی
```


## [2026-09-06T14:58:14.778Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9780,9800p' BQT_v1_pages.txt; echo \"=== leaf\"; awk 'NR<=9788{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v1_pages.txt"
}
```


### [2026-09-06T14:58:16.372Z] TOOL RESULT

```
طبری 021 (نعله) « واژه نامه ۱۲۷ ».
۵ - معرب آبلوج فارسی :
نت عطار ای‌جوان ابلوج من هست نیکویی‌تکلف » بی‌سخن
مننوی . ۱ لفت نامه » .
٩‏ - نی انباخون ؛ ودرنسخه ای ازفرهنکه اسدی : انباجون
دلفت نامه . .  .‏ ۷ - مصحف انضا و اتخوسا < لخت‌ناحه ». ابلك و دانةٌ آن
* بلق - ابلق نوعی اسب است برنگه ابلك :« اسب ابلق ناستوده است ونيك خود کم
بود .» « قابوسنامه » رك : نوروزنامه س ۵۳ : ۱۵ و۱۱ -۱۱۱ .و رل : ابلك .
۵ ابلیس - این‌درید نوخته : « اکر ابلسی عربی باشد اشتفاق‌آن از ابلس یبلی بمعنی
سانقی خن کده وین ای ازارشت دا سای انت» متهناوعر ایح مه را مولتات دقن
آورده . ابلیس ا زکلمةٌ بونانی 121۵00105 بمعنی کذاب ونمام که از نامهای شیطان است گرفته
شده «نفی * « جفری ۸-6۷ *. ای - ازعربی « این» بمعنی پسرء درآشوری بابلی
۷ , عری 067 , آرامی 0۲2 . در لغات جنوب الجزیره وحبشه 960 « و لفنسون ۲۸۳*.ابو طامون ۱ ۱ ۱ رس
بیندد وآترا بعربی, «خی‌الحمار» و «حتاه النزاله» ۱
خوانند . ۱
ابو طامون ۱ - باطای حمی بالف
کشیده و میم مضموم بواه و نون زده » نوعی از
مومیائی باشد و آترا « مومیائی کوهی» کوبند
و جربی «ققرالبهود» خوانند ؛ گویند (۱)این لعت .
عربی (۲) است .
ابو علس « بفتح عن بی نقطه و
=== leaf
293
```


## [2026-09-06T14:58:26.950Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON parlemân\"; grep -n \"پارلمان\\|پارلمانی\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -8; echo \"== MON balet\"; grep -n \"بالت\\b\\|بالِت\" MON_part1.txt MON_part2.txt 2>/dev/null | head -8"
}
```


### [2026-09-06T14:58:27.053Z] TOOL RESULT

```
== MON parlemân
MON_part1.txt:28033:پارلمان: ۱ (اح.) انجمن بزرگان 
MON_part1.txt:87228:معین صورت می‌گیر د) پارلمان. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:28033:پارلمان: ۱ (اح.) انجمن بزرگان 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:87228:معین صورت می‌گیر د) پارلمان. 
MON_part2.txt:58991:نموده و بدین وسیله آنها را از پارلمان دور 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:58991:نموده و بدین وسیله آنها را از پارلمان دور 
== MON balet
MON_part2.txt:4382:له تجلی (فاعل بالتجلی): فاعلی است که علم 
MON_part2.txt:5333:(ابالت) که در امور داخلی خود استقلالی 
MON_part2.txt:19987:کبالت: !0۰2 (ا.) (شیم.) فلزی سفید و 
MON_part2.txt:28559:دریای بالتیکك جستجو می‌کنند. قشری از 
MON_part2.txt:40594:علم» سرق؛ اختر. (اصط. تر. ع.) ابالت؛ 
MON_part2.txt:56298:ها ۱۵۵1 [ع۰] (امف.) اتیعبالت 
MON_part2.txt:73985:نبالت: اهاقنا۵ه [ع. . ثبالة ] (مص‌ل.) صاحب 
MON_part2.txt:83080:انفکاکی واحد بالترکیب است که واحد
```


## [2026-09-06T14:58:28.205Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FFD gadan\"; grep -n \"گاد\\|گایید\\|gād\\|gāy\" incoming/FFD/FFD_pages.txt | head -20"
}
```


### [2026-09-06T14:58:28.259Z] TOOL RESULT

```
== FFD gadan
1899:گادن
1900:گاد < فارسی میانه 834. امروزه «گایید» به جای «گاد» به کار می‌رود. «گایید» مادهٌ
1901:گای < فارسی میانه «(قع.گادن باید از ریشهٌ 83* به معنی «گاییدن» آمده باشد.
1903:گاد < فارسی میانه 834 < ایرانی باستان 83-12 *. برای 18 - آراست.
2354:8 (ريشةٌ ضعیف ۲ 4۵۴۷) ۳۰ 8 (ريشه <گاییدن) ۷۰
```


## [2026-09-06T14:58:39.059Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FFD pdf page tag near 1899\"; awk 'NR<=1899 && /\\[pdf page/ {p=$0} END{print p}' incoming/FFD/FFD_pages.txt; sed -n '1890,1910p' incoming/FFD/FFD_pages.txt; echo \"== MON parlman ctx\"; sed -n '28028,28040p' MON_part1.txt; echo \"== MON balet\"; grep -n \"بالت:\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-06T14:58:40.964Z] TOOL RESULT

```
== FFD pdf page tag near 1899
[pdf page 75]
: کوشید < فارسی میانه 10518 < 0810 .637810 مادةٌ ماضی جعلی است. از مادهٌ
مضارع ساخته شده است.
کوش < فارسی میانه 155 2595 < ایرانی باستان 3۵5-۵" برای ۵ + آرای. در
8 زاید است. 12۵5 صورت افزودةٌ ريشه و 1۵3 صورت ضعیف آن است. ۳3 به معنی
«نبرد کردن» است» «گُشتن) هم از ریشهٌ دتم آمده است.
« کوشید نو 037120هم به معنی «سعیکردنْ»به کار رفته‌اند و هم به‌معنی «تبردکر دن».
کوفتن
کوفت < فارسی میانه /5.
کوب < فارسی میانه ۵0
گادن
گاد < فارسی میانه 834. امروزه «گایید» به جای «گاد» به کار می‌رود. «گایید» مادهٌ
گای < فارسی میانه «(قع.گادن باید از ریشهٌ 83* به معنی «گاییدن» آمده باشد.
به‌شرح زیر
گاد < فارسی میانه 834 < ایرانی باستان 83-12 *. برای 18 - آراست.
گای < فارسی میانه (83 < ایرانی باستان 83-78" 2 برای ساختن مادهٌ مضارع از
ریشه به کار می‌رفته است.
گاشتن
صورت واداری «گشتن» است > گشتن.
گداختن
گداخت « فارسی میانه ۷14371 < ایرانی باستان ۴۷۹-13۳1۵ برای 18 -> آراست. ۷1
[pdf page 76]
== MON parlman ctx
غسلخانه و جز آن؛ گنداب؛ مرداب» 
منجلات. خندق گونه‌ای که بر گرد شهر 
برای گرد فا آب‌های آلوده می‌ساختند. 
مزبله. 

پارلمان: ۱ (اح.) انجمن بزرگان 
مملکت در دربار سایق فرانسه. (اخ.) دیوان 
عالی عدليةٌ فرانسه پیش از ۰۱۷۹۱ () 
مجلس شورای ملی» مجلس نمایندگان در 
کشورهای مشروطه و جمهوری. 

پارنج: ل««-02 (- پای‌رنج] (امر.) زری که 
به شاعران و مطربان دهند تا در جشن و 
== MON balet
MON_part2.txt:19987:کبالت: !0۰2 (ا.) (شیم.) فلزی سفید و 
MON_part2.txt:73985:نبالت: اهاقنا۵ه [ع. . ثبالة ] (مص‌ل.) صاحب
```


## [2026-09-06T14:59:08.660Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== CHEUNG gad\"; grep -n \"GAD\\|\\*gad\\|gāy-\\|copulate\" CHEUNG.txt | head -20; echo \"== CHEUNG zya\"; grep -n \"ZYA\\|\\*zyā\\|zinā\\|to harm, damage\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T14:59:08.756Z] TOOL RESULT

```
== CHEUNG gad
7063:*MIDDLE PERSIAN: BMP (SLYT(W)N-) /gäy-/, inf. g’tn /gadan/ ‘to copulate, unite 
12010:copulate’). His analysis of visäpa- is not compelling though, at least no more 
12020:yav-/yivd, Sariq. yeyv-/yevd, Yi. yay-/yed, yid ‘to have sexual intercourse, copulate 
15898:kin-/kinok, kin-/kwulak ‘to copulate’ (euphem.) = kan-/kanók 
== CHEUNG zya
6161:*SANSKRIT: drav ‘to cut down’ (RV), ‘to harm, damage’ (JB) > EWAia I: 756 
17093:*maiH ‘to harm, damage, fade, decrease (?)’ 
20702:*raš ‘to harm, damage, shed ?’ 
20704:*AVESTAN: ras- ‘to harm, damage’ = Liste: 57
```


## [2026-09-06T14:59:10.988Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7045,7090p' CHEUNG.txt"
}
```


### [2026-09-06T14:59:11.033Z] TOOL RESULT

```
*KHOTANESE: jsä- ‘to go’ || (+ *ui-) LKh. bijsa- ‘to depart’. Ф The palatal Js? in these 
forms is probably from 9ѕет, *gam!. = SGS: 37, 95 

*SANSKRIT: gà ‘to step, stride’ (RV+) = EWAia I: 482 


94 *gaH2 


«PIE *g"eH,- ‘to go, stride’ = LIV: 205 | Pok.: 463 f. 

*IE COGNATES: Gr. £ Bmv (aor.) ‘was ready to go’, Gr. Bra (n.) ‘step, rostrum’, Arm. 
eki ‘went’ (sec. 1), Lith. (dial.) góti ‘to go’, at-góti ‘to arrive’, Latv. gaju ‘I go’ 
*REFERENCES: DKS: 114b f.; Werba 1997: 282 f. 


*gaH? ‘to have sexual intercourse, coire’ 

*MIDDLE PERSIAN: BMP (SLYT(W)N-) /gäy-/, inf. g’tn /gadan/ ‘to copulate, unite 
with’ 

*CHORESMIAN: m/yy- ‘to have sexual intercourse’ — Samadi: 83 

*NWIR: NP gädan (obs.), gayidan/gay-, Bal. gät/gä(y)-, Kurd. gayin, Awrom. 
gay/-ga-, Gz. gain-/gaina, Khuns. g-/gà ‘to have sexual intercourse’ 

*NEIR: Pash. yay-/yowol, Oss. I. qæjyn, D. qæjun, Wa. Ysıy-/yoyd, Sh. yav-/yevd, 
Rosh. yav-/yevd, Bart. yav-/yivd, Sariq. yeyv-/yevd, Yzgh. yay-/yed, yid ‘to have 
sexual intercourse’. © The Pash. and Pamir forms appear to show a partial 
contamination with the root *Hiab. 

*MISC: Par. geh- ‘coire’ 

Ó The root *gaH is probably etymologically related to *gaH!, cf. YAv. upaétom 
*(having) sexual intercourse’ (*Hai): it has largely replaced the old IE “иеге? root 
*Hiab. 

*REFERENCES: Horn 1893: 197; ПЕГ I: 253a; HFL II: 524a; EVS: 37b; MacKenzie 1966: 96; MacKenzie, 


Pahlavi: 34; WIM I: 68; WIM II/1: 76; Steblin-Kamenskij 1999: 191; Bielmeier 1993: 13; Cheung 2002: 
213; Korn 2005: 318, 395 


*gaH ‘to sing, call’
```


## [2026-09-06T14:59:27.199Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gämö\\|gamö.b\\|coire\\|Beischlaf\" BRT.txt | head -20"
}
```


### [2026-09-06T14:59:27.246Z] TOOL RESULT

```
4323:•  j.  'an-aiwy'ästay-  Adj.,  nur  fem,  'kein Beiwohnen  (seitens  eines  Mannes)  habend, ; ohne  Beischlaf' :  tum . .  aH'a  . .  °tis  hunahi ' "gebierst  du  allein  . ,  ohne  Beischlaf?"  V.  ■ iS-io;  31.
16029:•  j.,  g.  pärvnday-  f.  'strotzende  Fülle, Üppigkeit:  3  äit  frat^Aärayat  .  .  sIryS mayä  •lA/w/iK'aa*"..  Weiber,  Beischlaf  und FüUe  herzubringend"  A,y.4{?)".  a)  als Gottheit";  aslm  .  .  ihm  .  .  äzüitlm  .  . frasastlm  varmhjm  *'dlm "  yazamaiäi  Y.
19925:•  j.  mayah-  n.  "Begattung,  Beischlaf: vaitumnfm  yä  fravSit  (Sp.  932  m.)  Yt, 79.80;  —  stryö  °yä  faryiufi^(_sd.)  upaväzB A.,;.4;  F.i/.
```


## [2026-09-06T14:59:31.562Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'Schritt'\\|Schritt\\b\" BRT.txt | head -12; echo \"== gamo.b\"; grep -n \"gam6\\|gamo\\.\\|gämo\" BRT.txt | head -10"
}
```


### [2026-09-06T14:59:31.629Z] TOOL RESULT

```
2034:und  an  Ursprünglichkeit  des  Lautbestands,  der  Formbezeichnung  und  der  Satz- fUgung  den  Hymnen  des  ^gveda  durchaus  die  Wage  halten,  stehen  Machwerke traurigster  Art  zur  Seite,  deren  Verfasser  auf  Schritt  und  Tritt  verraten,  dass  sie sich  einer  ihnen  fremden  —  weil  längst  abgestorbenen  —  Sprache  bedienen,  in der  sie  nur  ganz  stümperhafte  Kenntnisse  besitzen.  Als  Stücke  solcher  Art,  in deren  Benutzung  für  irgend  einen  Teil  der  Grammatik  dem  Sprachvergleicher  die grösste  Vorsicht  anempfohlen  sei,  bezeichne  ich  in  erster  Reihe:  Yt.  2,  j,  4,  Vyt,  Az,, Nik.,  Vd.,  FrW.  2,  8,  g,  FrB.,  FrD.  5,  6,  7,  FrG.,  FrBy.,  Sl.  8.  zz  Z.,  in  zweiter:  Yt. //,  12,  1$,  18,  V.  S2.  Auch  andern  alten  Teilen  sind  nicht  selten  minderwertige Zutaten  ein-  oder  angeßigt,  die  sich  zumeist  schon  durch  die  mangelhafte  Syntax deuthch  als  solche  zu  erkennen  geben;  z.  B.  in  Yt  /,  V.  10, 11,  13  usw.".
7269:Schritt  entfernt  ist,  auch  dem  Wasser opfern"  N.  6g.  A)  oft  neben  Feuer, Himmel,  Erde,  Rind,  FQanzen  (usw.):  ma x^ayamna  jasStt  ätnm  . .  äp>m  . .  tarn  . . gqm  ,  .  urvarqmY.g.^y,  42,  11. 1,  2,  5, 9,  10;  —  jia}  . .  vi'iürayat  asmamm  . . np)m  .  .  zqm  .  .  gqm  .  .  urvarqm  Yt  13. aS;  86,  Y.  ig.  8;  —  ahtaatca  apäalca^'> zimaatca  urvarayaatca  gaotca  Vr.  7. 4;- — para  asrntm  .  .  äp^m  ,  .  zqm  .  .  gqJt  ,  . urvarqm  .  .  atr?m  Y.  SQ.2;  —  fravaiayö ya  asmtm^m  viöäray^n  . .  lip»m  . .  zqm  . . gqm  Y.  2^.  1 ;  —  hs  ßptm  staoiti  .  .  zqm . .  gqm  . .  urvarä  . .  vtspa  vohü  H.  /.  3 ;
10342:♦)  Gleich  drei  Fuss  nach  V.  g.  9.  F.  i/  a  heisst es:  der  Schritt  weide  im  Vendidad  zu  drei  Fuss, sonst  zu  zwei  Ellen  gerechnet,  s.  gäya-  Pü.  Bd. 36.  l   hat  der  Schritt  nur  zwei  Fuss.
10349:•  j-  gäya-  m.  'Schritt',  als  Masseinheit**: gaim  F.  27  a.
12353:V.  5-  30.  31.  9-  7.  28,  3'.  rji  33'>  N-  ", Äs,  *F.  f ;  —  'rlmgäma  frabarat . .  urria H.2.15,  33;V.4.3s,j5.7;  1.6;— />««>■ j^«&  .  .  'ryeht^a  .  .  myazdake  A.J.  10; F.g;  —  V^^V.  7.  53  PüZ.;  —  -rj"* fNPn.)  %am)art  (sd.)  V.  74.  9;  Yt.  /.  7, VA/2;  —  'ry3(^)  uitavailyh  va..hät!lii hanääta  N.  702;  102;  —  'yanqm  Vd. 75.  a)  ASn.  'rXm  und  DS.  'ryai  als Adv.;  a)  'zum  vietten  Mal':  •ryjj'' H/<»aa:  (sd.)  -rj-si»)  ai/ajÄi  V./ö'.  16;  — /äjÄ  TrM'J  *gams.hninm  "nachdem  er den  vierten  Schritt  getan  hat"  V.  s8. 55-  ß)  "beim  vierten  Ma!';  ka  he  asH a^al  .  .  'rfm  %rUatfm  upäsananqm  V. 4. »9;  23,  37. 3I1 5- S>  *■  77-  Tf)  Viertens': kva  °rJm  aiiihi x?mS ^aisUm'V.^.^;  10,23. KompE.  {äxCiÜr').  —  Ordinale  lu  ca%war-; S  311.  —  ai.  turtya-,  lurya-  Adj.  —  Pü.  T  ea- härmn.  —  <)  In  sdjekt.  Gebrauch,  beimNom.act
14593:•  j.  ^ri-gäya-  n.  'Längeoausdehnung  ff.  9,  10,  Yl  i.  7,  14, 9,  V.  4.  2,  14.  9,  N.  2, dreier  Schritte,  drei  SchritÜängen':  A«/.  Vyt  2J,  Vd.  12;  —  «iä/m  a^rapaiHm haca  paourvaMyat  ya%a  •gättn  ka%a  upSisSii  ..  'Um  ..  täirJm  N, //;  iJa,  Y.p. (sd.)  •fJ/»t  _>'B^B  . .  "Wie  weit  von  den  19,  15.13,  V.5. 31»  8.  los',  p.  7,  28,  31, beiden  ersten?  Soviel  als  drei  Schritt-  y- 33',  F.  i;  —  'tim  asanhamcä  fäiira- längen  betragen  .."  V.9, 9;  S.  11,  39;  — '  namcä  V.  i.  $;  4.  38,  !§.  5,  H.  2. 15,  Yt •gäim  haea  wr^fJ  V._y.  17,  16.  i,;  6,  ^-37, ''5-38;  —  faoiryqm  ..  'iyam  pratqm  Yt, 40; — yat  nä  fasca  yaf  uahiMf  'gaim  .,\l-].  59;  H.  2.  5,  13,  VyLj.^;  —  %raosta "wenn  man,  nachdem  man  sich  erhoben,  1  ääi/^^  °tyayi  Ytj.  62;  —  'tyä  (GSf.) drei  Schritt  (davon)  . ."  V./Ä43.  \xiapa  ^raosta  R2.7,  V.7p.s8;  —  'iya
14662:•  j.  9-risata.e$ya-  n.  'Längenausdehnung von  dreissig  Schritten,  dretssig  Schritt- längen': äaj  tum  .  .  apaiaröis  ,  .  'gaim kala  apai  V.77.4;  3. 17J.
15257:■  j.  pan£äsata.gäya-  n.  "Längenausdeh- nung  von  fünzig  Schritten,  fünfzig  Schritt- längen': 'gäim  haca  barssinm  frastairyal V.i7.4.
15968:•  j.  päÄa-  n.  i)  'Tritt,  Schritt,  Schreiten': yat  Site  yüi  mazdayasna  'ob  (IS.)  ayantim (sd.)  vä  taantim  vä  barimtum  vä  .  .  \. 6.  aÖ,  a)  'Standort,  Heimstätte':  ma  hl avi  'hm  ava.kisia  mä gätäm  nipa&.yanuha Yt/7.  57;  —  kqmHt  %wqmla  *drujimca airyabys  (statt  Neutr.)  'täsibys  janUni  Yt.
18636:Pü.;  9  pai;  5  päl  yäi.  —  i)  Nüral,  des  Rei- nigungsraumt ;  vgl.  in  der  Tafel  bei  DsT.  ZA. 3.  163  die  mit  'pieires'  bezeichneten  ausge- füllten Kreise.  Zwischen  dem  ersten  Loch für  ßindsnrin  und  der  Nordseite,  zwiscUen dem  dritten  Loch  für  Wasser  und  der  Süd- seite des  ganzen  Raums,  sowie  twischen  dem sechsten  Loch  für  Rindsnrin  und  dem  ersten für  Wasser  ist  ein  Abstand  von  je  drei  Schritt- (tva.  neun  Fuss)längeni  s.  V.  g.  ö  ff.
19534:*)  Ein  nach  aussen  durch  dcei  parallele  Furcb- itriche  abgegrenztes  Rechteck  auf  dem  Bodeo, Von  6  zu  16  Schritt,  auf  der  langen  Mittellinie drei  Löcher  mit  Wasser  und  sechs  mit  Rinder- bam  enthaltend.  Der  Raum  ist  zunächst  in iwei  wieder  mit  je  drei  Furchstrichen  umzogene Abteilungen  getchiedeo,  eine  kleinere  mit  den Wasser-  und  eine  grössere  mit  den  Hamlöchern. In  der  letitem  Abteilung  ist  abermals  durch drei  Furcbstiiche  an  der  den  Wasserlöchern abgekehrten  Seite  eine  Unterabteilung  mit  drei Löchern  geschaffen.  Die  Furch  st  riebe  werden  zu je  dreien  gezogen  der  Reibe  nach  l)um  die  Unter' abteilung,  3)  um  die  grössere  Abteilung,  3]  um beide  Abteilungen,  4}  um  die  kleinere  Abteilung ; Tgl.  zu  antariiür.  Dann  werden  an  bestimmten Stellen  des  Raums  Steine  od.  dgl.  niedergelegt. Vgl.Sp.  10450.  und  dieZeichnungenbeiWESTSBE. /1J.43S  und  DsT.ZA.2.  l6z  (dessen  Erliulerungen aber  nicht  stimmen).  Abweichend  Sp.  Übers,  i, Tafel  Zur  Reinigungszeremonie  s.West  aO.431. Ableit.  aut  'BiaYo-(mit  Verschiebung  des  Wort- akzents?]!),  etwa  'Raum  mit  den  Lochern'. — Pü. :  msej.  —  ■)  D.  i.  er  soll  von  der  grossem Abteilung  (PüErL  pa  gömH)  in  die  kleinere gehen.  —  *)  Ob  etwa  miy"  zu  lesen?
24350:•  j.  visata.gäya-  n.  'I^ngenausdehnung von  zwanzig  Schritten,  zwanzig  Schritt- längen': aal  tarn  .  .  apa.barsis  .  .  'giiim haca  S^rat  V.  77.  4.
== gamo.b
```


## [2026-09-06T14:59:41.097Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gäm[a-zöäü3]*\\.b\\|gam[a-z3]*\\.b\\|gSm\" BRT.txt | head -12"
}
```


### [2026-09-06T14:59:41.146Z] TOOL RESULT

```
9010:yata.  -\^a  gSmqn  hauiayatai  ya^a  nava.- pdojiii  ",  .  'wie  so;  drei  Schrittlängen?' 'Die  (drei)  Schritte  müssen  aneinander gelegt  werden.'  'Was  heisst  das:  die Schritte  .  .?'  'Neun  Fusslängen.'"  V. /y.  g;
10855:•  j.,  g.  xSi-  f  'Not,  Elend':  x^3  (GS.)''> dangSm  ayU  (sd.)  Umanhö  Y.31.20;  — paiiistaße  xsayasca  (GS.)''  amayavay&sla Y.7/.  17;  —  xUm^'>  F.J.
12207:•  j-i  g-  t^mah-  n.  i)  'Finsternis,  Dunkel', Sing,  und  Plur.:  ks  kvSpä  raochslä  (sd.) dät  'mhs<ä  Y.  44.5; — ydisra  nSit  xsapa nSii  °ma  Yt  10.50;  —  dartgSm  3ys(sd.) 'matjAs  Y.JJ.30;  —  mihr^m  ..'manbääa^^ Jiyäurum  ". .  den  im  Dunkel"  wachsamen" Yt  io.  141;  —  'mauAqm  vä  *aiwi^ati (sd.)  V. A4;  —  paitiltJOe  'maakqm  Y.
12880:—  ')  S  411-  3  d. •  p.  darga-,  g.  daraga-,  j.  dar«}-a-  Adj. (fem.  °7J-)  'lang';  i)  räumlich:  Ufa  tarn car^am  yqm  'yqm  YtJp.  77;  5.50;  — mi^rtm  . .  yeAha  'yäat  bäeava  .  .  Yt.  10. 104.  z)  zeitlich:  M<?i«(sd.)  tat  äs  nsit 'y?m  Yt.5. 65;  —  "iimal  aipi  zrvätum Y.62.3,\tig.a6;  13.53;  —  °f^^  ^yo (sd.)  t^mattks  Y.31. 20;  —  'yayäsca  paiti danyjjltdis  YL  /y.  1 3  j ;  Y.68.11;  —  tsm (nämL  kämtm)  msi  data  'gahys  *yaos{^^^ vairyS  stSis  Y.  43.  13;  —  hyatcä  -gSm *Jr3gvö.d»dyS  rasö  {sd.)  Y.jo.ii; — ptn- fum/a  (sd.)  barjsma  starane  °y?mca  yasram ..yaaJnS'Vt.iO.iiSi—ya^a  Sicä  *aiivi- iayama  'ya  amiiayana  . .  hr^yrnya^^aSum (sd.)  Yt  70.  7  7 ;  —  °gäi  Tsyai  bfzvait!  hax- maim  (sd.)  Y.  40.  3;  —  'yai  hax^räi  Vt 10.  T),  17.6;  — fravaiayS . .  hulhaxmanS . .  'yaa'fyj  Aax^oralifyff  Vt  13.  30;  —  'y^m Aaxma  V.  60.  j;  —  dättm  tS tanuye  :^ar»nB ' urvnaläi  •y?m  havanfum  (sd.)  Yt77.  22; F.^b;  —  urunaica  'ye  havanhe  A.  i.ii; —  'yäi  AaosravaAAsi  .  .  -yai  AavafiAäi Vjtjs;  —  a  'yät  ^ä.bairyilt  (sd.)  Y. öo.  6;  —  'yqfi  upayanayä  (Stverz.)  Y, /.  13  usw.;  —  'ya  (APn.)  data  .  .  sara- >uäraAe  T.  ^6  {?);  —  iaia  tl  'yim  ävSya (sd.)  aakal  H.2. 34;  16.  a)  Adj.  an Stelle  unsres  Adv.'':  :^afsa  'yd  tna^äka "schlaf  lang,  o  Mensch"  V.  rÄ  16;  — earäiti  .  .  yä  'ya  apu%ra  aHti  V.  3.  34; 34.  b)  ASn.  als  Adv.:  H  utä,  'gam  jlvä
13188:noch  ai/arfrt  VytjfjjSp.gSm.        [P.5:  lies
14635:•  j,  *ri-pi9Twa-  Adj.  'der  drei  Mahl- zeiten bekommt':  *'w5  *al  asti  ätarl ahurahe  ma^äa  hama  bipi^ws  aiwigSme
18541:•  ).,  g.,  p.  naplt-:ffa//-  m.,  j.  naptar-: nafsir-  m.",  j.  naptl-  f.  'Enkel;  Enkelin': '  adam  d3ray^v(^ui . .  vistäspahya  puh^e^ arSätnakyä  '/J(NS.)'*  Eh.  j.  i;  —  'pS (NS.)"  ..  ■■//("  (NSf.)  i/a  V./2.11;  10;  — nyaka  haca  'ptöisSs,  (^\%y^  nyske  haca  'pti (statt  AblSf.)  V.  J2. 1 1 ;  —  hyai  us  alä napiyaisii  na/i'uCLP.yVä ..uzp//  (Sp.4gSm.)  ' fryänakya  aojyaiiü  '^.46.12.  a)  mit GP.  apam''  'Enkel  derWasser',  Name  einer Gottheit**;  a  dim  (näml.  3^ar)nö)  Hahra kangturvayat  apum  'ph  (NS.)  aun'at.aspö Yt.  rp.  s  1 ;  5 '".  '.7-  95^';  —  «/>?'»  >'»  (NS.) t&  ups  ,  .  aiiuhe  .  .  vi.baxsaiti  Yt  8.  34; —  b^ntantfm  ahuntn  xsa^rlm  xSaltitn apqm  'pättm  aurvat.asp?m  .  .  yB  upäpB yazatS  Yt  ig.  51 ;  Y.  2,  5;  —  apqm  'ptär?m yasamaide  nairJm  sanh^m  Y.  7/.  23;  — b»->sat3  ahurake  'fiorS  aPqm  apasca  maida- la/aya  Y.  r.  5;  —  b^ryza  a/iura  xsa^rya apqm  V»?(VS.)Y.6'5.ia.  _  a)Nameeiner jener  Gottheit  geweihten  Örtlichkeit*'  (oder eines  Husses,  einer  Quelle,  eines  Berges): tarn  (näml.  andriin)  yaznäa  . .  sSyuidrSis pu%ra  upa  b3r?zant?m  ahur>m  xsairim xsaWm  apqm  'paism  Ylj.  73.  [na/jonm Y. ij.ii:  s.  x/alirB.napiar-.\
20847:I  et  (eum)  qui  (est)  faciendi  et  dicendi" I  Y.  33. 14;  —  *grSkms . .  atikSus  maraxtärB I  (sd.)  ahya  \yai(a  ^'Grlhmas  . .  et  (ii)  qui (sunt) ..  destructores"  Y.J2. 13; —  ku%ra töi  andrS  (sd.)  .  .  yöi  .  ,  caxrays  "num tibi  (sunt)  fidi  (ü)  qui  . ,"  Y.^4.7;  — kada  .  .  yOi  uxiäiiS  ainqm  .  .  frärmtl "quando  . .  (ii)  qui  (sunt)  tauri  .  ."  Y.  4G. 3;  —  naldä  dahySus  \ydi  iastSrS  drjsvatas "neque  (ii)  qui  (sunt)  . .  imperatores"  Y. 4O.  I ;  —  tat  ..  uitanai  data  . .  ySi  sl gSus  v^nzinl  (sd.)  azyi  ".  .  vitae  (eorum) qui  .  ."  Y.  34.  14;  —  tim  at  yasna- nqm  paurvataia  yazamaidl  ySi  ..  iyeintJ ".  .  imprecationum  .  .  (eorum)  qui  .  ." ^•37-  2;  —  yi  varpsaiil  (sd.)  kyat vasnä  firasöJ^mim  "qui  . .  fecerit  . .  (id) quod  (est)  .  ."  "^.46.  19;  —  hyatcS dar>gSm  dr)gvll.d»byS  rasB  savai'a  alavabyö "et  (id)  quod  (est)  . .  damnum  et  lucra  . ." Y._jo.  11;  —  Aaihyavanitqm  {%A.)  hyat vasna  f?rasS.t}m}m  "verificationem  (eius) quod.."  Y. 50.11;  —  ai  zt  töi  vaxsya .. hyai  aksyä  (NSf.;  sd.)  dngvaiii  wörtlich ",.  von  dem,  was  die  Androhung  ist,,"  Y, 51.  8;  —  hyat  "qsasutä  (sd.)  yä  (NPn.) daiiiiana  (sd.)  fraoxta  "..  (ea)  quae  (sunt) . .  enuntiata"  Y.  48.  1 ;  —  das  Relativ  kon- gruirt  mit  dem  Praedikat:  vldvä  yalclt güzra  (sd.)  singhanhS  (wörtlich)  "kennend auch  (das),  was  die  geheimen  Lehren  (sind)" Y.4<V,3;  —  anais  a  vT.nSnasa  ya  (NSt) iarapsjis{ad.}cä  kjvltäscä  Y._J2.  15;  — *m>ndäiäyai  (sd.)  ya  (NSf)  toi  adisHi Y.44.8;  5,^.13;  —  nipatihw . .  tumas^a ya  armaitiH&d.)  Tiilcä  Y.4g.  10;  —  yS va  mSi  \yh  (NPf)  gasha  dasdi  (Sp. 7 1 S  u.)  *asnatihe  wörtlich  ". .  (das),  was meine  Besitztümer  (sind)  .  ."  Y,  46. 8;  — vtayUta  yä  (NPn.)  mrqi  sädra  drtgvats (wörtlich)  "immer  (wird  sein)  was  die Qualen  (sind)  .  ."   Y.45.  7;  43-5,  49-6;
22249:1. 1;  —  maiamya  vaca  frasrävayamnahe N,  20;  *26,  26,  33;  —  nitima  vaca  gäiiä srävayH  N.  27;  —  mt^rsm  ..yeiihe  vSxS gfmänahe  .  .  vi  Äafta  karhiqn  /asaiti yatcit  mmartka  vsHm  iaraiti  {Sp.  ^^sf.) yai  gaoi(sA.)ät  Yt/0.85;  73;  —  tmrr/S yS  parSäars  .  .  ä%rS  vScim  sururtaeiti FrW.  10.  41 ;  —  b»r3Z>m  barSi  zaota  välim Yt.  17. 61;  Y.  70.4,  Yt5. 123;  —  yat  bä faiti . .  näirikaca  apinnSyükasca .  .Janilm baraiti  väcim  V.J.  11;  —  yS  mq'hrä  (sd.) *vacim'''  ..  baraiti  V.  50.  6;  —  a^rä *väcim'''  baraitj  mihaAvacä  vä  *»n{.- vaeä  (sd.)  vä  Y.31.J2;  —  yeriAe /räyB (sd.)  sbaymtam  sraistfm  susruye  väHm Yt  i7. 1 7 ;  — *GS.  mit  avaifat-  (sd.)  '(Wehe- tum  der  Rede  sva.)  Weherufen':  daragSm äyü  (sd.)  timatfhs  äus^ar»^Sm  (sd.)  avaSäs (sd.)  vacö{G%.)  Y.J7.  ao.  a)  'Gesang' beim  Gottesdienst:  eis  saotarsi&d.)  kairim
23321:—  s.  noch  ^manah-  Ia  (Sp.  1128)'*  und mainyav-l  I  a  (Sp.  ir36  o,)'J.  b)  von Gottheiten:  *äat  iha yazamaidi  '»»Aaica  it 'tsuhiscä  It  spptüSng  am>sSng  Y.j'p.  3;  — 'nuhj  (ISf,)  ada  gaidi  mni  a  mBi  arapä (sd.)  Y.  49. 1 ;  —  upa.ßmsn  (sd.)  haurvata am»r»tat3  'nh3us*mainySus{%^.  ii37u.)'* iyaohanai!  Y.  45-51  —  as'jm  .  .  vahistfm .  .  'hucä  xla%rmt  (Sp.  545  m.)  Y.J7.  4  f.; 35. 10;  —  bes.  mit  ^manah-  (Stverz.,  Sp, ii39ff)*>:  kasi!  'kB  (als  Vok.)  mananha yS..Y.  2g.  7 ;  usw.  b)  im  j  Awr.  (unvoll- ständig); a)  von  Sachen;  die  göttlich  ver- ehrten Begriffe  sind,  soweit  sie  nicht  aus- gesprochen personlich  gedacht  erscheinen, hier  mit  aufgeführt:  '»»uAi  datna  (Stverz., Sp.  664  m-,  u.)  masdayasnil  Yt.  13.  94; usw.;  —  nstim  (Stverz.,  Sp.sgSm.)  'nuhim Vr.  4- 1 ;  usw.;  —  dahmam  'auhim  afritlm (Stverz-,  Sp.  330  u.)  Y.  7.  36;  P.^2  ('w*!), 33  ('aklm);  usw.;  —  "^r^S^  (sd.)  -aht^i *rasqstatS (sd.)  'f»kuyä  Y.i.i^;  —  saoiqm (Stverz.)  'tiuAlm  S.Z. 3;  usw.;  —  ratayä (Stverz,)  'nhuya  S.  /.  5;  usw.;  —  dahmaya •tihtya  anOäruxtBis  (sd.)  Y.  70. 3 ;  —  AauÜa
23550:•  j.,  g.  västra-  n.  'Weide';  i)  'was  das Vieh  weidet,  Gras,  Futter':  pars  *wmS  .. *da>ihsui  aaÄaj  dfrptj(sd.)  *r>m  V.2. 34; —  gSmia  "roAeca  YLjj.  100',  ig.  SA;  — I  Hat  .  .  ahe  nmänake  frapObwS  gaui  .  . \frapiiiwS  'nm  V.J.  3;  — gavsi  .  .  fral^- yamaht  räma^  °r?tncä  dazdyai  (sd.)  Y, J5.  4;  —  ahurahyi ..yasramila  vahm^mlä .  .  gsulca  'rsm  Y.JJ.  7;  —  gavSi  .  .  hyat htm  data  .  .  hads  'rS  gaodaya  %waxilT (sd.)  Y.  2g.  3;  —  'r>m  btnttm  (sd.)  gtrue ..gaodäyüm  nanm  Vr.z,  11;  —  :^ar>h»mca naire  .  .  'nmca  gave  huhhnhe  V.5.30;  — ■ \yavö  mi  maiys  ^arat  'rym  gave  Au^anhe I  V.5.30; —  yavaca  'raca  V.7.32;  —  yat !  bä  paiti  fraiit>m  kärayätt  .  .  yavanamca '  'ranqm(als  Obj.)/a  urvaranqmca  i^arihs.- bairyanqm  ".  .  Getreide  und  Gräser '  lind  Pflanzen  mit  essbaren  Früchten" iV.  J.  4;  g.  53;  —  as.danunqm(sd.)ca ,yavariqm  kasu.dänunqmca  °nanqm  Yt  S. \  39.  2)    'wo  das  Vieh  weidet,  Weide-
25269:•  g.  raäah-  n.  'Schädigung,  Schaden',  ins- bes.  der  im  andern  Leben":  ^itica  smits (Sp.  367  m.)  Ayalca  dar?gSm  *drs^-6jbbyi 'Is  savaUa  aiavabyS  "..  der  lange  Schaden für  die  Z>n/^enossen  und  der  Nutzen  für die  v^/aanhänger"  Y.  ^o.  11.
```


## [2026-09-06T14:59:48.933Z] TOOL CALL #61: Bash

```json
{
 "command": "sed -n 1,60p tools/fetch_source.py"
}
```


### [2026-09-06T14:59:48.973Z] TOOL RESULT

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


## [2026-09-06T14:59:56.306Z] TOOL CALL #62: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/زیان\" \"https://en.wiktionary.org/wiki/گاییدن\" \"https://www.etymonline.com/word/quench\" \"https://en.wiktionary.org/wiki/إبليس\"; do echo \"=== $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 206 verification (Gweie/Gwel 1)\"; done"
}
```


### [2026-09-06T15:00:00.944Z] TOOL RESULT

```
=== https://en.wiktionary.org/wiki/زیان
/home/sfmqrb/git/rishe/data/verification/sources/web/19230cc974bcb408.txt
=== https://en.wiktionary.org/wiki/گاییدن
/home/sfmqrb/git/rishe/data/verification/sources/web/e1261805427bca6c.txt
=== https://www.etymonline.com/word/quench
/home/sfmqrb/git/rishe/data/verification/sources/web/902c58b364c0a1e0.txt
=== https://en.wiktionary.org/wiki/إبليس
/home/sfmqrb/git/rishe/data/verification/sources/web/fae0b0c77ff5b813.txt
```


## [2026-09-06T15:00:03.694Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== ziyan\"; grep -n -A15 \"^Persian\" 19230cc974bcb408.txt | head -50"
}
```


### [2026-09-06T15:00:03.742Z] TOOL RESULT

```
=== ziyan
```


## [2026-09-06T15:00:04.373Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== gayidan\"; grep -n -i -m3 -A20 \"Etymology\" e1261805427bca6c.txt | head -60"
}
```


### [2026-09-06T15:00:04.420Z] TOOL RESULT

```
=== gayidan
```


## [2026-09-06T15:00:06.783Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c 19230cc974bcb408.txt e1261805427bca6c.txt 902c58b364c0a1e0.txt fae0b0c77ff5b813.txt; head -30 19230cc974bcb408.txt"
}
```


### [2026-09-06T15:00:06.844Z] TOOL RESULT

```
 9423 19230cc974bcb408.txt
 2039 e1261805427bca6c.txt
 5724 902c58b364c0a1e0.txt
 5082 fae0b0c77ff5b813.txt
22268 total
URL: https://en.wiktionary.org/wiki/زیان
FETCHED: 2026-09-06T14:59:58Z
STATUS: 200
TITLE: زیان - Wiktionary, the free dictionary

زیان - Wiktionary, the free dictionary 

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
```


## [2026-09-06T15:00:09.103Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '60,200p' 19230cc974bcb408.txt | grep -v \"^\\s*$\" | head -60"
}
```


### [2026-09-06T15:00:11.012Z] TOOL RESULT

```
 1.1 
 Alternative forms 
 1.2 
 Etymology 
 1.3 
 Noun 
 1.3.1 
 Derived terms 
 1.3.2 
 Descendants 
 1.4 
 Further reading 
 2 
 Persian 
 Toggle Persian subsection 
 2.1 
 Etymology 
 2.2 
 Pronunciation 
 2.3 
 Noun 
 2.3.1 
 Descendants 
 2.4 
 Further reading 
 3 
 Urdu 
 Toggle Urdu subsection 
 3.1 
 Etymology 
 3.2 
 Noun 
 Toggle the table of contents 
 زیان 
 8 languages 
 বাংলা 
 فارسی 
 Bahasa Indonesia 
 Kurdî 
 Malagasy 
 Русский 
 سرائیکی 
 Türkçe 
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
```


## [2026-09-06T15:00:13.298Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk 'NR>200' 19230cc974bcb408.txt | grep -v \"^\\s*$\" | head -60"
}
```


### [2026-09-06T15:00:15.013Z] TOOL RESULT

```
C – Uzakda bulunan düşmana fazla ziyan vermek ve anı bir an evvel muharebeye Türk'e mecbur ettirmek için yapılmış bir silahdır. (please add an English translation of this quotation) 
 loss , the result of no longer possessing an object , function , or characteristic 
 Synonyms: خسارت ( hasaret ) , ضرر ( zarar ) , غائب ( gayıb ) 
 Derived terms
 [ edit ] 
 زیان ویرمك ( ziyan virmek , “ to cause injury ” ) 
 زیان چكمك ( ziyan çekmek , “ to suffer loss ” ) 
 زیانجی ( ziyancı , “ damager ” ) 
 زیانسز ( ziyansız , “ harmless ” ) 
 زیانكار ( ziyankâr , “ harmful, mischievous ” ) 
 زیانلو ( ziyanlı , “ noxious, mischievous ” ) 
 Descendants
 [ edit ] 
 Turkish: ziyan 
 → Armenian: զիյան ( ziyan ) 
 → Bulgarian: зян ( zjan ) 
 → Macedonian: зијан ( zijan ) 
 → Serbo-Croatian: zìjān / зѝја̄н 
 Further reading
 [ edit ] 
 Çağbayır, Yaşar ( 2007 ), “ ziyan ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 5492 
 Devellioğlu, Ferit ( 1962 ), “ziyân”, in Osmanlıca-Türkçe Ansiklopedik Lûgat ‎ [ Ottoman–Turkish Encyclopedic Dictionary ]‎ [2] (in Turkish), Istanbul: Türk Dil Kurumu, page 1432 
 Kélékian, Diran ( 1911 ), “ زیان ”, in Dictionnaire turc-français ‎ [3] (in French), Constantinople: Mihran, page 652 
 Meninski, Franciszek à Mesgnien ( 1687 ), “Damnum”, in Complementum thesauri linguarum orientalium, seu onomasticum latino-turcico-arabico-persicum, simul idem index verborum lexici turcico-arabico-persici, quod latinâ, germanicâ, aliarumque linguarum adjectâ nomenclatione nuper in lucem editum ‎ [4] , Vienna, column 320 
 Meninski, Franciszek à Mesgnien ( 1680 ), “ زیان ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [5] , Vienna, column 2495 
 Nişanyan, Sevan ( 2002– ), “ ziyan ”, in Nişanyan Sözlük 
 Redhouse, James W. ( 1890 ), “ زیان ”, in A Turkish and English Lexicon ‎ [6] , Constantinople: A. H. Boyajian, page 1021 
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 From Middle Persian [Book Pahlavi needed] ( zydʾn' /⁠zyān⁠/ , “ loss, harm, damage ” ) , from Proto-Indo-Iranian . Cognate with Parthian 𐫉𐫏𐫀𐫗 ( zyʾn /⁠zyān⁠/ , “ loss, harm, damage, destruction ” ) , Avestan 𐬰𐬌𐬌𐬁𐬥𐬁 ( ziiānā , “ damage ” ) , Sanskrit ज्यान ( jyāna , “ oppression ” ) , as well as the Iranian borrowings: Old Armenian զեան ( zean ) , Jewish Babylonian Aramaic [script needed] ( zīyanā ) , Classical Mandaic ࡆࡀࡉࡉࡍࡀ ( zāyinā ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /zi.ˈjaːn/ 
 ( Dari, formal ) IPA ( key ) : [zi.jɑ́ːn] 
 ( Dari, formal ) IPA ( key ) : [zi.jɑ́ːn] 
 ( Kabuli ) IPA ( key ) : [zi.jɑ́ːn] 
 ( Hazaragi ) IPA ( key ) : [zi.jɔ́ːn] 
 ( Iran, formal ) IPA ( key ) : [zi.jɒ́ːn] 
 ( Tajik, formal ) IPA ( key ) : [zi.jɔ́n] 
 Rhymes: -aːn 
 Readings
 Classical reading ? 
 ziyān
 Dari reading ? 
 ziyān
 Iranian reading ? 
 ziyân
 Tajik reading ? 
 ziyon
 Noun
 [ edit ] 
 زیان • ( ziyān / ziyân ) ( Tajik spelling зиён ) 
 damage , detriment , injury , loss 
 Synonym: ضرر ( zarar ) 
 Antonyms: سود ( sud ) , فایده ( fâyede ) 
 Descendants
 [ edit ] 
 → Baluchi: زیان ( zyan )
```


## [2026-09-06T15:00:21.001Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== gayidan file\"; cat e1261805427bca6c.txt | head -25; echo; echo \"== quench\"; awk 'NR>20' 902c58b364c0a1e0.txt | grep -v \"^\\s*$\" | head -30"
}
```


### [2026-09-06T15:00:22.528Z] TOOL RESULT

```
== gayidan file
URL: https://en.wiktionary.org/wiki/گاییدن
FETCHED: 2026-09-06T14:59:58Z
STATUS: 200
TITLE: گاییدن - Wiktionary, the free dictionary

گاییدن - Wiktionary, the free dictionary 

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

== quench
 Origin and history of quench 
 quench (v.) 
 Middle English quenchen , "to extinguish, put out" (heat, light, fire, also of desire, hunger, thirst), also figurative, "to bring to naught, eliminate, render ineffectual" (c. 1200), Old English acwencan "to quench" (of fire, light), from Proto-Germanic *kwenkjanan , probably a causative form from the source of Old English cwincan "to go out, be extinguished," Old Frisian kwinka .
 No certain cognates outside Germanic; perhaps a substratum word. Especially "to cool or extinguish by means of cold water," hence "to drench in water" (late 15c.). Related: Quenched ; quenching .
 also from c. 1200 
 Entries linking to quench 
 quelch (v.) 
 1650s, a shortening of squelch , perhaps influenced by quench . Related: Quelched ; quelching .
 unquenchable (adj.) 
 late 14c. of fire, "inextinguishable," also figurative; 1560s of thirst; from un- (1) "not" + quench (v.) + -able . Related: Unquenchably . Unquenched "unextinguished" is from late 12c.
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 quell 
 Middle English quellen "to kill" (a person or animal), from Old English cwellan "to kill, cause to die; murder, execute," from Proto-Germanic *kwaljanan (source also of Old English cwelan "to die," cwalu "violent death;" Old Saxon quellian "to torture, kill;" Old Norse kvelja "to
 slake 
 Middle English slaken, from late Old English sleacian, slacian "become slack or remiss; relax an effort" (intransitive); "delay, retard" (transitive), from slæc "lax" (see slack (adj.), and compare Middle Dutch, Middle Low German slaken). The transitive sense of "make slack, loos
 allay 
 "put down, quiet, assuage, pacify," Middle English alegen, from Old English alecgan "to put, place, put down; remit, give up, suppress, abolish; diminish, lessen," from a- "down, aside" (see a- (1)) + lecgan "to lay" (see lay (v.)). A common Germanic compound (cognates: Gothic us
 marasmus 
 wasting away of the body," 1650s, Modern Latin, from Greek marasmos "a wasting away, withering, decay," from marainein "to quench...
 repel 
 early 15c., "to drive away, remove, quench" (a sense now obsolete), from Old French repeller and directly from Latin repellere...
 asbestos 
 Greek asbestos, literally "inextinguishable," from a- "not" (see a- (3)) + sbestos, verbal adjective from sbennynai "to quench...," from PIE root *(s)gwes- "to quench, extinguish" (source also of Lithuanian gesti "to go out," Old Church Slavonic gaso...
 amaranth 
 literally "unfading, undecaying," from a- "not" (see a- (3)) + stem of marainein "die away, waste away, decay, wither; quench...
 satisfy 
 early 15c., satisfien, "do penance," also "appease, assuage;" also "fulfill (a desire), comply with (a command), satiate (a hunger or thirst)," from Old French satisfiier "pay, repay, make reparation" (14c., Modern French satisfaire), from Latin satisfacere "discharge fully, comp
 put-out 
 "offended, angry, upset," by 1887, from the verbal phrase in the sense of "offend," attested by 1822; see put (v.) + out (adv.). Perhaps via the earlier sense of "cause to lose self-possession, disconcert" (1580s). The verbal phrase is from mid-14c. as "drive out, banish, exile;"
```


## [2026-09-06T15:00:37.471Z] TOOL CALL #69: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/parliament\" \"https://www.etymonline.com/word/ballet\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7elH-\" \"https://en.wiktionary.org/wiki/%CE%B2%CE%AC%CE%BB%CE%BB%CF%89\"; do echo \"=== $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 206 verification (Gwel 1: ballein, parliament, ballet)\"; done"
}
```


### [2026-09-06T15:00:41.278Z] TOOL RESULT

```
=== https://www.etymonline.com/word/parliament
/home/sfmqrb/git/rishe/data/verification/sources/web/f70a5a05955383a6.txt
=== https://www.etymonline.com/word/ballet
/home/sfmqrb/git/rishe/data/verification/sources/web/0bed7e376c793b93.txt
=== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7elH-
/home/sfmqrb/git/rishe/data/verification/sources/web/5e8cbbe748096099.txt
=== https://en.wiktionary.org/wiki/%CE%B2%CE%AC%CE%BB%CE%BB%CF%89
/home/sfmqrb/git/rishe/data/verification/sources/web/2b2b2d5a7eec1b6e.txt
```


## [2026-09-06T15:00:44.912Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== parliament\"; awk 'NR>20' f70a5a05955383a6.txt|grep -v \"^\\s*$\"|head -8; echo; echo \"== ballet\"; awk 'NR>20' 0bed7e376c793b93.txt|grep -v \"^\\s*$\"|head -8; echo; echo \"== gwelH\"; grep -n -i -m1 -A12 \"Root\" 5e8cbbe748096099.txt | head -30"
}
```


### [2026-09-06T15:00:47.015Z] TOOL RESULT

```
== parliament
 Origin and history of parliament 
 parliament (n.) 
 c. 1300, parlement , "consultation; formal conference, assembly," from Old French parlement (11c.), originally "a speaking, talk," from parler "to speak" (see parley (n.)); the spelling was altered c. 1400 to conform with Medieval Latin parliamentum .
 Anglo-Latin parliamentum is attested from early 13c. The specific sense of "representative assembly of England or Ireland" (with capital P- ) emerged by mid-14c. from the broader meaning "a conference of the secular and/or ecclesiastical aristocracy summoned by a monarch."
 also from c. 1300 
 Entries linking to parliament 
 parley (n.) 
 "conference, conversation, speech," especially with an enemy, mid-15c., parlai , from Old French parlée , from fem. past participle of Old French parler "to speak" (11c.), from Vulgar Latin *paraulare , from Late Latin parabolare "to speak (in parables)," from parabola "speech, discourse," from Latin parabola "comparison" (see parable ).

== ballet
 Origin and history of ballet 
 ballet (n.) 
 "theatrical, costumed dance and pantomime performance telling a story and representing characters and passions by gestures and groupings," 1660s, from French ballette from Italian balletto , diminutive of ballo "a dance," from Late Latin ballare "to dance," from Greek ballizein "to dance, jump about" (see ball (n.2)).
 also from 1660s 
 Entries linking to ballet 
 ball (n.2) 
 "dancing party, social assembly for dancing," 1630s, from French, from Old French baller "to dance," from Late Latin ballare "to dance," from Greek ballizein "to dance, jump about," literally "to throw one's body" (ancient Greek dancing being highly athletic), from PIE root *gwele- "to throw, reach." The extended meaning "very enjoyable time" is American English slang from 1945, perhaps 1930s in African-American vernacular.
 balletomane (n.) 

== gwelH
62: Root 
63-
64- 1.1.1 
65- Reconstruction notes 
66-
67- 1.1.2 
68- Derived terms 
69-
70- 1.2
```


## [2026-09-06T15:00:49.236Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk 'NR>120' 5e8cbbe748096099.txt | grep -v \"^\\s*$\" | head -40"
}
```


### [2026-09-06T15:00:50.849Z] TOOL RESULT

```
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
 A user suggests that this Proto-Indo-European reconstruction entry be moved, merged or split.
 Please see the discussion on Requests for moves, mergers and splits ( + ) for more information and remove this template after the request has been fulfilled.
 *gʷelH- [ 1 ] [ 2 ] 
 to throw , reach , pierce ; to hit by throwing
 Reconstruction notes
 [ edit ] 
 On the basis of Celtic nasal-infix present *balnīti and several Greek derived terms like βέλεμνον ( bélemnon , “ javelin, dart ” ) the laryngeal may be reconstructed as *h₁ .
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *gʷelH- (101 c, 0 e) 
 *gʷelH-éti ( root present ) 
 Armenian:
 Old Armenian: կեղ ( keł , “ wound, sore, ulcer ” ) , կեղեմ ( kełem , “ to torment, torture, afflict ” ) , ( possibly ) կեղերջ ( kełerǰ , “ complaint, grievance, pain ” ) 
 Proto-Indo-Iranian: *gráHti 
 Proto-Iranian: *gráHti 
 Avestan: 𐬥𐬌-𐬖𐬭𐬁𐬌𐬭𐬈 ( ni-γrā i re , “ to throw down ” ) 
 Pashto: غوزارول ( γwəzārawə́l , “ throw, cause to fall, knock over ” ) 
 Persian: گرزین ( gerzin , “ arrow ” ) 
 Balto-Slavic:
 Latvian: dzel̂t ( “ to sting ” ) 
 Lithuanian: gélti ( “ to hurt severely ” ) 
 Proto-Germanic: *kwelaną ( see there for further descendants )
 *gʷl̥-né-h₁-ti ~ *gʷl̥-n-h₁-énti ( nasal infix present ) 
 Proto-Celtic: *balnīti ( “ to die ” ) ( see there for further descendants )
 *gʷelHtlom or *gʷelHdʰlom
```


## [2026-09-06T15:00:58.753Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -A6 \"Etymology\" fae0b0c77ff5b813.txt | grep -v \"^\\s*$\" | head -30"
}
```


### [2026-09-06T15:01:00.676Z] TOOL RESULT

```
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
--
157: Etymology
158- [ edit ] 
159-
160- Not attested before the Qurʾān . Theorised to come from Ancient Greek διάβολος ( diábolos , “ devil , accuser , slanderer ” ) . Alternatively, it has been maintained to originate from the trilateral root ب ل س ( b l s ) with the meaning of "despairing [of God's mercy] or confounded [and unable to see the right course]" from the verb أَبْلَسَ ( ʔablasa ) . This would, however, require the trilateral root to take the form if'īl which, excepting إحليل , is usually associated with words of non-Arabic origin ( see: إدريس , إكليل , إنجيل , إبريز , and إبريق ).
161-
162- Pronunciation
163- [ edit ]
```


## [2026-09-06T15:01:28.654Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN quench/ballad/ball2\"; grep -n \"^quench,\\|^ballad,\\|^ball,\\|^ballet,\" KLN_1966.txt | head; echo \"== SKT quench\"; grep -n -i \"^quench\\|Quench\" SKT.txt | head -5; echo \"== NYB gadan\"; grep -n \"gādan\\|g'tn\\|gāy-\" NYB_vol2_glossary.txt | head -5; echo \"== HRN 679\"; grep -n \"^ *679\\.\" HRN.txt | head -3"
}
```


### [2026-09-06T15:01:28.756Z] TOOL RESULT

```
== KLN quench/ballad/ball2
4325:ball,  n.,  a  round  body;  a  sphere.  —  ME.  bade, fr.  ON.  bbllr,  which  is  rel.  to  OHG.  hallo,  balla, MHG.  bade,  bal,  G.  Ball,  fr.  I.-E.  base  *bhel-, ‘to  swell’.  See  belly  and  cp.  Balaena,  bale, ‘bundle’,  baleen,  balinger,  balloon,  ballot,  bil¬ low,  bulk,  ‘size’,  and  the  first  element  in  bill- berry  and  in  pall-mall.
4327:ball,  n.,  a  party  for  social  dancing.  — -  F.  bal,  fr. OF.  bailer,  ‘to  dance’,  fr.  VL.  ballare,  fr.  Gk. ^xXXl^etv,  ‘to  dance’,  which  prob.  derives  fr. fWXXetv,  ‘to  throw’.  See  ballistic  and  cp.  ballad, ballerina,  ballet,  bayadere, ballad,  n.,  1)  a  sentimental  or  romantic  song;  2)  a narrative  song.  —  ME.  balade,  prop,  ‘a  song written  for  a  dance’,  fr.  OF.  balade  (F.  ballade), fr.  OProven?.  balada,  lit.  ‘dance’,  later  used  in the  sense  of  ‘dancing  song’,  fr.  balar,  ‘to  dance’. See  ball,  ‘party  for  dancing’, ballade,  n.  a  poem  with  three  stanzas  of  eight  or ten  lines  each  and  an  envoy  of  four.  —  F.  See prec.  word.
31371:quench,  tr.  v.,  to  extinguish.  —  ME.  quenchen,  fr. OE.  cwencan,  in  dcwencan,  ‘to  extinguish’,  caus¬ ative  of  cwincan,  ‘to  be  extinguished,  disappear’, rel.  to  OFris.  kwinka,  of  s.m.  Cp.  quelch. Derivatives:  quench,  n.,  quench-able,  adj., quench-er,  n.,  quench-less,  adj.,  quench-less-ly, adv.,  quench-less-ness,  n. quenelle,  n.,  a  ball  of  minced  chicken.  —  F.,  bor¬ rowed  fr.  G.  Knodel,  ‘dumpling’,  fr.  MHG. knodel,  dimin.  of  knode,  ‘knot’,  which  is  related to  E.  knot.  See  knot,  ‘bow,  tie'.
== SKT quench
1005:Asbestos,  a  mineral.  <Gk.)  Gk.  <{• <Tf^«TTOf,  unquenchable;  because  it  is  in- combustible, —  Gk.  (1-,  tirg.  prefix;  and •ff/Jiar^r,  quenchable.  from  a^iyyvfu,  i quench,  extinguish.
5205:distinct.  (K.-L.1  O.  F.  distintf.^'L. dif/inrtus,  distinguished ;  pp.  of dis/ittgvtre. extinguish.  (L.)  Coined,  with  suffix -»j^,  from  L.  exttiti^uerr,  better  gJcsftM^tfre {^^.extifiitus,^xs/ttu/uj).  loquench,  *  L.«ir, out;  stinpttrt*,  (o  firick,  aUo  10  extiii- guUb.     "D^r.  extimt  (from  pp  txtimtuiy.
15377:Quench.   (£ )     M.  E.  qmtmhm.    k,\
17448:slftke.  to  slacken,   quench,   wet.    (E.)
== NYB gadan
== HRN 679
5992:679. :iiyän 'Schaden'.
```


## [2026-09-06T15:01:33.184Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5990,6000p' HRN.txt; echo \"== leaf/page\"; awk 'NR<=5992{n+=gsub(/\\f/,\"\")} END{print \"leaf\",n,\"=> printed\",n-21}' HRN.txt; echo \"== SKT quench full\"; sed -n '15377,15381p' SKT.txt"
}
```


### [2026-09-06T15:01:34.980Z] TOOL RESULT

```
Und aw. zaras[ca (ZPGl.), das doch sicher 'Galle', gr.
X^^Vy ist?
679. :iiyän 'Schaden'.
aw. zyana- 'Schaden*; phlv. zi(y)an (talm. Nr"»T;
mand. Xi"»NT) ; skr. (Brähm.) jfydna- 'Bedrückung'.
LW. kurd. af/. ziyän; bei. ziyänl (307); oss. ziän,
d. ziän ; arm. zean,
680. zer 'unten, unterhalb*.
Käs. jir (Vullers jBr, Jerü), zer,
aw. haca + aöairi\ päz. az^r, vergl. phlv. er\tan 'mild',- 151 -
ertanih, erman(i)sn 'niedrigen Sinnes' (Men.) ^); ai. vergl.
== leaf/page
leaf 171 => printed 150
== SKT quench full
Quench.   (£ )     M.  E.  qmtmhm.    k,\
nveiuan^   to   extinguish;    causal  of  A<
npinean  (pt,  t.  rawiw),  to  go  oot,
tingui&hed.     Lengthened  lrv<m  A-  S.
(pt    t.  ru/Ju^.  to  go  oat,  be  cxtii)(^
```


## [2026-09-06T15:01:43.593Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"zyāna\\|zināt\\|gayad\\|jayati\" WLD_Bd1_pages.txt | head -12; echo \"== ballein/niγrāire\"; grep -n \"niγraire\\|nigraire\\|βάλλω\\|ballein\" WLD_Bd1_pages.txt | head -8"
}
```


### [2026-09-06T15:01:43.682Z] TOOL RESULT

```
20570:     t'bcr    ai.    upa-vajayati „faclit das Feuer an“ ('von Panini als Kaus. zu va-
27435:    Ai. urj-,       iirjti          f.,        urjd- m. „Saft             und Kraft, Nalnung", urjayati ,,nahrt,
30452:anord. rcekr ..verwerflich", rcekja (: ai. vrajayati ) „verwerfen, vertreiben"
== ballein/niγrāire
```


## [2026-09-06T15:01:53.001Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC gwel\"; grep -n \"g^ʷel\\|gu̯el\\|gwel\\|ballo\\|βάλλω\" IEC.txt | head -10; echo \"== IEC gwei\"; grep -n \"gu̯ei\\|gwei\" IEC.txt | head -10; echo \"== WLD band3 index\"; grep -n \"guei\\|gu̯ei\\|gu̯el\" WLD_band3.txt | head -10"
}
```


### [2026-09-06T15:01:53.079Z] TOOL RESULT

```
== IEC gwel
1101:bhal- (2) ‘forehead; prominence’. WP II, 175 Skt. cf. (a)bhalam (1) ‘forehead’; Gk. cf. pháios ‘forepiece on helmet? a component also of phál-agx ‘wedge-shaped frontal formation’, phalaris ‘coot; Alb. ballë ‘forehead, front of a formation’; Lat. fala *battering-ram', beside in-fula ‘headgear, garland on animal fore- head; W bâl, pl. baloedd (*bhalos, -es-) ‘peak, prominence’; ON bali 'grass-bank' ; OPr. ballo ‘forehead’. Cf. also the Gk. cpd. phal- akrós ‘bald’. Cf. bhàal- (2). The form re- presented in Lat. balaena seems to represent a non-Greek form of phálaina (‘whale’, lit. ‘hostile forehead’, cf. nuino- ‘hostile’ in Gk. ainós: Olr. anfine, s. ‘enemy’: OE unwine, id.). For OHG belihha ‘coot’, see FK: Belche
4644:gheleuos, gheluos *yellowish, green'. WP I, 624. Cf. ghel-, $&hel-, $hol- Lat. helvus ‘blonde’; Osc. (name) Heleviis ‘Helvius’; Gallo-Lat. gilvus 'flesh-coloured' beside galbinus ‘greenish’; Ligurian (?) sub- strate in Rumansh gelc, f. gelgua ‘yellow’, but also in gial, f. gialla; It. giallo, a, id.; W gwelw ('pale', w. induced -w-, cf. W gwawr, chwerw); OHG gelo, gs gelwes (yellow, and com. Gmc.); Li. cf. gelsvas ‘yellowish, pale, bay'
5282:guluos, ios (2) ‘container, vessel" Gk. cf. arú-ballos (^well-bucket,, fr. arúð “draw water"); Maced. gullás, f. ‘cup’ (isophonic Lat. in-glüvies “throat, crop’, with the vocalism of MHG kolc ‘eddy’, for which, however, cf. gulg-)
19299:tumolos (tumulos) 'swell, surge, lump, hump, hillock’. WP I, 708. Cf. tumó, tumos Skt. tumulah, m. ‘tumult; tumurab, tumalah, adj. (noisy; tümrah ‘swollen’; Vedic: ‘big, strong’; Oss. tímbil, Dig. tumbul, adj. ‘found’; Alb. cf. tumull-ac, adj. ‘chubby’; m. “bladder, balloon’; Lat. tumulus, gs: -i, m. ‘hillock’ beside tumultum, n. ‘tumult’; Ir. cf. tomhal- tach, adj. ‘gluttonous’; tomhlaim, v. ‘guzzle’; OE pumle, pl. ‘entrails’ beside (*-ü-) bymel, m. 'thumb-stall, thimble’; ON pumall, m. ‘thumb’; Cz. tmel, m. ‘putty’; Slovak cf. tmo- lit sa, inf. ‘tumble, frolic’; Li. tümulas, m. ‘Jump, mass, pother'. See next
19937:uel- (5) ‘see, look’. WP I, 293 Gk. cf. dé-elos, délos, adj. ‘clear’; ne-ní-élos, adj. “blind, foolish’; Lat. cf. vultus, gs: -üs, m. “face; image’; W gwel, m. ‘vision’; gwelaf, İsg. pres. ‘see’; Br. gwélann, 1sg. id. (inf: gwé- let, gwélut: W gweled); Sw. (long-gde) vála, v. "watch, wait beside välnas, refi. “look for- ward'
19938:uel- (6) “big, great; greater, stronger; be big, be strong, be able; greatly; strongly; very’. WP I, 285 & 294. Cf. ual- (2) (r-gde) Skt. cf. variyas, mfn. ‘broader’; Per. cf. bis ‘more’; Osc. cf. valaemo-, superl. "best": OBr. guell, Cor. W. gwell, adj. ‘better’; OE cf. we- lig, adj. ‘rich, prosperous, abundant, fertile, luxurious’; Du. welig, id.; LG welig “bright, gay, luxuriant’; Go. cf. ga-wiljis, adj. “willing, agreeable’; Scots walie, adj. ‘ample, large; jol- ly’; ON cf. vilgi, adv. “very, at al’; OCS velij, adj. ‘big’; OCz. velí, Srb. velji, id.; Li. vély, adv. ‘rather’. Compounding forms in Per. bali- *up- beside bali (“indeed, certainly, yes’: Li. vély “rather?); Ir. feile- ‘very’; Go. waila-, px. *well2; OE, Du. wel, wel- ‘very, fully’; OCS, Cz. Slovene vele-, px. "great" Verbal forms: Per. balidan, inf. ‘grow’; Tokh. A. cf. wäl, B
19947:walo ‘king’; OE wealian, v. "be defiant’; Sw. vilja, v. ‘wish, want’: Slovene veljati, inf. ‘be worth, hold good'; Cz. velet, inf. command'. (Isophones: Arm. gelum, aor: geli (4) 'squat'; W gweli, pl. -iau, m. ‘wound, offence’; gwefio, inf. ‘expose; wound’, Big. velja, v. “speak, say’; Li. velið, v. (2) “adhere”; veléju (2) *devour)
19982:ueluó, ið (1) ‘twist, turn, bend, roll" Cf. uoluo, ulu-. WP I, 298 Arm. gelum, aor. geli, v. ‘twist, sprain’; Gk. eilümi, eilúð, eloo, eild, eillo, v. ‘roll, enve- lop’; Lat. volvo, ére, v. (turn, rol. Vowel ambig. Cf. uoluo); Umb. cf. amb-oltu! “let him turn round"; Ir. cf. fillim, v. “turn, bend? and MHG wëllen, pp: ge-wollen, v. (1) “roll, trun- dle’; OE wilian, v. “bind, connect’. (Isophone: W gwelw, adj. *pale")
20146:and Latv. ambig. Skt. vasarab, adj. “bright; vasrah, m. 'day- time’; Arm. gey, o-st. ‘beauty’; Lat. cf. vel-ox, gs: -Ocis, adj. ‘smart, nimble’; vel-es, -itis, m. “lightly armed soldier; jester', cf. ei-, it-); W gwel, m. “sight, vision" beside gwell, comp. ‘better’; (radical in) Go. wisan, v. (2) ‘rejoice’; OCS (and com. Sl.) veselü, adj. (/gay', ambig. cf. ueKsl-); OPr. wessals, adj. id.; (ambig. also in Latv. vesels, adj. “healthy”, pref. to ueksl-, q.v., in view of Li. veslüs ‘thriving, luxuriant’ and Alb. veshél, adj. *fertile"). (Iso- phone: Ir. feoil, f. ‘flesh, meat"). Cf. uisolos (2)
20174:ueslos (1), cf. ueselos (1) Thus in Skt. vasrah ‘day’; Arm. gey, o-st. ‘beauty’; W gwel, m. “sight, vision’
== IEC gwei
19667:uail- (3) ‘point, tip, edge’. Cf. WP I, 213 & 316 Skt. véla, f. id.; Arm. gajl, Let ‘wedge, gag"; W gwaell, pl. gweill, f. *spit, skewer, spindle'
19838:ue£hen- (ueghn-) ‘carrier, conveyor, convey- ance; carriage, cartage'. Cf. uegh- Skt. vahanam, n. ‘conveyance’; váhnih, m. *charioteer; steed'; Av. vazanom, n. 'cartage, conveyance’; -vazano, adj. cpds. *-conveying"; Lat. cf. (?) vena, f. (tube, vein’; LLat. also *stream — of tar'; cf. ductus, üs in a similar sense); Gaul. cf. co-vinnus, m. (fchariot'. Cf. W cy-wain, v. *Àconvey?); OIr. fén, Ir. féan, pl. féin, m. ‘wagon’; W gwain, pl. gweiniau, f. (2) ‘support; (3) ‘carriage’; (o-gde in) OHG wagan, mpl: wagene, wegene, m. (cart, and com. Gmc.); Blg. vezni, mpl. “scales, balance”; Li. vezenà, f. ‘goods in transit beside vež- mene, pl. “baggage”
19843:Av. cf. vastar, m. ‘draught-animal’; Lat. vectis, gp: -ium, m. ‘lever’; Olr. fecht, mf. (1) "our, ney'; W gwaith, pl. gweithiau, f. ‘course’; OBr. cf. (?) guithennou, pl. ‘veins’; Cor góth, gwyth, pl. gwythy, f. *vein, stream'. Semantics of ? Lat. vena, if fr. *ue&hna); MHG wihte-, cpds. *weight-, scale-; OE wiht, f. ‘weighing, weight; G Ge-wicht, id.; ON vætt, pl. vættir, f. (1) “weight; OCS cf. vezti, vesti, inf. ‘to convey’; Li. o-gde vaZtà, vastà, f. “freight; car, carriage"
19915:-yow, m. ‘time, occasion, act, work’; W gwaith, pl. gweithiau, m. id.; Go. waíhts, f. ‘thing’; OHG wiht, n. ‘being, thing’; OS wiht, f. i-st. id. (pl: ‘demons’); OHG wiht, fn. as OHG; ON vættr, pl. vættir, f. ‘being, creature’ beside vætr, id.; vætt-, cpds. “fighting-?; OCS vesti, f. ‘thing, nature’; Cz. věc, f. ‘thing’ (but veta, f. id. (veta za vetu 'tit-for-tat'): Pol. wet, said to be a Gmc. LW, fr. wette)
20149:uesor- (2) “grass, hay’. Cf. ues- (5) and ueser- (1). WP I, 311 (Radical in) Hitt. wesis, s. ‘pasture; OHG wisa, G Wiese ‘meadow’; Tokh. wäert, s. ‘grass’; MIr. fér, Ir. féar, m. ‘grass, fresh pas- ture’; OBr. guer- ‘mowing-grass’; W gwair, pl. gweiriau, m. ‘hay’; OCor. guer beside Cor. gora, collective: guyr-af, cpd. ‘hay’. (Myce- , naean has wearejo-, epithet of tables and chairs: “of rushes’? Hes. uphéar, n. ‘mistletoe’
== WLD band3 index
979:gue abret. 247 giedam & | cich abret. 293. guedd , species’ eymr. 223. guedenea abret, 297 gueid ,,Joch" cymr. 256
984:shee 206 gueial cymr. 212.
```


## [2026-09-06T15:01:58.386Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^guel\\|^guei\\|^gu̯el\\|^gu̯ei\" IEC.txt | head -20"
}
```


### [2026-09-06T15:01:58.447Z] TOOL RESULT

```
5142:gueidhó, io "chant, moan’. WP I, 665-6 ON kvíða “fear”; Sw. kvida ‘moan’; OLi. gíemi, gíesti, Li. gíedu, v. ‘sing’ beside inf. giedóti "chant": Latv. dziedu, åt ‘sing
5144:guel- (1) (guelón-) ��barb, spike, needle". Cf. guilos & WP I, 691 Myc. qero-; Gk. bélos, gs -eos ‘dart, arrow’; be- Jong ‘needle’; cf. o-belós, Dor. o-delós ‘spit (fr. *oK- °); EME (?) quill Creed or "oul: (OCS and com. Sl. Zel-ézo “iron”, a cpd.: Li. geležis and Latv. dzelzs, id. seem to contain *ehel- ‘yellow’, etc. q. v.); Srb. cf. žaoka (*Zal- ka ‘spike, dart); Li. geluonis, f. “point, tip, knife-edge': Latv. dzelonis ‘sting’
5145:guel- (2), guel- “pain, sorrow'. Figurative extn. of guel- (1)? Cf. WP I, 690 (with short vowel) Arm. key, o-st. ‘wound, ulcer'; keyem “torture, wound, hurt; MHG qu&l, f., quéln, v. id.; OHG quélan ‘die’; (OS id. & 'suffer); Li. gélia, impers., inf. gélti ‘ache’; Li. dzelu, dzelt “stab, burn, bite’. (with long vowel) Skt. (?) jalam (3) “fraud, blar- ney’; Gk. deléomai “hurt, harm’; OHG quàla, MHG quaàl, -e ‘torture’; G quälen, v. id.; Du. kwaal ‘chronic illness’; OCS Zali ‘sorrow’; žel- ja ‘sadness’ Li. gëlà ‘ache’; Latv. žēlas, fpl. (sorrow. LW? cf.. dzel-ums “bite, wound, sting’ and R u-žal, id., identifying gēl- with guel- (1)) Å
5146:guelbhos, à (guolbh-, gulbh-) “belly, womb, fetus'. WP I, 692 Skt. gárbhah ‘womb, fetus, baby’: Av. garowo, id.; Hitt. cf. hwelpis, adj. ‘newborn, young"; Gk. delphüs, Aeol. belphüs *womb', délphos ‘pig’; delphis, gs -inos “dolphin, pig of iron or lead”; a-delphoí (Cbrothers-and-sisters, sibl- ings’, fr. *sm -?); Lat. volba (& variants ‘vul- va’); Gallo-Lat. cf. galba (as proper n. *pot- belly”, fr. *gulbha); Scythian substrate? in Ukr.
5152:guelo, ið (1), see guel- (2)
5153:guelð, io (2) hurl, fling’. Tokh. B sall-, sal-, id.; Gk. béllo, béllomai, d: Arc. cf. ek-déllo beside zéllo, aor. ézelon, id.; Hes. déllo, id. (Isophonic: OHG quélen, OS id. ‘suffer, die’; OE cwelan, id., cf. ON kveld, Sw. kväll 'evening")
5154:guelón-, see guel- (1)
5159:gueleió — guer- (guor-)
```


## [2026-09-06T15:02:05.681Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^guei\\|^guio\\|^guii\\|jináti\\|jinati\\|bia ‘force\\|‘force, might\" IEC.txt | head -10; echo \"== SYN buck throw/conquer\"; grep -n -i \"^9.21\\|to throw\\b\" SYN.txt | head -5"
}
```


### [2026-09-06T15:02:05.762Z] TOOL RESULT

```
5142:gueidhó, io "chant, moan’. WP I, 665-6 ON kvíða “fear”; Sw. kvida ‘moan’; OLi. gíemi, gíesti, Li. gíedu, v. ‘sing’ beside inf. giedóti "chant": Latv. dziedu, åt ‘sing
5213:guiio, guiià ‘gut, bowstring; guts; strength, force’. Cf. guiios. WP I, 666, and see gliə Skt. Jya, jiya ‘bowstring; force’; Per. zi ‘life’; Gk. biós ‘bow’ beside bía “strength, force’; Lat. (?) vi- in viscera: Osc. cf. bass (pl. *strength"); Ir. cf. in-bhe ‘entrails’; OCS cf. dim. Zi-ca, f. ‘sinew’ and perb. Cz. žíně *horse- hair’; Slovene Zi-ma, id.; Li. eg ‘thread of warp’; Latv. dzija ‘yarn; W cf. bydd ‘tie’ beside bydd-ag ‘trap’. Variant of type *giio (q.v.) in W gi ‘fibre, sinew, nerve’; Cor. gyew: W giau, pl. ‘sinews’. Per. zih ‘bowstring’, like Skt. jya, id., is ambig.
5214:guiió ‘come to life; be alive; enliven’. WP I, 668. Cf. guiios (2) and guruo Skt. cf. jinvàmi, ;jinomi, cpds. ‘stir’; jínami, fut. jyasyami, pp. jitáh ‘overpower’; Per. zi- yam, inf. zistan "live; Gk. cf. beíomai, fut. ‘shall live; Cz. žiju, žít "live; Li. gyju, gyti ‘recover’; Latv. dziju, pf. 1sg. of dzīst “live”
5224:guiios (2) “alive; lively'. Cf. guiuos Skt. cf. -jyáh, cpds.; Lat. cf. vir-bius (for *bis- uius “having lived before? or *twice"); Li. cf. gyju, gyti ‘recover’; Cz. Žiju, žít “live?
== SYN buck throw/conquer
```


## [2026-09-06T15:03:08.987Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m2 -A6 \"Etymology\" 2b2b2d5a7eec1b6e.txt | grep -v \"^\\s*$\" | head -20; mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg206.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/206.png && echo copied"
}
```


### [2026-09-06T15:03:11.277Z] TOOL RESULT

```
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Verb 
--
97: Etymology 
98-
99- 2.2 
100- Pronunciation 
101-
102- 2.3 
103- Verb 
copied
```


## [2026-09-06T15:03:13.690Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"gʷelH\\|From Proto-Hellenic\\|to throw\" 2b2b2d5a7eec1b6e.txt | head -8"
}
```


### [2026-09-06T15:03:13.736Z] TOOL RESULT

```
203: From Proto-Hellenic *gʷəlnō , from Proto-Indo-European *gʷl̥-ne-h₁- , nasal-infix from *gʷelH- ( “ to hit by throwing ” ) . Cognates are uncertain, but compare Sanskrit उद्गूर्ण ( ud-gūrṇa ) and Old Irish at·baill ( “ dies ” ) . [ 1 ] Sihler [ 2 ] argues for a N nasal progressive aspect marker , but Curtius [ 3 ] and Smyth [ 4 ] argue for a *y progressive aspect marker . English ball has a similar sound and meaning, but is unrelated.
225: ( transitive ) to throw , cast , hurl 
3137: Ancient Greek terms derived from the Proto-Indo-European root *gʷelH- (throw) 
3151: Greek terms derived from the Proto-Indo-European root *gʷelH- (throw)
```


## [2026-09-06T15:10:41.109Z] TOOL CALL #81: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-206.json <<'JSON'\n{\n  \"pdf_page\": 206,\n  \"book_page\": 176,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Gweie, Gweye\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʷeyH- / *gʷyeh₁- 'to overpower, prevail, conquer' (Pokorny gʷeiə-, IEW 469-470; LIV *gʷyeh₁-)\",\n      \"note\": \"Pokorny p.469-470 has exactly this root: 'Root / lemma: gʷeiə-, Meaning: to prevail, be mighty', with Skt. jáyati 'overpowers, defeats', jyā́ 'force', Av. jayāi 'to defeat, conquer', Av. zinā-/zyā- 'damage', Gk. bía 'force'. Watkins (AHD appendix) has the same root as 'gʷeiə-. To press down, conquer. Sanskrit jayati, he conquers. [Pok. gʷeiə- 469]'. Nourai's twin citation form 'Gweie, Gweye' renders the two ablaut shapes gʷei-ə- / gʷeyə-; language label (Indo-European) and gloss ('to over power, defeat') are both right. The root as Pokorny states it is a bundle: the palatal-initial Iranian branch (zinā-, zyā- 'harm') and the labiovelar branch (Av. ǰay-, Skt. jayati, Gk. bía) are joined by him under one lemma, and modern handbooks (LIV) keep *gʷyeh₁- 'überwältigen' with the same members. The two doubtful members of Nourai's chart are the Avestan 'gā-' box (#3) and the Old English quench box (#8), see there.\",\n      \"note_fa\": \"ریشهٔ بازسازی‌شدهٔ هندواروپایی آغازین *gʷeyH-/*gʷyeh₁- به معنی «چیره شدن، شکست دادن» است؛ پوکورنی (ایو ۴۶۹–۴۷۰) آن را با همین معنا آورده و سنسکریت jáyati «چیره می‌شود»، اوستایی ǰay- «پیروز شدن» و zyā-/zinā- «آسیب رساندن» و یونانی bía «زور» را ذیل آن نهاده است؛ واتکینز نیز در پیوست ریشه‌های هندواروپایی همان ریشه را با ارجاع به همان صفحهٔ پوکورنی آورده است. پس نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است. تنها دو شاخهٔ آن (اوستایی gā- «گاییدن» و انگلیسی کهن ācwencan) مورد تردید پژوهش امروزی است که در همان گره‌ها توضیح داده شده.\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\"ref\": \"POK:469\", \"status\": \"supports\", \"note\": \"POK_full.txt (Pokorny database dump), entry 'Root / lemma: gʷeiə-, Meaning: to prevail, be mighty ... References: WP. I 666 ff. Page(s): 469-470'. The cited page 469 is the first page of the lemma; all four Iranian/Germanic members Nourai hangs on the root are discussed inside it.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷeiə-\", \"stance\": \"supports\", \"note\": \"'g”eia-. To press down, conquer. Sanskrit jayati, he conquers: JAIN. [Pok. gʷeiə- 469.]' — same root, same Pokorny page (grep 'To press down, conquer' in AHD_watkins1985.txt).\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. guiio/guiiā (line 5213)\", \"stance\": \"partial\", \"note\": \"'guiio, guiiā ‘gut, bowstring; guts; strength, force’ ... Skt. jyā, jiya ‘bowstring; force’; Gk. biós ‘bow’ beside bía ‘strength, force’. WP I, 666' — Mann keeps the same word-family (WP I 666 = Pokorny's own reference) but files it as a noun root 'sinew/force' rather than a verb 'overpower'.\"},\n        {\"src\": \"WLD\", \"where\": \"WP. I 666 ff. (Bd. I OCR unreadable at that place)\", \"stance\": \"silent\", \"note\": \"Walde-Pokorny I 666 ff. is the reference Pokorny himself gives; the local OCR (incoming/WLD/WLD_Bd1_pages.txt) does not yield the lemma on grep (Greek/diacritic OCR is destroyed), so it could not be read directly.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"zinât; zyâ 3, zyâni\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Bartholomae, AiWb col. 1707: 'j. zyā-; p. diyā- V. ‘schädigen’ (to damage). Praes. 11 zinā- ... Inf. zyānai', and cols. 1719 f. 'zyānay- f. ‘Schädigung’', 'zyānā- f. ‘Schädigung, Schaden’'. Nourai's 'zinât' is the 3sg. present zināṯ 'he injures' (nasal-infix present zi-nā- of the root zyā-), and 'zyâ 3, zyâni' are the root and the abstract noun zyāni- 'injury' (the 3 is the homonym number). Pokorny prints the same forms on p.469-470: 'Avestan zinat ‘damages’ ... Avestan zyana, zyani- f. ‘damage, harm’, Inf. zyanai ‘to harm’'; the palatal z- here goes back to the satem treatment of the initial, beside the labiovelar variant in Av. ǰay- (node #6) and Skt. jáyati, and Old Persian has the matching a-dinā-t 'he took away'.\",\n          \"derivation_fa\": \"اوستایی zyā- «آسیب رساندن» با ستاک حالِ میان‌وندی zinā- (سوم‌شخص مفرد zināṯ) و اسم zyāni-/zyānā- «زیان، آسیب» در فرهنگ بارتولومه (ستون ۱۷۰۷ و ۱۷۱۹) با همین معانی آمده است؛ پوکورنی نیز همین صورت‌ها را در صفحهٔ ۴۶۹–۴۷۰ ذیل ریشهٔ *gʷeyH- نقل کرده است. صورت پارسی باستانِ همریشه a-dinā-t «گرفت، ستاند» است. آغازهٔ z در این شاخه نتیجهٔ تحول سَتِمی است، در برابر شاخهٔ ǰ (گرهٔ ۶). ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:469\", \"status\": \"supports\", \"note\": \"Pokorny p.469-470 s.v. gʷeiə-: 'Avestan zinat ‘damages’ ... Avestan zyana, zyani- f. ‘damage, harm’, Inf. zyanai ‘to harm’' (grep 'zyana' in POK_full.txt).\"},\n            {\"ref\": \"SOD:470\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, printed p.470-471 (entries 11521 and 11535, located by the running page numerals in SOD_pages.txt): '11521 zyʾn B — zyan ‘harm’'; '11535 zykh B — zika (zykh) *ziyaka < Av. zya ‘damage’'. Gharib derives the Sogdian word from Avestan zyā- exactly as the arrow requires.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiWb col. 1707, 1719 (BRT.txt lines 28278, 28291, 28299)\", \"stance\": \"supports\", \"note\": \"'j. zyā-; p. diyā- V. ‘schädigen’. Praes. 11 zinā- ... Inf. zyānai'; 'zyānay- f. ‘Schädigung’'; 'zyānā- f. ‘Schädigung, Schaden’'.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 469-470\", \"stance\": \"supports\", \"note\": \"See ref_check; Pokorny places zinat/zyāni- under gʷeiə- and links them to Skt. jyāni-h 'decrease, loss'.\"},\n            {\"src\": \"SOD\", \"where\": \"p.470-471, entries 11521, 11535\", \"stance\": \"supports\", \"note\": \"Sogdian zyʾn 'harm', zykh 'damage' < Av. zya.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"zîyân «زیان»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. zyāni-/zyānā- 'damage' > Middle Persian zyān [zyʾn] 'loss, harm, damage' (MacKenzie, CPD 99) > New Persian ziyān, with the regular anaptyctic i breaking the initial cluster zy- (MP zyān is read ziyān already in Book Pahlavi practice). Parthian has the same word (Manichaean zyʾn), and the form was borrowed from Middle Iranian into Jewish Babylonian Aramaic zīyanā, Mandaic zāyinā, and Old Armenian zean; Kurdish and Pashto ziyān, Balochi ziyānī, Ossetic ziān are Persian loans (Horn no. 679). The meaning never shifted: 'harm, injury' > 'loss, damage'.\",\n          \"derivation_fa\": \"«زیان» از فارسی میانهٔ zyān (نوشتهٔ zyʾn، در فرهنگ مکنزی: «loss, harm, damage») و آن از اوستایی zyāni-/zyānā- «آسیب» است؛ خوشهٔ آغازیِ zy- در فارسی نو با واکهٔ میانجی i شکسته شده و ziyān شده است. مؤلف در حاشیهٔ برهان قاطع (ص ۱۰۵۰ به بعد) همین را می‌گوید: «پهلوی zyān، اوستا zyāna-، zyāni- (ضرر)، بارتولمه ۱۷۰۷ و ۱۷۱۹؛ سانسکریت jyāni-». هرن (شمارهٔ ۶۷۹) نیز واژه‌های کردی، افغانی، بلوچی، آسی و ارمنی را وام از ایرانی می‌داند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/زیان\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1050\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol.2 (BQT_v2_pages.txt, leaf 512 ≈ printed p.1050-1055; the ز+ی chapter 'بیان هیجدهم' opens on leaf 511) carries the headword زیان with Mo'in's etymological footnote: 'پهلوی zyān، اوستا zyāna-، zyāni- (ضرر) «بارتولمه ۱۷۰۷، ۱۷۱۹»؛ سانسکریت jyāni- (ظلم)؛ کردی ziyān؛ افغانی zyān؛ بلوچی ziyānī؛ آسی ziān؛ ارمنی zean'. Exactly Nourai's arrow. (The scan's running heads are too corrupt to fix the page to the digit, so the page is given as ≈1050.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.99 (PHD.txt line 686)\", \"stance\": \"supports\", \"note\": \"'zyān [zyʾn! | M zyyʾn, N ziyān] loss, harm, damage. ~gar, ~ōmand: harmful' — the MP link between Avestan and NP.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 679, p.150\", \"stance\": \"supports\", \"note\": \"'679. ziyān ‘Schaden’. aw. zyāna- ‘Schaden’; phlv. zi(y)ān (talm. זיאן; mand.); skr. (Brāhm.) jyāna- ‘Bedrückung’. LW. kurd. afγ. ziyān; bel. ziyānī; oss. ziān; arm. zean.'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/زیان (Persian section)\", \"stance\": \"supports\", \"note\": \"'From Middle Persian zydʾn /zyān/ ‘loss, harm, damage’ ... Cognate with Parthian zyʾn, Avestan ziiānā ‘damage’, Sanskrit ज्यान (jyāna) ‘oppression’.'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan\",\n          \"words\": \"gâ 2; gâmô\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The two words are real only in a qualified sense and the arrow from *gʷeyH- is not the modern view. (a) 'gâmô': Horn p.197 no. 883 quotes 'aw. gāmō.bərəti- ‘Coitus’ (nach Geiger, Ostiran. Kultur, 341 n.2)' — i.e. the sense rests on Geiger's interpretation of a compound; Bartholomae's AiWb has no Avestan gāmō 'coitus' at all (only gāya- 'step, pace' and its compounds, and mayah- 'Begattung' for 'coitus'). (b) The verb root 'gā 2 to rape' is likewise not an Avestan lemma in Bartholomae; it is the Iranian verb reconstructed from Middle and New Iranian. (c) The genealogy: Pokorny (469-470) mentions the family only as a hesitant aside — 'after Lidén IF. 19, 328 with npers. gāyad ‘futuit’, Inf. gādan, gān, from a root *gʷai- or (?) *gʷōi-, which would be compatible only with the latter beginning with gʷei- as lengthened grade of the o-gradation at most theoretically'. Cheung (Etym. Dict. of the Iranian Verb, s.v. *gaH² 'to have sexual intercourse') keeps the root separate and says 'The root *gaH is probably etymologically related to *gaH¹ [‘to go, stride’, PIE *gʷeh₂-]', a euphemism that 'has largely replaced the old IE root *Hiab'. So the modern account derives the word from 'to go/come (to)', not from 'to overpower'.\",\n          \"derivation_fa\": \"این گره مورد اختلاف است. «gāmō» تنها بر پایهٔ خوانش گایگر از ترکیب اوستایی gāmō.bərəti- به معنی «آمیزش» است که هرن (ص ۱۹۷) نقل کرده؛ بارتولومه چنین واژه‌ای ندارد و در فرهنگ او تنها gāya- «گام» و mayah- «آمیزش» آمده است. ریشهٔ فعلی «gā» نیز مدخل اوستایی نیست بلکه بازسازی از ایرانی میانه و نو است. پوکورنی خودِ پیوند با ریشهٔ *gʷeyH- را تنها با تردید و به نقل از لیدن آورده و آن را «دست‌بالا از دید نظری ممکن» خوانده است، و چونگ در فرهنگ ریشه‌شناختی فعل‌های ایرانی این ریشه را *gaH² «آمیزش کردن» می‌داند و آن را به احتمال زیاد با *gaH¹ «رفتن» (هندواروپایی *gʷeh₂-) پیوند می‌زند، یعنی کاربردی حُسنِ تعبیری. پس پژوهش امروزی این پیکان را نمی‌پذیرد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:470\", \"status\": \"partial\", \"note\": \"Pokorny p.469-470 does name the Persian verb under gʷeiə-, but only as Lidén's suggestion and with an explicit reservation: 'after Lidén IF. 19, 328 with npers. gayad ‘futuit’, Inf. gadan, gan, from a root *gʷai- or (?) *gʷōi-, which would be compatible ... at most theoretically'. He gives no Avestan gā-/gāmō.\"},\n            {\"ref\": \"HRN:197\", \"status\": \"supports\", \"note\": \"Horn p.197 no. 883: 'gāden ‘coitiren’, Praes. gāy-em, gāyīden, gāye, gūn ‘Coitus’. aw. gāmō.bərəti- ‘Coitus’ (nach Geiger, Ostiran. Kultur, 341 Note 2); phlv. gātan (Y.48,6 ...)' — this is where Nourai's Avestan gāmō comes from, with Geiger's caveat that Nourai drops.\"},\n            {\"ref\": \"FFD:70\", \"status\": \"partial\", \"note\": \"Abolghasemi, Fe'lhā-ye fārsi-ye dari p.70 (PDF page 75 of FFD_pages.txt, printed = pdf − 5): 'گادن: گاد < فارسی میانه gād ... گاد < فارسی میانه gād < ایرانی باستان *gād-'. He goes back only to Old Iranian *gād-, with no IE root and no Avestan attestation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiWb s.v. gāya- (BRT.txt line 10349) and mayah- (line 19925)\", \"stance\": \"contradicts\", \"note\": \"Bartholomae has 'j. gāya- m. ‘Schritt’, als Masseinheit' and, for coitus, 'j. mayah- n. ‘Begattung, Beischlaf’'; there is no Avestan root gā- 'coire' and no gāmō 'coitus' in the dictionary — the Avestan box has no lemma of its own.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *gaH² 'to have sexual intercourse'\", \"stance\": \"contradicts\", \"note\": \"'The root *gaH is probably etymologically related to *gaH¹ [‘to go, stride’], cf. YAv. upaētəm ‘(having) sexual intercourse’ (*Hai): it has largely replaced the old IE root *Hiab' — a different origin from Nourai's 'overpower' root; Cheung cites Horn 1893: 197 for the material.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 883, p.197\", \"stance\": \"partial\", \"note\": \"Supplies the forms, but the Avestan gloss is credited to Geiger, not established lexicography.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"gâtan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Book Pahlavi gʾtn = gādan, present stem gāy- (ideographically written SLYTWN-), 'to copulate with'. MacKenzie, CPD p.34: 'gādan, gāy- [SLYTWN-tn! < A šry; gʾtn! | N ~] copulate with', and the derivative gādār 'husband'. Horn p.197 already cited 'phlv. gātan (Y.48,6, vgl. Horn ZDMG 43,36 n.32; Vd.15(29) Gl.)', i.e. the verb is attested in the Pahlavi glosses to the Avesta. Nourai's 't' is the Book-Pahlavi transliteration (⟨gʾtn⟩) of what is transcribed gādan — intervocalic d written with the letter t is normal Pahlavi orthography.\",\n          \"derivation_fa\": \"پهلوی گادن (نوشتهٔ gʾtn، خوانش gādan) با ستاک حال gāy- به معنی «آمیزش کردن»؛ مکنزی (فرهنگ کوچک پهلوی، ص ۳۴) آن را با هزوارش SLYTWN-tn' ثبت کرده و مشتق gādār «شوهر» را نیز آورده است. هرن هم در ص ۱۹۷ به کاربرد آن در ترجمهٔ پهلوی یسنا ۴۸٫۶ و وندیداد اشاره می‌کند. نگارشِ t در «gâtan» همان املای پهلوی است و آوای آن d است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"HRN:197\", \"status\": \"supports\", \"note\": \"Horn no. 883, p.197: 'phlv. gātan (Y. 48, 6, vergl. Horn, ZDMG. 43, 36 Note 32; Vd. 15 (29) Gl.)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p.34 (PHD.txt line 376)\", \"stance\": \"supports\", \"note\": \"'gādan, gāy- [SLYTWN-tn! ; gʾtn! | N ~] copulate with'; also 'gādār' glossed 'husband' (PHD.txt line 2345).\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *gaH²\", \"stance\": \"supports\", \"note\": \"'MIDDLE PERSIAN: BMP (SLYT(W)N-) /gāy-/, inf. gʾtn /gādan/ ‘to copulate, unite with’.'\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual II Glossary\", \"stance\": \"silent\", \"note\": \"grep for gādan/gʾtn/gāy- in NYB_vol2_glossary.txt returns nothing — the verb is not in Nyberg's (selective) glossary.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"gâdan «گادن (گاییدن)»; گاد ، گای\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"MP gādan/gāy- continues unbroken into New Persian: the old infinitive گادن gādan (now obsolete/dialectal) with past stem گاد gād and present stem گای gāy-, beside the secondary infinitive گاییدن gāyīdan built on the present stem — exactly the two script forms and the two stems Nourai prints. Horn p.197: 'gāden ‘coitiren’, Praes. gāy-em, gāyīden, gāye, gūn ‘Coitus’', with the Iranian cognates Kurd. gāyīn, Pashto γaγ/γōmə, Ossetic qāyun, Balochi gāy. Abolghasemi (FFD p.70) states the same: 'گاد < فارسی میانه gād؛ امروزه «گایید» به جای «گاد» به کار می‌رود ... گای < فارسی میانه gāy'. The only thing this node does not carry is a connection to the chart's root (see node #3).\",\n          \"derivation_fa\": \"«گادن» (کهنه) با مادهٔ ماضی «گاد» و مادهٔ مضارع «گای»، و صورت نو «گاییدن» که بر پایهٔ مادهٔ مضارع ساخته شده، دنبالهٔ مستقیم فارسی میانهٔ gādan/gāy- است. هرن (ص ۱۹۷) همین صورت‌ها را با همریشه‌های کردی gāyīn، پشتو، آسی و بلوچی آورده و ابوالقاسمی در «فعل‌های فارسی دری» ص ۷۰ می‌نویسد: «گاد < فارسی میانه gād. امروزه «گایید» به جای «گاد» به کار می‌رود». پس زنجیرهٔ فارسی میانه ← فارسی نو در این گره درست است؛ تنها انتساب آن به ریشهٔ «چیرگی» (گرهٔ ۳) پذیرفتنی نیست.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"HRN:197\", \"status\": \"supports\", \"note\": \"Horn no. 883, p.197: 'gāden ‘coitiren’, Praes. gāy-em, gāyīden, gāye, gūn ‘Coitus’ ... kurd. gāyin ‘sich paaren’; afγ. γō, γōmə; oss. qāyun; bel. gāy'.\"},\n            {\"ref\": \"FFD:70\", \"status\": \"supports\", \"note\": \"Abolghasemi p.70 (pdf leaf 75 in incoming/FFD/FFD_pages.txt): 'گادن — گاد < فارسی میانه gād. امروزه «گایید» به جای «گاد» به کار می‌رود ... گای < فارسی میانه gāy ... گاد < فارسی میانه gād < ایرانی باستان *gād-'. Precisely the two stems (گاد، گای) printed in Nourai's box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *gaH²\", \"stance\": \"supports\", \"note\": \"'NWIR: NP gādan (obs.), gāyidan/gāy-, Bal. gāt/gā(y)-, Kurd. gayin, Awrom. gay/-ga-' — same NP forms.\"},\n            {\"src\": \"PHD\", \"where\": \"CPD p.34\", \"stance\": \"supports\", \"note\": \"'gādan, gāy- ... | N ~' — MacKenzie's '| N ~' means the New Persian form is identical to the Middle Persian one.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 883, p.197\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Avestan\",\n          \"words\": \"žayâi; žya 4\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"These are the labiovelar branch of the root in Avestan, where Nourai's ž- stands for the palatal affricate ǰ of standard transcription. Bartholomae AiWb: 'j. ⁴ǰyā- V. ‘debilitare, minuere’. Praes. 11 ǰinā-, ... Inf. ǰyāi. — ǰināiti ‘debilitat’ F.35', with the note 'd. i. ǰiy-, daher auch ǰay° geschrieben' — so Nourai's 'žya 4' is literally Bartholomae's homonym-number 4 ǰyā-, and 'žayâi' is the infinitive ǰyāi in its ǰay- spelling. Pokorny p.469-470 gives both senses: 'Avestan ǰayāi, full grade of the root, ‘to defeat, conquer’' and 'Avestan ǰyā-, present ǰināiti ‘exhausts, weakens’'. Nourai's gloss 'defeated, diluted' is a loose English rendering of 'debilitare, minuere' ('weakened, diminished') — 'diluted' is infelicitous but not wrong in intent.\",\n          \"derivation_fa\": \"این گره شاخهٔ لبی‌کامیِ ریشه در اوستایی است؛ آنچه نورایی ž می‌نویسد همان ǰ نویسه‌گردانی متعارف است. بارتولومه دارد: «⁴ǰyā- فعل ‘ناتوان کردن، کاستن’، ستاک حال ǰinā-، مصدر ǰyāi» و می‌افزاید که همین ریشه ǰay° هم نوشته می‌شود؛ پس «žya 4» دقیقاً شمارهٔ ۴ بارتولومه است و «žayâi» همان مصدر ǰyāi. پوکورنی (۴۶۹–۴۷۰) هر دو معنا را می‌آورد: ǰayāi «پیروز شدن، شکست دادن» و ǰyā-/ǰināiti «ناتوان می‌کند». برگردان «diluted» در کتاب ترجمهٔ آزادِ minuere «کاستن» است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:469\", \"status\": \"supports\", \"note\": \"Pokorny p.469-470: 'jayati (Perf. jigaya) ‘overmatched, overpowered, defeated’ (Avestan Inf. jayai, full grade of the root, ‘to defeat, conquer’) ... Avestan jya-, present jinaiti ‘exhausts, weakens’'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiWb s.v. ⁴ǰyā- (BRT.txt line ~11689)\", \"stance\": \"supports\", \"note\": \"'j. ⁴ǰyā- V. ‘debilitare, minuere’. Praes. 11 ǰinā-, 27 (Pass.) ǰya-. — Inf. ǰyāi. ǰināiti ‘debilitat’ F.35' + note 'd. i. ǰiy-, daher auch ǰay° geschrieben' — confirms both the form and Nourai's homonym number 4.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 469-470\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷeiə-\", \"stance\": \"partial\", \"note\": \"Watkins cites only 'Sanskrit jayati, he conquers' for this branch; the Avestan cognate is not spelled out but is the same etymon.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"Empty box. The printed page (PDF p.206 = book p.176, image copied to data/verification/sources/refs/ocr/BOOK/206.png) shows a wide rectangle to the right of the žayâi box with no language label, no reference and no word in it: the author drew the frame and never filled it. The extraction is faithful; there is nothing to verify.\",\n          \"derivation_fa\": \"این خانه در خودِ کتاب خالی چاپ شده است: در تصویر صفحهٔ ۱۷۶ (پی‌دی‌اف ۲۰۶) کادری بی‌برچسبِ زبانی، بی‌ارجاع و بی‌واژه در برابر خانهٔ žayâi دیده می‌شود. خطای خوانش اسکن نیست؛ خانه در چاپ خالی است و چیزی برای راستی‌آزمایی وجود ندارد.\",\n          \"sources\": [],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book\"}],\n          \"consulted\": [{\"src\": \"BOOK\", \"where\": \"printed page 176 (pdf 206), rendered at 200 dpi\", \"stance\": \"silent\", \"note\": \"the box is blank on the page itself; PNG stored at data/verification/sources/refs/ocr/BOOK/206.png\"}]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Old English\",\n          \"words\": \"âcwencan\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Old English word is real: ācwencan 'to quench, extinguish (fire, light)', the causative of cwincan 'to go out, be extinguished, vanish'. What is disputed is the arrow from the IE root. Pokorny does draw it — under gʷeiə- he lists 'Middle High German verquīnen ... Old English cwīnan, a-cwīnan ‘dwindle away’, extended Old English cwincan, acwincan ‘disappear’ (Kaus. with ablaut neologism acwencan, engl. quench)' — but modern Germanic etymology does not: Etymonline, s.v. quench, gives 'Old English acwencan ‘to quench’, from Proto-Germanic *kwenkjanan, probably a causative from the source of Old English cwincan ... No certain cognates outside Germanic; perhaps a substratum word', and Watkins' AHD appendix (which Nourai cites) has no QUENCH under gʷeiə- or any other root. So the word belongs to a Germanic family of unclear ultimate origin, and the IE derivation drawn here is Pokorny's 1959 guess only.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی کهن درست است: ācwencan «خاموش کردن» صورت سببیِ cwincan «خاموش شدن، ناپدید شدن» است. آنچه مورد اختلاف است پیوند آن با ریشهٔ هندواروپایی است: پوکورنی (۴۶۹–۴۷۰) آن را ذیل *gʷeyH- آورده و acwencan را «سببیِ نوساخته با تناوب واکه» خوانده، اما ریشه‌شناسی امروزی آن را از ژرمنی آغازین *kwenkjanan می‌داند و می‌افزاید «همریشهٔ مطمئنی بیرون از ژرمنی ندارد؛ شاید واژه‌ای زیرلایه‌ای باشد» (اتیمانلاین)؛ در پیوست ریشه‌های هندواروپاییِ واتکینز نیز quench اصلاً ذیل هیچ ریشه‌ای نیامده است. پس پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\"https://www.etymonline.com/word/quench\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1070\", \"status\": \"partial\", \"note\": \"p.1070 of the 1976 AHD New College Edition is the main-dictionary page with the entry 'quench', which gives the Old English form; but the AHD Indo-European appendix that Nourai normally cites for root membership does not list QUENCH — grep for 'quench' in AHD_watkins1985.txt returns only Latin stinguere under steig-, no QUENCH headword in the index. So the reference supplies the word, not the root link.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 469-470\", \"stance\": \"supports\", \"note\": \"'Old English cwīnan, a-cwīnan ... extended Old English cwincan, acwincan ‘disappear’ (Kaus. with ablaut neologism acwencan, engl. quench ‘extinguish, put out’)' — Pokorny does place it here.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. quench and s.v. blench\", \"stance\": \"contradicts\", \"note\": \"'quench ... fr. OE. cwencan, in ācwencan ‘to extinguish’, causative of cwincan, ‘to be extinguished, disappear’, rel. to OFris. kwinka' — Germanic-internal only, no IE root given.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/quench\", \"stance\": \"contradicts\", \"note\": \"'from Proto-Germanic *kwenkjanan ... No certain cognates outside Germanic; perhaps a substratum word.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and root list\", \"stance\": \"silent\", \"note\": \"QUENCH does not appear among the English derivatives of gʷeiə- (or of any root).\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"quench\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OE ācwencan > Middle English quenchen 'to extinguish, put out' (c.1200, of fire, light, and figuratively of desire, hunger, thirst) > modern quench; the OE prefix ā- was lost in Middle English and the palatalised -c- gave -ch-, as in drench : drink and blench : blink. The step from the Old English box to the English box is uncontroversial; only the ancestry above the Old English box is in doubt (node #8).\",\n          \"derivation_fa\": \"انگلیسی quench از انگلیسی کهن ācwencan و از راه انگلیسی میانهٔ quenchen «خاموش کردن» (حدود ۱۲۰۰ م.) آمده است؛ پیشوند ā- افتاده و c کامی‌شده به ch بدل شده است، درست مانند جفت‌های drink/drench و blink/blench. این پیوند بی‌اختلاف است و تردید تنها به تبارِ بالاتر از خانهٔ انگلیسی کهن (گرهٔ ۸) بازمی‌گردد.\",\n          \"sources\": [\"https://www.etymonline.com/word/quench\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"The AHD main entry (p.1070) gives the ME/OE chain for quench; the IE-roots appendix does not treat the word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. quench (KLN_1966.txt line 31371)\", \"stance\": \"supports\", \"note\": \"'quench, tr. v., to extinguish. — ME. quenchen, fr. OE. cwencan, in ācwencan, ‘to extinguish’, causative of cwincan'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Quench\", \"stance\": \"supports\", \"note\": \"'Quench. (E.) M. E. quenchen. A.S. cwencan, to extinguish; causal of A.S. cwincan (pt. t. cwanc), to go out, be extinguished.' (OCR garbled but legible).\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/quench\", \"stance\": \"supports\", \"note\": \"'Middle English quenchen, ‘to extinguish, put out’ ... Old English acwencan ‘to quench’.'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Gwel 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʷelH- (probably *gʷelh₁-) 'to throw, reach; hit by throwing'\",\n      \"note\": \"Pokorny pp.471-472 has 'Root / lemma: gʷel-2, gʷelə-, gʷlē-, Meaning: to drip, flow; to throw', whose β-section is exactly Nourai's material: 'Avestan niγraire ‘they are flung down’ (ni-gar-); gr. βάλλω ‘throw, cast’ (*gʷel-n-o) ... From New Testament Greek παρα-βάλλω > παραβολή > Latin parabola ‘parable’ > Italian parlare : Spanish hablar : French parler'. Watkins' appendix words the root with Nourai's very gloss: 'gʷelə-1. To throw, reach ... Greek ballein, to throw: BALLISTA; ... DEVIL, (DIABOLIC), (EBLIS) ... (PARLIAMENT) ... Greek ballizein, to dance: BALL², (BALLAD), (BALLET). [Pok. 2. gʷel- 471.]' Modern Wiktionary/LIV reconstruct *gʷelH- 'to throw, reach, pierce; to hit by throwing' and merge Pokorny's gʷel-1 ('pierce, pain') into it. Nourai's numbering 'Gwel 1' is his own (it is Pokorny's gʷel-2); the page 472 falls inside the lemma. Root, language and gloss are all right.\",\n      \"note_fa\": \"ریشهٔ هندواروپاییِ *gʷelH- (به احتمال *gʷelh₁-) «افکندن، پرتاب کردن، رسیدن»؛ پوکورنی آن را در صفحهٔ ۴۷۱–۴۷۲ با شمارهٔ gʷel-2 آورده و همان‌جا اوستایی niγraire «فروافکنده می‌شوند» و یونانی βάλλω و زنجیرهٔ παραβολή > لاتینی parabola > فرانسوی parler را نقل کرده است. واتکینز نیز با همین معنا «to throw, reach» و با فهرستی که DEVIL، EBLIS، PARLIAMENT، BALLET و BALLAD را دربر می‌گیرد. ویکی‌واژه امروز *gʷelH- را بازسازی می‌کند و ریشهٔ gʷel-1 پوکورنی («سوراخ کردن، درد») را نیز در آن ادغام می‌کند. شمارهٔ «Gwel 1» از آنِ خود نورایی است. ادعای او دربارهٔ ریشه درست است.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷelH-\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:472\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Root / lemma: gʷel-2, gʷelə-, gʷlē-, Meaning: to drip, flow; to throw ... Page(s): 471-472'; the cited page 472 is the second page of the lemma, where the Greek and Romance material stands.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷelə-1\", \"stance\": \"supports\", \"note\": \"'gʷelə-1. To throw, reach ... a. Greek ballein, to throw: BALLISTA; ... DEVIL, (DIABOLIC), (EBLIS), ... (PARLEY), (PARLIAMENT), (PARLOR), ... PROBLEM, SYMBOL; b. Greek ballizein, to dance: BALL², (BALLAD), (BALLET), BAYADERE. [Pok. 2. gʷel- 471.]' — the gloss is verbatim Nourai's.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. guelō (2) (IEC.txt line 5153)\", \"stance\": \"supports\", \"note\": \"'guelō, iō (2) ‘hurl, fling’. Tokh. B sall-, sal-, id.; Gk. béllō, béllomai ... Arc. ek-déllō' — the same root as a verb 'hurl'.\"},\n        {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/gʷelH-\", \"stance\": \"supports\", \"note\": \"'*gʷelH- — to throw, reach, pierce; to hit by throwing', with Avestan ni-γrāire and Greek βάλλω among the descendants.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"ni-ğrâ-ire; ni-gar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Bartholomae AiWb: 'j. ⁴gar- V., nur mit ni ‘niederschleudern’ (to hurl down). Praes. 21 grā-', citing Yt.10.40 'yōi niγrāire ... zarahu mašyākanąm', and adding 'Vgl. gr. βάλλω'. So Nourai's 'ni-gar' is the root as Bartholomae lemmatises it (⁴gar- with the preverb ni-, on which see Nourai's own root 'Nî 1'), and 'ni-ğrâ-ire' is the attested 3pl. present mediopassive ni-γrā-ire 'they are thrown down' from the zero-grade stem γrā- < *gʷl̥H-. Klein s.v. ballistic (p.143) quotes the same form as an IE cognate of ballein, and modern Wiktionary lists Avestan ni-γrāire under *gʷelH- via Proto-Iranian *gráHti. The Avestan γ is the regular voiced spirant from *gʷ before the syllabic liquid.\",\n          \"derivation_fa\": \"بارتولومه در فرهنگ ایرانی باستان دارد: «⁴gar- فعل، تنها با پیشوند ni: ‘فروافکندن’، ستاک حال grā-» با شاهدِ یشت ۱۰٫۴۰ «yōi niγrāire» و می‌افزاید «مقایسه شود با یونانی βάλλω». پس «ni-gar» صورت مدخلیِ ریشه با پیشوند ni- است و «ni-ğrâ-ire» صیغهٔ سوم‌شخص جمعِ مجهول-میانهٔ گواهی‌شده به معنی «فروافکنده می‌شوند»، از ستاک بی‌درجهٔ γrā- < *gʷl̥H-. کلاین نیز در مدخل ballistic (ص ۱۴۳) همین صورت اوستایی را همریشهٔ βάλλω می‌داند و ویکی‌واژه آن را ذیل *gʷelH- می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷelH-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:472\", \"status\": \"supports\", \"note\": \"Pokorny p.471-472, section β) of gʷel-2: 'β) Avestan niγraire ‘they are flung down’ (ni-gar-); gr. βάλλω ‘throw, cast, hit, strike’ (*gʷel-n-o)'.\"},\n            {\"ref\": \"KLN:143\", \"status\": \"supports\", \"note\": \"Klein 1966 p.143 (page marker 143 immediately precedes the entry in KLN_1966.txt), s.v. ballistic: '... fr. I.-E. base *gʷel-, whence also OI. apa-gurya- ‘swinging’, Avestic ni-γra-ire ‘they are being hurled down’, Toch. AB kla- ‘to fall’' — the exact form and gloss Nourai prints.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiWb s.v. ⁴gar- (BRT.txt line 10212)\", \"stance\": \"supports\", \"note\": \"'j. ⁴gar- V., nur mit ni ‘niederschleudern’. Praes. 21 grā-. ... yōi niγraire (3PPM.) zarahu mašyākanąm Yt.10.40. Vgl. gr. βάλλω.'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/gʷelH-\", \"stance\": \"supports\", \"note\": \"'Proto-Iranian *gráHti > Avestan ni-γrāire ‘to throw down’' listed under the root present *gʷelH-éti.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 471-472\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"Empty box. On the printed page (book p.176 / PDF p.206, image at data/verification/sources/refs/ocr/BOOK/206.png) the frame to the right of the ni-γrā-ire box is drawn but blank — no language, no reference, no word. The JSON reproduces the page correctly; there is nothing to verify.\",\n          \"derivation_fa\": \"این خانه در چاپِ کتاب خالی است: در تصویر صفحهٔ ۱۷۶ کادری در برابر خانهٔ ni-γrāire کشیده شده که نه برچسب زبانی دارد نه ارجاع و نه واژه. خطای استخراج نیست و چیزی برای راستی‌آزمایی ندارد.\",\n          \"sources\": [],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book\"}],\n          \"consulted\": [{\"src\": \"BOOK\", \"where\": \"printed page 176 (pdf 206)\", \"stance\": \"silent\", \"note\": \"blank frame on the page image stored at data/verification/sources/refs/ocr/BOOK/206.png\"}]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"ballein; para-ballein; sum-ballein; dia-ballein; dia-bolos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek βάλλω 'I throw, cast, hurl' (aor. ἔβαλον, perf. βέβληκα), from *gʷl̥-n-h₁- with the nasal infix, is the central IE reflex of the root. The compounds are all classical and glossed correctly: παραβάλλω 'to throw beside, set side by side, compare' (whence παραβολή 'comparison, parable' — the source of parler/parable, node #4); συμβάλλω 'to throw together, compare' (whence σύμβολον, the token whose two halves are matched); διαβάλλω 'to throw across; to set at variance, slander', whence the agent noun διάβολος 'slanderer', which in the Septuagint and New Testament renders Hebrew śāṭān and so becomes 'the Devil'. The prefix cross-references Nourai gives (Per 1 = περί/παρά, Sem 1 = σύν, Dwo = διά, from *dwo- 'two') are the standard analyses.\",\n          \"derivation_fa\": \"یونانی βάλλω «افکندن» از *gʷl̥-n-h₁- با میان‌وند خیشومی، بازتاب اصلی این ریشه است. ترکیب‌ها همه کلاسیک و درست معنا شده‌اند: παραβάλλω «کنار هم نهادن، سنجیدن» (که παραβολή از آن است و در گرهٔ ۴ به parler می‌رسد)؛ συμβάλλω «به هم افکندن، سنجیدن» (که σύμβολον از آن است)؛ διαβάλλω «از این‌سو به آن‌سو افکندن، بدگویی کردن» و اسم فاعلِ آن διάβολος «بدگو، تهمت‌زن» که در ترجمهٔ سبعینیه و عهد جدید برابرِ «شیطان» به کار رفت و معنای «ابلیس/دیو» گرفت. ارجاع‌های پیشوندی نورایی (Per 1، Sem 1، Dwo) نیز مطابق تحلیل متعارف است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/βάλλω\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. gʷelə-1: 'Suffixed zero-grade form *gʷl̥-n-o- in a. Greek ballein, to throw ... DEVIL, (DIABOLIC), ... PARABLE, (PARABOLA), (PARLEY), (PARLIAMENT), PROBLEM, SYMBOL'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. ballistic (p.143) and s.v. devil (p.~430)\", \"stance\": \"supports\", \"note\": \"'ballistic ... fr. Gk. βάλλειν, ‘to throw’ ... Cp. ... devil, diabolic, discobolus, Eblis, ... hyperbola, hyperbole, metabolism, parable, parabola, parlance, parley, parliament, parlor, parol, parole, ... problem, symbol'; and 'devil ... fr. Gk. διάβολος, ‘slanderer’, fr. δια-βάλλειν, ‘to throw across; to attack; to calumniate, slander’.'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/βάλλω\", \"stance\": \"supports\", \"note\": \"'From Proto-Hellenic *gʷəlnō, from Proto-Indo-European *gʷl̥-ne-h₁-, nasal-infix from *gʷelH- (“to hit by throwing”)'; verb sense 'to throw, cast, hurl'.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 471-472\", \"stance\": \"supports\", \"note\": \"'gr. βάλλω ‘throw, cast, hit, strike’ (*gʷeln-o), zero grade Arcadian ἐσδέλλοντες ... Aor. βαλεῖν, Perf. βέβληκα'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"parler; symbole\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both French words come from this Greek family, but through Latin, which the chart's single arrow suppresses. parler: Greek παραβολή 'comparison, parable' (from παραβάλλω) was taken into Ecclesiastical Latin as parabola 'parable, similitude', then in Late/Vulgar Latin parabolāre '(to speak in parables >) to speak', whence Vulgar Latin *paraulāre > Old French parler (11c.), Italian parlare, Spanish hablar, Portuguese falar — Pokorny himself sets out precisely this chain on p.471-472. symbole: French symbole is a learned 13c. borrowing of Latin symbolum, itself Greek σύμβολον 'token, sign used for matching', from συμβάλλω. Nourai's gloss 'signs (used for comparison)' is right; only the route (via Latin, and in the case of symbole as a learned Renaissance-era loan, not a popular inheritance) is compressed.\",\n          \"derivation_fa\": \"هر دو واژهٔ فرانسوی از همین خانوادهٔ یونانی‌اند، اما از راه لاتینی — و پیکانِ یک‌مرحله‌ایِ نمودار این میانجی را حذف کرده است. parler: یونانی παραβολή «سنجش، مَثَل» به لاتینی کلیسایی parabola رفت، سپس در لاتینی متأخر parabolāre «سخن گفتن (به مَثَل)» و در لاتینی عامیانه *paraulāre که در فرانسوی کهن parler و در ایتالیایی parlare و اسپانیایی hablar شد؛ خودِ پوکورنی (۴۷۱–۴۷۲) همین زنجیره را آورده است. symbole وام‌واژهٔ عالمانهٔ سدهٔ سیزدهم از لاتینی symbolum و آن از یونانی σύμβολον «نشانهٔ همسنجی» است. پس ادعای نورایی با احتیاط پذیرفتنی است: درست اما با حذف حلقهٔ لاتینی.\",\n          \"sources\": [\"https://www.etymonline.com/word/parliament\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. gʷelə-1 lists (PARLEY), (PARLIAMENT), (PARLOR), (PAROL), (PAROLE), PARABLE, SYMBOL among the English derivatives of Greek ballein — i.e. the French words are in the same family, though AHD too routes them through Latin parabola.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 471-472\", \"stance\": \"partial\", \"note\": \"'From New Testament Greek παρα-βάλλω ‘to throw beside’ > παραβολή ‘juxtaposition, comparison ... parable’ > Latin parabola ‘parable’ > Italian parlare : Spanish hablar : French parler' — the Latin stage is explicit in Pokorny, absent in the chart.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/parliament, entry 'parley (n.)'\", \"stance\": \"partial\", \"note\": \"'from Old French parler ‘to speak’ (11c.), from Vulgar Latin *paraulare, from Late Latin parabolare ‘to speak (in parables)’, from parabola ‘speech, discourse’, from Latin parabola ‘comparison’.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. ballistic\", \"stance\": \"supports\", \"note\": \"lists parlance, parley, parliament, parlor, parol, parole and symbol under Greek ballein.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"پارلمان ، سمبول\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both are modern French loans of the Qajar/Constitutional period: پارلمان pārlemān and سمبول sambol/sombol. Strictly, پارلمان renders French parlement (the institution), not the verb parler in the box above it — the French noun parlement is itself a derivative of parler (parler + -ment, 'a speaking, a conference'), so the chain holds one step longer than drawn; سمبول is French symbole directly. Persian took both after the Constitutional Revolution (1906) with the wave of French administrative and literary vocabulary; today سمبول competes with the calque نماد.\",\n          \"derivation_fa\": \"هر دو وام‌واژهٔ فرانسوی دورهٔ قاجار و مشروطه‌اند: «پارلمان» و «سمبول». دقیق‌تر آن‌که «پارلمان» از parlement فرانسوی (نامِ نهاد) گرفته شده، نه مستقیماً از فعل parler که در خانهٔ بالای آن آمده است؛ خودِ parlement مشتقِ parler است (parler + -ment «سخن‌گویی، مجلسِ گفت‌وگو»)، پس زنجیره یک حلقه بلندتر از آن است که در نمودار کشیده شده. «سمبول» بی‌واسطه از symbole فرانسوی است. این وام‌گیری‌ها پس از مشروطه و همراه موج واژگان اداری و ادبی فرانسوی وارد فارسی شدند؛ امروز در برابر «سمبول»، گَرتهٔ «نماد» به کار می‌رود. ادعای نورایی در کل درست، اما در جزئیاتِ صورتِ فرانسوی نادقیق است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"MON:1981\", \"status\": \"partial\", \"note\": \"The page cannot be mapped: only Mo'in's 2-volume Adena abridgement is on disk, whose pagination differs from the 6-volume Amir Kabir edition Nourai cites. The headword is there — MON_part1.txt line 28033: 'پارلمان: ۱ (اح.) انجمن بزرگان مملکت در دربار سابق فرانسه ... مجلس شورای ملی، مجلس نمایندگان در کشورهای مشروطه و جمهوری' — confirming the French institution as the source, but with no origin tag or page match.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (2-vol. abridgement), s.v. پارلمان\", \"stance\": \"supports\", \"note\": \"'پارلمان: (اح.) انجمن بزرگان مملکت در دربار سابق فرانسه ... مجلس نمایندگان در کشورهای مشروطه و جمهوری' — Mo'in defines it by way of the French institution.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/parliament\", \"stance\": \"partial\", \"note\": \"'from Old French parlement (11c.), originally ‘a speaking, talk’, from parler ‘to speak’' — the French noun that Persian actually borrowed is parlement, a derivative of parler.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"parliament\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English parliament, c.1300 parlement 'consultation; formal conference, assembly', from Old French parlement (11c., 'a speaking, talk') from parler; the spelling was refashioned c.1400 after Medieval Latin parliamentum, and the sense 'representative assembly of England' with capital P emerges by mid-14c. So the box's French > English arrow is exactly right.\",\n          \"derivation_fa\": \"انگلیسی parliament در حدود ۱۳۰۰ م. به صورت parlement به معنی «رایزنی، مجلس رسمی» از فرانسوی کهن parlement (سدهٔ یازدهم، در اصل «سخن‌گویی») وام گرفته شده و املای آن حدود ۱۴۰۰ م. به تقلید از لاتینی میانهٔ parliamentum تغییر کرده است؛ معنای «مجلس نمایندگان انگلستان» از میانهٔ سدهٔ چهاردهم رواج یافت. پس پیکان فرانسوی ← انگلیسی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/parliament\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book\"}],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/parliament\", \"stance\": \"supports\", \"note\": \"'c. 1300, parlement, ‘consultation; formal conference, assembly’, from Old French parlement (11c.), originally ‘a speaking, talk’, from parler ‘to speak’; the spelling was altered c. 1400 to conform with Medieval Latin parliamentum.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. ballistic (cross-reference list)\", \"stance\": \"supports\", \"note\": \"'parliament' listed among the English words derived from Greek ballein.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷelə-1\", \"stance\": \"supports\", \"note\": \"(PARLIAMENT) among the derivatives of Greek ballein.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through box with no word printed: it stands for the Latin transmission of the Greek nouns to English — ballista (borrowed from Greek βάλλειν/βαλλίστης in the 2c. BCE as the name of the siege engine), parabola, hyperbolē, problēma, symbolum, metabolē and Ecclesiastical Latin diabolus. Latin has no inherited verb of this root (Latin's own reflexes of *gʷelH- are marginal), so the box is correctly a borrowing station rather than an inherited link.\",\n          \"derivation_fa\": \"این خانه بی‌واژه چاپ شده و نقشِ ایستگاهِ انتقالِ لاتینی را دارد: نام‌های یونانی از راه لاتینی به انگلیسی رسیده‌اند — ballista (وام‌گرفته از یونانی در سدهٔ دوم پیش از میلاد برای منجنیق)، parabola، hyperbolē، problēma، symbolum، metabolē و لاتینی کلیسایی diabolus. لاتینی فعلِ موروثی از این ریشه ندارد، پس این خانه به‌درستی ایستگاه وام‌گیری است نه حلقهٔ موروثی.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. gʷelə-1 routes BALLISTA, HYPERBOLA, PARABOLA, PROBLEM, SYMBOL, DEVIL through Latin borrowings of the Greek nouns.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. ballista / devil\", \"stance\": \"supports\", \"note\": \"'ballista, n., an ancient military engine (Roman antiq.) — L., lit. ‘a throwing machine’, fr. Gk. βάλλειν, ‘to throw’'; 'devil ... fr. Eccles. L. diabolus, fr. Eccles. Gk. διάβολος'.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 471-472\", \"stance\": \"partial\", \"note\": \"Pokorny gives the Latin link only through the loan parabola > Romance; he lists no inherited Latin verb from gʷel-2.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"ballistic, parabola, hyperbola, metabolism, problem, symbol, devil\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All seven are Greek words that reached English through Latin (some through French): ballistic (1775, from Latin ballista), parabola (1570s, Latin parabola < παραβολή), hyperbola (1660s, ὑπερβολή 'a throwing beyond, excess'), metabolism (1878, μεταβολή 'change, a throwing about'), problem (late 14c., πρόβλημα 'a thing thrown forward, question put'), symbol (1590s, σύμβολον), devil (Old English dēofol, from Ecclesiastical Latin diabolus < διάβολος). Klein's ballistic entry lists precisely this set — 'amphibole, ... catabolism, devil, diabolic, ... hyperbola, hyperbole, metabolism, parable, parabola, ... problem, symbol' — so the box is exactly right; the only tacit shortcut is that devil entered Old English directly from Ecclesiastical Latin, several centuries before the learned Greek borrowings.\",\n          \"derivation_fa\": \"هر هفت واژه یونانی‌اند که از راه لاتینی (و گاه فرانسوی) به انگلیسی رسیده‌اند: ballistic (۱۷۷۵، از لاتینی ballista)، parabola (۱۵۷۰م، از παραβολή)، hyperbola (۱۶۶۰م، از ὑπερβολή «فراافکنی، زیاده‌روی»)، metabolism (۱۸۷۸، از μεταβολή «دگرگونی»)، problem (اواخر سدهٔ چهاردهم، از πρόβλημα «آنچه پیش افکنده شود»)، symbol (۱۵۹۰م، از σύμβολον) و devil (انگلیسی کهن dēofol از لاتینی کلیسایی diabolus). کلاین در مدخل ballistic دقیقاً همین مجموعه را برمی‌شمارد. تنها نکتهٔ ناگفته آن است که devil چند سده پیش از وام‌واژه‌های عالمانه و مستقیماً از لاتینی کلیسایی وارد انگلیسی کهن شده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. ballistic, p.143\", \"stance\": \"supports\", \"note\": \"'Cp. ball, ‘party for dancing’, ballista, amphibole, ... catabolism, devil, diabolic, discobolus, Eblis, ecbolic, ... emblem, embolism, emboly, hyperbola, hyperbole, metabolism, parable, parabola, parlance, parley, parliament, parlor, parol, parole, periblem, problem, ... symbol' — Nourai's list is a subset of Klein's.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷelə-1\", \"stance\": \"supports\", \"note\": \"'BALLISTA; AMPHIBOLE, ... DEVIL, ... (HYPERBOLA), HYPERBOLE, METABOLISM, ... PARABLE, (PARABOLA), ... PROBLEM, SYMBOL'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Arabic\",\n          \"words\": \"eblis, iblis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic إبليس Iblīs, the Qurʾānic name of the Devil, is a loan from Greek διάβολος. Jeffery, Foreign Vocabulary of the Qurʾān p.47: 'Iblīs. διάβολος the Devil par excellence ... That the word is a corruption of the Gk. διάβολος has been recognized by the majority of Western scholars'; he notes that the Muslim philologers' derivation from أبلس ablasa 'to despair' was already rejected by al-Jawālīqī. Klein (Eblis, p.496-497) adds the transmission detail: 'Arab. Iblīs, aphetic for Gk. διάβολος ... It is very probable that Gk. διάβολος came into Arabic through the medium of Syriac and that the first syllable of the Greek word was mistaken for the Syriac genitive particle di and subsequently dropped'. The alternative Arabic-root etymology survives as a minority view (noted on Wiktionary), but the form ʾiF'īl is, as Jeffery says, otherwise reserved for foreign words.\",\n          \"derivation_fa\": \"«ابلیس» در عربی وام‌واژه‌ای از یونانی διάβολος است. جفری در «واژگان دخیل در قرآن» ص ۴۷ می‌نویسد که «ابلیس تحریفِ διάβολος یونانی است و بیشتر خاورشناسان آن را پذیرفته‌اند» و می‌افزاید که اشتقاق آن از «أبلس یُبلس» (نومید شدن) را جوالیقی هم رد کرده است. کلاین (ص ۴۹۶–۴۹۷) می‌افزاید که این واژه احتمالاً از راه سریانی به عربی رسیده و هجای نخستِ آن (di) به اشتباه حرف اضافهٔ اضافیِ سریانی پنداشته و افتاده است. اشتقاقِ عربیِ آن امروز دیدگاهی اقلیتی است، چون وزن «إفعیل» جز در واژه‌های دخیل به‌کار نمی‌رود. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/إبليس\"],\n          \"ref_check\": [\n            {\"ref\": \"FVQ:47\", \"status\": \"supports\", \"note\": \"Jeffery p.47 (FVQ_pages.txt leaf 64, printed = leaf − 17): 'Iblīs. διάβολος the Devil par excellence ... That the word is a corruption of the Gk. διάβολος has been recognized by the majority of Western scholars. In the LXX διάβολος represents the Heb. שטן in Zech. iii ...'; also 'al-Jawālīqī, Muʿarrab, 17, also justly argues against an Arabic derivation'.\"},\n            {\"ref\": \"KLN:496\", \"status\": \"supports\", \"note\": \"Klein 1966, printed p.496/497 (the page marker '497' stands four lines before the entry in KLN_1966.txt): 'Eblis, n., the prince of the fallen angels (Arabian religion). — Arab. Iblīs, aphetic for Gk. διάβολος, ‘slanderer’, in Eccles. Gk. ‘devil’ ... probably came into Arabic through the medium of Syriac.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/إبليس\", \"stance\": \"supports\", \"note\": \"'Not attested before the Qurʾān. Theorised to come from Ancient Greek διάβολος ... Alternatively ... from the trilateral root ب ل س ... This would, however, require the trilateral root to take the form ifʿīl which, excepting إحليل, is usually associated with words of non-Arabic origin.'\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1, p.83, Mo'in's footnote 5\", \"stance\": \"supports\", \"note\": \"'ابلیس ... از کلمهٔ یونانی διάβολος بمعنی کذاب و نمّام که از نامهای شیطان است گرفته شده «جفری ۴۷-۴۸»' — Mo'in adopts the Greek etymology and cites the very Jeffery pages Nourai cites.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷelə-1\", \"stance\": \"supports\", \"note\": \"'(EBLIS)' is listed among the derivatives of Greek ballein.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Persian\",\n          \"words\": \"eblîs «ابلیس»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian ابلیس eblīs is an Arabic loan of the Islamic period, taken with the Qurʾānic text and its exegesis; the Persian form and meaning are identical with the Arabic ('the Devil, Satan'), only the pronunciation is Persianised (eblīs with e- for the Arabic hamzated i-). Borhan-e Qate' has the headword on p.83, and Mo'in's footnote there gives exactly the route the chart implies for the Arabic box above it (Greek διάβολος > Arabic > Persian), citing Jeffery pp.47-48.\",\n          \"derivation_fa\": \"«ابلیس» در فارسی وام‌واژه‌ای عربی از دورهٔ اسلامی است که همراه متن قرآن و تفسیرها وارد شده؛ صورت و معنا همان عربی است و تنها تلفظ فارسی شده (eblīs با e- به‌جای همزهٔ مکسور). برهان قاطع این مدخل را در ص ۸۳ دارد و حاشیهٔ معین همان‌جا مسیرِ یونانی διάβολος ← عربی ← فارسی را با استناد به جفری (ص ۴۷–۴۸) تأیید می‌کند. پس این گره دوگانه‌ای است در برابر «دیو/devil» انگلیسی که از همان διάβολος آمده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"BQT:83\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol.1, leaf 293 of BQT_v1_pages.txt = printed p.83 (leaf − 210), footnote 5: 'ابلیس - ابن‌درید نوشته: «اگر ابلیس عربی باشد اشتقاق آن از ابلس یبلس بمعنی ...» ... ابلیس از کلمهٔ یونانی διάβολος بمعنی کذاب و نمّام که از نامهای شیطان است گرفته شده «نفی» «جفری ۴۷-۴۸»'. The page number matches Nourai exactly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"Jeffery p.47\", \"stance\": \"supports\", \"note\": \"the Greek origin of the Arabic word that Persian borrowed (see node #9).\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in's footnotes to Borhan (BQT:83)\", \"stance\": \"supports\", \"note\": \"Mo'in is the author of the Borhan footnote quoted above; he adopts the Greek etymology without reservation.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Greek\",\n          \"words\": \"ballizein\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek βαλλίζω 'to dance, jump about' is a derivative of βάλλω, literally 'to throw one's body about' (ancient Greek dancing being highly athletic); it is attested chiefly in Sicilian and South-Italian Greek, which is exactly why it survived into Latin. Watkins puts it under the same root: 'b. Greek ballizein, to dance: BALL², (BALLAD), (BALLET), BAYADERE'; Klein: 'VL. ballare, fr. Gk. βαλλίζειν, ‘to dance’, which prob. derives fr. βάλλειν, ‘to throw’'.\",\n          \"derivation_fa\": \"یونانی βαλλίζω «رقصیدن، جست‌وخیز کردن» مشتقی از βάλλω است و تحت‌اللفظ یعنی «تنِ خود را افکندن» (رقصِ یونانی باستان ورزشی و پرتحرک بود)؛ این فعل بیشتر در یونانیِ سیسیل و جنوب ایتالیا گواهی شده و از همان‌جا به لاتینی راه یافته است. واتکینز آن را ذیل همین ریشه می‌آورد و کلاین می‌نویسد: «لاتینی عامیانه ballare از یونانی βαλλίζειν ‘رقصیدن’ که احتمالاً از βάλλειν ‘افکندن’ است». ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/ballet\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. gʷelə-1: 'b. Greek ballizein, to dance: BALL², (BALLAD), (BALLET), BAYADERE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. ball, 'a party for social dancing' (KLN_1966.txt line 4327)\", \"stance\": \"supports\", \"note\": \"'ball, n., a party for social dancing. — F. bal, fr. OF. baller, ‘to dance’, fr. VL. ballare, fr. Gk. βαλλίζειν, ‘to dance’, which prob. derives fr. βάλλειν, ‘to throw’. See ballistic and cp. ballad, ballerina, ballet, bayadere.'\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/ballet, entry 'ball (n.2)'\", \"stance\": \"supports\", \"note\": \"'from Late Latin ballare ‘to dance’, from Greek ballizein ‘to dance, jump about’, literally ‘to throw one’s body’ ... from PIE root *gʷele- ‘to throw, reach’.'\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"French\",\n          \"words\": \"bal, ballet\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Correct in substance, compressed in route. French bal 'a dance, dancing party' is the verbal noun of Old French baller 'to dance' (12c.), from Late Latin ballāre, itself the borrowing of Greek βαλλίζειν — so bal is two steps, not one, from the Greek. French ballet is later and comes back through Italy: 1660s, from Italian balletto, diminutive of ballo 'a dance' (from ballāre), taken into French with the court spectacle of the 16th-17th c. Neither word is a direct French continuation of a Greek verb, which is what the single arrow suggests.\",\n          \"derivation_fa\": \"محتوا درست است اما مسیر فشرده شده. فرانسوی bal «رقص، مجلس رقص» اسم مصدرِ فعل فرانسوی کهن baller «رقصیدن» (سدهٔ دوازدهم) است و آن از لاتینی متأخر ballāre که خود وام‌گرفته از βαλλίζειν یونانی است؛ پس دو حلقه فاصله دارد نه یک حلقه. «ballet» دیرتر و از راه ایتالیا آمده: در دههٔ ۱۶۶۰ از balletto ایتالیایی، مصغّرِ ballo «رقص»، که همراه نمایش‌های درباری سده‌های شانزدهم و هفدهم وارد فرانسوی شد. پس هیچ‌یک ادامهٔ مستقیم یک فعل یونانی در فرانسوی نیست و ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/ballet\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book\"}],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/ballet\", \"stance\": \"partial\", \"note\": \"'ballet (n.) ... 1660s, from French ballette from Italian balletto, diminutive of ballo ‘a dance’, from Late Latin ballare ‘to dance’, from Greek ballizein'; and 'ball (n.2) ... 1630s, from French, from Old French baller ‘to dance’, from Late Latin ballare'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. ball 'a party for dancing'\", \"stance\": \"partial\", \"note\": \"'F. bal, fr. OF. baller, ‘to dance’, fr. VL. ballare, fr. Gk. βαλλίζειν' — Latin stage explicit.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Persian\",\n          \"words\": \"bâlet «بالت»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian بالت bālet is a 20th-century French loan (ballet), taken with the European performing arts along with اپرا, تئاتر, ارکستر; the Persian spelling بالت reproduces the French pronunciation [balɛ] with the final -t of the French orthography, whence the older Persian rendering bālet, while the now-usual form is باله bāle, closer to the spoken French. No Arabic or Turkish mediation is involved.\",\n          \"derivation_fa\": \"«بالت» وام‌واژه‌ای فرانسوی از سدهٔ بیستم است (ballet) که همراه هنرهای نمایشی اروپایی و در کنار «اپرا»، «تئاتر» و «ارکستر» وارد فارسی شد؛ املای «بالت» تلفظ فرانسوی [balɛ] را با -t املای فرانسوی بازمی‌تاباند، حال آن‌که صورت رایج امروزی «باله» است که به تلفظ گفتاری فرانسوی نزدیک‌تر است. هیچ واسطهٔ عربی یا ترکی در کار نیست. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"MON:466\", \"status\": \"not_checked\", \"note\": \"Only the 2-volume Adena abridgement of Mo'in is on disk and it has no بالت headword (grep 'بالت:' in MON_part1/part2 returns only کبالت, نبالت, etc.); the 6-volume edition's p.466 (vol. 1, ب) cannot be reached — vajehyab/abadis carry the lexicon text but no page numbers.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, 2-vol. abridgement\", \"stance\": \"silent\", \"note\": \"no بالت entry in the abridged text on disk.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/ballet\", \"stance\": \"supports\", \"note\": \"gives the French word and its 1660s date, i.e. the donor form Persian borrowed in the 20th century.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"English\",\n          \"words\": \"ballet\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English ballet, 1660s, 'theatrical, costumed dance and pantomime performance', from French ballet, from Italian balletto — so, like Persian بالت, an early-modern borrowing of the French court term. The French > English arrow drawn here is exactly the accepted one.\",\n          \"derivation_fa\": \"انگلیسی ballet در دههٔ ۱۶۶۰ به معنی «نمایشِ رقص و پانتومیمِ داستان‌گو» از فرانسوی ballet و آن از balletto ایتالیایی گرفته شده است؛ یعنی مانند «بالت» فارسی، وام‌واژه‌ای از اصطلاح درباری فرانسوی در آغاز دوران جدید. پیکان فرانسوی ← انگلیسی در نمودار همان مسیر پذیرفته‌شده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/ballet\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book\"}],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/ballet\", \"stance\": \"supports\", \"note\": \"'1660s, from French ballette from Italian balletto, diminutive of ballo ‘a dance’.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. ball 'party for dancing'\", \"stance\": \"supports\", \"note\": \"'cp. ballad, ballerina, ballet, bayadere' — all filed under the same Greek etymon.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"English\",\n          \"words\": \"ballroom, ballad\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both belong to this family but neither comes straight from Greek. ballroom is an English compound (1690s) of ball 'dancing party' + room, and ball (n.2) is a 1630s borrowing of French bal (< Old French baller < Late Latin ballāre < βαλλίζειν). ballad is Middle English balade, from Old French balade, from Old Provençal balada 'a dance; a song to dance to', from balar 'to dance', again from Late Latin ballāre. So the Greek > English arrow skips Late Latin plus a Romance stage in each case; the etymology itself is uncontested.\",\n          \"derivation_fa\": \"هر دو به همین خانواده تعلق دارند اما هیچ‌کدام بی‌واسطه از یونانی نیامده‌اند. ballroom ترکیبی انگلیسی (دههٔ ۱۶۹۰) از ball «مجلس رقص» و room است، و ball خود در دههٔ ۱۶۳۰ از bal فرانسوی وام گرفته شده (< فرانسوی کهن baller < لاتینی متأخر ballāre < βαλλίζειν). ballad از انگلیسی میانهٔ balade و آن از balade فرانسوی کهن و آن از balada در پرووانسی کهن به معنی «رقص، ترانهٔ رقص» از فعل balar «رقصیدن» و باز از همان ballāre است. پس پیکانِ یونانی ← انگلیسی در هر دو مورد لاتینی متأخر و یک حلقهٔ رومی را حذف کرده است؛ خودِ ریشه‌شناسی بی‌اختلاف است.\",\n          \"sources\": [\"https://www.etymonline.com/word/ballet\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. ballad (KLN_1966.txt line 4327 f.)\", \"stance\": \"partial\", \"note\": \"'ballad, n. ... ME. balade, prop. ‘a song written for a dance’, fr. OF. balade (F. ballade), fr. OProvenç. balada, lit. ‘dance’, later used in the sense of ‘dancing song’, fr. balar, ‘to dance’. See ball, ‘party for dancing’' — the Romance intermediaries the chart omits.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/ballet, entry 'ball (n.2)'\", \"stance\": \"partial\", \"note\": \"'ball (n.2) ‘dancing party’, 1630s, from French, from Old French baller ‘to dance’, from Late Latin ballare' — ballroom is built on this English noun.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷelə-1\", \"stance\": \"supports\", \"note\": \"'BALL², (BALLAD), (BALLET)' listed under Greek ballizein; the parenthesised forms mark indirect (Romance-mediated) descent.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSON\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-206.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 206"
}
```


### [2026-09-06T15:10:44.867Z] TOOL RESULT

```
JSON OK
nodes verified: 24/24
node verdicts: {'confirmed': 16, 'disputed': 2, 'unverified': 2, 'plausible': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 17, 'partial': 5, 'not_checked': 8}
books consulted: {'supports': 42, 'contradicts': 4, 'partial': 10, 'silent': 5} | by book: {'KLN': 11, 'Etymonline': 10, 'POK': 7, 'AHD': 6, 'BRT': 4, 'Wiktionary': 4, 'PHD': 3, 'HRN': 3, 'CHEUNG': 3, 'MON': 3, 'BOOK': 2, 'SOD': 1, 'NYB': 1, 'SKT': 1, 'BQT': 1, 'FVQ': 1}
```


## [2026-09-06T15:11:06.851Z] AGENT

Page 206 (book p.176) verified — `data/verification/page-206.json` written, `verify_check.py 206` reports 24/24 nodes, 0 PROBLEM lines.

**Counts:** roots 2 confirmed · nodes 16 confirmed, 4 plausible, 2 disputed, 2 unverified (blank boxes). Ref checks: 17 supports, 5 partial, 8 not_checked. Books consulted: POK, WLD, AHD/Watkins, IEC, BRT, PHD, NYB, HRN, CHEUNG, SOD, BQT, MON, FFD, KLN, SKT, FVQ, plus Wiktionary/Etymonline (all web pages archived via fetch_source.py).

**Disputed**
- *Gweie* #3 Av. `gâ 2 / gâmô` "to rape" — Bartholomae has no Avestan root gā- 'coire' and no gāmō 'coitus' (only gāya- 'step', mayah- 'Beischlaf'); the gloss rests on Geiger's reading of gāmō.bərəti- quoted by Horn 197. Pokorny mentions NP gāyad here only as Lidén's guess, "at most theoretically"; Cheung (EDIV *gaH²) derives it instead from *gaH¹ 'to go' (euphemism). The Pahlavi/Persian nodes below it (#4 gātan, #5 gādan/gāyīdan) are solidly confirmed.
- *Gweie* #8 OE `âcwencan` — Pokorny 470 does put acwencan under gʷeiə-, but Etymonline/Klein give PGmc *kwenkjanan, "no certain cognates outside Germanic; perhaps a substratum word", and Watkins' appendix lists no QUENCH under any root. AHD:1070 is the main-dictionary page, not a root assignment (marked partial).

**Plausible (route compressed, not wrong):** Gwel 1 #4 (French parler/symbole skip Latin parabola/symbolum), #5 (Persian پارلمان is from French *parlement*, not *parler*), #12 (bal < LL ballāre; ballet < Italian balletto), #15 (ballad via Old Provençal balada).

**No extraction errors.** The two empty nodes (entry 0 #7, entry 1 #2) are blank frames in the printed book itself — confirmed on the page image, copied to `data/verification/sources/refs/ocr/BOOK/206.png`.

**Ref-page notes for the owner:** BQT:83 (ابلیس) lands exactly on vol.1 leaf 293 = p.83, and Mo'in's footnote there cites Jeffery 47-48 — the same FVQ:47 Nourai cites. FFD:70 is exact (pdf leaf 75). SOD:470 is a *page*, not an entry number: Gharib p.470-471 has zyʾn 'harm' and zykh < Av. zya. BQT:1050 (زیان) could only be pinned to vol.2 leaf ≈512 (≈p.1050-1055) — the scan's running heads are unreadable there; Mo'in's footnote on that leaf gives Pahlavi zyān / Avestan zyāna-, zyāni- citing Bartholomae 1707, 1719, exactly Nourai's arrow. MON:1981 and MON:466 are unverifiable: only the 2-volume Adena abridgement is on disk (پارلمان present, بالت absent, no page mapping).
