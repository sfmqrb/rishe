# Verification process log — verify-page-171


## [2026-09-05T20:42:33.161Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 171 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-171.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-171.json. Write /home/sfmqrb/git/rishe/data/verification/page-171.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 171` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:42:35.068Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:42:35.665Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:42:35.677Z] TOOL RESULT

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


## [2026-09-05T20:42:35.784Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-171.txt"
}
```


### [2026-09-05T20:42:35.794Z] TOOL RESULT

```
1	=== PDF page 171 (book page 141) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gene 1 : to give birth to  (refs POK:373)
4	#1 (parent #0) [Avestan] refs=POK:373; SOD:462 | zan 1 : to give birth to ; zâta 1 : born ; â-zâta 1 : free born, noble ; ni-zâti : race, generation ; fra-zaintiš : offspring, child ☞Per 1
5	  #2 (parent #1) [Sogdian] refs=SOD:462 | zn` : to give birth to
6	  #3 (parent #1) [Persian] refs=POK:373; BQT:34,995,1459,2134; HRN:181,231 | zâdan, zâîdan «زادن» : to give birth to ; mîrzâ «میرزا» : Nobel born, title of respect ☞A'.m.r ; âzâd «آزاد» : free ; nežâd «نژاد» : race ; farzand «فرزند» : child | extra: زاییدن ، زائو
7	#4 (parent #0) [Avestan / Old Persian] refs=POK:376; KNT:211 | zana 1 : human being
8	  #5 (parent #4) [None] refs=None | 
9	#6 (parent #0) [Sanskrit] refs=POK:375 | ja : made of ; krmi-ja : a red dye "made of worms" ☞Wer 2
10	  #7 (parent #6) [Persian] refs=BQT:1527 | qermez «قرمز» : red
11	  #8 (parent #6) [Arabic] refs=KLN:373 | qirmiz : red
12	    #9 (parent #8) [English] refs=KLN:373 | crimson, carmine, kermes
13	#10 (parent #0) [Latin] refs=AHD | gener, gent, genius, ingenium, germen, nâtus (gnâtus), prae-gnâs
14	  #11 (parent #10) [French] refs=None | 
15	    #12 (parent #11) [Persian] refs=MON |  | extra: جرم ، ژنرال ، ژاندارم ، ژنراتور ، ناسیونال
16	  #13 (parent #10) [English] refs=AHD | genius, engine, engineer, general, gentle, pregnant, generation, nation, nature, Noel
17	#14 (parent #0) [Greek] refs=AHD | genos : race, family ; eu-genos : well born ☞Su 1
18	  #15 (parent #14) [French] refs=None | 
19	    #16 (parent #15) [Persian] refs=MON |  | extra: ژن ، اکسیژن ، هیدروژن
20	  #17 (parent #14) [English] refs=None | gene, oxygen, hydrogen, Eugene
21	#18 (parent #0) [Germanic] refs=AHD | kundjaz : family ; kundigaz : royal born, king
22	  #19 (parent #18) [English] refs=None | kind, king
23	--- entry 1 ---
24	ROOT Gene 2 -> redirect to Gnô
25	
```


## [2026-09-05T20:42:38.867Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-171.json | python3 -m json.tool | head -200",
 "description": "Read source JSON for page 171"
}
```


## [2026-09-05T20:42:39.458Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:42:40.457Z] TOOL RESULT

```
{
    "pdf_page": 171,
    "book_page": 141,
    "entries": [
        {
            "root": {
                "name": "Gene 1",
                "lang": "Indo-European",
                "refs": "POK:373",
                "gloss": "to give birth to"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:373; SOD:462",
                    "words": [
                        {
                            "translit": "zan 1",
                            "gloss": "to give birth to",
                            "script": null
                        },
                        {
                            "translit": "z\u00e2ta 1",
                            "gloss": "born",
                            "script": null
                        },
                        {
                            "translit": "\u00e2-z\u00e2ta 1",
                            "gloss": "free born, noble",
                            "script": null
                        },
                        {
                            "translit": "ni-z\u00e2ti",
                            "gloss": "race, generation",
                            "script": null
                        },
                        {
                            "translit": "fra-zainti\u0161",
                            "gloss": "offspring, child",
                            "script": null,
                            "see": [
                                "Per 1"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Sogdian",
                    "refs": "SOD:462",
                    "words": [
                        {
                            "translit": "zn`",
                            "gloss": "to give birth to",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "POK:373; BQT:34,995,1459,2134; HRN:181,231",
                    "words": [
                        {
                            "translit": "z\u00e2dan, z\u00e2\u00eedan",
                            "gloss": "to give birth to",
                            "script": "\u0632\u0627\u062f\u0646"
                        },
                        {
                            "translit": "m\u00eerz\u00e2",
                            "gloss": "Nobel born, title of respect",
                            "script": "\u0645\u06cc\u0631\u0632\u0627",
                            "see": [
                                "A'.m.r"
                            ]
                        },
                        {
                            "translit": "\u00e2z\u00e2d",
                            "gloss": "free",
                            "script": "\u0622\u0632\u0627\u062f"
                        },
                        {
                            "translit": "ne\u017e\u00e2d",
                            "gloss": "race",
                            "script": "\u0646\u0698\u0627\u062f"
                        },
                        {
                            "translit": "farzand",
                            "gloss": "child",
                            "script": "\u0641\u0631\u0632\u0646\u062f"
                        }
                    ],
                    "script_extra": "\u0632\u0627\u06cc\u06cc\u062f\u0646 \u060c \u0632\u0627\u0626\u0648",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:376; KNT:211",
                    "words": [
                        {
                            "translit": "zana 1",
                            "gloss": "human being",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": null,
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "POK:375",
                    "words": [
                        {
                            "translit": "ja",
                            "gloss": "made of",
                            "script": null
                        },
                        {
                            "translit": "krmi-ja",
                            "gloss": "a red dye \"made of worms\"",
                            "script": null,
                            "see": [
                                "Wer 2"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "Persian",
                    "refs": "BQT:1527",
                    "words": [
                        {
                            "translit": "qermez",
                            "gloss": "red",
                            "script": "\u0642\u0631\u0645\u0632"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 6,
                    "lang": "Arabic",
                    "refs": "KLN:373",
                    "words": [
                        {
                            "translit": "qirmiz",
                            "gloss": "red",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "English",
                    "refs": "KLN:373",
                    "words": [
                        {
                            "translit": "crimson, carmine, kermes",
                            "gloss": null,
                            "script": null
                        }
                    ],
```


### [2026-09-05T20:42:40.487Z] TOOL RESULT

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


## [2026-09-05T20:42:44.687Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-171.json'))\nfor e in d['entries']:\n    print('ROOT', e.get('root'))\n    for n in e.get('nodes',[]):\n        print(n['id'], n['parent'], n['lang'], n['refs'], [ (w.get('translit'),w.get('gloss'),w.get('script')) for w in n['words']], n.get('script_extra'), n.get('note'))\n\" 2>&1 | tail -20"
}
```


## [2026-09-05T20:42:45.451Z] TOOL CALL #6: Bash

```json
{
 "command": "cat tools/verify_check.py | head -80 && echo ---- && ls data/verification/ | head -40"
}
```


### [2026-09-05T20:42:46.761Z] TOOL RESULT

```
1 0 Avestan POK:373; SOD:462 [('zan 1', 'to give birth to', None), ('zâta 1', 'born', None), ('â-zâta 1', 'free born, noble', None), ('ni-zâti', 'race, generation', None), ('fra-zaintiš', 'offspring, child', None)] None None
2 1 Sogdian SOD:462 [('zn`', 'to give birth to', None)] None None
3 1 Persian POK:373; BQT:34,995,1459,2134; HRN:181,231 [('zâdan, zâîdan', 'to give birth to', 'زادن'), ('mîrzâ', 'Nobel born, title of respect', 'میرزا'), ('âzâd', 'free', 'آزاد'), ('nežâd', 'race', 'نژاد'), ('farzand', 'child', 'فرزند')] زاییدن ، زائو None
4 0 Avestan / Old Persian POK:376; KNT:211 [('zana 1', 'human being', None)] None None
5 4 None None [] None None
6 0 Sanskrit POK:375 [('ja', 'made of', None), ('krmi-ja', 'a red dye "made of worms"', None)] None None
7 6 Persian BQT:1527 [('qermez', 'red', 'قرمز')] None None
8 6 Arabic KLN:373 [('qirmiz', 'red', None)] None None
9 8 English KLN:373 [('crimson, carmine, kermes', None, None)] None None
10 0 Latin AHD [('gener, gent, genius, ingenium, germen, nâtus (gnâtus), prae-gnâs', None, None)] None None
11 10 French None [] None None
12 11 Persian MON [] جرم ، ژنرال ، ژاندارم ، ژنراتور ، ناسیونال None
13 10 English AHD [('genius, engine, engineer, general, gentle, pregnant, generation, nation, nature, Noel', None, None)] None None
14 0 Greek AHD [('genos', 'race, family', None), ('eu-genos', 'well born', None)] None None
15 14 French None [] None None
16 15 Persian MON [] ژن ، اکسیژن ، هیدروژن None
17 14 English None [('gene, oxygen, hydrogen, Eugene', None, None)] None None
18 0 Germanic AHD [('kundjaz', 'family', None), ('kundigaz', 'royal born, king', None)] None None
19 18 English None [('kind, king', None, None)] None None
ROOT {'name': 'Gene 2', 'redirect': 'Gnô'}
```


### [2026-09-05T20:42:46.808Z] TOOL RESULT

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
----
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
```


## [2026-09-05T20:43:22.605Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD gene- ===\"; grep -n -A40 '^gene-' AHD_watkins1985.txt | head -80"
}
```


### [2026-09-05T20:43:22.655Z] TOOL RESULT

```
=== AHD gene- ===
```


## [2026-09-05T20:43:24.919Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 171 -l 171 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg171 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T20:43:27.003Z] TOOL RESULT

```
total 17500
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:43 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:43:31.484Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg171.png"
}
```


### [2026-09-05T20:43:31.950Z] TOOL RESULT

```

```


## [2026-09-05T20:43:31.947Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:43:32.704Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD gen- ===\"; grep -n \"kundjaz\\|kuningaz\\|kundiz\\|cynn\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:43:32.753Z] TOOL RESULT

```
=== AHD gen- ===
489:*klai-ni-, bright, pure, in: a. Old English cléne, pure, clean: CLEAN; b. Old English clénsian, to purify, cleanse: CLEANSE. 2. Extended and suffixed zero-grade form *glo-nd in Greek gléné, eyeball: EUGLENA. [Pok. gel- 366.] gel-3. Cold; to freeze. 1. Germanic *kaliz, coldness, in Old English c(iJele, chill: CHILL. 2. Germanic *kaldaz, cold, in Old English ceald, cold: COLD. 3. Germanic *kédl-, cool, in: a. Old English cdl, cold, cool: cooL; b. Germanic *koéljan, to cool, in Old English célan, to cool: KEEL’. 4. Suffixed form *gel-d- in Latin geldre, to freeze: GELA- TIN, GELATION, JELLY; CONGEAL. 5. Suffixed form *gel-u- in Latin gelu, frost, cold: GELID. 6. Probably suffixed zero-grade form *gl-k- in Latin glaciés, ice: GLACE, GLACIAL, GLACIATE, GLACIER, GLACIS. [Pok. 3. gel()- 365.] gembh-. Tooth, nail. I. Suffixed o-grade form *gombh-o-. 1. Germanic *kambaz, comb, in: a. Old English camb, comb: COMB, KAME; b. Old High German kamb, comb: CAM; c. Germanic denominative *kambjan, to comb, in Old English cemban, to comb: OAKUM, UNKEMPT. 2. Greek gomphos, tooth, peg, bolt: GoMPHosIS. II. Per- haps Germanic *kimb- in Old English cim-, cimb-, rim (only in compounds): CHIME?. III. Possibly suffixed form *gembh-ma in Latin gemma, bud, hence gem: GEM, GEMMA, GEMMATE, GEMMULE. [Pok. gembh- 369.] geme-. To marry. Suffixed zero-grade form “gmoa-o- in Greek gamos, marriage: GAMETE, GAMO-, -GAMOUS, -GAMY; GAMOSEPALOUS. [Pok. gem/(e)- 369.] gen-. To compress into a ball. Hypothetical Indo-Euro- pean base of a range of Germanic words referring to compact, knobby bodies and projections, sharp blows. 1. Germanic *kn-a-pp- in: a. Old English cnzpp, hilltop: KNAP?; b. Middle Dutch cnoppen, to snap, and Low German knappen, to snap, hence “to have a bite,” akin to Middle English knappen, to strike sharply, snap: KNAP!; KNAPSACK; C. Old English cnop, knob: KNop. 2. Ger- manic *kn-a-k- in Middle High German knacken, to crack; KNACKWURST. 3. Germanic *kn-a-r- in: a. Norwe- gian knart, knot in wood, akin to the source of Middle English knarre, knob: KNAR; b. Middle English knor, a swelling: KNUR. 4. Germanic *kn-u-b- in Middle Low German knobbe, knubbe, knot in wood, knob: KNOB, NuB. 5. Germanic *kn-u-k- in: a. Old English cnocian, to knock: KNOCK; b. Italian gnocco, nocchio, knot in wood: GNOCCHI; c. Middle Low German kndkel, knuckle, akin to Middle English knakel, knuckle: KNUCKLE. 6. Ger- manic *kn-u-l- in: a. Old English cnyllan, to strike: KNELL, KNOLL; b. Old English cnoll, a knoll: KNOLL!. 7. Germanic *kn-u-p- in Middle Dutch cnoppe, knob, bud: KNOBKERRIE. 8. Germanic *kn-u-t- in: a. Old Eng- lish cnytten, to tie in a knot, knit: KNIT; b. Old English cnotta, knot in cord: KNOT!; c. Old Norse kniitr, knot in cord: KNOUT. 9. Germanic *kn-u-th- in Old High German knodo, knob, knot (> French quenelle): QUENELLE 10. Germanic *kn-i-b- in Old English cnif, knife: KNIFE. 11. Germanic *kn-e-th- in Old English cnedan, to knead: KNEAD. [Pok. gen- 370.] gene-. Also gen-. To give birth, beget; with derivatives referring to aspects and results of procreation and to familial and tribal groups. 1. Suffixed zero-grade form *gn-yo- in Germanic *kunjam, family, in: a. Old English cyn(n), race, family, kin: KIN; KINDRED; b. *kuningaz, king (< “son of the royal kin”), in Old English cyning, king: KING. 2. Suffixed zero-grade form *gn-ti- in: a. Ger- manic *kundjaz, family, race, in Old English cynd, gecynd(e), origin, birth, race, family, kind: KIND!; b. Ger- manic*kundiz, natural, native, in Old English gecynde (ge-, collective prefix; see kom), natural, native, fitting: KIND?; c. Germanic variant *kinth- in Old High German kind, child: KINDERGARTEN, KRIss KRINGLE; d. Latin géns (stem gent-), race, clan (> French gens, men): GENS, GENTEEL, GENTILE, GENTLE; GENDARME. 3. Suffixed full-grade form *gen-es- in: a. Latin genus (stem gener-), race, kind: GENDER, GENERAL, GENERATE, (GENERA-
```


## [2026-09-05T20:44:03.064Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK gen- around 373 ===\"; grep -n \"gene\\?-, ĝen\\|ĝen-, ĝenə-\\|ĝenə-, ĝnē-\" POK_full.txt | head\necho \"--- search zeugen/gebären ---\"; grep -n \"erzeugen, gebären\" POK_full.txt | head"
}
```


### [2026-09-05T20:44:03.119Z] TOOL RESULT

```
=== POK gen- around 373 ===
--- search zeugen/gebären ---
```


## [2026-09-05T20:44:04.505Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT zana ===\"; grep -n \"zana\" KNT.txt | head -20\necho; echo \"=== KLN crimson/qirmiz ===\"; grep -n -i \"qirmiz\\|kermes\\|crimson\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-05T20:44:04.578Z] TOOL RESULT

```
=== KNT zana ===
392:paru-zana- ‘having many men’, with z from j.
395:Varka-zana- '(month) of the Wolf-Men', with z from g; but the entire word is merely re- stored after the Elamite.
1173:pIE *jono-, OP zana- ‘man’ with Med. г, Ау. zana-, Skt. jána-; m OP vispa-cana-, paru- canü-, and (restored month-name) Varka- 2010-; OP d is seen in *wsa-dana- *wispazana-', inferred from the Elamite mi-iš-ša-da-na.
1354:Also [ог } in OP Varkàna-, Varkazana- (see Lex), | : |
1492:Other instances of z are largely the product of pIE ў and gh in Median ($88, $91), or in OP before consonants ($91, $95); such a 2 became s and then š before n: pIE 0: paruzana-, vispazana-, Varkazana-, vaz-
1776:І. Attached to a verbal root, the ablaut grade of the root varying: kara- in compounds, u-céra-, küma-, Катёа-, gausa-, raga-, adv. daríam, drauga-, baga-, bara- and bāra- in compounds, zana- in compounds; less certain formations in d-baha- in daha-vaja, casa-, U-t&na-, u-tava-, gara- in batu-gara-, Vi-vdna-, varga- in hauma-varga-.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1916:а. The prior element is an adjectival modifier: paru-zana- ‘having many men’; vispa-zana- ‘hav-
1928:Varka-zana- ‘(Month) belonging to the wolf-men'. uvdi-pasiya- ‘having self as lord’, with adjectival sufhx.
1964:Without vriddhi in either part: Garma-pada-, and the restored Varka-zana- (but see Lex. s.v.). For further details, see Lex. s.vv. and 8161.
3584:519. 1.90-6. Saith Darius the King: After that I went off to Babylon. When I had not arrived at Babylon, à town by name Zazana, beside the Euphrates—there this Nidintu-Bel who called himself Nebuchadrezzar came with an army against me, to deliver battle. Thereupon we joined battle; Ahuramazda bore me aid; by the favor of Ahuramazda I smote that army of Nidintu-Bel exceedingly. The rest was thrown into the water, (and) the water carried it away. Of the month Anamaka II days were past, then we fought the battle.
3764:88 düha : Vidafarnà : Babiruviya : aja : uta : basta : anaya : Varkazanahya : màhy& : XXII : ra 89 ucabié : dakata : аһа: avafà : атат : Arzam : hya : Nabukudracara : a
3773:Wh. KIA, stating that the first character could be also pa, the third ке or c, the fourth c* or 2°; [Varkazanahya} Kent (all after the Elamite and the traces of OP charac- ters in Rl.'8 squeezes). * XXII KT.
3811:of the month Varkazana XXII days were past—
4512:11 ünàm : paruvzananàm : xSayabiya
4871:1 Adukanaiša Hadukanna$ Nisabbu Mch.- Apr. 2 Otiravahara Turmár Andru Apr.- May 30üigarci$ — Sdkurrisif —— Simannu May- June 4 Garmapada Karmabada$ Dwūzu June- July ОТОТ Turnabagi$ Abu July- Aug. ена агра (та) & — Ulülu Aug.- Spt. 7 Bügayüdi$ — Bagijüti Taxritu = Spt.- Oct. 8 *Vurkazana Margaíana$ Arahsamna Oct.- Nov. 9 Aciyadiya  Haifuüt(;a)& Küslimu — Nov.- Dec. 10 Anémaka HandmakaS Tebétu Dec.- Jan. It Sami(ia)maS Sabitu Jan.- Feb. 12 Viyarna = =Mitia)kannaS Addàru Кер. Мер.
4879:Darius came upon Nidintu-Bel and his army at the Tigris, forced the crossing, and defeated him in IX 26 ($18), and though Nidintu-Bel rallied his forces and took the offensive, again defeated him at Zazana on the Euphrates, X 2 ($19); he pursued him and his few remaining horsemen to Babylon, took that city and Nidintu-Bel with it, and put the rebel to death ($20).
5658:paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
5662:paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.

=== KLN crimson/qirmiz ===
KLN_1971.txt:39968:Iberian origin. See crimson, and miniature, 
KLN_1971.txt:46812:See cave, n., and cp. kirk, kermess, ‘fair’. Cp. 
KLN_1971.txt:49769:fr. Gk. xoxxoc, ‘grain of the kermes, kernel, 
KLN_1971.txt:49984:word fr. Gk. x<$xxo;, ‘grain of the kermes, ker- 
KLN_1971.txt:58937:cramoisy, adj., crimson. — F. cramoisi , whence 
KLN_1971.txt:58938:ME. crimosine. See crimson, 
KLN_1971.txt:59986:crimson, n., deep red. — Sp. cremesin , fr. Arab. 
KLN_1971.txt:59987:qirmiz, ult. fr. OI. ‘produced by a 
KLN_1971.txt:60002:Cp. kermes, carmine. 
KLN_1971.txt:60004:Derivatives: crimson, adj. and tr. v., crimson-ly, 
KLN_1971.txt:60005:adv., crimson-ness, n. 
KLN_1971.txt:81988:encrimson, tr. v., to make crimson. — Formed 
KLN_1971.txt:81989:fr. ist en- and crimson. 
KLN_1971.txt:130878:kermes, n., the bodies of the females of an insect 
KLN_1971.txt:130879:found on the kermes oak. — F. kermis, fr. 
KLN_1971.txt:130880:Arab, qirmiz, ult. fr. OI. kfmi-dza-, ‘produced 
KLN_1971.txt:130881:by a worm 1 . See crimson and cp. carmine, 
KLN_1971.txt:130882:kermess, kermis, n., 1) an annual outdoor fair 
KLN_1971.txt:146096:and the second element in kermess, Christmas, 
KLN_1971.txt:179717:petechia, n., one of a number of small crimson
```


## [2026-09-05T20:44:11.989Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '59980,60010p' KLN_1971.txt; echo \"=== carmine ===\"; grep -n -A8 \"^carmine\" KLN_1971.txt | head -20"
}
```


### [2026-09-05T20:44:12.060Z] TOOL RESULT

```
n., crimp-y , adj. 

crimp, n., one who procures seamen by entrap- 
ping them. — Of uncertain origin. 

Derivative: crimp, tr. v., to entrap (seamen), 
crimson, n., deep red. — Sp. cremesin , fr. Arab. 
qirmiz, ult. fr. OI. ‘produced by a 




177 



CROP 



worm’. 01 . kfmih , ‘worm’, is cogn. with Lith. 
kirtnis, kirmele, OIr. cruim , Alb. krimp , ‘worm’. 
Cp. kermes, carmine. 

Derivatives: crimson, adj. and tr. v., crimson-ly, 
adv., crimson-ness, n. 

crinal, adj., pertaining to the hair. — L. crindlis, 
fr. crinis, ‘hair’. See crinite and adj. suff. -al. 
cringe, intr. v. — ME. crengen , fr. OE. cringan , 
‘to fall in battle, yield’, lit. ‘to be bent’, rel. to 
=== carmine ===
39964:carmine, n., a purplish-red color; adj., of pur- 
39965-plish-red color. — F. carmin , fr. ML. carminium , 
39966-a blend of Arab, qlrmiz , ‘worm 1 and L. minium , 
39967-‘cinnabar, red lead, vermilion’, which is of 
39968-Iberian origin. See crimson, and miniature, 
39969-carnage, n., slaughter, massacre. — F., fr. It. car- 
39970-naggio , fr. VL. carnaticum , fr. L. card, gen. 
39971-carnis, ‘flesh, meat’. See carnal and -age and cp. 
39972-carrion, charnel.
```


## [2026-09-05T20:44:13.128Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT lexicon zana ===\"; grep -n \"zana- \" KNT.txt | sed -n '1,20p'\necho \"=== KNT page markers near lexicon z ===\"; grep -n \"vispazana\\|vispa-zana\" KNT.txt | head"
}
```


### [2026-09-05T20:44:13.186Z] TOOL RESULT

```
=== KNT lexicon zana ===
392:paru-zana- ‘having many men’, with z from j.
395:Varka-zana- '(month) of the Wolf-Men', with z from g; but the entire word is merely re- stored after the Elamite.
1173:pIE *jono-, OP zana- ‘man’ with Med. г, Ау. zana-, Skt. jána-; m OP vispa-cana-, paru- canü-, and (restored month-name) Varka- 2010-; OP d is seen in *wsa-dana- *wispazana-', inferred from the Elamite mi-iš-ša-da-na.
1354:Also [ог } in OP Varkàna-, Varkazana- (see Lex), | : |
1776:І. Attached to a verbal root, the ablaut grade of the root varying: kara- in compounds, u-céra-, küma-, Катёа-, gausa-, raga-, adv. daríam, drauga-, baga-, bara- and bāra- in compounds, zana- in compounds; less certain formations in d-baha- in daha-vaja, casa-, U-t&na-, u-tava-, gara- in batu-gara-, Vi-vdna-, varga- in hauma-varga-.
1916:а. The prior element is an adjectival modifier: paru-zana- ‘having many men’; vispa-zana- ‘hav-
1928:Varka-zana- ‘(Month) belonging to the wolf-men'. uvdi-pasiya- ‘having self as lord’, with adjectival sufhx.
1964:Without vriddhi in either part: Garma-pada-, and the restored Varka-zana- (but see Lex. s.v.). For further details, see Lex. s.vv. and 8161.
5662:paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.
=== KNT page markers near lexicon z ===
1492:Other instances of z are largely the product of pIE ў and gh in Median ($88, $91), or in OP before consonants ($91, $95); such a 2 became s and then š before n: pIE 0: paruzana-, vispazana-, Varkazana-, vaz-
1916:а. The prior element is an adjectival modifier: paru-zana- ‘having many men’; vispa-zana- ‘hav-
```


## [2026-09-05T20:44:21.371Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\\|^\\[page\\|\" /dev/null; python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf8',errors='replace').read()\nprint('formfeeds',t.count('\\f'))\ni=t.find('paruzana- adj.')\nprint(t[i-3000:i+3000].replace('\\f','<FF>')[:6000])\nEOF"
}
```


### [2026-09-05T20:44:23.234Z] TOOL RESULT

```
formfeeds 231
th acc. ‘beyond’ (§32, $63.1): Av. pard ‘before’, Skt. purds ‘before’, Gk. таро ‘before’; DPe 15; DPh 5; DH 4, See also para- dayadàm, paradraya.
parü postpos. with acc. ‘along’, and verbal prefix ‘forth’ ($132.3): Av. ?pará ‘before’, Skt. purá ‘before, formerly’, Gk. rapá ‘alongside’: in avapard and with ay-, ar-, gam-, bar-.
parauvaty lsn. as sb. ‘in the east’: руи] "Ре 15, a misreading for pr? : d*r^ ye (uninseribed space between r* and y*) = para : dra ya; seeunder paradraya.
paradayadám sb. asf., perhaps ‘pleasant re- treat’ ($55.II, §148.1V): Аа 3. Possibly mis- written руат“ for p'rud*iljme = paridai- dam, Av. patridaéza- ‘Umwallung, Ummauerung' (Bthl. AiW 865), borrowed in Gk. тарабено ‘park’, cf. JAOS 51.229; or for p'r*d'id^am* = paradidam, from ?para ‘beyond’ + didá- ‘wall’ (q.v.), as ‘that which is beyond or behind the wall’ (ef. Scheil 21.93; Bv. BSLP 30.1.67 j'vadiy paradayadám ‘paradis de vie’).
paradraya phrasal adv. ‘across the sea’ ($44, $191.[V): рата ‘beyond’ + acc. draya ‘sea’. DNa 28f; DSe 29°; XPh 24. paradraiya (848) A?P 24 (Hz. ApI 142). As two words, para draya DPe 15 (Cameron, JNES 2.307-8).
parana- adj. ‘former’: deriv. ($147.11) of stem in OP ?para, para (cf. ВЕШ. AiW 854), Av. рагі, рагб, Skt. рига ‘formerly’ (hardly to be normal- ized parna-, with MB Gr. $267, to Gt. faírneis ‘old’). See also dumlaparanam. — paranam asn. as adv. ‘formerly’ DB 1.51, D'Sb 3.
pariy prep. and prefix ‘around, about’: Av. pairi, Skt. pári, Gk. тері, Lt. per ‘through’, pIE *peri ($64, §75.1, $113, §140.1). Prep. with aec. ‘about’ DB 1.54. Prefix-with ay-, bar-; ef. also pariyana-.
196 OLD PERSIAN
pariyana- sb. ‘superiority’: deriv. ($147.IT) of pariy, in meaning seen in Ау. pairi ‘vorne, über ... hin’, Skt. pári as prefix ‘much, excessively’, cf. Gk. meptoads ‘excessive’ (otherwise Hz. ApI 273, Sen 250). pariyanam nsn. DNb 52.
paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
paruva- adj. ‘being before in time or place’ (§35.1[): Av. paurva-, Skt. pürva-, pIE *pruos (868, $150), ef. Gk. Ion. трохоѕ ‘early’. See also paruviyata, paruviyaüd. parwā npm. ‘former’ DB 4.51. parwam asn. as adv. ‘formerly’ DB 1.9; DBa 15f; DSe 43°, 47; XPh 36, 39; paruvam- ciy DB 1.63, 67, 69.
parwnyata, adv. with preceding hacd, ‘from long ago’: *paruviya- (ie. *parvya-, deriv. of paruva-), Av. paouruya-, Skt. pürvyd-, + adv. suffix -la^, Av. -£ó, Skt. -tas, Gk. -ros, Lt. -tus asin funditus, pIE *-los ($191.11). C£. also paruviyatà. DB 1.7, 8, 45; DBa 11, 12.
[paruv|iyafà adv. ‘at first attempt’: *paruviya- (see paruviyala) + adv. suffix -0à, Av. -fa, Skt. -ihà ($191.ID). DSj 3 (conj. of Brandenstein, WZKM 39.49-51; ef. note ad loc.).
paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.
Parga- sb. ‘Parga’, a mountain in Persia: Elam. par-rak-qa, NPers. Purg ($30). Parga лет. DB 3.44. |
partara- sb. ‘battle’ (as in Elam. and АКК. versions): extension of -r/n- s<FF>tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’, to root in Av. poral-onie ‘they fight’? (Bv. TPS 1945.69-4; not agency noun
‘fighter, foe’ as taken by Wb. KIA 90-1, Bv. Gr. $277; not paratara- ‘foe’, with Wackernagel, KZ 59.29-30, as compar. to [Skt.] pára- ‘distant’ = RV ‘enemy’). partaram asn. DNa 47.
Ратдата- (§29.n2, $31) adj. ‘Parthian’, also тазе, as sb. ‘Parthia’, a province of the Persian Empire: Elam. par-tu-ma, АКК. pa-ar-tu-á, Gk. IIapóià. Extension ($150) of stem seen with vriddhi in Pársa-, but with dialectal difference in the 0/s ($9. VT, 887).
(1) ‘Parthian’: Paréava nsm. DN iv; A?P 4. Par&avaibi$ ipm. DB 2.96. (2) ‘Parthia’: Paréava nsm. DB 1.16; 2.7, 92;
DPe 15; DNa 22; DSe 21°; DSm 8°; XPh 20.
Par8avai ism. DB 2.94° 96°; 3.5, 10. parna-, see duildparanam, parana-. ‘parsa- vb., see fraó-.
?parsa- sb. ‘court’, only in Hz. ApI 278; for his pa[r|saiy lsm. DNb 22, see under patiy.
Pársa- adj. ‘Persian’; also masc. as sb. ‘Persia’, a province of the Persian Empire: Elam. par-sin, АКК. pa-ar-su, Gk. Перо, Пероќа (§9. VI, $87, §126, 5143.11). See also Paréava-. `
(1) ‘Persian’: Pársa nsm. DB 1.49; 2.18, 19, 49; 3.18, 26, 31, 32, 56, 84; 4.16, 26, 83, 84 bis, 85 bis, 86; 5.8°; DPe 22; DNa 18, 46; DN i; DSe 12; DZe 7; XPh 12; A?P 1. Pérsam asm. DB 2.81; 8.2, 29f; DPe 21. Pàrsahyà gsm. DNa 13f, 43; DSe 13; XPh 12. Pérsé ism. DPe 8.
(2) ‘Persia’: Pársa пзш. AsH 3 (for loc., §52.1);
DB 1.14, 41; 2.7; DPd 6f; DSm 6°. Pársam asm. AsH 8f; DB 1.46; 3.33, 34; 49, 28; DZe 12. Pérsam-cé DB 1.66. Pürsá ism. XPa 14 (here ‘Persepolis’, acc. to Cameron, by letter; $166, 6166.1). Pürsà absm. РМа 18, 46f; DSe 17°; Юле 7f, 10; XPh 16. Parsa for lsm. AmH 2 (856.V, §314b; wrongly Hz. AMI 4.132-4, 8.17- 9, as instr. of extent); for пзш. AmH 5 ($53; not nsf. adj., as taken by Hz. AMI 820-1, 34). Pärsaiy lsm. DB 1.2, 34; 2.9; 3.23, 24, 28, 34, 52, 58, 71; DBa 2.
pasü prep. ‘after’, temporal with асе. and local with gen. (Bv. BSLP 33.2.153): Av. paséa, NPers. pds, Skt. paácá, isn. to stem in Lith. (dat.) adv. and prep. різки ‘behind, later, after’ (Foy, KZ 35.26); pIE *po as in Lt. po-lið, positus, Gk. &-vó, + *sg*é, inst. to root noun from *seq*- ‘fol- low’, Av... hacatte, Skt) Gdeate, Gk. trerai, Lt.
See nada lai baa a D Lo AMA tae io at OT IPE Ауаз a зз
~
LEXICON
sequitur (§105; Uhlenbeck, Etym. Wtb. d. altind. Spr., s.v. paced). The s in pasá is OP for Med. $c, Av. sé, from pAr. $c (Ву. Gr. §114; otherwise Mt. Gr. §114). Le
```


## [2026-09-05T20:44:23.425Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN zadan ===\"; grep -n -i \"zâdan\\|zādan\\|zadan\\|zâîdan\\|zāyad\" HRN.txt | head -20\necho \"=== HRN nezad/azad/farzand ===\"; grep -n -i \"farzand\\|āzād\\|nizād\\|nižād\" HRN.txt | head -20"
}
```


### [2026-09-05T20:44:23.497Z] TOOL RESULT

```
=== HRN zadan ===
1583:päz. awazadan.
=== HRN nezad/azad/farzand ===
```


## [2026-09-05T20:44:33.632Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf8',errors='replace').read()\nimport re\nfor m in re.finditer(r'\\b21[0-3]\\b\\s*(LEXICON|OLD PERSIAN)|(LEXICON|OLD PERSIAN)\\s*21[0-3]\\b', t):\n    print(m.start(), repr(t[m.start()-200:m.start()+400]))\n    print('---')\nEOF"
}
```


## [2026-09-05T20:44:33.660Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 1500 HRN.txt; echo; echo \"=== grep persian script ===\"; grep -n \"زادن\\|نژاد\\|فرزند\\|آزاد\" HRN.txt | head -20"
}
```


### [2026-09-05T20:44:35.435Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-05T20:44:35.510Z] TOOL RESULT

```
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
+ Refrain from automated querying Do not send aulomated queries of any sort to Google's Sy
=== grep persian script ===
```


## [2026-09-05T20:44:44.431Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['HRN','POK','SOD','BQT','KNT','KLN','MON','AHD','BRT','PHD','ARY']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-05T20:44:45.978Z] TOOL RESULT

```
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-05T20:44:50.542Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['HRN','POK','SOD','KNT','BQT']:\n    e=d[k]; print('##',k); print('offset:',e.get('page_offset')); print('hint:',e.get('lookup_hint')); print('files:',e.get('local_file')); print()\n\""
}
```


### [2026-09-05T20:44:52.327Z] TOOL RESULT

```
## HRN
offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
files: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt

## POK
offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt

## SOD
offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}
files: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']

## KNT
offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt

## BQT
offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
files: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
```


## [2026-09-05T20:44:57.312Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## HRN leaf 202 (p.181)\"; awk 'BEGIN{RS=\"\\f\"} NR==203' HRN.txt | head -60"
}
```


## [2026-09-05T20:44:58.139Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## HRN leaf 252 (p.231)\"; awk 'BEGIN{RS=\"\\f\"} NR==253' HRN.txt | head -60"
}
```


### [2026-09-05T20:44:59.066Z] TOOL RESULT

```
########## HRN leaf 202 (p.181)
— 181 —
811. ferüx Vorwärts, aufwärts; offen' etcJ).
aw. frq^ Vorwärts' (schw. St. ^frac-^ vergl. N. pr.
FrOdi/a-); phlv. fräd- (päz. fräz^ frfl^); ai. pränc-
(schw. St. präC') ^vorwärts*.
oss. räzäi Von vorn* etc. (210).
812. feramöS Vergessend; Vergessenheit', ferämus^ fera-
muSt^ fer(a)mösiden (Vis und RämTn, S. 50 V. 13).
ai. pra + |/';/?«rs-, ////ifya^c Vergessen' ; y\\]w , framös
bezw. farmös^ framöst^).
bei. samusag, samDsay, n. samusay^ Samösay Ver-
gessen (361), mit anderem Pracfix.
813. ferbih, ferheh^ ferhl (d. i. "^ferhiQi)) 'fett'. Vergl. np.
pih (No. 365).
aw. frapi^wa- 'Voizug, first-rate' (Geldner, Ve-
dische Studien 11, 17iJ)'^); phlv. frapili hi^zw. farpfh;
ai. prapitüd' (vergl. Geldner a. a. (). 155 folg.).
LW. wa;^. farhl^ sar. farhe,
Jüd.-pers. HO*!^ (Is. 17, 4) geht auf ein ap. *//(/-
2)itU' zurück.
814. ferjätn *Ende\
ap. ^frajäma- {{^gani- 'gehen*); \)\\\v, frajäm bezw.
farjam 'Ende', frajämtnltany vergl. fraj(a)ftan (AV.,
jung in Kolophonen. Siehe No. 113).
815. ferxane V^eise, gelehrt*, ferzanegl.
ai. pra + [/^./aw- , jafiäti- 'erkennen , verstehen' ;
phlv. frazänak bezw. farzänak,
Vergl. dänisten (ar. l/iaw-), No. 534.
816. ferzend 'Spross'. sowohl *Sohn* als auch 'Tochter (N'is
und Kämln, S. 22 V. 4, 5 v. u.).
aw. frazainti' 'Nachkonimenschalt*; phlv. farc^attd
bezw. frazand.
*) Vergl. Dar mestcter, Et. ir. IT, 112 foli^g.
*J Nach den arm. LW. hraman^ hrasak, hrahany zu sclilicsson,
scheint im Pehlevi noch /ra-, nicht schon far- gesprochen zu sein.
Das Päzend lässt beide Möglichkeiten offen.
'j Justi' Thema /raj9J/M- *Füllc' rauss also fallen.
```


### [2026-09-05T20:45:00.817Z] TOOL RESULT

```
########## HRN leaf 252 (p.231)
MI
— 231 -
WSO, niiad 'Geschlecht, Abstammung, Adel' *), nizade 'von
adeliger Abstammung 2).
aw. ^nizäti", vergl. skr. Jati-.
1031. uiS&iidy nezend niedergeschlagen (trop.); elend,
niedrig*.
ap. *ni -h l/yaw- niederschlagen*, also etwa ein ap.
*/ii/a«/M- 'niederschlagbar voraussetzend, vergl. indische
Bildungen auf -tti- bei B. Lind n er, Altindische Nomi-
nalbildung, 8 54, Ib (S. 80).
Unsicher.
1032. niSästen 'sich setzen lassen', Praos. uisän-em,
nisänden.
Causativ zu nisesten (No. 1083); phlv. n(i)sastan (vd.
16 (17) ÖL), n(i)sanet (M6n.).
1033. nisesten 'sitzen*, Praes. nisln-em,
g. senastmün 'sich setzen'.
ap. m + [/^had-, Caus. niyasädayam; aw. ni -\-
l^had-, mshiSaiti 'sitzen, sich setzen', Caus. niSädayöis;
phlv. n(i)sastan, n(i)$fnet (vd. 16 (1)) ; ai. ni + [/^sad-,
stdati,
kurd. LW. nisin 'sich setzen'; bei. nindag^ n. nin-
day^ Causat. nistainay (264).
Der Nasal der Wurzelsilbe in np. nism-em ist auf-
fallig (er findet sich auch in bei. nindag, ksl. sedq
(sösti), apr. midMs, ist also wohl alt), ebenso das
lange f. Vergl. Bartholomae, Studien II, 97, 98,
der eine Erklärung für die iranischen Formen allein
versucht. Np. nisäxten 'sich setzen lassen* (z. B. Vis
und Rämin, Seite 24 Vers 7) ist eine Analogiebildung.
1034. niseb Unteres; unten'.
aw. *mxsvaepa-, vergl. x^^^W^' (No. 799) ; phlv.
n(i)Sep (AV.), n(i)sepitan^ n(i)sepmd 'sie gehen unter*
(Salemaifn, Mel. asiat. IX, 238), vergl. v(i)seft, 'Ver-
lorenes Sprachgut*, No. 229.
>) VergL Rückert, ZDMa. 10, 138.
2J Vergl. besonders äähn. II, 765 Vers 11 ; auch II, 611 Vers 1601.
```


## [2026-09-05T20:45:08.376Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_full.txt',encoding='utf8',errors='replace')\nimport re\ndata=t.read()\nfor m in re.finditer(r'lemma:\\s*[^\\n]*g[̑ĝ]?en[əe\\-]', data):\n    print(repr(data[m.start()-60:m.start()+120]))\n    print('--')\nEOF"
}
```


### [2026-09-05T20:45:11.179Z] TOOL RESULT

```
'"male or female ancestor\' derived from zero grade of Root/ \nlemma: gen-1, gene-, gne- gnd-\\ \'to bear (mother, father)\' [origin of the old laryngeal g- > \n\nb-\\ \n\nMaterial: Armenian '
--
'ff., WH. I 601, Trautmann 101 f. \nPage(s): 379-380 \n\nRoot / lemma: gen- \n\nMeaning: to pinch, pluck, press, etc.. \n\nNote: (Persson Beitr. 88 f.); therefrom are gnegh-, gneig-, gner-'
--
'nces: WP. I 574 f., WH. I 590 f. \nPage(s): 369-370 \n\nRoot / lemma: gen-1, gene- gne- gno- \n\nMeaning: to bear \n\nMaterial: thematic present Old lndicya/7a//" generates, bears \', Old '
--
' Meillet \nCinquantenaire 172 ff. \nPage(s): 373-375 \n\nRoot / lemma: gen-2, gene- gne- gno- \n\nMeaning: to know \n\nNote: for the avoidance of the homonyms 1. gen- axe often used with v'
--
'es \' and gr. Y6vaT0(; etc. from gonuQ- \n\nComments: \n\nRoot / lemma: genu-1, gneu- : "knee, joint\' > Root / lemma: gen-1, gene-, gne-, gno- : "to \n\nbear\', (the euphemism of lower par'
--
'ced case Jenatr-i/ptr-): husband\'s brother\'s wife = Root/ \n\nlemma: gen-1, gena-, gne- gnd-\\ "to bear\' suffixed in -/erformant. \n\nMaterial: \n\nNote: \n\nlabialized laryngeal hre- > 0e-'
--
'ma: ken-1 \n\nMeaning: to press, pinch, etc.. \n\nNote: \n\nRoot/ lemma: ken-1 \\ "to press, pinch, etc\' derived from Root/ lemma: gen-\\ "to pinch, \n\npluck, press, etc.\'. \n\nNote: meaning-'
--
```


## [2026-09-05T20:45:23.674Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('POK_full.txt',encoding='utf8',errors='replace').read()\ni=data.find('Root / lemma: gen-1, gene- gne- gno-')\nj=data.find('Page(s): 373-375')\nprint(data[i:j+30])\nEOF"
}
```


### [2026-09-05T20:45:25.245Z] TOOL RESULT

```
Root / lemma: gen-1, gene- gne- gno- 

Meaning: to bear 

Material: thematic present Old lndicya/7a//" generates, bears ', Old Latin geno, gr. 

YEvsaOai (sysvovTO = Old Indie ajananta), compare Old Irish -genatharKon]. (to Indik. - 

gainethar^ it is born ' from *gn-ie-tro), also cymr. genn/^be born', (common Celtic -ns-, -nt- 

> -nn-), bret. gener to give birth to children '; 

redupl. present unthematic Old \n6'\c Jajant/, Avestan zTzanti{y. 1. zazanti), themat. 
Avestan zTzanenti^ they bear '; Konj. zTzanal^ she should bear ', kaus. Aor. Old Indie 
ajTjanaf gave birth to ', Old Irish Fut. gignithir{ *gi-gena-) " he will be born ' and with (old) 
zero grade the root gr. yiyvopai " to come into being; of persons, to be born; of things, to 
be produced; of events, to take place, come to pass, come on, happen, and in past tenses 
to be; to come into a certain state, to become ', Latin gigno, -ere {genui, genitum) " 
produce, bring forth'; 

Perf. Old Indie y5-y/7-e" I am born ', 3. Sq. jajana, 3. P\. jajnur, gr. ysyova, *Y£Yafj£v, 
ysyaclx; (Schwyzer Gr. Gr I 767, 769), Old Irish rogenar{ *ge-gn-) " be born '; 

/>present Avestan za-n-aite " they are born ?' ( *gn-na-mi), Armenian cnanim, Aor. cnay 
" is born; generate, bear ' (I 456; *gna-n-), gr. ysvvau) " of the father, to beget, engender; of 
the mother, to bring forth, to produce ' ( *(g/7-/7a-? different Meillet BSL. 26, 15 f.; postverbal 
is Y£vva "birth, origin, source, beginning; an ancestor; descent, birth; offspring, a 
generation; a race, family', whereof yzyyd\oc, " suitable to one's birth or descent; of 
persons, high-born, noble by birth; so of animals, well-bred; noble in mind, high-minded, of 



things, good of their kind, excellent, notable, genuine, intense '); compare SchwyzerGr. Gr 
1694 

Kaus.-lter. Old \v\6\c janayatr generates, bears ' = Old English cennan^ produce ' 
( *goneJd)\ (under the influence of common Celtic -ns-, -nt- > -nn-), yb-present Old Indie 
jayate^ is born ' (therefrom yaya ' woman '), npers. zayad {*gen-9ia, besides ^/7;;/o in:) 
Avestan zayeite6s.\ with lengthened grade of 2. Basis vowel *gne-Jd: Irish gnTu^\ make, 
do' ("*engender, create '); 

sAropresent Latin na-scor{ *gn-sk6-i) ' is born '; 

common lat gn- > n- 

/b-participle and similar: Old Indie ya/a-/?" born ' (/a/5 -/r? 'gender, sex, kind of), Avestan 
zata-\ Latin natus {cognatus, agnatus) ds., ' born m., a son '; 

Maybe alb. /ri//7a/" brother-in-law', /ri//7a/a "sister-in-law' from Rumanian c^/77/7a/" brother-in- 
law', c^/77/7a/a "sister-in-law'; from Latin cc»^/7a/^5 "related, connected by blood; m. and f. 
as subst. a relation either on the father's or the mother's side. Transf., akin, similar'. 

Paelignian cnatois " the rump, the buttocks ' ( *gn-t6s, so probably also :) gall. Cintu-gnatus 
" firstborn ' (could be in itself also = grYvu)T6(;), f. ^/7a//7a "daughter'; Old Norse kundr'son', 
Gothic -kunds {himina- ) " be a descendant of ', Old English heofon-kund, with t^ Old Norse 
as-kunnr^ of divine origin '; (under the influence of common Celtic -ns-, -nt- > -nn-), zero 
grade Latin genitus {*gen9- or *gene-tos, as :) gall. ^e/7e/a "daughter', expressive cymr. 
geneth {*genetta) ds.. Old Irish a/c/7eo'" nature' (*ad-gena-tom or *-gene-tom)\ Lithuanian 
ze/7/as "son-in-law' {*gena-to-s), ^e/7//s "kinsman, relative' (with gaiter g/mt/" be born '), 
Old Church Slavic zgtb m., Serbo-Croatian ze/"son-in-law, sister's husband ' ( *gena-ti-s)\ 

