# Verification process log — verify-page-400


## [2026-09-14T00:52:53.105Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 400 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-400.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-400.json. Write /home/sfmqrb/git/rishe/data/verification/page-400.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 400` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:52:54.220Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:52:54.998Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:52:55.010Z] TOOL RESULT

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


## [2026-09-14T00:52:55.492Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-400.txt"
}
```


### [2026-09-14T00:52:55.511Z] TOOL RESULT

```
1	=== PDF page 400 (book page 370) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pet 1 : to fly, to fall  (refs POK:825)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:825; HRN:22 | ptâta, tâta : falling ; ava-pat : to fall down ☞Au 2
5	  #2 (parent #1) [Pahlavi] refs=BQT:145 | oftâtan : to fall down
6	    #3 (parent #2) [Persian] refs=BQT:145 | oftâdan «افتادن» : to fall down
7	  #4 (parent #1) [Avestan] refs=AEF:382; HUB:41 | patta : fallen, low, inferior | NOTE: HRN:70 claims it is from a different root.
8	    #5 (parent #4) [Persian] refs=AEF:382 | past 1 «پَست ۱» : low, inferior
9	#6 (parent #0) [Avestan] refs=POK:825 | pataiti, patayeiti : flies ; patareta : flying
10	  #7 (parent #6) [Avestan] refs=POK:825 | fra-ptaražât : bird ☞Per 1 ; paiti-pasti : approach, step ☞Per 3
11	#8 (parent #0) [Old Persian] refs=POK:825; KNT:194 | pat : to fly
12	  #9 (parent #8) [Old Persian] refs=POK:825; KNT:194 | ud-pat : rise up, rebel ☞Ud 1 ; ud-a-pat-atâ : arose, rose up ☞Ud 1
13	#10 (parent #0) [Avestan / Old Persian] refs=POK:825; BRT:458 | karši-ptan : swift flying (bird) ☞Ôku | NOTE: Compare with Latin "acu-pedius"
14	  #11 (parent #10) [Pahlavi] refs=HRN:191 | karšift : a fast bird
15	    #12 (parent #11) [Persian] refs=BQT:1659; HRN:191 | kašak «کَشَک» : a fast bird, magpie | extra: کَبَک ، کَشکِرک
16	#13 (parent #0) [Germanic] refs=AHD | fethro : feather
17	  #14 (parent #13) [English] refs=None | feather
18	#15 (parent #0) [Latin] refs=AHD; BRT:458 | petere : to go forward ; piter : fly ; acci-piter, acu-pedius : a swift flying bird, falcon ☞Ôku
19	  #16 (parent #15) [English] refs=AHD | compete, repeat ; accipiter
20	#17 (parent #0) [Greek] refs=AHD | petron : wing ; helik-pter : spiral wing
21	  #18 (parent #17) [French] refs=AHD:611 | helîcopter
22	    #19 (parent #18) [Persian] refs=MON:5165 | helîcopter «هلیکوپتر» : helicopter
23	    #20 (parent #18) [English] refs=AHD | helicopter
24	#21 (parent #0) [Sanskrit] refs=POK:825 | patita : fallen, low
25	#22 (parent #0) [Greek] refs=AHD | pipo : to fall ; potamos : falling water, river ; hipos ho potamios : river horse, hippopotamus ☞Ekwos
26	  #23 (parent #22) [English] refs=None | hippopotamus
27	
```


## [2026-09-14T00:52:59.036Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-400.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:8000])\n\"",
 "description": "Dump page-400 source JSON"
}
```


## [2026-09-14T00:52:59.860Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:53:00.296Z] TOOL RESULT

```
{
 "pdf_page": 400,
 "book_page": 370,
 "entries": [
  {
   "root": {
    "name": "Pet 1",
    "lang": "Indo-European",
    "refs": "POK:825",
    "gloss": "to fly, to fall"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan / Old Persian",
     "refs": "POK:825; HRN:22",
     "words": [
      {
       "translit": "ptâta, tâta",
       "gloss": "falling",
       "script": null
      },
      {
       "translit": "ava-pat",
       "gloss": "to fall down",
       "script": null,
       "see": [
        "Au 2"
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
     "lang": "Pahlavi",
     "refs": "BQT:145",
     "words": [
      {
       "translit": "oftâtan",
       "gloss": "to fall down",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 2,
     "lang": "Persian",
     "refs": "BQT:145",
     "words": [
      {
       "translit": "oftâdan",
       "gloss": "to fall down",
       "script": "افتادن"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 1,
     "lang": "Avestan",
     "refs": "AEF:382; HUB:41",
     "words": [
      {
       "translit": "patta",
       "gloss": "fallen, low, inferior",
       "script": null
      }
     ],
     "script_extra": null,
     "note": "HRN:70 claims it is from a different root.",
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "Persian",
     "refs": "AEF:382",
     "words": [
      {
       "translit": "past 1",
       "gloss": "low, inferior",
       "script": "پَست ۱"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:825",
     "words": [
      {
       "translit": "pataiti, patayeiti",
       "gloss": "flies",
       "script": null
      },
      {
       "translit": "patareta",
       "gloss": "flying",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 6,
     "lang": "Avestan",
     "refs": "POK:825",
     "words": [
      {
       "translit": "fra-ptaražât",
       "gloss": "bird",
       "script": null,
       "see": [
        "Per 1"
       ]
      },
      {
       "translit": "paiti-pasti",
       "gloss": "approach, step",
       "script": null,
       "see": [
        "Per 3"
       ]
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 8,
     "parent": 0,
     "lang": "Old Persian",
     "refs": "POK:825; KNT:194",
     "words": [
      {
       "translit": "pat",
       "gloss": "to fly",
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
     "lang": "Old Persian",
     "refs": "POK:825; KNT:194",
     "words": [
      {
       "translit": "ud-pat",
       "gloss": "rise up, rebel",
       "script": null,
       "see": [
        "Ud 1"
       ]
      },
      {
       "translit": "ud-a-pat-atâ",
       "gloss": "arose, rose up",
       "script": null,
       "see": [
        "Ud 1"
       ]
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 10,
     "parent": 0,
     "lang": "Avestan / Old Persian",
     "refs": "POK:825; BRT:458",
     "words": [
      {
       "translit": "karši-ptan",
       "gloss": "swift flying (bird)",
       "script": null,
       "see": [
        "Ôku"
       ]
      }
     ],
     "script_extra": null,
     "note": "Compare with Latin \"acu-pedius\"",
     "quote": null
    },
    {
     "id": 11,
     "parent": 10,
     "lang": "Pahlavi",
     "refs": "HRN:191",
     "words": [
      {
       "translit": "karšift",
       "gloss": "a fast bird",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 12,
     "parent": 11,
     "lang": "Persian",
     "refs": "BQT:1659; HRN:191",
     "words": [
      {
       "translit": "kašak",
       "gloss": "a fast bird, magpie",
       "script": "کَشَک"
      }
     ],
     "script_extra": "کَبَک ، کَشکِرک",
     "note": null,
     "quote": null
    },
    {
     "id": 13,
     "parent": 0,
     "lang": "Germanic",
     "refs": "AHD",
     "words": [
      {
       "translit": "fethro",
       "gloss": "feather",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 14,
     "parent": 13,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "feather",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 15,
     "parent": 0,
     "lang": "Latin",
     "refs": "AHD; BRT:458",
     "words": [
      {
       "translit": "petere",
       "gloss": "to go forward",
       "script": null
      },
      {
       "translit": "piter",
       "gloss": "fly",
       "script": null
      },
      {
       "translit": "acci-piter, acu-pedius",
       "gloss": "a swift flying bird, falcon",
       "script": null,
       "see": [
        "Ôku"
       ]
      }
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
      {
       "translit": "compete, repeat",
       "gloss": null,
       "script": null
      },
      {
       "translit": "accipiter",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 17,
     "parent": 0,
     "lang": "Greek",
     "refs": "AHD",
     "words": [
      {
       "translit": "petron",
       "gloss": "wing",
       "script": null
      },
      {
       "translit": "helik-pter",
       "gloss": "spiral wing",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 18,
     "parent": 17,
     "lang": "French",
     "refs": "AHD:611",
     "words": [
      {
       "translit": "helîcopter",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 19,
     "parent": 18,
     "lang": "Persian",
     "refs": "MON:5165",
     "words": [
      {
       "translit": "helîcopter",
       "gloss": "helicopter",
       "script": "هلیکوپتر"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 20,
     "parent": 18,
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "helicopter",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 21,
     "parent": 0,
     "lang": "Sanskrit",
     "refs": "POK:825",
     "words": [
      {
       "translit": "patita",
       "gloss": "fallen, low",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 22,
     "parent": 0,
     "lang": "Greek",
     "refs": "AHD",
     "words": [
      {
       "translit": "pipo",
       "gloss": "to fall",
       "script": null
      },
      {
       "translit": "potamos",
       "gloss": "falling water, river",
       "script": null
      },
      {
       "translit": "hipos ho potamios",
       "gloss": "river horse, hippopotamus",
       "script": null,
       "see": [
        "Ekwos"
       ]
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 23,
     "parent": 22,
     "lang": "English",
```


### [2026-09-14T00:53:00.339Z] TOOL RESULT

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


## [2026-09-14T00:53:16.054Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-400.json'))\nprint(json.dumps(d['entries'][0]['nodes'][-1],ensure_ascii=False))\nprint(len(d['entries']),'entries; nodes',len(d['entries'][0]['nodes']))\n\" ; sed -n 1,60p tools/verify_check.py",
 "description": "Check last node and verify_check script"
}
```


### [2026-09-14T00:53:17.178Z] TOOL RESULT

```
{"id": 23, "parent": 22, "lang": "English", "refs": null, "words": [{"translit": "hippopotamus", "gloss": null, "script": null}], "script_extra": null, "note": null, "quote": null}
1 entries; nodes 23
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


## [2026-09-14T00:53:17.764Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nr=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','HUB','AEF','BQT','KNT','BRT','AHD','MON']:\n    print(k, json.dumps(r.get(k),ensure_ascii=False)[:600]); print()\n\"",
 "description": "Refs online entries"
}
```


### [2026-09-14T00:53:18.839Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
```


## [2026-09-14T00:53:23.151Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | head -50\ngrep -n \"pet-\\b\" POK_full.txt | head -20\necho ---\ngrep -n \"825\" POK_full.txt | head -5",
 "description": "Grep Pokorny for pet-"
}
```


### [2026-09-14T00:53:23.218Z] TOOL RESULT

```
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
64679:See also: see below pet-1. 
67266:Root / lemma: pet-1, pet-, peta- 
67304:Root / lemma: pet-2, peta- : pte- pto- (gr. pta^ 
67392:{*petema)\ abret. a//a/7c»c"volitans'; Middle Irish ette, nir. e/fe' wing ' (from *pet-entia). 
67393:Middle Irish etha/t'b\r6' = Old Indie /Oa/5/7//"fliegend' {*pet-ontl)\ Middle Irish eithrer\. "tail' 
---
19746:References: WP. I 825. 
19881:References: WP. I 825 f., Schwyzer Gr. Gr. I 302, 703, 714, 720, WH. I 524. 
24778:References: WP. I 106 f., WH. I 717 f., Schwyzer Gr. Gr. I 282, 4825, 491, 679^, 681, 694, 
67302:Page(s): 824-825 
67436:Page(s): 825-826
```


## [2026-09-14T00:53:24.345Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==833' POK_01.txt | head -80",
 "description": "Print POK_01 leaf 833"
}
```


### [2026-09-14T00:53:25.434Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:53:28.377Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '67260,67310p' POK_full.txt\necho \"=============== pet-2 ===============\"\nsed -n '67304,67440p' POK_full.txt",
 "description": "Print Pokorny pet-1 and pet-2 entries"
}
```


### [2026-09-14T00:53:28.453Z] TOOL RESULT

```
ablaut. Middle High German i/es// "fertile', i//5e/"penis'. 

References: WP. II 68, WH. II 281. 

Page(s): 824 

Root / lemma: pet-1, pet-, peta- 

Meaning: to open wide (the arms) 

Material: Avestan pa^ana-^W\6e, breit' (das z? after yoa/-az?^-ds.); 

gr. Aor. nsTaaaai, nsTaaai, thereafter n£Tavvu|ji 'breite from, offne', previous present 
niwriMi, nirvw (from *Pet-), nsraapa n. 'curtain', -nt^aaoc, m. 'breitkrempiger hat', n£TaAo(; 
"ausgebreitef, nsraAovn. 'Platte, leaf, naravn f. ' platter ' (from *n£Tavc(; out of it Latin 
patina (is.); 

Latin pated, -ere'sich erstrecken, be open '; in addition pando, -ere 'offne, breite from' 
(the variation /: o^ expounded sich through old athemat. inflection after Kuiper, Nasalpras. 
163), passusm. ' footstep, fathom'; pateral\at bowl' (from yC>a//>75 through influence of 
crater?); whether here petrius'th\n and fragile, flimsy '??; Oscan patpWJ 'patet', patensfns 
'panderent', Volscan Imper. an-patitu '*adpanditd\ 

Scots Gaelic aitheamii {*eitheamH) ' filament ' (as measure), = acymr. etem, ncymr. 
edau ds. ( *petima); 



Old Icelandic fadmr^ hugging, embrace, fathom, filament ', FIN Fgd, Gen. Fadar, Old 
English /fed/77 mf. ds. " filament, fathom', engl. fathom. Old High German fadam, fadum^ 
filament '; here also Old English foder, engl. father. Modern High German Fuder?, Old 
High German fuodar. Old Saxon father. Old English /&dc»/'"Wagenlast', Modern High 
German Fuder, from Germanic *fddra-^6as Umfassende'; Gothic fat^a. Middle High 
German vadei. 'fence' (as ' encirclement '); Old High German /feo'e/-^c»/o''Blattgold' (:gr. 
nsTQAov), doubtful Old English ^c»/o'-/fe//"Goldplatte', Middle High German golt-veF gold 
plating '; 

Lithuanian yoe/ys "shoulder'. Old Prussian pettei. ds.; pettisxn. "shovel, scapula'; 

Hittite pattar, Dat. paddanriab\e\.\. (?)'. 

References: WP. II 18, WH. II 244 f., 262, Trautmann 217. 
Page(s): 824-825 

