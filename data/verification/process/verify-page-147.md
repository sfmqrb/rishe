# Verification process log — verify-page-147


## [2026-09-05T20:08:42.379Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 147 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-147.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-147.json. Write /home/sfmqrb/git/rishe/data/verification/page-147.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 147` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:08:43.741Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:08:44.396Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:08:44.407Z] TOOL RESULT

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


## [2026-09-05T20:08:44.961Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-147.txt"
}
```


### [2026-09-05T20:08:44.977Z] TOOL RESULT

```
1	=== PDF page 147 (book page 117) ===
2	--- entry 0 ---
3	ROOT E -> redirect to I 2
4	--- entry 1 ---
5	ROOT Ebhi -> redirect to Ambhi
6	--- entry 2 ---
7	ROOT [Indo-European] Ed : to eat  (refs POK:287)
8	#1 (parent #0) [Avestan] refs=POK:287; BQT:44,1624 | adâiti : to eat ; asa 1 : food ; xarka-asa : eating bird ☞Ker 3
9	  #2 (parent #1) [Persian] refs=BQT:2099 | âš «آش» : a kind of soup ; nâštâ «ناشتا» : not eaten ; karkas «کرکس» : vulture
10	  #3 (parent #1) [Avestan] refs=BQT:119 | aspa-asa : horse food ☞Ekwos
11	    #4 (parent #3) [Pahlavi] refs=BQT:119,1624 | aspast, aspasti : alfalfa
12	      #5 (parent #4) [Persian] refs=BQT:119 | aspast «اسپست (سپست)» : alfalfa
13	      #6 (parent #4) [Syriac] refs=BQT:119 | pespesta
14	        #7 (parent #6) [Arabic] refs=None | al-fesfeseh : alfalfa
15	          #8 (parent #7) [Persian] refs=BQT:1624 | fesfeseh «فسفسه ، فصفصه» : alfalfa
16	          #9 (parent #7) [Spanish] refs=None | 
17	            #10 (parent #9) [English] refs=AHD | alfalfa
18	  #11 (parent #1) [Sogdian] refs=SOD:70 | `šp`dy : food, dish
19	#12 (parent #0) [Germanic] refs=AHD | it-an : to eat ; tanth-uz, tunth-sk : eater (tooth, tusk)
20	  #13 (parent #12) [English] refs=AHD | eat, etch ; tooth, tusk
21	#14 (parent #0) [Latin] refs=AHD | ed-ere : to eat ; dent : tooth
22	  #15 (parent #14) [English] refs=None | edible ; dental, denture
23	
```


## [2026-09-05T20:08:48.693Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-147.json",
 "description": "Read page 147 source JSON"
}
```


### [2026-09-05T20:08:48.731Z] TOOL RESULT

```
{
  "pdf_page": 147,
  "book_page": 117,
  "entries": [
    {
      "root": {
        "name": "E",
        "redirect": "I 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ebhi",
        "redirect": "Ambhi"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ed",
        "lang": "Indo-European",
        "refs": "POK:287",
        "gloss": "to eat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:287; BQT:44,1624",
          "words": [
            {
              "translit": "adâiti",
              "gloss": "to eat",
              "script": null
            },
            {
              "translit": "asa 1",
              "gloss": "food",
              "script": null
            },
            {
              "translit": "xarka-asa",
              "gloss": "eating bird",
              "script": null,
              "see": [
                "Ker 3"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2099",
          "words": [
            {
              "translit": "âš",
              "gloss": "a kind of soup",
              "script": "آش"
            },
            {
              "translit": "nâštâ",
              "gloss": "not eaten",
              "script": "ناشتا"
            },
            {
              "translit": "karkas",
              "gloss": "vulture",
              "script": "کرکس"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Avestan",
          "refs": "BQT:119",
          "words": [
            {
              "translit": "aspa-asa",
              "gloss": "horse food",
              "script": null,
              "see": [
                "Ekwos"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "BQT:119,1624",
          "words": [
            {
              "translit": "aspast, aspasti",
              "gloss": "alfalfa",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:119",
          "words": [
            {
              "translit": "aspast",
              "gloss": "alfalfa",
              "script": "اسپست (سپست)"
            }
          ],
          "note": null,
          "quote": {
            "text": "سنبل و سوسن کجا آمد بدست از روضه ای - کاندرو تخم سپست و سیر و سیسنبر برند",
            "poet": "Sanâî"
          }
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "Syriac",
          "refs": "BQT:119",
          "words": [
            {
              "translit": "pespesta",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {
              "translit": "al-fesfeseh",
              "gloss": "alfalfa",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "BQT:1624",
          "words": [
            {
              "translit": "fesfeseh",
              "gloss": "alfalfa",
              "script": "فسفسه ، فصفصه"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "Spanish",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "alfalfa",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:70",
          "words": [
            {
              "translit": "`šp`dy",
              "gloss": "food, dish",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "it-an",
              "gloss": "to eat",
              "script": null
            },
            {
              "translit": "tanth-uz, tunth-sk",
              "gloss": "eater (tooth, tusk)",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "eat, etch",
              "gloss": null,
              "script": null
            },
            {
              "translit": "tooth, tusk",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "ed-ere",
              "gloss": "to eat",
              "script": null
            },
            {
              "translit": "dent",
              "gloss": "tooth",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "edible",
              "gloss": null,
              "script": null
            },
            {
              "translit": "dental, denture",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:08:48.877Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:08:48.921Z] TOOL RESULT

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


## [2026-09-05T20:10:07.052Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','SOD','AHD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:800])\n\""
}
```


## [2026-09-05T20:10:07.161Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,80p' data/verification/page-127.json"
}
```


### [2026-09-05T20:10:09.150Z] TOOL RESULT

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
page-146.json
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
----
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<lea
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/82307409
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/
```


### [2026-09-05T20:10:09.195Z] TOOL RESULT

```
{
 "pdf_page": 127,
 "book_page": 97,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Dhem",
   "verdict": "confirmed",
   "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
   "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
   "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
   "sources": [
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
   ],
   "ref_check": [
    {
     "ref": "POK:247",
     "status": "supports",
     "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
     "stance": "supports",
     "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
     "stance": "supports",
     "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
     "stance": "silent",
     "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
    },
    {
     "src": "IEC",
     "where": "Mann, d-section (grep 'dhem' in IEC.txt)",
     "stance": "silent",
     "note": "Mann has dhen- (2) 'forehead', dhenguhó, dhinió etc. but no *dhem- 'blow, smoke' headword."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan",
     "words": "dam; da-dhmainya",
     "verdict": "plausible",
     "derivation": "The Avestan language has no attested finite verb dam- 'to blow': Bartholomae, Altiranisches Wörterbuch 731 f., knows only the Young-Avestan present participle daδmainiia- 'sich aufblasend, -blähend', said of (tree-)frogs at Vd. 14.5 and 18.73, which he analyses as 'ein Praes. auf -ainya- mit Inl.-Red.' and compares directly with 'ai. dhámati \"er bläst\", np. damīdan \"blasen\"'. Nourai's 'da-dhmainya' is that very word in his own transcription — he writes Avestan δ as dh and marks off the reduplication syllable da- with a hyphen — so the form is faithful; but his gloss 'I inflate, breathe' is wrong: it is an adjective/participle 'puffing itself up', not a 1sg verb. 'dam' is the root abstracted from that participle, i.e. Proto-Iranian *damH- 'to blow, breathe; to swell' (Cheung 2007 s.v. *damH³), which is real and is the ancestor of the Persian words in node 2; it is simply not an Avestan word-form. Hence plausible rather than confirmed: right root, misdescribed gloss, and one of the two 'words' is a root citation.",
     "derivation_fa": "در اوستا هیچ فعلِ صرف‌شدهٔ dam- «دمیدن» به‌جا نمانده است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۷۳۱ به بعد) تنها اسمِ فاعلِ جوان‌اوستاییِ daδmainiia- «باد کرده، خود را باد کننده» را می‌آورد که دربارهٔ قورباغه‌ها به کار رفته (وندیداد ۱۴٫۵ و ۱۸٫۷۳) و آن را ستاکِ حالِ پسوندِ -ainya- با تکرارِ درونی می‌داند و مستقیماً با «dhámati سنسکریت» و «دمیدنِ فارسی» می‌سنجد. صورتِ «da-dhmainya» در کتاب نورایی همان واژه است (او ذالِ اوستایی را dh می‌نویسد و هجای تکرارِ da- را با خط تیره جدا می‌کند)، پس خوانشِ کتاب درست است؛ اما معنایی که به آن داده («من می‌دمم») نادرست است، چون این صورت صفت/اسمِ فاعل است نه فعلِ اول‌شخص. «dam» هم واژهٔ اوستایی نیست بلکه ریشهٔ ایرانیِ باستانِ *damH- «دمیدن، باد کردن» است (چونگ، ذیل *damH³). بنابراین ریشه درست است ولی معنا و صورت‌بندیِ گره با احتیاط پذیرفتنی است.",
     "sources": [
      "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86"
     ],
     "ref_check": [
      {
       "ref": "POK:247",
       "status": "supports",
       "note": "IEW 247 (POK_01.txt line 3517): 'av. daδmainya- ,sich aufblasend, blähend, von Fröschen''  — the same Avestan form under the same root."
      }
     ],
     "consulted": [
      {
       "src": "BRT",
       "where": "Altiran. Wb. 731 f., s.v. daδmainya- (BRT.txt line 13362)",
       "stance": "partial",
       "note": "'j. däSmainya- Adj. \"sich aufblasend, -blähend\", von Fröschen … Eig. PPA. … — Vgl. ai. dhámati \"er bläst\", np. damidan \"blasen\"' — supports the root and the link to Persian, but shows the form is a participle, not '1sg I inflate'; and Bartholomae has no Avestan verb entry dam- 'to blow' (his dam- entries are 'Haus, Wohnung' and a present stem of dar- 'to hold')."
      },
      {
       "src": "CHEUNG",
       "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
       "stance": "supports",
       "note": "'*AVESTAN: Y Av. daδmainiia- \"blowing up (intr.)\" (V 14.5, V 18.73)' listed as the only Avestan reflex of *damH³."
```


## [2026-09-05T20:10:15.442Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ed-\\|ed-\\s*,essen\\|,essen\" POK_01.txt | head -30",
 "description": "Grep Pokorny for ed- root"
}
```


### [2026-09-05T20:10:15.513Z] TOOL RESULT

```
2604:Über  ddvvT]  (meist  PL),  äol.  kdvvag  Akk.  PI.  ,Schmerz',  ddvväv  ,Schmer3j verursachen,    betrüben'   s.  unter   ed-  ,essen';    vielleicht   hierher   davY.og d-gaavg  (,hitzig')  Hes.
4121:cd-  ,essen';  ursprüngl.  athematisch,  aber  meist  thematisch  geworden;  Nomi- nalformen:  ed-ono-,  ed-men-,  ed-uenl-u^  , Essen,  Speise';  Partiz. Perf.  Pass.  edto- (:'),  edio-  ,eßbar,  Speise';  edo-,  edä,  ,Speise';  edont-, dont-,  dnt-  ,Zahn*.
4135:hitt.  et-  ,essen*,  Imper.  e-it  (et),  1.  Sg.  Präs.  e-it-mi  (etmi),  3.  PI.  a-da-ai^l (adanzi)]  das  erste  a  durch  Assimilation?,  s.  Friedrich  IF.  41,  371;  ande^%^ Pedersen  Hitt.  128;      ^  ^
4145:ed-to-:  in  lit.  estas  , gegessen',  apr.  Subst.  Dat.  Sg.  istai  , Essen',  mbg. jasto  , Portion  Speise',  usw.
4151:.ii.  ddman-  n.  , Speise*  (:  eöiievai)]  -advan-  ,essend*;
```


## [2026-09-05T20:10:15.893Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ed-\\|To eat\\|ed-\\. To eat\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for ed-"
}
```


### [2026-09-05T20:10:15.945Z] TOOL RESULT

```
417:ed-. To eat; original meaning “‘to bite.” See dent-. 1. Ger- manic *etan in: a. Old English etan, to eat: EAT; b. Old High German ezzen, to feed on, eat: ETCH; c. Middle Dutch eten, to eat: orT; d. Germanic compound “fra- etan, to eat up (*fra-, completely; see per’), in Old English fretan, to devour: FRET). 2. Latin edere, to eat: EDACIOUS, EDIBLE, ESCAROLE, ESCULENT, ESURIENT; COMEDO, COMESTIBLE, OBESE. 3. Zero-grade form *d- in Latin compound prandium (< *pram-d-ium), “first meal,” lunch (*pram-, first; see per’): PRANDIAL. 4. Suf- fixed form *ed-un-d in Greek oduné, pain (< “gnawing care”); ANODYNE. [Pok. ed- 287.]
1044:s(w)eks. Six. I. Form *seks. 1. Germanic *seks in Old English s(iJex, six, six: sIx. 2. Latin sex (> Italian sei), six: SENARY, SEX-; SEICENTO, SEMESTER. 3. Suffixed form *seks-to- in Latin sextus, sixth: SESTET, SESTINA, SEXT, SEXTAN, SEXTANT, SEXTILE; SEXTODECIMO. II. Form *sweks in Greek hex, six: HEXA-, HEXAD. [Pok. sueks 1044.] swel-', To eat, drink. 1. Perhaps Germanic *swil- in Old English swilian, to wash out, gargle: swILL, 2. Extended form *swelk- in Germanic *swelgan, *swelhan in Old English swelgan, to swallow: SWALLOW!; GROUNDSEL!. 3. Iranian *khvdra- (attested in Avestan), to eat, in the probable source of Greek mantikhdras, manticore (see mer-?). [Pok. 1. suel(k)- 1045.] swel-2, To shine, burn. 1. Extended form *sweld- in Germanic *swiltan in Old English sweltan, to die, perish (perhaps < “be overcome with heat”): (SULTRY), SWEL- TER. 2. O-grade form *swol- in Germanic *swal- in Old Norse svalr, cool (< “lukewarm” < “hot”), akin to the Scandinavian source of Middle English swale, shade, shady place: SWALE. [Pok. 2. swel- 1045.]
```


## [2026-09-05T20:10:23.557Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^dent-\\.\\|dent-\\. Tooth\" AHD_watkins1985.txt | head; echo ====; grep -n \"dent-\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-05T20:10:23.627Z] TOOL RESULT

```
Exit code 1
364:LOIN. 4. Possibly suffixed variant *dlo-gho- in Greek dolikhos, long: DOLICHOCEPHALIC, DOLICHOCRANIAL. [Pok. 5. del- 196.] del-2. To recount, count. 1. Germanic *taljan in Old English tellan, to count, recount: TELL. 2. Germanic *tal6é in: a. Old English talu, story: TALE; b. Middle Dutch dle, speech, language: TAAL. 3. Old English denominative talian, to tell, relate, probably akin to the source of Middle English talken, to talk: TALK. 4. Per- haps Greek dolos, ruse, snare: DOLERITE. [Pok. 1. del- 193.] del-3. To split, carve, cut. 1. Suffixed form *del-to- in Germanic *teldam, “thing spread out,” in Old English teld, awning, tent: TILT?. 2. Germanic extended form *telg- in Old English telgor, telgra, twig, branch: TILLER’. 3. Perhaps o-grade form *dol-é- in Latin dolére, to suffer (? < “to be beaten”): DOLE?, DOLOR; CONDOLE, INDO- LENT. 4. Suffixed o-grade form *dold-dhraé in Latin dolabra, a heavy chopping tool (< doldre, to chisel, hew): DOLABRIFORM. [Pok. 3. del- 194.] del-*. To drip. Perhaps suffixed (stative) o-grade form *dol- in Germanic *talgaz in Middle Low German falg, talch, tallow (< “dripping fat”), perhaps akin to the source of Middle English talow, tallow: TALLOw. [Pok. 4. del- 196.] deme-'. Also dem-. House, household. 1. Suffixed re- duced o-grade form *dom-o-, dom-u-, house, in: a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJOR- DOMO; b. suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady): DAME, DAN?, DANGER, DoM, DOMAIN, DOMI- NATE, DOMINICAL, DOMINIE, DOMINION, DOMINO}, (DOM- INO2), DUENNA, DUNGEON; (MADAM), MADAME, MADEMOISELLE, MADONNA, PREDOMINATE. 2. Com- pound *dems-pot-, “house-master” (*-pot-, powerful; see poti-), in Greek despotés, master, lord: DESPOT. 3. Root form *dem()-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber, building material, lumber: TIMBER; b. Germanic *tumfté in Old Norse topt, homestead: Torr. [Pok. dem- 198.] deme-2. To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *doma- in Latin domdre, to tame, sub- due: DAUNT; INDOMITABLE. 3. Zero-grade form *dmo- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (dema-), doma- 199.] denk-. To bite. 1. Germanic *tanhuz in Old English toh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting, akin to the Scandinavian source of Middle English tonge, tange, point, tang: TANG!. 4, Germanic *teng- in Old High German zinko, spike, prong: z1Nc. [Pok. denk- 201.) dens-'. To use mental force. Reduplicated and suffixed zero-grade form *di-dns-sko- in Greek didaskein, to teach: pipactic. [Pok. 1. dens- 201.] dens-2. Dense, thick. 1. Suffixed form *dens-o- or *dns-o- in Latin dénsus, thick: DENSE; CONDENSE. 2. Suffixed zero-grade form *dns-u- in Greek dasus, hairy, shaggy: DASYURE. [Pok. 2. dens- 202.] dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dné- perhaps in Germanic *tunth-sk- in Old English tisc, tix, canine tooth: TUSK. 3. Full-grade form *dent- in Latin déns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE; (BIDEN- TATE), DANDELION, EDENTATE, INDENT!, (INDENTURE), TRIDENT. 4. O-grade variant form *(o)dont- in Greek odén, odous, tooth: -ODON, -ODONT, ODONTO-; CERATO- Dus. [In Pok. ed- 287.] deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek
(eval):1: === not found
```


## [2026-09-05T20:10:23.760Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==296' POK_01.txt | head -70"
}
```


### [2026-09-05T20:10:25.560Z] TOOL RESULT

```
 av.  ?/ö,  gr.  b'g,  rj,  d  ,welcher',  phryg.  log  (vi)  ,wer  immer', slav.  *ia-  in  i-ze,  L  ja-ze  usw.,  halt.  u.  slav.  in  der  Bestimmtheitsform  des Adjektivs,  z.  B.  lit.  geräs-is,  apr.  pirmaiin-ien,  -in^  aksl.  dohry-jh  (s.  Ber- neker 416 f.,  Trautniann  105 f.).  Zweifelhaftes  (lit.  jeT  ,wenn',  got.  jabai ,wenn')  s.  bei  Brugmann  IP  2,  347  f.  (Lit.);  Keltisches  bei  Pedersen  KG.  II 235,  Thurneysen  Gr.  323,  doch  kann  cymr.  a  nicht  dazu  gehören.
Komparativ  ai.  yatard-^  av.  yatära-,  gr.  (kret.  gort.)  bxeQoq  ,welcher  von beiden';  vgl.  ai.  yävatj  gr.  £wg,  dor.  äg  (*ciJ=og)  ,solange  als',  ai.  yäd  ,inso- fern,  wie'  ==  gr.  wg  ,wie';  s.  Schwyzer  Gr.  Gr.  I  528,  614 f.
C.  Partikeln  und  Adverbia:
Über  die  adnominale  und  ad  verbale  Partikel  ^,  o  s.  oben  S.  280  f.
e-,  e-  Augment  (,*dann,  damals')  ai.  a-  (auch  ä-,  z.  B.  ä-vYnak),  av.  a-, arm.  e-  (z.  B.  e-lik  =  e-XiTre),  gr.  I-  (auch  ^-,  z.  B.  hom.  '^SsiSr}).
e-  in  ai.  asäu  ,jener'  (neben  av.  hau),  a  ddh  ,jenes;  dort',  a-dyäj  a-dyd jheute'  (Stammkompositum?),  d-ha  .sicher,  ja';
arm.  e-t'e  (neben  t'e)  ,'daß,  wenn';
gr.  i-yd-eg,  i-ytsl,  e-y.eXiog  (nehen  v-slvog) ;
osk.  e-tantOy  umbr.  e-tantu  ,tanta',  osk.  päl.  e-co  ,hic',  osk.  exo-  (*e-ke-so) ,hic';
aksl.  (j)e-se  ,ecce'  (neben  se  ds.),  aruss.  ose,  russ.  e-to  ,da,  dahier',  e-tot ,der  hier,  dieser'  (neben  tot  ,jener') ;  serb.  bulg.  e-to  ,da'  (usw.,  s.  Berneker 259f.);
284
unsicherer  got.  i-haif  i-ba  Fragepartikel,  ahd.  ibu,  ola,  as.  anord.  ef  q^c und  ,wenn^,  ^S^-  9^/^  engl,  if  ds. ;
über  *eno-  in  gr.  evt]  usw.  siehe  besonderes  Stichwort.
Zu  e-  auch  die  Komparativbildung  av.  atära-  , dieser,  der  von  beideu' ds.,  alb.  jdt{e)re  , anderer',  umbr.  etro-  , anderer^,  lat.  in  ceterus  ,der  andern oder  übrige',  aksl.  eterh,  jetei-b  ,irgendwer',  PL  jeteri(ji)  ,einige',  nsorl> lüötery.
ed  (Nom.  Akk.  Sg.  n.):   über  lat.  ecce,  med  s.  oben;  av.  at  zur  Hervor- hebung des  vorhergehenden  Wortes  (wie  ü,  s.  unten ;  Bartholomae  Altiran Wb.  67);  wohl  auch  in  aksl.  jed-im,  -tm  , einer'  als  ,*gerade,  nur  einer*» ob   auch   ksl.  jede,   kyjb  ,quidam'   aus   gedoppeltem   *ed-ed   oder   nach  id^^ im  Ausgang  gerichtetem  *ed?  (Berneker  261,  bestritten  von  Brückner  KZ. 45,  302,  vgl.  Meillet  Slave  comm.«  444.)  *
ed  und  öd  (Abi.):  ai.  ät  , darauf;  und;  (im  Nachsatz)  so*,  av.  äat  , darauf dann;  und;  aber;-  denn*,    ostlit.  2   ,und  aber'    (aksl.  i  ,und'   ist  eher  *ei\1? lit.  o  ,und,  aber'  =  aksl.  a  ,aber'.  ***
ei  (Lok.):  gr.  sl  ,*so,  wenn'  (sl-ra  ,dann',  eT-d^s  , möchte  doch!',  iTt-sl (vgl.  el.  iTC-T^)  ,da*,  l/r-fitra;  daneben  dial.  ai,  Lok.  des  f.  St.  a,  und  ^  2i Instr.
```


## [2026-09-05T20:10:30.172Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=4121{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line 4121:\", n}' POK_01.txt; echo ====; awk 'BEGIN{RS=\"\\f\"} NR==299' POK_01.txt | sed -n '1,60p'"
}
```


### [2026-09-05T20:10:31.936Z] TOOL RESULT

```
Exit code 1
formfeeds before line 4121: 299
(eval):1: === not found
```


## [2026-09-05T20:10:34.148Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==300{print}' POK_01.txt | sed -n '1,60p'"
}
```


### [2026-09-05T20:10:35.819Z] TOOL RESULT

```
  Lauten  nach  teil- weise Nachfolger  von  idg.  obhi  (s.  unter  epi);
^ot.  bi,  ahd.  usw.  bi,  bi  ,auf  —  hin  (got.),  in  Beziehung  auf,  über*  mit Akk.;  .an,  bei'  mit  Dat.  (Lok.),  auch  mit  Instr.,  Präfix  ,be-'.,  s.  auch  unter ainbhi,  oben  S.  34,  das  im  Auslaut  dasselbe  Element  enthält;
aksl.  obh,  ob^  als  Präverb  ,um-,  be-'  in  obhstojati  oder  ob^-stojat^  , um- ringen', in  Kompositis,  wie  obhdo  n.  ,Scharz',  in  Ableitungen,  wie  obbHh, russ.-ksl.  obh^b  ,gemeinsam'  {*obhi-t{o-);  verstärkte  Form  obi-  im  russ - ksl.  obichoditi  , umhergehen';  die  Form  o,  ob  enthält  altes  *op-  (lit.  ap), s.  unter  efi.
\VP.  I  124,  Trautmann  1,  Meillet  Slave  comm.^  155  f.
cd-  ,essen';  ursprüngl.  athematisch,  aber  meist  thematisch  geworden;  Nomi- nalformen:  ed-ono-,  ed-men-,  ed-uenl-u^  , Essen,  Speise';  Partiz. Perf.  Pass.  edto- (:'),  edio-  ,eßbar,  Speise';  edo-,  edä,  ,Speise';  edont-, dont-,  dnt-  ,Zahn*.
Ai.  athera.  Präs.  1.  Sg.  dd-mi,  3.  Sg.  dt-ti  ,ißt',  Perf.  ädimd  (:  lat.  edimus, got.  etum)]  themat.  im  Medium  ada-sva]
av.  3.  Sg.  Konj.  adäiti]
arm.  ntem  ,esse*,  themat.  (*ö<i-);
gr.  hom.  Infin.  sS^evaL,  Fut.  (alter  Konj.)  eö-0-f.iai,  Imper.  ursprüngl. *h^i  (:  ai.  addhi),  danach  sekundär  Icr^/w  (go-^w)  ,esse';  sekundär themat.  edio  (nach  Partiz.  ädovr-  und  der  danach  aufgekommenen  3.  PL edova),  Perf.   hom.  iö-rjd-cjg,  eörjdoraL  (nach  nsTto-Tai),  att.  fidiJJoxa;
lat.  edö,  es,  est  usw.  , essen'  (Länge  des  e  entweder  alt  oder  nach  der  sog. Lachmannschen  Regel  zu  erklären;  ob  alt  im  Partiz.  esus  und  Supinum 6S(6-)wm?);   Perf.  edl-^  osk.  Infin.  edum,  über  umbr.  ezariaf  s.  unten  S.  288;
air.  Konj.  cini  estar  , obgleich  er  nicht  ißt'  {*ed-stro),  Fut.  iss-  {*i-ed-s-), Perf.  do  füaid  (*de-ti(p)o-od-e),  Partiz.  esse  , gegessen'  (*ed-tio-)]  cymr.  ys ,ißt'  {*ed-ti);
got.  themat.  itan  (Perf.  1,  PI.  etum,  ahd.  äzum  usw.:  alat.  edimus),  anord. 6ta^  as,  ags.-  etan,  engl,  eat,  afries.  Ua,  ahd.  ezzan  , essen'  (=  ai.  ddanam , Futter',  ^v.  ädavov  , Speise');  mit  Präfix  fra-  (*pro-):  got.  fra-itan  , auf- zehren', ags.  fretan  ,nagen',  ahd.  frezzan  , fressen';  kaus.  got.  fra-atjari] anord.  etia  »verzehren  lassen*,  ags.  ettan  ,grasen  lassen',  ahd.  azzen^  ezzen
288
,zu    essen    geben,   abweiden   lassen*,    nhd.    ätzen,    eigentlich   ,eine  scharf Flüssigkeit  sich  einfressen  lassen';
bsl.  *ed-mi  in :
lit.  edu,  edziau,  hti  (alt.  ^[c^Jr/ii,  3.  Sg.  ht)  , essen,  fressen',  Supin.  tatn. lett.  ^mu  (älter  *e^
```


## [2026-09-05T20:10:41.963Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"adaiti\\|adäiti\\|adāiti\\|ad-\\s*.*essen\" BRT.txt | head -20"
}
```


### [2026-09-05T20:10:42.010Z] TOOL RESULT

```
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
8751:Lebenskraft'^':  hyat  astvant»m  (sd.)  dada 'tatum  y.j/.  ij;  —  tal  ii  .  .  vairim  ast- rwV?  (sd.)  'tänäi''''  data  Y.^j.,^.  14;  —  at rätqm  zara'^uÜrö  tanvascti  x^ahya  'tattpm dadaiti  paurvatätpm\.33.i^;  —  f^ra  vS rahl  .  .  tanvasclt  c^'ahyS  'tatum  V.  //.  18; /_9.4;  — darsyö.xia'irpm  xsa'^raAe  dury/ö.- jUim  'tilnahe  A.  1.8]  Y.  17. 19;  —  m-^irpswa slün'i  gayehe  mprpzu^a (sd.)  xa  'tänahe  Yt. JO.  7 1 ;  —  avai  he  astt  masyö  ar^i^pm  yat \  'tatum  bttnjayüt  (sd.)  V.  7.  7 1 ;  —  ava \  apamm  (sd.)  gayehe  *frasatu>m  'tanahe  Yt.
12290:ai.  TgL  tüfnadaiti/lra-  Adj.,  mm  V.  äaJa/i 'beissl';  s.  tiädifiura:  —  *difslra-  statt  'dqSlra- nobl  in  Anletuiang  an  einen  KS.  *äSdqi 'schaifiälmig'  aus  •flSin/-  {al  iüä-dan),^  »gl. danlan-  und  tilidälä;  daitika-.  —  Npü.:  rti dan^n.
12648:(sva.  da&vah'):    urva^pm  staotär^m  van- hatikam  (sd.)  '%B  aoxta  ahurS  mazda    Y. 10.  9, Zum   V.   da-;    red,  Bildung;    vgl.   Wii.   Gr.' S  114S.  4.  —  ai.  'dada-,  'dadha-  Adj.  —  Pü. : ausgelassen;  Sü.  (zu  V.):  adadäm. j.  ddiaöis  Vyt.  $0:  lies  ditöii;  i.  'dä(y); g.  dadaiti,  dada/,  daduyi  usw.,  Verbalf. :    s.
19581:•  j.  ^mad-  V.  'zumessen'.    x-Aor,  i  mas-. 'zumessen,  zuteilen':  asakya  ysm  (sd.)
23731:Y.J5.  8;  —  in  Dualverb,  damit;  yesi  tat frajasst   antan    sairi  (sd.)    °zänt    V.  75. 17.        I  o)  imAp,  'cittä3>,  Stadt':  tatäna' namt^    -danam   Bh. /.  19;  2.3,  6,  12,  16, 3. 1,  4,  6,  8.  II         c)  in  sozialem  Sinn,  im Gegensatz  zu  Adel  und  Priesterschaft  als  Be- zeichnung des  dritten  Standes  (Sp.  908  m.) : k}  airyamä  ks  a^agtus'  (sd.)  .  .  anha^  yS *z!f!Ji   var^uAim   dal  frasastxm   Y.  45. 7 ; verwendet    YLp.  26,    wo    vansansi;    — aSyäcä    i^altus  yäsat    akyJ    'iSn>m    mal aityanmS  . .  uruätimn  (sd.)  mazäa  Y.32. 1 ; —  yi  ..yazai(Sp.i2jJ  ü.)  apa  i^aasu^ca tarSmaütm  'sinahy3cä  nazäistam  *ärußm airyamanasiä    nadtnts  (sd.)    "der    ich   .  . von  dir  . .  fernhalten  will  und  vom  Adel ,  .  und  von  der  Gemeinde  die  Drug  der Nachbarschaft   und   vom  Sodalen  . ."  Y, 33-  4;   —    "^^   x'attsi  aha   'gsnä   aha *hax3mam  (sd.)  Ryat  yaU  hiscamatdl    Y. 4/0- i,\    —    paifl    ifaSJus    airyamanasä dadaiti  {Sp.  J 20  m.)    nsii  mä  xsnaui  yä 'tSnä   (NSf.)     '"hSca    nalda     dahyius    ySi SOitärB  (sd.)  ". .  nicht  stellt  die  Gemeinde mich  zufrieden  . .  noch  . ,"  Y.  4S.  i "'. KompA.,  E.;   Abieil.  (s.  auch  ^vanzäna-).  — aX    v/y'äna-   n.   'geschlossene   Miederluiung;  > Dorfschaft;  oppidum'«),  np.  iarie»  'Quartier' i (wom  GliPh.  /b.  91);  vgL  vätü«  (s.  Pü.)  'zur Gemeinde  gehörig'!).    —    PO.:   verschieden; 1)  ..  V.  IS-   'T-  -urMn;   -   ..  V.  34.  H iSl.;  ie   pa  gäti  i  as  varzHn,  eri.:  väitryii;  \ —  ru  y.  4g.  7:   iet  i  vartiin  vch  da)üt  fräi\ vävattkänih;  —  lu  Y.  J./.  14  iSt!  varilket, ; Sü.:  viählyali!\  -  -  a)  lu  Y.  J5.  8:  fa  ahräiih  \ välüittA,    Sü.!    dharmasya    svapanttySm;    — zu  Y.  32.  1:  välünih,    Sü.!  niafanktitä;  — lu    Y.  3J.  4:    välünän,    ex\.:    kamsjyaiäti-A Sfi.t  svapankRyä^;  —  va  Y.  46.  \:  väliinlkA erL  !  hamsSyak,    Sü.!  svatrfriayaA ;    -^     la  Y.  1 40,  4:  välün,  Sü. :  sv<^Aitayäti.    Vgl.  dazu  | Pü.    M    varsiäitö^liis-    und    zu    vfrninya:    — ' ij  Als  Fem.  nar  y.46.  1.     Die  Stelle  ist  nicht recht  sieber.  —  >)  iBed.  und  lEt.  vgl.  Bthl. BB.iC.aiS,  /5.57,Gdn.BB.  75.253,  VSi./.  rsi, 2.   18,  3.   171,  ZDMG.  51.  734,   t'ov  KZ.  34. 245,  3S-  24;  weitere  Litt.  ebd.   Man  beachte auch  Yt.  13.  33.    S.  noch  No.  4f.  —  3)  Aus laC  eivitäiem  heriorgegangen !  —  4)  Bed.  nach  ! PW.     GnN.  rechnet  bei   seiner  Deutung   des  ' Worts  -  s.  No.  2  -  nicht    mit   der   Möglich- keil,    dass   im    ai.  vfjina-   bis   zu   vier  idg. ; Wörter    zusammengefallen    sein    können;    s. ' DL.   iS^O.  S44-    —    i)  Aus  urir.  *garza-  sva, tvarizänn:     Die   angegebene    Bedeutung  er- ' schliesse  ich  aus  der  PüErl.  hamsäyak. •  g.  varazänya-  Adj,  'der  der  Gemeinde , (a£  drittem  Stand)  angehört',  im  Gegensatz ' zu    :^altav-    und    airyaman-:    yS    aläum\
```


## [2026-09-05T20:10:43.050Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aspasti\\|aspast\\|aspo-asti\\|aspāsti\\|Luzerne\" BRT.txt PHD.txt PHD_mackenzie.txt HRN.txt HUB.txt | head -30"
}
```


### [2026-09-05T20:10:43.104Z] TOOL RESULT

```
HUB.txt:4465:(oben p. 42) ; aspist {ispist, vspust) 'Luzerne = phi. aspast ;
PHD.txt:219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
PHD.txt:1258:clover aspast.
PHD.txt:2684:lucerne aspast.
PHD_mackenzie.txt:1228:aspast [,spst l I N .-...] clover, lucerne.
PHD_mackenzie.txt:6209:clover aspast.                              idan, hanJaftan.
PHD_mackenzie.txt:6994:limit kanarag, karan, saman, wim-        lucerne aspast.
PHD_mackenzie.txt:11601:aspast         \~~
HRN.txt:1127:79. esjnst, uspust, ispist 'Luzerne'.
HRN.txt:1128:phlv. aspast 'Luzerne'.
HRN.txt:10138:28. aspastän 'Pferdestall'; arm. LW. aspastan.
HRN.txt:15630:aspast 79.
HRN.txt:15631:aspastän 28.
BRT.txt:5885:ni.  ahoilhäna-  n.,  mp.  (Pü.)  fli/flj/J«,  ann.I.W. aspastan,  —  ')  rSt.  s.  unter  usIräjlSna-. j.  aspiii':  a.  unter  aspan-, j.  BspkrtxilS  N.  pff;  lies  asprinö.
```


## [2026-09-05T20:10:49.311Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1120,1140p' HRN.txt; echo ==== HUB ====; sed -n '4455,4480p' HUB.txt"
}
```


