# Verification process log — verify-page-372


## [2026-09-07T20:16:12.884Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 372 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-372.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-372.json. Write /home/sfmqrb/git/rishe/data/verification/page-372.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 372` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:16:14.942Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:16:15.654Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:16:15.668Z] TOOL RESULT

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


## [2026-09-07T20:16:16.211Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-372.txt"
}
```


### [2026-09-07T20:16:16.231Z] TOOL RESULT

```
1	=== PDF page 372 (book page 342) ===
2	--- entry 0 ---
3	ROOT Obhi -> redirect to Ambhi
4	--- entry 1 ---
5	ROOT [Indo-European] Oies : pole  (refs WLD1:167)
6	#1 (parent #0) [Avestan] refs=SYN:496; BRT:32 | aeša 2 : pole, plow shaft
7	  #2 (parent #1) [Persian] refs=HRN:114; BQT:803; MON:1465 | xîš 2 «خیش ، خویش ۲» : plow or wagon pole ; xîškâr «خیشکار ، خویشکار ۲» : farmer
8	--- entry 2 ---
9	ROOT Oi-no -> redirect to I 2
10	--- entry 3 ---
11	ROOT [Indo-European] Okto : eight  (refs POK:775)
12	#1 (parent #0) [Avestan / Old Persian] refs=POK:775; KLN:504; GPL:41 | ašta 3 : eight ; ašta-dasa : eighteen ☞Dekm ; aštâti, aštaiti : eighty
13	  #2 (parent #1) [Persian] refs=BQT:2238 | hašt «هشت» : eight | extra: هیجده ، هشتاد
14	#3 (parent #0) [Germanic] refs=AHD | ahtô
15	  #4 (parent #3) [English] refs=None | eight, eighteen, eighty
16	#5 (parent #0) [Greek] refs=AHD | oktô : eight ; oktô-pous : eight legged ☞Ped
17	  #6 (parent #5) [French] refs=None | octopode
18	    #7 (parent #6) [Persian] refs=MON:164 |  «اختاپوس»
19	#8 (parent #0) [Latin] refs=AHD | octô
20	  #9 (parent #8) [English] refs=None | October, octagon, octave
21	#10 (parent #0) [Sanskrit] refs=DVS:130 | astâu : eight
22	
```


## [2026-09-07T20:16:19.717Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-372.json",
 "description": "Read source JSON for page 372"
}
```


### [2026-09-07T20:16:19.757Z] TOOL RESULT

```
{
  "pdf_page": 372,
  "book_page": 342,
  "entries": [
    {
      "root": {
        "name": "Obhi",
        "redirect": "Ambhi"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Oies",
        "lang": "Indo-European",
        "refs": "WLD1:167",
        "gloss": "pole"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SYN:496; BRT:32",
          "words": [
            {"translit": "aeša 2", "gloss": "pole, plow shaft", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:114; BQT:803; MON:1465",
          "words": [
            {"translit": "xîš 2", "gloss": "plow or wagon pole", "script": "خیش ، خویش ۲"},
            {"translit": "xîškâr", "gloss": "farmer", "script": "خیشکار ، خویشکار ۲"}
          ],
          "note": null,
          "quote": {
            "text": "کنم چاه آب اندرو صدهزار - توانگر کنم مردم خویش کار",
            "poet": "Ferdowsî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Oi-no",
        "redirect": "I 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Okto",
        "lang": "Indo-European",
        "refs": "POK:775",
        "gloss": "eight"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:775; KLN:504; GPL:41",
          "words": [
            {"translit": "ašta 3", "gloss": "eight", "script": null},
            {"translit": "ašta-dasa", "gloss": "eighteen", "script": null, "see": ["Dekm"]},
            {"translit": "aštâti, aštaiti", "gloss": "eighty", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2238",
          "words": [
            {"translit": "hašt", "gloss": "eight", "script": "هشت"}
          ],
          "script_extra": "هیجده ، هشتاد",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "ahtô", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "eight, eighteen, eighty", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "oktô", "gloss": "eight", "script": null},
            {"translit": "oktô-pous", "gloss": "eight legged", "script": null, "see": ["Ped"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "octopode", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:164",
          "words": [
            {"translit": null, "gloss": null, "script": "اختاپوس"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "octô", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "October, octagon, octave", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "DVS:130",
          "words": [
            {"translit": "astâu", "gloss": "eight", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T20:16:21.000Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['WLD','SYN','BRT','HRN','BQT','MON','POK','KLN','GPL','AHD','DVS','PHD','NYB','HUB','IEC']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-07T20:16:22.345Z] TOOL RESULT

```
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

GPL {"title": "J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911", "edition_found": "1911", "kind": "archive_djvu", "url": "https://archive.org/details/grammarofpersian0000plat", "identifier": "grammarofpersian0000plat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt", "page_offset": "leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Grammar organised by n

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

DVS {"title": "P. Davies, Roots: Family Histories of Familiar Words, McGraw-Hill 1981", "edition_found": "1981 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/rootsfamilyhisto0000davi (lending)", "identifier": "rootsfamilyhisto0000davi", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<word>.", "notes": "RE-SEARCH 2026-09: borrowable only."}

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open
```


## [2026-09-07T20:16:30.489Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80; echo ---; sed -n '1,80p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T20:16:30.540Z] TOOL RESULT

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
```


## [2026-09-07T20:16:31.930Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['WLD','SYN','BRT','HRN','POK','KLN','GPL','DVS','MON','BQT']:\n    v=d.get(k) or {}\n    print(k,'|local:',v.get('local_file'),'|offset:',v.get('page_offset'),'|hint:',str(v.get('lookup_hint'))[:300])\n    print()\n\""
}
```


### [2026-09-07T20:16:33.378Z] TOOL RESULT

```
WLD |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] |offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). |hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.

SYN |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt |offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.

BRT |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt |offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.

HRN |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt |offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

POK |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt |offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv

KLN |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

GPL |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt |offset: leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Grammar organised by numbered paragraphs (§); grep the paragraph number or the Persian word in transliteration.

DVS |local: None |offset: None |hint: Borrow via IA lending; in-book search ?q=<word>.

MON |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe

BQT |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] |offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
```


## [2026-09-07T20:16:40.700Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full lemma okto ===\"; grep -n -i \"lemma: ok\\?tō\\|lemma: okto\\|lemma: oktōu\\|okto[uw]\" POK_full.txt | head -20\necho \"=== POK_02 p.775 (leaf = p-344 => 431) ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=430 && NR<=432 {print \"----LEAF\",NR\"----\"; print}' POK_02.txt | head -120"
}
```


## [2026-09-07T20:16:41.887Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 p.167 => leaf 176 (1-based) ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=175 && NR<=177 {print \"----LEAF\",NR\"----\"; print}' incoming/WLD/WLD_Bd1_pages.txt | head -150"
}
```


### [2026-09-07T20:16:42.014Z] TOOL RESULT

```
=== POK_full lemma okto ===
=== POK_02 p.775 (leaf = p-344 => 431) ===
----LEAF 430----

----LEAF 431----

----LEAF 432----
```


### [2026-09-07T20:16:43.319Z] TOOL RESULT

```
=== WLD Bd1 p.167 => leaf 176 (1-based) ===
----LEAF 175----
                                                     ;




166                                                  oid-



oid- ..schwellen".

  Arm. ait (?-St.) „Wange“, aitnum „ich schwelle", aitumn ..Gescliwulst"
(Hiibschmann Arm. Gr. I 418).
     Gr. oldaco, oldsco „schwelle“, oldo                 n.   ..Geschwulst", oidat; ..unreife Feige“,
oldfza „ Aufschwellung, Scli\vall“.

  (Fern bleibt air. oil „Wange“ Stokes KZ. 35, 595); ahd. exj, nbd. mdartl.
Eis „Eiterbeule, Geschwiir", und als Bezeichnung von deren giftigem Inhalt
ahd. eitar , ags. dl(t)or. aisl. eitr ..Eiter" (aisl. auch ubertragen „Raserei.
bitterer Sinn“, ostfries. eitel „zornig, rasend"): aisl.   extill m. ..EinschluB in

einem Stein", norw. eitel ..Druse, Knorren am Baum, Knoten, Knospe“
                                                                11
(= mhd. ei$cl „kleines eiterndes Geschwiir       aisl. eista „Hode“ ( *oid-s-to(n )-,
                                                                     ;


von der Tiefstufe des es-St., gr. oldo?; s. u. slav. isto, *esto); vielleicht
auch ags. ate, engl. oat „Hafer“ (Binz ZfdtPli. 38, 369 ff. nach Skeat, vgl.
dann zur Bed. unten mss. jddrica ..Gersten-, Hafergriitze"), lett. idra „das
faule Mark eines Baumes", idrudt „einen faulen Kern bekoinmen“; mit slav.
V-, *ja- aus oi- (lautlich von Bruckner KZ. 46, 202 mit Unrecht be-
stritten) wohl abg. ->'dro, jadro (usw.) ..sinus   velum, Segel, poln. kaschub.
                                                                         ;


auch Netz" (Gdbed. „Sch\vellung“ gegen Bernekers 270 f., 442 Zerlegung
                                                 ;


in zwei versch. Worte s. Briickner KZ. 45, 317 f., der aber irrig auch slav.
       russ. jadro „Kern“ damit gleichsetzt; andere Deutungen von slav.
ji-clro,

jadro s. bei Berneker aaO., Mikkoll Ursl. Gr. 47),
     Yermutlich auch nhg.jadz ..Gift" (mit iibertragener Bed. „Zorn, sich giften".
                                               wenn lit. aidinti „reizen“ nach
slov. jiuhti „argern“, skr. ijediti ..erziirnen";
Bezzenberger BB. 27. 172 anzuschlieBen ist, entschiede es fur Entstehung
von slav. jadz aus *oidos und gegen die von Berneker 271 als zweite
Moglichkeit zugegebene Herkunft aus *edo- zu ed- ..essen". etwa wie Gift
zu yeben) und ksl. isto, pi. istesa ,,Hode, Niere" aus schwundstufigem *id-
s-fo-, woneben *oid-s-to- ( aisl. eista) vielleicht in aruss. jestesp n. Du
                                      ;




„lIoden“,  wenn damit *<r-stesp gemeint ist (s. Berneker 434); lit. hikstas
..Niere", apr. inucze (recte *hixte) ds. wiirde. wenn hierhergehorig, Nasal-
infix und parasitisches      zeigen is. Berneker 434, Trautmann Apr. 347
                                /.'



m. Lit.;      auch   u.   *en, *nifos     „in.       drinnen").               Wenn man eine nasalierte
Wzf. *ind- und deren Entw. zu *<d- (jcd- ) auch fiirs slav. anzunehmen
berechtigt ist, wiirde auch si. *jedro, *jedn in abg. jcdro ..schnell" (aus
        = „*geschwollen‘ ), russ. njadretb „stark werden. sich kraftigen;
,,*stark“                         l




schaumen, brausen, perlen (von Getriinken)“, skr. jedar „voll, kriiftig, frisch.
stark" und r.-ksl. jadro ..nucleus, testiculus", r. jadro „Kern“, jadrovityi
..kernig,    stark", jddrica ..Gcrsten-,                 Ilafergriitze",            poln. jadro „Kern; pi.
Hoden", jedrny ..kernig, kriiftig, riistig" (usw..                           s.   Berneker 455 f., Bruckner
KZ. 45, 317f.) viel einleuchtenderen AnschluB                                     hier finden,   als   beim iso-
lierten     gr.   ddgo? „voll ausgewachsen.                    reif,         stark,    dicht",   mit denen   sie
von Fick I 4 363. Prellwitz 2 s. v. (beidc mit unvereinbarem) und Berneker
aa(). (wo weitere Lit.) verbunden werden.

  Fick KZ. 21, 5, 463, Bugge Jbb. f. Phil. 105. 91. Fick 1 4 359, III 4 2
Falk-Torp u. odder, eiste. eitel.
     Lat. uemidus ..tumidus, zieq-vo>jfievog“ (Gloss.; mangels literarischer Be-
lege    ist die ursprgl. Bedeutungsfarbung nicht feststellbar), das Fick
                                                                             und

----LEAF 176----
             -          m                                                           ,




                                                    ojes             oui-s                                                    167

Bugge aaO. unter einem Ablaut ai         oi anreihten, vermag einen solchen
                                                             :



SchluB nicht zu stiitzen; vielleicht als „vor Hitze oder durch Yerbrennung
gedunsen“ nach Froehde BB. 5, 273 zu aiclh- „brenneir‘, lat. aedes, aestus.
—   Nicht geboten scheint es mil-, dt. Eis, Eiter lett. klra, slav. j<uh mit
Bezzenberger BB. 27, 172 aus obigem Yerbande zu losen und zu einer
versch. Sippe mit der Bed. des ..krankhaften Einschlusses“ zusammenzufassen;
denn dieser Begi'iff ist aus „Geschwulst“ ohne weiteres zu gewinnen (siehe
Binz aaO., Yf. LEWb. 2 u. aemulus ), und die lett. Anwendung auf faules
Mark ebenso aus „gequollen“ (Berneker 270 f.).

Oies- „Stange, Deichsel“                (
                                            :ois-:ts- ).
    Slov. skr. cech. oje             „Deichsel“
                                   (St. ojes-, gen. slow ojese)  bait. *aisd                                    ;


als Quelle von finn. wot. (usw.) aisa ,,Stange der Gabeldeichsel, Femer-
stange“ = gr. *oi[a]d m. oh'fiov „Steuerruder“. att. oiaf, -y.og „Griff des
Steuerruders, Steuerruder“, hom. ohjaeg _.,die Grille zu beiden Seiten des
Joches“ (s. zu dieser Bed. Bechtel Lex. 244 f., ai. lift „Deichsel‘', Bezzen-
berger GGA. 1896, 966, Liden Stud. 60 ff. (verfehlte Weiterungen            gr.                                        —
okovog usw.             —
                   bei Sadel IvZ. 43, 245 ff., s. auch unter *eis- „sich heftig
bewegen").      Liden vermutet neben oi-es- stehende en- und fir-Stamme
*oi-en- (vgl. slav. oko, ocese ,Auge“; ok-no „Fenster“) und oi-( ijr- (vgl.
                                               ;


ai. udhar    udhndh) in lit. lena. meist pi., auch ietie, -vs .Gabeldeichsel,
                    :
                                                                                                           ,


Deichsel am Einspanner, Handhabe am Schubkarren“ und in aisl. ags. dr
„Ruder“ (eig. „*Stange“), die nach Ausweis der L\v. finn. a iro und lett.
airis, ahr, lit. vairas „Ruder“ (die bait. Worte kaum urverwandt) auf urgerm.
*airo beruhen; bei der Vereinzelung der beiden Bildungen unsicher. (Andere,
aber verfehlte Deutungen von germ. *airo verz. Falk-Torp u. aare I).


oui-s       ;
                ,Schaf“.

      Ai. act- m. „Schaf“, avika- m. ds.. avika ,,weibliches Schaf                                     1
                                                                                                               (= abg. ocsca),
dvga-  „vom Schaf“, vgl. gr. oia; gr. on, olg (argiv. an. pi. d firs') „Schaf“,
ol'eo? „vom Schafe“, oi'a, da „Schaffell“, dehnstufig gia, dm ,.Schaffelh‘ (wie
```


## [2026-09-07T20:16:54.800Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"$f leaves: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) bytes: $(wc -c < $f)\"; done\necho \"=== grep okto in POK_full ===\"; grep -n -i \"oktō\\|okto(u)\\|ok'to\\|oktōu\\|okto\" POK_full.txt | head -20\necho \"=== grep 'acht' lemma ===\"; grep -n \"lemma: ok\\|lemma: o.to\" POK_full.txt | head"
}
```


### [2026-09-07T20:16:56.109Z] TOOL RESULT

```
POK_01.txt leaves: 363 bytes: 981836
POK_02.txt leaves: 433 bytes: 1137861
POK_03.txt leaves: 429 bytes: 1170809
=== grep okto in POK_full ===
1980:to- participle: OKToq, Latin actus' put in motion, moved, driven, tended, conducted', *amb 
34209:yAaKTO-cpayoc;), out of it *yAaK, *yAaKT6(; (hence yAaK(I)VT£(; psaroi yaAoKTOc; Hes. and 
63509:6KTCji)(Kai)5£Ka, Latin octodecim. Old High German aMozehan^8^, gr. OKTOKoaioi, Latin 
65570:pecem, pec/ds., etc.; Old Church Slavic pekb'heaV, potb 'Schweift' ( *pokto-), pestb 
80739:side'; gr. poKToi cpapavYSc; Hes. besides secondary panrai ds. 
=== grep 'acht' lemma ===
15907:lemma: ok"-: to see; eye. According to gr.s -k'^> -p, -g'"> -b. 
18274:shine, shimmer + zero grade of Root/ lemma: ok"-: to see; eye 
24247:coal < Root/ lemma: ok"-: "to see; eye' 
30181:lemma: gel-1\ "to curl; round' into gleg- + Root/ lemma: ok"-: "to see; eye'. 
63386:Root / lemma: ok- 
63392:Root/ lemma: ok-: 'to think over, *understand, see' derived from a reduced Root/ lemma: 
63416:Root/ lemma: oRtd(u)\ eight derived from the extended Root/ lemma: ok-\ "to think over, 
63517:Root / lemma: ok"- , {*{*hek'^h- ) 
63525:Root / lemma: ok"- : to see; eye derived from Root / lemma: deik- : to show' : Root / 
63893:coal < Root/ lemma: ok"-: "to see; eye'
```


## [2026-09-07T20:16:56.650Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT search aesa / Deichsel ===\"; grep -n \"Deichsel\" BRT.txt | head -20\necho \"=== BRT leaf structure near col 32 ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=25 && NR<=30 {print \"----LEAF\",NR\"----\"; print substr($0,1,3000)}' BRT.txt | head -160"
}
```


### [2026-09-07T20:16:58.008Z] TOOL RESULT

```
=== BRT search aesa / Deichsel ===
2777:(Kaus.)  aisaya-,  adaya-.  —  Inf.  'istS;  Absol.  |  np.  xn,  KSs.  ii;  vgl.  tfi-  f.  'Deichsel'.  —  Pü. : 'ihmnitn.  \      "i  so  nach  Ga.  (und  Dst.),
29969:•  j.  ^ham.ivä-  f.  Name  eines  Teils  vom  Ge- schirr des  mit  Pferden  bespannten  Wagens, vli  'Deichsel':  äal  ti  (näml.  aurvants)  vXspa /rü.yuxta  'vqmca  simqmca  simöihrqmca dirita  huhr^la  ^upairi.späta  aka  bastom "und  die  (Renner)  sind  alle  angeschirrt an  die  Deichsel  und  den  Halsring  und das  Joch,  die  mit  dem  aufgespaltenen wohlgefertigten  üb  ergesteckten  Zapfen  zu- sammengehalten sind"  Yt.  jo.  ia5(?).
=== BRT leaf structure near col 32 ===
----LEAF 25----
3-
77  ■■  Ytp.  18.
9  :Y.  3. 6,  37.3«.
34:YL/.34-
79;Vt5.i8.
\l:\.6l.6.
S:?j/-,r"-
81:  V.p.  14.
ij!Vt7j.  39.  SrB.5.
84tVtJ.i8.
i3iA.7.i.
41.  43:  YtJ.49-
8s.86;Vt/j.99.  '00.
I.  1  :  Y.  7. 1.
4S.47:  Yt.5.  «8,  104.
87  ;  Yt  J.  109.
3:V.3.3,  II.5-*-»;Z-
49.  5»  :  Yt  9.  29.
89.  90 -Yt/p.  11-13.
3.1  :Y.7.  17,  33,  A.J.19.
so,  s:  !Yt^3<^  3«-
97tYt/p.o.
6'Y.jJ.5.
db,Google
XVUI
Die  awestischcD  Text«.    Konkordanz
7:  A.J.  8-12.
17(57).  18  (s8):  V.J.  48, 49
42  (1121  :V..^.  21;  *20.
S-i2.\.s.7-
.9  (60):  V.J.  20.
43  (115);  44(118);  45(123);
ig:  A.  3.1.
20   63):  V.J.  19,  S- 49-
46  (128);    47  (131);   48
A.i:Y.i.4,^3.
31  (68h  V.J.  26,  p.  SO.
(134);  49  (137)-
a  :  V.  /.  18,  S.  /.  I.
22  (73):  V.J.  12.
50  {i43):V../.si-54.
3:A.4.&,V.43lo-
23  (75):  V.J.  4,  22.
51  {146)-54(154):V.4.S0.
SiVt/agi.  A.4-7-
*»  (79)-
54  ^V.  4- SS-
T.k.4-  5-
25  (84):  V.J.  26,  28,    /■9.23
SS  (156)  :V.  4. 13.  54.
i:k.4.3.
Yl.  //.  22.
8.i;i(7>
26  8       V.J.  25,  28.
3(I2):V.5.6.
Videvdat.
27  8
28  9       V.J-^S.  ^6-
4   13) -V.J.  7.*.  34. 5(16).
1.1.
29  9       1°  (96).  31  (99).  3
6(20),  7  (21):  V.J.  3,  4.
X  (5):  V.A4-13,  IS-i
9-
(        .  33  (111).
8  (24J  ■■  V.  5.  9.
3(9);  4  {13);  5(17):  6
21);
34  [1          V.J.  12,  35-
9  (30):  V.J.  8.
7(25);   8  {29);    9
33;
3S  tl         V.J. 34.
10  (35),  11  (38>
10(37);  11(41);  12
45);
36(1        V.j.37.38. 'J-I5
i2i42):V.j.i3,  *.9.
13  (49)-
37(1     .    V.J.  36,    4.16,   6
13  (45):  V.J.  12,  ÄJO.
4-13  :V.^.  2.
25,   Ä  25,   13.  4,  7j.  74
'•*^'''       ..     >
"4  (53);    15  (59);     16 17(67);  18(72);  19
63);
38(i3o):V.j.36,  J.27.
'S   SO,  16  (52):  V.J.  17, 18. 17  (54),  18(56):  V.J.  15,  16.
(76)-
39  (135):  V.J.  27.
15-19  iV.  2.2.
40  (137X  4"  ("4*).  At  (149)
19  (57  .  :=■>  (6i)-
2ä  (81).
V.  J.  28-30).
21    64  :V..*ÄS.V.ro.  18,19.
2.i;=»(4)-
4.1;  2(4);  3  (13);  4  (16).
22    69  :  V.J.  23-25.
3  (7):V.2.4,  5-
5  (i^):\.4-6-ia.
23  (70  -V.J. 22,  24,  25.
4(n)-V.s.3-
6(26)-.o{34);V..^.S.
24(72  :  V.J.  22,  23.
5  (14   :  V.  2.  3.
U  (36):V.  V.  Ia-i6.
25  (74l:V.J.22,  23.
6    17  ;  7  (19).
i2(39):V.^.n,  6.23,  J.24
26  |79l:V.J.21.
27  (83):o-30,  33-  36.  39,7-
9  (20}  =  V.2.9.    16,   25
3*-
13.  14.
S-io-V.2.12-14.  16-
18.
i3(42):V..#.ii,  55,  /J.13.
^'  ',?■
9!V.a.8,  17.
rS-S*-
27-30!V.7.s-8.
10  :  V.  3. 18.
i4{4S):V../.u,Ä26,/j.i2
28  187J:  V.J.  29-32.
29  (93)-32  (105):  V.J.  28.
1 1  :  V.  s.  IS,  19.
IS  (48):V.4.  11.
12  (23)-I4  :  V.  3.  8-10.
i6(5l);V.j.37.  V.U-
33  (109):  VJ. 34-36.  /2.21.
1S-V.2.U.
17  (54).
34(111   :  V.J.  33-
16  (26V18  (31).  V.?.  8
10.
i8is8):V.^.22,  26,30,34,
35  (114):  V.J.  33,  36.
I9(37rv.3..:.
37.  40.
36(ii6):V.J.33,  35.  38-
20(42):V.2.2l.
19  (63);  V.4.23,  27,  31,  34,
36-38  (121)  :V./2.  22-24.
2i:V.2.ao.
37.40,  fi.  11,  13,15.17
2
----LEAF 26----
:  V.  6  1,  4-
12  (38):  V.J.  13,  22,  23
.  34
36  (96)  ;V..*.  21;  ^.20.
4    7   :V.Ö.3-
13  (4i):V.j.9.   [2.
37  (99):  V. ./.  18,  19.
5    9);V..*.20.
14  (44):  V./.  24,27,5,1
3,41.
38  (I02) :  V.  4.  20.
```


## [2026-09-07T20:17:05.716Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2740,2830p' BRT.txt"
}
```


### [2026-09-07T20:17:05.769Z] TOOL RESULT

```
kommt;».  No.  3.  -  ')  llnthem.(?).  -  3)  S.  Y\.ig.$(>;iz;  —  apatat  /raarase  :^ar7n5
No.   t.  —  1)  Das  wegen  des  r  als  gelW.  an-  isö  zara'iuiträi  (als  Gen.)  YL/9.82;  56;
zusehen  isi.  —   äat   vö    kasäl    ma^anqm  .  .  :^ar)nS
•  j.  aesmö.barvtay-  f.  'Darbringuog  von  isa^ta  Yt.  i^.  53;  — yff  naeeim  isaiti  huna- Brennholz':  alvayacif  °niii  (IS.)'*  aiva-  ranqm'V.ij.i9;Aog.48;  —  äiä ..Ayämii , . yacit  bar7sm3.stir?iH  Y.24~  aiavanö  tnsyä  istsm^^  rJiVl'(sd,)  Y.  40. 4;
Pü.!  fsm  bariiniA.  —  D  Hds.  'u.  __  _ya;ja  /g^  isaaa  Vyt/2(?)  a)   mit
•  j.  aesmö.zasta-  Adj.  'Brennholz  in  der  Dat  'etwas  (Akk.)  haben  wollen,  begehren, Hand  haltend,  mit  Brennholz  in  der  Hand' :  erstreben  für  -':  yö  . .  tanuye  tsaite  >rä- yas3  ^WJ  .  .  frayazaite  "stö  Y.62.1;  V.  ^r^m  V.  ij,  19;  —  ä'irava  .  .  manmtam 3.1.  isimtiö  dalnayäi   am^m   iamnö  tanuye
Pu.!  ista  dail.  YtlO.lT,  ig'; — a>re  aesmqn   isailt  "fürs
•  j.  aeza-'*Ad]'.'verlangend':aätf(s.°3aÄ-)  Feuer  will  er  Brennholz  haben"  V.5. 2; jasal?m  'sähe  Yt/p,  82.  —  vaAUtä    isasä    mananhä  maibyö   x/a-
Zum  V.  äi-i),  Praes.  i^a-'X  —  ai.  f-ia-OAdj.  l^r)m  aojöngkvat  "so  erstrebe,  O  VM.,   für
—  O  Wegen  des  Diphthongen  in  aiza-,  tha-  mich  das   starke  Reich"  Y.^/.4.         3)  mit
S.BTHL.IF  5.216    -    »Falsch   IF.  j.  2.7  dopp.Akk,:  'Jemand  verlangen  als -,  von
(wegen  ai.  ingayati).  .,    '^'^    ..       ,     ■'  ,  ?  ,         -1,
.      _  ,,  .        „  1  ihm  wünschen,  verlangen,  dass  er  (..sei)  ;
.  ).  aeza'xan-  ni  Name  emes  Bergs  oder  ,„„^„,j„^  „  f„„  „„„-J  ,f^^  . .
Geb,rgs:  ii™/te«^«r«,./ra«»o.a»..^^j„    «/««i  garia^am    ytij.^'i    —
i^/^-    n.  'BrennhoU',    an.    asa  'Glutasche';  uiroiustriM    \t.l6.iy,    —    sarait^trä 85jl.  8)  +j-,rn-  f.  'Quelle';  eig.  also  „Glut-,   urva^im  ^nitlDm  «öfV  "vom  Freund  soll
ob,Google
19
'aes-  4
'aeä-  No.
30
Z  verlangen,  dass  er  (dem  Freund)  Schutz gewähre"  Y.  7/.  13,  a)  statt  des  praed. Akk.  ein  Adv.:  yimS  avai^a  ktrsnaot yaia  dim  Ual  ahurö  mazäi  "V.  tat  so, wie  es  AhM.  von  ihm  verlangte"  V.  2. 31.  4)  spez.  'zu  hören  verlangen,  hören wollen':  ^J  tsi  asä  yi  asäi gius  ia/.i  (sd.) mraot  is3ntl  tnä  tu  isi  vohB  manaaAl "was  ,  .  kund  getan  hat,  hören  wollen  sie dasdurchdeinenKji/."  Y.4Ö.9.  a)  ohne Ob],":  at  tä  vaxfyj  is?ntd  "ich  will  davon reden  zu  denen,  die  hören  wollen"  Y. _jo.i;  47-6*>;  — yalüä  asnat  yaila  anrät (sd)  isa:iä  Y.  45- 1-  5)  'Jemand  (Akk.) angehen,  sich  an  ihn  wenden,  ihn  bitten': ise  'i/wqm  aAura  mazda  ptrsst  '^wqm  . . Yt  12. 1 ;  —  *yas»  tat  *afivataiti  (sd.) paranlarfm  (sd.)  isöit  N./2;  —  vayö  .  . harn  istmmm  painyätte  ".  .  stellt  sich ein  bei  dem,  der  sich  (an  ihn)  wendet" Yt-/>S3;  —  al  yastim  nsii  na  is7mnS (inpass.Bcd.)9*Jj'i7/(sd.)Y.4ö.6.  a)  mit Inf.:  amslacit  .  .  avaiahe  isinli  masya- kanhs  "die  ^Ienschen  bitten  die  Am.  um Beistand"  Aog.  41.  6)  'Jemand  (Akk.) angehen  (in  feindlichem  Sinn),  angreifen, nachstellen';  avae^amai  ^iff  pantö  yim isfnli    mi^röjiruiS  Yt.  io.45.  7)    'er-
fahren, erlangen,  teilhaftig  werden':  ye/iyä savä  (sd.)  isänti  radat^ks  . .  Y.4^.7;  — ia'iä  . .  *rilnyS.si3rntlm  (sd.)  gam  isasöit
Y.50.2.
mit  a/a  — ?— :  ya  aäagiqm  *öim  kucit upöisäl  aUavat  apayalsa^"'*  N.  lOg.
mit  aibl  'sich  bemühen  um  — '  (Akk.): yi  aham  (sd.)  Hasqs  aibj  V. 51,19.  '
mit  upa  i)  'etwas  suchen,  wonach suchen',  mit  Akk.:  hat  aitaSsqm  ..  käHt ufaitätl  yavat  (sd.)  ha&r>m  "auf  welche  , Entfernung  .  .  soU  ei  von  ihnen  welche  ] suchen?  .  ."  N.  log;  —  antar»  käisnmcitx *iiat  artya  (sd.J  upaisöit  N. /0(j;  — yö\ aäagiqm  *öim  käcit  *upöisät"^  .  .  N. , lo^f?);  a)  ohne  Objekt:  yezi  nöit  updi- laiii"''.,  "wenn  er  nicht  (danach)  sucht,.."] N.  ;09;  —  yö  *updisöit"^  nt)it  *vinatti  \ "wer  (danach)  sucht,  aber  nicht(s)  findet"  | N.  10g.  2)  'etwas  ausfindig  zu  machen  | suchen  für  — '  (Dat):  ava'ha  hg  baisazam  \ (sd.)  upöisaypn"^  ya'^a  dahmätcst  V. /j. , 35-  3)  'etwas  wünschen':  yöi  ..  aoäilye.-  \ draonaahasca  *k>ntS  däitim  gius  draonS upa.il i mnö  (stall NP.) [avä\  avankabditUi
(sd.) N.52 ; 53{yio*up5is»mne)  ■".  4) 'Jem. besuchen,  sich  einfinden  bei  — ';  upä  tu  (sd.) nö  ioa  yti  asaonqm  nwsu*i>:^ntö{iVlk)"^ /ravasayd  Ylij.  146.  a)  insbes.  'einen Lehrer  besuchen,  zu  ihm  in  die  Schule gehen':  ivat  nj  *ai^rapaitint  (sd.)  upöi- sät"^  N. /j;  —  ..  *ainim  ai%rapailim (sd.)  upsissi/^'''  a'ia  "i^ritTtn  upsisöil  ai- va'ha  ioirim  upäisi}it"1^.ii.  5>'erfahren, '  erleben' :  upa  aBqm  xiapamm  üvavat  sätüis urva  *  Haiti  yaia  .,  H,  2.a.
mit  paiti  i)  'streben  nach  — ,  begeh- ren': a)  mit  Akk,:  tafca  yä  kasu.xratul ,  masyöjcrdkwqm  (sd.)  nöit  paitiSaiti  V.  7, I  59.  b)  mit  Gen.:  s.  AbsoL  a)  'sich befleissigen,  betätigen',  mit  Akk.'>:  paiti- sata  (2P.)  mazdayasna  sraoiahe  a/yeke '  yasmm  Y.  37. 13;  —  staota  yesnya  yaza- maide  .  .  dadräna  paitHäna  paitiima- .  r^mna  Y.  55. 6 ;  —  six/anlfm  sa/ayaitt^m paitisant^m  Vyt52,  *P- /?  (wo  °Ä«- ,ljm)'i^.  3)  'erfahren,  erleben':  iaia lUli  (sd.)  *paitUäma  '*>  frya  paiti  tanvi ,  Yt.  i7, 10.  a)  bes. 'zur  Vergeltung,  zum Dank  erfahren,  empfangen':  kä>:ä..kä%3 .  (sd.)  saidyäi  yS  I  paitisift  Y.44.2 ; — ya^a ahmya  amtsa  spmta  sraoläoa  aiyäoa paitisqn  . .  yasnqsca  vahmqsca  Y.  öb.6.
mit  pairi  1)  'ringsum  absuchen,  auf- lesen': mazdayasna  aitihh  zimß  pairisa- yanta  (Opt.)  . .  varfsqmca  (als  Obj.)  ..yezi nsit  pairiianie  . .  astqmca  7-arpsqm:a  .  . V.  ö.  7f. 's\  z)  'herumsuchen  nach  — , aussuchen,  auslesen':  asstnanqm  xraoldva- nqm  .  .pairlstanqmY.i4.4'i'>;  A.3.5'^; —  uxtiitn  srlr>m  pairisttm  F.^^f'*'; V.J. 42  PüZ,;  —  pairi  daxma  aSlayqn  vi daxma    calsayqn   Y.S.z.  a)    mit    Dat
'für  — ':  ä'kre  . .  agsmq  pairihnte  V.  14.  i. a\.{atn/)iiali,icMli,f}iiyali,t}ayali,i}'e!ii;  iffäh. — Pü,:  j^äslan;  s.  noch  No.  6,  ST.,  15.  —  ')  S. No.  12.  —  ')  Nur  im  Adj.  aüasa-.  —  i)  Nicht ganz  sicher;  s.  No,  4,  10.  —  i>  S.  Gdn.  KZ. ^5-  S^'i  S  ^^S.  I  [  und  No.  10;  doch  vgl.  auch die  Var.  und  IF.  s-  36.  —  i)  Stait  arhmni, mit  I  für  y>;  3.  zu  Hndmi-  No.  l.  Das  Part. Fut.  bezeichnet  öfters  die  Absicht  etwas lu  tun;  vgl.  Schmalz  LatGr.j  312;  s,  noch zu /aS.»™»!»  Yt. /ji.  93,  /ra.'WBdw  V. /J.  1 7.  VgL ferner  '«ai-  No.  3.  —  *)  Pü.:  /o  iit  (in  Aw.- Buchst.),  —  T>  Unrichtige  Bede  utungs  an  gäbe bei  Hb«.  ZL  30,  SBayrAW.  /<?//.  66S.  — S)  Pü.;  ka  nikirind.  So.:  paiyalak  (AI*.);  s. No.  15.  —  5)  Pü.;  fa  j^ähiin,  Sit.:  prärtha- yilum.  —  ")  Ob  afia+lyaSal  vgLNo.4.  Pü. fehlt.  —   'O  %  304X1.  30.     Hds.  auch  upSji'.
dbyGoot^Ie
31  'acä-  —  *aeäa-  II  I  i  a.  32
—  ">  So  Fi  usw.,  na.  isituuy  das  im  h\is- \  fraUayam  tyaipatiy  Bh.2.13.  aa)  ohne gang  mit  dem  gleich  folgendeiiy-flra™(«ausEe.Qi^j^l^j  fasäva"  adam  fraisayanl  "uva- glichen    isL     Gleiclie  Endung  zeigen  jasnila  \  v        ,.,      ',.-         ■  i  ■  >.  i  ■       •<
|s.  gam-  No.  aa)  und  kintö  (s.  'a-i-  No.  s3);  L/'""  orauf  liess  ich  nach  Susa  marschiren" ich   verweise    daiu   anf   go(.  Uugandau    und    Bh.  /.  1 7.
S  JOJ.  3.  Zum  &  von  &3niö  s.  IF.  8.  352.  —  (  ai.  ijo«,  iit-a//;  an.  tisa  'sich  rasch  vorwärts »3)  Hds,  failibiif.  —  14)  NA.  mit  Fl  usw. '  bewegen';  gr.  vgl.  tl/ia  'impetus'.  —  Pü.  (la foitiSJm,  was  unmöglich ;  vgl.  J 10.  —  '5)  Fü. :  |  Y,  und  P.  mit  /rS):  fraatfiiaa ,  (lu  V.  mit nüTräan,  Sü.:  tdritiilum ;  s.  No.  8.  —  16)  So  |  /rä):  framSnfal,  (zu  N.  mit /ara):  a/ii  fTs  .. Kl.   NA,  ufiairi  nach  Pl2  usw.  und  nach  Pü.  1     (undeutlich).
afiar;  damit  wird  aber  auch /^W  übersetit.  |,  j_  ,g^^^^,  ^  .pg^g..  _j,^^/„„  zayan^m •  j.,  g.  =ae5-,  p.  ais-  V.  '(sich)  in  eilige  Be-  ysstryehe  fhiyantö  'la  CND.)  >'»yA«»»(sd.) weguQg  setzen'.  Praes.  3  iSa-,  27  isya-,  30  ■  v_  j^^  ^^
(Kaus.)  aisaya-,  adaya-.  —  Inf.  'istS;  Absol.  |  np.  xn,  KSs.  ii;  vgl.  tfi-  f.  'Deichsel'.  —  Pü. : 'ihmnitn.  \      "i  so  nach  Ga.  (und  Dst.),
Med.  'sich  in  eilige  Bewegung  setzen,  •  j.  'aesa-  m.  'Suchen':  rasistahe  pai:S eilen';  s.  Absol.  ra^öis'.  j -äwä  vaic^mca  (?,A.)  V.6^.13,  —  g.  aese
mit  paiti    'admittere.    Jemanden  wozu  |  als  Inf.  s.  bes. (Akk,) gelangen  lassen,  es  ihm  verschaffen':  |     Zum  V.  >a.-J-.  —  Pü.:  *i''ähiln, yä^a    astva  *hqm    ultanava  (sd.)    astvat  •  j.,  g.  -aesa-  Adj. 'potens' "    i)  'der  ver- "^aikygahitn  paiHSät  Yt  ;_j.i39.  I  mag  was  er  will,  wirksam,   einflussreich';
mit  para  Kaus.  '(Wasser  od.  dgl.)  weg- ' yaia  °iS  amavü  %rqfiuö  fraxstüne  s^mil laufen  lassen,  verschütten';  vTspanqm  zt  paiti  Y.  ff. 20;  —  'silät  ^wa  imavantasiä *avajrasn-ntqmparaca  aisayamananam  ^(yarnJ  (sd.)  Y.4'-4;  —  hyatcä  tnöi  hy^i dasva  *raizaiie  (sd.)  N.  ÖÄ  \växs  'iö  "und  dass  meine  Rede  wirksam
Td\t  para  \mA  frs  'entsenden  hin  zu —',  sei"    \.  44.11.  2)    'der    hat   was    er
{upa  mit  Akic.);  para  n  *gaosp}nta  ...will,  cupiti  potens,  glücklich':  am^rstäiti baodasla  urvän^mca  */rai^ämahi  nazdista  '■  *asaonö  urvä  °sö  "in  Ewigkeit  (wird)  die upa  >war}sta  raoca  V.34.  [Seele    des  -4Aanhängers    glücklich    sein"
xaA/rä  (frö)  i) 'forteilen,  entweichen': ,  Y.  43. 7;  —  kyat  '^wH  xsayqs  {^A^  °hm s.  Ini./rasstö.  2)  'zum  Forteilen,  Weichen  \dy,il  imavanitm  "weil,  wer  es  vermag, bringen":  tia^a  eil  raSva  masya  /«/«/'  deinen  des  mächtigen  Wunsch  erfüllen nasoa  fraeiyeiti  "kein  .  .  vermag  (ihn)  zu  möchte"  Y.4j.  ro";  ■ —  "Ü!  *kasu.draonö töten  noch  zum  Weichen  zu  bringen"  Vt.  (sd.)  jn^a  a^rava  V.J.  45. t4Z^-       3) 'impellere,  anspornen,  dringen      KompE.  —  Zum  V.  a-j-;  aus  ar.  »iwi/a- ;  vgl.
in-',  mit  Inf.:   gavöi  ..  fraliyamahl  ra-\  f'''';,  T.^"''  ,''^'"''''' ''"  ^'- "'■?);<?  .-^jj^if"'
., '  ,        V        ,      ,     .   ,   ,■;  (zu  V.);  transskr.;   s.  No.  z.  —  0  Vgl.  PuErl.
maca.     vasirmca    dazdyat   (sd.)     surwiva-  \„  „„;,.!„._    _    ,)    Pü..   ta  i  ,5  fjitxm  öh,-
taslä   .  .    Y.J5.4;     —    frS    Va   /raBsyil   .  .!  mazd  pa  i^j/iisn  dah-l  amävandlh,  erl.:  kü  Jfri
mrßiUisd.)  Y.^p.Ö;  —  ahutamca  vairim'     gmve  at  amä-.'anJih  bavii. fralsyilmaht    ..    hatnislayaica    ,  ,     Y.  61.   •  j.  ^aesa-  Pron.  dem.  (fem.  °s.i-);  nur  'sä I.  4)    'promittere,    versprechen':    tat  NSm.,f.  und  °Ü>  NSm. 'dieser'  I)  in  stark-
vlsp?m  frlnämahi  tai  vlsp>m  fraZsyamaAT .  delktlschem  Sinn  'dieser  hier,  jetzt'  i)  ad- .  .  avi  . .  tansm  V.20.$.  5)  D  im  Ap.,  jektivisch,  sva,  'dieser  mein,  unser':  ajfat
Kaus.  '(Truppen,  einen  Truppenführer)  U  .  .  *dqnmahi  'sa  zao^ra  paiti.jam- entsenden,  marschiren  lassen':  pasäviJ'  yät  tava  .  .  Y.C^.i;  —  '/a  dacna  N.  j; adam     käram    /raisayam     Bh.  2.  6;    14,  ,*j'(?).  2)    substantivisch:     °/ü    aibi.-
3.6.  a)  mit  Angabe  des  Ziels  a.)  Akk.  i^«n/«(sd.)  Y.  70.  i.  Ilj  in  schwach- 'wohin?',  ß)ai/rundAkk.'zuwem?,gegen|deiktischem  Sinn  'dieser,  der,  er'  I)  auf wen?',  t)  patiy  und  Akk,  'gegen  wen?'; '  Zuvorgenanntes  —  oder  durch  den  Zu- dädarsis..avam  adam  fräilayam  arminam\s,a.mmenh^T\g  Angedeutetes  — ,  Zuvorge- Bh,2,7;  10,  _y.i4,  5.1;  —  iaram  pilrsam  sagtes  (Wort  oder  Satz)  zurückweisend /raisayam  abiy  ('zu')  vistäspatn  Bh.  j.  ,1)  auf  ein  Nomen  a)  adjektivisch:  ae>/i i;  —  vahyazdäta''  .  .  käram  /rifisaya*^nar0  „yeztca  vao(ät  "sö  nii  V./5.3;  5.41; Aara^uvatim  .  .  abiy  ('gegen')  aziam  Bh. !  —  Atlucä  *aitaya  narä  .  .  °sö  zt  narö  .  . 3-9i  3i9i  i'j    —  pasäva''  adam    karam\'^.4.ifii.;    —    kanqm  ..  'sa  hana  Y.lj.
dby  Google
33
*aesa- JI  I  i
ae^-
34
1 4  i  —  aHatihä  äps  yat  armaSltaya  . .  °/a ä/s  V.ö.^oL;  32;  —  ^z^manaya  ..  -sa tMiana  'S.  ij;  V.5.45,  50,  Ö.31,  7-29, 70,  71,  75.  6,  33,  24.  a)  öfters  zugleich
auf  ein  relativisch  angeschlossenes  Nomen vorausweisend:  >o/<iW:4a/  sp3  urupis  fuai -so  spl  yS  urupis  .  ,  V.5.33;  —  ufa  vä nasus  raz'iwst  .  .  'sa  Jruxi  yä  ttasus  V. J.14;  5.27,  28,  7.1—4,  *.i6,  41',  9.40, 48;  —  ä^ravaium  yaoida^o  ,  .  'so  nä yö  yaoid.1>ryS  V.<).  37— 39;  40,  42,  If). 21,  Vd.iV.  10.  b)  substantivisch;  aStacTva daxmaisva . .  "sö  zl  asH  äaivanam  rapakö V.  7.55f.;  —  daxme  .  .  yat  °/a  pqsnu ra^'>a'.J/(sd-)  V.  7,49f.;  —  aisa  y5..aiwi.- >r}lti^ätus  (sd.)  *aivayaHi  -io  barfsmö.- sbrfiti  ratufris  N.  /Oj;  —  slaotaca  (sd.) yasnäica  . ,  yat  °sa  ahurake  mazda  "Pre is- lieder  .  .:  das  des  AAM."  Vr.if.ö;  6;  — jtal  ..  kmntiit  ava  hö  mirysüe  anJmltÖ si  'SÖ  , .  "wenn  er  . .  operiit  (und)  der foperirte)  stirbt,  dann  ist  er  disqualifizirt.." ^'■7-37;  —  iD  Kongraenz  mit  dem  Prae- diltkt;  cit  ai-at  vacö  äs  ,  J  baya  °h  3s ahunahe  vairyehe  "Was  war  das  für  ein Sprach  .  .?  Das  war  das  Stück  A/iV." 'W  i<).  I  —3,  o)  öfters  zugleich  auf  ein
relativisch  angeschlossenes  Nomen  voraus- weisend; aoxtd  ratui . .  'lö  yö  ratul  V.  5. i6;  —  * af?r3n-iyüka  ..  'sa  *yd  apirin^- /ö^.>  N.  7;  V.  75. 16; — yö  kainitDtn  upaiti ..  ml  . .  'la  yä  kaitu  V.  15.9;  10,  13,  14'; — paiti-iristpot  ..  'sa  yJ  paitt.irista  V,  9. ,1  (?)■>.  2)  auf
der  . .  ?  . .  Das  ist  der  glaubensfeindliche
Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
folgendem  Fall  brauchen  wir  den  unbe- stimmten Artikel  'ein':  yavat  °sa  carsitika *avi.mqm  har>k>  (sd.)  hancayät  V.5.60. Undeutlich:  °sS  gaeHanam  . .  rass?  (sd.) N.  2;  —  ainitis  -iÖ  *växs  P.  26.  Vgl.
zu  iaita-,  das  die  fehlenden  Kasus  zu *aiia-  liefert
ai.  tfä,  efäh  'dieser',  esa  'diese';  nbal.",  np. eSä»  (Plur.).  —  PQ.:  Jh.  (lu  Y.  12,  V.  iS):  i, {zm\.4.7.%6,I4,  N.wj):  ö™«,  (znV.5.41): ausgelassen.    —    i'  Mao  verlangt  den  Akk.;
aedasa-  Adj.  'suchend,  ausgehend -',  mit  Akk.:  töi  narjpi/  *an>ßs  'sa einen  Sau,  substantivisch  in  Kongruenz  |  (pjpm.)  äijit.arpm  p»sö4anv5  ka  asavä mit  dem  Praedikat:  astuyi  damam  {^^Mahurö\tA.)  yi  Ts' . .  Ä3mihyäJ (sd.)  "sie,  die '/J  as/i  dainnya  . .  äsiailir  (sö.)  Y.  J2. 9 ;  i  darauf  ausgehen  die  Würdigen"  herabzu- —  yat  hl  nr'tp  fr9dvo.st?hamm (sd.)  ..'^^ setzen,  die  Missächter  des  heiligen  Rechts, zi  asti  äiiiya  kata  (statt  NS.)  aetake  yat:  djg  jjjren  Leib  verwirkt  haben  -;  wo  ist irisiahe  ".  .  so  (wie  beschrieben)  ist  die  der  .  ."  V.  \J.  9". vorschriftsmässige  Kammer  für  den  Leich- '     Zum  Praes.  14  des  V.  'a?/-.  —  Vgl.  üaia-,  —
nam"    V    511.                2)     vorausweisend'  Vä.-.  vasän  j^Jsl  ^slit  iat  dastawarlh, -^  ^M)\k
(öfters  zugleich   zurückweisend;  S.  1  1  a  0,|  'Würdigen'    sind   Zara%u}lr^    und   seine  An.
.      ,       ■,        r     -            1"   ..       j       j            ..  hanger  im  Gegensalz   lu  den  duh-ar^a-.  —
b  a);  r)  auf  eine  erläuternde  oder  ergan-  ,)  gdn.s  Deatung  der  Strophe.  KZ.  2Ä  jSj
leodc  nominale  Beifügung;  meist  entspricht  I  —  s.  auch  Js.  JAOS.  1$.  229  - unser  Artikel  (schwachton iges  'der') ;  a)  ad-  j jektivisch,     mit     relativischem    Anschluss: ,
"irS  .  .  ästlraili  yö  vacahinö V.4.5; —  'Sö  mirpyö  yö  pard.dars  VtV! . '".41;  41.  b)  substantivisch:    "äj   vS
dvaraiii  bälyqsla  danyö^ava  V.1S.16;  — ä/  käu  as  .'.  yö  .  .i  .  .  hö  bü  'iö  äs  .  . abmairjö  anafava  yd  . .    "wer    ist   das,
B.11IHOLOHAE.  Altiran.  Wh.
'Vermögen';    r)    'Können':
haltbar. aesä- yö  anu  'Sqm  bansma  *frast)r?nte  ya'^a "wer   so   gut   er   kann   das   B.   bereite^ wie  .  ."  N.iV^;  103.  2)  'Habe,  Eigen-
tum'; täyu/  fumat^Aö  (sd.)  . ,  'sqm^t  iira vä  asni  i^ra  v,J  xsafne  matianahe  x^äi pairigmnayeili  ".  .  als  ob  er,   seis   am
dby  Google
35  aeäamna-  —  aok-  36
Tag   seis   in   der  Nacht,   die  Habe   des'/'i^.tanusVt.io.gj;  —  srtioJ>m.,yii'iium
Hauses  für  seinen  Bedarf  wegnähme"  V.  st^r^'iwaia  snai>i/a  rixram^rttim  :far}m
4.1.  —  'sayä  Vyt4i(?).  )ainH  Y.57.10;  V.//.9;  —  'tm^m  FrW.
Zum  V.  a^i-;  sa%  «r.  •a«iJ-.  —  goL  vgl.  aii/!.  t).  2  (?);  —  sonst  mit  xn'T.drav  (sd.,  auch
—  W.(inN.rf9):  afurr  fa  iiÄa  hir  u  djlastia,   fdSt):  sraos?m..'mah£  xn-Ldraos  hamai-
(,n  V.):  ii.'».  {zu  N.  ,oj):  ausgelassen.  rf,7^«ytJj.iS;  — !'/*/<?  zT  anye  *ma'^wkö
■yG!»„i,»'V.4i:\^^y""-"'»-  (sd.)    'ma    haänle   *xn-idtTÖ  aat  hl'  yd
g.  <üi>«  m^yi  Y.  43.  ii:  lies  «^Um<,hy.u    ^.^^^  ^^-^g  ^^  ^^^-^^  un-äsmana  Y./O.
•  j,   aeäsmna-   Adj,   (fem.  'nä-),   PP17   g;  usw.
(Fut.)M.:  S.   ^ais-  mit  No.   5.  .j  \Tah<a.   der   durch  Trunkenheit    «rrCElen
•  g.  aeSe  InC  'zu    suchen',   mit   Gen.:  /J   Zomwüligkeit   (Y.  la.  8).     Er   gilt    als  Ceijncr *un'anim  mingatrlK^)  dadl aiis^a  vXdus  $f^  rf'*7^ei  w!'nd°schi.\''nn  z'si''i"8^'^^^^
. .  jcji7»  (7?°'>  «/(7*yJ')  Y.2cV.4.  '™    '     ,"   t'    „.-""        *    ^  '.,      -    ,
```


## [2026-09-07T20:17:26.705Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT Pflug ===\"; grep -n \"Pflug\" BRT.txt | head -20"
}
```


### [2026-09-07T20:17:26.762Z] TOOL RESULT

```
=== BRT Pflug ===
21863:•  j.  *yuyö.s»nii- ''  f.  Name  eines  land- wirtschaftlichen Geräts:  yalsqm  sayanqm västryehe ßuyanlB  alla  •»»■(ND.)''  "..Pflug und  .."  V./4. 10.
```


## [2026-09-07T20:17:28.954Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN p.114 => leaf 135 (0-based leaf idx = p+21) ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=135 && NR<=137 {print \"----BLOCK\",NR\"----\"; print}' HRN.txt | head -120\necho \"=== HRN grep xis ===\"; grep -n -i \"xis\\b\\|xes\\|Pflug\" HRN.txt | head -30"
}
```


### [2026-09-07T20:17:30.239Z] TOOL RESULT

```
=== HRN p.114 => leaf 135 (0-based leaf idx = p+21) ===
----BLOCK 135----
— 113 —
508. x^^> /ß^i ^^'^^ {^' i- X<^s, jüd.-pers.), (Sahn, /^^es^ daneben
äähn.O, AM.: ;kös) gut, schön, fröhlich* etc.").
Käs. x^Sj /öS.
phlv. /^as hezw, yüs (paz. ;^^as); kurd. /ös, v^; af/.
yöi; bei. vas (407); öij'n. ;Kdi^', sar. yS^.
Nöldeke (mündliche Mitteilung) nimmt als Grund-
form *huakSi- an. Dieselbe Anknüpfung des Wortes
bei Fr. Müller, WZKM. 5, 352.
509. yiiisnüdj x^snü zufrieden, fröhlich*.
aw. *huxsnüta' vergl. hu/rnüiti- 'Befriedigung'; phlv.
/iisnüt, /usnütik (AV.).
510. x^"'*^) 'Schwein, :i)5 (Qiss. Dan. S. 388).
aw. hü kehrpa in Ebergestalt'; phlv. /ük (Bund.),
yßköak hezw, /übadak (Payprus, Ilorn ZDMG. 43, 51);
skr. siikard- 'Eber, Schwein*.
kurd. /ü (H.-Sch.); B>fy.xilg; oss. d. t. yiä (310);
bei. hlk, n. hJy (157) ; wa;r. /äg, sar. y^ug,
511. //rn 'Blut', yümn.
aw. vohuni' *Blut'; phlv. yün, yUnömaud,
kurd. ;^("n (ll.-Sch.); af}'. vTne (f. pl.); bei. LW. hün,
hon (162); wa/. vu/c^n, Uyn. vlyTn, sar. va/ln, sangl.
vain,
512. xöl Helm', yöd.
ap. yauda- *Helm*; aw. ayö],yaoda'.
arab. LW. yu^at 'Helm'; Sify.yöl; oss. d. yodäy t. yüd
(302) ; sar. ydtid *Hut, hohe Mütze aus Schaffell'.
513. yi^'ei 'Schweiss .
aw. yya^öa- 'Schweiss' (ZPGl.), vergl. aw. y'^'Tsctt,
ynseu] phlv. yj^ai bezw. y^'ede, vergl. ynst (y. 9 (37),
») Z. B. xöst (I, 117 Vers 962).
*) Np. ves, das ich Mitteilungen, Heft IV, S. 25 No. 6 fälschlich
neben phlv. reh gesetzt habe, lässt sich nicht zu np. '/us stellen, da die
Vertretung von altem sv durch v wohl kurdisch und belucisch aber nicht
neupersisch ist. Nöldeke (mündliche Mitteilung) sieht r^s als Doppel -
form zu ges an, dessen Aussprache durch jüd.-per8. "»;^;j (Is. 10, 12) voll-
stündig sicher gestellt ist.
') Der bei diesem Worte auch Gberlie forte Majliril vokal if^t falsch.
II o !• n , Grundriss d. noiip. Ktymolojrio. S
----BLOCK 136----
- 114 -
vd. 3 (105)), /i'lstak (vd. 13 (13) GL, (22), (24) (aw.
roya-)), ynstahlh (vd. 9, (109) — der Commentar denkt
falschlich an np. y ästen, /ez-em): ai. svvda-; arm. l^irtn
(H. Xo. 291).
kurd./«, /öh, /oi 'Schweiss'; af/. yyale (f. pl.); oss.
yed (300, 2); bei. hed, n. ÄtJ (158); wa/. yß, sar. y«/().
514. /''^Ä ^verwandt, angehörig; selbst (eigen)', y^esävend^
yj^estefi, yyeskär^).
aw. vergl. y^aefU" angehörig, verwandt'; phlv. /«'es,
y^esih^ yHslmtan, y^'äskär, y^eskänh.
wa/. /is, sar. yeiy 'Verwandtschaft, Familie*.
Fr. Müller nimmt (WZKM. 5, 187) sehr unwahr-
scheinlich die Instrumentalform aw. ^/^aetusa als Grund-
form für np.y^es an. — Bartholomae (briefl. Mitteilung)
denkt dagegen an ein ap. *kwäisiija' als Grundform;
zum Suffix 'ttja- vergl. ai. -tya-, Whitney, § 1245, b.
515. -^f^en (dialektisch yec) 'Pflug'.
aw. aem- (vd. 14, 10 (43)); phlv. /es(?).
Darmesteter, Et. ir. I, 77.
51G. ^j!lm 'Naturanlage, Charakter'-), vergl. hed^hn^ dns/lm,
duzyim {Vis und Ramm S. 32 V. 5 v. u.).
aw. vergl. haya-^ haem vd. 13 (124), pancö^\hya-
(Geldner, KZ. 30, 514 Note 1); phlv. /I?« bezw. /n;j
(vd. 13 (124), 5 (117) Gl.), huyjm (Gemme, ZDMG. 44,
068 No. 105), dus/wu
Anders und falsch Fr. Müller, WZKM. 5, 187; die
Bedeutung der aw. Worte steht jedenfalls fest.
517. x^?/'^» yJ^ 'Speichel', ylin (Gazophyhicium s. v.
saliva, Vullers s. v. ylm No. 3).
aw. gereöi.']yava'^ yt. 15, 47 (?); plilv. ;^ay?7Ä; (y. 38
(13) GL), yaya (Bund.).
Justi, Bund. s. v. yayü,
AM. gebraucht die Form yeön (208 Zeile 3 v. u., 209
*J Bedeutet auch bei Firdüsi 'fleissig, rechtschaffen* wie im
Pehlevi; ein np. ^^'es *Pflug' statt j^es (No. 515) giebt es nicht.
2) Reimt auf htm (Via und Rämln S. 51 Vers 9; 166 Vers 13),
dns sohon damals nicht mc»]ir bem gesprochoii wurde.
----BLOCK 137----
- 115 —
Zeile 5, 232 Zeile 6, 7), vergl. ;^Mrfw (Vullers), /udn
(FR) ^). Die Zusammenstellung mit aw. geredi,]/(wa-
ist wohl falsch; das Nebeneinandervorkommen von d
(d) und y weist jedenfalls auf einen ursprünglichen
Dental hin, und so wird man auch im PehlevT besser
/adük, yadti lesen.
D.
518. dad 'Gerechtigkeit, Recht', dadistan,
ap. data- 'Gesetz*, {[/^da-, adadü); aw. data- {l^dä-,
daöäiti); phlv. ddt, dätastän, arm. LW. dat, datastan^
hebr. LW. Dl; ai. vergl. dhäman- 'Gesetz' ([^dha-,
dädhati),
LW. kurd. af^'. däd,
519. dädär 'Schöpfer .
aw. datar- 'Schöpfer ; phlv. dätär, päz. dädar, dadär;
ai. dhätär-,
520. (i) dädeti geben', Praes. dth-em, däd 'Gabe', dthis^
jiid.-pers. r^^m (Qiss. Dan., S. 402 Zeile 10 v. u.).
ap. Krfä-, dadütuv geben' ; aw. l/^rfö-, dadqmi 'geben' ;
phlv. dätan; ai. \^da-^ dddäti 'geben'; arm. tcd 'geben'
(H. No. 269).
kurd. däin^ dän 'geben'; afy. lal; oss. d. dädfun,
t. dänftin (240); bei. deag, n. deay (79); »i/n. J/-a?w,
sar. öä-m,
521. {2)däden machen, setzen, in Zusammensetzungen wie
äväz däden 'rufen', ferämös daden 'vergessen' u. v. a. m.
ap. l/^rfä-, adadä 'machen, setzen'; aw. [/'da-, dadaitl
V
') FJ hat folgende zwei Belege:
ö /üdü zed her rüxe ki rö^yl mäh
sijde äred pes i ö der sijdegäh
Mole vi Ma*iiovI (Mctr. Romel).
ez hed'i cer^-t äsiyä-gerdän
^ifsk^ sud der dehän-t hende -/üdü
Süzciil fMetr. Xeflf)
8*
=== HRN grep xis ===
522:neutralen Suffixes indog. -os sei (BB. 17, 113).
820:45. ätnäj 'Pflugsterz'.
3947:Pfluge befestigende Lederriemen' (H.-Sch.); bei. Jöy
4455:490. xiSm, xesm *Zorn*.
4652:515. -^f^en (dialektisch yec) 'Pflug'.
4670:Pehlevi; ein np. ^^'es *Pflug' statt j^es (No. 515) giebt es nicht.
6117:sar. spur 'Pflug .
6444:aw. \/saoi)' in sufrä- 'Pflug, die Geiger unter
6610:758. sTilT, snl 'Pflug* (unbelegt, nur im FS).
6612:'Pflug* zusammengebracht, was aber nicht vorkommt
9684:Suffixes -yär - vergl. beytyür 'glücklich* , hösyär
10109:aber wegen des Suffixes vielleicht nicht nur um-
11601:eiidöxis 132.
12806:xesterüiie 485.
18563:xes 853 Anm.
22376:gjxis «98.
```


## [2026-09-07T20:17:54.788Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full 63380-63520 ===\"; sed -n '63380,63530p' POK_full.txt"
}
```


### [2026-09-07T20:17:54.839Z] TOOL RESULT

```
=== POK_full 63380-63520 ===
Page(s): 774 

Root / lemma: oiua {*he/-ua-) 
See also: see above S. 297 {e/-). 
Page(s): 774 

Root / lemma: ok- 

Meaning: to think over, *understand, see 

Note: 

Root/ lemma: ok-: 'to think over, *understand, see' derived from a reduced Root/ lemma: 

ok''-: 'to see; eye'. 

Material: Gr. 6kvo(; ' dubiousness, hesitating ', okveoj ' hesitate ', OKvripoq ' dilatorily '; 



Gothic aha'sense, mind, understanding ', 5/775/7 "believe, mean', ahmam. "gliost'; 
ahaks'6ove' (as spirit bird); Old High German 5/7/5" observance, paying attention ' 
(Modern High German achtgeben). Old English eahti. " calculation, consultation, estimate 
', Old High German Old Saxon ahton. Old English ©5/7/75/7 "consider, observe, appraise ', 
Modern High German achten, beachten. Old Icelandic aetla {*ahtildii) "mean, think, intend, 
mean, aim'. 

References: WP. I 169; after Specht KZ 62, 21 1 to ok""-. 
Page(s): 774 

Root / lemma: oRtd(u) 

Meaning: eight 

Note: 

Root/ lemma: oRtd(u)\ eight derived from the extended Root/ lemma: ok-\ "to think over, 

*understand, see, count' + -/is attribute formant modelled after lllyrian attribute nouns, 

adjectives. Hence PIE numbers derived from previously ordinal numbers. 

Material: Old Indie asta, astau {besides asTtf-i. " eighty '), Avestan astaio Avestan asti- " 

width of four fingers ' (to Sg. *asta-), Henning TrPhSoc. 1948, 69; Armenian ^/'(probably 

from *optdW\Vc\ p assumed from seven p)\ gr. oktw; alb. tete {*oktd-t-)\ 

Note: 

Anatolian languages show a pattern similar to alb. So Lycian 5//5/5 "eight' : alb. /e/5 "eight'; 

Lycian nuntata'n\ne' : alb. nanda 'n\ne'. Therefore alb. 5/7/5/5 "seven' derived from a 

truncated *sa{pjtata^ seven' later Old Indie saptathah, Avestan hapta&a-. Old Saxon 

sivotho. Old English seofoda, Lithuanian septintas, also Old Indie saptatf-, Avestan 

haptaiti-lQ\ in alb. -ta, -teare attribute formants that were solidified in Anatolian and Indie 

cognates. The attribute -/5 formant (used in the genitive and adjectives) is unique to alb.- 

Anatolian languages alone. 

Therefore alb. tefa "eight' is a zero grade of Lycian a/tata {*oktd(u)ta) "eight'. It was initially 

an ordinal number used as an attribute [compare Latin octuag/nta^ 80']. 

A better explanation is the fact that Anatolian languages used the Akkadian script which 

did not permit 2 subsequent consonants, therefore a vowel was introduced between the 

double consonants found in: 

Northern 

Runic 

a:tta 

Old Norse 

atta 



Norwegian 

atte 
Danish 

otte 
Swedisli 

atta 

Dalecarlian 

atta 

Faroese 

atta 

Old Icelandic 

atta 

Icelandic 

atta 

compare maked. Otto-lobus^ 8 hill '; Latin odd; Old Irish oc/?//?- (nasalization after secht 
n- and noi n-)\ cymr. wyth, ncorn. eath, bret. eiz{*ochtT, older -Jfrom -o); Gothic ahtau. Old 
Icelandic atta. Old High German Old Saxon ahto. Old English eahta; Lithuanian astuo-nr. 
Old Church Slavic osmb (reshaped after the ordinals osmb); Tocharian B okt, A okat 

ordinals: Latin octavus (compare also Oscan Uhtavis ' Oktavius ') probably from 
*octduos. Old Phrygian otuFoi Fetei "in 8. years' {*oRtduoi uetesi); gr. Ionian Attic 
6y5o(F)o(; (6 after £p5o|JO(;), obstructed in oySoriKOVTa (hom. to oyScbKOvra reshaped after 
OKTib), compare Latin octuaginta^QO\ the former model from septuag/nta and arisen anew 
in very late time after the latter again; 

after the ordinals to septm {and deRm) have been directed Old Indie astama-, Avestan 
astama-, gall, oxtumetos. Old Irish ochtmad, cymr. wythfed, Lithuanian asmas. Old 
Prussian asman (Akk.), Old Church Slavic osmb {oRtmo-)\ compare Tocharian A oRtant, B 
oRtante^Vne eighth', alb. f. e teta^ the eighth ', m. i teti^ the eigth ' 

Other congruities are to name ved. astadasa- 1 8, Avestan astadase- 'the 1 8.', gr. 
6KTCji)(Kai)5£Ka, Latin octodecim. Old High German aMozehan^8^, gr. OKTOKoaioi, Latin 
oct/ngentr 800'. 

References: WP. I 172 f., WH. II 199 f., Trautmann 15 f. 
Page(s): 775 



Root / lemma: ok"- , {*{*hek'^h- ) 

Meaning: to see; eye 

Note: besides ok-, see there 

Note: 

Root / lemma: ok"- : to see; eye derived from Root / lemma: deik- : to show' : Root / 

lemma: dek-1\ "to take, *offer a sacrifice, observe a custom' [common lllyrian-Baltic d- > 

zero]. The drop of initial d- in proto Aryan languages Irft the bare laryngeal /?-.
```


## [2026-09-07T20:17:56.131Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full oies / Deichsel Stange ===\"; grep -n \"lemma: oi\\|oiTiiov\\|oieion\\|oi[eé]ion\" POK_full.txt | head -20\necho \"=== POK_full 'Deichsel' ===\"; grep -n \"Deichsel\" POK_full.txt | head -20\necho \"=== BQT v2 خیش ===\"; grep -n \"خیش\" BQT_v2_pages.txt | head -30"
}
```


### [2026-09-07T20:17:56.223Z] TOOL RESULT

```
=== POK_full oies / Deichsel Stange ===
63319:Root / lemma: oid- {*heid-os) 
63378:Root / lemma: oi-no-, oi-uo- {*hei-uo-) 
63382:Root / lemma: oiua {*he/-ua-) 
67230:lemma: oii- {* horghi-a)\ vine, *grape < Root/ lemma: orghi-, j'ghi-{*horghi-a)\ testicle. The 
=== POK_full 'Deichsel' ===
24612:e/-e/-\n Lithuanian felekstisi. " Deichselstange ', Latvian ieluksi, ablaut, ilkss, ilkmis6s.\ 
=== BQT v2 خیش ===
15192:         ‫»قرابت)«اسشق‪ »4۱۵‬کیلکی ‪ ۴ . 0511‬رکد‪:‬خیش‪.‬‬
15262:  ‫کار مر کب‬     ‫(ه‪.‬م‪+ ).‬‬      ‫‪ »۲:‬ظاحراً بمعئی مذ کور درمتن از ‪ :‬خیش‬            ‫‪۹۳۱‬‬    ‫اسم‌مصدر آ تست متا‬
15352: ‫که آنرا خیری وهميشه بهارگوبند ‪ - ۷‬ومردم‬              ‫خیش و آهن جفت باشد » بعنی آهنیکه بدان‬
15488:‫‪ -‬بروزن پیش (‪. )۲‬وز اری باشد‬                     ‫خیش‬                 ‫مقدار که خواهند نورآاخیز گیر بحذف بای‌ابجد‬
15512:                            ‫رو‬            ‫‪-‬‬   ‫خیشخانه‬                      ‫وحجم‌نده ویربای ات مه و أغز نده باشد‬        ‫‪۴‬‬
15549:                                                                                                                            ‫خیشفوج‬
26474: ‫وریزه را نکیوزیندا ‪ -‬وامر بریختن هم هست‬                        ‫برخیش بندند بجهت زمین شیار کردن ‪.‬‬
32599:  ‫‪-‬‬       ‫‪ ( 414010‬دستهٌ خیش ) » از رة‪‎‬‬   ‫هندی باستان ‪-‬‬    ‫‪- ۴‬‬           ‫‪.‬‬   ‫رك‪ :‬سوی‬      ‫‪٩‬‬
32601:  ‫‪( 1205 - 2۵۰‬بازکردن)؛سر یکلی]‪( 15‬خیش) «اسشق ‪«:۹۹۹6‬سپار ‪,‬کارآه نکه زمین‪‎‬‬
40371:   ‫‏‪ 4۳. trayêdaça‬تلفط خیشومی کلمه در فارسی ( مینزده ‪ ) 020205‬رك ‪ :‬دستور زبان‬
```


## [2026-09-07T20:18:06.966Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nf='BQT_v2_pages.txt'\ns=open(f,encoding='utf-8',errors='replace').read()\nleaves=s.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'خیش' in l:\n        m=re.search(r'\\[pdf page (\\d+)\\]',l)\n        print('LEAF',i,'tag',m.group(1) if m else None, 'printed~',i+543)\nEOF"
}
```


### [2026-09-07T20:18:08.375Z] TOOL RESULT

```
LEAF 258 tag None printed~ 801
LEAF 259 tag None printed~ 802
LEAF 261 tag None printed~ 804
LEAF 263 tag None printed~ 806
LEAF 264 tag None printed~ 807
LEAF 449 tag None printed~ 992
LEAF 547 tag None printed~ 1090
LEAF 669 tag None printed~ 1212
```


## [2026-09-07T20:18:14.571Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ns=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=s.split('\\f')\nfor i in (258,259,260,261,262,263):\n    print('='*20,'LEAF',i,'printed~',i+543)\n    print(leaves[i][:2500])\nEOF"
}
```


### [2026-09-07T20:18:15.847Z] TOOL RESULT

```
==================== LEAF 258 printed~ 801
  ‫‪۷ 6‬‬                                                                                                           ‫خوی درد‬

 ‫‪-‬‬        ‫هم هت‬    ‫باشد ‪ - ۴‬و نمعتی خود وخوشتن‬                     ‫خوی درد « بکراولرالی‌وسکون‬
‫وقلبه را نگیوزبند وآن چویی اس (‪ )۲‬که کاو‬                       ‫بیلقطة‬       ‫ودال‬   ‫ابجد مفتوح‌برا‬   ‫ودال‬   ‫تحتانیه حپول‬


‫آهن رایدان محکم سازند وزمین را شیارکنند ›‬                       ‫أن چنان باشد که‬           ‫و‬   ‫‪۰‬‬   ‫است‬   ‫زده » نام مرضی‬

 ‫‪ ۳‬بعضی کاوآهن را گفته‌اند ‪ - ۴‬و نمعتی خوت‬                     ‫اطراف انگت بخته شود و چرك کند و گاهی‬
‫وبن دکه‬ ‫ونيك‌هم آهده است ‪ - ۴‬و وجودرا نگیز‬
  ‫نقیض عدم است ‪ -‬ونوعی ازبافتة کتان باشد ‪#‬‬                                                                  ‫گوند ‪. ۱‬‬
 ‫خو بشتی د ار (‪ = )۳‬شخصی راگوند‬                                    ‫خوبه = بائالك مجهول ‪:‬روزن هرسه‪,‬‬
 ‫که پیوسته خود را او دا دارد و فراغت دوست‬
                                                                                       ‫مباحثه ومنافشه رگاوند‬

 ‫وتن‌پرور باشد چه خوبشتن بمعنی خوداست ‪- ۵‬‬                          ‫حو بش = بكر اول و ثانی معدوله‬
 ‫وشخصیرانیز گویند که خود رادر کفتن سخن حق‬                          ‫بروزن پیش " ممروف است که اقوام وخویشاوند‬
                                                                            ‫(‪ )۱‬چث »خم ‪ : ۱‬داخس ‪.‬‬
                                                                           ‫‪ :‬خویشتن دان (!)‬         ‫(‪ )۳‬چش‬

         ‫«تاوادبا ‪۷۱۰‬‬   ‫‪hsêvx‬‏‬   ‫پپلوی‬   ‫ت‬   ‫‪۳‬‬                 ‫) ‪۰‬‬    ‫‪ -‬رك‪ :‬شرح قاموی ( د ح س‬               ‫‪۱‬‬

         ‫‪ .‬رمش آمرانی‌باستان واوستابی‌ککمه مشکوك است «هویشمان‪.*4۱۵‬‬                     ‫‪۱‬ک‪4‬ک‪۰‬‬
                                                                                           ‫‪۰‬یر‬
                                                                                             ‫«مینا ‪ ۹۳۱:۲۹‬نی‬
         ‫»قرابت)«اسشق‪ »4۱۵‬کیلکی ‪ ۴ . 0511‬رکد‪:‬خیش‪.‬‬
                                                ‫وخی (‪.15‬سریکلی ‪( 163‬خوشاوندی ‪.‬‬
                                     ‫(ح(‬         ‫‪ :‬خودشتن‬    ‫رکه‬     ‫‪_ 2‬‬                 ‫رك ‪ :‬خوش ‪.‬‬         ‫‪۴‬‬

  ‫* ‪ ۴#‬خویشاوند ‪ -‬با واو معدوله وفتح ششم " پهلوی ‪« 002۷82156۷1‬مینا ‪> ۹۳۱:۲‬‬
                  ‫از‪ :‬خویش ‪ +‬آوند (یسوند) «اسفاا ‪ :‬ص‪ ۷۸۱‬؛ قوم »خویش هنوب ‪:‬‬
  ‫«کلتان ‪. › ۰۱۱‬‬      ‫وارنان را ز مر گك خوشاوند‪.‬‬       ‫رد میراث مخت نر بودی‬
  ‫[رك‪:‬‬   
==================== LEAF 259 printed~ 802
                                                                                                     ‫یه‬
                ‫وعربان خراطین میگوند (‪. )۲‬‬                              ‫وحرف خیرمعاف دارد ‪١‬‏ ‪4 .‬‬
 ‫خیوود ‪ - ۴‬بااول بنالیرسیده وثالك‬                    ‫خو بشکار ‪)( ۲‬ه با ئالی معدوله بروزن‬
 ‫بواو کشیده ویزای نقطه دار زده » شپره را ‪۳‬‬
                                                                  ‫پبشکار » برزیگر ومزارع راگوبند ‪.‬‬
                                                    ‫انی‬      ‫خو بله ‪mm ۳‬‏ بقتح‌اول ولام وسکون‬

                              ‫که شت پرواز کند‪ :‬‏‬    ‫ممدوله و ثالث » مردم یسمل و لادان واحمق را‬
‫را‬     ‫خو له * = بورزن موبه " پاروب‬                  ‫گوبند» ویشتراین لفظ را درمحل قدح ودشنام‬
‫کونند ‪.‬و آن بیل مانندی باشد از چوب که‬                                                         ‫استعمال كنمند ‪.‬‬
‫بدان کشتی برانند و برف و امثال آن نیزپاك‬            ‫بر وزن استاد » کرم‬                     ‫حوی ناد‬
                                                     ‫سرخی است که در مبان کل نرم متکون میشود‬

                                           ‫يان نوردهم‬
                      ‫درخای نقطه دار باهامشتمل برینج لغت‬

‫و جاو مقام‬           ‫ل‬‫زو‬
                       ‫ثطن‬
                         ‫می و‬
                            ‫قرشت » بممن‬             ‫الی " به‌عنی‬     ‫بفتح اول و سکون‬          ‫‏‪a‬‬   ‫حه‬

                                          ‫باشد ‪.‬‬     ‫خوش وخوشاوزه وزهی وپه باشد ککلهمة تحسین‬
 ‫خهل ‪ - ۲‬بنتح اول بر وزن بهل ‪.‬‬                       ‫وزمزه‬    ‫و یه‬   ‫خوشا‬       ‫بممنی‌خوشا‬

                                                                                       ‫ط‬
                                                                                             ‫وخەخه‬   ‫‪٩‬‏ ‪۰‬‬   ‫ات‬



 ‫بزبانکیلان بممنی کج وناراست وخم‌باشد» ونم‬                             ‫وبعربی بخ بخ وباركاله گویند ‪.‬‬
                                 ‫اول همگفته‌اند ‪.‬‬       ‫وای‬
                                                          ‫حهر‪ -‬بم اول و سکون انی ر‬

         ‫(‪ )۳‬چك ‪ :‬شپره را ‪.‬‬            ‫(‪ )۷‬چك ‪ .‬چش‪ :‬گوبند ‪.‬‬            ‫(‪)۱‬چش‪ :‬خویشکاو(!)‬

     ‫نفس است استعمال شده‪: ‎‬‬      ‫بر‬
                                  ‫طکه‬
                                    ‫لی‬‫‪ - ٩‬خویشتن‌دار درناریخ بیهقی بمعنی‌خوددار و ک‬
     ‫د رخلیفه افشین را کفت ‪ ):‬باز گردوپس ازین هشیارتر و خویشتن دارترباش» «تاریخ ببهقی‪٩۱۷۷ ‎‬‬
          ‫رك‪ :‬خوشتن داری (ح(‪9
==================== LEAF 260 printed~ 803
  ‫—‬       ‫س‬                                                                                               ‫خپله‬

‫خهی ‪ - ۲‬بفتحاولبروزن زهی کلم‬                              ‫خهله ‪ » ۱‬بنتح اول بروزن بهله ‪.‬‬
 ‫ست ازخه وای »نی‬
               ‫تحین است وآن مرکب ا ت‬                        ‫‪۱‬‬                         ‫بمعنی خپل است‬
                                                                                                  ‫‪۱‬‬           ‫اشد‬
                       ‫‪۰‬‬   ‫مرحبا وبارك ال و آفرین‬




                                                   ‫بیان بیستم‬


                                   ‫| شماربر خوافند ‪.‬‬        ‫فف‬  ‫اول وسکون ان‬
                                                             ‫میخ‪.‬‬                      ‫یک‬
                                                                                      ‫=ر‬ ‫ب‬‫ح‬
                                                            ‫مقانان و خي‬                ‫خيك یا‬
                                                                               ‫تعم اخزيك‬
‫خیار زره سنك ‪ -‬رستنیی باشد مانند‬
                                                                                                      ‫‪.‬‬       ‫‪:.‬‬
                                                                                                                ‫ماست‬
‫آنرا بعربی قثاء الحمار‬      ‫کر اما خار ندارد » ‪ ۱‬و‬                                    ‫‪۴‬‬

                               ‫‪.‬‬    ‫خو ای‬
                                   ‫خوانند‬           ‫و‬
                                             ‫وقثاءالبری‬
                                                                                          ‫ی‬
                                                                                          ‫‪° ¢‬‬             ‫‪۳‬‬

                                                                                   ‫معروف‬    ‫است‬           ‫دواسی‬

‫ای شله‌دار‬
         ‫خهبیاارر ژنهه‪ _-*۵‬ب ‪-.‬فتح !ول و زا‬                                                     ‫و‬
 ‫ونون وئانی بالف کشیده ‪ ۰‬خواهرزن راگویند ‪.‬‬                                         ‫گوند ‪ .‬اسهالآ ورد ‪.‬‬
‫خیال بر ستان = کنابه ازارباب نظم‬                                                     ‫خیار ره >‬
 ‫وثراست که شعرا ومنشیان‌باشند‪ -‬وعاشقان ودل‬                         ‫خیار چنبر‬       ‫بفتح زای هوز» شوشة‬
              ‫‪4‬‬   ‫داد گان را هم گویند‬          ‫از دست‬      ‫خباررا گویند‪ ,‬و آن‌خاری‌باشد درازو |نرا هر ی‬


  ‫را‪ :‬خي
==================== LEAF 261 printed~ 804
                                                                                                ‫سب‬   ‫ست ‪۵ ۱‬‬




 ‫خر د بکسراول بروزن هیر» سر گشته‬                      ‫خیتال ‪ -‬بروزن‌یتال‪ .‬بمعنی دروخ‪-‬‬
 ‫وحیران‌باشد ‪ -‬وهرزه وعبث وبی‌لقریب وبی‌سبب‬           ‫ومزاح وخوش‌طبعی ومطایبه باشد‪ .‬وبمعنی مزاج‬
‫و تیرکی و غباری را نیز‬         ‫رگاونیبزند ‪- ۵‬‬                                      ‫و طبیعت همگفته‌اند‬

‫کفته‌اند که درچشم بهم رسد © ت ونام کلی است‬
                                                      ‫خچ ‪ = ۱‬با ثالی مجهول بر وزن هیچ‪,‬‬
 ‫که آنرا خیری وهميشه بهارگوبند ‪ - ۷‬ومردم‬              ‫خیش و آهن جفت باشد » بعنی آهنیکه بدان‬
 ‫بیجیا وییشرم ‪ - ۷‬ورلد ودلیررا همگفته‌اند ‪3 ۷‬‬
                                                                                    ‫زمین رشایار کنند ‪.‬‬
‫و بقتح اول گاهی بجای نه استعمالکنند ‪ ۸‬که‬
                                                      ‫حید ‪ -‬بروزن بد ‪ .‬مخفف خوید است‬
                ‫لااست ویعری نقیض شر باشد ‪.‬‬
                                                      ‫که غلهةٌ دانه نرسده باشد عموماً ‪ -‬وجو سبزرا‬
 ‫خبر بوا‪٩‬‏ = پکسر اول وضم بای امد‬
                                                                                    ‫گوبند خصوصا ‪. ۴‬‬
‫وواوبالف کشید» ‪۰‬بمعنی‌هیل (‪ )۱‬است کهبعربی‬
                            ‫قاقلةٌ صغار گوبند ‪.‬‬       ‫خیدنآب بروزن دسن‪ .‬سی کج شدن‬

 ‫خیر حبر "*‪ -‬بخاای نقطهدار(‪ )۲‬بر‬                                                           ‫و خم گردیدن ‪:‬‬
‫وزن شیر گیر » ابن کلمه از توابع است بمعنی‬             ‫وخم‬   ‫‪.‬کج شده‬    ‫د ده‬    ‫برورن‬      ‫‪۳ ۵‬‬   ‫یل‬


 ‫هرزه‌وبپوده وبی‌حبب وبی‌نقریب‌باشد‪-۱۷‬وبمعنی‬          ‫کردیده وچفته وخمیده گروابند ‪ -‬ویشم و پنبة‬
 ‫تیره وتاربك هم گفته‌اند ‪ -۴۷‬وبمعنی شوخ‌شوخ‬                            ‫آزهم باز کردم را نیز گفته‌اند‬

                                                  ‫(‪ )۷‬چك ‪ :‬با خا‪.‬‬           ‫(‪ )۱‬چش‪ :‬هل ‪.‬‬

   ‫‪-۴‬مصحف «خمیدن*‪.‬‬              ‫رك ‪ :‬خوید ‪.‬‬       ‫‪۳‬‬         ‫(«‪.‬م‪: ).‬‬   ‫هش‬      ‫(ھ‪.‬م‪= ).‬‬     ‫خش‬       ‫=‬   ‫‪۱‬‬

   ‫رك‪ :‬خیرخیر »خیره ‪.‬‬      ‫‪۵‬‬         ‫‪.‬‬   ‫اسم مفعول از «خیدن» رك ‪ :‬لفت فرس ‪۲۱6‬‬                   ‫‪۴‬‬
   ‫‪ -‬کلمه عربی است و مسنوان‬               ‫‪ - ¥‬رك ‪ :‬خیره ‪.‬‬               ‫‪.‬‬   ‫رك ‪ :‬خیری‬           ‫‪۱‬‬

                 ‫= ‪( 61۳00081720‬فر) «لك ‪۲‬س‪. *۸‬‬                              ‫تفال بنیکی »استعمال‌شود ‪.‬‬
   ‫‪ 0-۸‬ومثال دادم تا گوسپندان من بفروشند تااگر چه 
==================== LEAF 262 printed~ 805
‫= ‪.‬‬
                                                                                                                       ‫خیرو‬

 ‫نغری ‪:‬کان ات‬           ‫تاوزن‬           ‫خیری‬                                                ‫حم بنظرآمدہ است‬
‫وانواع آن بہار ا‪:‬ستیکی ازآنها سیاه رنگ‬
                                                                 ‫خیرو = بااول بثالی رسیده والث بواو‬
‫میباشد وآنرا خیری خطابی میگویند ودبگری‬                           ‫» بمعنی خطمی باشد ‪, ۱‬و بعضی گوبند‬
‫رنگ‬           ‫ت‬
                                                                                                                       ‫کشیده‬
              ‫ف و‬
                ‫هدنی‬
                   ‫بئفش است و آنرا خبری مسر‬
                                                                 ‫نوعی اگزل‌خطمی است وآن‌سرخ رنگ وسفید‬
‫دیگر سفید و سرخ است و آن‬                    ‫عی‬
                                             ‫نندو»‬
                                                 ‫وان‬
                                                   ‫خو‬            ‫رنگ هم میباشد وخبازی ‪ ۴‬همان است وممرب‬
‫گونند ‪,‬‬       ‫صحرا‪:‬بی میباشد و آنرا خبری خرامی‬
                                                                 ‫آن‌خیروجاست » وبضی گفته‌اند خیری ‪ ۴‬است‬
‫است وآنرا خبری شیرازی‬                   ‫زعرد‬
                                           ‫وبك نو‬                ‫که گل‌هميشه بهارباشد‪,‬وبمعنی‌اول بازای‌نقطه‌دار‬
‫‏‪a‬‬                                                                                                     ‫نیز بنظر آمده |بسح‬
‫عصفیر و عسفیره خوانند (‪ . )۱‬طبیمت آن گرم‬
 ‫الدکه‬         ‫ته‬
                ‫فی‬‫زوکرا‬
                      ‫و خثك است ‪ -‬و خر‬                            ‫=روزن تیره » غباری رگاویند‬
                                                                                           ‫حیره ب‬
‫خبازی باشد ‪ - ۴۷‬وبمعنی صفه وابوان و طاق‬                          ‫که درپیش چشم پدید آبد ‪ - ۴‬و بمعنی شوخ‬
‫وروأق‌هم هت ‪٩٩‬‏ — ورنگ سرخرا نیز گونند‪.‬‬                          ‫دیده ویشرم وآبزیرم وهرزه وناهموارویحیا *‬
‫حیز ‪ -‬بکسر اول وسکون انی و زای‬
                                                                 ‫ولجوج وس رکش وسخن ناشنوباشد‪ -‬ورند وشجاع‬
                                                                  ‫رایز گفته‌اند؟ ‪ -‬ویمعنی بی‌سیب وبنهوده‬
                                                                                                                            ‫ودلیر‬
‫هوز‪.‬بمعنی برخاستن وبرجست
==================== LEAF 263 printed~ 806
  ‫کز عتارم‬                                                                                                         ‫‪ ۵ ۳‬بزح‬




                                                                     ‫ازمردم همان‌دایره میگوید که «برخیزوبگیر»‬
 ‫آهته بجایی درشدن باشد ‪ -‬وبمعنی لبغدزن‌هم‬                                                                    ‫را‬
‫هست ‪-‬ونشته‌و(‪)۱‬بچهاردست وپابرامرفتن اطفال‬                            ‫وود بجای او مینشیند » وآن شخص از دبال‬
                                                                                                         ‫خ‬
                                              ‫را لىز کوبند ‪۱‬‬         ‫دوندة اول میدود و او میگریزد و همجنن آن‬
‫‪ -‬بروزن پیش (‪. )۲‬وز اری باشد‬                     ‫خیش‬                 ‫مقدار که خواهند نورآاخیز گیر بحذف بای‌ابجد‬
                                                                                                             ‫حم وگو نی‬
 ‫زراعت کردن » وبسنیکرد آهنی است‬                           ‫دجهت‬
‫وبعضی گونند‬                ‫که زمن را مدان شار کنند ‪۷‬‬                 ‫جآمنز»بوارای‌فر شت بروزن مزبان ‪.۱‬‬
‫است که آهن را بدان محکم سازند ‪۰‬‬                             ‫ری‬        ‫و نبیاشد که بخم شدن نشکند‬                ‫نوعی اچزوب‬
‫بد چوبی است که بر گردنگاو‬                            ‫ودیگری ‪2‬‬        ‫وازآن تازبانه سازنف ‪ -‬وبفخ درخت سرو را نفز‬
 ‫نهند ‪-‬ونوعی آزیارچه وبافة کتان حم هت ‪- 4‬‬                                                                            ‫کویند ‪.‬‬
‫وجامةٌ پنبهآ کنده را گویند بمنی چیزی کهآ نرا‬                                               ‫خیز ران بلدی ‪۴‬‬
                           ‫باشند ‪۰‬‬     ‫تمه‬
                                         ‫ا بفاه‬
                                              ‫بنبه‬
                                                 ‫بپاشم وپ‬            ‫‪FE‬‏‬         ‫ند ‪۳۳۳‬‬          ‫اسفرم راکو‬        ‫ولام » مورد‬


 ‫خشاوه = بفتح وأو بر وزن بجاده »‬                                                                        ‫ات‬     ‫گرم وخشاك‬


                                                                      ‫» ‪:‬مەی خر‬         ‫بروزن زننده‬    ‫<یز لل و‬
                                 ‫‪۰‬‬    ‫و‬       ‫شار کرده‬      ‫رمن‬


       ‫‪ .‬خا‬           ‫شه‬
                       ‫ن‬ ‫اب‬
                          ‫خزن‬
                            ‫رو‬            ‫‪-‬‬   ‫خیشخانه‬                      ‫وحجم‌نده ویربای ات مه و أغز نده باشد‬        ‫‪۴‬‬

‫باشد که ددهت دقع حوای
```


## [2026-09-07T20:18:34.658Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ns=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=s.split('\\f')\nprint('='*20,'LEAF 263 FULL')\nprint(leaves[263])\nprint('='*20,'LEAF 264')\nprint(leaves[264][:2000])\nEOF"
}
```


### [2026-09-07T20:18:35.958Z] TOOL RESULT

```
==================== LEAF 263 FULL
  ‫کز عتارم‬                                                                                                         ‫‪ ۵ ۳‬بزح‬




                                                                     ‫ازمردم همان‌دایره میگوید که «برخیزوبگیر»‬
 ‫آهته بجایی درشدن باشد ‪ -‬وبمعنی لبغدزن‌هم‬                                                                    ‫را‬
‫هست ‪-‬ونشته‌و(‪)۱‬بچهاردست وپابرامرفتن اطفال‬                            ‫وود بجای او مینشیند » وآن شخص از دبال‬
                                                                                                         ‫خ‬
                                              ‫را لىز کوبند ‪۱‬‬         ‫دوندة اول میدود و او میگریزد و همجنن آن‬
‫‪ -‬بروزن پیش (‪. )۲‬وز اری باشد‬                     ‫خیش‬                 ‫مقدار که خواهند نورآاخیز گیر بحذف بای‌ابجد‬
                                                                                                             ‫حم وگو نی‬
 ‫زراعت کردن » وبسنیکرد آهنی است‬                           ‫دجهت‬
‫وبعضی گونند‬                ‫که زمن را مدان شار کنند ‪۷‬‬                 ‫جآمنز»بوارای‌فر شت بروزن مزبان ‪.۱‬‬
‫است که آهن را بدان محکم سازند ‪۰‬‬                             ‫ری‬        ‫و نبیاشد که بخم شدن نشکند‬                ‫نوعی اچزوب‬
‫بد چوبی است که بر گردنگاو‬                            ‫ودیگری ‪2‬‬        ‫وازآن تازبانه سازنف ‪ -‬وبفخ درخت سرو را نفز‬
 ‫نهند ‪-‬ونوعی آزیارچه وبافة کتان حم هت ‪- 4‬‬                                                                            ‫کویند ‪.‬‬
‫وجامةٌ پنبهآ کنده را گویند بمنی چیزی کهآ نرا‬                                               ‫خیز ران بلدی ‪۴‬‬
                           ‫باشند ‪۰‬‬     ‫تمه‬
                                         ‫ا بفاه‬
                                              ‫بنبه‬
                                                 ‫بپاشم وپ‬            ‫‪FE‬‏‬         ‫ند ‪۳۳۳‬‬          ‫اسفرم راکو‬        ‫ولام » مورد‬


 ‫خشاوه = بفتح وأو بر وزن بجاده »‬                                                                        ‫ات‬     ‫گرم وخشاك‬


                                                                      ‫» ‪:‬مەی خر‬         ‫بروزن زننده‬    ‫<یز لل و‬
                                 ‫‪۰‬‬    ‫و‬       ‫شار کرده‬      ‫رمن‬


       ‫‪ .‬خا‬           ‫شه‬
                       ‫ن‬ ‫اب‬
                          ‫خزن‬
                            ‫رو‬            ‫‪-‬‬   ‫خیشخانه‬                      ‫وحجم‌نده ویربای ات مه و أغز نده باشد‬        ‫‪۴‬‬

‫باشد که ددهت دقع حوای کرم از کتان ساز ند‬                             ‫و آن چنان باشد که‬           ‫نووعی از بازی ههمت‬
 ‫ووزون‌آن بر که مد بگتراند و براطراف آن‬                              ‫از خود‬     ‫ودست‬     ‫ترهی نادف‬    ‫کودکان بر‬
                                                                                                      ‫خاك‬    ‫وده‬

 ‫آب میپاشند و این بمتز لهخسخانة هشدوستان‬                              ‫برداشته فرو لغزند‪ .‬و این بازیر! عرب زحلوفه‬
 ‫است‪ - 4‬وییراهن کتان‌رانیز گفته‌اند*‪ -۷‬وبعضی‬                                                            ‫کودند ‪.‬‬
 ‫کوند خانه‌ای باشد که آنرا ازنی وعلف سازند‪.‬‬
                                                                      ‫خیز وان ‪ = ۴‬بروزن ومعنی شبروان‬
 ‫وبعضی دبگر گوبند خانه‌ای باشد که اطرافآنرا‬                                ‫‪۰‬‬   ‫ومشهور‬    ‫باشد معروف‬   ‫وان ولاشی‬         ‫‪۳‬‬    ‫ارت‬

 ‫ازخارشتری برآورند وازبیرون پیوسته آب‌بران‬
                                                                      ‫خیزه گیره سباکاف‌فازسی بروزن خیره‬
‫پاشند واز درون بادکنند بجهت دفع کرما واین‬
‫درسیستان متعارفست؟ ‪ -‬ودرسرمه‌سلیمانی بمعنی‬                                ‫خیره » بمعنی خیزبگیر است‪,‬وآن نوعی ازباز‬
                                                                                                ‫وفته شد؟ ‪.‬‬ ‫باشد گ‬
‫زر خالس حم آمده است ؛ و صاحب فرهنگه‬
 ‫جهانگیری‌بمعنی اولکه خیمهٌ کتان باشد باسین‬                           ‫= بروزن‌بیجیدن ؛ بم‌عنی‬         ‫خیز بدن ‪°‬‬
                                                ‫(‪ )۲‬چك‪ .‬چش ‪ :‬بیش‬                            ‫(‪ )۱‬چكت‪ .‬چش‪- :‬‬
       ‫‪ - ۱‬در عربی بفتح اول وضم سوم *تفی» خ=یزور (بفتح‌اول) «(مند» = ‪asub‬‏ ‪maB‬‬
   ‫‪.‬‬    ‫_‬       ‫لاب ‪۹‬‬          ‫‪ 2‬کل‬   ‫ناز کف و یلد ومحکم‬         ‫‪ ۰‬دارای سافه های‬       ‫ازکندمان صنه‌می از دسته علات‬

                ‫المالم و‬    ‫در جدود‬       ‫‪۴‬‬             ‫‪( houx_ frelon‬فر) «لك‪۲‬س “‪a۸‬‏ ‪.‬‬                      ‫‪۴‬‏ =‬
  ‫آزین‌قبیل‪« :‬خواندیدوراناو» ‪۳0۳‬‬                        ‫عض اشمارخافانی ‪۳۳‬‬
   ‫<< خاستن (ه‪.‬م‪).‬‬                        ‫‪ -‬بهلوی ‪0‬‬                            ‫‪e:‬‏‬             ‫‪۴‬‬         ‫خیروان »ر‬
                                                 ‫‪۰‬‬    ‫‪ ۹‬ڪڪ ر کف‪ :‬خر دن‬                     ‫«اسشق ‪« ۲۹4۰‬بونکر ‪.۱۱۱‬‬
       ‫‪ = ۲‬خیچ (ه م‪<- ).‬هیش (ه«‪.‬م‪ . ).‬اوستا ‪, 231563‬پهلوی "‪( 56:2‬؛) «استق‪.*۵۱۵‬‬
   ‫لیز‪ .‬پرده‌ماسیتست اوز پارچهُ مزبور که در اطاق هی آویختند و ؛برای سردی آنرانمنالك‬                           ‫‪۸‬‬              ‫‪۱‬‬


   ‫برآوردند خواب قلوله را وآن‌را مرملها ساخمند وخشها | وبختند»«تاریخ‬                             ‫«تاخایه‌ای‬    ‫میکردند ‪:‬‬
            ‫‪۰‬‬     ‫‪ :‬جه‬     ‫‪+‬‬    ‫‪۹‬‬             ‫خشن خانه‪. ‎‬‬    ‫رك‪:‬‬    ‫‪_ ٩‬‬           ‫‪.‬‬      ‫نه‬‫ا‪:‬‬
                                                                                            ‫خرك‬
                                                                                              ‫ی‪۱‬ش ‪.‬‬
                                                                                                  ‫خ ‪۲۱‬‬
                                                                                                     ‫بیهقی ص‬

==================== LEAF 264
                                                                                                                            ‫خیشفوج‬
 ‫==‬




‫میگویند نه مطلق خوی را؛ وبسضی کویندبمعنی‬                                                ‫بی‌نقطه آءرده است (‪ )۱‬اه اعلم ‪.‬‬
‫اول عربیادت ‪ -‬وحوالی باشد کهآنرا ازرسمان‬
                                                              ‫حیشفو ج ‪١‬‏ بفتح اول و سکون ثانی‬
‫پنبه بافته باشند ‪ -‬و رندش زوده و شکنبه را‬                     ‫وفتح ثالث وفای بواورسده و ‪,‬جم زده ‪,‬دنبددانه‬
‫روده‬       ‫و‬   ‫از شکنده‬    ‫انجه‬   ‫ەی‬
                                                                 ‫راگویند وبعربی حب‌القطن‌خوانند‪ .‬سینه وسرفه‬
     ‫۔‬
     ‫سشمدبهم‬
           ‫ری‌چ‬
              ‫بتراشند ‪-‬وفی وچر کیکه‌در گوشها‬                                                                    ‫را ناف ات ‪8.‬‬
‫ولعابی که آزدهان وبینی مردم براید ‪ -‬و بمعنی‬
                                                                 ‫بر وزن فیل ‪۰‬‬             ‫(ل‪)۲‬‬
                                                                                             ‫حیل ‪ -‬بکر او‬
                                                              ‫اماب علدظی را بند که ازبینی‌مردم‌برمیآید ‪۴‬۔‬
‫را‬    ‫دبوانه ومحنون‬        ‫هم آمده است ك‬           ‫جراحت‬


‫و بفتح اول درعربی بمعنی خیمه‬                ‫نیز گوبند ‪-‬‬        ‫و بفتح اول در عربی بمعتی جماعت و طایفه‬
                                                 ‫باشد ‪. ¥‬‬                                                                           ‫ماش ‪.‬‬
 ‫خیمه از دق کنابه اآزسان است ‪.‬‬
                                                             ‫خیل تاش ‪ ۴‬ح بفوافانی بالفکشیدہ‬
‫حیمه بصحر ا رذن = کنابه از‬                                   ‫وك‌کریرا گوبند که‬                   ‫‪ ۰‬سیاهی‬    ‫شین نقطه‌دار زده‬


 ‫عایب شدن باشد ‪ -‬ویمعتی آ شکارا وبی‌پرده بودن‬                    ‫همه ازيك خیل وبك طایفه باشند‪ .‬وصاح خیل‬
                                             ‫‪.‬‬     ‫هم ھت‬
```


## [2026-09-07T20:18:52.335Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN leaf 520 (p.496) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==521 {print}' SYN.txt | head -80\necho \"=== SYN grep PLOW ===\"; grep -n \"PLOW\\|8\\.21\" SYN.txt | head -20"
}
```


### [2026-09-07T20:18:53.610Z] TOOL RESULT

```
=== SYN leaf 520 (p.496) ===
boden (diele, es-
trich)
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
SELECTED INDO-EUROPEAN SYNONYMS
lit. ‘wind-eye’, cpd. of the words for ‘wind’ and ‘eye’. Falk-Torp 1383. ON gluggr (Sw. glugg ‘hole, opening’) fr. Gme. *gli- beside glo- in ON gléa, OE glowan ‘glow’, hence orig. ‘opening for light’ (cf. ON Wore ‘opening in the roof’ : js ‘light’). Walde-P. 1.627, Hellquist 288. 5. Lith. langas, Lett. lwogs, OPruss, lanxto, etym.? Possibly orig. a Swinging window and so: Lith. linguoti ‘swing back and forth’ (Leskien, Ablaut 334 with?). Late ChSI. okno, etc., general Slavic (but SCr. okno ‘window pane’) : ChSI. oko, Lith. akis ‘eye’, etc. Walde-P. 1.171. Brickner 377. SCr. prozor, fr. through’. SCr. pendzer, fr. Turk. pencere ‘win- dow’. Lokotsch 1648. 6. Skt. vatdyana-, lit. ‘wind-passage’, epd. of vata- ‘wind’ and ayana- ‘going, course’. Skt. gavaksa-, lit. ‘ox-eye’ (cf. NE bull’s-eye), epd. of gava- ‘ox’ and aksa- ‘eye’. Also grhaksa- (rare) lit. ‘house- eye’. Skt. jala- ‘net’, also ‘lattice-work win- dow’. Av. raotana- (NPers. rozan) : Skt. rocana- ‘bright’, locana- ‘eye’, etc. Barth. 1489.
pro-ziratt ‘look
D
en- qoor’ are mostly from &
like ‘bottom, ground’, ‘Hat flect a particular
oard’, or form of
Heese ‘bottom, ground’, and _ and Delian inscrip- sas ‘surface of the d Hom.
d’, and ‘floor (as ) ae words prob. cognate, ction dub. Walde-P.
( se uS' Boor’ (Pro 4s and 952.44), cpd. of
4,823, 43 : fr. dn : Souos ‘house’, etc. and by ‘ground’. Walde-P. 1.787.
Crk, réros ‘path’, Byz. (with new meaning fr. rar ‘tread’) ‘floor’ (> SCr. patos ‘Hoor’), NG ‘bottom’. Hence also, or better fr. the verb rar ‘tread’, after theanalogy of other derivs. in -wya, Byz., NG xérwpa. ‘floor’.
2. Lat. pavimentum, the normal tech- nical word for the Roman ‘floor’, fr. pavire ‘beat, tread down’ : Lith. piauti ‘cut’, ete. Hence It. pavimento ‘floor’, hile other Romance derivs. mean pavement’ or Rum. pdmint ‘earth’ (121), Walde-P, 2.12. Ernout-M. 743. REW 6312, fing solum ‘bottom, ground, soil’ nae oo oe Hence Sp. suelo,
oor’. REW 8079. pa’ EW Gist eS
Um, pard s 70s ‘oor, ee deriv. of (?Byz. ré- ard’, Orig, a ‘m blance to a leo
Turk. déseme Tiktin 590,
WELLING, HOUSE, FURNITURE
ized by Arya Samaj Foundation Chennai and eGangotri
471
MHG vluor, NHG flur ‘field, plain’ and ‘vestibule’); all orig. ‘flat surface’, fr. the same root as Lat. planus ‘flat’, etc. Walde-P. 2.61 f.
4, ON golf, Dan. gulv, Sw. golv, in ON also ‘an apartment’, etym.? Falk- Torp 361. Hellquist 293.
OE flor, etc., above, 3.
OHG dil, dilla, MHG dil, dille, NHG diele ‘board’ and ‘wooden floor’ : OPruss. talus ‘floor’, ChSI. tilo ‘bottom, ground’, Skt. tala- ‘surface’, etc. Walde- P. 1.740. Weigand-H. 1.354.
OHG astrth, MHG esterich, NHG estrich ‘stone floor’ or ‘cement floor’, fr. MLa
=== SYN grep PLOW ===
3545:4. OF a&pum (also ‘sister’s husband’), OHG eidum, MHG eidem, NHG eidam, perh. (Gmc. *aibuma-) : Osc. aeteis, Grk. afca ‘portion’ and orig. applied to an evecare a& man’s heiress- Static: | ane ‘Gon ae 1918.216 ff. Kluge-G.123, ee ay schwiegersohn, dial. toch-
5945:Skt. vadana-, vaktra- ‘mouth’ as organ of speech, fr. vad-, vac- ‘speak’ (18.21).
8213:5. Lith. nebylys, neg. cpd., second part : byloti formerly the common word for ‘speak’ (18.21).
12204:CHAPTER 8 th AGRICULTURE, VEGETATION! : . A 8.11 FARMER 8.44 Bariey ac : 8.12 Frexp (for Cultivation) 845 Rys dl ¢ 8.13 GarRDEN 8.46 Oats i ‘a 8.14 Barn 8.47 Marzz, (U.S.) Corn q 8.15 Cuurivats, TLL 8.48 Rice Me ; 8.21 Pxow (vb.; sb.) 8.51 Grass ht : 8.212 Furrow 8.52 Hay a i 8.22 Dic 8.53 PLant al 8.23 SpavE 8.54 Roor ( 8.24 SHovEL 8.55 Brancu ba 8.25 Hor 8.56 Lear ere 8.26 Tork 8.57 FLowER me 8.27 Raks 8.58 Rosz M 8.28° Harrow 8.60 Tree = 1.42 * 8.31 Sow; Srep 8.61 Oak 8.32 Mow, Reap a oe Bo 8.33 Sickie; ScyrHE 8, 64 ei i 8.34 THREsH 8.65 = t in ? 8.35 TsresHinc-Foor 8.66 hee 8.41 Crop, Harvest 8.67 VINE mS 8.42 Grarn (Generic = British Corn) 8.68 Tosacco ‘co 843 Wxeat 8.69 SmoxE (Tobacco) (6. ink 8.11 FARMER - Grk. — -yewpyés Goth. (airpds) waurstwja i ikini ini : . Lith kininkas, laukinin- NG —-yewpyds, xwpixds, ON bondi, akrmasr, to, ieee a i fal Ra Lat. aa Dan. — dyrker, landmand, Lett. laucinieks, zemnieks Ia Hiesehee “aactnctiorglontts bonde ChSI. délatelt, tezatelt the : as ae iiva- Sw. dkerman, jordbru-  SCr. __ratar, teak, seljak 1 Tr ant re fee kare, bonde Boh. __rolnik, sedldk i ; 4 ee pied tiva- OE = (eord)tilia, wcerman, Pol. _rolnik, chlop It Sp Waban RUE gebir, etc. Russ. zemledelec, krest'ja- thi pes f r “i agricultor ME husbond(man), acre- nin, muzik DD Ir, : eke He abe man Skt. ksetrakarsaka-, P Nir. paecmba ugar Ne eld (husbandman) kselrapati- W. amaethwr, ffermur OHG ee ae Av. vdstrya-
12263:Late ChSl. ratajt, SCr. ratar, rataj, lit ‘plow-man’ : ChSl. orati ‘plow’, etal (8.21).
12303:Boh. role, Pol. rola, late Chs). ralijq : ChSl. orati, ete. ‘plow’ (8.21), Miklo. sich 225. Briickner 462,
12396:on, ex i i : » €xpressions for th Some Verbs for ‘plow’ (8.21) ie
12408:3. Ir. airim ‘plow’ (8.21), also in wider sense ‘cultivate’. Hessen s.v.
12430:Russ. pachat’ ‘plow’ (8.21), also used in wider sense ‘cultivate’. :
12431:7. Skt. krs- ‘plow’ (8.21), also ‘cult- vate’(?).
12436:AGRICULTURE, VEGETATION 495 8.21 PLOW (vb.; sb.) Goth. arjan; hoha Lith. arti; pligas, arklas, «gpoTpv erja, plagja; ardor Zagre ap OP rarv00Sei on Ear Lett. art; arkls anerpt Dan. pldje; plov ChSI. orati; ralo ardre; ee ro Sw.  ploja; plog SCr. �� orati; plug arate, solearé; OE erian; sulh Boh. orali; pluk JaboureTs charrue ME ere; plogh Pol. oraé; plug arar; araa0 NE plow; plow Russ. achat’ (orat’); plug, ara; plug = Du. ploegen; ploeg socha * girim; ar aliens aM OHG  erren; pfluog Skt. krs-; lavigala-, sira-, treabhatmns MHG pfluegen, ern; pfluoc hala- ae Capa NHG _ pfliigen; pflug Av. karS-; aéSa- Br. arat;
12442:3. It. solcare, fr. Lat. sulcdre ‘furrow, plow’ (poet.), deriv. of sulcus ‘furrow’ (8.212).
12457:OE sulh : Lat. sulcus ‘furrow’, etc. (8.212).
12470:8.212 FURROW
12497:7. Skt. stta-, perh. fr. IE *sé(z)- ‘throw’ and ‘sow’ (8.31). See under Skt. stra- ‘plow’ (8.21).
12498:Skt. karsi-, Av. karga-, fr. Skt. krs-, Av. kars- ‘draw’ and ‘plow’ (8.21).
14312:Br. regi, prob. a variant of Tega ‘to furrow’, a deriv, of OBr. rec=W, rhyop ‘furrow’ (8.212). Henry 231.
17485:Byz., NG made, widespread pop. word for ‘run, run hard,’ fr. érvAad& (at- as in mvyobv ‘chin’, 4.209), epd. of Aadd (cf. 18.21) in its sense of ‘shout? to do- mestic animals, and so make them run (wtKadS in Patmos, according to an in- formant, is reg. used for ‘drive’ sheep, goats, etc.) Korais, “Araxra 1.303 f. Pernot, Phonétique des parlers de Chio 319. Bac. B&Bys, ’AGnva 29, mapapr. 39 ff.
23571:NIr. tuilleadh (followed by nom. or gen. or by de or is, freq. also with pro- leptic a ‘its’, ef. Dinneen), lit. ‘addi- tion’, Ir. twilled id., fr. a verbal stem to-lin-, cpd. of linaim ‘fill’ : Lat. plénus ‘full’, etc. (18.21). Pedersen 2.567.
26470:garédan ‘be mindful of’, radjan ‘speak’ etc. (18.21). Mihl.-Endz, 3.495. Traut’ mann 235.
```


## [2026-09-07T20:18:53.731Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN_1966 eight ===\"; grep -n \"^eight,\" KLN_1966.txt | head; grep -n \"^eight\" KLN_1966.txt | head\necho \"=== GPL leaf 53 (p.41) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==54 {print}' GPL.txt | head -70"
}
```


### [2026-09-07T20:18:54.990Z] TOOL RESULT

```
=== KLN_1966 eight ===
12734:eight,  adj.  and  n.  —  ME.  eighte,  eihte,  fr.  OE. eahta,  rel.  to  OS.  ahto,  ON.  atta,  Swed.  dtta, Dan.  otte,  OFris.  ahta,  Du.  acht,  OHG.  ahto, MHG.  ahte,  G.  acht,  Goth,  ahtau,  ‘eight’,  and cogn.  with  OI.  affd,  astdu,  Avestic  ashta,  Toch. A  ok  at,  B  okt.  Arm.  ut‘  (for  *optd ),  Gk.  oxtoj, Alb.  tets  (for  *okto-t),  L.  odd,  OSlav.  osmi  (re¬ fashioned  after  the  ordinal  number  osmu,  ‘the eighth’),  Lith.  astuoni,  OIr.  ocht  n-,  W.  wyth, Bret,  eiz,  ‘eight’.  All  these  words  prob.  derive  fr. I.-E.  *okto(u),  an  old  dual  form,  orig.  meaning ‘twice  four’  (Tetradic  system  of  reckoning!). The  re  in  Elian  Gk.  ortT<i>,  and  the  form  of Arm.  ut'  (for  *opto-)  is  due  to  the  analogy  of I.-E.  *septm-  (whence  Gk.  s7rra,  etc.),  ‘seven’. Cp.  also  Rum.  opt,  ‘eight’  (fr.  L.  odo),  influen¬ ced  in  form  by  $apte,  ‘seven’.  The  n  in  OIr, ocht  n-  is  due  to  the  analogy  of  secht  n-,  ‘seven’. Cp.  octa-,  octant,  octave,  octet,  octillion,  octo-, October,  octopus,  octoroon,  octuple,  utas. eighteen,  adj.  and  n.  —  ME.  eightetene,  eightene, eihtene,  fr.  OE.  eahtatyne,  eahtatene,  fr.  eahta, 'eight',  and  -tyne,  -tene,  ‘-teen’  (see  eight  and -teen);  rel.  to  OS.  ahtotian,  Du.  achttien,  OHG. ahtozehan,  MHG.  ahtzehen,  G.  achtzehn,  ON. dttjan,  atjdn,  Swed.  adertdn,  Dan.  atten,  ‘eigh¬ teen’.
12734:eight,  adj.  and  n.  —  ME.  eighte,  eihte,  fr.  OE. eahta,  rel.  to  OS.  ahto,  ON.  atta,  Swed.  dtta, Dan.  otte,  OFris.  ahta,  Du.  acht,  OHG.  ahto, MHG.  ahte,  G.  acht,  Goth,  ahtau,  ‘eight’,  and cogn.  with  OI.  affd,  astdu,  Avestic  ashta,  Toch. A  ok  at,  B  okt.  Arm.  ut‘  (for  *optd ),  Gk.  oxtoj, Alb.  tets  (for  *okto-t),  L.  odd,  OSlav.  osmi  (re¬ fashioned  after  the  ordinal  number  osmu,  ‘the eighth’),  Lith.  astuoni,  OIr.  ocht  n-,  W.  wyth, Bret,  eiz,  ‘eight’.  All  these  words  prob.  derive  fr. I.-E.  *okto(u),  an  old  dual  form,  orig.  meaning ‘twice  four’  (Tetradic  system  of  reckoning!). The  re  in  Elian  Gk.  ortT<i>,  and  the  form  of Arm.  ut'  (for  *opto-)  is  due  to  the  analogy  of I.-E.  *septm-  (whence  Gk.  s7rra,  etc.),  ‘seven’. Cp.  also  Rum.  opt,  ‘eight’  (fr.  L.  odo),  influen¬ ced  in  form  by  $apte,  ‘seven’.  The  n  in  OIr, ocht  n-  is  due  to  the  analogy  of  secht  n-,  ‘seven’. Cp.  octa-,  octant,  octave,  octet,  octillion,  octo-, October,  octopus,  octoroon,  octuple,  utas. eighteen,  adj.  and  n.  —  ME.  eightetene,  eightene, eihtene,  fr.  OE.  eahtatyne,  eahtatene,  fr.  eahta, 'eight',  and  -tyne,  -tene,  ‘-teen’  (see  eight  and -teen);  rel.  to  OS.  ahtotian,  Du.  achttien,  OHG. ahtozehan,  MHG.  ahtzehen,  G.  achtzehn,  ON. dttjan,  atjdn,  Swed.  adertdn,  Dan.  atten,  ‘eigh¬ teen’.
12735:eighteenth,  adj.  and  n.  —  Formed  fr.  eighteen with  numeral  suff.  -th  on  analogy  of  tenth.  Cp. OE.  eahtateoda,  which  was  formed  fr.  eahtatyne, ‘eighteen’,  after  teoda,  ‘tenth’;  see  tithe.  Cp.  also ON.  attjdndi,  atjandi,  ‘eighteenth’, eighth,  adj.  and  n.  —  ME.  eightethe,  eihtithe,  fr. OE.  eahtoda,  rel.  to  OS.,  OHG.  ahtodo,  OFris. acht  a,  MHG.  ahtode,  ahtede,  ahte,  G.  achte, Goth,  ahtuda,  ON.  dtti,  ‘eighth’.  See  eight  and numeral  suff.  -th.  Derivative:  eighth-ly,  adv. eightieth,  adj.  and  n.  —  Formed  fr.  eighty  with numeral  suff.  -th  on  the  analogy  of  tenth. eighty,  adj.  and  n.  —  ME.  eigteti,  fr.  OE.  (hund)- eahtatig,  rel.  to  OHG.  ahtozug,  G.  achtzig, ‘eighty’.  See  hundred,  eight  and  -ty,  suff.  denoting multiples  of  ten. eikon,  n.  —  See  icon.
34955:eighth  day  of  this  festival,  observed  on  the  22nd day  of  Tishre.  —  Heb.  shemini 'atzereth  (so  call¬ ed  after  Num.  29  :  35),  fr.  shemini,  ‘the  eighth (scil.  day)’,  fr.  shembna1',  ‘eight’  (see  tomin),  and 'atzereth,  ‘festive  assembly’,  which  derives  from the  verb  atzar,  ‘he  restrained,  kept  back,  stop¬ ped’,  and  prob.  means  lit.  ‘stoppage  (of  work)’, in  reference  to  the  abstention  from  hard  work prescribed  for  this  day;  see  Num.  29 :  35.  Heb. ‘atzar  is  rel.  to  Mishnaic  Heb.  'atzar,  ‘he  pressed, squeezed’,  and  to  Aram.  (Targum)  and  Syr. ‘atzar,  ‘he  squeezed,  pressed  out,  crushed’,  Arab. asara,  Ethiop.  'asara,  ‘he  pressed’,  Akkad,  eferu, ‘to  retain,  restrain’.
=== GPL leaf 53 (p.41) ===
the adjective precede the substantive the ی‎ or * of indefiniteness must be affixed to the noun; ۰.8. بندی دادی‎ ASS ‘good counsel hast thou given’; tS eB سکی‎ استخوانی می خورد‎ ‘a hungry dog was eating a dry bone’. Similarly, if the substantive is in the plural, it alone takes the زی‎ e.g. مردمانی خوب‎ ‘(some) good men’; بندگانی صادق‎ ‘ true (or loyal) servants’.
§ 39. Adjective used as a Subst. An adjective, whether Persian or Arabic, may be used substantively, and in that case it will be treated in every respect as a substantive; e.g. bls a learned man’; دانایان عصر‎ ‘the learned men of the age’; Jol» ‘an ignorant man’; yw ele ‘ignorant men’ ; بدهای آشعارش‎ ‘the bad things in (lit, of) his poems’,
In the rare cases which occur of a noun in the plural number in construction with what appears to be an adjective also in the plural it is generally considered that the ‘ adjective’ is used substantively in apposition. Such instances are—
Faithful servants بندگان مخلصان‎ Worldlywise sages asin پیران‎ Valiant heroes مردانن دلاوران‎
DEGREES OF COMPARISON §40 a. The comparative degree of adjectives (Persian or Arabic) is formed by adding the suffix ثر‎ tar to the positive, and the superlative by adding ین‎ in to the comparative ; e.g. ده‎ ‘good’, بهتر‎ ‘better’, بهترین‎ ‘best’; wo ‘bad’, بدتر‎ (generally contracted to بثر‎ battar, and often to بتر‎ batar) ‘worse’, بدترین‎ (contrac
```


## [2026-09-07T20:19:06.226Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 12436-12470 ===\"; sed -n '12436,12470p' SYN.txt"
}
```


### [2026-09-07T20:19:06.277Z] TOOL RESULT

```
=== SYN 12436-12470 ===
AGRICULTURE, VEGETATION 495 8.21 PLOW (vb.; sb.) Goth. arjan; hoha Lith. arti; pligas, arklas, «gpoTpv erja, plagja; ardor Zagre ap OP rarv00Sei on Ear Lett. art; arkls anerpt Dan. pldje; plov ChSI. orati; ralo ardre; ee ro Sw.  ploja; plog SCr. �� orati; plug arate, solearé; OE erian; sulh Boh. orali; pluk JaboureTs charrue ME ere; plogh Pol. oraé; plug arar; araa0 NE plow; plow Russ. achat’ (orat’); plug, ara; plug = Du. ploegen; ploeg socha * girim; ar aliens aM OHG  erren; pfluog Skt. krs-; lavigala-, sira-, treabhatmns MHG pfluegen, ern; pfluoc hala- ae Capa NHG _ pfliigen; pflug Av. karS-; aéSa- Br. arat;
The verbs and nouns for ‘plow’ (plough) go together in ore noun put not always. In the inherited group the verbs have, on the whole, been the more persistent. In the evolution of the implement, from the primitive crooked stick to the modern plow, the oldname may persist, or new words may arise (hence again, in part, new verbs) and spread as loanwords. In several languages there are different words for the modern plow and a more primitive wooden plow still used by peasants. 1, IE *ar- (*ara-, *ara-) in vbs. and sbs. common to the European languages and Armenian, but unknown in Indo- Iranian, Walde-P. 1.78. Ernout-M. 75. Walde-H. 1.69, oe a epee; Lat. arare (> It. & aig, ne ae eae ee atrim, W. ? - arjan, ON erja,
OE erian, ME ere, OHG erren, MHG
aXer, issi ? i Ey dissim, (Hatzidakis, Mec. ands) - ardtrum (> It, aratro, Sp. ee 1 W. aradr, Br. arar; taal ‘aa ett. arkls; ChSI. ralo fr Pal me 0 (but SCr, ralo, Boh. gait ‘ Pitc Mss, ralo, oralo, now us d dle Prititive Plow, or ‘plow-h : the Gian oa otherwise renIaceae iArm, araur;Toch. A fe
2. NG dpydvw, fr. dpyov dial. = épyov ‘work’. Similarly, xayarebw, fr. xaparos ‘labor’, is locally (Sparta, etc.) the com- mon verb for ‘plow’. Cf. Fr. labourer.
NG fevyapitw, fr. fevyapr ‘team of oxen’, class. Grk. fevyaprov, dim. of fetyos ‘team’.
3. It. solcare, fr. Lat. sulcdre ‘furrow, plow’ (poet.), deriv. of sulcus ‘furrow’ (8.212).
Fr. labourer, also in wider sense ‘culti- vate, till’. See 8.15.
Fr. charrue, fr. Gallo-Lat. carruca ‘wagon, wheeled plow’, deriv. of Gallo- Lat. carrus ‘wagon’. REW 1720. Ga- millscheg 210. Wartburg 2.424 ff.
Rum. plug, through Slavic fr. Gme. (below, 5).
4, NIr. treabhaim = MIvr. trebaim ‘in- habit, cultivate’, beside treb ‘dwelling place’, ete. (7.11).
Ir. cécht, Nir. céachta: W. caine ‘branch’, ChSI..sakii ‘branch’, Skt. ¢an- ku- ‘stake, post’, also (forms without nasal) Skt. gakha- ‘branch’, Goth. hoha ‘plow’, OHG huohili ‘aratiuncula’, perh. also Slavic socha (below, 7). ‘Plow’ fr. ‘branch, stick’. Walde-P. 1.335. Peder- sen 1.126. Feist 266.
5. Goth. hoha, see just above.
ON plégr, Dan. plov, Sw. plog, ME plogh (this sense perh. fr. Norse, cf. OF plog ‘a certain measure of land’), NE plow, Du. ploeg, OHG pfluog, pfluoh,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Benne ay,
a4 we 2
thes tae
Digitized by Arya Samaj Foundation Chennai and eGangotri
496 SELECTED INDO-EUROPEAN SYNONYMS
MHG pfluoc, NHG pflug; hence the vbs. ON plegja, etc.; now general Gme. for sb. and vb., the sb. also widely spread as loanword in eastern Europe (Lith. pligas, Russ. plug, etc.). Origin much disputed and quite uncertain. Walde-P. 1.812. Falk-Torp 838. Schra- der, Reallex. 2.186 f. Kluge-G. 442.
OE sulh : Lat. sulcus ‘furrow’, etc. (8.212).
6. Lith. pligas, fr. Gmc., for the mod- ern plow. For wooden plow either the old arklas (above, 1), or zagré : zagaras ‘dry limb’, OHG kegil ‘peg, stake’, Sw. kage ‘tree-stump’. Walde-P. 1.569 f.
7. ChSIl. oratz, ralo, etc., above, 1.
SCr. plug, etc., general Slavic for the modern plow, loanword fr. Gme. (above, 5).
Russ. socha ‘wooden plow’ : ChSl. socha ‘cudgel’ (Boh., Pol. ‘forked stick plow-handle’, etc.), outside connection disputed, perh. : Skt. ¢akha- ‘branch’, Goth. hoha ‘plow’, etc. (above, 4). Walde-P. 1.335. Stender-Petersen 409 f.
Russ. pachat’ (also pagnja ‘plow-land’) : late ChSl. pachati ‘shake, fan’, Russ.
pachntt’ ‘blow’, pdchnut’ ‘smell’, of Briickner 389. ‘Plow’ fr. ‘shake tyr”
the like. 3 8. Skt. krs-, Av. kar$-, both algo ‘ da pull’, beside : Skt. kargi-, Avy, karga- i
furrow’, outside connections dub Walde-P. 1.429. Barth. 456 f,
Skt. lafigala~- (RV+) perh. with lan. gula- ‘tail, penis’ : Lith. linguoti ‘swing rock’, Walde-P. 2.436. Otherwise, a, loanword fr. a pre-Aryan language Przyluski, BSL 22.118 f, :
Skt. stra- (RV+), perh., with Sita- ‘furrow’, fr. I *sé(z)- ‘throw’ and ‘gow’ (8.31), and denoting a kind of ‘drill. plow’ (i.e. for plowing and sowing) such as is attested for ancient Mesopotamia and modern India. Bloch, La charrue védique, Bull. School of Or. Studies 8.414 ff.
Skt. hala-, perh.: Arm. jol ‘post, stake’, Lith. Zuolis ‘stick, tree-trunk’; or : Arm. jlem ‘plow’ (vb.), all of dub. root connection. Walde-P. 1.629.
Av. aeSa-, NPers. xe prob. : Skt. isa- ‘pole of a plow or wagon’, Grk. otat ‘rudder-handle’, etc. (Walde-P. 1.167, without aésa-). Barth. 32.
8.212 FURROW
```


## [2026-09-07T20:19:08.380Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== GPL numerals ===\"; grep -n \"CARDINAL\\|NUMERALS\\|hasht\\|hašt\\|Cardinal\" GPL.txt | head -20\necho; echo \"=== GPL leaf 54,55 (p.42,43) ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=55 && NR<=57 {print \"--BLOCK\",NR\"--\"; print substr($0,1,1500)}' GPL.txt"
}
```


### [2026-09-07T20:19:09.753Z] TOOL RESULT

```
=== GPL numerals ===
520:Numerals—The Cardinal Numbers Al
523:IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
539:60. 1. شصت‎ for orig. شست‎ (Phi. shasht; O.P. khshvashti). 70. هفتاد مب‎ (Phi. haftat; O.P. haptaiti).
540:80. a. هشتاد‎ (Phi. hashtat; O.P. ashtaittt).
571:C: Disrrisutive NUMERALS § 52. Distributives are formed 1) by the repetition of a simple ~
2550:Tar NUMERALS I. The Cardinal Numbers
2565:ConsTRUCTION OF THE NUMERALS
2575:DistRIBUTIVE NUMERALS

=== GPL leaf 54,55 (p.42,43) ===
--BLOCK 55--
ted to (بترین‎ ‘worst’;
Formation of the Comparative 37
Jel ‘excellent’, فاضلتر‎ ‘more excellent’, فافلترین‎ ‘most excellent ’, وافعترین دلیل‎ ‘the clearest proof’.
6. These suffixes are even added to Arabic comparatives and superla- tives : as asl ‘more on * (from رافضل‎ compar. of els) ; تر‎ Gs or اولیتر‎ ‘ better, fitter, &c.’ ; اولول تربن‎ OF اولبترین‎ ‘best, &c.’ (from ءاولول‎ the masc. compar. and superlative of (ولبی‎ ۱
ce. The same suffixes are annexed to adverbs and prepositions which were originally substantives; e.g. بر‎ ‘upon, above’, py. (Phl. abar-tar) ‘higher’, برترد ین‎ highest’; پیش‎ ‘before’, پیشتر‎ ‘prior, more forward’, پیشترین‎ ‘most forward, foremost’; زیر‎ ‘under’, 39; (Phl. az-er-tar) ‘lower’, زیرترین‎ ‘lowest, nethermost’.
Rem. In the formation of the comparative, Persian follows its parent the Phl., which used the suffix éar to form the comparative, and the suffix مس‎ to form the superlative. Of the suffix éim no trace appears in Persian. To form the superlative Persian has recourse to a process peculiarly its own, viz. the intensifying of the comparative by the addition to it of the suffix %—the suffix which it also employs to form the superlative of eminence from the positive (v. § 42).
§ 41. The adjectives ده‎ ‘good’, کم‎ �
--BLOCK 56--
ing sets of suffixes for the formation of comparatives and superlatives, the first of which were added to the root of the adjective, and the second to its base or stem:
CoMPARATIVE SUPERLATIVE corresponding to S. 106 و‎ 1 S. ishtha; ۲. 5 | 1. yar! oe tov; Lat. ior; Eng. aa a a Lat. iss-; Eng. est. 2. tara (S. tara; Gr. repos). tama (S. tama; Lat. imus).
The second of these sets became, in Phl., tar, and tum, of which tar alone has been preserved in Persian. Of the first set the only traces of the comparative that remain are found in the words », 1 , 9۰ (§ 41). The words ‘good’ and ‘better’ were expressed in O.P. by
38 A ccidence
vahu and vah-yah; and in Phl. these distinct positive and compara- tive forms are both reduced to the one form veh, whence the Persian به‎ bih. It is the consciousness of the twofold origin of the form bih that has led to its use in both a positive and comparative sense. The case of the adjectives ps &c., is analogous. It follows, then, that ‘better’ may be expressed by بهتر‎ and زب‎ ‘less’ by کمتر‎ and دک‎ and so of the rest. The O.P. superlative ending in zsta is found in the two Persian words بهشت‎ bihisht ‘paradise’ (Phi. vehesht ; Z. vahishta), and نخست‎ nukhust ‘first’ (Phi. nukhust). §42 a. Construction of the Comparative. As regards the construction of the comparative, two methods are employed : 10, The object. with which the comparison is made is put im the ablative; e.g. Cre
--BLOCK 57--
� هرا ر چشم چنان کور بهتر که آفتاب سیاه blind than the sun dark’.‏ sgl ‘The fortunate arm (is) better‏ تخت به که بازوی سخت than the strong arm’.‏
6. Construction of the Superlative. The superlative, also, when expressing comparison, is constructed in three ways:
lo, By putting the object with which the comparison is made after it, in the genitive plural; e.g. خدا بهترین پادشاهان است‎ ‘God is the best of kings’,
2°. By putting the noun in the plural with از‎ after the superlative adjective; as ین از پادشاهان‎ 224 ‘the best of kings’.
3°. By using the singular after the superlative adj. without the 120704: e.g. مرد را فرماید‎ wo دو عمل‎ groves) بدترین دشمن‎ ‘the worst enemy (of the dein is he who gives two offices to one man’.
Intensive Adjectives 39‏ ALT oS‏ ترین گوهری نردم بنامی تربن شوهری
‘I will not say that I-have given a most precious jewel to a most renowned husband ’.
c. The comparative ee suffices to express the superlative ; ۰.8. بر تر است‎ op از بر ترد‎ ‘he is higher than the highest’ ; آنکه‎ x2 ‘the best thing is, that ...’; or by using it after از همه‎ of all’ , از همه" بهتر‎ این است‎ ‘this is best of all’.
Adverbial Superlative. The utmost possible degree is expressed by prefixing هر چه‎ to the comparative; e.g. sols �
```


## [2026-09-07T20:19:45.927Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== GPL 515-545 ===\"; sed -n '515,545p' GPL.txt\necho; echo \"=== BRT aesa m / 14.10 ===\"; grep -n \"aesa-  m\\.\\|aesa- m\\.\" BRT.txt | head"
}
```


### [2026-09-07T20:19:46.018Z] TOOL RESULT

```
=== GPL 515-545 ===
‘Though, in the estimation of lovers, I should become the very worst
of men (lit. ���the bad of the bad’), even so, it is better that self should be the object of my love’.
Tue ApsECTIVE oF ASTONISHMENT OR ADMIRATION
$45. The adjective of astonishment also belongs distinctly to the class of intensive adjectives. It is formed by adding the suffix تا‎ (sdle (الفب‎ to the simple adjective; as بدا‎ ‘how bad! or very bad’ (is) ; Te ‘how great, very great’ (is); Ly ‘how many’! خوشا‎ ۴ pleasant! how lovely’! In construction it usually precedes the sub- stantive, which often has a redundant |, called کلام‎ oe call ‘alif of ornamentation of speech’, or صوت‎ Se الف‎ ‘alif of extension of sound of the voice’, affixed to it; e.g. بدا سلطانیا که‎ ‘how bad (or very bad) is the king who . a0 1 بزرگا غلطا‎ “how great (is) the error’! خوشا شیرازا‎ ‘how beautiful (is) Shiraz’! ۱
Rem. The alif at the end of the adjective is by some termed ws? will ‘the .alif of astonishment’, and کثرت‎ will ‘the 0/7 of
Numerals—The Cardinal Numbers Al
excess’; while that at the end of the substantive is called زائد‎ Call ‘the redundant alzf’. It is the latter alzf that also occurs in the
word گفتا‎ (= wa) ‘he said’, This use of alifis not found in Phl. or O.P., it has its origin in modern Persian, and is probably derived from the Arabic: cf. the final ali in the Ar. وا زیدا‎ ‘Oh Zaid’ ! وا امیر الوم تن‎ 8 for the Conumander of the Belvo? ! This alif is called 433231 eet, or in Persian .الف ندیه‎
IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
Units (احاد)‎ 1.1 eb (Phi. gvak; O.P. aiva). 5.0 5%) (O.P. paiicha).
2. ۲ 49 (OP. dea). 6. 4 شش‎ (O.P. khshvash). 3. ۳ sw (O.P. thre). 7. ۷ هفت‎ (O.P. hapta).
4. ۴ چهار‎ or le (O.P. ۲ 8. ۸ هشت‎ (O.P. ashta), 9. 4 35 (O.P. nava).
۱ Tens (عشرات)‎
0 دهد‎ (poet. also) sls (O.P. dasa).
11. ۱۱ یازده‎ (dialec.) 3335, (O.P. aivadasa).
12. ۳ دوانزده . وو دوازده‎ (O.P. dvadasa). 13. ۱۳ وو سیزده:‎ .  هدزنیس‎ (O.P. thridasa).
14. ۱۴ چهارده‎ or چارده‎ ) ۰ chathrudasa).
15. 10 بانزده‎ )0.۳۰ paiichadasa).
16. ۱۰ شانزده‎ )۰ khshvashdasa).
17, ۱۷  هدتفه‎ or هفده‎ (O.P. haptadasa).
18. ۱۸ هزده رهشتده‎ or رتجدة‎ (O.P. ashtadasa).
19. 44 $9353; ,وا زده‎ dialec. نوانزده‎ )۰ navadasa). 20. ۲۰ بیست‎ (Phl. vist; O.P. 0190860
30. r- سی‎ (Phi. sth O.P. thrisat).
40. ۰ 2 Je (Phl. chahal ; O.P. chatvaresata). 50. 0+ Ash (Phi. panchah ; O.P. patichasat).
60. 1. شصت‎ for orig. شست‎ (Phi. shasht; O.P. khshvashti). 70. هفتاد مب‎ (Phi. haftat; O.P. haptaiti).
80. a. هشتاد‎ (Phi. hashtat; O.P. ashtaittt).
90. ۰ - نود‎ (Phi. navat ; O.P. ۵۵۵۸۸(۰
42 A ccidence
Hunpreps (متات)‎ 100. 1.. صد‎ (orig. Jw; Phi. sat; 0:۳, sata), plural les. 200. ۲۰۰ دویست‎ (O.P. duye saite) and to 59. 300 ۳ شیک‎ 500. 6. wah,
THOUSANDS (آلوف)‎ ۱
1000. ۱۰۰۰ هزار‎ (Phi. hazar; O.P. hazanra), plural هزاران‎ or .هزارها‎ 10,000. _\j@ ده‎ or UJ, obs. بیور‎ (Phi. 0200۴ و‎ O.P. baévar).

=== BRT aesa m / 14.10 ===
2778:Med.  'sich  in  eilige  Bewegung  setzen,  •  j.  'aesa-  m.  'Suchen':  rasistahe  pai:S eilen';  s.  Absol.  ra^öis'.  j -äwä  vaic^mca  (?,A.)  V.6^.13,  —  g.  aese
7711:•  }.  »rszaurvaesa-  m.  Name  des  zweiten Abschnitts  der  ersten  Hälfte  der  Nacht*'; 'Sät  F.  27  b.
12538:•  j.  daesa-  m.  'Zeichen,  Otnea':  pattiHatSe ayanqmca    :^a/nanqm    ayanqmca
14808:•  j.  'paesa-  m.  'Schmuck,  Zierrat':  °sa F.  10.
22162:•  '].  vaesa-  m.  'Knecht',  der  im  Herrenhof seine  feste,  dauernde  Wohnung  hat'*:  a%ra- varam..nman5.pailTm..nmanspaitTm  nairi- kqm..  'sJs/a  ^pairyaarSusca yaozda%d gSuI
23906:•  j,  VE^S'waesa-  m.  'Strauchdieb';  yasp %W3  . .  pa'iqm  fsd.)  jasaiti  'sB  Yt  13.  ao.
24803:"  J,  'raesa-  m.,  raesah-  n.  'Schädigung'; A)  körperliche  Schädigung  überhaupt; a)  in  Bezug  auf  den  Fötus;  yeHi^a  . .  kaine . .  3^atö  garnuim  irisyeiti  .  .  ptinbyS  (sd.) irisintqtn  ralli  Hkain  baoiiS.varltahe  ci- %aya  V.  75. 1 3.  b)  in  Bezug  auf  Hunde: yS  süne  piilrtm  jainti  ..  us  va  hl  gaohm 'hwirisaiti  apa  va  ks  pathyqm  kintUaiti . .  cikayat  sBnahe  °l5  (ASn.)  baob5.varHahe üfhaya  V.ij.io;  'Vyt.44;  —  ym..spiina ahaiiyS.at»/iar3^r>m  (sd.J  irisyqn  para  as- iqm  iriHntqm  'h  cikaen  baoZs.var^iahe Hhaya   V,  75.  22,  40.  2)  Rechtsaus-
25570:■  j.  urvaesa-  m.  'vertex,  Wirbel'  im Wasser;  vansdJtavanhsm  aps  'am  Yt  14. 29.  2)  "Wende'  des  Wegs, 'Wendepunkt' der  Rennbahn:  tl  .  .  fravas>nti  darai- urvals»m  t^twanS  's?m  nsAmna  "die  . . fahren  jetit  weiter  zu  der  fernen  Wende des  Wegs,  um  den  Wendepunkt  zu  er- reichen .  ."  Yt.  IJ.  58;  —  ^fläa  as/>a  ,  . aparat  haca  *s:l^  fratanm  'am  *näs?m>ta "wie  Rosse  .  .,  die  vom  hintern  Wende- punkt (der  Rennbahn)  her  den  vorderen Wendepunkt  erreichen  wollen"  VytSjj; —  °sU  F.p.  a)  überhaupt  'Ziel,  Ende': ushme  °se  gayehe  "am  äussersten  Ziel  des LebcDs"  Y.7r.iSi  '61  H.j.15;  —  damBil'si apiml  "beim  letzten  Ende  der  Schöpfung" Y.  4J.  5;  6;  —  apjmt  ankSus  'st  "beim letzten  Ende  des  Lebens"  Y.f/.ö;  —  'sa
25923:•  ].  sata'vaesa-  m.  Name  eines  als  Gott- heit verehrten  Fixsterns:  äal  th  aps  */ra- sSvayeiti  °sS  avi  haptS.kanyvaifli  Yt  &  9; —  'SB  ralDS  x^annanuhä  YL  <?.  3  2 ;  — ta  (yä.m[.frava^ays)  kinMnti  'am  an/an tarn  asmaramca..tat.apim  ux^at-urvanm Ytij.  43;  44;  —  'saht  frapahe  sBrahe YtS.o;  S.2.13.
```


## [2026-09-07T20:19:47.758Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON files ===\"; ls -la MON_part1.txt MON_part2.txt incoming/MON/ 2>/dev/null\necho \"=== grep اختاپوس ===\"; grep -n \"اختاپوس\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head\necho \"=== grep خیش in MON ===\"; grep -c \"خیش\" MON_part1.txt MON_part2.txt 2>/dev/null"
}
```


### [2026-09-07T20:19:47.858Z] TOOL RESULT

```
=== MON files ===
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt

incoming/MON/:
total 48692
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 20113727 Sep  4 14:06 MON_2vol_Adena_v1_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4377831 Sep  4 14:06 MON_2vol_Adena_v1_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 21014767 Sep  4 14:06 MON_2vol_Adena_v2_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4331421 Sep  4 14:06 MON_2vol_Adena_v2_djvu.txt
=== grep اختاپوس ===
=== grep خیش in MON ===
MON_part2.txt:8
MON_part1.txt:9
```


## [2026-09-07T20:20:07.165Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT Pflug variants ===\"; grep -n \"Pfiug\\|Ptlug\\|Pflag\\|Pfing\\|Pflu\" BRT.txt | head\necho \"=== MON grep خیش lines ===\"; grep -n \"خیش\" MON_part1.txt | head -12\necho \"=== MON grep هشت context? skip ===\"\necho \"=== BQT v4 pdf321 for هشت ===\"; python3 - <<'EOF'\ns=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=s.split('\\f')\nprint('nleaves',len(leaves))\nimport re\nfor i,l in enumerate(leaves):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m and int(m.group(1))in (320,321,322):\n        print('LEAF',i,'pdf',m.group(1),'printed~',int(m.group(1))+1917)\n        print(l[:2200])\nEOF"
}
```


### [2026-09-07T20:20:08.520Z] TOOL RESULT

```
=== BRT Pflug variants ===
21863:•  j.  *yuyö.s»nii- ''  f.  Name  eines  land- wirtschaftlichen Geräts:  yalsqm  sayanqm västryehe ßuyanlB  alla  •»»■(ND.)''  "..Pflug und  .."  V./4. 10.
=== MON grep خیش lines ===
30295:می آو بخته‌اند؛ خیش دوسار» درساره» 
30481:خیش. چوبی که بر بینی اشتر زنند برای مهار 
58612:خیش: 8« (- خیج - هیش] () (کشا) 
58616:ضیش: 8 [- کیش - معر. خیش ] (.) 
58621:خیشخانه: (0-)308-. (امر.) خانه‌ای که از 
58622:نی و علف و خار و خس يا با پرده؟ خیش 
58627:خیشوم: : (-110()06۷۰ 2۷۵ [ع ۰] (.) ینی. س 
71505:نگشایند بلکه آوازی از خیشوم و حلق 
84584:شخش: 808 [- شخیش] (امر.) مرغکی 
=== MON grep هشت context? skip ===
=== BQT v4 pdf321 for هشت ===
nleaves 553
LEAF 319 pdf 320 printed~ 2237
[pdf page 320]
دنه نیو
خروار باشد ۱ - و بمعنی خوب و خوش و زیبا | شد۸ - و بنمن یکره ومسکه هم‌ه ت که بجریی
هم‌هت ۲ . زبده خوانند ؛ و بحذف تحتانی هم بنظر آمدم
نیمور « بر وزن طیفور : آلت تناسل | است که بر وزن لیمو باشد .
راگویند ۴ - نی نهاو ندی - نم دارویی است که
یمه ۴ - بر وزن هیمه . صف هرچیز | عربان قسب‌الزربره خوانند وآن نی باریکی‌است
راکوبند - و برقع را نیز کفته‌اند وآن‌چیزیست | است مانند فلم وباریکتر ازفلم » وآن‌تیرم رنگه
که برروی پوشند 9 . وتلخ میباشد. معده وجچگر را نافع است-
نیم هلال - یک ها , کنایه از لب نیا - بکسر هردو نون بروز ن کیمیا +
ممشوق است. بلفت سربانی نانخواء راکوبند وآن تغمی است
نیناد ۱ - با اور بثانی رسیده ونون‌بالف که بر روی خمیر نان پاشند و اجواین همان
کشیده وبدال زده, بمعنی سبر باشدو آن‌مقاومت است ‎٩‏ .
شی است باهوا۷ ۰ لیق - بکر اول و ثانی مجهول پروزن
نینوک « بنم‌نون دویم بروزن بی‌موی» | دبوء بمعتی پهلوان وتجاع ودلیر ومر‌دانه ودلاور
بفری قدریم نام قسبةٌ موصل باشد . و نام شهری ‏ وبهادر باشد *۱-. و بممنی‌ناودان هم‌آمدهء‌است ۱۱
که بونی علیه‌اللام به‌آنجا بجهت دعوت کردن | - و بکر اول و ضم ثانی بمعنی راست باش د که
مردم‌آن شهر رفته بود و وقوع بطن ماهی‌درآآنجا | نقیض کج است.
۱ يم لنکه ( صف مدل) . ۴ -ر4 : جهپانگیری » رشیدی »۰
فرهنکه نظام .
۴ - من این لیمور خود را وق ف کردم علی مبیانکم با آبها آلای.
سوزنی سمرقندی « سروری» و رك : فرهتگه نظام -
۴ - پهلوی 60286 ( بخش » سهم . جهت ) . بلوچی: 2817088 (جهت و سمت ۰
طرف ) قی : افغانی 61381 ( صف ) « هوبشمان ۱۰۹۹ » شهمیرزادی 81702 «که . ۷ص
۷ رك : اسشق ۱۹۹ و ر4 : یم پهلوی 818021 ( پیراهن مقدس ) « تاواد‌پا
4۹ وقی: لیم نن ۰ لیم‌تنه . - دراسطلاح بنایی « نیمه » پیمتی نيمه (صف)آجر بکار رود
۹-ظ . بر ساخته فرقةٌ آذرکیوان . ۷ < هوی (عر). ۸ ینوا
06() شهری درآسیای قدرم » پایتخت مملکت‌آشور واقع در کنار دجله . ر4 : قاموی
مقس ص ۲-۹۲۱ ‎٩‏ همان «زیان» است : ۹
پدرم بسکه لینیا خور شد شکم او ز نیا پر شد .
پسرسید هلی رازی « جهانگیری ».
*- پهلوی 88۷ ( شجاع . فهرمان ) [ هز. 188 ] * پونکن رس ۴۱۱۸ : * نیوه مد
دلیر و مر‌دانه بود. فردوسی (طوسی) گفت :
چوطوی و چوگودر زکشواد وکیر چو کر کین و فرهاد وبهرام نیو .>
« لغت قری ی 4۱۲ *.
۱ ممال « باو» (ه.م.) :
بر دو سوی سرآن: دوکوش چو نیو چه کنی در هی خروش وغیربو -
و۱ - رد : ینوی . سنالی خردوی « فرهنکه نظام ».

LEAF 320 pdf 321 printed~ 2238
[pdf page 321]
بواد ۲۳۸
نیو ۱۵۱ - بروزن‌میعاده بممنی‌شجات نیوراد ۸ - بارای قرشت بر وزن
باشد . و آن حالتی‌است که مردم ببب آن قوی | دیوزاد » بمعنی انتظام باشد وآن حالنی است مر
دل شولد . شی راکه تقدس وثربیت آمور میکند.
یوار ؟- بروزن دیوار» مابین زمین نیور یوار *- یک رای بی نقطه در
وآسمائرا کوبند و بعربی جو خوانند. چهپارم » بمعنی‌کائنات جواست بعنی چیزهای ی که
نیو‌اده «» با نانی‌مجهول بروزن‌بیچاره, ۱ در میان زمین وآسمان بهم میرسند همچو قوس
چوبی باشد که خمیر نانرا بدان پهن سازند ۴ . قح وشهب و نیازك و ذوات‌الاذناب *۱و برف
نیوباریدن ۴ - بنم او واتای . وبلران و ماشد‌آن , چه یور بممنی‌کائنات ونیوار
بمعنینه الباشتن وپرلکردن وفرونبودن ولبقکندن | بمعنی جو باشد.
باغد چه اوپاریدن بممنی فرو بردن و پر کردن نیوساو ۱۱() - بکراول و سین بی
وانباشتن و افکندن است ومذ کور شد که‌هرکام | نقطه بالف کشرده وبواو ددم بممنی پاینیده وی
نون مفتوحه برسر کلمه‌ای که همزه داشته باشن | زوال است و درعربی بقاه بالله خوانند.
پیاورند آن نون بمنزلهٌ لای فی است وآن‌عمزه یوسوم ۱۱- با سین بی نقله بروزن
بیای حطی تبدیل می باید . ِ ریگه بوم » شره و حرص بسیار باشد بر چیزی
نیو آش * - بکراول وفتح‌تای‌قرشت | خوردن . .
بروزن پیشکش , جماع و مجاممت را کویند. نیوش ۱۴ یکسراول وضم نانی‌وسکون
نیو آور ‎٩‏ - باتای قرشت بروزن فیل تالك و شین قرشت » امربشنیدن باشد ری کوش
ور » پممنی کبر وغرور باشد وآن بز رکه‌داشتن کن و بشنو - وشنونده را لیر کویند که فاعل
است ی خود را ودیگران را خرد شمردن. غنیدن است ۹۴.
یور ۷ « بروزن زیور . بممنی کائنات نیوشا ۳(۱۴) - یکر اول وشین بالف
باشد وکائنات در لغفت بممنی حاسلات است (۱) | کشیده » بمعنی‌شنواباشد که شنونده است- وفهم
پمنی آنچه در عالم حاصل شود . کننده ویادگیرنده رائیز گونند.
(۱) چش : باشد . (۷) چك » چش : لیوساد .
(۳) چش : نیوشان .
۱-ظ . بر ساختهٌ فرقةٌ آذرکیوان . ۴ بر ساختةٌ دساتیر « فرهنگه دساتیر
س ۰.۲۷۳ ۴ - وآترا « چویه» نیز گوبند . « جهانگیری > و رك : رشیدی .
۴ -فی از « اویاریدن > (ه.م.) - از دساتیر « فرهنگه دساتیر ص۲۷۳*.
۹ -ظ. برساخته فرقة‌آذ رکیوان . ۷ - از دساتیر : «فیور . بروزن زبورهآنچه
درکرء هو متکون وییدا شود.» « فرهنگه دساتیرضش۲۷۳ > ور : نیورنیوار» ور : قاب۱اص45.
۸-ظ . برساختهٌ فرقهآذ رکیوان. ‎٩‏ - ر4: یور . ۴ ر4: چهارمقالهٌ
عروضی طبع دوم نگارنده ‎٩‏ وتملیقات ص ۰۱۱-۹ ۱ ظ . برساختهٌ فرقهةٌ آترکیوان ۰
۴۳- رك : یوعیدن . ارنگ آسم فاعل مرخم از «یوشیدن» .
۴ - از: یوش (ربشه قمل * آمی) ۱ 
LEAF 321 pdf 322 printed~ 2239
[pdf page 322]
ساهنده ابولا
نیوشد ۱ - بروزن فروزد , بلفت زند | شنیدن کوش خود را درا زکند يا از پس‌دیوار واز
وپازند(۱) بممنی آموزد و اد کیرد باشد که از | پس پرده و امثال‌آن کوش اندازد تا سخن ایعانر)
آموختن وباد کرفتن‌است؟ ؛ ودرفارسی بعنی کوش | بشنود وبجایی که نبایدگفت بگوید. واین «منی
کند و بشنود . را بمربی استراق سمع خواند 9 .
نیو‌شنده ۴ - بکراول بروزن‌فروژند.. نیوشیدن ؟ « بکر اول بر وزن
کوش کننده وشلونده راکویند + نکوهیدن » بممنی‌شنیدن ‏ وگو شش کردن باشد۷ -
نیوشه ۴ - بکراوزوفتح شین‌نقطه‌داره | و بممتی جستن وطلبیدن وتفص ونجس لمودن
گوت‌فر| داشتن باشد بحدیتی وآن کی‌راگوبند | هم آمده است.
که چون دوشخص باهم آهسته‌حرف زننداویجهت نیون ۸ - بکر اول بروزن ریوند »
() چك : ژد وپاژند .
۱ - مضارع آزه‌ییوشیدن» (۸.م.) ۲ - رد : لیوشیدن .
ارچ اس فاعل از« نیوشیدن» (م.) ۴ - از: یوش (۸.م.) ۸۳ (یونداس مصدره
اسم معنی) رك : اسم مصدر بقلم نگارندم م۱۱ و رك: نیوشیدن؛ بممنی آرقب «ترصد » مرأقیت:
همه نيوشهٌ خواجه بنیکوبی و ساح است همه نیوعهٌ نادان بجنگه وفتنه وغوغاست .
رو دکی‌سمرقندی «لفت فرس‌س ۲۱۷ و*شرح‌|حوال‌رود کی چاپ‌نفیسی‌ج۳س ۰6۱۰۵۰
8 رد3 : یوشیدن :
چون بنشیند زمی معثیرجوشه کویدکایدون تماند جای نیوشه
ورقکندسرخ مل برطل‌د وگوشه روشن کرددجهان ز گوعه‌بگوشه
کویدکاین می‌مرا نگردد نوشه تا نخورم باد شهریار عدومال .
۶ منوچهری دامغانی . دیوان س ۱۳۵
‎٩‏ - ۵9104520 ره از :یوش( م.)-یدن(پموند مسدری)؛پهلوی 210۵9101122
( غنیدن » مخفیانه گوش دادن ) » پازد 80253010888 ۰ ازط8۵5 « نیب رکه ی ۱۵۸کر4:
افوشا , شوشاك. هرن گوید : نیوشیدن » اوستایی 880512 - 381 ( شنیدن + گوش‌دادن). قی:
#1 رقط205ع 202 ۰ بپلوی قالط ۵5 000. 1۵0 1و۵ رنه مفی: صقالطی۵و(ناه
(شنیدن) ؛ هندی باستان ريعةٌ 80۵51 , [065081ق با غٌ ( شنیدن ,کوش دادن )ء بلوچی
58 دوه ط۵5توزه «اسعق ۱۶۷۰ هوبشمان قولهرن را در نشأت دق 81810۵902
( بهمین املاء ) ( شنیدن کوش دادن » استرانف سمع ) واففانی [8810۷818 ( شنیدن . اطامت
کردن ) . از ربشة ابرانی 8098 - 081 تأیید میکند . قسی بنیز بلوچی دلقع8۵588 (شنیدن),
استی 0099۱08لع ۰ ۹0918 (شنیدن ) « هوبشمان *۱*۶۷*.
۷ - فرستاده راگفت نیکو لیوتی بگو آنچه بشنیدی ای پیزهوش,
فردوسی طوسی ۶ لفت فری ص ۲۱۷*.
چون بخم اندر ززخم او بخروشد. یر زلد بی کمان و سخت بکوشد
مرد سر خمش استوار بیوشد تا بچگان از میان خم بنجوشد
آید هر ساعتی و پس بنیوشد تا شود هیچ قیل و با شود قال +
: منوچهری دامغانی . دبوان صس ۱۳۵ ۰
۸ - معتی اول . اظ برماختهٌ فرقهآ
```


## [2026-09-07T20:20:32.103Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re,glob\nfor f in ['incoming/BQT/BQT_v4_pages.txt','incoming/BQT/BQT_v5_pages.txt']:\n    s=open(f,encoding='utf-8',errors='replace').read()\n    leaves=s.split('\\f')\n    for i,l in enumerate(leaves):\n        if re.search(r'هشت',l):\n            m=re.search(r'\\[pdf page (\\d+)\\]',l)\n            pdf=int(m.group(1)) if m else None\n            pr=(pdf+1917) if (pdf and 'v4' in f) else ((pdf-5) if pdf else None)\n            # count occurrences\n            print(f.split('/')[-1],'leaf',i,'pdf',pdf,'printed~',pr,'hits',len(re.findall('هشت',l)))\nEOF"
}
```


### [2026-09-07T20:20:33.517Z] TOOL RESULT

```
BQT_v4_pages.txt leaf 13 pdf 14 printed~ 1931 hits 2
BQT_v4_pages.txt leaf 15 pdf 16 printed~ 1933 hits 1
BQT_v4_pages.txt leaf 18 pdf 19 printed~ 1936 hits 1
BQT_v4_pages.txt leaf 28 pdf 29 printed~ 1946 hits 1
BQT_v4_pages.txt leaf 32 pdf 33 printed~ 1950 hits 3
BQT_v4_pages.txt leaf 36 pdf 37 printed~ 1954 hits 1
BQT_v4_pages.txt leaf 40 pdf 41 printed~ 1958 hits 1
BQT_v4_pages.txt leaf 42 pdf 43 printed~ 1960 hits 1
BQT_v4_pages.txt leaf 49 pdf 50 printed~ 1967 hits 1
BQT_v4_pages.txt leaf 50 pdf 51 printed~ 1968 hits 1
BQT_v4_pages.txt leaf 54 pdf 55 printed~ 1972 hits 1
BQT_v4_pages.txt leaf 59 pdf 60 printed~ 1977 hits 2
BQT_v4_pages.txt leaf 69 pdf 70 printed~ 1987 hits 1
BQT_v4_pages.txt leaf 73 pdf 74 printed~ 1991 hits 1
BQT_v4_pages.txt leaf 74 pdf 75 printed~ 1992 hits 1
BQT_v4_pages.txt leaf 87 pdf 88 printed~ 2005 hits 1
BQT_v4_pages.txt leaf 89 pdf 90 printed~ 2007 hits 1
BQT_v4_pages.txt leaf 90 pdf 91 printed~ 2008 hits 1
BQT_v4_pages.txt leaf 92 pdf 93 printed~ 2010 hits 2
BQT_v4_pages.txt leaf 93 pdf 94 printed~ 2011 hits 5
BQT_v4_pages.txt leaf 94 pdf 95 printed~ 2012 hits 4
BQT_v4_pages.txt leaf 95 pdf 96 printed~ 2013 hits 1
BQT_v4_pages.txt leaf 100 pdf 101 printed~ 2018 hits 1
BQT_v4_pages.txt leaf 104 pdf 105 printed~ 2022 hits 1
BQT_v4_pages.txt leaf 106 pdf 107 printed~ 2024 hits 1
BQT_v4_pages.txt leaf 115 pdf 116 printed~ 2033 hits 3
BQT_v4_pages.txt leaf 117 pdf 118 printed~ 2035 hits 1
BQT_v4_pages.txt leaf 118 pdf 119 printed~ 2036 hits 2
BQT_v4_pages.txt leaf 119 pdf 120 printed~ 2037 hits 1
BQT_v4_pages.txt leaf 126 pdf 127 printed~ 2044 hits 1
BQT_v4_pages.txt leaf 128 pdf 129 printed~ 2046 hits 1
BQT_v4_pages.txt leaf 129 pdf 130 printed~ 2047 hits 3
BQT_v4_pages.txt leaf 140 pdf 141 printed~ 2058 hits 1
BQT_v4_pages.txt leaf 143 pdf 144 printed~ 2061 hits 1
BQT_v4_pages.txt leaf 153 pdf 154 printed~ 2071 hits 2
BQT_v4_pages.txt leaf 158 pdf 159 printed~ 2076 hits 4
BQT_v4_pages.txt leaf 164 pdf 165 printed~ 2082 hits 1
BQT_v4_pages.txt leaf 165 pdf 166 printed~ 2083 hits 1
BQT_v4_pages.txt leaf 202 pdf 203 printed~ 2120 hits 1
BQT_v4_pages.txt leaf 205 pdf 206 printed~ 2123 hits 1
BQT_v4_pages.txt leaf 208 pdf 209 printed~ 2126 hits 1
BQT_v4_pages.txt leaf 217 pdf 218 printed~ 2135 hits 1
BQT_v4_pages.txt leaf 218 pdf 219 printed~ 2136 hits 1
BQT_v4_pages.txt leaf 222 pdf 223 printed~ 2140 hits 1
BQT_v4_pages.txt leaf 231 pdf 232 printed~ 2149 hits 3
BQT_v4_pages.txt leaf 234 pdf 235 printed~ 2152 hits 1
BQT_v4_pages.txt leaf 236 pdf 237 printed~ 2154 hits 1
BQT_v4_pages.txt leaf 239 pdf 240 printed~ 2157 hits 1
BQT_v4_pages.txt leaf 252 pdf 253 printed~ 2170 hits 1
BQT_v4_pages.txt leaf 262 pdf 263 printed~ 2180 hits 1
BQT_v4_pages.txt leaf 265 pdf 266 printed~ 2183 hits 1
BQT_v4_pages.txt leaf 267 pdf 268 printed~ 2185 hits 2
BQT_v4_pages.txt leaf 271 pdf 272 printed~ 2189 hits 1
BQT_v4_pages.txt leaf 284 pdf 285 printed~ 2202 hits 1
BQT_v4_pages.txt leaf 285 pdf 286 printed~ 2203 hits 1
BQT_v4_pages.txt leaf 332 pdf 333 printed~ 2250 hits 1
BQT_v4_pages.txt leaf 342 pdf 343 printed~ 2260 hits 2
BQT_v4_pages.txt leaf 344 pdf 345 printed~ 2262 hits 1
BQT_v4_pages.txt leaf 359 pdf 360 printed~ 2277 hits 3
BQT_v4_pages.txt leaf 377 pdf 378 printed~ 2295 hits 1
BQT_v4_pages.txt leaf 383 pdf 384 printed~ 2301 hits 1
BQT_v4_pages.txt leaf 386 pdf 387 printed~ 2304 hits 1
BQT_v4_pages.txt leaf 387 pdf 388 printed~ 2305 hits 1
BQT_v4_pages.txt leaf 399 pdf 400 printed~ 2317 hits 1
BQT_v4_pages.txt leaf 417 pdf 418 printed~ 2335 hits 3
BQT_v4_pages.txt leaf 418 pdf 419 printed~ 2336 hits 1
BQT_v4_pages.txt leaf 420 pdf 421 printed~ 2338 hits 8
BQT_v4_pages.txt leaf 421 pdf 422 printed~ 2339 hits 24
BQT_v4_pages.txt leaf 422 pdf 423 printed~ 2340 hits 5
BQT_v4_pages.txt leaf 423 pdf 424 printed~ 2341 hits 1
BQT_v4_pages.txt leaf 425 pdf 426 printed~ 2343 hits 1
BQT_v4_pages.txt leaf 427 pdf 428 printed~ 2345 hits 1
BQT_v4_pages.txt leaf 431 pdf 432 printed~ 2349 hits 1
BQT_v4_pages.txt leaf 433 pdf 434 printed~ 2351 hits 1
BQT_v4_pages.txt leaf 437 pdf 438 printed~ 2355 hits 1
BQT_v4_pages.txt leaf 439 pdf 440 printed~ 2357 hits 1
BQT_v4_pages.txt leaf 440 pdf 441 printed~ 2358 hits 1
BQT_v4_pages.txt leaf 443 pdf 444 printed~ 2361 hits 2
BQT_v4_pages.txt leaf 444 pdf 445 printed~ 2362 hits 1
BQT_v4_pages.txt leaf 458 pdf 459 printed~ 2376 hits 1
BQT_v4_pages.txt leaf 473 pdf 474 printed~ 2391 hits 1
BQT_v4_pages.txt leaf 474 pdf 475 printed~ 2392 hits 1
BQT_v4_pages.txt leaf 483 pdf 484 printed~ 2401 hits 1
BQT_v4_pages.txt leaf 485 pdf 486 printed~ 2403 hits 2
BQT_v4_pages.txt leaf 490 pdf 491 printed~ 2408 hits 6
BQT_v4_pages.txt leaf 493 pdf 494 printed~ 2411 hits 1
BQT_v4_pages.txt leaf 495 pdf 496 printed~ 2413 hits 1
BQT_v4_pages.txt leaf 504 pdf 505 printed~ 2422 hits 1
BQT_v4_pages.txt leaf 509 pdf 510 printed~ 2427 hits 1
BQT_v4_pages.txt leaf 513 pdf 514 printed~ 2431 hits 1
BQT_v4_pages.txt leaf 515 pdf 516 printed~ 2433 hits 1
BQT_v4_pages.txt leaf 516 pdf 517 printed~ 2434 hits 1
BQT_v4_pages.txt leaf 520 pdf 521 printed~ 2438 hits 1
BQT_v4_pages.txt leaf 532 pdf 533 printed~ 2450 hits 1
BQT_v5_pages.txt leaf 4 pdf 5 printed~ 0 hits 1
BQT_v5_pages.txt leaf 10 pdf 11 printed~ 6 hits 1
BQT_v5_pages.txt leaf 17 pdf 18 printed~ 13 hits 1
BQT_v5_pages.txt leaf 18 pdf 19 printed~ 14 hits 1
BQT_v5_pages.txt leaf 23 pdf 24 printed~ 19 hits 2
BQT_v5_pages.txt leaf 24 pdf 25 printed~ 20 hits 1
BQT_v5_pages.txt leaf 25 pdf 26 printed~ 21 hits 2
BQT_v5_pages.txt leaf 27 pdf 28 printed~ 23 hits 4
BQT_v5_pages.txt leaf 28 pdf 29 printed~ 24 hits 3
BQT_v5_pages.txt leaf 31 pdf 32 printed~ 27 hits 1
BQT_v5_pages.txt leaf 39 pdf 40 printed~ 35 hits 1
BQT_v5_pages.txt leaf 44 pdf 45 printed~ 40 hits 1
BQT_v5_pages.txt leaf 67 pdf 68 printed~ 63 hits 1
BQT_v5_pages.txt leaf 73 pdf 74 printed~ 69 hits 2
BQT_v5_pages.txt leaf 92 pdf 93 printed~ 88 hits 1
BQT_v5_pages.txt leaf 110 pdf 111 printed~ 106 hits 1
BQT_v5_pages.txt leaf 126 pdf 127 printed~ 122 hits 1
BQT_v5_pages.txt leaf 129 pdf 130 printed~ 125 hits 1
BQT_v5_pages.txt leaf 140 pdf 141 printed~ 136 hits 1
BQT_v5_pages.txt leaf 141 pdf 142 printed~ 137 hits 1
BQT_v5_pages.txt leaf 146 pdf 147 printed~ 142 hits 1
BQT_v5_pages.txt leaf 158 pdf 159 printed~ 154 hits 1
BQT_v5_pages.txt leaf 178 pdf 179 printed~ 174 hits 1
BQT_v5_pages.txt leaf 185 pdf 186 printed~ 181 hits 8
BQT_v5_pages.txt leaf 186 pdf 187 printed~ 182 hits 3
BQT_v5_pages.txt leaf 195 pdf 196 printed~ 191 hits 1
BQT_v5_pages.txt leaf 223 pdf 224 printed~ 219 hits 1
BQT_v5_pages.txt leaf 237 pdf 238 printed~ 233 hits 1
BQT_v5_pages.txt leaf 255 pdf 256 printed~ 251 hits 1
BQT_v5_pages.txt leaf 257 pdf 258 printed~ 253 hits 1
BQT_v5_pages.txt leaf 265 pdf 266 printed~ 261 hits 1
BQT_v5_pages.txt leaf 272 pdf 273 printed~ 268 hits 1
BQT_v5_pages.txt leaf 274 pdf 275 printed~ 270 hits 1
BQT_v5_pages.txt leaf 281 pdf 282 printed~ 277 hits 1
```


## [2026-09-07T20:20:39.839Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ns=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=s.split('\\f')\nfor i in (420,421):\n    print('='*25,'LEAF',i)\n    print(leaves[i])\nEOF"
}
```


### [2026-09-07T20:20:41.284Z] TOOL RESULT

```
========================= LEAF 420
[pdf page 421]
سیر : یوزها
کاق , غله برافغان را گویته:وآن‌آلتن باشد که کنند ؛ و بسکون ثالی هم بنظرآمده است .
بان غله را بیاد دهند تا آزکاء جدا! شود - و نیز هیر ۱ - بروزن فقیر » بمعنی هس
طبْغی :باشد پپن که ازنی بافند و بدان غله پاکك | است که یخ باشد .
بیان دهم.
در های هوز با شین قطه‌ دار مشتمل بربیست و يك لت وکنایت
هش - بلتم اول و سکوق ثافیءپمعنی کیته‌اند که در برابر حیات وژند کی‌انی* . ‎٩‏
‏رفتن باشد که قیض آمدن است ۴ - و بممتی هشپلگ ۷ - بنم اول و بای فارسی
کل و لای :غمآمده است ۴ - وطم اول مخفف | بروزن بلبلك , صدائی‌است که کبونزبازان بوقت
هوش ات "که از کی و ذهن و عقل و شمور | کبوتر پرانیدن با دوسرانگشت دست ازدهان(۷)
و جان و روح باشد ۴ - و فوت واموت رانیز | ببرون‌کنند #۰
() خم۱: - از دهان .
۹ هس (وم.) :
امروز از خجالت دوشیته بنده را جالی است پر ژآتش » طبعی است پرهمیر.
سنائی غزلوی « فرهنگه نظام * .
۴ - جهانگیری این بیت سید عزالدین را شاهد آورده : ۱
کر بر تهمتن هشی بمصاف ار برکرکدن کشی بلاح ...
اکر شبط « هشی» سحیح باشد از حصدر « هشیدن » باشد . موولف فرهنگه نظام کوید: «کوپا...
بشی ( با باه ) هخفف: بشوی است که تصحیف خوانی شده .> ۴ -ظ. مصحف « لش »
« فرهنکه نظام.> رك : لش . ۴ -رك : هوش :
مود من دین‌را از هیبت توهش لبود گر میان تو و او بادیه باشد هشتاد. >
« فرخی سیستانی . دیوان ص ۶۷ .

8 - ر4 : هوش . ‎٩‏ - نیز « هش > جنم اولکلمه‌است که خربندکان خر را
بدان ایستَلدن و توقف فرمایند. - نیز < هس * هیس . از اسوات بمعنی ساکت. باشی:! خاموشی!
قی::کردی 10/818 » انگلیسی 315]13] ( خاموش » ساکت باش ) » عربی حس ( پم اول )* ژابا
متشه ۷ - اسم صوت , قی : شهل » شپلیدن » شهلت » شپیل .

2 هشت - بفتح اول . اوستا 25118 (هشت). پهلوی 138511 ( 28101 ). هندی ا-2ان
0 » ارمنی *۱1 ۰ افقانی 812 ۰ استی *851 ۰ وخی 80210 :8831 ۰ شفنی ۰۷8581
سریکلی ۷۵۳۸ , سنگلجی21] , منجی88128 , یفنوی 278 . ۸ «هشت > در پارسی جداید
از «هفت > کرفته شده. « اسشق ۶۱۰۹۵ ۰ کرمی 16801 , 128101 , زازا 136584 » دوجیکی
1 زاب ی 4۶۵ ,کیلکی 1128101 ؛ عدد میان هفت ونه » پنج بملاو سه -

۵ هشتاد - بفتح اول ؛ آوستا -281012111 (هشتاد) . پپلوی 82810121 ( 880121 )»
افدانی 8118 « اسشق ۰ ۱۰۹۹ *. کردی 8۴9011 ( هشتاد ) » 5216 - 169801206 ( هناد
ساله ) , 16ف , 8۵9۳18 , 3298160 ؛ زازا 56۵158121 ؛ دوجیکی 696۳46 « ژاباس
0 عدد برابن هشت بار ده » پاجاه پبلاوه سي » هباج باضانةٌ ده ‎ .‏ از برهان قاظع ۲۵ )

========================= LEAF 421
[pdf page 422]
کتتتاا ‏ اا ‏ عکک
هشت. باغ » کنایه از هفت بهفت هشت مرعی ؟ - بسمنی هشت موی
است . بود که کنایه از هشت بهشت باشد .
هشت بستان « بسنی هفت. باغ‌است هشت متظر - بسنی‌هشت مرعی‌باشد
که کنایه از هشت بهشت باشد .۸8 که هعت بهشت‌است - وهشت‌فاك را نیز کویند
هشت دهان .با دال ابجد وهای | که فلك‌البروج وفلك زحل و فلك مشتری‌وفلك:
هوز بروزن سخت کمان ‏ نام کیاهی است‌اوبسنی | مرخ و افلك آفتاب و افلك زهره و فلك عطارد
عود هندیراگویند ۱ ؛ و بعضی‌دیگن گل‌خیریر! | و فلك فقس باشد -
که خبازی باشد. نفرس را نافع است.# هشتن ۴ « بکر اول و سکون تالی
هشت گنج « مبارت از کنوز فمابة وفتح فوقالی ونون سٌاکن » بمعنی کداشتن وفرو
خرو پرویز است که کنج عروی وکنج بادآورد گذاشتن ورها کردن - وآویشتن باشد .
جوم نج افراتاپ وگنج سوخته هشت ومشت - بن اول و میم اين.
و کنج‌خضرا| وکنج شادآوردو کنج بارباشد » وهر
بك در جای خود آمده است . لفت از اتباع است پیمنی جنکه کردن با مشت.
.۰ هر ماویٌ ۴ شکنایه ازخفت هشت ولگد وسیلی وامثال‌آن (۱) 6 .
است . ۱ هشتو یش ۱ - بغتح ارل. و سکون

۱« هشت دهان . اسم قارسی‌نوعی از عودهندی است. جهت فقرس‌نافم.» «محیط اعظم».
هت دهان معرب ازفارسی > 4781089 0018 « دزی ج ۲ ی ۰۳۷۵۸

۴ - موی » با الف مقصوره عربی است بمعنی منزل » مسکن » جایگاه .

؟ - هرعی, با الف مقصوره عربی است بمعنی چراگاه. ‏ ۴ * هلیدن («م.) * هدیدن
(«.م.) » ريشةٌ اوستابی -18۳2 ۰ 167626811 ( گذاشتن » رها کردن » ول کردن ) » پهلوی
0 ,. قی 1۵ط1(5)ظ ( نراعه ) ؛ پازد ۸1488ط , 5۸110420 , 361640 , ریعه
هندی باستان -[587 , 51[401 ؛ بلوچی ۰1188 1188 ۰ 118810 (گذاشتن, رها کردن,پذبرفتن»
اجازه دادن ) رك : اسشق ۱*۹۷ ؛ ريشهٌ این کلمه در بهلوی اشکابی 3672 است و بحدس استاد
هنینگه «شف کلهرزان » ( 801-672۵8 6 «0‌هط5 ) که بقول حمزء اسفهانی - درشرح
قسیدة سينيةٌ ابونوای - شبی که کشیدان عزب‌هاری کردآبند ‏ لفة بمعنی (شب کلهشتن) است.
رك : مرغوی . یکی از فارسیات ابولوای . مجلةٌ داشکدء ادبیات تهران ٩:۳س۷۳‏ ؛ +کلپایگانی
0 (گذاشتن ) « فاسمی >. دراراك (سلطانآباد) 8898180 (گذاشتن ) , هط - 06
( بگذار ) و [قظ ( بگذار) « مکی‌دژاد کردی ع 0 ( رها کردن » ول کردن ۰
گذاشتن ) .۰ قی :کردی هلان ؛ داهشتین « ژابا س ۹-440 8 -بر4 : بهار عجم .

‎٩‏ - اوستایی ۷8815101815211 نام و عنوان فضل‌پنجم« کانها *ست که روز پنجم خمهٌ
مسترقه ( پنجهٌ دزدیده » بهیزك » پنجه ۰ پاچ‌وه ) را بدان نام خواندند . ر4 : پورداود . خرده
آوستا س ۲۱۱ . ورك : وهشت .

‏۵ هشنده - بفتح اول و چهارم » از : هشت ۳ ده هرد هیده ؛ عدد میان هقدم
ولوزده . رك : هیجده ,

‏0 هشتصد - بننح اول و چهارم » از؛ هفت ۳+ صد ( ۳ ند) ! عد برابر هقت‌پار صده
پاصد پملاوة سیصد .
```


## [2026-09-07T20:21:02.094Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON خیش ctx ===\"; sed -n '58605,58630p' MON_part1.txt\necho \"=== MON اختاپوس variants ===\"; grep -n \"ختاپوس\\|اختابوس\\|octopode\\|اکتاپوس\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-07T20:21:02.173Z] TOOL RESULT

```
=== MON خیش ctx ===
ضیسانیدل: 2:7020-.*(- خسساندن - 
عوسا تن | ( یم | زک اند 
خواهد خسانند» سخسان؛ خساننده» 
خیسانیده) تر کردن» مرطوب ساختن. 
جیسیدل: 5-1417 (مصل.) مرطوت 
شدن» تر شدن. حل کردن. سرشتن (مانند 
معجون). خمیر کردن. 
خیش: 8« (- خیج - هیش] () (کشا) 
آلتی آهنین که آن را به گردن گاو بندند و 
بدان زمین را شخم زنند؛ گٌاو آهن. (کشا.) 
شخم (زدن). (کشاء) جفت (زمین بنه. 
ضیش: 8 [- کیش - معر. خیش ] (.) 
بارچه‌ای خشن از کتان. برده‌ای از بارچه 
مذکور که آن را در اطاق می آویختند و 
برای خنکی آن را نمنا ک می‌کر دند. جامة 
پنبه ا کنده. 
خیشخانه: (0-)308-. (امر.) خانه‌ای که از 
نی و علف و خار و خس يا با پرده؟ خیش 
سازند و بر این ان باشند تا هه او, داخل ۳ 
هوای 
گرم از کتان سازند و درون آن برک بید 
8 بر اطراف وی اب باشند. 
خیشوم: : (-110()06۷۰ 2۷۵ [ع ۰] (.) ینی. س 
بسنی. اندرون بینی. نیت شامة از رام او 
دا کرو من امک کر زا ج. خیاشیم. 
خیط؛: : (۵۷۱۵6۷ [ع. ۰] (.) ر شته» سلکك؛ ج. 
=== MON اختاپوس variants ===
```


## [2026-09-07T20:21:03.796Z] TOOL CALL #29: Bash

```json
{
 "command": "pdftoppm -f 372 -l 372 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg372 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T20:21:05.588Z] TOOL RESULT

```
total 33496
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 16:21 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81599 Sep  7 14:37 350-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99691 Sep  7 14:40 351-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115624 Sep  7 14:43 355-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85914 Sep  7 14:35 358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19549 Sep  7 14:35 358-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74812 Sep  7 14:35 358-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95065 Sep  7 15:49 361-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65864 Sep  7 15:52 362-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77269 Sep  7 15:46 364-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   160756 Sep  7 15:55 365-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87585 Sep  7 15:50 366-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1583 Sep  7 16:16 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299343 Sep  7 15:34 bqt2173_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79304 Sep  7 15:38 bqt2195_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59998 Sep  7 15:38 bqt2210_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70860 Sep  7 15:48 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    34373 Sep  7 15:52 e0_p363.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37506 Sep  7 15:51 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37506 Sep  7 15:52 e2_p363.json
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30152 Sep  7 15:34 ffd77_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 15:34 ffd77.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67410 Sep  7 14:53 mk353.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87481 Sep  7 14:40 mk354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    38634 Sep  7 14:34 mk358.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53090 Sep  7 15:49 mk361.py
-rw-rw-r-- 1 sfmqrb sfmqrb    86861 Sep  7 15:51 mk362.py
-rw-rw-r-- 1 sfmqrb sfmqrb    33821 Sep  7 15:52 mk363a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36857 Sep  7 15:52 mk363b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62290 Sep  7 15:49 mk366.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54370 Sep  7 15:45 mk368.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86505 Sep  7 14:27 p358_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4789 Sep  7 15:38 p361_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4152 Sep  7 15:38 p362_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3458 Sep  7 15:35 p362_germ1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2606 Sep  7 15:35 p362_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135659 Sep  7 15:34 p363_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   223838 Sep  7 15:34 p363_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   118891 Sep  7 15:45 p365_row8.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13022 Sep  7 15:42 p366_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb     5736 Sep  7 14:43 patch354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59757 Sep  7 14:29 pg349.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82867 Sep  7 15:38 pg359.png
-rw-rw-r-- 1 sfmqrb sfmqrb    45536 Sep  7 15:36 pg360.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57895 Sep  7 15:38 pg361.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111691 Sep  7 15:34 pg362hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66511 Sep  7 15:33 pg363.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49805 Sep  7 15:37 pg364.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94462 Sep  7 15:45 pg365.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59224 Sep  7 15:34 pg367.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49419 Sep  7 15:35 pg368.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53926 Sep  7 16:17 pg371.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59170 Sep  7 16:21 pg372.png
-rw-rw-r-- 1 sfmqrb sfmqrb    47783 Sep  7 16:19 pg375.png
-rw-rw-r-- 1 sfmqrb sfmqrb       40 Sep  7 16:16 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0022.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0158.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4676 Sep  7 14:29 sns_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   135853 Sep  7 14:30 sns_n157.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129673 Sep  7 14:30 sns_n159.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   113320 Sep  7 14:30 sns_n21.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb   116699 Sep  7 14:30 t1.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T20:21:15.434Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg372.png"
}
```


### [2026-09-07T20:21:15.770Z] TOOL RESULT

```

```


## [2026-09-07T20:21:15.765Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:21:31.538Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 372 -l 372 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg372hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg372hi.png'); print(im.size)\nw,h=im.size\n# quote line approx y 690/2200 of page -> crop\nim.crop((int(w*0.40),int(h*0.295),int(w*0.79),int(h*0.325))).save('p372_quote.png')\nim.crop((int(w*0.40),int(h*0.258),int(w*0.79),int(h*0.300))).save('p372_pers.png')\n\"; ls -la p372_quote.png p372_pers.png"
}
```


### [2026-09-07T20:21:35.744Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 3884 Sep  7 16:21 p372_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb 4259 Sep  7 16:21 p372_quote.png
```


## [2026-09-07T20:21:38.537Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p372_quote.png"
}
```


### [2026-09-07T20:21:38.551Z] TOOL RESULT

```

```


## [2026-09-07T20:21:42.005Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg372hi.png'); w,h=im.size\nim.crop((int(w*0.40),int(h*0.320),int(w*0.79),int(h*0.348))).save('p372_q2.png')\n\""
}
```


### [2026-09-07T20:21:43.848Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:21:46.082Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p372_q2.png"
}
```


### [2026-09-07T20:21:46.125Z] TOOL RESULT

```

```


## [2026-09-07T20:21:51.084Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg372hi.png'); w,h=im.size\nim.crop((int(w*0.60),int(h*0.335),int(w*0.79),int(h*0.352))).resize((1600,int(1600*(h*0.017)/(w*0.19)))).save('p372_q3.png')\n\""
}
```


### [2026-09-07T20:22:29.021Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:22:31.145Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p372_q3.png"
}
```


### [2026-09-07T20:22:31.181Z] TOOL RESULT

```

```


## [2026-09-07T20:22:35.965Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg372hi.png'); w,h=im.size\nc=im.crop((int(w*0.415),int(h*0.334),int(w*0.60),int(h*0.353)))\nc=c.resize((c.width*2,c.height*2))\nc.save('p372_q4.png')\n\""
}
```


### [2026-09-07T20:22:37.927Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:22:40.240Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p372_q4.png"
}
```


### [2026-09-07T20:22:40.257Z] TOOL RESULT

```

```


## [2026-09-07T20:22:53.861Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T20:22:53.869Z] TOOL RESULT

```


```


## [2026-09-07T20:22:57.657Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%DB%8C%D8%B4",
 "prompt": "Give the Persian entry for خیش: etymology (Middle Persian, Avestan, Proto-Iranian forms), meanings (plough?), and any cognates cited. Also any note on خویش."
}
```


## [2026-09-07T20:22:59.974Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/o%E1%B8%B1t%E1%B9%93w",
 "prompt": "Give the reconstructed PIE word for 'eight': the headword, meaning, and descendants (Indo-Iranian, Greek, Latin, Germanic), plus any note on the reconstruction and references (Pokorny page)."
}
```


### [2026-09-07T20:23:03.509Z] TOOL RESULT

```
# Persian Entry: خیش (xēš / xiš)

## Etymology
The word derives from **Middle Persian** ēš ("plough"), specifically from Manichaean Middle Persian hēš. The entry notes "[script needed]" for the original forms, indicating historical script representation gaps.

## Meaning
**خیش** functions as a noun meaning "plough" or "ploughshare"—the cutting blade of a plough.

## Descendants
The word passed into **Arabic** as خَيْش (ḵayš), representing linguistic transmission across related languages.

## Pronunciation Variants
The term shows dialectal pronunciation differences across Persian-speaking regions:
- Classical: /ˈxeːʃ/
- Iranian Persian: [xiːʃ]
- Dari and Tajik variants also documented

## Notable Absence
The entry contains **no mention of خویش** (khvīsh, meaning "family" or "relative"). Despite potential etymological interest, no connection between these terms is established in this Wiktionary source.
```


### [2026-09-07T20:23:05.735Z] TOOL RESULT

```
# Proto-Indo-European Word for "Eight"

**Reconstructed Word:** *oḱtṓw

**Meaning:** Eight (cardinal numeral)

## Key Descendants

- **Indo-Iranian:** *Haštā́ (Sanskrit aṣṭá/aṣṭáu)
- **Greek:** *oktṓ
- **Latin:** *oktō
- **Germanic:** *ahtōu

## Reconstruction Notes

Scholars debate the exact form. Some suggest *h₃eḱteh₃ or *h₃eḱtoh₁ with initial laryngeal, noting that "the other numerals from three to ten showcases the e-grade." However, Armenian evidence suggests the initial element may have been *Hoḱ- or *Hḱ- rather than *h₃e-.

The term possibly derives from "(H)oḱto-" meaning "four fingers," with the dual form *oḱtṓw representing "two sets of four."

**Pokorny Reference:** Page 775 in *Indogermanisches etymologisches Wörterbuch*
```


## [2026-09-07T20:23:12.985Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%AE%D8%AA%D8%A7%D9%BE%D9%88%D8%B3",
 "prompt": "Persian entry اختاپوس: etymology (from which language, French? Greek?), meaning, and any notes."
}
```


## [2026-09-07T20:23:14.103Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%D8%B4%D8%AA",
 "prompt": "Persian entry هشت: etymology (Middle Persian, Old Persian/Avestan, Proto-Iranian, PIE forms), meaning, and derived terms like هشتاد and هجده/هیجده."
}
```


### [2026-09-07T20:23:18.871Z] TOOL RESULT

```
# Persian Word: اختاپوس (Uxtāpūs)

**Etymology:** The word derives from Ancient Greek *ὀκτώπους* (oktṓpous), which combines the Greek terms for "eight" and "foot."

**Meaning:** This Persian noun refers to an octopus—a marine mollusk belonging to the family Octopodidae. However, it's noted as the less common term; the more prevalent synonym in Persian is *هشت‌پا* (hašt-pâ), which literally translates to "eight-footed."

**Linguistic Note:** The etymology tree shows the word's path through Proto-Indo-European and Proto-Hellenic before arriving in Persian, demonstrating how this creature's name traveled through multiple language families over millennia.
```


### [2026-09-07T20:23:20.726Z] TOOL RESULT

```
# Summary of هشت (Hašt)

This Wiktionary entry documents the Persian word **هشت** (hašt), meaning "eight."

## Key Information

**Meaning & Usage:** The term functions as a numeral across multiple Iranian languages including Gilaki, Mazanderani, and Persian. In Persian, it serves as the cardinal number for 8, with the ordinal form being هشتم (haštom).

**Etymology:** The word traces back through multiple language stages. It derives from "Middle Persian 𐭧𐭱𐭲 (hašt)" and ultimately originates from Proto-Indo-European *oḱtṓw. The entry notes cognates across Indo-Iranian languages, including Northern Kurdish *heşt* and Sanskrit अष्ट (aṣṭa).

**Pronunciation:** Varies by dialect—Classical Persian uses /ˈhaʃt/, while Iranian formal Persian uses [hǽʃt̪ʰ]. The entry provides detailed IPA transcriptions for Dari, Tajik, and other variants.

**Linguistic Classification:** The page categorizes it as a Persian cardinal number and numeral, with extensive etymological documentation showing its Proto-Indo-European heritage.
```


## [2026-09-07T20:23:30.515Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%AE%D8%AA%D8%A7%D9%BE%D9%88%D8%B3/",
 "prompt": "Show the dictionary entries for اختاپوس, especially the فرهنگ معین (Mo'in) section with any origin tag like [فر.] (French) or [فر. octopode]. Quote it."
}
```


## [2026-09-07T20:23:31.732Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/octopus",
 "prompt": "Give the etymology of octopus, and any related entries mentioned (octopode, octo-, October, octave, octagon): Greek oktopous, Latin octo, PIE root."
}
```


### [2026-09-07T20:23:35.235Z] TOOL RESULT

```
# Dictionary Entry for اختاپوس

## Farhangi Mo'in (فرهنگ معین)

The Mo'in dictionary entry is concise:

> "(اُ) (اِ.) هشت پا."

This translates as: "(stressed) (informal) eight feet/legs."

The entry does not include an origin tag (such as French [فر.] or other language markers). It simply provides the Persian term "هشت پا" (eight-legged creature) as the definition, with notation for pronunciation stress and register.
```


### [2026-09-07T20:23:37.394Z] TOOL RESULT

```
# Etymology of Octopus

**Origin:** The word "octopus" comes from a Latinized form of Greek *oktōpous*, literally meaning "eight-foot," combining *oktō* "eight" and *pous* "foot."

**Etymology Chain:**
- Greek: *oktōpous* (eight-foot)
- Latin: Latinized scientific form
- PIE root: *\*ped-* meaning "foot"

**Related Entries Mentioned:**

The page references several connected terms:

- **Octo-**: Prefix from Greek *oktō* (eight)
- **October**: Contains the octo- prefix (originally the eighth month)
- **Octopod** (1826): "Eight-footed or eight-armed animal," from the same Greek root
- **\*ped-**: The Proto-Indo-European root underlying all foot-related words

**Plural Forms:** The entry notes three acceptable plurals: *octopuses* (English), *octopi* (Latin-influenced, from 1817), and *octopodes* (classically correct Greek plural).

The page does not discuss "octave" or "octagon," so those etymologies are not covered in the source material provided.
```


## [2026-09-07T20:23:47.651Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins okto ===\"; grep -n -i \"okto\" AHD_watkins1985.txt | head -20\necho \"=== IEC okto ===\"; grep -n \"okto\" IEC.txt | head -20\necho \"=== WLD Bd1 p.172 => leaf 181 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==181 {print}' incoming/WLD/WLD_Bd1_pages.txt | head -60"
}
```


### [2026-09-07T20:23:48.986Z] TOOL RESULT

```
=== AHD watkins okto ===
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
1954:ocTo- oktd(u) OcroBER okt6(u) ocToDEcIMO dekm, okto(u) OCTOGENARIAN dekm, okt0(u) OCTONARY okt6(u) octopus oktd(u), ped-1 OCTROI aug-! OCTUPLE pel-3 OCULAR oOkW- OCULIST okw- OCULOMETER okW- OCULOMOTOR okw- ODD us-
1967:OINTMENT ongW- OKTOBERFEST dhés- OLD al-3
=== IEC okto ===
7544:kokstis, os, ios “hard, old, withereď’. Cf. (variant) Koktos, kăkstios Skt. kastah ‘harmful’; Arm. košt, Let ((1; ‘hard, coarse’, via *kokitis by induction): Gaul. cotto-; Cor. coth, Br. koz, compar. kosoch, adj. Cold Ambig. cf. Koktos); Du. (ambig.) hecht (/solid, firm’, but cf. VW: EWNT: becht prob. fr. Gmc. *hafti-); OCS ko&tí "lean, slim?
9025:Koktos (KoKtos) “hard, old, stiff, firm’. Cf. kokstis (with velar initial) WP I, 333 & 358 Skt. Saktáh ‘strong, able’; Av. saxto ‘firm’; Per. saxt “hard, vehement, strong? beside sift “hard, stiff; Arm. cf. sastik (w. assimilated consonants: “hard, severe"); Gaul. cotto- (in a place-name); Br. koz, Cor. coth old: Du. becht “solid, firm”
11812:nóg- — noktiór (noktor)
12096:oKtou (okto, oKdo, oKdou, oKdmi) “eight. Cf. eK- (oK-) and duou (?). WP I, 173 Skt. astaü, astá (perh. 2 tetrads'. MacDonell); Av. asta; Per. hast (infl. of haft geven: Oss. ast; Tokh. A okát, B okt; Arm. ut, i-st.; Gk. októ; Lat. octó; Alb. tetë (aphetic w. added -të); Olr. ocht; Br. eiz; W wyth; Cor. eth; OHG ahtowi, pl.; MHG ehtewe, pl. beside aht, eht; Go. ahtau; OE eahta; ON átta; cf. vari- ants in OCS osmí (and com. Sl.); Li. aštuoni CG Lat. octoni ‘eight each"); Latv. astoni, id.
13328:poKos, us (poKmos, poktos) ‘fleece, wool, hair; (combed, kempt)'. WP II, 16, Cf. peko Per. pa$m *^wool'; Oss. fásm, id. beside fasín, v. ‘comb’; Arm. asr, gs. & ab. s. asu ‘fleece’; Gk. pókos, m. id., cf. pó-gon, -gonos ('kempt chin”, hence ‘beard’, or fr. aphetic *(a)po-8on- 2); OHG fahs, sn. ‘hair; MHG vahs, sm. & sn. id.; OE feax, n. ‘hair of the head’; ON fax, n. ‘mane’; Du. cf. vacht, f. ‘fleece’; Li. cf. pá$ymas, m. ‘combing, carding’; pašaŭ, -ýti, v. ‘comb, card’
=== WLD Bd1 p.172 => leaf 181 ===
                                                -                            i                                                )     :




172                                                            <3ku-s        — oktu(u)

27,    1 7   4f . ,
                         dessen Yerkniipfung der bait. Worte mit                                         ar. klid-   n.   „H6hle,
Offnung         1
                    ,   A;/(«- „Quelle,         Brunnen“ unter idg. *o<jho- qho- nicht vorzuziehen  :




ist    (s. u.       qhena x - „graben“).
      Ygl.      Curtius                PL 38Stf., Johansson BB. 18, 25;
                             463; bes. J. Schmidt
BrugmannI 2 613f.. II 2 1, 132, 173, 309, II 2 2, 202.       Verkehrt will                                    —
Lewy KZ. 40, 422 oq'i- „sehen‘ mit s-ecfi- „sehen, sagen“ und u-eq'i- „enog“
                                                                i




unter Annahme verschiedener Praeformanten vermitteln. Es ist ja gar
nicht ausgemaclit,                       daB die verbalen Anwendungen                                   in   unserer Sippe    das
altere seien.


oku-s         „schnell‘\
      Ai. (leu- ,,schnell“,                  Komp. (inyirn. Sup. unstha-, av. Cisu- „schnell“, Komp.
ttst/Ct,     Sup. asiZta-.               gr.       lat. d dor ,.schneller“, Sup.
                                               Jjttvs.         tbyJcov.            mxtaxos,
ocissimus (Positiv fehlt), acymr.          ncymr. diog, corn, dioc, bret. di-ec
                                                                         cli-ciuc ,

„trage“, eigentlich „unschnelb‘ (Curtius Gdz. 5 131, Osthoff IP. 6, 2f. m. Lit.).
    Eine Ablautform *aku „schnell“ steht nicht fest. Lat. acupedias „schnell-
fii6ig“ ist   auch als tfbersetzung von gr. divnovg verstandlich: lat. accipiter
 „Habicht, Falke” Ur jedenfalls durch volksetymologische Anlehnung an
 accipere) kann zwar den Begriff „schnellfliegend“ voraussetzen (vgl. drs.vg.
 (hy.vjuTt'jg, dry.vnxtoog, eXupQoxarog nET£i]vd>v als Beiworter des Habichts

 bei Homer; Solmsen Enters. 149), erweist aber auch dann nicht ein *ahi-
 pctrts als Gdf., da auch ein *ocu-petns fvgl. aufier tby.v-TreTijg, wxvjt xegog
 auch ai. Cigu-patvan- „schnellfliegend“) iiber „ociipeter nach accipere zu cu-
 cipitcr werden konnte (Thurneysen aaO. erwagt „spitzfluglig“ als Gdbed.
 dann aus *ilrri-petri-s durch Dissimilation zu *acipiter und durch Konso-
 nantenseharfung unter EinfluS von accipere zu accipiter). Auch ob got.
 ninths .,Taube“ (ahd. lheinfr. dk-falla „Taubenschlag“ [nach Feist Got. \Yb. 2
 442 zweifelhafte Glosse]) von einem solchen *aku- abgeleitet sei (Solmsen
 Unters. 149                A 1), ist hochst zweifelhaft (s. Feist Got. Wb. 2 12).
       Eine Ablautform                       *ckn-         mit           Praef. ga-         vermutet Erdmann (Zitat bei
 Noreen                 Ltl. 44)        in   ahd. gain                  „rasch,       hastig,   plotzlich“,    mhd. ijcehe, nhd.
 jdh         bair.             gehda „Ungestum“ ist recte gehdu „Sorge“
                          gdcli).       aber        ags.
 (Zweifel hinsichtlich der Bed. und Lautform des ags. Wortes bei Zupitza
 GG. 190 a 1     Doch konnte gal) auf grm. *yan/i- beruhen und neben
                            .
```


## [2026-09-07T20:24:00.350Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"okt[oó0][^]]\\{0,900\\}\" AHD_watkins1985.txt | grep -i \"eight\" | head -5\necho \"---- try direct\"\ngrep -n \"oktd(u)\\|okt6(u)\\|oktō(u)\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-07T20:24:01.659Z] TOOL RESULT

```
---- try direct
127:complete agreement on the numerals from two to ten: dwo- (*duw6), trei- (*treyes), kvetwer- (*k”etwores), penk”e, s(w)eks, septm, oktd(u), newn, dekm. For the nu- meral “one” the dialects vary. We have a root sem-' in some derivatives, while the western Indo-European languages Germanic, Celtic, and Latin share the form oi-no-. The word for “hundred,” formed from dekm, “ten,” was *(d)kmtom. No common form for “thousand” or any other higher number can be reconstructed for the protolanguage.
362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
795:od-'. To smell. 1. Suffixed form *od-os- in Latin odor, smell: opor. 2. Suffixed form *od-é- in Latin olére, to smell (with J for d representing a Sabine borrowing): OLFACTORY, REDOLENT. 3. Suffixed form *od-yo- in Greek ozein, to smell: OZONE. 4. Suffixed form *od-md- in Greek osmé, smell: OSMATIC, OSMIUM; ANOSMIA. [Pok. 1. od- 72.] od-2. To hate. Latin édi, I hate, and odium, hatred: ANNOY, ENNUI, (NOISOME), ODIUM. [Pok. 2. od- 773.] 6g-. Fruit, berry. 1. Zero-grade form *ag- in Germanic *ak-ran- in Old English zcern, acorn: ACORN. 2. Latin iva (preform uncertain), grape: UVEA, UVULA; PYRUVIC ACID. [Pok. 6g- 773.] oid-. To swell. 1. Possibly Old English date, oat: oat. 2. Greek oidein, to swell: EDEMA. [Pok. oid- 774.] oi-no-. One, unique. I. Basic form *oi-no-. 1. Germanic *ainaz in: a. Old English dn, one: A1, AN!, ONCE, ONE; (ALONE), ANON, (ATONE), (LONE), (LONELY), NONE; b. compound *ain-lif-, “one left (beyond ten),” eleven (*lif-, left over; see leikw-), in Old English endleofan, eleven: ELEVEN; Cc. Old High German ein, one, in Ger- man vereinen, to unite: EINKORN, TURNVEREIN. 2. Latin anus, one: INCH}, OUNCE!, UNCIAL, UNI-, UNION, UNITE, UNITY; COADUNATE, QUINCUNX, TRIUNE, UNANIMOUS, UNICORN, UNIVERSE. 3. Latin ndn, not (< *ne-oinom, “not one thing”; ne, not; see ne). II. Suffixed form *oino-ko- in: a. Germanic *ainigaz in Old English &nig, one, anyone: ANY; b. Latin dnicus, sole, single: UNIQUE. III. Suffixed form *oino-lo- in Latin dllus, any (see ne). [In Pok. e- 281.] oito-. An oath. Probably derived from ei-1. Germanic *aithaz in: a. Old English dth, oath: OATH; b. Old High German eid, oath, in German Eidgenosse, confederate: Hucuenor. [In Pok. 1. ei- 293.] okt6(u). Eight. 1. Germanic *ahté in: a. Old English eahta, eight: EIGHT; b. Old Norse ditjan (tjan, ten; see dekm), eighteen: ATTO-. 2. Latin octé, eight: OcTANS, OCTANT, OCTAVE, OCTAVO, OCTET, OCTO-, OCTOBER, OCTONARY; OCTODECIMO, OCTOGENARIAN. 3. Greek okt6, eight: OcTAD; ocTopus. [Pok. okt6 775.]
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1444:EGOIST eg EGOTISM EGREGIOUS ger-! EGRESS ghredh- EIDER &ti- EIDERDOWN dheu-! EIDETIC weid- EIDOLON weid- EIGHT oktd(u) EINKORN gre-no-, oi-no- EISTEDDFOD bheue-, sed-' EITHER kWo- EJACULATE yé- EJECT yé-
```


## [2026-09-07T20:24:11.737Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD hast / hes ===\"; grep -n \"^hašt\\|hašt \\|hašt,\\|^hēš\\|hēš\\|xēš\" PHD.txt | head -20\necho \"=== PHD_mackenzie ===\"; grep -n \"hašt\\|hēš\\|xwēš\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-07T20:24:11.807Z] TOOL RESULT

```
=== PHD hast / hes ===
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
186:~ih: heresy. āhēg Phwk' | M >ле, N ahd] fault, blemish. ahógénidan, áhógén- ["nokyn-ytn!] defile. a-homānāģ [’hwm’r’k'] unlike. ahēš [nof] deathless, immortal.
187:ahēših 7 amāwand
398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
1705:dry up hēšīdan.
1721:ear gēš; ~ of corn hēšag.
2383:immortal ahēš, amarg, anēš(ag).
2384:immortality ahēšīh, amargih, anēša- gih.
4315:window rózan, roz(b)anag. wine badag, may. wine-press karxēš.
4327:wither hēšīdan ; cause to ~ hūšēnīdan.
4364:wrath xēšm.
4806:haštād* sagēn nawad* sēn
=== PHD_mackenzie ===
```


## [2026-09-07T20:24:13.027Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB hast ===\"; grep -n \"hašt\\|hēš\" NYB_vol2_glossary.txt | head -20\necho \"=== HUB xes ===\"; grep -n \"xes\\|Pflug\\|/^es\" HUB.txt | head -20\necho \"=== SKT October/octave/octagon ===\"; grep -n \"^October\\|^octave\\|^octagon\\|^eight\" SKT.txt | head -10"
}
```


### [2026-09-07T20:24:13.121Z] TOOL RESULT

```
=== NYB hast ===
1069:who knew 121°; būt i ka nē būt ... u bavet ka ne bavet ches was a time when he did not exist, and there will be a time when he will not exist 642-3; ö(h) ~, v. ē(h); cf bavisn. — 2. as copula, with a noun, a pron. or a prep. + subst. as its complement, passim: hàn but Vahuman 56%; martom ... hamäk ahēš ... bavēnd willbe immortal 1049-19; kanicak pat giyäk bütàn (YHWWN-t*n'] pl. cas. obl. of the pret. büt used as a subst. ‘he who has been’ 5518, ~. V. bavétün.
1955:hašt [hšt'; figures] eight.
1956:hašt-dahom [hštdhwm] eighteenth. haštom [hštwm; 8-wm] eighth.
1979:hēšm
1987:hēšm [hyšm, hšm] wrath, anger: Artax- šer ~ grift A. was seized by anger 37; ~ kartan to become angry 154. 6815; ke ~ 6 tan nē hilét who leaves no room for anger 8414; ~ vas quick to anger 10?!; ~ rād dāšt persisted in his anger 101°; tāi bē nišastan à ~ until the anger sub- sides 6817-18; the work of Ahriman is ~ u kén u anästeh 7822; ~ u ken räd 14%; - personified as a demon, one of the chief evil powers: ~ dev 6123: equal to Ahri- man 68%; in company with Az 103°;
2023:hoá [hwš] death 997. — Av. (43sg.) aošah-; Paz. hēš, cf ahoš and anēšak.
2026:hēšītan to dry, to wither (intr.): pres. 3d p. sg. hēšēt [hwšyt'] 9612-13, 9811, hošet [hwšty] 128%. — Av. (1738) hao$-; MPrth pres. hwš-, xwš- (MHC); Bal husay; NP xoSidan. V. also husk.
2287:kön [kyn'] revenge, vengeance: ~ z for 9: pat hin i hunuškān ~ in order to avenge her progeny 501; wi... x“dstan to take vengeance for 14? (pat upon). 2712. 283; ~ a"üstan hac for 25*7—26!; ~ töxtan to take vengeance 45??; — hēšm u ~ 1443
4946:ačšma-: hēšm
6229:xyšm: hēšm
6258:Baluchi gécay: !véxtan gejak: *vēxtan gēžag: ?vextan (N Bal.) hčšay: hčšak husay: hēšītan jahl: zufr Pashto
6893:xašm: hēšm
=== HUB xes ===
2350:kratzen, glatten, rasieren*, rallum *Pflugreute', rast-
2495:des Suffixes a (= phi. ak) davon ab, was doch das
2727:*Pflug, *Ring', Tfeir und frz. 'sceau iibersetzt).
3156:des Suffixes a (= phi. ak) von kUz = arm. LW. kuz
4725:*Pflug8terz*')r g. mdtk, arm. mad?; ydftan *erlangen* = paz.
6100:siparam) 'iibergeben', Wrzl. spar; supdr 'Pflug', afgh. spdra
6101:fem. 'Pflugschar; supurz 'Milz* = zd. spereza; supus, supus- 173 —
7812:supurz 'Milz' = zd. spereza, skr. pllhan-; supar 'Pflug =
8083:vivad- (oben p. 104) ; amdj 'Pflugsterz , g. mCLtk, arm. mac (?);
8792:die Entstehung und Geschichte des A-Suflixes im Mittel-
9514:xism Gl. and Ind. 68 = zd. aesma-; xEs, ka§. is, xis *Pflug*
=== SKT October/octave/octagon ===
12610:octagon,  a  plane  B>sidcd  (iguie,  (Gk.)  i
12616:October.  (L.)     U  Oct^btr, month  of  the  Roman  yenr.~L*.<
23097:octave — utas.                      ^^^H
```


## [2026-09-07T20:24:24.782Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 9505-9525 ===\"; sed -n '9505,9525p' HUB.txt\necho \"=== PHD hast entry ===\"; grep -n \"TWMNYA\" PHD.txt | head -5\necho \"=== PHD numerals table ===\"; sed -n '4800,4812p' PHD.txt\necho \"=== SKT 12605-12620 ===\"; sed -n '12605,12620p' SKT.txt"
}
```


### [2026-09-07T20:24:24.857Z] TOOL RESULT

```
=== HUB 9505-9525 ===
(aber nicht vor e aus ary- und aus ava-) vorgeschlagen.
§ 162. Vorschlag von x hat stattgefunden bei:
xastu *Kern* = xasta JRAS. 1894, p. 458 = asta, zd. ast-
*Knochen'; xaya *Ei* (mit h im Kurd., Afgh. und Bal.) =
paz. xdyay phi. xayak Shk. 254, Min. Gl. 125, gr. aJoV, lat.
Ovum\ xdm roh' (kurd. mit x, bal. mit h) = skr. ama-,
arm. hum; xirs 'Bar, phi. x(i)rs Bdh. 56, 14 und 17, zd.
aresa-, skr. rksa-; xist 'Ziegel', phi. oHst = zd.istya-; xism,
xasm 'Zorn , paz. xasm {xism) Min. Gl. 124, Shk. 254, phi.
xism Gl. and Ind. 68 = zd. aesma-; xEs, ka§. is, xis *Pflug*
= zd. aesa-; xurma 'Battel', paz. xurma Min. Gl. 128,
arm. armav (5. Jhd.).
Hier ist x schon im Phi. vorgeschlagen worden, aber
die Kegel, nach welcher dieser Vorschlag erfolgte, ist
unklar.
*) ^&1» Hamaddn ^^ phi. Ahmatan § 107, b und 143.— 266 —
Kapitel 32: Umstellung von Konsonanten.
§ 163. Die ap. Lautgruppen xr, fr, sr, zr, mr und zg
werden im Neupersischen (nicht im Phi.)? wenn sie im
Auslaut stehen, umgestellt.
a) Ap, xr = np. rx : surx roth* = phi. suxr , zd. suxra- ;
=== PHD hast entry ===
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
=== PHD numerals table ===
166
sahmgen sahmgenih sāstār
sāstārīh
rawen-! rawenidan! rawiánt raftan! saxtag sabz
šast”
sī
haštād* sagēn nawad* sēn
sēnag
sen murw sezd sézdén haftād*
darr-t
PAHLAVI KEY
— AA Sri 33
süxtarih saxtih
=== SKT 12605-12620 ===
Oohre,  a  fine  clay,  commonly  yellow. <F.-L.-Gk.)     O.R   ocrt,   *okcr;'   Cot
—  L.  ockra.  *  Gk.  uxpa,  yellow  ochre ; from  its  pale  colour.  — Gk.  uxpSs,  pale,  wan.
Octaffon,  Ootanffular,  &c ;  see Ootave.
Octave.  (F.-L.-Gk.)  Lit  'eigbtb;' bence,  eight  days  after  a  festi\'al,  eight ttotninmusic— F.  A'/aiv,  .in octave  (,Cot.).
—  L.  octaua,  feni.  of  octaum,  eighth.  *  L. octo,  eight  ^Gk.  ^«T«t,  eight :  cc^^te  with £.  Blsht.
octagon,  a  plane  B>sidcd  (iguie,  (Gk.)  i
ODE.
From  Gk.  iirrA.  for  htcrii^  eight ; angle,  der.  from  yiw,  knee ;  see
octahedron,  a  solid  8-sidrd  fi| (Gk.)  From  Axrd,  for  ^ctw,  eight;! a  base,  from  the  base  Af^,  to  »it ;  see
octangular,  having  eight  angles. From  L.  oct-o,  eight;  itni^n*!Hs,  angle.
ootant,  the  aspect  of  tv^o  planets  1 distant  by  the  eighth  part  of  a  circle. L.  ociatUt  stem  ocfan-t,  an  insti measuring  the  eighth  of  a  circle eight
October.  (L.)     U  Oct^btr, month  of  the  Roman  yenr.~L*.<
octogenarian,  one  who  ia  eif old,  (L.)  From  L.  oitogcnariw^j,  bcloo| to  eighty.  — L.  octo^ni,  eighty  each. tributivc  fonn  of  octoi^tttta^  eighty.—  U c'gbt ;  -ginta,  short  for  dtcinta  *,  a  di alive  qK  dtftm,  ten.
octosyllabic.  (L  -  Gk.)  U  «■( hbicui,  having  eight  syllables.— Glc. It eight;  avKKt^if,  a  syllable;  see  Byllat Ocular.  (L)  L.  ocularis,  beloogin| the  eye.  —  L.  acn/tts,  eye ;  cognate  with Sye.
binocular,  having  two  eyes.  (L.)  F L.  hni,  Hi'ublc;  ocultu,  eye,
inoculate.  (U)  In  old  airthon means  'to  engralt.'— L.  inoculatus,  M inoculare,  to  engraft,  insert  a  graft  —  L in ;  ffcu/uj,  an  eye,  also  a  bud  of  a  pUal
```


## [2026-09-07T20:24:44.556Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AE%DB%8C%D8%B4' --note 'page 372, root Oies, node 2: Persian خیش plough, etymology MP hēš/ēš' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/o%E1%B8%B1t%E1%B9%93w' --note 'page 372, root Okto: PIE *oḱtṓw eight, Pokorny 775' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%87%D8%B4%D8%AA' --note 'page 372, root Okto node 2: Persian هشت from MP hašt' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A7%D8%AE%D8%AA%D8%A7%D9%BE%D9%88%D8%B3' --note 'page 372, root Okto node 7: Persian اختاپوس from Greek oktopous' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/octopus' --note 'page 372, root Okto nodes 5-6: Greek oktopous, octopod' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A7%D8%AE%D8%AA%D8%A7%D9%BE%D9%88%D8%B3/' --note 'page 372, node 7: Mo3in entry اختاپوس = هشت پا' 2>&1 | tail -3"
}
```


### [2026-09-07T20:24:49.013Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/17a8f1a73c3d0cd5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d644eea6d03f1fa0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4c2ba24587aaedef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b530a4cf749187f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a9d497ac585f6eca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fad729a4a35ccdb7.txt
```


## [2026-09-07T20:24:54.702Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AE%DB%8C%D8%B4%DA%A9%D8%A7%D8%B1/",
 "prompt": "Show the Dehkhoda (لغتنامه دهخدا) and Mo'in entries for خیشکار: meaning (farmer/ploughman?) and any Ferdowsi verse quoted. Also mention if خویشکار is cross-referenced."
}
```


## [2026-09-07T20:24:55.828Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://fr.wiktionary.org/wiki/octopode",
 "prompt": "French entry octopode: etymology (Greek oktopous?), part of speech, meaning. Quote the etymology line."
}
```


### [2026-09-07T20:24:57.290Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:25:00.349Z] TOOL RESULT

```
# Octopode Etymology

**Part of Speech:** Adjective and noun (masculine)

**Etymology Line:** "Du grec ancien ὀκτώπους, _oktốpous_."

**Meaning:**
- As an adjective: Having eight feet or legs (e.g., "Mollusque octopode")
- As a noun: An order of cephalopods; also a sub-order of wingless insects with eight arm-like appendages; or a banner divided into eight flame-shaped sections

The term derives from ancient Greek, with the root referring to the number eight combined with "pous" (foot).
```


## [2026-09-07T20:25:04.550Z] TOOL CALL #54: WebSearch

```json
{
 "query": "\"کنم چاه آب اندر او صدهزار\" \"توانگر کنم مردم\" فردوسی خویشکار"
}
```


### [2026-09-07T20:25:11.729Z] TOOL RESULT

```
Web search results for query: ""کنم چاه آب اندر او صدهزار" "توانگر کنم مردم" فردوسی خویشکار"

Links: [{"title":"گنجور » فردوسی » شاهنامه » سهراب » بخش ۱۸","url":"https://ganjoor.net/ferdousi/shahname/sohrab/sh18"},{"title":"گنجور » فردوسی » شاهنامه » داستان هفتخوان اسفندیار » بخش ۷","url":"https://ganjoor.net/ferdousi/shahname/7esfandyar/sh7"},{"title":"گنجور » ملک‌الشعرا بهار » قصاید » شمارهٔ ۳۷ - فردوسی","url":"https://ganjoor.net/bahar/ghasidebk/sh37/"},{"title":"شعر فردوسی | بهترین اشعار کوتاه فردوسی","url":"https://www.alamto.com/sms/romance-sms/ferdowsi-love-poems"},{"title":"اشعار شاهنامه فردوسی | گلچینی از شعرهای حکیم ابوالقاسم فردوسی","url":"https://www.talab.org/art/poetry/%D8%A7%D8%B4%D8%B9%D8%A7%D8%B1-%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C.html"},{"title":"شاهنامه فردوسی – اندر ستایش سلطان محمود | PDF کافه کتاب","url":"https://ketab.cafe/%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87-%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C-%D8%A7%D9%86%D8%AF%D8%B1-%D8%B3%D8%AA%D8%A7%DB%8C%D8%B4-%D8%B3%D9%84%D8%B7%D8%A7%D9%86-%D9%85%D8%AD%D9%85/"},{"title":"اشعار فردوسی + عکس نوشته و مجموعه شعر فردوسی شاعر محبوب ایرانی","url":"https://roozaneh.net/fun/sms/%D8%A7%D8%B4%D8%B9%D8%A7%D8%B1-%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C/"},{"title":"اشعار شاهنامه فردوسی + گزیده اشعار فردوسی با موضوعات مختلف","url":"https://roozaneh.net/fun/sms/%D8%A7%D8%B4%D8%B9%D8%A7%D8%B1-%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87-%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C/"},{"title":"این شعر نیست این منام","url":"https://banvit.blogsky.com/1394/11"}]

I found search results for the Persian verses you were looking for. The search has returned several results from Persian poetry websites, particularly from Ganjoor (a comprehensive Persian literature database) and other Persian poetry collections.

The search results include various passages from Ferdowsi's works, including excerpts from the Shahnameh (Book of Kings), though the specific verses you mentioned ("کنم چاه آب اندر او صدهزار" and "توانگر کنم مردم") appear in collections of Ferdowsi's wisdom poetry and general verses about virtue, capability, and human conduct.

The results show that these phrases are part of Ferdowsi's classical Persian literature and can be found on websites dedicated to Persian poetry, particularly Ganjoor.net, which is a major online repository of Persian literature.

If you're looking for the complete context or a specific verse containing these exact phrases, I'd recommend visiting the Ganjoor website directly, as it contains the full texts of Ferdowsi's works with detailed organization by book and section.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:25:16.212Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://vajehyab.com/dehkhoda/%D8%AE%DB%8C%D8%B4%DA%A9%D8%A7%D8%B1",
 "prompt": "Dehkhoda entry for خیشکار: meaning, and any verse quoted (Ferdowsi?). Quote the entry text."
}
```


### [2026-09-07T20:25:17.738Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T20:25:21.936Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY خیش ===\"; grep -n \"خیش\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY hasht ===\"; grep -n \"هشت\" incoming/ARY/ARY_pages.txt | head -8\necho \"=== ARY latin index XIS/HAST ===\"; grep -n -i \"XIS\\|HAST\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T20:25:22.015Z] TOOL RESULT

```
=== ARY خیش ===
1972:معنی اين واژه در سانسکریت: خیش؛ چنگکك زمین صاف‌کنی. یی
=== ARY hasht ===
2509:سانسکریت (84۸/5877): تقا ۸1 آلبانی (الفاهشتم: متکاکه ,۸57
4516:۳ چم.این واژه در همه‌ی زبان‌های غبر ایرانی این فهرست "بهشت"» افردوس" است و ضنناً همه از زبان فارمی
8448:۱ چم اصلی این واژه: دهشتناک» پسیار بد» تنفرانگیز» مهلکك
9563:چم آغازین این واژه: وحشت‌انگیز» خشم آور» دهشت» غضب.
15672:هشت /۵۲۱
15703:واژه‌ی هشتم هم از همین ريشه است (صفحه‌ی ۷۷۵ در ۳01)07۷) 9
15725:بازگشت به: هشت» ده.
15733:هشتن (به چم *گذاشتن" رها کردن") / ۵۳۱
=== ARY latin index XIS/HAST ===
165:hast bap Mylo ebptey gtiy GUTS y cde 9 byl y eal e doy re Gere
816:cost Obj hast yea Glad, | YT
1155:witha S JOLT, hast ya slay ahos a yeh
1745:os (RUSSIAN) .g3 AXIS LATIN) 3
1754:BARNHART: (AXIS) 69 AHSA
1757:ONIONS: (AXIS, AXLE) 66 FAX, OXULL
1758:SKEAT: (AXIS, AXLE) 42 AXIS, AXLE ENGLISH) 53851
2993:WEBEN GERMAN) ghaST UBHNATL, SANSKRIT) cy Suse
3553:eat pe Sl Susy als “BK y “shast” 5 "ouSit” oluajly ccael "457" ph 2 BHI ols!
4953:FIDORDHR, FIORD, FARA SANSKRIT) cxiSuile 4°"
```


## [2026-09-07T20:25:26.825Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ns=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlines=s.split('\\n')\nprint('--- 15665-15710 ---')\nprint('\\n'.join(lines[15660:15712]))\nprint('--- 1960-1985 ---')\nprint('\\n'.join(lines[1960:1985]))\nEOF"
}
```


### [2026-09-07T20:25:28.074Z] TOOL RESULT

```
--- 15665-15710 ---
8 ,55 ,8۵ 5 (۸15۵) :هام05
سا کسونی کهن (542007 010): 15 0 (15) :۸1002/218
فریزی کهن (#اماکل۲ ضان): 15 63536 لاه
آلمانی کهن (/02804۸ ۲۲014 صا0): (هم) دادن
01 ,187 139 :۸40/0
بادداشت,
۱ در بيشتر زبان‌های هند و اروپایی کارواژ (فمل) "وجرد داشتن"» با بکارگیری دو ریشه‌ی 871۰ و +88 صرف
می‌شرد.
۲ پازگشت به: بودن.
ها
[pdf page 528]
هشت /۵۲۱
ی سک
اوستایی (4۷837): ۸ ۸8117۸ دانمارکی (1824(م0): 077
پهلوی (4۲7ا۳۸7): ایا ۱۲ نروژی (/(۸707(۲201۸): از ی ۳۷
اوستی (0585716): ۸7 ملندی (7ل770ا۵): ۸7
کردی (082[54): ۰ 8۸۹11۳ ,11875177 اسلاوی کهن (51476 ۲726 0ا0):
افغانی (پشتی) (/۵/6/۷: ۰ ۸5۸ ش۸3 0
تخاری ۸ (۸ [(ل42ل705): 0۵7 لهستانی (57/ق۳۵): 0
تخاری 8 (8 [(/ل70504۸7): 07 ررسی (/(755314): ادن
سانسکریت (5۸۸/5277): چکه (280۶)): 03
۸8۲2 ,۸817720 ناهآ۸8 بلفاری (مل0۸ا): 05
ارمنی (۷ل۵0/8/14): اسلا کی (51-0440): 03
ات0 ,ق0075 ,لا117 لیتوانی (/7271۸2۸ل): ادن
برنانی 08880): 0 ایرلدی کهن (#لکل#ا 1:۵ 007۳
لاتین (۵7100ا): 00 گالی (5]4ا.انا0۸): ادا
فرانسه (/(788): 17 برتونی (878702)+ 5 812
اسپانیایی (50۸(1374): 000 گالیک (0/اق0۸): 00
ایتالیایی (۸۸ل17۸): 0770 آلبانی ((ملمها)م: 717
رومانی (۸/۸۸(۷): 0۳7
پرتغالی (۳087001783): 070 پسگشت‌ها اند ی اد ند
گوتیکد (00710): ۰ - ۸1۸ را
ایسلندی کهن (/07010/2ف5 طا0): 8 (816133) + اانقدط
جر 27۸ 3 (817) 0
ساکسونی کهن (54260/0. هله): 0 ۰ 12۱ 816) :۸035/28
فریزی کهن (/(514ل7 00): ۸7۸ 4 81657) :0/05
آلمانی کهن (/(/0822 07اب ا0): ۸/170 9 (816117) 57
آلمانی (0872607): ۸7 7 (816111) ۸2400
انگلیسی کهن 8۸705 ۰:0 3۸۲17۸ برهان قاطع + ۳۳۳۸
انگلیسی (۸/0/754): ان
[pdf page 529]
یادداشست:
واژه‌ی هشتم هم از همین ريشه است (صفحه‌ی ۷۷۵ در ۳01)07۷) 9
۹
[ رس ۳ هن ای ۱
| کلیس سوای تسش ی 208
اوستایی (42372): 1 انگلیسی کهن (7ز8(/01./3 0]0): 10177۳71
پهلری (1هال۸ه): انگلیسی (8(/01/570): وا ند
0 ,۸811۲۸ ,۸7 تکفا نروژی (۷ا۵/087۷50): 71
کردی (00/5): هلندی (007۳2): ۸6
1 ,۸81715 ,1881711 لهستانی (#ل3ابا۵): 051831277581۸5
اففانی (پشتر) (/۳0/۸/۷/): ۸7۸ ,۸713۸ روسی (05540: ۷0۵882108589۸5
--- 1960-1985 ---
لیعوانی (17[411۸01۸/7.): ی ۱۲۷۷۱۹ ی
ایرلندی کهن. (1/3 ۰:0 ۰۰:۰۰ :11۸0۸0 .: زد رفن6 نکنام ب۵هه6 متام ما
0 6ر 5 ما موه
ی ی 3 راهم 0
با مود ون رکد صعسن هی
۸7 هامید
: : اس ی بردانعطع: 7
1 ۰ 1 اک لفت‌نامه دهدا:؟: ۹:۰ :۱ ۳۳
۱ با ار 1 فرهتگه معینن از اه ۸۶
باداش 1 0 وس
۱- معنی این واژه در هند و اروپایی و اکثر زبان‌های دیگر: کلنگ؛ پفکهه" 6
معنی اين واژه در سانسکریت: خیش؛ چنگکك زمین صاف‌کنی. یی
1 معنی اين واژه در رومانی: چماف, اک
1 معنی این واژه در آلمانی کهن: شُخم. ما دا وراه
1 ۲- 8168۸7 ,0217088 این واژه را فقط تا ریشه‌ی لاتین پیگیری می‌کند ‏ دا اش برع ورد
[ رس رآ ۹
رایس مورا 16
:
ارستایی 0۸90:8700 ,3۸018031 پوناني 108880 8۸1008 ر99ل4....
3 ان اقا رب را را هه
. پارسی نباستان (4(۷اق۶8 00 لائین (7100مل):(شاید) ۰ * :۲ هش :
بالالاز الک ما۸ روت واهررسیت : ی ‏ ب۸
پپلری (/اماتهم): ۰2۸3۸0 ,۱۸۵۸۵ اسپانبْانیٌ (52۸۸/7877): (شاید) 7 1 8
تخاری ۸ (۸4 70874/7): اه ,اقق ایتالیایی آ(( 4 2/): (شاید) ری ادن یه
تخاری 8(:8 ((فن702): 6۸۸ ,الا رومانی 21/4 #): (شاید) ۷1
```


## [2026-09-07T20:25:47.790Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT achtzig/achtzehn/acht ===\"; grep -n \"achtzig\\|achtzehn\\|astaiti\\|aStaiti\\|astati\" BRT.txt | head -10\necho \"=== KNT ashta ===\"; grep -n -i \"ašta\\|ashta\\|aštā\" KNT.txt | head -10"
}
```


### [2026-09-07T20:25:47.851Z] TOOL RESULT

```
=== BRT achtzig/achtzehn/acht ===
6459:•  j.  aätadasa-  Adj.  'der  achtzehnte': dasjmS  yat  ahmt  sJ'ärtS . .  °sa  (statt  NSm.) baiiatya  Yt.  /.  8.
6461:(i,  asiüdajä-  Adj.;  mp.  (Fü.)  alldahum. ■  j.  aitai^'vant-  Adj.  'achtzigfach':  'vti (asti    mfirS)     anian    zämätara    i^asura Yl  10. 116.
6471:I»  j.  aätätay-  fem.  Zw.  'achtzig':  'täitim mai',yairyehe  (sd-)  da^u/iJ  T^rüraftiake A.J.  II.         a)    mit    Gen.:    'taitlm.    atrt.-
15767:als  anderes,  'vor  allem':  tasta  ks  'rlm/ra- snäiaymY.S.  40,  j6.  7;  7.4a,  <y.  19,76,  ().49, Yt.  4-  3  (?) ;  ^-  Ayai  t-3  hSm  mainya  Jastatim 'rvtm  dazdl  gafmcä  ajyäitlmcä  (sd.)  Y. 30.  4;  —  at  Adi  *>/j"(sd.)  zard^ustrS  'rvfm Y.  43.  8 ;  —  aAys  yOsä  (sd.)  . .  *'rvlm^'>  , . vlsping  syadhanaY,  28.1'^',  *5/.23';  —  Ayap %wS  at»ASu^  za5>Bi  dans^m  °rvJm  Y.  43- 5;  II.  2)  'zu  Anfang,  bei  Beginn':  Ayat 'rvm*'>  iaf  usümpm(s±)älY. 56.1,^7. p.-!;
27171:Sü.  (zu  A.):    hastatiUkäbhis    sarvaira  jääpayi-
=== KNT ashta ===
1027:П. OP f from pIE р before consonant: pIE *pro, OP fra- as prefix, Skt. prá, Gk. тро. pIE *prek- in OP pte. u-fraštam ‘well punished’,
1337:pIE *su-prek-to-, OP ufrašta- ‘well punished’, cf.
1439:ni-Sad- from ni- + sad- (Iran. had-), and the value $ š is extended to positions where the š is separated 1 from the т by the augment: ntyaštāyam ‘I com- : | manded’ (but avastayam ‘I restored"), niyašāda- d yam ‘I commanded’, So also the enclitic pronoun. 3
2634:but OP u-frašta- u-frasta- ‘well punished’ (where
3859:69 iy : avaiy : mā : dauštā : biya : ufraštādiy : eri : (абу : Dara
3885:%A blank space of one character between the di- vider and the following @ #, KT. 2 [akunavam] WB, KT; but KT state that the traces of the last letter are pos- sibly those of &, which leads to a restored akunauS (во also RL), of which Auramazda would have to be the implied subject (ef. Oppert’s restoration, IdA 150). It is more probable that the phrase is here as in DB 5.17, 29, 38, and that akunavam is correct. ? ah*y^ RL, KT; first correctly normalized ёлу by Tm. VS 1.30. So also 4.68, 72, 87. 9 ufraštam КТ. ? manfiydhy} Opp. МА, ete., KT; man(iyahay) Tm. after DPe 20; man[ryáhaiy] Kent, since there is no reason to assume here the defective writing of DPe. |
3891:character, perhaps miswritten and erased, after the divider. * daustà WB, KT. 9 ...à KT; biylà WBn, НК, Tm. © atifraštādiy RL; aifrastádiy WB, Jn.; ufrastadvy KT.
4201:1 adam : Dārayavauš : XS : vazraka : XS XSyan 2 ат : XS DHnàm : Vistáspahy& : риса : Ha 3 xümanifya : 08у : Dàrayavaus : XS 4 : vaSnà : AMha : adam : ava : akunavam : tya : 5 akunavam : visahyà :frašam : Oadayataly Note то DSa: * frasam : 9adayátaiy, Hz. ApI 156-8, for the previously accepted frasia : 0adayámaiy; but Hinz, ZDMG 95.223-5, supporta a[dam : visa]hyà : frašta : @адауйтаїу. TRANSLATION OF DSa: 1. 1-3. Tam... (= DPa 1-5). $2. 3-5. Saith Darius the King: By the favor of Ahuramazda I have done that which I have done; to every one may it seem excellent.
5554:-diy emphatic encl. particle: Av. zi, Skt. hi, Gk. encl. -xı in vai-xı ‘yes indeed’, of-xé ‘not at all’, pIE *ghi ($88, 5191.1). ufraštā-diy DB 4.69 (JAOS 35.351-2; not pron. apm., with Bv. BSLP 31.2.63-4, Gr. $845); hardly vasnd-[dily XPg 7f (despite Lg. 9.320; see under apiy); 7‘va-diy A’Sd 3 (JAOS 51.229).
5710:frašta DSa 5, DS] 6: discussed by Bv. ВІР 30.1.63-4, Gr. $103, Gray AJP 53.67, Brd. WZKM 39.20-1; but fra$am @adaydlary and not frašta ðadayämaiy ($54.11) should be read in both pas- sages (Hz. AMI 3.9-10, ApI 156-8). See under frasa-.
```


## [2026-09-07T20:25:55.554Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"'eight'\\|eight’\\|eighty\\|eighteen\" KNT.txt | head -10"
}
```


### [2026-09-07T20:25:55.606Z] TOOL RESULT

```
2706:C. Expressing specification: пата ‘as to name’ (see Lex. s.v. for examples, and $312), and pos- sibly nama (if long-vowel loc. and not acc.); prob- ably We 1 CXX karíayà ‘120 (units) in weight’, and D'Sa 1 (and A?Hb) apadénam stündya (if for -üyà) afagainam ‘palace made of stone as to its column(s)’,
2715:D. Alone, to express specification: DNb 40f yãumainiš amiy ша daslaibuyü ша pādaibiyā ‘trained am I both as to hands and as to feet’. So also with numerals: DB 2.56 Andmakahya mahyd XV raucabi$ 6akatà aha ‘of the month Anamaka, 15 by days were past’; Wa 1 IT karšā ‘2 (units) by weight’; cf. Lg. 19.227-9.
4864:In Behistan 4.4, Darius states that the 19 battles recorded by him in the first three columns of the inscription, with the attendant capture of 9 usurpers, took place hamahyáyà 6arda ‘in one and the same year’. For eighteen of the battles dates are given in the Persian calendar, with translation into the Elamite and the Akkadian. The difficulty has been to arrange these dates within one year, beginning with the killing of Gaumata, the false Smerdis; for the order of the months in the Persian
5284:karSa- sb. ‘weight, (unit by) weight’ (like Lt. pondo, Lg. 19.227-9), = 83.33 gr. or slightly less than 3 oz. avoirdupois (Gray, JAOS 20.55; Sehmidt, Treasury of Persepolis 62): Skt. karga- ‘pull, unit by weight’ (§29.n2, $80, $1431, VI). The OP kar$a- was one-sixth of the Babylonian mana ‘mina’ (weight; not unit of value). Elam. transcribes kur-Sa-wm, = kršam, which may mark the word as netter, since Elam. transcriptions commonly represent the nom. sg. of the foreign word; but the other evidence is rather for the masc. karšā ism. (§252D; Lg. 19.227-9; not ndm.) Wal. karíayá lsm. (§251C; Lg. 19.227-9; not npm.) We 1; Wd 1.
```


## [2026-09-07T20:26:06.629Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN October/octave/octagon/octopus ===\"; grep -n \"^October,\\|^octave,\\|^octagon,\\|^octopus,\" KLN_1966.txt | head\necho \"=== LEW octo ===\"; grep -n \"^octō\\|^octo\\b\\|octō ‘acht\\|acht'\" LEW_1910.txt | head -5\necho \"=== LAT octo ===\"; grep -n \"^octo\\|octō\" LAT.txt | head -5\necho \"=== IEC oies / oisa ===\"; grep -n \"oieso\\|oisa\\|oies\\|isa, .*pole\\|thill\" IEC.txt | head -10"
}
```


### [2026-09-07T20:26:06.730Z] TOOL RESULT

```
=== KLN October/octave/octagon/octopus ===
26027:octagon,  n.,  a  plain  figure  with  eight  angles  and eight  sides  (geom.) — L.  octagonos,  fr.  Gk.  6xt<4- ycovo?,  ‘eight-angled’,  which  is  compounded  of oxtoc-  (see  octa-)  and  -ycovo q,  from  the  stem ofycovta,  ‘angle’.  See  -gon.
26048:October,  n.  —  L.  October  (mensis),  lit.  ‘the  eighth month  (of  the  Roman  year)’,  fr.  odd,  ‘eight’; see  octa-.  (The  Roman  year  began  with  March; cp.  September,  November,  December). octodecimo,  n.,  1)  a  book  in  which  each  sheet  is folded  into  eighteen  leaves;  2)  the  size  of  such  a book.  —  Fr.  L.  in  octodecimo,  ‘in  the  eighteenth’, fr.  in,  ‘in’,  and  octodecimus,  ‘eighteenth’,  fr.  oc- todecim,  ‘eighteen’,  which  is  compounded  of  oc- to,  ‘eight’,  and  decern,  ‘ten’.  See  octa-  and  deci¬ mal  and  cp.  octavo.
26054:octopus,  l)  (cap.)  a  genus  of  the  eight-armed Cephalopoda;  2)  any  member  of  this  genus.  — ModL.,  fr.  Gk.  ox-iottoo?,  ‘eight-footed’,  fr. oxtco,  ‘eight’,  and  nous,  gen.  noSo;,  ‘foot’.  See octo-  and  -pod  and  cp.  prec.  word, octoroon,  n.,  the  offspring  of  a  white  and  a  qua¬ droon.  —  Formed  on  analogy  of  quadroon  fr. L.  odd,  ‘eight’  (see  octa-) ;  so  called  in  allusion to  his  having  one  eighth  negro  blood, octosyllabic,  adj.,  having  eight  syllables.  — Compounded  of  octo-  and  syllabic, octosyllable,  n.,  a  word  or  line  of  eight  syllables.
=== LEW octo ===
=== LAT octo ===
=== IEC oies / oisa ===
680:ardis ‘pont, tip, peak’. WP I, 83. Cf. rtis, arstis, ardus Arm. ardn (‘dart, lance’. Consonantism ob- scure. If a LW, cf. arstis); Gk. árdis; MIr.Ir. aird, áird ‘point, peak’; ON cf. erta ‘to taunt’ (:Gk. árdis. Boisacq)
7177:(Forms with initial kou- or káu- include) Skt. kavíh, adj. ‘wise’; Av. kavis, id.; Lyd. (queried) kaüein, acc. sg. ‘priestess’ & kaües, m. (priest. Semantics uncertain); Myc. (queried) -kowo- ‘watcher’; Gk. koéo (fnotice'. -o- a compro- mise vowel (?) cf. ous, dotós); Lat. caveo “heed; advise'; Paelignan cf. coisatens “they cared’; Ir. cf. at-chiu, do-chiu ‘I see’; OE hā- wian ‘inspect’; ON heyja ‘supervise, execute’; G cf. Ver-hau ‘fence, enclosure’; Latv. kavëju ‘hesitate’ beside kautrs ‘shy’. For OCS čujọ & Cuvajg see keuuo, ið. See next
7513:kois- (?) ‘officiate; supervision’ Gk. koiáomai ‘officiate’; koíēs ‘priest’; Paelig. coisa-, v ‘care, be in charge of’; Lat. cüra, f., cūrō, are, v. ‘care’
8181:ksetros, à, om ‘protection; protector, hold- er’. Cf. WP I, 504 Skt. ksatrám ‘dominion, power’; Av. xSaðro ‘ruler’; -à, f. ‘kingdom’; -om “rule; -is, f. *mis- tress of the house’; OPer. xsaśa- ‘kingdom, kingship’; Oss. äxsar ‘strength’ (LW in Oss. saxár ‘town’, fr. Per.); Per. šahr ‘city’; Hitt. cf. sxassaras ‘mistress of the house’; Olr. cf. cathir, f. (/city', fr. *ksotri-); W (R-gde as Ir.) cadr 'strong'; cader, f. *hill fortress'; cadar, pl. cedyr, f. ‘defence, shield’; OCz. cf. šetřiti ‘watch’; Cz. ‘regard, care for, save’; Slovak šetriť “notice; spare’; Pol. szatrzyc się ‘take care’. The Gk. LW satrápēs represents an Av. form xSaðra-pavan- (Boisacq)
9972:loiksos, a ‘stroke, mark’. Cf. loisa & WP II, 344 Skt. lekhah, m., Aa f. ‘stroke, line, streak, fur- row; drawing, writing'; z-gde in likh-, rikh-, vbl. root ('scratch', etc.); Av. raeka "line"; (Li. láiSkas & laiskas “leaf: letter, message’; lai$kuüs "bitter, tar & OCS léxa 'garden-plot, bed, bor- der" are potential isophones only); Blg. cf. lèša, v. ‘scrape — hideg’
10000:loisthos (prob. for loidhst-, but cf. loisa) ‘track; following, behind’. WP II, 388 et seq. Gk. loisthos, -ios, adj. “left behind, last’; Go. laists, m. ‘track’ beside laistjan, v. ‘follow’; OHG leist, m. ‘footstep; cobbler's last’; lei- sten, v. “follow, perform’; OE læste, s. *cob- bler's last; læstan, v “follow, serve; do; en- dure; provide’; ON leistr. m. “foot; sock (The semantics are those of W ôl ‘track’; ad]. ‘rear’; olaf “last”, and of OCS slédü “track? and po-
10010:loisuos, à ‘free, open; field, pasture’. (Se- mantics of types aruos & loukos, q. v.) OE læs, gs læswe, f. ‘pasture, ley’; LG lees, n. trushbed'; OCS (?) lésü “forest? (and com. SL); Li. laísvas ‘free’ beside (*-1-) lysve, f. *gar- den-bed"; liesvos, fpl. ‘stairs’. Ambiguously to OCS lěxa, f. *garden-plot'; Lusat. lécha, id. (and ‘ploughed strip) See loisa. An EME form leasow (cited by C. T. Onions, but not by S. Johnson or R. Ainsworth) is given as ‘pasture, meadow’.
10764:red, waved'. Skt. cf. mütáh, pp. ‘moved’; Gk. cf. Moüsa, Moisa, Dor. mósa, Lacon. Mõa, f. ‘goddess of song, music and poetry'; Lat. mótum, sup. of moveo; cf. Cz. (?) mytit, inf. “clear, rid". WP II, 252
12038:oisa, io 'shaft-pole'. Cf. oios (2) Skt. ísa, f. id.; Av. isa, f. id.; LW in Finn. aisa, id.
15742:skoidh- (sKoidh-) (separate divide, scatter’. Cf. sKhidh- Maced. skoidos, m. (governor, manager’; Go. skaidan, sv. 7 ‘divide’; (MHG scheiden, sv. 7. !; scheit, m. “separation”; scheite, wf. ‘chip’; OHG cf. sceitila, f. (top of the head’: G Scheitel, id.); OE scada, wm. id.; Sw. sked, m. ('spoon'. Cf. G Span ‘chip’ for change of sense); Li. skaidà, f. “analysis'; skáidyti, inf. “analyse”; Latv. šķiežu, pf: Skiedu, inf. Skiest, v. ‘scatter, waste’; skaida, f. ‘chip’; Skiedi, mpl. ‘teeth of weaver's comb’; Variant in OCS (and com. W. SL) cěždọ, céditi, v. “strain, ft, (Isophonic: Ir. scaoid, m. *leash"). Extns. of type *skoidhro- in Li. skaidrüs, adj. “clear” beside skiedra, f. “fragment, chip'; Latv. skaidrs, as Li. beside šķiedra, f. ‘fibre’; cf. R SCedrina, f. pockmark'. (Consonantism in Gk. skethrós 'clear, exact. Cf. skedhros. Boisacq untenable). Cf. skoistos
```


## [2026-09-07T20:26:38.450Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%88%E0%A4%B7%E0%A4%BE",
 "prompt": "Sanskrit ईषा (īṣā): meaning and etymology — the Proto-Indo-Iranian and Proto-Indo-European reconstruction given, and cognates (Avestan, Greek, Slavic, Baltic)."
}
```


### [2026-09-07T20:26:44.030Z] TOOL RESULT

```
# ईषा (īṣā) - Sanskrit Word Entry

**Definition:**
This Sanskrit feminine noun refers to "the pole or shafts of a carriage or plough," and can also mean a plank, board, or particular measure.

**Etymology:**
The word traces back through Proto-Indo-Aryan and Proto-Indo-Iranian to Proto-Indo-European *h₂iHséh₂*, meaning "shaft." It shares linguistic roots with several ancient languages, including Ancient Greek terms for rudder handles and Hittite words for carriage poles.

**Related Languages:**
The entry notes cognates across Indo-European languages: "the handle of rudder, tiller, helm" in Greek, comparable terms in Old English that gave rise to the modern word "oar," and related vocabulary in Baltic and Slavic languages.

**Modern Descendants:**
The word evolved into related forms in several Indian languages, including Assamese, Gujarati, and Pali.

The detailed declension table demonstrates its function as a feminine ā-stem noun across Sanskrit's grammatical cases.
```


## [2026-09-07T20:26:51.974Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 -c \"\nimport json,glob\nf=sorted(glob.glob('data/verification/page-3*.json'))[-3:]\nprint(f)\nd=json.load(open('data/verification/page-317.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False))\nfor e in d['entries']:\n    print(e['entry'], e['root'], e['verdict'], len(e['nodes']))\nprint(json.dumps(d['entries'][0]['nodes'][0],ensure_ascii=False,indent=1)[:2500])\n\" 2>&1 | head -60"
}
```


### [2026-09-07T20:26:53.300Z] TOOL RESULT

```
['data/verification/page-37.json', 'data/verification/page-38.json', 'data/verification/page-39.json']
{"pdf_page": 317, "book_page": 287, "verified_by": "claude-opus-5", "verified_on": "2026-09-06"}
0 Mad confirmed 12
1 Madhaxa, Mazaxa, Madika confirmed 2
3 Mağa confirmed 1
{
 "id": 1,
 "lang": "Avestan",
 "words": "masya 1 : fish; mada : having too much liquid, drunk; mad : a water bird, mina",
 "verdict": "plausible",
 "derivation": "Two of the three items are real Avestan words. (a) masiia- 'fish' (Y. 2.8, Vd. 2.8 etc.) is well attested, and Pokorny 694 derives it, with Skt. matsya-, from an -es-stem *mades- 'the wet one' — this is precisely Nourai's arrow; but Buck (p. 184) already marks it with a question mark, and current handbooks (Martínez García & de Vaan, Introduction to Avestan, p. 32; en.wiktionary s.v. Reconstruction:Proto-Indo-Iranian/mátsyas) call PII *mátsyas 'unknown; possibly borrowed from the BMAC substrate', citing the lack of any relation to *peysk- or *dʰǵʰu-, with the *meh₂d- connection only as an 'alternative theory'. (b) maδa- m. 'intoxicating drink, intoxicated ecstasy' (Bartholomae AiW 1112 'Rauschbegeisterung durch Haoma-Genuss', beside the verb maδ- 'to become intoxicated', Y. 10.8, N. 30) is exactly Pokorny's 'av. maδa- Rauschtrank' — Nourai's gloss 'having too much liquid, drunk' is a loose paraphrase but the derivation is right. (c) 'mad : a water bird, mina' is not an Avestan word at all: Bartholomae records only the verb maδ-, and the water-bird word Nourai wants is Sanskrit madgu-, which Pokorny equates with New Persian māγ ('ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ'). The printed page (see refs/ocr/BOOK/317.png) has exactly what the JSON has, so this is Nourai's own slip — he moved the Sanskrit/Persian bird word up into the Avestan box to give māγ a parent.",
 "derivation_fa": "از سه واژهٔ این گره دو تا اوستایی راستین‌اند. یک: masiia- «ماهی» گواهی‌شده است و پوکورنی (ص ۶۹۴) آن را همراه سنسکریت matsya- از ستاکِ ‎*mades-‎ «آنِ تر» می‌گیرد، یعنی همان پیکان نورایی؛ اما باک (ص ۱۸۴) همان‌جا علامت پرسش گذاشته و پژوهش امروزی (مارتینس گارسیا و دِ فان، ص ۳۲؛ ویکی‌واژه ذیل *mátsyas) خاستگاه این واژه را ناشناخته و شاید وام‌واژه‌ای از زیرلایهٔ باکتریا-مرو (BMAC) می‌داند و پیوند با *meh₂d- را تنها «نظری دیگر» می‌شمارد. دو: maδa- «نوشابهٔ مست‌کننده، سرمستی» (بارتولومه، فرهنگ ایرانی باستان ستون ۱۱۱۲) دقیقاً همان «maδa- = Rauschtrank» پوکورنی است و اگرچه معنایی که نورایی داده («دارای مایع بسیار، مست») دقیق نیست، اشتقاق درست است. سه: «mad» به معنی «پرندهٔ آبی، مینا» هیچ گواهی اوستایی ندارد؛ بارتولومه فقط فعل maδ- را ثبت کرده و واژهٔ پرندهٔ آبی در واقع سنسکریت madgu- است که پوکورنی آن را برابرِ «ماغ» فارسی می‌گذارد. تصویر صفحهٔ چاپی (refs/ocr/BOOK/317.png) نشان می‌دهد متن استخراج‌شده امانتدار
```


## [2026-09-07T20:26:58.892Z] TOOL CALL #63: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T20:26:58.928Z] TOOL RESULT

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


## [2026-09-07T20:29:18.949Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_0x Deichsel ===\"; grep -c \"Deichsel\" POK_01.txt POK_02.txt POK_03.txt\necho \"=== POK_0x oiesos / oieion ===\"; grep -n \"oieion\\|oi.ion\\|oiako\\|Stange, Deichsel\" POK_01.txt POK_02.txt POK_03.txt | head\necho \"=== POK_full 774-776 lemma list ===\"; grep -n \"^Root / lemma\\|^Root/ lemma\" POK_full.txt | sed -n '1,1p' >/dev/null; python3 - <<'EOF'\nimport re\ns=open('POK_full.txt',encoding='utf-8',errors='replace').read()\n# find blocks with Page(s): 773-776\nfor m in re.finditer(r'Root ?/ ?lemma: ([^\\n]+)', s):\n    end=s.find('Page(s):', m.end())\n    if end>0:\n        pg=s[end:end+30].splitlines()[0]\n        if any(x in pg for x in ['773','774','775','776']):\n            print(m.group(1).strip(),'|',pg.strip())\nEOF"
}
```


### [2026-09-07T20:29:20.439Z] TOOL RESULT

```
=== POK_0x Deichsel ===
POK_03.txt:3
POK_01.txt:5
POK_02.txt:4
=== POK_0x oiesos / oieion ===
=== POK_full 774-776 lemma list ===
od-1 | Page(s): 772-773
od-2{*had-) | Page(s): 773
od-2{*had^\ "disgust, hate' derived from Root/ lemma: od-1 {* had^\ "to | Page(s): 773
oid- {*heid-os) | Page(s): 774
oi-no-, oi-uo- {*hei-uo-) | Page(s): 774
oiua {*he/-ua-) | Page(s): 774
ok- | Page(s): 774
ok-: 'to think over, *understand, see' derived from a reduced Root/ lemma: | Page(s): 774
oRtd(u) | Page(s): 775
oRtd(u)\ eight derived from the extended Root/ lemma: ok-\ "to think over, | Page(s): 775
ok"- , {*{*hek'^h- ) | Page(s): 775-777
ok"- : to see; eye derived from Root / lemma: deik- : to show' : Root / | Page(s): 775-777
sauel- sauol- | Page(s): 775-777
od(e)go-ox dd(e)g''o- | Page(s): 773
6g- ag- | Page(s): 773
oRu-s | Page(s): 775
```


## [2026-09-07T20:29:36.306Z] TOOL CALL #65: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg372.png data/verification/sources/refs/ocr/BOOK/372.png && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%88%E0%A4%B7%E0%A4%BE' --note 'page 372, root Oies: Sanskrit isa pole of plough, PIE *h2iHseh2' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://fr.wiktionary.org/wiki/octopode' --note 'page 372, node 6: French octopode from Greek oktopous' 2>&1 | tail -2; ls -la data/verification/sources/refs/ocr/BOOK/372.png"
}
```


### [2026-09-07T20:29:38.339Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/313bb453db6e2a16.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/55bdbe4f00db0d06.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 59170 Sep  7 16:29 data/verification/sources/refs/ocr/BOOK/372.png
```


## [2026-09-07T20:36:16.003Z] TOOL CALL #66: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-372.json",
 "content": "{\n  \"pdf_page\": 372,\n  \"book_page\": 342,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 1,\n      \"root\": \"Oies\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂iHs-eh₂ / *oy(H)-es- 'thill, shaft, pole of a plough or wagon' (Walde-Pokorny I 167 'oies- Stange, Deichsel'; Mann *oisa 'shaft-pole')\",\n      \"note\": \"Walde-Pokorny I 167 has the headword spelled exactly as Nourai spells it: 'Oies- „Stange, Deichsel“ (:ois-:is-)', with Slovene/Serbo-Croatian/Czech oje 'Deichsel' (es-stem ojes-, gen. ojese), Baltic *aisā (source of Finnish/Votic aisa 'pole of a forked shaft'), Greek *oiā / oiēion 'Steuerruder', Attic oiax, -kos 'Griff des Steuerruders', Homeric oiēes 'the rails on both sides of the yoke', and Sanskrit īṣā 'Deichsel'. Language label (Indo-European) and gloss ('pole') are therefore both right, and the spelling 'Oies' is Walde-Pokorny's own. Two caveats worth recording. (1) Pokorny's 1959 IEW dropped this headword: between 'oiu̯ā' (p. 774) and 'ok-' (p. 774) there is no oi(e)s- lemma at all, so the root survives in the literature only in WP I 167 and in Mann's IEC ('oisa, io: shaft-pole'); modern Wiktionary reconstructs *h₂iHséh₂ 'shaft' for the ā-stem. (2) WP I 167 itself does NOT list the Avestan word that Nourai hangs under the root — Buck says so in as many words at the page Nourai cites for the Avestan node ('Walde-P. 1.167, without aēša-').\",\n      \"note_fa\": \"ریشهٔ هندواروپاییِ *oy(H)-es-/‏*h₂iHs-eh₂ به معنی «مال‌بند، تیرِ گاوآهن یا گردون» در والده-پوکورنی (جلد ۱، ص ۱۶۷) با همین املا «Oies-» و همین معنا («Stange, Deichsel») آمده و بازماندگانش اسلاویِ oje، بالتیکِ ‎*aisā‎ (وام در فنلاندی aisa)، یونانیِ oiēion/oiax «سُکّان» و سنسکریت īṣā «مال‌بند» است؛ پس نام، برچسبِ زبانی و معنای ریشه در نمودار درست است. دو نکته را باید افزود: نخست آنکه پوکورنی در چاپ ۱۹۵۹ این سرواژه را کنار گذاشته و در فاصلهٔ صفحات ۷۷۴–۷۷۵ نشانی از oi(e)s- نیست، پس تنها گواهِ کتابی همان والده-پوکورنی و فرهنگ مان است؛ ویکی‌واژه امروز *h₂iHséh₂ «تیر، مال‌بند» را بازسازی می‌کند. دوم آنکه خودِ والده-پوکورنی واژهٔ اوستایی aēša- را زیر این ریشه نیاورده است و باک (ص ۴۹۶) هم صریح می‌گوید «والده-پوکورنی ۱٫۱۶۷، بدونِ aēša-».\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E0%A4%88%E0%A4%B7%E0%A4%BE\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"WLD1:167\",\n          \"status\": \"supports\",\n          \"note\": \"Walde-Pokorny Bd. I p. 167 (local WLD_Bd1_pages.txt leaf 176, running head 'ojes — oui-s 167'): 'Oies- „Stange, Deichsel“ (:ois-:is-). Slov. skr. cech. oje „Deichsel“ (St. ojes-, gen. slow. ojese); bait. *aisā als Quelle von finn. wot. aisa „Stange der Gabeldeichsel, Femerstange“ = gr. *oi[a]ā, oiēion „Steuerruder“, att. oiax, -kos „Griff des Steuerruders“, hom. oiēes „die Grille zu beiden Seiten des Joches“, ai. īṣā „Deichsel“.' Exactly Nourai's root and gloss.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"pp. 772-775 (POK_full.txt lemma index)\",\n          \"stance\": \"silent\",\n          \"note\": \"Pokorny 1959 has no oi(e)s- lemma: the alphabetical run is 'od-1' (772-773), 'od-2' (773), 'oid-' (774), 'oi-no-, oi-u̯o-' (774), 'oiu̯ā' (774), 'ok-' (774), 'oḱtō(u)' (775), 'okʷ-' (775-777). He dropped Walde-Pokorny's headword; grep of POK_01/02/03 for 'Deichsel' turns up nothing under an oies- entry.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.v. oisa (IEC.txt line 12038)\",\n          \"stance\": \"supports\",\n          \"note\": \"'oisa, io „shaft-pole“. Cf. oios (2). Skt. īṣā, f. id.; Av. īšā, f. id.; LW in Finn. aisa, id.' — Mann keeps the root as *oisa 'shaft-pole', i.e. Nourai's gloss, but names the Avestan cognate as īšā-, not aēša-.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck p. 496 (§8.21 PLOW)\",\n          \"stance\": \"supports\",\n          \"note\": \"'Av. aēša-, NPers. xēš prob. : Skt. īṣā- „pole of a plow or wagon“, Grk. οἴαξ „rudder-handle“, etc. (Walde-P. 1.167, without aēša-). Barth. 32.' — Buck ties the Iranian words to the WP I 167 root, which is Nourai's whole chart, with 'prob.'\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, IE roots list\",\n          \"stance\": \"silent\",\n          \"note\": \"no *oies-/*ois- root in Watkins' appendix (grep 'oies', 'ois-' in AHD_watkins1985.txt gives nothing); the thill/oar family is not represented in the AHD list at all.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"aeša 2 : pole, plow shaft\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan aēša- is a real word, but it is attested (once) with the sense 'plough', not 'pole, plow shaft': Horn, Grundriss no. 515, cites it from the list of farm implements in Vendīdād 14.10, and Bartholomae's Altiranisches Wörterbuch col. 32 puts it beside New Persian xēš with a cross-reference 'vgl. īšā- f. „Deichsel“'. Buck, Dictionary of Selected Synonyms p. 496, §8.21 PLOW, lists 'Av. karš-; aēša-' in the table of words for the plough and comments 'Av. aēša-, NPers. xēš prob. : Skt. īṣā- „pole of a plow or wagon“, Grk. οἴαξ „rudder-handle“, etc. (Walde-P. 1.167, without aēša-). Barth. 32.' — that single sentence is the source of Nourai's root box, of this node and of both its references. Formally Proto-Iranian *aiša- (< *oyH-s-o-, o-grade thematic, PIE *oy > Ir. ai, *s > š after i by the ruki rule) stands beside the ā-stem *oyH-s-eh₂ that gives Skt. īṣā- and (per Mann) Av. īšā-, so the arrow root→Avestan is sound. What is wrong is the gloss: 'pole, plow shaft' is the meaning of the ā-stem (Skt. īṣā-, Gk. oiēion), while aēša- means the implement, the plough. Note also that Nourai's '2' is his own homonym number, not Bartholomae's — Bartholomae's ²aēša- is the noun 'Suchen' (seeking).\",\n          \"derivation_fa\": \"«aēša-» واژه‌ای اوستایی و راستین است، اما معنای گواهی‌شدهٔ آن «گاوآهن، خیش» است، نه «مال‌بند»: هرن در «بنیاد ریشه‌شناسی فارسی نو» (شمارهٔ ۵۱۵) آن را از فهرست ابزارهای کشاورزی در وندیداد ۱۴٫۱۰ می‌آورد و بارتولومه در ستون ۳۲ فرهنگ ایرانی باستان آن را در کنار فارسی نوِ xēš می‌نشاند و به īšā- «مال‌بند» ارجاع می‌دهد. باک نیز در بند ۸٫۲۱ («گاوآهن») صفحهٔ ۴۹۶ می‌نویسد که «اوستایی aēša-، فارسی xēš، به احتمال هم‌ریشه با سنسکریت īṣā- «تیر گاوآهن یا گردون» و یونانی oiax» — همین یک جمله سرچشمهٔ کل این نمودار است. از نظر آوایی ایرانی آغازینِ ‎*aiša-‎ (از ‎*oyH-s-o-‎، با تبدیل s به š پس از i بر پایهٔ قاعدهٔ روکی) در برابر ستاکِ ā-داری می‌ایستد که سنسکریت īṣā- را داده است؛ پس پیکانِ ریشه ← اوستایی پذیرفتنی است. آنچه نادرست است معناست: «مال‌بند» معنای ستاکِ دیگر است و aēša- خودِ گاوآهن است. همچنین «۲» شمارهٔ همنام‌سازیِ خودِ نورایی است، نه بارتولومه (‎²aēša-‎ در بارتولومه به معنی «جستن» است).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E0%A4%88%E0%A4%B7%E0%A4%BE\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SYN:496\",\n              \"status\": \"supports\",\n              \"note\": \"Buck 1949, p. 496, last paragraph of §8.21 (SYN.txt line 12467, leaf-page header '496 SELECTED INDO-EUROPEAN SYNONYMS'): 'Av. aeSa-, NPers. xe prob. : Skt. isa- „pole of a plow or wagon“, Grk. otat „rudder-handle“, etc. (Walde-P. 1.167, without aésa-). Barth. 32.' — the arrow, both its references and the root are all taken from here.\"\n            },\n            {\n              \"ref\": \"BRT:32\",\n              \"status\": \"supports\",\n              \"note\": \"Bartholomae, AiW col. 31/32 (BRT.txt line 2777; the OCR of this leaf interleaves the two columns): the entry has '... — Inf. ištō; Absol. … np. x[ē]š, x[ē]š; vgl. īšā- f. „Deichsel“', i.e. Bartholomae's own equation of the Avestan word with NP xēš and with the 'Deichsel' stem — which is what Buck cites as 'Barth. 32'. The column header on the leaf reads '31 ³aēš- — ⁴aēša- II I i a. 32'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 515, p. 114\",\n              \"stance\": \"supports\",\n              \"note\": \"'515. xēš (dialektisch xēč) „Pflug“. aw. aēša- (vd. 14, 10 (43)); phlv. xēš(?). Darmesteter, Ét. ir. I, 77.' — gives the Avestan attestation (Vd. 14.10) and the Persian outcome, but glosses aēša- as 'Pflug', not 'pole'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 167\",\n              \"stance\": \"partial\",\n              \"note\": \"the root is there ('Oies- „Stange, Deichsel“') with Slavic oje, Baltic *aisā, Gk. oiēion, Skt. īṣā — but no Iranian form at all; Buck flags this explicitly ('without aēša-').\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. oisa (line 12038)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Skt. īṣā, f. id.; Av. īšā, f. id.' — Mann's Avestan cognate of the 'shaft-pole' word is īšā-, not aēša-, which supports the view that Nourai's gloss belongs to a different derivative of the same root.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"cols 31-35 (BRT.txt lines 2740-2830)\",\n              \"stance\": \"partial\",\n              \"note\": \"Bartholomae's numbered homonyms in this stretch are ²aēša- m. 'Suchen', ³aēša- Adj. 'potens', ⁴aēša- Pron. dem., aēšā- 'Habe, Eigentum' — so 'aeša 2' in the chart is not Bartholomae's numbering.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"xîš 2 «خیش ، خویش ۲» : plow or wagon pole; xîškâr «خیشکار ، خویشکار ۲» : farmer\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The core of the node is right and well supported: New Persian خیش (Classical xēš, modern xiš) continues Avestan aēša-. Horn no. 515 (p. 114) writes 'xēš (dial. xēč) „Pflug“. aw. aēša-; phlv. xēš(?)'; Hübschmann, Persische Studien §162 (p. 265) lists it among the words that took a prothetic x- before ē/i — 'xēs, kaš. is, xis „Pflug“ = zd. aēsa-' — the same prothesis as in xišt 'brick' < Av. ištya-, xišm 'wrath' < Av. aēsma-, xirs 'bear' < Av. arəša-; and Mo'in's own etymological footnote in Borhan-e Qāṭeʿ (printed p. 806 of the Amir Kabir reprint) reads 'خیچ ← خیش … اوستا aēša، پهلوی *xēš(؟) «استق ۵۱۵»', i.e. he simply follows Horn 515. English Wiktionary takes the same word from Middle Persian ēš / Manichaean MP hēš 'plough' (whence the Arabic loan خَيْش), which is the same etymon with a different treatment of the initial. Two things in the chart are off. (i) The gloss: خیش is the plough/ploughshare, not a 'plow or wagon pole' — Borhan p. 806: 'خیش … وزراری باشد جهت زراعت کردن، و بستنی کرد آهنی است که زمین را بدان شیار کنند … و دیگری چوبی است که بر گردن گاو نهند'; Moʿin: 'آلتی آهنین که آن را به گردن گاو بندند و بدان زمین را شخم زنند؛ گاوآهن'. (ii) The variant spellings خویش ۲ / خویشکار ۲: Nourai has a source for them (Borhan, p. ~802, does print 'خویشکار — با ثانی معدوله بر وزن پیشکار، برزیگر و مزارع را گویند'), but Horn rejects them outright in his footnote to no. 514: 'ein np. xʷēš „Pflug“ statt xēš (No. 515) giebt es nicht' — for Horn the xʷ- forms belong to خویش 'own, self' (Pahlavi xwēškār 'one who does his duty', Ferdowsī's خویشکار 'diligent, dutiful'), and the 'ploughman' sense of خویشکار is a later folk-etymological crossing of the two words. Modern lexicography follows Horn. The 'farmer' gloss of خیشکار itself is fine: literally 'plough-worker' (خیش + کار), i.e. ploughman > farmer.\",\n          \"derivation_fa\": \"هستهٔ این گره درست و مستند است: «خیش» فارسی نو (کلاسیک xēš، امروز xiš) بازماندهٔ اوستایی aēša- است. هرن (شمارهٔ ۵۱۵، ص ۱۱۴) می‌نویسد «xēš (گویشی xēč) گاوآهن؛ اوستایی aēša-؛ پهلوی xēš(؟)» و هوبشمان در «پژوهش‌های فارسی» بند ۱۶۲ (ص ۲۶۵) آن را در شمار واژه‌هایی می‌آورد که پیش از ē/i «خ» افزوده (پیش‌آیندِ خ) گرفته‌اند: «xēs، کاشانی is/xis «گاوآهن» = اوستایی aēsa-»، همان‌گونه که «خشت» از ištya-، «خشم» از aēsma- و «خرس» از arəša- ساخته شده است. معین نیز در حاشیهٔ برهان قاطع (ص ۸۰۶ چاپ امیرکبیر) می‌نویسد: «خیچ ← خیش … اوستا aēša، پهلوی ‎*xēš‎(؟) «استق ۵۱۵»» یعنی همان هرن ۵۱۵. ویکی‌واژه همین واژه را از فارسی میانهٔ ēš / مانوی hēš «گاوآهن» می‌گیرد (که معرّبِ آن «خَیش» است). دو نکته در نمودار نادرست است: یک، معنا؛ «خیش» گاوآهن است نه «مال‌بندِ گاوآهن یا گردون» (برهان: «آهنی است که زمین را بدان شیار کنند»؛ معین: «آلتی آهنین … گاوآهن»). دو، املای «خویش ۲» و «خویشکار ۲»؛ نورایی برای آن سند دارد (برهان، ص ۸۰۲: «خویشکار … برزیگر و مزارع را گویند») اما هرن در حاشیهٔ شمارهٔ ۵۱۴ صریح می‌گوید «فارسی نوِ xʷēš به معنی گاوآهن، در برابر xēš، وجود ندارد» و «خویشکار» را از «خویش» (خود) می‌داند (پهلوی xwēškār «وظیفه‌شناس»)؛ یعنی معنیِ «برزیگر» برای «خویشکار» آمیختگیِ ریشه‌شناسی عامیانهٔ دو واژه است. ریشه‌شناسی امروزی از هرن پیروی می‌کند. معنی «خیشکار = کشاورز» درست است: خیش + کار، «گاوآهن‌ران».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AE%DB%8C%D8%B4\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:114\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss p. 114 (HRN.txt leaf-block 136, running head '- 114 -'): '515. xēš (dialektisch xēč) „Pflug“. aw. aēša- (vd. 14, 10 (43)); phlv. xēš(?). Darmesteter, Ét. ir. I, 77.' The same page, footnote to no. 514, adds 'ein np. xʷēš „Pflug“ statt xēš (No. 515) giebt es nicht' — supporting the خیش arrow but denying the خویش variant.\"\n            },\n            {\n              \"ref\": \"BQT:803\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qāṭeʿ ed. Moʿin, vol. 2 (BQT_v2_pages.txt leaf 263; the leaf→page conversion for this volume is printed ≈ leaf + 543 ±3, so the cited 803 falls in this spread): headword 'خیش - بروزن پیش. وزراری باشد جهت زراعت کردن، و بستنی کرد آهنی است که زمین را بدان شیار کنند … و دیگری چوبی است که بر گردن گاو نهند - و نوعی از پارچه و بافتهٔ کتان هم هست'; Moʿin's footnote on the same page: 'خیچ (ه.م.) ← خیش (ه.م.). اوستا aēša، پهلوی *xēš(؟) «استق ۵۱۵»'. Leaf 259 (≈ p. 802) additionally prints 'خویشکار — با ثانی معدوله بروزن پیشکار، برزیگر و مزارع را گویند', which is Nourai's warrant for the خویشکار spelling and the 'farmer' gloss.\"\n            },\n            {\n              \"ref\": \"MON:1465\",\n              \"status\": \"partial\",\n              \"note\": \"the 6-volume print page could not be paged directly (no scan with that pagination on disk). Moʿin's entry itself is verifiable: MON_part1.txt (2-vol. Adena text) line 58612 'خیش: [- خیج - هیش] (کشا) آلتی آهنین که آن را به گردن گاو بندند و بدان زمین را شخم زنند؛ گاوآهن. (کشا.) شخم (زدن). جفت (زمین بنه)'. So Moʿin has the word with the 'plough' sense — but no 'pole' sense and no خویش headword for it.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien §162, p. 265 (HUB.txt line 9514)\",\n              \"stance\": \"supports\",\n              \"note\": \"'§ 162. Vorschlag von x hat stattgefunden bei: … xism, xasm „Zorn“ … = zd. aesma-; xēs, kaš. is, xis „Pflug“ = zd. aesa-; xurma „Dattel“ …' — Hübschmann's independent confirmation of Av. aēša- > NP xēš, with the phonetic mechanism (prothetic x-) named.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie 1971, s.v. hēš- (PHD.txt line 398)\",\n              \"stance\": \"silent\",\n              \"note\": \"MacKenzie has no Middle Persian xēš/hēš 'plough'; the nearest headwords are 'hēšag [hwsk' | N xēša] ear of corn, cluster' and 'hēšīdan, hōš- dry up, wither'. So Horn's 'phlv. xēš(?)' is still only a reconstruction.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II glossary\",\n              \"stance\": \"silent\",\n              \"note\": \"no xēš/hēš 'plough' in the glossary (grep 'hēš' gives only hēšm 'wrath', hōš 'death', hōšītan 'to wither').\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1.txt line 58612 s.v. خیش\",\n              \"stance\": \"supports\",\n              \"note\": \"'آلتی آهنین که آن را به گردن گاو بندند و بدان زمین را شخم زنند؛ گاوآهن' — plough, not pole.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"ARY_pages.txt (grep خیش)\",\n              \"stance\": \"silent\",\n              \"note\": \"Aryanpur's IE-roots dictionary has no entry for خیش (the single hit, line 1972, is a gloss 'خیش؛ چنگک زمین صاف‌کنی' inside a different root article).\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Okto\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *oḱtṓw 'eight' (Pokorny 775 oḱtō(u); Watkins oktō(u))\",\n      \"note\": \"Pokorny p. 775 has the lemma 'oḱtō(u), Meaning: eight', with Old Indic aṣṭa/aṣṭau, Avestan ašta, Armenian utʿ, Gk. oktō, Alb. tetë, Lat. octō, OIr. ocht n-, Goth. ahtau, ON átta, OHG/OS ahto, OE eahta, Lith. aštuo-nì, OCS osmь, Toch. B okt / A okät, and refs 'WP. I 172 f., WH. II 199 f., Trautmann 15 f.' — the WP page is confirmed by the running head of Walde-Pokorny Bd. I p. 172 ('ōku-s — oktu(u)'). Watkins/AHD has 'oktō(u). Eight … [Pok. oktō 775.]'. Modern Wiktionary reconstructs *oḱtṓw, notes the competing laryngeal shapes (*h₃eḱteh₃, *h₃eḱtoh₁) and keeps the old dual reading 'two sets of four (fingers)' as the likeliest morphological explanation — which is also Klein's ('an old dual form, orig. meaning „twice four“ (Tetradic system of reckoning)'). Root name, language label and gloss are all correct.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازینِ *oḱtṓw «هشت» در پوکورنی صفحهٔ ۷۷۵ با سرواژهٔ «oḱtō(u): eight» آمده است، همراه با سنسکریت aṣṭa/aṣṭau، اوستایی ašta، ارمنی utʿ، یونانی oktō، لاتین octō، گوتیک ahtau، انگلیسی کهن eahta و … و ارجاع به «والده-پوکورنی ۱٫۱۷۲ به بعد» که سرصفحهٔ همان صفحهٔ ۱۷۲ جلد یکم تأییدش می‌کند. واتکینز نیز در پیوستِ ریشه‌های هندواروپایی «oktō(u): Eight … [Pok. oktō 775]» دارد. ریشه‌شناسی امروزی همان *oḱtṓw را بازسازی می‌کند و شکل دوگانه (dual) بودن آن، یعنی «دو دستهٔ چهارانگشتی»، همچنان محتمل‌ترین توضیح ساختاری است (کلاین: «صورت دوگانهٔ کهن به معنی دو بار چهار»). نام ریشه، برچسب زبانی و معنا هر سه در نمودار درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/o%E1%B8%B1t%E1%B9%93w\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:775\",\n          \"status\": \"supports\",\n          \"note\": \"Pokorny IEW p. 775 (POK_full.txt block 'Root / lemma: oḱtō(u) … Page(s): 775'): 'Meaning: eight. Material: Old Indic aṣṭa, aṣṭau (besides aśītí- „eighty“), Avestan ašta… Armenian utʿ… gr. oktō; alb. tetë… Latin octō; Old Irish ocht n-… Gothic ahtau, Old Icelandic átta, Old High German Old Saxon ahto, Old English eahta; Lithuanian aštuo-nì; Old Church Slavic osmь… Tocharian B okt, A okät. References: WP. I 172 f., WH. II 199 f., Trautmann 15 f.'\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I p. 172 f. (WLD_Bd1_pages.txt leaf 181, running head '172 ōku-s — oktu(u)')\",\n          \"stance\": \"supports\",\n          \"note\": \"the WP entry oktō(u) begins on p. 172, exactly the page Pokorny cites; this is the source Pokorny 775 is a revision of.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. oktō(u)\",\n          \"stance\": \"supports\",\n          \"note\": \"'oktō(u). Eight. 1. Germanic *ahtō in: a. Old English eahta, eight: EIGHT; b. Old Norse ātjan (tjan, ten; see dekm), eighteen: ATTO-. 2. Latin octō, eight: OCTANS, OCTANT, OCTAVE, OCTAVO, OCTET, OCTO-, OCTOBER, OCTONARY; OCTODECIMO, OCTOGENARIAN. 3. Greek oktō, eight: OCTAD; OCTOPUS. [Pok. oktō 775.]' Watkins' introduction (p. 127 of the local text) also names oktō(u) among the numerals on which 'the dialects are in complete agreement'.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann s.v. oktou (IEC.txt line 12096)\",\n          \"stance\": \"supports\",\n          \"note\": \"'oktou (okto, okdo, okdou, okdmi) „eight“. Cf. ek- (ok-) and duou (?). WP I, 173. Skt. aṣṭāu, aṣṭá (perh. „2 tetrads“, MacDonell); Av. ašta; Per. hašt (infl. of haft „seven“); Oss. ast; Tokh. A okät, B okt; Arm. utʿ; Gk. oktō; Lat. octō; Alb. tetë; OIr. ocht; … Go. ahtau; OE eahta; ON átta; … Li. aštuoni.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ašta 3 : eight; ašta-dasa : eighteen; aštâti, aštaiti : eighty\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three forms are correct Iranian reflexes of *oḱtṓw. Avestan ašta 'eight' shows the regular Iranian developments *o > a and *ḱt > št (Pokorny 775 'Avestan ašta'; Klein p. 504 'Avestic ashta'). ašta-dasa is the compound ašta + dasa 'ten' for '18'; Bartholomae records it as 'j. aštadasa- Adj. „der achtzehnte“' (the ordinal, from the same compound). 'aštâti, aštaiti' is the abstract in -ti- for '80': Bartholomae has 'j. aštātay- fem. Zw. „achtzig“' (stem aštāti-), Platts spells it aštāiti, and Moʿin's Borhan footnote gives 'آوستا aštāiti- (هشتاد)' — so both of Nourai's spellings are current transliterations of the same word. Platts & Ranking, Grammar of the Persian Language p. 41 supplies exactly Nourai's three items with exactly his 'Old Persian' labelling: '8. ۸ هشت (O.P. ashta)', '18. ۱۸ هژده/هشتده (O.P. ashtadasa)', '80. هشتاد (Phl. hashtat; O.P. ashtaittī)'. One caveat: the numeral 'eight' is nowhere spelled out in the Old Persian inscriptions (Kent's lexicon has no ašta-; OP writes numbers as figures), so the '/ Old Persian' half of the language label is Platts's reconstruction, not an attested form. Nourai's '3' is again his own homonym number.\",\n          \"derivation_fa\": \"هر سه صورت بازتاب‌های درستِ ایرانیِ *oḱtṓw هستند. اوستایی ašta «هشت» دگرگونی‌های قاعده‌مندِ ایرانی را نشان می‌دهد: ‎*o‎ هندواروپایی به a و خوشهٔ ‎*ḱt‎ به št بدل شده (پوکورنی ۷۷۵؛ کلاین ص ۵۰۴). ašta-dasa ترکیبِ ašta + dasa «ده» برای «هجده» است و بارتولومه آن را «aštadasa- صفت: هجدهمین» ثبت کرده است. «aštāti/aštāiti» نامِ معنیِ ‎-ti-‎دار برای «هشتاد» است: بارتولومه «aštātay- مادّه: هشتاد» دارد، پلاتس آن را aštāiti می‌نویسد و معین در حاشیهٔ برهان «آوستا aštāiti- (هشتاد)» آورده؛ پس هر دو املای نورایی گونه‌های آوانگاریِ یک واژه‌اند. دستور زبان فارسیِ پلاتس و رنکینگ (ص ۴۱) دقیقاً همین سه مورد را با همین برچسبِ «پارسی باستان» می‌آورد. یک احتیاط: عددِ «هشت» در سنگ‌نوشته‌های پارسی باستان به‌صورت واژه نوشته نشده است (کنت در واژه‌نامهٔ خود ašta- ندارد و اعداد با رقم نوشته می‌شدند)؛ پس نیمهٔ «پارسی باستان» برچسب، بازسازیِ پلاتس است نه صورتی گواهی‌شده. ادعای نورایی در مجموع درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/o%E1%B8%B1t%E1%B9%93w\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:775\",\n              \"status\": \"supports\",\n              \"note\": \"'Material: Old Indic aṣṭa, aṣṭau …, Avestan ašta … Other congruities are to name ved. aṣṭādaśa- 18, Avestan aštadasa- „the 18.“, gr. oktō(kai)deka, Latin octōdecim' — the Avestan cardinal and the '18' compound are both there.\"\n            },\n            {\n              \"ref\": \"KLN:504\",\n              \"status\": \"supports\",\n              \"note\": \"Klein 1966 vol. I p. 504 s.v. eight (KLN_1966.txt line 12734): '… and cogn. with OI. aṣṭā, aṣṭāu, Avestic ashta, Toch. A okat, B okt, Arm. utʿ (for *optō), Gk. oktō, Alb. tetë (for *okto-t), L. octō, OSlav. osmь …, Lith. aštuoni, OIr. ocht n-, W. wyth, Bret. eiz, „eight“. All these words prob. derive fr. I.-E. *oktō(u), an old dual form, orig. meaning „twice four“.'\"\n            },\n            {\n              \"ref\": \"GPL:41\",\n              \"status\": \"supports\",\n              \"note\": \"Platts & Ranking, A Grammar of the Persian Language, Part I, p. 41 (GPL.txt lines 520-540; the running head on that page reads 'Numerals—The Cardinal Numbers 41'): '8. ۸ هشت (O.P. ashta)'; '18. ۱۸ هژده، هشتده (O.P. ashtadasa)'; '80. هشتاد (Phl. hashtat; O.P. ashtaittī)'. All three of Nourai's forms, with his labelling.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae AiW (BRT.txt lines 6459, 6471)\",\n              \"stance\": \"supports\",\n              \"note\": \"'• j. aštadasa- Adj. „der achtzehnte“: dasəmə yat ahmāt … Yt. 1.8' and '• j. aštātay- fem. Zw. „achtzig“: aštātim maiδyairyehe … A. 3.11' — the two derived numerals of the node, in Avestan.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, Lexicon\",\n              \"stance\": \"silent\",\n              \"note\": \"no OP numeral for 'eight' in the lexicon (grep \\\"'eight'\\\" and 'eighty' in KNT.txt returns only unrelated discussion of the Behistan chronology and of karša- weights); OP wrote numbers with figures, so 'Old Persian ašta' is an inference.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. oktou\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. ašta' listed directly under the root, beside Skt. aṣṭāu.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e rišehā, p. 521 (ARY_pages.txt pdf page 528)\",\n              \"stance\": \"supports\",\n              \"note\": \"entry هشت with 'اوستایی (AVESTAN): AŠTA … پهلوی (PAHLAVI): HAŠT … سانسکریت: AṢṬAU, AṢṬĀ … لاتین: OCTO … گوتیک: AHTAU … انگلیسی کهن: EAHTA', and the note 'واژهٔ هشتم هم از همین ریشه است (صفحهٔ ۷۷۵ در POKORNY)' — Aryanpur cites the same Pokorny page as Nourai.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"hašt «هشت» : eight (extra: هیجده ، هشتاد)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan ašta > Middle Persian hašt > New Persian هشت. Nyberg's Pahlavi glossary has 'hašt [hšt'; figures] eight', 'haštom eighth', 'hašt-dahom eighteenth'; MacKenzie writes the word with the Aramaic heterogram (hašt [TWMNYA < Aram. tmny]) and lists haštād in his numeral key (p. 166). The initial h- is not inherited — Old Iranian ašta- should give *ašt — and both Mann (s.v. oktou: 'Per. hašt (infl. of haft „seven“)') and Moʿin's own footnote in Borhan-e Qāṭeʿ ('«هشت» در پارسی جدید از «هفت» گرفته شده') explain it as analogical after haft 'seven', the neighbouring numeral. The two extra forms in the box follow the same line: هشتاد 'eighty' < MP haštād < Av. aštāiti- (Borhan: 'هشتاد … آوستا aštāiti- (هشتاد). پهلوی haštāt'), and هیجده/هژده 'eighteen' < هشتده < MP hašt-dah (Borhan: 'هشتده … از: هشت + ده'; Nourai's ☞Dekm cross-reference for the '-dah' element is right). Nourai's reference number is wrong by 100: the هشت / هشتاد / هشتده entries with Moʿin's etymological footnotes stand on p. 2338 of the Amir Kabir reprint (vol. 4), not on 2238, which carries the نیو… entries. The printed page of Nourai's own book (see data/verification/sources/refs/ocr/BOOK/372.png) does read 'BQT:2238', so the slip is the author's, not the extraction's.\",\n          \"derivation_fa\": \"اوستایی ašta ← فارسی میانهٔ hašt ← فارسی نوِ «هشت». نیبرگ در واژه‌نامهٔ پهلوی «hašt [hšt']: هشت»، «haštom: هشتم» و «hašt-dahom: هجدهم» را ثبت کرده و مکنزی آن را با هزوارش آرامیِ TWMNYA می‌نویسد و «haštād» را در کلید اعدادِ ص ۱۶۶ می‌آورد. «ه»ی آغازی ارثی نیست — از ایرانی باستانِ ašta- انتظار «‎*اشت‎» می‌رفت — و هم مان (زیر ریشهٔ oktou: «فارسی hašt، به تأثیر haft») و هم خودِ معین در حاشیهٔ برهان قاطع («هشت در پارسی جدید از هفت گرفته شده») آن را همگونیِ قیاسی با «هفت»، یعنی عددِ همسایه، می‌دانند. دو صورتِ افزودهٔ جعبه هم بر همین خط‌اند: «هشتاد» از فارسی میانهٔ haštād و آن از اوستایی aštāiti- (برهان: «آوستا aštāiti-؛ پهلوی haštāt») و «هیجده/هژده» از «هشتده» و آن از پهلویِ hašt-dah (برهان: «هشتده … از: هشت + ده»؛ ارجاعِ نورایی به ریشهٔ Dekm برای جزء «ـده» درست است). ارجاعِ نورایی صد صفحه خطاست: مدخل‌های «هشت»، «هشتاد» و «هشتده» با حواشیِ ریشه‌شناسیِ معین در صفحهٔ ۲۳۳۸ چاپ امیرکبیر (جلد ۴) است، نه ۲۲۳۸ که مدخل‌های «نیو…» را دارد. تصویر صفحهٔ چاپیِ کتاب نشان می‌دهد که در متن هم «BQT:2238» چاپ شده است، پس خطا از نویسنده است نه از خوانشِ اسکن.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%87%D8%B4%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:2238\",\n              \"status\": \"not_found\",\n              \"note\": \"checked the text: p. 2238 of the Amir Kabir reprint = vol. 4 pdf leaf 320 (running head '۲۲۳۸'), which carries نیو، نیوار، نیوباریدن، نیوشیدن … and nothing on 'eight'. Nourai's number is a slip for 2338.\"\n            },\n            {\n              \"ref\": \"BQT:2338 (the page Nourai means)\",\n              \"status\": \"supports\",\n              \"note\": \"vol. 4 pdf leaf 420 = printed p. 2338: 'هشت - بفتح اول. اوستا ašta (هشت). پهلوی hašt (hašt). هندی باستان aṣṭā(u)، ارمنی utʿ، افغانی atə، استی ast، وخی haṭ/hašt … یغنوبی ašt. «هشت» در پارسی جدید از «هفت» گرفته شده. «اسشق ۱۰۹۵»'; and directly below, 'هشتاد - بفتح اول؛ آوستا aštāiti- (هشتاد). پهلوی haštāt'; and on p. 2339 'هشتده - بفتح اول و چهارم، از: هشت + ده … رک: هیجده'. Exactly what the arrow says.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB.txt lines 1955-1956)\",\n              \"stance\": \"supports\",\n              \"note\": \"'hašt [hšt'; figures] eight.' / 'hašt-dahom [hštdhwm] eighteenth. haštom [hštwm; 8-wm] eighth.'\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie 1971, addenda s.v. hašt and Pahlavi key p. 166\",\n              \"stance\": \"supports\",\n              \"note\": \"'hašt [TWMNYA < A tmny …]' (the Aramaic heterogram for the numeral) and 'haštād*' in the numerals list of the Pahlavi key (PHD.txt line 4806) — MP hašt/haštād as the ancestor of the Persian forms.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. oktou\",\n              \"stance\": \"supports\",\n              \"note\": \"'Per. hašt (infl. of haft „seven“)' — independent statement of the analogical h-.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"en.wiktionary / Moʿin\",\n              \"stance\": \"supports\",\n              \"note\": \"English Wiktionary s.v. هشت: 'from Middle Persian 𐭧𐭱𐭲 (hašt) … ultimately from Proto-Indo-European *oḱtṓw', with Northern Kurdish heşt and Sanskrit अष्ट (aṣṭa) as cognates.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur p. 521\",\n              \"stance\": \"supports\",\n              \"note\": \"same chain: اوستایی AŠTA / پهلوی HAŠT / فارسی هشت, with a reference to Pokorny p. 775.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"ahtô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Nourai's 'ahtô' is Proto-Germanic *ahtōu / *ahtō 'eight', the regular outcome of *oḱtṓw: PIE *o > Gmc. a, and the cluster *ḱt > *ht by Grimm's law (the *k spirantizes to h before t). Watkins gives it in precisely this shape: 'oktō(u). Eight. 1. Germanic *ahtō in: a. Old English eahta, eight: EIGHT; b. Old Norse ātjan …, eighteen: ATTO-.' Klein p. 504 lists the daughter forms — OS ahto, ON átta, Swed. åtta, Dan. otte, OFris. ahta, Du. acht, OHG ahto, MHG ahte, G. acht, Goth. ahtau — and Pokorny 775 adds Runic a:tta and OHG/OS ahto. This is a pass-through node with no word-internal problem.\",\n          \"derivation_fa\": \"«ahtô» در نمودار همان ژرمنیِ آغازینِ ‎*ahtōu/*ahtō‎ «هشت» است، بازتابِ قاعده‌مندِ *oḱtṓw: واکهٔ ‎*o‎ هندواروپایی در ژرمنی به a بدل شده و خوشهٔ ‎*ḱt‎ بر پایهٔ قانون گریم به ‎*ht‎ (سایشی شدنِ k پیش از t) دگرگون شده است. واتکینز همین صورت را می‌آورد: «۱. ژرمنیِ ‎*ahtō‎ در: الف) انگلیسی کهن eahta …». کلاین (ص ۵۰۴) صورت‌های دخترین را برمی‌شمارد: ساکسونی کهن ahto، نورسِ کهن átta، سوئدی åtta، دانمارکی otte، هلندی acht، آلمانی علیای کهن ahto، آلمانی acht، گوتیک ahtau. این گره واسطه است و اشکالی ندارد؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/o%E1%B8%B1t%E1%B9%93w\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. oktō(u): '1. Germanic *ahtō in: a. Old English eahta, eight: EIGHT; b. Old Norse ātjan (tjan, ten; see dekm), eighteen: ATTO-.' Nourai's 'ahtô' is Watkins' *ahtō.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein p. 504 s.v. eight\",\n              \"stance\": \"supports\",\n              \"note\": \"'ME. eighte, eihte, fr. OE. eahta, rel. to OS. ahto, ON. átta, Swed. åtta, Dan. otte, OFris. ahta, Du. acht, OHG. ahto, MHG. ahte, G. acht, Goth. ahtau, „eight“.'\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p. 775\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gothic ahtau. Old Icelandic átta. Old High German Old Saxon ahto. Old English eahta' — plus the Runic/Norse a:tta, átta forms listed in the table.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. oktou\",\n              \"stance\": \"supports\",\n              \"note\": \"'OHG ahtowi, pl.; MHG ehtewe, pl. beside aht, eht; Go. ahtau; OE eahta; ON átta.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"eight, eighteen, eighty\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are inherited, not borrowed, and descend through Old English from Germanic *ahtō. Klein p. 504: eight < ME eighte, eihte < OE eahta; eighteen < ME eightetene, eihtene < OE eahtatȳne, eahtatēne, i.e. eahta + -tȳne '-teen'; eighty < ME eigteti < OE (hund)eahtatig, i.e. eahta + -tig, the suffix of the decades. The -gh- of the modern spelling is the orthographic residue of the Old English velar fricative /x/ (< PGmc *ht), which was lost in pronunciation during the fifteenth century with compensatory lengthening of the preceding vowel, giving ME /eixt/ > /eːt/ > modern /eɪt/.\",\n          \"derivation_fa\": \"این سه واژه ارثی‌اند نه وام‌واژه، و از راهِ انگلیسی کهن از ژرمنیِ ‎*ahtō‎ می‌آیند. کلاین (ص ۵۰۴): eight از انگلیسی میانهٔ eighte/eihte و آن از انگلیسی کهنِ eahta؛ eighteen از انگلیسی کهنِ eahtatȳne (یعنی eahta + پسوندِ ‎-tȳne‎ = «‎-teen‎»)؛ eighty از انگلیسی کهنِ (hund)eahtatig (یعنی eahta + پسوندِ دهگانِ ‎-tig‎). حرف‌های «gh» در املای امروزی یادگارِ سایشیِ کامیِ /x/ انگلیسی کهن (از ‎*ht‎ ژرمنی) است که در سدهٔ پانزدهم از تلفظ افتاد و واکهٔ پیش از خود را کشیده کرد: /eixt/ ← /eːt/ ← /eɪt/ امروزی. این گره در نمودار مرجعی ندارد ولی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"(none cited)\",\n              \"status\": \"not_checked\",\n              \"note\": \"the node carries no refs= in the book; checked against Klein p. 504 and Skeat s.v. Octave/eight instead (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein pp. 504-505, s.vv. eight, eighteen, eighty\",\n              \"stance\": \"supports\",\n              \"note\": \"'eighteen … fr. OE. eahtatyne, eahtatene, fr. eahta, „eight“, and -tyne, -tene, „-teen“'; 'eighty … ME. eigteti, fr. OE. (hund)eahtatig … See hundred, eight and -ty, suff. denoting multiples of ten.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict., s.v. Octave\",\n              \"stance\": \"supports\",\n              \"note\": \"'L. octo, eight (Gk. ὀκτώ, eight: cognate with E. Eight)' — Skeat's cross-reference makes the same inherited English/borrowed Latin split that the chart draws.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, s.v. oktō(u) and index s.v. EIGHT\",\n              \"stance\": \"supports\",\n              \"note\": \"index entry 'EIGHT oktō(u)'; the Germanic branch of the root article names Old English eahta > EIGHT.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Greek\",\n          \"words\": \"oktô : eight; oktô-pous : eight legged\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek ὀκτώ is the direct reflex of *oḱtṓw (Watkins: '3. Greek oktō, eight: OCTAD; OCTOPUS'; Pokorny 775 'gr. oktō', with the Ionic-Attic ordinal ὄγδο(ϝ)ος showing secondary -γδ- after ἕβδομος). ὀκτώπους 'eight-footed' is a regular Greek possessive compound of ὀκτώ + πούς, gen. ποδός 'foot' (Klein s.v. octopus: 'Gk. ὀκτώπους „eight-footed“, fr. ὀκτώ „eight“, and πούς, gen. ποδός „foot“'), so Nourai's cross-reference ☞Ped for the second element is right — Watkins indexes OCTOPUS under both oktō(u) and ped-¹. Etymonline s.v. octopus confirms 'Latinized form of Greek oktōpous, literally „eight-foot“'. The gloss 'eight legged' is the adjectival use, which is what the compound is.\",\n          \"derivation_fa\": \"یونانیِ ὀκτώ بازتابِ مستقیمِ *oḱtṓw است (واتکینز: «۳. یونانی oktō، هشت: OCTAD؛ OCTOPUS»؛ پوکورنی ص ۷۷۵ «gr. oktō»، با ترتیبیِ ایونی-آتیکِ ὄγδο(ϝ)ος که ‎-γδ-‎ آن به قیاسِ ἕβδομος «هفتم» ثانوی است). ὀκτώπους «هشت‌پا» ترکیبِ داراییِ قاعده‌مندِ یونانی از ὀκτώ + πούς (اضافیِ ποδός) «پا» است (کلاین ذیل octopus). پس ارجاعِ نورایی به ریشهٔ Ped برای جزء دوم درست است؛ واتکینز نیز OCTOPUS را هم زیر oktō(u) و هم زیر ‎ped-¹‎ فهرست می‌کند. اتیمونلاین هم می‌گوید octopus «صورتِ لاتینی‌شدهٔ یونانیِ oktōpous، تحت‌اللفظی هشت‌پا» است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/octopus\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. oktō(u): '3. Greek oktō, eight: OCTAD; OCTOPUS'; the alphabetical index adds 'octopus oktō(u), ped-¹', i.e. the compound is analysed exactly as ὀκτώ + πούς.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. octopus (KLN_1966.txt line 26054)\",\n              \"stance\": \"supports\",\n              \"note\": \"'octopus … ModL., fr. Gk. ὀκτώπους, „eight-footed“, fr. ὀκτώ, „eight“, and πούς, gen. ποδός, „foot“. See octo- and -pod.'\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p. 775\",\n              \"stance\": \"supports\",\n              \"note\": \"'gr. oktō … gr. oktō(kai)deka … gr. oktakosioi' — the Greek numeral and its compounds under the root.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Octave / octagon\",\n              \"stance\": \"supports\",\n              \"note\": \"'octagon … From Gk. ὀκτά-, for ὀκτώ, eight; γωνία, angle' — same Greek base.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"octopode\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French octopode (adjective 'having eight feet', noun 'an octopod; the order Octopoda') is a learned nineteenth-century zoological formation taken straight out of Greek, not inherited through Latin: French Wiktionary gives the etymology in one line, 'Du grec ancien ὀκτώπους, oktṓpous'. Etymonline dates the parallel English octopod 'eight-footed or eight-armed animal' to 1826, the same wave of Cuvier-era taxonomy (Octopoda). So the arrow Greek → French that Nourai draws — bypassing Latin — is the right shape for this word; the word is a coinage on the Greek stem ὀκτώποδ- with the French adjectival ending -e.\",\n          \"derivation_fa\": \"واژهٔ فرانسویِ octopode (صفت «هشت‌پا»، اسم «هشت‌پایان، راستهٔ Octopoda») ساختی است دانشورانه از سدهٔ نوزدهم که یکسر از یونانی گرفته شده و از راه لاتین به ارث نرسیده است: ویکی‌واژهٔ فرانسوی ریشه را در یک سطر می‌آورد: «Du grec ancien ὀκτώπους, oktṓpous». اتیمونلاین صورتِ همتای انگلیسی، octopod «جانورِ هشت‌پا»، را به سال ۱۸۲۶ می‌رساند، یعنی همان موجِ رده‌بندیِ جانوریِ روزگار کوویه. پس پیکانِ «یونانی ← فرانسوی» که نورایی کشیده — با گذر از کنارِ لاتین — برای این واژه درست است؛ واژه بر ستاکِ یونانیِ ὀκτώποδ- با پایانهٔ صفتیِ فرانسویِ ‎-e‎ ساخته شده است.\",\n          \"sources\": [\n            \"https://fr.wiktionary.org/wiki/octopode\",\n            \"https://www.etymonline.com/word/octopus\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"(none cited)\",\n              \"status\": \"not_checked\",\n              \"note\": \"the node carries no refs= in the book; checked against fr.wiktionary s.v. octopode and Etymonline s.v. octopus/octopod instead (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"fr.wiktionary\",\n              \"where\": \"fr.wiktionary.org/wiki/octopode\",\n              \"stance\": \"supports\",\n              \"note\": \"'Étymologie: Du grec ancien ὀκτώπους, oktṓpous.' Adjective 'qui a huit pieds ou huit pattes (Mollusque octopode)'; noun, an order of cephalopods.\"\n            },\n            {\n              \"src\": \"WEB/etymonline\",\n              \"where\": \"etymonline.com/word/octopus\",\n              \"stance\": \"supports\",\n              \"note\": \"'Octopod (1826): „eight-footed or eight-armed animal“, from the same Greek root' — dates the learned formation and confirms it is built on Greek ὀκτώπους, not on Latin octō.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"«اختاپوس»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian اختاپوس (oxtāpūs / axtāpūs) 'octopus' is certainly a modern European loan built on Greek ὀκτώπους, and Moʿin does carry the headword, so MON:164 is the right kind of place: the Farhang-e Fārsi entry reads simply 'اختاپوس (اُ) (اِ.) هشت‌پا' ('octopus: eight-foot'). But the immediate donor is doubtful. The Persian form ends in -پوس /-pūs/, which renders the Greek/Latin nominative -pous / -pūs (Latin octopus, and the Linnaean genus name Octopus), whereas French octopode would have given اکتوپد; and French does not in any case use octopode as the everyday name of the animal (that is poulpe or pieuvre) — it is an adjective and an order name. English Wiktionary accordingly derives اختاپوس directly from Ancient Greek ὀκτώπους with no French station at all. The online text of Moʿin, moreover, carries no origin tag for this word (abadis.ir shows the entry with no [فر.] mark), so Nourai's 'French octopode' link is not visibly his source's. Verdict: the Greek ancestry is certain, the French routing is unsupported and probably wrong — the word most likely came in through the scientific/Latin form octopus. Native Persian usage prefers the calque هشت‌پا, which is also how Moʿin defines it.\",\n          \"derivation_fa\": \"«اختاپوس» بی‌گمان وام‌واژه‌ای اروپایی و ساخته بر یونانیِ ὀκτώπους است و معین هم این سرواژه را دارد، پس ارجاعِ MON:164 از نوعِ درست است: مدخلِ فرهنگ معین چنین است: «اختاپوس (اُ) (اِ.) هشت‌پا». اما زبانِ واسطه مشکوک است. صورتِ فارسی به ‎-پوس‎ ختم می‌شود که برگردانِ حالتِ فاعلیِ یونانی/لاتینِ ‎-pous/-pūs‎ است (لاتین octopus و نامِ جنسِ علمیِ Octopus)، در حالی که از فرانسویِ octopode «اکتوپد» انتظار می‌رفت؛ به‌علاوه در فرانسوی نامِ روزمرهٔ این جانور poulpe یا pieuvre است و octopode صفت و نامِ راسته است. ویکی‌واژهٔ انگلیسی نیز «اختاپوس» را یکسر از یونانیِ باستان ὀκτώπους می‌گیرد و هیچ ایستگاهِ فرانسوی نمی‌آورد. متنِ برخطِ فرهنگ معین هم برای این واژه هیچ برچسبِ خاستگاه (مثلِ «[فر.]») ندارد. داوری: تبارِ یونانیِ واژه قطعی است، اما مسیرِ فرانسویِ نمودار پشتوانه ندارد و به احتمال زیاد نادرست است؛ واژه بیشتر از راهِ صورتِ علمی/لاتینِ octopus وارد شده است. در کاربردِ فارسی، گرته‌بردارِ «هشت‌پا» رایج‌تر است — همان‌که معین نیز به‌عنوان معنی آورده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D8%AE%D8%AA%D8%A7%D9%BE%D9%88%D8%B3\",\n            \"https://abadis.ir/fatofa/%D8%A7%D8%AE%D8%AA%D8%A7%D9%BE%D9%88%D8%B3/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:164\",\n              \"status\": \"partial\",\n              \"note\": \"the entry exists and is the right word, but not with the derivation the arrow needs: Moʿin's Farhang-e Fārsi s.v. اختاپوس (via abadis.ir, section فرهنگ معین) reads only '(اُ) (اِ.) هشت پا' — no origin tag, no French form. The 6-volume print page 164 could not be paged directly (no scan with that pagination on disk), and the 2-volume Adena text of Moʿin on disk does not contain the headword at all.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir/fatofa/اختاپوس (فرهنگ معین)\",\n              \"stance\": \"partial\",\n              \"note\": \"'(اُ) (اِ.) هشت پا.' — the word and its meaning, without any [فر.] or Latin-script etymon.\"\n            },\n            {\n              \"src\": \"en.wiktionary\",\n              \"where\": \"en.wiktionary.org/wiki/اختاپوس\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'The word derives from Ancient Greek ὀκτώπους (oktṓpous) … the more prevalent synonym in Persian is هشت‌پا' — Greek directly, no French intermediary.\"\n            },\n            {\n              \"src\": \"fr.wiktionary\",\n              \"where\": \"fr.wiktionary.org/wiki/octopode\",\n              \"stance\": \"partial\",\n              \"note\": \"French octopode is an adjective and an order name, not the ordinary French word for the animal; its shape (-ode < ὀκτώποδ-) does not match Persian -پوس.\"\n            },\n            {\n              \"src\": \"WEB/etymonline\",\n              \"where\": \"etymonline.com/word/octopus\",\n              \"stance\": \"partial\",\n              \"note\": \"'Latinized form of Greek oktōpous' — the Latinized nominative octopus is the shape Persian اختاپوس actually reflects.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"octô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin octō 'eight' is the regular reflex of *oḱtṓw, the PIE final *-ōw being reduced to -ō in Latin (Watkins: '2. Latin octō, eight: OCTANS, OCTANT, OCTAVE, OCTAVO, OCTET, OCTO-, OCTOBER, OCTONARY; OCTODECIMO, OCTOGENARIAN'). Pokorny 775 adds the derivatives that show the old diphthong: the ordinal octāvus < *octōuos (compare Oscan Uhtavis 'Octavius' and Old Phrygian otuwoi wetei 'in the 8th year' < *oḱtōuoi wetesi), octōgintā '80' (remodelled on septuāgintā), and octōdecim '18'. Klein p. 504 lists 'L. octō' among the cognates of eight. A pass-through node with no problems.\",\n          \"derivation_fa\": \"لاتینِ octō «هشت» بازتابِ قاعده‌مندِ *oḱtṓw است و پایانهٔ ‎*-ōw‎ هندواروپایی در لاتین به ‎-ō‎ ساده شده است (واتکینز: «۲. لاتین octō، هشت: OCTANS، OCTANT، OCTAVE، OCTAVO، OCTO-، OCTOBER …»). پوکورنی در صفحهٔ ۷۷۵ مشتق‌هایی را می‌آورد که دیفتونگِ کهن را نشان می‌دهند: ترتیبیِ octāvus از ‎*octōuos‎ (بسنجید با اسکیِ Uhtavis «اوکتاویوس» و فریگیِ کهنِ otuwoi wetei «در سال هشتم»)، octōgintā «هشتاد» (به قیاسِ septuāgintā بازسازی‌شده) و octōdecim «هجده». کلاین (ص ۵۰۴) هم «L. octō» را در شمار هم‌ریشه‌های eight آورده است. این گره واسطه است و اشکالی ندارد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/o%E1%B8%B1t%E1%B9%93w\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. oktō(u): '2. Latin octō, eight: OCTANS, OCTANT, OCTAVE, OCTAVO, OCTET, OCTO-, OCTOBER, OCTONARY; OCTODECIMO, OCTOGENARIAN.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p. 775\",\n              \"stance\": \"supports\",\n              \"note\": \"'Latin octō … ordinals: Latin octāvus (compare also Oscan Uhtavis „Oktavius“) probably from *octōuos … compare Latin octuāgintā „80“ … Latin octōdecim.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein p. 504 s.v. eight\",\n              \"stance\": \"supports\",\n              \"note\": \"'L. octō' listed among the cognates; 'Cp. also Rum. opt „eight“ (fr. L. octō), influenced in form by şapte „seven“.'\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. oktou\",\n              \"stance\": \"supports\",\n              \"note\": \"'Lat. octō … (Lat. octōnī „eight each“)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"October, octagon, octave\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are learned loans, not inherited words, and all three come in through Latin as the chart draws. October < Latin Octōber (mēnsis), literally 'the eighth month' — of the old Roman year that began in March (Klein s.v. October: 'L. October (mensis), lit. „the eighth month (of the Roman year)“, fr. octō, „eight“; cp. September, November, December'). Octave < Old French/French octave < Latin octāva (diēs), feminine of octāvus 'eighth' (Skeat s.v. Octave: 'Lit. „eighth“; hence, eight days after a festival, eight tones in music. — F. octave … L. octāua, fem. of octāuus, eighth. L. octō, eight'); the musical sense is the interval spanning eight degrees. Octagon < Latin octagōnos, itself a borrowing of Greek ὀκτάγωνος 'eight-angled' (Klein s.v. octagon), so this one reaches English through Latin but with a Greek base — the Latin→English arrow is still the right route for the word as an English lexical item.\",\n          \"derivation_fa\": \"این سه واژه وام‌واژه‌های دانشورانه‌اند نه ارثی، و هر سه — چنان‌که نمودار کشیده — از راه لاتین به انگلیسی رسیده‌اند. October از لاتینِ Octōber (mēnsis) «ماه هشتم» است، یعنی هشتمین ماهِ سالِ رومیِ کهن که با ماه مارس آغاز می‌شد (کلاین ذیل October؛ بسنجید با September، November، December). Octave از فرانسویِ octave و آن از لاتینِ octāva (diēs)، مؤنثِ octāvus «هشتم» است (اسکیت ذیل Octave: «تحت‌اللفظی «هشتم»؛ از این‌رو هشت روز پس از یک عید، و هشت پردهٔ موسیقی») و معنای موسیقایی‌اش فاصلهٔ هشت‌درجه‌ای است. Octagon از لاتینِ octagōnos است که خود وام‌گیری از یونانیِ ὀκτάγωνος «هشت‌گوش» است (کلاین ذیل octagon)؛ پس این یکی از راه لاتین آمده اما پایه‌اش یونانی است. در مجموع ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"(none cited)\",\n              \"status\": \"not_checked\",\n              \"note\": \"the node carries no refs= in the book; checked against Klein s.vv. October/octagon (KLN_1966.txt lines 26027, 26048) and Skeat s.v. Octave (SKT.txt line ~12610) instead (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. October, octagon\",\n              \"stance\": \"supports\",\n              \"note\": \"'October, n. — L. October (mensis), lit. „the eighth month (of the Roman year)“, fr. octō, „eight“; see octa-. (The Roman year began with March; cp. September, November, December).' / 'octagon, n., a plain figure with eight angles and eight sides — L. octagōnos, fr. Gk. ὀκτάγωνος, „eight-angled“.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Octave\",\n              \"stance\": \"supports\",\n              \"note\": \"'Octave. (F.-L.-Gk.) Lit. „eighth“; hence, eight days after a festival, eight tones in music. — F. octave, an octave (Cot.). — L. octaua, fem. of octauus, eighth. — L. octō, eight (Gk. ὀκτώ, eight: cognate with E. Eight).'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, s.v. oktō(u), Latin branch\",\n              \"stance\": \"supports\",\n              \"note\": \"'2. Latin octō, eight: … OCTAVE, OCTAVO, OCTET, OCTO-, OCTOBER, OCTONARY' — Watkins puts OCTAVE and OCTOBER on the Latin branch, exactly as the chart does; his index lists 'OCTAVE oktō(u)', 'OCTOBER oktō(u)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"astâu : eight\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit अष्टौ aṣṭāu (beside अष्ट aṣṭa) 'eight' — Nourai's 'astâu' with the retroflexion left unmarked. It is the single most important witness for the reconstruction, because its dual-looking ending is what licenses PIE *oḱtṓw as an old dual ('two tetrads'): Pokorny 775 'Old Indic aṣṭa, aṣṭau (besides aśītí- „eighty“)'; Klein p. 504 'cogn. with OI. aṣṭā, aṣṭāu … All these words prob. derive fr. I.-E. *oktō(u), an old dual form, orig. meaning „twice four“'; Mann, 'Skt. aṣṭāu, aṣṭá (perh. „2 tetrads“, MacDonell)'. Phonetically Indo-Aryan aṣṭ- from *oḱt- shows *o > a and the regular Indic *ḱt > ṣṭ. Nourai's cited source, Davies' Roots (DVS:130), could not be consulted.\",\n          \"derivation_fa\": \"سنسکریتِ अष्टौ (aṣṭāu) در کنارِ अष्ट (aṣṭa) «هشت» — همان است که نورایی «astâu» نوشته و نشانهٔ واکِ کامی‌ـکاکلی (retroflex) را نگذاشته است. این صورت مهم‌ترین گواهِ بازسازی است، زیرا پایانهٔ دوگانه‌نمای آن است که اجازه می‌دهد *oḱtṓw را دوگانهٔ کهن («دو چهارگانه») بدانیم: پوکورنی ص ۷۷۵ «هندیِ باستان aṣṭa، aṣṭau (در کنارِ aśītí- «هشتاد»)»؛ کلاین ص ۵۰۴ «هم‌ریشه با aṣṭā، aṣṭāu هندیِ باستان … همهٔ این واژه‌ها به احتمال از هندواروپاییِ ‎*oktō(u)‎، صورتِ دوگانهٔ کهن به معنیِ «دو بار چهار»، می‌آیند»؛ مان: «سنسکریت aṣṭāu، aṣṭá (شاید «۲ چهارگانه»، مکدانل)». از نظر آوایی aṣṭ- هندوآریایی از ‎*oḱt-‎ با تبدیلِ ‎*o‎ به a و دگرگونیِ قاعده‌مندِ ‎*ḱt‎ به ṣṭ در هندی به‌دست آمده است. منبعِ خودِ نورایی (DVS:130) در دسترس نبود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/o%E1%B8%B1t%E1%B9%93w\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"DVS:130\",\n              \"status\": \"not_checked\",\n              \"note\": \"P. Davies, Roots: Family Histories of Familiar Words (1981) is lending-only on archive.org and has no OCR text on disk (refs_online.json: 'RE-SEARCH 2026-09: borrowable only', local_file null), so p. 130 could not be read.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p. 775\",\n              \"stance\": \"supports\",\n              \"note\": \"'Material: Old Indic aṣṭa, aṣṭau (besides aśītí- „eighty“)' — first item under the root.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein p. 504 s.v. eight\",\n              \"stance\": \"supports\",\n              \"note\": \"'cogn. with OI. aṣṭā, aṣṭāu, Avestic ashta … All these words prob. derive fr. I.-E. *oktō(u), an old dual form.'\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. oktou\",\n              \"stance\": \"supports\",\n              \"note\": \"'Skt. aṣṭāu, aṣṭá (perh. „2 tetrads“, MacDonell)' — the very form of the node.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur p. 521 s.v. هشت\",\n              \"stance\": \"supports\",\n              \"note\": \"'سانسکریت (SANSKRIT): AṢṬAU, AṢṬĀ' listed beside Avestan AŠTA and Pahlavi HAŠT.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-07T20:36:16.037Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-372.json (file state is current in your context — no need to Read it back)
```


## [2026-09-07T20:36:19.405Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-372.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 372"
}
```


### [2026-09-07T20:36:21.104Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'plausible': 3, 'confirmed': 9}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 11, 'partial': 2, 'not_found': 1, 'not_checked': 4}
books consulted: {'supports': 32, 'partial': 6, 'silent': 4, 'contradicts': 1} | by book: {'IEC': 6, 'KLN': 6, 'ARY': 4, 'POK': 4, 'MON': 3, 'SKT': 3, 'BRT': 2, 'PHD': 2, 'NYB': 2, 'AHD': 2, 'fr.wiktionary': 2, 'WEB/etymonline': 2, 'HRN': 1, 'WLD': 1, 'HUB': 1, 'KNT': 1, 'en.wiktionary': 1}
```


## [2026-09-07T20:36:45.558Z] AGENT

Done. `python3 tools/verify_check.py 372` → 12/12 nodes, 0 PROBLEM lines.

**Page 372 (book p. 342)** — 2 non-redirect entries (Oies, Okto); `Obhi` and `Oi-no` are redirects, skipped.

- Root verdicts: 2 confirmed. Node verdicts: 9 confirmed, 3 plausible, 0 disputed/transcription_suspect.
- Ref checks: 11 supports, 2 partial, 1 not_found, 4 not_checked (nodes with no `refs=`, plus DVS which is lending-only).

Plausible items (with reasons):
- **Oies #1 Avestan `aeša 2`** — route is Buck's (SYN p. 496: "Av. aēša-, NPers. xēš prob. : Skt. īṣā- … (Walde-P. 1.167, without aēša-). Barth. 32."), but the gloss is wrong: aēša- means *plough* (Vd. 14.10; Horn 515), while "pole/plow shaft" belongs to the ā-stem (Skt. īṣā, Gk. oiēion, Mann's *oisa).
- **Oies #2 Persian `xîš 2` / `xîškâr`** — core chain confirmed independently (Horn 114 no. 515; Hübschmann §162 "xēs … = zd. aēsa-", prothetic x-; Moʿin's Borhan footnote citing Horn 515). Two problems: the gloss (خیش = plough, not pole) and the variant «خویش ۲ / خویشکار ۲» — Borhan p. ~802 does print خویشکار "برزیگر و مزارع", but Horn's own footnote to no. 514 says flatly "ein np. xʷēš 'Pflug' statt xēš (No. 515) giebt es nicht"; the xʷ- forms belong to خویش "own" (MP xwēškār "dutiful").
- **Okto #7 Persian «اختاپوس»** — Greek ancestry certain and Moʿin has the headword ("(اُ) (اِ.) هشت پا"), but the French `octopode` routing is unsupported: -پوس reflects Greek/Latin -pous/-pus (sci. *Octopus*), not French -ode; en.wiktionary derives it straight from ὀκτώπους and Moʿin's online text carries no [فر.] tag.

Notes for the owner:
- **Nourai misprint (book, not extraction): `BQT:2238`** on the Persian `hašt` node. p. 2238 of the Amir Kabir reprint carries the نیو… entries; the هشت / هشتاد / هشتده entries with Moʿin's footnotes are on **p. 2338** (which supports the arrow verbatim). The printed page reads 2238 — page image saved to `data/verification/sources/refs/ocr/BOOK/372.png`.
- **Extraction error to fix**: in `data/extracted/batch/page-372.json`, entry 1 node #2 `quote.text` reads "…توانگر کنم مردم **خویش** کار"; the printed page (600 dpi crop checked) shows "…توانگر کنم مردم **خیش** کار" — no wāw. The `words` fields themselves are faithful («خیش ، خویش ۲», «خیشکار ، خویشکار ۲» both verified on the image).
- Also recorded: Pokorny 1959 **dropped** WP's `oies-` headword entirely (nothing between `oiu̯ā` p. 774 and `ok-` p. 774), so the root survives only in WLD I 167 + Mann; and Kent has no Old Persian numeral "eight", so the "/ Old Persian" half of node #1's label is Platts's inference.