Root / lemma: pet-2, peta- : pte- pto- (gr. pta^ 
Meaning: to fall; to fly 



Material: Old Indie patat/lWes, wirft sich, fallt' (= TTETOMai, Latin peto, acymr. hedarit), Aor. 
apaptat, peta-\x\ Put. patisyati, Supin. patitum, participle patita-); patayat/lWes' (= gr. 
=============== pet-2 ===============
Root / lemma: pet-2, peta- : pte- pto- (gr. pta^ 
Meaning: to fall; to fly 



Material: Old Indie patat/lWes, wirft sich, fallt' (= TTETOMai, Latin peto, acymr. hedarit), Aor. 
apaptat, peta-\x\ Put. patisyati, Supin. patitum, participle patita-); patayat/lWes' (= gr. 
noT£0|jai), yoa/aya// "allows fliegen, hurl, sling, fling, allows fall' (lengthened grade as pata- 
m. "Plug, fall, Sturz', gr. nwraoijai "flattre'), pra-pat-'\r\\ne\\en, fall', patman-n. "Plug, path, 
track, pathway' (: n6T|jO(;, noTa|j6(;); Avestan pata/t/lWes, hurries ', ap. ud-apatata ' erhob 
sich', Avestan pataye/t/ IWes', acapastd/s\ni. "hinabzufallen', paitipasti-i. "Entgegengehen, 
-treten' (compare Old Indie at/-patt/- ^Ze\tab\auV), from an u-present parapa^want- 
"fortfliegend (of arrow)'; Avestan tata-{*ptata-), "fallend (of rain': gr. htcjotoc; ds.); 

Armenian t'fc/m'\ fliege' {*pter-i-skd). 

gr. hom. TTeTO|jai "fliege' (snroijriv); otherwise also nsTapai, eiTTaTO "entflog', nTC((;, 
enrnv, Doric enrav. Put. nrnaopai; cbKunEiri^ "quick, fastfliegend', n£T£r|v6q, (*n£T£aav6(;), 
n£T£iv6(; (*n£T£av6(;) "geflijgelt, flugge', norn "Plug', noTav6(;, -r|v6(; "zum Pliegen befahigt, 
beflijgelt, fliegend', rroTaofjai (and noiEopai, see above) "flattre', nwTaopai ds., nrnaiq, by 
Suidas nrnpia "Plug', nrnvoq, Doric -niONOC, "fliegend'; 

stem TTSTa-, nra- "fly', but nsTS-, nrr)-, htcjo- with the meaning "fall': ni:-nTU) (for *nT-nTaj 
after pinru)) "fall'; Perf. nsnTajKa, participle nEnrncbc;, Attic nsnTcbc; from *n£nTau)(;; 
anTU)(;(Pind.), anTn(; (Doric inschr.) "not fallend, nicht dem Palle ausgesetzt'; nirvu) "fall'. 



eu-"rT£Tr|(; " comfortable, gijnstig', TTpo-TT£Tn(; "vorwarts fallend, willing, inclined' (: Old Indie 
pra-pat-), -ntaoo, n.(Gen. n£a£0(;from *tt£T£0(;) "cadaver", tt6tpo(; "lot, fate, fate, destiny, 
esp. trauriges', noTa|j6(; "river", actually "Wassersturz"; nTwpa, nrwaK; "fall' (: n£nTU)Ka); 
nrcoToq "fallend"; 

with the meaning-farbung of Latin petere:<^x. niTuAo(; " intense movement' (: Latin 
petulans, compare also £|jn£a£Tv "impetum facere'); 

finally has TTia- : nru)- : nra- also die probably from "niederstijrzen' development 
meaning "sich niederducken' and "verzagt, in fear sein': Kara-nTriTriv "(the horse) 
scheuten', n£nTr|U)<; "geduckf, nroia " fear, shyness, fright' (*nT(ji)Fic(, compare Ar|TU) 
riTcba, AnoAAwv FItcooc;), nTo(i)£Tv "frighten, in BestiJrzung versetzen'. Pass, "from 
Schrecken ergriffen become'; with guttural extension nrriaau) (*nTC(K-j(ji)) "ducke myself 
(Aor. £nTr|^a, Doric EnraKa also trans, "frighten'; Kara-nTaKcbv), nrojOKa^u) "ducke myself 
timorous, flee', nrcbaou) (*nT(ji)KaKi(jL)) ds.; nrcb^, -koc, "shy, fleeting ' (m. "hare'), ablaut. 
TTTQ^ m. f. " wimp ', Gen. nraKOc;; htcjoxo^ " beggar'; to letzteren, as it seems, also 
Armenian t'ak'cim, t'ak'eay^sich conceal'; 

Latin peto, -ere, -TvT, Ttum "auf etwas losgehen, to attain seek, long, want' {petT-tor, -tio, 
also probably yoe//^o" mange; scabies ' as "Befall'); petu/ans ^ aggress'w , pert, bratty, 
exuberant ', pe/^/c^s "pushing, thrusting ' (from *petulus, compare to Aforms gr. niTuAo(;), 
//77yoe'/i/s "assault, attack', praepes'm Fluge vorauseilend; quick, fast'; 

acymr. hec/anf'\/o\ant', ncymr. eh-ec/eg'6as Fliegen'; eh-edyddm. " lark '; 

Latvian yoe//'/ "desire have, nachforschen'. 

A-and /^formations: 1. with dem ^^forms Old Indie /05/5/77^a-"fliegend, bird', pataga- 
"bird' {*petn-go-s, from den Indern as "in Fluge going' reinterpreted); Avestan fraptarejat- {- 
jant-) "bird'; gr. tttepu^, -uyo(; "wing' (compare Old Indie pa/am-); das Denom. nTspuoaoMai 
"hit with den Flijgeln' after aiGuaou) "shake'; Old High German fed(e)rah^\N\v\g\ anfrk. 
/e/^eAscco "alarum' (-a-c- through influence of Old High German fedara-, anfrk. fethera); 

2. Old Indie pattra-, pata-tra-v\. "wing, feather ', patara-, pa/a/z/-"fliegend', Avestan 
yoa/a/p/a- "fliegend'; Armenian ///""Flug', t'itern^ butterfly' (redupl.), /'e/f'"leaf, foliage' 
( *pter-)\ gr. nrspov " feather, wing'; nrspK; "Farn'; 

Latin acci-piter, -pitris^ hawk, falcon' (to 1. part see below *d/r^- "quick, fast'); penna^ 
feather, wing' ( *petna)\ (under the influence of common Celtic -ns-, -nt- > -nn-), Old Latin 



pesna from *pets-na; p/nna'\s probably dial, form ior penna; pro(p)tervus' boisterous 
vordringend, cheeky ' {*pro-pteru-o-)\ 

Maybe alb. {*penna) pende leather' a Latin loanword. 

Maybe zero grade alb. sk/fter' hawk, falcon ', shq/ptar' eagle man ' are Latin loanwords. 
From there derived alb. shqipe, shkabe, shqiponje, zhgabonje, gabonje^ eagle' (common 
k- >^-guttutals in Celtic Baltic, also common alb. p- > b-). Also alb. shqiptoj^ speak, 
pronounce ', shqip^ Albanian language '. The name shqiptar' eagle man ' evolved after 
the Turkish invasion of Arberia (former Albania). Settlers who escaped to southern Italy 
before the invasion still call themselves Arberesh. The alb. name shqip\s unintelligible to 
Arberesh in Italy, the alb. name of the eagle derived from the banner of Albanians before 
the Turkish occupation, the double headed imperial eagle. 

acymr. e/e/7/7"bird', PI. atar, ncymr. aderyn, adar6s. (5 secondary from e); Old Irish en 
"bird' {*petno-), cymr. edn, acorn, hethen ds., abret. etn-coilhaam^\\o\6 Vogelschau', 
Middle Breton ezn, nbret. evn, e//7"bird', acymr. atari {*peteno-), ncymr. ada/n'\N\r\g, arm ' 
{*peten-), bret. (h)adan^ nightingale ', with secondary a, as cymr. adar\N\r\g, hand' 
{*petema)\ abret. a//a/7c»c"volitans'; Middle Irish ette, nir. e/fe' wing ' (from *pet-entia). 
Middle Irish etha/t'b\r6' = Old Indie /Oa/5/7//"fliegend' {*pet-ontl)\ Middle Irish eithrer\. "tail' 
( *peterio-); 

Note: 

Common Armenian ph- > h-, zero, spread in Sanskrit and Celtic 

ANATOLIAN 

Hittite pa/a- 'foot' 

WEST EUROPEAN 

Latin pe:s, pedis 'foot, of foot' 

Old Irish water' 

Tocharian A pats 'foot' 

SOUTH EUROPEAN 

Greek pous, podos 'foot, of foot' 

Armenian otn, otk"ioo{, feet' 

Sanskrit a:ts 'foot', pa.dam (accusative case) 

Avestan pad- 'foot' 



Old High German fedara, anfrk. fethera. Old English feder, Old Icelandic fjgdri. " feather 
' {*petra)\ Old High German fettah. Middle High German vittich. Middle Low German 
vit(te)k. Modern High German Fittich; 

Hittite pattaru.. Gen. PI. paddanas^ muo^'. 

*ptei-, pti-i^r. irTaiw "stofte an etwas (intr.), strauchle, irre, have whereas misfortune' 
(nraiaw, Enraiapai, sniaiaGriv), rare tr. "bump, poke, umstijrzen', nraTaija "damage, loss, 
misfortune, beating ', iGunfiwv "geradaus fliegend' (probably actually "geradaus treffend = 
pushing, thrusting, aufschlagend'), nriAov " feather, Flaumfeder'. 

References: WP. 1119 ff., WH. II 282 f., 297 f. 
Page(s): 825-826 

Root / lemma: peuR- and peug- 

Meaning: to stick; to punch
```


## [2026-09-14T00:53:59.731Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT karsipta ===\"; grep -n -i \"kar.ipta\\|karsipta\\|karsipt\" BRT.txt | head -20\necho \"=== HRN karsift/kaskarak ===\"; grep -n -i \"karsift\\|kar.ift\\|ka.ak\\b\" HRN.txt | head -30\necho \"=== PHD obastan/oftadan ===\"; grep -n -i \"ftadan\\|obastan\\|ʾwpstn\\|awbastan\" PHD*.txt | head -20\necho \"=== NYB ===\"; grep -n -i \"ptʾt\\|obast\\|ōbast\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep BRT, HRN, PHD, NYB"
}
```


### [2026-09-14T00:53:59.818Z] TOOL RESULT

```
=== BRT karsipta ===
9369:•  j.  karäiptar-  m.  Name  eines  Vogels, I 'accipiter'*' ■':   kö  avalia  dainqm  mSzda-
=== HRN karsift/kaskarak ===
7281:ap. aw. kama- 'Wunsch, Wille*; phlv. kamak,
7319:in der Stammsilbe {kebk aus *kapak) sind sie aber
7354:katak 'Grabstätte; Haus', katak\xutü^ katak\banüklh
=== PHD obastan/oftadan ===
PHD.txt:518:6 [OL < А Ч; ?w | M ’w] to, at; v. also 6h. ~ gird ámadan: gather, collect (intr.). — ham kardan: gather (tr.). ~ ham madan: gather (¿ntr.); come to an end. *óbad-, v. bastan, *óftadan. Obārdan, bär- Dwf?l-tn! | M ?wb’rd] swallow, devour. Obastan, *dbad- [NPLWN-stn! < A У npl; ^wpstn!, ^wpt- (if not Oft-, q.v.) | M ?wbyst, J ^wfst-] fall. *oftadan, Oft- Pwpt- | M *wpt'd, N uft~] fall. Gear Pwk’l] ebb. ogardan, ógàr- Pwk’l-tn'] remove, expel. *брга ['wgPy] declination, dip. Sh [KN < A kn | Mwh] so, thus; (with verbs, giving a sense of uncertainty) may, perhaps. Ohrmazd Pwhrmgd | M ^whrm(y)zd, N Hórmuzd] Ahura Mazda; astr. Jupiter; cal. 1st day of the month. -om [-wm | = M, N ~] suffix forming ordinal numbers from panjom onwards. -mand [-’wmnd | M -wmnd, N -mand] suffix forming adjectives of quality. *óréb(ih) [wlyp(yh)] disappointment. Dron ['cwlwn! | Mwrwn] hither. ад... ~: since. osán- Pws*n- | = M] throw down. óspurdan, ӧѕраг- [”zospl-tn!] tread, trample. 051°, v. awest^. Ost [220511] firm, reliable. ostigàn Pwstyk’n! | M Iwstyg^n, N ustuwàn?] firm, strong, sure, reliable. ~ih: reliability. lēš [wf | = M, N Ads] consciousness, intelligence. mih: = 68. 268 [wf | = M] death.
PHD.txt:5146:nifrin wafrūnag nifrīdag Obad-/oft-1 Obastan! nibard- nibardīdan nibard nibardag nibastan wabz wafišn xwest xwestant nibistan 1-2paft waz- wizār wizür- wizarisn wizārdan wizārdwars wizīh-
PHD_mackenzie.txt:3836:·obad-,v.obastan,·oftadan.
PHD_mackenzie.txt:3838:obastan, .obad- [NPLWN-stn l < A ...; npl; )wpstn', )wpt- (if not oft-,
PHD_mackenzie.txt:3840:·oftadan, Oft- [)wpt- I M )wpt)d, N uft-] fall.
PHD_mackenzie.txt:6538:evil-minded duswir.                                fall kaftan, obastan, Oftiidan, pad-.
PHD_mackenzie.txt:9965:obastanl           \'~ \~Q)\            wistax                   ,~~,
PHD_mackenzie.txt:11864:hucasmih                ~qt""              obastan                    \\M» Q)yt
PHD_pages.txt:3836:·obad-,v.obastan,·oftadan.
PHD_pages.txt:3838:obastan, .obad- [NPLWN-stn l < A ...; npl; )wpstn', )wpt- (if not oft-,
PHD_pages.txt:3840:·oftadan, Oft- [)wpt- I M )wpt)d, N uft-] fall.
PHD_pages.txt:6538:evil-minded duswir.                                fall kaftan, obastan, Oftiidan, pad-.
PHD_pages.txt:9965:obastanl           \'~ \~Q)\            wistax                   ,~~,
PHD_pages.txt:11864:hucasmih                ~qt""              obastan                    \\M» Q)yt
=== NYB ===
891:(the gods) allot subsequently' — Borrow- ed from Av. (922) baydbaxta-; Paz. bayobast, Skr. v. punar-dati, -bhāgya.
```


## [2026-09-14T00:54:01.914Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins pet ===\"; grep -n -i \"^pet-\\|pet-1\\|pet-2\\|To rush, fly\" AHD_watkins1985.txt | head -20\necho \"=== KNT pat ===\"; grep -n -i \"ud-a-pat\\|udapatata\\|pat-\" KNT.txt | head -30",
 "description": "Grep AHD and Kent"
}
```


### [2026-09-14T00:54:01.974Z] TOOL RESULT

```
=== AHD watkins pet ===
843:pet-
844:fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
=== KNT pat ===
3755:77 yasiya : yàtà : adam : Parsaiy : u(t)à : Madaiy : àham : рабу : duvitiyam : j 78 Babiruviya : hamiçiyā : abava : hacàma : I martiya : Атха : nàma : Armini 79 ya : Halditahya : puça : hauv : udapatata : Babirauv : Dubála : пата : dahy&
5593:napüt- sb. ‘grandson’: Av. Skt. napat-, Lt.’
5618:mi- + pub- ‘engrave, inscribe, write’: niyapat- Sam Ist sg. aor. ($02, $102, $130, $218.T, $226.IT) DB 4.71. mipaislanaty inf. ($03, $122, $288) XV 24f. nipislam asf. past ptc. pass. (803) XV 22f.
5623:pal- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. vérerat, Lt. рені ‘seeks’, pIE *pet-.
5624:ud- + pat- ‘rise up, rebel’ (cf. Ву. TPS 1945.64-
5638:Patigraband- sb. ‘Patigrabana’, a town in Parthia: Elam. pat-t-ig-rdb-ba-na; from pati- + root grab- + suffix (833, $103.IV, §147.1). Pati- graband nsf. DB 3.4f.
```


## [2026-09-14T00:54:12.764Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD pet- ===\"; sed -n '843,848p' AHD_watkins1985.txt | cut -c1-4000\necho; echo \"=== KNT lexicon pat ===\"; sed -n '5615,5640p' KNT.txt",
 "description": "Print AHD pet- and Kent lexicon"
}
```


### [2026-09-14T00:54:12.818Z] TOOL RESULT

```
=== AHD pet- ===
pet-
fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
pete-
ré, feather, in Old English fether, feather: FEATHER. 2. Latin petere, to go toward, seek: -PETAL, PETITION, PETULANT; APPETITE, COMPETE, IMPETUS, PERPETUAL, REPEAT. 3. Suffixed form *pet-nd in Latin penna, pinna, feather, wing: PANACHE, PEN!, PENNA, PENNATE, PEN- NON, PINNA, PINNACLE, PINNATE, PINNATI-, PINNULE. 4. Suffixed form *pet-ro- (see 6ku-). 5. Suffixed form *pet-yo- in Latin propitius, favorable, gracious, originally a religious term meaning “falling or rushing forward,” hence “eager,” “well-disposed” (said of the gods; pro-, forward; see per'): PROPITIOUS. 6. Suffixed zero-grade form *pt-ero- in Greek pteron, feather, wing, and pterux, wing: -PTER; ACANTHOPTERYGIAN, APTERYX, ARCHAEOP- TERYX, COLEOPTERA, MECOPTERAN, PERIPTERAL, PLE- COPTERAN, PTERIDOLOGY, PTEROCERCOID, PTERYGOID. 7. Suffixed zero-grade form “pt-ilo- in Greek ptilon, soft feathers, down, plume: COLEOPTILE. 8. Suffixed variant form *pté-no- in Greek pténos, winged, flying: STEAROP- TENE. 9. Reduplicated form *pi-pt- in Greek piptein, to fall: PTOMAINE, PTOSIS; PERIPETEIA, PROPTOSIS, SYMP- TOM. 10. O-grade form “pof- in Greek potamos (-amo-, Greek suffix), “rushing water,” river: HIPPOPOTAMUS. [Pok. 2. pet- 826.] pete-. To spread. 1. Suffixed o-grade form “pota)-mo- in Germanic *fathmaz, “length of two arms stretched out,” in Old English fethm, fathom: FATHOM. 2. Suffixed (stative) variant zero-grade form *pat-é- in Latin patére, to be open: PATENT, PATULOUS. 3. Variant zero-grade form in nasalized form *pat-no- probably in Latin pan- dere (past participle passus < *pat-to-), to spread out: PACE!, (PAS), (PASS), PASSIM; EXPAND, REPAND. 4. Suf- fixed form *pet-alo- in Greek petalon, leaf: PETAL. 5. Suf- fixed form *pet-ano- in Greek patané (? < *petand), platter, “thing spread out”: (PAELLA), PAN!, PATEN, (PATINA!), (PATINA2). [Pok. 1. pet- 824.] [petra. Cliff. Greek noun. Collective formation from petros, rock, stone (of unknown origin). PETRO-, PET- ROUS; PARSLEY, PETRIFY, SALTPETER.] peu-. To cut, strike, stamp. 1. Suffixed (participial) zero-grade form *pu-to-, cut, struck, in: a. Latin putdre, to prune, clean, settle an account, think over, reflect, consider: PUTAMEN, PUTATIVE; (ACCOUNT), AMPUTATE, COMPUTE, COUNT!, DEPUTE, DISPUTE, IMPUTE, REPUTE; b. possibly Latin puteus, well (> Old English pyét): Prt’. 2. Variant form *pau- in: a. suffixed form *pau-yo- in Latin pavire, to beat: PAVE, (PAVE); b. suffixed (stative) form *paw-é- in Latin pavére, to fear (< “to be struck”): PAVID; C. perhaps Greek paiein, to beat: ANAPEST. [Pok. 3. péu- 827.] peue-. To purify, cleanse. Suffixed zero-grade form *pii-ro- (< *pua-ro-) in Latin purus, pure, and purgdre, to purify (< “piir-igdre; second element agere, to drive; see ag-): PURE, PURGE, PURITAN; COMPURGATION, DEPU- RATE, EXPURGATE, (SPURGE). [Pok. 1. peu- 827.] peuk-. Also peug-. To prick. Zero-grade form “pug-. 1. Suffixed form *pug-no- in Latin pugil, pugilist, and pugnus, fist, with denominative pugndare, to fight with the fist: PONIARD, PUGILISM, PUGIL STICK, PUGNACIOUS; IMPUGN, OPPUGN, REPUGN. 2. Nasalized zero-grade form *pu-n-g- in Latin pungere, to prick: BUNG, POIGNANT, POINT, POINTILLISM, PONTIL, (POUNCE!), (POUNCE?), PUNCHEON!, PUNCTUATE, PUNCTURE, PUNGENT; COM- PUNCTION, EXPUNGE, SPONTOON, TRAPUNTO. 3. Greek pugmé, fist: (PYGMAEAN), PYGMY. [Pok. peuk- 828.] pezd-. To fart. 1. Suffixed form *pezd-i- in Germanic *fistiz, a fart, in Middle English fisten, to fart: FEIST, FIZZLE. 2. Latin pédere, to fart: PETARD. 3. Possibly Latin pédis, louse (? < “foul-smelling insect”): PEDICU- LAR. See also perd-. [Pok. pezd- 829, 2. peis- 796.] peter-. Father. 1. Germanic *fadar in Old English feder (> Middle English fader), father: FATHER; FOREFATHER. 2. Latin pater, father (> patrare, to bring about): PADRE, PATER, PATERNAL, PATRI-, PATRICIAN, PATRIMONY, PA- TRON; EXPATRIATE, IMPETRATE, PERPETRATE. 3. Greek
51
plat-

=== KNT lexicon pat ===
nüram adv. ‘now’: Av. nürom; from pIE *ná ‘now’ (Av. nū, Skt. пй, Lt. nu-nc, NEng. now) + final of (pAr.) *düram ‘long’ (§148.1), cf. düraty. DB 4.53.
pä- vb. ‘protect’: Av. pà-, pres. рйи, РЫ. pátan, Skt. pà-, pres. pati (ablaut, §122). See also zíacapüvan-. apayaiy lst sg. imf. mid. (Ву. BSLP 33.2.151-2; Kent, Lg. 9.42; S71, $214, $233.1II; wrongly to Skt. pt- ‘swell’, Wb. ЖА 41.820-1) XPf 39. padiy 2d sg. imv. (5208, §237.1) DPe 21f. pätwv (§208, $297.IT) AsH 12, 14; DPd 16; DPh 10; DNa 52; DSe 50; DSf 57; DS} 6°; D8n 2°; роз 7°; DSt 8°; ОН 8; XPa 18, 20; XPb 28; ХРе 12, 15; XPd 18; ХР 45, 48; XPg 13; XPh 57; Хе 5^; XV 25f; А:Ра 226; D'Sa 3; A?Hb^; A?He 19. pätw 3d pl. іту. (§237.1T) A'Sa 5°; A’Sd 4; А?На 6°; A?Pa 25. pála пзш. past ptc. pass. (§242.IT) DPe 22. pati- + pã- mid. ‘protect one’s self against’, with Ласа + abl.: райїрауаш@ (828; not wrongly written, despite MB Gr. §69) 2d sg. imv. mid. ($71, §214, 5297.11) DB 4.38.
paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, Paišiyđwwādā-, pisa-. аріа imf. DSf 54 (§211; cf. Konig, Burgbau 72). [ар #} уа] imf. pass. ($220) DB 4.91 (JAOS 62.268). [pjisia nsf. past pte. pass. ($242.1) DSf 42 (Bv. BSLP 30.1.62; Konig, Burgbau 71; not dista with Hz. Apī 121-5].
mi- + pub- ‘engrave, inscribe, write’: niyapat- Sam Ist sg. aor. ($02, $102, $130, $218.T, $226.IT) DB 4.71. mipaislanaty inf. ($03, $122, $288) XV 24f. nipislam asf. past ptc. pass. (803) XV 22f.
nipistü npf. XPh 31. nipistam nsn. ($122) DB 441, 47f; DNb 57°; DSe 52.
paišiyā- sb. ‘script, written text’: deriv. of pai- (§89, §144.V). See also Parsiyduvada-. ри nsf. DB 4.91 (conj. of Kent, JAOS 62.268).
PaiSiyd'uvdda- sb. ‘Paishtyauvada’: АКК. pi- &-"-hu-ma-du. Perhaps, with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of the Archives and Sacred Writings’ (on Pasargadae, ef. also Kónig, RuID 66; but Hz. ApI 275-6, modifying his view ш AMI 1.86n, takes prior element to be pati-, pati- becoming pa&-, with epenthesis; Bthl. AiW 907-8 normal- izes Piši- after the Akk., but gives no etymology). Paisiydwddim asf. DB 3.42. Parsilydluvadayd absf. DB 1.36f.
pa|camàm] adj. ‘fifth’, asf.: wrong restoration of Wb. at DB 5.8 (ef. Kent, JNES 2.109).
pal- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. vérerat, Lt. рені ‘seeks’, pIE *pet-.
ud- + pat- ‘rise up, rebel’ (cf. Ву. TPS 1945.64-
66): udapalatà imf. mid. (§84, 8213, 5285.П) DB 1.36, 38, 74, 78; 2.10, 14f; 3.24, 79.
patiy adv., prep., prefix ($140.I, $1911): Av. рай, Gk. (dial.) rori, pIE *poti, cf. pIE *proti in Skt. prát, Gk. Hom. троті, classical rpés (cf. Lg. 20.9-10).
(1) Adv. ‘thereto, again’: DB 2.37, 48, 57; 3.04, 71. pati-maty ($186) DNb 32f.  nai-pati-mà ($133, 5186) DNb 20. yadi-patiy (8136) DNa 38. (ya-patiy XPa 15; XPf 40f.
(2) Prep. (8271) with ace.: DB 52 ‘during’; DNb 22 ‘against? (Hz. ApI 273 reads par[slaiy ‘in court’, sb. to root fraé-); postposed DB 2.62 ‘on’. Encl., with ace. ‘during’ DB 1.20 (8133, $136); with inst. ‘near, at’ DB 2.16°, 3.26; with loc. ‘on, upon’ DB 2.76, 91; 3.52, 92. Ву. BSLP 42.2.70 takes all these as adverbs except DB 2.62, DNb 22.
(3) Prefix with verbs avahya-, ay-, ziay-, jan-, рӣ-, fraf-, d-bar-, zbü-; prior element in nouns palikara-, Patigraband-, perhaps Pátisuvari- and
"* 2 - -
also patiš, patisam.
patikara- sb. ‘picture, (sculptured) likeness’: .
РМ. patkar-, NPers. pátkür-;.pati- + kara- to root
as sata jeu iit И ЗАК
pores agent iain ee Seeman Re NE SS a cet ras ЧЕК ЧАС ve NEMPE
LEXICON 195
kar- ($143.V). patikaram asm. DSn 1°. palikara apm. DB 4.71, 78, 77; DNa 41.
Patigraband- sb. ‘Patigrabana’, a town in Parthia: Elam. pat-t-ig-rdb-ba-na; from pati- + root grab- + suffix (833, $103.IV, §147.1). Pati- graband nsf. DB 3.4f.
Я patipadam phrasal adv. ($191.17) ‘on its base, in its own place’: pati- ($186, $1401) + aec. padam (see pada-; 76.111, $122). DB 1.62.
palis prep. with acc. ‘against’: pati- + adv. -s, ef. Lt. ex, abs, ops- in os-lendó, sups- in sus-tined, Skt. nt and nis, Gk. ато iy, audi audis. See also patisam. DB 1.93; 2.33, 38, 43f, 52f, 58, 67; 3.36, 43, 65.
```


## [2026-09-14T00:54:14.006Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 212 (p.191) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==213' HRN.txt | head -60",
 "description": "Print Horn p.191"
}
```


### [2026-09-14T00:54:15.124Z] TOOL RESULT

```
=== HRN leaf 212 (p.191) ===
— 191 -
854. UuHt *Seite, Flanke', hu^Vl^ kustl 'Gürtel', vergl.
hergustvuan (No. 205) ; kusftgir 'Ringkämpfer (AM. 2()6
Zeile 8).
phlv. ktist^ kustak 'Seite*, kusttk^),
855. kuSten 'tödten', nt^^t^lD (Qiss. Dan.).
aw. l/ftaos-, kusaiti 'tödten'; phlv. kustan, vergl. asö]-
kvs (für aw. asavaynya-, vd. 5 (47)); skr. KÄö5-, kusnäti
'zerreissen' (?).
kurd. LW. (?) kustin 'tödton*; bei. L\V. (?) kuäag,
n. ßusay 'todten, scli lachten (207).
856. feesß/ ^Schildkröte ; Krebs (Zodiac, Sahn. I, 77 Vers
285)', keseto (dial.).
aw. kasyapu' 'Schildkröte' oder *Krebs' (Geldner,
KZ. 25, 503, 5()6j ; skr. (Brhm.) kagydpa- 'Schildkröte .
af/. kasy 'Schildkröte'; bei. käsib (190).
857. Ä-e«efc 'Elster .
Toniaschek, Painirdialokte S. 771, veigkM'cht aw.
karsiptan-^ phlv. kars{i)ft (L)eutun*i: nicht sicher), wa/.
karjöpc, sar. karjopc, si;'n. ksebc 'ElstiM-'.
858. kiSver^ kesver 'Ph-dteil'.
aw. karsvar- 'Weltteil'; phlv. kisvar^).
859. kesläen ziehen'.
aw. [/^km's-, karsayefi^); phlv. kasttan; ai. 1. [/^kars-,
• kdrsati, karmyati 'ziehen, schleppen'.
kurd. kisän ziehen'; af>'. k/dl; bei. kasay, n. /i'asay
'ziehen, abziehen, herausziehen' (19:^); arm. LW. (?)
Karsem 'ziehen*.
») Syr. LW. J^D^'ID, J^nDD, p^DDIp; ai'ab. LW. kustij (de
Lagarde, Ges. Abb. 59, 60); bei. LW. kustl (143). — Aber nicht gehört
dazu lat. c^ista *Rippe*, das Meringer, Sitzb. WAW. CXXV, *Beitr. z.
indg. Decl.*, 42, mir nicht einleuchtend, zu ai. dbthi- 'Knochen* stellt.
') Eine Volksetymologie in 'Selections of Zätsparnm* (West
P. T. I) 7, 9.
») Aw. [/has- will Hübschmann ZDMG. 44, 558 ausser Betracht
lassen.
```


## [2026-09-14T00:54:32.830Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT context 9355-9380 ===\"; sed -n '9355,9380p' BRT.txt\necho \"=== BRT col marker near ===\"; awk 'NR>=9280 && NR<=9375 && /^[0-9]{3,4}$|45[0-9]|46[0-9]/' BRT.txt | head -20",
 "description": "Bartholomae karšiptar context"
}
```


### [2026-09-14T00:54:34.092Z] TOOL RESULT

```
=== BRT context 9355-9380 ===
*)  Die  mit  einem  spitzen  Metatlstück  ge- zogenen Furchitriche  tollen  dazu  dienen,  einen Unreineti  abzusondern  und  so  der  von  ihm drohenden  Ansteckungsgefahr  zn  begegnen.  Vgl,
KompA'.,  E.  —  Zum  V.  Üari.  —  Fü.;  (zu  1): *tri),  (zu  a):  küvar.  —  i>  Mit  ir.  ar  oder  /■, vorauf  mp.  iis  weist;  IF.  9.  j6i.  —  ')  Un- thero.  —  j)  Wo  kariavahl.  —  4)  zBed.  s.  kariü-.
•  p.  "fcaräa-"  m.  Name  einer  Gewichts- einheit**: 2  "sä  T>-ig.
'I  Deren  Gewicht  Grav  JAOS.  30.  55  zu bestimmen  versucht.  Danach  wäre  1  ^  i^  1 76.7JD4 Gramm.
Vgl.  ai.  iar/a-  m.  —  ■)  Zum  ar  s.  Foy  ZDMG.
S-t-  357-  :
•  j.  karäay-  £  i)  'Furche,  Furchstrich':' yai  .  .  'saim  (AS-)'*  kärayeiti  Yt. 4. 1 4.  2)  'Pflügen'  (nur  AbleiL)
AbleiL  —  Zum  V.  iiars-.  —  ai.  i^-fäj"  f. •Pflügen'.  —  ')  Ganz  unsicher.
).  iarlavani  F.  5:  lies  iariaifii;  s.  •iarsa:
•  j,  kariä-  f.  'abgefurchter,  durch  Furch- ' striche  abgegrenzter  Raum':  äa^  tum..' avaMstSis  ava  ttisiarfm  (sd.)  °sayä  V.^.12.
Zun  V.  ikars-.  —  zBed.  vgl.  'iarSa-  2  und larh;:  —  Pü.;  M.
j  •  j.  karäö.räzah-  Adj.  (auch  fem.)  'der !  dem  Gau  die  gesetzlichen  Bestimmungen
Igibt,  Gesetze  vorschreibt':  mi^tTm  .  . 'zavAsm  tylxamm  Yt.  /o.  6 1 ;  —  *frazain-' tlm  °sqm  (ASf.)"'  vyäxanam  Y.  ^s.s,  F.5,
I  Pü. ;  kisvar  vitäi ,  Npü. :  iibanda  iakr.  — '  '*  S  3^1-  ^  <^d  Ausgang  des  folgenden 1      Worts.
•  j.  karäiptar-  m.  Name  eines  Vogels, I 'accipiter'*' ■':   kö  avalia  dainqm  mSzda-
' yasnim  vT.barat  altaShxi  varpf^a  yd  yitnö I  ksrsnaoti  .  .  vti  'ta  "Wer  hat  dort  , ,  ver- breitet? ..  Der  Vogel  K."  V.2.  42.
*)  Er  gilt  Bd.  24.  11  und  Vr.  /.  1  Pü.  als I  Ralav  der  Vögel ;  s,  yiala  fraftirijäl-.  Vgl.  auch jBd.  /p.  6,  Zs.  23.  4.
;  Komp.:  Harii'  (nur  KompA.,  aus  "V"*.  IF- p.  a6l|,  zu  lat,  currö,  mhd.  hurrt»  (SOLMSEN Stud.30)-|-*/''"^(»iis  '^E'  Ve)"'""'  derKomp- form  des  Nom.  ag.  zum  V.pit-,  S  34%  JSchmidt Plur.  174);  also  eig.  'Schnellflieger',  vgL  gr. sfusTfjj«»,  (öuiiirtriK  'pi;!  (»  87)  und  lat  acd- piltt  bei  JSchmidt  aO.  —  >]  Diese  Bedeutung folgt  ans  Bd.  34.  11:  karUj'l  ki  farj  (i  r  k) i^äitftitl;  vgl.  np.  i-'ur/ (ZDMG.  ViJ.  493);  ander» Zs.  33.  4.  -r-  Pü. :  transskr.;  dazu  die  Erl.i (iuM'öi  (wozu  IFAnz.  Z2.  24).
•  j.  karäi'vant-  Adj.  'Pflüger,  Ackerer': Im  zS  ,  .  yä  Jarrfa  akarsta  saita  yä  karsya 'vata  "die  Erde  . .,  die  lang  ungepflügt liegt,  die  zu  pflügen  ist  vom  Pfliiger" V.J.  24.
ai.  vgl.  kfja-alä-  ra.  'Ackerbauer',  —  Fü. : kisiinSmand.
•  j.  karäij-  £  i)  '.\ckerland':  Z3mS *'suya'''  "des  Ackerlands  der  Erde"(?)  F. 5.  s)  'Flur,  Landgebiet,  -bezirk,  Gau': *pouru.niaili  hanjamaine  *pouru.nairyA 'suya  "in  der  zahlreich  besuchten  Festver- sammlung des  männerreichen  Gaus"  Y. //.  2.
Zum  V.  Mfl'/-.  —  ai.  katfu-  f.  'Furche'.  — Vgl.  'karia-,  iariä-,  karhiar-  und  -  auch  zFIejt.  — Bthl.  IF.  p.  276.—  Pü.  {zu  1);  *//  rar'),  (zu 2):  karlär,  Sü.:  krtaiilryrfu.  —  ■)  K  20  ;  M  6 hat  'h'ii,  —  ')  Vgl.  np.  kisl  lär.
•  j.  "karäta-  Adj,,  PPfP.:  s.  'kars-. KompE.  -  np.  t.Ua.
•  j.  'karsta-  Adj.  'gemacht,  bewirkt,  ver- anlasst'.
KompE.  ■ —  Vgl.  unter  "karsH,  "karilu,  wofür Pü.  karr  hat,  und  •frakarila-,  das  Pü.  mit  dem selben  Verbum  wie  frakirmlal  usw.  übersetzt : /nif  ^i>/-fu/7i).  — Zum  Verhältnis  von  'karsla- (mit  ar.  /■,  IF.  g.  161)  lu  kirtla-  s.  unter ajtinuila-.  —  ')  Weshalb  man  CS  auch  faisch- lich  zum  V.  kar^l-  gezogen  hat;  so  zuletzt Ggr.  GlrPh.  Jh.  219,
dby  Google
=== BRT col marker near ===
45 5  karapan-  2  —  Ttars-  456
457
```


## [2026-09-14T00:54:34.145Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 92 (p.70) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==92' HRN.txt | head -50",
 "description": "Horn p.70"
}
```


### [2026-09-14T00:54:36.142Z] TOOL RESULT

```
=== HRN leaf 92 (p.70) ===
70 ~
phlv. ^patv(i)hltan , vergl. u^v(i)hTtan^ vd. 19 (16),
nv(i)himtan ^).
aw. *paitis + 1 [/'va^d-^ caeday^mi] ai. prati +
i/^ved'.
Np. h aus altem d zwischen Vokalen z. B. auch in
/'ähem aus ^svädämL Die gleiche Behandlung von d
und d (bei letzterem häufige Fälle des Übergangs in h)
zeigt, dass das d zwischen Vokalen im Persischen
ebenfalls spirantisch gesprochen wurde, daher auch
keine Scheidung im Altpersischen durch besondere
Buchstaben ; vergl. auch die allgemein durchgeführte
Spirans d bei AM., also im älteren Neupersisch, über
die Behandlung im Reim siehe Rückert, ZDM6. 8,
285, 286, 10, 263.
315. pes 'hinter, nachher, pesin 'letzter.
Käs. peCj pdc]es, pes.
ap. pasa, 'hinter', pasäva 'nachher ; aw. pasda 'nach',
paskät nachher, hinter , pasne 'hinter' ; phlv. paSj pasTn
'letzter ; ai. pagdd *hinter, nachher , pagcdt Von hinten,
hernach*.
kurd. püstve, pfisl; af/. LW. pas; oss. d. fastäge, t.
fästäg 'hinterer, nachher, zuletzt, am Ende' (280) ; bei.
pas^ Comp, pastara (287).
316. pest 'niedrig, nnoilN (Is. 2, 9; 11, 17).
ai. vergl. üpastiä, upastis 'Untergebener .
Bartholomae (briefliche Mitteilung).
LW. wa/. past, siyn. pist,
317. pistän 'Brust (der Frau)'.
a.w./stana' *Brust'; phlv. p(i)stan (vd. 9 (71)), pistän
(vd. 15 (26) 61.); ai. stdna-; arm. stin (H. No. 259).
LW. af/. pistän.
Vergl. Bartholomae, Indog. Forsch. I, 187 Anm. 2.
318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
1517 Vers 358 2), 1523 Vers 473).
*) So lese ich statt nvedlnltan.
*) An den beiden ersten SteUen vielleicht für puser zu emendireD,
doch kann bei puser wie bei pider die Izäfe fehlen, vergl. Landauer
zu S. 1517 Note 4.
```


## [2026-09-14T00:54:56.781Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB leaf 51 (p.41) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==51' HUB.txt | head -60",
 "description": "Hübschmann p.41"
}
```


### [2026-09-14T00:54:57.881Z] TOOL RESULT

```
=== HUB leaf 51 (p.41) ===
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


## [2026-09-14T00:54:58.670Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page 1[0-9][0-9]\\]\" BQT_v1_pages.txt | sed -n '1,5p'\necho \"---- search oftadan افتادن in BQT v1 ----\"\ngrep -n \"افتادن\" BQT_v1_pages.txt | head -10",
 "description": "Find BQT v1 page 145"
}
```


### [2026-09-14T00:54:58.766Z] TOOL RESULT

```
---- search oftadan افتادن in BQT v1 ----
951:۷۵ ( کشیدن)-۵۳ (افتادن) [قس: کمن ۱20اع (قدیم)؛ درمتون
11257:از حر افتادن - کنابه از مردن
11268:خر افتادن است که مردن و از عالم رفتن باشد .
11313:ارشکم افتادن - کنابه از مردن
12722:که لفزیدن دبسردرآمدن وافتادن‌باشد , چها کر
13879:و افتادن دبوار و امثال الرا نیز گویندب ویمعنی
17446:بیوست کسی افتادن - کنابه از
17881:بخیه برروی‌کار افتادن کنابه
30099:رشت از بام افتادن کنانه از
```


## [2026-09-14T00:55:03.869Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB leaf 52 (p.41) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==52' HUB.txt | head -60",
 "description": "Hübschmann p.41 correct leaf"
}
```


### [2026-09-14T00:55:04.956Z] TOOL RESULT

```
=== HUB leaf 52 (p.41) ===
— 41 —
Die Sanskritubersetzung giebt das paz. Wort durch
pagdnttdpin- Veuig* wieder. Es wird irgendwie zu zd.
pasda nachher und Wrzl. man *denken* gehOren und
urspriinglich *nachher-bedenkend* bedeutet haben.
313. Die von Noldeke und Horn erwahnte Form gu^s-
murdan des Judenpersischen zeigt, dass piSmurdan
'verwelken iiber alteres bizmurdan (Noldeke, ZDMG.
45, 106) auf *vizmurdan zuriickgeht. Damit fallt
Horn's Etymologic, insbesondere piz- aus patis.
314. Der Paragraph ist vollkommen verfehlt und zu streichen.
Vgl. Fr. Miiller, WZKM. 7, 371, dessen positive
Ausfiihrungen {piidh-tdan = pati + s + Wzl. von
np. justan, vgl. phi. vijustan WZKM. 8, 92) freilich
auch nicht einwandfrei sind. Ich lehne also np. piz-
aus patis (wie oben bis- aus abis) ab. Ich finde patis
auch nicht in np. paSkam^ {piskam^ baskam, biSkam)
*domu8 aestiva, aula, atrium, coenaculum, porticus =
arm. patSkam (patsgam^ patsgamb, patskamb) *Gemach,
Halle, Stockwerk*, sondern fiihre np. paSkam = arm.
patskamb auf ap. *pati-skamba~^ das ich zu zd. fra-
skemba- vd. 2, 26 ('Stiitzmauer Geldner, 'batiment
avec balcon* Darmesteter) stelle, zuriick. Im mittel-
persischen wurde *patskamb zu *paskamb, ehe pat-
(vor andern Consonanten als s, s, d) zu pai- wurde.
316. Np. past niedrig, gering' ist nicht = skr. upasti-,
das zu *bast geworden ware, sondem = *patta-y skr.
patita-, Vgl. oben Nr. 92.
317. Etym. dunkel, auch nach Fr. M tiller's Erklarung,
WZKM. 6, 184 (pistdn = pEstan Gl. and. Ind. 113 =
*payastdna', das zu zd. fStana- nicht stimmt).
318. 7m pus vgl. Spiegel, WZKM. I, 250.
219. Np. pasa/nd *angenehm, gefallig, gebilligt, will-
kommen', paz. pasandfdan *to approve* Skh. 263 ist mit
Spiegel aus *pat-sand zu erklaren. Vgl. skr. chad,
Shand gefallen', Shanda- gefallig*, zd. sad^ ap. ^ad.
') Fehlt bei H r n.
```


## [2026-09-14T00:55:05.554Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" BQT_v1_pages.txt | head -5\necho ...\ngrep -c \"\\[pdf page\" BQT_v1_pages.txt\necho \"=== v1 around printed 145 ===\"\ngrep -n \"\\[pdf page 1[5-9][0-9]\\]\" BQT_v1_pages.txt | head -20",
 "description": "BQT v1 page tags"
}
```


### [2026-09-14T00:55:05.667Z] TOOL RESULT

```
...
0
=== v1 around printed 145 ===
```


## [2026-09-14T00:55:18.699Z] TOOL CALL #20: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py",
 "description": "Read ref_page tool header"
}
```


### [2026-09-14T00:55:18.744Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

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
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-14T00:55:20.426Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v1 head ===\"; head -30 BQT_v1_pages.txt\necho \"=== formfeeds v1 ===\"; python3 -c \"\ns=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint(s.count('\\f'))\n\"",
 "description": "Inspect BQT v1 pages file"
}
```


### [2026-09-14T00:55:21.631Z] TOOL RESULT

```
=== v1 head ===
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م۸
و «ارس‌شبات
4
د انشمند محتر م آقای‌د کترمحمد معین‌استاد دانشگاه تهران
فوپانت تاموی ۲۰/۹/۳ ها رتیفارد *
=== formfeeds v1 ===
776
```


