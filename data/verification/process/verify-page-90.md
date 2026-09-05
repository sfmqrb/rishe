# Verification process log — verify-page-90


## [2026-09-05T13:45:21.269Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 90 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-90.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-90.json. Write /home/sfmqrb/git/rishe/data/verification/page-90.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 90` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T13:45:22.760Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T13:45:23.476Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T13:45:23.488Z] TOOL RESULT

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


## [2026-09-05T13:45:23.810Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-90.txt"
}
```


### [2026-09-05T13:45:23.830Z] TOOL RESULT

```
1	=== PDF page 90 (book page 60) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bher 3, Bhrei : to cut, pierce  (refs POK:133, 166)
4	#1 (parent #0) [Avestan] refs=HRN:49; BQT:270 | brây : to cut
5	  #2 (parent #1) [Pahlavi] refs=SNS:105 | brîdan : to cut
6	    #3 (parent #2) [Persian] refs=POK:133; BQT:270; HRN:59 | borîdan «بریدن» : to cut ; bor «ـبُر ۵» : cutter ; bîl «بیل» : shovel | extra: بُریده ، بُرش ؛ شیشه بُر ، سنگ بُر ، آهن بُر
7	#4 (parent #0) [Germanic] refs=AHD | borôn : to bore
8	  #5 (parent #4) [English] refs=None | bore
9	#6 (parent #0) [Latin] refs=AHD | forare : to pierce ; ferîre : to cut ; frîcare : to rub
10	  #7 (parent #6) [English] refs=None | perforate, interfere ; friction, debris
11	#8 (parent #0) [Indo-European] refs=KLN:182 | bherd : to cut
12	  #9 (parent #8) [Germanic] refs=None | BURD : board
13	    #10 (parent #9) [English] refs=AHD | board, border
14	--- entry 1 ---
15	ROOT [Indo-European] Bher 4 : bright, brown  (refs POK:136)
16	#1 (parent #0) [Avestan] refs=POK:136; KLN:158 | bowra : red, brown animal, beaver ; bawraini, bawri : beaver
17	  #2 (parent #1) [Persian] refs=BQT:231,314,315; MON:601; AEF:295 | bŭr «بور» : brownish red, red horse, flushed from embarrassment ; bŭreh «بوره» : borax, white | extra: بورک ، بورق
18	    #3 (parent #2) [Arabic] refs=BQT:315 | bŭrq : white, shining | NOTE: TAD:14 links this word to the Arabic root "B.r.q: shines".
19	      #4 (parent #3) [French] refs=PHN:71 | borax
20	        #5 (parent #4) [English] refs=AHD:152 | borax, boric, Boron
21	#6 (parent #0) [Pahlavi] refs=MON:471 | bavarak : beaver
22	  #7 (parent #6) [Persian] refs=MON:471 | babar «بَبَر» : beaver, red fox
23	#8 (parent #0) [Germanic] refs=KLN:158; AHD | brŭnaz : brown ; bero : brown animal, bear, beaver
24	  #9 (parent #8) [English] refs=None | brown, brunet, beaver, bear 2, Bernard
25	
```


## [2026-09-05T13:45:27.273Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-90.json && echo \"=== TOOLS ===\" && ls tools/ && echo \"=== prior example ===\" && ls data/verification/ | head -50",
 "description": "Read source JSON and list verification dir"
}
```


### [2026-09-05T13:45:27.327Z] TOOL RESULT

```
{
  "pdf_page": 90,
  "book_page": 60,
  "entries": [
    {
      "root": {
        "name": "Bher 3, Bhrei",
        "lang": "Indo-European",
        "refs": "POK:133, 166",
        "gloss": "to cut, pierce"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:49; BQT:270",
          "words": [
            {"translit": "brây", "gloss": "to cut", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:105",
          "words": [
            {"translit": "brîdan", "gloss": "to cut", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:133; BQT:270; HRN:59",
          "words": [
            {"translit": "borîdan", "gloss": "to cut", "script": "بریدن"},
            {"translit": "bor", "gloss": "cutter", "script": "ـبُر ۵"},
            {"translit": "bîl", "gloss": "shovel", "script": "بیل"}
          ],
          "script_extra": "بُریده ، بُرش ؛ شیشه بُر ، سنگ بُر ، آهن بُر",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "borôn", "gloss": "to bore", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "bore", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "forare", "gloss": "to pierce", "script": null},
            {"translit": "ferîre", "gloss": "to cut", "script": null},
            {"translit": "frîcare", "gloss": "to rub", "script": null}
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
            {"translit": "perforate, interfere", "gloss": null, "script": null},
            {"translit": "friction, debris", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "KLN:182",
          "words": [
            {"translit": "bherd", "gloss": "to cut", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Germanic",
          "refs": null,
          "words": [
            {"translit": "BURD", "gloss": "board", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "board, border", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bher 4",
        "lang": "Indo-European",
        "refs": "POK:136",
        "gloss": "bright, brown"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:136; KLN:158",
          "words": [
            {"translit": "bowra", "gloss": "red, brown animal, beaver", "script": null},
            {"translit": "bawraini, bawri", "gloss": "beaver", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:231,314,315; MON:601; AEF:295",
          "words": [
            {"translit": "bŭr", "gloss": "brownish red, red horse, flushed from embarrassment", "script": "بور"},
            {"translit": "bŭreh", "gloss": "borax, white", "script": "بوره"}
          ],
          "script_extra": "بورک ، بورق",
          "note": null,
          "quote": {"text": "بیازید چنگال گردی بزور - بیفشارد یک دست بر پشت بور", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "BQT:315",
          "words": [
            {"translit": "bŭrq", "gloss": "white, shining", "script": null}
          ],
          "script_extra": null,
          "note": "TAD:14 links this word to the Arabic root \"B.r.q: shines\".",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "PHN:71",
          "words": [
            {"translit": "borax", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:152",
          "words": [
            {"translit": "borax, boric, Boron", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:471",
          "words": [
            {"translit": "bavarak", "gloss": "beaver", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:471",
          "words": [
            {"translit": "babar", "gloss": "beaver, red fox", "script": "بَبَر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:158; AHD",
          "words": [
            {"translit": "brŭnaz", "gloss": "brown", "script": null},
            {"translit": "bero", "gloss": "brown animal, bear, beaver", "script": null}
          ],
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
            {"translit": "brown, brunet, beaver, bear 2, Bernard", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== TOOLS ===
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
=== prior example ===
agent
page-101.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
page-68.json
page-69.json
page-70.json
page-71.json
page-72.json
page-73.json
page-74.json
page-75.json
```


## [2026-09-05T13:45:30.599Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T13:45:30.634Z] TOOL RESULT

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


## [2026-09-05T13:45:31.084Z] TOOL CALL #5: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T13:45:31.118Z] TOOL RESULT

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


## [2026-09-05T13:45:48.610Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['POK','HRN','BQT','SNS','AHD','KLN','MON','AEF','PHN','TAD','PHD','BRT','WLD','IEC','SYN','CHEUNG','ARY']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\"",
 "description": "Inspect refs_online.json for relevant abbreviations"
}
```


### [2026-09-05T13:45:50.614Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

CHEUNG MISSING

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-05T13:45:54.898Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 142 145 175; do echo \"########## POK_01 leaf-index $n (0-based? using awk NR)\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' POK_01.txt | head -60; done",
 "description": "Print Pokorny pages 133,136,166"
}
```


### [2026-09-05T13:45:56.542Z] TOOL RESULT

```
########## POK_01 leaf-index 142 (0-based? using awk NR)
sche  usw.),  lett.  beru,  bert  ds.,  im  Ablaut  intransitiv  lit.  hyi^ü^  biraii birti  , streuen,  ausfallen*,  lett.   bifstUy   biruj   bift  , ausfallen,  abfallen',   usv^
Toch.  AB  pär-  , tragen,  bringen,  holen',  vielleicht  auch  in  A  kos-prej^ ,wieviel?'  ku-pre  ,wenn',  täprem  ,wenn*,  täpär{k)  ,jetzt',  falls  zu  gr.  li-cpQa  . . ; r6-(pQ(x  , solange  als'  (S.  129).  Über  hitt.  bar-ah-zi  ,jagt'  s.  Pedersen  Hitt.  185;
Specht  will  auch  (Dekl.  148),  mit  i-  und  it-Formans,  ags.  bri-d,  birci ,junger  Vogel',  germ.  brü-tis  ,Frau,  Braut',  ai.  bhimnd-  , Embryo',  lett. braüna,  Öech.  brnka  {*bhru-nka)  ,Nachgeburt'  hierherstellen.  S.  aber  unter bh(e)reu-  , quellen'.
WP.  II  153  f.,  WH.  I  483  f.,  527,  569,  865,  866,  Trautmann  31,  E.  Her- mann Stud.  Balt.  3,  65  f.
2.  bher'  etwa  , auf  wallen',  von  quellendem  oder  siedendem  Wasser  (auch  vom Aufbrausen  beim  Gähren,  Kochen,  sowie  vom  Feuer)  »sich  heftig  be- ,     wegen';    oft  mit  in-Formans;    auch  als  schwere  Basis  bbers-  :  bhr-^ bb{e)rei-,  bb(e)rf-.    Vgl.  6.  bher-.
Ai.  bhurdti  (Hhf-e-ti)  , bewegt  sich,  zuckt,  zappelt.  Intens. ^*ar-&Äwn^i  ds.; auch:  ,züngelt,  vom  Feuer';  bhuranydti  ,zuckt,  ist  unruhig;  setzt  in  heftige Bewegung,  rührt  um,  rührt  auf;  mit  m-Formans  ai.  bhramati,  bhrämyati jirrt  umher,  dreht  sich  herum',  bhramd-h  , wirbelnde  Flamme,  Strudel', bhfmi-h  ,beweglich;  Wirbelwind'  (s.  unten  aisl.  brimi  usw.);  bh'ärni-]^ ,heftig,  zornig,  wild,  eifrig',  dürfte  als  *bhfni-  ebenfalls  auf  der  schweren' Basis  beruhen;
hierher  wohl  av.  avabaraiti  , strömt  herab',  uzbardnte  ,sie  strömen  hervor(?)',l bardnti  ayqn  ,an  einem  Tag,  wo  es  stürmt'.
Aus  dem  Gr.  7tOQq)iQ(x)  (^rcoqcpvQ lo))  , walle  auf,  woge  auf,  bin  in  unru- higer Bewegung'  (:  si.  jdrbhurlti)'^  vermutlich  auch  (pi)qo)  »vermenge,  bringe durcheinander'  (wenn  ursprgl.  vom  Durcheinanderrühren  beim  Kochen; Gdf.  Hhoviö  mit  durch  den  Labial  bedingter  w-Färbung  des  Reduktionsvo- .  kales),  wozu  q)VQd7]p  »durcheinander*,  cpvQ(.iög  »Verwirrung',  q)VQdü)  .mische, rühre  durcheinander,  knete,  verwirre'.  '
Über  lig.  und  ven.  Namen  s.  unten.
Alb.  burme  .vollreif'  (*gargekocht)  aus  *bhormo-.
Aus  dem  Lat.  wahrscheinlich /re^t^m  undfretus,  -üs  ,Wallung  des  Meeres, bes.  Meerenge;  Brausen,  Wallen,  Hitze',  fretäle  ,Bratpfanne';
fermentiim,  Gärungsstoff,  Sauerteig'  (:  ags.  beorma,  engl,  barm,  nd.  barme, woraus  nhd.  Bärme  »Bierhefe');  auch /er-uere  S.  144;
Air.  topur,  nir.  tobar  »Quelle'  (Ho-uks-boro-),  mir.  commar  =  cymr.  cymmer »Zusammenfluß'  {*kom-bero-))  lig.  FIN  Comberanea-,  mir. /o6ar  »Quelle,  unter-
#' %
133
•rdisclier  Bach*  =  cymr.  gofer  ,BacliS  bret.  gouver  ds.  {*u[p]o'bero-), cvmr.  ^6'*^  
########## POK_01 leaf-index 145 (0-based? using awk NR)
-rr-  aus  -rz-)]  *baru-ha,  -ga-  ^verschnittenes q  1  ^^ein'  (vielleicht  mit  slav.  *borv^^  auf  einem  *6äo7-w-s, verschnittenes Tier^  beruhend  und  im  Ausgang  um  -ha- :  -ga-  nach  '^farha-  ,porcus'  er- weitert) in :  ahd.  barug,  barh,  nhd.  Barg,  Barch  {Borg,  Borch),  ags.  bearg, hearh  engl,  barrow,  aisl.  -h^rgr  ^verschnittenes  männliches  Schwein^  (dazu auch  siisl.  val-bassi  ^wilder  Eber^  als  *barh-s-an?  s.  Falk-Torp  u.  basse  N.); ahd.  as.  borön,  ags.  borian,  aisl.  bora,  -ada  ,bohren^  (s.  o.);  ahd.  bora Bohrer^^  ags.  bor,  byres  ds.;  aisl.  bora  ,Loch^  (auga-,  eyra-bord),
Lit.  bäras,  lett.  öars  ,Getreideschwaden^;  lit.  baru  (und  bariü),  bdrti schelten,  schmähen^^  refl.  _,sich  zanken^^  lett.  baru,  bäru,  bärt  ^schelten^ (=r  sl.  borjq),  lit,  barms  (Akk.  bafni)  ,Zank^  (=  aksl.  bram)]  lit.  burnä Mund^  =  bulg.  birna  ,Lippe^  (Gdf.  Hhornä,  vgl.  oben  ir.  bern  und  zur Bed.  arm.  beran).
Hierher  mit  halt.  Formans  5:  lett.  berzt  ^reiben,  scheuernVintrans.  birzt zerbröckeln^,  birze  ,Saatfurche^^  lit.  birBs  f.  ,Ackerfurche^
Mit  einer  Grundbed.  ^kerben' :  lit.  bürtai  PL  ^Los,  Zauber^  =  lett.  burts jZeichen  des  Zauberers,  Buchstabe^,  lit.  bürti  ^zaubern^,  lett.  buft  ,zaubern^, huftains  ,mit  Kerbschnitzerei  versehen^;  gr.  q)ao(xay.ov  ^Heilmittel,  Zauber- mittel^  (wohl  nichtidg.)  hat  nichts  damit  zu  tun.
Aksl.  horjg,  brati  ,kämpfen^  (häufiger  reflexiv),  russ.  borjü,  borötb  ,be- zwingen,  niederwerfen^,  refl.  ,kämpfen',  poln.  dial.  bi^öc  si^  ,ringen^;  aksl. bi-arib  ,Streit,  Kampfe,  aruss.  boronh  ,Kampf^,  russ.  börowb  ,Verbot^,  cech. hrah  ,Waffe,  Rüstung^  u.  dgl.,  russ.  za-bör  ,Zaun,  Plankenzaun^  (wie  lat. forus  auf  den  Begriff  ,Brett^  zurückweisend:  vgl.  russ.  alt.  zaborolo  ,höl- zerne  Stadtmauer,  Gerüst^,  cech.  zdbradlo  , Geländer,  Brustwehr^  u.  dgl.); russ.  borond  ;,Egge^,  und  mit  slav.  -2;c?a-Formans  slav.  *borzda  in  aksl. brazda,  russ.  borozdd  ,Furche^;  russ.  börov  ,Borg,  zahmer  Eber^,  skr.  brav jSchafvieh*",  mdartl.  ,geschnittenes  Schwein^,  slovak.  brav  ,verschnittener Eber^,  poln.  mdartl.  browek  ,gemästeter  Eber^  (s.  oben  germ.  *baruha-)- *b^rth  ,Bohrung,  Höhlung^  (*bhorti-)  in  russ.  borth  ,hohler  Baum,  worin sich  Bienen  eingenistet  haben'  usw.
Vgl.  die  verwandten  Wurzelformen  bheredh-,  bhrei-  (bhreig-,  
########## POK_01 leaf-index 175 (0-based? using awk NR)
iqvqfj  ds.; bhrätrya-m:  gr.  cpQaTqla,  aksl.  bratThja^  bratbja  ds.,  lat.  frätHa   ,Frau  de Bruders'.
Toch.  A  pracar  (Dual  pratri),  B  procer.
WP.  II  193,  WH.  I  541  f.,  866,  Specht  KZ  62.  249.  Fraenkel  REtlE 6  f.,  Risch  Mus.  Helv.  1,118.
bhred{h?)-  .waten',  im  Bsl.  auch  .plantschen,  die   Zeit  vergeuden;   Unsi schwatzen';  bhrod(h)0'S  ,Furt'.
Thrak.  ON  BqsSccl]  lig.  VN  Brodionti:  vgl.  gall.  FIN  Bredamia,  t La  Brenne,  ON  Bgodevria  (Bayern).
Alb.  bretJi,  Aor.  brodha  ,hüpfen'.
Lit.  bredü  (ostlit.  brendu),  bridau,  bristi  ,waten',  Iter.  braddu,  -yti  ,waten' brastä,  brastvä  .Furt  (kotige)',  bradä  .Schlamm',  brädas  m.  ,Fischfang' (^=  slav.  brod%),  mit  sek.  Ablaut  brydis  m.  .das  Waten,  Gang  ins  Wasser'. ter.  braidaüj  -yti  .fortgesetzt  umherwaten';  lett.  brienu  (mdartl.  binedu =  ostlit.  brendü),  bridu,  brist,  Iter.  braddt  ,waten;  mit  Füßen  treten; Albernes  sprechen',  braslis  m.  ,Furt',  bridis  m.  ,Weile,  kurze  Zeit';  apr. Chucunbrast  ,des  Teufels  Durchfahrt';  Schwundstufe  ir  =  *2'  noch  in  lit. bii'dä  ,nasser  Kot',  apr.  Birdaw,  Seename.
Russ.-ksl.  breduy  bresti  .durch  eine  Furt  waten'  (tiefstufig  Präs.  *brhdg in  neprebrhdorm  .nicht  durchwatbar'.  Aor.  pribrhde,  vgl.  aöech.  'pHbrde .wird  durchwaten',  poln.  brnci6  .waten'  aus  *brtdn(^ti),  russ.  bredü,  hresti .langsam  gehen,  mit  dem  Zugnetz  fischen',  breditb  ,Unsinn  schwatzen, phantasieren',  bred,  bredina  .Weide'  (,da  oft  im  Wasser  stehend'),  r.-ksl., russ.  (usw.)  brod^  .Furt',  iter.  r.-ksl.  broditi  .waten',  russ.  broditb  ,langsam gehen,  schleichen,  umherschweifen;  gären',  skr.  brbditi  ,waten'.
WP.  II  201  f.,  Trautmann  37,  Mühlenbach-Endzelin  332  f.
165
bbfeg'  ;brechen;  krachend A.i.  girt-hhrdj-  ^aus  den  Bergen  hervorbrechend';
lat.  frangö,  -ere,  fregi  ( :  got.  *brekum),  fräctum  ^brechen,  zerbrechen, beu^en^;  fragüis  , zerbrechlich^  usw.  (*bh\g-),  fragor  m.  ,das  Zerbrechen, Krachen,  Getöse';  mit  ä  (nach  fräctiis  usw.):  suffrägium  , Abstimmung, lärmender  Beifall,  Zustimmung';  siiffrägines  f. , Hinterbug  der  Tiere',  eigentl. ,Biegung-;  Knick';
mir.  hraigid  , furzt',  Verbaln.  braimm^  cvmr.  corn.  b7'am  m.  ,Furz',  mir. t-air-brech  ,Krachen';  aber  gall.  bräca  Kniehose  (vgl.  ßQÜy.Kac  aXyaiai Sicfd-egcci  TTaqä  KsXzolg  Hes.)   ist  germ.  Lw.,  air.  bröc  ,Hose'  ist  ags.  Lw.
o-ot.  brikan,  as.  brekan,  ags.  brecauy  ahd.  brehhan  ,brechen'  (lat.  fregimus =  got.  *brekiom,  nhd.  brachen),  ablaut.  got.  brakja  ,Ringkampf';  dehn- stuf, mhd.  brache  f.  , Umbrechung  des  Bodens,  nach  der  Ernte  unge- brochen liegendes  unbesätes  Land',  ags.  ä-b
```


