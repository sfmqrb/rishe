# Verification process log — verify-page-234


## [2026-09-06T15:34:10.218Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 234 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-234.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-234.json. Write /home/sfmqrb/git/rishe/data/verification/page-234.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 234` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:34:11.808Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:34:12.516Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:34:12.530Z] TOOL RESULT

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


## [2026-09-06T15:34:12.851Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-234.txt"
}
```


### [2026-09-06T15:34:12.875Z] TOOL RESULT

```
1	=== PDF page 234 (book page 204) ===
2	--- entry 0 ---
3	ROOT [Turkish] Kagaš, Kagat, Kagas, Kagaz : tree bark  (refs SIN:559)
4	#1 (parent #0) [Pahlavi] refs=SIN:559; PLA:225 | kâgad : paper | NOTE: Chinese paper was imported in Iran (Samarghand) as early as 650 AD but the word "kâğaz" was not borrowed from the Chinese word "Ku-Čih".
5	  #2 (parent #1) [Persian] refs=BQT:1569 | kâğaz «کاغذ» : paper
6	--- entry 1 ---
7	ROOT Kagat -> redirect to Kagaš
8	--- entry 2 ---
9	ROOT Kagaz -> redirect to Kagaš
10	--- entry 3 ---
11	ROOT [Avestan] Kahrpu, Kharpuna : lizard  (refs BQT:1612; SOD:193)
12	#1 (parent #0) [Pahlavi] refs=BQT:1612; SOD:193 | karpu, krpwk : lizard
13	  #2 (parent #1) [Persian] refs=MON:2933 | karbâsŭ «کرباسو» : lizard | extra: کرپاسو ، کربسو ، کرش ، کرپاشه ، چلپاسه
14	#3 (parent #0) [Sogdian] refs=SOD:193 | krps`k : lizard
15	--- entry 4 ---
16	ROOT [Indo-European] Kak 1 : to have power, help, enable  (refs POK:522)
17	#1 (parent #0) [Avestan] refs=POK:522; HRN:152; FFD:58 | sak, sač, sâx : to do, make ; sačaiti : able, qualified, deserving
18	  #2 (parent #1) [Persian] refs=HRN:152,160,162; BQT:1137; POK:522 | sâxtan «ساختن (سازیدن، سازش، سازگار)» : to build ; sezîdan «سزیدن (سزا، سزاوار)» : to qualify
19	#3 (parent #0) [Avestan] refs=POK:522 | čagad : helped ; čageman : gift ; čagvah : offered
20	#4 (parent #0) [Sanskrit] refs=POK:522; | saknôti : he is able to do ; siksati : he helps, serves ; čakta : strong, hard
21	  #5 (parent #4) [Pahlavi] refs=BQT:1106 | saxt : hard
22	    #6 (parent #5) [Persian] refs=SNS:173 | saxt «سخت» : hard, difficult
23	  #7 (parent #4) [English] refs=AHD:1205 | Sikh : a follower of Sikhism (a Hindu religious community)
24	#8 (parent #0) [Old English] refs=POK:522 | haeccan : to hatch
25	  #9 (parent #8) [English] refs=AHD:603 | hatch
26	
```


## [2026-09-06T15:34:15.915Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-234.json",
 "description": "Read source JSON for page 234"
}
```


### [2026-09-06T15:34:15.953Z] TOOL RESULT

```
{
  "pdf_page": 234,
  "book_page": 204,
  "entries": [
    {
      "root": {
        "name": "Kagaš, Kagat, Kagas, Kagaz",
        "lang": "Turkish",
        "refs": "SIN:559",
        "gloss": "tree bark"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "SIN:559; PLA:225",
          "words": [
            {"translit": "kâgad", "gloss": "paper", "script": null}
          ],
          "note": "Chinese paper was imported in Iran (Samarghand) as early as 650 AD but the word \"kâğaz\" was not borrowed from the Chinese word \"Ku-Čih\".",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1569",
          "words": [
            {"translit": "kâğaz", "gloss": "paper", "script": "کاغذ"}
          ],
          "note": null,
          "quote": {"text": "کاغذ بدریدند و قلم بشکستند - وزدست زبان حرف گبران رستند", "poet": "Sa`dî"}
        }
      ]
    },
    {
      "root": {"name": "Kagat", "redirect": "Kagaš"},
      "nodes": []
    },
    {
      "root": {"name": "Kagaz", "redirect": "Kagaš"},
      "nodes": []
    },
    {
      "root": {
        "name": "Kahrpu, Kharpuna",
        "lang": "Avestan",
        "refs": "BQT:1612; SOD:193",
        "gloss": "lizard"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:1612; SOD:193",
          "words": [
            {"translit": "karpu, krpwk", "gloss": "lizard", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:2933",
          "words": [
            {"translit": "karbâsŭ", "gloss": "lizard", "script": "کرباسو"}
          ],
          "script_extra": "کرپاسو ، کربسو ، کرش ، کرپاشه ، چلپاسه",
          "note": null,
          "quote": {"text": "میکشد هم نهنگ را راسو - مرگ عقرب بود ز کرباسو", "poet": "Âzarî Tûsî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:193",
          "words": [
            {"translit": "krps`k", "gloss": "lizard", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kak 1",
        "lang": "Indo-European",
        "refs": "POK:522",
        "gloss": "to have power, help, enable"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:522; HRN:152; FFD:58",
          "words": [
            {"translit": "sak, sač, sâx", "gloss": "to do, make", "script": null},
            {"translit": "sačaiti", "gloss": "able, qualified, deserving", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:152,160,162; BQT:1137; POK:522",
          "words": [
            {"translit": "sâxtan", "gloss": "to build", "script": "ساختن (سازیدن، سازش، سازگار)"},
            {"translit": "sezîdan", "gloss": "to qualify", "script": "سزیدن (سزا، سزاوار)"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:522",
          "words": [
            {"translit": "čagad", "gloss": "helped", "script": null},
            {"translit": "čageman", "gloss": "gift", "script": null},
            {"translit": "čagvah", "gloss": "offered", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:522;",
          "words": [
            {"translit": "saknôti", "gloss": "he is able to do", "script": null},
            {"translit": "siksati", "gloss": "he helps, serves", "script": null},
            {"translit": "čakta", "gloss": "strong, hard", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "BQT:1106",
          "words": [
            {"translit": "saxt", "gloss": "hard", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "SNS:173",
          "words": [
            {"translit": "saxt", "gloss": "hard, difficult", "script": "سخت"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:1205",
          "words": [
            {"translit": "Sikh", "gloss": "a follower of Sikhism (a Hindu religious community)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Old English",
          "refs": "POK:522",
          "words": [
            {"translit": "haeccan", "gloss": "to hatch", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD:603",
          "words": [
            {"translit": "hatch", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T15:34:16.457Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:34:16.486Z] TOOL RESULT

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


## [2026-09-06T15:34:22.618Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['SIN','PLA','BQT','SOD','MON','POK','HRN','FFD','SNS','AHD','TTS','LKT','PHD','BRT','KLN']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:900])\n    print()\n\""
}
```


## [2026-09-06T15:34:22.637Z] TOOL CALL #6: Bash

```json
{
 "command": "head -60 data/verification/page-202.json"
}
```


### [2026-09-06T15:34:24.801Z] TOOL RESULT

```
SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sections are numbered with plant/product names in caps; grep the Persian/Chinese word or the page number.", "notes": ""}

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py P

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"], "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 =

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea

TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books.", "notes": "Open full text (public domain). OCR rough (Fraktur +

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"}

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
```


### [2026-09-06T15:34:24.854Z] TOOL RESULT

```
{
 "pdf_page": 202,
 "book_page": 172,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Gwa, Gwâ, Gwen 2",
   "verdict": "confirmed",
   "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
   "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
   "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
   ],
   "ref_check": [
    {
     "ref": "POK:463",
     "status": "supports",
     "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-')",
     "stance": "supports",
     "note": "'gʷem-, gʷā-' … 'ai. gātram „Glied, Körper“; ai. gātu- „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu … ai. vi-gāman- n. „Schritt“ … av. gāman- n. „Schritt“'. This is the source Pokorny 463 abridges (Buck cites it as 'Walde-P. 1.675 ff.')."
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, g-list (AHD_watkins1985.txt line ~539)",
     "stance": "supports",
     "note": "'gʷā-. Also gʷem-. To go, come. 1. Germanic *kuman in a. Old English cuman, to come: COME … 3. Suffixed zero-grade form *gʷm̥-yo- in Greek bainein, to go, walk, step, with basis (< *gʷm̥-ti-), a stepping, tread, base'. Same double root, same gloss."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *gam¹ (CHEUNG.txt lines 7307, 7478) and *gaH¹ (line 7054)",
     "stance": "supports",
     "note": "'*gam¹ \"to come\" … «PIE *gʷem- “to go; come” = LIV: 209 f. | Pok.: 464 f.»'; and '«PIE *gʷeH₂- “to go, stride” = LIV: 205 | Pok.: 463 f.»'. Cheung's *gam¹ article lists, as its New-Persian outcome, exactly Nourai's harvest: 'NP zamān “time” … NP gām “step, pace” … NP āmadan … NP pay(g)ām “message”, NP pay(g)ambar … NP anjuman “company, assembly, club”'."
    },
    {
     "src": "SYN",
     "where": "Buck §10.47/10.48 (SYN.txt line 17514 f.)",
     "stance": "supports",
     "note": "'2. IE *gʷem-, *gʷā-. Walde-P. 1.675 ff. … Skt., Av., OPers. gam- \"go, come\" (Skt. gacchati, Av. jasaiti, sk̑o- presents like Grk. baskō; Av. jam- without prefix mostly \"come\"; also Av., OPers. ā-jam- \"come\", whence NPers. amadan \"come\")'."
    },
    {
     "src": "KLN",
     "where": "p.318 s.v. 'come' (KLN_1966.txt line 8320, page marker 318 at the foot)",
     "stance": "supports",
     "note": "'come … fr. I.-E. base *gʷem-, “to go; to come”, whence also OI. gámati, gacchati … Avestic jamaiti “goes” … Cp. the collateral base *gʷā- in OI. agām (aor.), Gk. ébēn (aor.), “I went”'."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan / Old Persian",
     "words": "gam : to come, step; jam, jantu : to go",
```


## [2026-09-06T15:35:02.004Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SIN grep kagad/kaghaz ===\"; grep -n -i -E 'k[aā][gḡğ]a[dḏz]|kaghaz|paper of' SIN.txt | head -40\necho \"=== SIN leaf for printed 559: leaf = printed-172 = 387 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==387||NR==388' SIN.txt | head -80"
}
```


## [2026-09-06T15:35:02.913Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK page 522 : POK_02 leaf = p-344 = 178 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==178' POK_02.txt\necho \"=== also 177/179 heads ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==177||NR==179' POK_02.txt | head -20"
}
```


### [2026-09-06T15:35:04.526Z] TOOL RESULT

```
=== SIN grep kagad/kaghaz ===
=== SIN leaf for printed 559: leaf = printed-172 = 387 ===
e
language  of  C'u  l§,  in  which  it  had  the  significance  "milk"  (%u  #L);
and,  as  the  bark  of  this  tree  contained  a  milk-like  sap,  this  word  was
*~  transferred  to  the  tree.    It  is  noteworthy  in  this  connection  that  Ts'ai  ;
\  Lun,  the  inventor  of  paper  in  a.d.  105,  was  a  native  of  C'u.     The  |
^dialectic  origin  of  the  word  kou  shows  well  how  we  have  two  root-words
for  exactly  the  same  species  of  tree.    This  is  advisedly  stated  by  Li
Si-cen,  who  rejects  as  an  error  the  opinion  that  the  two  words  should
refer  to  two  different  trees;  he  also  repudiates  expressly  the  view  that
the  word  kou  bears  any  relation  to  the  word  ku  in  the  sense  of  cereals  or
rice.    According  to  T'ao  Huh-kih,  the  term  kou  U  was  used  by  the
people  of  the  south,  who,  however,  said  also  £'w  U;  the  latter  word,
1  Journal  Roy.  As.  Soc,  1903,  p.  671.
2  According  to  Buhler  (Indische  Palaographie,  p.  91),  paper  was  introduced into  India  by  the  Mohammedans  after  the  twelfth  century.  The  alleged  Sanskrit word  for  "paper,"  kayagata,  ferreted  out  by  Hoernle  {Journal  Roy.  As.  Soc,  191 1, p.  476),  rests  on  a  misunderstanding  of  a  Sanskrit  text,  as  has  been  shown  by  Lieut.- Col.  Waddell  on  the  basis  of  the  Tibetan  translation  of  this  text  {{ibid.,  1914, pp.  136-137).
3  Ch.  36,  p.  4.
4  See  above,  p.  201.
Irano-Sinica— Paper  559
Persian-Arabic  word.    There  *  no  rea  ^  ^^  ^
paper  was  adopted  by  the  Arabs
  ana  r  know
designation  of  it  should  had  from  the  same  ^*rf o£  a  foreign  language  that  was  wdhng   ^ffj^  Greek.Latin any  designation  for  paper,    uur  w°  <.cotton  "  being  ultimately
W«;  R^ian  *-rS  °ngin^yt ?  The  Tibetans  learned  the  tech- Lceable  to  Middle  P^'a"  ^^fbXve  a  word  of  their  own niqueof  paper-makmg  from  th ^Chme  e  but  hav  ^  ^
srr&sr  firsts  -  «« ^ 5-  rs
§g£SSS3S3g|§
XaPT,s).      As  statea,  me  Kumandu,
Turkish  language: "'flcS     TarancC  and  Kazan  tego..    The
origin  ot  rn  significance  "tree-bark,
^fld  not  rep't  htre  the  oft-told  story  of  how  the  manufacture  of l  neeo.  nou     p  Qamarkand  by  Chinese  captives  in  a.d.  751.
Itls  well  known  that  the  Chinese  were  the  ongmators  of  \
money
invention  of  l^^.^tJl  expect  to  come  back  to  this  problem  on and  indeed  was  the  work  of  Ts  ^  Lun     I  ^  q{  Karabacek,  Wiesner,  and
another  occasion.    With  ^  rf  Pect  ^ ™  r^chine  conclusions  of  these  scholars  are Hoernle,  I  am  not  convinced  ^^2°^  less  theorizing),  especially all  justified.   We  are  in  need  c \™™™f^ ^mus  acC0unts  of  many  sorts  of of  ancient  papers  made  in  China  Jhere  ^^  should  be  cloSely  studied, naoer  hitherto  unnoticed,  in  Chinese  recorub,  w  111
^According  to  Masudi  (B.  pe  M~  L« P-nes  d  or   £LH,  J-Jj see  also   E.  Drouin,  Memoire  sur  les  Huns  Ephthahtes,  p.  53  V    v
Museon,  1895).
560  Sino-Iranica
paper  bank-notes.1!  The  Mongol  rulers  introduced  them  into  Persia, first  in  1294.  The  notes  were  direct  copies  of  Kubilai's,  even  the  Chinese characters  being  imitated  as  part  of  the  device  upon  them,  and  the Chinese  word  llao  i£  being  employed.  This  word  was  then  adopted by  the  Persians  as  lau  or  lav?  The  most  interesting  point  about  this affair  is  that  in  that  year  (1294)  the  Chinese  process  of  block-printing was  for  the  first  time  practised  in  Tabriz  in  connection  with  the  printing of  these  bank-notes.
In  his  graphic  account  describing  the  utilization  of  paper  money by  the  Great  Khan,  Marco  Polo3  makes  the  following  statement: "He  makes  them  take  of  the  bark  of  a  certain  tree,  in  fact  of  the  mul- berry tree,  the  leaves  of  which  are  the  food  of  the  silkworms, —  these trees  being  so  numerous  that  whole  districts  are  full  of  them.  What they  take  is  a  certain  fine  white  bast  or  skin  which  lies  between  the  wood of  the  tree  and  the  thick  outer  bark,  and  this  they  make  into  something resembling  sheets  of  paper,  but  black.  When  these  sheets  have  been prepared  they  are  cut  up  into  pieces  of  different  sizes."  In  the  third edition  of  Yule's  memorable  work,  the  editor,  Henri  Cordier,4  has added  the  following  annotation:  "Dr.  Bretschneider  (History  of Botanical  Discoveries,  Vol.  I,  p.  4)  makes  the  remark:  'Polo  states that  the  Great  Khan  causeth  the  bark  of  great  mulberry  trees,  made into  something  like  paper,  to  pass  for  money.'  He  seems  to  be  mistaken. Paper  in  China  is  not  made  from  mulberry-trees,  but  from  th
```


### [2026-09-06T15:35:06.304Z] TOOL RESULT

```
=== POK page 522 : POK_02 leaf = p-344 = 178 ===
lich  eigen',  daher  , allein'  und  ,ganz, vollständig' ;
lat.  caelehs,  -ibis  , unvermählt,  ehelos',  wohl  aus  *kaiuelo-lib(h)-s  , allein lebend',  zu  got.  liban  , leben'  usw.;    y gl.  lett.  Jcails  ,bloß,  kinderlos'.
WP.  I  326,  WH.  I  130,  455 ;  vgl.  auch  kai-ko-^  kai-lo-.
2.  kai  ,und'?
Die  Gleichung  gr.  xct  ,und,  auch' :  aksl.  cä  in  a  ce,  c^  i  ,'/.ai'VOL,  y.aln6Q, siftaq''  (vgl.  die  noch  unklaren  Formen  ark.  kypr.  xag,  kypr.  xa)  ist sehr  unsicher;  denn  cS  ist  wohl  als  ,*wie  =  wie  auch,  wie  wohl' zunächst  mit  lit.  kai,  lett.  kd,  kai,  apr.  kai  ,wie,  als'  vom  Pron.  St.  k'^o-, zu  verbinden,  während  xat  kaum  aus  kV:.-  (infolge  proklitischer  Stellung?) entwickelt  sein  kann;  nicht  zu  lat.  ceu  ,wie'  (^kai  ue  kaum  mit  e  aus  ai wie  prehendö  nach  Wackernagel  und  Niedermann  lA.  18,  76).
WP.  I  327,  Schwyzer  Gr.  Gr.  II  567  ^  Trautmann  112,  Endzelin  Lett. Gr.  §  474,  WH.  I  209.
ß.  käi-,  k^-  ,Hitze'.
Ahd.  hei  ,dürr',  gihei  n.  , Hitze,  Dürre',  arheigetun  ,verdorrten',  got.  Dat. PI.  haizam  ,den  Fackeln'  (es-St.  *hai-iz-).
Mit  -d-Erw. :  ahd.  heiz,  as.  het,  ags.  hat,  aisl.  heitr  ,heiß'  (wovon  ahd. nhd.  heizen,  ags.  hcetan,  aisl.  heita  ds.);  got.  heito  f.  , Fieber';  ahd.  hizza jHitze^,  i^hitjo)  as.  hittia,  ags.  hitt  t,  aisl.  hiti  m.  ds.
Mit -t-Erw. :  lit.  kaistü,  kaitau,  kaisti  ,heiß  werden',  kaiträ  , Feuerglut', kaitrüs  , Hitze  gebend',  präkaitas  m.  , Schweiß',  lett.  käistu,  käitu,  käist ,heiß  werden,  brennen'  u.  dgl.,  übertragen  lett.  kaiiinät  , ärgern,  reizen' (kalte  , Schaden,  Leid,  Gebrechen,  Plage',  vgl.  Mühlenbach-Endzelin  II  135), apr.  ankaitltai  , Angefochtene' ;
aisl.  häss  (*hairsa-  aus  *hais-ra-),  ags.  häs  ("^haisa-),  engl,  hoarse  (aus mengl.  hös  +  coarse),  as.  hes,  ahd.  heisi  ,heiser^  (unklar  ist,  ob  hierher aus  *kirsem  dXh.  kirrem  , werde  heiser*?).
WP.  I  326  f.,  Trautmann  113.
4.  käi-d-f  käi-t-  ,hell,  leuchtend'  s.  unter  {s)käi-d-,  {s)käi-t-.
kai-ko-  , einäugig;  mit  nur  einem  geraden  Auge,  schielend^  (im  Lat.  daraus ,blindO. Ai.  kekara-  , schielend';
lat.  caecus  ,blind,  lichtlos',  air.  caech  , einäugig,  schielend,  blind',  cymr. coeg  ,vacuus,  deficiens',  coegddall , einäugig',  acom.  cuic  ,luscus  vel  monoph- thalmus',  got.  haihs  , einäugig';  mir.  leth-chaech  , schielend'  (*halb-einäugig);
520  t
vielleicht  hierher    gr.  xamag  ,Nordostwind'  als  ,*der  dunkle'  (Güntert Kalypso  67«,  vgl.  aquilo  :  aquilus  oben  S.  23;   dagegen  Fick  GGA.  1894- 238:  vom  Kai'/.og,  einem  Fluß  der  Äolis,  herkommend);
lit.  keikti  ,fluchenS  eigentl.  ,bösen  Blick  werfen'
=== also 177/179 heads ===
hgefäß,  Fischreuse' (alles  aus  Flechtwerk),  cölö,  -äre  ,durchseihen,  läutern^ ;  ablaut.  lat.  cohum, nach  Paul.  Diac.  ,lorum,  quo  temo  buris  cum  iugo  colligatur,  a  cohibendo dictum'  als  ,Halter,  Umfassung',  dazu  incohö,  -äre  , fange  an',  eigentl.  ,an- legen,  anschirren'  (Wort  der  Bauernsprache);
hierher  osk.  icahag  ,incipias',  kahad  ,capiat':  umbr.  3.  PI.  Konj.  Perf. kukehe(n)s  ,occupaverint^  =  lat.  capere:  cepi  (s.  unten  S.  527  f.);  umbr.  cehefi ,captus  Sit'  ist  Konj.  Pass.  des  /-Perfekts  (E.  Fraenkel,  Fil.  Biedr.  Räksti 1940,  8 f.);
gall.  (5.  Jh.,  Zimmer  KZ.  32,  237  f.)  caii  ,cancelli'  Gl.,  caio  ,breialo sive  bigardio'  Nom.  Gall.  (daraus  frz.  quai,  afrz.  chai  .Flnßdamm') ;  abret. caiou  PL  ,munimenta',  cymr.  cae  ,Gehege'  und  ,Halsband',  corn.  ke  , Ge- hege', mbret.  kae  , Dornenhecke,  Zaun' ;  abgeleitet  cymr.  caii  , einhegen', bret.  kea  , einen  Hag  machen';  vielleicht  cymr.  caen  f.  ,Bedeckung,  Haut' (*kagh-na)  Vendryes  WuS.  12,  242 ;  daraus  entlehnt  mir.  cain  ,Oberfläche') ; cymr.  cael  ,das  Erlangen'  (*kagh-la),  s.  oben  S.  408;  ablaut.  in  bret.  mor-go (*mon'go,  zu  *wow-  ,Hals')  ,Halsring  der  Pferde',  falls  -go  aus  *kogho- (nach  V.  Henry,  Lexique,  jedoch  zu  cymr.  caw  ,Band'),  und  cymr.  myn-ci ds.,  falls  aus  *-cei,  idg.  *koghio-]  daraus  mir.  muince  , Halsband';   •
ahd.  hag  ,Hecke,  Gehege',  ags.  haga  m.  ,Hecke,  Garten',  engl,  haw, asächs.  hago,  aisl.  hagi  , Weideplatz' ;  ags.  hceg  n.  , Gehege,  Grundstück', engl.  Äay,  ags.  hecg  f.  ,Hecke',  engl,  hedge,  ahd.  lieckia,  heggia  , Hecke',  zu aisl.  hegg-r  ,Ahlkirsche'  (*hagjö',  daraus  frz.  haie  ds.) ;  Ableitungen:  ags. hagu-rUn  , Zauber',  hegi-tisse,  ahd.  haga-zussa  ,Hexe' ;  aisl.  hegna  , einhegen, schützen',   zu  ahd.  hagan   , Dornstrauch',   PN  Hagano,  anord.  Hqgni,  usw.
WP.  I  337  f.,  WH.  I  187  f.,  243  f.,  631,  Loth  RC  45,  198  f.
kaghlo-  , kleiner  runder  Stein,  Kiesel';  germ.  , Hagel'.
Gr.  xax^ijä,  -rjv.og  , Stein,  Kiesel',  Abi.  von  *Y,axlog  = ahd.  hagal,  ags.  hagol,  hcegel  m.  anord.  hagl  n.  ,Hagel'. WP.  I  338.
519
jcai-,  kai-uo-,  kai-uelo-  ,alleiii'.
Ai.  kivala-h  ,jemandem  ausschließ
  (*keikmi :  *kaikm^\ Wegen  der  Grundbed.  ^einäugig'  vgl.  *kai-  ,allein'.  j\
WP.  I  328,  WH.  I  129.  f
kaik-  oder  koik-  ,kratzen,  kämmen'.
Ai.  kesa-  m.  ^Haupthaar',  kesin-  ,mähnig'  (wie  aksl.  kosa  ,Haar'  :  ^esati ,kämmen'  von  *kes-  ,kratzen,  kämmen');
lit.  kauti  ^schaben,  reiben,  glätten',  iskaUti  ,Glas,  Holz  u.  dgl.  in^iea glatt  machen',  kalUuvas  , Glättinstrument  der  Böttcher',  apr.  coysnis  ,Kamin' coestue  ,Kamm,  Bürste';
abg.   cästa  ,Weg,  Straße'  als  ,geglätteter  Weg'.
WF.  I  328,  Trautmann  113.
kai-lo-  (kai-lu-)  ,heil,  unversehrt,  auch  von  guter  Vorbedeutung'.
Cymr.  coel  f.  , Vorzeichen',  acymr.  PI.  coilou  ,auspiciis',  abret.  coel ,(h)aruspicem',  leg.  ,(h) aruspicium',  acymr.  coiliaucc,  acorn.  chuillioc  ,augur' (air.  cel  ,augurium'  brit.  Lw.);
got.  hails,  aisl.  heul,  ahd.  heil  .gesund,  ganz',  ags.  häl,  engl,  whole ,ganz',  ahd.  heil  n.  ,das  Heil,  Glück',  ags.  hwl  ,günstiges  Vorzeichen,  Glück, Gesundheit',  aisl.  heil  (*heilz,  5-St.)  n.  f.  ,gute  Vorbedeutung,  Glück',  ahd. heilisön  ,Wahrzeichen  beobachten',  ags.  hälsian  ,(böse  Geister)  beschwören', aisl.  heilsa  ,begrüßen'  (vgl.  auch  got.  hails!,  ags.  wes  häl!  als  Gruß),  ags. hälettan,  ahd.  heilazzen  ,begrüßen',  ahd.  (usw.)  heilag  ,heilig' ;  ags.  hälan PL  , Nachgeburt'  =  norw.  heile  ds. ;
```


## [2026-09-06T15:35:15.927Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SIN grep kagat/kagas etc ===\"; grep -n -i -E 'kaga|kaghaz|kagd|kagit|kâgad|kagaz' SIN.txt | head -30\necho; echo \"=== POK grep k̂ak / vermögen helfen ===\"\ngrep -n -E \"vermögen,? ,?helfen|k.ak-.*helfen|saknóti|saknoti|s.aknoti\" POK_02.txt | head -20\ngrep -n \"522\" POK_02.txt | head -20"
}
```


### [2026-09-06T15:35:15.990Z] TOOL RESULT

```
=== SIN grep kagat/kagas etc ===
951:abbreviated  name  of  which  is  kurumi;  local  names  are  ogurumi  (Prov- ince of  Kaga),  okkoromi  (eastern  provinces),  and  so  on.  This  giant  wal- nut grows  to  a  large  tree.  Its  leaves  are  much  like  those  of  the  lacquer- tree  (Rhus  vernificera  DC.)  and  a  little  larger;  they  have  finely  serrated margins.  Its  new  leaves  come  out  in  the  spring.  It  flowers  in  the autumn.
953:"One  species  called  hime-gurumi  ('demoiselle  walnut,'  Juglans cordijormis  Maxim.,  ex  Matsumura,  I.e.),  or  me-gurumi  ('female  wal- nut,' from  the  province  of  Kaga),  has  thin  shells  with  fewer  furrows,  and the  kernels  can  easily  be  taken  out.  Under  the  heading  lukai  (£i-kie, explanatory  information  in  the  Pen  ts'ao),  this  kind  of  walnut  is  de- scribed as  'a  walnut  produced  in  Cinso  (C'en-ts'an,  a  place  in  Fuh- siah  fu,  Sen-si,  China)  with  thin  shells  and  many  surfaces,'  so  we  call it  linso-gurumi  (Pen-ts'an  hu-Vao).1  This  variety  is  considered  the best  of  all  yama-gurumi  (Ian  hu  Vao,  wild  walnuts),  because  no  other variety  has  such  saddle-shaped  kernels  entirely  removable  from  the shells.
3722:23.  Persian  lubi  cini  ("China  root"),  Neo-Sanskrit  cobaclnl  or copaclnl  (kub-cini  in  the  bazars  of  India),  is  the  root  of  Smilax  pseudo- china,  so-called  Chinese  sarsaparilla  {fu-fu-lih  zh  $t  4*) ,  a  famous remedy  for  the  treatment  of  Morbus  americanus,  first  introduced  into Europe  by  the  returning  sailors  of  Columbus,  and  into  India  by  the sailors  of  Vasco  da  Gama  (Sanskrit  phirangaroga,  "disease  of  the Franks").  It  is  first  mentioned,  together  with  the  Chinese  remedy,  in Indian  writings  of  the  sixteenth  century,  notably  the  Bhavaprakaga.5 Good  information  on  this  subject  is  given  by  Garcia  da  Orta,  who says,  "As  all  these  lands  and  China  and  Japan  have  this  morbo  napo- litano,  it  pleased  a  merciful  God  to  provide  this  root  as  a  remedy  with which  good  doctors  can  cure  it,  although  the  majority  fall  into  error. As  it  is  cured  with  this  medicine,  the  root  was  traced  to  the  Chinese, when  there  was  a  cure  with  it  in  the  year  1 53 5. "6  Garcia  gives  a  detailed description  of  the  shrub  which  he  says  is  called  lampatam  by  the  Chi- nese.7 This  transcription  corresponds  to  Chinese  len-fan-fwan  <v  f£  @8 (literally,  "cold  rice  ball"),  a  synonyme  of  Vu-fu-lin;  pronounced  at
4145:The  title  has  been  traced  by  E.  Chavannes  and  Sylvain  Levi  in the  Itinerary  of  Wu  K'un  (751-790).  The  Chinese  author  relates  that the  kingdom  of  Ki-pin  (Gandhara  and  territory  adjoining  in  the  west) sent  in  750,  as  envoy  to  the  court  of  China,  the  great  director  Sa-po  ta-kan II  tt  h  fr*  (or  T),  anciently  *Sat  or  Sar-pa  dar-kan  (cf.  Journal asiatique,  1895,  II,  p.  345).  Chavannes  and  Levi  have  recognized  a Turkish  dynasty  in  the  then  reigning  house  of  Ki-pin,  and  have  regarded the  title  ta-kan  also  as  Turkish,  without,  however,  identifying  it  {ibid., p.  379).  In  1903  Chavannes  noted  the  identity  of  the  Chinese  tran- scription with  Turkish  tarkan  (Documents  sur  les  Tou-kiue  occidentaux, p.  239).  The  Chinese  transcription  *dar-kan  does  not  allow  us  to  pre- suppose a  Turkish  model  darkan;  but  the  Old-Turkish  form  was  indeed tarkan,  as  is  also  confirmed  by  New  Persian  tarxan  and  Armenian t'arxan  (Hubschmann,  Armen.  Gram.,  p.  266).  Tarsa,  the  Persian designation  of  the  Christians,  is  transcribed  in  Chinese  by  the  same character,  ^  ^  ta-so,  anciently  *dar-sa.  The  complex  phonetic  phe- nomenon which  is  here  involved  will  be  discussed  by  me  in  another place.  Wherever  the  Chinese  mention  the  title,  it  regularly  refers  to Turkish  personages:  thus  the  pilgrim  Huan  Tsan  is  accompanied  by  an officer  Mo-tu  tarkan,  assigned  to  him  by  the  Turkish  Kagan  (Watters, On  Yuan  Chwang's  Travels,  Vol.  I,  pp.  75,  77);  for  examples  in  the Chinese  Annals,  see  Hirth,  I.e.
5821:kagas,  kagat  559
5843:kaden  553 kagat,  kagaz  559 kandir  294 karpuz  444 kismis"  231,  241,  299 koz  256

=== POK grep k̂ak / vermögen helfen ===
2719:522  •
```


## [2026-09-06T15:35:18.083Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT kahrpuna ===\"; grep -n -i -E 'kahrpu|karpuna|kǝhrp|kahrp' BRT.txt | head -30\necho \"=== SOD krps ===\"; grep -n -i -E \"krps|karpus|kyrps\" SOD_pages.txt | head -20\necho \"=== SOD entry 193 area ===\"; grep -n -E \"^ *193 |^193 \" SOD_pages.txt | head"
}
```


### [2026-09-06T15:35:18.186Z] TOOL RESULT

```
=== BRT kahrpuna ===
6536:Vfil.  aiakva-.  —  Pü. :  fehlt. •  j.  azay-  m.  i)  'Schlange',  ein  ^ÄiÄisches Tier:  /<fiws.tara  ya^a  'zayS  xsvoewanhs V.iS.ßs;  —  'Sinam  udarS.>rasanam  .  . °iinam  spakanqm  kahrpunanam  (sd.)  V. 14.%.  a)  Sing,  in  koll.  Sinn:  äat  ahe paityänm  .  .  'zimca  yim  raoioibtn  (sd.) zj'rtM/a..V./.2''; — yai3  '%wä  niHt  aiwi,- Jruzilnti  •iisea  arütuiisca  "damit  dir kein  Arg  antun  können  Schlangen  und  .." YL5, 90.  2)  schlangenähnlichcs  Untier 'Drache,  Ungeheuer'":  'zdis  sairitaAe simahe  vlsS.valpahe  Y.().3o;  —  'zis .  . gäuitava . .  vTraja  Aog.  ~S;  —  'leis  vJlspahe N.  48;  —  ktrasäsps  .  .  yS  jartat  °ilm (sd.)  yim  aspB.garpm  mnganm  ..
7817:•  g.  a^nman-  n.  'Stetigkeit;  Unaufhörlich- keit': al  kahrplm  utayäitJs  äadät  armaiti^ 'mä  (AP.)'*  "und  Arm.  verlieh  den  Leibern Dauer  und  Stetigkeit"  Y.jo.;.  a)  LS. °m7nT  als  Adv.  'stets,  ewiglich;  unaufhör- lich"'; yi  'mSnl  mazdn  srävi  ahurd  "der ewiglich  MAk.  heisst"  Y.  45. 10;  —  yaii' gqm  karaps  usixscä  (sd.)  alhmUi  däii yücä    kavä   *'mJnI^^    urüdSyatä  (sd.)    Y.
9158:—  ks  UKtmSm  (sd.)  cBrM"^  . ,  pu'^nm pure  Y.  44. 7 ;  —  kjrmaomi  "iwam  hacat.- pu^rqm  V.2^.6;  — yat  k^rmaot..  *amar- /an/a  fasu  vira  V.p.  4;  Yt5.  30,  /j.  16 [k^rmavani);  —  matdqmcä  (s,  i  c)  büiricä kjrpsvä  .  .  xrapaitl  (sd.)  Ayat  ahmat  aibi Y.  4n.  I ;  —  yi  umm  pinmm  k?rpnaoiti  . . bantjm.'a  drum  k^rmaoUi  V.  22.5;  uj.^%, Y.  10,13;  —  \hatm  parsam  hami'i''iyam akunaus  Bh.  4.2;  2%  3;  —  ya'ia  asym amasyq  (sd.)  kmnaväni  .  .  karh'qn  Yt. 5.30;  —  ts  k>rmava  mdwaire  ajyamnem V.2.z8;  36  {kirnittol);  — yat  amm  patti.- irist»m  /rä.nastirii  kjnnaaiti  V.  r/,  42;  — armadsth  atiyh  äps  k^nnaoi  Yt.5,78;— >J( Im  firasJmisA.)  *k3rjnaon'^^  ahsm  Y.30.9; Yt.iil.ii  (k^rMavqn),  89  {k»rma7,;li) ;  — yezi  iidit . .  mazdayasna  . .  kahrpsm  kvars.- dar^slm  (sd.)  k:>rmavqn  V.5,14;  13  (wo k^r»nai)t,  statt  Plur,);  —  raeko  (sd.)  mS haca  aühij  s»mat  vatihö  k^rjnaoiii  Yt. iy.2o;  10.2S;  —  ya  *a/r3.ur7'isval  (sd.) hrmavainti  irmi  Yt  13.  z6;  —  I  av<^taiy (^urJ'mazdä  ^mazänam  (sd.)  kunautiro Bh.  4.'6;   —  ava'^  adam  patipadam{%iL)
9326:•  j.  kahrpuna-  m.  Name  eines  a'aft'ischen  j  schleppten  sie  die  Weiber  den  Menschen Tiers'*:  baivan  alinam  spakanqm  •■nanqmX-^^^'  Yt. /g.  80".
9535:kahrp-  Noten
9545:•  j.,  g.  kahrp-,  ksr?/-^'^  f.,  n.'>  'das  sieht- ' bare  Äussere  jedes  Wesens  und  Dings, , äussere  Erscheinung,  sichtbare  Gestalt': sraliiqm  at  tSt  'p/m  (AS.)  -^pam  (GP.)  j ävaedayamakl  tnazdä  ahurä  iinä  raota  . . avat  y.ll  hvarS  aväcT  Y._J(*'.  6;  — para avtiiriAe  hü  "^warstö  (sd.)  'pya  (LS.)  Y. ' /p.  8;  —  asmamm  ,  ,  y3  hislaite  ayanhs 'pa  (IS.)  x^amahe  (sd.)  ".  .  mit  der  Er- scheinung von.,  (sva. ..  anzusehen  wie..)'' YL  13.  2.  A)  insbes.  von  lebenden Wesen;  auch  vom  gestalteten  Stoff  selbst 'Leib,  Körper';  i )  von  Menschen  und Göttern:  aj  'psm  (GP.)  utayuitil  dadat ärmaitis  qnmä  (sd.)  Y.jo.  7;  — ■  yd>!a varsnahe  'palie^^  dsus  (sd.)  N.  7o(7;  — paiti  ainii  .  .  'p^m  .  .  gaia/ie  .  .  °ppm  .  . säJiar/  .  .  "Pim  .  .  abmatr/aAe  .  .  'P^m ..jahikayüi  ..  -p.m  Y.//.  30-32;  32;  — avqm  'P^m  yazamaide .  -yqtn . .  k^r^säspahe Yt /?.  61;  Az._J;  —  üjasat . .  viriisra-fitä ..vätahe  'pa  (IS.)  Vt/4-2;  —  mi%nm..
11964:•  j.  tanu.kahrp-  Adj.  'die  Gestalt  der eigenen  Person  habend' (?) '*,  von  Söhnen: puHrS  zayanle  °pa  kiArpa  Vyt  V;  3.
17809:•  j.,  g.''  fravaäay-  f.  ^Fravasay*'>,  Be- zeichnung für  das  dem  Gläubigen  eigene Unsterbliche,  das  Element,  das  schon  vor setner  Geburt  vorhanden  war  und  ihn  über- dauert. So  lang  der  Gläubige  lebt,  wacht seine  Fr.  als  Schutzgeist  Über  ihn.  Die Gesammtheit  der  Fr.  der  Gläubigen  aber spielt  eine  ähnliche  Rolle  wie  die  indischen pitärah,  die  römischen  ««««■:  'sayö  hütti^ Aatqm..aigAu^qm..bUsyantqin{Sf.^^i  m.) a!'aanqmYt.i3.2\;—ä  hätqmca  anhusqfnca zätanqmca  azätanqinca  asaonqm  ilajasmiu °sayd  Y.  öj.  6;  —  aat  anyaisqm  'say!> jvanqm  narqm  aiaonqm  aojyehfi .  ,  ya^a iristanqm  "aber  im  übrigen  sind  die  Fr. der  lebenden  Gläubigen  stärker  als  die der  gestorbenen"  Yl;_j.  17;  —  vispäbyö asaonibyS  *nbyS  y3  irlrüu/qm  .  .  yasia jvantqm  .  .  yäsca  narqm  azätanqm  Y. 24-5;  —  vispanqmca  änhqm  alaonqm asaoninqmla  ila  yaxamatde  °stm  Yt,  ij. 148';  —  neben  'aAs-,  *da?nä-  usw.; alaonqm  aiaoninqmla  ahümla  dafaqtnca baoiasca  urvarumca  °slmca  Y.  26'.  4;  — gai^ssca  asdsbJlca  us'tänqsca  kahrpasca Uvlilsca  baohasia  urvämmca  'sTmca  Y. 55,  I ;  —  xardkuitrahe  . .  'Am  . .  sravä  . . dainqm  . .  varvtifmca  tkais»nca  Y.  16. 2 ; —  manä  . .  dalnä  . .  urunS . .  'say!)  (als  AP.)
21224:Au.irixt^m(sd.)..trinaxtiYt.io.6B.  a)init' vorhergehendem  vTspum  S  aAm3J  'donec, bis':  näa  difyäi  aäa  ^rityäi  vJsp^m  ä ahmst  y'  hl  han/asaitt  yaia  iahrutiim *yär?  N.42;  43,  Vd..#.  3)  mit  dem Konj.  (oder  Inj.)  in  fiiCuiischem  Sinn:  yai (s.  V)  .  .frasna  (sd.)  paiti.mravSm  y  mgm ftrpsai  axtys  Yt  j.  8z;  —  y  irista  paiti us»hiltqn  ..  äa%aite  fras>m  vasna  anhui Yt  Jp.  1 1 ;  —  y  astvatjTTls  fraxHäite  .  . avaaa  drujpm  nilbarat  Yt  jg.  92  f.;  —  y yavs  dqyät  aal  daeva  :^um  (sd.)  y^  ■  ■ äayap  äaO  ..  V.,;.  32;  —  asti  zT  ana avavai  uxäata  (sd.)  ya'äsa  y  dim  vJsp5 ar»huf  äsaxiat  (sd.)  . .  pairi  irtkyqstätat (sd.)  haraite  Y.ig.  10.  /)  im  Sinn  des lat  Fut  II:  aSaha  hr  tanüm  . .  »idaihyqn vTsppm  3  ahmat  .  .  yat  (s.  c.)  frä  vayS patqn  ,  .  äat  y°  ('wenn')  ht^  frä  vayS patqn  fra  urvara  ux^qn  nysttiä  apa.- tacin  .  .  ariala  .  .  kahrptm  kvanJansJm kmnaot  V.  5.  i  a  £ ;  —  *fra  *ma  . .  *gara- yffi/ (sdj)  y  raful  fritsil  *a/asäi  N.  ip;  — y  dim  iatäj..paia  *avaMääiV.S.too(t); io3(?); — yai  nSiriAa  voAunls  atwi.vamäl y  (nachdem')  Al  'kray3  xlafiia  sacatüe V.  16. 8;  — y  ('nachdem')  kl  tanul  hilkvi Mymii  pqsnu  bavat  pascaSa  .  .  jasBtt  V. p.  31.  a)  mit  vorhei^ehendem  pasca 'postquam':  aem  ai^he  asti  utvanam  yal (s.  V)  nä  pasla  y  usthtÜäi^^  .  .  änV aÄOT  ■  upajtuyät  V.  18.  43;  s.  V.  18.  49 (unter    4).  b)    mit    vorhergehendem
26811:•  j.  spaka-  Adj.  'hundeartig,  Hunds*'; aHaam  •kanam  kahrpunanam  (sd.)  V. 14.  S-
=== SOD krps ===
17512:     snakes                                                             4854 krps'k B        (<JLJ^)aJ^ i^^X^^ja^ i^JUf
=== SOD entry 193 area ===
4360:193 »p»t V*       B
```


## [2026-09-06T15:35:29.353Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 around line 2719 (page 522) ===\"\nsed -n '2700,2760p' POK_02.txt"
}
```


### [2026-09-06T15:35:29.395Z] TOOL RESULT

```
=== POK_02 around line 2719 (page 522) ===
WP.  I  329  f.,  WH.  I  133.
521
käi-t'  ,h.e\V  s.  unten  unter  skäi-t-.
kaito-  ,Wald,  unbebauter  Landstrich'  (kelt.  und  germ.).
Acymr.  coit,  ncymr.  coed  ,Wald',  acorn.  cuit,  mcorn.  coys,  cos  ds.,  bret. coet,  coat  ,Wald,  Gehölz',  gall.  ON  Kairö-ßgi^,  Ceto-briga,  Eto-cetum  u.  dgl. (die  spätere  rom.  Aussprache  -zetum  liegt  den  nhd.  Ortsnamen  auf  -scheid '     am  linken  Rheinufer  zugrunde);
got.  haipi  L,  aisl.  heidr,  ags.  hced,  engl,  heath,  ahd.  heida  f.  ,Heide- kraut',  mhd.  heide  f.  ,Heide' ]  daneben  ags.  *häd,  engl.  dial.  hoath]  urgerm. *Äaij{>ana5, steppenbewohnend,  wild',  wohl  Lehnübersetzung  von  iat.pä^änws ( :  pägtis  ,Land'),  dazu  got.  haipnö  f.  , Heidin',  aisl.  heidinn,  ags.  häeden, engl,  heathen,  asächs.  hethin,  ahd.  heidan,  heidin,  heidanisk  ^heidnisch' -^ anders  W.  Schulze  Kl.  Schriften  521  ff.
über  lat.  hücetum  ,Kuh-Trift'  s.  WH.  I  120,  Vendryes  RC  48,  398.
WP.  I  328  f..  Feist  237  f.
kaiur-t,  kaiun-t  , Grube,  Kluft'. Ai.  kivata-  m.  , Grube';
gr.  Tialara'  ÖQvy^ara  Hes.,  hom.  -/.aLaxösoGa  {AaY£Öaiy.(jov]  so  für  über- liefertes -KTjrcbsaaa  herzustellen)  , klüftereich',  y.aiddag  Erdschlund  in  Sparta (d  wie  in  dsy,dS-  :  lit.  deHmt-). WP.  I  327,  Specht  Idg.  Dekl.  25.
kakka-  ,cacäre';  Lallwort  der  Kindersprache.
Arm.  Hakor  ^Mist',  gr.  xaxx«w  ,cacö',  xaxxTj  , Menschenkot',  lat.  cacö, -äre,  mir.  caccaim  ,caco',  cacc  ,Kot',  cymr.  cach,  bret.  cach,  com.  caugh ds.,  russ.  usw.  käkatt  ,cacare',  nhd.  kacken-^
dazu  yielleicht  als  Kinderwort  —  vgl.  nhd.  gegga  ,pfui'  —  auch  gr. 7iay,6g  , schlecht';  neuphryg.  %a:^ow  ,Böses',  nach  Friedrich  (Eberts  Real- lexikon I  139)  gr.  Lw. ;  kaum  hierher  Kayiao ßog,  kleinas.  Reitergott  (in Lykien),  vgl.  oben  S.  309.
WP.'l  336.
käk-  Nachahmung  des  Krächzens.
Ai.  käka-  m.  , Krähe',  käkäla-,  käkola-  m.  ,Rabe';  lett.  käk'is  , Dohle' (auch  apr.  koce  ds.,  wenn  so  für  kote  zu  bessern) ;  zum  lett.  FIN  Kak'upe, lit.  FIN  Kakupis  (vgl.  Ka^vrtaQLg,  FIN  in  Sizilien?)?  Anders  über  die halt.  Worte  Mühlenbach-Endzelin  II  190.
WP.  I  335.
kak-  , abmagern'.
Av.  kasii-  ,klein,  gering',  Komp.  Superl.  kasyah-,  kasista-] nhd.  hager  (Trautmann  ZfdtWtf.  7,  267,  KZ.  43,  153);
522  •
lit.  nukaseti  ,ganz  entkräftet  werden'. WP.  I  334.
kak-  (kek-?)  , vermögen,  helfen'.
Ai.  saknöti  ,kann,  ist  imstande,  hilft',  Desid.  nksati  ,hilft,  huldigt, dient,  lernt',  sakti-  f.  ,Hilfe',  sakra-  ,vermögend',  sagma-  ,vermögend,  hilf- reich', sdcl  f.  ,Vermögeu,  Hilfe',  sdka-  m.  ,Kraft,  Hilfe',  ääkd-  ,kräftig, helfend;  m.  Helfer',  säkman-  n.  ,Hilfe';  y^\.  sdkvan-  ,geschickt';
av.  sacaiti  , versteht  sich  worauf,  Desid.  sixsaiti  , lernt',  npers.  saxt ,hart,  fest,  sehr'  =  Ki.Jakta-  ,vermögend' ;
air.  cedit  , Macht'  {*kankt-  oder  *kenkt-)]
Vielleicht  lit.  kankü,  käkti  , wohin  gelangen,  genügen,  hinreichen' (Reihenwechsel?);  unsicher  auch  ags.  hagan  ,genitalia',  mhd.  Äa^ew  , Zucht- stier', nhd.  dial.  hegel  ds.,  haksch  , Zuchtschwein',  nhd.  hecken  ,sich  paaren (von  Vögeln)',  engl,  hatch  ,hrüten',  ahd.  hegi-diniosa  ,Hode'.  Ebenso,  weil  nie -Ä-,  sondern  nur  -g-  im  Wurzelauslaut,  die  germ.  Sippe  aisl.  hagr  ,passend, geschickt',  liagr  m.  ,Lage,  Vorteil,  Wohlstand',  haga  , anordnen',  högr, hegr  ,passend,  bequem',  hättr  (*hahtu-)  ,Art  und  Weise'  (wäre  «w-St. neben  dem  ^i-St.  ai.  sakti-),  ahd.  st.  Partiz.  ki-hagan,  bihagan  ,heiter', mhd.  behagen  ,passen,  recht  sein',  nhd.  behagen,  mhd.  hage  m.  , Behagen, Wohlgefallen',  as.  bihagön  , behagen,  gefallen',  ags.  onhagian  ,passen,  be- hagen', gehagian  unpers.  , Gelegenheit  sein' ;  unter  Annahme  von  ausl.  -gh- vergleicht  Zupitza  Gutt.  104  sie  mit  prakr.  ca{y)ati  ,ist  fähig',  A9oka- Inschr.  caghati  ,ist  zu  etwas  bereit,  willig',  av.  cagdd-  (mit  rafdördm) , Hilfe  gewährend',  cagdman-  n.  , Geschenk',  cagvah-  ,bietend,  gewährend', die  freilich  w^iederum  in  ihrem  e-Vokalisraus  nicht  so  unmittelbar  zum germ,  a  :  ö  stimmen ;
toch.  A  käkmart,  B  kamart  ,Herrschaft'.
WP.  I  333,  334.
I.  käk-  :  kdk-,  wahrscheinlich  kä[i]k-  :  kik-  (mit  kdk-  als  Ablautneubildung von  kak-  aus)  , springen,  hervorsprudeln,  kräftig  sich  tummeln'.
Gr.  xrjKLüj  , entspringe,  sprudle  hervor',  xäx/w'  ISqovv  ItQxo^ai.  ^aY,(avsq Hes.,  x'^xfg,  -Idog^  dor.  xflix/g  f.  ,alles  Hervorsprudelnde  (Blut;  Purpursaft; ausbratendes  Fett;  Dampf)';  lesb.  xa/xvAi;  ds.  Hes.;
lit.  sökti  , springen,  tanzen';  nasaliert  sanküs  ,flink',  sankinti  ,(ein  Pferd) springen  machen'  (vgl.  Y.ayv.vh])  und  ahd.  hengist,  ags.  hengest  ,Hengst', eig.  Superl.  ,am  besten  springend,  bespringend',  germ.  *hangista  neben *hanhista  (gramm.  Wechsel)  in  anord.  hestr  ,Pferd',  zum  Positiv  *hanha-, dazu  Dat.  urnord.  hahai  ,dem  Renner'  und  ahd.  Häh-,  Hang-,  aisl,  Ha- in PN;   dazu  kelt.  *kankstikä  , Stute'  in   cymr.  caseg  ds.,   bret.   PL  kezeg
I
523
Pferde',  dial.  , Stuten',  acorn.  cassec  , Stute',  gall.  ON  Cassiciate  (Lok.) , Pferdepark'.
Für  käik-'.klk'  führt  man  das  wohl  thrak.-phryg.  aULv(v)Lg  ,Tanz  der Satyrn  zu  Ehren  des  Dionysos'  (zwar  i  bei  den  Lex.,  aber  Eur.  Cycl.  37 auch  mit  l  meßbar)  an,  wohl  auch  xtxvg  f.  , Kraft',  genauer  , Beweglichkeit, Frische',  ztxvw  *  Ta;fT;vw,  layvo)  Zonar.,  ep.  ion.  IjcxiKvgy  -vog  , schwach, schlapp';
Pedersen  KG.  I  51  stellt  hierher  (y(,Ty,vg  :)  ir.  eich  f.  ^weibliche  Brust', cymr.  cig,  bret.  kik,  acorn.  chic  , Fleisch'.
WP.  I  334,  Hof  mann  Etym.  Gr.  Wb.  142,  Kluge  ^^  s.  v.  Hengst
2.  kak-,  nasaliert  kank-  ,Ast,  Zweig,  Pflock';  kakhä  f.  ,gebogener  Zweig, Pflug'.
Ai.  säkhä  f.  ,Ast'  (:  got.  höha,  arm.  cax)]  sdkala-  m,  n.  ,Span,  Splitter, Holzscheit,  Schnitzel,  Stückchen'  (:  lit.  sakalys)]  sai^kü-  m.  ,Holznage], Pflock,  Pfahl,  Stecken'  (:  aksl.  s^k^,  cymr.  cainc,  anord.  Äär);  sakti-  f. ,Speer'  (:  air.  cecht)]
arm.  cax  , Zweig',  vielleicht  Lw.  aus  pers.  mx  ds.,  und  dies  aus  ai. säkhä]  nach  Meillet  Esquisse^  36,  Slave  commun^  23 f.  vielmehr  aus  idg. *ksäkh- ;
wegen  der  Bed.  unsicher  alb.  theke  ,Franse,  Zipfel',  vgl.  immerhin  die- selbe Bed.  von  norw.  hekel  , Zipfel'  unter  *keg-]
cymr.  cainc  (*kankü,  vgl.  den  w-St.  ai.  saTsku-),  PI.  cangau^  mcymr. canghau  ,Ast',  mir.  gec,  nir.  geag  ,Ast'  (mit  sekundärer  Media  im  Anlaut), mit  -s/c-Suffix  gallo-rom.  *gascaria  (frz.  jachere)  ,Brachland',  eigentl. ;Pflugland',  Hubschmied  Vox  Rom.  III  123^;  air.  gescae  , Zweig,  Ast';  mit ^Suffix  air.  cecht  , Pflug'  (wohl  als  *kank-to-  nächstverwandt  mit  ai.  sakti-);
got.  höha  , Pflug'  (=  ai.  sükhä)^  ahd.  huohili  ,aratiuncula' ;  nas.  anord. har    ,Ruderdolle'   (*hanha,   Ann.   Lw.),    hcell   , Pflock,    Stock'    (*hanhila-)]
lit.  §akä  ,Ast'  (ablaut.  mit  ai.  säkha),  säke  , Gabel',  sakalys  , Splitter' (:  ai.  sdkala-),  sakms,  apr.  sagnis  f.,  lett.  sakne  ,Wurzel';  lit.  sakarnis lästig',  lett.  sakarnis  , Wurzelende';  aksl.    sokz  ,surculus';
slav.  socha  ,Knüppel  (aksl.  usw.),  Haken,  Pflug  (russ.),  Gabelstange' (poln.),  poln.  rozsocha  ,gabelförmiger  Ast',  aksl.  posochz  m.  , Knüttel'.
WP.  I  335,  Trautmann  297  ff„  Specht  Idg.  Dekl.  55,  254;  vgl.  unter ke{n)g-,  ke{n)k-  ,Pflock,  Haken'  S.  537  f.  und  kenk-,  konk-  , schwanken, hangen',  S.  565.
I.  kal-  ,hart',  kal-no-,  kl-no-  , Schwiele,  harte  Haut'.
Ai.  kina-  m.  , Schwiele'  (mind.  aus  "^kfiia-s) ;  über  ai.  kathina-,  kathora- s.  unter  3.  kar- :
524  t
lat.  callum  n.,  callus  m.  ^verhärtete  dicke  Haut,  Schwiele'  (dazu  calleQ -ere  , dickhäutig  sein;  gewitzigt  sein',  callidus  , schlau') ;
alb.  a-kul  ,Eis';
air.  mir.  calatk,  calad  ,hart',  cymr.  caled  ds.,  gall.  VN  Caleti,  Caletes- dazu  gallo-rom.  *calio-,  *caliauo-  , Stein'  (M.-L.  1519  a),  sowie  gall.-lat. calUo-marcus  , Huflattich*  (für  *calUo  marci  ,testiculus  equi'),  epo-calium (leg.  -callium),  ebul-calium  (für  *epälo-callium,  zu  mcymr.  ebawl,  bret.  ehol , Füllen')  ds.,  zu  cymr.  caill,  bret.  kell  f.  ,Hode'  (Dual  *kalnai)'^
ksl.  kaliti  .abkühlen,  härten  (glühendes  Eisen)',  serb.  prikala  ,Reif'.
Zusammenhang  mit  kel-  .schlagen'  wäre  möglich.
WP.  I  357,  WH.  I  139 ff.;  388.
2.  kal-,  kali-,  kalu-  , schön,  gesund'.
Ai.  kalyd-  ,gesund,  rüstig',  kalyäna-  , schon,  heilsam'  {-äna-  ==  *älno-  zu gr.  (hXsrr],  wllöv,  oben  S.  308  f.) ;  gr.  *xcAZo-  =  ai.  kalya-  (?)  als  Grundlage von  Y-alllißv,  TLallLOTog  , schöner,  schönst',  v.&XXoq  n.  , Schönheit',  y.aXktv(xi , mache  schön',  ion.  -MiXIovr}  .Schönheit',  %aXXi-  als  1.  Kompositionsglied: daneben  mit  Formans  -u-  böot.  %aXf6g  =  hom.  xßAdg,  att.  usw.  %äX6q , schön';  dazu  als  Spottname  -/.allläg  ,Affe'  und  vielleicht  YAXXaiov  n. (meist  PL)  ,Hahnenkamm'.
i-Stamm  anord.  halr  (*hali-)  ,Mann,  Herr'  (poet.),  ags.  haele(d)  .Mann', asächs.  helid,  ahd.  helid  ,Mann.  Kämpfer,  Held',  aschwed.  hälitli,  daneben w-Stamm  anord.  hgldr  , freier  Bauer,  Mann'  (^halup).
WP.  I  356,  443,'  Specht  Idg.  Dekl.  128.  195;  Seiler,  Die  primären  gr. Steigerungsformen  68  ff.
5.  käl-  (köl-?)  , Gefängnis,  gefangen  (sein)'?
Ai.  kärä   .Gefängnis';    lit.  kaliü,    kaleti   .im    Gefängnis    sitzen',    kalirü, kalejimas  .Gefängnis',  kalinys  .Gefangener'. WP.  I  356.
```


## [2026-09-06T15:35:31.073Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK grep kak- root header ===\"\ngrep -n -E \"^k.ak-|kak-\\s+,|kak-\\s+‚|,vermögen|helfen'\" POK_02.txt | head -30\necho \"--- grep in POK_full ---\"\ngrep -n -E \"k.ak-.*(vermögen|helfen)\" POK_full.txt | head -20"
}
```


### [2026-09-06T15:35:31.147Z] TOOL RESULT

```
=== POK grep kak- root header ===
2395:lit.  nuo-y  pa-jegä  ,Kraft,  Vermögen^,  jegiil,  ßgti  ,vermögen,  stark  sein^, lett.Je^a  , Verstand^,  Je^^  , fassen,  verstehen^ ;  ob  hierher  das  isolierte  russ. dial.  jdglyj  ,heftig;  eifrig;  geschwind^?  (s.  Berneker  443).
2717:kak-  , abmagern'.
2721:kak-  (kek-?)  , vermögen,  helfen'.
2722:Ai.  saknöti  ,kann,  ist  imstande,  hilft',  Desid.  nksati  ,hilft,  huldigt, dient,  lernt',  sakti-  f.  ,Hilfe',  sakra-  ,vermögend',  sagma-  ,vermögend,  hilf- reich', sdcl  f.  ,Vermögeu,  Hilfe',  sdka-  m.  ,Kraft,  Hilfe',  ääkd-  ,kräftig, helfend;  m.  Helfer',  säkman-  n.  ,Hilfe';  y^\.  sdkvan-  ,geschickt';
2782:Idg.  kamp-  ist  möglicherweise  eine  Erw.  von  *kam-  , biegen,  wölben' (s.  auch  die  ähnliche  Wz.  {s)kamb-  von  gr.  axafxßög,  gall.  Cambio-dünum usw.);  doch  vgl.  auch  die  nasallose  gleichbed.  Sippe  von  ai.  cäpa-  m.  n. ,BogenS  capald-  ,unstet,  schwankend',  npers.  cap  ,link',  d.  i.  ,*krumm'; Endzelin  KZ.  44,  63  erinnert  für  *capala-  auch  an  lett.  kaparuoties ,zappeln',  k'epardt  , zappeln,  sich  mühsam  forthelfen',  lit.  käpanotis  , liegend sich  aufzuhelfen  suchen'  oder  , mühsam  gehen'.
3256:kelb-,  kelp'  ,helfen'?
3257:Got.  hilpan,  aisl.  hjaljpa,  as.  ags.  helpan,  ahd.  helfan,  helphan  ,helfen'; lit.  selpiü,  §elpti,  alit.  selhinos  ,helfen,  fordern' ;  unklar  ist  das  Verhältnis zu  gelbeti  ,helfen'.
4541:kuak-.    Einzelsprachliche    Nachahmungen    des    Froschlautes    und   Entenge- schnatters. Gr.   xoaj    ,vom   Quaken    des    Frosches',    lat.    coaxare    , quaken'    (wohl Nachbildung   von   xoa^),    dt.    quack^    quacken    ,von   Fröschen ;    schnattern (Ente)  usw.',  schwed.  mdartl.  kvaka  ,schnattern  wie  eine  Ente',  aisl.  kvaka ,zwitschern',  russ.  kvdkath  ,quaken',  u.  dgl. WP.  I  468.
5665:magh- :  znägh-  ,können,  vermögen,  helfen';  magh-ti-  , Macht'.
5671:aksl.  mogg,  mosti  ,können,  vermögen',  jpo-moHi,  Iterat.  po-magati , helfen' usw.,  aksl.  mosth,  russ.  moch  usw.  ,Macht,  Stärke'  (=  got.  mahts).
--- grep in POK_full ---
```


## [2026-09-06T15:36:05.004Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins kak ===\"; grep -n -E \"^kak-|kak-\\.|Sikh|hatch\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T15:36:05.057Z] TOOL RESULT

```
=== AHD watkins kak ===
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
344:bly Latin fridre, to crumble: FRIABLE. 3. In the Celtic source of Vulgar Latin *brisdre, the source of Old French brisier and French briser, to break: BRISANCE; DEBRIS. [Pok. bhréi- 166.] bhrekv-. To cram together. 1. Probably Latin frequens, frequent, crowded: FREQUENT. 2. Suffixed zero-grade form *bhrk~-yo- in: a. Latin farcire, to cram, stuff: FARCE, FARCI, FARCY; INFARCT; b. Greek phrassein, to fence in, enclose, block up: DIAPHRAGM. [Pok. bhareky- 110.] bhrem-'. To growl. 1. Latin fremere, to growl, roar: FREMITUS. 2. Perhaps variant *brem- in Greek bronté, thunder: BRONTOSAUR. [Pok. 2. bherem- 142.] bhrem-2, To project; a point, spike; an edge. 1. Germanic *bréma-, name of prickly shrubs, in: a. Old English brém, broom: BRooM; b. Old English diminutive bremel, brém- bel, bramble: BRAMBLE. 2. Germanic *berm-, *brem-, in: a. Middle English brimme, edge: BRIM; b. Middle Dutch berme, barm, edge of a dike: BERM. [Pok. 1. bherem- 142.] bhres-. To burst. Germanic “brest- in Old English ber- stan, to burst: BURST. [Pok. bhres- 169.] bhreu-'. To cut, break up. Extension of bher-2. 1. Suf- fixed form *bhreu-d- in Germanic *breutan, to break up, in Middle English britel, brittle: BRITTLE. 2. Suffixed form *bhreu-t- in Germanic *breuthan, to be broken up, in Old English bréothan, to deteriorate: BROTHEL. [Pok. 1. bhreu- 169.] bhreu-?. To boil, bubble, effervesce, burn; with deriva- tives referring to cooking and brewing. I. 1. Germanic *breuwan, to brew, in Old English bréowan, to brew: BREW. 2. Germanic *braudam, (cooked) food, (leavened) bread, in Old English bréad, piece of food, bread: BREAD. 3. Germanic *brudam, broth, in: a. Old English broth, broth: BROTH; b. Old French breu, broth (diminutive brouet): BREWIS; IMBRUE. II. Variant form *bhré- in Germanic *brédan, to warm, with derivatives. 1. *bréd-6, “a warming,” hatching, rearing of young, in: a. Old English br��d, offspring, brood: BROOD; b. denominative *brodjan, to rear young, in Old English brédan, to beget or cherish offspring, breed: BREED. 2. Germanic *bré- d6n-, roast flesh, in: a. Old High German brat, brdto (> German Braten), roast meat: BRATWURST, SAUERBRA- TEN; b. Old French braon, meat: BRAWN. 3. Perhaps distantly related is the Germanic source of Old French brese, burning coal, ember (> French braise): BRAISE, BRAZE?, BRAZIER?, BREEZE2, III. Reduced form “bher-, especially in derivatives referring to fermentation. 1. Suf- fixed form *bher-men-, yeast, in: a. Germanic *bermén- in Old English beorma, yeast: BARM, (BARMY); b. further suffixed form *bhermen-to- in Latin fermentum, yeast: FERMENT. 2. Extended form *bherw- in Latin fervére, to be boiling or fermenting: FERVENT, FERVID, (FERVOR); DEFERVESCENCE, EFFERVESCE. IV. As a very archaic word for a spring. 1. Suffixed zero-grade form *bhru- n(e)n- in Germanic *brunnon- in Old English burn, burna, spring, stream: BOURN!, BURN?. 2. Suffixed form *bhréw-r in Greek phrear, spring: PHREATIC. [Pok. bh(e)reu- 143, 2. bher- 132.] bhreus-'. To swell. 1. Suffixed form *bhreus-t- in Ger- manic *breustam, “swelling,” breast, in Old English bréost, breast: BREAST. 2. Suffixed zero-grade form *bhrus-t- in Germanic *brust-, bud, shoot, in Old French broust, brost, shoot, twig: BROWSE. [Pok. 1. bhreu-s- 170.] bhreus-2, To break. 1. Germanic *briisjan, to crush, in Old English brysan, to crush, pound: BRUISE. 2. Suffixed zero-grade form *bhrus-to-, fragment, in Latin frustum, piece: FRUSTULE, FRUSTUM. [Pok. 2. bhreu-s- 171.] bhri-. Eyebrow. Contracted from *bhrua-. 1. Germanic *bris in Old English bri, eyebrow, eyelid, eyelash: BROW. 2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugj6 (with cognates in Celtic and Slavic) in Old English brycg(e), bridge: BRIDGE}, [Pok. 1. bhrii- 172, 2. bhrii- 173.] bhrig-. Agricultural produce; also to enjoy (results,
572:kak-'. To enable, help. Sanskrit saknoti, he is able, he is strong: SHAKTI, SIKH. [Pok. kak- 522.]
594:keg-. Hook, tooth. 1. Germanic *hakan- in: a. Old Norse haki, hook, akin to Old English haca, hook: HAKE; b. Middle Low German hake, hook: HARQUEBUS. 2. Ger- manic lengthened form *Adka- in: a. Old English héc, hook: HOOK; b. Middle Dutch hok, hoec, hook: HOOKER}. 3. Germanic *hakila- in Middle Dutch hekel, hatchel, a flax comb with long metal hooklike teeth: HECKLE. 4. Germanic *hakkijan in Old English -haccian, to hack to pieces as with a hooked instrument: Hack!. [Pok. keg- 537.]
943:(s)keu-. To cover, conceal. Zero-grade form *(s)ku-. Variant *(s)keua-, zero-grade form *(s)kua-, contracted to *(s)kii-. 1. Suffixed basic form in Germanic *skeu-jam, cloud (“cloud cover’), in Old Norse sky, cloud: sky. 2. Zero-grade form *skd- in: a. suffixed form *ski-mo- in Germanic *skiimaz, foam, scum (< “that which covers the water’), in (i) Old High German sciim, scum (> German Schaum, foam): MEERSCHAUM (ii) Middle Dutch schiim, scum: SCUM; Db. suffixed form *ski-ro- in Latin obsciirus, “covered,” dark (ob-, away from; see epi): OBSCURE; CHIAROSCURO. 3. Zero-grade form *ku- in: a. suffixed form “ki-ti- in Germanic *hidiz in Old Eng- lish Ayd, skin, hide: HIDE?; b. suffixed form *ku-ti- in Latin cutis, skin: CUTANEOUS, CUTICLE, CUTIS; CUTIN; c. possibly suffixed form *kd-lo- in Latin cilus (> French cul), the rump, backside: CULET, CULOTTES; BASCULE, RECOIL; d. suffixed form *ku-to- in Greek kutos, a hollow, vessel: -cyTE, cyTo-. 4. Extended zero-grade form *kus- in: a. Germanic *huson- in Old English hosa, hose, covering for the leg: HOSE; b. suf- fixed form *kus-dho- (or suffixed extended form *kudh- to-) in Germanic *huzdam in Old English hord, stock, store, treasure (< “thing hidden away”): HOARD; c. Rus- sian kishka, gut (< “sheath”), akin to the Slavic source of Yiddish kishke, kishke: KISHKE. 5. Suffixed extended zero-grade form *kut-no- in Latin cunnus, vulva (< “sheath”): CUNNILINGUS. 6. Extended root *keudh- in: a. Germanic suffixed lengthened zero-grade form *hiid- Jan in Old English hydan, to hide, cover up: HIDE}; b. Germanic suffixed zero-grade form *hid-jdn- in French hutte, hut: HuT. [Pok. 2. (s)keu- 951.] skeubh-. To shove. 1. Germanic *skeuban and derivative lengthened zero-grade form *skdban in: a. Old English sciifan, to shove: SHOVE; b. Old Norse skifa, to push, perhaps akin to the probable Scandinavian scource of SCUFF, SCUFFLE!, 2. Germanic suffixed form *skub-ilé- in: a. Old English scofl, a shovel: SHOVEL; b. Middle Dutch schoffel, schuffel, a shovel, hoe: SCUFFLE?. 3. Ger- manic *skub-, *skuf-, *skup- in: a. Danish skof, jest, teasing, probably akin to the Scandinavian source of Middle English scof, mocking: scoFF; b. possibly (but quite doubtfully) Old English scop, poet (< “jester’): scoP; c. Low German schiiffeln, to walk clumsily, shuffle cards, probably akin to the source of SHUFFLE. [Pok. skeub- 955.] skeud-. To shoot, chase, throw. 1. Germanic *skeutan, to shoot, in: a. Old English scéotan, to shoot: SHOOT; b. Old Norse skj6ta, to shoot: SKEET. 2. Germanic *skutaz, shooting, shot, in: a. Old English sceot, scot, shooting, a shot: sHOT!; b. Old High German scuz, shooting, a shot: scHuss; C. Old Norse skot and Old French escot, contri- bution, tax (< “money thrown down”): SCOT, (SCOT AND Lot). 3. Germanic *skutjan probably in Old English scyttan, to shut (by pushing a crossbar): sHUT. 4. Ger- manic *skutilaz in Old English scytel, a dart, missile: SHUTTLE. 5. Germanic *skautj6n- in: a. Old English scéata, corner of a sail: SHEET?; b. Old English scéte, piece of cloth: SHEET!. 6. Germanic *skut- in Old Norse skita, mockery (< “shooting of words”), akin to the Scandinavian source of scouT*. 7. Germanic “skaut-, perhaps in Old French escoutille, hatchway: SCUTTLE}, [Pok. 2. (s)keud- 956.] skeup-. Cluster, tuft, hair of the head. 1. Germanic *skauf- in Old English scéaf, bundle, sheaf: SHEAF. 2. Possibly Germanic *hupp- in Middle Dutch hoppe, the hop plant (having tuftlike inflorescence): HoP?. [Pok. (s)keup- 956.]
```


## [2026-09-06T15:36:07.060Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN page 152 : leaf = printed+21 = 173 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==173' HRN.txt\necho \"===== HRN grep saxtan/sazidan =====\"\ngrep -n -E \"s[āaá]xtan|sāzem|sazīdan|sazidan|saz[aā]|sāxt\" HRN.txt | head -20"
}
```


### [2026-09-06T15:36:08.977Z] TOOL RESULT

```
=== HRN page 152 : leaf = printed+21 = 173 ===
- 151 -
ertanih, erman(i)sn 'niedrigen Sinnes' (Men.) ^); ai. vergl.
ddhara',
kurd. i^r; [af;'. lar; oss. t. dälä 'hinunter 0^8)1;
bei. LW. deräy n. serä, ser 'unter, unterhalb, am Fusse
von (63), ir, er (169); arm. LW. zil 'soprano' (IT üb seh -
mann, ZDMG. 35, 129, No. 22; 46, 259 No. 12).
681. zirek 'klug, entschlossen', äHr,
ai. Jlnt' 'rasch, lebhaft, thätig; aw. Jlra-, jirö.sdrö
(Geldner, 3 Yasht, 64).
af/. 0ir 'eilig'; arm. LW. 217' Vacker, ausdauernd'
(llübschmann, S. 12).
682. iiiire 'Kümmel'.
skr. jtraka- 'Kümmel*; \\}\\\\, zärak, vd. 18 (67) Gl.,
nach Haug, aber gewiss nicht richtig].
Kann in einer der beiden Sprachen Lehnwort sein.
683. eisten 'X^haxi , Praes. ziy-em; zinde; ztve^ jlve 'Queck-
silber'*'^).
Käs. ßgd^ jandd, vHandö (s. v. zinde),
ap. l^i^^-, jii'ähy 'leben'; aw. Jvaiti, d. i. jloaiti
(yt. 24, 1); phlv. zivastany z'w{i)sn, zivet (3. Sg.),
zwanddk; ai. V^jw-, jivati; arm. keam 'leben', keanfi
'Leben', kendani 'lebendig* (H. No. 142).
kurd. mn, zin 'leben'; af/. 2vand, zvandim 'Leben,
Sein , zvandai 'lebendig'.
Dazu vielleicht auch hedi, d. i. ein aus bizi ver-
lesenes hiöT (llückert, ZDMG. 8, 285, Salemann-
Shukovski, Pers. Gr. § 45 Anm.).
iünhär, zinhär s. unter np. düsten (No. 527).
*J West vergleicht hierzu das np. funbelcgto) irmäit 'llcue*.
^) Skr. Jivaha- 'lebündijj, lebhaft*; LW. arab. zifjoq , syr. 'VTi
kurd. zive^ arm. ztpak 'Quecksilber*.
===== HRN grep saxtan/sazidan =====
1999:aw. baesaza^ 'Arzenei, Arzt'; phlv. bBsazak (PPGl.),
6063:bei. LW. sazag (237). Np. nüxte, säz sind vielfach
10968:174. sacltan 'vorübergehen, ablaufen', Praes.saeet '), sazad
```


## [2026-09-06T15:36:23.089Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 174 182 183 184; do echo \"===== leaf $n =====\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | head -60; done"
}
```


### [2026-09-06T15:36:24.732Z] TOOL RESULT

```
===== leaf 174 =====
- 152 —
z.
684. £äle 'Hagel, Keif.
Ri.hrädünl' 'Hagel'; gr. ;faAa^a; hdt, (jranclo; ksl.
fjradü.
Nöldeke (mündliche Mitteilung). Neupersische
Grundform *zrade^ *zärde.
Diese Etymologie verdient vor der meinigen (KZ.
32, 588 No. 23) aus skr. Jada- 'kalt, starr, regungs-
los den Vorzug.
685. Serf 'tief*, PJniT (Is. 29, 15 ^), zerfi;.
aw. jfafra- 'tief; phlv. zufar^ zafr.
kurd. ziör, zaza /ör; afy. zavar; bei. juhl, n. jahl
(178).
686. MobTti, zöpm-), zöpin 'kurzer Speer (in Gelän bezw.
Delem gebräuchlich)', pDIT (Jer. 50, 42).
LW. ^ißvvt] (^Cvßivrj) etc. , arm. suin , syr. JOID
(de Lagarde, Ges. Abh. 67).
Die Herkunft des Wortes ist dunkel; vergl.
Hübschmann, ZDMG. 46, 250 No. 110.
687. zü$e 'Igel'.
mäz. arzarnldijl (?) ; g. jujlk,
aw. duzaka- Igel' (als Schimpfname des Hundes
verwandt) ; phlv. zUzak,
kurd. LW. arm]ijl (H.-Sch.)?, züzl (J.-J.).
S.
688. süyfeii 'machen, ausführen', Praes. säz-em, säz 'Gerät*.
Käs. Q. bäsöj, K. lesöj.
aw. i/^saC' , mit aiwi 'darbringen , ausführen
{yasnenif ; phlv. säxtan, sac(i)sn.
*) Nach Castle (bei Vullers) ,7V/.
2) Vis und Rämin, S. 49 Vers 15; z^^n^ S^*di, Bostän, S. 127
Vers 878.
===== leaf 182 =====
- 160 —
kurd. stün, istün\ af/. stan.
Die indogermanische Grundform ist nach Hübsch-
mann, ZDMG. 39, 93, "^'sthlnä-; dagegen siehe zuletzt
J. Schmidt, KZ. 32, 385 folg.
722. fiite^ *Kampf, Krieg*, süeziden,
aw. vergl. stij- *Kampf, Streit'; phlv. stej 'Kampf*
(Bund.).
Wohl zu ai. l/^t^J-, tejate 'scharf sein, scharf werden',
vergl. Desid. titiksati *sich scharf zu machen suchen,
sich zu stählen suchen gegen Etwas, d. h. Wider-
stand entgegensetzen ; gr. ötCQm, lat. in\stigärey
germ. i^stek-^) (as. stekaUy ahd. stehhan, got. staks
'Mal, Wunde').
723. sey(t 'hart, fest; sehr, se/ß.
ai. [/^^ak-, gaknoti 'vermögen, können*, skr. qaktä-
'vermögend*; phlv. sayt^ saxtak]tum (vd. 19 (47)).
bei. sak 'hart, stark, fest' (383); yidg. sukt.
V
72 t. sw/un, SU/m (Sahn. I, 29 V. 117 neben -ww, ebendas.
V. 109) 'Wort, Rede*.
Käs. K. siixan[6ni,
aw. sax'Ore (Y. 29, 4), säx^em (y. 53, 5) ('Plan, Rat,
Rede' (Bartholomae, Ar. Forsch. III, 36, 37); phlv.
sa/wi 'Wort, Rede'.
725. sed (heute geschrieben sed; AM. sed, S. 7 Zeile 15,
aber sed, S. 8 Zeile 4) 'hundert'.
aw. safa- 'hundert*; phlv. sat; ai. gatd-,
kurd. sed; af/. sal, sil; oss. sädä (218); wa;^. sar.
LW. sad.
720. ser 'Kopf; vergl. serapa 'Ehrengewand' ^).
aw. Sarah' 'Kopf; phlv. sar^ asar 'endlos' (aw.
anayra-); ai. ciras- 'Kopf; arm. sar 'Höhe, Gipfel,
Abhang' (H. No. 247).
'J Übertritt in die e-lleihe Ca. bei Feist, No. 531).
^) oiiottnts (llesycb), de Lagarde, Ooa. Abb. 208 (?); vergl.
Miklosiob,' Dcnksobr. WAW. Band 3S, 20.
===== leaf 183 =====
— 161 —
kurd. afj'. bei. (884) sar; oss. sär (220) ; wa/. sangl.
minj. sar.
121. se^'üT, sera *PaIast*.
Wohl zu aw. l/^i^rcl-, ^h'äyeinfi 'schützen , ai. yträ-^
trdyate; phlv. srWitan.
Hierher gehört wohl auch jüd.-pers. HNID 'Vorhof'
(Is. 62, 9), arm. LW. sr»/*, srahak^ arab. LW. surädiq
(de Lagarde, Pers. Stud. 72), aber nicht der lydische
Stadtnanie Sardes (vergl. 6. Meyer, Indog. Forsch.
I, 827).
Allgemein entlehnt.
728. sut% usmh Blei', "P)nD (Jer. 6, 29).
g. aurob.
aw. srn' 'Blei'; phlv. srpin 'bleiern'.
kurd. sirift (H.-Sch.); bei. surup, suruf (855).
729. serhär, sertvär 'Last, die man auf dorn Kopfe trägt .
aw. ^sara.hära- *Kopflast', vergl. sarnharn 'capitum
tegmina' (Isid. t&, 23).
Vergl. No. 726.
730. stir-^ Vot', Suhr[äbj Suhr]esp; vergl. sur/tce^ sur/tze
llöteln'.
ap. Ou/ra- (N. pr.) ; aw. sii^/ra- rot ; phlv. sii/r ;
ai. gukrä' 'klar, licht, hell'.
kurd. sör ; afy. sür ; oss. d. sur/, t. sir/ rot, schön'
(286) ; bei. suhr^ sohr Vot, glühend' (350) ; wa/. sökr.
731. serd 'kalt', sermä 'Kälte'.
g. sart,
aw. sareta- 'kalt'; phlv. sarty sarmäk (Bund.); skr.
vergl. gigira- 'Kälte'; arm. sarn 'Eis*, sahium., sarcim
'gefrieren, erfrieren' (H. No. 245) ; lit. szdlfas 'kalt'.
kurd. sür; afy. sör; oss. t. sald 'Kälte' (219); bei.
.sa/d, n. särf (336) ; wa;^. sür, süri.
np. sei'ma erklärt Nöldeke (mündliche Mitteilung)
überzeugend als Analogiebildung nach germä 'Wärme' ').
*j Lit. szarmä kann ihm also nicht gleichgeaetzt werdon
(Bezzonberger, Beitr. z. Gesch. der lit. Sprache, Ol).
II r II , (jiunUriüM tl. iioup. Ktyiuologpie. 11
===== leaf 184 =====
— 162 -
732. siristen 'niisclien, vermengen; schaffen, bilden, sirls
{*sires)j siriäem 'Leim* *).
aw. l^sraes- , sraesyeiti 'sich an etwas hängen ;
phlv. sristan^ sresct (PPGh); ai. skr. [/^rres-^ (^les-^
rlisyatl Verbinden, zusammenfügen'.
sar. xlr/'am ^vermischen, mengen etc.'
733. sirUk "Tropfen .
aw. sraska- 'Hagel' (Justi); für srasc- nimmt
Geldner, KZ. 27, 252 die Grundbedeutung giessen*
an, aw. sraska- bedeutet vielleicht 'Reif, Nebel'.
Unsicher.
734. serTfy sm% serfm *Horn'.
aw. srvä' *Klaue, Hörn'; phlv. srüh (d.i. srtn^), snw.
bei. srunbe^ surum 'Huf (348) -).
7»>r>. suvTiden singen, Praes. seräy-em^ seräf/tden 'singen;
sprechen (Sahn. I, 70 Vers 156), seräyis^ siirüd Lied'.
aw. l'^sruv-, (^aus. srävayeüi; phlv. srüfan 'recitiren',
srayltan^ sräy(i)su^ srüt 'Gesang; ai. l/'grav-^ Caus.
^rävdyati.
wa/. sirav-am^ sar. nasrav-am 'recitiren*.
736. seröä 'Engel' (Vis und RämTn, S. 37, V. 4 v. u.).
aw. Sraosa-; phlv. Srös, vergl. asrös ungehorsam*
(aw. asraosa-),
737. snrTniy surtn 'Hinterbacken, Hinterer.
aw. sraoni- *Hüfte*; phlv. sarük, vd. 8 (178) (181),
sarin 'Hinterer (Bund.) , sar'mak (PPGl.) ; ai. grmü'
'Hinterbacke, Keule, Hüfte'; lit. szlaimis, lat. cliinis,
gr. XA0I7C,' (?), ahd. hlatm ^).
bei. saren 'Lenden, Hüften* (338, wohl in sarzn zu
ändern, vergl. Hübschmann, ZDMG. 44, 555 unter
No. 2) ; wa/. simj, siyn. saun, sar. xdiin,
738. seztden sich ziemen, passen, sezä, sezäyiden.
phlv. sacifan^ sacPt (päz. sazed, saSSd), sacäk.
*) Afy. LW. s(fle/ -, i<(dex'
^) Geiger wirft np. sum^ suub *Huf* fälschlich mit serüu *Horn*
zusammen; vergl. No. 745.
*) Arm. srunl^ ^Schienbeine, Waden', das auch seiner Bedeutung
nach nicht paast, gehört nicht liierher (Fl übschmann, No. 260).
```


## [2026-09-06T15:36:38.285Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT sac- / sixsa ===\"; grep -n -E \"sac-|sacaiti|sixs|s.xs.aiti|saka-\" BRT.txt | head -20\necho; echo \"=== BRT cag ===\"; grep -n -E \"cagvah|cagdman|cagd.-|cagəd\" BRT.txt | head -10"
}
```


### [2026-09-06T15:36:38.358Z] TOOL RESULT

```
=== BRT sac- / sixsa ===
3510:•  j.  apajcraosaka-  Adj.  'schmähsUchtig' : nivayaka  mpalnaka  apa.skaraka  'ia(NP.) ima  paiti.vJsfTUe  Yt5.95.
5739:•  j.  a-sä£ayant-  Adj.  'nicht  lehrend';  ys saite  haurvqm  iarasca  xsapanim  ayaztmnö ..  asixsJ  asJäzyS  . .  "..  nicht  lernend,  nicht lehrend  . ."  V.  iS.  5.
6074:ys. .  mazdayasnö  aojanö  'sähe  raima  (sd.)  \  13.  42,  Y.  68.  7,  14-  48;  —  a^al  nS  vacö jlsti^amnS  "V .  8.  y, —  uxltie  (sd.)  xraiwe  .  ,  *sixsaimca  (sd.)  .  .  °jvW  haäz  yat vTdrvanahe  °sät  'V.4-AS',  — yaüra  nard  vahiHät  Y.iff.ii.  LS.  'Saya  als  Adv, asavatts  'um  h^tüi  zrazdatsma  (sd.)  YL  j  sbes.  II)  '(dem  heiligen  Recht  ent- y-  'S;  —  tha  5%ravanS  .  .  ma/iyetiU  sprechtnics,  ^/«mässigesj  rechtes,  recht- vanh^s  'sähe  Yt7j.  147;  —  vahistmi  schafTenes  Tun,  Gerechtigkeit,  Recht- °i3m  yatamaide  Vr.  2g.  i ;  —  ySi  'iäi  schaffenhcit';  auch  in  kollekt  Sinn  'alles vaonarp  (sd.)  Y.  26.  4,  S;**  —  yö  yaomwas  einer  recht  tut,  bona  opera'.  i)  im iärayeiti  hs  'hm  iarayeiti  [sA.)  V._J,  31;  ■  gAw.:     huää    (sd.)    'Sim    vohucä    manä
6998:Akk.  nebeneinander  -...hl  urvarum  vaAisütii ahüm  frapärayetii  . .  a  vahUtat  ataAaot  a . .  asat  a  . .  raocSbyS  Y.ig.d.  '  b)  zeit- lich: Jravasayö  . .  ya  haca  gayai  mariisnat a  saosyaiitat  virnHrayria^  Y. 26.10;  — pu^rJ . .  apara.iri^inis  *S  da/a('*^  vttataoi (sd)  Yt/J.ii,2i,  28;—  apqm..fratii.. haca  Aä  vaxist  S  ^hü'-^^  /rsfmSJatSil pairi.sacaiti  li.48;  Yt.5.91,  V.13.1;  — S  maioyat  xsapai  N.  50,46;  —  a  darsyai \x^ä.l>airyat  (sd)  Y.  60.6;  —  vTsp?m  ä ahmst  sbes.  c)    'in,   bei',    räumlich;
7817:•  g.  a^nman-  n.  'Stetigkeit;  Unaufhörlich- keit': al  kahrplm  utayäitJs  äadät  armaiti^ 'mä  (AP.)'*  "und  Arm.  verlieh  den  Leibern Dauer  und  Stetigkeit"  Y.jo.;.  a)  LS. °m7nT  als  Adv.  'stets,  ewiglich;  unaufhör- lich"'; yi  'mSnl  mazdn  srävi  ahurd  "der ewiglich  MAk.  heisst"  Y.  45. 10;  —  yaii' gqm  karaps  usixscä  (sd.)  alhmUi  däii yücä    kavä   *'mJnI^^    urüdSyatä  (sd.)    Y.
8521:•  g.  tisig-  m.  Bezeichnung  gewisser  der zr7rrti«j?nschen  Religion  feindlicher  Lehrer und  Priester**:  at  U  psnsit  yöi  pisydntl aliiyJ  kam  yilis  gam  karafiil  'sixs'ä  aZs^- mäi  diilä  "ich  will  die  danach  fragen,  die sehen,  wie  ihretwegen  (näml,  der  Daeva wegen)  der  Karapan  und  der  Usig^'>  das Rind  der  Raserei  preisgeben"  Y.  44.20.
9581:Et.?    \^.  i>r»5nay--l    -    PÜ.    (lu   Yt.  //):    vff^geri  :   altlyS k' yaifgam  karapH  usixsca
10920:•  i-i  K'i  P*  xSnä-,  'sna-  V,  "kennen'. Praes.  14  (Inkoh.)  xsaäsa-,  16  (Des.) sixsnanha-,  —  Inf.  'xsnJy  °xsn>m;  PPfP.
11010:—  karapä  usixsca  Y.  44-30;  —  karapanB kävayascä  Y.  46. 11;  —  dssta  mazdä  xsa- ya/ä  Y.  2<9.  7 ;  — ji3  ärmaitis  Izäcä  Y.  4g.
11463:raziStam  'tarn  matäaoälam  asac-nm  Yt^l'^-^'-^-'f  ^r " '  l'^  ^VV^?^^^  ^,  '" /ff.i,'Y.25.'5,  tiy.  1.8; -razistayi  'tayä  äh^^^a  (sd.)  ..  ^parayitt  >r,J       N.4.
17240:Ar.  'biäsa-  m.  Name  eines  Raubvogels'),  — ai.  bhäsa-  m.  (auch  als  EN.);  mp.  bähai  EN. (=  ai.  ikäsaka-  EN.\  S.  noch  Marquart EranSahr  128.  —  ')  Zn  gr.  ^n;  {eine  Adler- att)  s.  Bthl.  IF.  8.  235.
22169:Ableit  aus  "vatsaka-  m.  EN.,  Feldherr  de* Fraarasyan  (mp.  veiak,  np.  i'iSra);  vgl.  Bd.  J/. 16,  Ük.  s-   15.  a  (,  23.  6),  JusTi  NB.  366.
22221:—  altaica  nS  vais  frävaoce  *sixsaim- (&A.)ca  .  .  Y.  7p.  1 1 ;  —  Ayat  "qsasuta (sd.)  yä  daiMläita  (sd.)  fraoxtä  am?r> täitt  .  .   \.  48.  1.  a)    mit    Dat    der
22361:frävaocs  Y.ig.i''>;  8;  —  aitaica  nS  •ci>\ /rävao^e  *sixsaeml%d.)ca  .  ,  Y.  ig.ji;  — imat  -/s/ramrB:  mmö  .  .  V.  iff.  18;  FrW.  | /,  3 ;  —  ff  ?/5 .  ■  v3x/ ..  ä  'c5  oAunS  vairyö  \
25120:•  j.  ra-piihwä-  f.  'Mittag':  haca  '%wayät *matlyai  utayarai  pain.sacaiti  "sie  währt vom  Mittag  bis  zum  halben  Nachmittag" ^■49',  —  äat  yimB /ralasat  raoch  ä  upa •%wqm  hu  paiti  ahwanam  "da  ging  Y. zum  Licht  vor  am  Mittag  dem  Pfad  der Sonne  entgegen"  V,  3.  10.
25859:■  im  Gegensatz  zu  den  AmSp.:  lä  PfPr.  sa/ia-*^;  j-Aor.  i    saxs-.    —    PFP. ävisyä  rätayS  (sd.)  antan  ^amisisia  spmtS]  *sixsaya:
25865:'lehren',  b)  Des.  'lernen':  yazamaide  .  . manmna  vtrfztmna  *jixsfmna^>  s3ca- yamna  Y.  55.  6;  —  paitihiamil>m  v>r>- sintim  *sixs>ni)m^''  säiayant>m  Vyt. 52;  —  mamitim  *r>r?zint»m  sixhnt?m sä^ayantim  P.  13.
25898:■  p.  saka-  Adj.,  bezeichnet  ein  Volk 'Sake,  Skythe'*':  iyam  sku'ki^  hyi^  'kJ' Bh,k;S.j; —  'kä  *Aaumavaria  (sd.)  'kä tigraxauda  (sd.)  .  .  *ka  tyaiy  *tara^drayc^ (sd.)  D.  6. 3;  5.  a.  a)  Sing,  in  kollekt. Sinn :  ima  dahyäv(^  tyä  mana  paHyaisi^ ..  -itf*  Bh.l.6;2.2.
26322:•  j.  sixsant-  Adj.,  PPA.:  s.  'sak-. KompE.
28987:v^  tyä  Aacäma''  Aami%'iya  abavcC  Bh. 2.  2;  s,  ?.  5,  13',  5.  I.  i)zeiUich'\Qn. -  an,  inde  ab';  a)  im  jAw.:  ana  niam yasnayazaesa..A°  hU  vaxsa^ ä  Aufräsrnd.- diitsil  Yt.  5.  91 ;  —  kaAmai  A'  usaAinanqm gähantim  ratu/ri^  frajasaiti  N.  46;  *4y, *48,  4g,  50,  *$! ;  —  A'  Au  vaxiat  a  *Aa ''frälmd.datdit  pairisacaiti  N.  48;  4Ö,  47i 4(7—573;  —  fravasayS  . .  yi  h'  gayät matyhnat  ä  saosyantst  v»r3%raynat  Y.  26, 10.  "c)  im  Ap.:     «(Va*   xiah^am    A'

=== BRT cag ===
```


## [2026-09-06T15:36:40.762Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n -E \"^saxt|^sāxtan|^sazīdan|^sac|^sāz\" PHD.txt | head -20\necho \"=== PHD_mackenzie ===\"; grep -n -E \"saxt |sāxtan|sazīdan|sazidan\" PHD_mackenzie.txt | head -20\necho; echo \"=== CHEUNG sak / sač ===\"; grep -n -E \"\\*sak|\\*sa[cč]|sāxtan|sazīdan\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T15:36:40.902Z] TOOL RESULT

```
=== PHD ===
3493:sacrifice hādēxt.
4813:saxt
4814:saxtan, saxtan süg, sak say- sahigih sahig, sivag sas
=== PHD_mackenzie ===
4093:passaxt [ps)ht l ] test.
4513:saxt [s(')ht N -] strong, hard, severe(ly); very.
8599:passing                   J\"'UQ.>      passaxt                 \l'tX..tU.J V
9033:saxt                        \If.)U)     saxt                       ,~

=== CHEUNG sak / sač ===
19564:*KHOTANESE: ? pära- ‘cake’ (from *sacrificial offering’ ?, *parH?). © The form 
21191:*sacl 323 
21216:*sač! ‘to fit, be suitable, be able, be in command of; to prepare’ 
21245:324 *sac2 
55138:*män (s.v.), *sac? (s.v.), 
55200:*kas', *maH' (s.v.), *sac? 
55210:(s.v.), *paus (s.v.), *sac? (s.v.) 
55321:*kar (s.v.), *sac’, *tary (s.v.), 
55484:*sac? 
55521:*(d)banz’, *sac 
56600:*(d)banz’, *sac 
57336:*fan, *sac?, *xar 
57388:*sac? 
58231:(s.v.), *had (s.v.), *sac? (s.v.)
```


## [2026-09-06T15:36:47.234Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21191,21250p' CHEUNG.txt"
}
```


### [2026-09-06T15:36:47.280Z] TOOL RESULT

```
*sacl 323 


*SANSKRIT: rah ‘to be lost, be lonely’ (GrSu.+), || rahas- (n.) ‘secrecy, loneliness’ 
(Ер.+) > EWAia П: 442 

9 Henning, l.c. derived SSogd. ’pr’st and Yghn. piráyZ- from *apa-raz-, to which he 
added as cognates, Skt. rah, OP rad-, MP rastan [wrongly cited: rastan], NP rastan. 
Mayrhofer, Le, has apparently overlooked this footnote and only acknowledges the 
Ir. ‘secret’ forms as related to Skt. rah: MP, NP raz, etc. The meanings ‘secret’ and 
‘to flee, escape’ are not necessarily incompatible, if we assume an older meaning *to 
escape (one’s notice)’. 

«PIE 0 The IE etymology cited in his previous work KEWA III: 49 (IE *leg"- ‘to 
lay’, Gr. Aéxoc ‘bedstead’, etc.) is doubted by Mayrhofer in EWAia, l.c. = LIV: 
401 f. | Pok.: 651 


*REFERENCES: Henning, Anc. Lett.: 612, fn. 5; Abaev, Slovar’ I: 549; Andreev — PeSéereva: 306b f.; 
EVS: 71a; DKS: 359a f.; Werba 1997: 370 f.; Lecoq 2002: 127; NEVP: 10 


Š 


*sač! ‘to fit, be suitable, be able, be in command of; to prepare’ 

*MIDDLE PERSIAN: MMP sz-, BMP sc- /saz-/ ‘to be fitting, becoming, necessary, 
due’, BMP s’c- /saz-/ (caus.) ‘to make, prepare; [+ zyn /zén/] to saddle’, BMP scyn- 
/sazen-/ (sec. caus.) “to put into practice’ || (+ *pati-) MMP ps’c- (caus.) ‘to prepare, 
arrange’ || (+ *ham-) MMP hs’c- ‘to make ready’ or ‘to fix, dispose’, MMP hs’cyh- 
(pass.) ‘to be fixed, built, constructed’ > DMMPP: 306, 284a, 185b 

Pres.: IND. 3sg. MMP szyd ‘it should’, BMP scyt /sazéd/; Partic.: perf. pass. BMP scyt /sazid/; Caus.: 
pres. IND. 3sg. BMP scynyt /sazénéd/, 3pl. BMP s’cynd /sazénd/, IMPV. 2pl. BMP s’cyt /sazéd/; Inf.: 
BMP scstn /sazistan/ || (+ *pati-) Pres. IND. 1sg. BMP ps’cm /passazum/, 3sg. BMP ps’cyt /passazéd/, 
3р1. MMP ps’cynd; Partic.: perf. pass. BMP ps’htk /passaxtag/, MMP ps’xt, ps xt, Inf: BMP ps’htn 
/passaxtan/ || (+ *ham-) Pass.: pres. SUBJ. 3sg. MMP hs’cyh’d; Partic.: perf. pass. MMP hs’xt, hs xt 
*PARTHIAN: sc- ‘to be prepared, fitting, ready’, s’c- (caus./tr.) ‘to prepare, form’ || (+ 
*abi-) hw-’bs’gyft ‘docility, gentleness’ (+ hw- ‘well-, eu-’) || (+ *pati-) ps’c- ‘to 
make, prepare, fashion, arrange’ || (+ *ni-) nys’Z- (caus.) ‘to prepare, make ready’ 
= Ghilain: 50, 68 | DMMPP: 306a, 305a, 191b, 283b f., 254a 

Pres.: IND. 3sg. scyd; Partic.: perf. pass. caus. s’c’d; Caus.: pres. IMPV. 2pl. s’cyd || (+ *pati-) Pres.: 
IND. 3sg. ps’cyd, ps’cynd; Partic.: perf. pass. psxt, II ps’c’d || (+ *ni-) Pres.: SUBJ. 2pl. nys’c’d, IMPV. 
2р1. nys'Zyd 

*KHOTANESE: säj- ‘to learn’ = SGS: 132 

*SOGDIAN: SSogd. s'c, CSogd. s’c ‘to be proper, behove’, BSogd. s'c, MSogd. s’c 
‘to be necessary’ || (+ *abi-) BSogd. ’Bs’xs- ‘to be trained, accustomed, tamed’, 
BSogd. 'Bs"'c- ‘to tame, train’ || (+ *a-) CSogd. ’s’qy ‘suitable’ || (+ *pati-) BSogd. 


324 *sac2 


pts’y, CSogd. pts'c ‘to arrange, order’ || (+ *ham-) BSogd. ’ns’xs-, CSogd. ’sxs- ‘to 
be arranged, reconciled’, BSogd. ’ns’’c ‘to fix, erect, dispose’
```


## [2026-09-06T15:36:49.661Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD mackenzie saxtan/sazidan/sac ===\"; grep -n -E \"saxtan|sazi|sac[iī]|sāz\" PHD_mackenzie.txt | head -20\necho \"=== PHD.txt context 4810-4820 ===\"; sed -n '4808,4820p' PHD.txt\necho \"=== NYB glossary saxt ===\"; grep -n -E \"saxt|sāxtan|sacītan\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T15:36:49.734Z] TOOL RESULT

```
=== PHD mackenzie saxtan/sazidan/sac ===
1212:a~sazi§nlig ['scfn-yk ] imperishable, permanent.
4094:passaxtan, passaz- [ps'htn', ps'c- I M ps'xt, ps'c-] fashion, prepare;
4491:sanJ-, v. saxtan.
4518:saxtan, sanj- [s'htn ' , sne- 1 N -] weigh.
4519:saxtan, saz- [s'htn', s'e- 1 (P s'e-), N .......] make, prepare; tolerate.
4527:2saz-, .......isn, v. sazistan.
4528:saz-, v. saxtan.
4532:sazistan, 2saz- [se-stn'] pass.
6267:constitution passazisn.                      corrupt gannag, winastagj v. ,·otten.
6554:exiled uzdehig.                                    fashion (fraz) brehenidan, passaxtan.
6582:felling hambahisn.                         fitness sazisn, sazagih; v. suitabilit,·.
6875: imperishability asazisnih.                injury aziirisn, iizarm, wizayisn,
6876: imperishable afrasiwand, asazisn(ig).        wizend.
6882:  insert passaxtan.                        jackal torag.
7019:long dagr, dagrand, draz.                make kardan, saxtan.
7132:  omand, osomand, sazisnig.                      xem, xog.
7202:origin Cihr(ag), fragan.               pass sazistan, widardan, (widastan);
7205:oryx xarbuz.                           passing sazisn, widerisn(ih).
7256:permanence asazisnih, estisn.              plaster (n.) dos, gac; (a.) dosen,
7257:permanent asazisnig.                           gacen.
=== PHD.txt context 4810-4820 ===
sen murw sezd sézdén haftād*
darr-t
PAHLAVI KEY
— AA Sri 33
süxtarih saxtih
saxt
saxtan, saxtan süg, sak say- sahigih sahig, sivag sas
зап
saxwan sahóg
sak
sárcn- sārēnīdan sālwār sālagīh sālag
sahm sāmānūmand sūmān
sahmgēn
=== NYB glossary saxt ===
286:a-frac-saci8néh [’pr’c sešnyh] the quality of not passing away, continuance, con- tinued existence (of the family) 597°. — Av. (1554) pasca frasaxtahe mašyehe ‘after mankind has come to an end’, Vd. 1928, is rendered in Phl. by pas hac fräc-sacisneh i martömän, v. sacišneh.
2135:ka [MT], with encl. ’MT-m = ’MT-t = ka-t, °MT-š = ka-š ete.: 'MT-e = ka-c: A. conj. when, as, while; because; though, whilst; if; that. 1. temporal: standard type of period referring to the past: Pāpak ka-š hàn saxtan āšnūt kas fréstit by P. when by him this word was heard a man was sent = when P. heard this he sent a man 21!; passim; if con- taining an encl. pron. the apodosis is introduced a) by adak + encl., e. g. api-n ka én tigr vist adak-in . . . vist and when We shot this arrow, We shot it ... HajB: 4-6; 545-5; — b) by api- + encl., e. g. ka hac star frac būt api-š ... guft kū then he said 60?*; — c) by the independent forms of the enclitics: am, at, aš, aman, atān, ašān: hän étén amavandeh + ka zivandak bit hom am bit that great vigour which was mine when I was alive 345-6; ka giyāk-ē päh i gospandan vēnēnd ašān avd sahét when they see somewhere a flock of sheep it will seem astonishing to them 9724-25; — the apodosis may be introduced by adak alone (v. this w.); by pas (914-*); by andar han in the meantime (561°); — ka ... apāc àyet aš Kat-Xosroi bē 6 patirak āyēt ka pat vài našast ēstēt when he comes back he will
2465:martóm [mltwm; "NSWT?] 1. in an in- dividual sense: a human being: ~ hom 62°. 631; pl. cas. rect. ~: šmāh kē ~ het 67°; har ~ aed mat to everyone came a message 208-9, — 2. ~ in a collective sense: man, mankind, men, people; when subj., mostly construed as a pl. (thus serving as the pl. cas. rect. of 1): ka hamäk ~ avinüs bē bavénd 3412-13, 672, 961-2, 9717-18 (constr. ad sensum): 19. 104°. 10618-19, 12021, but ka Krisäsp kār (ag.) martöm (subj.) özat but 351, and thus 327. 9516. — 3. with the pl. cas. obl. ~-dn [mltwm’n', "NSW'T^-n']: a) gen.: andar tant ~ -än 65°; ~ -dn nē dänistan ... rād as men do not know 8016 etc.; — b) dir. obj.: ~-an pat kunisn girend 652, ete.; — c) dat.: dišop ... but 10718 sq.; as the logical subj. of an impers. pred.: ~-dn pat én 3 rah saxt estisn men must keep steadily to these 3 ways 65977; ~-dn ... dänistan nē tuvàn 8045; ~-n ... Süyet x"astan 891-2; — d) agent: —-čin guft ku 15-16, ete.; — e) after a prep.: hac ~-Gn 7?!; passim; — f) secondarily as the cas. rect. pl.: 58. 69-19 etc. passim; — as the app. of a pl.: amah c--ün 11%; astömandän ~-dn, viturtan
2986:passacakiha [psckyh’] in due course 1110.22, — Adv. of passacak ‘proper, ap- propriate, conformable’, from  pat-sac-, v. saxtan, sacāk, passat.
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
3008:homänäk, pat mānākēh similar(ly); pat nazdikéh i 7418 (pat han + fraškart nazdikéh 106%); apar pat han jaman ka 4123, adak apar pat jamān 61°; pat yuvat hac; — frame prep.: pat... rād (g. v.). — ll. in composition with a subst., forming adjectives with the sense of ‘provided, connected with’: yam i pat-göhr set with jewels 6°; (murvdn i) pat-àp aquatic 93°; zan i pat-göhr a woman of good birth 69%; cigon andar hindükän pat-vicin but high of station 11819-11; — enlarged with the adj. ending -ömand: ka krisäsp pat-tanómand u (pat-)janomand ne bit hah if K. had not been endowed with body (pat-tan) and life (pat-jān) 342. — B. adv. (rare): in addition, moreover 96%; u pat-ic and furthermore 904. The proper adv. be- longing to pat is patiš (g. v.). - OIr *patt (Skr prati), Av. (822 sqq.) pasti, OP patiy; MPrthPrs pd, pt; Paz. pa. In all prob- ability this pa was since old in common use alongside of pač as its sandhi form (cf passaxt, passand etc.), and on it the spelling of the prep. was based by analogy with the Semitic prepositions b-, k-, l-. As however, contrary to the Sem. ws., it maintained its character of an independ- ent w., and independent ona-consonantic
3181:pursitan [pwrsytn'] to ask, followed by ku introducing direct speech 3? and passim; with a dir. obj.: to consult 481%. 6371; to ask a p. : o 68—88 passim, elsewhere hac; — about: apar 4814-25, 4912, or pat 1615; — frašn, or saxtan ~ hac to ask a question, questions 2114-15, 742.6-7, 766; with a rel. pron. as its dir. obj. 76%, 1055.9; — 6 ham ~ to deliberate 577, cf hampursitan; hakanén ham pursénd thev will converse, communicate with each other 1061-18. — Av. (997 sqq.) fras-, pres. parasa-, OP frad-, pres. p(a)rsa- (Kent); MPrth pwrs’dn pwrs-; MPrs pwrsydn pwrs; Paz. NP pursidan.
3350:sac- [sc-] pres. st., impers. it is convenient, suitable, proper: cé sacēt bütan ? what can it be? 726, 1115-16, sacet dänistan kū it is proper to know, one ought to know 6217, — From sak-, Skr $aknoti ‘to be able’ [Av. (1552 sg.) tsak- in a specialized sense]; MPrth sc-, Ghilain 50; MPrs szyd ‘shall’ (A-H II); Paz. sažīdan or sažastan (SGV) saz- or saž- (Mx); NP sazidan sazad. V. also saxt and säxtan, passäzt.
3415:saxt [s'ht', sht'] firm, strong, violent; rich, abundant 53°; emphatic, comp. ~- -tar 41? ; — adv. firmly, strongly, violently, fast 8?. 3315. 657. 6674. 85!. — MPrs sat ‘very’ (S); Paz. NP saat; pt. of sak- (v. sac-), Skr pt. sakta- ‘able, strong’. — PWN s'ht' 108%: v. passat.
3416:saxtan [s'htn'] sác- to form, to prepare, to arrange, to build, to make: asp zén ~ to saddle the horse 2514-15, 269, 2811; x'"ari$n ~ to prepare.a meal 4216, 53*; hanbürak ~ to build a storehouse 973-6.10 [sht' for s?ht'!]:!!. — Caus. of sac- (q.v.); Av. (1552) säcaya- ‘to teach’; MPrth odn s’c- ‘to prepare, to form’ (A-H III); Paz. NP sdztan sāz-; v. also passdat. saxtaréh [s’ht’lyh] industriousness, sed- ulousness 70?5. — What the Skr. v. means by the translation $isyäpanä and West by ‘flattery’ is not clear to me.
3417:saxtéh [shtyh] violence 9!.
3418:saxtan [shwn'; MRY?] word, speech, passim; ~ haciš pursēnd they ask him 742.6-7, 765-6, — Av. (1569) saxtar- ‘device, plot’; MPrthPrs sewn; Paz. saxun; NP SAXUN, suxun, SULAN.
3571:-š encl. pron., cas. obl. of the pers. pron. 3d p. sg.; regularly attached to the first w. of the sentence, preferably to particles: api-š, adak-iš, be-š, cigon-aš, ka-š, etc., or to a pron., v. ce, 2, ké, sometimes to a w. in the interior of the sentence (406, v.s.v. pat-frācēh; 48°. 914, v. below); if it is attached to a subst. it never depends on it as its poss., but refers to another w. in the sentence; it is never governed by a prep. (single exception 54%, v. s. v. apar); it has an independent form aš (g. v.). It expresses 1. the gen. his, her, its: api-š bar xrat and its fruit is Wisdom 6613; fravahr i Zartuxst api-$ tan gohr Z.’s fra- vashi and his corporeal substance 4226-27; 4-$ his, her, its: tāt matan 1-š 0... 4714; — 2. for, to him (ete.): apt-š... 6 patirak āyēnd go to meet him 741-2; api-š vát-ic hayyār bavet 25°; — 3. dir. obj.: api-š nod be barem 3915; ka-š vir royét x"arét he who believes in it eats 1002; (he said) ku-"'$ man be 6 vahist ne hilom” 3425 (dir. speech aš); — 4. the agent, passim: cigon- aš dit as soon as by him was seen 19!?; ka-š hàn saxtan āšnūt 2219; Pourušāsp hac Zartuzšt, pat višopišn i haciš, -(a)š škujt tarsenit P. was terribly frightened by him (the Karap) because of Z. that he should suffer destruction by him 488-9; still unexplained is the construction in api-š ... šamšēr HDWN-yt' (commonly for pres. girét) u tak BYDWN.x, (com- monly for kunēt, but cf hištan) 2220-21, — Proleptically, anticipating a subst.: cigon- aš dit kanicak as soon as she, the girl, saw 15°; adak-iš mčnit Pouruščisp kü then he, P., thought 40%; api-§ guft, apar apäc vast, Pourušāsp and he, P., returning said 5117-18; — anaphorical, taking up a
5312:sácaya-: saxtan
5334:saxUar-: saxtan
6100:ps’xtn, ps’c-: passaxt
6127:soxtan swend: sčkand swd: süt swyg: a-sčhišn sxt: saxt sxwn: saxUan sygyn: *sak syh: ?sih szyd: sac-
6769:patmoxtan pašsār: patisär padvazed: pat-vac- padyavand- patiyavand pšč: pad paēdā, paidà: paitäk pačma(n): patman pačvand: patvand pačvastan: patvastan pahalim, pahlum : pahlom paharčxtan, paharčž-: pahrčxtan parastidan: paristätan pardazašn: pardaxtan pasand: passand pasaxt: passaxt päsux: passaxu paščman, -màni: pašč- mančh patit: patit patkàr: ~ päya: pädak péda: paitäk pédabar: paitäm-bar pčrož: pérdz pēš: ~
6798:saxt: ~
6799:saxtan, säz-: säxtan sazä: sacäk
```


## [2026-09-06T15:37:02.188Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21250,21300p' CHEUNG.txt"
}
```


### [2026-09-06T15:37:02.236Z] TOOL RESULT

```
Well attested: Pres.: IND. 2sg. SSogd. L’ s’cy ‘it does not fit you’, 3sg. SSogd. s’ct, BSogd. s’ct, etc. || (+ 
*abi-) well attested: Pres.: IND. 35р. BSogd. ’Bs’xsty, SUBJ. 3sg. BSogd. ’Bs’xs’t, OPT. 35р. BSogd. 


‘Bs’xs’y, etc. || (+ *a-) Partic.: perf. pass. BSogd. ’’s’ytk ‘compatible’ || (+ *pati-) well-attested: Pres.: 
IND. 2sg. CSogd. “pts’cy, SUBJ. 1р1. MSogd. pts’cym, etc. 

*CHORESMIAN: (+ *aua-) m/ws’cy- ‘to make peace with’ || (+ *ni-) nscy’k ‘mean, 
vile’ || (+ *ui-) m/wsxs- ‘to separate’ || (+ *ham-) m/sxs- ‘to be united, familiar with 
each other’, m/s’cy- ‘to make straight, in order; to behave like, pretend’ > Samadi: 
219, 221, 188, 178 

*BACTRIAN: oaxo- ‘to be assessed’ = S-W, Bact.: 223a 

*NWIR: Widely attested: NP sazad ‘it is fitting’, saxtan/saz- ‘to build, construct, 
prepare’, Bal. sacit/sac- ‘to adjust, be suitable, agree’, Gz. säz-/sät (intr.) ‘to be 
reconciled with’, Abyan., Abz., Nn., Tr. sata/saj-, Anar., Varz. sate/saj-, Ard. 
sutte/suj-, Ham. satän/saj-, Isfah. satän/saz-, Jow. bam-sa:t/a-sa:d3- ‘to do, build’, 
Khuns. saz-/sät, Mah. sat/saj- ‘to prepare, do’ || (+ *a-) NP äsagdah ‘prepared, 
disposed’ (< Sogd., cf. Henning 1939: 103 f.) || (+ *pati-) NP pasaxt, NP pasagdah 
‘disposed, prepared, experienced’ (< Sogd., cf. Henning 1939: 104) 

*NEIR: Oss. I. s&zyn/sagd, D. s&zun/sagd ‘to get stuck in’, I. sazyn/sagd, D. 
sazun/sagd ‘to place (in), dig in; [also D.] to build, construct’, Pash. satol/sat- ‘to 
keep, protect’, Yzgh. saj-/saxt ‘to prepare (a bed, etc.) || (+ *fra-) Oss. D. raesazun/ 
resagd ‘to drive, strike, stick in’. © Yzgh. saj-/saxt is probably a loan word, on 
account of -xt-, instead of regular -yd- (EVS: 1.c.). || 

*SANSKRIT: Sak ‘to be able, capable’ (RV+) = EWAia П: 600 

© Although this Ir. root has a good IE etymology, it has no further IE verbal 
correspondences. 

«PIE *Kek”- ‘to achieve, accomplish, be able, capable’ => LIV: 322 | Pok.: 522 

*IE COGNATES: Olrish cécht ‘might, power’, (?) MWelsh pybyr ‘strong, solid’, ON 
hagar ‘it is fitting, suitable’ 

*REFERENCES: KPF I: 82a, 141b; EVP: 70; Abrahamian 1936: 120, 132; Lambton 1938: 78a; EVS: 73a; 


DKS: 423b f.; Abaev, Slovar’ П: 376; WIM I: 72; WIM II/1: 82; Abaev, Slovar’ III: 55, 7 Ё; Werba 
1997: 240; Lecoq 2002: 123, 126, 128 (passim); Shahbakhsh: s.v. sac- 


*sai£ чо pass' 

*AVESTAN: Y Av. sac- ‘to pass’ => Liste: 61 

Pres. them.: IND. med. 3sg. YAv. sacaite (V 18.16, V 18.24), med. 3pl. YAv. fra sacinte (V 5.10), SUBJ.
```


## [2026-09-06T15:37:03.404Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN hatch/Sikh ===\"; grep -n -E \"^hatch|Sikh|hacchen\" KLN_1966.txt | head -20\necho \"=== SKT hatch ===\"; grep -n -E \"HATCH|hatch\" SKT.txt | head -10"
}
```


### [2026-09-06T15:37:03.488Z] TOOL RESULT

```
=== KLN hatch/Sikh ===
17284:Derivatives -hat,  tr.  v.,  hat-ful,  adj., hat-less,  adj., hatt-er,  n.,  hatt-ery,  n.,  hatt-ing,  n. hatch,  n.,  door,  wicket.  —  ME.  hacche,  hecche, fr.  OE.  hate,  ‘hatch,  grating;  gate’,  rel.  to MLG.,  MHG.  heck,  Du.  hek,  ‘fence;  gate’.  Cp. hack,  ‘board’,  heck,  ‘frame’, hatch,  tr.  and  intr.  v.,  to  produce  (young)  from eggs  by  incubation.  —  ME.  hacchen ,  rel.  to MHG.,  G.  hecken,  to  hatch,  breed’,  OHG. hegidruosa,  MHG.  hegedruos,  ‘testicle’,  MHG., G.  hagen,  ‘bull  kept  for  breeding’,  and  cogn. with  Lett,  kakale,  ‘membrum’.
17286:hatchet,  n.,  a  small  ax.  —  ME.  hachet,  fr.  OF. (=  F.)  hachette,  dimin.  of  hache,  ‘ax,  hatchet’, fr.  Frankish  *hapja,  ‘sickle’,  which  is  rel.  to OHG.  happa,  ‘sickle’;  prob.  derived  fr.  I.-E. base  *(s)qSp-,  *(s)qep-,  *(s)qSp-,  ‘to  cut’,  whence also  Gk.  xoTtt;,  ‘knife’,  Lith.  kaplys,  Lett,  kap-
17288:hatching,  n.  —  Formed  fr.  hatch,  ‘to  engrave’, with  -tag,  a  suff.  forming  verbal  nouns, hatchment,  n.,  an  escutcheon.  —  From  earlier atcheament,  alteration  of  achievement, hate,  n.  —  ME.  hete,  hate  (the  second  form  is  due to  the  influence  of  the  verb  hate,  see  next  word), fr.  OE.  hete,  rel.  to  OS.  heti,  ON.  hatr,  Swed. hat,  Dan.  had,  OFris.  hat,  MDu.  hate,  Du.  haat , OHG.,  MHG.  ha3,  G.  Hafi,  Goth,  hat  is,  fr. I.-E.  base  *kad-,  ‘ill-humor,  hatred’,  whence also  Avestic  sadra-,  ‘grief,  sorrow,  calamity’, Gk.  xijSoc,  Dor.  xaSo?,  ‘care;  trouble,  sorrow’, Gk.  xtjSeueiv,  ‘to  take  charge,  tend’,  Mir.  caiss, W.  cas,  Bret,  kas,  Co.  cueth,  ‘pain,  anger'.  Cp. hatred,  heinous.  Cp.  also  acedia,  epicedium. Derivatives :  hate-ful,  adj.,  hate-ful-ly,  adv.,  hate- ful-ness,  n.
20645:khaki,  adj.,  dust-colored;  n.,  a  dust-colored  cloth used  for  military  uniforms.  Hind,  khaki, ‘dusty,  dust-colored’,  fr.  Pers.  khak,  ‘dust’, khalif,  n.  —  A  var.  of  caliph, khalifate,  n.  —  A  var.  of  caliphate, khalsa,  n.,  the  community  of  the  Sikhs.  —  Hind., fr.  Arab.  khdlisah,  ‘pure’,  prop.  fem.  pp.  of khdlasa,  ‘he  was  pure,  withdrew,  retired’,  which is  rel.  to  Akkad,  halsu,  'pure',  Heb.  hdldtz,  ‘he drew  off,  withdrew’,  hilletz,  ‘he  saved,  delivered, freed’,  Aram. -Syr.  hdldtz,  ‘he  drew  off,  with¬ drew’,  Syr.  halitzd,  ‘free’, khamsin,  also  spelled  kamsin,  n.,  a  hot  wind flowing  from  the  Sahara  for  about  fifty  days (in  March,  April  and  May).  —  Arab,  khamsin, ‘fifty’,  short  for  rikh-al-khamstn,  ‘the  wind  of fiftv  (days)’.  Khamsin  is  gen.  of  khamsin,  ‘fifty’.
35186:Sikh,  n.,  member  of  a  Hindu  religious  commu¬ nity  founded  by  Guru  Naqak  about  the  end  of the  16th  cent.  —  Hind.,  lit.  ‘disciple’,  fr.  OI. sik$ati,  ‘studies,  learns’,  desiderative  of  saknoti, ‘is  able,  is  competent’.
35188:Sikhism,  n.,  the  tenets  of  the  Sikhs.  —  Formed  fr. Sikh  with  suff.  -ism.
35293:Singh,  n.,  title  of  the  Sikhs  after  their  initiation ceremony.  —  Hind,  singh,  fr.  OI.  sirnhah,  ‘lion’. Cp.  next  word.
38870:thatch,  tr.  v.  —  ME.  thecchen,  thacchen,  fr.  OE. peccan,  ‘to  cover’,  rel.  to  OS.  thekkian,  ON. pekja,  Swed.  tacka,  Dan.  deekke,  OFris.  thekka, MDu.  decken,  Du.  dekken,  OHG.  decchen, decken,  MHG.,  G.  decken,  ‘to  cover’,  and  to OE.  pxc,  ‘roof,  thatch’,  ON.  pak,  Swed.  tak, Dan.  tag,  OFris.  thek,  MLG.,  MDu.,  Du.  dak, ‘roof’,  OHG.  dah,  MHG.,  G.  dach,  ‘roof’,  fr. I.-E.  base  *(s)teg-,  ‘to  cover’,  whence  also  L. tegere,  ‘to  cover’,  tegumentum,  ‘a  covering’, tectum,  ‘roof’  (prop.  neut.  pp.  of  tegere  used  as a  noun),  tegula,  ‘tile’,  toga,  ‘toga’,  OIr.  tech,  teg, OW.  tig,  ‘house’,  OIr.  -tuigim,  ‘I  cover’,  OCo., W.  to,  ‘roof’,  Gk.  xsyoc,  ~trr\,  ‘roof’,  and — with  initial  s — OI.  sthagati,  sthagayati,  ‘covers hides,  conceals’,  Gk.  ax^yetv,  ‘to  cover’,  azsjoq, OTiyY],  ‘roof,  oxeyavoc,  ‘covering;  covered’, OSlav.  o-stegu,  ‘garment’,  o-stegnqti,  ‘to  cover’, OPruss.  steege,  ‘bam’,  stogis,  ‘roof’,  Lith. stogas,  ‘roof’.  Cp.  deck,  deckle.  Cp.  also  detect, detective,  integument,  obtected,  protect,  stegano-, tecto-(fr.  L.  tectum,  ‘roof’),  tectorial,  tectrices, tegument,  thug,  tile,  tog,  toga.
38872:thatch,  n.  —  ME.  thacche,  fr.  thecchen,  thacchen, ‘to  thatch".  See  thatch,  v.
=== SKT hatch ===
2329:Broil  (0.  to  fry.  grill.  (F. -Tcut?) M.  E.  broiUn.^O.  V.  bruiiierAQ  boil,  roa.it tKoqacfort).  Prob.  a  frequent  form  of Q.y.  bruir,  to  roast  (Burgny);  mod.  F. brom'r.  Perhaps  of  Tent,  origin;  cf.  Dn. broeiJiH,  to  foment,  hatch  c^s,  grow  Tery hot;  G. /'rw/ww,  to  scald.  ^  We  also  find GfteL  bruiiA,  to  bod,  roast ;  lifish  brni^Aimt I  boil.
2337:brocket,  a  red  deer  two  years  old (F.  — L.)  F.  brxart,  the  same;  so  calkd because  he  has  but  one  line  to  bis F.  br0£/u,  a  spit  also,  a  tine  of  a bora ;  see  Broooh. Brood.  (E.)  ME.  /f*/.  AS (rare) ;  '  hi  br^da^  beora  /'nA/'=  lliey  now ish  their  brood ;  jf^fric's  Horn.  ii.  to.-4-I^ breed;  G.  brut.  Perhaps  it  means  'ihst which  is  hatched  by  heal ;'  allied  to  Br**' cf.  W.  brofd,  warm.
2457:Bungalow,  a  Bengal  thatch«l  house. (Pers.— Bengalee.)  Pcrs.  bangaiah,  of  or belonging  to  Bengal,  a  bungalow;  Rich. Diet.  p.  293.     From  the  name  Bengal.
4237:Covey.  (F.-L.)  O.  F.  mm,  a  brood  of partridges ;  fcm.  of  pp.  o(rav€r  \  F  (ouvtr), to  hatch,  sit.  — L.  culare,  to  lie  down,  tit. +  Gk.  «ifirT».K,  to  bei  d.    (VKUP.)
4239:iocub&te  (L)  From  pp.  of  L.  in- fu^re,  to  tit  on  egf^s  to  hatch  them.
4820:Deck,  to  cover.  (O.  Lhi.)  DxLi^ilm,to cover :  dei,  r  cover,  a  ship^s  deck.  Co^pUu with  E.  Thatch,  q.  v.
5651:Eaves,  the  clipped  edge  of  a  thatc^ roof.  \E.^  M.  E  eutu\  pi  tuesu  ( eaveses).  AS.  efese^  a  clipped  edge  J thatch ;  whence  e/etian,  to  sorar.  ^  li N/Ui  Swed.  dial,  uffs,  Goth.  M^itiMi,  a  poi from  (he  prcjectioa  of  the  eaves ;  O.  Hj e/asa.  Urig.  sense  'that  which  profi or  is  over ; '  allied  to  Over.  Dar.  Ml dropper^  one  who  stands  under  droppi from  the  eaves,  a  secret  lisicncr.
5712:Egg  (1),  the  oval  body  whence  chickens, Ac  are  hatched.  (S.and  >  M.  E  #x'.  I'l* <Si''''J  -  Icel.  <gg,  Dnn.  ag,  tiwcd.  z^^. + A.  S.  ay  (-M.  £.  ty") ;  Du.  ii.  G.  ei.  Irish ugh,  GaeL  ^h,  W.  jt-}-,  L.  ouum,  Gk.  tWi'. Allied  to  L.  auit,  a  biid.
8230:lo  hatch  or  engrave;    ace
8414:Hatoh  (0,  a  half-door.  (E.>  M.  E, AafcAe  ;  a  AaUA  also  meant  a  latch  of  a door.  North  £.  Ae^k,  A.  i>.  Aa^a,  bolt  or bar  of  a  door;  also  Aacee,  a  hook.+Du. AeA,  fence,  rail,  gate,  Swed.  Aiirk.  coop, rack,  Dan.  Aai,  hakke,  rnck.  Allied  to Hook.  The  ortg.  sense  was  prob.  a  latch or  a  catch  of  a  door ;  hence,  various  modes of  fastening.  Der.  hatchet,  pi.  sb.,  a frame  of  cross-bars  over  an  opening  in  a ship's  deck;  AaUh-itny.
```


## [2026-09-06T15:37:24.626Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SIN leaves 385-386 (pp 557-558) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==385||NR==386' SIN.txt | tr -s ' ' | head -60"
}
```


### [2026-09-06T15:37:26.429Z] TOOL RESULT

```
=== SIN leaves 385-386 (pp 557-558) ===
arcia gives a detailed description of the shrub which he says is called lampatam by the Chi- nese.7 This transcription corresponds to Chinese len-fan-fwan <v f£ @8 (literally, "cold rice ball"), a synonyme of Vu-fu-lin; pronounced at
1 G. Jacob, Oriental Elements of Culture In the Occident (Smithsonian Report for 1902, p. 520). See also Leclerc, Traits des simples, Vol. I, pp. 71, 333; and Quatremere, Journal asiatique, 1850, I, p. 222.
2 E. Wiedemann, Zur Technik bei den Arabern, Sitzber. Phys.-Med. Soz. Erl., Vol. XXXVIII, 1906, p. 355-
3 Schlimmer, Terminologie, p. 334.
4 See Beginnings of Porcelain, p. 126.
5 J. Jolly, Indische Medicin, p. 106.
6 C. Markham, Colloquies, p. 379. Cf. also Fluckiger and Hanbury, Phar- macographia, p. 712. F. Pyrard (Vol. I, p. 182; ed. of Hakluyt Society), who trav- elled in India from 1601 to 1610, observes, "Venereal disease is not so common, albeit it is found, and is cured with China-wood, without sweating or anything else. This disease they call farangui baescour (Arabic basur, 'piles'), from its coming to them from Europe." A long description of the remedy is given by Linschoten (Vol. II, pp. 107-112, ed. of Hakluyt Society).
7 C. Acosta (Tractado de las drogas, p. 80) writes this word lampatan.
Irano-Sinica— China Root, Paper 557
^odu<Td by the Portuguese by a nasalized vowel or d^hthong^ or nstanee, Jo ("typhoon"), given by Fe m o Pmto »Ji^to«e
+;™ of thP root is rat* do China ("root of China j. U The re s loveriand trade in this root from China by way of M�
� t Jo Ladakh, and probably also toPersia. The P^nt has beento^n to the Chinese from aneient times, being described by T ao Hun mn. Thl emplo^ent of the root in the treatment of Morbus americanus ■lhe employment _ described at length by Li Si-Ben, who
£££££ W 5 K 6 * S celebrated physician, who lived quotes this tert Irom iw author o£ the Pen ts-ac M
\™,,«t of Garcia 3 Li Si-cen states expressly, The yan-met uicerb riifadin the ancient recipes, neither were there any people Xcted witb this disease. Only recently did ,t arise m Kwan-tun,
whence it spread to all parts of Chin£ enumerates onl7\
„a Of Chinese loan-words in Persian, xiukjn oh *
SU "tea") ^("teapot"), «- ("paper money"), and perhaps also 6» ( tea ><ca°°"*- v Aswiu te seen, there are manymore Chinese
Persians received the knowledge of paper from the <W=^«^ be traced to a term faxWft »« (ancient pronunciation kok-dz)
; ££«~ £"* P. * - <* ♦* » « ». »«— ««• **■
^'.Thave sXnt materia! to enab.e me to publish at some later date a detaned
history of the disease from Chinese sources.
« Grundriss der iran. Phil., Vol. I, pt. 2, p. 7- ^. td \r^ t iRnn n 12* or Chines. Studien, p. 209.
adopted by the Persians and from the P =^ns bJ ™e. "^ from this vacillating
558 Sino-Iranica
Karabacek and Hoernle.1 Let us assume for a moment that the prem- ises on which this speculation is based are correct: how could the Uigur, Persians, and Arabs make kdgad out of a Chinese kok-U (or dzi)? How may we account for the vocalization a, which persists wherever the word has taken root (Hindi kdgad, Urdu kdgaz, Tamil kdgidam, Mala- yalam kdyitam, Kannada kdgada) ?2 The Uigur and Persians, according to their phonetic system, were indeed capable of reproducing the Chinese word correctly if they so intended; in fact, Chinese loan-words in the two languages are self-evident without torturing the evidence. For myself, I am unable to see any coincidence between kok-U and kdgad. But this alleged kok-U, in fact, does not exist. The word ku, as written by Hirth, is known to every one as meaning "grain, cereals;" and none of our dictionaries assigns to it the significance "mulberry." It is simply a character substituted for kou HI (anciently *ku, without a final consonant), which refers exclusively to the paper-mulberry (Broussonetia papyrifera), expressed also (and this is the most common word) by c'u fit. The Pen ts'ao kan muz gives the character ku Wt on the same footing with lxu, quoting the former from the ancient dic- tionary Si min,4 and adding expressly that it has the phonetic value of m, and is written also W . The character ku, accordingly, to be read kou, is merely a graphic variant, and has nothing to do with the word ku (*kuk), meaning "cereals."
According to Li Si-cen, this word kou (*ku) originates from th
```


## [2026-09-06T15:37:26.459Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA leaf 240 (p.225) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==240' incoming/PLA/PLA_pages.txt | head -60\necho \"=== PLA grep kagad ===\"; grep -n -i -E \"k[aā][gġ]a[dḏz]|kāġad\" incoming/PLA/PLA_pages.txt | head -20"
}
```


### [2026-09-06T15:37:28.139Z] TOOL RESULT

```
=== PLA leaf 240 (p.225) ===
käg    d                                                                            225                                                             kibäb



b’-         kägad          = käßad                q. v.


i-          Kägad:             "Papier,                Brief"            pers.       ı m.                   kagad         2, mand.         kagad,
       kagid          (p.        xVY)             3, syr.            bo‘,            aram.      1>%5°.


ebK- käfür:                      "Kampfer"                 pers.          = gäfür a. v.                6,

Se.              kafüri:                "mit          Kampfer            bereitet".

      17                                          _                           ao
‚sb         -    kaviar             =        haviar        u.      babyäri           q.    v.    7,

      L,
&v-             käkanf:             "semen             santonici,                  Alkakandschi,            Winterkirsche"                 8, syr.g
       al-kekenge"                      (p.           7 X)         9,


Js         kal:       "Hammer                od.       Griff         aus       Elfenbein"             pers.        10    ?%


l/-         käma:          "eine             Speise"            pers.          ıl    ?,    aran.      j»>1?,


Sy              - kawzabän:                   "Borretsch"                     aus    pers.      cJ L ;,Kgäwzabän                13,


u,                   kawzawan                = käwzabän                  q.    v.


SL          kibab:              "Kebab;               am   Spieß          gebratenes             scharf        gewürztes          Hammelfleisch"
       (mit          Reis)          aus       pers. <-L/’kabäb                      Mn          pers.,        hindi       kabab      od.    tk.     kebab   15



1.    Wahrmund             s.       v.,       Addai           Scher           s.    v.
2.    pahl.-paz.                 s.      v.
3.    Macuch          s.       v.
4.    Brockelmann                   s.       v.
5.    Löw       s.    v.
6.    al-MuCarrab                   s.       Ve;       TaCalibi               figh       al-luga       s.     v.
7.    Schregle             S.       652,
8. Muhit             s.    v.,          Wahrmund              s.    v.,        Addai       Scher       s.     v.,       Kamäl   s.    v.
9.    Brockelmann                   s.       v.
10. Muhlt s. v.
11.    LA.       s.       v.,       al-Mu°Carrab                   Ss.    v
12.    Fraenkel                s.       v.
13.    Löw       s.       v.
14.    Chista             Bd.       10       S.       1191.
15.    Wahrig             s.    v.

=== PLA grep kagad ===
12592:i-          Kägad:             "Papier,                Brief"            pers.       ı m.                   kagad         2, mand.         kagad,
```


## [2026-09-06T15:37:43.308Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==387' SIN.txt | tr -s ' ' | sed -n '15,45p'"
}
```


### [2026-09-06T15:37:44.929Z] TOOL RESULT

```
3 Ch. 36, p. 4.
4 See above, p. 201.
Irano-Sinica— Paper 559
Persian-Arabic word. There * no rea ^ ^^ ^
paper was adopted by the Arabs
```


## [2026-09-06T15:37:45.016Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%BA%D8%B0' --note 'page 234, root Kagas, Persian kāġaz \"paper\" etymology' 2>&1 | tail -20"
}
```


### [2026-09-06T15:37:47.179Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d7504eebe611198b.txt
```


## [2026-09-06T15:37:49.401Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' data/verification/sources/web/d7504eebe611198b.txt"
}
```


### [2026-09-06T15:37:49.443Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%BA%D8%B0
FETCHED: 2026-09-06T15:37:47Z
STATUS: 200
TITLE: کاغذ - Wiktionary, the free dictionary

کاغذ - Wiktionary, the free dictionary 

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

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Azerbaijani 

 Toggle Azerbaijani subsection 

 1.1 
 Noun 

 1.1.1 
 Declension 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Alternative forms 

 2.2 
 Etymology 

 2.3 
 Pronunciation 

 2.4 
 Noun 

 2.4.1 
 Derived terms 

 2.4.2 
 Descendants 

 2.5 
 References 

 3 
 Punjabi 

 Toggle Punjabi subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Noun 

 3.3.1 
 Declension 

 4 
 Urdu 

 Toggle Urdu subsection 

 4.1 
 Etymology 

 4.2 
 Pronunciation
```


## [2026-09-06T15:37:50.890Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==387' SIN.txt | tr -s ' ' | tr ';' '\\n' | sed -n '1,80p' | grep -n -i -E \"turk|kaga|bark|uigur|kuman|taran|kazan\" "
}
```


### [2026-09-06T15:37:52.680Z] TOOL RESULT

```
4:and, as the bark of this tree contained a milk-like sap, this word was
```


## [2026-09-06T15:37:55.608Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -n -A30 \"^ 2.2\" data/verification/sources/web/d7504eebe611198b.txt | head -5; echo \"---\"; awk '/Etymology/{f=1} f' data/verification/sources/web/d7504eebe611198b.txt | sed -n '1,80p'"
}
```


### [2026-09-06T15:37:57.190Z] TOOL RESULT

```
75: 2.2 
76- Etymology 
77-
78- 2.3 
79- Pronunciation 
---
 Etymology 

 2.3 
 Pronunciation 

 2.4 
 Noun 

 2.4.1 
 Derived terms 

 2.4.2 
 Descendants 

 2.5 
 References 

 3 
 Punjabi 

 Toggle Punjabi subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Noun 

 3.3.1 
 Declension 

 4 
 Urdu 

 Toggle Urdu subsection 

 4.1 
 Etymology 

 4.2 
 Pronunciation 

 4.3 
 Noun 

 4.3.1 
 Declension 

 4.4 
 Further reading 

 5 
 Ushojo 

 Toggle Ushojo subsection 

 5.1 
 Etymology 

 5.2 
 Noun 

 Toggle the table of contents 

 کاغذ 

 26 languages 

 Deutsch 
 Ελληνικά 
 Español 
 فارسی 
 Français 
 Magyar 
 Bahasa Indonesia 
 日本語 
 한국어
```


## [2026-09-06T15:37:59.676Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -n -i -E \"Sogdian|Chinese|Middle Persian|uncertain|Hasandust|paper\" data/verification/sources/web/d7504eebe611198b.txt | head -40"
}
```


### [2026-09-06T15:37:59.724Z] TOOL RESULT

```
304: Old Chinese 紙 ( *kjeʔ ) bor. ? 
305: Sogdian 𐼸𐼰𐼲𐼹𐼰 ( kʾɣδʾ /⁠kāγaδā⁠/ ) bor. 
308: Borrowed from Sogdian 𐼸𐼰𐼲𐼹𐼰 ( kʾɣδʾ /⁠kāγaδā⁠/ ) , perhaps a borrowing from Old Chinese 紙 ( OC *kjeʔ ).
363: paper 
365: و در آن جا کاغذ نیکو سازند مثل کاغذ سمرقندی بل بهتر va dar ân jâ kâġaz-i nêkô sâzand mis̱l-i kâġaz-i samarqandî bal bihtar And they make high-quality paper over there, similar to Samarqand paper, but even better. 
367: این کاغذ سفید سفید است. in kâġaz sefid-e sefid ast. This paper is whiter than white. 
474: B. Gharib ( 2013 ), “ Sogdian language i. Loanwords in Persian ”, in Encyclopædia Iranica, online edition , New York 
498: paper 
557: Old Chinese 紙 ( *kjeʔ ) bor. ? 
558: Sogdian 𐼸𐼰𐼲𐼹𐼰 ( kʾɣδʾ /⁠kāγaδā⁠/ ) bor. 
562: Borrowed from Classical Persian کَاغَذ ( kāġaz ) , borrowed from Sogdian 𐼸𐼰𐼲𐼹𐼰 ( kʾɣδʾ /⁠kāγaδā⁠/ ) , possibly borrowed from Old Chinese 紙 ( *kjeʔ ) . Compare Sindhi ڪاغذ ( kāġazu ) .
580: paper , document 
587: ( dated ) newspaper 
646: paper 
655: Persian terms derived from Sogdian 
656: Persian terms derived from Old Chinese 
657: Persian terms borrowed from Sogdian 
676: Urdu terms derived from Old Chinese 
679: Urdu terms derived from Sogdian 
690: ur:Paper
```


## [2026-09-06T15:38:14.608Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://www.nisanyansozluk.com/kelime/k%C3%A2%C4%9F%C4%B1t' --note 'page 234, root Kagas: Turkish kâğıt \"paper\" origin' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.iranicaonline.org/articles/sogdian-language-i-loanwords-in-persian/' --note 'page 234, root Kagas: Gharib, Sogdian loanwords in Persian (kaghadh)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%86%D9%84%D9%BE%D8%A7%D8%B3%D9%87' --note 'page 234, root Kahrpu: Persian čalpāsa \"lizard\"' 2>&1 | tail -3"
}
```


## [2026-09-06T15:38:16.356Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TTS kagat/kagas ===\"; grep -n -i -E \"kagat|kagaz|kagas|kag.d|Papier\" incoming/TTS/TTS_pages.txt | head -20\necho \"=== LKT kagad ===\"; grep -n -i -E \"k[aā]g[aă]d|kagat|kaghaz|Papier\" LKT.txt | head -20"
}
```


### [2026-09-06T15:38:20.451Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1665f224c532673f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d79d4ffed8a2b41e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c3e95691350635ac.txt
```


### [2026-09-06T15:38:20.521Z] TOOL RESULT

```
=== TTS kagat/kagas ===
14298:         &M# = Wurm {kagas hütü = ^loiie, d. h. Papierwurm); büt-
=== LKT kagad ===
1296:'Hand'  [Horn  NpEt  S.  126,  Nr.  567], dästä,  tk.  deste  'Paket,  Bündel';  hieraus rum.  testea  'Buch  Papier'  [nach  Sain  60 auch  'Dutzend'],  bulg.  teste,  russ.  dest' 'Buch  Papier  =  24  Bogen'.  [Vgl.  dazu frz.  une  main  de  papier^  [Löbel  EITAP 95.  Gorjajew  90.  Bern  SlEtWb  187. Jacob  EMA  35.
1485:'Viel  und  verworren  schwatzen';  dazu Adj.farfär  'schwatzhaft,  flüchtig,  über- eilt'; pers.  färfär  'Spielball',  färfärä 'Papierwindmühle' ;  lk./'a/-^ra'Schwätzer, Windbeutel'  [vgl.  zu  diesem  Stamme  im Romanischen,  besonders  zu  it.  farfalla 'Schmetterling',  SPITZER  in  Herrigs Archiv  GXLI,  146/149].  Hieraus  zahl- reiche romanischen  Formen:  rum.  far- fara, it.  fanfano,  frz.  fanfaron,  sp.  fan- farrön  'Schwätzer,  Prahlhans',  pg.  fan- farräo,  kat.  fanfard,  it.  fanfarone, farfaro;  siz.  farfareddu  'törichter Meusch',  farfanti  'Lügner',  farfaru 'Spitzbube' ;  Vb.  it.  farfogliare  'stottern', frz.  (dial.)  farfouUer,  sp.  farfullar. [ZromPh  XXVIII,  738.  XXX,  676.  GrS VociSic  233/234.    ML  3194.
1931:Stipa  tenacissima  oder  arundo  epigeios, eine  Pflanze  aus  der  Familie  der  Gra- mineen [sp.  esparto  'Spartogras'],  aus der  man  Malten,  Hüte,  Schnüre,  Seile für  Ziehbrunnen,  Säcke  u.  ähnl.  macht; hieraus  mit  ar.  Art.  prov.  aufo,  frz.  (alt) auffS,  (neu)  alfa  'Spartgras',  auch  papier alfa\  prov.  aufiS  'Schlafmütze';  dtsch. Halfa^vas.  [Devic  DEt  47/48.  DE  100. ML  4002.
3701:1617.  Pers.  piiiibä: 'Baumwolle',  hieraus  tk.  pembe  'dass., rosafarben';  hieraus  rum.  pambria 'Schafwolle',  jmnbeii  'blaßrot'.  Aus  der pers.  Form  pänbäk  ergaben  sich  tk. pambuk  'Baumwolle'  und  gr.  udiußaE, ■iraiißdKiov  'dass.';  hieraus  rum.  bumbac, buig.  bubak,  serb.  panmk  'Baumwolle', FUSS,  bumaga,  klruss.  buniaha,  bamaha 'Papier'  sowie  mlat.  bambaqium,  it.  bam- bagin  'Baumwolle';  aus  lat.  bombacium wurde  frz.  bombasin,  engl,  bombasine, bombazine;  dtsch.  Bombasin,  russ.  bu- mazeja  'Art  Barchent'.  [Bern  SIEtWb 100/lül.
3927:'Bündel  oder  Pack  Kleider,  Papierstoß' ; hieraus  it.  risma  'ein  Ries  Papier',  sp. \>e,.  resma,raztyia,  VBi.raima,  frz.  rame; engl,  ream,  ndl.  7'iem,  dtsch.  Eies  [mit Abfall  der  letzten  Silbe  des  it.  Grund- worts], dän.  riis,  schwed.  ris.  Dazu sp.  pg.  rima  'ein  Haufen'  (z.  B.  Kleider, Lumpen),  rimero  'Stoß,  Schicht'.  —  Man denke  daran,  daß  das  Baumwollpapier bereits  früh  von  den  Arabern  hergestellt
3928:wurde,  aber  erst  im  XIII.  Jhdt.  lernten es  die  Spanier  unter  Alfons  X.  kennen; in  Padua  und  Treviso  in  Italien  wurde das  erste  Papier  erst  um  1350  hergestellt. [DE  333/335.    Eguilaz  482.    ML  7343.
4480:Gott  außer  Allah'.  Auf  Papier  ge- schrieben, diente  sie  als  Amulett;  in der  Folge  wurden  so  ganze  Koransuren, ja  selbst  der  ganze  Koran  oder  andere theologische  Werke,  in  einen  Behälter eingeschlossen,  getragen;  auch  die  christ- lichen Ritter  aus  der  Zeit  der  Recon- quista  nahmen  diese  Sitte  an  und  trugen Reliquien  oder  Gebete  in  einem  Amulett, das  tahlil  hieß;  dieser  Ausdruck  ging dann  auf  das  Band  über,  mit  dem  es gehalten  wurde,  schließlich  sogar  auf das  andere  Band,  an  dem  das  Schwert hing;  so  entstand  sp.  taheli,  tahaH,  pg. taly,  talim  'Degenkoppel'.  [Das  Wort ftama'il  >  Amulett  hat  gerade  die  um- gekehrte Bedeutungsentwicklung  ge- nommen, s.  hier  Nr.  866  :  [DE  346/347. Eguilaz  500.
4685:'Alles,  was  rund  ist:  Kugel,  Paket,  Bün- del' [vom  Stamme  tob  'Haute,  rund  > sammeln',  Vämbery  TktEtWb  S.  178, Nr.  192  I];  hieraus  bulg.  serb.  top  'Ku- gel'; rum.  top  'Ries  Papier'.  Vom  tk. Ablativ  topdan  'vom  Haufen'  kommt rum.  toptan  im  Ausdruck  a  .vinde  cu toptanul  'im  großen  verkaufen',  top- tangiü  'Großhändler'.  [Sain  60.  Löbel EITAP  96.    Mikl  SlEtWb  359  a.
4982:Arrecife  (Cördoba)  1704 ^4ssassmeM  839 ^<o«  132 '4«äö  133 Averroes  1084 ^OTcmna  579.  893. Bagdad  170 Bairam  183 Bakkam.  190 jBa/^is  203 Bartole  259 Baumwollpapier  1723 jBeÄen  176 Belsazar  1456  a Beriberi  291 £ete  sicula  1907
```


## [2026-09-06T15:38:26.940Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; echo \"=== NISANYAN ===\"; grep -n -i -E \"kâğıt|kağıt|Farsça|Soğd|Çince|köken\" data/verification/sources/web/1665f224c532673f.txt | head -30"
}
```


### [2026-09-06T15:38:26.985Z] TOOL RESULT

```
=== NISANYAN ===
4:TITLE: kâğıt - Nişanyan Sözlük
6:kâğıt - Nişanyan Sözlük
```


## [2026-09-06T15:38:28.661Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; echo \"=== IRANICA sogdian loanwords ===\"; grep -n -i -E \"kāḡaḏ|kagad|paper|kʾγδ\" data/verification/sources/web/d79d4ffed8a2b41e.txt | head -20; echo \"=== size ===\"; wc -l data/verification/sources/web/d79d4ffed8a2b41e.txt"
}
```


### [2026-09-06T15:38:28.714Z] TOOL RESULT

```
=== IRANICA sogdian loanwords ===
=== size ===
5 data/verification/sources/web/d79d4ffed8a2b41e.txt
```


## [2026-09-06T15:38:32.157Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:38:32.164Z] TOOL RESULT

```


```


## [2026-09-06T15:38:35.877Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/k%C3%A2%C4%9F%C4%B1t",
 "prompt": "Give the full etymology entry for kâğıt: source language, forms cited (Persian, Sogdian, Chinese, Old Turkic), dates of first attestation, and any note on origin."
}
```


## [2026-09-06T15:38:37.439Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/sogdian-language-i-loanwords-in-persian",
 "prompt": "Does this article list kāḡaḏ 'paper' as a Sogdian loanword in Persian? Quote the exact sentence and the Sogdian form given."
}
```


### [2026-09-06T15:38:39.384Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:38:40.421Z] TOOL RESULT

```
I apologize, but the webpage content provided doesn't contain the actual etymology entry for "kâğıt" (paper). The page only shows the header, navigation elements, and footer of the Nişanyan Sözlük (Nişanyan Dictionary) website, but not the substantive dictionary content itself.

To provide you with the full etymology entry including source languages, cited forms, attestation dates, and origin notes, I would need access to the actual entry page for "kâğıt" from this dictionary, which isn't included in the material shared.
```


## [2026-09-06T15:38:46.006Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/k%C3%A2%C4%9F%C4%B1t' --note 'page 234, root Kagas: Turkish kâğıt \"paper\" etymology (Wiktionary)' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%F0%BC%B8%F0%BC%B0%F0%BC%B2%F0%BC%B9%F0%BC%B0' --note 'page 234, root Kagas: Sogdian kʾγδʾ \"paper\"' 2>&1 | tail -2"
}
```


### [2026-09-06T15:38:49.223Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f30185b6a36d162f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/42eda0375e7d6cb7.txt
```


## [2026-09-06T15:38:52.493Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\necho \"=== TR kâğıt ===\"; grep -n -i -E \"Borrowed|Persian|Ottoman|Sogdian|Chinese\" data/verification/sources/web/f30185b6a36d162f.txt | head -20\necho; echo \"=== Sogdian kʾγδʾ ===\"; grep -n -i -E \"Borrowed|Chinese|paper|Descendants|Persian|Uyghur\" data/verification/sources/web/42eda0375e7d6cb7.txt | head -30"
}
```


### [2026-09-06T15:38:52.560Z] TOOL RESULT

```
=== TR kâğıt ===
188: Inherited from Ottoman Turkish كاغد ( ḱāğıd ) [ 1 ] , from Persian کاغذ ( kâġaz , “ paper ” ) [ 2 ] , from Proto-Common Turkic [Term?] (compare Karakhanid [script needed] ( kāɣïd , “ paper ” ) ), ultimately from Sogdian 𐼸𐼰𐼲𐼹𐼰 ( kʾγδʾ /⁠kāγaδā⁠/ ) ; further etymology is unknown, perhaps a borrowing from Old Chinese 紙 ( OC *kjeʔ ).
540: Avery, Robert et al. , editors ( 2013 ), The Redhouse Dictionary Turkish/Ottoman English , 21st edition, Istanbul: Sev Yayıncılık, →ISBN 
548: Categories : Turkish terms inherited from Ottoman Turkish 
549: Turkish terms derived from Ottoman Turkish 
550: Turkish terms derived from Persian 
553: Turkish terms derived from Sogdian 
555: Turkish terms derived from Old Chinese 
567: Sogdian terms with non-redundant manual transliterations 

=== Sogdian kʾγδʾ ===
```


## [2026-09-06T15:39:05.520Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==387' SIN.txt | sed 's/  */ /g' | fold -w 150 | sed -n '20,60p'"
}
```


### [2026-09-06T15:39:07.259Z] TOOL RESULT

```
Persian-Arabic word. There * no rea ^ ^^ ^
paper was adopted by the Arabs
```


## [2026-09-06T15:39:11.509Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==388' SIN.txt | sed 's/  */ /g' | fold -w 140"
}
```


### [2026-09-06T15:39:13.318Z] TOOL RESULT

```
 ana r know
designation of it should had from the same ^*rf o£ a foreign language that was wdhng ^ffj^ Greek.Latin any designation for paper, uur w° <
.cotton " being ultimately
W«; R^ian *-rS °ngin^yt ? The Tibetans learned the tech- Lceable to Middle P^'a" ^^fbXve a word of their own niqueof paper-makmg from th ^
Chme e but hav ^ ^
srr&sr firsts - «« ^ 5- rs
§g£SSS3S3g|§
XaPT,s). As statea, me Kumandu,
Turkish language: "'flcS TarancC and Kazan tego.. The
origin ot rn significance "tree-bark,
^fld not rep't htre the oft-told story of how the manufacture of l neeo. nou p Qamarkand by Chinese captives in a.d. 751.
Itls well known that the Chinese were the ongmators of \
money
invention of l^^.^tJl expect to come back to this problem on and indeed was the work of Ts ^ Lun I ^ q{ Karabacek, Wiesner, and
another occasion. With ^ rf Pect ^ ™ r^chine conclusions of these scholars are Hoernle, I am not convinced ^^2°^ less theorizing), especi
ally all justified. We are in need c \™™™f^ ^mus acC0unts of many sorts of of ancient papers made in China Jhere ^^ should be cloSely 
studied, naoer hitherto unnoticed, in Chinese recorub, w 111
^According to Masudi (B. pe M~ L« P-nes d or £LH, J-Jj see also E. Drouin, Memoire sur les Huns Ephthahtes, p. 53 V v
Museon, 1895).
560 Sino-Iranica
paper bank-notes.1! The Mongol rulers introduced them into Persia, first in 1294. The notes were direct copies of Kubilai's, even the Chines
e characters being imitated as part of the device upon them, and the Chinese word llao i£ being employed. This word was then adopted by the
 Persians as lau or lav? The most interesting point about this affair is that in that year (1294) the Chinese process of block-printing was 
for the first time practised in Tabriz in connection with the printing of these bank-notes.
In his graphic account describing the utilization of paper money by the Great Khan, Marco Polo3 makes the following statement: "He makes the
m take of the bark of a certain tree, in fact of the mul- berry tree, the leaves of which are the food of the silkworms, — these trees bei
ng so numerous that whole districts are full of them. What they take is a certain fine white bast or skin which lies between the wood of the
 tree and the thick outer bark, and this they make into something resembling sheets of paper, but black. When these sheets have been prepare
d they are cut up into pieces of different sizes." In the third edition of Yule's memorable work, the editor, Henri Cordier,4 has added the 
following annotation: "Dr. Bretschneider (History of Botanical Discoveries, Vol. I, p. 4) makes the remark: 'Polo states that the Great Khan
 causeth the bark of great mulberry trees, made into something like paper, to pass for money.' He seems to be mistaken. Paper in China is no
t made from mulberry-trees, but from th
```


## [2026-09-06T15:39:25.234Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -sL --max-time 90 'https://ia801604.us.archive.org/BookReader/BookReaderJSIA.php?id=sinoiranicachin00laufgoog' -o /dev/null 2>/dev/null; echo \"try direct djvu txt\"\nfor id in sinoiranicachin00laufgoog sinoiranicachine153lauf; do\n echo \"--- $id ---\"\n curl -s --max-time 30 \"https://archive.org/metadata/$id\" | python3 -c \"import sys,json; d=json.load(sys.stdin); print(d.get('server')); print([f['name'] for f in d.get('files',[]) if f['name'].endswith('djvu.txt')])\" 2>&1 | head -5\ndone"
}
```


### [2026-09-06T15:39:29.752Z] TOOL RESULT

```
try direct djvu txt
--- sinoiranicachin00laufgoog ---
ia802807.us.archive.org
['sinoiranicachin00laufgoog_djvu.txt']
--- sinoiranicachine153lauf ---
ia802903.us.archive.org
['sinoiranicachine153lauf_djvu.txt']
```


## [2026-09-06T15:39:32.809Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -s --max-time 120 -L 'https://archive.org/download/sinoiranicachin00laufgoog/sinoiranicachin00laufgoog_djvu.txt' -o sin_goog.txt\nwc -c sin_goog.txt; grep -n -i -E \"kagad|kagas|kagat|tree-bark\" sin_goog.txt | head -20"
}
```


### [2026-09-06T15:39:35.992Z] TOOL RESULT

```
1209522 sin_goog.txt
15142:On scraping the tree-bark, the gum appears like syrup, which is called 
16990:argumentation (ibid., pp. 43-45) in regard to the alleged asbestos from tree-bark, 
20136:kagat or kagib* ("paper"). As will be seen, there are many more Chinese 
20157:1 In my opinion, the word is of Uigur origin (kagat, kagas), and was subsequently 
20168:Persians, and Arabs make kagaS out of a Chinese kok-H (or d*i)? 
20170:word has taken root (Hindi kagad, Urdu kagas, Tamil kdgidam, Mala- 
20176:kagad. But this alleged kok-Si, in fact, does not exist. The word Jhc, 
20237:Turkish language: Uigur kagat or kagas; Tuba, Lebed, Kumandu, 
20238:Comanian kagat; Kirgiz, Karakirgiz, TaranJH, and Kazan kagaz. The 
20240:mandu, and Sor, we have kagaS with the significance "tree-bark." 
27413:kagas, kagat 559 
27508:kagat, kagaz 559
```


## [2026-09-06T15:39:38.592Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nsed -n '20130,20175p' sin_goog.txt; echo \"-----\"; sed -n '20225,20260p' sin_goog.txt"
}
```


### [2026-09-06T15:39:38.667Z] TOOL RESULT

```
are not mentioned in the ancient recipes, neither were there any people 
afflicted with this disease. Only recently did it arise in Kwafi-tufi, 
whence it spread to all parts of China." 

24. Of Chinese loan-words in Persian, Horn 4 enumerates only 
iai ("tea"), tddan ("teapot"), Z&u ("paper money"), and perhaps also 
kagat or kagib* ("paper"). As will be seen, there are many more Chinese 
loans in Persian; but thewordfor "paper" is not one of them, although the 
Persians received the knowledge of paper from the Chinese. This theory 
was first set forth by Htrth, 6 who asserts, "The Arabic word 
k&ghid for paper, derived from the Persian, 6 can without great difficulty 
be traced to a term ku-chih jR jR (ancient pronunciation kok-dz') 9 
which means 'paper from the bark of the mulberry-tree/ and was 
already used in times of antiquity." This view has been accepted by 

1 Toung Poo, 1916, p. 477. 

* Pen ts % ao kan mu, Ch. 8 B, p. 2; also Ch. 4 B, p. 6 b; Bbetschnbidb*, Bot. 
Sin., pt. Ill, p. 320. 

* I have sufficient material to enable me to publish at some later date a detailed 
history of the disease from Chinese sources. 

4 Grundriss der iran. Phil., Vol. I, pt. 2, p. 7. 

1 Toung Poo, Vol. 1, 1890, p. 12; or Chines. Studien, p. 269. 

1 In my opinion, the word is of Uigur origin (kagat, kagas), and was subsequently 
adopted by the Persians, and from the Persians by the Arabs. In Persian we have 
the forms k&yad, kayid, kayo*, and kHgU (Baluci k&gad). Aside from this vacillating 
mode of spelling, the word is decidedly non-Persian. See, further, below, p. 558. 



558 Sino-Iranica 

Karabacek and Hoernle. 1 Let us assume for a moment that the prem- 
ises on which this speculation is based are correct: how could the Uigur, 
Persians, and Arabs make kagaS out of a Chinese kok-H (or d*i)? 
How may we account for the vocalization a, which persists wherever the 
word has taken root (Hindi kagad, Urdu kagas, Tamil kdgidam, Mala- 
yalam kayitam, Kannada kdgada)?* The Uigur and Persians, according 
to their phonetic system, were indeed capable of reproducing the 
Chinese word correctly if they so intended; in fact, Chinese loan-words 
in the two languages are self-evident without torturing the evidence. 
For myself, I am unable to see any coincidence between kok-£i and 
-----
of a foreign language that was willing to adopt from the Chinese 
any designation for paper. Our word comes from the Greek-Latin 
papyrus; Russian butnaga originally means "cotton," being ultimately 
traceable to Middle Persian pambak. 1 The Tibetans learned the tech- 
nique of paper-making from the Chinese, but have a word of their own 
to designate paper (Sog-bu). So have the Japanese (kami) and the 
Koreans (muntsi). The Mongols call paper tsagasun (Buryat tsaraso, 
sarahan), a purely Mongol word, meaning "the white one." Among 
the Golde on the Amur I recorded the word zausal. The Lolo have 
t*o*i f the Annamese bia, the Cam baa, boar, or biar, the Khmer credos, 
which, like Malayan kertas, is borrowed from Arabic kirtas (Greek 
xAprip)*' As stated, the Persian-Arabic word is borrowed from a 
Turkish language: Uigur kagat or kagas; Tuba, Lebed, Kumandu, 
Comanian kagat; Kirgiz, Karakirgiz, TaranJH, and Kazan kagaz. The 
origin of this word can be explained from Turkish; for in Lebed, Ku- 
mandu, and Sor, we have kagaS with the significance "tree-bark." 

I need not repeat here the oft-told story of how the manufacture of 
paper was introduced into Samarkand by Chinese captives in a.d. 751. 
Prior to this date, as has been established by Karabacek, Chinese 
paper was imported to Samarkand as early as 650-1, again in 707.* 
Under the Sasanians, Chinese paper was known in Persia; but it was a 
very rare article, and reserved for royal state documents. 4 

25. Another form in which paper reached the Persians was paper 
money. It is well known that the Chinese were the originators of 

1 See above, p. 490. 

1 S. Prabnksl, Die aramaischen Fremdworter im Arabischen, p. 245. 

1 Cf. Hoernle, Journal Roy. As. Soc., 1903, p. 670. I regret being unable to 
accept his general result that the Arabs or Samarkandis should be credited with the 
invention of pure rag-paper (p. 674). This had already been accomplished in China, 
and indeed was the work of Ts'ai Lun. I expect to come back to this problem on 
another occasion. With all respect for the researches of Karabacek, Wiesner, and
```


## [2026-09-06T15:39:57.998Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD k'gd' paper ===\"; grep -n -E \"k'.d'|kʾγδʾ|k'gd|kg\\`d|paper\" SOD_pages.txt | head -20\necho \"=== PHD kagad ===\"; grep -n -i -E \"kagad|k'kt|kāgad\" PHD_mackenzie.txt PHD.txt | head"
}
```


## [2026-09-06T15:39:59.254Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD context around krps'k (line 17512) ===\"; sed -n '17495,17525p' SOD_pages.txt\necho \"=== which leaf? ===\"; awk 'NR<=17512 && /\\[pdf page/ {p=$0} END{}' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<17512' | tail -3"
}
```


### [2026-09-06T15:39:59.786Z] TOOL RESULT

```
=== SOD k'gd' paper ===
2312:invention of paper.14 Our first direct information
2314:Letters, which are on paper and presumably the                   settlers established themselves to the south of the
2428:20 ax>. The eight letters on paper contained writing            packed bundles, he discovered a number of rolls and
2714:STi), a collection of Sogdian translations of New                  paper, silk, skin and wood. Most of them were in the
16956:4620 jywndg M                                           *xj        paper
16966:                                                                    paper
16970:       (kywy6, kywnt, q-) ©prepos. in compd. =^kwl,                (o/)paper
39057:     on knees   1238                           3509,3515,3733,6199,6341,                paper    4632, 4634, 4635
=== PHD kagad ===
```


### [2026-09-06T15:40:01.681Z] TOOL RESULT

```
=== SOD context around krps'k (line 17512) ===
4836 krmswyn =* qrmswhn                                                      Bugut. Insc. Bill
4837 qrmswhn M                                            y&ijJjJ*,     4851 krp-      B, S                               vifpUOW/oW
     k(3)rmsuyn ? (krmswyn)
                                                                             kar/lp (krph, kip) ©<SkL kalpa ©->; pi. -r>
                                                                               ^kSp^klpO
     forgiveness
                                                                             world age
     BBB 532; GMS 499; Sogdica. 63.4
4838 qrmyr       M => krm'yr                                                 TSP 6.77, 78, 20.16; BSTBL, Vim. 181, Dhu. 241;
4839 krmyr =* krm'yr                                                           Frag. Len. 69.6; MDii
                                                                        4852 krpcyk B                                    J^
4840 qrmyr rytyy          M                         tfjjj^-M^                worldly
     karmir-rete                                                             kar/lpcik =*kSpcyk
     red-faced
     GMS 968; Gersh. Sogd. Cpds. 1945, 144.1                                 BSTBL, Dhy. 161
4841 qrmyst C                                                   u>      4853 krph => krp-
     kirmist ©pi. =»kyrm-
     snakes                                                             4854 krps'k B        (<JLJ^)aJ^ i^^X^^ja^ i^JUf
                                                                             karpase  ©<Av. kahrpuna-, PahL krpwfc, <*karp
                                                                               asakax xrafstar
    STi 6.9; GMS 512, 1186
     WhwZJH
                                                                             lizard
         karn     (qrrO   ©-cAv. k&r&rttM   ®ob.   — _y                      TSF*   13iy;   C1MS   1 3e»s   Bailey   f IJV1 V   p2B




                                                              Ij&ilJ'
    mumimm      mmmUM

=== which leaf? ===
```


## [2026-09-06T15:40:08.811Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" SOD_pages.txt | head -3\nawk 'NR<=17515' SOD_pages.txt | grep -n \"pdf page\" | tail -2"
}
```


## [2026-09-06T15:40:10.580Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT kahrpuna full (line 9326) ===\"; sed -n '9320,9330p' BRT.txt\necho \"=== BRT column near kahrpuna: search 'kahrp' col numbers ===\"; grep -n -E \"^\\s*45[0-9]{1,2}\\s*$\" BRT.txt | head -3"
}
```


### [2026-09-06T15:40:11.035Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-06T15:40:12.677Z] TOOL RESULT

```
=== BRT kahrpuna full (line 9326) ===
Schaft':  anäW  a  vlJDnäsä  ya  'ias^ä  (NS.)'*|      Ableit.  aus  karma-  EN.    Auffällige  Bildung.
kmtsscä     aväil    am  y}„g  ..    "deshalb  L    ■     «tarl-   V.  'trahere',   nur   mit  Praev.
ist  die  Karapan-  und  Ä^z-a^schaft   dem  p^^^s.  2  karAa-,  24  kar^aya-.
Untergang  verfallen   durch   die   (gerade),       ^^^    „^^    .(„,[(    si^h)    fortschleppen': D^  ^- 1       i'-^j'^'  ,.    r.       .  \dafva..vain3mnfm*apa.kttrsayml^ixA.y'^
jatms  haca  ma/yäkaiioyo     vor  aller  Augen
■e  karp  hrnd.  —   '>  iF.  s.  S  393-
•  j.  kahrpuna-  m.  Name  eines  a'aft'ischen  j  schleppten  sie  die  Weiber  den  Menschen Tiers'*:  baivan  alinam  spakanqm  •■nanqmX-^^^'  Yt. /g.  80".
ava.janyai  "zehntausend  Hundsschlangen,       ^jit   ava   '(mit  sich)   herabtühren,   an- (nämlich)  K. .  ."  V.14.  5.  schwemmen':  ana  tä  vaiötm  (sd.)  ayä  . .
Pü.:  transskt.  (karpun^) ^\t  der  Erl. :  «är  ,' I  ^^^-^  ^^.^^,^  „^^„,„  ava.kar»smü  späfum tanakll],    dazu  noch:    sakihii  t  tu  afiji:  o  kuti,'  „        ,  ,     -  ».   ,        j
nülnii  "handisch,  weil  er  sich  rückwärts  auf  ^'^  ■  ■  ■  •  d»™  l«im  Vierten  Mal  Schwem- den  Hintern  setzt",  —  »    DsT.s  Zusammen-'  men  sie  einen  Leichnam  an  ,  ."  V.5.  5.
Stellung  des  Worts  mit  np.£-«ria 'Katie' (ZA.  1  tti.  kdrsati,  np.  kasiJaii,  arm.  LW.  Haritl;  s. 3.  211)  ist  falsch;  das  wäre  Aw.  'gthrpa'  dam  Hbm.  KZ.  36.  166.  —  Pü. :  kaitlan.  — oder  *gir>pa'.  'I  Hds.  aparat';  »orher  gehl /ura,  mit  dem
=== BRT column near kahrpuna: search 'kahrp' col numbers ===
9266:453
9269:454
9345:457
```


## [2026-09-06T15:40:37.388Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD_pages formfeed leaf of line 17512 ===\"\npython3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\nn=0\nfor i,l in enumerate(lines[:17513]):\n    n+=l.count('\\f')\nprint('formfeeds before line 17512:',n, '-> leaf',n+1, 'printed page ~', n+1-66)\nEOF\necho \"=== BRT leaf of line 9326 ===\"\npython3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\nn=0\nfor i,l in enumerate(lines[:9327]):\n    n+=l.count('\\f')\nprint('leaf', n+1)\nEOF"
}
```


### [2026-09-06T15:40:39.337Z] TOOL RESULT

```
=== SOD_pages formfeed leaf of line 17512 ===
formfeeds before line 17512: 258 -> leaf 259 printed page ~ 193
=== BRT leaf of line 9326 ===
leaf 277
```


## [2026-09-06T15:40:39.400Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON grep کرباسو ===\"; grep -n \"کرباسو\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10\necho \"=== BQT v3 grep کرباسو ===\"; grep -n \"کرباسو\\|کرپاسو\\|چلپاسه\" incoming/BQT/BQT_v3_pages.txt BQT_v2_pages.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T15:40:39.477Z] TOOL RESULT

```
=== MON grep کرباسو ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:42300:اشت: چلیاسه؛ کلیاسه» کرباسو کلباسو» 
MON_part2.txt:42300:اشت: چلیاسه؛ کلیاسه» کرباسو کلباسو» 
=== BQT v3 grep کرباسو ===
incoming/BQT/BQT_v3_pages.txt:29614:مردم بائد ۴ . بروزن ومعنی کریاسه‌است که‌وزغه وچلپاسه‌باشد.
incoming/BQT/BQT_v3_pages.txt:29635:‏)1( خم۱: هلندور. . (۲) خم۱:کرباسو ‎ .‏ (۳) خم۱: کرباسه ‎ .‏ (4)خم۱:کرباسو.
incoming/BQT/BQT_v3_pages.txt:29636:)0( خم۱: کرباشه . . ‎)٩(‏ خم: هللدور . . (۷) چك » چش : وزنه وچلپاسه .
incoming/BQT/BQT_v3_pages.txt:29646:. ۱ - مبکند هم نپنگرا رامو "مره عقرب بود زکرباسو ۰ آتری طوسی « فرهنگه نظام >.
incoming/BQT/BQT_v3_pages.txt:29652:سهوالقلم است « سراج اللفات بنفل فرهنگه نظام ج ه س لط > . ‎dy te‏ : کرپاسو .
incoming/BQT/BQT_v3_pages.txt:29720:۱ - رك : سام . ۴ رك :کرپاسو :
incoming/BQT/BQT_v3_pages.txt:34635:‎dey‏ ازین جهت گفته که ‎OT‏ لفظ ‎ple‏ است وچلپاسه ازاقام‌آن « فرهنگ نظام .
BQT_v2_pages.txt:6581: ‫پشت را کویندد‬            ‫وزن سلسله» لا يشت‬            ‫چلپاسه ‪ -‬ب باای فارسی بروزن تلواسه‪,‬‬
BQT_v2_pages.txt:31896:                                                      ‫‪SII‬‬                  ‫نوعی ازچلپاسه است و‬
BQT_v2_pages.txt:37970:‫گوبند ‪ - .‬و بعضی کوبند نام شهپری است در‬                       ‫و بعضی گوبند بصورت سوسمار وچلپاسه است از‬
```


## [2026-09-06T15:40:46.782Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=29646 && /\\[pdf page/ {p=$0; n=NR} END{print n\": \"p}' incoming/BQT/BQT_v3_pages.txt\nsed -n '29605,29655p' incoming/BQT/BQT_v3_pages.txt"
}
```


## [2026-09-06T15:40:47.438Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '42290,42310p' MON_part2.txt"
}
```


### [2026-09-06T15:40:48.482Z] TOOL RESULT

```
29608: [pdf page 405]
‎۸4٩ gel?‏ * ۱ - رك :کران . ۷ مسف «کرایه » (هم).

‏۸ -ظ ممحف ‎ONS?‏ » و «کرانه » (هم.) .
[pdf page 405]
کرانه ‎ao a‏
‎che as‏ اول 5 آخ رکه ‎gies‏ | وبا شین قطه دار هم‌آمده است .
باشد » مرغی است سیاء رنه وبطی‌والسیر بمنی کر پاسه ۷ (۳) - بروزنوسنی‌چلیاسه
ست پرواز ‎٩‏ - و بکر اول اجرت بار کردن | اس تکه وزغه و کریاسو (4) باشد.
اسب و شتر و ‎ond‏ واجرت اشتن درخانه‌ودکان کر پاشه ۷ )0( با شین شله دار .
مردم بائد ۴ . بروزن ومعنی کریاسه‌است که‌وزغه وچلپاسه‌باشد.
‎We 4 f‏

کرب © بفتح اول وسکون ثانی‌وبای کر بال © ‎gin‏ اول بر وزت دتبال , نام
‎ol deal sae « _‏ واندوه باشد وگویشدعریی ‎AY,‏ است از فارس و برنج آنجا مشهور
مت ‎JA‏

‎WS‏ ه پا بای‌فارسی وواو بروزن
سرداران » بممتی کرپا است و آن گیاهی باشد
دوائی که هلندوز ‎)٩(‏ گویندش .
۷

‏کربایس ‎bY Al,‏
بی نقطه و شین نقطه دار بروزن افزایش »بمعنی
کریاسه است که چلیاسه ووزغه (۷) باشد.

‏کر بز ِ- نم اول ‎My‏ بروزن‌هرعز»
خیار دراز راگوند و و بعربی قتاءالحمارخوانند.

‏کربس ‎MA,‏ بنتح اود

‏)1( خم۱: هلندور. . (۲) خم۱:کرباسو ‎ .‏ (۳) خم۱: کرباسه ‎ .‏ (4)خم۱:کرباسو.
)0( خم۱: کرباشه . . ‎)٩(‏ خم: هللدور . . (۷) چك » چش : وزنه وچلپاسه .

‏- ام مرغی است ‎Le‏ فام که برآن خالهاست . رل : مهذب الاسماء در معنی اخیل
دفرهنگه نظام > . ۴ - مأخون ‎Gil‏ « کراء ککتاب, مزد مستاجر » « منتهی‌الارب >
۴ - (عی) «کرب بالفتح » اندوه دم گیر »کروب , جمع > « منتهی‌الارب >
۴ - پیش تیخ نو روز صف , دشمن هت چون پیش دای نو ‎LS‏
‏+رودکی . ج ۳ ص ۱۰۵۹ >
۵ - کرباسکه ‏ کربانو  ‎MAS ESR Se SOUS‏
کرپاشه ‏ کربایس ۳ کربایش ‏ کربی < کریش ‏ کرفش ‎tbe‏ ؛ در اوستا ‎kabrpu‏
‏در پپلوی ‎karpu‏ .
. ۱ - مبکند هم نپنگرا رامو "مره عقرب بود زکرباسو ۰ آتری طوسی « فرهنگه نظام >.
۷ - رك : کریاسو . ۸ یکی از ‎Las OLY, oly‏ فاری بطول ۷۲ وعرض
‎Vo‏ کیلومتر ۰ از شمال محدود است بارسنجان وه‌رودشت و از مشرق بدريلچة بختکان وازجنوب
‎Oey‏ و از مغرب ‎Lage‏ شیراز , جمعیت ‎OT‏ ۱۵۰۰ نن و دارای ‎٩٩‏ قربه است « کیهان.
جفرافیای سیاسی ص ۲۶۱ ). ‎٩‏ -کربز ‎le‏ اول و بای موحده ‎Oy‏ هرمز » در برهان
خیار دراز که پمربی ‎LS‏ الحمار کوبد ‎fae‏ کوبد این عبارت خالی از خبط نیت و کوبا
سهوالقلم است « سراج اللفات بنفل فرهنگه نظام ج ه س لط > . ‎dy te‏ : کرپاسو .

‏است
```


### [2026-09-06T15:40:48.528Z] TOOL RESULT

```
کوهستانی می‌زیند و گونه‌ای از آنها در 
منازل دیده می‌شود که به سوسمار خانگی با 
کلیاسو ( کلباسه) مشهور است. مارمولک از 
حشرات و کرم‌ها تغذیه می‌کند و بهیچوجه 
اذیت و ازاری برای انسان ندارد و از این 
جهت حبوان مفیدی است. مارمولک اقسام 
مسختلف دارد و گونه‌ای از آن که بنام 
سوسمار کویر موسوم است» ممکن است 
طولش تا ۲ متر هم برسد و آن در اصطلاح 
ساکنان نواحی کویر به بزغاله مار موسوم 
اشت: چلیاسه؛ کلیاسه» کرباسو کلباسو» 
کلیاسو؛ کلسوء کرسوء چلپاسو» گلموژ 
مار مل و کت مارملو ککث. ضح. مارمولکك 
زستان را در شکاف دیوارها و زیر تخته 
سنگک‌ها میخواید و با شروع گرما بیدا 
می‌شود و به فعالیت می‌پردازد. بزغاله مار در 
اماکن باتلاقی و رودخانه‌ها نیز می‌رید و از 
تسمام حیوانات کوچکتر از خود تعد به 
می‌نماید و در رودخانه به اسانی ث شنا می کند 
و از درخت‌ها نیز به سهولت بالا می‌رود و 
تخم پرندگان و جوجه‌های آنها را می‌خورد.
```


## [2026-09-06T15:41:03.304Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(d.get('page_offset'));print(d.get('lookup_hint'))\""
}
```


## [2026-09-06T15:41:04.957Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | sed -n '1,3p'\necho \"--- search کاغذ in v3 ---\"; grep -n \"کاغذ\" incoming/BQT/BQT_v3_pages.txt | head -20"
}
```


### [2026-09-06T15:41:05.166Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


### [2026-09-06T15:41:05.234Z] TOOL RESULT

```
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
--- search کاغذ in v3 ---
9594:وسکون تحتالی ومیم ‎OLS,‏ ازصفحة کاغذسفید
16622:ودرآن چراغ با شمع نهند تا ازباد محفوظ ماند . فانوی کاغذی فانوی درشکه
23526:‏میخورند ‎Lay‏ منشا ت که چوکاغذ زر میبرند...» ,24 بسا ص ۵ح۱. در نسخ دیگرهقصب‌الجبب»
26358:کاغذ زد کاغذیرا گوبند که درآن
26359:میلفی پیچیده‌یکی دهند - وکاغذی رانیز گوبند
26380:کاغذی ‎٩‏ با زال له دار بتحتانی
26381:کشیده . کاغذ گر وکاغذ فروش را گویند- و هر
26383:کاغذی وجوزکاغذی وامثال آن .
26385:کاغذیی جامه - کنابه از عجز
26401:‏کاغذ زر میبرند .© «کلتان مه > آفای فریب کاغذ زر را بمعنی برات و حواله توشته‌اند
26402:‎OLS)‏ چاپ قربب ص 0ح؟) ومرحوم فروغی «کاغذی که قیمتی و گرالبها باشد ماننداسکنای
26406:‏_ از: کاغذ ی ‎cus)‏ واصاف) .
26408:‏۱ < کاغنی جامه = ‎ale‏ کاغذی = کاغذین , جامه‌ای بوده از کاغذ که تظلم ‎os‏
26411:‏کاغذین جامه بخوناب بشویم که فلك
26422:‏عربی « کاغة » از اصل تر کی باشد تا بقول لوفر ازاصل چینی . هرچند که اصل کاغذسازی‎ es
26428:‏کاغذ بدربدند و قلم بشکتند وز دست زبان حرف گیران بستند ‎IT «  ,‏ ۳۳ ۰۲
29753:‎wth Goi‏ مانلدکاغذ که عنکبوت سازدو درون
30933:پردٌ سفیدی را گویندمانندکاغذ که عنکیوت‌سازو
32634:کاغذ ۳ - ‎ging‏ اول وسکون انی, مخفف کوتك
43007:میم باشد . ‎gles‏ است که بر اطراف کاغذ پاره
```


## [2026-09-06T15:41:13.114Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=26430 && /\\[pdf page/ {p=$0;n=NR} END{print n\": \"p}' incoming/BQT/BQT_v3_pages.txt\nsed -n '26414,26432p' incoming/BQT/BQT_v3_pages.txt\necho \"=== and page tag for the kahrpu footnote line 29649 ===\"\nawk 'NR<=29649 && /\\[pdf page/ {p=$0;n=NR} END{print n\": \"p}' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T15:41:14.886Z] TOOL RESULT

```
26429: [pdf page 363]

‏ره نمونیم بپای علم داد ‎2G‏
‏> حافظ شیرازی ۹۸ *.

‏بفتح سوم » بقول لوفر این کلمه از ‎el‏ چینی است . در چینی

‎) ‏از پوست درخت توت‎ LS) kok - ci. (kok - ۰ ‏تلف قدیم‎ ( ku _ chih
‏اما فرای گوید بیشتر احتمال میرو ذکه‌کلمة‎ (Laufer, Sino - Iranica, p . 557 sqq)
‏عربی « کاغة » از اصل تر کی باشد تا بقول لوفر ازاصل چینی . هرچند که اصل کاغذسازی‎ es
« XXIV, Speculum) Hitti ‏فرای درباب کتاب تاریخ عرب تألیف‎ Us) ‏از چین‌است.‎
SE ‏گون‌تهيه کنندو‎ US ‏نا زکی که ازخمیر موادمختلف نباتی برنگهای‎ yy ‏#ص۵۸۱ ) ؛‎

‏نوشتن بکاربرند :

‏کاغذ بدربدند و قلم بشکتند وز دست زبان حرف گیران بستند ‎IT «  ,‏ ۳۳ ۰۲
[pdf page 363]
ake

کاغله = بختلام. مخنف کاغاله است که
=== and page tag for the kahrpu footnote line 29649 ===
29608: [pdf page 405]
```


## [2026-09-06T15:41:34.064Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD p.58 = pdf 63 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==63' incoming/FFD/FFD_pages.txt | head -40\necho \"=== FFD grep ساختن ===\"; grep -n \"ساختن\\|سزیدن\" incoming/FFD/FFD_pages.txt | head -10"
}
```


### [2026-09-06T15:41:35.788Z] TOOL RESULT

```
=== FFD p.58 = pdf 63 ===
[pdf page 63]
ها فعلهای فارسی دری
زدن
زد < فارسی میانه 240 + ایرانی باستان ۵-12[*. برای ۵ > آراست. 3[صورت
: ضعیف 20[ است» به معنی «زدل).
زن < فارسی میانه 227 < ایرانی باستان «۵[*. به 48[ چیزی برای ساختن مادهٌ
مضارع افزوده نشده است > اوژدن.
زدودن
زدود < ایرانی باستان ۶2-43-12 برای 1۵ -> آراست. ۳۶ پیشوند فعلی است. ريشهٌ
تا به معنی «پاک کردن» است.
زدای + ایرانی باستان 8ر12-437-2* 22 برای ساختن مادهٌ مضارع از ريشه به کار
می‌رفته است. 413۷ صورت بالانده و ۵5 صورت ضعیف ريشةٌ 4۵۷ هستند > اندودن.
زیستن
زیست < فارسی میانه 2731» صورت کهنتر ۰.2۷181 27181 مادةٌ ماضی جعلی است.»
از 27۷ مادةٌ مضارع.
زی + فارسی میانه ۰27 صورت کهنتر 27۷« ایرانی باستان ۷۵[*. 7۷2[ صفت است
که مادةٌ مضارع گرفته شده و از ریشهٌ ۲[: زیستن» و پسوند 2 ساخته شده است.
ساختن
ساخت < فارسی میانه ۶371 + ایرانی باستان ۹21۵". برای 1۵ -> آراست. ‎٩3‏
‏صورت اصلی 835 است» ۴ پیش از ۲ به #بدل شده است. 83 صورت بالاندةٌ 82۴ است و
ريشهٌ 8۵ به معنی «توانابودن» است.
ساز < فارسی میانه 932 < ایرانی باستان ۹30-۵". برای 2 > آرای. ۴ به 6 بدل شده

=== FFD grep ساختن ===
283:برای آن الفبایی از الفبای فارسی میانهٌ زردشتی و مسیحی ساختند و آن‌را به قید کتابت
356:۱-مادة ماضی سین‌دار.ء ماده‌ای بوده که برای ساختن آن از ريشه 8 به کار می‌رفته
360:۲-مادهٌ ماضی بی‌سین» ماده‌ای بوده که برای ساختن آن از ربشه 8 به کار نمی‌رفته
374:2 برای ساختن ماده از ریشه آمده است).
422:(صورت اصلی ۵ - ۷۷۲-۷۷۵۲2 است. ۷۲ برای مضاعف کردن آمده و 5۵ برای ساختن
516:فارسی میانه دو روش برای ساختن فعل ماضی وجود داشته است» روشی خاص فعل
549:ماد تام برای ساختن فعلهای ترکیبی» مانند ماضی نقلی و بعید و فعل مجهول به‌کار
555:۲ در فارسی دری به‌جای 27 فارسی میانه (>ان» یا «ان» برای ساختن فعل واداری
560:روشهایی که در فارسی میانه برای ساختن فعل ماضی به کار می‌رفته» در ففارسی
577:0 فارسی میانه است. 27 در فارسی میانه برای ساختن مصدر از مادةٌ ماضی به کار
```


## [2026-09-06T15:41:35.999Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT col 1552 sak- ===\"; grep -n -E \"^\\s*155[0-9]\\s*$\" BRT.txt | head\necho \"=== BRT search sāčaya ===\"; grep -n -E \"sacaya|sāčaya|s.caya-\" BRT.txt | head -5\necho \"=== HUB saxt ===\"; grep -n -E \"saxt|sāxtan|sacītan\" HUB.txt | head -10"
}
```


### [2026-09-06T15:41:38.051Z] TOOL RESULT

```
=== BRT col 1552 sak- ===
25808:1550
25862:1553
=== BRT search sāčaya ===
23016:hatqm  syaohananqm  vahiHa  ^.3^.3;  — avat  "voAvar/te  nqma  yat  vohä  virtiyami Yt  75. 44;  —  humataii  mainimna  hüxtail mrvats  hvarsiais  vinzyantB  (NP.)  Y, 70.  4;  Yt  70. 106';  —  humatanqm  hüxta- nam  hvanstanqm  ..  vpr^zyamnanafn^ä vavfnzananqmca  Y.J5.  a;  —  vJspaca hvarsla  ,  .  iyadhna  .  .  •uaritaca  vans- yamnaia  Y.  57.  4;  —  manya  manavAs humat>m  .  .  Aisva  mrBili  Aäxtsm  .  . zastalibyB  varx!a(_aS.y^  Avarltim  *Syadhrum Aog.  27;  Gs.  ;5j;  —  voAu  .  .  hvarit>m fyaohmm  vtrizimnim  V.J.  41;  —  sps- nistä  (APn.)  armatsil  Audänvansvä  3'  Y. 53- V>  — "  y^*  '"'  *'  "^'^  '^^  mq%nm Tiaryffntl(Kon).)  ya'äa  Im  mSnaica  vaocaca "die  von  euch  das  Wort  nicht  so  be- tätigen, wie  ich  es  denke  und  sage"  Y. 45-  3 ;  —  staota  yesnya  yazamaide  .  . manmna  vpr^zimna  (APn.)  *sixhmna sacayamna  Y.  55. 6;  —  kimcit  .  .  aoi marfntim  *v3r?zyant»m'''^  sixlmttm  saca-
25858:•  j.,  g.  'sak-  V.  'sich  verstehen  auf  -'. Praes.  i  sai-,  16  (Des.)  six^a-'\  26 sa^a-"'',  30  (K.aMS.)  säcaya-,  Perf  i  sa!i-^.
=== HUB saxt ===
1202:274 bis jfp pasaoct im Uiiterschied von paz. phi. pasaxt
2695:inf. saxtan (ptc. saxta gewogen ), praes. sanjam {-sanj
3560:1032. Die Form nisaxtan auch bei Fird. I, 246, v. 57 als
4672:arm. patasxani *Antwort', ap. *pati8a(h)uvan- ; np. pasaxt
4673:*bereit' aus "^patsaxt?, aber paz. phi. nur pasaxta, pasaxtak;
6769:np. pasaxt aus *patsdxt (s. oben p. 36) neben paz. phi.
6770:pasaxt etc. (Shk. 262 — 263) aus patsdxt, Diese Assimili-
```


## [2026-09-06T15:41:53.481Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS grep saxt ===\"; grep -n -E \"saxt|sxt\" SNS_pages.txt | head -10\necho \"=== BQT v2 printed 1106 -> leaf 1106-543=563 ; 1137 -> 594 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==563' BQT_v2_pages.txt | head -30"
}
```


### [2026-09-06T15:41:55.281Z] TOOL RESULT

```
=== SNS grep saxt ===
7198:                                      ^o>^=saxtag:J^
7224:                                                                               -TA/T^ .o-ltf*L :saxt 5st5d:                  ^i^ -^ t*^^
7636:                                                                                                                           .ywt«^        .   c^-tfLj- :sarmag I saxt:                                         » v*-6^*»
8553:                                                                                                   •Wt'S -O-^osxt'o^jt :abar kasldan: «»o-oj
15849:Saxt 172/8                saxt 173/6
15851:saxtag 172/11-173/10      saxttar 173/9
=== BQT v2 printed 1106 -> leaf 1106-543=563 ; 1137 -> 594 ===
  ‫‪۵‬ات‬       ‫‪4‬‬
                                                                                              ‫سثروك‬
 ‫استرءوون بمعنی شبه و مانند" باشد‪ ,‬وچون‌استر‬           ‫باشد اروماده دست در گردن هم کرده و بابها در‬
‫لمی‌زابد او را باین‌اعتبار بدین نام خواننماند ‪-۴‬‬          ‫اتی‬
                                                            ‫ییراس‬
                                                                ‫رپا‬
                                                                  ‫بررا‬
                                                                     ‫یکدیگر محکم ساخته ون‬
 ‫زولی رکاویزبند که بیش ايزك‌فرزند‬                      ‫چپ ماده افتاده است و ماده را بمکس آن»وهر‬
‫تزایینه‌باشد ‪ ۰‬وبا اول وثالی‌مضموم همآ مفهاست‪.‬‬
                                                        ‫آرا بکند باندك روزی بمترد » و حاصل‬
                                                                                         ‫کس ا‬
‫بفتح اول و الی بروزن کقل »‬         ‫‪-‬‬   ‫ستل‬              ‫کردن آن باین نوع است که اطراف نآراخالی‬
 ‫بمعنی كتك زدن وآزاردادن باشد ‪ -‬وبکراول‪,‬‬                ‫کنند چنانکه بادك قولی کنده شود؛س‌رسمالی‬
          ‫ند ® ‪.‬‬
               ‫کتخورنرا‬
                      ‫لاب و اس‬
                             ‫وبتکایر‬
                                   ‫آ‬                   ‫آوریه وبك سر ران را برآن و سر دیگر‬
 ‫ستم = بکر اول بروزن شکم‪ .‬ممروف‬                       ‫شکاری در‬          ‫جذنادلووری‬
                                                                                 ‫راکبمر سکی بن‬
                                                                                             ‫و‬
‫است که تمدی و آزار باشد ‪٩‬‏ ‪ -‬و بمعتی دبفه‬              ‫شکار‬     ‫مجالب‬    ‫يا سکه‬    ‫سگه سر دهند‬    ‫یش‬

        ‫هنتف خوالند‪.‬‬   ‫‪ ۳‬دانته لیز کفته‌اند و دمر ی‬     ‫بدود وآن از بیخکنده شود آونرا بعربی‪,‬بروج‪-‬‬
‫ستم آ پاد ک‪-‬نابه ازجابی است که‬                          ‫الستم خواند ‪ -‬وبازبی هم هت مشهوروممرول‬

                                                       ‫ز چوپ سا اند پاين ابر سترنه نل‬
 ‫آا للم و تعدی بسیار وافع شود ک‪-‬نوابه‬
                                    ‫در ن‬                ‫و چون درآن بازی صورت پادشاه ووز هردورا‬
```


## [2026-09-06T15:41:56.144Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/hatch' --note 'page 234, root Kak 1: English hatch etymology' 2>&1|tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D8%AE%D8%AA%D9%86' --note 'page 234, root Kak 1: Persian sāxtan' 2>&1|tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B3%D8%AE%D8%AA' --note 'page 234, root Kak 1: Persian saxt' 2>&1|tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Sikh' --note 'page 234, root Kak 1: English Sikh' 2>&1|tail -2"
}
```


### [2026-09-06T15:41:59.828Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e470506379c9db62.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/04e0b6eb363f0b5c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/af4dc33181777c3c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/519c2c1289f4bdac.txt
```


## [2026-09-06T15:42:15.986Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='BQT_v2_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor w in ['سخت','ساختن','سزیدن','سزا']:\n    hits=[i for i,l in enumerate(leaves) if w in l]\n    print(w, 'leaves:', hits[:12], 'n=',len(hits))\nEOF"
}
```


### [2026-09-06T15:42:17.700Z] TOOL RESULT

```
سخت leaves: [17, 21, 31, 37, 88, 109, 116, 125, 145, 155, 160, 177] n= 67
ساختن leaves: [25, 29, 42, 49, 175, 181, 193, 205, 217, 225, 240, 247] n= 47
سزیدن leaves: [599] n= 1
سزا leaves: [245, 246, 294, 457, 469, 599, 600] n= 7
```


## [2026-09-06T15:42:28.701Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in range(555,605):\n    l=leaves[i]\n    # first few non-empty words\n    import re\n    ws=[w for w in re.findall(r'[؀-ۿ]{2,}', l)]\n    print(i, i+543, ' '.join(ws[:8]))\nEOF"
}
```


### [2026-09-06T15:42:30.786Z] TOOL RESULT

```
555 1098 سییفه داز ۱۱۳ نرا یتال وابس گل کر
556 1099 بهنای سفده ورن اش نس دست بفتح دال
557 1100 يان چهارم درسین بی نقطه بانای قرشت مشتمل
558 1101 ۱۰۵۹ ستار تک ناف آن چیزست راست تنک
559 1102 ات وبضی مطلق شاخ درخت را گفتداند خواه
560 1103 هه اس ستاله گفتن لمیدحکوبی دعا وثنا وشکر
561 1104 نز شا او بقزرک وهیجث ههویکل یمت فے
562 1105 ات سثروك استرءوون بمعنی شبه مانند باشد وچون
563 1106 آن قره بطالا باشد ون رهن یاآ یس
564 1107 سوه وزن کبوتر هوابی باشد با صدا که
565 1108 ۵۳ الوث ثلی ستهی بکس اول ثا آمده
566 1109 سنیز یابگراوهبمند بممنی ستیزندگی مآسم باشد وآن بوزن
567 1110 سجلاط ونافرمالی نمودن وفرباد وشور ولجاجت کردن ستیهیدن
568 1111 نجن سچیدن بروزن درسن سرمای سجن بفتح اول
569 1112 وه سج بکر اول فتح ثانی وسکون ستختا
570 1113 وش فنردل سخ فهمیده سخن فهم را نیزگوبند
571 1114 سدوم یت گوبند صمخ درخت آن موی را
572 1115 تس رز برامن آن است کهیومرث را صد
573 1116 وا خلال آشدنر بلفت اهل مدینه غور خرما
574 1117 سراب نی مع بآید که آب از رود
575 1118 ۳۱۱ ات نناکوی نامرگی است که چون اورا
576 1119 سرافوج سارفكرر بر وزن در انداز مقنعه ضم
577 1120 ۱۱۱ ونهشت را نیزگوبند ات حضممزه سر او
578 1121 کوبند هرچیز لرمی را نیز گفته اند که
579 1122 ۱۱۷ سرپوش است اعم از سرانداز موقتعة زان
580 1123 ۱۱۱ سرلیژ واف رسی سرچکادی بفاجایم مهود بزرکهو
581 1124 نف از استخوان سازند ویدان بدترا خارند ینم
582 1125 اف سرخزه سرخژه بزاای سر لیگ نوعی از
583 1126 سرد کردن آهده است حمیرا کویند کنابه از
584 1127 مردابه زودآورند زود سازند آنچه در دست سردا
585 1128 ٩۷۷۴ زلد گی تری زای هوز کنابه از
586 1129 ۷۱ ات که بجمد جهنده باشد نام درختی
587 1130 ۷۱۲ است وآنرادای ترکی نیز خواند؛ ویکسر لول
588 1131 ۷۱۷ ۷۹ سرزش کردن طعنه زدن را یز
589 1132 سکه فروختن ات فایق باشد بمعنی ضابط گرری
590 1133 اس فرشکاهلی کفته اند مطلقاً سر که فشانی
591 1134 هه سر مو تثه دبا تای قر شت
592 1135 ۳۱ ات لبلابرا نیزکوبند وآن حطی حم آمده
593 1136 سروچ ګوبند که راست رود وآن را ياين
594 1137 ۳۱۱ فاون وسر خای سرو خشت فتح اول
595 1138 لس روش کال سال شممی بنام ابدان موسوم
596 1139 ۱۳ سروشه مصالع آن رو بدو مقرر است
597 1140 صری ۳۱ سر هنګ رک بروزن فرهنگه ؛سردار
598 1141 ۱۳۹ هآممده است نام ولابتی وجایی بیز هت
599 1142 پا احد شنجرف سوخته است بعنی شنجرف عملی
600 1143 ۱۱۳ آمد وسزاوار گردید هم هت سزا باشد
601 1144 ۱۳۹ مخفف اصطرلاب است وآن آلتی باشد از
602 1145 اه حواشی بقبه از صفحٌ ۹۳۱۱ سمترب از
603 1146 الفبای سفدی برابر صفحه ۱۱ جر رد کے
604 1147 کے په ما الفبای سغدى متأخر نقل از
```


## [2026-09-06T15:42:39.927Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (569,570,599,600):\n    print('===== leaf',i,'(printed ~',i+537,') =====')\n    print(leaves[i][:3000])\nEOF"
}
```


### [2026-09-06T15:42:44.883Z] TOOL RESULT

```
===== leaf 569 (printed ~ 1106 ) =====
                                                                                                            ‫‪¬ ۱‬‬      ‫وه‬




 ‫سج = بکر اول و فتح ثانی‌وسکون‬                                         ‫ستختا له = بروزن متاه سکن مخت‬
‫جیم ‪ .‬علتی باشدکه آارا تنگی شضس کوبند؛ وبا‬                                                         ‫و درشت رگاوند ‪.‬‬
                      ‫جیم فارسی همآ مده است‪.‬‬                           ‫سخت بازو ‏ با بای ابجد بالف‬
 ‫سره ‪ - ۲‬سم اول بروزن‌مهره»بممنی‬                                                   ‫کشیده و زای هوز بواو رسیده ک‬
                                                                       ‫‪۰‬نابه از مردم‬
‫بیگار است که کار بیمزدکردن باشد‪ -‬وبمعنی‬                                     ‫قوی هیکل و توانا وصاحب حمایت باشد‪.‬‬
 ‫در عربی‬   ‫و‬    ‫‪۰‬‬   ‫است‬    ‫هم آمده‬              ‫زیون و زیر دست‬
                                                                              ‫سخت لگام ‪ -‬بکر لامکا‬
                                                                       ‫وف‌فارسی‬
                     ‫باشد‪.‬‬           ‫هیزا‬
                                        ‫تک‬‫سسضر‬
                                             ‫ام‬‫وعنی‬
                                                  ‫بم‬                  ‫بالف کشیده و بمیم زده » اسب سر کن وا کویند‬

 ‫‪ -‬بفتح اول بروزن رخش‪ ,‬کهنه‬                          ‫سخحش‬              ‫‪ -‬وکنابه از مردم گرددکش باشد بعنی کانیکه‬
‫پرستین و کهنه جامه وکپنه کلاء و امثال ابنها‬                                                  ‫سر باطاعت فرو نباورند‪3.‬‬

‫را کویند ؛ و باين معنی باشین نقطه دار هم‬                               ‫پر کو »‬    ‫‪ - ۱‬ضم اول بر وزن‬        ‫سختو‬
                               ‫آهده است ‪.‬‬
                                                                      ‫رود کوسفند را کویند کهآدرا با گوشت وبراج‬
‫سخالات ‪ - ۴‬بفتح اول و سکون آخر‬                                         ‫و مصالح بر کرده بر روغن بربان کرده باشند ‪-‬‬
‫اسمن را‬‫که فوفانی باشد بروزن اخلاط ‪ ۰‬بکل‬                                  ‫کونایه ازآلت تناسل هم هت که قضب‌باشد‪.‬‬
               ‫کوبند که باسمن سفید و کبود باشد‪.‬‬                        ‫سخته ‪ - ۲‬بفتح اول بروزن اخته‪,‬بمعنی‬
 ‫انی » ممروف‬         ‫و‬    ‫= بنم اول‬              ‫‪°‬‬   ‫سین‬               ‫سنجیده و بوزن درآمده و وکزرنده‌باشد؛ رصم‬
 ‫اول و فتح‌ثالی‬            ‫؛‬
                           ‫م‬ ‫وند‬
                               ‫عروبی کلام کوب‬
                                            ‫ابست‬                                                   ‫اول کهفمته‌اند ‪۶#.‬‬
‫و بفتحاول و ضم ابلفیتوح اول ثوالی هم‬                                  ‫سخحتی د بو ار ذهر ‪ -‬کنایه از‬
                                                     ‫| آمفه آنت‪:.:‬‬
                                                                       ‫آفتاب عالمتاب است کونابه ازحوادث روز کار‬
‫جور » بکر‪ .‬نون و فتح جیم‬                                ‫سخ‬                                                     ‫‪.‬‬    ‫هم 
===== leaf 570 (printed ~ 1107 ) =====
    ‫==‬                                                                            ‫وش‬
                                                                                   ‫فنردل‬
                                                                                       ‫سخ‬
           ‫فهمیده و سخن فهم را نیزگوبند ‪.‬‬      ‫و سکون واو و رای قرشت » کنابه از سخن بی‬
‫سخن سنگ د بک ثالث » کنابه از‬                                         ‫باشد ‪.‬‬    ‫لطات و دل شکن‬

         ‫رشان آمد ‪.‬‬
                  ‫کگو‬
                    ‫مخنی است که بر‬             ‫سحن دل‌قر وش د کنابه از سخن‬
‫ح اول و خم ثالی و واو‬  ‫فنت=‬ ‫بجو‬‫س‬                  ‫وز‬
                                                   ‫رخن‬
                                                     ‫وس‬‫دشدل‪-‬ف‬
                                                            ‫یح و موعظه با‬
                                                                        ‫صباو‬
                                                                           ‫خو‬
‫ونون هردو ساکن ؛ بمعنی سخن است که کلام‬         ‫عم بنظر آمده است که بجای شین قطه‌دار زای‬
                                  ‫باشد ‏‪. ١‬‬                                ‫شطمرار باشد ‪.‬‬

‫سیر " ه بر وزن قفیر » دوایی است‬                ‫سحن زههر بر = کنابه ازسخن بی‬
                                                                    ‫وفرده باشد‪.‬‬      ‫هزه و نك‬
‫قلخ » طبیعتش گرم و خشك است و حفوی معدم‬
               ‫هم هست وسدهء جگر بگشاید‪.‬‬         ‫سنن زن ‪ -‬بفتح زایقطه‌دار وسکون‬
‫ستخینوس = بنتح اول و انیبتحتالی‬                ‫نکوننا»به از شاعر و قصه خوان و سخن کذار‬
‫رسیده و نون بواو کشیده و بین بی‌قطةٌ زده »‬     ‫باشد ‪ -‬و کنایه از مردم افتراکننده و سشن فهم‬
 ‫بلغت یونالی ‪ ۴‬کیاهی‌است که براخلال‌مامونی‬
 ‫کوبند و بعربی اذخرخوانند ‪ -‬وبمعتی مسطکی‬        ‫سهتی سنج ‪ -‬بمعنی سخن زن است‬
                        ‫هم بنظر آمده است‪. .‬‬       ‫مدر‪-‬دوم‬
                                                        ‫کنهابه از شاعر و فصه خوان باش‬




                                                ‫‪ #‬ست] = بفتح اول و ثانی‌بالف کشیده»‬
                       ‫و قدرت و توانایی حم‬      ‫وثب وحمام و امثال‬
                                                                ‫کوه ک‬        ‫آوازیرا کونند که در‬
                                                              ‫آن پیچد و معرب‌آن صداست ‪. ۴‬‬
                       ‫بعربی فدجن ‪٩‬‏ بروزن‬      ‫»یاهی‬
                                                    ‫سداب = بس اول بروزنکلاب گ‬
                             ‫الکن خوانند ‪.‬‬      ‫باشد دوابی مانند پودنه ® ‪.‬خوردن‌آن دفع‌قوت‬
                                                ‫زان‬     ‫حمل‬   ‫مردان و اسقاط‬       ‫باه و مباشرت‬


          ‫رطل پرکن مگوی بیش سخون ‪.‬‬                     ‫‪- ۱‬بودلی بود می بیار اکنون‬
  ‫رود کی سمرقندی ‪.‬رود کی ‪ .‬اقیسیص ‪۷۶۱۱٩‬‏ ‪.‬‬

                 ‫‪ - ۴‬لکلرك کید ‪ :‬مااین ماده را نمی شناسیم ‪« .‬لك اص ‪۸۳۲٩‬‏ ‪.‬‬
 ‫‪-‬سدا باسین مپمله باين معنی در‬
                             ‫‪« ۴‬‬         
===== leaf 599 (printed ~ 1136 ) =====
                                                                                          ‫پا احد‬

‫شنجرف سوخته است » بعنی شنجرف عملی‬                    ‫بخورند وبعد‬       ‫مات‬
                                                                         ‫منداوب‬
                                                                              ‫سبزی وتاز کی بیز‬
 ‫که آنرا اسزیماب سازند نآهنکه اکزان‬                 ‫کفش‪-‬‬     ‫سازند و‬   ‫کنند وآرد‬    ‫از رسد کی خشك‬


                                      ‫برآ ورند ‪.‬‬     ‫چبانند ‪٩‬‏ ‪-‬‬       ‫ان‬
                                                                        ‫بزدها‬
                                                                            ‫چی‬        ‫فان‬
                                                                                        ‫حناو‬
                                                                                           ‫کصرا‬

   ‫لی‬
    ‫االی‬
       ‫تر ث‬
          ‫حلوک‬
             ‫تاو‬
               ‫ونم‬
                 ‫سرلن ‪- ۴‬ب‬                                                                    ‫‪.‬‬    ‫جلد‬
 ‫ولون ساکن » شتگاه آدمی‪ -‬و کفل وساغری‬
                                                    ‫سر لع ه بفتح اول و کر انی وسکون‬                  ‫‪۰‬‬
                      ‫حیوانات دنکر ‪ ۴‬ك‬
                                                     ‫تحتانی ر غین اقطه‌دار ‪ ۰‬خوشه انگور بردأله‌باشد»‬

  ‫سر یانفکندن کدنایه اززاچانرو‬                           ‫بند خوش انگوری باهشدنکوهز‬
                                                                                 ‫وضی‬
                                                                                   ‫کبع‬
                                                                                     ‫و‬
                           ‫شتن باشد ‪.‬‬     ‫مرب‬
                                            ‫و‬                            ‫‪.‬‬   ‫درست لشده بادث‬       ‫دالهاش‬

‫سر بنگاه = بمنی مطلق شتگاه باشد‬                     ‫سر یقون ‪ « ۲‬بفتح اول و ضم قاف‬
  ‫عموماً ‪ -‬وبمعنی تخت بادشاحان پود خصوصاً ‪.‬‬          ‫وسکون واو و لون » لغتی است سربالی وبمعنی‬


                                              ‫بيان دهم‬

 ‫سز گی پ=قتح اول و سکون‌انی وکاف‬                    ‫سز ا * ‪ .-‬بفتح اول بروزن جزا ء پاداش‬
 ‫سختی ورلج‬         ‫نی‬
                    ‫مهع»‬ ‫فارسی بتحتانی رس‬
                       ‫بید‬                          ‫را‬     ‫فق‬
                                                            ‫وارا و‬
                                                                 ‫مزاو‬
                                                                    ‫لا‪-‬یق وس‬
                                                                           ‫وشد‬
                                                                             ‫نیکی و بدی با‬
                                   ‫وآزار باشد ‪.‬‬                                        ‫لىز گونند ‪۴#.‬‬

‫سز بتونتن ‪ - ۷‬بافوقانی و دونوتای‬                        
===== leaf 600 (printed ~ 1137 ) =====
 ‫‪۱۱۳‬‬
             ‫آمد وسزاوار گردید هم هت ‪4.‬‬         ‫سزا باشد‬          ‫دن*بیزمعنی‬
                                                                           ‫بوز‬
                                                                             ‫سز بل ‪ = ۱‬بر‬

                                                ‫کمعهافات بدی و لیکی ابستم‪-‬عونی لابق‬

                                         ‫داهم‬
                                            ‫بیان ب‬

          ‫درسین بی‌نقطه با سین بی‌نقطه مشتمل برسه لغت کونایت‬
‫کوبند ‪ ۴‬و برکه درخت آن بکرفس مانند‬              ‫‪ ۶‬سست مهار » نم اول و سکون‬
      ‫‪ -‬و رام شدن‌ومطيم | امت وآنرابشیرازی آهو دوستك خوانند‪.‬‬                ‫یم‬
                                                                             ‫طو‬‫کینا»به از رمام‬
                                                                                             ‫ا‬
‫سمعند (‪ = )4‬بفتح عين بی‌لقطه پروزن‬               ‫بودن‪ -‬ومردم‌بی‌استمداد ناقابلرا نکیوزیند ‪*.‬‬
‫سسطیعون (‪ = )۱‬بفتح اول وکرطای | پس‌بند ‪,‬بلفت سربانی عود بلانراکوبند‪ .‬وآن‬
‫وعی ازعود است » وعرق‌النا ر صرع و تاریکی‬         ‫(‪ )۳‬بروزن‌افربدون»‬        ‫حملی )<( وضم عبن بشیطه‬
              ‫بلغت سربانی تخمی است دوابی وآنرا زوفرایز | چشم وضیو‌النفی را نافع است‪.‬‬

                                      ‫يبان دوازدهم‬


                ‫درسین بی‌ناطه با طای‌حطی مشتمل برهشت لفغت‬
                    ‫‪. ۴‬‬    ‫امزد‬
                              ‫یهنازدشک‬
                                     ‫سطا خینس » بنتح اول و الی بالف | وببچ‬
 ‫سطار بون = بفتحارلبروزن‌حواربون»‬                ‫کشیده و خای لقطه‌دار (‪ )۵‬بتحتانی رسیدمونون‬
‫مضموم بین بی نقطة زده » بلفت بونانی رستنیی | بلغت مونانی گیاهی‌است که آرا بفارسی برابران‬
‫رنبد‌نافع باشد‪.‬‬
              ‫عرقگز‬
                  ‫‌‌ب‬
                    ‫یآن‬
                      ‫گاد‬
                        ‫باشد مانند کندنای کوحی ‪ .‬بول وحیض را براند |)ک‪(٩‬و‏بند‪ ۴.‬ضم‬

  ‫(‪)۳‬چك‪-:‬بی نقطه‪.‬‬           ‫)<( جك ‪ :‬و کرطا ‪6‬‬          ‫)‪ 0‬خما ‪ .‬چش ‪ :‬سطیمون(‪.)۱‬‬

             ‫(‪ )۰‬چش ‪ :‬بربران‪.‬‬            ‫(ه) چك ‪ :‬وخا ‪.‬‬                 ‫(‪ )4‬چش ‪ :‬عبد ‪.‬‬

            ‫(انگلیسی ) ی انتیتگاس» ‪۲‬‬     ‫‪esina‬‏ ‪dliw‬‬      ‫‪-‬‬       ‫‪۴‬‬        ‫رك ‪ :‬سر ندن ‪.‬‬   ‫‪۱‬‬

  ‫‪breh ۲0۷۵۵۲ = ۴‬‏ ‪ ( eht‬انگلیسی) «اشتینگاس*‪.‬‬                         ‫_ك ‪:‬تحفۀحكېممۋەن‪.‬‬
                                                                                      ‫‪ ۴‬ر‬
   ‫زی بکر اول) ‪ ۰‬پهلوى ‪02‬ا‪1»25‬‬
                             ‫کر‬‫٭ سردن _ لبغفةتح اول وچهارم د(رلہجة م‬
            ‫‪.‬ازند ‪ ) 0601225 , 08225‬رك ‪ :‬اسشق ‪ ۸۳۷‬؛ از سائىكرت‬‫ف(مل آن ‪ 18025‬پ‬
           ‫؛استه بودن» لابق بودن » سزاوار بودن ‪.‬‬
                                               ‫‏‪ « Skt‬ببرگ ‪-٥48: ۸۹۱‬‏ » ش‬
  ‫‪ #‬ست ‪ -‬منم ارل » پهلوی ‪5‬لا (ملایم » سبك) ؛ نرم و ملامم ‪ -‬نازك ‪ -‬ناتوان »‬
            ‫ضعیف » کم زور ‪ -‬آهسته ‪ -‬تثبل‪,‬کاهل ‪ -‬مانده ‪ -‬بی‌معنی » بیهوده ؛ ضد ‪ :‬سخت ‪.‬‬
```


## [2026-09-06T15:42:58.866Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nl=leaves[568]\nimport re\ni=l.find('پهلوی')\nprint('leaf 568 (printed ~1105) tail:')\nprint(l[-1800:])\nEOF"
}
```


## [2026-09-06T15:43:00.127Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\necho \"=== etymonline hatch ===\"; grep -n -i -E \"hatch|Old English|hacchen|hecken|PIE\" data/verification/sources/web/e470506379c9db62.txt | head -20"
}
```


### [2026-09-06T15:43:00.923Z] TOOL RESULT

```
leaf 568 (printed ~1105) tail:
               ‫خوب وني‬
‫و درشت و تنگه و دشواررا نیز گونند ‪-‬ویمعنی‬        ‫اول بمعنی شوخ است که چرك بدن وجامه باشد‬
 ‫محکم هم هت که لقیض نرم و ست امت ‪-‬‬                                     ‫وبعربی ومخ گونند ‪٩‬‏ ‪.‬‬
‫و ماضی کشیدن و وزن کردن وستجیدن باشد ‪۷‬‬           ‫ستخحاخ ‪ -‬بفتح اول و انیبالف کشید»‬
‫یمنی کشید و وزن کرد ء سنجید ؛ و باين ععنی‬           ‫یاند‪.‬‬
                                                        ‫ور‬‫زده» زمین نگرم‬    ‫(طه‪)۳‬‬
                                                                                ‫رنق‬
                                                                                  ‫اای‬
                                                                                    ‫دبخ‬
                                                                                      ‫و‬
                      ‫سحت ‏‪ = ٩‬بفتح اول بروزن لخت‪,‬بمعنی | جضم اول هم آمده است‪.‬‬

      ‫ن‪:‬ده‪.‬‬
          ‫چ)بچش‬
              ‫(‪ )۳‬چك ‪ :‬وبخا ‪4( .‬‬               ‫جحا‪.‬‬
                                                  ‫(‪ )۱‬چك‪ :‬وفتح ب ‪.‬ا (؟و)ف چتك‪:‬‬
                 ‫‪ ۴‬م‪-‬توفی ‪ ۲6۹‬قمری ‪-‬‬              ‫‪ ۱‬متمدی آن «سجاندن» (ه‪.‬م‪.).‬‬
   ‫هندی‌یاستان‬   ‫‪۹‬‬   ‫‪_ 9:‬ظ‪ .‬مصحف «وسخ» (عر)‪.‬‬        ‫‪ ۴‬رك‪:‬سيغ‬       ‫(ه‪.‬م‪).‬‬   ‫شحرور‬
                                                                                ‫‪= ۴‬‬

  ‫رهٌ ‪_k4¢‬‏ ‪( 1460626 .‬تواستن»فدرت داشتن)»ساد کربت ‪4‬ا‪( 4‬نوانا) ‏ بهلوی ‪. 625‬‬
      ‫‪.‬‬‫‪5‬کی‪8‬بز‬
            ‫×گیل‬‫ا‪»۳‬‬
                  ‫بلوچی ‪( 128‬سخت ‪ ۰‬محکم » استوار) »بودغا )‪« 60۱5‬اسشق ه‪-‬وبشمان ‪۲۷‬‬
                                         ‫‪ - ۲‬سوم شخص مفرد ماضی «سختن» (ه‪.‬م‪).‬‬
                                        ‫‪ -‬رك ‪ :‬لفات متغفرفة پایان کتاب و‬    ‫٭ مك‬
```


### [2026-09-06T15:43:01.016Z] TOOL RESULT

```
=== etymonline hatch ===
1:URL: https://www.etymonline.com/word/hatch
4:TITLE: Hatch - Etymology, Origin & Meaning
6:Hatch - Etymology, Origin & Meaning 
21: Origin and history of hatch 
23: hatch (v.1) 
25: early 13c., hachen , "to produce young from eggs by incubation," probably from an unrecorded Old English *hæccan , of unknown origin, related to Middle High German, German hecken "to mate" (used of birds). Meaning "to come forth from an egg," also "cause to come forth from an egg" are late 14c. Figurative use (of plots, etc.) is from early 14c. Related: Hatched ; hatching .
28: hatch (n.1) 
30: "opening, grated gate, half-door," Old English hæc (genitive hæcce ) "fence, grating, gate," from Proto-Germanic *hak- (source also of Middle High German heck, Dutch hek "fence, gate"), a word of uncertain origin. This apparently is the source of many of the Hatcher surnames; "one who lives near a gate." Sense of "opening in a ship's deck" is first recorded mid-13c. Drinking phrase down the hatch attested by 1931 (the image is nautical).
32: hatch (v.2) 
34: "engrave, draw fine parallel lines," late 14c., from Old French hachier "chop up, hack" (14c.), from hache "ax" (see hatchet ). Related: Hatched ; hatching . The noun meaning "an engraved line or stroke" is from 1650s.
37: hatch (n.2) 
39: "that which has hatched; action of hatching," 1620s, from hatch (v.1).
42: hatch (n.3) 
44: "engraved lines or strokes," 1650s, from hatch (v.2).
47: Entries linking to hatch 
49: hatchet (n.) 
51: c. 1300 (mid-12c. in surnames), "small axe with a short handle," designed to be used by one hand, from Old French hachete "small combat-axe, hatchet," diminutive of hache "axe, battle-axe, pickaxe," possibly from Frankish *happja or some other Germanic source, from Proto-Germanic *hapjo- (source also of Old High German happa "sickle, scythe").
53: This is perhaps from PIE root *kop- "to beat, strike" (source also of Greek kopis "knife," koptein "to strike, smite," komma "piece cut off;" Lithuanian kaplys "hatchet," kapti, kapiu "to hew, fell;" Old Church Slavonic skopiti "castrate," Russian kopat' "to hack, hew, dig;" Albanian kep "to hew").
55: Hatchet-face in reference to one with sharp and prominent features is from 1650s. In Middle English, hatch itself was used in a sense "battle-axe." In 14c., hang up (one's) hatchet meant "stop what one is doing." Phrase bury the hatchet "lay aside instruments of war, forget injuries and make peace" (1754) is from a Native American custom to conclude a peace-making, is described from 1680 ( bury a tomahawk is by 1705). Hatchet-man was originally California slang for "hired Chinese assassin" (1880), later extended figuratively to journalists who attacked the reputation of a public figure (1944).
59: 1650s, "to hack, chop into small pieces," from French hacher "chop up" (14c.), from Old French hache "ax" (see hatchet ). Hash browns (1926) is short for hashed browned potatoes (1886), with the -ed omitted, as in mash potatoes . The hash marks on a football field were so called by 1954, from their similarity to hash marks , armed forces slang for "service stripes on the sleeve of a military uniform" (1909), which supposedly were called that because they mark the number of years one has had free food (that is, hash (n.1)) from the Army; but perhaps there is a connection with the noun form of hatch (v.2).
```


## [2026-09-06T15:43:23.680Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\necho \"=== wikt سخت ===\"; grep -n -i -E \"Middle Persian|Proto-Iranian|Proto-Indo|Sanskrit|Etymology\" data/verification/sources/web/af4dc33181777c3c.txt | sed -n '1,25p'\necho; echo \"=== wikt ساختن ===\"; grep -n -i -E \"Middle Persian|Proto-Iranian|Proto-Indo|Sanskrit|Avestan\" data/verification/sources/web/04e0b6eb363f0b5c.txt | head -15\necho; echo \"=== wikt Sikh ===\"; grep -n -i -E \"Sanskrit|Punjabi|disciple|śikṣ|shishya\" data/verification/sources/web/519c2c1289f4bdac.txt | head -15"
}
```


### [2026-09-06T15:43:23.749Z] TOOL RESULT

```
=== wikt سخت ===
62: Etymology 
73: Etymology 
99: Etymology 
185: Etymology
204: Etymology
207: From Middle Persian 𐭮𐭠𐭤𐭨 ( saxt ) , 𐭮𐭤𐭨 ( saxt ) .
209: This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . 
210:Particularly: “A few online opinions suggest that this ultimately derives from Proto-Indo-European *ḱek- ( “ to be able ” ) ; [ 1 ] [ 2 ] see Sanskrit शक् ( śak ) for more. Is there any literature which could verify this?”
347: Etymology
350: Borrowed from Classical Persian سخت ( saxt ) , from Middle Persian 𐭮𐭠𐭤𐭨 ( saxt ) , 𐭮𐭤𐭨 ( saxt ) .
378: Persian terms inherited from Middle Persian 
379: Persian terms derived from Middle Persian 
380: Persian terms inherited from Proto-Indo-European 
381: Persian terms derived from Proto-Indo-European 
390: Urdu terms derived from Middle Persian 
399: Middle Persian terms with non-redundant manual transliterations 

=== wikt ساختن ===
157: Proto-Indo-European *ḱek- der. 
158: Proto-Iranian *cāčáyati 
161: From Middle Persian s’htn' ( sāxtan , “ to build, make ” ) , from Proto-Iranian *cāčáyati ( “ to prepare, build ” ) . [ 1 ] Cognate with Sanskrit शक् ( śak , “ to be able, capable ” ) ; see there for more cognates.
648: Categories : Persian terms inherited from Proto-Iranian 
649: Persian terms derived from the Proto-Indo-European root *ḱek- 
650: Persian terms derived from Proto-Iranian 
651: Persian terms derived from Proto-Indo-European 
652: Persian terms inherited from Middle Persian 
653: Persian terms derived from Middle Persian 

=== wikt Sikh ===
181: Borrowed from Punjabi ਸਿੱਖ ( sikkha ) .
304: Punjabi: ਸਿੱਖ   (pa) ( sikkha ) 
381: Categories : English terms borrowed from Punjabi 
382: English terms derived from Punjabi 
427: Terms with Punjabi translations
```


## [2026-09-06T15:43:35.166Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A8%B8%E0%A8%BF%E0%A9%B1%E0%A8%96' --note 'page 234, root Kak 1: Punjabi sikkh, source of English Sikh' 2>&1|tail -2\npython3 tools/fetch_source.py 'https://www.ahdictionary.com/word/search.html?q=Sikh' --note 'page 234, root Kak 1: AHD entry for Sikh (Nourai cites AHD:1205)' 2>&1|tail -2\npython3 tools/fetch_source.py 'https://www.ahdictionary.com/word/search.html?q=hatch' --note 'page 234, root Kak 1: AHD entry for hatch (Nourai cites AHD:603)' 2>&1|tail -2"
}
```


## [2026-09-06T15:43:37.750Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS leaf of line 7224 ===\"\npython3 - <<'EOF'\ntxt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nn=0\nfor l in txt[:7225]: n+=l.count('\\f')\nprint('leaf',n+1)\nEOF\ngrep -n \"pdf page\" SNS_pages.txt | head -2\necho \"=== MON ساختن/سخت ===\"; grep -n \"پهلوی.*saxt\\|sāxtan\\|ساختن\\.\" MON_part2.txt | head -5"
}
```


### [2026-09-06T15:43:39.023Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/80729cf17d93d7a8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/769a536b1243e5b5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9dda05e3915e213a.txt
```


### [2026-09-06T15:43:41.027Z] TOOL RESULT

```
=== SNS leaf of line 7224 ===
leaf 103
=== MON ساختن/سخت ===
593:افسرده کردن کسی را آزرده ساختن. 
3302:به کر به آوردن» گریان ساختن. (مسص‌ل.) 
5668:افراحتن» بالا بردن. مشتعل ساختن. 
7066:نیکو خصلت ساختن. دانش آموختن» تعلیم 
7317:آن). ویران ساختن. (فد.) تعلق گرفتن روح
```


## [2026-09-06T15:43:44.972Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\necho \"=== AHD Sikh ===\"; grep -n -i -E \"Sikh|Sanskrit|disciple\" data/verification/sources/web/769a536b1243e5b5.txt | head -10\necho \"=== AHD hatch ===\"; grep -n -i -E \"hatch|Middle English|Old English\" data/verification/sources/web/9dda05e3915e213a.txt | head -12\necho \"=== Punjabi sikkh ===\"; grep -n -i -E \"Sanskrit|Etymology|disciple|śikṣ|शिष्य|शिक्ष\" data/verification/sources/web/80729cf17d93d7a8.txt | head -10"
}
```


### [2026-09-06T15:43:45.052Z] TOOL RESULT

```
=== AHD Sikh ===
1:URL: https://www.ahdictionary.com/word/search.html?q=Sikh
4:TITLE: American Heritage Dictionary Entry: Sikh
6:American Heritage Dictionary Entry: Sikh 
41: Sikh (s ē k; s ĭ k) 
46: n. An adherent of Sikhism.
48: adj. Of or relating to the Sikhs or to Sikhism.
50: [Hindi, from Sanskrit ś i ṣ ya ḥ , disciple, from ś ik ṣ ati , he wishes to learn, desiderative of ś aknoti , is able.]
=== AHD hatch ===
1:URL: https://www.ahdictionary.com/word/search.html?q=hatch
4:TITLE: American Heritage Dictionary Entry: hatch
6:American Heritage Dictionary Entry: hatch 
41: hatch  1 (h ă ch) 
48: c. A hatchway.
50: 2. A door that opens upward on the rear of an automobile; a hatchback.
53: Idiom: down the hatch Slang Drink up. Often used as a toast.
55: [Middle English, small door, from Old English hæc, hæcc .]
59: hatch  2 (h ă ch) 
64: v. hatched , hatch·ing , hatch·es 
71: 3. To devise or originate, especially in secret: hatch an assassination plot. 
73: n. 1. a. The act or an instance of hatching from an egg or similar structure.
=== Punjabi sikkh ===
62: Etymology 
150: Etymology
153: Inherited from Prakrit 𑀲𑀺𑀓𑁆𑀔𑀸 ( sikkhā ) , from Sanskrit शिक्षा ( śikṣā , “ instruction , teaching ” ) . Ultimately from Proto-Indo-Iranian *ćikš- ( “ to learn ” ) .
165: ( Sikhism ) a Sikh ; disciple of Guru Nanak ; the Sikh community 
167: ( literally , now rare ) a student ; learner ; disciple 
276: Punjabi terms inherited from Sanskrit 
277: Punjabi terms derived from Sanskrit
```


## [2026-09-06T15:43:57.771Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nsed -n '59,100p' data/verification/sources/web/9dda05e3915e213a.txt"
}
```


### [2026-09-06T15:43:57.812Z] TOOL RESULT

```
 hatch  2 (h ă ch) 
 Share: 

 Tweet 

 v. hatched , hatch·ing , hatch·es 
 v. intr. 1. To emerge from an egg or other structure that surrounds and protects an embryo.
 2. To emerge from a cocoon or chrysalis.
 3. To emerge from the water when transforming from an aquatic larval or pupal form to a winged form, as a mayfly or caddisfly.

 v. tr. 1. To produce (young) from an egg or eggs.
 2. To cause (an egg or eggs) to produce young.
 3. To devise or originate, especially in secret: hatch an assassination plot. 

 n. 1. a. The act or an instance of hatching from an egg or similar structure.
 b. The act or an instance of emerging from a cocoon or chrysalis.
 c. The act or an instance of emerging from the water when transforming from an aquatic larval or pupal form to a winged form.

 2. a. A group of young organisms, especially birds, that hatch at one time; a brood.
 b. A group of adult insects that emerge at one time.
 c. A group of winged insects, as mayflies or caddisflies, that emerge at one time from a body of water.

 [Middle English hacchen , from Old English *hæccan .]
 hatch  er n. 

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 hatch  3 (h ă ch) 
 Share: 

 Tweet 

 tr.v. hatched , hatch·ing , hatch·es To shade by drawing or etching fine parallel or crossed lines on.

 n. A fine line used in hatching.

 [Middle English hachen , to engrave, carve, from Old French hacher, hachier , to crosshatch, cut up; see HASH 1 .]

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
```


## [2026-09-06T15:43:59.892Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 333-334 kak ===\"; grep -n -E \"vermögen, helfen|saknoti|çaknóti|k.ak-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10\necho \"=== IEC kak ===\"; grep -n -E \"^kak-|kaknumi|kakti|saknoti\" IEC.txt | head -10\necho \"=== SYN able/hard ===\"; grep -n -E \"saknoti|çaknoti|sakta\" SYN.txt | head -10"
}
```


### [2026-09-06T15:43:59.982Z] TOOL RESULT

```
=== WLD Bd1 333-334 kak ===
35451:krak-aran .,Herd, Feuerbecken, Glutpfanne''. • 
=== IEC kak ===
6639:kakið (or kokið ?) ‘hold, grip’. Cf. koks- (2) Srb. kočim, iti ‘check’; Latv. kaķēt ‘clamp, brace’; (isophonic w. Li. pa-kakti ‘suffice’, and Latv kacet ‘reach, get’, uncertainly to OS bi- hagōn, OFris. hagia, OE -hagian ‘suit’)
6648:kak- (1) (kaKios, à, is) “leather; thong, strap’. Cf. koK-. (Semit. LW?) Skt. kásah (2) ‘whip, thong"; kása ren": Arm. kaši “skin, leather”; Gk. cf. kasēs (“skin used as horse-cloth', said to be Ethiopian, cf. Aramaic kasah) beside kasía (‘cinnamon bark’, referred to Assyr. kasia, but uncertain)
6649:kak- (2) “hold? Arm. kasem, tr. ‘stop’; kasim, tr. ‘hold’; cf. kast ‘pincers’; Alb. cf. n-gath ‘Impede; be- numb’ beside sh-kath ‘loosen, limber up’; MHG cf. hegen ‘keep, save’; LG id.; OS cf. hagu-stald (‘servantť’, lit. 'retainer); ON cf. hogld, npl. hagldir ‘buckle, cleat, toggle’, hagi, m. ‘pasture, meadow’; OE haga ‘enclosure’. (The Gmc. forms are ambig.)
6650:kak- (3) (?) ‘withered, miserable, diminu- tive’. Cf. koK- Av. kasus ‘little’; Oss. cf. käs-tår ‘younger’; G hager, EME hagger (Clean" LW in Fr. hagard); R kósnyj ‘sluggish’; Li. cf. kašiù, éti, v. ‘wither, shrink’. (Alb. ngath ‘benumb’, fr. *en-kak- here, or to (2))
6651:kak- (4) ‘strike’ (Phonol. ambig.) Skt. ka$àmi “strike, kil; Arm. kasum, aor. kasi ‘thresh’; OCS cf. pri-kosno -noti “touch?
6655:kak- — kaldhos
=== SYN able/hard ===
24777:Sw. sakta ‘gentle, slow’ (in the latter sense esp. as adv.) = Dan. sagte ‘soft, gentle’, fr. MLG sdchte, altered form of safte : NE soft, NHG sanft, ete. Falk- Torp 944. Hellquist 880.
```


## [2026-09-06T15:44:09.969Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 pages: find kak vermögen ===\"; grep -n -E \"vermögen.{0,15}helfen|çaknóti|caknoti|sakti-.*Hilfe\" incoming/WLD/WLD_Bd1_pages.txt | head -10\necho \"=== IEC kek- / around 6655 ===\"; sed -n '6652,6660p' IEC.txt\necho \"=== IEC search 'be able' kek ===\"; grep -n -E \"^kek-|kekt|kakti\" IEC.txt | head"
}
```


### [2026-09-06T15:44:11.687Z] TOOL RESULT

```
=== WLD Bd1 pages: find kak vermögen ===
31655:stellt hagen hegel zu ai. caknoti „vermag", eakrd- „kraftig“, erwiigenswert.
=== IEC kek- / around 6655 ===
kakKiom (?) ‘milk curdled and strained, cot- tage cheese. Lat. caseus, caseum “cheese” beside It. caccio, id.; Alb. kos *yoghurt; Li. cf. kósiu, kósti ‘strain, filter’; Latv. kaSu, kāst, id.
kal- (1) (kalt-) ‘slope’. Cf. WP I, 430 and kalt- Skt. cf. katakah 'slope'; Go. wilja-halpei, f. ‘favour’; OHG hald, adj. ‘inclined’; G Halde ‘slope’; Du. cf. hellen, v. ‘tilt’; ON hella *de- cant’; R cf. po-kolét ‘die off”; Li. kaliuos, kal- tis ‘lean’; üZ-kaliu, -kalti ‘lean’; at-kaltis, f. “back of chair; LW in Finn. kaltto, kalteva ‘sloping’
kal- (2) ‘bright, white’. Cf. WP I, 429 Gk. kalós (‘bright, beautiful’. Despite Boeot. kalwós?); cf. kállos, n. ‘beauty’; (-a- in) kelás, gs -ádos ‘goat w. white blaze’; Lat. cf. calidus (or calidus) *white-blazed'; Latv. cf. kaleju, et ‘bleach’. (Link w. Lat. caleo, ere "be bot, and w. LG hellig ‘thirsty’ uncertain). Cf. kali-
kak- — kaldhos
20
25
30
35
40
=== IEC search 'be able' kek ===
6639:kakið (or kokið ?) ‘hold, grip’. Cf. koks- (2) Srb. kočim, iti ‘check’; Latv. kaķēt ‘clamp, brace’; (isophonic w. Li. pa-kakti ‘suffice’, and Latv kacet ‘reach, get’, uncertainly to OS bi- hagōn, OFris. hagia, OE -hagian ‘suit’)
15582:sképtis (1) “pole, rod, prop'. Cf. sképos. (Variant *skekti-?) Arm. ec gs: xeği, ab. s. xeğiv, s. 'vine-prop, oar; Gk. sképsis, f. (1) “prop, support; W (ambig.) ysgeth, pl. au. f. lance?
```


## [2026-09-06T15:44:17.812Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '31630,31665p' incoming/WLD/WLD_Bd1_pages.txt\necho \"=== page tag ===\"; awk 'NR<=31660 && /\\[pdf page/ {p=$0;n=NR} END{print n\": \"p}' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T15:44:19.563Z] TOOL RESULT

```
  Ags. hagan „genitalia", mhd. lutgen „Zuchtstier", nhd. mdartl. h<gd ds.,
haksch           ,
                     Zuchtsehwein", nhd. hecken „sich paaren (von Vogeln)", engl. hatch,
ahd. hegidraosa ..Hode"                             (nicht        besser dariiber Siitterlin, s. u. koksa: und
Bezz.            GGA. 1S9S, 555: wegen                            der „Hagedriise am Halse" vielleicht zu
lit.   saibaudys ds.;                       doch
                                        „Schorf" keine befriedigende Bed.-
                                                    liefert       sciias
A^ermittlung mit „Hode"); vielleicht dazu    lett. leukale „Hodensack, penis“;

dagegen russ.-ksl. kocam „membrum virile' ist in dieser Bed. nur einmal           1




belegt und (wie alb. hots ds., G. Meyer Alb. Wb. 203) Ubertragung aus der
sonstigen Bed. „Kohlstrunk u. dgl." des AVortes (vgl. dt. vulgar Stengel").                                               ,,

    r
   A gl. Kluge 8 u. Hecke 2 , Zupitza Gutt. 104, Bezzenberger GGA. 1898,
                                                                           r
555, Berneker 527.     Unsicher, und auch wegen des beschriinkten A er-
breitungsgebietes kaum als sehr alt zu betrachten. Schrader ZfdtAVtf. 1 238 f.                                                 ,


stellt hagen hegel zu ai. caknoti „vermag", eakrd- „kraftig“, erwiigenswert.
                        ,


Vgl. aber Miihlenbach-Endzelin Lett.-D. AVb. II 137, Buga K. ir s. I 192.

 kaq-        :   kaq-, wahrscheinlich ka[i]q- : klq- mit koq- als Ablautneubildung von
         kueq-         aus „springen, hervorsprudeln, kraftig sich tummeln ‘.                                     !



=== page tag ===
:
```


## [2026-09-06T15:44:31.792Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '31600,31632p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T15:44:31.855Z] TOOL RESULT

```
(^mit raf.idrom) ..Hilfe gewiihrend", Uig.nnan- n. ..Geschenk", lagvah- ..bietend.
gewiihrend" (Bartholomae Air. Wb. 576). die freilieh wiederuin in ihrem
e-Yokalismus nicht so unmittelbar zum germ, u u stimmen.                                        :




   Uber die von Bugge und Thurneysen mit hagr usw. verbundenen lat.
colnt-s, osk. kahad s. u. gagh- ..getlochtene Hiirde".

   Yanicek LEWb. 2 65, Fickl 4 41, 419. II 4 58 ir. odtl ..Kraft" bleibt fern ).
III 4 6S. Uhlb. Ai. "VYb. 301 (aber lit. Mtnk'mfi. dt. Hcngst s. u.                                              icily- ..springen-;.

Bgm. IF.          1   9. 385. Yf.        LE\Yb. 2 u. eanda. rohvs. Falk-Torp. u. hag. hgntlr. btfirc.
334                                                qak   — kaq-      :   kaq-, ka[i]q   :   klq


qak- ..abmagern".
  Av. Icasu- ..klein. gering", komp. Sup. kasyah-, kasista- (aber gr. y.ay.6 g,
Hiibschmann Yokalsyst. 154, eher zu *kakka- ..cacare",; lit. nukusHi „ganz
entkraftet werden", nhd. huger (Trautmaun ZfdtAVtf. 7, 267, KZ. 43, 153;
andere Deutungen von huger s. bei Yf. LEWb. 2 u. craccntes, Berneker 133,
der es zw. mit russ. cachnufa ..dahinsiechen, abmagern" aus *qcq-s- ver-
bindet, das aber dehnstufige Kebenform von -ceznutb „schwinden, ver-
sehwinden" sein wird, mit eh statt s nach sochnutb sychnutb ,,vertrockneu“).                 ,




kak- ..mannliche Geschlechtsteile"?
  Ags. hagan „genitalia", mhd. lutgen „Zuchtstier", nhd. mdartl. h<gd ds.,
haksch           ,
                     Zuchtsehwein", nhd. hecken „sich paaren (von Vogeln)", engl. hatch,
```


## [2026-09-06T15:44:34.562Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM كاغذ ===\"; grep -n \"كاغذ\\|الكاغذ\" AFM_pages.txt | head -5\necho \"=== TAD كاغذ ===\"; grep -n \"كاغذ\" TAD_pages.txt | head -5\necho \"=== ARB كاغذ ===\"; grep -n \"كاغذ\\|القرطاس\" ARB_mo3rb.txt | head -5\necho \"=== HRN kalpase/carpasa ===\"; grep -n -E \"kalpase|calpase|karbasu|kerbase|Eidechse\" HRN.txt HUB.txt | head -10"
}
```


### [2026-09-06T15:44:34.653Z] TOOL RESULT

```
=== AFM كاغذ ===
3473:( الكاغد) فارسي حض بعنى القرطاس . والكاغذ لغة فيه ومن الحكردي
=== TAD كاغذ ===
=== ARB كاغذ ===
19898:() هذاقول شاذء ل كه غير المؤلف فيا أظن ٠‏ و ”” القرطاس ©“ يكسر القّاف وضهها 6 لنتات 
=== HRN kalpase/carpasa ===
HRN.txt:9367:1082. vei^ey Frosch', arab. LW. vazayat 'Eidechsenart'.
```


## [2026-09-06T15:44:54.528Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 234 -l 234 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg234 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg234.png"
}
```


## [2026-09-06T15:44:55.682Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=3473 && /\\[pdf page/ {p=$0;n=NR} END{print n\": \"p}' AFM_pages.txt\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['AFM']\nprint(d.get('page_offset'))\""
}
```


### [2026-09-06T15:44:56.907Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 82071 Sep  6 11:44 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg234.png
```


### [2026-09-06T15:44:58.984Z] TOOL RESULT

```
: 
198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
```


## [2026-09-06T15:45:00.994Z] TOOL CALL #76: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg234.png"
}
```


### [2026-09-06T15:45:01.451Z] TOOL RESULT

```

```


## [2026-09-06T15:45:01.449Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:45:32.681Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T15:45:32.720Z] TOOL RESULT

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


## [2026-09-06T15:45:53.332Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT cag- ===\"; grep -n -E \"cagvah|cagman|cagdman|'cag|Geschenk'\" BRT.txt | head -8\necho \"=== BRT search 'cagəd' variants ===\"; grep -n -E \"cag[3ə]d|Hilfe  gew|gewährend\" BRT.txt | head -8\necho \"=== TTS ctx ===\"; sed -n '14294,14302p' incoming/TTS/TTS_pages.txt\necho \"=== HJB Sikh ===\"; grep -n -E \"^SIKH|Sikh,\" HJB.txt | head -5\necho \"=== SKT hatch2 ===\"; sed -n '8414,8422p' SKT.txt"
}
```


### [2026-09-06T15:45:53.454Z] TOOL RESULT

```
=== BRT cag- ===
11119:•  g-  öagflman-  n.  'Geschenk':  apu  . . ma^aifaislä  (sd.)  . .  uhsibya  ahubyä  'm3 ■'die  Wasser  . .,  das  Geschenk  für  beide Existenzen"  Y.^S.^.
25305:•  j.,  g.  rSti-  f.  'Gabe,  Geschenk':  aäiauruns
=== BRT search 'cagəd' variants ===
6366:Ganz  unsicher.  F  1 :  rava  iläyä  yoBdqia. Gdn.  in  der  NA.  vermutet;  ravä.AusaySdifiH, was  wohl 'Raum  und  gutes  Wohnen  gewährend' bedeuten  soll.
11112:•  g.   £ag9d-  Adj.   'bietend,  gewährend',
11121:•  g.  £agvah-  Adj.  'bietend,  gewährend': ä  Ti  avaenä  (sd.)  aAurS  rafihrim  'vä  (NS.) kyat  fryS  fryäi  (sd.)  daidü  Y.^ö'.a.
15975:•  j.  päSra'vant-  Adj.  (fem.  'vaitl-)  'Schutz, Schirm  gewährend':  gk^a  karfilravainUa 'vaitlsHa  Y.55.  a'.
17217:Eig.  *hahen  Nutzen  gewährend'.  —  Pu. :  hulaad
20616:•  g.  ''^myasträ.barana-"  Adj.  'societatem praebens  (cum—)':  mazdh7ä  ahuräaAe  s *mByasträ.baranä  (NPm.)'>  asäcä  hya^ ha%ra  (sd.)  .  .  "MAA.  und  ihr  andern Götter,  heran  (kommt)!  eure  Bundesge- nossenschaft gewährend ,  und  Asa,  auf dass  .  ."  Y..?o.  93'.
23000:Eig.  'wirksamen  Schulz  gewährend'.  —  ■>  Nach der  B-Dekl.
23551:land, -grund,  Wiese';  yascä  °rS  vJVäpaj (sd.)  Y._J2. 10;  —  yai^a  a^a  ga%wa  mit \  ma%ime  \yä\  're  [vä\  frajasäl  ",  ,  mitten auf  einer  Weide  .  ."  V.  ;5. 4i'>;  —  yj ^wal  . .  yaeäi  afiä  . .  giuscä  "rät  aRstgnt mantüm  (sd.)  Y.jj.  4;  —  at  hvS  a^ahyä anhat  vanhiuila  'ri  mananhn  "der  wird (dereinst)  auf  der  Weide  des  A.  und  des VM.'^  sein"  Y.jj.  3;  —  yj  ahmai  gqm . .  hSiiutalal  ai  hsi  'rät  rämä.dä  ärmaiton "der,. geschaffen  hat,  aber  zu  dessen  (des Rindes)Wetde-"dievfrM.(Erde),(ihm)Frie- den  gewährend"  Y.  47-  3-  3)  'Weide- wirtschaft', Uberh.  'Landwirtschaft':  rtifij urvähs  dätsibyascä  karapanS  'rät  arSm (sd.)  Y.5/,  14;  —  nSii  htm  masn(sd.)  aSil 'r3m  frädai^he  Y.  4^.  30;  —  hScä  nä fiümS  , .  aiwyilxsayatü  hadä  asäcä  'räcä Y.  sS-  4-         [N.  Sy,  F.  5:  lies  vasf.]
=== TTS ctx ===
      Bit, büt, büi, Laus, Wurm, Käfer (Ungeziefer).
cag.             = Laus (osm. tachta izYe= Wanze, d.h. Bretlaus;
         bit, ftü«
         koj Uti— Zecke, d. h. Schaf laus; hudaj Wi!» = Kornlaus)
         &M# = Wurm {kagas hütü = ^loiie, d. h. Papierwurm); büt-
         cek,       büdek, mü^ek — KMer.
osm. bit,           bö£ek (wie oben; so: sümnkli böhk            — Schnecke, d. h.
         geifriger Käfer; jildiz &öie^i =: Johanniskäfer,              d.   h.   Stern-
         käfer).
=== HJB Sikh ===
20166:SIKH,  SEIKH.
20187:SIKH,  SEIKH,  n.p.  Panjabi-Hind. Sikh,  *a  disciple,'  from  Skt.  Sishya; the  distinctive  name  of  the  disciples of  Nanak  Shah  who  in  the  16th century  established  that  sect,  which eventually  rose  to  warlike  predomin- ance in  the  Punjab,  and  from  which sprang  Ranjit  Singh,  the  founder  of tne  brief  Kingdom  of  Lahore.
20189:SIKH,  SEIKH.
=== SKT hatch2 ===
Hatoh  (0,  a  half-door.  (E.>  M.  E, AafcAe  ;  a  AaUA  also  meant  a  latch  of  a door.  North  £.  Ae^k,  A.  i>.  Aa^a,  bolt  or bar  of  a  door;  also  Aacee,  a  hook.+Du. AeA,  fence,  rail,  gate,  Swed.  Aiirk.  coop, rack,  Dan.  Aai,  hakke,  rnck.  Allied  to Hook.  The  ortg.  sense  was  prob.  a  latch or  a  catch  of  a  door ;  hence,  various  modes of  fastening.  Der.  hatchet,  pi.  sb.,  a frame  of  cross-bars  over  an  opening  in  a ship's  deck;  AaUh-itny.
hatch  (3).  to  produce  a  brood  by  incu- bation. (E.)  From  the  coop  or  ha/i A  in which  the  motherbird  sits.  Thus  Swed. Aiuka,  to  hatch,  from  hdck^  a  coop ;  Dan. AtxkkeOuur,  a  breeding-cage,  from  AakJke,  a rack.
Hatoh  (3\  to  shade  by  lines,  in  engrav- ing;  Hatchot,  axe  :  sec  Hook  (1).
Batches;  see  Hatoh  <i).
Hatchment,  cKutcbeon ;  seeGapital(i ).
Hate,  sb.  (£.)  M.  E.  hate,  A.  S.  Aete, bate ;  the  mod.  E.  sb.  takes  the  vowel from  the  verb  hat  tan.  to  hate.+Du.  Aaat, IccL  hatr,  Swed.  haf,  Dan.  AaJ,  Goth. AeUis,  G.  Aass,  hate.  Cf.  W.  cat,  hate, tatau,  to  hate.     (V  KAD.)
hatred.  (E.)  M.  E.  hairt<i,  AatrttUn. The  su^ix  is  A.  S.  -r<kden,  law,  mode,  con dition.  state,  as  in  Aiw-riktUn,  a  household  ; and  sec  kindred .
Hauberk,  a  coat  of  ringed  moil  (F. » O.  U.  G.)  M.  Z.Aaui^rh.^Q.  F.  hauhert. -O.  U.  G.  hahbetx,  liL  ncck-dclei<ce.  - O.  H.  G.  hals,  neck  :  Ur^nn,  to  protect Sec  CoUar  an<l  Bury.
habergeon,  ainiour  for  neck  and  breast. {?.  -  O.  H.  G.)    M.  £.  hu^r^an,  Aatiir-
```


## [2026-09-06T15:45:54.635Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON کاغذ ===\"; grep -n \"کاغذ\" MON_part2.txt | head -5\necho \"=== ARY کاغذ ===\"; grep -n \"کاغذ\\|کاغد\" incoming/ARY/ARY_pages.txt | head -8\necho \"=== ARY سخت/ساختن ===\"; grep -n \"ساختن\\b\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-06T15:45:54.723Z] TOOL RESULT

```
=== MON کاغذ ===
6296:(کد.) کاغذ. فرش صورتی: فرش و قالی 
6409:فرفره: (اص.) کاغذ پاره‌ای که بر سر 
6567:کاغذ که بطور افقی وعمودی کشیده شود. 
7476:باریک از کاغذ یا مقوا که در داخل آن 
9489:فیش: 115 (.) کاغذ با مقوایی که روی آن 
=== ARY کاغذ ===
=== ARY سخت/ساختن ===
380:در انجیل آمده است که مردم پابل (8۸881) آغاز به ساختن برجی کردند که قرار بود بلندی
383:از ساختن پرج دست بکشند. این داستان اخلاقی عواقب غرور را نشان می‌دهد ولی طی قرون متمادی
3226:این باشد که پل‌های اولیه را از تیرهای چوبی می‌ساختند. ۱ ید
5562:۲- چم اين واژه در زبان‌های یونانی و لاتین: درخت سرخدار (که از آن تیر وکمان می‌ساختند!)
5589:۰ چم این واژه در زبان‌های دیگر: با فنوری و هنرمندی ساختن (به ویژه از چرب).
```


## [2026-09-06T15:46:17.567Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,ln in [('incoming/TTS/TTS_pages.txt',14298),('AFM_pages.txt',3473),('BRT.txt',11112),('BRT.txt',9326),('SNS_pages.txt',7224)]:\n    txt=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    n=sum(l.count('\\f') for l in txt[:ln])\n    print(f, 'line',ln,'-> leaf', n+1)\nEOF"
}
```


## [2026-09-06T15:46:19.227Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%BA%D8%B0/",
 "prompt": "Quote the \"فرهنگ معین\" (Mo'in) section for کاغذ, including any bracketed origin tag such as [ترکی] or [چینی], and any Dehkhoda/Borhan etymological note about the word's origin."
}
```


### [2026-09-06T15:46:19.425Z] TOOL RESULT

```
incoming/TTS/TTS_pages.txt line 14298 -> leaf 235
AFM_pages.txt line 3473 -> leaf 138
BRT.txt line 11112 -> leaf 340
BRT.txt line 9326 -> leaf 277
SNS_pages.txt line 7224 -> leaf 103
```


### [2026-09-06T15:46:27.164Z] TOOL RESULT

```
# کاغذ Etymology - Mo'in Dictionary Entry

According to the **فرهنگ معین** (Mo'in Dictionary), the entry for کاغذ includes:

> "(غَ) [از چی.] (اِ.) ورقة نازک، خم پذیر و مسطحی که معمولاً از خمیر الیاف گیاهی ساخته می شود"

The origin tag indicates **[از چی]** (from Chinese), though the detailed etymology section in Dehkhoda's dictionary notes that despite Chinese origins, the word became established in Persian through historical transmission via trade routes and cultural contact.

The Dehkhoda section emphasizes that while the manufacturing technique originated in China, the Persian linguistic form developed independently as the technology spread westward through Islamic territories, particularly via Samarkand in the 2nd-3rd centuries of the Islamic calendar.
```


## [2026-09-06T15:46:43.518Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(repr(txt[102][:1200]))\nEOF"
}
```


### [2026-09-06T15:46:45.740Z] TOOL RESULT

```
'                                          »\n\n\n                        L^   ^U -b    \')\')_\n\n\n\n\n                j"I ;iJ           —           gsh5n:   ^\n c akta\n          L,   .o^-^V         *\n                                              lMpf# 160 )\n                                                            bl?\n\n                        .^./L-sB«t tar: >*~»                                                                                             .f a:           40   :   -O\n                .\n                                                                      (Jackson. 106) catvarisSt                :   L caflwar^sat-                    sbm\n\n\n                    ,        M    3\n                                      ^o>^=saxtag:J^\n                                                                                                                             >*iJC       .*-:            si :A3\n\n\n                        ^v^-w"-\n                             :E av S nd:\n                                         SGVTWN, nd =   ^:^                                      1/1Y*£   .*-!?*- :sig3nag:              S3K3**\n\n                                            i37)\n                              '
```


## [2026-09-06T15:46:46.220Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%BA%D8%B0/' --note 'page 234, root Kagas: Mo’in tag for کاغذ ([از چی.] = from Chinese)' 2>&1|tail -2\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg234.png data/verification/sources/refs/ocr/BOOK/234.png && echo copied"
}
```


### [2026-09-06T15:46:49.772Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8c5ece60f35b5fe6.txt
copied
```


## [2026-09-06T15:47:51.011Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\necho \"=== چلپاسه ===\"; grep -n -i -E \"Etymology|Middle Persian|Avestan|lizard|inherit\" data/verification/sources/web/c3e95691350635ac.txt | head -12\necho \"=== sogdian page ===\"; head -6 data/verification/sources/web/42eda0375e7d6cb7.txt"
}
```


### [2026-09-06T15:47:51.068Z] TOOL RESULT

```
=== چلپاسه ===
=== sogdian page ===
URL: https://en.wiktionary.org/wiki/%F0%BC%B8%F0%BC%B0%F0%BC%B2%F0%BC%B9%F0%BC%B0
FETCHED: 2026-09-06T15:38:49Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T15:47:56.410Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://archive.org/download/sinoiranicachin00laufgoog/sinoiranicachin00laufgoog_djvu.txt' --note 'page 234, root Kagas: Laufer Sino-Iranica pp.557-559 clean OCR (Turkic origin of kagad, rejection of Chinese ku-chih)' 2>&1|tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3%D9%88' --note 'page 234, root Kahrpu: Persian karbāsu \"lizard\"' 2>&1|tail -2"
}
```


### [2026-09-06T15:48:01.594Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ae58a5a9c978e40a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/23d669ae1239d619.txt
```


## [2026-09-06T15:48:04.188Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -8 data/verification/sources/web/23d669ae1239d619.txt; grep -n -i -E \"Avestan|lizard|Etymology\" data/verification/sources/web/23d669ae1239d619.txt | head"
}
```


### [2026-09-06T15:48:04.245Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3%D9%88
FETCHED: 2026-09-06T15:48:01Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T15:48:07.054Z] AGENT

Now I'll write the verification file.


## [2026-09-06T15:51:54.614Z] TOOL CALL #87: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build234.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nSIN_URL = \"https://archive.org/download/sinoiranicachin00laufgoog/sinoiranicachin00laufgoog_djvu.txt\"\n\ndata = {\n \"pdf_page\": 234,\n \"book_page\": 204,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ------------------------------------------------------------------ entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Kagaš, Kagat, Kagas, Kagaz\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"Turkic *kāġad / kāġaz 'paper' (Old Uyghur kagat/kagaš, Karakhanid kāġïd); the meaning 'tree bark' is attested only for Lebed/Kumandu/Sor kagaš, and modern scholarship derives the whole family from Sogdian kʾγδʾ (kāγaδā) 'paper', itself possibly from Old Chinese 紙\",\n \"note\": \"The root box reproduces Berthold Laufer's 1919 thesis verbatim: Sino-Iranica p.559 says 'the Persian-Arabic word is borrowed from a Turkish language: Uigur kagat or kagaš; Tuba, Lebed, Kumandu, Comanian kagat; Kirgiz, Karakirgiz, Tarančī, and Kazan kagaz. The origin of this word can be explained from Turkish; for in Lebed, Kumandu, and Sor, we have kagaš with the significance \\\"tree-bark\\\".' Nourai's four head-forms and his gloss 'tree bark' are Laufer's, so the citation SIN:559 is exact. The problem is that Laufer's account is no longer the standard one. Modern Iranian philology (B. Gharib, 'Sogdian language i. Loanwords in Persian', EIr; Wiktionary s.v. کاغذ, citing her) treats NP kāġaḏ/kāġaz as a loan from Sogdian kʾγδʾ /kāγaδā/ 'paper', a word of the Sogdian merchant colonies of Samarkand, itself perhaps ultimately Chinese; Mo'in's own dictionary tags کاغذ simply '[از چی.]' = 'from Chinese'. The Turkic forms are then either parallel loans from the same Sogdian source or (Ottoman kâğıd) later loans back from Persian. 'Turkish' is also the wrong language label for Laufer's evidence, which is Old Uyghur plus Altai-Siberian dialects (Lebed, Kumandu, Sor, Tuba), not Ottoman/modern Turkish. The 'tree bark' sense survives in only three small Altai dialects and is more plausibly a secondary specialisation of 'paper' (paper being made from bast) than its source.\",\n \"note_fa\": \"این جعبهٔ ریشه دقیقاً دیدگاه برتولد لاوفر در «سینو-ایرانیکا» (۱۹۱۹، ص ۵۵۹) است: لاوفر واژهٔ فارسی-عربی «کاغذ» را وام‌گرفته از زبانی ترکی می‌داند (اویغوری kagat/kagaš، تووا و لبد و کوماندو kagat، قرقیزی و قزانی kagaz) و اصل آن را واژهٔ kagaš در گویش‌های لبد و کوماندو و شور به معنای «پوست درخت» می‌شمارد؛ پس ارجاع نورایی به SIN:559 کاملاً درست است. اما پژوهش امروزی این نظر را نمی‌پذیرد: بدرالزمان قریب (در مقالهٔ «وام‌واژه‌های سغدی در فارسی»، ایرانیکا) و به پیروی او ویکی‌واژه، «کاغذ» فارسی را وام‌واژه‌ای سغدی از kʾγδʾ (kāγaδā) «کاغذ» می‌دانند که خود شاید از چینی باستان آمده باشد؛ معین نیز در فرهنگ خود ذیل «کاغذ» تنها نشانهٔ «[از چی.]» می‌گذارد. افزون بر این، برچسب «ترکی» نادرست است، زیرا شواهد لاوفر اویغوری کهن و گویش‌های ترکیِ آلتایی-سیبری‌اند نه ترکی عثمانی. معنای «پوست درخت» نیز تنها در سه گویش کوچک آلتایی دیده می‌شود و محتمل‌تر است که تحول ثانویِ «کاغذ» باشد تا خاستگاه آن. حکم: پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n \"sources\": [SIN_URL, W + \"%DA%A9%D8%A7%D8%BA%D8%B0\", W + \"k%C3%A2%C4%9F%C4%B1t\", \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%BA%D8%B0/\"],\n \"ref_check\": [\n   {\"ref\": \"SIN:559\", \"status\": \"supports\",\n    \"note\": \"Laufer, Sino-Iranica p.559 (archive.org sinoiranicachin00laufgoog_djvu.txt lines 20237-20240; local SIN.txt \\\\f-leaf 388 has the same page but badly damaged OCR): 'As stated, the Persian-Arabic word is borrowed from a Turkish language: Uigur kagat or kagaš; Tuba, Lebed, Kumandu, Comanian kagat; Kirgiz, Karakirgiz, Tarančī, and Kazan kagaz. The origin of this word can be explained from Turkish; for in Lebed, Kumandu, and Sor, we have kagaš with the significance \\\"tree-bark.\\\"' Exactly Nourai's four head-forms and his gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"TTS\", \"where\": \"Vámbéry 1878, TTS_pages.txt leaf 235 (printed p.~205), s.v. bit/büt\", \"stance\": \"partial\",\n    \"note\": \"'kagas bütü = …, d. h. Papierwurm' — Vámbéry knows Turkic kagas only in the meaning 'paper' (bookworm = 'paper-worm'), not 'tree bark'; he gives the word no separate etymological entry.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch 1927 (LKT.txt, grep k[aā]g[aă]d / kagat / Papier)\", \"stance\": \"silent\",\n    \"note\": \"Lokotsch has no entry for kāġad/kâğıt at all; his 'Papier' hits are pambak > russ. bumaga (no. 1617) and risma > Ries, unrelated.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in s.v. کاغذ via abadis.ir\", \"stance\": \"contradicts\",\n    \"note\": \"'(غَ) [از چی.] (اِ.) ورقهٔ نازک، خم‌پذیر و مسطحی که معمولاً از خمیر الیاف گیاهی ساخته می‌شود' — Mo'in's origin tag is '[از چی.]' = from Chinese, not from Turkish.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, vol. 3 printed p.1569 (BQT_v3_pages.txt pdf page 363), footnote to کاغذ\", \"stance\": \"partial\",\n    \"note\": \"'بقول لوفر این کلمه از اصل چینی است؛ در چینی ku-chih (تلفظ قدیم kok-či) از پوست درخت توت (Laufer, Sino-Iranica, p. 557 sqq). اما فرای گوید بیشتر احتمال می‌رود که کلمهٔ عربی «کاغذ» از اصل ترکی باشد تا … از اصل چینی.' Mo'in's note reports both the Chinese and the Turkic hypothesis (and, in the OCR, misattributes the Chinese one to Laufer, who in fact argued against it).\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"kâgad\",\n \"verdict\": \"plausible\",\n \"derivation\": \"A Middle Persian/Pāzand kāgad 'paper' is genuinely on record — Asbaghi, Persische Lehnwörter im Arabischen p.225, s.v. Arabic kāġad 'Papier, Brief', marks it 'pers.' and cites the Pahlavi-Pāzand glossaries ('pahl.-paz. s.v.'), alongside Mandaic kāgad/kāgid, Syriac and Aramaic forms; Addi Shir p.~130 says outright '(الكاغد) فارسي محض بمعنى القرطاس' ('al-kāġad: pure Persian, meaning qirṭās'). So the Iranian form with -d and the Arabic borrowing from it are secure, and Nourai's date is Laufer's: paper was imported into Samarkand from China 'as early as 650-1, again in 707' (SIN p.559). What is not secure is the arrow from a Turkic 'tree-bark' word. MacKenzie's Concise Pahlavi Dictionary has no kāgad, i.e. the word is not attested in Book Pahlavi proper but only in the late Pāzand/glossary tradition, which fits a word that entered Iranian with the paper trade of the 7th-8th c. rather than an inherited item. The modern derivation is from Sogdian kʾγδʾ /kāγaδā/, the language actually spoken in Samarkand where the paper industry started in 751; the Sogdian δ regularly appears as Persian -d/-ḏ. Nourai's note is a faithful summary of Laufer's polemic — Laufer wrote 'For myself, I am unable to see any coincidence between kok-či and kāgad' (p.558) — but Laufer's rejection of Chinese 榖紙 ku-chih only disposes of that particular Chinese etymon, not of an ultimately Chinese source mediated by Sogdian, which is what most handbooks now assume.\",\n \"derivation_fa\": \"صورت فارسی میانه/پازند kāgad «کاغذ» واقعاً گواه دارد: اسبقی در «وام‌واژه‌های فارسی در عربی» (ص ۲۲۵) ذیل عربی kāġad «کاغذ، نامه» آن را فارسی می‌داند و به فرهنگ‌های پهلوی-پازند و نیز صورت‌های مندایی kāgad/kāgid و سریانی و آرامی ارجاع می‌دهد؛ ادّی شیر هم می‌نویسد «(الكاغد) فارسي محض بمعنى القرطاس». پس وام‌گیری عربی از ایرانی قطعی است. آنچه قطعی نیست پیوند با واژهٔ ترکی به معنای «پوست درخت» است: مکنزی در فرهنگ پهلوی خود اصلاً kāgad ندارد، یعنی این واژه در پهلویِ کتابی نیامده و تنها در سنّت پازند/فرهنگ‌های متأخر دیده می‌شود — و این با واژه‌ای می‌خواند که همراه با تجارت کاغذ در سدهٔ اول و دوم هجری وارد ایرانی شده باشد، نه واژه‌ای موروثی. ریشه‌شناسی امروزی آن را وام‌واژه‌ای از سغدی kʾγδʾ می‌داند؛ سمرقند، خاستگاه کاغذسازی در ۷۵۱ میلادی، سرزمین سغدی‌زبان بوده و δ سغدی به‌قاعده در فارسی به د/ذ بدل می‌شود. یادداشت نورایی نیز عیناً جدل لاوفر است («هیچ تناسبی میان kok-či و kāgad نمی‌بینم»)، ولی ردّ ku-chih چینی تنها همان یک ریشهٔ چینی را رد می‌کند، نه خاستگاه چینیِ باواسطهٔ سغدی را.\",\n \"sources\": [SIN_URL, W + \"%DA%A9%D8%A7%D8%BA%D8%B0\"],\n \"ref_check\": [\n   {\"ref\": \"SIN:559\", \"status\": \"supports\",\n    \"note\": \"Sino-Iranica p.559: 'I need not repeat here the oft-told story of how the manufacture of paper was introduced into Samarkand by Chinese captives in a.d. 751. Prior to this date, as has been established by Karabacek, Chinese paper was imported to Samarkand as early as 650-1, again in 707.' — this is verbatim the source of Nourai's NOTE. p.558: 'For myself, I am unable to see any coincidence between kok-či and kāgad' = the second half of the note.\"},\n   {\"ref\": \"PLA:225\", \"status\": \"supports\",\n    \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p.225 (PLA_pages.txt leaf 240, running heads 'kāġad … 225 … kibāb'): 'kāġad: \\\"Papier, Brief\\\" pers.; pahl.-paz. s.v. kāgad; mand. kāgad, kāgid; syr., aram.' — the Pahlavi/Pāzand form kāgad that Nourai's node needs.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, PHD.txt / PHD_mackenzie.txt (grep kagad, k'kt)\", \"stance\": \"silent\",\n    \"note\": \"No headword kāgad in the Concise Pahlavi Dictionary — the word is absent from Book Pahlavi.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir 1908, AFM_pages.txt leaf 138 (printed p.~130)\", \"stance\": \"supports\",\n    \"note\": \"'( الكاغد ) فارسي محض بمعنى القرطاس . والكاغذ لغة فيه ومن الكردي…' — Arabic al-kāġad is 'purely Persian', with kāġaḏ a variant.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966-67 (KLN_1966.txt, grep kagad/caghd)\", \"stance\": \"silent\",\n    \"note\": \"Klein has no entry for the word (it never entered English).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"kâğaz «کاغذ»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP کاغذ kāġaz/kāġaḏ 'paper' is one of the best-attested words of classical Persian and continues the older Iranian kāgad directly: intervocalic -g- is kept, and the final -d of kāgad appears in Persian both as ذ (kāġaḏ, the classical spelling and the one the Arabs borrowed as كاغد/كاغذ) and, after the merger of ذ with ز in later New Persian, as -z (kāġaz), which is why Laufer could list 'kāγad, kāγid, kāγaz and kāγiδ' side by side (SIN p.557 n.6). The Sa'di couplet Nourai prints, 'کاغذ بدریدند و قلم بشکستند / وز دست زبان حرف‌گیران رستند', stands on exactly the page he cites, Borhan-e Qate' ed. Mo'in p.1569. The step Pahlavi/older-Iranian kāgad > NP kāġaz is therefore correct as drawn; only the ultimate source of kāgad is at issue (see the root box), where Wiktionary, following Gharib, has 'Borrowed from Sogdian 𐼸𐼰𐼲𐼹𐼰 (kʾγδʾ /kāγaδā/), perhaps a borrowing from Old Chinese 紙 (*kjeʔ)'. From Persian the word went on to Arabic kāġad/kāġiḏ, Ottoman كاغد > Turkish kâğıt, Hindi kāgad, Urdu kāġaz, Tamil kākitam, Kannada kāgada — all with the invariable a-vocalism that Laufer used as his argument against a Chinese etymon.\",\n \"derivation_fa\": \"«کاغذ» از پرکاربردترین واژه‌های فارسی دری است و مستقیماً دنبالهٔ صورت کهن‌ترِ ایرانی kāgad است: گِ میان‌واکه‌ای بر جای مانده و دالِ پایانی هم به‌صورت ذ (kāġaḏ، املای کلاسیک و همان که عرب به شکل «كاغد/كاغذ» وام گرفت) و هم — پس از یکی شدن ذ و ز در فارسی متأخر — به‌صورت ز (kāġaz) دیده می‌شود؛ به همین سبب لاوفر صورت‌های kāγad، kāγid، kāγaz و kāγiδ را کنار هم آورده است. بیت سعدی که نورایی نقل کرده («کاغذ بدریدند و قلم بشکستند / وز دست زبان حرف‌گیران رستند») دقیقاً در همان صفحهٔ برهان قاطع به تصحیح معین (ص ۱۵۶۹) آمده است. پس گام «پهلوی kāgad ← فارسی کاغذ» درست کشیده شده و تنها خاستگاه نهاییِ kāgad محل بحث است (نگاه کنید به جعبهٔ ریشه)، که ویکی‌واژه به پیروی قریب آن را وام از سغدی kʾγδʾ و شاید در نهایت از چینی باستان 紙 می‌داند. از فارسی این واژه به عربی، ترکی عثمانی (> kâğıt)، هندی، اردو، تامیلی و کنّده رفته است.\",\n \"sources\": [W + \"%DA%A9%D8%A7%D8%BA%D8%B0\", W + \"k%C3%A2%C4%9F%C4%B1t\", SIN_URL],\n \"ref_check\": [\n   {\"ref\": \"BQT:1569\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in vol.3, printed p.1569 = BQT_v3_pages.txt pdf page 363 (line 26428): the entry کاغذ ends with the very verse Nourai quotes, 'کاغذ بدریدند و قلم بشکستند وز دست زبان حرف گیران رستند'، and Mo'in's footnote on the same page discusses the Chinese vs Turkic origin (see the root-level consulted note).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol.3 p.1569 (pdf page 363)\", \"stance\": \"supports\",\n    \"note\": \"Headword and Sa'di shāhed exactly as in the chart; Mo'in's own footnote gives both origin theories.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi s.v. کاغذ (abadis.ir)\", \"stance\": \"partial\",\n    \"note\": \"'[از چی.]' — Mo'in gives the word a Chinese tag; the Persian form and meaning 'ورقهٔ نازک … از خمیر الیاف گیاهی' agree with the chart, the origin does not.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn 1893 (HRN.txt, grep kagad/kagaz)\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss has no numbered entry for کاغذ (he treats it as a foreign word; Laufer cites Horn, Grundriss der iran. Phil. I/2 p.7, where kagat/kagid is listed among possible Chinese loans).\"}\n ]\n})\ndata[\"entries\"].append(e0)\n\n# ------------------------------------------------------------------ entry 3\ne3 = {\n \"entry\": 3,\n \"root\": \"Kahrpu, Kharpuna\",\n \"verdict\": \"transcription_suspect\",\n \"modern_form\": \"Young Avestan kahrpuna- m., the name of a xrafstra (noxious daēvic creature), taken by the Pahlavi and Sogdian tradition as 'lizard'\",\n \"note\": \"The word is real and the citations are exact, but the second head-form is corrupt. Bartholomae, Altiranisches Wörterbuch col. 455 f. (BRT.txt \\\\f-leaf 277) has '• j. kahrpuna- m. Name eines daēvischen Tiers: baēvanᵊ ašinam spakanąm ⁰nanąm ava.janyāi \\\"zehntausend Hundsschlangen, (nämlich) K…\\\" V.14.5', with the Pahlavi version transcribing karpun. Gharib's Sogdian dictionary no. 4854 (p.193) equally writes '< Av. kahrpuna-'. There is no Avestan *kharpuna-: the printed page (pdf 234, book 204) really does show 'Kahrpu, Kharpuna', so the metathesised second form is Nourai's own misprint for 'Kahrpuna', not an extraction error — the JSON is faithful. The first form 'Kahrpu' is not Avestan either but the shorthand of Mo'in's footnote in Borhan-e Qate' p.1612, 'در اوستا kahrpu، در پهلوی karpu'. The gloss 'lizard' is a later identification: Bartholomae only says 'name of a daēvic animal', and the Vidēvdād passage groups it with 'dog-snakes'; the equation with the lizard comes from the Pahlavi/Sogdian and Persian tradition. Bartholomae expressly rejects Darmesteter's attempt to link the word with NP čalpāsa (ZA III 211): 'ist falsch; das wäre Aw. *gᵊhrpa- oder *gᵊrᵊpa-' — which matters for the Persian node below, where چلپاسه is listed among the variants.\",\n \"note_fa\": \"واژه اصیل است و ارجاع‌ها دقیق، ولی صورت دومِ سرواژه غلط چاپی است. بارتولومه در «فرهنگ ایرانی باستان» ستون ۴۵۵ ‌به بعد آورده است: «kahrpuna- (اوستایی متأخر)، نام جانوری دیوی: baēvanᵊ ašinam spakanąm kahrpunanąm، وندیداد ۱۴٫۵»، و ترجمهٔ پهلوی آن را karpun آوانویسی کرده است؛ قریب نیز در فرهنگ سغدی (مدخل ۴۸۵۴، ص ۱۹۳) می‌نویسد «< اوستایی kahrpuna-». در اوستایی صورتی به شکل *kharpuna- وجود ندارد؛ تصویر صفحهٔ چاپی (ص ۲۰۴ کتاب) نشان می‌دهد که خودِ کتاب «Kahrpu, Kharpuna» چاپ کرده است، پس این قلبِ حروف خطای چاپی نورایی است نه خطای خوانش اسکن. صورت نخست «Kahrpu» هم اوستایی نیست بلکه همان است که معین در حاشیهٔ برهان قاطع (ص ۱۶۱۲) نوشته: «در اوستا kahrpu، در پهلوی karpu». معنای «مارمولک» نیز تعیینِ متأخر است؛ بارتولومه تنها «نام جانوری دیوی» می‌گوید. افزون بر این، بارتولومه پیوند دارمستتر میان این واژه و «چلپاسه»ی فارسی را صریحاً رد می‌کند: «نادرست است؛ آن صورت در اوستا باید *gᵊhrpa- یا *gᵊrᵊpa- می‌بود». حکم: خطای چاپی کتاب.\",\n \"error_in\": \"book\",\n \"book_prints\": \"Kahrpu, Kharpuna\",\n \"correct_form\": \"Kahrpuna (Av. kahrpuna-); 'Kahrpu' is Mo'in's shorthand form\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:1612\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in vol.3 printed p.1612 = BQT_v3_pages.txt pdf page 405: footnote 5 to کرباسو lists the variants 'کرباسکه ـ کربانو … کرپاشه ـ کربایس ـ کربایش ـ کربی ـ کریش ـ کرفش' and ends 'در اوستا kahrpu در پهلوی karpu' — Nourai's root name and his Pahlavi node come straight from this line.\"},\n   {\"ref\": \"SOD:193\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary entry 4854 (SOD_pages.txt \\\\f-leaf 259 = printed p.193): 'krps\\\\'k B … karpase ⟨< Av. kahrpuna-, Pahl. krpwk, < *karp-asaka × xrafstar⟩ lizard'. Page 193 is exactly where Nourai points.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae 1904, col. 455 f. (BRT.txt \\\\f-leaf 277)\", \"stance\": \"partial\",\n    \"note\": \"'• j. kahrpuna- m. Name eines daēvischen Tiers: baēvanᵊ ašinam spakanąm ⁰nanąm ava.janyāi … V.14.5. Pü.: transskr. (karpun) … Darmesteters Zusammenstellung des Worts mit np. čalpāsa (ZA. III. 211) ist falsch; das wäre Aw. *gᵊhrpa- oder *gᵊrᵊpa-.' Supports the form kahrpuna- and the Pahlavi karpun, but not the gloss 'lizard' and not the čalpāsa variant.\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib no. 4854, p.193\", \"stance\": \"supports\",\n    \"note\": \"Derives the Sogdian word from Av. kahrpuna- and glosses it 'lizard'; her base is *karp-asaka- crossed with xrafstar.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian (KNT.txt)\", \"stance\": \"silent\",\n    \"note\": \"No Old Persian cognate; the word is Avestan only.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"karpu, krpwk\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both forms are documented and both come from the two references Nourai cites. The Pahlavi Vidēvdād renders Av. kahrpuna- by a word Bartholomae transcribes karpun (col. 455 f.), and Mo'in's footnote in Borhan p.1612 gives the same in the form 'در پهلوی karpu'. The spelling krpwk that Nourai prints beside it is the Pahlavi orthography quoted by Gharib in her Sogdian dictionary (no. 4854: '< Av. kahrpuna-, Pahl. krpwk'), i.e. a graphic ⟨krpwk⟩ to be read *karpūg/*karpōg with the common Middle Persian diminutive/appurtenance suffix -ūg < *-uka-. Phonetically the step is regular: Av. kahrpuna- loses the -h- before -r- (Av. -hr- > MP -r-, as in kahrpa- 'body, form' > MP karp), the cluster is simplified, and the -una- stem is replaced by the productive -ūg. The animal designation stayed constant ('lizard, gecko'), the Avestan text having classed it among the xrafstras that a good Zoroastrian kills.\",\n \"derivation_fa\": \"هر دو صورت گواه دارند و هر دو از همان دو مأخذی می‌آیند که نورایی یاد کرده است. در ترجمهٔ پهلوی وندیداد، اوستایی kahrpuna- با واژه‌ای برگردانده شده که بارتولومه آن را karpun آوانویسی می‌کند (ستون ۴۵۵ به بعد)، و معین در حاشیهٔ برهان (ص ۱۶۱۲) همان را «در پهلوی karpu» می‌آورد. املای krpwk که نورایی در کنار آن نهاده، همان است که قریب در فرهنگ سغدی (مدخل ۴۸۵۴) نقل کرده و باید *karpūg/karpōg خواند، با پسوند پرکاربرد -ūg < *-uka- فارسی میانه. تحول آوایی به‌قاعده است: در ایرانی میانه خوشهٔ -hr- اوستایی به -r- ساده می‌شود (مانند kahrpa- «تن، پیکر» > karp پهلوی) و ستاک -una- جای خود را به پسوند زایای -ūg می‌دهد. معنای جانورشناختی («مارمولک، وزغه») دست‌نخورده مانده است؛ در اوستا این جانور از «خرفستران» به شمار می‌رفته است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:1612\", \"status\": \"supports\",\n    \"note\": \"'…در اوستا kahrpu در پهلوی karpu' (BQT vol.3 pdf page 405 = printed 1612, footnote 5 to کرباسو).\"},\n   {\"ref\": \"SOD:193\", \"status\": \"supports\",\n    \"note\": \"Gharib no. 4854 (p.193) cites 'Pahl. krpwk' as the Middle Persian counterpart of the Sogdian word — the second of Nourai's two Pahlavi forms.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 (PHD.txt, grep karp/krpwk)\", \"stance\": \"silent\",\n    \"note\": \"The Concise Pahlavi Dictionary has no entry for this animal name (it is a Vidēvdād gloss word, not part of MacKenzie's core vocabulary).\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae col. 455 f.\", \"stance\": \"supports\",\n    \"note\": \"'Pü.: transskr. (karpun) mit der Erl.: …' — the Pahlavi translators kept the word and only transcribed it.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\",\n    \"note\": \"Not in Nyberg's glossary, which covers the Kār-nāmag/Mēnōg ī xrad texts rather than the Vidēvdād gloss vocabulary.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"karbâsŭ «کرباسو»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Persian word is real and richly attested: Borhan-e Qate' p.1612 has کرباسو with the variant series کرباسکه، کربانو، کرپاسو، کرپاشه، کربایس، کربایش، کربی، کریش، کرفش, and the shāhed Nourai prints, 'میکشد هم نهنگ را راسو / مرگ عقرب بود ز کرباسو' (Āzarī Tūsī), stands on that same page; Mo'in's Farhang lists کرباسو، کلباسو، کلپاسو، کلسو، کرسو، چلپاسو among the synonyms of مارمولک 'lizard'. The etymological connection with Av. kahrpuna- is Mo'in's own and is accepted by Gharib. What is only plausible is the arrow as Nourai draws it, Pahlavi karpu/krpwk > NP karbāsu: the -āsu of the Persian form cannot come from *karpūg but matches Gharib's base *karp-asaka- (whence Sogdian krps'k karpase) exactly, so NP karbāsu and Sogd. krps'k are parallel outcomes of *karpāsaka-, not mother and daughter of the Pahlavi -ūg form; the voicing p > b in karbāsu is a normal New Persian intervocalic development beside the preserved کرپاسو. Two of the variants Nourai lists in the extra line are more doubtful still: کرش is a different word, and چلپاسه/چلپاسو with initial č- is precisely the form Bartholomae refuses to connect with kahrpuna- ('ist falsch; das wäre Aw. *gᵊhrpa- oder *gᵊrᵊpa-'), the initial č- of Persian requiring an Old Iranian *č-, so čalpāsa is at best a folk-etymological contamination of karpāsa with čal-/čap-.\",\n \"derivation_fa\": \"واژهٔ فارسی اصیل و پرگواه است: برهان قاطع (ص ۱۶۱۲) «کرباسو» را با گونه‌های کرباسکه، کربانو، کرپاسو، کرپاشه، کربایس، کربایش، کربی، کریش و کرفش آورده و شاهدِ همان صفحه بیت آذری طوسی است: «می‌کشد هم نهنگ را راسو / مرگ عقرب بود ز کرباسو». معین نیز در فرهنگ فارسی، کرباسو، کلباسو، کلپاسو، کلسو، کرسو و چلپاسو را از مترادف‌های «مارمولک» شمرده است. پیوند ریشه‌شناختی با اوستایی kahrpuna- از خود معین است و قریب هم آن را پذیرفته. آنچه تنها «با احتیاط پذیرفتنی» است شکل پیکانِ نمودار است: پسوندِ -آسو در «کرباسو» نمی‌تواند از *karpūg پهلوی بیاید، بلکه دقیقاً با پایهٔ *karp-asaka- (بازساختهٔ قریب، سرچشمهٔ krps'k سغدی) می‌خواند؛ پس «کرباسو» و صورت سغدی، هر دو بازماندهٔ موازی *karpāsaka-اند نه یکی زادهٔ دیگری. ابدال پ > ب در «کرباسو» تحول عادی میان‌واکه‌ای فارسی نو است و صورت «کرپاسو» گونهٔ کهن‌تر را نگاه داشته است. دو گونهٔ دیگرِ فهرست جای درنگ دارد: «کرش» واژهٔ دیگری است، و «چلپاسه/چلپاسو» با چِ آغازین همان صورتی است که بارتولومه پیوندش را با kahrpuna- «نادرست» می‌خواند، زیرا چِ فارسی نو نیازمند *č- ایرانی باستان است؛ پس چلپاسه احتمالاً آمیزش ریشه‌شناسی عامیانهٔ karpāsa با چل-/چپ- است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"MON:2933\", \"status\": \"partial\",\n    \"note\": \"The 6-volume Amir Kabir Farhang-e Fārsi is not on disk; the 2-volume Adena abridgement (MON_part2.txt line 42300) does carry the word: under مارمولک it lists 'چلپاسه، کلپاسه، کرباسو، کلباسو، کلپاسو، کلسو، کرسو، چلپاسو، گلموژ…' as its synonyms, i.e. Mo'in does gloss کرباسو as 'lizard' as Nourai says, but p.2933 of the 6-vol. edition could not be checked (different pagination).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in vol.3 p.1612 (pdf page 405)\", \"stance\": \"supports\",\n    \"note\": \"Headword کرباسو, the Āzarī Tūsī verse 'می‌کشد هم نهنگ را راسو ـ مرگ عقرب بود ز کرباسو' and footnote 5 with the variant list and 'در اوستا kahrpu در پهلوی karpu'.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in (2-vol. Adena abridgement), s.v. مارمولک\", \"stance\": \"supports\",\n    \"note\": \"'…اشت: چلپاسه، کلپاسه، کرباسو، کلباسو، کلپاسو، کلسو، کرسو، چلپاسو، گلموژ…' — کرباسو listed as a synonym of مارمولک 'lizard'.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae col. 455 f.\", \"stance\": \"contradicts\",\n    \"note\": \"For the چلپاسه variant only: 'Darmesteters Zusammenstellung des Worts mit np. čalpāsa (ZA. III. 211) ist falsch; das wäre Aw. *gᵊhrpa- oder *gᵊrᵊpa-.'\"},\n   {\"src\": \"HRN\", \"where\": \"Horn 1893 / Hübschmann, Persische Studien (HRN.txt, HUB.txt)\", \"stance\": \"silent\",\n    \"note\": \"Neither Horn nor Hübschmann has an entry for کرباسو/چلپاسه.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"krps`k\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Buddhist Sogdian krps'k, read karpase by Gharib, is entry no. 4854 on p.193 of her Sogdian-Persian-English dictionary — precisely the page Nourai cites — glossed 'lizard' and etymologised there as '< Av. kahrpuna-, Pahl. krpwk, < *karp-asaka × xrafstar'. The Sogdian form thus does descend from the same Old Iranian stem as the Avestan word, but with the animal-name suffix *-asaka- instead of *-una-, and with (Gharib argues) contamination from xrafstar-, the Avestan term for the noxious creatures to which the lizard belongs. Sogdian regularly keeps the cluster -rp- and writes the ending -'k for -ē/-ak, so krps'k = karpasē. The word is attested in the Buddhist manuscripts (Gharib refers to TSP 13 and to Bailey's Khotanese material).\",\n \"derivation_fa\": \"صورت سغدیِ بودایی krps'k، که قریب آن را karpase می‌خواند، مدخل شمارهٔ ۴۸۵۴ در صفحهٔ ۱۹۳ «فرهنگ سغدی» اوست — همان صفحه‌ای که نورایی ارجاع داده — با معنای «مارمولک» و این ریشه‌شناسی: «< اوستایی kahrpuna-، پهلوی krpwk، از *karp-asaka با آمیزش xrafstar». پس صورت سغدی از همان ستاک ایرانی باستان می‌آید، اما با پسوند جانورنام *-asaka- به‌جای *-una-، و به گمان قریب زیر تأثیر واژهٔ اوستایی xrafstar «جانور موذی» که مارمولک از آن دسته بوده است. سغدی خوشهٔ -rp- را نگاه می‌دارد و پایانهٔ 'k- را برای -ē/-ak می‌نویسد؛ پس krps'k همان karpasē است. این واژه در دست‌نوشته‌های بودایی سغدی گواه دارد.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:193\", \"status\": \"supports\",\n    \"note\": \"SOD_pages.txt \\\\f-leaf 259 = printed p.193, entry '4854 krps\\\\'k B … karpase ⟨< Av. kahrpuna-, Pahl. krpwk, < *karp-asaka × xrafstar⟩ lizard'. Both the page number and the gloss are exactly Nourai's.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib no. 4854, p.193\", \"stance\": \"supports\",\n    \"note\": \"As quoted; Gharib herself makes the Avestan connection Nourai draws.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae col. 455 f., s.v. kahrpuna-\", \"stance\": \"partial\",\n    \"note\": \"Confirms the Avestan etymon and the Pahlavi transcription, but says nothing about Sogdian (Bartholomae 1904 predates the Sogdian finds).\"},\n   {\"src\": \"ISS\", \"where\": \"Bailey, Khotanese material (ISS_alt_DKS.txt)\", \"stance\": \"silent\",\n    \"note\": \"No Khotanese cognate found under karp-/kahrp-.\"}\n ]\n})\ndata[\"entries\"].append(e3)\njson.dump(data, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part1.json','w'), ensure_ascii=False, indent=1)\nprint(\"part1 ok\", len(data[\"entries\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build234.py"
}
```


### [2026-09-06T15:51:56.688Z] TOOL RESULT

```
part1 ok 2
```


## [2026-09-06T15:57:35.661Z] TOOL CALL #88: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build234b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW = \"https://en.wiktionary.org/wiki/\"\nAHD_SIKH = \"https://www.ahdictionary.com/word/search.html?q=Sikh\"\nAHD_HATCH = \"https://www.ahdictionary.com/word/search.html?q=hatch\"\nETY_HATCH = \"https://www.etymonline.com/word/hatch\"\n\ne4 = {\n \"entry\": 4,\n \"root\": \"Kak 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ḱek- / *ḱak- 'to be able, be capable, help' (Pokorny IEW 522 k̂ak- (k̂ek-?) 'vermögen, helfen'; Watkins AHD kak-¹ 'to enable, help'; LIV 322 *ḱekʷ-)\",\n \"note\": \"Root box, language label, gloss and even the numbering are right. Pokorny p.522 — exactly the page Nourai cites — heads the entry 'k̂ak- (k̂ek-?) „vermögen, helfen\\\"' and fills it with the same material the chart uses: 'Ai. śaknóti „kann, ist imstande, hilft\\\", Desid. śikṣati „hilft, huldigt, dient, lernt\\\", śakti- f. „Hilfe\\\" … av. sacaiti „versteht sich worauf\\\", Desid. sixšaiti „lernt\\\", npers. saxt „hart, fest, sehr\\\" = ai. śakta- „vermögend\\\"; air. cécht „Macht\\\"'. Watkins' appendix, which Nourai cites elsewhere as AHD, has 'kak-¹. To enable, help. Sanskrit śaknoti, he is able, he is strong: SHAKTI, SIKH. [Pok. kak- 522.]' — so even Nourai's '1' in 'Kak 1' reproduces Watkins' superscript, and Watkins independently confirms the Sikh branch. Cheung 2007 (s.v. *sač¹) sets the Iranian family under 'PIE *ḱekʷ- \\\"to achieve, accomplish, be able, capable\\\" => LIV: 322 | Pok.: 522', noting that 'although this Ir. root has a good IE etymology, it has no further IE verbal correspondences'. The only weak branch on the chart is the Germanic one (nodes 8-9): Pokorny attaches Engl. hatch only under an explicit 'unsicher', and Walde-Pokorny I 334 puts it in a separate entry altogether.\",\n \"note_fa\": \"جعبهٔ ریشه، برچسب زبان، معنا و حتی شماره‌گذاری درست است. پوکورنی در صفحهٔ ۵۲۲ — همان صفحه‌ای که نورایی یاد کرده — مدخل «k̂ak- (k̂ek-؟) توانستن، یاری کردن» را آورده و همان مواد نمودار را در آن گرد کرده است: «سنسکریت śaknóti «می‌تواند، تواناست، یاری می‌کند»، صورت آرزویی śikṣati «یاری می‌کند، خدمت می‌کند، می‌آموزد»، śakti- «یاری»؛ اوستایی sacaiti «به چیزی داناست»، صورت آرزویی sixšaiti «می‌آموزد»؛ فارسی نو saxt «سخت، استوار، بسیار» = سنسکریت śakta- «توانا»؛ ایرلندی باستان cécht «توان»». واتکینز در پیوست AHD می‌نویسد: «kak-¹ توانا کردن، یاری کردن. سنسکریت śaknoti … : SHAKTI، SIKH. [پوکورنی ۵۲۲]» — پس شمارهٔ «۱» در «Kak 1» نیز از همان‌جاست و شاخهٔ «سیک» را هم واتکینز مستقلاً تأیید می‌کند. چونگ (۲۰۰۷) خانوادهٔ ایرانی را ذیل «PIE *ḱekʷ-، LIV ۳۲۲، پوکورنی ۵۲۲» می‌آورد. تنها شاخهٔ سست نمودار، شاخهٔ ژرمنی (گره‌های ۸ و ۹) است که پوکورنی خود آن را «نامطمئن» خوانده و والده-پوکورنی در مدخلی جداگانه نهاده است. حکم: ادعای نورایی دربارهٔ ریشه درست است.\",\n \"sources\": [W + \"%D8%B3%D8%A7%D8%AE%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:522\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt line 2721 (the leaf whose running numbers are 521-523, i.e. the page marked '522'): 'k̂ak- (k̂ek-?) „vermögen, helfen\\\". Ai. śaknóti „kann, ist imstande, hilft\\\", Desid. śikṣati „hilft, huldigt, dient, lernt\\\", śakti- f. „Hilfe\\\", śakra- „vermögend\\\" … av. sacaiti „versteht sich worauf\\\", Desid. sixšaiti „lernt\\\", npers. saxt „hart, fest, sehr\\\" = ai. śakta- „vermögend\\\"; air. cécht „Macht\\\" … unsicher auch ags. hagan „genitalia\\\" … nhd. hecken „sich paaren (von Vögeln)\\\", engl. hatch „brüten\\\" … prakr. ca(y)ati „ist fähig\\\", Aśoka-Inschr. caghati …, av. cagdə- (mit rafəδrəm) „Hilfe gewährend\\\", cagdman- n. „Geschenk\\\", cagvah- „bietend, gewährend\\\". WP. I 333, 334.' Page 522 alone underwrites the root box and nodes 1, 3, 4, 5, 6 and (with the reservation 'unsicher') node 8.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 333 f. (WLD_Bd1_pages.txt, running head 'q̂ak — kaq-')\", \"stance\": \"supports\",\n    \"note\": \"The source Pokorny abridges; the same Avestan material is there with the reference 'cagvah- „bietend, gewährend\\\" (Bartholomae Air. Wb. 576), die freilich wiederum in ihrem e-Vokalismus nicht so unmittelbar zum germ. a : ō stimmen'. But at p.334 Walde-Pokorny put the Germanic hatch group under a separate head, 'kak- „männliche Geschlechtsteile\\\"?', and only mention Schrader's link with ai. śaknóti as 'erwägenswert'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, k-list (AHD_watkins1985.txt line 572)\", \"stance\": \"supports\",\n    \"note\": \"'kak-¹. To enable, help. Sanskrit śaknoti, he is able, he is strong: SHAKTI, SIKH. [Pok. kak- 522.]' — identical gloss, identical numbering, and Sikh is derived from this root.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *sač¹ (CHEUNG.txt lines 21216-21280)\", \"stance\": \"supports\",\n    \"note\": \"'*sač¹ \\\"to fit, be suitable, be able, be in command of; to prepare\\\" … «PIE *ḱekʷ- \\\"to achieve, accomplish, be able, capable\\\" => LIV: 322 | Pok.: 522» … *IE COGNATES: OIrish cécht \\\"might, power\\\" … ON hagar \\\"it is fitting, suitable\\\".'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IE Comparative Dictionary, kak- (1)-(4) (IEC.txt lines 6648-6651)\", \"stance\": \"partial\",\n    \"note\": \"Mann has four homophonous kak- roots ('leather; thong', 'hold?', 'withered', 'strike') and no kak- 'be able'; he files the Germanic hagen/hagi group under kak- (2) 'hold', not with śaknóti — i.e. he does not recognise Pokorny's root under this shape.\"}\n ],\n \"nodes\": []\n}\nN = e4[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"sak, sač, sâx : to do, make ; sačaiti : able, qualified, deserving\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The forms are right, the glosses are loose. Bartholomae, Altiranisches Wörterbuch col. 1552 (BRT.txt line 25858) has '• j., g. sak- V. „sich verstehen auf –\\\". Praes. 1 sac-, 16 (Des.) sixša-, 26 sača-, 30 (Kaus.) sāčaya-' — so Nourai's three citation-forms sak (the root), sač (the thematic present sača-/sac-) and sāx (the causative stem sāčaya-, whose Middle Persian outcome is written s'ht-) are all genuine Avestan stems of one verb. But the Avestan verb does not mean 'to do, make'; it means 'to be versed in, understand', and its causative sāčaya- means 'to teach' (so Nyberg s.v. saxtan: 'Av. (1552) sācaya- \\\"to teach\\\"'). Likewise sačaiti is a 3rd sg. present 'he understands / it is fitting', not an adjective 'able, qualified, deserving' — that is the meaning of the Middle Persian derivatives sazāg / NP سزاوار which the chart's Persian node covers. Pokorny p.522 renders it exactly so: 'av. sacaiti „versteht sich worauf\\\", Desid. sixšaiti „lernt\\\"'. The sense 'to do, make' is a secondary Middle Iranian development of the causative ('cause to be fitting' > 'prepare, arrange, build'), not an Avestan meaning.\",\n \"derivation_fa\": \"صورت‌ها درست‌اند، معناها آزاد. بارتولومه در ستون ۱۵۵۲ می‌آورد: «sak- (اوستایی گاهانی و متأخر): «به چیزی دانا بودن»؛ ستاک‌های حال: sac-، صورت آرزویی sixša-، ستاک sača-، سببی sāčaya-». پس هر سه صورتِ نورایی — sak (ریشه)، sač (ستاک حالِ sača-/sac-) و sāx (ستاک سببی sāčaya- که در فارسی میانه s'ht- نوشته می‌شود) — اوستایی راستین‌اند. اما فعل اوستایی معنای «کردن، ساختن» ندارد؛ معنایش «به چیزی دانا بودن» است و سببیِ sāčaya- یعنی «آموزاندن» (نیبرگ ذیل saxtan: «اوستایی sācaya- «to teach»»). همچنین sačaiti فعل سوم‌شخص مفرد حال است («می‌داند، شایسته است»)، نه صفتی به معنای «توانا، سزاوار»؛ این معنای اخیر از آنِ مشتقات فارسی میانه (sazāg) و فارسی نو (سزاوار) است. پوکورنی نیز در ص ۵۲۲ می‌نویسد: «اوستایی sacaiti «به چیزی داناست»، آرزویی sixšaiti «می‌آموزد»». معنای «کردن، ساختن» تحول ثانویِ ایرانی میانه از ستاک سببی است («شایسته کردن» > «آماده کردن، ساختن»). حکم: با احتیاط پذیرفتنی؛ صورت‌ها درست، گلاس‌ها نادقیق.\",\n \"sources\": [W + \"%D8%B3%D8%A7%D8%AE%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:522\", \"status\": \"partial\",\n    \"note\": \"Pokorny 522 has 'av. sacaiti „versteht sich worauf\\\", Desid. sixšaiti „lernt\\\"' — the form, but glossed 'understands', not 'able, qualified, deserving', and he cites no Avestan sak-/sāx 'to do, make'.\"},\n   {\"ref\": \"HRN:152\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss no. 688 on printed p.152 (HRN.txt \\\\f-leaf 174): 'sāxten „machen, ausführen\\\", Praes. sāz-em, sāz „Gerät\\\" … aw. √sac-, mit aiwi „darbringen, ausführen (yasnem)\\\"; phlv. sāxtan, sac(i)šn.' Horn's page 152 is precisely Nourai's citation and it does give the Avestan root sac- as the source.\"},\n   {\"ref\": \"FFD:58\", \"status\": \"supports\",\n    \"note\": \"Abolghasemi, Fe'lhā-ye Fārsi-ye Dari p.58 (FFD_pages.txt pdf page 63): 'ساختن / ساخت < فارسی میانه sāxt < ایرانی باستان *sāč-ta … ریشهٔ sak به معنی «توانا بودن» است. / ساز < فارسی میانه sāz < ایرانی باستان *sāč-a-.' Exactly the root and stems of Nourai's node, and the gloss 'to be able' rather than 'to make'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae 1904 col. 1552 (BRT.txt line 25858)\", \"stance\": \"partial\",\n    \"note\": \"'• j., g. sak- V. „sich verstehen auf –\\\". Praes. 1 sac-, 16 (Des.) sixša-, 26 sača-, 30 (Kaus.) sāčaya-, Perf. sasč-.' — forms yes, meaning 'be versed in', not 'do, make'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon (KNT.txt)\", \"stance\": \"silent\",\n    \"note\": \"No Old Persian form of this root is attested in the inscriptions.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *sač¹\", \"stance\": \"supports\",\n    \"note\": \"Heads the family '*sač¹ \\\"to fit, be suitable, be able, be in command of; to prepare\\\"', with the Middle Persian causative 'BMP s'c- /sāz-/ (caus.) \\\"to make, prepare\\\"' — i.e. 'make' is the causative's meaning, exactly as argued above.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"sâxtan «ساختن (سازیدن، سازش، سازگار)» ; sezîdan «سزیدن (سزا، سزاوار)»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both Persian verbs are the regular New Persian continuations of the two stems of the same Old Iranian verb, and Nourai's three Horn page numbers hit all of it. (a) ساختن sāxtan / سازـ sāz- 'to make, build, prepare' < MP sāxtan, sāz- (Book Pahlavi s'htn', s'c-), the causative *sāčaya- of Av. sak-; the past stem *sāč-ta- gives -xt- by the regular Middle Iranian change č + t > xt (as in soxtan : sōz-, doxtan : dōz-), so sāz- : sāxt is a textbook pair. Horn no. 688 (p.152) states it, Nyberg s.v. saxtan gives 'Caus. of sac-; Av. (1552) sācaya- \\\"to teach\\\"; MPrth s'c- \\\"to prepare, to form\\\"; Pāz. NP sāxtan sāz-', MacKenzie has 'sāxtan, sāz- [s'htn', s'c-] make, prepare; tolerate', and Wiktionary derives NP ساختن 'from Middle Persian sāxtan, from Proto-Iranian *cāčáyati \\\"to prepare, build\\\", … cognate with Sanskrit śak-'. (b) سزیدن sazīdan 'to be worthy, be fitting' < MP sazīdan/sacītan, from the simple present sac- 'it is fitting'; Horn no. 738 (p.162) prints 'sezīden „sich ziemen, passen\\\", sezā, sezāyīden. phlv. sacītan, sacīt (pāz. sazed, sažēd), sacāk', and Nyberg s.v. sac- has 'From sak-, Skr. śaknoti \\\"to be able\\\" … MPrs szyd \\\"shall\\\"; Pāz. sažīdan or sažastan; NP sazīdan sazad.' The bracketed Persian derivatives are all in place: سازیدن and سازش and سازگار from sāz-, سزا (< MP sazāg) and سزاوار from saz-.\",\n \"derivation_fa\": \"هر دو فعل فارسی دنبالهٔ به‌قاعدهٔ دو ستاکِ یک فعل ایرانی باستان‌اند و هر سه شمارهٔ صفحهٔ هرن که نورایی داده درست است. الف) «ساختن / ساز-» از فارسی میانه sāxtan، sāz- (پهلوی کتابی s'htn'، s'c-)، که خود ستاک سببیِ *sāčaya- از ریشهٔ اوستایی sak- است؛ ستاک ماضی *sāč-ta با دگرگونی آواییِ همیشگیِ ایرانی میانه (č + t > xt، مانند سوختن : سوز-، دوختن : دوز-) به «ساخت» رسیده است. هرن در شمارهٔ ۶۸۸ (ص ۱۵۲) همین را می‌گوید، نیبرگ ذیل saxtan می‌نویسد «سببیِ sac-؛ اوستایی sācaya- «آموزاندن»؛ پارتی s'c-؛ پازند و فارسی نو sāxtan sāz-»، و مکنزی «sāxtan, sāz- [s'htn', s'c-] ساختن، آماده کردن» دارد؛ ویکی‌واژه هم آن را از فارسی میانه sāxtan و ایرانی آغازین *cāčáyati می‌داند. ب) «سزیدن» از فارسی میانه sazīdan/sacītan، از ستاک حالِ ساده sac- «شایسته است»؛ هرن در شمارهٔ ۷۳۸ (ص ۱۶۲) می‌آورد: «سزیدن، سزا، سزاییدن. پهلوی sacītan, sacīt (پازند sazēd)، sacāk»؛ نیبرگ نیز ذیل -sac می‌نویسد «از sak-، سنسکریت śaknoti «توانستن» … پازند sažīdan، فارسی نو سزیدن، سزد». واژه‌های داخل کمانک هم درست‌اند: سازیدن، سازش و سازگار از ستاک ساز-، و سزا (< پهلوی sazāg) و سزاوار از ستاک سز-. حکم: ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%B3%D8%A7%D8%AE%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:152,160,162\", \"status\": \"supports\",\n    \"note\": \"All three pages check out. p.152 (HRN \\\\f-leaf 174) no. 688 'sāxten „machen, ausführen\\\", Praes. sāz-em … aw. √sac- …; phlv. sāxtan, sac(i)šn'; p.160 (leaf 182) no. 723 'sext „hart, fest; sehr\\\" … ai. √śak-, śaknoti „vermögen, können\\\", skr. śaktá- „vermögend\\\"; phlv. saxt' (that is the saxt branch, nodes 5-6); p.162 (leaf 184) no. 738 'sezīden „sich ziemen, passen\\\", sezā, sezāyīden. phlv. sacītan, sacīt (pāz. sazed, sažēd), sacāk.'\"},\n   {\"ref\": \"BQT:1137\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in vol.2, printed p.1137 (BQT_v2_pages.txt \\\\f-leaf 600; the running-head offset in this stretch is leaf + 537, checked against سخت at leaf 569 = p.1106): the page carries سزا / سزیدن with Mo'in's etymological footnote '٭ سزیدن … پهلوی sazītan (فعل آن sazēt، پازند sazīdan, sazastan) … شایسته بودن، لایق بودن، سزاوار بودن.'\"},\n   {\"ref\": \"POK:522\", \"status\": \"supports\",\n    \"note\": \"Pokorny 522 cites 'npers. saxt' under this root; the verb sāxtan is not named on the page but its Avestan base sac-/sāčaya- is.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn nos. 688 (p.152) and 738 (p.162)\", \"stance\": \"supports\", \"note\": \"As quoted in the ref_check.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. sac-, saxtan (NYB_vol2_glossary.txt lines 3350, 3416)\", \"stance\": \"supports\",\n    \"note\": \"'sac- [sc-] pres. st., impers. it is convenient, suitable, proper … From sak-, Skr. śaknoti \\\"to be able\\\" [Av. (1552 sq.) sak- in a specialized sense]; MPrth sc-; Pāz. sažīdan or sažastan; NP sazīdan sazad. V. also saxt and sāxtan.' — 'saxtan [s'htn'] sāc- to form, to prepare, to arrange, to build, to make … Caus. of sac-; Av. (1552) sācaya- \\\"to teach\\\"; Pāz. NP sāxtan sāz-.'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.75 s.v. sāxtan (PHD_mackenzie.txt line 4519)\", \"stance\": \"supports\",\n    \"note\": \"'sāxtan, sāz- [s'htn', s'c- | (P s'c-)] make, prepare; tolerate' — and separately 'sazistan, saz- [sc-stn'] pass'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *sač¹, NWIr section\", \"stance\": \"supports\",\n    \"note\": \"'NP sazad \\\"it is fitting\\\", sāxtan/sāz- \\\"to build, construct, prepare\\\", Bal. sacit/sac- \\\"to adjust, be suitable\\\" …' — both of Nourai's Persian verbs under the one root.\"},\n   {\"src\": \"BQT\", \"where\": \"vol.2 p.1137 (leaf 600), footnote to سزیدن\", \"stance\": \"supports\",\n    \"note\": \"Mo'in gives Pahlavi sazītan/sazēt and the meanings 'شایسته بودن، لایق بودن، سزاوار بودن'.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Avestan\", \"words\": \"čagad : helped ; čageman : gift ; čagvah : offered\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The three words are genuine Gathic Avestan and Nourai has them from Pokorny p.522, who prints 'av. cagdə- (mit rafəδrəm) „Hilfe gewährend\\\", cagdman- n. „Geschenk\\\", cagvah- „bietend, gewährend\\\"'. Bartholomae col. 576 (BRT.txt lines 11112-11121) has them as separate lemmas: 'g. čagəd- Adj. „bietend, gewährend\\\"', 'g. čagəman- n. „Geschenk\\\"' (Y.38.2, of the waters as a gift to both existences), 'g. čagvah- Adj. „bietend, gewährend\\\"' (Y.46.2). So the correct forms carry a schwa, čagəd- / čagəman- / čagvah-, and the correct glosses are 'granting, offering' and 'gift'; Nourai's 'čagad : helped' is a compression of Pokorny's 'Hilfe gewährend' = 'granting help' (the collocation is čagəd- + rafəδrəm 'help'), and 'čagvah : offered' should be 'offering, granting' — an active participle, not a passive. The real reservation is about the arrow itself: Pokorny lists this Iranian group under k̂ak- only on Zupitza's conjecture that the root ended in -gh-, and immediately adds that the words 'freilich wiederum in ihrem e-Vokalismus nicht so unmittelbar zum germ. a : ō stimmen'. With Prakrit ca(y)ati 'is able' and Aśokan caghati they form a plausible but not established branch of the root; modern handbooks (Cheung, LIV) reconstruct the Iranian verb as *sač- / *ḱekʷ- and leave čag- aside.\",\n \"derivation_fa\": \"هر سه واژه اوستایی گاهانیِ اصیل‌اند و نورایی آن‌ها را از پوکورنی ص ۵۲۲ گرفته است: «اوستایی cagdə- (با rafəδrəm) «یاری‌بخش»، cagdman- «پیشکش»، cagvah- «ارزانی‌دارنده»». بارتولومه در ستون ۵۷۶ هر سه را مدخل جداگانه کرده است: «čagəd- (گاهانی) «ارزانی‌دارنده»»، «čagəman- «پیشکش»» (یسنه ۳۸٫۲، دربارهٔ آب‌ها به‌عنوان بخشش برای هر دو جهان)، «čagvah- «ارزانی‌دارنده»» (یسنه ۴۶٫۲). پس صورت‌های درست با شوا هستند — čagəd-, čagəman-, čagvah- — و معنای درست «بخشنده، ارزانی‌دارنده» و «پیشکش» است؛ «čagad: helped» فشرده‌سازیِ عبارت پوکورنی «Hilfe gewährend» (یاری‌بخش) است و «čagvah: offered» باید «ارزانی‌دارنده» باشد نه صورت مجهول. اما تردید اصلی در خودِ پیکان است: پوکورنی این گروه ایرانی را تنها بر پایهٔ حدس تسوپیتسا (که پایانهٔ ریشه را -gh- می‌گرفت) ذیل k̂ak- آورده و بی‌درنگ می‌افزاید که این صورت‌ها «با واکهٔ e خود چندان مستقیم با a : ō ژرمنی نمی‌خوانند». پژوهش امروزی (چونگ، LIV) فعل ایرانی را *sač- بازمی‌سازد و čag- را کنار می‌گذارد. حکم: با احتیاط پذیرفتنی.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:522\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt line 2721 ff.: 'unter Annahme von ausl. -gh- vergleicht Zupitza Gutt. 104 sie mit prakr. ca(y)ati „ist fähig\\\", Aśoka-Inschr. caghati „ist zu etwas bereit, willig\\\", av. cagdə- (mit rafəδrəm) „Hilfe gewährend\\\", cagdman- n. „Geschenk\\\", cagvah- „bietend, gewährend\\\", die freilich wiederum in ihrem e-Vokalismus nicht so unmittelbar zum germ. a : ō stimmen'. The page does carry all three words, but hedged.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae 1904 col. 576 (BRT.txt lines 11112, 11119, 11121)\", \"stance\": \"partial\",\n    \"note\": \"'• g. čagəd- Adj. „bietend, gewährend\\\"'; '• g. čagəman- n. „Geschenk\\\": … uxšibya ahubyā ⁰mə \\\"die Wasser …, das Geschenk für beide Existenzen\\\" Y.38.2'; '• g. čagvah- Adj. „bietend, gewährend\\\" … Y.46.2.' Confirms the forms (with schwa) and corrects the glosses; Bartholomae offers no IE etymology.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 333\", \"stance\": \"partial\",\n    \"note\": \"'…čagvah- „bietend, gewährend\\\" (Bartholomae Air. Wb. 576), die freilich wiederum in ihrem e-Vokalismus nicht so unmittelbar zum germ. a : ō stimmen.' — the same reservation, with Bartholomae's column number.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 (CHEUNG.txt, s.v. *sač¹ and index)\", \"stance\": \"silent\",\n    \"note\": \"Cheung does not treat čag- at all; his Iranian material for Pok. 522 is exclusively the *sač- family.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Sanskrit\", \"words\": \"saknôti ; siksati ; čakta\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The first two words are exactly Pokorny's: p.522 opens 'Ai. śaknóti „kann, ist imstande, hilft\\\", Desid. śikṣati „hilft, huldigt, dient, lernt\\\"' — so Nourai's saknôti 'he is able to do' and siksati 'he helps, serves' are faithful (he simply writes ś as s, as he does throughout this box). The third form is not. Sanskrit has śaktá- 'able, capable, strong', the past participle of śak-, which Pokorny cites on the same page in the equation 'npers. saxt „hart, fest, sehr\\\" = ai. śakta- „vermögend\\\"' and which Horn no. 723 quotes as 'skr. śaktá- „vermögend\\\"'. There is no Sanskrit *čakta-: an initial č- would presuppose Indo-Iranian *č-, whereas this word begins with the palatal ś from PIE *ḱ. The printed page (pdf 234 / book 204) does show 'čakta', so the JSON is faithful and the error is Nourai's own — a stray háček, all the more visible because the two words above it in the same box are transliterated with plain s. Apart from that letter the node is sound: śaknóti, śikṣati and śaktá- are the three pillars on which Pokorny built the root, and the semantic range 'be able / help / learn / strong' is exactly the root's.\",\n \"derivation_fa\": \"دو واژهٔ نخست دقیقاً از پوکورنی‌اند: صفحهٔ ۵۲۲ چنین آغاز می‌شود: «سنسکریت śaknóti «می‌تواند، تواناست، یاری می‌کند»، صورت آرزویی śikṣati «یاری می‌کند، خدمت می‌کند، می‌آموزد»»؛ پس saknôti و siksati نورایی درست‌اند (او ś را در سراسر این جعبه s می‌نویسد). واژهٔ سوم چنین نیست. در سنسکریت śaktá- «توانا، نیرومند» داریم، اسم مفعولِ ریشهٔ śak-، که پوکورنی در همان صفحه در برابرنهاد «فارسی نو saxt = سنسکریت śakta-» آورده و هرن نیز در شمارهٔ ۷۲۳ آن را «skr. śaktá- «vermögend»» نقل کرده است. صورتی به شکل *čakta- در سنسکریت وجود ندارد؛ چِ آغازین مستلزم *č- هندوایرانی است، حال آنکه این واژه با śِ کامی از *ḱ هندواروپایی آغاز می‌شود. تصویر صفحهٔ چاپی (ص ۲۰۴) نشان می‌دهد که خود کتاب «čakta» چاپ کرده است؛ پس خطا از نورایی است نه از خوانش اسکن — هاچکی سرگردان، که چون دو واژهٔ بالای آن در همان جعبه با s ساده نوشته شده‌اند بیشتر به چشم می‌آید. جز همین یک حرف، گرهٔ درست است. حکم: خطای چاپی کتاب.\",\n \"error_in\": \"book\",\n \"book_prints\": \"čakta\",\n \"correct_form\": \"śaktá- (in Nourai's own system: sakta)\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:522\", \"status\": \"partial\",\n    \"note\": \"POK_02.txt line 2722: 'Ai. śaknóti „kann, ist imstande, hilft\\\", Desid. śikṣati „hilft, huldigt, dient, lernt\\\", śakti- f. „Hilfe\\\", śakra- „vermögend\\\", śagma- „vermögend, hilfreich\\\", śácī f. „Vermögen, Hilfe\\\", śáka- m. „Kraft, Hilfe\\\", śāká- „kräftig, helfend; m. Helfer\\\", śākman- n. „Hilfe\\\"'; and further down 'npers. saxt … = ai. śakta- „vermögend\\\"'. Supports the first two words verbatim and gives the correct form of the third (śakta-, not čakta).\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, kak-¹ (AHD_watkins1985.txt line 572)\", \"stance\": \"supports\",\n    \"note\": \"'Sanskrit śaknoti, he is able, he is strong: SHAKTI, SIKH.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966-67 p.1445 s.v. Sikh (KLN_1966.txt line 35186)\", \"stance\": \"supports\",\n    \"note\": \"'…fr. OI. śikṣati, \\\"studies, learns\\\", desiderative of śaknoti, \\\"is able, is competent\\\".' — Klein's OI śikṣati/śaknoti are Nourai's siksati/saknôti.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 723, p.160\", \"stance\": \"partial\",\n    \"note\": \"'ai. √śak-, śaknoti „vermögen, können\\\", skr. śaktá- „vermögend\\\"' — again śaktá- with ś, not č.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Pahlavi\", \"words\": \"saxt\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The word and its etymology are right; the direction of the arrow is not. Middle Persian saxt [s'ht', sht'] 'firm, strong, violent; very' is the past participle of the same verb as node 1, i.e. Old Iranian *sak-ta-, and Nyberg says so in as many words: 'saxt … pt. of sak- (v. sac-), Skr. pt. śakta- \\\"able, strong\\\"'. MacKenzie has 'saxt [s(')ht] strong, hard, severe(ly); very'. The Sanskrit past participle śaktá- is therefore the exact morphological equivalent of MP saxt — Iranian *-kt- > -xt- as regularly (cf. *bak-ta- > baxt) — but it is a cognate, not an ancestor: no Middle Persian word was borrowed from Sanskrit śakta-, and Pokorny's page states the relation as an equation, 'npers. saxt „hart, fest, sehr\\\" = ai. śakta- „vermögend\\\"', with '=' meaning 'formally identical with'. In Nourai's charts a Sanskrit box is often used as a stand-in for the Indo-Iranian stage, so the tree is defensible as a shorthand; read literally it wrongly makes Persian derive from Sanskrit. The semantic shift is worth noting: 'able, strong' > 'firm, hard' > 'severe, difficult' and, as an adverb, 'very' — already complete in Book Pahlavi.\",\n \"derivation_fa\": \"واژه و ریشه‌شناسی‌اش درست است، جهت پیکان نه. فارسی میانه saxt (املای s'ht'/sht') «استوار، نیرومند، سخت؛ بسیار» اسم مفعولِ همان فعلِ گرهٔ نخست است، یعنی ایرانی باستان *sak-ta-؛ نیبرگ صریحاً می‌نویسد: «saxt … اسم مفعول sak- (نگاه کنید به sac-)، سنسکریت śakta- «توانا، نیرومند»». مکنزی هم دارد: «saxt [s(')ht] نیرومند، سخت، شدید؛ بسیار». پس śaktá-ی سنسکریت هم‌ارزِ ساختاریِ دقیقِ saxt پهلوی است — خوشهٔ *-kt- ایرانی به‌قاعده به -xt- بدل می‌شود (مانند *bak-ta- > baxt) — اما هم‌ریشه است نه نیا: هیچ واژهٔ فارسی میانه‌ای از سنسکریت śakta- وام گرفته نشده، و پوکورنی نیز این نسبت را با نشانهٔ برابری آورده است: «فارسی نو saxt = سنسکریت śakta-». در نمودارهای نورایی جعبهٔ سنسکریت غالباً جانشین مرحلهٔ هندوایرانی است، پس اگر آن را کوتاه‌نویسی بدانیم پذیرفتنی است؛ اگر لفظ به لفظ بخوانیم، فارسی را به‌نادرست زادهٔ سنسکریت می‌نمایاند. تحول معنایی نیز درخور یادآوری است: «توانا، نیرومند» > «استوار، سخت» > «دشوار» و در کاربرد قیدی «بسیار» — که همه در پهلوی کتابی انجام یافته است. حکم: با احتیاط پذیرفتنی.\",\n \"sources\": [W + \"%D8%B3%D8%AE%D8%AA\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1106\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in vol.2, printed p.1106 = BQT_v2_pages.txt \\\\f-leaf 569 (offset leaf + 537 in this stretch, verified against سزا at leaf 600 = p.1137): the سخت cluster (سختانه، سخت بازو، سخت لگام، سخته، سختی) with Mo'in's footnote '… śaknóti (توانستن، قدرت داشتن)، سانسکریت śakta (توانا) — پهلوی saxt … بلوچی sakt (سخت، محکم، استوار) … هوبشمان'. Exactly Nourai's Pahlavi saxt and its Sanskrit equation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.74 s.v. saxt (PHD_mackenzie.txt line 4513)\", \"stance\": \"supports\",\n    \"note\": \"'saxt [s(\\\\')ht N -] strong, hard, severe(ly); very.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. saxt (NYB_vol2_glossary.txt line 3415)\", \"stance\": \"supports\",\n    \"note\": \"'saxt [s\\\\'ht\\\\', sht\\\\'] firm, strong, violent; rich, abundant …; adv. firmly, strongly, violently, fast. — MPrs sat \\\"very\\\"; Pāz. NP saxt; pt. of sak- (v. sac-), Skr. pt. śakta- \\\"able, strong\\\".' — a cognate equation, not a borrowing from Sanskrit.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 723, p.160\", \"stance\": \"supports\",\n    \"note\": \"'sext „hart, fest; sehr\\\" … ai. √śak-, śaknoti …, skr. śaktá- „vermögend\\\"; phlv. saxt, saxtaktum (vd. 19 (47)). bel. sak „hart, stark, fest\\\"; yidg. sukt.'\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"saxt «سخت»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP سخت saxt 'hard, difficult; very' is the direct, unchanged continuation of Book Pahlavi saxt — the word passes from Middle to New Persian without any sound change at all, which is why Pokorny could cite the New Persian form itself as his Iranian witness on p.522 ('npers. saxt „hart, fest, sehr\\\"'). Wiktionary has 'From Middle Persian 𐭮𐭠𐭤𐭨 (saxt)', with the note that the ultimate source is PIE *ḱek- 'to be able'; Horn no. 723 (p.160) gives the same chain with the Balochi cognate sak(t) 'hard, strong, firm' and Yidgha sukt. The semantic development 'able, strong' → 'hard, firm' → 'difficult' is already Middle Persian, and the adverbial 'very' (سخت زیبا 'very beautiful') is inherited from the Pahlavi usage MacKenzie records as 'severe(ly); very'. Nourai's reference SNS:173 is the only loose end: Tavoosi's glossary of Šāyast nē-šāyast is a Pahlavi word-list, and its index (SNS_pages.txt) shows 'saxt 172/8, saxt 173/6, saxtag 172/11-173/10, saxttar 173/9', i.e. p.173 documents the Pahlavi word saxt and its comparative in that text — a citation for the Middle Persian stage rather than for the New Persian one.\",\n \"derivation_fa\": \"«سخت» فارسی نو دنبالهٔ مستقیم و بی‌تغییرِ saxt پهلوی کتابی است؛ این واژه از فارسی میانه به فارسی دری هیچ دگرگونی آوایی ندارد و به همین سبب پوکورنی توانسته است در صفحهٔ ۵۲۲ خودِ صورت فارسی نو را گواه ایرانی خود بیاورد («npers. saxt «سخت، استوار، بسیار»»). ویکی‌واژه می‌نویسد «از فارسی میانه saxt»، و ریشهٔ نهایی را *ḱek- هندواروپایی «توانا بودن» می‌داند؛ هرن نیز در شمارهٔ ۷۲۳ (ص ۱۶۰) همین زنجیره را با هم‌ریشه‌های بلوچی sak(t) «سخت، استوار» و یدغه sukt آورده است. تحول معنایی «توانا، نیرومند» ← «سخت، استوار» ← «دشوار» در فارسی میانه انجام یافته، و کاربرد قیدی آن («سخت زیبا») نیز میراث همان کاربرد پهلوی است که مکنزی «severe(ly); very» ثبت کرده است. تنها نکتهٔ لغزان، ارجاع SNS:173 است: «واژه‌نامهٔ شایست نشایست» طاوسی فرهنگ واژگان پهلوی است و نمایهٔ آن «saxt ۱۷۲/۸، saxt ۱۷۳/۶، saxtag، saxttar ۱۷۳/۹» را نشان می‌دهد، یعنی صفحهٔ ۱۷۳ گواهِ صورت پهلوی است نه فارسی نو. حکم: ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%B3%D8%AE%D8%AA\"],\n \"ref_check\": [\n   {\"ref\": \"SNS:173\", \"status\": \"partial\",\n    \"note\": \"Tavoosi, Vāzhe-nāme-ye Šāyast nē-šāyast: the index in SNS_pages.txt (line 15849 f.) reads 'saxt 172/8 | saxt 173/6 | saxtag 172/11-173/10 | saxttar 173/9', and the glossary body (\\\\f-leaf 103) carries the entries saxt/saxtag. So p.173 does document saxt, but as a Pahlavi form in the Šāyast nē-šāyast text, not as a New Persian word; the OCR of this volume is too poor to read the printed page numbers directly.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn no. 723, p.160 (HRN.txt \\\\f-leaf 182)\", \"stance\": \"supports\",\n    \"note\": \"'723. sext „hart, fest; sehr\\\" … phlv. saxt … bel. sak „hart, stark, fest\\\" (383); yidg. sukt.'\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in vol.2 p.1105 f. (leaf 568), footnote to سخت\", \"stance\": \"supports\",\n    \"note\": \"'سخت … بمعنی درشت و تنگ و دشوار … ومعنی محکم هم هست که نقیض نرم و سست است' with the footnote giving śaknóti '(توانستن، قدرت داشتن)', سانسکریت śakta '(توانا)', پهلوی saxt, بلوچی sakt.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. saxt\", \"stance\": \"supports\",\n    \"note\": \"'strong, hard, severe(ly); very' — the Middle Persian ancestor with the identical semantic range.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"Sikh\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English Sikh (in English from 1780s, of the Punjabi religious community founded by Gurū Nānak c.1500) does go back to this root, and the American Heritage Dictionary — the very work Nourai cites as AHD:1205 — spells out the chain in its entry: 'Sikh … [Hindi, from Sanskrit śiṣyaḥ, disciple, from śikṣati, he wishes to learn, desiderative of śaknoti, is able.]' Watkins' IE appendix files the word under the same root: 'kak-¹. To enable, help. Sanskrit śaknoti … : SHAKTI, SIKH. [Pok. kak- 522.]' Klein agrees: 'Sikh … Hind., lit. \\\"disciple\\\", fr. OI. śikṣati, \\\"studies, learns\\\", desiderative of śaknoti, \\\"is able, is competent\\\".' The immediate donor is not literally Hindi but Punjabi ਸਿੱਖ sikkh, which Wiktionary derives from Prakrit sikkhā < Sanskrit śikṣā 'instruction, teaching' — the noun of the same desiderative — while Hobson-Jobson (s.v. SIKH, SEIKH) takes it 'from Skt. śiṣya' 'a disciple'. Either way the word rests on the desiderative śikṣ- of śak-, so the arrow from the Sanskrit box is right; only the label 'English' hides the Indic transmission (Sanskrit → Prakrit/Punjabi → Anglo-Indian English of the Company period).\",\n \"derivation_fa\": \"واژهٔ انگلیسی Sikh (از دههٔ ۱۷۸۰ در انگلیسی، نام پیروان آیینی که گورو نانَک در حدود ۱۵۰۰ میلادی در پنجاب بنیاد نهاد) به‌راستی به همین ریشه بازمی‌گردد، و فرهنگ American Heritage — همان که نورایی با نشان AHD:1205 یاد کرده — زنجیره را چنین می‌آورد: «Sikh … [هندی، از سنسکریت śiṣyaḥ «شاگرد»، از śikṣati «می‌خواهد بیاموزد»، صورت آرزوییِ śaknoti «تواناست»]». واتکینز نیز در پیوست ریشه‌های هندواروپایی همین واژه را ذیل «kak-¹ توانا کردن، یاری کردن … : SHAKTI, SIKH» نهاده است، و کلاین می‌نویسد: «Sikh … هندی، به‌معنای «شاگرد»، از سنسکریت śikṣati «می‌آموزد»، صورت آرزوییِ śaknoti». وام‌دهندهٔ بی‌واسطه در واقع پنجابی سیکْھ (sikkh) است که ویکی‌واژه آن را از پراکریت sikkhā و سنسکریت śikṣā «آموزش» می‌گیرد، حال آنکه هابسن-جابسن آن را از śiṣya «شاگرد» می‌داند؛ در هر دو حالت پایه، صورت آرزوییِ śikṣ- از ریشهٔ śak- است. پس پیکان از جعبهٔ سنسکریت درست است؛ تنها برچسب «انگلیسی» مرحلهٔ هندی/پنجابی را پنهان می‌کند. حکم: ادعای نورایی درست است.\",\n \"sources\": [AHD_SIKH, \"https://en.wiktionary.org/wiki/Sikh\", \"https://en.wiktionary.org/wiki/%E0%A8%B8%E0%A8%BF%E0%A9%B1%E0%A8%96\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1205\", \"status\": \"supports\",\n    \"note\": \"The 1975 New College Edition is not on disk, but the same dictionary's current online text (ahdictionary.com, s.v. Sikh) has '[Hindi, from Sanskrit śiṣyaḥ, disciple, from śikṣati, he wishes to learn, desiderative of śaknoti, is able.]', and the Watkins appendix bound with that edition lists SIKH under 'kak-¹' (AHD_watkins1985.txt line 572). Nourai's page reference is to the alphabetical entry, which says exactly what his arrow says.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966-67 s.v. Sikh (KLN_1966.txt line 35186)\", \"stance\": \"supports\",\n    \"note\": \"'Sikh, n., member of a Hindu religious community founded by Guru Nanak about the end of the 16th cent. — Hind., lit. \\\"disciple\\\", fr. OI. śikṣati, \\\"studies, learns\\\", desiderative of śaknoti, \\\"is able, is competent\\\".'\"},\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson 1903 s.v. SIKH, SEIKH (HJB.txt line 20187)\", \"stance\": \"partial\",\n    \"note\": \"'SIKH, SEIKH, n.p. Panjabi-Hind. Sikh, \\\"a disciple,\\\" from Skt. Sishya' — same root family, but Yule/Burnell route it through śiṣya rather than śikṣati.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, kak-¹\", \"stance\": \"supports\",\n    \"note\": \"'kak-¹. To enable, help. Sanskrit śaknoti, he is able, he is strong: SHAKTI, SIKH. [Pok. kak- 522.]'\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Old English\", \"words\": \"haeccan\",\n \"verdict\": \"disputed\",\n \"derivation\": \"This is the one branch of the chart that modern scholarship does not accept. Two things are wrong with it. First, Old English hæccan is not attested: the earliest form is Middle English hacchen (early 13c.), and every dictionary that posits an Old English antecedent marks it with an asterisk — AHD5 s.v. hatch² '[Middle English hacchen, from Old English *hæccan.]', Etymonline 'probably from an unrecorded Old English *hæccan, of unknown origin'. Nourai prints 'haeccan' with no asterisk, so his box asserts an attested word that does not exist. Second, and more important, the attachment to *k̂ak- is not the modern view. Pokorny does mention it on p.522 — that much of the citation is honest — but under an explicit hedge: 'unsicher auch ags. hagan „genitalia\\\", mhd. hagen „Zuchtstier\\\" … nhd. hecken „sich paaren (von Vögeln)\\\", engl. hatch „brüten\\\", ahd. hegidruosa „Hode\\\"', and he goes on to say that the whole Germanic set is doubtful 'weil nie -k-, sondern nur -g- im Wurzelauslaut'. Walde-Pokorny I 334, Pokorny's own source, does not even list it here: it gives these words a separate head-entry, 'kak- „männliche Geschlechtsteile\\\"?', and mentions the link with śaknóti only as Schrader's suggestion, 'erwägenswert'. Klein derives hatch from the same Germanic group (MHG/G hecken 'to hatch, breed', OHG hegidruosa 'testicle') and compares Latvian kakale 'membrum', with no Indo-Iranian connection; Skeat derives it from the noun hatch 'coop' ('From the coop or hatch in which the motherbird sits'); Watkins' appendix — Nourai's own AHD — does not list hatch under kak-¹ at all. The modern verdict is therefore: a Germanic breeding-word of uncertain origin, most probably belonging with hecken/hagen, and not derivable from PIE *ḱek- 'to be able'.\",\n \"derivation_fa\": \"این تنها شاخهٔ نمودار است که پژوهش امروزی نمی‌پذیرد، و دو اشکال دارد. نخست آنکه صورت انگلیسی باستانِ hæccan گواه ندارد: کهن‌ترین صورت، انگلیسی میانهٔ hacchen (اوایل سدهٔ سیزدهم) است و هر فرهنگی که نیای انگلیسی باستان برای آن فرض می‌کند، ستاره می‌گذارد — AHD ویرایش پنجم: «[انگلیسی میانه hacchen، از انگلیسی باستان *hæccan]»؛ اتیمانلاین: «احتمالاً از *hæccanِ ناگواه در انگلیسی باستان، با خاستگاه ناشناخته». نورایی «haeccan» را بی‌ستاره چاپ کرده و چنین می‌نماید که واژه‌ای گواهمند است. دوم و مهم‌تر آنکه پیوند آن با ریشهٔ *k̂ak- دیدگاه امروزی نیست. پوکورنی در ص ۵۲۲ آن را یاد می‌کند — و از این حیث ارجاع نورایی صادقانه است — اما با قیدِ صریحِ «نامطمئن»، و می‌افزاید که کل این گروه ژرمنی مشکوک است «زیرا در پایان ریشه هرگز -k- نیست بلکه تنها -g- است». والده-پوکورنی (جلد ۱، ص ۳۳۴)، یعنی مأخذ خودِ پوکورنی، این واژه‌ها را اصلاً اینجا نیاورده و مدخل جداگانه‌ای برایشان ساخته است: «kak- «اندام‌های نرینه»؟»، و پیوند با śaknóti را تنها پیشنهاد شرادر و «درخور تأمل» می‌خواند. کلاین hatch را با همان گروه ژرمنی (آلمانی hecken، آلمانی باستان hegidruosa «بیضه») و لتونیایی kakale می‌سنجد، بی‌هیچ پیوند هندوایرانی؛ اسکیت آن را از اسمِ hatch «قفس مرغ» می‌گیرد؛ و پیوست واتکینز — همان AHD که نورایی به آن استناد می‌کند — hatch را اصلاً ذیل kak-¹ نیاورده است. حکم: پژوهش امروزی این را رد می‌کند و hatch را واژه‌ای ژرمنی با خاستگاه نامعلوم، احتمالاً هم‌خانوادهٔ hecken، می‌داند.\",\n \"sources\": [ETY_HATCH, AHD_HATCH],\n \"ref_check\": [\n   {\"ref\": \"POK:522\", \"status\": \"partial\",\n    \"note\": \"Pokorny 522 does contain 'engl. hatch „brüten\\\"', but inside the clause 'unsicher auch ags. hagan „genitalia\\\", mhd. hagen „Zuchtstier\\\", nhd. dial. hegel ds., haksch „Zuchtschwein\\\", nhd. hecken „sich paaren (von Vögeln)\\\", engl. hatch „brüten\\\", ahd. hegi-druosa „Hode\\\"', followed by 'Ebenso, weil nie -k-, sondern nur -g- im Wurzelauslaut, die germ. Sippe …'. He cites no Old English hæccan; his Old English form is hagan 'genitalia'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 334 (WLD_Bd1_pages.txt lines 31624-31632)\", \"stance\": \"contradicts\",\n    \"note\": \"Separate head-entry: 'kak- „männliche Geschlechtsteile\\\"? Ags. hagan „genitalia\\\", mhd. hagen „Zuchtstier\\\", nhd. mdartl. hegel ds., haksch „Zuchtschwein\\\", nhd. hecken „sich paaren (von Vögeln)\\\", engl. hatch, ahd. hegidruosa „Hode\\\" … Unsicher, und auch wegen des beschränkten Verbreitungsgebietes kaum als sehr alt zu betrachten. Schrader … stellt hagen hegel zu ai. śaknoti „vermag\\\", śakrá- „kräftig\\\", erwägenswert.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966-67 s.v. hatch (KLN_1966.txt line 17284)\", \"stance\": \"contradicts\",\n    \"note\": \"'hatch, tr. and intr. v., to produce (young) from eggs by incubation. — ME. hacchen, rel. to MHG., G. hecken, \\\"to hatch, breed\\\", OHG. hegidruosa … MHG., G. hagen, \\\"bull kept for breeding\\\", and cogn. with Lett. kakale, \\\"membrum\\\".' No Old English form, no Indo-Iranian cognates.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Hatch (2) (SKT.txt line ~8416)\", \"stance\": \"contradicts\",\n    \"note\": \"'hatch (2), to produce a brood by incubation. (E.) From the coop or hatch in which the motherbird sits. Thus Swed. häcka, to hatch, from häck, a coop; Dan. hækkebuur, a breeding-cage, from hække, a rack.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, kak-¹ and the k-list generally\", \"stance\": \"silent\",\n    \"note\": \"The appendix lists only SHAKTI and SIKH under kak-¹; hatch appears nowhere under it.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"English\", \"words\": \"hatch\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Taken on its own the arrow is right: Modern English hatch 'to bring forth young from an egg' continues Middle English hacchen (early 13c. hachen 'to produce young from eggs by incubation'), and the standard dictionaries reconstruct behind it an Old English *hæccan — AHD5 s.v. hatch² gives simply '[Middle English hacchen, from Old English *hæccan.]', which is the entry Nourai cites as AHD:603 (the page of hatch in the 1975 New College Edition), and Etymonline agrees. The senses developed inside English: 'come forth from an egg' and the causative 'cause to come forth' by the late 14c., and the figurative 'to hatch a plot' already early 14c. What the node inherits from its parent, however, is node 8's problem: the Old English antecedent is unattested and the further connection to PIE *ḱek- is rejected by Klein, Skeat, Watkins and Etymonline alike. This English box duplicates nothing else on the page; it is simply the modern reflex of the Germanic word.\",\n \"derivation_fa\": \"اگر این پیکان را جدا بسنجیم درست است: انگلیسی امروزی hatch «جوجه از تخم بیرون آوردن» دنبالهٔ انگلیسی میانهٔ hacchen (اوایل سدهٔ سیزدهم، hachen «با خوابیدن بر تخم جوجه آوردن») است و فرهنگ‌های معیار در پسِ آن صورت انگلیسی باستانِ *hæccan را بازمی‌سازند — AHD ویرایش پنجم ذیل hatch² تنها می‌نویسد «[انگلیسی میانه hacchen، از انگلیسی باستان *hæccan]»، و همین مدخل است که نورایی با نشان AHD:603 (صفحهٔ hatch در ویرایش ۱۹۷۵) به آن ارجاع داده؛ اتیمانلاین نیز همین را می‌گوید. تحول معنایی درون خود انگلیسی رخ داده است: «از تخم بیرون آمدن» و صورت سببی آن در اواخر سدهٔ چهاردهم، و کاربرد مجازی «توطئه پختن» از اوایل همان سده. اما اشکالِ گرهٔ پیشین به این گره نیز به ارث می‌رسد: نیای انگلیسی باستان گواه ندارد و پیوند دورتر با ریشهٔ هندواروپایی *ḱek- را کلاین، اسکیت، واتکینز و اتیمانلاین یکسره رد می‌کنند. حکم: خودِ گام «انگلیسی میانه ← انگلیسی نو» درست است.\",\n \"sources\": [AHD_HATCH, ETY_HATCH],\n \"ref_check\": [\n   {\"ref\": \"AHD:603\", \"status\": \"supports\",\n    \"note\": \"The 1975 New College Edition is not on disk; the same dictionary's current text (ahdictionary.com, s.v. hatch) has 'hatch² … v. intr. To emerge from an egg … [Middle English hacchen, from Old English *hæccan.]' (and hatch¹ 'small door … from Old English hæc, hæcc'). It supports the English word and the Old English antecedent, but gives it no Indo-European root reference.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966-67 s.v. hatch\", \"stance\": \"supports\",\n    \"note\": \"'hatch, tr. and intr. v., to produce (young) from eggs by incubation. — ME. hacchen…' — the same English chain, different ultimate etymology.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Hatch (2)\", \"stance\": \"partial\",\n    \"note\": \"Confirms the English word and its meaning but derives it from the noun hatch 'coop'.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict. (WEB_vol1.txt)\", \"stance\": \"silent\",\n    \"note\": \"Not consulted successfully: the volume on disk covers only part of the alphabet and no hatch entry was retrieved.\"}\n ]\n})\n\npart1 = json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part1.json'))\npart1[\"entries\"].append(e4)\nwith open('/home/sfmqrb/git/rishe/data/verification/page-234.json','w',encoding='utf-8') as f:\n    json.dump(part1, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build234b.py"
}
```


### [2026-09-06T15:57:37.741Z] TOOL RESULT

```
written
```


## [2026-09-06T15:57:42.411Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -m json.tool data/verification/page-234.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 234"
}
```


### [2026-09-06T15:57:44.739Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'plausible': 5, 'confirmed': 7, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'disputed': 1, 'transcription_suspect': 1, 'confirmed': 1}
ref checks: {'supports': 15, 'partial': 5}
books consulted: {'silent': 11, 'supports': 23, 'partial': 8, 'contradicts': 4} | by book: {'HRN': 6, 'PHD': 5, 'KLN': 5, 'BRT': 5, 'BQT': 4, 'NYB': 3, 'CHEUNG': 3, 'AHD': 3, 'MON': 2, 'WLD': 2, 'SKT': 2, 'AFM': 1, 'SOD': 1, 'ISS': 1, 'KNT': 1, 'HJB': 1, 'WEB': 1}
```


## [2026-09-06T15:58:01.879Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-234.json` written, `verify_check.py 234` reports **0 PROBLEM lines** (14/14 nodes).

**Page 234 (book 204) — 3 non-redirect entries, 14 nodes**

- Node verdicts: 7 confirmed, 5 plausible, 1 disputed, 1 transcription_suspect
- Root verdicts: 1 confirmed (Kak 1), 1 disputed (Kagaš), 1 transcription_suspect (Kahrpu)
- Ref checks: 15 supports, 5 partial, 0 contradicts/not_found. Every reference Nourai cites was located: SIN:559, PLA:225, BQT:1569/1612/1106/1137, SOD:193, MON (only via the 2-vol abridgement), POK:522, HRN:152/160/162, FFD:58, SNS:173, AHD:1205/603.

Flagged items:
- **ROOT Kagaš (Turkish "tree bark") — disputed.** SIN:559 supports Nourai word-for-word (it is Laufer 1919), but modern scholarship (Gharib in EIr; Wiktionary) derives NP کاغذ from Sogdian kʾγδʾ *kāγaδā*, possibly ultimately Old Chinese 紙; Mo'in tags کاغذ "[از چی.]". "Turkish" is also the wrong label for Laufer's Old Uyghur / Altai-Siberian evidence.
- **ROOT Kahrpu, Kharpuna — transcription_suspect (error in the BOOK).** Avestan is *kahrpuna-* (Bartholomae col. 455 f.); the printed page really shows "Kharpuna", a metathesis misprint for "Kahrpuna". Extraction is faithful.
- **#4 Sanskrit "čakta" — transcription_suspect (error in the BOOK).** Sanskrit is *śaktá-*; the printed page shows "čakta" with a stray háček, while the two words above it in the same box use plain s. Extraction faithful.
- **#8 Old English "haeccan" → hatch — disputed.** OE *hæccan is unattested (no asterisk in the book); Pokorny lists Engl. *hatch* at 522 only as "unsicher", Walde-Pokorny I 334 puts it under a separate root, and Klein, Skeat, Etymonline and Watkins' own AHD appendix all decline the *ḱek- connection.

No extraction errors found: every node, word, script form and quote in `data/extracted/batch/page-234.json` matches the printed page. One observation for the owner: the printed chart has an **empty, unlabelled box** to the right of the Avestan čagad node (entry 4) — nothing to extract, but it is absent from both the JSON and the chart text.

Page image saved for audit at `data/verification/sources/refs/ocr/BOOK/234.png`; 11 web sources archived via `fetch_source.py` (3 of them returned 404/JS-shell and are not cited).