### [2026-09-05T20:10:49.355Z] TOOL RESULT

```
Exit code 1
ap. asa[hara' und np. es[^^r (No. 86) stützen sich
gegenseitig und scheinen eine Nebenform asa- zu be-
weisen. Arm. LW. aspet steht natürlich für '^asp{a)pet,
78. isper ud^ isperü, isferüd 'ein kleiner Vogel' (bei AM. 226
Zeile 11 neben dem Sperling genannt).
Nöldeke (mündliche Mitteilung) vergleicht deutsch
Sperling (siehe Kluge, s. v.).
79. esjnst, uspust, ispist 'Luzerne'.
phlv. aspast 'Luzerne'.
bei. LW. aspust (7).
Wörtlich 'Pferdefutter' von esp und [/'ad-, Nöldeke,
ZDMG. 32, 408, Kärnämak, 54 '). Bartholomae
macht mich auf die ganz ähnliche Bedeutung von got.
aihvatundi aufmerksam.
80. espend 'Raute', esfend, isfend, spend,
aw. spenta- heilig ; phlv. spand, arm. LW. spand
'Raute*.
Die Pflanze erhielt ihren Namen von der ihr
anhaftenden mythologischen Bedeutung (vergl. de
Lagarde, Ges. Abh. 173).
*) Vergl. auch DJD Jer. 9, 17 (Hörn, Ind. Forsch. II, 136).
(eval):1: === not found
```


## [2026-09-05T20:10:53.308Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4455,4475p' HUB.txt"
}
```


### [2026-09-05T20:10:53.348Z] TOOL RESULT

```
gegeben: arm. Xosroc -= pers. Xusrav; arm. xortakem *schlage
in Stiicke', np. xurdj xurda *klein, kleines Stiick*. Vgl. gr.
XoHQOTjg = pers. Xusrav ; XfO()aaiLua = ap. {h)uvarazmis, np.
x^'arazm; ^AguyMaia = ap. hara(h)uvatis etc.
§ 6. Ap. a wird zu i:
a) einigemal vor Zischlauten (s, z, s, z) und y sowie
nach den Palatalen 6 und /: atis Teuer (so immer bei Vullers)
fiir alteres atas (vgl. Horn Nr. 7), afgh. LW. atas, paz.
ataSy arm. LW. afas (Sebeos), phi. ataocs^ zd. atars; pisan-
jfidan = pasanjldan 'besprengt werden, aus "^pal-sinc-Uan
(oben p. 42) ; aspist {ispist, vspust) 'Luzerne = phi. aspast ;
pieman (pazmdn^ puzmdn) *bereuend* aus paseman; hizisk
*Arzt*, arm. hzisk (aus^hizisk iuv ^bisizk), skr. bhisdj- 'Arzt'
(unter Mitwii^kung des i der ersten Silbe); hiayar Viel* =
ap. ^vasi-ddra- zu bas Viel' = ap. vasiy (unter Mitwirkung
des folgenden y) ; dadistan 'Urtheir = paz. dadastan, u. s. w. ;
sassanid. Hormizd, arm. Ormizd^ ap. A(h)uramazdd; miyan
'Mitte* = paz. phi. miyan ^ zd. mai^yfina-; piyada 'Fuss-
ganger', skr. pafidti-; jigar *Leber, zd. yakare^ skr. yakri-;
paz. cihar Vier (np. cahar), zd. cadwaro; np. cihil Vierzig'
= paz. cihal^ cihil, zd. cadwaresatem\ ci^m (A. M.) = casni
```


## [2026-09-05T20:10:54.280Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kahrkāsa\\|kahrkasa\\|karkas\\|kahrkās\" BRT.txt HRN.txt HUB.txt | head -20"
}
```


### [2026-09-05T20:10:54.325Z] TOOL RESULT

```
HUB.txt:7541:vas = s\iv, vag Vollen'?); kargas 'Geier = zd. kahrkasa-;
HUB.txt:8530:--^ zd. vareka- ; kargas 'Geier = zd. kahrkasa- ; pargm re-
```


## [2026-09-05T20:11:03.550Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kahrkäsa\\|kahrkasa\\|kahrka-\\|Geier\" BRT.txt | head -20"
}
```


### [2026-09-05T20:11:03.604Z] TOOL RESULT

```
6554:frässigsten  unter  den  fleischfressenden  Ge- schöpfen des  heiligen  Geists  soll  man  den Leichnam  überantworten,  den  Geiern"  V, 3.  20.
9238:•  j.,  p.  ^kara-  Adj.  (fem,  VT"-)  'machend  'Geier'O,  al.  fytaivafav-  m.  'Hahn'.  —  Pü,: (usw.)'.  *'^*-  —  '*  ZDMG.  s6.  63  i  haplol.  auä  *iar-
9245:/p,  19; — ya~ia  VIS.,  yahmäi  nsitcahmäi  •   j,    kahrkäsa-   m,  'Geier':    '53  zannu-
9548:arjnm  mainyüm  /ramiUm  aspahe  'pa (IS.)  Yt;p.29;i¥.i8,zi,r4.9;  —  ahmli . . üjasat  vaztmnö  i'sri^raynS  uftrahe  'fa ■  Yt. /4- n;  P-J-i  —  nizbayemi  iistrtni  .  . \gius  'pa  Y.if}.3T,  Yt&i6,  74.7;  —  he I  'pa  varäzaie  Yt  ;^  1 5 ;  —  maiiahe  'pa  Yt |j4.23;  —  bUzahe  'pa  Yt  74.25;  —  yat dim  us;a  usdi'qnayat  .  .  '^raltaonS  m^?- yahe  -pa  kahrkäsahe  Yt.  J.  6 1 ;  —  m»rrjahe 'pa  vär^iiahe  Yt/4. 19,  /9.35;  —  zaf- nimnpitt  .  .  :^ar^n3  m^rjyahe  'pa  fra^usap Vt/'>.34.  Undeutlich:  ratufris  *n.liri- A-ayi  'pa  näij  payauhs  nSit  sun5  'pa payai?h5  ratufris  v>hrkaya  'pa'a  paya- uha^a  N.j()*',  [V,  7.  a:  lies  maxHJ!'^
16039:*)  Er  wird  von  Brattaoiia  In  die  Luft  geschleu- dert, wo  er  in  Geiergestalt  umherfliegt,  bevor er  wieder  zu  t einem  Haus  herabkommt.
19573:Leiche    den    Geiern     überani-wortet    werden.
20369:ai.  mfga-m.  'Waldtier'  (Gazelle),  auch'Vogel'; np.  murf  'Vogel;  Huhn'.  —  Pü. :  mun:  — ')  Nur  für  V,  J.  1  gesichert;  s.  Db».  VglS. /.  129.  —  »)  Wie  Adler,  Geier,  Hubn;  im Gegensatz  zu  iv^-.  ~-  J)  Im  Nebensatz  fehlt das  Verbum ,   etwa  ufia,'iyäya.
```


## [2026-09-05T20:11:06.218Z] TOOL CALL #19: Bash

```json
{
 "command": "pdftoppm -f 147 -l 147 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg147 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T20:11:08.664Z] TOOL RESULT

```
total 3272
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 16:11 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb 168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    395 Sep  5 16:10 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb  53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb 107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb  89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb  60631 Sep  5 16:11 pg147.png
```


## [2026-09-05T20:11:14.218Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg147.png"
}
```


### [2026-09-05T20:11:14.578Z] TOOL RESULT

```

```


## [2026-09-05T20:11:14.574Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:11:14.636Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9230,9250p' BRT.txt"
}
```


### [2026-09-05T20:11:14.677Z] TOOL RESULT

```
V.  sg.  4a.  als  Bezeichnung  des  Hahns,
•)  Im  Mp.  iar  m<>hU,    ein  mythischer  Fisch,  KompA. ;  Abicit.  —  np.  tart  'Huhn';  ai.  vgl.
der  grösste  und  Akt  Ralav  der  Fische;  vgl.  Bd.  krka'vAkav'  m.  'Hahn',
14.  II,  34.  13;  tS-  3.  zs.  M.  4-  ,  .   kahrka'tit-  f.  (gemeiner  oder  Spott-)
.]  'kara-m.EN.emesTuramers:.^.j^e^^  ^'^^^   ^^^  ^^^^^._  \           y^  j^/,jJl
alavazdä..yatbavämaa,tut.vanyädänavs  ^^^^  ^^^^      -^  „^^^^_^^  ^...  ^„.,,„,^„^^
/ara..'r>maasa6a„>mvar,m^a..\t5.n-  uas  (NS.)  nama  aojaiU  Y.iS.iS-
'^'8'  *'''''■'                                                               '  Eig.    ■Kikerlkitum'.    —    Vgl.   ZDg.    iarktiis
•  j.,  p.  ^kara-  Adj.  (fem,  VT"-)  'machend  'Geier'O,  al.  fytaivafav-  m.  'Hahn'.  —  Pü,: (usw.)'.  *'^*-  —  '*  ZDMG.  s6.  63  i  haplol.  auä  *iar-
KompE.  —  Zum  V.   >*ar-.  —  ai.  "/■aro-  Adj.        iaiJiäi-   'Hähnerresser',  vgl.  lu  ioArhlsa-.
(fem-  Vi-).  ^  j    kahrkana-  m.  Name  einer  gläubigen
•  j.  "narate  (sd.)  karaiain"  N.p;.  Familie:      hufraväxs     'kananqm      asaonS
•  j.  'karana-  m.  'Ende';  i)  räumlich:  "des  gläubigen  H.,  (aus  der  Familie)  der 'Grenze,  Rand;  Ufer;  Flügel  (des  Heeres)';  A'."  YL/j.ia?.
dalinsm   upa   '■Tum   airihä  ziiiHi  YtiO.99;'  Ableit.  aus  Va^rin-,— ai,  vgl.  :*/-.<'ai?a-m.  (eine
12.  ao;  —  «va  -iia'>  ai^hä  2?m9  Vt.  lO.  95;  '^^  Rebhul.n.  auch  als)  EN,
/p,  19; — ya~ia  VIS.,  yahmäi  nsitcahmäi  •   j,    kahrkäsa-   m,  'Geier':    '53  zannu-
nalmanqm  "na'^  pairi.vasnöiie  ". .  bei  dem  mainil  (sd.)    YL  i4-  33;    —    msrrjahe  . ,
nicht   Anfang    noch    Ende    zu    gewahren  -sähe    Yt,  5,  61;    —    as.^ar}limaabyS  .  .
sind"  YLi^,3;  —  upa yaozsnta  -na''  zraya  dämattam*k?r>fi.:^arqttt  k:-r?ß paiti  nisri-
vouru.kaSaya  "an  den  wogenden  Ufern . ,"  ttuyjl  vayqm  'sam  V.J.  20.
Vt.5.  38;    —     yaoZiflli    vUpe    °n3    (NP,)''         KompA.'—     I^omp.;     *ta/iria-\-*.lia;     eig.
```


## [2026-09-05T20:11:26.315Z] TOOL CALL #22: Bash

```json
{
 "command": "grep -rl \"kahrka\" data/extracted/batch/ | head; echo ====; grep -rho \"kahrka[a-z-]*\" data/extracted/batch/ | sort | uniq -c | head; echo ==== xarka; grep -rho \"xarka[a-z-]*\" data/extracted/batch/ | sort | uniq -c | head"
}
```


### [2026-09-05T20:11:26.383Z] TOOL RESULT

```
Exit code 1
data/extracted/batch/page-257.json
(eval):1: === not found
```


## [2026-09-05T20:11:26.935Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nb=d['BQT']\nfor k,v in b.items(): print(k,':',str(v)[:600])\n\""
}
```


### [2026-09-05T20:11:28.580Z] TOOL RESULT

```
title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
kind : archive_djvu+local_scan_ocr
url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1
lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh
local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/
page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (
covers_etymology : True
notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text file
scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmq
cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
```


## [2026-09-05T20:11:33.128Z] TOOL CALL #24: Bash

```json
{
 "command": "grep -o \"kahrka[^\\\"]*\" data/extracted/batch/page-257.json | head; echo ====; python3 -c \"\nimport json,glob,re\nfor f in glob.glob('data/extracted/batch/page-257.json'):\n    s=open(f).read()\nprint([l for l in open('data/verification/agent/charts/page-257.txt')][:40] if __import__('os').path.exists('data/verification/agent/charts/page-257.txt') else 'no chart')\n\""
}
```


## [2026-09-05T20:11:33.832Z] TOOL CALL #25: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:119 2>&1 | head -60"
}
```


### [2026-09-05T20:11:34.760Z] TOOL RESULT

```
Exit code 1
kahrkatât
(eval):1: === not found
```


### [2026-09-05T20:11:36.621Z] TOOL RESULT

```
no scan of BQT covers printed page 119 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:11:45.708Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"اسپست\\|سپست\\|اسپس\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-05T20:11:45.798Z] TOOL RESULT

```
21170:و نلم عیوه‌ای هم هت شبیه بسپستان » و بستی
```


## [2026-09-05T20:11:46.428Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آش\\b\" BQT_v1_pages.txt | head -5; echo ==== leaf for 44; awk 'BEGIN{RS=\"\\f\"} NR==255{print substr($0,1,1500)}' BQT_v1_pages.txt"
}
```


### [2026-09-05T20:11:48.273Z] TOOL RESULT

```
Exit code 1
152:گذشته ازهم نگسته‌وخویشاوندی[نها بپمدیگر پیدا و آشکار است .
248:فارسی سروسامانی عیدهد » خانه و آشیان؛ دیرین [نها را نمودارمیسازد مثلا
508:زبانبای بابلی و آشوری وا کدی بدست آورد . معادل بياری از آنپا در
560:-٩‏ در کتیبه‌های آشوردی ۵۱ اي م۸ (رك- گیر‌شمن.!یر ان
1085:بپلوی و بارسی اختلافات [نهارا آشکار میسازد ازقبیل آوردن فل مفرد
(eval):1: === not found
```


## [2026-09-05T20:11:53.318Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 328 329 330 331; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n{print substr($0,1,900)}' BQT_v1_pages.txt; done"
}
```


### [2026-09-05T20:11:55.098Z] TOOL RESULT

```
=== leaf 328 ===
ما
ارم » جح اول و سکون.تانی و میم »
بنتی فد باشد ‏
ارمل س بر وژن جدول » بمنی بسیار
وکثیرباشد. وصدا وآوازرا یز گومند - وبمعنی
همه و مجبوغ هم آمده است
از ناو با نون و واو بی وزن غرفاو .
نم ناحیه‌ایست از نواحی حمدان .
از ناوه ت شتح اول وواو» سعنی ازناو
است که ناحیهای باشد از نواحی همدان ‏
از فس « بر وزن مذحب . بمعتی رنجش
باشد که از رنجیدن است - و در عربی فربه را
کونند که ضد لاعی باشد .
ار نقش گلور خار دستن .
کتابه از خواری و بی اعتباری باشد .
از ود - باواو بروزنشبگرد » دوابی
است که آنرا بفارسی انده فوقو گویند و ب
=== leaf 329 ===
اراد
باشد ٩‏ - و کنابه از مردم شجاع و قهرآلود حم
هت - ورایت و سرعلم را نیز گوبند ۴ -
وپادشاه تال و ححاك ماراترا هم گفته‌اند ۴ .
ادها « با کاف‌معنی آخراژدهاست
که نحاك ماران باشد ۴ .
اژدهای فلك - اثارء بشدنین رأی
و ذنب است - و تلی‌را نیز گویندکه ازجلهة
چهل و حشت صورت فلك باشد ٩‏ .
ارم خح اول و سکون انی و غن
نقطه دار , شاخهابی را گویند که از درخت بریده
باشند و بعربی جلمه خوانند٩‏ .
ار کان با کاف‌بروزن دربان ؛ بمعتی
مردم کاهل و باطل و مهمل و بیکار باشد .
باگد شبکه دار که ازیس آن نگاه توان کرد .
۱
ظ
از گهی -باها �
=== leaf 330 ===
۱ <<
رومی است . 1 2 بکویتد و باشیر تازه
بیامیز ند وبرزیر خصه‌بمالند نموظ عجبآورد۱
اساسه بفتح نی رو اس :
بمعتی نگرستن بگوشة چشم ووایس دیدن‌باشد ۴
وبکی اول نیز گفته اند .
اسا لیطوس یکی لام و سکون
تحنالی وضم طای حطلید واو وسین می‌نقطهسا کن»
بیونانی گلی‌است کهآ نرا بعربی طی ىکرمی‌خواننده
و آن کلی باشد سیاه رنگه و آترا طین کرمی
از آنجیت گوبند که در اول میک بر آوردن
درخت انگور ازان گل بردرخت مالند تا کرمی
که ب رکه آبرا میخورد ب رکه آنرا نخورد
وچشمهای تا را نباه نکند . ۱
اسالیون - بکس لام و ضم تحتانی
وسکون و
=== leaf 331 ===
اسپخحول بکسر اول و سکون‌انی
و بای فارسی مکور و خای نقطه دار حضموم‌بواو
ولام زده » بععتی‌پیخال است که فضله وافکند گی
اسیر ۱ س با بای فارسی بر وزن مهتر»
سپررا گونند و بعریی جثه خوانند .
اسپر اثین )0 بابای فارسی» بروزن
وممنی اسفرائین باشد. وآن شهرست مشهور در
خراسان » و چون رسم و عادت مردم آنجا چنان
بوده که یوسته با سیر می‌بوده اند لهذا بدین‌نلم
موسوم شده است . #
اسب رد س یا بای فارسی و زای هوز
اسب رس « بفتح‌اول بروزن دستری:
(۱) چش : اسیرآئن .
۱ و
اراشی آهکی عمیق خوب میرو‌بد .
- ۱۸۱ « کل کلاب ۷۱ >.
روستامی ۱۸
```


## [2026-09-05T20:12:02.623Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 332 333; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n{print}' BQT_v1_pages.txt; done"
}
```


### [2026-09-05T20:12:04.144Z] TOOL RESULT

```
=== leaf 332 ===
فآ فا برگه زرد چوبه است -
ودرخت خربزه را نیز گوبند .
اسیر لو س « بالام وسین بی‌نقطه ووار
مجپول بروزن کشورسوز » خانه وسرای پادشاحان
و سلاطین و حکام را کوبند .
اسیر 8 - بکسر اول و فتح ثالث ورابم
و سکون ثانی و میم » بمعنی اول اسپرغم است
که مطلق کلها و رباحین باشد ۱ .
اسر ۵] لب « دارو های پآب‌جوشانیده
باشد که بدن بیمارانرا بدان پشویند و بعربی
نطول خوانند .
اسیر نگ » بر وزن ومعنی اسفریگه
است ؛ و آن شهرست ترديك سمرفند و مولد
سف لجاست .
اسپر ود - بکس اول و شم الث
ورابع و سکون ثالی و واو مجهول و زای هوز »
تلم کوهیست بسیار بلند و رفیم» و ختح ثالث‌هم
کفتفانن ۳
اسر هم ۴ ه باهای‌هوز, بروزن ومعنی
اول اسپرغم است که مطلق کلها و رباحین باشد.
آسپر ی « بر وزن‌مهتری » بمعنیپست
۱ رك : اسپرهم .
اسیغول
شده و معدوم کردیده وآخرشده وبنهایترسیده
باشد - وبمعنی تمام شدن وباأخر رسیدن ونیست
گردانیدن - وصور کردن عم آمده است .
اسیر یز فتح اون و سکون تحتانی
مجهول بر وزن رم خیز » بمعتیاسب ری‌است
که میدان و سا و عرصه باشد ۳ تس اول
مم آمده است ؟ .
اسب د لسي - باسین بی‌هطه » بروزن
۲
دوالیدن باشد6 ؛ وبکسر اول همهست وسین‌دوم
قطبدارهم ۳ است وبا کیش قافیه کرده اند .
اسیست ۱ ب بفتح اول و کسر الث
وسکون »نی وسن‌سفنص
وئای قرشت» صیست را
کوندو آن علفی است
خوانتد و سریی ضصفصه
و تخم آنرا بدرالرطبه
گویند . اسیت
اسپقول - بکسر اول وفتح الث» بزد
۹۰
۴ ب ورگ : اسپرجس-.
بیعنی راه » اسپریس ا: کلمات فارسی است که سین پهلوی بجا مانده ؛ اسپرس بتصریح مضر
اوسنا در زمان ساسانیان ونامةٌ پهلوی بندهش, میدان ناخت ونازاسب » بدرازای دوهزار کلم است.
د ذاب ۰ ۱ : ۲۷۵-۷۲6 > . ۱ - در اوستا ویارسی باسنان 254 - 25۳0 » ای کلم
م رکب لفظاً یمنی « اسب میخورد * , جزه اول همان اسب است وجزه دوم از مصدر 24 مطایق
0 لانینی و655650 آلمانی و 6۵ (10) انکلیسی است بمعنی خوردن ( چنانکه رد اوستابی
ربثة آراستن وراست فارسی است ) . درپپلوی نیز 25۳356 آعده » از زبان یپلوی داخل‌سربانی
وازسربانی بعربی‌رفته « فصفصه » (جمم. فصافص) شد. وازعربی دراسپانیابی وارد شده صورت‌الفلفه
8 هه اسپانیولیانآنرا بآمبکا بردند و درآن سرزمین نیز الفلفه خوانند . «بونجه (اسیست)
بقیه درصفحة ۱۲۰
=== leaf 333 ===
قطونا باشد ۷ » و معنی ت رکیبی آن گوش اسب ۱
است ۰ چه غول بدمنی کوش هم آعده است ؛
وجط یکونند چون ب رکه آن بگوش اسب‌شبه
و معنی اسفناج است »
و آن سبزی باش د که در
آش و هله کنند , سرفه
است‌بنابرین اسب‌غول خوانند و بضی بشپش‌تشبیه | دا نافع ات (,
کرده اند , و جتح اول هم درست است . اسینانج .
باجیم مر وزن اصفهانك »
بمعنی اسفناح ننک 5
سبزی آش باشد ۴ . اسیناخ ( اسپناج )
ا سید ه معروفاست و (۲) آن دانه‌ای
باشد که بجپت چشم زخم در آش ریزند ۵ .
اسیندار بمعنی شمح باشد که معشوق
اسیلفج « بنتم اول و م لام و سکون ‏
ثانی و ثالث و نون و جیم ۴ کیاهی است (۱)
دوابی که آنرا صفاهان شنك و در خراسان‌رش
یزخال دار و بعرمی لحیةالنیس خوانند . طبیعت
آن سرد و خشك است » خون بینی و جمم‌اعضا
ببندد و ربهای کهنه را نافم باشد و فرحه
اععارا سود دارد » و آذناب‌النیل همان است . 4
پروانه است - و نام پکشناسب هم هست ٩‏
اسناخ ۴ باخای نقطه دار 1 بروزن
-ء بودن لیراعظم باشد دربرج حوت و 5
(۱) چك : - است . (۲) چش : کد.
لِ - جهانگری بمعنی پبخال آورده ۰ دلیلی ندارد چه در قدیم توبن فرهتگها مانند
حلشة قرهنگه اسدی تخجواتی بمعنی بزرقطونا ضبط کر‌ده‌اند واين شمریهرامی را شاهد! وردماند:
هیجگاه نارم بخانه کرد مقام ازانکه خانه پراز اسیغول جانور است .
واسیخول در شمرمذ کور بی‌شك بمعنی ماس است . « لفت‌نامه > -
۴ حکیم مومن وصاحب مخزن‌الادوبه « املنج > آورده اند . « لفت‌نامه » .
؟ - بلت‌علمی 50102012 بانگلی 5۳18260 با 50101286, بفرانسه 60102۲05
با لمانی01024کوعربی اسفاناخ» وفارسی‌اسیناخ»اسیناج» اسینانج,اسپاناج.اسپانج» اسباناج» اسباناخ‌ودد
طبری اسینا «واژه نامه۲۸> حمه‌ازيك ربشه است. داودشرسر انطا کی‌درتذ کرخود گوید : اسفاناج
مرب عن‌فارسية هواسباناح * ۰ دربونانی 5۳1081108 « اختینگاس » وآن از تیر* اسفناجیان ؛
ودارای ربشة قرمز دنگ وب رگهای خوراکی و کلهای نرومادء آن جداست . « کل گلاب4 ۰*۲۷
ی فرحنگه روستایی ۱۸-۱۸۳ > . ۴ راد : اسیناج ۱ ۵ در اوستا ٩۳۵1۵‏
بمعتی مقدس < بارتولمه۱۹۱۹ > ۰ طبری 65۳021 « واژه‌نامه ۷۷ ۰۲ کیلکی ٩۳20-4202‏ ,
قظرسی نیز اسفند . 18۱98 112۲۳0812 این گیاء در اغل نفاط ابران خود روست . «فرهنگه
روستابی۱۸4 * . ۱ ره : اسیندبار. ۷ ر4: امیندارمة .
خبه از صفحة ۱۱4۹
پورداود . بقما ۲ : ۱۲ * پهلوی 25۳25 « اونوالا ۲۸۰ > .
۵ اسبله - با سیلی 212015 51۷0۲135 از ماهیان
استخواندار که بچةٌ ماهیان پربهارا میخورد واز همین نظر ماهی
مسیارمضری‌است وقسمت عمده زند گانیرا در کودالهای‌رودخانه‌ها
سرسبرد ۵ ددیای خزد 64۱۳۳ اسله
( برهان قاطع ۳۰ )
```


## [2026-09-05T20:12:26.772Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT']['scans'],ensure_ascii=False,indent=1)[:2500])\n\""
}
```


## [2026-09-05T20:12:28.036Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 253 254 255; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n{print substr($0,1,600)}' BQT_v1_pages.txt; done"
}
```


### [2026-09-05T20:12:28.861Z] TOOL RESULT

```
[
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
]
```


### [2026-09-05T20:12:30.624Z] TOOL RESULT

```
=== leaf 253 ===
آسمار با میم بروزن شاخار , ورخت ]| کهکثانرا کویند و بعربی مجره خوانند .
وود 1 کرت و مرش ان ا: آ سهان‌ور بسمان - این مثل ات
آیما .۱۰ ۳ زااد ب درجایی کون که شخصی درب رآبر معفول‌جواب
| سهان " ه ممررفت وبعربی سما وفلك ۱
نادرست (۱) گومد .
خوانند» ومعنی ترکیبی آن آسیا مانند است . : ِ
بابار گردیین چه آسیا را آی یز کوشد ۴- سها 4 » بروزن‌آسنانه» سقف خان
=== leaf 254 ===
اندلختن و عداوت بهمر‌سانبدن علق باو دارد .
ستستان » بکس تون بر وزن
کافرستای ؛ غلم پدر زن وامق ات و او عاقبت
بردست وامق کشته شد ۱ . 3
سو ده - بر وزن آلوده » بمعنی بی
زحمت و بی‌عزاحمت ومی‌مشقت باشد - و بمعنی
خقته و خوایده هم آمده است , #
آسه ۴ - پروژن کاسه »کدت و زرات
باشد - و زمینی را نی ز کون که مجهت زراعت
کردن عستمد و مهیاکرده باشند - و دوائ�
=== leaf 255 ===
است که موسی علیه‌اللام را پرورد . ۶
]شام - بائن .قطمدار بروزن بادام ؛
خوردن و آشامیدنکم و اندك را کویند و بعرمی
قوت لایموت خوانند ۴ - و بمعنی وشیدن
و آشامیندن آب و شراب و مانند آن باشد -
وامر بان هعنی هم حست عتی بیاشام و بنوش -
و آشامنده را نیز گوبند که فاعل آشامیدن
باشد ٩‏ - و ام ولایتی است مان مشرق وشمال
بنگاله و درآ ئولابت عود بفابت خوب
```


## [2026-09-05T20:12:34.951Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==254{print}' BQT_v1_pages.txt"
}
```


### [2026-09-05T20:12:36.948Z] TOOL RESULT

```
اندلختن و عداوت بهمر‌سانبدن علق باو دارد .
ستستان » بکس تون بر وزن
کافرستای ؛ غلم پدر زن وامق ات و او عاقبت
بردست وامق کشته شد ۱ . 3
سو ده - بر وزن آلوده » بمعنی بی
زحمت و بی‌عزاحمت ومی‌مشقت باشد - و بمعنی
خقته و خوایده هم آمده است , #
آسه ۴ - پروژن کاسه »کدت و زرات
باشد - و زمینی را نی ز کون که مجهت زراعت
کردن عستمد و مهیاکرده باشند - و دوائی حم
آسیا ۴ - متروف لت هو آن نکن
باشد مسطح و مدور بربالای سنگه دیگر که آب
و باد و آدمی و حیوان دیگر آبرا نگ اف -
و پسی گوبند آنچه باب کردد آسياکوند و
آنچه بدست کردانند یا چاروا گرداند آسیا
کات چذلسی ارد اف زان ند زا کیان
سین و سین راکسره دادنه آش آب شده بثا بر
آنکه در لغت فارسی حرف آخر مضاف مکور
می‌باشد و چون فارسیان الف ممدوده را دو الف
اعتبار میکنند و مقور است که هرکاء بر اول
۱ - فرمود شا آمشتان بگاه
آسیب
کلمه‌ای که مصدر بالف ممدوده باشد یکی از این
چهار حرف که بای زایده و بای لمر و میم نهی
و تون نفی باشد درآورند . يك الف داییا قلب
کرد الف دیگر را حال خودمی گذ ار یه »وچون
کلمة آی را بر آب افزوددد و يك الف آبرا ییا
قلب کردند آسیاب شد یس آسیای دست‌وآسای
باد گفتن صحیح نباشد ولهذا آسیکه بخ وکاو
کردانند خرالر و آفجه بدست کسردانند دست
آ ی کوند ۵ . وچون درقارسی واو بیاوبرعکس
تبدیل می‌بابد آسیاو گفتن صحیح باشد» و دراین
لفت با و واو هر دو بکثرت استعمال افتاده است
و بعربی «رحی» میگویند .
آ سیا ]رن » باالف حدوده وتح زای
فارسی و سکون نون . آلتی باش دکه آسبا را
بدان تیز کنند و بعربی «نقار» گویند .
آ سیاب بروزن ماعتاب » آسیا باشد
وآنرا آسیاو یز گوند ۱ . *
]سیا ز 4- بختح زای هوز و نرن »
بمعنی آژنه است که آلت آسیا تيززکردن باشد
] سیب ۷ - بکر ثالث وسکون تحتالی
و بای ابجد » مطلق آزار باشد - و آزاربرا نیز
تال (هول وفار) « واژه نلمه 4۵۵ > -
ح‌ آسور _ رل ۳ آخور.
آسیارا اداره کند . عاحان .رگ : لفت نامه
```


## [2026-09-05T20:12:45.368Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==255{print}' BQT_v1_pages.txt"
}
```


### [2026-09-05T20:12:47.147Z] TOOL RESULT

```
است که موسی علیه‌اللام را پرورد . ۶
]شام - بائن .قطمدار بروزن بادام ؛
خوردن و آشامیدنکم و اندك را کویند و بعرمی
قوت لایموت خوانند ۴ - و بمعنی وشیدن
و آشامیندن آب و شراب و مانند آن باشد -
وامر بان هعنی هم حست عتی بیاشام و بنوش -
و آشامنده را نیز گوبند که فاعل آشامیدن
باشد ٩‏ - و ام ولایتی است مان مشرق وشمال
بنگاله و درآ ئولابت عود بفابت خوب میشود
و آیرا نیز گویند که در وقت برنج پخته شدن
از آن کرند . *
] شب « بنتح ثاك سکون بای ابجده
موضعی است از نواحی» طالقان وسکون الت‌حم
کگفته‌اند .
آش بچگان ۱« جندیداستر است.
کویند که از پهلو به پهلو زدن و دوش بر دوش
خوردن و کوفنن ‏ وکوقه شدن بهم رسد و آترا
بمریی «صدمه» خوانند ۱ - وبمعنی آفت وتکیت
اسیم » بر وزن جاجیم . بلفت زند
وپازند (۱) اسناد بزر که مرنبه و عظیم‌الشان را
گومشد .
آ یمه - . هیم» بمعنی دیوانه مزاج
وشیفته و شوریده ومدهوش - ومضطرب وس رأسیمه
و متحیر وس گشته باشد- وبمعنی خیره همآمده
است که از خی رکی (۲) باشد .
] سیون « بر وزن آبگون ۴ » بمعنی
آسیمه است که س رکشته و حیران و شوریده -
ومدهوش و خیره باشد .
] سیه - بر وزن ناحیه » نام زن فرعون
, (۱) چك : ژند و پاژند. (۷) چپ ۲ » چش : چیز کی ا
٩‏ باسیب پا و بزانو و دست همی‌مردم افکند چون پیلست. عنصری «لفت‌نامه».
؟ - هیچ آسیب نبود اندرین روز کار بیتان تا آمدن طفرل . ۶ تاریخ میتان بنقل
ی نامه > _ که وان من انت::
کته عدقت کرد آسون مرا از چه روس گشته و آسیونم . متجيك. رك : «لغن‌نامه».
۴ - ماخون از فرهنگه جهانگیری که مه معنی فوت ( و هو مابقوم به پدن‌الانان من
الطمام . سراح) داده و از شاعری مجهول بنام اسناد مت ذیلرا شاهد آورده‌است :
پملك شام ندهم تار مومت ندارم گرچه گاء شام آشام . د لفت نامه »
همین معنی در فرهنگه دساتیر س ۲۳۱ آعده ۰ - نیز بمعنی نوشیدنی » مش وب
و رت است . ۰ ۵ درکلمات م رکب : خون‌آشام » دردی آشام » غمآدا؛» می آشلم .
رگ : لغت‌ناعه. ۱ -مرکب از آی + بچکان ( جمم بچه ) » جزء اول در اوستا 2510
بمعتی بپار ؛ فراوان « بارتوله ۲۲۹ » . پس کلمه بمعنی بپار بچه است . < از بادداشت های
اتع شرا سوت
۵ آش - در ساسکرت ۸5 همریقة 80 بمعتی خوردن و با 600 لانینی و ثفنهان
دیگر اقوام هند واروبایی مانند 658560 آلمانی و 62 1۵ انکلنتی ۲ دارد . ادن‌رشه
درچندکلمةٌ فارسی بجامانده : کر کس ,آش, ناثتا .آش اصلا بممنی مطلق خوری است وامروزه نام
غذای مخصوصی است . ولی کمة آشیز و آغیز خانه باد آور ممنی اسلی انست < فاب
1 : ۰۷۲۲۳ . آشامیدن مرک از: پیشوند 2 ولغت اوستائی 51021718 بمعنی
نوشیدنی ۰ جرعه «بارتولمه رب حآهپز _ طباخ ی ن آشپزخانه مطیج »
جای یختن غذا . رلك : آش .
```


## [2026-09-05T20:13:15.985Z] TOOL CALL #34: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1624 2>&1 | tail -60"
}
```


### [2026-09-05T20:13:23.847Z] TOOL RESULT

```
REF: BQT:1624  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 417  OCR-lang: fas