## [2026-09-14T00:55:25.837Z] TOOL CALL #22: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:145 --image 2>&1 | head -60",
 "description": "Fetch BQT page 145"
}
```


### [2026-09-14T00:55:26.978Z] TOOL RESULT

```
no scan of BQT covers printed page 145 (see 'scans' in refs_online.json)
```


## [2026-09-14T00:55:35.476Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ns=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef num(t):\n    return t.translate(str.maketrans(fa,'0123456789'))\nfor i,p in enumerate(pages[:40]):\n    head=p.strip().split('\\n')\n    if head:\n        print(i, repr(num(head[0]))[:60], '||', repr(num(head[-1]))[:60])\nEOF",
 "description": "Inspect BQT v1 page boundaries"
}
```


### [2026-09-14T00:55:36.580Z] TOOL RESULT

```
0 '' || ''
1 '1 5 1! 1' || 'بسرمایه کنابفروشی ابن سینا - تپر ان'
2 'اداره کل دک زون.' || 'یی سین'
3 'شیر زوا عرسا رده ارسال 1317 0331« 9 لو امد 0' || 'ف'
4 '.ای وود دی ( ینمی 13 ارو 9 یت' || 'ردو'
5 'وش 1 اد 1 ل «وضیات .نا رالافاضل ,رات بان -' || 'و + مدا اسان ست 2'
6 'بر رم دور چا ,هلر ون 4 رصن' || 'چار'
7 '1' || 'خ مسیمت مصت \u200f سسسسست خن بت پوت وت بت سس'
8 'صفحه 7' || 'ید33 ویص تس'
9 'دما ساب ان' || 'وشوش ( درعیلام ) وبنستان ( - بیستون ) وهمدان والوند ( در ما
10 'مقد مه دو' || 'کوتاه است ( درسه سنگیعته ) از کورش دردشت مراب ( درنارس ) که
11 'سه ژبا نبای\u200cایرانی' || 'ما که درطی\u200cچندین هز ارسال درهمین\u200cسرزمین درسر زبان
12 'مقدمة 1 چپار' || 'تألیف ی : ِ'
13 'نج ژبانپای\u200cایرانی' || 'هخامنشی و سنگنبشتهای آخرین آنان تفاوئی هو جود است .'
14 'دقد 4 3' || 'است 0 مثلا در مأخذ قدمی دبار خودمان ریشه وین لنت هنجار بچای
15 'درلپجه سانسکریت که حرف « ها »> به < تن مات اک نیا' || 'بازخو انده شده » زبان پپلوی هم بمرز و بوم پارت ( خراسان)باز
16 'ههد عه هت' || 'درن\u200cام شپریاری چپارصد بان فراهم 7'
17 '0 زبانپای\u200cایرانی' || 'این نام میرسا ند کا تکارش تفسعر اوستا تازمان مزدك بسر بامدا
18 'مود م4 ده' || 'امیدوار بود که باز در تك\u200cربگ\u200cوخاك نوشتهای پپلوی پ
19 'یازده زبانبای\u200cایرانی' || 'تور1< کاو وغیره .'
20 'مقك مه دوازده' || 'يعنی بجایآن ایدئو گر امپای [رامی خود کلمات ایرانی معادل [ ن
21 'سیزده زبانهایایرانی' || '. 0 252258 . 648 زطد5 «هن« 135'
22 'م . معین' || '. 223-4 .0 ,69358'
23 'با نزده زبانپای\u200cایرانی' || '1-رك:بالیز (متن وحاشیه). 2- ازلپجةٌ وخی مد یاد خواهیم کرد .
24 'مقدیه شانزده' || 'جح 4 ش 0.3 (مقدمة بر های قاطع ]])'
25 'هقد م زبانبای ایرانی' || 'ق.م) بسفد, رژگ: دائرةا لمعاریاسلام: صقد. بقلم بارتولد.'
26 '0 عمقدمه هد ه' || '+ -هنینک. کتیبه\u200cهای پهلوی ترجمةٌ نگارنده\u200cس؟1 . 7-
27 'نوزده زبانهای ایرانی' || 'اسفتدماه 1325 .'
28 'من» 0 -< (مال) من مبر 2 902 مر دن» تو"7) < نو زیر 2772 < زر || '0 6 1 30 .5980 063500 ع4 نحعع , 04نحااناهت) -ع'
29 'یست و يك زبانبای ایرانی' || '7018.'
30 '035525 18 تاه ه115)6 ر ](ا)ارل13 . 8' || 'خو ار دمی'
31 'پیست و ضه زیانبای ایرانی' || 'توت ود مهد'
32 'مقدمه بت و چپار' || 'با میکنيم : بقیه در صفحهٌ 25'
33 'یست وینج زبانهای ایرانی' || '0 8 , 1936 271286 210 62 #اطمعاعع3 عجمك , 5255555 - 11500 ب
34 'مقدمه سست ورشش' || '1- برگیلکی ههامه] ( اتادن).'
35 'بیست وهفت زبانهای ایرانی' || 'زبان دری پش\u200cاز اسلام - اکرهم آثار مکنوب وجود داشته+ چی
36 'مقد مه سست وهشت' || '8 - ناریخ سیتان ص37 .'
37 'بیست و نه زبانبای ایرانی' || '7- درمتن : کلام\u200cالفری 4 و5 : پهله درعتن .'
38 'مقدمه : کی' || 'است\u200cاین موضوع\u200cمورد توجه دقیق مستفان ابرانی وارویا
39 'سی ويك زبا نبای\u200cایراتن' || '8- نام شیروبه . 4- شاهنامة بخ ج8 ص 2577 .'
```


## [2026-09-14T00:55:43.426Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ns=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\ntr=str.maketrans(fa,'0123456789')\nfor i,p in enumerate(pages):\n    t=p.translate(tr)\n    lines=[l.strip() for l in t.strip().split('\\n') if l.strip()]\n    if not lines: continue\n    cand=(lines[0]+' '+lines[-1])\n    m=re.findall(r'\\b(1[3-6][0-9])\\b',cand)\n    if m and 100<i<400:\n        print(i, m, lines[0][:50],'||',lines[-1][:50])\nEOF",
 "description": "Find printed page numbers in BQT v1"
}
```


### [2026-09-14T00:55:44.761Z] TOOL RESULT

```
262 ['131', '130'] آقای 1 هت || شمارژ ٩7ص‏ 131-130 .
338 ['139'] یعتی باز داشت و منم دفتن کرد . || بحا کم استان (درعهد ساسایان) اطلاق مشد. «کرستسن. م
353 ['138'] وا || یه درسفحةٌ 138
```


## [2026-09-14T00:55:57.907Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ftat\\|ftad\\|opast\\|apat\\|pat-\" BQT_v1_pages.txt | head -20\necho \"=== اوفتادن ===\"; grep -n \"اوفتاد\" BQT_v1_pages.txt | head\necho \"=== page index locate: find 'آبادان' or first entries ===\"\npython3 - <<'EOF'\ns=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nfor i,p in enumerate(pages):\n    if 'باب الالف' in p or 'حرف الف' in p:\n        print(i, p.strip()[:120].replace('\\n',' / '))\nEOF",
 "description": "Locate alef section in BQT v1"
}
```


### [2026-09-14T00:55:59.062Z] TOOL RESULT

```
=== اوفتادن ===
=== page index locate: find 'آبادان' or first entries ===
```


## [2026-09-14T00:56:02.784Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nr=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(r['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "BQT ref record"
}
```


### [2026-09-14T00:56:03.757Z] TOOL RESULT

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
```


## [2026-09-14T00:56:10.743Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ns=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nfor i in range(352,368):\n    t=pages[i].strip().replace('\\n',' | ')\n    print('--- leaf',i,'---')\n    print(t[:400])\nEOF",
 "description": "Print BQT v1 leaves 352-367"
}
```


### [2026-09-14T00:56:11.834Z] TOOL RESULT

```
--- leaf 352 ---
باشد ٩‏ - و بلفت زند و پازند (۱) بمعنی مینه | است که جربی صدر خوانند ۴ . | اسیر لگ - بارای فرشت بروز نکنيزك . | یار خریزه را کوش . | اسیز ۵ ]یه بنتح اول ورابع وسکون | عیم» داروی چندی است که اطبا درآب جوشانند | و بدن بیمار را بدان شویند و آنرا بعربی نطول | قبل‌ازین مذ کود شدتصحرف خوانی شده واشاعلم. | اسیو س ؟ « بح اول و سکون ثانی | نمك چینی را کوبند که شوره باشد و باروت‌را | از آن سازند و درهندوستا
--- leaf 353 ---
وا | اول هم آمده است ٩‏ . | اشتاب ۴ - جن‌اول وسکون بایابید. | بمعنی ثتاب و تعجیل باشد » و بکر اول حم | آمده است » و بجای حرف آخر واو هم کفته‌اند | که اشتاو باشد . | اشتا ؟ - بفتح اول بروزن هشتاد. نام | روز بیست و ششم است از هرماه شمسی - و نام | فرشته ات که موکل است بی دوژ آشتاد | و امور و مصالحی که در آن روز واقم میشود | تعلق باو دارد ؛ و تيك است دراین روز حاجت | خواسشن و جامه یوتبدن و صدفه دادت -
--- leaf 354 ---
اشتر گیا - بکر کاف فارسی و تحتانی | بالف کشیده , بممتی اشتر خار است که خار | شتری باشد ۰ و بسضنی کوبند کیاهی است‌دوابی | که آنرا سلخه خوانند . | اش شتر هرع - پرنده است که بای او | شراست وسنکه | و آش خورد و بایابپای | خود سثگه بر هر چیز | که خواهد زند و خطا | نکند و عربان اورا نعامه | کونند . اشتر مرغ | اشثر هووو « کویند جانورست مانند | یا و یه | ببزرکی بز کوهی میباشد و در جنگلهای حفرب | بمیار است 
--- leaf 355 ---
و سکن الی و دال ابجد , نام روزدوم است از | خمسا مترفةٌ فدیم- وبودن آفتاب دربرجعفرب | ودرین روز عفان بمنی آتش پرستان جش نکنند | و بمعنی اول بجای فوفانی نون عم آمده است . | اشتیم - بح اول بروزن تسلیم » چرله | وریمی را گوبند که در جراحت باشد ۱ . | اشتاد - بح اول و خای نقطه دار | بالف کشیده » قلیا را کوبند که زاح سیاه‌است | و رنگ رزان بکار برند - ونوشادر را لیز گوند | و آن مك مائدی امت که استادان حض گ
--- leaf 356 ---
اخك تلح ه جفتح فوقالی » کنایه از | شراب الکوری باشد - و اثك چشم را نیز | کواند . | باشد . ۷ | اشگر ف « بنتح اول وکاف فارسی بر | وزن خلجرف , نیکو وخوش آبنده را گود - | و پکس اول بمسئی مطبر و قوی :و گنده | وبز رکه باشد - وبمعنی‌شأن وش وکت وحشمت‌هم | آمده است_. | اشگر ه۱ « بکر اود و کاف وفتح | رای قرشت , مرغان شکاری دا کویند مطلقا | و ضی گوشد مرخی است شکاری از جنس | بلشه لیکن از باشه کوچکتر بود و آدر
--- leaf 357 ---
_ٍِِ | اشکو خیدن . مصدر اشکوخ است | که لفزیدن دبسردرآمدن وافتادن‌باشد , چها کر | کی را پایش از یش بدد رود و یفئد گویند | اشکوخیه . | اشکو 4 ه بن اول , بسنی شکوفه | و بهار درخت باشد - و فی و استفراغ را لبز | گویشد ۱. | اشکوه « بنم اول والث وسکون تانی | و واو و ها ء بمعنی شآن و شوکت و شکوه | وعنلمت باشد ۴ . | اشکیل؟ بکراول وثاكك وسکون‌الی | وئحتانی ولام » بمعنی اک ات وان اسبی‌بود | که دست راست وپایچ
--- leaf 358 ---
اشو ی | که کمانگران بر باژوی از جابدر رفته ‏ بندند | واشق معربآشت . | اشتاف مامثا بنتح اول و کسرفاه | یعنی عصاره مامثا ومامیئا بلغت سربانی‌نام رستنی | باشد که آنر! درفااضات بکاربرند وآنرا زهبانالی | که درئواحی موصل میباشند سازند . درد چشم | و ناقم افننت. ‏ | اشیهه - بفتح اول وکسر‌انی بتحانی. | رسیده و های مقتوح » آواز هو شيهه اسب را | قز بر 9 | هم حست خوشبوی که آنرا دواله میگوینه | وبعربی شبیه‌الس
--- leaf 359 ---
۳و | معتی امتضر است که قلمةٌ فاری باشد و آن | که داراین داراب‌استت هاگن وتالابرا لس | گویند . | اصطر خ" س بروزن ومعنی استخراست | که فلمة فارس ناشدب وتالابو آبگررا نز گووند. | سمفی است سرخ بسیاهی حابل و بسنی گویند | صمغ درخت زیتون است . نزله را نافم است . | اصطر لاب - ممروف است و آن | آلتی باشد ازیرنج وتال ساخته که منجمان‌بدان | ارتفاع آفتاب و کواکب معلوم کنند و این لفت | بونالی است بمعنی نرازوی آف
--- leaf 360 ---
وشطهای سیله دارد . ۱ نوعی ازبوی مادران باتد . گویند کترانیدن‌آن | اطموط ‏ بنتم اول بر وزن مضوط , | درخانه گزندکان موذی را بکربزاند وآنرابعربی | بمعنی اطماط است که بندق حندی باشد  .‏ ۰ | قیصوم خوانند . | اطمسا ه بفتح ال و ثالت بتحتانی ابو ط ‏ پابای حطیء بروزن و معنی | رسیده وسین بی‌نقطه بالف کشیده . بلغت بودابی | اطموط است که بندق خندی باشد . | درهمزه باغین نقطه دار مشتمل برهیجده لغت | سعقص ساکن, ب
--- leaf 361 ---
فیاصر# روم ؛ او را ازآن جپت قصر گفتندکه | مادرش بوفت ولادت عمرد 7 شکمش را بشکافتند | و او را برآوردند و پزبان رومی اینچنین شخصی | را قیسرخوانند٩‏ . و گویند عیسی علیه‌السلام در | زمان او بوجود آمد . وبقوط سین اول بروزن | فربوی هم بنظر امده است - | اغشته با اول وئانی مفتوح و سکون | شین فرشت وفتح فوقانی ‏ بمعنیآمیخته وآلوده | وتر کرده باشد؟ . | لام ؛ جایی‌باشد که در کوه وسحرا بجهت‌خوابیدن | کومفندان 
--- leaf 362 ---
اتمون | حمف خدایتمالی هم هست! - | / لتیهاون » بعتح‌اول. دوابی‌است‌ممروف | وآن شَكوفةٌ نبانی باشد که بسعتر می‌ماند و سر | شاخپای آن بارمك است ۰ وطبع آن کرموخشاثه | کوفت صرع را نافع است ۰ و آنرا بعربی سبع | الثمرا خوانئد , وی کوبند زیر رومی است | وتیزطعم میباشد . | اقچ4 - بن اول بروزن بقچه , علامتی | است که در غله زار ها و کشت و زراعت بجهت | رمیدن مرغان ساژند . وبفتح اولعم گفته‌اند . | اقد فتح ارل و
--- leaf 363 ---
افر اشتن بروزن ومعنی‌برداشتن: بلند | ساختن باشد . | افر اشته بروزث ومعنی برداشته‌و بطند | ماخته و بالارده )۱( باشد ۰ | ۱ فر دون - بفتح اول رانی‌وسکون‌نالث | و کربای ابجد وبای حطی بواو رسیده و بنون | زده , دوایی اس تکه آنرا قرفیون کوبند . ا کر | کزند کی جانوران را نانع است . | که آنرا بشیرازی بالنگوی خوورو (۲گوبند . | ء اس را نافع است ۳ | نام شهرست که نوشیروان آ ادکرده بود در کتار | دربای مصی » و م
--- leaf 364 ---
آفری | کشوث و نخم آنرا بذرالکشوث خوانند . فواق | را تافع است . | افری فتح اول وثانی بروزن سفری » | مخفف آفرین است که دد مقام تصی نگوند . | و بسکون انی هم درست است . | افر یدون ‏ - فربدونباشد. واویادشاهی | بوده. ءشهوره ویستی گویند افربدون نوح علیه ب | اللام است ۰ و بعضی ذوالقرنین اعظم او را | صسدانند ۰ | اقفر پسموسش_ » بسکون سی‌بی نفطه | وم حیموواو وسین دیکرساکن, پیونانی؟ مرضی | است که مردانرا بهم 
--- leaf 365 ---
ات | وافرا یمرن الیل خوالند . | اسر ۵لن؟ « بر وزن افشردن » بمعنی | سردشدن ویخ بستن ومنجمد کردیدن باشد - واز | چیزی ‏ وکسی‌دل سرد شدن هم هست - | آقتاب عالمتاب است . | افسرسگزی « بکس مین بی شله | و سکون کاف فارسی و زای نقطه دار بتحتانی | رسیده ۰ نام سازی باشد که نوازند - ونام تصنیفی | وقولی است ازصنیفات بارید . | افسر شدن » کنابه از پادشاء خدن | باشك . | افستتین ۴ - | بکسر الث و سکون | نون و فوقانی 
--- leaf 366 ---
بدان غلهٌ کوفته شده را برباد دهند تاکاه از آن | 9 | اقشه - بروزن کفچه, بمعنی باغورباشد | وآن ظه‌ایست که درآسیا خرد کنند و بشکنند | افغات» باین | نقطه‌دار بروزن‌سنان , | بممنی‌فرباد وزاری باشد- | ونام فسلهاست مشهور | چنانکه آرد نشود . | افشین ۱ ‌‌ مروزن کم 0 نام شخصی بوده | افی زد دفام - کنابه از قلمواسطی | ومعروف وجمعش‌آفاغنه | است بر وزن فراعته ؛ | بطرینی جمع عسربی - | وهمچنین هیتالرا نیز اعلیحضر
--- leaf 367 ---
افگنده(۱)سم کنابه ازعجز وزاری | بسیارباشد . | ومعرب افلاطون‌است . راو حکیمی بوده مشهور | و معروف در زمان کف واستاد ارسطو است» | وساز ارغنون مخترع اوست . | افالا گبان- بک رکف . کنامه ازئوابت | و سیارات است - وطایفه ای باششد از می دینان | ویدمذهبان . | افندبدن بت ور وزن ستدیدن ِ جنگ | وخصوحت کردن باشد ب | افیلون « بالام بروزن‌شبیخون » درمنة | کوهی را کوبند . | کرخاکشر آنرا باروغن‌بادام | پرموضم ریش
```


## [2026-09-14T00:56:23.067Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ns=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nfor i in (361,362):\n    print('=== leaf',i,'===')\n    print(pages[i])\nEOF",
 "description": "Print BQT v1 leaves 361-362 fully"
}
```


### [2026-09-14T00:56:24.413Z] TOOL RESULT

```
=== leaf 361 ===
فیاصر# روم ؛ او را ازآن جپت قصر گفتندکه
مادرش بوفت ولادت عمرد 7 شکمش را بشکافتند
و او را برآوردند و پزبان رومی اینچنین شخصی
را قیسرخوانند٩‏ . و گویند عیسی علیه‌السلام در
زمان او بوجود آمد . وبقوط سین اول بروزن
فربوی هم بنظر امده است -
اغشته با اول وئانی مفتوح و سکون
شین فرشت وفتح فوقانی ‏ بمعنیآمیخته وآلوده
وتر کرده باشد؟ .
لام ؛ جایی‌باشد که در کوه وسحرا بجهت‌خوابیدن
کومفندان ساژند؟ .
اغلیسون » با سن بی قطه بر وزن
افربدون ۰ قوس قرح را خوانند .
افتدستا
اغلیقی ‌ َنح اول,قلف سحتا سدكهه
بلفت بونانی؟ ترکیبی است کهآ نرا بغارسی پخته
جوشانیده‌اند ومیفختج همان است » وبکسر اول
نیز آعده شتگن «
اغول ه بر وزن ملول » از روی خشم
وفهر بگوث؛ چشم نگریستن باشد .
اغیرس < بنتح اولوثانی‌بتحتانی رسیده
و کسر رای قرشت و سکون سین سعفص ؛ جوز
رومی است و آن بار درختی باشد که صمغ آن
کهرباست ؛ و بعضی گویند چوب آن درخت
کهرباست .
اغیسی ‏ بروزن نفیس , نخمی اس ت که
آنرا بشیرازی تخم دلاشوب کونند » و ری
افتاد جنم اول بروزن استاد ۰ بعنی از
بای درآمد - و کنابه از دور شد هم هست که
ماضی دورشدن است .
افتاث گان » کاب از مظلومان
ویر بشان شدکان‌باشد .3۶
افتاده ممعثی عاجز و سقط وخراب
که و ژبرن گردننه باخد..
اقتال ‏ یک راون بروزن اقبال . به‌عنی
برا گنده وباشیده - وشکاقه ودریده باشد .
افتا ليفن « بکراول مصدر افتالاست
که بمعنی پراکندن و یائیدن و افشاندن -
وشکافتن ودربدن باشد .
افتان و خیز ان - کنابه از آحته
ودیر براه رفن باشد .
افقد - بنتم اود و کسر الث مر وژن
محجد ؛ و بمعنی ستاننده و متایش. کنده. باق ت
وبععنی شگفت وعجب ونعجب هم‌هسته .
افتدستا - کلمه ابیت مرکب از افتد
ستایش‌عجب وئیکوترین ستاش‌وبند گی- ویمعنی
2 ۱ متفه
۴ - بوتانیلا ان «اشتینگای».
=== leaf 362 ===
اتمون
حمف خدایتمالی هم هست! -
/ لتیهاون » بعتح‌اول. دوابی‌است‌ممروف
وآن شَكوفةٌ نبانی باشد که بسعتر می‌ماند و سر
شاخپای آن بارمك است ۰ وطبع آن کرموخشاثه
کوفت صرع را نافع است ۰ و آنرا بعربی سبع
الثمرا خوانئد , وی کوبند زیر رومی است
وتیزطعم میباشد .
اقچ4 - بن اول بروزن بقچه , علامتی
است که در غله زار ها و کشت و زراعت بجهت
رمیدن مرغان ساژند . وبفتح اولعم گفته‌اند .
اقد فتح ارل و رای وسکون دال
ابچد » بممنی افتد است که شگفت
روا ماه تور گر ۳
وآن سورخ و:
و عجب
افدد » بر وزن صقذر ؛ برادر در را
وخواهرزاده تبزامده ات ۰
اقدستا » با تای قرخت بروزن‌مجلهاء
جمعتی افتدستاست که ستایش عجب و نبکو نرین
متایش - و حمد خدای عز وجل باشد بزبابن
پهلوی ۴‏
اقد‌یدن » بروزن فهمیدن . شگفتی
کردن وتعجب نمودن باشد ۴ .
اقر) - بر وزن صفرا ۰ بمعنی آفرین
ونحسین پاشه .
ار احت ‏ بر وزن پرداخت » یعنی
برداشت وبلند ساخت .
. رک : اد وافدستا‎ ٩
ب 30۸
اقفر اختن - بر وزن برداختن 4 بمعنی
برداشتن وبلشد ساختن باشد .
افر احته بر وزن برداخته ». نی
برداشته وبلند گردانیده .
/ فر ازه بر وزن برواز, بمعنی‌بلندی
وبلند باشد - وامربدین معنی هم‌هست بعنی‌بردار
وبلند ساز - واسم فاعل هم آمده ات که بلنف
کننده باشد - و عنبر خطیبان را هم گویند -
ویمعنی جمم‌باشد که در مفابل فرد است - ویسته
و کشاده وبین شده را نیز گومند - ویمعنی‌قریب
وترديك وپیش باشد - وغشیب را هم کنته‌اند که
درمقابل فراز است - وبمعنی آزین باز و بعد از
این هم هست - و سر کش و سر کشیده را نیز
«ک تفت وا بینی آت تتال هم آمده است .
افر از بدن بمعئی ‏ بلند ساختن
و افراختن باشد - وبمعنی آراستن و زب دادن
وخوش کردن هم مده است .
افر اس س پروزن کربای . خیمه‌وفناث
را گویند ۰
بمعنی سواران آپ است که حباب باشد .
اقر اسیاب۱ - نم پادشاه تر کتان
است - و کناده ازهموار براه رونده هم‌هست جه
آب پمعنی راء رو هموار است .
افراشت بروزن برداشت , بعنی بلند
ساخت وبالا برد .
جز ازایز و تواع خداو ندی
```


## [2026-09-14T00:56:36.054Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,os\npm=json.load(open('data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json'))\nprint(pm.get('map',{}).get('1659'), pm.get('map',{}).get('1658'),pm.get('map',{}).get('1660'))\nEOF",
 "description": "BQT v3 pagemap for 1659"
}
```


### [2026-09-14T00:56:37.277Z] TOOL RESULT

```
452 451 453
```


## [2026-09-14T00:56:40.929Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nfor f in ['BQT_v3_pages.txt','BQT_v3_pages_faseng.txt']:\n    s=open(f,encoding='utf-8',errors='replace').read()\n    blocks=s.split('\\f')\n    for b in blocks:\n        m=re.search(r'\\[pdf page (\\d+)\\]',b)\n        if m and m.group(1)=='452':\n            print('###',f)\n            print(b[:3000])\n            break\nEOF",
 "description": "Print BQT v3 pdf page 452 (printed 1659)"
}
```


### [2026-09-14T00:56:42.167Z] TOOL RESULT

```
Exit code 1
### BQT_v3_pages.txt
[pdf page 452]
acs 4

ومحنت و تنگی - و افشرد نکلورااگونند ‎٩‏ - کلف ‎A bay‏ - بممنی ید بیناس تکه
ودرعربی بمعنی بر روی درافکندن‌ویر گردانیین | ممجزة موسی علیهالسلام,بود . گویند ه رگاه
جامه باشد - و بکر اول لیز در فارسی بمعنی | میخواست ظاهر سازد دمتها را از بغل برمپآورد
رنج و محنت وسختی باشد ۴ - و درعربی‌بمعتی | نوری از دستهای او ‎ates lag‏ که تا بآسمان
جزا دادن - و مانند یکدیگرشدن - و توالایی میرفت +
ودامن خیمه باشد ۴ .

کف ] بگینه » بکر ‎gt‏ .آبی‌باشد
که مانند کف بر روی آبکینه پیدا شودبهنگام
کداختن ؛ و بعضی گویند ریم آبگینه است .
سفیدی ‎pte‏ را زایل کند و آترابس‌بی‌زبدالقوارس
وماءالزجاج خوانند وبیونانیمسحوقو نباوس حقونیا
کفاند ۴ © بروزن رساند؛یعنی بشکافد
و بترکاند , وشق کند بدرازی .*#

کگفاثه * = بر وزن ‎sale‏ بچه ای را
کوبند که نارس از شکم مادر پیفند .

کفانیدن ‎٩‏ = پروزن رسانیدن»بمعنی
شکافتن وترکالیدن بدرازی باشد ۷ .

فت ‏ بنتح اول بروزن رفت » ماضی
کفانیدن است ‎٩‏ یعنی شکافت و ترکایید وبمعنی
ت رکید و شکافته شد هم درست است - و ‎pe‏
‏اول مخفف شکفت باشد که از شکفتن وواتدن
است - و مخفف کوفت هم هست که از کوفتن
‎ach‏ - وبکر اول بممتی دوش وسردوش‌است*۱
و بعربی ‎GT‏ خوانند #۰

کفتر ".- بروزن دفتر » کبوتررا گوبند
و بعریی حمام خواتند .

‎CRT‏ بر وزن دفتری » شانه‌ردفتین
‎MAY >‏ و بافندگان باشد .

‎a wr‏ ختح اول بروزن هفتگی»

‎. ‏جهانگیری © رشیدی‎ : Ay ٩

‎Soule - ۴‏ در اول شرح این لفت گفته است . ۴ رك : اقرب‌الموارد +
منتپی‌الارب . ۴ - نوم شخص مفرد متارع از «کفاندن » ودکفالیدن © ‎Com)‏

‏۵ مقلوب و مصحف « فگانه » ‎V Cpa)‏ = کفالدن, متعدی کفتن = کافتن.
۴ - هیبتش الماس سخت را بکفاند چون بکفاند در چشم مار زمرد .
« منوچهری دامفانیس۱۷*.
۸ -(عی) کف ( بتشدید دوم ) بیضام. ‎٩‏ - ماضی «کفتن » است [ماض ی کفالیدن
«کفانید » است ).
*- مقلوب« کتف » : بیاوردکر زکران را بکفت سپه ماند از کار او در شگفت .
فردوسی طوسی « رشیدی * .
‎YY‏ رك :کبوتر . ۴ از : کفته )= کافته) ‏ کفتگ دی (حاسل مسدر) .
‎eth - oT ۵‏ اول ودوم وپنجم .کفایدن ‎Coa).‏
‏۵ کفتار - بفتح اول کردی ع ‎keftar‏ راب۳۳۹ >
‎kaftér or‏ ؛ نجانوری است از کوثتخواران , که از لحاظ
وضع دندان شبیه بکربه , ولی از لحاظ وضم چنگال مانند
سگه‌است , ازایشرو ‎LT‏ حد وسط دوخانواد مذ کورمیدانند .
‎we‏ ازجالوران مرده و نیم خوردة گوشتخواران دیگر تغذبه میکند .


Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'BQT_v3_pages_faseng.txt'
```


## [2026-09-14T00:56:57.244Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\ns=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=s.split('\\f')\nfor b in blocks:\n    m=re.search(r'\\[pdf page (\\d+)\\]',b)\n    if 'کشک' in b:\n        print('pdf',m.group(1) if m else '?', '|', [l for l in b.split('\\n') if 'کشک' in l][:6])\nEOF",
 "description": "Find کشک in BQT v3"
}
```


### [2026-09-14T00:56:58.343Z] TOOL RESULT

```
pdf 88 | ['\u200epa cod \u200fکشکینت روا\u200e ob']
pdf 138 | ['کشکول تا مگر بسرش باژ کون کنشد.']
pdf 382 | ['\u200f«کشکنجیر» (هم.)']
pdf 389 | ['کشکی ۴ = بروزن مخزن , جام\u200cجوی\u200cرا']
pdf 393 | ['\u200f۴ رك : جهانگیری . ۴ رل : کشکول . © -کردی \u200ekecel\u200f « ژابا']
pdf 396 | ['کشک', '۸ از پی مصلحت برو خندد کشکضی بر بروت او بندد .']
pdf 445 | ['کشکاب ۴ » بر وزن میتاب : آش\u200cجو', 'کشکاب است که آش جو باشد .', 'کشکبا 1 ه بفتح اول و سکون \u200egt\u200f', 'کشکر لك ۷ - بارای قرشت \u200eOs»\u200f', 'کشکشان.', 'کشکله م بر وزن مشفله ؛ نوعی از']
pdf 446 | ['\u200eGES = FO\u200f نفد کشکینه', '\u200fکشکو ؟ - بر وزن بدرو ۵ \u200ewie\u200f', '\u200fکشکول = بروزن مقبول » بسنی کدا', 'باشد یعنیشخصی که کدایی کند - وکاسة کشکول', '\u200fکشکهای پر توه = بفتح اولوثانی»', '\u200fکشکهی \u200e٩\u200f » بر وزن بروین » بمنی']
pdf 447 | ['\u200e. \u200fپوند سبت ) . رك : کشکنه » کشکین\u200e ( ee PES: GY', 'کشکنه است که بان جو وفیره باشد .']
pdf 483 | ['دارند - \u200eLy\u200f چویین وکشکول کدایان را هم']
pdf 496 | ['\u200fتقطه\u200cدار . دوغ خشك شده راکوبند که کشکه\u200e']
pdf 528 | ['\u200fدویم ؛ بمعنی کشکنجیر است که سنگه منجنیق', '۰ معرب آن « جوسق \u200f « ابن درید *. ۷ رگ : کشکنجیر .']
pdf 542 | ['\u200f1 - برستوران و اقربات مدام کاه کهتاب باد و ج و کشکاب.']
pdf 689 | ['\u200eth »\u200f تفطه\u200cداربروزن کشکك.']
```


## [2026-09-14T00:57:07.577Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,re\npm=json.load(open('data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json'))['map']\nrev={v:k for k,v in pm.items()}\nfor p in (444,445,446,447,452):\n    print('pdf',p,'-> printed',rev.get(p))\ns=open('data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=s.split('\\f')\nfor b in blocks:\n    m=re.search(r'\\[pdf page (\\d+)\\]',b)\n    if m and m.group(1) in ('445','446'):\n        print('==========',m.group(1))\n        print(b[:4000])\nEOF",
 "description": "Print BQT v3 pdf pages 445-446"
}
```


