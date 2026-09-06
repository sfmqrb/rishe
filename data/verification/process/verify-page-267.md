# Verification process log — verify-page-267


## [2026-09-06T20:49:55.579Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 267 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-267.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-267.json. Write /home/sfmqrb/git/rishe/data/verification/page-267.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 267` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:49:56.738Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T20:49:57.580Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:49:57.601Z] TOOL RESULT

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


## [2026-09-06T20:49:58.145Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-267.txt"
}
```


### [2026-09-06T20:49:58.172Z] TOOL RESULT

```
1	=== PDF page 267 (book page 237) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ki 2, Ko 2, Kyô, Ke 2, Ghe 2 : this  (refs POK:417,609; KLN:710)
4	#1 (parent #0) [Avestan] refs=KLN:735; POK:417 | zî : for, because, indeed ; nôit-zî
5	#2 (parent #0) [Germanic] refs=AHD | hi
6	  #3 (parent #2) [English] refs=AHD | he, him, his, her, here, hence, it
7	#4 (parent #0) [Indo-European] refs=AHD:1523 | Ke-e-tero : other part, other time, again ☞I 2
8	  #5 (parent #4) [Latin] refs=AHD:1523; KLN:545; POK:284 | ce-terus : the other part ; et-cĕ-terî : and other things ☞Eti
9	    #6 (parent #5) [English] refs=None | et cetera
10	--- entry 1 ---
11	ROOT Kiĕ 1 -> redirect to Kei 1
12	--- entry 2 ---
13	ROOT Kie 2 -> redirect to Kei 2
14	--- entry 3 ---
15	ROOT [Indo-European] Kiĕs : bug, tick  (refs IEC:622)
16	#1 (parent #0) [Armenian] refs=IEC:622 | čeč : mite
17	#2 (parent #0) [Greek] refs=IEC:622 | sěs, seos : mite
18	#3 (parent #0) [Persian] refs=IEC:622; MON:1795 | sâs «ساس ۲» : louse, bug
19	--- entry 4 ---
20	ROOT [Indo-European] Kiph : thin flexible twig  (refs POK:598)
21	#1 (parent #0) [Sanskrit] refs=POK:598; WLD1:452 | šiphâ, čiphâ : twig, hair
22	  #2 (parent #1) [Persian] refs=BQT:1272; MON:2052 | šafš «شَفَش ( شَفشه ، شَفشَف )» : twig, wire ; šafšâhang «شفشاهنگ ، شفتاهنج» : a tool for extruding thin silver and gold wires
23	#3 (parent #0) [Greek] refs=POK:598 | xiphos : branch, rod
24	  #4 (parent #3) [Arabic] refs=TAD:39,78 | sayf : sword ; s.y.f : to strike with a sword
25	    #5 (parent #4) [Persian] refs=MON:1979 | sayf «سیف» : sword
26	
```


## [2026-09-06T20:50:01.184Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-267.json",
 "description": "Read source JSON for page 267"
}
```


### [2026-09-06T20:50:01.227Z] TOOL RESULT

```
{
  "pdf_page": 267,
  "book_page": 237,
  "entries": [
    {
      "root": {
        "name": "Ki 2, Ko 2, Kyô, Ke 2, Ghe 2",
        "lang": "Indo-European",
        "refs": "POK:417,609; KLN:710",
        "gloss": "this"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:735; POK:417",
          "words": [
            {"translit": "zî", "gloss": "for, because, indeed", "script": null},
            {"translit": "nôit-zî", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hi", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "he, him, his, her, here, hence, it", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "AHD:1523",
          "words": [
            {"translit": "Ke-e-tero", "gloss": "other part, other time, again", "script": null, "see": ["I 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": "AHD:1523; KLN:545; POK:284",
          "words": [
            {"translit": "ce-terus", "gloss": "the other part", "script": null},
            {"translit": "et-cĕ-terî", "gloss": "and other things", "script": null, "see": ["Eti"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "et cetera", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Kiĕ 1", "redirect": "Kei 1"},
      "nodes": []
    },
    {
      "root": {"name": "Kie 2", "redirect": "Kei 2"},
      "nodes": []
    },
    {
      "root": {
        "name": "Kiĕs",
        "lang": "Indo-European",
        "refs": "IEC:622",
        "gloss": "bug, tick"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Armenian",
          "refs": "IEC:622",
          "words": [
            {"translit": "čeč", "gloss": "mite", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:622",
          "words": [
            {"translit": "sěs, seos", "gloss": "mite", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:622; MON:1795",
          "words": [
            {"translit": "sâs", "gloss": "louse, bug", "script": "ساس ۲"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kiph",
        "lang": "Indo-European",
        "refs": "POK:598",
        "gloss": "thin flexible twig"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:598; WLD1:452",
          "words": [
            {"translit": "šiphâ, čiphâ", "gloss": "twig, hair", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1272; MON:2052",
          "words": [
            {"translit": "šafš", "gloss": "twig, wire", "script": "شَفَش ( شَفشه ، شَفشَف )"},
            {"translit": "šafšâhang", "gloss": "a tool for extruding thin silver and gold wires", "script": "شفشاهنگ ، شفتاهنج"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:598",
          "words": [
            {"translit": "xiphos", "gloss": "branch, rod", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "TAD:39,78",
          "words": [
            {"translit": "sayf", "gloss": "sword", "script": null},
            {"translit": "s.y.f", "gloss": "to strike with a sword", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1979",
          "words": [
            {"translit": "sayf", "gloss": "sword", "script": "سیف"}
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


## [2026-09-06T20:50:01.816Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T20:50:01.876Z] TOOL RESULT

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


## [2026-09-06T20:50:12.492Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','IEC','WLD','WLD1','MON','BQT','TAD','SYN','LEW','LAT','HRN','HUB','ARY','PLA','AFM','SKT','FVQ','ARB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:700]); print()\n\""
}
```


## [2026-09-06T20:50:13.204Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-259.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:3000])\""
}
```


### [2026-09-06T20:50:14.327Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015

WLD1 null

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git
```


### [2026-09-06T20:50:16.081Z] TOOL RESULT

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
---
{
 "entry": 0,
 "root": "Kerd 1, Kred",
 "verdict": "confirmed",
 "modern_form": "PIE *ḱḗr, oblique stem *ḱr̥d- (root *ḱerd-) 'heart'; with the compound *ḱred-dʰeh₁- 'to place one's heart, trust'",
 "note": "Pokorny p.579 bottom–580 heads the entry exactly '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’', so Nourai's headword 'Kerd 1, Kred', the language label 'Indo-European' and the gloss 'heart' all reproduce his source correctly; AHD (Watkins) has 'kerd-1. Heart. [Pok. kered- 579.]'. The one substantive caveat concerns the 'kred-' half: Pokorny himself (p.580) says the kred-dhē- 'believe' group is 'nicht hierher' (not to be connected with 'heart'), and Buck 17.15, Klein s.v. heart and Ernout–Meillet s.v. cor agree; modern standard works (Watkins/AHD, de Vaan 2008 s.v. crēdō, Wiktionary) do connect it, analysing *ḱred-dʰeh₁- as 'to place one's heart'. Nourai therefore follows the newer, now dominant, view — but not the page of Pokorny he cites. The Iranian branch has a further complication that the chart passes over: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, Av. zərəd-, PII *ȷ́ʰā́rd) where *ḱ- is expected, 'unexplained voiced aspiration' (Wiktionary), 'mit init. as if fr. IE gh, due to a blend with some other word' (Buck 251).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *ḱḗr (ستاک غیرفاعلی *ḱr̥d-، ریشهٔ *ḱerd-) به معنی «دل، قلب» است و پوکورنی در ص ۵۷۹–۵۸۰ سرواژه را دقیقاً «kerd-, kērd-, kr̥d-, kred-: Herz» آورده؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. تنها نکتهٔ محل بحث بخش kred- است: خودِ پوکورنی در ص ۵۸۰ پیوند kred-dhē- «باور داشتن» را با «دل» رد می‌کند و باک و کلاین و ارنو–مه‌یه نیز همین نظر را دارند، اما واتکینز (AHD)، دِ وان و ویکی‌واژه آن را می‌پذیرند و *ḱred-dʰeh₁- را «دل نهادن» می‌دانند؛ یعنی نورایی از دیدگاه نو پیروی کرده است نه از صفحه‌ای که به آن ارجاع داده. نکتهٔ دیگر آنکه در هندوایرانی به جای *ḱ- انسدادی واکدارِ دمیده دیده می‌شود (سنسکریت hṛd-، اوستایی zərəd-) که هنوز توضیح قطعی ندارد.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r",
  "https://en.wiktionary.org/wiki/credo%23Latin",
  "https://www.etymonline.com/word/heart"
 ],
 "ref_check": [
  {
   "ref": "POK:579",
   "status": "supports",
   "note": "Pokorny IEW p.579 (bottom) – 580, read in POK_02.txt leaf 239–240 (awk 'BEGIN{RS=\"\\f\"} NR==239'): '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’. Arm. sirt … gr. καρδία (att.), κραδίη (hom.) … lat. cor (aus *cord) … got. hairto, ahd. herza, ags. heorte, anord. hjarta n. ‘Herz’ (*ḱērd-on-)'. Exactly Nourai's root name and gloss."
  },
  {
   "ref": "SYN:251",
   "status": "supports",
   "note": "Buck, Selected Synonyms p.251 = §4.44 HEART (SYN.txt leaf 289, page number '251' printed in the running head above '4.44 HEART'): 'Most of the words for ‘heart’ belong to an inherited group … 1. IE *ḱerd-, etc., with gradation. Walde-P. 1.423 ff. Ernout-M. 219 f.'"
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. kerd-1 (AHD_wat
```


## [2026-09-06T20:50:24.789Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 70 71 72 73 74 75 76 77; do echo \"=== NR=$n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$n'' POK_02.txt | head -5; done"
}
```


## [2026-09-06T20:50:25.971Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ḱi-\\|ki-, ke-, ko-\\|ko-, ke-\" POK_02.txt | head -20"
}
```


### [2026-09-06T20:50:26.608Z] TOOL RESULT

```
=== NR=70 ===
 (<:* ghasto-);  daneben  *ghazdh-  in  mir.  ^fa« , Weiden-
413
rute^;  mir.  tris-gataim  ^durchbolire^;  vielleicht  dazu  air.  gataid  ^stiehlt-  als ^sticht  an^?  (Thurneysen  KZ.  63,  114*);
got.  gazds  m.  ,StacheF;  aisl.  gaddr  ,Stacliel_,  Spitze^,  as.  ßurgard  ^Feuer- crabel^,  ahd.  gart  m.  ^stimulus^;  dazu  mit  zä- Ableitung  ags.  gierd  f.  ,Rute^; afr.  ierde  , Gerte,  Meßrute*^,  as.  gerdia  ,Gerte,  Rute,  Stab,  StrahP,  ahd. gartia^  gertia  ,Rute,  Zepter^.
WP.  I  541,    WH.  I  636,  869.
=== NR=71 ===
n';    ahd.  *goto,    gota,    mhd.    g'öt{t)e,   got[t)^ .Pate,  Patina
WP.  I  529  f.,  Trautmann  367;    ausführl.  Lit.  bei  Feist  227  f.
ghauo-  ,falscb.  erlogen'??
Lat.  haud  Begriffsnegation  .nicht',  vielleicht  aus  ^hauidom  >  *Jmudom (>  haud  wie  nihilum  >  nihil),  neutr.  Adjektiv  .falsch  (wäre  es)' ;
air.  gäu,  gäo,  gö  f.  .Unrichtiges.  Lüge',  gü-forcell  .falsches  Zeugnis* mcymr.  geu,  ncymr.  gau  .falsch'.  Subst.  .Lüge',  corn.  gow  m.  ds..  bret gaou  ds. ;  abgeleitet  mcymr.  geuawc,  ncymr.  euog  .schuldig'.  z^;
=== NR=72 ===
  humilis  , niedrig' ( -vd-af^ccXög)  ]  im  Osk.-Umbr.  * homi-teros,  -temos  als  Kompar.  Superl.  vom Lok.  *homi  ,unten'  (:  ai.  ksdmi)  :  osk.  hu[n]truis  ,inferis',  huntrus  ,inferös'; umbr.  hutra,  kontra  ,lnfrä^  Abi.  hondomu  ,infimö';  umbr.  hondu  ,pessum- datö'  aus  *hon(d)-töd]  über  lat.  hümänus  s.  unten;
air.  du,  Gen.  don  ,Ort,  Stelle'  (Pedersen  KG.  I  89,  s.  auch  unten  zu duine]  die  Entw.  von  ghd  zu  d-  stimmte  zu  t  aus  -kp-  in  art  ,Bär'  aus /kpos]  n  statt  m  wie  in  '^d^övoq  aus  der  Vorstufe  *dön  —  aus  *  dörrt  —  von da  verschleppt);
lit.  itemej  lett.  zeme,  apr.  same,  semme  ,ErdeS  semmai  ^nieder'  (:  xaiialy s.  oben),  lett.  zem  ,unter*  (wohl  Verkürzung  des  Lok.  zeme);  lit.  zemas, lett.  z^ms  ^niedrig';
aksl.  zemlja  ,Erde';  dazu  auch  aksl.  zmhja  , Schlange'  (,auf  der  Erde kriechend,  x-^^H-^^og'),  zmbjb  , Drache'.
Dazu  Worte  für  ,Mensch'  als  , Irdischer': -  lat.  homö,  -inis  ,Mensch',  alat.  hemö  (auch  in  nemo  , niemand'  aus  *ne- Äemö),  Akk.  hemönem]  zu  humus  wohl  hümänus  , menschlich',  mit  unklarem Vokalismus  (*hoim-  würde  zum  oi  des  air.  PI.  doini  , Menschen'  stimmen, falls  hier  alter  Diphthong  vorläge,  aber  für  ein  idg.  *gdhoim-  fehlt  jede Wahrscheinlichkeit;  s.  auch  unten);  osk. -umbr.  *homön-  (Ablautstufe  *ghom- wie  humus,  gegenüber  lat.  hemön-  oder  einzeldialektischer  Umlaut  aus *hemün-),  osk.   kumuns  ,homines',  umbr.   homonus  ,hominibus';
=== NR=73 ===
de^  und  toch.  A  tkam,  Gen.  tkanU B  kern  ds.  werden  durch  Metathese  aus  *g{e)dhom-,  *gh{e)dhom  (Pede.sen Group.  41  f.),  dieses  aus  idg.  *dh(e)ghom  (Kretschmer  Gl.  20,  66  f.)  erklärt- dagegen  mit  beachtlichen  Gründen  Benveniste  Mel.  Van  Ginneken  193 ff/.: eine  Wurzel  *dhegh-  setzt  auch  Specht  Dekl.  241  an ;  ich  würde  die  hitt! und  toch.  Formen  mit  Benveniste  lieber  fernhalten.  :^.
WP.  I  662  ff.,  WH.  I  654  f.,  663  ff.,  869,  Trautmann  369.  #;
ghäies  (schwundst.  ghdis?),  vereinfacht  (?)  zu  ghSes,  ghißs,  ghes  ,gestemV ~Ai.  liydh  ,gestern'  (ghies),  hyastana-h  ,gestrig',  av.  zyö,  apers.  diya{ka\ pers.  di{g)]
gT.  eleisch  asg-ög'  x^k  Hes.  (aus  *xt£S,  idg.  ghies?);  gr.  x^k  {*9hdes), h^k  (nach  iytsLvog  :  y,eTvog,  selbständige  Partikel  oder  Vorschlagsvokal, s.  oben  S.  283  und  Schwyzer  Gr.  Gr.  I  413,  Lejeune  Traite  182);  x^i-^dg, adverb.  x^t^a  , gestrig',  nach  Schwyzer  Gr.  Gr.  I  351  aus  X-^k-{-*dtd zu  ai.  a-dyä  ,heute'  (Instrum.  von  idg.  *dios  ,Tag';  fehlt  oben  S.  183),  mit vortoniger  Schwächung  des  e  zu  i,  nach  Specht  KZ.  68,  205  aus  *ghdis >  ghis  mit  Adverbialsuffix  (wie  in  gr.  xQvß-da) ;  Xi9-£0't)'0g  , gestrig' ;
alb.  dje  ,gestern',  dial. , morgen'  (*ghes),  djetliine  ds.,  para-dje  ,vorgestern';
=== NR=74 ===
M ,fischen',  itvynas  m.  , Fischschuppe',  \Qtt.  zvini  m.  PL  ,Fischschuppen';  apr. sucka-ns  neben  Ix^g,  wie  lat.  sucu-la  neben  süs,  anord.  askr  neben  lit.  uosis.
417
Zur  Anlautfrage  {ghd  oder  (jhi'>)  vgl.  Schwyzer  Gr.  Gr.  I  325;  gleich- artig' ist  besonders  x^(^^'  '•  ^^^^^^>  und  eine  Parallele  mit  k-  bietet  hAxlvog:  ein. Kein  ganz  sicherer  Hinweis  auf  *gh,i'  ist,  da  in  seiner  Zugehörigkeit etwas  zweifelhaft,  der  Fischname  alt.  schwed.  gius,  nschwed.  gas  ,Perca Lucioperca^  nhd.  dial.  giesen  ,Cyprinus  cephalus^  und  alt.  schwed.  fiska- qiusen  ,ein  Raubvogel,  Falco  haliaetus',  worin  ein  *gji(se  , Fischer'  stecke.
WP.  I  664,  Trautmann  373,  Schwyzer  Gr.  Gr.  I  325,  413;  zum  idg.  d ycr\,  zuletzt  Lejeune  Traite  de  Phonetique  grecque  S.  31  f.
p-üze-,  g'^o-  u^d  ähnliche  enklitische  Partikeln  zur  Verstärkung  des  vorher- gehenden Wortes.  Es  scheinen  zwei  Gruppen  geschieden  werden  zu müssen,  einzelsprachlich  aber  z.  T.  die  eine  an  Stelle  der  andern getreten  zu  sein:  1.  gJie,  gho,  2.  mit  palatalem  Gutt.,  der  in  den  europ. Sprachen  als  g,  im  Ar.  als  gh  erscheint  (wie  in  den  Fällen  wie  gr.  yiwg: ai.  hdnuh),  also  eine  von  der  normalen  sog.  Media  aspirata  verschie- dene Artikulationsart  aufwies,  und  dem  Vokal  i  oder  e.
=== NR=75 ===
n.
2.  -i(b)^:
in  ai.  hi,  av.  zl  hervorhebende  Partikel  (nd  hi,  nahi,  av.  nöit  zl]  ai.  kdr-hi jwann?',  tdr-hi  , damals'  u.  dgl.),  hinter  dem  ersten  Wort  des  Satzes  ,denn  ja';
27
418
=== NR=76 ===
k',  intr.  ,weiche,  gehe zurück',  wie  das  Med.  Daß  ^«Aaw  ,lasse  nach,  werde  schlaff  oder  lose' auf  einem  partizip.  Adj.  "^ghd-lo-s  ,fortgehend'  oder  ,klaffend,  lose'?  beruhe, ist  vielleicht  erwähnenswert;  nach  Meillet  Esquisse  36  eher  zu  arm.  xal ,Spiel',  xaiat  ,f riedlich'  (mit  idg.  ä;ä-);
419
ahd.  gän  (=  ai.  häna-m)  .gehen^,  afries.  as.  ags.  gän,  aschwed.  adän. qä,  krimgot.  geen  ds. ;  über  die  Nebenform  ahd.  gen  s.  Kluge ^^  193^  Braune Ahd.  Gr.5  §3821;  ^it.  bei  Feist,  182  b.
Mit  der  Bed.-Färbung  A:
gr.  *xfiTLg  (Risch  Wortbildg.  d.  hom.  Spr.  74)_,  Dat.  x9}T£t  ,in  Erman- o-elung  von*^,  ablaut.  [*glid-t-)  %aTB(i),  yiOixiZ,i)i  ^ermangle,  bedarf,  ersehne,  be- o-ehre'^;  x^^og  ^beraubt,  leer^  (^  lat.  *hero-  in  heres),  xr^qa  ,Waise,  Witwe'^; mit  Abtönung  %wQog,  xiogä  ,leerer,  freier  Raum,  freies  Land  (im  Gegensatz zur  Stadt),  Gegend^,  epid.  ^w^ä  ,leere  Augenhöhle^,  x^Q^S  Adv.  und  Präp. m.  Gen.  ,getrennt;  ohne;  mit  Ausnahme  von;  außer^,  xw^/^w  ,trenne^, ^(ogstv  ,fassen,  aufnehmen  können,  von  Gefäßen^  (eig.  ,Raum  geben^)  und weichen,  fortgehen ;  gehen  überhaupt^ ;
=== NR=77 ===
420
.    skr.   zjäm,   zjäti   ,den   Mund   aufsperrenS    Iterativa   aksl    zijajq,,  zä russ.  zijdju,  -dth  ds.  und  sloven.  z^vati  ,den  Mund  geöffnet  halten', zivati,   russ.   zevdth   ,gähnen'    (sloven.   z^v,   poln.  zieio,  russ.  zev  ,Racli(
mit  p  (vgl.  unten  die  Wzf.  gheip-):  big.  ^e'paw,  poln.  ziepac  ,mit atmen',  klr.  ztpaty  ,nach  Atem  schnappen',  cech.  zipati  ^keuchen'.
Ähnlich,  aber  nach  den  e-Verben,  ahd.  glen  ,gähnen'  (wäre  got.  *gijf^ -aida)]  daneben  mit  noch  klärungsbedürftigem  (aber  schwerlich  aus  ^^ Wzf.  ghöM-  stammendem)  lo  im  Hiat  ahd.  anagiwen  ^inhiare',  geioön  ,^^ Mund  aufsperren,  gähnen'  (mhd.  geicen,  gücen  ds.),  ags.  giwian,  giowia^ ,verlangen,  fordern'  (aus  ,*mit  offenem  Munde,  gierig  wonach  lechzen«}» dazu  aisl.  ^^ä  f.  (*giwo)  einerseits  ,Spalte,  Kluft  in  der  Erde',  andrerseiti (von  ,lechzen'  aus)  ,wollüstiges  Leben',  mhd.  giude  (*giwipö)  ,geräuschvolle Freude',  giuden  ,prahlen,  großtun  (*den  Mund  weit  auftun);  in  geräusch* voller  Freude  sein,  verschwenderisch  leben',  nhd.  vergeuden]  ahd.  tw^innau ,auftun,  öffnen,  aufschneiden,  spalten'  aus  *ginuan  ist  wohl  Faktitiv  2^ ahd.  ginen  (s.  unten)  in  formellem  Anschluß  an  das  lautähnliche  ii^mwan,
sko-Präsens :  lat.  Mscö,  -ere  (*ghl-skö)  ,gähnen,  klaffen,  aufgesperrt  sein*; ähnlich  ags.  giscian,  mhd.  gischen  ,schluchzen'  und  norw.  mdartl.  geisktt ,die  Beine  ausspreizen'  (s.  Persson  Beitr.  318).
```


### [2026-09-06T20:50:26.650Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T20:50:38.901Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *609 *$\\|^ *610 *$\" POK_02.txt | head && echo \"--- awk find\" && awk 'BEGIN{RS=\"\\f\"} /^[[:space:]]*609[[:space:]]*$/ || /\\n609\\n/ {print \"leaf \" NR}' POK_02.txt | head"
}
```


## [2026-09-06T20:50:40.378Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ko-, ke-\\|dieser'\\|k'^o-\\|kOj  kej\\|ki-,  ko-\" POK_02.txt | sed -n 1,40p"
}
```


### [2026-09-06T20:50:40.672Z] TOOL RESULT

```
4195:609
--- awk find
leaf 269
```


### [2026-09-06T20:50:40.717Z] TOOL RESULT

```
4196:^o-,  ie-  (mit  Partikel  ke  ,hier'),  k(e)i-,  k(i)io-  Pronominalstamm  , dieser', ursprünglich  ich-deiktisch,  später  auch  ,jener';  ki-na  ,hinweg^
4197:Arm.  -s  ,Artikel'  (z.  B.  mard-s  ,der  Mensch'),  sa  ,dieser',  ai-s  ds.,  a-s-t ,hier';
4209:apr.  schis  (Adverb  schal  ,hier^),  lit.  fis  (lett.  sis  =  aksl.  sh  , dieser'),  Gen.  Üt. Ho,  aksl.  sego,  Akk.  PL  aksl.  shj^,  fem.  lit.  B  (lett.  H)  =  aksl.  si,  Akk.  S». f.  shj^,  lit.  B-tas  , dieser'  (^ki-to-),  dazu  staX  ,sieh  hier'  (alt  sitai),  apr. stas  ,der';  lit.  Haüdien,  lett.  Süodien  ,heute',  lit.  s^,  lett.  §e  ,hier',  aksl. si-ch  jTOLOVTog*  usw. ;
```


## [2026-09-06T20:50:42.597Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4190,4230p' POK_02.txt"
}
```


### [2026-09-06T20:50:42.640Z] TOOL RESULT

```
WP.  I  476,  WH.  I  261 ;  Wissmann  Nora,  postverb,  64,  183.
kneug-  , Schall  wort?'
Gr.  Y.vvCäv,  -eXv  ,knurren  (von  Hunden),   wimmern    (von  Kindern)' :  lit. kniaükti  ,miauen'.  Wohl  nur  zufällige  Ähnlichkeit. WP.  I  476.
knid-,  knid-,  sknid-  ,Laus,  Ei  der  Laus,  Nisse',  oft  tabuistisch  umgestaltet; vgl.  oben  S.  437  ghnldä  ds. Arm.  anic  ,Laus'  (*mc?-s); alb.  theni  ,Laus'  {*k{e)nid-)-,
gr.  xoWg,  -löoq  f.  (*knid-s),  wohl  an  ^/.öviq  , Staub'  angeglichen; mir.  sned  f.  ,Nisse',  kymr.  PI.  nedd,  nkorn.  ned,  bret.  nez  ds.  (*s(k)nida); ags.  hnitu  f.,  ahd.  (h)niz,  nhd.  Nisse  ,Ei  der  Laus'  (*knidä). Könnte  zu  (s)ken-  ,kratzen'  gehören,  wie  ghnldä  zu  ghen-  ds. WP.  I  461,  WH.  I  783  f.,  Specht  Idg.  Dekl.  44,    Trautmann  93.
609
^o-,  ie-  (mit  Partikel  ke  ,hier'),  k(e)i-,  k(i)io-  Pronominalstamm  , dieser', ursprünglich  ich-deiktisch,  später  auch  ,jener';  ki-na  ,hinweg^
Arm.  -s  ,Artikel'  (z.  B.  mard-s  ,der  Mensch'),  sa  ,dieser',  ai-s  ds.,  a-s-t ,hier';
phryg.  asixov{v)  , diesem'  {*kem-\-öi)\  anders  Pedersen  Tochar.  259.
gr.  Partikel  *xfi  in  -iistvog  und  ixetvog,  dör.  lesb.  y,f]vog  ,]ener'  aus  *(€)xs-evog; daraus  rückgebildet  (^)xa  ,dort',  {h)-/.BLd'i  usw. ;  *Ko-  in  arj^sgov,  att.  Trj(j,SQOv ,heute'  ('^xiaf.iegov),  wonach  auch  *xtß/fiTfig  ,heuer'  in  orjzeg,  att.  Tfjzeg, dor.  oäTsg]
lat.  -ce,  ce-Partikel  in  ce-do  ,gib  her'  (ebenso  osk.  ce-bnust  ,er  wird  her- gekommen sein'),  ceterus  ,der  andere,  der  übrige'  (*cÖ  -f  *e^ero-,  vgl.  umbr. etru  ,altero');  hi-c  (*hi-ce)j  Ms-ce^  sl-c  (sz-ci-ne),  illi-c,  illü-c,  tun-c,  nun-c usw.,  osk.  ekak  ,hanc',  ekik  ,hoc'  =  pälign.  eci-c,  marr.  iaf-c  ,eas',  esu-c ,eo';  osk.  idi-k,  umbr.  ere-k  ,id',  osk.  ekas-k  ,hae',  umbr.  esmi-k  ,huic', lat.  ecce  (wohl  aus  *ed-ke,  s.  *e  Pron.-St.),  osk.  um  -um  erweitert  ekk-um ,ebenso',  nach  puz  ,wie'  aus  *k'!^uti-s  umgebildet  ekss  ,ita*;  Konglutinat e-ko-  z.  B.  osk.  ekas  ,hae',  pälign.  ctcw/, hlc',  ecuc  ,huc',  ecic  ,hoc',  *e-Ä;(e)-50- z.  B.  osk.  exac  ,hac* ;
*Si-  in  lat.  eis  , diesseits',  citer  , diesseitig',  citrö  ,hierher',  cito^ä  , diesseits', citimus  ,nächstbefindlich',  umbr.  give  ,citra'  (St.  *ki-uo-)^  gimu,  simo  ,ad citima,  retro';
air.  ce  ,hier,  diesseits'  (*kei,  vgl.  ablautend  Ogom  coi  ,hier',  gall.  y^ovi,), cen  (vgl.  zum  w-Suffix  ahd.  hina  ,weg'  usw.)  , diesseits'  (in  cen-alpande ,cisalpinus')  und  ,ohne',  centar  , diesseits*;  gall.  etic  neben  eti  ,auch'  könnte ebenfalls  -ke  enthalten;
anord.  hänUj  hann  ,er'  (*hänaR,  idg.  *kenos  aus  *lce-eno-s),  hon  ;Sie'; asächs.  he,  he,  hie,  ahd.  he,  her  ,er',  nur  Nom.,  ags.  h^  ds. ;
got.  himma  ,huic',  hina  ,hunc',  hita  n.  ,jetzt',  asächs.  hiu-diga,  ahd. hiu-tu  ,hoc  die,  heute'  (:  asächs.  ho-digo  ds.),  ahd.  hiuru  (*hiu-järu)  , heuer', nhd.  jetzt;  Österr.  hietz(t),  mhd.  (*h)ie-zuo  (aus  *Aiw  +  Postpos.  tö  ,zu'); ahd.  hina  ,weg',  nhd.  hin,  himveg  (vgl.  air.  cen) ;  got.  hiri  ,komm  hierher' (Grundform  unsicher);  ahd.  hera,  as.  her  ,hierher';  got.  her,  ahd.  Mar, ags.  her  ,hier'  (*kei-r)]  got.  hidre  , hierher',  ags.  hider,  engl,  hither  , hierher' ( :  lat.  citer,  citrö),  nl.  heden  , heute',  ahd.  hitumum,  hitamun  ,erst,  demum' (:  lat.  citimus)'^
strittig,  ob  hierher:  got.  hindana  ,hinter,  jenseits',  ags.  asächs.  hindan^ ahd.  hintana  ,hinten',  anord.  handan  ,von  jener  Seite  her,  jenseits',  kompara- tivisch got.  hindary  ahd.  hintar  ,hinter',  superlativisch  got.  hindumists ,hinterster,  äußerster',  ags.  hindema  ,letzter*,  wobei  das  n  von  *ki-n-t-, *lco-n-t  dasselbe  wie  in  ahd.  hina  wäre;  oder  mit   gall.  Cintugnätos  ,Erst-
39
610  9
geborener',  air.  cetne,  cymr.  kyntaf  ,erster'  usw.  zu  *ken-  , frisch  kommen soeben  sich  einstellen,  anfangen'  (oben  S.  564)  mit  der  Bed.  ,letzter' =  ,novissimus' ?
apr.  schis  (Adverb  schal  ,hier^),  lit.  fis  (lett.  sis  =  aksl.  sh  , dieser'),  Gen.  Üt. Ho,  aksl.  sego,  Akk.  PL  aksl.  shj^,  fem.  lit.  B  (lett.  H)  =  aksl.  si,  Akk.  S». f.  shj^,  lit.  B-tas  , dieser'  (^ki-to-),  dazu  staX  ,sieh  hier'  (alt  sitai),  apr. stas  ,der';  lit.  Haüdien,  lett.  Süodien  ,heute',  lit.  s^,  lett.  §e  ,hier',  aksl. si-ch  jTOLOVTog*  usw. ;
hitt.  kl  , dieses',  ki-nun  ,jetzt'  enthält  *Äi  (Pedersen  Hitt.  50).
WP.  I  452  ff.,  WH.  I  192  f.,  208  f.,  222,  390,  644  f.,  855,  862,  Trautmann 304,  Schwyzer  Gr.  Gr.  I  613.
kob-  ,sich  gut  fügen,  passen,  gelingen';  kobo-m  , Erfolg'.
Air.  cob  n.  ,Sieg',  gall.  Ver-cohius,  *Cobo-nertos  >  Cobnertos  MN,  Coh- rünus,  -rünius  MN  (auch  ins  Slav.  gewandert  als  Kobrym,  wovon  der Stadtname  russ.  Kohrywb,  poln.  Kohryn  im  Gouv.  Grodno) ;
ags.  gehcejo  ,passend',  nas.  schwed.  hampa  sig  ,sich  ereignen'  =  norw. he'p'pa  ds.,  heppen  ,glücklich,  günstig',  aisl.  happ  n.  , Glück'  (engl,  hap , Zufall',  to  kappen  ,sich  ereignen',  happy  ,glücklich'  aus  dem  Nord.);
abg.  kobh  f.  ,Tvxr]^  Genius,  Schutzgeist',  ksl.  kobh  ,ola)voa'K07rla,  augurium', russ.  alt  kobh  ,Wahrsagung,  Vorahnung  nach  dem  Vogelflug  oder  Begeg- nung', heute  dial.  , Greuel,  Scheusal',  skr.  köb  ,gute  Vorbedeutung,  Glück- wunsch ;  Vorahnung,  böse  Vorahnung',  usw.
WP.  I  457  f.
koi-,  kui-    Nachahmung    des    Quietschlautes;    einzelsprachliche    Lautnach- ahmungen. Gr.  xot^SLv  ,quieken  wie  ein  Spanferkel',   nhd.  quieken,   quieksen,   quiet- schen, lit.  kvykti,  russ.  kvi^dth  , quieken,  zwitschern,  winseln'  usw. WP.  I  455,  Berneker  656  f.,  Trautmann  147.
koi-lo-  ,kümmerlich,  nackt^;  nur  kelt.  und  halt.
Air.  cöil,  cöel  ,dünn,  schmal',  cymr.  corn.  cid  ,macilentus,  macer'; lett.  kails  ,nackt,  kahl,  bloß',  kaili  laudis  ,Ehepaar  ohne  Kinder'  (könnte auch  zu  kai-  ,allein'  gehören). WP.  I  326,  455,  WH.  I  130.
koi~no-  ,Gras*.
Gr.  TiOLvä'  x^qxoq  Hes.  (vielleicht  Neutr.  PL);  lit.  sienas,  lett.  ^ens  ,Heu* (finn.  Lehnwörter  daraus  bedeuten  ,Heu,  Gras,  Kraut*) ;  aksl.  s^no  .xöqtog', skr.  sijeno  ,HeuS  acech.  s^no  ds.
WP.  I  455,  Mühlenbach-Endzelin  Lett.-D.  Wb.  IH  859,  Trautmann  297.
611
Lat.  cüra  , Sorge',  cürö^  -äre  ,sorgen',  alat.  coiravit  usw.,  päl.  coisatens ,curaverunt',  umbr.  kuratu  ,curato^;
dazu  allenfalls  got.  usliaista  , dürftig'  als  ,vernachlässigt' ? Hierher  vielleicht  die  gall.  PN  Koisis,  Coisa. WP.  I  455,  WH.  I  314,  859.
jco  kOf  kak(k)-f  ku(r)kur-   u.  dgl.   als   Nachahmung   des  Naturlautes  der Hühner;  Worte  ohne  nachweisbare  ältere  Geschichte.
I.  Gr.  y,aycxdßr]  f.,  Kaytytaßig  f.  ,Rebhuhn',  ytax-naßll^siv  vom  Naturlaut  der Rebhühner  (ebenso  das  entlehnte  lat.  cacabäre),  xaxxd^etv  , gackern';
lat.  cacilläre  ,gackern  (von  der  Henne)';
ndd.  kakkeln  ,gackern',  nl.  kokkelen  ,kollern  (vom  Hahn)',  woneben ahd.  gackizön  ,gackern  (von  der  ein  Ei  legenden  Henne)',  nhd.  gackern, dial.  gaggezen,  nhd.   Gockel  (s.  auch  unter  ghegh-).
II.  Lat.  coco  coco  ,Naturlaut  der  Hühner'  (Petron  59,  2),  franz.  coq  ,Hahn', dän.  kok,  schwed.  mdartl.  kokk  ,Hahn',  anord.  (afrz.  Lw.)  kokr,  ags.  cocc, nl.  alt  cocke  ds. ;  aksl.  kokotT>  ,Hahn',  kokoh  ,Henne',  russ.  kokotdth ,gackern'  usw.
```


## [2026-09-06T20:50:53.815Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD ko- ===\" && grep -n -A25 \"^ko-\\. *Stem\\|^ko-\\b\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-06T20:50:53.881Z] TOOL RESULT

```
=== AHD ko- ===
```


## [2026-09-06T20:50:55.026Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ce-tero\\|ketero\\|ke-etero\\|cetero\\|ceterus\" AHD_watkins1985.txt KLN_1966.txt SKT.txt | head -30"
}
```


### [2026-09-06T20:50:55.084Z] TOOL RESULT

```
AHD_watkins1985.txt:642:h. Anglo-Norman aloper, to run away from one’s hus- band with a lover: ELOPE. kneigwh-. To lean on. 1. Latin cdnivére (< *con-niguére; com-, together; see kom), “to lean together” (said of eyelids), to close the eyes, be indulgent: CONNIVE. 2. Suf- fixed zero-grade form *knigvh-to- in Latin nictdre, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.] knid-. Egg of a louse. Suffixed form *knid-d in Germanic *hnito in Old English hnitu, egg of a louse: NIT. [Pok. knid- 608.] ko-. Stem of demonstrative pronoun meaning “this.” I. Variant form *ki-. 1. Germanic *hi- in: a. Old English he, he: HE!; b. Old English him, him: HIM; c. Old English his, his: 1s; d. Old English hire, her: HER; e. Old English Ait, it: 1r. f. Old English hér, here: HERE; g. Old English heonane, heonon, from here: HENCE. 2. Suffixed form “ki-tro- in Germanic *hi-thra- in Old English hider, hither: HITHER. 3. Suffixed form *ki-s in Latin cis, on this side of: cis-. II. Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin céterus (neuter plural cétera), the other part, that which remains: ET CETERA. 2. Latin -ce (see nu-). III. Attrib- uted by some to this root (but more likely of obscure origin) is Germanic root *hind-, behind. 1. Old English bihindan, in the rear, behind (bi, at; see ambhi): BE- HIND, HIND!. 2. Old High German hintar (> German hinter-), behind: HINTERLAND. 3. Germanic derivative verb *hindron, to keep back, in Old English hindrian, to check, hinder: HINDER}. [Pok. ko- 609.] k6-. To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.] kob-. To suit, fit, succeed. Germanic *hap- in Old Norse happ, chance, good luck: HAP, (HAPPEN), (HAPPY); (HAP- LEss), (MISHAP). [Pok. kob- 610.] [kokkos. Kermes berry, pit, grain. Greek noun of un- known origin: COCCID, COCCUS, COCHINEAL; MONO- COQUE.] koksa. Body part. Latin coxa, hip: Coxa, CUISSE, CUSH- ION. [Pok. koksd 611.] kolem-. Grass, reed. Suffixed form *kolsm-o-. 1. Ger- manic “*halmaz in Old English healm, halm, straw: HAULM. 2. Latin cudmus, stalk: CULM!. 3. Zero-grade form “kibpm-o- in Greek kalamos, a reed, straw: CALA- MITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. kolomo-s 612.] koli-. Glue. Suffixed variant form *koly-a in Greek kolla, glue: COLLAGE, COLLO-, COLLODION; PROTOCOL. [Pok. Rolfeji- 612.] kom. Beside, near, by, with. 1. Germanic *ga-, together, with (collective and intensive prefix and marker of the past participle), in Old English ge-, with, also participial, collective, and intensive prefix: ENOUGH, HANDIWORK, YCLEPT. 2. Latin cum, co-, with: CUM; CONQUIAN. 3. Old Latin com, with (collective and intensive prefix): co-, com-. 4, Suffixed form *kom-trd in Latin contra, against, opposite: (CON!), CONTRA-, CONTRARY, (COUNTER!), COUNTER-, COUNTRY; ENCOUNTER. 5. Suffixed form *kom-yo- in Greek koinos, common, shared: COENO-; CENOBITE, EPICENE, KOINE. 6. Reduced form *ko- (see gher-', mei-', smei-). [Pok. kom 612.] konemo-. Shinbone, bone, Reduced form *kemmo- per- haps in Germanic *hamma in Old English hamm, ham, thigh: HAM. [Pok. konamo- 613.] konk-. To hang. 1. Germanic *hanhan in: a. Old English hon, to hang: HANG; b. Dutch (dialectal) hankeren, to long for; HANKER; ¢C. possibly Middle English he(e)ng, hinge, hinge (ultimately from the base of Old English hangian, to hang): HINGE. 2. Suffixed form *konk-t-d- in
```


## [2026-09-06T20:51:04.967Z] TOOL CALL #14: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','IEC','TAD','MON','BQT','WLD']:\n    print('==',k); print(json.dumps(d[k], ensure_ascii=False, indent=1))\n\""
}
```


### [2026-09-06T20:51:07.382Z] TOOL RESULT

```
== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
== IEC
{
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": "",
 "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"
}
== TAD
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
== MON
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
== BQT
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
== WLD
{
 "title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32",
 "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)",
 "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
 ],
 "page_offset": "Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).",
 "lookup_hint": "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.",
 "notes": "Tried IA (several queries), Google Books API (quota exceeded / not full view), HathiTrust (blocks automated access, 403). Band 2 (1927) is US public domain; Band 1 (1930) became US PD in 2026, so HathiTrust full view may exist - check manually at https://catalog.hathitrust.org/Search/Home?lookfor=walde+pokorny+vergleichendes. || UPDATE 2026-09: Bände I and II obtained in full from the Digital Library of India scans on archive.org (open, OCR layer in the _text.pdf).",
 "cites": "volume (WLD1 / WLD2) and page of Walde–Pokorny"
}
```


## [2026-09-06T20:51:15.606Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^he, pers\\.\\|^he,\\|^et cetera\\|^etcetera\\|^hence,\\|^hither,\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T20:51:15.664Z] TOOL RESULT

```
17341:he,  n.,  name  of  the  5th  letter  of  the  Hebrew  al¬ phabet.  —  Heb.  he,  probably  meaning  ‘lattice window’.
```


## [2026-09-06T20:51:16.315Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=360 && NR<=372 {print \"=== leaf \" NR \" ===\"; print substr($0,1,400)}' KLN_1966.txt"
}
```


### [2026-09-06T20:51:18.133Z] TOOL RESULT

```
=== leaf 360 ===
’.  See  gullet,  and  cp.  glutton, deglutition,  ingluvies.
Derivative:  glut,  n.,  a  swallow,  gulp, glut,  tr.  v.,  to  feed  to  satiety;  intr.  v.,  to  eat  to satiety.  —  ME.  glotten,  fr.  OF.  glut,  glout.
664
‘gluttonous’,  back  formation  fr.  glotir,  glutir, ‘to  swallow,  gulp  down’.  Cp.  OF.  glototer,  ‘to eat  greedily’,  freq.  of  glotir,  and  see  gl
=== leaf 361 ===
 without’),  whence  Gk. XijToi;,  ‘want,  need’,  ya-reiv,  ‘to  want,  be  in need  of,  long  for,  desire’,  yff'K,  ‘bereaved  of’, L.  heres,  ‘heir’ ;  see  heredity  and  cp.  chori-.  Cp. ago.
Derivatives:  go,  n.,  that  which  goes,  go-er,  n., go-ing,  n.
goad,  n.  —  ME.  gode,  fr.  OE.  gad,  ‘point,  sting, goad,  arrow’,  rel.  to  Lombard  gaida,  ‘sp
=== leaf 362 ===
er  its inventor.
gomeral,gomerel,n.,a  fool.— Of  unknown  origin, gomphosis,  n.,  an  immovable  union  of  bony  parts in  the  body  (anat.)  —  Medical  L.,  fr.  Gk.  y6|a- 903019,  ‘a  bolting  together’,  fr.  yopupouv,  ‘to fasten  with  bolts’,  fr.  y6pipo9,  ‘bolt’,  which  is cogn.  with  OE.  camb,  ‘comb’.  See  comb  and -osis  and  cp.  agomphious.
Gomphrena, 
=== leaf 363 ===
ives:  gorge,  intr.  and  tr.  v.,  gorg-ed,  adj. gorgeous,  adj.  —  OF.  gorgias,  ‘finely  dressed, luxurious’,  formed  from  the  name  of  Gorgias, a  Greek  sophist  and  rhetorician  (about  483- 375),  who  took  pleasure  in  showing  off  his luxury.
Derivatives:  gorgeous-ly,  ad v.,  gorgeous-ness,  n. gorget,  n.,  a  piece  of  armor  defending  the  throat. —  OF.  gorget
=== leaf 364 ===
eize.  —  Du. grabbelen,  freq.  of  MDu.  grabben.  See  grab, ‘to  seize’,  and  freq.  suff.  -le.
Derivatives:  grabbl-er,  n.,  grabbl-ing,  n. grace,  n.  —  ME.,  fr.  MF.  (=  F.)  grace,  fr.  OF. grace,  fr.  L.  gratia,  ‘favor  shown  to  another, kindness,  loveliness,  charm;  thanks,  thankful¬ ness,  gratitude’,  fr.  grants,  ‘beloved,  pleasing, dear,  agreeable;  
=== leaf 365 ===
tter’, lit.  ‘that  which  is  written’,  from  the  stem  of ypatpEiv,  ‘to  write’.  See  -graph  and  cp.  gramarye, grammatical.
grammarian,  n.,  a  student  of,  or  an  expert  in, grammar.  —  ME.  gramarien,  fr.  OF.  gramarien (F.  grammairien ),  fr.  OF.  gramaire  (F.  gram¬ maire),  ‘grammar’.  See  prec.  word  and  -ian. grammatical,  adj.  —  L.  grammaticdlis,
=== leaf 366 ===
to  the  genus  Grapsus (zool.)  —  Lit.  ‘resembling  a  crab’.  See  Grap- sus  and  -oid.
Grapsus,  n.,  a  genus  of  crabs  (zool.)  —  ModL., fr.  Gk.  Ypa+aio?,  ‘crab’,  which  is  of  uncertain origin;  it  is  prob.  not  connected  with  It.  gra- vosta,  ravosta,  OHG.  krebi 3,  OE.  crabba,  ‘crab’, graptolite,  n.,  a  fossil  zoolite  bearing  markings resembling  w
=== leaf 367 ===
  and  intr.  v., gray-ish,  adj.,  gray-ly,  adv.,  gray-ness,  n. graylag,  greylag,  n.,  the  gray  goose.  —  Short  for gray  lag  goose,  i.e.  ‘the  gray  lagging  goose’  (see lag,  adj.,  and  goose);  so  called  because  it  is  late in  migrating.
grayling,  n.,  a  freshwater  fish.  —  Formed  fr.  gray with  suff.  -ling.
graze,  tr.  and  intr.  v.,  to  feed  on  grass.  
=== leaf 368 ===
nen’,  derives  fr.  L.  linum  (see linen).
gridiron,  n.  —  ME.  gredirne,  gridirne,  folk- etymological  variants  of  ME.  gredire,  gridire (due  to  a  confusion  of  the  ending  -ire  with  ME. iren,  ‘iron’).  ME.  gredire,  gridire  are  altered  fr. ME.  gredil,  gridell,  ‘griddle’.  See  griddle  and cp.  andiron.
grief,  n.  —  ME.  grief,  gref  greve,  fr.  OF.  gri
=== leaf 369 ===
  MLG.  gristel,  and  to  OE.  grost, MHG.  gruschel,  ‘cartilage’,  and  prob.  also  to OE.  grist,  ‘grinding’.  See  1st  grist.
Derivatives:  gristl-y,  adj.,  gristl-i-ness,  n.
grit,  n.,  coarse  sand,  gravel.  —  ME.  grete,  fr.  OE. greot,  ‘grit,  sand,  dust,  gravel’,  rel.  to  OS.  gnot, OFris.  grit,  ON.  grjot,  ‘rock,  stone’,  OHG. grio3,  MHG.  grie$,  gru
=== leaf 370 ===
  grumble.  —  Prob.  of  imitative origin;  cp.  Gk.  ypu,  ‘a  grunt’,  YP^£tv>  ‘t0 grunt,  grumble’,  L.  grundire,  grunnire,  OE. grunian,  ‘to  grunt’,  which  all  are  of  imitative origin.  Cp.  grunt.  Cp.  also  grouch,  grudge, grutch. Derivative:  grous-er,  n.
grout,  intr.  and  tr.  v.,  to  dig  with  the  snout.  — Of  uncertain  origin.  Cp.  rout,  ‘to  dig 
=== leaf 371 ===
rig.  a  nickname  meaning ‘whelp,  cub’.  See  whelp.
Derivative:  Guelph-ic,  Guelf -ic,  adj.
Guendolen,  fem.  PN.  —  A  var.  of  Gwendolin(q.v.) guenon,  n.,  any  of  a  genus  of  long-tailed  African monkeys.  —  F.,  ‘she-monkey,  monkey’,  of  un¬ certain  origin.
guepard,  n.,  the  cheetah.  —  F.  guepard,  fr.  earlier gapard,  shortened  fr.  It.  gattopardo,  lit. 
=== leaf 372 ===
�,  and  suff.  -ible.
Derivative:  gullibil-ity,  n. gully,  n.,  a  small  ravine.  —  Altered  fr.  gullet. Derivative :  gully,  tr.  v.
gulosity,  n,,  gluttony  (rare).  —  Late  L.  gulositas, fr.  L.  gulosus,  ‘gluttonous’,  fr.  gula.  See  gullet, adj.  suff.  -ose  and  suff.  -ity. gulp,  tr.  and  intr.  v.  —  ME.  gulpen,  golpen,  glub- ben,  of  imitative  origin.  Cp
```


## [2026-09-06T20:51:24.302Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 545 710 735; do echo \"=== printed $p ===\"; grep -n \"^ *$p *$\" KLN_1966.txt | head -3; done"
}
```


### [2026-09-06T20:51:26.441Z] TOOL RESULT

```
=== printed 545 ===
=== printed 710 ===
17339:710
=== printed 735 ===
17900:735
```


## [2026-09-06T20:51:28.752Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### around p710\" && sed -n '17300,17400p' KLN_1966.txt"
}
```


### [2026-09-06T20:51:28.811Z] TOOL RESULT

```
<persisted-output>
Output too large (32.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bqeyk4ec3.txt

Preview (first 2KB):
### around p710
Derivatives:  haughti-ly,  adv.,  haughti-ness,  n. haul,  tr.  and  intr.  v.  —  ME.  halien,  halen,  haulen, fr.  OF.  (=  F.)  haler,  ‘to  pull,  draw,  haul’,  fr. ODu.  (=  Du.)  halen,  which  is  rel.  to  OS.  halon, ON.  hala,  OFris.  halia,  OHG.  halon,  holon, MHG.  haln,  holn,  holen,  G.  holen,  ‘to  draw, haul;  to  fetch’,  OE.  geholian,  ‘to  obtain’.  These Teut.  words  possibly  derive  from  an  I.-E.  base *kal~,  ‘to  draw,  puli’,  whence  also  Gk.  xaXo i?, ‘rope’.  Cp.  hale,  ‘to  haul’,  the  first  element  in halyard,  and  the  second  element  in  keelhaul. Derivatives:  haul,  n.,  haul-age,  n.,  haul-er,  n. haulm,  halm,  n.,  stalk.  —  ME.  halm,  fr.  OE. healm,  ‘straw,  stem  of  grass’,  rel.  to  OS.,  Dan., Swed.,  Du.,  OHG.,  MHG.,  G.  halm,  ON. halmr,  and  cogn.  with  L.  culmus,  ‘stalk,  stem', Gk.  xaXap.o?,  ‘reed’.  See  culm  and  cp.  words there  referred  to.  Cp.  also  the  second  element  in marram.
haunch,  n.,  hip.  —  Earlier  hunch,  fr.  ME.  hanche, haunche,  fr.  OF.  (=  F.)  hanche,  fr.  Teut. *hanka;  cp.  MDu.  hanke,  ‘haunch’.
Derivatives:  haunch-ed,  adj.,  hauneh-ing,  n. haunt,  tr.  v.,  to  visit,  frequent.  —  ME.  haunten, fr.  OF.  (=  F.)  hauler,  which  is  of  Teut.  origin. Cp.  ON.  heimta,  ‘to  bring  home,  fetch’,  which derives  fr.  heimr,  ‘homeland’,  and  OE.  hamettan, ‘to  shelter’,  which  comes  fr.  ham,  ‘home’,  and see  home.  Cp.  hamlet.
Derivatives:  haunt,  n.,  haunt-ed,  adj.,  haunt-er, n.,  haunt-ing,  n.  and  adj.,  haunt-ing-ly,  adv. haurient,  also  hauriant,  adj.,  with  the  head  in chief;  said  of  a  fish  (her.)  —  L.  hauriens,  gen. -entis,  pres.  part,  of  haurtre,  ‘to  draw  out (water),  to  drain,  breathe’.  See  exhaust  and  -ent and  cp.  haustellum,  haustorium. hausen,  n„  a  large  kind  of  sturgeon.  —  G.,  ‘stur¬ geon’,  fr.  MHG.  huse(n),  fr.  OHG.  huso.  See huso.
...
</persisted-output>
```


## [2026-09-06T20:51:32.069Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=17339 && NR<=17400' KLN_1966.txt | grep -n \"^he,\\|^he\\b\\|^her,\\|^here,\\|^hence,\\|^him,\\|^his,\" "
}
```


### [2026-09-06T20:51:33.968Z] TOOL RESULT

```
3:he,  n.,  name  of  the  5th  letter  of  the  Hebrew  al¬ phabet.  —  Heb.  he,  probably  meaning  ‘lattice window’.
```


## [2026-09-06T20:51:36.158Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=17335 && NR<=17370' KLN_1966.txt | cut -c1-1200"
}
```


### [2026-09-06T20:51:37.654Z] TOOL RESULT

```
haze,  tr.  v.,  to  harass.  —  OF.  haser,  ‘to  vex,  irri¬ tate’,  of  unknown  origin, hazel,  n.  —  ME.  hasel,  fr.  OE.  hxsel,  hxsl,  rel. to  ON.,  Norw.  hast,  Dan.,  Swed.  hassel,  MLG., MDu.  hasel,  Du.  hazelaar,  OHG.  hasal,  MF1G., G.  hasel,  ‘hazel’,  and  cogn.  with  L.  corulus, corylus  (for  *kozulus),  ‘hazel,  filbert  tree’,  OIr., OCo.,  W.,  Bret,  coll  (for  *coslo-),  ‘hazel’,  perh. also  with  OLith.  kasulas,  ‘a  hunting  spear’  (so called  because  it  was  usually  made  of  hazel wood).  Cp.  Corylus.
Derivatives:  hazel,  hazel-ed,  hazel-ly,  adjs. hazing,  n.,  the  act  of  harassing.  —  Formed  fr. haze,  ‘to  harass’,  with  -ing,  suff.  forming  verbal nouns.
hazy,  adj.,  characterized  by  haze.  —  Of  unknown origin.  Cp.  haze,  ‘fog’.
Derivatives:  hazi-ly,  adv.,  hazi-ness,  n. hazzan,  chazzan,  also  spelled  hazan,  chazan,  n., Jewish  cantor.  —  Mishnaic  Heb.  and  Aram. hazzdn ,  ‘superintendent,  officer’,  later  ‘cantor’, prob.  borrowed  fr.  Akkad,  hazanu,  hazannu, ‘chief  magistrate  of  a  town’  (cp.  Aram,  hazzand malhd,  ‘superintendents  of  the  town’,  Talmud Babha  Metzi'a,  93 b).  It  is  very  probable,  how¬ ever,  that  Akkad,  hazanu  was  borrowed  from  a WSem.  language  and  that  the  word  orig.  meant ‘overseer’,  from  a  verb  meaning  ‘to  see’;  cp. Heb.  hazdh,  Aram,  hazd,  ‘he  saw’.  (In  Akkadian, the  verb  hazd,  ‘to  see’,  does  not  occur;  if  it  had existed,  hazanu  might  be  its  derivative.)  If  Ak¬ kad.  hazanu  is  a  WSem.  loan  word,  then  Heb. and  Aram,  hazzdn  were  reborrowed  from  Ak¬ kadian.  See  Heinrich  Zimmern,  Akkadische Fremdworter  als  Beweis  fur  babylonischen KultureinfluB,  Leipzig,  1917,  p.6,  Note  3. he,  nom.  sing,  of  the  3rd  pers.  masc.  pron.  — ME.  he,  fr.  OE.  he  [fern,  heo,  hio,  neut.  hit;  pi. (for  all  genders)  hi,  hie],  rel.  to  OS.,  OFris.  he, hi,  
710
I.-E.  base  *ki-,  ‘this  one’,  whence  also  Hitt,  ki, ‘this’,  Gk.  k-y.ci,  ‘there’,  Ion.  Gk.  xeT-vo;, Aeol.  xTj-voi;,  Gk.  i-y.cT.-voc,  ‘that  person  or thing’,  <rf|-fx£pov,  ‘today’  (for  *>a£pepov,  lit. ‘this  day’,  fr.  I.-E.  *kyo-,  ‘this’,  and  Gk.  zjpipa, ‘day’),  L.  cis,  citer,  citra,  ‘on  this  side’,  ce-  and -ce,  emphatic  particles  meaning  ‘here,  there’, OSIav.  si,  Lith.  sis,  ‘this’.  Cp.  him,  her,  it,  hence, here,  hither.  Cp.  also  cede,  cis-,  citra-,  cy-pres, et  cetera,  hodiernal,  sic.
he,  n.,  name  of  the  5th  letter  of  the  Hebrew  al¬ phabet.  —  Heb.  he,  probably  meaning  ‘lattice window’.
head,  n.  —  ME.  heved,  hed,  fr.  OE.  heafod,  rel. to  OS.  hot) id,  ON.  hofud,  Dan.  hoved,  Swed. huvud,  OFris.  haved,  hafd,  MDu.  ho  vet,  hooft, Du.  hoofd,  OHG.  houbit,  houpit,  MHG.  houbet, houbt,  houpt,  G.  Haupt,  Goth,  haubip,  ‘head’, and  cogn.  with  OI.  kaput-,  ‘head’  (in  kapuccha- lam,  ‘hair  of  the  hind  part  of  the  head’),  L. caput,  ‘head’.  See  capital,  adj.
Derivatives:  head,  v.,  head-ed,  adj.,  head-er,  n., head-ing,  n.,  head-y,  adj.,  head-i-ly,  adv.,  head- i-ness,  n.
-head,  a  rare  collateral  form  of  suff.  -hood, headless,  adj.  —  ME,  hevedles,  hedles,  fr.  OE. heafodleas.  See  head  and  -less, headlong,  adv.  —  ME.  hedling,  formed  with  adv. suff.  -ling  fr.  hed,  ‘head’;  see  head.  The  form headlong  (for  *headling)  is  due  to  folk-etymolog¬ ical  association  with  -long  (cp.  sidelong). headman,  n.  —  ME.  hevedman,  hedman,  fr.  OE. heafodman,  fr.  heafod,  ‘head’,  and  man,  ‘man’. See  head  and  man  and  cp.  ON.  hofudsmadr, Swed.  huvudman,  OHG.  houbitman,  MHG. houbetman ,  ‘headman,  leader,  chief’,  G.  Haupt¬ mann,  ‘captain’.  Cp.  also  hetman, heal,  tr.  and  intr.  v.  —  ME.  helen,  fr.  OE.  hxlan, rel.  to  OS.  helian,  ON.  heila,  OFris.  hela,  Du. heelen,  OHG.,  MHG.,  G.  heilen,  Goth,  ga-hail- jan,  ‘to  heal'.  These  verbs  lit.  mean  ‘to  make whole’,  and  are  denominated  fr.  OE.  hal,  ‘whole’, resp.  its  equivalents  in  the  other  Teut.  lan¬ guages.  See  whole  and  cp.  hale,  ‘healthy’. Derivatives:  heal-er,  n.,  heal-ing,  n.  and  adj., heal-ing-ly,  adv.
heald,  n.,  a  heddle.  —  ME.  helde,  fr.  OE.  hefeld. See  heddle.
health,  n.  —  ME.  helthe,  fr.  OE.  hxld,  lit.  ‘whole¬ ness’,  formed  fr.  hal,  ‘whole’,  with  suff.  -d.  See heal  and  substantial  suff.  -th.  For  sense  de¬ velopment  cp.  Heb.  shaldm,  ‘completeness, wholeness,  health,  peace’,  fr.  shaldm,  ‘was  com¬ plete,  was  safe’.
Derivatives:  health-ful,  adj.,  health- ful-ly,  adv,, health-ful-ness,  n,,  health-y,  adj.,  health-i-ly,  adv., health-i-ness,  n.
heap,  n.  —  ME.  heap,  heep,  hepe,  ‘troop,  heap’, fr.  OE.  heap,  ‘troop,  band,  multitude’,  rel.  to OS.  hop,  MLG.  hupe,  Du.  hoop,  OHG.  hiifo, houf,  MHG.  hiife,  houfe,  G.  Haufe,  ‘heap’,  fr. I.-E.  base  *qeu-p-,  ‘to  bend,  arch,  vault’,  whence
711
also  OSIav.  kupu,  Lith.  kaupas,  ‘heap’,  kupra, ‘hump’.  See  cup  and  cp.  hive  and  hope,  ‘troop’. Cp.  also  howitzer,  Skupshtina, heap,  tr.  and  intr.  v.  —  ME.  hepen,  fr.  OE.  hea- pian,  ‘to  heap’,  fr.  heap.  See  heap,  n. Derivative:  heap-er,  n.
hear,  tr.  and  intr.  v.  —  ME.  heren,  fr.  OE.  hieran, hyran,  heron,  rel.  to  ON.  heyra,  Swed.  hdra, Dan.  here,  OS.  horian,  OFris.  hera,  hora,  Du. horen,  OHG.  horan,  horren,  MHG.  haren,  G. horen,  Goth,  hausjan,  fr.  I.-E.  base  *(s)qeu-, *{s)qeu-,  ‘to  look  at,  observe,  perceive’,  whence also  OI.  kavlh,  ‘wise’,  Gk.  jtoeiv,  ‘to  mark,  per¬ ceive,  hear’,  and  prob.  also  axouetv  (with  copul. pref.  a-),  ‘to  hear’.  See  show  and  cp.  hark,  hear¬ ken.  Cp.  also  acoustic.
Derivatives:  hear-er,  n.,  hear-ing,  n. heard,  past  tense  and  pp.  of  hear.  —  ME.  herde, fr.  OE.  herde,  fr.  heron,  ‘to  hear’.  See  hear, hearken,  intr.  and  tr.  v.  (the  latter  is  archaic).  — ME.  herknien,  herknen,  fr.  OE.  heorcnian, hyrcnian,  rel.  to  OFris.  harkia,  herkia  and  to E.  hark  (q.v.)
Derivative:  hearken-er,  n. hearse,  n.  —  ME.  herce,  herse,  fr.  MF.  herce (F.  herse),  ‘harrow;  portcullis;  triangular  frame for  holding  candles’,  fr.  L.  hirpicem,  acc.  of hirpex,  ‘harrow’,  fr.  Samnite  hirpus,  ‘wolf’; so  called  in  allusion  to  the  teeth  of  the  harrow, which  resemble  the  teeth  of  a  wolf.  Samnite hir-pus  is  rel.  to  L.  hir-cus,  ‘he-goat’.  Both  these words  are  prob.  rel.  to  L.  hir-sutus,  ‘shaggy, prickly,  bristly’.  See  hirsute  and  cp,  rehearse. Derivative:  hearse,  tr.  v.
heart,  n.  —  ME.  herte,  hert,  fr.  OE.  heorte,  rel. to  OS.  herta,  ON.  hjarta,  OFris.  herte,  hirte, ODu.  herta,  Du.  hart,  OHG.  herza,  MHG. herze,  G.  Herz,  Goth,  halrto,  ‘heart’,  and  cogn. with  Hitt,  kardiash  (gen.),  ‘of  the  heart’,  Arm. sir!  (for  *kerdi-),  Gk.  xapSta,  poet.  >a)p,  L.  cor (gen.  cordis),  OSIav.  srudice,  Russ,  serdce, ‘heart’,  Lith.  Sirdis,  ‘heart’,  OPruss.  seyr  (for *kerd),  acc.  siran,  OIr.  cride,  Ir.  croidhe,  ‘heart’, W.  craidd,  ‘heart;  center’,  Bret,  kreiz,  ‘middle’, OSIav.  sridd,  Russ,  seredd,  ‘middle’,  Avestic zlrl6aya-,  ‘middle’.  For  sense  development  cp. Heb.  lebh,  ‘heart’,  and  lebh  yam,  ‘the  midst  (lit. the  heart)  of  the  sea’,  lebh  ha'eli <*,  ‘the  midst of  the  terebinth’,  Akkad,  libbu,  ‘heart;  middle’. Cp.  cordate,  cordial,  core,  accord,  accordion, codling,  ‘a  variety  of  apple’,  courage,  concord, discord,  misericord,  record.  Cp.  also  cardiac, cardio-,  carditis,  endocardium,  epicardium,  peri¬ cardium.  L.  credere,  ‘to  believe’,  is  not  related to  L.  cor,  ‘heart’  (see  cree
Derivatives:  heart,  tr.  and  intr.  v.,  heart-ed,  adj., heart-ed-ly,  adv.,  heart-en,  tr.  and  intr.  v.,  heart- en-er,  n.,  heart-y,  adj.,  heart-i-ly,  adv.,  heart-i- ness,  n.,  heart-less,  adj.,  heart-less-ly,  adv.,  heart- less-ness,  n.
hearth,  n.  —  ME.  berth,  fr.  OE.  heord,  rel.  to  OS., OFris.  herth,  MDu.  hert,  Du.  hoard,  OHG.
herd,  MHG.  hert,  G.  Herd,  ‘hearth’,  fr.  Teut. base  *her-,  corresponding  to  I.-E.  base  *ker-, ‘to  singe,  bum,  glow’,  whence  also  Goth,  hauri, ‘coal’,  ON.  hyrr,  ‘fire’,  OI.  kudayati,  kulayati, ‘singes’,  OSIav.  kurjq,  kuriti  s^,  ‘to  smoke’, Lith.  kuriii,  kiirti,  Lett,  kuru,  kurt,  ‘to  heat’, Lith.  kdrStas,  ‘hot’,  katstis,  ‘heat’,  Lett,  karsts, ‘hot’,  kafst,  ‘to  grow  hot’,  and  prob.  also  L. carbo,  ‘coal,  charcoal’ ;  see  carbon.  Cp.  cremate, heat,  n.  —  ME.  hete,  Fr.  OE.  hxtu,  hxto,  rel.  to OS.  hittia,  ON.  hiti,  Dan.  hede,  Swed.  hetta, OFris.  hete,  Du.  hitte,  OHG.  hizzea,  hizza, heizi,  MHG.,  G.  hitze,  ‘heat’,  OE.  hxda,  ‘hot weather’,  Goth,  heito,  ‘fever’,  and  to  OE.  hat, etc.,  ‘hot’,  see  hot.  It.  izza,  ‘wrath,  anger’,  is  a Teut.  loan  word.
heat,  tr.  and  intr.  v.  —  ME.  heten,  fr.  OE.  hxtan, ‘to  heat’,  fr.  hxtu,  ‘heat’.  See  heat,  n. Derivatives:  heat-ed,  adj.,  heat-ed-ly,  adv.,  heat¬ er,  n.,  heat-ing,  n.
heath,  n.  —  ME.  heth,  fr.  OE.  hied,  ‘heath  (land); heath  (the  plant),  heather’,  rel.  to  OS.  hetha, ON.  heidr,  Dan.  hede,  Swed.  hed,  ‘heath’,  OHG. heida,  ‘heather’,  MHG.,  G.,  Du.  heide,  ‘heath; heather’,  Goth,  haipi,  ‘field’,  and  cogn.  with Gaulish  ceto-  in  Gaulish-Latin  place  names  like Cetobriga,  etc.,  and  with  OIr.  dad,  OW.  colt, W.  coed,  OCo.  cuit,  Bret,  coet  (for  *kaito-), ‘wood,  forest’,  but  L.  bucetum,  ‘cow  pasture’, is  not  cognate.  Cp.  heathen,  heather. Derivative:  heath-y,  adj.
heathen,  n.  —  ME.  hethen,  fr.  OE.  hxden,  adj. and  n.,  rel.  to  OS.  hethin,  adj.,  ON.  heidinn,  adj., OFris.  hethen,  adj.,  MDu.  heidijn,  heiden,  Du. heiden,  n.,  OHG.  heidan,  MHG.  heiden,  adj., OHG.  heidano,  MHG.  heiden,  G.  Heide,  n., ‘heathen’,  Goth,  haipnd,  ‘heathen  woman’. These  words  prob.  meant  orig.  ‘dwelling  on  the heath’.  See  prec.  word  and  cp.  hoyden. Derivatives:  heathen,  adj.,  heathenish  (q.v.), heathenism,  heathenize,  heathenry  (qq.v.) heathendom,  n.  —  ME.,  fr.  OE.  hxdendom,  ‘pa¬ ganism’,  fr.  hxden.  See  prec.  word  and  -dom. heathenesse,  n.,  heathenism  {archaic).  —  ME. hethenesse,  fr.  OE.  hidennes,  lit.  ‘heathenness’. See  heathen  and  -ness.
heathenish,  adj.  —  OE.  hxdenisc,  rel.  to  OHG. heidanisc,  G.  heidnisch,  ‘heathenish’.  See  heathen and  adj.  suff.  -ish.
Derivatives:  heathenish-ly,  adv.,  heathenish¬ ness,  n.
heathenism,  n.  —  A  hybrid  coined  fr.  heathen  and -ism,  a  suff.  of  Greek  origin, heathenize,  tr.  v.,  to  render  heathen;  intr.  v.,  to become  heathen.  —  A  hybrid  coined  fr.  heathen and  -ize,  a  suff.  of  Greek  origin, heathenry,  n.  —  A  hybrid  coined  fr.  heathen  and -ry,  a  suff.  of  L.-F.  origin, heather,  n.,  a  plant  of  the  heath  family.  —  ME. hather,  hadder,  possibly  derived  fr.  heth,  ‘heath, heather’.  See  heath.
Derivative:  heather-y,  adj.
heaume
hederaceous
heaume,  n„  a  kind  of  large  helmet.  —  F.,  fr.  OF. helme,  fr.  Frankish  *helm,  which  is  rel.  to  OHG. helm.  See  helmet.
heave,  tr.  and  intr.  v.  —  ME.  hebben,  heven,  fr. OE.  hebban,  ‘to  lift,  raise’,  rel.  to  OS.  hebbian, ON.  hefja,  Du.  heffen,  OHG.  heffan,  MHG. heben,  heven,  G.  heben,  Goth,  hafjan,  ‘to  lift, raise’,  and  to  OE.  habban,  etc.,  ‘to  hold,  pos¬ sess,  have’.  See  have  and  cp.  heavy.  Cp.  also heddle.
Derivatives:  heave,  n.,  heav-er,  n. heaven,  n,  —  ME.  heovene,  hevene,  heven,  fr.  OE. heofon,  hefon,  rel.  to  OS.  helkm,  LG.  heben, heven,  ON.  himirn,  Goth,  himins,  OS.,  OHG. himil,  OFris.  himel,  himul,  MDu.,  Du.  hemel, MHG.  himel,  G.  Himmel,  ‘heaven,  sky’.  These words  prob.  derive  fr.  Teut.  base  *hama(n)-,  fr. I.-E.  base  *kem-,  *kam-,  ‘to  cover’.  See  chemise and  cp.  words  there  referred  to.
Derivatives:  heaven,  tr.  v.,  heaven-ish,  adj., heaven-ish-Iy,  adv.,  heavenly  (q.v.) heavenly,  adj.  —  ME.  hevenly,  fr.  OE.  heofonlic. See  prec.  word  and  adj.  sufF.  -ly.
```


## [2026-09-06T20:51:43.763Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=17880 && NR<=17915' KLN_1966.txt | cut -c1-2500"
}
```


### [2026-09-06T20:51:45.398Z] TOOL RESULT

```
Derivatives:  hit,  n..  hitt-er,  n. hitch,  tr.  and  intr.  v.,  to  move  by  jerks.  —  ME. hytehen,  ‘to  move,  remove’,  rel.  to  dial.  E.  hike, ‘to  move  with  a  jerk’,  Scot,  hitch,  ‘a  motion  by jerks’.  Cp.  hike.
Derivatives:  hitch ,  n.,  hitch-er,  n.,  hitch-y,  adj., hitch-i-ly,  adv.,  hitch-i-ness,  n. hithe,  n.,  landing  place,  port  (archaic  or  in  place names).  —  ME.  hvthe,  fr.  OE.  hyth,  ‘landing place',  rel.  to  OS.  hath,  of  s.m. hither,  adv.  —  ME.  hider,  hither ,  fr.  OE.  hider, rel.  to  ON.  hedra  (for  *hidra),  ‘here’,  Goth. hidre,  ‘hither’;  formed  from  the  Teut.  demon¬ strative  base  *hi-  (whence  also  he,  here)  with the  comparative  suflf.  -ther.  Cp.  thither.  Cp.  also cis-,  citra-.
Derivative:  hither,  adj.
hitherward,  also  hitherwards,  adv.  —  OE.  hider- weard.  See  hither  and  -ward,  resp.  -wards. Hittite,  n.  —  Formed  with  subst.  suff.  -ite  fr.
Heb.  Hint,  ‘Hittite’  (pi.  Hittim),  fr.  Hitt.  Hatti, hive,  n.  —  ME.  hive ,  fr.  OE.  hyf  rel.  to  ON. hufr,  ‘hull  of  a  ship’,  and  cogn.  with  Of.  kQpah, ‘hollow,  pit,  cave’,  Gk.  v.'yrrr,,  ‘a  kind  of  ship’, xutts'aaov,  ‘cup’,  L.  cupa ,  ‘tub,  cask,  vat’.  See cup  and  cp.  words  there  referred  to.
Derivative:  hive,  tr.  and  intr.  v. hives,  n.,  any  of  various  eruptive  skin  diseases.  — Of  uncertain  origin.
Hivite,  n.,  one  of  an  ancient  tribe  of  Canaan  dis¬ possessed  by  the  Israelites.  —  Formed  with subst.  suff.  -ite  fr.  Heb.  Hiwwf,  lit.  ‘villager’,  fr.
734
hawwdh ,  ‘tent-village,  village’,  which  prob.  de¬ rives  fr.  base  h-w-h,  ‘to  gather’,  and  is  rel.  to Arab,  hawa,  ‘he  collected,  gathered’,  hiwa\ ‘circle  of  tents’.
ho,  interj.  —  Imitative.  Cp.  whoa, hoaetzin,  n.  —  See  hoatzin. hoar,  adj.  —  ME,  har,  hor,  fr.  OE.  hdr,  ‘gray, gray-haired,  old’,  rel.  to  ON.  hdrr ,  of  s.m.,  OS., OHG.  her,  ‘distinguished,  noble,  glorious,  ex¬ cellent’,  MHG.  her,  ‘distinguished,  noble, proud,  gay,  holy’,  G.  hehr,  ‘exalted,  august, noble,  sublime’,  Herr,  ‘lord,  master’,  herrlich, ‘glorious,  excellent’,  fr,  Teut.  base  *haira,  cor¬ responding  to  T.-E.  *koiro-\  cp.  Mir.  cfar, ‘dark’, fr.  base  *keiro-,  a  vowel-gradation  form  of *koiro-.  Cp.  Herr,  herring,  and  the  second  ele¬ ment  in  mynheer,  younkcr.  Cp.  also  hue. Derivatives:  hoar,  n.,  and  intr.  and  tr.  v.,  hoar-y, adj.,  hoar-i-ness,  n.
hoard,  n.  —  ME.  hord,  fr.  OE.  hord,  rel.  to  OS. hord ,  ON.  hodd,  OHG.,  MHG.,  G.  hort ,  Goth. huzd,  ‘treasure’,  lit.  ‘hidden  treasure’,  fr.  I.-E. *quz-dho-.  The  first  element  in  this  base  means ‘hidden’;  see  hide,  ‘to  conceal’,  and  cp.  words there  referred  to.  The  second  element  in  *quz- dho-  means  ‘placed’,  fr.  base  *dhe-,  *dho-,  ‘to place’,  whence  also  Gk.  -ctffcvai,  ‘to  place’, OE.  don,  ‘to  do’.  See  do  and  cp.  theme.  Cp,  also treasure.
hoard,  tr.  and  intr.  v.  —  ME.  horden,  fr.  OE. hordian,  fr.  hord.  See  hoard,  n.
Derivatives:  hoard-er,  n.,  hoarding  (q.v.) hoarding,  n.,  the  act  of  one  who  hoards.  — Formed  fr.  hoard,  \.,  with  -ing,  suff.  forming verbal  nouns.
hoarding,  n.,  a  temporary  fence.  —  Formed  with subst.  suff.  -ing  fr.  obsol.  E.  hoard,  fr.  OF. hourd,  hourt,  hort,  ‘scaffold',  which  is  of  Teut. origin.  Cp.  OHG.  hurd,  ‘hurdle’,  and  see
hurdle.
hoarhound,  n.  —  See  horehound. hoarse,  adj.  —  ME.  hors,  fr.  earlier  has,  fr.  OE. has,  rel.  to  OS.  hes,  ON.  hdss,  Dan.  hies,  Swed, hes,  Du.  hees,  OHG.  heisi,  heis,  MHG.  heise, heiser,  earlier  G.  heisch,  G.  heiser,  ‘hoarse’. These  words  prob.  meant  orig.  ‘dried  out; rough’,  and  are  rel.  to  OE.  hat ,  etc.,  ‘hot’;  see hot.  The  insertion  of  the  r  in  ME.  hors  is  prob. due  to  the  influence  of  harsh.
Derivatives:  hoarse-ly,  adv.,  hoarse-ness,  n. hoatzin,  hoaetzin,  n.,  a  bird  of  S.  America.  —  Sp., fr.  Nahuatl  uatzin.
hoax,  n.  and  tr.  v.  —  Fr.  earlier  hocus.  See  hocus- pocus.
Derivative:  hoax-er,  n.
hob,  n.,  i)  a  rustic;  a  clownish  lout :  2)  a  fairy.  — Fr.  Hob,  a  pet  form  of  Robin.  Cp.  hobgoblin, hob,  n.,  projection  at  the  side  of  a  fireplace;  peg. —  Of  uncertain  origin.  Cp.  hub. hobble,  intr.  v.,  to  go  haltingly,  to  limp;  tr.  v., to  cause  to  go  haltingly.  —  ME.  hobelen;  rel. to  Du.  hubbelen,  ‘to  rock  from  side  to  side’.
735
freq.  of  hobben,  ‘to  toss,  to  rock’.  Cp.  hopple and  hobby,  ‘a  small  species  of  falcon’. Derivatives:  hobble,  n.,  hobbler  (q.v.),  hobbl- ing-ly,  adv.
hobbledehoy,  also  hobbadehoy,  hobbedehoy,  n., a  clumsy  youth.  —  Of  uncertain  origin, hobbler,  n.,  one  who,  or  that  which,  hobbles.  — Formed  from  the  verb  hobble  with  agential suff.  -er.
hobbler,  n.,  a  retainer  who  maintained  a  horse for  military  service  (Engl,  hist.)  —  ME.  hobler, hobeler,  a  blend  of  OF.  hobin,  hobi,  ‘a  small horse’  (see  hobby,  ‘a  nag’),  and  OF.  hobeler, ‘to  skirmish’,  fr.  OF.  hober,  ‘to  bestir  oneself; shake,  agitate’,  which  is  of  Teut.  origin.  Cp. Du.  hobben,  ‘to  toss’,  and  see  hobble, hobby,  n.,  a  small  species  of  falcon.  —  ME.  hobi, hoby,  fr.  OF.  hobet,  dimin.  of  hobe,  ‘falcon’ (whence  also  F.  hobereau,  ‘hobby;  squireen’), fr.  OF.  hober,  ‘to  bestir  oneself’.  See  prec.  word, hobby,  n.,  1)  a  nag;  2)  hobby  horse;  3)  favorite occupation.  —  ME.  hobin,  ‘nag’,  fr.  OF.  hobin, hobi,  ‘a  small  horse’,  orig.  ‘the  ambling  animal’, fr.  OF.  hober,  ‘to  bestir  oneself’.  See  hobby, ‘a  species  of  falcon’,  and  cp.  aubin. hobgoblin,  n.,  i  t  (cap.)  Robin  Goodfellow;  2)  an elf,  goblin ;  3)  a  bogey.  —  Compounded  of  hob, ‘a  kind  of  fairy’,  and  goblin, hobnail,  n.  —  Compounded  of  hob,  ‘fairy’,  and nail.
Derivative:  hobnail-ed,  adj. hobnob,  intr.  v.,  to  be  on  intimate  terms.  —  A var.  of  early  ModE.  hab  nab,  fr.  OE.  habban, ‘to  have’,  and  nabban,  contraction  of  ne  habban, ‘not  to  have’.  Hence  hobnob  orig.  meant  ‘have or  have  not’.  See  have.
hobo,  n.,  a  tramp  ( American  Slang).  —  Of  un¬ known  origin.
hobson-jobson,  n.,  a  festal  excitement.  —  Cor¬ ruption  of  Arab,  ya  Hasan !  ya  Husayn  I  ‘O Hasan!  O  Husain!’,  cry  of  the  Mohammedans at  the  procession  of  the  Moharram.  See  Yule and  Burnell,  Hobson-Jobson,  p.  419.
Hobson's  choice,  n.  —  So  called  after  Thomas Hobson  (died  in  1631),  who  had  livery  stables  at Cambridge  and  let  out  horses  to  customers  on the  condition  that  they  had  to  take  the  animal standing  in  the  stable  nearest  to  the  stable  door, hock,  n.,  the  joint  in  the  hind  leg  of  a  horse.  — ME.  hough,  hoch,  fr.  OE.  hoh,  ‘heel’,  rel.  to  the first  element  in  ON.  ha-sin,  OE.  hoh-sinu,  ‘hock sinew’,  OHG.  hahsa,  MHG.  hahse,  G.  Hachse, ‘hock’,  ON.  hzll,  OE.  hsela,  ‘heel’,  and  cogn. with  OI.  kaksah,  kakfd,  Avestic  kasha,  ‘armpit’, L.  coxa,  ‘hip’,  Lith.  k'mka,  kenkle,  ‘knee  joint’, cinksla,  ‘knee  sinew’,  OIr.  coss,  ‘foot’.  Cp.  bough. Cp.  also  heel.  Cp.  also  coxa.  For  the  second element  in  ON.  hd-sin,  OE.  hoh-sinu,  see  sinew. Derivative:  hock,  tr.  v.,  to  hamstring, hock,  n.,  white  Rhenish  wine.  —  Orig.  ‘wine  of Hochheim’,  abbreviation  of  obsol.  hockamore, ‘wine  of  Hochheim’,  fr.  G.  Hochheimer,  fr.
Hochheim,  a  village  near  Mainz  in  Germany.
Hockday,  n.,  the  second  Tuesday  after  Easter.. — The  first  element  in  this  compound  is  of  un¬ known  origin.  It  is  not  related  to  G.  hoch,  ‘high’.
hockey,  n.  —  Prob.  fr.  OF.  hoquet,  ‘bent  club, shepherd’s  crook’,  formed  with  suff.  -et  fr.  OF. hoc,  ‘a  hook’,  which  is  of  Teut.  origin  (cp.  OE. hoc  and  see  hook);  prob.  so  called  because played  with  clubs  hooked  slightly  at  the  end.
hocus,  n.  and  tr.  v.  —  Short  for  hocus-pocus.
hocus-pocus,  n.,  a  conjurer’s  trick.  —  Sham  L. Cp.  hoax,  hokey-pokey.
hod,  n.,  a  portable  trough  for  carrying  mortar. —  MDu.  hodde,  ‘basket’,  rel.  to  Frankish *hotta  (whence  F.  hotte,  ‘basket  for  the  back’) and  to  dial.  G.  Hotte,  ‘basket  for  the  back’.
hodden,  n.,  a  coarse  woolen  cloth.  —  Perh.  fr. Northern  E.  dial,  form  of  holden,  pp.  of  held, hence  lit.  ‘cloth  held  (at  home)’.  See  hold.
Hodge,  n.,  the  agricultural  laborer.  • —  A  popular form  of  the  name  Roger.
```


## [2026-09-06T20:51:55.398Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hodiernal\" KLN_1966.txt | head && echo \"---\" && grep -n \"Avestic  zi\\b\\|Avestic  zt\\b\\|Av\\.  zi\\b\" KLN_1966.txt | head"
}
```


### [2026-09-06T20:51:55.463Z] TOOL RESULT

```
11361:dies  non,  a  day  on  which  no  legal  business  is carried  on.  —  L.  dies  non  ( juridicus ),  lit.  ‘a  not juridical  day’.  L.  dies,  ‘day’,  derives  fr.  I.-E. base  *dei-,  *deya-,  *di-,  *dya-,  ‘to  shine’.  See deity  and  cp.  dial,  diary,  diet,  ‘assembly’,  diur¬ nal,  diuturnal,  journal,  and  the  second  element in  hodiernal,  meridian,  Midi,  quotidian.  For  L. non,  ‘not’,  see  non-.
13092:Derivatives  :encompass-er,n.,encompass-ment,n. encore,  interj.  used  in  the  sense  ‘again’.  —  F,, ‘again,  still,  yet’,  fr.  L.  hanc  ad  horam,  ‘to  this hour’.  L.  hanc  is  acc.  of  haec,  fern,  of  hie,  ‘this’; see  hodiernal  and  cp.  haecceity.  For  L.  ad,  ‘to, toward’,  see  ad-.  L.  horam  is  acc.  of  hora, ‘hour’;  see  hour.  It.  ancora,  ‘again,  still,  yet’, is  a  French  loan  word.
17009:Hadrosaurus,  n.,  a  genus  of  extinct  dinosaurian reptiles  ( pa/eontol .)  —  ModL.,  compounded  of hadro-  and  Gk.  araupot;,  ‘lizard’.  See  sauro-. haecceity,  n.,  thisness;  individuality  (scholastic philos.)  —  ML.  haecceitas,  fr.  L.  haecce  (res), ‘this  (thing)’,  with  better  spelling  haece,  fern, of  hlce  (hicce),  intensive  form  of  hie  (fern,  haec, neut.  hoc),  ‘this’.  See  hodiernal  and  cp.  encore, langue  d’oe.  For  the  ending  see  suff.  -ity. haem-.  —  See  hem-.
17340:I.-E.  base  *ki-,  ‘this  one’,  whence  also  Hitt,  ki, ‘this’,  Gk.  k-y.ci,  ‘there’,  Ion.  Gk.  xeT-vo;, Aeol.  xTj-voi;,  Gk.  i-y.cT.-voc,  ‘that  person  or thing’,  <rf|-fx£pov,  ‘today’  (for  *>a£pepov,  lit. ‘this  day’,  fr.  I.-E.  *kyo-,  ‘this’,  and  Gk.  zjpipa, ‘day’),  L.  cis,  citer,  citra,  ‘on  this  side’,  ce-  and -ce,  emphatic  particles  meaning  ‘here,  there’, OSIav.  si,  Lith.  sis,  ‘this’.  Cp.  him,  her,  it,  hence, here,  hither.  Cp.  also  cede,  cis-,  citra-,  cy-pres, et  cetera,  hodiernal,  sic.
17918:hodiernal,  adj.,  of  this  day.  —  Formed  with  adj. suff.  -al  fr.  L.  hodiernus,  ‘of  this  day’,  fr.  hodie, ‘today’,  which  stands  for  hoc  die,  ‘on  this  day’, fr.  abl.  of  hie,  ‘this’,  and  dies ,  ‘day’.  L,  hie  prob. stands  for  hi-ce  or  he-ce,  which  is  compounded of  the  emphatic  particle  hi-,  resp.  he-,  and  the demonstrative  particle  -ce.  Particle  hi-,  he-  is cogn.  with  the  emphatic  particles:  OI.  ghc, ‘just,  indeed,  certainly’,  ha,  ‘of  course,  surely’, OI.  hi,  Avestic  zi,  ‘for,  because;  surely,  indeed’, Gk.  -yp.  (in  ou-xi,  \ct]--/_i,  ‘not’,  vai-yi,  ‘yea, verily’),  OSlav.  -go-,  -ze  (after  a  negation),  Lith, -gu,  -gi.  For  the  demonstrative  particle  -ce  cp. the  second  element  in  L.  islic,  ‘this’,  illic,  ‘that’. See  he  and  cp.  haecceity,  encore  and  langue d‘oc.  For  the  second  element  in  L.  hodie  see dies  non.
21109:Derivative:  langrag-ed ,  adj. langsyne,  adv.,  long  since;  n.,  the  long  ago,  an¬ cient  times  —  Scot,  form  of  long  since. language,  n.  —  ME.  langage,  language,  fr.  OF. (=  F.)  langage,  fr.  VL.  *linguaticum,  fr.  L.  lin¬ gua,  ‘tongue;  speech,  language’.  See  tongue  and -age  and  cp.  lingual.  The  spelling  language (with  u)  is  due  to  the  influence  of  F.  langue, ‘tongue;  language’.  Cp.  next  word  and  languet. langued,  adj.,  having  the  tongue  of  a  tincture  dif¬ ferent  from  the  rest  (her.)  —  Formed  with  3rd suff.  -ed  fr.  L.  langue,  ‘tongue’.  See  prec.  word, langue  d’oc,  the  Romance  language  of  Southern France;  the  Provencal  language.  —  OF.  langue d'oc,  ‘language  of  oc\  lit.  ‘yes  language’  (i.e.  the language  in  which  oc,  fr.  L.  hoc ,  ‘this  thing’,  is used  for  ‘yes’).  L.  hoc  is  the  neut.  form  of  hie; see  hodiernal  and  cp.  haecceity.  Cp.  next  word, langue  d’oil,  the  Romance  language  spoken  in  the center  and  north  of  France;  the  French  lan¬ guage.  —  OF.  langue  d'oll,  ‘language  of  oil,  lit. ‘yes  language’,  i.e.  the  language  in  which  oil  (now oui;  derived  fr.  L.  hoc  ille,  scil.  fecit,  ‘he  did  it’) is  used  for  ‘yes’.  See  prec.  word  and  ille. languet,  languette,  n.,  a  little  tongue;  used  of  vari¬ ous  tongue-shaped  parts  of  objects.  —  ME.  lan¬ guet,  languette,  fr.  MF.  (=  F.)  languette,  dimin. of  langue,  ‘tongue’.  See  tongue  and  -et,  -ette, and  cp.  language.
24128:moderate,  tr.  v.  —  ME.  moderaten,  fr.  L.  modera¬ tus,  pp.  of  moderari.  See  moderate,  adj . moderation,  n.  —  ME.  moderacion,  fr.  MF.  ( =  F.) moderation,  fr.  L.  moderationem,  acc.  of  mode- ratio,  ‘moderating’,  fr.  moderatus,  pp.  of  mode¬ rari.  See  moderate,  v.,  and  -ion. moderator,  n.  —  ME.  moderatour,  fr.  L.  mode¬ rator,  gen.  -oris,  ‘manager,  ruler,  director’,  lit. ‘he  who  moderates’,  fr.  moderatus,  pp.  of  mode¬ rari.  See  moderate  and  agential  suff.  -or. modern,  adj.  —  F.  moderne,  fr.  Late  L.  modernus, ‘modem’,  formed  with  suff.  -e-rnus  fr.  L.  modd, ‘just  now’,  which  is  prop.  abl.  of  modus,  ‘meas¬ ure’,  and  lit.  means  ‘by  measure' ;  see  mode.  For the  formation  of  Late  L.  modernus  fr.  L.  modd cp.  L.  hesternus,  ‘of  yesterday’,  fr.  heri,  ‘yester¬ day’,  hodiernus,  ‘of  today’,  fr.  hodie,  ‘today’. Cp.  hesternal,  hodiernal;  cp.  also  diurnal,  noc¬ turnal.
---
17918:hodiernal,  adj.,  of  this  day.  —  Formed  with  adj. suff.  -al  fr.  L.  hodiernus,  ‘of  this  day’,  fr.  hodie, ‘today’,  which  stands  for  hoc  die,  ‘on  this  day’, fr.  abl.  of  hie,  ‘this’,  and  dies ,  ‘day’.  L,  hie  prob. stands  for  hi-ce  or  he-ce,  which  is  compounded of  the  emphatic  particle  hi-,  resp.  he-,  and  the demonstrative  particle  -ce.  Particle  hi-,  he-  is cogn.  with  the  emphatic  particles:  OI.  ghc, ‘just,  indeed,  certainly’,  ha,  ‘of  course,  surely’, OI.  hi,  Avestic  zi,  ‘for,  because;  surely,  indeed’, Gk.  -yp.  (in  ou-xi,  \ct]--/_i,  ‘not’,  vai-yi,  ‘yea, verily’),  OSlav.  -go-,  -ze  (after  a  negation),  Lith, -gu,  -gi.  For  the  demonstrative  particle  -ce  cp. the  second  element  in  L.  islic,  ‘this’,  illic,  ‘that’. See  he  and  cp.  haecceity,  encore  and  langue d‘oc.  For  the  second  element  in  L.  hodie  see dies  non.
```


## [2026-09-06T20:52:04.165Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *736 *$\\|^ *734 *$\" KLN_1966.txt | head && echo \"--- 545 search\" && grep -n \"^et  cetera\\|^et cetera\\|et  cetera,\" KLN_1966.txt | head"
}
```


### [2026-09-06T20:52:06.075Z] TOOL RESULT

```
17887:734
17937:736
--- 545 search
13712:Etat  Major,  the  staff  of  the  army.  —  F.  etat- major,  fr.  etat,  ‘state’,  and  L.  major,  ‘greater’. See  etat  and  major,  adj. et  cetera,  ‘and  other  things’.  —  L.,  fr.  et,  ‘and’ (see  et),  and  neut.  of  ceteri,  ‘the  others’,  which is  formed  fr.  I.-E.  pron.  pref.  *ce-,  ‘there;  behold’ (see  he),  and  I.-E.  *etero-,  ‘the  other’,  whence also  Umbr.  etro-,  ‘another’,  Avestic  a-tara-, ‘one  of  the  two,  this’,  Alb.  jatere,  jatre,  ‘the other’,  OSlav.  jeteru,  iteru,  ‘some,  one’, etch,  tr.  and  intr.  v.,  to  engrave  with  acid.  —  Du. etsen,  ‘to  etch’,  fr.  G.  atzen,  ‘to  corrode’,  fr. MHG.  atzen,  etzen,  fr.  OHG.  azzon,  prop,  ‘to feed,  bait’,  causative  of  e$$an,  ‘to  eat’.  See  eat. Derivatives:  etch,  n.,  etch-er,  n.,  etch-ing,  ver¬ bal  n.
17340:I.-E.  base  *ki-,  ‘this  one’,  whence  also  Hitt,  ki, ‘this’,  Gk.  k-y.ci,  ‘there’,  Ion.  Gk.  xeT-vo;, Aeol.  xTj-voi;,  Gk.  i-y.cT.-voc,  ‘that  person  or thing’,  <rf|-fx£pov,  ‘today’  (for  *>a£pepov,  lit. ‘this  day’,  fr.  I.-E.  *kyo-,  ‘this’,  and  Gk.  zjpipa, ‘day’),  L.  cis,  citer,  citra,  ‘on  this  side’,  ce-  and -ce,  emphatic  particles  meaning  ‘here,  there’, OSIav.  si,  Lith.  sis,  ‘this’.  Cp.  him,  her,  it,  hence, here,  hither.  Cp.  also  cede,  cis-,  citra-,  cy-pres, et  cetera,  hodiernal,  sic.
```


## [2026-09-06T20:52:19.523Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=13650 && NR<=13730 && /^ *[0-9]{3} *$/ {print NR\": \"$0}' KLN_1966.txt"
}
```


## [2026-09-06T20:52:20.599Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"etero-\\|e-tero\\|Pronominalstamm\" POK_01.txt | sed -n 1,30p && echo \"=== page 283-284 marker\" && grep -n \"^ *284 *$\\|^ *283 *$\" POK_01.txt"
}
```


### [2026-09-06T20:52:23.144Z] TOOL RESULT

```
13685: 544
13696: 343
```


### [2026-09-06T20:52:25.301Z] TOOL RESULT

```
991:4-  au-,    u-    (:  ue-,    uo-)    Pronominalstamm   ,jener',   auch    gegenüberstellend , alter,    alius',   , andrerseits,   hinwiederum',    in   zwei    aufeinanderfolgen- den Satzgliedern  gesetzt  ,der  einerseits  —  der  andrerseits',  , einerseits —  andrerseits'. awo-:  Ai.  av.  apers.  ava-  ,jener';  aksl.  aruss.  ov^^  —  ov^-  ,der  einerseits —  der  andrerseits,   der  eine  —  der  andere',    ovogda  —  ovogda  ,das  eine
4742:eno-  (wohl  e-no-) :  ono-  :  no-  :  -rze-  Pronominalstamm  ,jener'.
=== page 283-284 marker
4049:283
4065:284
```


## [2026-09-06T20:52:28.171Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4045,4090p' POK_01.txt | cut -c1-1500"
}
```


### [2026-09-06T20:52:28.221Z] TOOL RESULT

```
lat.  IS,  id  Nom.  Sg.  ra.  (alt  auch  Is,  inschr.  eis,  eis-dem,  entweder  mu -s  ausgestattetes  idg.  *ei  =  ai.  ay-dm,  wie  man  auch  für  umbr.  er-e  u^d bestimmter  für  ir.  (h)e  ,Qr'  eine  solche  Grundf.  *ei-s  erwägt,  oder  Umbil  ' düng  von  is  nacli  eims,  e(i)l);  Akk.  altlat.  im  (=  gr.  IV)  und  em,  gedoppe^ emem  ,eundem^  (vom  Parallelst,  e-?)  =  Adv.  em  ,tuni'  und  *im  in  inter-im , unterdessen',  in-de  ,von  da',  Dat.  Abi.  PI.  ibus  (:  ai.  ebhydh)]  osk.  ü-iV. ,is',  idicj  idik  ,id'  (das  Anhängsel  -ik,  -ic  ist  selber  das  adverbiell  erstarrte n.  *id  +  *A;e),  osk.  is-id-um  ,idem'  und  esidum  ds.,  umbr.  er-e  ,is'  ers-e  er-g ,id',  umbr.  Dat.  Sg.  esmeij  esmikj  Gen.  PL  osk.  eisun-k,  umbr.  esom  (=  ^i. esdm)',  daraus  wurde  ein  St.  *eiso-  außer  in  Nom.-Akk.-Formen  gefolgert z.  B.  osk.  eizois  ,iis^,  umbr.  eru-ku  ,cum  eo',  doch  ist  immerhin  mit  einem alten  n.  *ed  zu  rechnen,  vgl.  lat.  ecce  ,da!  sieh  da!^  (wohl  aus  *ed-ke) =  osk.  ekk-um  {*ed-ke-um)  ,item',  und  vielleicht  Akk.  med,  ted,  ssd,  wenn aus  *me,  *te,  *se  +  ed,  wenngleich  dies  nur  mehr  adverbiell  erstarrtes  *ed voraussetzt;
ital.  eo-,  eäj  im  Osk. -Umbr.  nur  in  den  Nom.  (außer  Sg.  m.  n.)  und Akk.,  im  Lat.  auf  fast  alle  Casus  obliqui  ausgedehnt  (nur  eins  aus *esj,o-Sj  danach  Dat.  ei  steht  abseits),  z.  B.  lat.  ea,  eam,  osk.  iükj  ioc  ,ea^, io7ic  ,eum^,  u.  earn  ,eam',  sind  von  der  dem  ai.  Nom.  ay-dm  entsprechen- den Form  '^e(i)om  ausgegangen,  die  wegen  ihres  Ausganges  -om  als  Akk. empfunden  wurde  und  eam  usw.  nach  sich  zog;  tarn  bei  Varro  1.  1.  5,  166 und  8,  44  wohl  Schreibfehler  für  eam.  —  Aus  dem  Lat.  hierher  ipse  aus *ls-pse  (wegen  alat.  fem.  eapse),  is-te  (aber  ille  erst  danach  umgebildetes  - olhts),  vgl.  umbr.  estu  ,istumj  ista';
air.  e  [he)  ,er^  (wohl  *ei-s),  s.  oben;  ed  (Jied)  ,es^  (aus  *ic?-ä  =  got.  ita, womit  formell  identisch  ai.  idä  ,jetzt';  aber  lit.  tadä  ,dann'  erfordert wegen  ostlit.  tadii  einen  Auslaut  auf  Nasal);  Nom.  PI.  e  (he)  m.  f.  n.  =  • mkymr.  wy  (hwynt-wy)  wohl  wenigstens  zum  Teil  aus  idg.  *ei  (Näheres bei  Thurneysen  Gr.  283),  Akk.  Sg.  bret.  en  ,ihn,  es'  (infigiert),  cymr.  e (ebenso),  ir.  -a  n-  (ebenso),  -i  (suffigiert  hinter  Verben;  hinter  Präp.  teils ebenso,  z.  B.  airi  aus  *ari-en  ,auf  ihn',  teils  nur  mehr  als  Mouillierung  nach- wirkend, z.  B.  foir  aus  *uor-en),  Gen.*  Sg.  *esio,  f.  *esiäs  ,eius',  proklit.  a, älter  z.  T.  noch  e,  os;  cymr.  *eid-  nach  dem  Vorbild  der  konjugierten  Präpo- sitionen zu  mcymr.  eidatv,  f.  eidi  differenziert,  womit  identisch  air.  a  ,sein' (len.)  und  ,ihr'  (geminierend),  cymr.  com.  y,  bret.  e,  usw.;  über  air.  be- tontes äi,  ae  ,eius'  und  Dat.  PI.  -ib  s.  Thurneysen  Gr.  285;
got.  is  ,er',  Akk.  in-a,  neutr.  it-a  (s.  o.)  ,es'  (dazu  neugebildete  Plural- formen: got.  eis  aus  *ei-eSj  Akk.  ins,  Dat.  im,  ahd.  as.  im),  ahd.  er,  ir,  Akk.
283
in-an,  in;  n.  iz-,  as.  in-a,  n.  it'^  anord.  Relativpartikel  es,  er,  run.  eR-  vom St.  e-:  Gen.  Sg.  got.  m.  w,  f.  i^o»,  alid.  m.  n.  es(is),  L  ira({ru),  as.  es(is)^ eraijra)]  Gen.  PI.  g'ot.  ize,  22;o,  as.  ahd.  iro]  Dat.  Sg.  f.  got.  izai,  ahd.  (mit anderer  Endang)  iru-^  m.  n.  got.  imma,  ahd.  imw,  ???7o,  as.  imw,  vom  St.  i- got.  Akk.  ija  (ahd.  sia  usw.  mit  s-Vorschlag  nach  dem  Nom.  st)j  wonach neugebildete  Pluralformen,  got.  Nom.  Akk.  ijös  (ahd.  s?o);
lit.  jis  ,er',  Akk.  jl  (zum  anl.  j-  s.  Brugmann  Grundr.  11 2  2,  331),  fem. ji,  Akk.  ja  (;ös,  ;aT  usw.);
aber  aksl.  Akk.  Sg.  f.  jq,  Nom.  Akk.  PI.  f.  je  (über  die  weiteren  Kasus s.  Brugmann  aaO.),  Akk.  Sg.  m.  -(;>  in  vidity-jh  ,videt  eum',  mn-h  ,m eum'  usw.  (über  weiteres  slav.  Zubehör,  z.  K  jak^  ,qualis',  jeUk^  ,quantus', s.  Berneker  416  f.)  eher  aus  idg.  iV;
nach  Pedersen  Hitt.  58  f.  soll  das  Pron.  -as  ,er^  usw.  ein  0  im  Ablaut zu  idg.  *esio  usw.  enthalten  (?);  vom  Stamm  i-  hat  sich  vielleicht  das  n. it  ,es'  in  der  Verbindung  netta  ,und  es  dir^  (*nu-it-ta)  erhalten  (Friedrich Heth.  Elem.  I  27);  vgl.  hierogl.  hitt.  is  , dieser',  Akk.  jaw.
IJ,  Relativstamm  io-:
ai.  yds,  yd,  ydd,  av.  ?/ö,  gr.  b'g,  rj,  d  ,welcher',  phryg.  log  (vi)  ,wer  immer', slav.  *ia-  in  i-ze,  L  ja-ze  usw.,  halt.  u.  slav.  in  der  Bestimmtheitsform  des Adjektivs,  z.  B.  lit.  geräs-is,  apr.  pirmaiin-ien,  -in^  aksl.  dohry-jh  (s.  Ber- neker 416 f.,  Trautniann  105 f.).  Zweifelhaftes  (lit.  jeT  ,wenn',  got.  jabai ,wenn')  s.  bei  Brugmann  IP  2,  347  f.  (Lit.);  Keltisches  bei  Pedersen  KG.  II 235,  Thurneysen  Gr.  323,  doch  kann  cymr.  a  nicht  dazu  gehören.
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
ei  (Lok.):  gr.  sl  ,*so,  wenn'  (sl-ra  ,dann',  eT-d^s  , möchte  doch!',  iTt-sl (vgl.  el.  iTC-T^)  ,da*,  l/r-fitra;  daneben  dial.  ai,  Lok.  des  f.  St.  a,  und  ^  2i Instr.  ,wenn';  aksl.  i  ,und,  auch'  (vgl.  ti  ,und'  vom  St.  *to-;  von  Brückner KZ.  46,  203  dagegen  =  lit.  tei  gesetzt),  got.  -ei  Relativpartikel  (vgl.  jbei vom  St.  *to-  in  gleicher  Geltung),  z.  B.  sa-ei  , welcher',  nach  Junker  KZ. 43,  348  auch  die  arm.  Abi. -Endung  -e.    Siehe  auch  unten  1-.
em  (alat.  em,  s.  oben  S.  282)  liegt  vor  in  gr.  evd^a  ,da,  dahin,  damals*, rel.  ,wo,  wohin,  woher',   i'v-9-sv  ,von   da,  von  wo'  usw.    (Schwyzer  Gr.  Gr.  .   . I  628);  über  air.  and  s.  oben  S.  37  und  vgl.  kypr.  ävöa'  aiirrj.  "^"
e-tos:   ai.  d-taJi  ,von  hier'  (s.  unter  eti).
i:  wahrscheinlich  im  Lok.  auf  idg.  -i;  ferner  die  Grundlage  der  Kom- parativbildung *i-tero-:  ai.  i-tara-  ,der  andere'  (neuiran.  Entsprechungen bei  Bartholomae  IF.  38,  26 f.);
lat,  iterum  ,zum  andern,  zum  zweiten  Male* ;  ferner  in  ai.  i-va  ,wie' (vgl.  oben  ?}-/«  ,wie*);  in  gr.  i-di  ,und*  (vgl.  9j-ös).
i-dba  und  i-dhe:
ai.  i-hd,  präkr.  idha,  av.  iöa  ,hier';
gr.  i&aysvfjQ  ,(*hier  geboren*,  daher:)  eingeboren,  rechtmäßig  geboren' (über  id^aiysvyjg  s.  Schwyzer  Gr.  Gr.  I  448);
lat.  ibl  ,da,  dort'  (die  Lautentwicklung  dh  zu  f,  b  nach  ubl;  im  Auslaut nach  den  Lokativen  der  o-St.  gerichtet),  umbr.  ife  ,ibi,  eö',  ifont  , ibidem' (die  ar.  und  ital.  Formen  könnten  an  sich  auch  -dhe  enthalten,  vgl.  ai. ku-ha  =  aksl.  kz-de  ,wo',  sb-de  ,hier'  und  Schwyzer  Gr.  Gr.  I  627*);
285
nicymr.  yd,  y  ncymr.  ydd  Verbalpartikel,  com.  yz,  yth-,  bret.  ez-? (s.  Pedersen  KG.  II  234,  Lewis-Pedersen  243,  Thurneysen  Gr.  324 f.); dazu  auch  air.  infigiertes  -id-  aus  *id(h)e  oder  Hd{h)i.
i'tih)''.  ai.  itthä,  itthäd  ,bier,  dort',  av.  ipU  ,so',  ai.  itthdm  ,so'  und jjiit  -t-  {-t9  oder  -<i?)  ai.  iti  ,so';  lat.  ita  ,so',  item  , ebenso,  ebenfalls',  umbr. itek  ,itaS  mcymr.  Präverb  yt-,  ncymr.  yd-,  z.  B.  in  2/^  yd-wyf  ,ich  bin'; lit.  dial.  it   , durchaus;  wie',  it,  yt  ,ganz,   sehr',   lett.  it,   itin  ,recht,  eben'.
i  (betont  zur  Verstärkung  eines  deiktischen  Wortes,  unbetont  hinter einem  relativ  gebrauchten  Wort) :
ai.  i  (auch  im),  av.  i  hervorhebend  nachgestellt,  nach  Relativ  in  ved. yad-i ;
gr.  ovtoa-t,  -tv  {==  ai.  im?  oder  erst  jüngere  Erw.  von  -i?),  izeivoa-i, el.  To-i;
umbr.  wohl  in  po-ei  ,qui'  (usw.),  lat.  in  utl  (aus  *uta-t)'^
air.  {h)l  deiktische  Partikel  und  Stützpartikel  vor  Relativsätzen;
got.  -ei  Relativpartikel  in  sa-ei,  iz-ei,  ik-ei  hingegen  wohl  idg.  *ei,  s.  oben;
aksl.  verstärkend  in  to-i  (s.  Berneker  416),  aksl.  e-i  ,ja,  wahrlich' (?  Berneker  296).
Auch  im  1.  Gliede  von  ai.  i-drg-  ,so  aussehend,  so  geartet',  lit.  y-'paBai jbesonders',  y-patüs  ,einsam,  allein,  abgesondert,  eigentümlich'.
```


## [2026-09-06T20:52:48.000Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kies-\\|kiēs\\|čeč\\|ceč\" IEC.txt | head -20"
}
```


### [2026-09-06T20:52:48.044Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T20:52:48.664Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=320 && NR<=330 {print \"=== leaf \" NR; print substr($0,1,200)}' IEC.txt"
}
```


### [2026-09-06T20:52:50.401Z] TOOL RESULT

```
=== leaf 320
). Isophone in Du. over- rompelen (‘take by surprise. No certain etym.)
krumbos “bent, crooked; bend, crutch, haunch, joint’. Cf. krmb- Olr. crumb, MIr. cromm, Ir. crom ‘bent, curv- ed, crooke
=== leaf 321
ant in Li. kriusà "bal": Latv. kru- sa, id. Long-gde in OE hrüse, f. “earth, ground”; short-grade in OE hryre (‘fall, decay’, if here)
krustos, à (cover, covering, layer, case, en- casement
=== leaf 322
rawl represents a variant of type *krgos); R korgà ‘crow’; Cz. cf. krhat, v. ‘grate, croak’. See Supt:K
krk- radical element of onomat. verbs and nouns ‘croak, caw, crow’, etc. See also f
=== leaf 323
O-gde in Li. karšē *decrepitude". Cf. kerk- and next
krKos ‘dwarfed, lean, sickly’. Cf. krsos (2). WP I, 420 Skt. kr$ah, id.; Av. koroso, id.; Alb. cf. kérthi, gs kérthini ‘weakling’ besid
=== leaf 324
l. kierpce f. id.; Slovene krpica ‘rag’. A ^wanderword' of uncertain pro- venance, w. variant vocalism in the radical (*krp-: *korp- or *karp-). A further variant vo- calism is indicated in Li. ku
=== leaf 325
Society, 1942, 11-14, in need of revision, and "Initial x/š in the Slavonic Languages’, Slavo- nic and East European Review, 88, Dec. 1958, 131-140)
ksandh- ‘bright; brillance’. Cf. WP I, 358 A
=== leaf 326
ng-, Sequanian: -cingos ('gait, path” or sim.)
ksërið (1) ‘dry, parch, wither; turn dry, etc. Cf. kseros (1). WP I, 503 Skt. ksáràmi (2) ‘perish’; Arm. cf. xarem (‘sear, brand”, fr. *k
=== leaf 327
 cf. szybki, adj. ‘quick’; R Sibkit, id.; Latv. cf. (?) šaubu, 3aubit ‘swing’, tr.; šaubas, fpl. id. Cf. also Skt. ksobhah, m. ‘tremor, sway’
kseul- (kseuel-) ‘sway, swerve, totter’.
=== leaf 328
 OCS Setavú "Tool. hardy’; Cz. po-šetilý “silly”
ksnt- (2) ‘prickly; prickle, thorn’. Cf. ksonio, ksost-, ksot- Oss. cf. åxsid ‘carded, combed’; Gk. ksánsis, f. ‘carded wool, card
=== leaf 329
ewe(s) diptera(s) *scrapers and splitters of skins' (Pylos); Gk. ksüo ‘shave, scrape’; Alb. shij, aor: shiva & shina, T: shira ‘thresh, tread corn, winnow, scour, sweep, wipe’; Latv. cf. skuj
=== leaf 330
e hýpel, m. id.; Li. cf. kūbrýs, m. ‘mound; nape of neck’ beside kuburýs, m., kübure ‘hillock’; (Du. cf. heuvel “hill? beside hobbel, m. ‘hump, lump” from a variant)
kubito- (varian
```


## [2026-09-06T20:52:56.968Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"‘mite\\|'mite\\|“mite\\|mite’\" IEC.txt | head -20"
}
```


### [2026-09-06T20:52:57.017Z] TOOL RESULT

```
4412:grünå, os, iə ‘speck, fleck, flake, awn, mite’ Gk. grünós “firewood'; grunón “wild fig’; Lat. grunae ‘chaff, awns, or dust from wheat- sheaves’; Srb. Slovene grinja ‘mite, insect". (Isophonic are Gk. grüne ʻ“incense’ and grü- nos 'griffin")
4439:gubəlos, gubulos ‘hump, lump, boss’. Vari- ant: gubər-. See next Oss. (ambig) gubir 'hunchbacked'; MHG ko- fel “peak, summit’; Li. gübulas “lump” beside gübras ‘mound’. (Isophones: OE copel “un- steady’; LG koppel ‘paddock’; Cz. heble ‘tiny object, mite’)
8784:KiKos, à, us “tip, teat, dot, tot, infant’. Cf. Kik- and Kük- Skt. Si$ub, m. ‘infant’; cf. Si$náh, am. and Si$an ‘penis’; Oss. sis (1) (feather; tip; hair’; Alb. thithë, f. ‘teat’; MIr. cich, Ir. cioch, f. id.; Rum. substr. fítá, id. (doublet in Alb. cicë, f. id.); Srb. sisa, id. Cf. Li. šišas ‘pixie- hat; mood, whim’; Hes. kiknia ‘mites, ticks’ and (alleged) Gk. kíkkos (‘pericarp, trifle’: Skt. síkha “tuft, tip'?). See Kiksa and cf. Per. sisak ‘beetle’
8843:Kies “mite, tick, vermin'. (Variant: Kis-) Per. sàs “bug, louse’; Oss. sási "liver-fluke' beside saska ‘midge’ and eist -tä ‘louse’; Arm. cec, o-st. w. assim. consonants & short vowel *worm, mite, maggot, moth, woodlouse'; Gk. sés, gs seós ‘mite’
10583:meluos ‘soft, sweet’. See meleuos Arm. met, gs & ab. s. meyu, s. ‘honey’; meyu, gs mevui, ab. s. -uav ‘honeybee’; Ir. cf. mealbh- ach ‘sweet, honeyed'; W cf. melw-lith ('sun- dew’, lit. *sweet-lure") beside melus, adj. ‘sweet; ME melwe ‘mellow’. (Isophonic: MHG mële wf. & milwe, milewe, s. wf. ‘mite’; milwen, v. ‘powder’, cf. melo, io, etc. NB. Bre- ton mil-fid, mil-vid & mil-chwid, m. ‘thrush’, whence Fr. mauvis, E mavis are referred by Dottin to a Gaul. prototype reconstructed as melvi-)
10766:mid- “insect, tick, mite’.
10767:Gk. mídas, m. (2) ‘tick’; OE mite, wf., LG mit, wf., Du. mijt ‘mite’. (LW. in Fr. mite, f. ‘moth’, fr. LG. Isophonic LG met, mit, wf. ‘tick’; Du. mijt, f. id.) Cf. Gk. Mídas (proper name) (?)
10789:miklos, å, is (mikəl- mikul-) (1) “dainty, fine. Gk. (ambig.) míkulos, (expressive) míkkulos ‘tiny’; Alb. cf. mikloj, v. (flatter, fawn’, from a noun of type *mikuli- or sim.); Br. mégel, s. f. pl. mégled ‘tick, mite’; Li. miklas, miklüs “smart, clever’. Cf. also Slovene miken, adj. tiny”
14200:quorolis ‘mite, tick’. Cf. qurlis Arm. cf. akalar, akarar ‘mite? beside akal (‘bowstring hemp’, lit. ‘twist’ Bedevian. Pho- nol. obscure); Br. poral, pl. -ed, m. ‘tick’; Skt. cf. karirah, am. mn. ‘bamboo shoot? beside (z-gde) kurulah, m. ‘curl, lock’; Lat. cf. cur- culio, gs: -Onis, m. ((1) 'corn-weevil, lit. ‘twister’. Here, despite WH, and see below: quorquol-) (1)
14265:qurp- “turn, shape, form, body'. Cf. querp-, quorp- Skt. krp, f. “form, beauty’; Av. kohrp “flesh, body’; Per. cf. kalbad, s. “form, body’; Gk. prapís, f. “bosom, heart, diaphragm’; OLat. qurpus, Lat. corpus, gs: -oris, n. “body, flesh, substance, mass’; Olr. & mod. Ir. crí, m. ‘body, shape, frame’; (Olr. also = “life*); OHG cf. href, OE hrif, n. (belly, womb’, fr. *qurep-); Icel. horf, n. “trend, relation, condition); hor- fur, fpl. ‘outlook’; cf. ON horfa, v. ‘turn, ap- pear’. (Isophones: Slovene krp-elj, s. ‘mite, tick, crablouse’; Slovak krpelec, m. ‘dwarf;
15283:seus-, seuser- (?) ‘vermin’ OHG siurra, siura, wf. & siuro, wm. ‘tick, mite’; Du. zier, f. id. (and ‘bit, scrap’); R cf. šušera, f. ‘rabble’; Li. cf. sause, f. ‘grub’; Latv. cf. šaušalas, fpl. ‘revulsion’
15585:skerb- (1) ‘treasure, valuable’. (Variant: skrb-) MHG schërpf, sn. ‘mite, farthing’; OE sceorp, n. ‘ornament, equipment’; scierpan, v. ‘adorn; equip’; Pol. cf. (z-gde) skarb, m. ‘treasure’ (LW in Li. skarbas, id.); Srb. skřb, f. ‘care, concern’
15615:skheud- in Skt.) Skt. Codami, v. “egg on; hurry’; Alb. hudh, v. ‘fling’; MIr. cf..brot-scuad, s. ‘rubbish’; OHG skiozan, OS skiotan, OE scéotan, sv. 2 'shoot'; sceot, adj. ‘ready, quick’; ON skjóta, sv. 2 as OHG; skjótr, adj. as OE; (m. also “vehicle; horse); Sw. skjuta, sv. 2. ‘thrust, smite’ skeulos, om, is, à ‘cover, shelter’. Cf. skül-. (Skt. variant: skhoul-) Skt. cf. kholah, m. 'rainhat, helmet; Arm. (vowel ambig.) xuy, gs: xyi, ab. s. xyiv, s. ‘hut’; ON skjól, n. ‘shelter, cover’; Sw. skjul, n. ‘dutch barn’; N. E. shiel, shieling 'shepherd's huť; Norw. cf. skjule, v. ‘hide’. WP II, 547 skeup- ‘poke, stab, grope’. (Skt. variant: skhiup- or skhup-). Gmc. ambig. Skt. čhupāmi, v. “touch'; Go. (ambig. *skeubh-?) skiuban, sv. 2. ‘thrust; MHG schieben, sv. 2. id.; OE sceofan, sv. id. (beside sküfan, sv. 2. with instant aspect as lücan, sv. 2 ‘lock’, and a-sprütan, sv. 2. ‘sprout’; Du. schuiven, sv.; spruiten, id.); R SCup, m. “probe, lancet'; po-SCüpat, inf. “feel, grope’. Nominal type in Skt. chupah, m. “touch; hand-to-hand fight". Isophonic in OCS Stupli, adj. “weak, lean, ailing’; Pol. szczupły, Slovak, Stüply, id. skeut- ‘shred, tatter; shredded, torn’. (Vari- ant in Skt?) Skt. cf. a-Chotitab, pp. “torn off (butisophonic pra-$Cotami, v. = 'drip); ON skjóða, f. “skin bag’; Li. skiautis, gs: ies, f. ‘shred, snippet"; Latv. cf. Sautrs, adj. (loose, hanging’, from a variant *sKeut-?). (Isophonic in OCS Stusto, Stutiti, v. ‘perceive’, radical in Av. sku- look") skéuð, ið (sKeu-) “jump, start, go’. Cf. sKeuo as separate entry Skt. cf. (radical only) chyu- ‘go’; Gk. cf. skeüos, n. ‘equipment’; Alb. hov, v. jump’; Ir. cf. sceabha, m. ‘eagerness’; Go. skewjan, v. go’. LW in Fr. esquivier, It. schivare, Alb. shkoj & E eschew, via Romance); ON skæva, v. ‘hurry, clear off; (o-gde in) Du. schooien, v. ‘go away, clear off”; Fris. skoaje, v. ‘arrange’ (factitive: “make go"); OCz. ščuju, SCváti, v. fegg on: Pol. szczuC, v. ‘incite’; Ukr. SCuty (w. instr.), id. skond-, r-gde formula to accommodate some forms of type skend- (skand-); cf. sküd-
17338:streb- (stréb-) “twist, torture” Alb. shtrebé f. ‘mite’; Gk. cf. streblós, adj. ‘twisted’; Umb. strebula, npl. ‘intestines’; MHG cf. (long-gde) strafen, v. ‘punish’; strafe, sf., ‘punishment’. Cf. also Lat. stribligo, stri- biligð, f. ‘gaffe, solecism’; (potential isophone in Li. strebule, f. “angelica')
```


## [2026-09-06T20:53:05.288Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\n# find char offset of line 8843 (1-based)\noff=sum(len(l)+1 for l in lines[:8842])\nprint('leaf(0-based ff count)=', d[:off].count('\\f'))\n\""
}
```


### [2026-09-06T20:53:08.377Z] TOOL RESULT

```
leaf(0-based ff count)= 352
```


## [2026-09-06T20:53:15.168Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==353 {print}' IEC.txt | head -c 3000"
}
```


### [2026-09-06T20:53:16.750Z] TOOL RESULT

```
 “hail, summon’. In this sense only in Lat. cieo, id., but for sense of ‘go’, etc. see kiieio (ko) with velar initial. WP I, 361. Cf. Kie)
Kiemo, Kim- ‘hither’. Cf. Kie Umb. cimu, id.; OCS sémo, OCz. sém, R sjam, id. beside OCS (Cod. Supra.) sím, id.
Kiemos (Kemos) ‘dark, hoary, grey’. WP I, 361 Skt. $yàmáb “indigo, dark’; Arm. cpd. n-seam & n-sem, -i, -av *murky, grey'; Alb. i thimé ‘grey, hoary’; Li. Sëmas *blue-grey, livid". Cf. the variant Ir. ciamhar (*misty, gloomy’, fr. *Kemor-). The vocalism of Kémos is echoed in ON sámr ('swarthy', fr. *sémo-)
Kien- (Kion-, Kin-) ‘this’. (Emphatic form of
type Kis, q.v.) OCz. sen, m., id.; Li. cf. Siafi-dien ‘today’, etc.; Latv. cf. $o-dien, So-gad, šo-rīt ‘this day, year, morning'. (Parallel formations occur with type *sis, q. v. Cf. Galatian and Gaulish -sin, Sequanian sin-divos, -diu: W he-ddiw: Br. héziu, hiziu, hiriu (sic) today?)
Kieros (Kéros) ‘dark, grey ON hárr, id.; Ir. cíor & ciar, d R séryj ‘grey’; Cz. Ser, id.
Kies “mite, tick, vermin'. (Variant: Kis-) Per. sàs “bug, louse’; Oss. sási "liver-fluke' beside saska ‘midge’ and eist -tä ‘louse’; Arm. cec, o-st. w. assim. consonants & short vowel *worm, mite, maggot, moth, woodlouse'; Gk. sés, gs seós ‘mite’
Kieuuó, ið “move, stir’. (Variant of kieuuo, q. v.)
Gk. seúð, epi-sseúð ‘urge on, drive, chase’; Blg. sòvam ‘shove, wave’; OCz. suju, sovati ‘shift’; R sovàti beside sunüti “shove, shift?
(Kičuos ‘dark’, see Kruos (4))
Kio (Kiði) instr. masc. sg. of Kis, q.v. WP I, 453 Arm. cf. suj-n “this, that, the same”; Blg. saj ‘thus’; Li. Siuð (but dual nom. and acc. in Li. Siuo-du “these two")
Klak- (?)
Skt. cf. Slaksnah ‘slippery’; Li. cf. Slakü, éti ‘drip, drop’; Slákas, "drop, spot, freckle’; Latv. slaka ‘sprinkle, spray”
Klamo (Klamáàio) ‘resound, shout, exult’. Cf.
623
WP I, 444, Lat. and Gmc. ambig. cf. klàmo
(2)
(Lat. clamo, are ‘shout, exult? is ambig. cf.
klàm- Ou: Ir. cf. clamh- in the cpd. clamh-
ascar (“confused noise’: ascar = confusion); clamhán, m. ‘buzzard’; OHG hlamon, inf.
‘rush’ beside OE hlemman ‘clamour’; ON
hlamma ‘exult’; Li. $lamü, éti ‘rush, rustle’ Klau- (?) *incline, fall; inclined’
Skt. cf. $ravanah, śroņáh ‘lame’; Lat. cf. clau-
dus, id.; OCS cf. sludy, gs -dve, f. ‘precipice’ Klagh- (?)
Skt. Slaghe ‘boast, praise’; OE hlegian ‘roar’ (Kle-, Kleiio, see Kleio, Kli- and next) Kleiios, à 'aslant, twisted; slant, left-hand;
wrong'. Cf. WP I, 490 & II, 378
Skt. $rayah ‘refuge’; Alb. cf. -kithi (in pér-sé-
kithi *awry); Olr. clé, Ir. clé, ci "left-hand,
unlucky’; W cledd, pl. au. m. “left side, north; rest, repose’ beside go-gledd (/north', fr. upo-^); Br. kleiz, adj. ‘left-hand’; Cor. cléth,
id. (and *north"); Go. cf. hlei-duma ‘left-hand’;
Latv. sleja “line, stroke’. (Variant: Kleios, a) Kleitos, à, is,
```


## [2026-09-06T20:53:21.409Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *598 *$\" POK_02.txt && echo \"---\" && grep -n \"sipha\\|siphä\\|çiphä\\|xiphos\\|Zweig'\" POK_02.txt | head -20"
}
```


### [2026-09-06T20:53:23.610Z] TOOL RESULT

```
Exit code 1
```


## [2026-09-06T20:53:27.397Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"598\" POK_02.txt | head -10; echo \"=== xiph\"; grep -n \"^kseibh\\|kseip\\|ksiph\\|iiicpog\\|^skei\" POK_02.txt | head; echo \"=== search sipha\"; grep -rn \"sipha\" POK_0*.txt POK_full.txt 2>/dev/null | head"
}
```


### [2026-09-06T20:53:27.473Z] TOOL RESULT

```
647:WP.  I  598  f.,  WH.  I  429  f.  .
4018:598  9
=== xiph
=== search sipha
```


## [2026-09-06T20:53:29.477Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4010,4048p' POK_02.txt | cut -c1-1500"
}
```


### [2026-09-06T20:53:29.523Z] TOOL RESULT

```
WP.  I  377,  WH.  I  190,  0.  Szemerenyi  KZ.  70,  65.
keuk-  , leuchten,  hell,  weiß  sein,  glühen'.
Ai.  söcatij  iucyati  ,leuchtet,  glänzt,  glüht,  brennt,  leidet  heftigen  Schmerz, trauert',  iocdyati  ^entzündet,  betrübt;  ist  traurig,  beklagt',  söka-  m.  ,Glut, Flamme,  Schmerz,  Trauer',  suci-  , leuchtend,  glänzend,  rein',  ,^ukrd-,  sukld- ,licht,  weiß,  rein',  sukti-  f.  , Muschel,  Perlenmuschel,  Perlmutter'  (wenn ,*glänzend'),   vielleicht  siüctd-  , sauer'  (wenn  ,brennend  von  Geschmack') ;
av.  saoSint-  , brennend',  sao^ayeiti  ,inflammat  =  incitat',  npers.  söxtan , anzünden,  verbrennen',  av.  upa-suxta-  , angezündet',  ätrd-saoka-  m.  ,Feuer- brand',  np.  sog  , Trauer,  Kummer'  (arm.  sug  , Trauer'  ist  iran.  Lw.);  av. suxra-  ,leuchtend  (vom  Feuer)',  np.  surx  ,rot';
gr.  xuxvog  , Schwan'  als  ,der  Weiße'.
WP.  I  378.    Erweiterung  von  2.  keu-.
keuk-y  kuk-  , durcheinandermischen,  wirbeln'??
Gr.  -avüsd)}'  , Mischtrank',  xüxcrw  , rühre  ein,  mische',  v,vx7]-d^Qov  ,Rührkelle' ; lit.  §dukstas  , Löffel',  siUksmes  , Geröll,  Auskehricht',  HukHüs  ,mit  Spreu oder  Kleie  gemischt'.    Sehr  unsicher. WP.  I  377,  WH,  1  218  f.
598  9
kik-  ,Häher';  Schall wurzel.
Ai.  Ä;iH-,  hihidlvi-  m.  , blauer  Holzhäher'  {l  nicht  zu  c  zur  Festhaltung der  Schallnachahmung) ;
gr.  yiioaa,  att.  x/rra  (*xfXA-a)  , Häher':
ags.  Mgora  m.,  higore  f.  ,picus  (Elster  oder  Holzhäher)',  mnd.  heger n.  , Häher',  ahd.   hehara  , Häher'.
WP.  I  451.
I.  kik-  etwa  ,Riemeii'.
Ai.  sie-  f.,  sikya-  n.  , Schlinge,  Tragband',  säiTcya-  ,damasziert,  eigentl. mit  Schlingen  versehen';
gr.  üiGaaqog  und  xiacfdg  ,Efeu'(?),*
lit.  siJcsnä  , feines  Leder  zur  Verfertigung  von  Riemenwerk,  Riemen'.
WP.  I  451.
2.  kik-  , tröpfeln'.
Ai.  §lkdra-  m.  , feiner  Regen',  silcäyati  ,tröpfelt';   norw.  higla  ,tröpfeln', higl  , feiner  Regen'. WP.  I  451.
kiker-  u.  dgl.  , Erbse';  kaum  indogermanisch.
Arm.  sisefn  , Kichererbse'  (scheint  Jceiker-  oder  Jcoiker-  fortzusetzen);
gr.  (maked.)  y,UeQQOL  (so  für  überliefertes  mßsQQOt  durch  die  alph. Reihenfolge  gefordert)'  (bxQol.  May.sdöveg;  gr.  xgLÖg  , Kichererbse'  (wird aus  ^KLXQiög  dissimil.  sein);
lat.  cicer  , Kichererbse';
[lit.  Jceke  , Traube',  lett.  h'ekars  ds.  scheinen  dagegen  mit  lett.  h'eUis , Dolde,  Traube',  Lituanismus  zu  lett.  cekulis  ,Zopf,  Troddel,  Quaste, Strauß,  Büschel',  cecers  , Krauskopf'  und  cech.  ^eceriti  , struppig  machen, kräuseln'  eine  verschiedene  Sippe  zu  bilden.]
WP.  I  451  f.,  WH.  I  212.
klon-  (kison-?)  , Säule';  nur  arm.  und  griech. Arm.  siun  =  gr.  xlcüv  , Säule'. WP.  I  451.
kiph-  , dünner  biegsamer  Zweig  oder  Wurzelteil'?
Ai.   siphä   ,dünne  Wurzel,    Rute';   gr.  messenisch   xicpog   n.    ^arecpavog'] allenfalls  auch  lett.  sipsna  ,starke  Rute',  lit.  Hpulys  ,Holzspan,  Holzscheit'. WP.  I  452.
599
Jcistä  .geflochtener  Behälter'?
Gr.  y.LGT7]  , Kisten,  Kasten'  (daraus  lat.  cista,  cisterna)] ==  air.  cess  f.  ,Korb,  Hürde'  (vgl.  ro-cess  , wurde  geflochten'),  cisse  ,ge- flochten'  (vgl.  aber  Pedersen  KG.  II  491). WP.  I  452.
jclä-  ,breit  hinlegen,  darauflegen';  klä-to-  ,Deckstein^
Lit.  Jclöju,  Jclöti  ,hinbreiten,  breit  hinlegen',  lett.  hldju,  Jclät  ds.,  lit. JclMas  ,das  Pflaster  im  Hofe',  ü^klodas  , Bettdecke',  paMode  ,Bettlaken' (-d-  aus  einem  d-  oder  c?/i-Präsens  wie:)
abg.  kladq,  Jclasti  ,laden,  legen'  (usw.,  dazu  auch  russ.  kladü  ,ver- schneide') ;
^Präsens  (z.  T.  vielleicht  auch  ursprüngliche  to-Nomina)  in  got.  afhlapan ,überbürden^  aisl.  hlada,  ags.  as.  hladan,  ahd.  hladan  (Partiz.  gihlatan) , aufschichten,  laden';  aisl.  hlad  , Pflaster  im  Hofe^  Stapel,  Haufe',  ags. hlced  n.  , Erdaufwurf,  Haufe',  hlcedel  , Schöpflöffel',  und  vollstufig  (vgl. lit.  klotas)  nisl.  hlöd  Nom.  PI.  ;Herd'  sowie  ags.  hlöd  f.  ,Beute;  Menge, Schar',  anfränk.  hlötha  ,Beute',  mhd.  luot,  md.  lüt  ,Last,  große  Menge, Rotte'.
-to-  oder  -sto-,  -sti-  Nomen  zu  *hlapan  ist  aisl,  hlass  n.  ,Last,  Ladung', agst.  hlcest  n.,  ahd.  last,  PL  lesti  f.  ,Last'.
Sonderstellung  von  ags.  hlöd  f.  ,Raub,  Beute',  hlödere  ,Räuber'  (:  ahd. lander i  flatro',  aisl.  Jilenni  ,Räuber,  Dieb',  hlanna  ,rauben',  germ.  *hlanp-)'j da  auch  mhd.  luot,  md.  lüt,  die  nicht  aus  *Manp-  zu  gewinnen  sind,  die Bedeutung  ,Rotte^  haben,  ist  nur  fürs  Ags.  Zusammenfließen  zweier  ver- schiedener Worte  zuzugeben. '       WP.  1-489,  Trautmann  135  f.
```


## [2026-09-06T20:53:50.646Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 p452 (leaf 461)\" && awk 'BEGIN{RS=\"\\f\"} NR==461' incoming/WLD/WLD_Bd1_pages.txt | head -c 2500"
}
```


## [2026-09-06T20:53:51.293Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"شفش\\|شفشا\\|شفشه\" incoming/BQT/BQT_v3_pages.txt | head -20; echo \"=== MON\"; grep -n \"شفش\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-06T20:53:52.134Z] TOOL RESULT

```
=== WLD Bd1 p452 (leaf 461)
                                   I




452                                             kiph-   — ko-, ke-
(Bucheler Rh. Mus. 62, 476 f., Niedermann IA. 29, 32), xgtog „Kichererbse“
(wird aus *xixgiog oder eher xtxgog diss. sein); lat. cicer „Kichererbse“.
Im Balt, anklingende Formen mit (nach Zupitza KZ. 37, 401 allerdings an
sich als westidg. verstandlichen) Velaren,                      von denen aber nur apr. keekers
„Erbse“      der Bed. stimmt (wohl Lehnwort aus cicer durch dt. Kicher-
                 in
erbse , so Schmidt PI. 177 f , oder allenfalls nacb Trautmann Apr. 355 aus
                                            .


dem ebenfalls entlehnten poln. cieciorka, ciederzyca „Kichererbse“ unter
Anlehnung an ein dem lett. k'ekars entsprechendes Wort). Dagegen lit.
kekS „Traube“ (zur Flexion s. J. Schmidt aaO.), lett. k’ekars ds. (Tertium
comparationis mufite „Rankengewachs“ oder „erbsenartig runde Beere“
sein) scheinen mit lett. k'ekis „Dolde, Traube“ (Zubaty AfslPh. 16, 386),
vielleicht aucb lett. cekulis „Zopf, Troddel, Quaste, StrauB, Buschel“, cecers
„Krauskopf“ (J. Schmidt aaO.), ceeh. cecefiti „struppig machen, krauseln“
(Berneker 38, s. auch 540) eine verschiedene Sippe zu bilden.
                      1



   Ygl. Fick I 3 515, 4 381, Vf. LEWb. 2 u. cicer (die Vermutung yon Ent-
lehnung aus einer siidosteurop. nicht idg. Sprache ist nicht erweislich), Traut-
mann aaO. (Lit.).

kiph- „dunner biegsamer Zweig oder Wurzelteil“.
   Ai. gipha „diinne Wurzel, Rute“; gr. messenisch y.icpog n. „oxecpavog“
(wenn aig. „flechtbarer, geflocbtener Z\veig“; Petersson Gl., 4 298) ; allen-
falls auch (Endzelin KZ. 44, 58)     lett. sipsna „starke Rute“,  lit. sipulfys

„Holzspan, Holzscheit“, doch scheinen diese besser zu skei-p- „spalten“,
u. zw.          dessen palataler Variante skei-p- zu passen.
    Ai. gipha nicht besser (nach Hirt                     BB. 24, 236, Dhlenbeck Ai. Wb. s. v.)
zu qepa-h „Penis“ (s. u. keipo- „Pfahl“) oder (nach Charpentier KZ. 46,
3 Iff.) zu gipra-m „Schnurrbart“, cipra „Kopfhaar, Kopfaufsatz“ (s. u. qaput).


kis-ta „geflochtener Behalter“ ?
    Gr. y.tarrj „Kisten, Kasten“ (daraus lat. cista                  ,
                                                                         cisierna,   s.   Vf. LEWb. 2 s. v.
und gegen Beziehung zu curare auch Glotta 4, 374), vielleicht = air. ain-
ches „fiscina, Brot-korb“ (Fi
```


### [2026-09-06T20:53:52.205Z] TOOL RESULT

```
4653:‏شفشاهنج۱ = این شله‌دا. بر وزن
4664:‏بمعنی شفشاعتج اس تکه آهن سوراخدار استادان‎
4688:شفشه (- آهنج (آهنگه ). اسدی درلت‌فری ‎(Ve)‏ کوید:«شفتاهتم:شکنجه‌بود» و . هر
6651:فرشت )1( شفشة طلا و نقرء را گوبنه و آن
7647:‏شوشه ۴ © بروزن‌خوشه. شفشه‌وسبیکةً
9352:‏۴ 2 شوشه («.م.) ‏ شفشه(«م.) .
10511:۴ - «واخبر کشت از فروغ ‎GED‏ طبرخون وشبگون وزرد وبشفش . . فردوسی طوسی .
41696:مدیوشم ‎ol‏ فيشههيم گاه . اباثرم ‎lS‏ مدیایرریم گاه. همشفشمیذ گاه (آثارالباقیه‌س۲۱4 , ۰۲۲۰
48601:آتشفشان یافت میشود .
49860:‎daly‏ خاکهای آ تشفشانی بسیار حاصلخیز است . رل : کیهان . جغرافیای سیاسی ص ۲۹۵ ورلد:
=== MON
MON_part2.txt:14205:شکل رگه در سنگ‌های آتشفشانی بوجود 
MON_part2.txt:23542:کشفشن: 32-0 (مص‌م.) پرا کنده کر دن» 
MON_part2.txt:36841:اصلی خو بش در حوالی کوه‌های آتشفشان 
MON_part2.txt:92652:دهانه‌های آتشفشانی این عنصر به مقدار زیاد 
MON_part2.txt:93395:بیشتر در لایه‌های آتشفشانی قدیمی تست و 
MON_part2.txt:94441:فشفشه» ینجه یونجه معمولی. زکام یونجه: 
MON_part1.txt:2049:اتنشفشان: 1)0(850-.2 (افا. امر.) آنچه 
MON_part1.txt:22925:کوهی آتشفشانی واقع است که گویند 
MON_part1.txt:50635:آتشفشان: ( کد.) آفتاب. چشمة آفتاب: (کد.) 
MON_part1.txt:77413:ذکر کرده که جهت ساختن فشفشه‌های
```


## [2026-09-06T20:53:59.626Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=4600 && NR<=4700' incoming/BQT/BQT_v3_pages.txt | grep -n \"pdf page\" ; echo \"===ctx\"; sed -n '4640,4700p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T20:54:01.451Z] TOOL RESULT

```
30:[pdf page 63]
98:[pdf page 64]
===ctx

‎SS‏ - بروزن هفته » بضه مانندی‌باشد
آزرسمان که بر دوك ببچیده شود ؟ -

‏شفتیدن؟ عبکر اون بروزن بشنیدن»
پمعی‌شقتن است که خارالیدن - وجراحت کردت
- وتراوسن وچکیدن - و چکالیدن باشد.

‎pd‏ بنتح اول بر وزن ‎GS‏ می
وچوبی باشد که ندافان پنبه را بدان زشدو گرد
آوری و جمم ‎able‏ - و شا درخت را یز
گفته‌اند 1° و نم اول هم‌آمده است.

‏شفشاهنج۱ = این شله‌دا. بر وزن

‏و معتی‌شفتاهنج است و آن ‎Ges‏ آهنی باشد ۷

‎booth A foe

‏که در آن سوراخهای بز رکه و کوچك بتقلوت
کرده‌ياكندوسيم کشان ‎Wh‏ وقره را ازآن‌بکتند
تا بارك ومقتول شود +

‎1 BIG, ‏وزن‎ pe A Lalas
‏بمعنی شفشاعتج اس تکه آهن سوراخدار استادان‎
‏زر کش باشد - و بمعتی حلاج - وکمان حلاجی‎
‏حلاجی هم‌آمده است وآن چوبی‌باشد‎ Lee ‏و‎ -
- ‏میزلله‎ AS ‏که در وقت ینبه زدن بر زه‎
‏و بیعتی شاخار یز بنظرآعده است.‎

‏شقثف - بروزن‌دفرف » شاخ درخت که
کجواج باشد - و ‎aa‏ درخت‌را ی زکویند ‎٩‏ -

‎abd‏ - یکسراول بروزن اصفهشوشة
طلا و قرء راکویند وآن طلار شر# کداخته
است که در ناوچة آهنین ریزند - و بمعنی دوم
‎Wants‏ هم آمده است وآن موی چندی‌است‌از
کل و زلف ممشو قکه برروی و افتاده باشد
و شا درخت بیار از و راست و هموار رالیز
کفته‌اند ؛ و باين معنی بفتح اول هم آمده‌است
‎ney -‏ چوبی که حلاجان پنبه را بدان زند

‎pn ۱‏ چیزیست مانتدشفتالو وییشتر سرخومیید بود.عمجدی(مروزی) گوبد:
باسماع چنگه باش از ‎Kate‏ تا آن ز ‎ahs‏
‏برقاك پروین پدمد ‎wT‏ چوسیمین شفتریگه.» «لت‌فری۷۹۷ ۰ .
۴ ح شفتیدن (هم.) . ۳ - ‎alin sl eae‏ مک در
که ‎dbp‏ دیوار وعمارت ریزند * ۴ ‎Cea) gun‏
‎(Sy) Shish st ©‏ > واژه نامه ‎Ke as = ٩ «fore‏ («.م.) ازء
شفشه (- آهنج (آهنگه ). اسدی درلت‌فری ‎(Ve)‏ کوید:«شفتاهتم:شکنجه‌بود» و . هر
دو ‎ine‏ آمده ‎ay.‏ جح ۷ - حدیده (قرویتی) . ‎A‏ = عتعاهتج ‎(po)‏ :
کوه محروق آنکه همچون زر بشنشاهنگه در
‎yo‏ را ژو در شکنجهٌ حبی خذلان دیده ‎wail‏
‏« خاقانی شروابی ‎HA‏ =
‎٩‏ - ساسکریت ‎shipha‏ و 501008 ‎gy)‏ نهال لیفی با قابل انسناء شاخه) «وبلپلاز
۷۲ ,+

‏* سس شوشه (<م.) ‎ab yt‏ («م.) ‎ody MY‏ خنچه +
[pdf page 64]
-٩ ۳۳

oa) ‏هم‌هست‎ a, ‏رکردآوری‎ J
```


## [2026-09-06T20:54:15.799Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 63\\]/' incoming/BQT/BQT_v3_pages_faseng.txt | tail -30"
}
```


### [2026-09-06T20:54:17.339Z] TOOL RESULT

```
awk: cannot open "incoming/BQT/BQT_v3_pages_faseng.txt" (No such file or directory)
```


## [2026-09-06T20:54:19.581Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && ls && grep -n \"shipha\\|sipha\\|Sipha\" *.txt | head"
}
```


### [2026-09-06T20:54:19.631Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
BQT_v3_pages.txt:4693:‎٩‏ - ساسکریت ‎shipha‏ و 501008 ‎gy)‏ نهال لیفی با قابل انسناء شاخه) «وبلپلاز
```


## [2026-09-06T20:54:23.087Z] TOOL CALL #40: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1272 --image 2>&1 | tail -30"
}
```


### [2026-09-06T20:54:29.953Z] TOOL RESULT

```
- و چکالیدن باشد. که در وقت پنبه زدن بر زه کمان میزنند -
شفْتَه - بروزن هفته » بیضه ماتندی‌باشد و بمعتی شاخار یز بنظرآهده است.
ازرسما ن که بر دوك پیچیده شود ۴ - شفْشف - بروزنرفرف . شاخ درخت که
شفتیدن؟ -بکر اول بروزن بننیدن. | کجواج باشد - و بیخ درخت‌را نی زکویند ‎٩‏ .
بممتی‌شفتن است که خارانیدن - وجراحت کردن شُفْشه *۱ - یکراول بروزن تصفهءشوعه
- وتراویدن وچکیدن - و چکانیدن باشد. طلا و نقره راکویند وآن طلا و اضر کداخته
شفش - بفتح اول بر وزن کفش ۰ ی است که در تاوچهٌ آهنین ریزند - و بمعنی دویم
وچوبی باشد که ندافان پنبه را بدان زنندو کرد | خفچه۱۱ هم آمده است وآن موی چندی است از
آوری و جمع نمابند - و شاخ درخت راانیز | کاکل و زلف موق که برروی او افتاده پاش
گفته‌اند 6 ؛ و هم اول هم آمده است. و غاخ درخت بسیار #ازد و راست و هموار رالیز
شفشاهنج! « باشین لقطه‌دار» بر وزن | کفته‌اند ؛ و باین معنی بختح اول هم آمده‌است
و معنی‌شفتاهنج است و آن تخنةٌ آهنی باشد ۷ | - وبمعنی چوی ی که حلاجان پنبه را بدان زنند
۹ <هشفترنگه, چیزیست ماتندغفتالو وبیشتر سرخ‌وسپید بود.عصجدی(مر وزی) کوید:
باسماع چنگه پاش از چاشتگه نا آن ز مايك
برفلك پروین پدید آید چوسیمین شفترنگه.> ‏ «لفت‌قری ۲۹۷ ۶ ۰
۲ <* شفتیدن (هم.) . ۴ - غفته » بکس اول » دوغاب: آهکه وستگریزه

که دریایهٌ دیوار وعمارت ریزند . ۴ عفن (هم) .

* -_طبری 581510 (تر که) « واژه نامه ۵۰۰ - ۹ -< خعفعاهنگه (همم.) از
شنعه ۳ آهنج (آهنگه ). اسدی دراغت‌فری (س۷۳) کوید:«شفشاهنج,شکنجه بود» وظ . هر

دو معني آمده برك : حه. ۷ - حدیده (قزوینی) . -- شفعاهتج (ه.م.) :

کوه محروق آنکه همجون زر بشفداهنکه در
دیو را زو در شکنجهٌ حبی خذلان دیده اند .
۶ خاقانی شروانی ۹۸ ۰
‎٩‏ - ساسکریت 510182 و 5010802 (بیخ تهال لیفی با قایل انختاء شاخه) «وپلپاه‌ز
دنه ۹ نشرعه (م.) * شیوشه («م.) ۱ رف خفچه ۰
```


## [2026-09-06T20:54:37.496Z] TOOL CALL #41: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1272 --image 2>&1 | head -20"
}
```


### [2026-09-06T20:54:39.102Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1272.png
REF: BQT:1272  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 63  OCR-lang: fas

عتل ۱ ۱۱۷۳
شفتالو و زردآلو را چون باهم پیوند کتند ان که در آن سوراغهای بز رکه و كوچك بتفلوت
میوه حاصل شود ‎٩‏ - ۱ ۱ کردهباغندوسیم کشان طلا ونقره را ازآن‌بکشند

شفتل - بالام وح ر کت مجهول ,کیاحی | تا باريك ومقتول شود .
است که آنرا سه برکه کوبند و من‌کل آن | شفشاهنگ ۸ - بر وزن رنگارنکه .
است . بممنی غفعاهنج است که آهن سوراخ‌دار استادان
شفتن؟۲ «بکی اول بروزن کشتن, بمعنی زر کش باشد - و بمعنی حلاج - وکمان حلاجی
خارانیدن - وجراحت کردن - ولراوبدن‌وچکیدن | - و مشتَةٌ حلاجی هم‌آمده است وآن جوبی‌باشد
- و چکالیدن باشد. که در وقت پنبه زدن بر زه کمان میزنند -
شفْتَه - بروزن هفته » بیضه ماتندی‌باشد و بمعتی شاخار یز بنظرآهده است.
ازرسما ن که بر دوك پیچیده شود ۴ - شفْشف - بروزنرفرف . شاخ درخت که
شفتیدن؟ -بکر اول بروزن بننیدن. | کجواج باشد - و بیخ درخت‌را نی زکویند ‎٩‏ .
بممتی‌شفتن است که خارانیدن - وجراحت کردن شُفْشه *۱ - یکراول بروزن تصفهءشوعه
- وتراویدن وچکیدن - و چکانیدن باشد. طلا و نقره راکویند وآن طلا و اضر کداخته
شفش - بفتح اول بر وزن کفش ۰ ی است که در تاوچهٌ آهنین ریزند - و بمعنی دویم
وچوبی باشد که ندافان پنبه را بدان زنندو کرد | خفچه۱۱ هم آمده است وآن موی چندی است از
```


## [2026-09-06T20:54:41.367Z] TOOL CALL #42: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1272.png"
}
```


### [2026-09-06T20:54:41.939Z] TOOL RESULT

```

```


## [2026-09-06T20:54:41.936Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T20:55:20.144Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON شفشف/شفشاهنگ ==\"; grep -n \"شفشف\\|شفشاهنگ\\|شفشاهنج\\|شفشه\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt | head; echo \"== MON ساس ==\"; grep -n \"ساس:\\|ساس :\\|ساس(\" MON_part1.txt MON_part2.txt | head; echo \"== MON سیف ==\"; grep -n \"سیف:\\|سیف :\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-06T20:55:20.258Z] TOOL RESULT

```
== MON شفشف/شفشاهنگ ==
MON_part2.txt:94441:فشفشه» ینجه یونجه معمولی. زکام یونجه: 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:94441:فشفشه» ینجه یونجه معمولی. زکام یونجه: 
MON_part1.txt:77413:ذکر کرده که جهت ساختن فشفشه‌های 
MON_part1.txt:85534:شفش: 5اه [قس. شفشه» شوشه] (.) شاخ 
MON_part1.txt:85537:شفشه: (0-)8000 (.) شوشة طلاو نقره. 
MON_part1.txt:85541:شفشه: (8280)»0 (.) موی چندی از کاکل 
MON_part1.txt:85645:شفشفه: ()34 [ع. شقشقة ] (.) چبزی 
MON_part1.txt:86654:شفشه» شو شه. 
MON_part1.txt:87270:شوشه: (م)42؟ [- شفشه] (.) طلا یا نقره 
MON_part1.txt:87272:شفشه. هر چیز شبیه به شمش. هر چیز 
== MON ساس ==
MON_part2.txt:55369:مساس: 115 [ع. (مص م.) مس کردن» 
MON_part1.txt:7936:احساس: عقعت [ع ۰] (مسصم ۰ دریافتن» 
MON_part1.txt:10830:دیوار» شالده» بن» بی. اس اساس: بنیاد و باية 
MON_part1.txt:10861:اساس: 5 [ع.] (.) پی؛ پابه» بنباد» 
MON_part1.txt:53253:خساس: ۳ [ع.] (ص.) حس کننده» 
MON_part1.txt:73587:قرط ما ناساس :() رن ]شش 
MON_part1.txt:73939:ساس: عقه [یید؟] (ا.) (جاد.) حشره‌ای است 
== MON سیف ==
MON_part1.txt:82277:سیف: 2256۵ [ع.] () شمشیر) ج.
```


## [2026-09-06T20:55:22.991Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '73935,73950p' MON_part1.txt; echo \"-----\"; sed -n '82274,82286p' MON_part1.txt; echo \"-----\"; sed -n '85530,85545p' MON_part1.txt"
}
```


### [2026-09-06T20:55:23.082Z] TOOL RESULT

```
سازه: (#-)متقه (.) جاروب؛ جارو. 

سازه: (م)ممةه (رض.) (نو.) عامل» فاکتور. 
ساس: عقه [یید؟] (ا.) (جاد.) حشره‌ای است 
از راسته نیم‌بالان که رنگ قرمز مایل به 
قهوه‌یی دارد و بال‌هاش از بسن رفته است. 
این جانور روزها در شکاف‌های اشیاء چوبی 
و درز تشک و لحاظ سخفی می‌شود و 
شب‌ها خارج می‌گردد و به انسان نیش 
می‌زند و خون وی را می‌مکد. بوی بدی از 
آن استشمام می‌شود. تولید مثلش بسیار 
سریع است. ساس درختی: (جاذ.) سحشره‌ای 
است از راستة نیم بالان که در حقبقت 
گونه‌ای از سن می‌باشد و شکل و اندازه‌اش 
نیز به اندازةٌ سن است ولی بر خلاف سن که 
-----
(مصل.) غلبه یافتن» تسلط یافتن» چیره 
کشتن . (امص ۰( غلبه» تسلط» چیر گی. 
سیغ: * و [- هس ] رف نک نغز»ه خوب. 
سیف: 2256۵ [ع.] () شمشیر) ج. 
سیوف. 
سیفلیس: ۰18 () (پز.) مرضی عفونی و 
ساری که به ارث بطور مادرزادی به افراد 
نتقل می‌شود. عامل این ناخوشی باسیلی 
است مارپیچی بنام ترپونم پال. این مرضص 
بطور مستقیم از افرادمبتلی به فراد سالمقابل 
سیفو ر؛ .)22۷60۲ (ا.) بافتة اسر شمی 
لطیف (مانند دیا و اطلس). 
سیفون: 0 (.) لولهٌ خمیده‌ای به شکل 
-----
شفش: 5اه (.) نی و چوبی باشد که ندافان 
پنبه را بدان زنند و گردآوری کنند. 


شفش: 5اه [قس. شفشه» شوشه] (.) شاخ 
درخت. شوشه. 

شفشه: (0-)8000 (.) شوشة طلاو نقره. 
شاخ درخت بسیار نازک و راست و هموار. 
چوبی که حلاجان بدان پنبه زنند. 

شفشه: (8280)»0 (.) موی چندی از کاکل 
و زلف معشوق که بر روی او افتاده باشد. 
شفع: اه [ع.] (.) زوج (عدد)» جفت ج. 
اشفاع» شفاع.
```


## [2026-09-06T20:55:32.829Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"سيف\\|السيف\" TAD_pages.txt | head -20"
}
```


### [2026-09-06T20:55:32.877Z] TOOL RESULT

```
1015:  ‫معناه اسقف‬          ‫م‪0‬‬‫وثاني ‪5‬‬         ‫خوري اسيف و‪3‬خوريسمبوس ‪-‬‬
1252:     ‫اللانينية م‪ 15‬أي سيف البحر‬                 ‫ا‬                   ‫و‪3‬الي‬
1507:                        ‫سيف ‪ -‬ووناني ‪5‬وألى وهو القاضب والقاطع والماضي‬
1967:                      ‫« تر ند » أحيوهر السيف ووشيه‬                   ‫اافرن‬
2295: ‫ن الفارسيفبو متحوت مقر العرنى ومانالفارسىي ععى صاحت‬
2724:                               ‫أما قندتية‪ 8‬الايطالية قمناها ساحل البحر وسيفه‬
```


## [2026-09-06T20:55:39.747Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=1480 && NR<=1530' TAD_pages.txt | cat -A | grep -n \"pdf page\" ; echo \"---ctx\"; sed -n '1495,1520p' TAD_pages.txt; echo \"=== leaf計\"; python3 -c \"\nd=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\nfor ln in (1015,1252,1507,2295):\n    off=sum(len(l)+1 for l in lines[:ln-1]); print(ln,'leaf',d[:off].count('\\f'))\n\""
}
```


### [2026-09-06T20:55:41.849Z] TOOL RESULT

```
---ctx

                                                 ‫ل‬                       ‫دي‬

                            ‫‪3‬‬   ‫‪١‬‬   ‫‪5‬‬   ‫‪١‬‏‬           ‫‪1‬د‬               ‫اذا‬   ‫ود‬




                ‫سرس ‪ -‬ووثانى ‪ 27165‬معنأه سلسلة وزمام وحبل مرادفه نسعة‬
                                                          ‫و‬   ‫‪7‬‬   ‫‪4‬‬
                                        ‫لوم ل‬
                                                                                     ‫‪-‬‬
                        ‫سيف ‪ -‬ووناني ‪5‬وألى وهو القاضب والقاطع والماضي‬

                           ‫سمكارة ‪ 1‬اسيانى ‪0502‬هاه وهو اقافة من اتتبخ‬

‫سيمة وسماء وسيمياء ن‪-‬ونانى ‪ 8016853‬معناه علامة ونوافقه فى العربية‬
                                                                               ‫واسمسمة‬
‫سيمونية س نسبة الى سيمون أي سمعان الساحر وبراد ما التجارة بالاشياء‬
                                                                    ‫المقدسة لاجل الربح‬
‫ر‪-‬يب عاملياعفنرنسية والاصح قيما مسب الاصلاليوناني‬
                                                ‫ع‪-‬‬‫تما‬
                                                    ‫سي‬
                          ‫غ‪ 01‬ومعناه حركة مرادفه الصور المتحركة أوالاشباح‬

                                       ‫دش »‬
=== leaf計
1015 leaf 28
1252 leaf 34
1507 leaf 42
2295 leaf 62
```


## [2026-09-06T20:55:49.189Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (41,42,43,79,80,81,82,83):\n    t=d[i][:300].replace('\\n',' | ')\n    print(i, repr(t[:280]))\nEOF"
}
```


### [2026-09-06T20:55:51.214Z] TOOL RESULT

```
41 '\u202bوهو رياب\u202c      \u202bستعاير وستطور ت في التركية« سانطور » وناني\u202a161\u202c\u202c |  |                                                                       \u202bلهعشرة أوتار\u202c |   \u202bجرم\u202c |     \u202bرنه\u202c |       \u202b\u202a6\u202cأي\u202c |         \u202bفوت\u202c |           \u202bشمعار\u202a -\u202cاشوري مركب من « شينا» أي اثنان و « نار\u202c |       '
42 '                                        \u202bلوم ل\u202c |                                                                                      \u202b\u202a-\u202c\u202c |                         \u202bسيف \u202a -\u202cووناني \u202a5\u202cوألى وهو القاضب والقاطع والماضي\u202c |  |                            \u202bسمكارة \u202a 1\u202cاسيانى \u202a0502\u202cهاه '
43 '                                  \u202bأبنت\u202c |  |  \u202bفارسي «شاه ثراه\u202a 6\u202cأى ملك البقول وهو نبات ورقهنافم للجرب\u202c         \u202bشاهترج\u202c |      \u202bوهو المزمار من قصب وغيره ينفخ فيه\u202c      \u202bفياه \u202a --\u202cعامي بوناني \u202a2\u202c\u202c |  |                      \u202bشور \u202a -\u202cعبراني « شلوفار \u202a 6\u202cمعناه جيل وهو البوق\u202c |    '
79 ' \u202bالعرب اليكل مجازاً الضخم من الحيوان فقالوا فرس هيكل وللطويل من النبات\u202c | \u202bأما استعاله فى حلبعمنى المذبح فخهطواء فاحش ومخالف المعنى الرمزي الذ\u202a:\u202c\u202c | \u202b«ل \u202a 6\u202cالذييستعمله بعضهم فزمىاتنا عه\u202c    \u202bينك\u202c \u202bهىا\u202c \u202bللهكانبايءدة \u202a .\u202cعل\u202c\u202bيساتعم\u202c |                \u202bعظام المت انما هو تعربب \u202a2\u202cم'
80 '\u202bبانسون ب وثانى «مونسة وهو نبات زهره اسن طن الرانحة ويستقطرون\u202c |  |                                                           \u202bققيمعنه\u202c |                                                                 \u202bالنعسر\u202c |    \u202bالصثراء وهو يسرّب اصفرار الجلد\u202c   \u202bركان ب وونانى \u202a 80:611\u202cمعناه'
81 '\u202bافسىه \u202a :\u202cالبرهان يبان الحجة مالنبرهرهة وهي البيضاء\u202c  \u202bسري\u202c |                                                      \u202bأمخش\u202c |                                                         \u202bقال الز\u202c |  \u202b\u202a 0\u202cاري كااشتق السلطان\u202a.\u202cهنالسليط لاضاءته ق\u202a.\u202cلت\u202a :\u202cالسلطان لأفرظامى\u202c   \u202b\u200f\u202a١\u202c\u202c | \u202bوهو'
82 '                                  \u202bلامؤلف نسه\u202c | \u202b\u202a-\u202cتاناتةأتصوع قا تتساعق أمظ\u202c |                          \u202bبع\u202a2\u202cصده\u202a 1\u202cت\u202c        \u202b\u202a1\u202c\u202c                       \u202b\u202a“. 51\u202cأ\u202c |  \u202bملعم \u202a1\u202cام \u202a0\u202c\u202c   \u202bب\u202a,\u202cأناءلاطأرا \u202a -\u202cناذأ اده \u202a 311\u202cتنا "امادع بعول\u202c   \u202b\u202a1\u202c\u202c     \u202b\u202a11. 01\u202c\u202c |    \u202bومط\u202c |  '
83 '                                 \u202b\u202a0000\u202c\u202c |  |  |  |  |   \u202bاملب فاليمأأوس من \u202a.\u202cتن الاغة العربية والاصطلاحات\u202c |                                                 \u202bطعج\u202c |                                                   \u202bامولس م\u202c |                                                   '
```


## [2026-09-06T20:56:07.351Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\noff=sum(len(l)+1 for l in lines[:2723]); print('line2724 leaf',d[:off].count('\\f'))\nprint('total leaves',d.count('\\f')+1)\n\" ; echo \"--- leaf 84,85\"; python3 -c \"\nd=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (76,77,78): print(i, repr(d[i][:250].replace(chr(10),' | ')))\n\""
}
```


### [2026-09-06T20:56:09.295Z] TOOL RESULT

```
line2724 leaf 75
total leaves 87
--- leaf 84,85
76 '                                 \u202bيي للد\u202c   \u202bسس\u202c |  |  |  |  | \u202bاصل سكن معبد أي مكان الرحال في\u202c |                              \u202bانالهلفي\u202c |                                     \u202b\u202a-\u202cذلى وموم مع\u202c |                                                \u202bنأووس و\u202c |      \u202bالكنيسة '
77 '                 \u202bوي\u202c |                   \u202bعبرشت \u202a -\u202cفارسي م ركبمننمأي نصف وبرشمتشأي\u202c |                                            \u202b\u202a -- 0\u202cفارمي « ثامه » معناه كتاب\u202c |  |     \u202b\u202a3\u202cلوىاهط ( ولشا )\u202c |                    \u202b\u202a1\u202cب\u202a:\u202cة ا\u202c |                         \u202b»هو ل'
78 '                                          \u202b\u202a6» 8 5\u202c\u202c |  |                    \u202bسكمس\u202c |                       \u202bونالى وهاه وهو الطنياوة والدارة حولالقمر واك\u202c                   \u202bهالة \u202a-\u202c\u202c |  |  | \u202bوعتكر دقاكنة\u202c          \u202bان\u202c       \u202bصعغير من\u202c   \u202bحرن\u202c    \u202bوهو\u202c       \u202b'
```


## [2026-09-06T20:56:16.498Z] TOOL CALL #49: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T20:56:16.507Z] TOOL RESULT

```


```


## [2026-09-06T20:56:22.269Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1e",
 "prompt": "Give the full reconstruction entry: the PIE demonstrative *ḱe / *ḱi / *ḱo \"this\", its meaning, and all listed descendants (Latin cis/citer/ce-/ceterus, Germanic *hi- > English he/him/his/her/here/hence/it/hither, Hittite ki, Greek, Balto-Slavic). Quote the etymology/notes sections."
}
```


## [2026-09-06T20:56:24.474Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BE%CE%AF%CF%86%CE%BF%CF%82",
 "prompt": "Give the full Ancient Greek entry for ξίφος: meaning and the complete etymology section, including any mention of Pre-Greek origin, Beekes, Egyptian sfj.t, Arabic سيف sayf, Mycenaean qi-si-pe-e, and Chantraine. Quote it."
}
```


### [2026-09-06T20:56:29.889Z] TOOL RESULT

```
# Proto-Indo-European *ḱe Demonstrative Particle

## Reconstruction Entry

**Form:** *ḱi- ~ *ḱe- ~ *ḱo-* (or *-ḱe*)

**Meanings:** 
1. "Deictic particle, here"
2. "Post-positional demonstrative particle, this"

## Usage Notes

The particle functioned as an indeclinable form in Proto-Indo-European. Later, "some daughter languages, particularly Balto-Slavic, Germanic and Armenian added pronominal inflection later." The entry notes this parallels particles like *de, *h₂ew, and *gʰe in gaining grammatical inflection across descendant languages.

## Documented Descendants

**Anatolian:** Hittite ki-i

**Balto-Slavic:** Lithuanian šè ("look there"); Old Church Slavonic се (se, "behold")

**Greek:** Epic Greek κε (ke); Ancient Greek σήμερον (sḗmeron, "today")

**Italic:** Latin compounds including hic, haec, hoc; Faliscan hac, hec

**Germanic:** English he, him, his, here, hence (via Proto-Germanic *hē₂r)

**Celtic:** Primitive Irish koi ("here")

The entry demonstrates widespread reflexes across Indo-European branches, confirming this particle's foundational role in demonstrative systems.
```


### [2026-09-06T20:56:31.302Z] TOOL RESULT

```
# Ancient Greek Entry for ξίφος

## Meaning
**ξῐ́φος** (xĭ́phos) n — "sword" (the short, straight, double-edged sword of Iron Age and Classical Antiquity)

## Etymology Section

The entry states the word was "Already in Late Mycenaean Greek (Ta-716 from Pylos), attested in the dual _𐀥𐀯𐀟𐀁_ (qi-si-pe-e, 'two swords')."

Regarding origin: "Probably of Pre-Greek origin, related to and perhaps borrowed from Egyptian _zft_ ('sword, knife')."

The text presents an alternative theory: "If the Greek isn't borrowed directly from the Egyptian, perhaps both are from a Semitic word related to Ge'ez _ሰይፍ_ (säyf), Arabic _سَيْف_ (sayf), and Hebrew _סַיִף_ (sayip̄) or from a Libyan or 'Sea Peoples' word."

**Note:** The page cites Beekes (2010) in the References section but does not quote Chantraine directly in the main etymology section provided.
```


## [2026-09-06T20:56:43.096Z] TOOL CALL #52: Bash

```json
{
 "command": "pdftoppm -f 267 -l 267 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg267 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T20:56:45.371Z] TOOL RESULT

```
total 2136
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 16:56 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    242 Sep  6 16:55 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb  95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb  43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb  23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb  10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb  63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb  11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb  10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb  14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb  25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb 105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb  92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82276 Sep  6 16:46 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb  87489 Sep  6 16:55 pg270.png
```


## [2026-09-06T20:56:49.578Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg267.png"
}
```


### [2026-09-06T20:56:50.097Z] TOOL RESULT

```

```


## [2026-09-06T20:56:50.094Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T20:57:06.807Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ceterus",
 "prompt": "Give the Latin entry for cēterus / cētera: meaning and full etymology (analysis as *ke- + *eteros, PIE *ḱe + *e-tero-, and the phrase et cetera). Quote the etymology."
}
```


## [2026-09-06T20:57:08.243Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D8%B3",
 "prompt": "Give the Persian entry for ساس (sās) 'bedbug': its meaning and full etymology section (any Middle Persian, Proto-Iranian, or Indo-European reconstruction, Armenian ցեց, Greek σής, Ossetian). Also give any Arabic entry for ساس if present."
}
```


### [2026-09-06T20:57:11.924Z] TOOL RESULT

```
# Latin: cēterus / cētera

**Meaning:** The adjective cēterus means "the other, remainder, rest" and can also mean "besides" or "also." It functions as a first/second-declension adjective with feminine form cētera and neuter form cēterum.

**Etymology Analysis:**

The word derives from Proto-Italic *ke-eteros, composed of two elements:

1. *ke ("here") - from Proto-Indo-European *ḱe
2. *eteros ("other") - from PIE *h₁éteros

**Direct Quote:**
"From Proto-Italic *ke-eteros, from *ke ('here') +‎ *eteros ('other')."

The famous English phrase "et cetera" (meaning "and the rest") preserves this Latin word, appearing in the derived terms as "et cētera."
```


### [2026-09-06T20:57:15.490Z] TOOL RESULT

```
Based on the content provided, I cannot give you the Persian entry for ساس meaning 'bedbug' because **the web page shown does not contain a Persian section**. 

The page displays entries for:
- **Arabic**: ساس (sāsa) - a verb meaning "to direct, govern, rule, manipulate, manage, cox, steer"
- **Kashmiri**: ساس (sās) - the numeral "thousand"
- **Urdu**: ساس (sās) - a noun meaning "mother-in-law"

While the page header indicates "8 languages" with links to other Wiktionary editions (including فارسی/Persian), the actual Persian entry content is not included in this document. To find the Persian entry with etymological information about the bedbug meaning, you would need to visit the Persian Wiktionary directly.
```


## [2026-09-06T20:57:21.577Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN ==\"; grep -n \"Wanze\" HRN.txt HUB.txt | head; echo \"== ARY latin index sas ==\"; grep -n -i \"^SAS\\|ساس\" incoming/ARY/ARY_latin_index_pages.txt | head; echo \"== ARY pages ساس ==\"; grep -n \"ساس\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-06T20:57:21.654Z] TOOL RESULT

```
== HRN ==
== ARY latin index sas ==
803:Sassen Vpn OU} 99 Ab BS (ole gal 90 lel; EAS ISy FEI om) oF
846:Sasa ly age Ct aw Ley shel g eKb slash lebih GI sy
1066:SASL LL! gerlam ob 43 (ACHILLES) eT ely) yo abso oul Sop ote
1213:Sash yl ME yeu Serabj go ghajly gyealt SeuiglSouieo Wl
== ARY pages ساس ==
102:ساسکریت در هندوستان و (بسه طور نادرتر) برای اشاره به زبانهای اییرانی و هندی
728:ساسانی و چند دهه‌ی اول و دوران اسلامی بود. در اثر آمیزش شمار زیادی از واژه‌های عربی (و بعداً ۱
791:ژرمنی نوین نقش اساسی دارد. از قرون وسطی به بعد متون زیادی به انگلیسی کهن و آلمانی کهن و
953:رسید که اساس فرهنگك و جامعه‌ی هند و اروپایی بر سه انديشه استوار است: ۱-روحانی و یزدانی ۲-
988:(81371۸86/3) گزارش می‌دهند که حتی در قرن سوم بیش از میلاد نیز رومیان هنگام احساس خطر
1059:شامان بی لیاقت نقش اساسی داشتند. مجلس سنای روم باستان (57381۸7 173۳) و شورای گروسیا
1149:ساسانیان (۹۵۱-۲۲۴ میلادی) به رشته‌ی تحریر درآمده است.
1154:در دوران اشکانیان و ساسانیان زبان‌های ایرانی کهن به تدریج تبدبل به زبان‌های ایرانی میانه
1864:ساسکریت (6۸(/96/7: 1250873۸ را
1986:ساسکریت رازه اد سا پرتغالی "(۳0877010832): (شاید) :۹ ۱7 :۰.۹8۱
```


## [2026-09-06T20:57:23.941Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD/NYB sas ==\"; grep -n \"^sās\\|sās \\|sāsak\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head; echo \"== SOD ==\"; grep -n \"bug\\b\" SOD.txt | head -5; echo \"== ISS ==\"; grep -n \"bug'\" ISS_alt_DKS.txt | head -5"
}
```


### [2026-09-06T20:57:24.018Z] TOOL RESULT

```
== PHD/NYB sas ==
PHD.txt:4802:sāstārīh
NYB_vol2_glossary.txt:3408:sāstārēh bad domination, tyranny 109%.
== SOD ==
== ISS ==
961:üspar- 'tread', Z 22:147 Jseímu üspidà bräyünu '(the horse) treads lightly, pleasantly’; Z 23:153 [l| va aspude balysi 'the Buddha trod (on the stairway)’; Z 23:169 samu balysi üspude fando 'the Buddha trod on the ground’. Noun see äspara- ‘path’. With other preverbs: JS 7у2-3 paspudamdá tvünai brrimha ‘they trod upon your back’; JS 3313 vaspudai saysdá beda ' you trod upon the snakes’; Sid. 2v3 sästrrä Муа haspara, BS tantra-paddhati- ' path of the treatise’. From spar- ‘to tread, trample’, Av. jrasparat, visparat, Sogd. 'nipr- 'to step’, prip'r ‘kicking (?)', pnipr'y ‘to kick’, Вір'ту 'sole of foot’, pišpry ‘arrangement’, Sogd. Chr. рортіу ‘remains’, Sogd. Man. pipr- ' to fix’, pip'ryy ' rush forth’ ; M.Pers. T. nyspwrd ‘trodden down’, BSOAS 12, 1947, 46:46 an'n "шп пуғрита "yrp'y'n bug'n ‘І shall smite them and their oppressed, trampled servants’; pryspr- 'to tread’ (B505 9:86); Zor.P. spartan, spurtan, vispurt, N.Pers. sipardan ‘to tread’; Waxi naspar-: naspart ‘to tread down’ (IIFL 2:532; 473), bisper ‘kick’, биупї, RoSüni, Хой bispar, Огоҝогї baspür, Yazg. baspur; Sarikoli (Shaw) naxpor- ; naxpug, (Paxalina) zaxpe(dz)-: парид ‘to tread; N.Pers. naspür ' grape-treading place’. IE Pok. 992 sp(/)er-, O.Ind. sphurdti ‘kick, hurry’, redupl. aorist apaspharili, intens. pharpharāyate, Greek стгсірсо' jump ', Lat. зрели, spratum. O.Norse sperna ‘kick’, Lit. spiriti, spirti ' kick, press".
```


## [2026-09-06T20:57:31.840Z] TOOL CALL #58: WebSearch

```json
{
 "query": "Persian ساس sās bedbug etymology Proto-Iranian Armenian ցեց Greek σής moth"
}
```


## [2026-09-06T20:57:34.083Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%B3%D5%A5%D5%B3",
 "prompt": "Give the Armenian entry ճեճ or ցեց (cec) 'moth, mite': meaning and etymology, including any Indo-European comparison with Greek σής and Persian."
}
```


### [2026-09-06T20:57:36.111Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:57:46.291Z] TOOL RESULT

```
Web search results for query: "Persian ساس sās bedbug etymology Proto-Iranian Armenian ցեց Greek σής moth"

Links: [{"title":"Bedbug - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/bedbug"},{"title":"Proto-Iranian language","url":"https://en.wikipedia.org/wiki/Proto-Iranian_language"},{"title":"INSECTS - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/insects/"},{"title":"List of moths of Iran","url":"https://en.wikipedia.org/wiki/List_of_moths_of_Iran"},{"title":"Bedbug in Persian? How to use Bedbug in Persian. Learn Persian","url":"https://wikilanguages.net/Persian/Bedbug.html"},{"title":"bedbug - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/bedbug"}]

The search results don't contain specific etymological information connecting the Persian word "ساس" (sās) for bedbug to Proto-Iranian, Armenian, or Greek forms with the meanings you mentioned. Let me search more specifically for this etymological connection:

Links: [{"title":"sas - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/sas"},{"title":"Armenian Etymology With English Cognates and PIE Roots","url":"https://www.arak29.org/wp-content/uploads/2019/04/Armenian-Etymology-1.pdf"},{"title":"Around the World in 1001 Words - Keghart","url":"https://keghart.org/around-the-world-in-1001-words/"},{"title":"(PDF) Ancient Egyptian and Armenian (as an Indo-European language) Probable Cognates: Preliminary Research","url":"https://www.academia.edu/3851142/Ancient_Egyptian_and_Armenian_as_an_Indo_European_language_Probable_Cognates_Preliminary_Research"},{"title":"Sasun (historical region)","url":"https://en.wikipedia.org/wiki/Sasun_(historical_region)"},{"title":"When Similar Means Different: Evaluating LLMs on Arabic--Hebrew Cognates","url":"https://arxiv.org/pdf/2606.13218"},{"title":"bedbug - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/bedbug"},{"title":"Essentials 1 – Cognates – Armenian Church Resource Page","url":"https://arak29.org/gotoroot/essentials-1-cognates/"}]

Let me try a more targeted search for the specific etymological connection you're asking about:

Links: [{"title":"سوس - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%B3"},{"title":"σής - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/%CF%83%CE%AE%CF%82"},{"title":"σής - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CF%83%CE%AE%CF%82"},{"title":"Strong's Greek: 4597. σής (sés) -- Moth","url":"https://biblehub.com/greek/4597.htm"},{"title":"Strong's Greek: 4597. σής (sēs) -- a moth","url":"https://openbible.com/strongs/greek/4597.htm"},{"title":"moth - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/moth"},{"title":"G4597: σής (sḗs) - Strong's Greek Dictionary","url":"https://www.sermonindex.net/strongs/greek/g4597/"},{"title":"σής | Bill Mounce","url":"https://www.billmounce.com/greek-dictionary/ses"},{"title":"Mothax","url":"https://en.wikipedia.org/wiki/Mothax"},{"title":"Kata Biblon Wiki Lexicon - σής - moth (n.)","url":"https://lexicon.katabiblon.com/index.php?lemma=%CF%83%E1%BD%B5%CF%82"}]

Based on the search results, I found relevant etymological information about the terms you mentioned. Here's what I discovered:

## Etymology Connection

The moth term appears loaned in Ancient Greek σής (sḗs) and Old Armenian ցեց (cʻecʻ). Additionally, the Greek word is a Semitic loanword, found as Aramaic סָסָא (sāsā, "moth"), Hebrew סָס (sās, "moth"), Akkadian sāsum ("moth"), and Arabic سُوس (sūs, "moth-worm").

This indicates that the Persian word ساس (sās) for bedbug shares etymological roots with other Indo-European and Semitic languages through a Semitic loanword that was borrowed into Greek and Armenian. The Greek σής is apparently of Hebrew origin.

The search results confirm that this word family (referring to moths and similar insects) spread across multiple language families through borrowing, connecting Persian, Armenian, Greek, and the original Semitic languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T20:57:53.530Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%AE%CF%82",
 "prompt": "Give the Ancient Greek entry σής (sḗs) 'moth': meaning, declension (genitive σεός/σητός) and the full etymology section verbatim, including any mention of Semitic loanword, Akkadian sāsum, Hebrew סָס, Aramaic, Arabic سوس, Old Armenian ցեց, and Persian."
}
```


## [2026-09-06T20:57:54.641Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%B3",
 "prompt": "Give the Arabic entry سُوس (sūs) 'moth-worm, weevil': meaning and full etymology, including any Semitic comparisons (Akkadian sāsu, Hebrew סָס, Aramaic), and whether Persian ساس is mentioned."
}
```


### [2026-09-06T20:58:01.117Z] TOOL RESULT

```
# Ancient Greek σής (sḗs) - Moth

## Meaning
The term denotes a "moth," with synonyms including ἠπίολος (ēpíolos) and φάλαινα (phálaina).

## Declension
The noun displays irregular declension patterns:
- **Genitive singular**: σεός (seós) in Attic, or σητός (sētós) in later forms
- **Nominative plural**: σέες (sées) in old declension; σῆτες (sêtes) in third declension

## Etymology
The source material states: "A Semitic loanword, found as Aramaic סָסָא / ܣܳܣܳܐ (sāsā, 'moth'), Hebrew סָס (sās, 'moth'), Akkadian 𒌨𒈨 (sāsum, 'moth'), Arabic سوس (sūs, 'moth-worm')."

The content provided does not include references to Old Armenian ցեց or Persian etymological connections.
```


### [2026-09-06T20:58:03.162Z] TOOL RESULT

```
# Arabic Entry: سُوس (sūs) - Moth-worm, Weevil

## Meanings
The word has multiple related definitions: "maggot, moth-worm, woodworm, curculio, weevil," "mite," "rot/decay," and bacteria affecting teeth.

## Etymology
The term is "typically declared as inherited from Proto-Semitic *sūs- ('moth; insect especially one that bites or chews up materials')," which derives from Proto-Afroasiatic *suʔw-.

## Semitic Comparisons
The entry documents cognates across ancient languages:
- **Akkadian**: sāsum (moth; biting insect)
- **Hebrew**: סָס (sās)
- **Jewish Babylonian Aramaic**: ססא (sāsā)
- **Classical Syriac**: ܣܣܐ (sāsā)

It also notes related terms in Ge'ez, Amharic, Tigrinya, and Tigre, indicating this root is widespread in Afroasiatic languages.

## Persian Connection
The provided content does not mention a Persian term ساس in connection with this Arabic entry.
```


## [2026-09-06T20:58:12.506Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D6%81%D5%A5%D6%81",
 "prompt": "Give the Old Armenian / Armenian entry ցեց (cʻecʻ): meaning ('moth') and the full etymology section verbatim, including any Semitic loanword hypothesis, comparison with Greek σής, Akkadian sāsum, or Indo-European reconstruction (Mann, Pokorny)."
}
```


## [2026-09-06T20:58:13.930Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D8%A7%D8%B3/",
 "prompt": "Give the dictionary entries for Persian ساس (sās): the Dehkhoda entry and the فرهنگ معین entry, including any bracketed origin tag (e.g. [ع.], [په.]) and any etymological note. Quote the Persian text."
}
```


### [2026-09-06T20:58:20.269Z] TOOL RESULT

```
# ցեց (cʻecʻ) - Moth

## Meaning
The primary definition is **moth**. Secondary meanings include a skin disease and figurative uses (something that oppresses or a restless person).

## Etymology

The Old Armenian entry states the origin is uncertain. The dictionary notes similarities across neighboring languages:

- Udi: _цӏецӏ_ (c̣ec̣)
- Proto-Georgian-Zan: _\*c₁ic₁-_
- Akkadian: _sāsum_
- Classical Syriac: _sāsā_
- Ancient Greek: _σής_ (sḗs)

**Semitic Borrowing Hypothesis:**
"The Armenian is often considered a Semitic borrowing, even though Semitic _s_ is incompatible with Armenian _ց_ (cʻ)."

To resolve this incompatibility, Ačaṙean proposed derivation from an emphatic Akkadian form (_ṣāṣu_), though this alternative form's existence is questioned in modern references.

**Alternative Explanation:**
The entry suggests these may represent "independent expressive formations for insects in various languages" rather than related etymologies.
```


### [2026-09-06T20:58:24.819Z] TOOL RESULT

```
# Persian Dictionary Entries for ساس (sās)

## Dehkhoda Entry

The Dehkhoda dictionary provides an extensive etymological discussion. The entry notes that ساس refers to "a small insect from the category of bugs and fleas" and explains its origins, stating it is "authentic classical Arabic" (عربی فصیح). The entry traces the word's evolution from a general term for small insects to its specialized modern meaning.

## فرهنگ معین Entry

The Farhang-e Moein entry is marked with **(اِ.)** and defines the term as: "an insect from the order Hemiptera, larger than a flea [کک], that hides in the cracks of mattresses and cushions and in wooden objects, emerging at night to bite humans."

Both entries describe the creature as a blood-feeding insect that inhabits bedding and wooden furniture, active primarily at night.
```


## [2026-09-06T20:58:34.119Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%8A%D9%81",
 "prompt": "Give the Arabic entry سَيْف (sayf) 'sword': meaning, root س ي ف, verb sāfa/yasīfu, and the full etymology section verbatim — any mention of Egyptian sfj.t/zft, Greek ξίφος, Ge'ez ሰይፍ, Proto-Semitic, or a borrowing direction. Also note any Persian section."
}
```


## [2026-09-06T20:58:36.616Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0e",
 "prompt": "Give the PIE reconstruction *ǵʰe / *ǵʰi (emphatic/enclitic particle): meaning and descendants, particularly Sanskrit हि (hi), Avestan zī, Greek -χι, Latin -hi- in hic, Old Church Slavonic -že, Lithuanian -gi. Quote the entry."
}
```


### [2026-09-06T20:58:41.875Z] TOOL RESULT

```
# Arabic Entry: سَيْف (sayf) 'Sword'

## Meaning
The primary definition is: "sword, sabre, foil, rapier, scimitar"

## Root
The root is **س ي ف** (s y f), described as denominal.

## Etymology Section (Verbatim)
"Related to Ancient Greek ξίφος (xíphos); either a loan, or from a common original source. The same word is probably preserved in Egyptian zft, Coptic ⲥⲏϥⲉ (sēfe). Dümichen (1867) suggested an Old Semitic saïf or sêf, Myres (1930) a possible Libyan or 'Sea Peoples' word."

The entry also notes: "Compare Hebrew סַיִף (sáyif)."

## Verb Information
The page does not provide a verb entry "sāfa/yasīfu" for the sword meaning. Etymology 2 lists a different noun meaning "coast/riverbank/shore."

## Persian Section
No Persian section appears in this entry. However, descendants note: "→ Persian: سیف (seyf)"

## Additional Notes
The etymology references Egyptian, Coptic, Hebrew cognates but does not mention Ge'ez or provide explicit Proto-Semitic reconstruction.
```


### [2026-09-06T20:58:43.230Z] TOOL RESULT

```
# Proto-Indo-European *gʰe Particle

Based on the Wiktionary entry, this reconstructed particle functioned as a **postpositional intensifying element** with the core meaning of "indeed, at any rate, in fact."

## Key Characteristics

The particle occurred in multiple ablaut grades (*gʰe, *gʰo, *gʰi) and could appear either **postposed to intensified words** or at **discourse beginning**. As noted: "The particle was indeclinable in Proto-Indo-European. Some daughter languages...added pronominal inflection later."

## Descendants

The entry traces reflexes across language families:

- **Sanskrit**: ह (ha), घ (gha)
- **Greek**: γε (ge)
- **Latin**: reflexes in *hō- (hic, hōrsum)
- **Slavic**: *že (Old Church Slavonic)
- **Baltic**: Lithuanian -gi, Old Prussian neggi
- **Germanic**: *-k (Gothic -𐌺)
- **Tocharian**: ka ("just, scarcely")

The reconstruction notes indicate Dunkel distinguishes aspirated and unaspirated forms, acknowledging dialectal variation in both aspiration and ablaut grade across Indo-European daughter languages.
```


## [2026-09-06T20:58:51.818Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%BF%E0%A4%AB%E0%A4%BE",
 "prompt": "Give the Sanskrit entry शिफा (śiphā): all meanings (fibrous root, twig/rod, whip, hair?) and any etymology. Quote it."
}
```


## [2026-09-06T20:58:53.704Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/et%20cetera",
 "prompt": "Give the Etymonline entry for \"et cetera\": date of first attestation in English, and the Latin analysis of cetera (neuter plural of ceterus) with its PIE analysis (*ke- + *eteros / *i- 'this')."
}
```


### [2026-09-06T20:58:57.824Z] TOOL RESULT

```
# Sanskrit Entry: शिफा (śiphā)

## Meanings

The word has nine primary definitions:

1. A fibrous or flexible root (used for making whips)
2. A lash or stroke with a whip or rod
3. A branch
4. A river
5. A tuft of hair on the crown of the head
6. The root of a waterlily
7. Spikenard
8. Turmeric
9. A sort of dill or fennel

## Etymology

The entry notes that "This etymology is missing or incomplete."

## Direct Quote

According to Wiktionary's Sanskrit section, the word describes "a fibrous or flexible root (used for making whips)" as its primary meaning, with secondary meanings including "a lash or stroke with a whip or rod" and various botanical references.

The term is classified as a feminine ā-stem noun in Sanskrit declension, with full conjugation patterns documented across singular, dual, and plural forms.
```


### [2026-09-06T20:59:00.744Z] TOOL RESULT

```
# Etymonline Entry for "Et Cetera"

**Date of First Attestation:** Early 15th century

**Latin Analysis:** The term derives from Latin *et cetera*, literally meaning "and the others." The word *cetera* is the neuter plural of *ceterus* ("the other, other part, that which remains").

**PIE Etymology:** According to Etymonline, *ceterus* traces back to Proto-Italic *\*ke-etero‑*, which combines:
- *\*ke‑* (a variant form of the PIE root *\*ko‑*, meaning "this" as a demonstrative pronoun stem)
- *\*etero‑* (a PIE comparative adjective meaning "other (of two), again, a second time")

**Historical Note:** The abbreviation *&c.* was the common form before the 20th century, after which *etc.* became standard.
```


## [2026-09-06T20:59:12.374Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱe\" \\\n \"https://en.wiktionary.org/wiki/ξίφος\" \\\n \"https://en.wiktionary.org/wiki/ceterus\" \\\n \"https://en.wiktionary.org/wiki/σής\" \\\n \"https://en.wiktionary.org/wiki/سوس\" \\\n \"https://en.wiktionary.org/wiki/ցեց\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 267 (book 237), roots Ki 2 / Kiĕs / Kiph — verification\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T20:59:15.841Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a7141d49cece5cce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c742570e15eb8b62.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c364664646fe64e0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/48c35506fde8483b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f935493871a88b47.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/42ad08b35edf73c3.txt
```


## [2026-09-06T20:59:19.429Z] TOOL CALL #69: Bash

```json
{
 "command": "for u in \\\n \"https://abadis.ir/fatofa/ساس/\" \\\n \"https://en.wiktionary.org/wiki/سيف\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵʰe\" \\\n \"https://en.wiktionary.org/wiki/शिफा\" \\\n \"https://www.etymonline.com/word/et%20cetera\" \\\n \"https://www.etymonline.com/word/he\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 267 (book 237), roots Ki 2 / Kiĕs / Kiph — verification\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T20:59:24.903Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f545715fe63f50a9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f1f92c017f3dcfe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/32c9f44c17052417.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/17191585fc576706.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8758d7a34cc492c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/953c8c7f810d9f1c.txt
```


## [2026-09-06T20:59:43.771Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== POK ghe WP ref ==\"; awk 'BEGIN{RS=\"\\f\"} NR==75' POK_02.txt | grep -n \"WP\\.\" | head -3\necho \"== WLD Bd1 ko-,ke- p452/453 ==\"; awk 'BEGIN{RS=\"\\f\"} NR==462' incoming/WLD/WLD_Bd1_pages.txt | head -c 1800"
}
```


### [2026-09-06T20:59:45.441Z] TOOL RESULT

```
== POK ghe WP ref ==
13:WP.  I  541  f.,  WH.  I  644,    Schwyzer  Gr.  Gr.  I  606,  624.  :^
== WLD Bd1 ko-,ke- p452/453 ==
                             ;                                                                                          ,




gov),     wonach auch *xia$ersg „heuer“                                in orjzes,       att.         dor. cares; lat.
-ce,    ce-Partikel in               ce-do    ,,gib   her'’     (ebenso osk. ce-bnust „er wird herge-
kommen sein      oder hingekommen sein"; trotz J. Schmidt KZ. 26, 376,
Pedersen Pron. dem. 1 4 f. nicht aus redupl. g'ieg'ten- dissimiliertes *geben-
mit blot! orthographischem c fur g), ceterus „der andere, der ubrige"
(*ce oder *ceir                  —
                     s. Brgm. IP. 6, 87 f. und 28, 298          f- *etero -, vgl. umbr.

etru „altero“; die ich-deiktische Bed. ware zur Bed. eines bloBen Artikels
verblaBt, hi-c(e), his-ce, sl-c (si-ci-ne), illii-c, tun-c, nun-c usw., palign. eci-c,
ecu-c, marr. iaf-c, esu-c, oak. idi-k, umbr. ere-k „id“, osk. ekas-k ,.hae“,
umbr. esmi-k „huic“, lat. ecce (wohl aus *ed-ke s. *e Pron. -St.), osk. um          ,


-urn erweitert ekk-um „ebenso“, nach puz „wie“ aus *q'iuti-s umgebildet
ekss „ita" Konglutinat e-ko- z B. osk. ekas „hae“, palign. acuf „hic“, ecuc
                  ;


„huc", ecic „hoc'', *e-k(e)-so- z. B. osk. exac „hac" ; lat. cis „diesseits“, citer
„diesseitig'', citro „hierher“, citra „diesseits'‘, citimus „nachstbefindlich“,

umbr. give „citra" (St. *ki-uo-), gimu, simo „ad citima, retro"; air. ce ,,hier,
diesseits" (nach Pokorny ZfePh. 10, 403 aus *ke>, vgl. ablautend ogom
coi „hier“ mit der proklit. Nebenform ci), cen (vgl. zum w-Suffix ahd.
hina „weg             ‘
                          usw.) „diesseits“           (in     cen-alpande ,.cisalpinus“) und „ohne“, cen-
tar �
```


## [2026-09-06T20:59:53.144Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD I 541 (leaf 550) ==\"; awk 'BEGIN{RS=\"\\f\"} NR==550' incoming/WLD/WLD_Bd1_pages.txt | head -c 1600"
}
```


## [2026-09-06T20:59:54.200Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FRS شفشاهنج ==\"; grep -n \"شفشاهنج\\|شفشاهنگ\\|شفش\" FRS.txt FRS_pages.txt | head; echo \"== KLN xiphoid ==\"; grep -n \"^xiphoid\\|xiph\" KLN_1966.txt | head -5; echo \"== LAT ceterus ==\"; grep -n \"ceterus\" LAT.txt LEW_1910.txt | head -5"
}
```


### [2026-09-06T20:59:54.758Z] TOOL RESULT

```
== WLD I 541 (leaf 550) ==
                                             ,




                                         ghasto-      — glie-, gho-                                        541


ghasto- „Hand, Arm".
  Ai. hastu m. „Hand“, hastavant „ hand verse hen", av. zastu apers. (last a m.             ,



„IIand, und zwar ahurischer AVesen", zastu vant „tatkraftig“ lit. pazast'ts f..             ;


pagaste „Raum unterm Arm, Achselkohle".
  Fick I 4 420, 433, Wackernagel ai. Gr. I 248, Trautmann Bsl. Wb. 367.
  Abzulehnen die Anreihung von gr dyoarog „flache Hand“ (de Saussure
                                                       .



Memoire 53 A. 1, oft nachgesprocken, s. die Literatur bei Boisacq 9) vgl.
unter *ger- „fassen, zusammenfassen". — Uber aksl. pazucha „xoA7iog“ sielie
Berneker SlEWb. 233 f., Trautmann aaO. 64.

ghasto-, ghazdho- „Rute, Stange".
  Lat.    hastu      „Stange,       Stab,    Schaft,       Speer,         WurfspieB",           umbr. hostuta    ,



anostatu      „hastatos,       inhastatos"       (o    nicht   befriedigend         erkliirt),      mir.   gass
„Scho£S. SproB, Reis“ (< *ghaslo- Zupitza G. 96, Yf. KZ. 34, 488 f., Solmsen
IA. 19, 31); daneben *ghazdh- in mir. gat „ Weidenrute", mir. trisgatuim
„durchbohre“, got. gazds „Stachel“, aisl. guddr „Stachel, Spitze", as. fmr-
gard „Feuergabel“, ahd. gart „stimulus“, dazu mit io-Ableitung ags. gierd
f. „Rute“, afr. ierdt „Gerte, HeBrute", as. gerdia „Gerte, Rute, Stab, Stralil",

ahd. gartia, gertia „Rute, Szepter" (so Sievers z. ags. Yokalismus 25,
```


### [2026-09-06T20:59:54.828Z] TOOL RESULT

```
== FRS شفشاهنج ==
FRS.txt:3620:مردار باشد» شفشا هنج : شکلجه بوده وضج : بهن‌شده وا گوتن » قاج : 
FRS.txt:21669:شفشاهنج ۷۳ 
FRS_pages.txt:3811:‫مردار باشد» شفشا هنج ‪ :‬شکلجه بوده وضج ‪ :‬بهن‌شده وا گوتن » قاج ‪:‬‬
FRS_pages.txt:22757:          ‫شفشاهنج ‪۳۷‬‬                        ‫|ابورد ‪۷۸‬‬
== KLN xiphoid ==
2158:alevin,  n.,  a  young  fish.  —  F.,  ‘fry,  young  fish’, fr.  OF.  alevain,  fr.  VL.  *allevdmen,  fr.  L.  alle- vdre,  ‘to  lift  up,  lighten,  alleviate’,  in  VL.  also ‘to  bring  up,  rear’,  fr.  ad-  and  levare,  ‘to  raise, lift  up’.  See  lever  and  cp.  elevate.  The  French form  alevin  (fr.  OF.  alevain)  is  due  to  the  change of  suff.  -ain  (fr.  L.  -amen)  to  suff.  -in  (fr.  L.  -inus). Alexander,  masc.  PN.  —  L.  Alexander,  fr.  Gk. ’AXl^otvSpoi;,  lit., ‘defender  of  men’,  fr.  d&iijeiv, ‘to  ward  off,  keep  off,  turn  away,  defend,  pro¬ tect,  and  avfjp,  gen.  avSpO!;,  ‘man’.  ’AXeijeiv  is desiderative  of  (xXexeiv,  ‘to  ward  off’,  which  is related  to  aXxir),  ‘protection,  help,  strength, power,  courage’,  #Xxi|jlo9,  ‘strong’,  and  cogn. with  OI.  raksati,  ‘protects’,  OE.  ealgian,  ‘to  de¬ fend’,  and  possibly  also  with  OE.  ealh,  OS. alah,  Goth,  alhs,  ‘temple’,  OLith.  elkas,  alkas, ‘sacred  wood’,  Lett,  elks,  ‘idol’.  Cp.  Alcmene, alexin,  alexipharmic,  Alexis,  Alexius,  Alcestis, analcite.  Cp.  also  lac,  ‘one  hundred  thousand’. For  the  2nd  element  in  Alexander  see  andro-. alexanders,  the  meadow  parsnip.  —  Lit.  ‘the flower  of  Alexander  (the  Great)’;  so  called  for its  brilliant  color  suggesting  royalty. Alexandrine,  n.,  a  verse  of  six  iambic  feet,  having the  caesura  after  the  third.  —  F.  alexandrin;  so called  because  first  used  by  the  French  poet Alexandre  de  Paris  (de  Bernai)  in  a  poem  on Alexander  the  Great,  dating  from  the  13th  cent, alexandrite,  n.,  a  dark  green  variety  of  chryso- beryl  (mineral.)  —  Named  after  Alexander  II of  Russia.  For  the  ending  see  subst.  suff.  -ite. alexia,  n.,  inability  to  read  (med.)  —  Medical  L., formed  fr.  priv.  pref.  a-  and  Gk.  ‘speech’, from  the  stem  of  XsyEiv,  to  tell,  say,  speak’ (see  lexicon),  but  confused  in  meaning  with  L. legere,  ‘to  read’.  For  the  ending  see  suff.  -ia. alexin,  n.,  a  substance  which  destroys  bacteria (immunology).  — Coined  by  the  German  bacteri¬ ologist  Hans  Buchner  (1850-1902)  in  1888,  fr. Gk.  (xXeEeiv,  ‘to  ward  off.  keep  off.  protect’. See  Alexander  and  chem.  suff.  -in. alexipharmic,  adj.  counteracting  poison,  anti¬ dotal.  —  Gk.  dtXE^i^aptxaxoi;,  ‘acting  as  an  anti¬ dote’,  fr.  aXs^eiv,  ‘to  ward  off,  keep  off,  pro¬ tect’,  and  tpappiaxov,  ‘drug,  poison’.  See  Al¬ exander,  pharmacy  and  -ic.
2159:Derivative:  alexipharmic,  n.,  an  antidote.
28467:Derivatives :  pharmacopoei-al,  pharmacopoei-an, adjs.,  pharmacopoe-ist,  n. pharmacy,  n.,  the  art  of  preparing  and  dispensing drugs.  —  ME.  far  made,  fr.  MF.  (=  F.)  phar- rnacie,  fr.  Late  L.  pharmacia,  fr.  Gk.  9ap- paxeia,  ‘use  of  drugs’,  fr.  9app.axEuetv,  ‘to  ad¬ minister  drugs’,  fr.  9ap|jtxxov(  ‘medicine,  drug, remedy;  poison;  philter;  charm,  spell,  enchant¬ ment’,  which  is  perh.  cogn.  with  Lith.  buriu, burti,  ‘to  charm’,  Lett,  bur'u,  hurt,  of  s.m.  Cp. the  second  element  in  alexipharmic.
== LAT ceterus ==
LAT.txt:2724:tinction entre alius et alter et ceterus ne soit pas rigoureusement
LAT.txt:11516:ceterus, -a, -umr qui reste, restant, d'o 4 au pl. ceteri,-ae,-a
```


## [2026-09-06T20:59:59.179Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11510,11530p' LAT.txt; echo \"== FRS ctx ==\"; sed -n '3615,3625p' FRS.txt; echo \"== KLN xiphoid grep2 ==\"; grep -n \"5;t9o<;\\|xiphoid\\|Xiphias\\|sword-shaped\" KLN_1966.txt | head -5"
}
```


### [2026-09-06T20:59:59.257Z] TOOL RESULT

```
V. cornu, cerebru*, ceruix.
cesso, -as, -are; cf. cedo.409
ceueo
-cessC, -is, -Ini, -Ituta, -ere: n'existe qu'en composition dans
ar-cessS (?) in-cesso. D6sid£ratif, qu'il fant sans doate rattacher
k cedb "s 1 avancer".
ceterus, -a, -umr qui reste, restant, d'o 4 au pl. ceteri,-ae,-a
"tous les autres, ceux qui restent”. Difffere peu dans 1 'usage de reli¬
quus, e.g. Cic.,Rep.6,17, qui globus reliquos bmnis complectitur, sum¬
mus ipse deus arcens et continens ceteros-, toutefois semble plus
comprehensif, cf. Cic., Verr.5,87, erant perpauci reliqui, ceteri dimissi.
- Ceteri designe un enseable par opposition k alii: Sali.Iu.74,1,
ceteri formidine, pars ad Romanos, alii ad regem Bocchum profugerant ;
aussi est-il souvent joint k omnes, cuncti. Le neutre 9'emploie adver-
bialenent: ceterum, cetera "du reste” et depuis Salluste^ surtout
dans Tite Live, ”«ais” (cf. pour le sens gr. aXXa, 'nxXXa, xa Xchtox),
(de)cetero, ceteroqui(n). - Ancien, usuel et classique. Non ronan.
Comprend 6videmment le mot qui se retrouve en ombrien, avec le sens
de "alter”: etru "altero”, etram "alteram", etraf "alteras", etc., en
face de lat. alter et de osq. alttram, etc.; c’est le deriv 4 en *-tero~,
*-tro- des th&mes du demonstratif i.-e. *e- et *i-’, il se retrouve
== FRS ctx ==
دود 
درحاشية ن در آخر باب الجیم لغات ذیل بدون شاهد بخطی‌جدیدتر 
جر نسخه‌الحاق شده که غالب آنها تکرار لغات سابق‌است معهذا بازماآ نهارا 
عیتاً در اینجا هل میکنیم : 
یچ : معجب بود وچیزی طرفه را بپارسی کیج خوانند» گنچ (ا): شوخ 
مردار باشد» شفشا هنج : شکلجه بوده وضج : بهن‌شده وا گوتن » قاج : 
غلق درباشد » کیچ :| ص : کاج | سید تونیان بود » (ج [ ص + لخج ] 
زاگک فت نان «ود 6 فرخج بلید باشد ۰ 
کیچ دیگر | ص - کلچ | : شکن و چین باشد در زلف و رسن و جامه 


== KLN xiphoid grep2 ==
13231:ensemble,  n.,  the  whole.  —  F.,  ’together’,  fr.  L. insimul,  ‘at  the  same  time’,  which  is  formed  fr. in-,  ‘in’,  and  simul,  ‘at  the  same  time,  together’. See  simultaneous  and  cp.  assemble, enshrine,  tr.  v.  —  Formed  fr.  ist  en-  and  shrine, ensiform,  adj.,  sword-shaped.  —  Compounded of  L.  ensis,  ‘sword’,  and  forma,  ‘form,  shape’. The  first  element  stands  for  *qsis  and  is  cogn. with  OI.  asih,  ‘sword,  butcher's  knife’.  For  the second  element  see  form,  n. ensign,  n.,  1)  a  flag;  2)  in  the  United  States  Navy, a  commissioned  officer  of  the  lowest  rank.  — OF.  (=  F.)  enseigne,  fr.  L.  insignia,  pi.  of  in- signe,  ‘mark,  sign,  badge  of  office’,  prop.  neut. of  insignis,  ‘remarkable,  noted,  distinguished’, but  mistaken  in  Vulgar  Latin  for  a  fern.  sing, noun.  L.  insignis  is  formed  fr.  in-  ‘in’,  and  sig- num,  ‘mark,  sign’;  see  sign  and  cp.  insignia.  Cp. also  It.  insegna,  OProven?.  ensenha  and  OSp. enseha,  which  all  derive  fr.  L.  insignia.' Derivative :  ensign-cy,  n.
16203:gladiate,  adj.,  sword-shaped  (bot.)  —  Formed with  adj.  suff.  -ate  fr.  L.  gladius,  ‘sword’.  See next  word.
```


## [2026-09-06T21:00:10.827Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN1971 xiph ==\"; grep -n -o \"xiphoid[^.]\\{0,300\\}\" KLN_1971.txt | head -3; grep -n -o \"Xiphias[^.]\\{0,200\\}\" KLN_1971.txt | head -3; echo \"== FVQ sayf ==\"; grep -n \"saif\\|sayf\" FVQ.txt | head -5; echo \"== AFM سيف ==\"; grep -n \"( السيف )\\|( سيف )\" AFM.txt | head -3; echo \"== PLA sayf ==\"; grep -n -i \"^saif\\|sayf\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5"
}
```


### [2026-09-06T21:00:12.729Z] TOOL RESULT

```
== KLN1971 xiph ==
269136:xiphoid, adj
270757:Xiphias
== FVQ sayf ==
== AFM سيف ==
== PLA sayf ==
```


## [2026-09-06T21:00:14.998Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '269130,269145p' KLN_1971.txt; echo \"---\"; sed -n '270750,270765p' KLN_1971.txt"
}
```


### [2026-09-06T21:00:15.085Z] TOOL RESULT

```
Association, p. 141, Spiegelberg in Zeitschrift 
fur vergleichende Sprachforschung, 41, 132, 
Schrader, Sprachvergleichung und Urgeschich- 
te, 3rd ed., II, pp. 110 ff., Cp. prec. word and 
Ziphius. 

xiphoid, adj., sword-shaped. — Gk. fr<p oet&fc, 
‘sword-shaped’, fr. ^<poq, ‘sword’, and -oeiSrj?, 
‘like’, fr. elSoc, ‘form, shape’. See xipho- and 
-oid. 

Xmas, n., Christmas. — Prop. = X, the Greek 
letter chi, as the initial letter of Xpiax6<; (see 
Christ) and -mas (in Christmas), 
xoanon, n., a primitive wooden image {Greek an- 
tiq.) — Gk. 56avov, ‘an image carved of wood’, 
---

zip, tr. v., to close or fasten with a zipper. — 
Back formation fr. zipper. 

Ziphius, n., a genus of beaked whales (zool.) — 
ModL., altered fr. Xiphius, fr. Gk. ££<pt,o<;, 
‘swordfish’, fr. ££<po<;, ‘sword’. See xipho- and 
cp. Xiphias. 

Zipper, n., a slide fastener. — Fr. Zipper, a trade 
mark, formed from zip, n., with agential suff. 
-er. 

zircon, n. — F., a var. of jargon, ‘a variety of zir- 
con’ (q.v.)
```


## [2026-09-06T21:00:17.262Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '269105,269136p' KLN_1971.txt"
}
```


### [2026-09-06T21:00:17.328Z] TOOL RESULT

```
Compounded of Gk. ‘dry’, and <put6v, 

‘plant’. See xero- and -phyte. 

Xerxes, n., king of Persia, who reigned 486-465 
B.C.E.; called the Great. — Gk. 3£pSir)<;, fr. 
OPers. Xshayarshan-. See Ahasuerus. 
xiph-, form of xipho- before a vowel. 

Xlphias, n., a genus of fishes, the swordfish (ich- 
thyol.) — L., ‘swordfish’, fr. Gk. 
‘swordfish’, fr. ‘sword’. See xipho- and 

cp. Ziphus. 

xipho-, before a vowel xiph-, combining form 
meaning ‘sword’. — Gk. £iq>o-, Sup-, fr. JUqpos, 
‘sword’, of uncertain origin. It is perh. a loan 
word fr. Aram, saypha (whence also Heb. sdylf, 
Arab, sayf ), fr. Egypt, sefet, ‘sword’, which is a 
derivative of the verb sft, ‘to slaughter’. See H. 
Lewy, Die semitischen Fremd whiter im Grie- 
chischen, pp. 176 ff., Muss-Amolt, On Semitic 
Words in Greek and Latin, in the Transactions 
and Proceedings of the American Philological 
Association, p. 141, Spiegelberg in Zeitschrift 
fur vergleichende Sprachforschung, 41, 132, 
Schrader, Sprachvergleichung und Urgeschich- 
te, 3rd ed., II, pp. 110 ff., Cp. prec. word and 
Ziphius. 

xiphoid, adj., sword-shaped. — Gk. fr<p oet&fc,
```


## [2026-09-06T21:00:23.170Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xipho-\\|saypha\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T21:00:23.218Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:00:26.630Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Xerxes,  n\\.\\|xiph\\|Xipbias\\|Xiphias\" KLN_1966.txt | head -5; echo \"== nearby page markers ==\"; grep -n \"^ *174[0-9] *$\" KLN_1966.txt | head"
}
```


### [2026-09-06T21:00:28.508Z] TOOL RESULT

```
2158:alevin,  n.,  a  young  fish.  —  F.,  ‘fry,  young  fish’, fr.  OF.  alevain,  fr.  VL.  *allevdmen,  fr.  L.  alle- vdre,  ‘to  lift  up,  lighten,  alleviate’,  in  VL.  also ‘to  bring  up,  rear’,  fr.  ad-  and  levare,  ‘to  raise, lift  up’.  See  lever  and  cp.  elevate.  The  French form  alevin  (fr.  OF.  alevain)  is  due  to  the  change of  suff.  -ain  (fr.  L.  -amen)  to  suff.  -in  (fr.  L.  -inus). Alexander,  masc.  PN.  —  L.  Alexander,  fr.  Gk. ’AXl^otvSpoi;,  lit., ‘defender  of  men’,  fr.  d&iijeiv, ‘to  ward  off,  keep  off,  turn  away,  defend,  pro¬ tect,  and  avfjp,  gen.  avSpO!;,  ‘man’.  ’AXeijeiv  is desiderative  of  (xXexeiv,  ‘to  ward  off’,  which  is related  to  aXxir),  ‘protection,  help,  strength, power,  courage’,  #Xxi|jlo9,  ‘strong’,  and  cogn. with  OI.  raksati,  ‘protects’,  OE.  ealgian,  ‘to  de¬ fend’,  and  possibly  also  with  OE.  ealh,  OS. alah,  Goth,  alhs,  ‘temple’,  OLith.  elkas,  alkas, ‘sacred  wood’,  Lett,  elks,  ‘idol’.  Cp.  Alcmene, alexin,  alexipharmic,  Alexis,  Alexius,  Alcestis, analcite.  Cp.  also  lac,  ‘one  hundred  thousand’. For  the  2nd  element  in  Alexander  see  andro-. alexanders,  the  meadow  parsnip.  —  Lit.  ‘the flower  of  Alexander  (the  Great)’;  so  called  for its  brilliant  color  suggesting  royalty. Alexandrine,  n.,  a  verse  of  six  iambic  feet,  having the  caesura  after  the  third.  —  F.  alexandrin;  so called  because  first  used  by  the  French  poet Alexandre  de  Paris  (de  Bernai)  in  a  poem  on Alexander  the  Great,  dating  from  the  13th  cent, alexandrite,  n.,  a  dark  green  variety  of  chryso- beryl  (mineral.)  —  Named  after  Alexander  II of  Russia.  For  the  ending  see  subst.  suff.  -ite. alexia,  n.,  inability  to  read  (med.)  —  Medical  L., formed  fr.  priv.  pref.  a-  and  Gk.  ‘speech’, from  the  stem  of  XsyEiv,  to  tell,  say,  speak’ (see  lexicon),  but  confused  in  meaning  with  L. legere,  ‘to  read’.  For  the  ending  see  suff.  -ia. alexin,  n.,  a  substance  which  destroys  bacteria (immunology).  — Coined  by  the  German  bacteri¬ ologist  Hans  Buchner  (1850-1902)  in  1888,  fr. Gk.  (xXeEeiv,  ‘to  ward  off.  keep  off.  protect’. See  Alexander  and  chem.  suff.  -in. alexipharmic,  adj.  counteracting  poison,  anti¬ dotal.  —  Gk.  dtXE^i^aptxaxoi;,  ‘acting  as  an  anti¬ dote’,  fr.  aXs^eiv,  ‘to  ward  off,  keep  off,  pro¬ tect’,  and  tpappiaxov,  ‘drug,  poison’.  See  Al¬ exander,  pharmacy  and  -ic.
2159:Derivative:  alexipharmic,  n.,  an  antidote.
28467:Derivatives :  pharmacopoei-al,  pharmacopoei-an, adjs.,  pharmacopoe-ist,  n. pharmacy,  n.,  the  art  of  preparing  and  dispensing drugs.  —  ME.  far  made,  fr.  MF.  (=  F.)  phar- rnacie,  fr.  Late  L.  pharmacia,  fr.  Gk.  9ap- paxeia,  ‘use  of  drugs’,  fr.  9app.axEuetv,  ‘to  ad¬ minister  drugs’,  fr.  9ap|jtxxov(  ‘medicine,  drug, remedy;  poison;  philter;  charm,  spell,  enchant¬ ment’,  which  is  perh.  cogn.  with  Lith.  buriu, burti,  ‘to  charm’,  Lett,  bur'u,  hurt,  of  s.m.  Cp. the  second  element  in  alexipharmic.
== nearby page markers ==
```


## [2026-09-06T21:00:36.481Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"^HE, pron[^|]\\{0,400\\}\\|^HE\\b.\\{0,400\\}\" SKT.txt | head -3; echo \"== SKT cetera ==\"; grep -n -o \"cetera.\\{0,250\\}\" SKT.txt | head -3; echo \"== SKT hence ==\"; grep -n -o \"HENCE.\\{0,250\\}\" SKT.txt | head -2"
}
```


### [2026-09-06T21:00:38.130Z] TOOL RESULT

```
== SKT cetera ==
== SKT hence ==
```


## [2026-09-06T21:00:41.721Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -o \"hence, adv.\\{0,300\\}\\|hence (1).\\{0,300\\}\\|^he (1).\\{0,300\\}\" SKT.txt | head -5; echo \"-- try FSD\"; grep -l . FSD_vol*.txt; grep -n -o \"et cetera.\\{0,200\\}\" FSD_vol2.txt | head -3"
}
```


### [2026-09-06T21:00:43.378Z] TOOL RESULT

```
-- try FSD
FSD_vol3.txt
FSD_vol2.txt
FSD_vol4.txt
FSD_vol1.txt
```


## [2026-09-06T21:00:50.147Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC kiph ==\"; grep -n \"^Kiph\\|^kiph\\|Kipha\" IEC.txt | head -3; echo \"== IEC seip/skeip ==\"; grep -n -o \"Kip-.\\{0,200\\}\" IEC.txt | head -3; echo \"== SYN THIS ==\"; grep -n -o \"11\\.31.\\{0,300\\}\" SYN.txt | head -3; echo \"== BQT v2 ساس ==\"; grep -n \"ساس\" BQT_v2_pages.txt | head -8"
}
```


### [2026-09-06T21:00:52.151Z] TOOL RESULT

```
== IEC kiph ==
== IEC seip/skeip ==
15534:Kip- and skoip-. All the evidence is ambig.) Cf. MHG schibe, wf. (2) ‘slice’; E dial. shive, id. (fr. *skeibh-, *skeip- or fr. *skibh-, skip- with variant initial in) Blg. cipa, f. (skin'. LW in Mod. Gk. 
== SYN THIS ==
1269:11.312, Gram. 95.
5824:11.316. Bee obraz ‘face’ and ‘cheek’, fr. ‘, (ChSl. obrazi ‘form, shape, plavie, ‘cheek’, etc. Tiktin image’, SCr. obraz ‘cheek , etc.
16475:11.31). Weigand-H. 1166. Paul, Deutsches Wtb. 603.
== BQT v2 ساس ==
425:   ‫املا‬               ‫‪ .‬ساسکریت ‪2‬‬           ‫( ‪0086020 ۰‬‬     ‫(ازد‬
1682:                                                                                ‫ساسایان و شابد ق‬
2543:  ‫‪ - ۱‬از ‪ :‬جم ا(وستا ‪ , 20111۷‬ساسکریت (ودا) ‪ 21712۷۰‬پهلری‪ < 012۷‬بارتولمه‬
3834:   ‫شهمیر زادی ‪٣‬لا‏ ك ‪ ۲ .‬ص ‪ ۹۷۱۰‬ک»یلکی ‪.۲8086‬ساس کرت ‪٩( ۲21200‬‏ چترشاهی‪,‬درفش‬
4126:     ‫؟ ‪ -‬اھ درساسکربت‬                     ‫‪alãc‬‏ ؛تپرالی ام رك ‪:‬چالو ‪ ,‬چاله ‪-‬‬        ‫‪ ۱‬ورک‬
7425:     ‫هرمز چهارم پادشاه ساسانی بود که درجنك باخاقان‌تر کستان پیروز شد و حرمز اورا بجنك رومیان‪‎‬‬
7478:      ‫یناه برد ودربلغ بیاسود و چندی بد قتل رسید ‪.‬ک‪۶‬رستنن‪ .‬ساسان‪ ۳44.‬ببمد» ‪۵*۵۰ ۹۷:۰‬‬
7976:                                                  ‫ساسان ‪« ۷4۱‬بوستی ‪ .‬بندعش ‪. ۱۲۱‬‬
```


## [2026-09-06T21:00:58.106Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"ساس\" BQT_v2_pages.txt; grep -n \"ساس\" BQT_v2_pages.txt | sed -n '9,40p'"
}
```


### [2026-09-06T21:00:58.179Z] TOOL RESULT

```
72
9177: ‫ه«عاعق‪ 4 - 721۵۵2 ۰ ۵ - :‬یز ‪ ,‬پهلوی ساسانی ‪ . 0251262‬سغدی ‪« 2 - 126‬نبر که‬
10444:      ‫‪-‬پلوی ‪ » 725‬اوستا ‪ » 8721-‬ساس کرت ‪"« 2372016-‬اسفا! ‪ ۲:‬ص ‪٦٦‬‏ »‬
10527:   ‫تام دوآتشکدة بزر گے عهدساسالی‪-‬‬ ‫‪۷‬ظ‬         ‫عهد سانانی ) است‪« .‬مزدیتا ‪. ۹۷۲-۸۷۲‬‬
12138:                                                ‫عرمز وچپارم ونوادة انوشروان» شاهنشاه ساسانی‬
12256:   ‫‪ ۱‬پهلوی ‪ , 6051‬اوستا ‪ 800151 -‬ساسکرت ‪« 2612005 -‬اسفا ‪ ۲ :۱‬ص ‪۷٩‬‏‬
14341:   ‫‪٩‬‏ ‪ -‬پازند ‪. 802‬افتانی ع ‪( 05‬قشنك)»ساس کربت_‪(5۷۳3۷115‬ازلا‪( 5‬خوب)‬                             ‫دخواستن» ‪.‬‬
14751:                        ‫یایهساس‬
18241:  ‫= ڑر ‪.).‬م‪.‬ھ( زد و زد نکمم تسا لکش یب‌هجپل دشاب یفا ‪‎‬تیرکساس _ ‪4601‬‬                                   ‫‪١‬‬
19159:      ‫ظاهراً ددر"ور ساسانیان برموبدی اطلاق مشده است که بشتر در امور دینی و قضایی مطالعه‬
21617:   ‫‪ -‬ساسکرت ‪272۳14‬‬                ‫‪۵‬‬                 ‫اسم مصنر از ‪#‬بکوهیدن» بجای «نکوهش» ‪.‬‬                                    ‫‪۸‬‬
21670:        ‫( در اردو ‪ :‬دهار) دم شمشیر ‪.‬رك‪ :‬جمدر (ح) وقس ‪ :‬ساسکریت ‪( 4۲040‬دای) رك‪ :‬دای‬
21751:  ‫ظ‪ ,‬ممحف « دهوبه »‪ .‬این‌کله درعصر ساسانبان ویز در قرنهای اول اسلام معمول‬         ‫‪۱‬‬
21781:           ‫کربستنن ‪ .‬ساسان ‪۵۱٩‬‏ ودهیوید ( دهیویت ) رئیس کشور وناحيةٌ بزرگك بوده است‪.‬‬
22057:  ‫وتمان آبرا از ره‪ çid ‎‬ساسکرت‪ ) .‬شان دادن‪) ‎‬‬
22826:      ‫که ‪ ۵۹۱‬ساسکریت ‪58۵۲‬‬   ‫« بارتولمه ‪ 6۱۵۱‬آرامیع ‪ ( 8287‬سربالی ‪« ) "82۵۲۵‬ریب‬
22960:   ‫رأی‌الیفل آبرا برای عمربن خطاب ببك خسروان (ساسانی) ضرب کرده وبرآن صورت پادشاء‌حك‬
25069:        ‫‪ - ¥‬پهلری ‪ 8021‬؛ ساسکربت ‪ 2802۲‬لبر کث‪ , » ۱۹۱‬ارمنی ع ‪(802۲6‬لون)؛‬
27050:     ‫شایور دوم‌ساسالی (‪ ۹۷۳ - ۰۱۳‬م ‪ ).‬است‪ .‬درینکرد صله بنده آ مده‪« :‬از این پس‌هم خن گنه‬
28048: ‫زرنشت پر آذرباد مهرسیندان است که در عصر ساسالی موبدان موبد بوده * اما طبیق زرتشت با‬
28353:                                   ‫باشکال مختلف درآورند ‪ « ».‬کرستنسن‪ .‬ساسلن ‪ .‬ترجمه ص ‪.> ۸۲۳‬‬
28458: ‫برخی از محققان مذهب معمول مزدینی عبد ساسالی را همان زروانت دادته‌الد ‪ .‬بیاری از‬
29032:  ‫‪ - ۴‬زرو (‪.‬م‪ --).‬زالوح‪ -‬زلوك »‪.‬ساسکریت ‪2112 [86018‬ز ‪ 811,‬از (زالو)‪,‬‬
29262:  ‫‪ - ۱‬وآن مترادف «باژ» است ‪ .‬درکتاب الناج منوب بجاحظ آمده ‪« :‬پادشاهان‌ساسافی‪-‬‬
29615:   ‫تفر اوستا بعنی زلد » بزبان پپلوی شروع شد و ندوین این تفیرتا اواخر عهد ساسانیمخصوصاً‬
29618:      ‫فصل ‪ 4‬ولدندادآمده ) ‪ .‬زلد با تفیری که امروژه در دست داریم »ت>فسیرست اآزعهد ساسایان‪.‬‬
29780:  ‫میلادی در کتيبة ‪ 711121‬موبدان موبد شاهان‌ساسانی هرمزد اول وبهرام اول وبهرام دوم د رکعبة‬
30057:   ‫پازند ‪402۰‬ساسکرت ‪ » [40 -‬اوستا و بارسی باستان ‪* 2000-2‬‏ کردی ‪ , 02‬بلوچی)‪»02‬‬
30517:    ‫‪anayj -‬‏ ) طلم ) * کردی ع‬                       ‫ساسکرت‬              ‫« بارتولمه ‪۱۰۷۱٩ ۰ ۰۰۷۱‬‏ لیر گے‬
31716:‫ساس د بروزن پای ‪ ۰‬بمعنی لطیف‬
31743:    ‫= —‬                                                                                       ‫ساسا رکشت‬
31744:‫بدین معنی آن طایفه راکه ایشان بانواع کدبه‬                  ‫با ثالث بالف کشده‬    ‫کشت ت‬      ‫ساسار‬
31748:‫خوانند ‪ ۰ ۴‬و بعضی کویند ساسان چون از بم‬                         ‫که آنرا بعربی بزرالانجره وقریض‌خوانند ‪۰‬‬
```


## [2026-09-06T21:01:04.089Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\noff=sum(len(l)+1 for l in lines[:31715]); leaf=d[:off].count('\\f'); print('leaf',leaf,'printed',leaf+540)\n\" ; sed -n '31710,31725p' BQT_v2_pages.txt"
}
```


### [2026-09-06T21:01:06.558Z] TOOL RESULT

```
leaf 533 printed 1073
                                                                   ‫‌ر وز‬
                                                                       ‫یب‬‫اهیم‬ ‫سازمند ‪= ۴‬‬
                                                                            ‫ببا‬
 ‫ساز یدن ‪ - ۸‬بروزن بازیدن » بمعنی‬                        ‫چیزی ساخته و آراسته و با نظام باشد اعم از‬
  ‫ساختن و راست کردن ‪ -‬و درخورآمدن باشد‪:‬‬                  ‫توشه و ژاد رواحله و ساختگی آنچه درسفر‬
                                                                                                  ‫بکار است ‪.‬‬
‫ساس د بروزن پای ‪ ۰‬بمعنی لطیف‬
 ‫وکییازه باشد ‪ -‬وببازن‌هندی مادر زن‌را گوبند‪-‬‬             ‫ساز نوروز ‪ -‬بكر ات » سامان‬
  ‫و نام جانوری است سیاء از مقولة كيك و شپش‬                ‫وساختگی و سرانجام‌نوروز باشد از اشربه واطعمه‬
 ‫لیکن زرکراز آمنیهاباشد و در حندوستان‬                    ‫و البه ‪ -‬ونام لحن دوبم است از سی‌لحن باربد‬
  ‫ی‬                             ‫بسار |وهی‬                                                   ‫بقول شیخ نظامی‪.‬‬
                                      ‫که‬                     ‫بروزن‌بازو» رسمانیست‌درغایت‬      ‫سارو ‏‬
                                                                         ‫(‪ )۱‬چك‪ :‬بسکون زا ‪.‬‬
    ‫‪ ۴‬زباکی ‪( 285‬آواز خواندن) « گربرسن‬                           ‫اسم از «سلختن ‪( €‬ه‪..‬م) ‪8‬‬     ‫‪-‬‬

   ‫‪« :‬فرمود‬   ‫‪ -‬لیر وسله ‪ ۰‬استطاعت‬     ‫‪۳‬‬          ‫‪ ۰‬تار) ‪۳‬‬    ‫موسعی‬   ‫وتهرانی ‪1( 232‬ك‬        ‫‪ :.‬کیلکی‬    ‫‪4۶‬‬
```


## [2026-09-06T21:01:17.649Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== POK Motte/Milbe ==\"; grep -n \"Motte\\|Milbe\" POK_0*.txt | head -8; echo \"== AHD moth/mite root ==\"; grep -n -o \"\\bmat-.\\{0,120\\}\\|Moth\\.\\{0,120\\}\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-06T21:01:19.256Z] TOOL RESULT

```
== POK Motte/Milbe ==
POK_03.txt:2033:gr.  OKiä  f.  (shii-a)  , Schatten',  (7xt«^dg,  hom.  G%i6eLg  ,schattig,  dunkel*, GMQOv  ,Sonnenschirm'  (formal  =  alb.  hir,  mit  Länge  got.  skeirs);  mit der  Stufe  skä[i]-:ay,r]vrj,  dor.  ay,Civd  ,Zelt,  Bühne,  Szene',  a'/.rjvog,  dor.  oy.ä- vogn.  ,Zelt;  Leib  (als  Hülle  der  Seele)';  cx^v  ,Schmetterling,  Motte'  Hes.; amvaQ  n.  ,Leib';
POK_03.txt:2340:gr.    y,siQü)   (yiSQoj,   iy,dQr]v,   y,6y,aQ(xaL,   xagzög)   ,abschneiden;   scheren;   ab- fressen', y,£Q^a  n.  , Schnitzel,   kleine  Münze',   v.0Q(.i6g  m.   ,(abgeschnittener) Klotz,   Rumpf,   y.0Qi.iat(a  ,zerstückle' ;   vloqk^  m.   ,Wanze'   (=  russ.   korh  £•-- ,Motte':  ,schneidend,  beißend,  zerbeißend');  Gen.  xa^dg  ,Nichts'  in  t/w  di ^Lv  iv  ycccgdg  dtar],  vgl.  auch  y.aQi^oiQOvg-  Tovg  iv  fir^de^ua  ^oloa  .  .  .  Hes.,
POK_03.txt:2342:fernei"  dxaoi  n.  ^Milbe^,  dy.aQrjg,  äxagiaToc  ^winzig-',  Hes. ;  ^schneidend'  scheint jjq  Grundbed.  von  -/.a^jvog  und  ycdg  ,Laus'  Hes.;  zu  letzterem  vielleicht ^doov,  %ccQog  ,KümmeP  (von  der  Ähnlichkeit  des  Kümmelkornes  mit  einer Laus) ;  niit  gv.  -acoQvyiog  ,Ledersack^  vgl.  ir.  curach,  Hautboot',  cymr.  corivg, ^ii/j'icg  ds.  aus  *kÖrukos;  vgl.  ferner  aisl.  hgrr,  Leinenkleid^,  ahd.  harra Sack^;  mit  einer  Bed.  ^schneidender  Hohn*  hierher  y.eQToiAog  ^höhnend', %sotou€ci)  ^höhne,  lästere^  (^^eo-axo^og  ,Qm  Lästermaul  habend'?  im  1.  Glied ein  Wznomen  [s]/cer-,  oder  ein  -[e]s-St.  */:er-s-);  ov-equcpog,  v,SQa(pog  ,TadeP Hes.,  a/.€Q-ßolog'  XoldoQog,  G'KSQßolsi'   hTcaxä  Hes.,  oy.SQßö'kXix)  ,schmähe^;
POK_03.txt:2356:russ.    korh  f.   , Masern'    und   ,Motte'  (,*Schererin') ;   aruss.   kora   ,Rinde*, russ.  usw.  kord  , Rinde,  Kruste';  wovon  u.  a.  ksl.  korice  PL   ,Zimt',  russ." korica  ds.,  körka  , Schale,  Rinde,  Kruste',  korett  ,hart  werden',  bulg.  kordtl , steif,   hart',   serb.   o-kbreti  se  , steif,   hart   werden'   usw.   (aksl.   korhCb  »einf Hohlmaß',  russ.  korec  , Mühlkasten;  Schöpfkelle  usw.',  slov.  korec  ,KörbcheaJ u.  dgl.';  vielleicht  zu  ai.  carü-  , Kessel'  usw.,  s.  k^er-)]  fe
POK_03.txt:2770:smelJ^g- :  srntig- :  poln.  smagiy  , schlank,  schmächtig';  smigiy  ds.,  smiga , dünne  Rute'  (an  Entlehnung  aus  dt.  schmiegen  ist  gewiß  nicht  zu  denken); lit.  smaXgas  , Stange' ;  lett.  smidzis  ,Milbe,  Wasserfloh^ ;
POK_03.txt:4160:mit  /-Suffix :  gr.  xtlog  »dünner  Stuhlgang,  Abführen' ;  abg.  thUti  ,modern, [rerwesen'»  thlja  ,Verwesung'»  russ.  tlja  ,Motte'  (vgl.  unten  lat.  tinea), [»Blattlaus';
POK_03.txt:4163:aksl.  tina  , Schlamm';  wohl  'Jat.  tlnus  ,der  lorbeerartige  Schneeball' (von  der  stark  abführenden  Wirkung)  und  tinca  , Schleie*  {Hlnica  ,schlei- "»»iger  oder  im  Schlamme  lebender  Fisch');  lat.  tinea  ,Motte,  Holzwurm* V%^'  oben  russ.  tlja)  wohl  von  einem  *tino-,  *tinä  ,Moder';
POK_03.txt:4530:Ai.  trndttij  Kaus.  tardayati  {tardati  Gramm.),  Perf.  tatdrda  ,durcM spalten',  tardman-  n.  ,Loch,  Öffnung',  tarda-  m.  ,ein  Insekt',  trdild- durchbohrt',    tradd-    ,der   (durch    Bohren)    eröffnet';   lit.    trendu, Motten,  Würmern  zerfressen  werden',  trandl  u.  trandls  ,Made,  Hol ablaut.  lett.  trüdi  ,Moder',  trüdet  ,verwittern,  faulen' ;  lit.  tride  ,Di aksl.  tr2d^  , Zunder'  und  ,Art   Krankheit,  dvaswegia^  (vgl.  oben lit.  triediiu  ,habe  Durchfall':  cymr.  trwyddo  ,bohren'),  öech.  trud  ,Zi< am  Gesicht'.
== AHD moth/mite root ==
705:Moth
729:mat-
730:mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 70
730:Moth
1829:mat- MATURE ma-1 MATUTINAL ma-1 MAUL mele- MAULSTICK mel-2 MAUVE malakhé MAW mak-2
```


## [2026-09-06T21:01:23.644Z] TOOL CALL #85: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T21:01:23.681Z] TOOL RESULT

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


## [2026-09-06T21:02:20.569Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg267.png'); print(im.size)\nim.crop((580,1810,1120,1960)).resize((1620,450)).save('crop_skt267.png')\nim.crop((580,2060,1420,2220)).resize((2100,400)).save('crop_gr267.png')\n\""
}
```


### [2026-09-06T21:02:22.548Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-06T21:02:25.061Z] TOOL CALL #87: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_skt267.png"
}
```


### [2026-09-06T21:02:25.085Z] TOOL RESULT

```

```


## [2026-09-06T21:02:44.006Z] TOOL CALL #88: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_gr267.png"
}
```


### [2026-09-06T21:02:44.105Z] TOOL RESULT

```

```


## [2026-09-06T21:02:44.100Z] INPUT

[Image: original 2100x400, displayed at 2000x381. Multiply coordinates by 1.05 to map to original image.]


## [2026-09-06T21:02:50.698Z] TOOL CALL #89: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg267.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/267.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-06T21:02:50.764Z] TOOL RESULT

```
total 11728
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 17:02 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-06T21:02:52.745Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"^zi\\b.\\{0,300\\}\\|noit\\.zi.\\{0,200\\}\\|nöit\\.zi.\\{0,200\\}\" BRT.txt | head -6; echo \"== BRT search zi denn ==\"; grep -n \"1701\\|zi- 'denn'\\|zi ,denn\" BRT.txt | head -5"
}
```


### [2026-09-06T21:02:55.535Z] TOOL RESULT

```
28150:zi  2  A
28171:zi  2  B
== BRT search zi denn ==
```


## [2026-09-06T21:02:57.697Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28130,28180p' BRT.txt"
}
```


### [2026-09-06T21:02:57.747Z] TOOL RESULT

```
28.^*\
S.  *gav-  No.  I  und  S  aoÄ  2.  —  Vgl.  ai.  ja- vij/ia-  Adj.  'der  rascheste',  np.  cb</ ■rasch'.  — Pü.:  däSaJiSI,  (zu  Y.  46):  pa  ..  dahin il;  e. noch  No.  2.  —  ■)  Mit  i  nur  Vt  13.  —  >)  Pü. : haäi  Joint  kflpa  :^ihiSn  i  j^atailh  i  süldmand, eil:  xataiik  i  sülömand  apt  döiit  u  api  dakti.  — j)  In  Folge  Vetmengung  mit  'ioola-  mir.; falsches  bei  Ju.  GIrPh,  2.  636. g.  (,  j.)  zar^d-  n.  'Herz';  a^rä  *rJam
baraiti . .  Vidvä  v3  ividvä  vä  ahyä  °däcä
manatikäcä  ". .  nach  seinem  Herzen  und
Sinn"  Y._jj.  12".
KompA.  (s.  auch  z^»S^.°)i);  Ableit.  —  ai. hfd-  n.;  mp.  (PO.),  np.  äil,  —  Vgl.  *ariiaya:
—  ')  S.  tVerb.  RV.  /.  98.  2:  uii  Afäöiä mänaiS.  —  •>  S.  auch  taraiainySi.  —  3)  Siebs Versuch,  ai.  kj-d-äh  asw.  mit  lat.  owd-is  la vermittelu,  KZ.  j/.  300,  überzeugt  mich  nicht;
•  j.  *z«i^fiaya-  n.  'Herz':  *'oBfl«*>  F. 20.  a)  im  Sinn  voninnerstes, Höchstes'*: fflSa  *t3mahs  mathim  aS«  ''zmtahe  *'%aem^ "und  es  ist  des  Winters  Mitte  und  es  ist des  Winters  Herz"  V. /.  3.
ai.  hfdaya-  n.  ~  Vgl.  iind-.  —  PO.  (10  V.)t dil,  (lu  F.):  fehlt.  —  >)  Hds.  -ioi™.  — •)  Vergl,  zu  unAwar-.  —  Sl  Hds.  trwvi".
•  j,  zaraSaza-'J  m.  Name  eines  Bergs  oder Gebirgs**:  bityB  (nämL  gatrii'  Aqm.AiItai) '2S'^  gairil  pärtnfarsm  ar3%S  manulake "als  zweites  (Gebirg  erstand)  das  Gebirg  Z. (abseits  von  sva.)  zu  beiden  Seiten  des M."  Yt.  19.  i*>.
•)  Bd.  13.  a  ;  köf  i  sarlaz  »  ki  asl  täf  i  maiaü. Ich  nehme  an ,  dass  vor  4sl  -  am  Anfang  der Zeile  in  K  -  /a  iusi  i  ausgefallen  ist,  das  dem aw.  pär^ittarim  arüS  entspräche.  Der  Mtimüa- Berg  erhebt  sich  im  I]intergmnd  über  dem  vor- gelagerten 2.-Gebirg.  Die  Lage  des  Zfr'  wird Yl.  rg.  I  ebenso  bestimmt  wie  die  der  Ifaraiti ; vyl.  unter /«/dya-.
Et.  und  Bed.7  Wohl  Komp.  mit  oder  Ableit aus  z>iid-.  —  ')  Oder  Stamm  'at-7    S.  No.  a.
—  >)  Oder  GS.  lu  'm-?;  S  3S6-  —  J>  So  nach der  unlergeschri ebenen  /'Jsini/Iesung  in  K. Der  Pahlaviteit  hat  zrdli,  worin  man  da* letzte  Zeichen  fälschlich  für  'und'  genommen hat.
■  j.  z«r98ö.k3r9ta-  Adj.  'das  Herz  heraus- schneidend': taica  narS  g?r^SJifntäs- (sd.)rtr  '/Jj(NPm.)A  V.7.24.
Komp.  mit  CS.  loa  1.  Glied.  —  Pü. :  dil  hrrf-
«iinömand.
•  j.  zöiinav-,  g.  zöiS«nav-  Adj.  (fem. "«£-)   'zusammenschreckend,    schaudernd,
dby  Google
i693
zoizdiSta-
zi  2  A
1694
bebend',  vor  Frost:  avi  lanuye  'nuye(,DS{.) V,7.  70;  —  mit  Gen.  (Abi.)  der  Ursache: aodinscä  "»S  (NDm.)  r/Jss{sd.)  Y.jr.  12.
Za  ioiia-.  —  Pü.:  ialäifn,  ialaiäien,    (lu  V.)
erl.!  «man. ■  j.  zöizdiäta-  Adj.  'der  schau derhaßeste, abscheulichste',  von  den  xrafslra-:  ajaitala 'laca  .  .  xrafslra  Yt. 21.  \\  —  ya\ia  -fäis xrafstrsis  V.  7.  a.
Snperl.     lu     einem    V.    *sSiU5-    'schaudern
machen',  vgl.  zöilnav-  and  vasdä- :  xtasdüla;
—  Pü. :  *baiaklum,  erl. :  rtmatilum.
•  ].,  g.  z^O«-  n.  'Geburt,  Entstehung; Erzeugung,  Erschaffung':  y3  ..  häirinnqm "hat  ^gariwqn  yaozdahäid  Y.  65.  2;  — fra  t!  '"kintca  vaxsak»mca  .  .  frasnaymi V.2/.6;  —  zara%uitrahe  .  .  yehe  '"haiia vaxsaS^a  urvassn  äpS  .  .  Yt  y.  93;  93', V.  2t.  4;  —  atfhSu^  '^si  paouruyekyä  "bei  | der  ErschafTiing  des  ersten  Lebens"  Y.  1 48.  6;  43.  Si—para  Ups  . .  dät?hsit  para  ' nari  .  .  •%3t  Y.  ig.&;  —  kasnä  '^a  pa/S  ; asakya  *paouruyö  "wer  ist  durch  Er- schaffung der  Vater  des  A.,  der  erste?" Y.44-3.  [Y.^ÄS:  lies  aipjzqkim?^
KompE.  —  Zum  V.  tzan-,  aus  ar.  'saniha-, S  13.  —  Pü.:  zät,  (lu  V.  31):  zäyisn,  Ua  Y. tg)i  dahisn.
•  j.   zahyamna-  Adj.,  PPi7(Fut.)M,:  s.
Pü.:  iiyunömand.
•  j.  z^Ora-  n.  'Geburt':  °ra  F. 20.
Zum  V.  'sn«-.  —  tti.  vgl.  janilra-  n,  'Geburts- slätle';  s.  daiu  Bthl.  IF.  7.  70.  —  Pü.:  =j'.
•  j.,  g.  zi  enkl.  Part,  hinter  dem  ersten Wort  des  Satzes";  I)''  der  sf-Satz  be- gründet den  Inhalt  eines  andern  Satzes, dem  er  i)  folgen,  2)  vorausgehen,  3}  ein- gefügt sein  kann;  'denn;  ja';  a)  im  gAwr.; zu  i):  mä  Hs..dr>gvatü  rna^rqsca  gastä sasmis(sd.)c,l  *il  *zT  dsmSitim  vJsfm  vä  . . ädä^  dusi/ä(sd.y3  marakaicä  "keiner  . . höre  auf  des  Z'r«<f genossen  Worte  .  .; denn  Haus  und  Gemeinde  .  .  bringt  er in  Elend  .  ."  Y.J/.  iS;  —  /?m  .  .  *a.vT- vansö  (Sp.  1377  o.)  na  zU  (Sp.  154  u.) ialmainX  vyadarpsim  .  .  Y.  45.  S;  30.  10 {adiJ  zl  .  .);  —  at  yastsm  iwil  nä  is>mttS äya/ (Sp.  150  o.)  drU/J  hvs  dämqn  */iae- %ahyä  ffdj  (Sp.  517  m.)  AvS  zT  dngvä  yS dngziäit!  vahUtS  hvS  asavä  yahmäi  ai'avä /ryS{%A.)  Y.46.6;  —  atlöi  af)h>n  saofyantö (sd.)  dahyunqm y5i..isi  sj data  kamaistärS lsd.)*aa)/mäiyaY.4S.i3; 34.S  {iais sT..),
53-  S  ('"^  'f  ■  ■);  —  vaoc3  mdi  . .  kat (Sp.  436  o.)  asava  . .  vSnghat  dr>gvanl>mi ha  al  atjhsul  vaaukl  vista  (Sp.  1315  n.) ak^rTfil  Y. 48.  z;  —  at  tSi  myazd?m  .  . dama  .  .  arsi  (Sp.  185  o.)  «r  hudärthS vTspäi}  . .  x/nävasS  sav5  Y.34.  3;  50.  $ (arBi  et);  —  pjr^a{Sp.  998  m.}/J  na  yü tut  Shma  parita  parttsm  sT  %wa  yahanü tai  !mavatq$n  Y.43.10;  51,8  {vidusi zT..);
—  s.  noch  at  zi  (Sp.  70).  b)  im  jAw.: kB  Kirim  imqm  eqm  mazUta  xinaoma xsnävayäiii . .  yaj  bä  paiti  frasshm  kära- ydti  .  .  »Sit  zl  im  za  sä  (sd.)  ya  dar/ya akarlla  salta  V.j.23f.;  P./5;  —  airya- maram  tl  ihm  ntazistsm  mraomi  .  .  sra- vaaham  t>m  zT..  sravatsham  uparff.kairtm fradä^qm  FiW.4-i;  Y.  77.13,  Yt.y.76;
—  daiva  .  .  daxmaliva  gaahinii  apala vaipaiti  ..aisS{\it^.daxmB)  zX  asti  dania- nqm  rapakdi^A.)  ¥.7.56;  44,  5.11,  15.  28, N.  22 ;  —  nalcis  ai^anniqm  tva  . .  i^äsaya zJ  visps  anhul .  .  *jvaiti  V,  _j,  33;  — mäca  .  .  astvalahe  aahSus  didnzvS  pTsa (sd.)  manahfm  paiti. raixsJ^a  yU  zl  ..  di- dr)zvS plsa  *manahlm  ahüM  *paiii.irinaxli nsit  Al  gäul  bvat  .  .  P.40;  —  mikr»m mä  /auyä  .  .  mä  yim  drvatat  pinshrahe tnäyim  . . alaonat  tivaya  zi asti(Sp.2Tou.) mi^rS drvatasca  asaonalcaYt.  SO.  2;  ^.84;
—  aBatca  alsqm  uxhanqm  uJ^S.tamitn  (sd.) .  .  asli  zt  ana  avuvat  wäala  (sd.)  Y. ig.  10;  —  anaäi  aiibyS  *spä*?haiti  ..  "spa- yeili  (Sp,  lörs  m.)  zl  .  .  dama  mäzda- yasnis  . .  V.J.  40  f.;  —  s.  noch  Yt.  Ä55 bei  6  und  Anhang.  zu  i) ;  a)  im  gAw. : ahurahyä  zT  al  vi  mazda  yasrumla  vaA- mimca  vahistim  amshmaidl  .  ,  tat  at  vS V)r?zyamahl  Y.  J5.  7.  b)  im  jAwr.: hakirit  zl  irixtahe  (sd.)  sa^ayaca  vaS- naile  starasca  viasca  Imanca  taica  ayar? maiiiyente  yat  ySn  V.  2.  40  f. ;  —  paravS (Sp.  855  m.)  zt  ma^yäka  .  .  pattiJämm *aimm(sd.)  baraiti  anaiwyästS  datnqm  V. 18.  r.  zu  3);  nur  a)  im  gAw.:  nü  Im vispä  —  li%r}  zl  ~  *mazdar3hS.düiii  (Sp. 1181  o.)  \.45- 1-  2)=>  mit  zl  wird  die Satzaussage  als  etwas  allbekanntes,  selbst- verständliches, unleugbares  hingestellt,  'ja; allerdings,  freilich';  a)  im  gAvw.r  hvB  zt  .. spptttB  irixljm  vlspSibyB  (4j/"fl'(sd.)  mainyü *aAam.iis  (sd.)  urva'^B  Y.  44.  2;  51.8  (kvs «r..);  —  vidainm{%A)  ..ha  zi pourüs  il>ntö väuräi/l(Sp.  1361  u.)  Y.  47.  6;  —  s,  noch
dby  Google
I69S
zi  2  B
i  Noten
1696
y.^4.14  (tattl..)  bei  4;—  im  Neben- satz :  täcä  sp»nt3  mainyü  . .  aiävnZ  Isi^ (Sp.  430  o.)  yä  zi  Mä  vahista  Aanar? %waAmai  zaosäi  dr?gvä  baxsaitl  (sd.)  Y. 47.  S;zT.  verwendet  Y.J2.I.  B)imjAw.: JvB  %J  . ,  mairyS  drrä  .  .  ap>m  Jainti  .  . tiöil  ava%a  m>r>t5  "so  lang  er  lebt,  trifft er  allerdings . .,  nicht  (aber)  so,  wenn  er  tot ist"  V.j.36f..:38; — vJsfe  zJ anje*maiiank0 (sd.)  atima  kacitUe . .  sai  hö  yO  haomahe ma}iB  asa  hacaite  "alle  andern  Rausch- tränke  sind  freilich . .,  aber , ."  Y.  lo.  8;  — in  unregelmässiger  Stellung":  ümssaiibyö spmtaiibyd  . ,  ysi  i>at^fiSui  ä  manarshö syänti;  vatthiul  3^'  tt  ä  inaiianhB  fyeinti yHi  amysa  spmia  Yt.ii.ii.  3)'>  si steht  in  Sätzen,  die  a)  eine  Willens- erklärung oder  b)  eine  Aufforderung  ent- halten 'so  —  denn,  denn';  a)  im  gAw.; zu  a):  //m  zT  v?  *sp)r>tiä  * nivarä nT  {Sp. 136a  m.)  Y.5J.4;  —  s.  noch  aj  s] (Sp.  70).  zu  b)  /iä  tX  n?  AuM>?mä (sd.)  Aä  ni  utayuUm  dat  \.4S.  6.  B)im jAw.;  zu  b):  alte  zT  (näml.  väc5)  tara- ^ußra  .  ./ramrüili  Y.  7/.  14.  4)"  Der
Satz  mit  zi  enthält  eine  erläuternde  Aus- führung oder  Ergänzung  'nämlich,  und zwar',  a)  im  gAw.,  nur  hinterm  Pron. rel.^':  matdä  seu^HrJ  (sd.)  tnairistö  yä  ZJ j'ävfryssi  , .  yäcJ  varHaiti  Y.  25.  4;  — vispaAtSi  hujUayS  (sd.)  ya  tl at»har7 yasla h?nt!  Y.J'J.  10;  —  iä  %wil  pnsü  . .  yä (NPn.)  ZI  3i>i-(Sp.  148  m.)  finghatt^a  Y. $1. 14;  — yehya  savä  (sd.)  Üantx  radanhs ySi  zl  jva  *awAai-j{Sp.  267  m.)!:"*  brantna Y. 45.T,  —  tat  zl  (zu  Z) . .  vairim  astvaili (sd.)  u/tanai  data  . .  yni  zt  gsus  v>r?z}m (sd.)  azyä  Y._j^i4.  b)  im  jAw.;  im Hauptsatz:  ahumintfm  ratum^ntim  . ,  ayese yesti  hs  zl  asti  *ahumaca  *ratumaca  yd ahurS  mazdä  Vr.  2.  7;  —  tanu.mazS  (sd.) asayäili y^ ..tanu.mazd  zl*agtqni^it  asayqm *pa/re  *yaJ..P.iS;  —  im  rel.  Nebensatz: yazamaide  %wqm  maf^ana//e  (sd.)  paiti  .. drvaßaos  .  .  yahmi  zt  iaal  ianurtam dräßstmt  (sd.)  kamt  mai^aiiie  trii^riSJ V.16.10.  S)  ersteht  in  Fragesätzen, bes.  a)  hinter  dem  Interrog.,  'denn';  nur b)  im  jAw.:  tßm  zT  alfa  . .  anaiioyastis (sd.)  kunahii  V.  18. 10;  —  zu  a):  paili dim  p>nsai  zarahustrS:  kai  sT  asli  .  . tistryehe  .  .  daityi}.tJm3  yasnasca  vahmasca Yt-  «y-  57;    —    kalärS   zT  aya    vthrkay'
\jq%aiBJarS  *at»hat  V. /j.  41; —  *kva.^ra *£(*'  /i>nH  iristanqm  urjqnffTiVf,  10.  ^g;
—  in  auffälliger  Stellung"':  in  Auye/ti(sd.) kS  duiyesti  mqm  zl  mainyete  yasatim  Yt 10. 108.  6)  zl  dient  zur  Hervorhebung des  vorhergehenden  Wortes;  nur  b)  im jAw.:  nöit  zt  ahurB .  .yatikuyanqin  avars- tanqm  *paitiricya  dat^e  V.5. 60;  7. 52, FrW.  Ä  1;  —  ma  Zl  ahmt  nmane../rlm vao.'aia  mqm y'im  ahunm  mazdqm  yaka  . . P.iy;  —  a%a  zl mraoi a/iurS  »lazdä  A.4-3', Vr.  i2. 4',  V.  ;o.  19;—  aXe  zi  väcS . .  aAurd macdä  främraot  zard^uslrai  \.yi.  14;  H. J.4,  V.^49, /J.41,  Yt./4- iz;  —  alvahe zi*ai?mao-jahe ..zaiiu.dräja  asti  s/riti/(sd.) dvayä  ..  V.  JA  11;  4.47, 5.  41,  N.  ö',?;  — mliti  zi  ml  Alm  ..värvniaica  ..^1.$.  iio;
—  anijai/i  zi..  ali'a  asff.itGiti/ . .  H.i.  5; V.5,42;  —  in  unrcgelmässiger  Stellung": ^wä paiti  zt  Aaxxnm  (sd.)  daiüe  vaAisttm Yt.  10.  80.  a)  im  Nachsatz:  yasca tili  tiiyas^a  sadirra  frabaral  dazat  si mqm  . .  P.  22;  —  yat  ^riilm  dali'ayasnd hnntat  ava  AB  miryjite  anamätö  sf  al^S ^■7-ZTy  39;  —  y^  anAat  ä'^rava  frä zl  dvqsaiti  .  ,  druxl  V.  5.  aS;  —  y&i  zl (s.  Anh.  2)  azim  nSil  daioyqm . .  tiärim . . AamaAe  zl  ml  iha  ayqn  .  .pairika  .  .parlit pairiirt>m(sd.)a»AvqmavaMsiiyst..ti/tryB zl  (zu  I ) . .  avqm  pairikqm  adanzayeiti  Yt ^■5*~SS-  S.  noch  Anhang.  Anhang. 3l  hinter  Konjunktionen;  nur  b)  im  jAw.; i)  yat  zi;  zu  i:  yai  zi . .  airyä  datrihävö tistryeAe . .  aiwi.sacyar)s  daitim  yasmmca . . mit  . .  Yt.  8.  56.  2)  y^i  zi,  yetU  zi (Sp.  i239f.);  zu  I):  azfm  datqm  ..  asS ramS.daitlm  (sd.) .  .yeuti  si, ,  nlit  daioyqm ..vispB  anhuS . .  airyamm  vaijS  fräsm-St V./.i;  Y.7/.is,Yt.Ä52,/j.i2;  — zu*)' yeßti  zi  mä  masyaka  .  .  yazayanta  .  .  ari mqm  az-i.baioryqm  dasanqm  aspanqm  aojs YiS.74;  II,  ff.*3,  /o.sS,'74-  gAw.  at zi  und  'yezl  sbcs.
Aus  dem  Zusammenhang  gerissene  oder
sonst  undeutliche  Stellen:  Aog.  4!<;,  V.  4.
```


## [2026-09-06T21:04:51.682Z] TOOL CALL #92: Bash

```json
{
 "command": "tail -12 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('url'))\n\""
}
```


### [2026-09-06T21:04:53.562Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A4%BF%E0%A4%B7%E0%A5%8D
https://en.wiktionary.org/wiki/%D9%85%D9%82%D9%84%D8%A7%D8%AF
https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE
https://lamtakam.com/dictionaries/dehkhoda/320125/سرود
https://abadis.ir/fatofa/سروا/
https://en.wiktionary.org/wiki/%D9%82%D9%84%D9%85
https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CE%BB%CE%B1%CE%BC%CE%BF%CF%82
https://www.etymonline.com/word/caramel
https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%A3%E0%A4%BF
https://en.wiktionary.org/wiki/clunis
https://www.avesta.org/avdict/avdict.htm
https://abadis.ir/fatofa/%D8%B4%D9%85%D9%86/
```


## [2026-09-06T21:05:00.974Z] TOOL CALL #93: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nwant=[\"ceterus\",\"%CF%83%CE%AE%CF%82\",\"%CE%BE%CE%AF%CF%86%CE%BF%CF%82\",\"D8%B3%D9%88%D8%B3\",\"%D6%81%D5%A5%D6%81\",\"abadis.ir/fatofa/ساس\",\"D8%B3%D9%8A%D9%81\",\"%C7%B5%CA%B0e\",\"%E0%A4%B6%E0%A4%BF%E0%A4%AB%E0%A4%BE\",\"et%20cetera\",\"etymonline.com/word/he\",\"Proto-Indo-European/%E1%B8%B1e\"]\nfor l in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    d=json.loads(l); u=d.get('url','')\n    if any(w in u for w in want): print(u)\nEOF"
}
```


### [2026-09-06T21:05:02.723Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%88%D8%B3
https://www.etymonline.com/word/hectare
https://www.etymonline.com/word/et%20cetera
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eh%E2%82%81-
https://www.etymonline.com/word/heir
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eys-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ey-
https://www.etymonline.com/word/heap
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ers-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eng%CA%B0-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0er-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ewH-
https://www.etymonline.com/word/hegira
https://en.wiktionary.org/wiki/ceterus
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1eh%E2%82%82d-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1el-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ens-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1erd%CA%B0-
https://www.etymonline.com/word/hearth
https://www.etymonline.com/word/heart
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ewk-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ewh%E2%82%81-
https://www.etymonline.com/word/hear
https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%88%D8%B3
https://abadis.ir/fatofa/ساس/
https://www.etymonline.com/word/he
```


## [2026-09-06T21:05:15.471Z] TOOL CALL #94: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nids=[\"a7141d49cece5cce\",\"c742570e15eb8b62\",\"c364664646fe64e0\",\"48c35506fde8483b\",\"f935493871a88b47\",\"42ad08b35edf73c3\",\"f545715fe63f50a9\",\"9f1f92c017f3dcfe\",\"32c9f44c17052417\",\"17191585fc576706\",\"8758d7a34cc492c8\",\"953c8c7f810d9f1c\"]\nfound={}\nfor l in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    d=json.loads(l)\n    for k,v in d.items():\n        if isinstance(v,str) and any(i in v for i in ids):\n            found[v.split('/')[-1].split('.')[0]]=d.get('url')\nfor i in ids: print(i, found.get(i))\nEOF"
}
```


### [2026-09-06T21:05:17.182Z] TOOL RESULT

```
a7141d49cece5cce https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱe
c742570e15eb8b62 https://en.wiktionary.org/wiki/ξίφος
c364664646fe64e0 https://en.wiktionary.org/wiki/ceterus
48c35506fde8483b https://en.wiktionary.org/wiki/σής
f935493871a88b47 https://en.wiktionary.org/wiki/سوس
42ad08b35edf73c3 https://en.wiktionary.org/wiki/ցեց
f545715fe63f50a9 https://abadis.ir/fatofa/ساس/
9f1f92c017f3dcfe https://en.wiktionary.org/wiki/سيف
32c9f44c17052417 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵʰe
17191585fc576706 https://en.wiktionary.org/wiki/शिफा
8758d7a34cc492c8 https://www.etymonline.com/word/et%20cetera
953c8c7f810d9f1c https://www.etymonline.com/word/he
```


## [2026-09-06T21:13:19.387Z] TOOL CALL #95: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk267.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_KE   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱe\"\nW_GHE  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵʰe\"\nW_CET  = \"https://en.wiktionary.org/wiki/ceterus\"\nW_SES  = \"https://en.wiktionary.org/wiki/σής\"\nW_SUS  = \"https://en.wiktionary.org/wiki/سوس\"\nW_CEC  = \"https://en.wiktionary.org/wiki/ցեց\"\nW_SAS  = \"https://abadis.ir/fatofa/ساس/\"\nW_SAYF = \"https://en.wiktionary.org/wiki/سيف\"\nW_XIPH = \"https://en.wiktionary.org/wiki/ξίφος\"\nW_SIPH = \"https://en.wiktionary.org/wiki/शिफा\"\nE_ETC  = \"https://www.etymonline.com/word/et%20cetera\"\nE_HE   = \"https://www.etymonline.com/word/he\"\n\ndoc = {\n \"pdf_page\": 267,\n \"book_page\": 237,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n\n # ------------------------------------------------------------------ entry 0\n {\n  \"entry\": 0,\n  \"root\": \"Ki 2, Ko 2, Kyô, Ke 2, Ghe 2\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"PIE *ḱi- ~ *ḱe- ~ *ḱo- (also *ḱ(i)i̯o-) 'this (here)', deictic particle and pronominal stem — Pokorny 609 'ḱo-, ḱe- (mit Partikel ke «hier»), ḱ(e)i-, ḱ(i)i̯o- Pronominalstamm «dieser»'; Nourai's fifth alias 'Ghe 2' is a DIFFERENT root, the enclitic emphasising particle *ǵʰe / *ǵʰo / *ǵʰi (Pokorny 417)\",\n  \"note\": \"Root name, language label and gloss are all correct for the *ḱi-/*ḱe-/*ḱo- half of the box: Pokorny p.609 heads the entry exactly as Nourai's four first aliases (Ki 2 = ḱ(e)i-, Ko 2 = ḱo-, Ke 2 = ḱe-, Kyô = ḱ(i)i̯o-) and glosses it 'dieser', and Klein p.710 s.v. 'he' has 'I.-E. base *ki-, «this one»'. The caveat is the fifth alias, 'Ghe 2': Pokorny p.417 treats *ǵʰe-, *ǵʰo-, *ǵʰi- as a separate entry ('enklitische Partikeln zur Verstärkung des vorhergehenden Wortes'), and modern handbooks (Wiktionary's two separate reconstruction pages, Dunkel's Lexikon der Partikeln) keep the demonstrative *ḱe and the emphatic *ǵʰe strictly apart. Nourai is following Klein, who at p.735 s.v. 'hodiernal' derives the hi-/he- of Latin hic from the *ǵʰe-particle and then says 'See he' (p.710) — the two do in fact meet inside one Latin word, hi-c < *ǵʰi-ke, which is presumably why Klein and Nourai file them together. Merging them in one root box is therefore defensible but not the modern analysis, hence 'plausible' rather than 'confirmed'.\",\n  \"note_fa\": \"این جعبه در واقع دو ریشهٔ جداگانه را در هم آمیخته است. نیمهٔ نخست، یعنی «Ki 2, Ko 2, Ke 2, Kyô»، همان ریشهٔ هندواروپایی آغازین *ḱi-/*ḱe-/*ḱo- (و *ḱ(i)i̯o-) به معنی «این» است که پوکورنی در ص ۶۰۹ دقیقاً با همین چهار صورت و با معنی «dieser» آورده و کلاین نیز در ص ۷۱۰ ذیل he آن را «*ki- این» ثبت کرده است؛ تا اینجا ادعای نورایی درست است. اما «Ghe 2» ریشهٔ دیگری است: ادات پیوستهٔ تأکیدی *ǵʰe/*ǵʰo/*ǵʰi که پوکورنی در ص ۴۱۷ جداگانه آورده و ریشه‌شناسی امروزی (ویکی‌واژه، دونکل) آن را از *ḱe- جدا نگاه می‌دارد. نورایی در این ادغام از کلاین پیروی کرده، زیرا کلاین در ص ۷۳۵ ذیل hodiernal جزء hi-/he- در لاتینی hic را از همان ادات تأکیدی می‌گیرد و به مدخل he ارجاع می‌دهد؛ و به‌راستی در واژهٔ لاتینی hic < *ǵʰi-ke هر دو ریشه کنار هم آمده‌اند. بنابراین ادغام قابل دفاع اما نه دیدگاه امروزی است: با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_KE, W_GHE, E_HE],\n  \"ref_check\": [\n    {\"ref\": \"POK:609\", \"status\": \"supports\",\n     \"note\": \"Pokorny IEW p.609, read in POK_02.txt at the page marker '609' (line 4195): 'ḱo-, ḱe- (mit Partikel ke «hier»), ḱ(e)i-, ḱ(i)i̯o- Pronominalstamm «dieser», ursprünglich ich-deiktisch, später auch «jener»; ḱi-na «hinweg»'. Exactly Nourai's Ki 2 / Ko 2 / Ke 2 / Kyô and the gloss 'this'.\"},\n    {\"ref\": \"POK:417\", \"status\": \"supports\",\n     \"note\": \"Pokorny IEW pp.417-418, POK_02.txt leaves 74-75 (awk 'BEGIN{RS=\\\"\\\\f\\\"} NR==74,NR==75'): 'ǵʰe-, ǵʰo-, ǵʰi- u. ähnliche enklitische Partikeln zur Verstärkung des vorhergehenden Wortes ... 2. -ǵʰi: in ai. hi, av. zī hervorhebende Partikel (ná hi, nahí, av. nōit zī)'. This is Nourai's 'Ghe 2' and it is a separate Pokorny entry from p.609.\"},\n    {\"ref\": \"KLN:710\", \"status\": \"supports\",\n     \"note\": \"Klein 1966 p.710 s.v. 'he' (KLN_1966.txt line 17340, right after the page marker '710'): 'I.-E. base *ki-, «this one», whence also Hitt. ki «this», Gk. ἐκεῖ «there» ... L. cis, citer, citra «on this side», ce- and -ce, emphatic particles meaning «here, there», OSlav. si, Lith. šis «this». Cp. him, her, it, hence, here, hither. Cp. also cede, cis-, citra-, cy-pres, et cetera, hodiernal, sic.' — the whole English list and the et-cetera branch of Nourai's chart come from this one Klein entry.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ko- (AHD_watkins1985.txt line 642)\", \"stance\": \"supports\",\n     \"note\": \"'ko-. Stem of demonstrative pronoun meaning «this.» I. Variant form *ki-. 1. Germanic *hi- ... II. Variant form *ke-. 1. Preposed in *ke-etero- ... [Pok. ko- 609.]'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I pp.452-453 (WLD_Bd1_pages.txt leaves 461-462)\", \"stance\": \"supports\",\n     \"note\": \"Running head of p.452 reads 'kiph- — ko-, ke-'; the entry continues on p.453 with 'lat. -ce, ce-Partikel in ce-do «gib her» ... ceterus «der andere, der übrige» (*ce oder *cei ... + *etero-, vgl. umbr. etru «altero»)'.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/ḱe\", \"stance\": \"supports\",\n     \"note\": \"'*ḱi- ~ *ḱe- ~ *ḱo- (or *-ḱe): deictic particle, here; post-positional demonstrative particle, this'; descendants Hittite ki-i, Latin hic/haec/hoc, English he, him, his, here, hence.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/ǵʰe\", \"stance\": \"partial\",\n     \"note\": \"*ǵʰe/*ǵʰo/*ǵʰi is given its OWN page, 'postpositional intensifying particle: indeed, at any rate, in fact', with Sanskrit ha/gha, Greek γε, Lithuanian -gi — i.e. modern practice separates Nourai's 'Ghe 2' from 'Ki 2'.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Avestan\", \"words\": \"zî; nôit-zî\", \"verdict\": \"confirmed\",\n    \"derivation\": \"Avestan zī is the enclitic emphasising particle that stands after the first word of the sentence, 'for, because; indeed, of course' (Bartholomae, AiW cols. 1693-1696: 'zi enkl. Part. hinter dem ersten Wort des Satzes ... «denn; ja»'). It is the exact match of Vedic hí and continues PIE *ǵʰi, the i-grade of the enclitic *ǵʰe/*ǵʰo: the PIE palatal voiced aspirate *ǵʰ gives Proto-Indo-Iranian *ǰʰ, which yields Sanskrit h- but Avestan z- (as in Skt. hánu- : Av. zānu-), so *ǵʰi > PII *ǰʰi > Av. zī with the regular lengthening of the enclitic vowel. nōit zī 'for … not' is a fixed collocation of the negation nōit with the particle, quoted by Bartholomae from Vidēvdād 5.60 (nōit zī ahurō …) and listed by Pokorny p.418 in the same shape 'av. nōit zī'. The node therefore belongs to the 'Ghe 2' half of Nourai's root box, not to the *ḱi- demonstrative; the two roots meet only in Latin hi-c (< *ǵʰi-ke).\",\n    \"derivation_fa\": \"«zī» در اوستایی ادات پیوستهٔ تأکیدی است که پس از نخستین واژهٔ جمله می‌آید و معنی «زیرا، چه، به‌راستی» دارد؛ بارتولمه در فرهنگ ایرانی باستان (ستون ۱۶۹۳-۱۶۹۶) آن را چنین تعریف می‌کند: «zi ادات پیوسته پس از واژهٔ نخست جمله … «denn; ja»». این واژه برابر دقیق hí در سنسکریت است و از *ǵʰi هندواروپایی آغازین می‌آید: انسدادی کامی واکدارِ دمیدهٔ *ǵʰ در هندوایرانی به *ǰʰ بدل شده و سپس در سنسکریت h و در اوستایی z داده است (همانند Av. zānu- در برابر سنسکریت hánu-). ترکیب nōit zī «زیرا نه» نیز صورتی ثابت است که بارتولمه از وندیداد ۵٫۶۰ و پوکورنی در ص ۴۱۸ به همان شکل «av. nōit zī» نقل کرده‌اند. پس ادعای نورایی درست است؛ تنها باید توجه داشت که این گره به نیمهٔ «Ghe 2» ریشه تعلق دارد نه به ضمیر اشارهٔ *ḱi-.\",\n    \"sources\": [W_GHE],\n    \"ref_check\": [\n      {\"ref\": \"KLN:735\", \"status\": \"supports\",\n       \"note\": \"Klein 1966 p.735 s.v. 'hodiernal' (KLN_1966.txt line 17918, between the page markers 735 and 736): 'Particle hi-, he- is cogn. with the emphatic particles: OI. gha «just, indeed, certainly», ha «of course, surely», OI. hi, Avestic zi, «for, because; surely, indeed» ... See he.' Nourai's gloss 'for, because, indeed' is copied verbatim from Klein.\"},\n      {\"ref\": \"POK:417\", \"status\": \"supports\",\n       \"note\": \"Pokorny p.418 (POK_02.txt leaf 75): '2. -ǵʰi: in ai. hi, av. zī hervorhebende Partikel (ná hi, nahí, av. nōit zī) ... hinter dem ersten Wort des Satzes «denn ja»' — both of Nourai's words, zī and nōit-zī, stand on the cited page.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 1693-1696 s.v. zi 2 (BRT.txt lines 28150-28180)\", \"stance\": \"supports\",\n       \"note\": \"'j., g. zi enkl. Part. hinter dem ersten Wort des Satzes ... «denn; ja»'; §6 'zi dient zur Hervorhebung des vorhergehenden Wortes; nur im jAw.: nōit zī ahurō … V.5.60' — Nourai's nôit-zî is Bartholomae's first citation there.\"},\n      {\"src\": \"POK\", \"where\": \"IEW pp.417-418\", \"stance\": \"supports\", \"note\": \"see ref_check; av. zī and nōit zī printed on the cited page.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/ǵʰe\", \"stance\": \"supports\",\n       \"note\": \"Sanskrit ह (ha), घ (gha), Greek γε, Lithuanian -gi listed as reflexes of the postpositional intensifier; the Iranian z-form is the expected Avestan outcome of *ǵʰ.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Germanic\", \"words\": \"hi\", \"verdict\": \"confirmed\",\n    \"derivation\": \"Proto-Germanic *hi- is the near-deictic pronominal stem inherited from PIE *ḱi-, the i-grade of *ḱe-/*ḱo-. The consonant is regular: PIE palatal *ḱ merged with plain *k in the centum branches and Grimm's Law then gave PGmc *h- (compare Latin cis, citer beside Gothic hidrē, OE hider). Pokorny p.609 lists the Germanic material under the root — Gothic himma 'huic', hina 'hunc', hita 'now', hēr 'here', hidrē 'hither', ON hánn 'he', OS/OHG he, her 'he', OE hē — and Watkins/AHD reconstructs precisely 'Germanic *hi-'. The stem survives only in oblique and adverbial forms in most of Germanic; English is exceptional in keeping it as the ordinary third-person pronoun.\",\n    \"derivation_fa\": \"ستاک اشارهٔ نزدیک در ژرمنی آغازین *hi- است که مستقیماً از *ḱi- هندواروپایی آغازین (گونهٔ i-دار ریشهٔ *ḱe-/*ḱo-) به ارث رسیده است. تحول آوایی قاعده‌مند است: *ḱ کامی هندواروپایی در شاخه‌های کنتوم با *k ساده یکی شده و سپس بر پایهٔ قانون گریم در ژرمنی به *h بدل گشته است (بسنجید با لاتینی cis, citer در برابر گوتی hidrē و انگلیسی کهن hider). پوکورنی در ص ۶۰۹ صورت‌های ژرمنی را زیر همین ریشه آورده است: گوتی himma، hina، hita، hēr، hidrē؛ نورس کهن hánn؛ ساکسون کهن و آلمانی علیای کهن he، her؛ انگلیسی کهن hē. واتکینز نیز دقیقاً «Germanic *hi-» بازسازی می‌کند. ادعای نورایی درست است.\",\n    \"sources\": [W_KE],\n    \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. ko-: 'I. Variant form *ki-. 1. Germanic *hi- in: a. Old English hē, he: HE¹ ...' — the label 'Germanic' and the form 'hi' are Watkins's own.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.609-610 s.v. ḱo-, ḱe-\", \"stance\": \"supports\",\n       \"note\": \"'got. himma «huic», hina «hunc», hita n. «jetzt» ... got. hēr, ahd. hiar, ags. hēr «hier» (*ḱei-r); got. hidrē, ags. hider, engl. hither «hierher» (: lat. citer, citrō)'.\"},\n      {\"src\": \"KLN\", \"where\": \"1966 p.710 s.v. he\", \"stance\": \"supports\",\n       \"note\": \"'ME. he, fr. OE. hē [fem. hēo, hio, neut. hit; pl. hī, hie], rel. to OS., OFris. he, hi ... I.-E. base *ki-, «this one»'.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"English\", \"words\": \"he, him, his, her, here, hence, it\", \"verdict\": \"confirmed\",\n    \"derivation\": \"All seven are Old English forms of the one deictic stem *hi-: hē (nom. sg. m.) > he; him (dat. sg., which ousted the accusative hine in Middle English) > him; his (gen. sg.) > his; hire (gen./dat. sg. fem. of hēo) > ME hire > her; hēr 'in this place' (< *ḱei-r, cf. Gothic hēr, OHG hiar) > here; heonan/heonane 'from here', to which the adverbial genitive -es was added in Middle English (hennes) and later respelled with -ce > hence; and hit (nom./acc. sg. n., h- lost in unstressed position after c.1200) > it. Watkins/AHD lists exactly these seven words, in this order, under I.1.a-g of the root ko-, so the node is copied straight from Nourai's cited reference and is correct.\",\n    \"derivation_fa\": \"هر هفت واژه صورت‌های گوناگون یک ستاک اشارهٔ انگلیسی کهن‌اند: hē (فاعلی مفرد مذکر) ← he؛ him (برایی مفرد که در انگلیسی میانه جای صورت مفعولی hine را گرفت) ← him؛ his (اضافی مفرد) ← his؛ hire (اضافی/برایی مفرد مؤنث از hēo) ← انگلیسی میانه hire ← her؛ hēr «در اینجا» (از *ḱei-r، بسنجید با گوتی hēr و آلمانی علیای کهن hiar) ← here؛ heonan «از اینجا» که در انگلیسی میانه پسوند اضافی قیدی ‎-es‎ گرفت (hennes) و سپس با ‎-ce‎ نوشته شد ← hence؛ و hit (فاعلی/مفعولی مفرد خنثی که h آغازین آن در جایگاه بی‌تکیه پس از حدود ۱۲۰۰ میلادی افتاد) ← it. واتکینز در پیوست ریشه‌های هندواروپایی دقیقاً همین هفت واژه را به همین ترتیب زیر ریشهٔ ko- آورده است؛ پس ادعای نورایی درست است.\",\n    \"sources\": [E_HE, W_KE],\n    \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. ko-: '1. Germanic *hi- in: a. Old English hē, he: HE¹; b. Old English him, him: HIM; c. Old English his, his: HIS; d. Old English hire, her: HER; e. Old English hit, it: IT; f. Old English hēr, here: HERE; g. Old English heonane, heonon, from here: HENCE.' — Nourai's seven words verbatim.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 p.710 s.v. he\", \"stance\": \"supports\",\n       \"note\": \"'Cp. him, her, it, hence, here, hither' — Klein's cross-reference list under the same base *ki-.\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.609-610\", \"stance\": \"supports\",\n       \"note\": \"'ags. hē ds. ... got. hēr, ahd. hiar, ags. hēr «hier» (*ḱei-r); ahd. hina «weg», nhd. hin'.\"},\n      {\"src\": \"Etymonline\", \"where\": \"word/he\", \"stance\": \"supports\",\n       \"note\": \"Old English hē traced to PIE root *ko-, the 'this, here' demonstrative, with the same family (here, hence, it).\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"Indo-European\", \"words\": \"Ke-e-tero\", \"verdict\": \"confirmed\",\n    \"derivation\": \"*ke-etero- is a compound formed inside pre-Italic by preposing the deictic particle *ḱe 'here' to *e-tero- 'the other (of two)', the *-tero- contrastive derivative of the pronominal stem *e-/*i- (Pokorny pp.283-284; modern notation *h₁é-teros). Pokorny states it under that stem: 'Zu e- auch die Komparativbildung av. atāra- «dieser, der von beiden», alb. jat(e)re «anderer», umbr. etro- «anderer», lat. in ceterus «der andere oder übrige»'. Watkins gives the compound in exactly Nourai's shape and refers the second element to the root i- — which is what Nourai's cross-reference '☞ I 2' means. The gloss 'other part, other time, again' is Watkins's own wording ('*e-tero-, a second time, again').\",\n    \"derivation_fa\": \"‏*ke-etero- ترکیبی است که در مرحلهٔ پیش‌ایتالیایی ساخته شده: ادات اشارهٔ *ḱe «اینجا» پیش از *e-tero- «دیگری (از دو تا)» نهاده شده است؛ و *e-tero- خود مشتق تقابلی با پسوند ‎*-tero-‎ از ستاک ضمیری *e-/*i- است (پوکورنی ص ۲۸۳-۲۸۴؛ در نگارش امروزی *h₁é-teros). پوکورنی می‌نویسد: «به e- نیز صورت تفضیلی اوستایی atāra-، آلبانیایی jat(e)re، اومبریایی etro-، و لاتینی در ceterus «دیگری یا باقی‌مانده» تعلق دارد». واتکینز همین ترکیب را به همان شکلی که نورایی آورده ثبت کرده و جزء دوم را به ریشهٔ i- ارجاع داده است؛ ارجاع «☞ I 2» در نمودار نورایی دقیقاً همین است. معنای «بخش دیگر، بار دیگر، دوباره» نیز عین عبارت واتکینز است. ادعای نورایی درست است.\",\n    \"sources\": [W_CET, E_ETC],\n    \"ref_check\": [\n      {\"ref\": \"AHD:1523\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. ko-, section II.1: 'Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin cēterus (neuter plural cētera), the other part, that which remains: ET CETERA.' Page 1523 is the 1975/76 New College Edition appendix, which is not open online; the 1985 standalone edition of the same list has the entry under ko-.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW pp.283-284 s.v. e-, ei-, i- (POK_01.txt lines 4049-4065)\", \"stance\": \"supports\",\n       \"note\": \"'Zu e- auch die Komparativbildung av. atāra- ... umbr. etro- «anderer», lat. in ceterus «der andere oder übrige», aksl. eterъ, jeterъ «irgendwer»'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.453 s.v. ko-, ke-\", \"stance\": \"supports\",\n       \"note\": \"'ceterus «der andere, der übrige» (*ce oder *cei ... + *etero-, vgl. umbr. etru «altero»)'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. ceterus (LAT.txt line 11516 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'Comprend évidemment le mot qui se retrouve en ombrien, avec le sens de «alter»: etru «altero» ... c'est le dérivé en *-tero-, *-tro- des thèmes du démonstratif i.-e. *e- et *i-'.\"}\n    ]\n   },\n   {\n    \"id\": 5, \"lang\": \"Latin\", \"words\": \"ce-terus; et-cĕ-terî\", \"verdict\": \"plausible\",\n    \"derivation\": \"Latin cēterus 'the other, that which remains' (in practice only plural, cēterī/cēterae/cētera) continues Proto-Italic *ke-eteros, i.e. the deictic particle ce-/-ce (as in ec-ce, hi-c, cis, citer, citrā, cedo) prefixed to *eteros; Umbrian etru 'altero' shows the second element alone. Ernout-Meillet note that cētera is regularly joined to omnes/cuncti and that the neuter is used adverbially (cēterum, cētera 'du reste'), which is how the phrase et cētera 'and the other things' arose in written Latin. Two details of the chart are wrong: the phrase that means 'and other things' is et cētera, the neuter plural, not 'et-cĕ-terî' (cēterī is the masculine nominative plural); and the vowel of the second syllable is LONG — Klein, Watkins, Pokorny and Ernout-Meillet all write cēterus, so Nourai's breve (cĕ) is misleading. The derivation itself is correct, hence 'plausible' rather than 'confirmed'.\",\n    \"derivation_fa\": \"واژهٔ لاتینی cēterus «دیگری، باقی‌مانده» (که در عمل تنها به صورت جمع cēterī/cētera به کار می‌رود) دنبالهٔ *ke-eteros ایتالیایی آغازین است: ادات اشارهٔ ‎ce-/-ce‎ (همان که در ec-ce، hi-c، cis، citer، cedo دیده می‌شود) پیش از *eteros «دیگری» نهاده شده است؛ صورت اومبریایی etru «altero» جزء دوم را به‌تنهایی نشان می‌دهد. ارنو و مه‌یه یادآور می‌شوند که cētera بیشتر همراه omnes و cuncti می‌آید و صورت خنثای آن (cēterum, cētera) کاربرد قیدی دارد؛ از همین‌جا عبارت et cētera «و دیگر چیزها» در لاتینی نوشتاری پدید آمده است. دو نکته در نمودار نادرست است: عبارتی که «و دیگر چیزها» معنی می‌دهد et cētera (جمع خنثی) است نه «et-cĕ-terî» (که جمع فاعلی مذکر است)؛ و مصوت هجای دوم کشیده است (cēterus در کلاین، واتکینز، پوکورنی و ارنو–مه‌یه)، حال آنکه نورایی علامت کوتاهی (cĕ) گذاشته است. اصل اشتقاق درست است، پس با احتیاط پذیرفتنی است.\",\n    \"sources\": [W_CET, E_ETC],\n    \"ref_check\": [\n      {\"ref\": \"AHD:1523\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. ko- II.1: 'in Latin cēterus (neuter plural cētera), the other part, that which remains: ET CETERA' — Nourai's gloss 'the other part' is Watkins's phrase, and Watkins gives the neuter plural, not cēterī.\"},\n      {\"ref\": \"KLN:545\", \"status\": \"supports\",\n       \"note\": \"Klein 1966 p.545 (KLN_1966.txt line 13712, after the page marker '544'): 'et cetera, «and other things». — L., fr. et, «and» (see et), and neut. of ceteri, «the others», which is formed fr. I.-E. pron. pref. *ce-, «there; behold» (see he), and I.-E. *etero-, «the other», whence also Umbr. etro- «another», Avestic a-tara- ...'.\"},\n      {\"ref\": \"POK:284\", \"status\": \"partial\",\n       \"note\": \"The sentence Nourai needs — 'lat. in ceterus «der andere oder übrige»' — stands in the *e-/*i- entry that runs IEW pp.281-286; in the Toronto scan (POK_01.txt) it falls between the page markers '283' (line 4049) and '284' (line 4065), i.e. at the foot of p.283 rather than on p.284. Same entry, one page off in the scan; the substance supports the arrow.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.453 s.v. ko-, ke-\", \"stance\": \"supports\",\n       \"note\": \"'lat. -ce, ce-Partikel in ce-do «gib her» ... ceterus «der andere, der übrige» (*ce oder *cei ... + *etero-, vgl. umbr. etru «altero»)'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. ceterus\", \"stance\": \"supports\",\n       \"note\": \"'ceterus, -a, -um: qui reste, restant, d'où au pl. ceteri, -ae, -a «tous les autres, ceux qui restent» ... Le neutre s'emploie adverbialement: ceterum, cetera «du reste»' — confirms that the 'and other things' sense belongs to the NEUTER plural cetera.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"ceterus (Latin)\", \"stance\": \"supports\",\n       \"note\": \"'From Proto-Italic *ke-eteros, from *ke («here») + *eteros («other»)', with derived term 'et cētera' and the long ē marked.\"}\n    ]\n   },\n   {\n    \"id\": 6, \"lang\": \"English\", \"words\": \"et cetera\", \"verdict\": \"confirmed\",\n    \"derivation\": \"Taken over into English as an unanalysed Latin tag, first recorded in the early 15th century; abbreviated &c. (the ampersand standing for et) until about 1900, after which etc. became standard. English never inflected it, so the phrase preserves the Latin neuter plural cētera unchanged; the anglicised pronunciation with initial et- and often /ˌet ˈsetərə/ reflects the ecclesiastical Latin of the medieval schoolroom rather than a native development.\",\n    \"derivation_fa\": \"این عبارت همچون یک ترکیب دست‌نخوردهٔ لاتینی وارد انگلیسی شده و نخستین کاربرد آن به آغاز سدهٔ پانزدهم میلادی بازمی‌گردد. تا حدود سال ۱۹۰۰ آن را به شکل ‎&c.‎ کوتاه می‌کردند (نشانهٔ ‎&‎ به جای et) و پس از آن ‎etc.‎ رایج شد. انگلیسی هیچ‌گاه آن را صرف نکرده است، پس صورت جمع خنثای لاتینی cētera در آن دست‌نخورده مانده است؛ تلفظ انگلیسی آن نیز بازتاب لاتینی کلیسایی مدرسه‌های سده‌های میانه است نه تحولی درون‌زبانی. ادعای نورایی درست است.\",\n    \"sources\": [E_ETC],\n    \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The book gives this node no reference of its own; it hangs on the Latin box above it (AHD:1523; KLN:545; POK:284), all of which were checked there.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 p.545 s.v. et cetera\", \"stance\": \"supports\",\n       \"note\": \"'et cetera, «and other things». — L., fr. et, «and», and neut. of ceteri, «the others»'.\"},\n      {\"src\": \"Etymonline\", \"where\": \"word/et cetera\", \"stance\": \"supports\",\n       \"note\": \"'early 15c., from Latin et cetera, literally «and the others» ... cetera, neuter plural of ceterus «the other, other part, that which remains»'; the abbreviation &c. was usual before the 20th century.\"}\n    ]\n   }\n  ]\n },\n\n # ------------------------------------------------------------------ entry 3\n {\n  \"entry\": 3,\n  \"root\": \"Kiĕs\",\n  \"verdict\": \"disputed\",\n  \"modern_form\": \"No Indo-European root: the words are reflexes of a Semitic culture word — Proto-Semitic *sūs- 'moth; biting insect', Akkadian sāsum, Hebrew סָס sās, Aramaic/Syriac sāsā, Arabic سوس sūs 'moth-worm, weevil'\",\n  \"note\": \"The chart reproduces Mann, IEC 622, faithfully — his entry reads 'Kies «mite, tick, vermin». (Variant: Kis-) Per. sās «bug, louse»; Oss. sasḱ «liver-fluke» beside saska «midge»; Arm. cec, o-st. w. assim. consonants & short vowel «worm, mite, maggot, moth, woodlouse»; Gk. sḗs, gs seós «mite»' — but the reconstruction is Mann's alone. Pokorny has no *ḱies- (the nearest entries, knid- «Laus, Ei der Laus» p.608 and the words for Milbe/Motte in POK_03, are unrelated), Walde-Pokorny has none, and Watkins/AHD has none. Modern scholarship treats every one of the three words as Semitic or as an areal insect-name: Wiktionary states flatly that Greek σής is 'a Semitic loanword, found as Aramaic סָסָא (sāsā), Hebrew סָס (sās), Akkadian sāsum, Arabic سوس (sūs)'; the Armenian word 'is often considered a Semitic borrowing, even though Semitic s is incompatible with Armenian ցʻ' (Ačaṙean tried to save it with an emphatic Akkadian ṣāṣu), with Udi c̣ec̣ and Proto-Georgian-Zan *c₁ic₁- pointing to a Caucasian areal word or to 'independent expressive formations for insects'; and Dehkhoda calls Persian ساس عربی فصیح, i.e. classical Arabic. Two further points tell against the root: it is glossed by an irregular, unetymologisable declension in Greek (σής, gen. σεός), and Persian shows no Middle Persian or Avestan antecedent at all.\",\n  \"note_fa\": \"این نمودار مدخل مان (IEC ص ۶۲۲) را درست بازتاب می‌دهد — مان می‌نویسد: «Kies «mite, tick, vermin». فارسی sās «bug, louse»؛ آسی sasḱ؛ ارمنی cec؛ یونانی sḗs، اضافی seós «mite»» — اما این بازسازی تنها از آنِ خود مان است. پوکورنی چنین ریشه‌ای ندارد، والده–پوکورنی ندارد و واتکینز نیز ندارد. پژوهش امروزی هر سه واژه را سامی یا واژه‌ای منطقه‌ای می‌داند: ویکی‌واژه σής یونانی را صریحاً «وام‌واژه‌ای سامی» می‌شمارد و آن را با آرامی sāsā، عبری sās، اکدی sāsum و عربی سوس می‌سنجد؛ دربارهٔ ցեց ارمنی می‌گوید «غالباً وام‌گیری از سامی دانسته می‌شود، هرچند s سامی با ց ارمنی سازگار نیست» (آچاریان کوشید با صورت مؤکد اکدی ṣāṣu این ناسازگاری را حل کند) و صورت‌های اودی c̣ec̣ و پیش‌گرجی-زانی *c₁ic₁- را نیز یاد می‌کند که به واژه‌ای قفقازی یا به «ساخت‌های تقلیدیِ مستقل برای نام حشرات» راه می‌برد؛ و دهخدا «ساس» فارسی را «عربی فصیح» می‌خواند. افزون بر این، صرف بی‌قاعدهٔ یونانی (σής با اضافی σεός) نشانهٔ واژه‌ای بیگانه است و در ایرانی نیز هیچ صورت فارسی میانه یا اوستایی برای این واژه ثبت نشده است. پژوهش امروزی ادعای این ریشه را رد می‌کند و به جای آن وام‌واژه‌ای سامی می‌داند.\",\n  \"sources\": [W_SES, W_SUS, W_CEC, W_SAS],\n  \"ref_check\": [\n    {\"ref\": \"IEC:622\", \"status\": \"supports\",\n     \"note\": \"Mann, IEC p.622 (IEC.txt line 8843, leaf 352; the printed numeral '623' follows a few entries later on the same leaf): 'Kies «mite, tick, vermin». (Variant: Kis-) Per. sās «bug, louse»; Oss. sasḱ «liver-fluke» beside saska «midge» and cist -tä «louse»; Arm. cec, o-st. w. assim. consonants & short vowel «worm, mite, maggot, moth, woodlouse»; Gk. sḗs, gs seós «mite»'. Nourai's root name, gloss and all three nodes come from this single entry.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW, searched POK_01/02/03 for the root and for 'Milbe'/'Motte'\", \"stance\": \"silent\",\n     \"note\": \"No *ḱies-/*ḱis- entry exists. p.608 has knid-, ḱnid-, sknid- «Laus, Ei der Laus, Nisse»; the Milbe/Motte words found (ἄκαρι under (s)ker-, russ. korь, lat. tinea under tā-) have nothing to do with sās/σής.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, root list\", \"stance\": \"silent\",\n     \"note\": \"No root of this shape; between kiwi- and knid- Watkins has nothing for 'mite, bug'.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"σής (Ancient Greek)\", \"stance\": \"contradicts\",\n     \"note\": \"'A Semitic loanword, found as Aramaic סָסָא / ܣܳܣܳܐ (sāsā, «moth»), Hebrew סָס (sās, «moth»), Akkadian sāsum («moth»), Arabic سوس (sūs, «moth-worm»).'\"},\n    {\"src\": \"Wiktionary\", \"where\": \"سوس (Arabic)\", \"stance\": \"contradicts\",\n     \"note\": \"'typically declared as inherited from Proto-Semitic *sūs- («moth; insect especially one that bites or chews up materials»)', from Proto-Afroasiatic *suʔw-, with Akkadian sāsum, Hebrew סָס, Aramaic ססא, Syriac ܣܣܐ and Ethiosemitic cognates.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Armenian\", \"words\": \"čeč\", \"verdict\": \"disputed\",\n    \"derivation\": \"The word intended is Old Armenian ցեց (cʻecʻ) 'moth', also 'a skin disease' — Mann prints it 'cec' and describes it as an o-stem 'with assimilated consonants and short vowel'. Nourai's transliteration čeč is misleading: the initial and final are ց cʻ (an aspirated affricate ts), not č (ճ/չ). On the substance, Wiktionary's Armenian entry says the origin is uncertain: 'The Armenian is often considered a Semitic borrowing, even though Semitic s is incompatible with Armenian ցʻ (cʻ)', an objection Ačaṙean tried to remove by positing an emphatic Akkadian ṣāṣu whose existence modern references doubt; the entry also cites Udi c̣ec̣ and Proto-Georgian-Zan *c₁ic₁-, and concludes that these may be 'independent expressive formations for insects in various languages'. No modern source derives it from an Indo-European *ḱies-, and Armenian *ḱ- would in any case give s-, not cʻ-, so the sound-correspondence Nourai's chart implies (Arm. cʻ : Gk. s : Pers. s from one *ḱ) does not hold.\",\n    \"derivation_fa\": \"واژهٔ موردنظر ցեց (cʻecʻ) در ارمنی کهن به معنی «بید، پروانهٔ جامه‌خوار» و نیز نام نوعی بیماری پوستی است؛ مان آن را «cec» می‌نویسد و ستاکی o-دار «با همگونی همخوان‌ها و مصوت کوتاه» می‌خواند. آوانگاری نورایی، čeč، گمراه‌کننده است: آغاز و پایان واژه ց (cʻ، سایشی‌انسدادیِ دمیده) است نه č. از نظر محتوا، ویکی‌واژه خاستگاه آن را نامعلوم می‌داند: «صورت ارمنی غالباً وام‌گیری از سامی دانسته می‌شود، هرچند s سامی با ց ارمنی سازگار نیست»؛ آچاریان برای رفع این ناسازگاری صورت مؤکد اکدی ṣāṣu را فرض کرد که وجودش امروزه مورد تردید است. همان مدخل صورت اودی c̣ec̣ و پیش‌گرجی-زانی *c₁ic₁- را نیز می‌آورد و نتیجه می‌گیرد که شاید با «ساخت‌های تقلیدیِ مستقل» روبه‌رو باشیم. هیچ منبع امروزی آن را از *ḱies- هندواروپایی نمی‌گیرد و در هر حال *ḱ هندواروپایی در ارمنی s می‌دهد نه cʻ. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n    \"sources\": [W_CEC],\n    \"ref_check\": [\n      {\"ref\": \"IEC:622\", \"status\": \"supports\",\n       \"note\": \"Mann p.622: 'Arm. cec, o-st. w. assim. consonants & short vowel «worm, mite, maggot, moth, woodlouse»' — Nourai's node, except that Mann writes cec, not čeč, and glosses it more broadly.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"ցեց (Old Armenian/Armenian)\", \"stance\": \"contradicts\",\n       \"note\": \"'The Armenian is often considered a Semitic borrowing, even though Semitic s is incompatible with Armenian ցʻ (cʻ)'; compares Udi c̣ec̣, Proto-Georgian-Zan *c₁ic₁-, Akkadian sāsum, Syriac sāsā, Greek σής; alternative: 'independent expressive formations for insects in various languages'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW\", \"stance\": \"silent\",\n       \"note\": \"Armenian cʻecʻ does not appear anywhere in Pokorny; there is no root under which it is filed.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Greek\", \"words\": \"sěs, seos\", \"verdict\": \"disputed\",\n    \"derivation\": \"Attic σής 'clothes-moth', gen. σεός (later re-formed σητός, plural σῆτες beside older σέες) — Mann's two forms are exactly the nominative and the old genitive, and Nourai copies them correctly. But the word is not Indo-European. Its very declension is anomalous (a monosyllabic nominative in -ής with a genitive in -εός that no Greek stem class explains), a classic sign of a foreign noun, and Wiktionary states outright: 'A Semitic loanword, found as Aramaic סָסָא (sāsā, «moth»), Hebrew סָס (sās, «moth»), Akkadian sāsum («moth»), Arabic سوس (sūs, «moth-worm»)'. The Semitic word itself is inherited within Semitic (Proto-Semitic *sūs-, Proto-Afroasiatic *suʔw-), so the loan must have run Semitic → Greek, not PIE → Greek. Mann's *ḱies- would in any case predict Greek *κι-, not σ-, since PIE *ḱ gives Greek κ (centum), which is a decisive objection Mann never addresses.\",\n    \"derivation_fa\": \"σής در یونانی آتیک «بیدِ جامه» است، با اضافی σεός (که بعدها به σητός بازساخته شد و جمع آن σῆτες در برابر σέες کهن‌تر). دو صورتی که مان و به تبع او نورایی آورده‌اند دقیقاً همان فاعلی و اضافی کهن‌اند. اما این واژه هندواروپایی نیست: صرف آن بی‌قاعده است (فاعلی تک‌هجایی با ‎-ής‎ و اضافی ‎-εός‎ که در هیچ ستاک یونانی توضیح‌پذیر نیست) و این خود نشانهٔ روشن واژه‌ای بیگانه است. ویکی‌واژه صریح می‌گوید: «وام‌واژه‌ای سامی است که در آرامی sāsā، عبری sās، اکدی sāsum و عربی سوس دیده می‌شود». خودِ واژهٔ سامی درون سامی ارثی است (سامی آغازین *sūs-)، پس جهت وام‌گیری سامی ← یونانی بوده است نه هندواروپایی ← یونانی. افزون بر این، *ḱ در بازسازی مان باید در یونانی κ بدهد نه σ، و این ایرادی است که مان به آن نپرداخته است. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n    \"sources\": [W_SES, W_SUS],\n    \"ref_check\": [\n      {\"ref\": \"IEC:622\", \"status\": \"supports\",\n       \"note\": \"Mann p.622: 'Gk. sḗs, gs seós «mite»' — verbatim the chart's 'sěs, seos : mite'.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"σής (Ancient Greek)\", \"stance\": \"contradicts\",\n       \"note\": \"'A Semitic loanword, found as Aramaic סָסָא / ܣܳܣܳܐ (sāsā), Hebrew סָס (sās), Akkadian sāsum, Arabic سوس (sūs, «moth-worm»)'; declension given as gen. σεός (Attic) / σητός (later).\"},\n      {\"src\": \"Wiktionary\", \"where\": \"سوس (Arabic)\", \"stance\": \"contradicts\",\n       \"note\": \"Proto-Semitic *sūs- 'moth; insect that bites or chews up materials', from Proto-Afroasiatic *suʔw-, with Akkadian, Hebrew, Aramaic, Syriac and Ethiosemitic cognates — an inherited Semitic word, hence the source rather than the borrower.\"},\n      {\"src\": \"POK\", \"where\": \"IEW\", \"stance\": \"silent\", \"note\": \"σής is not entered anywhere in Pokorny.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Persian\", \"words\": \"sâs «ساس ۲»\", \"verdict\": \"disputed\",\n    \"derivation\": \"New Persian ساس sās is the bedbug, Cimex lectularius. Borhan-e Qateʿ (Moʿin's ed. p.1073) has it: «ساس - بر وزن پاس ... و نام جانوری است سیاه از مقولهٔ کیک و شپش لیکن بزرگ‌تر از آن‌ها باشد و در هندوستان بسیار ...», and Moʿin's Farhang defines it as a hemipteran that hides in the seams of mattresses and bites at night — Nourai's gloss 'louse, bug' and his homograph number ۲ are right. The etymology is not. Dehkhoda's entry calls the word عربی فصیح, 'sound classical Arabic', i.e. it is the Semitic insect-name (Arabic سوس sūs / ساس, Aramaic sāsā, Akkadian sāsum) taken into Persian in the Islamic period; there is no Middle Persian or Avestan antecedent — MacKenzie, Nyberg, Horn and Hübschmann all have nothing — which is exactly what an Arabic-era loan looks like. Mann's Ossetic sasḱ 'liver-fluke', saska 'midge' may belong to the same Wanderwort; they do not establish an inherited Iranian word, and an inherited reflex of *ḱies- would in any case have to show the Iranian outcome of *ḱ (s-) plus a reflex of the *-es- stem, which sās does not.\",\n    \"derivation_fa\": \"«ساس» در فارسی نو نام حشرهٔ خون‌خوار Cimex lectularius است. برهان قاطع (چاپ معین، ص ۱۰۷۳) می‌آورد: «ساس - بر وزن پاس ... و نام جانوری است سیاه از مقولهٔ کیک و شپش لیکن بزرگ‌تر از آن‌ها باشد و در هندوستان بسیار ...»؛ فرهنگ معین نیز آن را حشره‌ای از راستهٔ نیم‌بالان می‌داند که در درز تشک و لحاف پنهان می‌شود و شب‌ها نیش می‌زند. پس معنایی که نورایی داده و شمارهٔ همنگاشت «۲» درست است، ولی ریشه‌شناسی نه. دهخدا این واژه را «عربی فصیح» می‌خواند؛ یعنی همان نام حشرهٔ سامی (عربی سوس/ساس، آرامی sāsā، اکدی sāsum) که در دورهٔ اسلامی به فارسی وارد شده است. هیچ صورت فارسی میانه یا اوستایی برای آن ثبت نشده — مکنزی، نیبرگ، هرن و هوبشمان همه خاموش‌اند — و این دقیقاً نشانهٔ وام‌واژه‌ای عربی است. صورت‌های آسی sasḱ و saska که مان می‌آورد نیز شاید از همین واژهٔ سرگردان باشند و وجود واژه‌ای ارثی در ایرانی را ثابت نمی‌کنند. پژوهش امروزی ادعای نورایی را رد می‌کند و آن را وام‌واژه‌ای سامی می‌داند.\",\n    \"sources\": [W_SAS, W_SUS],\n    \"ref_check\": [\n      {\"ref\": \"IEC:622\", \"status\": \"supports\",\n       \"note\": \"Mann p.622: 'Per. sās «bug, louse»' — the first word he cites under Kies-, and the source of Nourai's gloss.\"},\n      {\"ref\": \"MON:1795\", \"status\": \"partial\",\n       \"note\": \"Only the 2-volume Adena abridgement of Moʿin is online, so the page cannot be checked; its entry (MON_part1.txt line 73939) reads «ساس: ... (اِ.) (جاند.) حشره‌ای است از راستهٔ نیم‌بالان که رنگ قرمز مایل به قهوه‌یی دارد ... شب‌ها خارج می‌گردد و به انسان نیش می‌زند و خون وی را می‌مکد». The meaning matches; the abridgement carries no origin tag, so it neither supports nor contradicts the Indo-European claim.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ, Moʿin's ed., p.1073 (BQT_v2_pages.txt leaf 533)\", \"stance\": \"partial\",\n       \"note\": \"«ساس - بر وزن پاس ... و به زبان هندی مادرزن را گویند - و نام جانوری است سیاه از مقولهٔ کیک و شپش لیکن بزرگ‌تر از آن‌ها باشد و در هندوستان بسیار ...» — the insect is there, but Moʿin attaches no etymological footnote to it, i.e. he claims no Iranian etymon.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. ساس\", \"stance\": \"partial\", \"note\": \"definition only, no origin tag in the available abridgement.\"},\n      {\"src\": \"Dehkhoda\", \"where\": \"Loghatname s.v. ساس (via abadis.ir)\", \"stance\": \"contradicts\",\n       \"note\": \"Dehkhoda's entry describes the insect and states that the word is عربی فصیح (sound classical Arabic), tracing it from a general term for small insects to the modern bedbug sense — i.e. a Semitic, not an Indo-European, word.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"no entry for sās; a search for 'Wanze' returns nothing.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary\", \"stance\": \"silent\", \"note\": \"no Middle Persian sās; the only sās- entries are sāstār 'tyrant' and its derivatives.\"}\n    ]\n   }\n  ]\n },\n\n # ------------------------------------------------------------------ entry 4\n {\n  \"entry\": 4,\n  \"root\": \"Kiph\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"PIE (?) *ḱiph- 'thin flexible twig or piece of root' — Pokorny 598, printed with his own question mark\",\n  \"note\": \"The root box is a faithful copy of Pokorny p.598: 'ḱiph- «dünner biegsamer Zweig oder Wurzelteil»?' — the language label and the gloss are exactly right, question mark and all. But the root is one of Pokorny's weakest: it rests on a single Sanskrit word (śiphā) plus one Messenian gloss (κίφος 'στέφανος'), and Walde-Pokorny I 452, from whom Pokorny took it, already warn that the Baltic comparanda (Latvian sipsna, Lithuanian šipulys) 'scheinen diese besser zu skei-p- «spalten» ... zu passen', and that Hirt, Uhlenbeck and Charpentier connected Sanskrit śiphā with quite different words (śepa- 'penis', śipra- 'moustache'). Watkins/AHD does not list the root at all and Mann has no entry for it either. Structurally the reconstruction is suspect because *-ph- is not a Proto-Indo-European phoneme, so at best this is an areal or expressive item, not an inherited root. Verdict 'plausible': Nourai reports his source correctly, but the source itself is tentative.\",\n  \"note_fa\": \"جعبهٔ ریشه رونوشت درست پوکورنی ص ۵۹۸ است: «ḱiph- «شاخهٔ نازک و انعطاف‌پذیر یا پارهٔ ریشه»؟» — برچسب زبانی و معنا، حتی علامت پرسش، درست‌اند. ولی این یکی از سست‌ترین ریشه‌های پوکورنی است: تنها بر یک واژهٔ سنسکریت (śiphā) و یک واژهٔ مسنیایی (κίφος «تاج گل») استوار است، و والده–پوکورنی (جلد ۱ ص ۴۵۲) که منبع پوکورنی است هشدار می‌دهد که صورت‌های بالتیک (لتونیایی sipsna، لیتوانیایی šipulys) «بهتر است به ریشهٔ skei-p- «شکافتن» نسبت داده شوند»، و یادآور می‌شود که هیرت و اولنبک و شارپانتیه śiphā را به واژه‌های دیگری (śepa-، śipra-) پیوند داده‌اند. واتکینز اصلاً چنین ریشه‌ای ندارد و مان نیز ندارد. از نظر ساختاری هم ‎*-ph-‎ واجی هندواروپایی نیست؛ پس این واژه در بهترین حالت واژه‌ای منطقه‌ای یا تقلیدی است نه ریشه‌ای ارثی. بنابراین گزارش نورایی از منبعش درست است ولی خودِ منبع محتاطانه سخن می‌گوید: با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_SIPH],\n  \"ref_check\": [\n    {\"ref\": \"POK:598\", \"status\": \"supports\",\n     \"note\": \"Pokorny IEW p.598 (POK_02.txt, immediately after the page marker '598' at line 4018): 'ḱiph- «dünner biegsamer Zweig oder Wurzelteil»? Ai. śiphā «dünne Wurzel, Rute»; gr. messenisch κίφος n. «στέφανος»; allenfalls auch lett. sipsna «starke Rute», lit. šipulys «Holzspan, Holzscheit». WP. I 452.' Root name, language and gloss are Nourai's exactly.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.452 (WLD_Bd1_pages.txt leaf 461)\", \"stance\": \"partial\",\n     \"note\": \"'kiph- «dünner biegsamer Zweig oder Wurzelteil». Ai. çiphā «dünne Wurzel, Rute»; gr. messenisch κίφος n. «στέφανος» (wenn eig. «flechtbarer, geflochtener Zweig»; Petersson Gl. 4, 298); allenfalls auch (Endzelin) lett. sipsna ..., lit. šipulys ..., doch scheinen diese besser zu skei-p- «spalten» ... zu passen.' Same root, but with the caveat Nourai does not report.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, root list between kiwi- and knid-\", \"stance\": \"silent\",\n     \"note\": \"No *ḱiph- root; Watkins never adopted it.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IEC, searched for a Kiph- headword\", \"stance\": \"silent\",\n     \"note\": \"Mann has no *ḱiph- entry (his nearest is Kip-/skoip- 'slice, split', IEC.txt line 15534, i.e. the *skei-p- family Walde-Pokorny preferred).\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"šiphâ, čiphâ\", \"verdict\": \"transcription_suspect\",\n    \"derivation\": \"There is only ONE Sanskrit word here, śiphā (शिफा) f., and its meanings are exactly Nourai's gloss: Monier-Williams (and Wiktionary after him) 'a fibrous or flexible root (used for making whips); a lash or stroke with a whip or rod; a branch; a river; a tuft of hair on the crown of the head' — hence 'twig, hair'. The second 'word', čiphâ, is a ghost. Pokorny p.598 prints the word in the modern transcription, 'Ai. śiphā'; Walde-Pokorny I 452, Pokorny's own source and Nourai's second citation, prints the SAME word in the older German-school transcription, 'ai. çiphā', where ç is simply ś. Nourai, working from both pages, took the two spellings for two words and rendered the cedilla ç with a háček as č. The printed page (pdf 267) reads 'šiphâ, čiphâ : twig, hair', so the JSON is faithful and the error is the book's, not the extraction's. As for the arrow itself, the derivation of śiphā from *ḱiph- is Pokorny's, and it is the only leg the root stands on; Sanskrit ś is the regular satem outcome of *ḱ, so the correspondence works, but nothing corroborates the reconstruction outside this one word.\",\n    \"derivation_fa\": \"در اینجا تنها یک واژهٔ سنسکریت وجود دارد: शिफा (śiphā) که معنای آن دقیقاً همان است که نورایی داده — مونیر ویلیامز و به پیروی او ویکی‌واژه می‌آورند: «ریشهٔ لیفی یا انعطاف‌پذیر (که از آن تازیانه می‌سازند)؛ ضربهٔ تازیانه یا ترکه؛ شاخه؛ رود؛ دسته‌ای مو بر فرق سر»، یعنی همان «شاخه، مو». اما واژهٔ دوم، čiphâ، واژه‌ای موهوم است: پوکورنی در ص ۵۹۸ همین واژه را با آوانگاری امروزی «Ai. śiphā» نوشته و والده–پوکورنی (جلد ۱ ص ۴۵۲) — که منبع پوکورنی و ارجاع دوم نورایی است — همان واژه را با آوانگاری کهن آلمانی «ai. çiphā» آورده است که در آن ç همان ś است. نورایی این دو املا را دو واژه پنداشته و ç را با علامت هاچک به č بدل کرده است. صفحهٔ چاپی (صفحهٔ ۲۶۷ پی‌دی‌اف) «šiphâ, čiphâ : twig, hair» را نشان می‌دهد، پس استخراج داده وفادار است و خطا از خودِ کتاب است (خطای چاپی/خوانشِ نویسنده). دربارهٔ خودِ پیکان، اشتقاق śiphā از *ḱiph- از آنِ پوکورنی است و تنها پایهٔ این ریشه؛ ś سنسکریت بازتاب قاعده‌مند *ḱ در زبان‌های ساتم است، پس تناظر آوایی درست کار می‌کند، ولی جز همین یک واژه شاهدی برای بازسازی در دست نیست.\",\n    \"error_in\": \"book\",\n    \"book_prints\": \"šiphâ, čiphâ : twig, hair\",\n    \"correct_form\": \"śiphā (older transcription çiphā) — one Sanskrit word, not two\",\n    \"sources\": [W_SIPH],\n    \"ref_check\": [\n      {\"ref\": \"POK:598\", \"status\": \"supports\",\n       \"note\": \"Pokorny p.598: 'Ai. śiphā «dünne Wurzel, Rute»' — ONE word, in the modern transcription.\"},\n      {\"ref\": \"WLD1:452\", \"status\": \"supports\",\n       \"note\": \"Walde-Pokorny Bd. I p.452: 'Ai. çiphā «dünne Wurzel, Rute»' (the OCR of the scan reads 'gipha' for çiphā) — the SAME word, in the older transcription with ç for ś. Reading the two spellings as two words is what produced Nourai's 'čiphâ'.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"शिफा (Sanskrit)\", \"stance\": \"supports\",\n       \"note\": \"'a fibrous or flexible root (used for making whips); a lash or stroke with a whip or rod; a branch; a river; a tuft of hair on the crown of the head' — covers both halves of Nourai's gloss 'twig, hair'; no second form ciphā is recorded, and the etymology section is marked 'missing or incomplete'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.452\", \"stance\": \"partial\",\n       \"note\": \"adds Petersson's semantic bridge for the Greek word and the alternative connections of śiphā proposed by Hirt/Uhlenbeck (śepa- 'penis') and Charpentier (śipra- 'moustache', ciprā 'head-hair').\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.598\", \"stance\": \"supports\", \"note\": \"as quoted; the Sanskrit word is the head of the entry.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Persian\", \"words\": \"šafš «شَفَش ( شَفشه ، شَفشَف )»; šafšâhang «شفشاهنگ ، شفتاهنج»\", \"verdict\": \"plausible\",\n    \"derivation\": \"Borhan-e Qateʿ p.1272 (vol. 3 of Moʿin's edition) — the page Nourai cites, and the page was read from the scan — carries FOUR separate headwords that the chart merges into one: (a) شَفْش 'a stick with which cotton-carders beat and gather cotton; also the branch of a tree', to which Moʿin's footnote 5 attaches not Sanskrit but Tabari šīš 'twig' («طبری shîsh (ترکه) «واژه‌نامه ۵۰۰»»); (b) شُفْشه 'an ingot (شوشه) of gold or silver; a very thin, straight, smooth branch; a lock of hair fallen over the beloved's face', footnote 10 merely cross-referring to شوشه/شیوشه; (c) شَفْشَف 'the branch of a tree; also the root of a tree' — and it is ONLY this headword that carries the Sanskrit note, Moʿin's footnote 9: «سانسکریت shipha و shiphâ (بیخ نهال لیفی یا شاخهٔ قابل انحنا) [مونیر ویلیامز] ۱۰۷۲:۹۱»; (d) شفشاهنج / شفشاهنگ 'a pierced iron plate through which goldsmiths draw gold and silver into thin wire', which Moʿin's footnote 6 analyses as شفشه (ingot) + آهنج/آهنگ 'draw', quoting Asadi Tusi's Loghat-e Fors p.73 «شفشاهنج: شکنجه بود». So the citation is genuine but displaced: the Sanskrit etymology belongs to šafšaf, the 'wire' half of Nourai's gloss comes from a compound whose first element means 'ingot', not 'twig', and Moʿin derives šafš itself from a Caspian dialect word. Phonetically a direct inheritance is impossible in any case — PIE *ḱ gives Iranian s-, not š-, and *-ph- would not yield -fš — and the reduplicated shape šafš / šafšaf / šafša looks like a Persian expressive formation; if Moʿin's Sanskrit link is right, it can only be a Wanderwort or an Indic loan, not a sister of śiphā inherited from *ḱiph-.\",\n    \"derivation_fa\": \"برهان قاطع در ص ۱۲۷۲ (جلد سوم چاپ معین) — همان صفحه‌ای که نورایی ارجاع داده و از روی اسکن خوانده شد — چهار سرواژهٔ جداگانه دارد که نمودار همه را یکی کرده است: (الف) «شَفْش» یعنی «چوبی که ندافان پنبه را بدان زنند و گردآوری و جمع نمایند - و شاخ درخت را نیز گفته‌اند»، که حاشیهٔ ۵ معین برای آن نه سنسکریت بلکه «طبری shîsh (ترکه) «واژه‌نامه ۵۰۰»» را می‌آورد؛ (ب) «شُفْشه» یعنی «شوشهٔ طلا و نقره ... و شاخ درخت بسیار نازک و راست و هموار ... و موی چندی از کاکل و زلف معشوق»، که حاشیهٔ ۱۰ آن تنها ارجاع به «شوشه» و «شیوشه» است؛ (ج) «شَفْشَف» یعنی «شاخ درخت که کجواج باشد - و بیخ درخت را نیز گویند»، و تنها همین سرواژه است که حاشیهٔ ۹ معین را دارد: «سانسکریت shipha و shiphâ (بیخ نهال لیفی یا شاخهٔ قابل انحنا) ۱۰۷۲:۹۱»؛ (د) «شفشاهنج / شفشاهنگ» یعنی «آهن سوراخ‌دار استادان زرکش ... تا سیم و زر را از آن بکشند تا باریک شود»، که معین در حاشیهٔ ۶ آن را «شفشه + آهنج (آهنگ)» تحلیل می‌کند و از لغت فرس اسدی (ص ۷۳) نقل می‌آورد: «شفشاهنج: شکنجه بود». پس ارجاع اصیل است ولی جابه‌جا شده: ریشه‌شناسی سنسکریت از آنِ «شفشف» است، معنای «سیم» از ترکیبی می‌آید که جزء نخستش «شمش» است نه «شاخه»، و خودِ «شفش» را معین از گویش طبری می‌گیرد. از نظر آوایی نیز وراثت مستقیم ناممکن است: *ḱ هندواروپایی در ایرانی s می‌دهد نه š، و ‎*-ph-‎ به ‎-fš‎ نمی‌انجامد؛ و ساخت مضاعف «شفش/شفشف/شفشه» به ساخت‌های تقلیدی فارسی می‌ماند. اگر پیوند سنسکریتی معین درست باشد، تنها می‌تواند وام‌واژه یا واژه‌ای سرگردان باشد نه هم‌ریشه‌ای ارثی. با احتیاط پذیرفتنی است.\",\n    \"sources\": [W_SIPH],\n    \"ref_check\": [\n      {\"ref\": \"BQT:1272\", \"status\": \"partial\",\n       \"note\": \"Read from the scan with tools/ref_page.py BQT:1272 --image (vol.3 pdf p.63; PNG cached at data/verification/sources/refs/ocr/BQT/1272.png) and by reading the image directly. The page has شفش, شفشاهنج, شفشاهنگ, شفشف, شفشه. Moʿin's footnote 9, attached to شَفْشَف, reads «سانسکریت shipha و shiphâ (بیخ نهال لیفی یا قابل انحنا، شاخه) «ویلیامز ۱۰۷۲:۹۱»» — the Sanskrit etymology Nourai wants, but for شفشف, not for شفش; footnote 5 on شفش reads «طبری shîsh (ترکه) «واژه‌نامه ۵۰۰»», and footnote 6 on شفشاهنج reads «شفشاهنگ (ه.م.) از شفشه + آهنج (آهنگ). اسدی در لغت فرس (ص۷۳) گوید: «شفشاهنج، شکنجه بود»».\"},\n      {\"ref\": \"MON:2052\", \"status\": \"partial\",\n       \"note\": \"The six-volume Moʿin is not online; the 2-volume Adena abridgement (MON_part1.txt lines 85530-85545) has «شفش: ... (اِ.) نی و چوبی باشد که ندافان پنبه را بدان زنند و گردآوری کنند» and a second «شفش: [قس. شفشه، شوشه] (اِ.) شاخ درخت. شوشه» plus «شفشه: شوشهٔ طلا و نقره ...». The words and senses match Nourai's node, but the abridgement gives only the internal cross-reference «قس. شفشه، شوشه» and no Sanskrit etymon; the page number cannot be verified.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors p.73 (FRS.txt line 3620; index entry 'شفشاهنج ۷۳' at line 21669)\", \"stance\": \"supports\",\n       \"note\": \"«شفشا هنج: شکنجه بود» — the oldest attestation of the compound, and the source Moʿin quotes in his footnote.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. شفش / شفشه\", \"stance\": \"partial\",\n       \"note\": \"gives the same senses (carder's stick, branch, ingot) and only an internal comparison «قس. شفشه، شوشه».\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"no entry for šafš or šafšāhang.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary\", \"stance\": \"silent\", \"note\": \"no Middle Persian antecedent recorded.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Greek\", \"words\": \"xiphos\", \"verdict\": \"transcription_suspect\",\n    \"derivation\": \"Pokorny p.598, the page cited in this very box, does NOT have ξίφος. What he prints under ḱiph- is 'gr. messenisch κίφος n. «στέφανος»' — a Messenian gloss with initial kappa meaning 'wreath, garland' (Walde-Pokorny I 452 add Petersson's justification, 'wenn eig. «flechtbarer, geflochtener Zweig»', i.e. 'if it originally meant a plaitable, plaited twig'). Nourai has turned κίφος into 'xiphos' and given it the root's own gloss, 'branch, rod', which is the meaning of neither κίφος ('wreath') nor ξίφος ('sword'). The printed page of the dictionary (pdf 267, image saved as data/verification/sources/refs/ocr/BOOK/267.png) reads 'xiphos : branch, rod', so the extraction is faithful and the fault lies in the book. The confusion matters because the next two boxes hang on it: ξίφος 'sword' cannot come from *ḱiph- at all — it is already Mycenaean (dual qi-si-pe-e, Pylos Ta 716), is classed as Pre-Greek by Beekes, and is 'probably ... related to and perhaps borrowed from Egyptian zft «sword, knife»' (Wiktionary), while Klein s.v. xipho- calls it 'of uncertain origin. It is perh. a loan word fr. Aram. saypha (whence also Heb. sayif, Arab. sayf), fr. Egypt. sefet «sword», which is a derivative of the verb sft «to slaughter»'.\",\n    \"derivation_fa\": \"صفحهٔ ۵۹۸ پوکورنی، همان که در این جعبه به آن ارجاع داده شده، اصلاً ξίφος ندارد. آنچه پوکورنی زیر ریشهٔ ḱiph- چاپ کرده این است: «gr. messenisch κίφος n. «στέφανος»» — واژه‌ای مسنیایی با کاف آغازین به معنی «تاج گل، حلقهٔ گل» (والده–پوکورنی جلد ۱ ص ۴۵۲ توجیه پترسون را نیز می‌افزاید: «اگر در اصل به معنی شاخهٔ بافتنی/بافته باشد»). نورایی κίφος را به «xiphos» بدل کرده و معنای خودِ ریشه، یعنی «شاخه، ترکه»، را به آن داده است؛ حال آنکه نه κίφος («تاج گل») و نه ξίφος («شمشیر») چنین معنایی ندارند. صفحهٔ چاپی کتاب (صفحهٔ ۲۶۷ پی‌دی‌اف، تصویر ذخیره‌شده در data/verification/sources/refs/ocr/BOOK/267.png) «xiphos : branch, rod» را نشان می‌دهد؛ پس خطای خوانش اسکن نیست، خطای خودِ کتاب است. این خلط مهم است چون دو جعبهٔ بعدی بر آن استوارند: ξίφος «شمشیر» به هیچ روی از *ḱiph- نمی‌آید — این واژه در میسنی نیز هست (صورت مثنای qi-si-pe-e در لوح Ta 716 از پیلوس)، بیکس آن را پیش‌یونانی می‌شمارد و ویکی‌واژه می‌گوید «احتمالاً با مصری zft «شمشیر، کارد» مرتبط و شاید از آن وام گرفته شده است»، و کلاین ذیل xipho- می‌نویسد: «خاستگاهش نامعلوم است. شاید وام‌واژه‌ای از آرامی saypha (که عبری sayif و عربی sayf نیز از آن‌اند)، از مصری sefet «شمشیر» که خود مشتق فعل sft «سر بریدن» است».\",\n    \"error_in\": \"book\",\n    \"book_prints\": \"xiphos : branch, rod\",\n    \"correct_form\": \"kiphos (Messenian κίφος n.) 'στέφανος, wreath' — the Greek word Pokorny actually gives under this root\",\n    \"sources\": [W_XIPH],\n    \"ref_check\": [\n      {\"ref\": \"POK:598\", \"status\": \"contradicts\",\n       \"note\": \"Pokorny p.598 s.v. ḱiph-: 'gr. messenisch κίφος n. «στέφανος»' — a kappa-initial word glossed 'wreath', not ξίφος 'sword' and not 'branch, rod'.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.452\", \"stance\": \"contradicts\",\n       \"note\": \"'gr. messenisch κίφος n. «στέφανος» (wenn eig. «flechtbarer, geflochtener Zweig»; Petersson Gl. 4, 298)' — the same kappa-form, with the semantic bridge spelled out.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1971 (one-vol.) s.v. xipho- / xiph- (KLN_1971.txt lines 269105-269130)\", \"stance\": \"contradicts\",\n       \"note\": \"'xipho-, before a vowel xiph-, combining form meaning «sword». — Gk. ξιφο-, ξιφ-, fr. ξίφος, «sword», of uncertain origin. It is perh. a loan word fr. Aram. saypha (whence also Heb. sayif, Arab. sayf), fr. Egypt. sefet, «sword», which is a derivative of the verb sft, «to slaughter». See H. Lewy, Die semitischen Fremdwörter im Griechischen, pp. 176 ff. ...' — Greek ξίφος is explicitly NOT Indo-European for Klein.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"ξίφος (Ancient Greek)\", \"stance\": \"contradicts\",\n       \"note\": \"'Already in Late Mycenaean Greek (Ta-716 from Pylos), attested in the dual 𐀥𐀯𐀟𐀁 (qi-si-pe-e, «two swords») ... Probably of Pre-Greek origin, related to and perhaps borrowed from Egyptian zft («sword, knife»)'; alternatively Greek and the Semitic words go back to a common source. Beekes (2010) cited.\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"Arabic\", \"words\": \"sayf; s.y.f\", \"verdict\": \"disputed\",\n    \"derivation\": \"Arabic سَيْف sayf 'sword' (pl. سُيُوف suyūf) with the denominal root س ي ف, from which the verb sāfa / yasīfu 'to strike with a sword' is formed — Nourai's second entry 's.y.f'. The arrow Greek → Arabic is exactly what his cited source says: al-ʿUnaysī (TAD) writes «سيف - ويوناني ξίφος وهو القاضب والقاطع والماضي», 'sayf — and (it is) Greek xiphos, and it is the cutter, the slicer, the sharp one'. Modern scholarship reverses or dissolves that arrow. Klein derives Greek ξίφος itself from Aramaic saypā 'sword', 'whence also Heb. sayif, Arab. sayf', ultimately from Egyptian sefet/zft 'sword' (a derivative of sft 'to slaughter'); Wiktionary's Arabic entry says sayf is 'Related to Ancient Greek ξίφος; either a loan, or from a common original source. The same word is probably preserved in Egyptian zft, Coptic ⲥⲏϥⲉ (sēfe)', citing Dümichen's Old Semitic saïf/sêf and Myres's Libyan or 'Sea Peoples' hypothesis, and compares Hebrew סַיִף sáyip̄ and Geʿez ሰይፍ säyf. Since Greek already has the word in Mycenaean (qi-si-pe-e, 13th c. BCE) while the Semitic form sits in a productive triliteral root with cognates across West Semitic and Ethiosemitic, a borrowing FROM Greek INTO Arabic is the least likely of the options on offer; and the chain's ultimate premise, that ξίφος descends from PIE *ḱiph-, is not held by anyone today.\",\n    \"derivation_fa\": \"«سَیف» در عربی «شمشیر» است (جمع: سیوف) با ریشهٔ سه‌حرفی اسم‌بنیاد س ی ف که فعل «سافَ/یَسیفُ» یعنی «به شمشیر زدن» از آن ساخته شده است — همان مدخل دوم نمودار. پیکان «یونانی ← عربی» دقیقاً همان است که منبع نورایی می‌گوید: طوبیا العنیسی در «تفسیر الألفاظ الدخیلة» می‌نویسد: «سيف - ويوناني ξίφος وهو القاضب والقاطع والماضي». اما پژوهش امروزی این پیکان را وارونه یا منحل می‌کند. کلاین خودِ ξίφος یونانی را از آرامی saypā «شمشیر» می‌گیرد — «که عبری sayif و عربی sayf نیز از آن‌اند» — و سرانجام از مصری sefet/zft «شمشیر» (مشتق فعل sft «سر بریدن»). ویکی‌واژه نیز می‌گوید: «با ξίφος یونانی مرتبط است؛ یا وام‌واژه است یا هر دو از یک خاستگاه مشترک‌اند. همین واژه احتمالاً در مصری zft و قبطی ⲥⲏϥⲉ حفظ شده است»، و عبری סַיִף و گعزی ሰይፍ را نیز می‌سنجد. از آنجا که یونانی این واژه را از دورهٔ میسنی (qi-si-pe-e، سدهٔ سیزدهم پیش از میلاد) دارد و صورت سامی در ریشه‌ای زایا با هم‌ریشه‌های سامی غربی و حبشی نشسته است، وام‌گیری از یونانی به عربی کم‌احتمال‌ترین گزینه است؛ و پیش‌فرض بنیادی این زنجیره، یعنی برآمدن ξίφος از *ḱiph- هندواروپایی، امروز هیچ طرفداری ندارد. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n    \"sources\": [W_SAYF, W_XIPH],\n    \"ref_check\": [\n      {\"ref\": \"TAD:39\", \"status\": \"supports\",\n       \"note\": \"al-ʿUnaysī, Tafsīr al-alfāẓ al-dākhila, TAD_pages.txt leaf 42 (printed page ≈ 37-39; the sīn entries end and the shīn entries begin on the next leaf): «سيف - ويوناني ξίφος وهو القاضب والقاطع والماضي». This is exactly Nourai's arrow, and it is his only authority for it.\"},\n      {\"ref\": \"TAD:78\", \"status\": \"not_found\",\n       \"note\": \"Leaves 82-83 of TAD_pages.txt (printed ≈ p.78) are the Latin-script appendix/index matter and the OCR there is unusable; no second treatment of سيف could be located. A grep of the whole file for سيف returns only leaf 42 (the sword) and leaves 34/75 (the homonym sayf 'seashore').\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. xipho-\", \"stance\": \"contradicts\",\n       \"note\": \"'Gk. ξίφος ... perh. a loan word fr. Aram. saypha (whence also Heb. sayif, Arab. sayf), fr. Egypt. sefet, «sword», which is a derivative of the verb sft, «to slaughter»' — the borrowing runs Egyptian → Aramaic → Greek/Arabic, i.e. the opposite of Nourai's arrow.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"سيف (Arabic)\", \"stance\": \"partial\",\n       \"note\": \"'Related to Ancient Greek ξίφος (xíphos); either a loan, or from a common original source. The same word is probably preserved in Egyptian zft, Coptic ⲥⲏϥⲉ (sēfe). Dümichen (1867) suggested an Old Semitic saïf or sêf, Myres (1930) a possible Libyan or «Sea Peoples» word.' The Greek-Arabic connection is accepted; the direction Nourai draws is not asserted.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n       \"note\": \"sayf is not among the Persian loans in Arabic — as expected, since nobody claims an Iranian source for it.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\",\n       \"note\": \"no entry ( سيف ); Addi Shir lists only Persian words arabised, and sayf is not one.\"}\n    ]\n   },\n   {\n    \"id\": 5, \"lang\": \"Persian\", \"words\": \"sayf «سیف»\", \"verdict\": \"confirmed\",\n    \"derivation\": \"New Persian سِیف seyf 'sword' is a plain Arabic loan of the Islamic period: Arabic سَيْف sayf was taken over unaltered in spelling, with the usual Persian monophthongising pronunciation of the ay-diphthong (sayf > seyf), and it remains a bookish, chiefly poetic and phraseological word (سیف و قلم, ذوالفقار), the everyday word for 'sword' being شمشیر šamšir (< Middle Persian šamšēr). Moʿin's Farhang marks it exactly so: «سیف: [ع.] (اِ.) شمشیر، ج. سیوف» — an Arabic noun with the Arabic broken plural suyūf carried over with it. Wiktionary's Arabic entry likewise lists '→ Persian: سیف (seyf)' among the descendants. This last link of Nourai's chain is the only uncontroversial one in the box.\",\n    \"derivation_fa\": \"«سیف» در فارسی نو وام‌واژه‌ای عربی از دورهٔ اسلامی است: «سَیف» عربی با همان املا به فارسی آمده و مصوت مرکب ay در تلفظ فارسی به ey بدل شده است (sayf > seyf). این واژه در فارسی کتابی و بیشتر شعری و ترکیبی است (سیف و قلم) و واژهٔ روزمرهٔ «شمشیر» (از فارسی میانه šamšēr) جای آن را گرفته است. فرهنگ معین نیز دقیقاً همین را می‌گوید: «سیف: [ع.] (اِ.) شمشیر، ج. سیوف» — اسمی عربی که جمع مکسر عربی‌اش نیز همراهش وام گرفته شده است. ویکی‌واژه نیز در مدخل عربی «سیف» زیر بازماندگان می‌آورد: «← فارسی: سیف (seyf)». ادعای نورایی در این حلقهٔ پایانی درست است؛ و این تنها حلقهٔ بی‌مناقشهٔ این نمودار است.\",\n    \"sources\": [W_SAYF],\n    \"ref_check\": [\n      {\"ref\": \"MON:1979\", \"status\": \"supports\",\n       \"note\": \"Moʿin, Farhang-e Farsi s.v. سیف (2-vol. Adena abridgement, MON_part1.txt line 82277): «سیف: [ع.] (اِ.) شمشیر، ج. سیوف» — an Arabic loan, exactly as the chart draws it. The 6-volume edition is not online, so the page number itself could not be verified.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"سيف (Arabic), Descendants\", \"stance\": \"supports\",\n       \"note\": \"'→ Persian: سیف (seyf)' — Persian is listed as a borrower of the Arabic noun.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. سیف\", \"stance\": \"supports\", \"note\": \"as quoted; tagged [ع.].\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi 1988\", \"stance\": \"silent\",\n       \"note\": \"not listed, confirming that no one treats سیف as a Persian word that went into Arabic.\"}\n    ]\n   }\n  ]\n }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-267.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk267.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-267.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 267"
}
```


### [2026-09-06T21:13:22.135Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 6, 'plausible': 2, 'disputed': 4, 'transcription_suspect': 2}
root verdicts: {'plausible': 2, 'disputed': 1}
ref checks: {'supports': 14, 'partial': 4, 'not_checked': 1, 'contradicts': 1, 'not_found': 1}
books consulted: {'supports': 21, 'contradicts': 8, 'silent': 9, 'partial': 5} | by book: {'Wiktionary': 9, 'POK': 7, 'KLN': 5, 'WLD': 4, 'MON': 3, 'Etymonline': 2, 'LAT': 2, 'HRN': 2, 'PHD': 2, 'PLA': 2, 'BRT': 1, 'BQT': 1, 'Dehkhoda': 1, 'FRS': 1, 'AFM': 1}
```


## [2026-09-06T21:13:52.151Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-267.json` written; `verify_check.py 267` reports **14/14 nodes, 0 PROBLEM lines**.

**Counts** — nodes: 6 confirmed, 2 plausible, 4 disputed, 2 transcription_suspect. Roots: 2 plausible, 1 disputed. Ref checks: 14 supports, 4 partial, 1 contradicts, 1 not_found, 1 not_checked.

**Flagged items**

- **ROOT `Kiĕs` "bug, tick" — disputed.** Mann (IEC 622) is faithfully copied, but the root is his alone: no *ḱies- in Pokorny, Walde–Pokorny or Watkins. Modern view: a Semitic culture word (Proto-Semitic *sūs-, Akkadian sāsum).
- **`Kiĕs` #1 Armenian čeč — disputed.** Word is ցեց cʻecʻ (Mann prints *cec*, not *čeč*); Wiktionary: origin uncertain, "often considered a Semitic borrowing", or an areal/expressive insect-name (Udi c̣ec̣, Proto-Georgian-Zan *c₁ic₁-).
- **`Kiĕs` #2 Greek sěs, seos — disputed.** Wiktionary: "a Semitic loanword" (Aramaic sāsā, Hebrew sās, Akkadian sāsum, Arabic سوس); PIE *ḱ would give Greek κ-, not σ-.
- **`Kiĕs` #3 Persian sâs ساس — disputed.** Dehkhoda calls it عربی فصیح; no MP/Avestan antecedent (MacKenzie, Nyberg, Horn, Hübschmann silent); Borhan p.1073 has the insect but attaches no etymology.
- **`Kiph` #1 Sanskrit "šiphâ, čiphâ" — transcription_suspect, error_in: book.** There is only one word: Pokorny 598 prints `śiphā`, Walde–Pokorny I 452 the same word in the old transcription `çiphā`. Nourai read the two spellings as two words and rendered ç with a háček. The printed page shows "šiphâ, čiphâ" — extraction faithful.
- **`Kiph` #3 Greek "xiphos : branch, rod" — transcription_suspect, error_in: book.** Pokorny 598 has Messenian **κίφος** 'στέφανος' (wreath), not ξίφος. The book prints "xiphos : branch, rod" (page image confirms). ξίφος is Mycenaean (qi-si-pe-e) and Pre-Greek/Egyptian, so it cannot descend from *ḱiph- either.
- **`Kiph` #4 Arabic sayf — disputed.** TAD:39 does support Nourai's arrow («سيف - ويوناني ξίφος»), but Klein (s.v. xipho-) runs it the other way: Egyptian sefet → Aramaic saypā → Greek ξίφος / Hebrew sayif / Arabic sayf; Wiktionary: "either a loan, or from a common original source". TAD:78 not found.

**Extraction notes for the owner** (JSON vs. printed page)
- No wrong-character extraction errors: the odd forms (`čiphâ`, `xiphos`, `et-cĕ-terî`) are all what the book itself prints.
- Minor gap: the printed chart has an **empty box** to the right of the Avestan `zî` node (arrow into a blank rectangle, no language label or words); it has no counterpart in `data/extracted/batch/page-267.json`. Content-free, so nothing verifiable, but the chart artifact is unrepresented.
- Latin node #5: the book's `et-cĕ-terî` is the wrong form/quantity for the phrase glossed "and other things" (should be *et cētera*, neuter plural, long ē) — recorded as `plausible`, not an extraction fault.

Page image saved to `data/verification/sources/refs/ocr/BOOK/267.png`; Borhan p.1272 cached at `data/verification/sources/refs/ocr/BQT/1272.png`; 12 web pages archived via `fetch_source.py`.
