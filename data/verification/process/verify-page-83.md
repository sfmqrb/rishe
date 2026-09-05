# Verification process log — verify-page-83


## [2026-09-05T06:19:31.299Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 83 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-83.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-83.json. Write /home/sfmqrb/git/rishe/data/verification/page-83.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 83` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T06:19:32.617Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T06:19:33.433Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T06:19:33.449Z] TOOL RESULT

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


## [2026-09-05T06:19:33.989Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-83.txt"
}
```


### [2026-09-05T06:19:34.015Z] TOOL RESULT

```
1	=== PDF page 83 (book page 53) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhe, Bheğh : outside, open (Bhe, Bheğh); outside, excluding, except (Bheğh-iks)  (refs IEC:69,70; POK:112)
4	#1 (parent #0) [Pahlavi] refs=MON:452 | a-pâč : open
5	  #2 (parent #1) [Persian] refs=IEC:70 | bâz «باز ٣» : open
6	#3 (parent #0) [Persian] refs=IEC:70; MON:473 | bejoz «بجز» : except, excluding
7	#4 (parent #0) [Sanskrit] refs=IEC:70 | bôhyah : outside, open ; bahis : except, excluding
8	#5 (parent #0) [Indo-European] refs=IEC:70; POK:115 | Bheg : to oust out, push out, strike, break
9	  #6 (parent #5) [Germanic] refs=AHD:1508 | bankon : river banks
10	    #7 (parent #6) [English] refs=AHD | bank, bankrupt, banquet ; bench : originally used by bankers to exchange money
11	--- entry 1 ---
12	ROOT [Indo-European] Bhě, Bho, Bha, Bhâ : indeed  (refs POK:113; IEC:59; WLD2:136)
13	#1 (parent #0) [Avestan] refs=POK:113; IEC:59 | bâ, bě, beî : indeed
14	#2 (parent #0) [Sanskrit] refs=IEC:59 | bha-la : yes
15	#3 (parent #0) [Armenian] refs=IEC:59 | ba : yes
16	  #4 (parent #1) [Persian] refs=IEC:59; MON:424,577 | bî-, be- «بِ- ، بی-» : emphatic prefixes ; baleh, balî «بله ، بلی» : yes | extra: برفت ، بیامد | NOTE: MON derives "baleh & balî" from Arabic while IEC claims they are Indo-European
17	--- entry 2 ---
18	ROOT Bheg -> redirect to Bhe
19	--- entry 3 ---
20	ROOT Bheğh -> redirect to Bhe
21	--- entry 4 ---
22	ROOT Bheğh-iks -> redirect to Bhe
23	
```


## [2026-09-05T06:19:36.774Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-83.json",
 "description": "Read source JSON for page 83"
}
```


### [2026-09-05T06:19:36.861Z] TOOL RESULT

```
{
  "pdf_page": 83,
  "book_page": 53,
  "entries": [
    {
      "root": {
        "name": "Bhe, Bheğh",
        "lang": "Indo-European",
        "refs": "IEC:69,70; POK:112",
        "gloss": "outside, open (Bhe, Bheğh); outside, excluding, except (Bheğh-iks)"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:452",
          "words": [
            {"translit": "a-pâč", "gloss": "open", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "IEC:70",
          "words": [
            {"translit": "bâz", "gloss": "open", "script": "باز ٣"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:70; MON:473",
          "words": [
            {"translit": "bejoz", "gloss": "except, excluding", "script": "بجز"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:70",
          "words": [
            {"translit": "bôhyah", "gloss": "outside, open", "script": null},
            {"translit": "bahis", "gloss": "except, excluding", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "IEC:70; POK:115",
          "words": [
            {"translit": "Bheg", "gloss": "to oust out, push out, strike, break", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Germanic",
          "refs": "AHD:1508",
          "words": [
            {"translit": "bankon", "gloss": "river banks", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "bank, bankrupt, banquet", "gloss": null, "script": null},
            {"translit": "bench", "gloss": "originally used by bankers to exchange money", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bhě, Bho, Bha, Bhâ",
        "lang": "Indo-European",
        "refs": "POK:113; IEC:59; WLD2:136",
        "gloss": "indeed"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:113; IEC:59",
          "words": [
            {"translit": "bâ, bě, beî", "gloss": "indeed", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:59",
          "words": [
            {"translit": "bha-la", "gloss": "yes", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Armenian",
          "refs": "IEC:59",
          "words": [
            {"translit": "ba", "gloss": "yes", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Persian",
          "refs": "IEC:59; MON:424,577",
          "words": [
            {"translit": "bî-, be-", "gloss": "emphatic prefixes", "script": "بِ- ، بی-"},
            {"translit": "baleh, balî", "gloss": "yes", "script": "بله ، بلی"}
          ],
          "script_extra": "برفت ، بیامد",
          "note": "MON derives \"baleh & balî\" from Arabic while IEC claims they are Indo-European",
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Bheg", "redirect": "Bhe"},
      "nodes": []
    },
    {
      "root": {"name": "Bheğh", "redirect": "Bhe"},
      "nodes": []
    },
    {
      "root": {"name": "Bheğh-iks", "redirect": "Bhe"},
      "nodes": []
    }
  ]
}
```


## [2026-09-05T06:19:38.505Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['IEC','POK','WLD','AHD','MON','KLN','HRN','HUB','PHD','NYB','BRT','SYN','ARY','BQT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-05T06:19:40.305Z] TOOL RESULT

```
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
```


## [2026-09-05T06:20:40.128Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; sed -n '1,120p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-05T06:20:40.182Z] TOOL RESULT

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
---
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
```


## [2026-09-05T06:20:42.189Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; awk 'BEGIN{RS=\"\\f\"} {n=NR-1; if (index($0,\"bheǵh\")>0 || $0 ~ /bahis/) print \"leaf\",n\": \", substr($0,1,200)}' $f | head -20; done"
}
```


### [2026-09-05T06:20:43.896Z] TOOL RESULT

```
== POK_01.txt
== POK_02.txt
== POK_03.txt
```


## [2026-09-05T06:20:48.628Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 120 121 122 123 124; do echo \"=== awk leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N{print substr($0,1,1500)}' POK_01.txt; done"
}
```


### [2026-09-05T06:20:50.302Z] TOOL RESULT

```
=== awk leaf 120 ===
�dd,  usw.
110
bhrozdh-
Alb.  breth,  bredhi  ^Tanne^;  air.  brot  ^Stachel^^  acorn.  bros,  bret.  broud vgl.    mir.    brostaim    ^stachle    an^    aus    *bhros-t-    (Loth    RC.  42,   70),    irrig] O'Rahilly  Eriu  13,  169  f.;  ahd.  h-art  ,Rand,  Kante,  Vordersteven,  schwe^ dial.  bradd.
bbrezdh-,  bhroZdh-
Mir.  brataim  ,plündere,  raube^  (dazu  bratdii  ,Lachs^)  =  cymr.  brath^^ ,stechen,  beißen,  durchbohren^;  Hhvozdh-  oder  Hhfzdh-  zu  germ.  *bruzi, in  ahd.  brort  ,Rand,  Kante^,  ags.  brord  m.  ,Spitze,  Keim,  Blatt^,  wsächs. brerd  (*brozdi-),  ags.  bryrdan  ,anstacheln,  reizen^,  aisl.  broddr  ,Spitze,  Ge- treidekeim, Schneide^,  ahd.  gibrortön  ,einfassen^;  =  baltoslav.  *bruzdä-  i^ aksl.  h'^zda,  russ.  brozde  ,Zaum^,  lit.  bruzdüklis,  alt  ,Zaum^,  heute  ,Pflockj KnebeP.  Hingegen  ist  h't.  brizgilas,  apr.  bisgelan  ,Zaum^  wohl  aus  urgerm. briidila-  (ags.  brigdds  ,Zaum^,  bregdan  ,flechten^)  entlehnt.  Anders  Speclit  '. Dekl.  142.
WP.  II  131  ff.,  WH.  I  461  f.,  546.
bhardhä  ,Bart^
Lat.  barba  ,Bart^  (assimil.  aus  *farba) ;  '
ahd.  bartj  ags.  beard  ,Bart^  m.,  davon  ahd.  barta^  as.  barda,  aisl.  baräa  : ,Beil,  Barte^,  weil  das  Eisen  wie  ein  Bart  am  Stiele  steht;  aus  dem  Germ. ! aksl.  brady  ,Axt,  BeiP;
aksl.  brada  ,Bart^,  russ.  borodd  ds.,  auch  ,Kinn^,  skr.  brdda^  Akk.  brädu ,Bart^  usw.;
apr.  bordus  ,Bart^  (unklar  nach  Trautmann  27);
lett.  
=== awk leaf 121 ===
^1  ^^^^  gallo-rom.  *har{i)ca  ^Holzhaus^  (vgl.  Bollelli  L'It.  dial.
17,  i47°f.);
toch   A  präkär,  B  präkre  ,fest^  (Van  Windekens  Lexique  100).
\VP.  II  134 f-;  ^VH.  I  456  f.,  Loth  RC.  38,  303 f.    Zweifel  bei  EM  332.
bbares-  ,Gerste^
Lat.  fctr  (eig.  farr),  farris  n.  ,Dinkel,  Spelt;  Schrot,  MehP  aus  *far(o)s, *far(e)zes  (bzw.  *fars,  *fars-es)  =  osk.  far^  umbr.  far]  lat.  farina  ,MehF Caus  *farrlna)^  farreus  ==  umbr.  farsio,  fasiu  ,farrea^;  got.  hariz-eins C=3  lat. /arma)  ;aus  Gerste^,  aisl.  harr  m.  ,Korn,  Gerste^,  ags.  here  ,Gerste^ (*b(ir(a)z-,  bzw.  *ha7'(i)z-)]  aber  slav.  *barsina-  in  aksl.  brahno  ,Nahrung^, skr.  bräsno  ,Mehl^,  russ.  börosno  ,Roggenmehl^,  nach  Jokl  Miletic-Festschr. (1933)  119  ff.  vielmehr  zu  1.  bher-  ,tragen^    Vgl.  auch  hhares-  S.  109.
WP.  I  134,  WH.  I  455  f.,  864.
bbasko-,  etwa  ,Bund,  Bündelt
Maked.  ßdayuoL '  ös(Tf4,ol  cpovydvcov  und  ßaa-/,svTai '  (paGylösg  (dies  die  echt oT.  Lautform),  äy/AXai  Hes.;  vielleicht  hierher  gr.  qxxa/.coXog  ,Ledersack^;
lat.  fascia  ,Binde,  Band,  Landstreifen^,  fascis  ,Bund,  Bündel,  Paket; das  Rutenbündel  mit  hervorragendem  Beil  als  Zeichen  der  Herrscher- gowal t^;
mir.  basc  , Halsband^,  abrit.  bascauda  ,eherner  Spülkessel^  (vielleicht  ur- .sprüngl.  ein  irdenes  über  einem  geflochtenen  korbartigen  Gerippe  ge- formtes und  gebranntes  Gefäß),  cymr.  baich
=== awk leaf 122 ===
eln,   schauke! usw.;   vielleicht   älter    däa.  had   ^Kampf;  Schade^,   mnd.  hat  ^Schade, glück*^;,  iihd.  Blutbad.
Unklar  ist  das  Verhältnis  zu  *hliäut-  (s.  unten);  ist  statt  Hhät-  etj *bhuät-  anzusetzen,  oder  liegt  eine  Wz.  *bhä-  mit  verschiedenen  Forma tien  zugrunde,  die  vielleicht  in  lat.  fämex,  -icis  ,Blutunterlauf'  (*durj| Schlag  entstandene  Blutgeschwulst)  vorliegt?
WP.  II  126  f.,  WH.  I  46,  99,  452,  464.
1.  bhMu'  :  bha-  ,schlagen,  stoßend
a)  Mit  Präsens  bildendem  -d-: Lat.  füstis   (*b]iüd-sti-s)   , Stock,   Knüttel  (=  gall.  büstis  in  aprov.  bi
,Baumstrunk'^  usw.),  füsterna  ,Knorrenstück^;
air.  bibdu  ,schuldig,  Feind^  (*bhe-hhud-uöts),  mir.  büalaim  ,schla^e^  au? *bhäud-l- .  .  .  (oder  *boug-l- ...  zu  nhd.  pochen  oben  S.  98) ;  wohl  auca ! air.  bodar  ,taub,  betäubt,  verwirrt^,  cymr.  hyddar  ,taub^  (*hudaro-)-
aisl.    bauta   (-ada)   ,schlagen,    stoßen^,   ags.  beatan   (beot),   ahd.   boz(z)an. (biez  oder  schw.  Verb)    ds.,   mhd.  boz,    böz,    büz  m.  ,Schlag^,   nhd.  Ämboß^- ags.  bytel   ,Hammer^,    mnd.   botet   ds.,    mhd.    boezel   , Schlägel^,    aisl.  beytilt ,Zeugungsglied  des  Pferdes'^;  aisl.  biitr  ,kurzes  Stück  eines  Baumstamms mit  expressivem  tt:  ndd.  butt  ,stumpf,  plump^  (dazu  der  Fischname  Butte] mhd.    butze   ,abgeschnittenes    Stück,    Klumpen^,  ags.   buttuc   ,Ende,  Stüct Land'^,   nor
=== awk leaf 123 ===
^noch'^  (^*außerdem^);  bet  ^sondern^,  aber^  (Bildung  wie  ne-t  ^son- dern')? ^^^'  ^^^^'  ^^^^;^^^^^6icht^  etwa^  (Hhe  +  est,  Endzelin  Stud.  halt.  7^  32  f.). Ob  hierher  air.  bes  ^vielleicht^^  vorton.  aus  *beis  <  *bhe-esti? WP.  n  137,  Trautmann  28,  Endzelin  Lett.  Gr.  497  f.
bbCf  ^^^  Partikel  bes.  der  Beteuerung  und  Hervorhebung.
Ar.  bä,  bat,  be,  böit  (letzteres,  wie  lit.  bei,  wohl  mit  Verstärkungsparti- jjel  *id)  Partikeln  der  Beteuerung  und  Hervorhebung,  bäda  ,fürwahr^  (,ob au  ai.  badham?^  Bartholomae  Wb.  953);
arm.  ba,  bay  hervorhebende  Partikel;
o-ot.  ba  Konditionalpartikel  (hierher  i-ba,  ibai  ,ob  denn?^  Konj.  ,daß nicht^,  ni-ba,  ni-bai  ,doch  nicht  etwa?^,  Konj.  ,wenn  nicht^,  ja-6az  ,wenn^, fthd.  ibii,  oba,  mhd.  ob{e)  ,wenn,  oV  usw.,  s.  Kluge  ^^  422);
lit.  bä  ,ja,  freilich^,  ben  ,wenigstens,  auch  nur^,  ostlit.  be  {==  apr.  bhe), hei  (s.  oben)  ,und^,  be,  bä,  bes,  bau  Fragepartikel,  apr.  beggi  ,denn^;
aksl.  (usw.)  bo  ,denn^,  i-bo  ,xat  yccg^,  u-bo  ,also^,  ne-bo-m  ,etenim^;  ab- lautend klr.  ba  ,ja,  freilich^,  cech.  poln.  ba  ,traun,  fürwahr^
WP.  n  136,  Trautmann  22  f.
bh^-  :  hhö'  ,wärmen,  rostend
Ahd.  baen,  bäjan,  nhd.  bälien  (*bheiö)  ,dureh  Umschläge  wärmen,  Brot rosten^,  dazu  mit  idg.  -<o-Suffix  aisl.  bad  ,Dampfbad'^,  as.  bath,  ags.  boep, ahd.  bad  ,Bad^;  dazu  auch  norw.  dial.  bara  ,mit
=== awk leaf 124 ===
  bodg,  bostl  (s-Aor.  bas^)  ,stechen',  bodr  m,  ,spina'  (*bod-lh)]  ^
toch.  A  pat-,  pät'  ,pfiügen';
vielleicht  auch  hitt.  pid-da-i  (kann  auch  pdd-da-i  gelesen  werden) ,macht  ein  Loch  in  die  Erde',  vgl.  Pedersen  Hitt.  77.
Vielleicht  hierher  gr.  ßö^Qog,  ßö&Vvog  m.  ,Grube'  ,Schwyzer  Gr.  Gr.  I  262, Zus.  2.  Anders  Petersson  Heterokl.  128  ff.
Wahrscheinlich  dazu   kelto-germ.  boduo-,  -ä  ,Kampf'  in  gall.  PN  Ate-bo- duus,    -uäj    Boduo-gnätus,    air.  bodb   f.  ,Krähe,    Schlachtgöttin    in    Gestalt einer  Krähe';  aisl.  bod  f.  (*badwö),  Gen.  bodvar,  ags.  beadu  f.,  as.  Badu^^ ahd.  Batu-  (in  PN)  ,Kampf'.
WP.  I  126  ff.,  188,  WP.  I  99,  521  f.,  866,  Trautmann  29.
2.  bbedh'  ,krümmen,  beugen,  drücken,  plagen'.
Ai.  bddhate   ,drängt,   drückt,  plagt',    Desid.  bibhatsate  ,scheut   sich   vor''|^ etwas,  empfindet  Ekel',  jün-bädh-  ,Knie  beugend';
alb.  bintj  med.  bindern  ,beuge  mich',  baskkr  ,zusammen',  bashkonj  ,ver-'i,J einige,  coeo';
got.  bida  ,Gebet',  ahd.  beta  f.  ,Bitte',  got.  bidjan  (sek.  -bidan)  ,bitten, beten',  aisl.  bidja,  ags.  biddan,  ahd.  bitten,  aisl.  kne-bedr  m.  , Kniepolster', ags.  cneow-gebed  n.  ,Gebet'  (vgl.  a,i.  jfiU'bädh-)]
lit.   bodüs  ,widerwärtig',  bodetis  ,sich  ekeln  vor';
toch.  B  peti,  A  poto  , Verehrung'.
WP.  II  130  f.,  140,  185,  W^H.  I  461,  495,  Feist  89  b;  anders  Kluge  »^  go.
bbeg-,
```


## [2026-09-05T06:21:13.579Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==122{print}' POK_01.txt | tail -30; echo \"##### grep bahis/bez\"; grep -n -i \"bahis\\|bahir\\|bāhya\\|bahya\" POK_01.txt POK_02.txt POK_03.txt | head -20"
}
```


## [2026-09-05T06:21:14.749Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=124 && NR<=126{print \"=== leaf\",NR,\"===\"; print substr($0,1,1800)}' POK_01.txt"
}
```


### [2026-09-05T06:21:14.994Z] TOOL RESULT

```
eln,   schauke! usw.;   vielleicht   älter    däa.  had   ^Kampf;  Schade^,   mnd.  hat  ^Schade, glück*^;,  iihd.  Blutbad.
Unklar  ist  das  Verhältnis  zu  *hliäut-  (s.  unten);  ist  statt  Hhät-  etj *bhuät-  anzusetzen,  oder  liegt  eine  Wz.  *bhä-  mit  verschiedenen  Forma tien  zugrunde,  die  vielleicht  in  lat.  fämex,  -icis  ,Blutunterlauf'  (*durj| Schlag  entstandene  Blutgeschwulst)  vorliegt?
WP.  II  126  f.,  WH.  I  46,  99,  452,  464.
1.  bhMu'  :  bha-  ,schlagen,  stoßend
a)  Mit  Präsens  bildendem  -d-: Lat.  füstis   (*b]iüd-sti-s)   , Stock,   Knüttel  (=  gall.  büstis  in  aprov.  bi
,Baumstrunk'^  usw.),  füsterna  ,Knorrenstück^;
air.  bibdu  ,schuldig,  Feind^  (*bhe-hhud-uöts),  mir.  büalaim  ,schla^e^  au? *bhäud-l- .  .  .  (oder  *boug-l- ...  zu  nhd.  pochen  oben  S.  98) ;  wohl  auca ! air.  bodar  ,taub,  betäubt,  verwirrt^,  cymr.  hyddar  ,taub^  (*hudaro-)-
aisl.    bauta   (-ada)   ,schlagen,    stoßen^,   ags.  beatan   (beot),   ahd.   boz(z)an. (biez  oder  schw.  Verb)    ds.,   mhd.  boz,    böz,    büz  m.  ,Schlag^,   nhd.  Ämboß^- ags.  bytel   ,Hammer^,    mnd.   botet   ds.,    mhd.    boezel   , Schlägel^,    aisl.  beytilt ,Zeugungsglied  des  Pferdes'^;  aisl.  biitr  ,kurzes  Stück  eines  Baumstamms mit  expressivem  tt:  ndd.  butt  ,stumpf,  plump^  (dazu  der  Fischname  Butte] mhd.    butze   ,abgeschnittenes    Stück,    Klumpen^,  ags.   buttuc   ,Ende,  Stüct Land'^,   norw.  dial.  butt  , Stumpf,  Klotz^  (auch   Holzkufe).    Aber  ags.  byi ,Flasche,  Tonne^  stammt  aus  lat.  buttis  ,Faß^,  ebenso  cymr.  both  ,Flasche'
aisl.  beysta  ,klopfen,  schlagen^  [Hhaud-sti-,  vgl.  lat.  füstis);  mit  -sÄ:-Suffix vielleicht  mhd.  büsch  , Knüttel,  Schlagt  (*bhüd-sko-),  vielleicht  verschieden von  büsch  , Rausch,  Wulsf,  s.  oben  S.  101.
b)  mit   f-Formans:
Alb.  mbütj  mbüs  , ersticke,  ertränke^,  skut.  miis  ,töte^,  vgl.  permismt ,niedergeschlagen^;  lat.  confütö,  -äre  ,niederschlagen,  dämpfen^,  refütö,  -an ,zurückdrängen,  widerlegen^  (mit  ü  aus  nachtonigem  au),  wahrscheinlich auch /ü^ziö,  -ere  ,beschlafen^;  air.  fo-botha  (Hutät)  bedroht',  Verbaln. /zt5- thad;  got.  baups  ,taub,  stumm^
WP.  II  125  ff.,  WH.  1  259  f.,  573  f.
2.  bhäu-  s.   1.  bhä-.
I.  b{h)e  und  b{h)eih  .  .  .  ,außer,  außerhalb,   ohne^
Ai.  bahih  (-s)  ,draußen,  von  außen,  außerhalb  von'  (m.  Abi.)
1
m
1.
113
or  hhe  ,olme^  (Präp.  m.  Akk.),  lit.  b^  ,oline^  (Präp.  m.  Gen.^  und  Nomi- loräfix);  lett.  bez  ^ohne'  (Präp.  m.  Gen._,  und  Nominalpräfix);  aksl.  bez yr  (dial.  auch  be)  ^ohne^  (Präp.  m.  Gen.^  und  Nominalpräfix).  Hierher uch  lit.  be  
##### grep bahis/bez
```


### [2026-09-05T06:21:16.553Z] TOOL RESULT

```
=== leaf 124 ===
  bodg,  bostl  (s-Aor.  bas^)  ,stechen',  bodr  m,  ,spina'  (*bod-lh)]  ^