### [2026-09-14T00:57:08.646Z] TOOL RESULT

```
pdf 444 -> printed 1651
pdf 445 -> printed 1652
pdf 446 -> printed 1653
pdf 447 -> printed 1654
pdf 452 -> printed 1659
========== 445
[pdf page 445]
وثالی پیمنی ‎Ke‏ باشد ‎OT, ٩‏ پرندهء‌است ‎ah‏
‏و سفید که عربان ‎Gale‏ خوانند - و بمعتی خط
هم‌آمده است خواه بردیوارکشند و خواء برروی
کاغذ ۳ - ‎ging‏ اول وسکون انی, مخفف کوتك
است که بالاخانه باشد ۴ .

کشکاب ۴ » بر وزن میتاب : آش‌جو
را گون دکه بجهت بیمار پز ند .

کشگاو * - بسکون ‎aly‏ بروزن‌ومعنی
کشکاب است که آش جو باشد .

کشکبا 1 ه بفتح اول و سکون ‎gt‏
‏و الت و بای ابجد بالف کذیده , آش حلیم را

کشکر لك ۷ - بارای قرشت ‎Os»‏
‏احمدك, پرنده ای
است سیاه و سفید
که ‎RA Lat‏
‎aS‏ و عربان
‎Gate‏ خوانند .

کشکشان.

بروزن حهوشان۸ ۰

۰ agli \ lad 0

Vere

مخقف کشان کشان است که کنابه ازآهسته و
بتألی‌براه رفتن ‎lps‏ بردن ‎th‏

کشکله م بر وزن مشفله ؛ نوعی از
‎ch‏ افزار باشد که شاطران و پیاده روان بر پای
کنند ‎٩‏ .

کشکنجیر ‎athe‏ اول ۱۴و ثالث
وسکون ثالی و نون و جیم بتحتال ی کشیده‌وبرای
قرشت زده » چیزی باش دکه بکشیدن ‎OT‏ ارمان
و آرزری کمان کشیدن حاسل شود و ‎OT‏ چنان
است که ستونی برزمین فروبرند و سرآنراشکافته
غلطکی برآن قرار دهند ورسمانی بربالایغلطك
اندازت و ازآن شکاف ‎asl aS‏ و از يك سر
‎clas vey‏ را پر از منک ‎Sy,‏ کرده
بیاویز ند و بر مان ‎OT‏ ستون قبضه مانندی‌صب
کنند ‎KS‏ خواهد مشق کمانداری کندبدست
چپ ‎OT‏ فبضه را بگیرد و بدست راست سر ‎OT‏
‏رسمان را ود ر کشا کش آورد(۱) وآنرا بثیرازی
منجل و پعربی مجیر و بهندی منجر گویشد -
یمعنی فلاخن هم آمد» است - وم ‎Sal‏ توپ
کلاترا میگویند که بدان دبوار قلمه را سوراخ
کنند و ‎ans,‏ و خراب سازند و بعضی کویند

۱ س«کس‌که» ‏ کشکرك (ه.م.), قس ‎-Karshiptan_ toy)‏ پهلوی ‎karsh(ift‏
‏(مفهوم ‎oF‏ واخح لیست) » وخی ‎karjbpe‏ « سریکلی ‎kshebe gas ۰ karjope‏ ( زافی ,
کلاغ زاغی ‎(JT) Elster=(‏ « استق۷ه ۰ عم )4( = ‎magpie‏ ( انگ ).

۴ ۳ کشه (ه.م.) و ‎nh‏ معنی در دساتیر هم‌آمده « فرهنگگ دساتیرص*۲۹*.

۴ رگ : کوشکه. معرب ‎OT‏ هم «کشك» ‎Sy‏ : اقرب الموارد . المنجد .

۴ - از :کشکه + آب ح کشکاو , خورشی که از کشکه وآب و روغن و مسالح‌دیگر

ea) ‏کتتاب‎ 2 ay

- از + کدکه+ با ‎AGT We)‏

‎kishkarak LS, - ۷‏ , درقروینی « کشک رکه » « جهالگیری ». رك : کشك .

‎. kishkish4n ‏امروزه‎ - ۸

‎٩‏ - پای پاکیزه برهنه به ببی

‏یز نم اول صحیم است .

‏چون ‎ole‏ اندر ‎Quays‏ کشکله .
‎soli?‏ خرو بلخی ص ۴۳۸۵

========== 446
[pdf page 446]
--1۵۳-

‎UIT‏ توپ است ؛ و ‎gene‏ دیگ رکویند سنگی
باشد که در منجنیقگذارند و پرحصار الدازند با
بر خصم ‎Vas‏ و وجه ‎has‏ آنکوشك‌سوراخ
کننده باشد چه کشك مخفف کوشكث است‌وانجیر
‎me‏ سوراخ هم‌آمده است ۲ .

‎GES = FO‏ نفد کشکینه
است که نان جو باشد ؛ و بعض ی کوبند ‎Babb‏
‏که ازآرد جو و آرد ‎WL‏ وآرد گندم وآردنشود
مجموعه را بپم آمیخته خمیر کنند و بپزند ؛
و بعضی دیگر گویند کندم بربان است که‌درظرفی
کنند و ماهیابه درآن ریزند و ییاز خام و ساق
چقندر و ‎phi‏ خرفه درآن داخل کنند ودرآ فتاب
گذارند تا ترش گردد .

‏کشکو ؟ - بر وزن بدرو ۵ ‎wie‏

‎OS‏ که آش جو باشد - ‎thy‏ مرغی هم

‏هت ‎Le‏ وسقید که ‎oT‏ را عکه خواند .

‏کشکول = بروزن مقبول » بسنی کدا
باشد یعنیشخصی که کدایی کند - وکاسة کشکول
کاسة کدا را گویند ۷ و ععنی ت رکیبیآ نکشیدن
بدوش است چه کش بممنی کشیدن و کول دوش
وکتف را کرد و با کداییکننده این معنی
هست - وکاسه‌ای را نیز گویند که کدامان دارند
- و آنچه مشهور است ظرفی باشد که ۳ براباندام
کشتی سازند .

‏کشکهای پر توه = بفتح اولوثانی»
بمعنی خطوط شماعی است چه کشك بمعنی خط
باشد و پرتو بمعنی شعاع .

‏کشکهی ‎٩‏ » بر وزن بروین » بمنی
اول ‎ET‏ است که نان جو باشد - و الیرا نیز
کویندکه ازآرد ‎WL‏ و نضود ‏ و کندم وجودرهم

‎: ‏که کشکنجیر غیر از منجنیق است‎ WL, ‏انوری‎ ce gil - ٩

‏نه منجئیق بسقفش وسد نه کشکنجیر

‏نه تیرچرخ ونه سامان برشدن بوهق.
* انوری چاپ لبریز ص ‎ANYE‏

‎: ‏کشکنجیر ثیر میانداختند‎ Slee ‏منوچهری‎ ce oul

‏داد جشن مه رکان امپهید عادل دهد

‏آن کجا تنها بکشکتجیربندازد زرنگ (خدنگه) .

‏? منوچهری ص4۸٩‏ .

‏و از ‎So bed‏ نیز همین ‎er‏ برمیآید. رلد: فرهنگه نظام ‎GUT.‏ مینوی نوشته‌اند: کشکنجیر
بعنی سوراخ ‎BET‏ کوشك . ‎OT)‏ نوعی ازآلات قلمه کشابی بوده است که بدان سنگپای کلان
با تبرهای بز که وستبر بدبوار قلعه با باروی شهر پرتاب ‎her Cae‏ واز ضربت آن‌دبوارسوراخ
و خراب میشده است ‎J).‏ : تعلیقات نوروزنامه ‎۱۲٩ oe‏ - ۱۳۰ .

‏۴ رك : الچیردن . ۴ - مخفف « کشکینه » (هم.) .

‎kashkaw - ۴‏ = کشکاب (هم.) = کشکر (هم.) . ۵ - بفتح راء .

‎SKS AV gn) ‏کیک رکه‎ me ‏«کشکر» « رتیدی‎ Gee ‏ظ‎ - ٩
‏علامه دهضدا » ؛ در عریی « کشکول  بفتح اول » مولف‎ GEG ‏آلیس‌الطالبین بخاری متملق‎ «
‏کل‌شی.‎ cole gies ) ‏کل » ( بضم اول و کسر دوم و خم چهارم‎ ET? ‏کوید ازآرامی‎ a?
‏و مراد محفظهایت که درریشان و کدایان هرچه از مردم ستانند درآن دهند - کشکول پوست‎
‏بخط استوا عمل مبآیید و شبیه بکشتیی‌است بارنگهياه,‎ thay ‏است که درجزایر‎ gle dew
‏تابتوان بدست آویخت , وآن‌کاسة کدابی‎ wae ‏سوراخ کنند و زنجیر با رسمان‎ VT ‏دوطرف‎
‏مغز نارجیل‎ OT ‏دروبشاست ؛ و آلگاه که بر درخت است دو کشکول بهم چپیده است و درمیان‎
. ‏فرهنگه دسالیر ۷۹۰ : کشکهای پرتوی » ورك : کشکه‎ « jabs ‏است . ۸ - از‎

‎. ‏دبت ). رك : کشکینه , کشکنه‎ ys) ‏از : کشک ین‎ - ٩
```


## [2026-09-14T00:57:43.078Z] TOOL CALL #33: Bash

```json
{
 "command": "pdftoppm -f 400 -l 400 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg400 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg400.png",
 "description": "Render PDF page 400"
}
```


### [2026-09-14T00:57:44.788Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 79028 Sep 13 20:57 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg400.png
```


## [2026-09-14T00:57:45.072Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT avapat / pat- verb ===\"; grep -n \"ava.pat\\|avapast\\|paiti.pasti\\|fraptar\\|fraptsr\\|patar.ta\\|patayeiti\\|pataiti\" BRT.txt | head -20",
 "description": "Bartholomae pat- forms"
}
```


### [2026-09-14T00:57:45.160Z] TOOL RESULT

```
=== BRT avapat / pat- verb ===
4316:•  ].  'an-aiwyästay-  f.  'Nichtanlegen  des Gürtels,  der  Gürtelschnur':  yat  tui  .  . /rapataiti  (sd.)  'ta  (LS.)  vä  anabdäts  vä "wenn  ein  Mann . .,  ohne  den  Gürtel  oder das  Hemd  angelegt  zu  haben"  "  V. /ä  54**; —  nöit  'H  (IS.)  astrmti  N._()5,  ^jj^'';  — a  'ti  sir:nti  H.(}6,  +95  3>,
6056:•  j.  azrö.daJtay-  Adj.  (auch  fem.)  'J^gd machend,  auf  Jagdbeute,  Raub  ausgehend': jaiivBJara  .  .  yai:a  v?hrkam'^  •da^Tm''> gaiüqm  avi  frapataiti  "todeswUrdiger  .  . ^  die  auf  Raub  ausgehende  Wälfin,  wenn ae  ins  Gehöft  einbricht"  V.  J&45.
8477:yäs<a  'rä  ytisca  . .  fravasayö  Yt  j.g;  10. ' 100,  y.147,  Vr.2/.i;  —  ta'ja  dim  aAurd mazda  avim  .  .  tat  äp3  'rasca  YtÄ?;  — katTM  d?r?tä  .  .  avapastsis  (sd.)  .  .  aps 'räscä  \.44.\;  —  usta  aps  'räsca  YtÄ »9;  23,  y-79'.  93'.  Y.i.iJ,  2.12,  76'.9, 7A63,  V.tf.46,  12.2,  Ny.4.0,  FrW./.2;
11387:im  Nachsau  'dann  wenn  . .  dann':  aSa TyasHi  pairi.pataiti  aoa  /raätim  vöiyna- »am  Csd.)  V.  /.  3.
11606:•  j.  Jahikä-  f.  dnw.  jaAi-  '• :  yai  nä  ['ia] " .  .  frapataiti  anaiwyästa  (sd.)  vä  . .  V, /Ä'.  54;  —  narö  pairistajduorö  ..  "ka para.daxsta  (sd)  Yt/J.  54;  —  mä  ki mairys  giurvaysii  mä  °ka  Yt,Ä59;  — nSit  *mairyeke  ndif  'kayä  P.  jo ;  —  tat näiriiayäi  .  .  aJaonyai  .  .  tal  'kayäi  . . drvaityai  i^ar3%3m  H.3,iS-36;  —  'kayai
14842:mit  avi  ^xnAfrä  'anfallen,  einfallen  in  — ' (Akk.),  von  «iift'ischen  Tielren:  yd^a  vä vihrkqm  (statt  NS.)  .  .  gagiam  aii  fra- pataiti  yäia  vä  vazayam  (statt  NS.)  .. ap»m  avi  frapataiti  V.'iÄös.
14852:.    (g.''>)   P-  pat-  V.    'fliegen;    fallen'.    (stattAP.)  Afl//fl  ^arÄff«  .- a/(//o/(Augm.) Praes.  a/a/a,  ipta-,  ta-''>,  24pataya-i\'/ra/9rajeYt.  ig.B2.       z) 'herum-,  zu  Ende 30  (KaMS.)pataya-'\  —  Inf.  'pastSiS,  'patai,  gehen',  vom  (/aftischen Winter:  aia  sySsHp *'paiiita  (Kaus.);  Absol  patnU»m.        [Vgl.  ■  pairipataiti  V.  i.  3. noch  tata-]  miifrä  1)  auffliegen':  yatfrä  vayS patan
14854:Ä8.  a)  mit  Abi.  'aus  -':  paourva.-  daliß&z\ia  Art  'herangehen  zu-';  a)  mit namat patai  dyaoHf^A.)  .  .  anrö  mainyus  -qxl.:  hamaka  airyabyU  daiAhubyB  hatna Yt. j.  iz;—ptat  (3SPrA.) F.  10.  3) ^oia ,  f^apatänti")  Yt  S.  61.  b)  m\tpaiH und Wasser;  a)  'herabfallen,  -strömen',  vom  j  Akk,;  s.  a/rapatai  Int Regenwasser:  s.-V««/-(in/«/.3A).  b)'über-  mit  z^r(z'(/)  in  rfo^Hscher  Art 'weg-,  fort- fliessen',vomsiedendenWasser(?):><W««/a  l,gn,.  ^fj- ^pam  Ha patmiu  vi  dalvhM (sd.)  patmla  F.  4  f.  4)  Term.  techn.  für  %j  ^  g  yf /o.  i . dasGehen  rfjftTschcr  Wesen:  hamySila  ..\  mit,ia«'fallen,hinabstürzen in-'(Akk.): davqi>ya  patqi^yä  Y.g.  18;  —  vagn^mn^  \  ^ru/asianam(sd.)  haMpataiti{T&m\.daevd) (sd.)  anmat  para  dalva  patayin  Yt  ig.  80; '  V  70  4.1    '  *
14871:•  j.  patarvta-  Adj.  'im  Flug  hegTiSeii,i  nipai'.yante(s±)  Äqm  vä 'ti  stairi/Aqrri  vä fliegend':  äsyajgia  (sd.)  vayazibya  °taiibya\°ti  bartzi^  V . ^.  ^i .  b)  auf  die  Frage ". ,  als  ein  paar  fliegende  Vögel"  Y.  57. 28;  i  wo?:  talam  vantanhS . .  gätiis  'ti  ^ätjfante — pasubya  staoralibya  vayaeibya 'taäbya^^  (S'p.  i^^  n.)  Ytij.io;  —  ya^/a  argAaJ yS  parmJnS  (sd.)  fravazänte  "mit  Klein-  1  bartsnul  'ti  gairinqm  V.  2.  23";  Y.^.  26, undOrossviehundmittliegenden Vägeln, .. "1 /0.3; —  :i^armö  baxlmli  zqm  'ti  akura- YtJO.119.  \Vttqm   Yt.6.1,  7.3;  jp.48,'$o,  Y. 13.4g,
18690:39,  79.69;  'Yt4-t,  Vyt.  74^;  —  duye navaiti  narqm  a/aonqm  vasiryaäa g^ . . - V.  74. 1 7 ;  A.  j.  7 ;  —  aü'hwSjgabmq  .  . narqm  aIaunqmY.13.3; — Sing.inkollekt. Sinn:  %rilum  nari  asaonS  frayoAuma- take  . .  apayasaitt  V.  18. 64.  c)'**  kas- na'^^  dtrita  tqmta  . .  avapastBt/ (sd.)  ks apB  . .  ks  .  .   iasnä'^^   "(welcher   Mann
23199:•  j.  vazaj^-  m.,  vazaj'a-  f.  'Frosch; Frosch  Weibchen';  ein  iÄiÄ-isches  Tier,  von dem  zwei  Arten  geschieden  werden,  Land- undWasser&Ösche:  °yanqm  dalmainyanqm (sd.)  .  .  'yanqm  ufapanqm  (sd.)  V.  14.  5 ; 'Ä73i  —  -yacT/ (statt  NSm.}  vii.kuskS\ tarS  ySr?  msrM  "ein  vertrockneter  über ein  Jahr  toter  Frosch"  V.5.36; — }q%wS.- tara  ..ydha  v3  °yq/ri  (statt  NSf)  hazavrS.- hunqm  äpim  frapataiti  "todes würdiger  als das  .  .  Froschwei beben,  wenn  es  sich  ins Wasser  stürzt"  V, /Ä'.  65.
23757:•  }.,  g.  vtnzyant-  Adj.,  PPA.:  s.  ava.)  Überschwemmung':  aoa  zyasHipairi- ^vam-.  pataiti  ata  fraist>m  'nanqm  "dann  wenn
27699:—  yB  hakat  astJica  ..  zimä^a'-^  kam.- rai%wayäti  (sd.)  Yt.  70. 72.  Daher  a)  oft im  Gegensatz  zu  a)  Himmel  und  Luft- raum: atitary  zqm  asmaiumca  Y.68.1^, Yt.<y.8,  io.95,  /J.13',  43,  44,  Y.Ol.i, H.7.16;  Yt  79.43;  —  vispqmca  zqm  .. vTspimca  asmamm  Y.  77,  9;  —  imqmla zqm  .  .  aomla  asmatam  "die  Erde  hier ..  der  Himmel  dort"  Yt7j.i53;  2,  77. 57,60; —  aiähäsia  ztmB  avai^htia  asnS Y.  7. 16;  —  kasna  djritä  zqmcä  ads  na- bäsiä  avapastöÜ {%A)  Y.44.  4;  —  s.  noch A.  ß)  den  Leuchten  des  Himmels: yetihe  växi  ,  ,  us  ava  raocä  asnaoiH  ava pairi  tmqm  sqm  jasaiti  Vt  70.85;  89, H.  7,  21;  —  ka^a  avatbyS  sitnbyB  aoi zqm  Yt5.85.  a)  Im  Gegensatz  lu Wasser  'Erde,  Land,  Festland':  aSavat apal  haca  nilbäraym  huskei^'A^  z?me''' nidaiiiyqn  V.(7. 29;  31;  —  zugleich  im Gegensatz  zu  Pflanzen:  zqm  akuraläiqm äptm  ,.  urvarqm  y.ig.$$;  5.33,  4a,  77. I,  a,  5,  9,  H,  7. 3;  —  Aa^a  apaj ..  z^mat •  ■  S^H  ,  .  urvarayät  V.  77.  10;  —  nava 3fs  .  .  tä  ..  urvarä  V.27.3;  —  ta^a fanti  sartta  äps  .  .  s»mB  . .  urvarayä V.  7. 3 ;  —  auch  Flur. :  imat  vS  äpS  Jaii- yemi  . .  z}mB  (VP.)  . .  urvarä  Y.  Ö3. 1  a;
```


## [2026-09-14T00:57:51.878Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg400.png"
}
```


### [2026-09-14T00:57:52.373Z] TOOL RESULT

```

```


## [2026-09-14T00:57:52.343Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T00:58:08.302Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npdftoppm -f 400 -l 400 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg400big\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg400big.png'); print(im.size)\n# kasak box region: from 200dpi coords approx x 900-1200, y 720-830 -> scale 3\nim.crop((2700,2130,3600,2520)).resize((1800,780)).save('pg400_kasak.png')\nim.crop((1750,3200,2500,3500)).resize((1500,600)).save('pg400_french.png')\n\"\nls",
 "description": "Crop regions of page 400"
}
```


### [2026-09-14T00:58:13.234Z] TOOL RESULT

```
(5100, 6600)
agents.txt
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
c404-empty.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
crop14-394.png
crop18-394.png
edit_about.py
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
pg399.png
pg400big.png
pg400_french.png
pg400_kasak.png
pg400.png
pg404hi.png
pg404.png
pg405.png
pg406.png
pg408-ampus.png
pg408-germ.png
pg408.png
queue.txt
```


## [2026-09-14T00:58:15.306Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg400_kasak.png"
}
```


### [2026-09-14T00:58:15.331Z] TOOL RESULT

```

```


## [2026-09-14T00:58:21.242Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg400big.png')\nim.crop((3300,2400,4100,2750)).resize((2000,875)).save('pg400_kasak2.png')\n\"",
 "description": "Crop kasak Persian script"
}
```


### [2026-09-14T00:58:22.965Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:58:24.816Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg400_kasak2.png"
}
```


### [2026-09-14T00:58:24.854Z] TOOL RESULT

```

```


## [2026-09-14T00:58:35.799Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg400big.png')\nim.crop((3700,2560,3980,2700)).resize((1680,840)).save('pg400_kasak3.png')\n\"",
 "description": "Zoom second Persian word"
}
```


### [2026-09-14T00:58:37.418Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:58:39.695Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg400_kasak3.png"
}
```


### [2026-09-14T00:58:39.732Z] TOOL RESULT

```

```


## [2026-09-14T00:58:51.154Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg400big.png')\nim.crop((1950,3520,2700,3720)).resize((2250,600)).save('pg400_fr2.png')\nim.crop((2950,3520,4000,3760)).resize((2100,480)).save('pg400_fa_heli.png')\n\"",
 "description": "Crop French helicopter box"
}
```


### [2026-09-14T00:58:52.799Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:58:55.075Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg400_fr2.png"
}
```


### [2026-09-14T00:58:55.206Z] TOOL RESULT

```

```


## [2026-09-14T00:58:55.204Z] INPUT

[Image: original 2250x600, displayed at 2000x533. Multiply coordinates by 1.13 to map to original image.]


## [2026-09-14T00:59:20.930Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW accipiter/acupedius ===\"; grep -n -i \"accipiter\\|acupedius\\|acu-pedius\" LEW_1910.txt LAT.txt | head -20\necho \"=== KLN accipiter ===\"; grep -n -i \"accipiter\" KLN_1966.txt KLN_1971.txt | head -10\necho \"=== KLN helicopter ===\"; grep -n -i \"helicopter\\|hélicoptère\" KLN_1966.txt KLN_1971.txt SKT.txt | head -10\necho \"=== KLN feather ===\"; grep -n -i \"^feather\\|feather, \" KLN_1966.txt | head -5",
 "description": "Grep Latin and Klein for accipiter, helicopter, feather"
}
```


### [2026-09-14T00:59:21.041Z] TOOL RESULT