Maybe suffixed alb. Geg {*gen-tai) dhander, Tosc dhender^ son-in-law ' [common alb. g- > 
d^. Phonetically alb. dhandri^ son-in-law ' : Old \r\^\o janitrl) "progenitor'. 

with reduced eOld High German A//7o'"kid, child' {*gen-tom). Old Saxon kind {*gent6m) 
ds.; 

with full grade the second base syllable gr. -\iyr\\oc, " born ' (5i6-, Koai-; proto gr. -r|-; 
yvnaioq " of or belonging to the race, i. e. lawfully begotten, legitimate '), with o-grade Old 
lndicy/75//-/7m. "kinsman, relative' (originally f. " kinship'), yvu)t6(; "kinsman, relative, 
brother', yvajiri " sister', mcymr. gnawt ^V\r\srr\ar\, relative', Gothic *kndt^s {Dai. knodai) 
"gender, sex'. Old High German knot, knuot'ger\6er, sex' (compare also Old High German 



knuosalv\. 'gender, sex, stem'. Old English cnos/n. " progeny, gender, sex, family '), 
Latvian znuots 'son-in-law, brother-in-law'; 

from the light basis Avestan -zanta-, -zanta-^ born ' (compare cpsprpov : bharf-tram); 
also acymr. -gint^V\6, child' from gen-t-. 

compare an other Aryan forms : Avestan fra-zaintis^ progeny ' (against Old \v\6\c pra- 
jati-h)\ Avestan zq&a-u. 'birth, origin' (Aryan *zan-tha-m)\ z^&ra-u. 'birth' (against Old 
lndicy^/7///'a/77'birth place'); zantu-^ district, administrative district ' = Old \v\6\c Jant'u-h 
'creature'; Avestan z^/7y5/77/7a- participle Put. (against Old \v\6\c Janisyate, Aor. ajanista); 
Old lndicy5/7/77a/7-n. besidesy5/7//77a/7-n. ' birth, gender, sex, lineage '. 

Gr. ysvsTn 'birth', Latin Gen/ta Mana^ name of a divinity', Oscan Deivai Genetai^ 
goddess of birth ', wherefore Latin genitalis ' of or belonging to generation or birth, causing 
generation or birth, fruitful, generative, genital '; 

gr. YSvsGic; ' origin, source, beginning; an ancestor ', Latin genetTvus^ of or belonging to 
generation or birth '; with reduced &. Avestan frazaintis {see above), Latin gens {or iroxw 
*gntf-) ' a clan, stock, people, tribe, nation. Transf., an offspring, descendant; a district, 
country ' (then probably ingens as ' monstrous, vast, enormous '), Germanic l<indi-\v\ 
Gothic fcindins {*genti-no-s) ' provincial governor ', Old Norse l<indi. 'entity, gender, sex, 
descendant '. 

gpt/-\n Old Indie y5//-/7' birth, family ' = Latin /75//-d 'birth, gender, sex', Umbrian nafine' 
a birth, origin, people, nation ', Old English (ge)cyndi. ' kind of, nature, quality, origin, 
source, beginning; an ancestor, descendant ' (engl. I<ind)\ 

/^-stem Latin natu {maior-) 'from birth', therefrom natura^ birth; nature, natural qualities 
or disposition, character; an element, substance, essence, nature'; 

/0/'5e^/75s 'pregnant', v\e\N praegnans, from *-gnatis. 

gena-ter-\r\ Old Indie ya/?//^/'- 'progenitor, father' , janitrf begetter, mother', gr. yEverrip, - 
npoc;, Y£V£TU)p, -opoc; 'progenitor, father', ysvsTSipa 'mother', alb. dtiender, dtiander^sor\- 
in-law, bridegroom ' {*gena-tr-), Latin genitor, genetnx{: Old \r\6\c janitr/j 'progenitor'; 

Armenian c/75^/ 'progenitor, father' {*gena-tio-)\ 



Old \nd'\c Jan/man- {and Janman-) n. " birth, gender, sex, lineage ', Latin germen'germ, 
sprout, scion, shoot, twig, branch', germinare^ sprouted out ', germanus, -a(-/77-from -mn- 
) " brother, 1 . sister (having the same father and mother)' ( *gen-men). 

genos-\n Old \n6\c janah {Gen. Janasah) n. 'gender, sex', Armenian c//7 'birth', gr. ysvog 
"gender, sex', Latin genus^ birth, descent, origin; race, stock, family, house; hence 
offspring, descendants; sex; in gen., class, kind, variety, sort; in logic, genus; of action, 
etc., fashion, manner, way ' {generare^ produce '). 

gon-os\n Old \nd\c jana-h {Gen. Janasah) m. 'gender, sex', Avestan (in compound) 
zana- 'people, humankind ', gr. yovoq m., yovr) f. 'birth, parentage, ancestry'; 

Maybe alb. Geg zana ^ nymph, goddess'; 

-geno-s, -gno-s, -genjos, -gniosasl. composition part e.g. in Latin capri-genus^ 
proceeding from a goat, of the goat kind ', indigenam. f. ' born in a country, native, 
indigenous ' (= Armenian ando-cin, ando-cna-c, ' born in the house of the appropriate 
patron '), alienigenaxw. f. ' born in a foreign land; foreign, alien; and subst., a stranger, a 
foreigner, an alien '; 

gall. Boduo-genus, Litu-genius, Old Irish ingen, ogom inigena' ^\x\ . 

gena\n ncymr. adian^ progeny ' {*ati-genS), anian, bret. dial, agnen^naiuxe' {*nde-gen^. 
Loth RC 36, 106; 39,63; 

with gr. -yEvriq, thrak. -ze/7e5 (AiOY£vr|<; = thrak. Diuzenus, Ai^evp)^), compare venet. 
volti-xenei and volti-xnos, lllyrian PH Anduno-cnetis {Gen.), Volto-gnas, Messapic 
oroagenas^ inhabitant of Uria '; 