## [2026-09-05T13:46:10.137Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== bher 3 headword ===\" && grep -n \"scharfem  Werkzeug\\|scharfem Werkzeug\" POK_01.txt POK_full.txt | head -10; echo \"=== bhrei ===\" && grep -n \"bhrei\\|bhr\\^ei\\|bhrëi\\|bhr[eē]i-\" POK_01.txt | head -20; echo \"=== glänzend hellbraun ===\"; grep -n \"hellbraun\" POK_01.txt | head -20",
 "description": "Grep Pokorny for bher-3, bhrei-, bher-5"
}
```


### [2026-09-05T13:46:10.216Z] TOOL RESULT

```
=== bher 3 headword ===
POK_01.txt:2391:bbrei-,  bhri-  Erw.  von  bher-  ,mit  scharfem  Werkzeug  schneiden,  usw.'.
POK_01.txt:2456:I»  bbreu-,  bbru-  Erw.  von  bher-  ,mit  scharfem  Werkzeug  schneiden,  ab- schaben usw.',  bes.  germ.  ,zerschlagen,  brechen';  bbrü-no-  (bhrou-no-) ,die  beim  Auskriechen  abgestoßene  Hauf^.
=== bhrei ===
1875:Vgl.  die  verwandten  Wurzelformen  bhereg-  ,kocben*,  bhereu-  , wallen*, bhreics-  , schwellen*,  bhrig-,  bhrüg-  , kochen,  braten*.
1907:Vgl.  die  verwandten  Wurzelformen  bheredh-,  bhrei-  (bhreig-,  -k-,  s.  dort auch  über  bherg-),  bhreu-,  bhreu-q^-,  -k-  _,schneiden',  bhreus-  ,zerbrechen', hherug-  ^Schlund^
2388:Eine  analoge  ^-Erw.  von  einer  i-Basis  bhrei-  könnte  allenfalls  vorliege^ in  norw.  brikja  ,hoch    emporragen;    prangen,  glänzen',    brik  ,eine  große den  Kopf  hoch  tragende  Frau',  briken  ,frisch,  lebhaft;  prächtig,  glänzend angenehm',  bi-ikna  ,Herrlichkeit,  Glanz,  Freude'  (Wood  KZ.  45,  66),  went nicht  etwa  ,glänzen,  hervorleuchten'  die  Grundlage  dieser  Bedd.  ist.
2389:Ein  bhrei-k-  vermutlich  in  gr.  (pgt^j  -xdg  ,das  Schauern,  Aufschauder^ Starren',  cpqtaau),  -Trw,  7te(pqly.a  ,emporstarren ;  schauern';  cymr.  bret.  h ,Gipfel'  (Hhnko-).
2397:Hierzu  wohl  auch  cymr.  brtoydr  , Kampf,  air.  briathar  ,Wort'  als *bhrei-trä  , Streit,  Wortstreit'  (zu  cymr.  brwyd  ,zerrissen,  durchlöchert'), vgl.  lit.  bdrti  , schelten',  refl.  ,sich  zanken',  aksl.  brati  ,kämpfen',  s.  2.  bher-^
2402:'^-Ervv.  bhrei-g-  vermutlich  in  lit.  brUiu,  bresti  , kratzen',  Iter.  braizau,
2404:'tri    die  mit  *bhrei-g-  parallele  g'-Erw.  der   einf.  Wz.  bher-  in  lett.  berzu^
2406:nf    eine    ^-Erw.    ^bhrei-k-    zurückfiihrbare    gr.    (fgUsg'    xd^axsg    Hes.;
2485:air.  brau  , zerschmettere,  zerschlage^  {*bhrüsiö,  gall.  brus-,  frz.  bruiser),  mir. brüire,  brüile  , Bruchstück^,  bruan  ds.,  bruar  ,Bruchstücke^,  brosna  (*brus- tonio-)  ,Reisig'bündeF,  galL  *bruskiä  ,Gestrüpp',  afrz.  broce  ds.,  mir.  brusc ,Krümchen*  usw.;  air.  bronnaim  ,schädig"e^  (*bhrusnämi)  (Subjunktiv  robria von  *bris-  ,brechen^  entlehnt,  s.  unter  bhrei-)]  mcymr.  breu,  ncymr.  brau jgebrechlich^,  mcorn.  bre^o  ,g*ebrochen^  (*bhrönso-)]  mbret.  briisun  ,Krüm- chen^  (*brous-t-)]
2498:Russ.-ksl.  obrezgnuti,  obrhzgnuti  ,sauer  werden',  cech.  bresk  ,herber  Ge-^^ schmack',  poln.  brzazg  ,unangenehmer,  herber  Geschmack;  üble  LauneVgl^ russ.  brezgdth  (alt  brezgati)  ,sich  ekeln' ;  zunächst  zu  norw.  bj^isk  ,bitterer  ^^: Geschmack',  brisken  ,bitter,  herbe';  wohl  zu  bhrei-  ,schneiden'  (wie  mndl.  Ji; brine  ,Salzwasser').  V.
=== glänzend hellbraun ===
1916:5.  bher-  ^glänzend,  hellbraun^:  bhero-s,  bberu-s,  vielfach  von  brauneu Tieren;  redupl.  bhe-btru-s,  bhe-bhro-s  ,braun;  Biber^;  flo-Bildun- gen :  bhre-no-,  bhro-no-  und  (*bheru-s :)  bhrou-no-,  bhrü-no. ,braun^.
```


## [2026-09-05T13:46:14.810Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1878,1912p' POK_01.txt",
 "description": "Pokorny bher-3 entry"
}
```


### [2026-09-05T13:46:14.874Z] TOOL RESULT

```
spalten;  bhoros  , Abschnitt,  zu  Planken  geschnittenes  Holz^
Ai.  (gramm.)  bhfnäti(7)  ,versehrt*^  =  npers.  burrad  ,scbneidet';  av.  tizi-
bära-  ,mit  scharfer  Schneide^  (=  arm.  bir,  vgl.  auch  alb.  borigle));  vielleicht
hierher  ai.  bhdrvati  ,kaut,  verzehrt^  (av.  baoirya-  ,was  gekaut  werden  muß,
134
fest^^  haou7'va-  ^kauend^)  aus  *bharati  durch  Einfluß   von   ai.  cdrvati  ,zer. kaut^  umgestaltet.
Arm.  heran  ^Mund'^  (ursprgl.  ^Spalt,  Öffnung^)^  -hir  ^aufgrabend"^  in  getna\ erkra-,  hola-bir  ,den  Boden  aufgrabend,  durchwühlend^  (Hhero-),  dazi brem  (*birem)  ^grabe  auf,  höhle  aus,  bohre  auf^,  br-ic  ,Hacke^;
bah,  Gen.  -i  ,Spaten^  {^bTif-ti-f  vielleicht  *bhorti-  =  russ.  borth),  6or^ Gen.  -oy  ,Schorf^
Gr.  *9}a(;w  , spalte,  zerstückele^  (ya^traf  oxlaai  EM),  ya^dw, pflüge* (==  ahd.  borön),  cpdoog  n.  ,Pflug,  Pflügen  (?)^^  m.  =  qxxovy^  (Hhevos),  ^'ya^ogl ,ungepflügt^,  cpagayS  ,Fels  mit  Klüften,  Schlucht^  (dazu  rom.  barraui ,Schlucht'^,  M.-L.  693a),  jon.  (pagaog  n.  ,abgerissenes  Stück,  Teil*;  hierbei vielleicht  q>doY.oq  m.  ,Mooszotten*  als  "^cpaga-Tiog.  Eine  Ä;-Erw.  in  ya^xu ,Runzel*,  (pOQy.6g  ,runzelig*  Hes.
Vielleicht  hierher  (IJ.  13,  157  n.  100)  mak.  ßiQQO^'  daav  (vgl.  ßiQQCj&fjvai raTtSLvcüd-fjvai  Hes.),  Grundbed.  ,Wollzotte*,  gr.  lesb.  thess.  ßeggöv  6aa^^ dor.  ßsiQOv  ds.,  ßsgßsQiov  , ärmliches  Kleid*,  lat.  burra  f.  ,zottiges  Gewaad'j bzw.  ,Wolle*,  reburrus  ,widerhaarig*.
Alb.  bie  (2.  pl.  birni,  Imp.  biera)  , klopfe,  schlage,  spiele  ein  Instrument; falle  (schlage  hin)*.
Alb.  brime  ,Loch*  (*bhj'-ma),  bire  ds.  (*bhera),  ^eg.  brej,  tosk.  brenß ,nage,  streite*;  britme  ,September  und  Oktober*  (wenn  eig.  ,Ernte,  Herbst^y auf  Grund  von  *bhr-ti-  ,das  Schneiden*);  brese  ,bittere  Wurzel,  Zichorie' (,bitter*  =  ,schneidend*;  -se  aus  -tiä,  borig(e))  ,Splitter,  Span*  {^bher-  m^ Form.  -ige).
Lat./eHö,  -Ire  ,stoßen,  hauen,  schlagen,  stechen,  treffen*  (s.  auch  WH.  1 481 zu  ferentärius  ,Wurfschütze,  Plänkler*).  Über  forma  ,Form,  Gestalt*  s: WH.  1530  f.
forö,  -äre  ,bohreu,  durchbohren*  (Bed.  wie  ahd.  borön,  aber  im  Ablaut verschieden;  Denominativ  von  einem  *bhorä  ,das  Bohren*), /o7'äme»  ,Loch*p forus,  -l  ,Schiffsverdeck;  Bretter,  Fächer  für  Bienenkörbe;  Sitzreihen  im Theater;  Spielbrett*;  aber  /o?'wm  (alat.  auch /orits)  ,Marktplatz*  nicht  als ,umplankter  Raum*  hierher  (umbr.  furo,  für u  ,forum*);  s.  unter  dhuer-.
Mir.  bern,  berna  f.  ,Kluft,  Schlitz*,  bernach  ,zerklüftet*;
wohl  auch  mir.  bairenn  ,Felsstück*  (dazu  bairnech  ,Tellermuschel'): air.  barae,  mir.  bara  (Dat.  barainn)  ,Zorn*,  bairnech  ,zornig*,  cymr.  bar. baran  ,Zorn*.
Aisl.  berja  (Prät.  barda)  ,schlagen,   stoßen*,   berjaslc  ,kämpfen*,   bardagf.
,Schlacht*,  ahd.  berjan,  mhd.  berjen,  bern  ,schlagen,  klopfen,  kneten*,  ags.
■  hered  ,niedergeschlagen*  (germ.  *barjan.=  slav.  borj(^),  afries.  ber  ,Angriff*;
mhd.  bnr  f.  ,Balken,  Schranke,  eingehegtes  Land*  (:  lat.  forvs,  -um),   engl.
bar  ,Schranke*,  aisl.  berlings-äss  ,Balken*;   germ.   ist  wohl   (anders  Wart-
^1
■^ ^
135
u  rcr  l  260)  auch  mhd.  har7^e  ^»Balken,  RiegeF  und  die  rom.  Sippe  von f  2  barre,  barrih-e  usvr.  (-rr-  aus  -rz-)]  *baru-ha,  -ga-  ^verschnittenes q  1  ^^ein'  (vielleicht  mit  slav.  *borv^^  auf  einem  *6äo7-w-s, verschnittenes Tier^  beruhend  und  im  Ausgang  um  -ha- :  -ga-  nach  '^farha-  ,porcus'  er- weitert) in :  ahd.  barug,  barh,  nhd.  Barg,  Barch  {Borg,  Borch),  ags.  bearg, hearh  engl,  barrow,  aisl.  -h^rgr  ^verschnittenes  männliches  Schwein^  (dazu auch  siisl.  val-bassi  ^wilder  Eber^  als  *barh-s-an?  s.  Falk-Torp  u.  basse  N.); ahd.  as.  borön,  ags.  borian,  aisl.  bora,  -ada  ,bohren^  (s.  o.);  ahd.  bora Bohrer^^  ags.  bor,  byres  ds.;  aisl.  bora  ,Loch^  (auga-,  eyra-bord),
Lit.  bäras,  lett.  öars  ,Getreideschwaden^;  lit.  baru  (und  bariü),  bdrti schelten,  schmähen^^  refl.  _,sich  zanken^^  lett.  baru,  bäru,  bärt  ^schelten^ (=r  sl.  borjq),  lit,  barms  (Akk.  bafni)  ,Zank^  (=  aksl.  bram)]  lit.  burnä Mund^  =  bulg.  birna  ,Lippe^  (Gdf.  Hhornä,  vgl.  oben  ir.  bern  und  zur Bed.  arm.  beran).
Hierher  mit  halt.  Formans  5:  lett.  berzt  ^reiben,  scheuernVintrans.  birzt zerbröckeln^,  birze  ,Saatfurche^^  lit.  birBs  f.  ,Ackerfurche^
Mit  einer  Grundbed.  ^kerben' :  lit.  bürtai  PL  ^Los,  Zauber^  =  lett.  burts jZeichen  des  Zauberers,  Buchstabe^,  lit.  bürti  ^zaubern^,  lett.  buft  ,zaubern^, huftains  ,mit  Kerbschnitzerei  versehen^;  gr.  q)ao(xay.ov  ^Heilmittel,  Zauber- mittel^  (wohl  nichtidg.)  hat  nichts  damit  zu  tun.
Aksl.  horjg,  brati  ,kämpfen^  (häufiger  reflexiv),  russ.  borjü,  borötb  ,be- zwingen,  niederwerfen^,  refl.  ,kämpfen',  poln.  dial.  bi^öc  si^  ,ringen^;  aksl. bi-arib  ,Streit,  Kampfe,  aruss.  boronh  ,Kampf^,  russ.  börowb  ,Verbot^,  cech. hrah  ,Waffe,  Rüstung^  u.  dgl.,  russ.  za-bör  ,Zaun,  Plankenzaun^  (wie  lat. forus  auf  den  Begriff  ,Brett^  zurückweisend:  vgl.  russ.  alt.  zaborolo  ,höl- zerne  Stadtmauer,  Gerüst^,  cech.  zdbradlo  , Geländer,  Brustwehr^  u.  dgl.); russ.  borond  ;,Egge^,  und  mit  slav.  -2;c?a-Formans  slav.  *borzda  in  aksl. brazda,  russ.  borozdd  ,Furche^;  russ.  börov  ,Borg,  zahmer  Eber^,  skr.  brav jSchafvieh*",  mdartl.  ,geschnittenes  Schwein^,  slovak.  brav  ,verschnittener Eber^,  poln.  mdartl.  browek  ,gemästeter  Eber^  (s.  oben  germ.  *baruha-)- *b^rth  ,Bohrung,  Höhlung^  (*bhorti-)  in  russ.  borth  ,hohler  Baum,  worin sich  Bienen  eingenistet  haben'  usw.
Vgl.  die  verwandten  Wurzelformen  bheredh-,  bhrei-  (bhreig-,  -k-,  s.  dort auch  über  bherg-),  bhreu-,  bhreu-q^-,  -k-  _,schneiden',  bhreus-  ,zerbrechen', hherug-  ^Schlund^
WP.  II  159  f.,  WH.  I  481  f.,  537,  865,  866,  Trautmann  27,  Mühlenbach- Endzelin  354.
4-  hher-  in  Schallworten  ,brummen,  summen'^  u.  dgl.
Arm.  bor,  -oy  ,Hummel,  Hornis^,  zum  redupl.  ai.  bambhara-h  (unbel.) jBiene^,    bambharälih    (unbel.)    ,Fliege',    bambhä-rava-h    ,das    Brüllen    der
136
Kühe^,   gr.  7t€!xq)Qr]öd)y   ,Art  Wespe^   (Bildung    wie  ävS-gr^dibv^   rsv&Qr]d(üp) ähnlich  auch  skr.  hümbar  ,HummeF,  klr.  bombär  .Maikäfer^
```


## [2026-09-05T13:46:15.430Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1916,1960p' POK_01.txt; echo \"=====BHREI=====\"; sed -n '2391,2410p' POK_01.txt",
 "description": "Pokorny bher-5 and bhrei- entries"
}
```


### [2026-09-05T13:46:15.480Z] TOOL RESULT

```
5.  bher-  ^glänzend,  hellbraun^:  bhero-s,  bberu-s,  vielfach  von  brauneu Tieren;  redupl.  bhe-btru-s,  bhe-bhro-s  ,braun;  Biber^;  flo-Bildun- gen :  bhre-no-,  bhro-no-  und  (*bheru-s :)  bhrou-no-,  bhrü-no. ,braun^.
Ai.  bhalla-k,  bhallaka-h  bhalVäka-h  ^'i.v'  (-11-  aus  -rl-)]  ahd.  bero^  ags. bera  ,Bär^  (*bheron-)j  aisl.  bigrn  ds.  (*bhernu-,  dessen  u  wie  das  n  von ai.  bhalVAka-h  aus  dem  St.  *bheru-  stammen  mag)  =  ags.  beorn  ,Krieger^ Häuptling';  aisl.  bersi  ,Bär^  (s  wie  in  Fuchs:  got.  fauhö,  Luchs:  schwed. lo)\  ablaut.  lit.  beras,  lett.  b^rs  ^braun  (von  Pferden)^;
gr.  gxxQT]'  vecpeXai  Hes.?  (*(paQe[(j]a  oder  *(paQ€J^a?  Letzternfalls  genau zu:)  (paQvvsL'  ka^rtgvvsL  Hes..,  (fQ'tvri^  (pQvvog  ^Kröte,  Frosch^  (*^die  braune^ =  ahd.  brün)]  ob  g)aor]  als  ^Wolkendecke^  zu  7.  bher-?
nep.  bhuro  ,braun^  (*bhrüro-)j  ahd.  mhd.  brün  ^glänzend,  braun^,  ags. brün,  aisl.  bränn  ds.;  russ.  mdartl.  brynä'th  ,weiß,  grau  schimmern^,  ab- lautend bruneth  ds.  (*bhrou-no-?)  und  (aus  *bhr-ono-,  -eno-)  russ.-ksl.  brom -  , weiß;  bunt  (von  Pferden)^^  russ.  bronv  (und  mdartl.  brynh),  klr.  brenity jisXh  werden,  reifen^,  aksl.  brhnije  (brenije)  ,Kot^,  slov.  brn  ^Flußschlamm';
ai.  babhrü-h  ^rotbraun;  große  Ichneumonart',  av.  baivra-,  baicri-  ,Biber'; lat.  fiber,  fibrl  ,Biber'  (auch  feber  s.  WH.  I  491;  wohl  i  geneuert  für  e, wie  auch)  kelt.  (nur  in  Namen):  *bibros,  *bibrus  in  gall.  ON  und FIN  Bibracte,  abrit.  VN  Bibroci^  mir.  VN  Bibraige  (*bibru-rigion),  PN Bibar  {*Bibrus)  neben  *bebros  in  gall.  FIN  *Bebrä,  frz.  Bievre]  Bebromiäj frz.  Beuvo'onne,  Brevenne  usw. ;  ahd.  bibar j  ags.  beofor  (ältest  bebr),  mnd. bever,  aisl.  biörr  ds.  (urg.  *SeSrw-);  vgl.  auch  nhd.  FIN  Bever,  alt  Biverna-,
lit.  bebras,  bäbraSj  bebrus  ds.  (dissimil.  debrüs  u,  dgl.),  apr.  bebrus  ds.; über  lit.  bruXsis  usw.  ,leuciscus  rutilus',  apr.  brun-se  ds.  s.  Specht  Dekl.  120;
slav.  ^bebr-b  in  poln.  FIN  Biebrza,  russ.  usw.  bobr  (zur  o-Red.  s.  Ber- neker  47;  daneben  vielleicht  *bhbi^  in  skr.  däbar  ,Biber'  und  aruss.  be- hrjam  ^aus  Biberpelz').    Vgl.  noch  \siX,  fibrinus  ,vom  Biber',  volsk.  Fibre-
137
Bachname,    av.    hawraini-   jVom   Biber^;    ahd.    bibarln,    gall.   lehrinus (Schol.  luv.),  lit.  hebrinis  ds.;
^t  eil   B  verne,  A  |?arno  ^leuchtend^,   davon  B  perwe,   A  -paräm  ,Würde^ Erweiterungen   unseres   hher-  scheinen   hhereg-,   bherek-  .glänzend    Vgl. ferner  L  bhel-  mit  ähnlicher  Bedeutung.
WP.  11  166  f.,  WH.  I  490  f.,  Van  Windekens  Lexique   93.
g  bher-   mit  ^-Erweiterungen,   wovor   z.  T.   i-,   w- Vokale,   ^rösten,   backen^ kochen^ ijjvon  2.  bher-  ,sich  heftig  bewegen,  Avallen,  kochen^  abgeleitet.
1.  Formen  ohne  -i-  oder  -u-:   bhereg-:
Ai.   bhurdjanta  ,kochend^  (*bh,reg-);    bhrjjdti  ,röstet^,  bhrsta-h  ,geröstet,
crobraten^,  bhrUstra-h  yRöst^iamne^   bkarj{j)ayati  ,röstet,  brät',    bharjana-k
röstend,   bratend',   mpers.  barstan  ds.;  vermutlich  ist  *bhraz-  (*bh\raz-  in
bhurdjanta),  *bharz-  die  ar.  Wurzelform  und  ind.  -jj  nur  im  Präs.  *bhig-
skö,  woraus  *bhx(g)sgö  entstand,  wie  gr.  filayo)  aus  *(XLy-a'Au).
Lat.  fertum  ,eine  Art  Opferkuchen',  alat.  ferctum  {firctum,  s.  Ernout El.  dial.  lat.  165),  Partiz.  eines  *fergö  ,backe',  osk.  fertalis  ,Zeremonien;^ bei  denen  Opferkuchen  gebraucht  wurden'.
Lit.  birgelas  ,einfaches  Bier',  lett.  birga  , Dunst,  Qualm,  Kohlendunst'^ apr.  aubirgo  ,Garkoch',  birgaharkis  ,ein  größerer  Schöpflöffel'  (mit  ven.- illyr.  g).
2.  Formen  mit  i,  ei:
Npers.  biris-tan  ,braten',  b'^rezan  ,Backofen',  bal.  brejag,  bHjag  ,braten', npers.  biryän  (*brigäna-)  ,gebraten',  pam.  (umgestellt)  icirzam  ,röste,  brate' u.  dgl.  (iran.  *brij-y  *braij-).
Lat.  frlgöj  -ere  ,rösten,  dörren',  umbr.  frehtu  ,gekocht'.
3.  Formen  mit  w:  bbrüg-:
^v.  (pQ'öyaj  ,röste,  dörre,  brate',  g)QV7iTÖg  ,geröstet;  Feuerbrand',  (pqtyavov ,dürres  Holz',  q)QiysTQOv  ,Gefäß  zum  Rösten  von  Gerste'.
Merkwürdig  ist,  daß  in  den  Schallsippen  von  gr.  q)QvyiXog  ,ein  Vogel', iRt.frigö  ,quietsche',  poln.  bargiel  ,Bergmeise',  russ.  berglezz  ,Stieglitz'  die Verteilung  der  Formen  mit  u,  mit  i,  und  ohne  beides,  dieselbe  wie  in den  Worten  für  kochen  ist.
WP.  II  165 f.,  WH.  I  486  f.,  548 L
7-  bher-  ,flechten,  weben'?  bb^u-  , Gewebe'.
Hom.  (pagog  =  att.  cpäqog  n.  {^cpaqfog)  ,Tuch,  Leinwand,  Hülle,  Decke'; (potQai  Q)' vq)aivuvyTc'ki'AELvllQs.'^  yo^^uog  , Tragkorb,  Matte';
lit.  burva  ,eine  Art  Kleidungsstück',  lett.  burves  PI.  ,kleine  Segel'  {-u-
138
Suffix  wie  in  gr.  *cpaQJ^og),  lett.  buras  ds.,  lit.  büre  ,Segel^  S.  zum  Vpka^ lisinus  Walde  Streitberg-Festschrift  176. WP.  II  164,  Specht  Dekl.  182.
bberedh-  ^schneiden',  bhrdho-  ,Brett^
Ai.  bardhaka-h  ^abschneidend,  scherend',  m.  ^Zimmermann',  sata-bradl^ na-h  ,100  Metallspitzen  habend';  vielleicht  gr.  tceq&u)  ^zerstöre',  noq^eii ^zerstöre,  verwüste';
bhredbos-  in   as.   ags.   bred  ,Brett',  ahd.  bret   n.,    davon   ahd.    britissc nhd.  Pritsche]
bhrdho-  in   got.  fötu-baürd  n.   ,Fußbrett',   aisl.   bord  n.  , Brett/ Tisch* ags.  bord  n.  ds.,   ahd.  bort  ds.  =  umbr.  forfo-   ds.  in  furfant  ,sie  legeo] auf  das  Brett';  wohl  damit  identisch  aisl.  bord  ,Rand,  Kante,  Schiffsrand' ahd.   mhd,    bort   ds.   (nhd.   Bord  aus   dem   Ndd.),  ags.   bord  ,Bord,  Rand; Schild';  ags.  boi-da  m.  ,Rand,  Verzierung',  ahd.  bortOj  nhd.  Borte-,
bhordhO'  in  aisl.  bard  ,Rand,  Kante',  norw.  dial.  bard  ds.
Aus  germ.  *burd-  stammen  skr.  brdo,  russ.  berdo  usw.  ,Weberkamiii^ und  lett.  birde  f.  , Webergestell'.
WP.  II 163, 174,  Devoto  Mel.  Pedersen  227  f.,  Meillet  Slave  commun«  75j
bhereg'  in   Schallworten  ,brummen,  bellen,  lärmen  u.  dgl.',  vgl.  bher-  ds sowie  die  bei  bhreg-  ,brechen'  und  ,krachen'  begegnende  Schallbedeutung
Ags.  beorcan  St.-V.,  bearkian  (*barkön),  engl,  bark  ,bellen',  aisl.  berkja ,bellen,  poltern,  toben';
lit.  (zem.)  burgeti  ,brummen,  zanken,  unfreundlich  sein',  burgesus ,Brummbart';  vermutlich  auch  skr.  brgljati  , murmeln,  schwatzen',  brgalica ,Turteltaube'.
Daneben  ähnliches  bhereq- :  lett.  brecu,  br^kt  , schreien',  russ.  breiü, brechdth  ,kläffen,  schreien,  zanken,  lügen',  brechnjd  , leeres  Geschwätz', skr.  bresem,,  brehati  , keuchen,  laut  husten'  (^bhreq^-s-),  brekcem^  brektati ,schnauben'.
Etwas  verschieden  wegen  der  helleren  Schallvorstellung  sind  folgende W^orte,  die  in  ihrem  teil  weisen  i-  und  n -Vokalismus  an  die  bei  bher(e)g- ,rösten'  A'orliegenden  Vokalverschiedenheiten  erinnern,  die  aus  verschie- dener Schallnachahmung  erklärt  werden:
gr.  q}QvyiXog  ,ein  kleinerer  Vogel'  (Umstellung  aus  *g)QiyvXoQ:  lat./ri^-?);
=====BHREI=====
bbrei-,  bhri-  Erw.  von  bher-  ,mit  scharfem  Werkzeug  schneiden,  usw.'.
Ai.  bhrlndnti  ,sie  versehren'  (Pf.  blbhräya  Dhätup.),  av.  pairibinmnti ,sie  schneiden  ringsum',  bröid-rö-taeza-  , scharfschneidig',  mpers.  brin jbestimmt'.
Thrak.  (?)  ßqilibv  ,Barbier'.
Lat.  friö,   -äre   , zerreiben,    zerbröckeln',  fricö,   -äre    , reiben,    abreiben'.^ (von  einem  *fri-co-s  , reibend,  schabend'),  refrlva  faba  , geschrotete  Bohne' j1 fmvolus    (aus  *fri-vo-s    , zerrieben'),    ,zerbrechlich,    wertlos,    fade,   nichtig*.-;
Mit  frlvolus  zu  vergleichen  ist  cymr.  briic  , zerbrochen;  Wunde*;  bHwo. ,zerbrechen,  schädigen' ;
mit  s-Erweiterung  hierher  gall.-lat.  brisäre  ,frangere',  frz.  bHser  usw.| gallorom.  *briscäre  , gerinnen',  Schweiz,  bretschi  ds.  (Wartburg),  air. brissid  ,bricht'  (vom  Partiz.  Perf.  *bristo-),  mir.  bress  f.  ,Lärm,  Kampf, breissem  ds.,  air.  PN  Bres-{iC)al  (*bristo-ualos),  com.  mbret,  bresel  »Streif, bret.  bresa  , streiten',  mir.  brise  , zerbrechlich',  br.  bresk  ds.;  vgl.  die Parallelbildungen  unter  2.  blireus-.
Hierzu  wohl  auch  cymr.  brtoydr  , Kampf,  air.  briathar  ,Wort'  als *bhrei-trä  , Streit,  Wortstreit'  (zu  cymr.  brwyd  ,zerrissen,  durchlöchert'), vgl.  lit.  bdrti  , schelten',  refl.  ,sich  zanken',  aksl.  brati  ,kämpfen',  s.  2.  bher-^
Hierher  vermutlich  mndl.  bnne,  nndl.  brijn,  mengl.  brlne,  nengl.  brine , Salzwasser,    Salzlake'    (vom   scharfen    Geschmack  wie  z.  T.  slav.    brid^).
Aksl.  britva  , Rasiermesser',  russ.-ksl.  brißi,  briti  , scheren',  bri6,  , Rasier- messer'; aksl.  brid^  ,(J^t^vg',  russ.-mdartl.  bridköj  ,scharf,  kalt!,  skr.  bridak
167
harf  sauer^;  aksl.  briselije  , Scherben*,  russ.-ksl.  bvbselije,  hi^seh  , Scherbe' '     -lav.  also  wahrscheinlich  *brhseh)  als  Hhri-d-selo-.
'^-Ervv.  bhrei-g-  vermutlich  in  lit.  brUiu,  bresti  , kratzen',  Iter.  braizau,
'/*   ds.     und   aisl.    brlk    f.  , Brett,    niedrige   Bretterwand,  niedrige  Bank';
'tri    die  mit  *bhrei-g-  parallele  g'-Erw.  der   einf.  Wz.  bher-  in  lett.  berzu^
herzu,  berzt  , reiben,  scheuern'  und   gr.  cpoqydvr]'  fj  doaioTrjg  Hes.  und  das
nf    eine    ^-Erw.    ^bhrei-k-    zurückfiihrbare    gr.    (fgUsg'    xd^axsg    Hes.;
bresti  nicht  besser  mit  idg.  b-  zu  ags.  prica  ,Punkt',  mnd.  jprickerij   mhd.
nfreclcen  , stechen'  usw.,  neben  welcher  mit  anderem  Wzlausl.  norw.  mdartl.
nrisa  , stechen,   reizen',  preima,  preina  ,necken,   reizen'  usw.   (über  Alter
und  Herkunft  dieser  germ.  Worte  steht  nichts  fest).
```


## [2026-09-05T13:47:03.680Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"###HRN p49 (leaf70)###\" && awk 'BEGIN{RS=\"\\f\"} NR==71' HRN.txt | head -40 && echo \"###HRN p59 (leaf80)###\" && awk 'BEGIN{RS=\"\\f\"} NR==81' HRN.txt | head -40",
 "description": "Horn pages 49 and 59"
}
```


### [2026-09-05T13:47:05.105Z] TOOL RESULT

```
###HRN p49 (leaf70)###
- 49 -
211. berre, bere 'Lamm*.
g. vare; semn. vara; mäz. vare; Kä§. verrd, verä,
veri,
ai. ürana- *Widder, Lamm'; phlv. varak', arm. gam
Xamm' (H. No. 64).
kurd. vark^ garik, bar/, bar/ik (H.-Sch.); af;'. vrai\
oss. d. warik^ urek, t. värjg (78) ; bei. gvarak, n. gvaraU
(137); wa;K. vurk, siyn. varg, sar. barka,
212. burrtden, burTden 'schneiden ^).
aw. V^bray-'^) 'schneiden', pairLbrinenti, pairLbrina-
fiuha; phlv. burUan (was ebenso gut auch burntan
sein kann); ai. V^bhray-, bhnndti Versehren; arm.
brem 'hacken, ausgraben, aushöhlen, zerstören' (un-
sicher, H. No. 50).
kurd. birin 'schneiden; bei. buray , n. buray (43);
wa;^. warünam^ warittam 'schneiden, mähen, scheeren'
(Tomaschek, 867, und nach ihm auch Geiger, Laut-
lehre des Balücl § 7, 2, stellen dieses Wort meiner
Meinung nach fälschlich zu skr. {/'rav-, lav-),
213. bu» *Ziege, Bock', bme (AM. S. 10, Zeile 1 v. u.), buj,
Semnän : boca 'junge Ziege' ; wohl nicht np. bece, wie
Houtum-Schindler ZDMG. 32, 535 meint.
aw. büza- 'Bock'; phlv. büj, vergl. /ar^bes:^ yßr^btj
(lies /ar]6w0, ;far]6wj'), Bund. 3); skr. vergl. btikka-
'Bock', bukka- 'Ziege'; arm. buc 'Lamm' (H. No. 60).
kurd. bizin ; af/. wuz ; bei. LW. bfiz (37) ; wa;^. buc,
bilc, sangl. wuz, minj. woza, si/n. sar. waz,
214. buzurg 'gross'.
mäz. bazarg.
*) Kä§. hürndn etc. haben secundär wieder das alte rn des Praesens
erhalten; dialektisch findet sich die Überführung in die neunte Klasse
häufig (vergl. Fr. Müller SWAW. Vol. XLV, 1864, Seite 283, Hern,
KZ. 32, 580 No. 6).
*) Bartholomae setzt Studien II, 107 Anm. 4, 180 die Wurzel
als hha^r- an, woraus hhrl- eine 'Weiterbildung' sei.
') Nach Nöldeke, Beiträge zur Geschichte des Aloxander-
romans, Denkschr. der Wiener Akad. , Band 38, Iß, ist np. x^rhitz
*Eselsziege' nach einem gr. ^ovorqayo^ gebildet.
Hörn, Grundriss d. neup. Etymologie. 4
###HRN p59 (leaf80)###
- 59 "-
)6. bese 'Wald, Dickicht', jüd.-pers. |NnDn:r^2 (Is. 2, 13).
Käs. Visa; mäz. täl. vtsi.
aw. varesa- *Wald'; phlv. vesaJc; ai. tjksd- *Bauin';
dazu gr. älaog (Bartholomae, briefl. Mitteilung),
kurd. vise (H.-Sch.).
37. bei ^Grabscheit* ^).
Käs. 6ör, böl, bäl^ berd.
Zu aw. [/^bray- schneiden' (de Lagarde, Ges. Abh.
297).
np. bei statt bäl beruht auf Imäla.
kurd. bal^ btel 'Spaten' (H.-Sch.); wa;r. bil, sar. bSil
*Spaten'.
58. blni 'Furcht'.
[bhay^ ' erschrecken , sich fürchten (aw. bai/-y ai.
bhay-), *bhänia7i- ; phlv. 6fm, blmkln,
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
ap. vainähiy Conj. (Venn) du siehst'; aw. vaenämi
*ich sehe'; phlv. ven-am, ven(i)sn^ venäk^ venastan (päz.
vm-), vergl. üben (vd. 19 (43)).
af/. vm-am; oss. d. mmin, t. ünin (82); wa;^. §iyn.
viti-am, sar. veln-am.
*) Gul. (Sprenger) S. 26 Zeile 8 reimt es ausnahmsweise auf piL
```


## [2026-09-05T13:47:07.097Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"###HRN grep buridan###\" && grep -n -i \"burîdan\\|buridan\\|bur\\-idan\\|burrad\\|brîtan\\|britan\" HRN.txt | head -20; echo \"### HRN bil ###\"; grep -n -i \"\\bbîl\\b\\|Schaufel\" HRN.txt | head -20; echo \"### HRN bor/braun ###\"; grep -n -i \"bôr\\|braunes Pferd\\|fuchsrot\" HRN.txt | head -20",
 "description": "Grep Horn for burīdan, bīl, bōr"
}
```


### [2026-09-05T13:47:07.180Z] TOOL RESULT

```
###HRN grep buridan###
### HRN bil ###
### HRN bor/braun ###
```


## [2026-09-05T13:47:20.212Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['BQT','SNS','KLN','MON','TAD','AHD','PHN']:\n    v=d[k]; print('==',k); print(' page_offset:',v.get('page_offset')); print(' lookup_hint:',v.get('lookup_hint')); print(' local:',v.get('local_file'))\n\"",
 "description": "Page offsets for BQT SNS KLN MON TAD AHD PHN"
}
```


### [2026-09-05T13:47:27.405Z] TOOL RESULT

```
== BQT
 page_offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
 lookup_hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
== SNS
 page_offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
 lookup_hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
== KLN
 page_offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 lookup_hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
== MON
 page_offset: None
 lookup_hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
== TAD
 page_offset: 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
 lookup_hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt']
== AHD
 page_offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
 lookup_hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
== PHN
 page_offset: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 lookup_hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt
```


## [2026-09-05T13:47:35.616Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### AHD bher ###\" && grep -n \"^bher-\\|^bhereg\\|^bheredh\\|^bhrei\\|^bher\\b\" AHD_watkins1985.txt | head -20",
 "description": "AHD Watkins bher roots"
}
```


### [2026-09-05T13:47:35.658Z] TOOL RESULT

```
### AHD bher ###
333:bher-1. To carry; also to bear children. 1. a. Germanic *beran in (i) Old English beran, to carry: BEAR! (ii) Old English forberan, to bear, endure (for-, for-; see per’): FORBEAR; b. Germanic *bérd in Old English bér, ber, bier: BIER; c. Germanic *bér- in Old Norse bdra, wave, billow: BORE’. 2. a. Germanic *barnam in Old English bearn, child: BAIRN; b. Germanic *barwdn- in Old Eng- lish bearwe, basket, wheelbarrow: BARROW!, 3. a. Ger- manic *burthinja in Old English byrthen, burden: BURDEN}; b. Germanic *burthiz in Old Norse burdhr, birth, akin to the source of BIRTH; C. Germanic *burja- perhaps in Old Norse byrr, favorable wind: BIRR}. 4. Compound root *bhrenk-, to bring (< *bher- + *enk-, to reach; see nek-2), in Germanic *brengan in Old English bringan, to bring: BRING. 5. Latin ferre, to carry: -FER, FERTILE; AFFERENT, CONFER, DEFER!, DEFER®, DIFFER, EFFERENT, INFER, OFFER, PREFER, PROFFER, REFER, SUFFER, TRANSFER, VOCIFERATE. 6. Latin pro- brum, a reproach (< “pro-bhr-o-, “something brought before one”; pro-, before; see per'): OPPROBRIUM. 7. Lengthened o-grade form *bhor- probably in Latin far, thief: FERRET!, FURTIVE, FURUNCLE; (FURUNCULOSIS). 8. Greek pherein, to carry: -PHORE, -PHORESIS, -PHO- ROUS; AMPHORA, ANAPHORA, DIAPHORESIS, EUPHORIA, METAPHOR, PERIPHERY, PHEROMONE, TELPHER, TOCOPH- EROL. 9. Greek pherné, dowry (“something brought by a bride”): PARAPHERNALIA. [Pok. 1. bher- 128.]
334:bher-2. To cut, pierce, bore. 1. Germanic *bordn in Old English borian, to bore: BORE}. 2. Germanic *baru-ga-, castrated pig, in Old English bearg, barg, castrated pig: BARROW’. 3. Germanic *bor-, perhaps in French burin, burin: BURIN. 4. O-grade form *bhor-d- in Latin fordre, to pierce, bore: FORAMEN; BIFORATE, PERFORATE. 5. Per- haps Greek pharunx, throat (< “a cutting, cleft, pas- sage”): PHARYNX. 6. Slavic *bor- in Russian borot’, to overcome: DUKHOBOR. See extension bhreu-'. [Pok. 3. bher- 133.]
335:bher-3. Bright, brown. 1. Suffixed variant form *bhri-no- in Germanic *briinaz in: a. Old English briin, brown: BROWN; b. Middle Dutch bruun (> Dutch bruin), brown: BRUIN; Cc. Old French brun, shining, brown: BRUNET, BURNET, BURNISH. 2. Reduplicated form *bhibhru-, *bhebhru-, “the brown animal,” beaver, in Germanic *bebruz in Old English be(o)for, beaver: BEAVER!. 3. Ger- manic *ber6, “the brown animal,” bear, in Old English bera, bear: BEAR?. 4. Germanic *bernuz in Old Norse bjérn (stem ber-), bear: BERSERKER. [Pok. 5. bher- 136.] bher-4. To cook, bake. Extended root form *bhrig- in Latin frigere, to roast, fry: FRY}. [Pok. 6. bher- 137.] bherdh-. To cut. 1. Zero-grade form *bhrdh- in Germanic *burd-, plank, board, table, in: a. Old English bord, board: BOARD; STARBOARD; b. Old Norse bordh (> Swedish bord), board, table: SMORGASBORD; c. Old French borde, hut, and bort, border: BORDELLO, BORDER. 2. Possibly Latin forfex, a pair of scissors: FORFICATE. [Pok. bheredh- 138.]
336:bhereg-. To shine; bright, white. Compare the by-form bherek-. 1. Germanic *berhtaz, bright, in Old English beorht, bright: BRIGHT. 2. “The white tree,” the birch (also the ash): a. Germanic *birkjon- in Old English birc(e), birch: BIRCH; b. suffixed zero-grade form *bhrag-s- probably in Latin fraxinus, ash tree: FRAXI- NELLA. [Pok. bherag- 139.]
```


## [2026-09-05T13:47:37.038Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN board ###\" && grep -n \"^board,\\|^border,\\|^bore,\\|^beaver,\\|^bear (\\|^bear,\\|^brown,\\|^brunette\\|^brunet,\\|^borax,\" KLN_1966.txt | head -30",
 "description": "Klein headwords"
}
```


### [2026-09-05T13:47:37.105Z] TOOL RESULT

```
### KLN board ###
4606:bear,  n.,  the  animal.  —  ME.  here,  fr.  OE.  her  a, rel.  to  MDu.  here,  Du.  beer,  OHG.  bero,  MHG. her,  G.  Bar,  ON.  bjorn,  lit.  ‘the  brown  animal’, fr.  I.-E.  *bhero-,  ‘brown’,  whence  also  Lith. beras,  Lett,  bgrs,  ‘brown’,  L.  fiber,  OE.  beofor, ‘beaver’,  lit.  ‘the  brown  animal’.  Cp.  beaver,  the animal,  and  brown.  Cp.  also  the  first  element  in Bernard.
4608:bear,  tr.  and  intr.  v„  to  carry.  —  ME.  beren,  fr. OE.  beran,  rel.  to  ON.  bera,  OFris.  bera,  Du. baren,  OHG.  beran,  ‘to  bear,  carry’,  Goth. bairan,  ‘to  bear,  carry,  give  birth  to’,  OHG.  gi- beran,  MHG.  gebern,  G.  gebaren,  Goth,  ga- bairan,  ‘to  give  birth  to’,  fr.  I.-E.  base  *bher-, whence  also  OI.  bhdrati,  ‘bears’,  bharman,  ‘sus¬ tenance,  care,  burden’,  Arm.  berem,  ‘I  bear, carry,  bring’,  bern,  ‘burden’,  Gk.  ipspeiv,  ‘to bear,  carry’,  <ptop,  ‘thief’,  L.  ferre,  ‘to  bear,  car¬ ry’,  fur,  ‘thief’.  Alb.  mbar,  bar,  ‘I  carry,  drag’, bir,  ‘son’,  OSlav.  berg,  birati  (for  earlier  bird), ‘to  bring  together,  collect,  take’,  bremg,  ‘bur¬ den’,  su-borii,  ‘assembly’,  OIr.  biru,  ‘I  carry’, W.  cymeraf  ‘I  take’,  Toch.  AB  par,  ‘to bear,  bring,  fetch’,  and  prob.  also  Toch.  B prari,  ‘finger’.  Cp.  bairn,  baron,  barrow,  ‘moun¬ tain’,  barrow,  ‘handcart’,  berth,  bier,  birth,  bore, ‘tidal  wave’,  borough,  burden,  ‘load’,  burly.  Cp. also  adiaphoresis,  adiaphorous,  afferent,  am¬ phora,  anthropophora,  Berenice,  bhat,  breba, brehon,  cataphora,  circumference,  confer,  cumber, defer,  deference,  differ,  difference,  differentiate, efferent,  -fer,  feretory,  -ferous,  ferret,  the  animal, fertile,  fortuitous,  fortune,  furtive,  furuncle,  in¬ fer,  metaphor,  offer,  opprobrium,  paraphernalia, periphery,  phoradendron,  phoresis,  Phormium, -phorous,  phosphorous,  phosphorus,  prefer,  prof¬ fer,  refer,  scirophorion,  semaphore,  Sobranje, suffer,  transfer,  varnish,  vernix  caseosa,  Vero¬ nica,  vociferate.
4629:beaver,  n.,  the  lower,  movable,  part  of  the  hel¬ met.  —  ME.  haviere,  fr.  OF.  baviere,  lit.  ‘a  bib’, fr.  baver,  ‘to  drivel,  slobber’,  which  is  of  imi¬ tative  origin.  Cp.  bavette.
5250:board,  n.,  side  of  a  ship.  —  OE.  bord,  ‘border, edge;  side  of  a  ship’,  rel.  to  OS.  bord,  LG. bo(o)rd  (whence  G.  Bord),  Du.  boord,  OHG. bort,  ON.  bard,  bord,  ‘border,  edge;  side  of  a ship’,  and  to  OE.  bord,  etc.,  ‘table,  plank’  (see prec.  word);  influenced  in  sense  by  F.  bord, ‘edge,  margin,  border,  shipboard’.  See  board, ‘table,  plank’,  and  cp.  border  and  the  second element  in  larboard.
5361:borax,  n.,  a  white  crystalline  salt  used  as  a  flux and  an  antiseptic.  —  F.,  fr.  Arab,  bauraq (VArab.  boraq),  fr.  Pers.  burah. bordage,  n.,  the  tenure  of  a  border  ( Feudal  sys¬ tem),  —  ML.  bordagium.  See  next  word  and  -age. bordar,  n.,  tenant  ( Feudal  system).  —  ML.  bor- darius,  fr.  borda,  ‘cottage’,  fr.  OF.  borde,  which is  a  Teut.  loan  word.  See  board,  ‘table,  plank’, and  cp.  border.
5363:border,  n.  —  OF.  (=  F.)  bordure,  fr.  border,  ‘to border’,  fr.  bord,  ‘a  border’,  fr.  Frankish  *bord.
5368:bore,  tr.  and  intr.  v.,  to  pierce.  —  ME.  borien,  fr. OE.  borian,  rel.  to  ON.  bora,  Swed.  borra,  Dan. bore,  OS.,  OHG.  boron,  MDu.,  Du.  boren, MHG.  born,  G.  bohren,  fr.  I.-E.  base  •bher-,  ‘to cut  with  a  sharp  point;  to  bore,  pierce’,  whence also  Arm.  beran,  ‘mouth’  (prop,  ‘opening’),  Gk. (papaco,  <pap6ca,  ‘I  plow*,  epapo?,  ‘plow  ,  ipapay^, ‘cleft,  chasm’,  pdpuyS,  ‘throat,  chasm,  gulf’,  L. ferire,  ‘to  strike,  smite’,  forare,  ‘to  bore,  pierce’, OSlav.  barjg,  brati  (for  *bor-ti),  ‘to  strike,  fight’, Lith.  bdras,  Lett,  bars,  ‘swath’,  Lith.  burna, ‘mouth’,  Russ,  borona,  ‘harrow’,  Mir.  bern, berna,  ‘cleft,  opening’.  Alb.  brims,  ‘hole’.  Cp. bark,  ‘rind  of  a  tree’,  barranca,  barrow,  ‘castrated boar',  board,  ‘table,  plank’,  board,  ‘side  of  a ship’,  Boris,  brackish,  broom,  burin,  foralite, foramen,  interfere,  perforate,  pharynx,  and  the second  element  in  Dukhobors.
5370:bore,  n.,  tidal  wave.  —  ME.  bore,  ‘wave,  billow’, fr.  ON.  bara,  ‘wave’,  lit.  ‘that  which  is  borne or  carried’,  rel.  to  ON.  bera ,  ‘to  bear’.  See  bear, ‘to  carry’.
5371:bore,  past  tense  of  bear.  —  ME.  See  bear,  ‘to carry’.
```


## [2026-09-05T13:47:50.097Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\ntargets=['board,  n.,  a  piece','board,','border,','bore,  tr','beaver,  n.,  the  animal','beaver,','brown,','borax,','Bernard','brunet']\nfor i,lf in enumerate(leaves):\n    for tg in ['board,','border,','bore,  tr','beaver,','brown,  adj','borax,','Bernard,','brunet']:\n        if tg in lf:\n            print('leaf',i,'~p',2*(i-12),'-',2*(i-12)+1,'::',tg)\nEOF",
 "description": "Locate Klein leaves for key headwords"
}
```


### [2026-09-05T13:47:51.911Z] TOOL RESULT

```
leaf 14 ~p 4 - 5 :: board,
leaf 21 ~p 18 - 19 :: border,
leaf 70 ~p 116 - 117 :: board,
leaf 75 ~p 126 - 127 :: board,
leaf 94 ~p 164 - 165 :: board,
leaf 94 ~p 164 - 165 :: beaver,
leaf 98 ~p 172 - 173 :: Bernard,
leaf 107 ~p 190 - 191 :: board,
leaf 107 ~p 190 - 191 :: border,
leaf 109 ~p 194 - 195 :: board,
leaf 109 ~p 194 - 195 :: border,
leaf 109 ~p 194 - 195 :: borax,
leaf 110 ~p 196 - 197 :: board,
leaf 110 ~p 196 - 197 :: border,
leaf 110 ~p 196 - 197 :: bore,  tr
leaf 115 ~p 206 - 207 :: board,
leaf 116 ~p 208 - 209 :: board,
leaf 116 ~p 208 - 209 :: border,
leaf 118 ~p 212 - 213 :: brown,  adj
leaf 118 ~p 212 - 213 :: brunet
leaf 119 ~p 214 - 215 :: brunet
leaf 123 ~p 222 - 223 :: brunet
leaf 140 ~p 256 - 257 :: beaver,
leaf 149 ~p 274 - 275 :: border,
leaf 166 ~p 308 - 309 :: board,
leaf 168 ~p 312 - 313 :: board,
leaf 203 ~p 382 - 383 :: border,
leaf 212 ~p 400 - 401 :: board,
leaf 223 ~p 422 - 423 :: board,
leaf 229 ~p 434 - 435 :: border,
leaf 259 ~p 494 - 495 :: board,
leaf 263 ~p 502 - 503 :: border,
leaf 283 ~p 542 - 543 :: border,
leaf 285 ~p 546 - 547 :: board,
leaf 337 ~p 650 - 651 :: border,
leaf 346 ~p 668 - 669 :: board,
leaf 379 ~p 734 - 735 :: Bernard,
leaf 465 ~p 906 - 907 :: board,
leaf 480 ~p 936 - 937 :: board,
leaf 482 ~p 940 - 941 :: border,
leaf 503 ~p 982 - 983 :: border,
leaf 504 ~p 984 - 985 :: border,
leaf 505 ~p 986 - 987 :: border,
leaf 583 ~p 1142 - 1143 :: border,
leaf 586 ~p 1148 - 1149 :: border,
leaf 637 ~p 1250 - 1251 :: board,
leaf 650 ~p 1276 - 1277 :: board,
leaf 657 ~p 1290 - 1291 :: board,
leaf 692 ~p 1360 - 1361 :: border,
leaf 718 ~p 1412 - 1413 :: border,
leaf 730 ~p 1436 - 1437 :: Bernard,
leaf 785 ~p 1546 - 1547 :: board,
leaf 798 ~p 1572 - 1573 :: board,
leaf 807 ~p 1590 - 1591 :: border,
leaf 828 ~p 1632 - 1633 :: board,
leaf 830 ~p 1636 - 1637 :: board,
leaf 833 ~p 1642 - 1643 :: border,
leaf 839 ~p 1654 - 1655 :: board,
leaf 851 ~p 1678 - 1679 :: board,
```


## [2026-09-05T13:48:05.406Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,lf in enumerate(leaves[80:130],start=80):\n    hits=[]\n    for tg in ['bear,  n.,  the  animal','board,  n.,  a  piece','borax,','bore,  tr','beaver,  n.,  the  animal','brown,  adj','bherd','I.-E.  base  *bherdh']:\n        if tg in lf: hits.append(tg)\n    # printed page numerals: look for standalone numbers\n    nums=re.findall(r'(?m)^\\s*(1?\\d{2,3})\\s*$', lf)\n    if hits: print('leaf',i,'nums',nums[:6],'hits',hits)\nEOF",
 "description": "Find Klein leaves and printed numbers"
}
```


### [2026-09-05T13:48:08.416Z] TOOL RESULT

```
leaf 82 nums ['134'] hits ['bherd']
leaf 94 nums ['157'] hits ['bear,  n.,  the  animal']
leaf 107 nums ['182', '183'] hits ['bherd']
leaf 109 nums ['186', '187'] hits ['borax,']
leaf 110 nums [] hits ['bore,  tr']
leaf 118 nums ['203', '204'] hits ['brown,  adj']
```


