# Verification process log — verify-page-165


## [2026-09-05T20:33:19.498Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 165 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-165.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-165.json. Write /home/sfmqrb/git/rishe/data/verification/page-165.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 165` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:33:21.433Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:33:22.127Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:33:22.140Z] TOOL RESULT

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


## [2026-09-05T20:33:22.345Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-165.txt"
}
```


### [2026-09-05T20:33:22.364Z] TOOL RESULT

```
1	=== PDF page 165 (book page 135) ===
2	--- entry 0 ---
3	ROOT [Arabic] F.r.q, Tafrîq : F.r.q: to split, divide. Tafrîq: distribution.  (refs KLN:1637)
4	#1 (parent #0) [Persian] refs=FVA:313 | farq «فرق» : difference, dividing line ; forqân «فرقان» : ability to distinguish (between good and bad), Koran | extra: فارق ، فاروق ، تفریق ، تفرقه ، فراق ، مفارقت ، متفرّق ، متفرّقه ، فرقه
5	#2 (parent #0) [Italian] refs=KLN:1637 | traffico : traffic ; traficare : to trade | NOTE: KLN:1637 claims "traffico" is possibly from Arabic "tafrîq: distribution", influenced by Latin "traficere: to take over".
6	  #3 (parent #2) [French] refs=KLN:1637 | trafic
7	    #4 (parent #3) [Persian] refs=None | trâfîc «ترافیک» : traffic
8	    #5 (parent #3) [English] refs=KLN:1637 | traffic
9	--- entry 1 ---
10	ROOT [Avestan] Fšân : spread, sprinkle  (refs HRN:24)
11	#1 (parent #0) [Avestan] refs=HRN:24 | aiwi-fšân : spread over, spread around ☞Ambhi
12	  #2 (parent #1) [Pahlavi] refs=BQT:1492 | afšântan : to sprinkle
13	    #3 (parent #2) [Persian] refs=HRN:24; BQT:1492; AEF:137 | afšândan «افشاندن» : to sprinkle, scatter ; afshân «افشان» : scattered ; afšŭn «افشون» : rake (for spreading sand, etc.) | extra: فشاندن
14	
```


## [2026-09-05T20:33:25.868Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-165.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read page 165 JSON and source matrix"
}
```


### [2026-09-05T20:33:25.913Z] TOOL RESULT

```
{
  "pdf_page": 165,
  "book_page": 135,
  "entries": [
    {
      "root": {
        "name": "F.r.q, Tafrîq",
        "lang": "Arabic",
        "refs": "KLN:1637",
        "gloss": "F.r.q: to split, divide. Tafrîq: distribution."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "FVA:313",
          "words": [
            {"translit": "farq", "gloss": "difference, dividing line", "script": "فرق"},
            {"translit": "forqân", "gloss": "ability to distinguish (between good and bad), Koran", "script": "فرقان"}
          ],
          "script_extra": "فارق ، فاروق ، تفریق ، تفرقه ، فراق ، مفارقت ، متفرّق ، متفرّقه ، فرقه",
          "note": null,
          "quote": {
            "text": "نور هر گوهر کزو تابان شدی - حق و باطل را از او فرقان شدی",
            "poet": "Molavî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Italian",
          "refs": "KLN:1637",
          "words": [
            {"translit": "traffico", "gloss": "traffic", "script": null},
            {"translit": "traficare", "gloss": "to trade", "script": null}
          ],
          "script_extra": null,
          "note": "KLN:1637 claims \"traffico\" is possibly from Arabic \"tafrîq: distribution\", influenced by Latin \"traficere: to take over\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": "KLN:1637",
          "words": [
            {"translit": "trafic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "trâfîc", "gloss": "traffic", "script": "ترافیک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:1637",
          "words": [
            {"translit": "traffic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Fšân",
        "lang": "Avestan",
        "refs": "HRN:24",
        "gloss": "spread, sprinkle"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:24",
          "words": [
            {"translit": "aiwi-fšân", "gloss": "spread over, spread around", "script": null, "see": ["Ambhi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:1492",
          "words": [
            {"translit": "afšântan", "gloss": "to sprinkle", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:24; BQT:1492; AEF:137",
          "words": [
            {"translit": "afšândan", "gloss": "to sprinkle, scatter", "script": "افشاندن"},
            {"translit": "afshân", "gloss": "scattered", "script": "افشان"},
            {"translit": "afšŭn", "gloss": "rake (for spreading sand, etc.)", "script": "افشون"}
          ],
          "script_extra": "فشاندن",
          "note": null,
          "quote": {
            "text": "اگر شراب خوری جرعه ای فشان بر خاک - از آن گناه که خیری رسد به غیر چه باک",
            "poet": "Hâfez"
          }
        }
      ]
    }
  ]
}
=== MATRIX ===
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


## [2026-09-05T20:33:30.267Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVA','HRN','BQT','AEF','FVQ']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900]); print()\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-05T20:33:30.529Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T20:33:32.202Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فر

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (19
```


### [2026-09-05T20:33:32.243Z] TOOL RESULT

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


## [2026-09-05T20:33:39.644Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"traffic\" KLN_1966.txt | head -30; echo \"=== 1971 ===\"; grep -n -i \"traffico\\|traficare\\|traficher\\|trafic\" KLN_1971.txt | head -20",
 "description": "Grep Klein for traffic"
}
```


### [2026-09-05T20:33:39.711Z] TOOL RESULT

```
4422:thrown.  —  L.,  fr.  Gk.  flapattpov,  ‘pit,  gulf, cleft’,  rel.  to  Homeric  Pepsbpov,  of  s.m.,  fr.  I.-E. base  *gwer-,  ‘to  devour’,  whence  also  Popup, ‘voracious’,  PpSfjta,  ‘food’,  lit.  ‘that  which  is eaten’,  L.  vorare,  ‘to  devour’.  See  voracious  and cp.  words  there  referred  to. barato,  n.,  money  given  to  bystanders  by  a  winner at  the  gaming  table.  —  Sp.,  from  the  adj.  barato , ‘cheap’,  fr.  baratar,  ‘to  barter,  traffic’,  which prob.  derives  fr.  Gk.  TTpa-trav,  ‘to  do,  perform’. See  practical.
5663:brinjarry,  also  binjarree,  n.,  a  dealer  in  grain  and salt  (Anglo-Ind.)  —  Hind,  banjara,  lit.  ‘one  who carries  on  trade’,  fr.  OI.  vanijya,  ‘trade,  traffic’ (fr.  van//',  ‘merchant’),  and  karah,  ‘doer’,  which is  rel.  to  kfnoti,  ‘he  does,  makes,  accomplishes’. See  Sanskrit  and  cp.  Chamar.  The  word  brinjarry was  influenced  in  form  by  Pers.  birinj,  ‘rice’.
8369:commerce,  n.  —  F.,  fr.  L.  commercium,  ‘trade, traffic,  intercourse,  commerce’,  fr.  con-  and merx,  gen.  mercis,  ‘merchandise’.  See  mercantile. Derivatives:  commerce,  intr.  v.,  to  have  inter¬ course,  commerc-iat,  adj.  and  n.,  commercial¬ ism,  n.,  commercial-ist,  n.,  cammercial-ize,  tr. v.,  commercial-ity,  n.,  commercial-ly,  adv. comminate,  tr.  and  intr.  v.,  to  threaten;  to  ana¬ thematize.  —  L.  comminatus,  pp.  of  commindri, ‘to  threaten’,  fr.  com-  and  minari,  ‘to  threaten’. See  minatory  and  cp.  menace, commination,  n.,  a  threat.  —  L.  comminatio,  gen. -onis,  fr.  comminatus,  pp.  of  commindri.  See prec.  word  and  -ion.
23519:Derivatives :  Mephistophele-an,  Mephistopheli- an,  Mephistophel-ic,  Mephistophel-ist-ic,  adjs. mephitic,  adj.,  exhaling  poison  from  the  earth;  of poisonous  smell.  —  Late  L.  mephiticus,  fr.  L. mephitis.  See  mephitis  and  adj.  suff.  -ic. mephitis,  n.,  poisonous  exhalation  from  the  earth ; a  poisonous  smell.  —  L.  mefitis  (less  correctly spelled  mephitis) ;  of  Oscan  origin, mercantile,  adj.,  commercial.  —  F.,  fr.  It.  mercan¬ tile,  fr.  L.  mercans,  gen.  -antis,  pres.  part,  ol mercari,  ‘to  trade,  traffic,  buy,  purchase’,  fr. merx,  gen.  mercis,  ‘merchandise,  wares’,  which is  of  uncertain  origin.  Cp.  market,  mart,  Mer¬ cedes,  mercenary,  merchandise,  merchant,  mercy, amerce,  commerce.
24248:moneyer,  n.,  one  who  coins  money.  —  ME.  mon- eyer,  fr.  OF.  monoler  (F.  monnayeur ),  fr.  Late  L. monetarius,  ‘master  of  the  mint,  minter,  coiner  . See  money  and  agential  suff.  -er. monger,  n.  —  ME.  mangere,  mongere,  fr.  OE. mangere,  ‘merchant,  trader’,  fr.  mangian,  to traffic,  trade’,  fr.  L.  mango,  ‘a  dealer  who  pol¬ ishes  his  wares,  trader,  trafficker,  a  slave  trader  , which  is  prob.  borrowed  fr.  Gk.  *p.ayT“v^  a word  rel  to  ptdyyavov,  ‘any  means  for  tricking or  bewitching,  philter,  drug’,  fr.  I.-E.  base
25154:Derivative:  negotiabil-ity,  n. negotiate,  tr.  and  intr.  v.  —  L.  negotiatus,  pp.  of negotiari,  ‘to  carry  on  business,  deal,  trade, traffic’,  fr.  negotium,  ‘business,  trade’,  lit.  ‘lack of  leisure',  from  the  sentence  neg'otium  est, ‘there  is  no  leisure’.  The  particle  neg'  derives  fr. *negi,  ‘not’ ;  see  negate.  For  the  etymology  of  L. otium,  ‘leisure’,  see  otiose,  for  the  ending  of negotiate  see  verbal  suff.  -ate. negotiation,  n.  —  L.  negotidtid,  gen.  -onis,  ‘busi¬
25155:ness,  traffic’,  fr.  negotiatus,  pp.  of  negotiari, ‘to  carry  on  business’.  See  prec.  word  and  -ion.
39777:traffic,  n.  —  MF.  trafique  (F.  trafic),  fr.  It.  tr  of¬ fice,  which  prob.  derives  fr.  Arab,  tafrtq,  ‘distri¬ bution’,  verbal  noun  of farraqa,  ‘he  distributed’, II  (=  frequentative  or  intensive  conjugation)  of faraqa,  ‘he  split,  divided’ ;  influenced  in  form  by assumed  L.  traficere  (for  * transftcere),  ‘to  make over’  (see  trans-  and  fact).  Arab,  faraqa  is  rel.  to Heb.  pardq,  ‘he  tore  away  (esp.  the  yoke),  he rescued’,  perdq,  ‘he  tore  off’,  Aram.  plraq,  ‘he rescued’,  Syr.  plraq,  ‘he  withdrew  (intr.);  he  re¬ deemed,  rescued',  Ethiop.  faraqa,  ‘he  set  free’. Derivatives:  traffic,  intr.  and  tr.  v.  (—  F.  trafi- quer),  traffic-able,  adj.,  traffick-er,  n. tragacanth,  n.,  gum  obtained  from  the  plant Astragalus.  —  F.  tragacanthe,  name  of  the  plant, lit.  ‘goat’s  thorn’,  fr.  Gk.  xpdeyos,  ‘he-goat’,  and axavffa,  ‘thorn’.  See  tragic  and  acanthus  and cp.  Tagetes  and  the  second  element  in  Tauro- tragus.
=== 1971 ===
251082:traffic, n. — MF. trafique (F. trafic), fr. It. traf- 
251087:assumed L. traficere (for *transficere), ‘to make
```


## [2026-09-05T20:33:40.937Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"afš\\|afsh.nd\\|afshand\\|fšan\\|afsandan\" HRN.txt | head -40",
 "description": "Grep Horn for afšāndan"
}
```


### [2026-09-05T20:33:41.028Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:33:46.945Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==46' HRN.txt | head -80",
 "description": "Print Horn leaf 46"
}
```


## [2026-09-05T20:33:48.614Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"traffic\" KLN_1966.txt | awk -F: '{print $1}' | while read l; do awk -v L=$l 'NR<=L{n+=gsub(/\\f/,\"\\f\")} END{print \"formfeeds before line \" L \": \" n}' KLN_1966.txt; done 2>/dev/null | tail -3",
 "description": "Find leaf number for traffic in Klein"
}
```


### [2026-09-05T20:33:49.425Z] TOOL RESULT

```
— 24 —
102. ef San den ausschütten', ^'sawrfew.
aw. aiwi + ßünayeinü *sie weiden aus , yt. 14, 56
(Geldner, 3 Yasht, 88) (?); phlv. aßäntan,
103. ef gen den 'wegwerfen', ßgenden^ ewgenden (AM.),
jn::5x (Is. 14, 12).
Kaum etwas anderes als aw. aiwi + [^kan-, wenn-
schon die Bedeutung nicht passt; phlv. afgantan
(Bund.) 'wegwerfen'.
Ein ganz anderes Verbum scheint efgenden, ewgenden
einfüllen, auffüllen zu sein, vergl. AM. 82 Zeile 1 *in
die Harnröhre einführen, einfüllen , 145 Zeile 3 v. u.
'in die Nase einführen, einfüllen* u. ö. (mit und ohne
bäz, letzteres z. B. 50 Zeile 4)^). Post häz ewgened
bei demselben Autor ^bewirkt Abschuppung der Haut'
(140 Zeile 2) gehört natürlich zu efgenden wegwerfen'.
Die Bedeutung auffüllen findet sich dagegen noch in
htm efgenden 'das Fundament auffüllen, den Grund
legen* (Sahn. I, 8 Vers 42 u. o.), synonym mit pei
efgenden (Sahn. I, 48 Vers 262). Ebenso wird die
bei AM. häufige Bedeutung verursachen, z. B. 173
Zeile 8 fBlasenstein), 164 Zeile 10 ('Jucken), 243
Zeile 4 v. u. ('Krankheit') hierher gehören.
Efgenden 'einfüllen, auffüllen' wird zu np. ägenden
(No. 41) zu stellen sein.
104. ek 'Schimpf, Schande, Unglück', ak'^),
aw. aka- *böse. Böses; skr. aka- 'Schmerz, Sünde'
(spät).
*) Als medicinischen t. t. vergl. Abdul Aohundow, Commentar
zum sog. Liber fundamentorum phaemaoologiae des Abu Mansur
Muwaffak-Ben- Ali-el-Hirowi , Dorpater medicinische Doctordissertation
1892, S. 18.
') FR und FJ haben die folgenden Belege (die zweite Stelle ist
in der Strassburger Handschrift des FJ sehr liederlich geschrieben):
äke n^reslde her tu ez men
sed bär^ tnerä zi tu resed äk
m
Sözeni, Metr. Hezej.
an flgende becäh^ behr-i ^em,
oän b^hä'kerd^ kern behezde direm
Senäl, Metr. Xeflf.
```


### [2026-09-05T20:33:51.361Z] TOOL RESULT

```
formfeeds before line 25154: 555
formfeeds before line 25155: 555
formfeeds before line 39777: 867
```


## [2026-09-05T20:34:05.739Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==868' KLN_1966.txt | grep -nE \"^[0-9]{3,4}|[0-9]{4}\" | head -20; echo \"---- head of leaf\"; awk 'BEGIN{RS=\"\\f\"} NR==868' KLN_1966.txt | head -5; echo \"---- tail\"; awk 'BEGIN{RS=\"\\f\"} NR==868' KLN_1966.txt | tail -5",
 "description": "Inspect Klein leaf 868 for page numbers"
}
```


### [2026-09-05T20:34:08.171Z] TOOL RESULT

```
7:tracheotomy,  n.,  incision  in  the  trachea  (surg.)  — Coined  by  the  German  surgeon  Lorenz  Heister (1683-1758)  in  1718  fr.  traeheo-  and  Gk.  -xopia,
14:1636
15:1637
---- head of leaf
 Compounded  of  trachelo-  and  Gk. -xopia,  ‘a  cutting  of’,  fr.  xoprj,  ‘a  cutting’.  See -tomy.
tracheo-,  before  a  vowel  trache-,  combining  form denoting  the  trachea.  —  See  trachea.
tracheocele
train  oil
tracheocele,  n.,  the  goiter  (med.)  —  Compounded of  traeheo-  and  Gk.  xr/.'/j,  ‘tumor,  hernia’.  See
---- tail
xpocyixo-,  fr.  xpaytx6p.  See  tragic, tragicomedy,  n.  —  MF.  (=  F.)  tragicomedie,  fr. Late  L.  tragicomoedia,  contraction  of  L.  tragi- cocomoedia.  See  tragico-  and  comedy.  The  con¬ traction  of  L.  tragicocomoedia  to  tragicomoedia in  Late  L.  is  due  to  haplology. tragicomic,  adj.  —  See  prec.  word  and  -ic. Derivatives:  tragicomic-al,  adj.,  tragicomic-al- ity,  n.,  tragicomic-al-ly,  adv. tragopan,  n.,  an  Asiatic  pheasant.  —  ModL.  tra- gopan,  fr.  Gk.  xpaydnav,  name  of  a  fabulous bird  of  Ethiopia,  lit.  ‘goat  of  Pan’,  fr.  xpayos, ‘he-goat’,  and  Ilav,  ‘the  god  of  the  woods  and fields’.  See  tragic  and  Pan.
Tragopogon,  n.,  a  genus  of  plants,  the  goat’s  beard (hot.)  —  ModL.,  lit.  ‘goat’s  beard’,  fr.  Gk. xpayo?,  ‘he-goat’,  and  rrclycov,  ‘beard’.  See tragedy  and  Pogonia.
tragus,  n.,  eminence  at  the  opening  of  the  external ear  ( anat .)  —  ModL.,  fr.  Gk.  xpayos,  prop,  ‘he- goat’  ;  so  called  from  the  bunch  of  hair  it  con¬ tains,  which  resembles  a  goat’s  beard ;  see  tragic and  cp.  antitragus.  In  its  anatomical  sense  the word  occurs  for  the  first  time  in  the  Onomasti- con  of  the  Greek  lexicographer  Julius  Pollux, who  lived  in  the  2nd  century, trail,  tr.  and  intr.  v.  —  ME.  trailen,  fr.  MF.  trail- lier,  trailler,  ‘to  tow  (a  boat)’,  fr.  VL.  *  tragulare, fr.  L.  tragula,  ‘a  kind  of  dragnet',  from  the  stem of  trahere,  ‘to  pull,  draw’.  See  tract,  ‘region’, and  cp.  train.  Cp.  also  drail.
Derivatives:  trail,  n.,  track,  trail-er,  n.,  trail-ing, adj.,  trail-ing-ly,  adv.
train,  tr.  and  intr.  v.  —  ME.  trainen,  fr.  MF. trainer  (F.  trainer),  ‘to  drag,  draw  long’,  fr.  OF., fr.  VL.  *traginare,  fr.  L.  trahere,  ‘to  pull,  draw’. See  tract,  ‘region’,  and  cp.  OProvenQ.  traginar, trainar,  Sp.  trajinar.  It.  trainare,  ‘to  drag,  trail’, which  all  derive  fr.  VL.  *traginare.  Cp.  entr
```


## [2026-09-05T20:34:18.356Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"furq[aā]n\\|Furqan\" FVQ_pages.txt | head -20",
 "description": "Grep Jeffery for furqan"
}
```