gr. yzo-yybc, ' new-born ', Gothic niu-kla-hs' under-age ' (dissim. from niu-kna-, with 
formants -ko), also aina-kla-^ isolated, occasional, sporadic (from *-kna-) and Latin 
singulus {irom *sem-gno-) as well as Latin malignus, benignus, pnv/gnus {'separate, i.e. 
born in other matrimony, stepchild '), Celtic -gnos\n people's name, originally Patronymica, 
e.g. gall. Truticnos{= Drutignos), latinis. Druti filius, ogom Gen. Coimagni, Irish Coim-an, 
gall. Ate-gnia, gr. b^byy\ec^ 'of the same descent '; 

about CypriotlvK; 'kid, child' (barely *£v-yvi(;) compare Schwyzer Gr. Gr. I 450^; 

*gn-Jo- {^\\exe\oxe the above -^/7/b- additional weakening) in Latin genius' the superior 
or divine nature which is innate in everything, the spiritual part, spirit; the tutelar deity or 



genius of a person, place; the spirit of social enjoyment, fondness for good living, taste, 
appetite, inclination; of the intellect, wit, talents, genius ', originally the personified fertility 
(at most zero grades *gen-ios), Gothic kuni{ *gn-io-m). Old High German (etc.) chunni 
"gender, sex', (under the influence of common Celtic -ns-, -nt- > -nn-), compare Gothic 
sama-kunjans f\Vk. PI. "the same gender': gr. opo-yvioq; Latin progenies^ progeny ', Old 
Irish gein {*genen < *gen-n) "birth'. Old English cyne-\n compound " royal ', Old Norse 
konr^son, noble-born man, husband' (Germanic */r^/7//7^a-z in Old High German etc. 
kun/ng'k\ng', i.e. "sprung forth from, belonging to a noble gender'). 

gp- in Old Indie ya-s" descendant ', pra-Ja' progeny \jas-pat/s' paterfamilias, male 
head of a family '(MeilletMSL. 10, 139); 

about Latin /ngenuus' free-born, born of free parents; worthy of a freeman, noble, 
upright, frank, candid, ingenuous ', genu/hus' innate, native, natural; genuine' s. WH. I 593 
f. 

References: WP. I 576 ff., WH. I 590 ff., 597 ff., 868, Trautmann 370, Meillet 
Cinquantenaire 172 ff. 
Page(s): 373-375 

Root / lemm
```


## [2026-09-05T20:45:40.175Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT azata ===\"; grep -n \"āzāta\\|azata\" BRT.txt | head -10\necho \"=== BRT frazainti ===\"; grep -n \"frazainti\\|frazaintiš\" BRT.txt | head -10\necho \"=== BRT nizanti/nizāti ===\"; grep -n \"nizāti\\|nizaiti\\|ni-zāti\" BRT.txt | head -10"
}
```


### [2026-09-05T20:45:40.244Z] TOOL RESULT

```
=== BRT azata ===
2478:Stelle  der  kongruenten  Form  steht :  a)  das  i ;  —  iE  äbyö  frSrtt^  fr}r»m-ainti  asaonqm Neutr.  Sing.:  yüzim  .  .  aogS  data  .  .  x/a-  ..frtrvaBbyoYX.13.afi;  —  zugleich  zurück- '^nmcS  .  .  azimcll  ahyä  (statt  Du.)  ..'weisend:  asti'atjntö  ..  atihe  haxayü  frä- %wqm  mPtihi  ..vaSd>m{sA.)Y.2<).ia;  —  \yente  astvatjr?lahe  Yt.i'>.95;  —  dacnnm dva/sing  ..  qstqscä  .  .  yezT  ahyä^^  (statt'.,  atiihi  ..  kavaya  ..  daenayn  V./o.ig. Plur.) /ö/  mal  xsayehTY.44.\\i.; — duye  —  a)  mit  relativischem  Anschluss;  ama- navaiti  astanqm  (sd.)  .  .  däittm  ahmäicil  !'af6yö  acibyö  yazataHbvT'  yat  am»saeibyö harf^r?m  hrmi^ät  V.  74. 17.  b)  das  sp»^aAbyöYi.fj.^;  —  mmö  äbyö  döi'iräbyü
2895:•  j.  aoxtö-näman-  Adj.  i)  'des  Name  (im Gebet  besonders)  genannt  wird',  von  Gott- heiten: ahrasca  "«lanii  Vr.9.5;  —  vananttm ..  'mamm  YL2/.  1;  —  °ma>um  yasatim V.2,3;  —  'manB yazatahe  Y.J.3,  _j.2of.^, 22.27.  2)  'worin  der  Name  (des  an- gerufenen Gottes)  besonders  genannt  wird', vom  Gebet:  -mana  iwü  yasna  . ,  müra yazäi  Yt.iO.31;  30,  54,  56,  8.  II,  23,  15.
3369:.  .  ungenügende  Nahrung  gäbe,  so  ver- sündigt er  sich"  V. /j.20;  22  {yio  yd^a ausgelassen  ist);  —  hinter  ya-:  yö  Al/°'^a frayazlite  yaia  Ais  AS  nl  yazata  . .  Yt. y.  41.  b)  f?/V  (sd.):  '>ä  °>a  ceij aAurö  ..  zard^ui'lriin  aöaxiayaaa  ,.  °'^i3 "^d  eait  zard^vitrS  .  .  vylnirvltä  °ia asimäl  .  .  7-Tmruyff  ya'iä  . .  vydmrvi/J  .  . sarairus/ro  Y.i2.$l.  2)  'ebenso,  des-
4458:•  j.  an-ähita-,  p.  *an-ähita-'*  Adj.  (fem. 'tä-)  'woran  kein  Fleck,  kein  Makel  ist, haftet,  makellos':  mihnm  .  .  yim  yazata haemö . .  't^m  'Is  "tili  parü  bartsm^n  °tayst pars  zaohräyat  'talibyS  farS  vayzibyS  Yt. JO.88;  —  tiilrtm  .  .  dßrät  vyavantsm bämtbyS  raoxsnibyi}  'iaäbyJ'^X.S.z;  —  'ta F. 5.  o)  bes.  von  der  Ar>dvT  (sd.): anduya  äpS  'tayh  Ny.  4,0,  Vr.  7.5;  Yt. /.  2i;  ^  sonst  mit  sQra-  Adj,  verb.;  ap?in andvJm  sürqm  Hqm  Y.  Ö5.  i  usw.'';  — aridvt  süra  °ta  Y.ö'5.4  USW.";  —  arpdvl Sure  'te  (VS.)  YL5.18  usw.'\  A)  als weibliche  Gottheit*',  Avamfi*:  D  «*«/'a*- masdä  "atfh'C  (=  anahiti')  Uta  mitriß mäm  pätuv  Am.  4;  Am.  j'.
4524:•  '}.  an-usant'  Adj.  (fem,  •saitt-)  'der (etwas)  nicht  (tun)  will,  widerwillig,  ohne CS  zu  wollen':  ndit  mam  vTspe  yazatat>hs •Sf/ttfm  fraerscinta  "nicht  mich  gegen meinenWillen.."Yt  i7. 19;  19;  —  v?r3zyjt usaitica  *°ja(//Vfl(NSf.)''"..  mag  sie  wollen oder  nicht"  N.  6\  —  virszylt  usaiti  (sd.) neu  *'saili'^  N.ö;  — yat  ■j^(NS.)  vi/yei- tii'aisA.)..  M.S.  a6.  a)  "jiJNSm.  alsAdv.J» 'widerwillig':  'sS..  avat  kvar»  ätäpaite{i^) •tJ  h-tu  ma  °s5  ave  stärB  V.9.41;  — frä ahmät  parö  vlspe  daiva  'SS  tarsta  mmanle Y.  57. 18.  o)  sva,  'mit  Gewalt':  vaim>m (sd.)  's5  pai'iy3ife^.4.i,^;  53.
4754:—  yal:iä  ro  data  °/il  (VP.)  spsntä  a^iä na  >räzäa?n  Y.5#.  5;  II.  iZ,  14.  i,  42.1, • — ■  mai^amnt  . .  yat  ksrmlun  "la  (NS.) sp>nta  vispe  hazaesaYLio.$i;  7.3',  /0.92, y.ga,  Y. 57.^23,  60.6;  —  /ml  '/ä  (NP.) spmtä  gaiia  giurvain  Y.2S.0;  Ny.l.i, VyL^o;- —  spmtsttg  °s3ng  yava^yff  yavaSsvB Y.,J.')-3;  4-A\  —  °^^  sptrüa  huxiäi:ra hmfmhs  (Stverz.)  Vr. ;/.  12;  usw.;  —  -sS spints  vatihali  srlräi^  namqn  äebaya  Y. /  5. 1 ;  Vr.  6.1;  —  vlspqscä  'iq  spintq  yasa- maidsY.42.()\  —  °h  spinlS alaonam  yasa- maideY.yi.2,  G.  2. 6  (wo  'sJtca);''*  — 'sanqm  sp)ntanqm  xialtanqm  vinzidsi- %ranqm  Ötnzatqm  aiwyämanqm  taxmanqm ähuiryanqm  ySi  aihy^anhs  alwvanB  ysi hapta  iam^.manavAö.. Yt  lj.82f.;Y.j. 4, 20,3;  — y3i  hapta  'sä  spmta  Yt.2.3;  — ape  °ianam  spmtanqm  dähXtn  Y./9.8;  Yt. ;^.  8 1 ' ;  —  vankubyS  yazataiibyS  yat  'laii- byS  spmtaHbys  Vr. 8.\;  ff. 4, 13. \,Yt.4.y,
4758:nqm  Yt.  J7.2;  —  yö  . .  yazata  ahunm mazdqm  yazata  -/J  spmts  Yt.  J".  1 8,  Y.57.Z ; 2/.2,'Vr./j.  1, 18.1,  ig.i,  23.1,  V.  ig.  19, N,  70;  —  aAur?m  mazdqm  .  .  'sit  sp^ntit yazamaidl  Y.jj.i;  2.2,  25.4,  77.4;  — ii^mS  afturäi  mazdäi . .  'salibyff  spantaAbyS V./p.2s;Ny./.  i,Yt<?.3s,  io.  89. /^.  157, J5.44,  S, /.  i;  —  nsit  xsnävayeiti  ahunm mazdqm  tßit  anye  °^a  sp?nta  Yt.  10. 139; 139;— ^i7/'J  nmätttm  mathantm  ahurahe mazdh  ..  'sanqm  spuntanam  V.  79.32;  32, Y.y.i,  4.7,  22.1.  29.2,  27.2,  Vr.9,6, A.  2. 1 ;  — bsrijayat  ahurd  mazdä  bgry/ay^n sp?ntfi  Yt. /o.  90;  —  yazaite  ahurtm 'IS  sputts  .  .  haom  urvänim Yx.6.\;  —  ahuräi  mazdai  ..  'laAbyS spmtaMyS  .  ,  aiwyS  vanuhibyS  Vr.  Ii.  i ; —  ahurahe  mazdl  .  .  "sanqm  sp>ntanqm sraofahe  asythe  . .  ähr5  Y.  22, 4;  —  ahu- rsica  mazdsi  sraosäica  .  .  rasnvaica  . . mi^räica  .  .  '/aeibyasca  sp>ntaHbyS  . .  Vr. II.  6 ;  Y.  4. 2;  —  ahurahe  mazda  . .  'Sanqm spmlanam  mü-rahe . ,  rUmanasca  ^ästrahe Y.22.23;  (JÄ22,  Yt.7.1.  b)  von  ein- zelnen Göltern:  ahm  at  vahiStfm  . .  hyat sra!st?m  hyat  sp>nt}m  'hm  Y.J7.4;  — astm  vahÜt)m  sra!st?m  °hm  sppnt>m  Yt. j.  18*;  S.  2. 3;  —  ahre  ..  ya^ustsmäi 'Sanqm  spinlanqm  "dem  Ä.,  dem  geschäf- tigsten der  ASp."  Y.I.2;  —  vahu  manS 'hm  sp3nt}m  S.  2.  2;  —  xlfdrtm  vairjm 'hm  sp^trm  S.  2.4;  —  haurvatätim  'hm spintam  S.2.6;  YX. 4-\<i' -j^ amgrsfatätim 'hm  spuntsm  S.  2.7.  ['s'a  spunta  Yt.Ä 38  ist  Einschiebsel,  s.  an-  No.  3.]
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
5412:•  j.  araja^aspa-  m.  EN.  eines  Hyaona- Fürsten":  mairyehe  hyaonahe  "pake  \'tf/. 30;  —  drfantptn^a  'piin  Yt.5.  109;  — tum  yazata    vandar^mainis  (sd.)    'ps  Vt.
5659:•  j.  *arStay-  f.,  anderer  Name  für  arftat- (sd.);  ufaratilUm  .  .  yqmca  sraosahe  ,  , yqmca  'tdif  yazata^e  y.^y.^^.
=== BRT frazainti ===
8047:•  j-.  g-  tätay-''  f.  i)  'Vermögen,  Können, Imslandsein,  Kiaff,  mit  Inf.:  Aat  vf  xsa- :^r^m  kn  'trfi'SS.)  iyao>amli  masda ya>ä *vä  ^kaxmi  (sd.)  asä  vokü  manatikä ^mydidyni  (sd.)  "habt  ihr  die  Herrsch- gewalt, habt  ihr  die  Kraft  lu  tun,  o  M., . .,  o  Asa,  o  VM. . .?"  Y. ^4.5.  2)  'Ver- mögen sva.  Habe,  Besitz,  Gut,  Reichtum'; auch  mit  obj.  und  subj.  Gen.:  mä  yave imat  timiliifm  .  ,  /ratahlt  .  .  x^iiiravatti °ti/  mä  j^ä'hravaiti  äsna  frazaintii  Y. 60.7;  —  äps  °tjm  vS  jaidyämi  pauru.- sars'iqm  . .  *frazaintimla  Y.  (fj.  1 1 ;  —  °tlm pourus.x^a'irqm  .  .  ''frazaintim  Y.  68. 1 1 ; —  kahmäi  °tim  .  .  kahmäi  ainistim  .  . baxsiJni  Yt  10.  108— 110;  —  '/Im  jaio- yanla  . .  molu  pas^aSta  . .  'tlm  baon  sivÜla Yt.5.98;  —  dazdi  ahmJk3tn  . .  'lfm  anum v)r?^r(qmnua  Yt.  ici.33;  —  ydi^a  , .  uz-
16741:•  j-,  g.,  p.  bav-  V.  'werden'.  Fraes.  1  \hm  V.  7.  52  PiiZ.;  —  iJ»«*'  gag'^ia  ''amar- bu;  bv-'\  2  bava-,  3  bva-'\  17  (Fat.)  ] säntis  Yt  ig.  12;  —  iä  srva  ..  bun^  .. büiya-,  22  bJ-'^,  [25  'vlli/\'>,  27  buya-(^)i']  dagvattam  karstayasia  . .  "die  Nägel  wer- Perf.  I  bväv*',  2  babv'^;  J-Aor.  i  bUs-*''.  \  den  zu  Messern  der  Z>.  und  . ."  V.  ly.  10; —  PPfP.  bsta-]  Inf.  buy^,  'bata,  bOzdyäi.  —  vXsp^m  a  ahmat  yat  kan5  .  .  bavaj I)  'werden  sva,  ins  Dasein  treten,  ent- ,  "usque  eo  donec  senex  . .  fuerit"  Y.j.ig; stehen;  erfolgen,  geschehen':  vupim  a/a-'j,  32,  5.38,  5.31,  Y.  65.  9,  FrW.4.3;  — vamm  hsntiinca  bavanlimcai'^  bßsyan-'  itala  dai/iAävS  AuyäiiyS  baväitti  Yt  S.  36; titnca  ",  .  der  (jetzt)  da  ist  und  (jetzt)  FrW.^.jj — yat  baväni /rya  fri^a  paiti.- ins  Dasein  tritt  und  künftig  ins  Dasein  irdn/tf  (s.5)  Yt./J.sö;  —  siviÜS  bavski ya'ka treten  wird"  Y.2/.4,  Vr,/Ä2;  — vispam  ,mazdi  Az.2.  2-7"^  Vyt4*;  —  *ya%a*ra aSaetüS  sttm  haitimca  bavaintJmca^''  bäs-  ,buyäl  (statt  Plur.)  Aväyaonänhs  pantätüS yeintxmia  Y.  rp,  9;  —  vTspayS  afaonö  Yl/ö.  3;  —  yesnyS  ahi  .  .  yesnyö  buyi stuii Aai'ätyaica  bavqi%yäi^a^  bB^yqi%-\Y.62.i;  —  Uta  buyä  afrazaintis  Y.ii.i; yäi^a  Y,52,i;  68.22;  —  ala  Aau  apa-\  —  ta  tiS  buyqn  kumiid^Y.^^.2;  —  «ä«i ylärB  bvat'''  "da  entstand  jener  Abfluss" ,  e?  buyarps  masänä  Ny. _j-ii;  —  alsiJca Yt  ig.  56;  —  yat  kvan  uzuxsyäti  bvat'>  ■  ^wä  Smavantasca  buyamä  "wirksam  möch- zqm  , .  yacsdäi^rjm  "wenn  die  Sonne  auf-  i  ten  wir  durch  dich  werden  und  mächtig" geht,   erfolgt  eine  Purifizirung  der  Erde"  |y.  47. 4;   —   buyama  ahurahe  . .  frya  ..
17974:frazaintivaiit-
17983:•  j.  frazainti'vant-  Adj.  (fem.  'vaiii-)  'der Nachkommenschaft,  Kinder  hat' :  käravaiti .  .  moigavaiti  •vaiti  (VSf.)  V.  2s.  7.
19415:—  lä^  möi  jtf j  (sd.)  tvSm  mazda  Y.46. 19;  —  af  tu  mBi  dai/(sd.)  Y.  43.10; 13.  zu  3):  o/  tat  möi  daxstsm  data Y.34.f>;  —  mazda  at  möi  vaAUtä  .. IWÄ  Y. 54.15";  — parä  hyal  mSt  a.ji- mai  straolB  Y.  43-  n  ^-  S.  noch  möi bes.  B  11)  im  jAw.;  zu  a  l):  yö  mg duf-saiakü  Aistaite  Y.1Q.12;  Y.g.$i]  — späbim  yB  mipaskat  vazaite  Yt  14.  58;  — *frazaintim..ya  ml frätayäi  nmaninua .. Y.  Ö2.  5;  70.14,  YLp.  a6*;  —  draonB  .  . yat  me  da'hat  akurB  Y.  rj.  s;  19. 1,  Yt  12. 25;  —  vanm  .  .  yä  me  aoxta  akurB  V. 2.  31;  —  Aa  ml  bara  aßmaca  . .  N.  lO^;
20187:•  j.  mazga'vant-  Adj.  (fem.  •vaitl-)  'mit Mark  versehen':  raoynavaiti  °vaili  (VSf.) frazaintivaiti  V,  21. 7.
28593:ß-aiusaiti  .  .  upa  tarn  vanam  aiili  yam hs  min-jS ..  V.j.if.  Anhang.  'Äa- (subst.)  steht  an  Stelle  des  Pron.  rel.  in einenn  Satz,  der  einem  vorausgehenden Relativsatz  inhaltlich  koordinirt  ist*':  yat nmänö.paitim  vindätna  ..yö  nS  hub)r?tqm barat  frazaintimla  hd  v»r3zyat  YL  73.  40; — ■  aiim  srvanm  .  ,  yim  upairi  k>r»saspB ayanha  pitüm  pacata  . .  tafsaica  h  S  uiatryH afUatia    Y.p.  II.  2)    auf  ein   Relativ
=== BRT nizanti/nizāti ===
```


## [2026-09-05T20:45:41.161Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD zn ===\"; grep -n \"^ *462 \\|zn'\" SOD_pages.txt | head -20"
}
```


### [2026-09-05T20:45:41.204Z] TOOL RESULT

```
=== SOD zn ===
4754:331 "wzn'k S                                ?.
5122:462 >p6>ys B                                                      14R20
7317: 1239 'nz'pt'ym         B =* 'zn'ptnym                                            (o)pcas ©Yaghn. picas =*pcs-, ptcs-
7778: 1393 >pw zn'kh B                               jbU t^h JjJj               opistarick (pystycyk)
10468:                                                                           =»jn}ptnym         Ozn'ptnym, 'nz'ptfym)
10513:2321 >zn' B                                                        2333 'zr'wsc S                                         c*i*jj
10520:     (o)znak Ozn'kh) ©fzna -»zn'kh:                                2335 'zrmyKh) M                                    ^J\ cj}\
16509:                                                                   xwecnak, xoycnak =>xwycnJk, xwzn'q
16833:     zayda ©f. pp. =*jyt-                                            zna =>)zn,k(h), »zn\ pjn}(h), zn'kh
22553:6561 p'zn'k    B                                     J* jl   6575 pcVt1 B                                    &juAm
34342:         Dhu. 283; abl. wyzr>, C2, 12V17; wyzry(y),             10580 wzn' C         ju^j J-j- ^/^ <? <JJ*)oy{\ i<*~+* U&*+
35248:10860 xwzn'q      C                         j&jnj*-.                   YypS 'nt
36134:11150 z'n'kh    B=» 'zn'kOi)                                    11162 zVkm'n      B                             ^o^
36652: 11326 zmwxtwy        M    i^j^S)^ ^^ j v^-w j3J <jjj *La\ j           11338 zn'kh2 B
36655:                                                                                         jn>     ^pw       zn'kh, zn'kh,
36659: 11327 zmy       B                             a^a <^>*a icz-j*        11339 zn'kh B
36661:                                                                             znak (zn'kh) =»jn\ zn*kh2
36666:                                                                      11340 zn'mnty C                                 J^Jj^Jj
36714:11337 zn'kh1     B                                             j*     11348 ZNH      B, S                              G*)j'<oT
36737:                                                                      z(i)nu ? ^zn'kh1, zyn'kh
```


## [2026-09-05T20:45:50.301Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 527 528 529; do echo \"##### leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' SOD_pages.txt | head -40; done"
}
```


### [2026-09-05T20:45:52.028Z] TOOL RESULT

```
##### leaf 527
                                                                                                                           460


  zyt-
            138.39; Frag. Len. 77R4                                11292 zyyrty C                                    6JL^"^»_p-
                                                                         zyerte ©pp. pi. -t
 11279~zyt- =* zyt-                                                      called, named, summoned
 11280 zyt- C=# zyt-, jyt-
                                                                         STi 33.17, 31.7; Sund. AoFi 1974, 2aR4; C2,
 11281 zyty =* zyty                                                        51V10, 56V29, 31R6, 48V18; BSTii 884.15,
                                          cJli"U3^S laJj^^Jj^
 11282 zyty B, S                                                           892.6
       zayde (zyty)                                                11293 ZK B,S                    (0>>^<-^)(^)j!<uT
       held
          BSTBL; Intox. 33; Hen. Tales. 481.51; BSTi 300;                 xo ©Idg. pron. art. nom. sg. m. 4xw, yw1, }yw
                                                                          that, the, he, it
            zYtw, Dhu. 112                                                VJ; TSP; KG pl93; MSP p56; MDii p215;
 11283 zy-w B, S                                       >kjJ^~>              BSTBL p77; SCE p76; Frag. Len. pi 13
       z(s)yu (zy-w) =»Sryw, jyw                                   11294 zk'nyh B                                ? JLi+ljj**
       very much                                                         zkane ?
          VJ 65e; TSP 2.894; MSP bl68                                    musician girl, singing girl

 11284 zy-w      B                                   jux^c-^w             BSTBL, Dhy. 287; "prostitute" TSP 5.43 n p201
         zyu (zy-w) ©nom. -y; nom.f. -}; abl. f. -y\ pi.           1 1295 ZKh S, B            (jy^ y^ ^)(>>)^T <3\ < jT
           -r*; adj. & adv. =*zwy, 8ryw, jyw                              xa ©Idg. pron. art. f. sg. & nom. ace. pi. -»x\
         hard, severe, cruel, difficult
         TSP 13ii 9, 3.39, 9.83n pl93; STii 1.75, 5.24                    the, she, they, them
           p602; C2, 69R22 & pi 97-8 v ace. z7w used as                   STiiyh,7.1y\3, *xh
                                                                                          21, 24; MSP p56; KG pl93; MDii
           adv.                                                             p215; Frag. Len. pi 13
                                                                   1 1296 ZKn S, B            (jy> ^<^t jj)(j*)J oT < jT jl
11285 zy-w       C =» zwyt, zwy, zy-w
                                                                         awen   ©Idg. pron. art. gen. dat. m. sg. -^}wyn,
                                                                           wyny(y)
11286 zywsk- B                               3^^f\^
      zyusk ©ob. -y; ace. -h>; pi. -ty =»zwxsq-,                         that, of that, the, his
        Srywsk, jwxsk/q
      disciple                                                           TSP; VJ; BSTBL; SCE; KG pl93; MSP p56;
                                                                           MDii p215; Frag. Len. pll3
         BSTBL, Dhy. 15, Dhu. 129, 207, 274; GMS 285
##### leaf 528
461


11301 ZKyHMw       S                               jli,U          C2, 104R3: BSTii 832.3
       wesan(u) ©Idg. =»wysnw                               11314 zmb M                                      X^U
       their                                         ^            zamb (zmb}) =*zmpy, znp(h)
       Anc. Lett. 2, 4, 6; S W, CI, 1991, 182                     shore
                                                                  GMS 524, 1159; Hen. Tales. 472.32; STii 1.2a,
11302 ZKysn(w) S                                   jt*,u
                                                                    GMS 424 n 1; S W, C2 n pl08       ' JI^JJ^
      wesan(u) ©Idg. =»wysnw
      their                                                11315 zmb* C=» zmb
      Anc. Lett. 3; S W, CI, 1991, 182                     11316 zmb n» yrP
                                                                 zamb na yarj3
11303 ZKZY(n) B, S                   (j*)4&7 ^^                  endless
      keti ?, xo-ti ? ©Idg. Zkny ^ky\ qyt, -n
                                                                 MSP e22                                      cJj <jU j
      who, which
      STii p602; SCE p76, BSTBL p77                        11317 zmn-    B, S
                                                                 zamn (zmnw, zmnh) ©<*zaman(a); <*zamanu
11304 am'k B                                       jl=^j
                                                                   ©nt. n. nom. ace. zmnw(hh ob. zmny(h), -yyh,
      zame ©Khwar. zmkync        =*zmyy, >zmy
      winter                                                       -(w)y\ pi. zmnth -^zmnw, jmnw, zmn(w)
      SCE 103                                                    time
                                                                 GMS 512 n 1; S W, BSOAS 1979, 341.37; VJ
11305 zm'qycq C                        u^> j? ^j--^                pl23; TSP p279; STii 9.14, 16; SCE 2; BSTBL,
      zmakick ©ob. -y; pi. -/ ^zm'y'yck*
                                                                   Dhy. 196, 249, 349, 397; Frag. Len. pi 13; MSP
      temptation
                                                                   b 138; Anc. Lett. 2.50, zmmh
      BSTii 905.4: C2, 57V4, 83R3
                                                           11318 zmncyk' B                                          ^Uj
11306 zm}t- S                         o-^<->^j *o>>» jT
      zmat ©pt. su pres. zmyy-\ perf. z^mtd^r                    zam(a)ncik ©in compd. «*trzmncyk())
      0o)try, (to)be tempted                                     TSP  5.55
                                                                 (o/)time
      Anc. Lett. 3.8 apud. Benv. TSP n p221
                                                           11319 zmnh    S =4 zmn-
11307 zmWk     B                                   <^jy>
##### leaf 529
                                                                                                                                 462
 zmwxtwy                                                                      body

        shore, river bank                                                    zinak   =4zyn}kh, znw
        C2, 87 VI 1 n pi 08.269; ace. zmpw, STi 77.9;
            zmpy, Sund. AoFiii 57                                            VJ 1106, 1261; Benv. J A 1939, 275; VJ ^*>-Ui
                                                                                                                      n p97t^jtjh

 11326 zmwxtwy        M    i^j^S)^ ^^ j v^-w j3J <jjj *La\ j           11338 zn'kh2 B
                                                                             (o)znak
                                                                               >zn>k(h),©<*zndka
                                                                                         jn>     ^pw       zn'kh, zn'kh,
        zmuxtuy ^'zmwyty rwc                                                 knowledge
        twenty-eighth day of the month
        Hen. JRAS 1945; Fasts. 151.5 etc.                                    SCE 132, 43; W-Lii 572                               lib
 11327 zmy       B                             a^a <^>*a icz-j*        11339 zn'kh B
        zme/I Ozm) ©Yaghn. izm-, Khwar. >zm;                                 knowledge
                                                                             znak (zn'kh) =»jn\ zn*kh2
          <*aizma(kah A v. aesma
        fuel, firewood                                                       GMS 264; TSP 9.80, 81, 94, 14.35; BSTBL, Vim.
                                                                               80, 112, Dhu 7, 8 & etc. p77, 148
       BSTBL, Dhy. 7, Mack, n p41
                                                                      11340 zn'mnty C                                 J^Jj^Jj
 11328 zmyx      C                           (J^St)**"^                     zan-amande
       zmex
       crucible                                                              bringing forth
                                                                             STi 73.7; GMS 1100
       apud. S W, C2 n pi 77, 102R18; Mack. BSOAS
         33, 115, zmyq                                                11341 zn>ndy(h)     M                                  •jqlj
                                                                            zanande
11329 zmyy M                       *                        jb~*j            bringing forth
      zame ^zmy, zm'k                                                         song
      winter                                                                 GMS 1068; zn& "children" Sund. 1994, 45.19
                                                                      11342 znd      M                     (^^J-'J^^'^o'/
       BBB pl40; W-Lii 547.8
                                                     jjuf j <Jp' j          zand ©<Av. zanti ^zntwkrdi), znt1
11330 zn-' B, M, C
      zan ©<Av. zan-         ©trans. & intrans. perf.                       GMS 525; Hen. LW 104                              o>lj
         znd>r- ^znd'r-, jn-                                          11343 zndV-    C
       Go)give birth, (to)bc born
```


## [2026-09-05T20:46:06.185Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### BQT v1 leaf 244 (p~34)\"; awk 'BEGIN{RS=\"\\f\"} NR==245' BQT_v1_pages.txt | head -50"
}
```


## [2026-09-05T20:46:06.936Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### BQT v2 leaf 452 (p~995)\"; awk 'BEGIN{RS=\"\\f\"} NR==453' BQT_v2_pages.txt | head -50"
}
```


### [2026-09-05T20:46:07.883Z] TOOL RESULT

```
##### BQT v1 leaf 244 (p~34)
در دل کسی‌جای کند ؛ وباین معلی بازای نفطه‌دار
هم آمده است .
11 ۱ مه بسکون زای نقطه داره یمعنی
آرزو و خواهش با ابرام و حرص باشد در جمیع
امور - ونام جابی ومقامی ونام شهری و مدینه‌ای
هی سب .
وه مکی زان طرسی. 2 نی
آسودن باشد - وامربآسودن هم هست معنی بیاسا
وأسوده شو .
]راد ؟
در توابع نشجوان (۱) و مردم آنجا سفید پوست
میب‌اشند ؛ و شرابآنملك شهرت عظیمی دارد-
و عطلق بی عیب وا کویند یعنی هر چیز که
آن عیب نداشته باشد ویی‌فقد ومجرد - وخلاس
شدم ونجات‌افته را نیز کویند چنانکه ا کر کسی
بر وزن آباد . نام شهرست
کوید «فلان را آزادکردم» یعنی از فید بندکی
فارخش ساختم و خلاصش کردم - و سوسن سفید
را نیز آزاد گونند بسبب آنکه او از علت کجی و
تکیه بشاغ دیگ رکردن فارفت - و درختی حم
هت ۴ که آنرا در هندوستان «یکاین» میگوبند
سو درخت آرون (۲) و کاوری را هم گویند - و
حرختی را نیز که میوه ندهد ؛ و همانا که سوسن
وسرورا باین اعتبار آزاد خوانند. ونام درخت‌سرو
هم هست . گویند از حکیمی پرسیدنکه‌چندین
درخت امور و پرومند هت چرا هیج يك‌راآزاد
تمگوند مگرسرو راکه هیچ‌تمره وعیوه ندارد؛
کفت: هربك را ضلی‌معین ووقتی معلوم اس تکه
کاهی تازماند و گاهی پژمرده و سرو از این ها
ارت و پیوسته تازه و نیکو باشد پس صفت
آزادگان این است - ونزد محفقن کی اس ت که
از تعلقات ظاهری و باطتی خلاص باید ؟ . 3
" بشت ۲ ص ۲۰۶۵ > :
چنین داد پاس خ که آز و باز
بر نکند وقانع نسازد. ۴
فردوسی
. > ,۳۲۵ اونئوالا‎ ۶ , ٩۹
- یز آزاد یکی از مهمترین مافیان
استخوان دار است و گوشت آن لذیذ است
۲ 6۲00۸۵ ۶921100 نربه‌انی ۱۳۷۲ >,
٩2100 225‏ « فرهنگ روستائی۱۱۲۰ »؛
آزاد ماهی بزر کترین توع ماهی فلی‌دار است
بند ۳۶» تلم بعض افراد ایران باستان « نام نامة
و
```


### [2026-09-05T20:46:09.914Z] TOOL RESULT

```
##### BQT v2 leaf 452 (p~995)
   ‫مهوت‬

‫دم ‪ = 1‬بروزن‌ميم ‪ ۰‬چرکی باشد که‌از‬                                   ‫و بمعنی ليك بخت هم هست که عربان وبحك‬
                                     ‫جراحت برود ‪.‬‬                    ‫خوانند ‪ ۱‬؛ وباین‌معتی بجای حرف اول واونیز‬
                                                                                                                ‫تب‬       ‫ات‬

 ‫بفارسی کر گدن‌خوانند وکوندشاخی برسربینی‬                              ‫رکا ؟ ه بروزن‌زیبا‪ ,‬مطنوب ومحبوب‬  ‫ی‬
                                                  ‫دارد ‪۲‬‬
                                                                                                 ‫و معشوق باشد ‪.‬‬
‫بر وزن شیراز » نوعی از‬          ‫ر بمار س‬                              ‫ریگاسه ‪ ۴‬م با ای مجپول سوین‬
 ‫جام لطیف بود و آنراکیمیا باکاف فارسی هم‬                              ‫بی‌نقطه بروزن بیجاده » بزبان اهل مروخاریشت‬
                                                  ‫وف‬                                 ‫کلاترا کونند و بعربی قنقذ خوانند ‪.‬‬
                                                                     ‫زیرکاشه (‪ ۱۸۳‬د با شین نقطه دار ‪.‬‬
 ‫باشد که دروقت گداختن در کوره‌م‌ماند وبهنگام‬                         ‫بر وزن و معنی ریکاسه است که خارپشت کلان‬
                          ‫يتك زدن ازآن مر یرد ‪.‬‬                                                              ‫تبرانداز باشد ‪.‬‬

 ‫باکاف‌فارسی ‪ ۰‬بروزن‬     ‫‪ ۲‬هننگ س‬        ‫رلم‬                         ‫ریگ روان = بکس کاف فارسی »‬
 ‫نیمج استکه بیخ خرغول باشد »‬     ‫هر‬‫آعنی‬
                                      ‫وم‬                              ‫ریگی است که درجانب جذوب میباشد و پدوسته‬
                                                                      ‫روان است ‪ .‬گوند آن ریگ تمام نقره است‬
   ‫وآن چر کے وریم زخم را پاک ازد وآرهبنج‬
                                                                      ‫و هرچشمه که ازآن بر می‌آبد آبش با سیحاب‬
                                                                      ‫آميخته باشدآ ب بربالاوسیماب درزبروهرحیوانیکه‬
 ‫یمز" بکسراول وفتح‌تالك وسکون‬
                            ‫ر‬                                                             ‫اآزن آب بخورد فی‌الحال بمیرد ‪.‬‬
                                                                      ‫زریگ ریگ کنابه ازذره ذره‌باشد‪.‬‬
 ‫است که نوعی‬    ‫بمعنتی ریماز‬    ‫نقطه‌دار ‪¢‬‬    ‫انی وزای‬


                                     ‫از جامه باشد ‪.‬‬
                                                                      ‫بمعنی ماهی صقنقور‬           ‫ر نگ راده =‬
 ‫رهسفت ه با سین و عین بی‌نقطه بر‬
                               ‫ل‬                                      ‫ات ‪ » ۵‬وآن جالورست شبیه بماهی وییوسته‬
‫وزن بی‌زحمت» بلفت سربانی دوابی است کهآ نرا‬                                                                ‫در ریگ میباشد ‪.‬‬
 ‫گرم ست‬     ‫بعربی‌سمد کوبندوبتر کی‌طبلاق‌خوانند‪.‬‬
                                                                     ‫رلو = با لام بروزن بیکو‪ .‬اشخار وقلیا‬
                                                                                                        ‫ب‬
         ‫دراول ودوم > وبعضی گوبند بونانی است‪.‬‬                         ‫کضویبند ربلو شنجار است» و آن‬
                                                                                                 ‫باشد » و بع‬
 ‫ھن د بفتح اول والك و سکون ثانی‬
                              ‫ر‬                                       ‫رستنیی باشدکه بر کهآن سیاه وبیخش سطبربود ‪.‬‬
 ‫ولون » محیل ومکار ودغا باز و کینه‌ور باشد‪-۱٩‬‏‬                                                                        ‫آفه اعلم‬

                                                                                            ‫)‪ (۱‬چش ‪ :‬ریخاشه ‪.‬‬

   ‫‪ = ۳‬ریکاشه(هم‪ = ,).‬رکاےه = رکاشه‪.‬‬                  ‫رك‪ :‬رایک‪.‬‬              ‫؟‬           ‫‪ -‬ر ک‪:‬ح‪٩‬‏ صفحهفبل‪.‬‬     ‫‏‪۱٩‬‬

    ‫‪ - ۹‬شکل پهلوی ‪= 0167‬‬                      ‫‪۰‬‬   ‫رك ‪ :‬سقنقور‬           ‫=‬    ‫‪۵‬‬             ‫= ریکاسه (ھ‪ .‬م(‬      ‫‪۳‬‬

 ‫و محفف‬     ‫مصحف‬        ‫رك ‪ :‬ریم آهن ‪ ۰‬رم آودكث »> رىمن ‪ ۰‬زریمه ‪۷.‬‬                            ‫بلوچی ‪ « 0۲6۲‬هو شمان ‪۴۹‬‬
```


## [2026-09-05T20:46:23.450Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'زادن' in p or 'زائو' in p or 'زاییدن' in p:\n        print('leaf',i,'printed~',i+543, [w for w in ['زادن','زائو','زاییدن'] if w in p])\nEOF"
}
```


### [2026-09-05T20:46:25.228Z] TOOL RESULT

```
leaf 114 printed~ 657 ['زادن']
leaf 209 printed~ 752 ['زائو']
leaf 339 printed~ 882 ['زائو']
leaf 456 printed~ 999 ['زادن', 'زاییدن']
leaf 457 printed~ 1000 ['زاییدن']
leaf 460 printed~ 1003 ['زادن']
leaf 464 printed~ 1007 ['زادن']
leaf 468 printed~ 1011 ['زادن']
leaf 508 printed~ 1051 ['زائو', 'زاییدن']
leaf 510 printed~ 1053 ['زادن']
leaf 511 printed~ 1054 ['زاییدن']
leaf 562 printed~ 1105 ['زادن']
```


## [2026-09-05T20:46:30.597Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==457' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-05T20:46:32.076Z] TOOL RESULT

```
  ‫~~‬                                                                                                                       ‫زایدن‬
 ‫که نقیض بنده باشد ‪ ۴۱‬و بممنی فرزند آدمی‬                                          ‫هت ‪ -‬ونام شعبه‌ایست از موسیقی ‪.‬‬
‫زکارةبنیوده شده از اسب و خر و غیره نیز‬
                                     ‫و‬                             ‫رالیدن ‪ = ۲‬پروزن خوایندن‪ ,‬به‌عنی‬
‫ماضی‬     ‫و‬    ‫نمعتی زاییدن ‪۱‬‬       ‫و‬    ‫‪-0‬‬      ‫‪ ۲‬مده است‬
                                                                                  ‫موصوف شدن باشد هفتی اصزفات ‪.‬‬
‫زابیدن هم هست بعنی زایید ‪ -۱۷‬و بمعنی سن‬                            ‫راج س بر وزن باح ‪ ۰‬معرب زاکه ‪۴‬‬
‫را تفر‬   ‫سااشورده‬      ‫هم گفته اند لهذا مردم‬          ‫سال‬   ‫و‬
                                                                   ‫است‪ » ۴‬وآن جوهری باشدکانی شبیه بنمك ‪۴‬۔‬