toch.  A  pat-,  pät'  ,pfiügen';
vielleicht  auch  hitt.  pid-da-i  (kann  auch  pdd-da-i  gelesen  werden) ,macht  ein  Loch  in  die  Erde',  vgl.  Pedersen  Hitt.  77.
Vielleicht  hierher  gr.  ßö^Qog,  ßö&Vvog  m.  ,Grube'  ,Schwyzer  Gr.  Gr.  I  262, Zus.  2.  Anders  Petersson  Heterokl.  128  ff.
Wahrscheinlich  dazu   kelto-germ.  boduo-,  -ä  ,Kampf'  in  gall.  PN  Ate-bo- duus,    -uäj    Boduo-gnätus,    air.  bodb   f.  ,Krähe,    Schlachtgöttin    in    Gestalt einer  Krähe';  aisl.  bod  f.  (*badwö),  Gen.  bodvar,  ags.  beadu  f.,  as.  Badu^^ ahd.  Batu-  (in  PN)  ,Kampf'.
WP.  I  126  ff.,  188,  WP.  I  99,  521  f.,  866,  Trautmann  29.
2.  bbedh'  ,krümmen,  beugen,  drücken,  plagen'.
Ai.  bddhate   ,drängt,   drückt,  plagt',    Desid.  bibhatsate  ,scheut   sich   vor''|^ etwas,  empfindet  Ekel',  jün-bädh-  ,Knie  beugend';
alb.  bintj  med.  bindern  ,beuge  mich',  baskkr  ,zusammen',  bashkonj  ,ver-'i,J einige,  coeo';
got.  bida  ,Gebet',  ahd.  beta  f.  ,Bitte',  got.  bidjan  (sek.  -bidan)  ,bitten, beten',  aisl.  bidja,  ags.  biddan,  ahd.  bitten,  aisl.  kne-bedr  m.  , Kniepolster', ags.  cneow-gebed  n.  ,Gebet'  (vgl.  a,i.  jfiU'bädh-)]
lit.   bodüs  ,widerwärtig',  bodetis  ,sich  ekeln  vor';
toch.  B  peti,  A  poto  , Verehrung'.
WP.  II  130  f.,  140,  185,  W^H.  I  461,  495,  Feist  89  b;  anders  Kluge  »^  go.
bbeg-,  bheng'  ,zerschlagen,  zerbrechen'.  v^
.    Ai.    bhandkti,    Perf.    babhäüja    ,brechen'    (erst    nachträglich    nach    der  4 7.  Klasse   umgebildet),    bhaidga-h  ,Bruch;    Welle'   (vgl.  lit.  bangä  ,Welle')^ bhänji-h  ,Brechung,  Beugung,  krummer  Weg,  Absatz,   Stufe, 
=== leaf 125 ===
autentgleisung  Formen  mit  ei,  ai  (vgl.  Endzelin Lett.  Gr.  60)  in  lett.  beigas  PI.  ,Ende,  Neige^,  lit.  pabaigä  ds.,  beigiü  und iQiqiit  ,ende^,  lett.  beidzu  ds. ;  da  lett.  buoga  auch  ,steiniger  Platz^  be- deutet, gehört  wohl  auch  russ.  büga  ,überschwemmtes  Waldgebiet^  hierher; anders  über  heig-  (zu  bhei-  ,schlagen^)  Kuiper  Nasalpräs.  184.
Die  folgenden  Formen  sind  wegen  des  Auslautes  und  wegen  der  Be- deutuno"  fernzuhalten  und  wohl  als  Schallworte  zu  deuten:
o-erm.  *bang-  ,schlagen^  in  aisl.  banga  ,schlagen^,  bang  ,Lärm^,  engl. hang  ,klopfen,  schlagen^,  mit  Ablaut  mhd.  mnd.  bungen  ,trommeln^;  ndd. hengel  ,Knüppel,  LümmeU  =  nhd.  Bengel,  engl.  dial.  bangle  ,Knotenstock^, anord.  Beiname  bqngull.
Dazu  mit  intensiver  Konsonantenschärfung:
germ.  *bank-  in  aschwed.  banka,  abl.  bunka  ,schlagen,  klopfen^,  obd. hunken  ,klopfen,  stoßen^,  mnd.  bunken,  ndl.  bonken  ,schlagen,  prügeln'.
Lett.  bungä  ,Trommel^,  bunga  ,Schlag^  stammen  wohl  aus   dem  Mnd.
WP.  II  149  f.,  WH.  I  503,  541,  Trautmann  26.
bbSgb' :  hhogh-  ,streiten^
Gall.  bägaudae  ,aufständische  Guerillas^  (Suffix  wie  in  alauda,  hascauda), air.  bägaid  ,kämpft,  prahlt,  droht^,  bäg  f.  ,Kampf^,  mcymr.  btoyo  (*bägi') ,schlagen^,  kymwy  (:  mir.  combäg  ds.)  ,Streit^,  -boawc  =  mir.  bägach  ,krie- gerisch^;  falls  cymr.  bai  ,Fehler^,  beio  ,tadeln^  dazu  gehört,  müßte  es  idg. *bhdgli-  enthalten;
ahd.  bägan,  (bägen?)  ,zanken,  streiten',  aisl.  bäga,  bcegja  ,adversari,  resi- stere'^,  ahd.  bäga  ,Zank,  Streit^,  as.  bäg  m.  , Prahlerei^,  mhd.  bäc,  -ges  m. jlautes  Schreien,  Streit^,  aisl.  bäge,  bägi  ,Gegner^,  bägr  ,schwie
=== leaf 126 ===
 daz^ als  Neubildung  aksl.  pribägng,  pribegngti  usw.  .fliehen',  sowie  aksl.  bäz^^ beltati  .fliehen'  usw.;  )
toch.  A  fkänt  (pkät)  .entfernt,  getrennt'  (Van  Windekens  Lexique  96).
WP.  II  184  f..  Trautmann  29.  Meillet  Slave  commun^  220.  235.  Schwyl  | zer  Gr.  Gr.  I  717.
bbei'  .Biene',  mit  «-.  k-  oder  ^Erweiterung.
Die   kurze   Form    noch   in    aisl.  by-fluga,  alem.   5i.   bair.   beij;    danebeuj Formen   mit  n  (kaum   erst   der   schwachen  Dekl.    entnommen),    wie  ahc bini  n.  .Biene',  ablaut.   bla  f.    (*bl-ön-  =   ags.  beo,   engl,  bee),  bina  (nh( dial.  Bein);  aksl.  b^cela,  btcela   ds.  (*bhikela)',   cymr.  bydaf  .Bienenstock'^ apr.  bitte,  lit.  bite,  bitiSj  lett.  bite  .Biene'.
Gall.  *bekos  .Biene'  (M.-L.  1014).  air.  bech  m.  .Biene',  gäl.  speach  .Stich'/| cymr.  6e(7-e^(2/)r  .Drohne'  weichen  im  Vokal  ab  (tahuierende  Entstellung?).''^
WP.  n  184  f..  WH.  I  555  f..  Specht  Dekl.  46.  ^!
bheid-  ,spalten'.
Ai.  bhinddmi  (Partiz.  bhinddnt-  =  lat.  findens,   bhinnd-h  neben   bhittd-h =  lat.  ßssus),  bhtdämi   .spalte,   schnitze,  zerbreche   usw.'.  bhidydte   .wir(M gespalten';
wahrscheinlich  gr.  (psiöoiiaL  (redupl.  Aor.  hom.  necpiöead-aC)  .womit] knausern,  sparsam  umgehn;  schonen;  sich  einer  Sache  entziehen'  (GdbedJ z.  T.  vielleicht  .scheide  mich  von  etwas  ==  entziehe  mich',  vor  allem  aber] .abzwacken,  knauserig,  nur  wenig  wovon  sieh  abschneiden');
lat.  findö,   -ere,  fidl   (wohl   Aor.  wie   ai.  Opt.  bhideyam,   ags.  bite,   ahd. .    bizzi  .du  bissest'),  fissum  .spalten',  fissum  n..  fissüra  f.  .Spalt';
got.  iei^an  .heißen',  aisl.  blta  .beißen;  eindringen  (vom  Schwert  u.  dgl.)', ,  as.
```


## [2026-09-05T06:21:36.075Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD bheg\"; grep -n -i \"bheg\" AHD_watkins1985.txt | head -20; echo \"=== AHD bankon\"; grep -n -i \"bankon\\|bank-\\|bench\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-05T06:21:36.130Z] TOOL RESULT

```
=== AHD bheg
325:English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1280:BE- ambhi BEACON bha-1 BEAD gWhedh- BEADLE bheudh- BEAM bheue- BEAN bha-bha- BEAR! bher-1 BEAR? bher-3 BEARD bhardha BEAT bhau- BEATIFIC deu-2, dhé-1 BEATIFY deu-2 BEATITUDE deu-2 BEAU deu-2 BEAUTY deu-2 BEAVER! bher-3 BECHE-DE-MER mori- BECK? bheg¥- BECKON bha-! BECOME gWa- BED bhedh-
1287:BENCH bheg-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
2084:-PHAGE bhag-1 -PHAGIA bhag-! PHAGO- bhag-1 -PHAGOUS  bhag-! PHALANGE bhelg- PHALANX bhelg- PHALAROPE bhel-1, ped-1 PHALLUS bhel-2 PHANEROGAM bha-! PHANTASM_ bha-! PHANTASMAGORIA bha-1 PHANTOM bha-1 PHARMACOPOEIA kWei-2 PHARYNX bher-2 PHASE bha-1 -PHASIA bha-2 PHELLEM bhel-2 PHELLODERM bhel-2 PHELLOGEN _bhel-2 PHENO- bha-1 PHENOMENON bha-1 PHEROMONE bher-1 PHILANDER ner-2 PHILANTHROPY ner-2 PHILATELY tela- -PHILE bhilo- -PHILIA bhilo- PHILLUMENIST leuk- PHILO- bhilo- PHILODENDRON deru -PHILOUS _bhilo- PHILTER bhilo- PHLEGETHON bhel-1 PHLEGM bhel-1 PHLEGMATIC bhel-1 PHLOEM bhlieu- PHLOGISTON bhel-1 PHLOGOPITE bhel-1, okw- PHLOX bhel-1 PHLYCTENA bhlieu- -PHOBE bheg¥- -PHOBIA bhegw- PHOEBE bheigw- PHOEBUS bheigw- PHONE! bha-2 -PHONE bha-2 PHONEME bha-2 PHONETIC bha-2 PHONO- bha-2 -PHONY bha-2 -PHORE bher-1 -PHORESIS bher-1 -PHOROUS bher-1 PHOS- bha-1 PHOSPHENE bha-1 PHOSPHORUS bha-1 PHOT bha-1
=== AHD bankon
325:English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
934:*sua-yo-, contracted to *si-yo- in Greek huein, to rain, and huetos, rain: ISOHYET. II. Possible extended zero-grade form *sib-. 1.Germanic *sip- in: a. Old English sipan, sipian, to drink, sip: suP!; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic “supp- in: a. Old English sopp, bread dipped in liquid: sop; b. possibly Low German sippen, to sip, probably akin to the source of Middle English sippen, to sip: stp. III. Possible ex- tended zero-grade form “sig-. 1. Germanic *sik- in Old English sican, to suck: sucK. 2. Germanic shortened form *sukdn in Old English socian, to steep: SOAK. 3. Latin siigere, to suck: SUCTION, SUCTORIAL. 4, Variant form *sik- in Latin siicus, succus, juice: SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High German sudelen, to soil, do sloppy work, akin to Middle Dutch soetler, sutler: SUTLER. [Pok. 4. seu- 914.] si-lo-. Silent. Suffixed (stative) form *si/-é- in Latin silére, to be silent: SILENT. [In Pok. 2. sé(i)- 889.] skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.] skai-. Also kai-. Bright, shining. 1. Extended form *kaid- in Germanic *haiduz, “bright appearance,” manner, quality, in Old English -hdd, quality, condition: -Hoop. 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kdi- 916.] [skalkaz. Servant, slave. Germanic noun of unknown origin. 1. Old High German compound marahscalc, “horse-servant” (see marko-). 2. Germanic compound *sini-skalkaz, “old servant” (see sen-'). [In Pok. (s)kel- 929.]] skamb-. Also kamb-. To curve, bend. Suffixed form *kamb-o- in Celtic *kambo-, crooked, and denominative verb *k(a)mb-yo-, to turn, exchange, whence Gallo-Latin cambidre, to exchange: CAMBIST, CAMBIUM, CHANGE. [Pok. (s)kamb- 918.] skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; AS- CEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-sld- in Latin scdlae, steps, ladder: ECHELON, ESCALADE, SCALE?. sked-. To split, scatter. Extension of sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian, to scatter: SHATTER. 2. Variant nasalized form *ska-n-d- in Latin scandula, a shingle for roofing (< “split piece”): SHINGLE}. [Pok. (s)k(hjed- 918.] skeei-. To gleam. 1. Suffixed form “ske(ji-no- in Ger- manic *skinan, to gleam, shine, in: a. Old English scinan, to shine: SHINE; b. Old High German scinan, to shine: GEGENSCHEIN. 2. Germanic extended form *ski-m- in Old English scimerian, scymrian, to shine brightly: SHIM- MER. 3. Possibly suffixed form *ski-nto-, shining, in Latin scintilla, a spark: SCINTILLA, SCINTILLATE, STEN- CIL, (TINSEL). 4. Suffixed zero-grade form *skia-G-, *skiy-d- in Greek skia, shadow: SKIAGRAM, SKIASCOPE, SQUIRREL. [Pok. skai- 917.] skei-. To cut, split. Extension of sek-. 1. Germanic suffixed form *ski-nd- in: a. Old English scinu, shin, shinbone (< “piece cut off’): SHIN!-; b. Old French eschine, backbone, piece of meat with part of the back- bone: CHINE, 2, Latin scire, to know (< “to separate one thing from another,” “discern”): SCIENCE, SCILICET, SCIOLISM, SCIRE FACIAS; ADSCITITIOUS, CONSCIENCE, CONSCIOUS, NESCIENCE, (NICE), OMNISCIENT, PLEBI- SCITE, PRESCIENT. 3. Suffixed zero-grade form *skiy-end in Old Irish scian, knife: SKEAN. 4. Extended root *skeid- in: a. Germanic *skitan, to separate, defecate, in Old English *scitan, to defecate: SHIT; b. suffixed zero-grade
1287:BENCH bheg-
```


## [2026-09-05T06:21:37.199Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN bench\"; grep -n \"bench\" KLN_1971.txt | head -20; echo \"=== KLN bankrupt\"; grep -n \"bankrupt\\|banquet\" KLN_1971.txt | head -20"
}
```


### [2026-09-05T06:21:37.267Z] TOOL RESULT

```
=== KLN bench
25455:banc, n., bench, esp. bench on which judges sit. — 
25461:banke and see* bank, bench. Cp. also banc and 
25625:and next word, and see bench. Cp. also bunk, 
25631:bank, n., a bench. — ME. banck, prob. fr. OF. 
25632:baric , ‘a bench’, which is of Teut. origin. See 
25633:bench and cp. prec. word and banc, banco, 
25635:— F. banque, fr. It. banco , orig. ‘bench, table, 
25638:bank, ‘bench’, and see bench. Cp. also bankrupt, 
25649:‘a broken bench’, fr. banca , ‘bench’, and rotta 
25651:fr. L. rumpere, (see bench and rupture); so called 
25652:from the habit of breaking the bench of bank- 
25715:co, ‘bench’. See bench and -et and cp. banc, 
25721:‘bench’. See prec. word and -ette. 
25745:‘bastard’, lit. ‘conceived on a bench’, fr. Bank, 
25746:‘bench’; see bench and subst. suff. -ling. For 
28174:bench, n. — ME., fr. OE. bene , rel. to ON. bekkr , 
28176:OHG., G. bank, MHG. banc , ‘bench’, ON. 
28179:Derivatives: bench , tr. and intr. v., benching, n. 
28180:bencher, n., any of the members of the Inns of 
28181:Court. — Formed fr. bench with agential suff. 
=== KLN bankrupt
8990:‘banquet, merrymaking, revel’. See comedy, 
25638:bank, ‘bench’, and see bench. Cp. also bankrupt, 
25646:Du., lit. ‘sweetmeat’, fr. F. banquet. See banquet 
25647:bankrupt, n. and. adj. — Refashioned after L. 
25655:Derivatives: bankrupt , tr. v., bankrupt-cy , n., 
25656:bankrupt-ly , adv. 
25714:banquet, n. — F., fr. It. banchetto, dimin. of ban- 
25716:banco, banket, banquette. 
25718:Derivatives : banquet , v., banquet -er, n. 
25719:banquette, n., the foot bank of a trench (fort.) — 
25720:F., fr. Languedoc banqueta , dimin. of banc 
28177:bakki, ‘felevation’. Cp. bank, banket, bankrupt, 
28178:banquet, charabanc, mountebank, saltim banco. 
34158:less, bankrupt. — See prec. word, 
35680:burra khana, a banquet {Anglo-lnd.) — Hind. 
63909:to the banquet at which Dionysius seated Da- 
64210:dapis, ‘sacrificial feast, banquet’, lit. ‘expense’, 
67462:quet’, Saivuvai, ‘to give a banquet or feast’, 
81947:(see 2nd en-) and xt6p.o?, ‘banquet, revelry; an 
202905:regale, n., feast, banquet. — F. regal , earlier
```


## [2026-09-05T06:21:46.106Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28174,28182p' KLN_1971.txt; echo ---; sed -n '25625,25660p' KLN_1971.txt"
}
```


### [2026-09-05T06:21:46.185Z] TOOL RESULT

```
bench, n. — ME., fr. OE. bene , rel. to ON. bekkr , 
Dan., Swed. bank, OS., OFris., MLG., Du., 
OHG., G. bank, MHG. banc , ‘bench’, ON. 
bakki, ‘felevation’. Cp. bank, banket, bankrupt, 
banquet, charabanc, mountebank, saltim banco. 
Derivatives: bench , tr. and intr. v., benching, n. 
bencher, n., any of the members of the Inns of 
Court. — Formed fr. bench with agential suff. 
-er. Cp. disbench. 
---
and next word, and see bench. Cp. also bunk, 
‘sleeping berth’. 

Derivative: bank, tr. and intr. v., to pile up in 
a bank. 

bank, n., a bench. — ME. banck, prob. fr. OF. 
baric , ‘a bench’, which is of Teut. origin. See 
bench and cp. prec. word and banc, banco, 
bank, n., an institution for the custody of money. 
— F. banque, fr. It. banco , orig. ‘bench, table, 
counter’ (scil. of a money changer), which is 
of Teut. origin. Cp. bank, ‘the edge of a river’, 
bank, ‘bench’, and see bench. Cp. also bankrupt, 
bunco, embankment. 

Derivatives: bank, intr. v., to keep a bank; to 
keep money in a bank; tr. v., to keep (money) 
in a bank ; bank-able, adj., bank-er,n. , bank-ing , n. 
banket, n., the conglomerate in the Witwaters- 
rand gold district in the Transvaal. — S. Afr. 
Du., lit. ‘sweetmeat’, fr. F. banquet. See banquet 
bankrupt, n. and. adj. — Refashioned after L. 
rupta, fr. F. banqueroute , fr. It. banca rotta , lit. 
‘a broken bench’, fr. banca , ‘bench’, and rotta 
(fr. L. rupta), fern. pp. of rompere , ‘to break’, 
fr. L. rumpere, (see bench and rupture); so called 
from the habit of breaking the bench of bank- 
rupts. 

Derivatives: bankrupt , tr. v., bankrupt-cy , n., 
bankrupt-ly , adv. 

bankshall, n., 1) a warehouse; 2) the office of a 
harbor master {Anglo-Ind.) — Hind, bangsal , 
‘store room’, prob. fr. OI. bhandasala -, ‘store-
```


## [2026-09-05T06:21:47.595Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD abaz\"; grep -n \"abāz\\|abaz\\|ʾp̄ʾc\\|apāč\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD be\"; grep -n \"^bē\\| bē \\[\" PHD.txt | head -20"
}
```


### [2026-09-05T06:21:47.655Z] TOOL RESULT

```
=== PHD abaz
PHD.txt:122:/abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity. Afson ... add M ?pswn. Vagar ..., add useless. vāgēš [kw | (M "^ wa, P ?gwc), N aqóš] embrace, armful. add vājištag | gyštk' | P * gyšt, N ayišta] mixed, defiled. add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acquainted with. āštīh ... add concord. ayad ... read |" byd^t' |... for bahr... and bahrag ... read bahr(ag) |b hl(k') | M bhr, N ~(a)] part, portion, share, lot; reason. (az) an bahrag ray : on that account, therefore. for  bahrwar ... read bahr(ag)war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm. baxtan ... add divide. bayaspān [by?sp^n' | = M]... bélür ... for M read P bylwr.
PHD.txt:164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
PHD.txt:547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
PHD.txt:691:abandon abāz éstádan az, hištan.
PHD.txt:748:again abaz, did, P bid.
PHD.txt:860:ascribe to abāz dādan 6.
PHD.txt:892:attribute abaz dadan 6.
PHD.txt:910:back (av.) abāz.
PHD.txt:1573:desist from abaz éstádan az.
PHD.txt:2493:issue abāz raftan. item tag. itinerant wiyābānīg.
PHD.txt:2983:open (v.) abāz kardan, wišādan; (the mouth) wiyaftan.
PHD.txt:3218:prevent abāz dāštan.
PHD.txt:3332:rearrange abaz wirāstan.
PHD.txt:3334:rebellion abazsarih.
PHD.txt:3335:rebellious abāzsār, mustgar.
PHD.txt:3376:remain (abaz) mandan, (mānistan), padan, pattüdan ; — over parréxtan.
PHD.txt:3806:stay abaz padan, mandan, (mānistan), pattüdan, win(n)irdan.
PHD.txt:4096:turn (vi.) gardidan, waštan; (vt.) gardánidan, wardēnīdan; ~ ¿nto abaz waštan 6.
PHD.txt:4288:wean abāz kardan az.
PHD.txt:4328:withhold abāz dāštan.
=== PHD be
265:bēxtār [bwht?l | M bwxt?r] saviour. ~ih: salvation.
270:bēyēnīdan, bóyén- [bwdyn-ytn'] scent, perfume.
271:bēyestān [bwdst?n! | M bwyst?n, № bdstan] (flower) garden. ~ban [-p’n'] gardener.
273:bēz-, „išn, v. bóxtan.
3742:bēšūmand, pimgén, zarigómand.
```


## [2026-09-05T06:21:58.823Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN baz\"; grep -n -i \"apāč\\|apāc\\|apac\\|bâz\\|bāz \" HRN.txt | head -30"
}
```


### [2026-09-05T06:21:58.868Z] TOOL RESULT

```
=== HRN baz
```


## [2026-09-05T06:22:00.341Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB abaz\"; grep -n \"abāz\\|ʾpʾc\\|apāč\" NYB_vol2_glossary.txt | head -15; echo \"=== NYB be\"; grep -n \"^bē\\|bē '\\|be' out\" NYB_vol2_glossary.txt | head -15"
}
```


### [2026-09-05T06:22:00.403Z] TOOL RESULT

```
=== NYB abaz
4996:apa: apāč
=== NYB be
990:bēšāzišuēh det. v. n. of bēšāzišn healing: (yätuk) ~ gl. to biziskeh 44?. — Cf MPrs bys’zyn- ‘to heal? (A-H II)
992:bēšēnītār [~-ynyt’l] causing pain, pain- ful, excruciating: ~ dart 43%.
993:bēšītan [byšytn'] to violate 73%. 831, 9824. — MPrs and Paz.
7061:bē- (bī-): apa-
7062:bēš: vēš
7063:bēšah: vēšak
7065:bēxtan: vēxtan
```


## [2026-09-05T06:22:06.021Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apāč\" NYB_vol2_glossary.txt | head; echo \"---- context 4996\"; sed -n '4990,5000p' NYB_vol2_glossary.txt; echo \"==== search bE entry\"; grep -n \"\\bbē \\[\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-05T06:22:06.089Z] TOOL RESULT

```
4996:apa: apāč
---- context 4996
anyādā: ēnyā
aojah-: oZ
ap-: apam
ap-, äp-, avi-ap-: ayaftan
ap-: ap
ap < A + ap-: tigr-ahy
apa: apāč
apāxtara-: apāxtar
a-peronāyu-: a-purnāi
a-peronāyūka-: apurnā- yīk
a-puyant-: apčhišn
==== search bE entry
```