## [2026-09-05T13:48:14.784Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (94,107,118):\n    lf=leaves[i]\n    print('===== leaf',i,'=====')\n    for line in lf.split('\\n'):\n        if any(k in line for k in ['bherd','bear,  n.,','beaver,  n.,  the  animal','brown,  adj','Bernard','brunet,','bhero']):\n            print(line[:1400])\nEOF",
 "description": "Print Klein entries board/bear/brown"
}
```


### [2026-09-05T13:48:16.701Z] TOOL RESULT

```
===== leaf 94 =====
bear,  n.,  the  animal.  —  ME.  here,  fr.  OE.  her  a, rel.  to  MDu.  here,  Du.  beer,  OHG.  bero,  MHG. her,  G.  Bar,  ON.  bjorn,  lit.  ‘the  brown  animal’, fr.  I.-E.  *bhero-,  ‘brown’,  whence  also  Lith. beras,  Lett,  bgrs,  ‘brown’,  L.  fiber,  OE.  beofor, ‘beaver’,  lit.  ‘the  brown  animal’.  Cp.  beaver,  the animal,  and  brown.  Cp.  also  the  first  element  in Bernard.
Derivatives:  beautiful-ly,  adv.,  beautiful-ness,  n. beautify,  tr.  v.  —  See  beauty  and  -fy. beauty,  n.  —  ME.  bealte,  beaute  (F.  beaute ),  fr. L.  bellitdtem,  acc.  of  bellitas,  ‘prettiness,  charm, loveliness,  beauty’,  fr.  bellus,  ‘pretty,  handsome, charming,  fine,  lovely,  beautiful’,  which  stands for  *dwenelos,  *dwenlos,  and  is  rel.  to  L.  bene, ‘well’,  bonus,  earlier  *dwenos,  ‘good’,  prob.  also to  bedre,  ‘to  make  happy’,  beatus  ‘happy’  and cogn.  with  OI.  duvas-,  ‘gift,  honor,  respect’, duvas-yati,  ‘honors,  respects’.  Cp.  bonus,  and words  there  referred  to.  Cp.  also  beatify,  bel- dam(e),  belladonna,  belle,  belles-lettres,  Beilis,  bel¬ vedere,  clarabella,  embellish,  Christabel,  Rosabel, beaver,  n.,  a  rodent  of  the  genus  Castor.  —  ME. bever,  fr.  OE.  beofor,  rel.  to  ON.  biorr,  OS.  bibar, OHG.  bibar,  MHG.,  G.  biber,  ‘beaver’,  and cogn.  with  L.  fiber,  OSlav.  bebru,  Lith.  bebrus (also  dissimilated  into  vebrus,  debrus),  Lett. bgbrs,  bebris,  OPruss.  bebrus,  W.  befer,  Bret. bieuzr,  Avestic  bawra,  ‘beaver’.  All  these  words lit.  denote  ‘the  brown  animal’;  they  derive  fr. I.-E.  *bhe-bhru-s,  ‘very  brown’,  whence  also  OI. babhruh,  adj.,  ‘brown’;  n.,  ‘the  larger  ichneu¬ mon’.  I.-E.  *bhe-bhru-s  is  reduplication  of  base *bhero-,  ‘brown’.  Both 
===== leaf 107 =====
boar,  n.  —  ME.  bar,  bore,  boor,  fr.  OE.  bar,  rel. to  OS.  her,  Du.  beer,  OHG.  ber,  dial.  G.  Bar, ‘boar’  (not  to  be  confused  with  G.  Bar,  ‘bear’), board,  n.,  table,  plank.  —  ME.  bord,  ‘table, plank’,  fr.  OE.  bord,  rel.  to  ON.  bord,  ‘plank’, Goth,  fotu-baurd,  ‘footstool’,  lit.  ‘foot  board’, Du.  bord,  ‘board,  blackboard’,  OE.,  OS.  bred, MLG.,  OHG.,  MHG.  bret,  G.  Brett,  ‘plank’; fr.  I.-E.  *bhptdm,  resp.  *bhyet-6m,  fr.  base *bherd-,  ‘to  cut’,  a  -^-enlargement  of  base *bher-,  ‘to  bore,  pierce,  perforate’.  See  bore, ‘to  pierce’,  and  cp.  board,  ‘side  of  a  ship’,  and the  second  element  in  gar  board.  Cp.  also  bord- age,  bordar,  bordel,  border,  berm,  brelan,  brim, predella.
===== leaf 118 =====
brought,  past  tense  and  pp.  of  bring.  —  ME. brought(e)  fr.  OE.  brbhte  (past  tense),  resp.  ge- broht  (pp.),  fr.  bringan,  ‘to  bring’.  See  bring, brow,  n.  —  ME.  browe,  fr.  OE.  bru,  rel.  to  ON. brim,  ‘brow’,  and  cogn.  with  OI.  bhrtih,  Toch. A  pdrwdm  (dual),  Avestic  brvat-,  ModPers.  abrit, bru ,  Gk.  otppup,  OSlav.  bruvi,  Lith.  bruvis, ‘brow’,  OPruss.  wubri  (metathesis  fr.  *brwi), OIr.  bru,  ‘edge’,  Mir.  bruad,  ‘brow’.  OE.  brxw, ‘eyelid’,  is  not  related  to  brow  (see  brae), brown,  adj.  —  ME.  broun ,  fr.  OE.  brim,  rel.  to ON.  bninn,  Dan.,  Swed.  brun.  OS.,  OFris., OHG.,  MHG.  brim,  MDu.  bruun.  Du.  bruin, G.  braun,  ‘brown’,  and  cogn.  with  Russ,  bron, ‘white,  variegated’,  Gk.  (ppOvop,  ippuvT),  ‘toad’, (prop,  ‘the  brown  animal').  These  words  have been  enlarged — with  -n-formative  element — from  I.-E.  base  *bher-,  ’shining,  brown’,  whence also  Lith.  beras,  Lett,  bfrs,  ‘brown’,  OE.  bera, ‘bear’  (prop,  ‘the  brown  animal’),  OE.  be(o)for, ‘beaver’  (lit.  ‘the  brown  animal’).  See  bear,  the animal,  beaver  and  cp.  bruin,  brunette,  brunis- sure,  Bruno,  burnet,  burnish,  Prunella. Derivatives:  brown,  n.  and  tr.  and  intr.  v., brownie  (q.v.),  brown-ish,  adj. brownie,  n.,  a  good-natured  goblin.  —  Formed fr.  brown  with  dimin.  suff.  -ie;  so
```


## [2026-09-05T13:48:27.855Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SNS brid ###\" && grep -n \"brīdan\\|bridan\\|brītan\\|brid\\b\\|brīn\" SNS.txt | head -20; echo \"### SNS pages leaf ###\"; python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nfor i,l in enumerate(lv):\n    if 'brid' in l or 'brīd' in l or 'brīn' in l:\n        print('leaf',i, [x for x in l.split('\\n') if 'brid' in x or 'brīd' in x or 'brīn' in x][:5])\nEOF",
 "description": "Grep Shayast ne Shayast glossary"
}
```


### [2026-09-05T13:48:29.399Z] TOOL RESULT

```
### SNS brid ###
### SNS pages leaf ###
```


## [2026-09-05T13:48:30.593Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD brīdan/brīn ###\" && grep -n \"brīdan\\|brīn\\|bridan\\|burrīdan\" PHD.txt PHD_mackenzie.txt | head -20; echo \"### PHD babr/bawrag ###\"; grep -n \"babr\\|bawrag\\|bab̄r\\|beaver\" PHD.txt PHD_mackenzie.txt | head -20; echo \"### PHD bōr ###\"; grep -n \"^bōr\\|bōr \\|bōrag\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep MacKenzie"
}
```


### [2026-09-05T13:48:30.677Z] TOOL RESULT

```
### PHD brīdan/brīn ###
PHD.txt:287:bridan, brin- [PSKWN-tn' < A У sq; blytn!, blyn- | M bryd, N
PHD.txt:292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
PHD.txt:4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
PHD_mackenzie.txt:1627:bridan, brin- [PSKWN-tn l < A ..; psq; blytn', blyn- I M bryd, N
PHD_mackenzie.txt:1679:buridan, bur- [bwl-ytn 1M bwr-, N.....,] = bridan.
PHD_mackenzie.txt:8610:past                      ,~cu          bridanI                \\~ \\'UJCl)
PHD_mackenzie.txt:11037:                                 - ""U-      bridan                     \\~\
### PHD babr/bawrag ###
PHD.txt:230:babr [bpl | N ~] tiger.
PHD.txt:231:babrag [bplk'] beaver.
PHD.txt:954:beaver babrag.
PHD.txt:4013:tiger babr.
PHD_mackenzie.txt:1449:babr [bpl IN ......] tiger.
PHD_mackenzie.txt:1450:babrag [bplk ] beaver.
PHD_mackenzie.txt:6034:beaver babrag.                                  ,..., of prey skarag.
PHD_mackenzie.txt:7787:tiger babr.                              treasure ganJ.
PHD_mackenzie.txt:11075:sczdah:-<                                    babrag
### PHD bōr ###
```


## [2026-09-05T13:48:49.334Z] TOOL CALL #21: Bash

```json
{
 "command": "pdftoppm -f 90 -l 90 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg90 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 90"
}
```


## [2026-09-05T13:48:51.094Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT bray/bri ###\" && grep -n \"brī-\\|bray-\\|pairi.brīn\\|brōiθrō\\|bawra\\|bawri\" BRT.txt | head -30",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T13:48:52.028Z] TOOL RESULT

```
total 29628
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 09:48 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83526 Sep  5 02:45 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
```


### [2026-09-05T13:48:52.075Z] TOOL RESULT

```
### BRT bray/bri ###
6602:anyff  rairtus"  razi/tJ  y.ij.gVüZ.;  —  värp- \  aAunaAe  vairyehe  Y./O.i— 3;  —  vas5.- fnahe  .  .  yS  vayqm  asti  asi/tä  Yt  i4.g;\xsa^r3  Ayilf  a/ava  Y. 8.6;  6;  —  y$  k?r3- 7.5,  i»-5i  iO.141,  19.52,  Y.9.28,  2S.$,'navät(sd.)  _yim  jimiiiig  mi^rjm  .  .  xsnBtS 0<y.  13,  V.  7.44t  Yyt^/;  —  yatasH  bawris\.  .  hylt  Yt. /O. izo;  —  *pasu  vTra  yä  sts (sd.)  sralsta  ya^a  yat  asti  gaoriöJ^ma  \  sarvoanam  vaiiitaYi.  13.12;  —  ioa  haur- Yt-5. 129;  —  %ripi'i7v5  *zT  asti  ätari  ,  ..vata  a»ipr>t<lta  ysi  st5  müdim  asaonam hama  F.  25  b;  Aog.49,  YLro.82,  105,  1.16,  Vti.15; — yazataäbyS ..ySi  hmti yasnyaca 'Y.^S.A,    (wo    astt);    ■ —    Hb    sJ  asti  vahmyüca  Y./.19;    10,  71. t\    10,  V.;.3,
8409:—  bawris  . .  °pS  Yt  5.  ra9;  —  udr?m  . . '  yim    'p>m  V.  i4~  1 ;   —   dva   udra    °pa  V.
9837:•  j.  gaonö.tama-    Adj.   (fem. haarigste,  dichtest  behaarte':  bawri^  (sd.) . ,  'tima  Yt.5.  lag.
11147:—  '^wärS  ahurum  vairim  frasrävaysii V. /Ä43";  —  bawranqm  *°turS  (Am.)  3' aJzanatqtn  (sd.)  Yt5. 119;  —  '/«ra  (An.)*' frasnana  frasnaysit  V, /p, 22;  —  aivake pasvö  .  .  jfos  .  .  %ryqm  .  .  °turqm  N.  65;
14658:•  j.  ftri-sata-  Zw.  'dreihundert"':  bamrami vasträ  .  .  'satanam  bawranam  Yt.5.  139.
15131:•  j,  paity-äp9m  Adv.  'in  der  Richtung gegen  die  Strömung  des  Wassers,  strom- aufwärts': yBi  Als  bawrar»  (sd.)  'ptm  Y. 65.6;  —  tiyapim  .  .  'pfm  V.  6'.  40.
16675:bawra-
16681:•  j.  bawra-  m.
16685:'Biber':  bawraini  vastra  . . iqm  *caturS  elzanatqm{s6..) 3n  dreihundert  Bibern  . ."
16687:•  j.  'bawray-m.'Biber',  f. 'Biberweibchen': yat  asti  'ris  sragsta  yä^a  yat  asti  gaonS.- t?ma  'ris  öavaili  upäpö  "da^  Biberweibchen ist  am  schönsten,  insofern  es  am  dichtesten behaart  ist;  der  Biber  ist  ein  Wassertier" Yt.5.129').
16691:•  j.  bawrinay-  Adj,  'vom  Biber  stammend, Biber"';  'wraini'^  (APn.)  vasträ  .  ,  Sma- tanam  bauiranqtn  (sd.)  Yt.5.  129.
16692:Ableit.  aus  bawra-.  —  Vgl.  lit  bibrinis  {io- Stamm).  —  ')  Statt  •■wrim  geschr.,  S  ^S.  9. (S.  noch  ipmaiiil,  liispö .tailü,  iailayc^
16769:a)  '(sein  sva.)  da  sein,  existiren':  yat  .  . paiti  frali^titn  bavainti  .  .  ggrihqm  (sd.) V.^.  10;  —  yai  kvqm  näirika  bavaiti "wenn  eine  rechtmässige  Frau  da  ist" Vd.2;  —  aSäunqm  ..  fravasayB  .  .  häiti^ hätqm  . .  3ffAu/qm  . .  bBsyantqm  "..  fide- lium  qui  sunt  .  .  fiicre  .  .  erunt"  Yt.  13. 21;  —  daSnqm  .  .  yä  häitinqmcä  bss- ytintinqmcä  tnazistäcä  . .  "dieReligion  . ., die  unter  allen,  die  es  gibt  und  geben wird, die  grösste  ist.."  Y./2.9.  b)  'sein' als  Praedikatsverbum  (Kopula):  bawris bavaiti  upäps  "der  Biber  ist  ein  Wasser- tier" Yt.5.  12g  Gl.;  —  *frayaire  ayqn bavaiti  kubatrS  .  .  aia  apare  (sd.)  ayqn duzäinm  "vormittags  ist  er  (noch) glücklich,  dann  (aber)  .  ."  Aog.5^;  — pairihwS  (sA.)  bavaiti  partiä  yim  .  .  "evi- tanda  est  via  quam  , ."  Aog.  7";  V.  ig. 43(?),  Vyt.Jo(?),  Nik.2,  j(?).  Unklar: kuymte  Yt.j5.s3*,  werüose  Stelle.
16797:mit  aiti  (Sp.  308  m.):  asänü  aiti  maya äiti  barSi f  Y.g.iJ.  3)  des  woher?, a)  durch  Praen. :_)-?(  hJs  bawran  paityäpim (zu  2  a)  nasdistayät  apal  haca  "die  sie  gegen den  Strom  aus  dem  nächsten  Gewässer getragen  haben"  Y.  Ö5. 6*'.  b)  durch
17206:Pü.:  bulatidi\  —  0  Statt  "ii^*  geachr.,  %268. 9;  s.  lu  bawrinay-,  —  ')  Übersetit  das  in vielen  Hds.  (lu  Y.  5/)  beieugte  bfnzai/im.
21171:•  j.  yaO-a  yat  Konjn.  i)  mit  Ind.;  a)  'i so  fem  als,  deshalb  weil':  yat  asti  bawrii (sd.)  srMÜa  y  y  asti  gaonSJ»ma  Yt  5.
21237:(sd.)  dngvanhm  avS  Y.32, 14;  —  täis  zl nä  /yao^anai/dyentf(sd.)..Ay  ('insofern') as  *aojS.  näidyankifn  (sd.)  Y.^J^.  8;  — vaidä  tal  ya  aAml . .  anaisö  tnä  kamna/svä hyatcä  (Sp.  574  o.)  kamnäna  aAmX  Y. 46.3;  —  parstim  zl  %wa  yohanä  tat )mavatqm{sA.)  Ay  {'■<Nt)[')%wä  x^ayqs{5i) alitm  dyat  imavantim  Y.43, 10.  b)  im jAw.:  atcit  bä  lumS  Aaomai  y'  ('weil') vupe  anye  tnatävAs  ailma  Aacinte  Yt  //.  5 ; Y,  /0. 1 3 ;  —  avat  vayul  ba  nqma  aAmi y  »va  dqma  vayemi  Yt  i^.  43;  43f-^;  — aojists . .  y  dim  upanAacat . .  Aqm.vanitts Yt/p.  38f.;  —  aom  ofarmB  AangSurva- yata  . .  ^raltaond .  .y  as . .  vftT^ravastTtnB Yt/5.36;  38;  —  bawraini  vasfrä  vajtAata ,,y  asti  bawris{sd.)  sraiita  Yt.5. 129;  — wn'^rayriB  ..  nBil ..  yanyB  (sd.)  vaAmyB .. y  nürjm  .  ,  dafvayäsS  voAunim  va  taca- yänti  . .  Yt  J^  54;  —  ^banhvB  va  patU vajaanaAe  .  .  y  alta%a  *Aanjastlnte  pouru gaonaAe  (sd.)  u%aheca  N.  65.  IV)  die Folge  oder  den  Zweck  angebend  'so  dass; auf  dass,  damit';  a)  im  gAw.;  1)  mit dem  Praeteritum;  Ayatis.!!!)  ji 3.dibaomä (sd.)  .  .  upa.jasat  Ay  ('so  dass')  vtrstmtä (sd.)    aciitim    manB   Y. 30.(1.  2)    mit
23152:•  j.  'vastra-  n.  'Kleid,  Gewand,  Kleidungs- stück': bawraitti  'rä  vatahüta  arydvT  Yt 5.  129;  —  spaSa  'rä  var^hatti  spaita Yljo.  136;  —  ?rf%ahm  zaranim  . . 'rSsca ktSh  bämanivä  Yt  i"],  14;  zit.  F.  5  (wo vüHrät  vaca  k°)\  —  'nm  . .  ubdanum V3  Izaimm  vä  V.  <?.  23;  —  sr%nm  'nm st»hrpa^aah»m  Vd.  20;20;  —  yänhuya- nam  ..  °ranam  Vd.2;  *I2;  —  hanhus :far^aheca  -rahe-a  V.  5, 38;  —  aSä :^ar»hi  ofaratu  a^ä  'rä  varahatu  V. 3.  19;  —  avalm  3?ar3h>mca  'rpmcij  Y. 5S-3i  z;  — yii0  x^arpia  jrOiS  'raV.^.S^i S7i  58,  Vyt45;  —  i^an^aliiyB  ..'ralibyS .  ,  astayanta  V,  J.  j8;  —  gave  x^arsham gave  'rtm'^  Y.  10.20;  —  mä  gSui  mS °rahe  hatS  aoäitlm  (sd.)   vag^sii  V.  4.46;
27622:'gebären';  1)  von  Menschen;  a)  Ait: SicöM  (nJimlandvIin)  Üaräitii zizanaitt^ (NPf.)  Jaihyante  huzämim  (sd.)  ".  .  ge- bärende Frauen  . ."  Yt.5.87;  —  3r»hqm raya  .  .  Auzämitö  (sd.)  zTzan?nH'''>  (näml. hairiSis)  Yty.  15;  —  ya%a  ha  tsm  zi- zanäp^  yS  .  .  Ytl^.  142;  —  gal%anqm Stshairyeke  (sd.)  .  .  yat  anAairyS  tlzatun Vr. /.  3;  2.3.  b)  Pass.  und  Med.  in pass.  Sinn:  yahmai  zayata  %raltaonS  V, /.  1 7 ;  —  ahmat  haea  puhra  (sd.)  zayaiti^^ Nik.  1;  —  zaySnte  .  .  dasa  ^%ra  Az.5; Vyt.  I,  j;  —  ndil  akmi  nmäne  *zänaite'''* (3PPM,)  ä^rava  naiita  . ,  äat  ,  .  zayinte "nicht  werden  in  diesem  Haus  geboren ein  Priester  noch  .  .,  sondern  es  werden ..geboren  werden  .."  Y.  j/. 6;  —  narqmca zätanqmca  zqkyamnanqmca  ".  .  die geboren  sind  und  künftig  geboren  werden" Y. ^5;  —  s.  noch  zata-  bes.  a)  von Tieren:  bawranqm  */atur3{sd.)  *sTzana- tarn    "der  Biber,  die  vier  Junge  werfen"
29476:tyaisaiy  frafamä  anusiya  ^aha'ia  .  .  ava-    59^;  —  ySi  hl/  bawran  (Sp.  934  m.)   .  ,
```


## [2026-09-05T13:48:59.609Z] TOOL CALL #23: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg90.png"
}
```


### [2026-09-05T13:49:00.300Z] TOOL RESULT

```

```