‫«بزاد برآمده» خوانند ‪ -‬ودر عربی توشة راه را‬                        ‫نوزابیده را لیزتا هفت روز زگاوحینده ؛‬
                                                                                                         ‫وزن‬
                                               ‫گونند ؟‪.۷‬‬                   ‫و بابن ممنی با جیم فاردی هم آمده اتر‬
 ‫راد خو ‪ ۴‬بخاای نقطه‌دار (‪ )۱‬بر‬
   ‫وزن نازیو ‪ ۰‬پر فرتوت سالخوزده را گونند ‪:‬‬
                                                                    ‫شادی وجشن وسوری باشد که در هدگام زابیدن‬

 ‫ازدخور‪ -۱‬با واو سدوله و سکون‬                                                                      ‫زنان وابام ولادت کنشد ‪.‬‬
 ‫رای فرشت ‪ ۰‬سمعتی زادخواست که بیرسالخوردءٌ‬
                                                                    ‫راچه یه بر وزن یاچه » بمعنی دوم‬
 ‫یشندومعنی محذف واومعدوله‌هم گفته‌اند‬
                                    ‫ابا‬
                                      ‫فرتبوت‬                        ‫زاج است که زن نوزاییده باشد * وبا جیم ابجد‬
                                       ‫که»زادخر باشد ‪.‬‬                                                        ‫لمز درست است ‪.‬‬

 ‫رادخوست ‏‪ ۰٩‬با واو ممروف بر‬                                         ‫دمرخت‬
                                                                         ‫راخل ‪ -‬بر وزن داغل ‪ ۰‬نا‬
 ‫وزن نازیوست * بمعنی زادخور است که پبرسال‬                         ‫زفوم است؛ وىجای خای نقطه دارجیم همگفتها ند‬
 ‫رشخصی را نز گفته‌اند کهچىزى‬                 ‫باشد ك‬   ‫حورده‬                       ‫‪ ۰‬أله اعلم‪.‬‬            ‫ولیکن به‌عی در<ت‬

 ‫کم خورد وضعیف ونحیف و نانوان شده باشد ‪-‬‬                            ‫خورش‬       ‫مخفف زار‬           ‫‪ ۸‬د‬    ‫راحو رش‬
 ‫و شخصی را نیز گونند که هر چه دارد صرف‬                              ‫است بمعنی‌زلبکه طمام اندك خورد و کم‌خورباشد‬
                                   ‫کند ‪.‬‬                            ‫وعرب آنزنرا قتین ‪٩‬‏ کویند بافاف ونای قرشت‬
                                                                                                                 ‫‪.‬‬       ‫من‬
                                                                                                                          ‫کزن‬
                                                                                                                            ‫بر و‬
                                                                    ‫آزاه است‬       ‫راد »ەر وزن باد ‪ .‬مخفف‬


                                                                                               ‫(‪ )۱‬چك‪ :‬باخا۔‬
         ‫‪.‬‬   ‫‪ :‬تفس‬     ‫رکه‬    ‫‪۴‬‬               ‫‪ :‬زاکه » زاغ ‪.‬‬       ‫رکه‬        ‫‪۴‬‬            ‫‪.‬‬    ‫‪ :‬زاب‬    ‫رک‬          ‫‪۱‬‬

   ‫‪ - ۴‬در اروپای قرون‌وسطی [نا‪ )(017011۷‬وفرانسوی[‪ « 01۳01۷‬لرککه ‪ .‬تاریخ طب<‬
    ‫® _ بهلوی ‪ (22‬دینکرت‪ .‬چاپ مدن ‪۷٤۷‬‏ و‪۹۷‬‬                                          ‫>‪.‬‬         ‫‪۹۲۱‬س‪۳‬‬
                                                                                                   ‫‪ ۰۱‬لكث‬                 ‫‪4‬ص‪۷‬‬‫‪۱‬‬
   ‫) اسشق (‪oi‬‏ ‪ ٠‬فقس ‪ :‬کیلکی ‪( 9222‬فرزند » بجه) ‪.‬‬                              ‫‪.‬م(‪).‬‬
                                                                                   ‫هچه‬
                                                                                     ‫زا‬            ‫) =‬    ‫زاا(دن‬
                                                                                                               ‫از رشه ز‬
  ‫‪:‬زاح سور‪.‬‬     ‫رکه‬          ‫‪۵‬‬    ‫طری‬    ‫( ) صاب‬       ‫اولاد واحفاد‬           ‫‪770-۷62‬‬          ‫‪ ۰‬طبری‬    ‫‏‪ ( zaak‬کود کك)‬


               ‫رك ‪ :‬زارخورش ‪.‬‬           ‫‪۵۸‬‬             ‫رك‪ :‬زاح‪.‬‬      ‫‪-‬‬    ‫‪۲‬‬         ‫سور‪.‬‬       ‫رکه‪ :‬زاج »‬        ‫‪-‬‬   ‫‪1‬‬


   ‫زادسر وه‬    ‫ازاد‪.‬‬     ‫رل‬                  ‫«منتهی‌الارب»‪.‬‬     ‫مرد کم طعام دابی طعام»‬         ‫«ونن‪...‬‬   ‫‪(-‬عر)‬       ‫‪۹‬‬




   ‫‪( -۴‬عر) «زاد » توشه ؛ ازادة ونزوید »‬                                  ‫‪ 0‬رل ‪ :‬زادن » زایدن ‪.‬‬                            ‫زادمرد ‪.‬‬
```


## [2026-09-05T20:46:45.490Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'قرمز' in p:\n        print('pdfpage',i,'printed~',i+1207)\nEOF"
}
```


## [2026-09-05T20:46:46.683Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== PHD zadan/zad ==\"; grep -n \"^zād\\|^zādan\\|^āzād\\|^frazand\\|^frazend\\|^nizād\" PHD.txt PHD_mackenzie.txt | head -20\necho \"== CHEUNG zan ==\"; grep -n \"ZAN\\|\\*zan-\" CHEUNG.txt | head -15"
}
```


### [2026-09-05T20:46:47.113Z] TOOL RESULT

```
pdfpage 163 printed~ 1370
pdfpage 291 printed~ 1498
pdfpage 319 printed~ 1526
pdfpage 336 printed~ 1543
pdfpage 672 printed~ 1879
pdfpage 693 printed~ 1900
```


### [2026-09-05T20:46:47.175Z] TOOL RESULT

```
== PHD zadan/zad ==
PHD_mackenzie.txt:2376:frazand [pr~nd I M frzynd, N farzand] child, son, offspring.
PHD.txt:356:frazand [prznd | M frzynd, N farzand] child, son, offspring.
== CHEUNG zan ==
```


## [2026-09-05T20:46:52.541Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==320' incoming/BQT/BQT_v3_pages.txt | head -50"
}
```


### [2026-09-05T20:46:54.304Z] TOOL RESULT

```
[pdf page 320]
روا ۱ قربطس
کنده باشد و در هر جای از آن قدری آب | بمعنی هشتاد سال است و ‎AS gam‏ هر قرتی
ایستاده باشد - و جوبی را نیز گوبند که آنرا ]| سی بال میباشد - و در عرمی شا کاو وشاخ‌بز
توکنده و احداث کرده باشند . و غیر آن - وگروه - و زماله - و هم سال -
رهز ۱ ‎Ge‏ اول و میم وسکون | و هم زمانه - و طرف روی و طرف سر و موی
‎ft‏ وزای نقطه دار. چیزی است که بدان‌چیزها | تفه ( ۲ ) شده - و آنچه در ‎Ole‏ فرج زنان
رنگ کنند ( ۱) وگویند قرمز جانوری است ‎ashe‏ د و متام و طوف بل لاب وقنی
کوچك و بر بوتهای خار می‌شیند آنرامیگیرند ‎BI‏ برمبید - و تیغ قتاب را نیز
و خشك‌میکنندومربی دودالسبافین خوانشد ۴ - کوش ۱
و حبی ‎Ss‏ هم هنت ‎atl‏ عدی و ‎BUT‏ قر فیاك » بنم اول و ثانی بر وزن (۳)
قرمز ‎LT SI. oS‏ در ابریشم سرخ کشند | زرنباد ؛ کراوبة صحرائی است ۴ . #
و بر محموم آویزند تب ازومفارقت کند و شفا قر نفل بستافی - درائی اس ‎TS‏
‎atk‏ ۲ فرنجمشك خوانند 9 و آن بالنگوی صحرائی
فرهزی‌دود - ‎cal gis Pal‏ | است و بعربی بقلة الضب خوانند. بواسیررا نافع
که پیش از طلوع آفتاب و بمداز صبح پهم‌میرسد. | است .
‎of‏ بفتح اول و سکون ثانی و نون» 5 ‎gael OV pela‏ اول و سکون‌نانی
(۱) چك : میکنند . (۷) چش : بافته . (۳) چك : بوزن .
)2( چش: قرنطیی ()
‎Y‏ قرمیزهالممجم‌چاپ مدری ص۲۲4 ‎ay‏ ازسانسکریت هژابا ۳۰۵» و از عربی وارد
فرانوی شده ‎kermés‏ . ۴ - قرمز اسلا ‎gue‏ دارای فطماتی خارداراطلاق میشود.
‎Lay‏ آن ریزتر از مادینه و دارای پر است و د رکیسه ای نرم زیدکی میکند و نمونه کامل آن
فرمز ملون ( ‎(kermes baphica‏ است «لاروس بز رکث» و ‎Sy‏ : الجماهر ص ۳۷ .
‎gle Ly - ۴‏ عربی است . رك : منتهی‌الارب , اقرب‌الموارد. محیط المحیط » دزی.
۴ - قرنفاد ]03۲۷ (کروبا) « دزی ‎Ye‏ ص۳4۰ قرنباد نام فارسی کرویابری است

«فولر یآ[ . ۷۲۳ «عقار ۱۹۵ ۵ - فرتفل بستانی = افرنجمشك « دزیجس*۳4*.
۲ - در بونانی ۳12۳6۵0 بمعنیعقل و هوش است ‎UBB‏ متن مصحف لفظی و معنوی
«فرنیطی» است .

‎SBA +‏ - بقتح‌اول ودوم وضم‌سوم ‎karudphulon st yj!‏
‎Ij?‏ با ۳۰۷ «عرمزدنامه ص ۰۱۵۹ «تضس» . بعی اصل‌کلمه را هنه‌ی
نوشته‌اند «آداب‌اللفةالمرییه ج | ص۶۱ «نقی‌زاده. ‎me‏ با ‎SLIT‏ 4
شمارة +س۲۲٩‏ درهندی ‎Spe OS?‏ (بمعن یگ لکوش) ‎oS]‏ بمعنی
کوش و پپول گل است] ووجه تسمیه آنکه :نان هند از ‎SAT eas‏
گوشواره بگوش نکنند. بجای آ نگل میخگه ‎Players‏ گوش‌میگذارند
تابهم نباید« فرهنگه نظام*قرنفل,میخك که‌باربا ‎BCs‏ درختی‌است درجزایر 1
هند ‎oo Slay‏ «منتهی الارب» .گل فرنفل 8۲9۷0۳۷0118 کلی ‎col‏ قرتفل
از دستة میخك‌ها )5,55 قرفلیان ‎IS?‏ گلاب ص ‎PONE‏
```


## [2026-09-05T20:46:54.424Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== PHD azad/zadan ==\"; grep -n \"azad\\|āzād\\|zād \\|zādan\\|nizād\\|zāyišn\" PHD.txt | head -20\necho \"== CHEUNG give birth ==\"; grep -n \"to give birth\\|be born\" CHEUNG.txt | head -15"
}
```


### [2026-09-05T20:46:54.487Z] TOOL RESULT

```
== PHD azad/zadan ==
155:xwarg ... add live coal. yazd ... read yazad ... N izad, yazd. yazdan ... read yazadan ..
225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
792:animal gyānwar; zāyišnīg; tame ~ dam; wild — dad.
947:bear (v.) burdan; ~ offspring zādan,
1000:birth zāyišn.
1048:born zādag, zāyišnīg; be ~ zādan.
1771:engendered zāyišnīg.
2037:free (a.) abēzār, āzād, harzag, kām- zīwišn; ~ from pargüd az.
2040:freedom āzādīh, pardazišn.
2141:gratitude āzādīh, spas, spāsdārīh, šnāyišn, šnēhr.
2167:growth ārēyišn, rēyišn; (increase) abzāyišn, abzón, wālišn, waxšišn.
2410:increase (n.) abzón, abzāyišn, fra- dahišnih, mehēnišn.
2441:injury āzārišn, azarm, wizāyišn, wizend.
2926:noble abarmanig, āsnūd(ag), (āsnī- dag), āzād, āznāwar, ēr, pēšēnīg.
3965:thank āzādīh, spās + dāštan, hangār- dan, etc.
3967:thanks āzādīh, spās; v. gratitude.
5074:zāy-! zāyišnīgi zāyišnī! zādan! 1-2zrëh zarrën | zargónih - zargon zarigomand zarig zarr(i)gar kàr-! kistárt kištant zalüg zraw- zarwan zruftan zarmānīh zarmān zardālūg zardīh zard Zardu(x)št
5221:wizāy- wizāyišnīg wizāyišn wizastan wizüdan -endag
== CHEUNG give birth ==
9580:*hauH? ‘to give birth, beget’ 
9582:*AVESTAN: YAv. hu- ‘to give birth, beget’, hunu- (m.) ‘(daévic) son, offspring’ (Y 
9594:*SANSKRIT: sav’ ‘to give birth’ (RV+), sünú- (m.) ‘son, offspring’ > EWAia II: 714, 
9597:«PIE *s(e)uH- ‘to give birth, beget? > LIV: 538 | Pok.: 913 
11359:*NEIR: Oss. I. aryn, waryn/ard, (+ *abi- ?) D. erun/ird ‘to arrive; to be born’, ? Sariq. 
14962:*abi-) BSogd. ‘Bz’y, MSogd. Bjy ‘to grow, add’ || (+ *a-) BSogd. ’’z’y- ‘to be born’, 
14975:"z'yt, SUBJ. 3sg. MSogd. "it ‘will be born’; Impf.: IND. 3sg. BSogd. ’’z’y; Pret.: intr. IND. 3pl. 
14988:jenda ‘alive, living’, Kurd. Zin ‘life’, Tr. zayaya/zay- ‘to give birth’ 
16647:*k(a)ur ? ‘to be born, related’ 
16659:*NEIR: (+ *ui-) Oss. I. g;yryn/g,yrd, D. igurun/igurd ‘to be born; exist’ 
30019:*zanH! ‘to give birth; (pass.) to be born’ 
30021:*AVESTAN: YAv. za(n)- ‘to give birth; (pass.) to be born’ || (+ *us-) ‘to breed, 
30036:*MIDDLE PERSIAN: MMP z’y(h)-, BMP z” (YLYDWN-) /za-/ ‘to be born; to give 
30046:*PARTHIAN: z’y- ‘to give birth to; be born’, z’dg ‘son’ || (+ *a-) *()jy- ‘to be reborn’, 
30053:*KHOTANESE: уѕап- ‘to give birth to’, ysai- (pass.) ‘to be born’, ysyafi- (caus.) ‘to
```


## [2026-09-05T20:47:08.254Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30019,30075p' CHEUNG.txt"
}
```


### [2026-09-05T20:47:08.322Z] TOOL RESULT

```
*zanH! ‘to give birth; (pass.) to be born’ 

*AVESTAN: YAv. za(n)- ‘to give birth; (pass.) to be born’ || (+ *us-) ‘to breed, 
produce; be produced, bred’ || (+ *ni-) YAv. nizanta- ‘born (in one’s own house)’ 
(F730) > Liste: 67 


*zanHl 465 


Pres. them. red.: IND. 3pl. YAv. zizananti (Yt 13.15), ? YAv. "us.zizanonti (V 3.5; De Vaan 2003: 213), 
INJ. 3pl. YAv. zizanon (Vr 1.3, Vr 2.3), SUBJ. 3sg. YAv. zizanät (Yt 13.142); Partic.: pres. YAv. 
zizanäti (Yt 5.129), fut. med. YAv. zahiiamna- (Y 4.5, 24.10, Vr 11.13), perf. pass. YAv. zäta- (Y 9.5, Y 
65.6, Yt 19.56, etc.); Pass.: IND. 3sg. YAv. zaiieiti (Yt 13.16), 3du. ҮАУ. us.zaiioie (Y 9.10), 3pl. ҮАУ. 
*us.zaiieinti (У 2.41), INJ. Zeg YAv. us.zaiiagha (Y 9.13), 3sg. YAv. хайаа (V 1.17), SUBJ. 35р. ҮАУ. 
zaiiaite (V 19.5), 3pl. YAv. zaiiante (Y 11.6, Vyt 1, Vyt 3, etc.) 

*MIDDLE PERSIAN: MMP z’y(h)-, BMP z” (YLYDWN-) /za-/ ‘to be born; to give 
birth, bear’, MMP z’yn- (sec. caus.) ‘to bear, give birth to, bring forth’ || (+ *a-) 
MMP d ВМР с? /azad/ ‘noble, free’ || (+ *fra-) MMP frzynd, ВМР prznd 
/frazand/ ‘child, son, offspring’ (LW) > DMMPP: 380b f., 84b, 161a 

Pres.: IND. 3sg. MMP z’yyd, z’’yyd, z’yd, 3pl. MMP z’ynd, z’yynd, SUBJ. 3pl. MMP z’y’nd; Pret.: 
IND. Isg. MMP z’dm; Partic.: perf. pass. MMP z'd, (pl) ВМР z’t’n /zadan/, caus. II MMP z’yn’d, 
z’ynyyd; Caus.: pres. IND. 2sg. MMP z’ynyy, 3sg. MMP “z’yn’d; Inf.: ВМР zim /zadan/; Pass.: pres. 
IND. 3sg. MMP z’yhyd, 3pl. MMP z’yhynd 

*PARTHIAN: z’y- ‘to give birth to; be born’, z’dg ‘son’ || (+ *a-) *()jy- ‘to be reborn’, 
"z'd ‘noble’ || (+ *fra-) frzynd ‘child, son’ = Ghilain: 87 f. | DMMPP: 380b f., 84b, 
161a 

Pres.: IND. 3sg. z’yyd, z'yd ‘is born’, Ipl. z’y’m, 3pl. z’ynd ‘they bear’, SUBJ. 3sg. "z'y'h, OPT. 
z’yndyy; Partic.: perf. pass. z'd || (+ *4-) Pres.: IND. 3sg. "ууа, 3р1. ’jynd, "pd 

*KHOTANESE: уѕап- ‘to give birth to’, ysai- (pass.) ‘to be born’, ysyafi- (caus.) ‘to 
cause to be born’ = SGS: 112, 114 

*SOGDIAN: BSogd. zn-, CSogd. zn-, MSogd. zn- ‘to bring forth’ || (+ *abi-) BSogd. 
Bz’yn ‘offspring, son’ || (+ *a-) BSogd. ’’z’y, BSogd. ’’z’y ‘to be born, be produced, 
grow; [tr.] to beget, produce’, MSogd. "y ‘to be born’ || (+ *upa-) MSogd. рх? 
‘birth place’, MSogd. pz’tyk ‘homeland-’ || (+ *fra-) BSogd. Bs’nt’k, Bs’ntk ‘child’ 
(Sims-Williams 1983: 50; MacKenzie, SCE: 39) || (+ *ni-) nyz’tcw (f.) ‘born (in 
one’s own house)’ (Yoshida — Moriyasu 1989: 23) 

Pres.: IND. 3sg. (intr., med. ?) znty (v. Gharib 1965: 99), SUBJ. 3sg. CSogd. zn’t ‘she wants to give 
birth’, IMPV. 2pl. MSogd. znd’ bring forth’; Pret.: tr. IND. 3sg. CSogd. znd’rt, Partic.: pres. CSogd. 
zn'mnty ‘giving birth’ || (+ *a-) Well attested: Pres.: IND. 35р. BSogd. ’’z’yt, BSogd. "zyt, OPT. BSogd. 
тугу, etc. 

*CHORESMIAN: Z d (ppp.) ‘born’, z’dk ‘son’ 

*BACTRIAN: бобо, Cadyo, Cadayo ‘born, native’ || (+ *abi-) “aßlavavo (pl) 
‘descendants’ || (+ *а-) aCu- ‘to be born, be produced’ || (+ *fra-) робо, 
oopCivdo ‘descendant’ || (+ *ni-) viķaðayo ‘born (in one's own house)’ = S-W, 
Bact.: 177b, 173, 230a, 208b 

*NWIR: NP zäyad ‘is born’, Bal. za(y)-/zat, zah-/zahit, Kurd. zayin/zé- (also
```


## [2026-09-05T20:47:13.306Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30075,30110p' CHEUNG.txt"
}
```


### [2026-09-05T20:47:13.356Z] TOOL RESULT

```
*NWIR: NP zäyad ‘is born’, Bal. za(y)-/zat, zah-/zahit, Kurd. zayin/zé- (also 
pass./intr.), Zaz. zayis/zén-, Abz. zowa/zon-, Anar. (pres. 35р.) ezoya, Awrom. 
zay/-z-, Tt. (Chal za/zas, (Ram.) zā/zāst ‘to give birth’, Gz. zén-/zint, zent, Gil. 
(Rsht.) zaan/zaj-, Gur. (Kand) za/-zi, Khuns. za-/za, Mah. zö-/zä ‘to bear, bring 


466 *zanH2 


forth’ || (+ *a-) NP azad, Kurd. аха ‘free’, (Sor.) ‘free; hero’, Gz. äzzä ‘free’ || (+ 
*fra-) NP farzand ‘child, son’ (< Pth.) 

*NEIR: Oss. I. zajyn/zad, D. zajun/zad ‘to bear, bring forth [usually of animals]; to be 
born, grow’, Pash. zöwul, zézédal ‘to be born’, Yghn. zan-/zänta ‘bear, give birth; to 
be born’, (orig. caus.) Sh. (Baj.) zi(y)-/zod, Rosh. zay-/zöd, Sariq. zey-/züd, zid ‘to 
bear’, Yi. ziy-/zuy- ‘to bear a child’, Yghn. Zuta ‘child, son’ || (+ *a-) ? Wa. 
yoz-/yozd-, Zit- ‘to bear [of animals]’ || (+ fra-) Sh. rizin, Khf. rizoen, Rosh. rizén, 
Bart. razen, Orosh. rizin, Sariq. rajen ‘daughter’ 

*MISC: Par. zà-, Orm. zay- ‘to be born’ = zay-/zayok || (+ *à-) Arm. (LW) azat ‘free’ 
*SANSKRIT: jan! ‘to produce, cause to be born, create’ (RV+) > EWAia I: 567 f. 

© This root has an impeccable IE etymology. 

«PIE *бепН,- ‘to beget, bear, produce’ = LIV: 163 f. | Pok.: 373 ff. 

*IE COGNATES: Gr. үіүуорол ‘I become, come into being’, OLat. genunt ‘they 
produce’, (ppp.) Lat. nätus ‘born’, Olrish gainethar ‘to descend from, to be 


produced’, Arm. cnanim ‘I am born, bear’, Goth. airba-kunds ‘of earthly origin’ 
*REFERENCES: KPF I: 81b f.; Ivanow 1926: 422; EVP: 103 f.; IIFL I: 302a, 414b; EVP: 103; KPF II: 202; 
Christensen, Contributions I: 67; IIFL П: 277a, 555b; Andreev — PeSéereva: 367a; MacKenzie 1966: 114; 
EVS: 109b, 71b; WIMI: 74; WIM II/1: 86; WIM II/2: 639; Abaev, Slovar' IV: 284 f.; Cabolov 1997: 73; 
Werba 1997: 288 f.; Paul 1998: 320a; Steblin-Kamenskij 1999: 431; Cabolov 2001: 105; Kiefer 2003: 
210; Lecoq 2002: 125; Shahbakhsh: s.v. za(h)-Korn 2005: 109 f., 379 (passim)
```


## [2026-09-05T20:47:34.385Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -40 tools/fetch_source.py"
}
```


### [2026-09-05T20:47:34.424Z] TOOL RESULT

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


## [2026-09-05T20:47:35.456Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('AHD_watkins1985.txt',encoding='utf8',errors='replace').read()\ni=d.find('gene-. Also gen-.')\nprint(d[i:i+4200])\nEOF"
}
```


### [2026-09-05T20:47:37.485Z] TOOL RESULT

```
gene-. Also gen-. To give birth, beget; with derivatives referring to aspects and results of procreation and to familial and tribal groups. 1. Suffixed zero-grade form *gn-yo- in Germanic *kunjam, family, in: a. Old English cyn(n), race, family, kin: KIN; KINDRED; b. *kuningaz, king (< “son of the royal kin”), in Old English cyning, king: KING. 2. Suffixed zero-grade form *gn-ti- in: a. Ger- manic *kundjaz, family, race, in Old English cynd, gecynd(e), origin, birth, race, family, kind: KIND!; b. Ger- manic*kundiz, natural, native, in Old English gecynde (ge-, collective prefix; see kom), natural, native, fitting: KIND?; c. Germanic variant *kinth- in Old High German kind, child: KINDERGARTEN, KRIss KRINGLE; d. Latin géns (stem gent-), race, clan (> French gens, men): GENS, GENTEEL, GENTILE, GENTLE; GENDARME. 3. Suffixed full-grade form *gen-es- in: a. Latin genus (stem gener-), race, kind: GENDER, GENERAL, GENERATE, (GENERA-
19
ger-?
TION), GENERIC, GENEROUS, GENRE, GENUS; CONGENER, (CONGENIAL), DEGENERATE, (ENGENDER), MISCEGENA- TION; b. Greek genos and genea, race, family: GENEAL- OGY, GENOCIDE, GENOTYPE, HETEROGENEOUS; c. Greek suffix -genés, ‘‘-born’”: -GEN, -GENY. 4. Suffixed full-grade form *gen-yo- in: a. Latin genius, procreative divinity, inborn tutelary spirit, innate quality: GENIAL!, GENIUS; b. Latin ingenium (in-, in; see en), inborn character: ENGINE, INGENIOUS. 5. Suffixed full-grade form *gen-d- in Latin indigena (indu-, within; see en), born in (a place), indigenous: INDIGEN, (INDIGENOUS). 6. Suffixed full-grade form *gena-wo- in Latin ingenuus (in-, in; see en), born in (a place), native, natural, freeborn: INGENUOUS. 7. Suffixed full-grade form *gen- men- dissimilated in Latin germen, shoot, bud, embryo, germ: GERM, GERMAN?, (GERMANE), GERMINAL, GERMI- NATE. 8. Suffixed full-grade form *gena-ti- in Greek genesis, birth, beginning: GENESIS, -GENESIS. 9. Redupli- cated form *gi-gn- in: a. Latin gignere (past participle genitus), to beget: GENITAL, GENITIVE, GENITOR, GENT!, (GINGERLY); CONGENITAL, PRIMOGENITURE, PROGENI- TOR, (PROGENY); b. Greek gignesthai, to be born: EPI- GENE. 10. Suffixed zero-grade form *-gn-o- in Latin benignus (bene, well; see deu-?), good-natured, kindly, and malignus (male, ill; see mel-5), evil-natured, malevo- lent: BENIGN, MALIGN. 11. Zero-grade form *gna- becom- ing *gnda- in Latin praegnds (prae-, before; see per’), pregnant: PREGNANT!. 12. Suffixed zero-grade form *gna-sko- becoming *gnd-sko- in Latin gndsci, ndsci (present participle ndscéns, past participle gndtus, nd- tus), to be born: NAIVE, NASCENT, NATAL, NATION, NA- TIVE, NATURE, NEE, NOEL; (ADNATE), AGNATE, COGNATE, CONNATE, ENATE, INNATE, NEONATE, PUISNE, (PUNY), RENAISSANCE. 13. Suffixed o-grade form *gon-o- in Greek gonos (combining form -gonos), child, procre- ation, seed: GONAD, GONO-; ARCHEGONIUM, EPIGONE. 14. Zero-grade form *gn- in Sanskrit ja- in krmi-ja-, “produced by worms” (see k*rmi-). [Pok. 1. gen- 373.] genu-'. Knee; also angle. 1. Variant form *gneu- in: a. Germanic *knewam in Old English cnéo, knee: KNEE; b. Germanic *knewljan in Old English cnéowlian, to kneel: KNEEL. 2. Basic form *genu- in Latin genii, knee: GENICULATE, GENUFLECT. 3. Suffixed variant form *gon-ya- in Greek gdnia, angle, corner: -GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL. [Pok. 1. genu- 380.] genu-2. Jawbone, chin. 1. Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN. 2. Basic form *genu- in Greek genus, chin: GENIAL. 3. Suffixed variant form *gna-dho- in Greek gnathos, jaw: GNATHIC, -GNATHOUS; CHAETOGNATH 4, Variant form “g(h)enu- in Sanskrit hanu, jaw: HANUMAN. [Pok. 2. genu- 381.] gep(h)-. Also gebh-. Jaw, mouth. 1. Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF!, 2. Germanic *kabraz, “gnawer,” in Old English ceafor, ceafer, beetle: CHAFER; (COCKCHAFER). 3. Ger- manic *kéfalaz in Old English céafl, jaw, cheek: JOWL!. [Pok. geph-, gebh- 382.] ger-'. To gather. 1. Extended form *grem- in Germanic *kram- in Old English crammian, to stuff, cram: CRAM. 2. Reduplicated form *gre-g- in Latin grex (stem greg-), herd, flock: GREGARIOUS; AGGREGATE, CONGREGATE,
```


## [2026-09-05T20:47:51.033Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in ژنرال اکسیژن هیدروژن ژاندارم ژنراتور ناسیونال; do echo \"== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null; done"
}
```


### [2026-09-05T20:47:53.248Z] TOOL RESULT

```
== ژنرال
MON_part1.txt:3
incoming/MON/MON_2vol_Adena_v1_djvu.txt:3
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1
MON_part2.txt:1
== اکسیژن
MON_part1.txt:26
incoming/MON/MON_2vol_Adena_v1_djvu.txt:26
incoming/MON/MON_2vol_Adena_v2_djvu.txt:29
MON_part2.txt:29
== هیدروژن
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
== ژاندارم
incoming/MON/MON_2vol_Adena_v1_djvu.txt:2
MON_part2.txt:1
MON_part1.txt:2
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1
== ژنراتور
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
== ناسیونال
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part2.txt:2
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2
```


## [2026-09-05T20:47:54.050Z] TOOL CALL #41: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5enh%E2%82%81-' --note 'page 171, root Gene 1, PIE *genh1- to beget' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%85%D8%B2' --note 'page 171 node 7, Persian qermez etymology' 2>&1 | tail -3"
}
```


### [2026-09-05T20:47:56.832Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0a6a37cf6c73cf18.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a140a73c6f30c206.txt
```


## [2026-09-05T20:48:01.068Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== ژنرال ctx ==\"; grep -o -m3 \".\\{80\\}ژنرال.\\{120\\}\" MON_part1.txt\necho; echo \"== ژاندارم ctx ==\"; grep -o -m2 \".\\{60\\}ژاندارم.\\{120\\}\" MON_part1.txt\necho; echo \"== ناسیونال ctx ==\"; grep -o -m2 \".\\{60\\}ناسیونال.\\{120\\}\" MON_part2.txt\necho; echo \"== اکسیژن ctx ==\"; grep -o -m3 \".\\{60\\}اکسیژن.\\{100\\}\" MON_part1.txt"
}
```


### [2026-09-05T20:48:01.169Z] TOOL RESULT

```
== ژنرال ctx ==

== ژاندارم ctx ==

== ناسیونال ctx ==

== اکسیژن ctx ==
```


## [2026-09-05T20:48:01.548Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,80p' data/verification/sources/web/a140a73c6f30c206.txt | head -80"
}
```


### [2026-09-05T20:48:01.592Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%85%D8%B2
FETCHED: 2026-09-05T20:47:56Z
STATUS: 200
TITLE: قرمز - Wiktionary, the free dictionary

قرمز - Wiktionary, the free dictionary 

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
 Arabic 

 Toggle Arabic subsection 

 1.1 
 Etymology 

 1.2 
 Noun 

 1.2.1 
 Declension 

 1.2.2 
 Derived terms 

 1.2.3 
 Descendants 

 1.3 
 See also 

 1.4 
 References
```


## [2026-09-05T20:48:06.004Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nt=open('data/verification/sources/web/a140a73c6f30c206.txt',encoding='utf8').read()\ni=t.find('Etymology',t.find('References'))\n# find sections\nimport re\nfor m in re.finditer(r'\\nEtymology\\b', t):\n    print(t[m.start():m.start()+700].replace('\\n\\n','\\n'))\n    print('=====')\nEOF"
}
```


### [2026-09-05T20:48:07.834Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:48:10.800Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nt=open('data/verification/sources/web/a140a73c6f30c206.txt',encoding='utf8').read()\nprint(len(t))\ni=t.find('Etymology')\nwhile i!=-1 and i<len(t):\n    print('...',t[i:i+500].replace('\\n',' '))\n    print('---')\n    i=t.find('Etymology', i+400)\nEOF"
}
```


### [2026-09-05T20:48:12.433Z] TOOL RESULT

```
9639
... Etymology    1.2   Noun    1.2.1   Declension    1.2.2   Derived terms    1.2.3   Descendants    1.3   See also    1.4   References    2   Persian    Toggle Persian subsection    2.1   Etymology    2.2   Pronunciation    2.3   Noun    2.3.1   Derived terms    2.3.2   Descendants    2.4   References    3   Urdu    Toggle Urdu subsection    3.1   Etymology    3.2   Pronunciation    3.3   Noun    3.3.1   Derived terms    Toggle the table of contents    قرمز    16 languages    العربية   বাংলা   فارس
---
... Etymology  [ edit ]    PIE word   *kʷŕ̥mis    From Persian *کرمست ( *kermest ) , ultimately from Proto-Indo-Iranian *kŕ̥miš ( “ worm ” ) . Compare Old Armenian կարմիր ( karmir ) , Hebrew כַּרְמִיל ( karmīl ) , Iranian borrowings.   Noun  [ edit ]    قِرْمِز • ( qirmiz )  m    kermes insect ( Kermes ilicis , an insect found on the kermes oak that is used to make crimson dyes)   kermes dye color, a shade of red similar to crimson , scarlet or vermillion .   Declension  [ edit ]    Declension of no
---
... Etymology  [ edit ]    PIE word   *kwŕ̥mis    Borrowed from Arabic قِرْمِز ( qirmiz ) , from Persian *کرمست ( *kermest ) , ultimately from Proto-Indo-Iranian *kŕ̥miš ( “ worm ” ) , whence also the inherited doublet کرم ( kerm , “ worm ” ) .   This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term.    Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /qir.ˈmiz/    ( Dari, formal ) IPA ( key ) : [qɪɾ.mɪz]    ( Dari, formal ) IPA ( key ) : [qɪɾ
---
... Etymology  [ edit ]    PIE word   *kʷŕ̥mis    Borrowed from Classical Persian قرمز ( qirmiz ) , from Arabic قِرْمِز ( qirmiz ) , from Persian *کرمست ( *kermest ) , ultimately from Proto-Indo-Iranian *kŕ̥miš ( “ worm ” ) .   Pronunciation  [ edit ]    ( Standard Urdu ) IPA ( key ) : /qɪɾ.mɪz/    Noun  [ edit ]    قرمز • ( qirmiz )  m ( Hindi spelling क़िरमिज़ )    carmine , crimson lake   kermes ( Kermes ilicis , an insect found on the kermes oak that is used to make the deep reddish carmine dye)
---
```


## [2026-09-05T20:48:35.715Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata,re\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    t=open(f,encoding='utf8',errors='replace').read()\n    n=unicodedata.normalize('NFKC',t)\n    for w in ['ژنرال','اکسیژن','ژاندارم','ناسیونال','ژن ']:\n        idx=[m.start() for m in re.finditer(re.escape(w),n)][:2]\n        for i in idx:\n            print(f,w,'|',n[i-120:i+160].replace('\\n',' '))\n        if not idx: print(f,w,'NONE')\n    print('====')\nEOF"
}
```


### [2026-09-05T20:48:38.575Z] TOOL RESULT

```
MON_part1.txt ژنرال | سد  (پس. دارندگی و نگهبانی)] (امر.) بالاترین  درجه نظامی در نظام ایران که به تازگی  معمول گردیده است و آن برابر است با  ژنرال چهار ستاره در نظام آمریکا.  ارتسصاد: 0 ([ع.] (مسصل.) چشم  داشتن» چشم به راه بودن.   ار تضاء: 2 (ع. ف. ار تضا] (مسص‌م.)  پسندبدن» خشنود شدن. اختبار کردن؛  
MON_part1.txt ژنرال |  زن‌ده‌پوشنده]  (ص‌فا.) آنکه لباس کهنه و فرسوده در تن  دارد) کهنه بوش.   نسرال: 2006151 (۱.) (نسط.) سر تیپ»    ‌    سر  ژنرالیسم: اما (2»عجع2 ( .۰) (نط ۰) فر مانده  کل‌قوی.   زنژیویت: ۶2۱3 )۱( (بز.) التهاب و  عفونت لشه بر اثر میکرب‌ها و عوامل  خارجی که در صورت مزمن شدن تبدیل به  
MON_part1.txt اکسیژن |   مشدی حسن (اقا مشهدی حسن).  اثروپلان: 1۳0 ((.) هو اییما.   اب 0 (1.) مایعی است شفاف» بی‌طعم و  بی‌بو؛ مر کب از دو عنصر اکسیژن و تیدرژن.  نشانه آن در شیمی ۵۵است و آن به عقند ه  کار و موب تیف  مق. آتش. دریا» بحر؛ مق. خش؟ می» بر . رو ده  نهر. اشکد» سر شکث. عرق؛ خوی. سزاق»  آب دهان؛
MON_part1.txt اکسیژن | مخلوط در مقابل  جسامی که می‌تواند کلر بگیرند» مولد کلر  است و در مقابل اجسامی که با | کسیژن میل  ترکسی داشته باشند مولد اکسیژن. آب  لاساراکك: (شیم.) مانند آب ژاول تهیه  می‌شود ولی بسجای سود پتاس مصرف  می‌گر دد:0116+11,0 +۲۲۵1۲-001 +0  این محلول نیز خواص شیمیایی آب ژاول را  دارا ا
MON_part1.txt ژاندارم | که برای کمکث در  مسواقع ضصروری ساخته شود. ست  امدادی آموزشگاه‌ها: شفاخانه (فره.) بست    بستا فرهنگک فارسی معین    ۳۷    ژاندارم: پاسگاه ژاندارم.   پستا: ۱252 [آغاز و انجام] (.) بر سر کاری  رفتن که قبل ازین شروع در آن شده باشد.  ذخیره» اندوخته. بار» کرت؛ دفعه. نویت.  پستان: «قامءم
MON_part1.txt ژاندارم |  مسواقع ضصروری ساخته شود. ست  امدادی آموزشگاه‌ها: شفاخانه (فره.) بست    بستا فرهنگک فارسی معین    ۳۷    ژاندارم: پاسگاه ژاندارم.   پستا: ۱252 [آغاز و انجام] (.) بر سر کاری  رفتن که قبل ازین شروع در آن شده باشد.  ذخیره» اندوخته. بار» کرت؛ دفعه. نویت.  پستان: «قامءم (.) (جاذ.) عضوی
MON_part1.txt ناسیونال NONE
MON_part1.txt ژن  | دی حسن (اقا مشهدی حسن).  اثروپلان: 1۳0 ((.) هو اییما.   اب 0 (1.) مایعی است شفاف» بی‌طعم و  بی‌بو؛ مر کب از دو عنصر اکسیژن و تیدرژن.  نشانه آن در شیمی ۵۵است و آن به عقند ه  کار و موب تیف  مق. آتش. دریا» بحر؛ مق. خش؟ می» بر . رو ده  نهر. اشکد» سر شکث. عرق؛ خوی. سزاق»  آب دهان؛ خدو
MON_part1.txt ژن  | ل محلولی  است با بوی کلر و این مخلوط در مقابل  جسامی که می‌تواند کلر بگیرند» مولد کلر  است و در مقابل اجسامی که با | کسیژن میل  ترکسی داشته باشند مولد اکسیژن. آب  لاساراکك: (شیم.) مانند آب ژاول تهیه  می‌شود ولی بسجای سود پتاس مصرف  می‌گر دد:0116+11,0 +۲۲۵1۲-001 +0  این محلول نیز 
====
MON_part2.txt ژنرال | الکک  خارجه و وظیفهً وی دفاع از حقوق یکی از  متداعبین .در صورت ابر نیت - وده است.  رتشا فد )سول تشون کار وان او  (سیا.) ژنرال کنسول» جنرال قنسول الذ.)  (نو.) (فره.) رثیس مباشرت و ملزومات؛  رئیس ادارةٌ کار پردازی. (یشاهنگی). (نو.)  متصدی لوازم پیشاهنگی. (نو.) هر یکث از  سه تن نمای
MON_part2.txt اکسیژن | د؛ مق.  عادی. غیر عاقلانه: بی‌خردانه؛ مق. عاقلانه.  عرعمدی: غیرارادی؛ مسق. عمدی.  یر عملی: آنجه که آن را عملی کرد؛  اه  اکسیژن و ازت و کلر و برخی چون گوکرد»  کرین و فسفر جامد هستند و تنها برم  ات ون غیر فلز ها دارای جلای  فلزی هستند و اگر هم جلایی داشته باشند  جلای شیشه‌بی است؛ د
MON_part2.txt اکسیژن |   به معنی فوق. (. ص.) پایین» فرود؛ مق. زبر»  بالا.   فرو: 6۳0 [آهنین] (ص. ا.) (شیم.) ترکیبی  است از آهن با کمترین مقدار اکسیژن مانند  اکسید فرو (0ع۳) که گرد سیاه رنگی است  که از تجزية کربنات آهن در پناه هوا و یا  احیای اکسید آهن بر اثر گهدروژن بسدست  می آید.   فرو آمدن: 0۳7 (مسص‌
MON_part2.txt ژاندارم | حفاظت  راه‌ها و جاده‌ها می‌شدند تا مسافران و  کاروان‌ها را از شر قاطعان طریق محفوظ  دارند. (صفویان تا قاجاریان)؛ امنیه» ژاندارم.  فره‌نی: (۱۸۲2-۱۸۲)۵۵ [تر. ف.] نی ساه.  (هنتته) نت تفر که توارشد کی ات که از  چوب و فلز ساخته می‌شود و رنگش سیاه  است..  فره‌یراق: ۳۸۲۵۵ [تر] (امر.) حا
MON_part2.txt ناسیونال | م.) زیباه جمیل. اف  است که دختران را دهند. (.) (عم.) گربه»  نازو. اسمی است که به گر به‌ها دهند.  نازی: 22 (ص.) پیرو حزب ناسیونال  سیوسیالیست آلمان دورةٌ هیتلر.  ناریدن: «22-142: [(نوازش‌کن)] (مص‌ل.)  (ناز بد» نازد» خواهد نازید» بنواز» نازنده»  نازان» نازیده» نازش). ناز کردن اسستغ
MON_part2.txt ناسیونال | فراموش کننده»  فراموشکار.   ناسید: 2-0 آف. ۳۵ (رص.) (عم.)  دشنام گونه‌ای است که به سبدان نادرست و  نایکار اطلاق کنند.   ناسیونال: 31 (ص.) ملی» قومی.  ضح.- احتراز از استعمال این کلمةٌ بیگانه  (جز در مورد اعلام) اولی است.   ناسیو نالیست: ۱297۵021-1 (رص.) آنکه  طر فدار ملت و قوم خود
MON_part2.txt ژن  |  غرابیه: (۳9«)۵ه« (ع.] (ص‌نس. (.)  قسمی نان قندی که از آرد بادام سازند)  را   غراچه: (۵-)۸۲5۵۵( [- غرچه | (ص.) نامر د»  ژن به حریف برء» دبوث. احمق» ابله» نادان.  غرار: :۱*8 [ع.) (مصل.) گول خوردن»  فریب خوردن. (امص.) فریفتگی» غرگی.  صح.- به این معنی در عربی «غره و «غره» و  «غرور» 
MON_part2.txt ژن  |  غر یز ه. طبیعی ؛ داتی» جبلی؛ فطری. حرارت  غریزی: حرارت طبیعی که در عروق بدن  تو أم با خون وجود دارد.   غریذنگ: ۵ (- غریژن - غریزن -  غلیزن] (.) گل و لای سیاه که در بن  حوض‌ها و ته تالاب‌ها و جوی‌ها است.  غریق: بآ۲ 2 [ع.] (ص.) غرق شده؛ در آب  فرو رفته؛ ج. غرقی. (مج.) فرا گرفته شد
====
```


## [2026-09-05T20:48:48.071Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata,re\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    t=unicodedata.normalize('NFKC',open(f,encoding='utf8',errors='replace').read())\n    for w in ['ژن:','ژنرال:','ژاندارم:','اکسیژن:','هیدروژن','هیدروژن:','ژنراتور','جرم:']:\n        for m in list(re.finditer(re.escape(w),t))[:2]:\n            print(f,'|',w,'|',t[m.start()-40:m.start()+200].replace('\\n',' '))\n    print('===')\nEOF"
}
```


### [2026-09-05T20:48:50.173Z] TOOL RESULT

```
MON_part1.txt | ژن: |  را از آن اندود می‌کنند  (حلبی)؛ قلع  ارژن: 20« (.) ( گیا.) درختچه‌ای از دستة  بادامی‌ها از تيرة گل‌سرخیان که دارای  گو نه‌های مختلف است و در نقاط خشک و  کوهستانی اطراف تهران و کرج و ارتفاعات  ۰ متری و جنگل‌های طالش می‌رود.  گو نه‌ای از آن 
MON_part1.txt | ژن: | م: (تص.) انسان کامل»  شیج» پیشوا.   اکسیژن: اه (.) (شیم.) گازی است  بی‌رنگله بیبو؛ بی‌طعم» کمی سنگین ترا  هو ا. یک لیتر آن ۰۵ ۰ گرم جرم دارد.  قز ات کتفین .سول ات ورد ۱۸  درجه و فشار ۵۰ جو به سختی مایع می‌شود.  در طبیعت به حالت ترکیب و آزاد
MON_part1.txt | ژاندارم: |  بست    بستا فرهنگک فارسی معین    ۳۷    ژاندارم: پاسگاه ژاندارم.   پستا: ۱252 [آغاز و انجام] (.) بر سر کاری  رفتن که قبل ازین شروع در آن شده باشد.  ذخیره» اندوخته. بار» کرت؛ دفعه. نویت.  پستان: «قامءم (.) (جاذ.) عضوی که در  بستانداران ماده»
MON_part1.txt | ژاندارم: | با نسانه تسود با  دو ددادة خ و کت تاک   ژاندارم: رصح (امر .) سر بازی که ماموز  حفظ نطم در راه‌ها و جاده‌های خارج شهر  می‌باشد» امنیه» ضصطبه.   زاندارمری: آعح۶500 (امر.) اداره‌ای  که مأمور حفظ نظطم در جاده‌ها و راه‌های  خارج از شهر و قری و ق
MON_part1.txt | اکسیژن: |  اعظم: (تص.) انسان کامل»  شیج» پیشوا.   اکسیژن: اه (.) (شیم.) گازی است  بی‌رنگله بیبو؛ بی‌طعم» کمی سنگین ترا  هو ا. یک لیتر آن ۰۵ ۰ گرم جرم دارد.  قز ات کتفین .سول ات ورد ۱۸  درجه و فشار ۵۰ جو به سختی مایع می‌شود.  در طبیعت به حالت ترکیب و 
MON_part1.txt | جرم: | ردن. سوار شدن بر چیزی»  برنشستن. ارتکاب جرم: (حق.) کاری بر   خلاف قانون انجام دادن.   ارتکاز: ۹2 [غ. ۰] (مص‌ل.) ات شدن.  ارتکاز برقوس: گوشةٌ کمان بر زمین نهاده بر  آن تکیه کردن (برای برخاستن)» بر کمان  تکیه کردن» کمان را بر زمین فرو برده  ا
MON_part1.txt | جرم: |  کردن. (امص.) آگاهی) ج.  اعلامات. اعلام جرم: (حق.) عارت است از  اینکه وکلای مجلس يا دادستان با اشخاص  جرم شخصی را ( که دارای مقام و رتبهةٌ قابل  توجهی است) به سمع اولیای امور برسانند و  او را تعقیب کنند. اعلام جنگ: اعلان جنگث  دادن. اعلام خ
===
MON_part2.txt | ژن: | تن آن به صورت «غلیظ بندم  غلط است.   غلیژن: اهر (- غلیزن - غریزن -  غریژن - غریژنگ] (.) لجن و لای سیاهی  که در ته حوض‌ها و جوی‌ها و تالاب‌ها بهم  رسد خلات.   غلیط: ۵۱7 [ع.] (ص.) گنده» کلفت. سشر  (در شبر و مانند آن)» پرمایه؛ مق. رقیق»  بار ی
MON_part2.txt | ژن: | هر شعبه از  فراماسونری در کشوری بزرگ.  لژن: ۱0۶۵۰ (- لزم - لجن - لجم] (.) گل و  لای تبره که در ته حوض و ین تالاب باشد.  لژیون: 27 (.) در روم قدیم؛ واحدی  از سربازان (و آن در عهد سزار و دوران  اپراطوری روم شامل ۰۰۰۰ سرباز بود.)  لژیونر: (.) 
MON_part2.txt | جرم: | ۵( مج رک | (ا.) ببگار؛ کار    مسا :    مجرم: ۱0۱0 ۳۵ (افا.) کسی کث جرمی  مرتکب شده. کناهکار؛ ج. مجر مین.   محر میت. ۱۱۱0۳۵۱۱-۱ اع. (مص جد.)  ها   مچر وح: ۱۳ [ع. (امف.) زخمی شده»  جراحت برداشته زخمی؛ خسته؛ ج.  م2 ۶   محر ور: ۱۲ ۳2 (امف.) کشی
MON_part2.txt | جرم: |  رئیس  محسوب می‌گردد؛ ج. معاونین. معاون جرم:  ۱  منضمات جرم به مجرم پاری کند.  مسعاونت: رهام مت [ع. معاو نه ]  (مص‌ع.) یاری دادن» کمک کردن. (امص.)  ازع کت‌کتا: مسقام شخصی که در  وزارت‌خانه با اداره بلافاصله پس از وزیر با  رس است.   معاهده: 
===
```


## [2026-09-05T20:49:09.531Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 171 -l 171 -r 450 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg171_450 && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg171_450.png'); print(im.size)\nw,h=im.size\n# node12 box approx fraction x 0.63-0.78, y 0.36-0.41\nim.crop((int(0.60*w),int(0.355*h),int(0.80*w),int(0.415*h))).save('$S/n12.png')\nim.crop((int(0.60*w),int(0.455*h),int(0.80*w),int(0.50*h))).save('$S/n16.png')\n\""
}
```


### [2026-09-05T20:49:13.595Z] TOOL RESULT

```
(3825, 4950)
```


## [2026-09-05T20:49:15.764Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/n12.png"
}
```


### [2026-09-05T20:49:15.777Z] TOOL RESULT

```

```


## [2026-09-05T20:49:18.691Z] TOOL CALL #50: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg171_450.png'); w,h=im.size\nim.crop((int(0.60*w),int(0.40*h),int(0.82*w),int(0.45*h))).save('$S/n12b.png')\n\""
}
```


### [2026-09-05T20:49:20.570Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:49:23.022Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/n12b.png"
}
```


### [2026-09-05T20:49:23.037Z] TOOL RESULT

```