## [2026-09-05T06:22:11.352Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apāč\\|apač\\|ap’c\\|apāc\" NYB_vol2_glossary.txt | head -20; echo \"=== bE glossary\"; grep -n \"^bē\\b\\|bē \\[BR\\|bē\\[\" NYB_vol2_glossary.txt | head -20; echo \"=== grep 'bē' lines 970-1000\"; sed -n '975,992p' NYB_vol2_glossary.txt"
}
```


### [2026-09-05T06:22:11.418Z] TOOL RESULT

```
394:of; o pattākēh ~ to appear 513, 1081; 6 patirak ~ to meet 8%. 731.20-21, ete.; 6 en kustak rón towards this district 715; — with hac: from 184 ete. [hac ... be 6 ... ~ to be converted from... to... PR 945]; hac ... ywvatük away from 747-8, 7667; — with pat: on (a path) ibd. ; — with prev.: andar — to come forth, to appear 87?5; to be handed down 10818-19; — apāc ~ to become again 104?*; apdc 6 to return to 5) (v. bälist). 818-19, 914, 12]9-10; hac ... apāc ~ to return from 991; — apar ~ to shoot up 9573-4; to be allotted to 98*; apértar apar āyēt ku surpas- ses 641%; — hac varten beron be ämat got off the chariot 20?3; (coursers) ke pat róc-6 70  frasang bē āyēnd- (h)b who are always riding a dis- tance of 70 parasangs in one day 6! (v.s.v. h-); hān<i>druž (be) āyēt the space which the Drug will cover 96?3, 9818; bé + the pres. of ~ regularly denotes the fut.: 24"; if the vb. takes the prep. 6 the order is always be 6: 9725, 985-6, 9912-13, 1046-7; — fröt ~ to come down, to descend (hac...6...) 104°; — ul ~ to rise 86°; šuhr pat post ul āmat the sperm rose to the skin 547°. — āmatan < *ā-gmatanai from à + Av. (493 sqq.) OP gam-, cf OP (par)ägmata- ‘gone forth’; äy- < à + Av. (147 sqq.) OP ay-; MPrs ’mdn ”y-; Paz. NP dmadan dy-. This vb. is characteristic of the SW dialects, as against NW āgatan,
407:ümurZitan [’mwleytn'] to forgive, to absolve, with be 3114. 35%. 67°; to pity 76°; Gi hac 61... bē āmuržīt this (bull) shielded him 49°, with the gl. kū-š gāvān haciš apāc dašt. — Ps. pt. ’mwicyt; Paz. dmuržidan, NP ämurzidan; MPrth subst. ’mwjd ‘compassion’ (A-H III), "mwždyft ‘mercy’ (S); MPrs ’mwrzydn (S), pres. >muw(r)[2- (Sogd. 45); Verbum 168 sq. Av. (1175) moroždā- pres. ‘to forgive’, marazdika- "mercy'.— V. also an-āmuržišn. āmušt [Pmwšt'] crushed 2622-24, — < *a-murst < *d-mrsta- < à + Av. (1150) marod- ‘to destroy’, cf MPrth >mStn, pt. ’mst ‘to crush, to destroy’ (A-H III), which seem to go back, quite irregularly, to *āmdrsta-; as to -rst > -št cf dāštan, vaštan, vitaštan; the explanation given in Verbum 218 is not satisfactory. Ghi- lain 99.
439:and [’nd] so much, so many: én ~ this much 64°; all this, all these 351. 623. 6572.24; hac én ~ sal apāc since so many years 1674; han ~ dušman all these ene- mies (sg. as with numerals) 249; 10426, 11923; — ~ cand as much (big, large, high, etc.) as: 3119-15, 935. (935 without ~); ~ cand yašt-ē (as much as =) at least some ceremonies 659; — hän <... cand as much (many, long, ete.) as 92°. 997. 10027, 10324-25; 2 ~ dranäi pahnāi cand han i nn hast twice the length (and) breadth of it as it is now 10024-25; 7000 han ~ cand
476:apäc [L'WEIL ; ’p’c] 1. adv. back, back- ward (opp. frāc 25?-*), again: hac 7-salak ~ for seven years 16?5; hac én and (q.v.) sal ~ 1674; — prev. with vbs. of motion, e. g. dmatan, šutan, vastan, ete., and many others, e.g. guftan, gumeatan, etc. — 2. prep. with (= apäk) 42%. — 1. < *apācā instr. adv. from Olr adj. *apdnk-, weak st. apük- and apác, derived from Av. (72) apa, OP apa, cf Skr apdfic- ‘situated be- hind’; MPrth °b’c; Paz. awāž; NP baz. — 2. < *upācā, instr. adv. from Olr adj. *wpünk- derived from Av. (388 sq.) upa, OP upä ‘under, with’; J-Prs ?b?z ‘with’ (common); v. further apäk.
479:apāc-kartakēh [L°>WHL ‘BYDWN-tkyh] the state of having been taken to pieces,
481:apāc-sārēh [—-s'lyh] rebellion 13%. — Paz.
482:awāž-sār ‘headstrong, rebellious, abstr. awāž-sārī SGV XI, 247-249, < apāc (1) + sār < Av. (1572) sära- = sarah- in compounds. Cf nigne-sär.
494:silent again, ceased speaking 342°; — 1. < *upäkä alternating with *upäcä, v. apäc 2; — 2. < *apdka- alternating with apäca-, v. apāc (1). MPrs ’b’g; Paz. awä; NP bä, prev. vä-.
622:ärästär restorer, pl. cas. obl. —-än 1105, arastarčh: apāc ~ restoration 111".
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
1117:cê [MH; cyh 12111] 1. interrog. pron. what? 59. 726. 89? ete.; how? 1513, 51?!; with prep. 6 cé, pat cé, hac cē; cé rād? why? 351! ete.; combined with a subst.: ce zaman? 715, cē gah? 722; pat ce āivēnak? how? 76%; cé vinäs? 121, cē vat? 7322, etc. ; apar cē ātvēnak margēnītan i Zartuxst pursit how to kill Z. 4912-25-26, 4813-14 (apar governs the whole clause). — 2. rel. pron. what: či ndmakY ce ... nipištv estet, ce Šahpuhr" . . . framätY nipigstany P 2:3-4; kart" ... ce ... sahät P2:8-9; har ce 61.3218, 86%. 9618; ēt ce ... apāc āvurt 11214715; 361; pat hàn cim rād ce 121". — 3. conj. a) subordinating: because 105); ce ka id. 991. — b) coordination: for 2$. 619.22. etc., passim. — MH 305 wrong ideogr. for encl. -c(%). — < cahya, gen. sg. of Av. OP (422 sq.) ka-.
1227:dat [d?t'] 1. law 6413-19, 6916, 8623, 9811, — 2. age 2?9 (with the gl. hangäm). 31. 10*%. 14°. 165. 622. 104°; cas. obl. dātēh 536-22, — 3. created, pt. of dätan: dēvān ~ created by the devs 1038-10-13, — 1. Av. (726) ddta- NP ddd ‘justice, equity’. — 2. NP dad ‘life, age’. — 3. Av. (671 sq.) daēvē.dāta-. dätan [YHBWN-tn'; d’tn' 119%, 1201] dah- [always YHBWN-], lst p. sg. YHBWN-m = dahom; 3d p. sg. = 2nd p. pl. ~ -yt = dahét; lst p. pl. ~-ym = dahem; 3d p. pl. ~-d = dahénd; subju. 2nd p. sg. —-'h = dahäh 34%; imp. sg. ~ = dah; pt. = pret. pass. 3d p. sg. dāt [YHBWN-t', inser. YHBWN; d>t' 22. 922 etc.] lst sg. dāt hom 57°; 2nd p. sg. dāt h&5'1*-* 3d p. pl. dāt hend '18?, construed as an act. form 18?!; pluperf. 3d p. sg. dat estet 8712, 3d p. pl. ~ ēstēnd 94*4; opt. pass. dāt [HWH-d =] he 2%; A. to give SPrs:15; 238-21 ete. passim; apāc ~ to give back 345-6; — fräc ~ to give away 5016-1’; — v, also dröt, framān, passax", zančh. — B. 1. to put, to place,
1420:dvaristan [dwb'lstn'], dvaritan [dwb'lytn'] to run, to rush, of enemies and demoniac beings 2518 ete. passim; — andar ~. to rush, to come dashing (6 into the presence of) 7526; to make an onslaught, of Ahri- man and the demons at the beginning of the world 933.13, 9519, 10318; to make an assault upon (6) 1142; — apāc ~ to run back 1024; apar ~ to coil upwards (up a tree) 4012; — bē ~ to dash off 422, 10211.14.20; — frāc ~ to rush forth 25%; to spring forth (hac from) 9674. 9819. — Av. (765) dvar- ; Paz. duärestan, dvärestan. dvarišn [dwb'lin'] the act of running; as pred.: has to run, or is running 6811-12, dvārišnēh det. v. n. = the preceding w.: višāt- ~ the act of running about with loose, open clothes 69%, v. višat. dväzdah [dw’cdh; figure] twelve; han 4 12 axtar, 12 axtarān etc., v. axtar; dväz- dahān [dw’cdh’n'] the Zodiac 57. [12-n!] Ti: i dvàzdahom [dwb’cdhwm; 12-wm] the twelfth 8216, 844, E
1454:éstatan (YK-YMWN-tn', yst'tn'; forms v. I, 177] 1. As an independent vb.: to stand 78. 1112, 2012. 3812, 7214; with prep. andar 9571-22; with apar 2874, 389; with pat to get up on 33%, in a figurative sense: to remain in, to live in 7419-16, to abide by, to stick to 58°. 6419.17; pat ravisn ~ to be in continual movement 9318-19; with 6 to set out on, to go into 19. 139. 10012; — apar pad ~ 18?!, apar 6 pad ~ 2513, bē 6(i) pad ~ 3424.27, 352, frāc 6 pad ~ 26°: to rise to one’s feet; — with prev.: andar ~ to befall 54!?; to remain, to be therein 95°. 9715; — apāc ~ to
1709:griftar [glpt’]] a p. who "catches”, i.e. incurs, liability: 1. ku pat dat 1 dévan ~ né bavé lest thou shouldst be subject to the law of the demons 6916-17; [ruvan pat ménoyan pat kunišn aržānīkēh ~ kunénd in the heavenly world they (the gods) call the soul to account according to the value of her deeds Mx ch. 382-6 (~ kunénd = girénd 65°, v. griftan)]. — 2. condemned to (šahrē-karān, v. s. v. kar) 92; prisoner: ~ kartan to imprison, to capture 615; [more general, to catch hold of: api-§ — kunēt u apāc 6 rah i yazdān āvarēt Mx ch. 1525]. — Cf NP gér?ftàr; v. also a-griftär.
1722:A. 6818: 7719-20, 7913-14-16, 8756.27 sq. 1068-9; with acc. c. inf. 11119, — authoritative religious sayings are in- troduced by the formulas cigon den göbet kü (36-54, passim), with hat instead of kū (387-8. 4325-26, 4414-15, 503-5), pat han + den gūbēt kü (43155), cigon ët i den gobet ku (533-24 ete.), seldom andar den guft estet ku 80"; regularly guft ēstēt is used of traditional, extracanonical sayings: 621-2, 6614. 6819. 6923, 7012, 1061-1, — with božišn, passax” and other subst., v. these; — apāc ~ to repeat 521-22; — apar ~ to utter loudly 45?!; — frže ~ to pro- nounce 581-?; v. also peš. — OP gaub-;
1738:apäk 971, andar 423, 6 42?5, andar 6 93"*. 10419-20, 116°; hakanén ~ to intermingle, to become blended 431; andar € giyäk gumēztēnd they will crowd together in one place 9615. 9812-13; apāc ~ with a pred. to mix so as to become again 10416-17, apāc 6 . apäc ~ id. 10417-18, — < *vi-maik-, vi-maic-; MPrth wmyxtn; MPrs gumyxtn, pres. intrans. gwmyas-, v.n. gwmyzysn (S), gwmyg ‘mixture’ (A-H II) confirming -k as the final cons. of the root; Paz. gumertan gumēž/z/-, gumežjzjašn. — V. ämecisn, ümek. gund [gnd] troop 8-18, — MPrth gwnd, Arm. lw. gund, Arab. lw. jund; cf Bailey, TPhS 1955, 73 sq.
1883:handixtan [hnd*htn'] handdc- 1. apāc ~ to bring together again, to reunite, with apāk ‘with’: apāk apastak apāc handāxt reunited (them) with the Avesta 1091, 11119-20, — 2. to measure, to calculate (the horoscope) 7$. — 3. impers.: api-m
1885:handāxtārēh [hnd’ht’lyh]: apāc — i 6 the act of bringing back to 11216,
=== bE glossary
990:bēšāzišuēh det. v. n. of bēšāzišn healing: (yätuk) ~ gl. to biziskeh 44?. — Cf MPrs bys’zyn- ‘to heal? (A-H II)
992:bēšēnītār [~-ynyt’l] causing pain, pain- ful, excruciating: ~ dart 43%.
993:bēšītan [byšytn'] to violate 73%. 831, 9824. — MPrs and Paz.
7061:bē- (bī-): apa-
7062:bēš: vēš
7063:bēšah: vēšak
=== grep 'bē' lines 970-1000
Religion 1097-8; hac kunišn 4 im bē out of the activity of this man 5212; — c) late, for pat, as NP bi-: bē ravākēh bavet 37? (gl.); 4717 (gl.); 502° (editorial summary). - 4. adversative conj. but: a) after a negative sentence or a negative part of the sentence: andar déh ne, be pat kustak-é € deh vitart 61%; nē ozančt, bé apäc 6 Käyös Sut 4527, ete.; ne ēvāc ... bé not only...
www.parsianjoman.org | ool sa,
bé
but (also) 455-5; — b) but, however, contin- uing the narration: HajB:8 (second BL") [= bes HajA:7, v. below]; 197-24. 2115 ete. — MPrs by only with the enel. --c: byc ‘but’ (v. 4b) and in by-rwn (v. beron), in all other cases 5b’, to be read bd, shortened form in proclitic position (cf k? = ka, v.s.v. ka); MPrth byh ‘outside’, ^ byh, ^w byh ’rg; conj. byc, byž ‘but, however’, Prth. inscr. bes (v. below). Paz. be, bi, be; NP only prev. bi-. Original form *bét, cf bēt-ānak ‘an outsider, foreigner’; MPrs bydwm ‘outermost’ (S) = Paz. bétum (SGV). [MPrth byd ‘again, further’ (= MPrs dwdy) belongs to the numeral ‘two’, and not to this w.] — BR? 19% is a wrong ideogr. for beh, opt. of bütan.
Béhistan [byhstn'] n. pr. f. 285. — NP bih ‘quince’; already Justi, NB 67, inter- preted the second element as Skr stana- ‘bust’. ‘having breast like quinces’. Cf the epithet beh-pistän applied to a woman, Unvala, King Husrav 35 (§ 96). The same -stan in Zarri-stan (g.v.). Cf, on the other hand, Bthl., ZsR I, 15 no., V, 20.
bérón [bylwn'; inser. bylwny] outwards HajB:10; out, connected with matan, āvurtan, kartan, v. these vbs.; kac... ~, v. āmatan; — prep. — asman kartan to put out of heaven 1039, — MPrs byrwn (S, BBB); Paz. bērūn; NP birün; < be + ron (g. v.).
ībēš [bys] grief, affliction 1116. 481; ~ burtan to grieve, to mourn 681, 8413, — Av. (814 sq.) dvaēšah-, tbaēšah- ‘hostili-
ty’; cf MPrth "'n"byš ‘without violation’ |
(BBB 53); Paz. bēš. Derivatives v. below.
2bēš (Prth) [byš] but, HajA:7. - < bē-c, v.s. v. bé; Prth c has very often changed to š, ef s. v. šit.
-wm
bčšizčh [byš*cyh] the act of healing; re- medy 4374. — Av. (9014sq.) baēšaza- ‘healing’ (adj.), ‘remedy’; MPrs byš?z ‘physician’, bys?zyh ‘the healing art’ (A—
bitaxš
H IÏ), cf Paz. baēšaž-gar ‘healthful’ (Mx).
Borrowed from Av.; the genuine WIr. forms v. bizisk.
bēšāzišuēh det. v. n. of bēšāzišn healing: (yätuk) ~ gl. to biziskeh 44?. — Cf MPrs bys’zyn- ‘to heal? (A-H II)
beš-burtar [bys bwlt?l] grieved 681°, v. bes.
bēšēnītār [~-ynyt’l] causing pain, pain- ful, excruciating: ~ dart 43%.
```


## [2026-09-05T06:22:27.066Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '965,978p' NYB_vol2_glossary.txt"
}
```


### [2026-09-05T06:22:27.109Z] TOOL RESULT

```
bazak [bck'] misdeed, crime 6817. 73° etc. — MPrthPrs bzg ‘evil, wicked’; Paz. baza, baža, bažaa (SGV); v. Bailey, BSOS VII, 1933, 85.
bazak-kar [bckly] evil-doer 1285. - MPrthPrs bzkr; Paz. bažagar (SGV). Cf also s. v. davr.
bāzūk [b'ewk'] arm 311”. — Av. (955) bāzu-; Ps. SW form b’dwky; NP bàzü; cf MPrth b’zwr (= bäzuvar) ‘wing’ (MHC).
bāž [b*c'] tribute 177. 5825, 11815-23, 1218, — OP baji-; NP baj, bad, baz.
bé [BR”; Sas. inser. BL”; Prth. LBR"] with enel. bé-c 3812, bé-p 53%, cf also 2bēš: l. adv. outside HajB:8; HajA:7 LBR = ö bé outward; ibd. 9 ‘L LBR? STR? = 6 bē ärak id.; — hac bē Xvanirah from outside Kh. 10812; — bē hac to out- side thee, thy domain 1035 (v.s. v. tē):!!; — together with a following prep.: bé 6 emphasizing the sense of direction inherent in 6, very frequent; still more emphatic tdi bē 6 right up to 9218; bē apar Zartuxst nīšān (g. v.) dräyit 487-8; — bē! away! 14%, — 2. prev.: a) off, out, away, forth, esp. with vbs. designating a motion or a change of place or of condition, v. each separate vb.; cf fratom 6 ünód apar raft, avdom bē raft he (the horse) was the first to come there, and the last to go away 49%; HajB:8 (first BL’). In this case be, as giving the vb. its specific sense, is not dropped when other preverbs or the negation are added;
m
| it also accompanies the vb. in the inf.,
the v. n. and the pt.: bé tacét, bé tacitan, bé tacióneh (e.g. 564); be šutan to go away, to disappear, bē šutak gone, van- ished 5?; etc. — b) denoting the per- fective aspect of the act, viz. that it comes to an end, or has its limit: with the pret. it gives it the sense of an act completed in the past, as in French the passé défini or in Lat. the perfectum historicum; with the pres. it denotes the completion of the aet in the future (Milr. has no special future tense); it is very often put before an imp., giving the order a peremptory force; also used in other expressions implying an act of will, cf apdyistan and framūtan; in this sense it does not stand together with an inf., or with a pt., nor with a negation, nor with other preverbs (which themselves give a_ perfective sense): be bavét he will be, but nē bavēt he will not be. The functions a) and b) are often difficult to keep apart. — 3. prep. a) except, but: hec zvandak apdc bà nē mānēt be hàn i ēvak Arjāsp no one but A. alone 2926-27; 2415-16; 964; cärak be man an kas xYāstan nē tuvān it is not possible to request a means from any other than me 34?; followed by a sub- ordinate clause: nisem nē vindät bē ka
. 6 kēft sar nišinend did not find foot- hold except if they perched 2018-19; 2115-16; 65?! (v. pätixsäi); — b) in frame preposi- tions: bē... ēnyā, v. Enya; — be... tài: be man tài an kas nē mand estet no one except mehas been spared 15?’ ; be Zartuxšt
tat ... kas-ic ne nobody but Z. alone 9313-14; — hac ... be: nipekihä i hac den bé writings outside (= not concerning)
Religion 1097-8; hac kunišn 4 im bē out of the activity of this man 5212; — c) late, for pat, as NP bi-: bē ravākēh bavet 37? (gl.); 4717 (gl.); 502° (editorial summary). - 4. adversative conj. but: a) after a negative sentence or a negative part of the sentence: andar déh ne, be pat kustak-é € deh vitart 61%; nē ozančt, bé apäc 6 Käyös Sut 4527, ete.; ne ēvāc ... bé not only...
www.parsianjoman.org | ool sa,
bé
but (also) 455-5; — b) but, however, contin- uing the narration: HajB:8 (second BL") [= bes HajA:7, v. below]; 197-24. 2115 ete. — MPrs by only with the enel. --c: byc ‘but’ (v. 4b) and in by-rwn (v. beron), in all other cases 5b’, to be read bd, shortened form in proclitic position (cf k? = ka, v.s.v. ka); MPrth byh ‘outside’, ^ byh, ^w byh ’rg; conj. byc, byž ‘but, however’, Prth. inscr. bes (v. below). Paz. be, bi, be; NP only prev. bi-. Original form *bét, cf bēt-ānak ‘an outsider, foreigner’; MPrs bydwm ‘outermost’ (S) = Paz. bétum (SGV). [MPrth byd ‘again, further’ (= MPrs dwdy) belongs to the numeral ‘two’, and not to this w.] — BR? 19% is a wrong ideogr. for beh, opt. of bütan.
```


## [2026-09-05T06:22:45.446Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7055,7070p' NYB_vol2_glossary.txt; echo \"=== IEC leaf 44/45\"; awk 'BEGIN{RS=\"\\f\"} NR>=43 && NR<=46{print \"=== leaf\",NR; print substr($0,1,2500)}' IEC.txt"
}
```


### [2026-09-05T06:22:47.690Z] TOOL RESULT

```
bāxtar: apāxtar
bayistan, bāyad: apāyis- tan
bāz: apāc
bāz kardan: apāc-karta- kēh
bažandī: apa-cand
bāzīdan, bāxtan: vāzītan
bē- (bī-): apa-
bēš: vēš
bēšah: vēšak
Bēvarasp: Bēvar-asp
bēxtan: vēxtan
bih: vēh
bih: Bēhistan
bihišt: vahišt
bīmār: vimar
bīnī: *duš-viyāk
=== IEC leaf 44/45
=== leaf 43
babol-, babər-, babot-, see bob-, bəbəd-, etc. (A theme of onomatopoeic character as are most IE themes with initial b-)
bābā (1), üs “old woman? Osc. (queried) babu “old priestess’; R bàba *woman'; Cz. bába, Srb. baba “old woman, midwife’. Cf. bhabh-
baba (2) ‘mess, slobber’ It. bava ‘drivel, dross, waste’; Fr. bave, id.; Du. poep (2) ‘excrement’; E dial. poop, id.; Cz. bába ‘bread-pudding, brown beer
babraio ‘slobber, mess about. Cf. bābā (2) Du. cf. poeperij ‘diarrhoea’, poepert ‘arse’; Fris. id.; Pol babrać ‘slop’; Cz. babrat ‘potter’
baĝāið (bagið) “kiss” Fris. patsjen; Cz. bozati, id.
bak- (?) ‘faint, limp’
Alb. bákem (v. ‘faint’); Ir. bacaim “lame,
hinder’ (ambig. cf. below; guaks-)
bal-, (baliio) ‘great-, greater’. WP II, 110. Cf. bel- Skt. báliyah ‘stronger’; Phryg. cf. balen ‘king’; Lat. cf. balivus (?) “bailiff” beside It. balía ‘power’; Br. béli, f. (power; bailiff': possibly Celtic, cf. Gael. bolanta, for (?) *balanta *excellent); Ir. cf. baileach “rather; OCS bolij; bolje ‘greater, more’, a possible cpd. in bolü-vanü ‘boulder
balb-, see bolb- (blb-)
bamb-, see bamb-
baubo, ið “roar, bellow, bark'. WP II, 104 Lat. baubor, àri; Li. baubiu, ti
bab-, babod-, babol-, babor, babot- — bolbotio (bolbütio, bIb-, bulb-)
B
20
25
30
35
40
50
bekio *bleat, bray' It. cf. becco ‘billy-goat’; Br. bégia ‘bleat’; Cor. bégy, begya, id. (and "brav Cz. bečet, Pol. beczec, Srb. becati ‘bleat’ beside Slovene békati, id.
bel- ‘strong, great', etc. See bal- (baliio-) Skt. (ambig.) bálam ‘strength’; Gk. cf. bel- tíon; Lat. cf. de-bilis
belbetióo, belbotio, see bolbotió Cz. cf. blebtati, Srb. blebetati ‘twaddle’
bobaio ‘prate’. Cf. baba (1) and next Gk. babázo; LLat. babare (both ambig.)
bobodió ‘prate; drivel Gk. babázo; Br. babaza ‘twaddle; slobber
bəbəl- ‘gibber; gibberish’. See next Lat. cf. babulus “silly; twaddler’; Cz. beblati ‘prate’; Blg. báblío, bábla, s. ‘stammerer beside băbljam ‘stammer, chatter
bobor- ‘prate; gibberish’. Cf. bəbəd-, bəbəl-, bəbət- MLG paperen ‘mutter’; Blg. băbrjam, băbrja ‘chatter, twaddle’
bobotió “bubble; prate’. Cf. bəbədið, etc. Arm. papačem ‘bubble’; Br. (ambig.) babaza (‘twaddle’. Cf. bəbad-); Blg. bobótja ‘rumble’; Srb. boboćem, bobotati ‘shiver’.
bəlbəl- (bələbəl-) ‘twaddle’. Cf. belbetio, bəlbəti
=== leaf 44
angle’ beside burbeti ‘mutter’
biĝ- ‘wax, glue, resin’ or sim. Oss. bidz, D bedzä ‘lees of beeswax’; Ir. bigh ‘glue’; Arm. cf. piyc (‘dirty’, fr. *biglo-)
bi&- ‘titch, tot; dot Skt. bijam 'seed, germ'; Arm. cf. pz-ti, pz- tik ‘tiny’; Go. cf. peika-bagms (fpalm-tree', lit. *prickle-tree. Here despite SF); OE pic ‘point; ON pík ‘pikestaff beside píka ‘girl’ and com. N; LW in Romance (It. picca, etc. beside picco (peak); Finn. LW piika ‘girl’. Speculations in EH: pig, pigg, pik. Gmc. history uncertain.
biks- (?) “point, dot; small ` Oss. bik, D bekä ‘pimple, point, navel’; Olr. becc, Ir. beag ‘small’; W cf. bych ‘wretch’
bimbos, å (?) Skt. bimbah, am “disc, mirror, picture; lizard’; bimba ‘red gourg’; It. bimbo, bimba ‘infant’; SEGer. Pimpf 'youngster; LG cf. pimps ‘youngster, midget’; EME cf. pimping “tiny, puny’
bisəlos, bisos, å ‘shoot, bud, phallus, nerve, cord’ Skt. bisalam '(sprout; bisilah ‘sprouting’; bisam, bisa ‘fibre, sucker, root’; Du. pezel ‘phallus’; pees ‘sinew, cord’; E pizzle
blaboró, ið (bləb-) ‘twaddle, chatter, stam- mer’. Cf. balb-, bəlb- Hes. blabüro ‘flutter; twaddle’; blaburía
10
20
25
30
35
40
45
52
‘twaddle’; Ir. cf. blabarán ‘stammerer’; LG. Du. plappern, plapperen (‘twaddle’. LW in HG); Li. cf. bleberis ‘twaddier’. Onomat.
bladið (?) (blnd- ?) For alleged *blakt-, see Suppt. Gk. blázo “play the fool, lark’, bladá ‘follies’ (preferably < blnd-, q.v.); SWGer. plátzen ‘slap’; OE plaettan, id.; plaett, s.
blateró ‘chatter, clatter. WP IT, 120. Cf. blatio (blt-) Lat. blatero; MLG pladeren ‘chatter’; LG pladdern ‘splash’; LWs from LG in Dan. pladre ‘twaddle’; Sw. pladdra, id. (EH)
blatio ‘twaddle’. Cf. blatero. For alleged *blagh-, *blegh-, *blog- see end. Lat. blatio, ire; R cf. boltát (fr. *blt-)
bloskó ‘dash, clash, crash, splash’. WP II, 218 & II, 209. See next Mir. bloscaim ‘bang, crash’; Ger. cf. pflat- . schen “bang, splash’, beside (LG form) plat- schern ‘splash’; N plaske, Sw. plaska, E plash; Li. blakaü, ýti ‘thrash about, fling about. (A variant occurs in Big. bláskam “beat (*blusk-)
bloskos “bang, dash, etc? Cf. blosko. Cf. WP II, 218 Mir blosc; E plash; Li. bláskas ‘threshing of corn'
blu- “an intestine" (?) E pluck ‘intestines of game’; Li. cf. blužnis, iés ‘spleen’; OPr. bluzne, id.
bInd- (?) ‘pleasantry, foliy’.
=== leaf 45
m; slobber, prate’; LG praten "chat": beside prāt ‘gossip’; Norw. (fr. LG?) prate, id.; R brodit ‘ferment’; Blg. brodjá, id.
braĝið ‘roar, bray, bleat Fr. braire (fr. *bragire); W breu ‘bleat, low’; Latv. brāžu, brāzt ‘rage’. (The background of Gk. brásso is uncertain)
brāl- ‘boasting, brawling’ W brawl, pl. broliau ‘boast; MLG prðlen ‘swagger’ (also prālen, beside pral, gs. pralles ‘din’) (Ger. prahlen & Sw. pråla fr. LG)
brékio ‘cry’ Du. praaien, LG praien, id.; Latv. brēcu, brēkt, id.
breunos, å ‘tip; bit’ (?) Mir brúan ‘fragment’; Cor. (ambig.) brunyon, pl. ‘oats’; OE, ON preon, prjónn ‘pin’ (specu- lations in FK: Pfriem, -e and in AD: brin); Li. briaunà ‘corner, tip’, briaunýs ‘prism’
brig- (?) ‘turbulent; turbulence’ Ital. (Gallo-Lat.?) brigare ‘strive’, briga, f. ‘strife; MDu. priken ‘exult’; Du. prijken ‘display os: Slovak brihat ‘brawl; OCS briZiti ‘afflict, briga ‘affliction, sorrow”; Li. cf. bryzgiù, brygsti ‘buzz, hum’; (-ï-) in Br. bré ‘toil, hardship’
bronghos, à, is ‘oppression, grief. WP cf. II, 119, 668. Cf. bhrongh- Alb. brángé (2) ‘grief; Go. cf. ana-praggan ‘oppress’; MHG  phrange ‘enclosure’, phrengen 'squeeze, oppress'; Du. prang “pres- sure, oppression ` OSw. prang (“narrow lane, gorge'. Isophonic with Gk. brógkhos, though prob. of difft. origin); Sw. práng *breaking- in device for horses, trave’; Icel. pranga
bombos — bubul-
20
25
30
35
40
45
54
‘haggle’; Li. brangùs ‘costly’; brangà ‘cramp, bracket. (Alb. brângë, -ê- is ambig.)
bronkà, om, is ‘swelling’. Cf. bhronk- Alb. brángé&, bréngé (1) ‘swelling, tumour’; Sw. cf. práng (1) ‘swagger’; Li. brankà 'swel- ling’. (The Alb. & Li. forms are ambiguous)
brotos ‘red liquid" (?) Gk. brótos ‘gore’; Cz. broť "red sap, woad’; Srb. broé "madder" cf. Cz. brotit, Pol. broczyc *bespatter w. blood'. (The Slav evidence is ambig., cf. bhrakt- in view of OCS brosti ‘purple dye’ & Ir. bracht 'sap")
broukos (breukos, ios) (?) “bug, beetle’ Hes. broükos, breükos ‘locust, and larva’; Alb. cf. bruc ((cockchafer', fr. *breutios); Cz. brouk ‘beetle’ (ambig.); LW in It. bruco
brüsd- (?) LG prusten ‘splutter, blurt out’, Sw. (fr. LG?) prusta ‘snort sneeze’; Li. brüzdü, brüsti “be busy’. (Ambiguous are Ir. brüid “hot ashes’; Gk. brúð (‘gush, teem, be full, prob. fr. *guruio, and L
=== leaf 46
hort ‘crumbly’, see C. T. Onions: cold-short, of iron: ‘brittle when cold”, shortbread, etc.)
brks- (?) ‘mugwort, wormwood’ Gk. cf. brákanon 'potherb'; Gallo-Lat. bri- cumus ‘wormwood’; LG. cf. porsch (“mug- wort’ or sim.)
bubolio, see buburio and next
bubul- (1) ‘rumble, throb, bubble, babble’. Skt. buburah ‘water’; Alb. bubulloj, bubullij ‘tumble’; Lat. cf. bübulare (&hoot', *büb-); MLG popelen ‘bubble up’; OE pypelian
 
55 bubul- — bülð . 56
‘erupt’; Du. popelen ‘throb’; Cz. beblat 'stut- ter; Li. cf. bubulis, io ‘poltergeist’; Latv. bubulis ‘din, rumble; poltergeist’. For the simplex, cf. Ir. bub ‘din’ and EME pop; OCz. bebtavy ‘babbling’. (The Alb. Slav. and Balt. forms are ambiguously *b- or *bh-). Lith. cf. bübis ‘poltergeist
bubul- (2) “knob, knot It. cf. bübbolo *knot in reed'; Fris. popel *bulrush'; Latv. bubulis (2) ‘knot in yarn’
buburió ‘rumble, bubble, rattle’ Skt. (ambig.) buburah (^water'. Pref. to bubul- (1), q.v); WGer. poppern “bang”
bud- (1), budio “lip; lips, mouth’. WP II, 114 Gk. cf. bázen, Hes. buzón “close together’; cf. poppüzo (‘smack the lips’, fr. *bud-budio); Alb. buzë ‘lip’, substrate in Rum. buză, wd: Big. büza ‘cheek’, and cf. Pol. buzia (“little mouth’, fr. *boud-); also E to pout and Fr. bouder, and cf. Slovak bozk “kiss? (fr. *bu- diko-)
bud- (2), büdóo, ið ‘thrust, force’ Gk. büzo (1) ‘cram’; OE potian, beside pytan (*thrust': *bud-, büd-); E to put, Scots to putt; Du. poten ‘plant’; Icel. pota ‘thrust’; Sw. putta ‘thrust, plug’; Norw. putte, id. Con- nexions uncertain for Ger. ab-putzen ‘to tick off and for LG putt-jung 'errand-boy'
bud- (3) (onomat.) "a hooting bird” Gk. cf. búzō (2) "boot: OE pytt-el ‘hawk, kite); EME puttock (2) *buzzard' or ‘kite’; Li. cf. budutis, čio ‘hoopoe’
bud- (4), budul- ‘knob, mushroom’ Arm. ptuy (o-st. ‘berry, fruit’), Cz. bedla, Pol. bedła ‘parasol mushroom’; Li. cf. budis, f. budele, id. (also bude). (?) Sw. putt ‘boy’
buduló, ið, budur, ið ‘rummage, delve’ Arm. ptrem; E potter, US putter; LG cf. . pótern *poke'; Du. peuteren “poke, rummage' (ü); Sw. cf. pottra ‘simmer’; Norw. putre, id. ` (ü) Latv. budulu, et “be busy”, budulis 'pot- terer’
budhos (?). Cf. busd- (buzd-) Gk. buthós; OE pudd ‘ditch’. Cf. E pod ‘pod, cocoon, eelnet'
büg- (7) ‘swelling’. Cf. bugol-, buĝil- OE pocc �
```


## [2026-09-05T06:22:58.027Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==48{print}' IEC.txt"
}
```


### [2026-09-05T06:22:59.855Z] TOOL RESULT

```
 and SI. forms with sim. onomat. content |
buzd-, see busd- and bzd-
bzdàlos, ios ‘stinking object”. Cf. bzdið and busd-, buzd- Gk. cf. ki-bdelos ‘filthy’; Li. cf. ku-bizdalis, io *puffball'. Cf. also possibly Gk. bdéllion “an aromatic gum”
bzdió, bzdēið (buzd-, burzd-) “break wind, buzz, hum’. WP II, 68 Per. vazidan “far; Arm. (*bh- in) bzzem “buzz? Gk. bdéo; cf. also kí-bdos (fdross', a cpd.); bdüllo ‘cause a stench’; LLat. (?) *burdo ‘drone’; Sw. prutta ‘to fart beside prutt, s. (metath. via *purt-); R bzdét, Pol. bzdziec, Cz. bzdít “fart”, beside Cz. bat ‘hum’, exten- sions in Pol. bzyczeC, Cz. bzičet (hum, fr. *bzeukijo?). The simplex occurs in Cz. bzed ‘fart’, bzdy ‘arse’, and in Cz. bez, Pol. bez, bezd, Srb. báza “elder; Lith. dial. bizdas *arse; bustle'. A variant occurs in Srb. bazd- jeti ‘stink: Bis büzdja; Li. bürzdu, det ‘bustle, rumble’; LG pusten ‘puff’, Pust ‘gust’ all from a type *busd- or *bursd- (the Slav forms ambig.). Lith. forms in bezd- are LWs from Polish (AB). Gk. psóa 'stink' is a doubt- ful relative
59
bha, bho — bhàginos
60
Bh
bha, bho ‘indeed’. WP II, 136. See next Skt. (Vedic) cf. bha-la; Per. ba-li ‘yes; Arm. ba (cj. ‘that, adv. ‘yes’. *a or *à); Olr. ba (an interrogative particle); Go. (infix) -ba- P; OCS bo (cj. *for); Li. cf. ar-ba ‘or’; bei indeed”
bhå ‘indeed’. Cf. bha, bho. WP II, 123 & 136 Av. bà; Oss. ba “but, yet; Arm. (ambig.) ba ('that'; *yes); Gk. phë; Cz. Pol. Ukr. ba
bhabos, à ‘berry, bean’. WP II, 131 Lat. faba; OCS bobü; OPr. babo; Finn. LW papu “bean, pea'
bhābhā, on ‘tassel, thrum’ Ir. bábán (2); Blg. baba (2), id.
Gk. paphlázo ‘well up’. Mod. also ‘bubble, pur?; Du. babbelen: Ger. babbeln
bhàbhos, à, ün, ios ‘child, baby’. Cf. bāb- (The Celt. & SI. forms ambig.) Ir. báb *baby, girl’; bábán (1) ‘baby’; Celtic LW in It. bab- báno ‘booby’; MHG buobe ‘boy’; Du. boef *knave'; Sw. bov, id.; ON bófi, id.; OCz. bábé ‘little girl, dol, baban ‘young man wedded to older woman’; Cz. cf. bábenec ‘youngster’. Cf. WP II, 105-7
bhadh-, bhadhn- ‘hollow, trough, bed’ Gk. páthne, phátne ‘trough, crib’; Go. badi (and comm. Germ.) ‘bed’; Finn. LW patja ‘mattress’; doubtfully also Lycian făzi ‘tomb’
bhādh- ‘hurt, sicken, repel, nauseate’. Cf. WP II, 130. Cf. bhedh-, bhodh- Skt. (ambig.) badhe ‘repel, harry’; badháh ‘tormentor’; bādhā ‘pain’; Gk. péthō ‘suffer’ is isophonic, but EB and JBH otherwise; Br. cf. bæz ‘dunce’; W boddi, 3s. bawdd ‘drown’ is isophonic, but uncertainly fr. *bhādh-; Li. bostu, inf. bosti, pf. bodau ‘tire, bore; be tired, be bored’; bodùs ‘nauseating’. (The Skt. mp. bibhadse "am sickened' in- dicates *bh- and *-dh-)
15
20
25
30
35
40
bhag-, bhāg- ‘enjoy; enjoyment’. WP II, 127 (à) Skt. bhajami “award; experience; enjoy; possess; bhagah “possession, luck’; bhágah “lord of the gods’; Av. bagom ‘share’, bayo ‘god’; Iran. LW in Arm. bag (i-st. share);
. Phryg. cf. bagaios ‘Zeus’; Gk. éphagon (aor.
İsg. ʻate’; -phagos (cpds.; LW in Arm. bagin, bagni, -av ‘idol’ is apparently isophonic with Lat. faenum (‘usury’, fr. *bhaginom?); OCS (and comm. SL.) bogü “god”, beside bog-atü ‘rich’; Cz. also ne-bohý, u-bohy ‘poor’; Srb. cf. z-bog, adverb "Tor the sake of: Latv. na- bags ‘poor’. Cf. -baig- in Olr. su-baig-idir (3s. dep. ‘he rejoices’). See next, and cf. bhag-
bhāg- (1) (variant of bhag-, q.v.). WP II, 127 Skt. bhagáh (Cshare'. Vedic: luck); Av. baya ‘part’; OPer. bàji- ‘tribute’; Per. bat id.; Tokh. A pàk, B pàke “part'; Olr. bág “sake, benefit’; MIr. bá (loss of -g as in brí, tí, rí); S
```


## [2026-09-05T06:23:09.325Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==53{print}' IEC.txt"
}
```


### [2026-09-05T06:23:10.835Z] TOOL RESULT

```
 ‘stupor’; Br. bad ‘stunning’ beside bada, badawi "be stunned"; Cor. cf. badüs, badæs moonstruck'; Cz. (a) cf. bat'ula ‘dunce’
bhask — bháu-
15
20
25
30
35
40
45
68
bhaudó, ið (1) “beat, chastise’. WP II, 127 & 147 Br. cf. bæz ‘stick, cosh’; OHG bozzan, Ger. bossen, MHG bo3en, sv. 7 “beat”, beside Ger. bauzen (“weep'. Semantics of Lat. plango): OE beatan, pt. beot, id.; ON bauta, id. Cf. MHG ane-bo; ‘anvil’; Li. baudziu, bausti ‘punish’. Cf. Arm. bawt, i, iv, ‘bad news” from *bhaustis `
bhaudó, io (2) 'fire, burn' | Gk. phaüzo “fry, roast, broil”; LG båuten, pt. bódd, pp. bótt ‘make fire”
bhaul- “puff, swel’ (?) Cf. phaul-, bhoul-. The evidence is ambig. Gk. cf. phaülos; phaulízo ‘trivial; make light of (cf. phaul-); Go. (ambig.) uf-bauljan “puff up’; Slovene bula ‘swelling, tumour’; OCz. búle, Cz. boule ‘swelling’; Pol. dim. bulka ‘blister’
bhaum- (noun-element of root bhàu, & cf. bhaio, bhami, etc.) OE béam ‘beam of light; bieme uml. 'trum- pet; Latv. baumas, fpl. “gossip”
bhaus- “violent, dashing, boisterous; bang, beat, din’ Arm. cf. (variant) z-bawsank ‘amusement’, z-bawsnum (‘amuse os, fr. *bhauK-); Fris. boas "lively, eager; (of weather) bad: OHG bosi ‘paltry, bad'; bosa ‘badness’; Du. boos “angry, malignant, evil’; Nynorsk (archaic Nor- wegian) baus ‘stalwart’; Cz. cf. vý-buch, Ukr. vy-bux ‘explosion’. Verbal types include: Arm. (variant) z-bawsnum ‘amuse oneself; MHG besen ‘do evil; Cz. bušiti ‘hammer’; Big. bùša ‘punch’ beside bùxam ‘flog’. Cf. also ON beysta ‘thresh’; Big. buxtjà ‘dash, roar’
bhåu- (1) ‘shine, show; tell’. Cf. bhaio, bhāmi Arm. cf. ham-bav (o-st. ‘report, news’, fr. *som-bhau-); Gk. pháos, n. and phós (fr. *bhauos, and -es-stem) beside pháo, pháuo light, v.; cf. phanós ‘bright’ and piphaüsko ‘show’; OE bywan ‘polish, decorate’; cf. MHG bou- in bouchen ('sign', fr. *bhau- + *gn-, see ĝn-, &nósKo, w. sim. formation to MHG zei-chen, see dai- ‘divide’), OE beacen ‘beacon’; cf. Icel. bákn “monster”
bhàu- (2) “press, oppress’. Cf. bhou-
69
OHG bouuen, id.; OCS za-bavljo, -baviti "ot, fend”, za-bava “difficulty”
bhäu- (3) (?) Cf. bhóu (1) and bhəu- Lat. cf. favissae 'Ilumber-rooms, basements’; Arm. cf. baviy (a-st.) ‘cavern, labyrinth’. If to Lat. favus, see bhəu- (MHG bou, Du bouw *etructure")
bhauos, see bhàu- (1) and bhouos, bhou-, bhü-
bhebhrinos “of beaver’. See bhebhros, us. II, 167 Lat. fibrinus; Ligurian (in Rumansh place- names) Beverin; OHG bibirin; Li. bébrinis, io
bhebhrio ‘tremble’. Cf. WP I, 849 Lat. febrio, ire (“have fever’. Simplex in febris “fever”, cf. also Febris ‘goddess of fear or danger); G. dial bebbern, bebern, LG bewern; Du. bibberen ‘shiver’
bhebhros, us ‘red-brown; beaver’. WP II, 167 Sk. babhrüh; Av. bavris; Lat. fiber; Gallo-Lat. beber, acc. bebrum; (whence It. bévero, Fr. biévre); cf. also Gaul. Bibr-acte (Autun); Ligur. Bevers (place-name); Rum. substr. breb (Dacian wd. cf. Rum. plop ‘poplar’ for me- tath.); Ir. Bibar (name); OHG bibar, bibur; OE befer; beofor; ON bjórr; OCS bebrü, bobrü; Slovene breber, bober; Li. bébras, bébrus; Latv. bebrs, bebris. (Variants occur in Slovene daber and in Lith. vebras)
bhedo, ið ‘dig, stab, bury’. Cf. WP II, 188, and see bhod- Hitt. pedahi, bedahi ‘dig’; Thrac. cf. béssa (valley, fr. *bhedio); Gk. cf. s-phedanós ‘thrusting, eager, violent’; Ir. cf. beadhán, m. ‘sting’; OBr. cf.
```


## [2026-09-05T06:23:15.408Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==54{print}' IEC.txt"
}
```


### [2026-09-05T06:23:17.052Z] TOOL RESULT

```
bed, W bedd ‘tomb’; Br. béz, id.; Cor. bedhy (denom. “bury'); Li. bedü, bèsti ‘thrust, stab’; Lat. bedu, best “dig”, beside bedre ‘ditch, grave’. (O-grade in Lat. fodio, Gre, and OCS bodo, bosti 'stab")
bheg- ‘break, pierce’ Skt. bhagnah ‘broken’; Arm. bek, id., bekem, bekanem ‘break’. (MHG bichen, bicken ‘stab’, bic, gs. bickes ‘stab; cut’; OE cf. becca ‘pick, mattock’: G Bicke preferably from bhig-, q. v.)
bhëguð ‘chase; run’. WP H, 248 Skt. cf. bhajak ‘quickly’; Gk. (ë) phébomai; OCS běžọ, ati; Li. begu, bēgti; Latv. bëgu, t
bhegh-iKs (-əK) “outside, without, except".
bháu- — bheidho
10
20
25
30
35
40
45
70
WP II, 137. See next Skt. bahís, bahís, bahí$ "out, away, except’; Arm. bac, bajc "but. baci ‘except’; Per. baguz, id., OW cf. bei, W bai ‘defect, oni bai ‘except’; OCS (and comm. SI.) bezü ‘without’; Latv. bez, id.
bhegh- (variant of bhe&h-, see bhe&h-iKs) Skt. bahyah, adj. ‘outside’; Per. bàz "open: Tokh. A cf. pakür, B pākri *'openly'; ON (CO) bagr ‘chary, awkward"; bagi *opponent , bægi- (*athwart', in cpds.). See next
bhégho, ið ‘oust’ (?). Cf. bhe&h-iKs, bhegh- Gk. cf. synth. cpd. ptésso, pf. éptekha ('scare',
„ fr. *d(e)-bhegho); OHG bàagan, MHG bàgen,
sv. 7 “strive; shriek; boast; quarrel’; cf. OHG baga ‘battle’; MHG bàc, bàges ‘shriek, din, quarrel, boasting' & Ger. Bager 'restlessness, haste’; bágern ‘badger, nag’; ON bægja ‘oust, thwart, quarrel, force” |
bheid- (bhid-) ‘cut, bite’, WP II, 138. Vedic bhédami, pp. bhittáh, bhinnáb; Lat. cf. fid (CI split, pf.); Ir. cf. béadan, bíodan, *backbiter'; béim, pl. -eanna, inf. ‘cut, blow? (fr. *bheidmn-); Go. beitan Chute" and comm. Gmc.); OE bitan “bite; cut; dash down’; (1) bita ‘wild animal; bite “bite, sting, cut’; OCS cf. o-biZdo, -bidéti ‘offend’
bheidh- (bheidhtis, bheistis, tio) “stability; pledge; faith". WP II, 139 Gk. (Hom.) peisa ((peace' or “confidence. Context: ‘his heart rested in —; Daco-Moe- sian -beista (in the name Bura-beista, partly glossed in Gk. Aria-peithes); Lat. cf. fid- ücia beside (1) in fides (but fidus); Alb. besé *pledge, trust; Gaul. cf. bessu (queried: *cus- tom); Olr. béss, id.; Br. boaz, pl. boasiu, id. (Note: some Greek examples containing peis- derive from a root bhendh-, q.v.). Cf. bhoidh-
bheidho (1) (bhindh-, bhidh-) ‘urge, per- suade, offer, promise'. WP II, 139. Cf. bheidh- above Gk. peítho, adj. pithanós; Lat. fido, Gre: Alb. cf. bind ‘persuade’; Ir. cf. béin (tcompulsion', fr. *bheidhnis)
bheidhó (2) "be become, wait Oss. bedun, pp. bidt “take place; be apparent'; OE bidan, MHG biten ‘dally, wait’; ON bíða, id.
71 bheldhó, ið — bherdho
bheldhó, ið ‘knock, rattle’. Cf. bhldh- Lat. (ambig.) bilbo, ére, & bilbio, ire (“bubble from a bottle’. Assimilated consonants as in barba, see bhardh-); Icel. *bjáld- (name) be- side (o-grade) baldinn ‘unruly’; Li. béldZiu, bélsti & bedlü, Eti, v. “knock, bang! beside (o-grade) baldà ‘din, ado’; baldüs ‘rugged’: Go. balp- OHG bald, etc. Parallel form: Latv. belZu, belzt, as Lith. WP II, 184
bhelegh- (bhelugh-) (?) (a furry animal) Sk. bhaluhah ‘dog’; Lat. cf. (?) feles ‘weasel’ or *marten'; W bele *marten'; Gallo-Lat. LW in Fr. belette, id. (dim.); OHG cf. (Alem.) pilih, MHG bilch (*dormouse', said to be fr. Sl. plükhü, see FK: Bilchmaus). (Lat. feles is ambig. see dhel-)
bhelenos (bhelnos) ‘henbane’. WP IT, 180 Gaul. belénion (variant: belen-ountiam. Gal- lo-Lat: bellinotem, bellonaria); Sp. LW be- leño; W bela; MLG billen; OE belene, beolone and belune; R belenà; Pol.
```


## [2026-09-05T06:23:47.370Z] TOOL CALL #23: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T06:23:47.379Z] TOOL RESULT

```


```


## [2026-09-05T06:23:49.250Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt; echo \"=== grep juz in HRN\"; grep -n -i \"juz\\|ǧuz\\|gûz\" HRN.txt | head -20; echo \"=== HUB\"; grep -n -i \"juz\\|bali\\|balê\" HUB.txt | head -20"
}
```


### [2026-09-05T06:23:49.303Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
=== grep juz in HRN
3625:nebüved der keläm-i tu juz edl
3669:juz medh-^ fU terhencU büved Iierci nüvesem
3914:juz (d. i. jiiS ez).
20074:! vavijuz 159.
=== HUB
733:sivend. bdi Arm', baiband (? fur baliband) 'Armband
1737:zd. yaozaiti wogt, wallt', bal. juzay 'to move', arm.
4612:ap. ^bardah" = zd. barezah^^) *H5he', phi. sup. balist, zd.
4615:balis *Kissen, phi. balisn Gl. and Ind. 76, zd. barezis; phi.
5386:hdX.juzay *to move', also =: a^^.^yauz-? ; yovaz, yavaz *Panther'
5649:Abalish I, 3 u. s. w.), nirgends mit v^), so dass die Gleichung
5660:64, 8 ; Spiegel, trad. Litt. p. 389 ; Barthelemy, Gujastak Abalish
6376:H. 167; bak Turcht H, 170; baU *hoch* H. 171; balis
8456:Shk. 257 = np. mahist (siehe oben) = ap. madista- ; balist
9311:phi. sup. balist := zd. barezista-; phi. sup. x^alist am
9313:'schmecken' H. 500; balis 'Kissen', zd. barezis-; phi. baltn
```


## [2026-09-05T06:23:53.592Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3900,3930p' HRN.txt"
}
```


### [2026-09-05T06:23:53.631Z] TOOL RESULT

```
Dann müsste die Grundbedeutung Verzehren* sein.
') Nicht *Gefä88*, wie ich ZDMG. 43, 48 übersetzt habe.
*) Reimt auf umed (Vis und Rämln, Seite 85 Vers 3 v. u.).
») Fr. Müll er 's Lesung .^ar^rmw (WZKM. 5, 380J ist unmöglich.— 94 -
416. Jäh 'Würde, Stellung.
ap. ^ya&a-, vergl. ai. yä^a- f Gang)*.
Hörn, KZ. 32, 586 No. 21.
417. JäT, ja 'Ort*, Jmgah, vergl. an]jiä, Tn\ja, h,i]jä.
g. yä, yäga; Käs. yö (durchgängig), yögö.
7aM l/"yÄ- gehen' ebenso wie goh zu X/'gä' gehen*
(Hörn, KZ. 32, 586 No. 21); päz. /a? bezw. ya%
(PPGL).
LW. kurd, //; afy. /äe; bei. /<^, jaga (112).
418. Jtidä getrennt; juU (AM.), /wd (AM.), 1U (Is. 3, 41),
juz (d. i. jiiS ez).
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
```


## [2026-09-05T06:23:55.542Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2",
 "prompt": "Give the full Persian etymology sections for باز, especially the one meaning \"open\" and the one meaning \"back, again\" — what Middle Persian, Old/Proto-Iranian and PIE forms are given? Quote the etymology text verbatim."
}
```


### [2026-09-05T06:24:03.535Z] TOOL RESULT

```
# Persian Etymology for باز

## Etymology 1 (Meaning "Open")

The entry states: "Perhaps related to Etymology 2." It notes that a relation to بختن (boxtan, "to save, liberate") seems "more semantically tenable," but the actual etymological derivation is incomplete.

## Etymology 2 (Meaning "Back, Again")

The documented ancestry proceeds as follows:

"Inherited from Middle Persian [Book Pahlavi needed] (LAWHL /⁠abāz⁠/, 'back, again, re-'), [Book Pahlavi needed] (ʾp̄ʾc), Manichaean Middle Persian 𐫀𐫁𐫀𐫝 (ʾbʾc), from Proto-Iranian *apāča- ('back'), derived from Proto-Iranian *apānk- ('behind'), from Proto-Iranian *Hápa ('off, away'), from Proto-Indo-Iranian *Hápa ('off, away')."

An alternative, less likely etymology proposes: "from Proto-Indo-European *bʰe (instrumental particle) + *-ǵʰs ('out'), cognate with Sanskrit बहिस् (bahis, 'out, aside from')."
```


## [2026-09-05T06:24:13.524Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%B2",
 "prompt": "Give the Persian etymology section for جز (joz/juz) \"except, other than\" verbatim — what Middle Persian and Avestan/Proto-Iranian forms are given? Also note any separate Arabic entry."
}
```


## [2026-09-05T06:24:14.787Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%87",
 "prompt": "Give the Persian etymology for بله (bale) \"yes\" verbatim. Is it derived from Arabic بلى (balā)? Quote the etymology."
}
```


### [2026-09-05T06:24:18.410Z] TOOL RESULT

```
# Persian Etymology for جز (joz/juz) "except"

The Persian Etymology 1 section states: "From Middle Persian [Term?] (/⁠jud az⁠/, 'except, apart from')."

The entry indicates the Middle Persian form as "jud az" but marks it with "[Term?]", suggesting the specific term reference is uncertain or missing from the source documentation. No Avestan or Proto-Iranian forms are provided in the etymology section.

## Arabic Entry

The page contains a separate **Arabic section** documenting جَزَّ (jazza) as a Form I verb meaning "to shear, to prune, to cut down, to fleece" and related meanings. This is etymologically distinct from the Persian preposition.
```


### [2026-09-05T06:24:18.990Z] TOOL RESULT

```
# Persian Etymology for بله (bale)

Based on the Wiktionary content provided, **no etymology is given for the Persian word بله (bale)**. 

The page only states that بله is "Iranian standard form of بلی (balē / bali, 'yes')" but does not explain the origin or derivation of this word. There is no mention of whether it derives from Arabic بلى (balā) or any other source language.

The etymological information is simply absent from this dictionary entry.
```


## [2026-09-05T06:24:22.106Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%84%DB%8C",
 "prompt": "Give the Persian etymology for بلی (balē/balī) \"yes\" verbatim. Is it from Arabic بلى? What does it say?"
}
```


## [2026-09-05T06:24:23.373Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%80",
 "prompt": "Give the Persian etymology for the verbal prefix بـ (be-/bi-) verbatim — what Middle Persian form is given and what is its origin?"
}
```


### [2026-09-05T06:24:26.380Z] TOOL RESULT

```
# Persian Etymology of بلی

According to the Wiktionary entry, the Persian word بلی (balē/balī) meaning "yes" comes from Arabic. Specifically, the etymology section states:

"Borrowed from Arabic _[بَلَى](/wiki/%D8%A8%D9%84%D9%89#Arabic "بلى")_ (balā)."

Yes, it is indeed derived from the Arabic word بَلَى (balā), with a note that Classical Persian underwent a vowel change in this borrowing, similar to other Arabic loanwords in Persian.
```


### [2026-09-05T06:24:28.526Z] TOOL RESULT

```
# Persian Etymology for بـ (be-/bi-)

According to the Wiktionary entry, the verbal prefix derives from **Middle Persian bʾ** (pronounced /⁠bē⁠/, meaning "out, away, forth"), which ultimately traces back to **Proto-Indo-European *bʰe**.

The article notes that in Classical Persian, this prefix carried "diverse and generally vague meanings depending on the context," eventually becoming grammaticalized as a subjunctive marker through a historical process involving the displacement of the simple present tense.
```


## [2026-09-05T06:24:40.291Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%80#Persian",
 "prompt": "Quote the full Persian etymology paragraph for the prefix بـ (be-) exactly as written, including any links/glosses for the Proto-Indo-European form *bʰe (what gloss is given for it?)."
}
```


## [2026-09-05T06:24:40.658Z] TOOL CALL #32: WebSearch

```json
{
 "query": "Wiktionary Middle Persian bē \"out, away\" Proto-Indo-European *bʰe outside etymology"
}
```


### [2026-09-05T06:24:44.702Z] TOOL RESULT

```
# Persian Etymology of بـ (be-)

Based on the Wiktionary page, here's the etymology paragraph for the prefix:

"From Middle Persian (bʾ /⁠bē⁠/, 'out, away, forth', also preverbal particle of unclear additional meanings), ultimately from Proto-Indo-European *bʰe."

The gloss provided for the Proto-Indo-European form *bʰe is not explicitly stated on this page. The entry only notes that it derives "ultimately from Proto-Indo-European *bʰe" without offering a specific meaning for that root form itself.
```


### [2026-09-05T06:24:48.500Z] TOOL RESULT

```
Web search results for query: "Wiktionary Middle Persian bē "out, away" Proto-Indo-European *bʰe outside etymology"

Links: [{"title":"بـ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%D9%80"},{"title":"Reconstruction:Proto-Indo-European/bʰewg- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0ewg-"},{"title":"بیـ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%80"},{"title":"بی - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%DB%8C"},{"title":"Category:Persian terms by Proto-Indo-European root - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Persian_terms_by_Proto-Indo-European_root"},{"title":"Category:Persian terms derived from the Proto-Indo-European root *bʰeh₂- (speak) - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Persian_terms_derived_from_the_Proto-Indo-European_root_*b%CA%B0eh%E2%82%82-_(speak)"},{"title":"Category:Persian terms derived from Proto-Indo-European - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Persian_terms_derived_from_Proto-Indo-European"},{"title":"Reconstruction:Proto-Indo-European/bʰey- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0ey-"},{"title":"Persian vocabulary","url":"https://en.wikipedia.org/wiki/Persian_vocabulary"},{"title":"Reconstruction:Proto-Indo-European/bʰebʰówdʰe - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eb%CA%B0%C3%B3wd%CA%B0e"}]

Based on the search results, I found the etymology information you were looking for on Wiktionary:

Middle Persian bē (meaning "out, away, forth" as a preverbal particle) ultimately derives from Proto-Indo-European *bʰe.

The search also revealed related etymologies: A similar but distinct Persian prefix bī ("without") comes from earlier abê, derived from Middle Persian apē, which traces back to Proto-Indo-European *h₂epó ("off, away").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T06:25:01.012Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AC%E0%A4%B9%E0%A4%BF%E0%A4%B8%E0%A5%8D",
 "prompt": "Give the Sanskrit entry for बहिस् (bahis): meaning and etymology (what PIE root, what cognates?). Quote verbatim."
}
```


## [2026-09-05T06:25:01.692Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bench",
 "prompt": "Give the etymology of \"bench\" verbatim, including the Proto-Germanic form and any PIE root mentioned. Also any note connecting it to bank."
}
```


### [2026-09-05T06:25:06.267Z] TOOL RESULT

```
# Sanskrit Entry: बहिस् (bahis)

**Meaning:** The adverb बहिस् denotes "out, forth, outwards, outside" and can mean "out of, apart from, except, beside" when used with ablative or at the start of compounds.

**Etymology:** According to the source, this term probably derives from Proto-Indo-European *bʰeǵʰ- ("outside"), formed from *bʰe (instrumental particle) + *-ǵʰs ("out"). 

**Cognates:** The document lists these related words: "Proto-Slavic *bez, Lithuanian bè, Latvian bez, Old Prussian bhe."
```


### [2026-09-05T06:25:08.378Z] TOOL RESULT

```
# Etymology of "Bench"

**Noun Origin:**
From Middle English *bench*, from Old English *benc* meaning "long seat," derived from Proto-Germanic *\*bankon*. The page notes this group is "cognate with bank (n.2) 'natural earthen incline beside a body of water,' and perhaps the original notion is 'man-made earthwork used as a seat.'"

**Verb Origin:**
The sporting sense "to take out of a (baseball) game" dates to 1902, derived from the noun's reference to where reserve players sit during games.

**Connection to Bank:**
Both *bench* and *bank* trace to Proto-Germanic *\*bankon*, suggesting they share a common root related to earthen constructions or slopes used as seats.

**Note on PIE roots:**
While the document discusses related words like *shambles* and *shamble*, which connect to Latin roots and a PIE root *\*skmbh-* meaning "to prop up, support," these are not explicitly linked to *bench* itself in the primary entry.
```


## [2026-09-05T06:25:21.740Z] TOOL CALL #35: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2' --note 'page 83, root Bhe/Bhegh, node #2: Persian باز bāz \"open\"/\"back\" etymology; Wiktionary derives from MP abāz < PIr *apāča- and calls the *bʰe+*-ǵʰs derivation \"less likely\"' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AC%D8%B2' --note 'page 83, node #3 bejoz: Persian جز from Middle Persian jud az \"except, apart from\"' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%84%DB%8C' --note 'page 83, entry 1 node #4: Persian بلی balē borrowed from Arabic بَلَى balā' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%80' --note 'page 83, entry 1 node #4: Persian verbal prefix بـ be- from Middle Persian bē \"out, away, forth\", ultimately PIE *bʰe' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%AC%E0%A4%B9%E0%A4%BF%E0%A4%B8%E0%A5%8D' --note 'page 83, node #4: Sanskrit bahis \"out, outside, except\" from PIE *bʰeǵʰ-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/bench' --note 'page 83, node #7: English bench < OE benc < PGmc *bankon, cognate with bank n.2' 2>&1 | tail -3"
}
```


## [2026-09-05T06:25:24.340Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb && pdftoppm -f 83 -l 83 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg83 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T06:25:25.609Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2347a7eacc81d31c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/922ad2368e42dff9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c9cfddcc517072c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77862998ff3a3587.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4e7083716254ea42.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/67326ae4947abd91.txt
```


### [2026-09-05T06:25:27.171Z] TOOL RESULT

```
Exit code 1
I/O Error: Couldn't open file 'EtymologicalDictionary-persian-english.pdf': No such file or directory.
```


## [2026-09-05T06:25:29.309Z] TOOL CALL #37: Bash

```json
{
 "command": "ls *.pdf 2>/dev/null; ls site/pages/83.jpg 2>/dev/null; find . -maxdepth 2 -iname \"*.pdf\" 2>/dev/null | head"
}
```


### [2026-09-05T06:25:29.371Z] TOOL RESULT

```
EtymologicalDictionary-persian-english.pdf
site/pages/83.jpg
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-05T06:25:32.464Z] TOOL CALL #38: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 83 -l 83 -r 220 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf $S/pg83 && ls -la $S/"
}
```


### [2026-09-05T06:25:34.595Z] TOOL RESULT

```
total 10072
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 02:25 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb  189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb    5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb   79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb  108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb  155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb   58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82358 Sep  5 02:23 pg84.png
```


## [2026-09-05T06:25:37.803Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg83.png"
}
```


### [2026-09-05T06:25:38.206Z] TOOL RESULT

```

```


## [2026-09-05T06:25:38.204Z] INPUT

[Image: original 1870x2420, displayed at 1545x2000. Multiply coordinates by 1.21 to map to original image.]


## [2026-09-05T06:25:53.593Z] TOOL CALL #40: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 83 -l 83 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf $S/pg83_600 && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg83_600.png'); print(im.size)\nw,h=im.size\n# node #4 area approx y 480/2420*h .. 530/2420*h ; x 370/1870*w .. 600/1870*w\nim.crop((int(0.19*w),int(0.19*h),int(0.36*w),int(0.225*h))).save('$S/pg83_bohyah.png')\n\"; ls -la $S/pg83_bohyah.png"
}
```


### [2026-09-05T06:25:57.544Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 1466 Sep  5 02:25 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg83_bohyah.png
```


## [2026-09-05T06:26:03.068Z] TOOL CALL #41: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg83_600.png')\nim.crop((1150,1450,2100,1800)).save('$S/pg83_bohyah.png')\nim.crop((1050,950,4000,1300)).save('$S/pg83_apac.png')\n\"; ls -la $S/pg83_bohyah.png $S/pg83_apac.png"
}
```


### [2026-09-05T06:26:07.576Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 7123 Sep  5 02:26 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb 4363 Sep  5 02:26 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg83_bohyah.png
```


## [2026-09-05T06:26:09.792Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg83_bohyah.png"
}
```


### [2026-09-05T06:26:09.808Z] TOOL RESULT

```

```


## [2026-09-05T06:26:17.313Z] TOOL CALL #43: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg83.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/83.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-05T06:26:17.392Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  59439 Sep  5 02:13 79.png
-rw-rw-r-- 1 sfmqrb sfmqrb  58953 Sep  5 02:13 80.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99904 Sep  5 02:17 81.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74477 Sep  5 02:22 82.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67094 Sep  5 02:26 83.png
```


## [2026-09-05T06:26:19.184Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 MON_part1.txt; echo; echo \"--- formfeeds:\"; python3 -c \"\nd=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('len',len(d),'pages',d.count('\\f'))\nd2=open('MON_part2.txt',encoding='utf-8',errors='replace').read()\nprint('len2',len(d2),'pages2',d2.count('\\f'))\n\""
}
```


### [2026-09-05T06:26:20.778Z] TOOL RESULT

```
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی 
--- formfeeds:
len 2611770 pages 0
len2 2568024 pages2 0
```


## [2026-09-05T06:26:26.887Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A8%D9%84%D9%87",
 "prompt": "What does Mo'in's dictionary (فرهنگ معین) say for بله? Give the entry text and any origin tag such as [ع.] (Arabic) or [په.] (Pahlavi)."
}
```


## [2026-09-05T06:26:28.310Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%84%D9%87/",
 "prompt": "Give the فرهنگ معین (Mo'in) section for بله, including any bracketed origin tag like [ع.] or [په.]. Also give the دهخدا entry if present."
}
```


### [2026-09-05T06:26:30.894Z] TOOL RESULT

```
According to Mo'in's dictionary entry shown above, the word "بله" is defined as:

"(بَ لِ) (ق .) آری ، بلی"

This indicates the word means "yes" or "indeed" (آری ، بلی). The notation "(ق .)" appears to mark it as a common or standard term, though no specific language origin tag like [ع.] (Arabic) or [په.] (Pahlavi) is provided in this dictionary entry.
```


### [2026-09-05T06:26:35.729Z] TOOL RESULT

```
# فرهنگ معین Entry for بله

According to the **فرهنگ معین** section:

**(بَ لِ) (ق.) آری، بلی.**
**(بُ لْ) [ع.] (اِ.) ابله، کم خردان.**

The first entry marks بله (with fatha on ب and kasra on ل) as synonymous with "yes/affirmative" and notes it derives from classical sources (ق.). The second entry indicates بله (with damma on ب and sukun on ل) as an Arabic loanword [ع.] meaning "foolish" or "simple-minded."

# دهخدا Entry

The **لغت نامه دهخدا** provides extensive documentation, beginning with: "محرف بلی در تداول فارسی" (a corrupted form of بلی in Persian usage), tracing its etymology and listing multiple semantic categories including affirmation, imperative actions, and intellectual deficiency.
```


## [2026-09-05T06:26:40.728Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%84%DB%8C/",
 "prompt": "Give the فرهنگ معین (Mo'in) entry for بلی, including any bracketed origin tag like [ع.] (Arabic). Also give the دهخدا etymology note if present."
}
```


## [2026-09-05T06:26:41.325Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D8%AC%D8%B2/",
 "prompt": "Give the فرهنگ معین (Mo'in) entry for بجز, including any bracketed origin tag. Also the دهخدا entry."
}
```


### [2026-09-05T06:26:47.132Z] TOOL RESULT

```
# بلی - Mo'in Dictionary Entry

**Farhang-e Mo'in (فرهنگ معین):**

The entry states: "(بَ) (ق.) بله، آری" and "(بِ لا) [ع.] (اِمص.) کهنگی، آوارگی"

This shows two forms with different pronunciations and origins:
- The first (with fatha on ba) means "yes" or "indeed" 
- The second (with kasra on ba, marked [ع.] for Arabic origin) means "antiquity" or "vagrancy"

**Dehkhoda Etymology Note:**

Dehkhoda indicates the word originally derives from Arabic "بل" (bal), with the final alif added "to make silence upon it sound proper, since if it were just 'bal,' the listener would await further speech."

The note traces the Persian usage as a response to negated questions, distinct from the Arabic "نعم" (na'am), which functions differently in grammatical contexts.
```


### [2026-09-05T06:26:47.564Z] TOOL RESULT

```
# Dictionary Entries for بجز

## Dehkhoda Entry
The Dehkhoda dictionary provides this definition: "بجز. [ ب ِ جُ ] (composite letter) (from: ب + جز) meaning 'without' or 'except.' It functions as an exception word meaning 'other than' or 'save.'" The entry includes classical Persian poetry examples from Ferdowsi and Nizami illustrating its usage.

## Mo'in Entry
The Mo'in dictionary entry is not separately detailed in this webpage content. However, the page references "فرهنگ معین" (Mo'in Dictionary) as one of its sources but does not provide a distinct Mo'in entry for this word.

The page does indicate that بجز carries meanings equivalent to English terms like "except," "save," and "apart from," with Persian equivalents including مگر، جدا از، and غیر از.
```


## [2026-09-05T06:27:01.279Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 baz\"; grep -n \"apāč\\|apāc\\|apac\\|bāz\\|Bāz\" BQT_v1_pages.txt | head -20; echo \"=== ARY latin index\"; grep -n -i \"BAZ\\|APAC\\|BALE\\|JOZ\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-05T06:27:01.340Z] TOOL RESULT

```
=== BQT v1 baz
=== ARY latin index
22:Pe UI Sly (Gley WUE o> IEE) ated ork bales!
793:Bla WLS LY 5b Baz He oly
794:Bale Se Soul (by Erp) 999, S30 ast b5 4s yy F skal
1215:KAUFEN ofly b gest wag tn oss See col lal BH ale Bales
2367:sabale raplalped 52 ajly gal eae
2962:POKORNY =SO~*~S~*~«s BAZA, BAL PAHLAVI) 5
2967:(OLD PERSIAN) jjhoel go 3h, BAZU, BAZAUSH,(AVESTAN) gl!
2968:BAZUSH, BASAUSH, BAZU- BAZAU-
2971:BUOG, BOGR BAZA (PAHLAVI) 5 34,
2976:BRECH _ NBRETON) 3.3. BES, BAZUK ARMENIAN) gh
3043:BALESHT AFGHAND) () gil BAREZISH s(AVESTAN) gis 9\
3045:BARHISH, BARISHN BALESHT, BALIN
3047:BALGS GOTHIC) Si BAZ AOSSETIC) ga)
3133:BRO, BRYGGA (SWEDISH) Sat y= BAZU AVESTAN) gl)
3651:VAAGE DANISH) Sails ‘WUZURG, BAZURG (PAHLAVI) (5 4,
4085:BAZEN (BOHEMIAN) san » BIM, BIMGEN, (PAHLAVI) 5 shy
15002:HVAL DANISH) ila BALEINE (alt) (FRENCH) il
15022:tot Aeglis PHALAINA gt 505}p b"Jty" ashy Se So jl gg Corb ot Als BALEINE aii 5
```


## [2026-09-05T06:27:06.409Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2955,2980p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== page tag\"; awk 'NR<=2962 && /\\[pdf page/{p=$0} END{print p}' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-05T06:27:08.176Z] TOOL RESULT

```
; BU gall 2 Soll om
oT SBF SUDL; 22 a5 cal em
eel AS ta 8 O85 22 059 atl om
ap ab A AS cellos 22 05a al ome
gt wot gli 9 yey Bao 225s ce om
\or
‘REFERENCES beuhy VAL AVESTAN) gts!
POKORNY =SO~*~S~*~«s BAZA, BAL PAHLAVI) 5
BUCK: 18 RHASAS. (SANSKRIT) <4 Suite .
ry sbi oly PHENE ca NOREEN) gh ae
te
[aes yr ei |
(OLD PERSIAN) jjhoel go 3h, BAZU, BAZAUSH,(AVESTAN) gl!
BAZUSH, BASAUSH, BAZU- BAZAU-
[pdf page 105]
sibel |e
BUOG, BOGR BAZA (PAHLAVI) 5 34,
BOGR HOLD NORSE) op ge POKE ——_(TOKHARIAN A) A «3 js
BUOG (OLD HIGH GERMAN) apf lt PAUK, POKE :(TOKHARIAN B) B 5,55
ve BUG > “ GERMAN) st BHU, SANSKRIT) 24 Suse
BOG (OLD ENGLISH) oy pnts! BAHUH, BAHUS
BRECH _ NBRETON) 3.3. BES, BAZUK ARMENIAN) gh
PEKBUS (GREEK) 3b y
‘REFERENCES ety BRACCHIUM (4L}(LATIN) 3
POKORNY ===~~S*~*~*~*~*~«é BRAS (QU FRENCH) wil
‘MACKENZIE: 102 BRAZD (uLEY(SPANISH) colslyl
=== page tag
[pdf page 104]
```


## [2026-09-05T06:27:18.782Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 quality\"; grep -c \"\" BQT_v1_pages.txt; grep -n \"باز\" BQT_v1_pages.txt | head -5; echo \"=== BRT ba particle\"; grep -n \"bāḍa\\|baḍa\\|bōiṭ\\|boit\\|bāδa\" BRT.txt | head -10; echo \"=== SYN bench\"; grep -n -i \"bench\\b\" SYN.txt | head -10"
}
```


### [2026-09-05T06:27:18.859Z] TOOL RESULT

```
=== BQT v1 quality
32486
157:ششصد واندی واژه ( غیرمکرر ) بکار رفته است. امید است باز باین سره‌ایه
193:باریارمته وارشامه از شهریاران‌فارس بازخو انده‌شود » ایرادی نیست‌جز اینکه
227:فارس ی کنو نی باشد . اماجای‌شادمانی است که بازيك
268:باز گروه انبوهی در ايران وهند پیرو اوستا ماندند »رشته پیو ند [نان باژبان
288:ساسانیان در دست داشتند ‏ فقط چپاريك آن بما رسیده » بازسندبز رگی است»
=== BRT ba particle
30319:.   ^  1   •     .    '    ^    i   L  ■.,      ■.  Pu.!    huboitum,   (in  V.  2.  z8)   erL:    ngon  pul
=== SYN bench
1195:ON bakki ‘riverbank’, but also ‘bank’ in general, as ME banke (fr. ON), NE bank : OHG banch, OE benc ‘bench,’ etc. perh. Skt. bhanj- ‘break.’ NED s.v. bank, sb.1. Falk-Torp 43. Walde-P. 2.148.
12089:6. Lith. lova : Lith. lava, Russ. lava ‘bench’, perh. ON 1éfi ‘threshing floor’, orig. a ‘piece of board’, fr. *leu- in Skt. lunati ‘cuts off’? Walde-P. 2.407. Berneker 695. ’
12117:3. Rum. scaun, fr. Lat. Scamnym, ‘bench, stool’ (> NG cKapyl ‘stool’) : Skt. skabh- ‘prop, support’, sb, skambha. ‘post, prop’. Walde-P. 2.539 Ernout- M. 901.
12854:Russ. lava ‘bench’, Lith. lova ‘bedstead’, etc., with dub. root connection. Walde P. 2.407. Falk-Torp 650.
19771:nea, with similar f pune D ce languages, were bor- other ae word bank ‘bench’ seen G bank, OF benc, NE were often applied to a a ter’ for the display of wares, that of the moneychangers Jar words for ‘bank’ and dto the rest of Europe It was the fem. form ommonly prevailed in this hanca, Fr. banque, etc. ; but ef, also Sp. banco, Lith. bankas vs. Lett. ianka, Pol., Russ. bank vs. SCr., Boh. hanka. NED s.v. bank, sb. 3. Wartburg 1.235 ff. 4. One cannot, of course, expect to find words for ‘bank’ in the early period
21039:‘bench’, Pol. fawa ‘bench, stand, stall in ° a market’, etc. Berneker 695.
32553:1. Grk. ceXis, -idos, used as an archi- tectural term for ‘cross-piece’, also ‘block of seats’, ‘rowing-bench’, etc. (beside cé\pa ‘deck, rowing-bench, scaffold’, etc.), was applied to the column of a papyrus roll (mot necessarily identical with the sheet of papyrus, the writing in column sometimes crossing the juncture of the sheets; cf. also xo\Ajpara se, ceAl- Ses pdf ‘95 sheets, 187 columns’, Riv. fil. 37.361), and later to the ‘page’ of codices. Hence NG cedida ‘page’.
```


## [2026-09-05T06:27:22.430Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 p136-137\"; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd2_pages.txt | head -3; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\[pdf page (\\d+)\\]',t)\nprint('nchunks',len(pages))\n# find chunk containing 'bhe-ĝh' or 'bahis'\nfor i in range(1,len(pages),2):\n    n=pages[i]; body=pages[i+1]\n    if 'bahis' in body or 'bahíṣ' in body or 'bez' in body.lower()[:4000] and 'ohne' in body:\n        print('=== pdf page',n, body[:300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T06:27:24.292Z] TOOL RESULT

```
=== WLD Bd2 p136-137
nchunks 1
```


## [2026-09-05T06:27:35.097Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 outside\"; grep -n -i \"bahis\\|bahih\\|bahíṣ\\|außerhalb, ohne\\|bhe-ĝh\\|bheĝh\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20; echo \"=== WLD band3 register\"; grep -n -i \"bahis\\|bahih\" WLD_band3.txt | head -10"
}
```


### [2026-09-05T06:27:35.160Z] TOOL RESULT

```
=== WLD Bd2 outside
=== WLD band3 register
```


## [2026-09-05T06:27:35.856Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT fürwahr\"; grep -n -i \"fürwahr\" BRT.txt | head -20"
}
```


### [2026-09-05T06:27:35.906Z] TOOL RESULT

```
=== BRT fürwahr
7741:•  j.  9r«zvo  Adv."  'wahrlich,  fürwahr'; 1)  an  der  Spitze  des  Satzteils,  vor  Vok.: fr°  asäum  spitama  ^7vam  da^at  ahurB maidä  Yt.  5.  89;  91,  95,  12.3,  13.  i,  Ij. 31.  2)  hinter  dem  Wort,  das  hervor- gehoben werden  soll;  a)  hinter  dem  Pron. pers.:  yat  tum  hs  uzsayatjha  tum  3r° zarahultra  Y.g.13;  —  aez'alia  bä  zara- 'i^ustra  ya>a  tum  jf  vasanhe  V.5. 17; z\;  —  paiti  »lam  if  ptnsat^uha  yim ahursm  mazäam  V. /^.  7,  b)  sonst: mazilt»n  ..vispanqm  tr"  sravaahamYi^N. 4.1;  —  daliiqm  »r'  yaozdaii-Xta  a^a  zX. . asti  yaozdäili^  .  .  havaya  ir'  dasnaya  V. la.  1 9.
7784:'fürwahr  es  werden  an  dir  vorbei  die  vom I  Mund  triefenden  Speisen  getragen  (wer- den)" V.^.29.
17075:•  j.  baäa  Fart  i)  der  Beteuerung,  am  Satz- anfang 'fürwahr':  b'  ila  aEni  6)n%i  (sd,) V.J.a?;  37,  39',  Yt-ÄS,  5.127,  F.ji?,Vyt 35^  3^-  3)  "^^^  Hervorhebung,  meist hinter  dem  ersten  Wort  des  Satz(teii)es"; a)  hinter  dem  Verbum:  lunti  b'  mavayacit cdkwars  arsäna  "sunt  profecto  mihi  etiam quattuor  mares"  V.  Jt^.  31.  b)  hinter dem  Relativ:_>'?  b'  ustanazastu gpnzaite  Yt 10.  53;  73;  —  ya%ra  b°  Y.  10.  7';  — yas» %wä  b'  fräyazäile  Y.  62.  i ;  — y!}  nS  b°  frä- yasäite  Yt y - S 2 ;  —  yas>  leb' .. baxsaite  Y. io,  13; — yim  vIsS  vTspaitis  b''^^  ustänazastö sbayeiti  Yt  10.  83;  84-86*''.  c)  sonst; avi  i'  fratmsaiti  Yt  iQ.  134;  134';  — alca  hl  b'  kammo^m  jaynvä  ..'^•Sy. 10; — yat  dim  dämSi^  upamanS  huirixttm  b° irinaxti  Yt/0.  68;  —  tal  i^aranS  b°  asti N.  30  ".  Ohne  Wert :  Vyt  5^,  Yt  2. 1 1 , Vd.  20.
```


## [2026-09-05T06:27:42.229Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Beteuerung\" BRT.txt | head -20"
}
```


### [2026-09-05T06:27:42.274Z] TOOL RESULT

```
6742:•  j.  ahe  Part,  der  Beteuerung  'fUrwahr, wirklich';  a'  framraomt  spitama  xlayad . . "fQrwahr  ich  sage,  o  Sp.: . ."  FrW,  4.2;  — tarn  a°  Vyt  22",  25;  —  mqnaym  (Stverz.)
17075:•  j.  baäa  Fart  i)  der  Beteuerung,  am  Satz- anfang 'fürwahr':  b'  ila  aEni  6)n%i  (sd,) V.J.a?;  37,  39',  Yt-ÄS,  5.127,  F.ji?,Vyt 35^  3^-  3)  "^^^  Hervorhebung,  meist hinter  dem  ersten  Wort  des  Satz(teii)es"; a)  hinter  dem  Verbum:  lunti  b'  mavayacit cdkwars  arsäna  "sunt  profecto  mihi  etiam quattuor  mares"  V.  Jt^.  31.  b)  hinter dem  Relativ:_>'?  b'  ustanazastu gpnzaite  Yt 10.  53;  73;  —  ya%ra  b°  Y.  10.  7';  — yas» %wä  b'  fräyazäile  Y.  62.  i ;  — y!}  nS  b°  frä- yasäite  Yt y - S 2 ;  —  yas>  leb' .. baxsaite  Y. io,  13; — yim  vIsS  vTspaitis  b''^^  ustänazastö sbayeiti  Yt  10.  83;  84-86*''.  c)  sonst; avi  i'  fratmsaiti  Yt  iQ.  134;  134';  — alca  hl  b'  kammo^m  jaynvä  ..'^•Sy. 10; — yat  dim  dämSi^  upamanS  huirixttm  b° irinaxti  Yt/0.  68;  —  tal  i^aranS  b°  asti N.  30  ".  Ohne  Wert :  Vyt  5^,  Yt  2. 1 1 , Vd.  20.
17235:•  j.  böit  Part,  der  Beteuerung  und  Her- vorhebung, hinter  dem  ersten  Wort  im Satz;  a)  hinter Nom. :  nanm  b°  alavamm.. V. y.  22;  —  iuinm  b'  yäsamHi  x''annö ..  dayata  Ny.j.  ii-  b)  hinter  dem Pron.:  aztm  böit  ..  tä  nipayemi  Ytj.Sg.
21153:tritt attributiv  eine  Form  des  lat  qualis, uzw.  insofern  das  Substantiv,  das  man im  Hauptsatz  erwarten  sollte,  in  den  ^•- Satz  gezogen  ist  (vgl.  Sp.  1204  m.);  b)  im gAw.  r  al  va  vXsp^ng  äySiy  ratüm  akurd vacdä  .  .  qsayä  (sd.)  ".  .  (talis)  qualem arbilium  Ahuras  novit  sva.  (talis)  arbiter qualem  . ."  \.JI.2.  c)imjAw.:  nari k)hrpa  .  .  taoa  ayaol  y'  paoirim  virfm avi  yü  bavaiti  "hominis  corpore  . .  adeo adulti  (corpore)  qualem  . .  virum  . .  sva. .  .  adeo  adulti  (corpore)  viri  qualem  .  ." Yt. -i'.  14;  14'.  X)_v*imStnn  vonquan- tum;  c)  im  jAw.:  y  taoa  pagirim  kan- dar3za{s^.)  altat  paiti  nidai^Ua  V.Ä76; 77  t*.  XI)  y  in  der  Beteuerung  sva, 'so  wahr  als';  c)  im  jAw.:  dätam  tl tatiuye  ifarmB .  .y  imal  yat  tl  fravaoHm sva,   ". .  so  wali  ich  dir  das  sage"  Yt.
```


## [2026-09-05T06:29:07.806Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B2/",
 "prompt": "Give the فرهنگ معین (Mo'in) entries for باز, including any bracketed origin tags like [په.] (Pahlavi) or [ع.]. Especially the sense \"open\" (گشوده) and \"back, again\"."
}
```


## [2026-09-05T06:29:08.977Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%89",
 "prompt": "Give the Arabic entry بَلَى (balā): meaning, part of speech, and etymology. Also list descendants (e.g. Persian)."
}
```


