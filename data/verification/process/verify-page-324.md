# Verification process log — verify-page-324


## [2026-09-07T15:49:24.372Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 324 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-324.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-324.json. Write /home/sfmqrb/git/rishe/data/verification/page-324.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 324` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T15:49:26.347Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T15:49:26.980Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T15:49:26.996Z] TOOL RESULT

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


## [2026-09-07T15:49:27.474Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-324.txt"
}
```


### [2026-09-07T15:49:27.494Z] TOOL RESULT

```
1	=== PDF page 324 (book page 294) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Me 2 : to measure; Měnôt: moon used to measure time  (refs POK:703, 731)  PART 2
4	#1 (parent #0) [Indo-European] refs=POK:705 | Med : to take appropriate measures, to cure
5	  #2 (parent #1) [Avestan] refs=POK:705; SYN:307 | vi-mad : care giver, physician ☞Wi
6	    #3 (parent #2) [Pahlavi] refs=None | vîmâr : patient
7	      #4 (parent #3) [Persian] refs=BQT:340; HRN:59 | bîmâr «بیمار» : patient
8	  #5 (parent #1) [Avestan / Old Persian] refs=POK:705 | azdâ : indicator, hint, news
9	    #6 (parent #5) [None] refs=None | 
10	  #7 (parent #1) [Latin] refs=AHD | 
11	    #8 (parent #7) [English] refs=None | medicine, remedy, moderate
12	  #9 (parent #1) [Latin] refs=AHD | modus : size
13	    #10 (parent #9) [French] refs=None | 
14	      #11 (parent #10) [Persian] refs=MON |  | extra: مدل ، مدرن ، کمد
15	    #12 (parent #9) [English] refs=None | mode, model, modern, modest, module, turmoil, mold, mood, commode
16	  #13 (parent #1) [Germanic] refs=None | 
17	    #14 (parent #13) [English] refs=None | must 1 : have to ; empty
18	--- entry 1 ---
19	ROOT Med -> redirect to Me 2
20	--- entry 2 ---
21	ROOT [Indo-European] Medhu : honey  (refs POK:707)
22	#1 (parent #0) [Avestan] refs=POK:707 | madhu : honey ; madha : wine
23	  #2 (parent #1) [Persian] refs=BQT:2071; HRN:225 ;SYN:389 | may «می» : wine ; mol «مُل» : wine | NOTE: For another possible root of "mol" see Mer 2
24	#3 (parent #0) [Sogdian] refs=SOD:220 | mwd : wine
25	#4 (parent #0) [Greek] refs=AHD:1524 | methu : wine
26	  #5 (parent #4) [French] refs=AHD:826 | 
27	    #6 (parent #5) [English] refs=None | methylene
28	
```


## [2026-09-07T15:49:31.652Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-324.json",
 "description": "Read source JSON page 324"
}
```


### [2026-09-07T15:49:31.688Z] TOOL RESULT

```
{
  "pdf_page": 324,
  "book_page": 294,
  "entries": [
    {
      "root": {
        "name": "Me 2",
        "lang": "Indo-European",
        "refs": "POK:703, 731",
        "gloss": "to measure; Měnôt: moon used to measure time"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:705",
          "words": [
            {"translit": "Med", "gloss": "to take appropriate measures, to cure", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:705; SYN:307",
          "words": [
            {"translit": "vi-mad", "gloss": "care giver, physician", "script": null, "see": ["Wi"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "vîmâr", "gloss": "patient", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:340; HRN:59",
          "words": [
            {"translit": "bîmâr", "gloss": "patient", "script": "بیمار"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Avestan / Old Persian",
          "refs": "POK:705",
          "words": [
            {"translit": "azdâ", "gloss": "indicator, hint, news", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": null,
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "medicine, remedy, moderate", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "modus", "gloss": "size", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON",
          "words": [],
          "script_extra": "مدل ، مدرن ، کمد",
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "mode, model, modern, modest, module, turmoil, mold, mood, commode", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 1,
          "lang": "Germanic",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "must 1", "gloss": "have to", "script": null},
            {"translit": "empty", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Med", "redirect": "Me 2"},
      "nodes": []
    },
    {
      "root": {
        "name": "Medhu",
        "lang": "Indo-European",
        "refs": "POK:707",
        "gloss": "honey"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:707",
          "words": [
            {"translit": "madhu", "gloss": "honey", "script": null},
            {"translit": "madha", "gloss": "wine", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2071; HRN:225 ;SYN:389",
          "words": [
            {"translit": "may", "gloss": "wine", "script": "می"},
            {"translit": "mol", "gloss": "wine", "script": "مُل"}
          ],
          "note": "For another possible root of \"mol\" see Mer 2",
          "quote": {
            "text": "به زرّینه جام اندرون لعل مل - فروزنده چون لاله بر زرد گل",
            "poet": "Onsorî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:220",
          "words": [
            {"translit": "mwd", "gloss": "wine", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1524",
          "words": [
            {"translit": "methu", "gloss": "wine", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "AHD:826",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "methylene", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T15:49:31.758Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T15:49:31.797Z] TOOL RESULT

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


## [2026-09-07T15:49:38.506Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','HRN','BQT','SOD','AHD','MON','PHD','BRT','WLD','KLN','IEC','LEW','LAT','NYB','HUB','ARY','CHEUNG']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:900])\n\""
}
```


## [2026-09-07T15:49:39.261Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && python3 -m json.tool data/verification/page-312.json | head -80"
}
```


### [2026-09-07T15:49:39.850Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.", "notes": ""}
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
== CHEUNG null
```


### [2026-09-07T15:49:41.250Z] TOOL RESULT

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
{
    "pdf_page": 312,
    "book_page": 282,
    "verified_by": "claude-opus-5",
    "verified_on": "2026-09-06",
    "entries": [
        {
            "entry": 2,
            "root": "Leuk, Leuqos",
            "verdict": "confirmed",
            "modern_form": "PIE *leuk- (Pokorny leuk\u0302-) 'light, brightness; to shine, to see', with the thematic *leuk-o-s (Gk. leuk\u00f3s) that Nourai calls 'Leuqos'",
            "note": "Root, language label, gloss and page reference are all right. Pokorny, IEW 687-690, lemma leuk\u0302- (leuk-), Meaning 'bright, to shine; to see' (References: WP. II 408 ff.), listing exactly the material of this chart: Av. raocah-, OP raucah-, Av. raox\u0161na-, Lat. l\u016bx/l\u016bmen/l\u016bna/l\u016bstrum/l\u016bstr\u0101re, Goth. liuha\u00fe / OHG lioht / OE l\u0113oht, Skt. loka-. Watkins/AHD: \"leuk-. Light, brightness. ... [Pok. leuk- 687.]\" \u2014 so POK:687 is the exact page. Kent (KNT:205), Nourai's second reference, gives the same root in the older notation pIE *leugos s.v. raucah-. 'Leuqos' is Nourai's spelling of the *leuk-o-s form (Gk. leuk\u00f3s 'white, bright', Skt. loka- 'open bright space, world', Lat. l\u016bcus 'grove'); it is not a separate root. Cross-cutting remarks: (1) the chart's strongest link, Persian r\u016bz/r\u014d\u0161an/afr\u016bxtan and the Arabic loan rizq, is fully confirmed; (2) two Persian items in the Persian box (\u0622\u0631\u0634, \u062f\u0631\u0641\u0634 \u06f1) and one Avestan item (a-rax\u0161a, plus the unattested rao\u010d-x\u0161aema) are not supported by modern sources; (3) the Sogdian box mixes an inherited word (rwx\u0161n) with a Sanskrit loanword (\u03b4wk' < Skt. loka); (4) the Germanic box misprints the reconstruction (liuhtam for *leuhtam); (5) on the printed page the Old Persian box has an arrow into an empty, unlabelled box that the JSON does not record.",
            "note_fa": "\u0631\u06cc\u0634\u0647\u060c \u0628\u0631\u0686\u0633\u0628\u0650 \u0632\u0628\u0627\u0646\u060c \u0645\u0639\u0646\u06cc \u0648 \u0634\u0645\u0627\u0631\u0647\u0654 \u0635\u0641\u062d\u0647 \u0647\u0631 \u0686\u0647\u0627\u0631 \u062f\u0631\u0633\u062a \u0627\u0633\u062a: \u067e\u0648\u06a9\u0648\u0631\u0646\u06cc \u062f\u0631 \u00ab\u0641\u0631\u0647\u0646\u06af \u0631\u06cc\u0634\u0647\u200c\u0634\u0646\u0627\u0633\u06cc\u0650 \u0647\u0646\u062f\u0648\u0627\u0631\u0648\u067e\u0627\u06cc\u06cc\u00bb \u0635\u0641\u062d\u0647\u200c\u0647\u0627\u06cc \u06f6\u06f8\u06f7 \u062a\u0627 \u06f6\u06f9\u06f0 \u0631\u06cc\u0634\u0647\u0654 leuk\u0302- \u0631\u0627 \u0628\u0627 \u0645\u0639\u0646\u0627\u06cc \u00ab\u0631\u0648\u0634\u0646\u060c \u062f\u0631\u062e\u0634\u06cc\u062f\u0646\u061b \u062f\u06cc\u062f\u0646\u00bb \u0645\u06cc\u200c\u0622\u0648\u0631\u062f \u0648 \u0647\u0645\u0627\u0646 \u062f\u0627\u062f\u0647\u200c\u0647\u0627\u06cc \u0627\u06cc\u0646 \u0646\u0645\u0648\u062f\u0627\u0631 \u0631\u0627 \u0628\u0631\u0645\u06cc\u200c\u0634\u0645\u0627\u0631\u062f: \u0627\u0648\u0633\u062a\u0627\u06cc\u06cc raocah- \u0648 raox\u0161na-\u060c \u067e\u0627\u0631\u0633\u06cc \u0628\u0627\u0633\u062a\u0627\u0646 raucah-\u060c \u0644\u0627\u062a\u06cc\u0646 l\u016bx \u0648 l\u016bmen \u0648 l\u016bna \u0648 l\u016bstrum\u060c \u06af\u0648\u062a\u06cc\u06a9 liuha\u00fe \u0648 \u0627\u0646\u06af\u0644\u06cc\u0633\u06cc \u06a9\u0647\u0646 l\u0113oht\u060c \u0648 \u0633\u0646\u0633\u06a9\u0631\u06cc\u062a loka-. \u0648\u0627\u062a\u06a9\u06cc\u0646\u0632 \u0646\u06cc\u0632 \u0630\u06cc\u0644 leuk- \u0647\u0645\u06cc\u0646 \u0627\u0631\u062c\u0627\u0639 \u00ab\u067e\u0648\u06a9\u0648\u0631\u0646\u06cc \u06f6\u06f8\u06f7\u00bb \u0631\u0627 \u062f\u0627\u0631\u062f. \u00abLeuqos\u00bb \u0635\u0648\u0631\u062a\u0650 \u0633\u062a\u0627\u06a9\u200c\u062f\u0627\u0631\u0650 *leuk-o-s \u0627\u0633\u062a (\u06cc\u0648\u0646\u0627\u0646\u06cc leuk\u00f3s\u060c \u0633\u0646\u0633\u06a9\u0631\u06cc\u062a loka-\u060c \u0644\u0627\u062a\u06cc\u0646 l\u016bcus) \u0648 \u0631\u06cc\u0634\u0647\u0654 \u062c\u062f\u0627\u06af\u0627\u0646\u0647\u200c\u0627\u06cc \u0646\u06cc\u0633\u062a. \u0628\u0647\u200c\u0637\u0648\u0631 \u06a9\u0644\u06cc: \u067e\u06cc\u0648\u0646\u062f\u0650 \u0641\u0627\u0631\u0633\u06cc \u00ab\u0631\u0648\u0632\u060c \u0631\u0648\u0634\u0646\u060c \u0627\u0641\u0631\u0648\u062e\u062a\u0646\u00bb \u0648 \u0648\u0627\u0645\u200c\u0648\u0627\u0698\u0647\u0654 \u0639\u0631\u0628\u06cc\u0650 \u00ab\u0631\u0632\u0642\u00bb \u06a9\u0627\u0645\u0644\u0627\u064b \u062a\u0623\u06cc\u06cc\u062f \u0645\u06cc\u200c\u0634\u0648\u062f\u061b \u0627\u0645\u0627 \u00ab\u0622\u0631\u0634\u00bb \u0648 \u00ab\u062f\u0631\u0641\u0634 \u06f1\u00bb \u062f\u0631 \u062c\u0639\u0628\u0647\u0654 \u0641\u0627\u0631\u0633\u06cc \u0648 \u00aba-rax\u0161a\u00bb \u0648 \u00abrao\u010d-x\u0161aema\u00bb \u062f\u0631 \u062c\u0639\u0628\u0647\u0654 \u0627\u0648\u0633\u062a\u0627\u06cc\u06cc \u067e\u0634\u062a\u0648\u0627\u0646\u0647\u0654 \u0627\u0645\u0631\u0648\u0632\u06cc \u0646\u062f\u0627\u0631\u0646\u062f\u061b \u062c\u0639\u0628\u0647\u0654 \u0633\u063a\u062f\u06cc \u06cc\u06a9 \u0648\u0627\u0698\u0647\u0654 \u0645\u06cc\u0631\u0627\u062b\u06cc (rwx\u0161n) \u0631\u0627 \u0628\u0627 \u06cc\u06a9 \u0648\u0627\u0645\u200c\u0648\u0627\u0698\u0647\u0654 \u0633\u0627\u0646\u0633\u06a9\u0631\u06cc\u062a (\u03b4wk' \u0627\u0632 loka) \u062f\u0631\u0622\u0645\u06cc\u062e\u062a\u0647\u061b \u0648 \u062f\u0631 \u062c\u0639\u0628\u0647\u0654 \u0698\u0631\u0645\u0646\u06cc \u0635\u0648\u0631\u062a\u0650 \u0628\u0627\u0632\u0633\u0627\u0632\u06cc\u200c\u0634\u062f\u0647 \u063a\u0644\u0637 \u0686\u0627\u067e \u0634\u062f\u0647 \u0627\u0633\u062a (liuhtam \u0628\u0647\u200c\u062c\u0627\u06cc *leuhtam).",
            "sources": [
                "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewk-",
                "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B2"
            ],
            "ref_check": [
                {
                    "ref": "POK:687",
                    "status": "supports",
                    "note": "POK_full.txt, block 'Root / lemma: lehuk- (*lehugh-)', Meaning 'bright, to shine; to see', Page(s): 687-690 \u2014 with \"rocas-, rocis-, Avestan raocah-, ap. raucah- n. 'light, radiance, esp. of heaven', Avestan raox\u0161na- 'gleaming'\", \"Latin l\u016bmen 'light' from *leuk-s-men; l\u016bna 'moon goddess' (*leuksna)\", \"lustrum ... l\u016bstro, -are 'to light up, illuminate'\", \"Gothic liuha\u00fe 'light' ... Old English leoht\""
                },
                {
                    "ref": "KNT:205",
                    "status": "supports",
                    "note": "Kent, Old Persian, Lexicon s.v. raucah- (KNT.txt leaf 229): \"raucah- sb. 'day': Av. raocah- 'light', Phl. r\u016b\u010d, NPers. r\u014dz, Skt. r\u00f3cas- 'light', pIE *leugos\"; cf. \u00a7156.II \"pIE *leugos, OP rauca, Skt. r\u00f3cas\". Kent's *leug-/*leugos is the same root in pre-1959 notation."
                }
            ],
            "consulted": [
                {
                    "src": "AHD",
                    "where": "Watkins 1985, s.v. leuk-",
                    "stance": "supports",
                    "note": "\"leuk-. Light, brightness. I. Basic form *leuk- ... [Pok. leuk- 687.]\" with the Germanic, Latin and Greek branches of this chart"
                },
                {
                    "src": "WLD",
                    "where": "Walde-Pokorny Bd. II 408-411, s.v. leuq-",
                    "stance": "supports",
                    "note": "the same root under the older lemma leuq-: \"rocas-, rocis- n., av. raocah-, ap. raucah- n. 'Licht, Leuchte, bes. des Himmels', ai. ruk\u1e63\u00e1- 'gl\u00e4nzend', av. raox\u0161na- 'gl\u00e4nzend' ... (= lat. luna ...); auf diesem -es-St. beruhen auch lat. l\u016bstr\u0101re, lucubr\u0101re\""
                },
                {
                    "src": "IEC",
                    "where": "Mann, s.vv. leuk-, leukos, leuks-",
                    "stance": "supports",
                    "note": "\"leukos (louk-) 'light, white; light, brightness'. Cf. louk-, luk-. WP II, 408: Skt. r\u00f3ka\u1e25 ...; Av. raoc\u014d n. 'glitter'; OPers. rauca- 'day'; Myc. & Gk. leuk\u00f3s\" \u2014 Mann's leukos is precisely Nourai's 'Leuqos'"
                },
                {
                    "src": "SYN",
                    "where": "Buck 14.41 DAY (p.991) and 7.25 WINDOW (p.470)",
                    "stance": "supports",
                    "note": "'day' table gives OPers. rauca; the WINDOW article gives \"Av. raocana- (NPers. r\u014dzan) : Skt. rocana- 'bright'\""
                },
                {
                    "src": "KLN",
                    "where": "Klein s.v. light (n.)",
                    "stance": "supports",
                    "note": "sets out the whole root under \"I.-E. base *leuq-, 'to emit light, to shine; bright'\", including Av. raocant-, raox\u0161na-, Lat. lux, lumen, luna, lustrum, lustrare"
                }
            ],
            "nodes": [
                {
                    "id": 1,
                    "lang": "Avestan",
                    "words": "rao\u010dah; rao\u010d-x\u0161aema, raox\u0161na; a-rax\u0161a; aiwi-raocya",
                    "verdict": "disputed",
                    "derivation": "Three of the four items are solid. (a) Av. raocah- n. 'light, luminary (esp. of heaven)' (Bartholomae, AiW cols. 1489-91: \"j., g. raocah-, p. raucah- n. 1) 'Leuchte' (bes. des Himmels)\") is the inherited -es-/-os- neuter *leuk-os of the root, with the regular Indo-Iranian changes PIE *l > Ir. r and *k > \u010d before a front vowel (Skt. r\u00f3cas-, r\u00f3cate). (b) Av. raox\u0161na- 'bright, shining' (AiW 1488) = *rauk-s-na-, the same -s- stem that underlies Lat. l\u016bna (*leuk-s-n\u0101), OPruss. lauxnos, OHG liehsen; it is the direct ancestor of NP r\u014d\u0161an. (c) Nourai's 'aiwi-raocya' is Av. aiwi.raocaya- 'to illuminate, light up' (AiW s.v. raok- 'leuchten': \"mit aiwi 'beleuchten, bescheinen': ya\u03b8 h\u012b st\u0101r\u0105m .. aiwi.raocay\u0105nte\", V.19.23), the ancestor of NP afr\u016bxtan (Horn no. 94). BUT (d) 'rao\u010d-x\u0161aema' is not an attested Avestan word: Bartholomae's raoc-/raox\u0161na- family is raox\u0161na-, raox\u0161nay-, raox\u0161nav-, raox\u0161n\u0101-, raocana-, raocah-vant-, raocas-ca\u0113\u0161man-, raocas-pairi\u0161ta- \u2014 nothing like rao\u010d-x\u0161aema. It is Nourai's own segmentation of raox\u0161na- as rao\u010d + x\u0161a\u0113- (hence his cross-reference to root Ksei 2, i.e. x\u0161ay-/x\u0161a\u0113ta- 'shine'); the printed page (pdf 312) does show 'rao\u010d-x\u0161aema', so the JSON is faithful and the odd form is the book's. And (e) 'a-rax\u0161a : bright' does not exist either: the Avestan word behind NP \u0100ra\u0161 is \u018er\u0259x\u0161a-, which Bartholomae (AiW s.v. \u0259r\u0259x\u0161a-) gives only as \"EN. eines ber\u00fchmten iranischen Sch\u00fctzen\" (Yt.8.6 ti\u03b3ri\u0161 .. yim a\u014bhat \u0259r\u0259x\u0161\u014d x\u0161viwi.i\u0161u\u0161 x\u0161viwi.i\u0161vat\u0259m\u014d airyan\u0105m 'the arrow which \u018e. shot, the best archer of the Aryans'), with no meaning 'bright'; its etymology is uncertain (a root meaning 'bear' is the usual guess). Hence the node is disputed for those two items.",
                    "derivation_fa": "\u0633\u0647 \u0635\u0648\u0631\u062a \u0627\u0632 \u0686\u0647\u0627\u0631 \u0635\u0648\u0631\u062a \u0627\u06cc\u0646 \u062c\u0639\u0628\u0647 \u062f\u0631\u0633\u062a \u0627\u0633\u062a: \u0627\u0648\u0633\u062a\u0627\u06cc\u06cc raocah- \u00ab\u0631\u0648\u0634\u0646\u0627\u06cc\u06cc\u060c \u0641\u0631\u0648\u063a (\u0628\u0647\u200c\u0648\u06cc\u0698\u0647 \u0627\u062e\u062a\u0631\u0627\u0646 \u0622\u0633\u0645\u0627\u0646)\u00bb \u0647\u0645\u0627\u0646 \u0633\u062a\u0627\u06a9 \u062e\u0646\u062b\u0627\u06cc *leuk-os \u0647\u0646\u062f\u0648\u0627\u0631\u0648\u067e\u0627\u06cc\u06cc \u0622\u063a\u0627\u0632\u06cc\u0646 \u0627\u0633\u062a \u0628\u0627 \u062f\u0648 \u062f\u06af\u0631\u06af\u0648\u0646\u06cc \u0622\u0648\u0627\u06cc\u06cc \u0645\u0646\u0638\u0645 \u0627\u06cc\u0631\u0627\u0646\u06cc\u060c \u06cc\u0639\u0646\u06cc l \u0647\u0646\u062f\u0648\u0627\u0631\u0648\u067e\u0627\u06cc\u06cc > r \u0648 k > \u010d \u067e\u06cc\u0634 \u0627\u0632 \u0648\u0627\u06a9\u0647\u0654 \u067e\u06cc\u0634\u06cc\u0646\u061b raox\u0161na- \u00ab\u0631\u0648\u0634\u0646\u060c \u062f\u0631\u062e\u0634\u0627\u0646\u00bb \u0633\u0627\u062e\u062a *rauk-s-na- \u0627\u0633\u062a\u060c \u0647\u0645\u0627\u0646 \u067e\u0633\u0648\u0646\u062f -s- \u06a9\u0647 \u062f\u0631 l\u016bna \u0644\u0627\u062a\u06cc\u0646\u06cc \u0647\u0645 \u062f\u06cc\u062f\u0647 \u0645\u06cc\u200c\u0634\u0648\u062f \u0648 \u0646\u06cc\u0627\u06cc \u00ab\u0631\u0648\u0634\u0646\u00bb \u0641\u0627\u0631\u0633\u06cc \u0627\u0633\u062a\u061b \u0648 aiwi.raocaya- \u00ab\u0631\u0648\u0634\u0646 \u06a9\u0631\u062f\u0646\u060c \u0628\u0631\u0627\u0641\u0631\u0648\u062e\u062a\u0646\u00bb (\u0628\u0627\u0631\u062a\u0648\u0644\u0645\u0647\u060c \u0630\u06cc\u0644 raok-) \u0646\u06cc\u0627\u06cc \u00ab\u0627\u0641\u0631\u0648\u062e\u062a\u0646\u00bb \u0627\u0633\u062a (\u0647\u0631\u0646\u060c \u0634\u0645\u0627\u0631\u0647\u0654 \u06f9\u06f4). \u0648\u0644\u06cc \u00abrao\u010d-x\u0161aema\u00bb \u062f\u0631 \u0627\u0648\u0633\u062a\u0627 \u0646\u06cc\u0633\u062a \u0648 \u062f\u0631 \u0641\u0631\u0647\u0646\u06af \u0628\u0627\u0631\u062a\u0648\u0644\u0645\u0647 \u0686\u0646\u06cc\u0646 \u062a\u0631\u06a9\u06cc\u0628\u06cc \u0648\u062c\u0648\u062f \u0646\u062f\u0627\u0631\u062f\u061b \u0627\u06cc\u0646 \u062a\u062c\u0632\u06cc\u0647\u0654 \u062e\u0648\u062f\u0650 \u0646\u0648\u0631\u0627\u06cc\u06cc \u0627\u0632 raox\u0161na- \u0627\u0633\u062a (\u0627\u0632 \u0627\u06cc\u0646\u200c\u0631\u0648 \u0627\u0631\u062c\u0627\u0639 \u0627\u0648 \u0628\u0647 \u0631\u06cc\u0634\u0647\u0654 Ksei 2 = x\u0161ay-/x\u0161a\u0113ta- \u00ab\u062f\u0631\u062e\u0634\u06cc\u062f\u0646\u00bb)\u061b \u062a\u0635\u0648\u06cc\u0631 \u0635\u0641\u062d\u0647\u0654 \u0686\u0627\u067e\u06cc \u0646\u0634\u0627\u0646 \u0645\u06cc\u200c\u062f\u0647\u062f \u06a9\u0647 \u0647\u0645\u06cc\u0646 \u0635\u0648\u0631\u062a \u062f\u0631 \u06a9\u062a\u0627\u0628 \u0622\u0645\u062f\u0647\u060c \u067e\u0633 \u062e\u0637\u0627 \u0627\u0632 \u06a9\u062a\u0627\u0628 \u0627\u0633\u062a \u0646\u0647 \u0627\u0632 \u062e\u0648\u0627\u0646\u0634 \u0627\u0633\u06a9\u0646. \u0647\u0645\u0686\u0646\u06cc\u0646 \u00aba-rax\u0161a\u00bb \u0628\u0627 \u0645\u0639\u0646\u0627\u06cc \u00ab\u0631\u0648\u0634\u0646\u00bb \u0648\u062c\u0648\u062f \u0646\u062f\u0627\u0631\u062f: \u0635\u0648\u0631\u062a \u0627\u0648\u0633\u062a\u0627\u06cc\u06cc \u0646\u0627\u0645 \u00ab\u0622\u0631\u0634\u00bb \u018er\u0259x\u0161a- \u0627\u0633\u062a \u06a9\u0647 \u0628\u0627\u0631\u062a\u0648\u0644\u0645\u0647 \u062a\u0646\u0647\u0627 \u0622\u0646 \u0631\u0627 \u0646\u0627\u0645\u0650 \u06a9\u0645\u0627\u0646\u06af\u06cc\u0631 \u0646\u0627\u0645\u062f\u0627\u0631 \u0627\u06cc\u0631\u0627\u0646\u06cc \u0645\u06cc\u200c\u062f\u0627\u0646\u062f \u0648 \u0647\u06cc\u0686 \u0645\u0639\u0646\u0627\u06cc \u00ab\u0631\u0648\u0634\u0646\u00bb \u0628\u0631\u0627\u06cc \u0622\u0646 \u0646\u0645\u06cc\u200c\u0622\u0648\u0631\u062f\u061b \u0631\u06cc\u0634\u0647\u200c\u0634\u0646\u0627\u0633\u06cc \u0622\u0646 \u0646\u0627\u0645\u0639\u0644\u0648\u0645 \u0627\u0633\u062a \u0648 \u062d\u062f\u0633\u0650 \u0631\u0627\u06cc\u062c \u0645\u0639\u0646\u0627\u06cc \u00ab\u062e\u0631\u0633\u00bb \u0627\u0633\u062a. \u0628\u0646\u0627\u0628\u0631\u0627\u06cc\u0646 \u0627\u062f\u0639\u0627\u06cc \u0646\u0648\u0631\u0627\u06cc\u06cc \u062f\u0631 \u0627\u06cc\u0646 \u062f\u0648 \u0645\u0648\u0631\u062f \u067e\u0630\u06cc\u0631\u0641\u062a\u0646\u06cc \u0646\u06cc\u0633\u062a.",
                    "sources": [
                        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewk-",
                        "https://www.behindthename.com/name/arash"
                    ],
                    "ref_check": [
                        {
                            "ref": "HRN:23",
                            "status": "supports",
                            "note": "Horn p.23 no.94 (HRN.txt leaf 44): \"efr\u014dxten 'anz\u00fcnden, erleuchten' ... aw. aiwi + \u221aruc- 'anz\u00fcnden'; phlv. afr\u014dxtan, afr\u014dc\u012bn ...; skr. abhi + \u221aruc-\" \u2014 exactly Nourai's aiwi-raocya > afr\u016bxtan arrow."
                        },
                        {
```


## [2026-09-07T15:49:49.178Z] TOOL CALL #7: Bash

```json
{
 "command": "ls site/pages/324.jpg 2>/dev/null; pdftoppm -f 324 -l 324 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg324 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


## [2026-09-07T15:49:49.779Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"med-\" POK_full.txt | head -40"
}
```


### [2026-09-07T15:49:50.987Z] TOOL RESULT

```
site/pages/324.jpg
total 80
drwx------ 2 sfmqrb sfmqrb  4096 Sep  7 11:49 .
drwx------ 4 sfmqrb sfmqrb  4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   251 Sep  7 11:49 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40 Sep  7 11:49 queue.txt
```


### [2026-09-07T15:49:51.025Z] TOOL RESULT

```
8403:(*cut) ' : *med-, *ue- 'blow' : Old Norse vedr. Modern High German Wetter), wherefore 
29488:the preposition in- being /; about acymr. permed-interedou q\. "that part of the abdomen 
57925:Umbrian mefs, mers^ right, privilege; law ' {*med-os-), mersto^ just, upright, righteous, 
57926:fixed by law, according to law, lawful, legal, legitimate ', Oscan med-diss^ a judge, decider, 
57931:pass judgment, decide ', airmed^ measure ', mess' a judgment' {*med-tu-), med {*meda) 
57998:\^zo^^q "full'; Middle Irish messm. {*med-tu-) " acorn, acorn mast, fruit harvest ', cymr. 
58043:lemma: med-1\ to measure; to give adviee, healing. 
60973:References: WP. II 237 f., WH. II 70 f., 81 f., Trautmann 179, 183; related with 1. med-.
```


## [2026-09-07T15:49:54.068Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '57890,58060p' POK_full.txt"
}
```


### [2026-09-07T15:49:54.122Z] TOOL RESULT

```
References: WP. II 261, Trautmann 173 f., Berneker II 31. 
Page(s): 707 

Root / lemma: mehd-1 

Meaning: to measure; to give advice, healing 

Material: A. Old Indie masti-i. " the measuring, weighing '; 

Maybe alb. mas, /77a/"measure'. 

whether also zero grade of Old Indie addha ( *md-6'^e) "certainly, yea, in truth ', Avestan 
Old pers. azdads.. Old Indie addhat/- ^ smart man, sage' with the meaning from Latin 
med/tar/etc.7 s. Pedersen Decl. Latin 72; 

Note: 



zero grade of Old Indie addha {*md-6^^ "certainly ' : Avestan Old pers. azda6s., Old Indie 
addhatf- 'smart man, sage' similar to gr. zero grade of gr. *mYa aya- "very' see Root / 
lemma: mehg(h)- : meg(h)- : big 



Armenian m/f{Gen. mti) "thought, notion, sense, mind' (: \ir\bzcx ete.); 

gr. |j£5o|jai "bin whereupon bedaeht', pi£5(jov, pisSswv "Walter, ruler', p£5iMV0(; " bushel '; 
lengthened grade pinSopai "ersinne, eateh einen Besehlufl', pnSea Nom. PI. "sorrows, 
advice^ounser^jnoKop^A^^ 

Latin meditor, -arf to reflect, muse, consider, meditate, give attention ', modus^ a 
measure, extent, quantity ', modestus^ keeping due measure, moderate, modest, gentle, 
forbearing, temperate, sober, discreet ', moderare^ to set a measure, set bounds, put 
restraint upon, moderate, mitigate, restrain, allay, temper, qualify ', modius' bushel ', 
Umbrian mefs, mers^ right, privilege; law ' {*med-os-), mersto^ just, upright, righteous, 
fixed by law, according to law, lawful, legal, legitimate ', Oscan med-diss^ a judge, decider, 
umpire in any matter ' ( *medo-diR-s) etc.; 

Old Irish midiur, Perf. ro-mTdar{: gr. [jriSopai, Gothic metum, Armenian mit} " to consider 
thoroughly, ponder, weigh, reflect upon, think, to examine judicially, to judge, be a judge, 
pass judgment, decide ', airmed^ measure ', mess' a judgment' {*med-tu-), med {*meda) 
" scales ', cymr. meddwr the rational soul, the mind, disposition, feeling, character, heart, 
soul, a thinking, considering, deliberating, thought, reflection, meditation, imagination ', 
mcymr. medu' be able, control ', cymr. /77e'ofa'^ " possess, control' (numerous Irish 
compounds by Pedersen KGr. II 577 f., British formations by J. Loth RC. 35, 446; 38, 177, 
296; 40, 347 ff., 350 f.; Ifor Williams RC. 40, 486; J. Lloyd-Jones RC. 43, 272); medd 
"inquif etc.; 

Gothic mitan. Old English metan. Old High German mezzan' measure ', Old Icelandic 
meta' assess ', metu. " weight ', Old English ge-metv\. " the measuring ', Adj. " fitly, 
reasonable'. Old High German mez' measure, drinking vessel'. Old English m/ttam. "grain 
measure'. Old High German mezzo " small dry measure ', Modern High German Metze(n), 
Gothic miton. Old High German mezzon' evaluate, estimate, consider'. Old Icelandic 
mjgtudr'iaie, destiny'. Old Saxon metodvn. "knife, orderer, arranger, creator, god'. Old 
English metodm. "fate, destiny', Gothic mitat^s' dry measure '; 



©■grade (besides PI. preterit Gotliic metumeic.) Gotliic us-meV lifestyle ', Old Icelandic 
matu. " the measuring ', Middle High German mazn. " measure, kind of way', Old High 
German maza^ measure, fitness, suitability ', Old Icelandic maetr^ respectable, valuable ', 
Old English gemsete^ suitable; fitting ', Old High German maz/6s.; 

<7-grade: Gothic ga-mot'may, find space, have place, permission ', Old English motan^ 
can, to be able, have the occasion ' (engl. must^ must, have to ' from the preterit). Old 
Saxon motan^ should, must find a place, have an occasion ', Old High German muoz, 
muozan^ to be able, possible, could be, might be, may be, may, might, can ', Modern High 
German mussen; Middle Low German motelree time, time, period '; 

Old High German muoza'iree time, attention, opportunity to something'. Modern High 
German Mulie, Old English se-metta, semta, from *a-mdtida\. ' leisure ', whereof 3em(e)tig 
= engl. empty^ empty, bare, lacking'; Old Icelandic motn. ' image, sign, kind, way '; 



Gothic mota^ customs duty ', Middle High German muoze^ Mahllohn ', Old English mot 
" customs duty, tribute, tax'; probably from Gothic derive Old High German (Bavarian) 
muta. Modern High German Maut, Middle Latin muta. Old Bulgarian myto. 

B. An already Proto language application for ' wise counsellor = one skilled in medicine ' 
lies in: Avestan vT-mad-^ one skilled in medicine, physician, medicine man', vT-ma5ayanta^ 
sie sollen die Heilkunde ausuben ', gr. Mr|5o(;, Mri5r|, 'AyapriSn etc. ' Heilgottheiten '; Latin 
medeor, -erf to heal, cure, remedy, be good for ', /77e'o'/ic^s 'physician, medicine man' 
(with secondary formants -/ic^sof Subst. 'Vr7eo'' physician, medicine man' = derived 
Avestan vT-mad). 

Latin medicus : Calabrese medicu ; miericu : Catalan metge : Catanese mericu : Furlan 
miedi : Sardinian Campidanesu meigu : Sicilian mericu : Valencian mege : alb. 

(*meiku) mjeku " doctor. 

Note: 

Alb. belongs to Occidental Romance languages. 

References: WP. II 259 f., WH. II 54 ff., 99 f.; 

See also: mehd- is related to meh-3 {above S. 703 f.). 

Page(s): 705-706 

Root / lemma: mehd-2 
Meaning: to swell 



Material: Gr. pis^sa (Hesiod), [itbza (Archil.), [jriSsa (Horn.; lies psSsa?) " male genitals '; 
\^zo^^q "full'; Middle Irish messm. {*med-tu-) " acorn, acorn mast, fruit harvest ', cymr. 
corn. mesi. " acorn ', bret. mez6s.\ also Middle Irish mess^ foster child '? 
References: WP. II 231 ; different Schwyzer Gr. Gr. 1 , 208. 
Page(s): 706 

Root / lemma: mehg(h)- : m^(h)- 
Meaning: big 

Note: (to Old Indie Aspiration s. Pedersen 5^ decl. Latin 48^, Hittite 36, 181 f.); to reduced 
grade compare Pedersen Hittite 169 f. 

Material: Old Indie mahant-, Avestan mazant-^b\Q, large'. Old Indie mah-, Avestan maz- 
ds. (only out of Nom. Akk.), Old Indie mah/Hom. Sg. neutr. (-/= -a, then = gr. (jsya), as 
front part Old Indie maha- (Avestan mqza- is a text mistake), mostly extended mahat- = 
Avestan mazant-'b\g, large'; Kompar. Superl. Old Indie mahTyas-, mahistha-, Avestan 
mazyah-, mazista-; 

Old Indie mahayatr pleases, venerates', maha-rc\. " celebration, sacrifice, oblation', 
mahJyate^ rejoices '; Avestan mimayzo^ you should try to glorify ', that is to say "hold 
festivities'; 

Old Indie mahas-, Avestan mazah-n. "greatness, bulk, extent'. Old Indie majman- 
"greatness, bulk, extent', Avestan /775Z5/7- "greatness, bulk, extent, grandeur'. Old Indie 
mahV the great, the old people, the earth ' (: Latin Mala); 

Adv. Gatha-Avestan /775s "very' ( *meghs), zero grade ( *rnghs) jav. as "very'; 

Armenian /77ec"big, large', Denomin. mecarem' uphold, preserve, honour; ' (: gr. 
|j£Yaipoo); 

gr. (jsyac;, (jsyaAri, psya {*meg-n) "big, large' (to (jsya is v^t^cxc,, -av neologism; psyaAo- 
the case obi. and of Fem. contains *a/c»-" growth, stature ', as xQaijaAoq "low'); Kompar. 
Ionian Doric Arcadian [je^wv from *fj£Yju)v (Attic [jei^wv after xsipwv), Superl. fj£YiaTO(;; 
psyaipcjo (: Armenian mecarem) " schlage hoch an, bewundere; halte fur zu hoch, 
miflgonne '; zero grade from *rnYa aya- "very' (aYa-vvi(po(; etc.), ayav "to very', aya^u) 
"aegre fero', compare a^ov psyav, uijjeAov Hes. and jav. as- "very'; in addition probably gr. 
dyaopiai " envy', ayafjai " adore, venerate', ayaAAu) " glorify ', ayanau) "love', ayauoc; 
"admirable, venerable'; 

Note: 



zero grade of Old Indie addha {*md-6^§) "certainly ' : Avestan Old pers. azda6s., Old Indie 
addhatf- 'smart man, sage' similar to gr. zero grade of gr. *mYa aya- "very' see Root / 
lemma: med-1\ to measure; to give adviee, healing. 

alb. math, madh/"b\g, large', madhonj^ aggrandize, praise'; 

Maybe alb. zmadhof increase ' Slavic z- prefix. 

Note: 

Alb. math^b\g,: mcymr. ma/th'\ong, big' large' common alb. - mcymr. -k > -th. 

Latin magnus'b\g, large' {*meg-nd-s), Kompar. mag-is^ more, in a higher degree, more 
completely ', maior^ greater' {*meg-Jds), Superl. maximus {*meg-Semo-s)\ in addition 
maiestas^ greatness, grandeur, dignity, majesty ' {*meg-Jes-tat-), compare alb. madheshtf 
( *megis-t-iJS) ds. (about Oscan mais, maimas, Umbrian mestrusee below me- "big, large'), 
Maia " Daughter of Atlas and Pleione, and the mother of Mercury by Jupiter '; deus Maius 
"Juppiter' (Tusculum), whereof the month Maius {as Oscan Maesius^ May ' derives from 
the missing God's name, s. Schuize Eigenn. 469 ff.), Oscan PN Ma/'/ufDat Sg. (compare 
also Celtic magio-); Latin (Celtic, also alb.) -a- is Indo Germanic e, about Latin maialis^ a
```


## [2026-09-07T15:50:05.792Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 70[0-9]\" POK_full.txt | head -20; echo ---; grep -n \"Page(s): 73[0-3]\" POK_full.txt | head; echo ---; grep -n \"lemma: meh-3\\|lemma: mehnot\\|menot\\|mehns-\" POK_full.txt | head -20"
}
```


### [2026-09-07T15:50:05.868Z] TOOL RESULT

```
57405:Page(s): 700 
57443:Page(s): 700 
57457:Page(s): 700 
57472:Page(s): 700 
57494:Page(s): 701 
57508:Page(s): 701-702 
57756:Page(s): 700-701 
57841:Page(s): 706-707 
57891:Page(s): 707 
57990:Page(s): 705-706 
58001:Page(s): 706 
58096:Page(s): 708-709 
58296:Page(s): 709 
58642:Page(s): 702 
58673:Page(s): 702-703 
60692:Page(s): 707 
60768:Page(s): 703 
60802:Page(s): 703 
60974:Page(s): 703-704 
61010:Page(s): 704 
---
59350:Page(s): 730 
59416:Page(s): 730 
59449:Page(s): 730-731 
59468:Page(s): 731 
59767:Page(s): 732 
59794:Page(s): 732-733 
60013:Page(s): 733 
61109:Page(s): 731-732 
61760:Page(s): 731 
---
61083:Root / lemma: menot. Gen. meneses, from which menes-, mens- mes-, men- 
61096:stem); Gothic menot^s. Old Icelandic manadr. Old English monad. Old Saxon manuth. Old
```


## [2026-09-07T15:50:09.217Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '60900,60980p' POK_full.txt; echo \"=====MENOT=====\"; sed -n '61083,61112p' POK_full.txt"
}
```


### [2026-09-07T15:50:09.301Z] TOOL RESULT

```
There "small cattle' could be an old nominalization of an Adj. meaning "small', one 
compares further Old Bulgarian malt ( *mdlo-) "small, little' (whereof kir. mal'i. collective 
"young sheep', etc.), Latin malus'evW, bad' (as small'), Oscan mallom, mallud^ malum ' 
(with expressive //?); 

with ani. 5- Gothic smals{*sm9-lo-). Old High German Old Saxon smal. Old English smael 
"small, little, narrow, tight, slim, slender, thin ', Old Icelandic smaleu. "small animal'. Old 
High German smala-noz, smaiaz fihu. Middle High German smal-noz, smal-vihe^6s., 
young animal ', Middle High German s/77a/-/7//'/e "herdsman, shepherd for small cattle'. 



References: WP. II 296, WH. II 20. 
Page(s): 724 



Root / lemma: me-3, m-e-t- 

Meaning: to measure 

Material: Old Indie mati, m/mat/"r(\\Q>t', m/fa-' measured, calculated ', matrai., mafra-n. " 

measure ', mana-n. 'the measuring, measure ' (: Czech men), mati-i. " measure, right 

cognition ' (= gr. mhtk;. Old English meed), upa-mati-' allocation ', mit'h ' measure, weight, 

cognition ', prakr. mettamAs. (= Old Indie *mitram)\ about mayas. 1. ma-\ 

Avestan ap. ma-^ measure ', participle -mlta-, -mata-, ap. fra-mafar-'\or6, master', 
Avestan m/f/- ' measure, weight, value, worth '; 

alb. mat, mas{*matid) " measure ', mate^ measure ', mdt{*meto-) "year, weather', 
matem^ raise the hand to strike, throw, cast' ('gauge = aim'); 

Maybe alb. moshe^ age '. 

Irish to-math-{e.g. 3. Sg. do-math/) "threaten'; 

gr. iJETpov " measure ' (after Brugmann Grundr. I|2 1, 342 as Old Indie d-a-tra-m "gift' to 
*dd-); mhtk; "plan, artifice', |jr|Tiau) " decide ', pr|TiC(0|jai " think up, dream up; invent '; 

Latin metior, -Tn, mensus sum (rhyme meaning to pensus) " measure, gauge ', whereof 
probably /77e/75a "table, a table, meal, course, a money-changer's counter, a sacrificial 
table, alter ' = Umbrian mefe^ measure ', mefa' a cake, pancake (flour, made up with milk 
or oil, and baked) ' as subst. Fem. of participle Perf. Pass.; 

mcymr. medru^ ein Ziel treffen, to be able ', to medr^ dexterity ' (: gr. [jsipov?); gall. 
matar/s^ spear, lance'; perhaps here acymr. maut. Middle Breton meut{*md-ta), ncymr. 
bawd' thumb ' (as measure?); 

Old English maedi. " measure '; Gothic me/am. " bushel '; Old Icelandic msef/rm. 6s., 
Old English maele, mele' paten '; Old Icelandic maela' measure '; Gothic melu. "time'. Old 
Icelandic mar measure, moment, time, repast, meal'. Old English mse/6s.. Old High 
German ma/' moment, repast, meal'. Modern High German ma/'meaV; 

Lithuanian metas'year, time, measure ', Old Prussian mettan'year', Latvian m^ts 
"stretch of time' (vocal as gr. iJEipov to beurteilen); in addition (*gauge > *aim > throw) 



Lithuanian metu, mesti, Latvian metu, mest'Vnrow', Iterat. Litliuanian metyt, Latvian metat 
" throw to and fro '; Old Prussian metis= Lithuanian metis vn. " throw, shot'; mastasm. " 
measure ', matasm. 6s., mafuof/" measure ', pamafas' foundation ' etc.; 

Old Church Slavic mefg, /77e5//" throw', slov. motati^ wind up, roll up ', russ. -Church 
Slavic Iterat. vbmetat/^ throw', slov. met^ throw, shot', etc.; Old Church Slavic mera' 
measure ', meriti^ measure '; Czech old men^ measure ' (: Old Indie mana-), russ. metitb 
"aim; strive ', etc.; 

Tocharian A me-, B mai- " measure '. 

References: WP. II 237 f., WH. II 70 f., 81 f., Trautmann 179, 183; related with 1. med-. 
Page(s): 703-704 

Root / lemma: me-4, mo- 
Meaning: big, important 

Material: Positive me-ro-s, mo-ro-s. gr. -pu)pO(; in £YX£cri-p(jopo(; 'big, large (?) in 
Speerwerfen ' , Old Irish mdr{dirom the comparative), mar^b\Q, large', cymr. mawr^b\i^, 
=====MENOT=====
Root / lemma: menot. Gen. meneses, from which menes-, mens- mes-, men- 
Meaning: month; crescent 
Grammatical information: m. 

Note: probably as personified ' time measurement ' to me-^ measure '. 
Material: Old Indie mas, masa-m., Avestan ma. Gen. marjhd, npers. /77a/7'moon, month '; 
Armenian amis. Gen. amsoy^ month ' {*mensos); gr. Attic neologism ppv, to Gen. \xv\y6c, 
(Lesbian pnvvoc;), Nom. Ionian \iz\c,, Doric \xr\(;, m. ' month ' {*mens), \xryjx\ (*|jr|vaa) 'moon'; 
alb. muai^ month ' ( */77d/7- from Indo Germanic *men-); lat mens/sm. ' month ' 
(conservative Gen. PI. mens-um), menstruus^ monthly ' (GN Mena\s gr. loanword), 
seme(n)stris^ 6-month, half-years of age, six-month-old ', Umbrian menzne^ mense '; Old 
Irish mT{*mens), Gen. mTs{*mensos), cymr. acorn, mis, bret. /77/z' month '; Gothic mena. 
Old Icelandic man!. Old English mona. Old Saxon Old High German /77a/7c»'moon' {-en- 
stem); Gothic menot^s. Old Icelandic manadr. Old English monad. Old Saxon manuth. Old 



High German manot, Modern High German month {*mendt-), Lithuanian menuo{*mendt), 
menes/sm. 'moon, month ', Latvian menes{/)s^ moon, month ' (dial. Lithuanian menas 
from a neutr. *menos). Old Prussian men/'ns' moon'; Old Bulgarian mes^cbm. 'moon, 
month ' ( *mes-n-ko-)\ 

Tocharian A man^ month ', man nkat'moon' (= ' month god '), B mene' month ', mem 
'moon'. 

References: WP. II 271 f.. WH. II 71 f., Trautmann 179 f., Brandenstein Studien 11 f. 
Page(s): 731-732 

Root / lemma: meuA^-, mauA^-, mud'^- 
Meaning: to complain or care about smth.
```


## [2026-09-07T15:50:15.806Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: medhu\\|lemma: mehdhu\\|medhu-\" POK_full.txt | head -20"
}
```


### [2026-09-07T15:50:15.859Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T15:50:18.157Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '57830,57895p' POK_full.txt"
}
```


### [2026-09-07T15:50:18.205Z] TOOL RESULT

```
Old Bulgarian mezda^road,' (originally " boundary strip '). 

Maybe alb. mezhde, mezhda^ baulk, strip of land between fields ' a Bulgarian loanword. 

russ. meza^ limit, boundary, slope ' (etc.). Old Bulgarian mezdu {Loc. Du.) " between ' 
Adv. preposition. Old Russian mezi{Lok. Sg.) ds.; here also probably as '* forest, 
boundary strip ': Old Prussian median, Latvian /77ezs'wood, forest', Lithuanian medzias 
"tree'; Lithuanian FIN Meduya. 

References: WP. II 261, WH. II 57 f., Trautmann 173, Specht Indo Germanic Dekl. 133 f. 
Page(s): 706-707 

Root / lemma: meljd^u 

Meaning: honey, intoxicating drink, mead 

Grammatical information: n. 

Note: actually nominalized adjective 'sweet' 

Note: 

Root/ lemma: mehli-t\ "honey' : Root/ lemma: meM^u: "honey' derived from a truncated 

Root /lemma: mehl-1 {awch smehl-), mehlsh-' mle-, mehl-d-. ml-ed-, mehl-6'^-, ml-ei-: 

mlh, mehlah-k-. mla-k-, mieu-. mlu-\ "to grind, hit; fine, ground'. 

Note: 

Root/ lemma: rnahd-: wet; glossy, fat, well-fed, intoxicating : Root/ lemma: meM'^u: 

honey, intoxicating. 



Material: Old Indie madhu-v\. "honey, mead ' (in addition macfhu-'s\Nee\.'; madh(u)v-ad- 
" honey-eater': Old Church Slavic medv-edb 'bear'); Avestan madu- n. " berry wine '; 

gr. |j£9u "wine ' (from the meaning "honey' has been abbreviated in pisAi = pisAi, -Toq " 
honey '); psGuu) ' be intoxicated', msGuokw "make intoxicated '; 

Old Irish m/'d {Gen. medd), cymr. medd, acorn. (Plur.?) medu, bret. mez 'mead ', Middle 
Irish medb^ intoxicating ' {*me6!^uo^, cymr. meddw^ intoxicated, drunk ', bret. mezo6s., 
mezvT intoxicate '; 

Old Icelandic mjgdr. Old English meodo. Old High German metum. " mead '; 

Lithuanian medusm. "honey' {m/'dus^ mead ' from Gothic *midus), Latvian mgdus 
"honey, mead ', Old Prussian meddo {*medu) "honey'; 

Old Bulgarian medb{Gen. meduand meda) "honey' (in addition among others serb. o- 
med/t/ se'spoW, ruin e.g. of fat', actually " sweetish, become tasteless or ferment'); 
Tocharian B /77// "honey'. 

Zur Konkurrenz with */77e///" honey' (not in any way " honey mead ') and about Finnish- 
ugr. comparison (Finnish mete-, lapp. m/tt, Mordovian med' chin, /t?/^ "honey') s. Gauthiot 
MSL. 16, 268 ff., Schrader RL. 85, 2139. 

References: WP. II 261, Trautmann 173 f., Berneker II 31. 
Page(s): 707 

Root / lemma: mehd-1 

Meaning: to measure; to give advice, healing
```


## [2026-09-07T15:50:35.010Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN bimar ===\"; grep -n -i \"bīmār\\|bimar\\|bTmar\\|bimär\" HRN.txt | head -20; echo \"=== HRN may/mul ===\"; grep -n -i \"^ *[0-9]*\\. *m[ae]i \\|Wein\" HRN.txt | head -40"
}
```


### [2026-09-07T15:50:35.070Z] TOOL RESULT

```
=== HRN bimar ===
2618:39. bimär 'krank^^ bimürJ.
11865:bimär 259.
=== HRN may/mul ===
1752:155. hädye *Weingefäss', vergl. bade 'Wein .
4609:510. x^"'*^) 'Schwein, :i)5 (Qiss. Dan. S. 388).
4612:skr. siikard- 'Eber, Schwein*.
6481:744. »ffgtir^ sngvrne, stiyvr 'Stachelschwein'. Si/uL sJ/ttr,
6488:schwein' (345).
7929:915. giristen, giristen *klagen, weinen', Impt. girl ^) girye,
7931:aw. [/^gar-, gerente 'anrufen*; phlv. grlstan 'weinen,
7934:kurd. girin weinen ; oss. d. yär, t. qär 'Geschrei,
7936:schreien, heulen, weinen*, Impt. bigri (117)^).
8034:Semn. vdle (vergl. np. vel *Blüte des Weinstocks*).
8408:Ar. mäSiy 'weisser Honig', moMyat 'glatter Panzer; "Wein* (dazu
8608:990. mul Wein'.
8609:ai. fn^d[vtka- 'Weintraube' (Hübschmann, ZDM6.
8665:997. möye 'Weinen, Klage', möylden,
8724:1003. mei 'Wein, jüd.-pers., ^^O.
8728:ksl. wedü 'Honig, Wein', nhd. Meth etc.
8905:1025*»*« nebld, nebtd 'Fruchtsaft, Wein »).
10541:93. garzltan 'klagen, weinen; beichten^)', garz(i)sn,
```


## [2026-09-07T15:50:37.078Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT vimad ===\"; grep -n \"vī-mad\\|vi-mad\\|vīmad\\|vimad\\|maδayanta\\|ma8ayanta\" BRT.txt | head -20; echo \"=== BRT azda ===\"; grep -n \"azdā\\|azda\" BRT.txt | head -20; echo \"=== BRT madu ===\"; grep -n \"maδu\\|maδa-\\|ma8u\" BRT.txt | head -20"
}
```


### [2026-09-07T15:50:37.155Z] TOOL RESULT

```
=== BRT vimad ===
24192:Bt.  vimadhya-  n.  'Mitte'").  —  ')  Hds.  'iim; s.  die  Var.  lu  Yt.  10.  104.  Doch  TgL  auch fatay-  No.  2.  —  ')  Wegen  tnp.  n  d  mn  d  (/Si.  I
24199:•  j.  vi-mad- :  'mäd-  m.  'Heilkundiger,  Arzt':
=== BRT azda ===
2080:logie.     Göttingen  I902. (PtroMBtADEB  Djaos:  Dyius  Asnra,  Ahnra  Mazda  und  die  Aiurai.     Halle  1885. BSächsGW.:  Berichte  der  phiL-hiiL  Klasse  der  K.  SächsUcben  Gesellschaft  der  Wissentchaften. BSLP.:  Bulletin  de  la  Socijlj  de  Ijnguiitique.     Paris. Bim.:  CrkBaktholomak. AF.!  Arische  Forschungen.     Halle  1S82  ff. AirV.:  Das  altiraniiche  Verbum.     München  1878.
2455:l'S.S  (wo  awÄ<f' als  LSf.),  Y.9-28';  —  w I  nH  aiäAili  i'lse  jamyät  as>mca  ..  asista  tä airihat  Aa'a  visal  güuS  buyät  Y.6'o.2i.; '  2.  S..2J.3.  52-3.  FrD.  P,  Yt.  /j.  i3;  ~  ioa fri>ä  .  .  buyata  ahmya  nmlne  Yt.  /J.  147  ; IS6f.^  Y.26.^,  62.3*;  —  fraddiäi  ahe nmanahe  ..  vlspaya  alaond  stöis  Y.52.4; 4.5',  Vr. ».  13*;  —  imim  >7oqm  .  .yänim .  .  jaioyemi  .  .  dn'atütam  aiiiAas?  tanvS ". .  Gesundheit  dieses  (meines)  Leibes"  Y. 5.19;  — yaiä  ratSm  akurö  valdil  . ,  aya qsayä(scL)Y.ji.2;  —  afäi  aAmäi  var^nai.. nidätitn  ahm  . .  iAaeiili  (sd.) . .  "und  in  diesen (ünsem)  Glauben  .  ."  Y.4ff-3;  —  aitiAa daenayä  mqs  vaca  dd^anaAe  Y.  j?.  3 1 ;  — frä  KTjri»ie(sd.)aA£(XS{.alsinstr.)da^(^a ..  aAura  ..  Vr.5.3;  —  atcäv3  mizdtm  (sd.) anhat  aAyä  magahyH  y.  S3T>  —  H  *"''^ (sd.)  maiy  aniya/ay  vasiy  astiy  kartam avJ*  ahiyäyä  dipiyä  ttaiy  nipislam  (sd.) ".  .  in  dieser  (meiner)  Inschrift  (hier)  . ." Bh,  4-  S;  —  yS  ach-a  mazdayasnalh-a  .  . ". .  wer  hier  unter  den  Af.  .  ."  V-S-z; —  aAyil  '^wil  J^rff  rtr»z3nil  .  .  pairl.ja-
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in  . . yantä  aiibyö  dair?  (sd)  voka  as  manö  Y.  \  geraten,  dadurch  könnte  er  Schaden  neh- 34-&]  9.  2&  10,  45-ii  — yaisqm  ..  mazdä  \iata"  V,/_j.37;  —  ahmat  haca  /«>nj  (sd) ..  vatghö  vai'ja  alsqm  ..  Yt.i6.%; — ^J  sayiJ/A' Nik.  7;  *2; — yesi  tat  paiti  irisjati syao^anä  yä  vacatihä  yä  yasnJ  .  .  ae^qm  '  aiähal  hala  iyae>n!i7ar3za  (sd.)  .  ,  V./_?. töi..}hmä  pourutimäil  äasl?(sd.}Y.j4-^,''  38-  2)  vorausweisend;  i)  adjektivisch ■ —  yöi  *aite  . .  *gä'kä  nSit  *srävayänti  . .  I  auf  direkte  Rede  oder  Zitat:  vahiütsm  . . assqm  fyaohamm\ia'\  .  .  N, 25;  —  ySt  ..'igänii  ..  vir^zyat  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag-  *pt3  asahyä  mazdlY.4y.2;~aya  antar?.- £qm  nöit  aita^qm  ratufris  ..  N.52;  ^j\  uxti  (sd.) :  nöit  nS  mana  (usw.,  Y..^5.z) —  yahmät  kakmäicit  nalmaruim  vätS  ä'^rö  Y.ig.i$.  —  a)  mit  ergänzendem  Relativ: baoiolm  vibaraiti  (sd.)  ahmll  kahmäiHt  aya  aibigara  (LS.  als  Instr.)  aya  aibijary- nalmanqm..\.8.&o.  a)  Die  Beziehung  ta{d.^.)  yä  amfsanqm  sp^ntanqm..:  gave ist  ungenau:  ^yJ  räakaytn  (sd.)  sravaahä  rto5j/(usw.,Y._j5.4)  Vr.J2.i.  a)  substan- vahistät  iyadkanäl  mantärü  aeibyö  mazäi  tivisch  und  adjektivisch  auf  eine  erläuternde akä  (sd)  mraot  "qua  alienant  doc-  oder  ergänzende  nominale  Beifügung:  «7.5- trina  . .,  üs  .  ."  (statt  qui  ..  iis  ,  .)  Y.32.  yacä  i^agtuL  yäsat  ahyi  Virßzin3m..ahyä .. 1 2'*^  Anhang  zu  II  I  1,  2.     a)  An   ahurahya  uruasimai^A.)  mazda  Y.j2.i ;  2S.
2479:Fem.  Sing.:   yä  haca  da?vayasnalibyö  .  .{yäahurahemazdaY. 68.12;  —  ahenarl-.yo
2488:ultä  kakmäiclt  .  .  däyät  ahurö 44-i6,  27.14;  — yastn  .,  tari.mqstä  .. anying  ahmat  yi  hei  arim  mainyätä  Y. 4j.ii;  —  anyö  akmat  yö janaili  V.5. 34; N.  iS\  —  agustä  (sd.)  vacS  singhamahl aHbyö  yöi  ,  .  alakyä  gaSha  vlm?r?ncaiis (sd.)  aihp  aiibyö  nahiltä  yöi  *zrazda  aa- Afn  tnazdai  Y.j/.  i;  jo.8;  —  alsam  gä- naoiti  v?rfirayrtim  yöi  diin  .  .  /r3yaz?nte YL/O.16;  —  vätöyö/ä (sd.)  1/  aäbyöyöi  Tl.. v»r^syqn  Y.J5.6;  —  vJspaiibyö  aiibyö  yöi .  .  upa.sruttvanii  N.  20;  —  ahe  .  .  yö  nö dussarfkö  AiitaiteY.  10.12  (s.a.);  —  mäoa fiS  a/tmi  /raniliti  (sd.)  yÖ  nö  ..  inrixsaile ^■^5'7i  —  ^y^  *äröi  häkunnim  {'^d^ yayä haiinti  urvqnö  Y.j'^j.  9;  — ■  //  äbya  (statt DP.)"*  bairyeinte  yalsatn  .  .  fräyö  (sd.) '      ■  ■  bei
2514:-  g.  'a-  Pron,  ident.  'ich,  du,  er  selbst',  humata  'ta'  ..  aat  mam  narö  paskat  ya- nur  NS. :  yi  maibya  yaos  (sd.)  akmai  astu  g3„ie . .  "um  dieses  (deines)  guten  Denkens vakUta  mahyä  isfois  voha  eöihm  mananM  willen  .  ."  H.2.14''.        2)  substantivisch: ".  .  dem  verspreche   auch  ich  selber  das  ,  ^tai  ti  .  .  avayam  *danmaM  Y.  öS.  i  '>;  — beste  meines  Besitzes  durch  VM."  y.4''-   am  yasna  .  .  ''ta  patti    ava.jasa  .  .  aoi \Z;    —    ai   -3    vaocal  ahurö  mazda    ''da  zam  ".  .    um    dessentwülen  (was  hier  ge- sprach er  selbst,  ^/iM."  Y.sp.ö.  [schiebt)    komm  . ."  Yt. 5.132  (s.  i);   — zBed._s.  Gdn.  GIrPh.   '  52      Ich   '^'^^<=^'^^'- -faimat puir.lt  (sUtt  AS.)  Kimar^xsaf^u/ia dass  f.  as'  aus  einerrart.  idg.  'n  'selber  er-    ,    ,  ,   ,.,       .,•.,..'        ,     .  ,        „ wachsen  ist,  die  in  aUi;  (aus  'a-u-r,  wie , (sd-)    damit  (was  ich  dir  gebe)  such  ..' eJroiaus*jn-H-/°)steckl.Dochs.B(;M,GrGr.3244-    V.  1^.  14;  —  in  Kongruenz  mit  dem  Prae-
2531:y.  I ;  —  cayö  'te  raola  at»A)n  . .  yö  ava^a  '  vayrjanake  .  .  yat  °&o  kanjasante  paouru Sraoiayeite'^.2.^<j\  —  "taFsva  daxtnaih'a .gaonaAec'a  IsA.)  . .  ti.6^\  yi(7);  —  taotarf yöi  faiti  äya  z^mä  iavainti  "V.y.^^;  — ^.gstava  ..  ■""'oa'*  ..  N-tVi;  —  yetiAe  'oa "U  malsma  .  .  yaHbyö  .  .  framayattte  V. .  mazdayasnanqm  näirika  . .  *ham.raf^wa- (S'.ii;  —  'taisam  syao^nafiam  yöi  v»r>-  yeiti  "wes  von  den  M.  Frau  dort  . ."  N, sjbA'  masy.lka  V.  J5.2;  —  "tiitbyff  zao-  11;  —  ava'ia  ''QrtV.4.50;  —  taica  "'jaca >rabyö  ..  yämham  ..  N.  71;  —  ku^a  -tat  pü^nm    baraili    Y.iy^^if).  a)    mit
2533:*'te  *yffi'^  fracarinti  , .  aiialiqm  .  .  N.  ,paiqn  ,  ,  'na  ,  ,  triltm  k>hrp}m  hvan.- ^.  III)  In  folgenden  Fallen  brauchen  i  t/arwr« -f?rv«aii/V.  5. 13,  3)  'dann'  im wir  den  Sing,  mit  'ein'  (unbestimmter  Ar- !  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Plur.  artikellos  (vgl.  ^aisa- 111}  j  dessen',  einen  Zwischensatz  hinter  einem yesica  .  .  upairi  'l^m  iristim  .  .  Ajr^zy^lf '  SaU  mit  yai  einleitend:  y^i  ndii  nidan- yaia  .  ,  "und  wenn  (man)  .  .  auf  einem  sayilnte  —  ''ja  kl  alte  sünö  vä  .  .  fraja- Toten  ..  liegen  lässt  .  ."  V.5.61;  — yö\s,yi>  —  kä  Af  asU  äiaX.ö.^T,  —  yaii'a vastnm  upaiiharizatti  upatri  °t»m  tristem  |  vaoeäp  aiSö  m7  Aanqm  .  .  p3r>saKuAa  — "wenn  einer  ein  Gewandstück  auf  einem '  "'la  ae^a  y<J  kaine  hanqm  . .  p?nsaili  , .  — Toten  liegen  lässt"  V.Äaj;  —  bei  rela- 1 'ort  assa  yS  kaine  altahmat  puir.lt  *mi- tivisch  angeschlossenem  Nomen:  yat  "te^  manxlstti  —  '^Aapanta  .  .  vfri^qn  .  . yöi  tnazdayasna  . ,  taci.apaya  nasSum  fra-  [  V.  /J.  1 3  f. ;  —  yeii  mit  Aari^nm  baraili jasqn  "wenn  Mazday.  auf  einen  Leich-  -  "da  aisa  yö  afirinüyakö  adJityö.an- nam  in  fliessendem  Wasser  stossen"  V.  6.  Aarj^nin  (sd.)  iri^ät  —  ^'>para  A!  iri- 26;  <y.73,  7-36.  \sittt5  rais?m  cikayat  .,  V.7j.i6.
2554:nominale  Beifügung;  in  den  meisten  'tat  .  .yat  a:£'ar3t>m  Yt.  J9.48;  46;  — Fällen  entspricht  unser  bestimmter  Artikel  'te yä  spö.jataca  .  -  V.  7,  3;  —  Ue yöt  spatui (schwachtoniges  'der');  a)  adjektivisch:  V.ij.ai,  22,  43;  —  'taisqm yöi gius  sar?- caiti  'te  mi>fa  tava  yat  ahurahe  mazdat  oanqm  V,2.4i;  Ytj.9,  12;  —  'lat?hqm "wie  vielfach  sind  deine,  des  AhM.  Ver-  (GPm.)  yat  myazdanqm  N.  6j;  —  ku>a träge?"  V,4,2;  —  "te  daxma  .  .  aniarSt  (Stverz.)  ti  v>r>zyqn  He  yöi  masdayasna naSmät  iarürirva  V.5.51;  —  i-.a  Vam  ;  V.  5,  i  o  usw. ;  42,  J.18",  (/.3,  26,  9.49, (APm.)  aJsnt^m(s±)..paiti.bar,ltN.ioj;'—  *Vd.i8-20i;  —  't^m  (als  ASn.)  .\  yat °tayä  urvarayä  älan»irfs'V.8.i$;N.6j,'Vd.\spiln~'  .  .  X.ij.sS.  2)  auf  ein  Relati-
2559:;j.  I ;  —  cayö  'tt  raocii  atjhin  . .  yö  avaha  '  v(rf'ianahe  .  .  yat  '6a  han)asSnte  paouru Sraoeayeite\.2.y);  —  'tae^va  äaxmagh'a,gaonaAe^a  (sd.)  ..  N.f*j;  "/(?);  —  saetari frV  paiii  3ya  ztma  bavainii  V.7.54;  ■ — \gätava  .  .  *'oa'>  ,  ,  N.  A;  —  yetiie  '6a "le  malsma  .  .  yaiibyö  .  .  /rasnayiinte  V. ;  mazdayasnanam  näirika  . .  *hqm.raEä:wa- J'.ii;  —  'taiiam  syao^naiiqm  yöi  V3r>-  yeiti  "wes  von  den  M.  Frau  dort  . ."  N, ziiiti  masyjka  V. /j.  2;  —  "täibyö  zao-  11;  —  avaoa  °oa  'V.4-50;  —  taica  °üaca 'irJbyß  ..yäakqm..  N.  7/;  —  iu>a 'tat  pu>nm    baraiti    V.  15. 49(?).  a)    mit
2561:'''tt  *yöP^  fracarmii  . .  aitaSsqm  .  .  N.  patan  .  .  'oa  .  .  agtJm  k>hrp>m  hvar».- ij.  III)  In  folgenden  Fällen  brauchen  j  i/awjrjw  fo/vwuc/ V.  5. 1 3.  3)  'dann'  im mir  den  Sing,  mit  'ein'  (unbestimmter  Ar- 1  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Flur,  artikellos  {vgl,  ^aila-  III) '  dessen',  einen  Zwischensatz  hinter  einem jcsVJ  .  .  upairi  'tim  iristim  .  .  k>r>zyllt.  Satz  mit  ytzi  einleitend:  ye:i  mit  mdart- ya>a  .  .  "und  wenn  (man)  .  .  auf  einem  l  sayanfe  —  'ca  he  alte  sünS  vä  .  .  fraja- Toten  . .  liegen  lässt  .  ."  V.  5. 6 1 ;  —  /^ ,  JiW^  —  kä  hl  asti  Wia  V.  6".  47 ;  —  yesila vastnm  upaifharizaiti  upairi  ^tfm  iristtm  ^  vaocät  aSsö  nä  hanqm  .  .  p>r?sat3uha  — "wenn  einer  ein  Gewandstiick  auf  einem  .  '<,a  aSsa  y.J  kaine  hanqm  ..p^nsititi  . .  — Toten  liegen  lässt"  V.  ^'.23;  —  bei  rela-,°ö(J  a^ia  yä  kaine  aetakmut  puir-at  *mi- tivisch  angeschlossenem  Nomen:  yat  °te\mar?x^iliti  —  '^hat<anta  .  .  7>)r?zyqn  .  . yei  mazdayasna  . .  taH.apaya  nasHum  fra- '  V.  /5. 1 3  f ;  —  yai  nöii  har^'^nm  baraiti jasqn  "wenn  Mazday.  auf  einen  Leich-  —  °ofl  aila  yS  ap^rinlyükö  adaityo.at3- nam  in  fliessendem  Wasser  stossen"  V.  6. '  harsirim  (sd.)  iriiyäi  —  ^para  he  iri- 26;  ^.73,  7-36-  \Hntö  raSsim  cikayat  ..  V./j.iö.
2563:mazdayasnaA^V.iO.iz:  -    hä  'U  y^ska\^^^^^  I„f_  vorausweisend;  'tat  dim..daz. H^  ¥.5.48;  -yava^  'tea»h>m  F.^c;  j    ^  ^^j_j  _  _  ^^^^,,.  ^urahi mainyiui  V. \.iij.i-,-  —ga,ri,masoaaho'takeV.s.^    /  ^^  'dann,  alsdann':  ^rUum  bar^
2633:'vergewaltigen,  kränken':  ks'iwqmyim akurim  mazdam  "mazislayanti  isA.)  tnaotü V./i-.öi. aL  inMi,  'initak.  —  Pü. ;  tetümtan.  —  '5  Das  ^ n  ist  im  letzten  Grunde  praesentisch.  —
2761:Z  verlangen,  dass  er  (dem  Freund)  Schutz gewähre"  Y.  7/.  13,  a)  statt  des  praed. Akk.  ein  Adv.:  yimS  avai^a  ktrsnaot yaia  dim  Ual  ahurö  mazäi  "V.  tat  so, wie  es  AhM.  von  ihm  verlangte"  V.  2. 31.  4)  spez.  'zu  hören  verlangen,  hören wollen':  ^J  tsi  asä  yi  asäi gius  ia/.i  (sd.) mraot  is3ntl  tnä  tu  isi  vohB  manaaAl "was  ,  .  kund  getan  hat,  hören  wollen  sie dasdurchdeinenKji/."  Y.4Ö.9.  a)  ohne Ob],":  at  tä  vaxfyj  is?ntd  "ich  will  davon reden  zu  denen,  die  hören  wollen"  Y. _jo.i;  47-6*>;  — yalüä  asnat  yaila  anrät (sd)  isa:iä  Y.  45- 1-  5)  'Jemand  (Akk.) angehen,  sich  an  ihn  wenden,  ihn  bitten': ise  'i/wqm  aAura  mazda  ptrsst  '^wqm  . . Yt  12. 1 ;  —  *yas»  tat  *afivataiti  (sd.) paranlarfm  (sd.)  isöit  N./2;  —  vayö  .  . harn  istmmm  painyätte  ".  .  stellt  sich ein  bei  dem,  der  sich  (an  ihn)  wendet" Yt-/>S3;  —  al  yastim  nsii  na  is7mnS (inpass.Bcd.)9*Jj'i7/(sd.)Y.4ö.6.  a)  mit Inf.:  amslacit  .  .  avaiahe  isinli  masya- kanhs  "die  ^Ienschen  bitten  die  Am.  um Beistand"  Aog.  41.  6)  'Jemand  (Akk.) angehen  (in  feindlichem  Sinn),  angreifen, nachstellen';  avae^amai  ^iff  pantö  yim isfnli    mi^röjiruiS  Yt.  io.45.  7)    'er-
2768:mit  paiti  i)  'streben  nach  — ,  begeh- ren': a)  mit  Akk,:  tafca  yä  kasu.xratul ,  masyöjcrdkwqm  (sd.)  nöit  paitiSaiti  V.  7, I  59.  b)  mit  Gen.:  s.  AbsoL  a)  'sich befleissigen,  betätigen',  mit  Akk.'>:  paiti- sata  (2P.)  mazdayasna  sraoiahe  a/yeke '  yasmm  Y.  37. 13;  —  staota  yesnya  yaza- maide  .  .  dadräna  paitHäna  paitiima- .  r^mna  Y.  55. 6 ;  —  six/anlfm  sa/ayaitt^m paitisant^m  Vyt52,  *P- /?  (wo  °Ä«- ,ljm)'i^.  3)  'erfahren,  erleben':  iaia lUli  (sd.)  *paitUäma  '*>  frya  paiti  tanvi ,  Yt.  i7, 10.  a)  bes. 'zur  Vergeltung,  zum Dank  erfahren,  empfangen':  kä>:ä..kä%3 .  (sd.)  saidyäi  yS  I  paitisift  Y.44.2 ; — ya^a ahmya  amtsa  spmta  sraoläoa  aiyäoa paitisqn  . .  yasnqsca  vahmqsca  Y.  öb.6.
2769:mit  pairi  1)  'ringsum  absuchen,  auf- lesen': mazdayasna  aitihh  zimß  pairisa- yanta  (Opt.)  . .  varfsqmca  (als  Obj.)  ..yezi nsit  pairiianie  . .  astqmca  7-arpsqm:a  .  . V.  ö.  7f. 's\  z)  'herumsuchen  nach  — , aussuchen,  auslesen':  asstnanqm  xraoldva- nqm  .  .pairlstanqmY.i4.4'i'>;  A.3.5'^; —  uxtiitn  srlr>m  pairisttm  F.^^f'*'; V.J. 42  PüZ,;  —  pairi  daxma  aSlayqn  vi daxma    calsayqn   Y.S.z.  a)    mit    Dat
2798:auf  ein  relativisch  angeschlossenes  Nomen vorausweisend:  >o/<iW:4a/  sp3  urupis  fuai -so  spl  yS  urupis  .  ,  V.5.33;  —  ufa  vä nasus  raz'iwst  .  .  'sa  Jruxi  yä  ttasus  V. J.14;  5.27,  28,  7.1—4,  *.i6,  41',  9.40, 48;  —  ä^ravaium  yaoida^o  ,  .  'so  nä yö  yaoid.1>ryS  V.<).  37— 39;  40,  42,  If). 21,  Vd.iV.  10.  b)  substantivisch;  aStacTva daxmaisva . .  "sö  zl  asH  äaivanam  rapakö V.  7.55f.;  —  daxme  .  .  yat  °/a  pqsnu ra^'>a'.J/(sd-)  V.  7,49f.;  —  aisa  y5..aiwi.- >r}lti^ätus  (sd.)  *aivayaHi  -io  barfsmö.- sbrfiti  ratufris  N.  /Oj;  —  slaotaca  (sd.) yasnäica  . ,  yat  °sa  ahurake  mazda  "Pre is- lieder  .  .:  das  des  AAM."  Vr.if.ö;  6;  — jtal  ..  kmntiit  ava  hö  mirysüe  anJmltÖ si  'SÖ  , .  "wenn  er  . .  operiit  (und)  der foperirte)  stirbt,  dann  ist  er  disqualifizirt.." ^'■7-37;  —  iD  Kongraenz  mit  dem  Prae- diltkt;  cit  ai-at  vacö  äs  ,  J  baya  °h  3s ahunahe  vairyehe  "Was  war  das  für  ein Sprach  .  .?  Das  war  das  Stück  A/iV." 'W  i<).  I  —3,  o)  öfters  zugleich  auf  ein
2885:Vgl.  a,ii;nA.  und  ay.jA-,  —  »  Die  Zusammen- slellung  uni;'  und  jtni/n-  auch  Y.  3(j.  10. •  j.  aogazdas't^ma-  Adj.  'der  am  meisten Kraft  gibt':  tg  z^mö . . 'tpma  iarainti  "die geben  dem  Winter  am  meisten  Kraft"  V. 7.27;  26'.
2954:•  j.  aoman-"  Adj.  'helfend,  beistehend': tä  nS  . .  %räy?nle  .  .  'mtta  (IS.)  ahura mazda  sraoiaea  .  ,  ".  .  una  cum  juvante AhM.  et  Sr."  Ytij.146.
=== BRT madu ===
```


## [2026-09-07T15:50:43.765Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24195,24210p' BRT.txt; echo \"=== azda ===\"; grep -n \"azdä\\|azda-\\|'azdä\\|azdä  \" BRT.txt | head; echo \"=== find azd ===\"; grep -n \"azd\" BRT.txt | grep -i \"kund\\|Kunde\\|bekannt\" | head"
}
```


### [2026-09-07T15:50:43.855Z] TOOL RESULT

```
j.  *vT>»a»äi:  ■.  unter  »fa«^.  bei  .<W.  als  Arzte  praktiziren"  V.  7. 40;  38; —
•  j.  viman^-kara-  Adj.  'dem  Zweifel  ent-  Zf'-  ^^^'^J'"^  vlrnälasai  vlmälayänU
•  j.  vi-maraziäta-  Adj.  'der  am  meisten, besten  abwischt,  reinigt,  läutert'  (mit  Akk.): ahrnUktm  nqma  yal  amilanqm  spjntanqm . .  tat  vlspahe  atafOus  astvatS  anhvqm  asti 'hm  "unser  Name  ist  es  . .,  was  am  besten die. Seelentriebe  . .  läutert"  Yli,4;  z.
Superl.   lum  V.  mam-,    —    Pu.:    5n  i  amäk rtäfn  4.  ^n    i   karvüfi    €t-^  i  asiömand  an  i  ^
•  j.  vi-mad- :  'mäd-  m.  'Heilkundiger,  Arzt':
vasS  pasca^a  maadayasna  "waäajciV  (NP.) vXmmayanIa  (sd.)  V.  7, 40;  38'.
Vgl.  lat.  medstt,  mrdiau.  —  S.  vimaiaya-.  —
Pü. :  fa  ape  äimäyismk,
•  j.  vi-mä(y)-  Adj.'*  'ausrichtend,  be- sorgend', mit  Akk.;  yezica  vä  gaiha  'mä (ND.)'>  *katarasHt  *parayat .  .nmanspaüil gai%a  näirika  *paray3i  ^Rätrika  gaths "vis''^  nmänS.paitis  *parayät  "und  wenn beide  den  Hausstand  beso^en  (können),  so kann  jeder  von  beiden  ausgehen^';  (wenn) der  Hausherr  den  Hausstand  (besorgt),  soll die  Frau  ausgehen'',  (wenn)  die  Frau  den Hausstand  (besorgt),  soll  der  Hausherr ausgehen"  J>  N,  5.
Zum  V.  Biä(j')-.  —  Pü.:  hakar  har  3  ,.  Sgehän *iirvandaiJh  -  tuISn  i'Silai  sardänh  Itum üaiän  karian  -  katära  I  ape  e  äyit.  sösyäiu  gu/l  : pa  ehrpaiiitätt  iartan.  —  >>  Sehr  iweifelhaft, vll.  verstümmelt.  —  ')  Verderbt;  man  er- wartete einen  NS.  zu  vimä,  auch  nach  Pu. Vll.  'vlrnHJ  —  3)  NämL  a%aHrumin,  s. FüErl.
•  j.  vimäJa'ya-  den.  Praes.  31  'mederi'. 'die   Heilkunde  ausüben  an  — '  (Akk.)r
rs  *TJUmaia-  m. 'Heilkunde';  vgl.  vi- :  —  Pü. :  äzmäyUn.
*vi-mitay-"   'Zerstörung,    Vemich- j.   vlmanö.hya-' n.   'Zweifelsuchf   ^\^\^^t:-_  «f^iä%rs^-''vaHmca  yai  n5it  gsus'
'iarf  (iiS.)  vJspaflu  vTdaSvsMn  YL/5.S3. »)  Das  wird  sich  vermutlich  der  Verfertiger des  Unworts  dabei  gedacht  haben.
Landplage  von  Nisilya;  nissim  .  .  ahe paityilrmi  frilkfnnlai  aarS  matnyjd  .  . aypm^a  'htm  V.  /.  7.
KompE.  —  Ableit.  aus  'vt-manah-  Adj.  (S  2ßS.
=== azda ===
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in  . . yantä  aiibyö  dair?  (sd)  voka  as  manö  Y.  \  geraten,  dadurch  könnte  er  Schaden  neh- 34-&]  9.  2&  10,  45-ii  — yaisqm  ..  mazdä  \iata"  V,/_j.37;  —  ahmat  haca  /«>nj  (sd) ..  vatghö  vai'ja  alsqm  ..  Yt.i6.%; — ^J  sayiJ/A' Nik.  7;  *2; — yesi  tat  paiti  irisjati syao^anä  yä  vacatihä  yä  yasnJ  .  .  ae^qm  '  aiähal  hala  iyae>n!i7ar3za  (sd.)  .  ,  V./_?. töi..}hmä  pourutimäil  äasl?(sd.}Y.j4-^,''  38-  2)  vorausweisend;  i)  adjektivisch ■ —  yöi  *aite  . .  *gä'kä  nSit  *srävayänti  . .  I  auf  direkte  Rede  oder  Zitat:  vahiütsm  . . assqm  fyaohamm\ia'\  .  .  N, 25;  —  ySt  ..'igänii  ..  vir^zyat  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag-  *pt3  asahyä  mazdlY.4y.2;~aya  antar?.- £qm  nöit  aita^qm  ratufris  ..  N.52;  ^j\  uxti  (sd.) :  nöit  nS  mana  (usw.,  Y..^5.z) —  yahmät  kakmäicit  nalmaruim  vätS  ä'^rö  Y.ig.i$.  —  a)  mit  ergänzendem  Relativ: baoiolm  vibaraiti  (sd.)  ahmll  kahmäiHt  aya  aibigara  (LS.  als  Instr.)  aya  aibijary- nalmanqm..\.8.&o.  a)  Die  Beziehung  ta{d.^.)  yä  amfsanqm  sp^ntanqm..:  gave ist  ungenau:  ^yJ  räakaytn  (sd.)  sravaahä  rto5j/(usw.,Y._j5.4)  Vr.J2.i.  a)  substan- vahistät  iyadkanäl  mantärü  aeibyö  mazäi  tivisch  und  adjektivisch  auf  eine  erläuternde akä  (sd)  mraot  "qua  alienant  doc-  oder  ergänzende  nominale  Beifügung:  «7.5- trina  . .,  üs  .  ."  (statt  qui  ..  iis  ,  .)  Y.32.  yacä  i^agtuL  yäsat  ahyi  Virßzin3m..ahyä .. 1 2'*^  Anhang  zu  II  I  1,  2.     a)  An   ahurahya  uruasimai^A.)  mazda  Y.j2.i ;  2S.
2552:direkte Rede  oder  Zitat;  a)  adjektivisch:  kochersoll  man  niederschlagen,  den  Kessel usia  ahmni  (usw.,  Y.4J-I)  ■  ■  ciit  °taya  sollen  sie  .  .,  den  Aufbau  ,  ."  V,(V.73f.; paiti.vaca paityümraoti  Y,2/,4;  ■ —  kini  zl  — ■  "//  jrVr.ji./  y^aratu  °i^  vasträ  i-iiv än4  (usw.,  Y.4Ö.6)  .,  'te  zT  väcö  ..  mazdä  katu  V.J.  19;  —  asta-ja  hz  'te  mazäayasna frii mrao tY.yi.i^t-jy. 4.  i^üZ.;- — arrum'a  °t»m  iristam  nidanzaym  "da  sollen  (sie) „afrJnSmi  ..'tarn  mq^nm  fradaisayöH ..  die  J/l  (ihn)  den  Toten  .,"  V.  6'.46;_;.  18, Yti4-46;  benutzt  Y'l4-9.  b)  substan-  5.13,  14,  41,  61,  6.7,  51'.  7-i2i  t''-S,  10, tivisch,  in  Kongruenz  mit  dem  Praedikat:  9.39',  '4-7,  iö-z,  12,  A.3.^  falsVok.?); am?mca  .,  Sfrlnämi  ..  'taSca  tivlcö  yöi  —  'tanhqm  astqmca  var»sqm:a  .,\.h;-; ".  .  und  das  sind  die  Worte,  die  .  ."  Yl  —  'te  ratavö  .  .  'ta£sqm  ra>wam  'S.i'o 14-46'.  1)    vorausweisend    (öfters   -82;  Vd.  2;    —    'ts  ja'iä  V.A16-22S;
2791:3.6.  a)  mit  Angabe  des  Ziels  a.)  Akk.  i^«n/«(sd.)  Y.  70.  i.  Ilj  in  schwach- 'wohin?',  ß)ai/rundAkk.'zuwem?,gegen|deiktischem  Sinn  'dieser,  der,  er'  I)  auf wen?',  t)  patiy  und  Akk,  'gegen  wen?'; '  Zuvorgenanntes  —  oder  durch  den  Zu- dädarsis..avam  adam  fräilayam  arminam\s,a.mmenh^T\g  Angedeutetes  — ,  Zuvorge- Bh,2,7;  10,  _y.i4,  5.1;  —  iaram  pilrsam  sagtes  (Wort  oder  Satz)  zurückweisend /raisayam  abiy  ('zu')  vistäspatn  Bh.  j.  ,1)  auf  ein  Nomen  a)  adjektivisch:  ae>/i i;  —  vahyazdäta''  .  .  käram  /rifisaya*^nar0  „yeztca  vao(ät  "sö  nii  V./5.3;  5.41; Aara^uvatim  .  .  abiy  ('gegen')  aziam  Bh. !  —  Atlucä  *aitaya  narä  .  .  °sö  zt  narö  .  . 3-9i  3i9i  i'j    —  pasäva''  adam    karam\'^.4.ifii.;    —    kanqm  ..  'sa  hana  Y.lj.
2876:(7ö/iKfr(3PP.)V.;7.3.  a)  refl. 'sich  nennen, bezeichnen  als  — ,  heissen',  mit  praed.  Nom. : at  v3  staoil  aojJi^''  mazdä  anAScii  "euer Lobsänger,  o  M.,  will  ich  heissen  und sein"  Y.  jo.  1 1 ;  —  Tbwöi  staotaras^ä  .  . aogtmadascä^''  usftnaAiciJ (sd.)  vTsamada?c<l Y.  4/.$;    ziL    Aog.  7.  3)    'ansprechen,
3221:paiti.astica  (sd.)  '  yasnahe  *°öa''  *fSü^ '  mahrahe  N.  22 ;  —  |  ava^a  xsnasäMdÜ yäataiy  azdä  bavatiy  .."dataip ..  "so  wirst du  sie  kennen  lernen  und  es  wird  dir kund  werden  .  .  und  .  ,"  D.  G.i,;  —  tat T^annö  apataaif..°6a  hau  apayisrö  bvat ", ,  und  es  entstand  , ."  Yt  15.56;  N.;o;
3554:an  Gerechtigkeit,  von  AHM.:  ahurvm  Durch H.pIoL  «us  -M-"«"'''"'"''-.  Superl.  aus mazdqm  ..yS  aÜahe  'mS  Y.57.4;  I.\;  — |  'apayanta- Aiy,  V¥¥.  iam\. yam-;  yant{a-  ist fravaslm  avqm  yqtn  shurahe  mazdä  ,  ,  |  Komp.-Form  zn  ü.  yämi^aväi,  IF.  /,  70. asäi°mqmca'V.26.2.  2) 'der  tüchtigste,  •  j.  apayav-  'der  es  (einem  Geräusch wirksamste"*;  'maya  fiaiti  vacastaitü  "^loxtmA  der  Stimme)  gleichtun  kann' :  _j'£si  .. der  wirksamsten  Strophe"  Y.5Ä 8;  —  °m>m\nSii..aiivi.surum>aiti  apayät{sA.)ym  apsU ra^wqm  H.'i.y, —  °mahe  rakws  Vr.i?.  j  (NS.)'*  aa/  näil  apöis(NS.)'^  iiat*maoTaya 6;  —  ihm  ..at'^rapaitim  upayali  *°m?m^^  *vala  /ramanmnö  ratufris  ", .  wenn  er  es dahmsm  N.  is,  1  gleichtun  kann  (,  ist  er  r^\    wenn  er  es
3627:•  j.  apa-stütay-  f.  'das  Sichabgeloben, Abschwören':  yä  haca  damayat  mazda- yasnSii  'Biiis  "das  Abschwören  dei  mazd. Religion"  N.41.
3987:■  j.  aiwylnhana-  n.  i)  'Gürtel,  Gürtel- schnur'*>:  'n^m  r3  aiwya»hayamnS  'mm bO/ayarnnS  (sd.)  Yti.iT,  —  /rä  i! mazdä  harat  ..  'n^m  ..  vanuhim  daSnqm mäzdayasnlm  "dir  (dem  Haoma)  brachte M.  einen  Gürtel  . .,  (näml.)  die  gute mazday.  Religion"  Y.9. 26'*;  —  yat  alle yö  mazdayasnS  ap^rmäyBks  avi  hs  hapta ■na  /rajasäiti . .  °nö "'  paitis  h!  maiayai bU)yamanS  avi  hlnara pascaili  tamauhmti 'wenn  dem  jungen  Masday.  sieben  Jahre vergangen  sind,  soll  man  ihm  den  Gürtel um  die  Hüften  legen,  worauf  ihn  die Männer  (als  ihresgleichen)  achten"  Vd, 18;  20'; — jairyö  °nö  ißjyamanff  "vieitem legt  man  (dem  Toten)  die  Gürtelschnur um"  Vd. /23),  a)  von  der  Schnur,  mit der  die  Barvsmanzvreigt  in  Bündel  zusam- mengebunden werden"":  a^a  'na  N. ioS(?).  2)  'Gewand,  Kleid';  ^5  iama *°«o"  aiitryia^qyanii  "wenn  zwei  gleiche Kleider  anziehen"  N.p4(?);  — yaii  tarasca 'na  aipi.vancainii'^.gs^); — bilyS  ant?ma 'nH  "zweitens  (soll  man  dem  Toten  mit- geben) das  Untergewand"  Vd./i>3'.
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
=== find azd ===
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2761:Z  verlangen,  dass  er  (dem  Freund)  Schutz gewähre"  Y.  7/.  13,  a)  statt  des  praed. Akk.  ein  Adv.:  yimS  avai^a  ktrsnaot yaia  dim  Ual  ahurö  mazäi  "V.  tat  so, wie  es  AhM.  von  ihm  verlangte"  V.  2. 31.  4)  spez.  'zu  hören  verlangen,  hören wollen':  ^J  tsi  asä  yi  asäi gius  ia/.i  (sd.) mraot  is3ntl  tnä  tu  isi  vohB  manaaAl "was  ,  .  kund  getan  hat,  hören  wollen  sie dasdurchdeinenKji/."  Y.4Ö.9.  a)  ohne Ob],":  at  tä  vaxfyj  is?ntd  "ich  will  davon reden  zu  denen,  die  hören  wollen"  Y. _jo.i;  47-6*>;  — yalüä  asnat  yaila  anrät (sd)  isa:iä  Y.  45- 1-  5)  'Jemand  (Akk.) angehen,  sich  an  ihn  wenden,  ihn  bitten': ise  'i/wqm  aAura  mazda  ptrsst  '^wqm  . . Yt  12. 1 ;  —  *yas»  tat  *afivataiti  (sd.) paranlarfm  (sd.)  isöit  N./2;  —  vayö  .  . harn  istmmm  painyätte  ".  .  stellt  sich ein  bei  dem,  der  sich  (an  ihn)  wendet" Yt-/>S3;  —  al  yastim  nsii  na  is7mnS (inpass.Bcd.)9*Jj'i7/(sd.)Y.4ö.6.  a)  mit Inf.:  amslacit  .  .  avaiahe  isinli  masya- kanhs  "die  ^Ienschen  bitten  die  Am.  um Beistand"  Aog.  41.  6)  'Jemand  (Akk.) angehen  (in  feindlichem  Sinn),  angreifen, nachstellen';  avae^amai  ^iff  pantö  yim isfnli    mi^röjiruiS  Yt.  io.45.  7)    'er-
3221:paiti.astica  (sd.)  '  yasnahe  *°öa''  *fSü^ '  mahrahe  N.  22 ;  —  |  ava^a  xsnasäMdÜ yäataiy  azdä  bavatiy  .."dataip ..  "so  wirst du  sie  kennen  lernen  und  es  wird  dir kund  werden  .  .  und  .  ,"  D.  G.i,;  —  tat T^annö  apataaif..°6a  hau  apayisrö  bvat ", ,  und  es  entstand  , ."  Yt  15.56;  N.;o;
6045:•  g.,  p-  azdi  Adv.  'kund,  gewiss' :  Ikärahya naiy  a'  abavaf'  tya'' . .  ". .  wurde  es  dem Volk  nicht  kund,  dass  .  ."  Bh.  1. 10;  — \adataiy  a°  bavätiy  D.  Ö.4';  —  k!  mSi pasSus  k!  mS  nä  ^ratd  vis/3  anyS  asät "^wa^cä  mazdä  ahurä  a'  zütä  vahisläatcä manaiahs  "von  wem  sonst  weiss  ich es  gewiss,  dass  er  auf  meinen  Ruf  meine Tiere,  dass  er  mich  beschirmt,  als  von A.  und  von  dir,  o  MAA.,  und  voaVM.}"
6084:(als  Subj.)3>  ya  'sät  gSUs  taiä  (sd.)  mraet Y.4/i.g;'~  mq'ir^m  yim  haurvatatS  'iahyä amsntätaicä  (sd.)  Y.gi.d;  —  kä  "iswöi 'iä  (Vok.)  äka  (sd.)  arpdrfng  isyä  Y.48. 8;  —  daidl  'iä  (Volc)  tqm  ailm  vanhsui ayaptä  manaifhö  Y.  28. 7;  6;  —  yS  vi mazdii  ahurä  pairljasäi  .  .  maibyO  dävBi akvh..  Jj-iT/t/J  (sd.)  'iilihacaY.28.2;sj.i; —  yahä  'sät  hacä  gqm  vJäal  (sd.)  västryS Y.5:.5;  43.14;  —  a/M  ahmai  mazda  'iä a»haüT..  ys..  "und  dem  o  M.,  wird  es (das  Rind)  durch  A.  zu  teil  werden . ., der  .  ."  Y.50.  3;  —  yehya  mUi  'iät  haia vahistsm  . .  valdä  (sd.)  mazdä  Y.5J.  12; 27. 15;  —  yqm  da  . .  °säcä  cBü  raneibyä (sd.)  xinOiim  Y.^i.$;  —  yj  vlänaet  da- iipmcä  (sd.)  aäa'Samli  dangrä  mante  -ia (Instr.)  mazdä  ahurö  ".  .  durch  seinen kundigen  Berater  Aia,  er  MAh."  Y.  46. 17;  3^-  '3;  —  vahista  säsnanqm  (sd.) yqm  .  .  sästl  'sä  ahurJ  Y.  48.  3;  34.  12, 46.  2;  —  maxdä  *yä  da  'iä  vanhSui mayh  (sd.)  manauAs  Y.  4y.  a;  44- ij  — yezl  ahyä  °iä psi  mat  xiayehl  (sd.)  ..mazdä Y.44~  15;  —  at  ahyäi  'iä  mazdä  urvarS vaxiat{sA.)  Y.48. 6;  —  ätrJm  ..  aojSt»hvan- tsm  'iä  Y.34-4'i  —  ^^  adr'ärum  . .  dalnk saoiyantqm  yä  ^haJc?r?tll  'iäcTt  urväxsat (sd.)  y'34.\z;  —  ks  vä  'iä  äfraiiä  (sd.) Y.5/.  11;  44- S;  —  'sät  hacä..  vaidä (sd.)  yS  Im  dat  Y.  45.  4;  —  vidui  (sd.) 'iä  ySm  mazdqm  ahur?tn  Y.  4S-  8 ;  — va»kSui  'iä  Aaozq%7Väi  (sd.)  ä  mananhs Y.45.  9;  —  ärmatsii  kasilt  'sä  hutSntus (sd.)  Y.  49.  S;  —  tSm  vS  'sä  mShmaidt huiJiaxäim  (sd.)  Y.  46.  13;  —  mazdä ahurS  'iä  hui.haxä  ifmvatä  Y.  32.  2 ;  — mazdä  ..%wävqs..  at  ns  fryä  °iä  dazdyäi häkurmä  (sd.)  Y.  44.  i;  —  spmtaHyäiä tur?i.. yehya  urvä  'iä  haiaifl (sd.)  Y.34. 2 ;  44. 1  o,  46- 16;  —  neit  'iahyä  adlvyeintj (sd.)  *hacsna  Y.  44. 13;  —  'iä  vyqm  (sd.) yehyä  hihäui(sd.)  nä  spmtö  Y.4^.  7;  — ärmaitlm  ..hi%qm  (sd.)  'iahyä  Y. ^4- ro; 4ß.  16;  —  tqm  dainqm  .  .  yä  msi  gai'iih •iä  frädBit  haiSmnä\sA)  Y.  44. 10;  43. 6,  34.14,  44-to,  4o-i',  —  'iahyä..  sairJ (sd,)  'iahyä  Virszsm  Y.35.Z;  41.6;  — /praiaaiträi  urväzistqm  (sd.)  'iahyä  da. sarSm  Y.49-8;  5J.  3,  31. 2\;  —  'i^miä ^ fradat.gal%Jm  Y.  j;j.  1 1 ;  —  'ia  (Vok.) kal  %wä  dar}sänl  (sd.)  Y.2ÄS,  45.6,  ;^. 6;  —  humqsdrä  (sd.)  °ia  (Instr.)  yeiä  yä
7546:pih,  Sü.  (lu  Y.  Tfi):  ?ot/B*,  (iu  Y.  4^)-.  ma- hallatnatvam;  s.  noch  No.  1  ff.  —  ')  Fb.:  s. isvid-  No.  I.  —  ')  Pü.;  atazüniilh,  Sü. ;  ma- hattamaWam;  s.  No.  4,  —  »  Dh.  es  ist  alles göttliches  Oebot,  dass  das  Kind  mil  seinem t'elt  (Fleisch)  und  seiner  Milch  dem  Menschen zur  Nahrung  dienen  solle,  äzülöii  mq%rjm weist  darauf  als  auf  etwas  Bekanntes  hin. Pü. :  an  i  laaaünJkih  pa  mäusr  öhtmazd  *ö  *di täiitir  . .,  erl. :  an  mizä'i)  i  hac  mänsr  fdiläi  d ei  dahcnd;  s.  da*u  No.  5.  Vgl.  iSt.  Bthl. AF.  3.  53,  Gani  anders  JuSTl  PiJ.  SS.jg.— 4)  Pü.:  (iwzilitiMfA);  Sü.:  r^-ddÜA;  s.  No.  a. — i)  Der  Sali  ist  anakoluth;  Pü.erL:  hii  m/:d7i dakrnd;  s.  No.  3.  —  *J  l'üErt.  bezieht  die Stelle  also  auf  die  letzten  Dinge;  s.  No.  7.  ~ n  S.  No.  6.     Hier  richtig.
7951:airyamanäi:  'mal  ts  saahat  ahurö  mazdS: az3m  yS  ahurS  .  .  "folgendes  tu  dem Airy.  kund:  'AhM.  tut  dir  folgendes  kund: 'Ich  Ah.  .  .'"  V,  22.7f.;  13;  —  S  vaiftä <^urJ'mazdäh<^  °m<^  adam  akunavam: adam  hamataxsaiy  .  .  Bh.  J.  14;  —  'm<^ ly<^  manä  kartam  pasäva''  yd^il  . ..-  ia'- ba/iya^  ..  Bh.j.io;  15,  5.1;!!  —  in  Kon- gruenz mit  dem  Praedikat:  'me  acte  va^a ySi  htnti  bisämrüta:  ahyayäsä  '^.lo.y,  7.
8032:•  j.,  g.  iäud'  i  'Schuldforderung',  die  an Jemand  gestellt  wird:  yä  "ds  (NP.)  dadsnU didranqm  (sd.)  hacä  aSäunJ  yasla  .  . ^dr^gvüJibyS  yaiä  ta  aahin  Y.J/.14;  — mazdä  at  möi  vahistn  sraväsUil  y/aeianäcä viioäl  a  tu  voha  manaahä  asäcä  "dim stäls  "o  M.,  tu  mir  die  besten  Lehren und  Handlungen  kund,  sie,  o  VM.,  und, o  Aia,  des  Preises  Schuldforderung"  Y. 34.\%-'^;~  kuira  ta  fryB  ..  tä  -i/j  (NP.) ij  ratayS  (sd.)  bavan  Y.  65.9,
9008:24  genannten  Bergs,  anj^ebl.  idiidräsfi,  den man  für  idenlkch  hielt,  s.  vunStackelber<i WZKM.  12.  239. •  j.,  g.  ka'iH  Adv.  1)  "wie?,  in  welcher Weise':  "^il  '>,wä  mazda  xlnaoiiii  {%A^  V. 4O.  1;  —  °^ff  zaoia  gidh  /rasrävayätti N'.W;  Vyt.j/C?);  —  -^d  ffjv7w»»  ^/-a.- iri^j-S  Oa  ..  ii/aJasJ  "wie  ists  geschehen, dass  du  . .  gestorben,  wie  dass  du  .  ." K.  2.  16;  16;  —  °ä(7'>  ajfiirS  daxsära fiiasaysi  dlsil  "durch  welches  Zeichen "' willst  du  die  Tage  kund  machen  für  dte Befragung?"  Y,4j.  7".  a)  als  Indefini- tum,  a)  mit  vorausg.  ja^a  und  folg.  ca  "wie, in  welcher  Weise  auch  immer':  hvqm  anu usiim  zaos?mca  yaiia  "iiaca  hs  zaosö  "nach seinem  Willen  und  Gefallen,  wie  immer sein  Gefallen  war"  V.2. 11;  Yt/fj.82,  N. _J7.  b)  mit  Neg.  und  folg.  cina  'nicht irgendwie':  *'mä',a  ^'i^aäna  paitt.Jime  (.sä.) Vr.22.3.  2)  'wie  so?,  was  ist,  heissi das?,  was  hat  man  darunter  zu  verstehen? (die  Antwort  wird  mit  ya'^a  eingeleitet) °>a  alvö.gäimi  ra>a  '^ripai^m  "'wie  so eine  Schrittlänge?'    'Drei  Fuss'."   V.  5. 8;
9182:'dem  Gedächtnis  einprägen"';  vahists ahurö  uiazd-l  ahun^m  rairtm  Jrilmraoi vahistö  häind  karayat  "der  beste  AhM. hat  den  AhunaVairya  kund  getan,  der selbe  beste  hat  ihn  dem  (unserm  ?j  Gedächt- nis eingeprägt"  \.ig.\t,; — a'ia  tkalhm kärayäti  "in  dieser  Weise  prägt  er  (uns) ein    Dogma    ein"   Y.  :;o.  1.  a)    in    der
```


## [2026-09-07T15:50:56.971Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('HRN.txt',encoding='utf8',errors='replace').read()\nfor pat in ['39. bimär','990. mul','1003. mei']:\n    i=t.find(pat)\n    leaf=t.count('\\f',0,i)\n    print(pat,'-> leaf',leaf,'printed approx',leaf-21)\n    print(repr(t[i-200:i+900]))\n    print('-----')\nEOF"
}
```


### [2026-09-07T15:50:58.441Z] TOOL RESULT

```
39. bimär -> leaf 80 printed approx 59
"äl beruht auf Imäla.\nkurd. bal^ btel 'Spaten' (H.-Sch.); wa;r. bil, sar. bSil\n*Spaten'.\n58. blni 'Furcht'.\n[bhay^ ' erschrecken , sich fürchten (aw. bai/-y ai.\nbhay-), *bhänia7i- ; phlv. 6fm, blmkln,\n39. bimär 'krank^^ bimürJ.\naw. v% ■-\\;- v^war-) (vergl. vJ-merencalt^); phlv.\nvimär, vlmärlh (Men.), virnärinltan (y. 30, 6 nach\nDarmesteter's Correctur, Et. ir. II, 138).\nDie Etymologie ist gewiss falsch, da altes vi- im\nNeupersischen consequent zu gu- wird, und selbst bei\nAnnahme eines Ausnahmefalles (z. B. biüer^ No. 218)\ndas i völlig unerklärt bliebe. Dass das erste Glied\nnp. be- *ohne' sei, könnte man nach sar. LW. bhnar\n(d. i. bemar) vermuten; doch erhält man bei dieser\nAbleitung keinen guten Sinn. Bartholomae schlägt\nmir die Etymologie upai (s. No. 247) + mära-y also\n*am Tode' vor, aber dafür spricht nicht das phlv. v\n(oder auch w),\n30. bin *sehend', hin-em^ binä^ bmis,\nap. vainähiy Conj. (Venn) du siehst'; aw. vaenämi\n*ich sehe'; phlv. ven-am, ven(i)sn^ venäk^ venastan (päz.\nvm-), vergl. üben (vd. 19 (43)).\naf/. vm-am; oss. d. mmin, t. ünin (82); wa;^. §iyn.\nviti-am, sar. veln-am"
-----
990. mul -> leaf 243 printed approx 222
",\nn. mahisk 'Fliege, Mücke' (222) ; wa;^'- ^clcs, minj. moya,\nnp. meges ist wie die sämmtlichen anderen neu-\niranischen Worte ausser kurd. mis nicht direct mit\naw. ma/si-, ai. mdksa' (^2«) vereinbar.\n990. mul Wein'.\nai. fn^d[vtka- 'Weintraube' (Hübschmann, ZDM6.\n35, 133 Note 2).\nniele% 'Heuschrecke' (Öähn. I, 188 Vers 1059) s. meig\n(No. 1010).\n991. {\\)fnen *ich', men^ 'Eigenliebe, Übermut'.\nap. manä meiner (Gen. sg.); aw. mana; ksl. mene.\n991**^ {2)men 'ein Gewicht' ^), ar. LW. mann,\nskr. vergl. niäna- 'Maass (ganz allgemein), Maass-\nstab, Gewicht', dann auch ein bestimmtes Gewicht'.\nOder zu ai. mand- 'ein best. Gewicht (Gold)', gr. ^«v«,\nlat. mina, die semitische LW. sind, vergl. akkad. mana\n(Schrader, Sprachvergl. und Urgesch.- 206 folg., 252)?\n992. meniS, menisn (Wörterbücher) 'Sinn, Charakter,\nvergl. dus[men, rr^^DirilD (Is. 12, 1).\nap. vergl. 'Jlpiaj/LisvTjg (Plutarch); aw. manah-^ dm-\nmanah-; phlv. dusman, vergl. men(i)sn; ai. rndnas-,\nskr. durmanas.\n993. mör 'Ameise', mürce-),\ng. möirik 'schwarze Ameise'; Käs. V. möröund,\naw. maoiri- 'Ameise'; phlv. mör.\nLW. (?) kurd. mürt^ me"
-----
1003. mei -> leaf 246 printed approx 225
"aw. ma^dman-\nbedeutet nur 'Belegung (einer Hündin)'; phlv. mShmatt\nGast', m^hmänlh ; ai. vergl. mithds 'zusammen, gemein-\nschaftlich'.\nkurd. mevan 'Gast'; afy. nwlmana (Darmesteter);\nsar. LW. meimdn,\n1003. mei 'Wein, jüd.-pers., ^^O.\nIn np. mei, phlv. mai, vd. 5 (132), sind aw. madv-\n'Honig', ai. mädhu- süss; Honig, Meth' und aw. maSa-\n'Rauschtrank', ai. indda- das. zusammengefallen; vergl.\nksl. wedü 'Honig, Wein', nhd. Meth etc.\nHierher gehört auch np. meivlz {*meive2?) 'Rosine'\n(AM. 174 Zeile 5 und 1 v. u.), gewöhnlich mevlZy\ndas bereits de Goeje, Bibl. geogr. arab. IV, 359\n(Low, Aram. Pflanzennamen, S. 91) als persisch in\nAnspruch genommen hat. Die zweite Silbe ist un-\nklar. MtvTze^ mlvtzaj 'Convolvulus' ist vielleicht ein\nganz anderes Wort.\n1004. miyün 'Mitte; mitten, mittlerer, miyäne,\naw. maiöyqna- 'Mitte'; phlv. miyän; ai. vergl.\nmddhya- 'Mitte'; arm. mEj 'Mitte* (H. No. 199).\nkurd. LW. maiyän ; af /. manj, miyanj (Suffix echt) ;\noss. d. medäg, t. mJdäg (186) ; bei. LW. niyäm, niymfg,\nniyOmay (265) ; wa/. inalung, siyn. meSina, sar. madän\n'Mitte, wa/. tnalungüng, sar. maöänenj"
-----
```


## [2026-09-07T15:51:32.222Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD wemar ===\"; grep -n \"wēmār\\|wemar\\|wymʾl\" PHD.txt PHD_mackenzie.txt | head; echo \"=== PHD may ===\"; grep -n \"^may \\|^mad \\|^maδ\" PHD.txt | head; echo \"=== NYB ===\"; grep -n \"vēmār\\|wēmār\\|vimār\\|may \" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T15:51:32.295Z] TOOL RESULT

```
=== PHD wemar ===
PHD.txt:649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
PHD.txt:2370:illness wašt(ag)īh, wēmārih, xindagih, yask.
PHD.txt:5212:wigrad wigridan nerang n��rógómand nerog nilopal nirmadomand nirmad ncm, wem wūmār wēmārīh nēmasp wimand wimandómand wimandig wimustan nemag ncmroz ncmtan niság wisbed
PHD_mackenzie.txt:5316:wemar [wym)ll M w)'1n)r, N bemar] ill, sick.
PHD_mackenzie.txt:6849:illness wast(ag)ih, wemarih, xindagih,   India Hindugan.
=== PHD may ===
465:may [HS < A hmr ?; mdy | M my, № ~] wine.
2693:mad dēwānag.
4778:may appear written as * Q35
=== NYB ===
468:"p: api-š, ”pm’n' or (Ps.) *pmn: api- man, ’pt’n': api-tän, "p$^n! or (Ps.) *pšn: api-ščin: 1. and, introducing and coordi- nating sentences, e.g. andar-rón andar šut api-$ guft 1818-14; coordinating substan- tives if the second subst. is determined by an encl. pron., e. g. zantšn + Ahriman api-š visütakän 8819; also preceded by u: u api-t 6°, u api-š 7822, u api-sdn 79°, etc. — 2. introducing the apodosis after ka 94. 1025, 5225-27, 5418; after cigon 931; after an isolated w. having the character of a protasis: hämöden api-š hàn zan... ayyāt būt all this [to supply: engaging his attention], the remembrance of that woman came upon him 11'!-!*; — taking up the sentence again after a preceding digression: han zan u hàn fradand 1-8... api-man ne özat 1212-3. — Av. (82 sg.) aipi, OP apiy ‘moreover, further’, both encl. and often only emphasizing: OP düraiy apiy (and other spellings) ‘very far’; surviving in Milr -p(?), g. v. Along with it there must have existed a fully stressed form "dpi; id.-europ. "dpi (Gr postp. Ézt, prep. èni), whence the gen- uine Arm. eu ‘and’; it is the counterpart of Gr ču, Lat et (eti-am). This "dpi > Milr ap, in the sense of ‘and’ and in the apodosis, is normally used in the Sassa- nian official language as the bearer of encl. pronouns beginning the sentence, but in fact occasionally occurs alone, as in the Ps. (several instances, v. Gloss.); PR 231.14, 347. 404; PhlY 31! (intro- ducing the apodosis). Apparently it was counted among the archaisms which need- ed explanation, because it was included in the FrP (ch. 24). Paz. has preserved some remnants of the archaic form: awam = api-m SGV VII, 22, awama = api-mān ibd. VI, 47. X, 28. 35; Paz. AV, ed. Antiā, Päz. texts 35818; hawasq = api- gan SGV V, 62, etc.; the Paz. forms reg- ularly occurring may be shortened allegro forms of api-m ete., v.s.v. u. The equi- valents of api-m etc. given by the FrP are wm, wt, wš, which seem to coincide
477:apa-cand [pend] pt. pass. thrown away daru i jün-—-it thy trunk (body) whose life is thrown away, which is lifeless 267. — Pt. pass. of *apa-can- = apa-kan-, v. apakandan, NP aužand ‘thrown’ = afgand (BQ), whence a den. v. auzandidan (BQ, Steingass). Cf also NP bazandi ‘disap- pointment, helplessness, poverty’ (BQ, Steingass), abstr. of "bažand which may safely be derived from "aBa-žand < apa- cand ‘cast down’. V. also daru.
535:scindo). This act. is generally supplanted by the secondary caus. apasihčnitan from apa-sih-. — Note: — There is a synonymous vb. of uncertain origin which may have been influenced by the apa-sih- vbs.: Paz. awasdinidan SGV XI" = Phl *apa-sāyēnītan; "ps'dín! = apa-sāyišn Mx 15% (wanting in Cod. K); *pys’synytn' = apēsāhēnītan (the second -s- inverse spelling of h) DkM 175°. 351! (in the MS 13419. 27015), *pys'hšnyh = apesahiš- neh ibd. 180° (= MS 13816); to be de- rived from *apa-sü- *apa-säy- ‘to rub away’, cf s. v. apa-sütak ?
691:"a-sištak [""sštk] stupid, dull 8025. — Meaning according to Skr. v.: jadi-bhita; the Paz. reading: xasasta (West, Antiā), zasasta (Anklesaria), is obscure. As it stands it may be taken as a privativum + *sištak ‘instructed’, thus ‘untaught, uneducated’, from Av. (1574 sq.) säh-, pt. sišta-, sästa- ‘to learn, to teach’ (= Skr šās-, pt. sista-; šisya- *disciple'), but this vb. seems to be exclusively Gathic.
802:collected and the members of his family acquired — (when it) is lost and gone PT 16613-15; — common theological term ex- pressing the nothingness of Ahriman and the evil powers, especially from an escha- tological point of view: ~ -éh $ Ganäk menči DkM 852, v. also ~ -büteh; andar višuft- A hrimaneh, ~-druzéh), apasihit deveh u nést-paitiyarakéh in a state where Ahriman has been destroyed, the drugs defeated, the devs annihilated, and there are no adversaries DD 798-?; den. vb. avinnitan [>wbynytn']: opt. avinnēš DkM 83811; avinnitäreh DD 7514; avinnenitan, pass. avinnihistan ibd. 765-5; etc.]. — Paz. avin, Skr v. an-upakärin ‘doing no service, useless, fruitless’ (Mx), vikala ‘defective, impaired’ (SGV). FrP ch. 25 gives full evidence as to sense and etymology of this w.: "wbyn'. ’yen. L'YT'.nyst'. heš. heyš (var. hes!, ?zy$), Paz. óbin (K öbin). ēzin (var. aizin, Arab letters ’zyn, ’yzn) rwid nist aziš (var. ajiš), the lemma being: ^wbyn': écin (LYT' =) nast haciš; com- mentary: — l. &in < *atva-cina ‘even one thing’, with neg. ‘no one thing, nothing at all’: Av. (594) -cina encl. emphasizing part. in neg. sentences, (595) cina- ‘whoever’, (595, 762) dväcina ‘two men whoever they may be’, (24) aēvā- cina in obscure context ;. 2. L“YT' glossed by nēst, and ambiguous keš elucidated; 3. the lemma says: *wbyn' means: ‘no one thing comes from it, there is no gain from it’. The reading is almost self-evi- dent: a-vinn <  "a-vinda- from Av. (1318 sqq.) *vaéd- ‘to find, to acquire, to share, to gain’, thus ‘not gaining’; also representing Av. (348) o-vindan- ‘left without any share' (of the food, of dogs Vd. 1378). As to the assimilation of -nd- > -nn-, common in SW, cf MPrs bn = bann < band; BP apa-sinn- (v. s. v. apa- sistan), nivinn- < ni-vind- (g. v.). — This etymology was already given in HP II, and I maintain it firmly. The most un- happy idea of Geiger (WZKM XL, 107), taking ^wbyn as an Aram. ideogr. and
1220:dāštan [d'štn'] dār- [YHSNN-; d'1- 217. 281. 10014. 10279], imp. sg. with encl. pron. där:om [YHSNN-m] 6t; opt. 2nd p. sg. dārēš 41!?; pt. dašt = pret. pass. 3d p. sg., construed as an act. form 495-5; to keep, to hold, to sustain, to maintain, to have, 8?! and passim; — with an adj. as a complement of the obj.: Sahpuhr kanicak āžarmīk u garamik däst Š. kept the girl honoured and respected 163-4; 225 ete. passim; the complement some- times comes near to an adv., e. g. véh ~ to keep, handle a th. well 5026-27, and may be replaced by an adv.: én zan garämikihä ddr 1024; 6415; — with an obj. and pat + an adj.: to consider a p. or a th. to be ...: pat margaržān ~ to consider a p. guilty of death 1014-19; 6398-9, 8017, 839-19; pat azateh (cas. obl. sg.) där-om! consider me as a free (wom- an) — release me (from slavery)! 64, v. s. v. Gzat; — pat & ~ ku to be of the opinion that, to think, imagine that 2525, 982-3, 3227 sq. 5012-13, ef NP pindāštan < *pa(t) én daštan; pat ce dārēh how do you regard (the case mentioned in the preceding kū- clause)? 105-$; pat depahr, pat nihän
1259:*Dēnē [dyny] n. pr. P1:7..— Reading not quite certain. It may be the abbre- viation of one of the numerous compound names beginning with Dén (Dén-Ohur- mazd, Den-Sähpuhr, Dēn-ayyār, Den-dät etc., v. Justi, NB).
1529:(someone) to read P2:4; — 3. by an inf. which may a) precede ~: 1171. 3726-27 etc.; b) be put after ~: 923, 101? ete.; in this case ~ must immediately precede the inf., separating it from its obj., adjuncts and preverbs: äkäh framäi kartan 11”; šahristān-ē ... framüt kartan 1278-2? and passim (but framüt . . . pairäyenitan with a long series of dir. objects between 120” sqq.); bé nisastan: be framäyet nišastan 141%; apar kartan: pat dar apar jramāyēm kartan 208 ; andar kartan : andar framit kar- tan 11423, and the like; similar construction of apäyet (g. v.); e) be introduced by ki, through contamination with no. 2: fra- mit ku ... kartan 121719; 4518; (+220). — Av. (1166) fra-mäy- ; MPrth frm’dn frm’y-, MPrs prm’dn prm’y-; Paz. far-midan, farmäyastan farmä-; NP farmudan far- may-.
1725:*guhrāyēnītan [gwh'Pynytn'] to awake, to rouse a p. from sleep 321’. — Caus. of guhräy- < gufräy-, cf gwpl’dt' = gufräyet rendering Av. (511) frāyrāyrāyetti ‘rouses (him) from sleep’ Vd. 1823 and Nir. Waag p. 46 (= Sanj. fol. 275), gwpl'dšnyh (this is the correct reading) = gufrayisneh rendering fräyräraye (inf. of the same vb.), Nir. ibd; frac gufradyisnéh rendering Av. (977) fra-yrāti- ‘the awakening’. gu-fray- may be explained from vi + frayrāyrāy-, from Av. (511) !gar- : fra-yrayräy- > frayräräy (dissimilation of y) > frayräy (first haplology) > fräräy- > fräy- -(se- cond haplology); vifrdy- > gufräy- > guhräy-; the spelling gwh’r- is analogous to spellings such as gwh?l = göhr, swh’l suxr, perhaps denoting a glide vowel: guher-, göher, sux*r. — V. also vi-gräs-.
1779:hakar [HT], with enel. pron. HT-m = hakar-am ete., if: 1. conditional conj.; apodosis introduced by adak, sometimes by pas (24°) or u pas (27°), or without particle; it may take a nominal clause:
1800:*hamāxakēh [hm’hkyh} comradeship, companionship 5718, 6114-23, — Abstr. of *hamāzak (no Paz. reading known to me) which renders Av. (1744) haxay- ‘friend, companion’, FrO XXIV. I derive *hamā- xak from *hama-haxa-ka-. MPrth Pm- zwnd ‘unanimous’ (S, List 83, Sogd. 54) may go back to *hama-haxa-vant- (and thus be separated from MPrs h’mwx in the same sense, v. BBB and List 83).
1865:hàn [ZK], with emphasizing particle hän-ic [ZK-c; on ZK-p, ZK-py 5113-15 v.s. v.-p], dem. pron., sg. and pl., refer- ring to what is distant from the speaker, or already mentioned; independent, or adj. placed before its headw. (exception: viyük han HajB: 9); the adj. han may be replaced by hàn t, properly ‘that which is’: hàn + "sih that *splendour 125-26; han i Vidrafš + yātūk 25%; han à yamak 571%; esp. if -c is added to it: hün-ic i dar-band 241; hān-ic i Hutēs
1957:hat [HWH-t'] 1. pres. subju. 3d p. sg. of h-: andar gāv pém guméxt ~ so that it may be mixed with the milk of the cows 423-4; modal: would seem to be 38°. — 2. ‘it shall be’ used as an adv. in order to introduce a quotation from a sacred text = to wit, namely: cigön den gobči ~ 388. 4326, 4415, 505; 1113. — 3. perf. pass. cigön niin kušt hat 981. A parallel form of hät; Paz. hat, Skr v. syat (SGV). — V. Grammar 7.7. l
2101:i [Prs inscr., Ps.. ZY; BP contracted to a ligature coinciding with y: ZY, except when connected with an encl. pron.: ZY- m = i-m, ZY -t = i-t, ZY -š = 4-6, ZY-m’n' = i-mān, ZY-Vn' = i-tün, ZV šin! +-šān] A. a) relative pron., may be used as the subj. or the dir. obj. of its clause: hān i ó man mat 12°; én fradand + andar aškamb därem 1013; has no cas. obl; instead it takes an encl. pron. referring to the correlate: hàn ... i- dmocišn he whose education 80" (rare, commonly k&-$); cannot be governed by a prep.; instead the prep. is placed ?n the clause and governs a pron. referring to the corre- late: *sīh-ē (v. ?sih) ... $ hac han nēva- koktar butan ne šāyist ‘splendor quo nullus pulchrior esse poterat’, a *splend- our that was the most beautiful. ever existent 717-18; or the prep. is changed into an adv. connected with the vb. of the clause: méx i patiš bandēnd 300 xirs poles on which they fasten 300 *rings 2026 (bastan construed with pat; patiš the adv. of pat, v.s.v. patiš); in such cases ke is more usual. — b) conj.: &on l . $ so ... that 2016-17, 3226-27; cand i as much as 3119; 4 ka, hān 4 ka, v. ka; —i-šān 4, 1-8 $ when, as soon as 5811,
2135:ka [MT], with encl. ’MT-m = ’MT-t = ka-t, °MT-š = ka-š ete.: 'MT-e = ka-c: A. conj. when, as, while; because; though, whilst; if; that. 1. temporal: standard type of period referring to the past: Pāpak ka-š hàn saxtan āšnūt kas fréstit by P. when by him this word was heard a man was sent = when P. heard this he sent a man 21!; passim; if con- taining an encl. pron. the apodosis is introduced a) by adak + encl., e. g. api-n ka én tigr vist adak-in . . . vist and when We shot this arrow, We shot it ... HajB: 4-6; 545-5; — b) by api- + encl., e. g. ka hac star frac būt api-š ... guft kū then he said 60?*; — c) by the independent forms of the enclitics: am, at, aš, aman, atān, ašān: hän étén amavandeh + ka zivandak bit hom am bit that great vigour which was mine when I was alive 345-6; ka giyāk-ē päh i gospandan vēnēnd ašān avd sahét when they see somewhere a flock of sheep it will seem astonishing to them 9724-25; — the apodosis may be introduced by adak alone (v. this w.); by pas (914-*); by andar han in the meantime (561°); — ka ... apāc àyet aš Kat-Xosroi bē 6 patirak āyēt ka pat vài našast ēstēt when he comes back he will
2171:kamak 1. will, wish, desire (= kam): 6 ~ rasét (imp.) may you attain, (the ful- filment of) your Royal Pleasure! 107; brihenisn u spahr u ~ i yazdān the predestination, Heaven, and the will of the gods 69°; pat ~ as teng as ever you wish 5915; ke Būšāsp ~ nē varzét he who does not (work the will of =) addict himself to Drowsiness 841%; ~ dátan 6 to direct one's will towards
2174:5623.25; „-hanjäm, v. hanjam; — love: mart u zan [virtual dat.] évak apak dit ~ bavēt man and woman wil be in love with each other 10474-%, — 2, used as an impersonal vb.: to be willing, to want, to wish: a) with ku: api-män ~ ka či fresteh and our will is that you should send him 35-%; b) with a v. n. in -išn placed after ~; if the subj. is a pron. it is placed before ~ as an encl. (-m, -t, ete.); if it is a subst. it is placed after ~ and may or may not be antici- pated by an encl. before ~: cé-§ ~ tó rād Ohurmazd apar-ästisneh 4 en den, api-sdn ~ amahraspandān, api-š ~ to rād apārīk yazdān for O. wants you to take care of this Religion, and the Amah- raspands want it, and the other gods, too, want you to do it 5919-31; miyan van ku ~ apar-barišn Pourusäsp the middle of the tree up which P. wanted to climb 415. — 3. adj., as the second element of a bahuvrihi, -ak being a secon- dary suff. of derivation (cf -sälak: sal): pus-~ having love for her son, loving her son 4821, 497.21, 5011; Ohurmazd is névakéh-— having his will directed to- wards good things, Ahriman is anadkéh--~ having his will directed towards evil 772824, ahldyéh-~-tar (Zartuxšt) whose will is most [of all beings] directed to- wards Righteousness 4528.
2237:ikartan [krtn'; klty; ‘BYDWN-t'] kun- [ BYDWN-;forms v. I, 179; pres. 3d p.sg. kwnd: read kund] to make, to do, to per- form, to exercise, to commit, to cause, to bring about; to manufacture, to construct (hac ‘of’ a material); — forms active deriva- tive vbs. a) from v.ns. in -išn, e.g. āsāyišn ^ to repose, azbäyisn ~ to invoke; gar- zišn, īzišn, koxšišn, nikērišn, pursišn, za- nisn ete.ete. ~ ; b) from other nouns: čfrin, amoxtareh, appar, hampursakeh, tak, varz ete. ete. —, v. the resp. ws.; — with a pred. adj., e.g. 73. 34" etc.; girt kart = girt kartak (g. v.); vat-kart v. vat; or a pred. subst., e.g. api-$ ... bitaxš kunom 2510-11; . with kart as its cognate obj. P2:6-7. 8 [read (TB =) nev kart" kunän that I may do good deeds]. — With prev.: andar 6 kar ~, v. kar; api-§ Mānušcihr andar 6 Patisz"argar kart he brought M. (as a captive) to P. 1164-5, cf Bd A p. 2315-5; — apüc ~ to repel 42*3 gl.; to reflect 1125; — pat ddr apar ~ to crucify a p. 208; — bé ~ to remove 65; — berön asmän kunst he wil turn them out of heaven 10318; — frāc ~ to send forth 161!5; to bring forth, to produce 48?9; to attempt 81?!. — NB: man kart HWH-wm 374-5 for man kart-om by me it was done, v.s. v. h- and -m. — *BYDWN.x,ot' = kunät 5314, cf BY- DWN-x,-yd = 2nd p.sg.kunēKnS VII, 11. — Av. (444 sqq.) tkar-, pres.ko ranu-; OP kar- kunav-; MPrth kyrdn kr-; MPrs kyrdn kwn-; Paz. NP kardan kun-; cf s.v. hangirtikeh.
2256:2kas [’YS], with the indef. art. kas-ē PYS-+1], with the encl. -c: kas-ic PYS-c], cas. obl. kasč-c [’YS-yc] a man, a person, somebody, anybody; with neg. nobody: pat —-éc ~ ... mā to no one at all (whoever it may be) 6616; hàn ~ ké that one who 416, 95; har ~ everyone 7016 ete. ; har —-& 100%. (subj.). 10374; harvén ~ 6419; har vat ~ ... né no evil man 619-9; bé man an ~ ... nē no one except me 342; héc ~ ... nē nobody 7175-9 ete.; vas ~ many people 151%; — pl. some men, people, pl. cas. obl. —-än 6922.26. 8225, 8423, 853. — Av. (424 sq.) kascit, whence in SW *kassit > Milr kas; OP kasciy is NW, but has no continuation in later stages (it would have resulted in *kaš). V. Tedesco, Dial. 209sg. — Cf ciš, "kaš, pas.
2268:katārcihē [kt'lehy] anyone, whatever or whoever it may be 6716. 100?, — Not kt?le?y as in the Index. Paz. kadärcihe < katār-ci he (opt.) ‘whoever it may be’. From Av. (433 sg.) katära- ‘which (of two) ?’; katarascit is indef.: ‘both, either’.
```


## [2026-09-07T15:51:33.247Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD mwd ===\"; grep -n \"mwd\" SOD_pages.txt | head -20; echo; echo \"=== SYN 307 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==331' SYN.txt | head -60"
}
```


### [2026-09-07T15:51:34.759Z] TOOL RESULT

```
=== SOD mwd ===
9567:                                                                            =^»wt©t^var-; Parth. hmwd
19535:     mu6 (mwd) *=»m5w                                              Hen. Magi. 138.27, 135f
19538:       p2l6, 2aV2                                                  muhr-5ip ©*mwdr\ Parth. ©ob. -yy

=== SYN 307 ===
dation Chennai and eGangotri
Y; BODILY FUNCTIONS AND CONDITIONS 291
or ‘carcass’, while ¢élo renders capa ‘body’, whether living or dead), Pol., Russ. trup ‘corpse’ (SCr., Boh. trup ‘trunk, block’, ete.) : ChSl. trupli ‘hol- low’, Lith. trupéti ‘crumble’, Grk. zpi- méw ‘bore’,etc. Walde-P. 1.732. Briick- ner 578.
SCr., Bulg. leg (likewise Rum. les, Alb. lesh), fr. Turk. le¥ ‘corpse, carcass’. Berneker 702. Lokotsch 1306.
6. Skt. cava-, prob. : ¢iu- ‘swell’, as orig. ‘swollen mass, body’.
Av. nasu- : Grk. vexpés, etc., above, 1.
4.78 BURY (the Dead) Goth. ga-, us-filhan, gana- Lith. (pa)laidoti, pakasti
Ge ee 0&Be wistron Lett. aprakt, apbedit
Tat. sepelire (humare) ON  jarda, heygja, grefta,  ChSl. pogreti Me It. __sollerrare, seppellire grafa SCr.  pokopati, sahraniti Tr, __enterrer, ensevelir Dan. begrave, jorde Boh. pochovati, pohrbitr
Sp. __ enterrar, sepultar Sw. begrava, jorda Pol. pochowaé, pogrzebaé Rum. inmorminta, ingropa OE byr(i)gan Russ. (s)choronit’, pogrebat’ Ir. adnaicim ME burie, enter Skt. _ni-khan-
Nir. cuirim, adhlacaim NE bury, inter Av. (nasu-spaya- ‘burial’) W.  claddu, daearu Du. begraven
Br.  douara, bezia : OHG bigraban, (bi)felahan
MHG._ begraben, bevelhen NHG _begraben, beerdigen, bestatten
In the disposal of the dead both burial (inhumation) and cremation have been practiced, either at different periods or contemporaneously, among nearly all the peoples of IE speech. The Zoroastri- an custom, attested also for some other Tranian peoples, was the exposure of the aoe to be devoured by dogs and vul- cp Cf. Schrader, Reallexicon s.v. cn ee Even where cremation was fs ced this was generally followed by
a of the bones or ashes. ee was denoted by the usual veKpobs § burn’, as Grk. xalw (kalew
‘n Hom.), Lat. drere (XII Tab. ig im urbe ne sepelito fecunte (the technical term
» Whence NE cremate, etc.),
Skt. dah- (RV 10.15.14 ye agnidagdha ye anagnidagdha ‘those who are and those who are not burned with fire’; AV 18.2.34 ye nikhata ... . ye dagdha ‘those who are buried and those who are burned’), ws- (hence uposana- ‘crema- tion’).
The words listed here are those for ‘bury’—with the following reservations. Grk. 64rrw, while probably originally ‘bury’ and appropriate to the actual burial of Mycenaean times, is in Homer ‘honor with funeral rites’, which were normally those of cremation, and only rarely specifically ‘bury’ (as Od. 11.52 éréOarro bro xOovds), later usually ‘bury’, but cf. also up! @arrev ‘cremate’. NHG bestaiten, though commonly felt
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
en
Digitized by Arya Samaj Foundation Chennai and eGangotri
292 SELECTED INDO-EUROPEAN SYNONYMS
as ‘bury with ceremony’, is used in scien- tific writings as a convenient general term to cover burial, cremation, etc. Many of the words for ‘bury’ are from those for ‘dig’ (8.22), in part differen- tiated from the latter by prepositional compounds with perfective sens
```


## [2026-09-07T15:51:45.023Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN physician ===\"; grep -n \"PHYSICIAN\\|4.44\" SYN.txt | head; echo \"=== SOD mδw ===\"; grep -n \"m6w\\|mδw\\|m8w\" SOD_pages.txt | head -20"
}
```


### [2026-09-07T15:51:45.113Z] TOOL RESULT

```
=== SYN physician ===
31:LPPPIOV4$94-4050565444 44455555 3 Geqy bis: REE bh puwNUl bUOLL 4 wtkbieesisaeviescibasein een
5268:There is frequent shift of application between words for parts of the body that are adjacent, of similar relative position, associated in function, or through common figurative uses with reference to the emotions. So between ‘head’—‘horn’ (from ‘summit’); ‘head’— ‘skull’—‘brain’; ‘mouth’—‘jaw’, ‘throat’, ‘cheek’, ‘chin’, ‘lip’; ‘neck’—‘throat’; ‘shoulder’—‘shoulderblade’—back’—“‘arm’ ; ‘hand’—‘arm’; ‘foot’—‘leg’; ‘finger’—‘toe’ ; ‘belly’—‘womb’; ‘breast’ as front of the chest—‘woman’s breasts’; ‘heart’ from ‘soul’ (Rum. inimd, 4.44) or ‘bowels’ (W. calon, 4.44).
6463:4.44 HEART
6542:Br. poullkalon, poulgalon (cf. Vallée s.v. estomac), epd. of poull ‘hole, hollow’ and kalon ‘heart’ (4.44).
7899:4.87 PHYSICIAN
13968:Fr. heurter ‘strike’, esp. ‘hit, knock’, deriv. of a Gmc. noun = ON hritr ‘ram’, hence orig. like NE vb. ram. REW 4244.
19193:Goth. arniba adv. (renders dc¢adés Mk. 14.44) : ON ern ‘brisk, vigorous’, OE eornost ‘zeal, earnestness’, etc. perh. fr. the root in Skt. roti, rnvati ‘arises, moves’, Grk. dpyipe ‘arouse, move’, etc. Walde-P. 1.138. Feist 58.
19216:6. ChSl. stichranino adv. (renders aopadras Mk. 14.44) : (st)chraniti ‘save, preserve’ (11.24).
22088:simple kreiz is used as prefix ‘mid~’, e g it kreizdeiz ‘midi’, kreiznoz ‘minuit’, Stan ‘ 3. Lith. vidurinis, Lett. vidéjs fp ib Lith., Lett. vidus ‘middle, inner part? for this prob. : Skt. vidhu- ‘solitary, He bt lated’, Lat. di-videre ‘separate, divide’ Walde-P. 1.239. st 4. SCr. srednij, Boh. st¥ednt, Po), ® Sredni, Russ. srednij, fr. the sbs. Ch§], . sréda, etc. ‘middle’: ChSl.  sriidice ‘heart’, etc. (4.44). Briickner 534, uN pot
24297:CHAPTER 14 TIME! 14.43 ae 14.44 ay 14.45 YounG 14.46 OLD 14.47 Barty (adv.) 14.48 Late (adv.) 14.49 Now 14.51 14.52
=== SOD mδw ===
15302:     ©Idg. =»m6w, m8>k
18812:         maSe =»m8w                                VL^'lT*               EGSii 153; GMS 136, 1109
```


## [2026-09-07T15:51:48.806Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7899,7960p' SYN.txt; echo \"==== leaf of 4.87 ====\"; python3 -c \"\nt=open('SYN.txt',encoding='utf8',errors='replace').read()\ni=t.find('4.87 PHYSICIAN')\nprint('leaf',t.count(chr(12),0,i))\n\""
}
```


### [2026-09-07T15:51:50.286Z] TOOL RESULT

```
4.87 PHYSICIAN
Grk. tarpés Goth. lékeis Lith. gydytojas
NG ytarpés ON leknir Lett.  drsts
Lat. medicus Dan. lage ChSl. — baltji, vratt, lékart It. medico Sw. lakare SCr. lijetnik, lijekar Fr. médecin OE lace Z Boh.  lékar
Sp. médico ME leche, fisicien Pol. lekarz
Rum. medic NE physician, doctor Russ. vraé, lekar!
Ir. liaig (midach) Du. arls Skt. bhisaj-, vaidya-, Nir. = liaigh OHG § lachi, arzat cikitsaka- W. meddyg MHG arz(e)t Av. vimad-
Br. medesin NHG arzt
The majority of the words for ‘physi- cian’ are connected with the verbs for ‘cure’, discussed in 4.86. Some are words for ‘teacher’ or ‘learned person’ used in specialized sense. Several, ac- cording to their probable etymological connections (cf. below, 3, on Ir. laig, ete., and 6 on ChSl. baltji and vract), reflect the primitive antecedent of the physician, the ‘conjurer’ or ‘medicine man’. Cf. also under ‘medicine’ (4.88), and Schrader, Reallex. 1.58 f.
1. Grk. tarpés, Hom. and dial. tarip : tdouar ‘cure’ (4.86).
2. Lat. medicus (> It. medico, OFr. mie, miege; and learned borrowings Sp. médico, Rum. medic; Fr. médecin, back formation to médecine ‘medicine’, 4.88), also poet. and late Lat. medéns pple. : medéri ‘cure’ (4.86).
3. Ir. liaig, NIr. liaigh, prob. fr. *lép-agi- ‘conjurer’ : W. llef ‘voice’, MW llefein ‘cry’, Br. lefiv ‘groan’, Skt. lap- ‘chatter, talk, whisper’, etc. Hence prob. (though also disputed) the Gmc.
group, Goth. lékezs, OE l@ce (> ODan. leke, Dan. lage), MI leche (NE leech arch.), OHG ldchi, and (re-formed after the verbs) ON leknir, Sw. ldkare; fr. Gmc. the Slavic group, late ChSl. lékari, SCr. lijekar (reformed lijeénik), Boh. léka7, Pol. lekarz, Russ. lekar’. Walde-P. 2.429. Walk-Torp 673. Feist 329. Pedersen 1.311. Stokes 251. Berneker 710. Otherwise for Gme. group (: Grk. Aeyw ‘speak’, etc.) Holthausen, If 39.71, Stender-Petersen 330.
W. meddyg, Br. mezec (obs.), also (rare) Ir. midach, fr. Lat. medicus (above, 2). Pedersen 1.239.
Br. medesin fr. Fr. médecin.
4. Goth. lékeis, etc., above, 3.
ME fisicien, NE physician (also ME and earlier NE ‘student of physics’) fr. OFr. fisicien ‘médecin’ (Godefroi), deriv. of Lat. physica ‘physics’ (fr. Grk. duatxds ‘natural’), but which came to be used extensively in medieval Latin for medi- cina (Du Cange). NED s.v.
NE doctor, the usual term in common
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
(0) ia j ial sense in MB in the specia se ae Doctur of Phestke), fr. Geet. doctor ‘teacher’. Simi- i found more or less re
languages : It. « all the Juropean ie ne docteur, etc., Dan., Sw., NHG ek dials.) doktor (and hence
70 ; h. eee Lett. dakteris), and in the en Slavic languages. mOHG arzat, MHG arzet, arat, NHG
‘ts, fr. late Lat. {LG arste, Du. arts, car Grk. are tarps (both frequent sls inserr.) ‘chief, (and hence court) ohysiian’ Weigand-H. 1.90. Kluge- G. 25. 5, Lith. gydytojas (4.86). Lett. arsts, (above, 4). 6, ChSI. balzjz (cf. balistvo ‘medicine’,
balovali ‘curare’), as orig. ‘conjurer’ : late ChSI. bajatz ‘relate, conjure, heal’,
gydyti ‘heal’
arste fr. MLG arste
Digitized by Arya Samaj Foundation Chennai and eGangotri
am BODY; BODILY FUNCTIONS AND CONDITIONS 309 r
SCr. bajati ‘enchant, conjure’, etc., fr. the root in Grk. gnyi ‘say’, ete. Berne- ker 42.
ChSl. vract, Russ. vraé = SCr. vraé ‘sorcerer, fortuneteller’, etc., orig. ‘con- jurer’ : Russ. voréat' ‘growl, grumble, mutter’, vraka ‘nonsense, idle talk’, etc., fr. the root *wer- in Grk. etpw ‘say’, Skt. vrata- ‘command, vow’, etc. Walde-P. 1.283. Solmsen, Unters. 263.
ChSl. (late) lékart, SCr. lijekar, lijeé- nik, etc., fr. the Gme. (above, 3).
7. Skt. bhisaj- : bhisaj-,  bhisajya- ‘cure’ (4.86).
Skt. vaidya-, lit. ‘one versed in science (vidya- : vid-‘know’), learned’, then, like the current European adoption of Lat. doctor, (above, 4), ‘one skilled in medical science, doctor’.
Skt. cckitsaka-, fr. cikitsa- ‘heal, cure’ (4.86).
Av. vimad- : Lat. (4.86). Barth. 1450.
medeéri ‘cure’, etc.
4.88 MEDICINE, DRUG
Grk.  $éppaxoy Goth. (lubja-) Lith. vaistas, gydyklas NG yrarpixd, péppaxo ON lyf, lekningarlyf,lek- Lett. _zles Tat. medicamen(tum), _re- nisdimr ChSI. baltstvo, lékit
medium Dan. medicin, legemiddel SCr. _lijek, ljekarije It. medicina, droga Sw.  medicin, lékemedel, Boh. lék me médicament, drogue drog Pol. _lekarstwo, lek Tim nedicamento, droga OE _lybb, lacedom, ete. Russ. lekarstvo oe medicament, leac, doc- ME __ medicine, drogges Skt.  dGusadha-, bhesaja- ae ae 1.) Ay. —_ baéSaza- Nh. ie f NE medicine, drug Waa, toc Du. —_artsenij, geneesmid- Bn eddyginiaeth, cyffur del, drogerij
poo OHG  lachin, lachintuom,
etc. MHG arzenie, arzatie, la- chen NHG arznei, heilmittel, me-
The dizin, droge
Wi : 2 itil listed cover the wider | cussed 4.86, 4.87. Some are the result ur erence di. any medicinal substance | of specialization, as from ‘herb’ through as g Siavleas and the narrower ‘drug’, | ‘healing herb’, from ‘substance’ to Stedien ies substance or in- | ‘medicinal substance’, from ‘dry With those for _valority are connected | wares’(?) to ‘drugs’, from ‘knowledge’
? eae Cure’ or ‘physician’, dis-
through ‘magic’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
310
1. Grk. ¢dppaxoy (also ‘poison, en- chantment, etc.’), prob. : Lith. burti ‘practice sorcery’, Lett. burt ‘enchant’, root connection dub. Walde-P. 2.161.
NG yarpixd, neut. of adj. lazprxds, deriv. of tazpés ‘physician’ (4.87).
2. Lat. medicamen(tum), medicina (also ‘medical science’), remedium (but with extension beyond medical sense, as likewise its derivs. Fr. reméde, NE remedy, etc.) : medért ‘heal’ (4.86). Hence It. medicina, Fr. médicament (OFr. medecine > ME, NE medicine), Sp. medicamento, Rum. medicament, W. meddyginiaeth, Dan., Sw. medicin, NHG medizin, also more or less common in Slavic, SCr. medicina, Boh. medecina, Pol. medycyna, Russ. medicina, medica- ment.
It., Sp. droga, Fr. drogue (> NHG droge, Sw. drog; Fr. droguerie > Du. drogerij), ME drogges pl. (fr. Fr. or earlier from same source?), NE drug, formerly and still in part (esp. Fr.) used for chemical ingredients in general, later esp. for ingredients of medicine, prob. fr. Du. droog ‘dry’, either through a fre- quently attested commercial phrase MDu. droge vate ‘dry barrels’ for ‘goods in packing barrels’ (Baist, Z. frz. Spr. 32, 298f.), or simply through droge waere lit. ‘dry wares’, but used for ‘drugs, spices’, just as Lat. speciés, in late Lat. ‘wares’, was specialized to spices (Fr. épice, NE spice) or drugs (It. spezieria ‘pharmacy’). REW 2776a. Gamill- scheg 327. Deriv. fr. Arab. durawa ‘chaff’, preferred by Lokotsch 549, Franck v. W. 136 (also Wartburg 3.189 in heading, but see 190) is less likely.
Rum. leac fr. ChSI. léti (below, 6).
Rum. doctorie (pop.), fr. doctor in sense ‘physician’.
3. Ir. leiges, NIr. leigheas, properly ‘cure, healing’, also ‘medicine’, fr. liaig ‘physician’ (4.87).
NI. ioc fr. Ir. icc ‘cure, healing’ ; iccaim ‘cure’ (4.86). ;
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
W. cyffur ‘substance, matter’ (orig,? also ‘drug’ (cf. cyfferiwr ‘druggist’),
Br. louzou lit. ‘plants, herbs’, orig, pl of sg. form in W. llys, Ir. lus ‘plant, herb’. Henry 190. ‘
4. ON lyf esp. ‘herb with healing or magic power’, cpd. lekningarlyf, leknjs. lyf (: lekna ‘heal’), OE lybb also ‘oi- son’ = OHG luppi ‘poison, charm, sor- cery’, Goth. lubja- in lubja-leisei ‘gappa- keta, sorcery’: Ir. lub, NIr. luith ‘herb, plant’. Walde-P. 2.418. Falk. Torp 679.
ON laknisdomr, OF le&cedom ‘cure, medicine’, fr. ON laknir, OF lace ‘physician’ (4.87).
Dan. legemiddel, Sw. ldkemedel lit. ‘healing agent’: Dan. lage, Sw. ldka ‘heal’ (4.86).
==== leaf of 4.87 ====
leaf 347
```


## [2026-09-07T15:52:01.025Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"m8w\\b\" SOD_pages.txt | head -20; echo \"---- context 15302 ----\"; sed -n '15290,15320p' SOD_pages.txt"
}
```


### [2026-09-07T15:52:01.089Z] TOOL RESULT

```
18812:         maSe =»m8w                                VL^'lT*               EGSii 153; GMS 136, 1109
---- context 15302 ----
                                                                   TSP  6.165;wife
                                                                                 Hen. Texts. 733; Benv. Titres et Noms
       "belonging" ?, TSP 11.6 n p223
                                                                     Propres. 31; Frag. Len. 44.7
4058 y^qynywny C                               ^Jj»          4071 y>w B, M, S
     yamken-yone                                                                                     (j^ jl^ ^)jf
     rule
                                                                  yaw ox
                                                                  cow, ©ob. ~y; pi. -t(h) =^yw2
       Sund. AoFviii 1981 pl802, 21 V2
                                                                  VJ; SCE 161, 164, 292; TSP 2.772, 3.138, 186,
4059 r>MRH S                              (j*M>*.                   9.43; BBB; Y'wh, MDii A 5, 24
     ©Idg. =»m6w, m8>k
     wine                                                    4072 yV-1 B                            o> }**->-* <o>j
       MDii, MDiii ?                                              xaw (DYaghn. Yow, xoy ? ©3sg. pers. Y*wt
4060 y>my                                                           =^x}w-, yw'w-
              b =* y>mkyn
4061 y»n' B                                                       0o)beat
                                                                  BSTBL, Dhu. 34; GMS 233
  \,

                                                                                                                                    162

               y'w-
              4073 y'w-'        B -» yw-
                                                                                  yPt-, yfs-, yps-
              4074 yWysypt-y S                                    3€ ^          0o)make effort, OcOget tired, (fo)be weary
                   yaw-oxsipdi                                                  BBB f79 pi 05; VJ 58e; BSTBL, Dhy. 4; Hen.
                   cow's milk                                                     Tales. 486.3
                   Hen. Tales. 486.22
                                                                           4086 Ypt-    B             ^j*\j*z~0-jAitoJuZj'i{)j>
```


## [2026-09-07T15:52:06.465Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"m8w\\|mSw\\|m6w\" SOD_pages.txt | head -30"
}
```


### [2026-09-07T15:52:06.513Z] TOOL RESULT

```
15302:     ©Idg. =»m6w, m8>k
18797:         thus                                                       5295 mSw B, M, S                                  (ji)^
18812:         maSe =»m8w                                VL^'lT*               EGSii 153; GMS 136, 1109
```


## [2026-09-07T15:52:09.792Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18780,18830p' SOD_pages.txt; echo \"=== page tag ===\"; awk 'NR<18830 && /\\[pdf page/ {p=$0} END{}' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<18830' | tail -3"
}
```


### [2026-09-07T15:52:11.161Z] TOOL RESULT

```
    5280 mcryn C                                           J^1A          TSP 2.970
         m(a)cren, misren
         Egypt                                                      5292 m5h   S(MD) =* m8y
         C2, 60R1, 94V9, 104V 10, mycryn                            5293 mSp'r S                                o>j*l«b~l



I
    5281 mcryncyq C                                                      ma&par =»m8\ mr5p)r
                                                                         here
         macrencik, mscrencik ?
         (c?/)Egypt                                                      MSP bl60
         Sund. AI 28, 1988, 182                                     5294 mStnpV B                           ^jj'^t/ (^>)
                                                           ^Sj-o*
    5282 m5' B                                                           (a kind c»/)herb
                                                                         TSP 19.7
         ma8 -tm'5
         thus                                                       5295 mSw B, M, S                                  (ji)^
         VJ 1075
                                                                         wine
                                                                         maou (mdw) =*m8Jk, mw62
    5283 m52 S                                            bo!
         ma&a =»mrS, m8y, mSp'r, 'mS^                                    TSP 2.388, 2 Hi. 4; GMS 408, 1171; Hen. BSOAS
         here                                                              10, 98; Anc. Lett. 4.6; MDii A-16, 6, STi 36.1;
         Anc. Lett. 4.8; mSK MDii                                          Sund. AoFiii 14R1; BSTii: C2, 57R18
    5284 -m5   B                                     t'.v
                                                   #HW              5296 mdw    C =* m5w
        ma5 ©<*ma-hada =»-m                                         5297 mdy   C =* m5y
        to me, with me                                              5298 m8y   B, M, S                    (jj^ >^     >>)^J
        GMS 1348
    5285 m5'k S                                                          ma8e
                                                                         here (m8h, mSyy, mdy) ©<*imada          =^,m8(,)
         maSe =»m8w                                VL^'lT*               EGSii 153; GMS 136, 1109
 211
                                                                                                                   mhystk

5299 mey^n M                                 •J^^j'jJ*                   12, 56; TSP 10.3; Benv. SYd% apud. Yoshida.
     ma5yan                                                              SI 1984, 146; CII 1990 F19
        means, remedy                                            5310 roy6Nv   B'                                       ^
        Hen. Sogdica. 39.32, 36 n p43
                                                                       may8au ^myS'k
5300 mSy^y       S                                  <;L*<o^            fruit
                                                                       VJ 1369
       ma5yane (myS'n'y) ©<medydn <maiSyana
         -^rnS'n                                                 5311 my6p- B, S                   -v>* <>_jj oj^
       middle                                                         maySaP ©<magu-pati ©nom. -y; ace. -w, pi.
                                                                        -r(>); ob. pi. -ty =*mywpt
       STSC 139
                                             bfcj ) jl I^Ad^j)        minister, adviser
5301 mSycyk S
     ma8eclk                                                           VJ; TSP 5.5, 6.166; BSTBL, Padm. 48; Frag. Len.
=== page tag ===
```


## [2026-09-07T15:52:22.985Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SOD_pages.txt',encoding='utf8',errors='replace').read()\ni=t.find('5295 m5w')\nprint('leaf',t.count(chr(12),0,i))\nimport re\n# find nearby pdf page tags\nseg=t[max(0,i-6000):i+3000]\nprint([m for m in re.findall(r'\\[pdf page \\d+\\]',seg)])\nj=t.find('4059 y')\nprint('4059 leaf',t.count(chr(12),0,j))\n\""
}
```


### [2026-09-07T15:52:24.327Z] TOOL RESULT

```
leaf 643
[]
4059 leaf 643
```


## [2026-09-07T15:52:35.912Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 bimar ===\"; grep -n \"بیمار\" BQT_v1_pages.txt | head -10; echo \"=== page tags near ===\"; grep -c \"\" BQT_v1_pages.txt"
}
```


### [2026-09-07T15:52:35.984Z] TOOL RESULT

```
=== BQT v1 bimar ===
6157:ازآن . باس‌پوشی سوراخ دار که اطبا بیماران‌ر!
6158:در آن خواباند بسا بتشانشد ؛ و سر بیمار را از
11535:باشد که بدن بیمارانرا بدان پشویند و بعربی
12439:و بدن بیمار را بدان شویند و آنرا بعربی نطول
15460:نقطمدار بروزن بیمارهش ؛ حوشنکه پمرسپامك
19205:کردن - و شفا دادن بیمار - و اجابت دعوات
22651:بمعتی مانند هم آمده است - و بیمارستانرا نیز
22653:پیمااد غشج - بیمار معلوم» وفتح ین
22654:نقطه دار و سکون نون و جیم . بمعنی بیمارناك
22655:و دردمند است یمنی بیشتر اوقات بیمار ورنجوز
=== page tags near ===
32486
```


## [2026-09-07T15:52:36.157Z] TOOL CALL #27: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2071 --image 2>&1 | head -60"
}
```


### [2026-09-07T15:52:43.275Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 154; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2071.png
REF: BQT:2071  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 154  OCR-lang: fas

-۱< خی
مهن ۱ ه یکراول‌بروزن نگین,بمعنی مهیوه ۴ - بفتح اول و ثالث و واو
بزرکتر وبز رکه ترین باشد ۴ . .| واسکون ثانی » مغفف ماهیاوه است که نان
مهینه ؟ - یکر اول بر وزن نگیده, | خورش مردم لار باشد که از ماهی کوچك سازند
بمعنی‌مپن‌است که بزرکتر وبز رکه‌ترینه باشد . | وخورند . ۰
بیان بیست وهشتم
در میم با بای حطی مشتمل برهشتاد و دو لغت وکنایت
می * - بنتح اول وسکون ثانی؛ شراب | - وپیاله‌را نیز بطریق کنایه کنته‌اند ۷ همچتانکه
انگوربرا کوبند - و بمعنی کلاب هم‌آمده‌است۹ | میگوبند پیاله‌میخورند پمنی‌شراب میخورند۸ -
۱- از : مه ( بز رکه )۲ین ( پوند سبت ) »کردی 136218 ( بز رکه » مشهور):
0 3828 ( رئیس ) : سمنانی 136518 ۰ بلوچی 338220 « ژابا س ۳۹۷ ۰
۴ - ۸ ... و خودی خویش را وقف کرده‌اند برنظارة ورج» یعنی شکوهمندی برین و بر
یافت خوشی مپین » « دانشنامهة علائی. الهی. مصحح نگارنده س *۱۱ *.
۴ - از : مه ( بز رکه )+ ینه ( پوند دبت ) » قی : مهین .
۴ - مخفف مهیاوه(ه.م.) * ماهیاوه ۳ ماهیابه (ه.م.)
- تلفظ فارسی متأخر1ه33 , تلفظ قدیم 121 ( ر: فپرست شاهنامهٌ ولف )» پپلوی
24 ۰ اوستایی -332001 ( عل ) » هندی باستان -1384121 ( شیرین» صل )» نیز اوستا
- 12042 ( مشروب مستی آور ) » هندی باستان 13202 » قی : اسلاوی کلیایی 6۹۲
(صل » غراب) ؛آلمانی عالی‌جدید 2/۵۲۳ اسشق ۱۰۰۳ *. دارمستتر بتبع سنت معنی1 7824
اوستائی‌را ( شراب ) میداند ولی‌معنی صل از کلمات استی111 , 1310 نأیید میشود «هوبشمان
۳ نیز در پهلوی 1 (می ) خوانده شده « اونوالا ۲۵۲ » کردی 13261 ( شراب »
مشروب ):. 1۷61 , 13261 ۰ 3380 ( خوشهٌ انگور , شراب ) « ژابااص *2۱ > قن : مٌل (بطم)
و رك : مزدسنا ص ۲۹۹ پیعد ؛ و رك : می‌سوسن . ‎٩‏ سر دح :
همه کوهر و زعفران ربختند همه مشکه با می برآمیختند
همه پال آسپان پرازمعك و می پراکنده دینار در زیر پی .
فردوسی طوسی « شاهنامةٌ بخ اج ۱ص ۷۲
ولف در فهرست‌شاهنامه « می » را دربعی موارد شاهنامه - ازجمله درابیات فوق - بمعنی کلاب
آورده است .
۷ -يك می بدوکنج شایگان خر رغم دل رایگان خران خر .
خاقانی شروانی « فرهنگه فظام >.
۸ - می ( بکر اول ) درتلفظ کنونی 1731 ودر تلفظ قدیم 18 » مشتق ازه همی» است
بحذف ۸۶ 32 . رك : همی « دارمست . تتبعات ج ۱ ص ۱۱۲ و ۲۱۵ ۰ ؛ وآن علامت ماضی
استمراری ( میکرد ) و مضارع ( میکند ) است که پیش از قعمل درآید و گاه برس امرخاشر در
آپد ( میکن ) .
```


## [2026-09-07T15:52:59.331Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"مُل\\|مل \\*\\|شراب انگوری\" BQT_v4_pages.txt | head -20; echo \"=== pdf page tags ===\"; grep -n \"pdf page\" BQT_v4_pages.txt | head -3"
}
```


### [2026-09-07T15:52:59.399Z] TOOL RESULT

```
2506:از شراب انگوری هم 09 با فرهنگه ۴ بمعتی سخن باشد
6162:معروب )۰ 361 ۰ 13261 ۰ 3320 ( خوشهٌ انگور , شراب ) « ژابا ص 2۱۰ » قی د مُل (ضم)
12946:۴ - از: یوش (ربشه قمل * آمی) ۱ (پموند صفت مشبهه) . قن : شوشا» شوشا4.
17869:باشد - و بفتح اول وضم ثالی» شراب انگوری را | افتد #۰
19783:مسحف « بوند که » «لع33۷2848 پهلوی ( در ارءنی 0۷28426 ) بمعنی کامل * بوندی
=== pdf page tags ===
1:[pdf page 1]
2:[pdf page 2]
23:[pdf page 3]
```


## [2026-09-07T15:53:04.445Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR<=17869 && /^\\[pdf page/ {p=$0} NR==17869 {print p}' BQT_v4_pages.txt; sed -n '17855,17900p' BQT_v4_pages.txt"
}
```


### [2026-09-07T15:53:05.863Z] TOOL RESULT

```
[pdf page 1]
کراین هفت پل را بچنگه آوریم جهان پیش کاوس تنگه‌آوریم -
فردوسی طوسی « شاهنامةٌ بخ ج اس ۸۱۹ 1
8 هنده - درتلقظ قدیم بفتح‌اول وسوم (نلفظ کنونی بکسراول‌وسوم) < هفت‌ده ؛ کردی
هفتده « ژابا ی ۸4۹ ۰ ی زکردی 6۴460 ۰ 46 - 56۲ ۰ 465 - 56 , طفلگقط ؛
زازا 821169 «ژابا ی ۸2۹ ؛ کیلکی 81۷48 ؛ عدد برابرده بعلاوة هفت ؛ صدد میان‌شاترده
وهیجده ؛ پاتزده پملاوه دو .
[pdf page 440]
- ۷و۳ حل
وماشد آن روید . کویند هر که آارا در محل کوبند - و بمعنی تردد هم آمده است.
جنایت وناپاکی‌خورد ددل وی منقطم کردديمني که ۴ ینم اول وفتح ثابی مشبو :
او را فرزند شود وآنرا بعربی بنات‌آلرعدخوانند
کر بای ابجد۱ . بمعنی هكك است که جتن کلو وفواق باشد.
هگوی دی رز مرو ون ۱ هکها ۴ بترم درها سگرن
و واو بتختابی کشیده, سرگشته وحیران‌وپربغان ٍ هر دوکاف , صدای گریه را کویند که در کلو
باشد - و بفتح اول وضم ثالی» شراب انگوری را | افتد #۰
بیان سیزدهم
در های هوز با لام مشتمل بر سی و دو؟ لفت و کنایت
هل - بنم اول و سکون ثالی » بممنی ا است بعنی بگذار وفروکذار و بهل ‎٩‏ - و عیل
آغوش وبغل باشد 8 - ویکسراول‌امریر گذاشتن | را نیز کوین د که بمربی قاقله خوانند ۷ .
() چش : می. :
۱ - « هکل. فقع است» « تحفة حکیم مومن *. رك : فقع - 7 سروری
نویسد ۰« هکوی بفنتح ها و ضم کاف » شراب باشد و بممنی تردد نیز آمدء. کذافی‌المژیده
و در ادات ( اداة الفسلاء ) بوزن مروی‌آمده بمعنی سر گشته و متردد ». رشیدی آرد : « هکوی
( بالضم و واو مکور ) سرگشته و متردد و در نخهٌ سروری ( بفتح ها و ضم‌کاف ) بمعنی تردد
آورده » و بمعنی شراب نی زگفته . و جتم ها وکاف ء خربزة لارسیده .» شاد لیاورده‌اند +
۴ - اسم صوت . رك : هكك , هكهك . هکچه. ۴ - اسم صوت . رك : هکه ,
هکك, هکچه ؛ حكهك در یزد و خراسان مستعمل است «فرهنگه نظام» : :
صوفی قرابه از می حکهك گربه کشاد کریةٌ خولین او در سجده جای او ببین-
خمرو دهلوی « رشیدی >.
6 - جهانگیری این بیت مولوی را شاهد آورده :
ای عشق خندان همچ وگل , ای خوش نظر چون عق ل کل
خورشید را درکش به هل . ای شهسوار هل انی!
مرا جکوید : « بدین معنی درکتب دیگر دیده اشده و میتواند که « مل > بضم میم باشد پممتی
شراب . ومعنی‌بیت برین تقدیر لیزصحیح میشود چنانکه پر دقیقه فهم پوشیده لیست .*۲فرهنگه
فظام ». ‎٩‏ - امر از ۸« هلیدن > و « هشتن > (عم.) ۷ -ر4 : هیل .
2 هگرز - بفتح اول و دوم » پهلوی ۵86170 ( هرکز ) « تاوادیا ۱۹۱ * ؛ هرکز .
ر4 : هرکز: شمس قیس در المعجم آرد : ۶ مود سعدگفته است :
کمام از پی‌آن نیروار قامت تو وزو مرا همه درد وغم است قسمت وقیر.
مرا ان تیر فراق کرد وهگرز کسی شنید که باشد کمان ال تور ؟
و در صحیح لفت دری « هگرز > لیست او مستمیل "هر کز؛ست . » ولی چنانکه دیده شد در
پهلری « عکرج > آمده است.
[pdf page 441]
هلا رده
هلا ۱ - بفتح اول و ثالی بالف کشیده هلاهالا - با ها و لام بروزن طباطیا »
بممنی دا باشد از برایآ کاهانیدن وتنبیه (۱) | بمعنی سهل وآمان باشد ‎٩‏ .4
کردن ؛ ودر طمنه زدن مکررکنند. هلتاكگ - بنتح اول وتای قرشت بروزن
```


## [2026-09-07T15:53:11.964Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"در میم با لام\\|مل \\[\" BQT_v4_pages.txt | head; echo ===; grep -n \"بیان .* در میم\" BQT_v4_pages.txt | head -40"
}
```


### [2026-09-07T15:53:12.026Z] TOOL RESULT

```
Exit code 1
4464:در میم با لام مشتمل بر سی وهفت لغت و کنایت
(eval):1: == not found
```


## [2026-09-07T15:53:15.860Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR<=4464 && /^\\[pdf page/ {p=$0} NR==4464 {print \"PDFPAGE:\",p}' BQT_v4_pages.txt; sed -n '4455,4520p' BQT_v4_pages.txt"
}
```


### [2026-09-07T15:53:17.251Z] TOOL RESULT

```
PDFPAGE: [pdf page 1]
میاه , 8805 .1۰176 ۰ س ۸۵ ) اکردی 5 لا . 025 ۰ حفقات . زازا 65 /رفه22
«زاباس ۳۹۹ , کیلکی 13-2882 : حشره‌ای از راستةٌ دوبالان, |
دارای خرطومی که رای آن برجسته و اسفنجی است . دو چشم 8 ت
مر کب‌بز رکه ودوشاخك كوچك کوتاه ويك جفت بال‌دارد. پاهای : ۹ رت
مکی بچنگاها و بادکش‌هایی ختم میشود . مکگس با خرطومش
هرچیز مایع را میمکد و ازآن نغذیه میکند و برروی زباله و .مکی
کثافات تخم میکند .
[pdf page 113]
بیان بیمت و سیم
در میم با لام مشتمل بر سی وهفت لغت و کنایت
مل ».ینم اول و اسکون ثالی » بممنی یافته را نیز کوبند - و بمعنی حخمیر درزبرآش
امرود باشد. وآن میوه‌است مفروف که بعریی کزدن - و جامه دوختن هم آمده است ۴ .8
کنثری خواشد ۱ - و نوعی از امرود بز رکه ملاخ - بنتح اول و ثای بالف کنشیده
بیمزه هم هست که آنرا حرمل کویند۱ - وبمعنی و بخای قطه‌دار زده , نام جزبره‌است از جزایی
غراب انگوری هم هست۳ - وبلفت اندلی‌دوامی | زبرباد واکنون بملاخه اشتهار دارد - ونام دوائی
است که آنرا پرسیاوشان کوبند - و بکراول, | هم هت ماند آغنان 8 .
بمعنی موی باشد مطلقاً ام از موی سر و موی : هلاه ۱ - بنم اولوفح زای قطه‌دار,
رش واعتای دیگراز اسان و حیوان۴ - و بفتح | گوشت پاره ای باشد شبیه بزبان کوچکی که از
اول و تشدید ثالی » در عربی بمعنی سیرشده واز اقهای کام آويخته است ؛ و بفتح اول هم درست
کرستکی برآمده باشد - وآزار واندوه و ملال | است ؛ و با زای فارسی نیز آمده است.#
۱ - ر4 : جهانگیری ۰ ۲ - هندی باستان - ۷164] 127 ( شراب‌انگوری)
اسشق ۹۹۰ بقل از . 2 2016 133 و35 ۰ 20۸10 ,0963288 310؛ سندی6 104
از 328401 , فس: فارسی «می» . تبدیل « ال > و3 ذ > » درین دو زبان سابقه دارد . رك : پل
[یکنر] [ پاشته ) * طج سندی ( .98 ۰ 8 ,. 1028-۳۷۵145۰ 28ن4ع50,ق2نس0ع11 )
«مل , لبیذ بود . عنصری ( بلخی ) کوید :
پزربنه جام اسرون لمل مل فروزنده چون لاله بر زردگل .>
5 لغت فرس ۰۳-۳۲۲
۴ - رش جش چنان دراز است کوب ی که مل دم گراز است .
شجاع بهرامی « جهانگیری >
۴ - ر4 : افرب‌الموارد ‏ منتهی‌الارب. 8 - ملاخ ( جنم اول وتشدید دوم ) عربی
است-وبگیاهان شورمز؛ بیارمختلف ازجمله ۳06۴ 4۵ 16۲م0007 ( ۲۶110009 عاونا ه)
اطلاق میشود « عقار ۲۲۵ ف >. ‎٩‏ «ملاز * ملاج « فرهنگه نظام » « ملازه » بتازی
لهاة کوبند یعنی‌کام » منجيك ( ترمذی ) گوید :
خواجه غلامی خرید دیگر تازه ست هل وعرزه گرد ولتره ملازه >
َ لغت فری ۸۷۸ ۰
ملا - جنم اول وتشدید دوم » در ترکی‌عشمانی مثلا ( چشم اول ) . ظ . مبدل «مولی»
عربی است بمعنی سرور ومخدوم . رك : دزی ج ۲ اس۹*۸. ملا محمدپاقر مجلسی در وسیت نامه
خود (چاپ مشکوة. تهران۱۳۲۳) نام وعنوان پدرخود ملامحمد تفی را «مولی محمد تقی» با دکرده
است ؛ آخوند » باسواد » درس خوانده , فاضل » روحانی .
5 ملاقه - بفتح اول و دوم : رك : ملمقه .
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
```


## [2026-09-07T15:53:33.800Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22630,22700p' BQT_v1_pages.txt; echo \"=== pdfpage ===\"; awk 'NR<=22660 && /\\[pdf page/ {p=NR\": \"$0} NR==22660{print p}' BQT_v1_pages.txt"
}
```


### [2026-09-07T15:53:35.164Z] TOOL RESULT

```
یله - با انی مجپول بر وزل حیله,
خشکی و جزبر؛ میان دربا و رودخانه باشد -
و نوعی از دوابی هم هت - و طبله و خرطهُ
عطار را هم گفته‌اند ومنشور یادشاهان؟ - وقبالة
خانه و باغ را نیز کویند ۴ - و بمعنی رخاره
و پهلو نیز آهده است- ویاروب کشثیبانان که‌بدان
غراب رانند - ویبکانی که مانندیل سازند» -
و چرل و ریمی که از زخم آید - و بمعنی له
ابریشم هم بنظر آمده است - و بت رکی بمعنی
همچنین باشد .
(۱) چك : ژد و بازند .
مك . نت وق <
دیب رک ۰۳۹ 1 : اس ۲۹.
«اونوالا+۲* ازریشابرانی باستان۲02۲3 -
کیلکی ۲1۳2۲ .
۸۵ ره : اسفا
ک ۳۰ ۳
لبم ٩‏ ت بروزن‌میم؛ تری‌وواهمعرا گوند.
دیمار ۷ بروزن دیوار, ناتوان وختهرا
کگویند وامربه نرسیدن هم هست متی بتری.
یماد سان ۸ بعثی‌سمارهانشد.چسان
بمعتی مانند هم آمده است - و بیمارستانرا نیز
کون که بعر نی دارالشقاء خوانند ِِ‌#
پیمااد غشج - بیمار معلوم» وفتح ین
نقطه دار و سکون نون و جیم . بمعنی بیمارناك
و دردمند است یمنی بیشتر اوقات بیمار ورنجوز
باشد- و کسی رائیز گویند که ببه‌اری او از روی
لاز و غمزه باشد .
بی‌محابا بلنگ ه کنابه از دیا
وروز کاراست - و کنابه ازمی که وهوت‌هم هست.
لیهیر ع بر وزن دییگر؛ بمعئی بیشمار
وییحد و حساب وبیار باشد. چه مربیعنی شمار
هم آمده ات
لیهاز ع کنابه ازمردم سبك‌وبی‌تمکین
مهو ری حم ثالث بروزن بی‌نوری؛
بمعنی مهابت و صلابت باشد*۱.
یف ۷اه بکسر اول بر وزن میتاء بمعنی
دیده ور باشد - و بلفت زند و پازند (۱) بمعنی
۴ - یلفان. شهرست تزديك
۴ -ر: یله. ۴ ر:
شهمیرزادی؟01۳18 < . ۲ص ۱۷
هی کب از امین هی
*- فرهنگ دسانیر ۲۳۷ .
«اسفا ۱ : ۲ ص ۱۸۱ ۰ .
معرب آن یمارستان و مارستان «شی». "۳:۱
ماه است که بعربی شه ر گوبندا .
که مردمرا در حالت ماشفه دیده میشوده وآنرا
مربی ممایثه کوش
دریجهٌ خانه را گوند .
بیناساك .. بسکون سینو کاف, بمعنی
بیناس باشد که دربحهٌ خانه است ۰ رب بای فارسی
هم‌آحده ۱ سست ه
بنایی بروزن‌زیبابی» بمعنی‌دیده‌وری
و بینند گی باشد - و گاه بینابی گویند و از آن
چشم اراده نماد که عین است
ین ب یکر اول و فتح ثانی و سکون
ی و هتند؟ باشد که از
هستی و بودن است
تی‌تماری ان از
زنان باشد .
بی نمکی کر دن - کنابه از بیوفایی
و بی‌عز گی- وبی وضع ی کردن باشد .
پیتنگ ه / با نون دیگربروزن‌زببنده,
بمسی شخص بینا و صاحب وفوف و عاقبت‌اندیش
باشد - و چشم را نیز کوند که بعربی عبن
خوانند ۵,
حیض آمدن
وقار باشد » چه شک به‌سنی عب و عار است. 8
مصد)
۵ - به بینندکان آفرشنده را
٩‏ رگ : ور
=== pdfpage ===
```


## [2026-09-07T15:53:42.521Z] TOOL CALL #33: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:340 --image 2>&1 | head -80"
}
```


### [2026-09-07T15:53:43.934Z] TOOL RESULT

```
no scan of BQT covers printed page 340 (see 'scans' in refs_online.json)
```


## [2026-09-07T15:53:49.039Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v1_pages.txt | head -3; echo ===; grep -n \"pdf page\" BQT_v1_pages.txt | awk -F: '$1<22660' | tail -2; echo ===; grep -n \"pdf page\" BQT_v1_pages.txt | awk -F: '$1>22660' | head -2"
}
```


### [2026-09-07T15:53:50.398Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-07T15:53:53.851Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v1_pages.txt | head -3 ; echo \"-----\"; grep -n \"pdf page\" BQT_v1_pages.txt | awk -F: '$1<22660' | tail -2 ; echo \"-----\"; grep -n \"pdf page\" BQT_v1_pages.txt | awk -F: '$1>22660' | head -2"
}
```


### [2026-09-07T15:53:55.227Z] TOOL RESULT

```
-----
-----
```


## [2026-09-07T15:53:58.906Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf8',errors='replace').read()\nprint('total ff',t.count(chr(12)))\ni=t.find('دیمار')\nprint('idx',i,'leaf',t.count(chr(12),0,i))\nprint(len(t))\n\""
}
```


### [2026-09-07T15:54:00.344Z] TOOL RESULT

```
total ff 776
idx 930526 leaf 560
1285412
```


## [2026-09-07T15:54:09.343Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1.txt BQT_alt_v1.txt BQT_dli_part1.txt; do echo \"=== $f ===\"; grep -n \"بیمار\\|دیمار\" $f | head -5; done"
}
```


### [2026-09-07T15:54:10.719Z] TOOL RESULT

```
=== BQT_v1.txt ===
10303:ازآن . باس‌پوشی سوراخ دار که اطبا بیماران‌ر! 
10304:در آن خواباند بسا بتشانشد ؛ و سر بیمار را از 
21797:باشد که بدن بیمارانرا بدان پشویند و بعربی 
23670:و بدن بیمار را بدان شویند و آنرا بعربی نطول 
29897:نقطمدار بروزن بیمارهش ؛ حوشنکه پمرسپامك 
=== BQT_alt_v1.txt ===
9453:ازآن . باس‌پوشی سوراخ دار که اطبا بیمارانرا 
9454:در آن خواباند با بتثاننه » و سر بیمار را اژ 
9668:و امثال آن بمقدار قامت آدمی که طبیبان بیمار 
19767:باشد که بدن بیمارانرا بدان بشویند و بعربی 
21392:و بدن ,بیمار را بدان شویند و آترا بعربی نطول 
=== BQT_dli_part1.txt ===
```


## [2026-09-07T15:54:21.198Z] TOOL CALL #38: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T15:54:21.207Z] TOOL RESULT

```


```


## [2026-09-07T15:54:25.790Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%85%D8%A7%D8%B1",
 "prompt": "Give the full etymology section for the Persian word بیمار (bimār) 'sick, patient' — Middle Persian form, Proto-Iranian reconstruction, and any cited authorities (Hasandust, MacKenzie, Cheung, Horn). Quote verbatim."
}
```


## [2026-09-07T15:54:27.025Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/med-",
 "prompt": "Give the reconstruction, gloss, and full descendants list for PIE *med- including Avestan, Latin, Germanic branches. Quote verbatim."
}
```


### [2026-09-07T15:54:31.113Z] TOOL RESULT

```
# Etymology of بیمار (bimār)

Based on the Wiktionary entry, here is the complete etymology section:

The word derives from **Middle Persian** _𐭥𐭩𐭬𐭠𐭫_ (wēmār, "sick, ill"), which combines a Proto-Indo-European root with an agent suffix. The source states: "From Middle Persian _𐭥𐭩𐭬𐭠𐭫_ (wēmār, 'sick, ill'), from Proto-Indo-European _\*wemh₁-_ ('to spew, vomit') + _ār_ (agent suffix)."

The entry identifies cognates including Latin _vomō_ ("be sick, vomit") and Northern Kurdish _bîvêr_.

**Note:** The provided content does not cite Hasandust, MacKenzie, Cheung, or Horn. The etymology relies on standard historical linguistic reconstruction without attribution to those specific authorities.
```


### [2026-09-07T15:54:33.709Z] TOOL RESULT

```
# PIE *med- Reconstruction

**Reconstruction and Gloss:**
The root *med- has three meanings: "to measure," "to give advice," and "healing."

**Selected Major Descendants:**

**Avestan:** The text references "𐬬𐬍𐬨𐬀𐬛 (vīmad, 'physician')" as an Indo-Iranian formation.

**Latin:** "medeor ('to heal')" derives from Proto-Italic *medēōr, with further descendants noted in the source.

**Germanic Branch:** Multiple formations appear, including Proto-Germanic *metaną ("to measure") and *mōtaną (from a secondary perfect). Old English reflexes include "metod," "meted," "metud," "meotod," and "meotud."

**Additional Major Branches:**
- Proto-Celtic: *medyetor ("to measure, judge")
- Proto-Hellenic: Ancient Greek μέδω (médō, "to protect"), μέδομαι (médomai, "to provide for")
- Proto-Tocharian: *meim, yielding Tocharian A "mem" and Tocharian B "maim"
- Proto-Armenian: Old Armenian միտ (mit, "mind, intellect")

The root shows remarkable productivity across Indo-European languages with semantic extensions from basic measurement to medical and cognitive domains.
```


## [2026-09-07T15:54:47.537Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG mad ===\"; grep -n \"^\\*mad\\|\\*mad-\\|vīmad\\|vimad\" CHEUNG.txt | head -20; echo \"=== CHEUNG vam ===\"; grep -n \"wēmār\\|vēmār\\|bīmār\\|bimār\" CHEUNG.txt | head; echo \"=== NYB ===\"; grep -n -i \"vemar\\|vēmār\\|vimar\\|bimar\" NYB_vol1.txt NYB_vol2_glossary.txt | head; echo \"=== HUB bimar ===\"; grep -n -i \"bimär\\|bimar\" HUB.txt | head"
}
```


### [2026-09-07T15:54:47.623Z] TOOL RESULT

```
=== CHEUNG mad ===
16779:*mad2 253 
16801:*mad! ‘to become intoxicated, joyous’ 
16813:*KHOTANESE: *mad- ‘to be intoxicated’ = SGS: 108 
16828:*mad ‘to curdle, coagulate’ 
16861:*SANSKRIT: Skt. mástu- (n.) ‘sour cream’ (< *mad-stu-) = EWAia П: 336 
37546:*mad-, 253 
55648:*mad 
55656:*mad', *yrad 
56184:*mad 
=== CHEUNG vam ===
=== NYB ===
NYB_vol2_glossary.txt:1435:enyä [’yny’] otherwise 1377; bē... ~ except: bē magvemart ... ~ ... hec mart pat xčinak i xvēš bē mà pāyēt except the Magians. .. no man shall remain at home 2035; bē pat parvānakēh + yazdān
NYB_vol2_glossary.txt:4152:vīmār [wym'l] ill, pl. cas. obl. ~-dn 85%. — MPrs wym?r (BBB); Paz. vimär, NP bimar.
NYB_vol2_glossary.txt:4154:vimarčnitan to make a p. ill 43??.
NYB_vol2_glossary.txt:6192:wym’r: vimar
NYB_vol2_glossary.txt:7069:bīmār: vimar
NYB_vol1.txt:9967:oum: vimar 
=== HUB bimar ===
```


## [2026-09-07T15:54:47.849Z] TOOL CALL #42: WebSearch

```json
{
 "query": "Hasandust ریشه‌شناسی بیمار فارسی میانه wēmār اوستایی"
}
```


### [2026-09-07T15:54:55.512Z] TOOL RESULT

```
Web search results for query: "Hasandust ریشه‌شناسی بیمار فارسی میانه wēmār اوستایی"

Links: [{"title":"بیمار به انگلیسی - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatoen/%D8%A8%DB%8C%D9%85%D8%A7%D8%B1/"},{"title":"بیمار - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%A8%DB%8C%D9%85%D8%A7%D8%B1/"},{"title":"زبان فارسی باستان - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C_%D8%A8%D8%A7%D8%B3%D8%AA%D8%A7%D9%86"},{"title":"زبان فارسی میانه - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C_%D9%85%DB%8C%D8%A7%D9%86%D9%87"},{"title":"ریشه‌شناسی واژة خورشید (خراسان)","url":"https://anthropologyandculture.com/%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C-%D9%88%D8%A7%DA%98%D8%A9-%D8%AE%D9%88%D8%B1%D8%B4%DB%8C%D8%AF-%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86/"}]

Based on the search results, I found relevant information about the etymology of the Persian word "بیمار" (bīmār, meaning "sick" or "ill"):

The Persian word "بیمار" (bīmār) is derived from the Middle Persian word "wēmār", which comes from the Avestan root "vi-mar-", meaning "that which relates to dying/is dying".

The Avestan prefix "vi" (which evolved into modern Persian forms "go" or "bi") combines with the Avestan word "mār", which derives from the root "mar" meaning "to die". The Aryan word "mār" itself comes from the root "mar" (meaning "to die"), related to death.

The search results also note that there are incorrect interpretations of "بیمار" as "bi-mār" (without mār, where mār is a symbol of health in Iranian culture), but the correct etymology traces back through the documented linguistic pathway from Avestan through Middle Persian to modern Persian.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T15:55:21.454Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD med- ===\"; grep -n \"^med-\\|^med- \\|med-\\.\" AHD_watkins1985.txt | head -20; echo; grep -n \"medhu\" AHD_watkins1985.txt | head; echo \"=== AHD me-2/me- measure ===\"; grep -n \"^me-1\\|^me-2\\|^me-3\\|^me-4\\|^menot\\|^mē\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T15:55:21.518Z] TOOL RESULT

```
=== AHD med- ===
732:form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,

148:The names for a number of insects can be reconstructed in the protolanguage, includ- ing the wasP (wopsa), the hornet (*kras-ro-, a derivative of ker-', “head,” from the shape of the insect), and the fly (mu-2). The BEE (bhei-') was particularly important as the producer of honey, for which we have the common Indo-European name melit-. Honey was the only source of sugar and sweetness (swad-, “sweet,” is ancient), and notably was the base of the only certain Indo-European alcoholic beverage, MEAD, medhu-, meaning in different dialects both “mead” (“wine” in Greece) and “honey.” The Germanic lan- guages have innovated, perhaps from a taboo on speaking the name while gathering wild honey; the common Germanic English word HONEY is from an old color adjective for “yellow,” k(e)neko-.
732:form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,
1237:AMBLYOPIA mel-1 AMBROSIA mer-2 AMBSACE ambho AMBULATE al-2 AMBUSCADE busk- AMBUSH busk- AMELIORATE mel-4 AMENABLE men-2 AMEND mend- AMENORRHEA mé-2 AMENT! = ap-1 AMENT2 men-1 AMETHYST medhu- AMIANTHUS mai-2 AMICABLE amma AMICE yé-
1833:MEAD! medhu- MEAD? mé-4
1860:-METER mé-2 METHEGLIN med- METHINKS tong- METHOD sed-2 METHYLENE hule, medhu- METONYMY no-men- METOPE okw-
=== AHD me-2/me- measure ===
```


## [2026-09-07T15:55:21.553Z] TOOL CALL #44: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/324.jpg"
}
```


### [2026-09-07T15:55:21.569Z] TOOL RESULT

```

```


## [2026-09-07T15:55:47.394Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD index turmoil / mood ===\"; grep -n \"TURMOIL\\|MOOD\" AHD_watkins1985.txt | head; echo \"=== AHD me-2 measure ===\"; grep -n \"To measure. Contracted\\|MENSES\\|mé-2. To measure\" AHD_watkins1985.txt | head; echo; grep -on \"mé-2[^A-Za-z][^.]\\{0,600\\}\" AHD_watkins1985.txt | head -4"
}
```


### [2026-09-07T15:55:48.815Z] TOOL RESULT

```
=== AHD index turmoil / mood ===
732:form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,
1882:MOLTO mel-4 MOLY md6(u)lo- MOLYBDENUM plumbum MOMENT meue- MOMENTOUS meue- MOMENTUM meue- MONAD men-4 MONANTHOUS = andh- MONASTERY men-4 MONAXON aks- MonpDay mé-2 MONEY men-! MONGER meng- MONGREL mag- MONILIFORM mon- MONISH men-1 MONITION men-1 MONITOR men-1 MONK men-4 MONO- men-4 MONOCLE oOkw- MONOCLINIC klei- MONOCLINOUS klei- MONOCOQUE kokkos MONODY wed-2 MONOECIOUS weik-! MONOMER (s)mer-2 MOoNOPHYSITE bheue- MONOPODIUM ped-1 MONOPOLY pel-5 MONOTREME tere-1 MONS men-2 MONSTER men-1 MONTAGNARD men-2 MONTANE men-2 MONTE men-2 MONTH mé-2 MONTICULE men-2 MONUMENT men-! MOOCH meug-! MOOD! mé-1 MOOD? med- MOON mé-2
=== AHD me-2 measure ===
730:tive masculus, male, manly: MACHO, MALE, MASCULINE; EMASCULATE.] mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 700.] mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS. 4, Latin mdteriés, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard timber used in carpentry, hence (by a calque on Greek Aulé, wood, matter) substance, stuff, matter: MATERIAL, MATTER. 5. Greek compound Démétér, name of the goddess of produce, especially cereal crops (dé-, possibly meaning “earth”): DEMETER. [Pok. mdter- 700.] math-. Worm. With uncertain preform, but clearly re- lated, is Old English moththe, moth: motu. [Pok. 1. math- 700.] [Mawort-. Name of an Italic deity who became the god of war at Rome (and also had agricultural attributes), hence also the name of the planet Mars (doubtless from its red color, the color of blood). Latin Mars (stem Mart-), Mars: MARCH, MARS, MARTIAL, MARTIAN.] mazdo-. Pole, rod, mast. Germanic *mastaz in Old Eng- lish mest, mast: MAST}. [Pok. mazdo-s 701.] me-1. Oblique form of the personal pronoun of the first person singular. For the nominative see eg. 1. Germanic *mé- in Old English mé (dative and accusative): ME, MYSELF. 2. Possessive adjective “mei-no- in Germanic *min- in: a. Old English min, my: MINE?, My; b. Middle Dutch mijn, my: MYNHEER. [Pok. 1. me- 702.] me-2, In the middle of. 1. Suffixed form *me-dhi in Germanic *mid- in Old English mid, among, with: MID- WIFE. 2. Suffixed form *me-ta in Greek meta, between, with, beside, after: META-. See also medhyo-. [Pok. 2. me- 702.] mé-1, Expressing certain qualities of mind. Contracted from *meo-. 1. Suffixed o-grade form *mé6-to- in Ger- manic *méthaz in (i) Old English méd, mind, disposition: MooD! (ii) Old High German muot, mind, spirit, in German Gemiit, spirit, feelings, temperament: GEMUT- LICH, GEMUTLICHKEIT. 2. Perhaps Latin més (< *mé-s-), wont, humor, manner, custom: MORAL, (MORALE), MORES, MOROSE. [Pok. 5. mé- 704.] m6-2, To measure. Contracted from *meo-. I. Basic form mé-. 1. Suffixed form *mé-lo- in Germanic *mélaz in Old English m#l, “measure, mark, appointed time, time for eating, meal”: MEAL?; PIECEMEAL. 2. Suffixed form *mé-ti- in Latin métiri, to measure: MEASURE, (MEN- SURAL); (COMMENSURATE), DIMENSION, IMMENSE. 3. Possibly Greek metron, measure, rule, length, propor- tion, poetic meter (but this is referred by some to med-): METER!, METER?, (METER?), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRO- NOME. 4, Suffixed form *mé-trd- in Sanskrit mdtrd, a measure: MAHOUT. II. Extended and suffixed forms *mén-, *mén-en-, *mén-s-, *mén-dt-, moon, month (an ancient and universal unit of time measured by the moon). 1. Germanic *ménén- in Old English ména, moon: Moon; (Monpay). 2. Germanic *ménéth- in Old English ménath, month: MONTH. 3. Greek mén, méné, month: AMENORRHEA, CATAMENIA, DYSMENORRHEA, (MENARCHE), MENISCUS, MENOPAUSE. 4. Latin ménsis, month: MENSES, MENSTRUAL, (MENSTRUATE); BIMES- TRIAL, SEMESTER, TRIMESTER. [Pok. 3. mé- 703, ménot- 731. fen Big. Contracted from *meo-. 1. Suffixed (compara- tive) form *mé-is- in Germanic *maiz6n- in Old English mara, greater, and madre (adverb), more: MORE. 2. Suf- fixed (superlative) form *mé-isto- in Germanic *maista- in Old English m&st, most: Most. 3. Suffixed o-grade
1846:MELON mélion MELT mel-1 MEMBER méms- MEMBRANE méms- MEMENTO men-! MEMORABLE (S)mer-1 MEMORANDUM (s)mer-1! MEMORY (s)mer-1 MENACE men-2 MENAGE men-3 MENARCHE = arkhein, mé-2 MEND mend- MENDACIOUS mend- MENDICANT mend- MENHIR s6-2 MENINX méms- MENISCUS mé-2 MENOPAUSE mé-2 MENSCH man-! MENSES mé6-2 MENSHEVIK mei-2 MENSTRUAL mé-2 MENSTRUATE mé-2 MENSURAL mé-2 MENTAL men-1 MENTION men-1 MENTOR men-1 MENU mei-2 MERCENARY merk-2 MERCER merk-2 MERCHANT merk-2 MERCURY merk-2 MERCY merk-2 MERE! mer-1 MERE? mori-

1237:mé-2 AMENT! = ap-1 AMENT2 men-1 AMETHYST medhu- AMIANTHUS mai-2 AMICABLE amma AMICE yé-
1299:mé-2 BIN bhendh- BINAL dwo- BINARY dwo- BIND bhendh- BINNACLE ghabh- BINOMIAL nem- BIO- gW¥ei-
1336:mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1385:mé-2 COMMENT men-! COMMERCE merk-2 COMMINUTE mei-2 COMMISERATE miser COMMIT (s)meit(a)- COMMIX meik- COMMODE med- COMMODIOUS med-
```


## [2026-09-07T15:55:49.032Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SYN.txt',encoding='utf8',errors='replace').read()\ni=t.find('5.91 WINE')\nprint(i)\nfor k in ['WINE','5.91']:\n    pass\nimport re\nfor m in re.finditer(r'5\\.9\\d [A-Z]+',t):\n    print(m.group(0), t.count(chr(12),0,m.start()))\n\""
}
```


### [2026-09-07T15:55:50.468Z] TOOL RESULT

```
-1
5.91 M 368
5.92 W 368
5.93 B 368
5.91 MEAD 435
5.93 BEER 436
```


## [2026-09-07T15:56:03.158Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('SYN.txt',encoding='utf8',errors='replace').read()\nfor m in re.finditer(r'5\\.(8[0-9]|9[0-9]) [A-Z][A-Za-z ,()]*',t):\n    print(repr(m.group(0)), 'leaf', t.count(chr(12),0,m.start()))\n\" | head -30"
}
```


### [2026-09-07T15:56:04.559Z] TOOL RESULT

```
'5.80 Berry ' leaf 368
'5.81 Saur ' leaf 368
'5.82 Prpprr ' leaf 368
'5.83 VINEGAR ' leaf 368
'5.86 Mixx (sb' leaf 368
'5.87 Minx (vb' leaf 368
'5.88 CHEESE ' leaf 368
'5.89 Burrer ' leaf 368
'5.91 Merap ' leaf 368
'5.92 Wine ' leaf 368
'5.93 Brrr' leaf 368
'5.80 BERRY' leaf 427
'5.81 SALT' leaf 428
'5.82 PEPPER' leaf 428
'5.83 VINEGAR' leaf 429
'5.84 HONEY' leaf 430
'5.85 SUGAR ' leaf 430
'5.86 MILK (sb' leaf 431
'5.87 MILK (vb' leaf 432
'5.83 CHEESE' leaf 433
'5.89 BUTTER Grk' leaf 434
'5.91 MEAD Goth' leaf 435
'5.93 BEER Grk' leaf 436
'5.85 Sow (vb' leaf 1093
'5.81 Heavy' leaf 1093
'5.82 Licut (in Weight) ' leaf 1093
'5.83 Wet, Dame ' leaf 1093
'5.84 Dry' leaf 1093
'5.85 Hot, WARM ' leaf 1093
'5.86 Cop' leaf 1093
```


## [2026-09-07T15:56:07.375Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==436' SYN.txt | head -80"
}
```


### [2026-09-07T15:56:08.728Z] TOOL RESULT

```
‘fat, oint-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ment’, unguere ‘smear, anoint’, Skt, aij. ‘anoint, adorn’. Walde-P. 1.181. Peder- sen 1.46.
4. ON smjor, Dan. smgr, Sw, Smér, OHG chuo-smero (lit. ‘cow-grease’) : Goth. smairpr ‘fat’, OF smeoru, OHG smero ‘fat, grease’ (NI smear), Ir. smir ‘marrow’, ete. Walde-P. 2.690f. Falk- Torp 1086 f.
5. Lith. sviestas, Lett. sviests, perh. : Av. xsvid- ‘milk’. Walde-P. 2.521.
SCr. maslac (beside maslo ‘grease’), Boh. mdslo, Pol. masto, Russ. maslo (‘butter’ and ‘oil’) : ChSI. maslo ‘oint- ment, oil’, mazati ‘anoint’, Grk. pacow ‘knead’, etc. Walde-P. 2.226. Berneker 2.23, 28.
6. Skt. ghrta- ‘clarified butter, ghee’ : Skt. ghr- ‘besprinkle’, further connec- tions dub. Uhlenbeck 85, 100. Walde- P. 1.407.
Skt. navanita- ‘fresh butter’, lit. ‘fresh drawn’ cpd. of nava- ‘new’ and pple. of nz- ‘lead, bring’.
Av. raoyna-, raoynya- ‘butter’ (? So Barth. 1488) or ‘oil’ (Darmesteter) : NPers. rawyan ‘oil, grease’, outside con- nections unknown.
See he Aa ee ee oe
me Ot ee >
oop AND DRINK;
jgor \lreto? ON mJjQ ilu Dan. if
jydromelt Sw. mjod jdromele OE medu, h yaromel ME mede pidromel NE mead pidromel, mied Du. mee
* mid OHG metu miodh MHG met(e) medd NHG met
mez 3 intoxicating
Mead was the ee qa pate ink, made from Aon Y) : C drink, on drink among the Celtic, Ger. a and Balto-Slavic peoples, but not among the Greeks and Romans. It is regularly expressed by @ word for ‘honey’ or a derivative of it. 1, IE *medhu- ‘honey’ and ‘mead’. WaldeP. 2.261. Here, only for the drink, Ir. mid, etc., all the Celtic words; ON mjoir, OE medu, etc., all the Gme. yords (Goth. *midus not quotable, but inferred fr. a Grk. transcription pééos, referring to a drink taking the place of wine at the Hunnish court; cf. NED sy, mead), The Balto-Slavic words are partly the same as for ‘honey’ (hence alo Rum. mied), partly derivs., as SCr., Bik, medovina; but Lith. midus is fr. ne midus, and ChSl. medii is quot- able only as ‘honey’ or late for ‘wine’.
5.92
olvos kpagl Goth. wein Yinum ON vin vino Dan. vin vin Sw. vin ving OE win vin ME wine fi in NE wine tion Du. wijn min OHG win win MHG win
NHG  wein
igitized by Arya Samaj Foundation Chennai and eGangotri
COOKING AND UTENSILS 389
5.91 MEAD Goth. *midus
Lith. midus Lett. medus ChSl. (medi) SCr.  medovina
medo Boh. medovina Pol. mi6d Russ. med
Skt. madhu- was used for any sweet in- toxicating drink, especially the soma juice. Av. maéu- was a kind of wine or beer (Barth. 1114.
```


## [2026-09-07T15:56:16.695Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==437' SYN.txt | head -60"
}
```


### [2026-09-07T15:56:17.981Z] TOOL RESULT

```
 NPers. mai ‘wine’, Horn 1003). Grk. pé6v occurs only as a poetical word for ‘wine’, but is the source of the common prose words pefiw, peOicxw ‘be drunk, make drunk’, whence NG peOucpévos ‘drunk’.
2. Grk. pedirecov (Plut. Mor. 672b of the drink of the barbarians), deriv. of perc ‘honey’.
3. Late Grk. sdpopedr, cpd. of téwp ‘water’ and pédt ‘honey’, whence Lat. hydromel(t), It. idromele, Fr. hydromel (> Rum. hidromel), Sp. hidromel (also aguamel, with substitution of agua ‘water’). These words are those em- ployed to denote the ‘mead’ of other peoples, though also used of an unfer- mented mixture of honey and water.
WINE Lith. vynas Lett. vins ChSl. vino SCr. vino Boh. vino Pol. wino Russ. vino Skt. draksarasa- Av. masu-, xSudra-(?)
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
i ' | { : | ' { I } t
: vs sf
Digitized by Arya Samaj Foundation Chennai and eGangotri
390 SELECTED INDO-EUROPEAN SYNONYMS
The intensive cultivation of the vine and the use of wine as the customary alcoholic drink had its home in the east- ern Mediterranean region, whence it spread over Europe, mainly through the Romans. In ancient India and Iran wine was not one of the common al- coholic drinks. Schrader, Reallex. 2.642 ff.
1. Grk. ofvos, early fotvos, Lat. vtnum (prob. fr. *woinom, like vicus, vidi : Grk. fotos, fotéa; in which case Umbr. vinu must be a Lat. loanword), Alb. vené, Arm. gini, together with the Semitic words, Arab. wain, Hebr. yayin, all prob. loanwords fr. some prehistoric Mediterranean source. So Meillet, MSL 15.168, Ernout-M. 1111. But even so, the source could be some IE language of that region. For if we as- sume that the orig. sense was ‘vine’, it is attractively derived fr. the same root as Lat. vitis ‘vine’ (IE *wei- in words for ‘twist, wind’, see 8.67). Walde-P. 1.226. Schrader, Reallex. 2.648 f.
Lat. vinum is the source of all the other Eur. words, except the Greek and Albanian.
2. NG xpact, fr. dim. of Gr ‘mixture’, its use arising from mon Greek practice of mixing water. The use of ofvos for th the sacrament may have been & factor in its disappearance from common speech.
k. Kpaors the Com. Wine and wine of
3. Skt. draksarasa- (rare), cpd. of draksa- ‘vine, grape’ (5.76) and rasa- ‘juice’.
Av. maéu- : Skt. madhu-, etc, 5.91.
Av. x§udra-, ‘liquid, semen’ also an ‘alcoholic drink’ (‘wine’? So Barth, 555) : x8usta- ‘liquid’, xgaosah- ‘stream, flood’, Skt. ksoda- ‘swell’ (of the waves), Walde-P. 1.502. t
Among other Indo-Iranian words for alcoholic drinks are: Skt. soma-, Ay. haoma- ‘juice of the soma plant? : Skt, su- ‘press, extract’ (Walde-P. 2.468); Skt. mada- ‘intoxication’ and Av. maga- ‘intoxicating drink’ : Skt. mad- ‘be glad, be drunk’, Lat. madére, ‘be wet’, ete. (Walde-P. 2.230f.). See also under ‘beer’ (5.93).
See
5.93 BEER Grk. — (Bpiros, tis) Goth. .... Li
```


## [2026-09-07T15:56:37.509Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1114\" BRT.txt | head -5; echo \"=== maδu BRT ===\"; python3 -c \"\nt=open('BRT.txt',encoding='utf8',errors='replace').read()\nimport re\nfor m in re.finditer(r'ma[85δ]u-',t):\n    print(t[max(0,m.start()-300):m.start()+400].replace(chr(10),' '))\n    print('---')\n\" | head -40"
}
```


### [2026-09-07T15:56:38.933Z] TOOL RESULT

```
30594:12.   127  mit  Wh.  Gr.»  g  1114»,
=== maδu BRT ===
```


## [2026-09-07T15:56:42.136Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Honigwein\\|Beerenwein\\|Rauschtrank\" BRT.txt | head -10"
}
```


### [2026-09-07T15:56:42.329Z] TOOL RESULT

```
16708:HB.  254.  — 3)  VgL  ai.oidi/fl-' Rauschtrank' und  •  j.  »band- V. 'kranken'.  Praes  30  (Kaus.) •Rausch'.  -  :.)  S.  dazu  West  Av.-Gloss,  220.  \  bandaya-.  —  PPfP.  bazda-  (sbes.).
19585:(näml.  haomd)  '%?m  mtvyl  nT  am?m  nl v?n%rayn»m  .  .  Y.  5,  17";  —  pairi  ti haoma , ,  daiqmi  imqm  tansm  . .  ^waxfäi haomäi  '%ai  havanuhai  asavastai  Y.J7. 10.  2)    'Rauschtrank,  Wein';    a)  vom
19586:Haomai  vTipe  zi  anyg  *°SawAj  aaftwa fiaSnte  .  .  äat  hs  ys  kaomahe  '%6  aiä AacaiU . .  rmjaiü  (sd.)  hasmake  °%3  "denn alle  andern  Rauschtrinke  sind  von  . .  A. begleitet,  aber  er,  der  Rauschtrank  des H.  . ."  Y.  10.  8;  Yt  17.5'.  b)  sonst: dahms  hurqm  (sd.)  ifaraiti  'S?  ^asfya.- paya/ahü  N.  jo;  —  kada  ajSn  mB%r>m ahya  *°äahyä''>  yä  . .  "wann  wirst  du  den Unflat  dieses  Rauschtranks  treffen,  mit dem.."  Y-^i".!©!).  [N.jo:  lies  mi^Ue statt  mähB  ^araiti;  s.  Pü.]
19592:•  j.  iiiaSav  n.  '(Wein  uzw.)  Beerenwein'  '* : gqm^a  ..yaom?a  . .  ''iula  ansptm  V.5. 52; 53>  54iF.  7/;    —    duye  navaiti  narqm  .
24149:•  j.  vi-baoha-  Adj.  'ohne  bartka-,  ohne Narkotikum,  Rauschtrank':  dalum  kunthm banfum  'htm  ".  ,  den  ohne  Rauschtrank trunkenen"  y.ig.4
30496:•  j.  hurä-  f.  Name  eines  alkoholischen Getränks,  'Milchwein",  Kumys"':  dahmö •rqm  :faraiH  ma%d  *aspya.payar3hs  (sd.) "ein  D.  trinkt  H.  -  (d.  i.)  der  Wein  der (aus)  Pferdemilch  -"  N._jO;  —  -rayäsät  aha  . aiiavatJ  daiäyai  ä  dit  franharayat  sraolät dqhista  .  .  "er  soll  vom  Milchwein  ein hinreichend  Mass  spenden,  er  soll  es trinken  lassen  die  . ."  A.^.  4;  —  duye navaiti  narqm ..  västryaSa  gSul  vä  s^an- %ahe  z'il  'rayä  vä  *>na6Sus  vä  "..soll  er laben  mit  Fleischspeise  oder  mit  Milch- oder Beerenwein"  V.  74. 17.
```


## [2026-09-07T15:56:49.055Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/turmoil",
 "prompt": "Quote the full etymology of \"turmoil\", including any link to Latin modius / trimodia / modus."
}
```


## [2026-09-07T15:56:49.497Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/methylene",
 "prompt": "Quote the full etymology of \"methylene\" and \"methyl\": who coined it, in what year, from what French form and Greek elements."
}
```


### [2026-09-07T15:56:54.254Z] TOOL RESULT

```
# Etymology of "Turmoil"

Based on the provided content, here is the full etymology:

**Turmoil (noun)** dates to the 1520s, meaning "distracting confusion; tumult, disturbance, and trouble." The origin is uncertain, though the term appears earlier as a verb (1510s, also spelled _turmoyle_).

The most plausible explanation suggests it may derive from an alteration of French _tremouille_, referring to a "mill hopper" — a device in constant back-and-forth motion. The word "moil" may have also influenced its development.

**Regarding Latin connections:** The document does not mention any link to Latin *modius*, *trimodia*, or *modus*. The etymology provided focuses on French origins and the possible influence of "moil" (which traces to Old French _moillier_ meaning "to wet, moisten").

The verbal sense of turmoil is now obsolete, though the related adjective _turmoilous_ appeared in the 1550s.
```


### [2026-09-07T15:56:55.866Z] TOOL RESULT

```
# Etymology of Methylene and Methyl

**Methylene** was coined in 1835 by French chemists Jean-Baptiste-André Dumas and Eugène-Melchior Péligot. According to the source: "from French _méthylène_ (1834), coined by Jean-Baptiste-André Dumas (1800-1884) and Eugène-Melchior Péligot (1811-1890) from Greek _methy_ 'wine'...+ _hylē_ 'wood'...+ Greek name-forming element _-ene_."

The compound was so named "because it was detected in wood alcohol."

**Methyl** derives from this same coinage. The etymological breakdown explains that "The breakdown of _methylene_ into _methyl_ and _-ene_, and the identification of the last syllable of _methyl_ with the general suffix _-yl_, led to the use of _meth-_ as a separate combining-element."

Thus, both terms originated from the same 1835 French innovation by Dumas and Péligot, combining Greek roots meaning "wine" and "wood" with the chemical suffix "-ene."
```


## [2026-09-07T15:57:05.555Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN turmoil ===\"; grep -n -i \"turmoil\" KLN_1966.txt KLN_1971.txt SKT.txt FSD_vol4.txt WEB_vol1.txt 2>/dev/null | head -8; echo; echo \"=== AHD TURMOIL ===\"; grep -c \"TURMOIL\" AHD_watkins1985.txt"
}
```


### [2026-09-07T15:57:05.622Z] TOOL RESULT

```
=== KLN turmoil ===
SKT.txt:20313:Turmoil.  *b.  (F.  ?  -  L.  ?)  Formerly turmoyl ;  probably  a  corrupt  form,  the latter  part  of  the  word  being  as&imilaCccI to  nioil,  q.  V.  :  and  the  former  part  to turn.  Prob.  from  F.  trtmouifU,  '  llie hopper  of  a  mill.'  also  called  tramcul (Cotgra>-e)  ;  also  spelt  tremoie,  trtmuyt (Rotiuefort).  (Ihe  (onn  tranuul  is  sutTi- ciendy  ncar.l  3.  So  named  from  t'cii^g  in cootioual  motion.  — L.  trtmert,  to  ticmble, shake.     CC  prov.  £.  trttnmU,  lu  tremble.
WEB_vol1.txt:22518:[Fr.] in Europe, one who frequents the boule- vards, particularly those of Paris; a man about town. bou-le-vérse/ment (Fr. pron. bél-vers-min’), n. [Fr. bouleverser, to overthrow.] turmoil; a complete overthrow; disorder; revolution. bou-lim/i-a, n. same as bulimia. boult, n. same as boll. boul’tel, n. same as boltel. boul’tér, n. a long, strong line for deep-sea fishing, having many hooks attached; a trawl: also spelled bolter. boun, a. [ME. boun; Ice. buinn, ready, pre- pared, pp. of bna, to till, prepare.] ready; pre- pared. [Obs.] boun, v.i. and v.i. to prepare (oneself); to get ready. [Archaic.] = bounce, v.i.; bounced, $t., pp.; bouncing, ppr. (ME. bounsen, bunsen; D. bonzen, to bounce, throw.] , 1. to leap or spring; to rush out suddenly. Out bounced the mastiff. —Swift. 2. to spring or leap against anything, so as to rebound; to bound or rebound, as a ball. 3. to boast; to brag. [Brit.] 4. to move in a sudden or noisy rush. bounce, v.!. 1. to cause to bound or rebound; as, to bounce a ball. 2. to bump; to thump. 3. to discharge from employment. [Slang.] 4. to put (a person) out by force. [Slang] bounce, 7. 1. a sudden spring or bound; a re- bound.
WEB_vol1.txt:25375:bus’tle (bus’sl), v.i. and v.t.; bustled, pt., pp.; bustling, ppr. [Ice. bustla, to bustle, splash; busil, a splashing, turmoil.] to move quickly, busily, fussily, often with rudeness, noise, or commotion.
WEB_vol1.txt:36732:coifed (koift), a. wearing a coif. coiffe, n. same as col. : coif-feur’ (kwii-fir’), n. [Fr.] a hairdresser. coif-fure’ (kwä-), n. [Fr., from coiffer, to dress 7 the head.] the arrangement of the hair; the style of dressing the hair; a headdress. , coign, coigne (koin), n. [var. of coin, quoin.]a projecting corner. Eas Bete. coign of vantage; a position of advantage for observation or action. a, coil, v.t.; coiled, $t., Pi coiling, ppr. [OFr. coillir, to gather, pick; L. colligere, to gather together.] j 3 f 1. to gather (a line, rope, etc.) into a cir- an form; to wind into a ring or spiral orm. 2. to gonis aes gih or as with coils. 3. to gather up close. [Obs. coil, vi. 1. to wind or twine around some- thing, as a vine around an oak tree. gate form rings or coils, or to move in a winding course. coil, n. 1. anything gathered into a series of rings or spirals; in nautical usage, a single turn cr wining ote rope is called a fake, and a pile of fakes is calling a fier. 5 2. a series of nes or spirals. 3. a single turn of a coiled figure. 4. in plumbing, a series or group of con- pected pipes in spirals, rows, or layers, as in a am-heating radiator. 5. in electricity, (a) a spiral of wire; (b) any device consisting essentially of such a spiral. Keon minna a radio antenna wound in the m of a coil. Flemish coil; among sailors, a coil of rope laid flat and forming a sort of mat. col [Early Mod. Eng., from OFr. acueil, x i 1sion, etc.] commotion; turmoil. [Archaic.] Sepee ae gathered into a circular form, as a gelon n. a cullion. [Obs.] coin, n. [ME. coyn, coyne, coin; OFr. coin, a wed wedge] iD, die, also a corner; L. cuneus, a A: a cornerstone; wedge; quoin; coign. aad piece of metal with a distinctive stamp, Ropes WEED pai weight, issued by a t and used as money. L such pieces collectively. z Y: [Slang.] : ip le used for stamping money. A pay one back in his own coin; to retaliate coin p tO give tit for tat. “to make (come) Pl, bp-i coining, pr: 1. (a) ins stamping metal; to mke (metal) into Gone ee 3 5 make up; devise; invent, as a new poor Phrase, ” be ve m money; to make money rapidly; to {Colloq} Successful or fortunate financially.
WEB_vol1.txt:38507:Ob n. compassion; pity; remorse cém’/mSbt, cöm’mõte, x. [V ; Wales, formerly one of ‘che i er al ivisi rea ar tical LOO, usually a subdivision of a eee cdm-mO6te’, v.t. to stir in tate; to disturb. [Rare.] cém-m0/tion, n. [L. commotio, a tion, from commotus, . of s pp. o move, disturb; com-, together, move. ] 1. a violent movement; commotion of the sea. 2. tumult of people; disturbance; di 5 as, the il in the schoolyard. sarees - perturbation; disorder of mind: 3 citement. [Obs.] ma hearin Syn.—agitation, tumult, turmoil, disturb- ance, perturbation.
WEB_vol1.txt:42212:Syn.—agitation, commotion, tumult, dis- turbance, turmoil, tremor, perturbation, throe.
WEB_vol1.txt:92997:2. to cast down; to over —Pope, 3. toutter with Seher an answer to a charge. 188, to hurl back hūrl, v.i. 1. to throw or fli person or thing). ng something (afa 2. to move with force or [Archaic.] 3. in baseball, to pitch, [Slang ] 4. to play the game called hurlin 5. to be wheeled. [Scot.] 8. hirl, n. 1. the act of throwing wi A a sionn throw or fling. ing with violence; . tumult; riot; commotion, 3. the stick used in the pee ii hūrl’bat, n. 1. a whirlbat; an old king’ weapon. [Obs.] $ ind of 2. a bat used in the game s htrl’bone, z. a whitlbanes of hurling, aure n. one who hurls or who play. urling. hirl’ey, hirl’y, n. 2. a hockey stick, hirl/ing, n. 1. a throwing with force 2. a ball game in which opposing sides o parties try to hurl or force a. ball through their opponents’ goal, or to deposit it at some designated spot at a distance; in Ireland, the game is the same as field hockey. j hūrl’wind, ». a whirlwind. [Obs.] huriy, n.; pl. htir’lies, uproar; turmoil, con- S1 . hir’ly-bur’ly, n.; pl. htir’ly-btir’lies, (prob, extended from hurly.) a turmoil; uproar; hubbub; confusion. hir’ly-bir’ly, a. disorderly and confused. Hüū’rðn, n. [Fr., a coarse fellow, ruffian, from hure, unkempt fe member of a confeder- ation of Iroquoian Indian tribes that lived between Georgian Bay and Lake Ontario, Canada: also called Wyandot. Hū’röðn, a. of the Hurons. hurr, v.i. to make a sound like rolling the let- ter r; to buzz. [Dial.] i hur-ra/, interj., n., v.i. and v.i. same as hurrah. hur-rah’, interj. [G. hurra; Dan. and Sw. hurra, hurrah.) an exclamation expressing ap- proval, joy, or exultation. 4 hur- räh’, n. a cheer; a shout of approval, joy, or exultation. hur'räh’, v.i. to cheer; to shout hur-rah/, v.l. to greet, encourage, with shouts of “hurrah.” i hur-ray’, interj., n., v.t. and v.t, same as hurrah hir’ri-cine, n. [Sp. puree a hurricane; W. Ind. (Taino) kuracan, z ; 1a soln cyclone with winds moving from 70 to 100 miles an hour, usually RE panied by rain, thunder, and lightning: ricanes generally occur in the trome and 2. anything like a hurricane in or speed; violent outburst. Syn.—gale, storm, cyclone, torna hiir’ri-cane bird, the frigate bird. hiirri-cane deck, the top deck of ship plying inland waters. hur-ri-ca’no, n. a hurricane; a
WEB_vol1.txt:110861:2. any place of turmoil, noise, and confu-

=== AHD TURMOIL ===
0
```


## [2026-09-07T15:57:16.469Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"مدل\" \"مدرن\" \"کمد\"; do echo \"=== $w ===\"; grep -n \"$w\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -4; done"
}
```


## [2026-09-07T15:57:16.481Z] TOOL CALL #56: WebSearch

```json
{
 "query": "français trémie trémouille étymologie latin trimodia modius trois modii"
}
```


### [2026-09-07T15:57:17.683Z] TOOL RESULT

```
=== مدل ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:17446:کستاز ارشننع: ده (مدلتصه(م22- [- 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:19743:کاویدن: مدل-2۲ از: کاو + ملد ن» بسد. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:23198:کش امدلن: ۱ -(۵۵) ۱:۱5 (مص‌ل.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:43006:ماله: (مدلق« (امص.) مالش مالندگی. 
=== مدرن ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:51717:مدرن: ۵06۲ (ص.) تازه؛ نو. بات روز. 
MON_part1.txt:36823:تازیانه: (م)‌ممدرنه [- تازانه] (.) آنچه 
MON_part1.txt:93496:طسخ کر دن؛ حدلتمدرن۲ه۱ [ع. . ف.] 
MON_part2.txt:51717:مدرن: ۵06۲ (ص.) تازه؛ نو. بات روز. 
=== کمد ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:26321:کمد؛ 04ص«هم! (ا.) کنجة دارای کشو که در 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:26327:بایگانی: کمدی که در آن پرونده‌های اداری 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:26328:را بایگانی کنند. کمد جا لباسی: کمدی که 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:26331:کمدی: ۵7 (.) (نم.) اثر نمایشی که
```


### [2026-09-07T15:57:26.258Z] TOOL RESULT

```
Web search results for query: "français trémie trémouille étymologie latin trimodia modius trois modii"

Links: [{"title":"Définition de trémie | Dictionnaire français","url":"https://www.lalanguefrancaise.com/dictionnaire/definition/tremie"},{"title":"trémie — Wiktionnaire, le dictionnaire libre","url":"https://fr.wiktionary.org/wiki/tr%C3%A9mie"},{"title":"trémie | Dictionnaire de l’Académie française | 9e édition","url":"https://www.dictionnaire-academie.fr/article/A9T2093"},{"title":"Définitions : trémie - Dictionnaire de français Larousse","url":"https://www.larousse.fr/dictionnaires/francais/tr%C3%A9mie/79392"},{"title":"Littré - trémie - définition, citations, étymologie","url":"https://www.littre.org/definition/tr%C3%A9mie"},{"title":"Trémie | Définition du dictionnaire français","url":"https://www.dicocitations.com/definition_littre/29147/tremie.php"},{"title":"Définition de trémie | Dictionnaire français","url":"https://www.dicocitations.com/dico-mot-definition/136978/tremie.php"},{"title":"trémie - Dictionnaire - Thesaurus","url":"https://thesaurus.altervista.org/dict/fr/tr%C3%A9mie"},{"title":"TRÉMIE : Etymologie de TRÉMIE","url":"https://www.cnrtl.fr/etymologie/tr%C3%A9mie"},{"title":"Trémie : Définition Trémie","url":"https://www.dico-definitions.com/dictionnaire/definition/29147/Tremie.php"}]

I found comprehensive information about the etymology of the French word "trémie" and its variants. Here's what the search results reveal:

## Etymology Summary

The word comes from Latin "trimodius" (a measure of three muids), combining "tres" (three) and "modius" (muid). It evolved into "trimodia" via "trimodium".

## Regional Variants

The word later transformed into different regional forms such as "tremouille," "tremue," "tremuée," "tremueia," "tramuja," "tremonha," "tramoggia," and in Late Latin "tremellum," "tremula," "tremoea," "tremuta," and "treumia".

## Competing Etymological Theories

There are two competing theories about the origin:

1. **"Tres modii" (three muids)**: Some believed that "trémie" represented "tres modii" (three muids), but Scheler believed that "tre" represents "tremere" (to tremble), suggesting the trémie is the trembling bushel.

2. **"Tremere" (to tremble)**: The forms "tremellum" and "tremula" indicate Latin "tremere" (to tremble), with the trémie being in continuous trembling.

## Historical Usage

The form "trémie" appeared from the late 11th century onwards through various stages: judéo-French "tremuie" (late 11th century), Old French "tremuie" meaning "funnel for grain in a mill" (1234-40), Middle French "tremie" (1412-13), and later meanings including "space reserved in a floor for a chimney hearth" (1437) and "bird feeder" (1680).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T15:57:34.672Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^مدل\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -5; echo \"--- context مدرن/کمد ---\"; sed -n '51715,51720p' MON_part2.txt; echo ---; sed -n '26319,26323p' incoming/MON/MON_2vol_Adena_v2_djvu.txt; echo \"--- search مدل headword ---\"; grep -n \"مدل:\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head"
}
```


### [2026-09-07T15:57:34.796Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v2_djvu.txt:45012:مدلل. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:47502:مدلل. استوار شده: برقرار. ثست شده؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:47510:مدلل سازنده. استو ار کننده. شت کننده؛ ج. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:51830:مدل: )0۵01 [ع.] (افا.) دلالت کننده؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:51833:مدل: ۱ع00« (.) الکو نمونه» سرمشق. 
--- context مدرن/کمد ---
(اسفار ج ۱ ص ۲۷ فرع. سج.) 

مدرن: ۵06۲ (ص.) تازه؛ نو. بات روز. 
ضح.- بسیاری از استعمال این کلمةٌ بیگانه 
احتراز دار ند. 

---
کمتر از همه اقل همه؛ مق. بیشترین. 
کوچکترین» حقیر ترین همه. ناقصترین. 
کمد؛ 04ص«هم! (ا.) کنجة دارای کشو که در 


--- search مدل headword ---
incoming/MON/MON_2vol_Adena_v2_djvu.txt:51830:مدل: )0۵01 [ع.] (افا.) دلالت کننده؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:51833:مدل: ۱ع00« (.) الکو نمونه» سرمشق. 
MON_part1.txt:32499:مدل: -۲0]07 (مص‌ل.) ببرون زدن 
MON_part1.txt:37489:تمدل: امتهاها [ع.] (مصل.) خوشرویی 
MON_part2.txt:51830:مدل: )0۵01 [ع.] (افا.) دلالت کننده؛ 
MON_part2.txt:51833:مدل: ۱ع00« (.) الکو نمونه» سرمشق.
```


## [2026-09-07T15:57:46.532Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9dhu",
 "prompt": "Give the reconstruction, gloss and descendants for PIE *médʰu, especially Proto-Iranian/Avestan, Sanskrit, Greek, Sogdian and Persian reflexes. Quote verbatim."
}
```


## [2026-09-07T15:57:48.282Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%DB%8C",
 "prompt": "Give the Persian etymology section(s) for می — specifically the noun می 'wine': Middle Persian form, Proto-Iranian, PIE root, and cited sources. Quote verbatim."
}
```


### [2026-09-07T15:57:48.593Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T15:57:52.936Z] TOOL RESULT

```
# Persian Etymology for می (wine)

**Middle Persian form:**
"[script needed] (HS) / [script needed] (mdy /⁠may⁠/, "wine")"

**Proto-Iranian:**
"*mádu" from Proto-Iranian language

**PIE root:**
"*médʰu" ("honey, mead") from Proto-Indo-European language

**Cited source:**
"Edelʹman, D. I. (2015), Etimologičeskij slovarʹ iranskix jazykov [Etymological Dictionary of Iranian Languages] (in Russian), volume 5, Moscow: Vostochnaya Literatura, page 116"
```


## [2026-09-07T15:58:02.500Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%85%D8%A7%D8%B1\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/med-\" \"https://www.etymonline.com/word/turmoil\" \"https://www.etymonline.com/word/methylene\" \"https://en.wiktionary.org/wiki/%D9%85%DB%8C\" \"https://www.cnrtl.fr/etymologie/tr%C3%A9mie\"; do timeout 180 python3 tools/fetch_source.py \"$u\" --note \"pdf page 324, roots Me 2 / Medhu: bimar, med-, turmoil<modius, methylene, may, tremie<trimodia\" 2>&1 | tail -2; done"
}
```


## [2026-09-07T15:58:04.046Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9d%CA%B0u",
 "prompt": "Give the reconstruction, gloss and descendants for PIE *médʰu — Proto-Iranian, Avestan, Sanskrit, Greek, Sogdian, Persian reflexes. Quote verbatim."
}
```


### [2026-09-07T15:58:07.694Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f6978c2ce536a231.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6feca935efe4f49a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b88ac36cf044dfb7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7e3a40a06505a38e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a3db22f19244fc49.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6168722bd761cd99.txt
```


### [2026-09-07T15:58:13.544Z] TOOL RESULT

```
# PIE *médʰu: Reconstruction and Descendants

**Reconstruction & Gloss:**
The Proto-Indo-European root is **\*médʰu** (neuter noun), meaning "honey" or "honey wine, mead."

**Key Descendants:**

- **Proto-Indo-Iranian:** \*mádʰu ("honey")
- **Sanskrit:** मध्वद् (madhvád, "honey-eater")
- **Avestan:** (descended from Proto-Indo-Iranian)
- **Greek:** Proto-Hellenic \*métʰu (see descendants)
- **Sogdian:** 𐼺𐼴𐼹 (mwδ /muδ/), possibly borrowed form
- **Persian:** (descended from Proto-Indo-Iranian branch)

**Additional Notes:**
The word is "athematic, proterokinetic" in inflection. It possibly derives from Proto-Semitic *matḳ- ("sweet") or Proto-Northeast Caucasian *miʒʒV ("sweet"), suggesting ancient borrowing. The term spread across Indo-European languages including Celtic, Germanic, Balto-Slavic, Anatolian, and even influenced non-Indo-European languages like Etruscan and Chinese.
```


## [2026-09-07T15:58:23.101Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19525,19545p' SOD_pages.txt"
}
```


### [2026-09-07T15:58:23.148Z] TOOL RESULT

```
5510 mw6' B,S                                                      magians
                                  (Jja :^Jais uU^)\^ tj*jj         BSTii 851.6, 843.41, 50, 850.1, 872.4; C2 gloss.
     mu5/mu5
     value, price
                                                              5521 mwyztw M
     VJ 1401; mw6yy VJ 1319; Anc. Lett. 5; S W,
       BSOAS 1983, 45                                              muy-zatu ©*magu-zati
                                                                     p215
                                                                   magian killing, magophonia
5511 mw62 S                                        (ji)^
     mu6 (mwd) *=»m5w                                              Hen. Magi. 138.27, 135f
     wine                                                     5522 mwhbt1 =» mwypt(w)
     GMS 408-, Anc. Lett. 4.6; Sund. AoFviii 1981             5523 mwhrdyb M                                        *A>j$*
       p2l6, 2aV2                                                  muhr-5ip ©*mwdr\ Parth. ©ob. -yy
                                                                                                                 ^m^mm
                                                                                  ^m
                                                                                                                 mwrtk (y)
  221

          -^mw^kk, dyb-yy                                              mwrt^zw^ntyk^k, jw'ndyCy)
          seal of letter                                             resurrection
```


## [2026-09-07T15:58:35.019Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT azda ===\"; grep -n \"azdā\\|azda\" KNT.txt | head -6; echo \"=== LEW modus ===\"; grep -n \"^modus\\|^medeor\\|modus,\" LEW_1910.txt | head -6; echo \"=== LAT modus ===\"; grep -n \"^modus\\|^medeor\" LAT.txt | head -6; echo \"=== IEC med ===\"; grep -n \"^med-\\|^medos\\|^modos\\|^medhu\" IEC.txt | head -10"
}
```


### [2026-09-07T15:58:35.102Z] TOOL RESULT

```
=== KNT azda ===
334:II. Avestan is the language of the Avesta or sacred writings of the Mazdayasnians, known also as Parsis (ie. Persians) and as Zoroastrians or followers of Zoroaster, the prophet who pro- claimed the religion. It consists linguistically of two parts: an older part containing the (402/8 or metrical sermons of Zoroaster himself, and the Later Avesta, differing in a number of linguistic features from the Gi0a’s. Zoroaster himself came from the northwest, but his successes in convert- ing to his faith were made in the northeast, in Bactria; it is therefore disputed as to whether Avestan is a northwestern or a northeastern lan- guage. It is noticeable that it agrees rather with Median than with OP, but this is not decisive.
464:18 а d' L 36, du КІ-Н 46 19 m n Rk 23 20 m nu КІ 46 1 р р G 02 22 f Зб 02 З | b Bf-L 36 24 m mRk2 25 mi ‘m L 36, m? L 39, mi RI-H 46 20 т" mu КІ 46 27 y y B-J 38 28 m r G02 20 т" sr G 15, 7” J 38, ru RI 46 30 А l Op 51 3l w w L 36, va RLH 46 32 v! v SM 23, vi КІ-Н 46 jd F s G 02 94 $ sch G 02 85 2 z Bf-L 36 96 № h B-J 38 Ideograms and Ligature 37 XS ‘König M-G 02 8 DH Ча L 45 39 BU ‘Erde’ L 45 40 AM ‘Ahuramazda’ Op 74, E 90 4| BG бода ‘god’ Sc 1929 42  AMha Auramazdé Sc 1929, Auramazda- ha Br 1932 (cf. Hz 1931) Word-divider 43: Ty 1798
641:$2. Tue InEoGRAMS are five in number, stand- ing respectively for s8dyabiya ‘king’, dahydus ‘province’, bümi$ ‘earth’, Auramazdá ‘Ahura- mazda’, and baga ‘god’; they are transcribed by Хо, DH, BU, AM, BG. In DSk 4 there is what seems to be a ligature for AM-ha,
659:АзРа has zšāyaðiya, DH, būmām (sc) and BUyé, Auramazdā, baga; a state of variation which is attributable to the inaccuracy of OP writing at this period. $3. NumeRars: The cardinals are not written
664:reliability of the copyist is confirmed by similar omissions in DSy, our text of which has been read from a carbon rubbing of the original.’ In other inseriptions omission of the divider 1s ex- tremely rare: examples are yadimaniyaiy XPh 47 = yadi(y) : maniyü(hayiy, and upà Artarsa- юат) Si. The gen. Auramazdàha is replaced in XPe 10 by Aurahyá Mazdaha, with declension of both parts of the compound, but no divider.
737:П. The -1- may be omitted in final -aiy: | Auramazda-tay DB 4.58, for -іату. mantyahay DPe 20, for -haty. ula-may A’Sde 4, for uta-maty (which is in db). Cf. forms of düraiy, with enclitic apiy (5186).
=== LEW modus ===
=== LAT modus ===
26051:modus, d^rivd par les granaairiens da pcp. fatur passif gerundus "node
36938:medeor
36970:medeor.
36971:medeor, -eris, pas de parfait, mederi: donner ses soins a (com-
37132:modus etait senti par les Latins, cf. P.F.110,26 medioximum, mediocre,
38497:modus, -I m. (contamination de deux noms differenta; l'un, de aena
=== IEC med ===
10429:medos, -es- ‘measure’. Cf. modos, ios and
10449:medhu ‘sweet drink, liquid honey, meag’. Cf. midhu & melit. WP II, 261 Skt. mádhu; Av. maðu ‘honey, mead’; Per.
10452:medhuo, medheuo ‘fill with honey or mead, intoxicate; be intoxicated’ Sk. cf. madhvasyami ‘long for honey’; Gk. methúð ‘be drunk, be tipsy’; Br. mezvi, inf. ‘intoxicate’; W meddwi, inf. id.; Cz. cf. medo- vat, inf. v. ‘gather honey’. See medhu above
10453:medhuolos (medhuälo-). See medhu above Skt. madhvalah, m. (carousal'; W meddwol ‘intoxicating .
10977:modos, -es- ‘measure, means’. Cf. méd-. WP II, 259
```


## [2026-09-07T15:58:38.664Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10425,10455p' IEC.txt; echo \"==== modos ====\"; sed -n '10975,10985p' IEC.txt; echo \"==== LAT medeor ====\"; sed -n '36965,36985p' LAT.txt; echo \"==== LAT modus ====\"; sed -n '38495,38520p' LAT.txt"
}
```


### [2026-09-07T15:58:38.749Z] TOOL RESULT

```
740
‘measure, tell, try’; OE metan, Du. meten, ON meta, Sw. mäta ‘measure, estimate’; cf. OS metod ‘fate’; OE metod, id. beside metten (a ‘Fate’); o-gde in metgian ‘moderate, govern’; ON mjọtuðr ‘dispenser of fate, judge, ruler; bane’; mjọt, npl. ‘due measure’; met, npl. ‘weights; OE met ‘measure, share, rule, means’; Du. meet, f. ‘mark, measure’
medo (2) ‘treat, remedy’. Same as (1) (?). Cf. medos Av. mad-, mað- ‘treat, cure’; maóo0, m. *medi- cine, science’; Lat. medeor -éri ‘heal, remedy’; cf. re-medium ‘remedy’.
(med- (3) of uncertain background for W medd, 3s. “he says? and W meddu, v. “possess; be able’)
medos, -es- ‘measure’. Cf. modos, ios and
medo (1) for most forms, but cf. Olr. mess, m. (judgment, fr. *medes-); OHG mëz, n. “measure, extent, aim, direction’; OS gi-met, n. ‘measure’; un-met ‘excessively’; G Metze, f. *milling-fee'; Du. meet, f. “mark, measure’; Sw. mát, m. 'distraint, seizure’; LW in Finn. mitta ‘measure’. O-gde in Lat. modius *milling-fee'; Latv. mazs, m. id., but MHG métze, OHG mëzzo (e-gde), id.
médos, ios, io, us ‘remedy, means’. Cf. medo (2). WP II, 259 Skt. cf. (alleged) vi-madah; Av. vi-maóas, -ah-, n. “medical treatment; Per. maye ‘wealth, Stock, matter’; Gk. médos, gs -eos, n. ‘care, deliberation’; Lat. cf. re-medium, n. ‘remedy’; Br. mz pl. -u “expense, outgoings’; MHG mas, sn. ‘measure’; OE mate, adj. (2) ‘proper, meet'; Du. maat f. “measure, size”; Fris. miet, s. ‘rule, ruler, marker’; Norw. måte ‘way, man- ner’; Sw. måtta, f. ‘measure’; ON máti “man- ner beside mæti, n. ( price, value’; pl. 'ameni- ties); mætr, adj. ‘fine’
medros, å, (medər-) ‘joyful; joy”
Skt. madrám ‘joy’; madirah “exciting, exhila- rating’; OIr. medair, s. ‘enjoyment’; Ir. mea- dhar, f. (2) “joy”
medheuos (medhuos, medhus) ‘honeyed, soaked in honey or mead, tipsy’. Cf. medhu, etc. WP II, 261 Skt. cf. mádhavah “an intoxicating drink’; mádhuh “sweet'; Ir. meadhbh ‘fed on mead:
741
fuddled'; W meddw ‘tipsy’; Cor. medhow, Br. mezó, id.; OCS medovü ‘honeyed, sweet médhigos, à “extract, sap, whey, sour milk, juice, essence'. (Variant moidhigos beside més-, mois-^). Skt. cf. médhajah ‘from sacrifice’ beside mé- dhah “juice, essence’; MIr. medg ‘whey’; Ir. meadhg, gs meidhg & mídhg, m. id.; Gallo- Lat. mesga id. (LW in Fr. mégue); OBrit. meid, id.; W maidd, Cor. myth, m. id.; EMDu. cf. meij-kaas ‘curds’; Sw. cf. mes-ost ^whey- cheese’; OCz. miezha, Cz. míza, Pol. miazga (‘sap’, fr. *mëdhiga). (Origin of G Matte un- certain) medhianos (medhionos) *midmost'. See fol- lowing entries Skt. cf. madhyanyah (sic), id.; Per. miyan ‘inside; between; waist, middle; miyane “middle; between’; Kurd. mijan (mi£an) *front-half of plough-beam'; Arm. mi£in, gs miéno, o-st “midmost'; Gk. cf. mesiáne, f. (intermediate layer of cement or sim.); Alb. mi, gs mie ‘heartwood’; Lat. medianus *mid- most'; Mir. medón, Ir. meadhón, meodhan, m. ‘middle; W mewn, prp. ‘inside’; i mewn, adv. id.; OE cf. on middan “in the middle ON meðan ‘meanwhile’; R cf. meZeni, f. *mid- summer”; Cz. cf. mezenec, m. ‘middle finger” medhiol- (medhil-, medhol-) Lat. cf. medulla *marrow, pith'; Ir. méadal, f. ‘paunch’; MHG mittel, adj. & sf., sn. *mid- die; OE middel, adj. & n. id.; ON meðal, miðil, in the phrr. á ~, í — “amid, among medhiomos (medhimo-, medhoamo-) "mid. most. WP II, 261 Skt. madhyamáh; Av. maóomo; Oss. mídámá, adv. ‘inward’; Gk. méson, adv. ‘between’; Alb. i mesëm “midmost? beside ndér-mjemé ('in- termediate’, fr. *enter-medhom-); Osc. messi- mass, fpl.; Go. miduma, f. id.; OHG mittamo, mëtemo ‘mediocre’; OE medeme, meodume, id.; ON mjóóm, pl. mjaómir, f. ‘waist’; Sw. cf. medan ‘while’; MHG mitten, mittene, id. medhio-nokt- *midnight Gk. cf. meso-nüktion, mesa-^; Alb. mes-naté; Romance in It. mezzanotte, Rumansch mez- zanot; OFr. & Fr. minuit; OW meinoeth; MHG mitte-naht; OE midde-neaht, -niht; ON
medhigos, à — medhu
20
25
30
35
40
45
742
mió-naetti, id. (Cf. also Skt. madhya-dityab, “high noon’: Alb. mes-dit8 *midday); lr. miodh-nocht, as ON
medhior- (medhiar-) ‘midmost; middle, centre Gk. cf. meséres *midmost, internal; Alb. (me- tath.) zemër ‘heart’, (cf. also Alb. parzém, par- mëz, f. “breast, bosom’; Gk. promesó-, cpds. *middle-); Cz. mezera, Slovak medzera *space, interval
medhios, à, io ‘middle; midst, centre’. WP II, 261 Skt. madhyah, adi. madhyam, n.; madhyá, adv. “in the middle’; Av. maióyo, adi: Oss. mid-, Dig. med- ('inside-, cpds.); cf. medág, adj. ‘inner’; Lyc. postp. (queried) miïtə “in- side’; Arm. meg, i meg "mm: meðk E mg£, gs mi£o, o-st. ‘middle, waist; Gk. mésos, més- sos, adj.; Myc. cf. mesato- (queried: "mid. most); Phryg. (Hes.) mézea, npl ‘genitals’; Alb. mes & mez, def. mezi “middle, waist, interval; meze, f. (setting, milieu', fr. *me- dhio); Lat. medius, adj.; cf. ni-mis ('exces- sively’, fr. *ne- *medhs- ? or -meds?); Osc. mefiaí, loc. sg f. ‘middle’; MIr. mid, adj. (‘half , cpds: ‘mid-’); Gaul. medio-, Sequanian mid-; W medd, m. ‘centre of motion, pivot’; Go. midjis, adj.; MHG mët-, cpds.; OE midd, midde, adj. & sf; OS middia, f. (middle: Ir. midhe, f. id.); ON miója, id. beside mióju “in the middle’; miór, adj.; Sw. midja, f., Norw. midje ‘waist; OCS mezda f. beside meZzdu ‘between’; Slovene medja *borderland'; Li. (?) cf. medis, gs medžio ‘tree’; mede ‘wood’; Latv. mežs (forest. (Note that Li. medžio vidus: E mid-wood with the terms reversed!) Cf. also some Lat. cpds. with mer-, cf. mer- idiés ‘midday’; mer-enda ‘snack meal’, if for *medh-edna, and mer-cedonius ménsis 'inter- calary month'
medhtos (mettos), see medhuo and next Skt. mattáh (2) ‘drunk’; Per. mast, id. (Iso- phonic: Ir. meath ‘weak, faint? adj.; ‘decline’, m.; W meth, pl. -ion, m. ‘failure’; methu, inf. ‘fail, miss, decay, perish’
medhu ‘sweet drink, liquid honey, meag’. Cf. midhu & melit. WP II, 261 Skt. mádhu; Av. maðu ‘honey, mead’; Per.
743
may ‘wine’; Oss. mid, mud ‘honey’; Tokh. B mit, id.; Gk. mæthu ‘wine’ beside méthé *drun- kenness'; cf. més-pilon, -pile (“medlar”, if for *medh- *honey-ball'); LLat. medus Cmead, from a Gmc. source); Umb. cf. (?) mefa “cake, of honey?; Olr. mid, cpds. med- ‘honey’; medb, adj. 'intoxicated'; Ir. meadh, f. as Olr. mid; meadhbh ‘drunk; (*-e- míodh, f. *mead'; OBr. med, Br. mez, m. Cor. méth, m. ‘mead’ beside Br. mezó, mezw ‘drunk’; Cor. medbow, id.; OW med, W medd m. ‘mead’; meddw, adj. ‘drunk’; Go. (in Greek documents) médos ‘mead’; OHG méto, mitu, métu, m. id.; MHG mit, id.; G Met, m. id.; OE medu, gs medwes, m. & n ‘mead’; Du. mee; Fris. mied, wd: ON mjoór gs mjaðar, ds miói, m. id.; Sw. mjód, id.; OCS medü (and com. SI.) ‘honey’; Li. medüs, m. id; Latv. medus, m. id.; OPr. medó (*medu), id. Extensions: (type *medhutios) Gk. méthusos ‘tipsy’; Li. medütis, gs medücio, m. ‘nectar’; (type: medhu-éd-): Vedic madhvad *honey- eating; OCS medvědů and com. SI. ‘bear
medhuo, medheuo ‘fill with honey or mead, intoxicate; be intoxicated’ Sk. cf. madhvasyami ‘long for honey’; Gk. methúð ‘be drunk, be tipsy’; Br. mezvi, inf. ‘intoxicate’; W meddwi, inf. id.; Cz. cf. medo- vat, inf. v. ‘gather honey’. See medhu above
medhuolos (medhuälo-). See medhu above Skt. madhvalah, m. (carousal'; W meddwol ‘intoxicating .
megstis (mesgtis) ‘meshing, mesh, entangle- ment. Cf. mesgo (1) W mais, pl. meisiau, f. ‘contraption, device’; Li. cf. mégsti, v. ‘knit, knot; magstas, m. *knit- ting-needle
mégho "be pleased, rejoice’. See next Skt. mahe, mp., mahiye, mp., ‘rejoice’; mahá- yāmi ‘cheer; OLi. mēgmi, Li. mēgstu, inf. megti ‘like’; Latv. cf. (?) mēdzu, mēgt ‘be fit, be used to, be able’; cf. also Skt. maghám, n. ‘reward, bounty’
==== modos ====
mod- (mod-) ‘against, towards; encounter, approach, contact, fitting, composition'. Cf. WP II, 304 Arm. mutk, gp mtic, ab. pl. -iwk (a singula- rized pl: approach"); h-mut, gs h-mti, ab. sg. h-mtav ('skilfuP, fr. *su-mod-); cf. (r-gde) mat- čim, v. (approach, fr. *modsKo); (r-gde also in) Hitt. mac(mi) ‘oppose’; Go. ga-motjan, v. “meet? beside ga-motan, v. ‘be obliged"; mota, f. ‘toll; (DW in OCS myto, id.); OS motan, v. ‘find room’; OFris. mota “have to, need to, be able to'; OHG muoza, f. (chance, facility’. Cf. G Müsse, müssig); muoz ‘I may, must’; Du. muot (CI must: G muss); OE metan, v. “meet; acquire’; mot, n. “meeting; council; confrontation; toll'; gemete, adv. ‘fitly’; mō- tian, denom. “discuss?; ON mót, n. “joint; meeting; móti, prp. ‘against. (Isophonic: Mir máidim ‘boast, triumph")
modios, io (grain-measure'. See next, and cf. med- Lat. modius, m. id.; cf. MHG metze, f. ‘corn- measure as milling-fee'; Latv. maZs m. id. (LW in Ir. muidhe, f. jug; Gael. ‘churo’; MHG mut, müt, mutte, mütte)
modos, -es- ‘measure, means’. Cf. méd-. WP II, 259
783
Lat. modus, gs -i, but archaic *modes- implied in modes-tus, moder-are, m. “measure, man- ner; Mir. muidh, mod. modh, pl. a -anna, m. “mode, measure, honour: ON mat, n. “assessment, tax
modhoros (modhuros) (1) ‘dye, dye-plant, dark colour”. WP II, 305 Sindh. madhura, s. ‘aniseed’; Ir. moidiur ‘hay- weed’; cf. modartha, adj. ‘discoloured’; mo- dar- in cpds. id.; OHG matara, f. *dyer's red'; OE maeddre, f. ‘madder; OCS modrü ('livid, grey, black’; Srb: ‘bluish’; Cz. ‘blue’ as also Blg. Slovene); Latv. madara *lady's bedstraw’; cf. also Sw. myske-madra, f. ‘woodruff
modhoros (modhuros) (2) “soft, sweet, gentle’. Cf. medhu Skt. madhurah ‘sweet’; Gael. modhar ‘soft
modhoros (3) Per. madar ‘clod’; NG cf. maddern, v. ‘botch’; Li. madaras *mud; muddle, botchery'
modhos, à “stir, turmoil Gk. móthos, m. id.; ON móór, m. 'excitement beside mod. móða ‘haze’. Isophonic with Go. móbps, m. “anger, courage; MHG muot, sm ‘strength, courage, joy, mood, intent; OE mod, n. (heart, mind’; adj. /harmonious); Du. moed, m. (courage
mogh- (radical element of the following en- tries) “large, powerful, heavy”, etc. (The Skt. forms are ambig. in view of Iranian equivalents of type *maz-). Cf. maháh “big, strong’; compar. mahiyas, superl. mahistha, but cf. Vedic maham, n. ‘great deed, exploit’: Av mayom, n. ‘greatness’, and Skt. mahán, n. ‘greatness: OE mægen, n. ‘strength; feat; force’; Skt. máhas, n. ‘greatness, glory’; ma- hát, pres. pt. ‘strong; great: Olr. mochta ‘mighty’; Go. mahts, etc The velar is explicit in Skt. maghám, n. ‘reward, bounty; OHG mag ‘I can, may’, and OCS mogọ, id. Cf. also OCS moštij ‘worse’. (Speculations on Go. mais, maiza ‘more’; OHG mēro, ON meiri, id. in SF: VWGS: mais)
moghdheio (moghidheio, -dhàio) ‘torture; toil, suffer’. (Sl. ambig. cf. maghido) Gk. mokhthéo ‘toil, suffer’; Lat. moereo, ere, supine: moestum ('grieve' if for *moghid- or *moghidh-, cf. meridies (*med-); merx
==== LAT medeor ====
mecia (macia?), -ae f. : mouron rouge, avocyaXXCc (Ps. Diosc.; Mare.
Emp. ).
meddix; apud Oscos nomen magistratus est, P.F.no,iy. Mot osque:
meddlss, du type iudex, compose du mot racine *med + dic-s "celui
qui montre le droit"; cf.ombr.mefs "droit" (de medos). V. modus et
medeor.
medeor, -eris, pas de parfait, mederi: donner ses soins a (com-
plement au datif m. alicui, m,morbo). Ancien (Caton; vieilles formules).
Apparait des 1 'origine speeialise dans la X. medicale au sens de "porter
remfede a" (cf. la specialisation cura, curd, et en grec de 8ep<X7teuto),
d 1 ou medens "m<?decin"; medela (arch.) "remede", remplace a 1'epoque
classique par remedium; medicus, -a, -um et medicus "medecin"; medibilis-,
Meditrina, cf. Varr., L.L.C,8i, et P.F.110,31: Mos erat Latinis populis,
quo die quis [primum] gustaret mustum, dicere ominis gratia: "Vetus
nouum uinum bibo, ueteri nouo morbo medeor," A quibus uerbis etiam
Meditrinae deae nomen conceptum, eiusque sacra Meditrinalia dicta
sunt. De medicus sont issus de nombreux derives qui ont remplace medeor,
medela, ainsi: medico,—as (et medicor) de j a dans Pl., medicamen (—mentum)
et leurs derivas; medicinus,-a,-um, d'ou medicina (ars), medicinalis:
tu. digitus " 1 'annulaire", trad. du gr. locxpixos SaxxuXog, v. M.Niedermann,
Festg. f. H.Flumner, 33y et suiv.; immedicatus, -cSbilis = oc 0 epa 7 ieuxoc;
==== LAT modus ====
- 736 -
V. medeor.
modus, -I m. (contamination de deux noms differenta; l'un, de aena
abstrait et de genre anime, a vocalisme en o, modus ; 1 'autre, de sena
concret et de genre inanime, a vocalisme en -e-, medos, atteste
in directement par le derive modestus [cf.scelus, sce lestus ], et par
le verbe moderor. L'0 de modestus eat du a 1 'influence de modus, -i;
de raeme pondo a determine le vocalisme de pondus, -eris qui normalement
devrait etre *pendus, cf. Meillet, Introd p. 3 ( 3 o) mesure de surface
(la mesure de capacite s'exprimant par le derive modius), et surtout
mesure agraire, modus agri. A modus "mesure" se rattache mode Ilus,
M.L.yGyO. Au sena mora] et abstrait "mesure qu'on ne doit pas depasser,
moderation, juste milieu". Dans lal.de la rhetorique et de la musique
"mesure rythmique, r.ythme" (souvent joint a numerus), "mesure muaicale",
de la modos facere "faire la musique (d ( accompagnement)"; modus lydius,
equivalent au gr. p,expov. Du sens de "mesure", modus est passe a celui
de "limite" (= opo$), et aussi a celui de "maniore de [se] conduire
ou de [se] diriger" (= Tp 07 ioc), et, par generalisation, A celui de
"maniore, fayon de faire" (souvent joint a mos avec lequel il alliture:
more modoque), d'ou les locutions nombreuses modo, in modum, ad modum,
omnibus modis, huius modi ; quo modS (et quomodo, unifie), quem ad modum
qui, dans la langue populaire, se substituent a ut, trop bref (cf.
1 ’emploi de quomodo dans le Satiricon), et dont le premier a eu une
grande fortune dans les langues romanes sous la forme apocopae quomo,
attestee plusieurs fois en bas 1 atin (v. J.Pirson, Festschr. Volmoller,
p.Oi), fr. comme, esp. cuemo, port. como, etc., cf. M.L. 6 y 73 , etc. le quomodi
```


## [2026-09-07T15:58:53.720Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN must ===\"; grep -on \"must (I), *aux[^|]\\{0,600\\}\" KLN_1966.txt | head -2; echo \"=== KLN empty ===\"; grep -on \"empty, adj[^|]\\{0,500\\}\" KLN_1966.txt | head -2; echo \"=== KLN mode ===\"; grep -on \"mode, n[^|]\\{0,400\\}\" KLN_1966.txt | head -2; echo \"=== KLN methylene ===\"; grep -on \"methylene[^|]\\{0,300\\}\" KLN_1966.txt | head -2"
}
```


### [2026-09-07T15:58:55.157Z] TOOL RESULT

```
=== KLN must ===
=== KLN empty ===
=== KLN mode ===
8386:mode, n.,  1)  a  chest  of  drawers;  2)  a  movable washstand.  —  F.,  fr.  commode,  ‘convenient, serviceable,  comfortable’,  fr.  L.  commodus,  ‘fit, suitable,  convenient’,  lit.  ‘measured  with’,  fr. com-  and  modus,  ‘measure,  manner,  mode’.  See mode  and  cp.  accommodate,  discommode, commodious,  adj.,  spacious,  roomy.  —  F.  com- modieux  (fern,  commodieuse),  fr.  Late  L.  com- 
=== KLN methylene ===
18421:methylene,  ylem. hylic,  adj.,  material,  corporeal  (philos.)  —  ML. hylicus,  fr.  Gk.  6X1x64,  ‘pertaining  to  matter, material’,  fr.  6X19  See  prec.  word  and  -k. hylicism,  n.,  materialism.  —  See  hylic  and  -ism. hylicist,  n.,  a  materialist.  —  See  hylic  and  -ist. hylo-,  before  a
23227:methylene,  amethyst, mead,  n.,  meadow  (poetic).  —  ME.  mede,  fr.  OE. mid,  med.  See  meadow.
```


## [2026-09-07T15:59:02.077Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"must,  *aux[^|]\\{0,700\\}\" KLN_1966.txt | head -2; echo \"=== empty ===\"; grep -on \"empty,  *adj[^|]\\{0,600\\}\" KLN_1966.txt | head -2; echo \"=== SKT must/empty ===\"; grep -n \"^Must\\|^Empty\\|^Mood\\|^Mode \" SKT.txt | head"
}
```


### [2026-09-07T15:59:03.445Z] TOOL RESULT

```
24753:must,  aux.  v.,  am  (or  is,  are)  obliged  to.  —  ME. moste,  fr.  OE.  moste,  pret.  of  motan,  ‘to  be allowed  to,  be  able  to,  have  opportunity  to, have  to’,  rel.  to  OS.  motan,  ‘to  be  obliged  to, have  to’,  OFris.  mdta,  MLG.  moten,  MDu.,  Du. moeten,  ‘to  be  obliged  to’, OHG.  muo^an,  MHG. mue^en,  ‘to  be  allowed  to,  have  to’,  G.  miissen,
=== empty ===
13009:empty,  adj.  — -  ME.  emtie,  empti,  fr.  OE.  iemetig, xmtig,  ‘vacant,  free,  idle’,  formed  with  suff.  -ig (whence  E.  -y)  fr.  xmetta,  ‘leisure’.  This  latter is  formed  fr.  priv.  x-  and  the  stem  of  (ge)mdt, ‘meeting’.  See  moot,  meet.  For  the  excrescent  p cp.  glimpse,  sempstress,  etc.
=== SKT must/empty ===
5811:Empty,  void.  (EO  M.  E.  tf/ipii.  A.  S. a/ftfi^,  lit.  full  of  leisure.  —  A.S.  lem/a, amtffa,  leiiiure-
11844:Mood  (i),  dlspoiilion  of  mind.  (E.) Prob.  sometimes  confused  with  mood  (a), but  properly  di«tincl.  M,  £.  mood,  miiKl. also  temper,  anger,  wrath.  A.  S.  mAit mind,  feeling,  he-art.  •^  Du.  moed,  courage; Icel.  rnJSr,  wtath,  moodiness;  Dan.  Swed. mcd.  G.  mutA,  courage ;  Goth,  mfids,  wrath. Cf.  Gk.  fUiiiux,  I  strive  after.  Perhaps  allied to  Mind.     Der.  moody,  A.  S.  miidig.
11845:Mood  (j),  marmer,  grammatical  form; iet  Mode.
12087:Must  (I),  jpart  of  a  Tcrb  implying '  obligalion.*  (£.)  Only  the  pt.  t.  remains, which  is  now  also  used  as  a  present M.  E.  met.  moot,  pres.  t.,  I  am  able,  1  am free  to,  I  ought ;  pt  t  mttste.  mtiste,  1  was able,  I  ought.  A.  S.  ic  mSt,  pres.  t ;  u m^ste,  I  most,  pt  t ;  as  if  from  an  inftn. nti'fan*.  -^  O  Sax.  m^/an,  pr.  t  tJk  m^t^ pt  t  A^  m6sta ;  Du.  moften,  to  be  obliged  ; Swcd.  m&ste.  I  must,  both  as  pres.  and  pt tense  (whence  the  E.  use) ;  G.  mussen,  pr. t.  If  A  muss,  pt.  I.  ifh  m«ssti\  Goth.  pr.  t tk  nu>t,  pt  t.  ik  mcsta.
12094:Muster ;  see  Monition.
```


## [2026-09-07T15:59:11.535Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"mëdhu\\|medhu\\|Honigwein\\|mëd-\" WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-07T15:59:11.585Z] TOOL RESULT

```
17091:                                               medhu — membh- uiid uiemb-V                         261
19515:  ^rm. meir „Homg“, gen. melii (zum             wohl nach '^medhu geworden;
```


## [2026-09-07T15:59:15.238Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '17085,17140p' WLD_Bd2_pages.txt; echo \"======= WP II 259 med- =======\"; grep -n \"^ *259\\| 259$\\|med-, mëd-\\|Heilkundiger\" WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-07T15:59:16.614Z] TOOL RESULT

```
madayanta ,,sie sollen die Heilkundc ausiiben", lat. me dear; eri „heilen",
medicus „Arzt" (entw. mit Sekundarformans -icus vom Subst. "^med „Arzt"
= av. vi-mad abgeleitet, oder von mederl nach 6 (pvoixog gebildet), gr. Mg-
dog, M/jdi]. Ayaju7]dg usw. ,,Heilgottheiten".
  S. Curtius 243, Fick I^ 105, Yf. LE\Yb.^ s. v. (wo der Zshaug mit nied,
„messen" bestritten war), Brugmann IF. 27, 242 ra. Anm. 1 : 28. 287.
                                               medhu — membh- uiid uiemb-V                         261

in6dhu n, „Honig; bes. Meti'S im Germ. u. BsL masc. geworden.
  Ai. mddlm „Honig, Met'^ (davon mddhu- ,,su6''; madh(u)v-dd- ,,Honig-
€sser“; aksl. medv-ldh „Bar“);
     av. madit „Beerenwein'''; tochar. B.                          ,;Honig^‘   ;
                                                                                   gr.   „Wein“ (aus
„Rau8chtranlv          ‘
                           ;
                               die Bed. „Honig‘' bat sich aui i^ieXt zuriickgezogen)        :
                                                                                                ^ledvoy
„bin trunken“; jAE'dvoKCo „mache trunken“.
   air. mid (gen. medd), cymr. medd, acorn. (Blur.?) medu^ bret.      „Met‘',
cymr. meddiv „berauscht“, bret. me^o ds., me^vi „berauschen“ (parallel gr.
jue^vco), ir. mesc ^berauschend, beraascht^, mesce „Trunkeiibeit“ (ohne ge-
schicbtlichen Zshang mit gr. /is&vgxco);
   aisL mjqdr, ags. meodo, ahd. mefzi ,Met“:                 5


   lit. medus „Honig'‘ {midiis „Met^' aus got. ^midus, Trautmann Germ. Ltg.

50), lett. medus „Honig, Met'S apr. meddo i^medu) „Honig^^; abg. medo, -?£
und -a „Honig'' (dazu u. a, skr. o-mediti se „verderben, z. B. von Fett“,
eigentlich „su61ich, fade werden oder vergahren“, BernekerII31 gegen
Bezzenberger bei Pick II ^ 207, Ublenbeck Ai. Wb. 212).
   Z. B. Curtius^ 279f., Pick I * 105, 281, 512, II ^ 207, III ^ 306.
   Zur Konkurrenz mit *melil „Honig“ (nie „Honigmet‘') und iiber finn.-
ugr. Vergleichung s. Gauthiot Msl. 16, 268 ff., Schrader RL. 85, ^ 139,

medhio- „raittlerer‘\
     Ai. madht/a-, av. maidya- „mittlereB*, Sup.                      ai.   madJiyama-, av. madoma-
,,mittlerer“ (vgl. u. das                      Germ.);
   arm. mej „Mitte'‘ (Hubschmann Arm. Gr. I 474); gr. (ep.) j^ieoGog, (att.)
jueGog,  lat. 7nedkis, osk. rnefiai ,,in media“, gr. ^£6a(a)dT//b == lat. medietas:

gall. Medio-lanum, -matrici, air. mid- in Zs. „medius^', mir. mide „Mitte‘‘,
Mide eigentlich „mittlere Provinz^', air. immedon ,,in medio'‘, cymr. meicn
„in*' {'^medug7io-, s. Pedersen KG. I 112); osk. messimas vermutlich „me-

dioximas"' (s. zuletzt Brugmann IP 1, 229) und mit Verschleppung des                                  .s


aus einem solchen Sup. wohl auch ir. messa „schlimmer“, eigentlich ,,mittel-
ma6iger“ (Pedersen KG. II 120; gegen Stokes KZ. 37, 259); got. midjisy
aisL midr, ags. inidd^ ahd. ynitti „medius*% Sup. got. miduma ,,die Mitte‘*,
aisl. mjgdm f „Hufte“, ags. inedimiay ^nidmest „der mittelste‘*, ahd. nic-

temo „mediocris^' (: av. maddma-) und got. "^'midjuma- (= ai. ^nadhyama-)
in midjun-gards, ags. midda^i-geard „Erdkreis'', ahd. mitiamo „mediocris'\
in miitame^x „inmitten“      (s. Brugmann IF. 14, 5, Grdr. IP 1, 226);
======= WP II 259 med- =======
16975:                                          met-   — med-                                      259
17084:Ratgeber = Heilkundiger" liegt vor in av. vi-mad- „Heilkundiger, Arzt", vT-
```


## [2026-09-07T15:59:35.068Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^me- (2)\\|^me- \\|^menot\\|^mens-\\|^menes\" IEC.txt | head -20; echo \"=== IEC me measure ===\"; grep -on \"^m[eē]-.\\{0,60\\}measure.\\{0,400\\}\" IEC.txt | head -5; echo \"=== IEC menes ===\"; grep -on \"men[eō]s.\\{0,50\\}month.\\{0,300\\}\" IEC.txt | head -5"
}
```


### [2026-09-07T15:59:40.053Z] TOOL RESULT

```
10615:menes (mones) ‘we’. Cf. mes, mnës Arm. menk, mek, id.; Ir. (Ulster) (o-gde) mu- inn, muinne, id.
=== IEC me measure ===
ugrep: error: error at position 101
sure(?:[^\n\x80-\xbf][\x80-\xbf]*){0,400}
            exceeds complexity limits___/


=== IEC menes ===
ugrep: error: error at position 100
nth(?:[^\n\x80-\xbf][\x80-\xbf]*){0,300}
           exceeds complexity limits___/
```


## [2026-09-07T15:59:45.138Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf8',errors='replace').read()\nfor pat in [r\"\\nme-\\s*\\(\\d\\)\", r\"\\nmeno[tsd]\", r\"\\nmenes-\", r\"\\nmens\", r\"\\nme-\\s*'\"]:\n    for m in list(re.finditer(pat,t))[:3]:\n        print(pat, '::', t[m.start():m.start()+500].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-07T15:59:46.548Z] TOOL RESULT

```
\nmeno[tsd] ::  menos, -es- “power, craft, ability, skil’. WP II, 264 Skt. mánas, n. “mind, mood, skilP ; Av. mano, n. id.; manahyo, adj. ‘intellectual; Per. manis ‘temperament; Gk. ménos, gs -eos, n. ‘power, desire, plan, design’; cf. a-meínon, comp. "better" It. ména (^work, task, condition, qua- lity, kind', whence menare ‘do, put, move, lead, deal, make"); OLat. cf. Menerua, Lat. Minerva (‘goddess of arts and crafts’, fr. *me- nes-uà) beside minerval, n. *college-fee'; ad- miniculum “prop, aid’; W cf. men
---
\nmens ::  mens, ménes- ‘moon, month’. Cf. mena, meno, (màn-, mõn-). Variant: mes Skt. cf. màs, m. jd: Av. mào, màóh-, m. ‘moon’; OPer. Per. mah, as, Skt.; Oss. mii, id.; Scyth. cf. més-plé ^*full-moon'; Tokh. mañ, pl. mañi; B men & meñe, as Skt.; Arm. cf. amis, gs amso, o-st. (‘month of the year”, for *am-mes); Hiero-Hitt. cf. mén-ulas "moon: Myc. & Gk. men, gen. sg. ménós, m. ‘month’; Dor. mes, dp mési & ménesi ‘moon, month’; Aeol. meis, gs mënós (Lesb. gs ménnos); gp mëng, -en- — mentos, à, io (menth-)
---
```


## [2026-09-07T15:59:52.023Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf8',errors='replace').read()\nfor m in list(re.finditer(r\"\\nm[eē]tro[sn]|\\nm[eē]-\\b|\\nm[eē]tis|\\nm[eē]ta\\b\",t))[:8]:\n    print('::', t[m.start():m.start()+380].replace('\\n',' '))\n    print('---')\nEOF"
}
```


### [2026-09-07T15:59:53.530Z] TOOL RESULT

```
::  metros, ios “measured, moderate, wise, con- siderate'. Cf. metrió, motriio, etc. Skt. cf. matrah, adj. ‘measuring, of dimen- sion’; -ah, am, -åa ‘measure’; Av. cf. maàtra, f. ‘healer’; Gk. métrios, méterros ‘moderate’; métron, n. ‘measure’; W medr, m. “skill, knowledge' mettós (pp. of type met-, see meto) “cast, fallen, failed, rejected, weak? Oss. cf. mát'àl “weak, sluggish’
---
```


## [2026-09-07T16:02:05.533Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT azda ===\"; python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf8',errors='replace').read()\nfor m in list(re.finditer(r\"azd[aā]\",t))[:8]:\n    print(repr(t[max(0,m.start()-150):m.start()+250].replace('\\n',' ')))\n    print('---')\nEOF"
}
```


### [2026-09-07T16:02:06.903Z] TOOL RESULT

```
=== KNT azda ===
'a corrupted form of the language, carry the line down to Artaxerxes ПІ (359-38). II. Avestan is the language of the Avesta or sacred writings of the Mazdayasnians, known also as Parsis (ie. Persians) and as Zoroastrians or followers of Zoroaster, the prophet who pro- claimed the religion. It consists linguistically of two parts: an older part containing the (402/8 or metrical sermons of Zoroaster '
---
'КІ-Н 46 jd F s G 02 94 $ sch G 02 85 2 z Bf-L 36 96 № h B-J 38 Ideograms and Ligature 37 XS ‘König M-G 02 8 DH Ча L 45 39 BU ‘Erde’ L 45 40 AM ‘Ahuramazda’ Op 74, E 90 4| BG бода ‘god’ Sc 1929 42  AMha Auramazdé Sc 1929, Auramazda- ha Br 1932 (cf. Hz 1931) Word-divider 43: Ty 1798 $18. Tue Orp-PERstiAN SviLABARY. The in- scriptions composed in the Old Persian language are inscribed on various hard'
---
' Ligature 37 XS ‘König M-G 02 8 DH Ча L 45 39 BU ‘Erde’ L 45 40 AM ‘Ahuramazda’ Op 74, E 90 4| BG бода ‘god’ Sc 1929 42  AMha Auramazdé Sc 1929, Auramazda- ha Br 1932 (cf. Hz 1931) Word-divider 43: Ty 1798 $18. Tue Orp-PERstiAN SviLABARY. The in- scriptions composed in the Old Persian language are inscribed on various hard materials in a syllabary, each character having the value of a vowel or of '
---
'aramcamary. $2. Tue InEoGRAMS are five in number, stand- ing respectively for s8dyabiya ‘king’, dahydus ‘province’, bümi$ ‘earth’, Auramazdá ‘Ahura- mazda’, and baga ‘god’; they are transcribed by Хо, DH, BU, AM, BG. In DSk 4 there is what seems to be a ligature for AM-ha, The ideograms, without addition of syllabic characters, stand for the nominative si\x0cngular; ! Final s after 7 and й became $ i'
---
' written. ; Ае agrees with DSf; it has bümim and Вуй, otherwise XŠ and DH , but Auramazdà and baga. АзРа has zšāyaðiya, DH, būmām (sc) and BUyé, Auramazdā, baga; a state of variation which is attributable to the inaccuracy of OP writing at this period. $3. NumeRars: The cardinals are not written in full (except aiwa- ‘one’ in a formulaic phrase), but are indicated by signs: 1, a single long vertic'
---
'ely rare: examples are yadimaniyaiy XPh 47 = yadi(y) : maniyü(hayiy, and upà Artarsa- юат) Si. The gen. Auramazdàha is replaced in XPe 10 by Aurahyá Mazdaha, with declension of both parts of the compound, but no divider. The emphatic adverb apiy is sometimes at- tached to the preceding as an enclitic, and some- times separated from it by a divider. The en- chtie pronoun diš is preceded by a divide'
---
'a (y). A\'Sa 4. p\'ar"s* = (loc.) Pársa(iy) АЗН 3. aame = alvdjme(iy) DB 5.2f (probable res- toration). П. The -1- may be omitted in final -aiy: | Auramazda-tay DB 4.58, for -іату. mantyahay DPe 20, for -haty. ula-may A’Sde 4, for uta-maty (which is in db). Cf. forms of düraiy, with enclitic apiy (5186). ПІ. The character a was sometimes omitted where it marked length: XSydném DPh 1, DH 1, тїйуабїуй'
---
'kartam. Düàrayava(u)Sahyà А?На 2, 2°, 4, 4°. marti(ya)hyà А?Ра 4f; адада( пат A*Pa 22. VIL. A serious haplography occurs, according 3 b B. y b 1 Auramazda(ma)iy DNa 50; ayáu(mayini$ DNb 4 | bi * UM to Bv. MSLP 23.182-3, in DB 1.66, where he 4 would read adind : adam : (patiydbaram : adam :) 3 küram; but his assumption is not necessary for * an interpretation. $53. Appition оғ Онлвлстенз: in almost'
---
```


## [2026-09-07T16:02:07.908Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WEB methylene ===\"; grep -on \"meth'yl-ene[^|]\\{0,300\\}\\|methylene, n[^|]\\{0,300\\}\" WEB_vol1.txt FSD_vol3.txt 2>/dev/null | head -4; echo \"=== KLN mode/model ===\"; grep -on \"^mode, n[^|]\\{0,400\\}\\|^model, n[^|]\\{0,400\\}\" KLN_1966.txt | head -4; echo \"=== KLN medicine ===\"; grep -on \"^medicine, n[^|]\\{0,400\\}\" KLN_1966.txt | head -2"
}
```


### [2026-09-07T16:02:09.237Z] TOOL RESULT

```
=== WEB methylene ===
=== KLN mode/model ===
=== KLN medicine ===
```


## [2026-09-07T16:02:18.197Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt SKT.txt KLN_1971.txt; do echo \"=== $f ===\"; grep -oin \"methylene.\\{0,200\\}\" $f | head -2; done; echo \"=== KNT azda variants ===\"; grep -oin \"azdà.\\{0,150\\}\\|azda.\\{0,120\\}\" KNT.txt | grep -i \"known\\|kund\" | head -4"
}
```


### [2026-09-07T16:02:19.614Z] TOOL RESULT

```
=== FSD_vol1.txt ===
58118:methylene and  an  oxidation  product  of  carone.
85296:methylene. —   cy"clo-hex'a-nol,  n.  An  alcohol  (C*Hu OH)  obtained  from  cyclohexane.  —   cy"clo-bex'a-none,  n. A   ketone  (CtHioO),  made  by  subjecting  cyclobexanol  to oxidation.
=== FSD_vol2.txt ===
36393:Methylene’  ‘
36395:Methylene  i Ja'misg....  Coal-tar....  D.  g*
=== FSD_vol3.txt ===
35444:methylene blue, see dlvb -
35451:methylene with
=== FSD_vol4.txt ===
25340:methylene groups  hcptamethjlene,  cjcloheptane  — su'ber-ate,  n Chem  A   salt  of  suberic  acid  —   su-bc're-ous,  a   Of,  per- taining to,  or  of  the  nature  of  cork  —   su-ber'Ic,  a   Of,  per- t
=== WEB_vol1.txt ===
90354:methylene, and tetramine.] a crysta the vul- pound, CeHuN4, used to speed UE ine asa canization of rubber and, in me urinary antiseptic.
=== SKT.txt ===
=== KLN_1971.txt ===
117865:methylene, ylem. 
147200:methylene, amethyst, 
=== KNT azda variants ===
334:azdayasnians, known also as Parsis (ie. Persians) and as Zoroastrians or followers of Zoroaster, the prophet who pro- claime
2696:azdà абага ‘it was not known to the people’, DB 1.75 kdrahyd агава afaha, DSa 5 nsahyd frasam badaydtary.
```


## [2026-09-07T16:02:25.620Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2690,2700p' KNT.txt | cut -c1-1200"
}
```


### [2026-09-07T16:02:25.666Z] TOOL RESULT

```
SI^ 2
uv
SYNTAX AND STYLE 8l
үшалпаһуа máhya XIV raucabiš бакаіа üha 44 days of the month Viyakhna were past’; DB 1.49 ngiy amazam taumayà Каёсту ‘not anyone of our family’, cf. amáxam taumäyä DB 1.28f depending directly on Kabügiyà; Ра 1f hya mah Ча bagünam the greatest of the gods’.
E. Expressing time within which: DB 4.4f Һатаћуду Sarda in one and the same year’; from this use came the use of the genitive харо, DB 1.20, in a riming pair with acc. rauca and enclitic patiy, to indicate time when,
F. As appositive to a genitive, as in DB 3.58f Dárayavahaus xXayatijahya.
G. Ав dative of indirect object, in DB 1.12 Auramazdá хёасат manā frübaro, DB 1.81f kürahy& naiy azdà абага ‘it was not known to the people’, DB 1.75 kdrahyd агава afaha, DSa 5 nsahyd frasam badaydtary.
Н. As dative of reference, in DB 1.87 antyahyä asam frünayam ‘for the rest I brought horses’, DNa 3f hya убит айй martiyahyà ‘who created happiness for man’; including the dative of pos- session, as in DB 4.56 utätaiy laumà vasty biyd ‘and to thee may there Бе family in abundance’.
І. As dative of goal, in DB 1.18 «mà dahyava tyā mand райуй$а ‘these are the provinces which came to me’.
J. With the idea of hama- ike’ in compounds: DB 1.30 Лата hamapilà Kabūjiyahyā ‘having the same mother and father as Cambyses’; the position of the genitive after the adjectives sug- gests that this is a dative use rather than a true genitive use (cf. §309)?
К. With prepositions, the mixed use with -ройу (see E); DB 3.32 pasa mand ‘behind me’; with anu- ‘according to’, in DNb 16, 18; with following rüdiy, to express agent, in DNb 9, 10f; with encli- tic -rddiy, in avahyarddiy ‘on account of this’.
```


## [2026-09-07T16:12:00.001Z] TOOL CALL #76: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndef n(**kw): return kw\n\nentry0_nodes = []\n\nentry0_nodes.append(n(\n id=1, lang=\"Indo-European\", words=\"Med\",\n verdict=\"confirmed\",\n derivation=\"Pokorny's mēd-1 (IEW 705-706), 'to measure; to give advice, healing', an extension of the *mē- 'to measure' of the root box — Pokorny says so himself at the foot of the entry ('See also: mēd- is related to mē-3 (above S. 703 f.)'). Watkins/AHD prints the lemma as 'med-. To take appropriate measures. ... [Pok. 1. med- 705.]', which is word-for-word Nourai's gloss; today the root is written *med- (with a long-vowel *mēd- in the Germanic and Celtic branches). The semantic bridge 'take the appropriate measure' > 'treat, cure' is Pokorny's section B ('An already Proto language application for “wise counsellor = one skilled in medicine”'), which links Av. vī-mad-, Gk. Mēdos/Agamēdē (healing deities) and Lat. medeor/medicus. Nourai's page reference and language label are both right.\",\n derivation_fa=\"«Med» همان ریشهٔ هندواروپایی آغازین *med- (در پوکورنی mēd-1، صص ۷۰۵–۷۰۶) است به معنای «اندازه گرفتن، تدبیر کردن؛ چاره کردن، درمان کردن». پوکورنی خود در پایان همین مدخل می‌نویسد که mēd- با mē- «اندازه گرفتن» (ص ۷۰۳) پیوند دارد، پس جای‌دادن آن زیر ریشهٔ اصلی درست است. واتکینز نیز در پیوست فرهنگ American Heritage عیناً می‌نویسد «med-. To take appropriate measures … [Pok. 1. med- 705]» که ترجمهٔ واژه‌به‌واژهٔ همان چیزی است که نورایی در جعبه آورده. تحول معنایی «تدبیر شایسته اندیشیدن» به «درمان کردن» را پوکورنی در بخش ب همین مدخل با گواه اوستایی vī-mad- و لاتینی medeor توضیح می‌دهد. ادعای نورایی درست است.\",\n sources=[W+\"Reconstruction:Proto-Indo-European/med-\"],\n ref_check=[dict(ref=\"POK:705\", status=\"supports\", note=\"POK_full.txt, block 'Root / lemma: mehd-1 / Meaning: to measure; to give advice, healing / … Page(s): 705-706', with 'See also: mehd- is related to meh-3 (above S. 703 f.)' — the page number and the gloss are exactly Nourai's.\")],\n consulted=[\n   dict(src=\"AHD\", where=\"Watkins 1985, s.v. med-\", stance=\"supports\", note=\"'med-. To take appropriate measures. … [Pok. 1. med- 705.]' — the whole of Nourai's chart (medērī, modus, modestus/moderāre, Germanic *mōt- > MUST, EMPTY) is laid out under this one lemma.\"),\n   dict(src=\"WLD\", where=\"Walde-Pokorny Bd. II 259\", stance=\"supports\", note=\"WLD_Bd2_pages.txt p.259: the 'Ratgeber = Heilkundiger' section — \\\"'Ratgeber = Heilkundiger' liegt vor in av. vi-mad- „Heilkundiger, Arzt“, vī-maδayanta „sie sollen die Heilkunde ausüben“, lat. medeor -eri „heilen“, medicus „Arzt“\\\".\"),\n   dict(src=\"IEC\", where=\"Mann, s.vv. medo (2), medos, médos\", stance=\"supports\", note=\"\\\"medo (2) 'treat, remedy'. Same as (1) (?). Cf. medos Av. mad-, maδ- 'treat, cure'; maδō, m. 'medicine, science'; Lat. medeor -ēri 'heal, remedy'; cf. re-medium 'remedy'\\\" and \\\"medos, -es- 'measure'. Cf. modos\\\".\"),\n ],\n derivation_note=None,\n))\n\nentry0_nodes.append(n(\n id=2, lang=\"Avestan\", words=\"vi-mad\",\n verdict=\"confirmed\",\n derivation=\"Younger Avestan vī-mad- m. 'one skilled in medicine, physician' (Bartholomae, AiW col. 1450: 'j. vi-mad- : *mād- m. „Heilkundiger, Arzt“', Vd. 7.40 'als Ärzte praktiziren'), with the denominative verb vī-maδaya- 'mederi, to practise the healing art' (Vd. 7.38, 40 vīmaδayanta 'sie sollen die Heilkunde ausüben'). It is vī- 'apart, thoroughly' + the zero-grade *mad- of PIE *med-, with the regular Indo-Iranian voicing/spirantisation of intervocalic *-d- to Avestan δ. Bartholomae himself adds 'Vgl. lat. medeor, medicus', and Walde-Pokorny II 259 derives Lat. medicus 'either with the secondary suffix -icus from the noun *med „physician“ = Av. vi-mad, or from medērī on the model of ὁ φυσικός'. Buck's PHYSICIAN article puts 'Av. vimad-' in the table of IE words for 'physician' and comments 'Av. vimad- : Lat. medērī „cure“, etc. Barth. 1450'. Nourai's gloss 'care giver, physician' and his cross-reference ☞Wi (to the preverb vī-) are both correct.\",\n derivation_fa=\"اوستایی متأخر vī-mad- «پزشک، درمانگر» (بارتولمه، فرهنگ ایرانی باستان، ستون ۱۴۵۰: «Heilkundiger, Arzt»، وندیداد ۷.۴۰) و فعل برساختهٔ vī-maδaya- «درمان کردن، طبابت کردن» از پیشوند vī- «جدا، سراسر» و ستاک صفر *mad- از ریشهٔ *med- ساخته شده است؛ دال میان‌واکه‌ای هندواروپایی در اوستایی به‌طور منظم به δ (ذ) بدل می‌شود. خودِ بارتولمه ذیل همین مدخل می‌افزاید «قس لاتینی medeor، medicus» و والده-پوکورنی (ج۲ ص۲۵۹) نیز medicus لاتینی را با همین *med «پزشک» = vi-mad اوستایی می‌سنجد. باک هم در بخش ۴٫۸۷ («پزشک») صراحتاً می‌نویسد «Av. vimad- : Lat. medērī، بارتولمه ۱۴۵۰». پس ادعای نورایی درست است.\",\n sources=[W+\"Reconstruction:Proto-Indo-European/med-\"],\n ref_check=[\n   dict(ref=\"POK:705\", status=\"supports\", note=\"POK_full.txt, mēd-1 section B: 'Avestan vī-mad- „one skilled in medicine, physician, medicine man“, vī-maδayanta „sie sollen die Heilkunde ausüben“ … Latin medeor … medicus „physician“ (… = derived Avestan vī-mad)'.\"),\n   dict(ref=\"SYN:307\", status=\"supports\", note=\"Buck 4.87 PHYSICIAN begins on printed p.307 (SYN.txt leaf 347); the table's Avestan row is 'Av. vimad-', and the discussion on p.309 ends 'Av. vimad- : Lat. medērī „cure“, etc. Barth. 1450.'\"),\n ],\n consulted=[\n   dict(src=\"BRT\", where=\"AiW col. 1450 s.v. vi-mad-\", stance=\"supports\", note=\"BRT.txt: '• j. vi-mad- : *mād- m. „Heilkundiger, Arzt“ … V.7.40; 38' and '• j. vimaδaya- den. Praes. 3l „mederi“, „die Heilkunde ausüben an —“ (Akk.)'; note 'Vgl. lat. medeor, medicus'.\"),\n   dict(src=\"WLD\", where=\"Walde-Pokorny Bd. II 259\", stance=\"supports\", note=\"'… liegt vor in av. vi-mad- „Heilkundiger, Arzt“, vī-maδayanta „sie sollen die Heilkunde ausüben“, lat. medeor, -eri „heilen“, medicus „Arzt“ (entw. mit Sekundärformans -icus vom Subst. *med „Arzt“ = av. vi-mad abgeleitet …)'.\"),\n   dict(src=\"IEC\", where=\"Mann, s.v. médos, ios\", stance=\"partial\", note=\"\\\"médos, ios, io 'remedy, means'. Cf. medo (2). WP II, 259 Skt. cf. (alleged) vi-madah; Av. vi-maδas, -ah-, n. 'medical treatment'\\\" — Mann treats the Avestan word as a neuter -as- stem 'medical treatment' rather than as the agent noun 'physician'.\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=3, lang=\"Pahlavi\", words=\"vîmâr\",\n verdict=\"disputed\",\n derivation=\"The Pahlavi word itself is beyond doubt: MP wymʾl, read wēmār by MacKenzie ('wēmār [wymʾl | M wymʾr, N bēmār] ill, sick. ~īh: illness', CPD 90) and vīmār by Nyberg ('vīmār [wymʾl] ill … MPrs wymʾr (BBB); Paz. vimār, NP bīmār'); Nourai's 'vîmâr' is Nyberg's/Horn's transliteration of the same word, so it is not a misprint. What is disputed is the arrow: deriving it from Av. vī-mad- 'physician' requires (a) a complete inversion of meaning, 'healer' > 'sick person', and (b) Av. δ > MP r, which is not a Middle Persian sound law. Horn, at the very page Nourai cites for the next node (Grundriss no. 39, p.59), sets out the Avestan vī-mad-/Pahlavi vīmār equation and then rejects it: 'Die Etymologie ist gewiss falsch, da altes vi- im Neupersischen consequent zu gu- wird, und selbst bei Annahme eines Ausnahmefalles … das ī völlig unerklärt bliebe', and reports Bartholomae's alternative to him, upa- (Horn no. 247) + māra- 'at the point of death'. Modern handbooks are equally unsettled: English Wiktionary derives MP wēmār from PIE *wemh₁- 'to spew, vomit' (cf. Lat. vomō) + the agent suffix -ār, while the widespread Iranian-studies view is *wi-mār- to mar- 'to die'. No source supports Nourai's route.\",\n derivation_fa=\"خودِ واژهٔ پهلوی تردیدی ندارد: صورت نوشتاری wymʾl را مکنزی wēmār («بیمار») و نیبرگ vīmār می‌خوانند و هر دو دنبالهٔ آن را «بیمارِ» فارسی نو می‌دانند؛ پس صورتِ «vîmâr» در کتاب خطای خوانش نیست، بلکه آوانگاری قدیمی‌تر است. آنچه محل مناقشه است پیکان نمودار است: برآمدن wēmār «بیمار» از vī-mad- اوستایی «پزشک» هم دگرگونی معنایی وارونه (درمانگر ← درمانده) می‌خواهد و هم تبدیل δ اوستایی به r که قاعدهٔ آوایی فارسی میانه نیست. هرن در همان صفحهٔ ۵۹ (شمارهٔ ۳۹) که نورایی برای گرهٔ بعدی به آن ارجاع می‌دهد، این ریشه‌شناسی را می‌آورد و سپس رد می‌کند: «این ریشه‌شناسی بی‌گمان نادرست است، زیرا vi- کهن در فارسی نو پیوسته به gu- بدل می‌شود و حتی با فرض استثنا، ای کشیده یکسره توضیح‌ناپذیر می‌ماند»؛ و پیشنهاد بارتولمه، یعنی upa + māra- «بر لب مرگ»، را نقل می‌کند. پژوهش امروزی نیز یکدست نیست: ویکی‌واژه wēmār را از *wemh₁- «قی کردن» (قس لاتینی vomō) به‌علاوهٔ پسوند -ār می‌داند و دیدگاه رایج ایران‌شناسی آن را *wi-mār- از ریشهٔ mar- «مردن» می‌گیرد. هیچ منبعی مسیر نورایی را تأیید نمی‌کند.\",\n sources=[W+\"%D8%A8%DB%8C%D9%85%D8%A7%D8%B1\"],\n ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"the book gives this box no reference of its own; the parent's POK:705 contains no Middle Persian material at all (checked POK_full.txt, mēd-1 entry).\")],\n consulted=[\n   dict(src=\"PHD\", where=\"MacKenzie, CPD p.90 s.v. wēmār\", stance=\"partial\", note=\"PHD.txt: 'wēmār [wyml | M wymʾr, N bēmār] ill, sick. ~īh: illness.' — the word and the New Persian outcome are confirmed; MacKenzie gives no Avestan etymon.\"),\n   dict(src=\"NYB\", where=\"Nyberg, Manual of Pahlavi II, s.v. vīmār\", stance=\"partial\", note=\"NYB_vol2_glossary.txt: 'vīmār [wymʾl] ill, pl. cas. obl. ~-ān 85³. — MPrs wymʾr (BBB); Paz. vimār, NP bīmār.' plus 'vīmārēnītan to make a p. ill'. Nyberg's reading is exactly Nourai's 'vîmâr', but he offers no derivation from vī-mad-.\"),\n   dict(src=\"HRN\", where=\"Horn, Grundriss no. 39, p.59\", stance=\"contradicts\", note=\"HRN.txt leaf 80: '39. bimār „krank“ … aw. vī-[mad-] …; phlv. vimār, vimārīh (Men.), vimārīnītan … Die Etymologie ist gewiss falsch, da altes vi- im Neupersischen consequent zu gu- wird …'\"),\n   dict(src=\"POK\", where=\"IEW 705-706, mēd-1\", stance=\"silent\", note=\"the Pahlavi word does not occur in the entry; only the Avestan vī-mad- is cited.\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=4, lang=\"Persian\", words=\"bîmâr «بیمار»\",\n verdict=\"confirmed\",\n derivation=\"This edge — Pahlavi wēmār/vīmār > NP بیمار bīmār — is regular and uncontested. Word-initial Middle Persian w- becomes NP b- without exception (MP wād > باد bād, MP wēš > بیش bēš, MP wīst > بیست bist, MP wistarg > بستر bestar), and MP ē yields NP ī in this environment; the abstract wēmārīh gives بیماری bīmārī and the compound بیمارستان bīmārestān (whence Arabic بیمارستان/مارستان). MacKenzie glosses the Pahlavi headword straight through to 'N bēmār' and Nyberg to 'NP bīmār'. Borhan-e Qateʿ, at the page Nourai cites, has the entry «بیمار … ناتوان و خسته را گویند» with «بیمارسان/بیمارستان». The one problem is the second reference: Horn p.59 is the page that DENIES the chart's upstream Avestan derivation, so Nourai is citing against himself; the Persian word itself is fine, but it hangs on a Pahlavi box whose parentage no source accepts.\",\n derivation_fa=\"این پیوند — پهلوی wēmār/vīmār ← «بیمارِ» فارسی نو — کاملاً منظم و پذیرفته است: واو آغازینِ فارسی میانه در فارسی نو بی‌استثنا به «ب» بدل می‌شود (wād > باد، wēš > بیش، wīst > بیست، wistarg > بستر) و ای کشیدهٔ فارسی میانه در این جایگاه ی می‌شود؛ اسم مصدر wēmārīh «بیماری» و ترکیب «بیمارستان» (که معرّب آن «مارستان» است) نیز از همین ساخته شده‌اند. مکنزی و نیبرگ هر دو صورت پهلوی را مستقیماً به «بیمار» فارسی می‌رسانند و برهان قاطع در همان صفحه‌ای که نورایی ارجاع داده «بیمار … ناتوان و خسته را گویند» آورده است. اما ارجاع دوم دردسرساز است: صفحهٔ ۵۹ هرن دقیقاً همان جایی است که ریشهٔ اوستایی این زنجیره را رد می‌کند؛ پس واژهٔ فارسی درست است ولی به جعبه‌ای پهلوی آویخته است که نیای اوستایی‌اش را هیچ منبعی نمی‌پذیرد.\",\n sources=[W+\"%D8%A8%DB%8C%D9%85%D8%A7%D8%B1\"],\n ref_check=[\n   dict(ref=\"BQT:340\", status=\"supports\", note=\"BQT_v1_pages.txt (leaf 560, the ب-ی section): 'بیمار — بروزن دیوار، ناتوان و خسته را گویند …' followed by 'بیمارستان … که بعربی دارالشفاء خوانند' — the word and the gloss 'patient' are there, but Moʿin's footnote cites Unvala 252 and an Old Iranian root, not Av. vī-mad-.\"),\n   dict(ref=\"HRN:59\", status=\"contradicts\", note=\"Horn p.59 (HRN.txt leaf 80 = printed 59, entry no. 39 'bimār „krank“'): after giving the Avestan/Pahlavi material Horn writes 'Die Etymologie ist gewiss falsch …' and prefers Bartholomae's upa + māra-. The page Nourai cites rejects his own arrow.\"),\n ],\n consulted=[\n   dict(src=\"PHD\", where=\"MacKenzie, CPD p.90\", stance=\"supports\", note=\"'wēmār [wyml | M wymʾr, N bēmār] ill, sick' — the MP > NP step is MacKenzie's own.\"),\n   dict(src=\"NYB\", where=\"Nyberg, Glossary s.v. vīmār\", stance=\"supports\", note=\"'… Paz. vimār, NP bīmār.'\"),\n   dict(src=\"BQT\", where=\"Borhan-e Qateʿ p.340\", stance=\"supports\", note=\"entry بیمار with the gloss ناتوان و خسته and the derivatives بیمارناک، بیمارستان.\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=5, lang=\"Avestan / Old Persian\", words=\"azdâ\",\n verdict=\"plausible\",\n derivation=\"The word is real and the double language label is right, but the gloss is loose and the etymology is Pokorny's own tentative one. Bartholomae (AiW 344) lists it as 'g., p. azdā Adv. „kund, gewiss“' — a Gathic Avestan and Old Persian adverb 'known, certain', not a noun 'indicator, hint, news'. Kent quotes DB 1.81f kārahyā naiy azdā abava 'it was not known to the people' and DB 4.? / D.G.4 yaθā-taiy azdā bavātiy 'so that it may become known to thee'; the idiom is azdā kar- 'to make known'. Pokorny attaches it to mēd-1 only with a question mark: 'whether also zero grade of Old Indic addhā (*md-dʰē) „certainly, yea, in truth“, Avestan Old pers. azdā, Old Indic addhāti- „smart man, sage“ with the meaning from Latin meditārī etc.? s. Pedersen Decl. Latin 72'. So the arrow reproduces Pokorny faithfully — including his hesitation — while the gloss is Nourai's paraphrase.\",\n derivation_fa=\"خودِ واژه و برچسبِ دوگانهٔ زبان («اوستایی/پارسی باستان») درست است، اما معنی‌ای که نورایی داده دقیق نیست و ریشه‌شناسی هم در خودِ پوکورنی با تردید آمده. بارتولمه (فرهنگ ایرانی باستان، ستون ۳۴۴) آن را چنین می‌آورد: «g., p. azdā قید: کند، گویس» یعنی «آشکار، معلوم، بی‌گمان» — قید است نه اسم به معنای «نشانه، خبر». کنت نیز از بیستون (۱٫۸۱) نقل می‌کند: kārahyā naiy azdā abava «برای مردم آشکار نشد»، و اصطلاح azdā kar- «آشکار کردن» شناخته است. پوکورنی این واژه را تنها با علامت پرسش زیر mēd-1 می‌گذارد و آن را ستاکِ صفرِ *md-dʰē می‌داند، هم‌ریشه با addhā «به‌راستی» و addhāti- «دانا» در هندی باستان. پس پیکانِ نمودار دقیقاً همان چیزی است که پوکورنی گفته، همراه با همان تردید؛ ولی معنی، بازنویسی آزادِ نورایی است.\",\n sources=[W+\"Reconstruction:Proto-Indo-European/med-\"],\n ref_check=[dict(ref=\"POK:705\", status=\"partial\", note=\"POK_full.txt, mēd-1: 'whether also zero grade of Old Indie addha (*md-dʰe) „certainly, yea, in truth“, Avestan Old pers. azdā ds., Old Indie addhati- „smart man, sage“ … s. Pedersen Decl. Latin 72;' — the form and the connection are on the page Nourai cites, but Pokorny marks the derivation as doubtful and glosses azdā 'certainly', not 'indicator, hint, news'.\")],\n consulted=[\n   dict(src=\"BRT\", where=\"AiW col. 344 s.v. azdā\", stance=\"partial\", note=\"BRT.txt: '• g., p. azdā Adv. „kund, gewiss“: kārahya naiy a° abava(f) „… wurde es dem Volk nicht kund, dass …“ Bh. 1.10; — yaθā-taiy a° bavātiy D. G.4' — gloss 'known, certain', part of speech adverb.\"),\n   dict(src=\"KNT\", where=\"Kent, Old Persian §Syntax (KNT.txt leaf ~93) and Lexicon\", stance=\"supports\", note=\"'DB 1.81f kārahyā naiy azdā abava „it was not known to the people“' — Kent confirms the Old Persian word and the meaning 'known'.\"),\n   dict(src=\"AHD\", where=\"Watkins 1985, s.v. med-\", stance=\"silent\", note=\"Watkins' med- entry has no Indo-Iranian material at all; azdā is not mentioned.\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=6, lang=None, words=\"\",\n verdict=\"unverified\",\n derivation=\"An empty pass-through box. On the printed page (pdf 324, book 294) there really is an arrow running right out of the azdā box into a large rectangle that carries no language label and no word — the box was left blank in the book's own artwork, exactly as the extraction records it. There is nothing to verify; in the parallel charts of Part 1 this slot normally holds the Persian or English reflex, and for azdā that would presumably have been a form Nourai never filled in.\",\n derivation_fa=\"جعبه‌ای تهی و بی‌محتواست. در صفحهٔ چاپی (صفحهٔ ۲۹۴ کتاب) به‌راستی پیکانی از جعبهٔ azdā به مستطیلی بزرگ می‌رود که نه برچسب زبان دارد و نه واژه‌ای؛ یعنی خودِ کتاب آن را سفید گذاشته و خوانش اسکن هم درست همان را ثبت کرده است. چیزی برای راستی‌آزمایی وجود ندارد؛ در نمودارهای همانند، این جایگاه معمولاً بازماندهٔ فارسی یا انگلیسی را نگه می‌دارد که نورایی اینجا آن را پر نکرده است.\",\n sources=[],\n ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"no reference; the box is blank in the book.\")],\n consulted=[dict(src=\"(printed page)\", where=\"EtymologicalDictionary-persian-english.pdf p.324 / site/pages/324.jpg\", stance=\"silent\", note=\"the rendered page shows an arrow from the 'Avestan / Old Persian azdā' box into an empty unlabelled rectangle; the JSON is faithful to the page.\")],\n error_in=\"book\", book_prints=\"(an empty, unlabelled box)\", correct_form=\"(nothing — the box is blank in the book)\",\n))\n\nentry0_nodes.append(n(\n id=7, lang=\"Latin\", words=\"\",\n verdict=\"confirmed\",\n derivation=\"A pass-through box standing for Latin medērī 'to look after, heal, cure' and its family — medicus 'physician', medicīna (ars) 'the healing art', remedium 'remedy', plus meditārī 'to reflect'. Ernout-Meillet: 'medeor, -eris, pas de parfait, medērī: donner ses soins à … Apparaît dès l'origine spécialisé dans la l. médicale au sens de „porter remède à“ … d'où medēns „médecin“; medēla „remède“, remplacé à l'époque classique par remedium; medicus „médecin“'. Watkins puts the whole group here: 'med- … 2. a. Latin medērī, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEGLIN, REMEDY'. Nourai's 'AHD' citation is therefore right, and leaving the box wordless is a drafting choice, not an error.\",\n derivation_fa=\"جعبه‌ای گذری است که جای فعل لاتینی medērī «پرستاری کردن، درمان کردن» و خانوادهٔ آن را می‌گیرد: medicus «پزشک»، medicīna «هنر پزشکی»، remedium «درمان» و meditārī «اندیشیدن». ارنو و مِیه در فرهنگ ریشه‌شناختی لاتین می‌نویسند که medeor از آغاز در زبان پزشکی به معنای «چاره کردن» تخصص یافت و medēns «پزشک»، medēla «دارو» (که در دورهٔ کلاسیک جای خود را به remedium داد) و medicus از آن برآمدند. واتکینز نیز همهٔ این گروه را زیر med- می‌آورد. پس ارجاع نورایی به AHD درست است و تهی‌بودن جعبه صرفاً شیوهٔ ترسیم است، نه خطا.\",\n sources=[],\n ref_check=[dict(ref=\"AHD\", status=\"supports\", note=\"Watkins 1985 s.v. med-: '2. a. Latin medērī, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEGLIN, REMEDY; b. Latin meditārī, to think about, consider, reflect: MEDITATE.'\")],\n consulted=[\n   dict(src=\"LAT\", where=\"Ernout-Meillet s.v. medeor (LAT.txt line ~36971)\", stance=\"supports\", note=\"'medeor, -eris, pas de parfait, medērī: donner ses soins à … d'où medēns „médecin“; medēla (arch.) „remède“, remplacé à l'époque classique par remedium; medicus … „médecin“'.\"),\n   dict(src=\"WLD\", where=\"Walde-Pokorny Bd. II 259\", stance=\"supports\", note=\"'lat. medeor -eri „heilen“, medicus „Arzt“'.\"),\n   dict(src=\"POK\", where=\"IEW 705-706\", stance=\"supports\", note=\"'Latin medeor, -erī „to heal, cure, remedy, be good for“, medicus „physician, medicine man“'.\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=8, lang=\"English\", words=\"medicine, remedy, moderate\",\n verdict=\"confirmed\",\n derivation=\"All three are Latin loans of the med- family that reached English through French. medicine: Lat. medicīna (ars) 'the healing art', fem. of medicīnus, from medicus < medērī; Old French medecine, Middle English medicine (13th c.). remedy: Lat. remedium (re- + medērī), Anglo-Norman remedie, ME remedie. moderate: Lat. moderātus, past participle of moderārī 'to keep within measure, restrain', which is built not on medērī but on the e-grade *med-es-, whose vowel was pulled to -o- by modus (Ernout-Meillet: 'l'autre, de sens concret … à vocalisme en -e-, *medos, attesté indirectement par le dérivé modestus … et par le verbe moderor'; Watkins med- 3b '*med-es-, replaced in Latin by *modes- by influence of modus'). So 'moderate' strictly belongs on the modus side of the fork rather than in the medērī box, but it is inside the same root, and Buck's MEDICINE article (5.88, p.309-310) treats medicāmen/medicīna/remedium as one family 'medērī „heal“. Hence It. medicina, Fr. médicament (OFr. medecine > ME, NE medicine)'.\",\n derivation_fa=\"هر سه واژه از خانوادهٔ لاتینی med- اند و از راه فرانسه به انگلیسی رسیده‌اند. medicine از medicīna (ars) لاتینی «هنر درمان»، مؤنث medicīnus از medicus و آن از medērī، از راه فرانسهٔ کهن medecine در سدهٔ سیزدهم میلادی وارد انگلیسی میانه شد. remedy از remedium (پیشوند re- + medērī) از راه انگلونورمن remedie. اما moderate از moderātus، اسم مفعول moderārī «در اندازه نگاه داشتن»، است که نه بر medērī بلکه بر ستاک *med-es- ساخته شده و واکهٔ آن زیر تأثیر modus به o بدل شده است (ارنو-مِیه و واتکینز هر دو همین را می‌گویند). پس «moderate» به‌دقت در شاخهٔ modus جای می‌گیرد نه در جعبهٔ medērī، هرچند هر دو زیر یک ریشه‌اند. ادعای نورایی در کل درست است.\",\n sources=[],\n ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"the box carries no reference of its own; the parent Latin box's 'AHD' covers all three words (Watkins med- 2a for MEDICINE and REMEDY, 3b for MODERATE).\")],\n consulted=[\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. med-\", stance=\"supports\", note=\"'MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEGLIN, REMEDY' under medērī, and 'Latin moderāre, „to keep within measure“, to moderate, control: MODERATE; IMMODERATE' under *med-es-/*modes-.\"),\n   dict(src=\"SYN\", where=\"Buck 5.88 MEDICINE, DRUG, printed pp. 309-310\", stance=\"supports\", note=\"'2. Lat. medicāmen(tum), medicīna (also „medical science“), remedium (but with extension beyond medical sense, as likewise its derivs. Fr. remède, NE remedy, etc.) : medērī „heal“ … OFr. medecine > ME, NE medicine.'\"),\n   dict(src=\"LAT\", where=\"Ernout-Meillet s.vv. medeor, modus\", stance=\"supports\", note=\"on modus: 'contamination de deux noms différents; l'un … à vocalisme en o, modus; l'autre … à vocalisme en -e-, *medos, attesté indirectement par le dérivé modestus … et par le verbe moderor.'\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=9, lang=\"Latin\", words=\"modus\",\n verdict=\"confirmed\",\n derivation=\"Latin modus, -ī m., the o-grade *mod-o- of the root: 'measure (of surface, and especially of land, modus agrī); in the moral sense the measure one must not exceed, moderation; in rhetoric and music, rhythm, musical measure; hence limit; hence manner, way' (Ernout-Meillet, who also notes that the classical noun is a contamination of two stems, o-grade modus and e-grade *medos, the latter surviving only in modestus and moderor). Watkins: '4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, manner, harmony, melody' — Nourai's one-word gloss 'size' is lifted from that string, so it is not wrong but it is only one corner of the word's range. The 'AHD' reference is the right one.\",\n derivation_fa=\"واژهٔ لاتینی modus صورت o-دارِ ریشه (*mod-o-) است: «اندازه» (به‌ویژه اندازهٔ زمین، modus agrī)، سپس «حدّ و مرزی که نباید از آن گذشت، اعتدال»، در بلاغت و موسیقی «وزن، ضرب»، و از آنجا «حد» و سرانجام «شیوه، روش». ارنو-مِیه می‌افزایند که این اسمِ کلاسیک آمیزهٔ دو ستاک است: modus با واکهٔ o و *medos با واکهٔ e که تنها در modestus و moderor بازمانده است. واتکینز نیز می‌نویسد «*mod-o- در لاتینی modus: اندازه، سایز، حد، شیوه، هماهنگی، آهنگ» — و معنیِ تک‌واژه‌ایِ «size» که نورایی آورده از همین رشته برگرفته شده است؛ نادرست نیست ولی تنها گوشه‌ای از معنای واژه است. ارجاع به AHD درست است.\",\n sources=[],\n ref_check=[dict(ref=\"AHD\", status=\"supports\", note=\"Watkins 1985 s.v. med-: '4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, manner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD¹, (MOOD²), (MOULAGE); (ACCOMMODATE), (COMMODE), COMMODIOUS, (COMMODITY).'\")],\n consulted=[\n   dict(src=\"LAT\", where=\"Ernout-Meillet s.v. modus (LAT.txt line ~38497)\", stance=\"supports\", note=\"'modus, -ī m. (contamination de deux noms différents … à vocalisme en o, modus; l'autre … *medos, attesté indirectement par le dérivé modestus … et par le verbe moderor) … mesure de surface … et surtout mesure agraire, modus agrī. … Du sens de „mesure“, modus est passé à celui de „limite“ … et aussi à celui de „manière“.'\"),\n   dict(src=\"IEC\", where=\"Mann, s.v. modos, -es-\", stance=\"supports\", note=\"'modos, -es- „measure, means“. Cf. mēd-. WP II, 259 Lat. modus, gs -ī, but archaic *modes- implied in modes-tus, moder-āre … Mir. muidh, mod. modh … „mode, measure, honour“; ON mat, n. „assessment, tax“.'\"),\n   dict(src=\"POK\", where=\"IEW 705\", stance=\"supports\", note=\"'Latin … modus „a measure, extent, quantity“, modestus …, moderāre …, modius „bushel“'.\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=10, lang=\"French\", words=\"\",\n verdict=\"confirmed\",\n derivation=\"A pass-through box for the French intermediaries by which this branch reached Persian: modèle (16th c., borrowed from Italian modello < Vulgar Latin *modellus, diminutive of modulus, itself the diminutive of modus), moderne (14th c., from Late Latin modernus, formed on the adverb modo 'just now', itself the ablative of modus), and commode (16th c. adjective, 18th c. as the noun for a chest of drawers, from Latin commodus 'fit, suitable', literally 'measured with', com- + modus — so Klein s.v. commode). All three are the actual etyma of the three Persian words in the next box, so the box is correctly placed even though it carries no words.\",\n derivation_fa=\"جعبه‌ای گذری برای میانجی‌های فرانسوی این شاخه که واژه‌ها را به فارسی رساندند: modèle (سدهٔ شانزدهم، وام از ایتالیایی modello از لاتینی عامیانه *modellus، مصغرِ modulus که خود مصغرِ modus است)، moderne (سدهٔ چهاردهم، از لاتینی متأخر modernus ساخته بر قید modo «هم‌اکنون» که حالت ازی modus است)، و commode (صفت در سدهٔ شانزدهم و اسم «گنجهٔ کشودار» در سدهٔ هجدهم، از لاتینی commodus «مناسب»، تحت‌اللفظ «هم‌اندازه»، از com- + modus؛ چنان‌که کلاین ذیل commode می‌آورد). هر سه دقیقاً نیای سه واژهٔ فارسی جعبهٔ بعدی‌اند، پس جای‌گذاری این جعبه درست است هرچند تهی است.\",\n sources=[],\n ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"no reference on the box; the parent's 'AHD' lists MODEL, MODERN and COMMODE under modus.\")],\n consulted=[\n   dict(src=\"KLN\", where=\"Klein s.v. commode (KLN_1966.txt line 8386)\", stance=\"supports\", note=\"'commode, n., 1) a chest of drawers; 2) a movable washstand. — F., fr. commode, „convenient, serviceable, comfortable“, fr. L. commodus, „fit, suitable, convenient“, lit. „measured with“, fr. com- and modus, „measure, manner, mode“.'\"),\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. med- §4\", stance=\"supports\", note=\"MODEL, MODERN, MODULE, MODULUS, (COMMODE) all listed under Latin modus.\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=11, lang=\"Persian\", words=\"مدل ، مدرن ، کمد\",\n verdict=\"confirmed\",\n derivation=\"Three modern European loans in Persian, all taken from French in the late Qajar/early Pahlavi period through French-medium schooling and the press: مدل model < Fr. modèle 'pattern, model'; مدرن modern < Fr. moderne 'modern'; کمد komod 'chest of drawers, wardrobe' < Fr. commode. Moʿin's Farhang-e Fārsi tags each entry with its French source form: 'مدل: model (ا.) الگو، نمونه، سرمشق', 'مدرن: moderne (ص.) تازه، نو، باب روز' (with the usage note that many writers avoid this foreign word), 'کمد: commode (ا.) گنجهٔ دارای کشو …' with the compounds کمد بایگانی and کمد جالباسی. The French pronunciation is preserved (komod, not *kommod), and کمد is not to be confused with the Arabic root k-m-d. Nourai's bare 'MON' reference is exactly right.\",\n derivation_fa=\"سه وام‌واژهٔ اروپاییِ نو در فارسی که همگی در اواخر دورهٔ قاجار و آغاز پهلوی از راه فرانسه — مدرسه و مطبوعاتِ فرانسه‌زبان — وارد شده‌اند: «مدل» از modèle فرانسوی، «مدرن» از moderne، و «کمد» از commode. معین در فرهنگ فارسی هر سه را با صورت فرانسویشان نشان می‌دهد: «مدل: model (اِ.) الگو، نمونه، سرمشق»؛ «مدرن: moderne (ص.) تازه، نو، باب روز» با این توضیح که «بسیاری از استعمال این کلمهٔ بیگانه احتراز دارند»؛ و «کمد: commode (اِ.) گنجهٔ دارای کشو …» با ترکیب‌های «کمد بایگانی» و «کمد جالباسی». تلفظ فرانسوی «کمد» (komod) حفظ شده و آن را نباید با مادهٔ عربی ک‌م‌د اشتباه گرفت. ارجاع کوتاه نورایی به «MON» کاملاً بجاست.\",\n sources=[],\n ref_check=[dict(ref=\"MON\", status=\"supports\", note=\"Moʿin, Farhang-e Fārsi (MON_part2.txt line 51833 'مدل: model (اِ.) الگو، نمونه، سرمشق'; line 51717 'مدرن: moderne (ص.) تازه، نو، باب روز'; MON 2-vol. line 26321 'کمد: commode (اِ.) گنجهٔ دارای کشو که در …') — every one of Nourai's three words is tagged in Moʿin with its French etymon.\")],\n consulted=[\n   dict(src=\"MON\", where=\"Moʿin, Farhang-e Fārsi s.vv. مدل، مدرن، کمد\", stance=\"supports\", note=\"see ref_check; Moʿin prints the Latin-script French source beside each headword.\"),\n   dict(src=\"KLN\", where=\"Klein s.v. commode\", stance=\"supports\", note=\"'F., fr. commode … fr. L. commodus … fr. com- and modus' — the French word behind کمد is itself from modus, so the whole chain root > Latin > French > Persian holds.\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=12, lang=\"English\", words=\"mode, model, modern, modest, module, turmoil, mold, mood, commode\",\n verdict=\"plausible\",\n derivation=\"Eight of the nine are exactly Watkins' list under Latin modus: 'MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD¹, (MOOD²), (MOULAGE); (ACCOMMODATE), (COMMODE), COMMODIOUS, (COMMODITY)', with MODEST placed one line earlier under the *med-es-/*modes- variant. In detail: mode < Fr. mode < modus; model < Fr. modelle/It. modello < *modellus (dim. of modulus); modern < LLat. modernus; module/modulus < Lat. modulus; mold¹ 'shape, matrix' < OFr. modle, molle < modulus; commode < Fr. commode < Lat. commodus (Klein: 'lit. „measured with“, fr. com- and modus'); mood is the grammatical mood², a variant spelling of mode (Skeat: 'Mood (2), manner, grammatical form; see Mode'), quite distinct from mood¹ 'state of mind' < OE mōd, which Watkins files under mē-1. The weak link is turmoil (verb 1510s, noun 1520s): Watkins does not list it at all; Etymonline calls the origin uncertain and offers 'perhaps an alteration of French tremouille „mill hopper“'; Skeat derives tremouille from Lat. tremere 'to tremble'; but the CNRTL/Littré etymology of Fr. trémie takes it from Latin trimodia/trimodius 'a vessel of three modii' (trēs + modius), which would indeed hang turmoil on the modius branch of this same root. So the arrow is defensible but nowhere established — hence 'plausible' for the box as a whole.\",\n derivation_fa=\"هشت واژه از نُه واژهٔ این جعبه عیناً همان فهرستی است که واتکینز ذیل modus لاتینی می‌آورد؛ «modest» را نیز یک سطر بالاتر ذیل گونهٔ *med-es-/*modes- می‌گذارد. به‌تفصیل: mode از modus از راه فرانسه؛ model از modello ایتالیایی/modelle فرانسوی از *modellus، مصغرِ modulus؛ modern از modernus لاتینی متأخر؛ module و modulus از modulus؛ mold «قالب» از modle فرانسهٔ کهن از modulus؛ commode از commode فرانسوی از commodus لاتینی («هم‌اندازه»، به گفتهٔ کلاین)؛ و mood در اینجا «وجهِ» دستوری است، گونهٔ دیگری از mode (اسکیت: «Mood (2)، شیوه، صورت دستوری؛ نگاه کنید به Mode»)، نه mood به معنای «حال و هوا» که از mōd انگلیسی کهن است و واتکینز آن را زیر mē-1 می‌آورد. حلقهٔ سست، turmoil است: واتکینز اصلاً آن را نمی‌آورد، Etymonline خاستگاهش را نامعلوم می‌داند و شاید دگرگون‌شدهٔ tremouille فرانسوی «قیفِ آسیاب» می‌شمارد، و اسکیت آن را به tremere لاتینی «لرزیدن» می‌بندد؛ اما ریشه‌شناسیِ CNRTL و لیتره برای trémie فرانسوی آن را از trimodia/trimodius لاتینی («ظرفِ سه مودیوس»، از trēs + modius) می‌گیرد که در آن صورت turmoil به شاخهٔ modius همین ریشه می‌پیوندد. پس این پیکان دفاع‌پذیر است ولی اثبات‌شده نیست؛ از این‌رو حکم جعبه «با احتیاط پذیرفتنی» است.\",\n sources=[\"https://www.etymonline.com/word/turmoil\",\"https://www.cnrtl.fr/etymologie/tr%C3%A9mie\"],\n ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"no reference on the box; the parent Latin box's 'AHD' covers everything except turmoil, which Watkins does not list (grep 'TURMOIL' in AHD_watkins1985.txt returns 0 hits).\")],\n consulted=[\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. med- §3-4 and Index\", stance=\"partial\", note=\"§4 lists MODE, MODEL, MODERN, MODULE, MODULUS, MOLD¹, (MOOD²), (COMMODE); §3a lists MODEST. Index line: 'MOOD¹ mē-1 / MOOD² med-'. TURMOIL is absent from the whole book.\"),\n   dict(src=\"SKT\", where=\"Skeat s.vv. Turmoil, Mood (2)\", stance=\"partial\", note=\"'Turmoil … probably a corrupt form … Prob. from F. trémouille, „the hopper of a mill“ … So named from being in continual motion. — L. tremere, to tremble.' — Skeat keeps turmoil away from modus; but 'Mood (2), manner, grammatical form; see Mode' confirms mood².\"),\n   dict(src=\"KLN\", where=\"Klein s.v. commode\", stance=\"supports\", note=\"'F., fr. commode … fr. L. commodus, „fit, suitable, convenient“, lit. „measured with“, fr. com- and modus.'\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=13, lang=\"Germanic\", words=\"\",\n verdict=\"plausible\",\n derivation=\"A pass-through box for the Germanic o-grade *mōt- 'ability, leisure, permission' — Gothic ga-mōtan 'to find room, be permitted', OE mōtan 'to be allowed, have occasion', OS mōtan, OHG muoz/muozan, NHG müssen; with the nouns OHG muoza 'leisure', OE ǣmetta 'leisure'. Pokorny files them here explicitly as the 'ō-grade' of mēd-1 (IEW 705), and Watkins repeats it but with an audible hedge: '6. Possibly lengthened o-grade form *mōd- in Germanic *mōt-, ability, leisure'. Mann's Indo-European Comparative Dictionary instead sets the same Germanic material under a separate root mod- 'against, towards; encounter, approach … be obliged' (WP II 304), alongside Hittite mac- 'oppose' and Armenian mut 'approach'; and Klein and Skeat give the Germanic paradigm with no IE root at all. So the box reproduces the standard handbook (Pokorny/Watkins) but the connection is not secure.\",\n derivation_fa=\"جعبه‌ای گذری برای ستاک ژرمنی *mōt- «توانایی، فراغت، اجازه»: گوتیک ga-mōtan «جا یافتن، اجازه داشتن»، انگلیسی کهن mōtan، ساکسون کهن mōtan، آلمانی علیای کهن muoz/muozan و آلمانی امروز müssen؛ و اسم‌های muoza «فراغت» و ǣmetta «فراغت». پوکورنی این‌ها را صریحاً «صورتِ ō-دارِ» mēd-1 می‌داند (ص ۷۰۵) و واتکینز همان را با احتیاط تکرار می‌کند: «شاید صورتِ کشیدهٔ *mōd- در ژرمنیِ *mōt-». اما مان در فرهنگ تطبیقی هندواروپایی همین مواد ژرمنی را زیر ریشهٔ جداگانهٔ mod- «رو در رو، برخورد، ناگزیر بودن» (والده-پوکورنی ج۲ ص۳۰۴) در کنار هیتی mac- «مخالفت کردن» و ارمنی mut «نزدیک شدن» می‌گذارد؛ کلاین و اسکیت هم هیچ ریشهٔ هندواروپایی برای آن نمی‌آورند. پس این جعبه بازتابِ کتاب مرجع رایج است، ولی پیوند قطعی نیست.\",\n sources=[],\n ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"no reference on the box; the connection is Pokorny's (IEW 705, 'ō-grade: Gothic ga-mōt „may, find space, have place, permission“, Old English mōtan …').\")],\n consulted=[\n   dict(src=\"POK\", where=\"IEW 705, mēd-1\", stance=\"supports\", note=\"'ō-grade: Gothic ga-mōt „may, find space, have place, permission“, Old English mōtan „can, to be able, have the occasion“ (engl. must „must, have to“ from the preterit) … Old High German muoz, muozan … Modern High German müssen'.\"),\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. med- §6\", stance=\"partial\", note=\"'6. Possibly lengthened o-grade form *mōd- in Germanic *mōt-, ability, leisure' — the hedge 'Possibly' is Watkins' own.\"),\n   dict(src=\"IEC\", where=\"Mann, s.v. mod- (WP II, 304)\", stance=\"contradicts\", note=\"'mod- „against, towards; encounter, approach, contact, fitting“. WP II, 304 … Go. ga-motjan, v. „meet“ beside ga-motan, v. „be obliged“; mota, f. „toll“ … OHG muoza, f. …; muoz „I may, must“; Du. muot … OE metan, v. „meet; acquire“; mōt …' — Mann puts the whole must-group under a different root.\"),\n ],\n))\n\nentry0_nodes.append(n(\n id=14, lang=\"English\", words=\"must 1 : have to; empty\",\n verdict=\"confirmed\",\n derivation=\"Both English words are in the box because Watkins puts them side by side in a single sub-paragraph: '6. … a. Old English mōtan, to have occasion, to be permitted or obliged: MOTE², MUST¹; b. Germanic compound ē-mot-ja- (prefix *ē-, meaning uncertain) in Old English ǣmetta, rest, leisure: EMPTY.' must¹ is historically a preterite: ME moste < OE mōste, past of mōtan (Klein: 'must, aux. v., am (or is, are) obliged to. — ME. moste, fr. OE. moste, pret. of mōtan, „to be allowed to, be able to, have opportunity to, have to“'; Skeat: 'Only the pt. t. remains, which is now also used as a present'), and the preterite-turned-present is common Germanic (Du. moeten, G. müssen, Sw. måste). empty is OE ǣmtig/ǣmetig 'vacant, free, idle', an -ig adjective on ǣmetta 'leisure', itself privative ǣ- + the stem of (ge)mōt 'meeting' — so literally 'without a meeting to attend, at leisure'; the -p- of the modern spelling is excrescent (cf. glimpse, sempstress). Pokorny has the same pair: 'Old English ǣ-metta … whereof ǣm(e)tig = engl. empty'. Nourai's box is Watkins transcribed, and the printed page really carries both words, so the extraction is faithful. The only caveat is the one carried down from the Germanic box: neither Klein nor Skeat commits to an Indo-European root for this group.\",\n derivation_fa=\"هر دو واژهٔ انگلیسی از آن‌رو در یک جعبه‌اند که واتکینز آن‌ها را در یک بند کنار هم آورده است: «انگلیسی کهن mōtan … : MOTE²، MUST¹؛ و ترکیب ژرمنی ē-mot-ja- در انگلیسی کهن ǣmetta „فراغت“ : EMPTY». واژهٔ must در اصل صورتِ گذشته است: انگلیسی میانه moste از mōste انگلیسی کهن، گذشتهٔ mōtan (کلاین: «ME moste، گذشتهٔ mōtan „اجازه داشتن، توانستن، ناگزیر بودن“»؛ اسکیت: «تنها صورت گذشته مانده که اکنون در معنای حال به کار می‌رود») — و این تبدیلِ گذشته به حال در همهٔ زبان‌های ژرمنی دیده می‌شود (هلندی moeten، آلمانی müssen، سوئدی måste). واژهٔ empty از ǣmtig/ǣmetig انگلیسی کهن «تهی، آزاد، بیکار» است، صفتی با پسوند -ig بر ǣmetta «فراغت» که خود از پیشوند سلبیِ ǣ- و ستاکِ (ge)mōt «انجمن، دیدار» ساخته شده، یعنی تحت‌اللفظ «بی‌انجمن، فارغ»؛ حرف p در املای امروزی زائد و میان‌افزوده است. پوکورنی نیز همین جفت را می‌آورد. پس این جعبه رونوشتِ واتکینز است و صفحهٔ چاپی هم هر دو واژه را دارد؛ خوانش اسکن درست است. تنها احتیاط، همان است که از جعبهٔ ژرمنی به ارث رسیده: کلاین و اسکیت ریشهٔ هندواروپایی‌ای برای این گروه قائل نیستند.\",\n sources=[],\n ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"no reference on the box; the pairing is Watkins' (med- §6a-b) and Pokorny's (IEW 705).\")],\n consulted=[\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. med- §6\", stance=\"supports\", note=\"'a. Old English mōtan, to have occasion, to be permitted or obliged: MOTE², MUST¹; b. Germanic compound ē-mot-ja- … in Old English ǣmetta, rest, leisure: EMPTY.' — Nourai's box is this sub-paragraph.\"),\n   dict(src=\"KLN\", where=\"Klein s.vv. must (aux. v.), empty (adj.)\", stance=\"partial\", note=\"'must, aux. v. … ME. moste, fr. OE. moste, pret. of motan …' and 'empty, adj. — ME. emtie, empti, fr. OE. ǣmetig, ǣmtig, „vacant, free, idle“, formed with suff. -ig … fr. ǣmetta, „leisure“. This latter is formed fr. priv. ǣ- and the stem of (ge)mōt, „meeting“.' — the words are right, but Klein stops at Germanic.\"),\n   dict(src=\"SKT\", where=\"Skeat s.vv. Must (1), Empty\", stance=\"partial\", note=\"'Must (1) … Only the pt. t. remains, which is now also used as a present … A.S. ic mōt, pres. t.; ic mōste, I must, pt. t.' and 'Empty, void … A.S. ǣmtig, lit. full of leisure. — A.S. ǣmetta, leisure' — same, without an IE root.\"),\n   dict(src=\"POK\", where=\"IEW 705\", stance=\"supports\", note=\"'Old English ǣ-metta, ǣmta, from *ǣ-mōtida „leisure“, whereof ǣm(e)tig = engl. empty „empty, bare, lacking“'.\"),\n ],\n))\n\nentry2_nodes = []\n\nentry2_nodes.append(n(\n id=1, lang=\"Avestan\", words=\"madhu : honey; madha : wine\",\n verdict=\"plausible\",\n derivation=\"The first word is right, the second belongs to a different root. (a) Av. maδu- n. is real — Bartholomae glosses it '(Wein usw.) Beerenwein' (AiW 1114; V.5.52-54), Walde-Pokorny II 261 'av. maδu „Beerenwein“', Buck p.389 'Av. maδu- was a kind of wine or beer (Barth. 1114)'. Nourai's spelling 'madhu' is his standing transliteration of Avestan δ as 'dh' (he writes maδa- as 'madha' in the same box), so it is a convention, not a Sanskritism, though the gloss 'honey' properly belongs to Skt. mádhu-: in Avestan the word had already narrowed to 'berry wine'. (b) Av. maδa- 'intoxicating drink, wine' (AiW s.v.: 'Rauschtrank, Wein', of haoma at Y.10.8) is NOT from *médʰu: it goes with Skt. máda- 'intoxication', mad- 'be drunk', Lat. madēre 'to be wet', i.e. PIE *mad- (Pokorny 694-695) — Buck says so explicitly on p.390. Nourai puts the two in one box because they merged in New Persian, which is precisely what Horn no. 1003 says ('In np. mei, phlv. mai sind aw. madv- „Honig“ … und aw. maδa- „Rauschtrank“ … zusammengefallen'). Read that way the box is defensible; read as an etymological claim about a single root it is half wrong.\",\n derivation_fa=\"واژهٔ نخست درست است و واژهٔ دوم به ریشه‌ای دیگر تعلق دارد. الف) maδu- اوستایی واقعی است؛ بارتولمه آن را «شرابِ توت/انگور» (Beerenwein، ستون ۱۱۱۴)، والده-پوکورنی «av. maδu „Beerenwein“» و باک «maδu- اوستایی گونه‌ای شراب یا آبجو بود» معنی می‌کنند. نوشتنِ «madhu» شیوهٔ ثابتِ نورایی برای نشان‌دادنِ ذالِ اوستایی با «dh» است (در همین جعبه maδa- را هم «madha» نوشته)، پس آوانگاری است نه صورت سنسکریت؛ اما معنیِ «عسل» در اصل از آنِ mádhu- سنسکریت است، چون در اوستایی معنا به «شرابِ میوه» تنگ شده بود. ب) maδa- اوستایی «مشروب مستی‌آور، شراب» (بارتولمه: Rauschtrank) از *médʰu نیست؛ با máda- سنسکریت «مستی»، mad- «مست شدن» و madēre لاتینی «تر بودن» هم‌ریشه است، یعنی از *mad- هندواروپایی (پوکورنی صص ۶۹۴–۶۹۵)؛ باک در ص ۳۹۰ همین را صریح می‌گوید. نورایی این دو را در یک جعبه گذاشته چون در فارسی نو با هم یکی شده‌اند — و این دقیقاً همان چیزی است که هرن در شمارهٔ ۱۰۰۳ می‌نویسد: «در «مِی» فارسی و mai پهلوی، madv- اوستایی „عسل“ و maδa- اوستایی „مشروب مستی‌آور“ در هم آمیخته‌اند». با این خوانش جعبه پذیرفتنی است؛ اما اگر ادعای ریشه‌شناختیِ یگانه باشد، نیمی از آن نادرست است.\",\n sources=[W+\"Reconstruction:Proto-Indo-European/m%C3%A9d%CA%B0u\"],\n ref_check=[dict(ref=\"POK:707\", status=\"partial\", note=\"POK_full.txt, 'Root / lemma: medʰu / Meaning: honey, intoxicating drink, mead … Page(s): 707': 'Old Indie madhu- n. „honey, mead“ … Avestan madu- n. „berry wine“; gr. μέθυ „wine“'. maδu- is on the page; maδa- is not — Pokorny has it only as a cross-reference note ('Root/lemma: mad-: wet; glossy, fat, well-fed, intoxicating : Root/lemma: medʰu: honey, intoxicating').\")],\n consulted=[\n   dict(src=\"BRT\", where=\"AiW cols. 1114 (maδav-) and s.v. maδa-\", stance=\"supports\", note=\"BRT.txt: '• j. maδav- n. „(Wein uzw.) Beerenwein“: gąmca .. yaomca .. maδuca anaptəm V.5.52; 53, 54' and, for maδa-, '2) „Rauschtrank, Wein“ … vīspe zi anye maδāŋhō aēšma haθente … Y.10.8' — both Avestan words exist with exactly the meanings Nourai gives.\"),\n   dict(src=\"WLD\", where=\"Walde-Pokorny Bd. II 261\", stance=\"supports\", note=\"'*medʰu n. „Honig; bes. Met“ … Ai. mádhu „Honig, Met“ … av. maδu „Beerenwein“; tochar. B mit „Honig“; gr. μέθυ „Wein“ (aus „Rauschtrank“; die Bed. „Honig“ hat sich auf μέλι zurückgezogen).'\"),\n   dict(src=\"SYN\", where=\"Buck 5.91 MEAD p.389 and 5.92 WINE p.390\", stance=\"partial\", note=\"p.389 'Av. maδu- was a kind of wine or beer (Barth. 1114)'; but p.390 'Skt. mada- „intoxication“ and Av. maδa- „intoxicating drink“ : Skt. mad- „be glad, be drunk“, Lat. madēre „be wet“, etc. (Walde-P. 2.230f.)' — Buck separates maδa- from medʰu-.\"),\n ],\n))\n\nentry2_nodes.append(n(\n id=2, lang=\"Persian\", words=\"may «می»; mol «مُل»\",\n verdict=\"disputed\",\n derivation=\"may is confirmed, mol is not. (a) NP می may 'wine' < Middle Persian may (written mdy, and very often with the Aramaic heterogram ḤMR — MacKenzie: 'may [HS < A hmr ?; mdy | M my, N ~] wine') < Proto-Iranian *madu- < PIE *médʰu, with loss of intervocalic δ and the -u glide giving -y. Moʿin's own footnote on exactly the page Nourai cites (BQT p.2071 n.5) sets it out: «تلفظ فارسی متأخر māy، تلفظ قدیم may … پهلوی may، اوستایی maδu- (عسل)، هندی باستان mádhu- (شیرین، عسل)، نیز اوستا maδa- (مشروب مستی‌آور)، هندی باستان máda-، قس: اسلاوی کلیسایی medŭ (عسل، شراب)؛ آلمانی Met؛ [هرن] ۱۰۰۳»; Buck p.389 has '(NPers. mai „wine“, Horn 1003)'; Mann lists 'Per. may „wine“' under medhu; Wiktionary (after Edelʹman, ESIJa V 116) gives Persian می < MP mdy /may/ < Proto-Iranian *mádu < PIE *médʰu. (b) مُل mol 'wine' is a different story. Horn treats it under a separate number, no. 990 on p.222 — NOT the page Nourai cites — and derives it from Skt. mṛdvīkā- 'grape, grape-wine' after Hübschmann, ZDMG 35, 133 n.2; Moʿin's footnote to the مل entry (which is at BQT p.2030, again not 2071) repeats that: «هندی باستان mṛdvīkā- (شراب انگوری)، [هرن] ۹۹۰ … قس: فارسی «می». تبدیل «ل» و «ذ» درین دو زبان سابقه دارد», i.e. mṛdvīkā is the source and may is only a comparison. Nourai's own NOTE ('For another possible root of “mol“ see Mer 2') registers the alternative, and modern scholarship takes that alternative, not the medhu one. The šāhed Nourai quotes — «به زرّینه جام اندرون لعل مل / فروزنده چون لاله بر زرد گل», ʿOnṣorī of Balkh — is the same verse Moʿin prints under مل (from Loghat-e Fors 322-323), so the attribution is correct.\",\n derivation_fa=\"«می» تأیید می‌شود، «مُل» نه. الف) «می» فارسی از may فارسی میانه (نوشته mdy، و بسیار اوقات با هزوارشِ آرامیِ ḤMR؛ مکنزی: «may [HS < A hmr ?; mdy] wine») و آن از ایرانی آغازین *madu- و از هندواروپایی *médʰu است؛ ذالِ میان‌واکه‌ای افتاده و -u به یای پایانی بدل شده. حاشیهٔ خودِ معین در همان صفحه‌ای که نورایی ارجاع داده (برهان قاطع ص ۲۰۷۱، پانوشت ۵) دقیقاً همین را می‌گوید: «تلفظ فارسی متأخر māy، تلفظ قدیم may … پهلوی may، اوستایی maδu- (عسل)، هندی باستان mádhu-، نیز اوستا maδa- (مشروب مستی‌آور) … قس اسلاوی کلیسایی medŭ، آلمانی Met، [هرن] ۱۰۰۳». باک نیز در ص ۳۸۹ می‌نویسد «NPers. mai „wine“، هرن ۱۰۰۳» و مان زیر medhu «Per. may „wine“» می‌آورد؛ ویکی‌واژه هم به‌پیروی از ادلمان (فرهنگ ریشه‌شناختی زبان‌های ایرانی، ج۵ ص۱۱۶) همین زنجیره را می‌دهد. ب) «مُل» داستان دیگری دارد: هرن آن را زیر شمارهٔ جداگانهٔ ۹۹۰ در صفحهٔ ۲۲۲ — نه صفحه‌ای که نورایی ارجاع داده — از mṛdvīkā- سنسکریت «انگور، شراب انگوری» می‌گیرد (به‌پیروی از هوبشمان)، و حاشیهٔ معین بر مدخل «مل» (که در برهان قاطع ص ۲۰۳۰ است، نه ۲۰۷۱) همان را تکرار می‌کند: «هندی باستان mṛdvīkā- (شراب انگوری)، [هرن] ۹۹۰ … قس: فارسی «می». تبدیل «ل» و «ذ» درین دو زبان سابقه دارد» — یعنی mṛdvīkā خاستگاه است و «می» فقط برای سنجش آمده. یادداشت خودِ نورایی («برای ریشهٔ محتملِ دیگرِ mol نگاه کنید به Mer 2») همین گزینه را ثبت کرده و پژوهش امروزی هم همان را می‌پذیرد نه medhu را. شاهدِ نقل‌شده — «به زرّینه جام اندرون لعل مل / فروزنده چون لاله بر زرد گل» از عنصری بلخی — همان بیتی است که معین ذیل «مل» از لغت فرس آورده، پس انتساب درست است.\",\n sources=[W+\"%D9%85%DB%8C\"],\n ref_check=[\n   dict(ref=\"BQT:2071\", status=\"partial\", note=\"ref_page.py BQT:2071 (BQT_v4_picofile.pdf pdf page 154) is indeed the «می» page — «می * بفتح اول و سکون ثانی، شراب انگور را کوبند …» with footnote 5 giving پهلوی may، اوستایی maδu-، هندی باستان mádhu-، نیز اوستا maδa- and the reference «۱۰۰۳» to Horn. But مُل is NOT on this page: its entry is in «بیان بیست و سیم، در میم با لام» at BQT_v4 pdf page 113 = printed p.2030, where Moʿin derives it from mṛdvīkā-.\"),\n   dict(ref=\"HRN:225\", status=\"partial\", note=\"HRN.txt leaf 246 = printed p.225 is entry '1003. mei „Wein, jüd.-pers.“: In np. mei, phlv. mai, vd. 5 (132), sind aw. madv- „Honig“, ai. mādhu- „süss; Honig, Meth“ und aw. maδa- „Rauschtrank“, ai. máda- das. zusammengefallen; vergl. ksl. medŭ „Honig, Wein“, nhd. Meth etc.' — full support for may. Horn's mul is a different entry, no. 990 on p.222: 'mul „Wein“. ai. mṛdvīkā- „Weintraube“ (Hübschmann, ZDMG. 35, 133 Note 2)' — not medʰu.\"),\n   dict(ref=\"SYN:389\", status=\"supports\", note=\"Buck 5.91 MEAD, printed p.389 (SYN.txt leaf 436-437): the discussion of IE *medhu- ends '… (NPers. mai „wine“, Horn 1003)' — Buck files NP may under this root, exactly as the chart does.\"),\n ],\n consulted=[\n   dict(src=\"PHD\", where=\"MacKenzie, CPD s.v. may\", stance=\"supports\", note=\"PHD.txt: 'may [HS < A hmr ?; mdy | M my, N ~] wine.' — the Middle Persian ancestor with the Aramaic heterogram, and the New Persian outcome.\"),\n   dict(src=\"HRN\", where=\"Horn nos. 1003 (p.225) and 990 (p.222)\", stance=\"partial\", note=\"no. 1003 supports may from Av. madv-/maδa-; no. 990 derives mul from Skt. mṛdvīkā- — Horn keeps the two words apart.\"),\n   dict(src=\"IEC\", where=\"Mann, s.v. medhu\", stance=\"supports\", note=\"'medhu „sweet drink, liquid honey, mead“ … Skt. mádhu; Av. maδu „honey, mead“; Per. may „wine“; Oss. mid, mud „honey“; Tokh. B mit; Gk. méthu „wine“' — may is in Mann's descendant list; mol is not.\"),\n   dict(src=\"BQT\", where=\"Borhan-e Qateʿ pp. 2030 (مل) and 2071 (می), with Moʿin's footnotes\", stance=\"partial\", note=\"p.2071 footnote supports may; p.2030 footnote on مل: «هندی باستان mṛdvīkā- (شراب انگوری) [هرن] ۹۹۰ … قس: فارسی «می». تبدیل «ل» و «ذ» درین دو زبان سابقه دارد» plus the ʿOnṣorī verse «به زرّینه جام اندرون لعل مل / فروزنده چون لاله بر زرد گل» from Loghat-e Fors 322-323.\"),\n ],\n))\n\nentry2_nodes.append(n(\n id=3, lang=\"Sogdian\", words=\"mwd\",\n verdict=\"confirmed\",\n derivation=\"Sogdian mwδ /muδ/ 'wine' — Gharib's Sogdian-Persian-English Dictionary entry no. 5511, on printed p.221: 'mwδ2 S — muδ (mwd) =» mδw — wine', cross-referenced to the Buddhist-script spelling mδw (no. 5295, p.211: 'mδw B, M, S — wine — maδu (mδw)') and the Christian mdw (no. 5296), with the ideogram ɣMRH (no. 4059, p.162, '=»mδw … wine' — the same Aramaic ḤMR heterogram that Pahlavi uses for may). The word continues Proto-Iranian *madu- directly, with the regular Sogdian loss of the final vowel and preservation of the intervocalic δ that Persian lost; the Wiktionary *médʰu page likewise lists 'Sogdian 𐼺𐼴𐼹 (mwδ /muδ/)'. Nourai's 'mwd' is the standard transliteration mwδ with δ typed as plain d, and the printed page shows 'mwd', so the extraction is faithful; his page 220 is a single page short of Gharib's 221.\",\n derivation_fa=\"سغدی mwδ (خوانده muδ) «شراب» — در فرهنگ سغدی–فارسی–انگلیسیِ بدرالزمان قریب، مدخل شمارهٔ ۵۵۱۱ در صفحهٔ ۲۲۱: «mwδ2 S — muδ (mwd) ⟵ mδw — wine»، که به املای بودایی mδw (مدخل ۵۲۹۵، ص ۲۱۱: «maδu (mδw) … wine») و صورت مسیحیِ mdw (مدخل ۵۲۹۶) ارجاع می‌دهد؛ هزوارش ɣMRH نیز (مدخل ۴۰۵۹، ص ۱۶۲) همان ḤMR آرامی است که در پهلوی برای «می» به کار می‌رفت. این واژه بازماندهٔ مستقیمِ *madu- ایرانی آغازین است: واکهٔ پایانی به‌قاعده افتاده و ذالِ میان‌واکه‌ای برخلاف فارسی حفظ شده است. ویکی‌واژه نیز ذیل *médʰu صورت سغدیِ 𐼺𐼴𐼹 (mwδ) را می‌آورد. «mwd» در کتاب همان آوانگاری mwδ است با تایپِ ذال به‌صورت د، و تصویر صفحهٔ چاپی همین را نشان می‌دهد؛ پس خوانش اسکن درست است و تنها شمارهٔ صفحه یک واحد کمتر از ۲۲۱ قریب آمده.\",\n sources=[W+\"Reconstruction:Proto-Indo-European/m%C3%A9d%CA%B0u\"],\n ref_check=[dict(ref=\"SOD:220\", status=\"supports\", note=\"SOD_pages.txt, entry 5511 on the page whose printed number is 221: 'mwδ2 S | muδ (mwd) =»mδw | wine | GMS 408-, Anc. Lett. 4.6; Sund. AoFviii 1981 p216, 2aV2'. Cf. entry 5295 (p.211) 'mδw B, M, S | wine | maδu (mδw)'. The word and the transliteration are Nourai's; the page is 221 rather than 220.\")],\n consulted=[\n   dict(src=\"SOD\", where=\"Gharib nos. 4059, 5295, 5296, 5511\", stance=\"supports\", note=\"four entries for the word: the heterogram ɣMRH (p.162), Buddhist mδw (p.211), Christian mdw, and mwδ (p.221), all glossed 'wine'.\"),\n   dict(src=\"IEC\", where=\"Mann, s.v. medhu\", stance=\"silent\", note=\"Mann's descendant list runs 'Skt. mádhu; Av. maδu; Per. may; Oss. mid, mud; Tokh. B mit; Gk. méthu …' — Ossetic mud is there but no Sogdian form.\"),\n   dict(src=\"POK\", where=\"IEW 707\", stance=\"silent\", note=\"Pokorny's medʰu entry cites no Sogdian material.\"),\n ],\n))\n\nentry2_nodes.append(n(\n id=4, lang=\"Greek\", words=\"methu\",\n verdict=\"confirmed\",\n derivation=\"Greek μέθυ méthu n. 'wine', the direct reflex of *médʰu with the regular Greek treatment *dʰ > θ. It is a poetic/Homeric word: Buck (p.389) notes 'Grk. μέθυ occurs only as a poetical word for „wine“, but is the source of the common prose words μεθύω, μεθύσκω „be drunk, make drunk“'. The semantic shift 'honey/mead' > 'wine' happened because Greece drank wine, not mead; Walde-Pokorny II 261 puts it exactly so: 'gr. μέθυ „Wein“ (aus „Rauschtrank“; die Bed. „Honig“ hat sich auf μέλι zurückgezogen)'. Watkins: 'medhu-. Honey; also mead. … 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.]'\",\n derivation_fa=\"یونانی μέθυ (methu) «شراب»، بازماندهٔ مستقیمِ *médʰu با تبدیلِ قاعده‌مندِ *dʰ هندواروپایی به θ در یونانی. این واژه‌ای شاعرانه و هومری است؛ باک (ص ۳۸۹) می‌نویسد «μέθυ تنها به‌عنوان واژه‌ای شاعرانه برای „شراب“ به کار می‌رود، اما سرچشمهٔ فعل‌های رایجِ μεθύω و μεθύσκω „مست بودن، مست کردن“ است». تحول معنایی «عسل/شرابِ عسل» به «شراب» از آن‌رو رخ داد که یونانیان شراب انگور می‌نوشیدند نه شرابِ عسل؛ والده-پوکورنی (ج۲ ص۲۶۱) دقیقاً همین را می‌گوید: «μέθυ یونانی „شراب“ (از „نوشیدنیِ مستی‌آور“؛ معنیِ „عسل“ به μέλι واگذار شد)». واتکینز نیز ذیل medhu- می‌نویسد «یونانی methu، شراب … : AMETHYST، METHYLENE». ادعای نورایی درست است.\",\n sources=[W+\"Reconstruction:Proto-Indo-European/m%C3%A9d%CA%B0u\"],\n ref_check=[dict(ref=\"AHD:1524\", status=\"supports\", note=\"Nourai's AHD page numbers refer to the 1975/76 New College Edition appendix (pp.1505-1550); the local copy is Watkins' 1985 standalone edition of the same list, where the entry reads 'medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD¹. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.]' — the content is confirmed; the exact 1975 page could not be paged to (the New College scans are lending-only).\")],\n consulted=[\n   dict(src=\"POK\", where=\"IEW 707\", stance=\"supports\", note=\"'gr. μέθυ „wine“ (from the meaning „honey“ has been abbreviated in μέλι … „honey“); μεθύω „be intoxicated“, μεθύσκω „make intoxicated“'.\"),\n   dict(src=\"WLD\", where=\"Walde-Pokorny Bd. II 261\", stance=\"supports\", note=\"'gr. μέθυ „Wein“ (aus „Rauschtrank“; die Bed. „Honig“ hat sich auf μέλι zurückgezogen) : μεθύω „bin trunken“; μεθύσκω „mache trunken“'.\"),\n   dict(src=\"SYN\", where=\"Buck 5.91 MEAD p.389\", stance=\"supports\", note=\"'Grk. μέθυ occurs only as a poetical word for „wine“, but is the source of the common prose words μεθύω, μεθύσκω „be drunk, make drunk“, whence NG μεθυσμένος „drunk“.'\"),\n ],\n))\n\nentry2_nodes.append(n(\n id=5, lang=\"French\", words=\"\",\n verdict=\"confirmed\",\n derivation=\"A pass-through box for French méthylène, a chemical coinage of 1834 by Jean-Baptiste Dumas and Eugène Péligot, built from Greek méthu 'wine' + hū́lē 'wood' + the suffix -ène, because the substance (wood alcohol, methanol) had been got by the dry distillation of wood — literally 'wood-wine'. Etymonline: 'from French méthylène (1834), coined by Jean-Baptiste-André Dumas (1800-1884) and Eugène-Melchior Péligot (1811-1890) from Greek methy „wine“ … + hylē „wood“ … + Greek name-forming element -ene', 'so called because it was detected in wood alcohol'. This is a learned nineteenth-century formation, not an inherited descent, and the chart's arrow Greek > French is therefore a borrowing/coinage arrow — which is how Nourai draws Greek-to-modern-European links throughout.\",\n derivation_fa=\"جعبهٔ گذری برای واژهٔ فرانسویِ méthylène، اصطلاحی شیمیایی که در سال ۱۸۳۴ ژان-باتیست دوما و اوژن پلیگو ساختند از méthu یونانی «شراب» + hū́lē «چوب» + پسوند -ène، زیرا این ماده (الکل چوب = متانول) از تقطیر خشکِ چوب به دست آمده بود؛ یعنی تحت‌اللفظ «شرابِ چوب». Etymonline می‌نویسد: «از فرانسوی méthylène (۱۸۳۴)، ساختهٔ دوما و پلیگو از methy یونانی „شراب“ + hylē „چوب“ + پسوند -ene … چنین نامیده شد چون در الکلِ چوب یافت شده بود». پس این ساختی عالمانه از سدهٔ نوزدهم است نه میراثی زبانی، و پیکانِ «یونانی ← فرانسوی» در اینجا پیکانِ وام‌گیری/برساختن است — همان شیوه‌ای که نورایی در سراسر کتاب برای پیوندهای یونانی با زبان‌های اروپاییِ نو به کار می‌برد.\",\n sources=[\"https://www.etymonline.com/word/methylene\"],\n ref_check=[dict(ref=\"AHD:826\", status=\"not_checked\", note=\"AHD:826 is a page of the New College Edition dictionary body (not the IE appendix), i.e. the alphabetical entry 'methylene'; that edition is lending-only on archive.org and could not be paged to. The local Watkins 1985 index confirms the content: 'METHYLENE hūle-, medhu-'.\")],\n consulted=[\n   dict(src=\"AHD\", where=\"Watkins 1985, Index of English words\", stance=\"supports\", note=\"'METHYLENE hūle-, medhu-' — the compound is analysed as Greek hū́lē + méthu, exactly the French coinage.\"),\n   dict(src=\"FSD\", where=\"Funk & Wagnalls, searched all four volumes\", stance=\"silent\", note=\"grep -i 'methylene' in FSD_vol1-4.txt returns only compound entries (cyclohexane, 'methylene blue', 'methylene groups', a coal-tar table) — the headword page with its etymology is not in this OCR.\"),\n ],\n))\n\nentry2_nodes.append(n(\n id=6, lang=\"English\", words=\"methylene\",\n verdict=\"confirmed\",\n derivation=\"English methylene (1835) is the French word méthylène taken over unchanged apart from the ending; from it English chemistry back-formed methyl (méthylène analysed as méthyl + -ène), and then, by identifying the last syllable with the general suffix -yl, the free combining element meth- (whence methane, methanol, methadone, methamphetamine …). Etymonline: 'The breakdown of methylene into methyl and -ene, and the identification of the last syllable of methyl with the general suffix -yl, led to the use of meth- as a separate combining-element.' So the whole meth- family of modern chemistry ultimately carries Greek méthu 'wine' — and behind it PIE *médʰu 'honey, mead' — which is the point of Nourai's chart.\",\n derivation_fa=\"واژهٔ انگلیسی methylene (۱۸۳۵) همان méthylène فرانسوی است که جز در پایانه دگرگون نشده. از آن، شیمیِ انگلیسی با تجزیهٔ méthylène به méthyl + -ène واژهٔ methyl را بازساخت، و سپس با یکی‌گرفتنِ هجای پایانیِ methyl با پسوندِ عمومیِ -yl، جزءِ ترکیبیِ آزادِ meth- پدید آمد (که در methane، methanol، methadone، methamphetamine و … به کار می‌رود). Etymonline: «تجزیهٔ methylene به methyl و -ene، و یکی‌انگاشتنِ هجای آخرِ methyl با پسوند عمومیِ -yl، به کاربردِ meth- همچون جزءِ ترکیبیِ جداگانه انجامید». پس سراسرِ خانوادهٔ meth- در شیمیِ امروز در نهایت méthu یونانی «شراب» و پشتِ آن *médʰu هندواروپایی «عسل، شرابِ عسل» را با خود دارد — و همین نکتهٔ نمودارِ نورایی است.\",\n sources=[\"https://www.etymonline.com/word/methylene\"],\n ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"no reference on the box; the parent's AHD:826 and Watkins' index line 'METHYLENE hūle-, medhu-' cover it.\")],\n consulted=[\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. medhu- and Index\", stance=\"supports\", note=\"'2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE' / 'METHYLENE hūle-, medhu-'.\"),\n   dict(src=\"WEB\", where=\"Webster's New Twentieth Century Dictionary vol. 1\", stance=\"silent\", note=\"grep 'methylene' in WEB_vol1.txt returns only the hexamethylenetetramine entry ('methylene, and tetramine … a crystalline compound, C6H12N4'); vol. 1 stops before the M headwords proper, so no etymology could be read there.\"),\n ],\n))\n\ndef clean(node):\n    d = {k:v for k,v in node.items() if v is not None or k in ('lang',)}\n    d.pop('derivation_note', None)\n    return d\n\nout = dict(\n  pdf_page=324,\n  book_page=294,\n  verified_by=\"claude-opus-5\",\n  verified_on=\"2026-09-07\",\n  entries=[\n    dict(\n      entry=0,\n      root=\"Me 2, Měnôt\",\n      verdict=\"confirmed\",\n      modern_form=\"PIE *meh₁- 'to measure' (Pokorny mē-3, IEW 703-704), with the derived *mēnōt-/*mēns- 'month, moon' (Pokorny mēnōt, IEW 731-732)\",\n      note=\"Root box, language label, gloss and both page numbers are right, and they come straight out of Watkins: the AHD appendix entry reads 'mē-2. To measure. Contracted from *meə-. … II. Extended and suffixed forms *mēn-, *mēn-en-, *mēn-s-, *mēn-ōt-, moon, month (an ancient and universal unit of time measured by the moon) … [Pok. 3. mē- 703, mēnōt- 731.]' — that is exactly Nourai's 'Me 2: to measure; Měnôt: moon used to measure time (POK:703, 731)', including the gloss 'used to measure time'. Pokorny's own note under mēnōt says 'probably as personified „time measurement“ to mē- „measure“'. Cross-cutting remarks on this chart: (1) the Latin/French/English/Persian half (medērī, modus, modèle/moderne/commode > مدل، مدرن، کمد) is solid throughout, and so is the Germanic must/empty pair, which is Watkins' §6 copied verbatim; (2) the Iranian half is the weak side — the Pahlavi vīmār box cannot be got from Avestan vī-mad-, and Horn p.59, the very page Nourai cites for بیمار, says so in as many words; (3) the azdā box reproduces Pokorny's own hesitant attachment of the word to this root, but glosses an adverb 'known, certain' as a noun 'indicator, hint, news'; (4) 'turmoil' in the English modus box is not in Watkins and rests on the contested trémie < trimodia etymology; (5) the printed page has an arrow from azdā into a completely blank box (node 6) — that is the book's own blank, faithfully extracted. No extraction errors found on this page: every word, script string, reference and the ʿOnṣorī quotation in the JSON matches the printed page.\",\n      note_fa=\"جعبهٔ ریشه، برچسبِ زبان، معنی و هر دو شمارهٔ صفحه درست است و مستقیماً از واتکینز گرفته شده: در پیوستِ فرهنگ American Heritage آمده «mē-2. اندازه گرفتن … صورت‌های گسترده و پسونددارِ *mēn-، *mēn-en-، *mēn-s-، *mēn-ōt-، ماه (کهن‌ترین و جهانی‌ترین یکای زمان که با ماه سنجیده می‌شد) … [پوکورنی mē- ۷۰۳، mēnōt- ۷۳۱]» — یعنی دقیقاً همان «Me 2: اندازه گرفتن؛ Měnôt: ماه که برای سنجش زمان به کار می‌رفت (POK:703, 731)» که نورایی نوشته. خودِ پوکورنی هم ذیل mēnōt می‌نویسد که این واژه احتمالاً «سنجشِ زمانِ شخصیت‌یافته» و برگرفته از mē- «اندازه گرفتن» است. نکته‌های کلی دربارهٔ این نمودار: (۱) نیمهٔ لاتینی–فرانسوی–انگلیسی–فارسی (medērī، modus، modèle/moderne/commode ← مدل، مدرن، کمد) سراسر استوار است و جفتِ must/empty نیز رونوشتِ بندِ ششمِ واتکینز است؛ (۲) نیمهٔ ایرانی نقطهٔ ضعف است — «وِمارِ» پهلوی را نمی‌توان از vī-mad- اوستایی گرفت و هرن در همان صفحهٔ ۵۹ که نورایی برای «بیمار» به آن ارجاع می‌دهد، صریحاً همین را می‌گوید؛ (۳) جعبهٔ azdā همان پیوندِ مردّدِ پوکورنی را بازتاب می‌دهد، ولی قیدی به معنای «آشکار، بی‌گمان» را همچون اسمی به معنای «نشانه، خبر» معنی کرده است؛ (۴) واژهٔ turmoil در جعبهٔ انگلیسیِ modus در واتکینز نیست و بر ریشه‌شناسیِ مورد اختلافِ trémie < trimodia تکیه دارد؛ (۵) در صفحهٔ چاپی پیکانی از azdā به جعبه‌ای یکسره سفید می‌رود (گرهٔ ۶) که سفیدیِ خودِ کتاب است و درست هم استخراج شده. هیچ خطای خوانشِ اسکنی در این صفحه یافت نشد.\",\n      sources=[W+\"Reconstruction:Proto-Indo-European/med-\"],\n      ref_check=[\n        dict(ref=\"POK:703\", status=\"supports\", note=\"POK_full.txt: 'Root / lemma: mē-3, m-e-t- / Meaning: to measure / … References: WP. II 237 f., WH. II 70 f., 81 f., Trautmann 179, 183; related with 1. med-. / Page(s): 703-704' — with Av./OP mā- 'measure', Gk. μέτρον, Lat. metior/mēnsa, Lith. metas 'year, time, measure'.\"),\n        dict(ref=\"POK:731\", status=\"supports\", note=\"POK_full.txt: 'Root / lemma: mēnōt. Gen. mēneses, from which mēnes-, mēns- mēs-, mēn- / Meaning: month; crescent / Note: probably as personified „time measurement“ to mē- „measure“. / Material: Old Indie mās, māsa- m., Avestan mā̊, Gen. mā̊ŋhō, npers. māh „moon, month“ … Page(s): 731-732'.\"),\n      ],\n      consulted=[\n        dict(src=\"AHD\", where=\"Watkins 1985 s.v. mē-2\", stance=\"supports\", note=\"'mē-2. To measure. Contracted from *meə-. I. Basic form mē-. … II. Extended and suffixed forms *mēn-, *mēn-en-, *mēn-s-, *mēn-ōt-, moon, month (an ancient and universal unit of time measured by the moon). … [Pok. 3. mē- 703, mēnōt- 731.]' — Nourai's root box, gloss and both page numbers, verbatim.\"),\n        dict(src=\"IEC\", where=\"Mann, s.v. mēns, mēnes-\", stance=\"supports\", note=\"'mēns, mēnes- „moon, month“. Cf. mēna, mēno, (mān-, mōn-). Variant: mēs. Skt. cf. mās, m.; Av. mā̊, mā̊ŋh-, m. „moon“; OPer. Per. māh … Gk. mēn, gen. sg. mēnós, m. „month“'.\"),\n        dict(src=\"POK\", where=\"IEW 703-704 and 731-732\", stance=\"supports\", note=\"both lemmata read and quoted in ref_check; Pokorny himself links mēd-1 back to mē-3 ('See also: mēd- is related to mē-3 (above S. 703 f.)').\"),\n      ],\n      nodes=[clean(x) for x in entry0_nodes],\n    ),\n    dict(\n      entry=2,\n      root=\"Medhu\",\n      verdict=\"confirmed\",\n      modern_form=\"PIE *médʰu n. 'honey; mead, honeyed intoxicating drink'\",\n      note=\"The root, the language label and the page number are right; the gloss is only half the story. Pokorny's lemma is 'medʰu / Meaning: honey, intoxicating drink, mead / Grammatical information: n. / Note: actually nominalized adjective „sweet“ … Page(s): 707'; Watkins heads it 'medhu-. Honey; also mead'; Walde-Pokorny II 261 '*medʰu n. „Honig; bes. Met“'. Nourai's bare 'honey' is defensible for the proto-meaning but it hides the fact that every single descendant on this chart — Av. maδu-, NP may, Sogd. mwδ, Gk. méthu — means 'wine' or 'fermented drink', not 'honey', because the drink-sense is what the Iranian and Greek branches kept. Buck's article on MEAD (5.91, printed p.389, one of Nourai's own references on the Persian box) sets this out and even supplies the missing link '(NPers. mai „wine“, Horn 1003)'. The chart is sound except for two items: Av. maδa- 'wine' in the Avestan box, which belongs to PIE *mad- 'be wet, be drunk' and not here (it merged with maδu- only later, in Persian), and Persian مُل mol, for which both Horn (no. 990) and Moʿin derive Skt. mṛdvīkā- 'grape-wine' — the alternative Nourai himself flags in his NOTE. The extraction of this entry is faithful to the printed page, including the ʿOnṣorī verse and the NOTE.\",\n      note_fa=\"ریشه، برچسبِ زبان و شمارهٔ صفحه درست است؛ اما معنی تنها نیمی از ماجراست. پوکورنی مدخل را چنین می‌آورد: «medʰu / معنی: عسل، نوشیدنیِ مستی‌آور، شرابِ عسل / خنثی / یادداشت: در اصل صفتِ اسم‌شدهٔ „شیرین“ … صفحهٔ ۷۰۷»؛ واتکینز عنوان می‌زند «medhu-. عسل؛ و نیز شرابِ عسل»؛ والده-پوکورنی هم «*medʰu خنثی „عسل، به‌ویژه شرابِ عسل“». معنیِ تنهای «honey» که نورایی نوشته برای معنیِ نیانی پذیرفتنی است، اما پنهان می‌کند که همهٔ بازماندگانِ همین نمودار — maδu- اوستایی، «می» فارسی، mwδ سغدی و méthu یونانی — به معنای «شراب» یا «نوشیدنیِ تخمیری‌اند» نه «عسل»؛ چراکه شاخه‌های ایرانی و یونانی معنیِ «نوشیدنی» را نگه داشتند. باک در بخش ۵٫۹۱ (صفحهٔ ۳۸۹، که خودِ نورایی در جعبهٔ فارسی به آن ارجاع داده) همین را شرح می‌دهد و حتی حلقهٔ گم‌شده را می‌آورد: «فارسی نو mai „شراب“، هرن ۱۰۰۳». نمودار جز در دو مورد درست است: maδa- اوستایی «شراب» در جعبهٔ اوستایی که در اصل به ریشهٔ *mad- «تر بودن، مست شدن» تعلق دارد و تنها بعدها در فارسی با maδu- درآمیخت؛ و «مُل» فارسی که هم هرن (شمارهٔ ۹۹۰) و هم معین آن را از mṛdvīkā- سنسکریت «شراب انگوری» می‌گیرند — همان گزینه‌ای که خودِ نورایی در یادداشتش به آن اشاره کرده است. استخراجِ این مدخل، از جمله بیتِ عنصری و یادداشت، با صفحهٔ چاپی مطابق است.\",\n      sources=[W+\"Reconstruction:Proto-Indo-European/m%C3%A9d%CA%B0u\"],\n      ref_check=[dict(ref=\"POK:707\", status=\"supports\", note=\"POK_full.txt: 'Root / lemma: medʰu / Meaning: honey, intoxicating drink, mead / Grammatical information: n. / Note: actually nominalized adjective „sweet“ / Material: Old Indie madhu- n. „honey, mead“ … Avestan madu- n. „berry wine“; gr. μέθυ „wine“ … Old Icelandic mjǫðr, Old English meodo, Old High German metu „mead“ … References: WP. II 261 … Page(s): 707'.\")],\n      consulted=[\n        dict(src=\"WLD\", where=\"Walde-Pokorny Bd. II 261\", stance=\"supports\", note=\"'*medʰu n. „Honig; bes. Met“ im Germ. u. Bsl. masc. geworden. Ai. mádhu „Honig, Met“ (davon mádhu- „süß“; madh(u)v-ád- „Honigesser“; aksl. medv-ědь „Bär“); av. maδu „Beerenwein“; tochar. B mit „Honig“; gr. μέθυ „Wein“ …'\"),\n        dict(src=\"AHD\", where=\"Watkins 1985 s.v. medhu- and the essay on Indo-European food\", stance=\"supports\", note=\"'medhu-. Honey; also mead. … [Pok. médhu 707.]'; and in the introductory essay: 'notably was the base of the only certain Indo-European alcoholic beverage, MEAD, medhu-, meaning in different dialects both „mead“ („wine“ in Greece) and „honey“.'\"),\n        dict(src=\"IEC\", where=\"Mann, s.v. medhu\", stance=\"supports\", note=\"'medhu „sweet drink, liquid honey, mead“. Cf. midhu & melit. WP II, 261 Skt. mádhu; Av. maδu „honey, mead“; Per. may „wine“; Oss. mid, mud „honey“; Tokh. B mit; Gk. méthu „wine“ beside méthē „drunkenness“ …'\"),\n        dict(src=\"SYN\", where=\"Buck 5.91 MEAD, printed p.389\", stance=\"supports\", note=\"'1. IE *medhu- „honey“ and „mead“. Walde-P. 2.261. … Skt. madhu- was used for any sweet intoxicating drink, especially the soma juice. Av. maδu- was a kind of wine or beer (Barth. 1114 … NPers. mai „wine“, Horn 1003).'\"),\n      ],\n      nodes=[clean(x) for x in entry2_nodes],\n    ),\n  ],\n)\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-324.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-324.json > /dev/null && echo JSON-OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 324"
}
```


### [2026-09-07T16:12:01.643Z] TOOL RESULT

```
written
JSON-OK
nodes verified: 20/20
node verdicts: {'confirmed': 13, 'disputed': 2, 'plausible': 4, 'unverified': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'not_checked': 9, 'contradicts': 1, 'partial': 4}
books consulted: {'supports': 36, 'partial': 12, 'contradicts': 2, 'silent': 7} | by book: {'AHD': 9, 'POK': 7, 'IEC': 6, 'WLD': 5, 'KLN': 4, 'BRT': 3, 'PHD': 3, 'LAT': 3, 'SYN': 3, 'NYB': 2, 'HRN': 2, 'BQT': 2, 'SKT': 2, 'KNT': 1, '(printed page)': 1, 'MON': 1, 'SOD': 1, 'FSD': 1, 'WEB': 1}
```


## [2026-09-07T16:12:11.543Z] TOOL CALL #77: Bash

```json
{
 "command": "python3 tools/verify_check.py 324 2>&1 | grep -i \"problem\\|warn\" ; echo \"exit=$?\"; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg324.png data/verification/sources/refs/ocr/BOOK/324.png && ls -la data/verification/sources/refs/ocr/BOOK/324.png"
}
```


### [2026-09-07T16:12:12.918Z] TOOL RESULT

```
exit=1
-rw-rw-r-- 1 sfmqrb sfmqrb 65279 Sep  7 12:12 data/verification/sources/refs/ocr/BOOK/324.png
```


## [2026-09-07T16:12:31.216Z] AGENT

Page 324 verified. `data/verification/page-324.json` written; `verify_check.py 324` reports 20/20 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed (entry 1 is the `Med -> Me 2` redirect, skipped). Nodes: 13 confirmed, 4 plausible, 2 disputed, 1 unverified. Ref checks: 10 supports, 4 partial, 1 contradicts, 9 not_checked (boxes with no `refs=`). 19 books consulted.

**Disputed**
- Me 2 → Pahlavi `vîmâr` (#3): the word is real (MacKenzie *wēmār*, Nyberg *vīmār*), but Av. `vī-mad-` 'physician' → 'patient' needs a reversed meaning and δ > r. Horn p.59 — the page Nourai cites for the next node — says "Die Etymologie ist gewiss falsch"; modern proposals are *wi-mār-* (mar- 'die') or Wiktionary's *wemh₁- 'vomit'.
- Medhu → Persian `mol` «مُل» (#2): Horn no. 990 (p.222) and Moʿin's footnote at BQT p.2030 both derive it from Skt. *mṛdvīkā-* 'grape-wine', not *medʰu — the "Mer 2" alternative Nourai flags in his own NOTE. `may` «می» in the same box is fully confirmed.

**Plausible** — `azdâ` (Pokorny attaches it only with a question mark, and it is an adverb 'known, certain', not "indicator, hint, news"); Av. `madha` (= maδa-, which belongs to PIE *mad-, merging with maδu- only in Persian); English `turmoil` (absent from Watkins; rests on the contested trémie < *trimodia* etymology); the Germanic `must/empty` box (Watkins hedges "Possibly", Mann files it under a separate root mod-).

**Unverified** — node #6: the printed page really has an arrow from `azdā` into a blank, unlabelled box. Book's own blank, faithfully extracted.

**Extraction errors: none.** Every word, script string, reference and the ʿOnṣorī verse matches the printed page (page PNG saved to `data/verification/sources/refs/ocr/BOOK/324.png`).

Notable ref findings: the root box `Me 2 / Měnôt … POK:703, 731` is Watkins' `mē-2` entry verbatim, page numbers included. `SYN:307` and `SYN:389` are exact (Buck 4.87 PHYSICIAN lists "Av. vimad-"; 5.91 MEAD supplies "(NPers. mai 'wine', Horn 1003)"). `BQT:2071` is exactly the می page with Moʿin's etymological footnote; مل is at p.2030, not 2071. `SOD:220` should be 221 (Gharib no. 5511 `mwδ` 'wine'), and Nourai's "mwd" is the standard mwδ with δ typed as d. Six web pages archived via `fetch_source.py`.