کر کس -۱۹۲۶-
گر کس ۱ » بر وزن ااطلس . مرغ کر کس رکش - بکر رابع .
مردار خوار رم تبرهابیراکویند که در ترکش گذارند » چه
باغدوییربی پم ود کرکن و تیر ام آند است.
نر کون( شور رس و / ۰ - شمرا۴ را کونند
و کنانه از گچوه ات چم و آن ام ثوابت .
تیرهم هست هگ کر کفیز ه با فا پروزن رستخیز؛بمهنی
که عبر بان دی کفگیر باشد وآن چمجداست سوراخ دارگ .
سهم خوانند کر کم » با کاف بر وزن مرهم » قوس
کر کی ۱ قرحرا کونند 8 و بمعنی زعفران هم آمده
کر سار ؟ با کاف فارسی بروزن | امت ‎٩‏ - و بعضی گوبند بیغ وری است و آن
شرمار » نام ولایتی است - وانام پپلوانی هم کیاهی باشد مانن د گیاه کنجد .
بوده تورانی و بهمن‌بن اسفندیار او را دستگیر کر کما یا سبامیم بروزن‌مر حباء پر نده‌ای
کرده و او بپمن را فریب داد ازراه هفت خوان | است دم دراز که بعرپی صه‌وه کونند .
که میآب وعلف بود بروبینه دز برد ۰ بهمن در کر کمان 4 بعّم‌اول بروزن‌تر کمان.
غضب شده او را ن ورد دوائی است که آنرا حندقوقی خوانند وبفارسی
کر کسان فلا - ادارء به نر طابر ۱ انده قوقو خوانند. برکلف مالند نافع باشد.
ونرواقع است که‌دوصورتند ازجملةٌ چپل وهشت کر کمیسه < بفتح اول و ثالث و میم
سورت فلك البروج . بتحتانی کشیده و سین بي‌نقطةٌ مفتوح ۰ نام کلی
۹ <«کرکی. اوستا - ۴210۳۴25۵ (کرکس) . پهلوی ۴۵۳۷2۵5 ۴27835 ۰
افغانی ع 8278285 . بلوچی ۴27822 ۰ استی 61۳88 ۸« اسشق ۸۶۹ >. کامهٌ اوستانی رکب
از دو جزء است : ۷211۳6۵ ( << کر که . مرغ )4 282 (خورنده) » جمماً نی مرغ‌خوار
* هرمزدنامه ص۱ > .کرکس (لاشخور ) پرنده ایست شکاری » بزر که وسنگین » باکردنی دراز.
خورا که وی از اجاد جانورانست . ۳ - صحیح « کر کار سم اول امت . رك:فهرمست
ولف . ۴ - منظور موْلف « شعری + 817109 است » ولی ظ . مراد از «کرکس فلك *
همان نر طابر است .
۴ - باری دارم چنانکه حلقة چشمش باشد از چشم کرکفیز فزوتش .
سوزنی سمرقندی «جهانگیری».
8 - فلك مرجامه‌ای را ماند ازرق مر اورا چون طرازی خوب کر کم :
بهرامی سرخی « لغت فرص ۶۳۵۰ ۰
‎٩‏ (عر ) « کر کم بالضم . زعفران ومصطکی > « منتهی‌الارب > . کرکم (عر ) <
4 (فر) . 1261100186 (فر). نامکر کم سامی‌است : آشوری 7 ۷۷۵7۴881 عبری
آرامی ۷۵۳۷۵۲۵ . این لفتها جمنی زعفران ( 9211۷8 ۱8ع070 ) است» ولی
بعدها بمعتی داروبی هندی 1078 ۲۱701132 با زعفران هندی گرفته شده . رك: عقار ۰۵ ف.
۷ -قن :کر کرك. ۸ - « حندقوقی . هوالنفل و الذرق والحایور و العرقصان » و بقال له
اساً حباقا . وهوالکر کمان » واسمه بعجمیةالاندلر‌طربیله » «عقار ۱۶۷ * ورك : ایا ۱۶۷ ف .
```


## [2026-09-05T20:13:47.098Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"فصفصه\\|فسفسه\" BQT_v3_pages.txt | head -20"
}
```


### [2026-09-05T20:13:47.184Z] TOOL RESULT

```
20490:فسفسه - بفتح هردو فا بروزن ‎sey‏
```


## [2026-09-05T20:13:50.283Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR>=20440 && NR<=20560' BQT_v3_pages.txt | grep -n \"pdf page\" ; echo ----; sed -n '20470,20530p' BQT_v3_pages.txt"
}
```


### [2026-09-05T20:13:52.027Z] TOOL RESULT

```
37:[pdf page 282]
111:[pdf page 283]
----

‏- از فان (سنکه)
فان
‎ween‏
‏۱ مخفف « افردن »

[pdf page 282]
۱4۸۹

قصره - بکس اول و قتح ‎pt‏ وئالث.
بمعنی لرزه باشد خواه از سرما و خواه از تری
و یم .

فمطاط ۲ = ‎a‏ اول و سکون ثابی
وطای حطی بالف کشیده وبطای دیگر زده» بلغت
رومی سرآپرده را گوبند ۴ - ونام شهری‌هم‌هنت
ازولایت عصرگ - و شهر جامم رانیز گفته‌اند۴؛
و پسنی گویند این لفت حبشی است و منم اول
‎Fe‏

فسفسه - بفتح هردو فا بروزن ‎sey‏
‏بمعنی اسپست باشد وآن علفی است که بعربی
رطبه (۱) وبتر کی یونجه گونند وصنصه معرب
آنت 9 .

فصلیون ۱ - بنتح اود و سکون ای
کر لام وتحتانی ‎AAT gly‏ وبنون‌زده,بیونانی
تخمی‌است که سبیوش ویزرفطونا باشد .

‎od‏ ۲ - بر وزن چمن » مخفف فان

‎. ‏خم۱ : رطبیه‎ (y)

‎mys

‎col‏ وآن‌سنگی‌باشد که‌کارد وشمشیر را (۲)بدان
یز کنند - ودرعربی سنادراگوبند ۸ ؛ وبمعتی‌را
اول پروزن شکن همآمده است .

‏فسو چن ‘ ‎Jd ee‏ وفتح‌جیم‌بروزن
ربودن .. نوعی ازطعام باشد که ‎Ate‏ مردم ‎OMS‏
‏پزند وخورند +

‏قموس = بکر اول و ثالی بواو
مجهول رسیده و بین بی‌نقطة زده ؛ بمعنی‌بازی
وظرافت و سخر و لاغ باشد ‎-٩۱‏ و بمعنی دریغ
و حسرت وئاسف هم آمده است - و از راه‌بیرون
شدن و بیراهی‌کردن را نیز گویند - و با واو

‏. معروف» نام شهرست که پایتخت‌دقیانوی‌بوده۱۴.

‏فسوسیدن ۰۱۳ بر وزن نکوهیدن .
بمعنی‌دریغ وتأسف و حسرت خوردن‌سومسض ‎S‏
‏وظرافت کردن - و از ‎oly‏ بیرون شدن وبیراهی

‏کردن باشد .

‎. ‏خم ۱ - را‎ (y)

‎» ‏بنم‌اول » فطاط بکراول‎ bled : ‏یاقوت کوید عرب درفطاط شش لفت دارد‎ - ٩
‏فاط ( بنم اول واسقاط طاء اولی وتشدید دوم ) , قاط ( بکسراول و اسقاط طاء اولی و تشدید‎
```


## [2026-09-05T20:14:05.045Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nimport json\nm=json.load(open('BQT_v3_pagemap.json'))\nks=list(m.items())[:5]\nprint(type(m), len(m))\nfor k,v in list(m.items()):\n    if str(v) in ('1624','1489') or str(k) in ('415','416','417','282','283'): print(k,v)\n\" 2>&1 | head -20"
}
```


### [2026-09-05T20:14:07.003Z] TOOL RESULT

```
<class 'dict'> 6
```


## [2026-09-05T20:14:09.646Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nimport json;m=json.load(open('BQT_v3_pagemap.json'));print(json.dumps(m,ensure_ascii=False)[:1500])\""
}
```


### [2026-09-05T20:14:11.431Z] TOOL RESULT

```
{"pdf": "data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "pdf_pages": 721, "offset_mode": 1203, "anchors": 34, "map": {"1210": 1, "1211": 2, "1212": 3, "1213": 4, "1214": 5, "1215": 6, "1216": 7, "1217": 8, "1218": 9, "1219": 10, "1220": 11, "1221": 12, "1222": 13, "1223": 14, "1224": 15, "1225": 16, "1226": 17, "1227": 18, "1228": 19, "1229": 20, "1230": 21, "1231": 22, "1232": 23, "1233": 24, "1234": 25, "1235": 26, "1236": 27, "1237": 28, "1238": 29, "1239": 30, "1240": 31, "1241": 32, "1242": 33, "1243": 34, "1244": 35, "1245": 36, "1246": 37, "1247": 38, "1248": 39, "1249": 40, "1250": 41, "1251": 42, "1252": 43, "1253": 44, "1254": 45, "1255": 46, "1256": 47, "1257": 48, "1258": 49, "1259": 50, "1260": 51, "1261": 52, "1262": 53, "1263": 54, "1264": 55, "1265": 56, "1266": 57, "1267": 58, "1268": 59, "1269": 60, "1270": 61, "1271": 62, "1272": 63, "1273": 64, "1274": 65, "1275": 66, "1276": 67, "1277": 68, "1278": 69, "1279": 70, "1280": 71, "1281": 72, "1282": 73, "1283": 74, "1284": 75, "1285": 76, "1286": 77, "1287": 78, "1288": 79, "1289": 80, "1290": 81, "1291": 82, "1292": 83, "1293": 84, "1294": 85, "1295": 86, "1296": 87, "1297": 88, "1298": 89, "1299": 90, "1300": 91, "1301": 92, "1302": 93, "1303": 94, "1304": 95, "1305": 96, "1306": 97, "1307": 98, "1308": 99, "1309": 100, "1310": 101, "1311": 102, "1312": 103, "1313": 104, "1314": 105, "1315": 106, "1316": 107, "1317": 108, "1371": 164, "1372": 165, "1373": 166, "1374": 167, "1375": 168, "1
```


## [2026-09-05T20:14:14.695Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nimport json;m=json.load(open('BQT_v3_pagemap.json'))['map']\nfor p in ['1487','1489','1490','1620','1622','1624','1626']: print(p, m.get(p))\""
}
```


### [2026-09-05T20:14:16.365Z] TOOL RESULT

```
1487 280
1489 282
1490 283
1620 413
1622 415
1624 417
1626 419
```


## [2026-09-05T20:14:27.130Z] TOOL CALL #40: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2099 2>&1 | tail -50"
}
```


### [2026-09-05T20:14:33.972Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 182; check the printed number and re-run with --pdf-page if off)
REF: BQT:2099  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 182  OCR-lang: fas

-۲۹۹- اروش
اسر اش ۱ - زبان حال را کویند | ناشتا و ناهار امک که ازسباح باز چیزی نخوردن
چنانکه سرایش زبان قال را. و۱۱) گفته شد . باشد .
ناحلت « بکر ثالك وسکون کاف : نام ناءماشکعةن ۷ « بمعنی ناها رکردن
یکی‌از صاحب شر,متان کفره هند است . واعتقاد واندك چیزی خوردن باشد .
اتباع او آنست که آدمیان همچو کیاه میرویند ناش ۸ » بکر ثاك وسکون کاف »
وخشْك میشوند و از هم میریزند و بخشر وشن | قرض‌دار و وام‌دار راکویند .
قائْل لیستند نه روحائی و له جمائی - وجماعتی ناصی» دارآن پاك - کنایه از
را یز کویند از اهل مغرب که در دین راسخ ملالکه باشد - و کنابه از صالحان و عابدان
یتند ۴ . ی
پ ناسهاد ۲ وزاهدان هم‌هست .
له (۲) < بکرثالك,بممنی ناعاوری ۹ < با طای‌حطی وواو ورای
بی‌فکرواندیشه و بی‌تامل باشد چه سگالش بمعنی قرشت و تحتانی »کشت بان راگوبند که زراعت
کر واندیشه است . نگاه دارنده باشد .
ناسوری - بر وزن لاهوری » کلو ناظر در سر ای - نوینده را کوند
وحلقوم باکر ۱ که بر درسرای سلاطین وحکام بنشیند تاه ر کدام
ناشتا ۴ » بکر شین نقطه‌دار وفوقانی | ازنوکران که بچاکری یایند بنویده واورا در
بالف کشیده , ناهار را کوبند که از بامداد باز | هندوستان ناغه نوبس میگویند .
چیزی لخوردن است ‎٩‏ . ناغوش *۱- بر وزن آغوش , چیزی
ناشتاب ۱ - بر وزن ماهتاب . بمعنی | را باآب فروبردن باشد - وسر به‌آب فرو بردن
(۱) چش :- و. (۲) چش : تاسکالیده.
۱ - از دسانیر ۸« قرهنگه دساتیر صس ۲۹۸ *. ۴ - بیرولی در تحقیق ماللهند
(ص ۱۵۱ ) در جدول ۸« طوایف جنئوب » هند ۶ ناسکه » - 372912 را آورده و نیز در ص
۶ درجدول ۸« (طوایف ) جنوب ازه سنگهت » ۳ 52770112 همین نام را د کر کرده است .
۴ - از : ۷ ( فی » سلب )+ سگالیده [ اسم مفعول از « سگالیدن > (۸.م.)] ۰
۴ - از : د(نفی » ساب )+ آشتا؛ هندی باستان 26 , 2675211 ( خوردن ) ؛ فّن :
فارسی « آش > « اسفق ۱۶۱۹ و رك : هوبشمان ۰.۱۶۱۹ ربشهٌ 25 8 از 80 خوردن ( قی:
0 لاینی , 68968 آلمانی و 62۶ 10 انگلیسی ) رك : بارتولمه 4۵۲ » امشق ۷۹ ۰ فاب ۱
س ۲۳۳ ح ‎٩‏ کردی ع 82 (روزه » چیزی نخورده ) «ژابا س ۸2۱۵ ‎ )‏ کیلکی 84318
) غذا ناخورده ( ۰
8 - شخورابه های بیمزه ناخوش آندر او همجون دهان صاحب علت بناشتا .
« معزی لیشاپوری ص ۲۵ *.
۹ < باعتا (ه.م.) ۷ - رد4 : ناشتا . ۸ - رد : شعك ().
‎٩‏ - از : ناطور (عر)** ناطر بمعنی محافظ زراعت با موستان ) .
*- ۸« ناغوش » سریآب فروبردن بود از مردم » ومرغ را نیز کویند . لبیب ی کوید :
کرد کرداب مکرد ارت نیاموخت‌شنا که‌شوی غرقه چو ناگاهی داغوش‌خوری.»
« لت فری می ۲۲۰
```


## [2026-09-05T20:14:43.125Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"šp\\`dy\\|'šp'dy\\|špʼδy\\|špδy\\|špdy\" SOD.txt SOD_pages.txt | head -20"
}
```


### [2026-09-05T20:14:44.891Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:14:47.394Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"food, dish\\|dish, food\\|'šp\" SOD.txt | head -20; echo ====; grep -n \"šp\" SOD.txt | head -30"
}
```


### [2026-09-05T20:14:47.441Z] TOOL RESULT

```
Exit code 1
(eval):1: === not found
```


## [2026-09-05T20:14:49.749Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l SOD.txt SOD_pages.txt && head -40 SOD.txt"
}
```


### [2026-09-05T20:14:49.794Z] TOOL RESULT

```
 111423 SOD.txt
  45615 SOD_pages.txt
 157038 total
SOGDIAN 
DICTIONARY 

Sogdian  -  Persian  -  English 


B.Gharib 


FARHANGAN  PUBLICATIONS 


Sogdian  Dictionary  (Sogdian-Persian-English) 

by  B.  Gharib 

editorial  supervisor:  A.  Mansouri 

editor:  S.  Fotouhi 

©  1995,  Farhangan  Publications 

2/52.  Shahid-e  Said  Street,  Tehran  15916,  Iran. 

Tel:  6460069.    Fax:  670230 


ISBN:  964-5558-06-9 


4f*Jj*l{^  0"J-^8  'Jy^**-  ^J>*4^  tfW  :  j'  a>„J^  <f  jljX-U^  -LUi^-L  ^JjJ'j^  L»  e jlf  ijj- 
;l_^0  jL-u  jlS'  4$"  (.5*^-*^'  "^^  (H^-  fJ 


L?JJ  J' 


•  l^>  o-^  jl  ^^<o  (j  ^jb^b  j  uij^-  ^C*"
```


## [2026-09-05T20:14:56.859Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==136{print}' SOD_pages.txt | head -60"
}
```


### [2026-09-05T20:14:59.660Z] TOOL RESULT

```
                                                                                                                              70

 'snVxCw)


       GcOthink, (to)count
       Anc. Lett. 3.33
                                                                          mst'y-
                                                                        (ro)show
                                                                        GMS 657; STii 1.87; BSTi 253; C2 gloss.; Sund.
 1764 'sm'xfw)     M                                        U^
                                                                          AoF 1981 p2l3
       asmax(u) ©<*smdxam          ^sm'yw, sm'x
                                                                  1777 >5t»y,mnty C                                ^liWjb,
       GMS   157, 1380; KG 332                                          astayamande   Osty'mnty)
                                                                        indication
       you
1765 'sn'ky'ntyc S           (/^Li/^j^JU^                    „U         STi 32.17; GMS 1100; BSTii 904.30 : C2, 57R30
     ssnaxandic- ^sn'xntyc
     fifth month of the year                                      1778 'st'yk S
     MDii Nov. 1R                                                      ostik =*Jstyk, >cstyk
                                                                       third
1766 'sn'ych ? =* yyn'ynch ?
                                                                        ~>v, Hen. Magi. 138.29; KG 339, 617; W-Lii 569;
1767 'sp^y S                        ? o> «j£ ,? *y>. <c^-J
     (o)spa5e ? ©Pers. as ?                                                -ft, MSP bl4

       part, portion ?, bowl ?                                    1779 »st»yny C                           (tjujtjjUj)^^
      Frag. Len. 60, 8, 69, 28-33; S W, BAI 1990, 286                   astayne ©pres. part.; ob. pi. -/y ^st'y-
1768 >sp>yr B                                                >         guide, indicator
                                                                       Sund. AoFviii 1981, 174.2
      osper ? ©*y/7arya        ©ob. -y
      cave, grotto                                                1780 >st5s B                                           >js**
      BSTBL, Dhy. 362; Benv. Notesii 237                               ast-5as ~>sts

1769 >spn- C                          ^jji t jju.j7                    eighteen
     aspan, arhspan ©Khwar. hsf-\ MP hasp-                             BSTBL, Dhy. 312-3
         ©impf. mspn ^'sp'nch, }nspn-
      (/<?)rest                                                   1782
                                                                  1781 >stmy  ** >st())
                                                                       »sth S B                                          ^
      BSTii 878.7; STSC 12; C2, 87R7, 60R15                            astami

1770 >ssh B                                                cr>         eighth 1096, 1331; TSP 2.331; VJ 885; BSTBL,
                                                                       GMS
     o(s)sa ? ®*rsa; <IE       *r£-j<?; Khwar. /irs; Av.
       arsa                                                              Dhu. 231, 254, 264
     bear
                                                                       astamik ^stmyq
      SCE 359; GMS      155                                       1783 >stmykC)) S

1771 >stc» SfB                       (u^>i->»)^u                       eighth
     ast(a) ('st, }sth) ®<*asta =*sV                                   TSP 3.99, 14.17, 9.18; Frag. Len. 69.27; -w, MSP
     eight                                                               b33, 108

      GMS 87, 1316.8; Frag. Len.; >Stht MDii                      1784 >stn B                              J*^jL^-I
1772 WdV-        C *± >st>y-                                           ostan ®<*hista- =^skwn                                *j>r
                                                                       durative particle
1773 >st't S                                               &±*
                                                                       Benv. AO 30, 1966, 46
```


## [2026-09-05T20:15:21.362Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"spa5e\\|sp\\^y\\|ospa\" SOD.txt | head; echo ==== ; grep -n \"1767\\b\" SOD.txt | head"
}
```


### [2026-09-05T20:15:21.413Z] TOOL RESULT

```
Exit code 1
16318:^pysp^y,  pspy- 
16846:opospay   =»*pspy-,  pspy- 
18492:©<*us-prtaka  ^'sp^y,  spty1 
18505:ospate  Ospty)  ^spty1, 'spt'k 
18530:ospat-srose 
18595:ospancne  ?   Ospnyn'k)  -^spnyn'y 
19252:1767  'sp^y   S  ?  o>  «j£  ,?  *y>.  <c^-J 
19253:(o)spa5e  ?  ©Pers.  as  ? 
52699:pacp'atCe)  (ptsp>ty)  ^psp^y 
60000:patkarct/i-spase   ^ptqry-sp^y,  sp>sy 
(eval):1: === not found
```


## [2026-09-05T20:15:25.408Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19240,19262p' SOD.txt"
}
```


### [2026-09-05T20:15:25.452Z] TOOL RESULT

```
you 

GMS  157,  1380;  KG  332 

1765  'sn'ky'ntyc   S  (/^Li/^j^JU^  „U 
ssnaxandic-   ^sn'xntyc 

fifth  month  of  the  year 
MDii  Nov.  1R 

1766  'sn'ych  ?  =*  yyn'ynch  ? 

1767  'sp^y   S  ?  o>  «j£  ,?  *y>.  <c^-J 
(o)spa5e  ?  ©Pers.  as  ? 

part,  portion  ?,  bowl  ? 

Frag.  Len.  60,  8,  69,  28-33;  S  W,  BAI  1990,  286 

1768  >sp>yr   B  > 
osper  ?   ©*y/7arya   ©ob.  -y 

cave,  grotto
```


## [2026-09-05T20:15:44.709Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o sod136.jpg \"https://archive.org/download/SogdianDictionary/page/n136.jpg\" --max-time 120 && file sod136.jpg && ls -la sod136.jpg"
}
```


### [2026-09-05T20:15:49.053Z] TOOL RESULT

```
sod136.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 5012x7053, components 1
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
```


## [2026-09-05T20:15:54.197Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('sod136.jpg')\nprint(im.size)\nim.crop((0,1400,2600,3200)).resize((1300,900)).save('sod136_crop.png')\n\""
}
```


### [2026-09-05T20:15:56.468Z] TOOL RESULT

```
(5012, 7053)
```


## [2026-09-05T20:15:58.726Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/sod136_crop.png"
}
```


### [2026-09-05T20:15:58.760Z] TOOL RESULT

```

```


## [2026-09-05T20:16:08.917Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o sod135.jpg \"https://archive.org/download/SogdianDictionary/page/n135.jpg\" --max-time 120 && python3 -c \"\nfrom PIL import Image\nim=Image.open('sod135.jpg'); print(im.size)\nw,h=im.size\nim.crop((0,int(h*0.18),int(w*0.55),int(h*0.45))).save('sod135_c.png')\n\""
}
```


### [2026-09-05T20:16:13.986Z] TOOL RESULT

```
(5116, 7125)
```


## [2026-09-05T20:16:16.561Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/sod135_c.png"
}
```


### [2026-09-05T20:16:16.828Z] TOOL RESULT

```

```


## [2026-09-05T20:16:16.825Z] INPUT

[Image: original 2813x1924, displayed at 2000x1368. Multiply coordinates by 1.41 to map to original image.]


## [2026-09-05T20:16:40.582Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA fisfisa ===\"; grep -n -i \"fisfisa\\|fiṣfiṣa\\|Luzerne\\|pespest\\|fasfasa\" AFA.txt | head -20; echo \"=== LKT ===\"; grep -n -i \"alfalfa\\|fisfisa\\|Luzerne\" LKT.txt | head -20; echo \"=== KLN alfalfa ===\"; grep -n -i \"alfalfa\" KLN_1966.txt KLN_1971.txt | head -10"
}
```


### [2026-09-05T20:16:40.687Z] TOOL RESULT

```
=== AFA fisfisa ===
=== LKT ===
1505:59S.  Ar.  fasfasu: 'Luzerne  Medicag-o  sativa  L.',  auch  fis- fifa;  hieraus  sp.  alfalfa,  alfafe  'dass., spanischer  Klee,  foenum  Burgundiacum', engl,  amerik.  alfalfa.  [DE  100/101. Eguilaz  156.    ML  4002  Anm.
5264:flruza  609 fisfisa  598 fistik  1064 fitna  611 fulän  614 fulük(a)  831 fM>»  615 /■«»rfMfc  616.  617 furhijün  567 fuiga  618 fursa  619 fusiak  1664 fMs<!^Ä;  620
=== KLN alfalfa ===
KLN_1971.txt:10963:alfalfa, n., lucerne. — Sp., fr. Arab. al-fd?fa?a h . 
KLN_1971.txt:10966:al-fd$fasa h and Sp. alfalfa.). 
KLN_1971.txt:140831:lucerne, n., a plant grown for forage, alfalfa. — 
KLN_1971.txt:147667:— ModL., fr. Gk. MtjB(,X7j, name of the alfalfa, 
KLN_1966.txt:2169:alfalfa,  n.,  lucerne.  —  Sp.,  fr.  Arab,  al-fasfasa  . (Cp.  the  collateral  Sp.  form  alfalfez,  which  rep¬ resents  the  intermediate  form  between  Arab. al-fdsfasah  and  Sp.  alfalfa.). alfaqui,  n.,  a  Mohammedan  scholar.  —  Sp.,  fr. Arab,  al-faqfh,  fr.  al-,  ‘the’,  and  faqih,  ‘learned, intelligent’,  fr.  fiqh,  ‘knowledge,  intelligence’, alfenide,  n.,  an  alloy  of  nickel  and  silver.  —  So called  after  the  chemist  Halphen,  who  invented this  alloy  in  1850.  For  the  ending  see  suff.  -ide. Alfred,  masc.  PN.  —  OE.  Mfrsed,  compounded of  self,  ‘elf’,  and  rted,  ‘counsel’.  See  elf  and  read, alfresco,  adv.  and  adj.,  in  the  open  air.  It.  al fresco ,  lit.  ‘in  the  fresh  (air)’.  It.  al,  lit.  ‘to  the  , is  formed  fr.  a,  ‘to’  (fr.  L.  ad), and  the  dcf.  article il  (fr.  L.  ille,  ‘that’);  see  ad-  and  ille  and  cp.  al segno.  For  It.  fresco  see  fresco, alga,  n.  —  L.,  ‘sea  weed’,  cogn.  with  OI.  pifdh, ‘viscous,  sticky’,  Norw.  ulka,  ‘moldy ;  slime  , fr.  I.-E.  base  *el-,  *ol-,  ‘to  putrefy,  rot’,  whence also  Norw.  ul,  ‘moldy’,  Swed.  ul,  rancid  ,  L. ulva,  ‘sedge’.  Cp.  Ulva.
KLN_1966.txt:22230:lucent,  adj.,  bright;  transparent.  —  L.  liicens,  gen. -ends,  pres.  part,  of  lucere,  ‘to  shine’,  fr.  lux,  gen. lads,  ‘light’,  fr.  I.-E.  base  *leuq-,  ‘to  emit  light, to  shine;  bright’.  See  light,  ‘brightness’  and  -ent and  cp.  luce,  lucerne,  lucid,  lucule,  luculcnt, Luzula,  relucent,  translucent,  Noctiluca. lucerne,  n.,  a  plant  grown  for  forage,  alfalfa.  — F.  luzerne,  fr.  ModProvenf.  luzerno,  which  is prob.  a  figurative  use  of  luzerno,  ‘glowworm’ ;  so named  in  allusion  to  the  glittering  grains  of  the lucerne.  ModProven?  luzerno,  ‘glowworm’  de¬ rives  fr.  L.  lucerna,  ‘lamp’,  which  is  prob.  formed fr.  lucere,  ‘to  shine’ ;  see  lucent.  The  ending  of  L. lucerna  is  due  to  the  analogy  of  its  synonym lanterna  (see  lantern).
KLN_1966.txt:23283:—  ModL.,  fr.  Gk.  MvjSixr),  name  of  the  alfalfa, lit.  ‘the  Median  (plant)'.  See  medic.
```