## [2026-09-05T13:49:00.297Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T13:49:17.701Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for m in re.finditer(r'ببر\\b', t):\n        s=max(0,m.start()-120); print(f, '...', t[s:m.start()+300].replace('\\n',' ')); print('---')\n        \nEOF",
 "description": "Grep Mo'in for ببر"
}
```


### [2026-09-05T13:49:19.787Z] TOOL RESULT

```
MON_part1.txt ...  (غم.) شمول  خواستن. از مطلب دور افتادن. (بع. .) گو بنده  وید مین مج ۷ هی با رن ار  بطلب اصلی خارج شود و به مضمون دیگر  ببر دازده آنگاه باز به مضمون نخستین باز  ۹   استطراف: ۲ (ع.] (سصم.) طرفه  بمردن) نو داسن: نو بیدا کردن چبزی را.  خوش کردن و شگفت داشتن به چیزی.  موی قلاعاجه [ع.] (مسص ع.) آگهی  خواستن» آگاهی جستن؛ اطلاع خواستن.  پرضتب-ل:   استطلاق: بقلاعاوه [ع.] (مصم.) رهایی  خواستن. رهانیدن از بند. (پز.) گشوده هد  
---
MON_part1.txt ... ن در حدود ۵۰۰  میلیون‌کیلومتر مربع است و بقیه را آب فرا  گرفته؛ ج. براری.   بر : ۳۹۲۵ [ع.] (ص.) نیک وکار» نیک وکر دار.  ببر: ۰ (ع.] (.) یی نیکوکاری؛  نیک وکر داری.   بر : 6۲ [ع.] (.) موش: هر را از بر نشخیص  نمی‌دهد) یچ چیز نمی‌داند» چیزی  بر: :50 (ری. بریدن) ریشه فعل «بریدن»عمل  جدا کردن ورق‌های بازی. (اف.) در ترکیب  به معنی «برنده» آید: آهن‌بر.   بر: ۲ (.) (سیم.) عنصری است دارای  ظرفیت ۳ و ۵و وزن مسخصوص ۰۲/۳۴۵  محکم
---
MON_part1.txt ... ود. برمور نقره - برموردارژان ترکیبی  است از برم و نقره که در عکاسی مورد    استعمال دار د.   برنا: 3(ص.) جوان» شاب؟ مسق. ببر.  ظریف» خوب. نیکک.   برناس: 5 ابرناس - فرناس] (ص.)  غافل, نادان.    بر نامه: (6-)02۲-18002 [- ورنامه - بر نامج»  معر. ] (امر.) آنچه بر سر نامه یا کتاب  نو سند؛ عنوان. دیباچه» مقدمه. دستور کار  یکث مجلس» خطابه؛ جشن يا انجمن؛ پرگرام  (فر ه.)   رت : لجع (.) (گا .) گیاهی از تبره  کستا‌شان خ و ومنتته
---
MON_part1.txt ...  جوان و  منوه‌ها فوامنل قسمت‌های البافی, را بر  می‌کند؛ بافت اسفنجی.   پاراو: 05:2 [قس. پیر] (ص.) پیر (مرد و  زن)) کنده ببر .   پاراوان: «5:۷2 (.) دیوار متحرک از  تخته و پارچه که به وسیلا آن یکك قسمت از  اطاق با دکان را از قسمت دیگر جدا کنند»  تجیر گونه‌ای که در اطاق‌ها برابر تختخواب  نهند تا روشنایی را کم کند.   پاراه: 22-0 (امر.) گذرگاه؛ معبر .   پارت: ۲8۳ (.) (جاذ.) پرنده‌ای از راستة پا  بلندان که دارای منقاری طوی
---
MON_part1.txt ... نماز    فرهنگ فارسی معین    ۳2۹    پس‌نماز: تقسمصح (.) آنکه پشت امام  نماز گزارد» مًموم؛ مق. پیش‌نماز.   پسوا: 29-3 (.) ببر وه تابع) مق. بشو ا.  پس‌وازنک: 55-22۱ (امر.) باز کشت  مر.ص» رجعت سماری» س‌افتادگی» عود»  ن   یس و پیش کر دل: 0-.0-0-.0  (مسصم.) جابجا کردن» تغییر جا دادن  بصورتی که آنچه پیش است به عقب برند و  عقب را پیش آرند. پس و پیش کردن مردم  راء بر کنار کردن» تبکیه. زدن.   پسودد: 25-0 [- سودن] (مسص م.)  سسو
---
MON_part1.txt ...  خون کسی تر کر دن:  کشتن او. پنجه تاکك: ب رگ رز.  پنحه. (0-)000[2 [- بنجه - ننجه] (.)  پیشانی» ناصیه. مویی که از سر زلف ببر ند و  آن را پیچ و خم داده بر پیشانی گذارند.  پنجه دردیده: (-)02۵]2-. (امسر.)  هر یک از دوازده ماه ایران ساستان دارای  سی روز بود و سال سیصد و شصت روز  بنابراین هر سال شمسی پنج روز کم داشت»  برای جبران در آخر هر سال پنج روز دیگر  (بنام بنجه دزدیده) می‌افرودند تا سال    شمسی درست سیصد و شصت و پنج 
---
MON_part1.txt ... ) پیر چهل ساله: (کد.)  عقل» قوت عاقله که در چهل سالگی کامل  شسود. (اخ.) جبرئیل. (اخ.) آدم(ص).  فبروزه» فبر وز ۳ پبروره. ببر خانقاه: (تص.)  شیح خانقاه» مر شد. پیر خدای: ( کذ.) عثمان  بن عفان. پبر خرابات: بیری که در میکده‌ها  شراب فروشد» پیر می فروش. (تص.) مرشد  کامل و مکمل است که مرید را به ترکت  رسوم و عادات وا دارد و به راه فقر و  تصوف هدایت کند. (تص.) سالک و عاشق  لاابالی که افعال و صفات جمیع اشیا را محو   در امال 
---
MON_part1.txt ...  و صفات الهیداند و هیچ صفت به  خود و به دیگری منسوب ندارد؛ بیر مفان.  پیر خرد: عقل» عقل کل. مرد دانا و عاقل؛  فرد کامل. ببر خسیس: (کد.) زحل» کنبوان.  (کد.) شیطان» ابلیس. پیر دالو: سخت پیره  سیار سالخور ده. بیر دلیل: (تص.) منصبی در  حوزهٌ تصوف؛ کسی که واسطةً میان مرشد و  مرید است. پیر خمیده: پیری خمیده پشت.  پیر دولت: از بزرگان دولت. (کد.) آسمان.  پیر دو مو(ی): آنکه موی سر وی سپید و  سیاء بود. ( کد.) دنیا به اعتبار شب
---
MON_part1.txt ...  بوحفض سغدی). ( کذ.)  شراب کهنه. بیر سک: سک سالخورده.  دشنامی است راء پیر ششم چرخ: (کد.)  (اح.) مشتری» بر جسس » اورمزد. ببر صحبت:  (تص.) مرشده پیر طریقت. پیر صفةٌ هفتم:    (اخ.) ( کد.) ستاره زحل» کبوان. پیر طر بقت    دیر: رهبان پیره    خدمتکار سالخورده. کهتر سالخورده برابر  پادشاهان و بزرگان از خود به تواضع بدین  کلمه یاد کند. پیر فلکك: فلکك کهن‌سال»  گیتی سالخورده. (اخ.) (کد.) زحل کیوان.  پیر کار: استادکار؛ دانای کا
---
MON_part1.txt ... ش‌سفید میجده» پبر میفروش. رند.  (تسص.) پیر طریقت. بیر منحنی نالان:  سالخوردهٌ گوژشت زاری کننده. (کد.)  (مس.) چنگ خمیده. ببر میحانه: پبر میکده؛  (تص.) پیر طریقت. پیر میفروش: پیر خمار»  سالخوردة باده و ۱ (تص.)  ببر طر بقت. پبر و استاد: : مرشد کامل و معلم.  یر و پیغمبر: مرشد» نبی. سوگند به پیر و  یشب (قسم مفلظ و شدید پیر و جوان:  شیح و شاب هسمه » همان قاطة. . پیر  هافهافو» هفهفو: ببری که دندان‌های وی  ريخته» سخت پیر. پی
---
MON_part1.txt ... کننده. (کد.)  (مس.) چنگ خمیده. ببر میحانه: پبر میکده؛  (تص.) پیر طریقت. پیر میفروش: پیر خمار»  سالخوردة باده و ۱ (تص.)  ببر طر بقت. پبر و استاد: : مرشد کامل و معلم.  یر و پیغمبر: مرشد» نبی. سوگند به پیر و  یشب (قسم مفلظ و شدید پیر و جوان:  شیح و شاب هسمه » همان قاطة. . پیر  هافهافو» هفهفو: ببری که دندان‌های وی  ريخته» سخت پیر. پیر هشت جلد: (اخ.)  ( کد.) رضوان» فرشته موکل بر بهشت. پیر  هفت فلکك: (اح.) ( کد.) زحل» کبوا
---
MON_part1.txt ... ی. به پیران سال: در روزگار  پیر ی"  پیرال‌سر: ۳.۰۲ [- - پیرانه‌سر] (ق‌مر.) ایام  ببری» سر ببری. به بیران‌سر: به روزگار  ببر ی.  پیراهن: 01220 [- بیراهان ‏ بیر هند] (.)  جامةٌ نیم تنه‌ای که زیر لباس بر بدن بوشند؛  قمسص. . جامه بلند و نازکی که زنان پوشند.  بیراهن خواب: جامه مخصوص هنگام  خواب؛ جامهٌ شب. ببراهن زير زنان. پیراهن  راحتی: بیراهنی که در مواقع فراغت در خانه  و نیز هنگام خواب پوشند. پیراهن فانوس:  جامةٌ انوس ج
---
MON_part1.txt ... ۷    (ص‌نسب.) منسوب به جو گندم. (کد.) موی  سر و ریش که سیاه و سفید باشد.   جوگی: وتا (ا.) فرقه‌ای از مرتاضان هند.  (ص.) ببر و طریقهٌ جوگیان مر تاض هندو.  جولان: (مقاسمل مها هه (ع.] (مصل.)  کشت » گرد بر امتان؛ کردیدن؛ دور ردن.  تاختن» تاخت زدن. (امص.) تاخت و تاز.  جولاه: (-.0۳) 3۳1[ [ جولاهه ِ  جولاهک ‏ جولخ - جولق - جولقی -  جوله - جولهه] (ص.) بافنده» نساج. (ا.)    عنکوت.   جولخ: (داحل»«ا0[ | - جولق. معر.] (.)  نوعی 
---
MON_part1.txt ... ن و  لگاماسب و رکاب.   چین. اه (ا.) شکن شکنجء چروکك» تا.  ین بر ابرو افکندن: (کذ.) روی درهم  کشیدن» در غضصب شدن. ( کد.) ببر شدن.  (زم.) شکل قسمتی از طبقات زمین پس از  جنیش‌های کو هزائی؛ ناهمواری‌ها و پست و  لندی‌هایی که به سبب عوامل طبیعی در  سطح رمین و جود آمده.   جیین خو ر 2 آ-6(8)«ل۲مدی (حامص.)  عمل چین خوردن. (زم.) تحول و تغیر    فر هنک فاررسی معین چیر    شکلی که در شکل طبقات زمین بر اثر  فشارهای جانبی و جنبش‌های
---
MON_part1.txt ...   (اصت.) آوایی که از دهان خوانیده شنیده  شو د.   خرنه: (0-)10۲1۸ [قس. خر نش» خر ناسه |  (اصت.) غرش جانوران مانند گربه و ببر.  خرو: 0:5« (- خروس] (.) خروس.    خروار: ۲7 [- خربار] (.) مسقدار بار  یکك خر. مقیاسی است برای وزن. ضح.-  طبق قانون مسصوب ۱۳۰۴ ه.ش یک  خروار (با ره ۳۹  کیلوگرم. ولی طبق معمول یکك خروار -  ۰ من تبریز - ۰ کبلو گرم -  یط نو یو ۱ خروار - یک تن  ام ور پاش یت وب  اتجلتی: اکن تن (2 تقریباً) -  ۳۱۳۱۹۹۱۸۴
---
MON_part1.txt ... خص باشده وسله.  بهانه. زد و خورد» درآویختن.  دستادست: :2:34 (ق‌سر.) معاملة  نقد» یعنی هر چه بخرند همان زمان قیمت  آن را ببر دازند؛ مق. پسادست.   دستار؛ 4200-27 (امر.) مندیل» رویا کك.  پارچه‌ای که به دور سر پیچند؛ عمامه.  دستاران: 0251210 (امر .) مزدی که بیش  از کار کردن به مزدور دهند. شاگردانه.  مه دگانی.   دستاربند: ]028 (امر .) آنکه دستار.  بندد؛ معمم. عالم» دانشمند» فقبه. صاحب  مستك:   دستارخوان: «قد.ه (امر.) سفرة
---
MON_part1.txt ... ) گرم حار؟ ج.  شخان (غم.)   ساد؛ 0 [ - ساده] (ص.) ساده» سی‌نقش و  نکار؛ مق. منقش» نگارین. ابله» نادان» ساده  دل. آمر د» ببر بش. ( دشت؛ بیابان.   ساد؛ 0 (.) خ وکث اک از   ساد: ۰20 (ع.] (افا.) سد کننده. استوار.  راست گفتار.   سادات؛ 202 [ع. ۰] (ص. 1ج سادة حج.  سائد (ساید). مهتران» بزرگان. فرزندان  رسول‌ص و ایمهٌ اطهار.   سادس: 60 (ع.] (عد. ترتیبی» ص.)    سادسا: «م-عع54ه [ع. ۰] (ق.) در مرحله  ۳ (-)۵3060-2 [ع. سادسة] (عد
---
MON_part1.txt ... اوش  ضح.- اين گروه در قدیم به جهت هیبت و    1.۴ فرهنگک فارسی معین سیاه‌چادر    صلایت سباه می بو شیده‌اند. کسی که شیر »  ببر و دیگر جانوران درنده را نگاهداری  کند؟ ج. سیاه پوشان.  سسیاه‌جادر: ۲ [< سسبه جادر ]  (ص‌مر.) خیمه‌های سیاه رنگ که کولیان و  صحرانشنان در دشت و صحرابرای  سکونت بر با کنند؛ ساه خانه.  سیاه‌چال: اقه.: (- سیه‌چال] (امر.) محل  گود و تنگ و تاریک. زندان تنگ و  تاریکث.  سیاه‌چرده: (ند. 60۲۳02)66706-.5 (
---
MON_part1.txt ... تعالی. (تص.) کسی که بر خدا و برای  خدا صبر کند و جزع و شکایت نکند.  صایو ته: (0-)2ان2ه [- سسایو ته» آسی  (استی)] (.) زن ببر.   صابون: ۰2050 (- صابون» معر.] (ا.)  (شیم.) جسمی است که از ماده‌ای چرب  ساخته شود و آن را در شستشوی بدن و  لباس بکار برند. ضح.- (شیم.) صابون‌ها  مخلوطی از نمک‌های سه اسید آلی بعنی  اولئات» پالمیتات و استارات سدیم هستند.    برای تهیةٌ صابون اسیدهای چربی‌دار را با  سود سوزآور در دیگ‌های بزرک - که
---
MON_part1.txt ... ت که صاحش بندارد که  عضو در دمند را می‌افشر ند.   ضافی: ]22 [ع.] (افا. ص.) کامل» تمام.  ضال: (731)1 [ع.] رافا.) گمراه؛» ببر ۵. آواره؛  ج. ضالین. (فق.) غلامی که راه خانة مولی را  گم کرده بی‌قصد؛ مق. آبق که قصد گریز  دارد. (فق.) انسان با حبوان کمشده. کمشده.  ضاله: (م)«للعه [ع. ضالة] (افا. ص.) مونث  ضال؛ گم گشته از حبوان و جز آن؛ ضایعه.  (ف.) گمراه کننده: «کتب ضاله,. ضح.- به  معنی اخیر در عربی «مضل» و «مضله» آمده.  ضامر
---
MON_part1.txt ... عجمه: (ع)«سله [ع. عجمة] (.) یک  هستهٌ خرما. یکك تکسک انگور. خرمابن که  از هسته روید؛ ج. عجمات.   عحور: 212 [ع.] (ص.) زن ببر» بیره زن»  زن کلانسال؛ ج. عسجائژ (عسجایز). برد  العجوز.   عچوزه: (2<«)0 له [ع. عجوزة] (ص.) زن  ببر» زن کلانسال. ضح.- فصحای عرب بدین    ۱۲ فرهنگ فارسی معین عجول    مسعنی «عسجوزه گویند ولی عوام عرب  «عجو ز ۵ استعمال کنند. دختر.   عجول: لاله [ع.] (ص.) آنکه کارها را به  عحله انجام دهد؛ شتابان.   عجو
---
MON_part1.txt ... ور: 212 [ع.] (ص.) زن ببر» بیره زن»  زن کلانسال؛ ج. عسجائژ (عسجایز). برد  العجوز.   عچوزه: (2<«)0 له [ع. عجوزة] (ص.) زن  ببر» زن کلانسال. ضح.- فصحای عرب بدین    ۱۲ فرهنگ فارسی معین عجول    مسعنی «عسجوزه گویند ولی عوام عرب  «عجو ز ۵ استعمال کنند. دختر.   عجول: لاله [ع.] (ص.) آنکه کارها را به  عحله انجام دهد؛ شتابان.   عجولانه: (م)عمق-ان له [غ. ف.] (ق‌مر.)  مانند عحولان شتاب.   عجیب: «اله (ع.] (ص.) شگفت آوره  عر یپ.   ع
---
MON_part2.txt ... در ترکیه و هند نیز معادن فیروزه  موجود است که رنگ‌های آنها غالبا آبی  مایل به سبز يا سبز زیتونی و سبز مایل به زرد  است؛ ببر وزه» ثبر ورج» حجر الظطفر؛ حجر  الغلبه. حجر العین؛ حجر الجاة. فیروزه  بادامی: (زم.) ی به شکل حباب و  یه شکل بادام است. فیروزه بواسحاقی  (بوسحاقی): پیروزة بواسحاقی؛ فیروزة  منسوب به معدن نیشابور.  راستی خاتم فیروزه سواسحاقی  خوش درخشید ولی دولت مستعجل‌بود  ضح.- بعصی تصور کرده‌اند که «فیروزة    ۲ ۱
---
MON_part2.txt ...  ۲ ۵    قحبگی: آ-(0۸)6 ۱« [ع. ف.] (حامص.)  زنا کاری» روسپی‌گری.   قصهه: (ه)دطادر [ع. قحه ] (ص. مونث  قح کلان سال). کنده ببر. فاحشه»  روسبی.   نحه‌خانه: (0-) ۲۰-602 [ع. ف.] (امر.)  فاحشه خانه.   قحط: ۸۱:[ع.] (مصل.) باز ایستادن باران»  خشکسال شدن. (اسص.) خشکسالی:  بیحاصلی. نایابی؛ کم بابی چیزی. قحط  رجال: کمیابی مردان با دانش» قحط الرجال.  قحط و غلا: قحط و گرانی. قحط در علف  خانه افتادن: (کذ.) به آخر رسیدن عمر (مراد  ا
---
MON_part2.txt ... دج (قس. قاقا] (.) میوه خشک و  تنقلات.   کاکا: :۲:5 (.) مربی خانزادگان» للة  بزرگزادگان» اتایکك. غلامی قدیمی که در  خانه ببر شده باشد.   کاکائو: "22 [-کاکااو |(ا.) ( گیا.) درختی  است از تبرة پنی رکبان که ارتفاعش ین ۴ تا    ۰ متر است. برگ‌هایش ساده و متقابل و  گل‌هایش منظم و کوچک و قرمز رنگ و  در همه فصول وجوددارند. کاکائو شامل ۵  کاسب رگ و ۵ گلب رگ و ۱۰ پرچم است.  مبوه‌اش سته و زرد رنگ است و به اندازة  یک خبار و محتوی
---
MON_part2.txt ... ص.) مردی: که سنش بین سی تا  بنیجاه سالگی باشد. مردی دو موی (ساه و  سپید موی) باو قار.  کهن: (قد. )۵۳۵۸ [ - کهنه ] (رص.) ببر»  سالد بده؛ مق. کودکك» جوان. ۳2 قدیم؛  مق. نوء تازه. کار کرده؛ فر سوده .گاه برای  تعظیم چیزی و رساندن مهارت کسی  استعمال کنند.  کهن‌دز: ۱۰-27 [- کهن‌دز ت قهندز» معر . <  کهن. ضصح.- غالب شهر های ایران در قدیم  رو داشته‌اند. (اح.) نام جند قلعه و  از جمله تیشایور.   میو ۱ : 0۳۵27-581 (رص مر.) آنکه 
---
MON_part2.txt ... رم می‌رسد و دارای شاخ‌های بلندی  هستند که گاهی طول آتهاتر ۲ متر بالغ  کر ده کاومشان وحشی از حیوانات  درنده مانند پلنگ و ببر و شیر هم باکی  لتاق غالا ظا آنها سبارزه می‌کنند.  گاو مشان را امروزه اسیر و اهلی می‌سازند.  گاومیشان املی در گیلان و مازندران و  آذربایجان و 3 شهر یار فراوانند و  اکثر رنگشان تبره و غالبا پیشانی شان سفید و  منگولة دم آنها نیز سفید رنگ است. . پوست  گاومیش بسیار ضخیم و چرم آن مرغوب  است. گاوبیش اه
---
MON_part2.txt ...    گر به: (-)0۲۸ی (۱.) (جاذ.) بستانداری است  از راشته که مه شتخواران که سردسته تبرة  گربه‌ها می‌باشد (در اين تیره شیر و ببر و  پلنگ و گرب وحشی نیز قرار دارند.) گربه‌ها  و همةٌ گوشتخواران دیگر تیرة گربه پنجه‌رو  و دارای ناخن‌های تبر سیار قوی هستند که  در حالت عادی و استراحت دنساله‌ای از  پوست روی آنها را می‌پوشاند به قسمی که  در این موقع به زمین نمی‌رسند ولی به هنگام  حمله از غلاف خارج شده و سل ی و  شکار حبوان ر تشکیل
---
MON_part2.txt ...  روی آنها را می بو شاند به  قسمی که در اين موفع به زمین نمی رسند  ولی هنگام - حمله ار غلاف خارج می‌شو ند.  شیر و پلنگ و ببر و یوزپلنگ و گرب  وحشی و گرب خانگی در این تیره جای  دار ند تبر گوبه ینجه‌روان. پنجه‌داران.  گربه‌شو (ی ) کردد: ۸( ۷) ۲۰-51  اقس. گربه شور(ی) کردن | (مص‌م.) چیزی  را ناتمام شستن» بطور کشف باکك کردن  گربه کوره: (-)0.: اقس. گرب کور|  (ص مر.) متا .کار مک تفاس   گربه کون: 1-0 (ص مر.) فر سسنده؛ دغانار؛
---
MON_part2.txt ... ده. جنگ کرده.  انتقال یافته. رسیده. زایل شده. غروب  کرده. لوچ؛ احول. سرگشته: حیران. بخت  بر گشته بدبخت. گم گشته, مفقود. ببر شده.  خطی در عهد ساسانی. مرکبی از عطر بات»  غالا مثلث.   کی 2:5 (ص‌نس.. ۱.) باسبان شب؛  نگهبان شب» عسس گز مه. (نظ.) (فره.)  دسته‌ای از نگهبانان که بابد محوطةً معینی را  مراقبت و نگهبانی نمایند و پیوسته در آن  کت بتتگهی رهق متگدیر [نر ی مر دانه |    (ص.) فسحل, نر. مایةٌ آبستنی و تلقیح.    سیر    
---
MON_part2.txt ...  تروید همراه است؛ در این صورت آن را  هیپوترو ئیدی نامند و يا با افزايش ترشح غدة  تبروگید همراه است» در این صورت آن را  هببر تبرو ثیدی کویند. معمولا انواع مختلف  کواتر را با ترکیبات پددار و یا هورمون‌های  غدة تبروشد معالجه می‌کنند و در صورت  ایجاد ژحمت کردن تومور با عمل جراحی  آن را بر می‌دارند؛ه غماد ۰ سلعه.  موضعی غده تیروئید است و به عبارت  دیکر یکك تومور نیک خیم بدون عارضة  غده تیروئید می‌باشد. ا کر این تورم غده  
---
MON_part2.txt ...  فارسی اسب ببری می‌باشد.  وجه تسمیه بدان جهت است که سطح بدن  حیوان دارای خطوط تیره و روشنی است که  از دور شباهت به پوست ببر پیدا می‌کند.    ماند) سرات. سدان اسب دوانی    کوهستانی افریقا می‌زید و بسصورت    فرهنک فارسی معین    ۱۳۵    را مانند اسب معمولی می‌توان اهلی و تربیت  زد فراز .ان استفاده و ۳    آفریقایی.   ۳ سر ۳ ۳  کوراکور: 0۲۲-۲ (ق‌مر.) با سشعله  سو ران:    گوراندن: ۲زا (مص م 9  ره اعد یر ومد آن را).  آشفتن بب
---
MON_part2.txt ... ی»؛ خر کور.  ضح. غالبا گور خر را با گور اسب اشتباه  کی کنو انس در آفر بقا وجود دارد و  بدنش دارای خطوطی شبیه نقش و نکار ببر  است. این حیوان را در اکثر کتب کلاسی به  خطا گور خر که یک گونة اصیل آن  امروزه در کویرهای ایران نیز یافت می‌شود -  خوانده می‌شود. مراد از ور اصلی همین    ۲ ۱۵۰  گورخر است. از سوی دیگر رنگک بدن  گورخر خرمایی است و خطی مشکی در  گردن تاانتهای دمش  کشیده شده و انتهای اندام‌هایش در نزدیک  سم‌ها ها نی
---
MON_part2.txt ... : ۲۲(ص.) تار» کدر؛ بی‌جلا.  شتا تا داز ۰۲ (.) آنکه در میدان  ویو خر ۳3 ۳0۳۳2  را بکشد؛ گاوباز.   ماتریالیست: 15۱ (ص. .) ببر و  مکتب ماتر یا  م‌اتریش: 5 (۱) (جا    لیسم؛ مادی.  پ.) قالب    ۱ ۵ ۴    فر هنک فاررسی معین ما    محضو فن بر وت سرفی دز چیه ۱  ماتم: ین [ع. ماتم] () محل اجتماع  مردم (عموماً) (غنم.) محل اجتماع مردم  جهت حزن و سوگ (خصوصا).  نوحه گری, سوگواری.   مانم‌کده: (6-)دل۳0-۵ [ع. ف.] (امسر.)  متصلی کته در ا
---
MON_part2.txt ... خانه. لعل ماهی: (جان.) گونه‌ای ماهی که  استخوانش سرخ رنگ است (آنند.) ماش  ماهی: (جان.) گونه‌ای ماهی استخوانی از  تبرةٌ سببر ینیده‌ها که بدنی کشیده و بالةٌ شنای    ماهمی    فررهنگ فارسی معین    ۱ ۷    بشتی کوتاه و نوکك تيز دارد. گونه‌هایی از    این ماهی در دریای خزر نیز فراوانند. ماهی  آزاد: ( (جاد.) گونه‌ای ماهی استخوانی از  راستةٌ تله‌اوستئن‌ها و از دستة فيز ستوم‌ها که  کيسةٌ هوایی شنا در آنها با مری مربوط است.  اين
---
MON_part2.txt ... ة  «اشهدان لا الها لا الله).  متشهی: ]۱ ۱۱۱0۵)24۸ اع. (افا.) خواهندة  جبزی» رغت کننده. ارزو دار ند ۵.  ۱۹۹۵۵ ۲ ۰ (افا.) ببر شونده.    پبر نما.  متشیع: 1۳0۱۹ (ع.) (ا9.) آنکه خو د را  شیعه معرفی کند. شیعه؛ ج. متشیعین.  متصادف؛ 9201ه۱هه [ع.] (افا.) رویرو  شونده» مقابل شو نده.   مستصادم: ۱101292067 [ع.] (انفا.) سیم  خوره با زین با هی زنتی با هم کرینده  ج. متصادمین.   متصاعد: ۱۱( [ع. (افا.) بالار و نده؛  بر بلندی رونده» ج
---
MON_part2.txt ...   منظور؛ مقصود. به مراد خود رساندن: به  مقصودش رساندن. به مراد (خود) رسیدن:  به مقصود خود نایل آمدن. (تص.) شیخ؛  مر شدء ببر؟ مق. مر بد.   مرادف: ]191011 [ع.] (افا.) کسی که بشت  سر دیگری سوار مرکبی باشد. آنچه که در  ردیف ا عقب چیزی آید. کلمه‌ای که با  کلمة دیگر در معنی مشتر ک باشد با معنیی  نز دیک بدان داشته باشد» مانند: انسان و بشر.  مرار. ۲ ,1112۲12۲ ل ۰] (. ) نام برخی از  گونه‌های قنطوریون (کل گندم) که دارای  گل‌ها
---
MON_part2.txt ... ده» تعمس کننده؛ اتاداقش‎  کننده. رتبه‌ای در فراماسو نری.‎  معمر : 1102000137 [ع.) (امف. ص.) آنکه‎    عمری طولانی کر ده» ببر سالخورده؛ مسین ؟  : معمر ۰   مسععمر: ۲( [ع۰] (اسف.) معموره  آنادان.    معمم: هه مه [ع.] (امف.) تعمیم داده  شد ۵ عام کرده شد ۵.    ۱۱۱۵2۱0182۵100 [ع. مستحدث ] (امف.)  عمامه بو شید ه» عمامه بر سر نهاده» عمامه‌دار؛  ج. معمعین.  معمودیه: (0-)۱۱-1۵ 10۸ [ع. معر.  مسعمودية از ارمی] (ص‌نسب. ا.) چشمة    
---
MON_part2.txt ... جسمی که از قطع کردن یک هرم با  صفحه موازی قاعده موجود آید. بنایی که به  شکل هرم باشد ج. اهرام.   هرم: همه [غ.] (ص.) سخت ببر و  خر فا.   سً 9۳0 () (عم.) گرمایی که از نقطه‌ای  نسية دور دست از آتش احساس شود  حرارت و تف آتش (فر عا.جما.)  هرماس: -۱0 ,2۳۳88 [راهرمن»؟] 0(  اهریمن» ابلیس» شیطان.   هرماس: ۳  خونخوار» هرمس. بچة پلنگ.   هر مر : ۱0۳۳02 [- اهورمز دا ارمز - ارمزد  - اورمزد - هورمز - هورمزد - هرمز]  هرمزد (همع.) (ب
---
```


## [2026-09-05T13:49:28.635Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nprint('nleaves',len(lv))\nimport re\nfor i in range(445,460):\n    head=lv[i][:200].replace('\\n',' ')\n    print(i,'|',head)\nEOF",
 "description": "Inspect BQT v1 leaves near p.231"
}
```


### [2026-09-05T13:49:30.403Z] TOOL RESULT

```
nleaves 777
445 | 2 بالاده ع بروزن آماده. اسب جنیبت‌را کون که اسب کوتل باشد ٩‏ . ۱ پالا - بسکون ذال نقطه دار . بمعنی بالاده است کفاسب جنیبت باشد. وبسنی‌اسب‌پالالی بار کش زا گوبند ۱ . پاللاد » بروزن نالار , شاء‌تیر را گ
446 | بالش زمرسرنهادن بالیز یر سر نهادن - کنابه از خوشحال کردانیدن باشدکسی را.طریق خوشامد و تیثال . بااش قر ه مقدار هشت درم‌ودودانگ شره باشد ‏ . بالغ - بضم ثالث و سکون غن‌نقطه‌دار , شاخ کاو میان خالی با چوب
447 | با لو س ت برءزن‌سالوی ء,کافورمخشوش,ا و ۳۹ پا لوش - با شن‌قرشت . بروزن‌وممنی بالوس است که کافورمفدوش باشد» چد درفارسی سین بشن و برعکس تبدیل می‌باید . باله - بروزن لاله . قسمی از جوالباشد که چیز ها را د
448 | مام شاد و عاجز شده باشد و در نهایت عسرت و پرشالی گذارد » و باین دو حعنی بض‌ثالث هم بنظرآعده است وبا بای‌فارسی هم کفتهاند .٩‏ ننم مطربیست که او نیز مانند بارید عدییل ونظیر تداشته . بام قشادهر فیع ‏ کنا
449 | بالف کشینه » بلفت زند ویلزند (۱) فبل‌را کوشد و آن ۱۳ در هندوستان . باهش 9 سکون ثالث و فاف مکسور مشین فرشت زدهه دانهٌ کوچکی است که براون- وین گونند و آلرا شوربا کرده خورند» و ممربی جیلخ را خوانند . باف
450 | ِ باور ۱ عم بر وزن خاور » بمعنی قبول و دیق سخن باشد - و بمعثی اسئواد و راست - واستوار داشتن هم‌بنظن آمده است . باوره ۲ بفتح واو و سکون زا و دال کاورزعینی ساوردین کودرز بافطاع مقرر فرهء‌وده بود , ار اي
451 | الو خوداست چنانکه‌شاسته حشتیو اجب‌الو حجو د(۱) را گونند . و بایگان ۴ باکاف فارسی بر وزن آسمان » بمی‌حافظ ونگاهدارنده بات وخزانه دار رایز با بروزن صبا , درخانه و در سرا را کوبند ۴ - و آشیرا نیز کون دکه
452 | سموده رستم اندر کوههای ۰ و پوست آبرا جیبه جامه ساخت . خاصیتش آنست که درآتش سیب درآب غرق شود و هیچ حربه مر آن‌کار ؛ وکویند وقتی‌درزمان الوشیروانآ نجالور آن جاتور در مبان] نجماعت افتادم‌همه رامجروح سلخت
453 | لت » بفتح اود و سکون ثانی. آهار جولاهگان را گوینده بمتی ه بردوی کار مالئد ودر عربی نیز همین‌معنی دارد ۷ - ربمعنی لیف جولاهکان هم آهفه است- و مرغابی را نز کویند و معرب آن بط است - و چشم اول‌حعبود وهسجو
454 | وتیردانی را کوبندک» پر از نبر باشد » ومعنی تر کیبی آن‌بت ماننداست چه‌بت لِف‌جولامگان و کیش ماننه را گومه . تقالاب »با لام بر وژن محراب » غلاف کل خرما را گود . تلخ و ترش دضادادن کنایه از راضی شدن بمحئت
455 | و۳ مب و فرویزدن چیزی در جابی باشف ۷ . بتو ر ال ‌ حتح اول و ثالی_ بواررسیده و رای بی‌نقطه بالف کشیده و.یعاف ده . چاحی باشد که غله و امثال. آن در آن‌کنند و خلاشه هم آخده است ؛ و بمعنی آخر بتفدیم تای‌فرش
456 | پجشلث ‏ بکر اول بی وزن سرتك » بسنی‌حکیم و داشندبود ٩‏ - و مخفف‌بنجشك هرهت که کنبجدكث باشدوحريي عصفورخوانند ۴ - . بجل این اول و انی بر وزن دهل » استضوان ای وت بان بندگاه سای پای عیباشه » و بتاز ی کعب م
457 | بچکم - بفتح اول و کاف بروزن شبتم» خانة 7 اطراف آن را شکه کرده بشند ۱ - و ابوان و سفه و بارکده را نیز گویند - و بمعتی کر که هم آهده است که بعربی ذئب‌خوانند » وبکسر اول هم درست‌است بچل - بر وزن کچل . شخ
458 | سه؛: روزة خوارزم که ای آنجا جمع حود و کنابه از دمت صاحب همتان هم هست . پحردمان مق عمل - یب از | بحری که دم آنرا برکزدن اسبان و برد سر علم ی بندند ۰ و بعضی کوبنذ کاوی است که در کوههای ۳0 بح - بکراول و 
459 | --- 1۳۵ باکت .- بروزن‌سخت؛ بمعتی‌طالع باشد ۷ - و سیاهی را نیز گویند که در خواب بر مرم‌افتد و آنرا بمربی کابوی وعدالجنه خوانند ۴ سونام جاتور کی است‌شبیه بملخ - ویضم اول‌نفام‌پادشا‌ی بت د ندان‌خای کنابه
```


## [2026-09-05T13:49:49.343Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nimport re\ndef find(pat):\n    out=[]\n    for i,l in enumerate(lv):\n        if re.search(pat,l): out.append(i)\n    return out\nfor pat,name in [(r'بورق','بورق'),(r'بوره','بوره'),(r'\\bبور\\b','بور'),(r'بریدن','بریدن'),(r'\\bبیل\\b','بیل')]:\n    print(name, find(pat)[:40])\nEOF",
 "description": "Locate BQT headwords"
}
```


### [2026-09-05T13:49:51.378Z] TOOL RESULT

```
بورق [284, 535]
بوره [184, 287, 535, 748]
بور [27, 30, 32, 35, 45, 56, 96, 100, 112, 125, 126, 130, 131, 136, 137, 164, 412, 462, 501, 534, 536, 652]
بریدن [309, 476, 490, 503]
بیل [110, 368, 673]
```


## [2026-09-05T13:50:01.605Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nfor i in (451,490,534,535):\n    print('========== leaf',i,'(printed ~p',i-220,') ==========')\n    print(lv[i][:2600])\nEOF",
 "description": "Print BQT leaves 451,490,534,535"
}
```


### [2026-09-05T13:50:03.428Z] TOOL RESULT

```
========== leaf 451 (printed ~p 231 ) ==========
الو خوداست چنانکه‌شاسته حشتیو اجب‌الو حجو د(۱)
را گونند .
و
بایگان ۴ باکاف فارسی بر وزن
آسمان » بمی‌حافظ ونگاهدارنده بات وخزانه
دار رایز
با بروزن صبا , درخانه و در سرا را
کوبند ۴ - و آشیرا نیز کون دکه از من یز ند»
و بن را بعربی حبةالخضرا گویند .
ببال دیگری ی پر یدن"- یعنی به
حمات دیگری کاری کردن .
بیقلث س بروزن خشتك : باره‌ای ازخوشة
انگور و خوشهٌ خرصا باشدکه چند دائة مانند
خوشهةٌ کوچکی بکجا جمم شده باشد .
لهر مه یتح اول‌وثانی وسکون رای شت»
جانوری باشد صحرایسی شبیه بگربه لیکن
دم نبارد و از بوست آن پوستن سازیه #۶
ونانی باشد که در ميان روغن بربانکرده باشند
و بسکون:ثانی نام درنده‌یست مشهور 6 -.وجیبه
بوشیده است و عصی, بند که آن ازپوست | کوان
دیو بوده -
و یکی اول
موشوا اکو, رذف
و بعریی فاره
. خوانند . مس
۱ # لله - نم اول وت 1 ۱
کوش و آق زراونه طوبل است ۷ بت
بربدن ماد شد شیش را بکشد .
ات نکتی رای فرشت ۰ همان
"جسه جامه‌است که رستم‌روز های جنگسپوشیده
است؛ و بسن ی کونند که آن ازیوست اکواندمو
ور شا نع ۱۳ آترا بجهت رستم
از , بپشت آورده بودند ؛ و سصی دیگ ‌کوشد
7
۵ سمفربآندز*بیدتض*.
========== leaf 490 (printed ~p 270 ) ==========
و کار بهوده و بیفایده کردن باشد . #
پر ود قلكك - کنابه ازماه است که‌قمر
باشد - و ژحل را نی زگفته‌اند 3
بر لژزن - بکر اول و تحتانی مجهول
بروزن شیمن » پرویزن باشد که بعربی غرپال
و علپال کوبند ۴ -و بممئی ترشی بالا هم آمده
لت - و ابه‌ای را نز گویند که از کل ساخته
باشند و بربالای آن‌نان پزند » و بقتح اول‌بمعنی
بر لژ ۵ » بکسر اول وئالث مجهولبروزن
سفیده . صمفی است دوایی شبیه بمسطکی وآن
سبك و خشك و بدبوی‌میباشد » و حمربان‌باززد
ریانما۰ با حای بی شطذ ولام
مشدد بالف کشیده , بربان باتره و پودنه وترخان
و نان و ییاز اون ۰
بریحی ۱ با چیم بر وزن رسیدن »
تنوری باش د که در آ نکماج و نان سنکك پزند ۰
و جربی فرن گوبند بضم فا .
بریخ زدن- بنتجبای حطی, کنایه از
خاطر محو نمودن و تلم نبردن و فرأمو شکردن
سونایدیدساختن‌ومعد وم گردانیدن- وهیچ‌انگاشتن
باشد -
بر بخ و شتن » کنابه‌از هیچ‌انگاشتن
- وکارییمدار و بی‌اثر کردن وضایم ساختن کاری
۱ - رك : برزن و پریزن . ۴ - رك : پرویزن . ۴ ٩‏ بریجن » پهلوی .
0 , ابرانی‌باستان [0۲21 * (یختن » برشتن) «اسفا ۱ : ۲ س ۷۱ *.
ری - بفتح‌اول . ظاهراً اسل آن‌از کلملانینی ۷5۲۵۸/105 کرفته شده بمعتی‌چاریای
چاپار و اب چایار وسپس بمعنی مك . سد ها باداره و دستگاه چاپار و عاقبت برمنزلی که بچندو .
حو.کز چاپار است اطلاق کردید و این منزل در بلاد ايران دو فرسنگه سه‌میلی و در ممالكشریی
اسلامی چهار فرسنکگ سهمیلی است ب «دائرءالممارف اسلام» . مولف د تفس » پرید را آزبردن فارمی
گرفه و آین‌درید و قرسی دانسته وصحیح قول اول است که مذ کور شد
۵ بریدن - بشم اول و فتح‌چهارم وتخفیف وتشدید دوم (هردو): ٍِ" 320( «منای
۷۰ ی , سانسکریت 010610804 «بارتولمه۲ 0۹۷ ؛ فطع کردن» جدا کردن - عبور
کردن, گذشتن - قطم علاقةٌ خویشاوندی کردن .
قبه ازصفحهٌ ۲3۹٩‏
بکدام سمت درحر کت بود؟ تکهبان این روکد بود؟ آبا آبها و ورطدهای ژرف وجود داشت ٩‏
درآ نوفت نهمر که بود وقفیتتر گن: » روزهنوز ازشب انفکاك نداشت ت. ففط «زات‌احدیت» نفس‌ميکشيد,
آن‌هم تتض یکه با ذات بيگانگی نداشت . جز او هیچ لبود . پس دراین ات واحد نتنآ رزو
پدیدار شد » و اين نضتین بذر تفکر نود . علابق حستی را درنست ی کف کرد . که میداند و که
میتراند بما بگومد که آفربنش از کجاآمد ؛ وآبا خدابان بعد از پیدا شدن جهان متولد شده اند
با نه کی چه میداند خلفت از کجا آمدماست ؛ این آفربنش از چه منشابی است ؟ آبا جپان
مخلوق است با نه 4 آنکبکه از بالاترین مقام آسمانی چشمش حافظ جهان است فقط اومیداند.
و ععلوم نبست او هم آ گاه هست با نه.؟» در حندوستان درحدود ۲۱۰ میلیون مرستانی و ثب‌آن
ساکنند. «ملل و تجل . باسمی. موم وعظ وخطابه ص‌٩۱».‏
‌ برهنگی _ بهلوی حاامصطاعره «هنای ۲۷۰ ؛ لختث. بودن » عور بودن .
۵ رنه پهلوی 3۲۵081 «منای ۲۷۰>*تاوادب۱۵4»:؛ عرمان » لخت- بی‌حجاب..
ناپوشیده . ۰. »ریات - بکسراول (ازمصدورمشتن) کیابشده , برشته‌شده ,کباب .
========== leaf 534 (printed ~p 314 ) ==========
۱ 2۳9
شبیه‌به ثیهولیک نکوچکتر ازاوست" وا نرا بعربی
سلوی خوانند .
بو ر نم اول و انی مجهول ر رای
قرشت هردو ماکن» اسب سرخ ونك را گویند ۴
بودش
‌
بودص - بکر دال ابجد بروزن
سوزش » بیعتی هستی و بود باشد و بعربی کون
خوانند ۱ . #
و ذ نه - تجح دال وئون : درنده است
که‌آنر! نیپومیگوبند. ریسضی کوبند پرنده‌اٍیست
۱ - معنولا اسم مصتر در فارسی آزريشة فعل (< دوم شخص مفرد از امر) ب؛ «ش »
ت کیب شود رلی بودش ازسوم شخص مقرد ماضي و« ش » تر کیب بافته برخلاف قیاس » و ناصر
. خسرو آنر | تن . رل : زادالمسافرین ۳۹4: ۰۱ ۳ 98۲ روباه» اسب؛ سرخ فهوه‌بی:
سانسکریت ۵۵11۲۷1 ( سرخ فهوه‌بی, فهومبی ) < اسفا ۱ : ۲ ص 4٩‏ * اوستا 02۷۲۵ اساسا
بممنی سرخ ( در نداول عوام بور شدن ؛ بعنی سرخ وخجل شدن) است که سیی بجانوری که در
فارسی ببر ( بدو فتح ) کویند اطلاق شده ( ۵ ۰م )» پهلوی تلا < بندهش ۱۲۱ و ۲۲۹ ۰
«بوستی. بندهش ۰۹۰۶ ؛ طبری 0۷1۲ ( زرد ) « واژه نامه ۱۵۴ > دزفولی 5102۲ - ناه را
یُمعنی ۶ لر » بکار برند چه لرهای خوزستان سوار اسب‌بور شوند .
۵ بودن - بغنعم سوم » چهلوی 00488 «منای ۰۶۲۷۰ 00127] داونوالا ۳۸۳»؛ ازريعة
آزبایی ۵2۷ , ۵۱08 (بهمن معنی) «نب یکت 4۱ اوستا 02۷۵141 , سانسکربت ۷2 قتا
(سوم شخص) . لانینی ۱20۳260]» اسلاو 1396 (مسدر) «۲براهامیان» وركك : فپرست اسقا ۱ : ۳؛
استن . وجود داشتن» هستی داشتن- وجود, هستی . ۱
یقه ازصفحهٌ ۳۱۳
72 , مادر وی مایا دوی[06۷ - 1۷1812 نام داشت . سوددنه راجه بود
وبرقببلهُسا کیا درکاینله وستولاا25 12۳112-۷ ( جنوب غربی نبار ۱۷6021 در هند شمالی )
حکومت میکرد " و مادر بودا نیز دختر راجه ۳۲20۵0412 - لاگ بود وبتابراین بودا اطبة
2 ( نجبا ر امرا)است واو در حدود سال ۵۹۶ ق.م ( بقول وبلیامز حدود ۵*۰ ق .م)
متولد شد . وی موسی آین بودایی احت و این آبن مبتنی است بر اشکه : حات رتج است
و رنج از هوی زاید و تركك فس تنها وسیلهٌ رهایی ازهوی وه‌وی‌است . کمالمطلوب بودابی عبارت
است ازوصول به 3۳۷۵7۵[ بافنای کل .
د رگد بودا در هشتاد 7 انفاق اقتاد . امروزه در حدور ۰۰۰۰۰۰۰۰ تن در حسّد
وبیرمانی وسراندیب وتبت‌وچین وژاپن پیرو آین بودابی هسند. رك: فرهنك سانسکرت‌بانگلسی.
مونبه وبلیامز ص ۷۳۳ سنون ۲ ؛
ماع :۲۵۲۱5۵ فلت مظ بل ۱۷۸6 ما ,4نافاا6 ۷5۸76(
: 1942 - ۱94۱ هاانهاج) ۰ ۷۵۱6 2 بتصکنطان9۵ عناعده۳۵( ۲۱۲ق۴ , 0۵16([
۰ 7 ۲۵۵۵008 مر 1 ,۷۵۱ رک5اظ0 ۳.6.۱۷۵۵
و رك : بد و پوداسپ. ۱
بوداسب» 4و اسب - مسلمانان نام بوداسب ور سوسس اساطیری مذهسی صایه اطلاق
کرده و گفته‌اند که دی ایرانبان رادر عهد طهمورت بان دین دموت کرد وابرانیان یش‌از آنگاه
بقیه در صفحةٌ ۳۱۵
========== leaf 535 (printed ~p 315 ) ==========
مشهور - و بمعنی یار هم هست که امر بآوردن
باشد ٩‏ . *
باشد » و بعضی گویند آشی بفر! است - و بسنی
سنبوسه و قطاب را کوبند - وبمعنی شتل ۴ حم
حست. وآن‌زری باشد که درقمار ببرند ومحاشران
دهند. و زنگاری را نیز گویند که برروی نان
بوربا کویی
رسیده و رای فرشت مفتوح . نام پادشاهی بوده
استولام جزبره‌ایست درجانب شمالی که شنقاررا
از آعجا آورند » وآن پرندمایست سفید وشکلری
ازجنی سیاه چشم» و کونند مردم‌آن جزیره‌همه
زال وسفیدموی میباشند.
لو ده - بروزن شوره. چبزست ماد
نمك وآبرا زر کران بکار برند - وشکر مفید دا
نیز کفته‌اند. ومعرب آن بورقاست وبعربی‌بطرون
نشیند » و باين ممئی یفتح اول و زای هوز
خوانند ۴ . و کویند ا گر فدری ازیوره باسدف
هم آمده است - و در عربی بمعنی مبارك باد
باشد . بایند و در بنی زن بدمند اگر آن زن عطه
لور نگاه بر وزن هوشنگه ۰ توعی از کند دوشیزه بود و اکر فکند دوشیژه نب‌اشد »
ریحان کوهی باشد . وبور# ارمنی همان است
بودیا کو یی » کنایه از بای .
۱ - بابن ممنی کلکی 08۷8۲ (یار) . ۳ - امروز ختلی ۹24۵11 گویند
۴ - درفطرالمحیط آعده: «البورق اسناف : مائی وجبلی و ارضی ومصری وهوالنظرون»
معرب بوره بالفارسية 4. ابن‌کلمةٌ مرب واردلاتینی قرون وسطی‌وسیس داخل‌فرانه شده 88072۷
گردیده(برات عیدرانه دسود ) «نداب ۳ : ۳ - . فرامرزی». فراسوبان ودیگران 80۳8 را
ازبورق عربی گرفته‌اند وعرب همآنرا از بورة فارسی اقتبایکرده‌است. «نضب۵4۳».
6۵ وراب - نلم آهنگی با زر کر فیصر روم ( درشاهنامه ) » بزعم ,یوسنی در 1 نامه
اصل کمه مستمل‌است اسم ونانی «بوربوی» باشد . «فرهنك شاه امه؟.
۵ بوران - پهلوی 9۵۲80 «بوستی. نام نامه ص۷۰» ظ , از9۵6 (ه . م) بمعنی‌سرخ»
کلم مز مور بمعنی کلگون‌است. وتر کیب اسماه ازردگها سابقه‌دارد (چنانکه سهراب وسرخاپ س
دارند آب و رنه سرخ , و سییشمد ام خانواد کی زرنشث بمعنی ( از نژاد ) سپید) ؛ نام دختر
خسرو پرویز که چندماء درابران سلطنت کرد - نیزنام دختر حسن‌بن‌سهل زن مأمون عباسی.
بورانی - نان خورش ی که ازاسقناج و کدو وبادنجان باماست با کشك سازند درالامی
فی‌الاسامی ( چاپ منگی ۱۲۹۵ ص ۱*۱) آمده : « البورانی متسوب الی پوران و حی امرأة *.
برخی آنرا منسوب ببوراندخت دخثر خرو پرویز وبرخی ببوران دختر حسن مهل دانسته‌اند» در
دزفولی 00۳۵8 گیلکی ظ۵اط . #وریا - ماخون از آرامی (اسفا ۱: ۲ص *.
حصیری که از نی شكافتة مخصوص‌سازند . ممرب‌آن « باری » است
نیزاز سومری بعارت کرفته شده« فاب ۱ : ۱۱۷ *.
نو رد و ده ‌ بضم اول و ثاك بواو
« اين درید ». در این زبانها
بقیه ازسفحهٌ ۳۱4
دين حنفاه را داشتدد . بوداسب با بوناسب مسعف نام «بوتاست» است که دریهلوی آمده ( بندهش
۸ ۰ ۳۶) واشتقاق آن چندان بانام«بودا» رابطه ندارد. بلکه از نام بودذبنوا 800010152)۷3
معتق اسث (رله متتر ]1 , س ۲۵۹ . 11[ ص 261/۷11 ) «داثرة المعارف
اسلام» - تيز بوداسف دراسطلاح نجوم وجه دوم میزان است بنا بر کتاب المدخل آبوه‌مشر بلخي.
دگاء شماری ص۳۳۹ >.
. اوستا , ترجمة دار
```


## [2026-09-05T13:50:47.713Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SNS ###\" && grep -n -i \"brīt\\|brit\\|bur\\|cut\" SNS.txt | head -30; echo \"### SNS_pages leaf count ###\"; python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read();lv=t.split('\\f');print(len(lv))\nfor i,l in enumerate(lv):\n  if 'brī' in l or 'brid' in l or 'brīd' in l: print(i, [x for x in l.split(chr(10)) if 'brī' in x or 'brid' in x][:3])\n\"",
 "description": "Grep SNS glossary"
}
```


## [2026-09-05T13:50:49.144Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHN borax leaf102 ###\" && python3 -c \"\nt=open('PHN.txt',encoding='utf-8',errors='replace').read();lv=t.split('\\f')\nprint(len(lv))\nfor i,l in enumerate(lv):\n    if 'BORAX' in l or 'Borax' in l: print('leaf',i,'printed p',i-31); print(l[:1500])\n\"",
 "description": "Pihan borax entry"
}
```


### [2026-09-05T13:50:49.834Z] TOOL RESULT

```
### SNS ###
681:Religious Customs. Hamburg 1930. 
959:Etymologie. Strassburg 1893 new ed., Nt 
976:Saint-Petersburg 1908. 
995:Strassburg, 1895. 
1012:Strassburg. 1904 new ed., Berlin 1961. 
1130:and Notes. Hamburg 1930. 
1410:burg 1904 new ed.., Berlin 1961. 
1477:burg 1908. 
1503:Strassburg 1893. new ed., 1974 (GNPE) . 
1514:: Persische Studien. Strassburg, 
1667:and Notes. Hamburg, 1930. 
2918:YfriS k« 9v « a bhr< gb J# ; aburnSyagan: **-o-»\r 
3069:f* [J^J^oy -.«*) .^ (jtijil ^: aburnay: JS, 
3081:l.^.fl-Ao/T <*(*-**)*!» <**, . I* :aburnayIg:^J> lC , 
3085:•A/Y ^ .iH,«jl 3 ;jj : aburnay Ig:^^!^ 
3571:. jj/ J**c 1j ^t^i I* : altar burdan : m°iv>** >kx>" 
7440:burrldan 
7702:• ***[* < JUu «aiiy .yi, ,j^* :burz: Vj) 
7705:u toT,*a.T^g^ J jT,«ai JJ ^II Vli p5T :adur I burz: ^j^m" 
7707:• ^oW * ^u^ 1 * « J^ilW ' J>ij*: burzed: wvu 
7709:- J-L> ««oi^ <j'*** : burdSr : lo^p 
7710:( w«i> •'*&) >i^«^>A1m<o«V !^5n burdflr : ^~»«>i**S> 
7714:• o j j* J** * o ■*.* :burdan: wwp 
7721:(jo*. ^.1) .j^,, ij-jt': burrisn/burisn: *gS)}) To 
7785:lf/1Y<^ >J^oAl<^V :bur * kardag: \a>J»3ii» 
7806:if Utfc^.969)bhuray : &§S,s** buray : jl .t_ 
8420:• y/T*S .cmU.*** :burld fistSd: yw»*»Aj V»3x»0 
8422:•0«**<u-*:burer:iisn: PSKWN, sn: >» s «u»j3»« y< 
8424:0-^-)0'*o*:burIdan: PSKWN, tn: >* »>*|>4«*j 
8429:•V/A^ (ilU^U.jl, .,£) . *£,,»£, :burrend:^ : ^113^0 
### SNS_pages leaf count ###
243
```


### [2026-09-05T13:50:51.345Z] TOOL RESULT

```
### PHN borax leaf102 ###
438
leaf 102 printed p 71
BOS 71
CoDstatitinople, il en existe plusieurs ainsi appelés et (]ui appro-
visionnent d'eau la capitale de l'Empire ottoman.
BORAX, s. m. (a.-p.)
vyy [iatwfl^] nitre, en persan ij^ [boûrah]. — Borax est le
nom donné vulgairement au sous-borate de soude, employé
en médecine et dans l'industrie, surtout pour la fonte et la
soudure des métaux. — Les Espagnols écrivent borrax, et les
Italiens borace. — Le borax brut s'appelle aussi tinkal. Voyez
ce mot.
BORDAT, s. m. (a.)
i^jj [bardât] Pièce de vêtement oblong en étoffe de laine, de
couleur grise ou brune , et dont on se sert pour s'envelopper.
Le manteau de Mahomet portait ce nom. — Il existe chez les
Arabes un poème mystique très-célèbre, intitulé le Bordât,
c'est-à-dire le Manteau, et qui a été composé à la louange du
Prophète par Abou Abd allah Mohammed, fils de Said, fils
deHamad, Bousiri, en reconnaissance d'une guérison mira-
culeuse qu'il avait obtenue, après avoir invoqué le nom du
fondateur de l'islamisme.
BOSTANDJI, s. m. composé, (p.-t.)
^Um^ [bostândjy] jardinier. Mot composé du substantif
persan^ [boâ] odeur en général, de ybu. [«ta?i], terminaison
qui sert à former certains noms de lieu (par conséquent, (jV&*m^
[Aotwton] signifie à la lettre lieu d'odeurs ou parterre odoriférant)^
ei de la particule turque (gs>' [djy] , qui, jointe aux substantifs,
cil fait des noms de métier. — Le ternie bostandji s'applique
leaf 411 printed p 380
380 TABLE ALPHABÉTIQUE
Bonde, 8. f. (p.) Page 70
Borax, s. m. (a.-p.) 71
Bordât, s. m. (a.) 71
Bostandji, s. m. compose, (p.-t.) 71
Boudjou, 8. m. (t.) — BiyAlb(nidjoû; valeur de cette monnaie. ... 79
Bougie, n. pr. (a.) 78
Bouquet , 8. m. ( a.) 73
Bouracan, s. m. (a.)« 7/1
Boumou8, 8. m. (a.) 74
Bourrache, s. f. compose, (a.) 74
Boutargue, s. f. compose, (a.) 75
Bouteille , s. f. (a.-p. ) 76
Bouzah, s. m. (t.) 75
Brevet, s. m. (a.) 76
Briquet, s. m. (a.) 76
Broc, s. m. (a.) 76
Buccine, s. f. (a.) 77
Buse, s. f. (a.) — Busard, Buson, s. m 77
c
Caabat ou Kaabat, n. pr. (a.) 78
Caban, «. m. et Cape, s. f. (a.) 78
Cabaret, s. m. (a.) 79
Cabire, adj. et subst. des 9 g. (a.) , 79
Câble, s. m. (a.) 80
Cachemire, n. pr. et s. m. (p.) 81
Cadeau, s. m. (a.) 81
Cadi, s. m. (a.) 81
Cadi-asker ou Cadi-iechker, s. m. compose, (a.) 89
Cafard, c, adj. (a.) 89
```


## [2026-09-05T13:51:00.880Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nimport re\nfor i,l in enumerate(lv):\n    if 'burIdan' in l or 'burrIdan' in l or 'burlDan' in l or 'burld' in l or 'burrld' in l:\n        print('leaf',i)\n        for x in l.split('\\n'):\n            if 'bur' in x: print('   ',x.strip()[:160])\n        print('---')\nEOF",
 "description": "Locate burīdan leaf in SNS_pages"
}
```


### [2026-09-05T13:51:02.570Z] TOOL RESULT

```
leaf 68
    burrldan                 :    j^ bhrlnant-i: of*** /br»y-:t-
---
leaf 78
    .^.^J-» .^O -tan p-»'                                       £                       •   y/T*S .cmU.*** :burld fistSd: yw»*»Aj
    k*   .   .j    -tan I pasSn:t**w«i*                          •0«**<u-*:burer:iisn: PSKWN, sn:              >» s «u»j3»«            y<
    0-^-)0'*o*:burIdan: PSKWN, tn: >* »>*|>4«*j
    •V/A^ (ilU^U.jl, .,£)      .   *£,,»£, :burrend:^               ^113^0
    \i                                         •»>*-«•»> : burred: >*
    f^\ji                                           MA-U/T** .aj^ :be burred :\e»)tf*»o -2b
---
leaf 237
    baj baxt 101/16          bavSnd 303/18                  b5y   I   p3k 111/5       burd 185/14
    bavisn 304/1                   bSzSh 107/13              burdan 108/16
    band 110/18              baxsiln 97/19                  b5zisn 107/18             burdar 108/13
    banded 33/6              baxt 97/10-11                  bozisnlgtar 108/2         burld 124/7
    bandend 33/4             Baxt Afrld 97/14               brad 102/9                burldan 124/12
    bandisn 32/20            baxtarlh 96/5                  brasnum 103/22            burld ested 124/9
    bar 101/19-20            be/be 105/10                   brazyag 102/13            burred 124/16
    bared 186/6-10           bfid    111/19                 brazyagtar 102/20         burrend 124/15
    barend 186/4             bSh 111/17                     brSh/brah 102/3           burrisn 108/20-124/
    barisn 186/1             b§ ka 105/18                    brfiheneh 105/1          burz 108/7
    barisnih 104/6           bfi    ke 105/22                brehenld 105/3           burzed 108/11
---
```


## [2026-09-05T13:51:11.011Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read();lv=t.split('\\f')\nprint(lv[68][:2500])\n\"",
 "description": "Print SNS leaf 68"
}
```


### [2026-09-05T13:51:12.573Z] TOOL RESULT

```
                                                «                                                                                                                                                  1

     UA                                                               UuU.jl,
                                                                                                                                                a^yUi tt^b MJb «ji^
                                                                                                                                                                                                        t<



                              «***                  AlS j>«           Ai£ jJJ*
                          •
                                         o*H°                 ,




                                                                                                   •   1T/A^


     (.-.1^^.^-LJ-i) .i/jAi-.Aijai..Aijji.                                            :br€hSnld :*»*_><£.

                                                                                                                                                M<».     9S1)        barasnta-                 ,
      pM-fOwlftiijili :br5h6nld                           Sst6d:                  *»irf«A**o»j-»0-^->                                                                                              &.
              •   )r/Y»       ^ .fj>>*.; br*hinlt istit:^ .*-•">
                                                                                                                           c>w*jl^UJifias dr0z M
                                                                                                                                                       barlSnUw-u^ -!•<>-
                                •
                                    o«*#t           0*f   ^ —     *   (j-1   )   o*** :brldan:           wf^
      burrldan                 :    j^ bhrlnant-i: of*** /br»y-:t-
          .«- »u          U*)                   ,»• »*.*«,        ciVAj-J 5* <***&•                     972)


                                                                                  •   ** i   be/bS :BR? :>h^|                 •mm,.   949-959) •£.„,        .   ,,
                                                                                                                                                                     '^ sbulanfl!                  ^
```


## [2026-09-05T13:51:22.906Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### TAD بورق ###\" && python3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read();lv=t.split('\\f');print(len(lv))\nfor i,l in enumerate(lv):\n    if 'بورق' in l: print('leaf',i); [print('  ',x[:200]) for x in l.split(chr(10)) if 'بورق' in x]\n\"; echo \"### NYB ###\"; grep -n \"brītan\\|brīdan\\|burīdan\\|babrak\\|babrag\\|bōr\\b\" NYB_vol2_glossary.txt | head -20",
 "description": "TAD and Nyberg"
}
```


### [2026-09-05T13:51:24.318Z] TOOL RESULT

```
### TAD بورق ###
87
### NYB ###
6496:brīdan, brīn-: brītan
```


## [2026-09-05T13:51:25.055Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### CHEUNG brai ###\" && grep -n \"\\*brai\\|bray\\|brīn\\|BRAY\\|brī-\" CHEUNG.txt | head -25; echo \"### HUB ###\"; grep -n -i \"bêl\\|bīl\\|Grabscheit\\|bôr\\|braun\" HUB.txt | head -20",
 "description": "Cheung and Hübschmann"
}
```


### [2026-09-05T13:51:25.119Z] TOOL RESULT

```
### CHEUNG brai ###
2620:22 *braiH 
2652:*braiH ‘to shave, shear, cut’ 
6155:*NEIR: Pash. Iwawol ‘to reap’, Yi. lorí-/lorei-, M. läri-/luriy-, Ishk. dbray-/dbred, 
8727:*CHORESMIAN: ? Trd- ‘to bray’ || (+ *upa-) b’Trd- ‘to roar’ => Samadi: 80, 18 
18582:*nar ‘to roar, bray, thunder ?’ 
18593:*CHORESMIAN: mjnr- ‘to roar, moan, bray’ (or mjnr- ?, cf. MacKenzie I: 544) 
18630:*NEIR: Pash. naral/nar- ‘to screech (of birds, etc.); to bray, bellow, low’ 
20145:express. ?), ? Zaz. lawayis/lawen ‘to bark’ || (+ *uz-) Zaz. zirayis/ziren- ‘to bray’ 
20146:*NEIR: Pash. rayal/ray- ‘to bray’, Oss. І. ræjyn/ræjd, D. rajun/rejd ‘to bark’, 
20153:*MISC: ? Par. ruh-/roita- ‘to bray’ 
55726:to bray 
56192:*braiH, *Hrais, *kap/f, 
57807:*braiH, *pas, *yap’, *xšau 
57808:*braiH, *paš, *xšau 
### HUB ###
2915:801. Dazu arm. asxSt Vothbraun* (vom Pferd), phi. sBtvars
7077:^) Dazu np. kahar = skr. kadrxi- *rotlibraun*, zd. kadrv0'{a3pa')^
8383:rothbraun' = zd. xsa^ta-, phi. setvars *rothhaarig, ri]). sed^)
9726:p. 89 unten. Hierher np. kahar *hellbraun* (Polak, Persien
9728:braun*, Geiger, Idg. F. IV, Anz. p. 23. Zn
```


## [2026-09-05T13:51:27.842Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2645,2700p' CHEUNG.txt",
 "description": "Cheung *braiH entry"
}
```


### [2026-09-05T13:51:27.891Z] TOOL RESULT

```
*IE COGNATES: Lith. bréksti ‘to break [of day], dawn’, Pol. o-brzasknaé ‘to become 
light’ 

*REFERENCES: IIFL I: 389b f.; Werba 1997: 467; Kiefer 2003: 193; ESIJa II: 184 ff. 


*braiH ‘to shave, shear, cut’ 


*AVESTAN: (+ *pari-) Y Av. pairi.bri- ‘to shave, shear’ = Liste: 40 
MED.; Pres. them. nà-: IND. 3р1. YAv. pairi.brinonte (V 17.2), INJ. 25р. Y Av. pairi.brinagha (V 17.4) 


*MIDDLE PERSIAN: MMP bryn-, BMP blyn- (PSKWN-) /brin-/ ‘to cut off, MMP 
bwr-, BMP bwr- /bur-/ ‘to cut off, sever’ (secondary formation, cf. Hübschmann 


1895: 28) = DMMPP: 111a, 117b 
Pres.: IND. 3sg. MMP brynyd || Pres.: IND. 3pl. MMP bwrynd, IMPV. 2sg. MMP bwr, Partic.: perf. pass. 
BMP blyt, BMP bwlytk /bridag/ (or /bur(r)idag/ ?), MMP bryd, Inf.: BMP /bridan/ 


*PARTHIAN: bryn- ‘to cut off — Ghilain: 111a | 

Pres.: IND. 3pl. brynynd; Partic.: perf. pass. bryd 

*KHOTANESE: OKh. barrai ‘sculptor 

*CHORESMIAN: m/Bn- ‘to shave, shear’ > Samadi: 39 

*NWIR: Widely attested: NP burridan/burr-, Zaz. birnayis/birnen- ‘to cut (off)', Bal. 
bur(r)it/bur(r)- ‘to cut’ (< Pers. ?), Kurd. birin/bir-, (also Sor.) wirm/wir- “о cut 
(off), shave’, Awrom. biriáy/bir- ‘to cut’, Abz. berida/berin-, Gur. (Kand) -ur-, 
(impv. birauwä), Ham. beriyän/berin-, Isfah. birintän/birin-, Delij. bar-bini, Siv. 
-bur-, Zaz. birn- ‘to cut’ (LW), Fariz. -bri-, Khuns. birn-, brin-/brina, (LW) 
bur-/bura, burna, Natan. -beri-, Semn. -brin-, Qohr. birid/bir-, Soi birit/-birn- ‘to cut 
(off)’, Tal. Быгып- ‘to shave’, Kurd. birin (Ё) ‘wound, injury’ (< *briH-nä-) 

*NEIR: Oss. I. elvynyn/elvyd, D. aelvinun/elvid ‘to shave’, Yghn. virin-/virita ‘to 
shear’, Ishk. varn-/vred ‘to shave, shear’, Wa. vrin-, vrun-/vrit ‘to shave, shear’, 


*bra(1)j 23 


Yghn. virin-, vérin-/virita ‘to shear off (wool)’, ? Yghn. viríc-, véríc-/virícta ‘to 
shave, shear’ (-c- < ?) || (+ *apa-) Pash. būrai ‘one whose nose, lips, ... have been cut 
off || (+ *a-) Oss. I. arviston ‘a mixture of hay and straw in pulverized form’ 
*SANSKRIT: bhri ‘to harm’ (RV+) = EWAia II: 282 

0 The root *’bar- : br- postulated in ESIJa II: 108 ff. is incorrect. 

«PIE *b'reiH- ‘to cut off (7) = LIV: 92 f. | Pok.: 166 

*IE COGNATES: OCS briti, Russ. brit’ ‘to shave’, etc., Olrish bronnaid ‘injures,
```


## [2026-09-05T13:51:39.656Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LEW forare/ferire/fricare ###\" && grep -n \"^foro\\|^ferio\\|^frico\\|^frio\" LEW_1910.txt LAT.txt | head -20; echo \"### SKT ###\"; grep -n \"^board\\|^bore (1)\\|^bore,\\|^brown\\|^beaver\\|^border\" SKT.txt | head -20",
 "description": "Latin etym dicts and Skeat"
}
```


### [2026-09-05T13:51:39.721Z] TOOL RESULT

```
### LEW forare/ferire/fricare ###
LEW_1910.txt:7220:foroind IT 445
LEW_1910.txt:7221:forosnain (mir.) IT 554
LEW_1910.txt:10737:friosan II 378 frisk, friscing II 354 friund II 364
LAT.txt:1381:foro proximum; ut "in tribunal" et "ad tribunal" uenire non unum est,
LAT.txt:20143:foro a quaternis hominibus nocte et die premi iustum est; factura,-ae
LAT.txt:21648:ferio, -Is, -Ire (verbe d 4 fectif; nne 3“ p. de pl. avec 4 largisse-
LAT.txt:23227:frico, uellico k c 6 te de frio, uell0): fonir, percer, M.L.34O3;
LAT.txt:24205:frico, -as, -ul, -ctun (et frlcdui, fricatum),-Ure: frotter. Ne
LAT.txt:30489:ferio est peu sensible, mais inuenio est plus populaire que reperio,
### SKT ###
2010:border,  an  edge.  (F.-O.  Dn.)  M.  E. bordurt,  Ch.  i»  F.  bordurt.  ••  Du.  boorti,  bor* :der,  edge;  orig.  the  same  word  as  Du. \^ni,  a  board ;  sec  alx^vc.
21309:boards  for  panel-work,  oa^
22876:brown — bruin.
```


## [2026-09-05T13:51:42.525Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC ###\" && grep -n \"bhrēi\\|bhrei\\|bhero-s\\|bhebhrus\\|bhe-bhru\\|bherō\" IEC.txt | head -20; echo \"### SYN cut/brown/beaver ###\"; grep -n -i \"burridan\\|burr-idan\\|bōr \\|babr\" SYN.txt | head -20; echo \"### WLD band3 ###\"; grep -n \"bhrēi\\|bawra\\|bhero\" WLD_band3.txt | head -20",
 "description": "Mann, Buck, Walde-Pokorny"
}
```


### [2026-09-05T13:51:42.596Z] TOOL RESULT

```
### IEC ###
1623:bhreit- ‘spike, sharp implement’. Cf. bhriió Lat. cf. frit (-1-?) “tip of corn-ear'; Br. brued ‘sley’; W brwyd "brooch" beside brwyden ‘sley’; Cz. břit, m., břiť, f. ‘cutting-edge’
### SYN cut/brown/beaver ###
14089:Av. bri- (only with pairi- ‘cut around’), NPers. burridan ‘cut’ : Skt. bhri- ‘injure’, ChSl. briti ‘shear’, britva ‘razor’. Walde-P. 2.194.
### WLD band3 ###
```


## [2026-09-05T13:51:50.306Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nn=0\nfor i,l in enumerate(lv):\n    if 'NPers. burridan' in l:\n        print('leaf',i,'printed p',i-24)\n        idx=l.find('NPers. burridan')\n        print(l[max(0,idx-900):idx+400])\nEOF",
 "description": "Buck page for 'to cut'"
}
```


## [2026-09-05T13:51:51.098Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21645,21660p;24200,24215p;23222,23232p' LAT.txt",
 "description": "Ernout-Meillet ferio frico frio"
}
```


### [2026-09-05T13:51:52.010Z] TOOL RESULT

```
leaf 611 printed p 587
 ‘knife, sword’) ; Lat. casirdre ‘castrate’. Walde-P. 1.448. Ernout-M. 160. Walde-H. 1.179.