```
=== LEW accipiter/acupedius ===
LAT.txt:1098:accipiter,-trls m.(f. dans Lcr.): oiseau de proie, epervier ou
LAT.txt:1103:55; e "t Caper, GLK VII 107,8, accipiter, non acceptor. Le nom rustique
LAT.txt:1111:Si l'on fait abstraction de 1 'influence de accipio, le mot accipiter
LAT.txt:1112:est parallfele A acupedius (v. ce mot). De meme que acu-pedius rappelle
LAT.txt:1113:gr. ojcu-to>u C, accipiter rappelle gr. dao-nxepoq, skr .d<pu-patvan- "qui vole
LAT.txt:1345:Adaptation de ofjimouc., comme celeripes de ajamouc. V. accipiter. Pour la
LAT.txt:5632:r 4 cente. V. accipiter.
LAT.txt:42951:coaposds dans lea aots archaxques: acupes, acupedius, accipiter (v.
LAT.txt:47252:dans des formes isolAes et obscures, penna st accipiter. - Pour "ton¬
LAT.txt:47734:de ling. roaane, I 336; pipiunculus: accipiter, accipitor (Gloss.);
LAT.txt:64607:dont il exiate an doublet pipiunculus: accipiter, acceptor (Gloas.).
=== KLN accipiter ===
KLN_1971.txt:5442:Accipiter, n., a genus of hawks and falcons (orni- 
KLN_1971.txt:5443:thol.) — L. accipiter fr. orig. *acu-peter, ‘swift- 
KLN_1971.txt:21725:ML.,fr. L. acceptor , secondary form of accipiter , 
KLN_1971.txt:21726:‘falcon’ (see accipiter), whence also OSp. aztor , 
KLN_1971.txt:110590:the second element in goshawk. L. accipiter , 
KLN_1971.txt:169868:alteration of L. accipiter, ‘hawk’. See Accipiter 
KLN_1966.txt:1342:Accipiter,  n.,  a  genus  of  hawks  and  falcons  ( orni - thol.)  —  L.  accipiter  fr.  orig.  *acu-peter,  ‘swift¬ ly-flying’,  but  influenced  in  form  through  a  con¬ fusion  with  accipere,  ‘to  take,  receive’.  The  first element  lit.  means  ‘sharp’  (cp.  acu-pedius,  ‘swift¬ footed’,  lit.  ‘sharp-footed’,  and  acuere,  ‘to sharpen’) ;  see  acute.  The  second  element  is  cogn. with  OI.  patram,  ‘wing,  feather’,  Gk.  nrepov, ‘wing’,  OE.  feder,  ‘feather’.  See  feather.  Cp. Astur,  ostreger.
KLN_1966.txt:3775:Astur,  n.,  the  genus  of  the  goshawks  (zool.)  — ML.,  fr.  L.  acceptor,  secondary  form  of  accipiter , ‘falcon’  (see  accipiter),  whence  also  OSp.  aztor. Port.  a(or.  It.  astore,  OProveng.  austor,  OF. ostoir,  ostour,  F.  autour,  ‘goshawk’.  Cp.  ostreger. astute,  adj.,  shrewd,  cunning,  crafty.  —  L.  astu¬ tus,  ‘artful,  drafty,  cunning’,  fr.  astus,  ‘clever¬ ness,  craft,  cunning’,  which  is  of  uncertain origin.
KLN_1966.txt:17319:Derivative:  haw,  n.,  hesitation  in  speech, hawk,  n.,  any  bird  of  the  falcon  family,  —  ME. havee,  hauk,  fr.  OE.  heafuc,  heafoc,  hafoc,  rel. to  OS.  habuc,  ON.  haukr,  Swed.  hok,  Dan  .hog, MLG.  havee,  MDu.,  Du.  havik,  OHG.  habuh, MHG.  habech,  G.  Hahicht,  ‘hawk’,  and  cogn. with  Russ,  kobec,  a  kind  of  falcon.  These  words lit.  mean  ‘seizer’.  They  derive  fr.  I.-E.  *gabh-,  a var.  of  base  *qap-,  ‘to  seize’,  whence  have  and heave.  Cp.  the  first  element  in  Hapsburg  and the  second  element  in  goshawk.  L.  accipiter, ‘hawk’,  is  not  cognate  with  the  above  words. Derivatives:  hawk,  tr.  v.,  to  hunt  animals  by means  of  trained  hawks,  hawker  (q.v.),  hawk¬ ing,  n.
KLN_1966.txt:26726:ostreger,  also  ostringer,  n.,  keeper  of  goshawks.  — ME.,  corrupted  fr.  OF.  ostruchier ,  astrucier,  fr. ostor ,  ostur,  ostoir  (F.  autour),  ‘goshawk’,  fr. Late  L.  auceptorem,  acc.  of  auceptor,  alteration of  acceptor,  ‘hawk’  (under  the  influence  of  L. auceps,  ‘birdcatcher,  fowler’),  which  itself  is  an alteration  of  L.  accipiter,  ‘hawk’.  See  Accipiter and  cp.  Astur.  The  n  in  ostringer  is  intrusive;  cp. messenger  and  words  there  referred  to. ostrei-,  combining  form.  —  See  ostreo-. ostreiculture,  n.,  the  culture  of  oysters.  —  Com¬ pounded  of  ostrei-  and  culture.
=== KLN helicopter ===
KLN_1971.txt:91158:compete, diptote, fern, helicopter, hippopotamus, 
KLN_1971.txt:111580:helicogyre, n., a kind of helicopter. — Com 
KLN_1971.txt:111595:helicopter, n. — F. helicopter e, compounded of 
KLN_1966.txt:14491:feather,  n.  —  ME.  fether,  fr.  OE.  feder,  rel.  to OS.  fethara,  ON.  fjddr,  Swed.  fjader,  Norw. fjer,  Dan.  fjter,  MLG.,  MDu.  vedere,  veder Du.  veder,  veer,  OHG.  fedara,  MHG.  vedere , veder,  G.  Feder,  fr.  Teut.  *fep(a)rd-,  correspond¬ ing  to  I.-E.  *petra-,  zero  degree  *ptera-, ‘wing;  feather’,  whence  OI.  patram,  ‘wing, feather;  leaf’,  Hitt,  pittar,  ‘wing’,  Gk.  7tTEp6v, ‘feather;  wing’,  Ttxepu!;,  ‘wing’,  OSlav.  pero  (for *ptero ),  ‘feather’.  Arm.  t'ir  (for  *pter-),  ‘flight’, OW.  eterin,  ‘bird’,  atar ,  ‘birds’,  and  the second  element  in  L.  acci-piter,  ‘hawk’;  fr. I.-E.  base  *pet-,  ‘to  fly,  fall  upon,  fall’,  whence also  OI.  patati,  ‘flies,  descends’,  patayati,  ‘flies’, Gk.  7r£TEa»oa,  ‘to  fly’,  ttoxx;,  ttoxt^x,  ‘flight’, 7roxa[x6<;,  ‘river’,  lit.  ‘something  flowing,  run¬ ning’,  7rl7rT£iv,  ‘to  fall’  (formed  fr.  orig.  *nl- 7TTELV  on  analogy  of  6:~telv.  ‘to  throw,  cast’), L.  petere,  ‘to  fall  upon,  rush  at,  attack,  assail ; to  seek,  ask,  request’,  perma  (OL.  pesna;  for pet-s-na),  ‘feather’,  OIr.  en,  gen.  eoin  (for  *pet- nos),  ModW.  edn,  OBret.  etn,  ‘bird’.  Cp.  Acci- piter,  appetence,  appetite,  aptote,  asymptote, compete,  diptote,  fern,  helicopter,  hippopotamus, impetigo,  impetus,  malabathrum,  Mesopotamia, pen,  ‘feather’,  pennate,  pennon,  peripeteia,  peri¬ pteral,  perpetual,  Petaurista,  petition,  petulant, pinion,  ‘distal  segment  of  a  bird’s  wing’,  pota- mo-,  propitious,  pteno-,  pteridium,  Pteris,  ptero-, pterygium,  ptomaine,  ptosis,  repeat,  repetition, symptom,  talipot,  triptote. feather,  tr.  and  intr.  v.  —  ME.  fetheren,  fr. OE .gefiderian,  ft.  feder,  ‘feather’.  See  feather,  n. Derivative:  feather-ed,  adj.,  feather-let,  n. feature,  n.  —  ME.  feture,  ‘shape,  form,  feature’, fr.  Of .  faiture,  feture,  ‘fashion,  shape,  form’, fr.  L.  factura,  ‘something  made’,  fr.  factus,  pp. of  facere,  ‘to  make,  do’.  See  fact  and  -ure. Derivatives:  feature,  tr.  v.,  feature-less,  adj. febri-,  combining  form  meaning  ‘fever’.  —  L. febri-,  fr.  febris,  ‘fever’.  See  fever, febrifugal,  adj.,  dispelling  fever.  —  See  next  word and  adj.  su(T.  -al.
KLN_1966.txt:17466:helicogyre,  n.,  a  kind  of  helicopter.  —  Com pounded  of  helico-  and  Gk.  Yupoc,  ‘circle,  ring’. See  gyre.
KLN_1966.txt:17471:helicopter
KLN_1966.txt:17473:helicopter,  n.  —  F.  helicopter e,  compounded  of Gk.  sXt£,  gen.  thiv.oq,  ‘coil,  spiral’,  and  rcxEpov, ‘wing’.  See  helix  and  ptero-. helicotrema,  n.,  the  opening  connecting  the  two scalae  in  the  cochlea  ( anat .)  —  Medical  L.,  fr.
=== KLN feather ===
2155:aletho-  and  Gk.  nxipip,  ‘fern’,  which  is  rel.  to Tcx£p6v,  ‘feather,  wing’.  See  ptero-.
3257:feather  and  cp.  symptom  and  words  there  re¬ ferred  to.
10917:deployer.  See  prec.  word  and  -mcnt. deplume,  tr.  v.,  to  pull  the  feathers  of,  to  un¬ plume.  —  F.  deplumer,  pluck,  unplume’,  fr. ML.  deptumdre,  fr.  de-  and  L.  pluma,  ‘feather, down’.  See  plume  and  cp.  unplume, depolarize,  tr.  v.,  to  deprive  of  polarity.  — • Formed  fr.  de-  (in  the  privative  sense  of  this prefix)  and  polarize.
11536:Diptera,  n.  pi.,  an  order  of  insects,  the  flies  ( en - tomol.)  —  ModL.,  fr.  Gk.  Sitrrepa,  neut.  pi.  of SbiTEpo?,  'having  two  wings’,  fr.  Si-  (see  di-, ‘two’)  and  mepiv,  ‘feather,  wing’.  See  ptero- and  cp.  next  word.
11539:Dipteryx,  n.,  a  genus  of  trees  of  the  pea  family (bot.)  —  ModL.,  fr.  di-,  ‘two’,  and  Gk.  Tt-repui;, ‘wing’,  which  is  rel.  to  rcrepov,  ‘feather,  wing’. See  ptero-.
```


## [2026-09-14T00:59:38.719Z] TOOL CALL #45: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T00:59:38.728Z] TOOL RESULT

```


```


## [2026-09-14T00:59:41.618Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peth%E2%82%82-",
 "prompt": "What is the root's meaning, and which descendants (Avestan, Old Persian, Sanskrit, Greek, Latin, Germanic) are listed? Quote the etymology and the main derived terms."
}
```


## [2026-09-14T00:59:43.735Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%AA%D8%A7%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology of افتادن (oftādan/uftādan): Middle Persian form, Proto-Iranian reconstruction, root, and any cited sources."
}
```


### [2026-09-14T00:59:48.125Z] TOOL RESULT

```
# Proto-Indo-European Root *peth₂-

## Root Meaning
The root has two primary meanings: "to spread out" and "to fly" (understood through the sense of spreading one's wings).

## Etymology
The entry notes that this root exists "in variations, *pet-, *peth₁-, *peth₂-."

## Key Descendants Listed

**Avestan:** The text mentions "patarəta" (winged)

**Sanskrit:** Multiple forms appear, including "papā́ta" (perfect form), "pátra" (leaf), and "pātáyati" (to cause to fly, throw, send; to cause to fall, fell; to spill, pour)

**Greek:** "píptō" (to fall) and "pétălon" (petal/leaf)

**Latin:** Forms include "pateo" (to be open), "patera" (bowl), and "passus" (step)

**Germanic:** "faþmaz" and "feþlą" are listed as descendants

## Main Derived Terms

Notable formations include the reduplicated present "*pí-pth₂-e-ti" (yielding Greek píptō), the nasal-infix present "*pt-né-h₂-ti," the causative "*pot(h₂)-éye-ti," and the nominal "*péth₂-lom" (leaf), which generated Greek pétalon, Sanskrit pátra, and Germanic feþlą.
```


### [2026-09-14T00:59:48.975Z] TOOL RESULT

```
# Persian Etymology of افتادن (oftādan)

## Middle Persian Origin
The word descends from Middle Persian **ōft-** (meaning "fall"), which evolved into the modern Persian form.

## Proto-Iranian Reconstruction
The Middle Persian root derives from Proto-Iranian:
- **\*ava-** ("away, down") + **\*pat-** ("to fly, rise; to fall")

## Proto-Indo-European Roots
These Iranian elements trace back further:
- \*ava- comes from Proto-Indo-Iranian **\*Háwa** ("away, down")
- \*pat- comes from Proto-Indo-European **\*peth₂-** ("to spread out; to spread one's wings, fly")

## Cited Source
According to the Wiktionary entry, Johnny Cheung's *Etymological Dictionary of the Iranian Verb* (Brill, 2007, page 301) documents this etymology, establishing the systematic sound changes from ancient Indo-European through Middle Persian to modern Persian.
```


## [2026-09-14T00:59:53.770Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^\\*PAT\\|PAT ‘\\|\\*pat-\\|ōft\\|uftādan\\|ava-pat\" CHEUNG.txt | head -20",
 "description": "Grep Cheung for PAT"
}
```


### [2026-09-14T00:59:53.814Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:59:55.452Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA",
 "prompt": "Give the Persian etymology of پست (past) 'low, base': Middle Persian form, Proto-Iranian reconstruction, root, cognates, and any cited sources. Also note any Arabic or other entries on the page."
}
```


### [2026-09-14T01:00:01.826Z] TOOL RESULT

```
# Persian Etymology of پست (past) 'low'

Based on the Wiktionary entry provided, the etymology section for the adjective پست (past) meaning "low" or "abject" is notably sparse. The page states:

"Compare [Armenian](https://en.wikipedia.org/wiki/Armenian_language "w:Armenian language") _[պստիկ](/wiki/%D5%BA%D5%BD%D5%BF%D5%AB%D5%AF#Armenian "պստիկ")_ (pstik)."

**Key observations:**

- **No Middle Persian form is explicitly provided** in this entry
- **No Proto-Iranian reconstruction is listed**
- **No root is cited** for this etymological sense
- The only comparative cognate mentioned is Armenian *pstik*
- The entry does not distinguish this adjective's origin from the separately-listed noun meanings

The page does include an elaborate etymology tree for Etymology 3 (the noun meaning "post"), tracing it to French *poste* through Proto-Indo-European and Latin, but this does not apply to the adjective sense discussed here.

**Notably absent:** Middle Persian attestations, reconstructed Proto-Iranian forms, and detailed etymological documentation for the adjectival meaning.
```


## [2026-09-14T01:00:06.665Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG head ===\"; grep -n \"pat\" CHEUNG.txt | head -20\necho \"=== PHD past ===\"; grep -n \"past \\[\\|past\\b\" PHD_mackenzie.txt | head -10",
 "description": "Cheung and MacKenzie for pat/past"
}
```


### [2026-09-14T01:00:06.727Z] TOOL RESULT

```
=== CHEUNG head ===
391:(old) *r and all ablaut series consist of the pattern, full grade *aC, lengthened *aC 
477:consuming to compile and correct the attested forms than anticipated initially. For 
1386:BSogd. B’m’k ‘colour’, BSogd. B’m’nt ‘shining’ || (+ *pati-) ? BSogd. ptByw, 
1479:s.v. *pat. The Wa. form has a (voiced) stop -b-, which cannot derive from old Ir. *b 
1518:*SOGDIAN: (+ *pati-) ? MSogd. ptByw Asg. ‘honouring, paying homage’ (МКС 585) 
1606:prison; band’ || (+ *pati-) MMP pywyn- ‘to bind, join’ || (+ *pari-) BMP plwnd- 
1615:perf. pass. MMP bstg, BMP bstk /bastag/, MMP bst, bst, Inf.: BMP bstn /bastan/, MMP bstn || (+ *pati-) 
1621:*PARTHIAN: bnd- ‘to bind’, IPth. bs- ‘to construct (a bridge)’ || (+ *pati-) pdbnd- ‘to 
1625:IPth. bstny || (+ *pati-) Pres.: IND. 3sg. pdbndyd; Partic.: perf. pass. pdbst || (+ *fra-) Partic.: perf. pass. 
1628:*KHOTANESE: bañ- ‘to bind’ || (+ *pati-) pabafi- (pabas-) ‘to bind’ || (+ *ham-) OKh. 
1633:‘to be impeded, restricted’ || (+ *a-) BSogd.*’’Bnd- ‘to bind, join’ || (+ *pati-) 
1641:"B'stk, CSogd. "bet || (+ *pati-) Pres.: OPT. 3sg. BSogd. pcBynt’y; Impf.: IND. 3sg. BSogd. ptB’ynt, 
1647:(of speeches)’ || (+ *pati-) pcBncy- ‘to bind together’, (pass.) ‘to be bound together’ || 
1666:-Bäst-/-Bäst-, Lasg. -Bast- ‘to bind’ || (+ *pati-) NP payvastan/payvand- ‘to join, 
1672:*pati-) Rosh. padve60-/padvost ‘to knit (a broken bone) || (+ *ni-) Oss. I. 
1705:on’ || (+ *uz-) ‘to bring, carry out’ || (+ *pati-) ‘to bring back; to commence’ || (+ 
1746:*OLD PERSIAN: bar- ‘to bear, lift, esteem’ || (+ *4-) ‘to perform’ || (+ *pati-) ‘to bring 
2146:*AVESTAN: baod-, Y Av. baoö- ‘to feel, sense’ || (+ *pati-) ‘to concentrate on, heed’ || 
2154:*MIDDLE PERSIAN: ВМР bwd /boy/ ‘perception, sense’ || (+ *pati-) MMP pyws- 
2157:(+ *pati-) Pres.: pres. IND. 3pl. pywsynd; Partic.: perf. pass. MMP pywst {unpubl.} 
=== PHD past ===
367:nouns in -dar/-tar [-t'l], and past participles in -dag/-ta~
1228:aspast [,spst l I N .-...] clover, lucerne.
4102:past [pst l IN .......] low; astr. dejection.
4117:past(ag) [pst(k)1 I J pst] pact, bond, agreement.
5919:agreement husazagih; pasn, past;          anti-knowledge pas-danisnih.
6081:bond band; mihr, paSn, past(ag).       bridge puhl.
6209:clover aspast.                              idan, hanJaftan.
6371:dejection (astr.) niseb, past.             detailed gokiinig.
6991:limb handam, (hannam), pesag.            lower, past.
6994:limit kanarag, karan, saman, wim-        lucerne aspast.
```


## [2026-09-14T01:00:12.717Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\*pat$\\|\\*pat ‘\\|^\\*pat\\|pat ‘to fly\\|‘to fly, to fall\\|to fall, fly\" CHEUNG.txt | head -20\necho \"---\"\ngrep -n \"PAT\" CHEUNG.txt | head -20",
 "description": "Locate Cheung *pat entry"
}
```


### [2026-09-14T01:00:13.849Z] TOOL RESULT

```
1672:*pati-) Rosh. padve60-/padvost ‘to knit (a broken bone) || (+ *ni-) Oss. I. 
3835:*pati-) Oss. D. fecawun/fecud ‘to pass, drive by’ 
4581:*pati-) Wa. pidic-, pidic-/piön-, pidn-, pidiyn- “о catch fire, be ignited’ 
4629:*pati-) padim- ‘to make’ => SGS: 46, 69, 118 
6749:*pati-) pdbwrs- ‘to read, recite’ || (+ *ui-) wyfr’s- ‘to teach, show’ = Ghilain: 69, 79 
6759:*pati-) Khot. pus- (pus-) ‘to read’ = SGS: 85, 20 
6875:*pati-fräuaia- (*frau'). The assumed common shift in meaning of ‘to fly against’ to 
6922:*pati-) BSogd. ’ps’nkty (pl.) ‘instruments of torture’, CSogd. pteng, peng, CSogd. 
7407:*pati-) SSogd. pty’m (m.), BSogd. pty’m, CSogd. pty’m ‘message’, CSogd. 
8622:*pati-) MMP pdyr- ‘to take, receive, accept’, BMP ptgyl- (MKBLWN-) /padir-/ ‘to 
11206:*pati-) ? OKh. peh- ‘to obtain’ || (+ *pari-) OKh. prev- ‘to obtain’ = SGS: 20, 106, 
11941:*pati-) ? LKh. pasus- ‘to become soundless’ = SGS: 153, 78 
12888:*pati-) MSogd. ptrys ‘to tear away’, BSogd. ptr’ySky ‘tearing away’ 
15104:*pati-) CSogd. ptyny’ (loc. sg. f.) ‘in the manner of (Schwartz 1967: 151) || С 
15491:*pati-) (?) NP paykandan/paykan- ‘to join; to collect; to draw out’ || (+ *pari-) NP 
15692:*pati-) Anar. pakaft/pak- ‘to strike’ 
18526:*pati-) BSogd. ptn’ym- ‘to imitate’ 
18879:*pat ‘to cook’ 
19683:*pat 299 
19739:*pat ‘to fly, rise; (?) fall’ 
---
```


## [2026-09-14T01:00:16.607Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '19735,19830p' CHEUNG.txt",
 "description": "Print Cheung *pat entry"
}
```


### [2026-09-14T01:00:16.657Z] TOOL RESULT

```
*REFERENCES: EVP: 37; UEL II: 234a, 238a; Morgenstierne 1942: 265; Abaev, Slovar’ I: 424; 
Andreev-PeSéereva: 294a; DKS: 249a; Steblin-Kamenskij 1999: 247 


*pat ‘to fly, rise; (?) fall’ 

*AVESTAN: Y Av. pat- ‘to fly’ || (+ *aua-) ‘to fall down, off’ || + *4-) ‘to come, rush 
to [daévic]’ || (+ *us-) ‘to come, go ош [daévic]’ || (+ *fra-) ‘to fly up; to enter 
[daévic]’ || (+ *ham-) ‘to fall, crash’ = Liste: 32f. 


300 *pat 


Pres. them.: IND. 3sg. YAv. frapataiti (Yt 8.61, V 18.54, V 18.65), YAv. ham.pataiti (V 19.41), 3pl. 
Y Av. patonti (Yt 10.128 ff., V 13.42 £), impf. 3sg. YAv. 4... apatat (Yt 19.41, Yt 19.82), INJ. 3sg. YAv. 
patat (Yt 3.13, F 475), YAv. auua.patat (Yt 19.58), YAv. us.patat (Yt 19.57, Yt 19.60, Yt 19.63), SUBJ. 
2sg. ? Y Av. “frapatäi (Yt 19.50), 3pl. YAv. frapatanti (Yt 14.53, Yt 8.61), YAv. fra patan (V 5.12), OPT. 
3pl. YAv. pataiion (Yt 19.80), YAv. apataiion (Y 9.15), IMPV. 3pl. YAv. patontu (Y 10.1); Partic: pres. 
Y Av. patant- (Yt 15.50); Caus.: pres. SUBJ. 1sg. YAv. uspataiieni (Yt 19.44) 


*OLD PERSIAN: (+ *uz-) udpat- ‘to rise up, rebel’ = Kent: 194 

MED.; Pres. them.: impf. IND. 3sg. udapatatä <u-d-p-t-t-a> (DB 1.36, DB 1.38, DB 2.10, etc.), 
<u-d-p-t-t-a> (DB 2.14), <u-d-p-t-[t]-[a]> (DB 1.78) 

*MIDDLE PERSIAN: ВМР pt- /pad-/ ‘to fall’ || (+ *aua-) MMP ’wbys- ‘to fall off, 
BMP ’wpt- (NPLWN-) /öft-/ ‘to fall’ || (+ *а-) MMP ’bd’g ‘assailant (a kind of 
demon)’ || (+ *ni-) BMP npd- (SKBHWN-) /nibay-/ ‘to lie down, sleep’, MMP 
nb’st- (pret. stem), BMP np’s- /nibas-/ (caus.) ‘to lay, throw down’ || (+ *ham-) 
MMP hmbh- ‘to collapse, fall down’, MMP hmb’st- (pret. stem) ‘to fell, cast down, 
demolish’. Ф The -h- in MMP hmbh- is perhaps from the past participle: -h- < OP 
*-0- < Ir. -s-. = DMMPP: 65b, 9a, 239a, 178a 

Pres.: IND. 3sg. BMP ptyt /padéd/ ‘falls’; Partic.: perf. pass. BMP ptyt /padid/ || (+ *aua-) Pres.: IND. 
3sg. BMP ’wptyt /ofted/, 3pl. BMP "wptynd /oftend/; Partic.: perf. pass. MMP ’wbyst, BMP "wpstk 
/obastag/ || (+ *ni-) Partic.: perf. pass. BMP npst /nibast/, caus. MMP nb'st, BMP np'st /nibast/ || (+ 
*ham-) Pres.: SUBJ. 3pl. MMP hmbh’nd; Partic.: perf. pass. caus. MMP "hmb’st 


*PARTHIAN: (+ *аџа-) IPth. (Nisa) "wpst ‘fell down; poured out’ || (+ *fra-) frbd- ‘to 
fall down’, frb'd- (caus.) ‘to hurl down’ || (+ *ham-) ’mbd- ‘to collapse, fall down’ 


= Ghilain: 53 | DMMPP: 154b, 39a 
(+ *fra-) Pres.: IND. 3pl. frbdynd, SUBJ. 1sg. frbd’n; Partic.: perf. pass. frbst, Caus.: pres. SUBJ. 15р. 
frb’d’n || (+ *ham-) Pres.: IND. 3pl. "mbdynd; Partic.: perf. pass. ’mbst ‘it collapsed’ 


*KHOTANESE: OKh. pat- (pit-) ‘to fall’ || (+ *aua-) OKh. vavat- (vapat-) ‘to fall’ 
= SGS: 66, 120 

*SOGDIAN: (+ *aua-) BSogd. ’wpt, CSogd. ’wpt, MSogd. ’wpt ‘to fall’ || (+ *ni-) 
BSogd. ’npt ‘to fall’ || (+ *ham-) CSogd. ’mpt ‘to fall’ 

(+ *aua-) Pres.: IND. 3sg. CSogd. ’mptt, 3pl. CSogd. ’mptnt, IMPV. 2sg. CSogd. ’mpt; Impf.: IND. 3sg. 
BSogd. mnpt, MSogd. *m'pt (GMS: §633); Fut.: IND./OPT. 3sg. CSogd. трі || (+ *ni-) Pres.: IND. 3sg. 
BSogd. ’npt, BSogd. ’nptt, 3р1. BSogd. ’npt’nt, Partic.: perf. pass. BSogd. ’np’st 

*CHORESMIAN: (+ *aua-) wbd ‘to plunge into’, ? (LW) hwg- ‘to fall down; collapse’ 
|| (+ *para-) prpd- ‘to fall off || (+ *ni-) m/npd- ‘to fall down’, (caus.) m/np‘cy- ‘to 
tear down (of houses)’. ó The etymology of hwf- is uncertain. Samadi remarks that 
the forms are similar to Skt. subh- ‘to suffocate; to strike’ in appearance, whereas 
MacKenzie 1990: 112 cautiously suggests a connection with Oss. xawyn ‘to fall’. 
Both etymologies meet unsurmountable difficulties and are best to be discarded. 
Borrowing from (dial.) Persian seems to me the best solution to account for the 
Chor. forms: the initial h- may be considered "prothetic" or it may be identified as 
the (productive) preverb *fra-. For the Middle and New Persian development of 


*pau 301 


postvocalic РІг. *p > b, v (= B]) compare ВМР npstn, MMP nbyst-/nbys-, NP 
nibistan (rare), nivistan, nivés- (< *ni-p(a)is-). || Samadi: 211, 155, 130 

*NWIR: (+ *aua-) NP öftadan/uft-, (Judeo-Pers.) ’wBst- ‘to fall (down); to happen, 
vorfallen’, Bakht. vastan ‘to fall’, Sist. aft, aftid ‘to fall’, Isfah. oftän/ous-, Ham. 
dor-oftan/dor-ows- (inch.) ‘to sleep’, vor-osayán/vor-aws-, Isfah. ver-osän/ver-os- 
“to stand up’ 

*NEIR: (+ *uz-) Wa. z(a)bat-, z(o)bo0-/z(o)bon- ‘to snap (of boots)’ (= zübüt- ‘to 
burst, IFL II: 556) || (+ *ham-) Sh. ambi0- Rosh. ambé6-/Ambost, Sariq. 
imbis-/imbist, Yzgh. ambis-/ambust ‘to fall down, roll down, crumble’, Ishk. ambid- 
‘to fall down, be destroyed’, Wa. bə0-/bə0t, bot-/bon- ‘to fall; to throw off, down; to 
collapse (of wall)’ 

*MISC: (+ *ni-) Orm. nwastak ‘to lie down, go to sleep’ 

*SANSKRIT: pat ‘to fly, fall (down)’ (RV+) = EWAia П: 71 

9 In some instances it is rather difficult to distinguish this root from the formally and 
semantically similar root *pad. 

«PIE *pet(H,)- ‘to fall down, collapse; to fly?'. o On the possible presence of a
```


## [2026-09-14T01:00:28.440Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON helikopter ===\"; grep -n \"هلیکوپتر\\|هلی کوپتر\\|هليكوپتر\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10\necho \"=== ARY latin index pet ===\"; grep -n -i \"PET\\b\\|PETERE\\|PTERON\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Mo'in and Aryanpur"
}
```


### [2026-09-14T01:00:28.509Z] TOOL RESULT

```
=== MON helikopter ===
=== ARY latin index pet ===
49:I aba ST pap Obj LIF pa bas coolaals ASU yo carpet 9 CS pa ase
667:Nays Sly Glas 9 sins .y OLS Jad layup 9a) BN AD cde Ga pet oye cabs)
896:ea tle Ll Las (Min lee y palo ge tag I NOE y Crlpet
1205:Gm pet cael he ony yl 39 eles Gal pte cael tt sila ar oligy! clevsly
1211:By ol (Sa pl y2 1K gh ele bee pet OL 22) PNIW — sely ob shen (4? om
4458:Srp gt e Cosa g! "SUR 9 4) PAs *PATy *PET- gly) gta eal bats call
4995:POKORNY SSS~*~*~*~*~« PET CZECH) Soy
6513:PET (BRETON) 35.2
8140:p53 299 eaghy Ob ey} GUL; 52 oN) on! PET
9946:ISPET, SAFETH =—(BALUCHI) gr sh SPET, SPED (PAHLAVI) 15.34,
```


## [2026-09-14T01:00:29.700Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/helicopter",
 "prompt": "Give the full etymology of helicopter: French form, date, Greek elements, and any note on the segmentation helico-pter vs heli-copter."
}
```


### [2026-09-14T01:00:34.918Z] TOOL RESULT

```
# Etymology of Helicopter

**French Origin (1861):** The term derives from French *hélicoptère*, described as a "device for enabling airplanes to rise perpendicularly" or "flying machine propelled by screws."

**Greek Elements:** The word combines:
- Greek *helix* (genitive *helikos*) meaning "spiral"
- Greek *pteron* meaning "wing" (from the PIE root *\*pet-* meaning "to rush, to fly")

**Historical Note:** The original concept aimed to "gain lift from spiral aerofoils, and it didn't work." Early usage by Jules Verne and the Wright Brothers referred to theoretical flying machines. The terminology was "transferred to helicopters in the modern sense by 1918 when those began to be developed."

**Segmentation:** The source material indicates the primary segmentation as **helico-pter** (spiral-wing), reflecting the Greek *helix* + *pteron* composition, though the modern morphological parsing often treats it as **heli-copter** in contemporary usage.
```


## [2026-09-14T01:00:45.123Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 pet- ===\"; grep -n \"pet-\\|pet[eē]-\\|patati.*fliegt\\|accipiter\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20",
 "description": "Grep Walde-Pokorny Bd2 for pet-"
}
```


### [2026-09-14T01:00:45.184Z] TOOL RESULT