### [2026-09-05T06:29:15.788Z] TOOL RESULT

```
# Arabic Entry: بَلَى (balā)

**Meaning:** Used to contradict a negative statement, equivalent to "yes" or "yes, I have" in English.

**Part of Speech:** Adverb

**Etymology:** Listed as "Etymology 1" in the entry, with pronunciation /ba.laː/

**Notable Descendants:**

The entry documents extensive linguistic influence across multiple language families:

- **Persian variants:** Classical Persian بَلی (balē), Iranian Persian بَلِه (bale)
- **Turkic languages:** Azerbaijani bəli, Ottoman Turkish بلی (bali), Turkish beli
- **Semitic dialects:** South Levantine Arabic مبلا (mbala), Maltese mela
- **Indo-Aryan:** Urdu بَلے (bale), Hindi बले (bale)
- **Kurdish varieties:** Central, Northern Kurdish, and Zazaki forms
- **Other languages:** Pashto بلې (bále), Chagatai-derived Uyghur and Uzbek forms

The word appears in Qur'anic quotations (2:260 and 34:3) dating to 609–632 CE, illustrating its classical Arabic roots and religious significance.
```


### [2026-09-05T06:29:15.921Z] TOOL RESULT

```
# Farhang-e Mo'in Entries for باز

Based on the dictionary content provided, here are the relevant Mo'in entries:

**"Open" sense (گشوده):**
"[ص.] گشاد، گشوده" — Listed as an adjective meaning "open, spread out."

**"Back/Again" sense:**
"[په.] ۱ - پسوندی که به آخر برخی واژه ها افزوده می شود و معنای «تا این زمان » را می دهد مانند: از دیرباز. ۲ - بر سر افعال درآید به معنی دوباره ، از نو"

This indicates a suffix [په.] (Pahlavi origin) meaning "until now" when appended to words, or "again/anew" when preceding verbs, with examples like بازگشتن and بازیافتن.

The dictionary also notes the chemistry sense as "[ع.]" (Arabic origin) and provides the unit of measurement definition separately.
```