```


## [2026-09-05T20:50:00.235Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf8',errors='replace').read()\nfor pat in [r'ni\\s*-?\\s*zant', r'nizan', r'z[āa]ta-\\s*Adj', r'ä-zäta', r'azäta', r'a-z[aä]ta', r'frazainti-', r'zan-\\s*V']:\n    ms=[m.start() for m in re.finditer(pat,t)][:3]\n    print('##',pat,len(ms))\n    for i in ms: print('   ',t[i-150:i+250].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:50:02.082Z] TOOL RESULT

```
## ni\s*-?\s*zant 1
      Fnssknöcbel hinab  gehend':  andvT  . .  'ga  (IS.)  aokra *paitijinuxta  ".  .  vom  Knöchel  abwärts mit  Schuhwerk  bekleidet"  Yt.3. 64. •  j.  ni-zanta-  Adj.  'ein(d.  i.  im  Haus)''ge- boren,  ingenuus';  'um  F.  26. mp.  (Pü.)  niiami;  ai.  vgl.  iti/'a-  Adj.  'eigen'; Bthl.  IFAni.  72.  27.  —  Pü.:  nieand,  erl.: /  pa  xmiak  säyll.  —  i>  S.  PüErl. •  j,  *m-zbaya-  m.  'Anru
## nizan 0
## z[āa]ta-\s*Adj 2
    mehr  yaanie;  s.  dazu  Mndati-  No.  I.  —  lo)  S.  ä No.  18.  —  ■')  Vgl.  V.  5.  56. •  j.  "hvai!  ätSe  yaza  ajik^  FrD.  7. •  j-i  g-  yazata- Adj.  'verchrungs-,  anbetungs- würdig': humsimi^i.)  %wa  film  'Um  aia- nhaHm  dadimaidtY, 41.^.  A)imjAwr. Bezeichnung  für  alles  göttlich  Gedachte, 'Gott'*':  tal  nS  dayata  yühm  'to  (VP.) asavanS  Y.  6^.  14;  Ny.  j.  11;  —  vXs
    ich. •  j,  hu-yaona-  Adj.  (fem.  'nä-)  'an  guter Stätte  stehend' './rava$ays..yh  'na  p3r3%u.- yaeith  \tis.  39, Vgl.  ifäyaima; •  j.  'hu-yazata-  Adj.  {fem.  '/J-)  'wohl, hoch  zu  verehren':  aslm  vaimhlm . .  •tarn Yt  ly.i. Vgl.  'iKfosata-  £N. •  j.  'hu'yazata-  m.  £N.  eines  Gläubigen: •tatahe  asaonö  Yt  13. 117. Vgl.  liu/azata-. •  j.  bu-yaita-  Adj.  i)  wohl  gebetet'
## ä-zäta 0
## azäta 3
    ) pairimatöiscä  Y.J2.3;  — y^!ttg  *slrSmcS  Y.44- 3;  —  ^pl' >■«,'  ^äiayi W£«;>Ktfji-'äV.6'.33(s.  dagegen  36,  Sp.5680.); —  daMyunqm  eätanqm  azätanqm^a  YL  if). 56;  —  have  atahi   M%raica   Yt.  7j.  67; —  %ioähü  gathaha  tanmica  Y. 43.T;  — 3^ai^  syaö^anai^  hisvasca  Y.5J.  13;  — msr^tB  bpfstaca  damayäi  V,  2.3;  —  dasä aspa  aHnavaitlS  idtrtmcä  Y.^^iS;  — vokB  manatsha 
    indischen pitärah,  die  römischen  ««««■:  'sayö  hütti^ Aatqm..aigAu^qm..bUsyantqin{Sf.^^i  m.) a!'aanqmYt.i3.2\;—ä  hätqmca  anhusqfnca zätanqmca  azätanqinca  asaonqm  ilajasmiu °sayd  Y.  öj.  6;  —  aat  anyaisqm  'say!> jvanqm  narqm  aiaonqm  aojyehfi .  ,  ya^a iristanqm  "aber  im  übrigen  sind  die  Fr. der  lebenden  Gläubigen  stärker  als  die der  gestorbenen"  Yl;_j.  17;  —  visp
    n  Gläubigen  stärker  als  die der  gestorbenen"  Yl;_j.  17;  —  vispäbyö asaonibyS  *nbyS  y3  irlrüu/qm  .  .  yasia jvantqm  .  .  yäsca  narqm  azätanqm  Y. 24-5;  —  vispanqmca  änhqm  alaonqm asaoninqmla  ila  yaxamatde  °stm  Yt,  ij. 148';  —  neben  'aAs-,  *da?nä-  usw.; alaonqm  aiaoninqmla  ahümla  dafaqtnca baoiasca  urvarumca  °slmca  Y.  26'.  4;  — gai^ssca  asdsbJlca  us'tänqsca
## a-z[aä]ta 2
    te  °^pniJ'^  Y.  2j.  i;  Yt. 13.28. Pü.:  anapeTiilarl,  erl.:  ilvam/ai.  —  ■)  Statt •Vb/"  tur  '^yinf,  %26S.2l;  s.  ^Wns- No.  I. •  j.  apara-zäta-  Adj.  'als  späterer,  zweiter geboren',  hinter  EN.  'der  jüngere'  (zur Unterscheidung  von  einem  älteren  gleichen Namens):  jämäspahe  °taht  ..  mathydi.- mätihahe  "tahe  . .  urvatatnarahe  "iahe  Yt y.i27. ai.  vgl.  aparajä-  Ad
    -anl'  zu iL/ärii-uA  s.  BTHL.IF.7.70;  falsch  JSCHMIDT Plor.  3S6.)  —  Pü. ;  asarwän.  —  ■)  Hds.  "JA j.  azurtm  N.  j)3:  lies  aW/m, •  j.  a-zäta-  Adj.  (fem.  °td-)  '(noch)  nicht geboren'  sva,  '(noch)  zu  gebären,  künftig* : hätamca  aaAusämca  zätanamca  'tanamla aiamamY.6^.6',  —  irfri^u/am  ../vantam .  .  narqm  '/anqm  frasBxar^ram  saol- yattiqmY.24.y,MLi3.i7,ig.az;  —  y
## frazainti- 0
## zan-\s*V 1
    ch./  -  ih »b'-  S  ^3,  femer  Hbm.  PSt  70,  Bgm.  Grdr. /'.  632 ;  falsch  Jn.  AJPh.  10.  86. j.  zaahim  N.  6^\  lies  pasväzanlum. •  j.  'zan-  V,  'zeugen,  gebären',  von  ahuri- sehen  Wesen  ■'.  Praes.  5  *zazafi-'\  zizan-, II  ziin-i\    17  (FuL)  zqAya'*\  27  (Pass.) zaya-^^.  —  PPfP.  ssäta-  (sbes.);  'tanta-^'>, •«w/«-*';  Inf.  *sataite. 'gebären';  1)  von  Menschen;
```


## [2026-09-05T20:50:13.309Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf8',errors='replace').read()\nfor pat in ['edelgeboren','Edelgeborener','frazaiti','fra-zainti','frazaintis','frazainti','Nachkommenschaft']:\n    ms=[m.start() for m in re.finditer(pat,t)][:3]\n    print('##',pat,len(ms))\n    for i in ms: print('   ',t[i-300:i+200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:50:15.100Z] TOOL RESULT

```
## edelgeboren 0
## Edelgeborener 0
## frazaiti 0
## fra-zainti 0
## frazaintis 1
    vispam  ,mazdi  Az.2.  2-7"^  Vyt4*;  —  *ya%a*ra aSaetüS  sttm  haitimca  bavaintJmca^''  bäs-  ,buyäl  (statt  Plur.)  Aväyaonänhs  pantätüS yeintxmia  Y.  rp,  9;  —  vTspayS  afaonö  Yl/ö.  3;  —  yesnyS  ahi  .  .  yesnyö  buyi stuii Aai'ätyaica  bavqi%yäi^a^  bB^yqi%-\Y.62.i;  —  Uta  buyä  afrazaintis  Y.ii.i; yäi^a  Y,52,i;  68.22;  —  ala  Aau  apa-\  —  ta  tiS  buyqn  kumiid^Y.^^.2;  —  «ä«i ylärB  bvat'''  "da  entstand  jener  Abfluss" ,  e?  buyarps  masänä  Ny. _j-ii;  —  alsiJca
## frazainti 3
    d.)  "habt  ihr  die  Herrsch- gewalt, habt  ihr  die  Kraft  lu  tun,  o  M., . .,  o  Asa,  o  VM. . .?"  Y. ^4.5.  2)  'Ver- mögen sva.  Habe,  Besitz,  Gut,  Reichtum'; auch  mit  obj.  und  subj.  Gen.:  mä  yave imat  timiliifm  .  ,  /ratahlt  .  .  x^iiiravatti °ti/  mä  j^ä'hravaiti  äsna  frazaintii  Y. 60.7;  —  äps  °tjm  vS  jaidyämi  pauru.- sars'iqm  . .  *frazaintimla  Y.  (fj.  1 1 ;  —  °tlm pourus.x^a'irqm  .  .  ''frazaintim  Y.  68. 1 1 ; —  kahmäi  °tim  .  .  kahmäi  ainis
     M., . .,  o  Asa,  o  VM. . .?"  Y. ^4.5.  2)  'Ver- mögen sva.  Habe,  Besitz,  Gut,  Reichtum'; auch  mit  obj.  und  subj.  Gen.:  mä  yave imat  timiliifm  .  ,  /ratahlt  .  .  x^iiiravatti °ti/  mä  j^ä'hravaiti  äsna  frazaintii  Y. 60.7;  —  äps  °tjm  vS  jaidyämi  pauru.- sars'iqm  . .  *frazaintimla  Y.  (fj.  1 1 ;  —  °tlm pourus.x^a'irqm  .  .  ''frazaintim  Y.  68. 1 1 ; —  kahmäi  °tim  .  .  kahmäi  ainistim  .  . baxsiJni  Yt  10.  108— 110;  —  '/Im  jaio- yanla  . .  molu  p
      Habe,  Besitz,  Gut,  Reichtum'; auch  mit  obj.  und  subj.  Gen.:  mä  yave imat  timiliifm  .  ,  /ratahlt  .  .  x^iiiravatti °ti/  mä  j^ä'hravaiti  äsna  frazaintii  Y. 60.7;  —  äps  °tjm  vS  jaidyämi  pauru.- sars'iqm  . .  *frazaintimla  Y.  (fj.  1 1 ;  —  °tlm pourus.x^a'irqm  .  .  ''frazaintim  Y.  68. 1 1 ; —  kahmäi  °tim  .  .  kahmäi  ainistim  .  . baxsiJni  Yt  10.  108— 110;  —  '/Im  jaio- yanla  . .  molu  pas^aSta  . .  'tlm  baon  sivÜla Yt.5.98;  —  dazdi  ahmJk3tn  .
## Nachkommenschaft 3
    es  haben  zusammen  fallen  lassen,  sollte  man  mit geistreichen  Kombinationen,  mit  dem  Aufbau  ganzer  Bedeutungsstammbäume  recht zurückhaltend  sein.  Wer  Wörter  von  konkreter  Bedeutung  auf  'Wurzeln'  zurückführt, deren  Bedeutung  ja  gerade,  damit  ihnen  eine  recht  zahlreiche  Nachkommenschaft zugesprochen  werden  kann,  möglichst  farblos  angesetzt  ist,  der  täuscht  sich  selbst, wenn  er  damit  etwas  erreicht  zu  haben  vermeint  Der  Wurzelspuk  hat  ja  in  den 
      öiäH. •  j,  aipi.dahyav-  Adj.  (auch  mask.)  'der hinter  dem  Land  ist' ;  mi'i^r.in  pairi.dahyiim .  .  'yütn  (ASm.)  Yt  to.  1 44. Npü. ;  ki  pas  i  Aar  iahr  asi. ob,Google 85 aipi.dvanara- aipy-üx8ay- Bthl.  if.  j •  j.  aipLdvipiara-  Adj.  (fem.  'ra-)  "wolkig,  |  (eben)  zur  Nachkommenschaft  gelangt  ist, neblig';  xsaps  va  *tq%Tyh  °rayS  "oder  in|(jüngst)geborenliat', von FrauemnJiWiffm finsterer,  nebliger  Nacbt"  Yt//.4-  \yqm  °ram  .  .  anasaxtqm  (sd.)  V,  J
    ir hier,  o  Mami'"  V.  7. 52.  2)  'huldigen', mit  Gen.:  bm/ayai  ahurS  .  .  b>njay>n amisä  spMta  yeAha  (sd.)  IbArpff  huraohaya ". .  des  schöngestaltetem  Leib  huldigte j4AM.  . ."  Yt  10.  90;  —  *fraiaintlmca  .  . ye^hh  peurUsca  iftv/ayqn'^  naicisca  aitiha ydssiti  . .  "und  Nachkommenschaft  , .,  der manch  einer  huldigen  und  der  keiner wünschen  soll  .  ."  Y.6'5. 11. El?   VgN  Haug  SBayrAW. /Ä*.a.40,  Gdn. Slud.  /.  35,  KZ.  30.  531.  —  S.  noch  ifrixia- u
```


## [2026-09-05T20:50:27.233Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in 'https://en.wiktionary.org/wiki/%D8%A2%D8%B2%D8%A7%D8%AF' 'https://en.wiktionary.org/wiki/%D9%86%DA%98%D8%A7%D8%AF' 'https://en.wiktionary.org/wiki/mirza'; do python3 tools/fetch_source.py \"$u\" --note 'page 171 node 3, Persian azad/nezad/mirza etymology' 2>&1 | tail -1; done"
}
```


### [2026-09-05T20:50:31.505Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/04d64aaab476b27c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bddb4913624ed4ea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/146fe729d5a93da4.txt
```


## [2026-09-05T20:50:35.160Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nimport re\nfor f,label in [('04d64aaab476b27c.txt','AZAD'),('bddb4913624ed4ea.txt','NEZAD'),('146fe729d5a93da4.txt','MIRZA')]:\n    t=open(f,encoding='utf8').read()\n    print('#####',label,len(t))\n    idxs=[m.start() for m in re.finditer('Etymology',t)]\n    for i in idxs[1:4]:\n        print(t[i:i+420].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-05T20:50:37.089Z] TOOL RESULT

```
##### AZAD 13079
Etymology    2.2   Pronunciation    2.3   Adjective    2.3.1   Synonyms    2.4   References    3   Khalaj    Toggle Khalaj subsection    3.1   Adjective    4   Ottoman Turkish    Toggle Ottoman Turkish subsection    4.1   Alternative forms    4.2   Etymology    4.3   Adjective    4.3.1   Related terms    4.3.2   Descendants    4.4   References    5   Persian    Toggle Persian subsection    5.1   Etymology    5.2   Pr
---
Etymology    4.3   Adjective    4.3.1   Related terms    4.3.2   Descendants    4.4   References    5   Persian    Toggle Persian subsection    5.1   Etymology    5.2   Pronunciation    5.3   Adjective    5.3.1   Inflection    5.3.2   Derived terms    5.4   Adverb    5.4.1   Descendants    5.5   References    6   Sindhi    Toggle Sindhi subsection    6.1   Etymology    6.2   Adjective    6.3   References    7   Urdu 
---
Etymology    5.2   Pronunciation    5.3   Adjective    5.3.1   Inflection    5.3.2   Derived terms    5.4   Adverb    5.4.1   Descendants    5.5   References    6   Sindhi    Toggle Sindhi subsection    6.1   Etymology    6.2   Adjective    6.3   References    7   Urdu    Toggle Urdu subsection    7.1   Etymology    7.2   Pronunciation    7.3   Adjective    7.3.1   Related terms    7.4   References    7.5   Further r
---
##### NEZAD 5596
Etymology    2.2   Pronunciation    2.3   Noun    2.3.1   Derived terms    2.4   References    Toggle the table of contents    نژاد    9 languages    বাংলা   فارسی   Bahasa Indonesia   Kurdî   Malagasy   پښتو   Русский   Türkçe   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Relat
---
Etymology  [ edit ]    (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .)    Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ni.ˈʒaːd/    ( Dari, formal ) IPA ( key ) : [nɪ.ʒɑ́ːd̪]    ( Dari, formal ) IPA ( key ) : [nɪ.ʒɑ́ːd̪]   ( Kabuli ) IPA ( key ) : [nɪ.ʒɑ́ːd̪]    ( Hazaragi ) IPA ( key ) : [ni.ʒɔ́ːd̪̥]    ( Iran, formal ) IPA ( key ) : [ne.ʒɒ
---
Etymology scriptorium .)    Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ni.ˈʒaːd/    ( Dari, formal ) IPA ( key ) : [nɪ.ʒɑ́ːd̪]    ( Dari, formal ) IPA ( key ) : [nɪ.ʒɑ́ːd̪]   ( Kabuli ) IPA ( key ) : [nɪ.ʒɑ́ːd̪]    ( Hazaragi ) IPA ( key ) : [ni.ʒɔ́ːd̪̥]    ( Iran, formal ) IPA ( key ) : [ne.ʒɒ́ːd̪̥]    ( Tajik, formal ) IPA ( key ) : [nä.ʒɔ́d̪] , [ni.ʒɔ́d̪]    Rhymes: -aːd    Readings   Classica
---
##### MIRZA 6939
Etymology    2.2   Pronunciation    2.3   Noun    2.3.1   Declension    2.4   Further reading    Toggle the table of contents    mirza    8 languages    Français   Kurdî   Malagasy   Polski   தமிழ்   Türkçe   Oʻzbekcha / ўзбекча   Walon    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   R
---
Etymology  [ edit ]    From Persian میرزا ( mirzâ ) .   Pronunciation  [ edit ]    ( UK ) IPA ( key ) : /ˈmɪəzə/ , /ˈməːzə/    Noun  [ edit ]    mirza ( plural mirzas )    ( historical ) An educated man in India or Iran (Persia); an official , a clerk . [from 16th c.]   1788 , Edward Gibbon , Decline and Fall of the Roman Empire , VI.65 : The same success attended the other mirzas and emirs in their excursions.    19
---
Etymology  [ edit ]    Inherited from Ottoman Turkish میرزا ( mirza ) , from Classical Persian مِیرْزَا ( mīrzā ) .   Pronunciation  [ edit ]    IPA ( key ) : /miɾˈza/    Hyphenation: mir‧za    Noun  [ edit ]    mirza ( definite accusative mirzayı , plural mirzalar )    ( historical ) Mirza    Declension  [ edit ]    Declension of mirza    singular   plural   nominative   mirza    mirzalar    definite accusative   mi
---
```


## [2026-09-05T20:50:45.746Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nimport re\nt=open('04d64aaab476b27c.txt',encoding='utf8').read()\nfor m in re.finditer(r'(Proto-Iranian|Middle Persian|Old Median|āzāta)',t):\n    print(t[max(0,m.start()-250):m.start()+250].replace('\\n',' '))\n    print('---')\n    break\ni=t.find('Persian  [ edit ]')\nprint(t[i:i+900].replace('\\n',' ') if i>0 else 'no')\nEOF\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%B1%D8%B2%D8%A7' --note 'page 171 node 3, Persian mirza = amir + zada' 2>&1|tail -1"
}
```


### [2026-09-05T20:50:47.548Z] TOOL RESULT

```
ences  [ edit ]    Çağbayır, Yaşar ( 2007 ), “ azat ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 399    Nişanyan, Sevan ( 2002– ), “ azat ”, in Nişanyan Sözlük    Persian  [ edit ]    Etymology  [ edit ]    From Middle Persian ʾcʾt' ( /⁠āzād⁠/ , “ noble; free ” ) , from Old Persian *āzātah , a northwestern borrowing from Proto-Iranian *āzātah . Cognate with Avestan 𐬁𐬰𐬁𐬙𐬀 ( āzāta , “ noble ” ) , Manichaean Middle Persian 𐫀𐫀𐫉𐫀𐫅 ( ʾʾzʾd /⁠āzād⁠/ ) , and Parthia
---
no
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/web/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-05T20:50:51.947Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%B1%D8%B2%D8%A7' --note 'page 171 node 3, Persian mirza = amir-zada' 2>&1|tail -1"
}
```


### [2026-09-05T20:50:53.782Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a3c23b64ec382782.txt
```


## [2026-09-05T20:50:56.424Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nimport re\nt=open('a3c23b64ec382782.txt',encoding='utf8').read()\nfor m in re.finditer(r'Etymology  \\[ edit \\]',t):\n    print(t[m.start():m.start()+450].replace('\\n',' ')); print('---')\nEOF"
}
```


### [2026-09-05T20:50:58.151Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:51:01.228Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('a3c23b64ec382782.txt',encoding='utf8').read()\nprint(len(t))\ni=t.find('Etymology')\nwhile i>0:\n    print(repr(t[i:i+350].replace('\\n',' ')));print('--')\n    i=t.find('Etymology',i+300)\nEOF"
}
```


### [2026-09-05T20:51:02.879Z] TOOL RESULT

```
5431
'Etymology    2.3   Pronunciation    2.4   Noun    2.4.1   Usage notes    2.4.2   Derived terms    2.4.3   Descendants    2.5   References    Toggle the table of contents    میرزا    4 languages    فارسی   Kurdî   Malagasy   Русский    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Action'
--
'Etymology  [ edit ]    From earlier میرزاد ( mirzâd ) , compound of میر ( mir , “ master ” ) and the suffix ـزاد، ـزاده ( -zâd, -zâde , “ child of, son of ” ) , from زادن ( zâdan , “ to bear ” ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /miːr.ˈzaː/ , /mir.ˈzaː/    ( Dari, formal ) IPA ( key ) : [miːɾ.zɑ́ː] , [mɪɾ.zɑ́ː]    ('
--
```


## [2026-09-05T20:51:12.651Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('0a6a37cf6c73cf18.txt',encoding='utf8').read()\nprint(len(t))\ni=t.find('Root')\nprint(t[:200])\nimport re\nfor k in ['to give birth','beget','Proto-Iranian','*ǵenh']:\n    m=t.find(k); print(k,'->',t[max(0,m-200):m+300].replace('\\n',' ') if m>0 else 'NONE'); print('--')\nEOF"
}
```


### [2026-09-05T20:51:14.276Z] TOOL RESULT

```
8520
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5enh%E2%82%81-
FETCHED: 2026-09-05T20:47:56Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/ǵenh₁- - Wiktionary, the 
to give birth -> ed , but are hypothesized to have existed based on comparative evidence.   Proto-Indo-European  [ edit ]    Root  [ edit ]    *ǵenh₁- ( perfective ) [ 1 ] [ 2 ] [ 3 ] [ 4 ]    to produce ; to beget ; to give birth   Synonyms: *h₂ems- , *teḱ- , *sewH-    Derived terms  [ edit ]    Terms derived from the Proto-Indo-European root *ǵenh₁- (149 c, 0 e)    *ǵénh₁-e-ti ( thematic root present )   Proto-Indo-Iranian: *ȷ́ánHati   Proto-Indo-Aryan: *ȷ́ánHati   Sanskrit: जनति ( jánati ) ( see there for fur
--
beget -> y attested , but are hypothesized to have existed based on comparative evidence.   Proto-Indo-European  [ edit ]    Root  [ edit ]    *ǵenh₁- ( perfective ) [ 1 ] [ 2 ] [ 3 ] [ 4 ]    to produce ; to beget ; to give birth   Synonyms: *h₂ems- , *teḱ- , *sewH-    Derived terms  [ edit ]    Terms derived from the Proto-Indo-European root *ǵenh₁- (149 c, 0 e)    *ǵénh₁-e-ti ( thematic root present )   Proto-Indo-Iranian: *ȷ́ánHati   Proto-Indo-Aryan: *ȷ́ánHati   Sanskrit: जनति ( jánati ) ( see there
--
Proto-Iranian -> an root *ǵenh₁- (149 c, 0 e)    *ǵénh₁-e-ti ( thematic root present )   Proto-Indo-Iranian: *ȷ́ánHati   Proto-Indo-Aryan: *ȷ́ánHati   Sanskrit: जनति ( jánati ) ( see there for further descendants )   Proto-Iranian: *jánHati ( see there for further descendants )   Proto-Italic: *genō   Old Latin: genō ( see there for further descendants )   *ǵénh₁-t ~ *ǵn̥h₁-ént ( athematic root aorist ) [ 3 ]   Armenian:  Old Armenian: ծնաւ ( cnaw , 3sg.aor. of ծնանիմ ( cnanim ) )    Proto-Hellenic:   Ancient Gr
--
*ǵenh -> rms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.   Proto-Indo-European  [ edit ]    Root  [ edit ]    *ǵenh₁- ( perfective ) [ 1 ] [ 2 ] [ 3 ] [ 4 ]    to produce ; to beget ; to give birth   Synonyms: *h₂ems- , *teḱ- , *sewH-    Derived terms  [ edit ]    Terms derived from the Proto-Indo-European root *ǵenh₁- (149 c, 0 e)    *ǵénh₁-e-ti ( thematic root present )   Proto-Indo-Iranian: *ȷ́ánHati   P
--
```


## [2026-09-05T20:51:23.437Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf8',errors='replace').read()\ni=t.find('Zranka')\nwhile i>0 and i<len(t):\n    print(repr(t[i-200:i+300].replace('\\n',' ')));print('--')\n    i=t.find('Zranka',i+2000)\nEOF"
}
```


### [2026-09-05T20:51:25.200Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:51:29.027Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf8',errors='replace').read()\nfor key in ['zana- sb','zana- ‘','zūra','zura- sb','yaud-','LEXICON']:\n    idx=[i for i in range(len(t)) if t.startswith(key,i)][:4]\n    print('##',key,len(idx))\n    for i in idx[:2]: print(repr(t[i-250:i+350].replace('\\n',' ')))\nEOF"
}
```


### [2026-09-05T20:51:31.391Z] TOOL RESULT