Av. 6waras- : Grk. oépé ‘flesh’, perh. OHG dwerah ‘across’ (as ‘cut across’), root *twerk-. Walde-P. 1.751.
Av. bri- (only with pairi- ‘cut around’), NPers. burridan ‘cut’ : Skt. bhri- ‘injure’, ChSl. briti ‘shear’, britva ‘razor’. Walde-P. 2.194.
Pol. krq.
P. ‘cut
9.23 KNIFE
Grk. paxatpa Goth. Lith.  peilis
NG paxalpe ON knifr Lett. nazis, peilis
Lat. culter Dan. kniv ChSl.  nozt
a coltello Sw. knif SCr. noz
fr. couleau OE seax, cnif Boh. niiz
Sp. cuchillo ME knife Pol. néz
Rum. cufit NE knife Russ. oz
S scian Du. mes Skt.  gastra-, krli-churi
```


### [2026-09-05T13:51:52.050Z] TOOL RESULT

```
credo, etc.; v. ansai 1 'article fetialis), on e8t tent 4 de poaer nn
ancien 41 argiasement *dhes~ qui serait repr 4 sent 4 par italique fes-.
Cf. peut-etre anasi lat. fas.
ferio, -Is, -Ire (verbe d 4 fectif; nne 3“ p. de pl. avec 4 largisse-
nent en n, ferinunt, eat atteatde par Festus 160,3; 363,$..An t 4 moi-
gnage dea graaaairiena, ferio eapmnte 8on parfait A percutio, IcS:
percussi, ici (ferii eat rare et tardif, 8 ei. dans le Thea.),et son
participe A ico: ictus, cf. Phocas GLK V 438,13; tontefois feriturus
apparant A la fin de 1'Eapire): "frapper", dans tona lea aena dn not:
frapper 1'ennemi, nn nnr, la nonnaie, nne victime, a la porte; frapper
nn trait 4 , k canae de la victime qu'on frappait ponr la circonstance,
cf. Varr., E.H.a,4,9, init iis pacis, foedus cum feritur, porcus occiditur.
Enfin feriS appartient k la s 4 rie des nota imag 4 s qui expriment dans
la 1 . familibre 1 1 id 4 e de "d 4 pouiller, voler", comme le fr."taper,
estamper, ronler"; T 4 r., Ph.46/7 (dana la bonche d'nn esclave), porro
autem Geta | ferietur alio munere, ubi era pepererit; Prop. 3 , 3 , 49 - 5 °;
d'aprbs fodere nn pcp . fodentes, A.504; 1 'abrdgd de Festas, 74,13,
signale an infinitif d'an intensif-daratif en - 5 -, fodire)', fonir,
foailler, creaser, percer; = oxaTtTU), opuatK». - Ancien, asael. M.L.
3401 fodere (et fodlre, cf. fr. fouir).
Derivas en fod- et en foss -: fodico,-ds, fornation populaire; cf.
frico, uellico k c 6 te de frio, uell0): fonir, percer, M.L.34O3;
*f odiculo,-as, M.L.3404. ;
fodina f.: mine, M.L.3404a (argent i-fodlna)', fossa, -ae f.: fosse.
M.L.3460; britt. fos', fossd, -as (et confosso)', fossatum n. (l. des ar-
pentenrs et des nilitaires): fosse, M.L.3461; fossula, M.L.34638;
fossio (t.techn. de la 1.rurale); fossor (item ); fossilis "qui effodi
frite qu'on interprete ordinaireaent par fretu, fiducia.
Le'sens rappelle skr .dharayati "il tient", etc.; v. sons fer(r)umen
et sous firmus. - La racine £tant aonosyllabique, 1 1 -e- serait un
element de formation indiquant 1'etat (type sedere), ce qui convient
pour le sens.
frico, -as, -ul, -ctun (et frlcdui, fricatum),-Ure: frotter. Ne
s'eaploie qu r au sens concret, contraireaent a terere qui adaet aussi
le sens aoral ( tempus terere)', et appartient sans do ut e i la 1. popu-
laire. - Ancien, usuel. Panroaan, M.L.3501.
D^riv^s, presque tous techniques: frictio (Celse), -tor,-trix (rares,
tardifs), frictus, -us a. (Mart. Cap .), frictura (Ps. Apul. ), fricSt io
(Ceis.), -tor, fricdtus (Plin.), fricamentum, M.L.3500, fricatura,
M.L.3503; tous de la langue iaperiale. Les 1 . romanes attestent aussi
*fricicdre, M.1.3503; *frictdre et *frictidre M.1.3505,3506; -fri—
cium, usite surtout dans dentifricium.
Coaposes: af-, circum-, con- (c. genua sensu obsceno), de- M.L.aSaoa,
```


## [2026-09-05T13:52:17.102Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T13:52:17.109Z] TOOL RESULT

```


```


## [2026-09-05T13:52:20.805Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology of بریدن (borīdan/burīdan): Middle Persian form, Proto-Iranian, Proto-Indo-European root, cognates (Avestan), and any cited sources."
}
```


## [2026-09-05T13:52:22.811Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B1",
 "prompt": "Give the Persian section for بور: meaning, etymology (Middle Persian, Proto-Iranian, PIE root), and cognates. Also any Persian بور 'brown/chestnut'."
}
```


### [2026-09-05T13:52:26.608Z] TOOL RESULT

```
# Etymology of بریدن (borīdan/burīdan)

Based on the Wiktionary entry provided, here's what can be established:

## Documented Etymology

The entry states the word comes "From Middle Persian [script needed] (brydan /burr-/ brīdan/, 'cut', 'cutting off')."

Unfortunately, the source material provides **limited etymological depth**. Specifically:

- **Middle Persian form**: brydan/brīdan (meaning "cut" or "cutting off")
- **Proto-Iranian**: Not specified in the article
- **Proto-Indo-European root**: Not mentioned
- **Avestan cognates**: No Avestan forms are cited
- **Sources**: No academic sources are referenced for the etymology

## What's Missing

The Wiktionary entry lacks the deeper historical reconstructions you're requesting. It does not trace the word backward to Proto-Iranian, Proto-Indo-European, or provide comparative Avestan evidence. The etymology section only documents the Middle Persian ancestor without further etymological analysis or cited scholarly sources.

To obtain a complete etymological analysis, you would need to consult specialized historical linguistics resources beyond this dictionary entry.
```


### [2026-09-05T13:52:29.162Z] TOOL RESULT

```
# Persian Section: بور

## Meaning
The word بور (bur) functions as an adjective describing colors, particularly "fair, blonde" or "light brown."

## Etymology
According to the source, بور derives from Middle Persian (bwl /⁠bōr⁠/, meaning "reddish-brown, bay [horse]"), which evolved from Proto-Iranian *buHráh, and ultimately traces to Proto-Indo-European *bʰerH- ("brown").

## Cognates
The entry identifies related words across languages:
- Ossetian бур (bur, "yellow")
- Northern Kurdish bor ("grey")
- Shughni vůr ("brown, grey")
- Old Armenian բորենի (boreni, "hyena")

These demonstrate the widespread distribution of this color-related root across Indo-European languages, reflecting shared ancestry in describing brown and yellow hues.
```


## [2026-09-05T13:52:41.627Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B1%D9%82",
 "prompt": "Give the Arabic section for بورق (būraq/bawraq): meaning, etymology, source language (Persian? Middle Persian?), and any descendants (Latin, French, English borax). Also any Persian section."
}
```


## [2026-09-05T13:52:42.068Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/borax",
 "prompt": "Give the full etymology of borax, including Medieval Latin, Arabic, Persian forms, dates, and any note on boron and boric."
}
```


### [2026-09-05T13:52:46.943Z] TOOL RESULT

```
# Arabic Entry: بورق (bawraq)

**Meaning:** The term denotes "borax," a mineral compound.

**Etymology:** The word originates from Middle Persian *bōrag, which also gave rise to the Persian term بوره (bōra/bure).

**Source Language:** Middle Persian served as the donor language for this Arabic borrowing.

**Notable Descendants:**

The term spread widely across languages:
- **Medieval Latin:** baurach
  - **Anglo-Norman:** boreis → **Middle English:** boras → **English:** borax
  - **Italian:** borace
- **Ottoman Turkish:** بوراق (burak)
- **Persian:** Multiple variants including بوراق (burâq) and بورق (buraq)

The entry demonstrates how this mineral terminology traveled westward through Romance languages, eventually reaching English as the familiar "borax," while also remaining in Persian and Turkish variants.
```


### [2026-09-05T13:52:49.492Z] TOOL RESULT

```
# Etymology of Borax

**Timeline & Language Path:**
The word borax entered English in the late 14th century through Anglo-French *boras*, derived from Medieval Latin *baurach*, which came from Arabic *buraq*. The Arabic term likely originated from Persian *burah*. This etymological chain reflects how the substance traveled westward through trade and cultural exchange.

**Original Source & Usage:**
"Applied by the Arabs to various substances used as fluxes," borax was originally obtained in Europe from salt lake beds in Tibet, demonstrating its importance as a mineral commodity across Eurasian trade routes.

**Related Terms:**
The adjective *boracic* is etymologically connected to borax. Additionally, the chemical element **boron** (named in 1812) derives from borax plus a suffix borrowed from carbon. Humphry Davy originally termed it *boracium* because it was extracted from boracic acid, with *boric* serving as the related adjective form.

This linguistic journey illustrates how scientific nomenclature often builds upon earlier trade terminology, preserving ancient cultural contacts in modern technical vocabulary.
```


## [2026-09-05T13:52:55.763Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%84",
 "prompt": "Give the Persian section for بیل (bīl) 'spade, shovel': etymology, Middle Persian form, Proto-Iranian, any link to a root meaning 'to cut', and cited sources (Hasandust, Cheung, Horn)."
}
```


## [2026-09-05T13:52:56.648Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A8%D8%B1",
 "prompt": "Give the Persian section(s) for ببر: all senses (tiger, beaver?), etymologies, Middle Persian forms (babr, babrag), Proto-Iranian, and cited sources."
}
```


### [2026-09-05T13:53:01.599Z] TOOL RESULT

```
# Persian Section: بیل (bīl)

## Etymology

The word بیل derives from **Middle Persian** (Book Pahlavi needed): /bēl/, tracing back through Proto-Iranian *bádHr̥ to Proto-Indo-European *bʰódʰh₂-r̥.

## Linguistic Connections

The entry notes cognates including Latin *fodiō* ("to dig") and Serbo-Croatian *bȏd* ("sting"), suggesting an ancient root related to piercing or digging actions.

## Middle Persian Form

The documented Middle Persian form is **byl** /bēl/, preserving the long vowel characteristic of Persian vocabulary.

## Notable Features

- Pronunciation varies by dialect: Classical [beːl], Dari [beːl], Iranian Persian [biːl], Tajik [bel]
- The term means "shovel" or "spade" across Persian varieties
- A quotation from al-Ghazalī's 1105 work *The Alchemy of Happiness* illustrates historical usage

**Note:** The webpage does not reference Hasandust, Cheung, or Horn as sources for this entry.
```


### [2026-09-05T13:53:08.203Z] TOOL RESULT

```
# Persian Section for ببر

## Etymology 1
Inherited from Middle Persian *bpl* (babr, "tiger, lion, panther").

## Noun (Tiger meaning)
**ببر** (babr) - tiger; also means lion in Indo-Persian contexts. Plural forms: ببرها (babr-hā) or ببران (babrān).

## Etymology 2
Derived from Middle Persian *bplk'* (babrag).

## Noun (Beaver meaning)
**ببر** (babar) - archaic term for beaver. Plural: ببرها (babr-hā).

## Cited Sources
- MacKenzie, D. N. (1971), *A concise Pahlavi dictionary* - references "babr"
- Horn, Paul (1893), *Grundriss der neupersischen Etymologie* - lists etymology on page 42

## Note on Etymology
The entry traces both senses back to Middle Persian forms, with the tiger sense having broader Semitic cognates (Classical Syriac, possibly Akkadian origins).
```


## [2026-09-05T13:53:27.975Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### NYB babr ###\" && grep -n -i \"babr\\|bawr\\|Biber\" NYB_vol2_glossary.txt NYB_vol1.txt | head -20; echo \"### NYB brid context ###\"; sed -n '6490,6500p' NYB_vol2_glossary.txt",
 "description": "Nyberg glossary"
}
```


### [2026-09-05T13:53:28.029Z] TOOL RESULT

```
### NYB babr ###
NYB_vol2_glossary.txt:953:bawra-, bawri-.
NYB_vol2_glossary.txt:5071:bawra-, bawri-: bavrak
### NYB brid context ###
brad: brat
brahm: brahmak
brazinidar: brah
brehinesn "n RUNS : brihénisn
birhénasn |
brehinīdan: brihēnītan
brīdan, brīn-: brītan
brih(i): brāh
buland: ~
bum: ~
bun: ~
```


## [2026-09-05T13:53:29.445Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nprint('leaves',len(lv))\nfor w in ['بریدن','بیل','بور','ببر']:\n    hits=[i for i,l in enumerate(lv) if w in l]\n    print(w,hits[:20])\nEOF",
 "description": "Aryanpur headword search"
}
```


### [2026-09-05T13:53:32.132Z] TOOL RESULT

```
leaves 545
بریدن [125, 221, 273, 384, 395, 415]
بیل [12, 35, 36, 205, 371]
بور [11, 14, 25, 53, 123, 477, 478, 516, 541]
ببر [37, 144]
```


## [2026-09-05T13:53:39.598Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '945,960p;5065,5078p' NYB_vol2_glossary.txt",
 "description": "Nyberg bavrak context"
}
```


### [2026-09-05T13:53:39.640Z] TOOL RESULT

```
bavandak-mēnišnēh [~-myn&snyh] perfect thinking, perfect thought 53%. 70. 8515, — The Phl. rendering of Av. (335sqq.) Armaiti-.
bavandak-mčnišniha adv. with perfect thinking, attention 12118-19, —
Bävel [b’pyl] the name of the town of Babel and of its founder 11427. — OP Babiru- (read by Meillet et Benveniste Babairu- because of Pali Baveru); Ps. bbyly; MPrth b’byl (S).
bavētān [YEIWWN-yt'n'] pl. cas. obl. of bavēt ‘he will be’ (v. bütan) used as a
Baxt-xósró
subst. ‘he who will be’ = the future, coming man: har hastän butan bavētān all those who are, who have been, and who will be 5518, — Cf the use of Jv as a subst. in Apocal. 1:4.8 ó àv x«i 6 Av xal ó čpy0- uevoc.
bavišn [YHWWN-šn'] v. n. of bütan: the act of entering into material existence; material existence 109° (opp. vindsišn). — Corresponds exactly to the Arab. philo- sophical term kaun (opp. fasdd), Gr yeveoic. Cf bütak.
bavrak [bplk'] the beaver 8219. — Av. (925)
bawra-, bawri-.
Baxl [b’hl] Balkh 1132. — Av. Bāxtrī-, Bäxöt-; NP Balz.
(953)
baxšišn [HLKWN-šn'] distribution 89%. From baztan.
baxt [b’ht', bht'] destiny, fate, fortune: ~ u bāgēbaxt (g. v.) 7712-13; pat aueš m murtan to die a natural death 2112-13; bé-Sutak ~ whose fortune is gone, doomed 52; v. also vat-bazt.
baxtan [b'htn'; HLKWN-tn'] baxá-, to allot, to distribute, to destine 6620-23, 7624, 799-19, 891138; — -§ apar baxt &stet dušman čzančt (it has been allotted to him that he should kill =) Fate has destined him to kill the enemies 271%. — Av. (921) bag-; Ps. pt. bhty; MPrthPrs pres. baš- (S, A-H I), pt. batg; Paz. baztan, barš-; NP baxsidan.
Baxt-xösrö [bht hwslw] n. pr. of the king of the Arabs 1173. — A distorted and Tranized form of Ass. Nabi-kudurri-usur, Hebr and Aram Nébükadnassar, nbwkd’- swr, Gr Naßoxodovooop; in Phl. orthog- raphy *nbwhtnsr, *nbwhtswr (h = x, t = ô); the initial n- having been taken for w and eliminated, bwhtnsr, bwht’swr, etc. were variously interpreted: Arab lw. Buat-nassar; adaptations to the Iranian name system: Baxt-xosro, Patisrav (DkM 689°), Baxt-narsé (Pseudo-Balkhi, ed. by
www.parsianjoman.org | peal wb
a-bar-: avurtan
barog-: buržitan
barosman-: barsom
barozan-: bālēn
barozišta-: balist
Bastavari-: Bastvar
bawra-, bawri-: bavrak
bazu-: bazuk
bereg-, berojyastoma- : burZitan
borozant-: buland
bi-taéya-: téh
bitya-: bitaxs, dit
bi-zangra-: d6-zang
bratar-: brat
```


