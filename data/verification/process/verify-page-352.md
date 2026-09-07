# Verification process log — verify-page-352


## [2026-09-07T18:17:49.159Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 352 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-352.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-352.json. Write /home/sfmqrb/git/rishe/data/verification/page-352.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 352` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T18:17:51.349Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T18:17:51.860Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T18:17:51.874Z] TOOL RESULT

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


## [2026-09-07T18:17:52.819Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-352.txt"
}
```


### [2026-09-07T18:17:52.850Z] TOOL RESULT

```
1	=== PDF page 352 (book page 322) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ne 1, Nei 3, An 4 : no, not  (refs POK:756; KNT:167)  PART 2
4	#1 (parent #0) [Greek] refs=AHD | a-,an- : no, not ; a-sěma : unstamped (silver) ☞Sěma ; a-tomos : "not breakable", atom ; a-sphallein, asphaltos : "not slippery", asphalt ☞Sphallein ; a-sbenunai : "not extinguishable", asbestos ☞Gwes
5	  #2 (parent #1) [Pahlavi] refs=KNT:209 | asěm : silver ; sîm : silver
6	    #3 (parent #2) [Persian] refs=KNT:209; BQT; MON | sîm 2 «سیم ۲» : silver, also referring to mercury and electric wire ☞Sěma
7	  #4 (parent #1) [Latin] refs=None | 
8	    #5 (parent #4) [French] refs=None | 
9	      #6 (parent #5) [Persian] refs=VOP | atom «اتُم» : "not splittable", atom ; âsfâlt «آسفالت ( اسفالت ، آسفالته )» : "not slippery"
10	    #7 (parent #4) [English] refs=AHD | a-, an-, atom, asphalt, asbestos
11	#8 (parent #0) [Latin] refs=AHD | in- : not
12	  #9 (parent #8) [English] refs=AHD | in- 2, ineffective
13	--- entry 1 ---
14	ROOT [Indo-European] Ne 2, Nes 2 : our, us  (refs POK:758)
15	#1 (parent #0) [Avestan] refs=POK:758; KLN:1683 | na 2 : us ; ahma, ahmâka : we
16	  #2 (parent #1) [Pahlavi] refs=BQT:1931; SNS:232 | amâg, amâh : we, us
17	    #3 (parent #2) [Persian] refs=BQT:1931 | mâ «ما» : we, us
18	#4 (parent #0) [Old Persian] refs=SOD:209 | amâxam : we
19	  #5 (parent #4) [Sogdian] refs=SOD:206,209 | m`x, m`ğw : we
20	#6 (parent #0) [Germanic] refs=AHD | uns : us ; unsara : our
21	  #7 (parent #6) [English] refs=None | us, our, ours
22	
```


## [2026-09-07T18:17:56.421Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-352.json",
 "description": "Read source JSON page 352"
}
```


### [2026-09-07T18:17:56.465Z] TOOL RESULT

```
{
  "pdf_page": 352,
  "book_page": 322,
  "entries": [
    {
      "root": {
        "name": "Ne 1, Nei 3, An 4",
        "lang": "Indo-European",
        "refs": "POK:756; KNT:167",
        "gloss": "no, not"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {
              "translit": "a-,an-",
              "gloss": "no, not",
              "script": null
            },
            {
              "translit": "a-sěma",
              "gloss": "unstamped (silver)",
              "script": null,
              "see": [
                "Sěma"
              ]
            },
            {
              "translit": "a-tomos",
              "gloss": "\"not breakable\", atom",
              "script": null
            },
            {
              "translit": "a-sphallein, asphaltos",
              "gloss": "\"not slippery\", asphalt",
              "script": null,
              "see": [
                "Sphallein"
              ]
            },
            {
              "translit": "a-sbenunai",
              "gloss": "\"not extinguishable\", asbestos",
              "script": null,
              "see": [
                "Gwes"
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
          "refs": "KNT:209",
          "words": [
            {
              "translit": "asěm",
              "gloss": "silver",
              "script": null
            },
            {
              "translit": "sîm",
              "gloss": "silver",
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
          "refs": "KNT:209; BQT; MON",
          "words": [
            {
              "translit": "sîm 2",
              "gloss": "silver, also referring to mercury and electric wire",
              "script": "سیم ۲",
              "see": [
                "Sěma"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "VOP",
          "words": [
            {
              "translit": "atom",
              "gloss": "\"not splittable\", atom",
              "script": "اتُم"
            },
            {
              "translit": "âsfâlt",
              "gloss": "\"not slippery\"",
              "script": "آسفالت ( اسفالت ، آسفالته )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "a-, an-, atom, asphalt, asbestos",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "in-",
              "gloss": "not",
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
          "refs": "AHD",
          "words": [
            {
              "translit": "in- 2, ineffective",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ne 2, Nes 2",
        "lang": "Indo-European",
        "refs": "POK:758",
        "gloss": "our, us"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:758; KLN:1683",
          "words": [
            {
              "translit": "na 2",
              "gloss": "us",
              "script": null
            },
            {
              "translit": "ahma, ahmâka",
              "gloss": "we",
              "script": null
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
          "refs": "BQT:1931; SNS:232",
          "words": [
            {
              "translit": "amâg, amâh",
              "gloss": "we, us",
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
          "refs": "BQT:1931",
          "words": [
            {
              "translit": "mâ",
              "gloss": "we, us",
              "script": "ما"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "SOD:209",
          "words": [
            {
              "translit": "amâxam",
              "gloss": "we",
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
          "lang": "Sogdian",
          "refs": "SOD:206,209",
          "words": [
            {
              "translit": "m`x, m`ğw",
              "gloss": "we",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "uns",
              "gloss": "us",
              "script": null
            },
            {
              "translit": "unsara",
              "gloss": "our",
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
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "us, our, ours",
              "gloss": null,
              "script": null
            }
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


## [2026-09-07T18:17:56.811Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T18:17:56.855Z] TOOL RESULT

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


## [2026-09-07T18:18:18.316Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -30 && sed -n '1,60p' tools/verify_check.py && python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','SOD','SNS','BQT','MON','VOP','AHD','KLN']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-07T18:18:19.608Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
```


## [2026-09-07T18:18:25.090Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['POK'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['KNT'],ensure_ascii=False,indent=1))\n\""
}
```


## [2026-09-07T18:18:25.836Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60 && wc -l POK_full.txt POK_01.txt POK_02.txt POK_03.txt 2>/dev/null"
}
```


### [2026-09-07T18:18:26.577Z] TOOL RESULT

```
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
{
 "title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953",
 "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/oldpers",
 "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt",
 "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.",
 "notes": "",
 "cites": "page number of Kent, Old Persian (1953); the lexicon starts p. 164"
}
```


### [2026-09-07T18:18:26.617Z] TOOL RESULT

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
  93771 POK_full.txt
   5151 POK_01.txt
   6715 POK_02.txt
   5974 POK_03.txt
 111611 total
```


## [2026-09-07T18:18:31.942Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=412 && NR<=416 {print \"=== NR \" NR \" ===\"; print}' POK_02.txt | head -200"
}
```


### [2026-09-07T18:18:33.305Z] TOOL RESULT

```
=== NR 412 ===
z-muorra  , Salzsumpf*  (*wöHö); apr.  mary  ,Haff'  {*mare) ;  lit.  märe,  meist  f.  PL  märes,  märios  ,Meer,  Ost- see, kurisches  Haff*;  aksl.  morje  ,Meer*;  baltoslav.  *pa-mariia-  n.  , Meeres- gegend* in  lit.  pa-marys  m.,  pa-märe  f.  , Seeküste*,  aksl.  po-morije  ,Meeres- gebiet*,  nhd.  Pommern.
WP.  II  234 f.,  WH.  II  33 f.,  Trautmann  169 f.;  nach  Specht  Idg.  DekL 119  zu  3.  mer-,
mormor-,  murmur-  Schallwort  ,murmeln,  dumpf  rauschen*.
Ai.  marmara-  ,rauschend*  m.  ,das  Rauschen*,  murmur a-  m.  ,knisterndes Feuer*,  murmurä  ,Name  eines  Flusses*;  arm.  mrmram,  mrmrim  (*murmur-am, -im)  ,murre,  murmle,  brülle*;  gr.  ixoQfxiuQü)  {*uoof.ivQ icü)  ,murmle,  rausche*; lat.  murmurö  ,murmle*,  murmur  n.  , Gemurmel,  Gemurr*;  ahd.  murmurön, murmulön,  nhd.  murmeln,  Kurzform  anord.  murra,  mhd.  nhd.  murren- Weiterbildung  ags.  murc(n)ian  ,klagen,  murren*;  ablautend  norw.  dial. marma  ,brausen  (vom  Meer)* ;  lit.  murmlenti,  murmenti  ,murmeln*,  murmHi, marmeti  , murren,  brummen* ;  ablaut.  marmalaX  ,große  Bremsen*  (eine  Kurz- form mit  Dissim.  m — m  zu  m — v  scheint  marvä,  mervä  ,Bremse*);  aksl. *mrzmrati  ,murmeln*.
r
749
Unredupl.  mit  7i-Suffix  ir.  muirn  (*murni-)  f.  ,Lärmen,  Sausen*. ^yp.  II  307 f.,  WH.  II  130 f.,  Trautmann  190;   zum  Folgenden?
0orii^o(.^^y  jGrausen,  grausig,  bes.  von  Gespensterfurcht'?
Gr.  fiOQ^id),  ixoQjxcüv  f.  »Schreckgespenst',  (xöofxoQog  ,Furcht',  fxOQ^o- lvY.eiov  jSchreckbild',  ^lOQ^o-XvTTo^at,  [j,OQf.ivvü)  ,setze  in  Furcht',  fivQfiog' q^dßog  Hes.,  MvQ(.uö6veg  eigentlich  ,das  Volk  der  Schreckgespenster';
lat.  formldö  ,das  Grausen,  peinigende  Furcht;  bes.  religiöse  Ehrfurcht'; farm-  diss.  aus  "^morm-  (wie  bei  formlca  :  ixvQ^ir]^).
WP.  II  308,  WH.  I  532.
0oro-  ,Brombeere'  (dann  südeurop.  auf  die  Maulbeere  übertragen).
Arm.  mor,  morij  moreni  ,Brombeere';
gr.  ^ÖQOv  {^ifjQOv  Hes.)  ,Maulbeere;  Brombeere';  cymr.  merwydden Jl  ,Maulbeere',  ist  aber  mit  e  als  Umlaut  von  o  auch  als  eine  Weiterbildung eines  keltischen  moro-  deutbar;  lat.  mörum  ,Maulbeere,  Brombeere'  gr. Lw.,  lat.  ö  als  Ersatz  des  geschlossenen  gr.  o-  gut  aus  Entlehnung  erklär- bar; ist  also  etwa  ein  *mÖrum  ,Brombeere'  durch  das  entlehnte  mörum aus  (xÖQOv  lautlich  absorbiert  worden?    Ob  zu  3.  mer-  S.  734?
Aus  dem  Lat.  stammen  ahd.  mür-j  mörhere,  mhd.  mülber  ,Maulbeere' und  lit.  möras  ds.
WF.  II  306,  WH.  II  114,  Specht  Idg.  Dekl.  119.
mortu-,  tabuistisch  entstellt :  uormo-,  mormo-,  mouro-  (germ.  auch  meuro-) jAmeise'.
Auf  morui-  sind  zurückführbar:  av.  maoirl-  (sekundär  m.  maurvay-), sogd.  ^m^wrö  f.,  npers.  mör  , Ameise';
air.  moirbj  Fl.  cymr.  myrion^  bret.  merien^  corn.  muryon;  abg.  mravi (daraus  umgebildet  russ.  muravej,  slov.  mräv,  bulg.  mravijd).
Auf  morm-'.  lat. 
=== NR 413 ===
 formica  (vgl.  zum  lautlichen  oben  lat.  formldö:  gr. (.LOQ{.id))]  gr.  !xvQf.iog  (Lycophr.),  (,iVQi.irj^j  dor.  (xvguä^  (Ä-Erw.  zum  ä-St., wie  bQi.Liyt.ag  lat.  formica^  ai.  valml-ka-  zum  I-St.,  und  ai.  vamra-hd  zum o-St.) ;    unklar  arm.  mrjiun  [*murjimno-)^  Gen.  mrjman.
Auf  norm- :  gr.  ßvqiia^,  ßoQi-ia^  Hes.  {ß-  Schriftbehelf  für  /,  vgl.  auch 8Q(j,iKag'  ^VQ(.i7]^  Hes.);  ai.  vaZTTiiÄa- m.  , Ameisenhaufen';  daneben  mit  ganz alleinstehender  Lautfolge  vamrd-  m.,  vamri  f.  , Ameise'.
Auf  mouro-'.  aisl.  maurr^  daneben  *meur-  in  dän.  myre^  schwed.  myi^a {*meu'i'iön-),  mndl.  Fl.  mure  (einmal  belegt)  miere,  nndl.  mier,  mnd.  mlre (zum  l  s.  van  Wijk),  mengl.  mire,  myre  (skand.  Lw.),  ags.  myre,  engl,  mire, heute  nur  noch  fis-mire  (vom  Ausspritzen  ihrer  Säure),   krimgot.  miera.
WP.  II  306  f.,  WH.  I  531  f.,  Trautmann  170,  Specht  Idg.  Dekl.  45.
750
niö[u]-lo- :  mu-lo-  , Wurzel,  Pflanze^;  als  ,Mund  der  Pflanze^  zu  mü-  S  7fsi Ai.  müla-  n.  ^WurzeF,  müla-karman-  n.  , Zauberei  mit  Wurzeln'
ir
art
gr.  fX(üXv  ,e'm  fabelhaftes  Wunderkraut  (Hom.) ;  gelbblühende  Knoblau  k
b  (Theophr.  Dioscor.)',  {.icblv^a  ,Knoblauchart^
WP.  II  303,  310,  Wackernagel  Sitz.-Ber.  Pr.  Akad.  1918,  410  f.
i22Ö[u]-ro-  :  znü-ro-  , stumpfsinnig,  töricht^.
Ai.  mürd-  ,stumpfsinnig,   blöde,   dumm^ ;    gr.   iio)q6q,  att.  ixwqoq  ,duiinn  -* töricht^  (daraus  lat.  mörus  ,närrisch,  albern^).  ^t^
WP.  II  303,  WH.  II  lt4.  '-§
■   ^- moz-g-o-,  moz-g-en-,  mos-k-o-  ,Mark,  Hirn^  '^
Ai.  majjdn,   majjä,   majjas-   ,Mark*,  mastülca-  , Gehirn',  mdstaka-  ,KopL  - Schädel*;  SiV.  mazga-  ,Mark,  Hirn';  ahd.  mar (a)^,  mar{a)kj  a.s.  mar g^  a^s» mearg,  aisl.  mergr  (Gen.  mergjar)  ,Mark*,   aschwed.  micergher]    ksl.  mozg^  ^ , Gehirn',  mo^dam  {*mozgem)^  Akk.  PL  mozdeni  ,Mark',  apr.  musgeno  ,Mark* wozu   (mit  Umstellung   aus  *mazgenes)   lit.   f.   PL   smageneSj  lett.  smadenet , Gehirn';  toch.  A  mäisunt  ,Mark'.
WP.  II  309,  Trautmann  172  f.,  Specht  Idg.  DekL  78  f.
mozgho-s  ,junges  Rind';  nur  arm.  und  griech.  ;^
Arm.  mozi   ,junges   Rind   ,Kalb*  =  gr.  ^oaxlov,    Demin.   zu  ixoc^og  m.
jjunger  Stier,  Kalb',  f.  Junge  Kuh,  Mädchen' ;  wohl  identiscsh  mit  i^öaxog
,Pflanzentrieb,  Schößling'.
WP.  II  309.  .
tnrk-  , eßbare  Wurzel,  Mohrrübe,  Möhre'?
Gr.  ßodyiava  , wildes  Gemüse'  Hes. ;  ahd.  mor{a)ha  ,Daucus  carota',  nhd. Mohr-rübe,  Möhre,  ags.  more,  moru  ds.,  spätahd.  Demin.  morhila  ,Morchel^ (möhrenähnlicher  Pilz);  dagegen  scheint  russ.  morkovh,  morkva  ,Möhre', serb.  mrkva  aus  dem  Germ,  entlehnt  zu  sein.
WP.  II  313.
•
inregh-in{n)o-  , Hirnschale,  Hirn'.
Gr.  ßQSxiiögy  ßqexua  n.  (und  ßgeyi-ia)  , Vorderkopf,  Oberschädel',  ags. hregen,  brcegen  n.  , Gehirn'  (engL  hrain),  afries.  brein,  mnd.  bragen,  bregen, nhd.  Bräge
=== NR 414 ===
n  m.  ds.
WP.  II  314.
mreghu-,  mrghu-  ,kurz'.
Präkr.  mühu-,  av.  mdrdzu-jlti-,  -Jva-  ^ßoaxvßiog^,  sogd.  murzak  ,kurz'; gr.   ßgaxvQ   ,kurz',   ßgdxscc   , seichte   Stellen';    dazu    ßQaxfaiv    , Oberarm', Komparativ  neben  ßQaaacjVj
751
lat.  Irevis  (zunächst  aus  dem  Fem.  *6re(x)wl)  ,kurz',  hrüma  ,Winter- sonnen wende,  Winter,  Kälte*  {*brevi-mä,  *hreu-ma  ,Zeit  der  kürzesten  Tage);
got.  gamaürgjan  ,verkürzenS  alid.  murg{i)  ,kurz',  murgfäri  ,zerbrechlich*, a^-s.  myrge  , angenehm*,  engl,  merry. Vf.  II  314,  WH.  I  115.
j.  IZ2U-  Schallnachahmung  für  den  mit  gepreßten  Lippen  erzeugten  dumpfen Laut:  jUndeutlich  reden,  unartikuliert  murmeln  (daher  auch  Worte  für ,stumm*);  Mund,  Maul;  den  Mund  geschlossen  halten  oder  schließen'; mü-ko-  , stumm'.
1.  Gr.  ^v,  ixv  , Ausruf  gepreßten  Schmerzes',  lat.  mü  facere^  mutmut facere  ,mucksen'.
2.  ai.  mnka-  ,stumm',  arm.  mwnj  , stumm',  gr.  ftCxdg,  (.(VTig,  uvTTÖg,  j^vSog, ^wagögf  Hes.  (j^vvöög  ,stumm',  lat.  mütus  ,st,umm';  vgl.  auch  älter  dän. muej  norw.  mua  ,schweigen,  nicht  mucksen';  ahd.  mäwen  , schreien',  lett. maunu,  mäwu^  maüt  , brüllen',  cech.  myjati  , muhen';  hierher  auch  nhd. Möioßj  ags.  rriziOj  meWy  aisl.  mär  (PL  mävar),  as.  meu  ds.
3.  [Ai.  mukhd-  n.  ,Mund'  stammt  aus  dem  Davidischen];  gr.  ^vXXov ^Lippe';  fj,vXXaivo)  , verziehe  den  Mund,  schneide  Gesichter'  (fxvara^  , Ober- lippe, Schnurrbart',  s.  Boisacq  m.  Lit.),  ahd.  mala  f.,  mhd.  mül  n.  ,Maul', mnd.  müle  ,Maul,  Schnauze',  aisl.  müli  ,Maul,  bes.  Oberlippe  an  Tieren, hervorragende  Felsspitze',  got.  faurmüljan  ,das  Maul  zubinden'  (ob  mit anl.  s-  dazu  norw.  smaul,  lett.  smaule  ,Maul'??);  s.  auch  unter  möu-lo- S.  750.
4.  Mit  dentalen  Formantien:
ludiX.  muttiö,  -Ire  ,mucksen',  muttum  nullum  ,keinen  Muckser'  (vgl.  oben mutmut) ;  ahd.  mutilön  jmurmeln^,  rieseln*,  müsse  , Quelle',  aisl.  mudla  ,mur- meln*,  daneben  mit  germ.  t:  norw.  dial.  mutra,  mengl.  muteren,  engl. mutter  ds. ;  lit.  mute  ,Maul*.
5.  Gutturalerweiterungen  (vgl.  oben  2.):
Mit  k:  gr.  [,iVycdo^aL  ,brülle*,  ixvx&iC^a)  ,schnaube,  spotte',  mhd.  mühen, mügen,  müwen  , brüllen',  abg.  myH  ,Gebrüll',  russ.  mycath  ,brüllen*,  skr. slov.  öech.  mukati  ,brüllen*.
Mit  g:  ai.  münjati,  möjati  ,gibt  einen  Ton  von  sich*  (Dhätup.);  mucchanä »schwellender  Ton* ;  gr.  (j,vKco  ,bringe  mit  geschlossenen  Lippen  einen  Laut hervor,  stöhne*  (daraus  lat.  mussäre),  iivyy
=== NR 415 ===
,6c,  , Seufzer*;
lat.  mügiöj  -Ire  ,brüllen',  conmügentö  ,convocantö',  müglnor  ,murmele  laut, brause*  (auch  ,nügäri  et  quasi  tardö  cönäri'),  umbr.  muieto  ,muttitum', mugatu  ,muttitö',   lat.  mügüäre  vom  Naturlaut   des  Esels;   ahd.  muckazzen
752
jleise  reden,  mucksen\  nhd.  mnd.  mucJcen  ,mit  halboffenem  Munde  reden*  '^' {kk  ist  expressiv),  ostfries.  muk  ,Kuß'.  ^^
6.  s-Erw. :  gr.^  ui(o  ,sicli   schließen,  von   den   Lippen  und  den  Auo-e^»  ^" (daher  f^voip  ,die  Augen  zusammenkneifend,  kurzsichtig* ;  (.ivdoj  , beiße  die Lippen  zusammen';  von  *iivai6g  ,verschwiegen' :  i^vozrjg  ,in  die  Mysterien Eingeweihter',  (xvaTLY,6g  ,die  Mysterien   betreffend',  ^vazrjQLOv  , Geheimnis geheime   Zeremonie*,  vgl.  auch  ^vsTv  ,in  die  Mysterien  einweihen';   norw mysa  ,die  Augen  zukneifen' ;  aus  dem  Germ,  hierher  auch  mnd.  mummelerL  ~" engl,  mumhle  ,murmeln',  mump,   norw.  mumpa  ds. ;  mhd.  mupf,  muff  ,Ver- Ziehung   des    Mundes',  mupfen,   muffen,   mnd.  mopen,  engl,  mope  ,gaffeii* engl,  mop  ,Fratze';  vielleicht  nhd.  bair.  mäuen  ,wiederkauen'  u.  dgl. ;
lett.  musindt  ,flüstern,  murmeln';  hitt.  mu-u-ga-ä-mi  (mügämi)  , spreche Klagegebete'.
WP.  II  309 ff.,  WH.  II  117,  119f.,  135,  139 f.,  Trautmann  188.  _;
2.  mü-,  znus-  schallnachahmend  für  ,Mücke,  Fliege'.
Arm.  mun,  Gen.  mnoy  , Stechmücke'   (*muS'  oder  *mu-no-) ;   alb.  mü-ze,  **" mi-ze  {ze  Diminutivsuffix)  ,Mücke';  gr.  iivXa  i^^^voia)  ,Fliege';  lat.  musca
aisl.  my  n.  (*müja-)  ,Mücke' ;  schwed.  mygg,  mygga,  ags.  mycg,  as.  muggia,   
ahd.  mucka  ,Mücke'  (*wi/Ä;2d);  mit  -s-  gotländ.  mausa  (*müsa),  fläm.  meuzie (*musl)]  lit.  muse,  apr.  muso,  lett.  müsa,  muSa  ,Fliege';  abg.  mucha  , Fliege' (*mousa)y  m^§ica  ,Mücke'.
WF.  II  311,  WH.  II  133,  Trautmann  191,  Specht  Idg.  Dekl.  43.
znuk-  , Haufe'  und  Zubehör?
Gr.  (ÄVKtav '  awQÖg  ^fxajv  Hes. ;  vorgall.  *mukina  , Steinhaufe'  (Jokl  V. Rom.  8,  193);  aisl.  mügi,  mügr  ,Haufen,  Menge',  ags.  müga  m.  ,(Korn-) Haufen',  müha  ds.  (auch  müwa),  vgl.  weiter  schwed.  dial.  moa  , zusammen- häufen' (*mühö7i),  ahd.  mü-werf  ,Maulwurf',  mit  -k^k)-:  mnd.  müke,  ndl. muik,  mhd.  müche,  nhd.  (halb  nd.)  Mauke  f.,  bair.  (echt  hochd.)  Mauche , Auswuchs,  Fußgeschwulst  der  Pferde',  Schweiz,  mauch  m.  ,Auswuchs an  Rebholz,  unordentlicher  Haufe'  und  mit  ü :  norw.  dial.  mukka  ,Haufen, Menge',  mhd.  mocke  m.  _,Klumpen,  Brocken'  (damit  identisch  ist  mhd. mocke  , Z
=== NR 416 ===
uchtsau');  aisl.  mostr  , große  Menge'  (*muh-stra-)]  einzige  Hoch- stufenform in  ags.  meagol  ,(*klumpig,  massig'  =)  ,fest,  stark'.
WP.  II  311;  nach  Hubschmid  ZnPh.  66,  33  f.  nichtidg.
inüs  jMaus'  auch  ,Muskel'  (älter  *müs,  musös  aus  *meus,  musös). Ai.  mü§-  m.  ,Maus,  Ratte',  np.  mü§  ,Maus';
arm.  mu-kn  ,Maus,  Muskel' ;  gr.  (j,vg  (^vdg,  ^vv  nach  ^g,  ''vög,  ^v)  ,Maus', auch  jMuskel';  alb.  ml  ,Maus',  lat.  müs  m.  ,Maus'  (mürlnus  :  mhd.  miusln
753
von  Mäusen*) ;  ahd.  mhd.  as.  mnd.  aisl.  ags.  müs  ,Maus,  Muskel'  (Kons. -St.) ib<^.  ""^y^^  ^'  »Maus'.
Vielfach  auf  Körperteile  angewendet:  arm.  muJcn  , Muskel',  gr.  (xvg Muskel',  [xv(bv  ,muskelreiche  Gegend  des  Leibes'  (woraus  auch  , wollüstiges \Veib'  in  gr.  ^vwv/a),  jwua^,  -aycog  m.  ,MiesDauschel,  Löffel'  :  lat.  mürex Purpurschnecke';  lat.  musculus  ds.,  ,Muskel',  ahd.  usw.  müs  ,Muskel,  bes. des  Oberarms',  mnd.  müs  bes.  ,der  Fleischballen  des  Daumens',  nhd.  Maus^ Mäuschen,  abg.  myhca  ,/9^orxtW';  andrerseits  ai.  muskd-  m.  ,Hode,  weibliche Scham',  npers.  musk  ^Bibergeil'  (aus  dem  Pers.  stammt  gr.  (xöayog,  nhd. Moschus)]  gr.  ixvGxov  , Geschlechtsorgan' ;
wohl  zu  ai.  musnäti  , stiehlt,  raubt'  usw.,  s.  unter  2.  meu-  , fortschieben'.
WP.  II  312  f.,  WH.  II  132  f.,    Trautmann  191,   Specht   Idg.  Dekl.  40f.
rnat-o-s  ,gestutzt'?
Lat.  mutilus,  mtitidus  ,verstümmelt',  *muticus  ,gestutzt',  mütöj  muttö Penis',  GN  Mutunus,  rom.  mutt-  ,abgestumpft' ;  ir.  mut,  gael.  mutach ,kurz'  (mit  expressivem  tt)\  vielleicht  auch  ir.  moth  ,penis'  als  , Stummel'.
WP.  II  312,  WH.  II  136 f.;  nach  E.  Lewy  eher  zu  lat.  mütus  S.  751, vgl.  , stumm' ;  ,verstümmeln'.
48
1.  nä-  jhelfen,  nützen*.
Ai.  nä-tha-  n.  , Hilfe*,  m.  ,Schützer'7  nä-tha-te  ,fleht*;  gr.  d-vl-vTi-ui -vä-fiev  ,nütze*,  Fut.  d-vrj-oojj  Med.  d-vi-vä-f.iat,  Aor.  <hn^fir]v  ,habe  Nutzen* oveiaq  n.,  richtiger  })vr]aQj  -arog  ,Nutzen*  (*o-7iä-wf),  usw.     '  |
WP.  II315.
2.  nä-  ,sich  fürchten,  schämen*,  Verbalnomen  auf  -sor-,  -sr-.
Air.  nä»'  ,bescheiden*  {*nä-sro-\  nd{i)re  , Scham*  (*7iä-smä);  hitt.  naÄ(Ä)- , fürchten,  sich  fürchten*,  nahSariia-  ,sich  fürchten*. H.  Pedersen  Hittitisch  187.
näg^h-  ,nüchtern*?  Nur  arm.  und  griech.
Arm.  naut'^i  ,nüchtern*;  gr.  viqcpw,  dor.  vdq)(a  ,bin  nüchtern*. WP.  II  317.
nak-  ,Fell*.
Gr.  vd%og  n.,  ya^rj  f.  , wolliges  Fell,  Vlies*,  äQvay.lg  f.  (für  *dQvo-vaxig) , Schaffell*,  vayiv(6)QL0v'  öig^a  Hes. ;  ags.
```


## [2026-09-07T18:18:38.988Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=418 && NR<=423 {print \"=== NR \" NR \" ===\"; print}' POK_02.txt"
}
```


### [2026-09-07T18:18:41.101Z] TOOL RESULT

```
=== NR 418 ===
(Nom.  näuh)  , Schiff,  Boot'  (nävya-  .schiffbar');  ap.  näviyä , Flotte'  (:  gr.  vriioq  ,zum  Schiff  gehörig');  näväja-  m. , Schiffer',  av.  navaza-  ds. (:  gr.  vav-rjyög  ds.,  vgl.  auch  lat.  nävig-äre,  -ium)-,  av.  nävaya-  , schiffbar' (über  ai.  ati-nu  s.  Brugmann  11^  137  Anm.  2);  arm.  nav  , Schiff'  (aus  dem Pers. ?);  gr.  hom.  vtjvg,  vrjög  {*vaf6g),  att.  vavg,  vscbg  , Schiff';  lat.  nävis  ds. (ursprüngl.  kons.  St.,  vgl.  Akk.  navem  =  ai.  nävam,  gr.  vfja) ;  air.  ndu  (Gen. nöe,  Dat.  PL  nöib)  , Schiff';  cymr.  noe  , flaches  Gefäß,  Backtrog',  bret.  neo ds.  (*näuia)]  hierher  gall.  (vorrom.)  navä  , Talschlucht',  auch  FIN;  gall. nausum , Schiff';  aisl.  nör  m. , Schiff',  nau-st  , Schiffsschuppen',  nöa-tün  (nöa  = gr.  viywv)  , Schiffsburg',  ags.  nöwend  , Schiffer',  (aber  mhd.  näwe,  ncdwe ,kleines  Schiff',  nhd.  dial.  iVawe  aus  dem  Lat.) ;  norw.  nö  ,Trog  aus  einem ausgehöhlten  Baumstamm',  nela  (*nöwilön-)  ,großer  Trog,  schweres  Boot',
48*
756
ahd.  nuosc,  mhd.  nuosch  m.  ,Trog,  Rinne',  afries.  nöst  ,Trog'',    mnd.  nöste  i
, Viehtrog',  Wassertrog' ;  hierher  der  lit.   FIN  Nova,  polonis.  Nawa.  -M
WP.  II  315,  WH.  II  148  f.,  J.  Hubschmid  R.  int.  d'Onom.  4,  3  ff.  ^;
2.  näu-  :  nou-  :  nü-   A.  ,Tod,   Leiche',    B.  ,bis   zur   Erschöpfung  abquälen.
ermattet  zusammensinken';  näuis  , Leiche'.  :
A.  Got.  naus  , Leiche*  {ga-nawiströn  , begraben*),  aisl.  när  ds,,  ags.  ntU) m.  ds. ;  aruss.  navh  , Leiche',  aöech.  ndv,  -i  m.  ,Jenseits,  Hölle',  lett.  ndwt ,Tod',  davon  ndwet  , töten',  näwities  ,sich  mühen,  sich  töten';  apr.  nowig ,Rurapf'.
B.  air.  7iüne  (älter  naunae)  f.,  cymr.  newyn  m.  ^Hungersnot'  (*w9w,mo-)  ;. bret.  naoun  (^ndu^no-)  ds. ;  mcymr.  neued  , Sehnsucht,  Not*  {*näu-ita) ;  lett.  i' ndwUies  (s.  oben),  lit.  novyti  , quälen,  töten',  is-novyti  , vernichten';  Kausat.  "^ aksl.  cech.  unaviti  , ermüden'.  Postverbal  cech.  ünava  , Ermüdung',  russ.  ^- dial.  ondva  , Müdigkeit',  schwundstufig  aksl.  unyti  ,schlaff  sein,  erschlaffen',  '^ öech.  nyti  ,dahinschmachten',  russ.  nyth  ,schwermüti^  werden'.  %
nou-ti-  in  got.  naups  f.  ,Not,  Zwang',  aisl.  naud,  naudr  f.  ,Zwano'  - Drangsal,  Notwendigkeit',  as.  nöd,  ahd.  not  ,Bedräng'nis,  Drangsal,  Not', ags.  nead-,  med  f.  ,Not,  Pflicht,  Drangsal';  apr.  nautin  (*näuti-)  (Akk.) ,Not' ;  im  Slav.  Formen  mit  u  und  g,  t  und  d  (s.  Meillet,  Slave  commun^ 61  f.):  aksl.  nqzda  , Zwang,  Gewalt,  Notwendigkeit'^,  poln.  n^dza  ,Not', abg.  ngditi  ,nötigen',  aber  auch  aksl.  nuzda  , Zwang,  Not',  nuditi  ,nötigen', poln.  nuda  , Langeweile';  mit  t  poln.  net  , Lockung',  bulg.  nut  , Zwang', poln.  nucic  (16.  Jhdt.)  , zwingen';  das  -d-  steht  als  idg.  Erweiterung  neben -t-,  das  
=== NR 419 ===
g  ist  durch  sekundäre  Nasalierung  entstanden.
WP.  II  316,  Trautmann  201  f.;  Loth  RC  45,   199 ff.
I.  xze,  ne,  nei  Satznegation  der  reinen  Verneinung  (ne  einzelsprachlich  auch   * Wortnegation   geworden);   n-  Wortnegation;  ne-k"o-s  , nicht  einer', nei-k^o-s  ds. ;  ne-k^e  ,und  nicht*,  ne-ue  ,oder  nicht*. ne:  ai.  nd  ,nicht',   ned   (iidid)   ds.,   av.  ap.  na-  ,nicht',   av.  nöit  (=  ai. ned),  ai.  nd-vä  =  av.  na-va  ,oder  nicht'  (vgl.  lat.  ne-ve,   und  genauer  air.  nö s.  unten) ;  ai.  naca  ,und  nicht'  (=  lat.  neque  usw.) ;
über  ne-  im  Arm.  {nual  ,langmssant'  aus  *ne-val-,  usw.)  s.  Dumezil BSL.  40,  48  f. ;
gr.  vB-  nur  (als  Ersatz  von  n-)  vor  verbalen,  dann  auch  andern  Adj. mit  dem  Anlaut  a,  I,  o,  mit  denen  es  kontrahiert  ist,  z.  B.  vTjy^saTog,  vrjXsrjg, rcüvu|u(>')os  (danach  sekundäres  vrj-  in  vrjTtoLvog  ,ungerächt',  dor.  värtoivog, usw.);
lat.  n^-  in  ne-fäs,  ne-sciö  (ne-sciens,  ne-scius),  ne-cesse,  ne-uter,  n'unquam, nusquam,  nüllus,  nön  (*n'oinlom'],  vgl.  ahd.  nhd.  nein),  ne-que  ,und  nicht,
757
jedenfalls  nicht'  (=  osk.  nep,  got.  nih,  air.  na[cK]  ,nicht^  ai.  na-ca),  osk. ne  ,non,  ne';  vgl.  auch  lat.  neg[äre,  -ötium']  oben  S.  418;  lat.  neu,  ne-ve, ^It  neive,  nlve  ,oder  nicht' ;
air.  oie-ch  ,aliquis^  cymr.  nep  ,quispiam'  (=  ai.  najcis  ^niemand',  aber mit  Abstreifung  des  negativen  Sinnes  in  Sätzen  mit  wiederholter,  aber einander  nicht  aufhebender  Negation ;  derselbe  Vorgang  in  lit.  nekas  ,irgend etwas^  nekurh  ,quidam',  usw. ;  ähnlich  gelangte  ne-ue  ,oder  nicht'  zur positiven  Bed.  ,oder'  in  :)  air.  nö,  nü,  cymr.  neu,  abret.  nou  ,oder',  auch verbale  Stützpartikeln  (für  Pronomina  infixa  und  das  relative  -n-)  air. no-,  nu-,  mcymr.  neu-  als  ursprüngl.  formelhaft  vorgesetztes  ,oder  nicht?'; proklitisches  *ne  ergab  *na  (wie  z.  B.  ir.  ass-  ,ex')  im  Vorton  in  der Verbindung  air.  na\_Gh],  mcymr.  nac  (usw.)  ,nicht'  aus  ne-k^e  mit  urkelt. Apokope(?)  des  ausl.  -e;
got.  ni,  ahd.  as.  ni,  ne,  ags.  ne  , nicht';  aisl.  ne  in  der  nur  poet.  Bed.  ,non', während  ne  in  der  Bed.  ,n^que'  ==  got.  nih  (gleichbed.  mit  ni  geworden) aus  *ne-k^e  =  ahd.  nih-ein,  as.  (mit  gramm.  Wechsel)  nig-en  ,kein'  (aber as.  nee  ,und  nicht'  ==  lat.  neg-^  s.  oben  S.  418) ;  ahd.  Konjunktion  noh  ,noch' aus  *neÄ  (^ne-k^e)  oder  aus  ne  +  ahd.  ouch  ,auch' ;  ahd.  nein,  as.  nen  ,nein' aus  *ne  +  oinom  , nicht  einer'  (s.  oben  lat.  nön,  nüllus);  ags.  nä  ,me,  nicht, nein',  engl,  nö  ,nein'  (auch  aisl.  nei  ,nein'  aus  *ni  +  aiw  =  as.  ahd.  nio ,nie') ;
apr.  ni,  lit.  ne  , 
=== NR 420 ===
nicht',  nekas,  nekurls  (s.  oben);  aksl.  ne  ,nicht';
hitt.   natta  ,nicht*,  näwi  ,noch  nicht'.
ne:  ai.  (ved.)  na  ,nicht';  lat.  ne  , nicht'  in  ne-quidem,  nequäquam,  nsqm- quam,  nequam,  gekürzt  wahrscheinlich  in  neutiquam  (aber  ne-uter  mit altem  *ng,  s.  oben),  ne  Konj.  ,daß  nicht',  osk.  ni  ,ne'  (nz-p  ,neve'),  marruc. ni  ,ne';  air.  ni,  mcymr.  ny,  ncymr.  ni,  corn.  ny,  bret.  ne  ,nicht'  (z.  T.  mit sekundärer  Kürzung);  air.  nl  ,ist  nicht'  ist  das  gewöhnliche  nl  mit  aus- gelassener Kopula;
got.  ne  ,nein'.
12 ei  betontes  ,nicht':  av.  nae-cis  ,keiner',  adv.  ^laecis  verstärkte  Negation; lat.  7ü,  altlat.  nei  Adv.  und  Konj.  1.  älter  ,nicht,  daß  nicht',  2.  ,si  non', quid-nl-,  osk.  nei  ,nicht'  (nei-p  ,neque');  got.  nei  {&TC.ley.)  ,nicht^  aisl.  nl ,nein',  ahd.  nl  emphatisches  ,nicht';  lit.  nie-kas  ,niemand',  ne%  ,auch  nicht, nicht  einmal' ;  aksl.  ni  ,neque',  ni-Uto  ,niemand' ;  die  germ.  Formen  viel- leicht aber  =  ai.  ned  ,durchaus  nicht,  damit  nicht',  av.  nöit,  ap.  nay  aus idg.  *ne  id  ,das  nicht';  vielleicht  ist  idg.  nei  aus  *ne-\-l  (vgl.  ovtoa-l)  zu deuten.
h-  Verneinungspartikel  als  erstes  Glied:  ai.  av.  ap.  a-,  vor  Vokalen  (auch i,  u)  an-',  gr.  ä-,  vor  Vokal  a»'-;  lat.  in-,  ältest  en-  (die  vorkonsonantische
758  '
Form);  osk.  umbr.  an-;  air.  in-  (vor  Med.),  e-  (vor  Tenuis),  an-  (y^  ' Vokal),  cymr.  com.  bret.  an-]  got.  ahd.  as.  ?m-,  aisl.  ö-,  ö-;  im  g^i durchaus  durch  ne-  verdrängt;  über  ksl.  ne-je-veTb  , ungläubig',  '^^-je-sytt, ,unersättlich  =  Pelikan'  s.  Berneker  429;  toch.  AB  a(w)-,  am-^  efnV em-,  071- ;  durch  mehrere  Sprachen  durch-gehende  Entsprechungen  sind  z.  B  » ai.  amfta-,  ^(.ißgoTog,  immortalis]  ai.  djnäta-,  Hyrcorog,  arm.  ancanaut' ignötus,  air.  ingnad,  got.  unJcunps]  ai.  anudrd-,  äwögog,  usw.
WP.  II  319f.,  WH.  II  150f.,  152,  165f.,  Trautmann  194f.,  Schwyzer Gr.  Gr.  1,  431  f.,  2,  590  ff.
:2.  22e,  ne,  enklit.  Partikeln  s.  oben  S.  320  f.
5.  ne-,  no-,  Plur.  nes-,  nbs-  ,wir'  (ursprüngl.  außerhalb   des  Nominativs* Nom.  s.  unter  *we).
1.  Ai.  Du.  Akk.  Dat.  Gen.  nau,  gthav.  G^n.  nä,  aksl.  nä,  gr.  yw,  hom. ywt  aus  *v(ü-J^t  (dessen  2.  Glied  der  Nominativst.  *ue-,  *id-  ist) ;  air.  nä(tha)r  ^ Gen.,  got.  ughis,   as.  wwc,   anord.   o^Är  ,uns  beide  (n)'  (unc  =  *n-ge,  vgl. mik  aus  *me-ge).
2.  Pluralisch:  ai.  waA  enklit.,  av.  W9,  nä,  nö,  lat.  nös,  alb.  na  Nom.  (*nd«), Tie  Gen.  Dat.  Akk.  (*nös);  ir.  ni  usw.  (scheint  *s-7ies).  Gen.  ar  n-  (*ns-rö-m),  ~" cymr.  corn.  bret.  ni,  ny  ,wir'  (*we5),  got.  ahd.  uns, 
=== NR 421 ===
 as.  w«,  anord.  oss  ,uns' (*ns),   aksl.  nas^  Gen.  (j^nös-söm),  apr.  nöuson  (ebenso) ;  £■_
auf  *nsme  (wohl  ns  -j-  Partikel  *sm-,  verwandt  mit  dem  -sm-  der  Pron.- Dekl.,  z.  B.  ai.  td-sm-ät)  beruhen  av.  ahma  (ai.  asmän,  ap.  Gen.  amäxam) =  äol.  ^'^u^-,  dor.  ö^-,  ion.-att.  ij^u- ;  Poss.  lesb.  ä^(j,og,  dor.  ß^iog  =  av. ahma-,  ion.   -att.   'fj^hsgog)  usw. ;   hitt.  Datt.  Akk.  anzäs,   enkl.  was  ,uns*.
WP.  II  320  f.,   Schwyzer  Gr.  Gr.  1,  600  f.
I.  nebh-  ,bersten'??
Ai.   ndhhate  , birst';    aisl.  ncefr  ,die  äußere  Birkenrinde'  als   ,berstend, sich  losschälend'. WP.  II  330.
2.  nebh-  s.  oben  S.  315  f.
I.  ned- ;  zicd-  , zusammendrehen,  knüpfen';  i2Öcfo-/-ä  , Geknüpftes'.
1.  Lat.  nödus  , Knoten'  (idg.  *nödos)',  vermutlich  nassa  (*nad-s-a)  , Fisch- reuse, geflochtener  Korb  mit  engem  Halse';  nectö,  -ere,  nexl,  nectum ,knüpfen,  binden'  ist  Neubildung  nach  j^Zec^ö;  mit  der  Bed.  ,nahe'  aus  ,eng verknüpft' :  osk.  nessimas  Nom.  PL  f.  ,proximae',  umbr.  nesimei  ,proxime';
air.  Kompar.  nessa,  Sup.  nessam  ,propior,  proximus',  cymr.  nes,  nessaf, corn.  nes,  mbret.  nes,  nessaß  ds. ;  air.  nascim  ,binde,  verpflichte*  (*n^d-sJcö),
759
arrienas  ,1  will  bind'  (usw.),  naidm  ,das  Binden,  Vertrag-^  for-naidm  ,Band^ nasc  ,Ring'  (^S^-  zur  -sÄ-Bildung  ahd.  nusca^  das  auch  im  u  =  ,  überein- stimmt^ ferner  av.  naska-  ,Textsammlung',  wahrscheinlich  eig.  ,Bündel'); bret.  nasJca  ^anbinden';
got  nati,  ahd.  nezzi,  as  net,  netti,  ags.  aisl.  net  ,Netz%  dehnstu%  (wie lat.  nödus),  aisl.  not  f.  ,großes  Netz';
mit  formantischem  -s-k-,  -s-t- :  ahd.  nuska,  mhd.  nüsche  ,Mantelschnalle', as.  nusk(i)a  , Spange'  (s.  oben);  aisl.  nist,  nisti  n.  , Spange  am  Kleid',  nista ^zusammenheften';  nesta  , festheften,  festnageln',  mhd.  nes^en  (nesteln)  , fest- binden" schnüren',  ahd.  nestilo,  nestila  ,Schleife,  Schnürriemen,  Binde', nhd.  Nestel,  as.  nestila  , Binde,  Haarband',  agutn.  nast,  nestli;  reduktions- stufig ags.  nos(t)le  ,Band';
daß  ned'  eine  Erw.  von  (s)?ie-  ,zusammendrehen'  sei,  wird  außer  durch die  Bed.  auch  durch  die  s-anlaut.  Formen  air.  snaidm  , Knoten'  (vgl. oben  naidm)  und  nhd.  hess.  Schnatz  ,das  geflochtene  und  um  die  Haar- nadel gewickelte  Haar  der  Frauen,  Kopfputz  der  Bräute'  (*snatta-  mit srerm.  -tt-)  wahrscheinlich.
2.  Hierher  vermutlich  die  Bezeichnungen  der  Nessel  (als  alter  Gespinst- pflanze) :
Gr.  didiyL7]  {*nd-ikä) ;  ahd.  nazza,  aisl.  nqtr,  ahd.  nezzila  (germ.  *natilön), ags.  netele]  daneben  mit  idg.  -t-  (also  *n9-t-,  nö-t-  als  ^Erw.  zur  vermut- lichen Wurzel  (s)ne-)  apr.  noatis,  lit.  notere,  notre  , Nessel',  nötryne  ,Taub
=== NR 422 ===
- nesseP,  lett.  ndtrCj  nätra  ,Nessel',  slav.  *nat'b  , Krautblätter'  in  slov.  nät (Gen.  nati),  poln.  nac  ds.  und  allenfalls  (als  redupl.  urkelt.  *ni-nati-?) mir.  nenaid,  nir.  neantög  ,Nessel',  dissimil.  bret.  linad  ds. '  WP.II  328  f.,  WH.n  144  f.,  155  f.,  172  f.,  Trautmann  194,  H.  Jacobsohn Arier  u.  Ugrofinnen  90 f.;  s.  unter  (s)we-.
2.  ned-  ,tönen,  brüllen,  rauschen'.
Ai.  nddati  ,tönt,  brüllt,  rauscht',  nada-  m.  ,Brüller,  Stier,  Fluß*,  nadi- f.  ,Fluß,  Flut',  nadl-na- m.,  nadl-sa-  m.  ,Meer',  usw.;  av.  wacZ- , schmähen'; gr.  (illyr.)  FIN  Neda  (Arkad.),  Nedwv  (Messen.);  thrak.  FIN  NeOTog] illjr.  FIN  Nearog  (Dalm.)  aus  *ned-to-.
A.  Mayer  Mel.  Boisacq  II  132  f.,  Krabe  IF.  58,  209  ff.
nedo-  ,Schilf'?
Ai.  nada-  m.  vermutlich  , Schilfrohr',  npers.  nai,  dial.  nad  , Schilf;  arm. net    ,Pfeil';   lit.    nendre   (und    Undre)   ,Schilfrohr'   (mit  Nasal   nach    lenkti ,biegen'?);    lett.  nasli  , Schilf  aus  *nadslis? WP.  II  329 ;  vgl.  Kuiper,  Proto-Munda  82.
760  •
negh-  , durchbohren,  stechen'.
Mir.  ness  , Wunde'  {*negh-8-)]  reduktionsstufig  aksl.  v^-nhzq  , steck hinein',  Infin.  v^-nhzngt^,  Kaus.  russ.-ksl.  v^-noziti  , hineinstechen'-  aksl nozh  , Messer';  ob  hierher  ai.  dhsu-  , Stange'  (*ngh-su-)?
WP,  II  326  f.,  Trautmann  200.
1.  nei-,  neio-ini-  , führen'.
Ai.  ndyati  (Partiz.  nltd-),  av.  nayeiti  , führt',  mpers.  nltan  , führen treiben',  ai.  nlthä  f.  , Führung,  Weg',  nltho,  netä^  ,Führer',  nitar-,  netdr- m.  ds.,  netrd-  n.  , Führung,  Auge';  mir.  ns,  nla  ,Krieger,  Held'  {*neit-i\ Gen.  Sg.  urir.  netas,  air.  niatJi  {*nei-t-os\  s.  auch  2.  nei-)]  hitt.  näi-,  lenken führen'.
WP.  II  321,  Pedersen  Hitt.  §  77  f.,  81,  Frisk  Suffixales  -th-  öf.
2.  nei-,  neis-  :  ni-  , lebhaft   bewegt   sein,    erregt   sein,   glänzen';    noi-bho-^
,gut,  heilig';  kelto-germ.  nei-to-,  ni-tu-  , Leidenschaft'.
Lat.  niteö,  -ere  ,glänze,  strahle',  nitidus  , glänzend',  nitor  ,  Glanz'  (von einem  Partiz.  *ni-tö-) ;  vielleicht  re-nldeö  , erglänzen'  (mit  präsensbildendem -d(hy)]  *nei-bhO'  in  mir.  nlab  , Lebenskraft',  cymr.  nwyf  ds. ;  noi-bho- in  apers.  naiba-,  npers.  new  , schön,  gut',  air.  nolh  , heilig';  *nei-mä  in mir.  nlam  , Glanz,  Schönheit';  *nei-Jco-  in  mir.  mach  m.  ,Held',  nlachus m., Tapferkeit';  *nei-to-  in  cjmr.  nwyd  , Leidenschaft',  hispan.  Kriegs- gott Netö]  air.  PN  Nlall  (Gen.  NeiU)  aus  *neit-s-lo-s]  steckt  vielleicht auch  in  air.  ma  ,Held'  (s.  1.  nei-)]  germ.  ^nipa-  in  got.  neip  n.  ,Neid', ags.  m(J  m.  , Kampf,  Haß,  Feindschaft',  as.  afries.  nith  , Eifer,  Haß,  Neid\ aisl.  nid  ,Hohn,  Schmach';  könnten  auch  zu  air.  nlth.  n.  (idg.  *i2ifu-) ,Kampf  gehören;  zweifelhaft  ai.  nila-  , schwarzblau',  naya
=== NR 423 ===
nä-  r\.  f.  ,Auge', netra-  n.  ds.
WP.  II  321,  336,  WH.  II  168,  171,  Vendryes  RC.  46,  265  ff.
3.  nei-,  ni-  s.  oben  S.  312  f.
I.  neid-  ,heruntermachen,  schmähen'.
Ai.  nindati,  Pass.  nidyd-te  , schmähen,  tadeln,  verachten',  dnedya-  ,nicht zu  schmähen',  nid-,  nidä,  nidä,  nindä  , Schmähung,  Tadel,  Verachtung'; av.  naed-  (näisml)  ,schmähen';  arm.  anicanem,  Aor.  3.  Sg.  anec  ,fluche' (*oneid-s-et) ;
gr.  ^vsLÖog  , Vorwurf,  Schmach',  dvsiöi^a)  , schmähe'  (o-Präfix  ,be-schimpfe', wie  auch  arm.  anicanem) ;  got.  ga-naitjan  , schmähen',  naiteins  , Lästerung', ■  ahd.  neizzen  , quälen,  plagen',  ags.  ncetan  ds.;  lit.  niedeti,  lett.  nist  ,ver- achten',  naids,  naidus  ,Haß,  Feindschaft'.
WP.  II  322  f.,  Kuiper  Nasalpräs.  130,  Trautmann  193;  wohl  zu  nei- S.  312f.
r
761
ueid-  '  n^d-  ^fließen,  strömen',  FIN  Neidä,  Nidä.
^i.    nedati  ,  flließt,    strömt';    gall.    FIN   Nida   ,Nidda'    und   ,Nied',    brit. pi^  Nida,  cymr.  Nedd  ,Neatli' ;  vollstufig  poln.  FIN  Nida,  lit.  FIN  Niedä, apr.  FIN  Nyda  ,Neide'. J.  Löwenthal  ZONF.  6,  81,  Krähe  BzNF.   1,  248ff.
aeig^-  ^waschen';  Pass.  Partiz.  nig'A-to-.
Ai.  nBnekti  , wäscht,  reinigt',  Aor.  anäiksU,  Pass.  nijyate,  Partiz.  niktd-, ninikta  Imper.  , waschet',  Kaus.  nejdyati-,  Aor.  naBnizaiti  Intens.  , wäscht ab,  spült  weg';  gr.  vit,o}  (*nig'^iö  =  ir.  nigim)  ,wasche',  Fut.  vlipw,  Aor. l^/ii//«,  viTtTQOv  ,Waschwasser',  x^Q-^'^yj  ds.,  ä-viTizog  ,ungewaschen'  (=  ai. niUd-,  ir.  necht)]  gr.  äviyqög  .^äy-ad-aq-coc,^^  ]  lat.  noegeum  (^noigV:-io-)  ,Schweiß- tuch^;
air.  nigid  , wäscht'  {'^nig^ieti,  Verlust  der  Labialisierung  vor  x),  Fut. -ninus  =  ai.  (Gramm.)  niniksati-,  necht  ,rein';  mcymr.  enneint  ,Bad' (*an-nig-antio-]  das  g  aus  dem  Präs.  übertragen);
germ.  *nikwe8^  -us-  in  aisl.  nykr  (Gen.  nyks)  , Wassergeist,  Flußpferd', ags.  nicor  ,Wasseruntier,  Krokodil',  ahd.  nihhus,  nichus  , Flußuntier, I  Wassergeist',  nhd.  Nix,  ahd.  nichussa  , weiblicher  Wassergeist,  Nixe', mndl.  nicker,  mnd.  necker  , Wassergeist'.
WP.  II  322,  Thurneysen  Gr.  115;  anders  Vendryes  RC.  47,  442  ff.
neik-  , Getreide  schwingen'.
Gr.  XiTiLidü)  jhandhabe  die  Getreideschwinge',  Xiy.fxr)rrJQ  ,der  das  Getreide schwingt',  Xi^iög,  XUvov  , Getreideschwinge',  diss.  aus  *viyLu6q,  *vUvov, vgl.  veTaXov,  vUXov,  vL'/,a '  XiTifj,^  Hes.,  wie  auch  tx^«y  •  Xixfiav  Hes.  (oder Haplologie  hinter  ava :  dvLy.^cbi.ied'a) ;  mir.  cruth-necht , roter  Weizen',  cymi-. nithio,  bret.  niza  , worfeln'  (auch  wohl  cymr.  gwenith,  bret.  gioiniz,  corn. gwaneth  ,  Weizen') ;  lit.  niek�
```


## [2026-09-07T18:18:59.025Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==182 || NR==183 {print \"=== leaf \" NR-1 \" ===\"; print}' KNT.txt | head -60"
}
```


## [2026-09-07T18:18:59.143Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=223 && NR<=226 {print \"=== leaf \" NR-1 \" ===\"; print}' KNT.txt | head -80"
}
```


### [2026-09-07T18:19:00.222Z] TOOL RESULT

```
=== leaf 181 ===
sed him, him- self becoming now king in Parsua, later called Ратѕа. Arsames, however, was not put to death, but (as the OP inscriptions tell us) lived on until after his grandson Darius got the throne of the Persian Empire. Thus Hystaspes never was king, and is not counted among the nine Achaemenian kings. Cyrus II thereafter conquered Media and added it to his dominions, and then extended his conquests in all directions. But he did belong by ancestry to the Achaemenian line; one can hardly brand him as a rank outsider.
Possibly Ctesias’ story, as repeated by Nicolaus Damascenus, originated in the line of Darius as a means of discrediting the line of Cyrus and of. justifying Darius in his seizure of the imperial power. The particular occasion might well be the unsuccessful revolt of Cyrus the Younger against his brother Artaxerxes IT, whom Ctesias served as personal physieian. Cf. JAOS 66.211 (1946).
IL SMERDIS AND GAUMATA
According to Behistan 510-513, Cambyses son of Cyrus killed his full-brother Smerdis, with such secrecy that his death was not known to the people; he then invaded Egypt. While he was on this expedition, rebellions developed in Persia and in Media and elsewhere. Notably a Magian named Gaumata headed the rebels, claiming to be Smerdis son of Cyrus, and he gained the kingship in all the rebellious territory. Cambyses, still in Egypt, committed suicide.
Gaumata started his rebellion in XII 14 of 523/2, and received the adherence of the Empire on IV 9 of 522/1. But Darius, a distant cousin of Cambyses, knowing that Gaumata was not the real Smerdis, with the aid of a few men fought with and slew Gaumata and his chief followers, on
VII 10 of the same year, at Sikayauvati, a fortress in Nisaya, a district of Media. Thereafter Darius became King.
Herodotus tells the same story at much greater length, in Book 3, chapters 1-38, 61-88. Cambyses invaded Egypt (chap. 1), and the reasons for the invasion and the course of the campaign are given (1-26). At Memphis he inflieted a fatal wound on the sacred bull which was worshipped as the God Apis (27-9), and thereupon lost his reason. Jeal- ous of his brother Smerdis’s prowess with the great bow which had come from the Ichthyophagi, he sent Smerdis back to Persia, and then, after a dream which betokened that Smerdis would sup- plant him, he sent his henchman Prexaspes to murder him secretly, which he did (30-8), esp. 30).
160
The Magus Patizeithes had been left by Cambyses as managing steward of his palace at Susa, and he was one of the few who knew of the death of Smerdis. He had himself à brother who greatly resembled Smerdis in appearance, and, says Herodotus, this brother's name was also Smerdis. Patizeithes put his brother Smerdis on the throne, under the pretense that he was Smerdis son of Cyrus and brother of Cambyses. The false Smerdis, by not admitting to his presence any one who had known the true Smerdis, successfully con- cealed his true identity for some time (61-2). But the news reached Cambyses in Egypt, and he knew the truth, because Prexaspes assured him that he had slain the real Smerdis. Resolved to fight the usurper, he leaped upon his horse to lead his army back to Susa, but as he did во he accidentally struck the point of his sword into his thigh, and from the wound he died (63-6). Thus the false Smerdis ruled for some months; but a Persian
OLD PERSIAN
nobleman, Otanes son of Pharnaspes, suspecting his identity, managed by a ruse to prove it to himself (67-9), and secured the help of five other trusted noblemen, to whom there was added Darius, who had come to Susa from his father Hystaspes, governor of Persia (70; see App. IIT). Darius insisted on immediate action against the two Magi (71-3). Helped by the confusion follow- ing the public confession of Prexaspes that he had murdered the true Smerdis, and by his suicide, the seven men burst into the presence of the two Magi and slew them (74-9). They then agreed upon a method of selecting one of their number to hold the throne, and Darius, aided by the trickery of his groom Oebares, was the winner (80-8).
The two accounts, it will be seen, agree in the main features, but differ considerably in the de- tails. Herodotus’ story has clearly entered into t
=== leaf 182 ===
he field of historical romance. See also PW 3A.710-2, s.v. Smerdis.
III. Tae HELPERS or DARIUS
The names of the six Persian noblemen who co- operated with Darius in slaying Gaumata the false Smerdis, are given in Behistan §68 and in Herodotus 3.70; there is agreement in the names of the first five:
Behistan Herodotus Vi"dafarnd son of Vayaspdra —— Intaphernes {Дата son of 8uxra Otanes son of
Pharnaspes
Gaubaruva son of Mardunitya ^ Gobryas Vidarna son of Bagübigna Hydarnes Bagabuxsa son of Détuvahya ^ Megabyzus Ardumamé son of Vahauka Aspathines
Herodotus, it will be seen, differs from the Behistan account in the name of the father of
Utana-Otanes; but he gives (7.82) Mardonius, the general in the third invasion of Greece, as son of Gobryas, which indicates agreement as to the name of Gobryas’s father. But Megabyzus son of Zopyrus (7.82) may or may not be the Behistan Bagabuxía son of Datuvahya, or his grandson. Herodotus does, in fact, mention all six of the helpers of Darius in passages outside 3.68-88, in passages which may be found in any Index Nomi- num Propriorum to the text of Herodotus.
The Behistan inscription mentions Vidarna again in §25, as defeating one of Phraortes’ armies in Media; Vi"dafarna in $50, as defeating the rebels at Babylon; Gaubaruva in $71, as crushing the last revolt of the Elamites.
IV. Tug Persian CALENDAR AND Benistan I-IV
In Behistan 4.4, Darius states that the 19 battles recorded by him in the first three columns of the inscription, with the attendant capture of 9 usurpers, took place hamahyáyà 6arda ‘in one and the same year’. For eighteen of the battles dates are given in the Persian calendar, with translation into the Elamite and the Akkadian. The difficulty has been to arrange these dates within one year, beginning with the killing of Gaumata, the false Smerdis; for the order of the months in the Persian
calendar, and in the other calendars, was by no means certain. Now, however, with evidence from additional Akkadian and Elamite tablets which have no Old Persian version, Arno Poebel has suc-
ceeded in reconstructing the lists of months, as
follows:!
! AJSLL 55.139-42. The Persian calendar has been the subject of many studies, but Poebel’s studies have sup- planted them all: ALSLL 55.130-65, 285-314, 56.121-45. Cf. also Hinz, ZDMG 96.326-31;
TEXTSIWITH NOTES AND TRANSLATION
Old Persian Elamite Akkadian Equivalent
1 Adukanaiša Hadukanna$ Nisabbu Mch.- Apr. 2 Otiravahara Turmár Andru Apr.- May 30üigarci$ — Sdkurrisif —— Simannu May- June 4 Garmapada Karmabada$ Dwūzu June- July ОТОТ Turnabagi$ Abu July- Aug. ена агра (та) & — Ulülu Aug.- Spt. 7 Bügayüdi$ — Bagijüti Taxritu = Spt.- Oct. 8 *Vurkazana Margaíana$ Arahsamna Oct.- Nov. 9 Aciyadiya  Haifuüt(;a)& Küslimu — Nov.- Dec. 10 Anémaka HandmakaS Tebétu Dec.- Jan. It Sami(ia)maS Sabitu Jan.- Feb. 12 Viyarna = =Mitia)kannaS Addàru Кер. Мер.
The narrative of the revolts, however, is not given in temporal sequence in Columns Т-Ш, but rather in а geographical order conditioned by the order in which the rebellious provinces are named in $22: Persia, Elam, Media, Assyria, Egypt, Parthia, Margiana, Sattagydia, Seythia. If we should reduce the story to a more easily intelligible pattern, it would be аз follows:
After Cambyses, son of Cyrus the Great, secretly slew his full-brother Smerdis and went on the expedition to conquer Egypt, uprisings against his rule took place in Persia and in Media and elsewhere (810). Notably a Magian named Gaumata led the revolt, claiming to be Smerdis, whose death was known to but few; he started his revolt on XII 14 of 528/2, and received the adherence of the entire Empire, becoming King on IV 9 of 522/1? Cambyses died by his own hand, either intentionally or accidentally, in Egypt soon after hearing of Gaumata’s revolt, (§11).
Three months later Darius and his associates killed Gaumata and his ehief followers at Sikayau- vati in Media, on VII 10 of 522/1. Thereby Darius
2 The months will be indicated by Roman numerals.
161
became King, but at the very outset his rule was contested by Agina in Elam, and by Nidintu-Bel (claiming to be Nebuchadrezzar son of Nabonidus) in Babylon, who were recognized as King each in his locality. But Аспа did not last long; Darius, after organizing the gove
```


### [2026-09-07T18:19:01.659Z] TOOL RESULT

```
=== leaf 222 ===
-. — fra&aram asn. XPf 26f, 37.
Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-ra-da, АКК. pa-ra-da-’ ; perhaps thematic noun- stem (§141) to fra- + *dà-, with vriddhi ($126), cf. Av. früd- ‘to further, increase’ (ТИМ. AiW 1012), but more probably hypocoristie to a com- pound name ($164.П1; Bthl. AiW 1018) of which the prior part was the participial stem to the same compound verb (§162), ef. Av. adj. fradat.qaéa- ‘prospering the household’, sb. frddaj.fsav- ‘Pro- moter of flocks’ (name of a divinity; Bthl. AiW 1013-4). Not with Sen 52 (fra- + OP *ad- ‘drive’, Av. azaiti, Skt. djati, Lt. agit), nor with Justi, INB 101 (fra- + had- ‘sit’, with loss of intervocalic -h-). Fraéda nsm. DB 3.12; 4.23; ОВ] 1.
framatar- sb. ‘master, lord’ (‘giver of judicial decisions’, ace. to Hz. ApI 150-4): fra- + root mā- + agent suffix -tar- (5154.1). framatéram asm. (§124.VI, $1861) DNa 7f; DSe 7; DSf 5; DE 11; XPa 5; XPb 11; XPe 5; XPd 8; ХР? 7f; XPh 6; XE 11; XV 9; A'Pa 8°; A?He 7. frama- ібгат (852.111) A?Pa 8.
framána- sb. ‘command’ (judgment, deci- sion’, acc. to Hz. ApI 144-50): РЫ. framán, NPers.
OLD PERSIAN
fürmán; fra- + mä- + suffix -nà- ($128, $1471), ef. Skt. pramána-m ‘measure, standard’. — framánà nsf. DNa 57; DNb 28; DSj 3°, framánáyà isf. DNb 37.
fravata adv. ‘forward, downward’: Phl. frót, NPers. fáród јато; from *frava-, extension of fra- as in Gk. rpõros ‘first’ from *proya-, + -tos as in amata (§191.1I; JAOS 51.204, 53.15; Bv. BSLP 30.1.59; hardly with Kénig, Burgbau 51; not identical with Skt. isf. pravátà ‘downhill’). DSf 23f, 28.
Frovartz- sb. ‘Phraortes’, a Median rebel: Elam. pir-ru-mar-t-18, Akk. pa-ar-ti-mar-ti-1§ Gk. Ppadprys: identical either with Av. frava&i- ‘guar- dian angel, soul’, from fra- + var- ‘protect’ + -ti- (S31, 8152.11) as ‘Protection’, or with Av. fraoroti- "Siehbekennen zu’, from fra- + var- ‘choose (re- ligiously)’ + -й- (Bthl. AIW 991, 992, 976; Nyberg Rel. 334-5, prefers second view); as man’s name, probably liypocoristic of a longer compound ($164.1). — Fravarti$ пата. DB 2.14, 66, 71, 73; 4.18; DBe 1f. Fravartim asm. DB 2.17. Fravar- tas gsm. DB 2.69, 93.
fras- vb., see јтаб-.
fraša- adj. ‘excellent’ (‘tauglich’, König Burg- bau 48, Brd. АКМ 39.87): Av. frasa- ‘directed toward, useful’, formed on adv. fraša to frünk-, Skt. adv. praca to ртайс-, from pra- + añe- (Bthl. AiW 1006-7); the irregular -3- for -s- of Sy- may be a contamination of *frasa- and *frasya- (otherwise ВБ. IF 2,266-7; borrowed from Aves- tan aec. to Hz. ApI 162). Hz. ApI 156-65 (recant- ing derivation from fra- + záy- ‘shine’, ‘brilliant’, AMI 3.1-11) takes as deriv. of pra-, through an idiom of racing or fighting, as 'extra (certamen), hors (concours)’, and therefore "incomparable, su- preme’. Cf. also Hz. RHRel. 113.26; Bailey, BSOS 6.595-7; Kent, Lg. 15.169. — frasam nsn. DSa 5, DS] 6 (see frasta-, for reading). frasam asn. DNb 2; DSf 56, 56f; DSo 4^; DSs 1°.
frašta DSa 5, DS] 6: discussed by Bv. ВІР 30.1.63-4, Gr. $103, Gray AJP 53.67, Brd. WZKM 39.20-1; but fra$am @adaydlary and not frašta ðadayämaiy ($54.11) should be read in both pas- sages (Hz. AMI 3.9-10, ApI 156-8). See under frasa-.
(mu. em lere Am ee шшш. ште у. mi ease e +
LEXICON 199
fraharavam, phrasal adverb ($191.]II), ‘in all’: fra- ($1401) + asn. haravam with variant orthography ($22, $26), to haruva-. DB 1.17.
. baug- vb. ‘free’: Av. baog-, NPers. boxtén; in Attydbausna-, Bagabuxsa-.
Düxtri- sb. ‘Bactria’, a province of the Persian Empire: Elam. ba-ak-&-18, ba-ik-tur-ri-i$, Akk. ba-ah-tar, Gk. (nt. pl) Béxrpa (§9.1, $79, 6103.111). OP %-stem, for older 7-stem (8152.II), seen in Av. báxói. — Büziri$ nsf. DB 1.16; DPe 16; DNa 23; DSe 22°; D8m 9°; XPh 21. Ваг- triyd \sf. DB 3.13f, 21. Baztriya absf. DSf 36.
bag- vb., see under baga-, bàji-.
baga- sb. ‘god’: Av. baga- ‘lot, good fortune’, Skt. bhdga- ‘dispenser (of good fortune)’, Gk. -paryos ‘eater’, OCS bogi ‘god’, pIE *bhago- ($101, $122, 5143.1, V, VI); ef. Hz. ApI 105-10. See also Bagábigna-, Bagabuxsa-, Bagayddi-, bà. рада nsm. AmH 6; AsH 6; DNa 1; DNb 
=== leaf 223 ===
1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. ($10, $119, $172) DB 4.61, 63. bagünám gpm. AsH 7; DPd 1f; DPh 9; D8f 9; DSp 1°; DH 7; XE 2; XV 2; A’He 2. bagaibiš ipm. DPd 14f, 22, 24; DSe 50f°; DSt 8; XPb 28f; XPe 12f, 15; XPd 18; XPg 13f; XSc 5°; XV 26; A'Pa 23°. Вот ($42) ipm. D’8a 3. |
Bagábigna- sb. ‘Bagabigna’, a Persian, father of Hydarnes: Elam. ba-qa-pi-ig-na; from baga- ‘sod’ + d-bigna-, pte. in -na- of an unidentified verbal root, cf. perhaps Skt. bija-m ‘seed’ (575.1, $103.IV, $160.Ie, $243). Baglalbignah{ya} gsm. DB 4.84f.
Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithras, since Phl. and NPers. call this month Mihr
‘(Month of) Mithras’ (Justi, ZDMG 51.247; Bthl. AiW 952-3). Bágayádait gsm. DB 1.55.
bàji- sb. ‘tribute’: NPers. Баг; deriv. (§152.1, $165) of root seen in Skt. bhdga- ‘portion, dis- penser’, OP baga- ‘god’, the verb being Skt. bhájatt ‘apportions’, Av. bag-, РЫ. bäztän (§101, $122, $128, $126). Балт asf. DB 1.19; DPe 9; DNa 19; DSe 18; XPh 17.
batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devouring, drinking’ ($160.Ia), cf. Av. aspé.gard ‘horse-de- vouring’, Skt. aja-gará- ‘goat-swallower, boa con- strictor’, Gk. dnuo-Bédpos ‘people-devouring’, Lt. carni-vorus ‘flesh-eating’, from root in Av. gar- ‘devour’, Skt. girdit, Lt. vorat, plE *g*er-. Bv. J As. 228.233-4 suggests, and На. AMI 8.9-17, Ap! 118—5, accepts cognation rather with Skt. galati ‘drips’, gdlayat ‘pours’, as ‘wine-pourer’, cf. Lt. рате ‘pour (as an offering to the gods)’, and NPers. piyàüla ‘drinking cup’, from *pati-gdra-. bülugara пет. ($56.V) АЧ.
ba*d- vb. ‘hind’: Av. band-, Skt. bandh-, Gt. bindan, pIE *bhendh-. See also badaka-. basta (NPers. bäst) nsm. past pte. pass. (867, $85, 5120, $122, 5182.1, 52421) DB. 1.82; 2.75, 90; 5.26. basta apm. DB 3.88".
ba"daka- sb. ‘subject, servant’ (cf. König, Кыр 64): Phi. bandak, NPers. bändäh; deriv. (§146.1T) of OP *ba"da- ‘bond, fetter’, Av. banda-, Skt. bandhd-, to pIE root *bhendh- (OP ba"d-; $39, $75.11, $111, §122, 8132.1). badaka пет. DB 2.20, 30, 49f, 82; 3.13, 31, 56, 85; 5.8. badakā npf. DB 1.19.
Bábiru- sb. (Babairu- because of Pali Báveru-, MB Gr. $80) ‘Babylon’, a city (S56.III, $166); ‘Babylonia’, a province of the Persian Empire; by transfer, ‘Babylonian’: Elam. ba-pi-li, Akk. bab-ilu, bab-ilàni ‘gate of the god(s)’, Gk. Вав (§75.V, $107). See also Babirwiya-. Bahrus пет. DB 1.14, 80; DPe 10f; РМа 26; DSe 25; DSm 7°; XPh 22; as ethnic ($56.11), DN xvi, A?P 16. Babirum asm. DB 1.83f, 91 bis; 2.2, 3, 3f; 3.82, 84, 87; 4115, 30. \Babiraus absm. ($168, 6182.1) DB 2.65. Варта lsm. DB 1.78, 81;
200 OLD PERSIAN
2.5, 6; 3.79, 88, 92; 4.2; DBd 7f; DBi 11 (written Bab*raw, $22); DSf 33 as loc. with усій, 33 as abl. with Ласа (hardly a real abl., corresponding to Av. -aut despite Hz. AMI 3.55n, Kent ЈАО 53.16).
Bābirwiya- adj. ‘Babylonian’: deriv. ($144.- ПТ) to preceding. — Bábiruviya nsm. DB 1.77, 79; 8.81; 4.13; DSf 20. Babiruviyam asm. DB 3.86. Babiruviyé npm. DB 3.78; DSf 53f. Bäbiruviyä apm. DB 3.88.
bar- vb. ‘bear, lift up, esteem’: present stem bara-, Av. батат, N Pers. bard, Skt. bhárati, Gk. dpa, Lt. fert, Gt. batrip, pIE *bhere/o- (8213). See also ubarta-, uSabdri-, Gaubaruva-, bara-. bara^tiy 3d pl. ($122, 5232.1) DB 5.22f (written berety, 522); DNa 42. abaram Ist sg. imf. ($61, $75.III, 5226.1) DB 1.2
=== leaf 224 ===
2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54, 60, 68, 86, 97^; 3.6, 17, 37, 45, 62, 67 (written ar?r^, 854.11), 87; 4.61, 62; DNa 50f; DSf 19°, 32; XPh 33, 45. abara” 3d pl. imf. ($10, $40, $84, $106, 8232.1) DPe 10; DSe 18°; DSf 34. aba- raha” 3d pl. imf. ($10, $218, $282.11) DNa 19f; XPh 17 (written орт, §54.1). abara"tà 3d pl. imf. mid. ($10, $236.II) DB 1.19. abariya imf. pass. (535.1, $220, $228.IT) DSf 23°, 31f, 35, 36, 38f, 40, 48, 45. abariya" 3d pl. imf. pass. ($220, 8232.11) DSf 41, 47.  baratuv imv. (5237.П) AmH 11^; DPd 14; DSk 5. аталаш inf. ($238) DNb 41.
à + bar- ‘perform’: dbaratiy ($218, $228.1) DNb 25. Cf. also Hz. Ар] 110-1, who refers to à-bar- certain other forms listed above as augmented forms of uncompounded bar-.
pati- + à + bar- ‘bring back, restore’: райуй- baram Ist sg. imf. DB 1.68 (but -à- perhaps only by influence of pardbartam, JAOS 62.275; 558, $206c).
para + bar- ‘bear away, take-away’: pardbara imf. DB 1.71, 96. pardbartam nsn. past pte. pass. (§242.1) DB 1.62, 67f.
pari- + bar- ‘protect, preserve’ (cf. Hz. Ар 112-3): paribarümiy Ist sg. (8226.]) DNb 17. paribarühy 2d sg. subj. ($27, $136, §222.IT, 4227.1) DB 4.78; paribaráh*-di$ (827, etc.) DB 4.74. pari- barā 2d sg. imv. (5237.1) DB 4.72, 88.
fra- + bar- ‘proffer, grant’: frábara imf. AmH 7; AsH 9; DB 1.12, 25, 60; DPd 3f, 7f; DPh 8; DNa 33; DSf 11; DSm 3°; DSp 2°; D8s 6; DZc 4; DH 7; A’He 18f, 20.
bara- sb. ‘bearmg, bearer’: Av. -bara-, Skt. -bhara-, Gk. -фороѕ, pIE "bhoros ($32, $122, $1431, ҮТ), to root bar- ‘bear’, in aritibara-, takabara-, vacabara-; also bāra- ‘borne by, rider of’, with vriddhi (8122, $126, 5148.1), in asabdra-, ef, usabüri-. See Hz. Ар] 95.
bard- vb. ‘be high’: Ау, baraz- ‘high’, baraz- ant- ‘lofty’, NPers. burz ‘high’, Skt. brhánt- ‘lofty’, OHG berg ‘mountain’, pIE *bhergh-; in Bardiya-, barsan-, probably in brazman-.
Bardiya- sb. Smerdis’, brother of Cambyses ($16411): Elam. bir-h-ia, АКК. bar-zi-ia, Gk. Урёрӧ ($29.02, $30). Репу. (§144.1V) of OP bard- ‘be high’ (575.11): ‘The Exalted’. Bardiya пет. DB 1.30, 32, 39, 52f; 3.25, 35, 54; 4.9, 27, 82; DBb 4f; DBh 5. Bardiyam asm. DB 1.31 bis, 51.
barSan- sb. ‘height, depth’ (S81): Av. barazan- .
(ВМ. AiW 950); deriv. of OP bard- (575.1, $155.1; Scheil 21.26; Konig, Burgbau 51; Hz. AMI 3.57; Bv. Gr. $812; Kent, JAOS 51.204, 99.15). bar$nà ism. (806, $120) DSf 26, 26f.
bav- vb. ‘become, be’: present stem bava- (8213), Av. bavatti, Skt. bhdvati, Gk. ote ‘grows’, Lt. fut ‘I was’, Lith. butt ‘to be’, NEng. be, pIE *bheu-. See also büm:-. bavatiy (§122, §228.1) XPh 55, 56. bæa"ty 3d pl. ($232.1) DNb 14 (башайу in 2d copy, Hz. ApI 115; ef. $48). abavam Ist sg. imf. DB 1.28, 60, 72; 4.5; 5.4^; DSm 6°; XPf 35, 36f; XPh 30; XSe 4°. abava imf. ($228.IT) DB 1.32, 38, 34, 40, 48, 77, 80; 2.16f, 17, 80, 94; 3.10, 11, 20, 27, 28, 76, 82, 83; 5.5, M^, 30; DSf 25; XPf 26.  abava^ 3d pl. imf. ($112, $232.IT) DB 1.76; 2.7, 93; 3.78; 4.34. bavātiy sub). ($222.11, §228.1) DNa 43, 45f; DNb 59 (Lg. 15.74; confirmed by photograph, JNES 444). [biyjä 2d sg. opt. ($114, $218.11, $223.I, $227.11) DB 4.69. буй opt. Cbhy-net, Bv. Gr. $232, comparing Av. buyd{ from *bhu-iët; but ВЫ. Gdr. IP 1. $143 takes as *bhy-i48t, = Lt. fiet, which may be either non-thematie opt. or thematic subj.; $114, $122, 5208, $218.II, §223.1, $228. ID) DB 4.56 bis, 58, 59, 741, 75, 78f, 79°.
bigna-, in d-bigna-, see Bagabigna-.
biimi- sb. ‘earth (= world or ground)’: Av. bümi-, NPers. büm, Skt. (RV) nom. bháümi bhümis; deriv. of root bhav- (see bav-) in grade bhi-, cf. Skt. aor. ábhüt, Gk. ёфо ($11, $65, §152.1V, §179.- IIT).
LEXICON
bümim asf. DNa 2, 32; DSe 2°; DSf 1; DSt 2; DZe 1f; DE 2; XPa 1; XPb 2; XPc 1; XPd 2; XPf 2; ХР 1f; ХЕ 3; XV 2f; A!Pa 2^; A?He 2. ратат, asf. ($55.1) A3Pa 2. bümiyà sf. (8179.IT) DNa 11f; DSb 9; DSe 10; Рб 5; DSs 2°, 3°; DZb 4; DZe 6; DE 17f; XPa 9; XPb 17; XPe 7f; XPd 12; XPf 12, 25; XPh 10; ХР); XE 17; XV 13; A'Pa 18°; A?8e 4°; Wb 7; Wc 8; Wd 8.
BU nsf. ($42) DSf 24, 28. 
=== leaf 225 ===
BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11.
brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhratar-, Gk. @parnp ‘clan-brother’, Lt. frater, OCS bratru, Gt. brobar, pIE *bhráter- (862, 875.111, $128, $154.П). баі nsm. ($124.5, 5186.1) DB 1.29f, 39f.
brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with braz- rather than barz- (883; cf. Elam. pir-ra-us-man-ni-ia, АКК. bi-ra- 2a-man-ni-1): deriv. (§144.IV) to pAr. antecedent of Skt. bráhman- ‘religious devotion, prayer’, ef. identical Skt. deriv. brahmanyd- ‘religious’, to pIE root *bhergh- (see OP bard-; $75.1II, §95, $120, 5155.11; Henning, TPS 1944.108-18). For other views, see Kent, Lg. 13.301; Hartmann, OLZ 40.145-60; Nyberg, Rel. 367, 478; Hz. AMI 8.69, Apl 116-8 (to Av. barag- ‘to welcome’, barag- ‘rite’, Бәтәгба- ‘beloved’; wrongly, since this would give OP *bragman-); Christensen, Essai sur la démonologie iranienne 40-1; Henning, BSOS 10.506; Abayev, Iranskie Yazyki 1.134; Scherman, JAOS 65.141-3 n.23. Cf. also О. M. Dalton, Treasure of the Oxus 94-5. On form and meaning of РЫ. brahm brahmak, see Henning, TPS 1944. 108-18. brazmaniya nsm. ХР 41, 51, 54 (hardly brazmaniy isn. modifying arid; also not -niy apn. ‘divine’ with Sen 155, nor adn. in elliptic dual with Pisani, see under aria-).
т°, of dubious meaning, Se 1; taken by Justi, IFA 17.112, to be an abbreviation for OP *méraka ‘seal’, NPers. maráh.
та-, stem of ist person pron. in obl. cases of sg.; see adam.
mà conj. ‘not’, in prohibitions ete.: Av. Skt. mà, Gk. шӯ, pIE *mé ($109, §191.1, §292b). With subj.: DNb 55 (mé-taty), 58. With opt.: DB 4.59, 69, 79°; DPd 18, 19 bis, 20; XPh 39. With
201
inj.: DB 4.54; DPe 21; DNa 58, 59, 60; DNb 52 (mà-lay). With imv.: DNb 60. With lost verbs: DNb 57, DSq 4 bis; with restored subj. A'Sa 5^ bis, A?Ha 7, 7°. See also mdtya.
mā- vb. ‘measure’: Av. Skt. ma-, Lt. métior ‘I measure’. à + må- ‘extend’: атӣій npm. past ptc. pass. (6242. П) ‘noble’ DB 1.7; DBa 11. fra- + mā- ‘command’ (‘decide, judge’, acc. to Hz. ApI 154-6; ‘plan,’ Hinz, ZDMG 95.233-5); see also framülar-, framdnd-. јтатауаіа imf. mid. ($214, 5285.11) XPg 5. framatam nsn. past pte. pass. ($242.IT) DSf 19f°, 56.
таш- vb. ‘flee’: meaning established by Мат. and АКК. versions (Hüsing, KZ 38.258); probably to Skt. munthate ‘flees’ (Jn. JAOS 38.122). атида imf. ($211) DB 2.2, 71; 3.41f, 71.
Maka- sb. ‘Maka’, a province of the Persian Empire (lit. on location given in JAOS 56.217-8): Elam. ma-ak-qa, АКК. ma-ak, cf. Gk. pl. Мака ($99, $1322, SI4LITD. See also Mactya-. Maka nsm. DB 1.17; DPe 18.
magu- sb. ‘Magian’, member of a priestly order of Media: Flam. ma-ku-i3, АКК. ma-qu-&u, Gk. Méyos ($153.1). Uncertain material on mean- ing and etymology, Kónig, Klotho 4 chap. 12, and RulD 66. magus nsm. DB 1.36, 44, 46, 64, 66, 101; 4.8; DBb 2. magum asm. DB 1.50, 54, 57, 73; 4.81.
Maciya- adj. ‘Macian’; pl., name of a prov- ince of the Persian Empire: deriv. of Maka- ($99, $113, 8132.2, $144.01). Maciya пет. A?P 29. Масту for nsm. (856.11) DN xxix. Macy npm. DNa 30; DSe 230; XPh 25.
madtar- sb. ‘mother’: Av. matar-, Skt. matdr-, Gk. Dor. ратар, Lt. mäter, pIE nom. *maté, stem *máler- ($154.П): in hamdtar-.
таша conj. ‘lest, that not, not’: mà ‘not’ + conj. tya (§133, 4292р).  matya-mam (5133) DB 1.52. тайа DB 4.43, 48, 71.
mabista- adj. ‘greatest’, equal to ‘crown prince’ in XPf (Speiser ap. Kent, Lg. 9.40-1; Hz. Apl 254-8): Av. masista-, NPers. mähist, Gk. ppxio ros ‘longest’ (radical vowel after that in anxos Jength"); superl. to pIE *mak-ros, Gk. накр, Lt. macer ‘thin’, pLE root *mak- (887) ‘be long and slender’ + superl.,suffix.<ste-) (S117, $156.11,
202 OLD PERSIAN
4190.1), Gk. -сто-, Av. -tšta-, Skt. (with aspira- tion) -gha-. таб: а пет. AsH 6; DB 2.13,
```


## [2026-09-07T18:19:12.695Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=189 && NR<=191 {print \"=== leaf \" NR-1 \" ===\"; print}' KNT.txt | head -40"
}
```


## [2026-09-07T18:19:13.586Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'asem\\|asēm\\|sim ‘silver\\|silver' KNT.txt | head -30"
}
```


### [2026-09-07T18:19:13.921Z] TOOL RESULT

```
=== leaf 188 ===
’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
OLD PERSIAN
grance’, therefore ‘having the fragrance of the truth’).  <Aé@iydbausinahya gsm. Sa 4-7.
Aéura sb. ‘Assyria (and Syria)’, a province of the Persian Empire ($6, $106.11): Elam. aš- &i-ra, АКК. áš-šur, Gk. 'Аттурв‚ but Aram. абиг. Aéuré nsf. DB 1.14f; 2.7; DPe 11; DNa 26f; DSe 26°; DSm 7°; XPh 22. Aéurayd lsf. (5186) DB 2.58f.
A@uriya- adj. ‘Assyrian’: deriv. to preceding .
($144.1), perhaps with vriddhi in first syllable (8126; Aburiya- ?). A@uriya пет. DN xvii; DSf 32; А?Р 17.
Agina- sb. ‘Acina’, ап Elamite rebel: Elam. ka-iš-ši-na, Akk. a-Si-na. Either borrowed from Elam. (Foy, KZ 37.498); or shortened from an IE name beginning with OP äç- = Av. átar- 007- ‘fire’ ($147.11, §152.1), ef. atoro-dáta- ‘Fire-given or Fire-created’ and other names (Vd. 18.52; Justi, INB 50; Bthl. AiW 324). Agina пет. DB. 1.74, 82: 4.10; DBe 1f. Acinam asm. DB 1.76.
Ld
A ciyádiya- adj. ‘Aciyadiya’, the ninth month, .
Nov.-Dec.: Elam. haššiyatiyaš, АКК. kislimu, Cpd. of átar- ‘Are’ + deriv. of yad- ‘worship’ ($126; $152.D: ‘Fire-Worship Month’. Agiyddiyahya gsm. DB 1.89; 3.18.
ada- adv. ‘then’: GAv. ald, LAv. ада, Skt. .
ба ‘therefore’ cf. Gk. трбе-бє (and -Gev) ^n front of’: pIE *e-dhe, to root in *a- ($76.11; $191.II); see also adakaty. — ada-taiy DNa 48, 45.
adakaiy adv. ‘then’: OP ada- + -kazy, Gk. aly. то ‘somewhere’, pIE *q¥ei, Isn. to int.-indef. stem ($135). DB 2.11, 24; 4.81, 82; DNb 38.
adam pron. “Р: Av. azam, Skt. adm, plE .
*eühom ($109), ef. pIE *ейб in Gk. yo, Lt. ego (8193.1). adam nsm. AmH 5,8; AsH 14; CMa 1; DB 1.1, 10, 12, 39, 52, 54 bis, 56, 59, 60, 62, 63, 64, 66, 67, 68 bis, 70, 72, 73, 75, 18, 82, 83, 86, 89, 91, 95; 23, 5, 6, 10°, 11, 15°, 19, 28, 30, 48, 50, 68, 64, 69, 72, 80, 81, 88; 3.1, 13, 25, 29, 50, 77, 80, 84; 48, 8, 11°, 14, 16, 19, 21, 24, 27, 29, 32, 40, 45, 59, 64, 71, 81, 89; 5.2, 6f, 13, 21°, 23°, 25°; DBa 1, 16; DBb 4, 6; DBe 5; DBd 3, 6; DBe 5, 8; DBf 3f; рве 5; DBh 4f, 8; ОВ: 4, 9; ОВ] 4; DPd 20; DPe 1, 7; DPh 4; DNa 8, 17, 34, 37, 531; DSa 1, 4; DSb 1; DSe; DSd 1°; DSe 7f, 16°, 34, 44°; DSf 5, 18°, 21°; D8g 1, 3°; DSi 1; DSj 1°, 2°. DSk 1, 4; DSm 1°, 6°; DSy 1; DZe 4, 7, 8, 11;
LEXICON
DE 11; DH 3f; XPa 6, 13, 14; XPb 11; XPe 6; XPd 8, 17; XP£ 8, 34f, 36, 39, 41; XPg 9; XPh 6f, 15, 29, 34, 37, 40, 421, 43, 50; ХР] bis; XSe 1°, 3°, 4°, XE 12; XV 9, 23; A!Pa 9°, 21°; D'8b 1°, 4°; A'Sa 4; A’Sb; A'8d 1, 3; A?Ha 5°; A’He 9, 16; Азра 11f; Wa 2; Wb 1; We 2; Wd 2; SDa; SDb; SXb 1; SXe 1. adam-áaty DB 2.731. айат-йт (839) DB 1.62, 83; 4.6; DNa 35. adam-sam DB 1.14; DNa 18; DSe 17 adam-[$am]; XPh 16.
mam asm. (Av. mam, Skt. mdm, рЕ *me + acc. -m; 5193.11) AsH 7, 11; DB 1.52 (métya-mam, $133), 82f, 93°; 2.18, 28, 48, 63, 67, 73, 88; 3.30; 4.35, 91; 5.13, 17, 26, 28°, 29°, 33; DPh 9; DNa 33, 31,51; ОХЬ 11, 22, 26, 46, 49; DSe 50°; DSf 9, 10, 14f, 17 bis, 57; DSi 3°; DSj 4, 6°; Рб 4°; DSs 6; DSt 7°; DZe 12; DH 71; XPa 18; XPb 27; XPe 12; XPd 17; XPf 31, 45; XPg 12; XPh 57; X8e 4°. XV 25; A!Pa 22°; A’Sa 5^; A’Sd 4; A?Ha 6; A?Hb?; A?Hc 19; A?Pa 5, 23, 24; 224, 26 ({56.У; for mand ?).
-mā asm. епс]. (Av. md, Skt. md, pIE *mé, 6193.1; cf. enel. *me in Gk. pe): nai-mā ОМ 8 (na[ima]), 10, 19; nai-pati-ma ОМ 20.
mand gsm. (Av. mana, Skt. máma, pAr. *mana, cf. Lith. mano; $193.11T) AmH 6, 10; AsH 9; DB 1.4, 9, 12, 18, 18, 19 bis, 28, 27, 60; 2.19f, 21, 25, 27, 29f, 31, 35, 40, 46, 49, 51, 55, 601, 82, 84, 87, 91f, 93; 3.0f, 10, 13, 15, 17, 20, 20f, 31, 32, 38, 45, 53, 56, 62, 67, 75f, 76, 84, 86; 4.2, 12, 35, 42, 49, 52, 531, 66, 821; 5.8, 14°, 30; Ва 5, 14£; DPd 7, 13; DPe 9; DNa 19, 21, 33; DNb 56°; DSe 18°, 20°, 38; DSf 12, 13, 58; DS} 5°; DSk 4; DSs 6°; XPa 19; XPb 23; XPe 11; XPf 16, 23, 31, 46; XPg 7; XPh 17, 19; Ха 2; XV 18; A!Pa 20°; D'Sb 4^; A’He 18.  mana-eá (8135) DPd 9f.
-maiy gsm. (gen.-dat. GAv. mót, LAv. mé, Skt. me, Gk. dat. но, pIE *mot) enclitic to айа (ns
=== leaf 189 ===
n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-; ucdram; uld, uta-; tya (nsn., asn.); dahydus; duvarayd; nat-; pati-; pasdva; уава; haw, hau-: Asl 12; DB 1.25 bis, 55, 87, 94; 2.24, 34, 40, 45, 54, 60, 68, 75, 79, 86, 90, 96; 3.6, 11, 17, 37, 441, 61, G6f, 87; 4.39, 46, 60, 64; DPd 28°; DPh 8, 10; DNa 50 (m° omitted, $52.VI), 52#, 544; DNb 13, 28, 28f, 31, 32f, 33, 48, 51, 52; DSe 51°, 52°; DSE 10, 19°, 20°, 58; Ds} 4°, 6°; DSk 5; DSI 4f; DSm 3°; D8s 7°; DSt 9°; DH 6, 8; Хра 15, 18f, 191; XPb 24, 29, 30; XPe 13 bis; ХРа 18f, 19; ХР 32, 38, 41, 45f, 47; XPg 14; XPh 32, 45, 58,
167
60; Хе 5° bis; XV 261°, 27°; A!Pa 23°, 24°: A’Sdb 4 (-may de, $52. VT); А?Не 20 bis.
-ma gsm. for -maty ($198.11); apan*yáka-ma А?За 3; [n"yà |kama for n*yàkam-ma (5130) A’Sa 4. Not kamna-ma DB 2.19, as taken by Tolman.
-ma absm. enel. (Av. maf, Skt. mat, pIE *med, $193.IV; orthotone pIE *méd in oLt. méd, elLt. mē); only in hacd-ma DB 1.19, 23; 2.6, 12°, 16, 98; 3.27, 78, 81; 4.92; DPe 9; DNa 20; DSe 19°; XPh 18. Not duviliya-ma DB 3.24 (with Bthl.); not apara-ma DB 4.37, 68, 87 (with Bthl.), nor DSt 10°.
vayam npm. (Av. vaém, Skt. vaydm, рї Е *uei + pAr. -am, cf. Gt. wei-s; §193.V) DB 1.7, 10°; DBa 10, 17.
amazam gpm. (Ау. ahmakem, Skt. asmákam; $118.11, §193.VI) DB 1.8, 28, 45, 49, 61, 69, 71; DBa 12.
Adukanaisa- adj. ‘Adukanaisha’ , first month, March-April: Elam. ha-du-kan-na-1§, АКК. nisannu: -natsa- on the evidence of the Elam., acc. to MB Or. $96, rather than -nisa- ($117). Cpd. of adu- ^ + kan- ‘dig’, possibly with vriddhi ($126; Adu- ?): "Irrigation-Canal-Cleaning Month’, re- ferring to the cleaning of the underground con- duits for irrigation water, regularly done in the spring (cf. РЕШ. AiW 61). Adukalnaz]Sahya gsm. DB 2.69.
an- neg. prefix before vowels, ef. !a- before consonants: Ау. Skt. an-, Gk. &»-, Lt. in-, Gt. un-, pIE *on- (867.1); in Anáhatà-.
and ism. to ?a- (q.v.); DPe 8 (not to Av. Skt. ana-); XPa 14 (not prep.).
Anàümaka- adj. ‘Anamaka’, tenth month, Dec.-Jan.: Elam. handémakas, АКК. febétu. Cpd. of neg. a- + ndma- ‘name’ (see ndman-) + adj. suffix -ka- ($146.11), possibly with vriddhi (8126; Anámaka- ?): ‘Month of the Nameless (= High- est) God’. Anàmakahya gsm. DB 1.96; 2.26, 56; 3.63.
Andhita- sb. ‘Anahita, Anaitis’, a goddess: Elam. a-na-hi-ud-da, Akk. a-na-ah-t-tu-’, Gk. ’Avairs; Av. andhitd-. Cpd. of neg. an- + pte. pass. dhita- ‘spotted, defiled’, of uncertain connec- tions (§67.J, §118.V, §242.1): ‘The Spotless’. The OP writings, being late, fail to show length of б in either position. Anahita (827, $52.11) nsf. A’Sd 3f; Anah*ta, A’Sa 4 (as gen., §313.11), 4f; A?Ha 5° (as gen.), б.
4
168
antya- adj. ‘the one or the other (of two), other (of any number), rest of’ (JNES 3.2334; not ‘enemy’, cf. Kent, JAOS 35.345.n6 and Bv. TPS 1945.56-9): Av. ainya-, Skt. anyd-, pIE *anjo-, cf. *аЦо- in Gk. ados, Lt. alius, and *an- tero- in Gt. anpara-, Gm. ander, NEng. other (889, 144.1, $204.17; decl, $203). aniya nsm. DB 1.95; 3.32; DSe 33°, 35. aniyam asm. DB 1.86; 0.25, 28; DSe 33, 35f. aniyahyd gsm. DB 1.87. aniyanā absm. DPd 11; DPe 20f. aniyai-ciy npm. XPf 29. aniyaha npm. ($10, $172) DB 4.61, 62f. aniyä nsf. ПЕ 25, 26 (not with Bv. Gr. $834, inst. as adv. ‘on one side ... on the other). aniyām asf. DSe 48f. aniya прі. DB 1.41. aniyüapf.DB 1.47, 67. aniyāwvä lpf. ($72) DB 1.35. aniya asn. XPf 39. aniyaš-ciy nsn. (§9.VI, 8105) DB 4.46; XPa 13; ХР 41f (written antyase*, §52.1).
an|iya|éa adv. ‘in other ways’ ($191.17); Cam- eron's interpretation for his reading але ++ wms, DB 4.89.
атш) (ie. anu) prep. ‘along, according to’: Av. anu with acc., loc., ‘toward, along’, Skt. ánu with acc. ‘after, along’; see also anuSiya-. (1) With inst., DB 1.92; DNb 25 (ef. Lg. 15.176). (2) With gen., DNb 16, 18 ($137, $267.IV ; anu-dim + gen.).
```


### [2026-09-07T18:19:13.964Z] TOOL RESULT

```
581:ardata- ‘silver’, Av. srezata-; Yezdi ali ‘silver’, from earlier ard-, is not necessarily evidence for OP, since Yezdi is a Kurdish dialect; Skt. rajatd- also has a different initial.
1170:pIE *rjnto-, OP ardala- ‘silver’, Av. orozata-, Lt. argentum, c£. Skt. rajaldn.
1798:$45. NOUN AND ADJECTIVE STEMS WITH SUF- prx. -ta- found in OP are mostly participles ($242), superlatives (8190.1), and ordinal numerals (8204). The remaining examples are aruvasta-, a neuter abstract seemingly formed upon an adjec- tive *aryani- (see Lex. s.v.); XSaérita-, а hypo- corstie to a compound personal name; ardata- ‘silver’, perhaps an -a- extension of a participle in -ni-, cf. Lat. arg-ent-um; dasta- ‘hand’, which can- not be related to any simpler extant root; and three feminine abstracts arsid-, hanalü-, avaslá-, the last two of which are dubious and the third is taken as having acquired concrete meaning.
3316:DPh = Darius, PEnsEPOUIS н: Trilingual, on two gold and two silver plates; now in Teheran. OP 10 lines, Elam. 7, Akk. 8; same text as DH. New York Times, Feb. 9, 1986, 2d news section, page 8; Univ. of Chicago Mag. 284.235, Feb. 1936; Hz. ApI 18-9 No. 6 and Plate 6 (1938).
3356:DH = Darius, HAMADAN: Trilingual, in dupli- cate on a gold and a silver plate; now in Teheran. OP 8 lines, Elam. 7 lines, АКК. 8 lines. The two copies vary slightly in the line-division; our text follows the gold plate. The text is repeated in DPh. JMUnwalla, Jame Jamshed, Sept. 30, 1926; Hz. DLZ 47.2105-8 (Oct. 16, 1926); SSmith, JRAS 1926.433-6; CDBuck, Lg. 3.1-5 (1927); LHGray, JRAS 1927.97-101; JMUn- walla, JCOI 10.1-3 (1927); Wb. 2А 37291-4 (1927); ESchwentner, ZH 6.171-3 (1928); Hz. Memoirs of the Archaeological Survey of India
3381:XH = Xerxes, HaMADAN: OP only, in one line, on a fragment of a silver pitcher. Hz. AMI 2.115-6 (1930); Brd. WZKM 39.83 (1932); Hz. ApI 43 No. 19 (1938); Sen, OPI 161 (1941).
3385:A'I = Artaxerxes I, iNCERTO Loco: OP only, in one line, identical inscription on four silver dishes. Hz. AMI 7.1-8 and 4 Plates (1935); Schaeder, SbPAW 1935.489-96; Hz. AMI 8.6-17, 46-51 (1937); Ву. JAs. 228.233-4 (1936); Kent, JAOS 56.215 (1986), 58.327 (1988); Hz. Ар] 46 No. 23 (1938); Sen, OPT 178 (1941).
4296:{81. 40-5. The silver and the ebony were brought from Egypt. The ornamentation with which the wall was adorned, that from Ionia was brought. The ivory whieh was wrought here, was brought from Ethiopia and from Sind and from Arachosia.
4677:TRANSLATION OF АЧ: Artaxerxes the Great King, King of Kings, King of Countries, son of Xerxes the King, of Xerxes (who was) son of Darius the King; in whose royal house this silver saucer was made.
5068:ardata- sb. ‘silver’: Av. arazata-, Skt. rajatá-, cf. Gk. &pyvpos, Lt. argentum. (S30, §88, $145); Yezdi ait ‘silver’ has Iran. ar-, not r- (Ву. BSLP 30.1.60, Origines 12). See also ardastdna-. arda- tam nsn. DSf 40.
5069:ardastāna- sb. ‘window-frame, window cor- nice’: arda- ‘light’ as in OP ardata- ‘silver’, Skt. rajatd- ‘white’, rjrá- ‘red’, Gk. àpyós ‘shining’ + stāna- ‘place’ (831, §160.Ib; Foy, KZ 35.48; hardly as with Bthl. AiW 193, or Hz. Ар! 74-6); ‘light- place’. ardasténa nsm. DPc.
```


## [2026-09-07T18:19:24.479Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^209$\\|  209  \\| 209$\" KNT.txt | head; awk 'BEGIN{RS=\"\\f\"} /(^|[^0-9])209([^0-9]|$)/ {print \"LEAF \" NR-1}' KNT.txt | head -20"
}
```


### [2026-09-07T18:19:25.717Z] TOOL RESULT

```
LEAF 8
LEAF 87
LEAF 89
LEAF 124
LEAF 195
LEAF 199
LEAF 211
LEAF 212
LEAF 221
```


## [2026-09-07T18:19:30.156Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=230 && NR<=234 {print \"=== leaf \" NR-1 \" ===\"; print substr($0,1,3000)}' KNT.txt"
}
```


### [2026-09-07T18:19:31.485Z] TOOL RESULT

```
=== leaf 229 ===
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39.
lwadé- conj. ‘where’: GAv yada, Skt. yada; probably rel. nt. pAr. #00 + postpos. 4. уайд- tya XPh 35f ($133, $296; cf. yaa tya ХР 29); yadàyà XPh 39 (perhaps error in writing, §55.1; but ef. Hz. AMI 8.66, ApI 358, Nyberg Rel. 477-8).
*Yadd- sb. ‘Yada’, probably ‘Anshan’ (as shown by the Elam. translation 3.3 an-za-an.mar, read by Cameron; cf. §166.n2): not an abstract yadà- ‘loyalty’ to root yad- (q.v.), as commonly taken (wrongly also Foy; KZ 35.43; Hüsing, ОГЛ
Ы
LEXICON | 205
8.513-6; Hz. ApI 244-9; Nyberg, Rel. 477-8). Yadayd absf. ($141, $175) DB 3.26.
yadiy conj. ^if, when’: Av. yetéi, Skt. yddi: per- haps pAr. nt. rel. *iad + deietic 4. Syntax $297. (1) Sf, with subj.: DB 4.38f, 54, 57, 721, 77; DPe 19, 22; DNa 38 (yadi-patiy), DNb 29 (yadi- và; cf. Hz. ApI 359); XPh 47 (yadi-maniyáty; 841, $92. VI); with opt., DNb 20f; with pres. ind., ОХЬ 25 (yadi-và). (2) ‘when’, with imf. ind., DB 1.38, DSf 11; ‘whenever’, with pres. ind., DNb 38f, 39.
yàna- sb. ‘favor, boon’: Av. yand-; deriv. of
‚ yam-, probably *ya- from *m-, with lengthening
and suffix -na- (5147.1). yànam asm. DPd 21, 23°; XSe 4°.
yaniy соп]. ‘where, whereon’: lsn. *ya^mi (= Skt. ydsmi-n, Av. yahmy-a ‘where’) to relative stem ya-, with -n- after isn. *yand, cf. isn. lyand to tya- (hardly yanazy, loc. formed on stem yana- extracted from isn. *yand, as taken by Bthl. Ат 1262; not miswritten for tyanaty, as taken by Müller, WZKM 7.112; other theories in Tm. Lex. 120 s.v.). Syntax $296. XV 22.
yam- vb. ‘stretch, reach out’: Av. yam- pres. yasaiti, Skt. yam-, pres. ydechati, OP pres. yasa-, pIE *im-ske-. See also уйпа-.
а + yam- ‘reach out for, (mid.) take as one's own’: ãyasatā imf. mid. (§97, $215, $235.IT) DB 147; 34, 49f.
ай- + yam- ‘reach beyond, present, read aloud to’: [аја] уа (823.T, $140.IIT, $220) imf. pass. DB 4.91 (conj. of Kent, JAOS 62.268; for -i-, ef. niyasaya, below).
ni- + yam- ‘reach out and down; (caus.) set down’: niyasaya imf. caus. (823.I, $140.IIT, $215) DNb 5, 46, 49 (In. JAOS 38.123-4; MB Gr. $199; Johnson, Gr. $4780; Hz. ApI 359-61).
уйа con]. ‘as long as’, isn. of *ydva-, exten- sion of pIE rel. */o-, pAr. *ia-, cf. Skt. ydvat, Av. yavala, Gk. dos (from *ayos); hardly from* yàva! à = GAv. (Ys. 43.8) yavat à, with contraction (Wackernagel, KZ 46.275-80). With subj. to show future time ($208): DB 4.71, 74, 78; 5.19, 35°.
raucah- sb. ‘day’: Av. raocah- ‘light’, Phi. rüé, NPers. róz, Skt. rócas- ‘light’, pIE *leugos ($70, $107, $156.ID, ef. Gk. Xexó-s adj. ‘ight’. тамса nsn. ($119, $1851) DB 3.8. rauca-pati-và
(899, $133) asn. DB 1.20.
=== leaf 230 ===
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $148.11), see urata-.
Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. $192.
ava- + rad- ‘leave, abandon’: avarada 2d sg. inj. (5213, $224, $227.11, $237) РМа 60.
?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
rādiy postpos. ($133) ‘on account of’, with gen.: NPers. тё, enel. postpos. as in &-rà ‘why’, also particle of various uses, often affixed to direct object for elarity; also OCS radi, postpos. with gen., “оп account of’; 10е, sgoof räd- (5188111), io root in Ski. radh- ‘effect; complete! (not to
206
"rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; DNb 9, 10f; also in avahyarádiy, q.v.
ram- vb. ‘be at peace’, with prefix d, in Arüjyüramna-, q.v.
rasa- present stem of vb., see ar-.
rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
‚ .. rlaryary, see vart-.
Labandna- (or Labnàna-) sb. ‘Lebanon’ (§6, §107), 2 mountain in Syria famous for its cedars. Labanéna nsm. DSf 31.
-vä encl. conj. ‘or’ (8133, $291.1
=== leaf 231 ===
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-07T18:19:37.007Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=233 && NR<=236 {print \"=== leaf \" NR-1 \" ===\"; print}' KNT.txt"
}
```


### [2026-09-07T18:19:38.291Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T18:19:41.478Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} END{print NR}' KNT.txt; awk 'BEGIN{RS=\"\\f\"} NR>=231 {print \"=== leaf \" NR-1 \" ===\"; print}' KNT.txt"
}
```


### [2026-09-07T18:19:43.394Z] TOOL RESULT

```
232
=== leaf 230 ===
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $148.11), see urata-.
Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. $192.
ava- + rad- ‘leave, abandon’: avarada 2d sg. inj. (5213, $224, $227.11, $237) РМа 60.
?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
rādiy postpos. ($133) ‘on account of’, with gen.: NPers. тё, enel. postpos. as in &-rà ‘why’, also particle of various uses, often affixed to direct object for elarity; also OCS radi, postpos. with gen., “оп account of’; 10е, sgoof räd- (5188111), io root in Ski. radh- ‘effect; complete! (not to
206
"rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; DNb 9, 10f; also in avahyarádiy, q.v.
ram- vb. ‘be at peace’, with prefix d, in Arüjyüramna-, q.v.
rasa- present stem of vb., see ar-.
rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
‚ .. rlaryary, see vart-.
Labandna- (or Labnàna-) sb. ‘Lebanon’ (§6, §107), 2 mountain in Syria famous for its cedars. Labanéna nsm. DSf 31.
-vä encl. conj. ‘or’ (8133, $291.1
=== leaf 231 ===
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-07T18:20:12.544Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD ne ===\" && grep -n -i \"^ne\\b\\|ne-\\. Not\\|nes-\\. \\|Not\\. \" AHD_watkins1985.txt | head -20 && echo \"--- AHD grep ne. no, not ---\" && grep -n \"no, not\" AHD_watkins1985.txt | head -20 && echo \"=== AHD nes ===\" && grep -n -i \"unsara\\|nes-2\\|nes-\\.\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T18:20:12.619Z] TOOL RESULT

```
=== AHD ne ===
102:The comparative study of Indo-European poetics has shown that such compounds were considered particularly apt for elevated, for- mal styles of discourse; they are a salient characteristic especially of Indo-European poetic language. In addition, it is amply clear that in Indo-European society the names of individual persons—at least in the priestly and ruling (or warrior) classes—were formed by such two-member compounds. Greek names like Sophocles, “famed for wisdom,” Celtic names like Vercingetorix, “warrior- king,” Slavic names like Wenceslas, “having greater gory,” Old Persian names like Xerxes, “ruling men,” Germanic names like Bertram, “bright raven,” are all compounds. The type goes as far back as Proto-Indo-Huropean, even if the individual names do not. English family names continue the same tradition with such types as Cartwright and Shake- speare, as do those of other languages, like Irish (O’)Toole, “‘people’s valor.”
774:ne. Not. 1. Germanic *ne-, *na- in: a. Old English ne (> Middle English ne), not, and nd, no: NAUGHT, (NAUGHTY), NEITHER, NEVER, NILL, NO!, NO2, NONE, (NoR!), NOT, NOTHING; b. Old Norse ne, not: NAY; c. Old High German ne, ni, not: NIx?. 2. Latin ne-, not, and nullus, none (ne- + illus, any; see oi-no-): ANNUL, NEFARIOUS, NESCIENCE, NEUTER, (NICE), NISI, NULL, NULLIFY, NULLIPARA. 3. Latin nimis, too much, exces-
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
1140:for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< “rolling or bubbling water,” “spring”): WELL; b. Old High German waillén, to roam: GABERDINE. 6. Perhaps suffixed o-grade form *wol-d- in Germanic *walé in: a. Old English walu, streak on the skin, weal, welt: WALE; b. Old High German *-walu, a roll, round stem, in *wurzwalu, rootstock (see wrad-). 7. Extended form *welw- in: a. Germanic *walw6n in Old English wealwian, to roll (in mud): WALLOW; b. Latin volvere, to roll: VAULT!, VAULT2, (VOLT2), VOLUBLE, VOLUME, VO- LUTE, VOLUTIN, VOLVOX, VOUSSOIR; CIRCUMVOLVE, CON- VOLVE, DEVOLVE, EVOLVE, INVOLVE, OBVOLUTE, REVOLVE; C. suffixed o-grade form *wolw-d- in Latin vulva, volva, covering, womb: VOLVA, VULVA; d. suffixed zero-grade form *wlw-d- in Latin valva, leaf of a door (< “that which turns”): VALVE; e. suffixed form *welu-tro- in Greek elutron, sheath, cover: ELYTRON. 8. Suffixed form *wel-n- in Greek eilein (< *welnein), to turn: ILEUS; NEURILEMMA. 9. Perhaps variant *wall- in Latin vallés, vallis, valley (< “that which is surrounded by hills”): VAIL!, VALE!, VALLEY. 10. Suffixed form *wel-end, possi- bly identical with the Greek name Helené (earliest form Welend), Helen, in Greek helenion, elecampane: ELECAM- PANE, INULIN. 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. 12. Suffixed form *wel-mi-nth- in Greek helmis, helmins (stem helminth-), parasitic worm:
--- AHD grep ne. no, not ---
=== AHD nes ===
784:nes-2, Oblique cases of the personal pronoun of the first person plural. For the nominative see we-. 1. Zero-grade form *ns- in Germanic *uns in Old English ds, us (accu- sative): Us. 2. Suffixed (possessive) zero-grade form *ns-ero- in Germanic *unsara- in Old English dser, ire, our: OUR, OURS. 3. O-grade form *nos-, with suffixed (possessive) form *nos-t(e)ro-, in Latin nds, we, and noster, our: NOSTRUM; PATERNOSTER. [Pok. 3. ne- 758.] nétr-. Snake. Germanic *néthré- in Old English nédre, snake: ADDER. [Pok. né-tr- 767.]
1124:we-. We. For oblique cases of the pronoun see nes-2, Suffixed variant form *wei-es in Germanic *wiz in Old English wé, we, we: we. [Pok. ué- 1114.]
1936:NOSH ghen- NOSTALGIA nes-1 NOSTRIL nas-, tere-2 NOSTRUM nes-2 NOT ne, wekti- NOTCH sek-
2005:OUR nes-2
2006:OURS nes-2
2065:Pass pete- PASSIBLE pé@{(i)- PASSIM pete- PASSION pé@{i)- PASSIVE pé@(i)- PASTILLE pa- PASTOR pa- PASTURE pa- PATEN pete- PATENT pete- PATER peter- PATERNAL peter- PATERNOSTER nes-2 PATH pent- PATHETIC kWent(h)- PATHO- kWent(h)- PATHOGNOMIC gné- PATHOGNOMONIC kWent(h)- PATHOS kWent(h)- -PATHY kWent(h)- PATIENT pé@(i)- PATINA! pete- PATINA? pete- PATRI- peter- PATRIARCH peter- PATRICIAN peter- PATRICLINOUS _ klei- PATRIMONY peter- PATRIOT peter- PATRON peter- _ PATRONYMIC nO-men- PATULOUS  pete- PAUCITY pau- PAUPER pau- PAUSE paus- PAVE peu-
```


## [2026-09-07T18:20:13.959Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD asem ===\" && grep -n -i \"asem\\|'sym\\|ʾsym\" PHD.txt PHD_mackenzie.txt | head -20 && echo \"=== PHD amah ===\" && grep -n -i \"amah\\|amāh\\|'mh \" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-07T18:20:14.035Z] TOOL RESULT

```
=== PHD asem ===
PHD_mackenzie.txt:1216:asem ['sym I = M, N sim] silver.
PHD_mackenzie.txt:4082: pasemal [psym)l, v. hamemal] defendant, accused.
PHD_mackenzie.txt:4103:paseman [psym'n l I = M, N .......] penitent, repentant.
PHD_mackenzie.txt:4540:sem [sym I N -] = asem.
PHD_mackenzie.txt:5908:accused pasemal.                          aged pir.
PHD_mackenzie.txt:6363:   pasemiilih.                              destroyed anast, miidag, tabiih, wany;
PHD_mackenzie.txt:6365:defendant pasemiil.                        destroyer, destructive kastar, zadiir.
PHD_mackenzie.txt:7232:pain bes, dard, pim.                   penitence petitigih, pasemanih.
PHD_mackenzie.txt:7233:painless adard.                        penitent petitig, paseman.
PHD_mackenzie.txt:7442:repentance abaxsih, pasemanih.           reward mizd, padiisn, diisar.
PHD_mackenzie.txt:7443:repentant abaxs, paseman.                rhinoceros karg.
PHD_mackenzie.txt:7582:silver (a)sem; (a.) asemen.                   slope, v. acclivity, declivity.
PHD_mackenzie.txt:8596:paseminih         -"'"U t""6\)U Q)      pardag                      \~~Q)
PHD_mackenzie.txt:8597:paseman                 \~Q)            pambagcn                 \~cU
PHD_mackenzie.txt:8606:passinJisn         ,~ ' \ t"'U CU       pasemal
PHD_mackenzie.txt:8608:pasm                       ~V           pasemalih             ~v
PHD_mackenzie.txt:11574:asemen               ,~           amarg                   ~
=== PHD amah ===
PHD.txt:189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
PHD.txt:191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
PHD.txt:214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
PHD.txt:388:h- [HWE- < A d hwh; h- | M h-] be (defective verb). !had [HWEt! ! = Av. Gat] now, then; that is (= à). *hàd [/?t!] a section of the Yasna. hàdamaàns?r [/Ptkmnsl = Av. hača.mādra-| those scriptures dealing with ritual matters. ~ig [-yk'] concerned with the above. - hādēxt [W#twht! = Av. hadaoxta-] certain scriptural texts; a particular sacrifice. haft [лб | M Apt, N ~] seven. ~ad [7o | M hpt'd, N ~] seventy. ~ag [-À! | N hafta] week. —šn [-”x!] the seven planets. haftàr [h5tl | (N kaftār !)] hyena. haftdah [%tdh | N ~, hifdah] seventeen. Haftóring [kftw(k)lng = Av. haptóiringa-] astr. the Great Bear. hagriz [hkic | M hgryc, N hargiz] ever; (with a negative) never. halag [Alz'] foolish, imprudent. ~th: folly, madness. halām [Pm | N ~] potted meat. halilag [hlylk' | N ~a] myrobalan. ham [hm | = M, N ~] also; same; v. 6. —ih: association, union, harmony. hamābēr [hm’fyl | M 72m°byr] storehouse. hamāģ [hm’k' | M Pwg, N hama] all. ~-dén [-dyn'] a complete religious ceremony. hamagih [hmkyh | N —i] totality, universality. hamahl [4(*)4[] = hamāl. hamāl [ml | N ~] equal, peer; comrade, hambadig [hmbtyk'] opponent, adversary. hambah-, v. *hambastan. hambāh-, ~išn, v. hambástan. hambān [hmb’n' | N anbán(a)] skin bag. hamband [hmbnd] connected. ~ih: connection. hamband-, —išn, v. 'hambastan.
PHD.txt:398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
PHD.txt:566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
PHD.txt:583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:1319:comrade hamahl, hamāl.
PHD.txt:1790:equal (n.) hamahl, hamal, hamtag.
PHD.txt:3072:peer hamahl, hamāl, hamtag.
PHD.txt:4384:Amahraspandan Wahman Ardwahišt (Urd-, Ašwahišt) Šahrewar Spandarmad Hordād Amurdād
PHD_mackenzie.txt:989: amahraspand ['mhrspnd I M (')mhr'spnd] a Holy Immortal.
PHD_mackenzie.txt:1014:Amurdad ['m(w)rdt' IN murdtid] Immortality, the sixth Amahraspand,
PHD_mackenzie.txt:1172:  Amahraspand, guardian of fire; cal. 2nd month; 3rd day.
PHD_mackenzie.txt:2674:hamahl [hme)hi] = hamal.
PHD_mackenzie.txt:2916: Hordad [hwrdt I M hrwd)d, N Xurdiid] Perfection, the fifth Amahra-
PHD_mackenzie.txt:4592:         Amahraspand, earth goddess; cal. 12th month; 5th day.
PHD_mackenzie.txt:4754:Sahrewar [Itrywr I N -] Best Rule, the third Amahraspand, guardian of
PHD_mackenzie.txt:5147:Wahman [whwmn ' I M whmn, N bahman] Good Mind, the first Amahra-
```


## [2026-09-07T18:20:29.502Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN sim ===\" && grep -n -i \"sīm\\|sim ‘\\|Silber\" HRN.txt | head -20 && echo \"=== HUB sim/Silber ===\" && grep -n -i \"Silber\\|asem\\|ἄσημον\\|asemon\" HUB.txt | head -20"
}
```


### [2026-09-07T18:20:29.569Z] TOOL RESULT

```
=== HRN sim ===
455:/2^' ab, ätv *Wasser ; vergl. slm]ab (*Quecksilber, wortl.
456:'Silberwasser' d. i. flüssiges Silber), i^'^i^M Jer. 41, 8
6016:silber'*'^).
6030:kurd. zive^ arm. ztpak 'Quecksilber*.- 152 —
6658:Xp. sim *Silber , sitnm 'silbern' (phlv. usltn, astnnn)
=== HUB sim/Silber ===
4215:'Silber =^ phi. asTm, gr. aatjiioQ (Noldeke, Pers. Stud. II,
4466:pieman (pazmdn^ puzmdn) *bereuend* aus paseman; hizisk
5825:zlvajjlva 'Quecksilber H. 683; suvaw 'ich gehe' H. 778 ; buvam
5974:Dagegen zlva, jlva 'Quecksilber H. 683.
6917:parsisch) = zd. aSemaoya- 'Ketzer . So bleibt von echt per-
8166:oben p. 49 — 50 und § il); jtva *Quecksilber = ziva^ siehe
8188:II, 57; zarf 'tief = zd. jiafra-; ztva --^ jiva 'Quecksilber,
8420:*Beir = zd. ^cisa-, arm. tasem 'behaue'; tast 'Becken' = zd.
8750:*) Z. B. zibaq 'Queoksilber', arm. zibak (geschrieben zipah\ syr.
10862:paSeman
```


## [2026-09-07T18:20:30.550Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT ahma ===\" && grep -n \"ahma-\\|ahmāka\\|ahmaka\" BRT.txt | head -20 && echo \"=== SOD max ===\" && grep -n \"m'x\\|mʾx\\|m`x\\|m’x\" SOD.txt SOD_pages.txt | head -20"
}
```


### [2026-09-07T18:20:31.836Z] TOOL RESULT

```
(eval):1: unmatched "
```


## [2026-09-07T18:20:37.187Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6650,6670p' HRN.txt && echo \"---- HUB ctx ----\" && sed -n '4205,4225p' HUB.txt"
}
```


### [2026-09-07T18:20:37.240Z] TOOL RESULT

```
^) In E^snadäsa^s Pärasiprakäga aus Akbar^s Zeit findet sich nur
{Mia- (No. 723), wie die heutige indische Aussprache lautet.
*) Vergl. Seite 128 Note 6.
^) Ich vermag mir nach der bei Vullers abgedruckten persischen
Erklärung keine rechte Vorstellung über die Verwendung des sim zu
machen, doch scheint es unserem 'Kummet* nahe zu kommen.— 169 —
Stützhülz (am Joch)'); arm. .sami\/v 'Stirnliolz des
Ochsenjoches (de Lagarde, No. 19:^8) i).
Xp. sim *Silber , sitnm 'silbern' (phlv. usltn, astnnn)
dagegen ist bekanntlich griechisches Lehnwort (vergl.
zuletzt Nöldeke, Pers. Stud. II, 45).
765. sl/inury 'Greif, Adler; N. pr.', vergl. STn\duxt,
aw. saenö mereyö- *Adler' ; phlv. stnmuro, seiw murük
(Yätkrtr-r Zar. S. ()4).
ai. ^ijefui' Talke*; arm. ein milvus (H. No. 280).
S,
766. Süx 'Zweig, Ast; Hörn (des Stieres), Greweih'.
ai. rdkhä' 'Zw^eig, Ast*; phlv. säk (West 111, 118
Note 1), natak]sak (Bund.) d. i. säx; arm. cu/ (H.
No. 279); lit. szakfi.
LW. kurd. säy; aty. ^ä/; bei. mh 'Hörn, afrt/ 'Ast*;
---- HUB ctx ----
vitae', twsdara, n^sgiya antidotum*, paz. anos 'antidote' Shk.
230, phi. anos Gl. and Ind. 59, vgl. phi. anorak *unsterb-
lich*, arm. anvsak unverganglich' ; dazu N. pr. Nosirevan
(bei Firdusi metri causa) = Nosirvdn (Muwaffaq
p. 4, Z. 7), alter Anosarvan (Noldeke, Tab. 136), paz.
anosruan, phi. anosakruvdn, arm. Anuseruan Xosrov (Sebeos
26, 30) = *Chosru Nushirvan*; N. pr. Noszad, alter Anosa-
zad, phi. anosakzat NOldeke, BB. 4, 52, Tab. 263, 467;
nosddir^) (bei Vullers ndsddur) =^ syr. anosddur, arm. ami-
sadr (nur bei CaxCax und im kleinen Wb.) 'Salmiak*; sltn
'Silber =^ phi. asTm, gr. aatjiioQ (Noldeke, Pers. Stud. II,
45); sdgird *Schuler = paz. asdgard Min. Gl. 17, arm.
asakert; vSrdn Viist', paz. avTrdn Min. Gl. 21, phi. aperdn;
vdrun ^) perversus, miser ^= paz. awdrun 'irregular, wicked*
Min. Gl. 26, phi. apdrfin Gl. and Ind. 9; zPr unten = paz.
azer Shk. 236 (aus z = «^^), paz. az = ap. hacd und paz.
er in ertan u. s. w. = zd. adardt); Murddd *der funfte
Monat' == paz. ^amerddd" Min. Gl. 7, parsT amiirddd
ZDMG. 36, 60, phi. amurd{d)t, zd. ameretdt-, ameretatdt-;
Naked, alter Anahed (Noldeke, Tab. 4) = paz. andhu)
Shk. 228, phi. andhit, arm. Anahit, np. anahata (fiir "^aftd-
```


## [2026-09-07T18:20:38.605Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'we, us\\|amaxam\\|amāxam' SOD_pages.txt | head -20; echo \"--- max ---\"; grep -nF \"m'x\" SOD_pages.txt | head -20"
}
```


### [2026-09-07T18:20:38.702Z] TOOL RESULT

```
18471:       maxu        OynVx, nVxw) ©<OP amaxam ^nVyCh)1,
18690:        max    OynVx, ym'x)   ©<*ahmakam; OP amaxam
18892:       TSP 2.951 n pl8l                                                           we, us
20066:    5701 mzyxy* M                                         X                we, us
--- max ---
8822:1744 >sk)yr- B                        jj^^O-^JL^                           sumax      =^sm}Yw, 'sm'xfw)
8857: 1764 'sm'xfw)     M                                        U^
8859:       asmax(u) ©<*smdxam          ^sm'yw, sm'x
10053:      canu, ka5u ©Idg. ^c'n'kw, k5                           2177 •ym'x    S =» 'ym^, m>x!
18371:      5160 V zprt B                                      <JU          max (m'xw) ©pers. pron. lpl. nom. -^m'yw,
18442:5160 V zprt B                                                      max (m'xw) ©pers. pron. lpl. nom. =^m}yw,
18506:      max/h -zamnu         ©loc. m>h-jmnwyi ^m'xjmnw                 split-minded(vv/i<9je mind has been split)
18671:      matsak, matisk ? (m'st'kh,                                         5260 m'xnwy M, C        •                              > .U
18680:                                                                         5261 m'x rwc    M         ^^'^j^jjj^^^jh^               Jjj
18686:       (to)initiate                                                      5262 m'x txyz M                                 *U ojc/Pft
18690:        max    OynVx, ym'x)   ©<*ahmakam; OP amaxam
18691:                                                                         5263 m'xw =» m^Oi)1, m'yw
18694:                                                                         5264 m'xyt -> m'x*
18695:       GMS 399, 1375; m'xw, KG; C2                                       5265 m'y'ms- B
18703:       CII 1990 G4; C2, m'xwi Anc. Leu. 2.63, 5.32,                             ->my9, my52, myt/8
18706:       nom. 4.9; CII 1990 A6; m'xy, GMS 622; C2-, CII
18708:       1990 Dl; m'xyu STii 4.40; ot'x/i.KG 591
18709:5254 m'xPryy M                           ( j»_j aU)«U (^'A>-
18715:5255 m'xc'ny M                             4jUU <*U(«j L> j>ja)          5268 m'yS'yt'k B                (hj, VU// jt Jh)j&-*j
18720:5256 m'xCh) -» m>Y(h)2
```


## [2026-09-07T18:20:47.567Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18680,18700p' SOD_pages.txt && echo \"--- page tags around ---\" && awk 'NR>=18400 && NR<=18760 && /pdf page/ {print NR\": \"$0}' SOD_pages.txt"
}
```


### [2026-09-07T18:20:48.820Z] TOOL RESULT

```
                                                                         5261 m'x rwc    M         ^^'^j^jjj^^^jh^               Jjj
 5249 m'tyrn ^ nVt1
                                                                               max-roc
5250 m'tys =» nVt1                                             './*/>          twelfth day of the month
5251 m\vysn- M                                                                 Hen. JRAS 1945, 149.19
     mawis(a)n ©impf. =^}nwysn*
       (to)initiate                                                      5262 m'x txyz M                                 *U ojc/Pft
                                                                              max-t(a)xez ?
       GMS 547                       s                                         rising of moon, moonrise
5252 mV        M, C                                                            GMS 662
        max    OynVx, ym'x)   ©<*ahmakam; OP amaxam
                                                                         5263 m'xw =» m^Oi)1, m'yw
         ©first, pi. pres. pron. ^nVyw, nVyCh)1, m}xnc
       we
                                                                         5264 m'xyt -> m'x*
       GMS 399, 1375; m'xw, KG; C2                                       5265 m'y'ms- B
                                                                              mayams ©impf.        >*>y>/nj-1 myms-
5253 m>x2                                                           .u
                                                                               (to)be finished
     max ©<*mah ©ace -w-> ob. -y; pi. -yt                                      GMS 828
         -mii^Gi)2, YRX>
--- page tags around ---
```


## [2026-09-07T18:20:58.676Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SOD_pages.txt | head -5; grep -c \"\" SOD_pages.txt; echo \"---\"; awk '/pdf page/{n=$0} NR==18690{print n}' SOD_pages.txt; echo \"--- mayw ---\"; grep -nF \"m'yw\" SOD_pages.txt | head -20"
}
```


### [2026-09-07T18:20:59.995Z] TOOL RESULT

```
45616
---

--- mayw ---
6279:879 'm'ywn      M
8818:       sk'wrSy*                                                    1758 'sm^h => 'sm'yw
8820:                                                                   1759 'sm'yw B, S                            us.
8859:       asmax(u) ©<*smdxam          ^sm'yw, sm'x
9593:      ustmax ©<vahistdm-aham              ^wstm'yw                   2021 ,wt,,kcyk       =* ,wt>kcyk
12141:                                                                               ace. & ob. -my, >PZY, -fy, -P, sm'yw
18371:      5160 V zprt B                                      <JU          max (m'xw) ©pers. pron. lpl. nom. -^m'yw,
18455:   m'yw
18468:  SHSm'yw          B,S                                                  15.21; SCE 462, 487, 524; VJ 332, 394; C2; MSP
18478:  5176 m'yw pyyy B
18486:  5177 m'ywnd- M
18492:  5178 m'ywnt       C =* nVywnd-                                        ^mW
18495:       mayone ^my*wn, 'm'ywn                                          BSTBL, Vim. 26, 182, Dhu. 56, 115
18691:                                                                         5263 m'xw =» m^Oi)1, m'yw
18711:     max-0ay ^m'yw pyyy                                                       me9/6 (my65, myy65) -»my9, my5*
30419:9259 sm'yw      B, S                                      Li
31425:         bodily, corporal                                          tan ©2pl. encl. pron. ^sm'yw, -t, -j3n, -fn
33341:10236 wstm'yw S                                    c^                 old, worn out
```


## [2026-09-07T18:21:05.510Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18450,18480p' SOD_pages.txt"
}
```


### [2026-09-07T18:21:05.554Z] TOOL RESULT

```
                                                                               'x1
                                                                                                                      206

   m'yw

                                                                       GMS 634, 687
            -*m>x2, YRX>
          moon, month
                                                                 5186 m'h      jj)(^>U j-> ^jj rijjf t>*>")>^ <J* <cjj<j&
          GMS 1274 n 1; VJ 38, 363; TSP 6.147, 8.166;
            BSTBL; SCE 495; MDii; MDiii; m'YK TSP                     man (m»n, m»nh) ©<*man ©ace. -w; ob. -(>)y
            2.1234, 3.147; BSTBL, Dhu. 229, 231, 269; nom.
                                                                        -►nVn'k, mWy, m>n prirtn, m>n prnVt'k2,
            m'Yy, GMS 970 n 1; Frag. Len. 52.14; rrixK KG               cnnVny, myn, cnm'ny
            591; rriYyK Intox. 35; -w, Vim. 129; Dhu. 229;            mind, spirit, heart, conscience
            -y, Dhu. 239                                              m>nyy BSTBL, Dhu. 238, 288, Dhy. 104; TSP
  SHSm'yw          B,S                                                  15.21; SCE 462, 487, 524; VJ 332, 394; C2; MSP
                                         (u^^^^U
                                                                        d2; GMS 348; rrinK VJ 1243; Hen. Tales. 48(14
       maxu        OynVx, nVxw) ©<OP amaxam ^nVyCh)1,
                                                                 5187 mWyd'k =* m)ny»yd»y
       we                                                        5188 m,n> M, C
                                   ;                                                                                    ^|
       GMS m'1x3175; VJ; TSP; BSTBL STi 86.10; Frag.                  mana (m0 ©f. pron. demons. -*m>n>k, 'mw,
         Len.; MDii
                                                                      thismys'nd, m'n'kh, mJnt
  5176 m'yw pyyy B
                                                     •U^Ui-           GMS 1402, 1466, 1473; BBB 560; Hen. Cosm.
       mSxu f3ayi -»m)xPyyy
```


## [2026-09-07T18:21:13.919Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=18452 && NR<=18760 && /^ *(20[0-9]|21[0-9]) *$/ {print NR\": [\"$0\"]\"}' SOD_pages.txt"
}
```


### [2026-09-07T18:21:15.338Z] TOOL RESULT

```
18666: [ 209]
```


## [2026-09-07T18:21:19.979Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT ahma ===\" && grep -n \"ahma\" BRT.txt | head -30"
}
```


### [2026-09-07T18:21:20.024Z] TOOL RESULT

```
=== BRT ahma ===
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2464:yat  baväma  aiwi.vanyn  dänavö  . .  ahmi gal'ie  piianähu  Yt.5.73;  —  ahmäi  J/ri- n?nti .  ./ravalayö  buyiil  ahmi  nmäne  giusia va^wa  ..  ". .  dem  . . ;  in  dessen  Hause  . ." V't.  jj-sif.;  Y..;j.6  (s.  2  2  aa);  —  auch bei  Beziehung  auf  das  Subjekt  des  Satzes: (ya^a)nar>m ..  asavamm*jas?nSfm  ahmya nmjne  .  .  paiti  taröpi^wim  dai'i^yät  "als ob  er  einen  Gläubigen,  der  in  sein  (zu ihm  ins)  Haus  kommt  .  ."  V.y.aa;  — naSca  ,  .  *hö  nl  ahmat  haca  gätaot  isaetci fraiütöip  nöit  apaiiitöit(%A.)'B.23.  b)  sub- stantivisch: adä  (sd.)  ta^a  guti  p>r9- sat  as>m  .  .  ahmäi  asä  (als  Subj.)  ,  ■  paitl.- mravat  Y.ag.ii.;  30.t,  46.8,  13;  —  uz- valoayat  zara^ustrS  annm  mainyUm  .  . paiti  ahmäi  adavata  .  .  aarS  mainyus  .  .
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in  . . yantä  aiibyö  dair?  (sd)  voka  as  manö  Y.  \  geraten,  dadurch  könnte  er  Schaden  neh- 34-&]  9.  2&  10,  45-ii  — yaisqm  ..  mazdä  \iata"  V,/_j.37;  —  ahmat  haca  /«>nj  (sd) ..  vatghö  vai'ja  alsqm  ..  Yt.i6.%; — ^J  sayiJ/A' Nik.  7;  *2; — yesi  tat  paiti  irisjati syao^anä  yä  vacatihä  yä  yasnJ  .  .  ae^qm  '  aiähal  hala  iyae>n!i7ar3za  (sd.)  .  ,  V./_?. töi..}hmä  pourutimäil  äasl?(sd.}Y.j4-^,''  38-  2)  vorausweisend;  i)  adjektivisch ■ —  yöi  *aite  . .  *gä'kä  nSit  *srävayänti  . .  I  auf  direkte  Rede  oder  Zitat:  vahiütsm  . . assqm  fyaohamm\ia'\  .  .  N, 25;  —  ySt  ..'igänii  ..  vir^zyat  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag-  *pt3  asahyä  mazdlY.4y.2;~aya  antar?.- £qm  nöit  aita^qm  ratufris  ..  N.52;  ^j\  uxti  (sd.) :  nöit  nS  mana  (usw.,  Y..^5.z) —  yahmät  kakmäicit  nalmaruim  vätS  ä'^rö  Y.ig.i$.  —  a)  mit  ergänzendem  Relativ: baoiolm  vibaraiti  (sd.)  ahmll  kahmäiHt  aya  aibigara  (LS.  als  Instr.)  aya  aibijary- nalmanqm..\.8.&o.  a)  Die  Beziehung  ta{d.^.)  yä  amfsanqm  sp^ntanqm..:  gave ist  ungenau:  ^yJ  räakaytn  (sd.)  sravaahä  rto5j/(usw.,Y._j5.4)  Vr.J2.i.  a)  substan- vahistät  iyadkanäl  mantärü  aeibyö  mazäi  tivisch  und  adjektivisch  auf  eine  erläuternde akä  (sd)  mraot  "qua  alienant  doc-  oder  ergänzende  nominale  Beifügung:  «7.5- trina  . .,  üs  .  ."  (statt  qui  ..  iis  ,  .)  Y.32.  yacä  i^agtuL  yäsat  ahyi  Virßzin3m..ahyä .. 1 2'*^  Anhang  zu  II  I  1,  2.     a)  An   ahurahya  uruasimai^A.)  mazda  Y.j2.i ;  2S.
2488:ultä  kakmäiclt  .  .  däyät  ahurö 44-i6,  27.14;  — yastn  .,  tari.mqstä  .. anying  ahmat  yi  hei  arim  mainyätä  Y. 4j.ii;  —  anyö  akmat  yö janaili  V.5. 34; N.  iS\  —  agustä  (sd.)  vacS  singhamahl aHbyö  yöi  ,  .  alakyä  gaSha  vlm?r?ncaiis (sd.)  aihp  aiibyö  nahiltä  yöi  *zrazda  aa- Afn  tnazdai  Y.j/.  i;  jo.8;  —  alsam  gä- naoiti  v?rfirayrtim  yöi  diin  .  .  /r3yaz?nte YL/O.16;  —  vätöyö/ä (sd.)  1/  aäbyöyöi  Tl.. v»r^syqn  Y.J5.6;  —  vJspaiibyö  aiibyö  yöi .  .  upa.sruttvanii  N.  20;  —  ahe  .  .  yö  nö dussarfkö  AiitaiteY.  10.12  (s.a.);  —  mäoa fiS  a/tmi  /raniliti  (sd.)  yÖ  nö  ..  inrixsaile ^■^5'7i  —  ^y^  *äröi  häkunnim  {'^d^ yayä haiinti  urvqnö  Y.j'^j.  9;  — ■  //  äbya  (statt DP.)"*  bairyeinte  yalsatn  .  .  fräyö  (sd.) '      ■  ■  bei
2511:■')  Pü.:  Ä  apumäyai  an  fan  i  :^ii.  ~  „) -^'^.snaro 'Um  myazdiin  yot.dim  hatfluma  (sd.) ai,  erl.!  ä  *"n.  —  13)  Pü,!  im  'ich  bin'.  —  Y. Äs;  —  '/il  yasrta  'ta  vahma  .  .  ava.- M)  Attraktion?  Pü.:  ic res iräyinä . . ä üän.  —  \jasa  . .  aot  sam  "um  dieses  (meines)  Ge- .s)Pü.:/«,.».«i^a«.-  .6)P(i.:,-ii_..;b  (g  ^iji        ;„  Yt5.i32  (s.  s);  —  am
2533:*'te  *yffi'^  fracarinti  , .  aiialiqm  .  .  N.  ,paiqn  ,  ,  'na  ,  ,  triltm  k>hrp}m  hvan.- ^.  III)  In  folgenden  Fallen  brauchen  i  t/arwr« -f?rv«aii/V.  5. 13,  3)  'dann'  im wir  den  Sing,  mit  'ein'  (unbestimmter  Ar- !  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Plur.  artikellos  (vgl.  ^aisa- 111}  j  dessen',  einen  Zwischensatz  hinter  einem yesica  .  .  upairi  'l^m  iristim  .  .  Ajr^zy^lf '  SaU  mit  yai  einleitend:  y^i  ndii  nidan- yaia  .  ,  "und  wenn  (man)  .  .  auf  einem  sayilnte  —  ''ja  kl  alte  sünö  vä  .  .  fraja- Toten  ..  liegen  lässt  .  ."  V.5.61;  — yö\s,yi>  —  kä  Af  asU  äiaX.ö.^T,  —  yaii'a vastnm  upaiiharizatti  upatri  °t»m  tristem  |  vaoeäp  aiSö  m7  Aanqm  .  .  p3r>saKuAa  — "wenn  einer  ein  Gewandstück  auf  einem '  "'la  ae^a  y<J  kaine  hanqm  . .  p?nsaili  , .  — Toten  liegen  lässt"  V.Äaj;  —  bei  rela- 1 'ort  assa  yS  kaine  altahmat  puir.lt  *mi- tivisch  angeschlossenem  Nomen:  yat  "te^  manxlstti  —  '^Aapanta  .  .  vfri^qn  .  . yöi  tnazdayasna  . ,  taci.apaya  nasSum  fra-  [  V.  /J.  1 3  f. ;  —  yeii  mit  Aari^nm  baraili jasqn  "wenn  Mazday.  auf  einen  Leich-  -  "da  aisa  yö  afirinüyakö  adJityö.an- nam  in  fliessendem  Wasser  stossen"  V.  6.  Aarj^nin  (sd.)  iri^ät  —  ^'>para  A!  iri- 26;  <y.73,  7-36.  \sittt5  rais?m  cikayat  .,  V.7j.i6.
2685:sat  Kiof);  —  ^kahmai  (s  'vahmi  paüi  .  j.  aevandasa-  Adj.  'der  elfte':  garayd va^Ö  ..  H.  /.  I  s>;  —  yo  g,l%aHqm  dyim  ■>  uzuxiyqn  .  .  'sß  .  .  dvadasS  .  .  Yt.  /p.  2 ; väcim  apayäUi  "vqm^vä  vacastalnm  N.  /.8_  vl/^.g,  5.29  (statt  AS.J;  —  ^ssm 42;  *42,  43;    —    'vo    akunö    vairyS   ..   asar^hamca  V.V.ij.
2686:*zamarigusa    avazat   vXspe   daifa    Yt /<?.       AbleiV  aus  ■arr'OB.u'ajflZw. 'elf;  vgl.  tF,  S  ?/o 81 ;  —  yahmai  . .  aurvantö  . .  v3sa  '^an-  ■     aK  und  IF.  p.  245.  —  Pü. :  yHdahum. }aianie   °va   caxra  (sd.)    Yt  10.136;    —  •  j-    aeväkam    Adv.    'zugleich' (?):    aiv aim  .  .  yß  t0  °ve  säsnä   (sd.)  gäsatä    Y.   narqm  asaonqm  ahunvitim  ga^qm  frasrä- ^9.8;  YtJ7.i9,2i;    —  yö  nö  °v6  at  U  vay'nti  Vd. /2.
2706:•  j,  aevo.gaya-  n.  'Längenausdehnung  |(>ij«(i">  me  yaoidäiUm  "ihr  könntet  mich eines  Schritts,  eine  Schrittlänge';  Äa/ ^«i-a  ,  purifiziren"  V.Äioo.  1,2  a)  mit  Gen. anys.anyaeibyö}  ya^a  'gatm  iu^a  (sd.) '  und  Inf.:  naj/a  .  .  Aäu  ni  ahmat  haca •gsimi  ,  .  "Wie  weit  von  einander?  "SiQ  gstaot  isalta  frasBtÖit  »eil  apasüföil  (sd.) viel  als  eine  Schrittlänge  beträgt  .  ."  "^  .{'^rayamcina  gämanam  P.  2jj>.  3)  '(es) p.  S.                                                                     I  können,  vermögen,  (dazu)  im  Stand  sein',
2964:vgl-  evata-  Adj.  'inferior'  (wozu  aera-  wie  Ht.  |  ^  püZ.^';  —  yahmat  haca  naicU  bunjayät
3269:•  j.  a-dahma-  Adj.  'der  nicht  dahma- (sd.),  nicht  unterrichtet  ist';  saota  anasava "mö  atanu.tnai<r3  Vt./o.iaS;  —  jahi  .  . yö  xsudrh  ham.rasiwayeiti  dahmanam 'manamca  V.1S.62.
3318:•  j.  aSu-tavah-  m.  Name  eines  Bergs oder  Gebirgs:  ahma^  kam  garayB  fraoxs- yqn  . .  °vasca  Yt,  if).  6.
3399:—  'rum  (GS.)  hö  rätanam  . .  isänAaaa (sd.)  Yl  ig.  53;  53';  F.  7^';  — paiH.ä3n?m ainim  baraiti  ..  diwiat  haca  'va  sauAaite V, /<y,  i;  2—4;  —  hial  n3  'va  a^aururum /ia:a  *gai>äöU  *parayat  "wie  weit  soll  ein , Priester  auf  Priesterdienst  aus  dem  Haus gehen?"  N.4; — nsit  ml  apqm  -va  aiwi/ti/. ■  vpnioye  (so.)  dai^Aava  carät  Y.p.z4;  — yS  *mainyde  davi^einti  haomimla  'va- ÄfMi"^  Y.  JO.  15; — 'runqmca  paitl.ajqinm (sd.)..^;/  *iyeyqm  düräi  as^.TsS(sd.)  dah- yunqm  V.42.6;  N.4;  —  °va  dürai/rakat5 (sd.)  Yl/ö.  17; — atl:mi  ma'irjm  mä  fra- äaisayöis  anyat  pure  vä  .  .  'va/iäi*^  vä Yti4.46;  —  °va  kqm^.na/5  Vyt^;  — 'vatum  yaoiäa'^^S  dahmayat  pars  ßfritsit ..daiiiMupailim..V.g.zT,  7.41-  A)  ins- bes.  als  Bezeichnung  für  den  eisten,  den Priesterstand  (s.  unter  ^piltra-):  "va  ra- >aistä  vastrys ßuyqt  hainsY.ig.iT,ii.S, Ytij.89,V.5.28,y*45'; — 'varum  asläya ra^alstärvm  . .  västrXm  /iüyant?m  Vr.j.  2;
3699:KompE.  —  Pü.:  ap7  zaiär  {!)  gSspand  . .,  erl. ; d»zd  H  zvrt  afii  Mrrl'-).  —  ')  Daher  DST. ZA.  2.  205:  'il  combat  pour  le  boeuf. .'  mit der  Bemerkung:  'expression  presque  brahma-
3777:gaikaAü  tanusi^ä  Y.^J.  7-       2)  Praev.  (mit 'ak;gam-,  'bar;y/th-,  valn-  usw.).        a)  bei Ellipse  des  Verbums:   "wi?a  aparpm  (sd.) paiica    aparam    apnca  paurvaäbya    V.  75, 48;  —  asäaüä  haiä  van/iSus^il  mananhs vankyuscS   xla>rilt  staotäis  '^Tnifl  ahum staotSibyö  °bT  ux'o/l    '^wüt  uxüSibyS  yasnH %wät  yasnsibyd  "und  um  des  ASa  willen und  des    VM.  und  des   guten  XS.:    Lob- gesänge (häufen  wir)  nunmehr,  o  Ah.^  auf Lobgesänge  und  Sprüche  auf  Sprüche  und Gebete  auf  Gebete"  V.^j,.  10";  —  huxsa- %rSJ»m!li  (sd.)    .  .    xsa'inm    ahmai   hya^ 'bii^  dadsmahica  .  .  Y._Jv5. KompA-i  Ableit. —  aLiiM/,  mp..rai*,  np.a/". —  Vgl.  laii,  aei.  —  Pü. :  afar;  (in Komp.  auch): d/f  und  wepgelassen.  —  ')  S.  lu  aiiaiwülay- No.  I.   —    ')  Man  kann  aus   dem   vorherg. Ahsatzdad3maideetgiaT.Ka.  Gdn.n  Übersetzung GlrPb.   3.  32    ist    mir   unverständlich.     Pä.: släyisn  i  IS  öhrmatd  am  haf  släyi'snän  apar,  Sü. : ilulih    te    a-ämin    slulibhya^    utirflalarä.      — ))  Man  erwartete  die  selbe  Redensart  wie  V.
4009:'nicht  hervorwachsend,  spricssend'. Pflanzen:  urvaranqm  . .  yä  para  ahmat histfitta  .  .  ^'yäntis  (NPf.)  hamaya  gätvS Yt.7J.SS-
4341:•  j.  an-ava'iiruxtay-"  f.  'Nichtbrechen des  Gelübdes,  Eidestreue'  (?):  yii  fnäml. data)  dahmayä  vauhuva  °C^ij"  Y.  70.3.
4385:•  j.  an-ahü-  Adj.  'der  keinen  Aha  (sd.) hat';  ahmaofanqm  .  ,  °ahunqm  aratunqm Yt.  /^.  I  o  5 ; — *anaKruA3i?)  ">  arafvS  acisifm duzanhavS  "das  Schlimmste  der  Hölle  ist fiir  den,  der  keinen  A.  und  R.  hat"  P.  14.
4421:•  j.  an-ä'druxtay-  f.  1)  'Nichtliigen':  yeMe xsahräüa  nsit  aot?m  ai)ha  nSit .  .  para HSit  "unter  des  Herrschaft  es  nicht  Kälte gab  noch  . .,  vordem  dass  er  log"  Yt.  ig. 33".  a)'Nichtverletzen  des  Vertrags,  Ver- tragstreue'(?) :  yä  (näml.  data)  dahmaya vaahuyh  'tsU  Y.  70. 3.
4592:•  j.  antar9.ka]»ha-  m.,  Plur.  Name  eines Gebirgs:  ahmat  haca  garayS  fraoxsyan  . . "tihaca  Yt  79.4.
4601:•  j.  antara.daöhav-,  °daliyav-  Adj,  (auch mask.)  'der  inmitten  des  Landes  ist': mi>nm  aiwi.daRyam  ..  '.ä/Sot  ( ASm.)  Yt lo.  1 44.  A)  m.  Name  eines  Berges  oder Gebirgs:  ahmat  haca  garayS  fraoxlyqn  ., dassmS  °/ihu/ Ytig.2.
4650:äahtmm  gä'^anqm  sraohrät  pairistaytili  N.^'<>;  —  mmS  ahuräi  mazdai  mmö N.4^;45^*fH.2.i3; — yd  'nyehe  dahmahe  amisaiibys spintaHbyS mmS'nyagsqm  asao- bansma  *frast»r3nfe  ii.104;  lOi;  —  bsöalnqm  V.i^. 25:32;  —  »üi/  xsnSvayeiti  ahu- iia  hislahe  ..  'nyehe  dvan  (sd)  srayatül  r?m  mazdam  tUSit  °nye  (als  AP.)  amisO. V.j.zg;  N.6',7; —  hvSiits  vä  ySiitö  (i'3)  |  ¥1,70.139;'  '39;  —  hapta  hanti  *käva- yim  vä  'inim  *hais^aeTia  (sd.)  .  .  cayqn ,  iiayS  ratavS  .  .  aai  'nyahu  ralu/risü  N. N./;  — ]avada  'niyam  md^ifia/fi  . .  Bh.  102.  a)  mit  ciV'' :  saoiyanlqm  vfn'üra- 5.  4(?);  —  "nyqmca  suttm  ..  N.ff2(,?);  — jamm  Uta  "nyasHt  (als  APn.)  haxayS  Yt. ^rayS 'nya  (als  APm.)  maya  nihwirgsöU  /p.S9'*'.  NSm.  "/yJ,  ASm.'fiim,  ASn.
4653:vorausg.  nagclm  und  la-  'nicht  irgend  ein anderer';  naSclm  tsm  'nySm  yOsmat  vasdä asa  "ich  kenne  nicht  irgend  einen  andern als  euch,  0  Asä"  Y.  j^7">.  II  a)  mit AbL  des  Verglichenen:  ttsit  mSi  vaiiä(sd.) x/mai  *nyS  Y.  2g.  1 ;  ^0. 1 ;  —  h3m  tta mavaitl  payBm  dadat  'nyJm  %wahmat a^rasciJ  ..Y.46.J;  34.7.  ni)  'alienus', a)  im  Gegensatz  zu  'eigen':  nsii  hl  'iiys ttrva  kaom  urvantm  paiti  irista  bqzaiti V.  y,  9'";  — jahikayai  ya  aom  pu>^r»m baraiti  'nyahmai  arsänai  varit»m  pai'^e apa.baraiti(sd.)Ytij.s8.  b), lim  Gegen- satz zu  'heimisch',  sva.  'hostis':  yadiy  ava'ia *maniyähay  hacä  'niyaria  (iS.)  ma  tarsam ".  ,  vor  keinem  Feind  will  ich  mich  zu fürchten  haben"  D.5,3;  D.4.2;  —  karam tyam  ..ajanam  vasiy  'iiiyJ'  apiy3*ahyaiä (sd)  Bh.  j.  19.  IV)  In  ungenauer  Aus- drucksweise; das  mit  a'  Bezeichnete  ist dem  Vorausgehenden,  dem  es  gegenüber- gestellt wird,  nicht  gleichartig'J':  daat {taeta)  -nyatsam  rähwqm  paiti.maydi^i^d^
4755:—  vTspe  vS  '/a  spmta  staota  zaota  .  .yüS- makim  yasnäica  . .  yat  'lanqm  spmianqm Vr.5.1;  2/,2,Y./2.i',  52.4,  Yt_).3,  4!.if.^ V-p:.i2,4ß,  *Vd.20,  V.  12,2;  —  äat  mraot ahurS  maeda:  ahmakim  tiqma  yat  'fanqm ipgntanqm  .  .  Yt  7.  3 ;  j.  i,  FrW.  /.  2 ;  — yB  nä  ..  kasiitam  . .  fräyatät  (sd.)  *ahma *yq  'i^  sp^tiO  Yt. /.24;  —  vaim  ySi  °s'ä sp»nta  Vyt.^js;  —  '^qsüa  sp^nta  saosyan- lascä  Y.  13.  3 ;  Vr.  3. 5  (wo  -J^sca),  P.  36 C'Si/a),  Vr.22.i,Vt//.i7;  —  sil  sp^nta dame  mäzdayasne..  tadhrasca  Y.  A3;  — kvanca  (sd.)  °sS  sp>nisYT,  ig.  2.  a)  bes. neben  AkM.  genannt:  a^m  ..  durfiianm ahurahe  mazää  x'aT^Aartm  'sanqm  spmta-
4767:ai.  amattya-  Adj.  »unstetblich'.   —    •)  Yl,  iS- 20  stehl  'ynn. p.  amäiaia :  s.  unter  ahma-.
4790:der  Richtung:  atcit  dim  aiwyäili'^^  ya dahma . .  ofritis  P.J2.  a)  'begehen,  (einen Weg)  gehen':  mä  dim  psrisS ..yim  xrvan- tim..pantqm  aiwitim^*'''  "frag  den  nicht, .  .  der  den  grausigen  .  .  Weg  gegangen ist"  H.2.17.        S.  noch  No.  26.
4855:.  j.  a-yaozdä-  f.  'Verunreinigung  Ver- . .  -  ayaBhö.Jyä-  Adj.  (mask.  -ya-)  'mit seuchung':  vT^pm  a  ahmat  'i^"  f 'dya\  ^^^^^^  (eisernen)  Sehnen':  vLlzah...
4970:aväjanam  |  *startä   akatiy  "vaiy  (als  AP.)  mä  dauitH 'vaiy  .  .  parsä  Bh.4'i4i  —  hauv  karam fräiSaytr  .  .  vivana^  nilwa"  pärs^  mann 6a!'dakaf'    karj'uvatiyä    xsa>''apJVt1    abty Bli.j.9;  —  kärJ"  kyi^  hamth^iy^ manä  naiy  gaubataiy  °vam  /adiy'Eh.2.'},io; martiyä  tyaisaty  ..anuHyä  äka'tS 'vaiy {3\sAF.)../rdÄ^/am  Bh.  2. 13.-,        i)  II  auf ein  Relativum  als  dessen  Korrelat:  tya* parsbartam    ä/Sa*    °^a*    adam  pattpadam akunavam    Bh.  t.  14;   —   tyJ'iam    adam aiakam  "vJ^  akunav^tä  D.d.  4 ;  3,  Bh.  l.  7, 4.16,    17,  X.r.  3,  2.3;  —  Uta   ty<^maiy pi^''a^  iatiam  -valciy  (ASn.)  t^urJ'mazdtl patuv    X.7.4;  J.3;    —   kyci'    aparam  .  . Patiparsatiy  °vaky3  . .  Bh.  4-  8;  —  tyaisaiy fi-atamä  anuiiyä  ähc^til  'vaiy  (als  AP.). . frahcTJam  Bh.  3. 1 3 ;  —  tyaiy  panevä  xsäya- hiyä  . .  'vaisäm  naiy  astiy  kartam . .  Bh.  4- 9.11       3)  auf  einen  Satz(inhalt) :  y3  nanm kasyatfke  (sd.)  satthii  da^tti  vfavi  'i'Ot paraiti  (sÄ)  V. /j.  2;  —  ya^a  nSii  .  . kar>tS. .  avasySt  vismteisd.)  °val .  ./rava- lays  Yty.72f.         a)  in  Verbindung  mit ta-  'hie  ille':  ya'isa  azim  häätyene  pu'^rgm daliai  ahmäi  tat  "vat  syapt?m  artdvi.. Ytj.i8f.;(j.S,J5.4,äi,  Vyt.45.        2)vor. ausweisend;  1)  auf  direkte  Rede,  sub- stantivisch: tamatfkil . .  °vat  stuyi:  nSit., xäa  Y.  J2. 3 ;  —  °vat  manawka  maiiiimna : nqm  stavap  Yt5.7;  123,  y.49,  '9- 50;   —  *viövä    'vai   hava    xra'hwa: ml  hiu  nä  .  .  P.  21.         2)  auf  eine erläuternde  oder  ergänzende  nominale  Bei- fügung, a)  adjektivisch,  auch  im  Sinn  unsres Artikels  (des  schwachtonigen 'der'): /a^i- kayäi  yil  aom  puiinm   baraiti  anyahmai arsanai  varsl»m  Yt.  17.58;  —  aat .  .  aom miryjim  /rayrarayati  .  .  parSJars  nqma \.i8.2y,  —  'vä  /ba^sä  .  .  daevaniim  mal- yänqmca  ". .  die  Anfeindungen  der  D.  und Menschen"  Yt. /.  10;  — yasi  tat  paiti  'vä gaiiiä  tayus  .  .  para.baraiti  dasa  ".  ,  was jenes,  das  Anwesen  anlangt.."  V. y.  10; II.         o)    mit   relativischem   Anschluss: *'vau  (NSf.)  pairika  yS   dulyäirya  Yt  8. 54;  —  'vqm  kikrpmt  . ,  yqm  sämake  Yt. y.6i  ;   62,    Y.2O.2,    y.19.14;    —  /la^a *'vadhat  vlsat  yat  tnäsdayamöit  V.  '9- 1 2 ; —  haca  "vaahät  tamia^  yat  datvö.Jatayh V.ig.20\    —    'va   (APn.)  "baEiaza  ..  ya kumäydte  Vr.  9.  3.  b)  substantivisch:
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
```


## [2026-09-07T18:21:21.415Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS amah ===\" && grep -n -i \"amah\\|amāh\\|LNE\" SNS_pages.txt | head -20 && echo \"=== SNS page 232 ===\" && grep -n \"pdf page\" SNS_pages.txt | head -3"
}
```


### [2026-09-07T18:21:21.484Z] TOOL RESULT

```
=== SNS amah ===
3574:                             (AiJ/b.      384)uxsyat-namah-: £»
3717:                .^_T/U^ (•$* :Jj) .»>l fj*:hOmyazad:                     W'Hf                                            •   Y/f^ ^IU <(S«-aU: amah hem:                                       _**.- *>
4942: bhrlnanti          : ^^.^brlnenti, /bray- 3 fc.                                 I
12297:                                                                                                                              i#io   :nislned-            ,yt i^: Y^J)^^
12988:    Ai^LJoj^/tgOsurvan amahraspand:^^^^^                                                -jl^ol^i j>J r L<"jff              1j/   ^^"iU G5us urva-                                     :       U
15138:brlnenti, 109/1            mazainya- 238/11                        raBsa- 234/13                varasa- 280/14
15318:uxsyat-namah 71/14       karana- 212/17
15717:valnen 276/16
15721:                         vlst ud do 221/10               visbad 273/16             vizlnend 271/10
16196:                                                                 getog xrid 180/8         gosurvan amahraspanc
16498:                                                            amah/araag 232/3         andar kar ested 31(
16500:                                                            amah hem 74/5            andar ofted 62/12
16504:                                                            amahraspandan 48/21      andarvay 81/3
=== SNS page 232 ===
```


## [2026-09-07T18:21:29.777Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"amah/\\|amaag\\|amag/\" SNS_pages.txt | head; echo \"=== SNS 232 area ===\"; grep -n \"232/\" SNS_pages.txt | head -20"
}
```


### [2026-09-07T18:21:29.834Z] TOOL RESULT

```
9255:                                                                                                                               U :amag/araah:
16498:                                                            amah/araag 232/3         andar kar ested 31(
=== SNS 232 area ===
14884:     r6ha- 232/10                Q?akta- 173/7                     stfbhih 179/2
14998:    asmlka- 232/4
15025:                                 patis 142/17-232/20               rauta- £29/13
15082:                                          omaxam- 232/4                 K
15146:raaGzant- 253/4            mi0rO-drug          243/12              raocfa- 232/10               vahista- 261/1
15184:drang- 324/7              nOit^.asti 232/13
15347:                                                   amaka- 232/4                  asparana- 342/2
15472:                         nwwra 262/21                      pry'd 129/12             rwy 232/10
15484:                             nyst 232/13                   pws/pwsr 138/16          s J r p r 193/19
15496:                             p'sb'n 117/2                  pys 142/17-232/20        sryn 163/1
15607:*b    Jn   14/16              >m'h 232/5
15888:pestar 232/22              pusarlh 109/17                    rad 226/2              reraanth 235/13
15903:prastisn 128/4             ranenfind 224/7                   rastag3n 226/17        rOnJf232/7
15909:purgyandadlha 139/20       rastlh 222/19                     raved 173/16           rOy 62/18-232/9
15966:                                                           patflglh 16/22                pfis    142/16-232/15
15992:n§st 232/12            nihuftag 262/15                                                           SzanlhSd 18/6
16498:                                                            amah/araag 232/3         andar kar ested 31(
16555:amOxted 52/8                a-s 195/4                              abaxtar ron 232/8         abar mad 242/8
```


## [2026-09-07T18:21:31.373Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ahma-\\b\" BRT.txt | head -20; echo \"--- headword style ---\"; grep -n \"ahmāka\\|ahmakim\\|ahmākəm\\|Pron\\. 'wir'\\|'wir'\" BRT.txt | head -20"
}
```


### [2026-09-07T18:21:31.427Z] TOOL RESULT

```
--- headword style ---
4755:—  vTspe  vS  '/a  spmta  staota  zaota  .  .yüS- makim  yasnäica  . .  yat  'lanqm  spmianqm Vr.5.1;  2/,2,Y./2.i',  52.4,  Yt_).3,  4!.if.^ V-p:.i2,4ß,  *Vd.20,  V.  12,2;  —  äat  mraot ahurS  maeda:  ahmakim  tiqma  yat  'fanqm ipgntanqm  .  .  Yt  7.  3 ;  j.  i,  FrW.  /.  2 ;  — yB  nä  ..  kasiitam  . .  fräyatät  (sd.)  *ahma *yq  'i^  sp^tiO  Yt. /.24;  —  vaim  ySi  °s'ä sp»nta  Vyt.^js;  —  '^qsüa  sp^nta  saosyan- lascä  Y.  13.  3 ;  Vr.  3. 5  (wo  -J^sca),  P.  36 C'Si/a),  Vr.22.i,Vt//.i7;  —  sil  sp^nta dame  mäzdayasne..  tadhrasca  Y.  A3;  — kvanca  (sd.)  °sS  sp>nisYT,  ig.  2.  a)  bes. neben  AkM.  genannt:  a^m  ..  durfiianm ahurahe  mazää  x'aT^Aartm  'sanqm  spmta-
8449:als  letzter,  mittelster,  erster  gerufen  wird"'  B-  uboya- (?)■>,  j.  uvaya-",  avaya-", G.  7,6;  —  sraos'fm  ..yazamaide  paoirimca  y^Y^-''^  Adj.  'beide,  beiderseitig';  a)  Sing., 'mtmca  mdotmfmca  fratimtmca  paoiryaca  nur  ASn.  'beides',  substantivisch:  _>■./  nö yasna 'ma^a  maMmaca/rai?mata\t.ii.ii;  ftf>tti  urune  Mvaiin  3^ani:»iiua  vastnm^a Vd.9,  Y,55.a;  3; —  isan  pascaaa  ra^m  ('wir')
13149:—  ahmäi  da%at^'>  v^3%rar]nB ..»rsiSis  xa Vt.i4.s9;'Vyt  34,46; — yä  ml  var^zänäi vaiiuhim  dat/rasastimyx.g.26'^^\—yS  süne . .  astanqm  (als  Obj.)  ahmarstanqm  daoaiti ^■'5-Z'' —  ^  noch  za;  — dazu  mit  IP. statt  DP.:  AaomS  azXzanäitibi?  dtKSiti xsaäS.puirJm  Y.p.  22;  —  durch  enkl. Dat.(-Gen.)  des  Pron.  pers.:  dayä  (Konj.) mS  atarl .  .  äsu  ^O^rym  Y.62.4;  6,  Y. 68.  5';  —  apB  yäivm  vS  yäsämi  . .  t^m ml  dayata  (zP.)  Y.65.11;  13;  —  avat äyaphm  dazdi  ml  YL5.  18,  q.  4,  /J,  3, i~,  25;  — yeiai  sl  ml nsil  daibtt''*>  upastqm .  .  fravaiayS  .  .  Vt.  /^,  1 2 ;  —  Ups  dasla (jP.)  nS  Um  yämm  yB  .  .  Y. 68.21;  21, Vyt  8;  —  kaoma  dazdi  ml  baiSasanqm (als  Obj.t  Y.  jo.  9;  F./4;  —  da>,ani' tl a^ahe  paiti  ('daflir')  hakat  hataur^m  as- panqm  V.  22,  3.  a)  zum  Pron.  re!.  ist der  Dat  eines  Pron.  dem.  zu  ergänzen: asu.aspim  d^äiti  mi%rB  .  .  ysi  mihnm KBit  otwiAruzirtH  Yt.  10. 3 ;  j'.  2}  durch Gen.:  a)  im  Awr.:  dazdi  ahmakim  tat ayaptfiri  yas3  ^wä  yäsämaAiYtlo.^^;
```


## [2026-09-07T18:21:41.791Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9240,9270p' SNS_pages.txt"
}
```


### [2026-09-07T18:21:41.831Z] TOOL RESULT

```
rv                           li; .-.-jl-t fc.U «3'>                                                                             lAi   c^b «.b«jl,
                                                                                                                                                                                   rrr


                                               .jaio :rextan:            Vflft« *
                       ^tf-^ ra?cayat- j /raSc j<                :       fc-
nakti      /r§c    :                                                                                                                                •T/T»5    (p.31 n6.
                                   M/Y^ (fiffPE. 141)
                                        •




                                                                                         aMtaam-:^          (i^ww^^
                                                                                          WtoJto*. ii, 4fi)VMj|fc &»«.
                                                                                                                               U :amag/araah:



                                                                                                                       167 (^UcJU,
                                                                                                                                                        LNH     :


                                                                                                                                                         ahni3ka _
                                                                                                                                                                        >»:

                                                                                                                                                                             ^     ^\


                                                                                                                                                         •f/1A^ .V/JHS
```


## [2026-09-07T18:21:42.510Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ahma\" BRT.txt | sed -n '1,60p' | cut -c1-200"
}
```


### [2026-09-07T18:21:42.596Z] TOOL RESULT

```
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■
2464:yat  baväma  aiwi.vanyn  dänavö  . .  ahmi gal'ie  piianähu  Yt.5.73;  —  ahmäi  J/ri- n?nti .  ./ravalayö  buyiil  ahmi  nmäne  giusia va^wa  ..  ". .  dem  . . ;  in  dessen  Hause  . 
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; 
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däi
2488:ultä  kakmäiclt  .  .  däyät  ahurö 44-i6,  27.14;  — yastn  .,  tari.mqstä  .. anying  ahmat  yi  hei  arim  mainyätä  Y. 4j.ii;  —  anyö  akmat  yö janaili  V.5. 34; N.  iS\  — 
2511:■')  Pü.:  Ä  apumäyai  an  fan  i  :^ii.  ~  „) -^'^.snaro 'Um  myazdiin  yot.dim  hatfluma  (sd.) ai,  erl.!  ä  *"n.  —  13)  Pü,!  im  'ich  bin'.  —  Y. Äs;  —  '/il  yasrta 
2533:*'te  *yffi'^  fracarinti  , .  aiialiqm  .  .  N.  ,paiqn  ,  ,  'na  ,  ,  triltm  k>hrp}m  hvan.- ^.  III)  In  folgenden  Fallen  brauchen  i  t/arwr« -f?rv«aii/V.  5. 13,  3)  'dann'  im w
2685:sat  Kiof);  —  ^kahmai  (s  'vahmi  paüi  .  j.  aevandasa-  Adj.  'der  elfte':  garayd va^Ö  ..  H.  /.  I  s>;  —  yo  g,l%aHqm  dyim  ■>  uzuxiyqn  .  .  'sß  .  .  dvadasS  .  .  Y
2686:*zamarigusa    avazat   vXspe   daifa    Yt /<?.       AbleiV  aus  ■arr'OB.u'ajflZw. 'elf;  vgl.  tF,  S  ?/o 81 ;  —  yahmai  . .  aurvantö  . .  v3sa  '^an-  ■     aK  und  IF.  p.  245
2706:•  j,  aevo.gaya-  n.  'Längenausdehnung  |(>ij«(i">  me  yaoidäiUm  "ihr  könntet  mich eines  Schritts,  eine  Schrittlänge';  Äa/ ^«i-a  ,  purifiziren"  V.Äioo.  1,2  a)  mit  Gen. 
2964:vgl-  evata-  Adj.  'inferior'  (wozu  aera-  wie  Ht.  |  ^  püZ.^';  —  yahmat  haca  naicU  bunjayät
3269:•  j.  a-dahma-  Adj.  'der  nicht  dahma- (sd.),  nicht  unterrichtet  ist';  saota  anasava "mö  atanu.tnai<r3  Vt./o.iaS;  —  jahi  .  . yö  xsudrh  ham.rasiwayeiti  dahmanam 'manamca  V
3318:•  j.  aSu-tavah-  m.  Name  eines  Bergs oder  Gebirgs:  ahma^  kam  garayB  fraoxs- yqn  . .  °vasca  Yt,  if).  6.
3399:—  'rum  (GS.)  hö  rätanam  . .  isänAaaa (sd.)  Yl  ig.  53;  53';  F.  7^';  — paiH.ä3n?m ainim  baraiti  ..  diwiat  haca  'va  sauAaite V, /<y,  i;  2—4;  —  hial  n3  'va  a^aur
3699:KompE.  —  Pü.:  ap7  zaiär  {!)  gSspand  . .,  erl. ; d»zd  H  zvrt  afii  Mrrl'-).  —  ')  Daher  DST. ZA.  2.  205:  'il  combat  pour  le  boeuf. .'  mit der  Bemerkung:  'expression 
3777:gaikaAü  tanusi^ä  Y.^J.  7-       2)  Praev.  (mit 'ak;gam-,  'bar;y/th-,  valn-  usw.).        a)  bei Ellipse  des  Verbums:   "wi?a  aparpm  (sd.) paiica    aparam    apnca  paurvaäbya    
4009:'nicht  hervorwachsend,  spricssend'. Pflanzen:  urvaranqm  . .  yä  para  ahmat histfitta  .  .  ^'yäntis  (NPf.)  hamaya  gätvS Yt.7J.SS-
4341:•  j.  an-ava'iiruxtay-"  f.  'Nichtbrechen des  Gelübdes,  Eidestreue'  (?):  yii  fnäml. data)  dahmayä  vauhuva  °C^ij"  Y.  70.3.
4385:•  j.  an-ahü-  Adj.  'der  keinen  Aha  (sd.) hat';  ahmaofanqm  .  ,  °ahunqm  aratunqm Yt.  /^.  I  o  5 ; — *anaKruA3i?)  ">  arafvS  acisifm duzanhavS  "das  Schlimmste  der  Hölle  i
4421:•  j.  an-ä'druxtay-  f.  1)  'Nichtliigen':  yeMe xsahräüa  nsit  aot?m  ai)ha  nSit .  .  para HSit  "unter  des  Herrschaft  es  nicht  Kälte gab  noch  . .,  vordem  dass  er  log"  Yt.
4592:•  j.  antar9.ka]»ha-  m.,  Plur.  Name  eines Gebirgs:  ahmat  haca  garayS  fraoxsyan  . . "tihaca  Yt  79.4.
4601:•  j.  antara.daöhav-,  °daliyav-  Adj,  (auch mask.)  'der  inmitten  des  Landes  ist': mi>nm  aiwi.daRyam  ..  '.ä/Sot  ( ASm.)  Yt lo.  1 44.  A)  m.  Name  eines  Berges  oder Gebirgs: 
4650:äahtmm  gä'^anqm  sraohrät  pairistaytili  N.^'<>;  —  mmS  ahuräi  mazdai  mmö N.4^;45^*fH.2.i3; — yd  'nyehe  dahmahe  amisaiibys spintaHbyS mmS'nyagsqm  asao- bansma  *frast»r3nfe  i
4653:vorausg.  nagclm  und  la-  'nicht  irgend  ein anderer';  naSclm  tsm  'nySm  yOsmat  vasdä asa  "ich  kenne  nicht  irgend  einen  andern als  euch,  0  Asä"  Y.  j^7">.  II  a)  mit AbL  des
4755:—  vTspe  vS  '/a  spmta  staota  zaota  .  .yüS- makim  yasnäica  . .  yat  'lanqm  spmianqm Vr.5.1;  2/,2,Y./2.i',  52.4,  Yt_).3,  4!.if.^ V-p:.i2,4ß,  *Vd.20,  V.  12,2;  —  äat  mrao
4767:ai.  amattya-  Adj.  »unstetblich'.   —    •)  Yl,  iS- 20  stehl  'ynn. p.  amäiaia :  s.  unter  ahma-.
4790:der  Richtung:  atcit  dim  aiwyäili'^^  ya dahma . .  ofritis  P.J2.  a)  'begehen,  (einen Weg)  gehen':  mä  dim  psrisS ..yim  xrvan- tim..pantqm  aiwitim^*'''  "frag  den  nicht, .  .  der
4855:.  j.  a-yaozdä-  f.  'Verunreinigung  Ver- . .  -  ayaBhö.Jyä-  Adj.  (mask.  -ya-)  'mit seuchung':  vT^pm  a  ahmat  'i^"  f 'dya\  ^^^^^^  (eisernen)  Sehnen':  vLlzah...
4970:aväjanam  |  *startä   akatiy  "vaiy  (als  AP.)  mä  dauitH 'vaiy  .  .  parsä  Bh.4'i4i  —  hauv  karam fräiSaytr  .  .  vivana^  nilwa"  pärs^  mann 6a!'dakaf'    karj'uvatiyä    xsa>
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  
5054:•  j.  ava(he  (indekL):  ihe  (sd.)  tha  yahna ahmai  av°   iha  yahna  ahmsi  avSya  iha
5055:lyahna  ahmai  Yt  75.63.  Sinnlose  Fluch- worte.
5270:frmmmfnd,    ?&.-.  frahrui-anlil^).    —    "3)^1311 *nh-al\  Btml,  IF.  ts.  :o6.  —  >*)  Pü.:  undeut- lich, wohl  Transskr. •  j..  g.  'ar-  V.  'gewähren'.     Praes.  10 snnav :
5383:•  j.,  g-  auruna-  'wild,  fenis,  saevus': maSsahe  kihrpa  'na^e  Yt.  l4- 23;  —  'na/a gairisiicö  sizdraca  ravascarätö  "die  wilden (Tiere),  die  in  den  Bergen  hausen,  und di
5453:•  j.  aratö.kar^^na-  AdJ,  'wofür  die  Er- füllung der  religiösen  Pflicht  bezeichnend ist',  von  Hamaspa^maedaya  (sd.)":  ha- maspahmaSdaim  "tum  Vr.  2.  z; —  kama- spdimaldaye
5594:acht Renoer", Name  cinesGebirgs*>:  ahmat\  j.  »arazah-  n.  'Abend':  yai  uHrSAva ha:a    garayl   fraoxiyqn  .  .    asta    'vants  m»r)neaite  (sd)  -zahva  bisasyät  V.2/.3. fitnkOfö 
5724:•  j-t  E-  (.  P-)  asan-iaj«-,  j.,  p.  asman-  m." i)  'Stein':  *ja«s(alsAP.)  äi/i{sd.)  maya  äiti darSii"V.g.  11;  —  'sSnaShia'^ ..  vtHiaeh-a' . .  tBiuxha  (sd.)  V,  6. 5 1, 
5732:hat,  wiiW:  yim  . .  aurvants  . .  viivSahS •ya  i'UEwiA' Y.  57- 27,  2)n.  (oder  f.  'yiJ-7) im  Du.  Name  eines  Bergs  oder  Gebirgs; ahmat   haca  garayö  /raox^yan  . .   'yaica
5752:•  j.  as9vi§ta-  Adj.  'der  die  geringste  Ge- walt, Stärke  besitzt,  am  wenigsten  vermag': asIS.vI^Stui . .  yahmathaca  nas"is  bunjaySt (sd.)  . .  «öiV  ai'irapatayS  nSit  dariku
5771:—  yai  nsit  sün}  .  .  a3atf/iqm  °tqm  .  . bannhm  (sA.) /rafasqn  V,  6.46;  —  'ti'a (AP.)  gaonaca  *dmi}'iaca  Ytij.  11;  —  yS süne  .  .  'tanqm'-''  (als  Obj.)  ahmarslanqm
5873:•  j.  asp9r«zö.dä'tama-  Adj.  'der  am meisten  Fürsorge  anwendet,  Sorge  trägt um  — '  (Dat):  ySi  *a»Am  nprtbyS  asava- byd  ayaptö.dahmasla  °masca  (statt  NPm.) "die  den 
5904:•  j.  asnvant-  m.  Name  eines  Bergs  oder Gebiigs":  ahmat  haca garays  fraoxsyqn.. 'väsca  Yt.  //).  5;  —  "vanlitn  gairJm  masda- <iSt)m  S.2.9;  —  'vaniahe'^  garSts  mazda- o�
6083:tl  cü  asra^fyanatn  tanunqm  'iahe .  .*vToiliti P-'i"**;  —  ndit..  "iahe  nöii  asayä  fräSmti (sd)  P.4J;  —  nöit  he  gäul  bvcU  nßit  'um oMt  "raola  ndit  vahUtö  ankui  Y
6084:(als  Subj.)3>  ya  'sät  gSUs  taiä  (sd.)  mraet Y.4/i.g;'~  mq'ir^m  yim  haurvatatS  'iahyä amsntätaicä  (sd.)  Y.gi.d;  —  kä  "iswöi 'iä  (Vok.)  äka  (sd.)  arpdrfng  isyä  Y.4
6339:•  j.  aäa,st9inbana-  m.  Name  eines  Bergs oderGebirgs:  ahmai  kala garayS fraoxyan .  .  'nasca  Yt.  ig.  5.
6583:—  yet'ikh  vS  aisS  ultrSMäniS  anhal  V, '  (auch  mit  dat.  Inf.) ;  Bj  im  Aw, :  mahmai 75.24; —  am?^anqm  sp^ntanqm ..  yaEsqm\hyättt  *ava>ihl  Y.50.J;  —  s3raos5  ilä asti  
6807:•  j,  aliu-mahrk-,  *ahü.in«r«nk-"  Adj.l5J.  a)  in  eiaem  andern  Kasus  als 'a^«/-a- (auch  fem.)  'das  (andre)  Leben  zer- , enthalten;  s.  dagegen  2.4:  aivä..akvä störend' " 
6900:•  j.  ahurana-  m.  Name  eines  Bergs  oder Gebirgs:  ahmat  haca  garayS  fraoxSyqn  .. 'nasca  Yt.  ly.  {.
6922:•  j.,  g.  ahma-,  g.  »hma-'>,  p.  ama-  Pron, I.  Pers.  Plur.  'uns'  (usw.).  Es  wird  ge- braucht i)  wenn  auf  dem  'uns'  (usw.)  be- sonderer Nachdruck  liegt:  *aia  nä  iixsta b
6923:—  ahmaräta-  396
6935:ahmaka-
6944:•  j.,  g.  ahmät  Adv.  I)  'inde';  i)  räumlich; nHt  käu  as  vaote  (sd.)  .  .  nBit  a'  vaiata ". ,  oon  inde  procedit"  P.  4^.  2)  zeit- lich, a)  'von  nun  an,  nunmehr':  ys 
6963:ausgehendem) cä:  ahmäkSiig  .  .  urunS pasukanqmcä  .  .  yalibyascä  tut  S  yas^ä agibyö  ä  at3k?n  ".  .  fiir  welche  diese  und welche  für  diese  dasind"  Y._jp.i.  a)  zu- gle
7034:kniipfiiDg  eines  adversativen  Satzes  'aber; sondern;  vielmehr;  gleichwohl':  iha  main- yete  dus:^armä  .  .  ä'  az3M  manya  Yt.  10. losf.;  —  nöil  .  .  vispa  yasathahs  .  .  
7042:—  jfff  ('wer'  sva,  'wenn  einer')  i/irar/i  zn aiwi.v?r)zyHti  .  .  ä"  aoxta  Tm  za  nara V.^j.aö.  8)  Ohne  Beziehung  nach  vom oder  zurück,  einfach  satzeinleitend: aoxta  sara
7113:*  j.  äxsta-  Adj.  'gefriedet',  nur  Plur.  ntr.  götthch*'  verehrt":  °tars  narim  jaitUi 'friedliche  Zustände,  Friede':  *a>a  »ä  'Ia  vilf  . . 'iars  {ÜS.)^  nanm  nsit  jainH
7151:ah'  m'  puhrsm  (statt  Gen.)  V.5.  2,  15.  | 45;  —  'trun'a  ioa  ah'  m'  pu^inm  yazo- maide  Vr.  lO.  i ;  Yt.  I().  46,  S.  2.  7,  9S,  Y. 2.4,  12,  /Ö.4,  /7,ii',  ifj.2,  25.7'
7223:—  V3r>-ir(^imn  . .  ya  . .  aca  paraca  pirs- saite  Yt.  j^.47.  2)  anschliessead  'dazu, dazu  auch,  und  auch';  aStS  sl  vSxs  .  . */ramrvqriö  ä  vacS  aAuriS  vairyö  fraoxtS .
7235:ahüm  fraparayeni  .  .  3  vakistat  atfhaot  a . .  as3t  a  . .  raocSby3  '^.ig.6. '  b)  zeit- lich :  fravasayS  . .  ya  kaca  gayät  marp^nat 3  saosyaHtät  vfrsiiraynat  Y.  s6. 10;  
7261:ya().         b)   eines  Nebensatzes:  yöi  nmäna kam.barSfnahi  (sd.)  .  ,  ätrsmca  .  ,  W  pas- ciota  ahe  nmänake  spä  vä  nä  va  in%yäi iüia  .  .  "wenn  wir  . ,  und  es  s
```


## [2026-09-07T18:21:49.223Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6918,6945p' BRT.txt | cut -c1-1200"
}
```


### [2026-09-07T18:21:49.272Z] TOOL RESULT

```
—  ')  Pü.  1  an  i  ahuränis,  eil. ;  armeil  11  caiti u  apärikci  äp  i  nämast;   s.  lU  maejtant-*). f.  aAureii  Yl.  ij,  99 :  lies  äAiiröü.
•  j.  ahurö.tkaesa-  Adj.  (fem.  'si-)-.  s. unter  ahura.tk'.
•  j.  *ahurö.pu9Ta-''  m.  'der  Sohn  des Herrn,  Fürsten':  asämni  .  .  abar»  (sd.) '"^rö  pu%rar»ha  basvar>patays  "den  Stein . .  trug  der  Herrensohn,  (trugen)  die . ."  Yt
O  NA.  gelrennt. j.  tthiiäl  N.  68:  liep  akunät;  s.  T. j.  ah!a  N,  4^:  lies  kala.
•  j.,  g.  ahma-,  g.  »hma-'>,  p.  ama-  Pron, I.  Pers.  Plur.  'uns'  (usw.).  Es  wird  ge- braucht i)  wenn  auf  dem  'uns'  (usw.)  be- sonderer Nachdruck  liegt:  *aia  nä  iixsta buyan  .  .  'm,li  (Dat.)  saoiäi  . .  u/n  ^fra- mainyäi  (sd.)  Yt.  if/.  3;  —  uUä  astl  usta 'mäi'^  hyat..  assm  (sd.)  Y.27.14,  a)  in Verbindung  mit  jiS:  pam  mtfsS  yatthö 'mäii'  np  sazdyäi  (sd.)  baoäaniö  pattT Y.  30.  2.  a)  bes.  bei  Gegenüber- stellung: daidi  sara'iiultrai  aojönghvat  ra- fmö  "maibyiicii  ..  Y.2,V.6*l;  —  däidi  a( nirqs  .  .  aiaHnaiihö    aidyUs    viistrying  .  .
—  ahmaräta-  396
\'niaifyä  ahmä.rafona»As{sA?)  Y, 4". 3;  —
i_fj  'mäi  gam  .  .  hSmJalat  at  höi  vSstrüi (sd.)  ..  Y.  47.35»;  —  'aeibyo  mal  as,i syazdat  yavqt  'mat  aurutiä  (sd.)  xra/strä Y.J4.9**; —  uzgpuniayeinti  zaslS  'mak^m ,  (GS.)  avaähe  yüsmäk>m  yasnahe  YL  13. 1 147;  —  s.  noch  unter  a,  a  a,  2)  vor I  einer  erläuternden  oder  ergänzenden  Bei- fügung; haxaya  •mäktm  saosyantqm  Yt. //.  17;  F.  7,  Vyt  J7; —  däyata  . .  mäva- yaca  zagere yaziinnai  'mäksmca  (statt  Dat) matdayasnanqm  fräyaztmnanqm  Y.  68.1 2; Vr. /2.  s;  —  haca  ahmät  nmätiift  "mä- kiiiua  mazdayasnanqm  "aus  dem  Haus hier  und  aus  (je)dem  von  uns,  der  M." Yt./_j.57;  —  s.  1.  a)  mit  relativischem .  Anschluss:  aom  narfm  .  .  yü  kasiSt?m  .  . \frSyatat  (sd.)  *°ma  (Akk.)  ^j-a"  atnisS sp?ntS  Yt  /.  24;  —  yUsmäk>m  yasmiica  . . \yqt  am^sanqm  .  .  'mäJhi/i  havaiiuhüua  ,  . ^yat  laesyatäam  Y.  14.  i,  Vr.  5.  i ;  Yt.  J.  i  f., I  FrVV.  I.  2 ;  -  's.  1 .  3)  sonst;  a)  D  im  Ap.
'  stets:  x^ai''a>n  tyaf'  hacä  'müxam  taumSy.l parübartam  äha'  Bh./.14;  10,  12,  13;  — '  hacä  pamriyatJ'  hyä  "mäxain  taumä  xsä- \ydhiyä  (sd.)  äht^  Bh. /,3;^f7ia-w  tysm \  'mSxam  *gU^avä  aväsiäyam  Bh.  1.  14; 1 14.  b)  im  Aw.  a)  notwendig,  sofern !  enklitische  Kasusformen  fehlen:  kii^ü I  drujwi  nis  °mal  ä  nts  näs'ijinä  (sd.)  \.44- j  13*>;  —  xrapaiil {s^.)  'mat  hyat  aibl  Y. \40.  i*';J5.S^'.  ß)  sonst  beliebig:  dazdi i  -makfin  (statt  Dat)  tat  äyapUm  ■  .  _f«:^a I  faän . .  Yt/o.33*>;  —  xsa>röi  höi  haun-atu '  amirftätä  'mäi  sU'i  dqn  (sd.)  t^-TÜ  Uta- [yain  y.45-io9i;  4y.i'°i;  —  pfrM,l(sd.)- j  ca  na  yä  tat  'mä  (Akk.) "  "'  parst.l  V, I4J.  10"';  —  ahmäi  paoiryö  äjasat  virf- I  "kraytiS  .  .  viitahe  k>hrpa  Yt  14.  2. '■  [N. /oj:  lies  hama^  Vgl  zu  vayam. '      KompA.;  Ableit.  — iFlex.s.S42J'J>-  —  ai..ij™i:/,
s.  noch  No.  2-10,  la.  —  ')  Mit  /  nur  Y.  43. 10;  s.  noch  N'0.9.  -    "'  ""     "  "■  "
)  Pü. :    .
)  NA.  :
)  Pli.:
aber  Pü.  und  ZDMG.  4S.IS0.  —  8)  Vgl.  da- gegen Yt.  J.  73.  —  W  Pü.:  ö  Ä.  —  "•)  Pü.: amäii  i'/s.ln.  —  n)  Im  Zitat  A.  J.  3  steht dafür  ahmäi.  —  ")  Pu.:  fa  An  pursiiii.  — 13)  Im  jAw.  scheint  der  DaL  durch  den  Gen. erseljt  in  sein  (s.  Y.  63.  12,  Yl.  10.  33).  vgl. IIa  als  Dat.  und  Gen.;  s.  jedoch  yiiima-.
•  j.  a-hmaräta-  Adj.  'nicht  zerkleinert': yü  süne  . .  astanqm  'tanqm  da<HiiH  "wer
dby  Google
»97
ahmaka-
einem  Hund  . .  nicht  zerkleinerte  Knochen
gibt"  V.7^.3.
Ar.  *rmj-ila-  (IF.  g.  261),  PPfP.  einer  Basis  anf (aj.)  I  i  [ih)  oder  i  'I.  VIL  zu  lett.  smaüs, Vit,  smiflkiis  'fein'  {luSji-  O'l-  —  Pü.;  a^^«- ür/  'nicht  zermahlen'.  —  ■)  Also  nicht  lu Ut  mfrdeö'.  —  >)  S.  noch  PesssoN  Wunclerw. II,  66.
j.  ii4>>)iii  F.  /  2.  St.:  lies  imäi.
•  ].,  g,  ahmäka-  Adj.  'unsrig,  unser':  tsm 'i,ns  azdibXscä  ustänätlcä  yasamaide  Y. .?7-  5;  —  pasBs  vTring  'kSTtg  Y.  45-  9 ;  —
,tÄ^  aat  urund  pasukanqmcä  "unsre Seelen  und  die  der  Haustiere"  Y.jp.  i; —  'kiin  nqma  .  .  yat  ampsanqm  nqma Yt  /.  3.  a)    Plur,    'die    Unsrigen';    yS
mafvSng  cixätulö  °k}ng  gJus  bagä  i^är^mnö I sd'>  Y. .;:;.  8.
Pi.  (za  y.  4Sy-  •  "i".  (lu  Yt  /):  i  ämSi. (iu_Y.j7.Ji,):    ia«.äian.    (lu   \.  32):    amä-
•  j.,  g.  ahmät  Adv.  I)  'inde';  i)  räumlich; nHt  käu  as  vaote  (sd.)  .  .  nBit  a'  vaiata ". ,  oon  inde  procedit"  P.  4^.  2)  zeit- lich, a)  'von  nun  an,  nunmehr':  ys . .  kayä (sd.)  a°  . .  7'ästryä  Y._jy.6;  — yä  a°  staota yasnya  irävayeni  "indem  ich  nunmehr  die StY.  aufsage"  Ny.4-S-  b)  mit  folgen-' dem  ya^a  und  fiiL  Konj.  'doncc,  bis  dass': aU'it  a'  yaha  ap?mgm  maniva  an  Aat mz'Ji/is  (sd.)  Y. 10.16.  U)  beim  Kompar., wörtL  'als  das',  was  i)  vorausgeht  oder 1)  folgt;  meist  unübersetzbar,  i)  zurück- weisend auf  zuvor  Genanntes  oder  Ge- sagtes: imaj  vS  jatöyemi  .  .  yalca  a°  asH miirya  ".  .  quodque  hoc  est  maius"  Y. 'jj.  14;  14'i  —  saisisca  .  .  oAqxitäiscä *ß-äyjblscal(sA.)ca  a-  Vr.  Ä  i.  a)  in Verbindung  mit  eil :  ayaaAaUtäis  kan- täis  paiti  azdibis  avaJitriäiyilt  {%^)  masyd vü  'mii-'i/V. 4. 50;  51,52.  2)  voraus- weisend auf  einen  Nebensatz  mit  &)yd:ia: yifnö  zqm  visävayat  afvit  irii'va  a'  mas- yefäm  ydia  fara  ahmai  Y.  2. 1 1 ;  —  nüit il  a-  *drajyS  *yätltn  framraemi  (sd.)  .  . äfrOIm  .  .  ya>a  .  .  V.33;  Yt. 
"ahmi  298
```


## [2026-09-07T18:22:06.758Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 1966 asphalt/asbestos/atom ===\" && grep -n \"asphalt\\|asbestos\\|^atom\\|atom, n\\.\" KLN_1966.txt | head -10 && echo \"=== KLN us/our p1683 ===\" && grep -n \"^1683\\|1683\" KLN_1966.txt | head -5 && echo \"=== KLN us, pron ===\" && grep -n \"us, pers\\.\\|our, poss\\|OE ūs\\|OE ǖs\" KLN_1966.txt KLN_1971.txt | head -10"
}
```


### [2026-09-07T18:22:06.862Z] TOOL RESULT

```
=== KLN 1966 asphalt/asbestos/atom ===
2192:Alhambra,  n.,  the  palace  of  the  Moorish  kings  at Granada.  —  Sp.,  fr.  Arab.  ( al-kal'at )  al-hamrd’, ‘the  red  (castle)’,  fern,  of  ahmaru,  ‘red’,  rel.  to hammara,  ‘he  dyed  red’,  humrah,  ‘redness’,  Heb. hemdr.  ‘bitumen,  asphalt’  (so  called  because  of its  reddish  color),  hamdr,  ‘he  covered  or  smear¬ ed  with  asphalt’,  hdmer,  ‘mortar,  clay’  (so  called from  its  color),  Heb.  hdmdr,  Arab,  himdr, Aram.-Syr.  ijamard,  Akkad,  imeru,  ‘ass’,  lit.  ‘the reddish  brown  animal’,  Heb.  yahmdr,  Aram. yalfmurd,  Arab,  yahmdr,  ‘roebuck’  (also  named from  its  color).  The  Alhambra  was  called  ‘the
2475:amianthus,  n.,  name  of  a  kind  of  asbestos.  L. amiantus,  fr.  Gk.  afnavrcw;  (scil.  ALiV,-),  lit. ‘undefiled  (stone)’,  fr.  <4-  (see  priv.  pref.  a-),  and piavTo^,  ‘stained,  defiled’,  verbal  adj.  of  tuodvetv, ‘to  stain,  defile’ ;  see  miasma.  The  spelling  th  (for t)  is  prob.  due  to  the  influence  of  Gk.
3579:asbestine,  adj.,  pertaining  to  asbestos.  —  L.  as- bestinus,  fr.  Gk.  daJ^aTivoi;,  fr.  Sapeaxoi;.  Sec next  word  and  adj.  suff.  -ine  (representing  L. -inus).
3580:asbestos,  n.  —  L.  asbestos,  fr.  Gk.  Sapearoc,  lit. ‘unquenchable,  inextinguishable’,  fr.  A-  (see priv.  pref.  a-)  and  opeaT^c,  verbal  adj.  of oPewivai,  ‘to  quench,  extinguish’,  which  derives fr.  I.-E.  base  *gwes-,  ‘to  quench,  extinguish’, whence  also  Lith.  gestu,  gisti,  ‘to  go  out,  be extinguished'.  OSlav.  gaSp,  gasiti,  of  s.m.,  Hitt. kishtari,  ‘is  being  put  out’,  Toch.  A  kas-,  B  kes-, kas-,  ‘to  go  out,  be  extinguished’, asbolite,  n.,  a  mineral  containing  oxide  of  cobalt.
3656:L.  asper,  ‘rough’.  See  asperity, asphalt  also  asphaltum,  n.  —  F.  asphalte,  fr.  Late L.  asphaltus,  fr.  Gk.  HayoXxoc,,  which  is  of  un¬ certain,  possibly  Sem.,  origin.  See  Heinrich Lewy,  Die  semitischen  Fremdworter  im  Grie- chischen,  Berlin,  1895,  p.53.
3657:Derivatives:  asphalt,  tr.  v.,  asphalt-ine,  asphalt¬ ic,  adjs.
3861:atom,  n.  —  F.  atome,  fr.  L.  atomus,  fr.  Gk.  axop.04, ‘atom’,  prop,  ‘uncut,  indivisible’,  fr.  4-  (see priv.  pref.  a-),  and  -xopop,  fr.  xspvetv,  ‘to  cut’. See  tome  and  cp.  anatomy.  The  word  axop.09 was  first  used  by  the  Greek  philosopher Leucippus.
3863:atomy,  n.,  skeleton.  —  From  misdivision  of  ana¬ tomy  into  an  atomy.  See  anatomy, atomy,  n.,  pygmy.  —  L.  atomi  (pi.  of  atomus, ‘atom’),  mistaken  for  a  singular.  See  atom, atone,  intr.  v.  —  Short  for  ‘to  be  at  one’.
5090:bitumen,  n.,  1)  asphalt ;  2)  an  inflammable  mineral substance.  —  L.  bitumen,  ‘mineral  pitch’,  an Osco-Umbrian  loan  word  (the  genuine  Latin form  would  have  been  *vetumen,  fr.  *gwetu- meri)  of  Celtic  origin;  cogn.  with  OI .  jatu,  ‘lac, gum’,  ON.  kvada,  ‘resin’,  OE.  ewidu,  cudu, ‘mastic,  cud’.  See  cud  and  cp.  beton.  Cp.  also Be  tula.
=== KLN us/our p1683 ===
31848:Reaumur,  adj.,  pertaining  to  the  French  physicist Ren6-Antoine  Ferchault  de  Rdaumur  (1683- 1757),  or  to  the  thermometric  scale  invented  by him  in  1731.
39754:tracheotomy,  n.,  incision  in  the  trachea  (surg.)  — Coined  by  the  German  surgeon  Lorenz  Heister (1683-1758)  in  1718  fr.  traeheo-  and  Gk.  -xopia,
=== KLN us, pron ===
```


## [2026-09-07T18:22:07.798Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB amah ===\" && grep -n \"amāh\\|amah\\b\\|LNE\" NYB_vol2_glossary.txt | head -15 && echo \"=== NYB asem ===\" && grep -n \"asēm\\|asem\\|ʾsym\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-07T18:22:07.855Z] TOOL RESULT

```
=== NYB amah ===
374:amah [LNH, Prth LN] pers. pron. Ist. p. pl. 1. cas. rect. we: —-ic... āyēm 913-14; to —-ic dāt hem we have been created by thee 397; ētšān (v.s.v. 04) ~ hem ke 5778; - an, ~ an: v. lan. — 2. cas. obl. us: a) dir. obj.: —-ic äkäh framāi kartan please let us know 11%; — martoman 11%; ~ (twice) proleptic obj. of zanišn 409-7; — b) virtual dat.: franāmišn ~ we must proceed 405; ~ ap i tē pat kar ne apāyet we have no need of your water 14?3; 191-2; — c) the agent of a pret. pass.: pas =: framāt HajB:11; HajA: 5.10 (Prth LN); ~ ētēn āšnūt ku 34, ete.; - d) i ~ our: dar i ~ 39, etc.; e) after a prep.: andar, apük, o ~. — Av. (295 sg.) gen. ahmākom, OP amāzam; MPrthPrs ’m’h; Paz. ema; NP ma. V. also -màn.
1083:to], amāh-tc, ké-c, ka-c (ka vas-ic v.s. v. ka), bē-c, apar-ic, ö-c(i), pat-ic, peš-ic, hac-ic; hac hàn bē tarsēh-ic 4812; ete.; in
1524:framätan [inscr.], framütan [plmwt'n] framäy-, imp. sg. framäi 10% ete. and framäye [plm’dyd 923,plm? dh 272, plm’ - dyw 5725]; pres. 2d p. sg. framdyé [plm’yh 64, plm’dyh 244]; 3d p. sg. = 2nd p. pl. framäyet 141°, 261° [plm’dt!, ef Ps. hwéty and ywdty 1289, v.s. v. hošitan and yöd-]; Ist p. sg. and pl. framdyém [plm’dym]; pt. = pret. pass. 3d p. sg. inser. framät [prm*t, plm?t; plm’ty P2:4], in the books framüt: to order, to issue an order, to command, to bid, with 6 of the p. to whom (3725-27), and rād of the p. concern- ing whom(219?)the order is issued; with a dir. obj. of the ordered th. 38. 64. 199%; apt-t pasēh framayém karkäs and we shall order the vulture (after thee —) to pursue thee 604; mā man 6 pasčh framdi do not bid me to turn my back 5774-75; — to please to, to deign to, with inf. 1122-26, 149; — kar framutan = kar kartan 27, v. kar; — the order itself is expressed 1. in dir. speech by an imp. introduced by ku: framut kū "nikēr” 45; 1213. 33%; consequently, in 216 (framut ku ...) ‘BYDWN-x, and in 109? YDLWN.x; should be taken as the imperatives kuné and baré; — 2. by a subordinate clause a) with kū + pres. ind. 313-5; b) with tāi + pres. ind. 129-19; c) after the pret. framut, with ku tài + opt. pass.: 217-18; d) introduced by the rel. pron.: amah framatké ... cit” we ordered someone (an
1795:hamāhakēh [hm’hkyh]: better hamaxakeh, g. v. hamäi [hm’y] 318. 952°: v. hamäk.
1797:hamak [hmk] whole P1:8. — KZŠPrth hmk = Prs hmky = Ps; MPrth hmg (A-H III); NP hamah. Av. (1713) *hama-.
2104:daughter of this farmer 1518-19; Frašāvart i tē pus 2319; pus + mas i Ardavàn 319; vasün martom + andar gehän 49; vas xuähisn i rāpak-karihā xudhet 746-2"; if more than one relative attribute is added the izāfat is repeated before each: 735 etc. ; 2. paraphrased by hàm i (én i, ēt 4, õi 1) and placed before its head w.; this is the definiterelative attribute: häniZar- tuxšt mätist 3612; han i težtom tap 4322-23; ete.; — forming possessives: a) placed after the headw.: 4 man my, % tē thy, 4 amāh our, % šmāh your, but in the 3d p. the encl. pron. is used: 2-5 his, her, 2-Sän their; b) plaeed before the headw. as a definite relative attribute: hàn % man pusar 51?!; & i to humat 78-16; han 7-8 burtär 43%; hàn i amah dēh 5072-3; han + či vēh-dēn 515, ete. — forming the genitive of the interrog. kē: % ke? han + kē? whose?; other constructions with the izäfat, v. the demonstr. pronouns; — after adverbs used as prepositions: peš 4, hacadar 4, hacapar i, miyān +, ete., but the MSS are very little consistent in this respect. — The limit between nominal relative clauses and relative attributes is sometimes floating. — Av. (1199 sqq.) ya-; OP ya- rare, commonly hya- (haya-
2183:Kāmak-vaxšišn [—-whššn'] n. pr. one of the seven heroes who will usher in the fraškart 1069-18, — Av, (1431) Vouru.- nomah- Yt. 13128; on kāmak for vouru- v. the preceding w. Usually vaxsısn is emended to niyäyisn (g. v.) in order to obtain congruency with namah- (v. na- mac), but I do think we should retain vaxsisn, which is attested by all MSS: ‘from whose will growth (or increase) arises’, as the counterpart of Kämak-süt ‘from whose will beneficial works arise’.
2208:kar [k'1] work, act, deed (also evil), busi- ness, errand, matter, case, task, cas. obl. kārē [k'ly], käreh [k'lyh] (ef s. v. karp); with indef. art. kār-ē [k'14-1] anything 1122, something 104°; pat kār-ē for some business 1417; 3511-14, 5027 etc., passim; — 6 butan i ham-ic kārē frahaxtak in order that all might be instructed in this matter (viz. in the new religion) 10811; pat martom käreh through human work (= as far is humanly possible) 1172; — ~ framiitan to bring about 19%; ~-om tō framāyē do thou thy duty to me! 2722; amāh dp i tč pat ~ né apäyet we do not need thy water 1423; 375-5; andar 6 ~ kartan to begin using regularly 9614; pat én ~ ku with the commission to ask: “.. — often coordinated with another notion so as to form a hendiadys expressing that the notion is put into practice: ~ u kirpak (work and religious virtue =) meritorious religious deeds 13% and passim; ~ u dätistän, v. this w.; ~ u räyenisn prac- tical function 87? (in this construction u is very often wanting in MSS and edi- tions); — šahrē -än (pl. cas. obl.) “‘state- work" — penal servitude, forced labour 92; zanč ~-dn 834 v.s.v. zan. — = NP. Av. only in the adj. kära-vant- (465); on OP kära- v. kürécür. — V. also a-kär, dast-kārēh, "ham-kär, kām-kār, kār-dāk, kàür-nàmak. ' > god
2347:kurušk [kwlwšk'] ewe, of a big species of sheep 509-11, — Zsprm X, 20 in telling this story: meš kurušk i šīr-pistān "with milk in her udder’. Also kwryšk' = Paz. kurišk, koriák, BdA, p. 959-1? = BdJ2918— 303: meš 5 sratak: han i pat-dumb, han 4 a-dumb, u sak meš, u meš *takilé [tkly ; Paz. tagr, tgar] <u> kurišk tmeš, ke srub vazurg, asp homänäk, 3 köf [BdA corrected from tan, BdJ Paz. koh] dārēt api-š 6 bārak girénd, cigēn gobet ku Mānušcihr + amāh niyak kurišk-ē pat bārak dāšt [sak
2465:martóm [mltwm; "NSWT?] 1. in an in- dividual sense: a human being: ~ hom 62°. 631; pl. cas. rect. ~: šmāh kē ~ het 67°; har ~ aed mat to everyone came a message 208-9, — 2. ~ in a collective sense: man, mankind, men, people; when subj., mostly construed as a pl. (thus serving as the pl. cas. rect. of 1): ka hamäk ~ avinüs bē bavénd 3412-13, 672, 961-2, 9717-18 (constr. ad sensum): 19. 104°. 10618-19, 12021, but ka Krisäsp kār (ag.) martöm (subj.) özat but 351, and thus 327. 9516. — 3. with the pl. cas. obl. ~-dn [mltwm’n', "NSW'T^-n']: a) gen.: andar tant ~ -än 65°; ~ -dn nē dänistan ... rād as men do not know 8016 etc.; — b) dir. obj.: ~-an pat kunisn girend 652, ete.; — c) dat.: dišop ... but 10718 sq.; as the logical subj. of an impers. pred.: ~-dn pat én 3 rah saxt estisn men must keep steadily to these 3 ways 65977; ~-dn ... dänistan nē tuvàn 8045; ~-n ... Süyet x"astan 891-2; — d) agent: —-čin guft ku 15-16, ete.; — e) after a prep.: hac ~-Gn 7?!; passim; — f) secondarily as the cas. rect. pl.: 58. 69-19 etc. passim; — as the app. of a pl.: amah c--ün 11%; astömandän ~-dn, viturtan
2514:crowd of Iranians who used to come there, to the court of A. the Khionite 616-7; puhl ... ke har ahlav u druvand avis ~ the (Chinvat) bridge to which everyone, pious or wicked, inevitably comes 7213; *kas-ip (g. v. amäh meneč ... ku “har- visten matür hom pat zanišn", nē amäh &t6n-ic harvisten matàr he 6 zamišn how- ever much you may think about us: ‘‘[I am an unavoidably-total-comer-to-slay =] I shall unavoidably come and slay (you) totally", yet you will never attain to slay us totally 469-5, with the gl. kū-t etón nē apasihēnītan i apāc nē bavēm ‘that is: it is not for thee to destroy (us) so utterly that we shall not come back” (the first amäh is the proleptie obj. of the first zanišn, and the second amāh of the second zanišn; however, as the author passes to direct speech after menč the dir. obj. of the first zanısn ought to be $mäh, so the first amäh lacks all connection; harvistén (g. v.), virtually a qualifier of zantšn, has been combined with matdr as its attribute).
2556:mihr [mtr'] 1. n. pr. the Aryan god Mitra, Av. Midra: ~u Srēš u Rasn 1215; ~ u Zurvān i akanārak u menčyč datistan 77-12, ~ zg"'"atài névak, Dahman Afrin 9213, ~ yazét u x"aršet 961! ; atur burzen ~ the third of the three imperial fires 11%. 2°, symbolizing the class of the cattle- breeders and farmers 2° (cf Av. [1430] Midrē yö vouru.gaoyaotiš); — existing in all animal beings 965-%; — Dadv pat ~ the name of the 15th day of the month 9715-16, — 2. the sun 78. 317. 7913-18, — 3. abstr. friendship, loyalty: — u došaram i apāk čišan 87°; ~ + amāh 98; ~ i čvak 6 dit 119; vehän ... ~ däst u dosteh varzit 5526-27, — Av. (1183 sqq.) midra-.
2626:1418, 1820, 1927. 35? (be o). 104! (pat). — Av. (1069) namah-; MPrthPrs mmc; FrP 19 *SGDH = nm’c, but Cod. 8, XVII, 7 nm'š with NP gl. namäj; Paz. namāž; NP namaz.
3228:ramak herd 50°. — Arm lw. eramak; NP ramah, ramak. V. hu-ramak.
3788:Pärsikän ... fréstit thou hast been sent by the Persian king 1319-1? (for frēstīt he); cē-šān tö-c kust 27° (for kust he; or perhaps an absolute clause: after thy having been slain by them); but kē tē dat he? by whom hast thou been created? 577-5; eoordinated with another pers. pron.: man u to āzmāyišn kuném 4); to an [LK 'NH] ... barom (for barém) ‘thou and I (we) shall...” 5319-20-24), v. s. v. arža- nikenitan; — 2. dir. obj.: né tčy-ic pat depahr därem 21%; mā ziön . . . to dzanénd 2612, 2912; tài to giram (v. gir-) 35°; etc.; — 3. to, for, against thee: har vat kas to nē tuvan kartan is not able to do thee any harm 6!9-%; tē ce vinās jasi estet? what sin has befallen thee? (v. jastan) 1211, 5317; nē tö u ne héc dam i man ästisn nē būt hah there would have been no permanence for thee, nor for any crea- ture of mine 3515-16; beginning the sentence and taken up later by the independent form of the encl. pron.: töy-ic kë vat hah at tar menčt 331^; — 4. agent: to nē dānā- kihä kart 419-11; to amāh-ic dat hem 39"; tē zat mar 1 Tür 99??; ete.; — 5. gen. a) dam i to 335; b) det. rel. attr.: 6 õi % tē pusar 51%; et i to pus 5218-14-15; eto.; c) tē brat 2211 etc.; to mät 227%; to pus 5116; — 6. with prep.: apar tē, hac tē, 6 to, pat to, tē rād. — 51% ZK-p tw: read an-ip to as a sort of ethic dat.: ‘thou mayest understand’ or the like, with an empha- sizing tē, v. lan B; v. further s. v. -p. — < tava, Av. (787) gen. of (786 sqq.) Owa-, OP 0uva- ; the cas. rect. Av. (661) tvēm < tuvam — OP, which would have develop- ed into *tū in Milr, has been absorbed by to, as far as we can judge. MPrthPrs tw, with -c: twy(y)c; Paz. 0o, Ou, tu (0 has no etymological value); NP tū. Cf -t and at.
=== NYB asem ===
668:asēmēn
682:asēm [sym] silver 118%. — Borrowed from Gr &onuov; MPrs ’sym (A-H II); NP sim.
3254:rasitan [lsytn'; YHMTWN-tn', ~-ytn'] ras-, pres. Ist p. sg. rasam [YHMTWN-m 2917], lst p. pl. rasēm [YHMTWN-ym 62. 197] ete., subju. 3d p. sg. rasät [YHM- TWN-t' 412]; pt. = pret. 3d p. sg. rasit [YHMTWN-t', YHMTWN-yt' (coin- ciding in spelling with pres. 3d p.sg. and 2nd pl. in -é)]: to arrive, to attain; to reach, to come (0, be 6, 6 peš 4 at, to); to fall to one's lot (6); passim; — andar rasit came to the place 31%; be 6 han i asar rošneh ... apar rasét he ascends up to the Endless Light 73?’ sq.; rasét apar 6 haft- kišvar damik will extend all over the sevenfold earth 51°; apar — to fall upon, to come upon, to assault 197. 726-7; — 6 ham ~ to come together, to meet 431’. 5017, 6122-25; — ruvän + ahlavàn pat buxtan
5811:’sym: asem
7322:pašīmān, pišmān, pižmān, pašīmāni, pišmānī: pasēmānēh
7393:sim: asem
```


## [2026-09-07T18:22:42.057Z] TOOL CALL #37: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1931 2>&1 | head -60"
}
```


## [2026-09-07T18:22:44.387Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD ne/nes ===\" && grep -n \"nes-\\|nos-, nes-\\|ns-me\\|nsme\" WLD_band3.txt incoming/WLD/WLD_Bd2_pages.txt 2>/dev/null | head -10; echo \"=== LEW in- ===\" && grep -n \"^in-\\|in-,  \\|in- (2)\\|in-  'nicht'\" LEW_1910.txt | head -10; echo \"=== SKT us/our ===\" && grep -n \"^us\\b\\|^our\\b\\|us, pron\\|our, poss\" SKT.txt | head -10"
}
```


### [2026-09-07T18:22:47.489Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 14; check the printed number and re-run with --pdf-page if off)
REF: BQT:1931  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 14  OCR-lang: fas

از کناب بردان قاطع درحرف میم با حروف تجی مبتنی
بر بیست و هشت بیان و محتوی بر بك هزاآر و یست
لذت و کنات
بیان اول
در میم با الف مشتمل بر دوست ید چهارده لغت و کنایت
ات ماپروین ۱ « بابای فارسی,مخفف ماه پروین است وآن بیخی باشد که دفع سموم
(۱) خم ۱: دوصد .
م (میم) - حرف بیست وهشتم از الفبای فارسی و حرف بیست وچهارم ازالفبای عربی
( ابتث ) و سیزدهم از حروف ابجد » و در حساب جمل آنرا چهل گیرند . این خر فگاه به«ن»
پدل شود . - م ( مفتوح ) 332 چون برسر فعل امر درآید » نمی سازد : مگوه مخور » مزئیده
ولیز برسرقعمل دعائی‌درآ ید : مباد, میادا. رلد: هه - لیز۱م؟ ضمیراول‌شخص مفرذباشد(رك : دبباچهة
موّلف س‌بط - که کو ) » درپهلوی 50 ( ضمیر اول شخص مفرد) « اوئوالا 4۹۳ >.
۹ - رك : ماه پروین . ۰
ما - پهلوی 2۳020 (ما) » پارسی باستان 2۳327)270 » اوستا 13822۳908 2اوراق
تورفان 2783211 « نیب رکه س ۷ > . پازند 6032 , هندی باستان - 2970462 « اسشق ۹۵۵ 6
استی ۶332 که . است ۱۲۹ » در لهجهٌ بهودبان ابرانی 2732 ۰ کردی 326 » 38 ۰ 126
« ابا س 4*۹ > شهمیرزادی وگیلکی 3002 » دزفولی 01300 » خواناری 832102 « سالنامة
کلیایگان ۶۷ > . رك : دارمستتر . قبعات چ۱ ص ۱۱۱ ۰۱۱۲۰ ۱۲۸ ؛ ضمیر اول شخص‌جمع
( متکلم مع‌الغیر ) وآن ضمیر منفصل است ,گاء در حالت فاعلی باشد :
ما نگوییم بدو میل بناحق نکنیم جامةٌ کس سیه و دلق خود ازرق نکنیم.
« حافظ شیرازی ص ۲۹۱ ۰
- وگاه در حالت مفعولی : ما راگفت - وگاه درحالت اضافی :
چو بنیاد ایجاد ها برفناست بمر گك کی شادمانی خطاست.
سمدی شیرازی . رك : دستور قبفهی ج ٩ص‏ ۹2۸۸
```


### [2026-09-07T18:22:47.568Z] TOOL RESULT

```
=== WLD ne/nes ===
WLD_band3.txt:3049:| on i 8 333, Geicht 2 Lier 00, Cspot aasigy Le 374°. gespronkelt 2, perk". ine : Gestalt 136, t A. grep- 436. ao, “ Gf. gestalten. 1. g*er- sat gebogenes Lae aryu- SI. 7 Sas geborgen acin nes- 394", gelingen qou- 457. Gestoll (Latten) grom 487, gebrauchen  bAriig- a 2. epé[i)- 650". | gestern _ Palitpjes- O04, okechen jAal- 54D geloben pS Pr treift =. rea pests a) 270 spend y a pari p eu. 501. mit a ey am Fup. | gelasten newdh- 326", a lim*, knéehel — aprwro-ehgg* | eelten ghelt- 632, | geetutet muloe 312°. os bss 9. a dp- 47, | Bemiistet : mad- 230°, | gesund eetliapts -ond- 63 F re as mere
incoming/WLD/WLD_Bd2_pages.txt:5685:(qen-)j genes- „kratzen".
incoming/WLD/WLD_Bd2_pages.txt:15573:hiehergeborige Sippe fiir „Mond“, s. ^menes-^ deutet er als ,,qul Qnutahir^^).
incoming/WLD/WLD_Bd2_pages.txt:17837:                                            menes-                                          ^71
incoming/WLD/WLD_Bd2_pages.txt:17875:inenes- [mens-] der nom. sg. '^mens wurde            und menot „Monat'‘.
incoming/WLD/WLD_Bd2_pages.txt:21137:^d20                                                       ne-, no*, nes-, nos-
incoming/WLD/WLD_Bd2_pages.txt:21179:lie-,    no-, plur. nes-, nos- ,,wir" (ursprgl. auBerhalb des Nominativs;                                          Nom.
incoming/WLD/WLD_Bd2_pages.txt:22087:334                                    ner-'   —   nes-
incoming/WLD/WLD_Bd2_pages.txt:22134:nes- „angenehm, gliicklich wohin gelangen“, auch                vom Geborgensein im
incoming/WLD/WLD_Bd2_pages.txt:22181:zweisilbigen Wz. enes- damit zu vereinigen sei.
=== LEW in- ===
=== SKT us/our ===
6318:us,  unholy;   lit   before  (i.e. the  tcmpIcL.  //u,  before; a  temple.
16293:our.  (F.  -  L.)  M.  E.  rumour.  - nifr.  vL.  ace  rMWffrfm,  from  rumcrt t,  murmur.  Cf.  L.  rumifan,  to reports.  —  ^  KU,  to  make  a  hum- use.  *  See  Bumble. p.  (Scand.)  M.  E.  rumpe.  -  Tcel. Sweid.  rum/Of  Dan.  rumpe.  4*  Dn. 'the  bulke  of  a  body  or  corps,  or without  a  head;*  Hexham, pie,  to  wrinkle:  eec  Bipple  (3). (E.)  M.  E.  rinmn,  pt.  L  ruM,  pp. ^  fimw  :  A.S.  hnnan,  pt.  t.  niHM, Vmmem ;  also  found  in  ^he  tran^poscil Itam,  pL  t.  arw.  +  Du-  rcnn^H.  Iccl. Dan.  rintU.  Swc<t.  rinua,  Golh. e  G.  ttHtuH.  Allied  to  SkL  riiufini. iae,  n,  to  £o :   L..  0r>in',   to  rise.
20492:our.  (E.)     A.  S.  tire,  of  tts ;  gen.  {4. utt,  we.    This  gen.  pi.  became  aj and  was  regularly  <lecUned  as stands  for  ds-trt  *  -^  Goth,  maaro, of  Goib.  nvu.  we.     Dar.  €^r4,  A. our-setf,  ourselves. Use.  sb.  (F.-1-)     ME.
```


## [2026-09-07T18:23:02.896Z] TOOL CALL #39: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1931 --image 2>&1 | tail -20"
}
```


## [2026-09-07T18:23:04.013Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21100,21180p' incoming/WLD/WLD_Bd2_pages.txt | cut -c1-300"
}
```


### [2026-09-07T18:23:04.183Z] TOOL RESULT

```
ات ماپروین ۱ « بابای فارسی,مخفف ماه پروین است وآن بیخی باشد که دفع سموم
(۱) خم ۱: دوصد .
م (میم) - حرف بیست وهشتم از الفبای فارسی و حرف بیست وچهارم ازالفبای عربی
( ابتث ) و سیزدهم از حروف ابجد » و در حساب جمل آنرا چهل گیرند . این خر فگاه به«ن»
پدل شود . - م ( مفتوح ) 332 چون برسر فعل امر درآید » نمی سازد : مگوه مخور » مزئیده
ولیز برسرقعمل دعائی‌درآ ید : مباد, میادا. رلد: هه - لیز۱م؟ ضمیراول‌شخص مفرذباشد(رك : دبباچهة
موّلف س‌بط - که کو ) » درپهلوی 50 ( ضمیر اول شخص مفرد) « اوئوالا 4۹۳ >.
۹ - رك : ماه پروین . ۰
ما - پهلوی 2۳020 (ما) » پارسی باستان 2۳327)270 » اوستا 13822۳908 2اوراق
تورفان 2783211 « نیب رکه س ۷ > . پازند 6032 , هندی باستان - 2970462 « اسشق ۹۵۵ 6
استی ۶332 که . است ۱۲۹ » در لهجهٌ بهودبان ابرانی 2732 ۰ کردی 326 » 38 ۰ 126
« ابا س 4*۹ > شهمیرزادی وگیلکی 3002 » دزفولی 01300 » خواناری 832102 « سالنامة
کلیایگان ۶۷ > . رك : دارمستتر . قبعات چ۱ ص ۱۱۱ ۰۱۱۲۰ ۱۲۸ ؛ ضمیر اول شخص‌جمع
( متکلم مع‌الغیر ) وآن ضمیر منفصل است ,گاء در حالت فاعلی باشد :
ما نگوییم بدو میل بناحق نکنیم جامةٌ کس سیه و دلق خود ازرق نکنیم.
« حافظ شیرازی ص ۲۹۱ ۰
- وگاه در حالت مفعولی : ما راگفت - وگاه درحالت اضافی :
چو بنیاد ایجاد ها برفناست بمر گك کی شادمانی خطاست.
سمدی شیرازی . رك : دستور قبفهی ج ٩ص‏ ۹2۸۸
```


### [2026-09-07T18:23:04.220Z] TOOL RESULT

```
  air. ne-ch „aliquis^^, cymr, nep „quispiam‘‘ (= ai. nahis „niemand“, aber
mit Abstreifung des negativen Srnnes in Satzen mit wiederholter, aber
einander nicht aufhebender Negation; derselbe Vorgangin lit. neTcds „etwas‘‘,
neMirs „quidam“, neJcadd „zuweilen“; ahnlich gelangte ^ne-iie .,oder nicht'‘
zur positiven Bed. „oder“ in:) air. nd^ no^ nn^ nfi^ cymr. nen, abret. non
..oder“ (s. Thurneysen Hdb. 500, Brugmann II ^ 3, 977, 988), womit Thur-
neysen KZ. 48, 53 die verbale Stiitzpartikel (fiir Pronomina infixa und das
relative -n-) air. no-^ nu-^  mcymr. ne^^- gleichsetzt als ursprgl. formelhaft
vorgesetztes „oder nicht?     deren Yerbindung mit "^nft „nun“ demnach auf-
zugeben ist; proklitisches ^ne ergab ^na (wie z. B. ir. ass- .,ex‘') im Yor-
ton in der Yerbindung air. na[ch\ mcymr. nac (usw., s. Pedersen KG. II
252 f.) „nieht" aus '^ne-q'ie mit urkelt. Apokope des ausl. -e (nicht nach
Trautmann Grm. Ltges. 67 mit idg. Ablaut aus nQ-cpie)
      got. ni. ahd. as. w?, we, ags. ne „nicht‘^                                 aisl. we, ne      in der nur poet. Bed.
.,non'\  wahrend ne in der Bed. „neque“ (nach Neckel KZ. 45, 1 ff.) = got.
nih (gleichbed. mit 7ii geworden; zum Lautlichen s. Brugmann IF. 33, 173),
ahd. nih-em, as. (mit gramm. Wechsel) nig-ni „kein“ (aber as. wee „und
nicht^' = lat. neg-^ s. o. iiber got. nauh^ ahd. 7ioJi s. u. nd „nun‘*); ahd.
                                              ;


wem,         as.    nen      „nein‘*        aus          -r-   oincnn       nicht einer^*        fs.   o. lat.   ndn^ nuUtts);
ags.     na        j^nie,    nicht, neim',             engl. no          .,nein'‘    (auch     —       trotz   Falk-Torp's u.
nei Zweifel                —       aisl.    nei   .,nein“        aus            -f      — as. ahd. nio „nie‘').                   Lit.
ne „nicht“,               ncJccis^    nekurs^ nekadd              (s.    o.);   abg. we ,,nicht“.

   We: ai. (ved.) wcT „nicht''; lat. we „nicht“ in ne—quidem^ nequaqnam^ ne-
qtilqtiain^          neqnam. gekiirzt wahrscheinlich in neutiquam (aber ne-uter mit
altem *we,               s. o.),    we Konj.          ,,dafi    nicht'*',   osk. ni     j.ne''    (ni-p „neve“), marruc.
Wi,,ne“;            mcymr. wy, ncymr. w/, corn. nij. bret. we „nicht'*' (wohl
                   air. ni^        w7,
durchaus, z. T, aber mit sekundarer Kiirzung, aus idg. we, s. Thurneysen
                                                                               ;




^d20                                                       ne-, no*, nes-, nos-



Hdb. 32, 152; hingegen geht Pedersen KZ. 40, 147, KGr. I 250, 301 von
idg. *ne aus, dasaber                        —
                          auBer im betonten nc-ch        wohl durchaus die                      —
Proklisenentwicklung zu na erfabren hat, s. o.); mit der Kopula kontrahiert
air. ni „ist nicht^^ aus ^nest^ ^ne-est (Pedersen KG*. II 421 sieht darin das
gewohnliche ni mit ausgelassener Kopula)
  got. 7ie „nein“. tJber aksl. ne~hbio „jemand^^ u. dgl. s. Pedersen KZ. 40, 147.
     '*nei betontes „nicht“, av. nae~cis „keiner^‘, adv. iiaecis verstarkte Negation;
lat.    n7, altlat. 7iei             Adv. und Konj.                1.    alter „nicht,     daB      nicht“, 2, „si non'',
qiiid-nt;          osk. nei „nicht“ {nei-p „neque“);                               got. 7iei (dji.key.) „nicht",    ahd.
m emphatisches „nicht“;                             lit.    nS-Jcas ,.niemand“,          7iel   „nicht einmal"     (iiber
nei „wie“           s.    o.);abg. 7ii „neque% 7^^-'k^to „niemand" (iiber klr. poln. ni
„wie“,       s. o.).       Die germ. Formen vielleicht aber = ai. 7ied „durchaus nicht,
damit nicht", av. ndit^ ap. 7iay aus idg. id „das nicht", Osthoff PBrB. 8,
312; Prellwitz BB. 22, 77 Anm. sucht diese Gdf. kaum mit Recht auch in
den andem genannten Formen; vielleicht ist idg. 7iei nach J. Schmidt
KZ. 32, 408 aus     (vgl. ovxoo~i) zu deuten; keinesfalls eine Locativ-
bildung (Fickl^ 499, Persson IF. 2, 204).
             Verneinungspartikel                      als erstes Zsglied: ai. av. ap. a-,                  von Yokalen
(auch        /,u) mi-; arm. an-;                      gr.    d-,   vor Yok. dv- (iiber dvd-nvevorog u. dgl.
s. Solmsen Unt, 264f.) lat. m-, altest en- (die vorkonsonantische Form);
                                         ;


osk.  umbr. a7i- (s. dazu Yf. Uber iilteste Bez. zw. Kelten und Italikern 53,
friihere Lit. Wb.^ u. in-); air. m- (vor Med.), c- (vor Tenuis), an- (vor
Yokal), cymr. corn. bret. a7i- (vgl. iiber die kelt. Formen Zimmer KZ. 24,
523 ff., R. Schmidt IF. 1, 68, Yf. aaO. 46); got. ahd. as. uyi-^ aisl. o-, u-,
Im Bsl. durchaus durch          verdrangt I's. dariiber, sowie iiber anderwei-
tigen Ersatz von w durch 7ie- Brugmann II ^ 1, 105 f.); iiber ksl. m-j§-vfro
.junglaubig", 7ie-jg-syih ^unersattlich = Pelikan" s. Berneker 429.      Durch
mehrere Sprachen durchgehende Entsprechungen sind z. B. ai; amfta-^
dfxPQOTog^           immortalis;             ai.     djnata-^          dyvcoTog^     arm. ancanaut^ ignohis^         air.
ingnad^ got. iinJcnnps;                      ai.    anudrd-, dvvbqog; u. a.
     Altere Lit. bei Curtius 306, 317,                                  v. Planta II      468 f.,    Brugmann IP. 6,
79—89.             — Zshang mit                    7ii-^   nei   (s.   d.),   ner- „nieder“ (Pick I ^ 94 zw.)         ist
ganz fragwiirdig, eher annehmbar der mit enm ,,ohne".

lie-,    no-, plur. nes-, nos- ,,wir" (ursprgl. auBerhalb des Nominativs;                                          Nom.
        8.   u.    Genaueres s. bei Brugmann II* 378 ff. und in den einzel-
```


## [2026-09-07T18:23:11.045Z] TOOL CALL #41: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1931 --image 2>&1 | grep -i \"png\\|vision\\|path\\|REF:\" ; ls -la data/verification/sources/refs/ocr/BQT/ 2>/dev/null | head"
}
```


### [2026-09-07T18:23:12.321Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1931.png
REF: BQT:1931  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 14  OCR-lang: fas
total 57428
drwxrwxr-x  2 sfmqrb sfmqrb   12288 Sep  7 14:22 .
drwxrwxr-x 13 sfmqrb sfmqrb    4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb  368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb    1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb  534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb    2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1076 Sep  4 15:27 103.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  330101 Sep  6 17:59 1092.jpg
-rw-rw-r--  1 sfmqrb sfmqrb    2600 Sep  6 17:59 1092.vision.txt
```


## [2026-09-07T18:23:15.486Z] TOOL CALL #42: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1931.png"
}
```


### [2026-09-07T18:23:15.958Z] TOOL RESULT

```

```


## [2026-09-07T18:23:15.955Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-07T18:23:50.102Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && cat > ocr/BQT/1931.vision.txt <<'EOF'\nBQT (Borhan-e Qate', ed. Mo'in) printed p. 1931 = vol. 4 scan pdf page 14\n[read from the page image by vision; the tesseract OCR garbles the Latin transliterations]\n\nHeader: گفتار بیست و چهارم / از کتاب برهان قاطع در حرف میم با حروف تهجی مبتنی بر بیست و هشت\nبیان و محتوی بر یک هزار و بیست لغت و کنایت / بیان اول / در میم با الف مشتمل بر دویست و چهارده لغت و کنایت\n\n* ماپروین ۱ – بابای فارسی، مخفف ماه پروین است و آن بیخی باشد که دفع سموم ...\n\nم (میم) – حرف بیست و هشتم از الفبای فارسی و حرف بیست و چهارم از الفبای عربی (ابتث) و سیزدهم\nاز حروف ابجد، و در حساب جمل آنرا چهل گیرند. این حرف گاه به «ن» بدل شود. – م (مفتوح) ma چون\nبر سر فعل امر درآید، نهی سازد: مگو، مخور، مزنید، ونیز بر سر فعل دعائی درآید: مباد، مبادا. رك: مه –\nنیز «م» ضمیر اول شخص مفرد باشد (رك: دیباچهٔ مؤلف ص بط – که کو)، در پهلوی ‑m (ضمیر اول شخص\nمفرد) «اونوالا ۴۹۳».\n\n* ما – پهلوی amâh (ما)، پارسی باستان amâxam، اوستا ahmâkəm، اوراق تورفان amâh «نیبرگ ص ۷»،\nپازند êmâ، هندی باستان asmáka‑ «استق ۹۵۵»، استی max «ک. است ۱۲۶»، در لهجهٔ یهودیان ایرانی êmâ،\nکردی me، ma، mé «ژابا ص ۴۰۹»، شهمیرزادی و گیلکی ama، دزفولی omûn، خوانساری hâmâ\n«سالنامهٔ کلیایگان ۴۷». رك: دارمستتر، تبعات ج۱ ص ۱۱۱، ۱۱۲، ۱۲۸؛ ضمیر اول شخص جمع\n(متکلم مع‌الغیر) و آن ضمیر منفصل است، گاه در حالت فاعلی باشد: ...\nEOF\necho saved; ls -la ocr/BQT/1931*"
}
```


### [2026-09-07T18:23:51.307Z] TOOL RESULT

```
saved
-rw-rw-r-- 1 sfmqrb sfmqrb 118409 Sep  7 14:22 ocr/BQT/1931.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2385 Sep  7 14:22 ocr/BQT/1931.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   2023 Sep  7 14:23 ocr/BQT/1931.vision.txt
```


## [2026-09-07T18:23:52.517Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"us,  pron\\|^us,\\|us  (2)\\|  us  (pers\" KLN_1966.txt | head -10; echo \"--- markers ---\"; grep -n \"1681\\|1682\\|1683\\|1684\" KLN_1966.txt | head -10; echo \"--- our ---\"; grep -n \"our,  poss\\|OE\\.  úre\\|ûre\" KLN_1966.txt | head -10"
}
```


### [2026-09-07T18:23:52.613Z] TOOL RESULT

```
40905:us,  objective  case  of  we.  —  ME.  ous,  us,  fr.  OE. us,  rel.  to  OS.,  OFris.  us,  ON.,  Swed.  oss,  Dan. os,  MDu.,  Du.  ons,  OHG.,  MHG.,  G.  uns,  Goth. uns,  fr.  I.-E.  base  *ns-,  for  *nes,  *nds,  ‘we’; cogn.  with  OI.  nas,  ‘us’,  Avestic  na,  ‘us’,  Toch. A  nas,  Hitt,  nash,  ‘us’,  Hitt,  anzash,  ‘we’.  Alb. na,  ‘us’,  Gk.  dual  vci,  vffii,  ‘we  two’,  Lesbian ap.p.£,  Dor.aui  (for  *aapiE;  whence  Ion.  and  Att. ■qpEu;),  Avestic  ahma  (for  I.-E.  *nsme),‘ we’,  L. nos,  ‘we,  us‘,  OSlav.  ny,  ‘us’,  nasu,  ‘our’,  OPruss. nouson,  ‘our’.  Alb.  ne,  ‘we’,  Olr.  ni,  W.,  Co., Bret,  ni,  ny,  ‘we,  us’.  The  rough  spirit  in  Att. 7)!Z£i:<;  is  due  to  the  influence  of  ujisTg,  ‘ye, you’.  Cp.  our,  nostrum.
--- markers ---
12789:Derivatives:  electric,  n.,  electric-al,  adj.,  electric¬ ally,  adv.,  electric-ian,  n.,  electric-ity,  n.,  elec- tri-fy,  tr.  v.,  electri-fi-er,  n.,  electri-fic-ation,  n., electr-ize,  tr.  v.,  electr-iz-ation,  n.,  electr-iz-er,  n. electricity,  n.  —  Formed  fr.  electric  with  suff. -ity;  first  used  by  the  English  physician  Sir Thomas  Browne  (1605-1682)  in  1646. electro-,  combining  form  meaning  ‘electric;  elec¬ tricity’.  —  Fr.  Gk.  ijXcxTpov,  ‘amber’.  See electric.
16732:grog,  n.,  alcoholic  drink  diluted  with  water.  — Shortened  fr.  Grogram,  nickname  of  Admiral Edward  Vernon  (1684-1757),  who  used  to  wear a  grogram  cloak  (see  grogram);  the  drink  was so  called  because  he  was  the  first  to  order  di¬ lution  of  sailor’s  rum.
17584:to  pneumonia  (med.)  —  Lit.  ‘appearance  of  a liver’ ;  coined  by  the  Italian  physician  Giovanni Battista  Morgagni  (1682-1771),  fr.  Gk.  -J)7ra- xi^eiv,  ‘to  be  like  a  liver’,  fr.  Jjicap,  gen.  •q7taxo9, ‘liver’.  See  hepatic  and  -ize. hepato-,  before  a  vowel  hepat-,  combining  form denoting  the  liver.  —  Gk.  Yjxaxo-,  fr.  )jxap,  gen. •ijixaxo?,  ‘liver’.  See  hepatic, hephaestic,  adj.,  pertaining  to  smiths;  —  hephaes- tic  cramp,  cramp  caused  by  the  excessive  use of  the  hammer.  —  See  next  word  and  -ic. Hephaestus,  n.,  the  god  of  fire  and  metal-working ; identified  later  with  Vulcan  ( Greek  mythol.)  — L.,  fr.  Gk.  "Htpatcrxo?,  a  pre-Hellenic  word  of uncertain  origin.
20328:Joe  Miller,  1)  a  jestbook;  2)  a  stale  joke.  — From  Joseph  Miller,  name  of  a  comedian  (1684- 1738),  whose  name  was  connected  with  a  jest- book  published  in  1739.
31848:Reaumur,  adj.,  pertaining  to  the  French  physicist Ren6-Antoine  Ferchault  de  Rdaumur  (1683- 1757),  or  to  the  thermometric  scale  invented  by him  in  1731.
32972:—  Medical  L.  ( musculus )  risorius,  ‘(the  muscle) that  causes  laughter’,  coined  by  the  Italian  anat¬ omist  Giovanni  Domenico  Santorini  (1681  - 1736),  fr.  L.  risus,  pp.  of  ridere,  ‘to  laugh’.  See risible.
39754:tracheotomy,  n.,  incision  in  the  trachea  (surg.)  — Coined  by  the  German  surgeon  Lorenz  Heister (1683-1758)  in  1718  fr.  traeheo-  and  Gk.  -xopia,
--- our ---
```


## [2026-09-07T18:24:05.408Z] TOOL CALL #45: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-07T18:24:05.441Z] TOOL RESULT

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


## [2026-09-07T18:24:12.213Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%E1%BC%84%CF%83%CF%86%CE%B1%CE%BB%CF%84%CE%BF%CF%82\" \\\n \"https://www.etymonline.com/word/asphalt\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nes-\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 352 verification (Ne 1/Nei 3/An 4; Ne 2/Nes 2): sim, ma, asphaltos, PIE roots\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-07T18:24:21.499Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b726e506f213ce7d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2e029ebd26ced867.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0d5b80f03d535ee6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eb936a6b8e13c6ad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cdc8f2896cc9caef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f1eb40e394615a67.txt
```


## [2026-09-07T18:24:25.482Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"===== SIM =====\" && grep -n -A25 \"^Persian\" b726e506f213ce7d.txt | grep -i -m1 -A25 \"etymolog\" | head -40"
}
```


### [2026-09-07T18:24:25.551Z] TOOL RESULT

```
===== SIM =====
```


## [2026-09-07T18:24:26.553Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"===== ASPHALTOS =====\" && sed -n '1,120p' 0d5b80f03d535ee6.txt | grep -n -i -A15 \"etymology\" | head -40; echo \"===== ETYMONLINE asphalt =====\"; grep -n -i -m1 -A20 \"asphalt (n\" eb936a6b8e13c6ad.txt | head -30"
}
```


### [2026-09-07T18:24:26.622Z] TOOL RESULT

```
===== ASPHALTOS =====
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.3.3 
77- Descendants 
===== ETYMONLINE asphalt =====
23: asphalt (n.) 
24-
25- early 14c., "hard, resinous mineral pitch found originally in Biblical lands," from Late Latin asphaltum , from Greek asphaltos "asphalt, bitumen," often said to be from Greek a- "not" + *sphaltos "able to be thrown down," taken as verbal adjective of sphallein "to throw down," according to Beekes "under the assumption that it denoted the material that protects walls from tumbling down," but he finds this proposed etymology "weak." Perhaps from Semitic [Klein, citing Lewy, 1895] or another non-Greek source.
26-
27- The meaning "paving composition of tar and gravel" dates from 1847 and its popular use in this sense established the modern form of the English word, displacing in most senses asphaltum , asphaltos . As a verb meaning "to cover with asphalt," from 1872. Related: Asphaltic .
28- also from early 14c. 
29-
30- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
31-
32- More to explore
33-
34- mummy 
35-
36- Medieval Latin mumia, which is perhaps from Greek moumia or directly from Arabic mumiyah "embalmed body," from Persian mumiya "asphalt...The sense evolution is from the old belief that Egyptian mummies were embalmed with asphalt, which was used medicinally in...Ancient mummies were harvested for asphalt they were thought to contain, and later merchants mummified executed criminals...Abd al-Latif al-Baghdadi, traveling in Egypt circa A.D. 1300, reported buying three mummified heads filled with asphalt for...
37-
38- naphtha 
39-
40- In ancient writers it refers to a more fluid and volatile variety of natural asphalt or bitumen....
41-
42- jungle 
43-
```


## [2026-09-07T18:24:31.596Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c b726e506f213ce7d.txt 2e029ebd26ced867.txt && echo \"=== SIM: search asem/Greek ===\" && grep -n -i \"asēm\\|asem\\|ἄσημον\\|Ancient Greek\\|silver\" b726e506f213ce7d.txt | head -20"
}
```


### [2026-09-07T18:24:31.660Z] TOOL RESULT

```
10147 b726e506f213ce7d.txt
30950 2e029ebd26ced867.txt
41097 total
=== SIM: search asem/Greek ===
241: silver , a lustrous , white , metallic element
244: money and coins made of silver 
247: silverlike thread , lace or metalware , wire 
252: سیمدوز ( sim-duz , “ one who stitches with silverlike threads ” ) 
253: سیمذقن ( sim-zakan , “ silver-chinned ” ) 
254: سیمین ( simin , “ of silver; silver-like ” ) 
284: From Middle Persian [script needed] ( (ʾ)sym /⁠(a)sēm⁠/ , “ silver ” ) , from Old Persian 𐎿𐎡𐎹𐎶𐎶 ( s-i-y-m-m /⁠siyamam⁠/ ) , from Ancient Greek ἄσημον ( ásēmon , “ silverware ” ) , neuter form of ἄσημος ( ásēmos , “ pure, unmarked ” ) . Akin to Parthian hsym ( hasēm , “ silver ” ) , Bactrian σιμινο ( simino , “ made of silver, silverware ” ) .
334: ( original sense , now poetic ) silver 
338:bar sar-e simine tasht tâsak-e zar barnehâd The little narcissus has again put that silver basin on its head
339:Upon the silvery head, the basin has put a little golden bowl 
365: Uzbek: sim ( “ wire ” ) , siym ( “ silver ” ) 
383: Short for ماهی سیم ( mâhi-ye sim ) , literally “silver fish”, but its old form was شیم ( šim ) .
502: Persian terms derived from Ancient Greek
```


## [2026-09-07T18:24:40.277Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"amāh\\|amah\\|ahmākam\\|Proto-Iranian\\|we, us\" 2e029ebd26ced867.txt | head -20"
}
```


### [2026-09-07T18:24:40.327Z] TOOL RESULT

```
561: مَا أَعْظَمَهُ رَجُلًا! ― mā ʔaʕẓamahu rajulan! ― How great man he is! 
562: مَا أَعْظَمَهُ مِنْ رَجُلٍ! mā ʔaʕẓamahu min rajulin! How great man he is! 
772: From Middle Persian 𐭫𐭭𐭤 ( LNE /⁠amāh⁠/ , “ we, us ” ) , from Old Persian 𐎠𐎶𐎠𐎧𐎶 ( amāxam ) (genitive plural form of the first person plural pronoun), ultimately from the variant *mey of Proto-Indo-European *wéy . Compare Proto-Slavic *my , Lithuanian mẽs and Old Armenian մեք ( mekʻ ) .
```


## [2026-09-07T18:24:57.406Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT in- ===\" && grep -n \"^in- \\|in-  privatif\\|in- 2\\|in-, préfixe\" LAT.txt | head -10; echo \"=== LEW in ===\" && grep -n \"in-  \\(privativ\\|.negativ\\)\\|in-  Präfix\\|in- 'un\" LEW_1910.txt | head -10; echo \"=== IEC ne ===\" && grep -n \"^ne-\\|^nes-\\|ne 'not'\\|nos-\" IEC.txt | head -15; echo \"=== SYN we/us ===\" && grep -n \"1st pers\\|13.31\\|we, us\" SYN.txt | head -10"
}
```


### [2026-09-07T18:24:57.492Z] TOOL RESULT

```
=== LAT in- ===
2236:in- privatif: incogitans, -tantia, -tatus, -tabilis (sans doute d'aprfes
11803:in- marquant le mouvement), il est second terme de compose dans solli¬
28719:in- local, "mettre en terre, inhumer" d'ou inhumator; pollinctor
29608:in- (i m- devant labiale b,p,m: imberbis, improbus, immodestus-,
29655:in- devant voyelle est analogique de la forme employ^e devant consonne,
30529:in- de sens local, comme le montrent les rapprochements qu 1 on lit
65726:in- (cf. M.L. 45x6), ob- (-obs ), d'ou obstrudulentus F. 308,36, obstrusio
=== LEW in ===
=== IEC ne ===
5737:2í2nosko (X2nos-) (intens.) ‘know’. Cf. ong- mi, ?nosKo. WP I, 577-80 Skt. cf. desid. jijfiase; Ober cf. xsnàs-, id.; Gk. gignósko, Epirote gnósko; Lat. a-, co-gnoscó, ére; Arm. cf. canucanem (^warn', fr. *$nosKno)
5779:$notér- ‘expert’. Variant &nostér Skt. jiatr; Av. Znata, obl. Znatar; Gk. cf. gnos- tér, id.
5780:$notis ‘kinsman, acquaintance’; notos “fa- miliar, familial. Cf. $nos- Kanic (Kültepe) cf. the name Kunut-ahsu (ca. 2000 BC. Cf. aksios); Skt. jfiatib ‘kinsman, blood-relation'; jüatáh ‘known’; jðatum, inf. ‘to know’; Tokh. cf. -knats, cpds. *-known'; Arm. (variant) canawt', i-st. ‘known; acquain- tance’; Gk. gnósis ‘knowledge’; gnotós, adj. ‘known, akin’; m. ‘kinsman, friend’; Lat. -no- tus, -gnōtus; Olr. gnáth “familiar; custom’; OW & W gnawd “usual; custom’; Go. knōps, or knōds, f. Let ‘race’; OHG knuot, f. i-st. ‘kind, substance’; R znať ‘nobility’; OCS fut. inf. znatü ‘to know’; Latv. znots ‘son-in-law’. WP I, 577-80
5794:(8namos, variant form of type gnom-, cf. $nos-, etc.). See next OCS (and com. Sl.) znamü (Cknown'. Ambig.); Li. Zinomas; Latv. zinams, id.
5811:Bugs, &nos-, see -£nos, $nós-
7376:ne-klosínü ^whole', see klaso)
11556:ne-, nē- (2) ‘in? in some cpds. Gk. cf. ne-díé 'diver-bird'; nē-dús ‘womb’; R né-dro ‘bosom’
11558:ne-bho ‘but, least, except, or’. Cf. ne, bhü-, bhà Osc. cf. nep (cor. Ambig. perh. fr. *neque); OHG nibu, nibi, nube, noba, cj. “unless;
11675:nes- (2) (nínés-) ‘turn, return, recover, thrive, succeed, proceed'. Cf. néio WP II, 334 Skt. nase, mp. “approach; join; deviate; go wrong’; Hitt. nesh- ‘turn’; Tokh. A nas-, B nes- "be: Gk. néomai, neümai, Ion. nisomai (return'; cf. also ko-néo ‘hurry, attend” ?); Go. ga-nisan, sv. 5 ‘survive’; MHG ge-nésen, OHG gi-nésan, wd OE nesan, id. Cpd. in Arm. (?) nah-angem, v. ‘turn, divert, thwart' beside nahang, gs: -i, abs: -av ‘region’. Cf. also Gk. en-neós Cdeatmute, lit. 'introverted'?); Ir. neas, m. “potters wheel
11676:nes- (3) (?) Hitt. cf. nas-su, nas-ma “either; or: OLat. (Fest.) nesi, pr. ‘without’; Li. nes, cj. “for, as’. (Lat. nisi, for *ne, siét “lest it be’)
11681:nes- — neur- (nour-, nur-)
11714:ne-uedh- (n-uedh-, ne-uédhst-) ‘unmarried’ Gk. eitheos “bachelor”; E un-wed; Li. ne-védes ‘unmarried’; OCS and com. Sl. ne-vésta *bride'
11720:ne-uid-, -ueid- (ignorant; ignoramus’. Cf.
11721:ne-, ueid-, uid-. Variant n-" Gk. néis, gs: nēidos ‘unknowing’; OE cf. unge- witt ‘ignoramus’, MHG un-wis ‘unknown’; un-wiz, -witze ‘ignorant’; Li. cf. nevidõnas, m. ‘demon’
=== SYN we/us ===
23365:13.31 Norse on THE NUMERALS
23833:13.31. NOTE ON THE NUMERALS
```


## [2026-09-07T18:24:59.571Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN ma pronoun ===\" && grep -n \"'wir'\\|ma 'wir\\|mä 'wir\" HRN.txt | head -10; echo \"=== ARY sim ===\" && grep -n \"سیم\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY latin SIM ===\" && grep -n -i \"^SIM\\|SIM \" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T18:24:59.651Z] TOOL RESULT

```
=== HRN ma pronoun ===
7756:ap. vi + l^tar-, vigatarayäma 'wir überschritten' ; aw.
=== ARY sim ===
171:کش و واکنش یکی از دلایل عمده‌ی تقسیم زبان واحد هندو اروپایی ابندا به گویش‌ها و سپس به
880:ِ تقسیم پندی زبانهای هند و اروپایی از نظر مکان جغرافیانی
935:تصویر کلی فرهنگ و جامعهی هند و اروپایی حدود شش هزار سال پیش را به تقریب ترسیم کنند.
1176:اروپایی نخستین را ترسیم نمایند. در چند دهه‌ی اخیر نیز زبانشناسان توانسته‌اند از راه همسنجی
3814:۲ معنی این واژه در سانسکریت: بخشنده) خداء تقسیم کننده,
6867:سیم موم
10934:| سیم (به چم آبخشی از برغ)
=== ARY latin SIM ===
630:DESY 6 AU slaty 9 ESL y lel ySIyla asim glalsleljgisyl
895:Sol eo ee AT G99 9 Oli GLUT U acd Foleal ace jab Sim yl ola Fh.y
3306:seed ty" Sim 59" 6 YIN" Badly Vodly gal “A
8289:-GUSSIM © (OLD IRISH) 45 54),,) (SANSKRIT) cy She
10460:KOFYTO POLISH) long) sIM {RURDISH) «52,6
11231:SIMTS LATVIAN) (5) 3) OLD SCANDINAVIAN) 48 5th!
```


## [2026-09-07T18:25:08.517Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT in- privative ===\" && sed -n '29600,29660p' LAT.txt | cut -c1-400"
}
```


### [2026-09-07T18:25:08.567Z] TOOL RESULT

```
=== LAT in- privative ===
exclut plusieurs des possibilites d^tymologie envisagees. Au point
de vue latin, imus semble etre a inferus (v. ce mot) ce que summus
est a superus', infimus aurait ete refait ensuite, sur le modble dein-
sso -
intimus, extimus, citimus, ultimus , etc., pour retablir la transpa-
rence ^tymologique. II faudrait donc partir de inf-mo-. Mais l'i
initial ne s'explique pas en osque, de sorte que 1 1 on n 1 arrive a
aucune certitude.
in- (i m- devant labiale b,p,m: imberbis, improbus, immodestus-,
il- devant I: illaudatus; ir- devant r: irritus; nasale gutturale
dans ignotus): pr^fixe privatif employe pour cr<?er des formes ad-
jectives et adverbiales, comme a—, av— en grec; cf. probus, improbus,
et demeurd naturellement dans leurs derives improbo, improbitas , etc.
Ne 3’emploie pas devant un verbe: le contraire de scio est nescio
(malgre inscius); de lego, neglego; de uolo, ne uolo nolo, etc.
(indecet est tardif et isole, cf. sons ignosco); inusite ^galement
devant un substantif: le contraire de otium est negStium; mais Quin-
tilien e erit inotiosus pour traduire acr^oXoC. Cf. encore infandum
a cSte de nefas. Des formations comme iniuria, incuria, sont au moins
virtuellement derivees d'adjectif; ingratiis ne vient pas de *ingratia
mais a 4 te bati sur gratiis (adverbe, etc.), sous 1'influence de in¬
gratus; iniussU sur iussu; inluuies est un calque poetique de aXouota;
imperfundies, imbalnities sont des creations artificielles de Lucilius
d'aprbs inluuies. Avec les substantifs, le latin a parfois des compos^s
d'un type plus recent: amens, demens, deformis, exlex; cf. aussi
male, dans male sSnus.
1'usage de in- privatif s'est particulierement d^veloppe dans la
latinite imperiale (dans Ovide seul, on compte comme n^ologismes
incommendatus, inconsumptus, incustoditus, indefletus, indelectus,
indelebilis, indeploratus, indestrictus, indigestus, innabilis, innu¬
bus, inobrutus, irrequietus) ; la poesie, les langues techniques, et
la langue de 1 ’Eglise ont cree un nombre considerable d^djectifs
de ce type, dont beaucoup ont servi a traduire des adjectifs du type
grec correspondant en a—: cf. incredulus = a 7 U,crroC, illaboriosus = axa-
(xaTOS; illacrimabilis = aSaxpuxos, illaesus = cc t 3 Xaj 3 -r]S; illaetabilis
= a^xpT]C, illamentatus = axXauaxoc, etc. Cette formation s'est i^tendue
k des substantifs: inapparatio (= aTOxpaaxeuaxa), infinitio (= arcei, pia);
imperturbatio ( = aTOxfieia). Ce sont des formes de lal. ecrite et savante;
les 1. romanes en offrent peu d^xemples: les seules formes abondamment
repr 4 sent£es sont infans dont le sens ne correspondait plus k l'ety-
mologie, infirmus specialise dans le sens de "malade, infirme" et
sans rapport semantique avec firmus, inimicus ,loin egalement de amicus,
insipidus, Insapidus "fade" en face de sapidus sp 4 cialise le plus
souvent dans le sens'de "sage", integer dont le rapport avec tango
n 1 apparaissait plus nettement, inultus en face duquel il n'y a pas
de simple *ultus . Quelques autres adjectifs ont surv^cu sporadiquement:
immundus: log. bundu "diable", M.L.4389 (mot d'Eglise); incredulus,
M.L.43G3 (autre mot d^glise); iners, M.1.4390; iniquus, M,1.4439;
Insulsus, M.L.4476; intactus, M.L.4477; inualidus, M.L.4526. Par
contre, les langues savantes ont repris et developpe cette formation
a 1'infini.
In- represente la forrae a degre zero *n- de la negation ne (v.
ce mot); devant consonne, il r^pond k indo-iran. a-, gr. a— , germ .un-,
celt.an-; un compose comme ignotus r^pond exactement a skr. ajnatah,
gr. a^varroG. Devant voyelle, 1 1 indo-iranien a an- et le gr.av-j lat.
in- devant voyelle est analogique de la forme employ^e devant consonne,
on attendrait *en~. En revanche, 1 1 osco-ombrien an-, employe devant
consonne, ainsi dans osq. am-prufld "improbe", ombr. an-takres "integris",
est analogique de la forme employee devant voyelle, qui n'est pas557
in
attest^e,
```


## [2026-09-07T18:25:10.188Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT a- prefix / atom / asbestos / asphalt / in- ===\" && grep -n \"^A-,\\|^a-, prefix\\|Atom\\|Asbestos\\|Asphalt\\|prefix.*not\" SKT.txt | head -20; echo \"=== IEC ne negation ===\" && grep -n \"^ne, nē\\|^ne (1)\\|ne (1) .not\\|'not'\" IEC.txt | head -20"
}
```


### [2026-09-07T18:25:10.256Z] TOOL RESULT

```
=== SKT a- prefix / atom / asbestos / asphalt / in- ===
1005:Asbestos,  a  mineral.  <Gk.)  Gk.  <{• <Tf^«TTOf,  unquenchable;  because  it  is  in- combustible, —  Gk.  (1-,  tirg.  prefix;  and •ff/Jiar^r,  quenchable.  from  a^iyyvfu,  i quench,  extinguish.
1097:Atom ;  see  Tomo.
8482:Ho.  (.E.)  A.  S.  V;  gen.  his.  dat.  Afwv, ace.  Ain€,  Fern.  sing.  nom.  hed,  gen.  dat. hirt,  acc-  hi;  neut.  sing.  noro.  hit,  gcn.<4t/, dat  him,  acc  hit.  PI.  (all  genders),  nom. acc.  hi^^  hi,  gen.  hira,  hiora,  dat  Aim, Atom,  -f  DU'  A/y,  Icel.  Aann,  Dan.  Swed. AdM.  Allied  to  Gk.  imiivot,  mtlvot^  that one.     (Base  KI.)
9019:Hyper-,  prefix,  denoting  excc».   (L.«      ■ Gk.)     h.  Aypcr-,  for  Gk.  vwip,  above,  be-     1 yood,   alliert   to   L.  su/tr.      lience  Ayper» b<uon,  a  transposition  of  words  from  natural order,  lit.  'x  going  beyond'  (from  ^Vfir, to  go)  ;    Ayp<r^bortan,    extreme    norlhcm (from  ^o^tat,  north  wind!  ;  kyptr-boU,  ex-      ^ aggeralion.  Gk.  iiM*^oKii   (from  f}dAA<iv,      fl to  throw,  cast).  1
10323:aU«j.  to  asni^.  (E.)  M.  Z.  alauii. En  Gower,  C.  A.  iii.  n,  ajj.  A.S.  dUigan. lo  lay  down,  lay  aside*  A.S.  ^  prefix (answering  to  Goth,  tu-,  G.  rr-) ;  /tcgun,  to lay ;  see  I&7  below.  ^  It  Ketns  to  have brea  confasc-d  |,ixi  sense  and  wriciof;.  if  not io  fipcfchi  with  M.  E.  aUggen,  to  aJ!€\-iatc, from  O.  F.  aI^^r  »  Low  L.  alltuiare^  10 alleviate:  see  aJLleTiate  under  Iiftvity  But thc/i>rm  and  j^vai/ remain  truly  EnHiih.
12330:non-,  prefix,  not.  (L)  L ori|;.  pot  one.  — L.  fu.  not;  unut.
19279:Mftib  ouOting  known,  public  accosation, ^^Bb,  injury,  vexation,  grief. IWlialler,  a  total  abstainer.  ^F.»L. : tA  E.  prefix  and  suffix.)  Tee-totai  is  an phuiscd  form  of  Total,  q.  v.  1'hc  word ginated  with  R.  Turner,  of  Preston,  who, a  tempcrsjice  meeting  about  1833,  u- ted  thkt  nothing  but  te^e-foial  will  do ; I  ilic  SUuoch  Tectoullcr,  ed.  by  J.  Live- I,  of  Preston  Jan.  1867.  fHaydn.) beiotum,  Totum,  a  spinning  107.  (U) tmesiy  totum  (Aiii,  i  77s  Fhillips.  1706). called  from  the  side  formerly  marked  7*, ich  signified  totum^  i.  e.  alt  the  stake, |u  L.  totum,  nent.  of  totus^  the  whole ; I  Total.     Hence  the  name  totum,  or  7-
20415:umbrella.  (Ital.  — L.)  Ital.  umbrella, 9mbr(t!a,  a  parasol;  riimin.  of  Ital.  ombra, B  sha<]e.  — L.  umbra,  a  shade. Umpire.  (F.  —  L.)  Put  for  numpire^ the  old  form  of  the  word  ;  M.  E.  nompere^ ttotimpert^  also  nouuNrt,  nounfter,  V. Plowman,  B.  v.  ^^l.^O.F.ncmfer*',  later nomf^ir,  peerless,  odd  (Col.)  ;  earliest form  nonper  (Roquefort).  Used,  like  L. impar,  in  the  sense  of  arbitrator  ;  the lit.  sense  is  uncqufil,  odd,  hence  a  third man  called  in  to  arbitrate,  a  'non  peer,'* O.  F,  non,  not ;  O.  F.  per,  pair,  a  peer. See  Won- ;  also  paer-,  under  Par,  %  Tlicrc b  no  doubt  as  to  this  result Un-  (0*  ncg.  prefix.  (E.)  Prefixed  to sbs.,  adjs.,  ana  aovs.  (Distinct  from  im- (a)  below.)  A.S.  ««•,  ncg.  prctix.+  Du. ON',  Icel.  i-,  ii-,  Daii.  u-,  bwcd.  tf-,  Guth. un-,  G.  ttif-,  W.  an-,  L.  im-,  Gk.  iof',  d-, orig.  <tra-.  Zend,  ana-,  Pera.  nd-,  Skt.  an-, p.  The  Aryan  form  seems  lo  have  been ANA;  whence  also  L.  ne^  and  Gk.  in;-, Goth,  ni-,  Ru^.  ne-,  Gael,  neo-,  negative prefixes,  y.  Readily  pfclixed  to  a  large number  of  woniU  ;  a  few  of  these,  such  as uH-couth,  of  which  the  simple  form  it  not Qscdp  will  be  found  below. Un*  (2),  verbal  jirefix,  expressing  the reversal  of  on  action.  (£.)  (3uitc  distinct from  un-  (1)  above ;  only  used  with  verbs Thus  to  UM'lock  -  to  reverse  locking,  lo n   that   which   wns  cl(i:>e«l   by  locking.
21917:The  foUowmg  is  a  lUt  of  Ihe  prindpal  prefixes  in  English,  &hewin| It  is  perhaps,  not  quite  exhaustive,  but  contains  nearly  nil  of  any  coc further  information,  see  the  etymologies  of  the  wortls  a'dcwn^  ^c^  in  the
22094:Iff-  (j),  negative  prefix.  (E.  cr  L.)  In now,  the  prefixed  n  is  doe  to  A.  S,  ne, not-  In  n-uli,  it  is  due  to  the  cognate L,  nt,  not.     See  Ne-.
22177:Un-  (i).  negative  prefix  to  nouns,  &c.  (E.) A.  S.  un-,  not ;  cognate  with  I*  m-,  no!, Gk.  cb--,  not      See  An-  \i).  In-  (.0.
23781:Appogg^aturo,  a  grace-note  or  passing Cotic  prefixed,  as  a  support,  to  an  essential note  of  a  melody.  (Ttal.*L  oHi/Qk.)  Ital. appcggiaturay  lit.  a  support.  — Ital.  appog- giare^  to  lean  upon.  — Ital.  ap-  (for  ad\  to, upon  ;  pc^t'o,  a  place  to  stand  or  lean  on, Ac  — I^iu/,  to;  pcJiur/if  an  elevated  place, a  balcony,  from  Gk.  v6ikoy.  See  Pew, P  5-I5-
=== IEC ne negation ===
```


## [2026-09-07T18:25:25.991Z] TOOL CALL #55: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%85/\" \"https://abadis.ir/fatofa/%D9%85%D8%A7/\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 352: Mo'in (MON) entry for سیم / ما\" 2>&1 | tail -1; done"
}
```


### [2026-09-07T18:25:30.453Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f6630de30854ea4e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6f0bb09f9e1c7ffe.txt
```


## [2026-09-07T18:25:34.061Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== MON sim ===\" && grep -n -A6 \"فرهنگ فارسی معین\\|معین\" f6630de30854ea4e.txt | head -40"
}
```


### [2026-09-07T18:25:34.111Z] TOOL RESULT

```
=== MON sim ===
21: سیم. ( اِ ) نقره. پهلوی «اسیم » ، در فارسی «آ» از اول کلمه ( پهلوی ) حذف شده ، اما سیمین در پهلوی آمده. اورامانی «سیم » ( رشته نقره ). برخی از محققان معاصر اصل سیم را یونانی دانند. ( مجله یادگار سال 4 شماره 6 ص 22 و شماره 9 و 10 ص 156 به بعد تقی زاده ). ( از: «اء»، علامت نفی و «سما» ، نشانه نهاده و علامت گذاشته ). و رجوع به فرهنگ یونانی - انگلیسی لیدل و اسکات شود. جمعاً یعنی نقره نامسکوک ( از افادات شفاهی بنونیست ) و الجماهر بیرونی ص 242 شود. ( از حاشیه برهان قاطع چ معین ). نقره. ( برهان ). ورق. فضه. ( ترجمان القرآن ) : 
22-گروهی اند که ندانند باز سیم از سرب 
23-همه دروغ زن و خربطند و خیره سرند. قریع ( از لغت فرس اسدی ص 296 ).
24-یکی ز راه همی زر برندارد و سیم 
25-یکی ز دشت به نیمه همی چند غوشای. طیان ( از لغت فرس اسدی ص 516 ).
26-تنش سیم و شاخش ز یاقوت و زر
27-بر او گونه گون خوشه های گهر. فردوسی.
--
56: فرهنگ معین
57-
58- [ په . ] (اِ. )۱ - نقره . ۲ - پول ، وجه . ۳ - فلزی قیمتی که در معادن به طور خالص یا به صورت ترکیب با فلزات دیگر (انتیمون ، سرب ) یافت می شود و چون آن را با مس ترکیب کنند محکم تر می گردد و در صنعت کاربرد زیاد دارد. ۴ - مفتول ، رشتة باریک فلزی . ۵ - یک یا 
59- (اِ. ) چرک ، خونابه .
60- (اِ. ) چوب هایی که برزگران بر دو طرف چوبی که بر گردن گاو زراعی گذارند، بندند، یوغ . 
61-
62- فرهنگ عمید
--
198:فرهنگ لغت معین
199-
200- سِیُّم
201-در فارسی قدیم به معنی سوم
202-
203- چون گُل چه کنی ز عشق پیراهن چاک/ مانند سمن سیم درانداز به خاک ( مقامات حمیدی )
204-
--
242: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
243-
244- لینک ها 
245-
246- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
247-
248- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-07T18:25:42.981Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"پهلوی\\|اوستا\\|باستان\" 6f0bb09f9e1c7ffe.txt | head -20"
}
```


### [2026-09-07T18:25:43.030Z] TOOL RESULT

```
201:اوستایی: azəm ( من ) 
202:فارسی باستان: adam ( من ) 
205:✅ �من� در فارسی، بازمانده ای از *azəm اوستایی است، نه ترکی. ( رجوع کنید به Bartholomae, Altiranisches W�rterbuch ) 
209:اوستایی: aṱ یا ava ( او ) 
216:اوستایی: vī یا vaēm
218:فارسی باستان: vām
255:اوستایی: ima ( این ) ، ava ( آن )
```


## [2026-09-07T18:25:48.092Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '15,40p' 6f0bb09f9e1c7ffe.txt | cut -c1-500; echo \"=== moein ===\"; grep -n -m3 -A5 \"فرهنگ معین\" 6f0bb09f9e1c7ffe.txt | head -20"
}
```


### [2026-09-07T18:25:48.143Z] TOOL RESULT

```
 معنی انگلیسی : we , us , our , ours 

 دنبال کنید 

 لغت نامه دهخدا

 ما. ( ضمیر ) ضمیر متکلم معالغیر و بیان آن به جمع و مفرد هر دو آمده است. ( آنندراج ). کلمه اشاره که بدان اشاره می کنند به اول شخص جمع از هر نوع. ( ناظم الاطباء ). ضمیر اول شخص جمع ( متکلم معالغیر ) و آن ضمیر منفصل است ، گاه در حالت فاعلی باشد و گاه در حالت مفعولی و گاه در حالت اضافی. ( از حاش
ای بلبل خوش آوا آوا ده 
ای ساقی آن قدح را با ما ده. رودکی.
بت پرستی گرفته ایم همه 
این جهان چون بت است و ما شمنیم. رودکی.
نباشد زین زمانه بس شگفتی 
اگر بر ما ببارد آذرخشا. رودکی.
نقل ما خوشه انگور بود ساغر سفچ 
بلبل و صلصل رامشگر و در دست عصیر. بوالمثل.
آمد نوروزو نو دمید بنفشه 
بر ما فرخنده باد و بر تو مرخشه. منجیک.
هرچه ورزیدند ما را سالیان 
شد به دشت اندر به ساعت تند و خوند. آغاجی.
گر خوار شدم سوی بت خویش روا باد
اندی که بر مهتر ما خوار نیم خوار. عماره ( از صحاح الفرس ).
گر شوم بودتی به غلامی به نزد خویش 
با ریش شومتر به بر ما هرآینه. عسجدی.
زی تیر نگه کرد و پر خویش در آن دید
گفتا ز که نالیم که از ماست که بر ماست. ناصرخسرو.
آنچه بر ما می رسد آنهم ز ماست. مولوی.
=== moein ===
65: فرهنگ معین
66-
67- (ضم . ) ضمیر اوُل شخص جمع . 
68-
69- فرهنگ عمید
70-
--
340: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
341-
342- لینک ها 
343-
344- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
345-
```


## [2026-09-07T18:25:58.890Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== PIE ne ===\" && grep -n -i -m3 -A8 \"Etymology\\|Particle\\|not$\" cdc8f2896cc9caef.txt | head -30; echo; echo \"=== PIE nes- ===\" && head -40 f1eb40e394615a67.txt"
}
```


### [2026-09-07T18:26:00.124Z] TOOL RESULT

```
=== PIE ne ===
62: Particle 
63-
64- 1.1.1 
65- Derived terms 
66-
67- 1.1.2 
68- Descendants 
69-
70- 1.1.3 
--
142: Particle
143- [ edit ] 
144-
145- *né [ 1 ] [ 2 ] 
146-
147- not 
148-
149- Derived terms
150- [ edit ] 
--
233: ↑ 1.0 1.1 1.2 1.3 Dunkel, George E. ( 2014 ), “1.*né 'nicht'”, in Lexikon der indogermanischen Partikeln und Pronominalstämme [ Lexicon of Indo-European Particles and Pronominal Stems ]‎ [1] (in German), volume 2: Lexikon, Heidelberg: Universitätsverlag Winter, →ISBN , pages 530-549 
234-
235- ^ Ringe, Donald ( 2006 ), From Proto-Indo-European to Proto-Germanic (A Linguistic History of English; 1)‎ [2] , 1st edition, Oxford: University Press, →ISBN , page 117 
236-
237- ^ Derksen, Rick ( 2015 ), “nė”, in Etymological Dictionary of the Baltic Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 13 ), Leiden, Boston: Brill, →ISBN , page 331 
238-
239- ^ De Vaan, Michiel ( 2008 ), “ nē ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , pages 403-4 
240-

=== PIE nes- ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nes-
FETCHED: 2026-09-07T18:24:21Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/nes- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/nes- - Wiktionary, the free dictionary 

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
```


## [2026-09-07T18:26:07.429Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -c \"\" f1eb40e394615a67.txt; grep -n -i \"does not\\|no entry\\|Wiktionary does not yet\" f1eb40e394615a67.txt | head -3\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%CC%A5-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9y\" ; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 352: PIE privative *n-; PIE 1pl pronoun *wey/oblique *n̥s-\" 2>&1 | tail -1; done"
}
```


### [2026-09-07T18:26:08.903Z] TOOL RESULT

```
235
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/web/tools/fetch_source.py': [Errno 2] No such file or directory
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/web/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-07T18:26:13.949Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%CC%A5-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9y\" \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA\" ; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 352: PIE privative *n-; PIE 1pl pronoun *wey/*ns-; Persian asfalt\" 2>&1 | tail -1; done"
}
```


### [2026-09-07T18:26:17.858Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b2179bc619450ec1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/795823af5d63f712.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/911b1eedefadb390.txt
```


## [2026-09-07T18:26:21.971Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== n- ===\" && grep -n -i -m2 -A14 \"^ \\*n\\|Prefix\\|Etymology\" b2179bc619450ec1.txt | head -30; echo \"=== wey ===\"; grep -n -i -m2 -A20 \"Pronoun\\|Etymology\" 795823af5d63f712.txt | head -40; echo \"=== asfalt ===\"; grep -n -i -m2 -A8 \"Etymology\" 911b1eedefadb390.txt | head -20"
}
```


### [2026-09-07T18:26:22.048Z] TOOL RESULT

```
=== n- ===
62: Etymology 
63-
64- 1.2 
65: Prefix 
66-
67- 1.2.1 
68- Related terms 
69-
70- 1.2.2 
71- Derived terms 
72-
73- 1.2.3 
74- Descendants 
75-
76- 1.3 
77- References 
78-
79- Toggle the table of contents 
=== wey ===
62: Pronoun 
63-
64- 1.1.1 
65- Inflection 
66-
67- 1.1.2 
68- Derived terms 
69-
70- 1.1.3 
71- Descendants 
72-
73- 1.2 
74- References 
75-
76- 1.3 
77- Further reading 
78-
79- Toggle the table of contents 
80-
81- Reconstruction:Proto-Indo-European/ wéy 
82-
--
140: Pronoun
141- [ edit ] 
142-
143- *wéy 
144-
145- we (more than two)
146-
147- Inflection
148- [ edit ] 
149-
150- A user suggests that this Proto-Indo-European reconstruction entry be cleaned up, giving the reason: “manual table should be moved to a template” .
151-
152- Please see the discussion on Requests for cleanup ( + ) or the talk page for more information and remove this template after the problem has been dealt with.
153-
154- Andrew Sihler 's reconstruction [ 1 ] 
155-
156- nominative
157-
=== asfalt ===
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Descendants 
69-
70- 1.3 
--
79: Etymology 
80-
81- 2.2 
82- Pronunciation 
83-
84- 2.3 
85- Noun 
86-
87- Toggle the table of contents
```


## [2026-09-07T18:26:25.850Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== n- body ===\"; sed -n '130,190p' b2179bc619450ec1.txt; echo \"=== wey oblique ===\"; sed -n '155,215p' 795823af5d63f712.txt | grep -n -i \"accus\\|genitiv\\|nsme\\|n̥s\\|ns-\" | head -20"
}
```


### [2026-09-07T18:26:25.910Z] TOOL RESULT

```
=== n- body ===
 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Zero grade form of the sentence negative *né , used with verbal adjectives and forming bahuvrihis .

 Prefix
 [ edit ] 

 *n̥- [ 1 ] 

 not , un- ( combining form of *né )

 Related terms
 [ edit ] 

 *né 

 Derived terms
 [ edit ] 

 Proto-Indo-European terms prefixed with *n̥- 
 Reconstruction:Proto-Indo-European/n̥mr̥tós 

 Descendants
 [ edit ] 

 Terms derived from the Proto-Indo-European root *n̥- (1 c, 0 e) 

 Proto-Albanian: *a- 
 Albanian: e- 

 Proto-Anatolian: 
 ⇒ Hittite: 𒄠𒈪𒅀𒀭𒍝 ( a-mi-ya-an-za /⁠amiyanza⁠/ , “ small ” ) [ 2 ] 

 Proto-Armenian: 
 Old Armenian: ան- ( an- ) ( see there for further descendants )

 Proto-Balto-Slavic: 
 Proto-Slavic: *ǫ- ( in *ǫrodъ and *ǫtьlъ ) 

 Proto-Celtic: *an- ( see there for further descendants )

 Proto-Germanic: *un- ( see there for further descendants )

 Proto-Hellenic: *ə- ( see there for further descendants )

 Proto-Indo-Iranian: *a- ( see there for further descendants )

 Proto-Italic: *n̥- ( see there for further descendants )

 Proto-Tocharian: *e(n)- [ 3 ] ( see there for further descendants )
=== wey oblique ===
6: accusative
8: *n̥smé ~ *nō̆s 
10: genitive
12: *n̥sóm ~ *nō̆s 
16: *n̥sm-ét 
20: *n̥sm-éy ~ *nō̆s 
22: Oblique plural *n̥s- possibly continues earlier **m̥s- (same element of singular oblique stem with plural -s). This n was made common to the whole paradigm, with even enclitic *nos for *mos, but the verb endings *-me(dʰh₂), *-mos(dʰh₂) were not disturbed. [ 2 ] 
30: accusative
32: *n̥smé ~ *nos 
34: genitive
50: accusative
52: *n̥s ~ *nōs (?)
54: genitive
```


## [2026-09-07T18:26:34.872Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '125,165p' 911b1eedefadb390.txt"
}
```


### [2026-09-07T18:26:34.912Z] TOOL RESULT

```
 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Ottoman Turkish
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from French asphalte ( “ asphalt ” ) , from Ancient Greek ἄσφᾰλτος ( ásphăltos , “ asphalt, bitumen ” ) .

 Noun
 [ edit ] 

 آسفالت • ( asfalt ) 

 asphalt , a sticky and highly viscous liquid or semisolid composed almost entirely of bitumen 
 Synonym: قطران ( katran )
```


## [2026-09-07T18:26:51.018Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '774p' AHD_watkins1985.txt | fold -w 200 | head -20; echo \"=== KLN in- pref ===\"; grep -n \"^in-,  pref\\|in-,  pref\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T18:26:51.076Z] TOOL RESULT

```
ne. Not. 1. Germanic *ne-, *na- in: a. Old English ne (> Middle English ne), not, and nd, no: NAUGHT, (NAUGHTY), NEITHER, NEVER, NILL, NO!, NO2, NONE, (NoR!), NOT, NOTHING; b. Old Norse ne, not: NAY; 
c. Old High German ne, ni, not: NIx?. 2. Latin ne-, not, and nullus, none (ne- + illus, any; see oi-no-): ANNUL, NEFARIOUS, NESCIENCE, NEUTER, (NICE), NISI, NULL, NULLIFY, NULLIPARA. 3. Latin nimis, t
oo much, exces-
=== KLN in- pref ===
18998:in,  adj.  —  Fr.  prec.  word, in,  adv.  —  ME.  in,  fr.  OE.  in,  inn,  inne,  rel.  to the  adverbs:  OS.  in,  inn,  ON.  inn,  OHG.  in  and to  OE.  in,  prep.  See  in,  prep, in-,  pref.  meaning  in,  into,  toward,  up,  against, as  in  in  born,  incline.  —  E.  in  or  L.  in;  see  in, prep.  In  words  of  Latin  origin,  in-  becomes  il- before  /,  ini-  before  b,  m  and  p,  ir-  before  r  (see il-,  ‘in’,  im-,  ‘in’,  ir-,  ‘in’).  Cp.  em-,  en-. in-,  privative  pref.,  as  in  in  advertence.  —  L.  in-, ‘not’,  cogn.  with  Goth.,  OE.  un,  ‘not’;  see  un-, priv.  pref.  L.  in-,  ‘not’,  becomes  *-  before  gn, il-  before  l,  im-  before  b,  m  and  p,  ir-  before  r (see  i-,  il-,  ‘not’,  im-,  ‘not’,  ir-,  ‘not’), in-,  form  of  ino-  before  a  vowel.
```


## [2026-09-07T18:26:55.706Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '774p' AHD_watkins1985.txt | fold -w 200 | sed -n '3,14p'"
}
```


### [2026-09-07T18:26:55.770Z] TOOL RESULT

```
oo much, exces-
```


## [2026-09-07T18:26:58.638Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '775,782p' AHD_watkins1985.txt | fold -w 200 | head -30"
}
```


### [2026-09-07T18:26:58.684Z] TOOL RESULT

```
nebh-
sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contrac
ted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, n
ot: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old Eng
lish wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- 
probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixe
d form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod
- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English n
etel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- matio
n of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METAN
EPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE,
 NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic 
*nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LIL
AC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx
!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, h
arm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, cor
pse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O
-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli-
 cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-.
 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
44
neud-
nox (stem noct-), night: NOCTI-, NOCTURN, NOCTURNAL, NOTTURNO; EQUINOX. 3. Latin noctua, night owl: Noc- TUID, NOCTULE. 4. Greek nux (stem nukt-), night: NYC- TALOPIA, NYCTITROPISM. 5. Possibly suffix
ed zero-grade form *nkt-i- in Greek aktis, ray of light: acTrno-. [Pok. neku(t)- 762.]
nem-. To assign, allot; also to take. 1. Germanic *nem- in: a. Old English niman, to take, seize: NIM, NUMB; (BENUMB); b. Old English n#mel, quick to seize, and numol, quick at learning, seizing: NIMB
LE. 2. Greek nemein, to allot: NEMESIS. 3. O-grade form *nom- in: a. Greek nomos, portion, usage, custom, law, division, district: NOME, -NOMY; ANOMIE, ANTINOMIAN, AN- TINOMY, (ASTRONOMER), (ASTRONOMY
), AUTONOMOUS, BINOMIAL, DEUTERONOMY, METRONOME, NOMOGRAM, NOMOGRAPH, NUMISMATICS; b. Greek nomé, pasturage, grazing, hence a spreading, a spreading ulcer: NOMA; c. Greek nomas, wandering in search o
f pasture: NOMAD; d. Greek nomimos, legal, probably borrowed in Latin nummus, coin: NUMMULAR, NUMMULATE. 4, Perhaps suffixed o-grade form *nom-eso- in Latin numerus, num- ber, division: NUMBER; ENUMER
ATE, SUPERNUMERARY. [Pok. 1. nem- 763.]
nepot-. Grandson, nephew. Feminine *nepti-. Latin nepos, grandson, nephew, and neptis, granddaughter, niece: NEPHEW, NEPOTISM, NIECE. [Pok. nepdt- 764.] ner-1, Under, also on the left; hence, with an
```


## [2026-09-07T18:27:09.963Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '130,180p' 0d5b80f03d535ee6.txt"
}
```


### [2026-09-07T18:27:10.003Z] TOOL RESULT

```
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 See also: άσφαλτος 

 Ancient Greek
 [ edit ] 

 Etymology
 [ edit ] 

 Generally taken as deriving from ἀ- ( a- , “ not ” ) +‎ σφάλλω ( sphállō , “ to fall, cast down ” ) , under the assumption that it denoted the material that protects walls from tumbling down. However, according to Beekes, the word is rather Pre-Greek .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ás.pʰal.tos/ → /ˈas.ɸal.tos/ → /ˈas.fal.tos/ 

 ( 5 th BCE Attic ) IPA ( key ) : /ás.pʰal.tos/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /ˈas.pʰal.tos/ 

 ( 4 th CE Koine ) IPA ( key ) : /ˈas.ɸal.tos/ 

 ( 10 th CE Byzantine ) IPA ( key ) : /ˈas.fal.tos/ 

 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈas.fal.tos/ 

 Noun
 [ edit ] 

 ἄσφᾰλτος • ( ásphăltos )  f or m ( genitive ἀσφᾰ́λτου ) ; second declension 

 asphalt , bitumen 

 Declension
 [ edit ]
```


## [2026-09-07T18:29:47.391Z] AGENT

Now I have enough evidence. Let me write the verification file.


## [2026-09-07T18:36:34.351Z] TOOL CALL #69: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-352.json <<'JSONEOF'\n{\n  \"pdf_page\": 352,\n  \"book_page\": 322,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ne 1, Nei 3, An 4\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *né 'not' (sentence negation), with the variants *nē, *ney and the zero-grade combining form *n̥- 'un-, not'\",\n      \"note\": \"Pokorny IEW 756-758 has exactly this headword complex: '1. ne, nē, nei Satznegation der reinen Verneinung (ne einzelsprachlich auch Wortnegation geworden); n̥- Wortnegation', so Nourai's three names map one-to-one onto Pokorny — Ne 1 = *ne, Nei 3 = *nei (Pokorny's separate paragraph 'nei betontes nicht'), An 4 = the zero-grade prefix *n̥- (Pokorny p. 758: 'n̥- Verneinungspartikel als erstes Glied: ai. av. ap. a-, vor Vokalen an-; gr. ἀ-, vor Vokal ἀν-; lat. in-, ältest en-'). Watkins (AHD appendix, s.v. 'ne. Not.') gives the same root with '8. Zero-grade combining form *n̥- in: a. Germanic *un-; b. Latin in-; c. Greek a-, an-; d. Sanskrit a-, an-' and cites [Pok. ne 756] — i.e. Nourai's own POK page. Language label 'Indo-European' and gloss 'no, not' are both correct. 'PART 2' is Nourai's continuation marker for a chart split over two pages.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *né «نه» (ادات نفی جمله) همراه با گونه‌های *nē و *ney و صورت درجهٔ صفر (بی‌واکه) *n̥- که در آغاز ترکیب، پیشوند نفی می‌سازد. پوکورنی در صفحهٔ ۷۵۶ دقیقاً همین مجموعه را زیر یک سرواژه آورده است و در صفحهٔ ۷۵۸ می‌نویسد که *n̥- در هندوایرانی a- (پیش از واکه an-)، در یونانی ἀ-/ἀν- و در لاتین in- (کهن‌تر en-) بازتاب یافته است؛ پس سه نام نورایی (Ne 1، Nei 3، An 4) و برگردان «نه» درست است. واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ AHD همین ریشه را با ارجاع به پوکورنی ۷۵۶ می‌آورد و کنت در صفحهٔ ۱۶۷ همان را از سوی پارسی باستان تأیید می‌کند. ادعای نورایی دربارهٔ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%CC%A5-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:756\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 418-420 (printed pp. 756-758): '1. ne, nē, nei Satznegation der reinen Verneinung (ne einzelsprachlich auch Wortnegation geworden); n- Wortnegation; ne-kʷo-s nicht einer ...' — the entry begins on p. 756 exactly as cited, and the privative section (Nourai's 'An 4') stands on pp. 757-758.\"},\n        {\"ref\": \"KNT:167\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 189 carries the printed page markers 167/168: 'an- neg. prefix before vowels, cf. ¹a- before consonants: Av. Skt. an-, Gk. ἀν-, Lt. in-, Gt. un-, pIE *ǝn- ($67.I); in Anāhitā-.' — Kent p. 167 is indeed the Old Persian negative prefix.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"Bd. I pp. 756-758 (POK_02.txt leaves 418-420)\", \"stance\": \"supports\", \"note\": \"'n- Verneinungspartikel als erstes Glied: ai. av. ap. a-, vor Vokalen (auch i, u) an-; gr. ἀ-, vor Vokal ἀν-; lat. in-, ältest en- (die vorkonsonantische Form)' (p. 757-758).\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II pp. 319-320 (WLD_Bd2_pages.txt ll. 21100-21178)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny II 319: 'Verneinungspartikel als erstes Zsglied: ai. av. ap. a-, von Vokalen (auch i, u) an-; arm. an-; gr. ἀ-, vor Vok. ἀν- ...; lat. in-, ältest en- (die vorkonsonantische Form)'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 774 s.v. ne (AHD_watkins1985.txt l. 774-775)\", \"stance\": \"supports\", \"note\": \"'ne. Not. ... 8. Zero-grade combining form *n̥- in: a. Germanic *un- in Old English un-, not: UN-1; b. Latin in-, not: IN-1; c. Greek a-, an-, not: A-1, (AN-); d. Sanskrit a-, an-, not. [Pok. ne 756.]'\"},\n        {\"src\": \"KNT\", \"where\": \"p. 167 s.v. an- (KNT.txt leaf 189)\", \"stance\": \"supports\", \"note\": \"quoted above; Kent reconstructs pIE *ǝn- for the prefix, i.e. the same zero grade.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"a-,an-; a-sěma; a-tomos; a-sphallein, asphaltos; a-sbenunai\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Greek privative ἀ- (before consonants) / ἀν- (before vowels) is the regular Hellenic reflex of the PIE zero grade *n̥-: syllabic *n̥ gave Proto-Hellenic *ə- and hence ἀ-, while before a vowel the nasal was preserved as ἀν- (AHD s.v. ne, 8c; Wiktionary Reconstruction:PIE/n̥- lists Proto-Hellenic *ə- among its descendants). The four illustrative compounds: (a) ἄσημος, neuter ἄσημον 'without a mark, unstamped' = ἀ- + σῆμα 'sign', the Hellenistic administrative term for unminted silver bullion (ἄσημον ἀργύριον) — Nourai's 'a-sěma' cites the noun σῆμα rather than the derived adjective, and he cross-refers to his root Sěma; (b) ἄτομος 'uncut, indivisible' = ἀ- + verbal adjective of τέμνω 'to cut', the technical term of Leucippus and Democritus in the 5th c. BCE (Klein: 'The word ἄτομος was first used by the Greek philosopher Leucippus'); (c) ἄσβεστος 'unquenchable, inextinguishable' = ἀ- + σβεστός, verbal adjective of σβέννυμι 'to quench' (Nourai writes the infinitive σβεννύναι), applied by Dioscorides to quicklime and later to the incombustible mineral; (d) ἄσφαλτος 'bitumen'. The one substantive problem is (d): the analysis ἀ- + σφάλλω 'to make fall, throw down' (whence the sense 'the material that keeps walls from tumbling down') is the traditional one and is what Nourai draws, but modern scholarship rejects it — Beekes calls the proposed etymology 'weak' and takes ἄσφαλτος as Pre-Greek, and Klein (following H. Lewy 1895) says it is 'of uncertain, possibly Semitic origin'. Hence 'plausible' for the node as a whole: the prefix itself and three of the four compounds are secure, the asphaltos analysis is not.\",\n          \"derivation_fa\": \"پیشوند نفی یونانی ἀ- (پیش از همخوان) و ἀν- (پیش از واکه) بازتاب قاعده‌مند صورت درجهٔ صفر هندواروپایی *n̥- است: *n̥ هجایی در یونانی آغازین به *ə- و سپس به ἀ- بدل شد و پیش از واکه، خیشومی به‌صورت ἀν- برجا ماند. چهار ترکیبی که نورایی می‌آورد: ἄσημος/ἄσημον «بی‌نشان، سکه‌نزده» از ἀ- + σῆμα «نشان» که در دورهٔ هلنی به نقرهٔ نامسکوک گفته می‌شد؛ ἄτομος «ناشکافتنی، تقسیم‌ناپذیر» از ἀ- + ستاک τέμνω «بریدن» که اصطلاح لوکیپوس و دموکریتوس در سدهٔ پنجم پیش از میلاد است؛ ἄσβεστος «خاموش‌نشدنی» از ἀ- + σβεστός (از σβέννυμι «خاموش کردن»). اما ἄσφαλτος: تحلیل سنتی آن (ἀ- + σφάλλω «افگندن») همان است که نورایی می‌آورد، ولی بیکس آن را «سست» می‌خواند و واژه را پیش‌یونانی می‌داند و کلاین آن را با احتیاط سامی می‌شمارد؛ پس این یک بند از گره، با احتیاط پذیرفتنی نیست و مجموع گره «با احتیاط پذیرفتنی» ارزیابی می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%84%CF%83%CF%86%CE%B1%CE%BB%CF%84%CE%BF%CF%82\",\n            \"https://www.etymonline.com/word/asphalt\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%CC%A5-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 p. 774 s.v. ne: '8. Zero-grade combining form *n̥- in ... c. Greek a-, an-, not: A-1, (AN-)'. Watkins does not treat asphalt (it is not of IE origin in his list), which is consistent with the doubt on that word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. asbestos, atom, asphalt (KLN_1966.txt ll. 3580, 3861, 3656)\", \"stance\": \"partial\", \"note\": \"'asbestos, n. — L. asbestos, fr. Gk. ἄσβεστος, lit. unquenchable, inextinguishable, fr. ἀ- (see priv. pref. a-) and σβεστός, verbal adj. of σβεννύναι, to quench' and 'atom, n. — F. atome, fr. L. atomus, fr. Gk. ἄτομος, prop. uncut, indivisible, fr. ἀ- and -τομος, fr. τέμνειν, to cut' — both support Nourai; but 'asphalt ... fr. Gk. ἄσφαλτος, which is of uncertain, possibly Sem. origin. See Heinrich Lewy, Die semitischen Fremdwörter im Griechischen, Berlin 1895, p. 53' contradicts the a- + sphallein analysis.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Asbestos (SKT.txt l. 1005); s.v. Un- (1) (l. 20415)\", \"stance\": \"supports\", \"note\": \"'Asbestos, a mineral. (Gk.) Gk. ἄσβεστος, unquenchable; because it is incombustible. — Gk. ἀ-, neg. prefix; and σβεστός, quenchable, from σβέννυμι, I quench, extinguish.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 319\", \"stance\": \"supports\", \"note\": \"'gr. ἀ-, vor Vok. ἀν-' listed as the Greek reflex of the privative particle.\"},\n            {\"src\": \"Wiktionary/Beekes\", \"where\": \"en.wiktionary.org s.v. ἄσφαλτος; Etymonline s.v. asphalt\", \"stance\": \"contradicts\", \"note\": \"'Generally taken as deriving from ἀ- + σφάλλω ... under the assumption that it denoted the material that protects walls from tumbling down. However, according to Beekes, the word is rather Pre-Greek.' Etymonline adds that Beekes 'finds this proposed etymology weak. Perhaps from Semitic [Klein, citing Lewy, 1895] or another non-Greek source.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"asěm; sîm\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian asēm (Book Pahlavi ʾsym, Manichaean ʾsym) 'silver' is a Hellenistic loan from Greek ἄσημον, the neuter of ἄσημος 'unstamped', which in Ptolemaic and Seleucid usage meant unminted silver bullion (ἄσημον ἀργύριον); the Greek ἄ- was still audible as Iranian a-, and Greek -η- was rendered by Middle Persian -ē-. Nyberg states the borrowing outright: 'asēm [sym] silver 118⁸. — Borrowed from Gr. ἄσημον; MPrs ʾsym (A-H II); NP sīm'. MacKenzie has 'asem [ʾsym | = M, N sīm] silver' and, separately, 'sem [sym | N —] = asem', i.e. the aphetic by-form without a- already existed inside Middle Persian — which is exactly why Nourai puts asēm and sīm side by side in one Pahlavi node. The same Greek word gave Parthian hasēm and Armenian asem. Hübschmann and Horn both label NP sīm / Phl. asīm a Greek loanword. The arrow Greek → Pahlavi is therefore right, and the Pahlavi node correctly hangs under the Greek a-sēma node rather than under the root.\",\n          \"derivation_fa\": \"فارسی میانهٔ asēm (پهلوی کتابی ʾsym) «نقره» وام‌واژه‌ای است از یونانی ἄσημον، صورت خنثای ἄσημος «سکه‌نزده، بی‌نشان»، که در دیوان‌های هلنی به نقرهٔ نامسکوک (ἄσημον ἀργύριον) گفته می‌شد؛ «ای» کشیدهٔ یونانی (η) در فارسی میانه به ē بدل شده است. نیبرگ صریحاً می‌نویسد: «asēm [sym] نقره ... وام‌گرفته از یونانی ἄσημον؛ فارسی میانهٔ ʾsym؛ فارسی نو sīm». مکنزی هم asēm و هم گونهٔ کوتاه‌شدهٔ sēm را ثبت کرده است، یعنی افتادن «الف» آغازین از همان دورهٔ فارسی میانه آغاز شده بود — و همین است که نورایی هر دو صورت را در یک گره پهلوی گذاشته است. همین واژه در پارتی hasēm و در ارمنی asem بازتاب یافته. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KNT:209\", \"status\": \"not_found\", \"note\": \"Kent's Old Persian lexicon has no word for silver but ardata- (KNT.txt l. 5068: 'ardata- sb. silver: Av. ardzata-, Skt. rajatá-, cf. Gk. ἄργυρος, Lt. argentum'), and no asēm/sīm entry anywhere (grep -n -i 'asem|silver' KNT.txt). The local scan also breaks off at printed pp. 206-207 (last leaf 231, headword vaj-), so p. 209 itself could not be read; alphabetically p. 209 would fall in the s/š/h range. The citation looks misplaced — the claim is supported instead by PHD, NYB, HRN and HUB.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. asem and s.v. sem (PHD_mackenzie.txt ll. 1216, 4540, 7582)\", \"stance\": \"supports\", \"note\": \"'asem [ʾsym | = M, N sim] silver.' / 'sem [sym | N -] = asem.' / English index: 'silver (a)sem; (a.) asemen.'\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary s.v. asēm (NYB_vol2_glossary.txt l. 682)\", \"stance\": \"supports\", \"note\": \"'asēm [sym] silver 118⁸. — Borrowed from Gr. ἄσημον; MPrs ʾsym (A-H II); NP sim.'\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien, list of words with loss of initial a- (HUB.txt l. 4215)\", \"stance\": \"supports\", \"note\": \"'sīm Silber = phl. asīm, gr. ἄσημος (Nöldeke, Pers. Stud. II, 45)' — cited in the same series as sāgird = paz. asāgard, vīrān = paz. avīrān.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss p. 169, no. 764 (HRN.txt l. 6658)\", \"stance\": \"supports\", \"note\": \"'Np. sīm Silber, sīmīn silbern (phlv. asīm, asīmīn) dagegen ist bekanntlich griechisches Lehnwort (vergl. zuletzt Nöldeke, Pers. Stud. II, 45).'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"sîm 2\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian سیم sīm 'silver' continues MP asēm by aphesis of the unstressed initial a-, one of the best-documented New Persian changes: Hübschmann lists sīm : phl. asīm in the very same series as šāgird : paz. asāgard, vīrān : paz. avīrān, zēr : paz. azēr. Mo'in's etymological footnote in his edition of Borhan-e Qate', quoted verbatim by Dehkhoda s.v. سیم, gives the whole story Nourai draws: 'پهلوی «اسیم»، در فارسی «آ» از اول کلمه (پهلوی) حذف شده، اما سیمین در پهلوی آمده ... برخی از محققان معاصر اصل سیم را یونانی دانند ... (از: «اء»، علامت نفی و «سما»، نشانه نهاده و علامت گذاشته) ... جمعاً یعنی نقره نامسکوک (از افادات شفاهی بنونیست)' — i.e. Greek a- privative + sēma 'mark' = 'unstamped silver', on Benveniste's authority, exactly Nourai's a-sēma. Mo'in's own dictionary tags سیم simply '[په.]' (Pahlavi). The two secondary senses Nourai notes are later Persian developments: 'mercury' through سیماب sīmāb, literally 'silver-water' (quicksilver), and 'wire' (سیم برق) a 19th-20th c. extension from the silvery colour of drawn metal. Wiktionary agrees on the route (MP (ʾ)sym /(a)sēm/ from Ancient Greek ἄσημον, neuter of ἄσημος) but inserts a doubtful Old Persian siyamam between them.\",\n          \"derivation_fa\": \"«سیم» فارسی نو ادامهٔ asēm فارسی میانه است با افتادن «الف» بی‌تکیهٔ آغازین — همان دگرگونی آوایی که در «شاگرد» (< ašāgird)، «ویران» (< avīrān) و «زیر» (< azēr) دیده می‌شود و هوبشمان سیم را در همین فهرست آورده است. حاشیهٔ ریشه‌شناختی معین بر برهان قاطع، که دهخدا واژه‌به‌واژه نقل کرده، همان زنجیرهٔ نورایی را می‌دهد: «پهلوی اسیم، در فارسی آ از اول کلمه حذف شده ... برخی از محققان معاصر اصل سیم را یونانی دانند ... از «اء» علامت نفی و «سما» نشانه ... جمعاً یعنی نقرهٔ نامسکوک (از افادات شفاهی بنونیست)». دو معنی دیگر (سیماب/جیوه و سیم برق) تحول معنایی متأخر فارسی است، نه بخشی از وام‌گیری. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85\",\n            \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%85/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KNT:209\", \"status\": \"not_found\", \"note\": \"as for node 2: Kent has no sīm/asēm entry (his silver word is ardata-, p. 170) and the local scan ends at pp. 206-207, so p. 209 could not be read.\"},\n            {\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"Mo'in's footnote in Borhan-e Qate', quoted by Dehkhoda s.v. سیم (abadis.ir): 'پهلوی «اسیم» ... برخی از محققان معاصر اصل سیم را یونانی دانند ... جمعاً یعنی نقره نامسکوک (از افادات شفاهی بنونیست) ... (از حاشیه برهان قاطع چ معین)' — the Greek a- + sēma etymology exactly as charted.\"},\n            {\"ref\": \"MON\", \"status\": \"partial\", \"note\": \"Farhang-e Mo'in s.v. سیم (via abadis.ir) gives only the origin tag '[په.]' (Pahlavi) with the senses 'نقره / پول / فلز قیمتی / مفتول، رشتهٔ باریک فلزی' — it confirms the Pahlavi source and the 'wire' sense but the online text does not carry the Greek step (which is in Mo'in's Borhan footnote instead).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"p. 169 no. 764 (HRN.txt l. 6658)\", \"stance\": \"supports\", \"note\": \"'Np. sīm Silber, sīmīn silbern (phlv. asīm, asīmīn) ... ist bekanntlich griechisches Lehnwort'.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l. 4215\", \"stance\": \"supports\", \"note\": \"'sīm Silber = phl. asīm, gr. ἄσημος' in the list of Persian words that lost an initial a-.\"},\n            {\"src\": \"MON\", \"where\": \"vajehyab/abadis, فرهنگ معین s.v. سیم\", \"stance\": \"partial\", \"note\": \"tag '[په.]' only; senses include 'مفتول، رشتهٔ باریک فلزی' (wire), which supports Nourai's gloss.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt l. 1216, 4540\", \"stance\": \"supports\", \"note\": \"MacKenzie already gives the New Persian outcome in the entry: 'asem [ʾsym | = M, N sim] silver'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through node: the Latin transmission of the Greek privative compounds, not of the prefix itself (Latin's own reflex of *n̥- is in-, node 8, which Nourai correctly hangs off the root). Latin took over atomus (Cicero, and Lucretius' rendering of Democritus), Late Latin asphaltus/asphaltum, and asbestos, changing nothing but the ending. Klein: 'atom, n. — F. atome, fr. L. atomus, fr. Gk. ἄτομος'; 'asphalt also asphaltum, n. — F. asphalte, fr. Late L. asphaltus, fr. Gk. ἄσφαλτος'; 'asbestos, n. — L. asbestos, fr. Gk. ἄσβεστος'.\",\n          \"derivation_fa\": \"این گره تهی است و تنها نقش گذرگاه دارد: انتقال ترکیب‌های پیشوند نفی یونانی به لاتین، نه انتقال خود پیشوند (بازتاب لاتینی *n̥- همان in- است که نورایی درست از خود ریشه آویخته است). لاتین atomus، asphaltus/asphaltum متأخر و asbestos را بی هیچ دگرگونی جز پایانهٔ صرفی وام گرفت. کلاین برای هر سه واژه همین راه یونانی > لاتین را می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/asphalt\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. atom, asphalt, asbestos (KLN_1966.txt ll. 3861, 3656, 3580)\", \"stance\": \"supports\", \"note\": \"'fr. L. atomus' / 'fr. Late L. asphaltus' / 'L. asbestos, fr. Gk. ἄσβεστος'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Asbestos (SKT.txt l. 1005), Atom (l. 1097 'Atom; see Tomo')\", \"stance\": \"supports\", \"note\": \"Skeat routes both through Latin from Greek.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through node: the French learned forms atome (attested 13th c.), asphalte (16th c., re-established in the modern technical sense in the 19th c.) and asbeste, which became the international scientific vocabulary and are the immediate donors for the Persian words in node 6 and for much of the English in node 7. Klein gives the step explicitly: 'atom, n. — F. atome, fr. L. atomus' and 'asphalt also asphaltum, n. — F. asphalte, fr. Late L. asphaltus'.\",\n          \"derivation_fa\": \"گرهی تهی و گذرگاهی: صورت‌های فرانسوی و فرهیختهٔ atome (از سدهٔ سیزدهم)، asphalte (سدهٔ شانزدهم و احیای معنای فنی آن در سدهٔ نوزدهم) و asbeste که واژگان علمی بین‌المللی از آنها ساخته شد و همین‌ها وام‌دهندهٔ بی‌واسطهٔ واژه‌های فارسی گرهِ بعدی هستند. کلاین این پله را صریح می‌آورد: «atom از فرانسوی atome از لاتین atomus» و «asphalt از فرانسوی asphalte». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/asphalt\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. atom, asphalt (KLN_1966.txt ll. 3861, 3656)\", \"stance\": \"supports\", \"note\": \"'F. atome' and 'F. asphalte' named as the immediate sources of the English words.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/asphalt\", \"stance\": \"supports\", \"note\": \"'from Late Latin asphaltum, from Greek asphaltos ... The meaning paving composition of tar and gravel dates from 1847' — the 19th-c. technical revival that carried the word into Persian through French.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"atom «اتُم»; âsfâlt «آسفالت ( اسفالت ، آسفالته )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are 20th-century European loans that reached Persian through French, the language of Iranian technical, military and administrative modernisation from the late Qajar period onward: Fr. atome > اتم otom/atom, Fr. asphalte > آسفالت āsfālt, with the spelling variant اسفالت and the adjectival آسفالته from French asphalté 'asphalted'. That final -e of آسفالته is decisive for French rather than English or Russian mediation, and آ- for the Greek/French initial a- reflects the French open [a]. Ottoman Turkish آسفالت asfalt, the neighbouring parallel, is likewise 'borrowed from French asphalte, from Ancient Greek ἄσφαλτος' (Wiktionary). So the chart's route Greek > Latin > French > Persian is right; note that the Greek internal analysis of asphaltos is itself doubtful (see node 1), but that does not affect this borrowing chain.\",\n          \"derivation_fa\": \"«اتم» و «آسفالت» هر دو وام‌واژه‌های سدهٔ بیستم‌اند که از راه فرانسوی به فارسی رسیده‌اند، یعنی زبانی که در دورهٔ قاجار و پهلوی واژگان فنی و اداری ایران را می‌ساخت: از atome فرانسوی «اتم» و از asphalte فرانسوی «آسفالت» با گونهٔ نوشتاری «اسفالت» و صفتِ «آسفالته» از asphalté فرانسوی. همان «ـه» پایانی «آسفالته» گواه قطعی میانجی‌گری فرانسوی (نه انگلیسی) است، و «آ» آغازین نیز بازتاب واکهٔ گشودهٔ فرانسوی است. در ترکی عثمانی نیز asfalt را وام‌گرفته از asphalte فرانسوی و آن را از ἄσφαλτος یونانی دانسته‌اند. پس مسیر یونانی > لاتین > فرانسوی > فارسی درست است؛ تنها تحلیل درونی خود واژهٔ یونانی (بند گرهِ یونانی) مورد تردید پژوهش امروزی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA\",\n            \"https://www.etymonline.com/word/asphalt\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"VOP\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e vāžehā-ye orupāyi dar fārsi (Alborz 1371) is exactly the right authority for these two words but no copy exists online: refs_online.json records 'RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook' (archive.org, ketabnak, noorlib all checked).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. آسفالت (Ottoman Turkish)\", \"stance\": \"supports\", \"note\": \"'Borrowed from French asphalte (asphalt), from Ancient Greek ἄσφᾰλτος (ásphăltos, asphalt, bitumen)' — the same French route as the Persian word.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. atom, asphalt (KLN_1966.txt ll. 3861, 3656)\", \"stance\": \"supports\", \"note\": \"establishes the Greek > Latin > French forms that Persian borrowed.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi vol. 4 (foreign compounds) — not available online\", \"stance\": \"silent\", \"note\": \"the volume that would carry اتم / آسفالت is not among the digitised Mo'in volumes (vajehyab and abadis serve only the lexicon volumes).\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"a-, an-, atom, asphalt, asbestos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English a-/an- 'not' is a learned prefix borrowed together with Greek vocabulary (amoral, anaemia), not the inherited reflex of *n̥-, which in English is un-; Watkins accordingly lists both under the same root: 'Zero-grade combining form *n̥- in: a. Germanic *un- in Old English un-: UN-1; ... c. Greek a-, an-, not: A-1, (AN-)'. atom entered English from French atome / Latin atomus (1477 in the Latin form, 'atom' from the 1590s); asphalt is attested from early 14c. in the biblical sense 'hard resinous mineral pitch', with the modern paving sense from 1847 which fixed the form asphalt over asphaltum/asphaltos; asbestos comes through Latin from Greek. All three are Greek-via-Latin-via-French learned words, exactly as the chart draws them under the Latin node.\",\n          \"derivation_fa\": \"پیشوند a-/an- در انگلیسی وام‌واژه‌ای فرهیخته است که همراه واژگان یونانی گرفته شده (amoral، anaemia) و بازتاب موروثی *n̥- در انگلیسی همان un- است؛ واتکینز هر دو را زیر یک ریشه می‌آورد. atom از atome فرانسوی و atomus لاتین (صورت لاتین از ۱۴۷۷ و صورت atom از دههٔ ۱۵۹۰)؛ asphalt از آغاز سدهٔ چهاردهم به معنای قیر معدنی کتاب مقدس و معنای امروزی «سنگ‌فرش قیری» از ۱۸۴۷ که همین صورت را تثبیت کرد؛ asbestos از راه لاتین از یونانی. هر سه وام‌واژه‌های فرهیختهٔ یونانی–لاتینی–فرانسوی‌اند، درست همان‌گونه که نمودار نشان می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/asphalt\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 p. 774 s.v. ne: '8. Zero-grade combining form *n̥- in ... b. Latin in-, not: IN-1; c. Greek a-, an-, not: A-1, (AN-)'; the English index lists 'NOT ne, wekti-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. atom, asphalt, asbestos (KLN_1966.txt ll. 3861, 3656, 3580)\", \"stance\": \"supports\", \"note\": \"gives the full Greek > Latin > French > English chain for each word.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Asbestos, Atom, Un- (1) (SKT.txt ll. 1005, 1097, 20415)\", \"stance\": \"supports\", \"note\": \"'Un- (1), neg. prefix. (E.) A.S. un-, neg. prefix + ... Goth. un-, G. un-, W. an-, L. in-, Gk. ἀν-, ἀ-' — the inherited English member of the same set.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/asphalt\", \"stance\": \"supports\", \"note\": \"'early 14c., hard, resinous mineral pitch found originally in Biblical lands, from Late Latin asphaltum ... The meaning paving composition of tar and gravel dates from 1847.'\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"in-\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin privative in- is the Italic reflex of the zero grade *n̥-: syllabic *n̥ yielded Proto-Italic *n̥- and Latin en- (the oldest, preconsonantal shape) > in-, with the assimilations im- before b, p, m (imberbis, improbus), il- before l (illaudatus), ir- before r (irritus) and i- before gn- (ignotus, matching Skt. ajñātaḥ and Gk. ἄγνωτος word for word). Before a vowel Latin in- is analogical, since one would expect *en-. Ernout-Meillet state precisely this: 'In- représente la forme à degré zéro *n̥- de la négation ne; devant consonne, il répond à indo-iran. a-, gr. ἀ-, germ. un-, celt. an-; un composé comme ignotus répond exactement à skr. ajnatah, gr. ἄγνωτος.' Note that Nourai correctly draws this arrow off the root and not off the Greek node — Latin in- is inherited, not borrowed.\",\n          \"derivation_fa\": \"پیشوند نفی لاتین in- بازتاب ایتالیکی صورت درجهٔ صفر *n̥- است: *n̥ هجایی در ایتالیکی آغازین *n̥- و در لاتین نخست en- (صورت پیش‌همخوانی کهن) و سپس in- شد، با همگونی‌های im- پیش از b، p، m (imberbis، improbus)، il- پیش از l (illaudatus)، ir- پیش از r (irritus) و i- پیش از gn- (ignotus که واژه‌به‌واژه برابر ajñātaḥ سنسکریت و ἄγνωτος یونانی است). ارنو و مییه همین را می‌گویند. نکتهٔ درست نمودار این است که نورایی این پیکان را از خود ریشه کشیده، نه از یونانی؛ زیرا in- لاتین موروثی است نه وام‌گرفته. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%CC%A5-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 p. 774 s.v. ne: '8. Zero-grade combining form *n̥- in ... b. Latin in-, not: IN-1 ... [Pok. ne 756.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet pp. 556-557 s.v. in- (LAT.txt ll. 29608-29660)\", \"stance\": \"supports\", \"note\": \"'in- (im- devant labiale b,p,m ...; il- devant l ...; ir- devant r ...; nasale gutturale dans ignotus): préfixe privatif ... In- représente la forme à degré zéro *n̥- de la négation ne'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 319\", \"stance\": \"supports\", \"note\": \"'lat. in-, ältest en- (die vorkonsonantische Form)'.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 758\", \"stance\": \"supports\", \"note\": \"'lat. in-, ältest en- (die vorkonsonantische Form)' in the list of reflexes of the privative n̥-.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/n̥-\", \"stance\": \"supports\", \"note\": \"'Zero grade form of the sentence negative *né ... Descendants: ... Proto-Italic: *n̥- (see there for further descendants)'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"in- 2, ineffective\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English privative in- is borrowed wholesale from Latin, partly through Old French, partly directly in learned coinages; dictionaries number it separately from the native/locative in- (Klein has two consecutive entries, 'in-, pref. meaning in, into, toward, up, against' and 'in-, privative pref., as in inadvertence. — L. in-, not, cogn. with Goth., OE. un, not'), which is exactly what Nourai's label 'in- 2' records. ineffective (1650s) is a Latin-type formation made inside English on effective, with the Latin assimilation rules still active for other bases (illegible, immobile, irregular). Watkins routes it to the same root: 'Latin in-, not: IN-1 ... [Pok. ne 756]'.\",\n          \"derivation_fa\": \"پیشوند نفی in- در انگلیسی یکسره از لاتین وام گرفته شده است، بخشی از راه فرانسوی کهن و بخشی مستقیم در واژه‌سازی فرهیخته؛ فرهنگ‌نویسان آن را از in- بومی/مکانی جدا شماره می‌کنند (کلاین دو مدخل پیاپی دارد: «in- به معنای در، به‌سوی» و «in- پیشوند نفی ... از لاتین in- «نه»، هم‌ریشه با un- گوتی و انگلیسی کهن») و همین است که نورایی آن را «in- 2» می‌نامد. واژهٔ ineffective (دههٔ ۱۶۵۰) ساختی لاتین‌گونه است که درون انگلیسی بر پایهٔ effective ساخته شده، در حالی که قاعده‌های همگونی لاتین در واژه‌های دیگر (illegible، immobile، irregular) هنوز کارآمدند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%CC%A5-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 p. 774 s.v. ne: '8. ... b. Latin in-, not: IN-1'; the reference list of the appendix gives [Pok. ne 756].\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. in- (privative pref.) (KLN_1966.txt l. 18998)\", \"stance\": \"supports\", \"note\": \"'in-, privative pref., as in inadvertence. — L. in-, not, cogn. with Goth., OE. un, not; see un-, priv. pref. L. in-, not, becomes i- before gn, il- before l, im- before b, m and p, ir- before r.'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Un- (1) and N- (1) (SKT.txt ll. 20415, 22094)\", \"stance\": \"supports\", \"note\": \"'Un- (1), negative prefix to nouns, &c. (E.) A.S. un-, not; cognate with L. in-, not, Gk. ἀν-, not.'\"},\n            {\"src\": \"LAT\", \"where\": \"pp. 556-557 s.v. in-\", \"stance\": \"supports\", \"note\": \"documents the Latin prefix that English borrowed, and its enormous late-Latin and ecclesiastical productivity, which is the source of the English type.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Ne 2, Nes 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *nes- / *n̥s- (also *nō̆s), the oblique stem of the 1st person plural pronoun (nominative *wéy)\",\n      \"note\": \"Pokorny IEW 758 has the entry verbatim: '3. ne-, no-, Plur. nes-, nos- wir (ursprüngl. außerhalb des Nominativs; Nom. s. unter *we-)', so Nourai's headword pair 'Ne 2, Nes 2' and, importantly, his gloss 'our, us' rather than 'we' both come straight from Pokorny. Walde-Pokorny II 320 has the same entry with the same wording. Pokorny 758 also supplies the entire Iranian and Germanic content of this chart in two sentences: 'auf *n̥sme (wohl n̥s + Partikel *sm-) beruhen av. ahma (ai. asmān, ap. Gen. amāxam) = äol. ἄμμε ...; Poss. lesb. ἄμμος, dor. ἁμός = av. ahma-' and 'got. ahd. uns, as. ūs, anord. oss uns (*n̥s)'. Watkins files it as 'nes-2, Oblique cases of the personal pronoun of the first person plural. For the nominative see we-. ... [Pok. 3. ne- 758.]' Modern handbooks (Sihler, Wiktionary) present the same forms as the oblique paradigm of *wéy — accusative *n̥smé ~ *nō̆s, genitive *n̥sóm ~ *nō̆s — which is a reorganisation of the presentation, not a disagreement about the forms.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *nes-/*n̥s- (و *nō̆s)، یعنی ستاک غیرفاعلی ضمیر اول شخص جمع که فاعلی آن *wéy است. پوکورنی در صفحهٔ ۷۵۸ عیناً می‌نویسد: «3. ne-, no-, جمع nes-, nos- «ما» (در اصل بیرون از حالت فاعلی؛ فاعلی را زیر *we- ببینید)»، پس هم دو سرواژهٔ نورایی و هم — که مهم‌تر است — برگردان او «مالِ ما، ما را» (نه «ما») درست و برگرفته از پوکورنی است. والده-پوکورنی جلد دوم صفحهٔ ۳۲۰ همان را دارد. پوکورنی در همان صفحه سراسر شاخهٔ ایرانی و ژرمنی این نمودار را نیز می‌دهد: «صورت‌های اوستایی ahma (سنسکریت asmān، اضافهٔ پارسی باستان amāxam) بر *n̥sme استوارند» و «گوتی و آلمانی علیای کهن uns، ساکسون کهن ūs، نورس کهن oss از *n̥s». پژوهش امروزی همین صورت‌ها را در جدول صرفی *wéy می‌گنجاند که تنها تغییر شیوهٔ عرضه است، نه اختلاف. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9y\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nes-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:758\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 420-421 (printed p. 758): '3. ne-, no-, Plur. nes-, nos- wir (ursprüngl. außerhalb des Nominativs; Nom. s. unter *we). 1. Ai. Du. Akk. Dat. Gen. nau ... 2. Pluralisch: ai. nah enklit., av. nə, nā, nō, lat. nōs ... got. ahd. uns, as. ūs, anord. oss uns (*n̥s) ... auf *n̥sme ... beruhen av. ahma (ai. asmān, ap. Gen. amāxam)'. Both the root and half the nodes of this chart are on that one page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 320 (WLD_Bd2_pages.txt ll. 21137, 21179)\", \"stance\": \"supports\", \"note\": \"running head 'ne-, no-, nes-, nos-' on p. 320 and the entry 'ne-, no-, plur. nes-, nos- wir (ursprgl. außerhalb des Nominativs; Nom. s. u. ...)'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 784 s.v. nes-2 (AHD_watkins1985.txt l. 784)\", \"stance\": \"supports\", \"note\": \"'nes-2, Oblique cases of the personal pronoun of the first person plural. For the nominative see we-. 1. Zero-grade form *n̥s- in Germanic *uns ... 3. O-grade form *nos-, with suffixed (possessive) form *nos-t(e)ro-, in Latin nōs, we, and noster, our. [Pok. 3. ne- 758.]'\"},\n        {\"src\": \"KLN\", \"where\": \"vol. II s.v. us (KLN_1966.txt l. 40905)\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *n̥s-, for *nes, *nōs, we; cogn. with OI. nas, us, Avestic na, us, ... Avestic ahma (for I.-E. *n̥sme), we, L. nōs, we, us, OSlav. ny, us, nasu, our, OPruss. nouson, our.'\"},\n        {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/wéy (Sihler's paradigm)\", \"stance\": \"partial\", \"note\": \"'accusative *n̥smé ~ *nō̆s; genitive *n̥sóm ~ *nō̆s ... Oblique plural *n̥s- possibly continues earlier **m̥s-' — the same forms, presented as the oblique of *wéy rather than as a separate root; the 'nes-' reconstruction page itself is a bare stub.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"na 2; ahma, ahmâka\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Two distinct things are correctly gathered here. (a) The Avestan enclitic nā / nə / nō 'us, to us, our' is the direct Iranian continuation of the unaccented PIE *nos / *n̥s (Pokorny 758: 'ai. nah enklit., av. nə, nā, nō'; Klein s.v. us: 'cogn. with OI. nas, us, Avestic na, us'). (b) The tonic stem Av. ahma- goes back to *n̥s-me-, the zero grade *n̥s- extended by the pronominal particle *-sme- (the same -sm- as in Skt. ta-sm-āt): Proto-Iranian *n̥sma- > *asma- > Av. ahma-, by the regular Iranian change of *s to h before a nasal / in this cluster (compare Av. haoma- : Skt. sóma-, Av. hapta : Skt. saptá). Its Greek counterparts are Aeolic ἄμμε, Doric ἁμέ, Ionic-Attic ἡμεῖς. Beside it stands the possessive adjective ahmāka- 'our' (Bartholomae AiW 297: 'j., g. ahmāka- Adj. unsrig, unser'), whose genitive plural ahmākəm is the form that survives into Middle Persian. One gloss caveat: Nourai renders both ahma- and ahmāka- as 'we', whereas ahma- is strictly the oblique stem 'us' (the Avestan nominative is vaēm) and ahmāka- is 'our' — the entry's own root gloss 'our, us' is the accurate one.\",\n          \"derivation_fa\": \"در این گره دو چیز جداگانه — و به‌درستی — یک‌جا آمده است. نخست، ضمیر پی‌بستی اوستایی nā/nə/nō «ما را، مالِ ما» که ادامهٔ مستقیم *nos/*n̥s بی‌تکیهٔ هندواروپایی است (پوکورنی ۷۵۸: «سنسکریت naḥ پی‌بستی، اوستایی nə، nā، nō»). دوم، ستاک تکیه‌دار اوستایی ahma- که از *n̥s-me- می‌آید، یعنی درجهٔ صفر *n̥s- به‌افزودهٔ جزء ضمیری *-sme- (همان -sm- در ta-sm-āt سنسکریت): ایرانی آغازین *n̥sma- > *asma- > اوستایی ahma- بر پایهٔ دگرگونی آوایی قاعده‌مند «س» ایرانی باستان به «ه» در این خوشه (سنجیدنی با haoma- اوستایی برابر sóma- سنسکریت و hapta برابر saptá). برابرهای یونانی آن ἄμμε ائولیایی و ἡμεῖς یونی-آتیکی است. در کنارش صفت ملکی ahmāka- «مالِ ما» است که بارتولومه در ستون ۲۹۷ فرهنگ ایرانی باستان آورده و اضافهٔ جمع آن ahmākəm همان صورتی است که به فارسی میانه می‌رسد. تنها نکته: نورایی برگردان هر دو را «ما» داده، حال آنکه ahma- ستاک غیرفاعلی «ما را» است (فاعلی اوستایی vaēm است) و ahmāka- «مالِ ما»؛ برگردانی که خودِ نورایی برای ریشه آورده («مالِ ما، ما را») دقیق است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9y\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:758\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 420: '2. Pluralisch: ai. nah enklit., av. nə, nā, nō, lat. nōs ...' and 'auf *n̥sme (wohl n̥s + Partikel *sm-, verwandt mit dem -sm- der Pron.-Dekl., z. B. ai. tá-sm-āt) beruhen av. ahma (ai. asmān, ap. Gen. amāxam) = äol. ἄμμε ...; Poss. lesb. ἄμμος, dor. ἁμός = av. ahma-'. Exactly Nourai's node.\"},\n            {\"ref\": \"KLN:1683\", \"status\": \"supports\", \"note\": \"Klein s.v. us (KLN_1966.txt l. 40905; the two-volume 1966-67 edition runs to p. 1776 and 'us' falls at p. 1683): 'us, objective case of we. — ME. ous, us, fr. OE. ūs ... fr. I.-E. base *n̥s-, for *nes, *nōs, we; cogn. with OI. nas, us, Avestic na, us, ... Avestic ahma (for I.-E. *n̥sme), we, L. nōs, we, us'. Both of Nourai's Avestan forms (na, ahma) stand in that one entry. The local scan carries no printed page numbers, so the page itself could not be re-read, but the content matches the citation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 296-297 s.v. ahma-, ahmāka- (BRT.txt ll. 6922, 6935)\", \"stance\": \"supports\", \"note\": \"'j., g. ahma-, g. əhma-, p. amā- Pron. I. Pers. Plur. uns (usw.)' with the Old Persian examples 'xšaçam tyaʰ hacā amāxam taumāyā parābartam āha Bh. 1.14'; and 'j., g. ahmāka- Adj. unsrig, unser'. Bartholomae files the Old Persian genitive amāxam under the Avestan stem, i.e. supports the node and shows that ahmāka- means our, not we.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 758\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n            {\"src\": \"KLN\", \"where\": \"vol. II s.v. us\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary s.v. amāh (NYB_vol2_glossary.txt l. 374)\", \"stance\": \"supports\", \"note\": \"'Av. (295 sq.) gen. ahmākəm, OP amāxam' — Nyberg's own etymological note, agreeing on the Avestan starting point.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"amâg, amâh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian amāh 'we, us' (Book Pahlavi written with the Aramaic logogram LNE / 𐭫𐭭𐭤, Manichaean and Turfan ʾmʾh, Parthian LN) continues Old Iranian *ahmākam, the genitive plural of ahma- / ahmāka-, which was generalised to serve as the whole non-enclitic first person plural pronoun. Phonetically: the cluster *hm simplified to m, the final syllable *-am was lost, and the intervocalic *-k- was lenited and voiced to -h- (*ahmākam > *amāhak > amāh), the same lenition seen in MP šāh < OP xšāyaθiya-type intervocalic weakening and in MP dēh < *dahyu-. Nyberg's glossary gives both the form and the etymology: 'amāh [LNH, Prth LN] pers. pron. 1st p. pl. ... — Av. (295 sq.) gen. ahmākəm, OP amāxam; MPrthPrs ʾmʾh; Paz. ema; NP mā'. MacKenzie: 'amā [LNE < A l-nh | M ʾmʾh, N mā] we, us.' Nourai's first form amāg is the -g reading of the same word: the glossary of Šāyast nē Šāyast indexes it as 'amah/amag 232/3', i.e. page 232 line 3 with the Pahlavi spelling ʾmʾh at line 5 — so both of Nourai's forms and his page reference are exactly right, even though MacKenzie and Nyberg print only amā(h).\",\n          \"derivation_fa\": \"فارسی میانهٔ amāh «ما» (در پهلوی کتابی با هزوارش آرامی LNE، در مانوی و اوراق تورفان ʾmʾh، در پارتی LN) ادامهٔ *ahmākam ایرانی باستان است، یعنی اضافهٔ جمع ahma-/ahmāka- که سپس به‌جای تمام ضمیر جدای اول شخص جمع به کار رفت. از نظر آوایی: خوشهٔ *hm به m ساده شد، هجای پایانی *-am افتاد و *-k- میان‌واکه‌ای نرم و به «ه» بدل شد (*ahmākam > *amāhak > amāh) — همان نرم‌شدگی میان دو واکه که در dēh < *dahyu- نیز دیده می‌شود. نیبرگ هم صورت و هم ریشه را می‌دهد: «amāh ... اوستایی اضافهٔ ahmākəm، پارسی باستان amāxam؛ فارسی میانه و پارتی ʾmʾh؛ پازند ema؛ فارسی نو mā». مکنزی صورت amā را ثبت کرده است. صورت نخست نورایی، amāg، خوانش با «گ» همان واژه است: واژه‌نامهٔ شایست نه شایست آن را دقیقاً «amah/amag ۲۳۲/۳» فهرست کرده، یعنی صفحهٔ ۲۳۲ سطر ۳ (و املای پهلوی ʾmʾh در سطر ۵)؛ پس هر دو صورت و شمار صفحهٔ نورایی درست است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1931\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 1931 (vol. 4 scan pdf p. 14; rendered to data/verification/sources/refs/ocr/BQT/1931.png, read by vision and saved as 1931.vision.txt): 'ما – پهلوی amâh (ما)، پارسی باستان amâxam، اوستا ahmâkəm، اوراق تورفان amâh «نیبرگ ص ۷»، پازند êmâ، هندی باستان asmáka- ...'. Mo'in's footnote gives the Pahlavi form as amâh (not amâg) and the whole chain of the chart.\"},\n            {\"ref\": \"SNS:232\", \"status\": \"supports\", \"note\": \"Tavoosi, Vazhe-name-ye Shayast ne Shayast: the Pahlavi index (SNS_pages.txt l. 16498) has 'amah/amag 232/3' and the Pahlavi-script index (l. 15607) 'ʾmʾh 232/5'; the page itself (l. 9255) shows ':amag/amah:'. So p. 232 carries both readings, and the same page comparatively lists OP amaxam- and Skt. asmāka- (index ll. 15082, 14998, both '232/4') — precisely Nourai's node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. amā (PHD.txt l. 189)\", \"stance\": \"supports\", \"note\": \"'amā [LNE < A l-nh | M ʾmʾh, N mā] we, us.' — MacKenzie reads amā, giving the Manichaean spelling ʾmʾh and the New Persian outcome mā.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary s.v. amāh (NYB_vol2_glossary.txt l. 374)\", \"stance\": \"supports\", \"note\": \"'amāh [LNH, Prth LN] pers. pron. 1st p. pl. 1. cas. rect. we ... 2. cas. obl. us ... — Av. (295 sq.) gen. ahmākəm, OP amāxam; MPrthPrs ʾmʾh; Paz. ema; NP ma.'\"},\n            {\"src\": \"BQT\", \"where\": \"printed p. 1931 s.v. ما\", \"stance\": \"supports\", \"note\": \"quoted above; Mo'in cites Nyberg p. 7 for the Turfan form.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"mâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian ما mā is MP amāh with loss of the unstressed initial a- (the same aphesis as سیم sīm < asēm in the first chart on this very page, and as شاگرد < ašāgird, ویران < avīrān) together with the loss of final -h; the resulting monosyllable serves as both subject and oblique pronoun from the earliest Dari poetry (Rudaki, Ferdowsi). Mo'in's footnote at Borhan-e Qate' p. 1931 lays out precisely Nourai's arrow and then some: 'ما – پهلوی amâh (ما)، پارسی باستان amâxam، اوستا ahmâkəm، اوراق تورفان amâh، پازند êmâ، هندی باستان asmáka-, استی max, کردی me/ma/mé, شهمیرزادی و گیلکی ama, دزفولی omûn, خوانساری hâmâ'. Nyberg and MacKenzie both end their entries with 'NP mā'. Wiktionary agrees on the route (MP 𐭫𐭭𐭤 amāh < OP amāxam) but attaches the whole thing ultimately to 'the variant *mey of Proto-Indo-European *wéy' rather than to the oblique *nes-/*n̥s- stem; Pokorny, Walde-Pokorny, Bartholomae, Klein, Watkins and Nyberg all derive amāxam / ahmākəm from *n̥s-me-, which is what the chart does, so Nourai is with the mainstream here and Wiktionary's *mey is the outlier.\",\n          \"derivation_fa\": \"«ما»ی فارسی نو همان amāh فارسی میانه است با افتادن «الف» بی‌تکیهٔ آغازین — همان دگرگونی که در «سیم» (< asēm) در نمودار نخست همین صفحه و در «شاگرد» (< ašāgird) و «ویران» (< avīrān) دیده می‌شود — به‌همراه افتادن «ه» پایانی؛ حاصل، تک‌هجایی «ما» است که از کهن‌ترین شعر دری (رودکی، فردوسی) هم در جای فاعل و هم در جای مفعول و مضاف‌الیه به کار رفته است. حاشیهٔ معین بر برهان قاطع در صفحهٔ ۱۹۳۱ عیناً همین زنجیره را می‌دهد و گونه‌های گویشی (کردی me/ma/mé، شهمیرزادی و گیلکی ama، دزفولی omûn، خوانساری hâmâ) را نیز می‌افزاید. نیبرگ و مکنزی هر دو مدخل خود را با «فارسی نو mā» به پایان می‌برند. ویکی‌واژه در مسیر هم‌داستان است ولی سرانجام آن را به گونهٔ *mey از *wéy هندواروپایی می‌بندد، نه به ستاک غیرفاعلی *n̥s-؛ پوکورنی، والده-پوکورنی، بارتولومه، کلاین، واتکینز و نیبرگ همه amāxam/ahmākəm را از *n̥s-me- می‌گیرند، پس نورایی با دیدگاه اصلی همراه است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%A7\",\n            \"https://abadis.ir/fatofa/%D9%85%D8%A7/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1931\", \"status\": \"supports\", \"note\": \"the entry ما stands at the head of the mīm section on printed p. 1931 (گفتار بیست و چهارم, بیان اول) with Mo'in's footnote 'پهلوی amâh (ما)، پارسی باستان amâxam، اوستا ahmâkəm ...' — see ocr/BQT/1931.png and 1931.vision.txt. Dehkhoda s.v. ما quotes the same footnote ('از حاشیه ...').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. amā (PHD.txt l. 189)\", \"stance\": \"supports\", \"note\": \"'amā ... N mā' — the New Persian outcome given in the entry itself.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. amāh (NYB_vol2_glossary.txt l. 374)\", \"stance\": \"supports\", \"note\": \"'... Paz. ema; NP ma.'\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. ما (via abadis.ir)\", \"stance\": \"partial\", \"note\": \"'(ضم.) ضمیر اول شخص جمع' — the online Mo'in lexicon text gives the grammatical definition only, with no etymology; the etymology is in his Borhan footnote.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. ما (Persian)\", \"stance\": \"partial\", \"note\": \"'From Middle Persian 𐭫𐭭𐭤 (LNE /amāh/, we, us), from Old Persian 𐎠𐎶𐎠𐎧𐎶 (amāxam) (genitive plural form of the first person plural pronoun), ultimately from the variant *mey of Proto-Indo-European *wéy' — same route, different ultimate root than Nourai's *nes-.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old Persian\",\n          \"words\": \"amâxam\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Persian amāxam is the genitive plural of the first person plural pronoun, attested in the Behistun inscription (DB 1.14 xšaçam tya hacā amāxam taumāyā parābartam āha 'the kingship which had been taken away from our family'; also DB 1.3, 1.8, 1.28 etc.). It answers Avestan ahmākəm and Sanskrit asmākam form for form, i.e. it goes back to *n̥s-me-ka-am: the Old Persian development of the cluster gives am- where Avestan has ahm-, and OP -x- corresponds to Av. -k-. Kent lists it at p. 167 under adam: 'amāxam gpm. (Av. ahmākəm, Skt. asmākam; §118.II, §193.VI) DB 1.8, 28, 45, 49, 61, 69, 71; DBa 12'; Bartholomae files it under ahma- (AiW 297). The arrow root > Old Persian is therefore right. One gloss caveat, as in node 1: amāxam means 'of us, our', not 'we' (the Old Persian nominative is vayam, also on Kent p. 167).\",\n          \"derivation_fa\": \"amāxam پارسی باستان اضافهٔ جمع ضمیر اول شخص جمع است و در سنگ‌نوشتهٔ بیستون گواه دارد (بیستون ۱/۱۴: xšaçam tya hacā amāxam taumāyā parābartam āha «شهریاری که از تبار ما گرفته شده بود»). این صورت واژه‌به‌واژه برابر ahmākəm اوستایی و asmākam سنسکریت است، یعنی از *n̥s-me-ka-am می‌آید؛ خوشهٔ آغازی در پارسی باستان am- شده در برابر ahm- اوستایی، و -x- پارسی باستان برابر -k- اوستایی است. کنت آن را در صفحهٔ ۱۶۷ زیر adam آورده: «amāxam اضافهٔ جمع مذکر (اوستایی ahmākəm، سنسکریت asmākam) بیستون ۱/۸، ۲۸، ۴۵ ...» و بارتولومه در ستون ۲۹۷ زیر ahma-. پس پیکان ریشه به پارسی باستان درست است. تنها نکته، مانند گرهِ اوستایی: amāxam معنای «مالِ ما» دارد نه «ما» (صورت فاعلی پارسی باستان vayam است).\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:209\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, printed p. 209 (SOD_pages.txt: page marker '209' at l. 18666; entry at ll. 18689-18696) entry 5252: 'mʾx M, C — māx (ymʾx, ymʾx) © < *ahmākam; OP amāxam © first, pl. pres. pron. ... we'. The cited page does carry the Old Persian form amāxam that Nourai attaches to it, although a Sogdian dictionary is an odd authority for an Old Persian headword — Kent p. 167 and Bartholomae AiW 297 are the primary sources.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"p. 167 s.v. adam / amāxam (KNT.txt leaf 189)\", \"stance\": \"supports\", \"note\": \"'amāxam gpm. (Av. ahmākəm, Skt. asmākam; §118.II, §193.VI) DB 1.8, 28, 45, 49, 61, 69, 71; DBa 12' — and on the same page 'vayam npm. (Av. vaēm, Skt. vayám ...)', showing that amāxam is the genitive, not the nominative.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW cols. 296-297 s.v. ahma- (BRT.txt l. 6922)\", \"stance\": \"supports\", \"note\": \"'3) sonst; a) D im Ap. stets: xšaçam tyaʰ hacā amāxam taumāyā parābartam āha Bh. 1.14' — Bartholomae puts OP amāxam under the Avestan ahma- stem.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 758\", \"stance\": \"supports\", \"note\": \"'av. ahma (ai. asmān, ap. Gen. amāxam)' — Pokorny explicitly labels amāxam the Old Persian genitive.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. amāh\", \"stance\": \"supports\", \"note\": \"'Av. gen. ahmākəm, OP amāxam'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sogdian\",\n          \"words\": \"m`x, m`ğw\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Sogdian mʾx / mʾγu 'we' is the Sogdian outcome of the same Old Iranian *ahmākam: aphesis of the initial a-, simplification of *hm to m, and loss of the ending give mʾx, beside the extended form mʾγu of the Buddhist and Christian texts. Gharib's dictionary confirms both of Nourai's forms and both of his page numbers exactly: entry 5185 on printed p. 206, 'mʾγw B, S — māxu (ymʾx, mʾxw) © < OP amāxam → mʾx(h)¹ ... we', and entry 5252 on printed p. 209, 'mʾx M, C — māx © < *ahmākam; OP amāxam ... first pl. pres. pron. we' (further readings at Gershevitch GMS §§399, 1375). The verdict is 'plausible' only because of the shape of the arrow: the chart makes Sogdian a daughter of Old Persian, whereas Sogdian is not descended from Old Persian at all — it is an independent North-Eastern Middle Iranian language, and the two forms are cousins going back to a common Old Iranian *ahmākam. Gharib's own '< OP amāxam' is comparative shorthand (she also writes '< *ahmākam' in the parallel entry), and Nourai appears to have read it as a statement of descent.\",\n          \"derivation_fa\": \"صورت سغدی mʾx / mʾγu «ما» بازماندهٔ همان *ahmākam ایرانی باستان است: افتادن «الف» آغازین، ساده‌شدن خوشهٔ *hm به m و افتادن پایانهٔ صرفی، mʾx را می‌دهد و در متون بودایی و مسیحی گونهٔ گسترش‌یافتهٔ mʾγu نیز دیده می‌شود. فرهنگ سغدی بدرالزمان قریب هر دو صورت و هر دو صفحهٔ نورایی را دقیقاً تأیید می‌کند: مدخل ۵۱۸۵ در صفحهٔ ۲۰۶ («mʾγw ... < پارسی باستان amāxam ... ما») و مدخل ۵۲۵۲ در صفحهٔ ۲۰۹ («mʾx ... < *ahmākam؛ پارسی باستان amāxam ... ضمیر اول شخص جمع»). ارزیابی «با احتیاط پذیرفتنی» تنها به سبب جهت پیکان است: نمودار سغدی را فرزند پارسی باستان نشان می‌دهد، در حالی که سغدی از پارسی باستان برنیامده، بلکه زبانی مستقل از شاخهٔ ایرانی میانهٔ شمال‌شرقی است و این دو صورت هم‌ریشه‌اند نه پدر و فرزند. نشانهٔ «>» در فرهنگ قریب کوتاه‌نویسی سنجشی است و نورایی آن را نشانهٔ تبار خوانده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:206\", \"status\": \"supports\", \"note\": \"SOD_pages.txt: page marker '206' at l. 18452; entry 5185 at ll. 18466-18472: 'mʾγw B, S — māxu (ymʾx, mʾxw) © < OP amāxam → mʾx(h)¹ ... we. GMS 3175; VJ; TSP; BSTBL STi 86.10; Frag. Len.; MDii'. Nourai's mʾγw is on exactly p. 206.\"},\n            {\"ref\": \"SOD:209\", \"status\": \"supports\", \"note\": \"page marker '209' at l. 18666; entry 5252 at ll. 18689-18696: 'mʾx M, C — māx (ymʾx, ymʾx) © < *ahmākam; OP amāxam © first, pl. pres. pron. → mʾγw, mʾx(h)¹, mʾxnc — we. GMS 399, 1375; mʾxw, KG; C2'. Nourai's mʾx is on exactly p. 209. Both page citations check out.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib, entries 5185 (p. 206) and 5252 (p. 209)\", \"stance\": \"supports\", \"note\": \"quoted above; note Gharib uses both '< OP amāxam' and '< *ahmākam' for the same word, i.e. her '<' is comparative, not genealogical.\"},\n            {\"src\": \"KNT\", \"where\": \"p. 167 s.v. amāxam\", \"stance\": \"partial\", \"note\": \"supplies the Old Persian form but says nothing about Sogdian; Old Persian is a South-Western dialect and cannot be the parent of a North-Eastern language.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 758\", \"stance\": \"partial\", \"note\": \"Pokorny lists av. ahma / ap. amāxam under *n̥sme but has no Sogdian material at all.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Germanic\",\n          \"words\": \"uns; unsara\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *uns is the regular reflex of the PIE zero grade *n̥s-: syllabic *n̥ became Germanic un-, giving Gothic uns, Old High German / German uns, Old Saxon ūs and Old English ūs (with loss of the nasal and compensatory lengthening before -s, the same change as in OE gōs 'goose' < *gans-). The possessive Gothic unsara / OE ūser, ūre reflects *n̥s-ero-, i.e. the same stem with the possessive suffix that also produced Latin noster and Old Prussian nouson. Watkins states it in Nourai's own terms: 'nes-2 ... 1. Zero-grade form *n̥s- in Germanic *uns in Old English ūs, us (accusative): US. 2. Suffixed (possessive) zero-grade form *n̥s-ero- in Germanic *unsara- in Old English ūser, ūre, our: OUR, OURS. [Pok. 3. ne- 758.]' Pokorny 758 has 'got. ahd. uns, as. ūs, anord. oss uns (*n̥s)'.\",\n          \"derivation_fa\": \"*uns ژرمنی آغازین بازتاب قاعده‌مند درجهٔ صفر *n̥s- هندواروپایی است: *n̥ هجایی در ژرمنی un- شد و از آن گوتی uns، آلمانی علیای کهن و آلمانی uns، ساکسون کهن ūs و انگلیسی کهن ūs (با افتادن خیشومی و کشیدگی جبرانی پیش از s، همان دگرگونی که در gōs «غاز» < *gans- دیده می‌شود). صفت ملکی گوتی unsara و انگلیسی کهن ūser/ūre از *n̥s-ero- است، یعنی همان ستاک با پسوند ملکی‌ای که noster لاتین و nouson پروسی کهن را نیز ساخته است. واتکینز عیناً همین را می‌گوید و به پوکورنی ۷۵۸ ارجاع می‌دهد، و پوکورنی می‌نویسد: «گوتی و آلمانی علیای کهن uns، ساکسون کهن ūs، نورس کهن oss از *n̥s». ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 p. 784 s.v. nes-2: '1. Zero-grade form *n̥s- in Germanic *uns in Old English ūs, us (accusative): US. 2. Suffixed (possessive) zero-grade form *n̥s-ero- in Germanic *unsara- in Old English ūser, ūre, our: OUR, OURS. [Pok. 3. ne- 758.]' — Nourai's two Germanic words verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 784 s.v. nes-2\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n            {\"src\": \"KLN\", \"where\": \"vol. II s.v. us (KLN_1966.txt l. 40905)\", \"stance\": \"supports\", \"note\": \"'fr. OE. ūs, rel. to OS., OFris. ūs, ON., Swed. oss, Dan. os, MDu., Du. ons, OHG., MHG., G. uns, Goth. uns, fr. I.-E. base *n̥s-'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. our (SKT.txt l. 20492)\", \"stance\": \"supports\", \"note\": \"'our. (E.) A.S. ūre, of ūs; gen. pl. ... This gen. pl. became adj. and was regularly declined ... ūre stands for ūs-ere. + Goth. unsara, of Goth. uns, we.'\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 758\", \"stance\": \"supports\", \"note\": \"'got. ahd. uns, as. ūs, anord. oss uns (*n̥s), aksl. nasъ Gen. (*nōs-sōm), apr. nōuson (ebenso)'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"us, our, ours\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English ūs (accusative-dative of wē) > Middle English ous, us > modern us; Old English ūre (originally the genitive plural of wē, literally 'of us', standing for *ūs-ere) > Middle English oure > our, on which the double genitive ours was built in the 14th century as part of the general Middle English creation of mine/thine/hers/ours/theirs. Klein s.v. us: 'ME. ous, us, fr. OE. ūs ... Goth. uns, fr. I.-E. base *n̥s-, for *nes, *nōs, we ... Cp. our, nostrum.' Skeat s.v. our: 'A.S. ūre, of ūs; gen. pl. ... + Goth. unsara, of Goth. uns, we. Der. our-s, our-self, ourselves.' The node carries no reference in the book, but the chain is uncontroversial.\",\n          \"derivation_fa\": \"انگلیسی کهن ūs (حالت مفعولی wē) به ous/us در انگلیسی میانه و سپس us امروزی رسید؛ ūre انگلیسی کهن که در اصل اضافهٔ جمع wē و برخاسته از *ūs-ere بود، در انگلیسی میانه oure و سپس our شد و بر پایهٔ آن در سدهٔ چهاردهم صورت اضافهٔ دوگانهٔ ours ساخته شد، همراه با mine/thine/hers/theirs. کلاین در مدخل us و اسکیت در مدخل our همین زنجیره را می‌دهند و our را به ūs و unsara گوتی می‌بندند. این گره در کتاب بی‌ارجاع است، ولی زنجیره کاملاً بی‌اختلاف است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None); the claim is covered by KLN s.v. us, SKT s.v. our and AHD s.v. nes-2.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. II s.v. us (KLN_1966.txt l. 40905)\", \"stance\": \"supports\", \"note\": \"'us, objective case of we. — ME. ous, us, fr. OE. ūs ... Cp. our, nostrum.'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. our (SKT.txt l. 20492)\", \"stance\": \"supports\", \"note\": \"'our. (E.) A.S. ūre, of ūs ... + Goth. unsara, of Goth. uns, we. Der. our-s, our-self, ourselves.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 784 s.v. nes-2 and index (ll. 784, 2005-2006)\", \"stance\": \"supports\", \"note\": \"index entries 'OUR nes-2' and 'OURS nes-2'; 'NOSTRUM nes-2'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-352.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-07T18:36:36.064Z] TOOL RESULT

```
JSON OK
```


## [2026-09-07T18:36:39.949Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 tools/verify_check.py 352"
}
```


### [2026-09-07T18:36:41.278Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'plausible': 2, 'confirmed': 14}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'not_found': 2, 'partial': 1, 'not_checked': 4}
books consulted: {'partial': 6, 'supports': 46, 'contradicts': 1, 'silent': 1} | by book: {'KLN': 9, 'SKT': 6, 'NYB': 5, 'POK': 5, 'PHD': 4, 'MON': 3, 'Wiktionary': 3, 'WLD': 2, 'HUB': 2, 'HRN': 2, 'Etymonline': 2, 'LAT': 2, 'BRT': 2, 'KNT': 2, 'AHD': 2, 'Wiktionary/Beekes': 1, 'BQT': 1, 'SOD': 1}
```


## [2026-09-07T18:37:03.976Z] AGENT

Done. `verify_check.py 352` reports 16/16 nodes, 0 PROBLEM lines.

**Page 352 (book p. 322) — 2 entries, 16 nodes**
- Root verdicts: confirmed 2. Node verdicts: confirmed 14, plausible 2.
- Ref checks: supports 14, partial 1, not_found 2, not_checked 4. Books consulted: 57 entries (supports 46, partial 6, contradicts 1, silent 1).

Flagged items (no `disputed`, no `transcription_suspect`, no extraction errors):
- **Ne 1 / An 4, node #1 (Greek), ἄσφαλτος — plausible.** Nourai's `a-sphallein → asphaltos` is the traditional LSJ analysis, but Beekes calls it "weak" and treats ἄσφαλτος as Pre-Greek, and Klein (after Lewy 1895) calls it "of uncertain, possibly Semitic origin". The prefix ἀ-/ἀν- itself and ἄσημος, ἄτομος, ἄσβεστος are all confirmed, so the node is downgraded rather than disputed.
- **Ne 2 / Nes 2, node #5 (Sogdian) — plausible.** Forms and both page cites (SOD:206 = entry 5185 mʾγw, SOD:209 = entry 5252 mʾx) check out exactly, but the chart hangs Sogdian *under Old Persian*; Sogdian is NE Middle Iranian and only a cousin — both go back to Old Iranian *ahmākam. Gharib's "< OP amāxam" is comparative shorthand that Nourai read as descent.

Reference-citation problems (book, not extraction):
- **KNT:209** (nodes #2, #3, Pahlavi asēm / NP sīm) — `not_found`. Kent's OP lexicon has no asēm/sīm at all (its silver word is `ardata-`, p. 170); the local scan also breaks off at pp. 206–207. Looks like a misplaced citation; the claim is fully supported instead by PHD, NYB ("Borrowed from Gr. ἄσημον"), HRN p. 169 and HUB.
- **VOP** (node #6, Persian atom/آسفالت) — `not_checked`, no copy exists anywhere (already recorded in refs_online.json).

Notable confirmations: POK:756/758 and KNT:167 verified on the page; BQT:1931 rendered and read by vision (saved as `sources/refs/ocr/BQT/1931.png` + `1931.vision.txt`) — Mo'in's footnote gives Nourai's whole ما chain (پهلوی amâh، پارسی باستان amâxam، اوستا ahmâkəm); SNS:232 index has "amah/amag 232/3", vindicating Nourai's otherwise unattested Pahlavi form *amâg*; KLN:1683 s.v. *us* has both `Avestic na` and `Avestic ahma (for I.-E. *n̥sme)`. Minor gloss looseness noted (not verdict-changing): Av. *ahmāka-* and OP *amāxam* mean "our/of us", not "we".

11 web sources archived via `fetch_source.py`.