```
=== WLD Bd2 pet- ===
78:iduTcticav eig. ^geradaus stoBend oder aufsohlagend“) s. u. pet- „auf etwas 
1188:pet- (peta-) 
1203:1 . pet- (pete-) „ausbreiten, bes. die Arme“. 
1245:pet- 
1251:2. pet- (z. li.peia-ypetd-) „auf etwas los- oder niederstiirzen, fliegen, fallen‘s ; 
1252:dazu emrjn-St. nom. pet-r-‘(g)^ gen, pet-n-es „FlugeP^ (J. Schmidt 
1285:eig. „Wassersturz" (Wiedemanns BB. 27, 256 a 1 Wz. pet-^ pot- „flie6en, 
1314:pet- 
1375:pet- 
1404:zu haltender Scheidung von pet- ^fallen^^ und pet- ^fliegen^, s. dagegen 
2757:S. u. 'pet- „fiiegen“ am Schliisse. 
3346:eines solchen "^pter-sna aus dem r-St. ^peier in nreQv^ usw. (s. u, pet- „worauf 
4652:Tiregov beeinfluBt, auch gr. nxlXov „Peder, Plaumfeder“? (s. u. pet- „auf 
40809:Persson Beitr. 429, 954, wo gegen Verb. m. sternere, sowie u. pet- „auf 
41526:pet- „auf etwas losstiirzen*') ; sir amen „Streu“ ( : oTgd)pa ; ai. stdriman -) ; 
42515:licher Bed. *peisqo-; lat. pinna ist ^dhX^penna^ Q,pet- „fliegen^). 
43952:verkniipft; iiber lit, sparnas ,,Flugel*' usw. s. u. pet- ,,auf etwas losstiirzen,
```


## [2026-09-14T01:00:47.186Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC pet ===\"; grep -n \"^pet-\\|pet- (\\|petō\\|pet-ō\" IEC.txt | head -15\necho \"=== SYN fly/fall ===\"; grep -n \"petomai\\|Skt. pat-\\|pátati\" SYN.txt | head -15",
 "description": "Grep Mann and Buck"
}
```


### [2026-09-14T01:00:47.262Z] TOOL RESULT

```
=== IEC pet ===
12796:pet- (1) (radical: “fly, dash'. Cf. peto, etc.). WP II, 20 . Skt. patah, m. “flight, fall; cf. patasah, m. ‘bird’; Oss. cf. fat, s. *arrow'; Gk. pésos, gs: -eos, n. ‘fall’; cf. más-peta “first leaves of ben- zoin'; pro-petés, adj. “tilted forward, head- strong"; Lat. cf. per-petis, adj. ‘continual’; peti- men, n. “breast of animal; disease of the shoulder’; MIr. eite, ite, f. “wing, feather; W ed, m. ‘velocity, aptitude’; OCor. hëd, Cor. hes, pl. hezow (w. ‘false’ h-), f. “flight, swarm’; Br. héd, pl. hedu, m. id.; OHG cf. féd-dah, m. (^wing, fr. *ped-tok-); Li. petis, gs: -iés, m. ^shoulder-blade, shoulder’
12797:pet- (2) (variant: pot-, radical: ‘extend, ex- pand’) Per. cf. (?) padīd, adj. ‘evident, clear’; Gk. cf. petánnümi, petázo, v. “spread”, beside pítno, id. and pétalos, adj. 'spread-out, flat; Lat. cf. (r-gde) pateo, ere, v. “lie open’; Olr. ed, s. ‘space’; Arm. cf. -at- in h-atanem, v. ‘plane’; z-at, adv. ('open'; px. 'apart); z-atanem, aor. z-ati, v. “separate? (r-gde fr. *pot-)
13426:pot-, (2) o-gde radical of type pet- (1) “fly, fall Gk. cf. potáomai, v. “fly, hover’; poté, f. (1) flight’ beside pótema, n. id.; potaánós, adj. ‘winged’; Li. pátinas, m. ‘winged creature"
13565:prom-, prom-, próm- (promi-) — pro-pet- (pro-pət-)
13580:pro-pet- (pro-pət-) ‘lurching, lunging, for- ward, headlong’. Cf. pro-, pet- Skt. cf. pra-pitvám, n. ‘flight’; Av. frapatō, m. ‘rush, dash’; Gk. pro-petës, adj. ‘hurtling, hasty’; Alb. përpjetë, adv. ‘steep, upward'.
13709:ptā-, extended z-gde of type pet- (2), peto, q. v. Cf. WP II, 19 Per. cf. futadan, inf. ‘fal’; Gk. cf. ptémai, v. ‘flake down, fall”; cf. ptenós, (Doric: -à-), adj. ‘winged’; ptená, npl. ‘birdlife’
15471:skapet- (skapt-) ‘cut, cutting; cut-out, thing cut, shape’. Cf. skapt- Gk. skápetos, m. “ditch, trench’; OE sceafoóa, wm. ‘chip, shaving’; OCS cf. skopíci, m. "eu. nuch’. See next
16824:spet- (?) Lat. cf. so-spes, -spitis, Fest. si-spes, adj. («healthgiving; wholesome, safe, whole’, if fr. *sye-^); Li. cf. spetas, m. ‘leisure’ beside spéti- nas, adj. fpresumable'; spétinai, adv. 'sup- posedly'; Latv. cf. spēt, inf. "be capable’. Semantics obscure, cf. sphéetós & WP IL, 657
=== SYN fly/fall ===
1393:4. Grk. rorapss (NG POp. wordt), fr. root of rimrw ‘fall’, réropat ‘fly’, Skt. pat- ‘fly, fall’, etc. That is, Torayés was at first the ‘falling, plunging, rushing’ stream. Walde-P. 2.19. Persson, Bei- trige 654. Kretschmer, Glotta 27,248 f.
16930:7. Skt. pad-, above, 6. Skt. pat-, Av. pat-, above, 1.
19383:Lat. petere, orig. ‘direct oneself toward, attack, fall upon’ then in weakened sense ‘seek’ (and later ‘ask’) : Grk. zérouat ‘fly’, mirrw ‘fall’, Skt. pat- ‘fly, fall’, etc. (10.23, 10.37). Walde-P. 2.19f. Er-
31976:3 Lat. petere (> Sp., Port. pedir), orig. (‘fly at’) ‘assail, attack’, hence geek’ and ‘ask, request’ : Grk. qérouac ‘fly’, Skt. pat- ‘fly, fall’, ete. Walde-P. 1.20, Ernout-M. 763 f.
```


## [2026-09-14T01:00:57.799Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1245,1300p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt",
 "description": "Print Walde-Pokorny pet- entry"
}
```


### [2026-09-14T01:00:57.857Z] TOOL RESULT

```
pet- 


19 


2. pet- (z. li.peia-ypetd-) „auf etwas los- oder niederstiirzen, fliegen, fallen‘s ; 
dazu emrjn-St. nom. pet-r-‘(g)^ gen, pet-n-es „FlugeP^ (J. Schmidt 
PI. 174f., Johansson Beitr. 1, BB. 18, 12, Pedersen KZ. 32, 245, zu 
den ^-Formen auch Brugmann IP 1, 508, 510). 

Ai. pdtati „fliegt, senkt sich, fallt, gerat in etwas“ {—nkopai, lat. peto, 
acymr. hedant^ Aor. apaptat; set-Formen Fut. patisyati, pf. paptima, sup. 
pdtitum, ptc. paiiid-\ patdyati „fliegt“ (= gr. noTeopai)^ patdyati „laBt 
fliegen, schleudert, lafit fallen" (dehnstufig wie m. „Flug, Fall, Sturz", 

gr. Jicordopai^ ir. aith)^ pra-pat- ,,hineilen, stiirzen", pdtman- n. „Flug, 
Pfad, Bahn" (: jiSrpog, Jiorajuog); av. pataiti „fliegt, eilt", ap. iid-apatata 
„erhob sich", ao. patayeiti „fliegt", acapastdis inf. „hinahzufallen", paiti- 
pasti- f. „Entgegengehn, -treten", (= ai. ati-patti- „das Verstreichen"), von 
einem i^-Prs. „fortfliegend (vom Pfeil)"; set-Form ao. tata- 

i^ptatd-)^ „fallend (vom Regen)" (Bthl. IF. 10, 196, Wb. 646: gr. mcorog). 

Gr. Tikopat „fliege" {ejiro/uirjv; set-Formen enjaxo „entflog", nxag^ ejixyv, 
dor, ejirdv, fut. jtrgoopat)^ (bxvnexrjg „schnell fliegen d", Jtexerjvog stereo^ 
dv6g)j jiexsivog {^Tzereovog) „geflugelt, fliigge", Tioxij „Flug", nordvog, 7]v6g 
„zum Fliegen be^higt, befliigelt, fliegend", Tzoxdopai (und TioxkpLaij s. o.) 
„flattre", nwxdopai ds., Tzrfjotg, bei Suidas Tzxyjua „Flug", jirrjvog, dor. 
jirdvog ^fliegend"; mit der Bed. ^fallen" tu-ttvco (fur nach ^iJircOy 

Brugmann Festgabe f. Kaegi 37) „falle" (Fut. jon. Tzeoiojuai aus ^nereopai, 
att. TiBoovpatf darnach Aor; att. bjzegov gegenuber dor. lesb. I'tzbxov; Pf. 
7t€JZT(oxa, 0 ) Pf. Ablaut wohl znp[e\t€-^ Meillet Msl. 1 3, 44, Brgm.-Thumb GrGr.^ 
373 kann zu einem '^petd nach Persson Beitr. 654 f., neTixychg (s. dazu auch 
Brgm.-Thumb 330a 1), att. Ttenjchg aus ^7iBnxd(bg\ dnxcog (Pind.), aTxxrjg 
(dor. inschr.) „nicht fallend^ nicht dem Falle ausgesetzt". mxvia) „falle", 
Evnenqg „bequem, gunstig", jiQOTiexgg „vorwarts fallend, geneigt (s. alb. 
perpjete „abschussig, steil", G. Meyer Wb. 333), Tteoog n. (gen. TtiaEog aus 
"^TiixEog) „cadaver", nkpog „Los, Schicksal, bes. trauriges", noxapog „Flu6", 
eig. „Wassersturz" (Wiedemanns BB. 27, 256 a 1 Wz. pet-^ pot- „flie6en, 
na6" gibt es nicht); nxddpay Tixcdoig „Fall" (: tzetixcoxci). 

Mit der Bed.-lurbung des lat. peicre gr. mxvXog „heftige Bewegung" 
(; petulans', z. B. Boisacq s. v., wo eine unannehmbare Alternative; 
vgl. auch EpTiEGElv „impetum facere"). 

Endlich hat die schwere Basis Txxd- : Jixco- : Ttxa auch die wohl aus „nieder- 
stiirzen" entw. Bed. ^sich niederducken" und „verzagt, in Furcht sein": 
HQxajixijxfjv ,,(die Pferde) scheuten", nETixt^cog „geduckt", nxvia „Scheu, 
Schrecken" (^jrrcoym, vgl. Arfcdo IJxqSay AtioXXcov ITtmog; s. noch u. pou- 
„sich angstigen"), jzxo{i)£iv „erschrecken, in Bestiirzung und seelischen 
Aufruhr versetzen". pass. „von Schrecken, Aufregung ergriffen werden" 
(imoaoEv Sappho, EJixod^rjg Eu.); mit gutt. Erw. tix'^ggco C^Ttxdx-icd) „ducke 
mich" (aor. €jm]^a^ dor. Enxdy.a auch trans. „er8chrecken" ; xaxaTixaxcov), 
jxxcoGxdCco „ducke mich furchtsam oder fliehe", jrtcoooco (^mcboxm) „ducke
```


## [2026-09-14T01:01:21.138Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 43 (p.22) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==43' HRN.txt | head -50",
 "description": "Horn p.22"
}
```


### [2026-09-14T01:01:23.048Z] TOOL RESULT

```
=== HRN leaf 43 (p.22) ===
- 21 —
85. U8tu%än, geschrieben ustux^än *Knochen, Kern'.
phlv. aslux^dn (AV.); zu aw. ast- 'Knochen', s. est
(No. 81).
Die merkwürdige Form findet sich als LW. im
Kurdischen, in den Pämirdialekten (sar. ust/än, wa/.
usta/än und wohl auch Uyn, sit/än) u. ö.
86. ester ^Maulesel'.
phlv. astar; ai. agvatard- 'Maulesel'.
kurd. istir, histir; bei. istal, n. hastal (438).
87. iiStur *Kameer, sutur.
aw. ustra- 'Kameel'; phlv. ustrlastän (vd. 15, 68);
ai. üstra-,
kurd. LW. (?) hustur^ sutur; bei. hustar etc. (161);
wa/. ü^tür^ siyn. stur, sar. xtiir, LW.(?).
88. eSk *Thräne .
g. sah,
aw. *asraka (vergl. skr. dgra-), *arsaka (Hörn, Indog.
Forsch., II, 136).
afy. ö^a resp. ö/a; wsl/, ya^k, sar. yujck,
Vergl. ers (No. 69).
89. iiSnän Name einer zum Waschen gebrauchten Pflanze,
Herba Alkali (AM. 28; 37 Zeile 2), sunan (DWlfi'IN,
Jer. 2, 22).
arm. LW. ausnan 'Seifenkraut*,
aw. "^aiwis'hnana- (\)^) (de Lagarde, Fers. Stud., 74).
Zu aiwis vergl. indessen unter bes-, bis- (No. 221).
90. eSnOse, isnöse 'das Niesen', senöse, sinöse, sinöse-).
germ. Vhnus bezw. /wws, vergl. ahd. niosan^ mhd.
') Die Awestaform ist von de Lagarde falsch angesetzt, der
die Lautverhältnisse verkennt.
V V
*) FR und FJ haben die folgenden Belege (nur FJ constatirt
einen Majhülvokal): (Metr. Hezej)
deniäyl pisk'l ö esnösc'l ter
cü äred gös^ gerdünrä küned her
Abu'l Xeir.
(Metr. Hezej):
merä imröz^ tobe süd^ däred
ciinänci derd-i dendänrä senöse
Rüdegl.
```


## [2026-09-14T01:01:23.910Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ns=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nlines=s.split('\\n')\nfor i,l in enumerate(lines):\n    if 'PET' in l and i>4400 and i<4520:\n        print(i,l)\n# find page tag near 4458\nfor j in range(4458,4300,-1):\n    if '[pdf page' in lines[j]:\n        print('PAGE TAG:',j,lines[j]); break\nprint('---- context ----')\nprint('\\n'.join(lines[4448:4475]))\nEOF",
 "description": "Aryanpur PET entry context"
}
```


### [2026-09-14T01:01:25.055Z] TOOL RESULT

```
4457 Srp gt e Cosa g! "SUR 9 4) PAs *PATy *PET- gly) gta eal bats call
4478 PEKO s(BULGARIAN) pS 5 shih, PETTEIN, PESSEIN, PEPSIS
PAGE TAG: 4458 [pdf page 156]
---- context ----
BARNHART: (FOODER) 396 PASCERE, PASCO ALATIN) 3
MACKENZIE: 62, (WATCH) 139 FODR (alt (GOTHIC) SF
ONIONS: (FODDER) 366 (4!) (OLD HIGH GERMAN) op git
SKEAT: (FODDER) 220 FOTAR
TRAUPMAN: 297 FUTTER (4ul2}(GERMAN) glalT
AMINDAROY: (GUARD) 232 (4l4}(OLD ENGLISH) aS pSS\
ver igbt day FODOR
FODDER — (4,12 }(ENGLISH) 5 J&i
lewtloal
Srp gt e Cosa g! "SUR 9 4) PAs *PATy *PET- gly) gta eal bats call
[pdf page 156]
7 a"
YOV | ody oy .
ail T 4h aly oy! JFUTTERN (SUIT oj!) y FEED, FOOD ii Gla jly) 2513
SUS et ol GV 9 gay} Slaejly geet
Ay ae Sight Frees ol lin Sly ae?
| (OLD HIGH GERMAN) 48 gal PAC, PACHTL —{AVESTAN) .o\xy!
CHOH, KOCH, KOCHON (OLD PERSIAN) dsl, go
KOCH, KOCHEN (GERMAN) ll PECTIS, PAKTAR’- :
(a2 MOLD ENGLISH) oS dS PUXTAN PAHLAVI) 5 shy
coc FICUN, FICHIN. §——(OSSETIC) aus!
cook ENGLISH) glS3\ PATIN (KURDISH) «52,5
KOGE DANISH) J lasls PASHAG, PACAG — :(BALUCHI) «>
KOCK A (SWEDISH) ($45 y« PAXAVUL AFGHANI) (4) glail
KOK DUTCH) «sacle PAK s(TOKHARIAN A) A 5,5
(OLD CHURCH SLAVIC) 95 53% PAK :(TOKHARIAN B) B (5 os
PEKA SANSKRIT) cy Sails
```


## [2026-09-14T01:01:31.161Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 44 (p.22) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==44' HRN.txt | head -60",
 "description": "Horn p.22"
}
```


### [2026-09-14T01:01:32.255Z] TOOL RESULT

```
=== HRN leaf 44 (p.22) ===
- 22
niesen, an. hnjosa, mittelengl. fnesen niesen', ver-
schieden von mittelengl. snesan, engl, to snee:se
(Kluge, Etymolog. Wörterbuch).
kurd. heenlsum *ich niese' (Justi, No. 66, wo auch
die Etymologie).
Die neupersische Grundform müsste *senöse sein.
91. ef-, ew-, Praefix, ß-, fu-,
ap. abiij 'herzu'; aw. aihi, aiwi *herzu, oben' etc.;
phlv. a/-, päz. awa-; ai. abhi 'herzu, oben' etc.
92. uftäden ^fallen', Praes. uft-em, fitaden, uftädegt
(Sa dl, Bostän 4, 1 Graf).
aüa-\- [/^pat'\ phlv. öftätan, öftet (vd. 6, (73) Gl.,
16, (20) Gl.), öftad (vd. 19, 94), oft falle (Göät-I Fr.),
vergl. öfttnltan, äwäZ'öft(i)smh (vd. 16 (64) Gl.),
öft(i)sn (Ys. 43, 4, aw. avapasti-) ^).
Im Neupersischen findet sich bei Dichtern noch
öf laden (die Aussprache mit ö ist allerdings nicht
bezeugt), z. B. Vis und Rämin, S. 61, Vers 5 v. u..
Sahn. I, 88, Vers 494, Sa di, Gul. (Sprenger), 38 Zeile 9.
93. efräiten 'erheben', efrästen, Praes. efräz-em, ewrästen,
ewraz (AM.), ini^N^DN (jüd.-pers.).
phlv. afrästan {afrä/tan zu lesen?) erheben.
Zu [/reg- + ahhi richten, aufrichten'; ai. irajydti
er richtet'; gr. oQfyw^ oQsyvv/Lu Vecke'; lat. rego richte';
got. uf-rakjan 'in die Höhe recken'.
wa;^. püt\rüzam, sar. pat\räzam 'sich recken, gerade
stehen'.
So viel ich sehe, ist die nahe liegende Etymologie
vor KZ. 32, 579 No. 4 noch nicht ausgesprochen
worden.
(Wohl die ersten zwei Misrä^'s eines Rubä*l)
cHn sepled ez m^y-l mü*ambär-t ^öse
göyed k*ekimn nemänd^ jäi/'i senöse
Minöcihrl.
*) Bevorzugter ist im Pehlevl öpa^tan.
```


## [2026-09-14T01:01:32.756Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"افتادن\\|اوفتادن\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY پست ===\"; grep -n \"پست \" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Aryanpur Persian index"
}
```


### [2026-09-14T01:01:32.819Z] TOOL RESULT

```
80:علت از رونق افتادن واژه‌های «آریا» و «آرین» و (آریایی» چه بود؟
5698:چم این واژه در سانسکریت و لیترانی و لثرنی و یونانی : لرزیدن» به لرزه افتادن
=== ARY پست ===
134:پست شدن نژادی و تیرگی نسبی رگ مو و چشم آنها شد. موضوع پرتری‌های نژادی (که امروزه
```


## [2026-09-14T01:01:45.566Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%B4%DA%A9/",
 "prompt": "Does any dictionary section (دهخدا، معین، عمید، برهان قاطع) define کشک as a bird (مرغ/پرنده/عقعق/کشکرک)? Quote the relevant definitions exactly."
}
```


## [2026-09-14T01:01:48.339Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%87%D9%84%DB%8C%DA%A9%D9%88%D9%BE%D8%AA%D8%B1/",
 "prompt": "What do the Persian dictionaries (فرهنگ معین، دهخدا، عمید) say about هلیکوپتر — its definition and stated language of origin (فر. = French, or English)? Quote exactly."
}
```


### [2026-09-14T01:01:51.160Z] TOOL RESULT

```
# Dictionary Definitions of کشک as Bird

Based on the dictionary sections provided, **none of the main four dictionaries (دهخدا، معین، عمید، برهان قاطع) define کشک as a bird**.

The definitions in these sections consistently refer to کشک as a dairy product:

- **دهخدا**: "دوغ خشک کرده" (dried whey)
- **معین**: "تَه ماندة ماست یا دوغ که پس از جوشاندن خشک کنند" (dried yogurt/whey residue)
- **عمید**: "ماده ای جامد یا مایع از انواع لبنیات" (solid or liquid dairy product)

The bird definition appears only in the user suggestions section ("پیشنهاد کاربران"), where contributors note: "کشک = زاغی/ کشکرک/swift flying پرنده ای سیاه" (a black swift bird), citing etymological dictionaries but not the four standard dictionaries listed.
```


### [2026-09-14T01:01:53.920Z] TOOL RESULT

```
Based on the Persian dictionaries shown:

**Dehkhoda Dictionary** states: "قسمی هواپیمای کوچک که به هنگام برخاستن از زمین و نشستن بر آن میتواند به حالت عمودی حرکت کند" (a small aircraft that can move vertically during takeoff and landing). Origin marked as French (فرانسوی).

**Farhang-e Mo'in** defines it as: "نوعی وسیلة ترابری هوایی که در هنگام فراز و فرود می تواند به طور قایم یا عمودی حرکت کند" (a type of aerial vehicle capable of vertical movement during ascent and descent). Origin marked as French (فر.).

**Farhang-e Amid** describes: "وسیلۀ نقلیۀ هوایی کوچک که هنگام بالا رفتن و فرود آمدن می تواند عمودی حرکت کند" (a small aerial vehicle capable of vertical movement during takeoff and landing). No origin explicitly stated in this entry.

All three identify it as a French loanword, emphasizing vertical flight capability as the defining characteristic.
```


