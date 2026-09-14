# Verification process log — verify-page-390


## [2026-09-14T00:49:29.983Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 390 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-390.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-390.json. Write /home/sfmqrb/git/rishe/data/verification/page-390.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 390` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:49:31.063Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:49:31.889Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:49:31.904Z] TOOL RESULT

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


## [2026-09-14T00:49:32.390Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-390.txt"
}
```


### [2026-09-14T00:49:32.411Z] TOOL RESULT

```
1	=== PDF page 390 (book page 360) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pel 2, Porkwos : pale, gray; bright, clean, pure  (refs POK:804; IEC:977)
4	#1 (parent #0) [Avestan] refs=POK:807 | pouruša, parya : gray, old
5	  #2 (parent #1) [Persian] refs=BQT:436 | pîr «پیر» : old, aged, spiritual leader
6	#3 (parent #0) [Persian] refs=MON:653; IEC:977 | pârsâ «پارسا» : chaste | extra: پارسای
7	#4 (parent #0) [Sanskrit] refs=IEC:978 | parŭsah : colorful
8	#5 (parent #0) [Latin] refs=AHD | pallěre : to be pale ; falcô : gray bird
9	  #6 (parent #5) [English] refs=AHD | pale, appall ; falcon
10	--- entry 1 ---
11	ROOT [Indo-European] Pel 3 : dust, flour  (refs POK:802)
12	#1 (parent #0) [Latin] refs=AHD | pulvis, pollen : dust
13	  #2 (parent #1) [French] refs=AHD:1024 | poudre : dust, powder
14	    #3 (parent #2) [Persian] refs=MON:827 | poůdr «پودر» : powder
15	    #4 (parent #2) [Turkish] refs=BQT:216; TAD:6 | 
16	      #5 (parent #4) [Persian] refs=BQT:216 | bârůt «باروت» : gun powder
17	    #6 (parent #2) [English] refs=AHD | powder, pulverize
18	  #7 (parent #1) [English] refs=AHD | pollen
19	
```


## [2026-09-14T00:49:33.743Z] AGENT

I'll read the source JSON and reference infrastructure.


## [2026-09-14T00:49:35.147Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-390.json",
 "description": "Read page 390 source JSON"
}
```


### [2026-09-14T00:49:35.195Z] TOOL RESULT

```
{
  "pdf_page": 390,
  "book_page": 360,
  "entries": [
    {
      "root": {
        "name": "Pel 2, Porkwos",
        "lang": "Indo-European",
        "refs": "POK:804; IEC:977",
        "gloss": "pale, gray; bright, clean, pure"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:807",
          "words": [
            {"translit": "pouruša, parya", "gloss": "gray, old", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:436",
          "words": [
            {"translit": "pîr", "gloss": "old, aged, spiritual leader", "script": "پیر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بندۀ پیر خراباتم که لطفش دایم است - ورنه لطف شیخ وزاهد گاه هست وگاه نیست",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:653; IEC:977",
          "words": [
            {"translit": "pârsâ", "gloss": "chaste", "script": "پارسا"}
          ],
          "script_extra": "پارسای",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:978",
          "words": [
            {"translit": "parŭsah", "gloss": "colorful", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "pallěre", "gloss": "to be pale", "script": null},
            {"translit": "falcô", "gloss": "gray bird", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "pale, appall", "gloss": null, "script": null},
            {"translit": "falcon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Pel 3",
        "lang": "Indo-European",
        "refs": "POK:802",
        "gloss": "dust, flour"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "pulvis, pollen", "gloss": "dust", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "French",
          "refs": "AHD:1024",
          "words": [
            {"translit": "poudre", "gloss": "dust, powder", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:827",
          "words": [
            {"translit": "poůdr", "gloss": "powder", "script": "پودر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Turkish",
          "refs": "BQT:216; TAD:6",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:216",
          "words": [
            {"translit": "bârůt", "gloss": "gun powder", "script": "باروت"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "powder, pulverize", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 1,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "pollen", "gloss": null, "script": null}
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


## [2026-09-14T00:49:37.531Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','BQT','MON','AHD','TAD','WLD','HRN','HUB','PHD','NYB','BRT','KLN','SKT','TTS','LKT','ARY','CHEUNG','SYN']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Check reference metadata"
}
```


### [2026-09-14T00:49:38.637Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG MISSING
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
```


## [2026-09-14T00:49:43.839Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','AHD','TAD','BQT','MON','ARY','SYN','WLD']:\n    v=d[k]\n    print('===',k)\n    for f in ['local_file','page_offset','lookup_hint','scans','cites']:\n        if f in v: print('  ',f,':',str(v[f])[:500])\n\"; ls data/verification/sources/refs/ | head -60"
}
```


## [2026-09-14T00:49:44.433Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T00:49:45.044Z] TOOL RESULT

```
=== POK
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?bas
   cites : page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)
=== IEC
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
   cites : column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)
=== AHD
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New Colleg
   cites : page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)
=== TAD
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt']
   page_offset : 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
   lookup_hint : Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
=== BQT
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, 
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag
   scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds a
   cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
=== MON
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incom
   page_offset : None
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden
   cites : page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)
=== ARY
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
   page_offset : printed page = pdf page + 1
   lookup_hint : Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image
   scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt'}]
=== SYN
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
   cites : page number of Buck, A Dictionary of Selected Synonyms (1949)
=== WLD
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/veri
   page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
   lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
   cites : volume (WLD1 / WLD2) and page of Walde–Pokorny
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
```


### [2026-09-14T00:49:45.088Z] TOOL RESULT

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


## [2026-09-14T00:49:49.483Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 80[0-9]\" POK_full.txt | head -40"
}
```


### [2026-09-14T00:49:49.573Z] TOOL RESULT

```
65651:Page(s): 805-807 
65671:Page(s): 807 
65705:Page(s): 807, 850 
65903:Page(s): 801-802 
65942:Page(s): 802 
65978:Page(s): 802-803 
66016:Page(s): 803-804 
66035:Page(s): 804 
66054:Page(s): 804 
66120:Page(s): 804-805 
66142:Page(s): 805 
66154:Page(s): 807 
66193:Page(s): 808 
66215:Page(s): 807 
66248:Page(s): 807-808 
66299:Page(s): 808-809 
66629:Page(s): 809-810
```


## [2026-09-14T00:49:50.330Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: pel\" POK_full.txt | head -30; echo ---; grep -n \"lemma: pork\" POK_full.txt | head"
}
```


### [2026-09-14T00:49:50.429Z] TOOL RESULT

```
65653:Root / lemma: peli-s- pel-s- 
65707:Root / lemma: pel-1, pela-, ple- 
65713:Root/ lemma: pel-1, pels-, ple-\ full, to fill; to pour; town (?), derived from a prefixed pe- + 
65870:Root / lemma: pel-2a, pelQ- : pla- 
65905:Root / lemma: pel-2b, pel-en-, pel-t-, pel-u- 
65944:Root / lemma: pel-3a 
65980:Root / lemma: pel-3b, pela- ple- 
66037:Root / lemma: pel-5 
66056:Root / lemma: pel-6 
66144:Root / lemma: pelpo- or polpo- 
67957:lemma: pel-2a, pela- : pla- : to cause to move, drive, felt. 
---
```


## [2026-09-14T00:50:01.982Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '66030,66075p' POK_full.txt"
}
```


### [2026-09-14T00:50:02.038Z] TOOL RESULT

```
References: WP. II 56 f., WH. II 278; 

See also: perhaps to pel-4an6 pel-Sas originally " container from skin'. 

Page(s): 804 

Root / lemma: pel-5 

Meaning: to sell; to make money 

Material: Gr. nwAsTv " sell ', Doric nwAa:, Attic (Gramm.) nu)Ar| f. "sale'; Old High German 

/^//"verkauflich, fell' {*pello-). Old Icelandic fair 6s. {*polo-)\ Old High German felli. Middle 

Low German velle. Old Frisian /e/"feir are not related; 



Lithuanian pelnas^ earnings, pay', pelnau, -ytr earn ', pe/c/et/" spare' , Latvian pe'lns, 
pel'na^ earnings, Gewinst', pe'lnTV earn, gain, verschulden'. Old Church Slavic /0/e/7b, 
russ. yOo/o/7 'booty'. 

References: WP. II 51, Trautmann 213. 
Page(s): 804 

Root / lemma: pel-6 

Meaning: grey; pale 

Material: Old Indie pa///a-, fern. paliknT{irom *-tn/} ' aged-gray, greis' (: nzKnyoq), parusa-' 

marked, stained ' = Avestan pourusa-, paourusa-^qray, old'; pers. pur^qray' {*parya-)\ 

Armenian alik'^6\e (weiften) waves, billows; white Bart, weiftes hair' {*pllio-)\ 

gr. Tr£AiTv6(; "gray' (for *tt£Ait6(; = Old Indie pa//ta-h after dem Fem. *Tr£AiTvia = Old Indie 
paliknl); Ionian n£Ai5v6q out of it after |jaK£5v6c; etc. reshaped; n£Ai6q ( *peli-uo-) "farblos, 
pallid, grauschwarz, bluish black' (here the PN DeAoijj), irzKKbc, ds. (*n£Aj6(;? *n£Av6(;?), 
noAioc; "gray, greis' ( *poli-uo-), niAvov cpaiov Kurrpioi Hes.; n£A£ia, n£A£iaq "wild dove' 
(named after the color, compare n£A£iai, n£A£ia5£(;, actually die graukopfigen, old, as 
appellation of the Priesterinnen in Dodona as well as tt£A£ioc; "age' Hes.; also Latin 
palumbes. Old Prussian poa//s'6ove'), TTzkap\/6q "swan' ("the schwarzweifte'); from 
*n£AaF(o)- + apyo^; maked. n£AAr|c; "T£(ppu)5r|<;' Hes.; probably here also nr|A6c;, Doric 
TTakoq {*-naKa6q) " loam, clay, slime, mud, ordure, morass';
```


## [2026-09-14T00:50:02.562Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '66145,66260p' POK_full.txt"
}
```


### [2026-09-14T00:50:02.678Z] TOOL RESULT

```
Meaning: woodwork 

Material: Old Indie parpa- (Lex.) ' bench orWagelchen for cripple and Fuftlahme', parpa-m 

(Lex.) "house' ("Bretterbude'), Latin yC>^/yO//^/r7"Brettergerust as stage or Tribune'. 

References: WP. II 66. 

Page(s): 807 

Root / lemma: penk^e 
Meaning: five 

Material: A. Old Indie panca, Avestan panda; Armenian hing, gr. ttsvte, Aeolic -nt\mz\ 
nspna^siv "an den 5 Fingern zahlen' (: bret. pempat'd'\e Garben [to 5] fold, plait, fold up, 
merge '); alb. pese, Geg p§se {*perjk"tia)\ LaWnquFnque {Faiter quTn(c)tus), Oscan-Umbrian 
*yOO/r7yC>e (compare Oscan pumperias, Umbrian pumpenas 'quincuriae); Old Irish coic, 
acymr. pimp, mcymr. nc. pump, corn, pymp, bret. pemp, gall. nspnsSouAa "nsvracpuAAov'; 
Gothic fimf. Old Icelandic fimm. Old High German fimf, finf. Old Saxon Old English fff 
(schwab. fuchze 15 after sechze; das ^ these forms as well as Old High German funf, 
funfzich and of Ord. Old High German funfto point at not auf Indo Germanic n); Lithuanian 
pe/7/r/ (inflectional); Old Church Slavic yO^/i. 5 (/from /r/ after dem ordinals; originally 
collective = Old Indie /Oa/7/r//-"Funfzahr, Old Icelandic fimti. "number from fijnf; also 
Umbrian puntes if "quiniones'); Tocharian A pen, B pis, here.-Hittite pa"ta. 

B. 15: Old \n6\c parJca-dasaf, Avestan pancadasa, Armenian hnge-tasan, gr. 
n£VT£(Kai)5£Ka, Gothic fimftaihun. Old High German finfzeiian. 

C. 50: paHcasat, Avestan pancasat, Armenian yisun (from *iiingisun), gr. nsviriKOVTa, 
Latin quinquaginta {aiter quadraginta). Old Irish coTco {\n\Vc\ diphthong). 

D. ordinals penk'ios:0\6 Indie paktiia-, Avestan pux5a- (after *kturtiia " the fourth ', 
compare pai7/a/7Ka-"Funfter); gr. n£pnTO(;, Latin quTntus, Oscan *yC>c»/7/c»5 (compare above 
Puntiis, V\o\xu\zc„ Paelignian Ponties 'Quinctius'= Latin Quinctius, also Oscan pomptis 
"quinquies'; -/77- after dem Kardinale, as also das /7from Quinctius and quinctus); Old High 
German fimfto, finfto. Old Saxon fffto. Old Icelandic fim{m)ti, Gothic (in compound) fimfta-, 
Lithuanian penktas. Old Bulgarian p§tb, Tocharian A pant, B pinkce; *penk''etos:0\6 Indie 
pancattia- {qe^'6\\y\\\c\\ex pancama- aiiex saptama-), alb. ipesete, ipeste, gall, pinpetos. 
Old Irish coiced, acymr. pimpiiet eic; with A-forms Armenian iiinger-ord^\he fijnfte'; 



compare perhaps Old Irish co/cer' number from fijnf and Gothic f/ggrs, Old Icelandic f/ngr, 
Old English f/nger, Old High German Old Saxon f/'ngar l\r\ger' {*f/nj"'raz, Indo Germanic 
*penk"'rds). 

References: WP. II 25 f., WH. II 407 f., Trautmann 213 f. 
Page(s): 808 

Root / lemma: pen-1 

Meaning: to feed 

Material: Latin penus, -orisn. and penus, -usm. "Mundvorraf, also "the interior of Hauses' 

(where die Lebensmittel aufbewahrt become); /Oe/7es (solidified Lok.) preposition with Akk. 

"by'; penitus^ {irom) inside, deep, grijndlich' {*pene-to-)\ in addition (after intus: intro) 

penetro, -^/"e "penetrate'; Penates "die Gotter in the interior of Hauses'; perhaps Gothic 

fenea {*finja) "Gerstenspeise'; Lithuanian penu, penef/lee6, fatten, overfeed ', Latvian 

yOe/7e/"verwohnen', Lithuanian penasloo6'. 

References: WP. II 25, WH. II 280 ff., 283, E.-M.2 753 f., Trautmann 214; 

See also: perhaps to pa- "feed'. 

Page(s): 807 

Root / lemma: pen-2, pen-ko- 

Meaning: swamp; water, wet 

Material: Middle Irish en{*peno-?) "water', e'/75c/7 "swamp, marsh', en-g/as '\Nasser'\ge 

milk', cymr. en-wyn' buttermilk'. Middle Irish c»/7-c/7j"Fischotter' ("Wasserhund'), FIN On, 

PN 0/7ac/7 ("swamp, marsh'), Celtic FIN "Evoc;, newer *En/os '\r\r\', gall. FIN *Ona'r'\yer', 

also as suffix (^e'i6'/'c»A7/75"Biberbach' etc.); zero grade Middle Irish ani. " water, urine ', 

gall, anom^ paludem '; 

Gothic fanir\. "slime, mud'. Old Icelandic fenr\. "swamp, marsh'. Old High German 
fenna, fenmi.. Middle High German venner\., Old Saxon fen/n. 6s., Middle Low German 
vennei. "moorige willow ', Old English fennm. n. "swamp, marsh, moor, fen', wherefore 
changing through ablaut Old English fyne^ dampness ', fynig^ moldy ' 
Maybe alb. finje^ soapwater, soap suds'. 

mnl. vunsc. Middle Dutch K^/7s"muffig'; Old Prussian pannean^Uoorbruch' (= Germanic 
*fanja-), Lithuanian paniabude^H\eger\'^\\z\ Latvian panei. "Jauche'; also lllyrian 
Pannonia. (under the influence of common Celtic -ns-, -nt- > -nn-). 

With Ao-formants: Old Indie y05/7/r5-m. n. "slime, mud, ordure, swamp, marsh'; Middle 
Irish e/ic/7e "salmon' {*penk-TnJo-); zero grade -/^/^oderivative *furjxW)3-'\r\ Old High 
German fuht, fuhti. Old English /&/?/ "humid, wet'. 



References: WP. II 5 f., Trautmann 205, Pokorny BzNF 2, 37 f. 
Page(s): 807-808 

Root / lemma: pent- 

Meaning: to go, walk; way 

Note: (in Aryan with //?) 

Material: Old Indie panthah (= Avestan panti), Akk. Sg. pantham (= pantqm), and 

panthanam {= Avestan pantansm), Instr. Sg. patha{= pa^a); /-stem in Instr. PI. pathibhih 

(Avestan padsbTS), Old pers. Akk. Sg. pa^/'m; Avesian panta a\so 'room, place', as in
```


## [2026-09-14T00:50:12.874Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '66075,66145p' POK_full.txt"
}
```


### [2026-09-14T00:50:12.942Z] TOOL RESULT

```
Latin palled, -ere "pale, wan sein', yC>5//c»/'"paleness', pallidas 'pa\e, wan' (at first from 
*paluos, older *poluos= Germanic falwa-, Lithuanian palvas. Old Church Slavic yO/ai/b); 
pullus 'sch\Narzgrau' (^/fromyinfolge of aniaut. p-; forms -no-); palumbes or -/5"wood-, 
dove, wood pigeon' ( *pelon-b^o-7 rather parallel formation to columbus, -a, see above S. 
547); 

Note: 

Alb. {*palumb) pellumb^ diOve' shares the same root with Latin palumbes -is, m. and f. "a 
wood pigeon, ring dove'. It is not a Latin loanword otherwise the ending -es, -/Jswould have 
been solidified in alb. like Latin radius> alb. rreze^ra\f\ actually Latin could have borrowed 
this cognate from lllyrian since the shift m > mb\s a typical alb. not Latin. 

alb. plak^ graybeard, Altester'; 



Middle Irish Hath, cymr. (etc.) //wyd'gray' (from *pleito-, compare Old Indie /7a///a- gr. 
nsAiTvoc;); 

Germanic *falwa- in Old Icelandic fglr. Old English fealo. Old Saxon falu. Old High 
German falo, fa/awer^sa\\o\i\/, paled, dun-colored, light grayish brown ' (in addition as 
"graue ash' Old Icelandic fg/sk/m., Old High German fa/aw/ska 'ash, Aschenstaubchen'); 
*falha-{: Lithuanian palsas) in aleman.- Rhein Franconian falch' dun-colored, light grayish 
brown, esp. from hellbraunem cattle'; *fela- or *felwa-\v\ westfal. f^r dun-colored, light 
grayish brown ', fgle 'fahles roe deer, fahles horse'; with dem Germanic /r-forms as in other 
bird name here presumably Old High German (etc.) /^/co 'falcon' (late Latin falco^rom 
dem Germanic); 

Lithuanian yoa/i/as'blaftgelb' (= Germanic *falwa, Latin palli-dus) = Old Bulgarian p/avb 
"white', Serb. p/uv'b\on6, blue'; Lithuanian pe/e' mouse ', Latvian pe/eds.. Old Prussian 
pelesP\. ' mouse (= Armmuskel)', Old Prussian pe/e "consecration'; as derivative from 
pele' mouse ' also Lithuanian pelekas, Latvian pe/e/rs "mausfarbig, sallow, paled, gray'; 
Lithuanian peleda, Latvian pgleda'o\N\ ' ("Mausefresserin'); from a *pele' mildew ' derives 
U\h\}av\\av\pele-ju, -ti" mildew ', pelesiaiP\. " mildew ' and in ab\a\}\. plek-stu, -ti" mildew, 
modern'; in ablaut Lithuanian pilkas'^raY, /Oe//re"Moorbruch', a\so palsas, Latvian paiss 
"sallow, paled' ( *polRos) as well as Old Prussian poa//s'doye' {*pdlis); Slavic *plesnb in 
russ.-Church Slavic plesnt. Old Czech plesen' mildew ' and Church Slavic /0e/e5"pullus', 
russ. pe/esjy" mottled, speckled, *tabby, varicolored'; das forms Indo Germanic -so- or -ko- 



References: WP. II 53 f., WH. II 239 f., 242, 386, Trautmann 205, 212; 
See also: see above S. 799 C {pel-1). 
Page(s): 804-805 

Root / lemma: {pel-9), pol- pie- plo- 

Meaning: to burn, be warm 

Note: also with -£/o- extended; perhaps = (s)p(h)el-'q\eavc\, shimmer' 

Material: Old Icelandic flor {*fld-wa-) "lukewarm, warm'; Dutch f/ouwla\nt, languid, 

lukewarm'. Modern High German flau {*ple-uo-); Old Church Slavic yoo^ip, /7C»/e//"burn' intr., 

causative pa//t/"burn' tr., vbs-p/anetb sg "KaTacpAsynasTai', plamy, plamenb m. "flame' 

( *polmen-); whether here Lithuanian plenys above S. 802? 

in addition probably cymr. ^c»-/ei/ "light', bret. gou-louds. {*plo-uo-); different Lewis- 
Pedersen 29 (to GN Lugus), compare above S. 690. 



References: WP. II 59 f., Trautmann 212 f., J. Loth RC. 36, 157. 
Page(s): 805 

Root / lemma: pelpo- or polpo-
```


## [2026-09-14T00:50:13.460Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '65900,65985p' POK_full.txt"
}
```


### [2026-09-14T00:50:13.544Z] TOOL RESULT

```
See also: hieher probably also /oe/-J"meal, flour'. 

Page(s): 801-802 

Root / lemma: pel-2b, pel-en-, pel-t-, pel-u- 
Meaning: powder, flour 



Material: Old \nd'\c pa/a/a- n. "ground, pulverized seeds, porridge, mash, smut'; gr. iraAri 
"dust, powder', nai-TiaAri, noi-anaAr| " fine flour'; naAuvw "bestreue'; Latin pa/eat "chaff, 
straw, grain husk '; 
Maybe in -/77-formant alb. i*pa/-) pja/m ' poWen' . 

with Mormants: TToKioq "porridge, mash from meal, flour', Demin. TToAiiov, noAiapiov; 
Latin pu/s, -tis " thick mash of spelt flour ' {* polios); Middle Irish littiu (Gen. litten), nir. lite, 
cymr. Illth (/instead of y after llith "bait') " flour soup, any thing eaten with bread, a sauce, 
condiment, relish (fruit, vegetables, salt, etc.), food ' {*plt-\ with expressive Gemination); 

with i/-formants: Latin pulvis, -e/7s"dust, powder' {*polui-\ inflection after cinis); gall, 
(rom.) *ulvos(^s.\ 

Maybe truncated alb. Geg {*pluvlni) pluhunl'dust, powder' < Sardinian Campidanesu 
pruini: Sicilian pruvulazzu < Latin pulvis, -e/75"dust, powder'. 

here (Indo Germanic *pel6us, pelu-6s) Old Indie m. PI. pa/ai/as "chaff', Balto-Slavic 
*pelu-av\6 *pelua-\. "chaff in Lithuanian pelusi. PI., Latvian pelus, pelavasi. PI. ds.. Old 
Prussian pelwoi. and Latvian pelvast PI. ds.; Old Church Slavic yO/eK/f. PI. "axupov', kir. 
polova ds. etc.; 

with /^formants: Latin pollen, -//7/s"very fine flour, dust powder ' (//from n. equalization 
in inflection *polen, *poines)\ polientai. "Gerstengraupen'; here also Old Prussian pelanne 
f. "ash', Lithuanian pelenaTrw. PI., Latvian p^lni ds., wherefore Old Prussian pelannoi. 
"stove, hearth', Lithuanian peiene^stove, hearth'; Old Prussian plieynis^ ash powder ', 
Lithuanian plenysi. PI. " Flockasche ', Latvian plene'\i\/\r\\te ash on coal '; s. S. 805; 

without /^forms, but with Redupl. russ. pepel. Old Church Slavic etc. popelh "ash', am 
ehesten as "crushed, ground, broken into fine particles' to pel-2a^ pellens, pultare '. 

References: WP. II 60, WH. II 331, 388, Trautmann 212 f., 225; 
See also: probably to pe/-i'"bump, poke'. 
Page(s): 802 

Root / lemma: pel-3a 

Meaning: to fold 

Material: a. pio-as 2. composition part in Adj. as gr. a-irAoq "simple, just', 5i-ttA6(;, SirrAa^ " 

twofold ' (compare Armenian /7a/ "Mai'), Latin simplus, duplus, duplex, triplus, triplex ^eiu-, 

two-, dreifach', Umbrian dupla^ double, twice as large, twice as much ', tuplakkVk. Sg. n. 



'duplicem', //7p/e/'"triplis'; Middle Irish c/fabu/' doub\e' {*duei-plo-); Gothic twei-fis '6o\ib\.\ 
Old High German zi//7^/"dubious', m. "doubt', probably also Avestan bifra-v\. " comparison, 
Ahnlichkeit ', in Gr. besides die Umbildungen of type anAooc; (to nAouq) and Ionian 
5inAriaiO(;; further with older /-Ableitg. (see below) 5inAaaiO(;, Doric SinAarioq etc. "double, 
double so groft' ( *pJtio-, SinaAioc; " twofold ' from *5inAaT0(;). 

p. alb. pale {*pol-nS) " crease, row, yoke, pair'; gr. n£:nAo(; m. "Frauengewand'; Old 
Icelandic feli. {*falja-) "furrow, stripe, crease ', Norwegian felai. "Faltenmagen'. 

y. -to-nouns and verbs: Old Indie /Oi//5//"umhullt with', puta-m. n. " crease, TiJte, pouch ' 
( *pulta-). Middle Irish a//"junctura, artus' {a Redukt. from Indo Germanic o, as perhaps also 
Old \v\6\c puta-), redupl. strong. V. Gothic fa/f^anlaW, Old Icelandic fa/da' den Kopf cover 
', Old English fealdan, Old High German faltan^io\6\ weak. V Old Icelandic falda'io\6\ Old 
English fealdian. Old High German faltdn6s.. Old Icelandic faldrm. " crease, corner, tail, 
Kopfputz the Frau', feldrxw. {*faldi-) "mantle'. Middle High German valte^ crease, 
convolution, angle '; Gothic ain-falt^s. Old High German einfald, -/, Old Icelandic einfaldr. 
Old English 5/7/fea/c/" simple, just' 

References: WP. II 55 f., WH. I 383 f.; 

See also: perhaps identical with pel-3b and pel-4. 

Page(s): 802-803 

Root / lemma: pel-3b, pela- ple- 
Meaning: to cover, wrap; skin, hide; cloth 

Material: Gr. nsAaq "skin', £puai-TT£Aa(; "HautentziJndung', a-i^zKoc, "nicht verheilte wound'; 
TTeA|ja n. "Sohle am foot or shoe ', naApn " light shield' (*of skin), Latin paleai. "Lappchen 
am Hahnenschnabel', palearu. "Wampe, dewlap '; Old Frisian f/7mene 'sk\n', Old English
```


## [2026-09-14T00:50:31.457Z] TOOL CALL #13: Bash

```json
{
 "command": "pdftoppm -f 390 -l 390 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$SCRATCH/pg390\" 2>/dev/null; SCRATCH=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; pdftoppm -f 390 -l 390 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$SCRATCH/pg390\"; ls -la \"$SCRATCH\""
}
```


### [2026-09-14T00:50:33.071Z] TOOL RESULT

```
total 72
drwx------ 2 sfmqrb sfmqrb  4096 Sep 13 20:50 .
drwx------ 4 sfmqrb sfmqrb  4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   326 Sep 13 20:50 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 55136 Sep 13 20:50 pg390.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40 Sep 13 20:49 queue.txt
```


## [2026-09-14T00:50:33.190Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\n# leaf ~= p/2+15 ; p=977 -> leaf ~ 503\nfor n in (501,502,503,504):\n    print('=== leaf',n)\n    print(leaves[n][:2500])\nEOF"
}
```


### [2026-09-14T00:50:34.154Z] TOOL RESULT

```
858
=== leaf 501
mai, v. (2) “eat, feed myself, cf. aga-páo ("love'. See nnt- for the px.)
pàk- (1) ‘reverse, perverse, wrong, back- ward'. See opakos and next Skt. pakah ‘childish, silly’; Arm. hak-, haka-, px. fcounter-' beside hakem, v. ‘incline, bend’; Lat. cf. opacus (‘dark, thick, in the shade" ? but cf. op-, px); OCS pace, adv. “however, but; Srb. id. beside OCS & R paky “in re- verse, adversely; OCS pak-ostí, f. ‘harm’; OCz. ‘ailment, reverse, hardship’; Ukr. Srb. ‘malice’; R “dirt; Cz. pak ‘then’; Srb. “and, but, then’; pako, id.; Li. cf. pokštas ‘joke’; Ukr. pacytysja, v. ‘recede’
pàk- (2) ‘strike, stir. See paks- below Gk. cf. ptáx, gs: ptákos, adj. *timid', ptésso, v. ('terrify', fr. *d-pakio w. reduced px.?); Sio- vene pok ‘bang’; póka, f. & poč, f. “crack, split; (long-gde in) Cz. pácit, v. “force, force open’; Slovene pacditi, v. ‘destroy’. Uncertainly Du. vagen, weg-vagen, v. 'scatter, destroy, blot out. (For Ukr. pacytysja, v. ‘warp’: Arm.
901
hakem, v. ‘bend’, see påk- (1). The secondary mng. of Cz. páčit “calculate'; Slovak páčiť ‘evaluate’; páCit sa agree to, be pleased to’, though isophonic w. Lat. pax, etc. seems to be a variant with -k- for -K-)
pāksið “stir, move, strike’. Cf. pak- (2) OCS paso, paxati, v. tr. (1) “stir, move: Cz. pásu, páchat *commit'; R paxnuüt, inf. ‘sweep; blow'; Li. pok3iu, eti, v. ‘knock, strike, fire a gun, etc?
păk- ‘fix, tie, bind, join; bond, fixture, pact. Element of the following. WP II, 2-7. Cf. pák- (2) (note.) | Short grade in Av. pas-, v. ‘tie’; pasmom, n. ‘bond’; Arm. hasnim, v. (reach, arrive’, fr. *pak- or *pàaK-, as also) hasun ‘ripe’; hasuk ‘mature’; Gk. cf. ém-pax, gs: -pakos, m. 'guar- dian’; Lat. páciscor, v. ‘bargain’; forpex, gs: -picis, f. ‘tongs, scissors’; Go. fulla-fahjan, v. “serve, satisfy’ beside (oxytonic prototypes) OHG gi-fag, OE fzege ‘acceptable’; Go. fagrs “suitable; thankful); OHG fagar, MHG vager, ON fagr, OE fæger, Sw. fager (fair. Cf. E fair in all senses); cf. OE fægen (“joyfuP', E fain); Sw. fàgna, v. ‘cheer, entertain’; ON fagna ‘re- joice'; MHG vagen, v. ‘comply’. Cf. also MIr. acht, s. ‘stipulation’ (mod. ‘act < Lat.). Long grade in Skt. pasah, m. “bond, noose, fetter; pa$ayami, v. ‘tie’; Tokh. (?) pyakàs, pyāçi, s. ‘stake’; Arm. (*a or *à) has, i-st. (agreement, due, payment, rent’; hasu, adj. “happening; clever’; hast, adj. ‘firm’; Gk. pésso, adj: péktós, v. ‘fix’; cf. hór- péx, gs: -pékos (Doric: -à-), m. ‘sapling, branch, pole, javelin’; Lat. pàx, gs: pàcis, i-st. f. agreement, pea
=== leaf 502
Lat. pactus ‘bargained for, m. u-st. ‘pact, bargain’; MIr. acht ('sti- pulation". But mod. Ir. acht «act influenced by Lat. actus); Go. cf. fullafahjan, v. ‘satisfy, serve
pal- (1) (palos, a, io, pal'is) ‘bare, blank, pale; space, expanse'. WP II, 61 Hitt. palhis, adj. “broad”; Lat. cf. palam, pro- palam ‘openly’; pallidus (fpale', either a synth. cpd. or fr. *palni-) beside palleo, ere, v. *be pale’; Gallo-Lat. cf. al-auda ( lark'. For -auda see áued-, áuod-); Sw. fal- (in cpds. “clearing”, also in place-names Fal- *plain-. Here EIT). OCS polü, R polyj, adj. open, bare’; polje, n. (and com. Sl.) ‘field’; cf. R polaja vodà “high water": Li. pálios, fpl. “fen, marsh’; Latv. pali, mpl. ‘flooded fields (Uncertainly Arm. nvay “dark, obscure; ailing', fr. *ni-pal-? Lat. palüs, gs: palüdis, f. ‘marsh’ is perh. a cpd., cf. üd-, üdn-, üdər water), See next
(pàl- variant of above, q.v.) Arm. (ambig.) ayawt, Let ‘dim’; alik, pl. (2) “grey hair beside alevor, adj. 'grey-haired"; Latv. palums, m. “patch, space, gap'; pals “grey”
(paln-? variant of above, q. v. Gmc. ambig. Cf. poluos) Lat. palleo, ére, v. ‘turn pale’; Icel. cf. fólna, intr. (fade, turn pale fr. *palnuo?); beside fölur, acc. fólvan, adj. (pale. Ambig. cf. po- luos); Cz. planý ‘empty, wild; fruitless’; na plano “in vain'; pláü, f. “plain, wold'; Pol. plonny ‘barren’; ptoh, f. as Cz.
pal- (2) ‘straw, chaff. Skt. ambig. Cf. pelos Skt. palah, m. id.; Lat. palea, f. ‘chaff; R cf.
903
pàlevyj, adj. ‘straw coloured" (*-a-)
pål- (3) ‘stake, post (Lat. palus, gs: -1, m. id. is from a type *pag(s)- lo-, cf. ala, mala, velum, and the dimin. forms in -xill-); Ukr. cf. palyk, m. dim. id.; OCS, R. palüka, pàlka, f. ‘stick beside OCS & R pàlica, id.; Srb. palije, fpl. ‘joists, roof-tim- bers'; Li. põlis, gs: -io, m. ('stake', if not fr. Gmc. Pfahl, a Lat. LW); Latv. palis, m. id. Short vowel in R. Cz. poléno, poleno, n. id. Uncertainly: ON fella, v. “frame”
pàl- (4) ‘scoop, shovel, ladle, container”. Cf. WP II, 2 Skt. parih, f. *milkpail'; Per. parü (2) ‘shoveľ; Srb. pala, f. ‘scoop, ladle, skin bottle’; (short vowel in) OCS polü, m. ‘scoop, well-bucket'; cf. poljo, plati, v. “draw water’. (Homeric pélex, gs: -&kos ‘helmet’, if fig. for 'bucket'?)
pal- (5) ‘wattle, dewlap, hanging flesh’ Alb. palë, f. “dried fig’; palëz, f. dim. ‘lobe of ear; Lat. palea, f. ‘wattle’; cf. palear, n. ‘dewlap’; W ail, pl. eiliau, m. ‘wattle’
pal- (6), palið ‘strike, beat, hurl’. Cf. pel- Arm. cf. hal-acem, v. ‘expel’; Gk. pállo *bran- di
=== leaf 503
 cf. gafalzjan, v. ‘pleat
paliəkā, is ‘girl, seductress. WP II, 7 Av. pairikā, f. ‘siren’; Per. pari ‘fairy’; Arm. ayič, gs: ayči, ab. s. ayčav ‘whore’; (dim. in) ayčik & ayğik, gs: ayčkan, ay&kan "el: Gk. pallakë ‘concubine’; (LW in) Lat. paelex & pellex, gs: -icis, f. id. (infl. by pel-licið, v. *allure")
pamp- "ewell: swelling, bud, excrescence’. Cf. pomp- & pump-. (S1. & Baltic forms ambig.) Lat. cf. pampínus, mf. 'vine-shoot; OCS popü, m. "navel: cf. Cz. pupek, m. id.; poupě, n. ‘bud’; pupen, m. ("leaf-bud': Lat. pampi- nus); Pol. pepek, m. "navel: Srb. Cr. pupa, f. *Jeaf-bud'; Slovene, pop-ec, m. ‘rosebud’; Li. pampstu, pampti, v. ‘swel? (LW in) Latv. pampt, id.; cf. pamplà, mf. *potbelly'; pamp- lýs, m. ‘tubby boy”
pan- (1), panos, à, (n) ‘cloth, rag, flag’. WP II, 5. Cf. pån-, pānos (1) Hes. cf. pánussa, f. ‘band, ribbon’; Lat. panus, gs: A m. ‘woof; Go. fana, wm. ‘rag; OE fana, wm. ‘banner; MHG van(e), wm. id.; EME fane, s. *weathervane'; OS fano, wm. ‘cloth’; Du. vaan, f. (flag: G Fahne); Icel. fanir, fpl. ^weathervane'; OCS ponija, f. “a garment’; cf. po-pona, f. ‘veil, film’; CZ. o- pona ‘curtain’; Ukr. ‘cover, veil’. For Lat. (2), see pan- (3)
pan- (2), panā, iə ‘fen’ Gaul. ana, f. id.; Go. fani, n. ‘mud’; Du. veen, n., ON fen, n. ‘fer’; cf. MHG venne, sn., OE fenn, mn., id. beside OE feon, id.; (OE also: ‘mud’), OCS cf. po-ponü, m. ‘seaweed’; Latv. pane, f. ‘dung-liquor’; OPr. cf. pannean (for *panjan, n. *marsh')
pan- (3), panos, à ‘swelling’. Cf. pan- (1)
905
Lat. panus, m. gs: -i (tumour, gnurP. For sense of ‘woof see pan- (1)); LLat. pana, f. ‘swollen gland’; Blg. cf. pon-ka, f. dim. ‘nipple’
pan- (1), panos ‘weave; weaving’. Variant of type pan- (1) (?), q.v. Arm. hanum, aor: hanaj, v. ‘plait, weave; Gk. pénos, m. “warp'; péne, f. (Doric: -a-) ‘woof; peníon, Dor. -à-, n. ‘bobbin
pàn- (2) panos, is (protective; protection; protector Skt. panah ‘protective; panam, n. 'protec- tion’; MIr. & Ir. án ‘noble; refined’; Olr. cf. ánai, pl. ‘wealth’; OCz. pap i-st. (lord. Thus also in the mod. cliché léta páně ‘years and years’) beside Cz. pán, Pol. pan Clord" The forms h-pán, Zu-pan are synthetic cpds. Cf. LW in Li. pónas “lorP )
pandos “bent, crooked, wrong'. WP II, 6 Lat. pandus, adj. ‘crooked, bent; MHG vanz, m. (2) ‘deception’; an-vanz, ale-vanz, m. id.; (here also (?) vanz (1) ‘rogue’); ON fattr, adj. “easily bent backward'; Sw. cf. fattig, adj. *wretched" (?) beside fattas, v. “lack? (?). See Supt: P: pand-
panghus (?) “all, total. (Cf. bhn
=== leaf 504
 f. (Choulder" fr. *papulis)
páprát-, see prátins ‘ferm
pareio, pario (come, go; make come, make go' Skt. cf. paráyami, v. “bring over’; Lat. pareo & párreó, ere, sup: -itum, v. ‘appear’; OE ferian, v. ‘come, go’; OCS parjo, pariti (1) ‘fly’; the simplex occurs in Latv. pāri “over, across’, cpd. in pār-eju, -iet, v. “pass, cross’. (Isophonic: Li. põriju, yti, v. ‘tell, relate’, and (with short vowel) redup: peparein, v. ‘to show? (Pindar). (The Lat. form with -rr- suggests a possible synthetic cpd. of type *pas-rëið? cf.reio)
părpărt-, see prătins; părtins
pas- (1) a possible variant of type pà-, see páio (2) Lat. paro, åre, v. "ger Gk. páomai, fut: pas- ‘get; possess’ and Alb. mba, mbaj, v. “keep, hold" are ambig.
pas- (2) “flour, powder, dust, pollen Gk. pas- in pas-pále, pas-paliá & perh. pai- pále “fine flour’; Alb. pah, m. (1) ‘dust, powder, pollen’; Slovene cf. posije, poseje, fpl. ‘bran’. (Isophonic: MHG vase, wm. ‘fibre; thread; fringe; seam; vasen, vesen, wv. ‘sprout, spread, thrive, go to seed”)
påsko “feed, tend, protect. Cf. paið (pà-). WP II, 72 Tokh. A pās-, B pàásk-, v. “preserve, protect, exercise’; Hitt. cf. pahhsami, v. ‘protect; Lat. páscó, ére, pf: pávi, v. “feed, tend'; OCS paso, pasti and com. Sl. “tend”; paša, f. ‘pasture’; R cf. u-pasti, inf. ‘protect’. Radical in Skt. pámi, fut: pásyámi *protect'. Noun-extn. in Lat. pàstus, gs: -üs, m. ‘pasture’ beside pas- cuum, id.; OCS & Cz. pastva, f. id.
pasnos, à, is, iom “thread, web, skein, tex- ture. Gmc. variant *paso(n); Slav. variant *pàsmom Hes. pénos, m. Gk. péné, Doric: -à-, f. ‘thread, web, woof, spool; pënion ‘bobbin’; Alb. pê, gs: péni, Tosk: pë, gs: péri, m. (fthread', fr. *pasni-? but cf. Lat. pensum “skein”, fr. *pes-
907
nom as censa ‘due, tithe’ fr. *cesna. The Alb. vowel is ambig.); OHG cf. faso, wm., fasa, wf. obl: fasan- as Gk.; cf. (variant) OCS pasmo, R pàsmo (and com. Sl.) "bank skein’; (LW in Finn. pasma, id. Wrongly associated w. pás ‘belt’ in Cz.); Li. pósmas, id. (LW)
påsos, is ‘kinsman; guardian (Y. WP II, 7.
Cf. på-, etc. Tokh. A påse, B pase ‘guard, protection’; Gk. pēós, Dor. pàós ‘kinsman’; Lat. cf. pāri- in pari-cida, mf. *paricide'; OCS cf. sü-pasü, m. ‘safety, salvation, saviour’; Cz. s-pása, f. 'res- cue'. (Short-gde radical possibly in Li. pas “near, at)
(pástor- ‘herdsman’. Explicit only in Lat. pastor, id. OCS pastyrl, m. id. may be a Mol- davian LW in SI. For OE fostor- 'foster-': and Cz. pastor-ek, -ka ‘stepchild’ see postor-, radical: pot-, põ- 'feed"
```


## [2026-09-14T00:50:41.555Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (538,539,540):\n    print('=== leaf',n)\n    print(leaves[n][:3000])\nEOF"
}
```


### [2026-09-14T00:50:42.711Z] TOOL RESULT

```
=== leaf 538
nd com. Gmc.)
pnt- (pnts-) ‘go, track; passage, way’. Cf. pent-, pont-. WP II, 26 Skt. cf. patháh, gen.sg. of pánthah, m. ‘way’; Av. paða-, id.; Ober, paði- f. id.; Oss. cf. fätäg (Cleader" Here: Abaev); Gk. pátos, m. ‘path’; cf. patéo, v. ‘tread, walk’; MIr. éiss, s. (Cpath', fr. *pnts-) beside étaim, v. “find”; éit, f. (“herd?. Background ambig.); OHG cf. funs, OS. OE fus, adj. “eager, ready’; R cf. o-pjàt', Cz. z-pét, adv. ‘back’; Cz. pata, f. ‘heel’; OPr. pintis ‘path, track’; Finn. LW (here?) pato “dam, weir’
putrom Du. vonder, m., Fris. fonder, m. ‘footbridge, bridge of planks’; OCS petro, n. (‘ceiling’, esp. ‘coffered ceiling’); Pol. pietro, Cz. patro ‘storey’
(po, aphetic form of apo and upo, q.v. Arm. v-; Arcad. Cypr. po-; OCS po, po-; Li. pa-; Latv. pa, pa-. Prob. also in Lat. synthetic cpds. as follow, but ambiguously *po- or *pod-, since WSP -d is lost in pro-pe for *pro- ped ‘near’, but not in apud, for *ad-pod, id. OLat. poplicod: publico, etc. Cf. pono fr. *po(d)-sino): *pons ‘decree’ in the cpd. ponti- fex, cf. G Gesetz, and E law for the sense; pudeo "am ashamed’, fr. *po(d)-uidejo, cf. R
969
po-zor ‘disgrace’ for the sense; po-moerium, n. “space round city wall, moat’; and perh. paene, if for *po-jó-ne or *po-jà-ne ‘nearly’, cf. Li. kuo-ne, id. forsense. Cf. also WH:LEW on polio, porceo & po-lübrum)
(pó- radical ‘drink’, see pótos, in Gk. pó-ma, n. (2) ‘beverage’; Cz. na-pájet, inf. "water — animals")
pod-, pód- radical: “foot: ground, base’. See ped-, pods and the following
podeio (podiio, podio) “set on a footing, set, base, foot, go’. Cf. pods, etc. Skt. padye, mp. (2) (go; Gk. podízo ‘pace out, shackle’, OHG cf. fazzen, v. “load, equip’ beside MHG vezzen, v. ‘fetter’; OE fetian "bring, fetch; induce; marry'; ON cf. fata, v. ‘step’; Srb. podim, iti ‘floor’; cf. Arm. atean, gs ateni, ab. s. -iv, s. ‘tribunal’; Ir. cf. ui- dheacht, f. “journey”
podios, iom, io of a foot, of a base, of a pace; foot, base, pace', etc. Cf. ped-, pod- (pods) and extns. WP II, 23. Adjectival variant: podiko- Skt. (vowel ambig.) pádyam ‘syllable’; pádya, f. “pace; path"; Oss. faz, Dig. fazà ('buttocks'. Vocalism as Lat. podex, but this is ambig. « *posd-?); Arm. oC, i-st. and o-st. (2) *haulm"; cf. atean, gs: ateni, i-st. ‘tribunal’; Gk. pódion, n. ‘small foot, foot-bandage'; (LW in) Lat. podium, n. ‘balcony, theatre-box'; Ir. oidhe, m. 'traveller'; OCor. odion, late Cor. ojyon, m. ‘0X’; Br. eZenn, s. id.; Icel. fet, n. ‘pace, step, foot’; OCS. poZzdi, m. “floor, pavement, foundation’; Li. padis, gs: padZio, m. ‘base’. For *podik- (podok-) cf. Skt. padikah “pede- strian’; Arm. h-atak, i, av, s. (bottom, base’, fr. *en-podok-); Gk. cf. a-pódikos “without standing, outcast’; Gaul. odicos, odecus, odo- cos *dwarf-elder'. (Lat. podex ‘arse’ is ambig. Despite the phonological equivalence of Oss. faz, fazà, id. the background may be *po-sd-, see po-, sed-). Cf. LG fette, f. 3oist
pods (pod-, podos, à, om, poduo-) ‘foot, base, ground, footing. WP II, 23. Cf
=== leaf 539
r, slab’ beside Cz. půda, f. “ground”; Li. pádas, m. ‘sole of foot’; pádis, gs: padio, m. ‘base’ (Li. pádas also “bottom, floor of hearth, threshing-floor' under infl. of Russian); Latv. pads, m. ‘clay floor
poi (?) "at Gk. (Arg. Phoc. Locr.) poi, id.; Alb. pe ‘from, to’; Latv. pie, px. pie-, prp. “aP
poigh- “mark; marked, motley, doomed'. Cf. poiK-, peigh, peiK- Umb. cf. peia-, peiu, adj. “a colour’; cf. Lat. pio, are, v. (2) ‘defile’; OHG feigi; Du. veeg; OE fag, adj. ‘motley, gay’ beside fæge “marked, doomed, fey’; OCS pégü, adj. ‘motley’; R pégij, id.; Srb. pjega, Cz. piha, f. ‘freckle’; Li. cf. piegma, f. id. ON feigr ‘fated’; Sw. feg ‘cow- ardly, (as OHG and Du.) display extn. of sense “marked?” > ‘doomed’.
poikos (?) ‘trivial, diminutive’ LLat. cf. *piculus (implied in It. piccolo "Dt. tle’); G fee, adj. ‘meek, shy, modest’; cf. Icel. peiminn, id. (if fr. *poikmen-); Li. paikas ‘silly’. (Finn. poika “boy? and poju, id., LW in Sw. pojke, id. unrelated)
poikeið ‘paint, decorate’. See next and poi- Kos, and cf. peik- (pik-) OPer. cf. a-paišam 'I have written’; Tokh. B paik- ‘write’; MHG vehen, wv. tr. & intr. (1) ‘decorate, colour; become coloured"; Li. pai- šau, -yti, v. ‘draw, sketch"
poiKolos (poikKilos) “painted, bright, gay, motley’. See next Skt. peSaláh, adj. ‘decorated’; Gk. poikilós, adj. ‘variegated’
poiKos, om (1) “mark, paint, drawing, writ- ing; marked, decorated’. WP II, 9. Cf. poikeio,
971
peik- (pik) and next Skt. pé$ah, m. 'ornament'; Av. paešō, m. id. (and ‘shape’); Ober cf. paisiya, f. ‘writing’; Oss. fes, s. (Tuck?. See note on poigh- "mark: Tokh. A cf. paik-, v. ‘write’; Gk. cf. poikilós ‘variegated’; Lat. picus, m. pica, f. (magpie; woodpecker’. Lit. ‘variegated or ‘pied’ bird"); Umb. peico, m., peica, f. as Lat., beside peica, adj. f. ‘brindled’; OS féh, MHG vech, gs: véhes, adj. ‘motley’; G cf. Feb, s. (“sable- skin’, lit. *mottled"); Go. cf. filu-fáihs, adj. *many-coloured'; Li. paiSas, paiSà, m. f. and -0s, fpl. ‘smudge, charcoal mark, blot’; cf. also piesà 'smut'; paisüs ‘smutty’. (OE fina, wm. *woodpecker' seems to represent a type *peiKno-)
poiKos, is (2) ‘demon, devil; malignant’. Skt. cf. paisunam, n. ‘slander’ beside (z-gde) pisunah, adj. ‘malignant, vile’; Av. paesis, f. 'she-demon, demon of corruption’; Arm. ajs, o-st. ‘demon’; (OHG [? oxytonic prototype] feigi, adj. ‘doomed? is ambig. See under poighos); (here however) MHG vehe, véhede, sf. ‘hostility’: OHG gi-fehida (beside EMDu. veete “malice'); also MHG véhen, sn. id. (: Skt. paiséunam)
poimóo(n), poimen- ‘herdsman’. WP II, 72 Myc. & Gk. poimén, gs: -enos, m. (and “guard, ruler); Li. piemuó, gs. -efis, m. id.; (LW in) Finn. paimen, id.; cf. also OE fæmne, wf. *gir; (?) ON. feima ‘shy girl’; Li. pieméne, f. 'shepherdess, cowgirl
poimos, om Av. paema, n. ‘mother’s milk’; OHG feim, MHG veim, sm. ‘foam’; OE fam, n. id.; Finn. cf. piimä (‘sour milk, yogurt’; “believed to be an archaic LW fr. an Iran. dial? — Itkonen & Joki: SKES IIT). See next.
poin- (1) (phoi
=== leaf 540
king; drink’. Cf pt-, etc. Skt. páyas, n. “fluid, sap, juice, milk’ beside peyah, adj. & s. ‘drinkable; drink’; payam, pt. (while drinking: (radical of) OCS na-paj-ati, v. ‘give to drink’); Av. payo, m. ‘pasture’ be- side payas, -áh-, n. ‘milk’; Gk. cf. poi-mandría *milk-pail'; Cz. cf. ná-poj, m. ‘beverage’
poksos, is, ios, üs ^wing, side, flank, wall, partition, pigeon-hole'. WP II, 3 Skt. paksáb, m. “wing, side, half, party’; Oss. faxs, pl. fäxstä ‘side’ beside fáxs ‘strip, board’; Gk. puxís, gs: -idos, f. (box. Vocalism as nüx, see noktis above); Myc. cf. pukso(1) (parts of a table, perh. *drawers, flaps"); Latv. paksis, pl "nterlocking beams, tenon-and-mortise joint, corner of box, side’. Cf. also OE fzes, n. ‘border’; Swiss Fácke, f. ‘wing’. Long-gde in R pax, Cz. pach, m. ‘groin’; Cz. also pachy “loose sleeves’; Ukr. paxa, f. ‘armpit’; Blg. pàxove, pl. (^waist': Skt. pāksah “of half, side or party’: Oss. faxs ‘side’)
poKos, us (poKmos, poktos) ‘fleece, wool, hair; (combed, kempt)'. WP II, 16, Cf. peko Per. pa$m *^wool'; Oss. fásm, id. beside fasín, v. ‘comb’; Arm. asr, gs. & ab. s. asu ‘fleece’; Gk. pókos, m. id., cf. pó-gon, -gonos ('kempt chin”, hence ‘beard’, or fr. aphetic *(a)po-8on- 2); OHG fahs, sn. ‘hair; MHG vahs, sm. & sn. id.; OE feax, n. ‘hair of the head’; ON fax, n. ‘mane’; Du. cf. vacht, f. ‘fleece’; Li. cf. pá$ymas, m. ‘combing, carding’; pašaŭ, -ýti, v. ‘comb, card’
pol- (1) ‘much, many; abundance’. Cf. po- luos (polu), pelu (1), peluð (1) & (2), plë-, etc. WP II, 65 Av. parus ‘full, big? beside paourus, pourus ‘abundant; perfect’; Gk. polús, Epic gs: po- léos, npl. polées, beside poulús, adj. ‘plenti- ful’; Lat. cf. pol- in po-pulus, if for *pol-polos; pol-lex, gs. -licis, if for *pol-diks ‘thumb’, lit. ‘full-finger’; Pol-lux ‘god of lightning’;
973
and perhaps: pul-cher, -cer ‘beautiful’, second element doubtful’; Arm. cf. h-olov, Let (“plen- tiful’, for *en-poleu- or sim.); R cf. polaja vodà ‘high water’; Latv. cf. pali, mpl. id. See poluos for further exx.
pol- (2) (polos, à, is, io, us) “fold, flap, flank, side, limb’. Cf. poltis Skt. paruh, m., parus, n. "limb, joint? beside palam, n. (*flesh', of ambig. background, but cf. ka-palam, n. "halt: Arm. cf. (?) hay-ord, i-st. (mutual, lit. *half-side'?); Gk. cf. epi- polés, adv. “on the surface’; Alb. palë, f. “fold; side; party; pair’; Lat. cf. inter-polo, -polare, v. ‘renew, repair’; ON fol, f. (“layer of snow’, fr. *polus) beside fel, f. lap, pleat of garment or sim. fr. *polis); mod. falur, pl. falir, m. *socket'; OCS polü, gs: polu, m. ‘side, bank, sex, half”; pola, f. “half, margin’; cf. poli, prp. w. gen. ‘adjoining’; Slovene pola, f. “flat sur- face, quire’; R pol, m. “half; sex’; polà, f. ‘flap, lapel; OCz. cf. oba-poly ‘twofold’; Li. palas, m., palà, f. “width of cloth’; pl. paliai, adv. ‘along, down’; Finn. LW puoli (*side, half”. For vowel cf. kuoppa ‘piť’, kuoria “shell, peel, see kop-, kor-); (uncertainly) cf. Arm. lvem, v. ‘hem’; Ivik “hem. Extn. in Hitt. pa
```


## [2026-09-14T00:50:47.478Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (541,542,543):\n    print('=== leaf',n)\n    print(leaves[n][:3600])\nEOF"
}
```


### [2026-09-14T00:50:48.455Z] TOOL RESULT

```
=== leaf 541
llo-Lat. olca, f. 'fallow-land' (phonol. cf. orco ‘pig’: farrow); MHG val, gs: valwes, adj. *pale'; Upper G falch, G fahl, adj. “fallow? be- side falb, adj. ‘blond’; OE fealh, f. “fallow- land’; R polosà, f. ‘strip, seam, tract of land” beside (e-gde) pelesyj, adj. ‘fallow’; Li. pal&as,
pol- — poluos
20
25
30
35
40
45
974
adj. ‘fallow, dun’; Late palss, id.
pelpolis, os ‘plethora, flood, swarm’. Cf. pol-, polu, poluos, etc. Arm. oyoy, i-st. “flood”; Lat. populus (early: poplo-: Osc. poplo-, Umb. puplu- "people"
poltis, os, ios, à (1) ‘side, fold, flap’. Cf. pol- (2). WP II, 56 Skt. (ambig. patah, m. “cloth, garment, screen, canvas’; patih, f. ‘kind of cloth’; Gk. cf. (e-gde) pélte, f. ("light shield’. Here?), and (z-gde): di-plásios. See plt- above); Hitt. cf. paltanas (fside" or *arm"); Alb. palsé, f. “fold, wrinkle, lobe of ear, muscle of nose! beside paltoj, denom. vb. 'fold'; Go. -falps, cpds. -fold? beside OE falod, fald, m. “fold, pen’; MHG valt, sm. “fold, wrinkle, roll of cloth, pack, envelope, corner? beside valte, s & wf. id.; ON faldr, m. “fold, hem’; OCS platü, m. 'rag, kerchief; Slovene ‘side, page’; Blig. ‘cloth-length’; Cz. cf. zá-plata, f. ‘patch’; R po- lot, f. ‘side of gammon’ cf. also R polotnò, Cz. plátno, n. linen’; (LW in) Finn. palttina, id.; Li. páltis, ies, f. ‘side of gammon, flitch’. (Gmc. forms imply *poltó-, poltá)
poltis, os, å, ios (2) *mash, pudding? Skt. cf. par-patab, m. (frice-mash, pease-pud- ding” fr. *pol-poltio-); Gk. póltos, m. “pudding, porridge’; Alb. palcë, f. ‘mush; marrow, pith’; Lat. puls, gs pultis, f. ‘pudding’ beside It. polta, f. ‘pap, batter’; Olr. cf. littiu, f. (“porridge, plaster’, if for *pltiu-); Latv. palts, gs. id., s. *puddle' beside paltas, fpl. “blood pudding”: (LW in) Finn. palttu, s. as Latv.
polu, see pol- (1) and poluos (1)
(poluis, a (pelu-) ‘dust, powder’, etc. See peluos & pélouos)
poluos (1) (polus, polu) “big, full; much, many, abundant; spate’. Cf. pel-, pl-, plnos, pltos, plëtos, etc. WP II, 65 Skt. cf. parvami, v. "DI": Av. paourus, pourus, parus, adj. “abundant; full, big'; OPer. cf. parav, prn. ‘many’; Per. cf. farawan, adj. “abun- dant’; Oss. fír, Dig. fur, prn. ‘much, many’; Arm. cf. h-olov, adj. (much, many, great’, fr. *en-peluo-); Myc. poru- (for polu-); Gk. Hom. poulüs, beside Gk. pollós ‘abundant, strong’; polüs, f: pollé, adj. ‘many’; Lat. cf. pollens, gs. -entis, adj. “powerful, resourceful’;
975
cf. pol-lex, Pollux, populus, mani-pulus, -plus, am-plus, pulvinus & polvinar, epulae, and pul- cer, -cher for possible relics of type *polu-); Olr. and Ir. oll, oll-, adj. & px. ‘great, huge"; R cf. polovodie, n. “high water’; Latv. cf. pali, mpl. id.
poluos (2) (poliuos, politos) “fallow, sallow, dun'. WP II, 53. Cf. polKos (2) Skt. cf. palitáh ‘grey’; Oss. fårv, Dig. fárwà ('alder'. Cf. E 'sallow-tree"); Myc. poriwo- (for *poliwo); Gk. poliós, adj. ‘grey’; Lat. pullus, adj. ‘tawny, hare-coloured, pale’; OE fealu, gs: fealwes 'fallow, dun'; OHG falo, id.; ON folr, acc. sg. falvan ‘pale’; OCS plavü, id.; Srb. “blond, blue’; Big. plàvi “light blue’; Li. palvas “fallow, pale yellow'. See FK:DEW: falb
pomn- ‘surface, cover, top’. (Aphetic for *upó-mn- (?), cf. upo-) Skt. pàman, m. 'scab'; Gk. póma, n. (2) “cover, lid”. (ISophonic: Gk. póma, n. (1) ‘beverage’; Lat. pomum *fruit^)
pompos ‘swelling; belly, navel. Cf. pamp- & pump-. (Sl. & Bait. ambig.). Cf. WP I, 130 & II, 108 Lat. cf. (7) pomponianus ‘pear shaped like a woman's breast; OCS (ambig.) popü, m. (nave. See pamp-); Latv. pope, f. “cushion, pillow? beside popis, s. ‘pad, felt; popét, inf. ‘stuff; Li. pam
=== leaf 542
 LW ?). (Isophonic: OCS podü, m. *food")
pondheió (pondhio) ‘press, probe, attack’. (Vocalism ambig.) MHG vanten, G venden, wv. “try, probe, find out’; OFris. fandia, wv. ‘visit’; OE fandian, v. “probe, explore, experience, visit"; cf. fandung ‘probe, search, temptation’; OS fandon, v. 'ransack; probe’; OCS poZdo, poditi, v. drive: Pol. pędzić, v. ‘drive’; Cz. pudit, inf. ‘impel’; Srb. puditi, inf. ‘scare off; cf. Pol. ped, m. ‘rush, dash; shoot, bud’; Cz. pud, m. "instinct". Here also EM. vanden, v. ‘visit’
poluos — pordhimos, pordhmos
20
25
30
35
40
45
976
ponguos ‘whole, sole; total, Jot" (?). (Evi- dence ambig. Cf. panghus & bhngh-) Hitt. pankus, gs: pangawas, adj. “whole, all’; Mir óg, uag, adj. id.; Cz. pouhý, Slovak pühy, adj. “sole, mere’
pontos, is, à (ponth-) “crossing, passage’. WP II, 26 Skt. cf. panthah, A mf. ‘path’; Av. panto, panta, mf. id.; Oss. (dim. type) fándag, pl. fándágta ‘road’; Arm. hun, s. “ford, strait’; Gk. póntos, m. ‘high seas, the main’; Alb. péndé, f. ‘weir, dam’ (if not a LW?); Lat. pons, gs pontis, gp pontium, m. ‘bridge’; OS foói, faói, io-st. (going, gait'; G cf. fahnden, v. (^sleuth, stalk’, but see pondheio); Icel. cf. fans, m. ‘gang’; OCS (and com. SI.) poti, gs: poti, m. “road, highway’; Latv. pants, m. “line of verse?
poqu-, o-gde form of pequ-, q.v.; poqutos (poquonos) ‘baked, cooked; baked or cooked object? Per. cf. puxte, pp. ‘cooked’; Arm. hac, i-st. “bread, loaf’; Tokh. A & B pak-, v. ‘boil, bake, ripen’; Myc. cf. a(r)to-poqo- ‘baker’; Gk. cf. pópanon, n. ‘cake’; Lat. coctus “boiled, ripe, digested; Gallo-Lat. pottus, m. Cpot, fr. *quoquto-, w. assimilation); W pob, adj. & s. “baked; baking’; poban, pl. au. f. “oven; roaster’; poeth, adj. (hot, fr. *quoqutos, w. assimilation); Cor. pobas, inf. ‘to bake"; poth, adj. ‘scorching’; OCS. (and com. Sl.) potü, m. ‘sweat’
por- (poro-), px. variant of type pro- (pro-), cf. also per-, pr-. Cf. WP II, 39 Skt. (ambig.) para- ‘over, further’; Av. (ambig.) para- “fore-?; Per. par-, id.; OHG far- (possi- bly a scribal form of for-); Li. par-, in par- duoti, inf. ‘sell’; par-da, f. ‘sale’; etc: Latv. pār- (in pār-dot ‘sell’, etc.); cf. also Lat. *por- implied in posco, por-tendo, por-go, etc.
pordos, à ‘fart’. O-gde to perdo, q.v. WP II, 49. Cf. prd- Skt. pardah, m. id.; Gk. pordé, f. id.; MHG farz, G Farz, sm. id.; Norw. cf. (slang) farte omkring “lounge about’; Li. pardà, f. fart
pordhimos, pordhmos ‘forefront, forward motion”. Cf. por-, pro-, etc. Gk. porthmós, m. “strait, passage, ferry’; Alb.
977
parsëm, parzëm, f. ‘chest, breast, bosom’; i parsëm, adj. “fore-, front-; MHG cf. vart, sf. Journey”
poreið “convey”. Cf. pero (2) and poros Gk. porízo, v. id.; Go. farjan, v. ‘travel’; MHG vern, wv. ‘travel; transport’; ON ferja, v. ‘ferry’; cf. G Ferge ('ferry', also Nora Eng.)
porg- (?) Arm. harkanem, v. (“strike; touch". Ambig. cf. prk-); Olr. & Ir. orgim, orgaim, v. ‘strike, kill"; Gaul. cf. orge! "Kl: OBr. tre-orgam, lsg. ('pierce', fr. *tro-?); orgiat, s. ‘killing’
por£os, porgen- ‘breeding animal; bred ani- mal, pig”. Du. varken, n. (‘pig’. Sense influenced by type *farh- as in OHG farah, MHG varch, gs: varhes ‘pig’. See porKos); Norw. fark ‘rogue, tramp’; OCS prazü, m., praze, n. dim. fram"; OR & dial. póroz, m. id.; Srb. praz, id.
porkos, io ‘net, sling’. Cf. porquà. WP II, 45 Per. cf. falaxan, s. ‘sling’; Iran. LW in Arm. pars, id.; Gk. pórkos, m. *fishing-net; creel’; OCS prakü, m. ‘sling, catapult’; beside prašta, f. id.; Cz. prak, m. id. beside Pol. proca, Srb. praća, f. id. (Srb. also ‘stirrup’)
(porks-, o-gde variant of type prks- (prs-), prk
=== leaf 543
 Cz. prach, m. ‘dust’, and com. Sl. beside R poròxa, f. ‘early snowfall’)
pork- (porKs-) (?) ‘surrounding, edge, rim’. Cf. perkus & WP II, 45 Ober. parsa- ‘court’; Gk. pórkes, m. “loop, ring, snath’; Lat. porca, f. (fridge, baulk’, but cf. porKos ‘pig’ and semantic note); W cf. variant: orch, pl. -au, f. ‘border, limit’
porKos, à ‘hog; sow'. WP II, 78 Arm. (?) cf. mkn-harsnuk ('weaseP', lit. *mouse-pig'?); Lat. porcus, gs. -1 m. ‘pig’; (LW in) Gk. pórkos ‘hog, boar’; Umb. purka, porca, acc. pl. f. ‘sows’; Ir. orc, m. ‘pig, boar’; OHG farah, farh, n., MHG varch, gs: varhes, sn. id.; OE fearh, m. id.; OCS (dim. type) prasę, n. id.; Li. parSas, m. id. (LW in) Finn. porsas, s. ‘piglet’. (Lat. porcina: Li. parsiena, f. *pork")
(porKsKó, sec prKsKo)
porKuos, is “bright, clear, clean, pure? Per. pārsā ‘chaste, pious’; (LW in) Arm. parz,
poreið — porsó
20
25
30
40
45
978
Lat ‘clear, blank, open’; Arm. oro&, oris, adj. ‘distinct’; Hitt. parkwis (acc. sg. once: parkun), adj. “pure, guiltless’; Hes. cf. (?) phorkós (err. for *porkós ?, adj. bright); Go. farwa, f. “shape”; cf. anparamma-farwai, adv. 'apparent- ly different; OHG faro, gs farawer, adj. 'seem- ing! beside farawa ‘colour, effec"; MHG var(e), gs varwer ‘coloured’; varwe, sf. ‘col- our’; Norw. farge, s. ‘colour’. Variants in Skt. parusáh (1) ‘motley’; Av. pauruso (alleged), id.; cf. also Du. verf, f. 'sheen' and Icel. farfi, m. “paint
pormos ‘going, gait, progress, ferry, freight". Variant porom-. WP II, 39. Cf. por-, pro-, etc. and next Skt. cf. param, adv. “away”; Tokh. A parma, B perma ‘meanwhile’; Gk. cf. pórimos, adj. ‘passing; inventive’; OS. OHG faram, farm, sm. 'swift stream, ferry; MHG varm, sm. ‘ferry’; OS (also) farm, m. ‘march, campaign’; OE fearm, m. “cargo”; ON farmr, Norw. farm, m. id.; R poróm, Cz. prám, Srb. pràm, m. Ter, ry
poros, om 'passage, crossing, track, space, period'. Cf. per-, por-, etc. Gk. póros, m. “passage, track, ford’; MHG var, sn. “ferry, passage); OE fzer, n. “way, passage, ship’; faru, f. journey; chattels; lifetime’; ON far, n. ‘passage, track’; for, f. u-st. journey’; -fari, cpds. ‘traveller’; R porà, f. ‘time’; Blg. pora, f. “age”; Li. para, f. ‘day of 24 hours’; par-, px. ‘back’. WP II, 39
(poros, à ‘beating, blow”, etc. See perio (2). Only in OCS pora, f. ‘strife; force, violence’; Slovene por, m. ‘rupture, têar’)
porpor- (parpar-?) Skt. parparīh, f. ‘tress’; Cz. Ukr. prapor, m. “flag?
porquos (porquið(n)) (1) ‘scab, itch’ Arm. cf. orkiwn, gs: o. ab. s. -ov beside orkin, s. id.; Li. párkai, mpl. & párkos, fpl. id.
porquos, à (2) fcrosspiece, buckle, clasp; board, thwart’. Cf. perquó Oss. fark, Dig. farkà “board; paddle, blade”; Myc. po(r)qa (queried: — ‘buckle’ or ‘clasp’); Gk. pórpē, f. ‘buckle’
porsó “forth, away, farther’
979
Gk. pórro, pórso beside pórsion, id. (the last a comparative form); Lat. porro, id.
porstis (prsth-) “calf; youngster'. Skt. cf. pfthukab, dim. type ‘child’; Arm. ort, gs. -u, S. (calf; Myc. & Gk. pórtis, f. ‘calf, heifer'; cf. the variants in OHG far, pl. farri, ferri, m. ‘bull; MHG verse, f. ‘heifer’; G Fárse, id.; Du. var, m. ‘bullock; boar’; vaars, f. ‘heifer’; Sw. får, n. ‘sheep’
port- (1) (portos, a, us, is) “way, passage, gate'. Cf. per-, perio (1), poros and prt- (1) Lat. portus, gs: -üs, m. ‘harbour’; porta, f. ‘gate, entrance, mountain pass’; Osc. pürta-, f. id.; OS fard, f. i-st. journey, way’; vart, sf. id.; G Fahrt & Fährte; OE fierd, f. 'expedi- tion’; OCS cf. pri-prati, f., -pratü, m. & -prata, f. ‘doorway, porch?’ beside (z-gde) pri-prütü, m. id.; cf. also prasto, pratiti, v. “attend, accom- pany’; Srb. p
```


## [2026-09-14T00:51:36.445Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins pel- entries\"; grep -n \"^pel-\" AHD_watkins1985.txt | head -20\necho \"=== falcon in AHD\"; grep -n -i \"falcon\" AHD_watkins1985.txt | head -20\necho \"=== pulvis/pollen\"; grep -n -i \"pollen\\|pulvis\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T00:51:36.512Z] TOOL RESULT

```
=== AHD watkins pel- entries
230:pel-*. IT. Extended form *peb-...
831:pel-4. Skin, hide. 1. Suffixed form *pel-no- in Germanic *felnam in Old English fell, skin, hide: FELL, 2. Ger- manic suffixed form *fel-men- in Old English filmen, membrane: FILM. 3. Suffixed form *pel-ni- in Latin pellis, skin: PELISSE, PELLICLE, (PELT!), PELTRY, PIL- LION; PELLAGRA, SURPLICE. 4. Greek -pelas, skin: ERY- SIPELAS. 5. Suffixed form *pel-to- in Greek pelté, a shield (made of hide): PELTATE. [Pok. 3 b. pel- 803.]
832:pel-5. To sell. Lengthened o-grade form *pdl- in Greek p6lein, to sell: BIBLIOPOLE, MONOPOLY. [Pok. 5. pel- 804.] pel-6. To thrust, strike, drive. I. Suffixed form *pel-de-. 1. Germanic “*felt-, *falt-, to beat, in: a. Old English anfilt(e), anfealt, anvil (“something beaten on”): ANVIL; b. Germanic “*feltaz, *filtiz, compressed wool, in (i) Old English felt, felt: FELT! (ii) Medieval Latin filtrum, filter, piece of felt: FILTER. 2. Latin pellere (past participle pulsus), to push, drive, strike: POUSETTE, PULSATE, PULSE!, PUSH; COMPEL, DISPEL, EXPEL, IMPEL, PROPEL, REPEL. 3. Suffixed o-grade form *pol-o-, fuller of cloth, in Latin polire, to make smooth, polish (< “to full cloth”): POLISH. II. Extended form *peb-. 1. Present stem *pelna- in: a. Latin appelldre, “to drive to,” address, entreat, appeal, call (ad-, to; see ad-): APPEAL; b. Latin compellare, to accost, address (com-, intensive prefix; see kom): COMPELLATION; Cc. Latin interpellare, “to thrust between,” interrupt (inter-, between; see en): INTERPEL- LATE. 2. Suffixed zero-grade extended adverbial form *pla-ti, in pre-Greek *pldti in Greek plésios, near (< “pushed toward”): PLESIOSAURUS. [Pok. 2. a. pel- 801.] pel-7. Dish. Suffixed lengthened-grade form *pél-owi- in Latin pélvis, basin: PELVIS. [Pok. 4. pel- 804.] pele-1. 1. To fill; with derivatives referring to abundance and multitude. Variant “*p/é-, contracted from “pleo-. I. Suffixed zero-grade form “pls-no-. 1.Germanic *ful- naz, *fullaz, full, in Old English full, full: FULL’. 2. De- rivative Germanic verb *fulljan, to fill, in Old English fylian, to fill: FILL. 3. Latin root *pldno-, replaced by *pléno- (influenced by Latin verb plére, to fill; see III. 1. below) in Latin plénus, full: PLENARY, PLENITUDE, PLENTY, PLENUM; PLENIPOTENTIARY, REPLENISH, TERREPLEIN. II. Suffixed form *p(e)la-u-. 1. Possibly Latin paliis, marsh (? < “inundated”; but possibly rather from pel-?): PALUDAL, PALUDISM. 2. Obscure compara- tive form (Old Latin p/ous) in Latin plis, more: PIU, PLURAL, PLUS; NONPLUS, PLUPERFECT, SURPLUS. 3. O-grade form *pol()-u- in Greek polus, much, many: POLY-; HOI POLLOI. III. Variant form “p/é-. 1. Latin plére, to fill: (ACCOMPLISH), COMPLETE, COMPLIMENT, COMPLY, EXPLETIVE, IMPLEMENT, REPLETE, SUPPLY. 2. Possibly suffixed form *plé-dhw- in Latin p/lébs, plébés, the people, multitude: PLEBE, PLEBEIAN, PLEBS; PLEBISCITE. 3. Suffixed form *plé-dhwo- in: a. Greek pléthos (Ionic pléthus), great number: ISOPLETH; b. Greek derivative verb pléthein, to be full: PLETHORA; PLETHYSMOGRAPH. 4. Suffixed (comparative) form *plé-i(sjon- in Greek pledn, pleién, more: PLEO-, PLEO- NASM; PLEIOTAXY, PLEIOTROPISM, PLIOCENE. 5. Suffixed (superlative) form *p/é-isto- in Greek pleistos, most: PLEISTOCENE. IV. Possibly Sanskrit piirah, cake (< “that which fills or satisfies”): POORI. [Pok. 1. pel- 798.] pela-2, Flat; to spread. Variant *pld-, contracted from *plaa-. 1. Suffixed form *pel{a)-tu- in Germanic “felthuz, flat land, in Old English feld, open field: FIELD. 2. Suf- fixed form *pel{a)-t-es- (by-form of *pel)-tu-) in Ger- manic *feltha-, flat land, in: a. Old High German feild, field: FELDSPAR; b. Middle Dutch veld, velt, field: VELDT. 3. Variant form “pld- in: a. suffixed form
=== falcon in AHD
507:ghaiso-. A stick, spear. 1. Germanic *gaizaz in: a. Old English gar, spear: GORE}; (GARFISH), GARLIC; b. com- pound *nabé-gaizaz, tool for piercing wheel hubs (*nabd, hub; see nobh-); c. Old Norse geirr, spear (in geirfalki, gyrfalcon, akin to the source of Old French girfaut): GYRFALCON. 2. Germanic *gaizé in Old English gdra, corner, point of land: GORE?. [Pok. ghaiso- 410.]
828:fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. zero-grade. form *pkt-en- in Greek kteis (genitive ktenos < *pktenos), a comb: CTENIDIUM; CTENOID, CTENOPHORE. [Pok. 2. pek- 797.] peku-. Wealth, movable property. 1. Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD?; INFEUDATION. 2. Suffixed form “peku-n- in Latin peciinia, property, wealth: PECUNIARY; IMPECUNIOUS. 3. Suffixed form *peku-l- in Latin peciilium, riches in cattle, private property: PECULATE, PECULIAR. [In Pok. 2. pek- 797.] pekv-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kvekw- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. 2. Greek pe- pon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN. 4. Greek -pepsia, digestion: DYSPEP- sia. 5. Sanskrit pakva-, ripe: PUKKA. [Pok. peky- 798.] pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: PoL- LEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff: PAILLASSE, PALEA. 4. Greek palunein, to sprinkle flour: PALYNOLOGY. 5. Greek poltos, porridge (made from flour), probably borrowed via Etruscan into Latin as puls, pottage: POULTICE, PULSE?. [Pok. 2 b. pel- 802.] pel-2. Pale. 1. Suffixed variant form *pal-wo- in: a. Ger- manic *falwaz in Old English fealu, fealo, reddish yellow: FALLOW DEER; b. Latin pallére, to be pale: PALE, PAL- LID, PALLOR; APPALL; C. Latin palumbés (influenced in form by Latin columbus, dove), ringdove, “gray bird”: PALOMINO. 2. Suffixed form “pel-ko- probably in Ger- manic *falkén-, falcon (< “gray bird”), in: a. Old French girfaut, gyrfalcon: GYRFALCON; b. Late Latin falcé, falcon (but Germanic *falkén- is also possibly from the Late Latin): FALCON. 3. Suffixed extended form *peli- wo- in: a. Greek pelios, dark: PELOPS; b. o-grade form *poli-wo- in Greek polios, gray: POLIOMYELITIS. 4. Per- haps Greek pelargos (< *pelawo-argos), stork (< “black- white bird”; argos, white; see arg-); PELARGONIUM. [Pok. 6. pel- 804.] pel-3. To fold. 1. Extended o-grade form *polt- in Ger- manic *falthan, *faldan in: a. Old English fealdan, faldan, to fold: FoLD!; b. Old High German faldan, to fold: FALTBOAT; Cc. Germanic compound “*faldistélaz, “folding stool” (*stdlaz, stool; see sta-), in Medieval Latin compound faldistolium, folding chair: FALDSTOOL;
1497:Fair? dhés- FAITH bheidh- FALCON pel-2 FALDSTOOL pel-3 FALL p(h)ol- FALLOW DEER _pel-2 FALTBOAT pel-3 FAME bha-2 FAMOUS bha-2 FAN! wet-1 FANATIC dhés- FANG pag- FANTASY bha-1 FANTOCCINI bha-2 FAR pert
1574:GYRFALCON ghaiso-, pel-2
=== pulvis/pollen
828:fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. zero-grade. form *pkt-en- in Greek kteis (genitive ktenos < *pktenos), a comb: CTENIDIUM; CTENOID, CTENOPHORE. [Pok. 2. pek- 797.] peku-. Wealth, movable property. 1. Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD?; INFEUDATION. 2. Suffixed form “peku-n- in Latin peciinia, property, wealth: PECUNIARY; IMPECUNIOUS. 3. Suffixed form *peku-l- in Latin peciilium, riches in cattle, private property: PECULATE, PECULIAR. [In Pok. 2. pek- 797.] pekv-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kvekw- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. 2. Greek pe- pon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN. 4. Greek -pepsia, digestion: DYSPEP- sia. 5. Sanskrit pakva-, ripe: PUKKA. [Pok. peky- 798.] pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: PoL- LEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff: PAILLASSE, PALEA. 4. Greek palunein, to sprinkle flour: PALYNOLOGY. 5. Greek poltos, porridge (made from flour), probably borrowed via Etruscan into Latin as puls, pottage: POULTICE, PULSE?. [Pok. 2 b. pel- 802.] pel-2. Pale. 1. Suffixed variant form *pal-wo- in: a. Ger- manic *falwaz in Old English fealu, fealo, reddish yellow: FALLOW DEER; b. Latin pallére, to be pale: PALE, PAL- LID, PALLOR; APPALL; C. Latin palumbés (influenced in form by Latin columbus, dove), ringdove, “gray bird”: PALOMINO. 2. Suffixed form “pel-ko- probably in Ger- manic *falkén-, falcon (< “gray bird”), in: a. Old French girfaut, gyrfalcon: GYRFALCON; b. Late Latin falcé, falcon (but Germanic *falkén- is also possibly from the Late Latin): FALCON. 3. Suffixed extended form *peli- wo- in: a. Greek pelios, dark: PELOPS; b. o-grade form *poli-wo- in Greek polios, gray: POLIOMYELITIS. 4. Per- haps Greek pelargos (< *pelawo-argos), stork (< “black- white bird”; argos, white; see arg-); PELARGONIUM. [Pok. 6. pel- 804.] pel-3. To fold. 1. Extended o-grade form *polt- in Ger- manic *falthan, *faldan in: a. Old English fealdan, faldan, to fold: FoLD!; b. Old High German faldan, to fold: FALTBOAT; Cc. Germanic compound “*faldistélaz, “folding stool” (*stdlaz, stool; see sta-), in Medieval Latin compound faldistolium, folding chair: FALDSTOOL;
2114:POLICE pele-3 POLICLINIC pela-3 POLICY! pele-3 POLICY? deik- POLIOMYELITIS pel-2 POLIS pele-3 POLISH pel-6 POLITIC pele-3 POLITY pele-3 POLKA pele-2 POLLEN pel-1 POLLEX pol- POLLUTE leu-2 POLTERGEIST bhel-4, gheis- POLTROON pau- POLY- pele-1 POLYGALA melg- POLYGLOT glégh- POLYGYNY gWen- POLYHISTOR weid- POLYMATH mendh-! POLYNYA pele-2 POLYP ped-1 POLYPNEA pneu- POLYPOD ped-1 POLYTECHNIC teks- POLYTENE ten- POLYTHEISM dhés- POLYTOCOUS tek- POLYTROPHIC threph- POMACE pomum POMADE pomum POME pomum POND bend- PONDER (S)pen- PONDEROUS (S)pen- PONIARD peuk- PONS pent- PONTIFEX dhé-!, pent: PONTIFF pent- PONTIL peuk- PONTINE pent- PONTOON pent- PONY pau-
```


## [2026-09-14T00:51:38.238Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_03 leaves around p804-807\"; python3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nprint(len(lv))\nfor n in (38,39,40,41,42,43,44,45):\n    s=lv[n][:300].replace('\\n',' | ')\n    print(n, s[:250])\nEOF"
}
```


### [2026-09-14T00:51:39.367Z] TOOL RESULT

```
=== POK_03 leaves around p804-807
430
38 j  f.  Verkauf;  ahd.- fäli   ,verkäuflich,    feil'    {*pelio-),    aisl.  fair   ds.   (*poZo-);    ahd.  feüi^  mnd. veile,  afries.  fei  ,feil'  sind  nicht  verwandt; | lit.  pelnas  , Verdienst,  Lohn',  pelnaü,  -yti  , verdienen',  peldeti 
39  als  Ableitung  von  pele ,Maus'  auch  lit.  pelekas,  lett.  peleks  , mausfarbig,  fahl,  grau';  lit.  peleda, lett.  pe^leda  ,Eule'  (,Mäusefresserin') ;  von  einem  *peU  , Schimmel'  stammt  lit. peU-jUj  -ti  ,schimmeln',  peUsiai  PI.  , 
40  plan  , Ebene,  Prärie',  sloven.  plän^  f. plana  ,frei  von  Baum  wuchs',  pldnja  , offene,  freie  Fläche',  skr.  planina ,Bergwald'  usw.; | hierher  —  etwa   vom  ziellosen   sich   Ausbreiten   weidender   Herden  —  ^t gr.  TiXdvog  ,irr
41  ,inflexus';    ablaut.    gall.   olca    , Brachland',   ags.  fealg^   bair.  falg ds.,  russ.  polosd  , Abteilung  eines  Feldes,  Streif. WP.  I  516. | pelpO'  oder  polpo-  ,aus  Brettern,  Holz  gezimmertes'? | Ai.  parpd-  (Lex.)  ,Bank  od
42  weist  nicht  auf  idg.  v);  litpenkz  (flektiert);  ^ aksl.  peth  5  (<  aus  kt  nach  dem  Ordinale;  ursprüngl.  kollektiv  =  a.!. pankH-^ ,Fünfzahl',  aisl  ßmt  f.  , Anzahl  von  fünf';  auch  umbr.  puntes  wenn  ,qui. niones');  toch.  A
43 ch,  streben,  gehen,  eilen'  =  ags. fundian  ds.,  ahd.  funden  ds.,  aisl.  füss  ,geneigt,  willig',  as.  ags.  füs ,schnell,  eifrig,  willig',  ahd.  funs  , bereit,  willig'  (^*fund-sa-)  norw.  füsa ,schnell  laufen'; | aksl.  pgtb  usw. 
44 r'. | A.  Dient  als  Präposition,  Präverb  und  Adverb: | a.  per,  peri  (Lokative  des  Wurzelnomens)  , vorwärts,  im  Hinausgehen,- Hinübergehen  über,  im  Durchdringen,  im  Übermaß',  woraus  ,über  —  hinaus,' durch  —  hin'; | ai.  pari,  
45 mel)',  paru§-  n.  ^Knoten, Gelenk,  Glied' ;  gr.  TtsiQag  , Knoten^  ist  unsicber  (G.  Björck  Mel.  Boisacq 1,  143  ff.). | b.  Adj.  pero-s  , ferner':  ai.  pdra-h  ,ferner,  jenseitig,  Feind;  früber; später',  Superl.  paramd-h  ,fernste
```


## [2026-09-14T00:51:56.110Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nprint(lv[38][-2200:])\nEOF"
}
```


### [2026-09-14T00:51:57.351Z] TOOL RESULT

```
arm.  alik''  ,die  (weißen)  Wellen ;  weißer  Bart^  weißes  Haar'  (*plno-)i gr.  TtsXLzvög  ^grau^  (für  ^TteXirög  ==  ai.  palitd-h  nach  dem  Fem.  *7T€XLrvia =  ai.  palikrii) ;  ion.  neXidvög  daraus  nach  {j,ay,sövög  usw.  umgebildet ;  n:sXt,6g (*peli-uo-)  ,farblos,  bleich,  grauschwarz,  schwarzblau'  (hierher  der  PN TIsXoxp),  neXXög  ds.  {*7isXi6g?  *7isXv6g?)^  noXiög  ^grau,  greis^  (*poli-uO'), TtiXvov  (paiöv  KvTTQioL  Hes. ;  niXsLa,  TteXeidg  ,wilde  Taube'  (nach  der  Farbe  be- nannt, vgl.  TteXsLai,  TtsXeiadsg,  eig.  die  grauköpfigen,  alten,  als  Bezeichnung der  Priesterinnen  in  Dodona  sowie  neXstog  ,Alter^  Hes. ;  ebenso  lat.  pa- lumhesj  apr.  poalis  , Taube'),  rteXaQyög  , Schwan'  (,der  schwarzweiße'); aus  '^7ieXaf{o)--]raQy6g)  maked.  iteXXrjg  ,,i;scpQ(bdrjg''  Hes.;  wahrscheinlich hierher  auch  rtrjXög,  dor.  TtäXög  {*7taXa6g)  ,Lehm,  Schlamm,  Kot,  Morast';
805
lat.  fCL^^^^j  '^'^^  ;blaß  sein',  pallor  ^Blässe^^  palUdus  ,blaß^  (zunächst  aus toaluos,    älter  *poluos  =  gerra.  falwa-,    lit.   paivas,    aksl.  plav^)]  pullus
jj^arzgrau'  («Z  aus  l  infolge  des  anlaut.  j9- ;  Formans  -wo-);  palumbes 'der  -i5  ;Holz-,  Ringeltaube^  (*pelon-hho-?  eher  Parallelbildung  zu  columbus, .a,  s.  oben  S.  547);
alb.  ^^«^  ,Greis^  Ältester';
mir.  liathy  cymr.  (usw.)  llwyd  ;grau'  (aus  '^pleito-,  vgl,  ai.  palitd-,  gr. ;csXtTy6g) ;
o-erin.  *falwa-  in  aisl. /^Zr^  ags.  fealo,  sls.  falu,  ahä.  falo,  falawer  ^fahl, falb^  (dazu  als  ;,graue  Asche'  aisl.  fglski  m.,  ahd.  falawiska  , Asche, Aschenstäubchen');  *fal}ia-  (:  lit.  pdlsas)  in  aleman.-rheinfränk.  /aZcÄ falb;  bes.  von  hellbraunem  Vieh' ;  *fela-  oder  *felwa-  in  westfäl.  f^l  ,iaXh', f^U  , fahles  Reh,  fahles  Pferd' ;  mit  dem  germ.  /:-Formans  wie  in  anderen Vogelnamen  hierher  vermutlich  ahd.  (usw.)  falco  , Falke'  (spätlat.  falco aus  dem  Germ.);
lit.  palvas  , blaßgelb'  (=  germ.  ^falica^  lat.  palU-dus)  =  abg.  plav^ ,weiß',  serb.  plüv  ,blond,  blau';  lit.  pell  ,Maus',  lett.  pele  ds.,  apr.  jpeles PI.  ,Maus  (=  Armmuskel)',  apr.  pele  ,Weihe';
```


## [2026-09-14T00:51:58.957Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN pir\"; grep -n -i \"p[iî]r\\b\" HRN.txt | head -20\necho \"=== HRN parsa\"; grep -n -i \"pârsâ\\|parsa\\|pärsä\" HRN.txt | head -20\necho \"=== HUB\"; grep -n -i \"\\bpir\\b\\|parsa\" HUB.txt | head -20\necho \"=== PHD\"; grep -n -i \"^pīr\\|pīr \\|pyl\\|pārsāy\\|pārsā\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-14T00:51:59.044Z] TOOL RESULT

```
=== HRN pir
2811:^) Kurd. pUr konnte dazu verführen, in np. pir 'alt, Alter* eben-
2814:eine pir ergebende Oontraction aus paruviya' sehr unwahrscheinlich ist.
2818:Bartholomae (briefliche Mitteilung) nimmt für np. pir als
3101:kurd. per^ pir, pird, purd, pel (H.-Sch.); af/. LW.
4835:d(i)blr (Inschr.); arm. LW. dpir^ talm. ^''Dl, daßtiQ
13381:pirärsäl 351.
18672:8. pir 318.
=== HRN parsa
2963:^) Die Annahme , dass np. pärsä 'enthaltsam , fromm*, aus
2965:115, NB. ohne Stern) contrahirt sei, ist durchaus unstatthaft. Pärsä
13310:pärsäl 270.
18774:K. reparsad 299.
=== HUB
492:vergleicht mit Recht phi. aparsar (= auf dem Kopfe'
1311:299. Np. pursam = ap. prsamiy (nicht parsamiy). Die
4036:lich nur der Dialekt der Provinz Persis (ap. Parsa-)^ viel-
10654:pir 38, 131, 146.
=== PHD
PHD.txt:321:ë ру | (M hyb)] particle giving the present tense optative sense. é, v, éd, éw. ēbāraģ [*dyp'lk', ^dwlk! | N éwàr] evening. ébgat(ih) ['ybgt!, -yh = Av. aifi.gati-] (onslaught of) Evil; the Adver- sary. ēbsrūsrim [>ур-, ?ybslwslym = Av. atBisrūdrima-) the gah from sunset to midnight. ébyünghan [>ур-, ?ywby?nghn!, etc. = Av. aiBydshana-] sacred girdle, = kustig. ёё Pye | (P ?ушус), N héc] (with a negative) not any. ēčand, v. éw-Cand. éd (HN A < A hr? | M? yd] this; v. dāštan. ~ ray ёё [cf. N z-é-rá] because, since. édar [LTME < À I-tnh | M?ydr, N ~] here. édin [ytwn'! | N ēdūn] thus, so. ~ih: (correct) manner. ëg [ADYN' < А *dyn | М ?yg] then, thereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix forming present participles. -én-idan [-yn-ytn' | M -yn-ydn, (N -àn-)] suffixes forming causative and transitive denominative verbs. *énókén Pynw(k)kyn' = Av. *aēnē.kaēnā-) heiress (under the obligation of continuing her father's line). enya рулу | (M ?n’y)] otherwise, moreover. lër [d] | M Zur, v. azér] down, below; low; under. — ud abar: upside down. tēr Pyl] noble; hero, ~ih: nobility, good conduct. Eran [y”x! | N ~] Eran, (land of) the Aryans. ~ag [-k'] an Eranian, Aryan. érang [”y/ng] blame, condemnation; error, heresy. ~ih: = érang. éranj-, v.  * éraxtan. Ērān|-šahr (yPnitr! | N ~] land of the Aryans. —-wëz [-wyc] (original) home of the Aryans. 1ёгахќап, ёгапј- Pylhtn!, ?уЇпс- | J ?yrxt] blame, condemn, damn.
PHD.txt:323:2ēraxtan, ёгапј- Pylhtn', *ylnc- | M ‘yrxt, ( yrnz-)] fight, dispute. éraxtür [y/At? 1] warrior. ēr-kaš ['dik£ | M *yrkš] (hands under the armpits in respectful) salutation, greeting. 1ërmán [?y/mx! | (MÉÁry! mwn), N ~] friend; а god. — ih: friendship. 23ër-man(ag) ['dim?n(k)'] humble. ēr-menišnīh [dimyninyh] humility. ér-tan ['ditn!'] humble. ~ih: humility. ērwār [D yleo?1] befitting a hero. ērwāraģ [*dlw?Ik! | J ?rw’rh] jaw, cheek. ésm ['ysm] = ézm. esp", v. sp”. éstádan, ést- [YKOYMWN-tn! < A ygym, У gum; ?sttn!, *zost- tn! | M ‘yst-’dn, N ~] stand; be, continue (as auxiliary of the perfect con- tinuous tense). ~išn: permanence, lasting, dwelling. ēš Pys | N xéf] plough. efm, v. $n. &(w) [z; HD < A hd | M ‘yw, N -ēļ a, one. éwan [*dwn') stalk, trunk. ēwān ['dw?n!] bridle. éwar ру! | J ?yf?r] certain(ly), assured(ly). éwarz [dwlc] movement. éwarzidan, éwarz- ['dwlc-ytn!] move, travel. éwarzig ['dwlcyk!] moving. 1&wáüz [?уш?с] word, utterance. tēwāz [?уш?с] sole, only. ~ig [-yk'] particular, individual. čw-bār Duech?) once. ē(w)-čand D у(то)спа] some, a few. éwén Pdwyn' | M *ywyn, (N àyin)] manner, custom, form, propriety. pad —: properly. léwénag ['dwynk! | M *ywyng] = ëwën ; v. ёё-. Ў *éwénag [?*dwynk! | (N āyīna)] mirror. Set (ъд) yn k éw-kard(ag) ['ywkrt(k)', -kltk'] united, joined. ē(w)-mēg D»(zo)mtok!] wearing (only) one shoe. éw-sün Pywsn' | (N yak-sān)] uniform, (a)like. ^ Ah : uniformity, likeness. éw-tüg Pywt?k' | М ‘yw 12, (N yaktà)] alone, single, individual. éz-, v. yaz-. —išn [уст] worship. ézm [CY BA < A syb | N hëzum] firewood, fuel. ged Zm4
PHD.txt:353:frazām-pērēzīh [p/c”*m pylwcyh] final victory.
PHD.txt:549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
PHD_mackenzie.txt:770:aber ['pyl] very, much.
PHD_mackenzie.txt:1312:aweran ['wyl'n l , )pyl'n l I N weran] desolate, ruined.
PHD_mackenzie.txt:2371:frazam-perozih [plc)m pylwcyh] final victory.
PHD_mackenzie.txt:4163: payrayag [pyl)dk' I M pyr)yg, N periiya] ornament, adornment.
PHD_mackenzie.txt:4197:peroz [pylwc I M pyrwz, N --] victorious.
PHD_mackenzie.txt:4199:perOzgar [pylwckl IN....,] victorious.
PHD_mackenzie.txt:4206:IpeAag [pylk l I N pesa] trade, craft; guild, caste.
PHD_mackenzie.txt:4217:pes-gah [pylg)s IN....,] audience chamber; foremost seat.
PHD_mackenzie.txt:4223:pesyar [pylk) I I N --] urine.
PHD_mackenzie.txt:4235:pil [pyt I M pyl, N --] elephant; (chess) bishop.
PHD_mackenzie.txt:4238:pillagan [plk)n I M pylg, N ......]steps, ladder.
PHD_mackenzie.txt:4242:pir [pyl IN ......] old, aged, ancient.
PHD_mackenzie.txt:5310:weh [SPYL < A spyr; wyh I M why, wyh, N bih] better, good.
```


## [2026-09-14T00:52:04.029Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 2795-2830\"; sed -n '2795,2830p' HRN.txt\necho \"=== HRN 2950,2980\"; sed -n '2945,2985p' HRN.txt"
}
```


### [2026-09-14T00:52:04.087Z] TOOL RESULT

```
=== HRN 2795-2830
285. pulten 'kochen, Praes. pez-em^ pezamden,
g. pa/tmün, P<^yß (= np. ptixt^) ; Käs. patSn, pa^te-
man; mäz. pa/ta,
aw. skr. [/^pac- 'kochen' ; phlv. pu^tan^ pazem, pazBt
(PPGl.), pazämlnUan (Bund., Men.).
kurd. patin 'kochen', bepiz; afy. pa/avul; oss. d. ficun^
t.ßcin (291) (?) ; bei. pacag, n. pasay (276) ; wa;t'- pöcam,
si/n. sar. pSzam (LW.); arm. LW. apu/t 'roher
Schinken'.
286. pider (peder) 'Vater'.
Käs. pei (aus ped),
ap. pitar- 'Vater'; aw. pitar-; phlv. pit, pitar (in
"inlON), P(i)tar\böxt N. pr. (Kanheri-Inschr.j; ai.
pitar- ; arm. hair 'Vater* (H. No. 155).
kurd. pier^) 'Vater'; af;'. plar\ oss. d. fidä, t. fid
(283) ; bei. pit n. pis, pid- (296) ; siyn. ped, sar. pit.
^) Kurd. pUr konnte dazu verführen, in np. pir 'alt, Alter* eben-
falls ein ursprüngliobes pitar- zu suchen (über altes, durch doppelte
Lautverschiebung zu y werdendes t vergl. s. v. mäye, No. 970), zumal
eine pir ergebende Oontraction aus paruviya' sehr unwahrscheinlich ist.
Plr findet sich jedoch bereits im Pehlevl, und die Bedeutung *alt* ist
dort schon so fest, dass an eine Ableitung von pitar- auch abgesehen
von der Seltsamkeit des i, nicht gedacht werden kann.
Bartholomae (briefliche Mitteilung) nimmt für np. pir als
Grundform ein ap. *pariya- an und vergleiclit zur Bedeutung ai.
puränd'^ skr. purcUana-,- 65 —
Die Form pid könnte man bei FirdüsT an den Stellen
einsetzen, wo nach peder keine Izäfe steht (vergl. pus) ;
sonst kommt sie neupersiseh nur in den Patet's vor.
287. pidräm 'schön, fröhlich' (Sahn. III, 1803, V. 372).
aw. *2)aiti.raman' ; vergl. np. räm (No. (504).
288. pedrad 'Heil, Lebewohl*.
phlv. pa i]^t) + drüt (Nöldeke, Kam. 65).
Vergl. np. durüd (No. 555).
289. pedJd 'sichtbar.
phlv. pa du {^\y\rr^^\ ps), Nöldeke, Karn. 40; also
=== HRN 2950,2980
Dann perwez.
308. pervfn 'Plejaden*.
aw. paoiryaeinyas\ca (yt. 8, 12), de Lagarde, Beitr.
z. altb. Lex. 56.
af/. peröne; bei. panvar 'Plejaden (Dam es, 54).
309. perhey(ten 'sich enthalten ; sich hüten', Praes. perliez-etn^
perhez, perheztden^).
aw. palti + [/ra^c- 'verlassen'; phlv. pahre/tan
'sich enthalten', pahrej, pahrej(i)sn.
kurd. pärlstin, dispärise 'ist enthaltsam, enthält sich*.
^) Die persischen Original Wörterbücher geben für hervär (No. 210)
und pervär (die de Lagarde schon geschieden hat) zusammen die
folgenden Formen an : pervär^ perräre, perbär, perbärff perbäl, perbcUe^
fervür^ ferväre (vergl. No. 82S)^ fet'väl^ ferväle . von denen die mit/
beginnenden in dieser Bedeutung gewiss falsch sind. Als Beleg für
die Bedeutung *Stall* dient ein Vers des Xäqänl (Metrum: Munsarih).
röz^ beperrär^ büd^ färbe ez an sude cünin
seb tSn-t himär^ däst läylr ez an sude dun an
^) Die Annahme , dass np. pärsä 'enthaltsam , fromm*, aus
*perhezä (eine solche Form construirt sich Darmesteter, Et. ir. I,
115, NB. ohne Stern) contrahirt sei, ist durchaus unstatthaft. Pärsä
bedeutet überhaupt nicht 'enthaltsam', sondern ursprünglich nur *brav*
(vergl. Sahn. I, 35 Vers 15, 70 Vers 158 u. o.), es bezeichnet gewiss
eigentlich den Pärsen.— 69 — '
810. perl 'Perl, guter Genius*.
aw. pairlkä' *Hure'; phlv. parlk, arm. LW. parik,
LW. af/. parT.
Nach Bartholomae, BB. 15, 9 ist die SiW. pairikä-
ursprünglich *die Fremde'.
811. perer Vorgestern, perejröz, pere\seb.
Kilo, perc; pere]sdl, pe7^i]söUf per]sew^ pörijsd.
aw. '^parö.ayare; phlv. parer.
kurd. picne (Houtum-Schindler), per; oss. vergl.
fal'iväre 'im vorvorigen Jahre' (274, 2); bei. parerl^
paireri^ n. paln (285).
812. piSmanj pemän^ ptizmän (8ähn. I, 359 Note 2, Calc.)
'bereuend', pesiman,
ap. patü r *wawc/- ; phlv. pasTmän (paz. pasemän) ;
ai. /)ra^^ -i- y/'yw^w- 'erwiedern, entgegenhalten'.
Die Entstehung der Form pesJmän ist ganz unklar ;
piz'' scheint aber sicher auf patis hinzuweisen. Der
```


## [2026-09-14T00:52:07.031Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD parsa\"; grep -n \"p?rs\\|parsay\\|pārsāy\\|pʾlsʾd\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB\"; grep -n -i \"pārsā\\|parsay\\|pīr \\|pyl.*old\" NYB_vol2_glossary.txt | head -20\necho \"=== HUB 38 131 146 context\"; grep -n -i \"pir\" HUB.txt | head -30"
}
```


### [2026-09-14T00:52:07.112Z] TOOL RESULT

```
=== PHD parsa
=== NYB
=== HUB 38 131 146 context
4:It has survived long enough for the copyright to expire and the book to enter the public domain. A public domain book is one that was never subject
5:to copyright or whose legal copyright term has expired. Whether a book is in the public domain may vary country to country. Public domain books
364:away evil spirits, or as a charm'.
890:Nebenform zu piring, die Horn nicht erwahnt. Zu
891:ihr stimmt kurd. pirinjok = birinj *bronze' (Justi-
1134:np. pill ^Briicke' = gel. ptird^ kurd. pird, purd^ pel
1522:351. Np. pirdr *das vorvergangene Jahr = ap. p{a)ruviya-
1530:auch die moderne Aussprache: np. pirahdn *Hemd,
1539:(NOldeke, Tab. 117), lat. piroses (Ammian).
2083:540. Arm. dpir setzt phi. diplr voraus und macht mir
2234:579. Dazu auch np. d4ida ^Pamilie' Pird. I, 453, v. 334.
3980:wandelte und die ar. aspirirten Medien {bh, dh u. s. w.) zu
3981:Medien {b, d u. s. w.) , die ar. aspirirten Tenues {ph, th
3983:u. 8. w.) zu tonlosen Spiranten (/, d^ u. s. w.) wurden, ging
3996:Dazu kamen vielleicht noch die tonenden Spiranten ^)
3998:und aspirirten Medien) nach Vokalen in tonende Spiranten,
4030:nisohe Grundsprache tonende Spiranten {w^ S, y^ i) an, Usst sie aber
4031:nur aus den arischen aspirirten Medien hervorgehen.
4594:impf. agrbaya); ptr alt' = ^piry- = *pirvy- = ^pxvya-
5102:vgl. bal. miray, ptc. murfa); ptr 'alt* aus *piry- = *pirvt/-
5322:aus alterem spirantischen y, Vgl. § 55.
6246:gut, sch5n' = skr. suvapufi-; dibtr 'Schreihev = arm. dpir;
6269:und syr. nur "lIDlfi? (seit dem 4. Jhd.), lat. Pirisabora Am-
6349:Pehlevi, wurde spater zur Spirans w, die im Pazend und
6367:die Geltung von Spiranten (= w, J, y), im Anlaut und
6477:ist b (Verschlusslaut) geblieben, ap. b ^= tv (Spirans) nach
6478:Vokalen blieb im Mittelpersischen als Spirans w^) und
6655:Spirans und t erst nach Vokalausfall zusammengekommen
6938:durch np. zard gelb*, zarda *das Gelbe* (des Eies) Pird. I,
7024:Spirans J und wurde im Paz. und Np. zu h oder y = i.
```


## [2026-09-14T00:52:29.955Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD grep p.rs\"; grep -n \"parsa\\|p[aā]rs[aā]\" PHD.txt PHD_mackenzie.txt | head\necho \"=== PHD page around parsang\"; grep -n \"parrag\\|parsang\\|parwardan\" PHD_mackenzie.txt | head\necho \"=== NYB parsay\"; grep -n -i \"p.rs.y\\|pyr\\b\" NYB_vol2_glossary.txt | head -20\necho \"=== CHEUNG pel/parya\"; grep -n -i \"parya\\|pārya\" CHEUNG.txt | head"
}
```


### [2026-09-14T00:52:30.070Z] TOOL RESULT

```
=== PHD grep p.rs
=== PHD page around parsang
4045:parrag [plk , plg I P prg, N ,....,a] wing.
4063:parwardan, parwar- [plwl-tn l I M prwrdn, N ......] foster, nourish,
6162:carriage wardyun.                       cherish parwardan.
6481:educate frahixtan, parwardan.                entrust abespurdan, gumardan.
6656:foster parwardan, parwal-.                   gain handoxtan.
7186:nourish parwardan, parwal-.                padiragih.
7945: weapon zay, zen.                       winged parragig, parrwar.
8626:frasp                        ~Cl)          parwardan                    \\~~Q)
8636:frazanag              \9""~eu              parrag                      ,~eu
8660:parwangah               -6"'U ~ ~ C2)    parragig                      \~Q)
=== NYB parsay
1855:ham-pursakéh [hmpwrskyh] deliberation, consultation, conference, dialogue, esp. of the meetings of Zartuxšt and his a- pocalyptie sons with Ohurmazd and the revelations received by them on these occasions: 4714, 514. 54%. 5717. 968-10, 989, 9910.12. in another context ~ kartan 1061. — SGV IV, 6 hampursai. Skr, v. anyonya-prasnatä.
2903:pairäyak [pdPdk'] adornment 664. — < *pat-rädak, v. the preceding w.; MPrs pyr'yg (S).
3118:*pērāvanihīt [pyr'wnyhyt] pass. pt. *stirred up: apt-š hamäk damik... — kart and he (the Wind) stirred up the whole soil 3316-17, — Reading hypothetical. I derive it from pari + d + van-, OP van- ‘to throw, to spread out’, v. Ben- veniste, BSL XVII, 1951, 25-26 (differing from Kent).
3492:(cf n. pr. %m10pa-6d77g). Henning identifies it (List 81; JRAS 1942, 239sg.) with MPrthPrs ‘spyr (= esper) which accord- ing to him is borrowed from Gr ogatp«. However, in this case -h- in spihr would be an inorganic insertion, which is quite improbable. Of course, the sense of spihr may have been influenced by ogaip«, but its formal independence is proved by NP sipihr which belongs to the living language. ��� As to the alternation -ih- : -ah- cf s. v. mahmäneh.
5553:‘spyr: spihr
5857:‘spyr: spihr
6106:pwlwd: polavatčn pwr: purr pwrsydn: pursitan pws: pus pwst: post pwšt: pušt py'dg: padatak pyd, pydr: pit pyd’g: paitak pyg: padak pygm: paitäm pym’n: patmän pymwen: patmöcan pymwxtn, pymwe-: patmöxtan pyr’yg: pairayak pyrwz: péroz pyšwb'y: p&söpäi pyšyn: pēšēnīk Pyš, pyšyy, pyšyh: pēš pyw’c-: patvac- pywn: patvand pywst: patvastan
=== CHEUNG pel/parya
8310:dressed’ || (+ *pari-) Sh. (Baj.) paryand-/paryust ‘to put on a dress, be covered (with 
8319:*MISC: (+ *a-) Par. ayun-/ayust- ‘to dress, put on’ || (+ *рап-) Orm. paryan-/ 
8320:paryanök ‘to dress oneself = porgon-/porgonók 
48262:paryand-/paryust, 114
```


## [2026-09-14T00:52:31.486Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY pir\"; grep -n \"پیر\" incoming/ARY/ARY_pages.txt | head -20\necho \"=== ARY parsa\"; grep -n \"پارسا\" incoming/ARY/ARY_pages.txt | head -20\necho \"=== ARY barut\"; grep -n \"باروت\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-14T00:52:31.575Z] TOOL RESULT

```
=== ARY pir
264:می‌شوند و زبانهای پیرامون بیشتر محافظه کارند و دارای واژه‌های کهن تراند. مثلاً زبان فرانسه‌ی رایج
266:در ایالت کبک در کانادا (یک زبان پیرامون) از زبان فرانسه‌ی رایج د رکشور فرانسه کمتر تغیی رکرده
268:حاشیه یا پیرامون حاوی واژه‌هابی هستند که قبل از خروج از گهواره جزو زبان هند و اروپایی
583:بودن واژه‌ی بازمازی شده را نشان دهند. (درکتاب حاضر نیز از این رسم پیروی شده است). . "
586:دیگر از زبانشناسان معتقدند که واژه‌های بازسازی شده با پیروی از اصول اثبات شده‌ی زبانشناختی و
922:پیروزی. ۳- بکار بردن نماد حیوانات وحشی (به ویژه گرگك) بعنوان نشان و عامل الهامبخش. ۴-
1089:ابدی بود. آنان با پیروی از آرمان‌های ی که در صدر آن جوانمردی و مروت و شجاعت قرار داشت در
1311:ررش معمول برای ربثه‌یابی واژه‌ها ( که در این کتاب نیز از آن پیروی شده) چنیناست؛ رب
4514:۲- واژه‌ی اوستایی از دو اجريشه درست شده است: ۳۸13 (به چم "دور" و "پیرامون") و 3۸122۸ (به چم "آدیوار»)
4793:۸۰ با ۳۸۲۸ به چم "اطراف" "پیرامرن) ۲- ۷۸2۸1771 یا ۷۸ (به چم "پریدن)
5386:دکتر محمد معین (به پیروی از نیبرگ) ریشه‌ی اوستایی این واژه را ۸0 ريشه‌يو پهلری آنرا
9069:مرحوم معین در پانوشت برهان فاطع: (و به پیروی از آنیبرگ" و "هوبشمان") واژه‌ی رفتن را از واجریشه‌ی هند و
9314:۱ زار (به چم "نحیف و ضعیف "» "پیر)» زال ۳۱۷1
11663:چم این واژه در زبان لیتوانی و لتونی؛ پیروی کردن» رهبری کردن.
12537:چم این واژه در زبان سانسکریت: پیری
14023:چم این واژه در آلبانی؛ پیروزی. :
=== ARY parsa
=== ARY barut
```


## [2026-09-14T00:52:38.574Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nprint('leaves',len(lv))\nfor i,p in enumerate(lv):\n    if 'باروت' in p:\n        print('--- leaf',i, p[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T00:52:39.671Z] TOOL RESULT

```
leaves 777
--- leaf 138 مقدمه صد وسی و تثری‌تا لیف کند ده‌ها سال تتبم وتحقیق واستغراجلغات ازمتون نظم و ن
--- leaf 292 مگ بر آن قبر میهد ٩‏ - د الم خخضصی که کاتای شا تلاح هو : آ یر هیمیه - مخنف ابراه
--- leaf 352 باشد ٩‏ - و بلفت زند و پازند (۱) بمعنی مینه است که جربی صدر خوانند ۴ . اسیر لگ -
--- leaf 416 و چون کل آن زرد و سفیدو کبود میباشدبنایر آن ایرسا نامیده‌اند چه شبیه بقوی‌فزح اس
--- leaf 436 با خوانند و آنراکبوتر بیار دوست دارد . 9 پاار لك - بکر تاكث و سکون کاف ؛ مشفف با
--- leaf 712 آر قنج» بر وزن شطرنج , راه باريك ودشوار را گویند ۵ . آر نك ۱ » بروزن‌فزند » بممن
--- leaf 771 4۳و تبر تظلم ه کنابه از آ, مظلومان باشد . تیرچرخ - "تیه از کرک ساره است - و چیزی
```


## [2026-09-14T00:52:39.910Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nhits=[i for i,p in enumerate(lv) if 'پیر' in p]\nprint('pir leaves',hits[:40])\nEOF"
}
```


### [2026-09-14T00:52:40.835Z] TOOL RESULT

```
pir leaves [12, 13, 16, 32, 71, 90, 92, 97, 112, 115, 169, 170, 183, 245, 246, 247, 248, 252, 273, 286, 294, 295, 415, 420, 426, 466, 480, 481, 489, 492, 520, 522, 534, 544, 562, 573, 589, 590, 603, 607]
```


## [2026-09-14T00:52:48.008Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\np=lv[436]\nprint(p)\nEOF"
}
```


### [2026-09-14T00:52:49.216Z] TOOL RESULT

```
با
خوانند و آنراکبوتر بیار دوست دارد . 9
پاار لك - بکر تاكث و سکون کاف ؛
مشفف باريك است که در مقاب لکنده باشد .
بار گاه - بروزن‌چار گاء.خیم‌پادشاهان
و سلاطن را ااگو, بند وجای رخصت واجازت‌باشد
و شکم حیوانات ماده را هم گویند .
باد گی » ختح ثاك بر وزن خانگی .
نوعی از اسب باشد » و بعضی اسب بالانی‌بار کس
,اگفته‌اند ٩‏ - ویمعنی قدرت ونوانایی هم هت
و روسییی و قععبگی را ايز گویند .
اد گیر - با رابم بتحتالی‌رسده وبراق
فرشت‌زده ۰ اسب و شنر وامثال آن باشد ازبرای
بار تردن و سواری و ارت مکی دادن ۴ -
و هودج و عماربرا هم کقنه‌اند - وماد#هرحیوانی
را نیز گویند .
بار گین » بکر رابم وسکون تحتانی
و اون » آبگر و تالابی را کوبند که در عبان
شهر و ادرون ده باشن - و جابی را نز گفتهاند
که زیر آب حملم ر مطخ و امثال آن در آن
جمح شود ۴ .
بار مان - بر وزن آرمان » نلم‌یکی از
بپلوانان ئوران است .
تجمل و حشمت و بزرگی باشد - و حنت نهادن
بر کسی - و پروانه وفرمان ورضا و رخصت‌دادن
باشد بدخول خانةٌ سلاطین - و بمعنی نازش
و مباهات - و لقب‌نيك وتفاخر + غرورهم‌هست
و بمعتی مدح و نعت هم بنظر آمده است.
بار نهادن - کنابه از زادن باشد .
بارو عه بر وژن جارو » حصار و قلمه را
گونتد . #۶
بارو د بادال » بر وزن و ععنی‌باروت
باشد که داروی تفنگه است: و بلخت سر بانی‌شوره
را گوبندکه جزو اعظم باروت باشد و آنرا نمك
چینی هم گونند ۴
بارود نه - بتح نات و زای هوز
و ون و سکون رابع » نلم فواٍبیست از موسیقی .
باروده » با زای حوز بر وزن پالوده.
خوراك و فوت‌هرروزه باشد- و ضروری‌وها:<تاح
هر روزه رانیز گویند از جامه و زبرجامه وامث
آن - و جامةٌ کهنه را نیز گفته‌اند .
بادوق » بر وزن فاروق ۰ بلخت رومی
باژه - بر وزن‌خاره ؛ دیوار و حمارقلمه
و شپر را کوبند ٩‏ - و کرت و مرنیت و خوبت
را نیز کفته‌اند - و بمعنی دوست هم آمده است
همچو: علام باره ,یمنی پسر دوست ۷ - و بمعئی
حق و شان هم حست چنانکه گونند : «درسارة
فلان؟ بعنی درحق فلان و در شان فلان‌سوبمعنی
۱ - ميي‌خو رکه مخشی زر و بلرکی
؟ ‏ زیان تنا گردر گاه مصطفی بهتر
۴ مثل ملك و ملك بوز کار
6 60۵56 دلك س۲۰۱*.
تست شهرت‌طلب و خسرو شاعزباره
۵ باروت ‏ رك : بارود .
/ بر هان فاطع ترا
```


## [2026-09-14T00:53:03.246Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nfor i in range(648,672):\n    s=lv[i].replace('\\n',' ')\n    print(i, s[:150])\nEOF"
}
```


## [2026-09-14T00:53:03.836Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:216 --image 2>&1 | tail -40"
}
```


### [2026-09-14T00:53:04.656Z] TOOL RESULT

```
648 کوند وآن دا گربه نز خوانند . نج هر لم» کیهی باشد خوشبوی باندام پنج انگشت - کویند مریم مادر عیسی علیه السلام در هنگام وضع حمل بر آن کیاء چسسلده بود* بن
649 اي وقطرة باران وقطر خون وامثال آن - و بععنی نقطه وذرات هم‌بنظر آمده است ۱ . ند یدن *ه بروزن خندیدن, صیحت کردن زصبحت پذیرفتن وصیحت شنیدن وقبول کردن باش
650 لذیو ۵» بر وزن خمیره » بمعنی پنیرگ است که آن را خبازی و مل و کیه و .نان کلاغ خوانند و شاب گردله را تنز گویند که است » و پنبر از آن جهت کویندش که میوو 
651 حه ی پا حس ۱ بو پل" با بای فارسی , بروزن و معنی ودر هندونتان با بر کک بان خور ند» ومعرب آن فوفل است. و وه با بای فلرسی بر وزن کوکو » شانه سر وهدحدرا ک
652 . بودان تروش فوفانی ورای بی‌نقطه وسکون واو وشن‌نقطه دار" نام ساحخری بوده که درزمان خود عثل و مائند نداشته ۷ . ۱ فوران دخت س من داد بی نقطه وسکون خای ن
653 4 ۷۲۷- ود یان - بکرثاك بر وزن‌حوربان» ۱ رای شهر کنوح۱ هم هست - و زای هوز » پبرامونو کردا کرد دهان حیوانات باشد - ومایین لب و بیتی را نیز گویندسوبم‌عنی
654 یوستین بگازر ۱ وعیب جوننده باشد ۰ (وستیی در بدن » کنابه از افثای راز کردن باشد . کردن. وعیب نمودن باشدا . که بر وقت رشتن مردوك محند. زره وجوشن را گوین
655 و پولاب بر وزن دولاب » بم‌نی حس باشد و پولاپی‌حسی, بعنی‌|نچه بحس ونظر درآ مد ۱ ۰ که از آن‌کارد و شمشیر واعثال‌آن سازند -وتیغ و شمشیر را نیز گویند - و 
656 4 بفتح اول وسکون ثانی » کلمه‌است که هنگام تصین با حیرتآمیخته برزبان رانن وتکرار نیز کننه؟ ۰ یاه » بر وزن بهانه . چوبکی باشد که درود گران درشکاف چوبی ک
657 4۳ اس ۱ بهلو صاییدن بهلو دادن کنابه از حثفت رسانیدن - و تردیکی نمودن باشد - و دوری کردن و کناره کزدن - و روکردانیدن را لیز پهلو داد - کی رااکوین که من
658 است که کنابه از برابری کردن در عال و فدر وهر تب باشد. هلو از دن» کنابه از گربختن ودو برنافتن- وترلك دادن و اجتناب نمودن و احتراژ کردن باشد . بهلو کند 
659 ی بهنا 4 بروزن مستانه , نوعی‌از میمون باشد- وکلیچةٌ روغنی را لبز گود . هنال بروزن کمند. دامی باشدکه‌بدان آهو گیر ند. (م ی و - بروزن فدفور » چیزیست مان
660 یاب وبکر او عخفف یه بات دکه درچراغ سوزند - وشمم تیز سلزند ۷ - یمیت بروزن سراب. بمعنی پاباباست که ین‌حوض وته جربا باشد وبعربی قمع رکوبند - وتهات عرچیز 
661 و۳ «« پیاهو - با های هوز بر وزن ترازو . هم عده است کهخالة شش بهلو 7 اری ماشد ٩‏ ۰ فیتا۵؟ - بانای قرشت؛ زد زن و معنی ت بلغت زند و بازند (۱). لیترسب؟ - 
662 تشن ولای‌هرچیز وضله حرشیتی را کوشد ازحیوانات پیتتن" -بروزن ربختن,بممنی پیچیدن باشف . ۱ یتخس" بروزن ک رکس . بممنی کمان بردن واز روی گمان فهمیدن وراه بچ
663 خافهای زیادن را عرد نی قلاف. ماهه 2 وبمعنی‌ساخدن ویرداختن ومنقح کردن- وچیزی‌را از عیب خالی نمودن هم هست . ثیر استو۱ « کم کردن چیزی باشد بواسطه زبابی و
664 پیراهن فبا کردن پیراستن وزینت دادن راگویند مطلقا- و دبافت کردن پوست را ه مکفته‌اند ‌# پیر آهی قبا کردن - کنابه از چا زدن و پاره کردن پیراهن باشد. پر ا
665 پیر فلا کنابه از کوکب زحل پیر كاخ - بکسر اول و سکون ثالی و فتح رای قرشت و نون ساکن و دا بی تفطه بالف کشیده و بخای نقطه دار زده » نیماج و سختیان را گوی
666 علت برص وجذام داشته باشده ۴. ودنه باثانی مجهول و دال بررزن بی سوزن » عبل نمودن و اراده کردن بطرفی باشد . لیسه ۴ » با ثانی مجهول بروزن کیسه » بمعتی سیا
667 تن پش باز و مواجه ویرابر و مقابل را یز کویند وکنابه ازدو لت م هست. لیشا نی ۵اد - بارال ابجد بالف کشیده و برای قرشت زده ۰ کي را گونندکه کاربرا بشکفتگی 
668 پیشواز است که بعربی استفبال گوبند و نوعی ازجامة پرشیدنی هم هست . پیش خاه - بسنی رواق است که بیشگاه خانه باشد - و ایوانی که در مرتبهٌ دویم ساخته باشند 
669 ۳و فیشگاه « باکاف فارسی بروزن ثیرماه» بیتی صدر- و صدر مجلس هردو آهده است - وفرشی‌را نیز گوبند که‌درپیش افکنند. وفرش یکه درپیش ابوان وصدر مجلس اندازند 
670 شطالی باشد .3 ی اد بایای حطی» بروزن وععنی بیشکار است ت که خادم و خدستکار اک رد ومزدور وش دست‌باشد ویمصی بیشاب و شاش هم هست که بمربی بول گویند- و قارور
671 وشرط را گونند ۳ لیتا- بکسر اول بر وزن جیفه » چوبی باشد بوسده در ولابت خوزسنان و آن را دای ی ۲ بکاربرند بمنی باستگه و چشماق آش درآن زننه 2 ییگاد ۴ - بن
```


### [2026-09-14T00:53:06.019Z] TOOL RESULT

```
no scan of BQT covers printed page 216 (see 'scans' in refs_online.json)
```


## [2026-09-14T00:53:14.800Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nfor i in (662,663):\n    print('======= leaf',i)\n    print(lv[i])\nEOF"
}
```


### [2026-09-14T00:53:15.953Z] TOOL RESULT

```
======= leaf 662
تشن
ولای‌هرچیز وضله حرشیتی را کوشد ازحیوانات
پیتتن" -بروزن ربختن,بممنی پیچیدن
باشف . ۱
یتخس" بروزن ک رکس . بممنی کمان
بردن واز روی گمان فهمیدن وراه بچیزی بردن
باشد .
سای ارل و تاك پر مك
- و چیزی که 9 فرم شده باشد -
و درمانده و عاجز شده را نیز کویند - و بمعئی
هی بست 4 دبوار ی که بیخ
ومحبری ومتحصن و کرفتاروبندی رانیز گفته‌اند
و بد بو و متعفن و گندیده شده را ه مگویند »
وبضم الث یز آمده است .
پیخسته ح بر وزن برجنه » بمعنی
زیر بای نرم شدم و عاجز ودرمانده - و محبوی
و گرفتار - و بد بو و متعفن - وکمان بردن را
- و در
زر کوسد ری ی رس اسر میتی
ره
بزور باشد ۰
بمعنی ترت ومرت وتار وعار و بفایده - وهرچه
از تف آش زرد وضایع شده باشد ِ#
ید اد بر وزن شداد ؛ بمعني بیدا
وظاهر باشد .
فيك او سی» بنتح واو و سین بی نفطه
بتحنانی کشیده . درمی که در زمان کیان رایج
بوده و هردرمی به‌ینج دینار خرج میشد, وبکسر
واو هم بنظر آمده ات :۷
پیر ؟ بروزن وه‌متی پدر |
اب گوند ۵ ۰
یر ا ۲ - با انی مجهول بروزن گیرا »
و سر تراش که موی زبادتی رابکند و باغبان که
؟ - در لغت فرس اسدی ( ص۳۹ )
اف ز چونن حقیر ومی‌هنی رد3
وتو
رك ؛ پشته .
" هز از وصد و شصت قنطار بود
که بر پپلوی موبد پلرسی
۵ درفارسی نیز
. کردی واففانی ۳3۲ .فی :
درم بد کزو پنج دینار بود
همی نامبردش به پیداوسی. فردوسی طوسی.
۴ کیلکی ۳66۲ .
۳۵۰
«2. ۲ص ۱۹6*.
4 یبدا
ابرانی باستان 0۵0۷263 ۵
۹ - ره ویزاسم
======= leaf 663
خافهای زیادن را عرد نی قلاف. ماهه 2
وبمعنی‌ساخدن ویرداختن ومنقح کردن- وچیزی‌را
از عیب خالی نمودن هم هست .
ثیر استو۱ « کم کردن چیزی باشد
بواسطه زبابی و خوش آیند کی همچو بربدن
ذاخهای زبادئی آزدرخت وموی زبادنی از بدن.
کوبند شبی اباز بامر سلطان محمود در حالت
مستی زلف خویش را بربد. روز دیگر سلطان
از آن حالت پریتان خاطر گفت. عنصری باین
رباعی سلطان را از کدورت بسرون آورد :
ر باعی
هنن زلف بت‌از کاسنن است
چه جای بفم نشتن و خاستن است
جای طرب ونثاط ومی خواستن است
کاراستن سرو ز پیراستن است.
سو دیاغت دادن چرم را نیز گویشد.
۳
بر استه؟ بروزن بی‌خواسته » به‌عتی
مرتب گردانیده و ساخته و پرداخته باشد -
و باغی که شاخهای زبادنی درختان آن را بریده
وعلفهای زبادنی آن‌را چده و صفا داده باشند -
و درخت ی که آن را پر کاوش کرده باشند » بعنی
شاخهای زیادتی آن را بریده باشند - ودهی را
معتی بابای ابجدهم بنظر آمده است.
نون و دال ابجد , ماضی متفرق ساختن
وافشاندن باشد بعنی متفرق ساخت ویریشان کرد
و افشانید ۰
یر آهن» با انی مجهول و میم بروزن
پیراهن» اطراف و کردا گرد چیزی را گونده .
پر اهون ,ائانی مجهول ومیم بروزن
طتطا کولنب. یفتتی مت امن انت. که ان ان
و گردا گرد چیز حاباغد ۵ ِ
لیر آن « بر وزن ابران » پهلوانی است
حشهور ازنوران وس گر افراسیاب بوده و بثر
او وسه تام دا ٩۰‏
پبر اهان با های هوز بر وزن
بی‌سامان ۰ پیراهن را کویند و بعربی قمیص
خوانند ۷ .
یر انهش* ۰ بکها بروزن‌یداش,
«اسشق ۰۳۵۲ پیراستن جانشن دومصدر پهلوی ۳۵1۳25028 (بمعنی زیت دادن) و ۷1۲۵620
(تراتیدن مو وغیرء) شده است واز همی‌رو در ادبیات قدیم فارسی معنی کاستن‌را حفظ کرده است
«از افادات استاد حنینگه» . ۴ - این داستان منقول از چپار مقالهٌ نظامی است. رك: چهار
مفالهٌچاپ لیدن ص ۳۹-۳4. ۴ - بهلوی۳86۲۵502. ۳ ظ, ممحف را کند»
رك : پراکندن . و تلفظ عامیانه هم تواند بود . ۵ در بهلوی 7 هم از جملهً
نیایش‌های خرده اوسئاییکی‌را «پرامون بشت» با «فرامون بشت» نامند و آن شامل دو نماز معروف
است که‌با «اشم وهو...» و «یتا اهو...»شروع میشود و شابد وجه نسميهٌ آن این باشد که این دو
نبایشگردا کردادعية دیگررا فراگرفته وهمهٌ نمازهاونباش‌هابااین دودعا احاطه شده‌است. «خرده
اوستا 454». بمعثی مذ کور در متن:
در میر ووزیر وسلطان را
۱ - همان متزل است اين جهان خراب
کجا رای پیران لشکر کشش ٩‏
بی‌وسیلت مگرد پیرامن. « کلستان ٩۳٩‏
که دیدست ایوان افراسیاب
کجاشیدهآن نرك خنجر کثش ٩‏
«حافا شیرازی ص ۳۵
۲ رد : پراهن . ۸ - تلفظی از «یبراش». رك ؛ بیراش.
```


## [2026-09-14T00:53:38.596Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nfor L in 662 436; do\n curl -sL --max-time 90 \"https://archive.org/download/borhan-ghate-v1/page/n${L}.jpg?fit=pad\" -o bqt390_n${L}.jpg -w \"%{http_code} %{size_download}\\n\"\ndone\nfile bqt390_n662.jpg bqt390_n436.jpg; ls -la"
}
```


### [2026-09-14T00:53:44.237Z] TOOL RESULT

```
200 527696
200 537986
bqt390_n662.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
bqt390_n436.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
total 1212
drwx------ 2 sfmqrb sfmqrb   4096 Sep 13 20:53 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    592 Sep 13 20:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 537986 Sep 13 20:53 bqt390_n436.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527696 Sep 13 20:53 bqt390_n662.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  55136 Sep 13 20:50 pg390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96039 Sep 13 20:53 pg394.png
-rw-rw-r-- 1 sfmqrb sfmqrb     40 Sep 13 20:53 queue.txt
```


## [2026-09-14T00:53:48.311Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nwhich convert magick python3; python3 -c \"import PIL; print(PIL.__version__)\""
}
```


### [2026-09-14T00:53:49.522Z] TOOL RESULT

```
/usr/bin/convert
magick not found
/usr/bin/python3
10.2.0
```


## [2026-09-14T00:53:53.375Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nconvert bqt390_n662.jpg -crop 2479x1100+0+2400 +repage -resize 1500x -quality 92 bqt390_662_foot.jpg\nconvert bqt390_n662.jpg -crop 2479x900+0+150 +repage -resize 1500x -quality 92 bqt390_662_top.jpg\nconvert bqt390_n436.jpg -crop 2479x1000+0+2500 +repage -resize 1500x -quality 92 bqt390_436_foot.jpg\nls -la *foot* *top*"
}
```


### [2026-09-14T00:53:54.961Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  95654 Sep 13 20:53 bqt390_436_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 124665 Sep 13 20:53 bqt390_662_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  93636 Sep 13 20:53 bqt390_662_top.jpg
```


## [2026-09-14T00:53:56.900Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt390_662_foot.jpg"
}
```


### [2026-09-14T00:53:56.922Z] TOOL RESULT

```

```


## [2026-09-14T00:54:10.871Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt390_662_top.jpg"
}
```


### [2026-09-14T00:54:10.893Z] TOOL RESULT

```

```


## [2026-09-14T00:54:16.444Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt390_436_foot.jpg"
}
```


### [2026-09-14T00:54:16.459Z] TOOL RESULT

```

```


## [2026-09-14T00:54:31.320Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nconvert bqt390_n436.jpg -crop 2479x400+0+150 +repage -resize 1500x -quality 92 bqt390_436_top.jpg"
}
```


### [2026-09-14T00:54:32.620Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:54:33.207Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD barud\"; grep -n \"بارود\\|باروت\" TAD_pages.txt TAD.txt | head -20\necho \"=== LKT barut\"; grep -n -i \"barud\\|barut\\|Schiesspulver\" LKT.txt | head -20\necho \"=== TTS barut\"; grep -rn -i \"barut\" TTS* 2>/dev/null | head"
}
```


### [2026-09-14T00:54:33.297Z] TOOL RESULT

```
=== TAD barud
TAD.txt:308:بارود - ترك « باروت »© وهو مأخوذ من 6ن1دادم الافرئسية أى غبار وقد 
TAD.txt:309:أطلقوه على الغبار الناري ومنه البارودة يتذف مها الرصاص والخردق 
TAD.txt:731:تفتكه - ترك وهو البارودة والرصاص الذي برى به ْ 
TAD.txt:998:خرحلوش وخرروش. - أيطالى 106012:ةه معناه ورقة محشوة بارودا مرادقه 
TAD.txt:1699:القضيب ءنالحديد وك هه اللحم ليشوى وتنصاح به البارودة ويدممو نه شياش. وفصيحهالسةعود‎ 
TAD.txt:1845:طبتجة ‏ ترق « طابائجة 4 وهو الغد ار أي البارودة الصغيرة 
TAD.txt:2127:فعك - ترى « فشتك » أ حشو البارودة 
TAD.txt:2500:وهو قع يحشى من ملح الزئيق فيشعل البارودة 
TAD_pages.txt:320:‫بارود ‪ -‬ترك « باروت »©وهو م‪6‬أخنوذ‪1‬مدنادم الافرئسية أى غبار وقد‬
TAD_pages.txt:321:           ‫أطلقوه على الغبار الناري ومنه البارودة يتذف مها الرصاص والخردق‬
TAD_pages.txt:731:     ‫ْ‬                                         ‫تفتكه ‪ -‬ترك وهو البارودة والرصاص الذي برى به‬
TAD_pages.txt:967: ‫خرحلوش وخرروش‪ - .‬أيطالى ‪:210601‬ةه معناه ورقة محشوة بارودا مرادقه‬
TAD_pages.txt:1639: ‫القضيب ءنالحديد وك هه اللحم ليشوى وتنصاحبالهبارودة ويشدمميوانشه‪ .‬وفصيحهالسةعود‪‎‬‬
TAD_pages.txt:1760:               ‫طبتجة ‏ ترق « طابائجة ‪ 4‬وهو الغدار أي البارودة الصغيرة‬
TAD_pages.txt:2017:                                         ‫فعك ‪ -‬ترى « فشتك » أ حشوالبارودة‬
TAD_pages.txt:2363:                              ‫وهو قعيحشى من ملح الزئيق فيشعل البارودة‬
=== LKT barut
=== TTS barut
(eval):4: no matches found: TTS*
```


## [2026-09-14T00:54:40.845Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=325 && /\\[pdf page/ {print NR\": \"$0}' TAD_pages.txt | tail -5\necho \"---- context\"; sed -n '300,325p' TAD_pages.txt"
}
```


### [2026-09-14T00:54:41.940Z] TOOL RESULT

```
---- context
                                               ‫مشور‬
                                                  ‫‏‪ 4:١‬أ)مافي الا‬
‫يابج ‏ فارسي « بابوش » معناه غطاء الرجل وهو داس يلبس في الرجل‬
                        ‫باور ‪. 7‬يطالي عنندمة؟ معناه مخار امدرفه بآخرة‬

‫بواتبم ‪ -‬فارسي « بابونه » وحهشيشة ذات زهر أصفر مكلل بأبيض‬
                                                              ‫يتداوى بها‬
‫بادزص جافاريق عركن من بادأي ضد وزهرأي سم وهو حجر نحمله‬
                                                                 ‫الدجالون‬
‫باديجان ‪ -‬في الفارسية « بادينجان »‪ 6‬نقل الى الاسبانية ‪2‬مئمعمه‪ 8‬ومنها‬
‫الى الافر نسية ‪#‬هنعروطناة ثاملى الايطالية ‪5‬ةنهده؛وم ويقال له في الايطالية‬
‫أيضا هسةتدداءه» و «داعنت في اليونانية معناه اسود فنظر بعضيم الى ظاهر لنظه‬
‫ففسره « بيض المان أو ابن الجنينة ‪ 4‬أما أصل هذا النبات فههنودي فيكون‬
                           ‫اسمه هندي أيضا ويقال له في العربية قهقب حدق‬
‫بارجة ‪ -‬ايطالي هنهعه‪ 1:‬وهو اسمطائر ماي سميت تلك السفينة باسمه‬
                                                   ‫وقد بطل الا ن استءالها‬

‫بارنامج‪ 5-‬فأرسي م كبمن يارأي هرة وحمل وتمأنمه أي كتابورسالة‬
                                    ‫بآرة ‪ -‬فارمي « باره ‪ 6‬معناه قطعة‬

‫بارود ‪ -‬ترك « باروت »©وهو م‪6‬أخنوذ‪1‬مدنادم الافرئسية أى غبار وقد‬
           ‫أطلقوه على الغبار الناري ومنه البارودة يتذف مها الرصاص والخردق‬
                                 ‫م‬‫ميه‬
                                    ‫م ل‬
```


## [2026-09-14T00:54:42.375Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt390_436_top.jpg"
}
```


### [2026-09-14T00:54:42.390Z] TOOL RESULT

```

```


## [2026-09-14T00:54:48.149Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nprint('leaves',len(lv))\nfor i,p in enumerate(lv):\n    if 'بارود' in p:\n        print('leaf',i)\n        break\nEOF\ngrep -c \"\" TAD_pages.txt"
}
```


### [2026-09-14T00:54:49.227Z] TOOL RESULT

```
leaves 87
leaf 9
3118
```


## [2026-09-14T00:54:56.310Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON parsa\"; grep -n \"پارسا\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10\necho \"=== MON pudr\"; grep -n \"پودر\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10\necho \"=== sizes\"; wc -l MON_part1.txt MON_part2.txt\necho \"=== MON adena\"; grep -c \"پارسا\" incoming/MON/MON_2vol_Adena_v1_djvu.txt"
}
```


### [2026-09-14T00:54:56.440Z] TOOL RESULT

```
=== MON parsa
MON_part2.txt:7397:کار بد» گناه» ناپارسایی. 
MON_part2.txt:11835:مومن؛ متقی؛ پارسا. برای اولیای دین مسیح 
MON_part2.txt:62969:پارسا. آنچه که از نظر دینی مورد توجه و 
MON_part2.txt:76957:بغمبران؛ امامان و پارسایان. 
MON_part1.txt:6905:پرهی زکاران» ترس‌کاران» پارسایان, " 
MON_part1.txt:10642:پا کیزه‌تر. پارساتر. 
MON_part1.txt:10774:پارساتر. 
MON_part1.txt:18754:ورع‌تر» پرهیزگار تر» پارساتر. 
MON_part1.txt:27814:(یش.) گذشته» ماضی: پارسال. 
MON_part1.txt:27947:پارسا: 2:05 [- پارسای] (ص.) آنکه از 
=== MON pudr
MON_part2.txt:18845:پودر می‌شود. (مخصوصاً اگر چند قطره 
MON_part2.txt:19061:(از آن پودر کاکائو تهیه می‌شود.) دانة این 
MON_part2.txt:25906:و از روی مرکب پودر مخصوصی می‌ریزند 
MON_part2.txt:37750:کوبیده بصورت گرد (پودر) درمی آورند و 
MON_part2.txt:41414:رنگ آماده کر دن. ( کد.) پودر و ماتیکك 
MON_part2.txt:89850:هرولین: 0 (ا.) (شیم. بز.) پودری 
MON_part1.txt:33019:پودر: ۲۳۵۲ (.) گرد غبار. باروت (غم.) 
MON_part1.txt:44720:جوش‌های تراخمی بصورت گرد (پودر) 
MON_part1.txt:68619:کنند. مواد مزبور را سایند و به شکل پودر 
MON_part1.txt:69050:فرمز؛ پودر روژ. 
=== sizes
  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
=== MON adena
29
```


## [2026-09-14T00:54:59.354Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== parsa entry\"; sed -n '27940,27975p' MON_part1.txt\necho; echo \"=== pudr entry\"; sed -n '33010,33030p' MON_part1.txt"
}
```


### [2026-09-14T00:54:59.431Z] TOOL RESULT

```
=== parsa entry
جنوب ایران. (تد.) یک در ارآ زار 
مذکو بارسی: (ند.) یک تن ابرانی» یرای 
(اح.) مسکن قوم مذ‌کور. 

پارس: 2« [تر. ء بارس (.) یوزپلنگ. 
پارس: 0 (اصت.) آواز سک» عوعوه 
هفهف» وغواغ» وعوع» وک وک نوف. 
پارسا: 2:05 [- پارسای] (ص.) آنکه از 
گناهان پرهیزد و به طاعت و عبادت و قناعت 
عمر گذارد) پرهیز کار» با کدامن» زاهد» 
مستقی. دبندار» مستد.ین» مسقدس. عارف» 
دانشمند) مق. ناپارسا؛ ج. بارسایان. 
پارسال: 027*51 (امر.) سال گذشته» پار. 
پارس ئیل: ۲-11 (تر. - بارس ثیل] (امر.) 
سال پلنگ» یکی ار سال‌های دوازده گٌانة 
بر کان: 

پارسنگ: 02۲-8 [- باره‌سنگک] (امر.) 
سنگی که در یک کفهة ترازو گذارند تا با 
کفه دیگر برابر گردد؛ پاسنگث» پاهنگ. 
پارسه: (6-)02152 [- بر سه ] (امر.) گدایی؛ 
پر سه» تکدی. کدا. 

پارسی: :27( (ص‌نس.) منسوب به 
پارس» فارسی. از مردم پارس» اهل پارس» 
فتارتی ان راب6 اهسل اسرانر زر 
مها زرتشتی مقیم هندوستان؛ ج. 
پارسیان. زبان مردم پارس» فارسی (به معنی 
خاص). زبان مردم ایران» فارسی. ماه‌های 
بارسی: دوازده ماه سال شمسی ایرانبان: 
فروردین ماه» اردیبهشت ماه خردادماه» تير 
ماه» مرداد ماه» شهر یور ماه» مهر ماه» آبان 
ماه آذرماه؛ دی ماه» بهمن ماه اسفندارمد 


(شهر بور)» اسفندارمذ» خرداذ» سرداده 

=== pudr entry
جامه بافند؛ مق. تار. (قالی) نخ سفید یابه 
رنگ دیگر که بعد از هر رک لای ردیف 
تارها کشیده می‌شو د؛ مق. تار. 


بود. 0 [- بوده < بد - یده» سوخته ] (.) 
هر چیز سریع الاحتراق که آتش چخماق بر 
آن افکنند؛ آتشگیره» حراقه. 

پودر: ۲۳۵۲ (.) گرد غبار. باروت (غم.) 
کرد سفید و معطری که به چهره مالند. 
پسودنه: (-)000۵ [- پونه ‏ پودینه < 
پوتنج» معر.- فودنج» معر.] (ا.) ( گیا.) گیاهی 
از تیرة نعناعیان که پایا می‌باشده ساقه‌اش 
ری استوانای (ولی همان شکدل کلی 
چهارگوش بودن تیرهٌ خود را حفظ کرده) و 
مسنشعب است و برگ‌هایش بیضوی ولی 
گردتر از برگک نعناع است. دندانه‌های 
برگ‌هایش ظریف و گل‌هایش گلی رنگ و 
بطور فراهم در نقاط مختلف ساقه با فواصل 
ی وت ۳ اين گیاه در اکثر
```


## [2026-09-14T00:55:13.044Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T00:55:13.054Z] TOOL RESULT

```


```


## [2026-09-14T00:55:16.750Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1",
 "prompt": "Give the full Persian etymology section for پیر (pir) \"old\": which Middle Persian and Proto-Iranian/Old Iranian form it derives from, and any cited authorities (Cheung, Hasandust, MacKenzie)."
}
```


## [2026-09-14T00:55:18.406Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B1%D8%B3%D8%A7",
 "prompt": "Give the full Persian etymology and definitions for پارسا (pārsā): derivation, Middle Persian form, and any cited authorities."
}
```


### [2026-09-14T00:55:22.804Z] TOOL RESULT

```
# Persian Etymology for پیر (pir) "old"

Based on the Wiktionary entry, here is the Persian etymology:

**Middle Persian form:** 𐬞𐬌𐬭 (pyl /⁠pīr⁠/, "old, aged, ancient")

**Proto-Iranian form:** \*paru- ("ash-gray, pale gray, hoary")

**Proto-Indo-Iranian form:** \*parHušás ("gray")

**Cited authority:** The entry references Edelʹman, D. I. (2020), *Etimologičeskij slovarʹ iranskix jazykov* [Etymological Dictionary of Iranian Languages], Moscow: Vostochnaya Literatura, page 172.

The entry notes comparative evidence from Sanskrit परुष (paruṣa, "spotted, rough") and English "pale." However, the document does not cite Cheung, Hasandust, or MacKenzie for this particular entry.
```


### [2026-09-14T00:55:23.622Z] TOOL RESULT

```
# Etymology and Definitions of پارسا (pārsā)

## Etymology
The origin is **uncertain** and the term "is not found in Middle Persian." However, scholars frequently suggest a connection to Middle Persian **𐭯𐭠𐭫𐭮𐭩** (pʾlsy /⁠Pārs⁠/, "Persia"), with reference to the Zoroastrian belief that Iranians held a special status as God's chosen people.

## Definitions

**As an Adjective:**
1. Pious or devout
2. Abstemious or temperate
3. Chaste (specifically describing a woman)

**As a Noun:**
1. A pious, saintly, or ascetic person
2. A chaste or virtuous woman

**As a Proper Noun:**
A male given name (Parsa)

## Historical Citation
The word appears in Shaykh Muṣliḥ-ud-Dīn Saʿdī's 13th-century *Gulistan*, where it refers to "a hermit" experiencing suffering while maintaining gratitude to God.
```


## [2026-09-14T00:55:37.743Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/barut",
 "prompt": "What is the etymology given for Turkish \"barut\"? Which language does it come from, earliest attestation date, and what origin is given for the Arabic form bārūd?"
}
```


## [2026-09-14T00:55:39.178Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/falcon",
 "prompt": "Give the full etymology of \"falcon\", including Late Latin falco, the \"curved claws\"/falx theory and the Germanic \"gray bird\" theory."
}
```


### [2026-09-14T00:55:41.414Z] TOOL RESULT

```
I cannot provide the etymology information you requested based on the content above. The webpage excerpt shows only the header, navigation elements, and footer of Nişanyan Sözlük (a Turkish etymological dictionary), but does not include the actual dictionary entry for "barut" that would contain the etymological details about its origin language, attestation dates, or information about the Arabic form bārūd.

To find this information, you would need to access the full entry page for "barut" on the Nişanyan Sözlük website.
```


### [2026-09-14T00:55:44.201Z] TOOL RESULT

```
# Etymology of Falcon

The word "falcon" entered English in the mid-13th century from Old French *faucon*, which derives from Late Latin *falconem* (nominative *falco*). This Latin term spread across Romance and Germanic languages, appearing in Spanish, Portuguese, Italian, German, and Dutch variants.

## The Curved Blade Theory

The primary explanation suggests the bird's name comes from Latin *falx*, meaning "curved blade, pruning hook, sickle, or war-scythe." According to this theory, the bird was named "for the shape of its talons, legs, or beak," or alternatively for "the shape of its spread wings."

## The Germanic "Gray Bird" Theory

An alternative theory proposes that the Latin bird name *falx* has Germanic origins, deriving from a Proto-Indo-European root meaning "pale" or "gray bird." However, this theory faces opposition from scholars who note that falconry appears to have been imported from the East to Germanic peoples via Rome, not the reverse.

Both theories remain unresolved, reflecting the uncertain ultimate origin of this widespread word for these birds of prey.
```


## [2026-09-14T00:55:51.946Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B1%D9%88%D8%AF",
 "prompt": "Give the Arabic etymology of بارود (bārūd) \"gunpowder, saltpetre\": proposed origins (Greek, Latin, French poudre?), and the Persian/Turkish sections of the page if present."
}
```


## [2026-09-14T00:55:52.460Z] TOOL CALL #50: WebSearch

```json
{
 "query": "Nişanyan barut etymology Arabic bārūd kökeni"
}
```


### [2026-09-14T00:55:58.167Z] TOOL RESULT

```
# Etymology of بارود (bārūd)

The Arabic word has **uncertain origins** and is not Classical Arabic. The Wiktionary entry proposes three possible etymologies:

1. **From Arabic برود (barūd)**: "a soothing collyrium used against inflammation of the eye; any powdery collyrium," with colloquial sound changes between *a* and *ā*.

2. **Via Aramaic from Armenian վառօդ (vaṙōd)**: meaning "gunpowder," composed of "burning" + "air." However, this may represent folk-etymology reshaping of an earlier Armenian term ultimately borrowed from the Arabic word itself.

3. **From Medieval Greek πύρωτον (pýrōton)**: "type of flammable chemical," derived from Ancient Greek πυρίτης λίθος (purítēs líthos, "stone of fire, flint"), with the root πῦρ (pûr, "fire").

**No Greek, Latin, or French origins are mentioned.** The Persian section lists بارود (bârud) as an archaic alternative form of باروت (bârot), ultimately from Arabic. The Turkish section shows باروت (barut) as a descendant from Ottoman Turkish.
```


### [2026-09-14T00:56:00.960Z] TOOL RESULT

```
Web search results for query: "Nişanyan barut etymology Arabic bārūd kökeni"

Links: [{"title":"باروت - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B1%D9%88%D8%AA"},{"title":"Sevan Nişanyan / En son yazıları: Barutun şeceresi","url":"http://nisanyan1.blogspot.com/2019/05/barutun-seceresi.html"},{"title":"BĀRŪT - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/barut-also-barut-and-barud-gunpowder-is-a-loanword-from-arabic-it-passed-from-turkish-into-persian-usage/"},{"title":"barut - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/barut"},{"title":"بارود - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B1%D9%88%D8%AF"},{"title":"Nisan (disambiguation)","url":"https://en.wikipedia.org/wiki/Nisan_(disambiguation)"},{"title":"барут - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D0%B1%D0%B0%D1%80%D1%83%D1%82"},{"title":"Sevan Nişanyan / En son yazıları: May 2019","url":"http://nisanyan1.blogspot.com/2019/05/"},{"title":"Aiming stone","url":"https://en.wikipedia.org/wiki/Aiming_stone"},{"title":"बारूत - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A4%AC%E0%A4%BE%E0%A4%B0%E0%A5%82%E0%A4%A4"}]

Based on the search results, here's what I found about the etymology of "barut" according to Sevan Nişanyan and other sources:

## Etymology Overview

The word "barut" was borrowed from Arabic بارود (bārūd). Bārūt (also bārūṭ and bārūd) meaning "gunpowder" is a loanword from Arabic that passed from Turkish into Persian usage.

## Deeper Etymology Questions

However, Sevan Nişanyan's blog discusses intriguing questions about the ultimate origin of the Arabic term itself. Nişanyan notes that the word appears in Byzantine manuscripts as "pyrōton" and "pyrotron," which would yield "birūd" or "bürūd" in Arabic when accounting for sound changes (p and o sounds becoming b and ū in Middle and Late Arabic).

## Possible Ancient Greek Origin

One possible etymology suggests the Arabic بَرُود (barūd) may derive from "a soothing collyrium used against inflammation of the eye; any powdery collyrium", though this seems to be a folk etymology. The Greek connection raised by Nişanyan points to a more complex history than the direct Arabic borrowing might suggest.

The search results show that while the immediate etymological path is clear (Arabic → Turkish → Persian and other languages), the ultimate origin of the Arabic term itself remains somewhat uncertain, with possible Byzantine Greek influences in its history.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T00:56:07.879Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/barut-also-barut-and-barud-gunpowder-is-a-loanword-from-arabic-it-passed-from-turkish-into-persian-usage/",
 "prompt": "Quote the opening etymological statement about BĀRŪT: what language is it a loanword from, how did it reach Persian, and when is it first attested in Persian?"
}
```


### [2026-09-14T00:56:09.176Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T00:56:09.566Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/powder",
 "prompt": "Give the etymology of \"powder\": Old French poudre/pouldre, Latin pulverem/pulvis, and the PIE root cited. Also note what is said about pollen if mentioned."
}
```


### [2026-09-14T00:56:13.497Z] TOOL RESULT

```
# Etymology of "Powder"

**Origin Chain:**
The word "powder" traces back through Old French *poudre* (11c. *pouldre*) to Latin *pulverem* (nominative *pulvis*), meaning "dust" or "powder." The Latin term is the source for related Romance language words like Spanish *polvo* and Italian *polve*.

**PIE Root:**
The etymology dictionary does not explicitly cite a Proto-Indo-European root for *pulvis*.

**Note on Pollen:**
The entry mentions that Latin *pulvis* "perhaps is related to Latin *pollen* 'mill dust; fine flour'" but indicates uncertainty about this connection, noting that etymologist de Vaan has additional analysis on the matter.
```


## [2026-09-14T00:56:19.690Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B1%D9%88%D8%AA",
 "prompt": "Give the Persian and Ottoman Turkish etymology sections for باروت (bārut): what language Persian borrowed it from, and what Ottoman Turkish borrowed it from."
}
```


## [2026-09-14T00:56:21.420Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pollen",
 "prompt": "Give the etymology of \"pollen\" (Latin pollen \"mill dust, fine flour\", PIE root) and any mention of appall/pale roots on the page."
}
```


### [2026-09-14T00:56:23.641Z] TOOL RESULT

```
# Etymology Origins for باروت (bārut)

**Persian Etymology:**
Persian borrowed باروت from Arabic. The source states: "Borrowed from Arabic _[بارود](/wiki/%D8%A8%D8%A7%D8%B1%D9%88%D8%AF#Arabic "بارود")_ (bārūd)."

**Ottoman Turkish Etymology:**
Ottoman Turkish also borrowed the word from Arabic. According to the entry: "Borrowed from Arabic _[بَارُود](/wiki/%D8%A8%D8%A7%D8%B1%D9%88%D8%AF#Arabic "بارود")_ (bārūd, 'saltpetre; gunpowder')."

Both languages independently borrowed this term from the same Arabic source word.
```


### [2026-09-14T00:56:25.590Z] TOOL RESULT

```
# Etymology of "Pollen"

**Latin Origin:**
The word "pollen" comes from Latin *pollen*, meaning "mill dust; fine flour" (from Linnæus, 1751). An earlier English usage from the 1520s referred to "fine flour."

**Related Words:**
According to the page, Latin *pollen* is connected to *polenta* ("peeled barley") and probably to Greek *poltos* ("pap, porridge") and Sanskrit *pálalam* ("ground seeds"), though "the ultimate origin is uncertain."

**PIE Root:**
The page does not mention a Proto-Indo-European (PIE) root for pollen.

**Appall/Pale Roots:**
There is no mention of "appall" or "pale" roots anywhere on this page.
```


## [2026-09-14T00:56:32.457Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT pouruša\"; grep -n -i \"pouru.a\\|paourusa\\|paourusa-\" BRT.txt | head -20\necho \"=== BRT parya\"; grep -n -i \"parya-\\|pairya\" BRT.txt | head -10"
}
```


### [2026-09-14T00:56:32.523Z] TOOL RESULT

```
=== BRT pouruša
3950:•  j.  'abda-  Adj,  'ausgezeichnet,  trefflich': dämqn  pouruca  -daca  (APn.)  Vt.  ifj.io.
6860:'rS  maaiä y7  mazistJ yjzatanqm yJ  vaAi^^  yt,i^.  ^T  \t%v.;  —  cattt  alte  mi^ra  tava  yit yazatanqm  Yt.J7.16; —  °r>m  tnazäqm  ..'.°ra  ma3äaV.4-3;  —  ahm  äuyoarfm 'rahe hudanfam  mazishm  yjzalim  yim  sjvisi?iH  \  mazdii  3^ai>karpm  ain>sanqm  spmtanam /rädat^ali:}m  dätänmvohunam  damanqm\'^K.i-j.z;  16,  V.  79.  13;  —  us  mg  fita \,  16.  i;  —  nh'afiayemi..daiusj(StvcTZ.)iAaomäi  draond  frSnnaoi  °rS  mazdh  ..  V. °rahe  mazdä  ralvatS  c^annarmAalS  (Sl-  /j,  4;  —  astvatintä  .  .  asts  mazda  °rahe verz.)  mazistahe'a  vahistahe^a  sralHahecaYlx.ig.f)-i;  I3.\\f>,  V./(7.34;  —  buyama xraoMistake'a  xraiwistaheÜa  kukinpttma- ,  'rahe  mazda  frya  väsiita  astayJ  (sd.)  V, he'a  aSät  apanSJtmahe'a  hwiHmanS  vouru.- 1  70. 4;  —  haomö  . .  zaota  °räi  (statt  Gen.) ra/na»/i^  y7  nS  daöa  yd  lata^aylltu^ruy?\mazdai  Vty.88f.;  —  ySs^a  t!  y?na  'ra yj  mainyus  ipmtSJimB  V.  /.  i ;  usw. ;  —  mazda  Vr.  7.  4 ;  —  fravasTm  avqm  yqm pQuru^ar)na)3ha  'ra  mazda  VyL  2^^;  —  °raAe  mazdä  Y.  26.  2;V. 1^.14;  —  vXsp»mca °raki  mazdh  ..  STvUtah!  \.  56.  1;  — ^k^rs/s  'rahe  mazdä  Y.ji,^; —  ««  'rahe ax^aßis  ahi  abai>hJ!  tum  yS  °rD  maxdä  1  mazda  yazamaide  dar?ir3i  (sd.)  mq^rahtr V,  jp.  20;  —  'rät  mazält  .  .  vpr/irayne ■  sp^ntaAe  xralüm  'rahe  masdi  ..  marjirrüi frädat^aliai  yat  huxla'iräi  .  .  ratu-l..  hievam  ° rahe  matdä  . .  fravSkäi  .  .  Yt. xla%rai  Vr.ll.i;  —  huxsa'irSJ^mli.'if  1.2%;  —  gayehe  marP^nS  .  .  yS  paoiryd at  xsa'ir?m  eiyJt  yat  'rät  masdäi  A.^.  °räi  (stitt  Gen.)  mazdJi  manlscä  *git/ta 6;  s.  Y.J5.5;  —  'rät  masdäi  fanhavl  säsnasca  Yt./_J.87;  Y.jp.14;  —  nazdys vohumaill  Y.  I2.\;  "V,  tg.  11;  —  vaAists\ahmi  az>m  (Stverz.,  unter  3)  yö  'rS 'ra  mazda  Y.  /p.  1 5 ;  —  xsayat?  "rahe  I  mazda  vispahe  aukSul .  .  ya^a  .  .  P.  2(.?; mazda  YX.13.-jZ;  —  ise  ^wqm  'ra  mazda ..\  usw.;  Vyt.j^';  —  pascasta  azim  ya  'rS aoaoyf  ahi  a'iaoyS.xratul ..vTsps.viwS  Yi.'mazdil  aoi  urune  urväsma  (sd.)  dassayeni /2,  i;  70.  III,  V.  ig.  20,  a6,  Vr.jp.  i;  — Ivahi/ipmea  ahüm  .  .  V.38;  Y.ig.6,  7;  — °rJ  mazda  hvapis  Yt  5.  85;  Y.  7/.  10  (wo  vasas^a  tu  'ra  mazda  . .  x/ag/a  havanqm ab  Vok.) ;  —  'ra  mazda  mainyl  spinUta  1  däinanqm  Y.  Ä*.  5 ;  —  imat  dqma  yat  "rahe dätar?  gai^anqm  astvaitinqm  asäum  {^\.-\  mazdh  V.jy.14,  17,  34;  Vyt  20,  Vd.  i, verz.,  unter  I  2  a.);  usw.;  —  tsm  bay?m\YX.i(f.iZ,\.22.Z;  —  irrj/^/^-rJ (statt Vok.) t)m  ratüm  ,  .yim  'ram  mazdqm  daovätih?m  \  mazdä  vanuhti  dämqn  .  .  yazamaide  yäü i^t^vcz)  rapant3mtarh'a»h?mt'üpa*voh[i^dadä'ia  pouruca  vanhuia  Y.  7;.  10;  ;.  1, Y.70.1;  usw.;  fo.  9;  —  'rim  mazdqm\  12.  7, Yt  ig.  10,  58,V.  21. 4;  —  azmi  daoqm mainyaem  mainyavanqm  dämanqm  main-...tistrim..ya'ia  mqmcit  yim  'nm  mazdam yaoyä  stSts  ahUm;a  ratümca  Vr.  2.  4;  7,IVlÄ'.5o;  —  ttstrlm  .  .  yahmäi  hazaitnm ^'■57-4j  —  allat  dim  vlspanqm  mazih?m\yaoxstinqm  fradd^at  °rS  mazda  Yt^.45; dazdyäi  (sd.)  ahUm^a  ratUmca  yim  °r}m\iQ.Z%; —  tistrim  ..yim  ratüm  frada'hat masdqm  Y.  27.  i;  Vr.  /;.  21;  —  imimca'  'ro  mazdä  YL<?.  44;  5-  89,  70.103,^5.35; isi"^ rahe paitim ..yim  'rsm  mazdqmY.2.i6;\  —  arpdvjm  . . yeiihe  ca'^wärB  arSäna  ham.- 13.1,  ^.I03{?);  —  ySvaram  °rS  mazdä ..^tlsaX  'rJ  mazdä  Yt. 5.120;  —  ya'ia  vs tä  varmScä  .  .  ahmi  Y.12.  7;  —  mi^rpm  '  'rS  mazdä  fradaiim  haxsat  F.  ^Ib;  —  tä ..yim  yazata  'rS  mazdä  raoxsnlt  paiti  (frava^ayS)  ii3..'ä^rayente  ..aomna  'ra{lS^ gars  nmänlt  Yt.  10.12s;  5- '7!    —    avi\  mazda  Yt  13. 146;  S.7,  $&;  —  äyaptj/r.
8467:•  j.,  g.  urvarä-  f.  Tflanze',  meist  Plur.; Sing,  äwich  koll.'*;  oft  göttlich  verehrt; I )  im  AUgemeben,  hauptsächlich  von  den Nutz-  und  NährpSanzen:  eaiti  hsnti  'ranqm sar»fia  "wie  viel  Arten**  von  Pflanzen giebt  es?"  V.5.19  PitZ.;  —  a^ra  »;? raoomti  vUpk  vispSjarvoö  V,5.  19;  — yerihe  paiti  pourujar^a  s»mSoa  usuxlyeinii •rä  Yt  /j,  10;  —  avqm  vanqm  .  .  yä visps.bis(_sd.)  nqma  yqm  upairi  vjspanqm •ranqm  iacxma  nilayal  YL  /2. 1 7 ;  —  vis- paaqm  'ranqm  taoxma  .  .  ysi  hmti bartzisia^a  hubaotaitsmaca  V.  2.  28; 'ranam  (als  Subi.)  zairi^aonanam  tarp- matm  paiti  amäca  *usuxsyänti  Yt7.4'';
9782:a^3.dätayä  gSusca  pouru^arihaya  Yt.7.0;  1 y.  /.  1 1 ;  —  mawha  *ra  (VS.)  V.  21.  9.
10141:—  '^riiajca  (sd.)  &a  ..  °Jus  apa./asaj  Y.'J.  2,  22.1  ■ — mit  baoirya-  kd],  {sd.):  'qm 2.23;  —  kat  ta  '3ul  yaozdayqn  {^^  .  .\baoiryqm  Y.  ^.  3  GL,  7.  3  Gl.  III)  mit V.  7.  76.  a)  in  der  Bed.  I  und  lA  oft  1 1)  aiv5.däta-  Adj.  ">  (sd.)  oder  a)  kkt"  i\. neben  Himmel,  Erde,  Feuer,  Wasser,  vom  Urrind'^',  dessen  Seele  (urvan-)  ver- Pßanzen  usw.:  ya^  spmtö  mainyui  vVjä-\^vCiv:\A  erscheint***':  i)  'Sus^a  acvd.- rayal  asman>m  . .  apim  . .  zam  . .  "qm  . .  j  dätayä  giusca  (s.  I  A)  pouru.sar»oay<'i urvaram  Yt.  13.  iZ;  Y.  2J.  i,' 15.  2,  Y^.-;.\xmao%ra  ..  Yt.7.0;  —  'aom  (statt  Gen.?) 4;  —  para  . .  asnö  . .  äp3  . .  z»mö  .  .  an^S-dälahe  . .  gaom  (s.  I  A)  pouruaarf urvarayii  ..  'Sus  datjhöit  Y.  ig.  8;  —  kuha  aahe  urunB  .  .  S.u.  12.  2)  yä.varanä .  .  yaohda'iäni  .  .  iitrim  .  .  äptm  .  .  zam  I  ilpS  . .  urvari  . .  'aus  hudai''  Y.  12.  T,  — . .  'am  V,  //.  I ;  2,  6,  9,  g.  33,  42 ;  —  Aach '  usshistat  "aus  V.  2.  10  PQZ.(?);  —  tai-a airat  .  .  apat  , .  samat  .  .  'aot  V.u.  10;,  'Jus  ÄuaS/fAü'*  urutie  FrW.tf.i; — ..'Suiia
13162:—  atfhSui  akyä  .  .  valdä  yJ  Im  dät  Y. 4S-  4;  —  äämqn  .  .  yäü  äaäitäa  pouruta vohula  Y.7/.  io;/p.  10,  Vr.J2.4;  —  akurd .. paitiia  daman  daiHn3Ytig.$8;  —  aai/i daoam  atryan^m  cfarpttS  YtlS.i;  3 ;  — oAurö  masdä  yS  gam  dada  yS  narvm  ala- vamrn  Y.  12. 7;  —  ddi^usU  ahurahe  . .  yö nS  dala  yB  tatasa ..Y.l.i;  —  iyat  domo paouruyh  da  ahurä  "seitdem  dass  du  die ersten  D,  geschaffen  hast,  o  AhV  V.4ti.6; _J/.  1 1 ;  —  II  öaga*  *'vazaria*  <^urJ'tna»dä Ayer  imäm  ÖBmim  adä'' . .  asmäaam  ada!' . . martiyam  adl^  . .  liyjtim  adj'  martiyakyU (imSinndesDatcomin.)D.  (».  i;-',  X,7.  i^, 6.  I*,  Ao.  /.  i';l  —  s.  noch  daovah- bes.  2)  mit  Lok.  des  Ziels  'versetzen, verbringen  in  — ':  eastaistä  (sd.)  yS  tia x'^^ri  däyäi  (Kon].)  Y.50.  5;  —  ilyap/a  .. yäis  rapatds  fsd.)   daidtt  x^a>rl  \.28.  2;
16225:•  j.  pouru.aspa-  Adj.  'der  viele  Rosse  be- sitn,  rossereich':  'ps  yaka  paourusaspahe Vyt  a; —  '^J»»  b«tvSMya%a  *pouruiaspahe Az.4.
16259:•  j.  pouru.baevan-  Adj.  (auch  fem.)  Viele Zehntausende  betragend';  äatfra^mü  . . fravaiayS  paeins  pourujatk  .  .  pouru.- hazanrh  .  .  'vanS  (NPf.)  YLjj.  65;  — aoa  .  .  urvarä  baisaeyä  utbarym  paoiril pouru.sati  . .  pouru Jtazatsra  . .  *van3  (APC)
16309:pouruSa-
16311:•  ).  pouruia-  (,  paourusa-)  Adj.  'grau, greis';  *°sö  asti  varsS  "greis  ist  das  Haar" V.  -.  57  Gl.
16313:•  j.  pourusaspa- '*  m.  EN.  des  Vaters Zara^ustras:  'ps ..yat  hi  tum  ussayaaha .  .  tara%ultra  nmänahe  'paheH.g.xy,  V. IQ.  4,  46,  F.4£;  —  puhnm  yai  'pahe  . . zarahustnm  Yl  5.  18;  V.  jp.  6;  —  mä OtaraySis  saraiustrake  {sXaXXVS.)  mä  'pake (statt  AS.)  mä  duyts.vqm  "erziime  nicht,  ■ oZ.,  den  F.,  nicht  die  Z»."  FrD.  ^;  — I pouru.aspB{sA.Y^ yä^a  'pahe  Vyt2  ";  hz.4.  \
16320:•  ).  pouru-hazaura-  Adj,  {fem.  'rä-)  'viele  I Tausende  betragend':  äat  fralüstnti  .  , fravasayS  paoirll  pouru.sata  ,  .  'ra  .  .  \ pouru.daevans  Ytij.6$i  —  a&a  un}ara\ balsazyä  uzbanm  paoirjl  pouru^ala  . .  °rä  I . .  pouru.baevanS  V.  20. 4.
16445:—  'hfvm  ..  duyoarpm  Y,i2.s;  i,  3;  — näirya  va  '%raAe  vä  Y.  //.  i ;  —  nar»m vä  *näirikqm  vä  °&/vw  va  FrB.;  —  °^raAe '^rrtrt  Frb.7;  —  II  vistäspahyä  •ä'a* ariämahyä  napa  Bh.  i.\-,  —  küraui '%* J" Bh.  /.  10,  II,  13,  j,  5,  4.  i»,  b,  h;  J.  16^, 2.3,.?i3'.  4.i\  18*,  d,  i,  D./,  2,  5.1, 6'.  \',  72,  jy,  76',  ig,  X.  I.  2,  5,  Am.  /*,  2, Ao.  1.  2^;  l  —  pouruSaspahe  ''irS  V.  ig.  6, Yt.5. 18;  7z,  105,5.18,  30,  Y.5.  5;  —  ala- vazdasca  ^ritasca  säyuidrsi?  °'^ra  (ND.) Yt5.72;  —  /f^a"'ärfl(NP.)  "iiranaonahe F.  4  f.;  —  ycti  aslüal?r»tö  (sd.)  /raxUäiU äste  ..  vJspa.taurvaya  '^rS  Ytjp.  92;  — '"iratihs  daiähu.paitinqm  Yt.  5.  85;  /4. 59,  V.rp.43;  —  ''kra  (oder  °%r!>)  kava vJliäspa  (oder  'psi-,  Stverz.)  Vytj'  usw.; '■'i  31'  52.  54i  55;  —  i'ftff  "Sr?  ä^wya- >iSisYt5.32,  /7.3s;  y.7.43;  —  airpm (Stvetz.) aAuraAe  masdi  '^n>nY.2.J2U3y/.;
17106:—  dämqn  .  .  pouruca  'myaca  (NPn.)  Yt  als  Komp.  —  j)  In  bätuMoi^ali-.  Eij.  'die ig.  10;  — /ravasayS     'myä  YLJ?  37'  —  beiden  (aoagestreekten)  Arme';  np.Aii  'Kltf-
17821:yemi  , ,  imat  am>ia  spptita  .  .  imat  asäu- nqm  varguAls  °iays  (VP.)  Wjra  aiiuihüra Y.  65. 1 2 ;  Ny.  /.  I ;  —  aora  varmkis  upa.- sa^a  .  .  äps  .  .  urvarä  .  .  tüäunqm  fra- vasays  Yt  13. 147;  1. 9,  10. 100,  H.  34,  y, 79,  FrW. /.  3;  —  jamyqn  i^ra  asäunqm .  ,  'iaylf  asöis  basfaza  hacimnä  . .  istSe *vadhar»Aqm  paitiHätSe  ätaranqm  Y.  60. 4;  —  qpqmea  .  .  urvaranqmca  .  ,  asao- nqmla  'hnqm  yasnsm  Vr. 21.  \;  —  yS nä  his  hubinta  *barat  jva  a?aonqtn *says  (als  AP.)  sästa  .  .  hö  anhaiti  za- sulttmS  Yt  /J.  1 8 ;  —  fravasayS  .  .  yä a/raourvisvat  k?r»navainti  irsm  yahmya jaanti  Yt.  y.  26;  —  -says  . .  ya  ahurahe xsayats  dasinqm  upa  yü&yänti  yezi  aim bavaiti  ^alavaxsnuiW.  13. 63  ;  — frasüSTnii uyrä  asäunqm  'fayS  paoirij'  pouru^sata .  .  pouruAatanra  .  .  pouruiasvanS  apitii ashntnä  haväi  käcil  näfäi  . .  tä  yü^yeinti pfianähu  have  asahi  Yt  l^.  65if.;  —  "sayS .  .ya  avai  trayS  aiwyaxsayänti  yat  vouru- kahm  ..yä  ave  strjui  atwyäxsayeinti yqm ^haptöiringS  ..ya  avqm  k^hrpim  aiwyäxsa- yänti  yqm  .  .  hnsäspahe  .  .  ya  avqm *x^rqm  (sd)  aiwyäxSayänti  yqm . .  tara- 'huStrahe  navaca  navaitlsla  navaca  sota nava^a  hatattra  navasSs^a  baevqn  Yt  13. 59—62;  —  "iayS  .  .  yä  vts^&a  ävayänli hamaspa>:maedaim  paiti  ratüm  äat  a^ra vtcar?nii  dasa  pairi  xsa/nö  Yt/J.  49;  — asSunqmcä  'HbyS  yä  nS  iltä  urvSibys  Y. 5Ö.  2 ;  —  asäunqm  '/is  narqmcä  näiri- nqmcä  yazamaidl  Y.^7. 3;  —  °fayS  yä paeirya  (sd.)  anhan  Y.  23.  \;  —  äyeseyesti "vTspaya  asavane  'se"  Y,  2_j.  3;  —  vTspä °iayS  (als  AP.)  asäunqm  yazamaide  ädah- *yunqmca ..  'say5 ..*u%dahyunqmla . .  °iayS.. narqmca  ..'^ayD  ..näirinqmfa  ..  °sayS  yaza- maide  Vr.l6.  2;  7.  i,  10.2,  16.  i;  —  nabä- nazdiäanqm  para.iristanqm  aliirapaitinqm a!>iryanqm  narqm..näirinqm  'iayff  yaza- maide  Y.  26.  T,  8  ff.";  —  a/äunam  "sayd .  .  nmänyä  visya  zantumä  däAyumä  zara- ^ustrSJpmä  Y.  ly.  18;  —  airyanqm'  .  . /ßityanqm'  .  .  sairimanqm'  .  .  säininqm' . .  dahfnqm' . .  vTspanqm'  dakyunqm  narqm .  .  näirinqm  .  .  °sayö"  yasamaide  Yt  13. 143—145;  —  fä  'sayU  .  .  aoßstA  hittti  .  . ya  paoiryanqm  tkaihnam  ya  vä  narqm azätanqm  /rais.car>^rqM  saoiyantqm  Yt. y.i7;'Y./.i8',  23.2,  24.5;  —'  vjipä .  .  'Iay3  .  .  yä    haca   gayät    mariihnai   ä
19311:3a; —  daevanqm  anSyantqm  ahmaUa  'näi aimäiüi  °tiahe  nmans.palSe  Y.  52,  2 ;  Yt  15. t*;-~fpfvru'^wa,.aora  mainyB kaca  °nat V.  11.10;  — yaoiääta..bun  'na  V. i/.a;  1, 4,  12.2;  —  yat  aiiS  nä yS yaoldi^tyS  hala aHiiyd  'naiiiyö  xshats . .  psrayst  V.g.  39; 40,  13.22;  —  yat . .  aiiqmUt  •»anqm[ca] caratB  dva . .  V.  y.  49 ; — vTspanqm  akmya •ne  nabänasdistanqm  Y.  26'.  7 ;  —  *katämS *naAe*'>  a%auruntm  (sd.)  pärayai  N.  /;  Yt 2.11;  —  t^a.vasatfitha  avi  'tarn  airya- maim  V.  22.  7;  13;  —  tum  . .  sara%uhra *nahe  pourusaspahe'H.  g.\y,  V. /p.  4,  46, Yt  i^.  36;  —  olsmanqmHt  .  ,  vazyäi/  .  . ratsui  'tarn  fränäiayata  A. j.  5:5;  —  us3.- hista  haia  gätvs/rasasa  haca  d^mänSi'-'' Yt  16.2;  —  yavat . .  späna  dt/  hapta  'tia *pairiJ(üahi{sA.)  bavqn  V.J5.4S;  — fratara (sd.)  haca  'na  v>r3syqn  .  .  V.iö.^;  — nistara.naOnal  'nahe  V.  17.  7 ;  6. 43,  g.  33, Yt//.  60;  —  mahsmya  'naÄe  N.yX;  — parepasca  'nahe  V.  y.  45,  46;  45;  —  k»m kfmHl  aipi  'ne  gatu  *saSe  Yt5. 102;  — raocamtn  paiti  'nahe  V.  7. 14;  —  ysi  °nä hqm.6arämahi  .  .  ätnmca  .  .  3at  paslalta ahe  'nahe  spa  vä  na  vä  iriäyäj  .  .  us haca  aHbyS  'naiiby3  baraym  . .  ätnmia  . . ku%a..älr7m  aiti  barqn  ava  aitim  'rum..1 V.5-39-4i;5'33';  —  '""  '»"^^  vfti  vTsi hr3yff  kata  (sd.)  uedat^yan  aetahe  yat iristahe  V.  5.  10;  —  ahe  'nahe  upa.- %'Ui»nsqn  (sÄ)  upa^w3T»tayqn  V,  Ä  10; — yui  .  .  iristim  upaJi?r3%wSJar3m  (sd.) avajtanqn  ava  .  .  iristim  baraytn  avaha 'mm  himaym  upa  .  .  'ntm  baötayqn  . . yezi  . .  *fum  upaJ>jr3%ws.tanm  avaxanqn ava  ..  °n3m  baraytn  V.  4",  af.;  —  ratu- fris  havS  yä  'nahe  *paitiricyehe  (sd.) ^■55-  8)  bes.  im  Gegensatz  zu  Ge- meine, Gau  und  Land*);  'vsa%Pi:^..yS  hu- dänul  damanahya^  xla'hr?m  idßirahya vä  dahySu/  vä  . .  frada%äi  (sd.)  aspfrazats Y.31. 16;  —  3  eJ  'mmf'  vUsm  vä  ist^rtm vä  dahyüm  vä  ädat  dusitäcä  (sd.)  .  ,  Y. ,3/.  18;  —  im  jAw.:  mikrS  .  .  ahmäi frasanäayäti  'tamca  vfs^m^a  zantümca dahyümca  daiiihusasilmca  Yt/o.  87;  18, Y.  62. 5,  V.  Ä  1 03,  N.  6';  —  «5 ..  ahmt  'ne .. aähe  vSse  . .  ahmt  *zantvlf  . .  a^he  da^kvB ftim  vaoSata  . .  ahurpm  P./7;  Y.5.  aS,  Vr, 12.  5,  N.(?;  —  *'nyaca  (LS.)*'  vjsyaca  tarda- vaca  *da^havaca  Vr. /2.  gj  —  yujyastTm haia  *'näp'>  a^a  [. .]  vTsal  ha%r?m  {ha&i)
19651:•)  iV.i  Vater  A-,  ist  der  Bruder  Pourusatpas,
20474:«  j.  maSrö.baeäaza-  Adj.  '(Arzt,)  der  mit dem  hnligen  Wort,  durch  Besprechungen damit  kurirt':  ya£  pouruiaSasa  (sd.)  Aait- fasSnie  kar>tS,baiiasSsla  urvarö.baiiasisia 'iis/a  (NS.)'>  V.7.44;  —  'tS  Yt>6.
21228:jAw.:  i)  mit  Ind.:  ^°  aiAlA  amS  mkanie spanasia  irista  . .  ka  hl  asti  aha  V.3.  36; iX  36,  37,  12.  i;  —  y  .  .  caratd  dva  mS apajw>tayaaa  V.y.49;  —  hs para  mintS daSvS  .  ■  y  maiys  maitm  xhtdra  avi franhirftaiti  y  vä  mafys  .  .  xsudranqm *pairi,gmrvayäti  V.  Ä32;  —  hs  ba  .  . arhtqm  MtyS  y  na  paurva  frabda  (Sp. 984  o) /rabdsJrajB  framalxaiti  V.  j8.  40; 34,  46,  54;  —  y  aoxte  aiia  . .  a%a  *ha *x/ayete..  haxäsit (sd.)  ü.g;  7;  — y  hakat *amrute  . .  aliü  *ratu/rii y5 . .  N.24;  — ta^a  y  paiti.barvnti  yä  .  .  äjayaurra N,54;  —  yl>  sSne  piÜr^m  jainti  . . yas»*'^ tat . .  täyus  . .  para.baraiti  dasa  (sd.)  oSj/ päili  afsl  aiayai(sd.)  Y.  13. 10;  —  aät y  bavaiti  avijpastS  sasta  .  .  ta  hascit upajbayäte  Yl  13.  69;  46;  —  yO  nars snaHmt  usihiltaiti  a^at  hl  ag^r^ptam  (sd.) y  frasusaiti  altai  hl  avaoirist»m  {sd.)  y . . Y.4.1T,  —  al^  zr  narS  paityeinti  (sd.) *aslS.vitotus  pgsanaiti  yasla'>''  isui..p»ia- naiti yasca^..Y .4.^^^^; — h^m  ita  (s.Ntr.) tltao^ra  bavairiti  (Sp.  939  O.)  yasj*^  tava frabannte  drvantö  . .  ".  .  dann  .  .  wenn (sie)  dir  darbringen  . ."  Yt.5. 94,  2)  mit Konj.  (oder  Inj.);  y  .  .  masdayasna  .  . nassum  frajasqn  ku%a  . .  v^myqn  "ange- nommen den  Fall:  die  M.  stossen  aul einen  Leichnam  .  .,  wie  .  .?"  V.  6. 36: 5.45,  Äi,  4,  J&i;  —  y  •■  spä  avaca va  bavat , ,  kuha  . .  vjrxyqn  . .  masdqyasna V.  13.  39;  35;  — y  . .  masdayasna  bal^atai (sd.)  fravasänte  katärö  paurvB  ämayänie (sd.)  V.  7. 36;  —  y  iavani  (sd.)  aiwi.- sasls  . .  eis  aiAhe  asti  balfazd  Yt  J4.34; —  y  afvS  zaata  (sd.)  frayatäiti .,  zaoiars gatava  N,  tf/;  70;  —  y  ahmt  nmlne  . . nairika  daxstavaiti  arthal  y  vä  ..  *aipi.- irytS.gatus  isd.)  altala  .  .  V.5.  59;  — y pouruiaist^a  hanjasänte . .  t^m  i^ra  ha*- Jasante  V,  7,44;  YL//.6;  —  yas/a^>  .  . väcim  paiti  taBtii' {sd.)  ar?hat  nsil.. täyus .  .  para.baraiti  Y.J3.40;  —  y  ma^äia frayazantt  .  .  rüsit  t^ra  airyä  daiähävS /ras  hyätYt.i4.^&;  — y paoirim . . itryntäl .  .y ' . ,  ktrmtät'  ava  hö  miryaite  anämStS ZT  ais6  Y.y.^T,  —  nthenyesi:  yeti/a  alte asti  . .  gar>mBkva  (sd.)  vjiänte  y  vä  aiU gar^ma  (sd.)  i^ars^a  stamaruM  .  .  apa.- daiai  .  .  aiühai   haca  .  .  bavainti  p»sB.-
23077:•  j.  'varäna-  m.  Bezeichnung  </aA/iscber Geschöpfe:  aat  ahmi  nmäne zayätüe  daha- käca  mürakäca  (sd.)  pouru^ar^a  'nä/a Y.7/.6.
=== BRT parya
5979:—  y5  "i^wat  mazdä  'lim  . .  yazäi  (sd.)  a Y.J'J.4;  —  ysi  °tois  p?rmatth5  .  .  "die, des  Ungehorsams  voll,  .  ."  Y.rf^.i at  tu  mSi  nöit  'tä  pairyatr/zä   "da   be- fahlst du   mir,  nicht  ohne   dass  ich  ge- horchte" Y.^j.ia'*,
12315:pairyaiTflä ..Y.43-^^'  2)  hinter  dem Relativuni:  . .  mJzä?m  (sd.)  maxda  yehya ta  da%r>m  Y.J4.  13;  —  yl  .  .  däyat anhTusyä  tu  vSista  (sd.)  vahilts  Y. 46.  \o; —  fä  zastayä  ta  haßt  (sd.)  . .  Y.  43.  4;  — ux%3il,.yaisqm  ta  *paouruyB..Jradaxsiä (sd)  ahTY.51.z-  a)  es  folgt  unmittel- bar ein  VS.:  urvatäiS  (sd.)  yä  tu  masdä dfAnSlf  \.44-^5;  — yal/am  ta  aAura irixt^m  (sd.)  . .  vaidUtö  ahi  Y.  32.  T,  — ySngsta'^  mazda  hadtmsi  minai  (sd.)  Y. 46-  14;  —  yähs  tu  J  *aiuramazt/ä msnghalä  .  .  ahä  .  .  Y.j(j.4.
12842:■L  dardinti,  t^yjäyai,  äärayati;  dflai, ;  Dp.  darrJ- dani  gr.  ipenif.  —  Pü. ;  darrUan.  —  ')  Nur  im Inf. •  j.  *dar-  V.  'achten',    Ptaes,  27  dir^ya-. —  PPfP.   •dir^ta-. 'achten':  s.  adsrstö.'. mit  3  'achten  auf  — ,  wachen  über  — ' (Akt.):    darssa  na  pairyaoxtaca  umllanä *äd»nyäte ''  nyde  uslanavaitt!  vJsph  frasu- maitls  (sd.)  P.  S^-
12948:•  j.  (,  g.)  darssa-  m.  i)  'Erblicken,  An- blicken, Blick':  °sa  (IS.) ..  pairyaoxia<a  (sd.) P.5Ä  a)'Anblick'(nurKomp.).  AblS. •sat  als  Inf.  sbes.  [Y.  4(5.16:  lies  s^Sng.- darvsSi.]
15304:•  j.  'par-  V.  'gleich  machen'.  Praes.  4 psra-,  3$  (Pass.)  pairya-.
15551:I):  fei,  (lu  II):  api  hac,  (lu  III):  apc;  s.  noch No.  2  ff.,  6,  8  ff.  —  0  Hds.  pari.  —  »)  D.  i. TOT  oder  nach  der  Rezitation  der  Gs%ä%\  Pü.: pas  -  tu  fralum    kär   ape   kuntt  pas   apasläk gffujet-aiävp/i—ku  afaitik  (Rest  weggelassen). —  3)  Pü.:  ausgelassen.  —  4)  Unsicher.     Pü.: apar.     -    S>  Vgl.  Bipi  II  I   i  (Sp.  83  ">■)■  - 6)    PD.  :    apar  pa  barsm.    —     ?)   S.  dam  Dbr, VglS.  /.   71 1.  —  »'  PS-:  i'  onrfflr  an  apar.  — 9)  Pü. !  *ia/.  —  10)  Pü. :  undeutlich.  —  "»  Pii, : apF,  —  ")  Wörtlich :  "non  profuse  sine  semine', eine  Vermischung  der  beiden  sinngemäss  rich- tigen  Ausdrücke   */rai>har>iäl  pairi  xl'    und tt/raa/iamäl  paiti  xs',    vgl.  anädntxlay-  No. I.     Pü.:    fehlt.    —     '.0  Pü.:    hat.  —   M)  Wo NA.  unrichtig  abteilt ;    s.  Vt,  3,  la  —  >5)  Wo die  Hds.  das  2.  Mal/aiV/  bieten;  s.  Yt.  j.  14. •  j.   *pairi.aoxtay- ",    pairyaoxtay-    f. i)    'Aussprache,    Vortrag':  yezi  araitrim (sd.)  *'ta'^  pairi Jta  Ü.32.         2)  'Zuruf, Befehl':    dansa    nä    'tala    (LS.  als  IS.) uzustanä    *adir»yäte  .  .  frasumaitls  (sd.)
15715:•  j.  pairyaoxtay-  f.:  s.  nat&i pairi,aoxtay-.
18053:•  j.  frasu'mant-  Adj.  (fem.'maifl-)  'sich vorwärts  bewegend,  beweglich' :  dansa  na pairyaoxlaca  taus/a/iä  *äd)rfydte  nyäe a^tanavaitls  vlspä  'maitls  (APf.  statt  n.) "durch  Blick  und  Zuruf  Überwacht  man (alle)  leblose,  leitet  man  alle  lebende  be- wegliche Habe"  P.5*'>.
18598:i)  'Jemanden  leiten,  führen':  darisa  nä pairyaQxtaca  . .  ^nyete  usianavaitli'  vTspä /rasutfiain/ (sd.)  P.jÄ  a)  ["hinführen, hinbringen  zu  —'  (abiy  mit  Akk.):  Äauv {ih''d'laxinam  agarbäye^  anayi^  abiy  mSm Bh.2. 14;  5.1;  —  fravartis  .  .  anayatä (in  pass,  Sbn)  abiy  mim  Bh.2.  13;  — hatev ,.  baitJ*  *anayaiä  (pass.)''  abiy  mäm Bh,  1. 17.  3)  'wegführen,  wegbringen':
19036:asrusts  (sd.)  pairyaoyzä  Y.  43-^  s;  —  ayä'n'  Asvanane  n'^  ..  V.  5.  58;  —  Ab n°  ins  vliyätä  dafaäcinii  (Sp.  595  o.)  Y.  aevS  .  .  apayeiti  hasHt  (Sp.  592  u,)  vä 30.6;  —  mit  Ellipse  von  asti:  avalsam  ^(■akuA.  apayeiti)  n°  vä  Yt.  14.20*^; — mit ff  vlduy!  (sd.)^'  yä  ..Y.  2g.  3.  c)   im  Ellipse  von  äi^Aa  'war':  «•  aSra  frakavS
```


## [2026-09-14T00:56:34.368Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nprint('leaves',len(lv))\n# printed = leaf - 5 (1-based). p.53 -> leaf 58 (1-based) -> index 57; p.60 -> index 64\nfor idx in (57,58,64,65):\n    print('=== idx',idx)\n    print(lv[idx][:1800])\nEOF"
}
```


### [2026-09-14T00:56:35.332Z] TOOL RESULT

```
leaves 725
=== idx 57
                                                pel-                                                   53

 Anlaut nicht einleuchtend Jacobsohn KZ. 42, 264, Schrijnen KZ. 44, 19)
 „Schlacht, Krieg“, got. iisfilma „erschrocken, entsetzt'', usfilmei „Schrecken,
Stauneii“, ohl^felmsf idlr „schreckensvoll, erscbrocken“,        „Schrecken"
felmta „er8chrocken sein, zittern", (alma ,,tappen, unsicher betasten, zittern,
vor Scbrecken verdutzt sein“. Fick KZ. 19,262, Wb.             478, IIP 236;    P
 vgl. aucb Petersson KZ. 47, 246 f, (dessen weitere Anreihung Yon arm.
 liohn „Wind“ und gar von abg. plamenh^ russ. polomja, pldmja ,,Flainme“
 aber nicht iiberzeugt).
    Gegen Yereinigung unseres peJ{emy mit pel- jjStoBend oder schlagend in
 Bewegung setzen, treiben'', s. d.

 5.    pel- in Ausdriicken fur unscharfe Farben wie j.grau, schwarzlich, fahb^,
         auch „scheckig'‘,
   Ai. palitd-, fern, pdliknl (aus -ini) „altersgrau, greis“ (: TtekiivoQ ) parnsd-
                                                                           ;

„fleckig^^    =
             av.             paourusa- „grau, greis“ (Bartholomae Wb. 903;
verkehrt       Wooda Kr. 252); ai.                jjWeifilichgelb, weiB, bleich'' (mit               dem
ind.      Formans -nda-^ Liden Stud,            90),   paiala-                wie
                                                                     „blaBrot^‘     (^-Bildung
Jiataka-, abg. zlato    „Gold“ von ^ghel-, Liden aaO.).
    Arm. dlik „die (weiBen) Wellen(kamme), Wogen; AveiBer Bart, weiBes
 Haar” (—rroAioc, wenn dies nicht etwa              j^og; Hiibschmann Arm.-Gr. I
 412, Liden Arm. St. 61: a aus o in offener Anlautsilbe, nicht Reduktions-
stufe nach Meillet lA. 22, I6f.
    Gr. TieliTvog „grau" (fiir ^nehiog = ai. palitd-h nach dem F
=== idx 58
54                                                        pel-


   Germ.          (s. o.) in aisl.fqlr^ ags.fealo^ as.faht^ ahd./aZo „fahl, falb‘'

(dazu als „graue Asche^^ aisL folski m., ahd. falmviska „Asche, Aschen-
staubchen“) *falha- (: lit. pdlszas^ Much ZfdA. 40, 296) in aleman-rhein-
                     ;


frank. fdlch „falb, bes. von hellbraunem Yieh'';             oder "^feliva- (Holt-
hausen IF. 25, 150) in westfal./*^? „falb^", f^le „fahle Huh, fahles Pferd^‘;
mit dem germ. Z;-Formans wie in anderen Vogelnamen hieher vennutlich
ahd. (usw.) falco „Falke^‘ (Much ZfdA. 40, 295 ff.; spatlat. /'a?co aus dem
Germ., Lit. bei Yf. LEWb.^ s. v., Falk-Torp u. falk. Zur Bed. s. u. apr,
'pele     „Weihe‘').
     Lit.    'palvas     „bla6gelb“               (= germ,       "^fahva,   lat.    palU-dus) = abg. plavz
„wei6^5         skr, pldv „blond, blau“;                 lit.    pole   „Maus“
                                                      (fern, zu ziehog, wenn
dies        etwa aus *7t8h-j^6g; Trautmann Apr. 393 f.), lett. peie ds., apr.
           nicht
peles PI. „Maus (= Armmuskel)‘S apr. pele „Weihe‘^ (wie dt. Falke von
der graubraunen Farbe, Lit. bei Trautmann 392 f.), als Abl. von pele „Maus^^
auch lit. pelehas, lett. peleks ^mausfarbig, fahl, grau“; von einem ^peU
„SchimmeP stammt lit. pele-jti, ~ti „schimmeln“, pelesiai pi. „SchimmeP‘ und
(wohl durch Yerm. eines ^pelekas dieser Bed.) plek-sttt, -ti „schimmeln,
modern^ ob zu pelesiai auch abg. plesnh f. „Schimmel^ formantische Bez.
                ;


hat (s. Osten-Sacken IF. 33, 238), ist angesichts des slav. Formans -sni-
recht fraglich.
     Mit Intonation                einer     set-Basis    lit,    p'dkas    „grau“     (s.   auch    u.   pelaq-
„Sumpf^), pdlszas, letfc. palss „fahl“ l^pohkos); apr, po
=== idx 64
60                                                pel-



          flouw {"^fleiva-) „lau schlaff^^ (daraus dt.
Til.vloiiiVy                                                  die Abschwachung
der Bed. im Germ, mag durch das reimende            yeranlafit seia. S. J. Schmidt
Yoc. n, 271, Fick 111* 249. Hochst fragwiirdige Anreihungen bei Falk-
Torp u. flaas^ flusj flarlce sig.

13. pel- in          Worten fur „Staub, Mebk*, weiter auch „Meblbrei“.
     Gr.   7id}.ri   „Staub, Staubmehl“,         Ttai-ndXrjj   jza-oTtdXt]   „feiaes   Mehk‘   (zur
Kedupl.       s.   Brugmann        727,   II ^   i,   128, 129;    ob zu     TtdXr]   auch naXvvm
„bestreue'^?         s.    „Haut“); ai. (Uhlenbeck s. v.) pdlala- n. „zerriebene
                          u. pel
Se&amkorner, Brei,        Schmutz“; mit f-Formans Tzolxog „Brei aus Mehl“,
Dem. nohiovy nolrdQiov, lat. ptdsy ~tis „dicker Brei von Speltmehk' (wohl
  polios^ = Oder aus gr, n6XTog)\ mir. IHim (gen. Utten)^ nir. lite^ cymr.
llitli {i statt y nach llith „K6der“) „Mehlsuppe^           pulmentum^* (^pltno-;
Stokes IP. 2, 173, Fick II* bl, 252, Pedersen KG. I 160).
    Mit w-Formans: lat. pulvis^ ~eris „Staub“ (^polui-; Flexion nach cinis;
nicht nach Brugmann IF. 17, 488 zu apr. pelivo „Spreu^‘ usw., s. u. pel-
„Haut‘‘). Nicht hierher cymr. nJw „favilla'^ bret. ulven „duvet, qui s'eleve du
liUj quand on le peigne“ (Pick 11* 53, Pedersen EG. I 33; auch in poit.

auveche „Kohlenstaub“ nach Meyer^Lubke ZfromPh. 34, 125).
    Aus dem Bilde des flimmernden Staubwirbels erklart Bartholomae IF.
31^ 35 ff. auch den Plejadennamen np. parv ("^pelui- oder *polui-)^ parvm,
av. paviryaenas\ca und gr.IIkeiddeg (Ausgang nach ^Yddeg; nXe^i- sei aus
         nach nlej^co umgestellt); doch modifiziert dies Moller Or. d. Z. 1914,
62 f. vielleic
=== idx 65
pela- „breit und flach, ausbreiten; durch Druck oder Schlag flacb formen,
     breitschlagen, breitklatschen“.
  Lat. palam          5
                          jOffenj offentlich,vor den Augen der Leute'* (eig, .jin flacher,
offener Hinbreitung“,                Akk., wie clain^ von einem        oder          nicht        ^


naher zu paJma^ Meringer IF. 17, 160, wobei ein weiterer Kasusausgang
zu erwarten ware); russ. polyj „offen, frei, nnbedeckt, hohl, leer"' (auch
.,ausgetreten, vom Wasser^', in dieser Bed. anderer Herkunft? s. v. d. Osten-
Sacken IP. 33, 237. Versnche, auch abg. usw. poh „Halfte“ damit zu ver-
einigen, bei Pedersen KZ. 38, 374 und Masing Padag, Anzeiger f. RuBland
1911, Nr. 12; vielleicht von „Seite“ aus, wie bei ir, leth- „halb'' loth ,,Seite“:        :



lethan „breit“, s. u. pld-)^ abg. polje ,,Feld“ f„ausgebreitete Fiache^', wie
dt. Feld), aschwed.-nschwed. /a/a „Ebene, bes. bauinlose; Heide^^ (Persson
Beitr. 227 f. — Pick III*^ 568  aber gr. em-noXi) „Oberflache'‘, z. B. schon
                                               ;



bei Pick BB. 2, 200, bleibt      TieXofim), alb.      „offenbare“, psrpal .,Yev-
6ffentliche“ Jokl SBx\k. Wien 168.1. 83 f.
  tJber arm. hot „Erde, Staub, Boden,                          Land“ s. Pedersen KZ. 39, 370.
  Mit Formans                 zum Typus Brugmann TI- 1, 408 f.) *pd-to- 7nj
                             -to-    (vgl.
"^pl-td „Plache'‘ mahd. /eZcZ „Peld, Boden, Flache, Ebene% as.-ags./*eW ds.,
aisl. /‘oZfZ „Erde, Feld“, ags. folde^ as. /'oWa „Erd-, Land-, Erdbodea“ (die
Vokalstellung von Feld widerrat nahere Verkniipfting mit ai. prfliivl^ pra-
thate usw,, Wzf. -plet{h)-^ z. B. bei Pick III*, 244 zw., Falk-Torp u. felt
nach Persson Wzerw. 33; aisl. fjall^ fell n. „Gebirge“ wohl nicht als "^felpa-
oder,
```


## [2026-09-14T00:56:58.264Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN falcon\"; grep -n -i \"^falcon\\|falcon, n\" KLN_1966.txt | head -5\ngrep -n -i \"falco, 'falcon'\\|L\\. falco\\|falcon,\\ n\\.\" KLN_1966.txt | head -5\necho \"=== KLN powder\"; grep -n -i \"powder, n\\.\\|pulvis\" KLN_1966.txt | head -8\necho \"=== KLN pollen\"; grep -n -i \"pollen, n\\.\" KLN_1966.txt | head -5\necho \"=== KLN appall\"; grep -n -i \"appall\\|appal,\" KLN_1966.txt | head -5\necho \"=== KLN pale\"; grep -n -i \"pallere\\|pallēre\" KLN_1966.txt | head -5"
}
```


### [2026-09-14T00:56:59.481Z] TOOL RESULT

```
=== KLN falcon
14325:falconer,  n.  —  ME.  fauconer,  fr.  OF.  falconier, fauconier  (F.  fauconnier),  fr.  faucon.  See  falcon, falcula,  n.,  a  sharp-pointed  claw  (zool.)  —  L., ‘sickle’.  See  falcate.
14324:falchion,  n.,  1)  a  short  curved  sword;  (poet.)  any sword.  —  ME .fauchoun,  fr.  OF.  fauchon,  fr.  VL. *falcidnem,  acc.  of  *falcio,  dimin.  of  L.  falx, gen  .falcis,  ‘sickle’.  See  prec.  word  and  suff.  -ion. falciform,  adj.,  sickle-shaped.  —  Formed  fr. L.  falx,  gen.  falcis,  ‘sickle’,  and  forma,  ‘form, shape’.  See  falcate  and  -form, falcon,  n.  —  ME.  faucoun  fr.  OF.  (=  F.)  faucon, fr.  Late  L.  falconem,  acc.  of  falco,  prop,  ‘the bow-legged  (animal)’,  and  identical  with  L. falco,  -onis,  ‘bow-legged’,  fr.  falx,  gen.  falcis , ‘sickle’,  for  which  see  falcate.  For  sense  develop¬ ment  cp.  Gk.  Spirt),  ‘sickle;  kite’.  OHG.  falcho (MHG.  valke,  G.  Falke),  MDu.  valke  (Du.  valk), ON:  falki,  are  Latin  loan  words.  Cp.  gerfalcon. Derivatives:  falcon,  intr.  v.,  falconer,  n.  (q.v.) Falcon,  n.,  the  typical  genus  of  falcons  ( ornithol .) —  L.  falco.  See  falcon.
=== KLN powder
29410:pollen,  n.,  the  fertilizing  male  element  of  flowers. —  L.,  also  pollis,  ‘fine  flour,  milldust’,  fr.  I.-E. base  *pel-,  ‘dust,  porridge  made  of  meal’, whence  also  pollenta,  polenta,  ‘peeled  barley’, pulvis,  ‘dust’,  Gk.  7t6Xto?,  ‘pap,  porridge' (whence  L.  puls,  gen.  pultis,  of  s.m.),  na. Xr), ‘sifted  meal’,  OI.  pdlalam,  ‘ground  seeds’, OPruss.  pelanne,  ‘ashes’,  Lith.  pelenaT,  Lett. pelni,  OSlav.  popelU,  Russ,  pepelu  (formed through  the  reduplication  of  the  base),  ‘ashes’. Cp.  pollinate.  Cp.  also  polenta,  powder,  pulse, ‘seeds’,  poultice,  pulverize,  and  the  second  ele¬ ment  in  Paspalum.
29872:powder,  n.  —  ME.  poudre,  fr.  OF.  (—  F.)  poudre, fr.  OF.  poldre,  p(o)udre  (F.  poudre),  fr.  L.  pul- verem,  acc.  of  pulvis,  ‘dust,  powder'.  See  pollen and  cp.  words  there  referred  to.
30983:pulton,  pultun,  n.,  a  native  infantry  regiment  in India.  —  Hind,  paltan,  fr.  E.  battalion;  prob. influenced  in  form  by  E.  platoon. pulverize,  tr.  v.,  to  reduce  to  dust;  intr.  v.,  to  be reduced  to  dust.  —  MF.  (=  F.)  pulveriser,  fr. Late  L.  pulverizare,  fr.  L.pulvis,  gen.  -eris,  ‘dust’. See  pollen  and  cp.  powder.
30985:pulverulence,  n.,  the  state  of  being  covered  with dust.  —  Formed  from  next  word  with  suff.  -ce. pulverulent,  adj.,  covered  with  dust.  —  L.  pulveru- lentus,  ‘full  of  dust’,  fr.  pulvis,  gen.  -eris.  See pulverize  and  -lent.
=== KLN pollen
=== KLN appall
3157:Derivative:  apotheos-ize,  tr.  v. apotropaion,  n.,  an  amulet,  a  charm,  anything supposed  to  avert  evil.  —  Gk.  a7TOTp6traiov, neut.  of  anoTpoTratoi;,  ‘that  which  averts  ,  fr. txmozpi.Kci'J,  ‘to  turn  away,  avert’,  fr.  ino  (see apo-)  and  tpetieiv,  ‘to  turn’.  See  trope, apozem,  n.,  a  decoction  ( pharm .)  —  F.  apozeme, fr.  L.  apozema,  fr.  Gk.  atr6ijsp.a,  ‘decoction  , fr.  aro^ctv,  ‘to  boil  till  the  scum  is  thrown  off’, fr.  airo  (see  apo-)  and  CeTv,  ‘to  boil’.  See  ec¬ zema  and  cp.  words  there  referred  to. appall,  tr.  v.  —  ME.  appallert,  apallen,  ‘to  make pale,  become  pale’,  fr.  OF.  apallir,  ‘to  grow pale’,  fr.  a,  ‘to’  (see  a),  and  pallir,palir(¥  .palir), ‘to  grow  pale’,  fr.  pale  (F.  pale).  See  pallor  and cp.  pale,  pallid.
14333:Fallopian,  adj.,  discovered  or  described  by  Ga¬ briel  Fallopius  (in  Italian  Gabriele  Fallopio), the  celebrated  Italian  anatomist  (1523-62). Fallopian  tubes,  the  oviducts  of  mammals.  —  So called  because  they  were  discovered  and  first described  by  Fallopius.  See  prec.  word, fallow,  adj.,  brownish  yellow.  —  OE.  fealo,  gen. fealwes,  ‘dull-colored,  yellow,  yellowish  red, brown’,  rel.  to  OS.  falu,  ON.  fair,  MDu.  valu, vale,  Du.  vaal,  OHG.  falo,  MHG.  vat,  vafwer, G.  fahl,  falb,  fr.  I.-E.  base  *pel-,  ‘dark-colored, gray’,  whence  also  OI.  palitah,  ‘gray’,  pandtih (for  *paln-du-),  ‘whitish,  pale’,  Arm.  alik‘, ‘waves;  white  beard’,  alevor,  ‘gray’,  Gk.  ireXi6? (prob.  for  *ireXi-F6?),  ‘livid’,  ireXiTv6?,  Ion. ireXiSvb?,  ‘gray’,  ireXXo?,  (for  *ireXio?  or  *iteX- vo?),  ‘dark-colored,  dusky’,  iteXapY^,  ‘stork’ (for  *irEXaF-ap-|-6?),  ‘stork’,  lit.  ‘the  blackish white  bird’,  ntXzux,  ‘pigeon’,  lit.  ‘the  dark- colored  bird’,  iroXi6?  (prob.  for  *110X1-/6?), ‘gray’,  L.  pallere,  ‘to  be  pale’,  pallor,  ‘paleness’, pullus,  ‘dark-colored,  blackish  gray,  dusky’, palumbes,  ‘wood  pigeon’,  lit.  ‘the  dark-colored bird’,  OSlav.  plavit,  Lith.  palvas,  ‘sallow’,  pil- kas,  ‘grey’,  pike,  ‘mud,  mire’,  pel l,  ‘mouse’, OPruss.  poalis,  ‘pigeon’,  MIr.  Hath,  W.  llwyd, ‘gray’.  Cp.  appall,  favel,  pale,  adj.,  pall,  v.,  pal¬ lid,  pallor,  Pelargonium,  Pellaean,  peristeronic, Pleiad,  polyomyelitis.
27022:Derivatives :  pall ,  tr.  v.,palli-al,  adj ,,pall-ed,  adj. pall,  intr.  v.,  to  become  insipid.  —  ME.  pallen, prob.  aphetic  for  apallen,  ‘to  appall’.  See  appall. Palladian,  adj.,  in  the  style  of  the  Italian  archi¬ tect  Andrea  Palladio  (1518-80).  —  For  the  end¬ ing  see  suff.  -an.
27034:pallor,  n.,  paleness.  —  L.  pallor,  ‘paleness’,  fr. pallere,  ‘to  be  pale’,  rel.  to  pullus ,  ‘dark-colored, blackish  gray,  dusky’,  palumbes,  ‘wood  pigeon’, lit.  ‘the  dark-colored  bird’,  fr.  I.-E.  base  *pel-, ‘dark-colored,  gray’,  whence  also  OI.  palitdb, ‘gray’,  pandiih  (for  *paln-du-),  ‘whitish,  pale’, Gk.  ireXi.6;,  ttsaiSvo;,  ‘livid’,  tteXXo^;  ‘dark- colored,  dusky’,  raXapYo?  (for  *7reXa.F-apY6s ), ‘stork’,  lit.  ‘the  blackish  white  bird’,  msXeia, ‘pigeon’,  lit.  ‘the  dark-colored  bird’,  tzdkiot;, ‘gray’,  OE.  feato,  ‘dull-colored,  yellow,  yellow¬ ish  red,  brown’.  See  fallow,  ‘brownish  yellow’, and  cp.  pale,  pall,  v.,  pallid,  appall, palm,  n.,  the  inner  part  of  the  hand.  —  ME. palme,  fr.  OF.  palme,  paume  (F.  paume),  ‘palm of  the  hand’,  fr.  L.  palma,  of  s.m.,  which  is cogn.  with  Gk.  mxXdcpT],  ‘open  hand,  palm’, OIr.  lam,  W.  Haw,  OCo.  lof  ‘hand’,  OE.  folm, OHG.  folma,  of  s.m.,  and  with  OI.  panih  (for *pdlnifi),  ‘hand;  hoof’.  All  these  words  derive fr.  I.-E.  base  *pild-,  ‘spread  out,  flat’,  for  which see  plain,  adj.,  flat.  Cp.  palama.
=== KLN pale
14333:Fallopian,  adj.,  discovered  or  described  by  Ga¬ briel  Fallopius  (in  Italian  Gabriele  Fallopio), the  celebrated  Italian  anatomist  (1523-62). Fallopian  tubes,  the  oviducts  of  mammals.  —  So called  because  they  were  discovered  and  first described  by  Fallopius.  See  prec.  word, fallow,  adj.,  brownish  yellow.  —  OE.  fealo,  gen. fealwes,  ‘dull-colored,  yellow,  yellowish  red, brown’,  rel.  to  OS.  falu,  ON.  fair,  MDu.  valu, vale,  Du.  vaal,  OHG.  falo,  MHG.  vat,  vafwer, G.  fahl,  falb,  fr.  I.-E.  base  *pel-,  ‘dark-colored, gray’,  whence  also  OI.  palitah,  ‘gray’,  pandtih (for  *paln-du-),  ‘whitish,  pale’,  Arm.  alik‘, ‘waves;  white  beard’,  alevor,  ‘gray’,  Gk.  ireXi6? (prob.  for  *ireXi-F6?),  ‘livid’,  ireXiTv6?,  Ion. ireXiSvb?,  ‘gray’,  ireXXo?,  (for  *ireXio?  or  *iteX- vo?),  ‘dark-colored,  dusky’,  iteXapY^,  ‘stork’ (for  *irEXaF-ap-|-6?),  ‘stork’,  lit.  ‘the  blackish white  bird’,  ntXzux,  ‘pigeon’,  lit.  ‘the  dark- colored  bird’,  iroXi6?  (prob.  for  *110X1-/6?), ‘gray’,  L.  pallere,  ‘to  be  pale’,  pallor,  ‘paleness’, pullus,  ‘dark-colored,  blackish  gray,  dusky’, palumbes,  ‘wood  pigeon’,  lit.  ‘the  dark-colored bird’,  OSlav.  plavit,  Lith.  palvas,  ‘sallow’,  pil- kas,  ‘grey’,  pike,  ‘mud,  mire’,  pel l,  ‘mouse’, OPruss.  poalis,  ‘pigeon’,  MIr.  Hath,  W.  llwyd, ‘gray’.  Cp.  appall,  favel,  pale,  adj.,  pall,  v.,  pal¬ lid,  pallor,  Pelargonium,  Pellaean,  peristeronic, Pleiad,  polyomyelitis.
26970:pale,  adj.,  whitish,  wan.  —  ME.,  fr.  OF.  pale  (F. pale),  fr.  L.  pallidus,  ‘pale’,  fr.  pallere,  ‘to  grow pale’.  Sec  pallor  and  cp.  words  there  referred  to. Derivatives:  pale,  intr.  and  tr.  v.,  pale-ly,  adv., pale-ness,  n.
27030:palliation,  n.  —  MF.  (=  F.),  fr.  ML . palliationem, acc.  of  pallidtio,  fr.  Late  L.  pallidtus ,  pp.  of palliare.  See  prec.  word  and  -ion. pallid,  adj.,  pale;  wan.  —  L.  pallidus,  ‘pale’,  fr. pallere,  ‘to  grow  pale’,  rel  to  pallor,  ‘paleness’. See  pallor,  and  cp.  words  there  referred  to. Derivatives:  pallid-ly,  ad v.,  patlid-ness,  n. pall-mall,  n.,  an  old  game.  —  MF .  pallemaille,  fr. It.  pallamaglio,  lit.  ‘ball-mallet’,  ft.  palla,  ‘ball’, and  maglio,  ‘mallet*.  The  first  element  is  a  Teut. loan  word ;  see  ball,  ‘a  round  body’,  and  cp. pallone.  The  second  element  derives  fr.  L.  mal¬ leus,  ‘a  hammer’ ;  see  malleus, pallone,  n.,  an  Italian  game.  —  It.,  ‘large  ball’.
27034:pallor,  n.,  paleness.  —  L.  pallor,  ‘paleness’,  fr. pallere,  ‘to  be  pale’,  rel.  to  pullus ,  ‘dark-colored, blackish  gray,  dusky’,  palumbes,  ‘wood  pigeon’, lit.  ‘the  dark-colored  bird’,  fr.  I.-E.  base  *pel-, ‘dark-colored,  gray’,  whence  also  OI.  palitdb, ‘gray’,  pandiih  (for  *paln-du-),  ‘whitish,  pale’, Gk.  ireXi.6;,  ttsaiSvo;,  ‘livid’,  tteXXo^;  ‘dark- colored,  dusky’,  raXapYo?  (for  *7reXa.F-apY6s ), ‘stork’,  lit.  ‘the  blackish  white  bird’,  msXeia, ‘pigeon’,  lit.  ‘the  dark-colored  bird’,  tzdkiot;, ‘gray’,  OE.  feato,  ‘dull-colored,  yellow,  yellow¬ ish  red,  brown’.  See  fallow,  ‘brownish  yellow’, and  cp.  pale,  pall,  v.,  pallid,  appall, palm,  n.,  the  inner  part  of  the  hand.  —  ME. palme,  fr.  OF.  palme,  paume  (F.  paume),  ‘palm of  the  hand’,  fr.  L.  palma,  of  s.m.,  which  is cogn.  with  Gk.  mxXdcpT],  ‘open  hand,  palm’, OIr.  lam,  W.  Haw,  OCo.  lof  ‘hand’,  OE.  folm, OHG.  folma,  of  s.m.,  and  with  OI.  panih  (for *pdlnifi),  ‘hand;  hoof’.  All  these  words  derive fr.  I.-E.  base  *pild-,  ‘spread  out,  flat’,  for  which see  plain,  adj.,  flat.  Cp.  palama.
27902:Pelargonium,  n.,  a  genus  of  plants  (bot.)  — —  ModL.,  fr.  Gk.  7TEXapY<k,  'stork',  which stands  for  ‘jrEXx-Fapyoi;,  lit.  ‘blackish  white’. The  first  element  of  this  word  is  rel.  to  treXt 6$, ‘livid’,  tteXXo?,  ‘dark-colored,  dusky’,  7:0X16?, ‘gray’,  and  cogn.  with  L.  pallere,  ‘to  be  pale’, pallor,  ‘paleness’,  OE.  fealo,  ‘dull-colored,  yel¬ low,  yellowish  red,  brown’.  See  fallow,  ‘brown¬ ish  yellow’,  and  words  there  referred  to  and  cp. esp.  Pellaea.  For  the  second  element  see  argent. Pelasgian,  adj.,  of  the  Pelasgi;  n.,  one  of  the  Pe- lasgi.  —  Formed  with  suff.  -an  fr.  L.  Pelasgius, fr.  Gk.  IleXixCTYio?,  ‘of  the  Pelasgi’,  fr.  IleXoca-
```


## [2026-09-14T00:57:00.805Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW falco\"; grep -n -i \"falco\" LEW_1910.txt | head -8\necho \"=== LEW pulvis\"; grep -n -i \"pulvis\" LEW_1910.txt | head -8\necho \"=== LEW pollen\"; grep -n -i \"pollen,\" LEW_1910.txt | head -5\necho \"=== LAT falco/pulvis\"; grep -n -i \"falco\\b\" LAT.txt | head -5; grep -n -i \"pulvis\" LAT.txt | head -5\necho \"=== SYN grey\"; grep -n \"4\\.6[0-9] \\|GRAY\\|GREY\" SYN.txt | head -10"
}
```


### [2026-09-14T00:57:00.945Z] TOOL RESULT

```
=== LEW falco
=== LEW pulvis
=== LEW pollen
=== LAT falco/pulvis
9829:10,145, qui d 4 signerait aussi, comme le latin falco, les bommes dont
20356:falco, - 5 nis m.: faucon. V.falx. Peut-etre calque semantique de
20414:*defalcb, 3516; falco,-onis a.: -nes dicuntur quorum digiti pollices
20416:peut-etre a rapprocher de falco,-onis "faucon" que les gloses ex-
=== SYN grey
6908:4.61 SLEEP (vb.; sb.)
6935:4.62 DREAM (sb.)
6955:4.63 WAKE (a, trans., b, intr.)
6995:4.64 BREAK WIND, FART (vb.)
7029:4.65 URINATE; URINE
7052:pARTS OF 4.66 VOID EXCREMENT; EXCREMENT, DUNG taae ee Goth. . ; maihstus, Lith.  Sikti; $udas, méSlas k KaKKaO, xe} Noe smarna Lett. dirst; stids, mésls
7135:4.67 HAVE SEXUAL INTERCOURSE
24305:14.53 14.61 14.62 14.63 14.64 14.65 14.66 14.67 14.68 14.71 14.72 14.78 14.74 14.75 14.76 14.77 14.78
25567:14.61 WEEK
25613:14.62 SUNDAY
```


## [2026-09-14T00:57:21.055Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN gray concept\"; grep -n -i \"15\\.6[0-9]\\|GRAY\\b\" SYN.txt | head -10\necho \"=== SYN OLD\"; grep -n \"14\\.15 OLD\\|OLD (1)\\|^14\\.15\" SYN.txt | head -5\necho \"=== IEC peluos\"; grep -n \"^peluos\\|^pelouos\\|pelos\\b\\|^pel-\" IEC.txt | head -20"
}
```


### [2026-09-14T00:57:21.141Z] TOOL RESULT

```
=== SYN gray concept
882:1. Grk. rydés, Dor. rads most com- monly potters’ and masons’ ‘clay’ (9.73), strictly moistened earth (vii dypd dupa- Geioa Plat. Tht. 147c), but also ‘mud’ (Hdt., Aristoph., etc., and so clearly in NT Jn. 9.6, though rendered as ‘clay’ in our versions since Wycliff), etym. dub. ; perh. (if ‘clay’ is the earlier sense) : Grk. rodtés ‘gray’, Lat. pallére ‘be pale’, ete. Walde-P. 2.53 (1.441). Boisacq 779.
1944:Pol. chmura ‘cloud’ : Boh. chmoura, Russ. chmura ‘dark cloud’, beside Russ. smuryj ‘dark gray’, etc. Root connec- tion dub., but notion of ‘dark’ the im- mediate source. Miklosich 311. Briick- ner 180.
1955:The present differentiation of NE mist, fog, and haze cannot be matched in the other languages, where with some eX- ceptions the same word answers roughly to all three. Many of the words are cop- nate with some of those for ‘cloud’. Others are from such diverse notions as ‘vapor’, ‘dim’, ‘gray’, ‘wet’, ‘winter’, etc.
1970:3. Ir. cdo (gen. ciach), NIv. ceo, perh. : Ir. ciar ‘dark brown’, OF har ‘gray’ (NE hoar), ete. Walde-P. 1.360.
1977:NE haze, prob. a back-formation fr. hazy, earlier hawsey, this fr. OE hasu, haswe ‘gray’: Lat. canus ‘gray’, etc. Walde-P. 1.357. Falk-Torp 380.
3760:Color words underlie some, as ‘brown’ in the Gme. words for ‘bear’ (3.73) and an IE word for ‘beaver’ (NE beaver, etc.); ‘gray’ in Lith. pelé ‘mouse’ (3.63) and prob. a widespread word for ‘hare’
3762:k ‘gray’), possibly ON griss ‘pig’ (8.35);
4470:‘gray’, etc. Walde-P. 1.602f. TFalk- | ssdéi ‘suck’. 3.36 3.37 3.38 GOAT HE-GOAT KID (Generic or feminine) Grk. al (xlpatpa) Tp&yos épidos NG ylét, fem. yida  rpa&yos, rpayl karolxe Lat. capra hircus, caper haedus It. capra becco, capro capretto Fr. chevre, bique bouc chevreau, biquet Sp. cabra, chiva cabrén cabrito Rum. capré lap caprioard Ibe, gabor boce menn(dn) Nir. gabhar boc mionnan W. gafr bweh myn Br. gaor bouc’h gaorig Goth. gaits Sante pueceis | ON get hafr (bukkr) kid | Dan. ged buk kid Sw. get bock kid OE gat bucca, hafor ticcen, hécen ME pote bucke kide NE goat he-goat kid Du. geit bok geitje OHG  geiz, ziga boc zicki(n), kizzt(n) - MHG geiz, zige bock 2ickelin NHG ziege, geiss bock zicklein Lith. oka ozys ozelis, ozkutis Lett. kaza Gzis kazlens ChSl. koza koztlit koztle SCr. koza jarac Jare, kozlié Boh. koza kozel kizle Pol. koza koziot koéle Russ. koza kozel kozlenok Skt. _aja-; fem. aja- aja-, chaga- “a Av. i tlcts biza-
4891:6. SCr. maéka, Boh. macka (obs.), orig. a pet-name form of Maria, like NHG Mieze, Mies also used for ‘cat? (Weigand-H. s.v.), NE Malkin, pet- name form of Matilda, used for ‘cat? (NED s.v. 5), also Gray-Malkin (Shaks.), Grimalkin (NED s.v.). The masculines, SCr. maéek, Boh. macek, are, of course, by this view formed sec- ondarily to the feminines. Berneker 2.1.
4902:5. Lith. pelé, Lett. pele, orig. ‘the gray one’: Lith. pilkas ‘gray’, Grk. medtds ‘livid’, etc. Walde-P. 2.54.
=== SYN OLD
24433:14.15 OLD
=== IEC peluos
489:ambh- (ombh-, mbh-), px. ‘round’. WP I, 54. Cf. ambhi Arm. cf. amb-oy£ ‘whole’; Gk. cf. ám-, án- in ámpelos, ántux; lat. amb- in ambire, an-quiro, etc.; W am-. Cf. Alem. sich em- meln ‘twist
12475:pal- (2) ‘straw, chaff. Skt. ambig. Cf. pelos Skt. palah, m. id.; Lat. palea, f. ‘chaff; R cf.
12620:pel- (pels-) (1) “strike, urge, drive Cf. pels- as a separate entry. WP II, 57. Semantics obscure. Cf. pelm- (3) Gk. cf. a-peiléo, a-péllo, v. ‘round up; threa- ten; warn; boast; swear; cf. a-pellaí, fpl. ‘assembly’; (here also?) á-pelos, m. ‘wound, sore' (all fr. a type *sm-^); Lat. pello, ére, pf: pepuli, v. ‘drive, strike’; Olr. cf. ella- cpds. “go”; ellam, adj. “quick. Ambig. (?) < *pels-); W (?) elu, inf. (move on, go’, if fr. *pel-); Du. (?) velen, v. ‘suffer, endure’; Slovene pel- jati, inf. ‘lead’; Big. (?) pelëja, also pilěja, v. ‘squander’; Latv. peļu, pelt, v. ‘pound, knock, throb; calumniate'. For the extn. of type *pels- cf. Umb. pelsanu, acc. m. (‘to be mashed" or sim.); Cz. plísnit, inf. “abuse, scold’; Latv. pelsans, adj. ‘foose’, and perh. LG fell, adj. (evil, wild’. LW in OFr. fel, It. fello, but see pelk- below)
12621:pel- (2) ‘grey; grey object or creature’. WP II, 53. (Variant: pelit-) Skt. cf. palitah, adj. ‘grey, hoary’; Arm. cf. ey- in eyeamn, gs: eyeman, s. (“hoarfrost, drizzle'. See pelm- (1)); Gk. pelós, pélios, pél- los, adj. "dark dun’; cf. pel-argós (Cgrey-white', epithet of ‘stork’ or ‘crane’) and péleia, f. ‘dove’; pelitnós, adj. "bvd: Ir. cf. eala, pl: ealaí, f. ‘swan’; R cf. pel-esnyj ‘pallid, fal- low’; pépel, m. Cash fr. a type *pel-pel-) be- side plésni, plésenií, Cz. plíseň ‘mildew’ (fr. *pelsen-); Li. peléju, čti, v. ‘grow mouldy’; pele, f. ‘mouse’; Latv. pele, f. id.; cf. Li. Latv. peleda, f. *ow?; Li. pélenai, pl. ‘ashes; pele- siai, pl. ‘mildew’; Latv. cf. pelēks, adj. ‘grey’; pelécis, s. ‘grey creature’; pelu, ét, v. “turn grey, get mildewed'; pelni, mpl. «ashes
12624:pel- (pels-) — peln-
12649:pelos ‘chaff, straw’. Cf. pel- (2), pal- (2) Skt. palah, m. ‘straw’; Li. pelai, mpl. ‘chaff; pélas, m. ‘awn’; Latv. cf. pelus, pelavas, pl. ‘chaff; OE cf. fileóe, filióe, n. “hay?
12670:peluos ‘dust, specks, chaff. Variant pelouos, q. v. Cf. pelsmn- (2) Oss. cf. fárwakà, färakä ‘bran’; Skt. cf. palavam, n. ‘chaff, husks’; Lat. (e-, o- or z-gde) pulvis, gs: pulveris, m. ‘dust, powder’; ON. fol, f. ‘thin blanket of snow; R. Ukr. polóva, f. ‘chaff beside Ukr. pliva, f. ‘film’; Cz. pleva, f. ‘chaff ; Latv. cf. pelavas, pelus, id. (pl.); LW in Finn. pelu ‘chopped straw, chaff
13944:quelos, -es- ‘turn, turning’. Cf. quel-, queló, quolos, etc. WP I, 514 Skt. cf. Calab, čarab, adj. ‘mobile’; Ober, cf. abi-Cari$ (^pasture', fr. *mbhi-^); Oss. cf. (*-e-) car, S. “ceiling, vaulting’; Arm. Keyi, gs: -vo, ab. s. -eav ‘shaft, pole, rudder, helm’; (o-gde in) olok, i, av & olokKn, gs: olokan ‘shank, shin’; olor, i-st. ‘twist, curl’; Gk. cf. ám-pelos, m. (‘vine’, fr. mbhi-^); pólos, m. (axis; vault; turned-up earth', fr. *quolo-); Alb. siellé, mf. ‘crank; winder; screw-propeller'; Lat. (*-e- or Sol colus, gs: -üs and -i, f. 'spinning-wheet'; colos & color, gs: -oris, m. “colour, appear- ance’; cf. also columba (pigeon', if fr. *quol- uendh-?); ON hvel, ds: hveli, n. (^wheel'. Cf. quequol-); OCS (*-e- or *-o-) kolo, gs kola and kolese, n. (^wheel, and com. Sl); Li. kélias, m. "road: kelys, gs: -io, m. ‘knee’; Latv. cel3 “road; celis ‘knee’. Cf. also the Lat. cpds. in-cola ‘inhabitant; in-quiflinus ‘tenant’; ex- quiliae ‘outhouses’
15791:(skopelos, skopalos. See Supt:S)
15797:skopelos, skopolos — skortos, is
```


## [2026-09-14T00:57:22.386Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pale",
 "prompt": "Give the etymology of \"pale\" (adjective): Old French pale, Latin pallidus/pallere, and the PIE root *pel- \"pale\" and its cognates. Also mention appall if present."
}
```


### [2026-09-14T00:57:26.610Z] TOOL RESULT

```
# Etymology of "Pale" (Adjective)

The adjective "pale" originates in the early 14th century, describing "a whitish appearance, bloodless" complexion. The word traces back through Old French *paile* to Latin *pallidus*, meaning "pale, pallid, wan, colorless."

The ultimate source is the Proto-Indo-European root **\*pel-** (1), signifying "pale." This root also generated related terms like *pallid* (a doublet of pale) and *pallor* (paleness).

The Latin verb *pallere* ("be pale, grow pale") forms the semantic core of this etymological family, producing various descendants across Romance languages indicating paleness or lack of color.

**Note:** The document does not mention "appall" in connection with this etymology, so I cannot comment on that relationship based on the provided content.
```


## [2026-09-14T00:57:33.856Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '24433,24470p' SYN.txt | head -50\necho \"=== search pir in SYN\"; grep -n \"Pers\\. pir\\|pir ‘old\\|pīr\" SYN.txt | head"
}
```


### [2026-09-14T00:57:33.932Z] TOOL RESULT

```
14.15 OLD
Grk. adatés, dpxatos, Goth. fairneis, alpeis, Lith.  senas
yépwv sineigs Lett. veces NG madtés, apxatos ON forn, gamall ChSl.  vettichit, slarit Lat. velus, senex Dan. gammel : SCr. star It. vecchio Sw. gammal Boh. _ stary Fr. vieux (ancien) OE eald, gamol Pol. stary Sp. viejo ME old Russ.  staryj Rum. vechiu, batrin NE old (ancient) Skt. jirna-, sana-, vrddha- Tr. sen Du. oud Av. hana- NIr. _ aosta, crionna, sean- OHG | allt, firni W. hen MHG allt, virne Br. koz, hen- NHG alt
Most of the words for ‘old’ are used alike for ‘old’ vs. ‘new’ and ‘old’ vs. ‘young’, and this is to be understood in the following, except as otherwise noted. But a few are used wholly or chiefly in the latter sense, esp. of old persons; and this was the orig. application of many of the others, as indicated by their etym.
1. TB *sen-. Walde-P. 2.494. Er- nout-M. 922 f.
Lat. senex (of living things, mostly persons); Ir. sen, NIr. sean, W. hen (Br. hen- as prefix, as often Ir. sen- and most- ly NI. sean-); Goth. sineigs, super. sin- ista (only of persons, ‘rpecBirns, mpeoBbre- pos’); Lith. senas, Skt. (Ved.) sana- (opp. to nava- and yuvan-), sanaya-, Av.
hana- (quotable only for old persons); Arm. hin; cf. Grk. é&os ‘of last year’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
évn kal véa (Sc. jyépa) ‘the old and new day’ = ‘last day of the month’, ON sina ‘dry standing grass from the previous year’.
2. Ii *wetus- (*wetos-?), prob. : Grk.
réros ‘year’, etc. (14.73), as orig. ‘full —
of years’ or even ‘one year old’ (which would be ‘old’ vs. ‘new’ for wine, grains, fruits, etc.). Walde-P. 1.251. Ernout-M. 1100 (with doubt).
Lat. vetus, vetustus, dim. vetulus (> VLat. veclus > It. vecchio, Fr. vieux, Sp. viejo, Rum. vechiu), Lat. veterdnus ‘veter- an’ (> vetraénus > Rum. bdirin); OLith. velugas, Lett. vecs; ChSl. vetticht in the Gospels ‘ranarés’.
3. Derivs. of IE *§er- perh. orig. ‘be- come old, ripe, frail, etc.’, vb. forms os Skt. jarati ‘makes frail, causes to age,
; r ws old’
; os frail, decays, Bro ,
! ese ‘ripen’, ete. Walde-P. Sl.
mostly of men, ‘old, re- ostly sb. ‘old man’, pl. + of things as shield,
tare c.; NG yépurs yépovras, “YépOS prone
f. ‘ pepat0s (
oman j e); jarant- ‘not tweak ed b: age’, ete. Fee. bs (NG pop. mahsos, mostly of things; of persons only in de- rogatory sense as matavOpwros worth- less fellow, rascal’), fr. adv. wadau ‘of old, Jong ago’ : THAE, Lesb. mfdue ‘far away’, W. pell ‘far distant’, Skt. carama- ‘the last’, ete, Walde-P. 1.517.
(tk. épxatos, lit. ‘belonging to the be- ginning’, hence ‘ancient, old’, fr. apx7 ‘beginning’ (14.25).
5, Fr, ancien (> NE ancient), both mostly with reference to things ‘of for- mer times’, but also in Fr. and formerly in NE ‘old’ of persons, fr. deriv. of Lat. anle ‘before’. REW 494. NED s.v. ancient.
6. NIr. gosta, lit. ‘aged’ (: aois ‘age’, a but now most general word for
NI, crionna, properly ‘wise, ex-
eg but commonly ‘old’ of per-
a, po MI. crinda ‘prudent,
es Meyer, Contrib. 518), orig.?
oh ae with crin ‘withered, shrunk,
iia , Old’, as sb. ‘dry wood fagots’? ¢ latter of. Pedersen 2.498.
TIME
Digitized by Arya Samaj Foundation Chennai and eGangotri
959
Br. koz, Corn. coth, cf. Gall. Cottos, etym.? Henry 78.
7. Goth. fairneis (‘radatés’), ON forn (‘old’ and ‘of old, of former times’), OF fyrn ‘ancient’, OHG firni, MHG virne (‘old’ and of persons ‘experienced, wise’) : Goth. af fairnin jéra ‘of the pre- vious year’, Lith. pernaz ‘in the pre- vious year’, etc., all fr. *per- in Skt. para-, OF feor ‘far, distant’, Grk. repa ‘beyond’, etc. Walde-P. 2.31. Feist 140.
Goth. albeis (‘yépw’ and neut. pl. ‘ra apxeta’), OF eald, ME, NE old, Du. oud, OHG-NHG ald, all lit. ‘nourished, grown’ fr. the root of Goth. alan ‘grow up’, ON ala, Lat. alere ‘nourish’. Walde- P. 1.86.
ON gamail (of persons), Dan. gammel, Sw. gammal, OE gamol mostly of persons (but also of sword in Beowulf), etym. dub., but prob. as orig. ‘of many winters’ : Lat. hiems, Ir. gemred ‘winter’, etc. (14.64). Walde-P. 1.547. Falk-Torp 298f. Hellquist 269.
8. ChSl. starz (in Gospels ‘peoBirns, yépwv’), ete., general Slavic :: Lith. storas ‘thick, bulky’, ON stdrr ‘large, big’, fr. the root *sta- ‘stand’, semantic develop- ment from ‘standing (firm)’ to ‘solid’, whence ‘large’ and ‘old’. Walde-P.
=== search pir in SYN
```


## [2026-09-14T00:57:46.064Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT Pulver\"; grep -n -i \"pulver\\|barud\\|bärüd\\|barüt\" LKT.txt | head -10\necho \"=== PLA barud\"; grep -n -i \"barud\\|bārūd\" incoming/PLA/PLA_pages.txt | head -5\necho \"=== AFM barut\"; grep -n \"بارود\\|باروت\" AFM_pages.txt AFM.txt | head -5\necho \"=== ARB\"; grep -n \"بارود\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -3\necho \"=== TTS files\"; ls incoming/TTS/ 2>/dev/null"
}
```


### [2026-09-14T00:57:46.185Z] TOOL RESULT

```
=== LKT Pulver
2006:Eine  Pflanze  aus  der  Familie  der  Ruta- ceen,  Peganum  harmala  L.  'Harmelraute' [von  den  Arabern  zur  Gewinnung  eines roten  Farbstoffes,  des  sog.  Harmalins 'Türkischrot'  und  eines  Insektenpulvers benutzt];  hieraus  gr.  äp|aa\a,  lat.  har- mala, sp.  alharma,  harma,  alfarma, harmaga,  alharmaga,  amargaza,  ga- marza,  pg.  harmale,  kat.  annalä,  frz. harmale,  it.  armora.  [DE  III.  Eguilaz 162.  DevicDEt  137.  ZfromPh  V,  241. RomForsch  IV,  363.    ML  4051.
2069:'Schatz',  tk.  hazna  ;  hieraus  rum.  hazna 'Schatzkammer,  Abtritt',  venez.  casnd 'Haufen  Geld'  [L'Oriente  I,  196];  russ. kazna  'Krone,  Staat,  Vermögen,  Pulver- kammer', kaznaöei  'Rentmeister,  Kas- sierer' [letztere  Bedeutung  wohl  durch Einfluß  von  kasa  'Kasse'  entstanden], bulg.  hazna  'viel  Geld,  Schatz',  serb.
2095:'Pulver  aus  den  Blättern  der  Lawsonia inermis  oder  der  Wurzel  von  Aleanna tinctoria  Tausch.,  mit  dem  sich  die Frauen  des  Orients  Haare  und  Nägel rot  oder  gelb  färben'  [ausführlich J.  LÖW  in  ZfSem  I,  136/144].  Hieraus mit  ar.  Art.  sp.  alhefia,  it.  alcanna,  al- chenna,  alfena,  mlat.  alchanna,  engl. alkanet,  sp.  alcanna  'Hennapulver',  frz. (dial.)  arcanne  'Rötel',  prov.  alquana 'Röte  des  Gesichtes';  frz.  kenne.  Über tk.  kgna  wurde  rum.  cänä,  cänealä 'Haarfärbemittel',  bulg.  kzna,  serb.  kna 'dass.',  russ.  hna  'Henna'.  [DE  138. DevicDEt  138/139.  Lammens  Rem  135. ML  4135.    Bern  SlEtWb  530.
2880:[Über  aram.  kuhlä  vielleicht  aus  ass. guhlu  ZAkkFW"  61]  'Spießglanzpulver (Schwefelblei)  zum  Färben  der  Augen- brauen, Wimpern  und  Lider'  [über  den Gebrauch  und  die  Zusammensetzung  der orientalischen  Augenschminke  vgl.HlLLE in  ZDMG  V,  236/242];  noch  im  16. Jahrhundert  ist  das  hieraus  entstandene Wort  Alcohol  in  der  Alchemie  der  ge- läufige Ausdruck  für  'trockenes,  feines Pulver',  erst  später  wurde  es  zur  Be- zeichnung des  Weingeistes  benutzt.  Die einzelnen  Formen  sind:  sp.  pg.  alquifol, alcofol,  alcofor,  alcohol,  kat.  alcofoll, frz.  alquifoux,  coheul,  alcohol,  it.  alcool, rum.  alcool;  ndl.  alkohol,  engl,  alcohol, dtsch.  Alkohol;  russ.  alkogoV.  —  [Pers. und  tk.  heißt  die  Augenschminke  übrigens sürme,  subst.  Inf.  des  tk.  Vbs.  siirmek 'glätten'  vom  Slamme  seb,  sit<>,  süp  'glatt,
3264:'Koralle'  [aus  gr.  laapTapiTr^q  ZDMG  LI, 304],  tk.  mergan  'dass.';  hieraus  rura. märgean,  mnrgicä;  bulg.  merdzan  'Ko- ralle'. Mit  ar.  Art.  und  Imäla  [ä  >  e] «rgab  sich  der  alte  pharmazeutische Ausdruck  frz.  almargen:  poudre  d^al- margen  'gepulverte  iioralle',  die  früher in  der  Medizin  benutzt  wurde.  —  Als Fraueiiname  ist  Morgiane  in  der  Ge- schichte von  'ALI  BABÄ  und  den  vierzig Räubern  in  1001  Nacht  zuerst  durch GALLAND  bekannt  geworden.  Er  steckt auch  in  it.  fata  morgana  'Fee  Morgana', dann  'Luftspiegelung  in  der  Wüste', schon  in  Eschenbachs  Parzival  56,  18 mhd.  Fämurgän,  Feimurgan.  —  Man hat  auch  versucht,  auf  das  ar.  Grund- wort margän  das  dtsch.  Meerschaum zurückzuführen,  zuerst  A.  Vambery  in Magyar  Nyelvör  1899,  S.  537 ;  vgl. ZfdWf  I,  361.  II,  345/346.  VII,  79^/796. Da  aber  der  tatsächlich  auf  tk.  Boden bei  Eskisehir  in  Kleinasien  gewonnene Meerschaum  tk.  liile  tisy  oder  dehiz köjmjil  'Pfeifenstein'  oder  'Meeres-, schäum',  niemals  aber  margan  heißt, muß  Meerschaum  [engl,  meerschaum, ndl.  meerschuim,  frz.  Racine  de  mer] deutsch  erklärt  werden,  was  um  so leichler  möglich  ist,  als  auch  die  vier Sorten  in  Eskisehir  an  Ort  und  Stelle mit  dtsch  Namen  „Lager,  Kasten,  Groß- baumwolle, Kleinbaumwoile"  bezeichnet werden;  vgl.  Hugo  Grothe,  Auf  tk.  Erde. Reisebilder  und  Studien.  ^  Berlin  1903. S.  380,  wo  sich  auch  eine  Schilderung der  Gewinnung  des  Meerschaums  findet: S.  277/281.  Ferner  vgl.  Joseph  Grunze), Die  wirtschaftlichen  Verhältnisse  Klein- asiens. Wien  1897.  S.  34/44;  Dernburg, Auf  dtsch.  Bahn  in  Kleinasien.  Berlin 1892.  S.  51  ff.  „Die  Sladt  des  Meer- schaums*. —  Der  Kuriosität  halber  sei noch  die  Etymologie :  dtsch.  Meerschaum <  ar.  morsüm  [soll  heißen  marsüm] 'gesiegelt'  erwähnt,  s.  J.  G.  Kochs, Vergleichungen  mineralogischer  Benen- nungen des  Deutschen  mit  arabischen Wörtern.  Leipzig  1795.  S.40.  [Kluge  304. Devic  DEt  2.Ö/26.    Lammens  Rem  18.
3851:'Rotes  Schwefelarsenik'  [eigentlich  'Höh- lenpulver', aus  ra%"'Pulver',  ^är'Höhle', weil  man  das  Arsenik  aus  Minen  ge- wann]; hieraus  s^.rejalgar,  pg.resalgar, rosalgar,  it.  risigallo,  risogello,  (alt)  Pisa risalgado;  dtsch.  Realgar  'Rauschgelb', engl,  realgar  'red  orpiment'  [<;^  frz.  or- piment  <^  lat.  auri  piymentmn].  [DE 332/333.    Eguilaz  482.    ML  7011.
4395:Eine  Staude  Bhus  coriaria  L.  'Essig- baum' [vom  Vb.  samaka  'einen  schönen Wuchs  haben'  oder  aus  dem  Aram.]; hieraus  it.  sommaco,  prov.  frz.  sumac, sp.  zumaque,  pg.  summagre,  rum.  sumac; russ.  sumah;  engl,  sumac,  sumach.  shu- mach,  ndl.  smalc,  dtsch.  Schmaclc,  Su- mach.  —  Die  zu  Pulver  zerriebenen
4750:oxyd'  Tills  Putzpulver  benutzt].  --  Aus pers.  tütijäuäk  'luti;i  ähnlich'  [s.  De  Sacy ChiAr  III,  44:2;  ebenda  4529/442  über tütijä'']  entstanden  die  Formen  engl. tuteudt)  'iml.  Zink;  Legierung  aus  Kupfer, Nickel  und  Zink  für  Tisch  bestecke';  Irz. toutenafjue,  tintenague,  pg.  tutenaga  Mie- seibe Legierung'.  [DE  '■217.  Devic  DEt 222/t2i23.  Eguilaz  509.  309/:!l().  Lam- mens  Rem  ti2!2.    Mikl  SlEtVVh  3G4b.
=== PLA barud
=== AFM barut
=== ARB
=== TTS files
TTS_pages.txt
TTS_vambery1878_uoft_djvu.txt
TTS_vambery1878_uoft.pdf
```


## [2026-09-14T00:57:48.073Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%B0%E0%A5%81%E0%A4%B7",
 "prompt": "Give the Sanskrit entry परुष (paruṣa): meanings (spotted, variegated, rough?) and etymology / Proto-Indo-Iranian root."
}
```


### [2026-09-14T00:57:55.804Z] TOOL RESULT

```
# Sanskrit परुष (paruṣa)

## Meanings

The entry identifies several primary senses:

1. **Spotted/variegated appearance**: "spotted, variegated, dirty-colored" with an example from the Ṛgveda (c. 1500-1000 BCE) describing oxen "of speckled hue"

2. **Physical texture**: "knotty, rough, hard, stiff, rugged, uneven, shaggy" (attested in the Atharvaveda)

3. **Interpersonal qualities**: "piercing, keen, sharp, violent, harsh, severe, unkind"

## Etymology

The word derives from **Proto-Indo-Iranian *parHušás**, which itself comes from Proto-Indo-European *pelHu-só-s. This traces back to the PIE root *pelH- meaning "gray, pale," cognate with the Sanskrit term पलित (palitá, "gray, hoary").

Related cognates include Avestan pouruša ("gray of hair"), Persian pir ("old"), Latin pallidus, and Ancient Greek pelitnós, demonstrating the word's broad Indo-European heritage.
```


## [2026-09-14T00:58:03.350Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TTS barut\"; grep -n -i \"barut\\|bárut\\|Pulver\" incoming/TTS/TTS_pages.txt | head -8\necho \"=== ARY latin index PIR/PARSA\"; grep -n -i \"^PIR\\|\\bPIR\\b\\|PARSA\" incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== ARY pudr\"; grep -n \"پودر\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-14T00:58:03.458Z] TOOL RESULT

```
=== TTS barut
3874:kir.   wm = Mehl, Staub, Tulver; wm/rtZ; = zerrieben wie Pulver
=== ARY latin index PIR/PARSA
4264:TIF yO ebb ily PARSNA, PARSANA (HITTITE) =a
4628:PIRSIN ABURDISH) 52,8 PERESA, FRASA, PERESAITI
4630:PUSHT AAFGHAND (4) gli APARSAM
4950:FARJAN PEL, PURD, PIRD, PIR
5204:PIRSHYS (LITHUANIAN) gly PARQSU-, PaRQSU- :(AVESTAN) gly!
=== ARY pudr
```


## [2026-09-14T00:58:04.693Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%AF%D8%B1",
 "prompt": "Give the Persian etymology of پودر (pudr): from which language is it borrowed, and what is the Persian meaning?"
}
```


### [2026-09-14T00:58:07.838Z] TOOL RESULT

```
# Persian Etymology of پودر (pudr)

**Source Language:** The word is "Borrowed from French _poudre_."

**Persian Meaning:** According to the Wiktionary entry, پودر means "powder." The document provides an example usage: washing powder (_پودْرِ لِباس‌شویی_), with an alternative Persian synonym being گرد (gard).
```


## [2026-09-14T00:58:20.758Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npdftoppm -f 390 -l 390 -r 150 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg390b\nconvert pg390b.png -resize 1400x -quality 92 pg390b.jpg; ls -la pg390b.jpg"
}
```


### [2026-09-14T00:58:22.333Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 120893 Sep 13 20:58 pg390b.jpg
```


## [2026-09-14T00:58:24.390Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg390b.jpg"
}
```


### [2026-09-14T00:58:24.409Z] TOOL RESULT

```

```


## [2026-09-14T00:58:56.063Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=powder",
 "prompt": "Give the etymology line for the noun \"powder\" as printed in the American Heritage Dictionary (Middle English, Old French, Latin forms and the Indo-European root cross-reference)."
}
```


### [2026-09-14T00:59:00.153Z] TOOL RESULT

```
# Etymology of "Powder"

According to the American Heritage Dictionary entry, the etymology line reads:

"[Middle English _poudre_, from Old French, from Latin _pulvis__, pulver-_.]"

The entry also notes that the dictionary includes an online appendix for Indo-European roots, with a link to "[Indo-European Roots](/word/indoeurop.html)" for additional etymological information, though the specific Indo-European root form is not provided in this particular entry's etymology section.
```


## [2026-09-14T00:59:13.525Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B1%D8%B3%D8%A7' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B1%D9%88%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B1%D9%88%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%AF%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%B0%E0%A5%81%E0%A4%B7' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 390, roots Pel 2/Porkwos and Pel 3: Persian pir, parsa, pudr, barut/barud; Sanskrit parusa' 2>&1 | tail -2\ndone"
}
```


## [2026-09-14T00:59:15.389Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://www.etymonline.com/word/falcon' \\\n 'https://www.etymonline.com/word/powder' \\\n 'https://www.etymonline.com/word/pollen' \\\n 'https://www.etymonline.com/word/pale' \\\n 'https://ahdictionary.com/word/search.html?q=powder' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 390, roots Pel 2/Porkwos and Pel 3: falcon, powder, pollen, pale' 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T00:59:17.064Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1062cf632afd7bb8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/597dd3bc9e52d2b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/94d771761a5305e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/830da7a41c1db247.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/91785479154fb834.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c2febf9435e5c9a7.txt
```


### [2026-09-14T00:59:19.808Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bbb911e52944dd03.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/848d9c009040e7bb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd64e22aeaa0d145.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a2e704f36534f63e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/62ea275ee36c3c19.txt
```


## [2026-09-14T00:59:45.283Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BQT\nSC=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ncp $SC/bqt390_n436.jpg data/verification/sources/refs/ocr/BQT/216.png\ncp $SC/bqt390_n662.jpg data/verification/sources/refs/ocr/BQT/436.png\ncat > data/verification/sources/refs/ocr/BQT/216.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed page ٢١٦ = 216 (archive.org borhan-ghate-v1 leaf n436).\nRead from the page image by claude-opus-5 on 2026-09-13 for the verification of PDF page 390.]\n\nHeadword (main column):\nبارود بادال - بر وزن و بمعنی باروت باشد که داروی تفنگ است؛ و بلغت سریانی شوره را\nگویند که جزو اعظم باروت باشد و آنرا نمک چینی هم گویند.\n\nCross-reference entry at the foot of the page:\nباروت - رک: بارود.\n\nMo'in's footnote 4 on this page (the etymological note Nourai cites as BQT:216), verbatim:\n«۴ - بارود در عربی نیز مستعمل است مأخوذ از کلمهٔ ترکی باروت و آن از poudre فرانسه\n(بمعنی غبار و مادهٔ مشتعلهٔ مخصوص) مأخوذ است «نفیسی».»\n\n(i.e. \"bārūd is used in Arabic too, taken from the Turkish word bārūt, and that in turn is\ntaken from French poudre (meaning dust, and a particular combustible substance) — [so]\nNafisi.\")\n\nFootnote 5 on the same page: «۵ - Céruse. رک ۱ ص ۲۰۱».\nEOF\ncat > data/verification/sources/refs/ocr/BQT/436.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed page ٤٣٦ = 436 (archive.org borhan-ghate-v1 leaf n662).\nRead from the page image by claude-opus-5 on 2026-09-13 for the verification of PDF page 390.]\n\nHeadword: پیر - بر وزن و بمعنی پدر ... (with the Shahnameh/other verses printed under it)\n\nMo'in's footnote 5 on this page (the etymological note Nourai cites as BQT:436), verbatim:\n«۵ - در فارسی نیز بمعنی سالخورده، مقابل جوان؛ پهلوی pîr «اونوالا ۵۸۱» «اسنق ۳۵۰»،\nکردی و افغانی pîr، قس: اوستا parô * parya (پیشین) «اسنق ایضاً»، گیلکی pir.\nفریزندی و برنی و نطنزی pir «ک. ۱ ص ۲۹۳»، سنگسری و سرخه‌ای و لاسگردی و شهمیرزادی\nنیز pir «ک. ۲ ص ۱۹۴».»\n\n(i.e. Pahlavi pîr; Kurdish and Afghan pîr; compare Avestan parô, *parya \"former, prior\";\nGilaki pir; Farizandi, Yarani/Barani and Natanzi pir; Sangsari, Sorkhe'i, Lasgerdi and\nShahmirzadi also pir.)\n\nFootnote 4 on the same page: «۴ - گیلکی peer.»\nAdjacent footnote (headword پیدا): «پیدا - پهلوی Paitâk «نیبرگ ۱۶۸» ، padhtâk «اونوالا ۵۸۴»\nو patyâk، ایرانی باستان patyâka، سانسکریت pratyánc ، pratyâka، کردی peidâ، افغانی\npaidâ «اسنق ۳۴۹» «نیبرگ ۱۶۸-۱۶۹»؛ آشکار، ظاهر.»\nEOF\nls -la data/verification/sources/refs/ocr/BQT/"
}
```


### [2026-09-14T00:59:46.451Z] TOOL RESULT

```
total 61240
drwxrwxr-x  2 sfmqrb sfmqrb   12288 Sep 13 20:59 .
drwxrwxr-x 13 sfmqrb sfmqrb    4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb  368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb    1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb  534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb    2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1076 Sep  4 15:27 103.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1325 Sep  7 16:52 1074.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  330101 Sep  6 17:59 1092.jpg
-rw-rw-r--  1 sfmqrb sfmqrb    2600 Sep  6 17:59 1092.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  541712 Sep  6 17:54 1187.png
-rw-rw-r--  1 sfmqrb sfmqrb    1579 Sep  6 17:54 1187.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  393921 Sep  6 11:40 1219.png
-rw-rw-r--  1 sfmqrb sfmqrb    3603 Sep  6 11:40 1219.txt
-rw-rw-r--  1 sfmqrb sfmqrb     818 Sep  6 11:40 1219.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  435393 Sep  6 10:57 1223.png
-rw-rw-r--  1 sfmqrb sfmqrb    4468 Sep  6 10:57 1223.txt
-rw-rw-r--  1 sfmqrb sfmqrb  446843 Sep  4 13:39 1225.png
-rw-rw-r--  1 sfmqrb sfmqrb    4412 Sep  4 13:39 1225.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1254 Sep  4 14:18 1225.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  384634 Sep  6 10:57 1226.png
-rw-rw-r--  1 sfmqrb sfmqrb    3662 Sep  6 10:57 1226.txt
-rw-rw-r--  1 sfmqrb sfmqrb  467471 Sep  6 17:23 1237.png
-rw-rw-r--  1 sfmqrb sfmqrb    4642 Sep  6 17:23 1237.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1013 Sep  6 17:24 1237.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  150675 Sep  6 12:03 1261.png
-rw-rw-r--  1 sfmqrb sfmqrb    3458 Sep  6 12:04 1261.txt
-rw-rw-r--  1 sfmqrb sfmqrb  367477 Sep  6 18:15 1266.png
-rw-rw-r--  1 sfmqrb sfmqrb    3484 Sep  6 18:16 1266.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1652 Sep  6 18:18 1266.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  391494 Sep  6 18:17 1267.png
-rw-rw-r--  1 sfmqrb sfmqrb    3614 Sep  6 18:17 1267.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1292 Sep  6 18:18 1267.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  391186 Sep  6 16:54 1272.png
-rw-rw-r--  1 sfmqrb sfmqrb    3762 Sep  6 16:54 1272.txt
-rw-rw-r--  1 sfmqrb sfmqrb  408541 Sep  4 15:42 1275.png
-rw-rw-r--  1 sfmqrb sfmqrb    3183 Sep  4 15:42 1275.txt
-rw-rw-r--  1 sfmqrb sfmqrb  157869 Sep  6 17:13 1279.png
-rw-rw-r--  1 sfmqrb sfmqrb    3347 Sep  6 17:13 1279.txt
-rw-rw-r--  1 sfmqrb sfmqrb  169575 Sep  6 11:42 1280.png
-rw-rw-r--  1 sfmqrb sfmqrb    3896 Sep  6 11:42 1280.txt
-rw-rw-r--  1 sfmqrb sfmqrb     741 Sep  6 11:43 1280.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  163035 Sep  5 22:19 1294.png
-rw-rw-r--  1 sfmqrb sfmqrb    3361 Sep  5 22:19 1294.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1085 Sep  5 22:32 1294.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  176513 Sep  6 16:57 1296.png
-rw-rw-r--  1 sfmqrb sfmqrb    4459 Sep  6 16:57 1296.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2048 Sep  6 17:03 1296.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  421610 Sep  6 16:58 1297.png
-rw-rw-r--  1 sfmqrb sfmqrb    3920 Sep  6 16:58 1297.txt
-rw-rw-r--  1 sfmqrb sfmqrb  163035 Sep  6 16:58 1298.png
-rw-rw-r--  1 sfmqrb sfmqrb    3361 Sep  6 16:58 1298.txt
-rw-rw-r--  1 sfmqrb sfmqrb   91088 Sep  5 22:32 1299.png
-rw-rw-r--  1 sfmqrb sfmqrb     573 Sep  5 22:32 1299.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  171926 Sep  5 22:20 1300.png
-rw-rw-r--  1 sfmqrb sfmqrb    4011 Sep  5 22:21 1300.txt
-rw-rw-r--  1 sfmqrb sfmqrb     238 Sep  5 22:32 1300.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  410950 Sep  5 22:20 1302.png
-rw-rw-r--  1 sfmqrb sfmqrb    3921 Sep  5 22:20 1302.txt
-rw-rw-r--  1 sfmqrb sfmqrb     284 Sep  5 22:32 1302.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  184884 Sep  6 17:35 1318.png
-rw-rw-r--  1 sfmqrb sfmqrb    4677 Sep  6 17:35 1318.txt
-rw-rw-r--  1 sfmqrb sfmqrb  100817 Sep  6 17:39 1320.png
-rw-rw-r--  1 sfmqrb sfmqrb     615 Sep  6 17:36 1320.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1262 Sep  6 17:39 1320.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  122289 Sep  4 16:05 1339.png
-rw-rw-r--  1 sfmqrb sfmqrb    2421 Sep  4 16:05 1339.txt
-rw-rw-r--  1 sfmqrb sfmqrb  325629 Sep  4 14:06 1357.png
-rw-rw-r--  1 sfmqrb sfmqrb    2656 Sep  4 14:06 1357.txt
-rw-rw-r--  1 sfmqrb sfmqrb  341763 Sep  4 15:53 1382.png
-rw-rw-r--  1 sfmqrb sfmqrb    2851 Sep  4 15:53 1382.txt
-rw-rw-r--  1 sfmqrb sfmqrb  447895 Sep  4 14:33 1385.png
-rw-rw-r--  1 sfmqrb sfmqrb    3725 Sep  4 14:33 1385.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2008 Sep  4 14:34 1385.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  370032 Sep  6 11:46 1439.png
-rw-rw-r--  1 sfmqrb sfmqrb    3587 Sep  6 11:46 1439.txt
-rw-rw-r--  1 sfmqrb sfmqrb  405983 Sep 13 20:54 1444.png
-rw-rw-r--  1 sfmqrb sfmqrb    3782 Sep 13 20:54 1444.txt
-rw-rw-r--  1 sfmqrb sfmqrb  392691 Sep  4 19:05 1445.png
-rw-rw-r--  1 sfmqrb sfmqrb    3677 Sep  4 19:05 1445.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1790 Sep  4 19:14 1445.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  168297 Sep  4 21:39 1452.png
-rw-rw-r--  1 sfmqrb sfmqrb    3942 Sep  4 21:39 1452.txt
-rw-rw-r--  1 sfmqrb sfmqrb  356058 Sep  6 11:07 1453.png
-rw-rw-r--  1 sfmqrb sfmqrb    3545 Sep  6 11:07 1453.txt
-rw-rw-r--  1 sfmqrb sfmqrb  443522 Sep  4 14:46 1455.png
-rw-rw-r--  1 sfmqrb sfmqrb    4392 Sep  4 14:46 1455.txt
-rw-rw-r--  1 sfmqrb sfmqrb  384649 Sep  5 16:34 1462.png
-rw-rw-r--  1 sfmqrb sfmqrb    3664 Sep  5 16:34 1462.txt
-rw-rw-r--  1 sfmqrb sfmqrb  439837 Sep  5 17:04 1465.png
-rw-rw-r--  1 sfmqrb sfmqrb    4158 Sep  5 17:04 1465.txt
-rw-rw-r--  1 sfmqrb sfmqrb  465000 Sep  5 16:34 1471.png
-rw-rw-r--  1 sfmqrb sfmqrb    4410 Sep  5 16:34 1471.txt
-rw-rw-r--  1 sfmqrb sfmqrb  170243 Sep  5 16:35 1472.png
-rw-rw-r--  1 sfmqrb sfmqrb    4248 Sep  5 16:35 1472.txt
-rw-rw-r--  1 sfmqrb sfmqrb  154569 Sep  4 15:14 1488.png
-rw-rw-r--  1 sfmqrb sfmqrb    3724 Sep  4 15:14 1488.txt
-rw-rw-r--  1 sfmqrb sfmqrb  334007 Sep  5 16:35 1492.png
-rw-rw-r--  1 sfmqrb sfmqrb    3081 Sep  5 16:36 1492.txt
-rw-rw-r--  1 sfmqrb sfmqrb  179424 Sep 13 20:56 1499.png
-rw-rw-r--  1 sfmqrb sfmqrb    4298 Sep 13 20:57 1499.txt
-rw-rw-r--  1 sfmqrb sfmqrb     958 Sep 13 20:57 1499.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  165600 Sep 13 20:56 1502.png
-rw-rw-r--  1 sfmqrb sfmqrb    3976 Sep 13 20:56 1502.txt
-rw-rw-r--  1 sfmqrb sfmqrb     965 Sep 13 20:57 1502.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  167633 Sep  6 10:58 1544.png
-rw-rw-r--  1 sfmqrb sfmqrb    3973 Sep  6 10:58 1544.txt
-rw-rw-r--  1 sfmqrb sfmqrb  162631 Sep  6 12:37 1550.png
-rw-rw-r--  1 sfmqrb sfmqrb    4047 Sep  6 12:37 1550.txt
-rw-rw-r--  1 sfmqrb sfmqrb  398954 Sep  6 17:22 1563.png
-rw-rw-r--  1 sfmqrb sfmqrb    3996 Sep  6 17:22 1563.txt
-rw-rw-r--  1 sfmqrb sfmqrb  387725 Sep  6 11:43 1564.png
-rw-rw-r--  1 sfmqrb sfmqrb    3765 Sep  6 11:43 1564.txt
-rw-rw-r--  1 sfmqrb sfmqrb     797 Sep  6 11:43 1564.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  426166 Sep  6 18:13 1567.png
-rw-rw-r--  1 sfmqrb sfmqrb    4184 Sep  6 18:13 1567.txt
-rw-rw-r--  1 sfmqrb sfmqrb  446417 Sep  6 11:50 1571.png
-rw-rw-r--  1 sfmqrb sfmqrb    3968 Sep  6 11:50 1571.txt
-rw-rw-r--  1 sfmqrb sfmqrb  409830 Sep  6 11:41 1572.png
-rw-rw-r--  1 sfmqrb sfmqrb    4035 Sep  6 11:41 1572.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1691 Sep  6 11:41 1572.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  399694 Sep  6 11:31 1578.png
-rw-rw-r--  1 sfmqrb sfmqrb    3943 Sep  6 11:31 1578.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2183 Sep  6 11:32 1578.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  175836 Sep  6 17:48 1583.png
-rw-rw-r--  1 sfmqrb sfmqrb    4315 Sep  6 17:48 1583.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2566 Sep  6 17:53 1583.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  462972 Sep  6 11:56 1589.png
-rw-rw-r--  1 sfmqrb sfmqrb    4365 Sep  6 11:56 1589.txt
-rw-rw-r--  1 sfmqrb sfmqrb  178338 Sep  6 12:37 1594.png
-rw-rw-r--  1 sfmqrb sfmqrb    4016 Sep  6 12:37 1594.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1100 Sep  6 16:54 1594.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  159233 Sep  6 12:29 1604.png
-rw-rw-r--  1 sfmqrb sfmqrb    3769 Sep  6 12:29 1604.txt
-rw-rw-r--  1 sfmqrb sfmqrb    3246 Sep  6 16:38 1604.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  387981 Sep  6 12:17 1619.png
-rw-rw-r--  1 sfmqrb sfmqrb    3736 Sep  6 12:17 1619.txt
-rw-rw-r--  1 sfmqrb sfmqrb  476500 Sep  6 17:56 1622.png
-rw-rw-r--  1 sfmqrb sfmqrb    4650 Sep  6 17:56 1622.txt
-rw-rw-r--  1 sfmqrb sfmqrb  420606 Sep  5 16:13 1624.png
-rw-rw-r--  1 sfmqrb sfmqrb    3785 Sep  5 16:13 1624.txt
-rw-rw-r--  1 sfmqrb sfmqrb  380653 Sep  6 12:18 1631.png
-rw-rw-r--  1 sfmqrb sfmqrb    3687 Sep  6 12:18 1631.txt
-rw-rw-r--  1 sfmqrb sfmqrb  371457 Sep  6 11:56 1637.png
-rw-rw-r--  1 sfmqrb sfmqrb    3501 Sep  6 11:56 1637.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1332 Sep  6 11:56 1637.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  161530 Sep  6 11:57 1648.png
-rw-rw-r--  1 sfmqrb sfmqrb    3648 Sep  6 11:57 1648.txt
-rw-rw-r--  1 sfmqrb sfmqrb     580 Sep  6 12:02 1648.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  170707 Sep  6 12:16 1671.png
-rw-rw-r--  1 sfmqrb sfmqrb    3766 Sep  6 12:16 1671.txt
-rw-rw-r--  1 sfmqrb sfmqrb  369192 Sep  6 12:16 1673.png
-rw-rw-r--  1 sfmqrb sfmqrb    3541 Sep  6 12:16 1673.txt
-rw-rw-r--  1 sfmqrb sfmqrb  171693 Sep  6 12:07 1688.png
-rw-rw-r--  1 sfmqrb sfmqrb    3776 Sep  6 12:07 1688.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1084 Sep  6 12:12 1688.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  153064 Sep  6 11:44 1689.png
-rw-rw-r--  1 sfmqrb sfmqrb    3467 Sep  6 11:44 1689.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2123 Sep  6 11:45 1689.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  166637 Sep  6 11:44 1694.png
-rw-rw-r--  1 sfmqrb sfmqrb    3914 Sep  6 11:44 1694.txt
-rw-rw-r--  1 sfmqrb sfmqrb  404649 Sep  6 11:04 1707.png
-rw-rw-r--  1 sfmqrb sfmqrb    3506 Sep  6 11:04 1707.txt
-rw-rw-r--  1 sfmqrb sfmqrb  163959 Sep  6 12:07 1709.png
-rw-rw-r--  1 sfmqrb sfmqrb    3832 Sep  6 12:08 1709.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1192 Sep  6 12:12 1709.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  182880 Sep  6 18:01 1721.png
-rw-rw-r--  1 sfmqrb sfmqrb    4359 Sep  6 18:01 1721.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1484 Sep  5 16:15 172.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  436538 Sep  6 11:57 1731.png
-rw-rw-r--  1 sfmqrb sfmqrb    4201 Sep  6 11:57 1731.txt
-rw-rw-r--  1 sfmqrb sfmqrb  159132 Sep  6 16:43 1738.png
-rw-rw-r--  1 sfmqrb sfmqrb    3667 Sep  6 16:43 1738.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2166 Sep  6 16:48 1738.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  431312 Sep  6 16:37 1749.png
-rw-rw-r--  1 sfmqrb sfmqrb    4248 Sep  6 16:37 1749.txt
-rw-rw-r--  1 sfmqrb sfmqrb  427199 Sep  6 10:53 1754.png
-rw-rw-r--  1 sfmqrb sfmqrb    4156 Sep  6 10:53 1754.txt
-rw-rw-r--  1 sfmqrb sfmqrb  454456 Sep  5 22:20 1759.png
-rw-rw-r--  1 sfmqrb sfmqrb    4255 Sep  5 22:20 1759.txt
-rw-rw-r--  1 sfmqrb sfmqrb  159644 Sep  6 11:30 1774.png
-rw-rw-r--  1 sfmqrb sfmqrb    3985 Sep  6 11:30 1774.txt
-rw-rw-r--  1 sfmqrb sfmqrb    3319 Sep  6 11:37 1774.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  356628 Sep  5 16:42 1776.png
-rw-rw-r--  1 sfmqrb sfmqrb    3111 Sep  5 16:42 1776.txt
-rw-rw-r--  1 sfmqrb sfmqrb  155054 Sep  6 18:18 1778.png
-rw-rw-r--  1 sfmqrb sfmqrb    3665 Sep  6 18:18 1778.txt
-rw-rw-r--  1 sfmqrb sfmqrb  402415 Sep  6 10:55 1781.png
-rw-rw-r--  1 sfmqrb sfmqrb    3852 Sep  6 10:55 1781.txt
-rw-rw-r--  1 sfmqrb sfmqrb  451977 Sep  5 22:19 1783.png
-rw-rw-r--  1 sfmqrb sfmqrb    4467 Sep  5 22:19 1783.txt
-rw-rw-r--  1 sfmqrb sfmqrb  398622 Sep  5 22:19 1786.png
-rw-rw-r--  1 sfmqrb sfmqrb    3921 Sep  5 22:19 1786.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1117 Sep  5 22:20 1786.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  430713 Sep  6 12:21 1795.png
-rw-rw-r--  1 sfmqrb sfmqrb    3979 Sep  6 12:22 1795.txt
-rw-rw-r--  1 sfmqrb sfmqrb  417435 Sep  6 11:09 1800.png
-rw-rw-r--  1 sfmqrb sfmqrb    4047 Sep  6 11:09 1800.txt
-rw-rw-r--  1 sfmqrb sfmqrb  177775 Sep  6 10:56 1802.png
-rw-rw-r--  1 sfmqrb sfmqrb    4218 Sep  6 10:56 1802.txt
-rw-rw-r--  1 sfmqrb sfmqrb  671488 Sep  5 16:59 1803.png
-rw-rw-r--  1 sfmqrb sfmqrb    4559 Sep  6 10:56 1803.txt
-rw-rw-r--  1 sfmqrb sfmqrb    3889 Sep  6 11:01 1803.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  377836 Sep  6 10:55 1806.png
-rw-rw-r--  1 sfmqrb sfmqrb    3579 Sep  6 10:55 1806.txt
-rw-rw-r--  1 sfmqrb sfmqrb  419173 Sep  6 10:56 1807.png
-rw-rw-r--  1 sfmqrb sfmqrb    4077 Sep  6 10:56 1807.txt
-rw-rw-r--  1 sfmqrb sfmqrb  289735 Sep  6 18:18 1809.png
-rw-rw-r--  1 sfmqrb sfmqrb    2830 Sep  6 18:18 1809.txt
-rw-rw-r--  1 sfmqrb sfmqrb  482084 Sep  5 01:38 180.png
-rw-rw-r--  1 sfmqrb sfmqrb    1288 Sep  5 01:39 180.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  393337 Sep  6 18:18 1814.png
-rw-rw-r--  1 sfmqrb sfmqrb    3694 Sep  6 18:18 1814.txt
-rw-rw-r--  1 sfmqrb sfmqrb  136243 Sep  6 18:19 1816.png
-rw-rw-r--  1 sfmqrb sfmqrb    2905 Sep  6 18:19 1816.txt
-rw-rw-r--  1 sfmqrb sfmqrb  168820 Sep  5 16:29 1819.png
-rw-rw-r--  1 sfmqrb sfmqrb    4031 Sep  5 16:29 1819.txt
-rw-rw-r--  1 sfmqrb sfmqrb  510341 Sep  5 01:38 181.png
-rw-rw-r--  1 sfmqrb sfmqrb    1196 Sep  5 01:39 181.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  184808 Sep  6 10:56 1832.png
-rw-rw-r--  1 sfmqrb sfmqrb    4143 Sep  6 10:56 1832.txt
-rw-rw-r--  1 sfmqrb sfmqrb  156526 Sep  7 12:10 1835.png
-rw-rw-r--  1 sfmqrb sfmqrb    3813 Sep  7 12:10 1835.txt
-rw-rw-r--  1 sfmqrb sfmqrb  455748 Sep  7 14:22 1836.png
-rw-rw-r--  1 sfmqrb sfmqrb    3674 Sep  7 14:22 1836.txt
-rw-rw-r--  1 sfmqrb sfmqrb  421444 Sep  6 11:18 1838.png
-rw-rw-r--  1 sfmqrb sfmqrb    4063 Sep  6 11:18 1838.txt
-rw-rw-r--  1 sfmqrb sfmqrb  423523 Sep  6 11:17 1841.png
-rw-rw-r--  1 sfmqrb sfmqrb    3783 Sep  6 11:18 1841.txt
-rw-rw-r--  1 sfmqrb sfmqrb  166992 Sep  5 16:32 1848.png
-rw-rw-r--  1 sfmqrb sfmqrb    3879 Sep  5 16:32 1848.txt
-rw-rw-r--  1 sfmqrb sfmqrb  439207 Sep  6 18:14 1849.png
-rw-rw-r--  1 sfmqrb sfmqrb    4173 Sep  6 18:14 1849.txt
-rw-rw-r--  1 sfmqrb sfmqrb   92182 Sep  6 11:00 1854.png
-rw-rw-r--  1 sfmqrb sfmqrb    4245 Sep  6 10:55 1854.txt
-rw-rw-r--  1 sfmqrb sfmqrb     979 Sep  6 11:00 1854.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  182549 Sep  7 16:22 1858.png
-rw-rw-r--  1 sfmqrb sfmqrb    4320 Sep  7 16:22 1858.txt
-rw-rw-r--  1 sfmqrb sfmqrb  478549 Sep  5 16:40 1861.png
-rw-rw-r--  1 sfmqrb sfmqrb    4045 Sep  5 16:40 1861.txt
-rw-rw-r--  1 sfmqrb sfmqrb  174536 Sep  5 22:18 1862.png
-rw-rw-r--  1 sfmqrb sfmqrb    4183 Sep  5 22:19 1862.txt
-rw-rw-r--  1 sfmqrb sfmqrb  431778 Sep  5 22:26 1864.png
-rw-rw-r--  1 sfmqrb sfmqrb    4099 Sep  5 22:26 1864.txt
-rw-rw-r--  1 sfmqrb sfmqrb  158181 Sep  5 22:26 1865.png
-rw-rw-r--  1 sfmqrb sfmqrb    3521 Sep  5 22:26 1865.txt
-rw-rw-r--  1 sfmqrb sfmqrb  454639 Sep  5 16:55 1870.png
-rw-rw-r--  1 sfmqrb sfmqrb    4381 Sep  5 16:56 1870.txt
-rw-rw-r--  1 sfmqrb sfmqrb  454639 Sep  7 12:24 1872.png
-rw-rw-r--  1 sfmqrb sfmqrb    4381 Sep  7 12:24 1872.txt
-rw-rw-r--  1 sfmqrb sfmqrb  385446 Sep  6 18:39 1874.png
-rw-rw-r--  1 sfmqrb sfmqrb    3726 Sep  6 18:54 1874.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1449 Sep  6 18:46 1874.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb   91864 Sep  6 18:39 1876.png
-rw-rw-r--  1 sfmqrb sfmqrb    4101 Sep  6 18:55 1876.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2421 Sep  6 18:46 1876.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  442264 Sep  4 15:37 1878.png
-rw-rw-r--  1 sfmqrb sfmqrb    4418 Sep  4 15:37 1878.txt
-rw-rw-r--  1 sfmqrb sfmqrb  418415 Sep  6 18:51 1879.png
-rw-rw-r--  1 sfmqrb sfmqrb    3781 Sep  6 18:51 1879.txt
-rw-rw-r--  1 sfmqrb sfmqrb  417664 Sep  6 18:51 1880.png
-rw-rw-r--  1 sfmqrb sfmqrb    4166 Sep  6 18:51 1880.txt
-rw-rw-r--  1 sfmqrb sfmqrb  247438 Sep  6 21:40 1894.png
-rw-rw-r--  1 sfmqrb sfmqrb    2004 Sep  6 21:40 1894.txt
-rw-rw-r--  1 sfmqrb sfmqrb  368487 Sep  4 15:37 1900.png
-rw-rw-r--  1 sfmqrb sfmqrb    3698 Sep  4 15:37 1900.txt
-rw-rw-r--  1 sfmqrb sfmqrb  168384 Sep  6 18:51 1902.png
-rw-rw-r--  1 sfmqrb sfmqrb    3899 Sep  6 18:51 1902.txt
-rw-rw-r--  1 sfmqrb sfmqrb  143065 Sep  6 21:42 1904.png
-rw-rw-r--  1 sfmqrb sfmqrb    3144 Sep  6 21:42 1904.txt
-rw-rw-r--  1 sfmqrb sfmqrb  343118 Sep  4 16:03 1908.png
-rw-rw-r--  1 sfmqrb sfmqrb    3313 Sep  4 16:03 1908.txt
-rw-rw-r--  1 sfmqrb sfmqrb  385933 Sep  7 15:35 1922.png
-rw-rw-r--  1 sfmqrb sfmqrb    3769 Sep  7 15:35 1922.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2338 Sep  7 15:38 1922.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  118409 Sep  7 14:22 1931.png
-rw-rw-r--  1 sfmqrb sfmqrb    2385 Sep  7 14:22 1931.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2023 Sep  7 14:23 1931.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  165567 Sep  7 12:10 1934.png
-rw-rw-r--  1 sfmqrb sfmqrb    4191 Sep  7 12:10 1934.txt
-rw-rw-r--  1 sfmqrb sfmqrb  378727 Sep  7 12:11 1947.png
-rw-rw-r--  1 sfmqrb sfmqrb    3742 Sep  7 12:11 1947.txt
-rw-rw-r--  1 sfmqrb sfmqrb  422554 Sep  7 12:12 1948.png
-rw-rw-r--  1 sfmqrb sfmqrb    3894 Sep  7 12:12 1948.txt
-rw-rw-r--  1 sfmqrb sfmqrb  449810 Sep  7 12:15 1949.png
-rw-rw-r--  1 sfmqrb sfmqrb    4309 Sep  7 12:15 1949.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2069 Sep  7 12:21 1949.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  382045 Sep  7 12:21 1986.png
-rw-rw-r--  1 sfmqrb sfmqrb    3344 Sep  7 12:22 1986.txt
-rw-rw-r--  1 sfmqrb sfmqrb  422891 Sep  7 11:53 2001.png
-rw-rw-r--  1 sfmqrb sfmqrb    4149 Sep  7 11:53 2001.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1308 Sep  7 11:54 2001.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  398541 Sep  7 11:52 2002.png
-rw-rw-r--  1 sfmqrb sfmqrb    3768 Sep  7 11:52 2002.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1505 Sep  7 12:04 2002.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  149233 Sep  7 12:10 2006.png
-rw-rw-r--  1 sfmqrb sfmqrb    3575 Sep  7 12:11 2006.txt
-rw-rw-r--  1 sfmqrb sfmqrb  381443 Sep  7 13:38 2010.png
-rw-rw-r--  1 sfmqrb sfmqrb    3609 Sep  7 13:38 2010.txt
-rw-rw-r--  1 sfmqrb sfmqrb  470974 Sep  7 13:38 2014.png
-rw-rw-r--  1 sfmqrb sfmqrb    4282 Sep  7 13:38 2014.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1912 Sep  7 13:46 2014.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  414605 Sep  7 13:38 2015.png
-rw-rw-r--  1 sfmqrb sfmqrb    3852 Sep  7 13:38 2015.txt
-rw-rw-r--  1 sfmqrb sfmqrb   66580 Sep  6 11:00 2023.png
-rw-rw-r--  1 sfmqrb sfmqrb    3650 Sep  6 10:56 2023.txt
-rw-rw-r--  1 sfmqrb sfmqrb     668 Sep  6 11:00 2023.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  391384 Sep  7 11:52 2029.png
-rw-rw-r--  1 sfmqrb sfmqrb    3170 Sep  7 11:52 2029.txt
-rw-rw-r--  1 sfmqrb sfmqrb  386994 Sep  7 11:52 2035.png
-rw-rw-r--  1 sfmqrb sfmqrb    3609 Sep  7 11:52 2035.txt
-rw-rw-r--  1 sfmqrb sfmqrb  420719 Sep  7 11:52 2039.png
-rw-rw-r--  1 sfmqrb sfmqrb    3935 Sep  7 11:52 2039.txt
-rw-rw-r--  1 sfmqrb sfmqrb  436943 Sep  7 13:39 2049.png
-rw-rw-r--  1 sfmqrb sfmqrb    4066 Sep  7 13:40 2049.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2090 Sep  7 13:40 2049.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  464717 Sep  7 13:41 2051.png
-rw-rw-r--  1 sfmqrb sfmqrb    3925 Sep  7 13:41 2051.txt
-rw-rw-r--  1 sfmqrb sfmqrb  467734 Sep  7 13:37 2053.png
-rw-rw-r--  1 sfmqrb sfmqrb    3855 Sep  7 13:37 2053.txt
-rw-rw-r--  1 sfmqrb sfmqrb  431201 Sep  7 13:42 2054.png
-rw-rw-r--  1 sfmqrb sfmqrb    4060 Sep  7 13:42 2054.txt
-rw-rw-r--  1 sfmqrb sfmqrb  397295 Sep  7 13:40 2055.png
-rw-rw-r--  1 sfmqrb sfmqrb    3877 Sep  7 13:40 2055.txt
-rw-rw-r--  1 sfmqrb sfmqrb  169342 Sep  7 11:52 2058.png
-rw-rw-r--  1 sfmqrb sfmqrb    3654 Sep  7 11:52 2058.txt
-rw-rw-r--  1 sfmqrb sfmqrb 1133377 Sep  7 11:55 2060.png
-rw-rw-r--  1 sfmqrb sfmqrb    2428 Sep  7 11:55 2060.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1942 Sep  7 11:56 2060.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  436869 Sep  7 13:40 2062.png
-rw-rw-r--  1 sfmqrb sfmqrb    4369 Sep  7 13:41 2062.txt
-rw-rw-r--  1 sfmqrb sfmqrb  161573 Sep  7 13:41 2068.png
-rw-rw-r--  1 sfmqrb sfmqrb    3433 Sep  7 13:41 2068.txt
-rw-rw-r--  1 sfmqrb sfmqrb  416989 Sep  7 12:11 2069.png
-rw-rw-r--  1 sfmqrb sfmqrb    3764 Sep  7 12:11 2069.txt
-rw-rw-r--  1 sfmqrb sfmqrb  156736 Sep  7 11:52 2071.png
-rw-rw-r--  1 sfmqrb sfmqrb    3519 Sep  7 11:52 2071.txt
-rw-rw-r--  1 sfmqrb sfmqrb  426384 Sep  7 11:53 2073.png
-rw-rw-r--  1 sfmqrb sfmqrb    3575 Sep  7 11:53 2073.txt
-rw-rw-r--  1 sfmqrb sfmqrb  176856 Sep  7 11:53 2076.png
-rw-rw-r--  1 sfmqrb sfmqrb    4220 Sep  7 11:53 2076.txt
-rw-rw-r--  1 sfmqrb sfmqrb  409985 Sep  7 12:11 2079.png
-rw-rw-r--  1 sfmqrb sfmqrb    3744 Sep  7 12:11 2079.txt
-rw-rw-r--  1 sfmqrb sfmqrb  501074 Sep  5 22:15 2080.png
-rw-rw-r--  1 sfmqrb sfmqrb    5077 Sep  5 22:15 2080.txt
-rw-rw-r--  1 sfmqrb sfmqrb  166089 Sep  5 16:31 2083.png
-rw-rw-r--  1 sfmqrb sfmqrb    3634 Sep  5 16:31 2083.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1238 Sep  7 12:21 2083.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  171185 Sep  7 12:11 2084.png
-rw-rw-r--  1 sfmqrb sfmqrb    4130 Sep  7 12:11 2084.txt
-rw-rw-r--  1 sfmqrb sfmqrb  189036 Sep  7 15:32 2086.png
-rw-rw-r--  1 sfmqrb sfmqrb    4436 Sep  7 15:32 2086.txt
-rw-rw-r--  1 sfmqrb sfmqrb  188700 Sep  7 14:21 2095.png
-rw-rw-r--  1 sfmqrb sfmqrb    3336 Sep  7 14:21 2095.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1832 Sep  7 14:22 2095.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  400069 Sep  5 16:14 2099.png
-rw-rw-r--  1 sfmqrb sfmqrb    3804 Sep  5 16:14 2099.txt
-rw-rw-r--  1 sfmqrb sfmqrb  429736 Sep  7 13:41 2107.png
-rw-rw-r--  1 sfmqrb sfmqrb    4324 Sep  7 13:41 2107.txt
-rw-rw-r--  1 sfmqrb sfmqrb  154350 Sep  7 13:42 2130.png
-rw-rw-r--  1 sfmqrb sfmqrb    3617 Sep  7 13:42 2130.txt
-rw-rw-r--  1 sfmqrb sfmqrb  149510 Sep  6 11:27 2133.png
-rw-rw-r--  1 sfmqrb sfmqrb    3204 Sep  6 11:27 2133.txt
-rw-rw-r--  1 sfmqrb sfmqrb  135836 Sep  7 15:37 2134.png
-rw-rw-r--  1 sfmqrb sfmqrb    2902 Sep  7 15:38 2134.txt
-rw-rw-r--  1 sfmqrb sfmqrb  187781 Sep  7 14:22 2136.png
-rw-rw-r--  1 sfmqrb sfmqrb    4792 Sep  7 14:22 2136.txt
-rw-rw-r--  1 sfmqrb sfmqrb  442354 Sep  4 15:42 2143.png
-rw-rw-r--  1 sfmqrb sfmqrb    3763 Sep  4 15:42 2143.txt
-rw-rw-r--  1 sfmqrb sfmqrb  160377 Sep  6 17:36 2147.png
-rw-rw-r--  1 sfmqrb sfmqrb    3531 Sep  6 17:36 2147.txt
-rw-rw-r--  1 sfmqrb sfmqrb  171078 Sep  7 13:38 2155.png
-rw-rw-r--  1 sfmqrb sfmqrb    4323 Sep  7 13:38 2155.txt
-rw-rw-r--  1 sfmqrb sfmqrb  149311 Sep  6 18:17 2157.png
-rw-rw-r--  1 sfmqrb sfmqrb    3410 Sep  6 18:17 2157.txt
-rw-rw-r--  1 sfmqrb sfmqrb  159377 Sep  6 18:13 2163.png
-rw-rw-r--  1 sfmqrb sfmqrb    3571 Sep  6 18:13 2163.txt
-rw-rw-r--  1 sfmqrb sfmqrb  174900 Sep  7 15:42 2165.png
-rw-rw-r--  1 sfmqrb sfmqrb    4270 Sep  7 15:42 2165.txt
-rw-rw-r--  1 sfmqrb sfmqrb  121802 Sep  7 14:19 2167.png
-rw-rw-r--  1 sfmqrb sfmqrb    2583 Sep  7 14:19 2167.txt
-rw-rw-r--  1 sfmqrb sfmqrb  537986 Sep 13 20:59 216.png
-rw-rw-r--  1 sfmqrb sfmqrb    1125 Sep 13 20:59 216.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  424467 Sep  7 14:19 2170.png
-rw-rw-r--  1 sfmqrb sfmqrb    3775 Sep  7 14:19 2170.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1487 Sep  7 14:20 2170.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  129763 Sep  7 15:33 2173.png
-rw-rw-r--  1 sfmqrb sfmqrb    2723 Sep  7 15:33 2173.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1264 Sep  7 15:34 2173.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  344471 Sep  7 15:38 2195.png
-rw-rw-r--  1 sfmqrb sfmqrb    3187 Sep  7 15:38 2195.txt
-rw-rw-r--  1 sfmqrb sfmqrb     762 Sep  7 15:39 2195.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1063 Sep  5 02:20 220.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  150850 Sep  7 15:38 2210.png
-rw-rw-r--  1 sfmqrb sfmqrb    3685 Sep  7 15:38 2210.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1091 Sep  7 15:39 2210.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  175959 Sep  4 16:03 2222.png
-rw-rw-r--  1 sfmqrb sfmqrb    4471 Sep  4 16:03 2222.txt
-rw-rw-r--  1 sfmqrb sfmqrb  172443 Sep  5 16:41 2224.png
-rw-rw-r--  1 sfmqrb sfmqrb    4308 Sep  5 16:41 2224.txt
-rw-rw-r--  1 sfmqrb sfmqrb  160789 Sep  7 13:41 2226.png
-rw-rw-r--  1 sfmqrb sfmqrb    3825 Sep  7 13:41 2226.txt
-rw-rw-r--  1 sfmqrb sfmqrb  176049 Sep  7 14:22 2228.png
-rw-rw-r--  1 sfmqrb sfmqrb    4094 Sep  7 14:22 2228.txt
-rw-rw-r--  1 sfmqrb sfmqrb  397725 Sep  7 13:38 2233.png
-rw-rw-r--  1 sfmqrb sfmqrb    3574 Sep  7 13:39 2233.txt
-rw-rw-r--  1 sfmqrb sfmqrb  158497 Sep  6 11:25 2242.png
-rw-rw-r--  1 sfmqrb sfmqrb    3925 Sep  6 11:25 2242.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1558 Sep  6 11:26 2242.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  186249 Sep  4 19:06 2246.png
-rw-rw-r--  1 sfmqrb sfmqrb    4787 Sep  4 19:06 2246.txt
-rw-rw-r--  1 sfmqrb sfmqrb     805 Sep  4 19:14 2246.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  153553 Sep  6 18:19 2258.png
-rw-rw-r--  1 sfmqrb sfmqrb    3635 Sep  6 18:19 2258.txt
-rw-rw-r--  1 sfmqrb sfmqrb  159195 Sep  6 18:19 2279.png
-rw-rw-r--  1 sfmqrb sfmqrb    3455 Sep  6 18:19 2279.txt
-rw-rw-r--  1 sfmqrb sfmqrb  161090 Sep  5 16:37 2293.png
-rw-rw-r--  1 sfmqrb sfmqrb    3927 Sep  5 16:37 2293.txt
-rw-rw-r--  1 sfmqrb sfmqrb  146680 Sep  7 12:16 2316.png
-rw-rw-r--  1 sfmqrb sfmqrb    3273 Sep  7 12:16 2316.txt
-rw-rw-r--  1 sfmqrb sfmqrb     842 Sep  7 12:21 2316.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  139260 Sep  5 22:15 2331.png
-rw-rw-r--  1 sfmqrb sfmqrb    2882 Sep  5 22:15 2331.txt
-rw-rw-r--  1 sfmqrb sfmqrb  173269 Sep  6 10:59 2395.png
-rw-rw-r--  1 sfmqrb sfmqrb    4408 Sep  6 10:59 2395.txt
-rw-rw-r--  1 sfmqrb sfmqrb  178528 Sep  5 16:12 2396.png
-rw-rw-r--  1 sfmqrb sfmqrb    4354 Sep  5 16:12 2396.txt
-rw-rw-r--  1 sfmqrb sfmqrb  169473 Sep  5 16:26 2406.png
-rw-rw-r--  1 sfmqrb sfmqrb    4202 Sep  5 16:26 2406.txt
-rw-rw-r--  1 sfmqrb sfmqrb  166000 Sep  4 14:53 2407.png
-rw-rw-r--  1 sfmqrb sfmqrb    3983 Sep  4 14:53 2407.txt
-rw-rw-r--  1 sfmqrb sfmqrb  144481 Sep  6 11:25 2417.png
-rw-rw-r--  1 sfmqrb sfmqrb    3114 Sep  6 11:25 2417.txt
-rw-rw-r--  1 sfmqrb sfmqrb     561 Sep  6 11:25 2417.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  161891 Sep  6 11:16 2420.png
-rw-rw-r--  1 sfmqrb sfmqrb    3629 Sep  6 11:16 2420.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2009 Sep  6 11:17 2420.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  153589 Sep  5 16:27 2427.png
-rw-rw-r--  1 sfmqrb sfmqrb    3424 Sep  5 16:27 2427.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1757 Sep  5 16:28 2427.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2615 Sep  4 15:28 31.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  512022 Sep  5 16:12 333.png
-rw-rw-r--  1 sfmqrb sfmqrb    1339 Sep  5 16:12 333.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  527696 Sep 13 20:59 436.png
-rw-rw-r--  1 sfmqrb sfmqrb    1425 Sep 13 20:59 436.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1508 Sep  4 15:27 58.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1931 Sep  4 15:02 70.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  257093 Sep  7 16:31 71.png
-rw-rw-r--  1 sfmqrb sfmqrb    1476 Sep  7 16:31 71.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1606 Sep  4 14:54 72.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  669351 Sep  5 01:38 733.png
-rw-rw-r--  1 sfmqrb sfmqrb    1152 Sep  5 01:39 733.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  726576 Sep  6 18:36 829.png
-rw-rw-r--  1 sfmqrb sfmqrb     981 Sep  6 18:36 829.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  624515 Sep  5 16:20 902.png
-rw-rw-r--  1 sfmqrb sfmqrb    1658 Sep  5 16:20 902.vision.txt
```


## [2026-09-14T00:59:49.753Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T00:59:49.810Z] TOOL RESULT

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


## [2026-09-14T01:01:37.973Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:08:06.139Z] TOOL CALL #73: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-390.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nWIKT_PIR = \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1\"\nWIKT_PARSA = \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B1%D8%B3%D8%A7\"\nWIKT_BARUD = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B1%D9%88%D8%AF\"\nWIKT_BARUT = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B1%D9%88%D8%AA\"\nWIKT_PUDR = \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%AF%D8%B1\"\nWIKT_PARUSA = \"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%B0%E0%A5%81%E0%A4%B7\"\nEO_FALCON = \"https://www.etymonline.com/word/falcon\"\nEO_POWDER = \"https://www.etymonline.com/word/powder\"\nEO_POLLEN = \"https://www.etymonline.com/word/pollen\"\nEO_PALE = \"https://www.etymonline.com/word/pale\"\nAHD_POWDER = \"https://ahdictionary.com/word/search.html?q=powder\"\n\ndata = {\n  \"pdf_page\": 390,\n  \"book_page\": 360,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Pel 2, Porkwos\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *pelH- / *pel- 'pale, grey' (Pokorny 6. pel- 804-805; Watkins pel-2 'Pale') — but Nourai's second label 'Porkwos' is S. E. Mann's separate reconstruction *porkʷuos 'bright, clear, clean, pure' (IEC 977-978), not the same root\",\n      \"note\": \"The root box merges two different reconstructions. (a) Pokorny's 6. pel- 'grau; fahl' (IEW 804-805) is uncontroversial and carries exactly the material Nourai draws from it: 'ai. palitá-, paruṣá- \\\"fleckig\\\" = av. paourusa- \\\"grau, greis\\\"; pers. pīr \\\"grau\\\" (*parya-)'; Latin pallēre, pallidus, Gmc *falwa-, OHG falco all sit there too. (b) 'Porkwos' is Mann's headword 'porKuos, is \\\"bright, clear, clean, pure\\\"' at IEC 977-978, where the members are Hittite parkui- 'pure', Gothic farwa 'shape', Armenian parz 'clear', and — the point of Nourai's arrow — 'Per. pārsā \\\"chaste, pious\\\"', with Skt. paruṣáh and Av. pauruṣō listed as 'variants'. Mann's identification of the 'grey/speckled' family with a 'bright, pure' family is his own and is not shared by Pokorny, Walde-Pokorny, Watkins or Wiktionary, which keep *pelH- 'grey' and the *perḱ-/*pork̑- 'speckled, bright' material apart. Language label 'Indo-European' and the two glosses are each correct for their own reconstruction; the merger is what makes the box only plausible.\",\n      \"note_fa\": \"این قاب ریشه در واقع دو بازسازی جداگانه را در هم آمیخته است. نخست ریشهٔ هندواروپایی آغازین *pelH- «خاکستری، پریده‌رنگ» که پوکورنی (ص ۸۰۴–۸۰۵) آن را با اوستایی paourusa-، سنسکریت paruṣá-، لاتینی pallēre و فارسی «پیر» گرد آورده و کاملاً پذیرفتهٔ پژوهش امروزی است. دوم Porkwos که برساختهٔ شخصی مان (Mann) در فرهنگ تطبیقی هندواروپایی ص ۹۷۷–۹۷۸ است به معنای «روشن، پاک، خالص» و اعضای آن هیتی parkui-، گوتی farwa و «پارسا»ی فارسی‌اند. یکی‌گرفتن این دو ریشه از آنِ مان و نورایی است و پوکورنی، والده‑پوکورنی، واتکینز و ویکی‌واژه آن را نمی‌پذیرند. بنابراین ریشه و زبان و معنی هر یک درست است، اما ادغام آن دو تنها «با احتیاط پذیرفتنی» است.\",\n      \"sources\": [WIKT_PARUSA, WIKT_PARSA],\n      \"ref_check\": [\n        {\"ref\": \"POK:804\", \"status\": \"supports\", \"note\": \"Pokorny IEW, 'Root/lemma: pel-6, Meaning: grey; pale', Page(s) 804-805 (POK_full.txt line 66056; printed text in POK_03.txt leaf 38-39 = pp. 804-805): 'Old Indic palita-, ... parusa- \\\"marked, stained\\\" = Avestan pourusa-, paourusa- \\\"gray, old\\\"; pers. pir \\\"gray\\\" (*parya-)'. Exactly the root, gloss and members Nourai's box claims.\"},\n        {\"ref\": \"IEC:977\", \"status\": \"supports\", \"note\": \"Mann, An Indo-European Comparative Dictionary, p. 977 (IEC.txt leaf 543, running head 'poreio — porso', printed 977/978): 'porKuos, is \\\"bright, clear, clean, pure\\\" | Per. pārsā \\\"chaste, pious\\\"; (LW in) Arm. parz ... Hitt. parkwis ... adj. \\\"pure, guiltless\\\" ... Go. farwa, f. \\\"shape\\\" ... Variants in Skt. parusáh (1) \\\"motley\\\"; Av. pauruso (alleged), id.' — the source of Nourai's second root label and of node #3.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 53 (WLD_Bd2_pages.txt leaf idx 57)\", \"stance\": \"supports\", \"note\": \"'5. pel- in Ausdrücken für unscharfe Farben wie \\\"grau, schwärzlich, fahl\\\", auch \\\"scheckig\\\". Ai. palitá- ... paruṣá- \\\"fleckig\\\" = av. paourusa- \\\"grau, greis\\\" (Bartholomae Wb. 903)' — the 'grey' half of the box, with no 'pure/clean' branch.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pel-2 (AHD_watkins1985.txt line 832)\", \"stance\": \"supports\", \"note\": \"'pel-2. Pale. 1. Suffixed variant form *pal-wo- ... b. Latin pallere, to be pale: PALE, PALLID, PALLOR; APPALL ... [Pok. 6. pel- 804.]' — same root, same page reference as Nourai's POK:804; Watkins has no 'bright, clean, pure' sense.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann p. 902 'pel- (2) \\\"grey; grey object or creature\\\". WP II, 53' (IEC.txt line 12621)\", \"stance\": \"partial\", \"note\": \"Mann himself keeps a separate 'grey' root pel- (2) apart from porKuos, so even Nourai's own authority does not fuse the two boxes.\"},\n        {\"src\": \"KLN\", \"where\": \"s.v. fallow / pallor (KLN_1966.txt lines 14333, 27034)\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *pel-, \\\"dark-colored, gray\\\", whence also OI. palitah \\\"gray\\\" ... L. pallere \\\"to be pale\\\", pallor \\\"paleness\\\" ...' — the 'grey/pale' root confirmed; Klein knows no 'pure' sense for it.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 14.15 OLD (SYN.txt line 24433) and 1.214 (line 882)\", \"stance\": \"silent\", \"note\": \"Buck's 'OLD' table has no New Persian column and does not treat pīr; at 1.214 he only mentions in passing 'Grk. polios \\\"gray\\\", Lat. pallēre \\\"be pale\\\", etc. Walde-P. 2.53'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"pouruša, parya\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Av. pouruša- (also paourusa-) 'grey, hoary' is genuine and well attested: Bartholomae, Altiranisches Wörterbuch col. 903, 'pouruša- (, paourusa-) Adj. \\\"grau, greis\\\"', with the Pahlavi gloss on Vd. 7.57 *pourušō asti varəsō 'greis ist das Haar'. It continues Proto-Indo-Iranian *parHušás < PIE *pelH-u-s-ó- and is the exact match of Sanskrit paruṣá- (node #4), the -š- being the regular RUKI development of *-s- after *u. The second form 'parya' is a different matter: it is not an attested Avestan word but a starred Old Iranian reconstruction *pariya-/*parya- that Bartholomae supplied to Horn by letter (Horn, Grundriss no. 286 n. 1: 'Bartholomae ... nimmt für np. pir als Grundform ein ap. *pariya- an und vergleicht zur Bedeutung ai. purāṇa-') and that Moʿin repeats in his footnote at Borhān 436 as 'قس: اوستا parô * parya (پیشین)', i.e. glossed 'former, prior', not 'grey, old'. Nourai prints it without the asterisk and under the Avestan label with the gloss of pouruša-. The first word is confirmed, the second is a reconstruction of different meaning presented as an attested Avestan form.\",\n          \"derivation_fa\": \"واژهٔ اوستایی pouruša- (و گونهٔ paourusa-) به معنای «خاکستری، سپیدموی، پیر» کاملاً ثبت شده است؛ بارتولومه در فرهنگ ایرانی باستان ستون ۹۰۳ آن را «grau, greis» معنی کرده و شاهد وندیداد ۷٫۵۷ را آورده است. این صورت از هندوایرانی آغازین *parHušás و آن از هندواروپایی آغازین *pelH-u-s-ó- می‌آید و هم‌ریشهٔ دقیق سنسکریت paruṣá- است؛ تبدیل s به š پس از u همان قاعدهٔ آوایی معروف (RUKI) است. اما صورت دوم، parya، واژه‌ای اوستایی نیست بلکه بازسازی ستاره‌دار *pariya- است که بارتولومه در نامه‌ای به هرن پیشنهاد کرد (هرن، شمارهٔ ۲۸۶ پانویس ۱) و معین نیز در حاشیهٔ برهان قاطع ص ۴۳۶ آن را با معنی «پیشین» آورده است، نه «خاکستری». نورایی این صورت بازسازی‌شده را بدون ستاره و ذیل برچسب اوستایی و با معنی pouruša- چاپ کرده است؛ پس واژهٔ نخست درست و واژهٔ دوم با احتیاط پذیرفتنی است.\",\n          \"sources\": [WIKT_PARUSA, WIKT_PIR],\n          \"ref_check\": [\n            {\"ref\": \"POK:807\", \"status\": \"not_found\", \"note\": \"Pokorny p. 807 does not contain this material: POK_full.txt gives 'pelpo- or polpo- \\\"woodwork\\\"' (Page(s) 807), 'pen-1 \\\"to feed\\\"' (807) and 'pen-2 \\\"swamp\\\"' (807-808); the printed POK_03.txt leaf 41 (= p. 807) has parpa-/pelpo- and penkʷe follows on leaf 42. The Avestan pouruša- material is at pp. 804-805 (leaf 38-39) under pel-6, i.e. the page Nourai cites in the root box. The node's page number is off by three.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 903 (BRT.txt line 16311)\", \"stance\": \"supports\", \"note\": \"'j. pouruša- (, paourusa-) Adj. \\\"grau, greis\\\"; *°sō asti varšō \\\"greis ist das Haar\\\" V. 7.57 Gl.' Bartholomae has no Avestan headword parya-.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 53\", \"stance\": \"supports\", \"note\": \"'ai. ... paruṣá- \\\"fleckig\\\" = av. paourusa- \\\"grau, greis\\\" (Bartholomae Wb. 903)' — the Avestan word and its Sanskrit equation.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p. 978\", \"stance\": \"partial\", \"note\": \"'Variants in Skt. parusáh (1) \\\"motley\\\"; Av. pauruso (alleged), id.' — Mann flags the Avestan form as 'alleged' under porKuos; he does not know a form parya.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 286 footnote 1, pp. 64-65 (HRN.txt lines 2811-2818)\", \"stance\": \"partial\", \"note\": \"'Bartholomae (briefliche Mitteilung) nimmt für np. pir als Grundform ein ap. *pariya- an und vergleicht zur Bedeutung ai. purāṇa-' — the source of the form, explicitly starred and Old Persian, not Avestan.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"pîr «پیر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP پیر pīr 'old, aged; elder, Sufi master' continues Middle Persian pīr [pyl] 'old, aged, ancient' (MacKenzie, Concise Pahlavi Dictionary s.v. pir), which Horn already noted is attested in Pahlavi with the meaning 'old' firmly fixed, so that a derivation from pitar- 'father' is impossible. The Old Iranian antecedent is disputed in the older literature: Bartholomae (through Horn) and Moʿin reconstruct *par(i)ya- 'older, former'; Hübschmann (Persische Studien, 'pīr \\\"alt\\\" aus *piry- = *pirvy- = *p(a)rvya-') derives it from *parwya- 'first, foremost' (cf. Av. paourviia-, OP paruviya-, whence NP pirār 'the year before last'). Modern Iranian etymology sides with Nourai's grouping: Edelʹman, Etimologičeskij slovarʹ iranskix jazykov (2020) p. 172, followed by Wiktionary, derives pīr from Proto-Iranian *paru- 'ash-grey, pale grey, hoary' < PII *parHušás, i.e. the same etymon as Av. pouruša- and Skt. paruṣá-. The semantics are the usual 'grey-haired' > 'old' > 'elder, spiritual guide', the last sense being the Sufi one in the Hāfez couplet Nourai quotes (بندهٔ پیر خراباتم که لطفش دایم است). Strictly, pīr does not descend from the Avestan word but from a sister Old Persian/Middle Persian form of the same stem.\",\n          \"derivation_fa\": \"«پیر» در فارسی نو از فارسی میانهٔ pīr (نوشتهٔ pyl) به معنی «سالخورده، کهن» می‌آید؛ مکنزی در فرهنگ کوچک پهلوی آن را ثبت کرده و هرن نیز تأکید دارد که چون این واژه پیش‌تر در پهلوی با همین معنی به کار رفته، اشتقاق آن از pitar- «پدر» ناممکن است. دربارهٔ صورت ایرانی باستانِ آن اختلاف هست: بارتولومه و به پیروی او معین *parya- «پیشین» را پیشنهاد کرده‌اند، ولی هوبشمان آن را از *parwya- «نخستین» گرفته است (قس فارسی «پیرار»). ریشه‌شناسی امروزی — ادلمان در فرهنگ ریشه‌شناختی زبان‌های ایرانی (۲۰۲۰، ص ۱۷۲) و به پیروی او ویکی‌واژه — همان چیزی را می‌گوید که نورایی رسم کرده است: pīr از ایرانی آغازین *paru- «خاکستری، سپیدموی» و هم‌ریشه با اوستایی pouruša- و سنسکریت paruṣá-. تحول معنایی نیز طبیعی است: «سپیدمو» ← «سالخورده» ← «مرشد و پیرِ طریقت»، که همان معنی در بیت حافظ دیده می‌شود. تنها نکته آنکه «پیر» از خودِ واژهٔ اوستایی نمی‌آید، بلکه از صورت هم‌عرضِ پارسی باستان/میانهٔ همان ستاک. ادعای نورایی درست است.\",\n          \"sources\": [WIKT_PIR, WIKT_PARUSA],\n          \"ref_check\": [\n            {\"ref\": \"BQT:436\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, printed p. ٤٣٦ (archive.org borhan-ghate-v1 leaf n662, page image read and saved to data/verification/sources/refs/ocr/BQT/436.png + 436.vision.txt). Moʿin's footnote 5 on the headword پیر: «در فارسی نیز بمعنی سالخورده، مقابل جوان؛ پهلوی pîr «اونوالا ۵۸۱» «اسنق ۳۵۰»، کردی و افغانی pîr، قس: اوستا parô * parya (پیشین) «اسنق ایضاً»، گیلکی pir ...» — i.e. exactly Nourai's Avestan *parya- > Persian pīr arrow, though Moʿin glosses parya as 'پیشین' (former), not 'grey'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 68 s.v. pir (PHD.txt line 551)\", \"stance\": \"supports\", \"note\": \"'pir [pyl | N ~] old, aged, ancient. ~ih: age.' — the Middle Persian intermediate Nourai's chart passes over silently.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 286 n. 1 (HRN.txt lines 2811-2818)\", \"stance\": \"partial\", \"note\": \"'Pir findet sich jedoch bereits im Pehlevi, und die Bedeutung \\\"alt\\\" ist dort schon so fest, dass an eine Ableitung von pitar- ... nicht gedacht werden kann. Bartholomae ... nimmt für np. pir als Grundform ein ap. *pariya- an' — supports the *parya- route but with 'old/former', not 'grey', semantics.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien (HUB.txt lines 4594, 5102)\", \"stance\": \"contradicts\", \"note\": \"'pīr \\\"alt\\\" = *piry- = *pirvy- = *p(a)rvya-' and, at line 1522, 'Np. pirār \\\"das vorvergangene Jahr\\\" = ap. p(a)ruviya-' — Hübschmann derives pīr from *parwya- 'first, former', not from the 'grey' root.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt; grep 'pyr', 'p.rs.y')\", \"stance\": \"silent\", \"note\": \"no pīr headword in the OCR of Nyberg's glossary.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt (grep 'پیر', 'PIR')\", \"stance\": \"silent\", \"note\": \"Aryanpur's Persian IE-roots dictionary has no entry for پیر in the OCR; the only 'PIR' hit is the pol/pird 'bridge' family.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"pârsâ «پارسا»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"NP پارسا 'abstinent, pious, chaste' (older/variant پارسای, which Nourai prints in the box) is drawn straight from the IE root box with no Old or Middle Iranian intermediate — and none is attested. Nourai's authority is Mann, who lists 'Per. pārsā \\\"chaste, pious\\\"' as the first member of his *porkʷuos 'bright, clear, clean, pure' (IEC 977), beside Hittite parkui- 'pure' and Gothic farwa. Modern scholarship prefers a quite different origin. Horn rejected the connection with 'abstinence' outright: 'Pārsā bedeutet überhaupt nicht \\\"enthaltsam\\\", sondern ursprünglich nur \\\"brav\\\" (vergl. Šāhn. I, 35 V. 15 ...), es bezeichnet gewiss eigentlich den Pärsen' (Grundriss no. 309 n. 2, p. 68) — i.e. pārsā is the gentilic, OP Pārsa- > MP Pārs 'Persia, Persian', the sense 'pious' arising from the Zoroastrian self-designation, with the earliest sense simply 'upright, good'. Wiktionary likewise: the origin 'is uncertain' and the word 'is not found in Middle Persian', the usual link being to MP 𐭯𐭠𐭫𐭮𐭩 Pārs 'Persia'. The word's earliest literary life (Šāhnāma, Saʿdi's Golestān) fits the 'Persian/upright man' sense. Nourai's arrow therefore rests on a single idiosyncratic reconstruction that the standard handbooks do not follow.\",\n          \"derivation_fa\": \"«پارسا» (و گونهٔ کهن‌ترِ «پارسای» که نورایی در همان قاب آورده) در نمودار او یکراست از ریشهٔ هندواروپایی گرفته شده، بی هیچ واسطهٔ ایرانی باستان یا فارسی میانه — و چنین واسطه‌ای هم در دست نیست. مأخذ نورایی مان است که در ص ۹۷۷ فرهنگ خود «پارسا»ی فارسی را نخستین عضو ریشهٔ برساختهٔ *porkʷuos «روشن، پاک» می‌شمارد، در کنار هیتی parkui- «پاک» و گوتی farwa. اما پژوهش امروزی سرچشمهٔ دیگری را ترجیح می‌دهد: هرن (شمارهٔ ۳۰۹ پانویس ۲) به‌صراحت می‌نویسد که «پارسا» اصلاً به معنی «پرهیزگار» نبوده بلکه در آغاز تنها «نیک و برومند» معنی می‌داده و در حقیقت نامِ «پارسی» است؛ ویکی‌واژه نیز ریشه را نامعلوم می‌داند، یادآور می‌شود که این واژه در فارسی میانه دیده نشده و معمولاً آن را به Pārs «پارس» می‌پیوندند و معنی «پرهیزگار» را برخاسته از خودنامیِ زرتشتیان می‌شمارد. پس ریشه‌شناسی نورایی بر یک بازسازی یکه استوار است و پژوهش امروزی آن را رد می‌کند.\",\n          \"sources\": [WIKT_PARSA],\n          \"ref_check\": [\n            {\"ref\": \"MON:653\", \"status\": \"partial\", \"note\": \"Moʿin, Farhang-e Fārsi s.v. پارسا (MON_part1.txt line 27947): «پارسا: [= پارسای] (ص.) آنکه از گناهان پرهیزد و به طاعت و عبادت و قناعت عمر گذارد، پرهیزکار، پاکدامن، زاهد، متقی، دیندار ... مق. ناپارسا؛ ج. پارسایان» — the word, the gloss 'chaste/abstinent' and the variant پارسای that Nourai prints, but Moʿin gives no origin tag and no etymology, so the page supports the gloss only, not the IE arrow. (The OCR text carries no printed page numbers, so 'p. 653' itself could not be verified.)\"},\n            {\"ref\": \"IEC:977\", \"status\": \"supports\", \"note\": \"Mann p. 977 (IEC.txt leaf 543): 'porKuos, is \\\"bright, clear, clean, pure\\\" | Per. pārsā \\\"chaste, pious\\\"; (LW in) Arm. parz ... Hitt. parkwis ... \\\"pure, guiltless\\\"'. This is verbatim Nourai's claim — his own reference does support him.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 309 footnote 2, p. 68 (HRN.txt lines 2963-2965)\", \"stance\": \"contradicts\", \"note\": \"'Pärsä bedeutet überhaupt nicht \\\"enthaltsam\\\", sondern ursprünglich nur \\\"brav\\\" ... es bezeichnet gewiss eigentlich den Pärsen.' Horn derives the word from the ethnic name, not from a 'pure' root.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie (PHD.txt / PHD_mackenzie.txt, grep 'p.rs')\", \"stance\": \"silent\", \"note\": \"no MP headword pārsāy/pārsā in the Concise Pahlavi Dictionary OCR — consistent with Wiktionary's note that the word 'is not found in Middle Persian'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II glossary (grep 'p.rs.y')\", \"stance\": \"silent\", \"note\": \"no pārsāy entry found.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Moʿin (BQT_v1_pages.txt, grep پارسا)\", \"stance\": \"silent\", \"note\": \"no etymological footnote of Moʿin on پارسا was located in the vol. 1 OCR.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. پارسا\", \"stance\": \"contradicts\", \"note\": \"'The origin is uncertain ... is not found in Middle Persian. However, scholars frequently suggest a connection to Middle Persian 𐭯𐭠𐭫𐭮𐭩 (Pārs, \\\"Persia\\\")', with the Zoroastrian 'chosen people' motivation for the sense 'pious'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"parŭsah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit paruṣá- (Nourai's parŭsah = paruṣaḥ) is attested from the Ṛgveda in the sense 'spotted, variegated, dirty-coloured' (of oxen 'of speckled hue'), later also 'rough, harsh'. Nourai's gloss 'colorful' renders the first sense; Walde-Pokorny give it as 'fleckig'. It is formed *pelH-u-s-ó- > PII *parHušás, the exact cognate of Avestan pouruša- (node #1) and the immediate source of the Wiktionary/Edelʹman reconstruction from which NP pīr is derived. Walde-Pokorny II 53 sets the equation explicitly: 'ai. ... paruṣá- \\\"fleckig\\\" = av. paourusa- \\\"grau, greis\\\"'. The semantic range 'grey ~ speckled ~ dirty-coloured' is the normal one for this root (cf. Gk. peliós, pellós, Lat. pullus).\",\n          \"derivation_fa\": \"واژهٔ سنسکریت paruṣá- از ریگ‌ودا به معنی «خال‌خال، رنگارنگ، تیره‌رنگ» به‌کار رفته است (و بعدها «درشت، خشن»)؛ همان که نورایی «colorful» ترجمه کرده و والده‑پوکورنی «fleckig» آورده‌اند. ساخت آن *pelH-u-s-ó- است که در هندوایرانی آغازین *parHušás شده و هم‌ریشهٔ دقیق اوستایی pouruša- است. والده‑پوکورنی (جلد دوم ص ۵۳) این برابری را به‌صراحت آورده‌اند. گسترهٔ معنایی «خاکستری ~ خال‌خال ~ تیره» برای این ریشه عادی است (قس یونانی peliós و لاتینی pullus). ادعای نورایی درست است.\",\n          \"sources\": [WIKT_PARUSA],\n          \"ref_check\": [\n            {\"ref\": \"IEC:978\", \"status\": \"supports\", \"note\": \"Mann p. 978 (IEC.txt leaf 543, s.v. porKuos): 'Variants in Skt. parusáh (1) \\\"motley\\\"; Av. pauruso (alleged), id.' — the word, the 'motley/colourful' gloss and the attachment to the root box are all there, though Mann files it under his *porkʷuos rather than under a 'grey' root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 53\", \"stance\": \"supports\", \"note\": \"'Ai. palitá- ... paruṣá- \\\"fleckig\\\" = av. paourusa- \\\"grau, greis\\\"' — the Sanskrit-Avestan equation under the 'grey, fahl' root.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 804-805 s.v. pel-6 (POK_full.txt line 66056)\", \"stance\": \"supports\", \"note\": \"'Old Indic palita- ... parusa- \\\"marked, stained\\\" = Avestan pourusa-, paourusa- \\\"gray, old\\\"'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. परुष\", \"stance\": \"supports\", \"note\": \"'spotted, variegated, dirty-colored' (RV); 'from Proto-Indo-Iranian *parHušás, from PIE *pelHu-só-s, root *pelH- \\\"gray, pale\\\"', cognates Av. pouruša, Persian pir, Latin pallidus.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"pallěre; falcô\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two words of unequal standing. (1) pallēre 'to be pale' (with pallor, pallidus) is a secure member of the root: Latin pallidus goes back to *paluos, older *polwos = Gmc *falwa-, Lith. palvas, OCS plavŭ (Pokorny 805, Walde-Pokorny II 53-54, Klein s.v. pallor). Confirmed. (2) falcō 'falcon' is contested, and even on the view Nourai follows the chart is drawn wrongly. Pokorny and Walde-Pokorny put the bird here only through Germanic — 'mit dem germ. k-Formans wie in anderen Vogelnamen hieher vermutlich ahd. falco \\\"Falke\\\" (spätlat. falco aus dem Germ.)' — i.e. Late Latin falcō is a loan FROM Germanic *falkōn- 'the grey bird', not an inherited Latin descendant of the root; Watkins says the same, adding the hedge 'but Germanic *falkōn- is also possibly from the Late Latin'. The majority view is different again: Klein s.v. falcon takes Late L. falcō as identical with falcō, -ōnis 'bow-legged', from falx 'sickle', after the curved talons; Ernout-Meillet s.v. falco simply refer to falx; Etymonline treats the falx explanation as primary and notes that the Germanic 'grey bird' theory is opposed because falconry reached the Germanic peoples from the East via Rome, not the other way round. The gloss 'gray bird' is Watkins's parenthesis about the Germanic etymon, not a meaning of Latin falcō.\",\n          \"derivation_fa\": \"دو واژه با پایگاه ناهمسان. نخست pallēre «رنگ‌پریده بودن» (با pallor و pallidus) که عضو مسلّم این ریشه است: pallidus از *paluos و کهن‌تر *polwos، برابر با ژرمنی *falwa- و لیتوانیایی palvas (پوکورنی ص ۸۰۵؛ والده‑پوکورنی II/۵۳–۵۴؛ کلاین). این بخش تأیید می‌شود. دوم falcō «شاهین»: حتی بر پایهٔ همان دیدگاهی که نورایی برگزیده، نمودار نادرست رسم شده است، زیرا پوکورنی و واتکینز falco را واژه‌ای ژرمنی (*falkōn- «پرندهٔ خاکستری») می‌دانند که لاتینی متأخر آن را وام گرفته است، نه بازماندهٔ خودِ لاتین از ریشه. از سوی دیگر دیدگاه رایج‌تر (کلاین، ارنو–می‌یه، اتیمآنلاین) falcō را از falx «داس» می‌گیرد، به سبب چنگال‌های داسی‌شکل. افزون بر این، معنی «پرندهٔ خاکستری» شرحِ واتکینز دربارهٔ صورت ژرمنی است، نه معنای لاتینی falcō. پس این گره تنها با احتیاط پذیرفتنی است.\",\n          \"sources\": [EO_FALCON, EO_PALE],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. pel-2 'Pale' (AHD_watkins1985.txt line 832): '1. ... b. Latin pallēre, to be pale: PALE, PALLID, PALLOR; APPALL ... 2. Suffixed form *pel-ko- probably in Germanic *falkōn-, falcon (< \\\"gray bird\\\"), in: ... b. Late Latin falcō, falcon (but Germanic *falkōn- is also possibly from the Late Latin): FALCON. [Pok. 6. pel- 804.]' — both of Nourai's Latin words and even his 'gray bird' gloss come from this entry, hedges included.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 805 (POK_03.txt leaf 39)\", \"stance\": \"partial\", \"note\": \"'lat. palleo, -ēre \\\"blaß sein\\\", pallor, pallidus ...' supports pallēre; for the bird: 'mit dem germ. k-Formans ... hierher vermutlich ahd. falco \\\"Falke\\\" (spätlat. falco aus dem Germ.)' — the Latin form is a Germanic loan, so it cannot be a Latin node under the root.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 54\", \"stance\": \"partial\", \"note\": \"same wording as Pokorny: 'mit dem germ. k-Formans wie in anderen Vogelnamen hieher vermutlich ahd. (usw.) falco \\\"Falke\\\" (Much ZfdA. 40, 295 ff.; spätlat. falco aus dem Germ.)'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. falcon (KLN_1966.txt line 14324) and pallor (line 27034)\", \"stance\": \"contradicts\", \"note\": \"'falcon, n. — ME. faucoun fr. OF. faucon, fr. Late L. falconem, acc. of falco, prop. \\\"the bow-legged (animal)\\\", and identical with L. falco, -onis, \\\"bow-legged\\\", fr. falx, gen. falcis, \\\"sickle\\\" ... OHG. falcho ... are Latin loan words' — the opposite direction and a different root; pallor/pallere, by contrast, Klein does put under I.-E. *pel- 'dark-colored, gray'.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. falco (LAT.txt line 20356)\", \"stance\": \"contradicts\", \"note\": \"'falco, -ōnis m.: faucon. V. falx.' — Ernout-Meillet refer the bird to falx 'sickle'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"pale, appall; falcon\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"pale (adj., early 14c. 'wan, bloodless') < ME pale < OF pale < Lat. pallidus < pallēre — Klein s.v. pale, Etymonline s.v. pale, both tracing it to PIE *pel- 'pale'; pallid is its learned doublet. appall < ME appallen 'to make pale, become pale' < OF apal(l)ir 'to grow pale' (a- + palir, from pale), the modern sense 'dismay' developing from 'make (someone) turn pale' — Klein s.v. appall. Both are confirmed and both pass through French, which Nourai's single Latin > English arrow compresses. falcon < ME faucoun < OF (F.) faucon < Late Latin falcōnem: the English and French links are beyond doubt, but whether the Late Latin word belongs to this root at all is contested (see node #5), so the node as a whole is only plausible.\",\n          \"derivation_fa\": \"«pale» در انگلیسی میانه pale از فرانسهٔ کهن pale و آن از لاتینی pallidus (از pallēre) است و pallid دوگانهٔ عالمانهٔ همان؛ «appall» از انگلیسی میانهٔ appallen «رنگ‌پریده کردن/شدن» و آن از فرانسهٔ کهن apalir (پیشوند a- + palir «رنگ باختن») است و معنی امروزی «هراساندن» از همان «رنگ از رخ بردن» برآمده است. هر دو تأیید می‌شوند، هرچند نورایی با یک پیکان لاتینی←انگلیسی حلقهٔ فرانسوی را نادیده گرفته است. اما «falcon» از انگلیسی میانهٔ faucoun و فرانسهٔ کهن faucon و لاتینی متأخر falcōnem آمده که تعلق خودِ آن به این ریشه مورد مناقشه است (نگاه کنید به گرهٔ ۵). از این رو این گره در مجموع «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [EO_PALE, EO_FALCON],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. pel-2 'Pale': 'Latin pallēre, to be pale: PALE, PALLID, PALLOR; APPALL' and 'Late Latin falcō, falcon ...: FALCON' — precisely the three English words in Nourai's box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. pale (line 26970), appall (line 3157), falcon (line 14324)\", \"stance\": \"partial\", \"note\": \"'pale, adj. ... fr. OF. pale (F. pâle), fr. L. pallidus, \\\"pale\\\", fr. pallere'; 'appall, tr. v. — ME. appallen, apallen, \\\"to make pale, become pale\\\", fr. OF. apallir' — supports; but falcon Klein derives from falx, not from *pel-.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com s.v. pale, falcon\", \"stance\": \"partial\", \"note\": \"pale: 'Old French paile ... Latin pallidus ... PIE root *pel- (1) \\\"pale\\\"' — supports; falcon: the falx 'curved blade' theory is given as primary and the Germanic 'gray bird' theory as a disputed alternative ('both theories remain unresolved').\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Pel 3\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *pel- 'dust, flour' (Pokorny 2 b. pel-, pel-en-, pel-t-, pel-u- 'Staub, Mehl', IEW 802; Watkins pel-1 'Dust, flour')\",\n      \"note\": \"Root, language label and gloss are all right and the cited page is the right one. Only the numeral is Nourai's own: his 'Pel 3' is the third of his own homophonous Pel entries, not Pokorny's pel-3, which is 'to fold' (IEW 802-803) and 'to cover, skin' (803). The entry actually cited at p. 802 is Pokorny's pel-2b 'powder, flour', and Watkins renumbers the same entry pel-1 'Dust, flour' while still referring to '[Pok. 2 b. pel- 802]'. Walde-Pokorny II 60 have it as '13. pel- in Worten für \\\"Staub, Mehl\\\", weiter auch \\\"Mehlbrei\\\"'.\",\n      \"note_fa\": \"ریشه و برچسب زبانی و معنی، همه درست است و شمارهٔ صفحه‌ای هم که نورایی آورده (پوکورنی ص ۸۰۲) دقیقاً همان جای درست است. تنها شمارهٔ «۳» از آنِ خود نورایی است، یعنی سومین مدخلِ هم‌آواییِ Pel در کتاب او، نه شمارهٔ پوکورنی؛ زیرا pel-3 نزد پوکورنی «تا کردن» و «پوشاندن، پوست» است. آنچه در ص ۸۰۲ آمده pel-2b «گرد، آرد» است و واتکینز همان را pel-1 «Dust, flour» شماره زده و باز به «Pok. 2 b. pel- 802» ارجاع داده است. والده‑پوکورنی نیز در جلد دوم ص ۶۰ همین ریشه را با عنوان «pel- در واژه‌های به معنی گرد و آرد» آورده‌اند. ادعای نورایی درست است.\",\n      \"sources\": [EO_POWDER, EO_POLLEN],\n      \"ref_check\": [\n        {\"ref\": \"POK:802\", \"status\": \"supports\", \"note\": \"Pokorny IEW, 'Root/lemma: pel-2b, pel-en-, pel-t-, pel-u-, Meaning: powder, flour', Page(s) 802 (POK_full.txt lines 65903-65942): 'with u-formants: Latin pulvis, -eris \\\"dust, powder\\\" (*polui-; inflection after cinis) ... with l-formants: Latin pollen, -inis \\\"very fine flour, dust powder\\\" (ll from n equalization in inflection *polen, *polnes)'. Exactly the root, gloss and Latin members of Nourai's box.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pel-1 (AHD_watkins1985.txt line 832)\", \"stance\": \"supports\", \"note\": \"'pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: POLLEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff ... [Pok. 2 b. pel- 802.]' — the whole of Nourai's second chart in one line.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 60 (WLD_Bd2_pages.txt leaf idx 64)\", \"stance\": \"supports\", \"note\": \"'13. pel- in Worten für \\\"Staub, Mehl\\\", weiter auch \\\"Mehlbrei\\\". ... Mit u-Formans: lat. pulvis, -eris \\\"Staub\\\" (*polui-; Flexion nach cinis)'.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann pp. 902, 906, 972 (IEC.txt lines 12475, 12670 and leaf 502 'pas- (2)')\", \"stance\": \"partial\", \"note\": \"Mann splits the material: 'peluos \\\"dust, specks, chaff\\\" ... Lat. pulvis, gs: pulveris, m. \\\"dust, powder\\\"' and 'pas- (2) \\\"flour, powder, dust, pollen\\\"'; he has the same Latin word but under a differently shaped reconstruction.\"},\n        {\"src\": \"KLN\", \"where\": \"s.v. pollen (KLN_1966.txt line 29410)\", \"stance\": \"supports\", \"note\": \"'pollen, n. ... — L., also pollis, \\\"fine flour, milldust\\\", fr. I.-E. base *pel-, \\\"dust, porridge made of meal\\\", whence also ... pulvis, \\\"dust\\\" ... Cp. also polenta, powder, pulse, poultice, pulverize'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Latin\",\n          \"words\": \"pulvis, pollen\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin pulvis, gen. pulveris 'dust, powder' goes back to a u-stem *polu-i- of the root, its -er- inflection remodelled after cinis, cineris 'ash' (Pokorny 802, Walde-Pokorny II 60); pollen, gen. pollinis 'very fine flour, mill-dust' is the l-formation *polen, whose -ll- arose by levelling from the oblique stem *polnes (Pokorny 802). Both glosses in the chart ('dust') are right, pollen being specifically the finest flour. Klein s.v. pollen puts the two together under 'I.-E. base *pel-, \\\"dust, porridge made of meal\\\"' with Gk. pálē 'sifted meal', póltos 'porridge', Skt. pálalam 'ground seeds'. Etymonline is more cautious, noting that pulvis 'perhaps is related to Latin pollen', but no source proposes a different root for either word.\",\n          \"derivation_fa\": \"لاتینی pulvis (اضافی pulveris) «گرد، غبار» از ستاکِ u‑داری چون *polu-i- می‌آید که صرف -er- آن به قیاس cinis/cineris «خاکستر» بازساخته شده است (پوکورنی ص ۸۰۲؛ والده‑پوکورنی II/۶۰). واژهٔ pollen (اضافی pollinis) «آرد بسیار نرم، غبار آسیاب» صورت l‑دار *polen است که دوگانگی ll آن از همگونی با ستاک اضافیِ *polnes پدید آمده است. هر دو معنایی که نورایی آورده درست است. کلاین نیز هر دو را ذیل ریشهٔ هندواروپایی *pel- «گرد، آرد» می‌آورد، در کنار یونانی pálē و póltos و سنسکریت pálalam. اتیمآنلاین محتاط‌تر است و پیوند pulvis و pollen را «شاید» می‌داند، ولی هیچ منبعی ریشهٔ دیگری برای آن‌ها پیشنهاد نکرده است. ادعای نورایی درست است.\",\n          \"sources\": [EO_POWDER, EO_POLLEN],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. pel-1 'Dust, flour': '1. Latin pollen, fine flour, dust: POLLEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. [Pok. 2 b. pel- 802.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 802 (POK_full.txt lines 65903-65942)\", \"stance\": \"supports\", \"note\": \"'with u-formants: Latin pulvis, -eris \\\"dust, powder\\\" (*polui-; inflection after cinis) ... with l-formants: Latin pollen, -inis \\\"very fine flour, dust powder\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 60\", \"stance\": \"supports\", \"note\": \"'Mit u-Formans: lat. pulvis, -eris \\\"Staub\\\" (*polui-; Flexion nach cinis; nicht nach Brugmann IF. 17, 488 zu apr. pelwo \\\"Spreu\\\")'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. pollen (line 29410)\", \"stance\": \"supports\", \"note\": \"'L., also pollis, \\\"fine flour, milldust\\\", fr. I.-E. base *pel-, \\\"dust, porridge made of meal\\\", whence also pollenta, polenta ... pulvis, \\\"dust\\\"'.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com s.v. pollen, powder\", \"stance\": \"partial\", \"note\": \"pollen: related to polenta and 'probably' to Gk. poltos, Skt. palalam, 'the ultimate origin is uncertain'; powder: 'Latin pulvis ... perhaps is related to Latin pollen \\\"mill dust; fine flour\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"French\",\n          \"words\": \"poudre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French poudre 'dust, powder' continues the Latin accusative pulverem: Vulgar Latin *púlv're loses the intertonic vowel, the resulting -lvr- cluster takes an epenthetic -d- (pulv're > pol-d-re, attested in Old French poldre, 11th c.), and preconsonantal l vocalises to u, giving pouldre and modern poudre. Klein s.v. powder gives the whole chain: 'OF. poldre, p(o)udre (F. poudre), fr. L. pulverem, acc. of pulvis'. The chart's gloss 'dust, powder' is exactly the French range; the gunpowder sense (poudre à canon) is a 14th-century specialisation that matters for node #4.\",\n          \"derivation_fa\": \"واژهٔ فرانسویِ poudre «گرد، پودر» دنبالهٔ حالت مفعولیِ لاتینی pulverem است: در لاتینی عامیانه واکهٔ میانی می‌افتد (*púlv're)، سپس در خوشهٔ -lvr- واجِ میانجی d پدید می‌آید (فرانسهٔ کهن poldre، سدهٔ یازدهم)، و آنگاه l پیش از همخوان به u بدل می‌شود: pouldre > poudre. کلاین همین زنجیره را آورده است. معنی «گرد و پودر» که در نمودار آمده درست است؛ معنی «باروت» (poudre à canon) تخصیص معنایی سدهٔ چهاردهم است و در گرهٔ شمارهٔ ۴ اهمیت می‌یابد. ادعای نورایی درست است.\",\n          \"sources\": [EO_POWDER, AHD_POWDER],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1024\", \"status\": \"partial\", \"note\": \"p. 1024 of the 1975/76 AHD New College Edition is the main-dictionary page carrying POWDER; that edition is not open online, so the printed page could not be read. The current AHD online entry for powder was checked instead and gives exactly what the arrow needs: '[Middle English poudre, from Old French, from Latin pulvis, pulver-.]' (ahdictionary.com/word/search.html?q=powder).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. powder (KLN_1966.txt line 29872)\", \"stance\": \"supports\", \"note\": \"'powder, n. — ME. poudre, fr. OF. (= F.) poudre, fr. OF. poldre, p(o)udre (F. poudre), fr. L. pulverem, acc. of pulvis, \\\"dust, powder\\\". See pollen'.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com s.v. powder\", \"stance\": \"supports\", \"note\": \"'Old French poudre (11c. pouldre) ... from Latin pulverem (nominative pulvis) \\\"dust, powder\\\"', with Sp. polvo, It. polve as parallels.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"poŭdr «پودر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP پودر pudr is a modern loan straight from French poudre, taken in with the French-mediated pharmaceutical and cosmetic vocabulary of late Qajar and Pahlavi Iran (the same layer as پماد pomād, کرم kerem, ماتیک mātik). French -dre is rendered as a final -dr cluster with no epenthesis, whence pudr. Moʿin's entry gives the range faithfully: «پودر (ا.) گرد، غبار. باروت (عم.) گرد سفید و معطری که به چهره مالند» — 'dust; (in common use) gunpowder; the scented white powder applied to the face'. The word is absent from Borhān-e Qāṭeʿ (1062/1652), as expected of a 19th/20th-century Europeanism. The native equivalent is گرد gard.\",\n          \"derivation_fa\": \"«پودر» وام‌واژه‌ای نو است که یکراست از فرانسهٔ poudre گرفته شده و همراه با لایهٔ واژگان دارویی و آرایشیِ فرانسوی در اواخر دورهٔ قاجار و در دورهٔ پهلوی وارد فارسی شده است (مانند «پماد»، «کرم»، «ماتیک»). خوشهٔ پایانی -dre فرانسوی بی هیچ واکهٔ میانجی به -dr بدل شده است. معین نیز آن را چنین آورده: «پودر (ا.) گرد، غبار. باروت (عم.) گرد سفید و معطری که به چهره مالند». این واژه در برهان قاطع (۱۰۶۲ ق) نیست، چنان‌که از یک وام‌واژهٔ اروپاییِ سدهٔ نوزدهم/بیستم انتظار می‌رود. برابر فارسیِ آن «گرد» است. ادعای نورایی درست است.\",\n          \"sources\": [WIKT_PUDR],\n          \"ref_check\": [\n            {\"ref\": \"MON:827\", \"status\": \"partial\", \"note\": \"Moʿin, Farhang-e Fārsi s.v. پودر located in MON_part1.txt line 33019: «پودر: (ا.) گرد، غبار. باروت (عم.) گرد سفید و معطری که به چهره مالند» — the word and the gloss 'powder' are there, but the OCR has lost the Latin-script headword transcription and Moʿin's bracketed origin tag [فر.], and the text file carries no printed page numbers, so 'p. 827' itself could not be verified.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. پودر\", \"stance\": \"supports\", \"note\": \"'Borrowed from French poudre', gloss 'powder' (e.g. پودرِ لباس‌شویی 'washing powder'), with the native synonym گرد.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Moʿin (BQT_v1_pages.txt, grep پودر)\", \"stance\": \"silent\", \"note\": \"no پودر headword — a 17th-century Persian dictionary naturally has no French loan of this kind.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep پودر)\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary of Persian has no entry for پودر.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Turkish\",\n          \"words\": \"\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The box is deliberately empty in the printed chart: it is the Turkish way-station through which Nourai routes French poudre to Persian bārut, i.e. Ottoman Turkish باروت barut 'gunpowder'. His two references do say so. Moʿin's footnote at Borhān 216 (citing Nafisi) reads «بارود در عربی نیز مستعمل است مأخوذ از کلمهٔ ترکی باروت و آن از poudre فرانسه (بمعنی غبار و مادهٔ مشتعلهٔ مخصوص) مأخوذ است»; and Tobia al-ʿUnaysi's Tafsīr al-alfāẓ al-dākhila s.v. بارود: «ترك «باروت» وهو مأخوذ من poudre الافرنسية أي غبار وقد أطلقوه على الغبار الناري ومنه البارودة». But this is a 19th/20th-century guess that modern work reverses. Wiktionary derives Ottoman Turkish باروت and Persian باروت alike from Arabic بارود bārūd 'saltpetre, gunpowder', and Encyclopaedia Iranica's article BĀRŪT states that the word 'is a loanword from Arabic; it passed from Turkish into Persian usage'. Arabic bārūd for saltpetre/gunpowder is already current in the Mamluk military literature (Ḥasan al-Rammāḥ, c. 1280), generations before French poudre could have reached Ottoman Turkish, so the French source is an anachronism; the Arabic word's own origin is unsettled (Arabic barūd 'powdery collyrium'; Medieval Greek πύρωτον, from πυρίτης λίθος 'firestone'; or an Armenian վառօդ intermediary). The Turkish node itself is real and the Turkish>Persian step is right, but the arrow that feeds it is wrong.\",\n          \"derivation_fa\": \"این قاب در کتاب عمداً تهی است: ایستگاه ترکی است که نورایی از راه آن poudre فرانسوی را به «باروت» فارسی می‌رساند، یعنی ترکی عثمانی باروت. هر دو مأخذ او همین را می‌گویند: معین در حاشیهٔ برهان ص ۲۱۶ به نقل از نفیسی می‌نویسد «بارود در عربی نیز مستعمل است مأخوذ از کلمهٔ ترکی باروت و آن از poudre فرانسه ... مأخوذ است»، و طوبیا العنیسی نیز در «تفسیر الألفاظ الدخیلة» ذیل بارود همین را آورده است. اما پژوهش امروزی جهت را وارونه می‌کند: ویکی‌واژه ترکی عثمانی «باروت» و فارسی «باروت» را هر دو وام‌گرفته از عربی «بارود» می‌داند و دانشنامهٔ ایرانیکا نیز می‌نویسد که این واژه وام‌واژه‌ای از عربی است و از راه ترکی به فارسی رسیده است. واژهٔ عربی «بارود» به معنی شوره و باروت در نوشته‌های نظامی مملوکی (حسن الرمّاح، حدود ۱۲۸۰ م) رایج بوده، یعنی نسل‌ها پیش از آنکه poudre فرانسوی به ترکی عثمانی برسد؛ پس سرچشمهٔ فرانسوی نابهنگام است. خاستگاه خودِ واژهٔ عربی هم روشن نیست (عربی «برود»، یونانی میانهٔ πύρωτον از πυρίτης λίθος «سنگ آتش»، یا میانجی ارمنی). پیوند ترکی←فارسی درست است، اما پیکانی که به این قاب می‌رسد نادرست است.\",\n          \"sources\": [WIKT_BARUT, WIKT_BARUD],\n          \"ref_check\": [\n            {\"ref\": \"BQT:216\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, printed p. ٢١٦ (archive.org borhan-ghate-v1 leaf n436; page image and transcript saved to data/verification/sources/refs/ocr/BQT/216.png and 216.vision.txt). Moʿin's footnote 4: «بارود در عربی نیز مستعمل است مأخوذ از کلمهٔ ترکی باروت و آن از poudre فرانسه (بمعنی غبار و مادهٔ مشتعلهٔ مخصوص) مأخوذ است «نفیسی»» — Nourai's French > Turkish > Persian/Arabic chain verbatim, on Saʿid Nafisi's authority.\"},\n            {\"ref\": \"TAD:6\", \"status\": \"supports\", \"note\": \"Tobia al-ʿUnaysi, Tafsīr al-alfāẓ al-dākhila fī al-lugha al-ʿarabiyya, s.v. بارود (TAD_pages.txt form-feed leaf 9, line 320; the leaf offset of 4-6 puts it at printed pp. 5-6, i.e. Nourai's 'TAD:6'): «بارود - ترك «باروت» وهو مأخوذ من poudre الافرنسية أى غبار وقد أطلقوه على الغبار الناري ومنه البارودة يقذف منها الرصاص والخردق» — the same claim, and probably Moʿin's/Nafisi's own source.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. باروت and بارود\", \"stance\": \"contradicts\", \"note\": \"باروت: Ottoman Turkish 'Borrowed from Arabic بَارُود (bārūd, \\\"saltpetre; gunpowder\\\")' and Persian 'Borrowed from Arabic بارود (bārūd)'; بارود itself is 'not Classical Arabic', of uncertain origin — Arabic برود 'powdery collyrium', or Medieval Greek πύρωτον < πυρίτης λίθος 'stone of fire', or via Armenian վառօդ. No French etymon is mentioned anywhere.\"},\n            {\"src\": \"Iranica\", \"where\": \"Encyclopaedia Iranica, article BĀRŪT (iranicaonline.org; the article body returned HTTP 403 to the fetcher, only its title/summary line was readable)\", \"stance\": \"contradicts\", \"note\": \"The article's own opening statement is 'BĀRŪT (also bārūt and bārūd), gunpowder, is a loanword from Arabic; it passed from Turkish into Persian usage' — Turkish as the transmitter, Arabic as the source, not French.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (LKT.txt, grep 'barud', 'barut', 'Pulver')\", \"stance\": \"silent\", \"note\": \"Lokotsch has no barut/bārūd headword; the 'Pulver' hits are all in unrelated entries (harmala, hazna, henna, kuḥl, rahǧ al-ġār).\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (PLA_pages.txt, grep 'barud')\", \"stance\": \"silent\", \"note\": \"no entry — Asbaghi does not treat bārūd as a Persian loan in Arabic, consistent with a non-Iranian origin.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"bârŭt «باروت»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"NP باروت bārut 'gunpowder' did enter Persian from Ottoman Turkish barut — Encyclopaedia Iranica: the word 'passed from Turkish into Persian usage' — and the doublet بارود bārud, with Arabic د, sits beside it; Borhān-e Qāṭeʿ (1062/1652) has both, the main entry running «بارود ... بر وزن و بمعنی باروت باشد که داروی تفنگ است، و بلغت سریانی شوره را گویند که جزو اعظم باروت باشد و آنرا نمک چینی هم گویند» and the cross-reference «باروت ـ رک: بارود». So the Turkish > Persian step of the chart is correct, and Nourai's gloss 'gun powder' is right. What is wrong is the ultimate source: modern scholarship takes Turkish barut from Arabic bārūd 'saltpetre, gunpowder', attested in Arabic pyrotechnic and military writing from the 13th century, not from French poudre; Borhān itself calls the word Syriac rather than European. Note also that Persian bārut is a homonymic doublet of the recent French loan pudr (node #3) only on Moʿin's/Nafisi's theory — if the Arabic derivation is right, the two Persian words are unrelated.\",\n          \"derivation_fa\": \"«باروت» در فارسی از ترکی عثمانیِ barut گرفته شده — ایرانیکا نیز همین را می‌گوید — و گونهٔ «بارود» با دالِ عربی در کنار آن جای دارد. برهان قاطع (۱۰۶۲ ق) هر دو را دارد: «بارود ... بر وزن و بمعنی باروت باشد که داروی تفنگ است، و بلغت سریانی شوره را گویند که جزو اعظم باروت باشد و آن را نمک چینی هم گویند»، و در جای دیگر «باروت ـ رک: بارود». پس گام ترکی←فارسی درست است و معنی «باروت» هم درست. آنچه نادرست است سرچشمهٔ نهایی است: پژوهش امروزی barut ترکی را از عربی «بارود» می‌گیرد که از سدهٔ سیزدهم میلادی در نوشته‌های آتش‌بازی و نظامی عربی به کار رفته است، نه از poudre فرانسوی؛ خودِ برهان نیز این واژه را سریانی می‌خواند نه اروپایی. افزون بر این، «باروت» تنها بر پایهٔ نظر نفیسی و معین دوگانهٔ «پودر» (گرهٔ ۳) است؛ اگر اشتقاق عربی درست باشد، این دو واژه هیچ پیوندی با هم ندارند.\",\n          \"sources\": [WIKT_BARUT, WIKT_BARUD],\n          \"ref_check\": [\n            {\"ref\": \"BQT:216\", \"status\": \"supports\", \"note\": \"Same page as node #4 (printed p. ٢١٦, leaf n436, image saved). The main entry «بارود بادال - بر وزن و بمعنی باروت باشد که داروی تفنگ است ...» plus the cross-reference «باروت ـ رک: بارود», and Moʿin's footnote 4 giving the French > Turkish > Arabic/Persian derivation on Nafisi's authority. Nourai's own reference does back his arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. باروت (Persian section) and بارود (Arabic)\", \"stance\": \"contradicts\", \"note\": \"Persian باروت 'Borrowed from Arabic بارود (bārūd)'; the Arabic word is of uncertain, non-French origin (Arabic برود, Medieval Greek πύρωτον, or Armenian վառօդ).\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, main text of p. 216\", \"stance\": \"partial\", \"note\": \"«و بلغت سریانی شوره را گویند که جزو اعظم باروت باشد» — Borhān's own compiler calls the word Syriac and equates it with saltpetre, which is the Arabic/Near-Eastern tradition, not a European one; only Moʿin's modern footnote brings in French.\"},\n            {\"src\": \"TAD\", \"where\": \"al-ʿUnaysi s.v. بارود (TAD_pages.txt leaf 9)\", \"stance\": \"supports\", \"note\": \"supports Nourai ('ترك «باروت» وهو مأخوذ من poudre الافرنسية'), but al-ʿUnaysi is precisely the 1932 source from which the French theory descends.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM_pages.txt, grep بارود/باروت)\", \"stance\": \"silent\", \"note\": \"no entry — Addi Shir does not treat bārūd as a Persian word arabised.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"powder, pulverize\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"powder < ME poudre (13c.) < OF poudre < Lat. pulverem, acc. of pulvis — Klein s.v. powder, Etymonline s.v. powder; the chart's French routing is exactly right. pulverize is a learned formation of the same family, also French-mediated: Middle French pulvériser < Late Latin pulverizāre 'to reduce to dust', from pulvis, pulveris (Klein s.v. pulverize), so hanging it on the French node rather than directly on Latin is defensible, though the Late Latin verb is the immediate base. Watkins lists both English words together under pel-1 'Dust, flour' via Latin pulvis.\",\n          \"derivation_fa\": \"واژهٔ powder از انگلیسی میانهٔ poudre (سدهٔ سیزدهم) و آن از فرانسهٔ کهن poudre و آن از حالت مفعولی لاتینی pulverem است؛ پس مسیر فرانسویِ نمودار دقیقاً درست است. واژهٔ pulverize نیز ساختی عالمانه از همان خانواده و باز با میانجی فرانسوی است: فرانسهٔ میانهٔ pulvériser از لاتینی متأخر pulverizāre «به گرد تبدیل کردن» از pulvis. بنابراین قرار دادن آن ذیل قاب فرانسوی پذیرفتنی است، هرچند پایهٔ بی‌واسطهٔ آن فعل لاتینی متأخر است. واتکینز هر دو واژه را با هم ذیل pel-1 «گرد، آرد» و از راه pulvis لاتینی آورده است. ادعای نورایی درست است.\",\n          \"sources\": [EO_POWDER, AHD_POWDER],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. pel-1 'Dust, flour': '2. Latin pulvis, dust: POWDER, PULVERIZE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. powder (line 29872) and pulverize (line 30983)\", \"stance\": \"supports\", \"note\": \"'powder, n. — ME. poudre, fr. OF. (= F.) poudre ... fr. L. pulverem'; 'pulverize, tr. v. ... — MF. (= F.) pulvériser, fr. Late L. pulverizare, fr. L. pulvis, gen. -eris, \\\"dust\\\". See pollen and cp. powder.'\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com s.v. powder\", \"stance\": \"supports\", \"note\": \"'Old French poudre (11c. pouldre) ... from Latin pulverem (nominative pulvis) \\\"dust, powder\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"pollen\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English pollen is the Latin word taken over unchanged: first in the sense 'fine flour' (1520s), then as the botanical term after Linnaeus used pollen for the fertilising dust of flowers in 1751. Because it is a direct Latinism and not a French loan, Nourai is right to hang it on the Latin node rather than on poudre — the chart distinguishes the learned and the popular transmission of the same root correctly. Klein s.v. pollen: 'L., also pollis, \\\"fine flour, milldust\\\", fr. I.-E. base *pel-'.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی pollen همان واژهٔ لاتینی است که بی‌تغییر وام گرفته شده: نخست به معنی «آرد نرم» (دههٔ ۱۵۲۰ م) و سپس همچون اصطلاح گیاه‌شناسی پس از آنکه لینه در ۱۷۵۱ آن را برای گَردهٔ گل به کار برد. چون این واژه وامی مستقیم از لاتینی است و نه از فرانسه، نورایی به‌درستی آن را به قاب لاتینی بسته است نه به poudre؛ یعنی نمودار به‌درستی میان انتقال عالمانه و انتقال مردمیِ یک ریشه فرق گذاشته است. کلاین نیز آن را «از لاتینی pollen/pollis از ریشهٔ هندواروپایی *pel-» می‌داند. ادعای نورایی درست است.\",\n          \"sources\": [EO_POLLEN],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. pel-1 'Dust, flour': '1. Latin pollen, fine flour, dust: POLLEN.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. pollen (KLN_1966.txt line 29410)\", \"stance\": \"supports\", \"note\": \"'pollen, n., the fertilizing male element of flowers. — L., also pollis, \\\"fine flour, milldust\\\", fr. I.-E. base *pel-, \\\"dust, porridge made of meal\\\"'.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com s.v. pollen\", \"stance\": \"supports\", \"note\": \"'from Latin pollen \\\"mill dust; fine flour\\\"' — English sense 'fine flour' 1520s, botanical sense from Linnaeus 1751; ultimate origin of the Latin word 'uncertain'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-390.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-390.py"
}
```


### [2026-09-14T01:08:07.322Z] TOOL RESULT

```
ok
```


## [2026-09-14T01:08:09.674Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-390.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 390"
}
```


### [2026-09-14T01:08:10.928Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 3, 'confirmed': 7, 'disputed': 3}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'not_found': 1, 'supports': 11, 'partial': 3}
books consulted: {'supports': 17, 'partial': 9, 'contradicts': 8, 'silent': 10} | by book: {'KLN': 6, 'Wiktionary': 5, 'Etymonline': 5, 'WLD': 4, 'HRN': 3, 'BQT': 3, 'POK': 3, 'PHD': 2, 'NYB': 2, 'ARY': 2, 'BRT': 1, 'IEC': 1, 'HUB': 1, 'LAT': 1, 'Iranica': 1, 'LKT': 1, 'PLA': 1, 'TAD': 1, 'AFM': 1}
```


## [2026-09-14T01:08:30.614Z] AGENT

Page 390 verified. `verify_check.py 390` reports 13/13 nodes, 0 PROBLEM lines.

**Verdicts** — roots: 1 confirmed, 1 plausible. Nodes: 7 confirmed, 3 plausible, 3 disputed. Ref checks: 11 supports, 3 partial, 1 not_found.

**Disputed**
- *Pel 2/Porkwos* #3 **pârsâ پارسا** — Mann (IEC 977) really does list "Per. pārsā 'chaste, pious'" under his *porkʷuos 'bright, pure', so Nourai's ref backs him; but Horn (no. 309 n. 2) says flatly "Pārsā bedeutet überhaupt nicht 'enthaltsam' … es bezeichnet gewiss eigentlich den Pärsen", and Wiktionary calls the origin uncertain, unattested in Middle Persian, normally linked to MP *Pārs* "Persia".
- *Pel 3* #4 **Turkish (empty box) ← French poudre** — both cited refs support the French route (Moʿin's BQT 216 footnote quoting Nafisi; al-ʿUnaysi TAD s.v. بارود), but Iranica and Wiktionary derive Turkish *barut* from Arabic *bārūd*, current in Mamluk military writing c. 1280, long before French *poudre* could reach Ottoman Turkish.
- *Pel 3* #5 **bârŭt باروت** — same reason; the Turkish→Persian step is right, the ultimate French source is not. Borhān itself calls the word Syriac.

**Plausible (with a structural error worth noting)**
- Root box *Pel 2, Porkwos* merges Pokorny's *pel-6 "grey, pale" (804-805) with Mann's private reconstruction *porkʷuos "bright, clean, pure" (977-978); no other handbook fuses them.
- #1 **pouruša, parya** — *pouruša-* is solid (Bartholomae col. 903); *parya* is not an attested Avestan word but Bartholomae's starred OP \**pariya-* "former, prior", printed without asterisk and with the wrong gloss.
- #5/#6 **falcô / falcon** — even Pokorny and Watkins make Late Latin *falcō* a loan **from** Germanic \**falkōn-*, so it cannot stand as a Latin descendant of the root; Klein, Ernout-Meillet and Etymonline prefer *falx* "sickle" altogether.

**Wrong page citation (book's error, not the extraction's):** node #1 cites POK:807; Pokorny p. 807 has *pelpo-*/*pen-* — the Avestan *pouruša* material is on 804-805, the page the root box already cites.

**Extraction errors: none.** I rendered PDF p. 390 and the JSON matches the printed chart exactly (root box split into two lines "Pel 2 : pale, gray" / "Porkwos : bright, clean, pure", empty Turkish box, `parŭsah`, `pallěre`, `falcô`, `poŭdr`, `bârŭt` all faithful).

Two Borhān page images were read and saved for audit: `data/verification/sources/refs/ocr/BQT/216.png|.vision.txt` (Moʿin's bārūd footnote) and `436.png|.vision.txt` (Moʿin's pīr footnote). 11 web pages archived via `fetch_source.py`.