## [2026-09-05T20:16:48.014Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1498,1515p' LKT.txt; echo \"=== AFA search ===\"; grep -n -i \"fisfis\\|fasfas\\|isfist\\|Klee\" AFA.txt | head -20"
}
```


### [2026-09-05T20:16:48.095Z] TOOL RESULT

```
'Feldherr,  Vezier'  [zu  pers.  färzänä 'weise,  gelehrt'  Horn  NpEt  S.  1 81 ,  Nr.  8 1  ö]; da  im  orientalischen  Schach  neben  dem König  [säh  s.  hier  Nr.  1762]  nicht  die Königin,  sondern  der  Wesir  die  Haupt- figur war,  wurde  hieraus  afrz.  ferce, fierge,  nfrz.  vierge  [mit  volksetymolo- gischer Umdeutung  zur  „Dame"],  prov. fersa  ;  bulg.  serb.  ferz,  russ.  ferz'  'Dame oder  Königin  (im  Schachspiel)'.  [Mikl SlEtWb  58a.  Bern  SlEtWb  280/281. ML  3266.
596.  Ar.  Fäs:
N.  pr.,  Hauptstadt  von  Marokko:  hieraus die  Bezeichnung  der  Kopfbedeckung  der Muslimen ;  über  tk.  fes  wurde  rum.  fes, iTZ.fez;  fiel,  pheci  {—  kepi\,  dtsch.  Fez usw.  —  ,Die  heute  in  Europa  allgemein gebräuchliche  Bezeichnung  Fez  für  die in  den  verschiedensten  Formen  vor- kommende, fast  in  der  ganzen  muham- medanischen  Welt  übliche  rote  Kopf- bedeckung hat  mit  Fes,  der  Hauptstadt von  Marokko,  nichts  mehr  zu  tun,  wenn auch  der  Name  auf  Fes  als  dem  ursprüng- lichen Fabrikationsort  hindeuten  mag. Die  heutigen  Fese  stammen  fast  durch- weg aus  Europa,  insbesondere  aus  Öster- reich. In  der  Stadt  Fes  werden  nur spitz  zulaufende  Tarbusche  aus  grobem, rotem  Filz  mit  kleiner  blauer  Seiden- quaste hergestellt,  welche  hauptsächlich von  den  marokkanischen  Soldaten  unter einem  großen  weißen  Turban  getragen werden. "  Max  Freiherr  von  Oppenheim,
Ar.  fa's.]
48
Vom  Milteluieer  zum  Persischen  Golf. Berlin  18'.t9.    1,2  Anm.  2.
597.  Ar.  fa's: 'Beil,  Axt';  hieraus  mit  ar.  Art.  pg.  al ferce  'Hacke,Spaten, Doppelkarst';  alfega 'Eisen,  mit  dern  tiie  Schmiede  die  Ösen oder  Löcher  der  Äxte,  Hämmer  usw. ötl'nen-.  [Gonstancio  Dice  49  b  und  c. Dl-:  112.
59S.  Ar.  fasfasu: 'Luzerne  Medicag-o  sativa  L.',  auch  fis- fifa;  hieraus  sp.  alfalfa,  alfafe  'dass., spanischer  Klee,  foenum  Burgundiacum', engl,  amerik.  alfalfa.  [DE  100/101. Eguilaz  156.    ML  4002  Anm.
599.  Ar.  fasha:
'Leerer,  weiter  Raum';  hieraus  mit  ar. Art.  sp.  alfeiza  'Tür-  oder  Fenster- öffnung'.   [DE  112.
600.  Ar.  falil:
'Gedreht;  Docht',  ebenso  ik.fitil  'Docht': hieraus  rum.  fitil  'dass.,  Aufreizung' [vgl.  auch  ngr.  9utijX,  Jannarakis, Deutsch  -  Neugriechisches  Handwörter- buch. Hannover  1883.  S.  129a];  bulg. serh.  ßtilj,  russ.  fitil'  'Docht,  Lunte'. [Bern  SlEtWb  282.
601.  Ar.  fatläta:
'Stückchen  Brot,  Brosame'  [vom  Vb. /a«a 'zerbröckeln'];  hieraus  infolge Imäla und  Unterdrückung  des  intervokahschen t  pg.  fatia  'dünne  und  lange  Schnitte' besonders  Brot  oder  Käse.  Vgl.  den Ausdruck:  fez  em  f alias  os  niembros  do martyr.  [Gonstancio  Dicc  550c.]  [DE 267/268.
602.  Ar.  fatwä:
{Vom  Vb.  fatä  'eine  gesetzmäßige  Ent- scheidung auf  Grund  von  Koran  und Tradition  fällen']  'Gutachten  einesRechts- gelehrten^  [faklh  s.  hier  Nr.  572,  oder tnuftt  von  derselben  W^urzel  wie  fatwä, s.  hier  Nr.  1493],  tk.  fettvo;  hieraus  frz. fetva,  fetfa,  dtscli.  Fetwah,  engl,  fetwa. [Devic  DEt  120.
603.  Tk.  ferege:
[Wie  ar.  farüga  vielleicht  aus  gr.  qpo- peaia]  'StraßenmnnteP,  einfarbiger  Man- tel mit  langen  Ärmeln,  den  die  vor- nehmen muslimischen  Damen  auf  der Straße  tragen;  dieser  Anzug  wird  noch durch  den  jasmak 'Kopfschleier',  der  über das  Gesicht  gezogen  wird,  vervollstän- digt. Aus  dem  tk.  Grundwort  kommt rum.  feregea  'ärmelloser  Mantel,  Frauen- mantel'; bulg.  feredze,  feredza  'Ober- gewand der  Braut',  serb.  feredza,  wc- redza  'tk.  Obergewand',  russ.  ferez, ferejaz  'langes  Unterkleid  russischer Frauen;  langer  Männerrock  ohne  Taille und  Kragen'.    [Mikl  SIEtWb  58 a.
=== AFA search ===
```


## [2026-09-05T20:16:57.010Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c AFA.txt; grep -c \"Luzerne\" AFA.txt; echo \"=== PLA ===\"; grep -n \"فصفصة\\|فصفصه\\|fisfisa\\|Luzerne\\|isfist\\|aspast\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20; echo \"=== AFM ===\"; grep -n \"فصفصة\\|فصفصه\\|اسپست\\|سپست\" AFM.txt AFM_pages.txt | head -20"
}
```


### [2026-09-05T20:16:57.091Z] TOOL RESULT

```
600115 AFA.txt
0
=== PLA ===
2421:mel - "asfast: "Luzerne, Futterpflanze" pers. 7 aus pers. ul aspast 
2422:MP. ana aspast 8 
15342:ansıms - fisfisa: "Luzerne" pers. ?. 7, dtsch. Alfalfa. 
15362:wLs3_ fisaäfis: Pl. veoes fisfisa q. v. 
15365:29 _ fisfisa: "Luzerne"  pers.cuuul asbast od. a, asfast 9 
15386:fisfisa 
15395:- fissa = fisfisa q. v. 
=== AFM ===
```


## [2026-09-05T20:17:01.823Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2410,2435p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== fisfisa ===\"; sed -n '15355,15400p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt"
}
```


### [2026-09-05T20:17:01.878Z] TOOL RESULT

```
Bu; 2. 
er! - > isfaranf: ein Ort in Samarkand, aus dem pers. Zusı esfarang 6 


05 - 
1 - "isfarani: Nisba ve ”isfarang 


3 
mel - "asfast: "Luzerne, Futterpflanze" pers. 7 aus pers. ul aspast 
MP. ana aspast 8 


gut - ”isfanab: "Spinat" = ”isbänäh q. v. 


9 


.93 
Seel. ”isfand: "Wein" pers. ° aus dem pers. x..spand MP. 10» Spand 


1. Lokotsch S. v. 
=== fisfisa ===


a, 
ls _ faSaka: "Patronentasche". 


E- fi$anf: ägypt. Ar. = ar. faßaka vers. Ks fe$ang 8, 
wLs3_ fisaäfis: Pl. veoes fisfisa q. v. 


29 _ fisfisa: "Luzerne"  pers.cuuul asbast od. a, asfast 9 


1. Muhlit s. v. 

2. Genaust s. v., Fraenkel s. v. 

3. pahl.-paz. s. v., Mackenzie s. v. 

4. Hosrow Qobädän n. Chista Bd. 9 s. v. 
5. Löw Ss. v. 

6. Fremdwörterbuch s. v. 

7. al-MuCarrab s. v. 

8. Chista Bd. 10 S. 1195. 

9. Muhit s. v. 


fisfisa 


4 


fissa 211 fundug 


- fissa = fisfisa q. v. 
o>la_ fagäfira: Pl. v_,ss fagfür q. v. 


_an3 - fagfür: "Titel der chinesischen Kaiser" pers. »& bagpur mp.
```


## [2026-09-05T20:17:11.697Z] TOOL CALL #56: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:17:11.704Z] TOOL RESULT

```


```


## [2026-09-05T20:17:15.575Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/alfalfa",
 "prompt": "Give the full etymology section for the English noun alfalfa: Spanish, Arabic, Aramaic/Syriac, Middle Persian forms and any cited sources."
}
```


## [2026-09-05T20:17:16.576Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ed-",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (Indo-Iranian, Avestan, Latin, Germanic) and any note about *h₁dont- 'tooth'."
}
```


### [2026-09-05T20:17:21.909Z] TOOL RESULT

```
I cannot provide information about *h₁dont- 'tooth' based on the webpage content you've shared. The document only covers **\*h₁ed-** ("to eat"), which is a different Proto-Indo-European root.

The page does not contain any discussion of dental terminology or the reconstruction *h₁dont-. To obtain accurate information about the tooth root, you would need to consult a separate etymological resource or the Wiktionary entry specifically dedicated to that reconstruction.

If you're interested in the derivatives of *h₁ed-, I can summarize those based on the provided content.
```


### [2026-09-05T20:17:22.949Z] TOOL RESULT

```
# English Etymology of "Alfalfa"

**Source Language Path:** The word traces back through Spanish to Arabic origins.

**Spanish:** From Old Spanish *alfalfez*

**Arabic:** From Arabic *الْفَصْفَصَة* (al-faṣfaṣa, "alfalfa, lucerne")

**Historical Progression:** The Wiktionary entry shows: "From Spanish *alfalfa*, from Old Spanish *alfalfez*, from Arabic *الْفَصْفَصَة* (al-faṣfaṣa, 'alfalfa, lucerne')."

**Related Ancient Forms:** The etymology tree indicates connections to:
- Old Median *aspāstiš* 
- Proto-Iranian *Hástiš* and *HacwaHastiš*
- Proto-Indo-Iranian *Háćwas*

**No Direct Aramaic/Syriac Listed:** While the translations section mentions Classical Syriac and Jewish Aramaic terms (ܐܰܣܦܷܣܬܳܐ and אַסְפַּסְתָּא), these appear as translations of the plant name rather than etymological sources for the English word itself. The primary documented path runs Spanish→Arabic.
```


## [2026-09-05T20:17:33.300Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B5%D9%81%D8%B5%D8%A9",
 "prompt": "Give the Arabic entry فصفصة: etymology (Aramaic/Syriac/Middle Persian forms), meaning, and any cited references."
}
```


## [2026-09-05T20:17:34.792Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B1%DA%A9%D8%B3",
 "prompt": "Give the Persian entry کرکس: etymology (Middle Persian, Avestan kahrkāsa-, components), meaning, and cited sources."
}
```


### [2026-09-05T20:17:39.849Z] TOOL RESULT

```
# Arabic Entry: فصفصة (faṣfaṣa/fiṣfiṣa)

**Meaning:** This Wiktionary entry documents an Arabic noun with two vowel variants. It functions as both a singulative (individual unit) and collective noun form.

**Grammar:** The word is feminine, with a collective form فَصْفَص (faṣfaṣ) or فِصْفِص (fiṣfiṣ), and plural فَصَافِص (faṣāfiṣ). The entry notes it is "singulative of فِصْفِص (fiṣfiṣ)" or an "alternative form" of the same root.

**Etymology & References:** The Wiktionary page provided contains **no etymological information** regarding Aramaic, Syriac, or Middle Persian origins. The entry includes extensive declension tables showing triptote singular and diptote plural forms, but offers no historical or comparative linguistic context explaining the word's source language or development.

The page categorizes it under "Arabic singulative nouns" and notes standard morphological patterns but does not cite external references or provide cross-linguistic analysis.
```


### [2026-09-05T20:17:42.210Z] TOOL RESULT

```
# Persian Entry: کرکس (karkas)

## Etymology
The word derives from Middle Persian (klkʾs /kargās/, "vulture"). It is cognate to Avestan karkāsa ("vulture") and shares roots with borrowings in Classical Syriac, Biblical Hebrew, and Elamite languages. The term literally means "hen-eater," combining the Persian word کرک (kark, "hen") with Proto-Indo-European *h₁ed- ("eat").

## Meaning
کرکس denotes a **vulture**, specifically the lammergeier (*Gypaetus barbatus*). Related synonyms include لاشخور (lâšxor) and نسر (nasr).

## Cited Sources
The entry references a 1066 citation from Asadī Ṭūsī's *Garshāsp-Nāma*, where the word appears in poetic context: "Due to the radiance of the blade's edge and the water's reflection, / The vulture in the air was becoming roast meat."

Additional scholarly references include works by Dehkhoda, Hayyim, Hinz, Horn, Justi, Lagarde, and Ciancaglini documenting the word's etymological development across Iranian and related language families.
```


## [2026-09-05T20:17:48.442Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B4",
 "prompt": "Give the Persian entry آش (âš): etymology (Middle Persian, Proto-Iranian, PIE root), meaning, and cited sources. Also any note on آشپز."
}
```


## [2026-09-05T20:17:48.984Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/alfalfa",
 "prompt": "Give the full etymology of alfalfa, including dates, Spanish, Arabic, and any Persian/Iranian mention."
}
```


### [2026-09-05T20:17:54.992Z] TOOL RESULT

```
# Persian Entry: آش (âš)

## Etymology

The origin of Persian آش is disputed. The entry notes two competing theories:

1. **Turkic origin**: "Perhaps from a Turkic language" with comparison to Proto-Common Turkic *aš, though "there seems to be an unexplained mismatch in vowel length."

2. **Middle Persian origin**: "Alternatively, inherited from Middle Persian" (specific form not provided), described as "a hapax legomenon found in the Vendidad, although this word is claimed to be misread."

Sanskrit connections are "sometimes proposed" but deemed irregular.

## Meaning

آش denotes:
- A thick soup dish (aush in Iran/Dari)
- Pilaf with rice, meat, and oil (in Tajik)
- Pottage generally

## Cited Sources

Doerfer, Gerhard (1965) and Encyclopædia Iranica are referenced for etymological discussion.

## Note on آشپز

آشپز (âš-paz) appears in the Derived terms section, appearing to combine آش with paz, likely meaning "cook" or "chef" (paz suggesting preparation/cooking).
```


### [2026-09-05T20:17:55.195Z] TOOL RESULT

```
# Etymology of Alfalfa

**Date of Entry into English:** 1845

**Spanish Origin:** The word entered North American English from Spanish *alfalfa*, an earlier form being *alfalfez*.

**Arabic Connection:** Spanish sources indicate the term derives from Arabic *al-fisfisa*, meaning "fresh fodder."

**Persian/Iranian Root:** According to Watkins, the ultimate source traces to an Old Iranian compound *\*aspa-sti-* meaning "alfalfa, clover." This combines:
- *\*aspa-* ("horse," from PIE *\*ekwo-*)
- *\-sti-* ("food," from PIE *\*ed-* meaning "to eat")

The etymological path thus runs: Old Iranian → Arabic → Spanish → English, with the plant name literally reflecting "horse food" in its ancestral form.
```


## [2026-09-05T20:18:19.337Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD ed- ===\"; grep -n \"ed-  ,essen\\|ed- ,essen\\|essen'\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo; grep -n -i \"^ed-\\|ed-, ēd-\\|Wz. ed-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-05T20:18:19.399Z] TOOL RESULT

```
=== WLD ed- ===
17272:ner-gh- .,drehen, zusammenwinden, wiirgen, pressen' . 
25112:ek- „essen'‘, gegen Vergleich mit ai. rvdnta- „ruhig" (?) s. Boisacq s. v.): 
37189:lich „pressen' - ), aschwed. lemma „mit der Hand driicken, hart umfassen“ 
43023:auch kreum „nage“?? Pedersen KZ. 39, 427); alb. nqrane ..gegessen' - 
47245:.jdriicken, pressen' und wohl auch anfrk. both ntvcn ..deprimere ‘ zuriickgehn 

7698:ed- „essen“.
```


## [2026-09-05T20:18:21.298Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB aspast ===\"; grep -n \"aspast\\|spst\" NYB_vol2_glossary.txt | head -10; echo \"=== IEC ===\"; grep -n \"^ed-\\|edmi\\|edo, \" IEC.txt | head -10; echo \"=== SYN eat ===\"; grep -n \"ed-mi\\|Lat. edo\\|edō\" SYN.txt | head -10"
}
```


### [2026-09-05T20:18:21.386Z] TOOL RESULT

```
=== NYB aspast ===
1267:*depasten ["dypstyn'] "full of wrath 10316, — Cf Ps. dypsty, dypsny rendering Syr ruģzā ‘wrath’. Text spspyn’, correct- ed by Dhabhar to spstyn' and combined with NP sapist 'nasty'. This spstyn' may, however, be read dypstyn' as well; the assumed meaning of this w. would suit the context better. [MPrs ^npspyn M 985 (S) is indistinetly written and guite uncertain].
=== IEC ===
1184:bhedo, ið ‘dig, stab, bury’. Cf. WP II, 188, and see bhod- Hitt. pedahi, bedahi ‘dig’; Thrac. cf. béssa (valley, fr. *bhedio); Gk. cf. s-phedanós ‘thrusting, eager, violent’; Ir. cf. beadhán, m. ‘sting’; OBr. cf. bed, W bedd ‘tomb’; Br. béz, id.; Cor. bedhy (denom. “bury'); Li. bedü, bèsti ‘thrust, stab’; Lat. bedu, best “dig”, beside bedre ‘ditch, grave’. (O-grade in Lat. fodio, Gre, and OCS bodo, bosti 'stab")
1374:bhlendhó ‘mix, confuse, dazzle’. WP II, 216. Cf. bhlondh-, bhindh- MHG blinden ‘dazzle; grow blind; OCS bledo, best ert, rampage’; OCz. bledu, blésti ‘twaddle’; Li. blendZiu, blesti ‘mix w. flour’; blendZiuos, blestis become overcast
1617:Cf. bhrodh- Alb. bredh, aor. brodha, v. “wander; leap’; W (*-&-) bridd “leap forward’; OFris. bred-, "Sw. bråd, ON bráór “rapid, sudden’; ON bræða ((2) *hurry'); OCS bredo, bresti ‘wade, ford; R bresti ‘wander’, beside bred 'deli- rium’; Li. (nasal infix) brendu, bristi ‘wade’; Latv. briedu (fr. a nasal type), inf. brist, id.
2753:dheigó, io “shape, mould, make’. (There is some confusion w. next, q. v.) WP I, 833 Tokh. (ambig.) A tsek-, B tsaik-; Lat. cf. fingo, pf. finxi beside figulo, figlinus, etc.; Osc. cf. fifikus “shalt make’; Fal. fifiked (if not fr. *tuak-, q.v.) “has shaped; MHG tichen, sv.l. *make, form" beside tich *dam'; OE dic: Du. dijk; (?) cf. Cz. diže (trough for kneading dough’, but see next entry); metath. in OCS ziždọ, zidati “build, found”; OLi. Ziedmi, Li. žiedžiù, Ziesti (“fashion on potter's wheel). See next entry
3420:` edmi. WP I, 118
3422:edolis, os, om “edible; food". WP I, 118. Cf. éd-, edmi, etc. Lat. edulis; OE etol; ON etall; Blg. jàlo, jàdalo ‘food’; Cz. jedlý “edible”; jídlo ‘food’; Li. ēda- las ‘pigfood, swill’
3424:edmi, (edó), 3s esti *eat. WP I, 118 Skt. ádmi; Av. ad-; Hitt. écmi; Hom. édo; Lat. edo, 3s ést; Osc. edum, mi Ir. cf. íd-ighim ('consume', fr. *éd-a8-); Go. itan; OE etan;
3426:OHG e33an, ezan; G essen, beside aassen 'de- vour’; OCS jami, inf. jasti; R jém, jësti; OLi. edmi, Li. ēdu, inf. ēsti; Latv. edu, est
3693:ëskå (əsk-) “food. Cf. edmi & WP I, 119 Hitt. cf. acikimi (for *atskimi: ʻeat’); Lat. esca; Li. eskà ‘appetite’; esküs ‘gluttonous’
6597:kai-, modal fragment: “alone, separate; only, but, yet’. Cf. kaikos, kailos (2) Skt. cf. ké-valah “alone, separate'; Arm. cf. kes (‘half ? if for a type *kai-K-. For the semantic parallel cf. *sé- "apart: *semi ‘by parting’ hence ‘half. See sémi); Gk. kaí and Lat. cf. caedo, ére, v. eut, lit. ‘separate’? ambiguously to OCS céZdo, céditi ‘sift? etc., which is pre- ferably to skoid-, q. v.); cf. Lat. cael-ebs (see „ail- below); synth. cpd. in OCS cé-glü (“alone”). Second element obscure)
=== SYN eat ===
```


## [2026-09-05T20:18:29.399Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7690,7715p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:18:29.447Z] TOOL RESULT

```
Ai. Citm&n- daher nicht (obwohl lautlich unanstoBig) mit a- als Tief- 
stufe von ani-ti „atmet“, wie auch (trotz Prellwitz BB. 23, 75) fur die germ. 
Y’orte Anknupfung an diese AYz. *an- (angeblich auch *enc-) unmoglich ist. 

Ganz fraglich ir. athach „Hauch, Wind“ (Fick II 4 8). Uber gr. dr/aos 
„Dampf, Dunst“ > aus aezftog) s. vielmehr *ue- „wehen“. 

ed- „essen“. 

Praes. unthematisch ai. admi, dtti „essc, ifit“ (themat. ada-sva); gr. k'd- 
iierai, Fut. (eigentlich kurzvokalischer Konj.) edo/.iai (vgl. auch odcoi’ aus 
*tdd>v „Zahn“, Ptc. wie ecnv zu eon .,ist“; das thematische edco ist nach 
Sommer Krit. Erl. 156 wohl erst aus dem Ptc. idovi- und der danach auf- 
gekommenen 3. pi. edorzi erwachsen, hiingt also mit ai. ada-sva, germ. 
*dan nicht geschichtlich zusammen), imper. *lodh = ai. addhi vorausgesetzt 
von iodtco (sbi?oj) ,,esse“ (Brugmann IF. 32, 63 f. ; lat. \edo\ es, est usw. 
„essen“ (zur Liinge des c und zum Aufkommen thematischer Formen siehe 
Sommer Ildb." 540 f., Krit. Erl. 156 f. m. Lit,; e scheint alt, vgl. bait. slav. 
*edmi, Brugmann II 2 3, 522, wiihrend Sommer Hdb. 2 122, 542, Krit. Erl. 
159 in es, est, esse, esus Dehnung von e nach der sog. Lachmannschen 
Hegel sieht; osk. Inf. edum ); lit. emi [aus *cdmi , vgl. Buga Kalba ir sen. 
I 213] ( edu ), esti „essen“, lett. edu (emu), est, apr. ist „essen“; 

aksl. jamb, jasti „essen“, szn-esti ,.verzehren“. Thematisch got. it an, an. 
cin, as. ags. ctan, ahd. r.^an ,,essen“; arm. idem ,.esse“ (*od~; Hiibscb-
```


## [2026-09-05T20:18:29.656Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"5\\.11\\|EAT\" SYN.txt | head -10; echo ====; grep -n \"4\\.27\\|TOOTH\" SYN.txt | head -10"
}
```


### [2026-09-05T20:18:29.700Z] TOOL RESULT

```
Exit code 1
696:Rain (sb.) Snow (sb.) Icz WEATHER Fire FLAME (sb.) SMoKE (sb.) ASHES Burn (vb.)
2044:1.78 WEATHER
5209:Breatuy; BREATH
5893:Most of the words for ‘ear’ belong to an inherited group. ‘These and the others, so far as their origin is clear, are related to words for ‘perceive, hear’ (15.11, 15.41),
6352:4.393 FEATHER
6693:4.51 BREATHE; BREATH
6785:4.55 SWEAT (sb.)
7344:4.75 DIE; DEAD; DEATH
8314:CHAPTER 5 FOOD AND DRINK; COOKING AND UTENSILS 5.11 Eat 5.57 Minn 5.12 Foop 5.61 Mezar 5.13 Drink (vb.) 5.612 Burcurr 5.14 Hunexr (sb.) 5.62 Brrr 5.15 Turrsrt (sb.) 5.63 Sausace 5.16 Suck (vb.) 5.64 Sour, Brots 5.17 Mrx 5.65 VEGETABLES ' 5.21 Cook (vb.) 5.66 Bran ? 5.22 Bor 5.67 Pra 5.23 Roast, Fry 5.68 Onion 5.24 Baxe 5.69 CaBBAGE 5.25 Oven 5.70 Porato 5.26 Por 5.71 Fruir 5.27 Kerrin 5.72 APPLE 5.28 Pan 5.73 PEAR 5.31 Disx 5.74 Pracu 5.32 Prats 5.75 Wie : 5.33 Bown 5.76 Grape 5.34 Pircuer, Jue 5.77 Nur 5.35 Cup 5.78 OLIvE 5.36 Saucer 5.79 Om 5.37 Spoon 5.80 Berry 5.38 Kyire 5.81 Saur 5.39 Fork 5.82 Prpprr 5.41 A Mua, 5.83 VINEGAR 5.42 BReakFast Bi Rdeer ona 5.43 Luncx 585 § 544 Dinner een Base Sucnbn. 5.86 Mixx (sb.) 5.51 Breap 5.87 Minx (vb.) 5.52 Caxn 5.88 CHEESE 5.58 Dover 5.89 Burrer 5.54 Kwrap 5.91 Merap 5.55 Mzau, Frour 5.92 Wine 5.56 Grinp 5.93 Brrr
8318:EoD AND DRINK; COOKING AND UTENSILS 327 4 5.11 EAT sate th 20° tpayov Goths malian itan un ager (ésti) iy 1 .
(eval):1: === not found
```


## [2026-09-05T20:18:35.227Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8318,8345p' SYN.txt"
}
```


### [2026-09-05T20:18:35.270Z] TOOL RESULT

```
EoD AND DRINK; COOKING AND UTENSILS 327 4 5.11 EAT sate th 20° tpayov Goths malian itan un ager (ésti) iy 1 .
Gr. epirtyy BOT epaye Dan.  spise (ade) ChSl. jasti NG Fase; ederé Sw. dta SCr. jesli Lat. mangiare OE elan Boh. jislt It manger ME ele Pol. gesé ee comer NE eat Russ. jest’ (kuSat’) Ln minca Du. _eten Skt.  ad-, ag-, bhuj-, ghas- Ir. ithim OHG = ezzan Av. z’ar-, gah- Nir. ithim MHG ezzen W. cl NHG essen, spcisen Brigrene 2
A majority of the words for ‘eat’ be- | of animals, etc. (NE fret with total loss long to a2 inherited group Aa ae of any relation to food).
survive on ; ;
an ID *ed-. A at oe candle fee cf 2. Grk. tp&yw ‘gnaw, nibble, feed on’ as homely words use The’ gabsti- (perh. : Lat. tergére ‘rub off’, terere ‘rub’,
ing’ oF yulgarly of men. : sul tutes are partly words meaning original-
ly ‘chew, nibble, swallow’, etc., which were used of animals ‘feeding ‘ and also gs colloquial or slang expressions with reference to men (cf. NE where’ll we feed?), until they finally became the standard words for ‘eat’. Others are derivatives of nouns meaning ‘food, meal’ (these of various sources discussed under ‘food’, etc.), that is, ‘take food, a meal’; or again from the notion of ‘par- take of’, with specialization to ‘partake of food’, as frequently in NE. 1. IE *ed-. Walde-P. 1.118. nout-M, 294f. Walde-H. 1.392 f. Grk. éw (poet.), Att. éciw; Lat. ésse, late edere, Ose. edum; Ir. subj. estar, Oe * Pass. eisse, etc. (supplying parts of Grae ef. Pedersen 2.559; Thurneysen, ae 471), W. ysu ‘devour’; Goth. titan, : as Gme.; Lith. ésti, Lett. ast, Br a aa jasti, ete., general Slavic; wie (re eulem; Hitt. ef-. But Dan. ith, as for ‘eat? in Dan. Bible) and ae are now used only of animals Barly of men). Falk- NSB gy. alk-Torp 1411.
Cf, feat enw Goth. fra~itan (for xarecOls zon ‘de, se ), OE fretan, OHG free- » Whence NHG fressen, used
Er-
etc. Walde-P. 1.732), used mostly of animals, but also of men, and in late times simply ‘eat’. In the NT, while less common than éo@iw, it is usual in the Fourth Gospel and must have there a fully respectable standing, for it is put in the mouth of Jesus (Jn. 13.18, etc.). For other examples in pap., cf. Moulton- Milligan s.v. NG zpw(y)w is the reg. word for ‘eat’ in the present.
Grk. aor. é$a7yor, still persisting in NG tava, fut. 04 da(y)w, etc. : Skt. bhaj- ‘sive or receive a portion’, bhaks- ‘par- take of, eat or drink’, Locr. rayaroga- yetcrat ‘have one’s property confiscated’ is a relic of the more general meaning. Walde-P. 2.127.
Grk. BiBpacxw ‘devour, eat up’ and simply ‘eat’, BeBpwxa, eBpadnv being used in Hellenistic Greek as tenses of écbiw, fr. IE *g*er- ‘swallow, devour’ (cf. Grk. Bapabpov ‘pit’) in Skt. gr-, Lat. vorare, ChSl. Zréti, etc. Walde-P. 1.682 ff.
3. Lat. comedere (> Sp., Port. comer) epd. of edere.
Lat. manditcare ‘chew’ (beside older mandere), used collog. for ‘eat? and freq. in this sense from Varro on (esp. Petronius, Peregrinatio, Itala, etc.). Hence Olt. manicare, Fr. manger (> It.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Hoot See eens
Digitized by Arya Samaj Foundation Chennai and eGangotri
328 SELECTED INDO-EUROPEAN SYNONYMS
mangiare), Rum. minca, etc. Ernout-M. 585. Walde-H. 2.24. REW 5292.
4, Ir. ithim : Skt. pitu- ‘food, drink’, ChSl. pitéti ‘feed’, etc. (5.12). Pedersen 2.559.
W. bwyita, fr. bwyd ‘food’ (5.12).
Br. dibri, MBr. dibriff, OBr. sb. diprim ‘food’, Corn. dibry., prob. fr. a cpd. *di-prim-: NIr. creimim ‘gnaw, chew’ (Ir. vbl. n. creim, K. Meyer, Contrib. 511). Henry 95. Loth, Vocab. vieux-breton 105. (Otherwise, but to be rejected, Pedersen 1.111).
5. Goth. matjan (more common than titan), fr. mats ‘food’ (5.12).
Dan. spise, fr. sb. spise, loanword fr. MLG spise ‘food’ (5.12). As the polite term this has displaced the old ede (above, 1), as NHG speisen has en- croached on essen, but without displac- ing it (Kretschmer, Wortgeogr. 469).
6. Lith. valgyti (displacing és¢; 1), fr. valgis ‘food, meal’ (5.12),
7. Russ. kugat’, polite term ‘partake of’ food or drink : ChSl. = kuszij ‘taste? etc. (15.31). :
8. Skt. ag- ‘eat, devour’, et: ; Walde-P. 1.112, pe!
Skt. bhuj- ‘enjoy’, esp. ‘enjoy food eat’, prob. : Lat. fungi ‘be engaged in, perform’. Walde-H. 1.566 (with Tefs.)
```


## [2026-09-05T20:18:35.885Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'ad-  V\\.\\|ad-  V\\.  'essen\\|essen'\" BRT.txt | head -20"
}
```


### [2026-09-05T20:18:35.949Z] TOOL RESULT

```
2533:*'te  *yffi'^  fracarinti  , .  aiialiqm  .  .  N.  ,paiqn  ,  ,  'na  ,  ,  triltm  k>hrp}m  hvan.- ^.  III)  In  folgenden  Fallen  brauchen  i  t/arwr« -f?rv«aii/V.  5. 13,  3)  'dann'  im wir  den  Sing,  mit  'ein'  (unbestimmter  Ar- !  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Plur.  artikellos  (vgl.  ^aisa- 111}  j  dessen',  einen  Zwischensatz  hinter  einem yesica  .  .  upairi  'l^m  iristim  .  .  Ajr^zy^lf '  SaU  mit  yai  einleitend:  y^i  ndii  nidan- yaia  .  ,  "und  wenn  (man)  .  .  auf  einem  sayilnte  —  ''ja  kl  alte  sünö  vä  .  .  fraja- Toten  ..  liegen  lässt  .  ."  V.5.61;  — yö\s,yi>  —  kä  Af  asU  äiaX.ö.^T,  —  yaii'a vastnm  upaiiharizatti  upatri  °t»m  tristem  |  vaoeäp  aiSö  m7  Aanqm  .  .  p3r>saKuAa  — "wenn  einer  ein  Gewandstück  auf  einem '  "'la  ae^a  y<J  kaine  hanqm  . .  p?nsaili  , .  — Toten  liegen  lässt"  V.Äaj;  —  bei  rela- 1 'ort  assa  yS  kaine  altahmat  puir.lt  *mi- tivisch  angeschlossenem  Nomen:  yat  "te^  manxlstti  —  '^Aapanta  .  .  vfri^qn  .  . yöi  tnazdayasna  . ,  taci.apaya  nasSum  fra-  [  V.  /J.  1 3  f. ;  —  yeii  mit  Aari^nm  baraili jasqn  "wenn  Mazday.  auf  einen  Leich-  -  "da  aisa  yö  afirinüyakö  adJityö.an- nam  in  fliessendem  Wasser  stossen"  V.  6.  Aarj^nin  (sd.)  iri^ät  —  ^'>para  A!  iri- 26;  <y.73,  7-36.  \sittt5  rais?m  cikayat  .,  V.7j.i6.
2561:'''tt  *yöP^  fracarmii  . .  aitaSsqm  .  .  N.  patan  .  .  'oa  .  .  agtJm  k>hrp>m  hvar».- ij.  III)  In  folgenden  Fällen  brauchen  j  i/awjrjw  fo/vwuc/ V.  5. 1 3.  3)  'dann'  im mir  den  Sing,  mit  'ein'  (unbestimmter  Ar- 1  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Flur,  artikellos  {vgl,  ^aila-  III) '  dessen',  einen  Zwischensatz  hinter  einem jcsVJ  .  .  upairi  'tim  iristim  .  .  k>r>zyllt.  Satz  mit  ytzi  einleitend:  ye:i  mit  mdart- ya>a  .  .  "und  wenn  (man)  .  .  auf  einem  l  sayanfe  —  'ca  he  alte  sünS  vä  .  .  fraja- Toten  . .  liegen  lässt  .  ."  V.  5. 6 1 ;  —  /^ ,  JiW^  —  kä  hl  asti  Wia  V.  6".  47 ;  —  yesila vastnm  upaifharizaiti  upairi  ^tfm  iristtm  ^  vaocät  aSsö  nä  hanqm  .  .  p>r?sat3uha  — "wenn  einer  ein  Gewandstiick  auf  einem  .  '<,a  aSsa  y.J  kaine  hanqm  ..p^nsititi  . .  — Toten  liegen  lässt"  V.  ^'.23;  —  bei  rela-,°ö(J  a^ia  yä  kaine  aetakmut  puir-at  *mi- tivisch  angeschlossenem  Nomen:  yat  °te\mar?x^iliti  —  '^hat<anta  .  .  7>)r?zyqn  .  . yei  mazdayasna  . .  taH.apaya  nasHum  fra- '  V.  /5. 1 3  f ;  —  yai  nöii  har^'^nm  baraiti jasqn  "wenn  Mazday.  auf  einen  Leich-  —  °ofl  aila  yS  ap^rinlyükö  adaityo.at3- nam  in  fliessendem  Wasser  stossen"  V.  6. '  harsirim  (sd.)  iriiyäi  —  ^para  he  iri- 26;  ^.73,  7-36-  \Hntö  raSsim  cikayat  ..  V./j.iö.
3173:•  j.  a-£istäe  Inf.  'zu  speisen,  zu  essen': ya  pipi^wa  vasö  a^  "feste  Nahrung  darf man  nach  Belieben  essen"  N.  (>2.
3800:•  j.  aiwi-ynixta- Adj.  (fem.  VJ-) 'angenagt, angefressen' :7«i'  nasus  °ta  sünö  v3  k?niß.- s^arö  vayS  vä  k^m/s^i^arö  {%A.)  V.  7. 30; —  'la  V.5.34PÜZ'.
3802:•  j.  aiwri.j'zärain  Absol.  'beim  Herzu- fiiessen':  ka(,a  x3  .  .  a/iam  yiJrqm(^V.) a'  "wann  werden  die  Wasserquellen  herzu- fliessend  fliessen?"  VtÄ  42.
4282:•  j.  an-aiwi)Tiixta  Adj.  (fem.  'ia-)  'nicht angenagt,  ange&essen':  yezi  aisa  nasus  °ta sanö  v3  kjr^s.x^arS  (sd.)  V.7.29.
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
6722:1)  'werfen  (eine  Waffe),  schiessen':  arstii yqm  *an/iyeili'^  avi.>tiiiris  Yt  10.  ao;  *2i; —  tiyris" .  ,  yi'm  an/iaf  »rsxsö  (sd.)  Yt  8. 6;  —  äsyatjka  Avastayn  {sA.)  *arikima- nayäi^  (GD.)  Y.57.  28;  —  yalat  hvasttm (sd.)  *a»Ayeiti''>  Yt/0. 21;  —  asia  F. 7.  2)  II  militärisch  'werfen'  sva.  'drängen in  — '  (Lok.):  aniy<^  äpiyä  *,lAyata^'>  "der Feind  wurde  ins  Wasser  gedräng "" /.  19.
6958:•  j.  ahyäsä-"  fem.  Adj,  'die  Worte  ahyä '  •  j.  a-x'^sa-  n.  'Nichtessen':  s^älaya  vispö yäsä    enthaltend,    damit    beginnend':    'ia  '  afvhtts  .  .  jvaiti  "se  fi-amiryeite  V.^.33. Äaiii/ (sd.)'i   Y.  2<S'  Überschr.;    —    'sqm       Fa.:  Aa^  ax'arü-  - AaUlm  yazamaide  V,  a.S' is,
10288:•  j.  gah-  V.  'essen;  fressen',  uzw.  von i/iiAischen  Wesen'',  Praes.  2  gatsha-, 4  gäffha-,
10289:'essen',  von  den  Dasva:  aste  yöi  dagva aitaisva  daxmaisva  gan/i)nti  apäca  vae- pmH  ya>a  .  .  V.7.SS.
10291:mit  nis  'auf-,  wegfressen',  von  Tieren: spis  (sd.)  . .  yim  tnasyaka  yaom  yav5.hva niigaahinti  vaslra  vasträhva  V.ij.^.
10501:■      ■        —       ■  'nmän^fatil.?,ii.:k<,,!am  \ ,  j.  yjar-  V.  'iÜessen'.     Praes.  4  fzära-, "  """""'  t^i   7  (Jnt)  yiari.yiar-,  2oyiaurv;  30  (Kaus.)
10511:Eig.  Bed.?    VgL  JusTi  NB.  507.  1      nüt  irnft  'herzufliessen':  s.  Absol.
11809:mitiirä'>'herzufliessen':z'I'{^a«^«i&  apqm aiwi.tacaintqm  Vd.  ^
11818:mit^J  z  )'hervorfiiessen;  vorwärts,  weiter fliessen':  artdvlm  .  .  yä  amavaiti  /rata- caiti  .  .  aoi  zrayü  . .  V.65.3;  —  äps  yh t^nüt  faiti  /raiaätiH  "^.ßs-y,  —  äänus (sd.) . .  *Jrä  bunat  ta/in/i/QiSi)  Aog.  77
11837:undeutlich ;    vgl.  Sp.  Komm.  /. 2}  'Fliessen'.
11865:•  j.  ta£at.ip-  Adj.  'des  (bei  dem,  durch den  die)  Wasser  fliessen':  xsvföa  ätoiti  . . °apa  (ND.)  ux^yatunara  Y.i6.8'\
12728:•  p.  'dao-  V,  'fliessen'.    Praes.  10  äanu-.
14854:Ä8.  a)  mit  Abi.  'aus  -':  paourva.-  daliß&z\ia  Art  'herangehen  zu-';  a)  mit namat patai  dyaoHf^A.)  .  .  anrö  mainyus  -qxl.:  hamaka  airyabyU  daiAhubyB  hatna Yt. j.  iz;—ptat  (3SPrA.) F.  10.  3) ^oia ,  f^apatänti")  Yt  S.  61.  b)  m\tpaiH und Wasser;  a)  'herabfallen,  -strömen',  vom  j  Akk,;  s.  a/rapatai  Int Regenwasser:  s.-V««/-(in/«/.3A).  b)'über-  mit  z^r(z'(/)  in  rfo^Hscher  Art 'weg-,  fort- fliessen',vomsiedendenWasser(?):><W««/a  l,gn,.  ^fj- ^pam  Ha patmiu  vi  dalvhM (sd.)  patmla  F.  4  f.  4)  Term.  techn.  für  %j  ^  g  yf /o.  i . dasGehen  rfjftTschcr  Wesen:  hamySila  ..\  mit,ia«'fallen,hinabstürzen in-'(Akk.): davqi>ya  patqi^yä  Y.g.  18;  —  vagn^mn^  \  ^ru/asianam(sd.)  haMpataiti{T&m\.daevd) (sd.)  anmat  para  dalva  patayin  Yt  ig.  80; '  V  70  4.1    '  *
```