## [2026-09-14T01:02:02.945Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peth₂-\" \\\n \"https://en.wiktionary.org/wiki/افتادن\" \\\n \"https://en.wiktionary.org/wiki/پست\" \\\n \"https://www.etymonline.com/word/helicopter\" \\\n \"https://abadis.ir/fatofa/کشک/\" \\\n \"https://abadis.ir/fatofa/هلیکوپتر/\" ; do\n  timeout 180 python3 tools/fetch_source.py \"$u\" --note \"page 400, root Pet 1 (PIE *pet- fly/fall): root, oftadan, past, helicopter, kasak\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:02:08.832Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4d6fa6a730dc079b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c737378475aa2481.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9012e26b0e491149.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d1972850f3916184.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cc68f301e71a19e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c9f175587bf7dbd0.txt
```


## [2026-09-14T01:02:36.521Z] TOOL CALL #65: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg400.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/400.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-14T01:02:36.615Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-14T01:13:19.400Z] TOOL CALL #66: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-400.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peth₂-\"\nW_OFT  = \"https://en.wiktionary.org/wiki/افتادن\"\nW_PAST = \"https://en.wiktionary.org/wiki/پست\"\nETYH   = \"https://www.etymonline.com/word/helicopter\"\nAB_K   = \"https://abadis.ir/fatofa/کشک/\"\nAB_H   = \"https://abadis.ir/fatofa/هلیکوپتر/\"\n\nnodes = []\ndef N(**kw):\n    nodes.append(kw)\n\nN(id=1, lang=\"Avestan / Old Persian\", words=\"ptâta, tâta; ava-pat\",\n  verdict=\"confirmed\",\n  derivation=\"Both words are genuine and both belong to PIE *pet(h₂)- 'to fly, to fall'. Avestan tata- (Yt. 8, of rain) is the seţ-participle *ptata- 'falling', i.e. the zero-grade participle of pat- with the initial p- surviving only in the reconstructed form; Pokorny prints it exactly as Nourai does: \\\"Avestan tata- (*ptata-), 'fallend (of rain)'\\\" and compares Greek πτωτός. ava-pat- is the same verb with the preverb ava- 'down, away' (Av. ava.pastōiš inf. 'hinabzufallen', Y. 44.4); Cheung (EDIV 299–301) lists Y.Av. pat- 'to fly' || (+ *aua-) 'to fall down, off'. There is no Old Persian *ptata-/ava-pat- attested, so the double language label 'Avestan / Old Persian' is loose (Old Persian has only ud-pat-, node 8–9); the words themselves are Avestan.\",\n  derivation_fa=\"هر دو صورت از ریشهٔ هندواروپایی آغازین *pet(h₂)- «پریدن، افتادن» است. اوستایی tata- (در وصف باران) همان صفت مفعولی صفردرجهٔ *ptata- «فروافتاده» است که پوکورنی (ص ۸۲۵) دقیقاً به همین شکل آورده است؛ ava-pat- نیز همین فعل با پیشوند ava- «فرو، پایین» است (مصدر اوستایی ava.pastōiš). تنها ایراد این است که برچسب «پارسی باستان» درست نیست؛ این دو صورت صرفاً اوستایی‌اند. روی هم رفته ادعای نورایی درست است.\",\n  sources=[W_PIE, W_OFT],\n  ref_check=[\n    {\"ref\":\"POK:825\",\"status\":\"supports\",\"note\":\"Pokorny IEW pet-2 (pp.825-826): 'Avestan pataiti „fliegt, eilt“, ap. ud-apatata „erhob sich“, ... ava-pastōiš inf. „hinabzufallen“ ... Avestan tata- (*ptata-) „fallend (vom Regen)“' — grep 'Page(s): 825-826' in POK_full.txt.\"},\n    {\"ref\":\"HRN:22\",\"status\":\"supports\",\"note\":\"Horn, Grundriss p.22 no.92 s.v. uftāden: 'aυa- + √pat; phlv. ōftātan, ōftēt ... ōft(i)šn (Ys. 43,4, aw. avapasti-)' — leaf 44 of HRN.txt.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"col. ~840 s.v. pat-\",\"stance\":\"supports\",\"note\":\"Bartholomae AiW: 'P. pat- V. „fliegen; fallen“ ... Praes. pata-, ipta-, ta- ... Inf. pastōiš, patai ... [Vgl. noch tata-]' (BRT.txt line 14852).\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV pp. 299-301 s.v. *pat\",\"stance\":\"supports\",\"note\":\"'*pat ‘to fly, rise; (?) fall’ ... Y Av. pat- ‘to fly’ || (+ *aua-) ‘to fall down, off’'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p.19 (2. pet-)\",\"stance\":\"supports\",\"note\":\"Walde-Pokorny II 19: 'av. pataiti „fliegt, eilt“, ap. ud-apatata ... aυapastōis inf. „hinabzufallen“ ... av. tata- (*ptata-) „fallend (vom Regen)“'.\"}])\n\nN(id=2, lang=\"Pahlavi\", words=\"oftâtan\",\n  verdict=\"confirmed\",\n  derivation=\"Middle Persian ōftādan / ōft- 'to fall' < Old Iranian *ava-pat-: the preverb *ava- contracted with the following labial to ō- (as in ōstan, ōzŋdēn), Old Iranian intervocalic -p- was preserved before the -t- of the root so that *ava-pat-tan gave ōft-. MacKenzie prints '*ōftādan, ōft- [ʾWPT- | M ʾWPTʾD, N uft-] fall' beside the older 'ōbastan, *ōbad- [NPLWN-stnʹ < Aram. npl; ʾWPSTNʹ]', i.e. ōbastan is the earlier Book-Pahlavi verb and ōftādan the younger formation that New Persian continues. Horn p.22 gives exactly Nourai's form: 'phlv. ōftātan'.\",\n  derivation_fa=\"فارسی میانهٔ ōftādan / ōft- «افتادن» از ایرانی باستان *ava-pat- است: پیشوند *ava- با لبی پس از خود به ō- بدل شده و پ ایرانی باستان پیش از t محفوظ مانده و ōft- داده است. مکنزی صورت‌های ōbastan (کهن‌تر) و ōftādan را کنار هم آورده و هرن (ص ۲۲) دقیقاً همین صورت «ōftātan» را می‌آورد. ادعای نورایی درست است.\",\n  sources=[W_OFT],\n  ref_check=[{\"ref\":\"BQT:145\",\"status\":\"partial\",\"note\":\"Borhan-e Qate' (Mo'in ed.) p.145 = BQT_v1_pages.txt leaf 361 carries the headwords 'افتاد ... افتادگان ... افتاده', but no Pahlavi etymology footnote is legible in the OCR of that leaf; the Pahlavi form ōftātan Nourai prints is Horn's (HRN:22), not Borhan's.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie p.60 s.v. ōbastan / *ōftādan\",\"stance\":\"supports\",\"note\":\"'ōbastan, *ōbad- [NPLWN-stnʹ < A npl; ʾWPSTNʹ, ʾWPT-] fall. *ōftādan, ōft- [ʾWPT- | M ʾWPTʾD, N uft-] fall.' (PHD.txt line 518).\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV p.300\",\"stance\":\"supports\",\"note\":\"'*MIDDLE PERSIAN: ... (+ *aua-) MMP ʾWBYS-, BMP ʾWPT- (NPLWN-) /ōft-/ ‘to fall’'.\"},\n    {\"src\":\"HRN\",\"where\":\"p.22 no.92\",\"stance\":\"supports\",\"note\":\"'phlv. ōftātan, ōftēt (vd. 6 (73) Gl., 16 (20) Gl.), ōftad (vd. 19, 94)'; footnote: 'Bevorzugter ist im Pehlevī ōpastan.'\"},\n    {\"src\":\"NYB\",\"where\":\"Manual II, glossary\",\"stance\":\"silent\",\"note\":\"grep for 'ōbast|obast' in NYB_vol2_glossary.txt returns only bayōbaxta-; the verb is not in the Nyberg glossary excerpt on disk.\"}])\n\nN(id=3, lang=\"Persian\", words=\"oftâdan «افتادن»\",\n  verdict=\"confirmed\",\n  derivation=\"New Persian افتادن oftādan / uftādan, present stem uft-, continues Middle Persian ōftādan without change beyond the regular MP ō > NP o/u in the pretonic syllable; the classical poets still scan ōftādan (Vīs u Rāmīn, Šāhnāma, Sa‘dī, per Horn p.22). Wiktionary, citing Cheung 2007:301, gives the same chain: NP uftādan < MP ōft- < Proto-Iranian *ava- + *pat- < PIE *peth₂-. Mann (IEC s.v. ptā-) likewise cites 'Per. futadan, inf. ‘fall’' under the zero-grade of pet-.\",\n  derivation_fa=\"«افتادن» از فارسی میانهٔ ōftādan (ستاک حال: ōft-) و آن از *ava-pat- ایرانی باستان است. ō کشیدهٔ فارسی میانه در فارسی نو به o/u بدل شده و در شعر کهن (ویس و رامین، شاهنامه، سعدی) هنوز اوفتادن خوانده می‌شده است (هرن، ص ۲۲). چونگ و ویکی‌واژه همین زنجیره را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n  sources=[W_OFT, W_PIE],\n  ref_check=[{\"ref\":\"BQT:145\",\"status\":\"partial\",\"note\":\"BQT_v1_pages.txt leaf 361 (≈ printed p.145): 'افتاد بفتح اول بروزن استاد ... افتادگان ... افتاده بمعنی عاجز و سقط و خراب' — the word is there with its Persian sense, but the derivation from Pahlavi is not stated on that page.\"}],\n  consulted=[\n    {\"src\":\"HRN\",\"where\":\"p.22 no.92\",\"stance\":\"supports\",\"note\":\"'92. uftāden ‘fallen’, Praes. uft-em, ftaden, uftādegī (Sa‘dī, Bostān 4,1) — aυa- + √pat'.\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV p.301 (*NWIR)\",\"stance\":\"supports\",\"note\":\"'(+ *aua-) NP ōftādan/uft-, (Judeo-Pers.) ʾWBST- ‘to fall (down); to happen’'.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann s.v. ptā-\",\"stance\":\"supports\",\"note\":\"'ptā-, extended z-gde of type pet- (2) ... Per. cf. futadan, inf. ‘fall’'.\"},\n    {\"src\":\"BQT\",\"where\":\"vol.1 p.145 (leaf 361)\",\"stance\":\"partial\",\"note\":\"headwords افتاد / افتادگان / افتاده present, no etymological footnote.\"}])\n\nN(id=4, lang=\"Avestan\", words=\"patta\",\n  verdict=\"plausible\",\n  derivation=\"The etymology is Hübschmann's and Nourai reproduces it correctly, but the form is a reconstruction, not an attested Avestan word. Hübschmann, Persische Studien p.41 no.316, says verbatim: 'Np. past „niedrig, gering“ ist nicht = skr. upasti-, das zu *bast geworden wäre, sondern = *patta-, skr. patita-' — i.e. the pre-form is the past participle *pat-ta- of the root pat- 'fall', matching Sanskrit patitá-. In actual Avestan the -tt- cluster is already resolved to -st- (Av. ava.pasta-, pastōiš), so a spelling 'patta' can only be a reconstructed Proto-Iranian *pat-ta-; labelling the box 'Avestan' is therefore too strong. The chart's own NOTE that HRN:70 derives past from a different root is accurate (see node 5).\",\n  derivation_fa=\"ریشه‌شناسی از آنِ هوبشمان است و نورایی آن را درست نقل کرده، امّا صورت *patta- واژه‌ای اوستایی مضبوط نیست بلکه بازساخته است: صفت مفعولی *pat-ta- از ریشهٔ pat- «افتادن»، هم‌ارز با سنسکریت patitá-. در اوستایی خوشهٔ -tt- پیشاپیش به -st- بدل شده (ava.pasta-)؛ پس برچسب «اوستایی» برای این خانه دقیق نیست. با احتیاط پذیرفتنی است.\",\n  sources=[W_PAST, W_PIE],\n  ref_check=[\n    {\"ref\":\"HUB:41\",\"status\":\"supports\",\"note\":\"Hübschmann, Persische Studien p.41 no.316 (HUB.txt leaf 52): 'Np. past „niedrig, gering“ ist nicht = skr. upasti-, das zu *bast geworden wäre, sondern = *patta-, skr. patita-. Vgl. oben Nr. 92.' — exactly Nourai's arrow.\"},\n    {\"ref\":\"AEF:382\",\"status\":\"not_checked\",\"note\":\"Khaleqi Motlaq's Persian version of Horn (Asās-e Ešteqāq-e Fārsi) is not online and not on disk (refs_online.json: 'Not online').\"}],\n  consulted=[\n    {\"src\":\"HRN\",\"where\":\"p.70 no.316\",\"stance\":\"contradicts\",\"note\":\"Horn: 'pest ‘niedrig’ — ai. vergl. upastha, upasti- „Untergebener“. Bartholomae (briefliche Mitteilung)' — i.e. from *upa-sthā-, the 'different root' the chart's NOTE mentions.\"},\n    {\"src\":\"BRT\",\"where\":\"AiW s.v. pat-\",\"stance\":\"partial\",\"note\":\"Bartholomae lists the participle only as the -st- form (ava.pasta-, pastōiš); no Avestan lemma 'patta-'.\"},\n    {\"src\":\"POK\",\"where\":\"IEW 825-826\",\"stance\":\"partial\",\"note\":\"Pokorny gives Skt. participle patita- but no Iranian *patta-.\"}])\n\nN(id=5, lang=\"Persian\", words=\"past 1 «پَست ۱»\",\n  verdict=\"plausible\",\n  derivation=\"Persian پست past 'low, base' goes back to Middle Persian past 'low' (MacKenzie: 'past [pstʹ | N ...] low; astr. dejection'), and Hübschmann's derivation from *pat-ta- 'fallen' (Proto-Iranian *pasta- by the regular Iranian change *-tt- > -st-) is phonologically impeccable and semantically parallel to Sanskrit patitá- 'fallen, low' (node 21) and to English 'fallen' in the moral sense. It is not, however, universally accepted: Horn p.70 (on Bartholomae's advice) compared Sanskrit upasti- 'subordinate' (*upa-sthā-), and Wiktionary offers no Iranian etymology at all, only a comparison with Armenian pstik. Because two nineteenth-century authorities disagree and no modern handbook settles it, 'plausible' rather than 'confirmed'.\",\n  derivation_fa=\"«پست» از فارسی میانهٔ past «نگون، فرود» (مکنزی) است. هوبشمان آن را از *pat-ta- «افتاده» می‌گیرد؛ خوشهٔ *-tt- ایرانی به -st- بدل می‌شود (*pasta- > past) و از حیث معنا دقیقاً موازی سنسکریت patitá- «افتاده، فرود» است. در مقابل، هرن (ص ۷۰) به راهنمایی بارتولومه آن را با upasti- سنسکریت (از *upa-sthā-) سنجیده است. از آنجا که مرجعی امروزین این اختلاف را فیصله نداده، ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[W_PAST],\n  ref_check=[{\"ref\":\"AEF:382\",\"status\":\"not_checked\",\"note\":\"Asās-e Ešteqāq-e Fārsi (the Persian edition of Horn+Hübschmann) is print-only; refs_online.json records it as not available. Its content for this item is Hübschmann no.316, which was checked directly (HUB:41).\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie p.66 s.v. past\",\"stance\":\"supports\",\"note\":\"'past [pstʹ | N .......] low; astr. dejection.' (PHD_mackenzie.txt line 4102) — the Middle Persian link the chart omits.\"},\n    {\"src\":\"HUB\",\"where\":\"p.41 no.316\",\"stance\":\"supports\",\"note\":\"'... sondern = *patta-, skr. patita-'.\"},\n    {\"src\":\"HRN\",\"where\":\"p.70 no.316\",\"stance\":\"contradicts\",\"note\":\"'pest ‘niedrig’ ... ai. vergl. upastha, upasti- „Untergebener“'.\"},\n    {\"src\":\"MON\",\"where\":\"vajehyab/abadis\",\"stance\":\"silent\",\"note\":\"not consulted online for this item; MON_part1/2 on disk contain no پست etymology note.\"}])\n\nN(id=6, lang=\"Avestan\", words=\"pataiti, patayeiti; patareta\",\n  verdict=\"confirmed\",\n  derivation=\"Avestan pataiti '(he) flies, hurries' is the thematic 3sg. present of pat- (Yt 8.61 frapataiti etc.); patayeiti is the -aya- (causative/iterative) present 'flies', exactly matching Greek ποτέομαι and Sanskrit patáyati. patarəta- is the verbal adjective 'in flight, flying'; Bartholomae's entry reads 'j. patarəta- Adj. „im Flug begriffen, fliegend“' with the citation āsyaŋhā vayažibya patarətaeibya '... as a pair of flying birds' (Y. 57.28). Pokorny lists the same three forms on p.825.\",\n  derivation_fa=\"pataiti صیغهٔ سوم‌شخص مفرد حال از ریشهٔ اوستایی pat- «پریدن» است و patayeiti ستاک سببی/تکراری با پسوند -aya- که دقیقاً با سنسکریت patáyati و یونانی potéomai برابر است. patarəta- صفت فعلی «در پرواز، پرنده» است که بارتولومه به همین معنا ضبط کرده است. ادعای نورایی درست است.\",\n  sources=[W_PIE],\n  ref_check=[{\"ref\":\"POK:825\",\"status\":\"supports\",\"note\":\"IEW pet-2: 'Avestan pataiti „fliegt, eilt“ ... Avestan patayeiti „fliegt“ ... Avestan patarəta- „fliegend“'.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"AiW s.v. patarəta- and pat-\",\"stance\":\"supports\",\"note\":\"'j. patarəta- Adj. „im Flug begriffen, fliegend“: āsyaŋhā vayažibya °taeibya „.. als ein paar fliegende Vögel“ Y.57.28' (BRT.txt line 14871).\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV p.300\",\"stance\":\"supports\",\"note\":\"lists YAv. frapataiti, patənti, pataṯ, Caus. uspataiiēni etc. for *pat.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p.19\",\"stance\":\"supports\",\"note\":\"'av. pataiti „fliegt, eilt“ ... av. patayeiti „fliegt“'.\"}])\n\nN(id=7, lang=\"Avestan\", words=\"fra-ptaražât; paiti-pasti\",\n  verdict=\"confirmed\",\n  derivation=\"Avestan fraptarəjat- (-jant-) 'bird', lit. 'flying forward', is the compound fra- 'forth' + a participle of the extended stem *ptar- (the same *pt-er- that gives Greek πτερόν); Pokorny lists it under the r-/n-formations: 'Avestan fraptarəjat- (-jant-) „Vogel“'. paiti-pasti- f. 'going/stepping towards, approach' is paiti- 'towards' + the -ti- abstract of the same root with the regular Iranian *-tt- > -st-; Walde-Pokorny II 19 glosses it 'Entgegengehn, -treten' and equates it with Sanskrit ati-patti-. Nourai's transliterations (ž for j, and pasti for pasti-) are his usual conventions. Hanging them under pataiti (node 6) rather than directly under the root is a drawing convenience, not an error of substance.\",\n  derivation_fa=\"fraptarəjat- «پرنده» تحت‌اللفظ «پیش‌پرنده» است: fra- «پیش» + صفت فاعلی از ستاک گستردهٔ *ptar- (همان که در یونانی pteron «بال» دیده می‌شود). paiti-pasti- «پیشواز، رویارویی» از paiti- «به‌سوی» و اسم مصدری -ti- همین ریشه است، با تبدیل قاعده‌مند ایرانی *-tt- > -st-. والده–پوکورنی هر دو را ذیل همین ریشه آورده‌اند؛ ادعای نورایی درست است.\",\n  sources=[W_PIE],\n  ref_check=[{\"ref\":\"POK:825\",\"status\":\"supports\",\"note\":\"IEW pet-2 p.826: 'Avestan fraptarəjat- (-jant-) „Vogel“'; and p.825 'paitipasti- f. „Entgegengehen, -treten“ (compare Old Indic ati-patti-)'.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"AiW s.v. pat-\",\"stance\":\"supports\",\"note\":\"Bartholomae's pat- article cites 'fraptarəjat- Yt.19.82' among the present forms (BRT.txt line 14852).\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p.19\",\"stance\":\"supports\",\"note\":\"'paiti-pasti- f. „Entgegengehn, -treten“ (= ai. ati-patti- „das Verstreichen“)'.\"}])\n\nN(id=8, lang=\"Old Persian\", words=\"pat\",\n  verdict=\"confirmed\",\n  derivation=\"Old Persian pat- 'to fly' is a lexicon lemma in Kent's Old Persian: 'pat- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. πέτεται, Lt. petī ‘seeks’, pIE *pet-' (Lexicon p.194) — the page Nourai cites. In the inscriptions the simplex is not attested; the lemma is set up on the strength of the compound ud-apatatā (node 9), which is why Kent enters it immediately before 'ud- + pat-'.\",\n  derivation_fa=\"پارسی باستان pat- «پریدن» در واژه‌نامهٔ کنت (ص ۱۹۴) مدخل دارد: «pat- فعل «پریدن»: اوستایی pat-aiti، سنسکریت pátati، یونانی pétetai، لاتین petī، هندواروپایی *pet-». خود فعل ساده در سنگ‌نبشته‌ها نیامده و از روی مرکّب udapatatā بازسازی شده است. ادعای نورایی درست است.\",\n  sources=[W_PIE],\n  ref_check=[\n    {\"ref\":\"KNT:194\",\"status\":\"supports\",\"note\":\"Kent, Old Persian, Lexicon p.194: 'pat- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. πέτεται, Lt. petī ‘seeks’, pIE *pet-.' (KNT.txt line 5623; the LEXICON 195 running head follows a few lines later).\"},\n    {\"ref\":\"POK:825\",\"status\":\"supports\",\"note\":\"IEW p.825 cites 'ap. ud-apatata „erhob sich“' for Old Persian.\"}],\n  consulted=[\n    {\"src\":\"KNT\",\"where\":\"Lexicon p.194\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV p.300\",\"stance\":\"partial\",\"note\":\"'*OLD PERSIAN: (+ *uz-) udpat- ‘to rise up, rebel’ = Kent: 194' — Cheung lemmatises only the compound, i.e. the simplex is unattested.\"}])\n\nN(id=9, lang=\"Old Persian\", words=\"ud-pat; ud-a-pat-atâ\",\n  verdict=\"confirmed\",\n  derivation=\"ud-pat- 'to rise up, rebel' = ud- 'up' + pat- 'fly'; the attested form is the 3sg. imperfect middle udapatatā <u-d-p-t-t-a>, with the augment a- inserted between preverb and root as Old Persian requires. It occurs seven times in the Bisotun inscription of Darius (DB 1.36, 1.38, 1.74, 1.78, 2.10, 2.14f, 3.24, 3.79) of rebel leaders, e.g. DB 1.78-79 '… Árʿa nāma Arminiʿya … hauv udapatatā Babirauv' ('a man named Arxa, an Armenian … he rose up in Babylon'). Kent p.194 has both the lemma and the attestations, and Pokorny p.825 cites the same form. The semantic shift 'fly up' → 'rise in revolt' is the ordinary Old Persian idiom for rebellion.\",\n  derivation_fa=\"ud-pat- «برخاستن، سر برداشتن (شوریدن)» از پیشوند ud- «بالا» و pat- «پریدن» است؛ صورت مضبوط udapatatā (ماضی استمراری سوم‌شخص مفرد میانه) است که در سنگ‌نبشتهٔ بیستون هفت بار دربارهٔ سرکشان به کار رفته است (افزایهٔ a- میان پیشوند و ریشه می‌آید). تحول معنایی «برپریدن» > «شوریدن» اصطلاح معمول هخامنشی است. ادعای نورایی درست است.\",\n  sources=[W_PIE],\n  ref_check=[\n    {\"ref\":\"KNT:194\",\"status\":\"supports\",\"note\":\"Kent p.194: 'ud- + pat- ‘rise up, rebel’ (cf. Bv. TPS 1945.64-66): udapatatā imf. mid. (§84, §213, §285.II) DB 1.36, 38, 74, 78; 2.10, 14f; 3.24, 79.'\"},\n    {\"ref\":\"POK:825\",\"status\":\"supports\",\"note\":\"IEW p.825: 'ap. ud-apatata „erhob sich“'.\"}],\n  consulted=[\n    {\"src\":\"KNT\",\"where\":\"text DB 1.78-79 and Lexicon p.194\",\"stance\":\"supports\",\"note\":\"KNT.txt line 3755 quotes the passage 'martiya Árʿa nāma Arminiʿya … hauv udapatatā Babirauv'.\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV p.300\",\"stance\":\"supports\",\"note\":\"'MED.; Pres. them.: impf. IND. 3sg. udapatatā <u-d-p-t-t-a> (DB 1.36, DB 1.38, DB 2.10, etc.)'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p.19\",\"stance\":\"supports\",\"note\":\"'ap. ud-apatata „erhob sich“'.\"}])\n\nN(id=10, lang=\"Avestan / Old Persian\", words=\"karši-ptan\",\n  verdict=\"plausible\",\n  derivation=\"The bird-name is real and the analysis is the standard one, but the form and the language label both need correction. Avestan has karšiptar- (nom. karšiptā), the mythical bird that brought the Mazdayasnian religion to Yima's vara (Vd. 2.42); Bartholomae's article reads 'j. karšiptar- m. Name eines Vogels' and analyses it as 'karši- (… zu lat. currō, mhd. hurren) + *ptar- … der Kompositionsform des Nom. ag. zum V. pat-; also eig. „Schnellflieger“, vgl. gr. ὠκυπέτης … und lat. accipiter' — which is exactly Nourai's gloss 'swift flying (bird)', his cross-reference to Ôku (*ōḱu- 'swift') and his NOTE comparing Latin acu-pedius. The spelling karši-ptan follows Horn p.191 ('aw. karšiptan-'), an older reading that Bartholomae superseded; and the word is purely Avestan, not Old Persian.\",\n  derivation_fa=\"نام این پرنده در اوستا karšiptar- (فاعلی: karšiptā) است، مرغ افسانه‌ای که دین مزدیسنا را به ورِ جم برد (وندیداد ۲،۴۲). بارتولومه آن را به karši- «تند، تیز» + *ptar- (صورت ترکیبی اسم فاعل از ریشهٔ pat-) تحلیل کرده و معنای تحت‌اللفظی آن را «تندپر» گفته و با یونانی ōkupetēs و لاتین accipiter سنجیده است — همان چیزی که نورایی می‌گوید. امّا ضبط karši-ptan از هرن (ص ۱۹۱) گرفته شده و کهنه است، و برچسب «پارسی باستان» نادرست است. با احتیاط پذیرفتنی است.\",\n  sources=[W_PIE],\n  ref_check=[\n    {\"ref\":\"BRT:458\",\"status\":\"supports\",\"note\":\"Bartholomae AiW col. 457-458 s.v. karšiptar-: 'Name eines Vogels ... Komp.: karši- ... + *ptar- ... der Kompositionsform des Nom. ag. zum V. pat- ...; also eig. „Schnellflieger“, vgl. gr. ὠκυπέτης ... und lat. accipiter bei JSchmidt' (BRT.txt line 9369ff; the surrounding column heads read '455 karapan- 2 — kars- 456 ... 457').\"},\n    {\"ref\":\"POK:825\",\"status\":\"not_found\",\"note\":\"Pokorny's pet-2 article (pp.825-826) does not mention karšiptar-; it cites only fraptarəjat- for an Avestan bird name.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"col. 457-458\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n    {\"src\":\"HRN\",\"where\":\"p.191 no.857\",\"stance\":\"partial\",\"note\":\"'Tomaschek, Pamirdialekte S.771, vergleicht aw. karšiptan-, phlv. karš(i)ft (Deutung nicht sicher)' — Horn's spelling is Nourai's, but Horn flags the interpretation as uncertain.\"},\n    {\"src\":\"KNT\",\"where\":\"Old Persian Lexicon\",\"stance\":\"silent\",\"note\":\"no karši- compound in Kent; the word is not Old Persian.\"}])\n\nN(id=11, lang=\"Pahlavi\", words=\"karšift\",\n  verdict=\"plausible\",\n  derivation=\"A Pahlavi karš(i)ft is attested as the Middle Persian continuation of Av. karšiptar-: the Bundahišn (24.11) names karšift as the ratu (chief) of birds, and Bartholomae's footnote to karšiptar- cites 'Bd. 24.11: karšift kē farz ē (?) ...'. Phonologically Av. karšipt- > MP karšift with the regular Middle Persian spirantisation of postvocalic -p- to -f- before -t. Horn p.191 gives the form as 'phlv. karš(i)ft' but adds 'Deutung nicht sicher'; the word is in neither MacKenzie's nor Nyberg's glossary, so it rests on the Bundahišn passage alone — hence 'plausible' rather than 'confirmed'.\",\n  derivation_fa=\"در فارسی میانه karš(i)ft نام مرغی است که در بندهش (۲۴،۱۱) ردِ پرندگان خوانده شده است؛ بارتولومه همین قطعه را در حاشیهٔ karšiptar- آورده است. از نظر آوایی، پِ اوستایی پیش از t در فارسی میانه به f بدل شده است. امّا این واژه نه در فرهنگ مکنزی و نه در نیبرگ مدخل دارد و خود هرن نیز می‌نویسد «تفسیر آن قطعی نیست»؛ پس با احتیاط پذیرفتنی است.\",\n  sources=[AB_K],\n  ref_check=[{\"ref\":\"HRN:191\",\"status\":\"supports\",\"note\":\"Horn, Grundriss p.191 no.857 (HRN.txt leaf 213): '857. kesek ‘Elster’. Tomaschek ... vergleicht aw. karšiptan-, phlv. karš(i)ft (Deutung nicht sicher), waḵ. karjöpc, sar. karjopc, šign. kšebc ‘Elster’.'\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"col. 458 footnote 2\",\"stance\":\"supports\",\"note\":\"'Diese Bedeutung folgt aus Bd. 24.11: karšift kē farž ... ; vgl. np. kurž (ZDMG. VI, 493)'.\"},\n    {\"src\":\"PHD\",\"where\":\"MacKenzie\",\"stance\":\"silent\",\"note\":\"grep 'karšift|karsift' in PHD.txt / PHD_mackenzie.txt → no hit.\"},\n    {\"src\":\"NYB\",\"where\":\"Manual II glossary\",\"stance\":\"silent\",\"note\":\"no hit for karšift.\"}])\n\nN(id=12, lang=\"Persian\", words=\"kašak «کَشَک» (extra: کَبَک ، کَشکِرک)\",\n  verdict=\"transcription_suspect\",\n  derivation=\"The word and the derivation are real, but the JSON's second Persian form is a misreading. Borhan-e Qate' (Mo'in's ed.) vol. 3 p.1651-52 has the headword کشک kašk: 'و آن پرنده‌ای است سیاه و سفید که عربان عقعق خوانند' ('a black-and-white bird which the Arabs call ‘aq‘aq [magpie]'), and Mo‘in's footnote 1 to p.1652 reads: '«کشکه» = کشکرک (ه.م.)، قس: (ایر.) پهلوی karš(ift)_Karšiptan (مفهوم آن واضح نیست)، وخی karjöpc، سریکلی karjope، شغنی kšebc (زاغی) = Elster = magpie' — i.e. Mo‘in reproduces Horn's comparison, which is the whole basis of Nourai's arrow. So the chain Av. karšiptar- > MP karš(i)ft > NP kašk/kašak (with loss of the -r- of the cluster -rš- and of the final -t) is Tomaschek's conjecture, adopted by Horn and Mo‘in but expressly marked uncertain; the Pamir cognates (Wakhi karjöpc, Shughni kšebc) are the real support. The printed page of Nourai gives the variants as کَسَک ، کَشکِرک; the JSON's first variant کَبَک (kabak 'partridge') is an extraction error — the middle letter on the page is a dotless sīn, not bē.\",\n  derivation_fa=\"خود واژه و ریشه‌شناسی هست ولی خوانش اسکن ایراد دارد. برهان قاطع (چاپ معین، ج ۳ ص ۱۶۵۱–۱۶۵۲) ذیل «کشک» می‌نویسد: «و آن پرنده‌ای است سیاه و سفید که عربان عقعق خوانند»، و معین در حاشیه آن را با پهلوی karš(ift) و اوستایی Karšiptan و صورت‌های پامیری (وخی karjöpc، شغنی kšebc) می‌سنجد و می‌افزاید «مفهوم آن واضح نیست». پس زنجیرهٔ karšiptar- > karšift > کشک حدس توماشک است که هرن و معین با احتیاط پذیرفته‌اند. نکتهٔ مهم: در صفحهٔ چاپی کتاب صورت‌های دیگر «کَسَک ، کَشکِرک» آمده است، نه «کَبَک»؛ پس این خطای خوانش اسکن است نه خطای چاپ کتاب.\",\n  error_in=\"extraction\",\n  book_prints=\"کَشَک  /  کَسَک ، کَشکِرک\",\n  correct_form=\"کَسَک ، کَشکِرک\",\n  sources=[AB_K],\n  ref_check=[\n    {\"ref\":\"BQT:1659\",\"status\":\"not_found\",\"note\":\"Printed p.1659 (= BQT_v3_picofile.pdf page 452 per BQT_v3_pagemap.json) carries کف، کفاند، کفت، کفتر، کفتار — nothing about the bird. The material Nourai uses is seven pages earlier, at pp.1651-52 (pdf 444-445, running head '1653' on the next leaf): headword کشک 'پرنده‌ای است سیاه و سفید که عربان عقعق خوانند' with Mo‘in's footnote 1 citing پهلوی karš(ift), Karšiptan, وخی karjöpc, شغنی kšebc = Elster/magpie. So the page number is off by 7.\"},\n    {\"ref\":\"HRN:191\",\"status\":\"supports\",\"note\":\"Horn p.191 no.857 'kesek ‘Elster’' — the headword between kešef (کشف, no.856) and kišver (کشور, no.858), i.e. کشک; 'vergleicht aw. karšiptan-, phlv. karš(i)ft (Deutung nicht sicher)'.\"}],\n  consulted=[\n    {\"src\":\"BQT\",\"where\":\"vol.3 pp.1651-52 (Mo‘in's footnote 1)\",\"stance\":\"supports\",\"note\":\"'«کشکه» = کشکرک (ه.م.)، قس: (ایر.) پهلوی karš(ift)_Karšiptan (مفهوم آن واضح نیست)، وخی karjöpc، سریکلی karjope، شغنی kšebc (زاغی، کلاغ زاغی) = Elster ... = magpie'; and footnote 7 'کشکرک kiškarak ... رک: کشک'.\"},\n    {\"src\":\"HRN\",\"where\":\"p.191 no.857\",\"stance\":\"partial\",\"note\":\"Horn records the comparison but calls the interpretation uncertain.\"},\n    {\"src\":\"MON\",\"where\":\"abadis.ir کشک (فرهنگ معین/دهخدا/عمید)\",\"stance\":\"silent\",\"note\":\"the modern one-volume dictionaries list کشک only as the dairy product ('ته‌ماندهٔ ماست یا دوغ که پس از جوشاندن خشک کنند'); the bird sense survives only in Borhan/Dehkhoda.\"}])\n\nN(id=13, lang=\"Germanic\", words=\"fethro\",\n  verdict=\"confirmed\",\n  derivation=\"Proto-Germanic *feþrō 'feather' < PIE *pet-rā, the r-stem noun of *pet- 'to fly' (Grimm's Law: PIE p > Gmc f, PIE t > Gmc þ). Watkins/AHD prints it in exactly Nourai's shape: 'pet- Also petə-. To rush, fly. … 1. Suffixed form *pet-rā in Germanic *feþrō, feather, in Old English fether, feather: FEATHER.' The same stem underlies Greek πτερόν and Hittite pattar; Klein sets up Teut. *feþ(a)rō- 'corresponding to I.-E. *petrā, zero degree *pterā, „wing; feather“'.\",\n  derivation_fa=\"ژرمنی آغازین *feþрō «پَر، پرِ پرنده» از صورت پسونددار *pet-rā از ریشهٔ *pet- «پریدن» است؛ طبق قانون گریم p هندواروپایی به f و t به þ بدل می‌شود. واتکینز (پیوست ریشه‌های فرهنگ AHD) عیناً همین صورت را می‌آورد. هم‌ریشهٔ یونانی pteron و هیتی pattar است. ادعای نورایی درست است.\",\n  sources=[W_PIE],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 (AHD_watkins1985.txt s.v. pet-): 'Suffixed form *pet-rā in Germanic *feþrō, feather, in Old English fether, feather: FEATHER.'\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. feather\",\"stance\":\"supports\",\"note\":\"'fr. Teut. *feþ(a)rō-, corresponding to I.-E. *petrā, zero degree *pterā, ‘wing; feather’'.\"},\n    {\"src\":\"POK\",\"where\":\"IEW 826\",\"stance\":\"supports\",\"note\":\"'Old High German fedara, anfrk. fethera, Old English feder, Old Icelandic fjǫdr „feather“ (*petrā)'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p.19-21\",\"stance\":\"supports\",\"note\":\"the r-/n-stem nom. *pet-r-(ɡ), gen. *pet-n-es „Flügel“ heads the article.\"}])\n\nN(id=14, lang=\"English\", words=\"feather\",\n  verdict=\"confirmed\",\n  derivation=\"English feather < Middle English fether < Old English feþer, feþor < Proto-Germanic *feþrō (node 13); cognate with Old Saxon fethara, Old High German fedara (> German Feder), Old Norse fjǫdr. Klein sets out the whole series and connects it with Greek πτερόν and the second element of Latin acci-piter, all from I.-E. base *pet- 'to fly, fall upon, fall'.\",\n  derivation_fa=\"انگلیسی feather از انگلیسی میانه fether و آن از انگلیسی کهن feþer است، از ژرمنی آغازین *feþрō؛ هم‌ریشه با آلمانی Feder و ایسلندی کهن fjǫdr. کلاین همین زنجیره را ذیل ریشهٔ *pet- می‌آورد. ادعای نورایی درست است.\",\n  sources=[W_PIE],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference in the book; the parent box cites AHD, which covers this step ('in Old English fether, feather: FEATHER').\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. feather, n.\",\"stance\":\"supports\",\"note\":\"'ME. fether, fr. OE. feder, rel. to OS. fethara, ON. fjǫdr … fr. Teut. *feþ(a)rō-'.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins s.v. pet-\",\"stance\":\"supports\",\"note\":\"'in Old English fether, feather: FEATHER'.\"},\n    {\"src\":\"SKT\",\"where\":\"Skeat\",\"stance\":\"silent\",\"note\":\"grep 'feather' in SKT.txt gives only cross references in this extract.\"}])\n\nN(id=15, lang=\"Latin\", words=\"petere; piter; acci-piter, acu-pedius\",\n  verdict=\"disputed\",\n  derivation=\"Two of the three items are right and one is wrong. (a) Latin petō, petere 'to make for, fall upon, attack, seek' is the direct continuant of *pet- (Pokorny p.825; Buck 19383: 'Lat. petere, orig. “direct oneself toward, attack, fall upon” then in weakened sense “seek”'). (b) accipiter 'hawk, falcon' goes back to *acu-peter 'swiftly-flying', reshaped under the influence of accipere; its second element -piter is indeed the *pet- root, so Nourai's isolated entry 'piter : fly' is a segmentation, not a Latin lemma. (c) acu-pedius, however, does NOT mean 'a swift flying bird, falcon' and does not belong here: it is the adjective 'swift-footed', literally 'sharp-footed' (Paulus Festus), whose second element is pēs, ped- 'foot' (*pōd-). Klein says so explicitly under Accipiter — 'cp. acu-pedius, “swift-footed”, lit. “sharp-footed”' — and Ernout-Meillet make the same point: 'De même que acu-pedius rappelle gr. ὠκύ-πους, accipiter rappelle gr. ὠκύ-πτερος, skr. āśú-patvan-'. The two words are morphological parallels, not synonyms, and Nourai has merged them into one gloss.\",\n  derivation_fa=\"از سه قلم این خانه دو تا درست است و یکی نادرست. لاتین petere «روی آوردن، حمله بردن، جستن» دنبالهٔ راستین *pet- است؛ accipiter «باز، قره‌‌وش» از *acu-peter «تندپر» است که زیر تأثیر accipere دگرگون شده، و پس جزء دوم آن (-piter) همین ریشه است. امّا acu-pedius هرگز به معنای «پرندهٔ تندپر» نیست؛ صفتی است به معنای «تندرو، تیزپا» که جزء دومش pēs/ped- «پا» (از *pōd-) است، نه pet-. کلاین و ارنو–میه هر دو همین را می‌گویند. پس پژوهش امروزین این بخش از ادعای نورایی را رد می‌کند.\",\n  sources=[W_PIE],\n  ref_check=[\n    {\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins s.v. pet-: '2. Latin petere, to go toward, seek: -PETAL, PETITION, PETULANT; APPETITE, COMPETE …' and '4. Suffixed form *pet-ro- (see ōku-)' — supports petere and accipiter but says nothing about acu-pedius.\"},\n    {\"ref\":\"BRT:458\",\"status\":\"partial\",\"note\":\"Bartholomae (karšiptar-) compares 'lat. accipiter bei JSchmidt' and Gk ὠκυπέτης, but not acu-pedius.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. Accipiter\",\"stance\":\"contradicts\",\"note\":\"'L. accipiter fr. orig. *acu-peter, ‘swiftly-flying’ … The first element lit. means ‘sharp’ (cp. acu-pedius, ‘swift-footed’, lit. ‘sharp-footed’, and acuere, ‘to sharpen’)' — acu-pedius is 'swift-footed', not a bird.\"},\n    {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. accipiter (LAT.txt 1111-1113) and s.v. acupedius (1345)\",\"stance\":\"contradicts\",\"note\":\"'De même que acu-pedius rappelle gr. ὠκύ-πους, accipiter rappelle gr. ὠκύ-πτερος, skr. āśú-patvan- “qui vole (vite)”'; s.v. acupedius: 'Adaptation de ὠκύπους, comme celeripes …'.\"},\n    {\"src\":\"POK\",\"where\":\"IEW 826\",\"stance\":\"supports\",\"note\":\"'Latin acci-piter, -pitris „hawk, falcon“ (to 1. part see below *ōku- „quick, fast“)' — Nourai's Ôku cross-reference is right.\"},\n    {\"src\":\"SYN\",\"where\":\"Buck 19383\",\"stance\":\"supports\",\"note\":\"'Lat. petere, orig. ‘direct oneself toward, attack, fall upon’ … : Grk. πέτομαι ‘fly’, πίπτω ‘fall’, Skt. pat- ‘fly, fall’'.\"}])\n\nN(id=16, lang=\"English\", words=\"compete, repeat; accipiter\",\n  verdict=\"confirmed\",\n  derivation=\"compete < Latin compētere 'to strive together for, coincide' (com- + petere), attested in English from the 1610s in the sense 'to enter into rivalry'; repeat < Old French repeter < Latin repetere 're-seek, do again' (re- + petere). Accipiter is the modern Linnaean genus name for the true hawks, taken over unchanged from the Latin noun. All three are listed under *pet- by Watkins ('APPETITE, COMPETE, IMPETUS, PERPETUAL, REPEAT') and by Klein under feather ('Cp. Accipiter, appetence, appetite … compete … repeat, repetition').\",\n  derivation_fa=\"compete از لاتین compētere (com- + petere) «با هم بر سر چیزی تاختن» و repeat از فرانسهٔ کهن repeter از لاتین repetere «دوباره جستن» است. Accipiter نیز نام سردهٔ دوم‌نامی زیست‌شناسی است که عیناً از لاتین گرفته شده. واتکینز و کلاین هر سه را ذیل ریشهٔ *pet- آورده‌اند؛ ادعای نورایی درست است.\",\n  sources=[W_PIE],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins s.v. pet-: 'Latin petere, to go toward, seek: -PETAL, PETITION, PETULANT; APPETITE, COMPETE, IMPETUS, PERPETUAL, REPEAT.'\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. feather (cross-reference list) and s.v. Accipiter\",\"stance\":\"supports\",\"note\":\"'Cp. Accipiter, appetence, appetite, aptote, asymptote, compete … repeat, repetition, symptom'; 'Accipiter, n., a genus of hawks and falcons (ornithol.) — L. accipiter'.\"},\n    {\"src\":\"POK\",\"where\":\"IEW 826\",\"stance\":\"supports\",\"note\":\"'Latin peto, -ere, -īvī, -ītum „auf etwas losgehen, to attain seek“'.\"}])\n\nN(id=17, lang=\"Greek\", words=\"petron; helik-pter\",\n  verdict=\"transcription_suspect\",\n  derivation=\"The Greek word for 'wing, feather' is πτερόν pterón (zero-grade *pt-ero- of *pet-), not 'petron'; πέτρος/πέτρα is the unrelated word for 'rock'. The printed page (pdf p.400, book p.370) really does read 'petron : wing', so this is Nourai's own misprint (or a slip for his transliteration of πτερόν), faithfully carried over by the extraction; Watkins s.v. pet- has '6. Suffixed zero-grade form *pt-ero- in Greek pteron, feather, wing'. The second item, helik-pter, is not an ancient Greek word at all but the Greek material of the 19th-century French coinage hélicoptère: ἕλιξ, gen. ἕλικος 'spiral' + πτερόν 'wing'. Nourai's gloss 'spiral wing' and his segmentation helico-pter (rather than the popular heli-copter) are correct.\",\n  derivation_fa=\"واژهٔ یونانی «بال، پَر» pterón (πτερόν) است، صورت صفردرجهٔ *pt-ero- از *pet-؛ «petron» واژه‌ای دیگر (پتروس/پترا «سنگ، صخره») است. در صفحهٔ چاپی کتاب هم عیناً «petron» آمده؛ پس خطای چاپی خود نورایی است و خوانش اسکن درست عمل کرده است. جزء دوم، helik-pter، واژهٔ یونانی باستان نیست بلکه مادهٔ یونانیِ ساختهٔ فرانسوی hélicoptère (۱۸۶۱) است: hélix/helik- «مارپیچ» + pteron «بال»؛ معنایی که نورایی می‌دهد درست است.\",\n  error_in=\"book\",\n  book_prints=\"petron : wing\",\n  correct_form=\"pteron (πτερόν) 'wing, feather'\",\n  sources=[ETYH, W_PIE],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"contradicts\",\"note\":\"Watkins s.v. pet-: '6. Suffixed zero-grade form *pt-ero- in Greek pteron, feather, wing, and pterux, wing' — the form is pteron, not petron.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. helicopter and s.v. feather\",\"stance\":\"contradicts\",\"note\":\"'helicopter, n. — F. hélicoptère, compounded of Gk. ἕλιξ, gen. ἕλικος, ‘coil, spiral’, and πτερόν, ‘wing’'; s.v. feather: 'Gk. πτερόν, “feather; wing”'.\"},\n    {\"src\":\"POK\",\"where\":\"IEW 826\",\"stance\":\"contradicts\",\"note\":\"'gr. πτερόν „feather, wing“'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p.20\",\"stance\":\"contradicts\",\"note\":\"the Greek material is listed under πτερ-, never *petron.\"}])\n\nN(id=18, lang=\"French\", words=\"helîcopter\",\n  verdict=\"plausible\",\n  derivation=\"The route is right, the spelling is not French. The word was coined in French in 1861 by Gustave de Ponton d'Amécourt as hélicoptère, 'flying machine propelled by screws', from Greek ἕλιξ/ἕλικος 'spiral' + πτερόν 'wing'; it passed into English in the same century and was transferred to the modern rotorcraft by 1918 (Etymonline). Nourai prints 'helîcopter', which is neither the French hélicoptère nor the English helicopter but his own transliteration habit (î = long i, French accents dropped); the extraction is faithful to the page, so this is a book-side spelling, not a scan error. The derivational claim itself (Greek → French → English and Persian) is correct.\",\n  derivation_fa=\"مسیر درست است ولی ضبط فرانسوی آن نادرست. این واژه در سال ۱۸۶۱ در فرانسه به دست پونتون دامکور به صورت hélicoptère ساخته شد، از helix/helik- «مارپیچ» و pteron «بال»، و تا ۱۹۱۸ به معنای بالگرد امروزی به کار رفت. نورایی «helîcopter» می‌نویسد که نه فرانسوی است و نه انگلیسی، بلکه شیوهٔ آوانگاری خود اوست؛ این صورت در صفحهٔ چاپی هم همین طور آمده است. با احتیاط پذیرفتنی است.\",\n  sources=[ETYH],\n  ref_check=[{\"ref\":\"AHD:611\",\"status\":\"not_checked\",\"note\":\"The 1975 New College AHD is not on disk (only the Watkins IE-roots appendix, AHD_watkins1985.txt, which has no 'helicopter' headword). p.611 falls in the 'h' range of that edition, so the citation is plausible but unverified.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. helicopter\",\"stance\":\"supports\",\"note\":\"'helicopter, n. — F. hélicoptère, compounded of Gk. ἕλιξ, gen. ἕλικος, ‘coil, spiral’, and πτερόν, ‘wing’' — spelling hélicoptère.\"},\n    {\"src\":\"WEB\",\"where\":\"Webster's New Twentieth Century\",\"stance\":\"silent\",\"note\":\"no hit for the French form in WEB_vol1.txt (the volume on disk is A-L in part only).\"}])\n\nN(id=19, lang=\"Persian\", words=\"helîcopter «هلیکوپتر»\",\n  verdict=\"confirmed\",\n  derivation=\"Persian هلیکوپتر helikōpter is a 20th-century loan taken from French hélicoptère (with the French stress pattern and the -pter ending, not the English -copter), as the Persian dictionaries themselves state: Mo‘in's Farhang-e Fārsi tags it [فر.] = French and defines it 'نوعی وسیلهٔ ترابری هوایی که در هنگام فراز و فرود می‌تواند به طور قایم یا عمودی حرکت کند'; Dehkhoda likewise marks it فرانسوی. So the arrow French → Persian is exactly right, and Nourai's reference to Mo‘in is the right authority for it.\",\n  derivation_fa=\"«هلیکوپتر» وام‌واژه‌ای است از فرانسهٔ hélicoptère که در سدهٔ بیستم وارد فارسی شده است؛ شاهد آن پایانهٔ «پتر» است نه «کاپتر» انگلیسی. فرهنگ معین آن را با نشانهٔ [فر.] ضبط کرده و دهخدا نیز آن را فرانسوی خوانده است. ادعای نورایی درست است.\",\n  sources=[AB_H, ETYH],\n  ref_check=[{\"ref\":\"MON:5165\",\"status\":\"supports\",\"note\":\"Mo‘in's Farhang-e Fārsi (consulted via abadis.ir/fatofa/هلیکوپتر/, section فرهنگ معین) has the headword with the origin tag [فر.] (French) and the definition quoted above; the page number 5165 falls in the foreign-word volume of the continuous pagination, which could not be checked directly because MON vols 4-6 are not in the local OCR.\"}],\n  consulted=[\n    {\"src\":\"MON\",\"where\":\"abadis.ir, فرهنگ معین s.v. هلیکوپتر\",\"stance\":\"supports\",\"note\":\"origin marked فر. (French).\"},\n    {\"src\":\"ARY\",\"where\":\"Aryanpur\",\"stance\":\"silent\",\"note\":\"no entry for هلیکوپتر in ARY_pages.txt (the book covers inherited Indo-European vocabulary, not modern European loans).\"}])\n\nN(id=20, lang=\"English\", words=\"helicopter\",\n  verdict=\"confirmed\",\n  derivation=\"English helicopter is borrowed from French hélicoptère (1861), first in the sense 'device for enabling airplanes to rise perpendicularly' and used by Jules Verne and the Wright brothers of theoretical machines; it was transferred to the modern rotorcraft by 1918. The popular re-analysis as heli-copter (whence copter, helipad) is later and secondary; the true division is helico-pter. Klein: 'helicopter, n. — F. hélicoptère'.\",\n  derivation_fa=\"انگلیسی helicopter وام‌گرفته از فرانسهٔ hélicoptère (۱۸۶۱) است که نخست برای دستگاه‌های فرضی به کار می‌رفت و از ۱۹۱۸ بر بالگرد امروزی اطلاق شد. تجزیهٔ عامیانهٔ heli-copter (که copter را زاد) متأخر است؛ تجزیهٔ درست helico-pter است. ادعای نورایی درست است.\",\n  sources=[ETYH],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins s.v. pet- derives the -pter of helicopter from '*pt-ero- in Greek pteron' (the '-PTER' entry in the word list); the AHD main entry for helicopter ('F. hélicoptère') could not be checked, the 1975 volume not being on disk.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. helicopter\",\"stance\":\"supports\",\"note\":\"'F. hélicoptère, compounded of Gk. ἕλιξ … and πτερόν, ‘wing’. See helix and ptero-.'\"},\n    {\"src\":\"FSD\",\"where\":\"Funk & Wagnalls\",\"stance\":\"silent\",\"note\":\"no helicopter entry found in the volumes on disk.\"}])\n\nN(id=21, lang=\"Sanskrit\", words=\"patita\",\n  verdict=\"confirmed\",\n  derivation=\"Sanskrit patitá- is the -ta- past participle of pátati 'flies, falls' (RV onwards), 'fallen', and in the classical language also 'fallen (from caste), degraded, low' — exactly the double sense Nourai gives. It is the Indic exact match of the Iranian *pat-ta- that underlies Persian past (nodes 4-5), which is why Hübschmann adduced it there. Pokorny prints 'participle patita-' in the opening line of pet-2.\",\n  derivation_fa=\"سنسکریت patitá- صفت مفعولی (پسوند -ta-) از pátati «می‌پرد، می‌افتد» است، به معنای «افتاده» و در سنسکریت کلاسیک «فروافتاده، از کاست رانده‌شده، پست» — دقیقاً همان دو معنایی که نورایی می‌آورد. این صورت هم‌ارز هندیِ *pat-ta- ایرانی است که زیربنای «پست» فارسی شمرده می‌شود. ادعای نورایی درست است.\",\n  sources=[W_PIE],\n  ref_check=[{\"ref\":\"POK:825\",\"status\":\"supports\",\"note\":\"IEW pet-2: 'Old Indic patati „fliegt, wirft sich, fällt“ … Supin. patitum, participle patita-'.\"}],\n  consulted=[\n    {\"src\":\"WLD\",\"where\":\"Bd. II p.19\",\"stance\":\"supports\",\"note\":\"'set-Formen Fut. patisyati, pf. paptima, sup. pátitum, ptc. patitá-'.\"},\n    {\"src\":\"HUB\",\"where\":\"p.41 no.316\",\"stance\":\"supports\",\"note\":\"'= *patta-, skr. patita-' — Hübschmann's equation of the Indic participle with the Iranian pre-form.\"}])\n\nN(id=22, lang=\"Greek\", words=\"pipo; potamos; hipos ho potamios\",\n  verdict=\"transcription_suspect\",\n  derivation=\"potamos and hippopotamos are right; the first item is a misprint. Greek for 'to fall' is πίπτω piptō (infinitive πίπτειν), the reduplicated present *pi-pth₂-e-ti of *pet- (Watkins: '9. Reduplicated form *pi-pt- in Greek piptein, to fall'); 'pipo' is not a Greek word, and the printed page (pdf 400, book p.370) does read 'pipo : to fall', so the fault is the book's, not the scan's. ποταμός potamós 'river' is the o-grade *pot- plus the suffix -amo-, originally 'rushing, plunging water' — Pokorny glosses it eig. 'Wassersturz', Buck 'at first the “falling, plunging, rushing” stream' — which is exactly Nourai's 'falling water, river'. ἵππος ὁ ποτάμιος hippos ho potámios 'the river horse' (Herodotus 2.71) is the phrase that was univerbated into ἱπποπόταμος; Nourai's single-p 'hipos' is his usual simplified transliteration and his cross-reference to Ekwos (*eḱwo- 'horse') is correct.\",\n  derivation_fa=\"دو قلم دوم درست است و قلم نخست غلط چاپی. فعل یونانی «افتادن» piptō (πίπτω) است، ستاک حالِ دوگانه‌ساختِ *pi-pth₂-e-ti از ریشهٔ *pet-؛ «pipo» واژهٔ یونانی نیست و در صفحهٔ چاپی کتاب هم همین طور آمده؛ پس خطای کتاب است نه خطای خوانش اسکن. potamós «رود» از درجهٔ o یعنی *pot- با پسوند -amo- است و معنای نخستینِ آن «آبِ فروریزنده» بوده (پوکورنی: Wassersturz؛ باک: the falling, plunging stream). hippos ho potámios «اسبِ رودخانه» (هرودوت ۲،۷۱) همان عبارتی است که بعداً هیپوپوتاموس شد.\",\n  error_in=\"book\",\n  book_prints=\"pipo : to fall\",\n  correct_form=\"piptō / piptein (πίπτω) 'to fall'\",\n  sources=[W_PIE],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins s.v. pet-: '9. Reduplicated form *pi-pt- in Greek piptein, to fall: PTOMAINE, PTOSIS … 10. O-grade form *pot- in Greek potamos (-amo-, Greek suffix), “rushing water,” river: HIPPOPOTAMUS.' — supports potamos/hippopotamus, contradicts the form 'pipo'.\"}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"IEW 825\",\"stance\":\"partial\",\"note\":\"'πί-πτω (for *πτ-πτω after μίμνω) „fall“ … ποταμός „river“, actually „Wassersturz“'.\"},\n    {\"src\":\"SYN\",\"where\":\"Buck 1393\",\"stance\":\"supports\",\"note\":\"'Grk. ποταμός, fr. root of πίπτω ‘fall’, πέτομαι ‘fly’, Skt. pat- ‘fly, fall’ … ποταμός was at first the “falling, plunging, rushing” stream. Walde-P. 2.19.'\"},\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. feather\",\"stance\":\"partial\",\"note\":\"'ποταμός, “river”, lit. “something flowing, running”, πίπτειν, “to fall” (formed fr. orig. *πί-πτειν on analogy of μίμνειν)'.\"}])\n\nN(id=23, lang=\"English\", words=\"hippopotamus\",\n  verdict=\"confirmed\",\n  derivation=\"English hippopotamus is the Latin hippopotamus, itself from Greek ἱπποπόταμος, a univerbation of Herodotus' phrase ἵππος ὁ ποτάμιος 'the horse of the river' (ἵππος < PIE *h₁eḱwos, Nourai's Ekwos; ποταμός from *pet-, node 22). English use dates from the 16th century, in the Latin form, replacing earlier ypotame from Old French. Klein and Watkins both file it under *pet- through potamos.\",\n  derivation_fa=\"انگلیسی hippopotamus از لاتین hippopotamus و آن از یونانی hippopótamos است که خود از عبارتِ هرودوتی hippos ho potámios «اسبِ رودخانه» پدید آمده است؛ hippos از *h₁eḱwos «اسب» (هم‌ریشهٔ «اسب» فارسی) و potamos از همین ریشهٔ *pet-. ادعای نورایی درست است.\",\n  sources=[W_PIE],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference in the book; the parent Greek box cites AHD, whose pet- article ends '… river: HIPPOPOTAMUS'.\"}],\n  consulted=[\n    {\"src\":\"AHD\",\"where\":\"Watkins s.v. pet-, sense 10\",\"stance\":\"supports\",\"note\":\"'O-grade form *pot- in Greek potamos … “rushing water,” river: HIPPOPOTAMUS.'\"},\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. feather (cross-reference list)\",\"stance\":\"supports\",\"note\":\"'Cp. … helicopter, hippopotamus …' filed under I.-E. base *pet-.\"}])\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Pet 1\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *pet- / *peth₂- 'to fly, to fall; to rush at'\",\n  \"note\": \"Pokorny's pet-2 'to fall; to fly' occupies pp.825-826 of the IEW, so Nourai's POK:825 is right and his gloss 'to fly, to fall' reproduces Pokorny's 'fallen; fliegen' exactly; his own numbering 'Pet 1' corresponds to Pokorny's 2. pet- (Pokorny's 1. pet- 'to spread out', pp.824-825, is Nourai's other Pet entry). Modern handbooks reconstruct the root as *peth₂- and Wiktionary treats 'to spread out' and 'to fly' as two senses of one laryngeal root, so the root box is if anything conservative. On the printed page (pdf 400, book p.370) two boxes in the right-hand column — to the right of the Avestan fra-ptaražât box and of the Old Persian ud-pat box — are drawn but left completely empty; the extraction correctly contains no node for them. Two of Nourai's transliterations on this page are his own misprints (petron for pteron, pipo for piptō), one Latin item is misassigned (acu-pedius), and one Borhan-e Qate' page number is off by seven (BQT:1659 should be 1651-52).\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *pet- / *peth₂- «پریدن، افتادن، فروافتادن بر چیزی»؛ پوکورنی آن را در صفحات ۸۲۵–۸۲۶ زیر pet-2 «fallen; fliegen» آورده است، پس ارجاع POK:825 و معنای نورایی هر دو درست است؛ شمارهٔ «Pet 1» از آنِ خود اوست و با pet-2 پوکورنی برابر است. در ریشه‌شناسی امروزین این ریشه با حنجره‌ای *peth₂- بازساخته می‌شود. در صفحهٔ چاپی، دو خانهٔ سمت راست (روبه‌روی fra-ptaražât و ud-pat) تهی رها شده است. چهار ایراد در این صفحه هست: petron به جای pteron، pipo به جای piptō، معنای نادرست acu-pedius، و شمارهٔ صفحهٔ برهان قاطع (۱۶۵۹ در برابر ۱۶۵۱–۵۲ درست).\",\n  \"sources\": [W_PIE, ETYH],\n  \"ref_check\": [\n    {\"ref\":\"POK:825\",\"status\":\"supports\",\"note\":\"Pokorny IEW: 'Root / lemma: pet-2, petə- : ptē- ptō- ; Meaning: to fall; to fly … References: WP. II 19 ff., WH. II 282 f., 297 f. Page(s): 825-826' (POK_full.txt line 67304ff).\"}],\n  \"consulted\": [\n    {\"src\":\"WLD\",\"where\":\"Bd. II p.19\",\"stance\":\"supports\",\"note\":\"'2. pet- (z. T. petə-, petē-) „auf etwas los- oder niederstürzen, fliegen, fallen“; dazu … nom. pet-r-(ɡ), gen. pet-n-es „Flügel“'.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. pet-\",\"stance\":\"supports\",\"note\":\"'pet- Also petə-. To rush, fly. Variant *ptē-, contracted from *pteə-. … [Pok. 2. pet- 826.]'\"},\n    {\"src\":\"IEC\",\"where\":\"Mann s.v. pet- (1)\",\"stance\":\"supports\",\"note\":\"'pet- (1) (radical: “fly, dash”. Cf. peto, etc.). WP II, 20' — Mann keeps Pokorny's two roots apart in the same way.\"},\n    {\"src\":\"SYN\",\"where\":\"Buck 1393, 19383\",\"stance\":\"supports\",\"note\":\"Buck repeatedly cites 'Grk. πέτομαι ‘fly’, πίπτω ‘fall’, Skt. pat- ‘fly, fall’' as one root (Walde-P. 2.19).\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV pp.299-301\",\"stance\":\"partial\",\"note\":\"Cheung reconstructs 'PIE *pet(H₁)- ‘to fall down, collapse; to fly?’' — same root, with the fall-sense primary and the fly-sense queried.\"}],\n  \"nodes\": nodes\n}\n\nout = {\n  \"pdf_page\": 400,\n  \"book_page\": 370,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [entry]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-400.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"nodes:\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-400.py && python3 -m json.tool data/verification/page-400.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 400",
 "description": "Build and validate page-400.json"
}
```