### [2026-09-05T20:34:18.414Z] TOOL RESULT

```
8142:jU^ (Furqan).
8147:and Aaron the Furqan and an illumination " (xxi, 49), and "We gave
8148:to Moses the Book and the Furqan " (ii, 50), where it would seem to
8159:grant you a Furqan and forgive your evil deeds." In viii, 42, however,
8160:where the reference is to the Battle of Badr, " the day of the Furqan,
8165:authorities. Tab. on ii, 50, says that Scripture is called Furqan
8245:conceived of his Furqan as associated with the revelation of the
```


## [2026-09-05T20:34:19.441Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"traffico\\|trafficare\\|traficare\" LKT.txt SKT.txt DEV.txt PHN.txt FSD_vol4.txt WEB_vol1.txt 2>/dev/null | head -20",
 "description": "Grep other dictionaries for traffico"
}
```


### [2026-09-05T20:34:19.505Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:34:21.709Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8130,8270p' FVQ_pages.txt",
 "description": "Read Jeffery furqan entry"
}
```


### [2026-09-05T20:34:21.752Z] TOOL RESULT

```
we note that the Christian forms give us the final J. In Gk. it is
<I>a/)aa)j>, in Syr. ^QL;2>, and in Eth. ?*}. The probabilities
are that it was borrowed from Syriac (Mingana, Syriac Influence, 81 ;
Sprenger, Leben, i, 66 ; Horovitz, JPN, 169).
There does not seem to be any well authenticated example of the
word in pre-Islamic times, for the oft quoted examples from Zuhair
and Umayya are spurious. 2 Sprenger has noticed the curious fact
that the name does not occur in the Sura of Joseph where we should
naturally expect it, which may indicate that the name was not known
to Muhammad at the time that story was composed, or may be was
not used in the sources from which he got the material for the story.
^-V
jU^ (Furqan).
ii, 50, 181 ; iii, 2 ; viii, 29, 42 ; xxi, 49 ; xxv, 1.
Discrimination.
In all the passages save viii, 42, it is used as though it means
some sort of a Scripture sent from God. Thus " we gave to Moses
and Aaron the Furqan and an illumination " (xxi, 49), and "We gave
to Moses the Book and the Furqan " (ii, 50), where it would seem to
1 As Noldcko showed in his essay Ober die Atnszlekiter, Gottingen, 1864, this
name is used by Arabic writers in a very loose way to cover all sorts of peoples of
the Near East of whose racial affinities they had no exact knowledge. The term is
used indifferently for Philistines, Canaanites, and Egyptians, and Bagh. in his note
on ii, 46, tells us that Pharaoh was the ruler of the Amalekite Copts !
2 Horovitz, KU 9 130, however, would defend the genuineness of one passage in
Umayya.226 FOREIGN VOCABULARY OF THE QUR ? AN
be the equivalent of Taurah. In iii, 2, it is associated with the Taurah
and the Injil, and xxv, 1, and ii, 181, make it practically the equivalent
of the Qur'an, while in viii, 29, we read, " if ye believe God, he will
grant you a Furqan and forgive your evil deeds." In viii, 42, however,
where the reference is to the Battle of Badr, " the day of the Furqan,
the day when the two hosts met," the meaning seems something quite
different.
The form of the word would suggest that it was genuine Arabic,
a form J^*i from (Jj*, and thus it is taken by the Muslim
authorities. Tab. on ii, 50, says that Scripture is called Furqan
because God J^Ub <J*^ Ut\ *>. ^J*> and as referrm S to Badr
it means the day when God discriminated (L?^) between the good
party and the evil (Raghib, Mufraddt, 385). In this latter case it is
tempting to think of Jewish influence, for in the account of Saul's
victory over the Ammonites in 1 Sam. xi, 13, where the Heb. text
reads ^K1BP3 71VWT\ HIPP nBW DT71, m the Targum it reads
wpnia mrr 121? fi war, where MPTIB or is
exactly J^a * jM
The philologers, however, are not unanimous as to its meaning.
Some took it to mean ^^ ; Baid. on xxi, 49, tells us that some said
it meant j^\ ^U, and Zam. on viii, 29, collects a number of other
meanings. This uncertainty and confusion is difficult to explain if
we are dealing with a genuine Arabic word, and is sufficient of itself
to suggest that it is a borrowed term. 2
Arguing from the fact that in the majority of cases it is connected
with Scriptures, Hirschfeld, New Researches, 68, would derive it
from D^(!?"1S, one of the technical terms for the divisions of the
1 Lidzbarski, Z8, i, 92, notes an even closer verbal correspondence with Ts. xlix, 8,
where for "pm?* niTW CTUl the Pesh. has ^Ziyl jl>ioZ)> ]iDQxOO.
2 This is strengthened by the fact that there are apparently ho examples of its
use earlier than the Qur'an. Fleischer, Kleinere Schrrften, ii, 125 ft'., who opposed
the theory that it is a foreign word, is compelled to admit that it was probably a
coining of Mubammad himself, f-'ee Ahrens, Vhristlwhe** 31, 32.FOREIGN VOCABULARY OP THE QUR'AN 227
text of the Hebrew Scriptures. 1 This, however, is rather difficult,
and Margoliouth, Mohammed, 145 (but see ERE, ix, 481 ; x, 538),
while inclining to the explanation from D^pIS, refers it, not to the
sections of the Pentateuch, but to a book of Sayings of the Jewish
Fathers, which Muhammad heard of from the Jews, and which he
may have thought of as similar to the Taurah and the Injil. This
theory is more probable than that of Hirschfeld, and has in its favour
the fact that resemblances have been noted between phrases and
ideas in the Qur'an and the well-known fTON ^pIS. 2 It also,
however, has its difficulties, and in any case does not explain the use
of the word in viii, 42.
Linguistically there is a closer equivalence in the Aram. Ip'lS,
]p"113 deliverance or redemption, and Geiger, 56 ff., 3 suggested this
as the source of the Arabic word. He would see the primary meaning
in viii, 29 " He will grant you redemption and forgive your evil
deeds," where the Targurnic fcWpllD would fit exactly (cf.
Ps. iii, 9, etc.). Nowhere, however, is JOSHIS used of revela-
tion, and Geiger is forced to explain jS^* in the other passages,
by assuming that Muhammad looked upon revelation as a means of
deliverance from error.
Geiger's explanation has commended itself to many scholars, 4
but Fraenkel, Vocab, 23, in mentioning Geiger's theory, suggested
the possibility of a derivation from Syr. (loioa, a suggestion
which has been very fruitfully explored by later scholars. 5 Not only
is lloiQS) the common word for salvation in the Peshitta and the
ecclesiastical writers (PSm, 3295), but it is the normal form in the
Christian-Palestinian dialect, and has passed into the religious
vocabulary of Eth. as C^1 (Noldeke-Schwally, i, 34) and
Armenian as ^/n_^u/V 6 It is of much wider use than the Rabbinic
1 So Grimmc, Mohammed, ii, 73, thinks it means sections of a heavenly book and
compares the Rabbinic plB, Xj^5 ; but see Rudolph, Abhangigkeit, 39.
2 Rudolph, Abhangigkeit, 11 ; Hirschfeld, Jiutrage, 58.
3 So Torrcy, Foundation, 48.
4 Ullmann, Der Koran (Bielefeld, 1872), p. 5 ; von Kremer, Ideen, 225 ; Sprenger,
LfJbfn, ii, 337 ff. ; Pautz, Offenbarung, 81.
5 Sehwally, ZDMG, Iii, 135 ; Knieschke, Erlosinqshhre des Koran (Berlin, 1910),
p. 11 fF. See also Wellhauson, ZDMG, Ixvii, 633 ; Massignon, Lexique, 52 ; Mingana,
Syriac Influence, 85.
6 Merx, Chrertomathia Targumica, 264; Huhschmann, KDMG, xlvi, 267; Arm.
Gramm., i, 318.228 FOREIGN VOCABULARY OF THE QUR'AN
, but as little does it refer to revelation, so even if we agree
that the borrowing was from Syr. we still have the problem of the
double, perhaps triple, meaning of the word in the Qur'an.
Sprenger thought we might explain this by assuming the influence
of the Ar. root 3^ on the borrowed word. 1 Schwally, however, has
suggested that this is not necessary, as the word might well have had
this double sense before Muhammad's time, under the influence of
Christian or Jewish Messianic thought, 2 and Lidzbarski, ZS, i, 91,
points out that in Gnostic circles " Erlosung und Heil besonders
durch Offenbarung vermittelt werden ". 3 There is the difficulty,
however, that there seems to be no evidence of the use of the word
in Arabic earlier than the Qur'an, and Bell, Origin, 118ff., rightly
insists that we must associate the use of the word for revelation with
Muhammad himself. He links up the use of the word in the Qur'an
with the story of Moses, and thinks that as in the story of Moses the
deliverance was associated with the giving of the Law, so Muhammad
conceived of his Furqan as associated with the revelation of the
Qur'an. Wensinck, El, ii, 120, would also attribute the use of the word
in the sense of revelation to Muhammad himself, but he thinks we have
two distinct words used in the Qur'an, one the Syr. lioioa meaning
salvation or deliverance, and the other a genuine Arabic word meaning
distinction, which Muhammad used for revelation as that which makes a
distinction between the true and the false. 4 Finally, Horovitz, A r t/,77,
w^ould make a sort of combination of all these theories, taking the
word as of Syriac origin, but influenced by the root L?^ and also
by the Heb. D^pIS (cf. also JPN, 216-18).
In any case it seems clear that jS^i is a word that Muhammad
himself borrowed to use as a technical term, and to whose meaning
1 Leben, ii, 339, " Wenn Mohammed Forkan auch aus dem AramiiiHohen entnom-
men hat, so schwehtc ihm doch die arabisohe Etymologie vor." See also Rudolph,
AbMngigkeit, 39; Bell, Origin, 118: Noldeke, tiketfhen, 38.
2 Nokleke-Schwally, i, 34 : " in erstcr Linie und am wahrscheinlichsten untcr
Christen, in zweiter Linie in mcRsianisch grrifhteten judischen Kreisen."
3 He refers, for examples, to Liechtenhan's Die Offenbarung im Gnosticismus,
p. 123 ff. ; hut as Rudolph, Abhangigkeit, 92, points out, this idea is not confined to
Gnostic circles.
4 Wensinck seems to have been unduly influenced by the theories of the native
Commentators.FOREIGN VOCABULARY OF THE QUR*AN 229
he gave his own interpretation. The source of the borrowing was
doubtless the vocabulary of the Aramaic-speaking Christians, whether
or not the word was also influenced by Judaism.
(Falaq).
```


## [2026-09-05T20:34:56.573Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT fšan ===\"; grep -n \"fšan\\|fšān\\|fšā̆n\\|aiwi.fšan\\|fšu-\\|fšūnav\\|fšnav\" BRT.txt | head -30",
 "description": "Grep Bartholomae for fšan"
}
```


### [2026-09-05T20:34:56.616Z] TOOL RESULT

```
=== BRT fšan ===
```


## [2026-09-05T20:34:58.116Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG ===\"; grep -n -i \"afšān\\|afšand\\|XŠAN\\|ŠAN\\b\\|fšan\" CHEUNG.txt | head -40",
 "description": "Grep Cheung for šan/afšāndan"
}
```


### [2026-09-05T20:34:58.165Z] TOOL RESULT

```
=== CHEUNG ===
29271:*AVESTAN: OAv. *хёат- (xšan-) ‘to be content with, resign oneself to = Liste: 17 
29292:*xšan ‘to harm, hurt, wound’ 
56911:*xad, *xšan, *zarH!
```