## [2026-09-05T20:18:43.536Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"j\\.  ad-\\|g\\.  ad-\\|ad-  V\\|adaiti\\|aiaiti\" BRT.txt | head -20; echo \"=== asa- ===\"; grep -n \"äsa-  Adj\\|asa-  Adj\\|'essend'\\|essend\" BRT.txt | head -20"
}
```


### [2026-09-05T20:18:43.593Z] TOOL RESULT

```
3210:•  j.  ad-  V.  'sagen'.  Praes.  24  aoaya-,^ 30  (Iter.)  aiaya-,  PrP.  J»w;  Perf.  nJ:
3249:KompA.  —  Vgl.  aiaiti.  —  ai.  aJiara-  Adj., np.  -»gl.  «>»).    —    Pü.   (lu  S.,    N.  52):    alar,\
3383:•  j.  ad-auruna-  n.  'priesterliche  Funktion, Priesterdienst':  Äa/  nä  a%rava  (sd.)  *ngm
5455:•  g-  (t  j)  arad-  V.  'gedeihen  lassen'. Praes.  i   arid-  :  »rjd-.
6189:Gen.  subj.  und  obj.:  alsm  *d>nidyäi{iA.) .  .  rayS  'st/  ". .  jrXoiiTOU  fioi'pai"  Y.  4J.  i ; —  abifra  (sd.) . .  ya  vaahsus  'sis  mananha Y._3i5.i3;  —  aiahya  yasa  {%A:)  'slm  y am iiyam  Y.  54.1;  —  °M/a  ^ae^ananqm viäu/(sd.)  ahurakya  mazdS  ".  .  des  AhM. Belohnungen  fiir  die  Taten  . ."  Y.2<V,4; — ■  nöit  kl  "M  *^ao^nanqm  vimysit  N. 16  ij);  —  zard>!ustrahe  .  .  asatinS  'itmia fravaiimca  yazamatde  Vr.  16. 2 ;  2,  Yt  13. 95;  —  tti  ahmt  nmane  Jamyarps  yh  asao- nqm  xshätas/a  'sayasca  . .  paitisatitayasla Y.  60. 2.  a)  mit  vanAav-  Adj.  und  aka^ Adj.  näher  bestimmt:  vatfkttyascä  °Ssi/ .. yS  ns  ara^ä  (sd.)  irmavaia^a  asanhäxs ^■5^-3't  —  syao^ana  mizdavqn  (sd.)  .. akfm  akai  vamthlm  'stm  vanhaavi  Y. 43. 5 ;  —  tSm  vatmklm  yasä  (sd.)  °sim  Y. 5;. ai;  —  maifyn  siaya  ahm  vaaAuya 'st  gaui  (sd)  Y.5/.  10«;  —  xmBth  afn- n>ntu  ahmya  nmsne  vawtklm  °/lm  i^a- parqm  Yt.  /J. i  S 7 ;  —  vaauAlsca  aöa  vaau- klsca  'sayS  Y.53.3;  —  yhca  tsi  gmh *aiura.mazda  ..  iSä  . .  vanukim  iihl/  'lim . .  ihm  .  .  *panndlm  yazamaidi  Y.^S. if  b)  Du.  'die  beiden,  beiderlei  Lose', d.  i.  (das)  gute  und  (das)  böse:  tmnanha (sd.) y5  dä%alibyd  priLratüm  xsayqs  'äfä*"^ üista  ". .,  der  über  beiderlei  Lose  gebietend den  Klugen  den  wahren  Ratav  versprochen hat"  Y.57.5.  A)  als  Gottheit,  die  die Lose,  insbesondere  die  guten  verteilt,  im jAw.  als  Göttin  des  durch  Frömmigkeit  ver- dienten Wohlstands*';  I)  im  gAw,:  Siraosö 'sfi  mqza.raya  (sd.)  Aacimnif  ya  vT  altl *ran3ibya  savlfi(sd.)  vldayäi  \ .  4j.  1 2 ; -^ sraosS  .  .  yU  *'li^  haiaiti  *mqxaraya  V. 27.6,  Vr. /2.1;  —  ya  vldayaf  'sts' (HS.) räshqm  (sd.)  Y.j^.  la;  —  ys  fta  'sSis aojaifha  var>dayaita  yqm  ,  .  gai^qm  .  . Y.  so.  3.  a)  Du,  in  Verbindung  mit armaiay-  Du.  ^A.  und  Arm.':  yads  ahm zivlm  (sd.)  .  ,  mazdasca  .  .  'sicil  armaitl Y.31.^.  II)  im  jAw.:  yö  'lim  yazäite ..k5  mihnm  yazaiieY\..i-j.2;  —  -/j  (VS.) srlre  'si  banumaili  .  .  °li  dä'ire  vehäm i^arifiilYt.sy.^;  6of.*;  —  hm  hacSl  'Hl pourvsj^ä'iira'Yt  /j?.54;  — /rä  mqm  aiwt.- urvalsayatfuha  marsdik?m  'al  (als  VS.) hnzaiti  Yl  77. 1 5 ;  —  'lim  . .  darr/S.- variiman3m..bartntltn  vispä  baSlazsY.S'i. 2;  —  sraohmla  'lim  nairXmca  sauh>m IVyt.40;   —  fravalays   .  .    'Isil  balsaza
8751:Lebenskraft'^':  hyat  astvant»m  (sd.)  dada 'tatum  y.j/.  ij;  —  tal  ii  .  .  vairim  ast- rwV?  (sd.)  'tänäi''''  data  Y.^j.,^.  14;  —  at rätqm  zara'^uÜrö  tanvascti  x^ahya  'tattpm dadaiti  paurvatätpm\.33.i^;  —  f^ra  vS rahl  .  .  tanvasclt  c^'ahyS  'tatum  V.  //.  18; /_9.4;  — darsyö.xia'irpm  xsa'^raAe  dury/ö.- jUim  'tilnahe  A.  1.8]  Y.  17. 19;  —  m-^irpswa slün'i  gayehe  mprpzu^a (sd.)  xa  'tänahe  Yt. JO.  7 1 ;  —  avai  he  astt  masyö  ar^i^pm  yat \  'tatum  bttnjayüt  (sd.)  V.  7.  7 1 ;  —  ava \  apamm  (sd.)  gayehe  *frasatu>m  'tanahe  Yt.
9068:75.44;  —  tJm  ahmakäis  azdibiscä  "tänäiscä  I  a)  °vaUi  häitis  (sd.)''  Y.^J  Überschr.;  — yazamaidg'^.^'.^;  —  nöit  astS  ttiS'it  'tänahl\  -vaitim  häitlm  {&A^^^ yazamaide  \ .  43. 17; Hnmata\.i2.y,  —  vi . .  wvaesayäl  astaca  a.4Ö;  —  'vatlyä  vü  . .  Aälsis  {sA.)'>  Aan- 'tänaca  (APn.)  P.2/;  —  Stars  handaiaiti\dsta'^.  102''.  b)  'Taitlm  g.l'^qm  (sd.)" ^asia  "tämm^a  V.5.9;— «(X^  asWa  nBit . .  .  yazamaide  V.46.2Q;  yi. 16,  Vr.  i'.  8, 'i-irumca  {HSn.)  nBit  inoaasea  *vT.ur7'lsyät  iX.o,  H.2.8;  —  'raitya  gu^aya  (sd.)" V,  it).  T,  —  vlspii  gafiäs.'a  tanvas'a  .Aandäiä  yazamaide  \.4b,xo;  A.  2.  i,  V. azd:>hls(a  'tänqsca  kglirpasca  tnnsista  dat>- ■  iff-^S,  Vr. /.6,  jS'.y,  *N. /02. oas^a  unMlTumt'a  fravasim:a  pairica  dadj- ,  "  !*■  ■■  V.  43-  —  "  D-  i-  Y.  43-^- mahl  .  .  V.  jy  1 ;  —  "/iPit  ynysi  'täna"  ■  •  j.  usta.x''araiiah-  m.  Name  eines  Bergs Nik.2.  \u<liina    \. 43.16:    s.  zu   Ufiä-'odeTGthiTgs'.a/imatha/trgamyti/rai'xsy-m
9272:mit  aipi  'ab-,  entzwei-,  in  Stücke  zer- schneiden': hakat  vTspi  aipi.kgr^titaiti "alles  schneidet  er  .  .  in  Stücke"  Yt.  JO-  7  2 ; —  i'JiÖ  massdd.fraoxia . .  yüi  aipi.k»r»n/^nti vlsp»m  dusmat3m . .  aipi.k)r?nlifUi . .  duzQx- t3m  ..  aipi.k>ryntmii  ..  dusvarsUm ätarS  huskitn  aismjim  .  .  c häfayeili  (sd.)  äaiaiti  Y.  7/.
9742:—  yavanqm  .  .  västranqm  .  .  '•%anqmca  Wesen  und  Dingen  zum  (Reich  des)  Asa, ashaiiinqm  YtÄ29;  usw.;  —  s.  noch  zur  stofflichen,  sichtbaren  Welt  des  Asa Anhang  «.  2)  'Wesen'  im  Sinn  von  gehört':  'irj^räi  asake  °'^anqm  "um  zu 'Anwesen';  'Gehöft,  Haus  und  Hofs>,  schirmen  alles,  was  zum  Asa  gehört"  Vt. Hausstand  (ramilia)',  überhaupt  'Hab  und  /p.  48;  Y. 55.  3^  57.  17;  —  makrkai  alahe Gut' (im  Gegensatz  zu /<2ns-,/fl«a/-), 'weit-  '>anqm  Yt. /<).  50,  Y.(?.  8;  <?.  3,  V. /Ä  sSi lieber  Besitz*  (im  Gegensatz  zu  ankav-  —  asiby5  yli  urvätäiS  drRjS  asahyä  '^ii I  2);  Sing,  und  Plur.i  yi  .  .  varidayoSä  vTtn?r?ncaiti  (sd.)  Y.31.  1;  —  ^un  ''^ä yqm  nasdi/tqnt  '^qm  dr»^a  iax/ai ff.. (sd.)  amar/antis  ya  ahhe  Yt,  sf).  la;  — drufim ^■5'>-Z'>  — yä^a  ■  ■  v?hrkqm  azr5.dai)tTm\iti~barat  asahe  haca  ''iabyS  Yt.  ig.  93;  — fsd.)  -iaw  avi  frafiaiaiti'y.  18. 6 $'•'>■,  N.  —  s.  noch  Vt.  6'.  i  (unter  z).  a)  auch 3'Q);  —  spämm  dd^tm  ..''i^anqm  Aar»-  mA  astvanh  Adj.:  ktmat  atiAsus  astvatS ^räi  V./y.39";  — yesi  narü  ..  kafa  aoi  .  .  '''^abyö  *  astvaitibyS^^  asake  ^.13; ''iäbyS  pain.iri>:yeiii  Vd.  13;  —  cval  ns  —  gandartwim  , .  y3  apatat . .  m»r»xlam ä^rata  (sd.)  a>aurun?m  haca  *'%äbu^'>  °^J  astvaifiS  alake -Hx.  iQ.  i,\ ;  V./iV.  55, *parayät  N.  4;  —  yS  ^yujyasfim  //a.ft  .  SrB.j;  —  dar7sca(sd^  ddisat'^amfrixsyan- '"iabyd  paräiti    V.  13.  17**;    —  yas)  tat  tim  vTspqm  yqm  astvaiHm  gai'iqm  Yt.ig.
10242:•  j.  garad-  V.  'gradi',  nur  mit  Praev. Praes.  i  g>r>d-.
10322:—  '%a  *sravayD  yasmm  yaz>ntim  paitisiaiii (sd.)  ..-%anqm  *sravayamnanqm  paitisti . . N.22;  —  'hih/a  iravayS  apas.'a  ..yaamnS H.  2. 1 3 ;  V.  jÄ  9 ;  —  zara'^uslrpui  , .  °%asfa srävayatitsm  Y. g.i;  N. 48;  —  '%anqmca srao^nm  Y.^,4,  d-i.  22.3;  —  frasrüifi •'ianqm  V.  12.  2;  —  ia/  asti  .  .  'hanqm kank^riitis  Y.~i.i;  N.22;  —  yö  °%anqm anumaiti  (sd.)  va  *anumainyeie  N,  2j;  — y5..anyS  va  kl  dahmö  sruik  '%h  daiaiti *ralu/ris  atruta  (sd.) ..  N.  2^;  —  aiwyäita (sd.)  mazdayasna  '"iä  sr-lvayat  nsil  anaiw- yasta  N.(?5;  —  yS  '>a  srävayeiti  apö  va paitisj^aiiie{%A.)  . .  N.  26;  32;  —  iauAqm na  'ianqtn  srutanqm  aratu/ris  {sA.)i  *ya *maixS  va  ..  srävayeiti  N._37;  22',38,3q;
10531:•  j.   xad-  V.,   nur  mit   vi  'auseinander quetschen'.     Praes.  2  xala-.
12290:ai.  TgL  tüfnadaiti/lra-  Adj.,  mm  V.  äaJa/i 'beissl';  s.  tiädifiura:  —  *difslra-  statt  'dqSlra- nobl  in  Anletuiang  an  einen  KS.  *äSdqi 'schaifiälmig'  aus  •flSin/-  {al  iüä-dan),^  »gl. danlan-  und  tilidälä;  daitika-.  —  Npü.:  rti dan^n.
12588:i)  'brennen  (tians.)  sva.  durch  Brand versehren,  schmerzen':  *iiait^'*  sT  mqm miavata  daxia  ydha  ana  .  .  P.  22;  F. j4-  3)  'verbrennen  (trans.)  sva.  durch Brand  vernichten,  aufzehren':  ya^a  ätari\ huihm  a^mtm  . .  aipiMnntaiti  Aävayeili . (sd.)  daiaiti  Y.  71. 8.
12590:mit  kam  dnwS.  2 :  ätari  hanäaiaiti  *asca ustäiumca  V.5, 9.
12648:(sva.  da&vah'):    urva^pm  staotär^m  van- hatikam  (sd.)  '%B  aoxta  ahurS  mazda    Y. 10.  9, Zum   V.   da-;    red,  Bildung;    vgl.   Wii.   Gr.' S  114S.  4.  —  ai.  'dada-,  'dadha-  Adj.  —  Pü. : ausgelassen;  Sü.  (zu  V.):  adadäm. j.  ddiaöis  Vyt.  $0:  lies  ditöii;  i.  'dä(y); g.  dadaiti,  dada/,  daduyi  usw.,  Verbalf. :    s.
13176:yesnya  AauniaiiA.)  *daiaiti  N.J7;  P.,J2;
19578:•  j.  'mad-  V.  'sich  berauschen'.  Fraes.  2 ma^a-,  24  mahaya-.  —  PPfP.  °masta-'^.
19581:•  j.  ^mad-  V.  'zumessen'.    x-Aor,  i  mas-. 'zumessen,  zuteilen':  asakya  ysm  (sd.)
20055:•  g.  marad-  V.  'verderben'.  Praes.  3 mand-,  9  mSrmda-''^.
=== asa- ===
2053:Dabei  sind  die  anaptyktischen  und  epenthetischen  Vokale  des  Awestischen  — die  im  Grundriss  der  Iran.  Philologie  mit  überhängenden  Buchstaben  gedruckt  sind  — , sowie  der  ergänzte  Nasal  und  das  ergänzte  h  (ausser  vor  ü)  des  Altpersischen unberücksichtigt  geblieben;  desgleichen  die  Quantität  woz-ftchliessender  Vokale.
2533:*'te  *yffi'^  fracarinti  , .  aiialiqm  .  .  N.  ,paiqn  ,  ,  'na  ,  ,  triltm  k>hrp}m  hvan.- ^.  III)  In  folgenden  Fallen  brauchen  i  t/arwr« -f?rv«aii/V.  5. 13,  3)  'dann'  im wir  den  Sing,  mit  'ein'  (unbestimmter  Ar- !  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Plur.  artikellos  (vgl.  ^aisa- 111}  j  dessen',  einen  Zwischensatz  hinter  einem yesica  .  .  upairi  'l^m  iristim  .  .  Ajr^zy^lf '  SaU  mit  yai  einleitend:  y^i  ndii  nidan- yaia  .  ,  "und  wenn  (man)  .  .  auf  einem  sayilnte  —  ''ja  kl  alte  sünö  vä  .  .  fraja- Toten  ..  liegen  lässt  .  ."  V.5.61;  — yö\s,yi>  —  kä  Af  asU  äiaX.ö.^T,  —  yaii'a vastnm  upaiiharizatti  upatri  °t»m  tristem  |  vaoeäp  aiSö  m7  Aanqm  .  .  p3r>saKuAa  — "wenn  einer  ein  Gewandstück  auf  einem '  "'la  ae^a  y<J  kaine  hanqm  . .  p?nsaili  , .  — Toten  liegen  lässt"  V.Äaj;  —  bei  rela- 1 'ort  assa  yS  kaine  altahmat  puir.lt  *mi- tivisch  angeschlossenem  Nomen:  yat  "te^  manxlstti  —  '^Aapanta  .  .  vfri^qn  .  . yöi  tnazdayasna  . ,  taci.apaya  nasSum  fra-  [  V.  /J.  1 3  f. ;  —  yeii  mit  Aari^nm  baraili jasqn  "wenn  Mazday.  auf  einen  Leich-  -  "da  aisa  yö  afirinüyakö  adJityö.an- nam  in  fliessendem  Wasser  stossen"  V.  6.  Aarj^nin  (sd.)  iri^ät  —  ^'>para  A!  iri- 26;  <y.73,  7-36.  \sittt5  rais?m  cikayat  .,  V.7j.i6.
2561:'''tt  *yöP^  fracarmii  . .  aitaSsqm  .  .  N.  patan  .  .  'oa  .  .  agtJm  k>hrp>m  hvar».- ij.  III)  In  folgenden  Fällen  brauchen  j  i/awjrjw  fo/vwuc/ V.  5. 1 3.  3)  'dann'  im mir  den  Sing,  mit  'ein'  (unbestimmter  Ar- 1  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Flur,  artikellos  {vgl,  ^aila-  III) '  dessen',  einen  Zwischensatz  hinter  einem jcsVJ  .  .  upairi  'tim  iristim  .  .  k>r>zyllt.  Satz  mit  ytzi  einleitend:  ye:i  mit  mdart- ya>a  .  .  "und  wenn  (man)  .  .  auf  einem  l  sayanfe  —  'ca  he  alte  sünS  vä  .  .  fraja- Toten  . .  liegen  lässt  .  ."  V.  5. 6 1 ;  —  /^ ,  JiW^  —  kä  hl  asti  Wia  V.  6".  47 ;  —  yesila vastnm  upaifharizaiti  upairi  ^tfm  iristtm  ^  vaocät  aSsö  nä  hanqm  .  .  p>r?sat3uha  — "wenn  einer  ein  Gewandstiick  auf  einem  .  '<,a  aSsa  y.J  kaine  hanqm  ..p^nsititi  . .  — Toten  liegen  lässt"  V.  ^'.23;  —  bei  rela-,°ö(J  a^ia  yä  kaine  aetakmut  puir-at  *mi- tivisch  angeschlossenem  Nomen:  yat  °te\mar?x^iliti  —  '^hat<anta  .  .  7>)r?zyqn  .  . yei  mazdayasna  . .  taH.apaya  nasHum  fra- '  V.  /5. 1 3  f ;  —  yai  nöii  har^'^nm  baraiti jasqn  "wenn  Mazday.  auf  einen  Leich-  —  °ofl  aila  yS  ap^rinlyükö  adaityo.at3- nam  in  fliessendem  Wasser  stossen"  V.  6. '  harsirim  (sd.)  iriiyäi  —  ^para  he  iri- 26;  ^.73,  7-36-  \Hntö  raSsim  cikayat  ..  V./j.iö.
2596:messend,  ibiablend';   Bthl.  IF.  /.M38.  -  "at     \.'J5.9;F.7;  —  tat    n  1  Jac^-aras': rl
2685:sat  Kiof);  —  ^kahmai  (s  'vahmi  paüi  .  j.  aevandasa-  Adj.  'der  elfte':  garayd va^Ö  ..  H.  /.  I  s>;  —  yo  g,l%aHqm  dyim  ■>  uzuxiyqn  .  .  'sß  .  .  dvadasS  .  .  Yt.  /p.  2 ; väcim  apayäUi  "vqm^vä  vacastalnm  N.  /.8_  vl/^.g,  5.29  (statt  AS.J;  —  ^ssm 42;  *42,  43;    —    'vo    akunö    vairyS   ..   asar^hamca  V.V.ij.
2805:aedasa-  Adj.  'suchend,  ausgehend -',  mit  Akk.:  töi  narjpi/  *an>ßs  'sa einen  Sau,  substantivisch  in  Kongruenz  |  (pjpm.)  äijit.arpm  p»sö4anv5  ka  asavä mit  dem  Praedikat:  astuyi  damam  {^^Mahurö\tA.)  yi  Ts' . .  Ä3mihyäJ (sd.)  "sie,  die '/J  as/i  dainnya  . .  äsiailir  (sö.)  Y.  J2. 9 ;  i  darauf  ausgehen  die  Würdigen"  herabzu- —  yat  hl  nr'tp  fr9dvo.st?hamm (sd.)  ..'^^ setzen,  die  Missächter  des  heiligen  Rechts, zi  asti  äiiiya  kata  (statt  NS.)  aetake  yat:  djg  jjjren  Leib  verwirkt  haben  -;  wo  ist irisiahe  ".  .  so  (wie  beschrieben)  ist  die  der  .  ."  V.  \J.  9". vorschriftsmässige  Kammer  für  den  Leich- '     Zum  Praes.  14  des  V.  'a?/-.  —  Vgl.  üaia-,  —
3374:'sd.)  sacinte  "ija  aiwi.game  V.  5. b)  'drum,  so  —  denn',  vor  Imp., Inj.,  Konj.,  Opt  und  Inf.:  tsmca..  laibyo dat  sarim  °%a  Asm  foraSua  %wa  xra^toä ^-  53-3'  —  "^'i  ^^'  västs  (sd.)  xsmat anyö  'äa  möi  sqs/a  (sd.)  veAs  vastrya  Y. 2ij.i;  3l.iS,34-7i —  °^«  «f  ii  humayd.- tara  anAm  Vr,  72.4;  4;  ~  "'ia  tu  n9 gayasca..Rya  y,4'-S'> — "^^  »■'  sasdyai (sd.)  usia  V.57. 16.  4)  anschliessend 'und';  a)  ein  Nomen:  i^a  i  Aaiiyaisd.) nare  "'^ä  jsnayö  Y.  5_J,6  3\  b)   einen
3439:urvata  saia%ä{%A.).,at  a»^r(sd.)..  "wenn ihr . .,  dann . ,"  Y._^0. 1 1 ;  46.  i  a ;  —  hyatcä m5i  mraol  .  .  /raxs>vm{s,d.)  at  tä  möi .. "und  ab  .,,  da  .."  Y.^^ia.  d)  hinter dem  Rel-T  yl ..  sardhuitr^m  rädanha  (sd.) .  .  xihäui  . ,  at  hui  mazda  aküm  (sd.) dadat\.46.\y,33.-i.  e)  hinter  einem konjunktionslosen  Vordersatz:  ivlzayai^ä (sd.)  magern  tsm  al  i'Jvay^Hsd.)  auhaitl.. "scheidet  ihr  euch  . .,  so  . ,"  Y.  53. 7.  II)  einen  selbständigen  Satz  i)  an- schliessend, üzw.  a)  zum  Ausdruck  zeit- licher Folge:  psr?sailj  ma  lis  ahil  .  .  al hsi  aopfsd.)..  "..  und  mich  fragte:  'Wer bist  du?..'  Drauf  sagte  ich.."  Y.4i^.7f.; —  at  3  (sd.)  vao'ai  ahurS  .  .  Y,  25. 6; 30. 6, 31. 1  o.  b)  zur  Hervorhebung  eines Gegensatzes:  adä  zT  ava  drBjd  ..  bavaill shndd  spaya'irahyä  (sd.)  at  asutJ  yao- ;anig{iA.) .,  "daraui  . .,  aber  . ."  Y.^o. loj  ^2.3,  43.16,45.^,  46.6,  47.3,  4f(.s, 4f).ti.  c)  zur  Begründung:  itStt  m pouri2s{sA.)  dngvatl  hyat  (ixsntds  at  tsi .  .  angr}rtg  (sd.)  *asaenJ  ädarS  "nicht soll  man  .  ,  Denn  alle  ,  ."  Y.  43. 15;  2.V. 1  o.  d)     einfach    anknüpfend    'und ' :
3441:7-axsya  isjw/j..Y.30.i; 4^.1-6.  ß)Konj. (Inj.):  at  i'S yaoja  zrvlslySng {sA.)  aun-alU V-SO.T,  4,  II,  43-4,  44-so;  —  al  hsi vakming  .  .  nidamä  Y.45-8;  2t}. $,34.^; — ma  äl  at  vs.  .gssta  Y. j j.  1 8  ■>.  t)  I"»P- (Inj.):  at  ySng  .  .  vSistl  .  .  pn'iriling  ffiÄ.) .  .  aabyS  pprpna  apanais  (sd.)  iairtjm  Y. 2fl.  10;  25.11,  43-9, 10;  —  mazda  al  moi ..raora  Y.j^.ij'*.  &)  Opt.:  at'hvs .. vahyö  na  aibi.jamyV  Y.43-  3-  lU)  einen Satzteil  anschliessend;  a)  zur  Hervorhebung des  Gegensatzes:  ya>aca  ai^kat  apitmnt
3455:atcit  . .  "wenn  auch  .  .,  so  doch  . ."  Yt s)  einen  selbständigen  Satz  ein- leitend, vor  Konj.,  unübersetzbar:  a/cTt aAmäi  .  .  ankaiti  Y.50.3.  3)  einen Satzteil  anschliessend;  a)  'und  zwar" :  panca- ahmi  .  .  ajcij  ahmäl  ya^a  .  .  av/ia^ niväitisisd.)^.  10.16.  b)  'aber':  agustJ (sd.)  . .  aäbyl  ySi  . .  atlu  a^bya  vakiltä  Y. 31.1.
3742:•  j.  apiäma.x'ar-  Adj.  'blindlings  essend': 'rS  (NSm.",  näml.  'ist  der  Hund')  yaia  |     "'  '  '■ t3yus  V.  /J.47;  47-  I  •  j-  aipy-öxSay-  f  'Hineinsprechen,  Ein-
3802:•  j.  aiwri.j'zärain  Absol.  'beim  Herzu- fiiessen':  ka(,a  x3  .  .  a/iam  yiJrqm(^V.) a'  "wann  werden  die  Wasserquellen  herzu- fliessend  fliessen?"  VtÄ  42.
4023:Besitz':  mSvA^m  ..  *'nauAunhm  Yt  7.5;  | 'nicht  vorwärts  fliessend':  apqm..y^para
4043:•  j.  a-fra'nharsza-  Adj.  'sich  nicht  er- giessend';  °sat  J>airi  xsudrät  "ohne  dass Samenerguss  erfolgt''  W.iG.id.
4538:•  j.  anu.zafan-  Adj.  'längs  des  Mauls, dem  Maul  entlang  gehend';  *usrB.az(t»S hisiinte  "faiiB  takahe  "(die  Rinder)  stehen da  Tränen  vergiessend,  dem  Maul  endang gehenden  Laufs"'*  Yt. /0.38.
5015:Pö,:  atac  rauh  a!  Jahun,  (So.:  anaeoguru- team  ;  ctL:  kis  gufl  fa  ävar  nt  daran.  — 'I  Der  Vertrae  durch  da»  blosse  Wort  (s.  V. *  3  und  in  urvaitya-)  setit  d«  gr&Hte  Ver- tnsn  in  den  Vertragtchli  essenden  Toram.
5265:I  mit  nt,  niy  i)  'herab(zur  Erde)kommeB, I -sinken':  vTsp>m  a  ahmltyataim  (tiyris) \paili.apayal  vazamnö  sl'amantpm  avi gat- Wlm  ^fanvaia  paiti  nirat'''  "bis  dass  er (der  Pfeil)  dahinschiessend  zum  Berg  X^. gelangte;  auf  dem  ?C.  kam  er  zur  Erde" Yt<?.38;  —  5.  noch  «r«  Inf.  2)  'herab- kommend sich  einstellen  in  — ',  mit  abiy und  Akk.;  siy.itis..  hauvciy  t^urä  nirasätiy abiy  imäm  vi^am  "Wohlbehagen  ■ .  (es) wird  sich  durch  Ah.  einstellen  in  diesem Haus"  D.  5.3.
5924:•  j.  *asrü.azan- '*  Adj.  'Tränen  (treibend sva.)  vergiessend' :  'z3nS  (NP.)  hilt>nte anuxajand  (sd.)  takahe  Yt.  JO.38.
6178:•  j.  a£a.''näsa-  Adj.  'wofiir  man  das (höchste)  Anrecht  erlangt";  kö  paitisanai gaomata  sasta  .  .  °näsa  lUmaaAa  Yt.  13. 50.  -nasim  als  Inf.  s.  bes.
6459:•  j.  aätadasa-  Adj.  'der  achtzehnte': dasjmS  yat  ahmt  sJ'ärtS . .  °sa  (statt  NSm.) baiiatya  Yt.  /.  8.
```


## [2026-09-05T20:18:52.840Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3236,3256p' BRT.txt"
}
```


### [2026-09-05T20:18:52.883Z] TOOL RESULT

```
•  p,  *ada-kiy  '*  Adv.  'damals'  r  imaiy  mar- tiyH  tyaiy  ad'  avads  äAa'til  yätä  . .  "das sind  die  Männer,  die  damals  dort  (dabei) waren,  als  , ."  Bh.  ^i8;  i8,  2.4,  6,
kty  hervorheb.  Part.,  eig.  IS.  in  'Aif- ').  ~  lat. '^ttl(ßtqm);  ai.  vgl.  •kirn  {aklm);  %  2l8.  3,  415. —  I)  NA.  'kaiy,  womit  Thumb  KZ.  J2.  125, WN.  KZ.  33.  22  ET.  «.  (,:r«  ^«\  eig.  LS.  zu idg.  *ko-  lusammenM eilen.  (Die  Buchstaben des  Wortes  stehen  gegen  WZKM.  3.  150  fest, Tgl.  ZDMG.  ^.  297  .\o.  3.)  —  ä)  Vgl.  iyaakal.
•  \.  yä  "aSaoaDhe')  N,j5. Pa.!  fehlt  —  0  Var.  ataohf.
•  p.  adam:  s.  unter  azim.
•  j,  adav-  (,  p.  adav-)  f.  'Wasserlauf; Bach,  Kanal':  us  . .  apqm  °oavd  apaiti.- »nti  Jasanti  Yt  Ä  29.
KompA.  —  Ob  lu  ai.  nadf- 1  'FIuss'?  Anders JusTi  ZDMG.  j/.  246;  B.  aber  lu  (liiaan-.
•  j.  a-8avay-  Adj.  (auch  mask.)  'der  keinen Trug  übt,  nicht  trügt,  betrügt':  *''T'r/(NSm.) nama  aAmt  *vtöavl/  nqtna  ahmt  Yt.  /.  14; —  n^mö  voku  °vim  (ASm.  statt  n.)  aibai- hm  Vr. 21. 3,  Yt  luz;  —  yeiihe  vähm Äangryuinäili  "vil  (NSf.)  paoirls  (sd.)  .  . i4ä  *dämya  (sd.)  xlaztäi  Yt.  iO,  143.
Pü.  (m  Yt.  7):  afrlfak,  erl. :  kaiän  ni  frfpim, (lu  Vr.  21)-.   adamak  (lum  V.  dab-,   vgL  aiao-
•  j.  aSara  Adv.:  s.  t^ara-.
•  j,  aSara-  Adj.  i)  'der  untere,  unten  be- findlich':   'rO  F.jg;  —  -rat  naimlt  "an
der  Unterseite,  unten"  V.  14.  7.  a)  IS.
'ra  als  Adv.  'unten,  untenhin':  nsmattha  °ra diia . .  upara  data  Yt.  lo.  1 1 8.  b)  ASa 'rtm  als  Adv.  'nach  unten':  at.kisca  .  . yai  *'r3m^^  aiwyankayanti ..yezi  *upar>m ". .  wenn  sie  sie  (von  oben)  nach  unten  an- ziehen . .,  wenn  (von  unten)  nach  oben  . ." N.53.  2)    'von    unten,    vom  Tiefland
herkommend',  d.i. 'westlich':  vät>m  'r?m ..  upanm  ..fratanm  ..pasiqüTm  "den westlichen,  östlichen,  südlichen,  nördlichen Wind"  S.  2,  jz;  —  vätaAe  ..  'rohe  S. 7.22.
KompA.  —  Vgl.  aiaiti.  —  ai.  aJiara-  Adj., np.  -»gl.  «>»).    —    Pü.   (lu  S.,    N.  52):    alar,\
(sonst):  Aa^aiarfiiemai).  —  ')  Hda.  asarim.  — >l  Das  wäre  j.  haca  aiatäf  (mp.  Aa^aiar,  Pli.
•  j.  aüara-naema-  m.  'die  untere  Seite'; nur   Abi.   °mit  'von   unten   her,   unten':
urvaiö  (sd.)    °milt    . .    upara.namni    Yt
74  19-
Npü.:  az   larf  i  lakl.
•  j.  ajlaram  Adv.:  s.  t^ara-.
•  j.  adairi  Praep.  'unter,  unterhalb';  i)  mit Akk.:    ao'  hax>m  nivöiryeite  V.  <¥.  69;  —
```


## [2026-09-05T20:19:01.727Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"V\\.  'essen\\|V\\. 'essen\\|'essen'\" BRT.txt | head; echo ====; sed -n '3165,3180p' BRT.txt"
}
```


### [2026-09-05T20:19:01.783Z] TOOL RESULT

```
Exit code 1
10288:•  j.  gah-  V.  'essen;  fressen',  uzw.  von i/iiAischen  Wesen'',  Praes.  2  gatsha-, 4  gäffha-,
10289:'essen',  von  den  Dasva:  aste  yöi  dagva aitaisva  daxmaisva  gan/i)nti  apäca  vae- pmH  ya>a  .  .  V.7.SS.
(eval):1: === not found
```


## [2026-09-05T20:19:03.829Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3168,3180p' BRT.txt"
}
```


### [2026-09-05T20:19:03.873Z] TOOL RESULT

```
a£i$t%e
flim  das  AUeischlechteste  und  stinkendste lu  Teil  werden  .  ."  ^.40;  —  mit  Inf.: y>  't)m  *vainariAe  (sd.)  aogidä  gqmcä  .  . hianiä  V.?-'.  10.  a)  bes.  van  an/iav- (sd.);  Aaia  -tat  auhaot  Y.7J.15; — okAus 'lö  V.jo,  4;  —  äi'a  't)m  aüa  ähüm  ä V-53S;  FrW.j.a;  —  -täi  auuhe'^.i,. 61.  A)    in    religiös- moralischem  Sinn:
Uta  %rayam  vahiltanqm  amiiyS  (sd.) bw^ata  . .  "^raj/am  'tatiqm  aiwi'hyö  buyata V.J.V  17;  —  'y,i  maiyä  Uä  (APn.)  daniö vaxhnii  dagi5jsuitif(%A..)  Y._32.  4; —  aya *mainiv3  varatä  (sd.)  yi  dngvH  'tä Timyö  . .  Y.  30. 5 ;  —  yi  ..  yazli  apä  . . 'bm    mantüm    (sd.)    Y.j;^.  4.  a)    mit
manaA-  n.  (sd);  hyat  v?T}niltä  (sd.)  'I}tn manS  Y.jo.ö;  —  ya  x/ä^rä  grihmö hiiatal  (sd.)  'tahya  d^mum  manatthö  Y. ^2.13.
SuperL  in  ata-.  —  Pü. ;  i'atlar,  Valium,  valtar- lum.  —  '»  Im  Gegens.  zu  t-ahiiiii:  —  ')  ilds. aulT-iraniim,  aber  Pü.;  lalldrlum.
•  j.  a-£istäe  Inf.  'zu  speisen,  zu  essen': ya  pipi^wa  vasö  a^  "feste  Nahrung  darf man  nach  Belieben  essen"  N.  (>2.
Zu  einer  w.  Basis  *t'äxs-  (mit  ö);  i  aas  > '}.  — VgL  mp.  (äil,  eäilai  'Mahl'  (N.  64),  np.  !ä!t, xna.  LW.  r'aL  —  fu.-./nt  i  fuxt  pa  kämak  x^a- rii>/^Vi\  pa  iirVi.  —  ')  Uhlenbeck's  Elyroo- logie  WAiSpr.  90  ist  falsch.
j.  ajayaui^aya  H-SJ:  Wei  a/nyaiinia  aya;  i. grai-.
j.  ajiuiyamnäi  Yt.  S.  49 :  lies  ajiiy'.
•  j.  a-]asta-  Adj.  'ungebeten'  sva,  'uner- wünscht, verhasst';  pailistälie  °taca  zöiz- distaöj  . .  xrafsira  Yt.  11.  i.
PPfP.  Eom  V.  s'"'--  —  Vgl.  np.  iiijaiia.
•  j.  a-]astay-  £  'Nichtbitte':  yat  nil  kasz'i- kqm.'ina  . .  'ta  (LS.)  . .  daoäiti  "wenn  er bei  Nichtbitte  (sva.  'ohne  darum  gebeten zu  sein')  '>  . ."  V.  /Ä37.
PL:  ia  tu  iasl.  —  ')  S.  lAiudr.  BthL.  IF. p.  156.
```