## [2026-09-05T06:29:23.250Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AD%E0%A4%B2",
 "prompt": "Is there a Sanskrit entry भल (bhala)? Give its meaning and part of speech (is it a Vedic particle meaning \"indeed/certainly\"?) and any etymology."
}
```


### [2026-09-05T06:29:25.088Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T06:29:26.504Z] TOOL CALL #59: Bash

```json
{
 "command": "for u in 'https://abadis.ir/fatofa/%D8%A8%D9%84%D9%87/' 'https://abadis.ir/fatofa/%D8%A8%D9%84%DB%8C/' 'https://abadis.ir/fatofa/%D8%A8%D8%AC%D8%B2/' 'https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B2/' 'https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%89'; do python3 tools/fetch_source.py \"$u\" --note 'page 83: Mo3in/Dehkhoda/Wiktionary lookups for باز، بجز، بله، بلی، Arabic بلى' 2>&1 | tail -1; done"
}
```


### [2026-09-05T06:29:34.755Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/715f350229418b81.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/584928e60983ff2d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8237726790dcab2b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c2c11b87300594fb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f431f399c3272711.txt
```


## [2026-09-05T06:29:40.716Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.sanskritdictionary.com/?q=bhala",
 "prompt": "What do Monier-Williams and other dictionaries give for Sanskrit \"bhala\"? Quote the definitions verbatim."
}
```


### [2026-09-05T06:29:44.270Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T06:29:46.161Z] TOOL CALL #61: WebSearch

```json
{
 "query": "Sanskrit \"bhala\" Vedic particle Monier-Williams \"indeed\" khalu"
}
```


### [2026-09-05T06:29:53.348Z] TOOL RESULT

```
Web search results for query: "Sanskrit "bhala" Vedic particle Monier-Williams "indeed" khalu"

Links: [{"title":"खलु - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A4%96%E0%A4%B2%E0%A5%81"},{"title":"Monier-Williams: A Sanskrit-English Dictionary (1872)","url":"https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse72_u.htm"},{"title":"Monier-Williams","url":"http://buddhism-dict.net/ddb/monier-williams/mw-02.html"},{"title":"Amarakosha Search - Sanskrit Dictionary","url":"https://sanskritdictionary.com/?action=Search&iencoding=slp1&lang=sans&q=Kalu"},{"title":"Search - Sanskrit Dictionary","url":"https://sanskritdictionary.com/?q=khalu"},{"title":"Monier Monier-Williams","url":"https://en.wikipedia.org/wiki/Monier_Monier-Williams"},{"title":"A Sanskrit English Dictionary : Monier-williams, Monier, Sir : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/in.ernet.dli.2015.31959"},{"title":"Monier-Williams Sanskrit English Dictionary Page 0498","url":"http://www.ibiblio.org/sripedia/ebooks/mw/0400/mw__0498.html"},{"title":"Monier Williams - Sanskrit-English Dictionary 1872 | PDF","url":"https://www.scribd.com/document/321388649/Monier-Williams-Sanskrit-English-Dictionary-1872"}]

Based on the search results, here's what I found related to your query about Sanskrit particles:

Regarding **khalu**: Monier Williams (1899) documents "khalu" in A Sanskrit–English Dictionary at page 338, column 2. The particle is rarely used alone at the beginning of an expression and often combined with other particles like atha, and it can be merely expletive.

The search results also reference **bhala** in connection with Monier-Williams entries, though the specific entry for "bhala" as a Vedic particle meaning "indeed" wasn't directly detailed in the results. However, the Monier-Williams dictionary cross-references "bhala" in relation to other entries.

The results indicate that both terms appear in Monier-Williams' Sanskrit-English Dictionary, which is a fundamental reference work for Sanskrit lexicography. If you need more specific information about the exact definitions and usage of "bhala," you may want to consult the Monier-Williams dictionary directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T06:29:57.703Z] TOOL CALL #62: WebFetch

```json
{
 "url": "http://www.ibiblio.org/sripedia/ebooks/mw/0700/mw__0748.html",
 "prompt": "Does this Monier-Williams page contain an entry for \"bhala\"? If so quote it verbatim. List the headwords on the page."
}
```


### [2026-09-05T06:30:01.390Z] TOOL RESULT

```
Based on the content provided, I cannot determine whether this page contains an entry for "bhala" or identify specific headwords. The page content shows only navigation elements and a reference to an image file, with no actual dictionary text visible. To answer your question accurately, I would need the actual content of the dictionary page itself.
```


## [2026-09-05T06:30:07.914Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL --max-time 120 'https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse72_u.htm' -o mw1872.htm && ls -la mw1872.htm && grep -o -i \"bhala[^<]\\{0,200\\}\" mw1872.htm | head -10"
}
```


### [2026-09-05T06:30:22.324Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
bhala
bhala, as
bhalagna
bhala
bhalakṣaṇa
bhalakṣaṇa
bhalambhana
bhala, jambīra
bhala
bhala
```