## [2026-09-05T13:53:41.388Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nfor i in (144,125,36,123):\n    print('===== leaf',i,'=====')\n    print(lv[i][:1600])\nEOF",
 "description": "Print ARY leaves"
}
```


### [2026-09-05T13:53:43.115Z] TOOL RESULT

```
===== leaf 144 =====
[pdf page 145]
۶ /_بيوگاني» ویوگانی (به چم"*عروسی") : :
[ ریعه! ۱
۱
اوستایی (/۸789742): ۷0۸ اسلاوی کهن (۲1اماة بزع#نایی 00 (شاپد) پچ 1
پهلری (۷1هالام۳): ۹ وا 7*۶
کردی (۸8015]7): ۸1 روسی (/5514۸ل)(شاید) ۷۳۹
اففانی (پشتر) (/۸۳0[1۸۸7): ۱۱یا لیترانی (7440۷/۸۷/)(شاید) ‏ ,۷۸۵۸8 ۱
سانسکریت (5۸۸/5/7): ۷۸3۰ ,۷۸17118 1 ت۷2 ۱
درد تون (لی) (71400ملا این ۷۸/67
لاتین (/47/0ل)(شاید) 8 ,۷۸8 ایرلندی کهن (1#/50 01.2)(شاید) 38010 ۱
گرتیک (0077716)(شاید) ,۲/۸ هتیت (2//77/2)(شاید) ات الا ید ۱
َ نی ادن
ایسلند یکهن (470/0/۸۷2۸(۷ع5 010)(شاید) پسگشت‌ها اش شبات ادن :
3 ۷507۸ زر اسر
آلمانی که (05821۸۸ ۶/0۶7 012)(شاید) 5 (۷30) ی ۱
۷ ۷۲877 291 :م02
آلمانی (08294۷)(شاید) 53 0۸31۸030 ,89 اقب
۷۷8۳75 10102 (60لا)
انگلیسی کهن (8۸0//974 012)(شاید) ۲۷80 7 (۷۲50) :0/1008
انگلیسی (7ل8اا6۸/0)(شاید) ,8۵ |7085 (۷80) ماه |
۷ 7 (62708) #مممصم |
سوئدی (377722/54)(شاید) ۷۸2 برهان قاطع : ۲و ۲۳۰۲ ۱
ملندی (01076)(شاید) ۱۷800821 ,۷3008
بادداشت:
۱ به جز واژه‌های هند و ایرانی» بقیه‌ی واژه‌های این فهرست محتمل هستند و به همین دلیل جلر آنها (شاید) آمده
است.
۲ واژه‌های فارسی "یوگ" و "ببرگ" و "بیو" و بهمچنین واژه‌ی کردی 811۴ با واژه‌های هند و ایرانی فهرست فوقق
خویشی نزدیکك دارند.

===== leaf 125 =====
[pdf page 126]
اا ‏ ااا گگ ی .
۱ بریدن / ۱۲۷
اسلواکی 51-07470): انشا ی ۱۱ پسگشت‌ها شهب درد
لیتوانی (۸۸/1۵27تا8ل7ل). ند دیا 0 20050
ایرلندی کهن (بغولگا صان): ۷۸ 1 (318شآ) دام دی ها
116160 ناه
1 :قلطم 2 #ملتهه)
یادداشت:
معنی این واژه در لاتین: گوسپنداخته شده,
| گس سوازی ناش ی 60۴
اوستایی (4۲5874/۷: 8۸07183/۸ ,8817۸ آلمانی کهن (/08/04۸0 210 0ا۵): ۱
8۸ +881 00۸ ,204020
پهلری (۲7ائل۸): ,8837۸۷ ,8178130۸ آلمانی (088000: ۰ 81308 ,207573
َ لا انگلیسی کهن 20/0870 صا0): ,تل۸ت808
اوستی (0555712): 71( 10
کردی(8013/7-: 88818۲ ,258۸31210 انگلیسی (701/520(ق): 208
سانسکریت (8۸(/58077): 87181 دانمارکی (0۸/37): ۸0
7 811۸8۷۸7 ,8118۸۵71 سوئدی (9(/52157): 3073۸ ,8083
ارمنی (0/52/۵9بم. " 21 نروژی (0070750107: 808
بونانی (07885): ۳۸08,83۸3۸0 اسلاوی کهن (۲10ما؟ 267ن 27 )+
لین مین بصع تور ۸ 2711
را 1 روسی (۷5914): ۱
ایتالیایی (42ال7۸): 0 لیترانی (777۸7۵۷/ل). 8ف328
ایسئند یکهن (/01014771۸(ی5 صا0۵): لدرنی (لتی) (7۲4۸ا): نی
بش80 آلبای (نمااله‌هام. 3 ,815
نورس کهن (۸۷07۶8 0ا0): 8۳87۸ با8087
فریزی کهن (54(7ل۲۸ صا0): 3

===== leaf 36 =====
[pdf page 37]
۸ ریشه‌های هندو اروپایی زبان فارسی
کهن هند و اروپایی اپن واژه چنین است: سانسکریت: 0۸۸/۳۸77 اوستایی ۴۳۸771 08070
یونانی:08870785. مثال دیگر واژه‌ی «نوه» است که همربشه‌های آن در زبان هند و اروپایی چنین
است: هند و اروپایی نخستین: 7 سانسکریت: ۸1۸77۸7 اوستابی ‎٩1۸3۸7‏ لانین:
58 آلمانی: ‎٩18۳۳8‏ انگلیسی: ایسلندی کهن:0۷3۳1 ایرلندی کهن:11۸٩‏
هلندی ۸7۳8۳ ایتالیایی: 5 لینوانی: 87۳۳0718 کردی: ‎٩3783۷1‏ سا کسو نی کهن؛ 90وی ..
این واژه‌های همريشه و واژه‌های مشابه دیگر رابطه‌ی خانوادگی هند و اروپائیان نخمتین را بطور"
تفریبی مشخص می‌کنند. ۱ :
۵- زناشویی: واژگان همربشه‌ی هند و اروپایی و متون کهن ایرلندی و ولزی و همچنین
اضانه‌های پونانی و رومی نشان می‌دهند که هند و اروپایی‌ها دارای گونه‌ای ازدواج و مراسم زناشویی
بودندکه با تأید و تحت نظ رکاهتان انجام می‌شد. ضمناً ازدواج نوعی معامله هم بود: داماد یا ایل او به
پدر عروش يا ایل عروس «هدیه؛ (مثلاً چند رس گاو) می‌دادند. در مقابل پدر عروس موظف برد که
جهیزبه عروس را تهیه کند. معمولاً مذا کرات وابسته به زناشویی طولانی بود.
ضمناً ون حقوقی گال‌ها و ایرلندی‌های کهن و همچنین حماسه‌های پاستانی (سانند آثار
هومر) نشان می‌دهند که رسم چند زنی نیز در میان توانگران هند و اروپایی رایج بوده است. ژول
سزار (2۸738۸ .7) درکتاب خو د (200ته 8811۵ 08)گزارش می‌دهد که تعدد زوجات
در میان اعیانگال رواج داشت و اگر شوهر به طرز سرا رآمیزی می‌مرد» زن‌های او مورد شکنجه قرار
می‌گرفتند. در حماسه‌ی ابلیاد (1۸0ن11) اثر هومر آمده است که پریام (/۳۸1۸3) شاه تروا دو زن
داشت. اولی هکوبا (180178۸]) برد که برایش نوزده پسر زائید. دومی لائوتو (۸07730]) بود.
که برایش دو پسر زایید.
عم سازمان ایل و امت: همانطور که در بالاگفنیم 1084 واژه‌یع «خانه» بود و واژه‌ی ریس
خانواده پا خانسا
===== leaf 123 =====
[pdf page 124]
3ج
برّموزء برّمور» برّمزء برّمر» برّموء بوز (به چم "زنبور) / ۱۲۵
یادداشت:
واژه‌های انگلیسی 81.00۸1 ,81088086 (و همریشه‌های ژرمنی آنها) نیز از همین واجریشه‌ی هند و اروپایی
آمده‌اند.
8۸7۸ ,8۸3۸2 ,8۸7۱/78 ,8۸336172
پپلوی (1مالهم: (۸۲۲۵185) 852 لیتوانی (۸(1۸/4ل 4 7/.): 8 و817]8
ساسکریت (54۸/۶8۵/7): 818۸۸/۸3۸ آتونی (لتی) (7۵/۷ا): 7
8۸/81۸۸ پروسی کهن (4۷ا59نا۲# ا0): ۰ 817785
لاتین (/710مل): 08 ایرلندی کهن (#اکلقا 0ا0): انا
ایسلند یکهن (ل۵/( 0ات5 صام. 8 گالی (0ل8لانا0۸): 2305
آلمانی کهن ((05۸۸/۸ ۲04 صاه): ولزی (7اک7): اد
انار
آلمانی (0874۸0): دازا پسگشت‌ها گت دش
انگلیسی کهن (تل5لل5(/0 طان): ردنا 6 ۶0020
انگلیسی (8(/01387): ادن 5 (888) جمترچید
دانمارکی (/0۸//3): 2 142 :م05
سرئدی (7ل8(75275): 3 4 (885) :28( مار
نروژی (/(2/0717201۵): 3 192 ۸0
هلندی (7ل007): 11 4 (852) :0/05
اسلاری کهن (10ما؟ تال صز): 3 (888) 37
ی 810175۸ برهان قاطع : ۳و ۳۱۶
ای چکه (62808:. ۷5۸ لغت‌نامه دهخدا: ۳۳۹
اسلراکی ماه ۷0۲5۸
یادداشت,
۱ واژه‌ی آانگیین" فارسی از آانگه" به چم "شیر ۰ و عسل" است(برهان قاطع :: ۱۷۴). واجریشه‌ی ۰81881 از هند و
اروپایی -8737* به چم "زنبور" است. واژه‌های "انگدان" و "انجبار" و "انگوژه" نشان می‌دهد که "انگه" به چم "یره
و شهد" است. لذا "انگیین" يا "انگویین " یعنی یره پا شهد" زنبور,
```


## [2026-09-05T13:54:02.488Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD bel ###\" && grep -n \"bēl\\|spade\" PHD.txt | head -10; echo \"### ARY bil leaf205/371 ###\"; cd incoming/ARY && python3 -c \"\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read();lv=t.split('\\f')\nfor i in (205,371,12,35):\n    print('=== leaf',i,'==='); print(lv[i][:700])\n\"",
 "description": "MacKenzie bēl and ARY bīl"
}
```


### [2026-09-05T13:54:04.024Z] TOOL RESULT

```
### PHD bel ###
256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
3756:spade bél.
### ARY bil leaf205/371 ###
=== leaf 205 ===
[pdf page 206]
توده ] ۲۰۷
| جماگلیس سرواژی ارس ۷۷۵۹69
کردی (7731ن): درا برتونی (/70ق88): 712
لاتین (4710مل): 4 ,10718 هتیت (1/77778): - 71022
گوتبک (607770): ۰ 73100 ,77770
ایسلندی کهن (010447(ی5 صته): پسگشت‌ها انشگ رش دا
رن رن را
آلمانی کهن (7(ف02804 07لا صام): 14 :47اه
۸ ,2107 اد اراد :223 بل 73متتهلط
انگلیسی کهن (#لقل200 صزم: 718800 3 (۳۸37) :0 ام
لیتوانی (140۷/له۸ل 7 آرم: 717 124 لها
تونی (لتی) (777۵27ا): 77۸ برهان قاطع + ۳۰
پروسی کهن (7نفاد۳۸75 ۰:0۵ 71۸10 لغت‌ نامه دهخدا: ۷۱۱۴
ایرلندی گهن (تادلها صا): 7 فرهنگ معین: ۱۱۶۵
گالی (نادلتنامه): 730
بادداشت.
۱ پسگشت‌های ابرانی ریشه‌های این واژه را نمی‌دهند.
۲- واژه‌های 7811700 ,781770016 ,0517803 هم از همین واجریشه آمده‌اند.
۳ چم این واژه در ای
=== leaf 371 ===
[pdf page 372]
اج وو وود دما
شانه (به چم "استخوان کلف" و "کثیف) / ۳۷۳
پسگشت‌ها آش‌ هرد ند 3 (813188) :5028 ۱۷۸
1 ۹ 8002 بق 2520 ۸00
3 (817885) رامیت نا برهان قاطع + ۱۳۳۰
پهلری (/۲اتنم۳): 5۳20۷۸ ,517201۸6 انگلیسی (7ل8(/05): 0710
بلوچی (اتلعتانلم8): ۰ 81120060 ,817۸4 دانمارکی (0۸2۷/34): 3 دراه ادن
افغانی (پشتر) (/4۳0/4۸4): 05۸ سوئدی (817820/374): 50008۸ ا
برنانی 02870): کلتشا5 ,اتمه نروژی (/۸/0775014): 3 را 8 هن
لانین (/47): شهاناقف؟٩‏ ,قاتا هلندی (7ل07): 3 دای اش
فرانسه (7ح/۳52): ۵۳۸5
اسپانیایی (8۳۸(/]5): 3۸ پسگشت‌ها اراد گرا ادا
ایتالیایی (97 ۳4 5۶۸3۸ 5 ۸0090
پرتغالی (ظ۳087001052: ۰ 3188۸21۸ 0 (5130110538) ۰ . مهد
گونیک (0077712): 315 9 (ا۲ن2۸۲) بالط
ایسلندی کهن (507210410 2ا0): یه ها
۱ 8۸ات
=== leaf 12 ===
[pdf page 13]
۴ ریشه‌های هندو اروپایی زبان فارسی :
آلمانی 43186077 لتونی 81:828؛ روسی 3۳:882۸) در برخی زبانها (مثلاً فارسی) از بین رفته
است و در زبانهای دیگر به گیاهان متفاوتی اطلاقی می‌شود. علت این دگرگونی آشکار است.
کوچگران وقتی به گیاه یا جانور تازه‌ای برمی‌خورند يا نام محلی را می‌پذپرفتند» یا نام جدیدی را
نوآوری می‌کردند و يا نام هند و اروپایی قدیمی را برای آن بکار می‌بردند. این فرآیند امروز اهر
صادق است. واژه‌ی «یخچالء (چاله‌ی یخ) را برای ابزار سرد ساز برقی بکار می‌پریم. واژه‌ی «سپر» را ۰۹ 48۶
که مدتها عملاً کاربرد روزمره نداشت برای بخشی از اتومبیل بگار می‌بریم, اصولاً ردیابی واژگانی
بیشتر روی همریشگی تاکید دارد نه هم چمی.

ضمناً همه‌ی واژه‌های همريشه (۲0011۸7) در تعیین خاستگاه هند و ار
=== leaf 35 ===
[pdf page 36]
۳۳۳۳۳
دیباچه / ۳۷
سرخپوستان امریکای مرکزی) مر تکب قربانی کردن انسان نیز می‌شدند. در متون سانسکریت در چند
مورد به قربانی کردن انسان اشاره شده است. ظاهراً در نظر هندیان پاستان» انسان والاترین جانداری
بودکه می‌توان برای تراضی خدایان قربانی کرد. در زمانهای تاریخی نیز رسم قربانی کردن انسان در
مین هند و اروپائیان ادامه داشت. مورخان یونانی و رومی مکرراً و با اشتمثزاز به این رسم در میان
اقوام ژرمنی و اسلاوی اشاره می‌کنند. شواهد نشان می‌دهد که خود یونانی‌ها و رومیان هم در ایام
کین‌تر همین کار را می‌کردند. مثلاً در داستان جنگ تروا آمده است که آقاممنون
(۸0۸۸/52/01011) فرمانده‌ی کل یونانیان؛ دختر خود را قربانی کرد تا خدایان باد مساعد برای
حرکت ناوگان یسونان بسوی تروا بفرستند. دو مورخ کهن»
```


## [2026-09-05T13:54:22.849Z] TOOL CALL #51: WebSearch

```json
{
 "query": "Persian بیل bēl spade etymology Middle Persian *badra- Proto-Iranian fodio Hasandust"
}
```


## [2026-09-05T13:54:24.595Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0erH-",
 "prompt": "What does this reconstruction page say: meaning of the root, derived terms, and descendants (Iranian, Germanic, Latin)? Is there a *bʰerH- 'to cut/pierce/bore' and a separate one 'brown'?"
}
```


### [2026-09-05T13:54:33.730Z] TOOL RESULT

```
Web search results for query: "Persian بیل bēl spade etymology Middle Persian *badra- Proto-Iranian fodio Hasandust"

Links: [{"title":"بیل - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%84"},{"title":"Reconstruction:Proto-Iranian/bádHr̥ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/b%C3%A1dHr%CC%A5"},{"title":"بلند - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%86%D8%AF"},{"title":"Dialectal Layers in West Iranian: a Hierarchical Dirichlet Process Approach to Linguistic Relationships","url":"https://arxiv.org/pdf/2001.05297"},{"title":"بلی - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%D9%84%DB%8C"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"},{"title":"Contributions to a relative chronology of Persian - ScienceDirect","url":"https://www.sciencedirect.com/org/science/article/pii/S221258842100003X"},{"title":"Proto-Iranian language","url":"https://en.wikipedia.org/wiki/Proto-Iranian_language"}]

Based on the search results, I can provide you with information about the etymology of the Persian word بیل (bēl, "spade"):

The Persian word بیل (bēl) is inherited from Middle Persian (byl /bēl/), which comes from Proto-Iranian *bádHr̥, from Proto-Indo-Iranian *bʰádʰHr̥, and ultimately from Proto-Indo-European *bʰódʰh₂-r̥. It can be compared with Latin fodiō ("to dig"), which shares the same Proto-Indo-European root.

The Proto-Iranian form shows variation in its reconstruction as *badra-, *badar-, *baddra-, *badadra-, *barθra-, and *barθrya-, deriving from the Proto-Indo-European root *bʰedʰh₂- meaning "to dig, pierce".

The search results also note some interesting dialect variations in Iranian languages that reflect this etymological line, including Balochi bard and Bashkardi bahr as related forms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-05T13:54:33.978Z] TOOL RESULT

```
# Proto-Indo-European *bʰerH- Root Analysis

Yes, this page documents **two distinct homonymic roots** sharing the form *bʰerH-.

## First Root: "Pierce/Strike"

**Meaning:** "to pierce" or "to strike"

**Key Descendants:**
- **Latin:** *feriō* ("to strike")
- **Germanic:** Proto-Germanic *barjaną* (English "bar")
- **Greek:** *pérthō* ("to destroy")
- **Balto-Slavic:** Lithuanian *bùrtis* ("sign"), Slavic *bъrtь* ("carving")

## Second Root: "Brown"

**Meaning:** "brown" (though scholar Donald Ringe states "an actual PIE word of [the requisite] shape and meaning is not recoverable")

**Key Descendants:**
- **Germanic:** Proto-Germanic *brūnaz* ("brown")
- **Indo-Iranian:** Sanskrit *bhrūra*, Persian *bōr* (reddish-brown colors), Hindi *bhūrā* ("brown")
- **Baltic:** Lithuanian *bė́ras* ("bay, reddish brown")
- **Beaver etymology:** Possibly *bʰébʰrus* derives from this root

The page explicitly categorizes these as "homonymic roots"—different etymological sources that coincidentally share identical phonetic form.
```


## [2026-09-05T13:54:43.304Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/board",
 "prompt": "Give the full etymology of board (Old English bord, Proto-Germanic, PIE root) and any mention of border and the PIE root *bherdh- 'to cut'."
}
```


## [2026-09-05T13:54:44.516Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/debris",
 "prompt": "Give the full etymology of debris: French débris, débriser, Old French brisier, Late Latin brisare, and the ultimate root."
}
```


### [2026-09-05T13:54:49.336Z] TOOL RESULT

```
# Etymology of Debris

The word "debris" traces back through multiple language stages:

**Modern English (1708):** The term entered English from French *débris*, meaning "remains, waste, rubbish."

**French origins:** French *débris* derived from the obsolete verb *debriser*, which itself came from Old French *de-* (a prefix meaning "down" or "away") combined with *briser*, meaning "to break."

**Latin connection:** The Old French *briser* descended from Late Latin *brisare*.

**Ultimate root:** The Late Latin *brisare* is "possibly of Gaulish origin," with a cognate found in Old Irish *brissim*, meaning "I break."

This etymology shows the word's development from a prehistoric Celtic root through Latin and French before arriving in English as a term for accumulated rubbish or waste from destructive processes.
```


### [2026-09-05T13:54:49.347Z] TOOL RESULT

```
# Etymology of Board

## Full Etymology Chain

**Board (n.1)** traces back through Old English *bord* ("a plank, flat surface") to Proto-Germanic *\*burdam*. The content suggests a possible PIE verb meaning "to cut" as the ultimate origin, though this connection isn't definitively established.

The text states: *"perhaps from a PIE verb meaning 'to cut.'"* This indicates uncertainty about the deepest root.

## Related Word: Border

**Border** has a distinct but overlapping etymology. According to the page, it derives from Old French *bordeure* ("seam, edge of a shield, border"), which came from Frankish *\*bord* or a similar Germanic source. The etymology notes: *"from Frankish \*bord or a similar Germanic source (compare Old English bord 'side')"*

## PIE Root *bherdh-*

**The content makes no mention of the PIE root *bherdh-* 'to cut'.** While the board entry mentions *"perhaps from a PIE verb meaning 'to cut,'"* it does not specify *bherdh-* or cite this particular root form.
```


## [2026-09-05T13:55:01.631Z] TOOL CALL #55: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%DB%8C%D8%AF%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B1%D9%82' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%84' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%A8%D8%B1' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 90 (Bher 3 / Bher 4): Persian nodes borîdan, bûr, bûreh/bûrq, bîl, babar' 2>&1 | tail -2; done",
 "description": "Archive Wiktionary sources"
}
```


### [2026-09-05T13:55:04.856Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/be34520268d14566.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fef201864b5f9478.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/320fb2e398e8d578.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f3be1263b45e3a0e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/51ffc641f79fea9b.txt
```


## [2026-09-05T13:55:11.074Z] TOOL CALL #56: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0erH-' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/b%C3%A1dHr%CC%A5' \\\n 'https://www.etymonline.com/word/borax' \\\n 'https://www.etymonline.com/word/board' \\\n 'https://www.etymonline.com/word/debris' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 90 (Bher 3 / Bher 4): PIE root, bîl reconstruction, borax/board/debris chains' 2>&1 | tail -2; done\nmkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg90.png data/verification/sources/refs/ocr/BOOK/90.png && echo copied",
 "description": "Archive remaining sources and copy page image"
}
```


### [2026-09-05T13:55:15.924Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/65e34851a92819f9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/438bf8132601ee08.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5caad4ca102d33a2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bf582f1536b978a7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1b445f637a642af9.txt
copied
```


## [2026-09-05T13:55:23.601Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LKT borax ###\" && grep -n -i \"borax\\|buraq\\|bûraq\\|bôraq\\|Borax\" LKT.txt | head -10; echo \"### AFM بورق ###\"; grep -n \"بورق\\|بوره\" AFM.txt | head -10; echo \"### PLA ###\"; grep -n -i \"borax\\|bauraq\\|bawraq\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10; echo \"### DEV ###\"; grep -n -i \"^BORAX\\|Borax\" DEV.txt | head -5; echo \"### FVQ ###\"; grep -n -i \"buraq\" FVQ.txt | head -5",
 "description": "Arabic borax loans in Lokotsch, Addi Shir, Asbaghi, Devic"
}
```


### [2026-09-05T13:55:23.687Z] TOOL RESULT

```
### LKT borax ###
982:[Aus  pers.  büräh]  'Borax,  borsaures Natron';  hieraus  mit  gleicher  Bedeutung sp.  borraj,  pg.  borax  [auch  tincal],  frz. borax,  it.  borrace;  ndl.  engl,  borax, dtsch.  Borax;  russ.  bulg.  bura,  serb. poln.  boraks.  cech.  borax.  [DE  241. Devic  DEt  70.
4668:'Borax'  [Pijn  63b;  aus  sskr.  tankana], hieraus  pers.  tängär,  ar.  tinkär,  tinkäl; liieraus  span.  atincar,  pg.  tincal,  atincal, frz.  tincal,  tinkal;  engl,  tincal,  tinkal 'Rohborax  (aus  Persien,  Indien  oder Tibet)'.  [DE  216.  Eguilaz  307/308. Devic  220/221.
5765:besehein  j.  2210 Beteigetize  St.  695 Betel  2149 betucht  j.  267 Betuchter  j.  267 Betuecliter  j.  267 Bezoar  1605 Bisam  293 ii/Mse  1647 Boback  181 ß��c/i^r  j.  180 Bombasin  16 17 Bonze  331 Borax  356 Boretsch  13 Borretsch  13 £os  j.  184  a Bronze  1657 Burnus  365 Burrich  13 5?<sa  376 Buxkin  324
6018:borax  356
6375:j  i>o«2;e  331 1  borax  356 I  bosan  376 1  botargue  274
7494:borax  356
8082:borax  356
### AFM بورق ###
834:( البورق) اضئاف مالم وجلى وارمنى ومصري وهو النطرون معرب بوره ومنة 
1431:( النودّري) حب ورقه ܒܝ بورق الفراسيون مر بع المذر وجذره قدر نصف 
1589:+ ( أ مجار) بات ܦܟ سديه بورق الرطبة عليه زغب لطيف كالغبار وله 
2579:4 الاون ذات عقّد صغيرة طية الرائحة ٠‏ ونماتها ماتصى بالا رض سُنيه بورق اللوف 
6061:( ® نات له ورق سُدِيهِ بورق الكر رم البري تعر بيب 8596 
6446:الصنوبر كثير الوجود في بلاد فارس «عقود الساق ورقه سُبيه بورق الياسسين. 
### PLA ###
3996:ob - buragqg: "Borax, borsaures Natrium" aus dem pers.e,„ börah mp .D1 
3999:burak, SYT. 25,02 ‚ mand. burgita 2, frz. borax, dtsch. Borax 3, 
5322:3» - büraqg: "Borax" aus dem pers. os bure ı mand. burgaita 2 frz. 
5323:borax, dtsch. Borax. 
5324:Borax mlat. borax er. bürak < pers. bürah 3 
### DEV ###
314:20.  Almisadre,  almisadir,  ahmzadîr,  amizadir,  anoxadic, anoiasier,  misadir,  mixadir,  muzadir,  musadi,  nysadir,  nusia- dat,  nestudar,  sel  ammoniac.  Tous  ces  mots  sont  des  alté- rations plus  ou  moins  fortes  de  l'arabe  ^:>l-àwJl  an-nochâdir ; comp.  les  formes  hispaniques  almojatre,  ahnohatre,  almo- crale,  nochalro.  Alinzadir,  borax,  est  le  même  mot.
848:Borax.  Esp.  horrcix,  borraj;  ital.  borracc.  De  l'arabe 1^^^  bauraq  ou  boUraq,  venant  du  persan  ii^y>  boûrah, même  signification,  ^^^o  est  dans  Bazi  (man.  déjà  cité, fol.  hq  verso),  et  Gérard  de  Crémone  transcrit  è^wrac/i.  Il n'est  pas  inutile  de  remarquer  que  le  borax  nous  vient surtout  des  pays  asiatiques;  Léman ^  dit  que  ce  mot,  em- prunté aux  Arabes,  s'est  introduit  dans  les  langues  euro- péennes vers  le  ix*'  siècle.
2222:TiNCAL  ou  TiNKAL.  Borax  brut.  Esp.  atincar,  portug. atincal,  tincal.  C'est  l'arabe-persan  JlSJo  tinkâl,  ou  ^\^  tin- kâr^  (en  persan  ;l^ou  tengâr).  Le  tincal  nous  vient  princi- palement de  l'Asie  (Perse,  Tbibet,  Inde).  Il  semble  qu'une sorte  de  confusion  se  soit  établie  entre  le  tinkâr  et  une autre  substance  appelée  en  arabe  ^^3  zindjâr,  en  persan
2228:On  ne  comprendrait  pas  que  le  borax  pût  être  confondu avec  le  vert-de-gris,  si  l'on  ne  savait  que  le  borax  brut, tel  qu'on  le  tire  de  certains  lacs  de  l'Asie,  est  coloré  en vert  par  des  substances  étrangères.
3075:Borax.
### FVQ ###
```


## [2026-09-05T13:55:37.401Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nfor i in range(16,23):\n    print('==== leaf',i,'====')\n    print(lv[i][:1200])\nEOF",
 "description": "TAD leaves around p.14"
}
```


### [2026-09-05T13:55:38.943Z] TOOL RESULT

```
==== leaf 16 ====
‫من ‪0110‬م تفاح‬      ‫حت ابطالى ‪010002‬وم أي فاح ذهى ‪05 .‬‬               ‫ادو‬
                                ‫و‪ 0500‬من ذهب ويقال له‪ 2‬الاسبانية ‪10‬‬

                     ‫ترك ه باشك اولى» وهونباث مسبت منوم‬              ‫ابنج‬


                                   ‫بنجرة ‪ -‬فارسي « ينجره » أي شباك‬


‫العلاملكيير‪--‬فارسي ‪ 2‬بند ‪ 26‬ممنأه عقدة ورباط دعي كذا لانه‬
                                                                              ‫‪0‬‬
                                                           ‫ربط عل السهم‬

 ‫وشاه بندر معناه‬      ‫ىء‬
                       ‫طعلى‬
                          ‫اسفن‬
                             ‫شط ال‬
                                 ‫لمرب‬
                                    ‫اناه‬
                                       ‫ار‪-‬سى « بندر ©مع‬
                                                      ‫فدر‬
                                                        ‫بن‬
                                                               ‫رئيس التجار‬
                                     ‫‪7‬‬                           ‫د‬
                      ‫أي اليوم الخسون‬    ‫مم يونانى ‪65‬‬

 ‫من بند‬    ‫وي او‬          ‫عامية من الايطالية ‪202‬‬ 
==== leaf 17 ====
                                ‫‪0 0‬‬


                          ‫سبلوان ‪--‬فارسي ‪ 3‬مبلوان » معناهبطلومكافح‬
  ‫بلى ‪ 85209‬معناه فى الاصل اليونانى كيس من جلد لحنظ‬     ‫وارصيةطا‬
 ‫جرة بأسهم‬    ‫اية‬
                ‫للتجار‬
                     ‫كهأاعما‬
                           ‫الدراءمويرادبهفي زماننامجلس التجاريجري في‬
                                                      ‫اولرابتحجار السفنالخ‬
 ‫وتقة وودقة ودوطة وبوانة ‏ فارسي ‪ 2‬لوده » وهو وعاء يديب الصائغ‬



             ‫وق ‪ -‬لاتيني ودأءعمط مرادفه الصور والناقور والتقير تفخ فيها‬

  ‫تق من برق أي لمم فنقل من العربية الى اللاتينية وبناا »«ة؟وط‬
         ‫‪5‬‬       ‫‪03‬‬       ‫‪5‬‬             ‫‪0‬‬      ‫‪ 59‬ع‬   ‫‪-‬‬     ‫‪75‬‬       ‫ع‬

                                                            ‫مرقش‪-‬‬
                                                                ‫بو‬
 ‫الحامض البورفي والنطرون منهطبيعي‬   ‫والىالفارسية « بوره ‪ 6‬وهو ملح حاصل من‬


  ‫وقد بوجدعلىضفاف الامبر في فارص وتيبت وكاليفورنيا ومنه ما حصل باعمال‬
 ‫النطرون فدعي كذ! هن وادي النطرون في‬
                                   ‫كياوية وهو خلاف اللطرون ‪ .‬أم ا‬

                                                      ‫‪ 11111‬ئيسه‬
   
==== leaf 18 ====
‫ينع فيمصر واللفظة مصرية ‪ .‬جاءففيبعضترجمات الاتميلكانلابسا البرفير‬
‫والارجوان وهو غاط والاصحكان لاسا البوص والارجوان أي كانلاب قيصاً‬
                                 ‫طويلا كمتنان ورداء من الارجوان أى العرفير‬
                              ‫وغاز ‪ -‬ترك « بوغاز مع»ناه خليجومضيق‬
‫وفاطة ‪ -‬عامية من الايطالية ‪6‬نههناط معناه غسل اشاب اء الرماد مرادفه‬
                                                                   ‫اميل‬
‫وليس ‪ - 72‬يوناني هعافادم معناه تديير المديئة وسياستها مرادفه الدّمرتط‬
                                                                      ‫وشحئة البلد‬
 ‫أيطالي ‪ 922‬اوم املنلاتينية *‪«6110‬معناء وصول وهو ورقة ‪.‬يدرج‬              ‫وليصة‬

                             ‫في بابان وصول درام وأمتعة وبضاعة وحو ذلك‬
                  ‫وقال ب يوناني وذلهعانزهط معناه كوزمنفخار“يشركب به‬
‫للمحذاء‬
      ‫فهملالعه ا‬
               ‫وادق‬
                  ‫ويا‪ -‬تركي « بوي »ا ممناهصبغوخضاب ولونمر‬
                           ‫معناه طابعم رأدفه طابعبريد‬       ‫ول | ايطاللي ‪0‬‬

 ‫بيقة والعامة تقول بأقبة ‏ يوناني داعااط وفي اللانينية ‪ 2017‬وهي الكرسة‬
          ‫بييدر ‪ -‬ارامية د بيت إدرا » بمعنى أى موضع ‪:‬درس فيه المنطة‬
 ‫نبادة ‏ فارسي « بياده » معناه الم
==== leaf 19 ====
 ‫بير| ح ايطالى همءنط من المرمانية «عنة عرببها جعة تصنم من مخمير الشعير‬
                                                      ‫وزهر نباد"؛ «واطنمط‬
           ‫بيرمون ‪ -‬ونانى معناه أستعداد لعيد مامن ‪ 02276153530‬استعد‬

      ‫بات يي قال ثبت فى السين‬         ‫وشه»و‬
                                          ‫باشلف‪-‬اورفسية ‏ بي‬
           ‫فبرة‬
              ‫حثش‬
                ‫وناه‬
                   ‫بدش ونخش ‪ -‬عامية مأخوذة من الايطالية ‪0‬عتاط مع‬

 ‫ببعة ‏ ارامية « بعدنا » مركة من« ب » معنىفىزائدة و «عدتا» ومعناعا‬
               ‫بحمكنيسةوليست‪ 9‬ببع»ة من بيعن»ا ابميمناهابيعة‬
                                                  ‫راجعبركار‬     ‫ببكار‬

     ‫بيك عامية ايطالى ‪0061‬م وهو منحث من حديد تنحث به الحجارة‬

                        ‫امك درق ‪:‬وله مضاء كبروانينوعام‬
‫بمارستان ‪ -‬فارسيمركب من « بما» أي مريض و ‪١‬‏ ستان »أداة تدلعلى‬
                                                ‫ظلرف المكان وهو المستشفى‬
            ‫ببوردي وببورادي ‪ -‬رق معناه أمر ومرسوم وعربيه القليد‬
 ‫ايطالى عمده؟‪.‬ممهزم معناه منخفض جبوري وها صفتان للمبوت وهو‬        ‫يأو‬
 ‫آله طرب ذات مجسات محرا الاوتاراتحاسية اخترع سنة ‪١‬‏ آلا مرادفه حدرة‬
                                      
==== leaf 20 ====
                              ‫ا‪4‬ع‪1‬د‪ #‬ست‬
                          ‫‪#‬أننوس ‏ بوناني ‪ 5008061‬معناه لشنج الاعصاب‬

                ‫تازه وطازج ‏ فارسي « تازه ‪ 6‬ممناه جديد وحديث وطري‬
     ‫تأبوروي!نا‪-‬ني ‪81006‬ها معناه نوظنرظرية وتعليم نظري واعتبار وتأمل‬
                           ‫نفاانر‪-‬سي ‪ 3‬تنبان » وهو سروالصغير‬
‫حيث منكأء فتقل الى‬        ‫نبغل مشتق من أسمجزبرة في المكسيك ‪0‬‬

 ‫التركية تنباكووهو المعروف بالدخان ويعضهم يقول نتن من التركية « لوبون ‪6‬‬
                                 ‫ومعناه دخان وعرابه بعض الاطياء ‪ 2‬طباق »‪6‬‬
‫تخت فارسي « تخت ونخته© معناهأوح من خشب فتوسعوا فيهفصار برأد به‬

                                  ‫سربر وعرش وباي مختعندهمعاصمة الممك‬
  ‫تراخوما ‏ يوناني ‪#‬ددة‪:‬ادهء معناه خشونة مرادفه الرمّد الذي يصيب العين‬
                ‫نراطور ري « تراطور وطراتور © مرادفه افاويه وتوابل‬
                       ‫رينتينه ‏‪ ٠‬لاتيني مدننلاهاده! معناه دهن الم‬
          ‫عامي افرشي ‪ 637761‬معناه حد واعل مرادفه وفكواواث‬            ‫رم‬
        ‫ات نوناني ‪ )5002611‬ممناه حار وهو نبات له حب مر الطعم‬

‫من‬    ‫معناه مقياس الحرارة وهو ‪5‬‬         ‫‪ 7000-05‬توناني ‪0020‬‬

                                            ‫عار و ‪ 8074607‬قياس‬    
==== leaf 21 ====
                                                            ‫غهرن‬
                                                               ‫صم إ‬
                                                                  ‫مشح‬

                                                            ‫‪0‬‬                             ‫‪8‬‬       ‫‪٠.‬‬       ‫‪0‬‬         ‫‪.‬‏‬
                                                 ‫عقار معطى ضد مهش السباع ‪:‬وهو دواء دم السموم‬


‫‪١‬‏‬             ‫تا ‪ - 00‬لنظهندي براد به لسيعج منحربر أو كان شفاف تزادقة اكيت‬

     ‫ْ‬                                         ‫تفتكه ‪ -‬ترك وهو البارودة والرصاص الذي برى به‬
‫اتق مساه الكتابة عن بعدوهو مركت ‪9‬مفن‪1‬فااغاية ونهاية ‪١‬‏‬
                                                     ‫نن‬‫وف”؟‬
                                                          ‫نغرا‬
                                                             ‫تل‬
                                                                                      ‫وحد و ‪:010‬ع كدب‬

‫"لفون س بوناني معناه الخاطبة عن بعد وهو مركب من ‪506‬ة غاية وتهاية |‬
     ‫ْ‬                                                                            ‫وحد و‪ 8201‬أي صوت‬

‫ثق عن ( ليد » أي عامومنها
==== leaf 22 ====
                                     ‫« بيت ثور » في الارامية أي ببتالنار‬
                               ‫لوهبوزوبدرق‬
                                         ‫تتكارا»‬       ‫كابس‬
‫كدري « ‪ 4 5‬وهو حديد تمزو ج بالقصدير يدق صفائح وتكجي‬
                                                                   ‫صائفه‬
   ‫رق‬
    ‫لسطعند‬
         ‫انحا‬
            ‫وال ‪ -‬فارسي ه ‪:‬وبال ») ويهتومسااقط من الحديد وال‬
                                                     ‫مرادفه حتات وسحالة‬
                             ‫ونيا فارسي وهو حجر يكتحل بمسحوقه‬
‫‪ 0‬معدنية ‏ يقال لهفي الجرمأنية زرنك معان وهو معدن لذن بددّقصفاتم‬

     ‫ل‬                                          ‫عيراني « ‪0‬‬       ‫توراة‬

‫مونى اسة وهو مشتق من « ألراه © أي القى ووضح و « نوره ‪ 4‬في الفارسية‬

                                                            ‫ناهشراعة‬
                               ‫كح اران ( تنكننا ‪#‬هعناه رياط وشل"‬
‫تبارو ‪ -‬ايطالي ‪:‬دعا من اليونائي دمء‪ 2681:‬معناه مشهد ومنظر مرادفه‬
                      ‫حضر وملهى وملعب ‪ .‬ومكان الممثلينفييقاهل ‪ 4‬شل‬
                                                 ‫‪ -‬انظر دغار‬
                            ‫تفوس ‪ -‬نونابي ‪ 5000‬براد به الى الحرقة
```


## [2026-09-05T13:56:35.112Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT around bawra ###\" && sed -n '16660,16700p' BRT.txt | head -50; echo \"### BRT brī search ###\"; grep -n \"pairi.bri\\|pairibri\\|brdiOro\\|bri-\\b\" BRT.txt | head -10",
 "description": "Bartholomae bawra- column and brī-"
}
```


### [2026-09-05T13:56:35.179Z] TOOL RESULT

```
### BRT around bawra ###
KompE.  (s.  «w't    —    Zam  V.  iag--.   —   mp.  räo»m(sd.ya  baxiaiti  Y.p.  azf.
öaxiir.  —  0  Vgl.  \t.  S.  34.  „,;[  j  'zuteilen,  austeilen':  ^maÄml  hls
•  j.  baxa^ra-  il  'Anteil,  Portion':  *'ra  zaoiw  *äbaxiöAfa  "nach  deinem  Gefallen F.  ;&■>;  —  sairimananqm  'räi  Vyt52(?).  teile  sie  aus"  Y.j;^,  io'>,
KompE.  —  Zorn  V.  ia}r-.  —  Pu.:  Wjrrj);  s.  mit  n  'austeilen  an— '(Dat'):  ta  (näml. noch  No.  2.   -   n  Hds.  •xira.    -    >)  Pü.:  ^^^j        vtboxsaiti  äbyS  daitiAubyS  seilte
..  d«u  DST.  ZA.  3.  680.-J)  Geschr.  baar ;  |  (naml^Aj/o^)^,  ^^  *■  47;  34- np.  katx ;  aus  ar.  *iAaitr' ;  vgl.  in  bäitrl-  nnd
Hau.  PSl  33.
•  j.,  g.  baxs-  V.  'Anteil  haben,  geben'. Praes,  i  l>ax/-,2  baxsa-,  30 (Itcr.) ^lur/a)«-.
i)  'Anteil  haben  an  — ,  inne  haben; Anteil  nehmen  an  — ,  bekommen',  mit Akk.  oder  Gen.:  nöil  .  .  avsstryö  .  . Aum»rjtsis{sd.)  baxs'täY. 31. 10;  —  tiuiasSt nSii  baxiaiti  vahiitahe  auhSus  "und,  wenn er  gestorben  ist,  wird  er  des  besten  Lebens nicht  teilhaftig"  V.5.61;  —  asäuni  cdis (sd.)   yä    il    cicä    vahistä     hanarp    (sd.)
'hwahmät  zacsät  dngi'S  baxsaili  (3SKA.)  1  aitm^al  'tanqm  (nämL  yavaaqm)  aOavai ".  .  soll  .  ,  der  ZJn^enosse  (daran)  teil ;  abatanqm  V.  7,  35.
haben?"    Y.  47.  5'';    —    vanäayalil   (sd.)        KompE.—  Et.?  Vgl.  Var.  6axr.   Bed.?    Das yqm    natdiitqm   gttl>am    dr?gi-i    baxsaitt       Wort ^steht^^wischen  .^ox/a- und  Wa-.- Pa.: ".  .   das    nachbarliche    Haus,    das    (jetzt  |       "     *       "^""^  ''' noch)  der  i>«^gläubige  (Fürst)  inne  hat"  j  •  p.  ba''da'ka-  Adj.  (fem.  'kä-')  'Untertan; Y.  s°-  3*' j  —  y^  *^  ■  ■  ftaema  . .  gava  \  Untertan,  Vasall':    imä   dahyuve^  tyä  .  .
■•Erweiteniiig'  ans  ia^-,  sd.;  S  1?ft  5-  —  "P- inssiäaH  'schenken'.  —  Pü.:  iaxiilani  s.  noch No.  1,  a,  5.  —  ■)  Pfi,  «L:  i'ästai  tu  pa  api- yasi  I  15  därrnd.  —  i>  D,  i.  das  jetit  noch lut  falschen  Religion  hälL  Pü.  etl.:  kti  an andar  därisn  afi  stänend.  —  3)  Vgl,  N.  /tf nnter  2.  Falsch  Dsr.  ZA.  /.  104.  —  *>  Ganz falsch  DsT.  ZA.  2.  144;    Tgl.  Hbm.  PSl  131
tn  np.  daxiüdan.  —  5)  Vgl.  zSL  Gun.  KZ.  JO. SI8.  Pü.  erl,:  ö  ariämUn.  —  *)  F I.  NA. "hA.  —  7)  An  den  folgenden  NP.  des  Pron. rel.  —  8)  Gdn.  BB.  l£.  258  will  'lurückgeben, vergelten'.     Das  väre  aber  doch  eher  paitiJf.
•  j.  bata-  Adj.  'geschrotet',  vom  Getreide:
dby  Google
9^5
bawra-
banda-
926
manä  'ks  (NPf.)  äh^is  ".  .  die  .  .  mir untertaa  waren"  Bh.  /.  7 ;  —  dadarÜs  .  . Manä  'ia*  Bh.^,  3,  2.  7;  6,  10,  14,^.6,  9, 14.  5- 1.
Eig.    'der   Qemands)  Fesseln  trägt'.   —    np.
ianfl'fl  'Sklave'.
•  j.  bawra-  m.
%risatanqm  'rc
"Biberkleider  1
Ytj.  129- Ableit.  ■ ahd.  bibar;
'Biber':  bawraini  vastra  . . iqm  *caturS  elzanatqm{s6..) 3n  dreihundert  Bibern  . ."
)  Vgl.  ^baufray;  ^    mp.  b<ne/rat, .    a.  vgl.  babkräii-   Adj.    'rotbraan', auch  Tiernanie;  1.  noch  GlrPh.  /  b.  49.
•  j.  'bawray-m.'Biber',  f. 'Biberweibchen': yat  asti  'ris  sragsta  yä^a  yat  asti  gaonS.- t?ma  'ris  öavaili  upäpö  "da^  Biberweibchen ist  am  schönsten,  insofern  es  am  dichtesten behaart  ist;  der  Biber  ist  ein  Wassertier" Yt.5.129').
VgL  baniro;  —  ")  Ich  halte  das  Game  für spätere  Zotat,  nicht  nur  die  letzten  drei  Worte.
•  j.  Tiawray-  m.  Name  einer  Stadt, Babylon:  tarn  yazala  aus'..  dahakB  TSil\ paiti  daifihaove  Yt.  5.
VgL  iSiirav-.
•  j.  bawrinay-  Adj,  'vom  Biber  stammend, Biber"';  'wraini'^  (APn.)  vasträ  .  ,  Sma- tanam  bauiranqtn  (sd.)  Yt.5.  129.
Ableit.  aus  bawra-.  —  Vgl.  lit  bibrinis  {io- Stamm).  —  ')  Statt  •■wrim  geschr.,  S  ^S.  9. (S.  noch  ipmaiiil,  liispö .tailü,  iailayc^
•  j.  'baoha-,  bangha-''>  m,  i)  Name einer  Pflanze*'  (und  deren  Saft),  die  auch zur  Kind  sab  treibung  benutzt  wurde:  asia kana  frabaraiti  'him  vä  iaffym  vü  .  . kqmcii  Vä  vTtaananqtn  urvaranqm  V.  i^. 14.  z)  Name  eines  aus  jener  Pflanze hergestellten  Narkotikums '>  und  zugleich
dvär^nts  yä  bqnayitt  ahüm  maniSnS  "zu- sammen gingen  sie  darauf  zu  A.  über, durch  den  sie  das  Leben  der  Menschen krank  machen"  Y.^jo.ö".
Vgl.  got.Äoiy o 'Wunde',  ahd.  *a«fl' Verderben'». —  S.  auch  'band-.  —  Pü.;  vimärhtilan,  erl. : ähökcmian.  —  ■>  S  3g6.  3.  —  ')  Vgl.  dagegen IQ  ^aAümM-.  —  j)  Doch  a.  Zupitza  Gu(t,  30.
•  j.  banta-  Adj.  (fem.  °tä-)  'erkrankt; krank,  siech':  ä/riti  .  .  yä  .  .  avanhmHt bandayeiti  'hmca  drSm  k»rmaoiH  ".  .  die den  Nichtkranken  krank  werden  lässt  und den  Kranken  gesund  macht"  V.  22.  s  ;  — fravalayS  .  .  yä  .  ,  dä%rT/  'iäi  drvatättm Vl/J.  24;  —  Ha  F.  16.
KompE.  (fl*%  av).  —  PHP.  wm  V,  ian-,  — Vgl.  bazda-.  —  Pfi.:  vimär.
•  j.,  p. "band- V, 'binden'.  Pr^es.  8  *ba»ad-z band-'\  34  bandaya-.  —  PPfP.  basta-'^.
r)  'binden,  fesseln':  is'ar  pasca  puxl>m bandum  (sd.)  bandyät^''  Vd./3;  —  dazdi tm  .  .  ydha  .  .  bandayem  .  .  franrasyämm Uta  basttm  vätayeni  uta  bastfm  upana-
\yeni  bast?m  ,  .  Yt.5,  '^J  —  haosrava  .  .
### BRT brī search ###
```


## [2026-09-05T13:56:40.496Z] AGENT

Now I'll write the verification file.


## [2026-09-05T14:04:33.903Z] TOOL CALL #60: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk90.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\ndata = {\n \"pdf_page\": 90,\n \"book_page\": 60,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Bher 3, Bhrei\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *bʰerH- 'to pierce, strike, cut with a sharp tool' (Pokorny 3. bher- 133-135) with the i-extension *bʰreyH- 'to cut off, shear' (Pokorny bhrēi-, bhrī- 166; LIV² 92f.)\",\n   \"note\": \"Both root labels and both page numbers are right. Pokorny 133 heads '3. bher- : mit scharfem Werkzeug bearbeiten: ritzen, schneiden, spalten; bhoros \\\"Abschnitt, zu Planken geschnittenes Holz\\\"', and Pokorny 166 heads 'bhrēi-, bhrī- Erw. von bher- \\\"mit scharfem Werkzeug schneiden, usw.\\\"'. Watkins/AHD prints the same root as 'bher-2. To cut, pierce, bore. [Pok. 3. bher- 133]'. Nourai's decision to put the two under one box is Pokorny's own (bhrēi- is explicitly an 'Erweiterung' of bher-). Modern notation: *bʰerH- (Lat. feriō, PGmc *barjaną) and *bʰreyH- (Av. pairi.brī-, OCS briti). The gloss 'to cut, pierce' is accurate; the language label 'Indo-European' is right.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰerH- «سوراخ کردن، زدن، با ابزار تیز بریدن» و گسترش ای‌دار آن *bʰreyH- «بریدن، تراشیدن». پوکورنی در صفحهٔ ۱۳۳ ذیل «bher- ۳» می‌نویسد «با ابزار تیز کار کردن: خراشیدن، بریدن، شکافتن» و در صفحهٔ ۱۶۶ ذیل «bhrēi-, bhrī-» آن را صراحتاً «گسترشِ bher-» می‌خواند؛ پس یکی‌کردن این دو در یک جعبه، کار خودِ پوکورنی است نه ابتکار نورایی. واتکینز (AHD) نیز همین ریشه را «bher-2: بریدن، سوراخ کردن، مته زدن» آورده و به پوکورنی ۱۳۳ ارجاع داده است. نام زبان، شمارهٔ صفحه‌ها و معنای ریشه هر سه درست است؛ ادعای نورایی در این جعبه درست است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰerH-\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:133\", \"status\": \"supports\", \"note\": \"POK_01.txt (leaf 142 ends with the printed numeral 133): '3. bher- … spalten; bhoros \\\"Abschnitt, zu Planken geschnittenes Holz\\\"' — grep 'scharfem  Werkzeug' in POK_01.txt.\"},\n    {\"ref\": \"POK:166\", \"status\": \"supports\", \"note\": \"POK_01.txt line 2391: 'bhrei-, bhri- Erw. von bher- \\\"mit scharfem Werkzeug schneiden, usw.\\\"'; the printed numeral 167 falls inside that entry, so the entry begins on p.166.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 334, s.v. bher-2\", \"stance\": \"supports\", \"note\": \"'bher-2. To cut, pierce, bore. … 4. O-grade form *bhor-d- in Latin forāre … [Pok. 3. bher- 133.]'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 2652, s.v. *braiH\", \"stance\": \"supports\", \"note\": \"'*braiH \\\"to shave, shear, cut\\\" … «PIE *bʰreiH- \\\"to cut off\\\" = LIV: 92 f. | Pok.: 166'\"},\n    {\"src\": \"SYN\", \"where\": \"SYN.txt leaf 611 = printed p. 587 (9.22 'to cut')\", \"stance\": \"supports\", \"note\": \"'Av. bri- (only with pairi- \\\"cut around\\\"), NPers. burridan \\\"cut\\\" : Skt. bhri- \\\"injure\\\", ChSl. briti \\\"shear\\\", britva \\\"razor\\\". Walde-P. 2.194.'\"},\n    {\"src\": \"WLD\", \"where\": \"WP II 159 f. (bher-3) and WP II 194 (bhrēi-), cited at the foot of Pokorny's two entries; WLD_band3.txt (Register) silent\", \"stance\": \"supports\", \"note\": \"Pokorny closes p.135 with 'WP. II 159 f.' and Buck cites 'Walde-P. 2.194' for the bhrēi- group — the two Walde-Pokorny places Nourai's root box needs. Only Band 3 (index) is on disk locally.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"brây\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan has the root brī- 'to cut, shear', attested only with the preverb pairi- : Vd. 17.2 pairi.brīnəṇte 'they cut off (the hair/nails) all round', Vd. 17.4 injunctive pairi.brīnaŋha, and the compound brōiθrō.taēza- 'sharp-edged'. Nourai's citation form 'brây' is simply the Avestan root as Horn (1893) writes it — Horn no. 212 sets it up as 'aw. √bray-', the full-grade shape of the present stem, beside which Bartholomae (Studien II 107 n.4, 180) preferred a root bhar- of which bhrī- is a 'Weiterbildung'. Both spellings denote one and the same root, PIE *bʰreyH-, so the node is right; only note that the ONLY actually attested Avestan forms are the pairi- compounds, never a simplex *brāy-.\",\n     \"derivation_fa\": \"در اوستایی ریشهٔ brī- «بریدن، تراشیدن» تنها با پیشوند pairi- گواهی شده است: pairi.brīnəṇte «گرداگرد می‌برند» (وندیداد ۱۷٫۲) و صفت مرکب brōiθrō.taēza- «تیزبُر». صورت «brây» که نورایی آورده همان است که هُرن (۱۸۹۳، شمارهٔ ۲۱۲) به شکل «اوستایی √bray-» می‌نویسد، یعنی ستاک حال با درجهٔ کاملِ آوایی؛ بارتولومه در «مطالعات» ریشه را bhar- گرفته و bhrī- را گسترشِ آن دانسته است. هر دو نگارش به یک ریشه اشاره دارند و از *bʰreyH- هندواروپایی می‌آیند؛ ادعای نورایی درست است، تنها باید یادآور شد که صورت ساده و بی‌پیشوندِ آن در متون اوستایی گواهی نشده است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰerH-\"],\n     \"ref_check\": [\n      {\"ref\": \"HRN:49\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 70 (printed '- 49 -'), no. 212: 'burrīden, burīden \\\"schneiden\\\" — aw. √bray- \\\"schneiden\\\", pairi.brīnenti, pairi.brīnaŋuha; phlv. burītan …; ai. √bhray-, bhrīnáti \\\"versehren\\\"'. This is verbatim Nourai's Avestan form and gloss.\"},\n      {\"ref\": \"BQT:270\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 490 (printed p.270), Mo'in's footnote 5 on بریدن: '… پهلوی …، سانسکریت …«بارتولمه»؛ قطع کردن، جدا کردن' — an etymological footnote that cites Bartholomae for the Old-Iranian antecedent.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 2652-2660, s.v. *braiH\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: (+ *pari-) Y Av. pairi.bri- \\\"to shave, shear\\\" … Pres. them. nā-: IND. 3pl. YAv. pairi.brinəṇte (V 17.2)'\"},\n      {\"src\": \"BRT\", \"where\": \"BRT.txt (grep 'pairi.bri', 'brī-')\", \"stance\": \"silent\", \"note\": \"The OCR of Bartholomae's AiW is too corrupt in the br- columns for the entry to be recovered; no hit for any spelling of the root. (Bartholomae's own view is reported at second hand by Horn p.49 n.2.)\"},\n      {\"src\": \"SYN\", \"where\": \"SYN.txt leaf 611 = p.587\", \"stance\": \"supports\", \"note\": \"'Av. bri- (only with pairi- \\\"cut around\\\")' — confirms both the root and the restriction to the pairi- compounds.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"brîdan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian brīdan, present stem brīn- (Book Pahlavi ideogram PSKWN-tn' < Aramaic psq, phonetic blytn' / blyn-; Manichaean bryd, bryn-) 'to cut, cut off', continues Old Iranian *bri-na- (the nā-present of *braiH-), the same stem as Av. pairi.brīnəṇte; Parthian has bryn- as well. Beside it MP already has the secondary formation burīdan, bur- (bwl-ytn'), built on the zero-grade with anaptyctic u; MacKenzie prints 'burīdan, bur- … = brīdan'. So Nourai's Pahlavi form is the older and better one, and the arrow Avestan → Pahlavi is regular: intervocalic-free *br- is kept, the Av. nā-present brīn- gives MP brīn-, and the past stem brīd- gives the infinitive brīdan.\",\n     \"derivation_fa\": \"فارسی میانه brīdan با ستاک حال brīn- (به خط پهلوی کتابی با هزوارش PSKWN-tn' و نگارش آوایی blytn'/blyn-؛ مانوی bryd, bryn-) «بریدن» دنبالهٔ ستاک ایرانی باستان *bri-na- است، همان ستاک نون‌دارِ اوستایی در pairi.brīnəṇte؛ در پارتی هم bryn- دیده می‌شود. در کنار آن، صورت ثانوی burīdan / bur- (bwl-ytn') از درجهٔ صفرِ ریشه با واکهٔ میانجی u ساخته شده که مکنزی خودش آن را «= brīdan» می‌آورد. بنابراین صورتی که نورایی آورده صورت کهن‌تر و درست‌تر است و پیوند اوستایی ← پهلوی از نظر تحول آوایی بی‌اشکال است؛ ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/بریدن\"],\n     \"ref_check\": [\n      {\"ref\": \"SNS:105\", \"status\": \"supports\", \"note\": \"SNS_pages.txt leaf 68 — identified as printed p.105 from the book's own index (leaf 237: 'brēheneh 105/1', 'brehenīd 105/3', 'bē ka 105/18', all on the same leaf). The leaf carries the entry ':brīdan:' followed by 'burrīdan : … bhrīnant-i … /brāy-:' — i.e. Tavoosi glosses the Shāyast-nē-Shāyast form as burrīdan and refers it to Skt. bhrīnanti and Av. √brāy-, exactly Nourai's chain.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"PHD.txt line 287 (MacKenzie p.19)\", \"stance\": \"supports\", \"note\": \"'brīdan, brīn- [PSKWN-tn' < A psq; blytn', blyn- | M bryd, N …] cut'; and line 287 further on 'burīdan, bur- [bwl-ytn' | M bwr-, N ~] = brīdan.'\"},\n      {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 6496 (Pahlavi–Pāzand/NP concordance)\", \"stance\": \"supports\", \"note\": \"'brīdan, brīn-: brītan' — Nyberg's glossary carries the same lemma.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt s.v. *braiH, 'MIDDLE PERSIAN' paragraph\", \"stance\": \"supports\", \"note\": \"'MMP bryn-, BMP blyn- (PSKWN-) /brin-/ \\\"to cut off\\\", MMP bwr-, BMP bwr- /bur-/ … (secondary formation, cf. Hübschmann 1895: 28)'; '*PARTHIAN: bryn- \\\"to cut off\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"borîdan «بریدن»; bor «ـبُر ۵»; bîl «بیل»\", \"verdict\": \"disputed\",\n     \"derivation\": \"Two of the three words are right, the third is not. (1) بریدن borīdan/burrīdan 'to cut' is the direct continuation of MP brīdan/burīdan; the modern standard form generalises the secondary u-stem (burr-), whence بُریده, بُرش and the agent compounds شیشه‌بُر، سنگ‌بُر، آهن‌بُر — confirmed by Cheung 2007 ('NP burridan/burr-'), Buck p.587 and Pokorny p.133 itself ('npers. burrad \\\"schneidet\\\"'). (2) بُر bor 'cutter', the bound present stem -بُر of that verb, is the same word — confirmed. (3) بیل bīl 'shovel, spade' is DISPUTED. Nourai follows Horn no. 237, who took over de Lagarde's connection 'zu aw. √bray- \\\"schneiden\\\"' and explained the vowel as imāla of an older bāl. Modern scholarship rejects this: MP bēl (byl, MacKenzie p.18 'bēl … spade') is derived from Proto-Iranian *badHr̥ / *badra- 'digging tool', Proto-Indo-Iranian *bʰádʰHr̥, PIE *bʰódʰh₂-r̥ from *bʰedʰh₂- 'to dig, pierce' — the root of Latin fodiō 'I dig' and OCS bodǫ 'I stab' — with Balochi bard and Bashkardi bahr as the Iranian cognates. That is a different PIE root from *bʰerH-/*bʰreyH-, so this one arrow of the node is superseded.\",\n     \"derivation_fa\": \"از سه واژهٔ این جعبه دو تا درست است و یکی نادرست. ۱) «بریدن» دنبالهٔ مستقیم فارسی میانهٔ brīdan/burīdan است؛ فارسی نو ستاک ثانویِ burr- را عمومیت داده و از همان «بُریده»، «بُرش» و ترکیب‌های «شیشه‌بُر، سنگ‌بُر، آهن‌بُر» ساخته شده است — چونگ (۲۰۰۷)، باک (ص ۵۸۷) و خودِ پوکورنی (ص ۱۳۳: «npers. burrad») آن را تأیید می‌کنند. ۲) «ـبُر» همان ستاک حالِ همین فعل است و درست است. ۳) اما «بیل» پذیرفتنی نیست: نورایی از هُرن (شمارهٔ ۲۳۷) پیروی کرده که به تبع دِلاگارد آن را «به اوستایی √bray-» بسته و «ی» را نتیجهٔ اِماله دانسته بود. ریشه‌شناسی امروزی این را رد می‌کند: فارسی میانهٔ bēl (نزد مکنزی byl «بیل») از ایرانی باستان *badra-/*badHr̥ «ابزار کندن» و آن از هندواروپایی *bʰedʰh₂- «کندن، فروبردن» است — همان ریشهٔ لاتینی fodiō «می‌کَنَم» — با هم‌ریشه‌های بلوچی bard و بشکردی bahr. پس این یک پیکان از سه پیکانِ جعبه، بنا بر پژوهش امروزی، به ریشهٔ دیگری تعلق دارد.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/بیل\", \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/bádHr̥\", \"https://en.wiktionary.org/wiki/بریدن\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:133\", \"status\": \"supports\", \"note\": \"POK_01.txt, first lines of 3. bher-: 'Ai. (gramm.) bhr̥ṇāti \\\"versehrt\\\" = npers. burrad \\\"schneidet\\\"; av. tiži-bāra- \\\"mit scharfer Schneide\\\"' — Pokorny p.133/134 does name the New Persian verb, as Nourai claims. It says nothing about بیل.\"},\n      {\"ref\": \"BQT:270\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 490 = printed p.270, Mo'in's footnote 5: 'بریدن — بضم اول و فتح چهارم و تخفیف و تشدید دوم (هردو) … سانسکریت … «بارتولمه» ؛ قطع کردن، جدا کردن — عبور کردن، گذشتن'.\"},\n      {\"ref\": \"HRN:59\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 80 (printed '- 59 -'), no. 237: 'bēl \\\"Grabscheit\\\". Zu aw. √bray- \\\"schneiden\\\" (de Lagarde, Ges. Abh. 297). np. bēl statt bāl beruht auf Imāla.' Horn does say what Nourai says — but this 1893 view is the one modern work rejects (see derivation).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt s.v. *braiH, 'NWIR' paragraph\", \"stance\": \"supports\", \"note\": \"'Widely attested: NP burridan/burr-, Zaz. birnayiš/birnen-, Kurd. birin/bir- …' — but Cheung lists no بیل under this root.\"},\n      {\"src\": \"PHD\", \"where\": \"PHD.txt line 256 (MacKenzie p.18)\", \"stance\": \"partial\", \"note\": \"'bēl [byl | (M byl), N ~] spade' — the MP word exists, but MacKenzie gives it no etymology and does not link it to brīdan.\"},\n      {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt leaf 125 = pdf p.126, printed p.127, s.v. بریدن\", \"stance\": \"supports\", \"note\": \"Aryanpur's بریدن entry lists Avestan, Pahlavi, Ossetic, Kurdish, Sanskrit BHRI-, Armenian, Greek, Old High German and English BORE under one IE root — the same family Nourai draws.\"},\n      {\"src\": \"SYN\", \"where\": \"SYN.txt leaf 611 = p.587\", \"stance\": \"supports\", \"note\": \"'NPers. burridan \\\"cut\\\" : Skt. bhrī- \\\"injure\\\", ChSl. briti \\\"shear\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Germanic\", \"words\": \"borôn\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *burōną / *borōn 'to bore, pierce' > OHG and OS borōn, OE borian, ON bora, MDu./Du. boren, MHG born, G. bohren; the derived noun OHG bora 'drill', OE bor, byres. It is the o-grade verbal of PIE *bʰerH- 'to pierce', beside Latin forō, -āre 'to bore through' (Pokorny remarks that the Latin and Germanic verbs have the same meaning but different ablaut). Watkins/AHD sets it out exactly so: 'bher-2 … 1. Germanic *borōn in Old English borian, to bore'.\",\n     \"derivation_fa\": \"ژرمنی آغازین *borōn/*burōną «سوراخ کردن، مته زدن» که به آلمانی علیای کهن و ساکسونی کهن borōn، انگلیسی کهن borian، نورس کهن bora، هلندی boren و آلمانی امروز bohren رسیده و اسم ابزار OHG bora «مته» از آن ساخته شده است. این فعل صورتِ درجهٔ o از ریشهٔ هندواروپایی *bʰerH- «سوراخ کردن» است، در کنار لاتینی forāre که پوکورنی تصریح می‌کند «معنایش همان است ولی درجهٔ آوایی‌اش متفاوت». واتکینز نیز عیناً می‌نویسد «ژرمنی *borōn در انگلیسی کهن borian». ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/board\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 334: 'bher-2. To cut, pierce, bore. 1. Germanic *borōn in Old English borian, to bore: BORE.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"POK_01.txt, 3. bher-, printed p.135\", \"stance\": \"supports\", \"note\": \"'ahd. as. borōn, ags. borian, aisl. bora, -aða \\\"bohren\\\"; ahd. bora \\\"Bohrer\\\", ags. bor, byres ds.'; and on p.134 'forō, -āre \\\"bohren, durchbohren\\\" (Bed. wie ahd. borōn, aber im Ablaut verschieden)'.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 110 (printed pp.190-191), s.v. 'bore, to pierce'\", \"stance\": \"supports\", \"note\": \"'ME. borien, fr. OE. borian, rel. to ON. bora, Swed. borra, Dan. bore, OS., OHG. boron, MDu., Du. boren, MHG. born, G. bohren, fr. I.-E. base *bher-, \\\"to cut with a sharp point; to bore, pierce\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"bore\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English bore 'to pierce' < Middle English borien < Old English borian, the direct reflex of Germanic *borōn; the noun bore 'hole, calibre' is deverbal from it. (The homonyms bore 'tidal wave' < ON bára and bore, past tense of bear, belong to bher-1 'to carry' and are not meant here.) One step, wholly uncontroversial.\",\n     \"derivation_fa\": \"انگلیسی bore «سوراخ کردن، مته زدن» از انگلیسی میانهٔ borien و آن از انگلیسی کهن borian، بازتاب مستقیم ژرمنی *borōn؛ اسمِ bore «سوراخ، قطر لوله» از خودِ همین فعل ساخته شده است. (همنامِ آن، bore به معنی «موجِ مد» از نورس کهن bára و نیز bore گذشتهٔ bear، به ریشهٔ دیگری یعنی *bʰer- «بردن» تعلق دارند و مقصود این جعبه نیستند.) این پیوند یک‌مرحله‌ای و بی‌مناقشه است؛ ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/board\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the parent node's AHD citation covers it ('Old English borian, to bore: BORE').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 110 (printed pp.190-191), s.v. bore\", \"stance\": \"supports\", \"note\": \"'bore, tr. and intr. v., to pierce. — ME. borien, fr. OE. borian …'\"},\n      {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 334\", \"stance\": \"supports\", \"note\": \"'Germanic *borōn in Old English borian, to bore: BORE.'\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Latin\", \"words\": \"forare; ferîre; frîcare\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three Latin verbs belong to the root box, though to its two halves. forō, -āre 'to bore, pierce' (whence forāmen 'hole') is a denominative of *bhorā 'the boring', o-grade of *bʰerH-; feriō, -īre 'to strike, smite, cut' is the e-grade of the same root (Ernout-Meillet: 'frapper, dans tous les sens du mot'); both stand under Pokorny's 3. bher- on pp.134-135. fricō, -āre 'to rub' belongs instead to the second half of the box, Pokorny p.166 bhrēi-, where 'Lat. friō, -āre \\\"zerreiben, zerbröckeln\\\", fricō, -āre \\\"reiben, abreiben\\\" (von einem *fri-co-s \\\"reibend, schabend\\\")' is listed. Since Nourai's root box explicitly reads 'Bher 3, Bhrei', drawing all three from it is correct.\",\n     \"derivation_fa\": \"هر سه فعل لاتینی به همین جعبهٔ ریشه تعلق دارند، اما به دو نیمهٔ آن. forāre «سوراخ کردن» (که forāmen «سوراخ» از آن است) فعلِ اسم‌بنیاد از *bhorā، یعنی درجهٔ o از *bʰerH-، است؛ ferīre «زدن، ضربه زدن، بریدن» درجهٔ e از همان ریشه است و اِرنو–مِیه آن را «زدن، در همهٔ معناهای کلمه» می‌آورد؛ هر دو زیر «bher- ۳» پوکورنی در صفحه‌های ۱۳۴–۱۳۵ آمده‌اند. اما fricāre «مالیدن، ساییدن» به نیمهٔ دوم جعبه یعنی صفحهٔ ۱۶۶ (bhrēi-) تعلق دارد که پوکورنی در آن «لاتینی friō و fricō» را آورده است. چون نام جعبهٔ نورایی صراحتاً «Bher 3, Bhrei» است، کشیدن هر سه پیکان از آن درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰerH-\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 334 covers forāre only: 'O-grade form *bhor-d- in Latin forāre, to pierce, bore: FORAMEN; BIFORATE, PERFORATE.' Watkins puts feriō under a separate entry and does not list fricāre here, so the AHD citation supports one of the three verbs; Pokorny (which Nourai also cites in the root box) supplies the other two.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"POK_01.txt, 3. bher-, printed pp.134-135, and bhrēi- p.166\", \"stance\": \"supports\", \"note\": \"p.134 'Lat. feriō, -īre \\\"stoßen, hauen, schlagen, stechen, treffen\\\" … forō, -āre \\\"bohren, durchbohren\\\" … forāmen \\\"Loch\\\"'; p.166 'Lat. friō, -āre \\\"zerreiben, zerbröckeln\\\", fricō, -āre \\\"reiben, abreiben\\\"'.\"},\n      {\"src\": \"LAT\", \"where\": \"LAT.txt (Ernout-Meillet) lines 21648 s.v. ferio and 24205 s.v. frico\", \"stance\": \"supports\", \"note\": \"'ferio, -īs, -īre (verbe défectif …): \\\"frapper\\\", dans tous les sens du mot'; 'frico, -ās, -uī, -ctum … -āre: frotter. … Ancien, usuel. Panroman, M.L.3501.'\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 110, s.v. bore\", \"stance\": \"supports\", \"note\": \"Klein lists under I.-E. *bher- 'L. ferire, \\\"to strike, smite\\\", forare, \\\"to bore, pierce\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"perforate, interfere; friction, debris\", \"verdict\": \"plausible\",\n     \"derivation\": \"Three of the four are exact. perforate < Lat. perforāre (per- + forāre), 15th c.; interfere < Old French (s')entreferir 'to strike one another' < Lat. inter + ferīre, originally of a horse striking one hoof against another; friction < Lat. frictiō, -ōnis, noun of action to fricāre. debris, however, does not come from any of the three Latin verbs printed in the parent box: it is French débris (in English from 1708), from obsolete débriser, from de- + briser 'to break', from Late Latin brisāre, probably of Gaulish origin (cf. Old Irish brissid 'breaks'). Nourai's own root box still covers it, because Pokorny puts 'gall.-lat. brisāre \\\"frangere\\\", frz. briser' precisely under bhrēi- on p.166; so the word is in the right family but hangs from the wrong Latin parent. Hence plausible rather than confirmed.\",\n     \"derivation_fa\": \"سه واژه از چهار واژه دقیق است: perforate از لاتینی perforāre (per- + forāre)؛ interfere از فرانسهٔ کهن entreferir «به هم زدن» از inter + ferīre که نخست دربارهٔ اسبی می‌گفتند که سمّش به سمّ دیگر می‌خورد؛ friction از لاتینی frictiō، اسمِ مصدرِ fricāre. اما debris از هیچ‌یک از این سه فعل لاتینی نمی‌آید: از فرانسهٔ débris (ورود به انگلیسی در ۱۷۰۸) از فعل متروکِ débriser، از de- + briser «شکستن»، از لاتینی متأخر brisāre که احتمالاً خاستگاه گُلی (سِلتی) دارد. با این حال خودِ جعبهٔ ریشهٔ نورایی آن را پوشش می‌دهد، زیرا پوکورنی در صفحهٔ ۱۶۶ ذیل bhrēi- می‌نویسد «gall.-lat. brisāre \\\"frangere\\\"، فرانسوی briser». پس واژه در خانوادهٔ درست است ولی پیکانش از پدرِ نادرست کشیده شده؛ به همین سبب «با احتیاط پذیرفتنی» ارزیابی می‌شود.\",\n     \"sources\": [\"https://www.etymonline.com/word/debris\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is printed on this node; the parent's AHD citation covers PERFORATE only.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 110 (pp.190-191), s.v. bore\", \"stance\": \"supports\", \"note\": \"Klein's cross-reference list at the end of 'bore' names 'foralite, foramen, interfere, perforate, pharynx' — i.e. exactly Nourai's first two English words.\"},\n      {\"src\": \"POK\", \"where\": \"POK_01.txt, bhrēi-, printed p.166\", \"stance\": \"partial\", \"note\": \"'mit s-Erweiterung hierher gall.-lat. brisāre \\\"frangere\\\", frz. briser usw. … air. brissid \\\"bricht\\\"' — supports debris for the ROOT but not for the Latin parent forāre/ferīre/fricāre.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Indo-European\", \"words\": \"bherd\", \"verdict\": \"confirmed\",\n     \"derivation\": \"PIE *bʰerdʰ- 'to cut' (Pokorny writes it bheredh-, p.138: 'bheredh- \\\"schneiden\\\", bhr̥dho- \\\"Brett\\\"'), a dh-enlargement of *bʰerH-, with Sanskrit bardhaka- 'cutting, shearing; carpenter' and śata-bradhna- as its Indo-Iranian witnesses. Watkins prints it 'bherdh-. To cut.' The chart's shortened spelling 'bherd' is Klein's, whose board entry sets up 'I.-E. *bhr̥dóm, resp. *bhr̥etóm, fr. base *bherd-, \\\"to cut\\\", a -d-enlargement of base *bher-, \\\"to bore, pierce, perforate\\\"'. Root, gloss and the arrow from the parent root are therefore all correct.\",\n     \"derivation_fa\": \"هندواروپایی *bʰerdʰ- «بریدن» (پوکورنی در صفحهٔ ۱۳۸ آن را bheredh- می‌نویسد: «bheredh- بریدن، bhr̥dho- تخته»)، گسترشِ dh-دارِ ریشهٔ *bʰerH-؛ گواه هندوایرانیِ آن سنسکریت bardhaka- «برنده، تراشنده؛ نجّار» است. واتکینز آن را «bherdh-: بریدن» می‌آورد. املای کوتاه‌شدهٔ «bherd» در نمودار، املای کلاین است که در مدخل board می‌نویسد «از پایهٔ *bherd- \\\"بریدن\\\"، گسترشِ d-دارِ پایهٔ *bher- \\\"سوراخ کردن\\\"». ریشه، معنا و پیکانِ آن از ریشهٔ مادر، هر سه درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/board\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:182\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 107, which carries the printed numerals 182/183, s.v. 'board, n., table, plank': '… fr. I.-E. *bhr̥tóm, resp. *bhr̥etóm, fr. base *bherd-, \\\"to cut\\\", a -d-enlargement of base *bher-, \\\"to bore, pierce, perforate\\\". See bore, \\\"to pierce\\\"'. Page and content match Nourai's citation exactly.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"POK_01.txt, printed p.138, s.v. bheredh-\", \"stance\": \"supports\", \"note\": \"'bheredh- \\\"schneiden\\\", bhr̥dho- \\\"Brett\\\". Ai. bardhaka-ḥ \\\"abschneidend, scherend\\\", m. \\\"Zimmermann\\\" … WP. II 163, 174.'\"},\n      {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 335\", \"stance\": \"supports\", \"note\": \"'bherdh-. To cut. 1. Zero-grade form *bhr̥dh- in Germanic *burd-, plank, board, table … [Pok. bheredh- 138.]'\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"Germanic\", \"words\": \"BURD : board\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *burdą 'plank, board' < PIE zero-grade *bʰr̥dʰ-o-m, literally 'a cut piece (of wood)'. Attested in Gothic fōtu-baúrd 'footstool', Old Norse borð 'plank, table', Old English/Old Saxon bord, Old High German bort, Dutch bord, beside the extended *bredą (OE/OS bred, OHG/MHG bret, G. Brett). Umbrian forfo- in furfant 'they lay on the board' is the Italic match Pokorny cites. Nourai's capitalised 'BURD' is simply his notation for the reconstructed Germanic stem.\",\n     \"derivation_fa\": \"ژرمنی آغازین *burdą «تخته» از درجهٔ صفرِ هندواروپایی *bʰr̥dʰ-o-m، تحت‌اللفظ «پارهٔ بریده‌شده (از چوب)». گواه‌های آن: گوتی fōtu-baúrd «زیرپایی»، نورس کهن borð «تخته، میز»، انگلیسی کهن و ساکسونی کهن bord، آلمانی علیای کهن bort، هلندی bord، و در کنارشان صورت گسترش‌یافتهٔ *bredą (انگلیسی کهن bred، آلمانی Brett). پوکورنی همتای ایتالیکِ آن را در اومبریایی forfo- در furfant می‌بیند. حروف بزرگِ «BURD» در نمودار صرفاً شیوهٔ نگارش نورایی برای ستاکِ بازسازی‌شدهٔ ژرمنی است؛ ادعای او درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/board\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this node; the parent's KLN:182 and the child's AHD cover the step.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"POK_01.txt, printed p.138, s.v. bheredh-\", \"stance\": \"supports\", \"note\": \"'bhr̥dho- in got. fōtu-baúrd n. \\\"Fußbrett\\\", aisl. borð n. \\\"Brett, Tisch\\\", ags. bord n. ds., ahd. bort ds. = umbr. forfo- ds. in furfant'.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 107 (pp.182-183), s.v. board\", \"stance\": \"supports\", \"note\": \"'ME. bord, \\\"table, plank\\\", fr. OE. bord, rel. to ON. borð, \\\"plank\\\", Goth. fōtu-baúrd, \\\"footstool\\\", lit. \\\"foot board\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"English\", \"words\": \"board, border\", \"verdict\": \"confirmed\",\n     \"derivation\": \"board < ME bord < OE bord 'plank, table; side of a ship' — a straight inheritance from Germanic *burdą. border is the same Germanic word taken back into English through French: Old French bordure 'seam, edge of a shield' from border 'to edge', from bord 'edge, border', itself a Frankish loan (*bord) into Gallo-Romance; hence border entered Middle English in the 14th c. Watkins registers the detour explicitly under bherdh-: 'Old French borde, hut, and bort, border: BORDELLO, BORDER'. So placing both words in one English box under Germanic *burd- is right, provided one remembers that border came the long way round through Frankish and French.\",\n     \"derivation_fa\": \"board از انگلیسی میانهٔ bord و آن از انگلیسی کهن bord «تخته، میز؛ پهلوی کشتی»، میراثی مستقیم از ژرمنی *burdą. اما border همان واژهٔ ژرمنی است که از راه فرانسه به انگلیسی بازگشته: فرانسهٔ کهن bordure «لبه، حاشیهٔ سپر» از فعل border «لبه‌دار کردن» از اسم bord «لبه»، و این bord خود وام‌واژه‌ای فرانکی (*bord) در گالو-رومی است؛ از این راه border در سدهٔ چهاردهم وارد انگلیسی میانه شد. واتکینز همین دور زدن را زیر bherdh- تصریح می‌کند: «فرانسهٔ کهن borde و bort: BORDELLO, BORDER». پس جای دادن هر دو واژه در یک جعبهٔ انگلیسی زیر ژرمنی *burd- درست است، به شرط آنکه بدانیم border راه دورتری از فرانکی و فرانسوی پیموده است.\",\n     \"sources\": [\"https://www.etymonline.com/word/board\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 335, s.v. bherdh-: 'a. Old English bord, board: BOARD; STARBOARD; … c. Old French borde, hut, and bort, border: BORDELLO, BORDER.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 107 (p.182) s.v. board and leaf 109 (pp.186-187) s.v. border\", \"stance\": \"supports\", \"note\": \"'border, n. — OF. (= F.) bordure, fr. border, \\\"to border\\\", fr. bord, \\\"a border\\\", fr. Frankish *bord.'\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt line 2010, s.v. border\", \"stance\": \"supports\", \"note\": \"'border, an edge. (F.-O. Du.) M.E. bordure … F. bordure … orig. the same word as Du. boord, a board.'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Bher 4\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *bʰerH- / *bʰer- 'bright, brown' (Pokorny 5. bher- 136-137 'glänzend, hellbraun'), with *bʰeru-s/*bʰero-s and the reduplicate *bʰe-bʰru- 'beaver, the brown one'\",\n   \"note\": \"Nourai's 'Bher 4 : bright, brown' with POK:136 lands exactly on Pokorny's '5. bher- \\\"glänzend, hellbraun\\\": bhero-s, bheru-s, vielfach von braunen Tieren; redupl. bhe-bhru-s, bhe-bhro-s \\\"braun; Biber\\\"' on p.136 — the numbering differs only because Nourai counts his own Bher entries. Watkins likewise has 'bher-3. Bright, brown. [Pok. 5. bher- 136.]'. One caveat worth recording: Wiktionary, following Ringe, notes that 'an actual PIE word of [this] shape and meaning is not recoverable' as a simple root — the family is really carried by the derivatives *bʰrūHnos 'brown' and *bʰebʰrus 'beaver'. That does not affect any arrow on this page.\",\n   \"note_fa\": \"«Bher 4: درخشان، قهوه‌ای» با ارجاع POK:136 دقیقاً بر مدخل «bher- ۵» پوکورنی در صفحهٔ ۱۳۶ منطبق است: «درخشان، قهوه‌ایِ روشن: bhero-s، bheru-s، بیشتر دربارهٔ جانوران قهوه‌ای؛ با تکرارِ هجا bhe-bhru-s «قهوه‌ای؛ سگ آبی»». تفاوت شماره فقط از آن روست که نورایی مدخل‌های Bher خود را جداگانه شماره می‌زند. واتکینز نیز «bher-3: درخشان، قهوه‌ای» را با همان ارجاع به پوکورنی ۱۳۶ آورده است. تنها نکتهٔ احتیاطی که باید ثبت شود این است که ویکی‌واژه به پیروی از رینگه یادآور می‌شود که ریشه‌ای سادهٔ هندواروپایی با دقیقاً این شکل و معنا بازسازی‌پذیر نیست و بارِ این خانواده بر دوش مشتق‌های *bʰrūHnos «قهوه‌ای» و *bʰebʰrus «سگ آبی» است. این نکته هیچ‌یک از پیکان‌های این صفحه را خدشه‌دار نمی‌کند؛ ادعای نورایی درست است.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰerH-\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:136\", \"status\": \"supports\", \"note\": \"POK_01.txt line 1916: '5. bher- \\\"glänzend, hellbraun\\\": bhero-s, bheru-s, vielfach von braunen Tieren; redupl. bhe-bhru-s, bhe-bhro-s \\\"braun; Biber\\\"; no-Bildungen: bhre-no-, bhro-no- und (*bheru-s:) bhrou-no-, bhrū-no- \\\"braun\\\"'; the printed numeral 137 appears part-way into the entry, so it opens on p.136.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 335, s.v. bher-3\", \"stance\": \"supports\", \"note\": \"'bher-3. Bright, brown. 1. Suffixed variant form *bhrū-no- in Germanic *brūnaz … 2. Reduplicated form *bhibhru-, *bhebhru-, \\\"the brown animal,\\\" beaver … [Pok. 5. bher- 136.]'\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 94 (printed p.157) s.v. bear, the animal\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. *bhero-, \\\"brown\\\", whence also Lith. bėras, Lett. bę̄rs, \\\"brown\\\", L. fiber, OE. beofor, \\\"beaver\\\", lit. \\\"the brown animal\\\".'\"},\n    {\"src\": \"WLD\", \"where\": \"WP II 166 f., cited by Pokorny at the foot of 5. bher- (p.137)\", \"stance\": \"supports\", \"note\": \"Pokorny closes the entry 'WP. II 166 f., WH. I 490 f., Van Windekens Lexique 93' — the Walde-Pokorny place for this root. Only Band 3 (index) is on disk locally.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"bowra; bawraini, bawri\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The Avestan word for 'beaver' is bawra- m. (Bartholomae AiW col. 925), with the by-form bawray-/bawri- m. 'beaver', f. 'she-beaver' and the adjective bawraini-/bawrinay- 'made of beaver'; all three occur in the one passage Yt. 5.129 about Anāhitā's coat of 'three hundred she-beavers'. The stem continues *bʰebʰru-/*bʰeru- 'the brown one', beside Skt. babhrú- 'reddish-brown', Lat. fiber, OHG bibar. Nourai's second and third forms, bawraini and bawri, are Bartholomae's exactly. His FIRST form, however, is printed 'bowra' — with -o- — which is not a possible Avestan shape and is contradicted within his own box by 'bawraini, bawri'. The printed page (PDF p.90) does read 'bowra', so this is the book's own misprint for bawra-, not a scanning error; the extraction is faithful. The gloss 'red, brown animal, beaver' is right (Bartholomae 'Biber', Pokorny 'av. bawra-, bawri- \\\"Biber\\\"').\",\n     \"derivation_fa\": \"واژهٔ اوستاییِ «سگ آبی» bawra- است (بارتولومه، فرهنگ ایرانی باستان، ستون ۹۲۵)، با گونهٔ bawray-/bawri- مذکر «سگ آبی» و مؤنث «مادهٔ سگ آبی»، و صفتِ bawraini-/bawrinay- «از پوست سگ آبی»؛ هر سه در همان یک بندِ یشت ۵٫۱۲۹ دربارهٔ جامهٔ آناهیتا از پوست «سیصد مادهٔ سگ آبی» آمده‌اند. این ستاک دنبالهٔ *bʰebʰru-/*bʰeru- «قهوه‌ای» است، هم‌ریشه با سنسکریت babhrú-، لاتینی fiber و آلمانی علیای کهن bibar. صورت دوم و سوم که نورایی آورده (bawraini، bawri) عیناً صورت‌های بارتولومه است، اما صورت نخست در کتاب «bowra» چاپ شده که در اوستایی ممکن نیست و با همان دو صورت دیگرِ درونِ همان جعبه هم ناسازگار است. تصویر صفحهٔ ۹۰ نشان می‌دهد که خودِ کتاب «bowra» چاپ کرده است؛ پس خطای چاپیِ کتاب است، نه خطای خوانشِ اسکن. معنایی که داده شده («سرخ، جانور قهوه‌ای، سگ آبی») درست است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"bowra\",\n     \"correct_form\": \"bawra-\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰerH-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:136\", \"status\": \"supports\", \"note\": \"POK_01.txt, 5. bher-, printed p.136-137: 'ai. babhrú-ḥ \\\"rotbraun; große Ichneumonart\\\", av. bawra-, bawri- \\\"Biber\\\"; lat. fiber, fibrī \\\"Biber\\\"' and, on p.137, 'av. bawraini- \\\"vom Biber\\\"'. Pokorny has all three of Nourai's forms — and spells the first bawra-, not bowra.\"},\n      {\"ref\": \"KLN:158\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 94 (printed numeral 157 on the leaf, so pp.157-158), s.v. 'beaver, n., a rodent of the genus Castor': '… and cogn. with L. fiber, OSlav. bebrŭ, Lith. bebrus …, W. befer, Bret. bieuzr, Avestic bawra, \\\"beaver\\\". All these words lit. denote \\\"the brown animal\\\"; they derive fr. I.-E. *bhe-bhru-s, \\\"very brown\\\"'. Klein too writes bawra.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"BRT.txt, column 925 (the running head 'bawra-' is legible in the OCR)\", \"stance\": \"supports\", \"note\": \"'j. bawra- m. \\\"Biber\\\": bawraini vastra … \\\"Biberkleider von dreihundert Bibern\\\" Yt.5.129'; 'j. bawray- m. \\\"Biber\\\", f. \\\"Biberweibchen\\\" … Yt.5.129'; 'j. bawrinay- Adj. \\\"vom Biber stammend\\\" … Ableit. aus bawra-.'\"},\n      {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 5071 (Avestan→Pahlavi index) and line 953\", \"stance\": \"supports\", \"note\": \"'bawra-, bawri-: bavrak' — Nyberg indexes exactly the two Avestan stems Nourai prints (again with -aw-).\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"bŭr «بور»; bŭreh «بوره»\", \"verdict\": \"plausible\",\n     \"derivation\": \"بور bur/bōr 'bay, reddish-brown (of a horse); flushed' is solid: Middle Persian bōr (bwl) 'reddish-brown, bay [horse]', from Proto-Iranian *buHrá-/*bawra-, PIE *bʰerH- 'brown', with Ossetian бур 'yellow', Northern Kurdish bor 'grey', Shughni vūr, Old Armenian boreni 'hyena'. Mo'in's own footnote at Borhān p.314 states it in the same terms: 'روباه، اسب سرخ قهوه‌ای؛ سانسکریت babhru-؛ اوستا bawra اساساً بمعنی سرخ (در تداول عوام بور شدن، یعنی سرخ و خجل شدن)' — which is where Nourai's third gloss, 'flushed from embarrassment', comes from verbatim. The Ferdowsī line quoted on the page ('… بیفشارد یک دست بر پشت بور') is the horse sense. بوره būra 'borax' is the doubtful half. That the word is Persian and is the source of Arabic بورق is beyond dispute (see node 3); but nothing in Mo'in, Asbaghi, Lokotsch or Wiktionary connects بوره to بور 'brown' — the mineral is white, and Nourai has to gloss it 'borax, white' and lean on the 'bright' half of the root to make the link. Treat that arrow as Nourai's own conjecture, not received doctrine; hence plausible for the node.\",\n     \"derivation_fa\": \"«بور» به معنی سرخ‌قهوه‌ای و اسبِ کهر، استوار است: فارسی میانه bōr (نوشتهٔ bwl) «سرخ‌قهوه‌ای، اسب کهر»، از ایرانی باستان *buHrá-/*bawra-، از هندواروپایی *bʰerH- «قهوه‌ای»، هم‌ریشه با آسی бур «زرد»، کردی شمالی bor «خاکستری»، شغنی vūr و ارمنی کهن boreni «کفتار». حاشیهٔ خودِ معین بر برهان قاطع (ص ۳۱۴) همین را می‌گوید: «روباه، اسب سرخ قهوه‌ای؛ سانسکریت babhru-؛ اوستا bawra اساساً بمعنی سرخ (در تداول عوام بور شدن، یعنی سرخ و خجل شدن)» — و معنای سومِ نورایی، «سرخ‌شده از شرم»، لفظ‌به‌لفظ از همین‌جاست. بیت فردوسی که در صفحه نقل شده نیز به معنی «اسبِ بور» است. اما نیمهٔ دوم، یعنی «بوره» (بوراکس)، تردیدآمیز است: فارسی‌بودنِ آن و اینکه سرچشمهٔ «بورق» عربی است بی‌گمان است، ولی نه معین، نه اصبغی، نه لوکوچ و نه ویکی‌واژه «بوره» را به «بور» به معنی قهوه‌ای نبسته‌اند؛ این نمک سفید است و نورایی ناچار شده آن را «بوراکس، سفید» معنی کند و بر نیمهٔ «درخشان»ِ ریشه تکیه کند. پس این پیکان حدسِ خودِ نورایی است نه رأی پذیرفتهٔ عام؛ ارزیابی جعبه «با احتیاط پذیرفتنی» است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/بور\", \"https://en.wiktionary.org/wiki/بورق\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:231\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt leaf 451 = printed p.231 is the ببر entry ('… جانوری باشد صحرایی شبیه بگربه لیکن دم ندارد و از پوست آن پوستین سازند … و بسکون ثانی نام درنده‌ای است مشهور'), i.e. babar 'beaver-like animal' vs babr 'tiger'. A real and relevant page, but it belongs to node #7 (babar), not to bur/būreh.\"},\n      {\"ref\": \"BQT:314\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 534 = printed p.314, Mo'in's footnote 2 on بور: 'روباه، اسب سرخ قهوه‌ای؛ سانسکریت babhru- (سرخ قهوه‌ای) «اسفا ۱:۲ ص ۴۹»؛ اوستا bawra اساساً بمعنی سرخ (در تداول عوام بور شدن، یعنی سرخ و خجل شدن) است که سپس بجانوری که در فارسی ببر (بدو فتح) گویند اطلاق شده …؛ پهلوی … طبری būr (زرد) … دزفولی bōr'.\"},\n      {\"ref\": \"BQT:315\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 535 = printed p.315, headword بوره: 'بروزن شوره. چیزی است مانند نمک و آنرا زرگران بکار برند … و معرب آن بورق است و بعربی بطرون خوانند' — the very page for būreh and its Arabic form, as cited.\"},\n      {\"ref\": \"MON:601\", \"status\": \"not_checked\", \"note\": \"Mo'in's 6-vol Farhang-e Fārsi is not online with its original pagination (refs_online.json: 'Page numbers cannot be mapped online'); the 2-vol Adena abridgement on disk (MON_part1.txt) has no page breaks and its Persian OCR is too corrupt to isolate the بور entry.\"},\n      {\"ref\": \"AEF:295\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asās-e Ešteqāq-e Fārsi (the Persian translation of Horn) is print-only; refs_online.json marks it 'Not online (searched archive.org …)'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"PHD.txt (grep 'bōr', 'bwl')\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary has no bōr headword in the OCR; the MP form is supplied by Wiktionary (bwl /bōr/) and by Mo'in's Borhān footnote.\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt line 982 (Lokotsch no. 356)\", \"stance\": \"supports\", \"note\": \"'[Aus pers. būrāh] \\\"Borax, borsaures Natron\\\"; hieraus … sp. borraj, pg. borax, frz. borax, it. borrace; ndl. engl. borax, dtsch. Borax' — Persian بوره is the ultimate source, but Lokotsch offers no link to بور 'brown'.\"},\n      {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt (searched for بور as a headword)\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary has no بور entry in the scanned pages.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Arabic\", \"words\": \"bŭrq\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic بورق būraq / بَوْرَق bawraq 'borax, natron' is a loan from Middle Persian *bōrag, the ancestor of Persian بوره būra; the Arabic lexica themselves say so. Addī Shīr quotes the Qatr al-Muḥīṭ: 'البورق أصناف: مائي وجبلي وأرضي ومصري وهو النطرون، معرّب بوره' — 'arabicised from [Persian] būra'. Asbaghi's Persische Lehnwörter im Arabischen has the entry 'būraq: \\\"Borax\\\" aus dem pers. bura', and Devic likewise: 'De l'arabe bauraq ou boûraq, venant du persan boûrah'. So the ARROW Persian → Arabic is correct, and Nourai's gloss 'white, shining' reflects the substance's appearance and the Arabic lexicographers' association with barq. THE NOTE on the node reports al-'Unaysī (TAD) as deriving the word from the Arabic root b-r-q 'to shine' — I checked that page and it says exactly that, and even reverses the direction of the loan ('فنقل من العربية إلى اللاتينية … وإلى الفارسية «بوره»'). Modern scholarship (Asbaghi 1988, Lokotsch 356, Devic, Mo'in's Borhān footnote, Wiktionary, Etymonline) is unanimous against al-'Unaysī: the Persian word is the source and the Arabic form is the borrowing, its resemblance to b-r-q being a folk-etymological attraction inside Arabic.\",\n     \"derivation_fa\": \"عربی «بورق/بَوْرَق» به معنی بوراکس و نطرون، وام‌واژه‌ای است از فارسی میانهٔ *bōrag، نیای «بورهٔ» فارسی؛ خودِ فرهنگ‌های عربی هم همین را می‌گویند. اَدّی شیر از قطر المحیط نقل می‌کند: «البورق أصناف: مائي وجبلي وأرضي ومصري وهو النطرون، معرّب بوره». اصبغی در «وام‌واژه‌های فارسی در عربی» مدخل «būraq: بوراکس، از فارسی bura» را دارد و دُویک نیز می‌نویسد «از عربی bauraq که از فارسی boûrah آمده». پس پیکانِ فارسی ← عربی درست است و معنای «سفید، درخشان» که نورایی داده، بازتاب ظاهرِ این نمک و نیز پیوندی است که فرهنگ‌نویسان عرب با ریشهٔ «برق» برقرار کرده‌اند. دربارهٔ یادداشتِ خودِ نمودار: طوبیا العنیسی (TAD) واژه را از ریشهٔ عربی «ب.ر.ق» گرفته و حتی جهت وام‌گیری را وارونه کرده است («فنقل من العربية إلى اللاتينية … وإلى الفارسية «بوره»»)؛ صفحهٔ او را دیدم و دقیقاً همین را می‌گوید. اما پژوهش امروزی یک‌صدا خلافِ اوست: واژه فارسی است و شباهتش به «برق» ریشه‌شناسی عامیانه‌ای است که در درون عربی پدید آمده.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/بورق\", \"https://www.etymonline.com/word/borax\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:315\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 535 = printed p.315, Mo'in's footnote 4: 'درقطرالمحیط آمده: «البورق اصناف: مائی وجبلی و ارضی ومصری وهو النطرون» معرب بوره بالفارسیة. این کلمهٔ معرب وارد لاتینی قرون وسطی و سپس داخل فرانسه شده borax گردیده … فرامرزی، فراسویان و دیگران BORAX را از بورق عربی گرفته‌اند و عرب هم آنرا از بورهٔ فارسی اقتباس کرده است.'\"},\n      {\"ref\": \"TAD:14\", \"status\": \"supports\", \"note\": \"The note is a faithful report of al-'Unaysī. TAD_pages.txt leaf 17 (printed p. ~13-14; the leaf runs بلوان … بوته … بوق … بورق … بوغاز) reads: '… بورق … من برق أي لمع، فنقل من العربية إلى اللاتينية … وإلى الفارسية «بوره» وهو ملح حاصل من الحامض البورقي والنطرون …'. So TAD does say what the chart's NOTE says — and Nourai is right to flag it as a competing view rather than adopt it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AFM\", \"where\": \"AFM.txt line 834 (Addī Shīr, s.v. البورق)\", \"stance\": \"supports\", \"note\": \"'(البورق) أصناف مائي وجبلي وأرمني ومصري وهو النطرون، معرب بوره' — Persian بوره named as the source of the Arabic form.\"},\n      {\"src\": \"PLA\", \"where\": \"incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt lines 3996-3999 and 5322-5324\", \"stance\": \"supports\", \"note\": \"'būraq: \\\"Borax, borsaures Natrium\\\" aus dem pers. بوره bōrah, mp. …; syr. …, mand. burqita, frz. borax, dtsch. Borax'; 'Borax mlat. borax < ar. būrak < pers. būrah'.\"},\n      {\"src\": \"DEV\", \"where\": \"DEV.txt line 848, s.v. Borax\", \"stance\": \"supports\", \"note\": \"'De l'arabe bauraq ou boûraq, venant du persan boûrah, même signification … Gérard de Crémone transcrit baurach.'\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt line 982 (no. 356)\", \"stance\": \"supports\", \"note\": \"'[Aus pers. būrāh] \\\"Borax, borsaures Natron\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"French\", \"words\": \"borax\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The Arabic word travelled west with the Arab pharmacopoeia: Gerard of Cremona (12th c., Toledo) transcribes it baurach, whence Medieval Latin baurach/borax and Old French/French borax, with the Iberian and Italian doublets Spanish borraj/borrax and Italian borrace. Pihan's Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, p.71, gives the entry as 'BORAX, s. m. (a.-p.) بورق [baurak] nitre, en persan بوره [boûrah]' — the label '(a.-p.)' meaning 'Arabic, from Persian', exactly the route Nourai draws. Devic adds that the word entered the European languages from the Arabs about the 9th century.\",\n     \"derivation_fa\": \"این واژه همراه با داروشناسی عربی به مغرب‌زمین رفت: ژِرار کرمونایی (سدهٔ دوازدهم، تولدو) آن را baurach آوانویسی کرد و از آنجا به لاتینیِ سده‌های میانه (baurach/borax) و سپس به فرانسوی borax رسید، با گونه‌های اسپانیایی borraj/borrax و ایتالیایی borrace. پیئان در «فرهنگ ریشه‌شناختی واژه‌های فرانسوی برگرفته از عربی، فارسی و ترکی»، صفحهٔ ۷۱، مدخل را چنین می‌آورد: «BORAX (ع.-ف.) بورق [baurak]، نطرون، در فارسی بوره [boûrah]» — و نشانهٔ «(a.-p.)» یعنی «عربی، از فارسی»، درست همان مسیری که نورایی رسم کرده است. دُویک می‌افزاید که این واژه در حدود سدهٔ نهم میلادی از عرب‌ها به زبان‌های اروپایی راه یافت. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/borax\"],\n     \"ref_check\": [\n      {\"ref\": \"PHN:71\", \"status\": \"supports\", \"note\": \"PHN.txt leaf 102, whose running head reads 'BOS 71': 'BORAX, s. m. (a.-p.) بورق [baurak] nitre, en persan بوره [boûrah]. — Borax est le nom donné vulgairement au sous-borate de soude … Les Espagnols écrivent borrax, et les Italiens borace. Le borax brut s'appelle aussi tinkal.' Page and content match Nourai's citation exactly.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"DEV\", \"where\": \"DEV.txt line 848\", \"stance\": \"supports\", \"note\": \"'Borax. Esp. borrax, borraj; ital. borrace. De l'arabe bauraq … Il n'est pas inutile de remarquer que le borax nous vient surtout des pays asiatiques; Leman dit que ce mot, emprunté aux Arabes, s'est introduit dans les langues européennes vers le ixe siècle.'\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt line 982 (no. 356)\", \"stance\": \"supports\", \"note\": \"'… hieraus mit gleicher Bedeutung sp. borraj, pg. borax, frz. borax, it. borrace; ndl. engl. borax, dtsch. Borax; russ. bulg. bura, serb. poln. boraks, čech. borax.'\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"borax, boric, Boron\", \"verdict\": \"confirmed\",\n     \"derivation\": \"borax is attested in English from the late 14th century, taken from Anglo-French boras (Anglo-Norman boreis) < Medieval Latin baurach < Arabic būraq; Middle English boras was later re-latinised to borax. The adjective boric (and the older boracic) is formed on the same stem; Boron is Humphry Davy's coinage of 1812 — he first called the element boracium because he obtained it from boracic acid, then cut it to boron on the model of carbon. So the whole English box is a straight continuation of the French/Latin form, and the capital B on 'Boron' is simply Nourai marking a chemical element.\",\n     \"derivation_fa\": \"واژهٔ borax از اواخر سدهٔ چهاردهم در انگلیسی گواهی شده، از انگلوفرانسویِ boras (انگلونورمنِ boreis) از لاتینیِ سده‌های میانه baurach از عربی būraq؛ صورت انگلیسی میانهٔ boras بعدها دوباره به شکل لاتینیِ borax درآمد. صفت boric (و صورت کهن‌ترِ boracic) بر همین ستاک ساخته شده است، و Boron نام‌گذاری هامفری دِیوی در ۱۸۱۲ است: نخست آن را boracium نامید چون از «اسید بوریک» به دستش آمده بود، سپس به قیاسِ carbon آن را boron کوتاه کرد. پس این جعبهٔ انگلیسی ادامهٔ مستقیم صورت فرانسوی/لاتینی است و حرف بزرگ در Boron صرفاً نشانهٔ عنصر شیمیایی است؛ ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/borax\", \"https://en.wiktionary.org/wiki/بورق\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:152\", \"status\": \"not_checked\", \"note\": \"Nourai's AHD page numbers are to the 1975/76 New College Edition main dictionary (p.152 would be the 'borax' headword), which is not open online — the IA scans of the 1970s AHD are lending-only (refs_online.json). The local AHD_watkins1985.txt is only the Indo-European appendix and has no borax entry, borax not being an inherited word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 109 (printed pp.186-187), s.v. borax\", \"stance\": \"supports\", \"note\": \"'borax, n., a white crystalline salt used as a flux and an antiseptic. — F., fr. Arab. bauraq (VArab. bōraq), fr. Pers. burah.'\"},\n      {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (Webster's New Twentieth Century)\", \"stance\": \"silent\", \"note\": \"Not consulted usefully — the OCR of the b- volume did not yield a clean borax entry; Etymonline and Klein cover the chain.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Pahlavi\", \"words\": \"bavarak\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian bavrak / babrag, written bplk', 'the beaver' — Nyberg's glossary to his Manual of Pahlavi gives it as 'bavrak [bplk'] the beaver 82.19. — Av. (925) bawra-, bawri-', i.e. he refers it to precisely the Avestan stems in node #1 and to Bartholomae's column 925. MacKenzie reads the same spelling babrag and keeps it apart from babr [bpl] 'tiger'. The form is the Old Iranian reduplicated *babra-ka- (PIE *bʰe-bʰru-, cf. Skt. babhrú-, Lat. fiber, OHG bibar) with the common MP diminutive/appurtenance suffix -ak. Nourai's 'bavarak' is Nyberg's transcription with an anaptyctic vowel written out; drawing it straight from the root box rather than from the Avestan node is correct, since a reduplicated *babra- is a sister of bawra-, not its descendant.\",\n     \"derivation_fa\": \"فارسی میانهٔ bavrak/babrag، به نگارش bplk'، «سگ آبی». نیبرگ در واژه‌نامهٔ «راهنمای پهلوی» می‌آورد: «bavrak [bplk'] سگ آبی ۸۲٫۱۹ — اوستایی (۹۲۵) bawra-, bawri-»، یعنی آن را دقیقاً به همان ستاک‌های اوستاییِ جعبهٔ پیشین و به ستون ۹۲۵ بارتولومه بازمی‌گرداند. مکنزی همین نگارش را babrag می‌خواند و آن را از babr [bpl] «ببر (درنده)» جدا نگاه می‌دارد. صورت اصلی، *babra-ka- ایرانی باستان با تکرار هجای آغازین است (هندواروپایی *bʰe-bʰru-، هم‌ریشه با سنسکریت babhrú-، لاتینی fiber و آلمانی علیای کهن bibar) به‌علاوهٔ پسوندِ رایج فارسی میانه -ak. «bavarak»ِ نورایی همان آوانویسی نیبرگ است با واکهٔ میانجیِ نوشته‌شده؛ و کشیدن پیکان آن از خودِ ریشه (نه از جعبهٔ اوستایی) درست است، چون صورت مکرّرِ *babra- خواهرِ bawra- است نه فرزندِ آن.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/ببر\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:471\", \"status\": \"not_checked\", \"note\": \"Mo'in's 6-vol Farhang-e Fārsi cannot be paged online (refs_online.json), and the Persian OCR of the 2-vol Adena abridgement on disk is too corrupt to isolate the ببر entry; the claim was instead verified against Nyberg and MacKenzie, which support it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 953 (Glossary) and line 5071 (Avestan index)\", \"stance\": \"supports\", \"note\": \"'bavrak [bplk'] the beaver 82.19. — Av. (925) bawra-, bawri-.' and, in the Avestan-to-Pahlavi index, 'bawra-, bawri-: bavrak'. This is Nourai's form and gloss verbatim.\"},\n      {\"src\": \"PHD\", \"where\": \"PHD.txt lines 230-231 (MacKenzie p.16)\", \"stance\": \"partial\", \"note\": \"'babr [bpl | N ~] tiger. babrag [bplk'] beaver.' — the same word, but MacKenzie normalises the reading to babrag rather than bavrak.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Persian\", \"words\": \"babar «بَبَر»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian ببر with the two fatḥas, babar, is the (now archaic) word for the beaver, the regular reflex of MP babrag with loss of the suffix -ag; it is kept apart from ببر babr 'tiger', which continues MP babr [bpl] and is itself suspected of being a Semitic/Akkadian culture-word. Borhān-e Qāṭe' p.231 describes the babar exactly as a beaver-like fur animal — 'جانوری باشد صحرایی شبیه بگربه لیکن دم ندارد و از پوست آن پوستین سازند' — and adds 'و بسکون ثانی نام درنده‌ای است مشهور', i.e. with sukūn (babr) it is the well-known predator. Mo'in's footnote at p.314 makes the etymological connection Nourai draws: Av. bawra 'basically means red … and was then applied to the animal which in Persian is called ببر (with two fatḥas)'. Nourai's second gloss, 'red fox', is Mo'in's 'روباه' from that same footnote.\",\n     \"derivation_fa\": \"«بَبَر» با دو فتحه، واژهٔ (اکنون کهنهٔ) فارسی برای سگ آبی است و بازتاب منظمِ فارسی میانهٔ babrag با افتادنِ پسوند -ag؛ باید آن را از «ببر» (babr) به معنی درندهٔ مشهور جدا داشت که دنبالهٔ فارسی میانهٔ babr [bpl] است و خود گمان می‌رود واژه‌ای فرهنگی با خاستگاه سامی/اکدی باشد. برهان قاطع در صفحهٔ ۲۳۱ «ببر» را چنین وصف می‌کند: «جانوری باشد صحرایی شبیه بگربه لیکن دم ندارد و از پوست آن پوستین سازند»، و می‌افزاید «و بسکون ثانی نام درنده‌ای است مشهور». حاشیهٔ معین در صفحهٔ ۳۱۴ نیز همان پیوندی را برقرار می‌کند که نورایی رسم کرده است: «اوستا bawra اساساً بمعنی سرخ است … که سپس بجانوری که در فارسی ببر (بدو فتح) گویند اطلاق شده». معنای دومِ نورایی، «روباه سرخ»، همان «روباه»ِ آغازِ همین حاشیه است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/ببر\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:471\", \"status\": \"not_checked\", \"note\": \"Same limitation as node #6: Mo'in's 6-vol edition is not pageable online and the Adena abridgement's OCR is unusable for this headword. The substance of the claim was checked in Borhān (which Mo'in edited) at pp.231 and 314, and in Wiktionary, both of which support it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt leaf 451 = printed p.231 (headword ببر) and leaf 534 = printed p.314 (Mo'in's footnote 2)\", \"stance\": \"supports\", \"note\": \"p.231: '… جانوری باشد صحرایی شبیه بگربه لیکن دم ندارد و از پوست آن پوستین سازند … و بسکون ثانی نام درنده‌ای است مشهور'; p.314 n.2: 'اوستا bawra اساساً بمعنی سرخ … است که سپس بجانوری که در فارسی ببر (بدو فتح) گویند اطلاق شده'.\"},\n      {\"src\": \"PHD\", \"where\": \"PHD.txt lines 230-231\", \"stance\": \"supports\", \"note\": \"'babr [bpl | N ~] tiger. babrag [bplk'] beaver.' — the Middle Persian pair behind the two Persian homographs.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Germanic\", \"words\": \"brŭnaz; bero\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Two Germanic derivatives of the 'brown' root. (1) *brūnaz 'brown, shining' (< *bʰruH-no-) > OE brūn, ON brúnn, OHG/MHG brūn, MDu. bruun, G. braun; Old French borrowed it as brun, whence brunet, burnish. (2) *berô, weak stem *beran-, 'the brown one' = 'bear' > OE bera, OHG bero, MHG ber, G. Bär; the ON o-form bjǫrn is *bernuz. Both are set out this way by Pokorny p.136 ('ahd. bero, ags. bera \\\"Bär\\\" (*bheron-); aisl. bjǫrn ds. (*bhernu-)' and 'ahd. mhd. brūn \\\"glänzend, braun\\\"') and by Watkins. The gloss Nourai attaches to bero, 'brown animal, bear, beaver', conflates two words: *berô is the bear, while the beaver is Germanic *bebruz (OE beofor, OHG bibar) — the reduplicated stem. Pokorny and Klein both list them side by side under the one root, so the box is right, but the beaver belongs to *bebruz, not to *berô.\",\n     \"derivation_fa\": \"دو مشتقِ ژرمنیِ ریشهٔ «قهوه‌ای». ۱) *brūnaz «قهوه‌ای، درخشان» (از *bʰruH-no-) که به انگلیسی کهن brūn، نورس کهن brúnn، آلمانی علیای کهن brūn و آلمانی امروز braun رسیده؛ فرانسهٔ کهن آن را به‌صورت brun وام گرفت و از آن brunet و burnish پدید آمد. ۲) *berô، ستاک ضعیف *beran-، «آن قهوه‌ای» یعنی «خرس» که به انگلیسی کهن bera، آلمانی علیای کهن bero و آلمانی Bär رسیده است؛ صورت نورس کهن bjǫrn از *bernuz است. پوکورنی در صفحهٔ ۱۳۶ و واتکینز هر دو همین را می‌آورند. اما معنایی که نورایی به bero داده («جانور قهوه‌ای، خرس، سگ آبی») دو واژه را در هم آمیخته است: *berô خرس است و سگ آبی در ژرمنی *bebruz (انگلیسی کهن beofor، آلمانی علیای کهن bibar) یعنی همان ستاکِ مکرّر. چون پوکورنی و کلاین هر دو این‌ها را کنارِ هم زیر یک ریشه می‌آورند، جعبه در کل درست است، اما سگ آبی به *bebruz تعلق دارد نه به *berô.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰerH-\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:158\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 94 (printed 157, so pp.157-158): 'bear, n., the animal. — ME. bere, fr. OE. bera, rel. to MDu. bere, Du. beer, OHG. bero, MHG. ber, G. Bär, ON. bjǫrn, lit. \\\"the brown animal\\\", fr. I.-E. *bhero-, \\\"brown\\\" …' and, on the same leaf, 'beaver … fr. I.-E. *bhe-bhru-s, \\\"very brown\\\"'.\"},\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 335, s.v. bher-3: '1. Suffixed variant form *bhrū-no- in Germanic *brūnaz … 3. Germanic *berô, \\\"the brown animal,\\\" bear, in Old English bera, bear: BEAR.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"POK_01.txt, 5. bher-, printed pp.136-137\", \"stance\": \"supports\", \"note\": \"'ahd. bero, ags. bera \\\"Bär\\\" (*bheron-); aisl. bjǫrn ds. (*bhernu-)'; 'ahd. mhd. brūn \\\"glänzend, braun\\\", ags. brūn, aisl. brúnn ds.'; 'ahd. bibar, ags. beofor (ältest bebr) … (urg. *bebru-)'.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 118 (printed pp.203-204), s.v. brown\", \"stance\": \"supports\", \"note\": \"'brown, adj. — ME. broun, fr. OE. brūn … enlarged — with -n-formative element — from I.-E. base *bher-, \\\"shining, brown\\\", whence also Lith. bėras … OE. bera, \\\"bear\\\" …, OE. be(o)for, \\\"beaver\\\".'\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"brown, brunet, beaver, bear 2, Bernard\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All five are standard members of the family. brown < OE brūn < Gmc *brūnaz. brunet(te) is the French diminutive of brun, itself Germanic *brūnaz borrowed into Old French — so an inherited word re-imported. beaver < OE be(o)for < Gmc *bebruz, the reduplicated *bʰe-bʰru- ('bear 2' is Nourai's numbering to distinguish the animal from bear 'to carry'). bear (the animal) < OE bera < Gmc *berô 'the brown one'. Bernard is the Germanic personal name Bern-hard 'bear-strong', its first element the same *bern-/*ber- stem — Klein ends his bear entry with 'Cp. also the first element in Bernard'. Watkins routes the same five words through bher-3 (BROWN, BRUIN, BRUNET, BURNISH, BEAVER, BEAR, BERSERKER).\",\n     \"derivation_fa\": \"هر پنج واژه اعضای متعارف این خانواده‌اند. brown از انگلیسی کهن brūn از ژرمنی *brūnaz. brunet(te) صورت مصغّرِ فرانسویِ brun است و brun خود همان *brūnaz ژرمنی است که به فرانسهٔ کهن وام رفته بود؛ پس واژه‌ای است که پس از وام‌رفتن دوباره وام گرفته شده (نوعی دوگانه). beaver از انگلیسی کهن be(o)for از ژرمنی *bebruz، بازتاب صورت مکرّرِ *bʰe-bʰru-. «bear 2» شماره‌گذاری خودِ نورایی برای جدا کردنِ «خرس» از bear «بردن» است و از انگلیسی کهن bera از ژرمنی *berô «آن قهوه‌ای» می‌آید. Bernard نام خاصِ ژرمنیِ Bern-hard «خرس‌نیرو» است که جزء نخستش همان ستاکِ *bern-/*ber- است؛ کلاین مدخل bear را با جملهٔ «نیز بنگرید به جزء نخستِ Bernard» به پایان می‌برد. واتکینز نیز همین پنج واژه را زیر bher-3 می‌آورد. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰerH-\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed on this node; the parent's KLN:158 and AHD citations cover all five words.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 94 (pp.157-158) and leaf 118 (pp.203-204)\", \"stance\": \"supports\", \"note\": \"s.v. bear: '… lit. \\\"the brown animal\\\" … Cp. beaver, the animal, and brown. Cp. also the first element in Bernard.'; s.v. brown: '… cp. bruin, brunette, brunissure, Bruno, burnet, burnish, Prunella.'\"},\n      {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 335, s.v. bher-3\", \"stance\": \"supports\", \"note\": \"'a. Old English brūn, brown: BROWN; b. Middle Dutch bruun …: BRUIN; c. Old French brun, shining, brown: BRUNET, BURNET, BURNISH. 2. … Old English be(o)for, beaver: BEAVER. 3. … Old English bera, bear: BEAR. 4. Germanic *bernuz in Old Norse bjǫrn …: BERSERKER.'\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-90.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk90.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-90.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 90",
 "description": "Write and validate page-90.json"
}
```


### [2026-09-05T14:04:36.390Z] TOOL RESULT

```
written
JSON OK
nodes verified: 19/19
node verdicts: {'confirmed': 15, 'disputed': 1, 'plausible': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 18, 'not_checked': 9, 'partial': 2}
books consulted: {'supports': 39, 'silent': 4, 'partial': 3} | by book: {'KLN': 9, 'POK': 6, 'PHD': 5, 'CHEUNG': 3, 'NYB': 3, 'AHD': 3, 'LKT': 3, 'BRT': 2, 'SYN': 2, 'ARY': 2, 'DEV': 2, 'LAT': 1, 'SKT': 1, 'AFM': 1, 'PLA': 1, 'WEB': 1, 'BQT': 1}
```


## [2026-09-05T14:04:42.746Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | grep -i \"90\\|missing\\|not archived\" | head -20; echo \"exit=$?\"",
 "description": "Check archived sources for page 90"
}
```


### [2026-09-05T14:04:48.867Z] TOOL RESULT

```
exit=0
```


## [2026-09-05T14:04:50.956Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -20",
 "description": "Full archive check output"
}
```


### [2026-09-05T14:04:55.352Z] TOOL RESULT

```
768 cited URLs, 22 not yet archived
archived 22, failed 0
```


## [2026-09-05T14:05:13.985Z] AGENT

Page 90 verified. `verify_check.py 90` reports 19/19 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed. Nodes: 15 confirmed, 2 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 18 supports, 2 partial, 9 not_checked (MON pages can't be mapped online; AEF and the 1976 AHD print aren't accessible). 46 `consulted` entries across 17 books.

**Flagged items**
- **disputed** — entry 0 #3 (Persian), word **bîl «بیل»**: Nourai follows Horn no. 237 (de Lagarde) tying bēl to Av. √bray- "cut". Modern work derives MP bēl from PI *badra-/*badHr̥ < PIE *bʰedʰh₂- "to dig" (Lat. *fodiō*, Bal. *bard*) — a different root. The other two words in the box (borîdan, bor) are confirmed by Cheung, Buck and Pokorny 133 itself ("npers. burrad").
- **transcription_suspect** — entry 1 #1 (Avestan) **"bowra"**: `error_in: book`. Pokorny 136, Bartholomae col. 925, Klein 157 and Nyberg all write **bawra-**, and Nourai's own box has "bawraini, bawri". The printed page (PDF p.90, copied to `data/verification/sources/refs/ocr/BOOK/90.png`) does read "bowra" — the author's misprint, extraction is faithful.
- **plausible** — entry 1 #2: بور *bur* fully confirmed (Mo'in's Borhān footnote p.314 is the verbatim source of Nourai's "flushed from embarrassment"), but the link of بوره *būreh* "borax" to the "bright/brown" root is Nourai's own conjecture — no source connects them.
- **plausible** — entry 0 #7: perforate/interfere/friction are exact, but **debris** comes from Late Latin *brisāre* (Gaulish), not from forāre/ferīre/fricāre; it is still inside the root box (Pokorny 166).

**Notable positive findings**: SNS:105 located precisely (leaf 68, dated by the book's own index) and it does gloss the Pahlavi verb with Av. √brāy-; KLN:182 is verbatim Nourai's "bherd : to cut"; PHN:71 and BQT:315 confirm the Persian بوره → Arabic بورق → Latin/French borax chain, corroborated by Addī Shīr, Asbaghi, Lokotsch and Devic. The chart's own NOTE (TAD:14 deriving būraq from Arabic b-r-q) was checked on the page and reported faithfully — but modern scholarship is unanimous against it, and Nourai was right to flag rather than adopt it. Nyberg's glossary confirms Pahlavi *bavrak* [bplk'] "beaver ← Av. bawra-, bawri-", vindicating Nourai's otherwise odd-looking "bavarak".

**No extraction errors found** — the JSON matches the printed page throughout.