## [2026-09-05T20:19:12.007Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3200,3216p' BRT.txt"
}
```


### [2026-09-05T20:19:12.068Z] TOOL RESULT

```
Ableil.  aus  'a-,    Bthl.  IF.   lo.   14.    —    Fü.:
•  j.  *aiti(-ö(J/i7v-) "  f-  'Beiseitelegen,   Be-
dby  Google
55
ad-
adaoyamna-
5«
seitigen' :ya%a  nöil*aiti  nüsitica'^ *airi^a "dass  sie  nicht  durch  Beseitigen  und  Ver- bergen Schaden  nehmen"  N.  6j  (?).
Pü.:  undeutlich.—  ■)  Hds.  a^ti  nü;  s. No. s.
—  *)  Abkürzung  aus  ailihäili  niiSilii'a;    s.  zu
•  j.  ad-  V.  'sagen'.  Praes.  24  aoaya-,^ 30  (Iter.)  aiaya-,  PrP.  J»w;  Perf.  nJ:
'sagen':  äla  (sSPfA.)  F.-K;  —  mit ui/i  is±):  aöaica  (iSPfM.)"'  uiti  V.4.47, N._J7.  a)  Pass.  'genannt  werden,  heissen', mit  dopp.  Nom. :  yäia  . .  akarana  anayra asaonö  sfif  aili  Yt.Ä48.
mit  paiti  i)  'etwas  (Akk.)  beantworten, worauf  antworten':  paili  //  (als  Akk.) Shaydit  aSsa  paiti.irista  tumascS..  "darauf soll  der  Verunreinigte  antworten:  tum" ." Y.g.i2.  1)  'Jmdm.  (Dat.,  Gea)  ant- worten auf  — '  (Akk.),  im  kirchlichen Wechselgesang:  äaj  *atravaxsaAe {sd.)  yal ,.  zaokralca  vacim  failiMoaySi  aHä  ratus N.  7J;  72  (wo  paiti.aoayät);  —  aoäj  an- yalsqm  rähivqm  (nämL  väam)  paiti.äla- yöit  "darauf  soll  er  (der  Zaotar)  den  Ä.s auf  der.  andern  Seite  (auf  Ihren  Gesang) antworten"  N.  83.         [S.  noch  paityäüa-^
mit  pairi  'aufsagen,  hersagen'  (die  Gä- 'kä%):  *yöi  glü^i  ..srävayanti yezi  arastnm (sd.)  pairi.aoxta  pairi.äaa  vä  . .  pasla  vä parö  Vä  pairi.äm  aratufryö  ".  .  wenn einer  .  .  (die  GiJääworte)  zu  spät  oder  zu früh  aufsagt,  die  sind  ar."  N._J2.
ai.  aha  (Pf.);  s.  Gdh.  KZ,  ja  3^3,  Cld.  KZ.
33.  466,  Hbm,  IF.  4.  117.  —  Vä.:  guflaa,  (mit
paiti):  pasax"  guftan,  (mit /lain):    apt  gußati,
```


## [2026-09-05T20:19:30.813Z] TOOL CALL #74: WebSearch

```json
{
 "query": "Avestan adāiti \"to eat\" subjunctive Bartholomae ad- Yasna"
}
```


### [2026-09-05T20:19:39.053Z] TOOL RESULT

```
Web search results for query: "Avestan adāiti "to eat" subjunctive Bartholomae ad- Yasna"

Links: [{"title":"Old Iranian Online - The Linguistics Research Center","url":"https://lrc.la.utexas.edu/eieol_master_gloss/aveol/16"},{"title":"AVESTAN LANGUAGE iii. The Grammar of Avestan - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/avestan-language/avestan-language-iii-the-grammar-of-avestan/"},{"title":"AVESTAN LANGUAGE iv. AVESTAN SYNTAX - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/avestan-language-4-syntax/"},{"title":"AVESTA: YASNA: (English)","url":"https://www.avesta.org/yasna/"},{"title":"Avestan","url":"https://en.wikipedia.org/wiki/Avestan"},{"title":"Old Avestan: Yasna 29, the Cow's Lament","url":"https://lrc.la.utexas.edu/eieol/aveol/10"},{"title":"Introduction – Part 2: Avestan texts and ritual practice Avestan ALMUT HINTZE","url":"https://spw.uni-goettingen.de/projects/aig/doc/AVE-INT-002.pdf"},{"title":"Old Avestan: Yasna 29 (continued)","url":"https://lrc.la.utexas.edu/eieol/aveol/20"},{"title":"Yasna","url":"https://en.wikipedia.org/wiki/Yasna"}]

I found search results related to Avestan language, Yasna texts, and Christian Bartholomae's work on Avestan grammar and translation. However, the search results don't contain specific information about the Avestan verb *adāiti* ("to eat") or its subjunctive form in relation to Bartholomae's work on the prefix *ad-*.

The results do provide general context about:
- Bartholomae's work on Avestan language and Old Persian
- Bartholomae's translation of the Gathas in his work "die Gatha's des Awesta: Verspredigten" (Strassburg, 1905)
- General information about Avestan verb forms and subjunctive mood in the Yasna texts

However, to provide you with the specific etymological or linguistic information about *adāiti* and Bartholomae's analysis of the *ad-* prefix, you would likely need to consult Bartholomae's original scholarly works or specialized Avestan language references that discuss this particular verb and its prefixation patterns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:20:04.929Z] TOOL CALL #75: WebSearch

```json
{
 "query": "Syriac \"pespestā\" OR \"ܦܣܦܣܬܐ\" aspastā lucerne Arabic fiṣfiṣa Aramaic loanword Middle Persian aspast"
}
```


### [2026-09-05T20:20:13.509Z] TOOL RESULT

```
Web search results for query: "Syriac "pespestā" OR "ܦܣܦܣܬܐ" aspastā lucerne Arabic fiṣfiṣa Aramaic loanword Middle Persian aspast"

Links: [{"title":"SYRIAC LANGUAGE i. IRANIAN LOANWORDS IN SYRIAC - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/syriac-language-i/"},{"title":"فصفص - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%81%D8%B5%D9%81%D8%B5"},{"title":"GEORGE A. KIRAZ TOWARDS A LEXICON OF SYRIAC LOANWORDS IN CHRISTIAN ARABIC","url":"https://bethmardutho.org/wp-content/uploads/2020/07/Kiraz_2018_Towards-a-Lexicon-of-Syriac-Loanwords-in-Christian-Arabic.pdf"},{"title":"Reconstruction:Proto-Iranian/HacwaHastiš - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/HacwaHasti%C5%A1"},{"title":"(PDF) Aramaic (Syriac) Loanwords","url":"https://www.academia.edu/8557402/Aramaic_Syriac_Loanwords"},{"title":"List of loanwords in Assyrian Neo-Aramaic","url":"https://en.wikipedia.org/wiki/List_of_loanwords_in_Assyrian_Neo-Aramaic"}]

Based on the search results, I found relevant information about this etymological chain:

The Syriac word ʾspstʾ means "alfalfa, lucerne" and is a loanword from Middle Persian aspast. The Arabic fiṣfiṣa (فِصْفِصَة) was borrowed from Aramaic ʾaspastā (אַסְפַּסְתָּא), which itself derives from Old Median *aspāstiš meaning "lucerne".

The Classical Syriac form ܐܣܦܣܬܐ (ʾespestā) is attested as a reflexes from Proto-Iranian, and it also gave rise to the Arabic forms fiṣfiṣa, faṣfaṣa, and fisfisa.

The etymological origin traces back to Proto-Iranian *HacwaHastiš meaning "lucerne," literally "horse-food" from Proto-Iranian *Hácwah ("horse") and Proto-Indo-European *h₁ed- ("related to eating"). This word was adopted by the Babylonians after the Akkadians borrowed it following the Medes' cavalry models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:21:00.743Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B5%D9%81%D8%B5",
 "prompt": "Give the full etymology of Arabic فصفص / فصفصة: the Aramaic/Syriac forms cited (with transliteration), Old Median / Proto-Iranian forms, and any references (Löw, Ciancaglini, etc.)."
}
```


## [2026-09-05T20:21:02.155Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/HacwaHasti%C5%A1",
 "prompt": "Give the reconstruction, meaning, morphological analysis (components), and full descendant list including Old Median, Middle Persian, Syriac, Arabic, Spanish, English."
}
```


### [2026-09-05T20:21:08.213Z] TOOL RESULT

```
# Etymology of Arabic فصفص (faṣfaṣ)

## Aramaic/Syriac Forms
The word derives from Aramaic _אַסְפַּסְתָּא_ (ʾaspastā) or Syriac _ܐܰܣܦܷܣܬܳܐ_ (ʾaspestā), meaning "lucerne."

## Etymology Chain
The term traces through multiple ancient languages:

1. **Akkadian**: _aspastu_ ("presumably lucerne")
2. **Old Median**: _*aspāstiš_ ("lucerne")
3. **Proto-Iranian**: _*HacwaHastiš_ ("lucerne," literally "horse-food"), composed of:
   - _*Hácwah_ ("horse")
   - Proto-Indo-European _*h₁ed-_ ("related to eating") + _*-tis_

## Historical Context
According to the entry, "the Assyrians having it borrowed when modelling their cavalry after the Medes and thus taking over this name for a plant serving as horse food."

## Key References
Scholarly sources cited include works by Immanuel Löw (1924), Berthold Laufer (1919), Muhammad A. Dandamayev (1992), and entries in the Comprehensive Aramaic Lexicon Project and Assyrian Dictionary of the Oriental Institute.
```


### [2026-09-05T20:21:09.876Z] TOOL RESULT

```
# Proto-Iranian *HacwaHastiš

**Reconstruction:** *HacwaHastiš

**Meaning:** "Alfalfa" or "lucerne"

**Morphological Analysis:** This term combines "*Hácwah" (horse) + "*Hástiš" (food), ultimately derived from Proto-Indo-European "*h₁ed-" (to eat) with the suffix "*-tis"

**Major Descendant Line:**

The word traveled through multiple language families:

- **Old Median:** "*aspāstiš"
  - **Middle Median:** "*aspast" (intermediate form)
    - **Middle Persian:** attested in Book Pahlavi script
      - **Classical Persian:** "اسپست" (aspist)
        - **Modern Iranian Persian:** various forms including "espest," "aspest," "sepest"
      
**Extended Descendants Through Persian:**
- **Syriac:** "ܐܣܦܣܬܐ" (ʾespestā)
  - **Coptic:** "ⲡⲉⲥⲡⲉⲥⲧⲁ" (p-espesta)
    - **Arabic:** "فِصْفِصَة" (fiṣfiṣa), "فَصْفَصَة" (faṣfaṣa)
      - **Spanish:** "alfalfa"
        - **English:** "alfalfa"

This etymological chain illustrates how an Iranian compound term entered European languages through Semitic intermediaries.
```


## [2026-09-05T20:21:27.956Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"^etch,\" \"^edible,\" \"^denture,\" \"^tusk,\" \"^tooth,\"; do echo \"=== $w\"; grep -n \"$w\" KLN_1966.txt | head -2; done"
}
```


### [2026-09-05T20:21:29.646Z] TOOL RESULT

```
=== ^etch,
=== ^edible,
=== ^denture,
=== ^tusk,
=== ^tooth,
```


## [2026-09-05T20:21:32.379Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"etch,  tr\\|etch, tr\\|edible,  adj\\|denture,  n\\|tusk,  n\" KLN_1966.txt KLN_1971.txt | head -10"
}
```


### [2026-09-05T20:21:32.453Z] TOOL RESULT

```
KLN_1971.txt:85951:etch, tr. and intr. v., to engrave with acid. — Du. 
KLN_1971.txt:92102:fetch, tr. and intr. v. — ME. fecchen, fr. OE. 
KLN_1971.txt:94116:fletch, tr. v., to provide (an arrow) with a feather; 
KLN_1971.txt:233953:stretch, tr. and intr. v. — ME. strecchen, fr. OE. 
KLN_1966.txt:9614:Derivatives:  credential,  tr.  v.,  credentials,  n.  pi. credibility,  n.  — -  ML.  credibilitds,  fr.  L.  credi- bilis.  See  next  word  and  -ity. credible,  adj.  —  L.  credibilis,  ‘worthy  of  belief, credible’,  fr.  credere.  See  creed  and  -ible. Derivatives:  credible-ness,  n.,  credibl-y,  adv. credit,  n.  —  F.  credit,  fr.  It.  credito,  fr.  L.  cre- ditum,  ‘that  which  is  believed;  a  loan’,  pp.  of credere,  ‘to  believe’,  used  as  a  noun.  See  creed. Derivatives:  credit,  tr.  v.,  credit-able,  adj.,  ere-
KLN_1966.txt:10879:dentoid,  adj.,  tooth-shaped.  —  A  hybrid  coined fr.  L.  dens,  gen.  dentis,  ‘tooth’,  and  Gk.  -oetSrjc, ‘like’,  fr.  e!8o?,  ‘form,  shape’.  See  denti-  and -oid.  The  correct  form  is  either  odontoid  or  den¬ tiform.  (In  the  former  both  elements  are  of Greek,  in  the  latter,  of  Latin  origin), denture,  n.,  a  set  of  teeth,  esp.  a  set  of  false  teeth. —  F.,  fr.  dent,  ‘tooth’.  See  dent,  ‘toothlike  pro¬ jection’,  and  -tare.
KLN_1966.txt:12639:Derivatives:  edge,  tr.  v.,  edg-ing ,  n.,  edg-ing-ly, adv.,  edg-y,  adj.,  edg-i-ness,  n. edible,  adj.  —  Late  L.  edibilis,  ‘eatable’,  fr.  L. edere,  ‘to  eat’.  See  eat  and  cp.  comedo,  comestible, esculent,  obese.
KLN_1966.txt:13712:Etat  Major,  the  staff  of  the  army.  —  F.  etat- major,  fr.  etat,  ‘state’,  and  L.  major,  ‘greater’. See  etat  and  major,  adj. et  cetera,  ‘and  other  things’.  —  L.,  fr.  et,  ‘and’ (see  et),  and  neut.  of  ceteri,  ‘the  others’,  which is  formed  fr.  I.-E.  pron.  pref.  *ce-,  ‘there;  behold’ (see  he),  and  I.-E.  *etero-,  ‘the  other’,  whence also  Umbr.  etro-,  ‘another’,  Avestic  a-tara-, ‘one  of  the  two,  this’,  Alb.  jatere,  jatre,  ‘the other’,  OSlav.  jeteru,  iteru,  ‘some,  one’, etch,  tr.  and  intr.  v.,  to  engrave  with  acid.  —  Du. etsen,  ‘to  etch’,  fr.  G.  atzen,  ‘to  corrode’,  fr. MHG.  atzen,  etzen,  fr.  OHG.  azzon,  prop,  ‘to feed,  bait’,  causative  of  e$$an,  ‘to  eat’.  See  eat. Derivatives:  etch,  n.,  etch-er,  n.,  etch-ing,  ver¬ bal  n.
KLN_1966.txt:14623:fetation,  foetation,  n.,  formation  of  a  fetus.  — Formed  with  suff.  -ion  fr.  L.  fetatus,  pp.  of fetare,  ‘to  produce  offspring’,  fr.  fetus,  ‘a  bring¬ ing  forth;  offspring’.  See  fetus, fetch,  tr.  and  intr.  v.  —  ME.  fecchen,  fr.  OE. feccan,  earlier  fetian,  ‘to  fetch,  bring’,  rel.  to OE.fatian,  of  s.m.,  obsol,  E.  fet,  ‘to  fetch’,  ON.
KLN_1966.txt:19101:Derivatives:  increase,  n.,  increas-able,  adj.,  in- creas-ed-ly,  adv.,  increase-ment,  n.,  increas-er, n„  increas-ing,  adj.,  increas-ing-ly,  adv. incredibility,  n.  —  L.  incredibilities,  ‘incredibility’, fr.  incredibilis.  See  next  word  and  -ity. incredible,  adj.  —  L.  incredibilis ,  ‘that  cannot  be believed’,  fr.  in-,  ‘not’,  and  credibilis,  ‘worthy  of belief’.  See  credible  and  cp.  incroyable. Derivatives:  incredihle-ness,  n.,  incredibl-y,  adv. incredulity,  n.  —  F.  incredulite,  fr.  L.  increduli- tatem,  acc.  of  incredulities,  ‘disbelief’,  fr.  in- credulus.  See  next  word  and  -ity. incredulous,  adj.  —  L.  incredulus,  ‘unbelieving’, fr.  in-,  ‘not’,  and  credulus,  ‘credulous’.  See credulous.
```


## [2026-09-05T20:21:47.089Z] TOOL CALL #80: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK data/verification/sources/refs/ocr/SOD && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg147.png data/verification/sources/refs/ocr/BOOK/147.png && cat > data/verification/sources/refs/ocr/SOD/70.vision.txt <<'EOF'\n[read from the page image https://archive.org/download/SogdianDictionary/page/n135.jpg = printed p. 70 of B. Gharib, Sogdian Dictionary (Farhangan 1995); OCR of SOD.txt was unreliable for the hacek letters, so the entry was read directly from the scan]\n\n1764 'šm'x(w)  M                     شما\n     əšmax(u)  ©<*šmāxam  ⇒'šm'γw, šm'x\n     you\n     GMS 157, 1380; KG 332\n\n1765 'šn'kγ'ntyc  S        ماه پنجم سال (بیرونی: اشناخندا)\n     əšnāxandīč-  ⇒šn'xntyc\n     fifth month of the year\n     MDii Nov. 1R\n\n1766 'šn'ych ? ⇒ yγn'ynch ?\n\n1767 'šp'δy  S                قسمت، جزء ؟، کاسه، ظرف ؟\n     (ə)špăδč ?   ©Pers. āš ?\n     part, portion ?, bowl ?\n     Frag. Len. 60, 8, 69, 28-33; S W, BAI 1990, 286\n\n1768 'šp'yr  B                              غار\n     əšpēr ? ©*sparya ...\nEOF\necho saved; ls data/verification/sources/refs/ocr/SOD/"
}
```


### [2026-09-05T20:21:48.884Z] TOOL RESULT

```
saved
70.vision.txt
```


## [2026-09-05T20:21:56.950Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/alfalfa' --note 'page 147, root Ed, node 10: English alfalfa < Spanish < Arabic al-faṣfaṣa' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/HacwaHasti%C5%A1' --note 'page 147, root Ed, nodes 3-10: PIr *HacwaHastiš horse-food, Old Median aspāstiš, MP aspast, Syriac espestā, Coptic p-espesta, Arabic fiṣfiṣa, Spanish alfalfa' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%81%D8%B5%D9%81%D8%B5' --note 'page 147, node 7: Arabic faṣfaṣ/fiṣfiṣa < Aramaic aspastā / Syriac espestā, Löw 1924' 2>&1 | tail -2"
}
```


### [2026-09-05T20:22:00.396Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3957c14073214b5e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1520cda12d1a5898.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/507fc27754d0d8aa.txt
```


## [2026-09-05T20:22:00.842Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D8%B1%DA%A9%D8%B3' --note 'page 147, nodes 1-2: Persian karkas < MP kargās < Av. kahrkāsa- hen-eater' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A2%D8%B4' --note 'page 147, node 2: Persian āš, disputed etymology (Turkic *aš vs inherited)' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/alfalfa' --note 'page 147, nodes 3-10: alfalfa 1845, Watkins Old Iranian *aspa-sti- horse food' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ed-' --note 'page 147, root Ed: PIE *h₁ed- to eat' 2>&1 | tail -2"
}
```


### [2026-09-05T20:22:03.802Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/36775fbce7605c08.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a19b134825ef0550.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/01b2b5ab2d62475e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c15264ddbe2767e6.txt
```


## [2026-09-05T20:22:11.714Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"کرکس\\|ناشتا\" ARY_pages.txt | head -10; echo \"=== latin idx ===\"; grep -n -i \"^ED\\b\\|EDERE\\|KARKAS\\|ASPAST\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-05T20:22:11.780Z] TOOL RESULT

```
11959:۱ واژه‌های فارسی "کرکس " و اوستایی 1۸11816۸8۸ و سانسکریت 1678۸8۸ نیز از همین واجريشه آمده‌اند.
14580:۲ | ناشتا(به چم "خوراک نخورده")
14603:۱- واژه فارسی آناشتا" از پیشوندنا" (نشان منفی) و ربشه‌ی "شتا" (به چم "خرردن") درست شده است.
=== latin idx ===
302:ed ASAT ES pb ee phege GI Fale SULT 4 Soo lh ww y col
1766:[ Tra HOLD FRISIAN) e955. ESSE, EDERE (LATIN) op3¥
2371:THE AMERICAN HERITAGE DICTIONARY) ASPAST s(PAHLAVI) 5 hq
5299:ed yy pat jl PENER 359 SUPANIR 55 14)" 24" 05ly 245 Joel 4-1
12706:ed SLAG coe gh ool ay} slanly ool gets, WS cel sds BARNHART -)
14323:ETML, ET, ETIR HITTITE) uta EDO, ESSE, EDERE = (LATIN) 3
14497:SEDERE {(ITALIAN) gid NISHASTI, HAVESTAN) gles)
14511:SITTA (SWEDISH) (543 yo SEDERE, SEDES, ALATIN) 53
```


## [2026-09-05T20:22:13.132Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B4%D8%AA%D8%A7",
 "prompt": "Give the Persian entry ناشتا: etymology (Middle Persian form, components nā- + āšta, root), meaning, and cited sources."
}
```


### [2026-09-05T20:22:19.967Z] TOOL RESULT

```
# Persian Entry: ناشتا (nâštâ)

## Etymology

The Persian word has two etymological origins:

**Etymology 1 (Adjective):** Likely cognate with Sanskrit *अनाशित* (anāśita, "one who has not eaten, hungry"). An alternative theory suggests composition from *نه* (na, "not") plus a form derived from Proto-Indo-European *h₁ed-* ("to eat").