## [2026-09-05T06:30:25.660Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'EOF'\nimport re,html\nd=open('mw1872.htm',encoding='utf-8',errors='replace').read()\nt=re.sub(r'<[^>]+>',' ',d)\nt=html.unescape(t)\nfor m in re.finditer(r'bhala\\b',t):\n    s=t[max(0,m.start()-120):m.start()+300].replace('\\n',' ')\n    print('---',' '.join(s.split()))\nEOF"
}
```


### [2026-09-05T06:30:27.789Z] TOOL RESULT

```
--- . ku ), N. of a Daitya, a younger brother of Jambha and son of Prahrāda or Prahlāda, a son of Hiraṇya-kaśipu. kujambhala kujambhala, as , m. a thief who breaks into a house; also kujambhira and kujam-bhila ; [cf. kumbhila .] kujjiśa kujjiśa or kujjhiśa, as , m. a sort of fish; [cf. kuḍiśa .] kujjhaṭi kujjhaṭi, is or ī , or kujjhaṭikā , f. a fog or mist. kuñc kuñc , cl. 1. P. kuñcat
--- f a Daitya, a younger brother of Jambha and son of Prahrāda or Prahlāda, a son of Hiraṇya-kaśipu. kujambhala kujambhala, as , m. a thief who breaks into a house; also kujambhira and kujam-bhila ; [cf. kumbhila .] kujjiśa kujjiśa or kujjhiśa, as , m. a sort of fish; [cf. kuḍiśa .] kujjhaṭi kujjhaṭi, is or ī , or kujjhaṭikā , f. a fog or mist. kuñc kuñc , cl. 1. P. kuñcati, cukuñca, k
--- a river. kulambhara kulam-bhara, as, ā, am , carrying or upholding a family; ( as ), m. a wrong form for kujambhala , a thief. kulayoṣit kula-yoṣit, t , f. a woman of noble family; a virtuous high-born woman. kularakṣaka kula-rakṣaka, as, ā, am , preserving a family. kularatnamālikā kula-ratna-mālikā , f. title of a work. kulavat kula-vat, ān, atī, at , belonging to a nob
--- f Hiraṇya-kaśipu; N. of the father-in-law of Hiraṇyakaśipu; N. of the father of Sunda; the citron tree, = jambhīra, jambhala, jambīra ; eating, food; biting asunder, opening by biting, explanation, interpretation; a quiver; a part, a portion; ( ā ), f. opening of the mouth; [cf. antar-jambha, ku-j-, tapur-j-, tigma-j-, tṛṣṭa-j- , &c.; cf. also Gr. [greek]] jambhakuṇḍa jambha-kuṇḍa, am , n., N. of a Tīrtha.
--- il with small leaves, a kind of Ocimum, = maruvaka or prastha-puṣpa; (am) , n. a citron; [cf. jam-bhīra, jambha, jambhala .] jambīraka jambīraka, as , m. a kind of Ocimum. jambu jambu, us , or jambū, ūs , f. (said to be fr. rt. 1. jam ), a fruit tree, the rose apple, Eugenia Jambolana, or another species of Eugenia; ( ūs, u ), f. n. its fruit; ( us, u ), m. n., N. of a Dvīpa [cf. jambu-dvīpa ]; N.
--- ana . See under 1. and 2. jabh . jambhara jambhara, as , m. the lime or citron tree; [cf. the following.] jambhala jambhala, as , m. the lime or citron tree [cf. jambīra ]; N. of a Jina or deified Jaina saint; N. of a man; ( ā ), f. a female Rākṣasī, by meditating on whom women become pregnant. jambhaladatta jambhala-datta, as , m., N. of the supposed author of the Vetāla-pañca-viṃśati. jam
--- nder 1. and 2. jabh . jambhara jambhara, as , m. the lime or citron tree; [cf. the following.] jambhala jambhala, as , m. the lime or citron tree [cf. jambīra ]; N. of a Jina or deified Jaina saint; N. of a man; ( ā ), f. a female Rākṣasī, by meditating on whom women become pregnant. jambhaladatta jambhala-datta, as , m., N. of the supposed author of the Vetāla-pañca-viṃśati. jambhin jamb
--- saint; N. of a man; ( ā ), f. a female Rākṣasī, by meditating on whom women become pregnant. jambhaladatta jambhala-datta, as , m., N. of the supposed author of the Vetāla-pañca-viṃśati. jambhin jambhin, ī , m. the lime or citron tree. jambhīra jambhīra, as , m. the lime or citron tree, apparently of more than one species; a plant considered to be a kind of basil with small leaves; [cf. jam-bīr
--- cl. 10. A. bhālayate, bālayate , &c., Ved. to describe; to see, behold; to throw up (?); [cf. ni-bh-, sam-bh- .] bhala 1. bhala , ind., Ved. certainly; [cf. bal, baṭ , and Marāṭhī bhalla , 'well!'] bhala 2. bhala, as , m. a term used in addressing the Sun. bhalatā bha-latā , f. See under 4. bha . bhalandana bhalandana, as , m., N. of a man; of the father of Vatsa-prī or Vatsa-prīti; (ās)
--- bhālayate, bālayate , &c., Ved. to describe; to see, behold; to throw up (?); [cf. ni-bh-, sam-bh- .] bhala 1. bhala , ind., Ved. certainly; [cf. bal, baṭ , and Marāṭhī bhalla , 'well!'] bhala 2. bhala, as , m. a term used in addressing the Sun. bhalatā bha-latā , f. See under 4. bha . bhalandana bhalandana, as , m., N. of a man; of the father of Vatsa-prī or Vatsa-prīti; (ās), m. pl. th
--- f. ni-bh-, sam-bh- .] bhala 1. bhala , ind., Ved. certainly; [cf. bal, baṭ , and Marāṭhī bhalla , 'well!'] bhala 2. bhala, as , m. a term used in addressing the Sun. bhalatā bha-latā , f. See under 4. bha . bhalandana bhalandana, as , m., N. of a man; of the father of Vatsa-prī or Vatsa-prīti; (ās), m. pl. the descendants of Bhalandana; [cf. bhālandana, bhālandanaka, bhanandana .] bha
--- sam-bh- .] bhala 1. bhala , ind., Ved. certainly; [cf. bal, baṭ , and Marāṭhī bhalla , 'well!'] bhala 2. bhala, as , m. a term used in addressing the Sun. bhalatā bha-latā , f. See under 4. bha . bhalandana bhalandana, as , m., N. of a man; of the father of Vatsa-prī or Vatsa-prīti; (ās), m. pl. the descendants of Bhalandana; [cf. bhālandana, bhālandanaka, bhanandana .] bhalānas bha
--- bhālla, bhālleya ]; ( as, ā, am ), propitious, favourable ( = bhadra, śiva ); a term used in addressing the Sun (= 2. bhala , q. v.). bhallapucchī bhalla-pucchī , f. 'bear's tail', N. of the plant Hedysarum Lagopodioides. bhallākṣa bhal-lākṣa (-la-ak-), as , m., Ved. an expression used in addressing a flamingo ( = bhadrākṣa , q. v.). bhallaka bhallaka, as , m. = bhalla , a bear. bhallāt
--- om honey, sugar-candy; the earth; ( am ), n. beeswax. madhujambīra madhu-jambīra, madhu-jambha , or ma-dhu-jambhala, as , m. a kind of citron. madhujāta madhu-jāta, as, ā, am , 'honey-born', sprung or produced from honey. madhujit madhu-jit, t , m. 'conqueror of the Daitya Madhu', an epithet of Viṣṇu. madhujihva madhu-jihva, as, ā, am , Ved. 'honey-tongued, sweet-tongued' (said of
--- ables told by a Vetāla to king Vikramāditya (of which there are three recensions extant, two by Śiva-dāsa and one by Jambhala-bhaṭṭa; versions of these popular tales exist in Hindī and almost every Hindū vernacular, as well as in Tamil and Telugu, and translations in other languages are also current). vetālapañcaviṃśatikathā vetāla-pañcaviṃśati-kathā , f., N. of part of the Vṛhat-kathā. vettṛ 1. vettṛ,
--- bhā ), a happy man [cf. śam-bhu ]; Indra's thunderbolt; the iron-bound head of a pestle; [cf. śaṃva, śamba .] śambhala śambhala (perhaps connected with 2. śam ), N. of a town situated between the Rathaprā and Ganges (identified by some with Sumbhul in Moradabad; the town or district of Śambhala is fabled to be the place where Kalkī, the last incarnation of Viṣṇu, is to appear in the family of a Brāhman nam
--- appy man [cf. śam-bhu ]; Indra's thunderbolt; the iron-bound head of a pestle; [cf. śaṃva, śamba .] śambhala śambhala (perhaps connected with 2. śam ), N. of a town situated between the Rathaprā and Ganges (identified by some with Sumbhul in Moradabad; the town or district of Śambhala is fabled to be the place where Kalkī, the last incarnation of Viṣṇu, is to appear in the family of a Brāhman named Viṣṇu-ya
--- town situated between the Rathaprā and Ganges (identified by some with Sumbhul in Moradabad; the town or district of Śambhala is fabled to be the place where Kalkī, the last incarnation of Viṣṇu, is to appear in the family of a Brāhman named Viṣṇu-yaśas); ( ī ), f. a procuress, bawd. śambhalagrāmamāhātmya śambhala-grāma-māhātmya or śambha-la-māhātmya, am , n. 'the glory of the town Śambhala', N. of a part
--- to appear in the family of a Brāhman named Viṣṇu-yaśas); ( ī ), f. a procuress, bawd. śambhalagrāmamāhātmya śambhala-grāma-māhātmya or śambha-la-māhātmya, am , n. 'the glory of the town Śambhala', N. of a part of the Skanda-Purāṇa (consisting of twenty-four chapters). śambhaleśvaraliṅga śambhaleśvara-liṅga (-la-īś-) , N. of a Liṅga. śambhu śam-bhu, śam-bhaviṣṭha , &c. See under 2. śam .
--- bawd. śambhalagrāmamāhātmya śambhala-grāma-māhātmya or śambha-la-māhātmya, am , n. 'the glory of the town Śambhala', N. of a part of the Skanda-Purāṇa (consisting of twenty-four chapters). śambhaleśvaraliṅga śambhaleśvara-liṅga (-la-īś-) , N. of a Liṅga. śambhu śam-bhu, śam-bhaviṣṭha , &c. See under 2. śam . śaya śaya, as, ā or ī, am (fr. rt. 1. śī ), lying down, asleep, sleeping;
--- sambhal sam-bhal , cl. 10. P. A. -bhālayati, -te, -yitum , to observe well, perceive, hear, see, behold. sambhala sambhala, as , m. (for sam-bhara ), Ved. one who brings together, one who arranges a marriage, a match-maker; a suitor, wooer; a procurer, pimp; ( ī ), f. a procuress, bawd, (also written śambhalī .) sambhava sam-bhava , &c. See under sam-bhū . sambhā sam-bhā , cl. 2. P. -bhā
--- l sam-bhal , cl. 10. P. A. -bhālayati, -te, -yitum , to observe well, perceive, hear, see, behold. sambhala sambhala, as , m. (for sam-bhara ), Ved. one who brings together, one who arranges a marriage, a match-maker; a suitor, wooer; a procurer, pimp; ( ī ), f. a procuress, bawd, (also written śambhalī .) sambhava sam-bhava , &c. See under sam-bhū . sambhā sam-bhā , cl. 2. P. -bhāti, -babhau
```


## [2026-09-05T06:30:42.694Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^bench\\|Bench, \" SKT.txt | head -5; grep -n -i \"bench\" SKT.txt | head -12"
}
```


### [2026-09-05T06:30:42.758Z] TOOL RESULT

```
1714:Bench.  (E.)     See  Bank.
17028:nblea.  (L,)  Orig.  stalU  on  which rn  expoBo  meat  for  ulc :  pi.  of U,  a  bench,  butcher'*  bench  or  stall.
22857:bench — bank  ^1  \.  bank  (S),!
1379:Bank  (i)>  a  mound  of  earth.    (£.)  U.^j bankt,  b^ukt    (Layamon,    >rlS,s)* bam  (nn authorised),    4*    G.  Du. bench;    Icel.  bakki  (for  banki\   a O.  H.  G.pan^A,  a  bank«  a  bench.    Doi btmA,
1385:^^  B  MBsD  bencfa  or  Ubie ;  dimin. ^Kvlif.  H.G.  6a$te,  a  bench.  Ublc.
1714:Bench.  (E.)     See  Bank.
11943:motmteb&nk.  a  qoacic  doctor.  (Ital. ~L.  ami  G.)  Lit.  one  who  motmts  a btmh,  to  proclaim  his  nostrums.  —  Ital. moniambanco,  a  mountebank ;  O.  Ital. monta  in  hanco^  the  same.-* Ital.  mon/are, to  mount;  in,  on;  bamo,  a  bench.  Here montai-e  is  Ihe  same  word  as  F.  monter,  to mount ;  xn  —  L.  w,  on  ;  and  tamo  is  from O.  H.  a  i>anc,  a  bench  ;  see  Bank  (a).
17028:nblea.  (L,)  Orig.  stalU  on  which rn  expoBo  meat  for  ulc :  pi.  of U,  a  bench,  butcher'*  bench  or  stall.
17029:Emil,  a  stool.  —  L.  scamtllum,  a Ic  bench  ;  allied  to  uamftum, :h,  itabdlum,  fooi-itool.  Orig. )rop;'  cf.  L.  stafus^  shaft,  stem, t.  <r«^wT«iK,  to  prop.  ^^SKAP.) S&e.  (E.)  A.S.  sceamu,  scamu.-\' Jflimtu  ;    Dan.  Sw.  xjham  ;   C-  scham.
17351:),  a  long  bench  with  a  high A.S.  ////,  a  scat.+Goth.  jf//j;
20018:I  (F  -  L. ;  with  JL  prtjix^  From and  O. F.  irair  (K.  trahir^,  to from  L.  traJert.  ^  The  prefix fo  coafa>ion  with  bewray. see  Jet  (i). ooal-wngfron.  car  on  rails, words  dram-road  and  /rum- as  early  as  k.tt.  1794;  we  even a  will  dated  1555  t.^urtees xxxnii.  37).  The  same  as i«,  shaft  Ota  can,  beam,  bar, ,  a  mtlk'bench  (orig.  a  \o^  of fram-rthtd  was  prob.  at  hrst a  rail-road  on  Ueepers.* m,  log,  stock  of  a  tree,  ai^o O.  i>we<l.  trAirif  trum.
22857:bench — bank  ^1  \.  bank  (S),!
```


## [2026-09-05T06:30:44.970Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse72_u.htm' --note 'page 83, entry 1 node #2: Monier-Williams 1872 s.v. \"bhala 1. bhala, ind., Ved. certainly\"' 2>&1 | tail -1; python3 tools/fetch_source.py 'https://www.etymonline.com/word/bank' --note 'page 83, node #7: English bank (money) < Italian banca < Germanic; bank (earthen) < ON bakki' 2>&1 | tail -1"
}
```


### [2026-09-05T06:30:50.211Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/11c3e8d78a7efef6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/56d370ffb0d59441.txt
```


## [2026-09-05T06:30:53.768Z] TOOL CALL #67: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T06:30:53.809Z] TOOL RESULT

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


## [2026-09-05T06:30:57.962Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-82.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False))\nprint(json.dumps(d['entries'][0],ensure_ascii=False)[:2500])\n\""
}
```


### [2026-09-05T06:30:59.823Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/home/sfmqrb/git/rishe/data/verification/page-82.json'
```