### [2026-09-14T01:13:20.934Z] TOOL RESULT

```
nodes: 23
JSON OK
nodes verified: 23/23
node verdicts: {'confirmed': 14, 'plausible': 5, 'transcription_suspect': 3, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 17, 'partial': 5, 'not_checked': 5, 'not_found': 2, 'contradicts': 1}
books consulted: {'supports': 40, 'silent': 10, 'partial': 8, 'contradicts': 7} | by book: {'KLN': 9, 'WLD': 7, 'BRT': 6, 'CHEUNG': 6, 'HRN': 6, 'POK': 6, 'PHD': 3, 'MON': 3, 'KNT': 3, 'NYB': 2, 'BQT': 2, 'HUB': 2, 'AHD': 2, 'SYN': 2, 'IEC': 1, 'SKT': 1, 'LAT': 1, 'WEB': 1, 'ARY': 1, 'FSD': 1}
```


## [2026-09-14T01:13:41.566Z] AGENT

Done. `data/verification/page-400.json` written; `verify_check.py 400` reports 23/23 nodes, 0 PROBLEM lines.

**Page 400 (book p. 370) — root "Pet 1" [IE] "to fly, to fall" (POK:825) — root verdict: confirmed**

Node verdicts: confirmed 14 · plausible 5 · transcription_suspect 3 · disputed 1
Ref checks: supports 17 · partial 5 · not_checked 5 · not_found 2 · contradicts 1

Flagged items:
- **disputed — #15 Latin "acu-pedius : a swift flying bird, falcon"**: `acupedius` means 'swift-footed' (lit. 'sharp-footed'), second element `pēs/ped-`, not `pet-`. Klein (s.v. Accipiter) and Ernout–Meillet say so explicitly; `petere` and `accipiter` in the same box are fine.
- **transcription_suspect — #17 Greek "petron : wing"** (`error_in: book`): Greek is πτερόν *pteron*; the printed page really reads "petron", so it is Nourai's misprint, extraction faithful.
- **transcription_suspect — #22 Greek "pipo : to fall"** (`error_in: book`): Greek is πίπτω *piptō*; page prints "pipo". `potamos` and `hipos ho potamios` in the same box are correct.
- **transcription_suspect — #12 Persian kašak** (`error_in: **extraction**`): see below.

**Extraction error for the owner to fix** (data/extracted/batch/page-400.json, node 12 `script_extra`): JSON has `"کَبَک ، کَشکِرک"`; the printed page shows **`کَسَک ، کَشکِرک`** (dotless sīn, not bē). Verified on a 600-dpi crop; page PNG saved to `data/verification/sources/refs/ocr/BOOK/400.png`.

Other findings worth noting:
- **BQT:1659 is off by seven pages** (node 12): the magpie material is at Borhan-e Qate' pp. 1651–52 (headword کشک "پرنده‌ای است سیاه و سفید که عربان عقعق خوانند" + Mo'in's footnote citing Pahlavi karš(ift)/Karšiptan and the Pamir cognates). p.1659 has کف/کفتار.
- HUB:41 no. 316 supports the `patta → past` arrow verbatim and explicitly rejects HRN:70 — so the chart's own NOTE is accurate; both nodes left "plausible" since no modern handbook settles it.
- HRN:22 gives Nourai's Pahlavi `ōftātan` verbatim; BQT:145 only has the Persian headwords (marked partial).
- Two boxes on the printed page (right of #7 and of #9) are drawn but completely empty; the extraction correctly has no nodes for them.
- Six web pages archived via `fetch_source.py` (Wiktionary *peth₂-/افتادن/پست, Etymonline helicopter, abadis کشک/هلیکوپتر).