**Etymology 2 (Noun):** Derived from the original *ناشتایی* (nāštā'ī, nāštāyī), related to Etymology 1 above.

## Meanings

1. **Adjective:** Hungry
2. **Noun:** Breakfast (chiefly in Dari and Tajik dialects; Iranian Persian uses *صبحانه* sobhâne instead)

## Cited Sources

The Wiktionary entry references:
- "An Etymological Dictionary of Persian, English and other Indo-European Languages" by Ali Nourai (2011), page 117

This comprehensive dictionary entry documents the word's presence across Persian variants (Classical, Dari, Iranian, and Tajik) with detailed phonetic transcriptions.
```


## [2026-09-05T20:22:29.273Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && awk 'NR<=11959 && /\\[pdf page/{p=$0} END{}' ARY_pages.txt; for L in 11959 14603 ; do echo \"=== line $L ===\"; awk -v L=$L 'NR<=L && /\\[pdf page/{p=$0} NR==L{print p; print}' ARY_pages.txt; done; echo \"=== context 11950-11962 ===\"; sed -n '11950,11962p' ARY_pages.txt; echo \"=== context 14575,14606 ===\"; sed -n '14575,14606p' ARY_pages.txt"
}
```


### [2026-09-05T20:22:31.189Z] TOOL RESULT

```
=== line 11959 ===
[pdf page 401]
۱ واژه‌های فارسی "کرکس " و اوستایی 1۸11816۸8۸ و سانسکریت 1678۸8۸ نیز از همین واجريشه آمده‌اند.
=== line 14603 ===
[pdf page 491]
۱- واژه فارسی آناشتا" از پیشوندنا" (نشان منفی) و ربشه‌ی "شتا" (به چم "خرردن") درست شده است.
=== context 11950-11962 ===
انگلیسی (877لا5(70): ۴ 0 (۸136) با
دانمارکی (0۸(71873): دای ۱ 9 (۸33) 2
سوئدی (8750157): 16۸ 8 (816) :00/5
نروژی (۵/08۳8007: ۸1۲618 ,81۳65 0 (16) :57
ملندی (007777)+ نداد یلا۱4 لغت‌نامه دهخدا: ۱۸۳۷۳
اسلاوی کهن (4۲76ا5 7ل#ناتن) طام): پرهان قاطع : ۱۶۳۲

زان ناد ۱
یادداشت: :
۱ واژه‌های فارسی "کرکس " و اوستایی 1۸11816۸8۸ و سانسکریت 1678۸8۸ نیز از همین واجريشه آمده‌اند.
۲- چم این واژه در زبان پهلوی: قرقاول
چم این واژه در زبان‌های غیرایرانی و غیرهندی: غرید» غدغد کردن» صدای قورباغه ایجاد کردن. :
[pdf page 402]
=== context 14575,14606 ===
انگلیسی کهن (8۸۷01/577 012): 4 (اتغ۸ا) ادا ام
تکعه ی ۳۹ کفد ناه
!۱ انگلیسی ([60/01/3): ۸7 برهان قاطع + ۳.۸۹ ْ
دانمارکی (0۸7/574): دنا
[pdf page 491]
۲ | ناشتا(به چم "خوراک نخورده")
اوستایی (۸887:400): 1 ۱ هلندی (007070): ۰ ل
اوستی (0898716): 2 اسلاوی کهن (72بما5 2۳0807 010):
کردی (68.015): نا ۱ 7 بولا] ۸5[
1 تخاری ۸ (۸ [(۸ل702۸): ادن ۷ لینرانی (4(۷الدن577): 5/1 ,ت82 ,5871
سانسکریت (71:)54۸8/7 ۸۳11۸ ,۸041 لتونی (لتی) (701۵97بصل): 137
۸0۰ پروسی کهن (۳3۷05510 010): 17
ارمنی (۵742424): 1 ایرلندی کهن (1#/874 012): 1733781 ,155
برنانی (06240): گالی ([5/ل0۸): 5 ,5
8 ,0 بل501187۸ ولزی (57 )+ زان
لاین (/470): ۰ 8۵ط50 ,8555 ,800 هتبت (۳7]77175): اآ5 ,37/1
گریکه (0077710): ,17۸
ایسلندی‌کهن (/1010/۸140م8 2ا0): پسگشت‌ها دهدن ال
۸ از 0 را
ساکسونی کهن (542000 0ا0): 7۸ ماد (7هق) دای ان
: فریزی کهن (/۴/5140 010): 1۸ 4 (۸1۸3683) 05۰
آلمانی کهن (/(05294 07ات صطام): 327 ما8
122۸7 8 (8۸7) :0(/70(3
آلمانی (0870//0): ادن ] 7 (5ه5) ی
انگلیسی کهن (ل5لا800 ۰:02 81۸۲ برهان قاطع + ۳۹۹
انگلیسی (7ل3ا8(/0): ۸7 فرهنگ معین + ۳۸۳
سوئدی (97۷5/0157): 27۸
یادداشت:
۱- واژه فارسی آناشتا" از پیشوندنا" (نشان منفی) و ربشه‌ی "شتا" (به چم "خرردن") درست شده است.
۲- چم این واژه در زبان‌های این فهرست (به جز سانسکریت و زبانهای ایرانی): خوردن» خورد,
اوستایی (7ل۸۷287۸): م۸۸۳۸ پارسی باستان (/(۲88514 010): ۰ ۸۸۳۸7
[pdf page 492]
```


## [2026-09-05T20:22:42.682Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && awk -v L=2371 'NR<=L && /\\[pdf page/{p=$0} NR==L{print p; print}' ARY_latin_index_pages.txt; sed -n '2365,2375p' ARY_latin_index_pages.txt"
}
```


### [2026-09-05T20:22:44.540Z] TOOL RESULT

```
[pdf page 84]
THE AMERICAN HERITAGE DICTIONARY) ASPAST s(PAHLAVI) 5 hq
Ba jal ly cel tla 3 ry (ss! SEL) Don obaa! 9 te Gldks GAIT 9 zy eto
caylo ages Seo algljasie » gla! gobs 2
sabale raplalped 52 ajly gal eae
REFERENCES [eT *ASPO-ASTI HAVESTAN glu)
POKORNY ——~~—~S~*~*«SOS BT *ASPO., «(OLD PERSIAN) ileal 54
‘MACKENZIE: (CLOVER) 107 ASTI
THE AMERICAN HERITAGE DICTIONARY) ASPAST s(PAHLAVI) 5 hq
OF THE ENGLISH LANGUAGE: ASVAS-ADMI—:(SANSKRIT) < 4 Sails
(ALFALFA) 43 ASPO-UTEM ARMENIAN) + !
rr Spee Seah .
VW4-t¥e ‘gb dey
```


## [2026-09-05T20:23:56.266Z] AGENT

Now I have everything I need. Writing the verification file.


## [2026-09-05T20:30:48.301Z] TOOL CALL #87: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-147.json <<'JSONEOF'\n{\n \"pdf_page\": 147,\n \"book_page\": 117,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 2,\n   \"root\": \"Ed\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₁ed- 'to eat' (older notation *ed-), athematic present *h₁és-ti, with the participial derivative *h₁dónt-/*dnt- 'tooth' ('the biting one')\",\n   \"note\": \"Pokorny IEW 287 heads the entry 'ed- \\\"essen\\\"' and adds 'Nominalformen: ed-ono-, ed-men-, ed-uen-… ; edont-, dont-, dnt- \\\"Zahn\\\"', which is precisely Nourai's root box plus the tooth branch he draws under Germanic and Latin. Walde-Pokorny I 118 has the same headword; Watkins/AHD 1985 p.417 'ed-. To eat; original meaning \\\"to bite\\\". See dent-. [Pok. ed- 287.]'. Language label ('Indo-European'), form and gloss are all right; the modern laryngeal notation is *h₁ed-. The two weak places on this page are the Avestan box (node 1: 'xarka-asa' is a misprint for kahrka-āsa- and 'asa' is glossed 'food' where it means 'eating'), the Persian box (node 2: آش is disputed), and the reconstructed compound in node 3, where every other source writes *aspa-asti- (with the -ti- abstract), not 'aspa-asa'. The extraction is faithful: I rendered pdf page 147 at 200 dpi (copy at data/verification/sources/refs/ocr/BOOK/147.png) and every form, gloss, script string and reference in page-147.json matches the printed chart. One citation error of Nourai's own: BQT:1624 is the کرکس page, so it supports nodes 1-2 but not node 8 (فسفسه stands at BQT p.1489).\",\n   \"note_fa\": \"ریشهٔ نمودار همان ریشهٔ هندواروپایی آغازینِ *h₁ed- «خوردن» است که پوکورنی در صفحهٔ ۲۸۷ فرهنگ خود با صورت قدیمی‌ترِ ed- و معنای آلمانی «essen» آورده و در همان‌جا می‌افزاید که صورت‌های اسمیِ edont-, dont-, dnt- به معنی «دندان» نیز از همین ریشه‌اند؛ یعنی هر دو شاخهٔ «خوردن» و «دندان» که نورایی رسم کرده، درست است. والده-پوکورنی (جلد ۱ ص ۱۱۸) و واتکینز در پیوستِ فرهنگ American Heritage (ص ۴۱۷) نیز همین را می‌گویند: «ed-. خوردن؛ معنای اصلی: گاز گرفتن». پس جعبهٔ ریشه، برچسب زبان و معنا هر سه درست است و ادعای نورایی در این حد پذیرفتنی است. سه نقطهٔ سست در نمودار هست: صورت «xarka-asa» در گرهٔ ۱ (که غلط چاپی به‌جای kahrka-āsa- است)، ریشه‌شناسی «آش» در گرهٔ ۲ که امروزه محل اختلاف است، و ترکیبِ بازسازیِ گرهٔ ۳ که در همهٔ مأخذها *aspa-asti- نوشته می‌شود نه aspa-asa.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ed-\"\n   ],\n   \"ref_check\": [\n    {\n     \"ref\": \"POK:287\",\n     \"status\": \"supports\",\n     \"note\": \"POK_01.txt, form-feed page 300 (= IEW pp. 287-288; grep -n \\\"cd-  ,essen\\\" → line 4121, the OCR reads initial e- as c-): 'ed- ,essen'; ursprüngl. athematisch, aber meist thematisch geworden; Nominalformen: ed-ono-, ed-men-, ed-uen-… ; edont-, dont-, dnt- ,Zahn'.' The same page then lists 'av. 3. Sg. Konj. adäiti', 'lat. edö, es, est ,essen'', 'got. themat. itan … ags. etan, engl. eat'. Exactly the root box and the three first-generation branches Nourai draws.\"\n    }\n   ],\n   \"consulted\": [\n    {\n     \"src\": \"WLD\",\n     \"where\": \"Walde-Pokorny I 118 (WLD_Bd1_1930_dli_70244_djvu.txt line 7698)\",\n     \"stance\": \"supports\",\n     \"note\": \"'ed- „essen“. Praes. unthematisch ai. admi, atti „esse, ißt“ … lat. edo, es, est … Thematisch got. itan, an. eta, as. ags. etan, ahd. ezzan „essen“' — the source Pokorny 287 abridges.\"\n    },\n    {\n     \"src\": \"AHD\",\n     \"where\": \"Watkins 1985, AHD_watkins1985.txt line 417 (ed-) and line 364 (dent-)\",\n     \"stance\": \"supports\",\n     \"note\": \"'ed-. To eat; original meaning \\\"to bite.\\\" See dent-. 1. Germanic *etan in: a. Old English etan, to eat: EAT; b. Old High German ezzen … : ETCH … 2. Latin edere, to eat: EDACIOUS, EDIBLE … [Pok. ed- 287.]'; and 'dent-. Tooth. (Originally participle of ed- in the earlier meaning \\\"to bite.\\\") 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dnt- perhaps in Germanic *tunth-sk- in Old English tūsc, tūx, canine tooth: TUSK. 3. Full-grade form *dent- in Latin dēns … [In Pok. ed- 287.]'\"\n    },\n    {\n     \"src\": \"IEC\",\n     \"where\": \"Mann, IEC.txt lines 3420-3426, 3693\",\n     \"stance\": \"supports\",\n     \"note\": \"'edmi, (edō), 3s esti \\\"eat\\\". WP I, 118 — Skt. ádmi; Av. ad-; Hitt. ēdmi; Hom. édō; Lat. edō, 3s ēst; Osc. edum; Go. itan; OE etan; OHG eʒʒan …'; also 'edolis, os, om \\\"edible; food\\\"' and 'ēskā \\\"food\\\"'.\"\n    },\n    {\n     \"src\": \"SYN\",\n     \"where\": \"Buck 5.11 EAT (SYN.txt line 8318 ff.)\",\n     \"stance\": \"partial\",\n     \"note\": \"'1. IE *ed-. Walde-P. 1.118 … Grk. édō, Lat. ēsse, late edere, Osc. edum … Goth. itan, so all Gmc.' — but Buck's Avestan column for 'eat' gives 'Av. xᵛar-, gah-', not ad-: in Avestan itself the inherited root survives only marginally (the subjunctive adāiti and compounds), the ordinary verb being xᵛar-.\"\n    }\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"adâiti; asa 1; xarka-asa\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"xarka-asa : eating bird ☞ Ker 3\",\n     \"correct_form\": \"kahrka-āsa- (Av. kahrkāsa- 'vulture', lit. 'fowl-eater')\",\n     \"derivation\": \"Three items, three different situations. (a) adâiti is real: Pokorny 287 cites 'av. 3. Sg. Konj. adāiti' as the Avestan continuation of athematic *h₁ed-, i.e. a 3sg subjunctive 'he shall eat' — not an infinitive, and not the ordinary Avestan verb for 'eat', which is xᵛar- (Buck 5.11); Bartholomae's Altiranisches Wörterbuch col. 55 has only an ad- 'to say'. So the root is preserved in Avestan only marginally, in this form and in compounds. (b) 'asa 1 : food' is Avestan -āsa-, but it is a compound-final adjective 'eating, eater' (Mo'in glosses it خورنده), never an independent noun 'food'; Nourai's gloss reverses the word class. (c) 'xarka-asa' is a misprint. The Avestan word is kahrkāsa- m. 'vulture' (Bartholomae col. 456, 'j. kahrkāsa- m. \\\"Geier\\\" … Komp.: *kahrka- + *āsa-'), a bahuvrihi-type compound of kahrka- 'cock, hen' (Nourai's own root 'Ker 3'; he spells it kahrkatât on book p. 227 = pdf 257) with -āsa- 'eating'. It therefore means 'fowl-EATER', not 'EATING bird' — the compound is object + verbal noun, and Mo'in states it flatly: «مرغ‌خوار». I rendered pdf p.147 at 200 dpi: the printed page really shows 'xarka-asa : eating bird', so the extraction is faithful and the error is Nourai's own (probably a compositor's loss of the first syllable ka(h)- of kahrka-).\",\n     \"derivation_fa\": \"این جعبه سه واژه دارد و وضع هر سه فرق می‌کند. نخست، adâiti واقعی است: پوکورنی در ص ۲۸۷ آن را «صیغهٔ التزامیِ سوم‌شخص مفرد اوستایی» از ریشهٔ *h₁ed- می‌آورد؛ یعنی «بخورد»، نه مصدر. باید توجه داشت که فعل معمولِ «خوردن» در اوستا xᵛar- است و بارتولومه در ستون ۵۵ فرهنگ خود فقط ad- به معنی «گفتن» را آورده است؛ پس این ریشه در اوستا تنها به‌صورت پراکنده (همین صیغه و در ترکیب‌ها) مانده است. دوم، asa صفتِ پایانِ ترکیب است به معنای «خورنده»، نه اسم به معنای «خوراک»؛ معین هم آن را «خورنده» معنی کرده است. سوم، «xarka-asa» غلط چاپیِ کتاب است: صورت درست اوستایی kahrkāsa- «کرکس» است، مرکب از kahrka- «کرک، مرغ» و āsa- «خورنده»، یعنی «مرغ‌خوار» و نه «پرندهٔ خورنده»؛ خودِ نورایی در ص ۲۲۷ کتاب kahrkatât می‌نویسد. تصویر صفحهٔ چاپی را دیدم: در کتاب هم «xarka-asa» چاپ شده، پس خطا از خوانشِ اسکن نیست، خطای چاپی خودِ کتاب است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%DA%A9%D8%B3\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:287\",\n       \"status\": \"supports\",\n       \"note\": \"IEW 287 (POK_01.txt, \\\\f-page 300): 'av. 3. Sg. Konj. adäiti' — the exact form of the chart, under ed- 'essen'.\"\n      },\n      {\n       \"ref\": \"BQT:44\",\n       \"status\": \"supports\",\n       \"note\": \"BQT_v1_pages.txt leaf 255 (= printed p. 44/45; offset ≈ leaf − 210), Mo'in's footnote 5 s.v. آش: «آش — در سانسکریت aś، هم‌ریشهٔ ad بمعنی خوردن و با edo لاتینی … مانند essen آلمانی و (to) eat انگلیسی … این ریشه در چند کلمهٔ فارسی بجا مانده: کرکس، آش، ناشتا» (OCR: 'در ساسکرت ۸5 همریقة 80 بمعتی خوردن … کر کس ,آش, ناثتا'). Exactly the root and the three Persian reflexes.\"\n      },\n      {\n       \"ref\": \"BQT:1624\",\n       \"status\": \"supports\",\n       \"note\": \"printed p. 1624 = BQT_v3_picofile.pdf p. 417 (pagemap), the کرکس page; Mo'in's footnote 9: «کرکس. اوستا kahrkāsa (کرکس). پهلوی kargās … کلمهٔ اوستایی مرکب از دو جزء است: kahrka (= کرک، مرغ) + āsa (خورنده)، جمعاً یعنی مرغ‌خوار». It supports the derivation but spells the first member kahrka, not Nourai's xarka, and glosses the compound 'fowl-eater', not 'eating bird'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Altiran. Wb. col. 456 (BRT.txt line 9245) and col. 455 (line 9238)\",\n       \"stance\": \"partial\",\n       \"note\": \"'j. kahrkāsa- m. \\\"Geier\\\" … KompA. — Komp.: *kahrka- + *āsa-; eig. …' and, s.v. kahrka-tāt-, 'vgl. ZDg. kark(u)s \\\"Geier\\\", ai. kṛkavāku- m. \\\"Hahn\\\" … kaḫḫāl- \\\"Hähnerfresser\\\", vgl. zu kahrkāsa-'. Supports the compound analysis, contradicts the form 'xarka'; and Bartholomae's col. 55 entry is 'j. ad- V. \\\"sagen\\\"' — he has no Avestan verb ad- 'to eat'.\"\n      },\n      {\n       \"src\": \"HUB\",\n       \"where\": \"Persische Studien (HUB.txt lines 7541, 8530)\",\n       \"stance\": \"supports\",\n       \"note\": \"'kargas \\\"Geier\\\" = zd. kahrkāsa-' — twice, in the lists of np. a > i and of np. reflexes of Avestan words.\"\n      },\n      {\n       \"src\": \"ARY\",\n       \"where\": \"Aryanpur, ARY_pages.txt pdf page 401 (footnote 1 of the *ker- root)\",\n       \"stance\": \"supports\",\n       \"note\": \"«واژه‌های فارسی 'کرکس' و اوستایی KAHRKĀSA و سانسکریت KṚKAVĀKU نیز از همین واج‌ریشه آمده‌اند» — again kahrkāsa with the full first syllable.\"\n      }\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"âš «آش»; nâštâ «ناشتا»; karkas «کرکس»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Two of the three words are solid, the first is not. karkas «کرکس» 'vulture' is the regular continuation of Av. kahrkāsa- through Middle Persian klkʾs /kargās/: intervocalic Old Iranian -s- is kept, the -ā- of -kāsa- shortens in New Persian, and Av. kahrka- 'hen' gives NP کرک kark, so karkas is transparently 'fowl-eater' (Hübschmann; Wiktionary s.v. کرکس, citing Horn, Justi, Lagarde, Ciancaglini; the word is already in Asadi's Garšāsp-nāma, 1066). nâštâ «ناشتا» is the privative نا nā- + āštā, a participial 'not-eaten, fasting' from the same *ad-/*aś- root (Mo'in, BQT 2099: «از: نا (نفی، سلب) + آشتا؛ هندی باستان aś, aśita (خوردن)»; cf. Skt. anāśita- 'one who has not eaten'), whence the modern noun 'breakfast' in Dari/Tajik. آش, however, is disputed: Wiktionary's first option is a Turkic loan (Proto-Turkic *aš 'food', Doerfer TMEN), noting that the derivation from *ad- leaves the long ā unexplained, and that the supposed Middle/Old Iranian ancestor is a hapax of the Vendidad which is 'claimed to be misread'; Mo'in (BQT 44) and Aryanpur do derive it from Skt. aś-/ad-. Note also that Wiktionary's ناشتا entry cites Nourai's own dictionary p.117 — i.e. this very chart — so it is not independent evidence for this node.\",\n     \"derivation_fa\": \"از سه واژهٔ این جعبه، دو تا استوار است و یکی محل بحث. «کرکس» دنبالهٔ منظمِ kahrkāsa-ی اوستایی است که از راه فارسی میانهٔ kargās (نوشتهٔ klkʾs) به فارسی نو رسیده؛ سِ میانِ دو واکه نگه داشته شده و آی کشیدهٔ -kāsa در فارسی نو کوتاه شده است، و چون kahrka- در فارسی «کرک» شده، معنای تحت‌اللفظیِ «مرغ‌خوار» هنوز آشکار است (هوبشمان؛ ویکی‌واژه به نقل از هرن، یوستی، لاگارده و چیانکالینی؛ شاهدِ گرشاسپ‌نامهٔ اسدی، ۱۰۶۶ م). «ناشتا» هم از پیشوند سلبیِ «نا» + «آشتا» (اسم مفعولِ «خورده») از همین ریشه است، چنان‌که معین در حاشیهٔ برهان قاطع ص ۲۰۹۹ می‌نویسد و سنسکریتِ anāśita- «نخورده» آن را تأیید می‌کند. اما دربارهٔ «آش» پژوهش امروزی دو دل است: ویکی‌واژه نخست وام‌گیری از ترکی (*aš «خوراک»، به پیروی از دورفر) را می‌آورد و می‌گوید کشیدگیِ آی با ریشهٔ ad- نمی‌خواند؛ در برابر، معین و آریان‌پور آن را از ریشهٔ aś/ad می‌دانند. پس این گره را باید «مورد اختلاف» شمرد. یادآوری: مدخلِ «ناشتا» در ویکی‌واژه خودِ کتاب نورایی (ص ۱۱۷، یعنی همین صفحه) را مأخذ داده و بنابراین گواهِ مستقل نیست.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%DA%A9%D8%B3\",\n      \"https://en.wiktionary.org/wiki/%D8%A2%D8%B4\",\n      \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B4%D8%AA%D8%A7\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:2099\",\n       \"status\": \"supports\",\n       \"note\": \"printed p. 2099 = BQT_v4_picofile.pdf p. 182 (offset −1917), the ناشتا page; Mo'in's footnote 4: «از: نا (نفی، سلب) + آشتا؛ هندی باستان aś, aśita (خوردن)؛ قس فارسی 'آش' … ریشهٔ aś از ad خوردن (قس: edo لاتینی، essen آلمانی و (to) eat انگلیسی) رك: بارتولمه». Supports nâštâ and, by cross-reference, âš.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"HUB\",\n       \"where\": \"HUB.txt line 7541\",\n       \"stance\": \"supports\",\n       \"note\": \"'kargas \\\"Geier\\\" = zd. kahrkāsa-'.\"\n      },\n      {\n       \"src\": \"ARY\",\n       \"where\": \"Aryanpur, ARY_pages.txt pdf pages 401 and 491\",\n       \"stance\": \"supports\",\n       \"note\": \"p.491 (the *ed- root): «ناشتا (به چم 'خوراک نخورده')» with the note «واژهٔ فارسی 'ناشتا' از پیشوند 'نا' (نشان منفی) و ریشهٔ 'شتا' (به چم خوردن) درست شده است», the cognate list giving Latin EDO, ESSE, EDERE and Old Persian/Avestan forms; p.401 gives کرکس under the *ker- root.\"\n      },\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Horn, Grundriss (grep 'kargas', 'āš' in HRN.txt)\",\n       \"stance\": \"silent\",\n       \"note\": \"Horn has no numbered article for آش or کرکس (his no. 79 covers only espist 'Luzerne'); the OCR yields no hit for either headword.\"\n      },\n      {\n       \"src\": \"BQT\",\n       \"where\": \"BQT_v1_pages.txt leaf 255, Mo'in fn. 5 s.v. آش\",\n       \"stance\": \"supports\",\n       \"note\": \"«آش اصلاً بمعنی مطلق خوردنی است و امروزه نام غذای مخصوصی است، ولی کلمهٔ آشپز و آشپزخانه یادآور معنی اصلی آن است» — Mo'in's argument for the inherited derivation that Wiktionary/Doerfer contest.\"\n      }\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Avestan\",\n     \"words\": \"aspa-asa\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The idea is right, the form and the language label are not. No compound *aspa-asa- is attested in Avestan (Bartholomae has no such entry), and the second member of the alfalfa word is not -āsa- 'eating' but the -ti- abstract *-asti- 'food, eating': Watkins reconstructs Old Iranian *aspa-sti- 'horse food' = *aspa- 'horse' (PIE *h₁eḱwo-, Nourai's root Ekwos) + *-sti- from *ed- (Etymonline s.v. alfalfa), Wiktionary reconstructs Proto-Iranian *HacwaHastiš 'lucerne', lit. 'horse-food' (*Hácwah + *Hástiš < *h₁ed- + *-tis) with Old Median *aspāstiš, and Mo'in himself writes the ancestor 'aspō-asti' in Avestan and Old Persian (BQT 119), as does Aryanpur (*ASPO-ASTI Avestan, *ASPO- + ASTI Old Persian). The -ti- stem is what gives the -t of Pahlavi aspast; from 'aspa-asa' one would expect **aspās. The form is best labelled Old Iranian / Old Median rather than Avestan; the Akkadian aspastu of the Neo-Assyrian period shows the word was already current in Median cavalry usage in the 7th c. BCE.\",\n     \"derivation_fa\": \"اندیشهٔ نورایی درست است ولی صورت و برچسبِ زبان نه. در اوستا ترکیبی به شکل *aspa-asa- گواهی نشده (بارتولومه چنین مدخلی ندارد) و جزء دومِ نامِ یونجه نه -āsa- «خورنده» بلکه اسمِ مصدرِ *-asti- «خوراک» است: واتکینز صورتِ ایرانی باستانِ *aspa-sti- «خوراکِ اسب» را بازسازی می‌کند و ویکی‌واژه ایرانی آغازینِ *HacwaHastiš را (از *Hácwah «اسب» + *Hástiš از ریشهٔ *h₁ed- با پسوندِ *-tis) با صورتِ مادیِ باستانِ *aspāstiš می‌آورد؛ خودِ معین هم در حاشیهٔ برهان (ص ۱۱۹) صورتِ نیایی را aspō-asti می‌نویسد و آریان‌پور نیز *ASPO-ASTI (اوستایی) و *ASPO- + ASTI (پارسی باستان). همین پسوندِ -ti- است که «ت»ِ پایانیِ aspastِ پهلوی را توضیح می‌دهد؛ از aspa-asa باید **aspās به دست می‌آمد. پس درست‌تر آن است که این صورت را «ایرانی باستان/مادی» بنامیم نه «اوستایی». گواهِ اکدیِ aspastu در دورهٔ آشورِ نو نشان می‌دهد این واژه در سدهٔ هفتم پیش از میلاد در زبانِ سوارکارانِ ماد رایج بوده است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/alfalfa\",\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/HacwaHasti%C5%A1\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:119\",\n       \"status\": \"partial\",\n       \"note\": \"BQT_v1_pages.txt leaf 332 (= printed p.119; the page ends «بقیه در صفحهٔ ۱۲۰»), Mo'in's footnote 2 s.v. اسپست: «در اوستا و پارسی باستان aspō-asti … این کلمهٔ مرکب لفظاً یعنی 'اسب می‌خورد'؛ جزء اول همان اسب است و جزء دوم از مصدر ad مطابق edo لاتینی و essen آلمانی و (to) eat انگلیسی است بمعنی خوردن». Same root and same 'horse food' reading — but Mo'in's form is aspō-asti, with the -ti- suffix, not aspa-asa. (The Latin transliterations are badly OCRed; Aryanpur prints the same reconstruction in clear type.)\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Altiran. Wb., grep 'aspast', 'aspāsti' in BRT.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"no Avestan compound of aspa- with an 'eat' word; the only related item is 'ni. aspōstāna- n., mp. (Pü.) aspastān, arm. LW. aspastan' (line 5885), i.e. 'stable', not the fodder word.\"\n      },\n      {\n       \"src\": \"ARY\",\n       \"where\": \"Aryanpur, ARY_latin_index_pages.txt pdf page 84 (ALFALFA / ASPAST)\",\n       \"stance\": \"partial\",\n       \"note\": \"lists '*ASPO-ASTI (AVESTAN)', '*ASPO-, ASTI (OLD PERSIAN)', 'ASPAST (PAHLAVI)', 'ASVAS-ADMI (SANSKRIT)', 'ASPO-UTEM (ARMENIAN)', with REFERENCES: POKORNY, MACKENZIE (CLOVER), THE AMERICAN HERITAGE DICTIONARY (ALFALFA) — the -asti form again.\"\n      },\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Horn no. 79 (HRN.txt lines 1127-1133)\",\n       \"stance\": \"supports\",\n       \"note\": \"'espist, uspust, ispist \\\"Luzerne\\\". phlv. aspast \\\"Luzerne\\\" … Wörtlich \\\"Pferdefutter\\\" von esp und √ad-, Nöldeke, ZDMG. 32, 408' — the compound analysis 'horse' + root ad- exactly as Nourai draws it.\"\n      }\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"aspast, aspasti\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian aspast [ʾspst] 'clover, lucerne' is the regular outcome of Old Iranian *aspa-asti-: the two a's of aspa-asti contract across the compound seam and the final -i- of the abstract is lost, as normally in MP (*aspāsti > aspast). MacKenzie's Concise Pahlavi Dictionary p.13 gives it verbatim, and the word is attested in Book Pahlavi (Xusraw ud Rēdag). The doublet 'aspasti' Nourai adds is not a separate Pahlavi form; it is the older -ti- stem (Old Median *aspāstiš) which he seems to be showing beside the shortened one, and it is exactly that -ti- that survives in the Syriac/Aramaic ʾaspastā and in Classical Persian اسپست.\",\n     \"derivation_fa\": \"فارسی میانهٔ aspast (نوشتهٔ ʾspst) «یونجه» دنبالهٔ منظمِ *aspa-asti-ی ایرانی باستان است: دو «ا» در درزِ ترکیب در هم ادغام می‌شود و «ی»ِ پایانیِ اسمِ مصدر به عادتِ فارسی میانه می‌افتد (*aspāsti > aspast). مکنزی در فرهنگ کوتاه پهلوی (ص ۱۳) همین را می‌آورد و واژه در متن‌های پهلویِ کتابی (خسرو و ریدگ) گواهی شده است. صورت دومِ «aspasti» که نورایی افزوده صورتِ جداگانه‌ای در پهلوی نیست، بلکه همان ستاکِ کهنِ -ti- (مادیِ باستان *aspāstiš) است که همان هم در «اسپستا»ی سریانی-آرامی و در «اسپست»ِ فارسی دری بازمانده است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/HacwaHasti%C5%A1\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:119\",\n       \"status\": \"supports\",\n       \"note\": \"Mo'in fn. 2 s.v. اسپست (BQT_v1_pages.txt leaf 332): «در پهلوی نیز aspast آمده» — with the reference «پهلوی aspast (اونوالا ۲۸۰)» in the continuation of the note on the next page.\"\n      },\n      {\n       \"ref\": \"BQT:1624\",\n       \"status\": \"not_found\",\n       \"note\": \"printed p.1624 (BQT_v3 pdf 417) is the کرکس page and says nothing about aspast; the alfalfa material is at BQT 119 (and 1489 for فسفسه). The citation looks like a slip carried over from node 1.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"PHD\",\n       \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.13 (PHD.txt line 219; PHD_mackenzie.txt line 1228) and the English index (PHD.txt lines 1258, 2684)\",\n       \"stance\": \"supports\",\n       \"note\": \"'aspast [ʾspst | N ~] clover, lucerne.'; index: 'clover aspast.' / 'lucerne aspast.'\"\n      },\n      {\n       \"src\": \"NYB\",\n       \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt, grep 'aspast'/'spst')\",\n       \"stance\": \"silent\",\n       \"note\": \"the glossary has no aspast entry; the only 'spst' hit is a text-critical note s.v. *dēbastan (line 1267) about a manuscript reading spstyn', unrelated.\"\n      },\n      {\n       \"src\": \"PLA\",\n       \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (PLA_asbaghi_1988_ia_djvu.txt line 2421)\",\n       \"stance\": \"supports\",\n       \"note\": \"'ʾisfist / ʾasfast: \\\"Luzerne, Futterpflanze\\\" … aus pers. اسپست aspast, MP. aspast' (with al-Muʿarrab as source) — the Middle Persian form is the etymon of the Arabic borrowings.\"\n      }\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"aspast «اسپست (سپست)»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian اسپست aspast/espest 'lucerne, alfalfa' continues MP aspast unchanged; the by-form سپست sepest arises by the ordinary Persian loss of prothetic/initial a- before a consonant cluster (cf. اسپر ~ سپر), and Horn records the further variants espist, ispist, uspust with the regular raising of unstressed a > i before a sibilant that Hübschmann documents (§6: 'aspist (ispist, uspust) \\\"Luzerne\\\" = phl. aspast'). Nourai's Persian script and the Sanā'i couplet he quotes («سنبل و سوسن کجا آمد بدست از روضه‌ای / کاندرو تخم سپست و سیر و سیسنبر برند») are the ones printed in Borhān-e Qāṭeʿ p.119 with the سپست form, so the word is attested in Ghaznavid-period verse.\",\n     \"derivation_fa\": \"«اسپست» فارسی نو، دنبالهٔ بی‌تغییرِ aspastِ فارسی میانه است؛ صورتِ «سپست» از افتادنِ الفِ آغازین پیش از خوشهٔ همخوانی پدید آمده (مانندِ اسپر ~ سپر) و هرن صورت‌های espist و ispist و uspust را نیز ثبت کرده که در آن‌ها «اَ»ی بی‌تکیه پیش از سایشیِ س به «اِ/ای» بدل شده است — همان قاعده‌ای که هوبشمان در بند ۶ کتابش می‌آورد: «aspist (ispist, uspust) 'یونجه' = پهلوی aspast». بیتِ سنایی که نورایی نقل کرده همان شاهدِ برهان قاطع (ص ۱۱۹) با صورتِ «سپست» است، پس واژه در شعرِ سدهٔ ششم گواهی دارد. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/HacwaHasti%C5%A1\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:119\",\n       \"status\": \"supports\",\n       \"note\": \"BQT_v1_pages.txt leaf 332: «اسپست — بفتح اول و کسر ثالث و سکون ثانی … سپست را گویند و آن علفی است … و عربی فصفصه خوانند و تخم آنرا بذرالرطبه گویند»; the Sanā'i couplet and the سپست spelling are on the same page, and Mo'in's fn. 2 attaches the etymology to it.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Horn, Grundriss no. 79 (HRN.txt line 1127); index p.79 (line 15630)\",\n       \"stance\": \"supports\",\n       \"note\": \"'79. espist, uspust, ispist \\\"Luzerne\\\". phlv. aspast \\\"Luzerne\\\". bel. LW. aspust. Wörtlich \\\"Pferdefutter\\\" von esp und √ad-.'\"\n      },\n      {\n       \"src\": \"HUB\",\n       \"where\": \"Hübschmann, Persische Studien §6 (HUB.txt line 4465)\",\n       \"stance\": \"supports\",\n       \"note\": \"'aspist (ispist, uspust) \\\"Luzerne\\\" = phl. aspast' — cited as an instance of np. a > i before sibilants.\"\n      },\n      {\n       \"src\": \"PLA\",\n       \"where\": \"Asbaghi (PLA djvu line 15365)\",\n       \"stance\": \"supports\",\n       \"note\": \"'fiṣfiṣa: \\\"Luzerne\\\" pers. اسپست asbast od. asfast' — the New Persian form is the source of the Arabic.\"\n      }\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Syriac\",\n     \"words\": \"pespesta\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The route is right, the cited form belongs one step further west. Middle Persian aspast was borrowed into Aramaic/Syriac as ʾspstʾ — Jewish Aramaic אַסְפַּסְתָּא ʾaspastā, Classical Syriac ܐܰܣܦܷܣܬܳܐ ʾaspestā 'lucerne' (Löw, Aramäische Pflanzennamen 1924; Ciancaglini, Iranian Loanwords in Syriac) — and it is that Aramaic form, not the Persian one directly, that Arabic borrowed. The shape 'pespesta' with initial p- and a reduplicated pe-…-pe- is the Coptic ⲡⲉⲥⲡⲉⲥⲧⲁ p-espesta (the Coptic masculine article ⲡ- fused to ʾespesta), which Wiktionary's descendant tree puts between Syriac ʾespestā and Arabic fiṣfiṣa and which explains why Arabic has f- and not ʾ-: Arabic has no p and substitutes f. So Nourai's node correctly records the Semitic intermediary that Mo'in asserts («از زبان پهلوی داخل سریانی و از سریانی به عربی رفت»), but the form he prints under the label 'Syriac' is the Coptic-article form; the genuine Syriac word is ʾespestā/ʾaspastā.\",\n     \"derivation_fa\": \"مسیر درست است ولی صورتی که آمده یک گام غربی‌تر است. فارسی میانهٔ aspast به آرامی و سریانی وام رفته: آرامیِ یهودی אַסְפַּסְתָּא (ʾaspastā) و سریانیِ کلاسیک ܐܰܣܦܷܣܬܳܐ (ʾespestā) «یونجه» (لِو، نام‌های گیاهیِ آرامی ۱۹۲۴؛ چیانکالینی، وام‌واژه‌های ایرانی در سریانی)، و عربی همین صورتِ آرامی را گرفته نه صورتِ فارسی را. اما شکلِ «pespesta» با «پ»ِ آغازین و تکرارِ pe-…-pe- صورتِ قبطیِ ⲡⲉⲥⲡⲉⲥⲧⲁ (p-espesta) است، یعنی همان ʾespestā با حرفِ تعریفِ مذکرِ قبطیِ ⲡ-، که ویکی‌واژه آن را حلقهٔ میانِ سریانی و عربی می‌داند و همو توضیح می‌دهد چرا عربی «ف» دارد نه همزه (عربی «پ» ندارد و آن را به «ف» بدل می‌کند). پس حلقهٔ سامیِ نمودار درست است — همان که معین می‌گوید «از زبان پهلوی داخل سریانی و از سریانی به عربی رفت» — ولی صورتی که زیرِ برچسبِ «سریانی» چاپ شده در واقع صورتِ قبطی است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/HacwaHasti%C5%A1\",\n      \"https://en.wiktionary.org/wiki/%D9%81%D8%B5%D9%81%D8%B5\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:119\",\n       \"status\": \"partial\",\n       \"note\": \"Mo'in fn. 2 (leaf 332) asserts the route but gives no Syriac form: «در پهلوی نیز aspast آمده، از زبان پهلوی داخل سریانی و از سریانی به عربی رفت 'فصفصه' (جمع: فصافص) شد».\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"AFA\",\n       \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt, grep 'fisfis', 'fasfas', 'Luzerne')\",\n       \"stance\": \"silent\",\n       \"note\": \"no hit for the word or for 'Luzerne' anywhere in the 600 kB OCR; Fraenkel's plant chapter apparently does not treat it (or the OCR has lost it).\"\n      },\n      {\n       \"src\": \"PLA\",\n       \"where\": \"Asbaghi (PLA djvu lines 2421, 15365)\",\n       \"stance\": \"partial\",\n       \"note\": \"Asbaghi routes both Arabic ʾisfist and fiṣfiṣa straight from Persian ('pers. اسپست aspast') without an Aramaic middleman, though he cites Löw among his sources — so the Semitic intermediary of the chart is not universally drawn.\"\n      },\n      {\n       \"src\": \"LKT\",\n       \"where\": \"Lokotsch no. 598 (LKT.txt line 1505)\",\n       \"stance\": \"silent\",\n       \"note\": \"'Ar. faṣfaṣu \\\"Luzerne Medicago sativa L.\\\", auch fiṣfiṣa; hieraus sp. alfalfa …' — Lokotsch starts the chain at Arabic and says nothing about Syriac or Persian.\"\n      }\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Arabic\",\n     \"words\": \"al-fesfeseh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic فِصْفِصَة fiṣfiṣa (also فَصْفَصَة faṣfaṣa, collective فِصْفِص fiṣfiṣ, pl. فَصَافِص faṣāfiṣ) 'lucerne, green fodder'; with the article, al-fiṣfiṣa. It is a loan from Aramaic ʾaspastā / Syriac ʾespestā (via the p-form): the Aramaic sibilant cluster is arabicised as ṣ, the p- of the Coptic/Aramaic form becomes f- (Arabic lacks p), and the result is reshaped into the native quadriliteral reduplicated pattern fiṣfiṣ, which then looks like an Arabic root f-ṣ-f-ṣ. Klein and Lokotsch both start their alfalfa chain from this word, and Asbaghi lists it as a Persian loanword in Arabic.\",\n     \"derivation_fa\": \"عربیِ «فِصْفِصَة» (و «فَصْفَصَة»، جمعِ آن «فصافص») به معنی یونجه و علفِ تازه است و با حرفِ تعریف «الفصفصة» می‌شود. این واژه از آرامیِ ʾaspastā / سریانیِ ʾespestā (از راهِ صورتِ پ‌دار) وام گرفته شده: خوشهٔ سایشیِ آرامی در عربی به «ص» بدل شده، «پ» به «ف» (چون عربی «پ» ندارد)، و سپس واژه در قالبِ رباعیِ مضاعفِ عربی (فِعْفِل: فصفص) ریخته شده تا شکلِ ریشه‌ای عربی به خود بگیرد؛ این همان چیزی است که در ریشه‌شناسیِ عامیانه آن را عربیِ اصیل می‌نماید. کلاین و لوکوچ هر دو زنجیرهٔ «آلفالفا» را از همین واژه آغاز می‌کنند و اصبغی آن را در فهرستِ وام‌واژه‌های فارسی در عربی آورده است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%81%D8%B5%D9%81%D8%B5\",\n      \"https://en.wiktionary.org/wiki/alfalfa\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"None\",\n       \"status\": \"not_checked\",\n       \"note\": \"Nourai gives no reference for this node; the claim is nevertheless carried by his BQT:119 citation on the neighbouring nodes (Mo'in: «از سریانی به عربی رفت 'فصفصه' (جمع: فصافص) شد»).\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein s.v. alfalfa (KLN_1966.txt line 2169; KLN_1971.txt line 10963)\",\n       \"stance\": \"supports\",\n       \"note\": \"'alfalfa, n., lucerne. — Sp., fr. Arab. al-faṣfaṣah. (Cp. the collateral Sp. form alfalfez, which represents the intermediate form between Arab. al-faṣfaṣah and Sp. alfalfa.)'\"\n      },\n      {\n       \"src\": \"LKT\",\n       \"where\": \"Lokotsch no. 598 (LKT.txt line 1505)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Ar. faṣfaṣu: \\\"Luzerne Medicago sativa L.\\\", auch fiṣfiṣa; hieraus sp. alfalfa, alfafe … engl. amerik. alfalfa. [DE 100/101. Eguilaz 156. ML 4002 Anm.]'\"\n      },\n      {\n       \"src\": \"PLA\",\n       \"where\": \"Asbaghi p.211 area (PLA djvu line 15365)\",\n       \"stance\": \"supports\",\n       \"note\": \"'fiṣfiṣa: \\\"Luzerne\\\" pers. اسپست asbast od. asfast' (source: Muḥīṭ), and separately 'fiṣāfiṣ: Pl. v. fiṣfiṣa q. v.'\"\n      }\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Persian\",\n     \"words\": \"fesfeseh «فسفسه ، فصفصه»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"A genuine round trip: the Iranian word that Aramaic and then Arabic had taken over as fiṣfiṣa came back into Persian as فسفسه/فصفصه, a moʿarrab (arabicised) doublet of the inherited اسپست. Borhān-e Qāṭeʿ has the entry: «فسفسه — بفتح هر دو فا … بمعنی اسپست باشد و آن علفی است که به عربی رطبه و به ترکی یونجه گویند و فصفصه معرب آن است», i.e. the lexicographers themselves knew that فصفصه is the arabicised shape and اسپست the Persian one. The spelling with ص is the Arabic orthography, the one with س a Persian re-spelling.\",\n     \"derivation_fa\": \"این گره نمونهٔ روشنِ «رفت و برگشت» است: واژه‌ای ایرانی که از راه آرامی به عربی رفته و آنجا «فصفصة» شده، دوباره به فارسی بازگشته و به‌صورتِ «فسفسه/فصفصه» در کنارِ صورتِ موروثیِ «اسپست» نشسته است، یعنی دوگانه‌ای (doublet) که یک عضوش معرّب است. برهان قاطع خود همین را می‌گوید: «فسفسه — بفتح هر دو فا … بمعنی اسپست باشد و آن علفی است که به عربی رطبه و به ترکی یونجه گویند و فصفصه معرّب آن است». املای با «ص» صورتِ عربی است و املای با «س» بازنویسیِ فارسی. ادعای نورایی درست است، تنها شمارهٔ صفحه‌ای که داده نادرست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%81%D8%B5%D9%81%D8%B5\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:1624\",\n       \"status\": \"not_found\",\n       \"note\": \"printed p.1624 = BQT_v3 pdf 417 is the کرکس page, which has nothing on فسفسه. The فسفسه entry is at printed p.1489 = BQT_v3 pdf 282 (BQT_v3_pages.txt line 20490): «فسفسه — بفتح هردو فا بروزن … بمعنی اسپست باشد … و فصفصه معرب آنست». Nourai's page number is off by ~135; the substance of his claim is nevertheless in Borhān.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BQT\",\n       \"where\": \"Borhān-e Qāṭeʿ p.1489 (BQT_v3_pages.txt, pdf page 282)\",\n       \"stance\": \"supports\",\n       \"note\": \"quoted above: فسفسه = اسپست, «و فصفصه معرب آنست».\"\n      },\n      {\n       \"src\": \"PLA\",\n       \"where\": \"Asbaghi (PLA djvu line 15365)\",\n       \"stance\": \"supports\",\n       \"note\": \"'fiṣfiṣa … pers. asbast od. asfast' — the Arabic word is recognised as Persian in origin, which is what makes the Persian فصفصه a re-borrowing.\"\n      },\n      {\n       \"src\": \"MON\",\n       \"where\": \"Mo'in, Farhang-e Fārsi (MON_part1/2, grep فصفصه)\",\n       \"stance\": \"silent\",\n       \"note\": \"the Persian OCR of MON yields no clean hit for فسفسه/فصفصه; Mo'in's statement is used from his Borhān footnote instead.\"\n      }\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"Spanish\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"An empty pass-through box for Spanish alfalfa (older alfalfe, alfalfez), taken over with the Arabic article agglutinated (al- + fiṣfiṣa) during the Andalusi period, like hundreds of Spanish Arabisms (alcalde, algodón). Klein points to alfalfez as the intermediate stage between Arab. al-faṣfaṣah and modern alfalfa; the -z of alfalfez renders the Arabic tāʾ marbūṭa of the pausal form. Spanish settlers carried the plant and its name to the Americas, which is where English met it — Mo'in notes exactly this: «از عربی در اسپانیایی وارد شده صورت الفلفه … اسپانیولی‌ها آن را به آمریکا بردند».\",\n     \"derivation_fa\": \"این جعبهٔ خالی حلقهٔ اسپانیایی است: alfalfa (صورت‌های کهن‌تر alfalfe و alfalfez) که در دورهٔ اندلس با حرفِ تعریفِ عربی (al- + fiṣfiṣa) یکجا وام گرفته شده، درست مانندِ صدها وام‌واژهٔ عربی در اسپانیایی (alcalde، algodón). کلاین صورتِ alfalfez را حلقهٔ میانی میانِ al-faṣfaṣah عربی و alfalfa امروزی می‌داند و «ز»ی پایانیِ آن برگردانِ تاء مربوطهٔ عربی است. اسپانیایی‌زبانان این گیاه و نامش را به آمریکا بردند و انگلیسی همان‌جا با آن آشنا شد؛ معین هم دقیقاً همین را می‌نویسد: «از عربی در اسپانیایی وارد شده … اسپانیولی‌ها آن را به آمریکا بردند».\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/alfalfa\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"None\",\n       \"status\": \"not_checked\",\n       \"note\": \"no reference given for this node; covered by Klein and Lokotsch below and by Mo'in's BQT:119 footnote.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein s.v. alfalfa (KLN_1966.txt line 2169)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Sp., fr. Arab. al-faṣfaṣah. (Cp. the collateral Sp. form alfalfez …)'\"\n      },\n      {\n       \"src\": \"LKT\",\n       \"where\": \"Lokotsch no. 598\",\n       \"stance\": \"supports\",\n       \"note\": \"'hieraus sp. alfalfa, alfafe \\\"dass., spanischer Klee, foenum Burgundiacum\\\"'.\"\n      }\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"English\",\n     \"words\": \"alfalfa\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English alfalfa is a 19th-century Americanism, first recorded 1845, taken from the Spanish of the south-west and of Chile (whence the crop was reintroduced to California in the 1850s); Britain kept the older name lucerne, itself from Provençal luzerno. Watkins/AHD, which Nourai cites here, files alfalfa under the Indo-European root and traces it to Old Iranian *aspa-sti- 'horse food', so the whole arc of the chart — PIE *ed- → Iranian 'horse food' → Aramaic → Arabic → Spanish → American English — is the standard account.\",\n     \"derivation_fa\": \"«alfalfa» در انگلیسی واژه‌ای آمریکایی و نو است؛ نخستین کاربردِ ثبت‌شدهٔ آن ۱۸۴۵ م است و از اسپانیاییِ جنوب‌غربِ آمریکا و شیلی گرفته شده (کشتِ این گیاه در دههٔ ۱۸۵۰ از همان راه به کالیفرنیا رسید)؛ در انگلیسیِ بریتانیا هنوز نامِ کهن‌ترِ lucerne (از پروانسالیِ luzerno) به کار می‌رود. واتکینز در پیوستِ فرهنگِ American Heritage — همان مأخذی که نورایی داده — این واژه را ذیلِ همین ریشهٔ هندواروپایی و از ایرانیِ باستانِ *aspa-sti- «خوراکِ اسب» می‌گیرد. پس کلِ کمانِ نمودار (هندواروپایی → ایرانی → آرامی → عربی → اسپانیایی → انگلیسیِ آمریکایی) روایتِ پذیرفتهٔ امروزی است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/alfalfa\",\n      \"https://en.wiktionary.org/wiki/alfalfa\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"Watkins' appendix files ALFALFA under the horse word; Etymonline reports it explicitly: 'according to Watkins, the ultimate source is Old Iranian *aspa-sti- \\\"alfalfa, clover\\\", from *aspa- \\\"horse\\\" + -sti- \\\"food\\\", from PIE *ed- \\\"to eat\\\".' (The 1985 standalone reprint on disk indexes alfalfa under ekwo-, not under ed-.)\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein s.v. alfalfa\",\n       \"stance\": \"supports\",\n       \"note\": \"'alfalfa, n., lucerne. — Sp., fr. Arab. al-faṣfaṣah.'\"\n      },\n      {\n       \"src\": \"WEB\",\n       \"where\": \"Webster's New Twentieth Century Dictionary (WEB_vol1.txt, s.v. alfalfa)\",\n       \"stance\": \"supports\",\n       \"note\": \"same Spanish-Arabic derivation for the forage plant Medicago sativa; the dictionary tradition is unanimous from Lokotsch (1927) onward.\"\n      }\n     ]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"Sogdian\",\n     \"words\": \"`šp`dy\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Gharib's Sogdian Dictionary p.70, entry 1767, does have the word Nourai transcribes (his ` renders aleph, his d the letter δ): 'ʾšpʾδy S — (ə)špăδč ? ©Pers. āš ? — part, portion ?, bowl ?' with the Persian gloss «قسمت، جزء ؟، کاسه، ظرف ؟» and the attestations Frag. Len. 60, 8; 69, 28-33. Two things follow. Gharib does connect it with Persian āš, which is why Nourai hangs it under this root, so the placement is his source's own suggestion. But every element of the entry carries a question mark — reading, gloss and etymology alike — and the gloss is 'part, portion; bowl', not 'food, dish': 'dish' is defensible for کاسه/ظرف 'bowl, vessel', 'food' is Nourai's extension of 'portion'. Given that the Persian anchor āš is itself disputed (node 2), the node can be no better than plausible.\",\n     \"derivation_fa\": \"در فرهنگِ سغدیِ بدرالزمان قریب، ص ۷۰، مدخلِ ۱۷۶۷ همان واژه‌ای هست که نورایی آورده (علامتِ ` در نوشتهٔ او همان الف/همزه و d همان ذال است): «ʾšpʾδy، خوانشِ (ə)špăδč ؟، © فارسیِ āš ؟، معنی: قسمت، جزء ؟، کاسه، ظرف ؟» با شاهدهای Frag. Len. ۶۰ و ۶۹. از این دو نکته برمی‌آید: نخست آنکه خودِ قریب این واژه را با «آش» فارسی سنجیده، پس جای‌دادنِ آن زیرِ این ریشه پیشنهادِ مأخذِ نورایی است نه ابداعِ او؛ دوم آنکه قریب بر سرِ هر سه چیز — خوانش، معنا و ریشه — علامتِ پرسش گذاشته و معنایی که داده «قسمت، جزء، کاسه» است نه «خوراک، خورش»: برگردانِ «dish» برای «کاسه/ظرف» رواست ولی «food» افزودهٔ نورایی است. چون تکیه‌گاهِ فارسیِ این گره («آش») خود محلِ اختلاف است، این گره بیش از «با احتیاط پذیرفتنی» نمی‌تواند بود.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"SOD:70\",\n       \"status\": \"partial\",\n       \"note\": \"Gharib, Sogdian Dictionary, printed p. 70 = leaf n135 of archive.org/details/SogdianDictionary, entry 1767 (SOD.txt line 19252; the hačeks are lost in the OCR, so I read the scan and saved the transcript to data/verification/sources/refs/ocr/SOD/70.vision.txt): «1767 ʾšpʾδy S — (ə)špăδč ? ©Pers. āš ? — part, portion ?, bowl ? — Frag. Len. 60, 8, 69, 28-33; S W, BAI 1990, 286». Right page, right word, and Gharib herself compares Persian āš; but the gloss is not 'food, dish' and everything is queried.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"SOD\",\n       \"where\": \"Gharib p.70 no.1767 (image n135, transcript saved locally)\",\n       \"stance\": \"partial\",\n       \"note\": \"see the quotation above; note also that Gharib's neighbouring entries 1768 ʾšpʾyr, 1769 ʾšpn- show the same ʾšp- spelling, so the reading of the consonants is not in doubt, only the interpretation.\"\n      },\n      {\n       \"src\": \"ISS_alt_DKS\",\n       \"where\": \"Bailey, Dictionary of Khotan Saka (grep 'spady', 'aspast')\",\n       \"stance\": \"silent\",\n       \"note\": \"no Khotanese counterpart of the word turns up; Bailey's entries under āś-/ad- do not cite the Sogdian form.\"\n      },\n      {\n       \"src\": \"HENNING\",\n       \"where\": \"Henning, Selected Papers (HENNING_selected_papers.txt, grep 'špʾδ')\",\n       \"stance\": \"silent\",\n       \"note\": \"no discussion of the word in the OCR of the Selected Papers.\"\n      }\n     ]\n    },\n    {\n     \"id\": 12,\n     \"lang\": \"Germanic\",\n     \"words\": \"it-an; tanth-uz, tunth-sk\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *etan- 'to eat' is the thematised continuation of the athematic present of *h₁ed-, with Grimm's law leaving initial e- and medial -t- < *-d- (Gothic itan, Old Norse eta, Old Saxon/Old English etan, Old High German ezzan, the last with the High German consonant shift t > ʒʒ). The tooth words descend not from the verb but from its old participle *h₁dónt- 'biting': o-grade *dont- > Gmc *tanþuz (Gothic tunþus, OE tōþ) with Grimm d > t and the regular ON/West-Germanic development -anþ- > -āþ-; the zero grade *dn̥t- gives Gmc *tunþ-sk- in OE tūsc/tūx. Nourai's 'tanth-uz, tunth-sk' are exactly Watkins' *tanthuz and *tunth-sk-, and his gloss 'eater' for them is the etymological sense of the participle. Watkins puts them under a separate headword dent-, but says in so many words that it is 'originally participle of ed- in the earlier meaning \\\"to bite\\\"' and files it '[In Pok. ed- 287]', so Nourai's decision to draw one root is Watkins' own analysis.\",\n     \"derivation_fa\": \"ژرمنیِ آغازینِ *etan- «خوردن» دنبالهٔ ستاکِ بی‌میانجیِ *h₁ed- است که در ژرمنی به ستاکِ میانجی‌دار بدل شده؛ بر پایهٔ قانونِ گریم، «د»ی هندواروپایی به «ت» بدل شده و از این‌رو گوتیِ itan، نورسِ کهنِ eta، انگلیسیِ کهنِ etan و آلمانیِ علیای کهنِ ezzan (با جابه‌جاییِ دومِ همخوان‌ها) داریم. اما واژه‌های «دندان» نه از فعل، بلکه از اسمِ فاعلِ کهنِ *h₁dónt- «گازگیرنده» آمده‌اند: درجهٔ o یعنی *dont- در ژرمنی *tanþuz شده (گوتی tunþus، انگلیسی کهن tōþ) و درجهٔ صفر یعنی *dn̥t- صورتِ *tunþ-sk- را داده که انگلیسیِ کهنِ tūsc/tūx «دندانِ نیش» از آن است. صورت‌های «tanth-uz» و «tunth-sk» در نمودار عیناً همان صورت‌های واتکینز است و معنایی که نورایی داده («خورنده») همان معنای ریشه‌ایِ اسمِ فاعل است. واتکینز این‌ها را زیرِ سرواژهٔ جداگانهٔ dent- آورده، اما خود می‌نویسد «در اصل اسمِ فاعلِ ed- به معنای کهنِ گاز گرفتن» و ارجاعش را «[در پوکورنی ذیلِ ed- ص ۲۸۷]» می‌دهد؛ پس یکی‌کردنِ این دو شاخه در نمودار، تحلیلِ خودِ واتکینز است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"Watkins 1985 p.417: 'ed- … 1. Germanic *etan in: a. Old English etan, to eat: EAT; b. Old High German ezzen … ETCH; c. Middle Dutch eten … d. Germanic compound *fra-etan … OE fretan: FRET'; and s.v. dent-: '1. O-grade form *dont- in Germanic *tanthuz in Old English toth: TOOTH. 2. Zero-grade form *dnt- perhaps in Germanic *tunth-sk- in Old English tūsc, tūx, canine tooth: TUSK. … [In Pok. ed- 287.]' — Nourai's forms letter for letter.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW 287-288 (POK_01.txt \\\\f-page 300)\",\n       \"stance\": \"supports\",\n       \"note\": \"'got. themat. itan (Perf. 1. Pl. etum, ahd. āzum …), anord. eta, as. ags. etan, engl. eat, afries. ita, ahd. ezzan \\\"essen\\\" … mit Präfix fra-: got. fra-itan \\\"aufzehren\\\" … kaus. got. fra-atjan … ahd. azzen, ezzen \\\"zu essen geben\\\", nhd. ätzen'; and the headword line already lists 'edont-, dont-, dnt- \\\"Zahn\\\"'.\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Walde-Pokorny I 118-119\",\n       \"stance\": \"supports\",\n       \"note\": \"'Thematisch got. itan, an. eta, as. ags. etan, ahd. eʒʒan „essen“' in the same article as the tooth derivatives.\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein s.v. eat, tooth, tusk\",\n       \"stance\": \"supports\",\n       \"note\": \"Klein derives eat from OE etan, Gmc *etan, and tooth from OE tōþ, Gmc *tanþ-, both from the same IE base *ed-.\"\n      }\n     ]\n    },\n    {\n     \"id\": 13,\n     \"lang\": \"English\",\n     \"words\": \"eat, etch; tooth, tusk\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"eat < ME eten < OE etan, the direct inheritance. etch is a 17th-century artists' term borrowed from Dutch etsen, itself from German ätzen 'to corrode' < MHG etzen < OHG azzōn 'to feed, bait', the causative *atjan of ezzan 'to eat' — i.e. 'to make (the acid) eat', so it belongs to the root by way of a causative, not by inheritance into English; Nourai's arrow is right but the route is Dutch/German, not native. tooth < OE tōþ (pl. tēþ) < Gmc *tanþuz with loss of n before þ and compensatory lengthening; tusk < OE tūsc/tūx, a metathesised by-form of the same *tunþ-sk-. All four are Watkins' own English glosses under ed- and dent-.\",\n     \"derivation_fa\": \"«eat» از انگلیسیِ میانهٔ eten و انگلیسیِ کهنِ etan، یعنی میراثِ مستقیم. اما «etch» وام‌واژه‌ای است از سدهٔ هفدهم از هلندیِ etsen که خود از آلمانیِ ätzen «خوردن/سوزاندنِ فلز با تیزاب» آمده و آن از آلمانیِ علیای کهنِ azzōn «خوراندن»، یعنی صورتِ سببیِ *atjan از ezzan «خوردن»؛ پس معنای اصلیِ حکاکیِ اسیدی «خوراندنِ فلز به تیزاب» است و پیوندِ آن با ریشه از راهِ فعلِ سببی و وام‌گیری است نه وراثت. «tooth» از انگلیسی کهنِ tōþ (جمع tēþ) از ژرمنیِ *tanþuz است، با افتادنِ «ن» پیش از «ث» و کشیده‌شدنِ واکه در جبرانِ آن؛ و «tusk» از انگلیسیِ کهنِ tūsc/tūx، صورتِ قلب‌شدهٔ همان *tunþ-sk-. هر چهار واژه در پیوستِ واتکینز ذیلِ ed- و dent- آمده‌اند. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. ed- gives EAT and ETCH; s.v. dent- gives TOOTH and TUSK — the four English words of this box.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein s.v. etch (KLN_1966.txt line 13712; KLN_1971.txt line 85951)\",\n       \"stance\": \"partial\",\n       \"note\": \"'etch, tr. and intr. v., to engrave with acid. — Du. etsen, \\\"to etch\\\", fr. G. ätzen, \\\"to corrode\\\", fr. MHG. etzen, fr. OHG. azzōn, prop. \\\"to feed, bait\\\", causative of eʒʒan, \\\"to eat\\\". See eat.' Same root, but through Dutch and German rather than by native descent.\"\n      },\n      {\n       \"src\": \"SKT\",\n       \"where\": \"Skeat s.v. eat, tooth, tusk (SKT.txt)\",\n       \"stance\": \"supports\",\n       \"note\": \"Skeat gives eat < AS. etan, cognate with Lat. edere, Gk. edein, Skt. ad; tooth < AS. tōð, Lat. dens, dentis.\"\n      }\n     ]\n    },\n    {\n     \"id\": 14,\n     \"lang\": \"Latin\",\n     \"words\": \"ed-ere; dent\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin edō, ēsse (later edere), ēdī 'to eat' continues the athematic present *h₁ed-mi/*h₁és-ti almost intact — ēst 'he eats' is the direct match of Skt. átti and Hittite ēzzi, and the long ē of ēsse is either inherited or Lachmann-lengthened (Walde-Pokorny I 118 discusses both). dēns, gen. dentis 'tooth' is the full grade *dent- of the same participle *h₁dónt-, with the regular Latin loss of the initial laryngeal-plus-e; the stem dent- is what surfaces in all the derived vocabulary. Both are Watkins' Latin entries under ed- and dent-, and Nourai's citation 'AHD' is exactly right for them.\",\n     \"derivation_fa\": \"لاتینِ edō، ēsse (بعدها edere)، ēdī «خوردن» ستاکِ بی‌میانجیِ *h₁ed-mi/*h₁és-ti را تقریباً دست‌نخورده نگه داشته است: ēst «می‌خورد» عیناً برابرِ átti سنسکریت و ēzzi هیتی است، و «ē»ی کشیدهٔ ēsse یا کهن است یا برآمده از قاعدهٔ لاخمان (والده-پوکورنی جلد ۱ ص ۱۱۸ هر دو رأی را می‌آورد). dēns با ستاکِ dent- «دندان» درجهٔ کاملِ همان اسمِ فاعلِ *h₁dónt- است، با افتادنِ حنجریِ آغازین در لاتین؛ همین ستاکِ dent- است که در همهٔ مشتق‌ها پیدا می‌شود. هر دو واژه در پیوستِ واتکینز ذیلِ ed- و dent- آمده‌اند، پس ارجاعِ نورایی به AHD درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"'2. Latin edere, to eat: EDACIOUS, EDIBLE, ESCAROLE, ESCULENT, ESURIENT; COMEDO, COMESTIBLE, OBESE' (s.v. ed-) and '3. Full-grade form *dent- in Latin dēns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE …' (s.v. dent-).\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW 287 (POK_01.txt \\\\f-page 300)\",\n       \"stance\": \"supports\",\n       \"note\": \"'lat. edō, ēs, ēst usw. \\\"essen\\\" (Länge des e entweder alt oder nach der sog. Lachmannschen Regel zu erklären …); Perf. ēdī, osk. Infin. edum'.\"\n      },\n      {\n       \"src\": \"SYN\",\n       \"where\": \"Buck 5.11 (SYN.txt line 8318 ff.)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Lat. ēsse, late edere, Osc. edum' under 'IE *ed-. Walde-P. 1.118'.\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Walde-Pokorny I 118\",\n       \"stance\": \"supports\",\n       \"note\": \"'lat. edo, es, est usw. „essen“ … osk. Inf. edum'.\"\n      }\n     ]\n    },\n    {\n     \"id\": 15,\n     \"lang\": \"English\",\n     \"words\": \"edible; dental, denture\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are Latinate, entering English through learned channels rather than by descent. edible (1590s) is Late Latin edibilis 'eatable', from edere. dental is Medieval/New Latin dentālis, from dēns, dentis, first used of the teeth in the 16th century and of speech sounds soon after. denture is a 19th-century borrowing from French denture 'set of teeth', formed on French dent < Latin dēns with the suffix -ure (< Latin -ūra). Watkins lists EDIBLE under ed- and DENTAL under dent-, which is Nourai's chart exactly, although he gives no reference on this box.\",\n     \"derivation_fa\": \"هر سه واژه از راهِ لاتین و به‌صورتِ وامِ فرهیخته وارد انگلیسی شده‌اند، نه از راهِ وراثت. «edible» (حدود ۱۵۹۰ م) از لاتینِ متأخرِ edibilis «خوردنی» از edere است؛ «dental» از لاتینِ میانه/نوِ dentālis از dēns, dentis که نخست در سدهٔ شانزدهم دربارهٔ دندان و اندکی بعد دربارهٔ آواهای دندانی به کار رفت؛ و «denture» وامِ سدهٔ نوزدهم از فرانسویِ denture «دست‌دندان» است که خود از dentِ فرانسوی (< dēns لاتین) با پسوندِ -ure (< -ūra لاتین) ساخته شده. واتکینز EDIBLE را ذیلِ ed- و DENTAL را ذیلِ dent- می‌آورد، یعنی همان چیزی که نمودار نشان می‌دهد؛ هرچند نورایی برای این جعبه هیچ مأخذی نداده است. ادعای او درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"None\",\n       \"status\": \"not_checked\",\n       \"note\": \"no reference on this node; the chain is covered by the AHD citation of the parent Latin box and by Klein below.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein s.v. edible and denture (KLN_1966.txt lines 12639, 10879)\",\n       \"stance\": \"supports\",\n       \"note\": \"'edible, adj. — Late L. edibilis, \\\"eatable\\\", fr. L. edere, \\\"to eat\\\". See eat and cp. comedo, comestible, esculent, obese.' and 'denture, n., a set of teeth, esp. a set of false teeth. — F., fr. dent, \\\"tooth\\\". See dent … and -ure.'\"\n      },\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985 s.v. ed- and dent-\",\n       \"stance\": \"supports\",\n       \"note\": \"EDIBLE listed under ed-; DENTAL, DENTATE, DENTI-, DENTICLE under dent-.\"\n      }\n     ]\n    }\n   ]\n  }\n ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-147.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-05T20:30:50.860Z] TOOL RESULT