## [2026-09-05T06:31:02.468Z] TOOL CALL #69: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -40; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-66.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False))\nprint(json.dumps(d['entries'][0],ensure_ascii=False)[:1800])\n\""
}
```


### [2026-09-05T06:31:04.290Z] TOOL RESULT

```
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
{"pdf_page": 66, "book_page": 36, "verified_by": "claude-fable-5-1", "verified_on": "2026-09-04"}
{"entry": 0, "root": "A`.s.r", "verdict": "confirmed", "modern_form": "Arabic root ع ص ر ʿ-ṣ-r 'to press, squeeze (the juice out)'; West Semitic *ʿṣr 'to press, restrain, retain'", "note": "The root box is right on all three counts: the Arabic verb عَصَرَ ʿaṣara 'he pressed, squeezed' is real, the language label is right, and the gloss 'to squeeze (the juice out)' is almost word for word the gloss of the AHD Appendix of Semitic Roots ('ʿṣr — West Semitic, to press, restrain, retain … alizarin, probably from Arabic al-ʿuṣāra, the juice, from ʿaṣara, to squeeze'). Two refinements. (a) The root is not specifically Arabic but common West Semitic: AHD labels it West Semitic and Klein, s.v. alizari, compares Hebrew ʿātzar, Aramaic-Syriac ʿătzar 'he retained' — so 'Arabic' should read 'Arabic (West Semitic)'. (b) The derived noun is vocalised ʿuṣāra عُصَارَة by AHD and by Wiktionary, ʿaṣārah by Klein; Nourai follows Klein's a-vocalism ('a`sârah'), and since both variants are attested this is not an error, only a choice of source. The European branch of the chart (Sp. → Fr. → Eng. alizarin) is Klein's and AHD's account, but AHD hedges it with 'probably', Dozy explicitly declared the origin unknown, and Wiktionary/Webster's 1913 now prefer an Ottoman-Turkish route — see node #3.", "note_fa": "ریشهٔ «ع ص ر» به معنای «فشردن، آب چیزی را گرفتن» ریشه‌ای اصیل و درست است و برچسب زبانی و معنای آن در نمودار نورایی با آنچه پیوست ریشه‌های سامی فرهنگ American Heritage می‌آورد یکسان است؛ تنها نکته آن است که این ریشه ویژهٔ عربی نیست و سامی غربی است (کلاین هم عبری «عَصَر» به معنای «نگاه داشتن» را هم‌ریشهٔ آن می‌داند). گونهٔ اسمی آن در فرهنگ‌های امروزی عُصارة و در کلاین عَصارة ضبط شده و نورایی ضبط کلاین را برگزیده است؛ هر دو ضبط پذیرفتنی است و خطا نیست. شاخهٔ اروپایی این نمودار (اسپانیایی ← فرا
```


## [2026-09-05T06:32:34.677Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD jud\"; grep -n \"jud \\[\\|jud(\\|ywdt\\|jud az\\|jud-\" PHD.txt | head -10; echo \"=== PHD be BRA\"; grep -n \"BR'\\]\\|bē \\[BR\\|\\bbē\\b\" PHD.txt | head -10; echo \"=== PHD except\"; grep -n \"^except\\|except \" PHD.txt | head -5"
}
```


### [2026-09-05T06:32:34.755Z] TOOL RESULT

```
=== PHD jud
414:jawédan [LOLMN < А l-Imn; ywyt?n' | (P y'wyd?n, M Pyn), N ~] eternally, always. ~ag [-k! | (P -g), N ~a] eternal, perpetual. jawén [S£yn! | № jawin] made of barley. jeh [yh, yyh = Av. jahi-] the Whore, female arch-demon. fiw [суш!, yyw! = Av. fiwya-] (consecrated) milk. *jomā [ywm’y] together with; both. jorda [ywilt’y, 2k | (P yw?rd?w), J *jwrd?r] corn, grain. jo(y) [ywd, ywb! | N ~] stream, channel. Jóy-, -išn, v. Jadan. jud [ywdt' | M jwd] separate, different; anti-. ~ az [N juz] except, apart from. judàg [ywd? h! | N juda] separate, different. ~ih: separation, difference. Jūdan, jóy- [ywtn!, ywd- | M jwwdn, (jw-), (N jawruan)] chew; devour (daevic). „išn: eating (daevic). jud-|-bēš [ywdt bys] harmless, antidote. ~-dadestan [-D YN A] disagreeable, opposing. ~-déw [-ŠD YA) anti-demonic. ---này [-> d] a fathom (6 ft.). jud-ristag [yzodt lystk!] schismatic, heretic. ~th: heresy. Juy [усе | N ~] yoke. Jumbāģīh [ywmb’kyh] motion. jumbénidan, jumbén- [ywmbyn-yin'] (cause to) move. jumbidan, jumb- [ywmb-yin' | N ~] move. ~išn: motion, movement. jumbihistan, jumbīh- [ywmbyh-stn'] be moved. juttar [ywdtl | M jwtr] different, otherwise. --īh: opposite, reverse. Juwān [ywb?n! | (P ywn), N jawàn] young; a youth. ~th: youth. juxt [ywht! | (P ywxt), N juft!] pair, couple.
801:anti- jud- ; anti-demonic jud-déw.
803:antidote anēš, jud-bëš, pādzahr.
808:apart from fraz az, jud az.
1828:except bē . . . (enyā), jud az.
3530:schismatic jud-ristag; v. heretic.
3583:separate (a.) jud(āg).
5451:| gandag dóvs?r jūvišn judāgīh judāg judbēš jud-dādcstān! jud judnāy -Cnīdan 1 *lawīdan juttar
5457:judristag jud-déw!
=== PHD be BRA
256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
414:jawédan [LOLMN < А l-Imn; ywyt?n' | (P y'wyd?n, M Pyn), N ~] eternally, always. ~ag [-k! | (P -g), N ~a] eternal, perpetual. jawén [S£yn! | № jawin] made of barley. jeh [yh, yyh = Av. jahi-] the Whore, female arch-demon. fiw [суш!, yyw! = Av. fiwya-] (consecrated) milk. *jomā [ywm’y] together with; both. jorda [ywilt’y, 2k | (P yw?rd?w), J *jwrd?r] corn, grain. jo(y) [ywd, ywb! | N ~] stream, channel. Jóy-, -išn, v. Jadan. jud [ywdt' | M jwd] separate, different; anti-. ~ az [N juz] except, apart from. judàg [ywd? h! | N juda] separate, different. ~ih: separation, difference. Jūdan, jóy- [ywtn!, ywd- | M jwwdn, (jw-), (N jawruan)] chew; devour (daevic). „išn: eating (daevic). jud-|-bēš [ywdt bys] harmless, antidote. ~-dadestan [-D YN A] disagreeable, opposing. ~-déw [-ŠD YA) anti-demonic. ---này [-> d] a fathom (6 ft.). jud-ristag [yzodt lystk!] schismatic, heretic. ~th: heresy. Juy [усе | N ~] yoke. Jumbāģīh [ywmb’kyh] motion. jumbénidan, jumbén- [ywmbyn-yin'] (cause to) move. jumbidan, jumb- [ywmb-yin' | N ~] move. ~išn: motion, movement. jumbihistan, jumbīh- [ywmbyh-stn'] be moved. juttar [ywdtl | M jwtr] different, otherwise. --īh: opposite, reverse. Juwān [ywb?n! | (P ywn), N jawàn] young; a youth. ~th: youth. juxt [ywht! | (P ywxt), N juft!] pair, couple.
1125:but bē.
1465:cure bēšiz(ēn)-.
1828:except bē . . . (enyā), jud az.
2205:harm (n.) ak, anāgīh, azarm, bei, bēšišn, wizend, zyàn.
2232:heal bēšāz(ēn)-.
2233:healing (a.) bēšāz.
2234:healing (n.) bēšāz(ēn)išnīh.
2324:hostile bēšburdār.
=== PHD except
77:Verbs are quoted in the infinitive form, followed by the present stem, except when either of these is not certainly attested. Cross references are made where necessary.
95:1 In Bartholomaean transcription (Altiranisches Wörterbuch) except for а, B, w, replacing q, w, v respectively.
1828:except bē . . . (enyā), jud az.
```


## [2026-09-05T06:32:44.603Z] TOOL CALL #71: Bash

```json
{
 "command": "tail -14 /home/sfmqrb/git/rishe/data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('url'))\n\""
}
```


### [2026-09-05T06:32:46.045Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/fluo
https://en.wiktionary.org/wiki/folium
https://en.wiktionary.org/wiki/%CF%86%CF%8D%CE%BB%CE%BB%CE%BF%CE%BD
https://en.wiktionary.org/wiki/flos
https://abadis.ir/fatofa/%D9%81%D9%84%D9%88%D8%A6%D9%88%D8%B1/
https://abadis.ir/fatofa/%DA%A9%D9%84%D8%B1%D9%88%D9%81%DB%8C%D9%84/
https://www.ahdictionary.com/word/search.html?q=blister
https://abadis.ir/fatofa/%D8%A8%D9%84%D9%87/
https://abadis.ir/fatofa/%D8%A8%D9%84%DB%8C/
https://abadis.ir/fatofa/%D8%A8%D8%AC%D8%B2/
https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B2/
https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%89
https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse72_u.htm
https://www.etymonline.com/word/bank
```


## [2026-09-05T06:39:18.801Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk83.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_BAZ   = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2\"\nW_JOZ   = \"https://en.wiktionary.org/wiki/%D8%AC%D8%B2\"\nW_BALI  = \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%DB%8C\"\nW_BE    = \"https://en.wiktionary.org/wiki/%D8%A8%D9%80\"\nW_BAHIS = \"https://en.wiktionary.org/wiki/%E0%A4%AC%E0%A4%B9%E0%A4%BF%E0%A4%B8%E0%A5%8D\"\nW_BALA  = \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%89\"\nE_BENCH = \"https://www.etymonline.com/word/bench\"\nE_BANK  = \"https://www.etymonline.com/word/bank\"\nA_BAZ   = \"https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B2/\"\nA_BEJOZ = \"https://abadis.ir/fatofa/%D8%A8%D8%AC%D8%B2/\"\nA_BALEH = \"https://abadis.ir/fatofa/%D8%A8%D9%84%D9%87/\"\nA_BALI  = \"https://abadis.ir/fatofa/%D8%A8%D9%84%DB%8C/\"\nMW      = \"https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse72_u.htm\"\n\ndoc = {\n \"pdf_page\": 83,\n \"book_page\": 53,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Bhe, Bheğh\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *b(h)e / *b(h)eǵʰ-, *b(h)eǵʰ-s 'outside, besides, without, except' — Pokorny IEW 112-113 'I. b(h)e und b(h)eǵh … außer, außerhalb, ohne'; Mann IEC 69-70 'bheǵh-iḱs (-əḱ) outside, without, except'; Wiktionary analyses it as *bʰe (instrumental particle) + *-ǵʰs 'out'\",\n   \"note\": \"The root box is essentially right. Pokorny's entry on the page Nourai cites (IEW 112, running into 113) is headed 'I. b(h)e und b(h)eǵh … außer, außerhalb, ohne' and opens 'Ai. bahiḥ (-s) draußen, von außen, außerhalb von', continuing on p.113 with 'apr. bhe ohne, lit. bè ohne, lett. bez ohne, aksl. bez ohne'; Mann IEC 69-70 heads the same theme 'bheǵh-iḱs (-əḱ) outside, without, except. WP II, 137'. Both the language label (Indo-European) and the '-iks' extension (= Wiktionary's *-ǵʰs) are correct, and 'outside, excluding, except' is the standard gloss. Two caveats. (a) Pokorny writes the initial as b(h)-, i.e. he cannot decide between plain *b- and aspirated *bʰ-; Nourai's flat 'Bhe' hides that uncertainty. (b) The gloss 'open' in the first line has no support outside Mann, who reaches it only through the Persian word bāz (IEC 70 'bheǵh- (variant of bheǵh-) … Per. bāz open'); Pokorny, Wiktionary and the Slavic/Baltic evidence give only 'outside, without, except'. The real trouble on this chart is not the root but what is hung on it: the two Iranian nodes (bāz, bejoz) and the Germanic bank family all have better-established origins elsewhere — see nodes #1, #3, #5, #6.\",\n   \"note_fa\": \"جعبهٔ ریشه در بنیاد درست است: پوکورنی در همان صفحه‌ای که نورایی ارجاع می‌دهد (ص ۱۱۲–۱۱۳) مدخل «b(h)e و b(h)eǵh» را با معنای «بیرون، بیرونِ، بی‌، جز» آورده و سنسکریت bahiḥ، پروسی کهن bhe، لیتوانیایی bè، لتونیایی bez و اسلاوی کلیسایی کهن bez را ذیل آن نشانده است؛ مان نیز در فرهنگ تطبیقی هندواروپایی (ص ۶۹–۷۰) همین ستاک را «bheǵh-iḱs: بیرون، بی‌، جز» می‌نامد. دو نکته: نخست آنکه پوکورنی آغازهٔ واژه را b(h)- می‌نویسد، یعنی میان *b و *bʰ تردید دارد و نورایی این تردید را نشان نداده است؛ دوم آنکه معنای «باز، گشوده» در سطر نخست تنها بر پایهٔ واژهٔ فارسی «باز» و به پیروی از مان افزوده شده و در پوکورنی و ویکی‌واژه نیامده است. اشکال اصلی این نمودار در خودِ ریشه نیست، بلکه در گره‌هایی است که به آن آویخته شده‌اند: «باز»، «بجز» و خانوادهٔ ژرمنی bank ریشه‌شناسی پذیرفته‌شدهٔ دیگری دارند (نگاه کنید به گره‌های ۱، ۳، ۵ و ۶).\",\n   \"sources\": [W_BAHIS],\n   \"ref_check\": [\n    {\"ref\": \"IEC:69,70\", \"status\": \"supports\", \"note\": \"Mann, IEC, the pp.69-70 spread (local OCR /refs/IEC.txt, form-feed leaf 54): 'bheǵh-iKs (-əK) \\\"outside, without, except\\\". WP II, 137. See next — Skt. bahís, bahíṣ, bahíś \\\"out, away, except\\\"; Arm. bac, bajc \\\"but\\\", baci \\\"except\\\"; Per. bajuz, id.; OW cf. bei, W bai \\\"defect\\\", oni bai \\\"except\\\"; OCS bezŭ \\\"without\\\"; Latv. bez, id.' Immediately below: 'bheǵh- (variant of bheǵh-, see bheǵh-iKs) — Skt. bahyah, adj. \\\"outside\\\"; Per. bāz \\\"open\\\"…'. This is exactly Nourai's root box, glosses included.\"},\n    {\"ref\": \"POK:112\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.112 (local OCR POK_01.txt, awk leaf 122, running head '113' on the next leaf): 'I. b(h)e und b(h)eǵh … \\\"außer, außerhalb, ohne\\\" — Ai. bahiḥ (-s) \\\"draußen, von außen, außerhalb von\\\" (m. Abl.)', continued p.113 'apr. bhe \\\"ohne\\\" (Präp. m. Akk.), lit. bè \\\"ohne\\\" …; lett. bez \\\"ohne\\\" …; aksl. bez … \\\"ohne\\\"'. Supports the root, the language label and the 'outside/except' gloss; does not give 'open'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p.112-113 (POK_01.txt leaf 122-123)\", \"stance\": \"supports\", \"note\": \"'I. b(h)e und b(h)eǵh … außer, außerhalb, ohne'; the aspiration is left open as b(h)-.\"},\n    {\"src\": \"IEC\", \"where\": \"pp.69-70 (IEC.txt leaf 54)\", \"stance\": \"supports\", \"note\": \"'bheǵh-iKs (-əK) outside, without, except. WP II, 137.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix\", \"stance\": \"silent\", \"note\": \"grep -i 'bhegh' AHD_watkins1985.txt returns only 'bheg- To break' and 'bhegʷ- To run away'; the appendix has no *bheǵʰ- 'outside' root, because no English word descends from it.\"},\n    {\"src\": \"WLD\", \"where\": \"WP II 137 (cited by Mann); local WLD_Bd2 djvu text\", \"stance\": \"silent\", \"note\": \"grep -i 'bahis|bahih|außerhalb, ohne|bheĝh' over incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt and WLD_band3.txt returned nothing — the Bd. II OCR is too poor to locate p.137; Mann's own reference 'WP II, 137' is the only witness available.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 1949\", \"stance\": \"silent\", \"note\": \"Buck has no chapter for 'outside/except' particles; grep of SYN.txt for bahis/bez found nothing.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"a-pâč\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The word is real: Book Pahlavi ʾpʾc (ideogram LʾWḤL, from Aramaic lʾ(w)ḥr), read abāz, Manichaean MP ʾbʾc, Parthian ʾbʾc; MacKenzie glosses it 'back, again, re-' and lists the phrase 'abāz kardan: open', which is where Nourai's gloss 'open' comes from. What is wrong is the ancestry drawn. Nyberg derives apāč from *apācā, an instrumental adverb of the Old Iranian adjective *apānk- (weak stem apāk-/apāč-), itself built on Avestan and Old Persian apa 'off, away' (cf. Skt. apáñc- 'situated behind') — i.e. from PIE *h₂epo, not from *bʰeǵʰ-. Nourai's own transcription 'a-pâč' in fact spells the apa- prefix out. Wiktionary knows the *bʰe + *-ǵʰs derivation only as an explicitly 'less likely' alternative to the *apāča- one. A second, smaller point: 'open' is not a lexical meaning of abāz at all but a contextual value of the compound verb abāz kardan 'to put back, throw back (a door)'.\",\n     \"derivation_fa\": \"صورت پهلوی درست است: در پهلوی کتابی ʾpʾc (با هزوارش LʾWḤL) خوانده abāz، در پهلوی مانوی ʾbʾc و در پارتی نیز ʾbʾc؛ مکنزی آن را «پس، دوباره، باز-» معنی می‌کند و ترکیب abāz kardan «گشودن» را می‌آورد که سرچشمهٔ معنای «باز/گشوده» در نمودار نورایی است. اما تبارِ کشیده‌شده نادرست است: نیبرگ apāč را از *apācā، قید ابزاریِ صفت ایرانی باستان *apānk- (ستاک ضعیف apāk-/apāč-) می‌داند که خود از پیشوند apa «دور، از» در اوستایی و پارسی باستان ساخته شده است (هم‌ریشه با سنسکریت apáñc- «واقع در پشت»)، یعنی از *h₂epo هندواروپایی، نه از *bʰeǵʰ-. جالب آنکه خودِ نگارش نورایی («a-pâč») همین پیشوند apa- را آشکار می‌کند. ویکی‌واژه اشتقاق از *bʰe + *-ǵʰs را تنها همچون گزینه‌ای «کم‌احتمال‌تر» یاد می‌کند. پژوهش امروزی ادعای نورایی را در این بند رد می‌کند.\",\n     \"sources\": [W_BAZ, A_BAZ],\n     \"ref_check\": [\n      {\"ref\": \"MON:452\", \"status\": \"partial\", \"note\": \"Mo'in's print vol. 1 p.452 could not be read (no OCR; the Persian OCR of MON_part1.txt is unusable). The online Mo'in text (abadis.ir/fatofa/باز) does tag the 'back, again' باز as '[په.]' (Pahlavi) — 'بر سر افعال درآید به معنی دوباره، از نو' — which supports a Pahlavi antecedent, i.e. Nourai's Pahlavi box, but Mo'in gives no Latin-script Pahlavi form and no Indo-European root, so the arrow from *bʰeǵʰ- is not in Mo'in.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. abāz (PHD.txt line 164)\", \"stance\": \"supports\", \"note\": \"'abāz [LʾWḤL < A lʾ(w)ḥr; ʾpʾc | M ʾpʾc, N bāz, wā] back, again, re- … ~ kardan: open.' Confirms the Pahlavi form, the New Persian outcome and the 'open' value of the compound.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. apāc (NYB_vol2_glossary.txt line 476)\", \"stance\": \"contradicts\", \"note\": \"'apāc [LʾWḤL; ʾpʾc] 1. adv. back, backward (opp. frāc), again … 1. < *apācā instr. adv. from OIr adj. *apānk-, weak st. apāk- and apāc, derived from Av. (72) apa, OP apa, cf Skr apáñc- \\\"situated behind\\\"; MPrth ʾbʾc; Paz. awāž; NP bāz.' Explicitly *apa-, not *bheǵh-.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann pp.69-70\", \"stance\": \"partial\", \"note\": \"Mann puts 'Per. bāz \\\"open\\\"' under 'bheǵh- (variant …)' but cites no Pahlavi form at all, so he supports the New Persian node, not this Pahlavi one.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index\", \"stance\": \"silent\", \"note\": \"grep -i 'BAZ|APAC' over incoming/ARY/ARY_latin_index_pages.txt only returns the entries for بازو BAZU 'arm' (pdf pages 104-105); no entry for باز 'open'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"bâz «باز ٣»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"New Persian باز bāz continues Middle Persian abāz (ʾpʾc) with the regular loss of the unstressed initial a- of a proclitic preverb (abāz > bāz, beside the dialectal/archaic doublet wā-); MacKenzie prints the equation himself, 'abāz … | M ʾpʾc, N bāz, wā', and Nyberg ends the apāc entry with 'NP bāz'. So the arrow #1 → #2 as drawn is right, and Mann does list 'Per. bāz \\\"open\\\"' on the cited page. What keeps this from 'confirmed' is a second uncertainty above the arrow: Wiktionary treats bāz 'open' (Etymology 1) and bāz 'back, again' (Etymology 2) as separate entries, saying only 'Perhaps related to Etymology 2' and floating an alternative link to بختن boxtan 'to save, liberate'. The 'open' sense is best explained as an ellipsis of bāz kardan 'to throw back, open', already Pahlavi abāz kardan; the ultimate root remains *h₂epo (see #1), not *bʰeǵʰ-.\",\n     \"derivation_fa\": \"«باز» فارسی نو دنبالهٔ abāz فارسی میانه (ʾpʾc) است؛ الفِ آغازینِ بی‌تکیهٔ پیشوند در گذر به فارسی نو افتاده است (abāz > bāz، در کنار گونهٔ کهن‌تر wā-). مکنزی خود این برابری را می‌نویسد («abāz … N bāz, wā») و نیبرگ نیز مدخل apāc را با «NP bāz» به پایان می‌برد؛ پس پیکان گره ۱ به گره ۲ درست است و مان هم در همان صفحه «Per. bāz: open» را آورده است. آنچه مانع «تأیید کامل» می‌شود، تردیدی است که ویکی‌واژه دربارهٔ یکی بودن «بازِ گشوده» و «بازِ دوباره» دارد: آن دو را دو مدخل جدا آورده و تنها می‌گوید «شاید مرتبط». به احتمال بسیار «باز» به معنای گشوده کوتاه‌شدهٔ «باز کردن» است که در فارسی میانه نیز abāz kardan بوده است. ریشهٔ نهایی همچنان *h₂epo است، نه *bʰeǵʰ-.\",\n     \"sources\": [W_BAZ, A_BAZ],\n     \"ref_check\": [\n      {\"ref\": \"IEC:70\", \"status\": \"supports\", \"note\": \"Mann, IEC p.70 (leaf 54): 'bheǵh- (variant of bheǵh-, see bheǵh-iKs) — Skt. bahyah, adj. \\\"outside\\\"; Per. bāz \\\"open\\\"; Tokh. A cf. pakär, B pākri \\\"openly\\\"; ON bagr \\\"chary, awkward\\\"…'. Mann says exactly what Nourai's box says.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. abāz\", \"stance\": \"supports\", \"note\": \"'abāz … | M ʾpʾc, N bāz, wā] back, again, re-' — the MP → NP step is MacKenzie's own.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. apāc\", \"stance\": \"partial\", \"note\": \"'…MPrth ʾbʾc; Paz. awāž; NP bāz' — supports the descent, contradicts the PIE root.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in s.v. باز (online, abadis.ir)\", \"stance\": \"partial\", \"note\": \"'[ص.] گشاد، گشوده' for the adjective and '[په.]' (Pahlavi) for the 'again' particle; a Pahlavi origin, no IE root.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'apāč|apac|bâz|bāz ' over HRN.txt returns nothing; Horn has no numbered entry for بازِ 'open'.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"bejoz «بجز»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"بجز is not a single inherited word but a transparent phrase: the preposition بِ (be, from به) + جز joz 'except', exactly as Dehkhoda analyses it, 'بجز. [بِ جُ] (حرف مرکب) (از: ب + جز)'. جز in turn goes back to Middle Persian jud 'separate, different' and its phrase jud az 'except, apart from' — MacKenzie prints the equation 'jud [ywdtʾ | M jwd] separate, different; anti-. ~ az [N juz] except, apart from', Wiktionary has 'From Middle Persian jud az \\\"except, apart from\\\"', and Horn (no. 418) traces the whole family to Avestan yūta- 'separated' (Pahlavi jutāk, jut), listing juz among the New Persian variants of jud. Mann does print 'Per. bajuz' under *bʰeǵʰ-iḱs on the cited page, which is where Nourai got it, but the match is accidental: the b- is the Persian preposition, and *-ǵʰ-s could not yield -z after a j- that has no place in the reconstruction. Modern Iranian etymology is unanimous for *yuta-.\",\n     \"derivation_fa\": \"«بجز» واژه‌ای یکپارچه و موروثی نیست، بلکه ترکیبی روشن است: حرف اضافهٔ «بِ» (از «به») + «جز». دهخدا هم آن را چنین تحلیل می‌کند: «بجز. [بِ جُ] (حرف مرکب) (از: ب + جز)». «جز» خود از فارسی میانهٔ jud «جدا، دیگرگون» و ترکیب jud az «جز، غیر از» می‌آید؛ مکنزی صریحاً می‌نویسد «jud … ~ az [N juz] except, apart from» و ویکی‌واژه نیز همین را می‌گوید. هرن (شمارهٔ ۴۱۸) کل این خانواده را به اوستایی yūta- «جدا» (پهلوی jutāk، jut) بازمی‌گرداند و juz را در شمار گونه‌های فارسی «جدا/جد» می‌آورد. مان در همان صفحهٔ ۷۰ «Per. bajuz» را ذیل *bʰeǵʰ-iḱs آورده و منبع نورایی همین است، اما این شباهت تصادفی است: «ب» حرف اضافه است و «ج» جایی در بازسازیِ *bʰeǵʰ-iḱs ندارد. ریشه‌شناسی امروزی ایرانی ادعای نورایی را رد می‌کند و «جز» را از *yuta- می‌داند.\",\n     \"sources\": [W_JOZ, A_BEJOZ],\n     \"ref_check\": [\n      {\"ref\": \"IEC:70\", \"status\": \"supports\", \"note\": \"Mann, IEC p.70: 'bheǵh-iKs (-əK) \\\"outside, without, except\\\" … Skt. bahís …; Arm. bac, bajc \\\"but\\\"; Per. bajuz, id.; … OCS bezŭ \\\"without\\\"; Latv. bez, id.' Mann does list the Persian word here, so Nourai reports his source faithfully — the reference supports the arrow even though the arrow itself is wrong.\"},\n      {\"ref\": \"MON:473\", \"status\": \"not_found\", \"note\": \"Mo'in's print vol.1 p.473 unreadable (no OCR). The online Mo'in text for بجز (abadis.ir/fatofa/بجز) has no separate Mo'in entry at all; the Dehkhoda entry on the same page gives '(از: ب + جز)', i.e. a compound, not a single inherited word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 418 (HRN.txt line 3914)\", \"stance\": \"contradicts\", \"note\": \"'418. jūdā \\\"getrennt\\\"; jud (AM.), jut (AM.), jū (Is. 3, 41), juz (d. i. juz ez). … aw. yūta- \\\"getrennt\\\"; phlv. jutāk, jut bezw. yutak, yut.' Horn puts juz squarely with Av. yūta-.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. jud (PHD.txt line 414)\", \"stance\": \"contradicts\", \"note\": \"'jud [ywdtʾ | M jwd] separate, different; anti-. ~ az [N juz] except, apart from' — MacKenzie's own MP → NP equation for juz.\"},\n      {\"src\": \"MON\", \"where\": \"Dehkhoda/Mo'in via abadis.ir\", \"stance\": \"contradicts\", \"note\": \"Dehkhoda: 'بجز … (حرف مرکب) (از: ب + جز)'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p.70\", \"stance\": \"supports\", \"note\": \"'Per. bajuz' listed under bheǵh-iKs — the only source for Nourai's arrow.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"bôhyah; bahis\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The second word is right: Sanskrit बहिस् bahis (also bahiḥ, bahir) 'out, forth, outwards, outside', and with the ablative or in compounds 'out of, apart from, except' — Wiktionary derives it 'probably from PIE *bʰeǵʰ- (outside), from *bʰe (instrumental particle) + *-ǵʰs (out)', with the cognates Proto-Slavic *bez, Lith. bè, Latv. bez, OPr. bhe, and Pokorny opens the whole entry with it ('Ai. bahiḥ (-s) draußen, von außen, außerhalb von'). Nourai's gloss 'except, excluding' is however only the secondary, ablative-governing value; the primary sense is 'outside, out'. The first word is a misprint. Sanskrit has no *bôhyah; the intended word is बाह्य bāhya- 'outer, external, being outside', a vṛddhi derivative in -ya- of bahis, and this is exactly what Nourai's own source prints — Mann IEC 70 'Skt. bahyah, adj. \\\"outside\\\"' (i.e. bāhyaḥ). Since Nourai renders Sanskrit ā everywhere else with â (bâ, bâz, Bhâ), 'bôhyah' with ô is his own slip for 'bâhyah'. The printed page (pdf 83, book 53) shows 'bôhyah' plainly, so the extraction is faithful and the error is the book's.\",\n     \"derivation_fa\": \"واژهٔ دوم درست است: संस्कृत बहिस् bahis (نیز bahiḥ, bahir) به معنای «بیرون، به بیرون، در بیرون» و با «ازی» (ablative) یا در ترکیب «جز، غیر از». ویکی‌واژه آن را «به احتمال از *bʰeǵʰ- هندواروپایی آغازین، مرکب از *bʰe (حرف ابزاری) + *-ǵʰs «بیرون»» می‌داند و هم‌ریشه‌های آن را اسلاوی *bez، لیتوانیایی bè، لتونیایی bez و پروسی کهن bhe می‌شمارد؛ پوکورنی نیز مدخل خود را با همین واژه می‌گشاید. تنها ایراد آنکه معنای «جز، مگر» ارزش دومِ این قید است و معنای اصلی «بیرون» است. اما واژهٔ نخست غلط چاپی است: در سنسکریت *bôhyah وجود ندارد؛ صورت درست बाह्य bāhya- «بیرونی، برونی» است، مشتقی با پسوند -ya- و وریدّهیِ bahis؛ و خودِ منبع نورایی (مان، ص ۷۰) همین را «Skt. bahyah, adj. outside» می‌نویسد. چون نورایی در همه‌جا آ را با â می‌نگارد (bâ, bâz, Bhâ)، «bôhyah» لغزش خود او به جای «bâhyah» است. تصویر صفحهٔ چاپی (صفحهٔ ۸۳ پی‌دی‌اف، صفحهٔ ۵۳ کتاب) «bôhyah» را آشکارا نشان می‌دهد؛ پس خطا از خوانش اسکن نیست، از چاپ کتاب است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"bôhyah\",\n     \"correct_form\": \"bâhyah (Sanskrit बाह्य bāhya- 'outer, external')\",\n     \"sources\": [W_BAHIS],\n     \"ref_check\": [\n      {\"ref\": \"IEC:70\", \"status\": \"partial\", \"note\": \"Mann IEC p.70 has both words but spells the first differently: 'bheǵh- (variant …) — Skt. bahyah, adj. \\\"outside\\\"…' and 'bheǵh-iKs … Skt. bahís, bahíṣ, bahíś \\\"out, away, except\\\"'. So the reference supports the two Sanskrit items and their affiliation, but prints bahyah (bāhyaḥ) where Nourai prints bôhyah.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.112 (POK_01.txt leaf 122)\", \"stance\": \"supports\", \"note\": \"'Ai. bahiḥ (-s) \\\"draußen, von außen, außerhalb von\\\" (m. Abl.)' — heads the entry; note Pokorny's gloss is 'outside', with 'außerhalb von' (= 'apart from') only with the ablative.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p.70\", \"stance\": \"partial\", \"note\": \"'Skt. bahís, bahíṣ, bahíś \\\"out, away, except\\\"' and 'Skt. bahyah, adj. \\\"outside\\\"'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"no *bheǵʰ- root in the appendix (grep 'bhegh' → only bheg-, bhegʷ-).\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 1949\", \"stance\": \"silent\", \"note\": \"grep 'bahis' over SYN.txt returns nothing.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Indo-European\",\n     \"words\": \"Bheg\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"This box silently welds two different Indo-European roots together, and neither of them descends from *bʰeǵʰ- 'outside'. (a) 'To oust out, push out' is Mann's theme 'bhéǵho, iō \\\"oust\\\" (?)' on the very page Nourai cites (IEC 70): Gk. ptḗssō 'scare', OHG bāgan / MHG bāgen 'strive, shriek, quarrel', OHG bāga 'battle', ON bægja 'oust, thwart, quarrel, force'. Mann does cross-refer it to bheǵh-iḱs/bheǵh-, which is Nourai's warrant, but he flags it with a question mark, and Pokorny, who has the same root on p.115 as 'bhēgh- : bhōgh- \\\"streiten\\\"' (Gall. bāgaudae, OIr. bāgaid, OHG bāgan, ON bāga, bǣgja), does not connect it to b(h)e / b(h)eǵh- on p.112 at all. (b) 'Strike, break' is a wholly separate root, Pokorny 114-115 'bheg-, bheng- \\\"zerschlagen, zerbrechen\\\"' (Skt. bhanákti, babháñja, bhagná- 'broken'), which Mann also keeps apart, listing it on the same p.70 as 'bheg- \\\"break, pierce\\\": Skt. bhagnaḥ \\\"broken\\\"; Arm. bek, bekem'. Only sense (b) leads to the Germanic bank family below (node #6), while only sense (a) has any tie — a queried one — to the root box above. The node as drawn is therefore a conflation, and the arrow root → #5 is not in Pokorny.\",\n     \"derivation_fa\": \"این جعبه دو ریشهٔ هندواروپاییِ جداگانه را در هم آمیخته است و هیچ‌یک از آن دو از *bʰeǵʰ- «بیرون» برنمی‌آید. الف) معنای «راندن، بیرون راندن» همان مدخل مان در همان صفحهٔ ۷۰ است: «bhéǵho «راندن» (؟)» با شواهد یونانی ptḗssō، آلمانی علیای باستان bāgan، و نورس کهن bægja؛ مان آن را به bheǵh-iḱs ارجاع می‌دهد (و همین مستند نورایی است) اما با علامت پرسش. پوکورنی همین ریشه را در ص ۱۱۵ زیر «bhēgh- : bhōgh- «ستیزیدن»» آورده و هیچ پیوندی میان آن و b(h)eǵh- ص ۱۱۲ برقرار نکرده است. ب) معنای «زدن، شکستن» ریشه‌ای یکسره جداست: پوکورنی ص ۱۱۴–۱۱۵ «bheg-, bheng- «درهم شکستن»» (سنسکریت bhanákti، bhagná-)؛ مان نیز آن را جدا و در همان ص ۷۰ چنین می‌آورد: «bheg- «شکستن، سوراخ کردن»: Skt. bhagnaḥ؛ Arm. bek». تنها معنای (ب) به خانوادهٔ ژرمنی bank در گره بعدی می‌رسد و تنها معنای (الف) پیوندی — آن هم پرسش‌دار — با جعبهٔ ریشه دارد. بنابراین این گره آمیزهٔ دو ریشه است و پیکان «ریشه ← گره ۵» در پوکورنی نیست.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"IEC:70\", \"status\": \"partial\", \"note\": \"Mann IEC p.70 has 'bhéǵho, iō \\\"oust\\\" (?). Cf. bheǵh-iKs, bheǵh- — Gk. cf. synth. cpd. ptḗssō …; OHG bāgan, MHG bāgen … ON bægja \\\"oust, thwart, quarrel, force\\\"' — supports the 'oust' half and the cross-reference to the root, but with Mann's own '(?)'; the 'strike, break' half is Mann's separate theme 'bheg- \\\"break, pierce\\\"' on the same page, not cross-referred to bheǵh-.\"},\n      {\"ref\": \"POK:115\", \"status\": \"partial\", \"note\": \"Pokorny p.115 (POK_01.txt leaf 125) does carry both 'bheg-, bheng- \\\"zerschlagen, zerbrechen\\\"' (running over from p.114) and, further down, 'bhēgh- : bhōgh- \\\"streiten\\\"'. So the page number is right for the forms; but Pokorny nowhere derives either root from b(h)e / b(h)eǵh- (p.112), so the reference does not support the arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW pp.114-115 (POK_01.txt leaves 124-125)\", \"stance\": \"contradicts\", \"note\": \"Two independent entries, 'bheg-, bheng- \\\"zerschlagen, zerbrechen\\\"' and 'bhēgh- : bhōgh- \\\"streiten\\\"', neither cross-referred to p.112 b(h)e/b(h)eǵh-.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p.70\", \"stance\": \"partial\", \"note\": \"'bheg- \\\"break, pierce\\\"' and 'bhéǵho \\\"oust\\\" (?)' are two separate themes on that page; only the second is cross-referred to bheǵh-.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bheg-\", \"stance\": \"partial\", \"note\": \"'bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. … [Pok. bheg- 115.]' — Watkins knows only the 'break' root here, with no 'oust' sense and no link to any 'outside' root.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Germanic\",\n     \"words\": \"bankon\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Germanic form and gloss are correct and are exactly Watkins's: AHD's IE-roots appendix (the pages 1505-1550 Nourai cites as AHD:1508) lists under 'bheg-. To break' the item 'Possibly Germanic nasalized forms *bankiz and *bankōn-, bank of earth (possibly < \\\"feature where the contour of the ground is broken,\\\" escarpment, riverbank, possibly also associated with \\\"manmade earthwork\\\"), later also bench, table'. Buck agrees in substance: 'ON bakki \\\"riverbank\\\", but also \\\"bank\\\" in general, as ME banke (fr. ON), NE bank : OHG banch, OE benc \\\"bench\\\", etc. perh. Skt. bhanj- \\\"break\\\"'. Two hedges keep this from 'confirmed'. First, Watkins prefixes the whole root with 'Possibly in various Germanic forms' and the *bankiz/*bankōn- item with a second 'Possibly'. Second, Pokorny on the very page Nourai cites (115) actively excludes the Germanic *bang-/*bank- group from bheg-: 'Die folgenden Formen sind wegen des Auslautes und wegen der Bedeutung fernzuhalten und wohl als Schallworte zu deuten: germ. *bang- \\\"schlagen\\\" … germ. *bank- in aschwed. banka, abl. bunka \\\"schlagen, klopfen\\\"'. And whichever way that is decided, *bankōn- attaches to 'break', not to the 'outside' root at the head of this chart.\",\n     \"derivation_fa\": \"صورت و معنای ژرمنی درست است و دقیقاً همان چیزی است که واتکینز می‌آورد: پیوست ریشه‌های هندواروپاییِ فرهنگ American Heritage (همان صفحات ۱۵۰۵–۱۵۵۰ که نورایی با AHD:1508 به آن ارجاع می‌دهد) ذیل «bheg-: شکستن» چنین دارد: «شاید صورت‌های خیشومی‌شدهٔ ژرمنی *bankiz و *bankōn- «کرانهٔ خاکی» (شاید از «جایی که خطِ زمین شکسته می‌شود»: پرتگاه، کنارِ رود) و سپس نیمکت و میز». باک نیز همین را می‌گوید و آن را با سنسکریت bhanj- «شکستن» می‌سنجد. اما دو احتیاط مانع تأیید کامل است: نخست آنکه واتکینز خودِ ریشه و نیز این بند را با «شاید» می‌آغازد؛ دوم آنکه پوکورنی در همان صفحهٔ ۱۱۵ گروه ژرمنی *bang-/*bank- را از bheg- بیرون می‌گذارد و آن را واژه‌های آوایی (Schallworte) می‌شمارد. به هر روی، *bankōn- به ریشهٔ «شکستن» می‌پیوندد، نه به ریشهٔ «بیرون» که در سر این نمودار نشسته است. پس این بند «با احتیاط پذیرفتنی است».\",\n     \"sources\": [E_BENCH, E_BANK],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1508\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 325), s.v. bheg-: '2. Possibly Germanic nasalized forms *bankiz and *bankōn-, bank of earth (possibly < \\\"feature where the contour of the ground is broken,\\\" escarpment, riverbank …), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank … BANK¹; c. Old High German banc, bank, bench, moneychanger's table (> Italian banca): BANK², BANTLING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET. [Pok. bheg- 115.]' Nourai's 'bankon: river banks' is Watkins's *bankōn- 'bank of earth … riverbank'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bheg-\", \"stance\": \"supports\", \"note\": \"quoted above; note the double 'Possibly'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.115 (POK_01.txt leaf 125)\", \"stance\": \"contradicts\", \"note\": \"'Die folgenden Formen sind wegen des Auslautes und wegen der Bedeutung fernzuhalten und wohl als Schallworte zu deuten: germ. *bang- \\\"schlagen\\\" … germ. *bank- in aschwed. banka …'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 1949 (SYN.txt line 1195)\", \"stance\": \"supports\", \"note\": \"'ON bakki \\\"riverbank\\\", but also \\\"bank\\\" in general, as ME banke (fr. ON), NE bank : OHG banch, OE benc \\\"bench,\\\" etc. perh. Skt. bhanj- \\\"break.\\\" NED s.v. bank, sb.1. Falk-Torp 43. Walde-P. 2.148.'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. bench (KLN_1971.txt line 28174)\", \"stance\": \"partial\", \"note\": \"'bench, n. — ME., fr. OE. benc, rel. to ON. bekkr, Dan., Swed. bank, OS., OFris., MLG., Du., OHG., G. bank, MHG. banc, \\\"bench\\\", ON. bakki, \\\"elevation\\\".' Klein gathers the same Germanic family but offers no PIE root.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"bank, bankrupt, banquet; bench\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All four English words go back to the Germanic *bank-/*bankōn- of node #6, by four different routes, and every step is standard. bench is the直 native one: OE benc 'long seat' > ME bench, from PGmc *bankiz (Etymonline: 'from Old English benc \\\"long seat\\\" … from Proto-Germanic *bankon … cognate with bank (n.2)'). bank 'money institution' is the borrowed one: Lombardic/OHG banc 'bench, moneychanger's table' > It. banco/banca > Fr. banque > English bank (16th c.) — Klein, s.v. bank: 'F. banque, fr. It. banco, orig. \\\"bench, table, counter\\\" (scil. of a money changer), which is of Teut. origin'. bankrupt is It. banca rotta 'a broken bench' > Fr. banqueroute, refashioned in English on Latin rupta (Klein: 'so called from the habit of breaking the bench of bankrupts'), first English use 1530s. banquet is Fr. banquet, from It. banchetto, diminutive of banco 'bench' — a meal taken at the bench (Klein s.v. banquet). Skeat files them together in one line, 'Bench. (E.) See Bank.' One correction to the chart: the note 'originally used by bankers to exchange money' is printed against bench, but it belongs to bank/banca — bench is simply the inherited Old English seat and has nothing to do with money-changing.\",\n     \"derivation_fa\": \"هر چهار واژهٔ انگلیسی از همان *bank-/*bankōn- ژرمنیِ گرهٔ ۶ می‌آیند، اما از چهار راه جدا و همهٔ گام‌ها استاندارد است. bench واژهٔ موروثی است: انگلیسی باستان benc «نیمکت بلند» از *bankiz ژرمنی آغازین. bank به معنای «بانک» وام‌واژه است: banc در لومباردی/آلمانی علیای باستان «نیمکت، میز صرّاف» ← banco/banca ایتالیایی ← banque فرانسوی ← bank انگلیسی (سدهٔ شانزدهم)؛ کلاین می‌نویسد «از فرانسوی banque، از ایتالیایی banco، در اصل «نیمکت، میز» (میزِ صرّاف)، که خاستگاه ژرمنی دارد». bankrupt از banca rotta ایتالیایی به معنای تحت‌اللفظی «نیمکتِ شکسته» است (کلاین: «از این رو که نیمکت ورشکستگان را می‌شکستند»)، از راه banqueroute فرانسوی و سپس بازساخته بر پایهٔ rupta لاتینی. banquet نیز از banchetto ایتالیایی، مصغّرِ banco «نیمکت»، از راه فرانسوی. یک اصلاح: یادداشت «در اصل نزد صرّافان برای تبدیل پول به کار می‌رفت» در نمودار زیر bench نشسته، حال آنکه به bank/banca مربوط است؛ bench همان نیمکتِ موروثیِ انگلیسی باستان است و ربطی به صرافی ندارد.\",\n     \"sources\": [E_BENCH, E_BANK],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. bheg- lists precisely these words: 'a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank … BANK¹; c. Old High German banc, bank, bench, moneychanger's table (> Italian banca): BANK², BANTLING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET.' The index confirms it: 'BANK¹ bheg- BANK² bheg- BANKRUPT bheg-, reup- BANQUET bheg-' and 'BENCH bheg-'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.vv. bench, bank, bankrupt, banquet (KLN_1971.txt lines 25625-25721, 28174-28178)\", \"stance\": \"supports\", \"note\": \"'bank, n., an institution for the custody of money. — F. banque, fr. It. banco, orig. \\\"bench, table, counter\\\" (scil. of a money changer), which is of Teut. origin'; 'bankrupt … fr. It. banca rotta, lit. \\\"a broken bench\\\" … so called from the habit of breaking the bench of bankrupts'; 'banquet, n. — F., fr. It. banchetto, dimin. of banco, \\\"bench\\\"'; 'bench, n. — ME., fr. OE. benc …'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat (SKT.txt lines 1379, 1714)\", \"stance\": \"supports\", \"note\": \"'Bench. (E.) See Bank.'; 'Bank (1), a mound of earth … Icel. bakki (for banki), O.H.G. panch, a bank, a bench.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 1949 (SYN.txt line 19771)\", \"stance\": \"supports\", \"note\": \"on 'bank': 'the word bank \\\"bench\\\" … were often applied to a … counter for the display of wares, that of the moneychangers … It was the fem. form … banca, Fr. banque, etc.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 index\", \"stance\": \"supports\", \"note\": \"'BANG¹ bheg- BANK¹ bheg- BANK² bheg- BANK³ bheg- BANKRUPT bheg-, reup- … BANQUET bheg- BANQUETTE bheg-' and 'BENCH bheg-'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Bhě, Bho, Bha, Bhâ\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *bʰē̆ / *bʰō / *bʰā, an asseverative and emphasising particle ('indeed, truly') — Pokorny IEW 113 'bhē̆ … Partikel bes. der Beteuerung und Hervorhebung'; Mann IEC 59 'bha, bho \\\"indeed\\\". WP II, 136' and 'bhā \\\"indeed\\\". WP II, 123 & 136'\",\n   \"note\": \"This root box is right on every count. Pokorny p.113 heads the entry 'bhē̆ … Partikel bes. der Beteuerung und Hervorhebung' and assembles Av. bā, bāt̰, bē, bōit̰, bāδa 'fürwahr'; arm. ba, bay; Goth. ba (conditional), i-ba, ni-ba; Lith. bà 'ja, freilich', be, bei; OCS bo 'denn', i-bo, u-bo, ne-bo-n; Ukr./Czech/Polish ba 'traun, fürwahr'. Mann IEC 59 splits the same material into two adjacent themes, 'bha, bho \\\"indeed\\\"' and 'bhā \\\"indeed\\\"', and cites WP II 136 for both — which is exactly Nourai's third reference WLD2:136. The four ablaut variants in the box (Bhě, Bho, Bha, Bhâ) match Mann's two headwords plus the o-grade he cites from OCS bo. It is worth stressing that this particle is kept strictly apart by Pokorny from the *b(h)e / *b(h)eǵh- 'outside, without' of the previous chart on this same page (IEW 112), and Nourai keeps them apart too — correctly. That separation is what makes the Persian node #4 below a problem, since the modern derivation of Persian be-/bi- runs through the OTHER root.\",\n   \"note_fa\": \"این جعبهٔ ریشه از هر نظر درست است. پوکورنی در ص ۱۱۳ مدخل «bhē̆» را «حرفی برای سوگند و تأکید» می‌نامد و شواهد اوستایی bā، bāt̰، bē، bōit̰ و bāδa «فی‌الواقع»، ارمنی ba و bay، گوتیک ba، لیتوانیایی bà «آری، البته»، اسلاوی کلیسایی کهن bo «زیرا» و چکی/لهستانی ba «به‌راستی» را گرد می‌آورد. مان (ص ۵۹) همین مواد را در دو مدخل کنار هم می‌نشاند: «bha, bho: به‌راستی. WP II, 136» و «bhā: به‌راستی. WP II, 123 و 136» — و همین ارجاع سومِ نورایی (WLD2:136) است. چهار گونهٔ آوایی جعبه (Bhě، Bho، Bha، Bhâ) با دو سرواژهٔ مان و گونهٔ o-دارِ اسلاوی می‌خوانند. باید تأکید کرد که پوکورنی این حرفِ تأکید را از ریشهٔ *b(h)e / *b(h)eǵh- «بیرون، بی‌» در نمودار پیشینِ همین صفحه (ص ۱۱۲) یکسره جدا نگاه می‌دارد و نورایی نیز درست همین کار را کرده است؛ و همین جدایی است که گرهٔ چهارم فارسی را دچار اشکال می‌کند، زیرا ریشه‌شناسی امروزیِ پیشوند «بـ» فارسی از آن ریشهٔ دیگر می‌گذرد.\",\n   \"sources\": [MW],\n   \"ref_check\": [\n    {\"ref\": \"POK:113\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.113 (POK_01.txt awk leaf 123, running head '113'): 'bhē̆ … Partikel bes. der Beteuerung und Hervorhebung. Av. bā, bāt̰, bē, bōit̰ (letzteres, wie lit. bei, wohl mit Verstärkungspartikel *id) Partikeln der Beteuerung und Hervorhebung, bāδa \\\"fürwahr\\\" … arm. ba, bay hervorhebende Partikel; got. ba Konditionalpartikel … lit. bà \\\"ja, freilich\\\" … aksl. bo \\\"denn\\\" … klr. ba \\\"ja, freilich\\\", čech. poln. ba \\\"traun, fürwahr\\\". WP. II 136.'\"},\n    {\"ref\": \"IEC:59\", \"status\": \"supports\", \"note\": \"Mann IEC p.59 (IEC.txt leaf 48): 'bha, bho \\\"indeed\\\". WP II, 136. See next — Skt. (Vedic) cf. bha-la; Per. ba-lī \\\"yes\\\"; Arm. ba (cj. \\\"that\\\", adv. \\\"yes\\\"); OIr. ba; Go. (infix) -ba-; OCS bo (cj. \\\"for\\\"); Li. cf. ar-ba \\\"or\\\"; bei \\\"indeed\\\".' and immediately after: 'bhā \\\"indeed\\\". Cf. bha, bho. WP II, 123 & 136 — Av. bā; Oss. ba \\\"but, yet\\\"; Arm. (ambig.) ba; Gk. phē; Cz. Pol. Ukr. ba.'\"},\n    {\"ref\": \"WLD2:136\", \"status\": \"partial\", \"note\": \"Walde-Pokorny Bd. II p.136 could not be read directly (the local WLD Bd. II OCR is unusable; grep for 'Beteuerung|bhē' returned nothing). But BOTH Pokorny ('WP. II 136') and Mann ('WP II, 136') cite that exact page for this particle, so the reference is corroborated at second hand and Nourai's citation is certainly correct.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p.113\", \"stance\": \"supports\", \"note\": \"'bhē̆ … Partikel bes. der Beteuerung und Hervorhebung.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann p.59\", \"stance\": \"supports\", \"note\": \"'bha, bho \\\"indeed\\\"' / 'bhā \\\"indeed\\\"'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"the appendix has no asseverative *bhē̆ root (no English descendant); grep of AHD_watkins1985.txt for 'bhē'/'indeed' particle entries returns nothing between bhedh- and bheg-.\"},\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW\", \"stance\": \"supports\", \"note\": \"s.v. bāδa (BRT.txt line 17075) 'Part. 1) der Beteuerung, am Satzanfang \\\"fürwahr\\\" … 2) zur Hervorhebung, meist hinter dem ersten Wort des Satz(teil)es' and s.v. bōit̰ (line 17235) 'Part. der Beteuerung und Hervorhebung, hinter dem ersten Wort im Satz'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"bâ, bě, beî\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The first two forms are genuine Avestan and stand exactly where Nourai puts them. Pokorny p.113 opens the entry with 'Av. bā, bāt̰, bē, bōit̰ … Partikeln der Beteuerung und Hervorhebung, bāδa \\\"fürwahr\\\"', citing Bartholomae's Altiranisches Wörterbuch, and Bartholomae has both bāδa ('Part. 1) der Beteuerung, am Satzanfang \\\"fürwahr\\\"') and bōit̰ ('Part. der Beteuerung und Hervorhebung, hinter dem ersten Wort im Satz'); Mann IEC 59 gives 'Av. bā' under bhā 'indeed'. The third form 'beî' is not an Avestan word. Two explanations are possible and I cannot decide between them from the page alone: either it is a garbling of Bartholomae's/Pokorny's bōit̰ (which Nourai's system would write bôit), or it is the Lithuanian particle bei 'indeed, and' picked up out of the same lists and mis-labelled Avestan — Pokorny p.113 has 'lit. … bei (s. oben) \\\"und\\\"' and Mann p.59 has 'Li. cf. ar-ba \\\"or\\\"; bei \\\"indeed\\\"' three words away from the Avestan citation. The printed page (pdf 83) reads 'bâ, bě, beî' plainly, so the JSON is faithful and the fault is the book's.\",\n     \"derivation_fa\": \"دو صورت نخست اوستایی راستین‌اند و درست همان‌جایی می‌نشینند که نورایی نهاده است: پوکورنی در ص ۱۱۳ مدخل را با «اوستایی bā، bāt̰، bē، bōit̰ … حروف سوگند و تأکید، bāδa «فی‌الواقع»» می‌گشاید و به فرهنگ ایرانی باستانِ بارتولومه ارجاع می‌دهد؛ بارتولومه نیز هم bāδa و هم bōit̰ را با همین کارکرد دارد، و مان (ص ۵۹) «Av. bā» را ذیل bhā «به‌راستی» می‌آورد. اما صورت سوم «beî» واژه‌ای اوستایی نیست. دو توضیح ممکن است و از روی صفحه نمی‌توان میان آن دو داوری کرد: یا دگرگون‌شدهٔ bōit̰ بارتولومه است (که در دستگاه نگارشیِ نورایی bôit می‌شد)، یا حرف لیتوانیایی bei «به‌راستی، و» است که از همان فهرست‌ها برداشته و به‌خطا اوستایی برچسب خورده است؛ پوکورنی در ص ۱۱۳ «lit. … bei» و مان در ص ۵۹ «Li. … bei «indeed»» را تنها چند واژه دورتر از شاهد اوستایی آورده‌اند. تصویر صفحهٔ چاپی «bâ, bě, beî» را آشکارا نشان می‌دهد؛ پس خطای چاپیِ کتاب است، نه خطای خوانش اسکن.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"bâ, bě, beî\",\n     \"correct_form\": \"bâ, bě, bôit (Avestan bā, bē, bōit̰; Pokorny 113 also bāt̰, bāδa)\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:113\", \"status\": \"partial\", \"note\": \"Pokorny p.113 gives 'Av. bā, bāt̰, bē, bōit̰' — supports bâ and bě, gives bōit̰ (not 'beî'), and lists 'lit. … bei' separately as Lithuanian.\"},\n      {\"ref\": \"IEC:59\", \"status\": \"partial\", \"note\": \"Mann p.59 gives only 'Av. bā' (under bhā 'indeed'); 'bei \\\"indeed\\\"' appears on the same page but explicitly as Lithuanian ('Li. cf. ar-ba \\\"or\\\"; bei \\\"indeed\\\"').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae AiW s.vv. bāδa, bōit̰ (BRT.txt lines 17075, 17235)\", \"stance\": \"partial\", \"note\": \"'bāδa Part. 1) der Beteuerung, am Satzanfang \\\"fürwahr\\\"'; 'bōit̰ Part. der Beteuerung und Hervorhebung, hinter dem ersten Wort im Satz'. No Avestan 'beî' anywhere in the AiW.\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.113\", \"stance\": \"partial\", \"note\": \"as quoted; Pokorny explicitly ties bōit̰ to Lith. bei ('letzteres, wie lit. bei, wohl mit Verstärkungspartikel *id').\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian\", \"stance\": \"silent\", \"note\": \"grep for the particle in KNT.txt found nothing — the asseverative bā is not attested in Old Persian.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"bha-la\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The word is real. Monier-Williams (1872, s.v.) has 'bhala 1. bhala, ind., Ved. certainly; [cf. bal, baṭ, and Marāṭhī bhalla, \\\"well!\\\"]' — a Vedic asseverative indeclinable equivalent to khalu. Nourai's hyphenated spelling 'bha-la' is copied straight from Mann, IEC 59 'Skt. (Vedic) cf. bha-la', which is the only source that files it under the IE particle *bʰa/*bʰō; Mann's 'cf.' is itself a hedge. Pokorny does not list bhala at all in the p.113 entry, and Monier-Williams compares it not with the particle but with the Vedic bal, baṭ. The gloss is also loose: bhala means 'certainly, indeed', not 'yes' (Sanskrit has no dedicated word for 'yes'). So: a real Vedic particle, semantically at home in this root, but the affiliation rests on Mann alone.\",\n     \"derivation_fa\": \"واژه راستین است. مونیر-ویلیامز (۱۸۷۲) می‌نویسد: «bhala، حرف، ودایی: به‌یقین؛ سنجیده شود با bal و baṭ و مراتیِ bhalla «خوب!»» — یعنی حرفِ تأکیدِ ودایی هم‌ارز khalu. نگارشِ خط‌فاصله‌دارِ «bha-la» در نمودار عیناً از مان (ص ۵۹: «Skt. (Vedic) cf. bha-la») گرفته شده و مان تنها منبعی است که آن را ذیل حرفِ هندواروپاییِ *bʰa/*bʰō می‌نشاند، آن هم با قید «cf.» که خود نشانهٔ احتیاط است. پوکورنی در مدخل ص ۱۱۳ نامی از bhala نمی‌برد و مونیر-ویلیامز نیز آن را نه با این حرف، بلکه با bal و baṭ می‌سنجد. معنا هم اندکی گشاده است: bhala یعنی «به‌یقین، به‌راستی»، نه «آری» (سنسکریت واژهٔ ویژه‌ای برای «بله» ندارد). بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [MW],\n     \"ref_check\": [\n      {\"ref\": \"IEC:59\", \"status\": \"supports\", \"note\": \"Mann IEC p.59 under 'bha, bho \\\"indeed\\\"': 'Skt. (Vedic) cf. bha-la' — Nourai's hyphenation and his placement are Mann's.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.113\", \"stance\": \"silent\", \"note\": \"the entry lists Avestan, Armenian, Gothic, Lithuanian, Old Prussian and Slavic forms but no Sanskrit at all; bhala is absent.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p.59\", \"stance\": \"supports\", \"note\": \"'Skt. (Vedic) cf. bha-la'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"no such root in the appendix.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Armenian\",\n     \"words\": \"ba\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Armenian բա ba is a genuine emphasising particle and both of Nourai's authorities have it. Pokorny p.113 lists 'arm. ba, bay hervorhebende Partikel' immediately after the Avestan forms, in the same entry as OCS bo, Lith. bà and Gothic ba; Mann IEC 59 gives 'Arm. ba (cj. \\\"that\\\", adv. \\\"yes\\\". *a or *ā)'. The equation is phonologically trivial — an unextended particle *bʰa/*bʰā gives Armenian ba with the regular Armenian reflex b < *bʰ — which is why it is agreed on all sides. Nourai's gloss 'yes' is Mann's adverbial value; Pokorny's more cautious 'emphasising particle' is the primary function.\",\n     \"derivation_fa\": \"«ba» ارمنی (բա) حرف تأکیدِ راستینی است و هر دو مأخذِ نورایی آن را دارند. پوکورنی در ص ۱۱۳ بی‌درنگ پس از صورت‌های اوستایی می‌نویسد «ارمنی ba، bay: حرف تأکید» و آن را در همان مدخلِ اسلاویِ bo، لیتوانیاییِ bà و گوتیکِ ba می‌نشاند؛ مان (ص ۵۹) نیز «Arm. ba (حرف ربط: که؛ قید: آری)» می‌آورد. برابرسازی از نظر آوایی بی‌دردسر است، زیرا *bʰ هندواروپایی در ارمنی به b بدل می‌شود و حرفی بی‌پسوند مانند *bʰa/*bʰā مستقیماً ba می‌دهد؛ به همین سبب همهٔ منابع بر آن هم‌داستان‌اند. معنای «آری» را نورایی از مان گرفته است؛ کارکرد اصلی، چنان‌که پوکورنی محتاطانه‌تر می‌گوید، تأکید است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"IEC:59\", \"status\": \"supports\", \"note\": \"Mann IEC p.59: 'Arm. ba (cj. \\\"that\\\", adv. \\\"yes\\\". *a or *ā)' under 'bha, bho \\\"indeed\\\"', and again 'Arm. (ambig.) ba (\\\"that\\\"; \\\"yes\\\")' under 'bhā'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.113 (POK_01.txt leaf 123)\", \"stance\": \"supports\", \"note\": \"'arm. ba, bay hervorhebende Partikel'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p.59\", \"stance\": \"supports\", \"note\": \"'Arm. ba (cj. \\\"that\\\", adv. \\\"yes\\\")'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"no such root in the appendix.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Persian\",\n     \"words\": \"bî-, be- «بِ- ، بی-»; baleh, balî «بله ، بلی»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Both halves of this box fail, for different reasons. (a) The verbal prefix be-/bi- (برفت be-raft, بیامد bi-āmad — the two examples Nourai prints) does not continue the Avestan asseverative bā of the parent node. It continues Middle Persian bē, written BRAʾ / bʾ (Man. MP by), which MacKenzie lists twice: '¹bē [BRAʾ < A brʾ | M P] but; out; ~ … (enyā), except; ~ az: without' and '²bē [BRAʾ | M P, N bi-] particle with verbs, with ō, of indefinable function' — the second is literally Nourai's prefix, and MacKenzie writes the New Persian outcome 'N bi-' himself. Nyberg's entry is fuller: '1. adv. outside … 2. prev. off, out, away, forth … also denoting the perfective aspect … 3. prep. except, but … 4. adversative conj. but … Paz. be, bi, bē; NP only prev. bi-. Original form *bēt, cf bēt-ānak \\\"an outsider, foreigner\\\"', with bērōn 'outside' = bē + rōn. Wiktionary agrees: 'From Middle Persian bʾ /bē/ \\\"out, away, forth\\\" … ultimately from Proto-Indo-European *bʰe' — and the *bʰe meant there is the instrumental particle that yields *bʰeǵʰ- (Skt. bahis, OCS bez), i.e. the root of the OTHER chart on this same page, not the asseverative *bʰē̆. Nourai's 'emphatic' label does capture the perfectivising/emphatic use the particle acquired in late Middle Persian, but the arrow is drawn from the wrong root. (b) baleh/balī are Arabic. Wiktionary: 'بلی — Borrowed from Arabic بَلَى (balā)', and the Arabic entry بَلَى lists Classical Persian بلی balē and Iranian Persian بله bale among its descendants, alongside Ottoman Turkish بلی, Urdu بلے, Pashto بلې and the Kurdish forms — the classic profile of a Qurʾānic particle (Q 2:260, 34:3) spread by Islam. Dehkhoda derives بلی from Arabic بل + a final alif added 'تا سکوت بر آن درست آید', and calls بله 'محرف بلی در تداول فارسی'. Mann's 'Per. ba-lī \\\"yes\\\"' (IEC 59) is a false comparison. The chart's own NOTE therefore resolves in Mo'in's favour: MON is right, IEC is wrong.\",\n     \"derivation_fa\": \"هر دو نیمهٔ این جعبه نادرست است، هر یک به دلیلی. الف) پیشوند فعلیِ «بـ / بی‌» (برفت، بیامد — همان دو نمونه‌ای که نورایی چاپ کرده) دنبالهٔ حرفِ تأکیدِ اوستایی bā نیست، بلکه دنبالهٔ bē فارسی میانه است که در پهلوی کتابی BRAʾ / bʾ و در مانوی by نوشته می‌شود. مکنزی آن را دو بار می‌آورد: «¹bē … اما؛ بیرون؛ جز؛ ~ az: بی‌» و «²bē [BRAʾ | M P, N bi-] حرفی با فعل‌ها، با کارکردی تعریف‌ناپذیر» — و خودِ او برونداد فارسی نو را «N bi-» می‌نویسد. نیبرگ مفصل‌تر است: «۱. قید: بیرون … ۲. پیشوند فعلی: بیرون، دور، به‌سوی بیرون … و نیز نشانهٔ وجه کامل … ۳. حرف اضافه: جز، مگر … ۴. حرف ربطِ استدراکی: اما … در پازند be, bi, bē؛ در فارسی نو تنها پیشوندِ bi-. صورت اصلی *bēt، سنجیده شود با bēt-ānak «بیگانه»» و نیز bērōn «بیرون» = bē + rōn. ویکی‌واژه نیز همین را می‌گوید و آن را سرانجام به *bʰe هندواروپایی می‌رساند — اما آن *bʰe همان حرف ابزاری است که *bʰeǵʰ- (سنسکریت bahis، اسلاوی bez) از آن ساخته شده، یعنی ریشهٔ نمودارِ دیگرِ همین صفحه، نه حرفِ تأکید *bʰē̆. برچسب «تأکیدی» نزد نورایی کارکرد متأخرِ این پیشوند را درست بازمی‌تاباند، اما پیکان از ریشهٔ نادرست کشیده شده است. ب) «بله» و «بلی» معرّب نیستند بلکه خودْ عربی‌اند: ویکی‌واژه «بلی» را وام‌واژه از عربی «بَلَى» می‌داند و در مدخل عربی بَلَى، «بلی» فارسی کلاسیک و «بله» فارسی امروز را در کنار «بلی» عثمانی، «بلے» اردو، «بلې» پشتو و صورت‌های کردی در شمار بازماندگان می‌آورد — الگویی آشنا برای حرفی قرآنی (بقره ۲۶۰، سبأ ۳) که با اسلام پراکنده شده است. دهخدا «بلی» را از «بل» عربی به‌علاوهٔ الفی می‌داند که «تا سکوت بر آن درست آید» افزوده شده، و «بله» را «محرف بلی در تداول فارسی» می‌خواند. «Per. ba-lī» نزد مان مقایسه‌ای نادرست است. پس یادداشتِ خودِ نمودار به سود معین حل می‌شود: حق با معین است و مان بر خطاست.\",\n     \"sources\": [W_BE, W_BALI, W_BALA, A_BALEH, A_BALI],\n     \"ref_check\": [\n      {\"ref\": \"IEC:59\", \"status\": \"partial\", \"note\": \"Mann IEC p.59 does list 'Per. ba-lī \\\"yes\\\"' under 'bha, bho \\\"indeed\\\"' — that is the source of the chart's second word and of the NOTE's 'IEC claims they are Indo-European'. Mann does NOT list the Persian verbal prefix be-/bi- at all, so the first word of the node has no support even in Nourai's own reference.\"},\n      {\"ref\": \"MON:424,577\", \"status\": \"partial\", \"note\": \"Mo'in's print vol.1 pp.424 and 577 could not be read (no usable OCR). Online Mo'in (abadis.ir) gives s.v. بله '(بَ لِ) (ق.) آری، بلی' and s.v. بلی '(بَ) (ق.) بله، آری', with no bracketed origin tag on the 'yes' senses in the web text (the [ع.] tags there sit on the homonyms بُله 'fools' and بِلا). Dehkhoda on the same pages does derive بلی from Arabic بل, which is what Nourai reports MON as saying, so the substance of his NOTE is corroborated even though the printed tag could not be seen.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.vv. ¹bē, ²bē (PHD.txt line 256)\", \"stance\": \"contradicts\", \"note\": \"'¹bē [BRAʾ < A brʾ | M P] but; out; ~ … (enyā), except. ~ az: without.' and '²bē [BRAʾ | M P, N bi-] particle with verbs, with ō, of indefinable function.' MacKenzie's own MP → NP equation for the prefix; nothing to do with Av. bā.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. bē (NYB_vol2_glossary.txt lines 975-978)\", \"stance\": \"contradicts\", \"note\": \"'bē [BRAʾ; Sas. inscr. BLAʾ; Prth. LBRAʾ] … 1. adv. outside … 2. prev. a) off, out, away, forth … b) denoting the perfective aspect … 3. prep. a) except, but … 4. adversative conj. but … Paz. be, bi, bē; NP only prev. bi-. Original form *bēt, cf bēt-ānak \\\"an outsider, foreigner\\\"; MPrs bydwm \\\"outermost\\\".' Also 'bērōn … < bē + rōn'.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in and Dehkhoda via abadis.ir (بله، بلی)\", \"stance\": \"contradicts\", \"note\": \"Dehkhoda s.v. بله: 'محرف بلی در تداول فارسی'; s.v. بلی: from Arabic بل with an added alif.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p.59\", \"stance\": \"supports\", \"note\": \"'Per. ba-lī \\\"yes\\\"' — the source of the chart's IE claim, which the Arabic evidence overrides.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss\", \"stance\": \"silent\", \"note\": \"grep -i 'bali|balê' over HRN.txt returns only بالش/بالست words (balist, balis 'Kissen'); Horn has no entry for بلی, consistent with his excluding Arabic loans.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-83.json','w',encoding='utf-8') as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\n    f.write('\\n')\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk83.py"
}
```


### [2026-09-05T06:39:20.770Z] TOOL RESULT

```
ok
```


## [2026-09-05T06:39:27.041Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 -c \"\nimport json,io,re\np='data/verification/page-83.json'\nd=io.open(p,encoding='utf-8').read()\nprint('stray CJK:', re.findall(r'[一-鿿]', d))\nd=d.replace('bench is the直 native one','bench is the native one')\nio.open(p,'w',encoding='utf-8').write(d)\njson.load(open(p))\nprint('valid json')\n\" && python3 -m json.tool data/verification/page-83.json > /dev/null && echo \"json.tool ok\" && python3 tools/verify_check.py 83"
}
```


### [2026-09-05T06:39:28.775Z] TOOL RESULT

```
stray CJK: ['直']
valid json
json.tool ok
nodes verified: 11/11
node verdicts: {'disputed': 4, 'plausible': 3, 'transcription_suspect': 2, 'confirmed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 8, 'supports': 6, 'not_found': 1}
books consulted: {'supports': 14, 'contradicts': 9, 'partial': 9, 'silent': 9} | by book: {'IEC': 7, 'POK': 6, 'AHD': 6, 'PHD': 4, 'NYB': 3, 'MON': 3, 'HRN': 3, 'SYN': 3, 'KLN': 2, 'ARY': 1, 'SKT': 1, 'BRT': 1, 'KNT': 1}
```


## [2026-09-05T06:39:35.269Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN bali\"; grep -n -i \"bali\\|balê\\|balî\" HRN.txt | head -8; echo \"=== KNT ba particle\"; grep -n -i \"\\bbā\\b\\|Beteuerung\\|asseverative\" KNT.txt | head -8; echo \"=== AHD bhe indeed\"; grep -o -i \"bhē[^ ]\\{0,3\\}\\. [A-Z][a-z]* [a-z]*\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-05T06:39:36.874Z] TOOL RESULT

```
=== HRN bali
=== KNT ba particle
=== AHD bhe indeed
```


## [2026-09-05T06:39:43.980Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 -c \"\nimport io\np='data/verification/page-83.json'\nd=io.open(p,encoding='utf-8').read()\nold=\\\"grep -i 'bali|balê' over HRN.txt returns only بالش/بالست words (balist, balis 'Kissen'); Horn has no entry for بلی, consistent with his excluding Arabic loans.\\\"\nnew=\\\"grep -n -i 'bali|balê|balî' over HRN.txt returns nothing at all; Horn's Grundriss has no entry for بلی, as expected of a work that excludes Arabic loanwords.\\\"\nassert old in d\nio.open(p,'w',encoding='utf-8').write(d.replace(old,new))\nprint('patched')\n\" && python3 -m json.tool data/verification/page-83.json > /dev/null && python3 tools/verify_check.py 83"
}
```


### [2026-09-05T06:39:45.809Z] TOOL RESULT

```
patched
nodes verified: 11/11
node verdicts: {'disputed': 4, 'plausible': 3, 'transcription_suspect': 2, 'confirmed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 8, 'supports': 6, 'not_found': 1}
books consulted: {'supports': 14, 'contradicts': 9, 'partial': 9, 'silent': 9} | by book: {'IEC': 7, 'POK': 6, 'AHD': 6, 'PHD': 4, 'NYB': 3, 'MON': 3, 'HRN': 3, 'SYN': 3, 'KLN': 2, 'ARY': 1, 'SKT': 1, 'BRT': 1, 'KNT': 1}
```


## [2026-09-05T06:40:04.153Z] AGENT

Page 83 (book p. 53) verified — `data/verification/page-83.json` written, `verify_check.py 83` shows **0 PROBLEM lines**.

Counts: 2 roots (both `confirmed`); 11 nodes — `confirmed` 2, `plausible` 3, `disputed` 4, `transcription_suspect` 2. Ref checks: 6 supports, 8 partial, 1 not_found. Books consulted: POK, IEC (Mann), AHD/Watkins, WLD, SYN (Buck), KLN, SKT, PHD, NYB, BRT, KNT, HRN, MON/Dehkhoda, ARY. Page image copied to `data/verification/sources/refs/ocr/BOOK/83.png`; 13 web pages archived via `fetch_source.py`.

Disputed / suspect items:
- **Bhe #1 `a-pâč`** (disputed) — MP abāz (ʾpʾc) is real, but Nyberg: `< *apācā … from OIr *apānk- … derived from Av. apa`, i.e. PIE *h₂epo, not *bʰeǵʰ-. Wiktionary calls the *bʰe+*-ǵʰs route "less likely".
- **Bhe #3 `bejoz`** (disputed) — بجز = بِ + جز (Dehkhoda: "از: ب + جز"); جز < MP *jud az* (MacKenzie: "~ az [N juz]"), Av. *yūta-* (Horn no. 418). Mann's "Per. bajuz" under *bʰeǵʰ-iḱs is a chance resemblance.
- **Bhe #4 `bôhyah`** (transcription_suspect, `error_in: book`) — no Sanskrit *bôhyah*; correct is बाह्य *bāhya-*, and Nourai's own source prints "Skt. bahyah". Printed page shows `bôhyah`, so the extraction is faithful — the book's misprint for `bâhyah`.
- **Bhe #5 `Bheg`** (disputed) — welds two roots: Mann's queried *bhéǵho* 'oust' (IEC 70) and Pokorny's separate *bheg-, bheng-* 'break' (IEW 114-15). Pokorny derives neither from b(h)e/b(h)eǵh- (112).
- **Bhě #1 `bâ, bě, beî`** (transcription_suspect, `error_in: book`) — bā/bē are genuine; `beî` is not Avestan: either a garbling of bōit̰ or Lithuanian *bei* mis-labelled (both stand a few words away in Pokorny 113 / Mann 59).
- **Bhě #4 `bî-, be-` / `baleh, balî`** (disputed) — the verbal prefix continues MP bē 'out, away' (MacKenzie "²bē … N bi-"; Nyberg), which belongs to the *other* root on this page; بله/بلی are Arabic بَلَى (Wiktionary, Dehkhoda). The chart's own NOTE resolves in MON's favour.

Extraction errors for the owner: **none** — the JSON matches the printed page everywhere, including `bôhyah` and `beî`.