```
## zana- sb 0
## zana- ‘ 4
'. Cf. also note 1. SCRIPT 9 Vi"dafarnd, one of Darius’s helpers, with f from Sy. III. Words in the official titles: aiayabiya ‘king’, with 6j from ig. vazraka ‘great’, with z from ў. yispa-zona- ‘having all men’, with sp from ku and z from j. . paru-zana- ‘having many men’, with z from j. waspa- ‘having good horses’, with sp from ky. IV. Technical words of the religion: гага ‘evil’, with z from gh. Varka-zana- \'(month) of the Wolf-Men\', with z from g; but the entire word is merely re- stored after the Elamite. V. Names of cultural materials: asan- ‘stone’, with s from Ё. [азайа ‘semi-precious '
" c£. Skt. rajaldn. рі *geus- in OP dauslar- ‘friend’, Av. 200 ‘enjoy’, Skt. gus-. pIE\x0c *uej- in OP vazraka- ‘great’, in the royal title and as epithet of the Earth, cf. Av. vazra- ‘dub’, Skt. edjra- ‘Indra’s thunderbolt’; with Med. z. pIE *jono-, OP zana- ‘man’ with Med. г, Ау. zana-, Skt. jána-; m OP vispa-cana-, paru- canü-, and (restored month-name) Varka- 2010-; OP d is seen in *wsa-dana- *wispazana-', inferred from the Elamite mi-iš-ša-da-na. pIE teghom, ОР adam ‘P, Av. azam, Skt. айт. pIE *ghosto-, OP dasta- ‘hand’, Av. zasta-, Skt. hasta-. pIE *ghal- in OP daraniya- ‘gold’, Av. zaranya-"
## zūra 0
## zura- sb 0
## yaud- 3
'nce, with non-OP z from ў or gh; ef. Gk. Yap&yya, and also Apayyiavy, with OP d. Other examples of OP d from pIE ĝ are seen in ardastina-, Ardumants, avahar|da], uradana-, dan- in adánd, vardana-; from plE gh in gaud-, Bar- diya; from pIE ĝ or gh in yaud-. For materials on these words, see Lex. s.vv. $89. PIE ki became pAr. é, and then OP ў and finally $, since 6 before 2 became $ in OP ($80); the only example is a dubious опе, paisiyd- ‘written text’, from *peik- or *poik- + jā- in nsf. ра уй DB 4.91, and perhaps as the first element of the place-name Paiiiya*uvddd- (see Lex. s.vv.). $90. PIE'
'n of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim], 138 with Wb. © stabava (as Rl. JRAS 10.310 had it), see Lex. 8.v.; not starava nor stakava. TRANSLATION OF DNa: §1. 1-8. A great god is Ahuramazda, who cre- ated this earth, who created yonder sky, who cre- ated man, who created happiness for man, who made Darius king, one king of many, one lord of many.  — $2. 8-15. 1 am '
## LEXICON 4
't of this book on the web at http://books.goodle.com \x0cien = vw es cos ut T s$ [4 ^s Ж $^ Ido" PH 4 22 ra 2} T TG 3 #29 xx 3+ xe Et бт» el P em ME эы г иф > Ad t А; Мане ur ауе. T A 5251 dC ert M s Н E { �\x0c� i тег. E EAD Мут OLD PERSIAN GRAMMAR TEXTS LEXICON BY ROLAND G. KENT Professor Emeritus of Indo-European Linguistics University of Pennsyloania AMERICAN ORIENTAL SOCIETY NEW EAV\x0cEN, CONNECTICUT 1950 — | PLATE 1 pe * SAF iiu in i ka o ЕЛ Жок Sons THE INSCRIPTION AND SCULPTURES OF DARIUS THE GREAT AT BEHISTAN Copyrighted by George С. Cameron, b\x0cy whose courtesy tt appears here FOREWORD This v'
'; SD etc. 157; XVs ete. 157. Historical Аррепфіх...................... I, The Achaemenian Dynasty 158; II, Smerdis and Gaumata 159; III, The Helpers of Darius 160; IV, The Persian Calendar and Behistan I-IV 160; The Accession of Xerxes 163. PART HI. LEXICON 107 Lexicon and Concordance 164; Numerals 215; Defective Passages 215, ADDENDA ILLUSTRATIONS e 9 c9 e «оэ» * у ostas 4d o? SS 2 o9 „э + э, to а o9 € у 9 ө à э э э > э 9 8 9 9 з 4 э э 9 + е + 9$ c э у у м o3 5 (4 Frontispiece facing page 10 facing page 151 xii 164 216 Digitized by Google GENERAL BIBLIOGRAPHY Bibliography of OP studies is to '
```


## [2026-09-05T20:51:37.397Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 226 227; do echo \"#### leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -c 1800; echo; done"
}
```


### [2026-09-05T20:51:39.330Z] TOOL RESULT

```
#### leaf 226
24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32.
Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of the Persian Empire: Elam. ma-da, АКК. ma-da-a-a, Gk. pl. Mado.
(1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2, Madam asm. DB 2.21, 82; 3.30. Mada npm. DSf 50, 54. Майа] ipm. DB 2.23. MddatSuva lpm. DB 2.23.
(2) ‘Media’: Мада пзш. DB 1.15°, 41; 2.7; DPe 10; DNa 22; DSe 21°; Рб 8°; XPh 19. Madam asm. DB 1.47; 2.22, 28f, 48f, 68, 65 bis; 3.32f; 4.20. Méddam-ca DB 1.66f. Madaiy lsm. DB 1.84, 59; 2.15, 17, 22, 28, 66 bis, 72, 92; 3.77; DBe 10f.
tman- vb. ‘think’: Av. man-yele, Skt. mán- yale, Gk. utuova ‘(I bave thought of,) I desire’, Lat. memini ‘I remember’, pIE *men-. See also manah-. maniyary lst sg. mid. (§214, 5238.1) DNb 38. amaniyazy lst sg. imf. mid. (8214, 6233.11) DSI 3f. mantydhaiy 2d sg. subj. mid. (831, $222.11, §234.1) DB 4.39 (manl. . .); DPe 20 (maniydhay, $27, 552.11); DNa 38 (maniya- [...); XPh 47 (maniyaty, without the h*: $27, $52.VI, Lg. 13.302; Hz. AMI 8.66, ApI 243-4). maniyál|taty) sub). mid. (5222.1) DB 4.50.
^man- vb. ‘remain’: Av. man-, iterative pres. manaya- (8123, $215), Gk. pvo, Lt. maneo; prob- ably specialization of pIE *men- ‘think’ (see ‘man-) in meaning ‘remain thinking. amdnaya imf. DB 2.48, 63; amünaiya ($48) DB 2.28.
mana'uwin- adj. ‘mindful, wilful, hot-tem- pered’: from manah- + -win- (§155.V), cf. Lg. 15.170, JNES 4.47 (Hz. ApI 242 otherwise, wrongly). manauvis (remade from -07, $187) пэш. DNb 13.
manah- sb. ‘thinking power, power of will’ (Jn. Iran. Rel. $70; Kent, JNES 445-7, 232): Av. manah-, Skt. m�
#### leaf 227
ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36.
EU: ET TORR ON |
INS SEE cals la pen X AN, ae ete. ЫЗ, Ses f. Av m ee Sm SN Ie e mne -
LEXICON 203
‘martiya- adj. as sb. ‘man’: -ize- extension of pIE *morios, Av. marata- ‘mortal, man’, NPers. márd, Skt. mária- (§31, $106, $122, 5242.11), ef. ~o- extension in Av. masya-, Skt. mártya- ($144.IV). See also wmartiya-, *Martiya-.
martiya nsm. DB 1.21, 36, 48, 74, 77; 2.8, 14, 79; 3.12, 22, 70, 78; 4.38, 65, 68; 5.5°, 7°; DNa 46; ОМ 16, 19, 21, 24; XPh 51. martiyà узш. "Ма 56. martiyam asm. DB 3.57; DNa 3; DNb 12, 22; DSe 3; DSf 2, 16f; DSs 2; DSt 3°; рле 2; DE 4f; XPa 2; XPb 4f; XPe 21; XPd 3f; XPf 3; XPh 3; XE 5; XV 4; A'Pa 3P; А°Не 3f; A?Pa 3f. martiyahyé gsm. DNa 4, 44; ОМ 3; DSe 4f; DSf
. 8; D8s 5^; DSt 4^; DZe 2f; DE 6; XPa 3; ХРЬ 6;
ХРе 3; XPd 4f; ХРі 4f; XPh 4; XE 7; XV 5; AlPa 5°; A?He 4f; martthya A3Pa 4f (852.VI; hardly phonetie, as taken by Morgenstierne, Ácta Or. 1.253). martiyá npm. DB 1.571; 4.80, 82; DSf 47, 49, 51, 52, 54. татітуй apm. DB 2.77; 3.48, 50, 74, 90, 91. татйуйтат gpm. DB 4.87. martiyaibiš ipm. DB 1.56f.
? Martiya- sb. ‘Martiya’, a Susian rebel: Elam. mar-tiia, АКК. mar-t-ta; same аз 'martiya-, specialized as man’s name (§168.Ib, $164.III; but ef. HK Iran. Eigenn. 13-4, Phil. 66.183-4, ApKI 1.54, 2.26). Martia nsm. DB 2.8; 4.15; DBf 1. Martiyam asm. DB 2.12f.
mard- vb. ‘crush’: Av. marad- ‘destroy’, Skt. mrd- ‘rub, crush’, Lt. mordet ‘bites’, pIE *merd- (Foy, KZ 35.48). See also Marduniya-.
vi- + mard- ‘destroy’: vimardatiy (830, $213) DSe 40f. wyamarda imf. (written v
```


## [2026-09-05T20:51:44.527Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 234 235 236; do echo \"#### leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -c 1200; echo; done"
}
```


### [2026-09-05T20:51:46.055Z] TOOL RESULT

```
#### leaf 234

#### leaf 235

#### leaf 236
```


## [2026-09-05T20:51:49.616Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i,p in enumerate(t):\n    m=re.search(r'LEXICON (\\d+)|(\\d+) OLD PERSIAN',p)\n    if m and i>220: print(i, m.group(0), p[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:51:51.589Z] TOOL RESULT

```
leaves 232
222 LEXICON 199 -. — fra&aram asn. XPf 26f, 37. Fraéda- sb. ‘Frada’, a Margi
223 200 OLD PERSIAN 1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1
225 202 OLD PERSIAN BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; D
227 LEXICON 203 ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80
```


## [2026-09-05T20:52:02.894Z] TOOL CALL #66: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; grep -n -o \".\\{80\\}zana- adj.\\{200\\}\" $S/kent.txt | head -5; echo ---; grep -n -o \"vispazana.\\{200\\}\" $S/kent.txt | head -3"
}
```


### [2026-09-05T20:52:04.849Z] TOOL RESULT

```
---
```


## [2026-09-05T20:52:08.467Z] TOOL CALL #67: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 - <<EOF\nt=open(\"$S/kent.txt\",encoding='utf8',errors='replace').read()\nprint(len(t), t.count('\\f'))\nimport re\nfor m in list(re.finditer(r'zana-', t))[-6:]:\n    print(repr(t[m.start()-200:m.start()+300].replace('\\n',' ')));print('--')\nEOF"
}
```


### [2026-09-05T20:52:10.453Z] TOOL RESULT

```
903299 0
' 5°; Ada 4, Аас 4 (iispa db, $55.1);  A?Ha 6°.    vispazana- adj. ‘containing all (kinds of) men’  ($101.09): borrowed in Elam. mi-iš-ša-da-na,  from the OP form *visadana-: Med. vispa- ‘all’ +  Med. zana- ‘man, human being’ ($9.11, §88, $90).  uspazananim gpf. DNa 10Ї; DSe 9f; DZc 5.    LEXICON 200    Vistaspa- sb. ‘Hystaspes’, father of Darius:  Elam. mi-iš-da-aš-ba, Akk. wufia-as-pa, Gk.  ‘Loraonns. Prior element višta- perhaps pte. of  (Av.) vaés- ‘come in ready for action’ (Bthl. AiW  1326)'
--
'1, 80;  2.2f, 17, 22, 32, 51f, 72, 85, 95°; 3.4, 16, 28, 32,  33, 42, 59f, 72, 73f, 82, 87; 5.9; XPE 33f. aSiyava"  За pl. imf. ($2821) DB 1.76.    Skaurim, see under skauh-.  #а-, see under зій-.    zana- sb. ‘human being’: Av. zana-, Skt. jána-,  Gk. *yóvos ‘child, offspring’, pIE *gono- (§88, §148.-  1); in paruzana-, Varkazana-, vispazana-.    zam- sb. ‘earth’: Av. nom. 20, Gk. хода ‘on  the earth’, Lt. humus ‘earth’, Lith. zémé, pIE  *ühem- (S11, §142, 5148.1), cf. *jóhem- in Skt.  ksam-, G'
--
', 72, 85, 95°; 3.4, 16, 28, 32,  33, 42, 59f, 72, 73f, 82, 87; 5.9; XPE 33f. aSiyava"  За pl. imf. ($2821) DB 1.76.    Skaurim, see under skauh-.  #а-, see under зій-.    zana- sb. ‘human being’: Av. zana-, Skt. jána-,  Gk. *yóvos ‘child, offspring’, pIE *gono- (§88, §148.-  1); in paruzana-, Varkazana-, vispazana-.    zam- sb. ‘earth’: Av. nom. 20, Gk. хода ‘on  the earth’, Lt. humus ‘earth’, Lith. zémé, pIE  *ühem- (S11, §142, 5148.1), cf. *jóhem- in Skt.  ksam-, Gk. хб»; їп Üvàrazmi-, uzma-. '
--
'За pl. imf. ($2821) DB 1.76.    Skaurim, see under skauh-.  #а-, see under зій-.    zana- sb. ‘human being’: Av. zana-, Skt. jána-,  Gk. *yóvos ‘child, offspring’, pIE *gono- (§88, §148.-  1); in paruzana-, Varkazana-, vispazana-.    zam- sb. ‘earth’: Av. nom. 20, Gk. хода ‘on  the earth’, Lt. humus ‘earth’, Lith. zémé, pIE  *ühem- (S11, §142, 5148.1), cf. *jóhem- in Skt.  ksam-, Gk. хб»; їп Üvàrazmi-, uzma-.    [za]rlanayà with Med. z-, alternative restora-  tion for {dalrianayd; see dartana-. '
--
'($2821) DB 1.76.    Skaurim, see under skauh-.  #а-, see under зій-.    zana- sb. ‘human being’: Av. zana-, Skt. jána-,  Gk. *yóvos ‘child, offspring’, pIE *gono- (§88, §148.-  1); in paruzana-, Varkazana-, vispazana-.    zam- sb. ‘earth’: Av. nom. 20, Gk. хода ‘on  the earth’, Lt. humus ‘earth’, Lith. zémé, pIE  *ühem- (S11, §142, 5148.1), cf. *jóhem- in Skt.  ksam-, Gk. хб»; їп Üvàrazmi-, uzma-.    [za]rlanayà with Med. z-, alternative restora-  tion for {dalrianayd; see dartana-.    Zazüna- s'
--
'.76.    Skaurim, see under skauh-.  #а-, see under зій-.    zana- sb. ‘human being’: Av. zana-, Skt. jána-,  Gk. *yóvos ‘child, offspring’, pIE *gono- (§88, §148.-  1); in paruzana-, Varkazana-, vispazana-.    zam- sb. ‘earth’: Av. nom. 20, Gk. хода ‘on  the earth’, Lt. humus ‘earth’, Lith. zémé, pIE  *ühem- (S11, §142, 5148.1), cf. *jóhem- in Skt.  ksam-, Gk. хб»; їп Üvàrazmi-, uzma-.    [za]rlanayà with Med. z-, alternative restora-  tion for {dalrianayd; see dartana-.    Zazüna- sb. ‘Zazana’,'
--
```


## [2026-09-05T20:52:19.428Z] TOOL CALL #68: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 - <<EOF\nimport re\nt=open(\"$S/kent.txt\",encoding='utf8',errors='replace').read()\ni=t.rfind(\"zana- sb. ‘human being’\")\nseg=t[i-6000:i+4000]\nfor m in re.finditer(r'(LEXICON \\d+|\\d+ OLD PERSIAN)', seg):\n    print(m.group(0), '@', m.start()-6000)\nEOF"
}
```


### [2026-09-05T20:52:20.957Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:52:24.847Z] TOOL CALL #69: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 - <<EOF\nimport re\nt=open(\"$S/kent.txt\",encoding='utf8',errors='replace').read()\ni=t.rfind(\"zana- sb. ‘human being’\")\nseg=t[i-12000:i+8000]\nfor m in re.finditer(r'(LEXICON|OLD PERSIAN|NUMERALS)[^\\n]{0,20}', seg):\n    print(repr(seg[max(0,m.start()-40):m.start()+40]))\nEOF"
}
```


### [2026-09-05T20:52:26.678Z] TOOL RESULT

```
'’, Gk. ‘Todpvns. Perhaps vi- ‘apart’ \n\n\nOLD PERSIAN \n\n\n+ dar- ‘hold’, as ‘Suppor'
'zananim gpf. DNa 10Ї; DSe 9f; DZc 5. \n\n\nLEXICON 200 \n\n\nVistaspa- sb. ‘Hystaspes’'
'0-5). spa@maidaya loc. sg. \nDNb 30f. \n\n\nOLD PERSIAN \n\n\nSparda- sb. ‘Sardis’, a p'
'11, 6179.017); see also \n\n\ndi PERDER \n\n\nLEXICON \n\n\nSiydia-. For ‘happiness after'
' ha-gmata- (q.v., under gam-; §103.- \n\n\nOLD PERSIAN \n\n\nIV, $147.11): ‘City of Ga'
'XPe 12, \n\n\n> \n\n\need TRS \n\n\n= once ae \n\n\nLEXICON 213 \n\n\n15; XPd 18; XPg 13; XSc 5'
```


## [2026-09-05T20:52:37.865Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/crimson' --note 'page 171 node 9, English crimson/carmine/kermes from Arabic qirmiz' 2>&1|tail -1\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/king' --note 'page 171 nodes 18-19, English king/kind from Germanic *kuningaz/*kundjaz' 2>&1|tail -1\nmkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg171.png data/verification/sources/refs/ocr/BOOK/171.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-05T20:52:40.810Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f956d16f33359865.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/56d67ad2851fea85.txt
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T20:52:44.441Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/BOOK/171.png; python3 - <<'EOF'\nimport re\nfor f,l in [('data/verification/sources/web/f956d16f33359865.txt','crimson'),('data/verification/sources/web/56d67ad2851fea85.txt','king')]:\n    t=open(f,encoding='utf8').read()\n    print('####',l,len(t))\n    # print first 1200 chars after title\n    i=t.find('TITLE')\n    print(t[i:i+1600].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:52:46.254Z] TOOL RESULT

```
data/verification/sources/refs/ocr/BOOK/171.png
#### crimson 8528
TITLE: Crimson - Etymology, Origin & Meaning  Crimson - Etymology, Origin & Meaning    Search   Log in    Columns   Forum   Apps   Premium    Log in    Advertisement Remove Ads   Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.   Origin and history of crimson    crimson (n.)    "highly chromatic deep red color," early 15c., cremesin, "cloth dyed deep purplish-red," also as an adjective, "of a crimson color," from Old Italian carmesi, cremesi (c. 1300), later carmisino, cremesinus , "crimson color; cochineal dye," from Arabic qirmizī (see kermes ). For similar transfer of the dye word to generic use for "red," compare Old Church Slavonic čruminu , Russian čermnyj "red," from the same source. The French form in 15c.-16c. when the word entered English was cramoisin . "The word in Italian came from Arabic, and the word in all other European languages came from Italian via exports of silk cloths from Italy." ["English Words of Arabic Ancestry"]  also from early 15c.    crimson (v.)    c. 1600, "to make crimson" (transitive), from crimson (n.). From 1805 as "to become crimson" (intransitive). Related: Crimsoned ; crimsoning .  also from c. 1600    Entries linking to crimson    kermes (n.)    c. 1600, "shield louse ( Coccus ilicis ) that yields a red dye" (1590s of the tree on which the insects live), from Medieval Latin cremesinus (also source of French kermès , Italian chermes , Spanish carmes ), from Arabic qirmiz "kermes," from Sanskrit krmi-ja a compound meaning "(red dye) produced by a worm."   The Sanskrit compound is krmih "worm" 
#### king 10233
TITLE: King - Etymology, Origin & Meaning  King - Etymology, Origin & Meaning    Search   Log in    Columns   Forum   Apps   Premium    Log in    Advertisement Remove Ads   Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.   Origin and history of king    king (n.)    a late Old English contraction of cyning "king, ruler" (also used as a title), from Proto-Germanic *kuningaz (source also of Dutch koning , Old Norse konungr , Danish konge , Old Saxon and Old High German kuning , Middle High German künic , German König ).   This is of uncertain origin. It is possibly related to Old English cynn "family, race" (see kin ), making a king originally a "leader of the people." Or perhaps it is from a related prehistoric Germanic word meaning "noble birth," making a king etymologically "one who descended from noble birth" (or "the descendant of a divine race"). The sociological and ideological implications render this a topic of much debate. "The exact notional relation of king with kin is undetermined, but the etymological relation is hardly to be doubted" [Century Dictionary].   General Germanic, but not attested in Gothic, where þiudans (cognate with Old English þeoden "chief of a tribe, ruler, prince, king") was used. Finnish kuningas "king," Old Church Slavonic kunegu "prince" (Russian knyaz , Bohemian knez ), Lithuanian kunigas "clergyman" are forms of this word taken from Germanic. Meaning "one who has superiority in a certain field or class" is from late 14c.   As leon is the king of bestes. [John Gower,   "Confessio Amantis," 1390]
```


## [2026-09-05T20:53:02.494Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ['LEW_1910.txt','LAT.txt']:\n    t=open(f,encoding='utf8',errors='replace').read()\n    for m in list(re.finditer(r'\\bgener\\b',t))[:3]:\n        print(f,'|',t[max(0,m.start()-150):m.start()+400].replace('\\n',' '))\n        print('--')\nEOF"
}
```


### [2026-09-05T20:53:04.330Z] TOOL RESULT

```
LAT.txt | t, P.F.83,a8. La forae genu- coaprise dans genuini dentes r^pond A celle de iri. gin (geno) "bouche", gall. gen "joue, aenton", got.kinnus "aAchoire,gener - 4 O 0 -i jone"-, skr. hdnuh "nachoire" (le h doit provenir d'une Otynologie populaire), gr. ysvuS "nachoire inferieure", la plupart feminina. Une forne *gona-dh~,e at afteate par lit. Sdndas "n&choire", lette zuods "aenton" et l'on en rapproche naturellenent gr.yvdi. 0 oC "nachoire", iTec un autre vocaliane. La forne gena du latin 3'explique par le genre feninin; cf. nurus, nora', elle a p
--
LAT.txt | . nurus, nora', elle a pernia de differencier le non de la "joue" de celui du "genou", v. genu. Elle a pu etre favorisOe par 1’existence de mala (e). gener, -eri n. (dat. abl.pl. generibus dana Acc. R 3 , 64): gendre, par oppoaition a socer ; quelquefois "beau-frere". - Ancien; panronan. M. L. 37 3 o . Conpoae: progener: -un appellat auus neptis suae uirun, P.F.«57,«. On trouve dana lea gloaea, CGL II 3«,45, une forne genta, cf. Nie- dernann, Melanges linguistiquea A.Meillet, p.109; la forne a 4 te contestee par M.Schrader, I.F.17,is, cf.Meille
--
LAT.txt | l} "apparente", jardh "proten¬ dant"; le - tar - indo-iranien est aecondaire conne on le voit par av. zanaoya "frere du gendre". Il rOsulte de IA que gener appartiendrait au fond A la fanille de gignS. Hitt. gaena- eat peu clair. Il senble bien qu'il y ait IA un terne de politesse, n'inpliqnant aucune parentO r 4 elle. genista (genesta), - ae f. : genet (Vg ., Plin. ). Les fomes ronanes renontent A genSsta (logoud.) genista et ginestra, itaJL ginestra, v.lua. *ginist, ali . Ginster. Panronan, sauf rounain. M.L.3733. Ponr la va- riation, cf. lep
--
```


## [2026-09-05T20:53:24.947Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,p in enumerate(t):\n    if re.search(r'(ĝen-|gen-).{0,40}(erzeugen|geb[aä]ren)', p) or 'zizanti' in p or 'frazaintis' in p:\n        print('leaf',i,p[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:53:27.185Z] TOOL RESULT

```
leaves 895
leaf 588   gr. yvcboiyog „kenntlich, bekannfc, angesehen", yvcogt^co „mache bekannt", wozu mit Ablaut *ge no-ro- lat. gnarus „einer Sache kundig", ignarus „un- kundig“ ( ignoro eher aus *ignaro nach nosco umge
```


## [2026-09-05T20:53:32.596Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i,p in enumerate(pages):\n    if 'erzeugen' in p and ('jánati' in p or 'janati' in p or 'gigno' in p or 'yiyvo' in p or 'zäta' in p):\n        print('leaf',i, p[:300].replace('\\n',' '))\n        print('....')\nEOF"
}
```


### [2026-09-05T20:53:34.412Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:53:37.996Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\n# find leaf containing printed page number 576 marker\nfor i,p in enumerate(pages[560:620], start=560):\n    head=p.strip()[:80].replace('\\n',' ')\n    if re.search(r'\\b57[0-9]\\b', head) or 'gen-' in head:\n        print(i,'|',head)\nEOF"
}
```


### [2026-09-05T20:53:39.817Z] TOOL RESULT

```
578 | ;     570                                           g(h?)egh-        — gep(h)-, 
580 | ;     572                                                                     "e
581 | gem-                                     573  ,,Zaum‘, vmlem „drficke, driicke z
583 | gembh-, gmbh-, gombhos                                                      575 
586 | 578                                                     g(en-), gene-,     geno-
589 | :                                            gen-
```


## [2026-09-05T20:53:42.679Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i in (584,585,586):\n    print('#### leaf',i)\n    print(pages[i][:1500])\nEOF"
}
```


### [2026-09-05T20:53:44.406Z] TOOL RESULT

```
#### leaf 584
                   :                                                                                                                         ;




                               4
     Ygl. im allgem. Fick I 51 f., 2 [ 5 f                                     .   ,
                                                                                           432.     —
                                                                                                    Ob nasalierte Form zu jcph-,
"jbbh   ..Kiefer. Mund"?     Zupitza Gutt.                                             1   92 f., Bartholomae Airan. Wb. 1657.
— Uber                           *
                 ynioyjij/jai s. gambit -.
                       gr.

     Anmerkung:     yopcyog in der gewohnlicheren Bed. „Pflock, Nagel" ist
rait    lit.    Nagel zum Aufhangen. Ivnagge"' zur Wz. genobh- zu stellen,
               gentle                ,,


s. Zupitza Gutt. 192,  Persson Beitr. 81 mit Anm. 2; obwohl aber „Zahn“
an sicli aus „Pfiock, Stiff" iibertragen sein kbnnte, ist yojurfog „Zahn" doch
wegen der genauen Gleichung mit jambha-h usw. von dem daher nur zu-
fallig     gleichlautenden youg. os ..Pflock" zu scheiden.


1.     geu-, vielfach gene-, genb- ..erzeugen".
     Thematisches Praes. ai. jdnati „erzeugt. gebiert",                                                         alat. gtnunt ,    gr.   (durch
ytyvopai in die Geltung als Aorist gedrangt) yevsa&ai                                                       
#### leaf 585
yvcorog „Yerwandter, Bruder", yvonij     „Schwester lett. znnuts „Schwieger-                                               £

                                                                                                                               ,
                                                                                                                                                                                               £
sohn, Schwager“ (iiber lit. zentas aksl. zdt s. unten u. *yemc- heiraten '),       ,                                                                                          ,;


vgl. u. ai .jnati-h „Yerwandter“ von der anit.-Wz. av. -zanta-, zmita- „ge-
                                                                          ;


boren“ (Yerlust des o? s. J. Schmidt Krit. 1 SO f. Bartholomae ZfrnG. 50,                                              ,


692.   Persson Beitr. 6S6 nimmt altes Nebeneinander von unit- und set-
Form an, wie cpegroov bharitram. Auch acymr. -yint „Kind ££ Fick II 4 111,
                                               :
                                                                                                                                                              ,


aus gen-t-). Kaclt Buga Kalba ir. s. I 222 gehort lit. zentas hierlier.
   Ygl. an andern arischen cmit-Formen a \. f razanh- N a c h k o rn rn e n s c k a 1             :                                     . ,
                           
#### leaf 586
578                                                     g(en-), gene-,     geno-


d.    i.   in        anderer Ehe geboren, Stiefkind“), kelt. -gnos in Personennamen,
ursprgl. Patronymica, z. B. ogom Gen.             Coimagni, ir. Coim-un ; gall. Abe-gnia,
gr.  ofioyvios „von gleicher Abstammung"; *gn-[o- (wozu obiges -gnio-
weitere Scbwacliung in Zs.) in lat. genius ,,der Schutzgeist des Mannes“,
ursprgl. die personifizierte Zeugungskraft allenfalls bochstufiges *gen-ios ),
got. knni, ahd. (usw.) Jcitnni ,,Geschlecht“, vgl. got. scnnaktinjans Acc. pi.
„desselben Gesclilechtes“ gr. Suo-yviog lat. progenies „Nachkommenschaft“,
                                                :                      ;


air. gem „Geburt“, ags. cyne- in Zs. „koniglich“, anord. konr „Sohn, edel-
geborener Mann“ (Abl. ahd. usw. Kuning „Konig“, d. i. „einem edlen Ge-
                                                                   1
schleehte angehorig,                      ihm entsprossen' ) ;             ein ?<-St. in         ai.   janu-li   „Geburt“
(nur Gramm.), yielleicht in lat. genu-lnus ,,angeboren, echt“ (wenn nicht
erst im AnschluB an ingenuus „freibiirtig“ aufgekommen, das als *-ovos
eine Bildung wie caedmis, riguus). Und viele andere Worte, z. B. ysvea,
ysvedh) ,, Abstammung, Geschlecht“, yovevs ,Erzeuger“ (yiyae „Riese“??
s.    Yf. LEWb. 2 386;                    unbefriedigend Prellwitz 2 94).                      arm. cin „Geburt, Ur-
sprung“.
      Alles Wesentliche
```


## [2026-09-05T20:54:52.569Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1971.txt',encoding='utf8',errors='replace').read()\nfor pat in [r'\\ngene, n\\.', r'\\noxygen, n\\.', r'\\nhydrogen, n\\.', r'\\nengineer, n\\.', r'\\neugenics', r'\\nNoel']:\n    m=re.search(pat,t)\n    print('##',pat, '->', (t[m.start():m.start()+420].replace('\\n',' ') if m else 'NONE'))\nEOF"
}
```


### [2026-09-05T20:54:54.329Z] TOOL RESULT

```
## \ngene, n\. ->  gene, n., a hypothetical agent transmitted from  parent to offspring {biol.). — See -gen.   -gene, combining form, identical in meaning and  origin, with -gen (q.v.)   genealogical, adj. — Formed with adj. suff. -al  fr. Gk. yev£aXoyix6<;, ‘of genealogy’, fr. yevea-  Xoyia. See next word and -ic.   Derivative: genealogical-ly, adv.  genealogy, n. — ME. genealogie , fr. OF. genea-  logie (F. genealogie ), fr. Late L.
## \noxygen, n\. ->  oxygen, n., a gaseous chemical element. — F.  oxygene , short for principe oxygine (earlier prin-  cipe oxygine ), lit. ‘the acidifying principle’ ; coin-  ed by the French chemist Antoine-Laurent La-  voisier (1743-94) in 1777 fr. Gk. 6£u<;, ‘sharp,  acid’, and yetvofxoa, ‘I beget, bear, bring forth’,  which stands for *y£vio{xoci. and is rel. to yev-  vaw, ‘I beget, bring forth, generate, produce’ ; see  oxy-, ‘sh
## \nhydrogen, n\. ->  hydrogen, n., name of a gaseous element (chem.)   — F. hydrogdne, lit. ‘producing water’, coined  by the French chemist Antoine-Laurent de La-  voisier (1743-94), in 1787 fr. Gk. uSwp, ‘water’,  and the stem of yevvav, ‘to beget, bring forth,  generate, produce’. See hydro- and -gen.  Derivatives: hydrogen-ate tr. v. f hydrogen-  ation, n., hydrogen-ator, n., hydrogenize, tr. v.,  hydrogen-ous, adj.   hydrograph, n.
## \nengineer, n\. ->  engineer, n. — Formed fr. engine with suff. -eer.  Derivatives: engineer, tr. and intr. v., engineer-  ing, n.   England, n. — OE. Engla land , lit. ‘land of the  Angles’; see next word and land: For the con-  traction of OE. Engla land into England see  haplology.   Derivative: England-er, n.   English, adj. and n. — OE. Englisc, Aenglisc ,  ‘English’, fr. Engle , Angle , name of a Teutonic  tribe that settled in B
## \neugenics ->  eugenics, n., the study of the improvement of the  human race by selection of the parents. —  Coined by Sir Francis Galton (1822-1911) in  1883 from the adjective eugenic. For the ending  see -ics,   Euglandina, n., a genus of snails (zool.) — A  ModL. hybrid coined fr. eu-, L. glam, gen.  glandis , ‘acorn’ (see gland), and suff. -ina.   euhemerism, n., theory of Eubemerus, a Sicilian  Greek philosopher of about 300
## \nNoel ->  Noel, masc. PN. — OF., lit. ‘of, or born on,  Christmas’, fr. L. natalis (scil. dies); see prec.  word and cp. Natalia. The name was orig. given  to children of either sex born on Christmas,  noetic, adj., pertaining to the intellect. — Gk.  vot]tl>c 6(;, ‘pertaining to intelligence, intellec-  tual’, fr. vor,T6q, ‘perceptible by the mind, men-  tal’, verbal adj. of voeo>, ‘I perceive by the  mind’, fr. v6o$, vou?,
```


## [2026-09-05T20:55:05.697Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'فرزند' in p and 240<i<270: print('v3 pdf',i,'printed~',i+1207, p[:80].replace('\\n',' '))\nt4=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t4):\n    if 'میرزا' in p and 200<i<235: print('v4 pdf',i,'printed~',i+1917, p[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:55:07.478Z] TOOL RESULT

```
v3 pdf 251 printed~ 1458 [pdf page 252] سنننه علم وحکمت وداش و استواری باشد ۱ وبکر اول فرزین شطریج را گوب
v3 pdf 261 printed~ 1468 [pdf page 262] NENA  فرمیست  ‎WAS‏ سباکاف بر وزن فرزند. بسعنی فرکن است که زمینی 
v3 pdf 262 printed~ 1469 [pdf page 263] —N\tye  Pata ‏فرمس ۱ = فتح اولوضتالث وسکون‎ ‏بزیان فرس قدیم تام‌ش
v4 pdf 215 printed~ 2132 [pdf page 216] بیان نهم در نون با زای نقطه‌دار مشتمل برشش لغت فزار ۱ بکس اول برو
v4 pdf 224 printed~ 2141 [pdf page 225] یرم ۱1۳ نسیرم۱- بتح اول و رای قرشت فسیله ؟ - بتح اول بروزن‌وسیله,
v4 pdf 228 printed~ 2145 [pdf page 229] شکرده -۱4۹- الحجامین گوبند . ماهی را کویند ۴ - و بمعنی دو چیز را
```


## [2026-09-05T20:55:15.559Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt4=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i in (216,217,218):\n    p=t4[i]\n    print('#### pdf',i,'printed~',i+1917)\n    print(p[:700])\nEOF"
}
```