```
JSON OK
```


## [2026-09-05T20:30:54.646Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 tools/verify_check.py 147"
}
```


### [2026-09-05T20:30:56.651Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'transcription_suspect': 1, 'disputed': 1, 'plausible': 3, 'confirmed': 10}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 10, 'partial': 3, 'not_found': 2, 'not_checked': 3}
books consulted: {'partial': 5, 'supports': 29, 'silent': 8} | by book: {'KLN': 6, 'PLA': 5, 'HUB': 3, 'ARY': 3, 'HRN': 3, 'LKT': 3, 'BRT': 2, 'BQT': 2, 'POK': 2, 'WLD': 2, 'PHD': 1, 'NYB': 1, 'AFA': 1, 'MON': 1, 'WEB': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'HENNING': 1, 'SKT': 1, 'SYN': 1, 'AHD': 1}
```


## [2026-09-05T20:31:01.921Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"alfalfa\" WEB_vol1.txt | head -5; echo \"---SKT---\"; grep -n \"^eat,\\|eat, v\\|tooth, s\\|tusk, s\" SKT.txt | head -5; grep -n -i \"tooth.*Lat. dens\\|A.S. tôð\" SKT.txt | head -5"
}
```


### [2026-09-05T20:31:02.025Z] TOOL RESULT

```
87962:hay’fiéld, z. a field in which grass, alfalfa, etc. is grown for hay, or a field on which hay is cured and stored.
110146:3. ed; divided into ee es 20ans equivalent in extent to the Discophora. luck’y, 4.; comp: $ ZN lū-cērne’, n. [Fr.] alfalfa, Medicago sativa, a 1. having good luck; fortunate. nately 2. happening or resulting
---SKT---
```


## [2026-09-05T20:31:06.790Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"EAT, to consume\\|EAT,\" SKT.txt | head -5; echo ---; grep -n \"TOOTH\" SKT.txt | head -5; echo ---; grep -n \"TUSK\" SKT.txt | head -3"
}
```


### [2026-09-05T20:31:06.925Z] TOOL RESULT

```
27:REV.  WALTER  W.  SKEAT,  LiTT.D.,  LL.D.
---
---
```


## [2026-09-05T20:31:10.330Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^Eat\\. \\|Eat,  to\\|Eat\\.  (E\" SKT.txt | head -5; grep -n -i \"Tooth\\.\" SKT.txt | head -5; grep -n -i \"Tusk\\.\" SKT.txt | head -5"
}
```


### [2026-09-05T20:31:10.411Z] TOOL RESULT

```
3327:Cheat,  to  defraud.  (F.-L.)  Cheat  is merely  short  for  escheat ;  cf.  M.  E.  chete,  an escheat  (Prompt.  Parv.).  The  eickeaters were  often  cheaters-,  hence  the  verb.  See osoheat,  entered  under  Codenco.
5459:■  Drowse,  Drowse ;  act  Dreary. Drub,  to  beat.  (E.)  Prov.  E.  Jrah,  to beat.  A  secondary  verb,  due  lo  A.  S. Ktioog  vb.  drepan  ipt  C  dtvp),  to  beat.  + Iccl,  drrpa,  to  kill,  slay ;  Sned.  drahda,  to hit,  dnipa,  to  kill ;  Dan.  drahe,  to  kill.  G. tfxpm,    to    hiu       (Base     DRAP.)       Sec
5647:Eat.  tE )     M.  E  <{tn     A    >  ^  :
8113:fuse,  Swcil.  giisa,  to  guc»s.+  Du.  gissem, eel  giska.    Allied  to  Dan.  gjeae.  to  guess ; the  Iccl.  giika  stands  for  git-ska  *,  i.e.  to If)  to  get,  from  gtta^  to  get.    Thus  gtuss is  the  dcsiderative  ot  get ;  see  Got. Gueat.  (E)    M.  E.^j/.    A.S.ga'sf,ges/.
19706:tidy,  leasonable,  neat.  (E.)  M.  E.  tidy, seasonable,  from  M.  EL  tid  or  tide,  time; see  Tide.  +  Dii.  tijdig,  Dan.  Swed.  tiiHg, G.  -iiti^,  timely.
5648:€tcn%  Iccl.  eta,  Swed.  dta.  D.. itan,  G-  etsen,  L.  tJen,  Gk.  *-«:>,  oki  i to  cat     ^V  AD.)     See  Tooth.
9418:Jaff,  a  notch,  tooth.  (C.)  Irish  gstg,  a ficleft,  from  ga^gtum.  1  >plit.  notch  :  W.  gag Gael,  gag,  an  aperture,  cleft,  chink  ;  Gael. gagt  to  split,  notch.
11210:Mastodon,  an  extinct  elephant  (Gk.) Named  from  tlic  nipiile-like  projections  on Its  molar  teeth.  — Glc.  fMurr-^t,  the  female breast;  ddoi*-,  short  for  68oifr-i  stem  of Uffit,  s  tooth;  tec  Tooth.
19084:Tog.  a  point  of  metal  at  the  end  of  a lace,  &c.  (Scand.)  'An  aglet  or  tag  of a  poynt;'  Barct  (1580).  —  Swed,  tagg,  a prickle,  point,  tootfa.4-Low.  G.  takk^  point, tooth.  Prob.  of  Celtic  origin  ;  tec  Taok. J>6r.  tag-rag,  for  tag  anJ  ni^*  every  ap- |}endage  and  shred.
19744:A.  5.   fitvi.  +    i toolb  of  a  t  ake      1  '1  vb.  allied ' a  tooth,  and  to  Tooth.
20340:^X*uak    (E.)    A.  S.  ftwr,  usually  spelt /tfjr, l»o  ^i»<#r,  a  tusk.      rrob.  for  /wise*,  as  if L  double  tooth  :*  from  A.  S.  twis,  double, lird  to  fwtf  two,     bee  Two. %iaBle ;  see  Touse, ^!Put.  an  exclamation  of  impatience  (E.) -f.  K.  fruf  (the  same) ;  and  cf.  tush. ^Tutelar,     Tutela^re,     Tutor ;     sec ^nltion.
```


## [2026-09-05T20:31:18.695Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"alfalfa\" FSD_vol1.txt | head -5"
}
```


### [2026-09-05T20:31:18.746Z] TOOL RESULT

```
10118:alfalfa
18060:Alfalfa-a  
26400:cochyta ,   usually  manifested  by  spots  on  the  leaves  or  other  -ase,  sujjtr.  Cpcrrt.  Used  In  naming  enzyms.  It  Is  sometimes organs  or  the  host  plant.  Alfalfa,  peas,  and  strawberries  added  to  a   part  or  the  whole  of  the  name  of  the  compound
40471:ber-seem',  l   bsr-slm';  2   ber-eCm',  n.  A   clover  (Trtfolluni alexandrtnum)  grown  as  forage  in  the  Nile  valley  and  the S.  W.  United  States.  It  la  better  forage  than  alfalfa, ber'serk,  )   1   bur'sark,  -sark-ar;  2   b6r'serk,  -serk-er, bcr'serk-erx,  J   n.  1.  In  Norse  legend,  a   warrior  who fought  with  a   frenzied  fury  known  as  the  “   berserker rage,”  who  could  assume  the  form  and  ferocity  of  wild beasts,  and  whom  fire  and  iron  could  not  harm.
60005:Caterpillars  are  worm-like  and  have  three  pairs  of  true legs,  and  several  pairs  of  proIeg3  or  fleshy  supports,  under the  abdomen.  They  feed  chiefly  on  leaves  and  vegetables, and  are  usually  designated  by  the  name  of  their  food-plant. 2.  The  larva  of  some  other  insects,  as  of  a   saw-fly  or tenthredinid.  3.  [Prov.  Eng.]  A   cockchafer.  4.  (1) A   plant  of  the  European  genus  Scorpiurus,  of  the  bean family,  with  caterpillar-like  pods.  (2)  Alfalfa  or  lucern.
```


## [2026-09-05T20:31:21.494Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10110,10125p' FSD_vol1.txt"
}
```


### [2026-09-05T20:31:21.548Z] TOOL RESULT

```
now  chiefly  poetical.  Tillage  refers  directly  to  the  work bestowed  upon  the  land,  as  plowing,  manuring,  etc.;  culti- vation refers  especially  to  the  processes  that  bring  forward the  crop:  we  6peak  of  the  tillage  of  the  soil,  the  cultivation of  corn;  we  speak  also  of  land  as  in  a   state  of  cultivation, under  cultivation,  etc.  Culture  is  now  applied  to  the  care- ful development  of  any  product  to  a   state  of  perfection, especially  by  care  through  successive  generations;  the  choice varieties  of  the  strawberry  have  been  produced  by  wise and  patient  culture;  a   good  crop  in  any  year  is  the  result  of good  cultivation.
—   Department  of  Agriculture,  see  department.
Some  Terms  Used  in  Agriculture.
Words  and  phrases  which  are  not  self-explaining  will  be found  defined  In  their  appropriate  vocabulary  places,  often with  additional  information  as  to  growth,  styles,  varieties, etc.  Some  of  the  most  common  and  self-explaining  words
pi.)  Bot.  1.  Any  species  of  Agri- moma.  2.  Any  one  of  several  plants of  other  genera;  as,  the  hemp- agrimony,  w&touagrimony,  etc.— ag'rI-mo-nr*grass",  n.  The  colic- root  ( Alctrls  farinosa ).  a.»rootf. a-grln',  l   a-grln';  2   a-grln',  adv.  &   a. In  the  act  of  grinning;  grinning.
tAgrlmony.
1
and  phrases,  as  well  as  terms  common  to  other  departments  Ag"rI-o-clice/rI-dse,  1   ag'n-o-kl'n-di;  2 and  trades,  are  omitted.  AD*riww>a'riwis  n   -ni  7^1  a   fnmuw  »«
alfalfa
almond
apple,  a.-peeler
apricot
artichoke
asparagus
aveler
avocado
```


## [2026-09-05T20:31:25.700Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"al-fal\\|alfal'fa\\|al'fal\" FSD_vol1.txt | head -5"
}
```


### [2026-09-05T20:31:25.750Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:31:38.940Z] TOOL CALL #95: Bash

```json
{
 "command": "python3 - <<'PY'\nimport json\np='data/verification/page-147.json'\nd=json.load(open(p))\nnodes={n['id']:n for n in d['entries'][0]['nodes']}\n\n# node 10: fix the WEB claim\nfor c in nodes[10]['consulted']:\n    if c['src']=='WEB':\n        c['where']=\"Webster's New Twentieth Century Dictionary vol.1 (WEB_vol1.txt) and Funk & Wagnalls (FSD_vol1.txt)\"\n        c['stance']=\"silent\"\n        c['note']=\"neither OCR yields an 'alfalfa' headword with an etymology: WEB_vol1 has only 'lucerne, n. [Fr.] alfalfa, Medicago sativa' (line 110146) and incidental uses (line 87962); FSD_vol1 has 'alfalfa' only in an agriculture word-list panel (line 10118) and a picture caption (line 18060). No disagreement, just no entry found.\"\n\n# node 13: correct the Skeat note\nfor c in nodes[13]['consulted']:\n    if c['src']=='SKT':\n        c['where']=\"Skeat s.v. Eat (SKT.txt lines 5647-5648) and s.v. Tusk (line 20340)\"\n        c['stance']=\"partial\"\n        c['note']=\"'Eat. (E.) M.E. eten … Icel. eta, Swed. äta, Du. eten, G. essen, L. edere, Gk. ἔδω … to eat. (√AD.) See Tooth.' — supports eat and the eat/tooth link. But Skeat's tusk is different: 'Tusk. (E.) A.S. tūsc, usually spelt tūx … Prob. for *twisc, as if \\\"double tooth\\\": from A.S. twis, double, allied to twā, two. See Two.' — i.e. Skeat (1911) took tusk from the word for 'two', not from *tunth-sk-; Watkins' derivation (which Nourai follows) is the later and now standard one, and Watkins himself marks it 'perhaps'.\"\n\njson.dump(d,open(p,'w'),ensure_ascii=False,indent=1)\nprint('written')\nPY\npython3 -m json.tool data/verification/page-147.json >/dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 147"
}
```


### [2026-09-05T20:31:40.759Z] TOOL RESULT

```
written
JSON OK
nodes verified: 15/15
node verdicts: {'transcription_suspect': 1, 'disputed': 1, 'plausible': 3, 'confirmed': 10}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 10, 'partial': 3, 'not_found': 2, 'not_checked': 3}
books consulted: {'partial': 6, 'supports': 27, 'silent': 9} | by book: {'KLN': 6, 'PLA': 5, 'HUB': 3, 'ARY': 3, 'HRN': 3, 'LKT': 3, 'BRT': 2, 'BQT': 2, 'POK': 2, 'WLD': 2, 'PHD': 1, 'NYB': 1, 'AFA': 1, 'MON': 1, 'WEB': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'HENNING': 1, 'SKT': 1, 'SYN': 1, 'AHD': 1}
```


## [2026-09-05T20:31:58.718Z] AGENT

Page 147 (book p. 117) verified — `data/verification/page-147.json`, `verify_check.py 147` shows 0 PROBLEM lines.

**Counts** — 1 root: confirmed. 15 nodes: 10 confirmed, 3 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 10 supports / 3 partial / 2 not_found / 3 not_checked. 42 book consultations across 21 books.

**Flagged items**
- **transcription_suspect — node 1 (Avestan "xarka-asa : eating bird")**: `error_in: "book"`. The printed page really shows *xarka-asa* (rendered at 200 dpi, copy at `data/verification/sources/refs/ocr/BOOK/147.png`), so the extraction is faithful; the Avestan word is **kahrkāsa-** 'vulture' = *kahrka-* 'hen' + *-āsa-* 'eating', i.e. 'fowl-EATER', not 'eating bird'. Nourai's own source (Mo'in, BQT 1624) and Bartholomae col. 456 both print *kahrka*; Nourai himself writes *kahrkatât* on book p. 227.
- **disputed — node 2, the word آش**: Wiktionary/Doerfer put a Turkic loan (*aš*) first and note the long ā is unexplained under *ad-*; Mo'in (BQT 44) and Aryanpur keep the inherited derivation. The other two words of the box (کرکس، ناشتا) are confirmed. Also worth knowing: Wiktionary's ناشتا entry cites Nourai p. 117 — this very chart — so it is not independent.
- **plausible — node 3** ("Avestan aspa-asa"): the compound is unattested in Avestan; Watkins, Wiktionary (PIr *HacwaHastiš*), Mo'in and Aryanpur all reconstruct *\*aspa-asti-* / Old Median *\*aspāstiš* — the -ti- is what yields the -t of Pahlavi *aspast*.
- **plausible — node 6** ("Syriac pespesta"): the Syriac word is *ʾespestā/ʾaspastā*; the p- form Nourai prints is the **Coptic** ⲡⲉⲥⲡⲉⲥⲧⲁ (p-espesta), which is what explains Arabic f-.
- **plausible — node 11** (Sogdian): Gharib p. 70 no. 1767 does have ʾšpʾδy and does compare Persian āš, but glosses it 'part, portion ?, bowl ?' with question marks throughout, not 'food, dish'. Scan transcript saved to `sources/refs/ocr/SOD/70.vision.txt`.

**Citation errors of Nourai's (not extraction errors)**: `BQT:1624` is the کرکس page — it supports nodes 1–2 but not node 8 (فسفسه is at BQT p. 1489) and not node 4.

**No extraction errors found** — every form, gloss, Persian script string, quote and reference in `data/extracted/batch/page-147.json` matches the printed chart.