## [2026-09-05T20:35:03.343Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT variants ===\"; grep -n \"aiwi.fs\\|aiwi\\.fš\\|fsan\\|fsu-\\|fsav\\|fšu\" BRT.txt | head -20; echo \"=== BRT 'fs' near weiden ===\"; grep -n \"ausweiden\\|weiden aus\" BRT.txt | head",
 "description": "Grep Bartholomae variants"
}
```


### [2026-09-05T20:35:03.407Z] TOOL RESULT

```
=== BRT variants ===
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in  . . yantä  aiibyö  dair?  (sd)  voka  as  manö  Y.  \  geraten,  dadurch  könnte  er  Schaden  neh- 34-&]  9.  2&  10,  45-ii  — yaisqm  ..  mazdä  \iata"  V,/_j.37;  —  ahmat  haca  /«>nj  (sd) ..  vatghö  vai'ja  alsqm  ..  Yt.i6.%; — ^J  sayiJ/A' Nik.  7;  *2; — yesi  tat  paiti  irisjati syao^anä  yä  vacatihä  yä  yasnJ  .  .  ae^qm  '  aiähal  hala  iyae>n!i7ar3za  (sd.)  .  ,  V./_?. töi..}hmä  pourutimäil  äasl?(sd.}Y.j4-^,''  38-  2)  vorausweisend;  i)  adjektivisch ■ —  yöi  *aite  . .  *gä'kä  nSit  *srävayänti  . .  I  auf  direkte  Rede  oder  Zitat:  vahiütsm  . . assqm  fyaohamm\ia'\  .  .  N, 25;  —  ySt  ..'igänii  ..  vir^zyat  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag-  *pt3  asahyä  mazdlY.4y.2;~aya  antar?.- £qm  nöit  aita^qm  ratufris  ..  N.52;  ^j\  uxti  (sd.) :  nöit  nS  mana  (usw.,  Y..^5.z) —  yahmät  kakmäicit  nalmaruim  vätS  ä'^rö  Y.ig.i$.  —  a)  mit  ergänzendem  Relativ: baoiolm  vibaraiti  (sd.)  ahmll  kahmäiHt  aya  aibigara  (LS.  als  Instr.)  aya  aibijary- nalmanqm..\.8.&o.  a)  Die  Beziehung  ta{d.^.)  yä  amfsanqm  sp^ntanqm..:  gave ist  ungenau:  ^yJ  räakaytn  (sd.)  sravaahä  rto5j/(usw.,Y._j5.4)  Vr.J2.i.  a)  substan- vahistät  iyadkanäl  mantärü  aeibyö  mazäi  tivisch  und  adjektivisch  auf  eine  erläuternde akä  (sd)  mraot  "qua  alienant  doc-  oder  ergänzende  nominale  Beifügung:  «7.5- trina  . .,  üs  .  ."  (statt  qui  ..  iis  ,  .)  Y.32.  yacä  i^agtuL  yäsat  ahyi  Virßzin3m..ahyä .. 1 2'*^  Anhang  zu  II  I  1,  2.     a)  An   ahurahya  uruasimai^A.)  mazda  Y.j2.i ;  2S.
4679:tsin  aiare^  utä  'niyä  bagäA^  lyaty  At^tiy Bh.  4-  ■  2  >  13;  —  "^'"i  vahistsm . .  'iiya^qm yat  anifsanqm  spmtanqtn  YL_j,3;  —  yetii zT  MS  maiysia  .  .  yazayanta  yak:a  'nye yazaiinhe  . .  yazinti  ". .  wie  dae  andern y.  verehrt  werden"  YtÄii;  —  ahe  nars asaofiB  ..  äai  'nyazsqm  asaonqm  Yti.30; i3-  ^Ti  —  airime  gstüm  kl  nUhka^a  .. *par^itar?m  kala  'uyalibyd  mazdayas- f>aiibysY.(}.^y, —  'nye  aaksus /rals.iar^ %ra  Aog.65(?)'';  —  \'.ulä  pärsJ' uls  msdt^ utä  "niyS  dahySve^  Bh. /.  13,  14;  11;  — psrsaiy . .  msdaiy  utä  'niy^uvä  dakyusuvä Bh.  J.  10;  —  ahmäi  nmsnäi  daaäiti  gBu^ca vq^iwa  . .  upa  'nya  (APn.)  sHndayäti  Yt /o,  2  8 ;  —  vätB  , ,  AubaoioitarS  . .  'nyalifyö vstaeihyö  H.2.7;  25,  V.j.ss,  ^,29,  Vyt. 45i  —  ""^  a%ra  frakavB  mä  apakavB  . . maia.cim  'nyqm  (GPn.)  daxstanqm  V,  2. 29;  —  ahtnavaila  (sd.)  gäkanqm  .  . uilavaitTm  hsitlmca  , .  av5  yS  °nya  (näml. gä'^h)  srSvaydii  N.  46.  a)  Plur.  mit folg.  äi  'auch  die  andern' :   tl  mqm  ava%a
6302:•  j.  *asa'vaat-'*  Adj.  i)  'rechtschaffen' (nur  Ableit).  i)  'der  das  (höchste) Anrecht  a)  besitzt':  haurvafsavS  .  .  drvä Maurva  -vantö  (NP.)  Y.jÄiS.  b)  'ver- schafft':  hadiiasca  (sd.)   'vaiS  vOstravatS
6335:•  j.  a&afsania.-  m.  EN.  zweier  Gläu- biger; i)  'oahe  alasairyqs  asaonS  Yt.  13. 114.      x)  °%aAe  *zairyas  afa<mö\t.l3. IJ4.
10258:mafySnam  pard  fsanmat  {sA.)  :^atU  °W3m^  ".^j/.imi;  Utensils  med  in  the/äi' »j^*-^/(highet
11099:hochtonige  Wörter  dazwischen  stehen,  die nicht  zu  dem  mit  i'J  angeschlossenen  Skttt eil gehören.  Enklitika  trennen  nicht,  s.Y.jg.3 tSp.  569  o.),  41--  4  (Sp.  5Ö7  n.);  vgl.  Yt.  /.  i9(Sp. 573  u.).  —  3I  c'H  iwischen  iwei  verbundenen Duilen  verknüpft  nicht  diese  untereinander, sondernbeideiusunmeniUcinGlied  mit  einem oder  mehr  andern;  s.  Bthl.  BU.  /O.  268.  So  Y. 30.  II,  3/.  4,  Vr.  p.  5.  —  4>  Man  erwartete iu/rtumniafias^a  V  ffsaniühi.  —  J)  Man  ver- langte vircAuilniH  .  ,  vätäM  kyal .  .  earaii.  — <'1  5.  dazu  Cld.  KZ.  30.  545,  31.  157,  Proa. 43.  —  7>  oSäi  und  Uubyä^  gehören  als  Eweiles Glied  Eusammen,  s.  Sp.  5JÖ  m.  —  S>  Man  sollt« yat  haemim  gavafa  r"  .  .  erwarten.  —  9>  Für Stellen  wie  Y.  9.  18,  Yt.  fj.  1,  19.  67  nsw. ist  Bildung  von  Gruppen  anzunehmen,  deren Glieder  iT.  asynibetisch  aneinander  gereiht sind.  Im  Folgenden  werden  nur  diese  Gruppen berückiichiigt.  Doch  ist  begreiflicher  Weise die  Grenze  nicht  überall  mit  Sicherheit  lu bestimmen;  s.  i,  B.  Y.  5/.  7,  Sp,S7i  o.  (vgl. dagegen  Y.  44.  6),  Yt.  //.  14,  Sp.  570  m.  — ■o)  Nach  Ausweis  des  Metrums  Glosse.  — ■')  Man  tivanei  yaniyai^  xia^r^m.  —  '»)  Von denen  in  Strophe  1  d  :  yaifä  . .  die  Rede  ist. —  ij)  Normal  wäre  ainraiS  m'.  —  ■«)  Statt des  regelrechten  aSilra  aparäJim^m.  —  <i)  tä ist  enklitisch;  vgL  No,  2.
11746:tat  x^arynS (sd.)  bäla  asti:daAmS  Aurqm (sd.)  ^araiti  .  .  N.jo;  —  tatäi  isytiti apqm  napa  :  aSoi  afarpt^  Aangrrfsane  Yt ig.  51.  b)    adjektivisch,    nur     b)    im
12048:—  hin,  Über  —  hin,  über  —  hinweg';  a)  räum- lich: bis  Aapta  pfsavB  fraoirisysit  {sA.)  f ap3  nävaya  V.  i4'  16;  j5.  74;  —  UMayara uzXra  hvar)xlaita  .  .  t°  harqm  bimaitlfn V.  21.  $;  Yt  70.  118;  —  'ia  a/aunam urvänS   t°    harqm  .  .  *amaoiti  V.  ig.  30  j
14215:•  j.  'drva-,  p.  duruva-  Adj.  (fem.  °vä-) 'gesund,  heil':  bantsm^a  (sd.)  °rüm  itr»- naoiti  V.  22,  5;  —  haurvafsavS  drvö.- gal^a  .  .  'rt'S  (NPm.)   Aaurvä    Y.  5Ä  6;
14245:•  j.  drvö.vira-  Adj.  'der  gesunde  Männer, Leute  besitzt':  dadimahl  .  .  dmafsavB  'rä (NP.)  Y.5Ä6;  —  mag%anake{^)  paiU .  .  drvaßaos  'rahe  Y.  16.  10.
20036:—  D  6aga^  *vatarkt^  .  .  Aya^  'yam  ad^ hye^  siyätim  ada/'  'yakyä  D.  6.  i,  7. 1,  X. /.  I,  G.\,  Ao-i,  i'>;ll  —  kB . .  ä%rs  taßtm darayal  fanaot  haia  'yeke  V.  20. 1 ;  —  avi imqm  lanüm  yqm  'yänqm  V,  20, 3,  5;  — ya^  Als  antar»  vots  fravaiti  barV.ba^ (sd.)  'yänqm  Ytij.46;  —  'yänam  parS fsanmäi  "aus   Scham   vor  den  Leuten"
20120:•  masah-  n.  'Länge;  Grosse':  ar?dvlm sürqm..yiJ  asti  avavaiti  {sA,)  'sSyd^a.. Y.  65. 3.  a)  AS.  als  Adv.  'valde' :  za/ar? tafsan  (sd.)  aya  's3  V.^.3a.
20453:—  iai  hUx/tmf  -rB  sptntsY.ig.  19;  FrW. j).  I ;  —  hat  asti  'rahe  spmtahe  ama^ vastsmtm  ,  .  ?  .  .  ahmäksm  nqtna  .  .  yai amfsanqm  sp^ntanqm  tai  °rahe  spiniahe amavasttmim  YL  /.  1—3;  12.  i;  —  upa  vä 'nm  spmt^m  maraUa  V.4.4S;  —  upa- ratatitn  yqm  asahe  vahillahe  paitiparltJm- (sd,)Äi  °rahe  spmtahe  Yl/o.  33;  —  'rahe spmtahe  aiaonS  varszyanuhahe  dätahe  vi- dalvahe  dätahe  zara'huströis  dar»yayä  upa- yanayä  daEnayä  vaahuyä  mSzdayam5ÜY. /.13;  2.13,  77.5,  YL/AIS,  S.2.39;  —  dätäi hähaJätäi  vTdaevai  .  ,  haoa.ma'^rJi  ,  . upairi^atubyS  (sd.)  gtnptäi  °rai  spmiilt Extr.  /;  2,  3,  4;  —  zarazdättTm  'r-m  spm- t?m  . ,  uii.dan%r3m  daXnqm  mäzdayasnlm ..  vaäiim   'rmt   sp»fil>m  Y.25.  6;  22.  25*;
21383:vakma-i  fira  vS  rahi  ami^ä  ipmiS  'mmca vahtnfmÜl  Y. //.  18;  —  avi  apqtn&t urvaranqmca  asaonqmla  fravaHnqm  'rata g»r3hmahi  vahimm^a  Vt.si.i;  if.*;  — 'nsmca  vahmtmla  .  .  a/rlnami  ahurahe matdä  \.y2.6;  62.1,  P..J9,  F.^g: v^v3  aliqm  (n'äml.  des  ÄhM.  usv.)  'nfmia vahmtmca  Vr,  ir,  19;  — frä  *lg*siaomaide ,  .  ^vanküs  'nasla  *vahmqsca  N.  4^; yaita  . .  anuia  spmta  ,  .  paitisqn  vaahUs (AP.)  'nqsca  vahmqüa  vohü  (AD.)  'nsmci vahmftnca  Y.  60. 6 ;  — yal . .  sacyär>l  ääitTn 'n^mü  vahimmca  yaha  Al  asti  äaityd. timS'nasca  vahmascaYl.8.<,(i\  Y.ÖS.j;  — yä  *aiwinas>nU  vatahüS  'nqsca  vahmqsüa Y-  -J-  3;  —  vlspasla  apS  yaiamaide  . .  a 'näaiia  vahmäaica  yaia  ankam  asti (s.  eben)  Y.6Ä6f.(?);  —  aäa  'na  a vahma  ..  avajasa  YL5. 13a;  —  yat  ti aitihe  ava.urürao^a  yat  'naheia  vakma- kela  Y.i.  21,  o)  insbes.  DS.  in  infini- tivischem Sinn  (s.  Sp.  1270  u.):  mrHioi vacil  zara%ustra  ahmSktm  'näi^a  vakmäica yai  antfsanqm  spgntanqm  FrW. /.  2;  G./.  7 j.  7,  ^9,  5'.  6,  YL/o.iaz,  Vr.5.6,  Y.i^.i', ^y^47i  —  daevanqm  'nüUa  vahmäüa  V, i6.\\-, — staotaca'näica  vakmäica  frasasta- yal^a  yai  a^a  akurake  Vr.  (J.  6;  —  kävanse .  .  'ttäica  vakmäica  xsnadi^räH^tveiz.)^a frasastayatla  Y.  J.  23;  usw.  c)  in  Ver-
23961:•  j.  vi-Jajrniäta-  Adj.  'der  am  meisten sich  verbreitet  über  — ,  erstreckt  auf  — (Akk.)  sva.  der  am  meisten  einwirkt auf  — ':  ahmäkim  nqma  yat  amfsanqm  .  . tat  vispahe  anhSui  astvatö  *manS'''  asti 't)tn  "unser  Name  ist  es  . .,  was  am meisten  .  .  auf  das  Denken  einwirkt"  Yl /.  4;  a.
27595:~  haväi  kamaica  °säila  YL/j.  33;  — :^akmi  °ie  Vr.  J«/.  2 ;  —  larasia  aarahe mainy!ui ..  'Iq  YL/0.118;  — yai  %uiä didva^a..  yai  'sa  yai  aiaosa"..  ahsichüicii oder  unabsichtlich"  Y.  J,  ai,  2)  'Wohl- gefallen' :  /ai  värüi  (sd.)  radmfl  ahurakya •si  mazdi  Y.33.  2; —  'Äfi  ahurahe  matdä 'M  amfsanqm  spmtanqm  YtÄ  35;  — kihrpa  avavatqm  sraya  yaha  dthayatqm ■/i  "von  der  Körperschöne  solcher,   wie
29628:•  j-  (i  S)  haurva-,  p.  haniva-  Adj.  (fem. 'va-")  'ganz';  i)  sva.  'unverletzt,  unversehrt, heil';  dad)mahl  haurvafsavS  .  .  drva  *va (NPm.)  ttüvants  Y.  iß.  6.  2)  sva.  'ge- sammt,  vollständig':  \pasava''  kar<^  °va* /iami'äi''iya^  abava^  Bh.  i.  1 1 ;  1 6 ;  —  °v<^- iim  kära''  avaint/"  Bh.  2, 13,  14;  II  —  'vqm handaitlm  staotanqm  yesnyanqm  Y.  5^'.  8; —  vlsp>m  vacff  fravähm  (sd.)  °rum  vacS ahurahe  mazdä  \.  ig.  14;  —  'vqm  tarasca xlapamm  V.  ;&5,  6;  —  zusammen  mit vTspa-^^:  yO  vtspqm  'vqm  tansm  upanAan- zaiti  V,  6'.  24.  a)  Akk.  in  Verbindung mit  'da-  'etwas  ganz,  vollständig  machen,
29644:•  j.  haurva-ßav-  Adj.  'des  Haustiere unversehrt  sind';  pairX . .  dadrmahf  'fsavö (NP.)  Y.5Ä6.
=== BRT 'fs' near weiden ===
```


## [2026-09-05T20:35:04.184Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG sprinkle ===\"; grep -n -i \"to scatter\\|to sprinkle\\|to strew\" CHEUNG.txt | head -30",
 "description": "Grep Cheung for scatter/sprinkle"
}
```


### [2026-09-05T20:35:04.259Z] TOOL RESULT

```
=== CHEUNG sprinkle ===
2765:(caus.) ‘to scatter’ || (+ *ui-ati-) ? LKh. güjsabris- ‘to be dispersed’, LKh. güjsaba’j- 
3670:*NEIR: ? Yi. Cai-/Caid- ‘to sprinkle’, (Zarubin) ёӧу-/ёёу- ‘to sow, scatter’, ? Khf. 
4996:connect MMP ’y’rd-, BMP ’d’It- /ayard-/ to Skt. ага ‘to scatter’, which 15 
7886:Latv. bert ‘to strew’, cited in SGS: l.c. and DKS: 237a, is less convincing, since the 
9050:‘to sprinkle, pour out’ — Liste: 72 
9062:|| (+ *pati-) BMP psnc- /passinj-/ ‘to sprinkle’ || (+ *pari-) MMP prsynz- ‘to flow 
9085:pisanjidan ‘to sprinkle’, Khor. pšing ‘spraying, explosion’ 
12814:riZ-/rit ‘to scatter, spread’, Jow. bam-ri:t/a-ri:dz-, Meim. bem-ret/a-ri:dz-, Semn. 
13936:*KHOTANESE: OKh. уай- ‘to scatter’ || (+ *uz-) OKh. uysvän- ‘to throw up’ = SGS: 
15432:BMP plkn- /pargan-/ ‘to scatter, sow’ || (+ *fra-) BMP plkn- /fragan-/ ‘to throw, lay 
15442:*para-ä-) pr’gn- ‘to scatter, sow’ || (+ *pari-) prgn- ‘to scatter’ || (+ *ui-) wygn- ‘to 
15455:surround; to apply’, ? LKh. parkam- (parküfi-) ‘to sprinkle, scatter’ || (+ *ui-) OKh. 
16041:‘to scatter (manure)’, ? Oss. I. xelyn/xald, D. ixzlun/ixald ‘to be spoilt, ruined, 
16051:*SANSKRIT: kar ‘to strew, scatter’ (RV+) || саг ‘to move, roam, go’ (RV) > EWAia 
16057:causative of IE *kerH- ‘to scatter (seed), sow’ in Iranian. It is impossible to separate 
19522:sipen-, Rosh. sipön- ‘to strew, scatter, pour into, fill into (excess), place, Sariq. 
19623:*parš ‘to sprinkle, strew’ 
19630:*NWIR: NP pasidan/pas-, (LW) Bal. pasit/pas-, Gz. pas-/pasa, Siv. pas- ‘to sprinkle, 
19631:strew’, Gz. раёп-/раёпа (caus.) ‘to scatter, spread’, ? Гог. perxa ‘sprinkling’ 
19633:*NEIR: ? Sh. purx-/purxt, Rosh. parx- ‘to sprinkle, splash water’, Sariq. pirx-/pirxt ‘to 
19638:*MISC: Par. phis- ‘to strew, scatter, sow’, (?) Orm. prusnaw- ‘to sprinkle’ 
19644:*IE COGNATES: Hitt. /pappars-/ ‘to spray’, Toch. pärs- ‘to sprinkle’, OCS ras-praso 
23290:*MISC: Arm. (LW ?) srskel ‘to sprinkle’ 
23296:‘to sprinkle’, Latv. slacit ‘to make wet’, Russ. s/jakot’ ‘sleet’, Lith. släkas ‘drop’ 
23814:*pati-) LKh. pastar- ‘to strew? = SGS: 134, 94, 77 
24277:shake off’, Awrom. sanay/san- ‘to scatter, sow’, Gur. (Kand.) šän-á/-šān- ‘to throw, 
25817:*Өгаў$ ‘to scatter, spread, strew’ 
25819:*SOGDIAN: BSogd. 5^3, CSogd. š'š MSogd. 5° ‘to scatter, disperse’, (pass.) BSogd. 
26404:wblr(bI)V-/wblrovd-, wor(br)v-/worovd- ‘to sprinkle’, Wa. weir ‘rain’ 
27154:*SANSKRIT: vap! ‘to scatter, strew (out), spread (out)’ (RV+) > EWAia II: 503
```


## [2026-09-05T20:35:08.014Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24240,24330p' CHEUNG.txt",
 "description": "Read Cheung root entry around line 24277"
}
```


### [2026-09-05T20:35:08.062Z] TOOL RESULT

```
Pres.: CSogd. ëmm, OPT. 3р1. CSogd. Symynt 

9 The existence of this root in PIr. is uncertain: it is not even clear whether the forms 
above are cognate with each other at all. 

*REFERENCES: Gershevitch, Mithra: 233; Nyberg II: 77a; Sims-Williams 1985: 180 ad 111V; Gharib: 
373,379 


*San ‘to shake (down ?)’ 

*MIDDLE PERSIAN: (+ *apa-) BMP ’ps’n- (PZKWN-) /afsan-/ ‘to spread, scatter, 
sow’ 

Pres.: IND. 3sg. BMP /afsanéd/ 

*PARTHIAN: (+ *aua-) wy8’n- ‘to shake off, down’ = DMMPP: 359b 

Pres.: IND. 2sg. wys’nyh, 3р1. ws^nynd, *wys’nynd, IMPV. 2р1. ws’nyd; Partic.: perf. pass. П wys’n’d 
*KHOTANESE: OKh. safi- ‘to shake down’ = SGS: 127 

*SOGDIAN: BSogd. sn-, CSogd. Sn- ‘to shake, tremble, shiver’ || (+ *pati-) BSogd. 


pts’nkh ‘cross, scaffold (?) || (+ *fra-) CSogd. fsn- ‘to tremble, cower’ 


372 *taé 1 


Pres.: IMPV. 2sg. CSogd. "ën": Impf.: IND. 3sg. BSogd. sn’ || (+ *fra-) Pres.: IMPV. 25р. CSogd. fin’; 
Fut.: IND. 3sg. CSogd. fSntyq’ 


*CHORESMIAN: Sny- ‘to tremble’ = Samadi: 198 

*NWIR: Zaz. Sanayis/Sanen- ‘to shake, scatter’, Bal. Sant/sän- ‘to throw, throw up, 
shake off’, Awrom. sanay/san- ‘to scatter, sow’, Gur. (Kand.) šän-á/-šān- ‘to throw, 
strike, swing’, Maz. Sanne ‘he shakes’ || (+ *apa-) NP afsandan/afsan-, Gil. (Rsht.) 
fisan- ‘to disperse’ || (+ *aua-) Vafsi ho-wsin-/wasenä ‘to shake down’ || (+ *ati- ?) 
Tt. (Owr.) do-sän- ‘to shake down’ || (+ *fra-) Kurd. (Kurm.) rasandin “о spread’ 
*NEIR: Pash. San- ‘to ransack, search, stir’, Sanaw- (caus.) ‘to shake, jolt, stir’ || (+ 
*apa-) Sh. biyen/biyent, (Baj.) biwen-/biwent ‘to shake (fruit, nuts) down from a 
tree’ || (+ *aua-) Ishk. wulin- ‘to shake down’, M. wuson- ‘to churn’ || (+ *fra-) Y1. 
firsön-/firsoy ‘to shake trees’ (Zarubin) 

*MISC: Rom. (LW) usan- ‘to shake down’ 

*SANSKRIT: ? Pkt. chanana ‘sifting’, Khow. chonik ‘to shake down’, Hi. channä ‘to 
be strained’ 

9 An IE etymology for *san is lacking. The root may be related to Sean (which is a 
"substrate" borrowing). 


*PIE — > LIV: — | Pok.: 

*REFERENCES: EVP: 75; KPF II: 181; Christensen, Contributions I: 57; Bailey 1935: 777; IIFL II: 209a; 
MacKenzie 1966: 109; EVS: 19a; DKS: 408b f.; Asatrian — Livshits: 83; Paul 1998: 313b; NEVP: 79; 
Shahbakhsh: s.v. sant 


*tač! ‘to flow, run, walk’ 

*AVESTAN: YAv. tac- ‘to flow; walk’ || (+ *apa-) ‘to flow away’ || (+ *abi-) ‘to flow 
towards’ || (+ *pari-) ‘to run around, encircle’ || (+ *fra-) ‘to flow to’. Ф On the Av. 
desid. formation tixsonti see Hoffmann (apud Mayrhofer, Fs Morgenstierne: 142f.). 
c» Liste: 24 

Pres. {1} them.: IND. 35р. YAv. fratacaiti (Y 65.3 f., Yt 5.3 f., Yt 5.15, etc.), 3pl. YAv. fratacinti (Y 65.3, 
Yt 5.3, Yt 5.15, etc.), INJ. 3sg. YAv. tacat (Y 16.8), YAv. apatacat (Y 9.11, Yt 19.56), Y Av. pairi.tacat 
(Yt 17.26), 3pl. YAv. apatacin (V 5.12), Y Av. fratacin (Yt 13.78), SUBJ. 1sg. YAv. atacani (Yt 5.38), 
3pl. YAv. tacanti (Yt 8.5), OPT. 3sg. YAv. tacöit (V 8.100 ff.), IMPV. 2sg. YAv. taca (F 18); Pres. {2} 
athem.: IND. 2sg. med. YAv. taxse (Y 10.17), SUBJ. 3pl. YAv. apa.tacin (V 5.12); Partic.: pres. {1} 
Y Av. tacint- (Yt 6.2, Yt 10.20, V 6.26, etc.), YAv. (Gpl.) aiBi tacaintam (ViD 4), Y Av. atacint- (Yt 8.42), 
perf. YAv. -fratat.kus- (Yt 13.53); Caus.: pres. IND. 3pl. YAv. tacaiieinti (Yt 14.54), INJ. 3sg. ҮАУ. 
*fratacaiiat (У 2.34), IMPV. 2sg. Y Av. "fratacaiia (V 2.26); Desid.: pres. IND. 3pl. YAv. "tixsonti (Y 
9.22) 


*taé 1 373 


*MIDDLE PERSIAN: MMP tz-, BMP tc- /taz-/ ‘to run, flow’, BMP t’c- /taz-/ (caus.) ‘to 
pour; to ride [an horse]’, BMP tcyn- /tazén-/ (sec. caus.) ‘to cause to run, flow; to 
chase, pour’ || (+ *apa-) MMP ’bdx- (pret. stem) ‘to flee, escape’, MMP ’bd’c- 
(caus.) ‘to free, remove, rescue, liberate (from)? > DMMPP: 333a, 9 

Pres.: IND. 3sg. BMP tcyt /tazed/, SUBJ. 3р1. MMP “tz’nd, 3р1. BMP tcynd /tazénd/; Partic.: pres. MMP 
tz’n ‘running’, caus. BMP t’c’n /tazan/, perf. pass. BMP tcyt /tazid/, caus. BMP tcynyt /tazénid/; Caus.: 
pres. IND. 3pl. BMP t’cynd /tazénd/; Inf.: BMP tcytn /tazidan/, BMP thtn /taxtan/, caus. BMP t’htn
```


## [2026-09-05T20:35:29.206Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD afšān ===\"; grep -n -i \"afšān\\|afsan\\|pš'nd\\|afšandan\\|afšārdan\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"afšān\\|afsān\\|afsan\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg for afšān"
}
```


### [2026-09-05T20:35:29.268Z] TOOL RESULT

```
=== PHD afšān ===
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:3526:scatter afšāndan, pargandan.
PHD.txt:3753:sow afšāndan, kištan,
PHD_mackenzie.txt:880:   afsan [)ps'n' I (M "ps)ng). N afsana] story, fable.
PHD_mackenzie.txt:891:   afsandan. afsan- ['#'n-tn l I N -] spread, scatter. sow.
PHD_mackenzie.txt:6530:   speech dus-gowisn; of...... thought             fable afsan.
PHD_mackenzie.txt:7638: soul frawahr, fraward, griw, gyan,     spread afSandan, wistardan.
PHD_mackenzie.txt:7650: sow afsandan, kistan.                 stand awistadan, estiidan, padan; ,.."
PHD_mackenzie.txt:7685:story afsan.                               suffer widiir(i)dan; V. endure.
=== NYB ===
```


## [2026-09-05T20:35:31.122Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n \"afšand\\|afšān\\|efšān\\|efsan\" HUB.txt | head -20; echo \"=== ARY latin ===\"; grep -n -i \"AFSHANDAN\\|AFSAND\\|FESHAND\" incoming/ARY/ARY_latin_index_pages.txt | head",
 "description": "Grep Hübschmann and Aryanpur"
}
```


### [2026-09-05T20:35:31.179Z] TOOL RESULT

```
=== HUB ===
=== ARY latin ===
```


## [2026-09-05T20:35:38.596Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1492\" incoming/BQT/BQT_v3_pages.txt | head -5; echo \"--- search فشاندن\"; grep -n \"فشاندن\" incoming/BQT/BQT_v3_pages.txt | head -10",
 "description": "Locate BQT p.1492"
}
```


### [2026-09-05T20:35:38.662Z] TOOL RESULT

```
--- search فشاندن
16767:‏۴ - وبرافشاندن زر وسیم وگل ومانندآن :
28777:‏افشاندن دست شیر مردان ز دوکون اکنون بترانه و کول افدده است ,
34688:و سکون ‎SI‏ و نون » بمعنی تکانیدن وافشاندن
```


## [2026-09-05T20:35:40.642Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON افشاندن ===\"; grep -n \"افشاندن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10; echo \"=== MON فرقان ===\"; grep -n \"فرقان\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5",
 "description": "Grep Moin for افشاندن and فرقان"
}
```


### [2026-09-05T20:35:40.730Z] TOOL RESULT

```
=== MON افشاندن ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:3179:استین افشاندن: (مسص ل.) 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:3185:کسی افشاندن: با جنبش دست و آستین 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:13225:پرا کندن» پراکنده کردن» افشاندن. گل نم 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:15096:افشاندن: «02-:2627 [- افشانیدن - فشاندن 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:28257:برافشاندن. امر از «باشیدن». در کلمات 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:28311:افشاندن. ربختن» باچیدن (عم.) شنجیدن. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:29901:گفتار: تخلف از آن. پراگندن تخم: افشاندن 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:32183:افشاندن آب. آب مترشح: یک پشنگ آب. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:34270:توزیع کردن» افشاندن. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:41568:خوی کردن» خوی برافشاندن. یرون شدن 
=== MON فرقان ===
MON_part2.txt:62222:گزارندهٌ فرقان؛ ج. سفسرین. کسی که در 
MON_part2.txt:62702:۱ و ۷۲۱ سورة فرقان مستقرا و مقاماً (به
```


## [2026-09-05T20:35:46.202Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15085,15105p' incoming/MON/MON_2vol_Adena_v1_djvu.txt",
 "description": "Read Moin افشاندن entry"
}
```


### [2026-09-05T20:35:46.256Z] TOOL RESULT

```
اسرار. 
افشار: ۲ (- فشار] (.) فشار. (امف.) در 
ی امن ی ین 
(افشر ده) آمده» دست افشار؛» مشت افشار. 
(افا.) در برخی کلمات به معنی ممد و معاون 
آید: دردافشار. 
افشار: 208 (.) (مس.) گوشه‌ای است در 
دستگاه شور. 
افشان: 2520 [- فشان] (افا.) در بعضی 
کلمات مرکب به معنی افشاننده آید: 
آتش‌افشان. 
افشاندن: «02-:2627 [- افشانیدن - فشاندن 
- فشانیدن] (مص‌م.) (افشاند؛ افشاند» خو اهد 
افشاند» افشاننده» افشانده) ریختن و باشیدن» 
پرا کنده کردن. 
افشردن: 0-]2180 [- فشردن] (مسصمع.) 
(افشرد» افشرد» خواهد افشرد» سیفشر» 
افشر دنده؛ افشر ده) فشار دادن. آب؛ شیر ۵؛ با 
روغن چیزی را به فشار گرفتن؛ عصاره 
گرفتن؛ افشرده گرفتن. استوار کردن. 
افشره: (6-)2150۲-2 [< افشرج» مسعر.] (ا.)
```


## [2026-09-05T20:35:47.424Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | head -3; echo ...; grep -c \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt; echo \"--- lines around 34688\"; sed -n '34670,34700p' incoming/BQT/BQT_v3_pages.txt",
 "description": "Inspect BQT v3 page tags"
}
```


### [2026-09-05T20:35:47.492Z] TOOL RESULT

```
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
...
721
--- lines around 34688
سوراح ‎aS,‏ و باي کناهکاران و مجرمان و ‎S:‏ بز
‎ob‏ محکم کنند ‎٩‏ , وقلندر ممربآلست۷ .
کلندده ‎٩‏ - بفتح اول و ثانی و دابع
ورای قرشت وسکون ثالث» بمعنی کلندر اس ت که
چوب کند؛ ناتراشیده - و مردم ناهموار زدرشت

و خوشة آن پنج من تبریز میشود و هر داله ای
پنج درم -

کلنچك ۱ بطم اول وفتح ثانی‌وجیم
وسکون نون وکاف » ‎Kags‏ را کویندوعربان
سرطان خوانشد ؛ و بکر اول و انی هم آمده

است .

باشد , ‎ping‏ اول هم آمده است .

‎OT‏ > بنم اول و فتح تانی و دابع
و سکون ‎SI‏ و نون » بمعنی تکانیدن وافشاندن
‎JG‏ و دامن و امثال ‎OT‏ باشد .
۰ کلنده ‎Jol che‏ بروزن روئد»؛ لکلکه
راکویند وآن ‎Kye‏ باشد که یکس آنادول
آسیا و سر ‎YT Ss‏ در ‎LT Ke che‏
بعنوانی صب‌کنند که از کردش سنگه ‎OTT‏
‏چوبك ح رکت کند و ازدول کم کم ‎als‏ در ‎LT‏
‏رزد ‎٩‏

‏کلندی "۲ بفتح اول بروزن لوندی,
زمین مخت ودرشت راگویتد .

‏کلف » بنتح اول بروزن سمند » دست
```


## [2026-09-05T20:35:55.416Z] TOOL CALL #25: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1492 2>&1 | head -60",
 "description": "Fetch BQT page 1492"
}
```


### [2026-09-05T20:36:03.274Z] TOOL RESULT

```
REF: BQT:1492  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 285  OCR-lang: fas

خلی -۱۵۹-
ریس و ریزان - واامر بر فتافن باشد یمنی ۱ فان ۱ . +
بیان باز دهم
در حرف فا با طای حطی مشتمل برچهار لغت
فطر - نم اول و سکون نانی و رای | مطلق تخم راگوبند و بعربی بذر خوانند .
قرشت (۱)» نوعی از سماروغ باشد واین‌بدترین قطر اسالیون * - بلفت بونانی تنم
همه انواع است و بر و کرفی باشد چه فطرا بمعتی‌تشم وسالیون کرفی
پوست این زهر په 3 را کوبند و بسنی کوبند فطرا سالیون کرفی
قاتل باشد و اگر لّ کوعی است ۱ و بحنی کوبند نوعی از سماروغ
کیترخوردیهوش م6 است .
کرداند۲ - ویفتح چا اسر نسحم قطیر « بر وزن خمیر » ثانی را گوبند
اول»درعریی بمعنی فطن که خمیرآنر! همایه ازده باشندوبرنیامده‌ونرسیده
آفربدن و ایتدا کردن درکاری و مخترع چیزی | باشد - و خمیر برنيامده را نیز گفته‌اند - ودر
شدن - وشکافته شدن دندان‌شتر- وشکاف هرچیز عربی بمعنی تازه - وهرچیز که زود رسانیده‌شود
باشد » وکوبند بهمهٌ معانی عربی‌است ۴. - و بدو انگشت شیر دوشیدن را نیز گویبند .
قطر۱ ۴ - بروزن سحرا . بلفت بونانی | اوکونند بهمةٌ معانی عربی است۷ ,9
) چك : ورا ۰
۹ رك : فاندن . ۴ - فطر نام نوعی قارج‌است درعربی «عقار ۱۹۲ فی» رل :
تحةٌ حکیم موْمن وشرح قاموی. ۴ - ر4: شرح قاموی - ۴ - ازیوتانی 8۳61۳2
بمعنی صخره » سنکه ‏ کوه. «فرهنگه بونانی - انگلیسی لیدل وسکات» «اشتینگاس» ورل: بطرا.
8 - بم اول از بونانی ۳۵1۳۵۶611808 (11۷860]06 ۰ 920۷286 06۲811 (فر ) )
« دزی ج ۲ ص ۸ و رك : بطراسالیون - در کیاه شناسی کل کلاب در ذکر ره چتربان
5 آمده ( ص۲۳4 ): « جنفری ۳61۳0961681012 , دارای بر گهای‌پسیاربریده
که جنس خود روی آن درکتب قدیمی ما ( فطراسالیون ) نامیده شده .>
‎٩‏ - لغة بهمین هعنی است . ۲ - فطیر (عر) ناخواسته » و هرچه زودی‌وشتایی
کرده شود از وقت ادراكآن - بلا وسختی - نان بی‌خمیرمایه « منتعی‌الارب > .
فدافدن - بفتح وکسر اول وفتح پنجم <- افاندن ؛ پهلوی 810038180 ( رك .
اسشق هوبشمان ۱۶۲ ۰ اسقا ۲:۱ص ۳۹۶ ) ؛ پاشیدن » ربختن » تکاندن » پراکندن .
فعولیون - رد : لغات متفرقةٌ پایان کناب .
```


## [2026-09-05T20:36:31.398Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT traffic ===\"; grep -n \"^traffic\\|traffic,\" SKT.txt | head; echo \"=== FSD traffic ===\"; grep -n \"traffic\" FSD_vol4.txt | head -5; echo \"=== WEB traffic ===\"; grep -n \"trafficare\\|tra ficare\\|traffico\" WEB_vol1.txt | head -5",
 "description": "Grep Skeat/FSD/Webster for traffic"
}
```


### [2026-09-05T20:36:31.470Z] TOOL RESULT

```
=== SKT traffic ===
11430:traffic.  (F.  — L.)  F  nm mum'mm,  trade. --L.  com- i  mtrci-,  crude  lorm  of Uae  (above).
11432:^-L)  O  F  ntarket*, bbo  mmrkuf.  manhetx  (F. firav.  mertatfi,  Jtal.  mtrcate, V  wurtatus,  traffic,  also  a ft  G.  markt,  &c)  — L.  mtr' )tnari,  to  trade ;  see  mer-
=== FSD traffic ===
21834:engine  that  derives  its  motiv’e  force  from  the  action  of  being  steamy,  vaporous,  or  mlstj steam,  commonly  by  confinmg  it  and  utilizing  the  pres-  steam 'ship",  1   stlm'^p',  2   stem'ship',  n   A   large  ves- sure,  a   form  of  heat-engine  in  which  steam  is  the  work-  sci  propelled  bj  steam  and  designed  for  ocean  traffic: Ing  fluid  There  Is  no  record  of  the  use  of  steam-expansion  now  usually  a   screw  steamer  Compare  steamboat as  a   propulsive  power  up  to  the  17th  century  The  con-  steam 'way",  1   stim'we',  2   stem'wa',  n   A   channel  cast trivance  described  by  Hero  of  Alexandria  was  a   reaction  around  or  upon  a   cjhnder  of  an  engine,  for  the  admis-
25963:sub'way'%  1   sob'we',  2   sub'wa',  n   1.  An  artificial passage  under  or  below  the  lev’el  of  the  ground,  specif  , a   subterranean  passage  for  traffic,  or  an  accessible  con- dmt,  as  for  water*  and  gas-mains,  electnc  cables,  etc See  maNholx  2.  [U  S   1   An  electnc  railroad  beneath the  street  Compare  tube,  tuxxel sub-zo'nai.  o   \   Situated  Y)eneath  the  zona  pehucidaol  the ovum  2   Somewhat  zonary,  as  a   placenta  —   sub'zone'',  n A   subdivision  at  a   zone  — sub-zy"go-mat1c,  a   Situated beneath  the  zygomatic  process  of  the  temporal  hone Snc"ar-noo'chee  Creek,  1   suk'or-nQ'tihl,  2   sQc  ar-ndb'chs A   river  in  central  E   Mississippi  and  W   Alabama  length, loom  to  the  Tomblcbee  nv  er
32494:or  raceme  [F ,   <   LL  terminahs,  <   L   terminus boundary  ]   Svn„  see  final “   terminal  dementia,  a   form  of  dementia  following some  primary  or  preceding  mental  derangement,  as  acute mania,  etc  secondary  dementia  —   t   facilities  (Railroad). a   system  of  tracks,  with  other  conveniences,  for  making  up and  receiving  trains  and  handling  or  storing  baggage  or freight,  at  a   terminus,  also,  a   railway  system  connecting various  termini  for  the  easy  Interchange  of  traffic,  as  In  large cities  —   t   figure,  t.  god,  or  t   statue,  same  as  terminal, ^   *   2   —   t.  pedestal,  a   pedestal  that  tapers  toward  Its  base
34438:4.  A   place  through  wMch  much  business  traffic  passes
37921:It.  X   1.  To  engage  in  commerce  or  business  transac- tions of  bargain  and  sale ,   barter,  exchange ,   traffic ,   hence,
=== WEB traffic ===
```


## [2026-09-05T20:36:32.917Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB p162 (leaf?) ===\"; grep -n \"afsand\\|afSand\\|afšand\\|fšand\\|fsand\\|pasidan\" HUB.txt | head -10; echo \"=== HUB formfeeds ===\"; grep -c $'\\f' HUB.txt",
 "description": "Grep Hübschmann"
}
```


### [2026-09-05T20:36:34.566Z] TOOL RESULT

```
=== HUB p162 (leaf?) ===
6470:afsos *Spott' H. 101 (?), paz. aw(a)sd8; afsandan ausstreuen'
=== HUB formfeeds ===
291
```


## [2026-09-05T20:36:38.812Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6460,6485p' HUB.txt; echo \"=== leaf of line 6470 ===\"; awk 'NR<=6470{n+=gsub(/\\f/,\"&\")} END{print n}' HUB.txt",
 "description": "Read Hübschmann context"
}
```


### [2026-09-05T20:36:40.722Z] TOOL RESULT

```
vgl. Seligmann, Codex Vindobonensis p. XKY, Text p. 8, 6; 84, 5;
226, 5, 14, 18; 227, 6 u. s. w., Sal. Shuk. Gram. p. 17.— 183 —
raz), jiid. pers. awraStan, A. M. awraz H. 93; afroxtan =
avrOxtan, jiid. pers. awrdxtan anziinden*, A. M. warozi 2. pr.,
paz. aw(a)rdi' (zd. aiwi + rwd) H. 94; afzar, avzar *Werk-
zeug', A. M. awzar 'Organ H. 95, paz. aw(a)zar, oben p. 16;
afzUdaUy avzUdan *zunehmen'; A. M. wazili Vermehrend'
H. 96, paz. aw{a)ziidan, oben p. 16; afsar *Zuger H. 97;
afsCLn^ avsan *Wetzstein' H. 98; afsar Krone H. 99, oben
p. 17; afsurdan *frieren' H. 100, paz. aw(a)sard 'frozen*;
afsos *Spott' H. 101 (?), paz. aw(a)sd8; afsandan ausstreuen'
H. 102 (?) ; afgandan, avgandan Vegwerfen' A. M. awgandan
H. 103 (?); avzan 'todtend' (fiir awzan nach Sal. Shuk.
p. 17), paz. aw{a)zadan\ arm. ausard alte Frau — ap. *awi'
sarda- *bejahrt'. Also ware aus *awiS'karih (Horn Nr. 222)
nicht baskarl sondern *af§kari geworden!
§ 78. Resultat: ap. 6 im Anlaut und nach Nasal
ist b (Verschlusslaut) geblieben, ap. b ^= tv (Spirans) nach
Vokalen blieb im Mittelpersischen als Spirans w^) und
wurde im Np. 1) vor r zu fe, 2) vor Vokalen und im Aus-
laut zu t; , 3) in der Praep. aw = ap. awi- zu / (urspr.
vor tonlosen Konsonanten) oder v (urspr. vor t5nenden
Konsonanten) = tv bei Muwaffaq (vor z, r, g).
§ 79. Schwund des b (= w) ist eingetreten in : giram,
pr. von giriftan ergreifen*, das auf *grwyamiy (vgl. ap.
agrbayamj zd. geurvayaf) zuriickgehen wird, und in goyam,
=== leaf of line 6470 ===
193
```


## [2026-09-05T20:36:58.332Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T20:36:58.337Z] TOOL RESULT

```


```


## [2026-09-05T20:38:10.437Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%D8%A7%D9%86%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology section for افشاندن (afšāndan): Middle Persian form, Proto-Iranian reconstruction, prefix analysis, cognates, and any cited authorities (Cheung, MacKenzie, Hasandust)."
}
```


## [2026-09-05T20:38:12.008Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/traffic",
 "prompt": "Give the full etymology of 'traffic': Middle French trafique, Italian traffico, proposed origins (Arabic tafriq, Vulgar Latin *transfricare, Latin trans+facere), dates, and what the entry says about uncertainty."
}
```


### [2026-09-05T20:38:18.089Z] TOOL RESULT

```
# Persian Etymology of افشاندن (afšāndan)

## Middle Persian Origin
The word derives from Middle Persian ʾpšʾn-tn' (/afšāndan/), as documented in MacKenzie's *Concise Pahlavi Dictionary* (1971).

## Proto-Iranian Composition
The etymology breaks into two elements:
- **Prefix**: *Hápa* meaning "away"
- **Root**: *šan* meaning "to shake"

This combines to convey the sense of shaking or dispersing outward.

## Cognates Across Iranian Languages
The documented related forms include:
- **Old Khotanese**: ṣāñ ("to shake down")
- **Baluchi**: شانگ (šánag, "to vomit, throw, shake out")
- **Northern Luri**: شںنێ (şənı, "to throw")
- **Gilaki**: فشادن (fišādən, "to disperse")
- **Northern Kurdish**: reşandin ("to sprinkle, throw, vomit")

## Indo-Iranian Parallel
A broader Indo-Iranian connection appears with **Hindi** छनना (channā, "to be restrained"), suggesting deeper linguistic roots.

## Lexicographic Authority
The Dehkhoda Dictionary Institute's comprehensive Persian dictionary provides the primary modern reference for this term.
```


### [2026-09-05T20:38:18.236Z] TOOL RESULT

```
# Etymology of Traffic

**Direct lineage:** The word derives from Middle French *trafique* (15c.), which came from Italian *traffico* (early 14c.), itself from the verb *trafficare* meaning "carry on trade."

**Proposed origins:** The OED notes the etymology remains uncertain. Three main theories exist:

1. **Vulgar Latin source:** Possibly from *\*transfricare* ("to rub across"), combining Latin *trans* ("across") with *fricare* ("to rub"), with the original Italian sense being "touch repeatedly, handle."

2. **Latin alternative:** The second element might represent "an unexplained alteration of Latin *facere*" ("to make, do").

3. **Arabic source:** Klein suggests ultimate derivation from Arabic *tafriq* ("distribution").

**Uncertainty acknowledged:** The OED explicitly states the word "appears to have been the noun of action from the verb," but the precise origin remains unresolved. Modern scholarship continues to debate whether the root is European (Latin-based) or possibly borrowed from Arabic.

**Dating:** The commercial sense appears around 1500; the modern traffic/vehicles meaning emerged by 1825.
```


## [2026-09-05T20:38:36.133Z] TOOL CALL #32: WebSearch

```json
{
 "query": "Avestan \"aiwi\" fšan Yasht 14.56 Bartholomae afšāndan etymology \"aiβi\""
}
```


## [2026-09-05T20:38:37.355Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/%C5%A1an",
 "prompt": "What does this reconstruction page say about Proto-Iranian *šan 'to shake'? List descendants, any Avestan attestation, and cited sources."
}
```


### [2026-09-05T20:38:39.736Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:38:44.874Z] TOOL RESULT

```
Web search results for query: "Avestan "aiwi" fšan Yasht 14.56 Bartholomae afšāndan etymology "aiβi""

Links: [{"title":"Bahram Yasht","url":"https://en.wikipedia.org/wiki/Bahram_Yasht"},{"title":"Old Iranian Online - The Linguistics Research Center","url":"https://lrc.la.utexas.edu/eieol_master_gloss/aveol/16"},{"title":"Haft Amahraspand Yasht","url":"https://en.wikipedia.org/wiki/Haft_Amahraspand_Yasht"},{"title":"Avestan","url":"https://en.wikipedia.org/wiki/Avestan"},{"title":"AVESTAN LANGUAGE ii. The phonology of Avestan - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/avestan-language/avestan-language-ii-the-phonology-of-avestan/"},{"title":"YAŠTS - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/yashts/"},{"title":"Avesta - Wikipedia","url":"https://en.wikipedia.org/wiki/Avesta"},{"title":"Avesta/Yašt - Wikisource","url":"https://wikisource.org/wiki/Avesta/Ya%C5%A1t"},{"title":"Avestan, Introduction to (Martínez & de Vaan).pdf","url":"https://theswissbay.ch/pdf/Books/Linguistics/Mega%20linguistics%20pack/Indo-European/Iranian/Avestan,%20Introduction%20to%20(Mart%C3%ADnez%20&%20de%20Vaan).pdf"}]

The search results provide some relevant information about Avestan phonology and the prefix in question. Based on the results, here's what I found:

In Young Avestan, "aiβi" means 'to, towards', which appears as a variant alongside other forms. This is found alongside Old Avestan "aibī" and Sanskrit "abhí".

The search results also mention this in the context of phonological variation: the preposition "auui" is also written as "aoui, aoi," from *aβi, contrasting with "aiβi" in nominal compounds.

However, the specific query elements you asked about—the precise reference to Yasht 14.56, the "aiwi fšan" construction, Bartholomae's etymology, or the "afšāndan" verb—do not appear in these search results. To find more specialized information about these particular etymological and textual details, you would likely need access to more specialized linguistic and Avestan scholarly literature, such as Bartholomae's Altiranisches Wörterbuch or specialized Avestan linguistic studies that discuss this specific passage and its morphology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:38:54.365Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ausstreu\\|bestreu\\|streuen\" BRT.txt | head -20",
 "description": "Grep Bartholomae for streuen"
}
```


### [2026-09-05T20:38:54.412Z] TOOL RESULT

```
9192:i)  '(S^™c°)  ausschiitien,  ausstreuen  auf  acaraiti  Yt.^.46;  8.  2}  'wohin  (Akk.)
16897:mit  ^r  i)  'auseinandertragen,  'tun,  zer- streuen, zerteilen':  yal  \vä\  attim  ätnm usdanza  (sd.)  . ,  vica  barSit  .  .  V.  Ä  7  5 ; —  vX.barS  fravsxis  (sd.)  ratu/ris  nöit *avr.bars  N.gS;  gg;  —  ^paouru/ravJxsill (sd.)  .  .  *7/l.barasca  *avl.barasca  *rcUufrit\ N.p^ä'';  p5^'>.  s)    'aus-,    verbreiten':  |
28551:n  Kaus.  'ausemandergehen  lassen' ; :  ^uvaistam  'Hs'  axsatS  (sd.)  . .  D.  5. 3 ;  1  - 'zerstreuen':  yat . .  ätr^m^  utäanta  \  "^^zi/iya  dl  Ulis  mamyät  (sd.)  kasist»m urvarayä  . .  vTca  barsil  vUa  sävayStJ  ^^yj^^amaya"    DkB.  '131.  /aiÜ,  *s-atl
```


## [2026-09-05T20:38:54.993Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Yt.14.56\\|Yt. 14. 56\\|Yt.i4.56\\|14\\.56\" BRT.txt | head -10",
 "description": "Grep Bartholomae for Yt 14.56"
}
```


### [2026-09-05T20:38:55.042Z] TOOL RESULT

```
12457:•  j.  daeman-n.  1) 'Auge,  Augapfel';  mi^rd .  .  a%ra  naram  mi^rSJrujqm  .  .  *pairi 'ma  (AP.)  värayeiti  Yt  10. 4*8;  —  yat  .  . uB  pairtjäarayeifttH^ä)  °ma  (als  AD.)  . . pairi.urvaBayänti  Yt  14. 56.  a)  "Blick': irtra  datäiti  •mäna  (AP.?)'>  darätsüka dsi'iräiya  Yt  10. 107  (?).
```


## [2026-09-05T20:39:09.129Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"Yt[ .]*14\\.[ ]*56\" BRT.txt | head -20; echo \"--- count\"; grep -c \"14\\. 56\\|14\\.56\" BRT.txt",
 "description": "Find all Yt 14.56 citations in Bartholomae"
}
```


### [2026-09-05T20:39:09.188Z] TOOL RESULT

```
12457:Yt  14. 56
15840:Yt.14.  56
18589:Yt.  14. 56
--- count
3
```


## [2026-09-05T20:39:11.960Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15835,15845p' BRT.txt | cut -c1-1200; echo \"=====\" ; sed -n '18585,18593p' BRT.txt | cut -c1-1200",
 "description": "Read Bartholomae lemmas citing Yt 14.56"
}
```


### [2026-09-05T20:39:12.035Z] TOOL RESULT

```
Vgl.  'parSfay-.  —  ai.  pfsfhä-  n.,  np.  piät-, weitre  unsichere  Anknüpfungen   IF.  //.  285.
—  Pü.  (in  Yt.  /):  Hai pas  u  pii  Si  i  man  näm hac  piiit  palirai  barih,  Npü-fzuVl.  7^);  pSsux.
—  0  So  alle  guten  Hds.;  NA.  'ilm.
•  j.  "parStay-  f.  '(gegenseitige)  Befragung, Disputation':  yS  .  .  gaot)ma?ie  (sd.)  parSyä HSit  avaiti  \t13.16.  LS.  'ta  als  Int sbes.
KompE.  —  Zum  V./ras-.  —  S.  lüm.parsISii Inf,  a-nä  firailay:  —  afy.  \^.  puilrdql 'ita%fa' (wozu  IF.  9.  264>
•  j,  'parätay-  f..  Du."  'Rücken':  'ti (AD.)  he  .  .  assa  drux^  .  .  upaJvqsaiti S.S.  51;  52,  g.  18,  19.         [Yt.14.  56:  lies
Vgl.  'Par'sla:  —  ai.  ppfßy-  t,  'Rippe'?  — Pü.:  pult.  —  ')  Weil  aus  zwei  Haften  rechts und  links  des  Rückgrats  bestehend.
•  j.  parStS.va£ah-  Adj.  'der  die  (heiligen) Sprüche  erfragt,  durch  Fragen  erkundet hat':  ä^ravanö  'canhs paitiparstö.sravatfh8 Yt.5.91.
•  j.paräv-anika-  Adj.  'mit  ungleichfarbiger, gesprenkelter  Stirn-,  Vorderseite',  vom  Wild- schwein'*:  Au  kthrpa   varszahe  .  .  'iahe
IL  14- 15-
')    Vgl,    Br£HU   Tietleben:  'Am   Vorderteil
=====
Eig.  'da  und  dort  Sorge  tr^end';  "tastay-  f., .™  V.  rld-  (S  51  II),  ..  in  räl... j.  natalima  N,  86:  lies  tii  nUima.
•  j.,  g.namV,'sich(weg)beugen'.  Praes.3 tuma-,  3  °nma-,  4  näma-,  30  (Kaus.)  »3- maya-.  —  PPfP.  *'nala-;  Inf.  nsinSi.
parö  a^rlf  baoh^  dürSt  tumaiii  Vyt 5/(?).         S.  noch  Inf.
mit  apa  'entfliehen,  weichen  von  —  weg' (Abi.  mit  ha^ä):  paoirXm  i^annS  apani- mata  .  .  yimat  kaca  Yt  J^.  35.
mit^a  i)  'fliehen',  absolut:  /ränämailt . .  artrS  mainyul  Yt/p.gö.  a)  'fliehen vor  -'  (.pars  mit  Abi.,  Lok.):  hö  nöit taritS  *franämaite^^  .  ,  parS  dafvatibyö Y.57. 18;  — frä  akmat  parB  vlspe  daiva tarita  tumanle^.sy.i&,'^t.f).n{wQn3m/irite); — yä^a  assm  mit tarÜS  fra.nmäne .. pat daSvalibyS  Yt.5.4;  —  a?iu pars fränämaiU alsmö'VLit).')^.  3)  Kaus. 'niederbeugen, eindiiicken':  frS  *parst)m  nSmayänti  .  . ßättayänti  (sd.)  Yt.  14. 56.  Undeutlich ; yat  */ranata'^  bun  N.Ö5.
mit  VI  'sich  auseinander  tun,  -ziehen, -dehnen':  ärmaite  fraca  üia  vlla  mmataka
nay-  1043
harShre  pasvqmla  . .  "Arm.,  geh  vorwärts und  tu  dich  auseinander,  um  tragen  zu können  .  ."  V.  2. 10.  a)  Kaus.  'aus- einander treiben,  sprengen':  fravasayS  .  . yi  rasmanS  .  .  vf  ma&iyqmtn   namayeinti
Yty.39-
```


## [2026-09-05T20:39:26.354Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ttayänti\\|fSanay\\|fsanay\\|Sanayeinti\\|anayeinti\" BRT.txt | head -10; echo \"=== lemma search aiwi.f ===\"; grep -n \"aiwi\\.f\\|aißi\\.f\\|aiöi\\.f\\|ai\\bi\\.f\" BRT.txt | head -10",
 "description": "Find Bartholomae lemma for the Yt 14.56 verb"
}
```


### [2026-09-05T20:39:26.434Z] TOOL RESULT

```
18589:mit^a  i)  'fliehen',  absolut:  /ränämailt . .  artrS  mainyul  Yt/p.gö.  a)  'fliehen vor  -'  (.pars  mit  Abi.,  Lok.):  hö  nöit taritS  *franämaite^^  .  ,  parS  dafvatibyö Y.57. 18;  — frä  akmat  parB  vlspe  daiva tarita  tumanle^.sy.i&,'^t.f).n{wQn3m/irite); — yä^a  assm  mit tarÜS  fra.nmäne .. pat daSvalibyS  Yt.5.4;  —  a?iu pars fränämaiU alsmö'VLit).')^.  3)  Kaus. 'niederbeugen, eindiiicken':  frS  *parst)m  nSmayänti  .  . ßättayänti  (sd.)  Yt.  14. 56.  Undeutlich ; yat  */ranata'^  bun  N.Ö5.
=== lemma search aiwi.f ===
```


## [2026-09-05T20:39:38.742Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT tafriq/trafik ===\"; grep -n -i \"tafriq\\|tafrik\\|trafik\\|traffik\\|Verkehr\" LKT.txt | head -10; echo \"=== DEV/PHN trafic ===\"; grep -n -i \"trafic\" DEV.txt PHN.txt LAM.txt 2>/dev/null | head -10; echo \"=== AFA faraqa ===\"; grep -n -i \"faraqa\\|farraqa\\|p6raq\\|peraq\" AFA.txt | head -10",
 "description": "Grep Lokotsch, Devic, Pihan, Fraenkel"
}
```


### [2026-09-05T20:39:38.814Z] TOOL RESULT

```
=== LKT tafriq/trafik ===
373:a)  Vom  Vb.  amara  'befehlen',  also: 'Befehlshaber,  Fürst'.  In  der  vulg.  Form emlr  in  alle  europäischen  Sprachen  als Fremdwort  übergegangen,  bemerke  be- sonders ndl.  emier.  —  Mit  ar-rahl 'Transport',  d.  h.  die  Transportflotte,  die dem  Verkehr  u.  der  Verbindung  zwischen Andalusien  u.  Nordafrika  diente,  wurde amir  verbunden  zu  amlr  ar-rahl,  dem Titel  für  den  Befehlshaber  dieser  Flotte. Hieraus  ergeben  sich  aus  der  Verkür- zung der  Form:  pg.  amiralh,  prov. amiralhs,  atnirat,  afrz.  amiri,  nfrz. amiral  [u.  mit  falscher  etymologischer Beziehung  zu  lat.  admirari]  admiral, rum.  amiral,  it.  ammiraglio  [u.  wie  im
463:Im  Vulgärarabischen  des  Magrib  [Nord- westafrika] Interjektion  zum  Antreiben der  Tiere  [JAs  1843,  II,  216],  vielleicht
826:'Erbeuten,  rauben,  besiegen';  hieraus it.  bazza,  kat.  basa,  sp.  baza  'Stich  im Kartenspiel'.  [Ableitungen  vom  mhd. bazze  'Gewinn',  it.  bazza  'vorspringen- des Kinn'  oder  bazzicare  'verkehren' bei  ML  1011  mit  Begründung  zurück- gewiesen].   [ZfromPh  XXV,  747.
1669:'Westlich';  hieraus  il.garbino,  frz. garbin 'Südwestwind'  auf  dem  Mittelmeere, prov.  garbin,  sp.  garbino  'Süd-  oder Westwind',  sp.  pg.  algarve  'fruchtbar', pg.  garabia  'Westen'.  Aus  dem  It. wurde  serb.  garbin  'Südwind'.  Jeden- falls mit  Kontamination  von  al-  arabija 'die  arabische  Sprache'  entstand  pg.  al- garabia,  pg.  algravia,  frz.  charabia  'un- verständliches Zeug,  Kauderwelsch',  frz. insbesondere  'Dialekt  der  Auvergne'.  — Aus  demselben  Stamme  ar.  garaba 'untergehen  (Sonne)'  ist  mit  präfigiertem ma-  zur  Angabe  des  Ortes  magrib  ge- bildet; der  Magreb  ist  Nordwestafrika von  Tunis  bis  Marokko;  ms  al-magribl 'der  Bewohner  des  M.'  wurde  irz. maugrebin  'dass.'.  —  Auch  der  Name der  pg.  Provinz  Algarve  ist  ar.  garb 'Westen',  daher  sp.  algarabio,  algarabia, pg.  algaravio  'Bewohner  von  Algarve'. [DE  119.  241.  Eguilaz  178.  Devic  DEt 125.    ML  3683.    Bern  SlEtWb  295.
2458:'Wort',  ebenso  tk.  kelimet;  hieraus  rum. a  face  chelemet  'mit  jmd.  verkehren'.
3206:'Bastard'  [im  AT  zweimal:  Deut  23,  2]; hieraus  mgr.  luavZirip  als  geläufiges Schimpfwort  [so  wurde  JOHANNES DA  MASGENUS  von  CONST  ANTIN  VI. statt  mit  seinem  Ehrennamen  Mansür als  tAa\Zr\pöc,  bezeichnet],  durch  den Verkehr  mit  jüd.  Rabbinern  sp.  mancer 'Hurenkind'  [Dicc  Gast  1307  b:  'hijo  de la  mujer  publica']  und  poln.  (alt)  mam- zer,  mamzer  'Neugetaufler'.  Vgl.  GRÜN- BAUM in  ZDMG  XL,  264.
4158:Eine  Münze  in  Tungking  im  Werte eines  halben  Pfennigs  [also  etwa  dass. wie  ein  cash,  s.  hier  Nr.  1102],  eine flache  runde  Kupfermünze,  die,  mit einem  viereckigen  Loche  versehen,  auf Schnüren  gereiht  wird  und  die  einzige Verkehrsmünze  Chinas  bildet;  so  wird sie  schon  von  arabischen  Reisenden zur  Zeit  Karls  des  Großen  beschrieben. Frz.  sap&que,  dtsch.  Sapeke.  [Hirth ChinFW  199/^
=== DEV/PHN trafic ===
=== AFA faraqa ===
```


## [2026-09-05T20:39:44.627Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/traffico",
 "prompt": "Give the Italian etymology of traffico and trafficare — what origin does Wiktionary give (Arabic tafriq? Vulgar Latin *transfricare? Catalan/Occitan?), with any cited sources."
}
```


## [2026-09-05T20:39:45.969Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%82%D8%A7%D9%86",
 "prompt": "Give the Arabic etymology of فرقان (furqān) and any Persian section for فرقان: root f-r-q, the Syriac/Aramaic purqana theory, and cited sources."
}
```


### [2026-09-05T20:39:51.156Z] TOOL RESULT

```
# Etymology of "traffico" and "trafficare"

According to Wiktionary, **traffico** has two possible origins:

1. **Vulgar Latin origin**: "from _[*trānsfrīcō](/w/index.php?title=Reconstruction:Latin/transfrico&action=edit&redlink=1)_ ("to rub across"), from _trans-_ + _frico_"

2. **Arabic origin**: Klein proposes "ultimate origin in Arabic _تَفْرِيق_ (tafrīq, "distribution, dispersion"), reshaped to match the native prefix _tra-_ ("trans-")"

The article notes these are competing theories rather than a consensus, using the phrase "Potentially from" for the Vulgar Latin theory and "Klein instead suggests" for the Arabic alternative.

**trafficare** is identified as a related term derived from the noun **traffico**, but no separate etymology is provided—it follows from the noun's origins.

No sources are cited for either etymology in the visible content.
```


### [2026-09-05T20:39:54.274Z] TOOL RESULT

```
# Etymology of فرقان (furqān)

## Arabic Etymology

The word **فُرْقَان** (furqān) is "Borrowed from Classical Syriac ܦܘܪܩܢܐ (purqānā) or Hebrew פֻּרְקָן (purqān)."

It belongs to the **Semitic root ف ر ق** (f-r-q), which encompasses 15 related Arabic terms.

## Meanings

The entry notes that "the meaning of this term is uncertain" but lists several possibilities:

1. Verbal noun of فَرَقَ (faraqa) in Form I
2. Criterion or distinction
3. Evidence or proof
4. Redemption or salvation
5. The Qur'an itself

The Qur'anic usage appears in 25:1, where it refers to divine revelation.

## Sources Cited

The entry references scholarly works including:
- Arthur Jeffery's *The Foreign Vocabulary of the Qurʾān* (1938)
- Friedrich Schwally's "Lexikalische Studien" (1898)
- Georg Freytag's *Lexicon arabico-latinum* (1830–1837)

## Note on Persian Section

The page indicates this word appears in multiple languages (including Persian), but the detailed entry shown focuses on the Arabic form only.
```


## [2026-09-05T20:40:00.922Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%A7%D9%81%DB%8C%DA%A9",
 "prompt": "Give the Persian etymology of ترافیک (terāfik / trāfik): which language it was borrowed from (French trafic or English traffic) and the definition."
}
```


## [2026-09-05T20:40:02.253Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%82",
 "prompt": "Give the Arabic etymology and meaning of فرق (farq) and the Persian section for فرق (farq): is Persian farq a borrowing from Arabic? Quote the etymology lines."
}
```


### [2026-09-05T20:40:16.154Z] TOOL RESULT

```
# Persian Etymology of ترافیک

**Origin Language:** French

**Source Term:** According to the Wiktionary entry, the word was "Borrowed from French _trafic_."

**Definition:** The Persian noun ترافیک (terâfik) means "traffic (congestion)."

The word represents a loanword that entered Persian from the French language, rather than directly from English.
```


### [2026-09-05T20:40:20.282Z] TOOL RESULT

```
# Arabic Etymology and Meaning of فرق (farq)

**Arabic Etymology:** The word فرق belongs to the Semitic root ف ر ق (f r q).

**Primary Meaning:** As a noun, فَرْق (farq) means "difference" or "separation." The entry notes it is the verbal noun of فَرَقَ (faraqa, "to separate").

**Verb Forms:** The term has multiple verb forms including:
- فَرَقَ (faraqa) - "to split, separate, distinguish"
- فَرِقَ (fariqa) - "to fear, be afraid"
- فَرَّقَ (farraqa) - "to separate, distinguish, disperse"

---

# Persian Section: Is فرق (farq) Borrowed from Arabic?

**Yes, it is a borrowing.** The etymology section explicitly states:

> "Borrowed from Arabic فَرْق (farq)."

This confirms that Persian فرق derives from the Arabic source word, following a common pattern of lexical influence from Arabic into Persian.
```


## [2026-09-05T20:40:29.354Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 افشون ===\"; grep -n \"افشون\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -10; echo \"=== MON افشون ===\"; grep -n \"افشون\" incoming/MON/MON_2vol_Adena_v1_djvu.txt MON_part1.txt 2>/dev/null | head -10",
 "description": "Grep for افشون"
}
```


### [2026-09-05T20:40:29.431Z] TOOL RESULT

```
=== BQT v1 افشون ===
=== MON افشون ===
MON_part1.txt:15110:افشون: 2807 (- انشان] (ا.)افزاری است 
MON_part1.txt:51790:شو د؛ 0 غله بر افشان» افشون» هسته. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:15110:افشون: 2807 (- انشان] (ا.)افزاری است 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:51790:شو د؛ 0 غله بر افشان» افشون» هسته.
```


## [2026-09-05T20:40:32.108Z] TOOL CALL #45: Bash

```json
{
 "command": "ls site/pages/165.jpg 2>/dev/null; pdftoppm -f 165 -l 165 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg165 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 165"
}
```


### [2026-09-05T20:40:34.545Z] TOOL RESULT

```
site/pages/165.jpg
total 17164
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:40 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:40:39.547Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15106,15122p' MON_part1.txt",
 "description": "Read Moin افشون entry"
}
```


### [2026-09-05T20:40:39.601Z] TOOL RESULT

```
آبی که از نشردن مبوه‌ها گیرند» عصارة 
مایعی که به وسیلة فشار از مبوه‌ها استخراج 
افشک: 2626 [- انشک - افنشسنگ] (ا.) 
منم ژاله. 
افشون: 2807 (- انشان] (ا.)افزاری است 
دارای بنجه‌ای چوسن (سه شاخه با چهار 
شاخه) و دسته‌ای بلند که به وسبلةٌ آن غلهً 
کوفته را باد دهند و دانه را از کاه جدا سازند؛ 
انگشته» هسته. 
افشه: (50)0ه اقس. فروشک] (.) گندم 


نیم کوفته» بلغور» برغول. 

افسصاح: 20 [ع.] (مص‌ل.) زبان آور 
شدن» شیوا شدن. (امص.) زبان اوری» 
روشن گفتاری» شیوا سخنی.
```


## [2026-09-05T20:40:46.084Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg165.png"
}
```


### [2026-09-05T20:40:46.418Z] TOOL RESULT

```

```


## [2026-09-05T20:40:46.415Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:41:37.538Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%D8%A7%D9%86%D8%AF%D9%86\" \\\n \"https://www.etymonline.com/word/traffic\" \\\n \"https://en.wiktionary.org/wiki/traffico\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%82%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%82\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%A7%D9%81%DB%8C%DA%A9\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 165 verification (F.r.q/Tafriq; Fsan): etymology of afsandan, traffic/traffico/trafic/terafik, farq/forqan\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


## [2026-09-05T20:41:39.965Z] TOOL CALL #49: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg165.png data/verification/sources/refs/ocr/BOOK/165.png && ls -la data/verification/sources/refs/ocr/BOOK/165.png",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-05T20:41:41.020Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/62baaaaf5a498666.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/141941b17344cd4f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/41bd402fac1f15c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1f170f8dd96e890c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ce40b4311b7b9e43.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/844bea26dc6e0827.txt
```


### [2026-09-05T20:41:41.075Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 61265 Sep  5 16:41 data/verification/sources/refs/ocr/BOOK/165.png
```


## [2026-09-05T20:41:55.464Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== RCH farq ===\"; grep -n \"farq\\b\\|furqan\\|furqán\\|Furqán\" RCH.txt | head -8; echo \"=== MON ترافیک ===\"; grep -n \"ترافیک\" MON_part1.txt MON_part2.txt 2>/dev/null | head -3; echo \"=== FSD traffic headword ===\"; grep -n \"traf'fic\\|traf\\\"fic\\|traffic,\" FSD_vol4.txt | head -5",
 "description": "Grep Richardson, Moin, FSD"
}
```


### [2026-09-05T20:41:55.554Z] TOOL RESULT

```
=== RCH farq ===
=== MON ترافیک ===
=== FSD traffic headword ===
25963:sub'way'%  1   sob'we',  2   sub'wa',  n   1.  An  artificial passage  under  or  below  the  lev’el  of  the  ground,  specif  , a   subterranean  passage  for  traffic,  or  an  accessible  con- dmt,  as  for  water*  and  gas-mains,  electnc  cables,  etc See  maNholx  2.  [U  S   1   An  electnc  railroad  beneath the  street  Compare  tube,  tuxxel sub-zo'nai.  o   \   Situated  Y)eneath  the  zona  pehucidaol  the ovum  2   Somewhat  zonary,  as  a   placenta  —   sub'zone'',  n A   subdivision  at  a   zone  — sub-zy"go-mat1c,  a   Situated beneath  the  zygomatic  process  of  the  temporal  hone Snc"ar-noo'chee  Creek,  1   suk'or-nQ'tihl,  2   sQc  ar-ndb'chs A   river  in  central  E   Mississippi  and  W   Alabama  length, loom  to  the  Tomblcbee  nv  er
32494:or  raceme  [F ,   <   LL  terminahs,  <   L   terminus boundary  ]   Svn„  see  final “   terminal  dementia,  a   form  of  dementia  following some  primary  or  preceding  mental  derangement,  as  acute mania,  etc  secondary  dementia  —   t   facilities  (Railroad). a   system  of  tracks,  with  other  conveniences,  for  making  up and  receiving  trains  and  handling  or  storing  baggage  or freight,  at  a   terminus,  also,  a   railway  system  connecting various  termini  for  the  easy  Interchange  of  traffic,  as  In  large cities  —   t   figure,  t.  god,  or  t   statue,  same  as  terminal, ^   *   2   —   t.  pedestal,  a   pedestal  that  tapers  toward  Its  base
37930:ship  The  word  trade  Is  properly  applied  to  pursuits  which arc  distinguished  from  unskilled  labor  agricultural  employ- ments commerce,  the  learned  professions,  and  the  fine  arts 2   Buying  and  selling  for  gam  or  as  a   means  of  liveli- hood, mercantile  traffic,  commerce,  hence,  any  indi- vidual bargain,  as,  to  engage  m   foreign  trade •3.  [U  S   1   (1)  In  politics,  a   corrupt  bargain  m   patronage  or influence  between  partv  leaders  a   deal  (2}  An  exchange or  barter,  as,  a   tradt  of  implements  4   The  body
37939:traf'flc,  1   traf'ik  2   traf'ic,  v   [tbaf'ficked,  trap'ficts, traf'fick-ing  )   I.  <   i   To  make  the  subject  of  com- mercial  exchange,  as  goods  or  wares,  barter  To
37943:traf'fic,  n   1.  The  exchange  of  goods,  wares,  or  any  kind of  merchandise  between  individuals,  commumties,  or countries,  whether  such  exchange  be  direct  (barter)  or by  the  use  of  money,  bills  of  exchange,  etc  ,   trade 2   The  business  of  transportation,  as  of  persons,  ani- mals, or  goods,  as,  railroad  or  canal  traffic  3.  The subjects  of  transportation  collectively,  the  persons, animals,  or  goods  earned  4   [Rare  ]   hlarketable  goods collectively,  as  the  subject  of  trade  5   [Scot  or Archaic)  A   business  procedure,  transaction,  hence,  deal- ings or  intercourse  6   [Prov  Eng]  A   track  or  path, trail  [   <   F   trafic,  traffic,  said  to  bo  <   L   trans  across, +   vicjs,  change )
```


## [2026-09-05T20:41:57.229Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY افشاندن ===\"; grep -n \"افشاندن\\|افشان\" incoming/ARY/ARY_pages.txt | head -8; echo \"=== FFD ===\"; grep -n \"افشاندن\\|فشاندن\" incoming/FFD/FFD_pages.txt | head -8",
 "description": "Grep Aryanpur and Abolghasemi"
}
```


### [2026-09-05T20:41:57.306Z] TOOL RESULT

```
=== ARY افشاندن ===
=== FFD ===
836:افشاندن
1097:معنی به کار رفته‌اند: ۱-«غربال کردن»» ۲-«افشاندن»» «ریختن». در شاهنامه آمده است:
```


## [2026-09-05T20:42:02.745Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '820,860p' incoming/FFD/FFD_pages.txt",
 "description": "Read Abolghasemi entry for افشاندن"
}
```


### [2026-09-05T20:42:02.804Z] TOOL RESULT

```
فعلهای فارسی دری
افروز < فارسی میانه 20702 « ایرانی باستان ۵01-72008*. 6 در 12062 به جای ۲ آمده
است.
۱ افزودن
افزود < فارسی میانه 20200 + ایرانی باستان 20-1۵[-۵01*. برای 201 > افراشت و
برای ۵ > آراست. 0[ صورت دیگرش 108 است به معنی «افزودن» است.
افزای + فارسی میانه 20237 < ایرانی باستان -3۷-878[-۵01*. 3[ صورت بالاندةٌ 21[
است و 278 نشانه‌ای که برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است.
افسردن
افسرد < فارسی میاته ۵08370 < ایرانی باستان 202-637-1۵*. برای 1۵ -> آراست. 208
پیشوند فعلی است. ۶3۲ صورت بالاندةٌ ريشةهٌ ۶۵۲ است. ۶۵۳ و 20837422 به معنی
«اسردشدن) هستند.
اقفسر + فارسی میانه 20937 < ایرانی باستان 202-837-2*. برای 2 -> آرای.
افشردن
افشرد < فارسی میانه 21870 215370.
افشار < فارسی میانه ۸1837.
افشاندن
افشاند < فارسی میانه 15300. ۱
افشان < فارسی میانه 21538
افگندن
افگند < فارسی میانه 208284 « ایرانی باستان 202-127-1*. برای 1۵ + آراست.
[pdf page 36]
ماد»‌های ماضی و مضارع قارسی دری سس ۲۱
4 پیشوند فعلی است. ريشهٌ 128 به معنی «نهادن» و «افگندن» است. از 127 در فارسی
دری «آگندن» و «پراگندن» هم آمده‌اند > آگندن و پراگندن. در ایرانی باستان 8۵8
دیگری هم بوده است که از آن «کندن» آمده است > کندن.

افگن < فارسی میانه 20827 < ایرانی باستان ۳۵08-۵-۵. برای ۵ -> آرای.

انباردن.» انباشتن

انبارد < فارسی میانه ۳۵۳0276* < ایرانی باستان 82-037-12*. برای 2 > آراست.
0 پیشوند فعلی است. 037 صورت بالاندةٌ ریشهٌ 07 است» به معنی «پرکردن». از 087
«اوباردن» هم آمده است > اوباردن. «انباشت» در فارسی دری به قیاس با «کار»
«کاشت)» به وجود آمده است.

انبار + فارسی میانه 127003 < ایرانی باستان 1۵:۳-037-2*. برای 2 -> آرای.

انجامیدن

«انجامید» مادةٌ ماضی جعلی است» از مادهٌ مضارع ساخته شده است. مادةٌ ماضی
```


## [2026-09-05T20:42:13.809Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^فرق\\|فرق: \\|فرقان: \\|فُرقان\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10",
 "description": "Find Moin headword for فرق"
}
```


### [2026-09-05T20:42:13.876Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4018:فرق سعیه را نام پرند مانند عبدالله ببن 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:6421:فرق: 2۷ [ع.] (مص‌م.) جدا کردن. تمیز 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:6423:فرق: 0 [ع.] (.) تار سر که راهی است 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:6433:فرق‌افشان: مق [ع. ف.] (امر.) نثاری 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:6482:فرق‌افشان 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:7238:فرق. فروق. (غم.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:12279:فرقاول: ۲۷۵۷ (.) (جاد.) پرنده‌ای است 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:21043:فرق «کجا, و «کو». تا کجاها: تا چه اندازه 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:35409:فرقی نمی‌کند یعنی هم می‌توان بذر آن را 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:46639:متفرق: 1۳۵ 1۱10012]2 [ع« (افا.) براکنده
```


## [2026-09-05T20:42:16.596Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6418,6440p' incoming/MON/MON_2vol_Adena_v2_djvu.txt; echo \"=== فرقان ===\"; grep -n \"فرقان\" incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -5",
 "description": "Read Moin فرق entry"
}
```


### [2026-09-05T20:42:16.680Z] TOOL RESULT

```
فرفور: ۲ (ع.] (ا.) شتر فر به. 
فرفوری: ->000] (.) (ص‌نسب.) چینی 
(ظروف). ظروف چینی ژاپن (خصوصا). 
فرق: 2۷ [ع.] (مص‌م.) جدا کردن. تمیز 
دادن» امتیاز نهادن. (امص.) جدابی. امتباز» 
فرق: 0 [ع.] (.) تار سر که راهی است 
میان موی سر؛ چکاد» چکاده. فرق سر: سر 


۷۰ ۱ 
کله. بالای هر چیز. فرق است میان... و (با) 
... اختلاف سار است مبان... و... فرق باز 
کرفان (عم.) از وسط سر موی رابه دو 

جهت مخالف بردن و شانه کشیدن. 
فرق‌افشان: مق [ع. ف.] (امر.) نثاری 
که بر سر عروس و داماد ریزند؛ نثارسر 


شاباش. 

فر قان: 0۳۳3 [ع.] (رص.) آنجه جدا کننده 
حق از باطل باشد. 
=== فرقان ===
62222:گزارندهٌ فرقان؛ ج. سفسرین. کسی که در 
62702:۱ و ۷۲۱ سورة فرقان مستقرا و مقاماً (به
```


## [2026-09-05T20:43:37.166Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:47:48.458Z] TOOL CALL #55: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-165.json << 'JSONEOF'\n{\n  \"pdf_page\": 165,\n  \"book_page\": 135,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"F.r.q, Tafrîq\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic root ف ر ق (f-r-q) 'to split, separate, divide'; فَرْق farq 'separation, difference'; تَفْرِيق tafrīq 'distribution, dispersal', verbal noun of Form II فَرَّقَ farraqa\",\n      \"note\": \"Both the language label and the two glosses are right. faraqa 'he split, divided' is a well-attested Common Semitic root (Heb. pāraq 'he tore away', Aram./Syr. pəraq 'he rescued, withdrew', Eth. faraqa 'he set free'), and tafrīq is the regular taf'īl verbal noun of the Form II intensive farraqa, so 'distribution, dispersing' is exactly its sense. Nourai's own source (Klein p. 1637) states this chain verbatim. The only substantive problem on this chart is not in the root box but in the two arrows leaving it (see nodes #1 and #2).\",\n      \"note_fa\": \"ریشهٔ سه‌حرفی عربی «ف ر ق» به معنی «جدا کردن، شکافتن» ریشه‌ای است سامی مشترک (عبری pāraq، آرامی/سریانی pəraq، حبشی faraqa) و «تفریق» مصدر باب تفعیل از «فرَّق» است، پس معنی «پخش‌کردن، پراکندن» درست ثبت شده. کلاین (ص ۱۶۳۷) — همان مأخذی که نورایی به آن ارجاع داده — دقیقاً همین را می‌گوید. ادعای نورایی دربارهٔ خودِ ریشه درست است؛ اشکال‌ها در دو پیکانی است که از این ریشه بیرون می‌رود (گره‌های ۱ و ۲).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%82\",\n        \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%82%D8%A7%D9%86\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:1637\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 868 (the leaf is page-stamped '1636 / 1637'), s.v. traffic: 'Arab. tafrtq [tafrīq], \\\"distribution\\\", verbal noun of farraqa, \\\"he distributed\\\", II (= frequentative or intensive conjugation) of faraqa, \\\"he split, divided\\\" ... Arab. faraqa is rel. to Heb. pāraq ... Aram. pəraq ... Ethiop. faraqa'. Exactly the root box as drawn.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"FVQ\", \"where\": \"pp. 225-229 s.v. Furqān (FVQ_pages.txt lines 8142-8250)\", \"stance\": \"partial\", \"note\": \"Jeffery: 'The form of the word would suggest that it was genuine Arabic, a form fuʿlān from f-r-q, and thus it is taken by the Muslim authorities' — but he concludes for a borrowing. Confirms the reality and sense of the root while disputing that furqān is one of its native formations.\"},\n        {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi (Adena 2-vol., v.2) s.v. فرق / فرقان\", \"stance\": \"supports\", \"note\": \"«فرق: [ع.] (مص‌م.) جدا کردن، تمیز دادن، امتیاز نهادن» and «فرقان: [ع.] (وص.) آنچه جداکنندهٔ حق از باطل باشد» — both marked [ع.] = Arabic.\"},\n        {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter (AFA.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'faraqa|farraqa|peraq' returns nothing; Fraenkel treats Aramaic words borrowed INTO Arabic and does not discuss the native root f-r-q.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"farq; forqân\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both words are Arabic loans in Persian, taken over with the Arabic lexical stratum from the 8th-9th c. onward; Persian did not inherit them. فرق farq is the Form I verbal noun of فَرَقَ faraqa 'to split', hence 'separation, difference' and concretely 'the parting of the hair, crown of the head' (Mo'in gives both senses) — Nourai's gloss 'difference, dividing line' is exact, and Wiktionary's Persian section says plainly 'Borrowed from Arabic فَرْق (farq)'. The chart's extra list is likewise a set of regular f-r-q formations borrowed into Persian: فارق (act. part.), فاروق (faʿūl intensive, the epithet of the caliph ʿUmar 'he who distinguishes truth from falsehood'), تفریق and تفرقه (Form II verbal nouns), فراق (Form I 'separation'), مفارقت (Form III), متفرّق / متفرّقه (Form V participles), فرقه (fiʿla 'sect, group'). فرقان forqân is the point of doubt: deriving it directly from f-r-q as a fuʿlān noun is the traditional Muslim analysis (Ṭabarī on Q 2:50; Mo'in's gloss «آنچه جداکنندهٔ حق از باطل باشد» reproduces it), but modern Qurʾānic scholarship since Geiger and Fraenkel — set out at length by Jeffery (FVQ 225-229) and followed by Wiktionary — takes Arabic furqān as a loan from Classical Syriac ܦܘܪܩܢܐ purqānā 'salvation, deliverance' (or Jewish Aramaic/Hebrew purqān), later drawn into the native root f-r-q by folk association, which explains why the Qurʾānic senses ('scripture', 'criterion', 'the day of Badr') do not cohere. Nourai's arrow (Arabic → Persian) is unimpeachable; his implied morphology of forqân from f-r-q is what modern scholarship contests.\",\n          \"derivation_fa\": \"هر دو واژه معرَّب نیستند بلکه وام‌واژه‌های عربی در فارسی‌اند که از سدهٔ دوم و سوم هجری همراه لایهٔ واژگانی عربی وارد فارسی شده‌اند. «فرق» مصدر/اسم‌مصدر باب اول از «فَرَقَ» است به معنی «جدایی، تفاوت» و نیز «شکاف میان موی سر» (معین هر دو معنی را آورده)؛ ویکی‌واژه هم می‌گوید فارسیِ «فرق» وام‌گرفته از عربیِ فَرْق است. واژه‌های فهرست‌شده (فارق، فاروق، تفریق، تفرقه، فراق، مفارقت، متفرّق، متفرّقه، فرقه) همگی ساخت‌های قاعده‌مند همین ریشه‌اند. اما دربارهٔ «فرقان»: تحلیل سنتی آن را بر وزن فُعلان از ف‌ر‌ق می‌داند (و معین هم همین را می‌آورد)، ولی قرآن‌پژوهی امروزی (گایگر، فرنکل، جفری «واژگان دخیل در قرآن» ص ۲۲۵–۲۲۹، بِل، هوروویتس و ویکی‌واژه) آن را وام‌واژه‌ای از سریانیِ purqānā «رهایی، نجات» می‌شمارد که سپس به ریشهٔ عربی ف‌ر‌ق منسوب شده است. پس پیکانِ نورایی (عربی ← فارسی) درست است و تنها تحلیل درون‌عربیِ «فرقان» با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%82\",\n            \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%82%D8%A7%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:313\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989): refs_online.json records 'no digital copy found' on archive.org, ketabnak, noorlib or the open web; catalogue record only (OpenLibrary OL2012991M). Could not be consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Adena 2-vol. v.2, s.v. فرق and فرقان\", \"stance\": \"supports\", \"note\": \"«فرق: 2۷ [ع.] (مص‌م.) جدا کردن. تمیز دادن، امتیاز نهادن. (امص.) جدایی، امتیاز» ; «فرقان: [ع.] (وص.) آنچه جداکنندهٔ حق از باطل باشد» — Mo'in marks both as Arabic and glosses forqân exactly as Nourai does.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 225-229 s.v. Furqān\", \"stance\": \"contradicts\", \"note\": \"'Linguistically there is a closer equivalence in the Aram. pūrqān \\\"deliverance or redemption\\\" ... Fraenkel ... suggested the possibility of a derivation from Syr. purqānā, a suggestion which has been very fruitfully explored by later scholars ... In any case it seems clear that furqān is a word that Muhammad himself borrowed'. Contradicts a straightforward f-r-q derivation of forqân.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 p. 1637 s.v. traffic\", \"stance\": \"supports\", \"note\": \"gives the Arabic root and its Form II verbal noun tafrīq, i.e. the morphological family from which farq and the chart's extra list are formed.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Italian\",\n          \"words\": \"traffico; traficare\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Italian traffico 'trade' and trafficare 'to trade' appear in Tuscan merchant prose from the early 14th c. Nourai reproduces (and flags in his own NOTE) Klein's account: traffico 'prob. derives fr. Arab. tafrīq \\\"distribution\\\"', the word reaching Italy along the Pisan/Genoese/Venetian trade with the Arab Levant and the Maghrib and being reshaped after the native prefix tra- (< Latin trans-) under the influence of an assumed Latin traficere (for *transficere) 'to make over'. That is one live hypothesis, not the received view: the OED (via Etymonline) calls the origin unresolved and puts the Arabic proposal beside a Vulgar Latin *transfricare 'to rub across' (trans- + fricāre, original sense 'to touch repeatedly, handle'), and Wiktionary lists the Vulgar Latin etymon first with 'Klein instead suggests' the Arabic one. Funk & Wagnalls (FSD s.v. traffic) offers a third guess, '< L trans across + vicis change'. Telling against the loan is that Lokotsch's Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927) — the standard register of European Arabisms — has no entry for traffico/trafic at all, nor do Devic or Pihan for French. Two textual points: the book prints the Italian verb as 'traficare' where standard Italian is trafficare (a single-f spelling that does occur in older Italian but is not the modern form), and Nourai's NOTE renders Klein's gloss of traficere 'to make over' as 'to take over'.\",\n          \"derivation_fa\": \"واژهٔ ایتالیایی traffico «داد و ستد» و فعل trafficare از آغاز سدهٔ چهاردهم میلادی در نثر بازرگانی توسکانی دیده می‌شود. نورایی همان نظر کلاین را نقل می‌کند (و خود هم در یادداشت به «احتمالاً» بودنش اشاره دارد): وام‌گیری از عربیِ «تفریق» از راه بازرگانی پیزا و جنووا و ونیز با شام و مغرب، با تأثیرِ لاتینیِ فرضیِ traficere که آغاز واژه را به پیشوند بومی tra- (از trans-) مانند کرده است. اما این تنها یکی از فرضیه‌هاست: فرهنگ آکسفورد ریشه را نامعلوم می‌داند و در کنار آن لاتینی عامیانهٔ ‎*transfricare‎ «سودن، مالیدن» را می‌گذارد؛ ویکی‌واژه نیز همان را نخست می‌آورد. نکتهٔ مهم آنکه لوکوچ در فرهنگ واژه‌های اروپاییِ خاورتبار (۱۹۲۷) اصلاً مدخلی برای این واژه ندارد. پس ادعای نورایی با احتیاط پذیرفتنی است. ضمناً کتاب صورت «traficare» را چاپ کرده که املای امروزی ایتالیایی trafficare است، و در یادداشت، معنی traficere را «to take over» نوشته حال آنکه کلاین «to make over» دارد.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/traffic\",\n            \"https://en.wiktionary.org/wiki/traffico\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1637\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 868 (page-stamped 1636/1637), s.v. traffic: 'MF. trafique (F. trafic), fr. It. traffico, which prob. derives fr. Arab. tafrīq, \\\"distribution\\\" ... influenced in form by assumed L. traficere (for *transficere), \\\"to make over\\\"'. The page says what Nourai's NOTE says; note that Klein's own hedge is 'prob.', and that his gloss is 'to make over', not 'to take over'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"Lokotsch 1927, whole dictionary (LKT.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'tafriq|tafrik|trafik|traffik' finds no entry; the standard inventory of European words of Oriental origin does not include traffico, which is evidence that Lokotsch did not accept the Arabic etymology.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, vol. 4 s.v. traf'fic, n.\", \"stance\": \"contradicts\", \"note\": \"'[ < F trafic, traffic, said to be < L trans across, + vicis change ]' — same Romance route, but a Latin, not Arabic, ultimate source.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale (DEV.txt); also PHN, LAM\", \"stance\": \"silent\", \"note\": \"grep -i 'trafic' returns nothing in Devic, Pihan or Lammens — the three French dictionaries of Arabisms give no entry for trafic.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"French\",\n          \"words\": \"trafic\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Italian noun was taken into French in the 15th c. as trafique (also traffique), which is the form Klein and the OED cite; modern French spells it trafic. The route Italy → France is uncontested in every source consulted, whatever the ultimate origin of the Italian word; it belongs to the large 15th-16th c. layer of Italian commercial vocabulary in French (banque, bilan, escompte, trafic). Etymonline: 'Middle French trafique (15c.), from Italian traffico (early 14c.), from trafficare \\\"carry on trade\\\"'.\",\n          \"derivation_fa\": \"اسم ایتالیایی در سدهٔ پانزدهم میلادی به فرانسه راه یافت به صورت trafique (املای امروزی: trafic). این حلقه — از ایتالیایی به فرانسوی — در همهٔ منابع پذیرفته است و بخشی از لایهٔ بزرگ واژگان بازرگانی ایتالیایی در فرانسهٔ سده‌های پانزدهم و شانزدهم است (مانند banque و bilan). ادعای نورایی در این گره درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/traffic\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1637\", \"status\": \"supports\", \"note\": \"KLN_1966 p. 1637 s.v. traffic: 'MF. trafique (F. trafic), fr. It. traffico' — the Italian → French arrow verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 4 s.v. traffic, n.\", \"stance\": \"supports\", \"note\": \"'[ < F trafic, traffic ...]' — F&W too routes the word through French.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan, Dict. étym. des mots français dérivés de l'arabe (PHN.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'trafic' finds nothing; Pihan does not list trafic among French words of Arabic/Persian/Turkish origin.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"trâfîc\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian ترافیک terâfik / trâfik 'traffic (congestion)' is a 20th-c. loan from French trafic, part of the large body of European technical and administrative vocabulary that entered Persian through French from the late Qajar period and the Dār al-Fonūn onwards (French, not English, being the vehicle language of Iranian modernisation until the mid-20th c.). Wiktionary's Persian entry states 'Borrowed from French trafic'; the French final -c is written with ک and the first syllable is rendered with long â, both regular for French loans in Persian (compare ترافیک، فابریک، شیک). Mo'in's dictionary has no entry for it — grep of the two-volume Adena text returns nothing — which fits its recency. The chart gives this node no reference, correctly, since it is Nourai's own observation.\",\n          \"derivation_fa\": \"«ترافیک» وام‌واژه‌ای است نوین (سدهٔ چهاردهم خورشیدی) از فرانسویِ trafic، از همان لایهٔ گستردهٔ واژگان فنی و اداری اروپایی که از اواخر دورهٔ قاجار و از راه دارالفنون و زبان فرانسه وارد فارسی شد. ویکی‌واژه به‌روشنی می‌گوید «وام‌گرفته از فرانسویِ trafic». آوانگاری آن هم قاعده‌مند است: -c پایانی فرانسوی با «ک» و هجای نخست با «ا» کشیده نوشته می‌شود. در فرهنگ معین مدخلی برای آن نیست که با تازگی واژه سازگار است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%A7%D9%81%DB%8C%DA%A9\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the book gives this node no reference; verified against Wiktionary and by the absence of the word from Mo'in.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Adena 2-vol. (both volumes)\", \"stance\": \"silent\", \"note\": \"grep 'ترافیک' returns no hit — the word is too recent for Mo'in's lemma list.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. ترافیک (Persian)\", \"stance\": \"supports\", \"note\": \"'Borrowed from French trafic.' Definition: 'traffic (congestion)'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"traffic\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English traffic (first recorded c. 1500 as traffike/traffique, in the commercial sense 'trade, buying and selling') is from Middle French trafique, itself from Italian traffico; the modern sense 'movement of vehicles and people' is a 19th-c. development (Etymonline dates it to 1825). Klein gives exactly this chain, with the verb from French trafiquer. So the French → English arrow is beyond doubt; only the Arabic origin at the top of the chain (node #2) is contested.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی traffic نخستین بار حدود سال ۱۵۰۰ میلادی به صورت traffike/traffique و به معنی «داد و ستد» ثبت شده و از فرانسویِ میانه trafique و آن از ایتالیاییِ traffico گرفته شده است؛ معنی امروزیِ «رفت‌وآمد وسایل نقلیه» تحولی است در سدهٔ نوزدهم (اتیمآنلاین: ۱۸۲۵). کلاین نیز همین زنجیره را می‌دهد. این حلقه بی‌گمان درست است؛ تنها حلقهٔ آغازین (عربی ← ایتالیایی) محل بحث است.\",\n          \"sources\": [\"https://www.etymonline.com/word/traffic\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1637\", \"status\": \"supports\", \"note\": \"KLN_1966 p. 1637: 'traffic, n. — MF. trafique (F. trafic), fr. It. traffico ... Derivatives: traffic, intr. and tr. v. (— F. trafiquer)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 4 s.v. traf'fic, n. and v.\", \"stance\": \"supports\", \"note\": \"full entry with the senses 'the exchange of goods ... the business of transportation'; etymology '[ < F trafic ...]' — agrees on the French source, differs on the ultimate one.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt)\", \"stance\": \"silent\", \"note\": \"grep '^traffic|traffic,' finds only incidental uses of the English word inside other entries (barato, market); Skeat's concise edition carries no traffic headword.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Fšân\",\n      \"verdict\": \"disputed\",\n      \"modern_form\": \"Proto-Iranian *šan- / *san- 'to shake (down)'; New Persian افشاندن < Middle Persian afšāndan < *Hapa-šan- — the f is part of the preverb, not of the root, and no Avestan root fšān- is securely attested\",\n      \"note\": \"The root box is Nourai's condensation of Horn's entry no. 102 (Grundriss p. 24), where Horn compares 'aw. aiwi + fšūnayeinti \\\"sie weiden aus\\\", Yt. 14, 56 (Geldner)' — but adds his own '(?)'. Hübschmann repeats the comparison with '(?)' too (Persische Studien 183, 'afšandan \\\"ausstreuen\\\" H. 102 (?)'). Bartholomae's Altiranisches Wörterbuch does not lemmatise any aiβi.fšān-: the word at Yt 14.56 he prints under nam- (col. 1043) and calls 'Undeutlich', and s.v. *paršti- 'Rücken' he even proposes an emendation of the passage. Modern Iranian etymology has abandoned the reconstruction: Cheung, Etymological Dictionary of the Iranian Verb (2007) sets up *san 'to shake (down ?)' with Middle Persian ʾpsʾn- /afsan-/ 'to spread, scatter, sow' analysed as *apa- + *san, no Avestan cognate cited, and adds 'An IE etymology for *san is lacking'; Wiktionary's افشاندن analyses it as Proto-Iranian *Hápa 'away' + *šan 'to shake'. Abolghasemi (FFD 20-21), who gives an Old Iranian reconstruction for every neighbouring verb (افروختن، افزودن، افسردن، افگندن), pointedly stops at Middle Persian for افشاندن. So the root box should read Proto-Iranian *šan- 'to shake', not Avestan Fšân, and the segmentation aiwi + fšān is at best one of two competing analyses of the preverb.\",\n      \"note_fa\": \"این جعبهٔ ریشه فشردهٔ مدخل شمارهٔ ۱۰۲ هرن (ص ۲۴) است، آنجا که هرن اوستاییِ «aiwi + fšūnayeinti» را با علامت پرسش می‌آورد؛ هوبشمان نیز (پژوهش‌های فارسی، ص ۱۸۳) همان را با «(؟)» تکرار می‌کند. بارتولومه در «فرهنگ ایرانی باستان» هیچ مدخلی برای aiβi.fšān- ندارد و صورت مورد بحث در یشت ۱۴/۵۶ را ذیل ریشهٔ nam- می‌آورد و آشکارا «Undeutlich» (نامفهوم) می‌خواند. ریشه‌شناسی امروزیِ ایرانی این بازسازی را کنار گذاشته است: چونگ (۲۰۰۷) ریشهٔ ایرانی آغازین را ‎*san‎ «تکاندن» می‌داند و فارسی میانهٔ afsan- را ‎*apa-san-‎ تحلیل می‌کند؛ ویکی‌واژه هم «افشاندن» را ‎*Hápa‎ «دور» + ‎*šan‎ «تکاندن» می‌گیرد. ابوالقاسمی نیز در «فعل‌های فارسی دری» برای «افشاندن» — برخلاف افروختن و افزودن و افسردن و افگندن — هیچ صورت ایرانی باستانی نمی‌آورد. نتیجه: پژوهش امروزی این ریشه را رد می‌کند؛ به جای «اوستایی Fšân» باید نوشت «ایرانی آغازین ‎*šan-‎ (تکاندن)» و «ف» جزء پیشوند است نه ریشه.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%D8%A7%D9%86%D8%AF%D9%86\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"HRN:24\", \"status\": \"partial\", \"note\": \"HRN.txt leaf 46 (= printed p. 24, leaf = printed + 21 + 1 for the 0/1 offset), no. 102: 'efšānden \\\"ausschütten\\\", afšānden. aw. aiwi + fšūnayeinti \\\"sie weiden aus\\\", yt. 14, 56 (Geldner, 3 Yasht, 88) (?); phlv. afšāntan'. Horn does give the comparison Nourai turns into a root box, but he marks it '(?)' and never sets up an Avestan root Fšān as a lemma; the gloss 'sie weiden aus' ('they gouge out', of eyes at Yt 14.56) is also not 'spread, sprinkle'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 1043 s.v. nam-, and s.v. *paršti-\", \"stance\": \"contradicts\", \"note\": \"s.v. nam- 'mit fra ... 3) Kaus. \\\"niederbeugen, eindrücken\\\": frā *parštəm nəmaiieinti .. fš[ā]naiieinti (sd.) Yt. 14. 56. Undeutlich'; and s.v. *paršti- 'Rücken': '[Yt.14.56: lies ...]'. Bartholomae has no lemma aiβi.fšān- and declares the very passage Horn built the root on obscure.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007: 371-372 s.v. *san 'to shake (down ?)'\", \"stance\": \"contradicts\", \"note\": \"'*MIDDLE PERSIAN: (+ *apa-) BMP ʾpsʾn- (PZKWN-) /afsan-/ \\\"to spread, scatter, sow\\\" ... *NWIR: ... || (+ *apa-) NP afsandan/afsan- ... An IE etymology for *san is lacking.' No Avestan section at all: the root is *san with the preverb *apa-, not a root fšān-.\"},\n        {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 183 (§77-78)\", \"stance\": \"partial\", \"note\": \"'afšandan \\\"ausstreuen\\\" H. 102 (?)' listed among words in which 'ap. b = w ... in der Praep. aw = ap. awi- zu f (urspr. vor tonlosen Konsonanten)' — Hübschmann too treats af- as the preverb (from awi-), and marks Horn's Avestan comparison with a question mark.\"},\n        {\"src\": \"FFD\", \"where\": \"Abolghasemi, Fe'l-ha-ye Farsi-ye Dari pp. 20-21\", \"stance\": \"partial\", \"note\": \"«افشاندن / افشاند < فارسی میانه afšānd ؛ افشان < فارسی میانه afšān» — unlike افروختن، افزودن، افسردن، افگندن on the same pages, which all get an «ایرانی باستان *…» reconstruction, افشاندن gets none: Abolghasemi declines to reconstruct an Old Iranian form.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"aiwi-fšân\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The cross-reference to the root Ambhi is itself correct — Avestan aiβi- / Old Persian abiy- 'around, over' does continue PIE *h₂mbhi 'on both sides, around', the etymon of Greek amphí and Latin ambi-. What is not established is the compound. Horn (no. 102, the node's own reference) proposed 'aw. aiwi + fšūnayeinti' at Yasht 14.56 and immediately queried it; Hübschmann (PSt 183) repeats it with the same '(?)'. Bartholomae's dictionary, the standard lexicon of Avestan, has no entry aiβi.fšān-: the disputed word of Yt 14.56 is printed under nam- with the verdict 'Undeutlich', and under *paršti- 'Rücken' Bartholomae proposes emending the line. Meanwhile modern Iranian verb etymology reads the preverb differently: Cheung (2007) s.v. *san lists Middle Persian afsan- as *apa- + *san 'to shake down' (with Parthian wyšʾn- < *aua-, Khotanese ṣāñ-, Sogdian šn-, Balochi šant/šān-, Kurmanji reşandin), and Wiktionary follows with *Hápa + *šan. Under both the old and the new analysis the f-/af- is a preverb rather than the initial of the root; the difference is whether it comes from *abi- (Horn/Hübschmann, giving af before a voiceless consonant) or from *apa- (Cheung, Wiktionary), and the latter is now standard. An Avestan lemma aiwi-fšān 'spread over, spread around' therefore cannot be cited as attested.\",\n          \"derivation_fa\": \"ارجاع نمودارِ کتاب به ریشهٔ «Ambhi» درست است: اوستایی aiβi- و پارسی باستان abiy- «پیرامون، بر» بازماندهٔ هندواروپاییِ آغازینِ ‎*h₂mbhi‎ (یونانی amphí، لاتینی ambi-) است. اما خودِ ترکیبِ «aiwi-fšân» اثبات‌شده نیست: هرن آن را با علامت پرسش پیشنهاد کرده و هوبشمان هم با «(؟)» تکرار کرده است، حال آنکه بارتولومه در «فرهنگ ایرانی باستان» چنین مدخلی ندارد و صورت یشت ۱۴/۵۶ را «نامفهوم» می‌خواند و حتی تصحیح متن را پیشنهاد می‌کند. از سوی دیگر چونگ (۲۰۰۷) فارسی میانهٔ afsan- را ‎*apa-san-‎ می‌گیرد (با شواهد پارتی wyšʾn-، ختنی ṣāñ-، سغدی šn-، بلوچی šānt، کرمانجی reşandin) و ویکی‌واژه نیز ‎*Hápa + *šan‎. در هر دو تحلیل، «اَفـ» پیشوند فعلی است نه آغازِ ریشه؛ اختلاف تنها در آن است که از ‎*abi-‎ آمده (هرن و هوبشمان) یا از ‎*apa-‎ (چونگ)، و امروز دومی پذیرفته‌تر است. پژوهش امروزی این گره را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%D8%A7%D9%86%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:24\", \"status\": \"partial\", \"note\": \"HRN.txt leaf 46 (printed p. 24) no. 102: 'aw. aiwi + fšūnayeinti \\\"sie weiden aus\\\", yt. 14, 56 (Geldner, 3 Yasht, 88) (?)'. Horn is the source of the node, but the '(?)' is his own and the gloss he gives is not 'spread over'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1043 s.v. nam- (mit fra, Kaus.); also s.v. *paršti-\", \"stance\": \"contradicts\", \"note\": \"'frā *parštəm nəmaiieinti .. fš[ā]naiieinti (sd.) Yt. 14. 56. Undeutlich'. Grep of BRT.txt for all three occurrences of 'Yt 14. 56' shows no lemma aiβi.fšān-; the third is s.v. daēman- 'Auge', i.e. the passage is about eyes, matching Horn's odd gloss 'sie weiden aus'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *san 'to shake (down ?)'\", \"stance\": \"contradicts\", \"note\": \"MP afsan- is derived '(+ *apa-)', with cognate preverbal formations in Parthian '(+ *aua-) wyšʾn- \\\"to shake off, down\\\"' and NP '(+ *apa-) afsandan/afsan-'. No Avestan aiβi- compound is recognised.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p. 183, §77-78\", \"stance\": \"partial\", \"note\": \"'afšandan \\\"ausstreuen\\\" H. 102 (?)' and §78 'ap. b = w ... in der Praep. aw = ap. awi- zu f (urspr. vor tonlosen Konsonanten) oder v' — supports the preverbal analysis of af-, but with an explicit question mark on this verb.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"afšântan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Middle Persian word itself is solidly attested: MacKenzie, Concise Pahlavi Dictionary p. 5, 'afšāndan, afšān- [ʾpšʾn-tn' | N ~] spread, scatter, sow' (and in the English-Pahlavi index s.vv. 'scatter', 'sow', 'spread'). The Book Pahlavi spelling ʾpšʾntn' does not distinguish t from d, so Nourai's transliteration afšāntan (taken from Horn's 'phlv. afšāntan' and from Mo'in's footnote in Borhān) and MacKenzie's normalisation afšāndan are the same word; this is a convention difference, not an error. Mo'in's etymological footnote at BQT p. 1492 s.v. فشاندن reads «فشاندن ... <- افشاندن؛ پهلوی afšāntan (رک: اشتقاق، هوبشمان ...)؛ پاشیدن، ریختن، تکاندن، پراکندن», i.e. exactly Nourai's Pahlavi form and gloss. What is only plausible is the parent drawn above it: the Middle Persian verb is a preverb + root formation, but the preverb is now read as *apa- (Cheung: *apa-san-) rather than Av. aiwi-, and no Avestan antecedent is attested. Formally MP afšān- is the present stem, afšānd/afšāst the past, with the -tan infinitive; NP inherits both stems.\",\n          \"derivation_fa\": \"خودِ واژهٔ فارسی میانه استوار است: مکنزی در «فرهنگ کوچک پهلوی» ص ۵ می‌آورد «afšāndan, afšān- [ʾpšʾn-tn'] پراکندن، افشاندن، کاشتن». در خط پهلوی «ت» و «د» از هم بازشناخته نمی‌شوند، پس صورت «afšântan» نورایی (برگرفته از هرن و از حاشیهٔ معین در برهان قاطع) و «afšāndan» مکنزی یک واژه‌اند و این اختلافِ شیوهٔ آوانگاری است نه خطا. حاشیهٔ معین در برهان (ص ۱۴۹۲، ذیل «فشاندن») نیز می‌گوید: «فشاندن ... ← افشاندن؛ پهلوی afšāntan؛ پاشیدن، ریختن، تکاندن، پراکندن». آنچه تنها «با احتیاط پذیرفتنی» است پیکانِ بالای این گره است: فعل فارسی میانه ترکیبِ پیشوند + ریشه است، اما پیشوند را امروز ‎*apa-‎ می‌خوانند (چونگ) نه اوستاییِ aiwi-.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1492\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:1492 → BQT_v3_picofile.pdf pdf page 285, the ف/ط section. OCR of the last lines: «فشاندن - بفتح وکسر اول وفتح پنجم <- افشاندن ؛ پهلوی [afšāntan] ( رك . اشتقاق هوبشمان ۱۶۲ ...) ؛ پاشیدن ، ریختن ، تکاندن ، پراکندن.» The Latin Pahlavi form and the Hübschmann page number are garbled by the OCR, but the Persian text is clear and gives exactly the Pahlavi etymon Nourai cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 5 s.v. afšāndan\", \"stance\": \"supports\", \"note\": \"'afšāndan, afšān- [ʾpšʾn-tn' | N ~] spread, scatter, sow' (PHD.txt line 172; also PHD_mackenzie.txt line 891). Confirms the Pahlavi verb, its stems and its sense.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\", \"note\": \"grep -i 'afšān|afsān|afsan' in NYB_vol2_glossary.txt returns nothing; the verb does not occur in the texts Nyberg glosses.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *san\", \"stance\": \"partial\", \"note\": \"'BMP ʾpsʾn- (PZKWN-) /afsan-/ \\\"to spread, scatter, sow\\\"; Pres.: IND. 3sg. BMP /afsanēd/' — same Middle Persian verb, but derived from *apa-san-, not from an Avestan aiwi- compound.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"afšândan; afshân; afšŭn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"افشاندن afšāndan 'to sprinkle, scatter' is the direct continuation of Middle Persian afšāndan/afšān- with no change beyond the loss of Middle Persian final vowels; the by-form فشاندن fašāndan that the chart adds in its extra field arises by aphaeresis of the unstressed initial a- of the preverb, exactly as in افگندن/فگندن، افروختن/فروختن، افزودن/فزودن — Ḥāfeẓ's line quoted in the box («جرعه‌ای فشان بر خاک») uses the imperative of that shorter form. افشان afšān is the present stem used as an adjectival/agentive second member ('scattering', زرافشان، آتشفشان) and, absolutely, 'scattered'; Mo'in lists it as «(افا.) در بعضی کلمات مرکب به معنی افشاننده». افشون afšūn is a dialectal -ūn variant of افشان (Mo'in prints it as «افشون [= افشان]»), used as the name of an implement; Mo'in defines it as «افزاری است دارای پنجه‌ای چوبین (سه شاخه یا چهار شاخه) و دسته‌ای بلند که به وسیلهٔ آن غلهٔ کوفته را باد دهند و دانه را از کاه جدا سازند؛ انگشته، هسته» — a winnowing fork, not a rake for spreading sand, so Nourai's gloss is loose, though the derivation from افشاندن 'to scatter' that the chart draws is correct. Horn no. 102 and Mo'in's footnote at BQT 1492 both give precisely this Persian ← Pahlavi step.\",\n          \"derivation_fa\": \"«افشاندن» دنبالهٔ مستقیم فارسی میانهٔ afšāndan / ستاک حال afšān- است و جز افتادن واکهٔ پایانیِ فارسی میانه دگرگونی دیگری ندارد. صورت کوتاه «فشاندن» از افتادن «اَ»ی بی‌تکیهٔ آغازین (پیشوند) پدید آمده است، درست مانند افگندن/فگندن و افروختن/فروختن؛ بیت حافظ در همین جعبه («جرعه‌ای فشان بر خاک») امرِ همین صورت کوتاه است. «افشان» ستاک حال است که در ترکیب‌ها معنی «افشاننده» می‌دهد (زرافشان، آتشفشان) و به‌تنهایی «پراکنده». «افشون» گونهٔ ‎-ūn‎ دار «افشان» است؛ معین آن را چنین تعریف می‌کند: «افزاری است دارای پنجه‌ای چوبین (سه یا چهار شاخه) و دسته‌ای بلند که با آن غلهٔ کوفته را باد دهند و دانه را از کاه جدا سازند» — یعنی «شن‌کش/چنگک» نیست بلکه «پنجه/چهارشاخِ بادافشانی» است؛ پس معنیِ نورایی دقیق نیست هرچند اشتقاق درست است. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%D8%A7%D9%86%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:24\", \"status\": \"supports\", \"note\": \"Horn no. 102 (printed p. 24): 'efšānden \\\"ausschütten\\\", afšānden ... phlv. afšāntan' — the New Persian verb and its Pahlavi antecedent, exactly this node's arrow.\"},\n            {\"ref\": \"BQT:1492\", \"status\": \"supports\", \"note\": \"Mo'in's footnote s.v. فشاندن (vol. 3, pdf p. 285 of the picofile scan): «فشاندن ... ← افشاندن؛ پهلوی afšāntan؛ پاشیدن، ریختن، تکاندن، پراکندن» — gives both the NP head form and the variant فشاندن that Nourai lists in his extra field.\"},\n            {\"ref\": \"AEF:137\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq, Asās-e Eshteqāq-e Fārsi vol. I — refs_online.json: not digitised anywhere; since it is the Persian translation of Horn (with Hübschmann's notes), the instruction is to verify it against HRN and HUB, which was done above (HRN no. 102, HUB p. 183).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Adena 2-vol. v.1, s.vv. افشاندن، افشان، افشون\", \"stance\": \"supports\", \"note\": \"«افشاندن: [= افشانیدن = فشاندن = فشانیدن] (مص‌م.) ... ریختن و پاشیدن، پراکنده کردن»; «افشان: [= فشان] (افا.) در بعضی کلمات مرکب به معنی افشاننده آید: آتش‌افشان»; «افشون: [= افشان] (ا.) افزاری است دارای پنجه‌ای چوبین (سه شاخه یا چهار شاخه) و دسته‌ای بلند که به وسیلهٔ آن غلهٔ کوفته را باد دهند و دانه را از کاه جدا سازند؛ انگشته، هسته». Confirms all three words and the fašāndan variant; refines the gloss of افشون.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 5\", \"stance\": \"supports\", \"note\": \"'afšāndan, afšān- [ʾpšʾn-tn' | N ~]' — the '| N ~' notation means the New Persian form is identical, i.e. MacKenzie himself equates NP افشاندن with the Pahlavi verb.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *san\", \"stance\": \"supports\", \"note\": \"'*NWIR: ... || (+ *apa-) NP afsandan/afsan-, Gil. (Rsht.) fišan- \\\"to disperse\\\"' — the Gilaki f-initial form is the same aphaeretic type as Persian فشاندن.\"},\n            {\"src\": \"FFD\", \"where\": \"Abolghasemi, Fe'l-ha-ye Farsi-ye Dari pp. 20-21\", \"stance\": \"supports\", \"note\": \"«افشاندن / افشاند < فارسی میانه afšānd ؛ افشان < فارسی میانه afšān» — the New Persian past and present stems are both derived straight from Middle Persian.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-165.json > /dev/null && echo \"JSON OK\"",
 "description": "Write verification file and validate JSON"
}
```


### [2026-09-05T20:47:51.803Z] TOOL RESULT

```
JSON OK
```


## [2026-09-05T20:47:55.099Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 tools/verify_check.py 165",
 "description": "Run verify_check for page 165"
}
```


### [2026-09-05T20:47:56.794Z] TOOL RESULT

```
nodes verified: 8/8
node verdicts: {'plausible': 3, 'confirmed': 4, 'disputed': 1}
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'not_checked': 3, 'supports': 6, 'partial': 1}
books consulted: {'supports': 10, 'contradicts': 4, 'silent': 6, 'partial': 2} | by book: {'MON': 3, 'FSD': 3, 'CHEUNG': 3, 'PHD': 2, 'FVQ': 1, 'KLN': 1, 'LKT': 1, 'DEV': 1, 'PHN': 1, 'Wiktionary': 1, 'SKT': 1, 'BRT': 1, 'HUB': 1, 'NYB': 1, 'FFD': 1}
```


## [2026-09-05T20:48:13.251Z] AGENT

Page 165 verified — `data/verification/page-165.json` written, `verify_check.py 165` reports 8/8 nodes, 0 PROBLEM lines.

**Counts:** roots 1 confirmed / 1 disputed; nodes 4 confirmed, 3 plausible, 1 disputed. Ref checks: 6 supports, 1 partial, 3 not_checked (FVA:313, AEF:137 — neither digitised; node #4 carries no ref). 22 book consultations across 15 books.

**Disputed:**
- ROOT `Fšân` [Avestan] — no Avestan root fšān- is attested. Nourai condenses Horn no. 102, where Horn himself writes "(?)"; Hübschmann repeats the "(?)"; Bartholomae has no lemma aiβi.fšān- and calls the Yt 14.56 passage "Undeutlich". Cheung 2007 s.v. *san and Wiktionary derive MP afšān- from *apa- + *šan- 'to shake'; Abolghasemi gives no Old Iranian form at all. The f belongs to the preverb, not the root.
- Node #1 `aiwi-fšân` [Avestan] — same reason; the ☞Ambhi cross-reference (aiβi- < PIE *h₂mbhi) is itself correct, but the compound is unattested and the preverb is now read *apa-, not *abi-.

**Plausible (worth the owner's eye):**
- Entry 0 #1 `forqân` — Persian got it from Arabic (arrow fine), but Jeffery FVQ 225-229 and Wiktionary derive Arabic furqān from Syriac purqānā 'salvation', not from f-r-q. `farq` itself is confirmed.
- Entry 0 #2 `traffico` — Klein's Arabic tafrīq origin is one of three competing theories; OED/Wiktionary prefer VL *transfricare, F&W give trans + vicis, and Lokotsch (the register of European Arabisms) has no entry at all.
- Entry 1 #2 Pahlavi `afšântan` — the word is confirmed (MacKenzie p.5, Mo'in at BQT 1492); only its drawn parent is doubtful. afšāntan vs afšāndan is a transliteration convention, not an error.

**No extraction errors** — the JSON matches the printed page (image saved to `data/verification/sources/refs/ocr/BOOK/165.png`). Two book-side quibbles, faithfully extracted: the page prints Italian "traficare" for standard *trafficare*, and Nourai's NOTE renders Klein's "to make over" as "to take over". Also, Mo'in defines افشون as a winnowing fork, not "rake for spreading sand" — Nourai's gloss is loose but the derivation holds. Six web sources archived via `fetch_source.py`.