### [2026-09-05T20:55:17.345Z] TOOL RESULT

```
#### pdf 216 printed~ 2133
[pdf page 217]
زا 1 ده
قزه ۱ - بفنتح اول و ثانی و ظپور ها » ترا ی کردنآب را نز کفته‌اند .
بممتی سقف باشد ؛ وبستی کوینگ چویی باش دکه فزیدت ؟ « بر وزن وزیدن » بمعنی
سقف خانه را بدان پوشند - وجای درآمدن باد | بیرون کشیدن باشد .
بیان دهم
در نون با زای فارسی مشتّمل بر نه لغت
و - بفنتح اول و سکون ثانی , بیرون | کوهری کنه اصیل باشد » و نژاده تفسیر اصیل
کشندء چیزی راکویند ۴ - و دنداند‌کلید راهم ۱ است ۰۱۶
کتته‌اند ۴ . وغار ۱۱ باغین تقطه‌داربروزن رفتاره
نزاد * < بکراول بروزن نخاط , اسل | بانگه و فرباد وتعره راکویند .
و نب را گوبند ‎٩‏ - و بمعنی اسیل و نجیب رم ۱۳- بکر اول وسکون ثانی ومیم»
وخداوند اصل ودب هم‌آمده است ۷ . بمعتی‌میغ‌است وآن بخاری باعد تاربك وملاصق
فزاده * - یک اول بر وزن فتاده . | زمین ؛ 
#### pdf 217 printed~ 2134
[pdf page 218]
-و۲۱۳-< س‌
ون و دال ایجد » بمعتی اندوهگین و غمناکه قژه - بفتح اول و ثانی وظهور ها» خاخ
وفرومانده و افمرده و سرفرود افکنده و پژمرده | درختی راکوبند که بسیار نازك و لطیف برآمده
باشد ‎٩‏ - و بمعنی‌سر گشته وخشمکین وفهرآلود | باشد ۴ - و ورق طلا و نقره رانیز کوبند که
هم هست - وپست و حضرض را نیز کوبند که در | بهیأت بر که کل بریده باشند و برسر پادشاهان
مقابل بلند واوج باشد ۴ ؛ وبفتح اول هم آمده | و نودامادان نثارکنند ۴ - ونام ستاره‌ای هم‌هست
است . از ثوابت * - و چوبی که بدان سقف خانه را
نک ۴ - بفتح اول و دون بر وزن پوشند ۴ .
نغزك , دام و تله راکوبند که حیوانات را بدان فژیدان ‎٩‏ » بروزنومعنی کشیدن باشد.
گیرند.
بیان یاز دهم
در نون با سین بی‌نقطه مشتمل بر سی وهشت لغت و کنایت
: پوز باشد 
#### pdf 218 printed~ 2135
[pdf page 219]
دا هندها
هم آمده است ۱ - و با تشدرید قالی »در عریی آفتاب هرکز تتابد یاکمتن پرسد ۲ - و بههنی
بسمتی خغك خدن وشتر راندن باشد. مرده هم آمده است که نقیض زنده باشد ۴ -
۰ ۰ وبکراول, نام شهرست درخراسان ۴ - و بلفت
نما < بفتح اول و ثانی بالف کشیده + ] زند و پازند (۱) کوشت واستخوان مرده راکونند
موضمی را کوبند ا زکوه و غیر آن که در آنجا | از آدمی و سایر حیوانات دیگر ۴ - و دراعریی
() چك : پاژند ویاژند . ۰
۱ - جپانگیری این معنی را آورده باستناد این بیت مولوی :
يك سیه دیوی و کابولی زئی گعت. بر شپزاده با که رهزلی
آن تودساله عجوز(عجوزی) گند هکس لی(نه) خرد هشت آن‌ماكرا-ونه «س.
رشیدی کوید : « شاید که درین بیت مراد معنی اول باشد که تکرار نشود یعنی دعان و خرداو را
نگذاشت که حرف بزند.» و رك : فرهنگ
```


## [2026-09-05T20:55:28.654Z] AGENT

Now I have all the evidence. Writing the verification file.


## [2026-09-05T21:02:01.714Z] TOOL CALL #80: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build171.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Gene 1\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ǵenh₁- 'to beget, give birth, produce' (Pokorny ĝen-1, ĝenə-, ĝnē-, ĝnō- 'erzeugen, gebären', IEW 373-375)\",\n  \"note\": \"Root, language label and gloss are all correct. Nourai's split into 'Gene 1' (to give birth) and 'Gene 2' (redirected to Gnô, 'to know') reproduces exactly Pokorny's two homonymous lemmas ĝen-1 'gebären' (pp. 373-375) and ĝen-2 'kennen' (pp. 376-378), and Watkins keeps the same separation (gene- vs gnō-). The chart is a faithful digest of Watkins' AHD article for the Latin/Greek/Germanic branches and of Pokorny/Horn for the Iranian ones; the weak points are the Sanskrit->Persian qermez arrow (#7), the unattested Avestan *ni-zāti (#1), the Germanic form 'kundigaz' (#18, a misprint for *kuningaz) and the Persian «جرم» in the French box (#12).\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ǵenh₁- «زادن، پدید آوردن» است که پوکورنی آن را زیر ĝen-1 در صفحات ۳۷۳ تا ۳۷۵ آورده و واتکینز (AHD) و ویکی‌واژه نیز همان را می‌آورند. نامِ زبان («هندواروپایی») و معنای «زادن» در کتاب درست است، و جدا کردن «Gene 1» از «Gene 2» (که به Gnô «دانستن» ارجاع داده شده) دقیقاً همان تفکیک دو ریشهٔ همنام در پوکورنی است. ادعای نورایی دربارهٔ خودِ ریشه درست است؛ اشکال‌ها در چند شاخهٔ فرعی است که در ذیل هر گره توضیح داده شده.\",\n  \"sources\": [W+\"Reconstruction:Proto-Indo-European/%C7%B5enh%E2%82%81-\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:373\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt: 'Root / lemma: ĝen-1, ĝenə- ĝnē- ĝnō- | Meaning: to bear ... References: WP. I 576 ff. ... Page(s): 373-375'. The very next lemma is 'ĝen-2 ... Meaning: to know' (pp. 376-378), i.e. Nourai's Gene 1/Gene 2 split.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 576-578 (WLD_Bd1_pages.txt leaves 584-586)\", \"stance\": \"supports\",\n     \"note\": \"'1. ĝen-, vielfach ĝenə-, ĝenē- \\\"erzeugen\\\". Thematisches Praes. ai. jánati \\\"erzeugt, gebiert\\\", alat. genunt, gr. γενέσθαι' — the source Pokorny 373 itself refers to (WP. I 576 ff.).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gene-\", \"stance\": \"supports\",\n     \"note\": \"'gene-. Also gen-. To give birth, beget; with derivatives referring to aspects and results of procreation and to familial and tribal groups. ... [Pok. 1. gen- 373.]'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *zanH¹ (p. 465-466)\", \"stance\": \"supports\",\n     \"note\": \"'This root has an impeccable IE etymology. PIE *ǵenH₁- \\\"to beget, bear, produce\\\" = LIV: 163 f. | Pok.: 373 ff.'\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/ǵenh₁-\", \"stance\": \"supports\",\n     \"note\": \"'*ǵenh₁- (perfective): to produce; to beget; to give birth'.\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry[\"nodes\"].append\n\nN({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"zan 1; zâta 1; â-zâta 1; ni-zâti; fra-zaintiš\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Av. zan- 'to beget, give birth' (Bartholomae AiW s.v. zan- V. 'zeugen, gebären', redupl. pres. zīzanti, pass. zaiieiti) is the regular Iranian continuant of PIE *ǵenh₁- with the satem outcome *ǵ > z. Its perfect passive participle zāta- 'born' (< *ǵn̥h₁-to-, = Skt. jātá-, Lat. nātus) is well attested (Y 9.5, Yt 19.56), as is the compound fra-zaintiš f. 'offspring, progeny' (< *fra-ǵn̥h₁-ti-, Y 60.7, Y 68.11; the negated a-frazaintiš 'childless' Y 11.1). ā-zāta- 'noble, freeborn' (lit. '(well) born into the family') is likewise real: Wiktionary's Middle Persian entry cites 'Avestan āzāta \\\"noble\\\"' as the cognate of MP āzād. The one form that is not attested as such is 'ni-zâti': the Avesta has ni-zanta- adj. '(house-)born, ingenuus' (AiW, F 26; Cheung 'YAv. nizanta-'), and Horn — the very source Nourai cites for nežād — writes the abstract with an asterisk, 'aw. *nizāti-, vergl. skr. jāti-'. Nourai prints the reconstruction without the asterisk, which is why the node is 'plausible' rather than 'confirmed'.\",\n \"derivation_fa\": \"ستاک اوستایی zan- «زادن، به دنیا آوردن» بازماندهٔ مستقیم ریشهٔ هندواروپایی *ǵenh₁- است و دگرگونی آوایی آن قانونمند است: ǵ هندواروپایی در زبان‌های ساتم و از جمله ایرانی باستان به z بدل شده. صفت مفعولی zāta- «زاده» (از *ǵn̥h₁-to-، هم‌ریشه با سنسکریت jātá- و لاتین nātus) و ترکیب fra-zaintiš «فرزند، نسل» (یسنا ۶۰٫۷ و ۶۸٫۱۱، و شکل منفی a-frazaintiš «بی‌فرزند») در اوستا گواهی شده‌اند، و āzāta- «نژاده، آزاده» نیز به گواهی ویکی‌واژه و بارتولومه واقعی است. تنها ni-zāti «نژاد» در متون اوستایی نیامده است؛ آنچه هست ni-zanta- «زادهٔ خانه» است و خودِ هرن (شمارهٔ ۱۰۳۰) این صورت را با ستاره می‌نویسد: aw. *nizāti-. پس ادعای نورایی با احتیاط پذیرفتنی است و تنها یک صورت آن بازسازی‌شده است نه گواهی‌شده.\",\n \"sources\": [W+\"%D8%A2%D8%B2%D8%A7%D8%AF\"],\n \"ref_check\": [\n   {\"ref\": \"POK:373\", \"status\": \"supports\",\n    \"note\": \"IEW ĝen-1 (pp. 373-375) lists 'Avestan zīzanti', 'Avestan zāta-', 'Avestan fra-zaintiš \\\"progeny\\\"' and 'Avestan zaṇtu- \\\"district\\\"' — the Avestan material of this node except ni-zāti.\"},\n   {\"ref\": \"SOD:462\", \"status\": \"supports\",\n    \"note\": \"Gharib p. 462 (SOD_pages.txt leaf 529), entry 11330: \\\"zn-' B, M, C | zan ©<Av. zan- ©trans. & intrans. ... (to)give birth, (to)be born\\\" — Gharib himself derives the Sogdian verb from Av. zan-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW s.vv. zan-, a-zāta-, ni-zanta-, frazainti-\", \"stance\": \"partial\",\n    \"note\": \"'j. zan- V. \\\"zeugen, gebären\\\" ... PPfP. zāta-'; 'j. ni-zanta- Adj. \\\"ein (d. i. im Haus) geborener, ingenuus\\\"; F. 26'; frazainti- quoted from Y 60.7 and Y 68.11. Bartholomae has no entry *ni-zāti-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *zanH¹ p. 465\", \"stance\": \"partial\",\n    \"note\": \"'YAv. za(n)- \\\"to give birth; (pass.) to be born\\\" || (+ *ni-) YAv. nizanta- \\\"born (in one's own house)\\\"' — again nizanta-, not *nizāti-.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 577 (leaf 585)\", \"stance\": \"supports\",\n    \"note\": \"'av. -zanta-, zanta- \\\"geboren\\\" ... Vgl. an andern arischen …-Formen av. frazanti- \\\"Nachkommenschaft\\\"'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"آزاد, Persian section\", \"stance\": \"supports\",\n    \"note\": \"'From Middle Persian ʾcʾt (āzād, \\\"noble; free\\\"), from Old Persian *āzātah, a northwestern borrowing from Proto-Iranian *āzātah. Cognate with Avestan 𐬁𐬰𐬁𐬙𐬀 (āzāta, \\\"noble\\\")'.\"}\n ]\n})\n\nN({\n \"id\": 2, \"lang\": \"Sogdian\",\n \"words\": \"zn`\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian zn- (written zn' in the Buddhist, Manichaean and Christian scripts) 'to bring forth, give birth' continues the same Old Iranian *zan- as Avestan zan-, with the Sogdian loss of final short vowels and the usual aleph spelling of the stem-final vowel. Gharib's dictionary (the SOD Nourai cites) states the derivation explicitly, and Cheung lists the Sogdian forms under *zanH¹ with the causative znd'r- and the participle zn'mnty 'giving birth' (STi 73.7). The arrow Avestan -> Sogdian is of course to be read 'Old Iranian', not 'Sogdian from Avestan': the two are sister languages, Avestan standing here for the Old Iranian stage.\",\n \"derivation_fa\": \"فعل سغدی zn- («زن» با املای zn') به معنی «زاییدن، به دنیا آوردن» دنبالهٔ همان ستاک ایرانی باستان *zan- است و غریب در فرهنگ سغدی (شمارهٔ ۱۱۳۳۰، صفحهٔ ۴۶۲) خود نوشته است «<Av. zan-». چونگ نیز آن را زیر ریشهٔ *zanH¹ می‌آورد با صورت‌های znd'r- (ماضی متعدی) و zn'mnty «زاینده». تنها نکته آن است که پیکان «اوستایی ← سغدی» را باید «ایرانی باستان ← سغدی» خواند، زیرا سغدی از اوستایی نزاده بلکه خواهر آن است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:462\", \"status\": \"supports\",\n    \"note\": \"SOD_pages.txt leaf 529 = printed p. 462 (printed ≈ leaf − 67 here), entry 11330: \\\"zn-' B, M, C | zan ©<Av. zan- ... (to)give birth, (to)be born\\\".\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *zanH¹, Sogdian section\", \"stance\": \"supports\",\n    \"note\": \"'*SOGDIAN: BSogd. zn-, CSogd. zn-, MSogd. zn- \\\"to bring forth\\\" ... Partic.: pres. CSogd. zn'mnty \\\"giving birth\\\"'.\"},\n   {\"src\": \"SOD\", \"where\": \"p. 462 nos. 11338-11341\", \"stance\": \"supports\",\n    \"note\": \"the neighbouring entries zn'kh 'knowledge', zn'mnty 'bringing forth' and zn'ndy(h) 'bringing forth' confirm the page and the semantic field.\"}\n ]\n})\n\nN({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"zâdan, zâîdan «زادن»; mîrzâ «میرزا»; âzâd «آزاد»; nežâd «نژاد»; farzand «فرزند»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are genuine reflexes of *zan-/*zāta-. (1) زادن zādan / زاییدن zāyīdan 'to give birth': the past stem continues *zāta- (MP zād, inf. zādan; MMP z'y(h)- 'to be born'), the present stem زای- zāy- continues the Old Iranian passive/ya-present *zaya- (Av. zaiieite), whence also the doublet zāyīdan and زائو zāyū 'woman in childbed'. (2) میرزا mīrzā is a contraction of earlier مirzād mīrzād < amīr-zāda 'son of an amīr' — Arabic أمير amīr borrowed into Persian as mīr plus the participle -zād(a) 'born (of)' from zādan; hence Nourai's cross-reference to the Arabic root A'.m.r. (3) آزاد āzād 'free, noble' < MP āzād [ʾcʾt] < Old Iranian *ā-zāta- 'born (into the clan), of good birth'; Armenian azat is a Middle Iranian loan of the same word. (4) نژاد nežād 'race, descent' < *ni-zāta-/*ni-zāti- 'born in (the house)', with ni- 'down, in' — Horn no. 1030 'nižād \\\"Geschlecht, Abstammung, Adel\\\", aw. *nizāti-, vergl. skr. jāti-'. (5) فرزند farzand 'child' < *fra-zanti-/*fra-zainti- 'offspring', through Parthian frzynd (Cheung marks NP farzand as a loan from Parthian) / MP frazand, exactly Horn no. 816 'aw. frazainti- \\\"Nachkommenschaft\\\"; phlv. farzand bezw. frazand'.\",\n \"derivation_fa\": \"هر پنج واژه بازماندهٔ همان ستاک *zan-/*zāta- است. «زادن» از ستاک گذشتهٔ *zāta- (فارسی میانه zād / zādan) و «زاییدن» و «زائو» از ستاک حالِ zāy- که دنبالهٔ صورت مجهولِ ایرانی باستان *zaya- (اوستایی zaiieite) است. «آزاد» از فارسی میانهٔ āzād [ʾcʾt] و آن از ایرانی باستان *ā-zāta- «زاده در تبار، نژاده» است (وام‌واژهٔ ارمنی azat گواه همین صورت است). «نژاد» از *ni-zāta-/*ni-zāti- «زادهٔ درون خانه» با پیشوند ni- است؛ هرن در شمارهٔ ۱۰۳۰ همین را می‌گوید. «فرزند» از *fra-zainti- «نسل، فرزند» است که از راه پارتی frzynd و پهلوی frazand به فارسی نو رسیده (چونگ آن را وام از پارتی می‌داند). «میرزا» نیز کوتاه‌شدهٔ «میرزاد/امیرزاده» است: «میر» معرّبِ برگرفته از عربی أمیر به‌اضافهٔ «ـزاد(ه)» از همین «زادن»؛ از این‌رو نورایی به ریشهٔ عربی A'.m.r ارجاع داده است. ادعای نورایی در این گره درست است.\",\n \"sources\": [W+\"%D9%85%DB%8C%D8%B1%D8%B2%D8%A7\", W+\"%D8%A2%D8%B2%D8%A7%D8%AF\"],\n \"ref_check\": [\n   {\"ref\": \"POK:373\", \"status\": \"supports\",\n    \"note\": \"IEW ĝen-1: 'npers. zayad' quoted beside Avestan zayeite as the ya-present.\"},\n   {\"ref\": \"BQT:34\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaf 244 (printed p. 34) is the آزاد article: 'آزاد ... و مطلق بی‌عیب را گویند ... فلان را آزاد کردم یعنی از قید بندگی فارغش ساختم'.\"},\n   {\"ref\": \"BQT:995\", \"status\": \"partial\",\n    \"note\": \"vol. 2 leaf 456 (printed ≈ 999, the running-head offset is ±4 in this part of the scan) carries the زاد/زادن/زاییدن articles with Mo'in's footnotes 'رک: زادن، زاییدن' and 'پهلوی zād'; p. 995 falls in the same ز-section, but the exact printed number could not be read off the OCR.\"},\n   {\"ref\": \"BQT:1459\", \"status\": \"supports\",\n    \"note\": \"vol. 3 pdf page 252 (printed ≈ 1458-1459) is the فرزند/فرزین page of Borhan.\"},\n   {\"ref\": \"BQT:2134\", \"status\": \"supports\",\n    \"note\": \"vol. 4 pdf pages 216-217 (printed 2133-2134): 'نژاد ... بکسر اول بروزن نخاط، اصل و نسب را گویند ... و بمعنی اصیل و نجیب' followed by 'نژاده'. So BQT:2134 is the نژاد article, not میرزا.\"},\n   {\"ref\": \"HRN:181\", \"status\": \"supports\",\n    \"note\": \"Horn p. 181 (HRN.txt leaf 202) no. 816: 'ferzend \\\"Spross\\\", sowohl Sohn als auch Tochter. aw. frazainti- \\\"Nachkommenschaft\\\"; phlv. farzand bezw. frazand.'\"},\n   {\"ref\": \"HRN:231\", \"status\": \"supports\",\n    \"note\": \"Horn p. 231 (leaf 252) no. 1030: 'nižād \\\"Geschlecht, Abstammung, Adel\\\", nizāde \\\"von adeliger Abstammung\\\". aw. *nizāti-, vergl. skr. jāti-.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. āzād, frazand, zādan, zāyišn\", \"stance\": \"supports\",\n    \"note\": \"'āzād [ʾcʾt | M ʾzʾd, N ~] 1. noble; 2. free'; 'frazand [prznd | M frzynd, N farzand] child, son, offspring'; index: 'born zādag, zāyišnīg; be ~ zādan', 'birth zāyišn'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *zanH¹, MP/Parthian/NP sections\", \"stance\": \"supports\",\n    \"note\": \"'MMP zʾy(h)-, BMP zʾ /zā-/ \\\"to be born; to give birth\\\" ... (+ *ā-) MMP ʾzʾd ... /āzād/ \\\"noble, free\\\" || (+ *fra-) MMP frzynd ... /frazand/ \\\"child, son, offspring\\\" (LW)'; and '*NWIR: NP zāyad \\\"is born\\\" ... (+ *ā-) NP āzād ... (+ *fra-) NP farzand \\\"child, son\\\" (< Pth.)'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"میرزا, Persian etymology\", \"stance\": \"supports\",\n    \"note\": \"'From earlier میرزاد (mirzâd), compound of میر (mir, \\\"master\\\") and the suffix ـزاد، ـزاده (-zâd, -zâde, \\\"child of, son of\\\"), from زادن (zâdan, \\\"to bear\\\")'.\"},\n   {\"src\": \"HRN\", \"where\": \"nos. 816, 1030 (pp. 181, 231)\", \"stance\": \"supports\",\n    \"note\": \"see ref_check; Horn is the standard reference behind Nourai's two page numbers.\"}\n ]\n})\n\nN({\n \"id\": 4, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"zana 1\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian zana- 'man, human being' and Avestan zana- 'people, mankind' are the o-grade noun *ǵon-o- of the same root (Skt. jána- 'people, race', Gk. γόνος 'offspring'). In Old Persian it survives only in compounds — paru-zana- 'having many kinds of men', vispa-zana- 'containing all kinds of men' (DNa 10, DSe 9), Varka-zana- '(month) of the wolf-men' — and Kent notes that the z shows Median transmission (OP itself would give d, whence the Elamite rendering mi-iš-ša-da-na for *visa-dana-). Kent's lexicon entry is verbatim Nourai's gloss: 'zana- sb. \\\"human being\\\": Av. zana-, Skt. jána-, Gk. *γόνος \\\"child, offspring\\\", pIE *ǵono-'.\",\n \"derivation_fa\": \"«zana-» در پارسی باستان و اوستایی به معنی «مردم، انسان» صورت اسمیِ درجهٔ o از همان ریشه است (*ǵon-o-)، هم‌ریشه با سنسکریت jána- و یونانی γόνος. در پارسی باستان تنها در ترکیب‌ها می‌آید: paru-zana- «دارای مردمان بسیار»، vispa-zana- «دربرگیرندهٔ همهٔ مردمان» (کتیبهٔ نقش رستم و شوش) و Varka-zana- نام ماه. کنت یادآور می‌شود که z در این واژه نشانهٔ گویش مادی است، زیرا در پارسی باستانِ ناب باید d می‌شد (چنان‌که در نویسهٔ ایلامی mi-iš-ša-da-na دیده می‌شود). واژه‌نامهٔ کنت عیناً همان معنایی را می‌دهد که نورایی آورده است؛ پس ادعا درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:376\", \"status\": \"partial\",\n    \"note\": \"Pokorny does give 'ĝon-os: ... Avestan (in compound) zana- \\\"people, humankind\\\"' — but inside the lemma ĝen-1, whose printed span is 373-375; p. 376 already begins ĝen-2 'to know'. The material is right, the page number is one page late.\"},\n   {\"ref\": \"KNT:211\", \"status\": \"supports\",\n    \"note\": \"Kent, Lexicon (z-entries, printed pp. 211-213 of the 1950 ed.): 'zana- sb. \\\"human being\\\": Av. zana-, Skt. jána-, Gk. *γόνος \\\"child, offspring\\\", pIE *ǵono- (§88, §148.1); in paruzana-, Varkazana-, vispazana-.' Quoted from the fuller OCR of the same scan (the refs/KNT.txt copy breaks off at p. ~205).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"§88 and s.v. vispazana- (p. 199-200)\", \"stance\": \"supports\",\n    \"note\": \"'pIE *ǵeno-, OP zana- \\\"man\\\" with Med. z, Av. zana-, Skt. jána-; in OP vispa-zana-, paru-zana-'; 'vispazana- adj. \\\"containing all (kinds of) men\\\" ... Med. vispa- \\\"all\\\" + Med. zana- \\\"man, human being\\\"'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 577-578\", \"stance\": \"supports\",\n    \"note\": \"the ĝon-os section of WP I lists the Aryan *ĝana- nouns beside gr. γόνος, γονή.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW s.v. zana-\", \"stance\": \"silent\",\n    \"note\": \"the OCR of Bartholomae is too corrupt at this column to quote; no contradicting statement found.\"}\n ]\n})\n\nN({\n \"id\": 5, \"lang\": None,\n \"words\": \"\",\n \"verdict\": \"unverified\",\n \"derivation\": \"Empty pass-through box: on the printed page (pdf p. 171) the box to the right of 'Avestan / Old Persian zana 1' is drawn but contains no language label and no words, so there is no derivation to check. The extraction is faithful to the page — the blank box is in the book. Presumably the slot was meant for the Persian reflexes of zana- (the -zan of compounds such as hamzan / the second element of hamzabān-type formations, or NP zan in yakzan), but the book leaves it empty.\",\n \"derivation_fa\": \"این خانه در خودِ کتاب خالی است: در صفحهٔ چاپی (صفحهٔ ۱۷۱ پی‌دی‌اف) کادری در برابر «اوستایی/پارسی باستان zana» کشیده شده که نه نام زبان دارد و نه واژه‌ای. بنابراین چیزی برای راستی‌آزمایی وجود ندارد و خطای خوانش اسکن هم در کار نیست؛ استخراج داده با صفحهٔ چاپی می‌خواند. احتمالاً جای بازماندهٔ فارسیِ zana- خالی مانده است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no references because it carries no content.\"}],\n \"consulted\": [\n   {\"src\": \"BOOK\", \"where\": \"printed page 141 = pdf p. 171 (copy at data/verification/sources/refs/ocr/BOOK/171.png)\", \"stance\": \"silent\",\n    \"note\": \"the rendered page shows an empty rectangle to the right of the 'Avestan / Old Persian' box, with no text of any kind.\"},\n   {\"src\": \"KNT\", \"where\": \"s.v. zana-\", \"stance\": \"silent\",\n    \"note\": \"nothing to attach: Kent lists only the Old Persian compounds, no New Persian continuant.\"}\n ]\n})\n\nN({\n \"id\": 6, \"lang\": \"Sanskrit\",\n \"words\": \"ja; krmi-ja\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sanskrit -ja is the zero-grade root noun *ǵn̥h₁-ó- 'born of, produced by', used only as the second member of compounds (Pokorny: 'ĝn̥- in Old Indic ja-ḥ \\\"descendant\\\", pra-jā \\\"progeny\\\"'). kṛmi-ja- literally 'worm-produced' is the classical name of the red dye got from the lac/kermes insect, kṛmi- 'worm' being the cognate of Persian kerm, Lat. vermis (PIE *kʷr̥mi-). Watkins puts the two together in the same article Nourai is digesting: 'Zero-grade form *gn̥- in Sanskrit ja- in kṛmi-ja-, \\\"produced by worms\\\" (see kʷr̥mi-)'.\",\n \"derivation_fa\": \"«ja-» در سنسکریت صورت بی‌واکهٔ ریشه (*ǵn̥h₁-o-) به معنی «زاده از، پدیدآمده از» است و تنها در جزء دوم ترکیب‌ها به کار می‌رود؛ پوکورنی آن را در همین مدخل می‌آورد: «ĝn̥- در سنسکریت ja-ḥ \\\"فرزند\\\"، pra-jā \\\"نسل\\\"». ترکیب kṛmi-ja یعنی «زادهٔ کرم»، نام رنگ سرخی که از حشرهٔ قرمزدانه می‌گرفتند؛ kṛmi- «کرم» هم‌ریشهٔ «کِرم» فارسی و vermis لاتین است (از *kʷr̥mi- هندواروپایی). واتکینز نیز همین دو را کنار هم آورده است؛ ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/crimson\"],\n \"ref_check\": [\n   {\"ref\": \"POK:375\", \"status\": \"supports\",\n    \"note\": \"IEW ĝen-1, last paragraph (printed p. 375): 'ĝn̥- in Old Indic ja-ḥ \\\"descendant\\\", pra-jā \\\"progeny\\\", jās-patiš \\\"paterfamilias\\\"'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gene- §14\", \"stance\": \"supports\",\n    \"note\": \"'14. Zero-grade form *gn̥- in Sanskrit ja- in kṛmi-ja-, \\\"produced by worms\\\" (see kʷr̥mi-).'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. crimson\", \"stance\": \"supports\",\n    \"note\": \"'crimson ... ult. fr. OI. [kṛmi-ja] \\\"produced by a worm\\\". OI. kṛmiḥ \\\"worm\\\" is cogn. with Lith. kirmis, OIr. cruim, Alb. krimb \\\"worm\\\".'\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. kermes\", \"stance\": \"supports\",\n    \"note\": \"'from Arabic qirmiz \\\"kermes,\\\" from Sanskrit krmi-ja a compound meaning \\\"(red dye) produced by a worm.\\\"'\"}\n ]\n})\n\nN({\n \"id\": 7, \"lang\": \"Persian\",\n \"words\": \"qermez «قرمز»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The word is real and belongs to this word-family, but not by the route drawn. New Persian قرمز qermez is a re-borrowing from Arabic قِرْمِز qirmiz (hence the qāf, impossible in an inherited Iranian word), and the Arabic itself came from Middle Iranian, not from Sanskrit: Wiktionary derives Arabic qirmiz from Persian *کرمست *kermest, ultimately Proto-Indo-Iranian *kŕ̥miš 'worm', 'whence also the inherited doublet کرم (kerm, \\\"worm\\\")'. So qermez is Persian's own word for 'worm' come home through Arabic — a classic Persian > Arabic > Persian round trip — and the Sanskrit form kṛmi-ja is at best a parallel Indo-Aryan formation, not the ancestor of the Persian word. Mo'in's own footnote in Borhān (the page Nourai cites) keeps the older Sanskrit derivation but at the same time records the Arabic mediation into European languages.\",\n \"derivation_fa\": \"واژه واقعی است اما راهِ ترسیم‌شده در نمودار درست نیست. «قرمز» فارسی نو وام‌گرفته از عربی «قِرْمِز» است — «ق» آغازین خود گواه است، زیرا در واژهٔ ایرانیِ موروثی چنین آوایی نداریم — و عربی نیز آن را نه از سنسکریت بلکه از ایرانی میانه گرفته است: ویکی‌واژه اصل آن را فارسی *کرمست می‌داند، از هندوایرانی آغازین *kŕ̥miš «کرم»، که دوگانهٔ موروثی‌اش در فارسی همان «کِرم» است. پس «قرمز» نمونهٔ روشن رفت‌وبرگشت فارسی ← عربی ← فارسی است و kṛmi-ja سنسکریت ساختی موازی است نه نیای آن. حاشیهٔ معین بر برهان قاطع (همان صفحه‌ای که نورایی ارجاع داده) هنوز ریشهٔ سنسکریت را می‌آورد ولی راه عربی را نیز ثبت می‌کند. پژوهش امروزی پیکانِ «سنسکریت ← فارسی» را رد می‌کند.\",\n \"sources\": [W+\"%D9%82%D8%B1%D9%85%D8%B2\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1527\", \"status\": \"partial\",\n    \"note\": \"Borhān vol. 3, pdf page 320 = printed ≈ 1526-1527, the قرمز article ('قرمز ... چیزی است که بدان چیزها رنگ کنند، و گویند قرمز جانوری است کوچک و بر بوته‌های خار می‌نشیند'); Mo'in's footnote (OCR): 'قرمز ... چاپ مدرس ص ۲۲۴ ... از سانسکریت ... و از عربی وارد فرانسوی شده kermés'. So Mo'in does say 'from Sanskrit' (supporting Nourai) but also documents the Arabic route the chart omits.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"قرمز, Persian section\", \"stance\": \"contradicts\",\n    \"note\": \"'Borrowed from Arabic قِرْمِز (qirmiz), from Persian *کرمست (*kermest), ultimately from Proto-Indo-Iranian *kŕ̥miš (\\\"worm\\\"), whence also the inherited doublet کرم (kerm, \\\"worm\\\")'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. crimson, kermes\", \"stance\": \"partial\",\n    \"note\": \"Klein knows only the Arabic > European route and derives the Arabic 'ult. fr. OI. kṛmi-ja'; he says nothing about a direct Sanskrit > Persian passage.\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. kermes\", \"stance\": \"partial\",\n    \"note\": \"same older view (Arabic qirmiz < Sanskrit krmi-ja); no Sanskrit > Persian arrow.\"}\n ]\n})\n\nN({\n \"id\": 8, \"lang\": \"Arabic\",\n \"words\": \"qirmiz\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Arabic قِرْمِز qirmiz 'kermes insect; crimson dye' is certainly a borrowing from the Indo-Iranian 'worm-born' word, but the immediate donor is contested. Klein (the page Nourai cites) and Etymonline give the traditional derivation 'Arab. qirmiz, ult. fr. OI kṛmi-ja \\\"produced by a worm\\\"'; Wiktionary and the Iranist literature instead posit a Middle Iranian *kermest/*kirmiz, i.e. the Persian rather than the Indic form, which explains the Arabic vocalism qirmiz better than a Sanskrit compound in -ja would. Either way the root is the same PIE *kʷr̥mi- 'worm' plus *ǵn̥h₁-o- 'born', and the word travelled with the dye trade into Arabic in the early Islamic centuries and thence into Mediaeval Latin cremesinus.\",\n \"derivation_fa\": \"«قِرْمِز» عربی بی‌گمان وام‌واژه‌ای هندوایرانی است، اما دربارهٔ زبانِ واسط اختلاف هست. کلاین (همان صفحه‌ای که نورایی ارجاع می‌دهد) و اتیمانلاین آن را از سنسکریت kṛmi-ja «زادهٔ کرم» می‌گیرند؛ ویکی‌واژه و پژوهش‌های ایران‌شناسی صورت ایرانی میانهٔ *kermest/*kirmiz را مأخذ می‌دانند که آواگذاریِ qirmiz را بهتر توضیح می‌دهد. در هر دو صورت ریشه یکی است: *kʷr̥mi- «کرم» به‌اضافهٔ *ǵn̥h₁-o- «زاده». این واژه همراه با تجارت رنگِ سرخ در سده‌های نخست اسلامی به عربی و از آنجا به لاتینِ میانه (cremesinus) رفت. ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"%D9%82%D8%B1%D9%85%D8%B2\", \"https://www.etymonline.com/word/crimson\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:373\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. crimson (vol. 1 p. 373 of the 1966 ed., the CRI- range): 'crimson, n., deep red. — Sp. cremesin, fr. Arab. qirmiz, ult. fr. OI. [kṛmi-ja] \\\"produced by a worm\\\".' Cp. also s.v. kermes: 'F. kermès, fr. Arab. qirmiz, ult. fr. OI. kṛmi-ja-, \\\"produced by a worm\\\".'\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"قرمز, Arabic section\", \"stance\": \"contradicts\",\n    \"note\": \"'From Persian *کرمست (*kermest), ultimately from Proto-Indo-Iranian *kŕ̥miš (\\\"worm\\\")' — an Iranian, not Indic, source for the Arabic.\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. kermes\", \"stance\": \"supports\",\n    \"note\": \"'from Arabic qirmiz \\\"kermes,\\\" from Sanskrit krmi-ja a compound meaning \\\"(red dye) produced by a worm\\\"'.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 3 p. ~1527, Mo'in's footnote to قرمز\", \"stance\": \"supports\",\n    \"note\": \"Mo'in likewise derives it from Sanskrit and notes the passage into French as kermès.\"}\n ]\n})\n\nN({\n \"id\": 9, \"lang\": \"English\",\n \"words\": \"crimson, carmine, kermes\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three English colour words go back to Arabic qirmiz, each by its own Romance intermediary: crimson (early 15c. cremesin) came through Old Italian carmesi/cremesi and Spanish cremesin, with the Italian silk trade ('the word in Italian came from Arabic, and the word in all other European languages came from Italian via exports of silk cloths from Italy'); kermes (c. 1600) came through French kermès from Mediaeval Latin cremesinus; carmine through French carmin from Mediaeval Latin carminium, which Klein analyses as a blend of Arabic qirmiz with Latin minium 'cinnabar, red lead'. The chart's direct Arabic -> English arrow is therefore shorthand for Arabic -> Italian/Spanish/Latin -> French -> English.\",\n \"derivation_fa\": \"هر سه واژهٔ انگلیسی از «قِرمِز» عربی‌اند، اما هر کدام از راهی جداگانه در زبان‌های رومی: crimson (سدهٔ پانزدهم، cremesin) از ایتالیایی کهن carmesi/cremesi و اسپانیایی cremesin، همراه با تجارت پارچهٔ ابریشمِ ایتالیا؛ kermes (حدود ۱۶۰۰) از فرانسوی kermès و لاتین میانهٔ cremesinus؛ و carmine از فرانسوی carmin و لاتین میانهٔ carminium که کلاین آن را آمیزهٔ qirmiz عربی با minium لاتین («شنگرف») می‌داند. بنابراین پیکان مستقیم «عربی ← انگلیسی» در نمودار کوتاه‌نوشتِ راهِ عربی ← ایتالیایی/اسپانیایی ← فرانسوی ← انگلیسی است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/crimson\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:373\", \"status\": \"supports\",\n    \"note\": \"Klein p. 373 s.v. crimson: 'Sp. cremesin, fr. Arab. qirmiz ... Cp. kermes, carmine'; s.v. carmine: 'F. carmin, fr. ML. carminium, a blend of Arab. qirmiz \\\"worm\\\" and L. minium \\\"cinnabar, red lead\\\"'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Etymonline\", \"where\": \"s.v. crimson, kermes\", \"stance\": \"supports\",\n    \"note\": \"'crimson (n.) early 15c., cremesin ... from Old Italian carmesi, cremesi ... from Arabic qirmizī (see kermes)'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. kermes\", \"stance\": \"supports\",\n    \"note\": \"'kermes, n., the bodies of the females of an insect found on the kermes oak. — F. kermès, fr. Arab. qirmiz'.\"}\n ]\n})\n\nN({\n \"id\": 10, \"lang\": \"Latin\",\n \"words\": \"gener, gent, genius, ingenium, germen, nâtus (gnâtus), prae-gnâs\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The list is copied item for item out of Watkins' AHD article, whose forms it reproduces including their citation shape: 'gent' is Watkins' gēns (stem gent-) 'clan, race' (< *ǵn̥h₁-ti-), and 'gener' is his genus (stem gener-) 'race, kind' (< *ǵenh₁-es-), not the homograph gener 'son-in-law'. genius < *ǵenh₁-yo- 'the procreative divinity, inborn spirit'; ingenium (in- + *ǵenh₁-yo-) 'inborn character'; germen < *ǵenh₁-men- (with dissimilation of m...m) 'shoot, bud, germ'; gnātus/nātus, past participle of gnāscī/nāscī < *ǵn̥h₁-sko- 'to be born'; praegnās 'pregnant' < prae- + *ǵnā- (zero-grade *ǵn̥h₁-). Should 'gener' after all be meant as 'son-in-law', it is still defensible: Ernout-Meillet conclude 'il résulte de là que gener appartiendrait au fond à la famille de gignō', although Pokorny (369) and most moderns file it under *ǵem(ə)- 'to marry'.\",\n \"derivation_fa\": \"این فهرست واژه‌به‌واژه از مقالهٔ واتکینز (AHD) گرفته شده است و حتی شکل ارجاع را نگه داشته: «gent» همان gēns (ستاک gent-) «تیره، قوم» از *ǵn̥h₁-ti- است و «gener» همان genus (ستاک gener-) «نژاد، گونه» از *ǵenh₁-es-، نه واژهٔ همنگارِ gener «داماد». genius از *ǵenh₁-yo- «ایزدِ زایندگی، سرشت درونی»؛ ingenium از in- + همان؛ germen از *ǵenh₁-men- «جوانه» با ناهمگونیِ m…m؛ nātus/gnātus صفت مفعولی nāscī/gnāscī «زاده شدن» از *ǵn̥h₁-sko-؛ و praegnās «آبستن» از prae- + ستاک بی‌واکهٔ *ǵn̥h₁-. اگر هم مقصود gener «داماد» باشد، ارنو و مِیه آن را «در بنیاد از خانوادهٔ gignō» می‌دانند، هرچند پوکورنی (ص ۳۶۹) آن را زیر *ǵem- «زناشویی کردن» می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. gene-: '§2d Latin gēns (stem gent-), race, clan'; '§3a Latin genus (stem gener-), race, kind'; '§4a Latin genius'; '§4b Latin ingenium'; '§7 Latin germen, shoot, bud, embryo, germ'; '§11 Latin praegnās'; '§12 Latin gnāscī, nāscī (past participle gnātus, nātus)'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 373-375\", \"stance\": \"supports\",\n    \"note\": \"'Latin gēns ... Latin genus ... Latin genius ... Latin germen \\\"germ, sprout\\\" ... prōs-gnās \\\"pregnant\\\", new praegnans, from *-gnātis'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 577-578\", \"stance\": \"supports\",\n    \"note\": \"'*gn̥-jo- ... in lat. genius \\\"der Schutzgeist des Mannes\\\", ursprgl. die personifizierte Zeugungskraft'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. gener\", \"stance\": \"partial\",\n    \"note\": \"'Il résulte de là que gener appartiendrait au fond à la famille de gignō' — i.e. even the 'son-in-law' word is claimed for this root by Ernout-Meillet, against Pokorny's ĝem- 369.\"}\n ]\n})\n\nN({\n \"id\": 11, \"lang\": \"French\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box marking the Latin > French > Persian route. The relevant French continuations are gens (< gēns, gentem), général (< generālis), gendarme (< gens d'armes, with gens from gēns), générateur (< generātor) and national (< nātiōnālis, from nātiō < nāscī); Watkins explicitly notes 'Latin gēns (stem gent-), race, clan (> French gens, men): GENS, GENTEEL, GENTILE, GENTLE; GENDARME'.\",\n \"derivation_fa\": \"این خانه در کتاب تهی است و تنها گذرگاهِ «لاتین ← فرانسوی ← فارسی» را نشان می‌دهد. دنبالهٔ فرانسوی این ریشه چنین است: gens از gēns لاتین، général از generālis، gendarme از gens d'armes، générateur از generātor و national از nātiōnālis (از nātiō و آن از nāscī). واتکینز نیز خود می‌نویسد که gēns لاتین به فرانسوی gens رسیده و gendarme از همین است. این گره درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gene- §2d\", \"stance\": \"supports\",\n    \"note\": \"'Latin gēns (stem gent-), race, clan (> French gens, men): GENS, GENTEEL, GENTILE, GENTLE; GENDARME.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. Noel, gendarme-related entries\", \"stance\": \"supports\",\n    \"note\": \"'Noel, masc. PN. — OF., lit. \\\"of, or born on, Christmas\\\", fr. L. natalis (scil. dies)' shows the same Latin > French transmission for this family.\"}\n ]\n})\n\nN({\n \"id\": 12, \"lang\": \"Persian\",\n \"words\": \"(script only) جرم ، ژنرال ، ژاندارم ، ژنراتور ، ناسیونال\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"Four of the five are unimpeachable modern French loans in Persian, all of them borrowed in the Qajar/Pahlavi period through the army and the press: ژنرال < général, ژاندارم < gendarme (< gens d'armes), ژنراتور < générateur, ناسیونال < national — and Mo'in, Nourai's reference, lists them as such ('ناسیونال [Fr.] (ص.) ملی، قومی'). The first word is the problem: the page prints «جرم» with a plain jīm (verified on the 450-dpi rendering of pdf p. 171), i.e. the Arabic word jerm 'body, mass' / jorm 'crime', which is not a French loan at all. What Nourai must mean is French germe 'germ' (< Latin germen, his §7 item), which Persian writes ژرم with three dots. Mo'in has no French جرم — his جرم entries are all the Arabic ones. So the JSON is faithful and the fault is the book's: a missing pair of dots (ژرم > جرم) or a slip of the pen.\",\n \"derivation_fa\": \"چهار واژه از پنج واژه بی‌گمان وام‌واژهٔ فرانسوی‌اند و در دورهٔ قاجار و پهلوی از راه ارتش و مطبوعات وارد فارسی شده‌اند: «ژنرال» از général، «ژاندارم» از gendarme (خود از gens d'armes)، «ژنراتور» از générateur و «ناسیونال» از national؛ معین نیز — همان مأخذی که نورایی داده — «ناسیونال» را با نشانِ [فر.] و معنی «ملی، قومی» آورده است. مشکل واژهٔ نخست است: صفحهٔ چاپی «جرم» با جیمِ یک‌نقطه دارد (با بزرگ‌نمایی ۴۵۰ نقطه‌بر‌اینچ بررسی شد)، یعنی همان واژهٔ عربیِ جِرم/جُرم که هیچ ربطی به فرانسوی ندارد. مقصود نورایی آشکارا germe فرانسوی «تخمه، ژرم» (از germen لاتین) است که در فارسی «ژرم» نوشته می‌شود. پس این خطای چاپی کتاب است نه خطای خوانش اسکن؛ داده‌های استخراج‌شده با صفحه می‌خواند.\",\n \"error_in\": \"book\",\n \"book_prints\": \"جرم\",\n \"correct_form\": \"ژرم\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"partial\",\n    \"note\": \"Mo'in, Farhang-e Farsi: 'ناسیونال: [Fr.] (ص.) ملی، قومی. صح.- احتراز از استعمال این کلمهٔ بیگانه ... اولی است' (MON_part2.txt); 'ژاندارم: (امر.) سربازی که مأمور حفظ نظم در راه‌ها و جاده‌های خارج شهر می‌باشد، امنیه' and 'ژنرالیسم: (نظ.) فرماندهٔ کل قوا' (MON_part1.txt). No French جرم anywhere in Mo'in: every جرم entry there is the Arabic word (جرم 'crime' in ارتکاب جرم, اعلام جرم).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt s.vv. ژاندارم، ژنرال؛ MON_part2.txt s.v. ناسیونال\", \"stance\": \"partial\",\n    \"note\": \"confirms the four French loans, is silent on a French جرم/ژرم.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gene- §2d, §7\", \"stance\": \"supports\",\n    \"note\": \"'GENDARME' under gēns and 'GERM ... GERMINATE' under germen — the Latin/French sources of the Persian loans.\"},\n   {\"src\": \"BOOK\", \"where\": \"pdf p. 171 at 450 dpi (data/verification/sources/refs/ocr/BOOK/171.png)\", \"stance\": \"supports\",\n    \"note\": \"the printed box reads «جرم ، ژنرال ، ژاندارم / ژنراتور ، ناسیونال»; the first word unambiguously has one dot under the jīm.\"}\n ]\n})\n\nN({\n \"id\": 13, \"lang\": \"English\",\n \"words\": \"genius, engine, engineer, general, gentle, pregnant, generation, nation, nature, Noel\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Every word on the list is in Watkins' article under the Latin bases of node #10, and most of them reached English through Old French rather than straight from Latin: genius is the Latin word taken over directly (15c.); engine < OF engin < ingenium, whence engineer (engine + -eer); general < generālis; gentle < OF gentil < gentīlis (gēns); pregnant < praegnās; generation < generātiō; nation < OF nacion < nātiōnem; nature < OF nature < nātūra ('birth, natural qualities', a nātus-derivative); Noel < OF Noel < (diēs) nātālis 'birth-day', i.e. Christmas.\",\n \"derivation_fa\": \"همهٔ این واژه‌ها در مقالهٔ واتکینز زیر همان ستاک‌های لاتینِ گرهِ پیشین آمده‌اند و بیشترشان نه یکراست از لاتین بلکه از راه فرانسویِ کهن به انگلیسی رسیده‌اند: engine از engin فرانسوی کهن و آن از ingenium، و engineer از همان با پسوند -eer؛ general از generālis؛ gentle از gentil فرانسوی و gentīlis لاتین؛ pregnant از praegnās؛ generation از generātiō؛ nation از nātiōnem؛ nature از nātūra («زایش، سرشت»)؛ و Noel از nātālis (dies) «روز میلاد». genius نیز مستقیم از لاتین در سدهٔ پانزدهم گرفته شده است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. gene- lists exactly these English words under the relevant Latin bases: 'GENIAL, GENIUS' (§4a), 'ENGINE, INGENIOUS' (§4b), 'GENDER, GENERAL, GENERATE, (GENERATION), GENERIC ...' (§3a), 'GENS, GENTEEL, GENTILE, GENTLE' (§2d), 'PREGNANT' (§11), 'NAIVE, NASCENT, NATAL, NATION, NATIVE, NATURE, NEE, NOEL' (§12).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. engineer, Noel\", \"stance\": \"supports\",\n    \"note\": \"'engineer, n. — Formed fr. engine with suff. -eer'; 'Noel, masc. PN. — OF., lit. \\\"of, or born on, Christmas\\\", fr. L. natalis (scil. dies)'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 373-375\", \"stance\": \"supports\",\n    \"note\": \"the Latin etyma (genus, genius, gēns, nātus, nātūra, praegnās) are all in the lemma.\"}\n ]\n})\n\nN({\n \"id\": 14, \"lang\": \"Greek\",\n \"words\": \"genos; eu-genos\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Greek γένος génos 'race, family, kind' is the s-stem *ǵenh₁-es- (= Lat. genus, Skt. jánas-) and is exactly as the chart has it. 'eu-genos' however is not a Greek word: the compound is εὐγενής eugenḗs 'well-born, noble' (whence eugenics, coined by Galton in 1883, and the name Εὐγένιος Eugenios > Eugene), because compounds of an s-stem take the adjectival ending -ής, not -ος. Watkins accordingly lists 'Greek suffix -genēs, \\\"-born\\\"' beside 'Greek genos and genea'. The claim is right, the Greek form is mis-shaped, so 'plausible'.\",\n \"derivation_fa\": \"«γένος» یونانی به معنی «تبار، خاندان، گونه» همان ستاک s-دار *ǵenh₁-es- است (برابر genus لاتین و jánas- سنسکریت) و آنچه در نمودار آمده درست است. اما «eu-genos» واژهٔ یونانی نیست: صورت درست εὐγενής (eugenḗs) «نیک‌زاد، نژاده» است، زیرا ترکیب‌های ساخته‌شده از ستاک s-دار پایانهٔ صفتیِ -ής می‌گیرند نه -ος؛ از همین εὐγενής است که eugenics (ساختهٔ گالتون در ۱۸۸۳) و نام Εὐγένιος/Eugene آمده‌اند. واتکینز نیز «پسوند یونانی -genēs» را جدا از genos می‌آورد. پس ادعای اصلی درست است ولی صورتِ یونانی نادرست نوشته شده و از این‌رو با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins §3b-c: 'Greek genos and genea, race, family: GENEALOGY, GENOCIDE, GENOTYPE, HETEROGENEOUS; c. Greek suffix -genēs, \\\"-born\\\": -GEN, -GENY.' The adjective is -genēs, not -genos.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 373-375\", \"stance\": \"partial\",\n    \"note\": \"'ĝenos- in ... gr. γένος \\\"gender, sex\\\"'; and 'with gr. -γενής, thrak. -zenes' — again the -ής form for the compound.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. eugenics\", \"stance\": \"partial\",\n    \"note\": \"'eugenics ... Coined by Sir Francis Galton (1822-1911) in 1883 from the adjective eugenic' (< Gk. εὐγενής).\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 578\", \"stance\": \"supports\",\n    \"note\": \"'γενεά, γενεθλή \\\"Abstammung, Geschlecht\\\", γονεύς \\\"Erzeuger\\\"' listed for the Greek branch.\"}\n ]\n})\n\nN({\n \"id\": 15, \"lang\": \"French\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box for the Greek > French > Persian route. The French words behind the Persian ones are the chemists' coinages oxygène (Lavoisier, 1777, 'the acidifying principle', from Gk. ὀξύς 'sharp, acid' + the -γενής element) and hydrogène (Lavoisier, 1787, from ὕδωρ 'water' + the stem of γεννᾶν), plus gène, the French rendering of Johannsen's German Gen (1909), itself abstracted from Greek -genēs.\",\n \"derivation_fa\": \"این خانه نیز تهی است و تنها گذرگاهِ «یونانی ← فرانسوی ← فارسی» را نشان می‌دهد. واژه‌های فرانسویِ پشت واژه‌های فارسی، ساخته‌های شیمی‌دانان‌اند: oxygène که لاووازیه در ۱۷۷۷ از ὀξύς «تیز، ترش» و جزء -génes ساخت، و hydrogène که همو در ۱۷۸۷ از ὕδωρ «آب» و ستاک γεννᾶν ساخت؛ و gène که برگردان فرانسوی واژهٔ آلمانی Gen (ساختهٔ یوهانسن در ۱۹۰۹) از همان -genēs یونانی است. این گره درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. oxygen, hydrogen\", \"stance\": \"supports\",\n    \"note\": \"'oxygen, n. — F. oxygène ... coined by the French chemist Antoine-Laurent Lavoisier (1743-94) in 1777 fr. Gk. ὀξύς \\\"sharp, acid\\\", and γείνομαι \\\"I beget, bear, bring forth\\\"'; 'hydrogen ... F. hydrogène, lit. \\\"producing water\\\", coined by ... Lavoisier ... in 1787 fr. Gk. ὕδωρ \\\"water\\\", and the stem of γεννᾶν'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gene- §3c\", \"stance\": \"supports\",\n    \"note\": \"'Greek suffix -genēs, \\\"-born\\\": -GEN, -GENY' — the element used in oxygène/hydrogène/gène.\"}\n ]\n})\n\nN({\n \"id\": 16, \"lang\": \"Persian\",\n \"words\": \"(script only) ژن ، اکسیژن ، هیدروژن\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Three twentieth-century French loans in Persian, all showing the tell-tale ژ /ʒ/ that marks a French rather than an Arabic or English source: ژن < gène, اکسیژن < oxygène, هیدروژن < hydrogène (English would have given *اکسیجن/*جین). They entered Persian with the school science vocabulary of the Reza Shah period; Mo'in registers اکسیژن as the chemical element ('اکسیژن: (شیم.) گازی است بی‌رنگ، بی‌بو، بی‌طعم، کمی سنگین‌تر از هوا') and uses هیدروژن in the definition of آب ('مرکب از دو عنصر اکسیژن و هیدروژن').\",\n \"derivation_fa\": \"هر سه وام‌واژهٔ فرانسوی سدهٔ بیستم‌اند و «ژ» آغازین یا میانی خود گواه فرانسوی بودن آنهاست، نه انگلیسی: «ژن» از gène، «اکسیژن» از oxygène و «هیدروژن» از hydrogène (اگر از انگلیسی می‌آمدند «اکسیجن» و «جین» می‌شدند). این واژه‌ها با واژگان علمیِ مدرسه‌های نو در دورهٔ رضاشاه وارد فارسی شدند. معین «اکسیژن» را چنین آورده است: «(شیم.) گازی است بی‌رنگ، بی‌بو، بی‌طعم، کمی سنگین‌تر از هوا»، و در تعریف «آب» می‌نویسد «مرکب از دو عنصر اکسیژن و هیدروژن». ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"supports\",\n    \"note\": \"MON_part1.txt: 'اکسیژن: (شیم.) گازی است بی‌رنگ، بی‌بو، بی‌طعم، کمی سنگین‌تر از هوا. یک لیتر آن ۱٫۴۳ گرم جرم دارد ...'; s.v. آب: 'مایعی است شفاف، بی‌طعم و بی‌بو، مرکب از دو عنصر اکسیژن و هیدروژن'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. اکسیژن، آب\", \"stance\": \"supports\",\n    \"note\": \"see ref_check; Mo'in gives the words as modern European borrowings.\"},\n   {\"src\": \"KLN\", \"where\": \"s.vv. oxygen, hydrogen\", \"stance\": \"supports\",\n    \"note\": \"establishes the French originals (Lavoisier 1777/1787) from which the Persian forms with ژ were taken.\"}\n ]\n})\n\nN({\n \"id\": 17, \"lang\": \"English\",\n \"words\": \"gene, oxygen, hydrogen, Eugene\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Modern learned formations on the Greek element: oxygen and hydrogen are anglicisations of Lavoisier's French oxygène (1777) and hydrogène (1787), built on ὀξύς / ὕδωρ + the -γενής 'born, producing' element; gene is Johannsen's German Gen (1909), abstracted from Darwin's pangene and ultimately from the same Greek -genēs (Klein files English gene under -gen); Eugene is Greek Εὐγένιος 'well-born' through Latin Eugenius and French Eugène. The chart's Greek -> English arrow again passes silently over the French/German coiners.\",\n \"derivation_fa\": \"این‌ها ساخته‌های علمیِ نوین بر پایهٔ جزء یونانی‌اند: oxygen و hydrogen صورت انگلیسی‌شدهٔ oxygène (۱۷۷۷) و hydrogène (۱۷۸۷) لاووازیه‌اند، ساخته از ὀξύς / ὕδωρ به‌اضافهٔ جزء -γενής «زاینده»؛ gene همان Gen آلمانی است که یوهانسن در ۱۹۰۹ از pangene داروین جدا کرد و ریشهٔ آن نیز همان -genēs یونانی است (کلاین gene را ذیل -gen می‌آورد)؛ و Eugene از Εὐγένιος یونانی «نیک‌زاد» از راه Eugenius لاتین و Eugène فرانسوی است. پیکان «یونانی ← انگلیسی» در نمودار از سازندگان فرانسوی و آلمانی این واژه‌ها نامی نمی‌برد. با این توضیح ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book; the parent Greek box cites AHD.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. gene, oxygen, hydrogen\", \"stance\": \"supports\",\n    \"note\": \"'gene, n., a hypothetical agent transmitted from parent to offspring (biol.). — See -gen'; 'oxygen ... F. oxygène ... coined by ... Lavoisier ... in 1777 fr. Gk. ὀξύς ... and γείνομαι'; 'hydrogen ... F. hydrogène ... coined by ... Lavoisier ... in 1787'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gene- §3c\", \"stance\": \"supports\",\n    \"note\": \"'Greek suffix -genēs, \\\"-born\\\": -GEN, -GENY' covers gene/oxygen/hydrogen; §3b covers the Eugen- name-type.\"}\n ]\n})\n\nN({\n \"id\": 18, \"lang\": \"Germanic\",\n \"words\": \"kundjaz; kundigaz\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The first form is right: Proto-Germanic *kundjaz 'family, race' < *ǵn̥h₁-ti-, which gives Old English cynd, gecynd(e) 'origin, birth, race, kind' (> kind). The second, 'kundigaz', is not a Germanic form anyone reconstructs; the word meant is *kuningaz 'king' (OE cyning > king), which Watkins glosses exactly as Nourai does — 'king (< \\\"son of the royal kin\\\")' — deriving it from *kunjam 'family' (< *ǵn̥h₁-yo-). Walde-Pokorny says the same: 'anord. konr \\\"Sohn, edelgeborener Mann\\\" (Abl. ahd. usw. kuning \\\"König\\\", d. i. \\\"einem edlen Geschlechte angehörig\\\")'. The 450-dpi rendering of the printed page shows 'kundigaz' plainly, so this is Nourai's own misprint (a blend of the neighbouring *kundjaz/*kundiz with *kuningaz), not an extraction error.\",\n \"derivation_fa\": \"صورت نخست درست است: ژرمنی آغازین *kundjaz «خاندان، تبار» از *ǵn̥h₁-ti- که در انگلیسی کهن cynd / gecynd «اصل، زایش، گونه» شده و امروز kind است. اما «kundigaz» صورتی است که هیچ‌کس بازسازی نکرده؛ آنچه مقصود بوده *kuningaz «شاه» است (انگلیسی کهن cyning ← king) که واتکینز دقیقاً با همان معنایی که نورایی آورده تعریف می‌کند: «شاه، یعنی زادهٔ تبار شاهی» و آن را از *kunjam «خاندان» می‌گیرد. والده-پوکورنی نیز می‌نویسد: «نروژی کهن konr \\\"پسر، مردِ نژاده\\\" و از آن ahd. kuning \\\"شاه\\\"، یعنی \\\"وابسته به تباری نژاده\\\"». تصویر ۴۵۰ نقطه‌ایِ صفحهٔ چاپی به‌روشنی «kundigaz» را نشان می‌دهد؛ پس این خطای چاپی خودِ کتاب است (آمیزهٔ *kundjaz/*kundiz با *kuningaz) نه خطای خوانش اسکن.\",\n \"error_in\": \"book\",\n \"book_prints\": \"kundigaz\",\n \"correct_form\": \"*kuningaz\",\n \"sources\": [\"https://www.etymonline.com/word/king\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins s.v. gene-: '§1 Suffixed zero-grade form *gn̥-yo- in Germanic *kunjam, family, in: a. Old English cyn(n) ...: KIN; b. *kuningaz, king (< \\\"son of the royal kin\\\"), in Old English cyning, king: KING. §2a Germanic *kundjaz, family, race, in Old English cynd, gecynd(e) ...: KIND.' The source Nourai cites has *kundjaz and *kuningaz — never *kundigaz.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 578 (leaf 586)\", \"stance\": \"supports\",\n    \"note\": \"'got. kuni, ahd. (usw.) kunni \\\"Geschlecht\\\" ... anord. konr \\\"Sohn, edelgeborener Mann\\\" (Abl. ahd. usw. kuning \\\"König\\\", d. i. \\\"einem edlen Geschlechte angehörig, ihm entsprossen\\\")'.\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. king\", \"stance\": \"supports\",\n    \"note\": \"'a late Old English contraction of cyning \\\"king, ruler\\\" ... from Proto-Germanic *kuningaz ... possibly related to Old English cynn \\\"family, race\\\" (see kin), making a king originally a \\\"leader of the people\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 373-375\", \"stance\": \"supports\",\n    \"note\": \"'Germanic kindi- in Gothic kindins \\\"provincial governor\\\" ... Old Norse konr \\\"son, noble-born man\\\" (Germanic *kuningaz in Old High German kuning \\\"king\\\")'.\"},\n   {\"src\": \"BOOK\", \"where\": \"pdf p. 171 (data/verification/sources/refs/ocr/BOOK/171.png)\", \"stance\": \"supports\",\n    \"note\": \"the Germanic box prints 'kundjaz : family / kundigaz : royal born, king'.\"}\n ]\n})\n\nN({\n \"id\": 19, \"lang\": \"English\",\n \"words\": \"kind, king\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"kind (noun and adjective) continues Old English cynd / gecynd(e) 'origin, birth, race, nature' < PGmc *kundjaz / *kundiz < *ǵn̥h₁-ti-, the semantic path being 'inborn nature' > 'natural, fitting' > 'benevolent' for the adjective. king is Old English cyning, contracted to cyng/king in late Old English, from PGmc *kuningaz, formed with the -ing- patronymic/appurtenance suffix on *kunjam 'family', hence 'one of (noble) kin'. Etymonline notes that although the exact notional relation is debated, 'the etymological relation [of king with kin] is hardly to be doubted'.\",\n \"derivation_fa\": \"واژهٔ kind (هم اسم و هم صفت) دنبالهٔ cynd / gecynd انگلیسی کهن «اصل، زایش، سرشت» است از ژرمنی *kundjaz/*kundiz و آن از *ǵn̥h₁-ti-؛ تحول معنایی آن چنین بوده: «سرشتِ زادی» ← «طبیعی، درخور» ← «مهربان». واژهٔ king نیز از cyning انگلیسی کهن است که در اواخر آن دوره به cyng کوتاه شده، از ژرمنی *kuningaz، ساخته‌شده با پسوند نسبتِ -ing بر *kunjam «خاندان»، یعنی «از تبارِ (نژاده)». اتیمانلاین می‌گوید هرچند در جزئیاتِ رابطهٔ مفهومی king با kin بحث است، «پیوند ریشه‌شناختی آن دو را به‌سختی می‌توان انکار کرد». ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/king\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference; the parent Germanic box cites AHD.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gene- §1b, §2a\", \"stance\": \"supports\",\n    \"note\": \"'*kuningaz, king (< \\\"son of the royal kin\\\"), in Old English cyning, king: KING'; 'Germanic *kundjaz ... in Old English cynd, gecynd(e), origin, birth, race, family, kind: KIND'.\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. king\", \"stance\": \"supports\",\n    \"note\": \"'from Proto-Germanic *kuningaz ... \\\"The exact notional relation of king with kin is undetermined, but the etymological relation is hardly to be doubted\\\" [Century Dictionary].'\"}\n ]\n})\n\ndoc = {\n  \"pdf_page\": 171,\n  \"book_page\": 141,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [entry]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-171.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build171.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-171.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 171"
}
```


### [2026-09-05T21:02:04.195Z] TOOL RESULT

```
written
JSON OK
nodes verified: 19/19
node verdicts: {'plausible': 3, 'confirmed': 12, 'unverified': 1, 'disputed': 1, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 16, 'partial': 6, 'not_checked': 5}
books consulted: {'partial': 8, 'supports': 38, 'silent': 3, 'contradicts': 2} | by book: {'KLN': 9, 'AHD': 6, 'Etymonline': 6, 'WLD': 5, 'Wiktionary': 4, 'POK': 4, 'CHEUNG': 3, 'BOOK': 3, 'BRT': 2, 'KNT': 2, 'MON': 2, 'SOD': 1, 'PHD': 1, 'HRN': 1, 'BQT': 1, 'LAT': 1}
```


## [2026-09-05T21:02:25.409Z] AGENT

Done. `verify_check.py 171` reports 19/19 nodes, 0 PROBLEM lines.

**Page 171 (book p. 141), root "Gene 1" = PIE \*ǵenh₁- — root confirmed (Pokorny IEW 373–375, Watkins, Cheung, Wiktionary).**

Verdicts: confirmed 12 · plausible 3 · disputed 1 · transcription_suspect 2 · unverified 1 (root: confirmed).
Ref checks: supports 16, partial 6, not_checked 5. Books consulted: POK, WLD, AHD/Watkins, KLN, BRT, KNT, HRN, PHD, CHEUNG, SOD, BQT (vols 1/3/4), MON, LAT, Etymonline, Wiktionary.

Flagged items:
- **disputed — #7 Persian قرمز qermez** (drawn straight from Sanskrit kṛmi-ja): modern view is a round trip — NP qermez ← Arabic qirmiz ← Middle Iranian \*kermest (PII \*kŕ̥miš "worm"), the inherited doublet being کرم kerm; the qāf rules out direct inheritance. Mo'in's footnote (BQT ~1527) still gives Sanskrit but records the Arabic route.
- **transcription_suspect — #18 Germanic "kundigaz : royal born, king"** (`error_in: book`): AHD, which Nourai cites, has \*kuningaz for "king" (and \*kundjaz "family", which he gets right); "kundigaz" is a misprint blending the two. Page image checked at 450 dpi.
- **transcription_suspect — #12 Persian «جرم» in the French box** (`error_in: book`): the page prints جرم with a single-dot jīm (the Arabic word "mass/crime"); the intended French loan germe should be ژرم. Mo'in has no French جرم. The other four (ژنرال، ژاندارم، ژنراتور، ناسیونال) are confirmed.
- plausible: #1 (Av. "ni-zâti" is unattested — Horn writes \*nizāti-, Avestan has nizanta-), #14 (Greek "eu-genos" should be εὐγενής), and #8 (Arabic qirmiz: Klein's Sanskrit source vs. Wiktionary's Iranian one).
- #5 unverified: the box is genuinely **empty in the printed book** (extraction faithful).

Extraction errors for the owner to fix: **none** — the JSON matches the printed page everywhere, including جرم and kundigaz.

Incidental finding: Nourai's BQT page list for node #3 maps to 34=آزاد, 995≈زادن, 1459=فرزند, **2134=نژاد** (not میرزا); KNT:211 matches Kent's lexicon entry "zana- sb. 'human being'" verbatim; POK:376 for zana- is one page late (the material is on p. 375, inside ĝen-1). Page PNG archived at `data/verification/sources/refs/ocr/BOOK/171.png`; 7 web pages archived via `fetch_source.py`.
