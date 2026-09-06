# Verification process log — verify-page-280


## [2026-09-06T21:29:55.040Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 280 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-280.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-280.json. Write /home/sfmqrb/git/rishe/data/verification/page-280.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 280` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:29:56.464Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T21:29:57.154Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:29:57.171Z] TOOL RESULT

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


## [2026-09-06T21:29:57.412Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-280.txt"
}
```


### [2026-09-06T21:29:57.433Z] TOOL RESULT

```
1	=== PDF page 280 (book page 250) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ksero : dry  (refs POK:625)
4	#1 (parent #0) [Greek] refs=POK:625; AHD:424 | xěros : dry powder, medicine
5	  #2 (parent #1) [Arabic] refs=AHD:424 | al-iksir : elixir ☞Al3
6	    #3 (parent #2) [Persian] refs=MON:331 | eksîr «اکسیر» : elixir
7	    #4 (parent #2) [French] refs=DEV:108 | 
8	      #5 (parent #4) [English] refs=KLN:509 | elixir
9	  #6 (parent #1) [English] refs=KLN:1757 | xer-, xero- : dry ; xeroderma : roughness of the skin
10	#7 (parent #0) [Latin] refs=KLN:1422 | serenus : clear, calm sky
11	  #8 (parent #7) [English] refs=None | serene, serenity
12	  #9 (parent #7) [French] refs=None | serenade : music played at night
13	    #10 (parent #9) [English] refs=None | serenade
14	--- entry 1 ---
15	ROOT [Indo-European] Kseubh : to shake, rock, disturb  (refs POK:625)
16	#1 (parent #0) [Avestan] refs=POK:625; FFD:26 | xšaob, xšufsan : disturbance ; xšaub : to shake ; â-xšuf-ta : disturbed ; â-xšaub-a : disturbance
17	  #2 (parent #1) [Pahlavi] refs=ISS:11 | âšŭp ; âšŭptak
18	    #3 (parent #2) [Persian] refs=POK:625; BQT:45; MON:2988; FFD:26 | âšŭb «آشوب» : disturbance ; âšoftan «آشفتن (آشفته)» : to be disturbed ; kašoftan, kašaftan «کَشُفتن» : to disturb | extra: کَشفت ، کَشفتگی
19	--- entry 2 ---
20	ROOT [Indo-European] Kseud, Qseud : water, to clean by stamping in water  (refs POK:625; WLD1:502)
21	#1 (parent #0) [Avestan] refs=POK:625; WLD1:502 | xšaod, xšaud : flow ; xšudra : water, liquid, semen ; xšâudra : male, husband ; xšvîd : milk ; svěstas : butter
22	  #2 (parent #1) [Persian] refs=HRN:172,177; BQT:1267,1312; FFD:63 | šostan «شستن» : to clean, wash ; šǔy «شوی ۲ ( شوهر ، شو ، زناشوئی )» : husband | extra: شوی ۱ ، رختشوی ، شور ۲
23	
```


## [2026-09-06T21:30:01.085Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-280.json",
 "description": "Read source JSON page 280"
}
```


### [2026-09-06T21:30:01.141Z] TOOL RESULT

```
{
  "pdf_page": 280,
  "book_page": 250,
  "entries": [
    {
      "root": {
        "name": "Ksero",
        "lang": "Indo-European",
        "refs": "POK:625",
        "gloss": "dry"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:625; AHD:424",
          "words": [
            {"translit": "xěros", "gloss": "dry powder, medicine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "AHD:424",
          "words": [
            {"translit": "al-iksir", "gloss": "elixir", "script": null, "see": ["Al3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:331",
          "words": [
            {"translit": "eksîr", "gloss": "elixir", "script": "اکسیر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "جز قلب تیره نشد هیچ حاصل و هنوز - باطل در این خیال که اکسیر میکنند", "poet": "Hâfez"}
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "French",
          "refs": "DEV:108",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:509",
          "words": [
            {"translit": "elixir", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:1757",
          "words": [
            {"translit": "xer-, xero-", "gloss": "dry", "script": null},
            {"translit": "xeroderma", "gloss": "roughness of the skin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:1422",
          "words": [
            {"translit": "serenus", "gloss": "clear, calm sky", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "serene, serenity", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "serenade", "gloss": "music played at night", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "serenade", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kseubh",
        "lang": "Indo-European",
        "refs": "POK:625",
        "gloss": "to shake, rock, disturb"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:625; FFD:26",
          "words": [
            {"translit": "xšaob, xšufsan", "gloss": "disturbance", "script": null},
            {"translit": "xšaub", "gloss": "to shake", "script": null},
            {"translit": "â-xšuf-ta", "gloss": "disturbed", "script": null},
            {"translit": "â-xšaub-a", "gloss": "disturbance", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "ISS:11",
          "words": [
            {"translit": "âšŭp", "gloss": null, "script": null},
            {"translit": "âšŭptak", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:625; BQT:45; MON:2988; FFD:26",
          "words": [
            {"translit": "âšŭb", "gloss": "disturbance", "script": "آشوب"},
            {"translit": "âšoftan", "gloss": "to be disturbed", "script": "آشفتن (آشفته)"},
            {"translit": "kašoftan, kašaftan", "gloss": "to disturb", "script": "کَشُفتن"}
          ],
          "script_extra": "کَشفت ، کَشفتگی",
          "note": null,
          "quote": {"text": "یکی را خانهٔ شادی کَشُفته - یکی را باغ پیروزی شکُفته", "poet": "Vîs-o-Râmîn"}
        }
      ]
    },
    {
      "root": {
        "name": "Kseud, Qseud",
        "lang": "Indo-European",
        "refs": "POK:625; WLD1:502",
        "gloss": "water, to clean by stamping in water"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:625; WLD1:502",
          "words": [
            {"translit": "xšaod, xšaud", "gloss": "flow", "script": null},
            {"translit": "xšudra", "gloss": "water, liquid, semen", "script": null},
            {"translit": "xšâudra", "gloss": "male, husband", "script": null},
            {"translit": "xšvîd", "gloss": "milk", "script": null},
            {"translit": "svěstas", "gloss": "butter", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:172,177; BQT:1267,1312; FFD:63",
          "words": [
            {"translit": "šostan", "gloss": "to clean, wash", "script": "شستن"},
            {"translit": "šǔy", "gloss": "husband", "script": "شوی ۲ ( شوهر ، شو ، زناشوئی )"}
          ],
          "script_extra": "شوی ۱ ، رختشوی ، شور ۲",
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T21:30:01.201Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T21:30:01.244Z] TOOL RESULT

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


## [2026-09-06T21:30:21.531Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','KLN','DEV','MON','BQT','HRN','ISS','FFD','LKT','SKT','LEW','LAT','IEC','SYN','HUB','CHEUNG','BRT','PHD','NYB','ARY','FSD','WEB','PHN']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-06T21:30:22.135Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && head -60 data/verification/page-259.json"
}
```


### [2026-09-06T21:30:23.245Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

CHEUNG null

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
```


### [2026-09-06T21:30:23.279Z] TOOL RESULT

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
  "pdf_page": 259,
  "book_page": 229,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-06",
  "entries": [
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
          "where": "Watkins 1985, s.v. kerd-1 (AHD_watkins1985.txt line 621)",
          "stance": "supports",
          "note": "'kerd-1. Heart. 1. Suffixed form *kerd-en- in Germanic *hertōn- in Old English heorte, heart: HEART. 2. Zero-grade form *kr̥d- in: a. Latin cor (stem cord-), heart … b. suffixed form *kr̥d-yā in Greek kardia … 3. Possibly *kred-dhə-, “to place trust” … in Latin crēdere, to believe. [Pok. kered- 579.]' — the whole chart in one entry."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny I 423 f. (cited by POK and by Buck 4.44; only Band III index available locally, WLD_band3.txt line 2965 'kerd- 423')",
          "stance": "supports",
          "note": "Both Pokorny and Buck refer the 'heart' root to WP. I 423 f.; the local library holds only the Register volume, whose index line points to that page."
        },
        {
          "src": "IEC",
          "where": "Mann, s.vv. Kerd- and Kr̥d- (IEC.txt lines 8676, 9088)",
          "stance": "supports",
          "note": "'Kerd- (Kerdis, ā, io) “heart, core, centre”. Cf. Kr̥d-. WP I, 424' and 'Kr̥d- (Kr̥ds, Kr̥diiom, iio) “core, centre, heart” … Hitt. kar-, ds kardi … Gk. kardia; Lat. cor, gs cordis …'"
        },
        {
          "src": "LAT",
          "where": "Ernout–Meillet p.254–255 s.v. cor (LAT.txt leaf 272–273)",
          "stance": "partial",
          "note": "'Le nom du “coeur” … est au fond le même dans toutes les langues indo-européennes. Il est probable que le nominatif-accusatif était de la forme *ḱerd, conservée dans hitt. kir … gr. κῆρ, v.pruss. seyr, et que les autres cas reposaient sur *ḱr̥d-'; but adds 'Pour le rapport qu'on a envisagé, sans raison, avec crēdō, v. ce mot' — i.e. rejects the 'Kred' half."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
```


## [2026-09-06T21:30:27.591Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','DEV','HRN','FFD','BQT','MON','ISS','WLD']:\n    print(k, d[k].get('page_offset'))\n    print('   hint:', str(d[k].get('lookup_hint'))[:400])\n    print('   local:', d[k].get('local_file'))\n    print()\n\""
}
```


### [2026-09-06T21:30:29.323Z] TOOL RESULT

```
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-d
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt

KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt

DEV leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: French headword in caps at line start.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt

HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt

FFD 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
   hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt']

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
   hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']

MON None
   hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']

ISS DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.
   local: None

WLD Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
   hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt']
```


## [2026-09-06T21:30:33.042Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"lemma: kse\" POK_full.txt | head -20; echo \"=== page 625 refs ===\"; grep -n \"Page(s): 62[456]\" POK_full.txt | head -20"
}
```


### [2026-09-06T21:30:33.102Z] TOOL RESULT

```
48832:Root / lemma: kseip-, kseib- 
48854:Root/ lemma: kseiJo^-{*ghseiJo'^-) 
48878:Root / lemma: kseud- {*gheud-) 
=== page 625 refs ===
47237:Page(s): 626 
48792:Page(s): 624 
48830:Page(s): 624 
48848:Page(s): 625 
48852:Page(s): 625 
48874:Page(s): 625 
48905:Page(s): 625 
48966:Page(s): 626 
51227:Page(s): 626 
51938:Page(s): 624 
51960:Page(s): 624 
51984:Page(s): 625 
52364:Page(s): 626-627
```


## [2026-09-06T21:30:33.224Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==281' POK_02.txt | head -80"
}
```


### [2026-09-06T21:30:34.731Z] TOOL RESULT

```
dryes  RC  44,  313  ff.,  Specht  KZ.  68,  193  ff.  wäre  idg.  *Ä:^erp! tabuistische  Metathese  zu  ^perk^:.-  ,Leben,  Welt,  Eiche*  (got.  fairhus ,Welt*).
WP.  I  486  f.,  WH.  I  277  f.
2.  krep-  s.  oben  S.  567  ff.  unter  1.  ker-.
1,  krep-  ,stark,  fest*;  nur  germ.  und  slav.
Aisl.  hrcefa  ,ertragen*  (vgl.  russ.  krepithsja  ,ausdauern,  beharren*);  abg. krep^,  kräp^k^  ,f est,  stark* ;
cymr.  craff  ,schnell*  aus  aisl.  krappr  ds.  (=  krappr  ,engS  S.  388). WP.  I  487.
2.  krep-  s.  oben  S.  581  unter  kerdp-,
I.  kret-  , schütteln*  (ob  als  ,stoßen*  mit  kret-  , schlagen*  identisch?  oder  Er- weiterung von  sker-  , drehen,  kreisend  schwingen*?).
Lit.  kreciüj  krSsti  , schütteln,  schüttelnd  streuen*,  Iter.  kratau,  -yti  ds., kretü  kreteti  ,sich  hin  und  her  bewegen,  sich  schütteln,  schlottern*,  lett. krest  ,schütteln*,  Iterat.  kratit,  kr^tulis  ,Art  Sieb*  (lett.  kraitdt  ,taumeln* Entgleisung  von  einem  *krit-  aus) ;
mir.  crothaim  ,schüttle*,  gall.-rom.  '^■crottiäre  ,schütteln* ;
ahd.  redan  ,sieben*,  nhd.  mdartl.  räder,  rädel  ,Sieb*;  aisl.  hradr  ,schnell*, ags.  ArcBjb,  hrcßd  ,schnell,  behend*,  engl,  rather  ,lieber*,  ahd.  hrad,  hrat ,velox,  strenuus* ;  aisl.  hrceda  ,erschrecken  (trans.)*,  hrceddr  ,entsetzt* ;
auch  ags.  ä-hreddan  ,befreien,  retten*,  ahd.  retten  ,bewegen,  treiben; befreien,  retten'  als  ,von  der  Gefahr  wegstoßen*?
WP.  I  484,  Mühlenbach-Endzelin  II  274,  261,  256.
621
jcret'  »schlagen*;  wohl  ursprünglich  mit  1.  Jcret-  identisch.
Qr.  y.QÖTog  ,jedes  durch  Schlagen,  Stampfen,  Klatschen  entstehende Geräusch*;  %Qoreiv  ,klatschen,  klopfen,  schlagen*, x^dra^oi^, Klapper',  yiQÖzacpog ^Schläfe*  (eigentlich  ,*das  Klopfen*);  ,Berghang;  Seite*,  ^qoxacpig  ,Spitz- hammer* ;
dazu  mit  ursprüngl.  wohl  bloß  präsentischer  Nasalierung  aisl.  hrinda, hrattj  ags.  hrindan,  hi^and  ,stoßen*;
vielleicht  die  slav.  Sippe  von  ahg.  krostg^  krotiti  ,zähmen*,  krot^k^  ,sanft, mild,  mäßig*,  wenn  ursprüngl.  , durch  Prügeln  mürbe  machen'?
WP.  I  484  f.,  Berneker  624.
X.  kreu-,  kreuo-ikrü-  1.  ,dickes,  stockendes  Blut,  blutiges,  rohes  Fleisch*, vermutlich  ,g
```


## [2026-09-06T21:30:38.061Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '48780,48980p' POK_full.txt"
}
```


### [2026-09-06T21:30:38.113Z] TOOL RESULT

```
probably to Lithuanian karka " Sehweinefuf^, Vorderbein des Sehweines ', ablaut. East 
Lithuanian kirkalism. 'stilt'; 

Slavie *korkai. in sloven, kraka, kraca^ Sehweinefufl '; 

besides Slavie *kork-b in Bulgarian Ara/rMeg, foot', russ. d/ro/'o/r'ham'; in addition ablaut. 
Slavie *krok-b m. in Serbo-Croatian krdk{Gev\. kroka), Czeeh krok^ footstep ' and Slavie 
*korak-b m. in Serbo-Croatian korak sloven. korak6s. 

Quite unelear the ablaut relation. 

References: WP. I 488, Trautmann 118. 
Page(s): 624 

Root / lemma: krom- 

Meaning: wooden fenee, ete.. 

Note: only Germanie and Slavie 

Material: Old leelandie hremma 'catch, elamp ', Old English hremman' tighten, restriet, 

hinder' (probably from '*fenee'). Old Frisian hrembend '{r\anac\e', Duteh remmen' restrain, 

bloek (a wheel) ' ("*with a beam'), presumably also Old leelandie hrefni' the lowest plank 

above the ship ground ' and Gothie hramjan' cxwc\\)i ' (as ' an ein Gestell heften '); 



russ. kr6myP\. "loom', zakromftb' mit Brettern umstellen ', kir. prykromyty'tame, 
domestieate', russ. 5-Ard/77/7>y" blushful' ete. (eommon Slavie alb. k- > sk- , shk-). 

References: WP. I 487 f. 
Page(s): 623-624 

Root / lemma: krut- 

Meaning: protuberanee; breast; belly 



Material: Middle Irish crotti. " hunch, harp', nir. emit 6s., altbrit.-gall. c/c/Za'harp', cymr. 
crwthm. " hunch, fiddle, violin', crothi. "belly, uterus, vulva'; 

Lithuanian krut'is^ female breast', /r/77///7e "breast', Latvian kruts^\\\\\, breast'. 

Probably to kreu-^ curve ', see below (s)ker-, (s)kereu-^\.uxy\\ 

References: WP. I 485, 489, Specht Indo Germanic Dekl. 772. 
Page(s): 624 

Root / lemma: kseip-, kseib- 

Meaning: to throw, be thrown 

Material: Old Indie ksipati^ throws, flings ', Kaus. ksepayati, ks/pra-h ' qu'\ck, fast'; with 

voiced-nonaspirated Old Church Slavic osiba-jg, -ti^ avert, prevent; turn away ', russ. 

s/t>atb'\hro\N\ s/My "quick, fast', os/batb'chop, cut, reject', os/batbsja' wander'. 

common Old Indie gh- > ks- : Old pers. gh- > xs- : npers. xs- > s- 

Hence Slavic xs- > s- is of npers. origin. 

References: W P. I 501. 

Page(s): 625 

Root / lemma: ks-en-, ks-es- ks-eu- 
See also: see above S. 585 f. under kes- 
Page(s): 625 

Root/ lemma: kseiJo^-{*ghseiJo'^-) 

Meaning: to sway, swing 

Material: Old Indie ksubhyati, ksobhate {ksubhnoti, -nati) " sways, trembles ', ksobhayati^ 

sets in motion ', ksobha-m. " sway, tremor '; Avestan xsaob-'go into raptures, become 

excited ' {xsufsqn), npers. a-suftan, a-softan^ in Bewegung versetzen ', a-sdi? "perplexity, 

tumult '; 

common Old Indie gh- > ks- : Old pers. gh- > xs- : npers. xs- > s- 

poln. chybac^ swing, move to and fro '; chybkT nimble, agile; graceful; sharp, keen, 
rash, hasty'; kir. chybaty^ be ambivalent, have mixed feelings ', chyba {*ksuba) "lack, fault, 
error' etc. 

common Old Indie gh- > ks- : Slavic gh- > ch- 
References: WP. I 502 f., Trautmann 144. 
Page(s): 625 



Root / lemma: kseud- {*gheud-) 

Meaning: to grind in little pieces 

Material: Old Indie ksodati^ stamps, crushes ', ksoda-m. ' push, stamping, crushing; flour, 

powder, mash ', ksudra-^ sma\\\ low, despicable ', compounds ksodTyas-, ksudra-u. 'mote, 

speck'; common Old Indie gh- > ks- : Slavic gh- > ch- 

Old Bulgarian chudt^ smaW; small, evil, bad', compounds chuzdbjb{: Old Indie ksod/yas- 
)■ 

Machek (Slavia 16, 174) takes as originally meaning ' skinny ' an (Czech chudy' poor, 
bad, lean '), which he consequently would place to Old Indie ksudhyat/" starves' , ksodh- 
uka-^ hungry'. 

Old Church Slavic: xudb 'small, insignificant, scanty' [adj o]; A^t/zoV/" worse'; Russian: xudoj 
'thin, lean, bad, full of holes' [adj o]; A-^ze 'worse' 

Maybe alb. {*ksdda-) holle^ poor, bad, lean ' common Slavic- alb. cM? reading; common 
alb. Italic -d- > -A. 

connection from Old Indie ksudra-W\\h Avestan xsudra-^i\u\(y (see kseud-2} attempts 
explain Batakrishna Ghosh (Les formations nominales en p, S. 21). 

References: WP. I 502. 
Page(s): 625 

Root / lemma: kuku 

Meaning: cuckoo cooing 

Material: Old Indie kokila-rw. 'the cuckoo pertaining to India ', koka-m. 'cuckoo' (also 

'goose; wolf see below kan). 

Gr. KOKKu^, -Oyoc; m. 'cuckoo' (dissim. from *kukku-), kokku: 'shout of cuckoo ', kokku^oj 
' shout cuckoo'; 

Latin cucu/us ^ cuckoo' (directly shaped from *cucu)\ 

Middle Irish cuach {or neologism to Old Irish cd/< *kovik-s. Gen. cuachl), cymr. cog 
'cuckoo'; Modern High German Kuckuck, 

Lithuanian kukuoti, Latvian /rJ/r^/d/' cuckoo cry'; serb. kukavica^ cuckoo' russ. kukusa 
etc. ds., r. kukuvatb etc. ' cry like a cuckoo '. 



maybe alb. kukuvajke' cuckoo' a Slavic loanword. 

References: WP. I 466 f., WH. I 299. 
Page(s): 627 



Root / lemma: ku-, kus- {*k"'uk"'h-) 

Meaning: to kiss 

Note: (compare bu- S. 103) 

Material: Gr. kuveoj, sKuaaa "kiss' (Greek -ne- infix of the present *Ku-v£-a-[pi]). 

Comments: 

Greek infix -ne- : Hittite infix -nin- which is used, like the more frequent suffix -nu-, in order 

to build the causative of some verbs : hark- "to collapse" harnink- "to throw down", istark- 

"to be ill" istarnink- "to make ill". 

With the stop of the consonant shift in onomatopoeic words of Old Icelandic koss. Old 

English coss. Old High German /ri/s "kiss'. Old Icelandic kyssa. Old English cyssan. Old 

High German kussen^V\ss'\ Gothic kukjan. East Frisian /rJ/r/re"/? seems out of it to be 

reshaped in the baby talk; 

Hittite 3. PI. kuwassanz/" they kiss '. (common -wa- infix of the present in Hittite). 

similar Old Indie cusat/" sucks' , cuscusa' munching the food '. 



References: WP. I 465, Kuiper Nasalpras. 151 . 
Page(s): 626 



Root / lemma: kuak- 

Meaning: croaking, quacking 

Material: Gr. koq^ " of the croaking of the frog ', Latin coaxare "quack' (probably imitation of 

Koa^), German quack, quacken^ from frogs; cackle (duck) etc.', Swedish Dialectal kvaka^ 

cackle like a duck ', Old Icelandic /ri/a/ra "chirp, twitter', russ. kvakatb "quack'. 

Maybe alb. {*kuak) kuak'croak'.
```


## [2026-09-06T21:30:46.855Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 284 285 286; do echo \"===== leaf $n =====\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_02.txt; done"
}
```


### [2026-09-06T21:30:48.489Z] TOOL RESULT

```
===== leaf 284 =====
t  »stampfen'»  lit.  kr{i)avr HuSj  pakraüsius  »Abhang';
623
abg.  u-kruch^  (ksl.  auch  krucH)  , Bruchstück,  Brocken*,  abg.  si>-krusiti zerbrechen  (trans.)',  Sh-krusemje  , Zerknirschung*  (poln.  s-krucJia  ,Reue^), ablaut.  *k'rhchd  ,Brocken,  Krümchen*  (russ.  krochd  , Stückchen'),  *kr^ch^k^ zerbrechlich,  spröde'  (poln.  krechki),  *kTbsiti  (slov.  kfsiti)  ,zerstückeln, zerbrechen'  (usw.,  s.  Berneker  628 — 630). WP.  I  480  f.,  Trautmann  143.
.   i^reu-  ,Schallwort'  s.  oben  S.  570  f.  unter  1.  kev-.
kreup-  , Schorf,  sich  verkrustend
Gall.  crujppellarii  ,gepanzerte  Gladiatoren  der  Aedui',  hrit.  Mons  Graupius (leg.  *Croupios)j  wegen  des  idg.  p  veneto-illyr.  Herkunft  (Pokorny  Ur- illyr.  131);
aisl.  hrjüfr  ,rauh,  schorfig',  hryfe  ,Schorf',  hrüfa  ,Wundrinde',  ags.  hreof ,rauh,  schorfig,  aussätzig',  ahd.  rioh  ,aussätzig',  hriupl  ,scabies',  {h)ruf, PI.  hruvi,  mhd.  ruf  ,Blatter,  Schorf,  Grind,  Aussatz',  nhd.  bair.  ruff  f. , Kruste  auf  rasch  getrocknetem  Erdreich',  rufe,  riefe  , Aussatz,  Schorf, ahd.  ge-roby  nhd.  grob-
lit.  su-si-kraüpti  ,zusammenschauern',  nu-krüp^s  , schorfig',  kraupüs  ,rauh^, lett.  kraüpa  , Grind,  Warze',  kraüpis  , Grind;  Kröte'  (von  der  warzigen Haut;  apr.  crupeyle  , Frosch'),  krüpu,  krupu,  krupt  ,verschrumpfen'^  krupis jKröte,  Zwerg' ;  vom  Rauhwerden  der  Haut  (,Gänsehaut')  auch  lit.  pakraüpti, kruptis  ,schaudern,  erschrecken'.
Dagegen  russ.  krupnyj  ^grobkörnig;  groß',  cech.  krupy  ,rudis'  zunächst zu  abg.  krupa  , Brocken,  Krümchen'^  usw.  [dazu  ablautend  alb.  krip(e), krüp  f.  ,Salz*  (*Ä;r?Zpä)];  diese  Sippe  wohl  eigentl.  , Abgebrochenes'  oder dgl.  zu  3.  kreu-,  krou-s-  ,brechen,  stoßen',  s.  dort.
WP.  I  481  f.,  Trautmann  143.
kreu-t-  (kreu-db-?)  , schütteln,  schwingen,  lebhaft  bewegen'.
Mhd.  rütten  (*hrudjan)  ^rütteln,  schütteln',  nhd.  ,zer-rilttet\  engl,  rudder, ruddle  ,Sieb' ;  ags.  hreade-müs  , Fledermaus' ;  wahrscheinlich  aisl.  hraustr ,rasch,  mutig' ;  vielleicht  als  ,sich  schüttelnd,  schwankend' :  ahd.  Jiriot, nhd.  Riety  as.  hriod,  ags.  hreod  , Schilfrohr'   (*kreu-dho-) ;
vgl.  toch.  A  kru  ,Rohr'?
lit.  krutü,  -Ui  ,sich  regen,  sich  rühren',  krutüs  , rührig,  regsam';
WP.  I  481,  Trautmann  143  f.
krom-  jGestell  aus  Latten,  hölzerne  Umzäunung';  nur  germ.  uud  slav.
Aisl.  hremma  , fassen,  klemmen',  ags.  hremman  ,einengen,  behindern* (wohl  aus  ,*einzäunen'),  afries.  hremhend  , Fes
===== leaf 285 =====
sel',  ndl.  remmen  ,(ein  Rad) hemmen,   sperren'   (,*mit   einem    Balken'),    ^01"^^*^^^^    auch    aisl.    hrefni
624  •
»unterste  Planke  überm  Schiffsboden*  und  got.  hramjan  ,kreuzigen'  {^ ,an  ein  Gestell  heften');
russ.  kröray  PL  »Webstuhl',  zakromü^  »mit  Brettern  umstellen',  klr.  pry. kromyty  »bändigen',  russ.  s-krömnyj  »bescheiden'  usw.
WP.  I  487  f.
kr{6)k-sko-,  -u-  ,Arm  u.  dgl.'?
Ai,  kisku-  m.  »Vorderarm;  Stiel  einer  Axt;  ein  Längenmaß'  (mind.  für *krsku-) ;
alb.  krake  ,Oberarm,  Schulter»  Flügel'  {""krok-sko-?)  ]
wahrscheinlich  zu  lit.  kdrka  »Schweinefuß»  Vorderbein  des  Schweines*, ablaut.  ostlit.  kirkälis  m.  »Stelze';
slav.  *korka  f.  in  sloven.  krdka^  krdda  »Schweinefuß*;
daneben  slav.  *korkb  in  bulg.  krak  »Bein»  Fuß*,  russ.  ökorok  »Schinken*; dazu  ablaut.  slav.  *krok^  m.  in  skr.  ki^ok  (Gen.  kroka),  öech.  krok  »Schritt* und  slav.  *korakh  m.  in  skr.  koräk,  sloven.  kordk  ds.
Ganz  unklare  Ablautverhältnisse.
WP.  I  488»  Trautmann  118.
krüs-  »Unterschenkel»  Bein'.
Arm.  srun-k'  PI.   (Gen.  srvanc,  sruni-c)  »Schienbein,  Wade*  (*/crüs-m-)ji lat.  crüs,  -ris  n.  »Unterschenkel»  Bein*. WP.  I  489»  WH.  I  295.
krut-  »Wölbung»  Brust»  Bauch*.
Mir.  crott  f.  »Höcker»  Harfe*»  nir.  cruit  ds.»  altbrit.-gall.  crotta  »Harfe*, cjmr.  crwth  m.  »Höcker»  Geige'»  croth  f.  »Bauch»  uterus»  vulva*;
lit.  krütis  »weibliche  Brust*»  krütine  »Brust*»  lett.   kriits  »Hügel»  Brust*. Wohl  zu  kreu-  »wölben*»  s.  unter  (s)ker-j  (s)kereu'  »drehen*. WP.  I  485,  489»  Specht  Idg.  Dekl.  77  2.
ksä-  »brennen  (versengt»  dunkel  V  ?)*  ?
Ai.  ksäyati  »brennt'»  ksäti-  f.  »Glut*»  ksämd-  »versengt»  ausgedörrt»  ver- trocknet*»   ksärd-   »brennend»    ätzend*;    Kaus.   ksäpdyati   »macht    brennen*;
zu  letzterer  p-Yovm  vielleicht  arm.  cav  »Schmerz*»  casnum  »zürne*»  Aor. caseay  (»*hitzig  sein*;  s  =  ps-)]  zu  ksämd-  wohl  arm.  camaJi  »trocken* (die  arm.  Worte  weisen  auf  ks-).
WP.  I  500»  Frisk  Nominalbild.  6 ;  s.  unter  ks'n-ro-.
625
;eip-,  kseih-  , werfen,   schwingend   schleudern,   in   schwingender   heftiger Bewegung  sein'.
Ai.  kßipdti   ,wirft,    schleudert',  Kaus.  ksepdyati,    ksiprd-h   ,schnell';    mit Media  aksl.  osiba-jg,  -ti  ,sich  abwenden',  russ.  lihdth  , werfen',  sibkij  ,schnell', ^sibdth  , abschlagen',  osibdhsja  ,sich  irren'. WP.  I  501.
fs-en-,  ks-es-,  ks-eu-  s.  oben  S.  585  f.  unter  kes-.
ics^-J'o-  ,trocken';   vom  Himmel  und  Wetter  auch  ,trocken  =  hell,  klar'. Gr.  ^€q6v  (nur  Akk.)
===== leaf 286 =====
  , festes,  trockenes  Land',  dehnstufig  ^rjgög  ,trocken, dürr' ;  vgl.  oben  S.  624  ai.  ksärd- ;
lat.  serescunt  (Lucil.  I  306)  ,(die  Kleider)  trocknen  (in  der  Sonne)', serenus  ,heiter,  hell,  klar,  trocken'  (vom  Himmel  und  Wetter) ;
ahd.  serawen  ,trocken  werden,  tabescere,  languere,  marcere',  mhd.  nhd. Serben  ,verdorren,  welk  werden' ; toch.  A  ksär{k)  ,Morgen'?
Daß  ks^-ro-  eine  Erweiterung  von  ksä-  ,brennen,  versengen'  sei,  ist  wahr- L     scheinlich. i       WP.  I  503,  Schwyzer  Gr.  Gr.  I  329.
kseuhh-  ,schwanken,  in  schwingender  Bewegung  sein'.
Ai.  ksübhyatij  ksöbhate  (ksubhnöti,  -näti)  ,schwankt,  zittert',  ksöbJiayati ,setzt  in  Bewegung',  ksöbha-  m.  , Schwanken,  Erschütterung';  av.  x§aob- ,in  Aufregung  geraten'  (xsufsqn),  npers.  ä-mftan^  ä-§öftan  ,in  Bewegung versetzen',  ä-söb  , Verwirrung,  Tumult';
poln.  chybac  ,schaukeln,  hin  und  her  bewegen' ;  cJiybki  ,behend,  rasch' ;  klr. chybdty  ,zweifeln,  unschlüssig  sein',  chyba  (*ksüba)  , Mangel,  Fehler'  usw.
WP.  I  502  f.,  Trautmann  144.
kseud-  jklein  stampfen'.
Ai.  ksödati  ,stampft,  zermalmt',  ksöda-  m.  ,Stoß,  Stampfen,  Zermalmen; Mehl,  Pulver,  Puder',  ksudrd-  ,klein;  niedrig,  gemein',  Komp.  ksödlyas-] ksudrd-  n.  ,Stäubchen';
abg.  chud^ ', klein-,    gering,   schlecht',    Komp.  chuzdhjh   (:  ai.  ksödiyas-).
Machek  (Slavia  16,  174)  nimmt  als  ursprüngl.  Bedeutung  ,mager'  an (cech.  chudy  ,mager'),  das  er  somit  zu  ai.  ksudhyati  ,hungert',  ksödh-uka- ,hungrig'  stellen  möchte.
Verbindung  von  ai.  ksudrd-  mit  av.  x§udra-  ,flüssig*  (s.  2.  kseud-)  versucht Batakrishna  Ghosh  (Les  formations  nominales  en  p^  S,  21)  zu  begründen.
WP.  I  502.
40
626  •
kpei'  ,siedeln,  sich  ansiedeln,  eine  Niederlassung  gründen*.
Ai.  ksiti,  hsiydti  ,weilt,  wohnt',  av.  saeiti  ds.,  ai.  ksiti',  av.  Hti-  ,Wohn.' platz,  SiedelungS   ai.  kskra-,   av.  söid-ra-  n.  ,Gnindbesitz,  Wohnplatz',  ^j^ Jcsema-  m.  ,ruhiges  Verweilen';
arm.  sen.  Gen.  Hni  ,bewohnt,  bebaut,  Dorf  (:  gr.  xzrotW);
gr.  'ATL^cü  ,gründe',  iv-KTifj^svog  ,wohl  gehaut,  wohl  bestellt',  iv'/.TLTog  ^. rteQiy.TLOvsg,  Tteqiy.Tkai  ,Um wohner,  Nachbarn',  d(X(pLy,TLOvsg  ,Herumwohnende* (zur  Form  df.icptxrvovsg  Lit.  bei  Boisacq  525  Anm.  2),  xr/ö-tg  , Anbauung' Ansie
```


## [2026-09-06T21:31:06.617Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kseud\" POK_02.txt | head -20; echo \"=== POK_full kseud ===\"; grep -n -i \"kseud\" POK_full.txt | head -20; echo \"=== WLD Bd1 p502 (leaf 511) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==511' incoming/WLD/WLD_Bd1_pages.txt | head -60"
}
```


### [2026-09-06T21:31:08.410Z] TOOL RESULT

```
4503:kseud-  jklein  stampfen'.
4507:Verbindung  von  ai.  ksudrd-  mit  av.  x§udra-  ,flüssig*  (s.  2.  kseud-)  versucht Batakrishna  Ghosh  (Les  formations  nominales  en  p^  S,  21)  zu  begründen.
=== POK_full kseud ===
48878:Root / lemma: kseud- {*gheud-) 
48901:connection from Old Indie ksudra-W\\h Avestan xsudra-^i\u\(y (see kseud-2} attempts 
=== WLD Bd1 p502 (leaf 511) ===
                                                                                           ,                                     ;




502                                      qseu-, qsneu-, qneu-, sneu-                   — qseubh-

Lautnachalimung       verhaltenem Niesen gehort; man erinnert andrer-
                                   bei
seits     an qs-n-m       „kratzen“ zu qes- ds.) **qsneu und
                               :    qs-eu-                        vielleicht                                      —
daraus vereinfachtes                     —
                         *sneu und *qneu- in mengl. snesen, engl. sneeze
..niesen" (ahnlich nd. sniisen, dan. snnse ,,schnobern, -wittern"), npers.
isnosa, asnbsa „niesen“ (ahnlich lit. sniaukti ..schnupfen")                       ahd. niosan mnd.     ;                            ,


mengl. ncsen, aisl. hnjosa                    ,,   niesen" (wieder verschieden, aus *pneus, ags .fnco-
snn , hoW.fniesen „ niesen", vgl. aueh mhd. phmtsen niesen, schnauben"; esspielt
wohl die Wz. von gr. nveco zivevya herein). Ygl. Trautmann Bsl. Wb. 266.
                                                       ,



   Im Slav, ein kwh-, kyeh- aus Ms- (z. B. skr.-ksl. kshnovenije Niesen'',                                              ,,


klr. kychaty) und rsch- cich- (*kts - z. B. russ. c'echs Niesen", achats cAchcUs
                                                                     ;                             ,,
                                                                                                                             ,


,,
     niesen").
  Ygl. Zupitza Gutt. 9, BB. 25, 95, Uhlenbeck Ai. Wb. 72, Fick III 4 100f.,
Falk-Torp u. fnyse, nyse snuse, Berneker 165, 658.-
                                              ,




kseud-        ,,klein     stampfen".
                      zermalmt", ksoda- m. „StoB, Stampfen, Zermalmen;
      Ai. kioduti „stampft,
Mehl. Pulver. Puder", kinulrd- ..klein. gering; niedrig, gemein", Komp.
ksoihyas -, kmdra- n. ..Staubchen"; abg. clinch ,, klein; diirftig, gering.
schlecht;         Komp. chnzds/s i: ai. k^ldiyas-).
   Pedersen IF. 5, 60 f. mit fernzuhaltendem, so der u. *qseud- „Fliissig-
 keit" behandelten Sippe von ai. k-6das „Flut". ferner       wie auch KZ. 39.                           —
 428     —
        von gr. ipvdgos ..liignerisch", endlich von lit. siaudjs „Strohhalm".
 simulaT ..Stroh", deren Bed. mit der von ai. ksocla- nur kiinstlicli zu ver-
 einigen ware und die ini Gutt. von chads abweichen wiirden).


 qseud-       ..Fliissigkeit"              (nur arisch).
       Ai.   k sodas-     n.        ..bewegtes Wasser, Flut, Wassermasse, Strom" = av.
 xsaodah-         n.   „FIuB,         Strdmung, Wasserschwall", xsudra -, xsudra- ..fliissig;
 n.     Fliissigkeit",             xsitsta-            (   *ksud-ta -)       ..fliissig,   breiig,      geschmolzen‘‘,                   fsra-
 xiuostra-        n.   ..YorwartsflieBen".   Cbarpentier IF. 28, 178ff., der eine
```


## [2026-09-06T21:31:19.201Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==511' incoming/WLD/WLD_Bd1_pages.txt | sed -n '40,120p'; echo \"=== leaf 512 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==512' incoming/WLD/WLD_Bd1_pages.txt | head -40"
}
```


## [2026-09-06T21:31:19.753Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xsaodah\\|x§aodah\\|ksodas\\|k sodas\" POK_02.txt POK_full.txt | head; echo ---; grep -n \"Flüssigkeit\\|fliissig\" POK_02.txt | sed -n '1,20p'"
}
```


### [2026-09-06T21:31:20.965Z] TOOL RESULT

```
kseud-        ,,klein     stampfen".
                      zermalmt", ksoda- m. „StoB, Stampfen, Zermalmen;
      Ai. kioduti „stampft,
Mehl. Pulver. Puder", kinulrd- ..klein. gering; niedrig, gemein", Komp.
ksoihyas -, kmdra- n. ..Staubchen"; abg. clinch ,, klein; diirftig, gering.
schlecht;         Komp. chnzds/s i: ai. k^ldiyas-).
   Pedersen IF. 5, 60 f. mit fernzuhaltendem, so der u. *qseud- „Fliissig-
 keit" behandelten Sippe von ai. k-6das „Flut". ferner       wie auch KZ. 39.                           —
 428     —
        von gr. ipvdgos ..liignerisch", endlich von lit. siaudjs „Strohhalm".
 simulaT ..Stroh", deren Bed. mit der von ai. ksocla- nur kiinstlicli zu ver-
 einigen ware und die ini Gutt. von chads abweichen wiirden).


 qseud-       ..Fliissigkeit"              (nur arisch).
       Ai.   k sodas-     n.        ..bewegtes Wasser, Flut, Wassermasse, Strom" = av.
 xsaodah-         n.   „FIuB,         Strdmung, Wasserschwall", xsudra -, xsudra- ..fliissig;
 n.     Fliissigkeit",             xsitsta-            (   *ksud-ta -)       ..fliissig,   breiig,      geschmolzen‘‘,                   fsra-
 xiuostra-        n.   ..YorwartsflieBen".   Cbarpentier IF. 28, 178ff., der eine
                                                                    Lit. bei
 Wzvariante ksn-i-(d-) in folgenden, schon wegen der verschiedenen Be-
 deutungswendung auf schleimiges Bedenken weckenden Worten sucht                                                                             ;



 ai. kivrda-, ksvcta- m. ,,Gift“, (mi.) kheta- „Schleim, Rotz", khed aya- „Gift“

 (aber k'slra- ,, Milch" nicht mit ks- aus ksu- in denselben Kreis, s. *ksTro-;
 und av. xivld- „Milcb" zu lit. svestas „Butter", dessen Anlaut trotz Ch. nicht
 wohl aus ksv- herleitbar ist).
    Lit .kudus ..ScheiB" (Pedersen IF. 5, 60 f.) ist im Gutt. unvereinbar.


     qseubh- ..schwanken, in schwingender Bewegung sein".
       Ar. ksiihhyati, ksobhate                            (   ksubhnoti ,   -ndti)    „schwankt,           zittert",   ksobhayati
 ,,setzt     Bewegung", ksobha-h „Schw anken, Erschiitterung"; av. xsaob-
             in                                                                r



 „in Aufregung geraten"    xsufsqn), np. a-suftun a-softan ,.in Bewegung
                                                   i
                                                                                               ,


 versetzen", yu-iuftan ..zerstreuen", ii->ob „Yerwirrung, Tumult";
    poln. chybac, chybnac „schaukeln. hin- und herbewegen; sich riihren.
     bewegen", rhybki ,,behend, rasch", klr. chybdty ..zweifeln, unschliissig sein".
     chyba ..Mangel, Fehler" usw. Zupitza BB. 25, 94; Berneker 4 2 f mit lit.                                       1



     s- aus qs- (doch s. Berneker aaO.), vielleicht nach Trautmann KZ. 43, 109
     auch preuli-lit. snub id, saiibti, lit. sianbiii siaiibti ..spielend toben, rasen.
                                                                                   ,

=== leaf 512 ===
               -




                                                             kser-       — ksuelp-                                                 503

von wilden Kindern; Possen reiBen, Zoten angeben" (vgl. dt. Schwank zu
sueng- „biegen, schwingen"), preuB.-lit. suboti , lit. siubiioti ..schaukeln, sich
mit dem Oberkorper wiegen" ( subinS ,,AfterofFnung"?? Leskien Abl. 310),
siubuokle „Schaukel". Lett, schaublt ,,wackeln machen" (setzt ein *siub- vor-
aus,Leskien aaO.), doch konnen die bait. Formen auch idg. seu-bQi)- sein,
s.  sen
     u.    biegen", wo auch iiber lit. siipti.
                    ,,


  Mit aksl. zybati „schaukeln“ ist preuB.-lit. suboti trotz Bruckner KZ. 46,
234 nicbt zusammenzubringen.

kser- „trocken“;                               vom Himmel und Wetter auch                    „trocken = hell. klar\
     Gr. gegov (*nur Akk.) ,,festes, trockenes Land', dehnstufig gijoog ,,trocken,
diirr     ’   (zur       wohl triigerischen Gleiehsetzung mit ai. ksard- ,,brennend“ siehe
u. *kse-   ,,brennen“); lat. serescunt (Lucil. I 306) „(die Kleider) trocknen
                                1
(in  der Sonne)     (verschieden von lac frigore seresrit „wird molkig", das
                                    '



von serum „Molken" abstamint). serenus ,.heiter, hell, klar, trocken (vom                                                11



Himmel und Wetter; gegen die Deutung „*hell wie Molkenwasser spraclie                                            1
                                                                                                                     '
```


### [2026-09-06T21:31:21.063Z] TOOL RESULT

```
---
1573:gr.  xf(/)w  , gieße',  Aor.  hom.  ex^va  <  ^exsvaa,  Perf.  xf/vKoc,  x^'^oc;  , ge- gossen', xfr^/a  ,Guß,  Fluß,  Trankopfer',  x^^^^S»  X^^^g  , Schmelzgrube, Gußform',  x^V  ,Trankopfer  für  Tote',  xofivg  m.,  f.  ,Maß  für  Flüssigkeiten', Xovg  ds.,  Gen.  x^^S  ^^^  X^^g,  älter  dial.  x^^  °^'>  ^-  ,aufgebäufte  Krde', XOJI-KX  ,ErdwaU',  x^f^  , schütte  Erde  auf;  x^'^Qog,  x^'^Q^  , irdener  Topf, X<Ji^lov  ,Waschwasser',  x^^V^  , reichlich,  hingeschüttet'  (zum  d  vgl.  die Wurzelerweiterung    gheud-),    -KoxvSelv    ,in    Menge    hervorströmen',    xoxv*
1845:Asächs.  quappa,  quappia,  quappo  .Aalquappe'  (mit  bei  lautmalenden  Worten häufiger  Konsonantengemination),  daraus  mhd.  quappe^  quape,  kobe,  nhd. Quappe,  hoU.  kivab(be)  .Quappe.  Kropf.  Wamme',  isl.  kvap,  kvapi  .Gallert oder  gallertartige  Dinge',  schwed.  dial.  (s)kvabb  .etwas  Dickes.  Fettes', {s)kvebba  .feiste  Frau',  engl,  quab  .Morast',  quaver  .zittern,  vibrieren'. Dazu  das  Verb  norw.  dial.  kvapa  .eine  Flüssigkeit  aussenden',  schwed. dial.  kvabba,  ndd.  quabbeln  .vor  Fettigkeit  zittern';
1890:g^eid{hy  ,Schlamm,  halbfliissiger  Schmutz^?
3554:Anord.  hrjöta  , brüllen,  schnarchen,  brummen',  ags.  hnitan  , schnarchen, schnauben',  ahd.  rüzan,  rüzön  , rasseln,  schnarchen,  summen';  vgl,  ags. hrot  m.  , dicke  Flüssigkeit,  Schleim',  usw.  unten  S.  537 ;
4300:lat.  congius  ,Hohlmaß  für  Flüssigkeiten'  ist  höchstwahrscheinlich  gr.  Lw. ; unsicher  lett.  sence  ,Muschel',  da  zence  die  richtigere  Form  scheint. WP.  I  461  f.,  WH.  I  260,  J.  B.  Hofmann  Gr.  etym.  Wb.  151.
4312:iormno-,  krmno-  ,ätzende,  beißende  Flüssigkeit,  Lauge,  Harn*.
4976:ags.  asächs.  lagit  (*lakü-)  ,See'  (dazu  der  nordwestd.  FIN  Leine  aus Lagina),  aisl.  Iqgr  m.  ,See,  Wasser,  Flüssigkeit^^ ;  dazu  lä,  Ix  f.  ,Strand- wasser,  See'  (^lahö),  mhd.  lä  ,Brunnen,  Sumpfwasser';
4998:mir.  laüh  ,Bier,  Flüssigkeit;  Sumpf  =  gall.  Äre-late  Stadt  ,östlich  des Sumpfes',  corn.  lad  ,liquor',  acymr.  Hat  ds.,  cjmr.  llaid  {Hatio-) , Schlamm', mir.  lathach  ds. ;
5034:aisl.  lehr  ,leck',  leki  m.  ,Leck',  ags.  hlec  (mit  falschem  h)  ,leck',  nhd. (eigentlich  ndd.)  Lech,  Adj.  lech  und  (ndd.)  leck,  mnd.  Iah,  aisl.  leka  stark.  V. ,das  Wasser  durchlassen',  mnd.  leken  ds.,  ahd.  ze(r)lechen  , zerlechzt,  leck', mhd.  lechen  , Flüssigkeit  durchlassen,  vor  Trockenheit  Risse  bekommen, verschmachten'  {lechezen  ,austrocknen',  eigentlich  ,ausrinnen',  nhd.  lechzen); Kaus.  Hakjan  in  ags.  leccan  , benetzen',  mnd.  lecken  , seihen',  mhd.  lecken , benetzen';  mnd.  lak  m. n.  ,Fehler,  Mangel,  Gebrechen',  mengl.  lac,  nengl.  lack ds.,  afries.  lec  , Schade' ;  dehnstufig  aisl.  lekr  m.  ,Bach',  norw.  auch  , Pfütze'.
5328:Air.  lind  (u-Stamm)  n.  ,Flüssigkeit,  Trank',  Gen.  lenda,  nir.  lionn,  Gen. leanna  ,ale',  cymr.  llyn  , Trank',  davon  verschieden  (s-Stamm)  air.  lind. Gen.  linde  f.  ,Wasser,  Teich,  See',  cymr.  llyn  ,Teich',  acorn.  len  ,Wasser', bret.  lenn  , Teich',  abrit.  Alvdov  ON,  gall.  Lindo-magus  Schweiz.  Flußname ,Limmat* ;
5448:lat.  luöj  -ere  , büßen,  zahlen',  in  Glossen  ,Xv(i)^,  reluö  ,löse  wieder  ein', solüö  (*se-luö)  solutus  , lösen',  lues  (,*Auflösung',  daher  :)  ,unreine  Flüssigkeit usw.';
5708:Arm.  mör  ,Kot,  Schlamm,  Sumpft  (*mak-ri-)  ]  alb.  make  ,Leim,  Haut auf  Flüssigkeiten^;
5962:skr.  m\2-äm,  -ati  ,harnen'  {z  aus  dem  Präs.  *miz-jg  verallgemeinert) ; sloven.  mdzi,  mdzeti  ,hervordringen  (von  Flüssigkeiten)',  m922?ia  ,Moorgrund'; slav.  *m^zga  (*moigzghä  aus  *moigh-ska)  ,Baumsaft'  (,*hervortröpfelnd') in  skr.  mezga,  öech.  mizha,  miza  usw.;
6376:Auf  dem  r-Nominativ  beruhen:  gr.  fxdgr]  f.  ,Hand',  ei^aQrjg  ,leicht  zu handhaben',  (Äagig,  -scog  m.  ,Flüssigkeitsmaß';  alb.  marr  , nehme,  empfange, halte,  fasse'  (*marnö,  n-Präs.  als  Denominativbildung  von  *mar'  ,in  die Hand  bekommen').
6386:I.  meu-,  mevLQ- :  mu-  ^feucht,  moderig,  netzen,  unreine  Flüssigkeit  (auch Harn),  beschmutzen',  auch  ,waschen,  reinigen';  mu-dlo-  ,WaschmitteP, mu-tro-  , Schlamm,  Sumpf.
```


## [2026-09-06T21:31:49.853Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### AHD ksero/kser\"; grep -n -i \"ksero\\|kser-\\|kseubh\\|kseud\" AHD_watkins1985.txt | head -20; echo \"### AHD xero/elixir/serene\"; grep -n -i \"xerophyte\\|elixir\\|serene\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T21:31:49.912Z] TOOL RESULT

```
### AHD ksero/kser
648:English hréowan, to distress, grieve: RUE!, RUTH. 2. Ex- tended o-grade form *krous- in Greek krouein, to strike: ANACRUSIS. [Pok. 3. kreu- 622.] kreup-. Scab; to become encrusted. 1. Germanic *hrub- in: a. Middle Low German ruffelen, to crumple, akin to the Germanic source of Middle English ruffelen, to ruffle, roughen: RUFFLE}; b. Germanic compound *ga-hrub- (*ga-, intensive prefix; see kom) in Middle Dutch grof, harsh: GRuFF. 2. Suffixed o-grade form *kroup-d in Serbo-Croatian krupa, groats (perhaps > German Graupe, barley): GRAUPEL. [Pok. kreup- 623.] kreus-. To begin to freeze, form a crust. 1. Suffixed zero-grade form *krus-to- in: a. Latin crusta, crust: CROUTON, CRUST, CRUSTACEAN, CRUSTACEOUS, CRUS- TOSE; b. Greek krustallos, ice: CRYSTAL, CRYSTALLINE, CRYSTALLO-. 2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-. [Pok. 1. B. kreu- 621.] kreut-. Also kreudh-. Reed. Germanic *hreuda- in Old English hréod, reed: REED. [Pok. kreut- 623.] kropo-. Roof. Germanic *hréfam in Old English hrdf, roof: ROOF. [Pok. krdpo- 616.] krut-. Musical instrument. 1. Germanic *Arut- in Old French rote, a stringed instrument: ROTE3, 2. Geminated form *krutté in Welsh crwth, an ancient Celtic instru- ment: CROwD?. [Pok. krut- 624.] ksero-. Dry. 1. Lengthened-grade form *kséro- in Greek xéros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHAL- MIA. 2. Perhaps suffixed variant form “kseres-no- in Latin serénus, serene, bright, clear: SERENE. [Pok. ksero- 625.] ksun. Preposition and preverb meaning “with.” 1. Greek sun, xun, together, with: syN-. 2. Russian so-, s-, with, in sputnik, fellow traveler (see pent-): SPUTNIK. [In Pok. 2. sem- 902.] ku-. Hypothetical base of a variety of conceivably related Germanic words meaning “a hollow space or place, enclosing object, round object, lump,” and some other derivative denotations. 1. Germanic *kubdn-, hut, shed, room, in: a. Old English cofa, bedchamber, closet: COVE!; b. Middle Dutch cubbe, “pen, stall,” fish basket, akin to the probable source of CUBBY; C. Germanic compound *kubawald-, probably “house ruler,” household god (wald-, power; see wal-), in Middle High German kobolt, an underground goblin: COBALT, KOBOLD. 2. Germanic *kutam in Old English cot, cottage: COT?, (COTTAGE). 3. Germanic *kutdn- in Old English cote, shelter: CoTE!. 4. Germanic *k(e)ud- in: a. Old English codd, bag, husk: cop?; b. Old English cudele, cuttlefish (from its ink bag): CUTTLE. 5. Germanic k(e)ut- in Old English *cieter, intestines (probably > Middle English chiterling): cx1T- TERLINGS. 6. Germanic *kukk- in Middle English cok, haycock, pile of straw: cock?. 7. Germanic *kuk- in Old English cicen, chicken: CHICKEN. 8. Germanic *kugg- in Swedish kugge, cog, akin to the possible Scandinavian source of Middle English cogge, cog: coc}. 9. Germanic *kuggila in Old English cycgel, rod, cudgel: CUDGEL. 10. Germanic *keulaz in: a. Low German kielswin, keel- son: KEELSON; b. Middle Dutch iel, ship, keel of a ship: KEEL?, 11. Germanic *kijp- in Middle Dutch kipe, cask, tub, basket: COOPER. 12. Germanic *kunt- in Middle Low German kunte, vulva, akin to the Low German source of Middle English cunte, vulva: CUNT. 13. Germanic kird- in Icelandic kiird, to crouch, lie in wait, akin to the Scandinavian source of Middle English couren, to cower: COWER. 14. Possibly Old Norse kiiga, to oppress, akin to the probable source of cow?. [In Pok. géu- 393.] kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: Kiss. [Pok. ku-, kus- 626.] kwat-. To ferment, be sour. Possible root. Suffixed vari- ant form *kwét-so- in Common Slavic *kvasi in Russian kvas, kvass: Kvass. [Pok. kuat(h)- 627.] kwe, And (enclitic). Latin -que, and: SESQUI-, UBIQUITY. [Pok. kve 635.]
1449:ELIXIR ksero-
2087:PHYLACTERY phulax PHYLAXIS phulax PHYLE bheue- PHYLETIC bheue- -PHYLL bhel-3 PHYLLO- bhel-3 PHYLLOCLADE kel-1 -PHYLLOUS bhel-3 PHYLLOXERA ksero- PHYLOGENY bheua- PHYLUM bheue- PHYSIC bheue- PHYSIO- bheue- PHYSIOGNOMY gn6- PHYSIQUE bheue-_ PHYSOSTIGMINE pu-1 PHYSOSTOMOUS_ pu-! -PHYTE bheue- PHYTO- bheue- PHYTON bheue- PIACULAR pius PIANO? pele-2 PIANOFORTE bhergh-2 PIAZZA plat- PIBROCH pipp- PICA2 (s)peik- PICARO (s)peik- PICE ped-1 PICEOUS_ pik- PICKET (s)peik- PICOLINE pik- PICRO- peig-1 PICTOGRAPH peig-1 PICTOR peig-! PICTURE peig-1 PICTURESQUE peig-', (s)peik- PIE? (s)peik-
2249:SEQUESTRUM sekw-1 SERAC ser-2 SERE! saus- SERENE ksero- SERF servus SERGEANT servus SERIES ser-3 SERIF skribh- SERIOUS swer-5 SERMON ser-3 SEROTINOUS sé@-2 SERPENT serp-2 SERPIGO serp-2 SERRIED ser-3 SERTULARIAN ser-3 SERUM ser-2 SERVAL_ ker-! SERVE servus SERVICE servus SERVILE servus SERVITUDE servus SESQUI- kwe, sémi- SESQUIPEDALIAN ped-! SESSILE sed-1 SESSION sed-1 SESTERCE sémi-, trei- SESTET s(w)eks SESTINA s(w)eks SET! sed-1 SETTLE sed-1 SEVEN septm SEVER pere-! SEVERAL pere-1 SEVERE WEér0- SEW syu-
### AHD xero/elixir/serene
648:English hréowan, to distress, grieve: RUE!, RUTH. 2. Ex- tended o-grade form *krous- in Greek krouein, to strike: ANACRUSIS. [Pok. 3. kreu- 622.] kreup-. Scab; to become encrusted. 1. Germanic *hrub- in: a. Middle Low German ruffelen, to crumple, akin to the Germanic source of Middle English ruffelen, to ruffle, roughen: RUFFLE}; b. Germanic compound *ga-hrub- (*ga-, intensive prefix; see kom) in Middle Dutch grof, harsh: GRuFF. 2. Suffixed o-grade form *kroup-d in Serbo-Croatian krupa, groats (perhaps > German Graupe, barley): GRAUPEL. [Pok. kreup- 623.] kreus-. To begin to freeze, form a crust. 1. Suffixed zero-grade form *krus-to- in: a. Latin crusta, crust: CROUTON, CRUST, CRUSTACEAN, CRUSTACEOUS, CRUS- TOSE; b. Greek krustallos, ice: CRYSTAL, CRYSTALLINE, CRYSTALLO-. 2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-. [Pok. 1. B. kreu- 621.] kreut-. Also kreudh-. Reed. Germanic *hreuda- in Old English hréod, reed: REED. [Pok. kreut- 623.] kropo-. Roof. Germanic *hréfam in Old English hrdf, roof: ROOF. [Pok. krdpo- 616.] krut-. Musical instrument. 1. Germanic *Arut- in Old French rote, a stringed instrument: ROTE3, 2. Geminated form *krutté in Welsh crwth, an ancient Celtic instru- ment: CROwD?. [Pok. krut- 624.] ksero-. Dry. 1. Lengthened-grade form *kséro- in Greek xéros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHAL- MIA. 2. Perhaps suffixed variant form “kseres-no- in Latin serénus, serene, bright, clear: SERENE. [Pok. ksero- 625.] ksun. Preposition and preverb meaning “with.” 1. Greek sun, xun, together, with: syN-. 2. Russian so-, s-, with, in sputnik, fellow traveler (see pent-): SPUTNIK. [In Pok. 2. sem- 902.] ku-. Hypothetical base of a variety of conceivably related Germanic words meaning “a hollow space or place, enclosing object, round object, lump,” and some other derivative denotations. 1. Germanic *kubdn-, hut, shed, room, in: a. Old English cofa, bedchamber, closet: COVE!; b. Middle Dutch cubbe, “pen, stall,” fish basket, akin to the probable source of CUBBY; C. Germanic compound *kubawald-, probably “house ruler,” household god (wald-, power; see wal-), in Middle High German kobolt, an underground goblin: COBALT, KOBOLD. 2. Germanic *kutam in Old English cot, cottage: COT?, (COTTAGE). 3. Germanic *kutdn- in Old English cote, shelter: CoTE!. 4. Germanic *k(e)ud- in: a. Old English codd, bag, husk: cop?; b. Old English cudele, cuttlefish (from its ink bag): CUTTLE. 5. Germanic k(e)ut- in Old English *cieter, intestines (probably > Middle English chiterling): cx1T- TERLINGS. 6. Germanic *kukk- in Middle English cok, haycock, pile of straw: cock?. 7. Germanic *kuk- in Old English cicen, chicken: CHICKEN. 8. Germanic *kugg- in Swedish kugge, cog, akin to the possible Scandinavian source of Middle English cogge, cog: coc}. 9. Germanic *kuggila in Old English cycgel, rod, cudgel: CUDGEL. 10. Germanic *keulaz in: a. Low German kielswin, keel- son: KEELSON; b. Middle Dutch iel, ship, keel of a ship: KEEL?, 11. Germanic *kijp- in Middle Dutch kipe, cask, tub, basket: COOPER. 12. Germanic *kunt- in Middle Low German kunte, vulva, akin to the Low German source of Middle English cunte, vulva: CUNT. 13. Germanic kird- in Icelandic kiird, to crouch, lie in wait, akin to the Scandinavian source of Middle English couren, to cower: COWER. 14. Possibly Old Norse kiiga, to oppress, akin to the probable source of cow?. [In Pok. géu- 393.] kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: Kiss. [Pok. ku-, kus- 626.] kwat-. To ferment, be sour. Possible root. Suffixed vari- ant form *kwét-so- in Common Slavic *kvasi in Russian kvas, kvass: Kvass. [Pok. kuat(h)- 627.] kwe, And (enclitic). Latin -que, and: SESQUI-, UBIQUITY. [Pok. kve 635.]
1449:ELIXIR ksero-
2249:SEQUESTRUM sekw-1 SERAC ser-2 SERE! saus- SERENE ksero- SERF servus SERGEANT servus SERIES ser-3 SERIF skribh- SERIOUS swer-5 SERMON ser-3 SEROTINOUS sé@-2 SERPENT serp-2 SERPIGO serp-2 SERRIED ser-3 SERTULARIAN ser-3 SERUM ser-2 SERVAL_ ker-! SERVE servus SERVICE servus SERVILE servus SERVITUDE servus SESQUI- kwe, sémi- SESQUIPEDALIAN ped-! SESSILE sed-1 SESSION sed-1 SESTERCE sémi-, trei- SESTET s(w)eks SESTINA s(w)eks SET! sed-1 SETTLE sed-1 SEVEN septm SEVER pere-! SEVERAL pere-1 SEVERE WEér0- SEW syu-
```


## [2026-09-06T21:31:50.905Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN elixir\"; grep -n \"^elixir\" KLN_1966.txt | head; echo \"### KLN xero\"; grep -n \"^xer-\\|^xero-\\|^xeroderma\\|^xerasia\" KLN_1966.txt | head; echo \"### KLN serene\"; grep -n \"^serene\\|^serenade\\|^serenity\\|^serein\" KLN_1966.txt | head"
}
```


### [2026-09-06T21:31:50.988Z] TOOL RESULT

```
### KLN elixir
12838:elixir, n.,  1)  asubstance  supposed  to  prolonglife; 2)  a  substance  supposed  to  change  all  metals into  gold.  —  ML.,  fr.  Arab,  al-iksir,  which  is formed  fr.  Arab,  al-,  ‘the’,  and  Gk.  jjp'.ov,  ‘dry medicinal  substance,  cataplasm’,  fr.  ‘dry’. See  serene  and  cp.  xero-.
### KLN xero
### KLN serene
34671:serein,  n.,  a  fine,  misty  rain.  —  F.,  fr.  OF.  seirein , fr.  seir  (F.  soir),  ‘evening’,  fr.  L.  serum,  ‘late time’,  prop.  neut.  of  the  adj.  serus,  ‘late’,  used as  a  noun.  See  serotine  and  cp.  soiree.
34676:serene,  adj.,  clear,  bright;  calm.  —  L.  serenus, ‘clear,  fair,  cloudless,  serene’,  of  uncertain  ori¬ gin.  It  possibly  stands  for  *kseresnos  and  is cogn.  with  Gk.  E*]p6c,  ‘dry’,  OI.  kfdrah,  ‘burn¬ ing,  corroding’,  kfayati,  ‘bums’,  OHG.  sera- wen,  ‘to  become  dry’.  Cp.  elixir,  xerasia,  xero-.
```


## [2026-09-06T21:32:01.164Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ndef leafof(idx): return t[:idx].count('\\f')\nfor pat in ['elixir, n.,','serene,  adj.,','serenade','serenity','xero-,','xerasia','xeroderma','xer-, xero-']:\n    for m in re.finditer(re.escape(pat),t):\n        print(pat,'| leaf',leafof(m.start()),'|',t[m.start()-60:m.start()+200].replace('\\n',' ')[:260])\n        print()\nEOF"
}
```


### [2026-09-06T21:32:02.975Z] TOOL RESULT

```
elixir, n., | leaf 277 | ctus,  pp.  of  eligere.  See  elect  and  cp. prec.  word. elixir, n.,  1)  asubstance  supposed  to  prolonglife; 2)  a  substance  supposed  to  change  all  metals into  gold.  —  ML.,  fr.  Arab,  al-iksir,  which  is formed  fr.  Arab,  al-,  ‘the’,  and

serene,  adj., | leaf 755 | rmer  name  of  Ceylon.  For  the  ending  see suff.  -ity. serene,  adj.,  clear,  bright;  calm.  —  L.  serenus, ‘clear,  fair,  cloudless,  serene’,  of  uncertain  ori¬ gin.  It  possibly  stands  for  *kseresnos  and  is cogn.  with  Gk.  E*]p6c,  ‘dry’,

serenade | leaf 77 | ee  sere,  adj.,  and  cp.  austere, aubade,  n.,  morning  serenade.  —  F.,  fr.  Proven?. aubado,  fr.  auba,  ‘dawn’,  fr.  L.  alba,  fem.  of albus,  ‘white’,  used  as  a  noun.  See  alb  and  -ade. aubain,  n.,  alien,  foreigner.  —  F.,  orig.  writ

serenade | leaf 152 | r  the  ending  see  suff.  -ity. charivari,  n.,  a  mock  serenade,  rough  music.  — F.,  fr.  Late  L.  caribaria,  fr.  Gk.  xap-/;  (Sapid, ‘heaviness  in  the  head,  top  heaviness’, compound¬ ed  of  xd pi,  ‘head’,  and  (hipoc,,  ‘weight’;  see cere

serenade | leaf 755 | f  serenus, ‘clear,  fair,  bright,  joyous’.  See  serene, serenade,  n.  —  F.  serenade ,  fr.  It.  serenata,  lit. ‘calm  sky',  fr.  sereno ,  ‘serene,  calm’,  fr.  L.  sere¬ nus.  See  serene  and  -ade.  It.  serenata  was  influ¬ enced  in  meaning  

serenade | leaf 755 | air,  bright,  joyous’.  See  serene, serenade,  n.  —  F.  serenade ,  fr.  It.  serenata,  lit. ‘calm  sky',  fr.  sereno ,  ‘serene,  calm’,  fr.  L.  sere¬ nus.  See  serene  and  -ade.  It.  serenata  was  influ¬ enced  in  meaning  by  the  noun  sera,  

serenade | leaf 755 | at  night’.  See  serotine and  cp.  serein. Derivatives :  serenade,  tr.  and  intr.  v.,  serenad-er, n. serenata,  n.,  serenade.  —  It.,  whence  F.  serenade. See  serenade. serendipity,  n.,  the  gift  of  finding  interesting things  by  chance.  —  

serenade | leaf 755 | nade,  tr.  and  intr.  v.,  serenad-er, n. serenata,  n.,  serenade.  —  It.,  whence  F.  serenade. See  serenade. serendipity,  n.,  the  gift  of  finding  interesting things  by  chance.  —  Coined  by  the  English author  Horace  Walpole  (1717-97)  in 

serenade | leaf 755 | enad-er, n. serenata,  n.,  serenade.  —  It.,  whence  F.  serenade. See  serenade. serendipity,  n.,  the  gift  of  finding  interesting things  by  chance.  —  Coined  by  the  English author  Horace  Walpole  (1717-97)  in  a  letter  to Mann  in  January

serenade | leaf 755 | enata,  n.,  serenade.  —  It.,  whence  F.  serenade. See  serenade. serendipity,  n.,  the  gift  of  finding  interesting things  by  chance.  —  Coined  by  the  English author  Horace  Walpole  (1717-97)  in  a  letter  to Mann  in  January  1754  from  t

serenity | leaf 755 | e,  n.  and  tr.  v.,  serene-ly,  adv., serene-ness,  n.,  serenity  (q.v.) serenity,  n.  —  MF.  (=  F.)  serenite,  fr.  OF.  sere- nite,  fr.  L.  serenitatem,  acc.  of  serenitas,  ‘clear¬ ness,  serenity’,  fr.  serenus.  See  serene  and  -ity. serf, 

serenity | leaf 755 |  v.,  serene-ly,  adv., serene-ness,  n.,  serenity  (q.v.) serenity,  n.  —  MF.  (=  F.)  serenite,  fr.  OF.  sere- nite,  fr.  L.  serenitatem,  acc.  of  serenitas,  ‘clear¬ ness,  serenity’,  fr.  serenus.  See  serene  and  -ity. serf,  n.  —  F.,  fr. 

serenity | leaf 755 | fr.  L.  serenitatem,  acc.  of  serenitas,  ‘clear¬ ness,  serenity’,  fr.  serenus.  See  serene  and  -ity. serf,  n.  —  F.,  fr.  L.  servum,  acc.  of  servus,  ‘slave’. See  serve. Derivatives:  serf -age,  n.,  serf-dom,  serf-hood,  n. serge,  n.  —  

xerasia | leaf 755 | bums’,  OHG.  sera- wen,  ‘to  become  dry’.  Cp.  elixir,  xerasia,  xero-. Derivatives:  serene,  n.  and  tr.  v.,  serene-ly,  adv., serene-ness,  n.,  serenity  (q.v.) serenity,  n.  —  MF.  (=  F.)  serenite,  fr.  OF.  sere- nite,  fr.  L.  serenitatem,

xeroderma | leaf 236 | dermis,  hypo- dermis,  leucoderma,  pachyderm,  taxidermy, xeroderma. dermal,  adj.,  pertaining  to  the  skin.  —  A  hybrid formed  fr.  Gk.  Seppa,  ‘skin’  (see  prec.  word), with  -al,  a  suff.  of  Latin  origin. dermat-,  form  of  dermato-  before
```


## [2026-09-06T21:32:18.402Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (276,277,278,754,755,756):\n    print('=== leaf',n,'===')\n    s=t[n]\n    print(repr(s[:200]))\n    print('...')\n    print(repr(s[-200:]))\nEOF"
}
```


### [2026-09-06T21:32:20.368Z] TOOL RESULT

```
=== leaf 276 ===
'��uplifted,  ex¬ alted’  (used  as  pp.  of  efferre,  ‘to  bring  out,  carry out;  to  raise,  lift  up’),  fr.  e-  and  latus  (used  as pp.  of  ferre,  ‘to  bear,  carry’),  which  stands  for\ne'
...
" critical’,  fr. kXeyxel'J-  See  prec.  word  and  -ic.\nEleocharis,  n.,  a  genus  of  plants,  the  spike  rush (bot.)  —  ModL.,  lit.  ‘delight  of  the  marsh’, compounded  of  Gk.  eXo?,  ‘mars"
=== leaf 277 ===
'h’,  and  yapi?, ‘grace,  delight’.  The  first  element  is  cogn.  with OI.  sdras-,  ‘pond’.  For  the  second  element  see Charis.\nelephant,  n.  —  ME.  elifaunt,  olifaunt,  fr.  OF.  oli- font'
...
'bore.\nElkanah,  n.,  1)  masc.  PN.;  2)  in  the  Bible,  name of  the  father  of  the  prophet  of  Samuel.  —  Heb. Elqandh,  lit.  ‘God  has  created  or  acquired’.  For the  first  element  see'
=== leaf 278 ===
'  El.  Heb.  qandh,  ‘he  created or  acquired’,  from  which  derive  qinydn,  ‘thing acquired,  acquisition’,  and  miqneh,  ‘cattle’,  is rel.  to  Aram.-Syr.  q(na,  ‘he  acquired’,  Arab. qdnd,  '
...
'zevir,  adj.,  pertaining  to  the  Elzevirs,  a  Dutch family  of  printers,  or  to  books  printed  or published  by  them.\nDerivative:  Elzevir,  n.,  a  book  printed  by  the Elzevirs.\nem,  n., '
=== leaf 754 ===
'e next  word  and  cp.  sepia.\nsepsis,  n.,  putrefaction.  —  Medical  L.,  fr.  Gk. (TTjt)/u;,  ‘putrefaction’,  from  the  stem  of  of] rreiv, ‘to  make  rotten’,  which  is  of  uncertain  origin'
...
'it. ‘anything  separated’,  neut.  of  L.  sequester,  used as  a  noun.  See  sequester, sequin,  n.,  1)  an  Italian  gold  coin;  2)  an  ornamen¬ tal  disk  or  spangle.  —  F.,  fr.  It.  zecchi'
=== leaf 755 ===
'no,  ‘coin’, dimin.  formed  fr.  zecca,  ‘a  mint’,  fr.  Arab. sikkah,  ‘a  die  for  stamping’.  Cp.  sicca, sequin,  n.,  ornament  on  women’s  dresses.  — Named  in  1802  after  the  French  ch'
...
'osus,  ‘a  religious  discourse’.  Cp.  It.  sermone, Sp.  sermon,  which  are  of  the  same  origin  and meaning  as  OF.  sermon.\nDerivatives :  sermon,  tr.  and  intr.  v.,  sermon-er, n.,  sermo'
=== leaf 756 ===
'net,  sermonette  (qq.  v.),  sermonettino (q.v.),  sermon-ic,  sermon-ic-al,  adjs.,  sermon- ic-al-ly,  adv.,  sermon-ics,  n.  pi.,  sermon-ize, intr.  and  tr.  v.,  sermon-iz-er,  n. sermonet, se'
...
't.  ‘shaped  like  a  ses¬ ame  seed’,  fr.  Gk.  ar(oa(j.oeiSr)i;,  ‘like  sesame or  sesame  seed’,  which  is  compounded  of  cnrjCTa- p.ov,  ‘sesame’,  and  -oeiSt)?,  ‘like’,  fr.  sTSoc, ‘form,'
```


## [2026-09-06T21:32:32.652Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlf=lambda i:t[:i].count('\\f')\nfor m in re.finditer(r'xer',t):\n    s=t[max(0,m.start()-80):m.start()+260].replace('\\n',' ')\n    if 'xero' in s or 'xerasia' in s or 'xeroderma' in s:\n        print('leaf',lf(m.start()),'|',s[:320]); print()\nEOF"
}
```


## [2026-09-06T21:32:34.042Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('DEV.txt',encoding='utf-8',errors='replace').read()\nlf=lambda i:t[:i].count('\\f')\nfor m in re.finditer(r'(?i)elixir|iksir|iksîr',t):\n    print('leaf',lf(m.start()),'|',t[max(0,m.start()-200):m.start()+700].replace('\\n',' ')[:900]); print('---')\nEOF"
}
```


### [2026-09-06T21:32:35.139Z] TOOL RESULT

```
leaf 236 | ic,  epidermis,  exodermis,  hypo- dermis,  leucoderma,  pachyderm,  taxidermy, xeroderma. dermal,  adj.,  pertaining  to  the  skin.  —  A  hybrid formed  fr.  Gk.  Seppa,  ‘skin’  (see  prec.  word), with  -al,  a  suff.  of  Latin  origin. dermat-,  form  of  dermato-  before  a  vowel. dermatalgia,  n.,  pain  in  

leaf 277 | v,  ‘dry medicinal  substance,  cataplasm’,  fr.  ‘dry’. See  serene  and  cp.  xero-. Elizabeth,  1)  fern.  PN.;  2)  in  the  Bible,  the  name of  the  wife  of  Aaron.  —  Late  L.  Elisabeth,  fr. Gk.  ’EXELaotJUeft,  ’EXtaafte-r,  fr.  Heb.  Elishebha', lit.  ‘God  is  an  oath’.  For  the  first  element  see  

leaf 629 | ee  phyllo-.  For  E.  -ous, as  corresponding  to  Gk.  -09,  see  -ous. Phylloxera,  n.,  a  genus  of  plant  lice  (zool.)  — ModL.,  compounded  of  phyllo-  and  Gk.  £75969, ‘dry’.  See  xero-  and  cp.  Xerophyllum. phylo-,  before  a  vowel  phyl-,  combining  form meaning  ‘tribe’.  —  Gk.  96X0-,  96X-,  fr.

leaf 629 | ice  (zool.)  — ModL.,  compounded  of  phyllo-  and  Gk.  £75969, ‘dry’.  See  xero-  and  cp.  Xerophyllum. phylo-,  before  a  vowel  phyl-,  combining  form meaning  ‘tribe’.  —  Gk.  96X0-,  96X-,  fr.  96X0V, ‘tribe’,  which  is  rel.  to  96X7),  of  s.m.  See  phyle. phylogeny,  also  phylogenesis,  n.,  evolut

leaf 755 | oding’,  kfayati,  ‘bums’,  OHG.  sera- wen,  ‘to  become  dry’.  Cp.  elixir,  xerasia,  xero-. Derivatives:  serene,  n.  and  tr.  v.,  serene-ly,  adv., serene-ness,  n.,  serenity  (q.v.) serenity,  n.  —  MF.  (=  F.)  serenite,  fr.  OF.  sere- nite,  fr.  L.  serenitatem,  acc.  of  serenitas,  ‘clear¬ ness,  s

leaf 755 | fayati,  ‘bums’,  OHG.  sera- wen,  ‘to  become  dry’.  Cp.  elixir,  xerasia,  xero-. Derivatives:  serene,  n.  and  tr.  v.,  serene-ly,  adv., serene-ness,  n.,  serenity  (q.v.) serenity,  n.  —  MF.  (=  F.)  serenite,  fr.  OF.  sere- nite,  fr.  L.  serenitatem,  acc.  of  serenitas,  ‘clear¬ ness,  serenity’,
```


### [2026-09-06T21:32:36.919Z] TOOL RESULT

```
leaf 141 | ,  M.  Sanguinetti  a  noté t^!>)  lâmi,  gomme  élémi.  Mais  l'ouvrage  où  il  a  recueilli ce  terme  est  trop  récent  pour  qu'on  en  puisse  rien  con- clure sur  la  nationalité  du  mot^. Elixir.  Esp.  et  portug.  elixir,  ital.  clisire.  (j'est  l'arabe wufc^iJÎ  el-ikslr,  terme  par  lequel  les  alchimistes  désignent la  pierre  philosophale,  la  matière  solide  ou  liquide  qui doit  servir  à  la  transmutation  des  métaux,  la  poudre  de projection  :  «In  ipsis  pulveribus  qui  a  philosophis  vocantur elixir.  w  (^Opus  mirabile  de  Mercurio  ad  ejus  Jîxationem^.^  On '   Lillré,  Dict. -  Journ.  asiat.  mal  1866,  p.  3aa.  On  peut  voir  aussi  Dozy,  Gloss.  p.  269. ^  L'auteur,  Alkulioubi,  est  mort  en  i()r)(). *  Dans  le  man.  lat.  n"  7 1  /17,  ancien  fonds,  de  la  Bibl.  nat.  p.  1 8  verso.  Le môme  volume  contient  un  traité 
---
leaf 141 | t^!>)  lâmi,  gomme  élémi.  Mais  l'ouvrage  où  il  a  recueilli ce  terme  est  trop  récent  pour  qu'on  en  puisse  rien  con- clure sur  la  nationalité  du  mot^. Elixir.  Esp.  et  portug.  elixir,  ital.  clisire.  (j'est  l'arabe wufc^iJÎ  el-ikslr,  terme  par  lequel  les  alchimistes  désignent la  pierre  philosophale,  la  matière  solide  ou  liquide  qui doit  servir  à  la  transmutation  des  métaux,  la  poudre  de projection  :  «In  ipsis  pulveribus  qui  a  philosophis  vocantur elixir.  w  (^Opus  mirabile  de  Mercurio  ad  ejus  Jîxationem^.^  On '   Lillré,  Dict. -  Journ.  asiat.  mal  1866,  p.  3aa.  On  peut  voir  aussi  Dozy,  Gloss.  p.  269. ^  L'auteur,  Alkulioubi,  est  mort  en  i()r)(). *  Dans  le  man.  lat.  n"  7 1  /17,  ancien  fonds,  de  la  Bibl.  nat.  p.  1 8  verso.  Le môme  volume  contient  un  traité  intitulé  Elixiris  composi
---
leaf 141 |  la  pierre  philosophale,  la  matière  solide  ou  liquide  qui doit  servir  à  la  transmutation  des  métaux,  la  poudre  de projection  :  «In  ipsis  pulveribus  qui  a  philosophis  vocantur elixir.  w  (^Opus  mirabile  de  Mercurio  ad  ejus  Jîxationem^.^  On '   Lillré,  Dict. -  Journ.  asiat.  mal  1866,  p.  3aa.  On  peut  voir  aussi  Dozy,  Gloss.  p.  269. ^  L'auteur,  Alkulioubi,  est  mort  en  i()r)(). *  Dans  le  man.  lat.  n"  7 1  /17,  ancien  fonds,  de  la  Bibl.  nat.  p.  1 8  verso.  Le môme  volume  contient  un  traité  intitulé  Elixiris  composilin  vera ;  il  semble linduit  de  Tliébreu  et  commence  par  ces  mots  :  rln  nomine  Adonay.') DES  MOTS  D'ORIGINE  ORIENTALE.  109 Iroiivo  aussi  nlexir,  c^medicina  alcliymice  praeparala??  (Ru- land,  Led'ic.  alchcm.)^  xir,  yxir  ai  y  sir. Le  mot  arabe  lui-même  n'est  autre  chose  que
---
leaf 141 |  269. ^  L'auteur,  Alkulioubi,  est  mort  en  i()r)(). *  Dans  le  man.  lat.  n"  7 1  /17,  ancien  fonds,  de  la  Bibl.  nat.  p.  1 8  verso.  Le môme  volume  contient  un  traité  intitulé  Elixiris  composilin  vera ;  il  semble linduit  de  Tliébreu  et  commence  par  ces  mots  :  rln  nomine  Adonay.') DES  MOTS  D'ORIGINE  ORIENTALE.  109 Iroiivo  aussi  nlexir,  c^medicina  alcliymice  praeparala??  (Ru- land,  Led'ic.  alchcm.)^  xir,  yxir  ai  y  sir. Le  mot  arabe  lui-même  n'est  autre  chose  que  la  trans- cription du  grec  ^vpov,  sec,  médicament  sec.  On  a  objecté^ contre  cette  origine  que  les  Arabes  transcrivent  le  ?  par JuM  sk  et  non  par  ^jf^  ks;  mais  il  existe  d'autres  exemples de  cette  dernière  transcription  ks  ou  qs,  et  M.  Defrémery en  a  cité  trois^:  ^^^luwJb  hoqsls^  buis  =  ^arv^os;  I^Uw.aj  haqsa- mût,  hi^cmi
---
leaf 271 | ouscous. Aldea,  hisp.  voy.  Aidée. Aldébaran. Aldég. Aldeia ,  pg.  voy.  Aidée. Alécarilh,  voy.  Alchimie,  93. Aleii,  esp.  voy.  Cheiranthe. Alépihe. Alerce ,  esp.  voy.  Raze. Alexir,  voy.  Elixir. Aleza>. Alfa,  voy.  Auffe. Alfabaca ,  pg.  voy.  Fabrègue. Alfabega ,  esp.  voy.  Fabrègue. Alfandega ,  pg.  voy.  Fonde. Alfanehe,  esp.  voy.  Fennec. Alfaneque,  esp.  voy.  Alphanette. Alfanex,  voy.  Fennec. Alfange. Alfarda,  esp.  voy.  Fardeau. Alfarroba,  pg.  voy.  Caroube. Alfena,  pg.  voy.  Henné. Alfeneiro ,  ;;§■.  voy.  Henné. Alfenim,  pg.  voy.  Alphénic. Alfeiiique,  esp.  voy.  Alphénic. Alferes,  pg.  voy.  Allier. Alferez,  esp.  voy.  Ailier. Alficoz,  esp.  voy.  Cabas. Alfido,  ital.  voy.  Fou. Alfier. Alfiere ,  ital.  voy.  Alfier. .\lfil,  hisp,  voy.  Fou. AlfîluB,  b.  lai.  voy.  Fou. Alfinde,  esp.  voy.  Oiinde. Alfino,  ital.  voy.  Fou. Alfonde
---
leaf 297 | jti7,  vov.  Kima. 1 ^62 DICTIONNAIRE  ÉTYMOLOGIQUE. Xir,  voy.  Élixir. Xirque,  esp.  voy.  Siroc. Xpïaua,  voy.  R usina. Xufi/a,  voy.  Alchimie. Yataghan. Yed. Yseloc,  voy.  Siroc. Ysir,  voy.  Elixir. Ysserop,  voy.  Sirop. Yxir,  voy.  Elixir. Zaffera,  ital.  voy.  Safre. Zafferano,  ital.  voy.  Safran. Zafre,  esp.  voy.  Safre. Zagaie. Zaibac,  voy.  Alchimie,  3. Zaibach,  voy.  Alchimie,  3. Zaibar,  voy.  Alchimie,  3. Zaïm. Zain. Zaino,  hisp.  ital.  voy.  Zain. Zalacca,  voy.  Rotin. Zambach,  voy.  Sambac. Zambecco,  ital.  voy.  Ghébec. Zanna,  ital.  voy.  Marfil. Zang,  voy.  Zéen. Zaouia. Zara,  ital.  voy.  Hasard. Zarbatana,  esp.  voy.  Sarbacane. Zarcào,  pg.  voy.  Jargon. Zarfa,  voy.  Alchimie,  /17. Zarne,  voy.  Alchimie,  29. Zarnec,  voy.  Alchimie,  39. Zarnich,  voy.  Alchimie,  29. Zarquâo,  pg.  voy.  Jargon. Zarra ,  pg.  voy.  Jarre. Zebd,  voy.  A
---
leaf 297 | LOGIQUE. Xir,  voy.  Élixir. Xirque,  esp.  voy.  Siroc. Xpïaua,  voy.  R usina. Xufi/a,  voy.  Alchimie. Yataghan. Yed. Yseloc,  voy.  Siroc. Ysir,  voy.  Elixir. Ysserop,  voy.  Sirop. Yxir,  voy.  Elixir. Zaffera,  ital.  voy.  Safre. Zafferano,  ital.  voy.  Safran. Zafre,  esp.  voy.  Safre. Zagaie. Zaibac,  voy.  Alchimie,  3. Zaibach,  voy.  Alchimie,  3. Zaibar,  voy.  Alchimie,  3. Zaïm. Zain. Zaino,  hisp.  ital.  voy.  Zain. Zalacca,  voy.  Rotin. Zambach,  voy.  Sambac. Zambecco,  ital.  voy.  Ghébec. Zanna,  ital.  voy.  Marfil. Zang,  voy.  Zéen. Zaouia. Zara,  ital.  voy.  Hasard. Zarbatana,  esp.  voy.  Sarbacane. Zarcào,  pg.  voy.  Jargon. Zarfa,  voy.  Alchimie,  /17. Zarne,  voy.  Alchimie,  29. Zarnec,  voy.  Alchimie,  39. Zarnich,  voy.  Alchimie,  29. Zarquâo,  pg.  voy.  Jargon. Zarra ,  pg.  voy.  Jarre. Zebd,  voy.  Alchimie,  5o. Zebeb,  voy.  Alchimie,  /i8. 
---
```


## [2026-09-06T21:32:46.988Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('total leaves',len(t))\nfor n in range(886,893):\n    print('=== leaf',n,'===')\n    print(t[n][:1500])\nEOF"
}
```


### [2026-09-06T21:32:49.564Z] TOOL RESULT

```
total leaves 903
=== leaf 886 ===
(i.e.  ‘alms,  charity’).  Cp. the  second  element  in  Melchizedek. tzadhe,  tzade,  n.,  name  of  the  19th  letter  of  the Hebrew  alphabet.  —  Heb.  tzade,  lit.  ‘fishing hook’,  fr.  tziidh,  ‘to  hunt,  catch,  capture’;  so called  in  allusion  to  the  ancient  Hebrew  form  of this  letter.  Heb.  tziidh  (whence  tzayidh,  ‘hunt¬ ing,  game',  tzayyadh,  ‘hunter’,  rtf  tzudhdh ,  ‘prey, net;  fastness,  stronghold’,  mltzodhah,  ‘net,  trap, snare’)  is  rel.  to  Aram.-Syr.  tziidh,  ‘he  hunted’, Ugar.  sd,  Akkad,  fddu,  ‘to  hunt’,  Arab,  sada, ‘he  hunted’.  Cp.  sadhe.  Cp.  also  Sidonian. tzar,  tzarina.  —  See  czar,  czarina, tzigane,  n.,  gipsy.  —  F.,  fr.  Hung,  cigdny,  whence also  G.  Zigeuner.  Cp.  ezigany.
W 6
ulterior
U
uberous,  adj.,  plentiful  (rare).  —  Late  L.  uberosus, from  the  L.  adjective  uber,  ‘fruitful’,  from  the noun  uber  (for  *uder),  ‘teat,  pap,  dug,  udder’. See  udder  and  -ous  and  cp.  exuberant. Derivatives:  uberous-ly,  adv.,  uberous-ness,  n. ubiety,  n.,  whereness  ( philos .)  —  ModL.  ubietas, formed  with  suff.  -tas  (gen.  -tat is),  fr.  L.  ubi, ‘where’  (whence  ubi-que ,  ‘everywhere’),  which stands  for  orig.  *cubi  (cp.  ali-cubi,  ‘elsewhere’), rel.  to  Oscan  puf,  pufe,  Umbr.  pufe,  ‘where’,  fr. I.-E.  *qwu-dhei- ;  cp.  OI.  kuha  (for  *kudha), OSlav.  kude,  ‘where’;  fr.  I.-E.  base  *qwu-, ‘where,  whither’,  whence  also  Vedic  ku,  Avestic ku,  ‘where’,  OI.  k
=== leaf 887 ===
rich’.  The  first  element  is  rel.  to  OE.  eedele, ‘noble’,  odel,  ‘home,  land',  ON.  odal,  ‘home, property’ ;  see  atheling.  For  the  second  element see  rich  and  cp.  the  PN.’s  there  referred  to. ulster,  n.,  a  long,  loose  overcoat.  —  Fr.  Ulster, the  Northern  province  of  Ireland:  so  called because  first  made  in  Belfast,  in  the  province Ulster.
ulterior,  adj.,  1)  later;  further;  2)  undisclosed.  — L.,  ‘farther,  beyond’,  compar.  of  *ulter,  ‘that which  is  on  the  other  side’,  rel.  to  ultra,  ultro, ‘on  the  other  side,  beyond,  besides’,  uls,  ‘be¬ yond’,  OL.  ollus,  ‘that  one’,  olim,  ‘formerly’, and  prob.  also  to  alius,  ‘another’.  See  else  and cp.  alias.  Cp.  also  ultima,  ultimate,  ultimatum, ultra,  ultra-,  ultroneous.  Cp.  also  outrage,  outre. For  the  ending  of  ulterior  see  1st  suff.  -lor.
ultima
umlaut
16/4
1675
Derivative:  ulterior-ly,  adv. ultima,  adj.,  farthest,  last,  final;  n.,  the  last  sylla¬ ble  of  a  word.  —  L.  ultima  fem.  of  ultimus,  ‘last’.
See  ultimate.
ultimacy,  n.  —  Formed  from  next  word  with  suff. -cy.
ultimate,  adj.,  final,  fundamental;  n.,  something ultimate.  —  Late  L.  ultimatus,  pp.  of  ultimare, ‘to  come  to,  or  be  at,  an  end’,  fr.  L.  ultimus, ‘last’,  superl.  of  L.  uls,  ‘beyond’.  See  ulterior  and adj.  suff.  -ate.  For  the  superl.  suff.  -timus  in  ul¬ timus  see  intimate,  adj.  and  cp.  posthumous, mar
=== leaf 888 ===
mbrella,  adj.  and  tr.  v. umbrette,  n.,  the  bird  called  Scopus  umbretta.  ■ — ModL.  umbretta,  fr.  F.  ombrette,  dimin’  of ombre,  ‘the  grayling'.  See  umber,  ‘the  grayling’, and  -ette.
Umbrian,  adj.,  pertaining  to  Umbria.  —  Formed with  suff.  -an  fr.  L.  Umbria,  name  of  a  district  in Central  Italy- Derivative:  Umbrian,  n.
umbriferous,  adj.,  giving  shade.  —  Formed  with suff.  -ous  fr.  L.  umbrifer,  'giving  shade,  casting  a shade,  shady’,  which  is  compounded  of  umbra, ‘shade’,  and  the  stem  of  ferre,  ‘to  bear,  carry’.
See  umbra  and  -ferous. umiak,  n.,  an  Eskimo  boat.  —  Eskimo, umlaut,  n.,  vowel  mutation.  —  G.  Umlaut,  ‘modi¬ fication  of  a  vowel’,  coined  by  the  German poet  Friedrich  Gottlieb  Klopstock  (1724-1803) fr.  urn,  ‘around,  about’,  and  Laut,  'sound'.  The first  element  derives  fr.  MHG.  umbe,  umbe,  fr. OHG.  umbi,  which  is  rel.  to  OE.  ymbe,  ‘around, about’ ;  see  ambi-  and  cp.  ampbi-.  The  second
umpire
1676
element  is  rel.  to  G.  laut,  ‘loud’ ;  see  loud  and  cp. ablaut,  anlaut,  auslaut.  As  a  technical  term  of grammar,  the  word  umlaut  was  introduced  by the  German  philologist  Jakob  Ludwig  Karl Grimm  (1785-1863).
umpire,  n.,  judge,  arbiter.  — •  ME.  nompere,  noun- pere,  fr.  OF.  nomper ,  earlier  nonper,  ‘not  equal’, fr.  non,  ‘not’,  and  per,  ‘equal,  peer’,  fr.  L.  non, ‘not’,  resp.  par,  ‘equal’.  See  non  and  peer,
=== leaf 889 ===
nd  adj.,  understand- ing-ly,  adv.,  understand-ing-ness,  n, undertake,  tr.  and  intr.  v.  —  ME.  undertaken ;  see under  and  take.  ME.  undertaken  is  prop,  a  loan translation  of  OE.  underniman,  ‘to  undertake’ (formed  fr.  under-  and  niman,  ‘to  take’),  which is  rel.  to  OS.  undarniman,  Du.  ondernemen, OHG.  untarneman,  MHG.  undernemen,  G.  un- ternehmen.  Cp.  F.  entreprendre,  ‘to  undertake’, fr.  entre,  ‘between,  among’,  and  prendre,  ‘to take’.
Derivatives:  undertak-er,  n.,  undertak-ing,  n. and  adj.,  undertak-ing-ly,  adv. underwrite,  tr.  and  intr.  v.  —  Loan  translation  of L.  subscribere,  fr.  sub,  ‘under’,  and  scribere,  ‘to write’.  See  under  and  write.
Derivatives:  underwrit-er,  n.,  underwrit-ing,  n. undies,  n.  pi.,  women’s  underwear  (colloq.)  — Formed  from  the  abbreviation  of  underwear with  -ies,  pi.  of  dimin.  suff.  -y. undine,  n.,  a  female  water  sprite.  — -  G.,  fr.  F.  on- dine,  introduced  by  the  French  poet  Pierre  de Ronsard  (1524-85)  fr.  ModL.  undina,  a  word coined  by  Paracelsus  fr.  L.  unda,  ‘wave’.  See undate  and  -ine  (representing  L.  -ina).  For  sense development  cp  .gnome,  sprite,  salamander,  sylph. undo,  tr.  v.  —  ME.  undon,  fr.  OE.  undon,  ondon, fr.un-,pref.  expressing  reversal,  and  don,  ‘to  do’. See  do,  v.
Derivatives:  undo-er,  n.,  undo-ing,  n. undone,  unfastened,  pp.  of  undo.  —  ME.  undon, pp.  of  undon,  ‘to  un
=== leaf 890 ===
  universolog- ist,  n.
univocal,  adj.,  having  one  meaning  only.  —  Form¬ ed  with  adj.  suff.  -al  fr.  Late  L.  univocus,  which is  compounded  of  L.  unus,  ‘one’,  and  vox,  gen. vocis,  ‘voice,  sound’.  See  uni-  and  vocal, unkempt,  adj.,  not  combed;  untidy.  —  Formed fr.  priv.  pref.  un-  and  ME.  kempt,  pp.  of  kemben, fr.  OE.  cemban,  ‘to  comb’,  which  stands  in  gra¬ dational  relationship  to  OE.  camb,  ‘comb’.  See comb.
unless,  conj.  —  Fr.  earlier  onlesse,  ontesse  that, i.e.  ‘on  less  that’.  Cp.  F.  a  moins  que,  ‘unless’, lit.  ‘on  less  that’,  and  see  on  and  less, unmeet,  adj.,  not  meet;  unsuitable.  —  ME.  un- mete,  fr.  OE.  unm&te,  ‘not  meet’.  See  priv.  pref. un-  and  meet,  adj.
Derivatives:  unmeet-ly,  adv.,  unmeet-ness,  n. unruly,  adj.,  hard  to  restrain,  disorderly.  —  ME. unreuly,  fr.  priv.  pref.  un-  and  reuiy,  ruly,  ‘amen¬ able  to  rule’,  fr.  reule,  ‘rule’.  See  rule,  n.,  and adj.  suff.  -y.
Derivatives:  unruli-ly,  adv.,  unruli-ness,  n. untie,  tr.  and  intr.  v.  —  ME.  untyen,  fr.  OE.  un- tiegan.  See  un-,  pref.  expressing  reversal,  and
tie.
until,  prep,  and  conj.  —  ME.,  prob.  fr.  unto  (with the  substitution  of  til,  ’till’,  for  to).  Cp.  Dan. indtil  and  Swed.  intill  and  see  unto  and  till, unto,  prep.  —  ME.,  contraction  of  *und  to.  The first  word  means  ‘up  to,  until’,  and  is  rel.  to  OE. dp,  OS.,  ON.,  OFris., 
=== leaf 891 ===
  the  past  participle.
urea,  n.,  crystalline  compound  found  in  the  urine of  animals  (biochem.)  —  ModL.,  fr.  F.  uree,  a word  coined  by  the  French  chemist  Antoine- Franqois  de  Fourcroy  (1755-1 809)  frond, the  base of  the  word  urine  (q.v.)  )
Derivative:  ure-al,  adj.
urease,  n.,  an  enzyme  occurring  in  soybeans (bio¬ chem.)  —  Coined  fr.  urea  and  suff.  -ase. uredo,  n.,  a  kind  of  rust  (bot.)  —  L.  uredo,  ‘a blast,  blight;  a  burning  itch",  fr.  urere,  ‘to  burn’. See  combust.
uremia,  uraemia,  n.,  a  morbid  condition  of  the blood  (med.)  —  Medical  L.,  compounded  of oupov,  ‘urine’,  and  octpia,  ‘blood".  See  urine, hemal  and  1st  -ia.
Derivative:  urem-ic,  uraem-ic,  adj. ureter,  n.,  the  duct  conveying  urine  from  the  kid¬ neys  to  the  bladder  (anat.)  —  Medical  L.,  fr.  Gk. oup^-r^p,  usually  in  the  pi.  ouprj-vjpEi;,  fr. oupciv,  ‘to  pass  urine’,  fr.  oupov.  See  urine. Derivatives:  ureter-al,  ureter-ie,  adjs. ureteritis,  n.,  inflammation  of  the  ureter  (med.)  — Medical  L.,  formed  from  prec.  word  with  suff. -itis.
uretero-,  before  a  vowel  ureter-,  combining  form denoting  the  ureter.  —  Fr.  Gk.  oup7;-rr]p.  See
ureter.
urethan,  urethane,  n.,  ethyl  carbamate  (chem.)  — F.  urethane,  coined  by  the  French  chemist  Jean- Baptiste-Andrd  Dumas  (1800-84)  from  the  ab¬ breviation  of  the  words  urea  and  ether  and  suff. -an,  -ane.
urethra,  n., 
=== leaf 892 ===
us.  See  use, n.,  and  -age.
usance,  n.  —  ME.  usaunce,  fr.  OF.  ( —  F.)  usance, fr.  user,  ‘to  use’.  See  use,  v.,  and  -ance. use,  n.  —  ME.  us,  use,  fr.  OF.  (=  F.)  us,  fr.  L. usus,  ‘usage,  custom,  use’,  fr.  usus,  pp.  of  uti,  ‘to use’,  fr.  OL.  oilier,  which  is  rel.  to  Oscan  uittiuf, ‘use’;  of  uncertain  origin.  Cp.  usage,  usance, usual,  usufruct,  usurp,  usury,  utensil,  utility, utilize,  abuse,  misuse,  peruse.
Derivatives:  use-ful,  adj.,  use-ful-ly,  adv.,  use¬ fulness,  n.,  use-less,  adj.,  use-less-ly,  adv.,  use¬ less- ness,  n.
use,  tr.  v.  —  ME.  usen,  fr.  OF.  (=  F.)  user,  fr. VL.  *usdre  (whence  also  It.  usare.  Proven?., Cat.,  Sp.,  Port,  usar),  freq.  of  L.  uti  (pp.  its  us), ‘to  use’.  See  use,  n.
Derivatives:  us-ed,  adj.,  us-ed-ly,  adv.,  us-ed- ness.  n.,  user  (q.v.)
user,  n.,  one  who  uses.  —  ME.  See  use,  v.,  and agential  suff.  -er.
user,  n.,  right  of  use  (law.)  —  OF.  (=  F.)  infin. user,  ‘to  use’.  See  use,  v.  For  the  subst.  use  of the  infinitive  in  law  terms  cp.  attainder  and  words there  referred  to.
ushabti,  n.,  a  small  figure  representing  a  servant, deposited  in  an  ancient  Egyptian  tomb.  — Egypt,  ushebti,  ‘lit.  answerer’, usher,  n.  —  ME.  ussher,  fr.  MF.  ussier,  uissier  (F. huissier),  fr.  OF.,  fr.  VL.  ustiarius,  ‘doorkeeper’.
fr.  L.  ostiarius,  of  s.m.,  fr.  ostium,  ‘door,  en¬ trance’.  See  ost
```


## [2026-09-06T21:33:00.239Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in list(range(272,282))+list(range(750,760)):\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',t[n])\n    nums2=re.findall(r'\\b(\\d{3,4})\\b',t[n])\n    print(n, nums, nums2[:12])\nEOF"
}
```


### [2026-09-06T21:33:01.776Z] TOOL RESULT

```
272 [] ['1834', '1241', '1961', '107']
273 ['501', '502', '503'] ['1847', '1931', '501', '502', '503']
274 ['504', '505'] ['1832', '1900', '1672', '1719', '1883', '1940', '504', '505']
275 [] ['1879', '1955']
276 ['506', '507'] ['506', '1729', '1540', '1603', '1600', '507', '1605', '1682', '1646', '1791', '1867', '686']
277 ['508'] ['508']
278 ['510'] ['1781', '1855', '510', '633']
279 ['512', '513'] ['512', '513']
280 [] []
281 ['516', '517'] ['1817', '1858', '516', '517']
750 ['1413'] ['141', '646', '1413', '1610', '1779', '1848']
751 [] ['1772', '1834', '1671', '1713', '1856', '1924', '1795', '1881', '1640', '1748', '1832', '1884']
752 ['1416'] ['474', '1781', '161', '1666', '1709', '1416']
753 [] ['1713', '1767', '1859', '1790']
754 [] ['1792', '1794', '1879', '1837']
755 ['1422'] ['1802', '1843', '1422', '1717', '1754']
756 ['1424', '1425'] ['1795', '1821', '1424', '1425', '429']
757 ['1426', '1427'] ['1426', '1427', '528', '642']
758 ['1428'] ['1428', '1802', '1745', '1800']
759 [] []
```


## [2026-09-06T21:33:09.031Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in range(893,903):\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',t[n])\n    print('=== leaf',n,nums,'===')\n    print(t[n][:400].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T21:33:10.685Z] TOOL RESULT

```
=== leaf 893 [] ===
id.  Cp.  also uvea,  uvula. uvanite,  n.,  a  hydrous  uranium  vanadate  (min¬ eral.)  —  Coined  fr.  uranium,  vanadium  and  subst. suff.  -ite. uvarovite,  n.,  a  calcium-chromium  garnet  (min¬ eral.)  —  Named  after  Count  Sergei  S.  Uvarov (1786-1855),  president  of  St.  Petersburg  Acad¬ emy.  For  the  ending  see  subst.  suff.  -ite. uvea,  n.,  the  posterior  colored  surface 
=== leaf 894 [] ===
andering’,  formed with  gerundive  suff.  -bundus  fr.  vagari.  See  va¬ gary.  Derivatives:  vagabond,  n.  and  intr.  v., vagabondage  (q.v.),  vagabondism  (q.v.) vagabondage,  n.  —  F.,  from  the  verb  vagabonder, ‘to  roam  about  like  a  vagabond’,  fr.  vagabond. See  prec.  word  and  -age. vagabondism,  n.,  vagabondage.  —  See  vagabond and  -ism. vagal,  adj.,  pertaining  to  t
=== leaf 895 ['1691'] ===
,  bodies  of  those  who were  slain  in  battle’,  wol,  ‘pestilence’,  OHG., MHG.  wal,  ‘battlefield;  slaughter’,  OHG.  wuol, ‘slaughter’,  and  cogn.  with  OIr .fuil,  ‘blood  ,  W. gweli,  ‘wound’,  Toch.  A  wal,  ‘to  die’,  Lith. velis,  ‘ghosts  of  the  dead’.  The  second  element is  rel.  to  OE.  heall,  ‘hall’ ;  see  hall.  Cp.  the  first element  in  Valkyrie. 1 vali,  n.,  t
=== leaf 896 ['1692'] ===
��,  nr^  (Hesychius), ‘web’,  L.  pannus,  piece  of  cloth’.  See  pane. Derivative:  van-ed,  adj. Vanessa,  n.,  a  genus  of  butterflies  ( entomol .) ModL.,  of  uncertain  origin, vang,  n.,  either  of  two  ropes  extending  from  the end  of  a  gaff  to  the  deck  ( naut .)  —  Du.  vang,  ‘a catch',  fr.  vangen,  ‘to  seize,  catch,  capture , which  is  rel.  to  G.  fangen,  of  s
=== leaf 897 [] ===
  —  A  hybrid  coined  fr.  vari¬ ola  and  suff.  -ite  (representing  Gk.  -Tty)?  ) ;  so called  from  its  smallpoxlike  appearance, varioloid,  adj.,  resembling  smallpox.  —  A  hybrid coined  fr.  variola  and  Gk.  -oei8 ‘like’,  fr. elSoq,  ‘form,  shape’.  See  -oid. variolous,  adj.,  pertaining  to,  or  having,  small¬ pox.  —  Medical  L.  varioldsus,  fr.  variola.  See variola  
=== leaf 898 ['1694', '1695'] ===
agential  suff.  -or. vau,  also  waw,  n.,  the  sixth  letter  of  the  Hebrew alphabet.  —  Heb.  waw,  ‘hook,  pin,  peg’;  so called  in  allusion  to  the  ancient  form  of  this letter. vaucberia,  n.,  a  genus  of  algae  (bot.)  —  ModL., named  after  the  Swiss  botanist  Jean-Pierre vaudeville velites fitienne  Vaucher  (1763-1841).  For  the  ending see  1st  suff.  -ia. vaudeville,
=== leaf 899 ['1696'] ===
  F.)  veine,  fr.  L. vena,  ‘blood  vessel,  watercourse,  vein;  natural inclination',  which  is  of  uncertain  origin.  Cp. venation,  vennel,  venose,  venule  and  the  first  ele¬ ment  in  venesection. Derivatives:  vein,  tr.  v.,  vein-ed,  adj.,  vein-er,  n., vein-ing,  n.,  vein-y,  adj.,  vein-i-ness,  n. velamen,  n.,  a  membrane  (anat.)  —  L.  velamen, ‘a  covering',  fr.  vel
=== leaf 900 [] ===
r’, vojina,  ‘war’,  Gk.  iep.ai  (for  ‘I  as¬ pire  to,  tend  to,  make  haste,  long  for’,  OE.  wap, ‘hunting’,  ON/  veidr,  ‘chase,  hunting,  fishing’, OHG.  weida,  MHG.,  G.  weidc,  ‘pasture,  graz¬ ing,  food;  pasture  land’,  are  prob.  derivatives of  a  denasalized  var.  of  the  above  base.  Cp.  the first  element  in  voivode. venery,  n.,  sexual  love,  (archaic).  —  From
=== leaf 901 [] ===
, ventricle,  n.,  cavity  in  an  organ  of  the  body.  — Fr.  F.  ventricule,  or  directly  fr.  L.  ventrieulus, ‘stomach,  ventricle’,  dimin.  of  venter,  ‘belly’. See  venter,  ‘abdominal  cavity’,  and  -cle  and  cp. ventrieulus. ventricose,  adj.,  bellied.  —  ModL.  ventriedsus,  fr. L.  venter,  ‘belly’.  See  venter,  ‘abdominal  cavity’, and  adj.  suff.  -ose. Derivative:  ventri
=== leaf 902 [] ===
��true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See very  and  -scope.  The  correct  form  would  be alethoscope  (fr.  Gk.  dcXvjffrji;,  ‘true’  and  -rsy.6- mov ) . veratral,  n.,  the  radical  C9H10O4  (chem.)  —  Form¬ ed  with  adj.  suff.  -al  fr.  L.  verdtrum,  'hellebore’. See  veratrine. veratric,  adj.,  pertaining  to  a  white  crystalline acid. —  Formed  with
```


## [2026-09-06T21:33:16.072Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -i \"xero[a-z-]*[^\\n]\\{0,220\\}\" KLN_1971.txt | head -20; echo \"=== xerasia ===\"; grep -n -o \"xerasia[^\\n]\\{0,200\\}\" KLN_1971.txt | head -5; echo \"=== elixir 1971 ===\"; grep -n -o \"elixir, n[^\\n]\\{0,300\\}\" KLN_1971.txt | head -3"
}
```


### [2026-09-06T21:33:19.473Z] TOOL RESULT

```
ugrep: error: error at position 318
][\x80-\xbf]|\xf4[\x80-\x8f][\x80-\xbf][\x80-\xbf]){0,220}
                             exceeds complexity limits___/


=== xerasia ===
218571:xerasia, xero-. 
269073:xerasia, n., excessive dryness of the hair {med.) — 
=== elixir 1971 ===
80459:elixir, n., 1) a substance supposed to prolonglife;
```


## [2026-09-06T21:33:22.316Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '269070,269110p' KLN_1971.txt"
}
```


### [2026-09-06T21:33:22.377Z] TOOL RESULT

```
anther. 

xerasia, n., excessive dryness of the hair {med.) — 
Medical L., fr. Gk. impact a, ‘dryness’, from 
the stem of ^palvetv, ‘to dry’, fr. 5>)p 6$. See 
xero-. 

xero-, before a vowel xer-, combining form mean- 
ing ‘dry’. — Gk. ^7)po-, ^p-. fr. ‘dry’, 

which is rel. to £ep6v, ‘the dry land’, and prob. 
cogn. with L. serenus (for *kseres-nos), ‘clear, 
fair, cloudless, serene’. See serene and cp. elixir. 
Cp. also the second element in Phylloxera, 
xeroderma, n., roughening of the skin {med.) — 
Medical L., coined by Erasmus Wilson (see 
xanthoma ) fr. xero- and Gk. 8£ppux, ‘skin’. See 
derma. 



xerophilous, adj., drought loving {bot.) — Com- 
pounded of xero- and -philous. 
xerophthalmia, n., a form of conjunctivitis {med.) 
— Medical L., lit. ‘dryness of the eye’, fr. Gk. 
^7)p6?, ‘dry’, and 6<p£aXp.6<;, ‘eye’. See xero- 
and ophthalmia. 

XerophyUum, n., a genus of plants, the turkey 
beard {bot.) — ModL., compounded of xero- 
and Gk. <puXXov, ‘leaf’. See phyllo- and cp. 
Phylloxera. 

xerophyte, n., a xerophilous plant (bot.) — 
Compounded of Gk. ‘dry’, and <put6v, 

‘plant’. See xero- and -phyte. 

Xerxes, n., king of Persia, who reigned 486-465 
B.C.E.; called the Great. — Gk. 3£pSir)<;, fr.
```


## [2026-09-06T21:33:30.466Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"xsaod\" \"x.aod\" \"xsudra\" \"x.udra\" \"xsvid\" \"x.vid\" \"xsaob\" \"x.aob\" \"xsufs\" \"x.ufs\" \"xsust\"; do echo \"### $p\"; grep -n -i -- \"$p\" BRT.txt | head -8; done"
}
```


### [2026-09-06T21:33:32.527Z] TOOL RESULT

```
### xsaod
### x.aod
7075:•  j.,  g.  ä-kä-  i)  Adj.  'manifestus';  a)  'der sehen  lässt,  wa^  er  tut,  sich  bei  dem  was er  tut  sehen  lässt,  es  offenkundig  tut': aiiyi^  kasHt  .  .  para.baraiti  'ka  (NS.) *hazatiha  *anskils>  iayusU.tJj;  6.  b)  'der sehcQ  lässt,  was  geschehen  ist',  spez.  von den  bei  der  äkä-  (s.  2)  Beteiligten,  'Offen- leger': hadä  asil  vakistScä  tiiananhä  xsa- 'irä.'a  yä  (NPn.)  /w  stanhai  a  pai^t  .  . 'ka  (NP.)  ar^ärSng  d^mänS  garö  Sfrao^äiiS "sammt  .  .  und  dem  Xs.,  welche  als  Offen- leger,  von  den  Frommen  ersehnt,  auf  dem Weg  zum  Haus  des  Lobs  den  Gehorsamen erwarten  werden"  Y.50,4'>.  2)  f.  'mani- festatio,  dilucidatio',  d.  i.  die  'Offenlegung' der  Taten  des  ersten  Lebens  bei  den  letzten Dingen  " :  dngvats  . .  yehyä  urvä  xraodattT (sd.)  cinvaiö  pinta  'kä  (Abi.)  "-  .  vor  der Offenlegung  an  der  Brlicke  des  Scheiders" V.  5/-I3;  —  ka  '^wöi  alu  'i,i  (NS.) arfdrSiig  ilyJ  "wird  deine  Offenlegung, o  A-,  den  Froramen  erwünscht  seini*"  Y. 4<V.8; — vahiitö  anktti  °>f(7j(AbL)-i-'?iV (sd.) ahüire  jasmtqm  Y.  60. 11.
8027:•  j.  iSasa-  Adj.  dnw.  «aa ja- (sd.) :  isan.- itäitya  ml  vlspS  at)hu}  astva  'Sftn  jitahm xraodat.urva  (sd.)  .  .  V.5.4.
10572:•  g.  (,  j.)  xraod-  V,  '(sich)  ängstigen', Praes.   i  xraed-,
10573:i)  'ängstigen':  karapanö  kavayascä  .  . ySiig  :^3  umä  £'a?:ä  xraodat  (3SKA.) äami  ". .  die  ihre  eigene  Seele  und  ihr eigenes  Ich  ängstigen  wird"  Y.  46. 11;  — s.  xraodat.',  2)  'sich  ängstigen,  bangen
10574:vor    — '    (Abi.):    dr?gvalS  .  .  yehyä    urvä xraodaitl  (3SKA.)  anvats  p?r»tii  äka  (sd.) ". .  des  Seele  bangen  wird  vor . ,"  Y.  5/.  1 3. Pu. :  xröiiiii  ('Geschrei')  dilan.
10575:•  j.  xraodaturvan-''  Adj.  'den  seine  Seele ängstigt'  sva.  'des  Seele  sich  ängstigt'; isanJtaitya  ml  vTspö  avhus  astitä  isas?m jit.as>m  (sd)  'va  ptsSJanus  "in  Kürze würden  mir  bei  der  ganzen  Menschheit ..  die  Seelen  voll  Angst,  die  Leiber  dem Gericht  verfallen  sein"  V.  5.4.
10576:-xr^-nianl-  Adj.,  PPA.:  S.  xiaod-.—  Pü.i  xrS- siin  dät  Ö  rm-Sa,  erl. :  tiiSän  ruvän  hai  garSI- män  *xrisilak  u  *aiiää/ai')  bat  hlnd  t.  — »  Das  Wort  ist  im  Anschluss  an  Y.5/.  13  b gebildet.  —  ')  S.  10  tmya.
11425:[des  Scheiders'  (beim  letzten  Gericht)**: .yehyä  urvä  xraodaUl  'vatspfntn  ska  (sd.)
### xsudra
8240:•  j.  ui9^e.tät-  f.-  ?  -:  yü  *xsudra  (sd.) *ya£   v3  yasanti  yat  vä  * Aqm.raS^vi}nti
10772:•  j.  xSaOri-  £  TVeib,  Weibchen'  (geschlecht- lich); a)  von  Menschen:  ar»dvT  .  .  hä yaozdahaili  . .  arsnqm  xsudrh  hä  -'^rinatn *garxi>qn  hä  ''hrinqm  paima  Y.  65.  5;  — yd^a  anyasHi  arsänff  avi  xsudra  °%nsiia hqm.v»rmavairtii  V.  iS.^z.  b)  von  Tieren (K.3mtl):yff  (nämhusirS)  ar/nq»t..tnasishm aojS  äbaraiti  . .  yS  '^rtsiia  aväiti  Yt  14. 1 2 ;  ^  avä  zJ  *'in'iu  hupatSJ?ma  ya  ui'trS
10863:•  j.  xSudra-,  xSuSra-''  i)  Adj.  'flüssig':, vTs/ia  tarsuca  (sd.)  'draca  A.J.  12,  Yt.ip. 58,    P.  42.  3)    n.    'Flüssigkeit';    uzw.
10869:KompE.,  A.(?)9.  —  PPfP.  einer  Basis  (ar.) *ksaud-,  woiu  noch  xsaoiah-,  xsudra-,  pm- xia0itra-%  s.  Hdm.  ZDMG.  38.  43i-  —  !'"■ (lu  F.,  Y.):  ^imxt,  (iu  V.);  /,«r.  -  ')  Unthom.; zSchr.  s.  IF.  //.  137.  NA.  xiivisli.  —  ")  S. noch  '^hilasmc.  —  3)  VgL  intay').  —  4)  Hds. hisf.  —  SS.  No.  2.
20920:asavJ  eara'iuslrOY.i2.6;\t-4.T,  —  zatö  be'.mraomi  (sd.)  ..yam  dahmqm  ..  S/rTlTm yS  a/ava  saraiiuärB  y.ip.  46;  Vr. //.  19, '  P.j;^.  c)  IPm.,  n.:  pairi  yäi/  hapta Yt5.io4,  14.2S,  IJ.47;  —  nazdyB  tqm^  karsvqrt  mairyB  apatat /ratgrase  "Vt.  ig.%3; upahi^tat  y  B  spitilfnB  zara^us'tr jYt.  ij.  21;  —  humäyQ.tarala  .  .  inhäma  yäü  ipm- 1 8, 10,  V.  JJ.  1 7 ;  —  uHa  nd  siitB  lihrava  yB  tahe  mainySul  dlmqn  Vr.  12.  4. spittimB  sara^ui/rB  Yt  13. 94  fodcr  zu  A); —  [  Von  undeutlichen  oder  verderbten  Stelleo jasani  il  ava»ha?ca  rafttai>ha!'a  (iwffi_j'5|  erwähne  ich:  hamSm  tatvahUtähtySusu- (zu  A)  ahurS  mazda  fasäiti  .  .yB  varthui  ruy!  syascU  dahmahya  Y.J2. 16;  —  tiBit sraosS  .  .  jasaiiti  .  .  yä  (s.  d)  äpB  Yt  /.  9;  i  ftä  xsnäul yä  v»r>ZSnä  hScä  Y.  4^- 1 ;  — 10. 100;  — yaiä  aha  vairyB  zaotä  frä  tnl  yä  (NDra.)  nara  gatum  baraite  F.^d;  — mrütg ya'iia  aha  vairyB  yä  zaota  frä  mZjaht  ..yB  xsudra  ham.raS%wayäH  V.lS. m^fi/f  Y.J.  25;  N._y7*,  Vr._j,  7; — paoinm  6a '^^i — yS  hapta  hmdu  V./,i8;  —  upa gtima  frabarat  yö  narif  asaonS  urva  H.  2.  |  a^a^u  (sd.)  rauhaya  yB  asärO  aiwyiixia- 15;  7i  8,  15;  —  bavat  aiwl.vanyh  yasi  yanti  V.l.  19;  —  psityh  ähitya  yä  anrö taxmS  kava  vlsiäspö  \X.iy.%i;    —   yim  mainyui  fraksrtniat  V.  20.  3;  —  aridvim
21031:I )  'heil  machen,  vollbringen,  vollkommen machen':  ka%a  möi  yani  yaoi  da?tiqm \^yaoi]dam*>  yqm  *hud3iiaos  . .  "ob  mir wohl  fiir  die  Dalnä,  die  ich  vollkommen machen  will,  für  die  des  einsichtigen  . ." Y.44.^;  —  dasnqm  pnn'S  yaoidaiiüa V.  10. 19;  —  yJ  hvqm  aiahvqm  yaoiäätte iuinatilißa..'V.5.2i;io,ig;  —  arfdvjm sBrqm  ..yä  ..  arsnqm  xSudra  yaotda%aUi yH  . .  häirisinqm  sq%äi  *gar7Wqn  yaosda- haiti  ¥.65.2;  —  Aa  (näral.  artdvt)  m? aps  yaoidaiäiti  Y.6'5. 5.  2)  'rituell  voll- kommen machen,  den  religiösen  Vor- schriften gemäss  bereiten,  in  den  gehörigen Stand  setzen' :  atwyS  xadkrä  frabaröil yaozdäta  dahmS.pairistä  Y.  (J5, 10;  — yaozdstqm  zao'^rqm  Yt  10.  120;  — xao'iiranqm  .  . yaoidstanqin  'W.I4-4')  Yt. 5.63;  ™  sao'>:räbyS  yaozdutnbyö  pairi- aaharsilbyS  Yt.  5.  8 ;  —  Au^?m  aismsm yagsdatim  hupairistim  Y,  7/.  8;  — aismanqm  yaoidätanqm  /rasnätagibya zastadbya  V.JÄ19;  —  aSsm^misA.)  ..hikUs *ragcaspaitJltqm  aiahebfnja  *yaosdätqm (APm.)Y.62.io.  c)iiat/rab?r>tarf{sA.) yat  ä^ras!a  agvqm  %raxtim  yaoiddhati^ N.  74;  T3-  3)    'wieder   rituell   voll-
21228:jAw.:  i)  mit  Ind.:  ^°  aiAlA  amS  mkanie spanasia  irista  . .  ka  hl  asti  aha  V.3.  36; iX  36,  37,  12.  i;  —  y  .  .  caratd  dva  mS apajw>tayaaa  V.y.49;  —  hs para  mintS daSvS  .  ■  y  maiys  maitm  xhtdra  avi franhirftaiti  y  vä  mafys  .  .  xsudranqm *pairi,gmrvayäti  V.  Ä32;  —  hs  ba  .  . arhtqm  MtyS  y  na  paurva  frabda  (Sp. 984  o) /rabdsJrajB  framalxaiti  V.  j8.  40; 34,  46,  54;  —  y  aoxte  aiia  . .  a%a  *ha *x/ayete..  haxäsit (sd.)  ü.g;  7;  — y  hakat *amrute  . .  aliü  *ratu/rii y5 . .  N.24;  — ta^a  y  paiti.barvnti  yä  .  .  äjayaurra N,54;  —  yl>  sSne  piÜr^m  jainti  . . yas»*'^ tat . .  täyus  . .  para.baraiti  dasa  (sd.)  oSj/ päili  afsl  aiayai(sd.)  Y.  13. 10;  —  aät y  bavaiti  avijpastS  sasta  .  .  ta  hascit upajbayäte  Yl  13.  69;  46;  —  yO  nars snaHmt  usihiltaiti  a^at  hl  ag^r^ptam  (sd.) y  frasusaiti  altai  hl  avaoirist»m  {sd.)  y . . Y.4.1T,  —  al^  zr  narS  paityeinti  (sd.) *aslS.vitotus  pgsanaiti  yasla'>''  isui..p»ia- naiti yasca^..Y .4.^^^^; — h^m  ita  (s.Ntr.) tltao^ra  bavairiti  (Sp.  939  O.)  yasj*^  tava frabannte  drvantö  . .  ".  .  dann  .  .  wenn (sie)  dir  darbringen  . ."  Yt.5. 94,  2)  mit Konj.  (oder  Inj.);  y  .  .  masdayasna  .  . nassum  frajasqn  ku%a  . .  v^myqn  "ange- nommen den  Fall:  die  M.  stossen  aul einen  Leichnam  .  .,  wie  .  .?"  V.  6. 36: 5.45,  Äi,  4,  J&i;  —  y  •■  spä  avaca va  bavat , ,  kuha  . .  vjrxyqn  . .  masdqyasna V.  13.  39;  35;  — y  . .  masdayasna  bal^atai (sd.)  fravasänte  katärö  paurvB  ämayänie (sd.)  V.  7. 36;  —  y  iavani  (sd.)  aiwi.- sasls  . .  eis  aiAhe  asti  balfazd  Yt  J4.34; —  y  afvS  zaata  (sd.)  frayatäiti .,  zaoiars gatava  N,  tf/;  70;  —  y  ahmt  nmlne  . . nairika  daxstavaiti  arthal  y  vä  ..  *aipi.- irytS.gatus  isd.)  altala  .  .  V.5.  59;  — y pouruiaist^a  hanjasänte . .  t^m  i^ra  ha*- Jasante  V,  7,44;  YL//.6;  —  yas/a^>  .  . väcim  paiti  taBtii' {sd.)  ar?hat  nsil.. täyus .  .  para.baraiti  Y.J3.40;  —  y  ma^äia frayazantt  .  .  rüsit  t^ra  airyä  daiähävS /ras  hyätYt.i4.^&;  — y paoirim . . itryntäl .  .y ' . ,  ktrmtät'  ava  hö  miryaite  anämStS ZT  ais6  Y.y.^T,  —  nthenyesi:  yeti/a  alte asti  . .  gar>mBkva  (sd.)  vjiänte  y  vä  aiU gar^ma  (sd.)  i^ars^a  stamaruM  .  .  apa.- daiai  .  .  aiühai   haca  .  .  bavainti  p»sB.-
21263:. ,  aparaöhayäe  y  v  naimsm  y  v  ä«'- /um  y  V  cahru/um  y  V  paatartkum '^■ig.y,  Y.6.32*,  l6.2*; — yä  *xsudra(ßd.) *y'il  y  yazmti  y  v°  *hqm.ralhwpnii y'v' ..  N.  61.  n)  in  aülimiliger  Ver- wendung; xrafstrMn  ava.janaita  maotrim dänSjiaritm  y"  v'  hama  duyt  laile  kahyä- cit  .  .  xrafstranqm  ava.janyät  y  v  .  . zaOta  "das  Xr.-Geschmeiss,  die  kömer- schleppende  Ameise  soll  er  im  Sommer töten,  zweihundert  Stück,  dagegen  (zwei- hundert Stück)  beliebiger  Xr.s  soll  er  im Winter  töten"  V.  16. 12  {?).
### x.udra
8240:•  j.  ui9^e.tät-  f.-  ?  -:  yü  *xsudra  (sd.) *ya£   v3  yasanti  yat  vä  * Aqm.raS^vi}nti
10772:•  j.  xSaOri-  £  TVeib,  Weibchen'  (geschlecht- lich); a)  von  Menschen:  ar»dvT  .  .  hä yaozdahaili  . .  arsnqm  xsudrh  hä  -'^rinatn *garxi>qn  hä  ''hrinqm  paima  Y.  65.  5;  — yd^a  anyasHi  arsänff  avi  xsudra  °%nsiia hqm.v»rmavairtii  V.  iS.^z.  b)  von  Tieren (K.3mtl):yff  (nämhusirS)  ar/nq»t..tnasishm aojS  äbaraiti  . .  yS  '^rtsiia  aväiti  Yt  14. 1 2 ;  ^  avä  zJ  *'in'iu  hupatSJ?ma  ya  ui'trS
10859:xäudra-
10863:•  j.  xSudra-,  xSuSra-''  i)  Adj.  'flüssig':, vTs/ia  tarsuca  (sd.)  'draca  A.J.  12,  Yt.ip. 58,    P.  42.  3)    n.    'Flüssigkeit';    uzw.
10869:KompE.,  A.(?)9.  —  PPfP.  einer  Basis  (ar.) *ksaud-,  woiu  noch  xsaoiah-,  xsudra-,  pm- xia0itra-%  s.  Hdm.  ZDMG.  38.  43i-  —  !'"■ (lu  F.,  Y.):  ^imxt,  (iu  V.);  /,«r.  -  ')  Unthom.; zSchr.  s.  IF.  //.  137.  NA.  xiivisli.  —  ")  S. noch  '^hilasmc.  —  3)  VgL  intay').  —  4)  Hds. hisf.  —  SS.  No.  2.
15636:•  j.  pairiS&x&udra-,  •xtiutra-  Adj.  'dem der  Same  versiegt  isf;  narS  °'hrS..jafdka paraMaxsta  Yt  i"].  54;  —  yat  hatiS  vä taurtirö  v3  'drS  vS  bavSt  V._y.  19;  — yat  sam/  paraJrüyäH  *naäa.sjmanasca 'dras^  V,  ij.  50.
16384:•  j.  pipivah-  Adj.,  nur  fem.  pipyßst-  'die Milch  in  der  Brust  hat,  säugt':  yS  nairi- kam  yqm  apu^rqm  °pyBsim  va  apipyästm va  anasaxtqm  (sd.)  para  xludra  avi fra^hiTszaiti  ". .  eine  Frau  . .  gleichviel  ob
20920:asavJ  eara'iuslrOY.i2.6;\t-4.T,  —  zatö  be'.mraomi  (sd.)  ..yam  dahmqm  ..  S/rTlTm yS  a/ava  saraiiuärB  y.ip.  46;  Vr. //.  19, '  P.j;^.  c)  IPm.,  n.:  pairi  yäi/  hapta Yt5.io4,  14.2S,  IJ.47;  —  nazdyB  tqm^  karsvqrt  mairyB  apatat /ratgrase  "Vt.  ig.%3; upahi^tat  y  B  spitilfnB  zara^us'tr jYt.  ij.  21;  —  humäyQ.tarala  .  .  inhäma  yäü  ipm- 1 8, 10,  V.  JJ.  1 7 ;  —  uHa  nd  siitB  lihrava  yB  tahe  mainySul  dlmqn  Vr.  12.  4. spittimB  sara^ui/rB  Yt  13. 94  fodcr  zu  A); —  [  Von  undeutlichen  oder  verderbten  Stelleo jasani  il  ava»ha?ca  rafttai>ha!'a  (iwffi_j'5|  erwähne  ich:  hamSm  tatvahUtähtySusu- (zu  A)  ahurS  mazda  fasäiti  .  .yB  varthui  ruy!  syascU  dahmahya  Y.J2. 16;  —  tiBit sraosS  .  .  jasaiiti  .  .  yä  (s.  d)  äpB  Yt  /.  9;  i  ftä  xsnäul yä  v»r>ZSnä  hScä  Y.  4^- 1 ;  — 10. 100;  — yaiä  aha  vairyB  zaotä  frä  tnl  yä  (NDra.)  nara  gatum  baraite  F.^d;  — mrütg ya'iia  aha  vairyB  yä  zaota  frä  mZjaht  ..yB  xsudra  ham.raS%wayäH  V.lS. m^fi/f  Y.J.  25;  N._y7*,  Vr._j,  7; — paoinm  6a '^^i — yS  hapta  hmdu  V./,i8;  —  upa gtima  frabarat  yö  narif  asaonS  urva  H.  2.  |  a^a^u  (sd.)  rauhaya  yB  asärO  aiwyiixia- 15;  7i  8,  15;  —  bavat  aiwl.vanyh  yasi  yanti  V.l.  19;  —  psityh  ähitya  yä  anrö taxmS  kava  vlsiäspö  \X.iy.%i;    —   yim  mainyui  fraksrtniat  V.  20.  3;  —  aridvim
### xsvid
10985:•  j.,  g.  xSvid-  m.  'Milch';  im  Gegensatz zu  axBtay-  (sd.)  überhaupt  'flüssige  Nah- rung' im  Gegensatz  zu  fester:  pars  °isca (NS.)  äsaitisca'^  gsui  mal  "hervor  (geholt werde)  Milch  und  Fett  samrat  Fleisch" V.13.2%;  —  ■ilaica  (DS.)  azStayalFa''> Y.ßS.ii  —  am  äiStBis(sd.)  aAurB mohnm tasat  .  .  gavSi  'lihmlä'''  * AvS urusalibyS V.  25,  7;  —  *mmdäidyäi  (sd.)  «ftfem^)  Y. 1/.9.  a)  Du.  in  Verbindung  mit  äsütay- Du.:  "röa  (AD.)  äzuiti  yazamaiäeY.iG.Z; zit.  *F,5.  a)  pasca  xsavaidlm  ayara- namca  (soll  heissen)  "nach  sechs*'  Tagen" Vd.5.
13887:—  'canAö  (\P.)  ..  dri'gvati>\.4<).ii.; —  Ohne   Obj.:    vldvä    vidusl  mraotü    mä avaiähäi  pairikayai  . .  yä  duiystrya  yamXsVidvä  *aipi'^  djbävayat  ".  .  nicht  länger
20358:*  S-  (>  j)  '''ni^ndäidyäi,  man  . .  daidyäi Inf.  'im  Gedächtnis  zu  behalten,  eingedenk zu  bleiben';  *m>ndäidyai  yä  tut  mazdä SäiMi  "deiner  Willensmeinung  will  ich eingedenk  bleiben,  o  M"  y.44.8;  —  tat m0i  vJcidyäi  (sd.)  vaoüä  . .  vTduyi . .  t»Jnäl daidyai  Y.  Ji.  5;  —  yS  nS  alvS  at  ll  uyl '^rayöidyäi  türahe  *mmd3idyai  xSvidstn haptaidyai  nava  dasme  yei  vS  yae^ma  V. u.  9*>.
20359:*)  Ein  kabbalistisches  Gemengsel  aus  meist ^iSischen  Wörtern,  die  lum  guten  Teil  in andrer  als  der  ihnen  zukommenden  Bedeutung gebraucht  sind.  Vgl.  Sp.  Komm.  3.  134,  Dst. ZA.  /.  113,  Gdn.  KZ.  2/.  250,  Bthl.  IFAni. 6.  41,  IF.  lt.  139-  «i'id',  aus  Y.  44.  8  ge- nommen, soll  'ßnffach'  (od.  dgl.;  Pö.:  panj td  nn)  bedeuten,  s.  dazu  No.  I.  Entsprechende Bedeutung  ist  den  Wörtern  "yi,  %räy5idyäi, türahe,  xsvidim ,  hapläidyäi  beigelegt  (sd.),  die mit  den  Zahlwörtern  für  2,  3,  4,  6,  7,  8  in  Zu- sammenbang gebracht  worden  sind,  an  die  sie z.  T.  anklingen.
### x.vid
10985:•  j.,  g.  xSvid-  m.  'Milch';  im  Gegensatz zu  axBtay-  (sd.)  überhaupt  'flüssige  Nah- rung' im  Gegensatz  zu  fester:  pars  °isca (NS.)  äsaitisca'^  gsui  mal  "hervor  (geholt werde)  Milch  und  Fett  samrat  Fleisch" V.13.2%;  —  ■ilaica  (DS.)  azStayalFa''> Y.ßS.ii  —  am  äiStBis(sd.)  aAurB mohnm tasat  .  .  gavSi  'lihmlä'''  * AvS urusalibyS V.  25,  7;  —  *mmdäidyäi  (sd.)  «ftfem^)  Y. 1/.9.  a)  Du.  in  Verbindung  mit  äsütay- Du.:  "röa  (AD.)  äzuiti  yazamaiäeY.iG.Z; zit.  *F,5.  a)  pasca  xsavaidlm  ayara- namca  (soll  heissen)  "nach  sechs*'  Tagen" Vd.5.
13887:—  'canAö  (\P.)  ..  dri'gvati>\.4<).ii.; —  Ohne   Obj.:    vldvä    vidusl  mraotü    mä avaiähäi  pairikayai  . .  yä  duiystrya  yamXsVidvä  *aipi'^  djbävayat  ".  .  nicht  länger
20358:*  S-  (>  j)  '''ni^ndäidyäi,  man  . .  daidyäi Inf.  'im  Gedächtnis  zu  behalten,  eingedenk zu  bleiben';  *m>ndäidyai  yä  tut  mazdä SäiMi  "deiner  Willensmeinung  will  ich eingedenk  bleiben,  o  M"  y.44.8;  —  tat m0i  vJcidyäi  (sd.)  vaoüä  . .  vTduyi . .  t»Jnäl daidyai  Y.  Ji.  5;  —  yS  nS  alvS  at  ll  uyl '^rayöidyäi  türahe  *mmd3idyai  xSvidstn haptaidyai  nava  dasme  yei  vS  yae^ma  V. u.  9*>.
20359:*)  Ein  kabbalistisches  Gemengsel  aus  meist ^iSischen  Wörtern,  die  lum  guten  Teil  in andrer  als  der  ihnen  zukommenden  Bedeutung gebraucht  sind.  Vgl.  Sp.  Komm.  3.  134,  Dst. ZA.  /.  113,  Gdn.  KZ.  2/.  250,  Bthl.  IFAni. 6.  41,  IF.  lt.  139-  «i'id',  aus  Y.  44.  8  ge- nommen, soll  'ßnffach'  (od.  dgl.;  Pö.:  panj td  nn)  bedeuten,  s.  dazu  No.  I.  Entsprechende Bedeutung  ist  den  Wörtern  "yi,  %räy5idyäi, türahe,  xsvidim ,  hapläidyäi  beigelegt  (sd.),  die mit  den  Zahlwörtern  für  2,  3,  4,  6,  7,  8  in  Zu- sammenbang gebracht  worden  sind,  an  die  sie z.  T.  anklingen.
### xsaob
10710:•  j.  xsaob-  V.,  nur  Praes.  14  (Inkoh.) vu/sa-^^  'in  Aufregung  geraten', /u/  aspanqm  sri/a  (sd.)  xsufsqn  Yt./o.
### x.aob
10710:•  j.  xsaob-  V.,  nur  Praes.  14  (Inkoh.) vu/sa-^^  'in  Aufregung  geraten', /u/  aspanqm  sri/a  (sd.)  xsufsqn  Yt./o.
### xsufs
10710:•  j.  xsaob-  V.,  nur  Praes.  14  (Inkoh.) vu/sa-^^  'in  Aufregung  geraten', /u/  aspanqm  sri/a  (sd.)  xsufsqn  Yt./o.
### x.ufs
10710:•  j.  xsaob-  V.,  nur  Praes.  14  (Inkoh.) vu/sa-^^  'in  Aufregung  geraten', /u/  aspanqm  sri/a  (sd.)  xsufsqn  Yt./o.
### xsust
4910:yS  histaite  . .  'yar)ks  fohrpa  ifaSnake  (sd.) ^t-y-3>  —  vazr»m  ..  zardi/ (sd.)  °yat»ks\ frahioctsm  Yt.  10.  96;  —  /rat3rasy3n?m .  .  *pairis.:^axt>m  (sd.)  'yat>Aafie'^  Y.  11. 7.  a)  'Gerät  aus  Metall  (Eisen)';  hanhui draos^a  *mmataheea  (sd.)  'yaTjheca  (GS.)" V,  5.38.  a)spez.zumKochen, 'Kessel' i>: aum..yim  upairi  Afr^säspn 'yanha  pitsm paiata  . .  iafsatca  As  mairyU  . .  /ras  (sd.) "yaahB  fraiparat  V.^.ii.  a)  im  gAw. vom  glühenden  Metallstrom  beim  letzten Gericht;  auch  mit  :faSna-  und  xsusta-\^ (sd.):  aeSqm  töi  ä  anhat  ya'i^it  'yattkä adänäii  paouruyB  "so  ,dass  er  bei  deinen Heimzahlungen  durch  das  Metall  vor  ihnen den  Vorzug  haben  wird"  Y.^o.  7«'; — yä JBya  (sd.)  s^nghaiti  .  .  x^aims  'yartha  Y. 32.T,  —  yqm  xsnODm  räneidyä  (sd.)  du ,  .  'yanha  xsiista  Y.5/.9.
4934:•  j.  ayö-xäusta-",  ayaoxSusta-'^  n.  'ge- schmolzenes(flüssiges)MetaIl(Eisen)':Ai^ff- yäli  mam..ya>a  "ftffi  Yt.z/.ao,  a)  Be- zeichnung des  feurigen  Metallstroms  beim letzten  Gericht*:  vohu  x^aHnm  . .  xia- "^rjm  vairim  .  .  °t3m  yasamaide  Vr.  20.  i ; —  'tim  ..  marzdikam  %räyB.driyüm  S.2. 4;  —  °tahe  tnarzdikai  ^mySjiriyaove  S, /.4-
```


## [2026-09-06T21:33:53.454Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10855,10875p' BRT.txt; echo \"#### a-xsufta\"; grep -n -i \"axsufta\\|ä.xsufta\\|axsu\\b\\|a.xsaub\\|xsaob-\\|xsufta\" BRT.txt | head -10; echo \"#### axsaob\"; grep -n \"xsaub\\|x§aub\" BRT.txt | head"
}
```


### [2026-09-06T21:33:53.551Z] TOOL RESULT

```
•  j.,  g.  xSi-  f  'Not,  Elend':  x^3  (GS.)''> dangSm  ayU  (sd.)  Umanhö  Y.31.20;  — paiiistaße  xsayasca  (GS.)''  amayavay&sla Y.7/.  17;  —  xUm^'>  F.J.
Vgl.  xiayS.    —    Pü.;    inian  'Jammern'  (wozu Hbm.  AGr.  /.  2 14).  —  ')  Für  *xHyB,  'xHyasäi, *xSiy>ni  S  /pj,  ^/o. j.  xHvti/i   V.  2.  31:    liei   arAüA'j    t.   unter
dby  Google
S5S
xäudra-
xänao3'wo.t«ina-
55«
j.  xiuiia  F.  J:  lies:  xhriia.  1
•  j.  xSudra-,  xSuSra-''  i)  Adj.  'flüssig':, vTs/ia  tarsuca  (sd.)  'draca  A.J.  12,  Yt.ip. 58,    P.  42.  3)    n.    'Flüssigkeit';    uzw.
a)  alkoholische,  'Wein',  Plur.:  ya  *°efra''> *yat  vä  yatanii  yat  vä  * hant-rat^winti "den  Wein  wenn  sie  opfern  oder  mischen" N,  61.  b)  'Samenfliisstgkeit,  semen  virile': a/ra»Aarpzat  {&A.)  pairi  °ärät  V,  JÖ'.  16; —  sonst  Flur. ;  aridvXm  ..  yä  . .  arsnam °ärä  yaoläa^iaUi  Y.  ö'^.  2,  5;  F.^g;  — yaäsa  . .  arsäns  avi  'dra  xsakriiva  Aam.- vjrmavainti  (sd.)  V.  iJ.  32;  —  ya^  nä :^aptS  °dra  fräraobayeite  V.  18.  46;  —  yO näirikqm .  .'drS  avi  ^frarshamaitt  V.  i$.  7, 8;  JA  67,  Nik.i; — yai  maryß  niaslm 'dra avi  fraahfnzaiü  yat  vS  masyS  masySnqm 'dranqm  (als  Obj.)  *pairi  gmrvayäti  V.Ä  3  %  \ — /a^j^J  (statt  NSf.)''rfnl  hqm.rafiwayeiti (sd.)  dahmanqm  adahmanqmca  V.^iV.  6z; N.Ji;  — fravasayö  ..  ya  avam  *°orqtn^'> aiwyax^ayänti  yam  . .  zara^ustrahe  Yt 13.  62*>.
•)  Der  lur  Erde  gefallene  Same  de»  Zar.. von  Nairy0.saaha  aufgenommen  und  der  ArJdt>i übergeben,  wird,  im  See  Xqsaaya  ruhend,  von 99999  Frai-aiay  bewacht;  %.  Bd.  j2,  8,  9;  wei- tere» bei  West  SBE.  S7-  33.  47-  15,  105,  Dst. ZA.  2.  521,  Jh.  Zor.  21,  BöKLEN  Eschalo- logie  91.
Ableit.  —  iEL  i.  unter  xhiila-  und  Gdm.  sYt. 42«.  —  Pü.i  iiia-  (wozu  ZDMG.  36.  67),  lu N.  6r  erl.:  mai;  Npü.  (la  A.  3.  n):  Htm, Sfi.  (ebd.):  madhüni;  s.  noch  WZKM.  14.  202 No.  2.  —  ')  Nur  Yt.  /p.  58  und  ♦/j.  62.  — ')  YiA'i.  imdm.  —  3)  AP.  wie  avqta  undj^i}!«. Hd».  'not.  —  4)  Die  IF.  5,  60  gegebene  Zu- sammenstellung scheint  mir  semasiologiscb unmöglich.
•  j-,  g.  xäusta-  Adj.  'Üüssig*,  spcz.  'brei- flüssig'; a)  vom  Lehm,  sva.  'aufgeweicht': yäiia  nü  ma/yska  *xsvisti  (LS.)  '>  zjtiiS (sd.)  vfsä2'ayänti  V,  3.  3i'>,  b)  vom Metall  (Eisen),  sva.  'geschmolzen',  mit ayah-  n.  Bezeichnung  des  glühenden  Me- tallstroms beim  letzten  Gericht^*:  yqrn xstiütim  rSf\Sibyä  (sd.)  dh  ^!ci,l  iJ^rJ suxrä  .  .  aya»Ää  °tä  Y.  j/,  9;  —  *'lpm^''
F.5-
KompE.,  A.(?)9.  —  PPfP.  einer  Basis  (ar.) *ksaud-,  woiu  noch  xsaoiah-,  xsudra-,  pm- xia0itra-%  s.  Hdm.  ZDMG.  38.  43i-  —  !'"■ (lu  F.,  Y.):  ^imxt,  (iu  V.);  /,«r.  -  ')  Unthom.; zSchr.  s.  IF.  //.  137.  NA.  xiivisli.  —  ")  S. noch  '^hilasmc.  —  3)  VgL  intay').  —  4)  Hds. hisf.  —  SS.  No.  2.
•  j,  xStavay-''  m.  Name  einer  iramschen
Familie:  fravalays  ..yä  .. pi^anäAu  iaoa nijasm  (sd.)  't/fiwyS''  Vt.  79.37.
Ableit.  (s.  xilävay).  —  Et.?  VII.  lu  S  S6.  — ')  Wegen  avay.rvi  i.  Meillet  bei  Bgm.  Grdr, n.  1091.
j.  jri/i/,  a-xslal  (usw.):  s.  'j/J-.
•  j.  xätävaenya-  patr.  Adj.  'von  Xsläia stammend,  dessen  Nachkomme':  pouru- oilx//dis  (sd.)  'nyehe^''  a/aen^Yt.ij.iii;  — *xh'i'wraspaht  'nyehe^^  a/aensYt  ij.iii.
Ableit.  aus  *x}IJfa-  EN.  (s.  xitäfa«/-) ; iSuff.  vgl.  lis/ryarnT-;  s.  noch  No.  —  ■»  J  lo hat  xSlävayanait ,  das  wäre  patr.  Adj.  lu xs/m/ay-i  F  1  xstäiBtvatnythe.  Lesung  also unsicher.
#### a-xsufta
10710:•  j.  xsaob-  V.,  nur  Praes.  14  (Inkoh.) vu/sa-^^  'in  Aufregung  geraten', /u/  aspanqm  sri/a  (sd.)  xsufsqn  Yt./o.
#### axsaob
```


## [2026-09-06T21:34:05.259Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xsaoiah\\|xSaoiah\\|x.aoiah\\|xsaodah\" BRT.txt | head -5"
}
```


### [2026-09-06T21:34:05.318Z] TOOL RESULT

```
10869:KompE.,  A.(?)9.  —  PPfP.  einer  Basis  (ar.) *ksaud-,  woiu  noch  xsaoiah-,  xsudra-,  pm- xia0itra-%  s.  Hdm.  ZDMG.  38.  43i-  —  !'"■ (lu  F.,  Y.):  ^imxt,  (iu  V.);  /,«r.  -  ')  Unthom.; zSchr.  s.  IF.  //.  137.  NA.  xiivisli.  —  ")  S. noch  '^hilasmc.  —  3)  VgL  intay').  —  4)  Hds. hisf.  —  SS.  No.  2.
```


## [2026-09-06T21:34:07.683Z] TOOL CALL #29: Bash

```json
{
 "command": "ls site/pages/280.jpg 2>/dev/null; pdftoppm -f 280 -l 280 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg280 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T21:34:10.080Z] TOOL RESULT

```
site/pages/280.jpg
total 23516
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:34 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     484 Sep  6 17:33 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb   97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb   41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb 8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb   25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb  105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb  122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82065 Sep  6 17:34 pg280.png
```


## [2026-09-06T21:34:12.891Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg280.png"
}
```


### [2026-09-06T21:34:13.230Z] TOOL RESULT

```

```


## [2026-09-06T21:34:13.227Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T21:34:24.616Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD asuftan\"; grep -n -i \"āšuft\\|asuft\\|ašuft\\|āšōb\\|asob\\|ašob\" PHD.txt PHD_mackenzie.txt | head -15; echo \"### PHD sustan/soy\"; grep -n -i \"šustan\\|sustan\\|šōy\\|soy \\|šōy\" PHD.txt | head -15"
}
```


### [2026-09-06T21:34:24.678Z] TOOL RESULT

```
### PHD asuftan
PHD.txt:4095:turmoil āšōb.
PHD_mackenzie.txt:7829:transience frasawandih, sazisn, ward-    turmoil asob.
PHD_mackenzie.txt:11288:asob                              Cl)~    haftar                        \'-'¥,q)'
### PHD sustan/soy
161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
585:šimšār Lë"! | N ~] box tree. Sir [HLBA < A hlb’; $1 | M šyyr, N ~] milk. šīrēn [5/yn! | M syryn, N ~in] sweet. ~ih: sweetness. SiSag [$y$k! | N fifa) bottle, flask. škaft [Ар] = Skeft. škāftan, škāf- [sk’p-tn' | M ‘kk’ pt, N fikáftan] split, burst. Skarag [skik! | P *škr-] (bird) of prey. škarwīdan, škarw- [fklw-ytn' | M ‘fkrw-st, N fikarfidan] stumble, stagger. škastan, Sken(n)- [TBLWN-tn' < A N tbr; škstn!, škyn- | M ‘tkn-, N stkastan, fikan-] break. ^ i$n: breaking. škēbāģ [fkyp?k! | P kyb-, N #hëba] patient. ~ih: patience. Skeft [škypt! | P “#kyft, N šigift] hard; extraordinary, astonishing; very. ~ih: hardness; hardship, distress; astonishment. šken(n)-, ~išn, v. škastan. ških- [fkyh- | N šikth-] be broken. Skóf-, у. Skuftan. Skdfag [fRwpk! | N šukēfa] flower, blossom. Skoft [škwpt'] = škeft. 1$kóh [ол | M Ай] poor. --īh: poverty. *§k6h [kwh | N sukdh] dignity, majesty; fear. škuftan, &ЕбЇ- [škwp-tn! | N fukuftan] flower, blossom. Énàs-, v. Snaxtan. šnàsag [fn'sk! | P *$n*sg] knowing, knower; sense. ~ih: knowledge. šnāxtan, $nàs- [fm htn!, fie | M хіп, Чи s-, N fin-] know, recog- nize. šnāyēnīdan, šnāyēn- [sz dyn-ytn'] please, propitiate. ~išn: happiness. šnāyīdan, šnāy- [fr'd-ytn!] praise, propitiate. --i$n : praise, gratitude. šnāz [frc | (N šinā(w))] swimming. šnāzīdan, šnāz- [fr'c-ytn! | M $2? 2-, (IN šināw-)] swim. $nóhr [snwhl | М *fnwhr] gratitude, contentment. šnūmaģ [fnwmk! | M *fnwm-] satisfaction, contentment. &nó&ag [šnwšk! | N šunoša] sneeze. $nüg [šnwk' | M *fnwg] knee. šnūman [fnwmn! = Av. xsniimaine] propitiation. 86n [swn'] kind, manner. ~ig [-yk!] customary, ordinary. šūy-, v. Sustan. Sdy [std | N ~] husband.
589:šustan, šūy- [HLLWN-tn! < A V hill | М Swst, šwy-, N ~] wash. šuy [#04] hunger.
4268:wash šustan.
5297:niSustan!, niSistan!
```


## [2026-09-06T21:34:25.723Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### CHEUNG xsaub\"; grep -n -i \"xšaub\\|xsaub\\|xšaud\\|xsaud\\|\\*xšau\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T21:34:25.773Z] TOOL RESULT

```
### CHEUNG xsaub
8993:s.v. *xSaud. 
28933:of/with some (other) ‘scratch’ roots, notably *xšau and *xrà&. 
29360:*xSaub ‘to rustle, tremble’ 
29378:*xSaud 455 
29410:*xSaud ‘to wash’ 
55134:*xsaub (s.v.) 
57665:*xsaub 
57807:*braiH, *pas, *yap’, *xšau 
57808:*braiH, *paš, *xšau 
58373:*xsaud
```


## [2026-09-06T21:34:32.771Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29355,29475p' CHEUNG.txt"
}
```


### [2026-09-06T21:34:32.818Z] TOOL RESULT

```
EVS: 101b, 77b, 79b, 104a, 65a, 71a, 116b, 94b; Abaev, Slovar’ IV: 240 f.; Steblin-Kamenskij 1999: 
339, 416 


*xSaub ‘to rustle, tremble’ 

*AVESTAN: Y Av. *xSaob- (xsuf-) ‘to rustle, tremble’ = Liste: 17 

Pres. inch.: SUBJ. 3pl. YAv. xsufsan (Yt 10.113) 

*MIDDLE PERSIAN: (+ *a-) MMP ’’Swb, ВМР ’Swp /asob/ ‘turmoil, disturbance’ || (+ 
*yi-) MMP w(y)swb-, BMP wswp- /wisob-/ ‘to destroy, disturb’? = DMMPP: 57b, 
347b 

(+ *ui-) Pres. IND. 3sg. MMP wswbyd, BMP wswpyt /wisöbed/, 3pl. BMP wswpynd /wisobend/; 
Partic.: pres. MMP wswb’g, (pl) MMP wswb’g’n, perf. pass. (sec) MMP wyswbyhyd, MMP 
*wyswbyh'd; Inf.: BMP wswptn /wisuftan/ 

*PARTHIAN: ‘уур, "šwb ‘turmoil’ || (+ *ui-) w(y)swpt- (past stem) ‘to disturb, 
destroy’ = Ghilain: 95 | DMMPP: 57a, 347b 


*xSaud 455 


*SOGDIAN: ? CSogd. m-xwb- ‘to rush out, move forth’. © This hapax form cannot 
regularly derive from *a-xs(a)ub-, v. MacKenzie 1970: 124; Schwartz 1970: 293; 


Sims-Williams 1985: 56. Perhaps, it is a borrowing from Choresmian (cf. xwBy-) ? 
Impf.: IND. 3pl. CSogd. mxwbynt (C2 12V.9) 


*CHORESMIAN: xwfy- ‘to press’ = Samadi: 246 

*NWIR: (+ *a- NP 4suftan/asub- ‘to agitate, disturb’, Kurd. (Kurm.) 
(h)aZötin/(h)aZö-, (Sor.) aZütin/aZü- ‘to chase, rush; to jump’ || (+ *ui-) NP *gusuftan 
(lit., lex.) ‘to scatter, fade’ (attested in dictionaries as 372) 

*NEIR: (+ *abi-) ? Wa. vis(bI)v-/visovd-, wis(BI)v-/wisovd- ‘to wipe (off)’ (rather 
*xSaip/b ?) 

*SANSKRIT: ksobh ‘to rock, start to swing, tremble’ (RV+) = EWAia I: 440 

“PIE *k“ seub'- ‘to rock, tremble’ = LIV: 372 | Pok.: 625 

*IE COGNATES: Pol. chybaé ‘to rock, to move to and fro’, Lith. skubti ‘to start to 


hurry’, Goth. af-skiuban, OE scufan, Engl. to shift. 
*REFERENCES: Horn 1893: 8, 206; IIFL II: 548; Nyberg II: 216a f.; Steblin-Kamenskij 1999: 379; Werba 
1997: 344 f.; Cabolov 2001: 106 


*xSaud ‘to wash’ 
*AVESTAN: OAv. *xSaod- ‘to become liquid’, YAv. xSaodah- (n.) ‘gush, flush of 
water’ (Yt 10.14), YAv. xsuöra- (Yt 19.58), YAv. xSudra- ‘liquid, fluid’(Yt 13.62, V 


15.7 f., V 16.17, etc.) 

Partic.: perf. pass. Ү Ау. xsusta- ‘melted, liquid (of metals)’ (Y 31.3) 

*MIDDLE PERSIAN: MMP šwy-, BMP sws- (HLLWN-) /Sus-/ (past stem) ‘to wash’ 
c DMMPP: 320b 

Pres.: SUBJ. 3sg. MMP swyy’d; Partic.: perf. pass. MMP šwst; Inf.: BMP swstn /Sustan/ 

*PARTHIAN: Sw(w)d- ‘to wash’ = Ghilain: 64 | DMMPP: 320a 

Pres.: IND. 3pl. Swwdynd; Partic.: perf. pass. šwst; Inf.: šwstn 

*KHOTANESE: (+ *ара-, *pati-) ? LKh. pasoj- (inch. ?) ‘to be washed’ © SGS: 77 
*CHORESMIAN: xs- ‘to wallow’ (cf. MacKenzie IV: 533) = Samadi: 242 

*NWIR: NP sustan/Soy-, Kurd. (Kurm.) Sustin/So-, (Sor.) Sitin/So-, Bal. Sust, Sust/Sod-, 
Awrom. Sıtay/sor-, Abyan. S6sta/Sur-, Ab: S6sta/sur-, Anar. Suste/ Sur-, Ard. 
Soste/Sor-, Fariz. -Sust, Yar. -Sust, Gz. Sur-/Sus(s)-, Gil. (Rsht.) Sostaen/Sor-, Ham. 
Sostän/Sur-, Gur. (Kand.) sürin/-Sür-, Jow. bam-foft/a-fur-, Meim. bem-foft/a-fuzr-, 
Khuns. sür-/Sut, Suss, Nn. Suste/Sur-, Qohr. süsta/sür-, Sang. -Sost-/Suroen-, Siv. 
Sür-/sét, Shamerz. -Süst-/Suräm-, Sorkh. -šust-/šur- ‘to wash’. © The -r- frequently 
found in the pres. stems of modern dialects is probably analogical. It can be ascribed 
to the influence of the paradigms of (notably) dastan/dar- ‘to have, hold’, kistan/kär- 
‘to plant, sow’ (rather than possibly from a denomin. of Suhr ‘sperm’, as suggested 
by Nyberg II, ibid.). 

*NEIR: Sariq. XóXtuj ‘watering place’ (< *xsudra-StaHka-) 


456 *x&ij ? 


*SANSKRIT: ksod ‘to dissolve, disintegrate’ (RV) = EWAia I: 439 

*PIE © The IE correspondences of the common Пг. root are unclear. The comparison 
to Slavic (OCS xud» ‘small, bad’, etc.), by Pokorny is semantically difficult. W.P. 
Schmidt (Gs Henning: 377 f.) suggests a connection with Lith. skudrus ‘quick’, 
skaudrus ‘flowing quickly’ and several names of rivers in Lithuania, Skäudinis, 


Skaudupelis, etc. = LIV: 372 | Pok.: 625 

*REFERENCES: Horn 1893: 172 f.; KPF I: 142a; Ivanow 1926: 422; KPF II: 204; Christensen, 
Contributions I: 68, 166; Christensen, Contributions II: 59, 116, 160; Abrahamian 1936: 122; Lambton 
1938: 42a, 78a; Fraenkel П: 798b; MacKenzie 1966: 109; EVS: 104b; Nyberg П: 187b f., WIM I: 72; 
WIM II/1: 83; DKS: 70a, 223a f.; Blau 1980: 231b; WIM III: 117; Omar 1992: 608b; Cabolov 1997: 72; 
Werba 1997: 173 f.; Lecoq 2002: 121, 123, 126, 130 (passim); Korn 2005: 314, 387 


*xSij ? ‘to desire, long for’ 

*KHOTANESE: ksimj- ‘to desire, long for’ = SGS: 24 

*BACTRIAN: bo ‘good’ = S-W, Bact.: 235a 

*NEIR: Oss. І. exsyzgon, D. axsizge “pleasant; urgently needed’ 

© Considering the limited distribution, *xsij may be a regional borrowing. 
*PIE LIV: - | Pok.:
```


## [2026-09-06T21:34:53.919Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 193 194 198 199; do echo \"===== HRN leaf $n =====\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' HRN.txt; done"
}
```


### [2026-09-06T21:34:55.520Z] TOOL RESULT

```
===== HRN leaf 193 =====
- 171 —
Saa^isaa (Amin. Marc XIX, 2, llj^); arm. LW.
sahartsali,
774. HayiHteii *öiuh ziemen, können'-), Prae«. myed (Im-
person.).
aw. \^xsuy-, /sat/ft^ 'im Stande sein, vermögen ;
phlv. my(i)stan^ sät/at; lat. queö (^'qiiejo).
775. Seh *Nacht\
K5§. mc,
ap.;firt/yii]«?Ä Mes Nachts* ; aw. /sap', /sapan- Nacht*:
phlv. sap, saw(ik\ vergl. Sapak, N. pr. (Hörn, Mit-
teilungen, Heft IV, 29 No. 15); ai. ksdp-.
kurd. sew ; afy. spa ; oss. ä/jaw (44) ; bei. sap (862) ;
wa/. LW. smJ, sij'n. sa6, sar. /at, minj. ;^srfw?a, /asa/rr/.
Der ;<-Stamm findet sich vielleicht noch in np.
sebänröz^) (AM. sehärözT , wie jüd.-pers. ""'iNO^iJ),
sebänffäh, sebdnböl, sebänver u. a. m. erhalten.
77G. sahän Hirte, siiwän, IN2iir (Is. 1, 24).
Kas. cepän, cüptm, cap6 (vergl. V^ullers cüpdn),
aw. ysti.päna-; phlv. spän *Hirte' (AV.), supän
(FP61.), arm. LW. spat (aw. *ßu,paUi')^).
kurd. siwan ; aty. spün 'Hirt*, spankai 'Schäferbube' ;
bei. sipänk, n. mwäuK, safänk 03(57) ; wa/. s/)JJw, süpiin.
Die dialektischen c«/?i7w (auch kurd. cuwän 'Hirt',
cöpän 'Fleischer) sind jung. Das i der kurd. und
beluc. Form ist ebenfalls jung, es ist erst nachträg-
lich zwischen die zusammengerückte Gruppe sp, sw
getreten, also *sup% ^suw" — ^sp'', ^sw'* — siw"^ sip"
(Geiger* s Etymologie *sa — Praeüx — und |/^pö*- ist
falsch).
777. Htäften 'eilen', Praes. sitäb-em^ sitab, DNDl^iN (Jer.
48, 16).
*J E. Drouin*s Lesung suhanum uut* Münzen (Kevuc niumiä-
matique, 1890, S. 361) ist ebenso verfehlt, wie seine Qemmenentzifferungeii
(vergl. ZDMG. 45, 429 folgg.).
') Vergl. oben No. 179 Anm. _
5) IV^u/^ijufQoy, H. 8. Jarret, Aln-i Akbari-Transl. Vol. II, 13
Anm. 2.
*) Ilübsohmann, ZDMG. 44, 5ß0.
===== HRN leaf 194 =====
— 172 -
phlv. östaftan ') (vd. 7 (27) GL, 18 (98), Meii.) eilen,
arm. LW. staij, davon Denomin. stapim 'eilen.
aw. *aiwis + l^tap-, täpaj/eiti *iri Wärme, Hitze
bringen', dann tropisch-).
Zu aiwis vergl. oben np. hes- (No. 221).
778. sHden gehen; sein, werden', Praes. sev-em.
ap. \/^siya€', aslt/avam, asiyuva 'gehen, marschiren';
aw. {/sav-, suvaite'^) gehen'; ai. [/^cyav-, Ci/dvate 'fort-
gehen ; arm. cit 'Aufbruch', ciiem 'aufbrechen' (H.
No. 242).
kurd. eleu 'gehen', dicm; sify, soal 'werden, gehen';
oss. d. t. cäün 'gehen, schreiten, spazieren, fahren'
(319) ; bei. suta, siit, n. suöa, iud^a (322) ; wa;^. cduam,
si/n. oi\zafcam, sar. va]zevsam.
779. siirrän, serrün 'unablässig lliessend', slrän Kegen' (y),
sun-iden^), vergl. sär {äbsär), särulen, ,
ai. l^ksar-, ksdrati 'fliessen, strömen' (Geiger,
Etym. d. Bai. unter No. 66; bei. ö[ur 'Giessbach'
kann aber nicht verglichen werden, s. Htibsch-
mann, ZDMG. 44, 556).
780. Herrn 'Schaam'.
aw. fsarema- 'Schaam'; phlv. sarm *Schaam', sarm-
[gas 'Genitalien' (vd. 16 (5) Gl.).
oss. t. äfsdrm, d. äfsänni 'Schande' (121) ; LW. aty.
bei. (253) sarm 'Schaam', kurd. serm,
781. sest, sest 'sechzig*.
aw. yscasti- 'sechzig ; päz. säst (FPGl.); ai. saüi-,
kurd. FD. LW. sest; afy. speta,
782. susten Vaschen', Praes. söy-em^),
phlv. sustan, söyBnd^ söy(i)sn; kurd. LW. sustin
'waschen' (vergl. g. sustinUu neben sustmün) ; bei.
*) Pfiz. qastäftun^ qastäwidan (Men.) ist Unsinn.
*) An ursprüngliches ^sila^ten (vergl. jjuft aus jf*x^) darf man
wegen Praes. siiäb-em natürlich nicht denken.
^) Bartholomae, Ar. Forsch. III, 33 liest staitc.
*) Zum Teil unbelegt.
^j Reimt auf higöyetl, Vis und Rämln S. 70 Vers 6.
===== HRN leaf 198 =====
— 176 —
790. suma 'ihr.
aw. ynsmäka-, gä»*^. /smäka- euer; päz. suma; ai.
yuämdka-; arm. yer 'euer (H. No. 176).
oss. d. sinaxy t. suma/ ihr, euch' (225); bei. savä-
"\\\v\ saraiy 'euer (365).
791. stifnar *Zahl, Anzahl', summden (mit her- erzählen*).
g. simärtmün; Kä§. V. veresmörtdn , Q. öresmärdeff^
K. esmördemün, Z. veresmdrt^),
aw. I/"r/?ar-, märay^iti 'bemerken, sieh merken*
(y. 32, 6); phlv. sVmär (vd. 9 (132) Gl.), vergl.
ösmartan^ ösmar (Bund.), anösmär 'ungezählt' (Men. 49,
22); ai. {^smar- gedenken'.
kurd. azmardin (H.-Sch.), zimärtin zählen'.
np. sumurden (gegenüber ämär^ mer) ist aw. aim-r-
mar- {aiwisrnaretö), das allerdings yt. 14, 34 eine ganz
andere Bedeutung hat; np. nehmür 'zahllos hat die
ursprüngliche Form der Wurzel, smor-, am Besten
erhalten. Wegen phlv. ösmartan darf bei sumurdmi
nicht Entstehung im Satzsandhi angenommen werden.
792. sinä, sinäh 'Schwimmen', sinär, sinärlden.
aw. l^snClr, US snayaeta 'sich waschen'; ai. l^snä-,
sndii- 'sich baden.
oss. t. nähi 'baden', d. a^snun^ t. a^snin 'waschen*
(196).
Die Nebenformen sinäb^ sinäv, sinävtden erklären
sich entweder wie deryäw (No. 561) oder sie gehen
auf [/^S7iav' {gi\ vsio 'schwimmen', äol. raa», vavftt
'fliessen') zurück.
np. s ist im Satzsandhi oder durch Übertragung
entstanden.
793. Hnäyiten 'erkennen', Praes. sinäs-efn, shuls.
ap. /snäsatiy 'solle kennen'; phlv. snäxtav, sfinaPf,
snäsüntän.
kurd. 7fäfiin 'erkennen*, ez dinäsim.
Gehört zur arischen [/'San- (wie ap. adma, np.
*) Nirgends findet sich in den Dialekten das np. //.
===== HRN leaf 199 =====
^_ 177 -
dänisfen). Über den Vorschlag des ap. ;^ vergl. Bar-
tholomae, Ar. Forsch. III, 20, Indog. Forscli. I, 185;
Fr. Müll er' s Bemerkungen dagegen (WZKM. 4, 309,
348) hat Bartholomae soeben schlagend widerlegt
(Indog. Forsch. II, 260 folg.). Ap. /Jnas- entspricht
genau lat. gnösc-ö,
795. Hunüden, senlden *hören', Praes. sunev-em, sinev-em,
usnüden , Tliy^^N'O (Is. 1 , 2) , sinuften , sunuften,
sinuväntden (AM. S. 261 Zeile 1).
g. äsnuftmün.
aw. l/^srar-, surunaoiti 'hören'; phlv. vergl. äsnütan,
asnuvet *hören [srütan heisst nur 'recitiren etc.*] ; ai.
l^p'av- gfnoH *hören*.
bei. stway (353).
Bartholomae, Studien II, 43 erklärt das np. s
durch Übertragung; Fr. Müller, WZKM. IV, 355,
ist wenig überzeugend.
796. Höher {*söhr) *Gatte'.
aw. ^ysaudraka-, vergl. ;^i'wc/rflf- 'Same', /sdudra-,
np. söi^) *Gatte', phlv. söl (vd. 15 (29) Gl.) setzen
ein aw. ^/sauda- voraus, das diosolbe Bedeutung wie
^'yjaudraka- hatte.
797. sehr \Stadt', vergl. s(~u\ säristdn, sdrsän (Sahn. I, 209
Vers 1431/5).
ap. xsatf'a- 'Reich, Land'; aw. /sa^ra-; phlv. snirj
mtrestän, päz. sahr, suhrastän (PI^Gl.), chald. ft^lTki'nx,
de Lagarde, Semitica I, 42; ai. Icsaträ-.
Allgemein entlehnt.
Ein altes sehri 'edel* (aw. yßatirya-, ai. HatHya-)
scheint noch durchzuschimmern im ar. LW. sahnyatun,
PL sahärty 'persisches oder kurdisches Ross' (de Goeje,
Bibl. geogr. arab. IV, 277).
798. sehryär 'Herrscher*.
aw. *xia3rö.dära' ; phlv. (Inschr.) satrdarän.
*) Reimt auf möt, 8ähn. I, 155 Vera 472, öi, I, 43 Vers IGT.
Mazend.-Dial. bat o'in aufTallip^o.'» s/, wio auch ;///• (*ITjijir') otc.
Uorii, Gruuilri.<<s d. iieiip. KtynioI<>(;-i(>. 12
```


## [2026-09-06T21:35:15.826Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FFD pdf 31 (p.26) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==31' incoming/FFD/FFD_pages.txt | head -60; echo; echo \"=== FFD pdf 68 (p.63) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==68' incoming/FFD/FFD_pages.txt | head -60"
}
```


### [2026-09-06T21:35:17.762Z] TOOL RESULT

```
=== FFD pdf 31 (p.26) ===
[pdf page 31]
و فعلهای فارسی دری
11 شفتن. آشوفتن
آشفت + فارسی میانه 2311 + ایرانی باستان 18 - 2501 - *. برای 3و 12 -> آراست.
: دنا که صورت ضعیف ريشهٌ 75210 است» صورت اصلی لا« است» 0 پیش از ۲ به ؟
بدل شده است. ريشةٌ 35800 به معنی «لرزیدن» است. «آشوفت» زیر نفوذ «آشوب»
به‌وجود آمده است.
آشوب < فارسی میانه 2300 + ایرانی باستان ۸ - 35200 - 3*. برای 2 + آرای.
«کشفتن» هم از ربشةٌ 1520 آمده است. > کشفتن.
آفریدن
آفرید < فارسی میانه 2874 < ایرانی باستان ها - 87 - 3*. برای 3 و 1۵ > آراست.
آفرین + فارسی میانه 38:78 + ایرانی باستان 83 - 8۲ - 3*. 23 نشانه‌ای بوده است
که با آن از ريشه, ماده ساخته می‌شده است. ريشةٌ 7 به معنی («ستودن» است. در
فارسی میانه 21778, 31710487 به دو معنی به کار می‌رفته: ۱ -ستودن, آفرین کردن ۲ -
خلق‌کردن. در فارسی دری معنی «ستودن» در «آفرین» به جا مانده که به عنوان «صوت»
به کار می‌رود.
آگندن
آگند + فارسی میانه 28270 < ایرانی باستان 1۵ - 6۵۵ - 2*. برای 3و ها آراست.
ريشهٌ 1۵0 به معنی «نهادن و افگندن» است.
«افگندن» و «پراگندن» هم از ريشهٌ 1۵0 آمده‌اند. -> افگندن و پراگندن. در ایرانی
باستان 1۵8 دیگری هم بوده است که از آن «کندن» آمده است. > کندن.
آگن < فارسی میانه 284 < ایرانی باستان ۵ - 5۵2 - 3*. برای 8 -> آرای. "
آلودن
آلود + فارسی میانه 2130 < ایرانی باستان ۴3-۳0-1۵
برای #وقها + آراست. 8 به معنی «آلوده‌بودن» است.
آلای + فارسی میانه 213 < ایرانی باستان 8له-3-73۷*.


=== FFD pdf 68 (p.63) ===
[pdf page 68]
ماده‌های ماضی و مضارع فارسی دری سا ۳و۶
شو < فارسی میانه 32 + ایرانی باستان 32-۵*. برای 2 > آرای.
شست.
شست < فارسی میانه 5081 ج ایرانی باستان 3508-1۵*. برای 1۵ -> آراست. 7504
صورت اصلی 3۷8 است. 4 پیش از 1 به 5 بدل شده است. 7504 صورت ضعیف ريشةٌ
40 و آَن به معنی «تحریک کردن» است.
شوی < فارسی میانه 50 < ایرانی باستان 35200-8*. برای 2 آرای. «شور) به جای
اشوی» جدید است > جستن.
شکافت < فارسی میانه 531 < ایرانی باستان ۴2-31-1۵ برای 12 -> آراست. 2
پیشوند فعلی است. 831 صورت بالاندهٌ ریشهٌ قاا است و ۴۵۲ به معنی «شکافتن» است.
شکاف < فارسی میانه 5۶ + ایرانی باستان 2-3۶-۵*. برای 2 -> آرای.
شکست < فارسی میانه 5۵91 < ایرانی باستان ۹16۵۶-12*. برای 18 -> آراست. ‎٩1۵0‏
‏صورت اصلی ۶۵8 است. 4 پیش از ۲ به 8 بدل شده است. ۹24 صورت ضعیف ريشةٌ
4 است.برای‌ضعیف کردن ريشه #حذف شده‌است. 5۵74 به‌معنی «شکستن»است.
شکن < فارسی میانه 5۵7 < ایرانی باستان ۶1۸2-۵*. برای 2 -> آرای.
شکفت < فارسی میانه 5/1
شکف جشکوف ج فارسی میانه 501
شکیفت < ایرانی باستان ۴۶1۵1۲1۵. برای 18 - آراست. ‎٩1۸10‏ صورت اصلی ‎٩۳۵۲‏
```


## [2026-09-06T21:35:38.172Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 leaf ~255-265 (p45) ===\"; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if 'آشوب' in p and i<340:\n        print('leaf',i, p[:80].replace('\\n',' '))\nEOF"
}
```


## [2026-09-06T21:35:38.940Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON اکسیر\"; grep -n \"اکسیر\" MON_part1.txt | head -5; echo \"### MON آشوب\"; grep -c \"آشوب\" MON_part1.txt MON_part2.txt"
}
```


### [2026-09-06T21:35:40.345Z] TOOL RESULT

```
=== BQT v1 leaf ~255-265 (p45) ===
leaf 116 مقد مه صد وهفشت و ذیل : اکحوان ) » باتو (ذیل : طاریقه ) » بالنگوی خودرو ۱ (ذیل :
leaf 123 صد وپانزده اقتباس وقلید وترجبه و ردبرهان مجموعه در ۱۲۸۳ قمری مطایق ۱۸۷میلادی درم
leaf 210 اشارتمت بر ضی‌کامل و عقل کل » و او را ضس حلهیه گویتد ۷ - آب ۲ تش د نگ - یکس شالت
leaf 298 «سیخول» نیز کوبند . ۶ آقوت » با تای قرشت بر وز نکبود . بلغت‌زند ومازند(۱) بمعنی
```


### [2026-09-06T21:35:40.405Z] TOOL RESULT

```
### MON اکسیر
15846:اکسیر: تام (ا.) (کیم.) جوهری گدازنده 
### MON آشوب
MON_part2.txt:19
MON_part1.txt:28
```


## [2026-09-06T21:35:44.802Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15840,15860p' MON_part1.txt; echo \"=== BQT v1 leaf 255 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==256' BQT_v1_pages.txt | head -40"
}
```


### [2026-09-06T21:35:46.767Z] TOOL RESULT

```
شود مانند: اکسید آهن و اکسید ازت. 
اکسیدهای فلزی در طبیعت فراوانند. 

ا کسید اسیون: 0 آن (ا.) (شسیم.) 
عمل اکسید کردن» ترکیب جسمی با 
اکسیژن. حالت جسمی که | کسیده شده باشد. 
اکسیر: تام (ا.) (کیم.) جوهری گدازنده 
که ماهیت اجسام را تغییر دهد و کاملتر سازد 
مثلا جیوه را نقره و مس را طلا سازد. هر 
چیز مفید و کمیاب. دارویی که به عقیدة 
قدما هر مرضی را علاج می‌کرد. (تص.) نظر 
مربی و مرشد کامل که ماهیت اشخاص را 
تغیبر دهد. ا کسیر اعظم: (تص.) انسان کامل» 
شیج» پیشوا. 

اکسیژن: اه (.) (شیم.) گازی است 
بی‌رنگله بیبو؛ بی‌طعم» کمی سنگین ترا 
هو ا. یک لیتر آن ۰۵ ۰ گرم جرم دارد. 
قز ات کتفین .سول ات ورد ۱۸ 
درجه و فشار ۵۰ جو به سختی مایع می‌شود. 
در طبیعت به حالت ترکیب و آزاد فراوان 
=== BQT v1 leaf 255 ===
ی آشنا کر
خابة سک آنی است ۷ . خالهرا نیز گویند چنانکه گوبند «اين عمارت سه
آ ش لقن * کنابهازآنت کهکیرا | آشکوب است» بمنی مه حرتبه است - و بمعنی
چینه دبوارهم آمده اسث یمنی هر مرتبه که از
از عراعه آزارکسی رانگرانه: . < با ِ
سم ۲ 9 ار گنارند - وآسمادا نی کوینه  ٩‏
] شتی خواده - حلوا و طعاسی را یو ین 7
گوند که بعد از آفتی:.مسان دوستان بپز ند ۳ ح بفتح شالث بر وزن و۳9
مرن زارد مخذف « آشامد » باشد که ماضی آشامیدنست .
: ]شتا » بسکون ثاث و نون بالف
کید . ممروفت که قض ببگاله باشد ۴ -
تلور اه هو وا ليز گونن که شتا کننده
باشد - و شناوری و آب ورزی را هم گفته‌اند ۴
) شتینه پروزن و هعنی اشامت
۲ شفته » بنم نك بر وزن آلفند . بهم
برآهده و پریشان حال - و عاشق را گویند ۷
اشکو - باکاف بروزن چارسو ؛ مخفف
آشکوب است که هر مرنبه ازیوششی خانه‌باشد .
آ شکوب ؟. بروزن‌خا کروب . بمعنی
آسمانه و سقف خانه باشد - وهر موتبه ازیوشش
- وودمطنان خنصی است که بذانه شامای از
تحضق باخود آورده باشد وباشاهد وحدنتی رابطة
آشنایی بود .
] شناب « بر وزن ماعتاب . بمعنی
قتایی اد که اتتوزی و فا کففد اسخ 9 :
آشنا گر « بفتم کاف فارسی و سکون
۱ کند بیستر. جندبادستر , قندقیری* مخزن الادوبه » : فسطوریون 1251076120
«لت نایه» و رله ؛ شنها ۱ : ۲۸۷ ‌ و ۲۹۵ ج. بهلوی م29۳۵ «منای ۱۵۸: ۲
« دعارله ۱۸۹ ۰ . ۴ - مرکب اژ: پیشوند 2 ور اوستابی و پارسی باستان 1807
بمعنی شناختن « بارتولمه ۵۵4 > پهلوی 250086 « متون پهلوی ٩۸‏ *: « منای۲۹۸ *.
۴ - مرکب از : پشوند 2 + اوستابی 502 شنن » ساسکربت 5020 , حاشا20۵ ,
اسنی شرقی 9818 .استی غربی 257100 ۲ «بارنولمد ۱۹۲۸ - ۲٩‏ پهلوی 50۵1 , 51020
* دیشکرت ۰۷۵۹ ۷۹۰ * در پارسی شنا » شناو ؛ شناب » شناء , شنار » آشناء » آشناب » و در
ت کب آشناور و آشناگر و شناور و شناکر دیده مشود . در طبری 925۷1 , مازندرانی کنونی
ور 98110 « واژه نامه ۳۰۸ » . ۵ _ ره : آشنا .
ه آشتی _ پهلوی الم « مررکب از 2506 بمشی صلح و آرامش . دراوستا
کم < بارئولیه ۰۲۳۹۹ بر کب ۰۲۵ وا[ نثانٌ حاصل مصدر . هب آشفتن _
م رکب از "پیشوند 2 و1510800 اوستائی بمعنی مضطرب شدن ۰ نحريك شدن, در سانسکربت
6 د«بارنولمه ۲ ۵۶» خشم کرفن » مشب کردن - شوریدن . انقلاب . - بهیجانآمدن .
«لغت ناعد». آشکارا_ بپلوی 1 هسمنای۲۱۸» « تب رکگ۲۵ * اوراعالی
```


## [2026-09-06T21:36:10.461Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON کشفتن\"; grep -n \"کشفتن\\|کَشفتن\\|کشفته\" MON_part1.txt MON_part2.txt | head -5; echo \"### BQT v3 pdf 58\"; awk 'BEGIN{RS=\"\\f\"} NR==58' incoming/BQT/BQT_v3_pages.txt | head -50"
}
```


### [2026-09-06T21:36:12.555Z] TOOL RESULT

```
### MON کشفتن
MON_part2.txt:23534:(فع.) سوم شخص مفرد ماضی از « کشفتن». 
MON_part2.txt:23535:کشفتن: ۲:۱۵ (- شگفتن - شکافتن ] 
MON_part2.txt:23539:۱۳۹۴ فر هن فارسی معیر کشفتن 
### BQT v3 pdf 58
[pdf page 58]
lw

- وماه شب چهارده را یز میگویند(۱) ‎٩‏ .

ششی بانو ۴ -کنابه ازع ‎SS‏
‏است که آن زحل و مشتری و مریخ و زهره
و عطارد و قمر باشد.

ششی پستان - بنم ‎Ih‏ و کر بای
فارسی بروزن کرجستان ۰ زیرا کوبند که پستان
‎cle‏ او درم وبزر که و افتاده باشد - و کنایه‌از
زن پیر هم هنت - و بفتح اول دشنامی باشد
‎Ly;‏ چه آیشان را بسک نسبت کنند - و سکه
را یز کوبند که بتازی کلب خوانند .*

شش پنجه = بر وزن سرینجه ۰ دام
داروبی است که ‎NYT‏ کشنه بر وزن دشنه
میگوشد .

شش بندان ‎be‏ بای ابجد بر وزن
فرزندان » درخت ‎SU‏ صحرابی باشد » وآن‌سانند

. ‏کوبند‎ tele )۱(

(۷) چك: بفتح زا .

شش خانون

عشقه بردرختها پیچد و آرا بشیرازی ‎gala ole‏ "
ویعربی کرمة الاسود خوانشد.

شش آا - با فوقانیبالف کشیده طنبور
شش‌تار را گوبند چتانکه سه تا طنبوره سه تاره
را گویند ۰

شش تا 095 - بنتم زای‌شله‌دار(0)
و دال بی قطه (۳) , طنبور شش تار نواختن را
گوند - وق بجول باختن را هم کفته‌اند که
نوعی از قمار است.

شش ره -بفتح تا ‎chy‏ قرشت,روای
را کویند و آن بیخی است که چیزها بدان‌رنگه
کذدند .

شش ‎gan - FOG‏ ش‌بانوات
که شش ک وکب زحل و مشتری و مریخ وزهره
و عطارد و ‎wth ole‏

(۳) چك: - می‌نقطه .
```


## [2026-09-06T21:36:21.526Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if i<160 and ('شستن' in p or 'شست' in p):\n        print('pdfpage',i+1,'| شست hits', p.count('شست'), '|', p[:60].replace('\\n',' '))\nprint('---- شوی/شوهر ----')\nfor i,p in enumerate(t):\n    if 60<i<180 and ('شوی' in p or 'شوهر' in p):\n        print('pdfpage',i+1,'|', p.count('شوی'), p.count('شوهر'), '|', p[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T21:36:24.292Z] TOOL RESULT

```
pdfpage 23 | شست hits 1 | [pdf page 23] که ازآن راهپا وشمبها جدا شود - وفام‌جالوری ‎co
pdfpage 56 | شست hits 2 | [pdf page 56] Atte ‏شروان است - و نام یکی از فرزسزادهای ملك‎
pdfpage 57 | شست hits 4 | [pdf page 57] سازها بندلد ۰ ‎de - ٩‏ زلف ‎te‏ کیسو و ‎tile‏ 
pdfpage 58 | شست hits 3 | [pdf page 58] lw  - وماه شب چهارده را یز میگویند(۱) ‎٩‏ .  ش
pdfpage 60 | شست hits 1 | [pdf page 60] ols ANA  روز سنت است. شش ‎Oly‏ - با بای حعی بر
pdfpage 96 | شست hits 2 | [pdf page 96] ‎cod oly‏ ویکم  ‏در شین قطه دار با واومشتمل بر
pdfpage 121 | شست hits 2 | [pdf page 121] ys  شقو موری »با فان ومیم هردوبواو رسیده و ور
pdfpage 136 | شست hits 1 | [pdf page 136] ۱۳۳  که ‎OT‏ محراب - وئیزی انوان وعسارت و پل 
---- شوی/شوهر ----
pdfpage 83 | 1 0 | [pdf page 83] شملید است که حلبه وشبلیله باشد . شم. ۱ کوند ۴ 
pdfpage 90 | 1 0 | [pdf page 90] {Aa  رآن‌گیاهی باندکه بدان رخت شویند ‎٩‏ - ‎Ky
pdfpage 96 | 2 1 | [pdf page 96] ‎cod oly‏ ویکم  ‏در شین قطه دار با واومشتمل بر
pdfpage 103 | 3 4 | [pdf page 103] هومیزیدن ۱۳۱6 شوهیز ین ۱ ‎vine‏ موپیچیدن . | 
pdfpage 104 | 3 0 | [pdf page 104] ۳۱۳  ‎ply -‏ بشتن هرهت ۱ - وبکسر اولرثالی شبت
pdfpage 121 | 1 0 | [pdf page 121] ys  شقو موری »با فان ومیم هردوبواو رسیده و ور
pdfpage 132 | 1 0 | [pdf page 132] انجام  در ضاد تقطه دار با حروف تیجی مشتمل بر 
pdfpage 150 | 0 1 | [pdf page 150] ۷و۳ ‎jb‏ ز بان ‎tbe ald‏ را کوند که سخن اوستا
pdfpage 161 | 1 0 | [pdf page 161] ‎oly‏ سوم  ‏درعین .بی نقطه با خیم مشتمل بر چه
pdfpage 166 | 2 0 | [pdf page 166] ۳ات  باشد - و دام کنج اول است از گنجهای خسرو 
pdfpage 167 | 0 1 | [pdf page 167] Sur  که اورا بشوهر دهند - وبوم ماده را نی زگو
pdfpage 173 | 1 0 | [pdf page 173] بیان پانزدهم  در ‎ort‏ بی‌قطه با لام مشتمل بر
```


## [2026-09-06T21:36:39.416Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (55,56,57):\n    p=t[i]\n    print('=== pdf page',i+1,'===')\n    print(p[:2500])\nEOF"
}
```


### [2026-09-06T21:36:41.084Z] TOOL RESULT

```
=== pdf page 56 ===
[pdf page 56]
Atte
‏شروان است - و نام یکی از فرزسزادهای ملك‎
. ۱ ‏کیوی برادر الوشیروان هم‌هت‎
‏شریتا ۴ - با نای فرشت (۱) بر وذن‎
‏مسیحا » بلفت 5 وپازند (۲) پادشاه را گویشد.‎

شریدن ۴ = بر وزن رسیدن » بمعنی

تراوبدن باشد - و جنم اول و الی مشدد بروزن
غربدن | بمعنی رختن پی‌دریی باشد ببفاصله.
‎eau, ۵‏ :
سر یتو لقن ‎phe”‏ لون ونای قرشت
پروزن پربروفکن » بلغت زند ویازلد(۲) بمعنی
کشادن‌باشد. و شربتولمی بعنی کشامم‌وشربتونید
‎Mag yin‏

‎ol‏ دهم

‏در شین نقطه دار با سین بی‌نقطه مشتمل برشش لغت و کنایت

‏سپ » بنتح اول وسکون ‎QU‏ و بای
فارسی » بمعنی جهنده و خی زکننده باشذ ۵ -
و بمعنی غیبت (۳) هم‌آمده است که در مقابل
حضور است.

‏شست = بروزن دست » چند ممنی‌دارد:
۱- عددی است معروف که بعربی ستین گویند
و معرب ‎oT‏ شصت باشد ۰.۱۷ ۲- بمعتی زار
‎ath‏ و آن رسمالی است که کبران و هنود بر
کمربندند و ب گردن‌اندازند . . ۳-نش‌ویشتر
فاد و رکه زن باشد و بعربی مبضم خواهد .

‏(۱) چك : پا تا .

‎. ‏چك: ژلد ویاژلد‎ (x)

‏> - انگشت بز رکه‌باندکه انگشت زهگیراست
و بعربی ابهام گویند. 0 - بمعنی زهگی‌باشد
و آن انگفتر ‎gust.‏ است که از استضوان‌سارند
و در الگشت ابهام کنند و دروقت کمانداری زء
کمان را بدان گیرنه و ‎WT‏ باعتبار انگشت‌ابهام
شت میگرند.  ‎-٩‏ قلایی باشدکه ‎holy‏
‏کیرند ۷ . ۷ -مشراب را کویند و آن
چیزیت که بسنی از سازها مثل ‎Lig‏ وقالون
و عود و طنبور ورباب را ‎oly‏ وازند. ۸ تلر
روده و ابریشم و مفتول برنج و فولاد باشد که‌پر

‎٩‏ سدر له پادشاهان طبرستان دوشروین اشت:شروین(دوم) بن‌رستم بن سرخاب‌بن فارن
این‌شهربار ‎op‏ شروین(اول) بن شرخاب بن مپره‌ردان بن ‎Ghee‏ بن باو (جدملوگ باوند)بن شاپور

‏ابن کیوی بن قباد . «مرزبان نامه مصحح قزویتی تهر ان ۱۳۱۷

‏مقدمه ص و

‎: ‏ورگ‎ Cat Sy? lest . pAtaxshab ‏پپلوی‎ .sh(a)rita. » - ۴

‏باروچا ۲۳۹ : ‎sharitaih‏ (یادشاهی) .

‏( جاری شدن » روان شدن) )4 شران ‎gael‏ ۰۷۷۹ .

‎kshar ‏باستان ربشة‎ sae . guj = ۴

‎sh(a)riténitan, ‏مز‎ - ۴

‏( ونظایرآن) » پپلری ۷912۵۵0 ۰ کشادن «بونکر۸۳» . ورك: باروچا ۲۳۹ .

‏6 ظ.مصحف « شپ» ‎Cem)‏

‏۷ - اوستا - ‎XShvashti‏ (شست) « پازنه

‎۰۴ ۸۷۱ ‏اسشق‎ « shpéta uit. shest ‏ع‎ ws: shashtf - ott ‏هندی‎ . shast

‎. Shast ‏کیلکی‎

‏۲ - من شت بدربا فرو فکندم

‏ماهی برمید و ببرد شتتم .
معروفی بلشی.«لفت فری ‎٩8۲‏ .

‏# هزو - رك: لفات ‎oll Bie‏ کتاب .

=== pdf page 57 ===
[pdf page 57]
سازها بندلد ۰ ‎de - ٩‏ زلف ‎te‏ کیسو
و ‎tile‏ رسن وکمند و امثال آنرا گوبند .
۰ شت گاء زنان باشد - و با اول مکسور
مختصر اشت باشد که در مقابل‌برخاست‌است (.

شتگانی ۲ - ‎SG‏ و سکون
‎yt‏ و فوقانی و ‎SE‏ فارسی بالف کشیده و ‎Op‏
‏بتحتالی رسیده » بمعنی بنیاد و پی ‎caylee‏ باشد
ویعربی ‎Ll‏ خوانند ۴ -

شست گرا = بقتح‌کاف فارسی, کتابه
از تبراندازان و کمانداران ‎ash‏ چه 0

Ha TL, ‏کماندار‎

HATA

شستقه - بروزن خفته ۰ ممروف است ۴
که از شتن و یاکیزه کردن باشد - و بمعنی
رو پاك و دستارچه هم کنته‌اند و ممرب آن
شنجه (۱) است.

سین « بنتح ‎Syl‏ وسکون آخ رکه‌بون
‎ach‏ وحرکت ثالی مجپول » صدف را گویند

کهکوش ماهی باشد - و نامیه را نیز کفته‌الد

مطلقاًبمنی هرچیز که آن نمو کند و ببالد
و یفزایه - ونی شکر را ‎ga‏ میگوبند -
و بمعنی خار ترنجبین هم هست - و رحم را لیز
کفته‌اند که بچه‌دان باشد ؛ و بجای حرف ثالی
شین شله‌دار (») ‎gh‏ بنظر آمده است .

بیان یاز دهم

درشین ‎aba‏ داریا شین نقطه دارمشتمل بربیست ونه لغت و کنایت

شش ت بح اول عددی است ممروف ©
- وضم اول چیزست سفید
بسرخی ‎asl LL‏ گوشت
ویجگرمتصل‌است ‎V‏ وبادزن
‎dey py‏ دل باشد و کنایه
از پستان‌رم‌وسست و آویخته

عت .

شش[ ماسید هم .

نم اول . کنابه از مردم شش

بد دل وید اسرون ونامرد باشد.

شش ]دار » بروزن پس انداز, کسی
را کوبند که شش بجول بازی میکرده باشدوآن
‎ey‏ از قمار است - و ‎Waly‏ پیز کفته‌اند ‎(vr)‏
‏یعنی کی که لرد بازی کند - و شخصیرا ‎Di‏
‏گفته‌اند که شش کوی الوان مدور از چوب با
غیر ‎OT‏ بهر دو دست بگیرد برهردستی سه عدد
در هوا اندازد و میگیرد هر شش را چنانکه بر
زمین لمی‌افتد وپبوسته چپار عدد آن درهواست

. ‏شنجة()‎ : ose )۱(

۱ -رل: شتن (ح) .
۴ - زقب درکه اوساز شتگانی عمر

. ‏دار‎ ales - : ‏چك‎ (x)

۴ - از:

(۳) چك: گوبشد.

شت (شت) ۳- کانی (یسوند سبت) .

که قلب کمبه‌بود شستگانی محراب .
« ابوالفرج رولی ۲۰ * .

۴ -اسم مفعول از «شستن»(بم‌اول,وییزوبفتح آن بمعنی شته) . ‎٩‏ -وآن‌شمارمایت

بی‌پنج وهفت,دویرابر سه؛ اوستا- ‎xshvash‏ (شش) ‏ پهلوی ‎shash‏ » هندی‌باستان 5890 «
ارمنی ‎veg‏ .5 ع ‎shesh‏ , افتانی ‎shpazh‏ . استی ‎dxsiz‏ .رخی ‎shadh, shal‏
بقیه در ‎baie‏ ۱۲۹۷

=== pdf page 58 ===
[pdf page 58]
lw

- وماه شب چهارده را یز میگویند(۱) ‎٩‏ .

ششی بانو ۴ -کنابه ازع ‎SS‏
‏است که آن زحل و مشتری و مریخ و زهره
و عطارد و قمر باشد.

ششی پستان - بنم ‎Ih‏ و کر بای
فارسی بروزن کرجستان ۰ زیرا کوبند که پستان
‎cle‏ او درم وبزر که و افتاده باشد - و کنایه‌از
زن پیر هم هنت - و بفتح اول دشنامی باشد
‎Ly;‏ چه آیشان را بسک نسبت کنند - و سکه
را یز کوبند که بتازی کلب خوانند .*

شش پنجه = بر وزن سرینجه ۰ دام
داروبی است که ‎NYT‏ کشنه بر وزن دشنه
میگوشد .

شش بندان ‎be‏ بای ابجد بر وزن
فرزندان » درخت ‎SU‏ صحرابی باشد » وآن‌سانند

. ‏کوبند‎ tele )۱(

(۷) چك: بفتح زا .

شش خانون

عشقه بردرختها پیچد و آرا بشیرازی ‎gala ole‏ "
ویعربی کرمة الاسود خوانشد.

شش آا - با فوقانیبالف کشیده طنبور
شش‌تار را گوبند چتانکه سه تا طنبوره سه تاره
را گویند ۰

شش تا 095 - بنتم زای‌شله‌دار(0)
و دال بی قطه (۳) , طنبور شش تار نواختن را
گوند - وق بجول باختن را هم کفته‌اند که
نوعی از قمار است.

شش ره -بفتح تا ‎chy‏ قرشت,روای
را کویند و آن بیخی است که چیزها بدان‌رنگه
کذدند .

شش ‎gan - FOG‏ ش‌بانوات
که شش ک وکب زحل و مشتری و مریخ وزهره
و عطارد و ‎wth ole‏

(۳) چك: - می‌نقطه .

۱ - نیز «تش انداز» خورشی را کویند که بانعم مرغ و پیاز و کدو و بادنجان وشکر

ونوعی از ترش ی کنند .
؟ - قس:شش خانون.شش عروی.
# شش بنج - شش وپنج ‎Gee)‏
‏3 شدی بهر حفت ونه در رلج

۴ - قی: شش ‎th‏ : شش عروس .

نقد مت فتاد در شش پنج .
امیرخرو دهلوی . «فرهنك ‎Hels‏

# شش‌پنجز لای ح شش وپنج زان ‎Cem)‏ :

شش پنج زان داو برده

قیه از ‎dente‏ ۱۲۹۹

اما همه لقش ‎Ch‏ شمرده.
خاقانی شروانی ‎Kae ge‏ تظام» -

شفنی 561150 «اسمی۷۸۳». کیلکی ‎shish‏ , نپرانی ‎shish‏ . ۷ - اوستا -51لا5.اففانی
22181 , ساسکریت 6۷25 (دمیدن ) «هوبشمان ۷۸4 ؛ پهلوی ‎sush‏ . افتانی ‎Saghai‏ .
وخی ¢ ‎shush‏ .سربکلی ‎sill‏ «اسشق۷۸4» بعربی ‎ay LT‏ (رثه) گویند .

# هشن - بفتح اول وسوم , مخفف «شستن» (ه.م.) ورگ: شست .

# شستی - ‎pe‏ اول وفتح سوم . پهلوی ‎shustan‏ , کردی ع ‎Shushtin‏ (تطهیر) «

بلوچی 5۳06۵4088 ,511۵00881 ,50۵228 (نطهیر »پاك کردن " استحمام کردن) ‎IVAN GL!‏
بقول ‎Fr. Miiller‏ از ساسکریت ‎kshud‏ (زدن , ‎Jub‏ کردن). اما درفارسی به‌عنی تطهیر»
پاك کردن ‎(OT ey)‏ آمده » فس: یازند ‎Shustan‏ (تطهیر ‎(Or SLs‏ > هویشمان۷۸۲ »,
دزفولی ‎shoshtan‏ «امام» , کیلکی ‎shostan‏ » اورامانی ‎a> (c+) shot‏ اورامان ‎Ay‏ .
```


## [2026-09-06T21:36:54.769Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (102,103):\n    print('=== pdf page',i+1,'===')\n    print(t[i][:3000])\nEOF"
}
```


### [2026-09-06T21:36:56.630Z] TOOL RESULT

```
=== pdf page 103 ===
[pdf page 103]
هومیزیدن ۱۳۱6
شوهیز ین ۱ ‎vine‏ موپیچیدن . | باشد که برروی خمیر نان پاشند ۷ - و زمین
‎ines‏ شیارکردن و زرات مودن باشد. ‎As‏ کردم وبرزیگر و زراعت کننده را یز
‎get‏ فك ۴ = بنتع اول والی‌وسکون‌بون | کفته الد ۷ .
ودال‌ابجد, بمعنی‌باعت وسبب ‎Saley‏ هرچیزباشد. شو لیز ب4 ‎tne‏ اول و تحنالی آخر »
‎Lb ge‏ - بنتح اول و ثالی و دال بالف | نام مسجدی است غیر معلرم ۸ .
کشیده , شنوا وشنونده را کویند ۴ . شوه = بنتح اول و انی وظهور هاء بر
شو ندان « بروزن‌قلمدان,جم‌شوند ۴ | وزن و معنی شبه است و آن سنکی باشد سیاء
است که اسباب مواد و بواث باشد .متی سببها | وسبك ‎٩‏ - و باخذای ها بممنی سبب و بامت
و ماده‌ها و پاعثها + و ماده باشد ۱۰ .۷
شو ‎Sad‏ * = بنم اول و کر ‎su‏ شوی ۰ بنتع اول وکر ‎GE‏ و سکون
ر سکون سین بی تقطه و فوقالی | بممنی فسون | تحتالی معروف ؛ بمعنی پیراهن‌استوبعربی‌قمیص
وعلاج باشد . کویند - ریم اول و تحتانی مجهول » شوربا
شی یز » با اول بثالی رمیده و ‎att‏ | وآهاری را کوبند که بر روی تار پارچه‌ای که
بتحتالی کشیده و بزای نقطه دار زده , سیاء ‎ails‏ میبافند مالند ۱۱ - و بضم اول و سکون ‎BE‏
‎TL‏ ویعربی حیةالسودا خوانند و ‎oT‏ تضبي | و تحتالی بمعنی شوهر باشد ۱۴ - و بممنی‌شتن

۱ - از : شومیز -یدن (پسوند مسدری) . ۴ - از ‎jal,‏ «فرهتکه ‎gals‏
‎Yoo‏ ور : شوه. ۴ - جپانگیری برای ‎gl‏ همنی بیت ذبل را از منوچهری دامغانی
آورده و ‎je‏ فرهنکه نظام ازاو پیروی کرده است:

این سماع خوش ‎aly‏ الا زيرويم را شمه از کوش دل و کوش شوددا شتوند.

ولی‌عصراح دوم دردبوان منوچپری صور ذیلآعده: تفه از کوش‌دلو کوش هوبداشود...

وش _وسویدانشود ....هوش‌سوبد! نشود.... گوش‌سوبدانشود.رك:دبوان‌منوچهری. بکوشش دییرسیاقی

ص ۱۲ . ۴ - جمم «شوند؟ ‎Gen)‏ از دساتیر . 8 رك : شوت »و رك ۱
رشیدی + ۹ = ‎jy‏ «فرهنگه ‎tolls‏ شنز «رشیدی» ‏ شینیز ‎Coa) pe Coa)‏

و رك ؛ سنیز , ممرب آن « شژیزه « رشیدی * شولیز با ‎Nigella = att.‏ ازتيرء ‎YT‏
‏و شمارة کلب ر ‎AS‏ آن از پنج تا هشت است و دانه‌های سیاه رنکه آن در ب رکه های وسط کل
‎FNS‏ و بوی مخصوصی دارد ‎GIT IS?‏ ۷۰۰ » . ۷ - ره : شومیز .

۸ - «شویزیه ؛ مقبره‌ایست ‎shady‏ درجالب غربی آن ‏ و کروه بیار از صالحان بدانجا
مدفوند ازجملة ‎OUT‏ :جنید وجعفی ‎Gale‏ ورویم‌وسمتون معحب, ودرآنجا خانقاهی است صوفیان

‎٩ Ay‏ «معجم‌البلدان» + ‎٩‏ = شبه («م) . ۴ - از دساتیر ‎Cia b>‏ وسائیر
‎AGU? ۰۵‏ ص۰۸۷ . ۱ رك: ‎Shey‏ . ۴ - پهلوی 51۵1 ‎gel‏ ۷۹5

‏مازدرانی ‎sht gaye. Shi‏ گردی 50 ‎yew,‏ فان «هوبشمان»۷۹»» ‎‘shi yy‏ طنزی
0 «2. اس۲۸۹», سنگسری ‎Shu‏ » سرخه‌بی ‎shi‏ , لاسکردی ‎Vay vd? Shit‏ -

‏دزفولی ‎SHE‏ «امام» ورك؛ شر ». شوهر .
© شوهر - پنتح اولوسوم ؛ اوستا- 951080072168 مفی- 1690210078 (تخم.منی)»

‎Xshaudra_‏ «اسشق ‎Jyh evan‏ هوبشمان شرهرهمیءشة «شوی» ‎cha Cpa)‏ پدر(ه.م.) وپس
(«.م.) در فارسی ساخته شده «هوبشمان ‎EVAN‏ قس : شهمیرزادی ‎SBUP‏ (شوهر) 2۰ .۷۰ س
۷ . مردی که ‎OS th)‏ زوج .

=== pdf page 104 ===
[pdf page 104]
۳۱۳

‎ply -‏ بشتن هرهت ۱ - وبکسر اولرثالی
شبت را کوبند ۴ و آن رستنیی باشد که آنرا
ربزه کنند و در طعام و ماست ریزند - و دهلیز
و دالان خرد وکوچك را یز کفته‌اند.

‏شو پست = بنتم ‎Syl‏ و الی بتحتالی
کشیده و ‎gee‏ بی‌قطه و فوقالی زده ۰ بمعنی
‎Sol,‏ و پربشالی باشد ۴ ۰

‏شه باله

‎Wet‏ = شم اول ‎lly‏ بتحتالی رسیده
و لام بالف کشیده , بلفت سربالی کیاهی‌است
که آنرا ‎sy‏ مادران ‎ary‏ و بیوتالی ارطمیا
خوالند ۰

‏شوی مال ?= بر وزن کوشمال ۰
شخصی را گوبند که آهار وآش برتارجامه‌ا ی که
میبافند بمالد .

‏بیان بیست ودویم

‏در شین لقطه دار با هامشتمل بر ‎See‏ و شش لغت و کنایت

‎Mt‏ » بنتع ‎Syl‏ و سکون ‎gl‏ ۰ مخفف
شاه است که اصل و خداوند و بز رک ‎Math‏ -
و داماد رائیز کویند ۵ - و سیردرمقابل کرسته
را هم کفته‌اند٩‏ - ویمعنی منم هم‌آمده است که
در ‎ply‏ رخصت و رضاست - و کشت کردن شاه
‎ge‏ باشد ‎gin, ٩‏ مهره‌ای را درجایی‌بگذارند
که شاه حریف لاملاج از جای خود برخیزد با
علاج‌برخاستن ‎CT‏ -وهر چیز را ‎Sar Ssh‏
در پزر گی و خوبی بحسب صورت و سیرت از
امثال خود بزر کتر و همتاز باشد همچه شه‌سوار
و شهباز و ‎sept‏ و امثال آن ‎٩‏ -و بضم ‎AB Syl‏
است که در محل کراهت ولفرت گویشد.

‏شهاب » بر وزن شراب » مخفف شاه
آبت » وآنآب سرخی باشد که مرتبهٌ اول از
کل کاجیره گیردد - و درعربی شیری باشد از
کوسفند با کاو که باآب آمیخته باشند -وبکس

‏اول هم درعربی ک و کب و ستارء - وشعله کفیدن
‎aT‏ راگویند وشهب جمع آدت ۷ .

‏شهادت سر بسته = کواهیرشهادنی
راکوبند که درآن شك وریب و ‎PATEL‏
‏باشه ر از روی راستی واخلاص باشد.

‏شهباز ‎A‏ - با بای ایجد بروزن پروازء
جالوری است شکاری که بجثه از باز بزرکتر
و بگیرایی کمتر میباشد - و باز بز رکه را لیز
‎aS‏ .

‎as‏ بالا * - با لام الف » بممنی‌شاءبلا
است یعنی داماد بالا چه شه بمعتی دامادهم‌هست.
و آن شخصی است که بقد و ‎My‏ وسن و سال با
‎SS‏ او را کدخدا میکنند برابر میباشد و او
را نیز ماد داماد آراسته کرده با داماد ‎lee‏
‏عروس میبرند و بترکی ساق دوش‌میگویشد.

‏شه ‎BY‏ 2 بر وزن ده ساله ؛ ‎ga,‏

‏۱ - رك :شتن .

‏رشیدی +

‎. ‏-رك: کیش‎ ٩

‏۴ مشفف ه شوید ‎By. ٩‏ : شبت .
۴ - از : شوی ‎(pa)‏ + مال (مالنده ).
۷ - (عر) ‎oles?‏ » بالکسر درخش آتش, ویاره‌ای ‎STN‏ »ردرخش

‏۴ ره :

‏© - مخذف شاء(هم) .

‏هرچیز سپید ‎Yo‏ برآهده , شپاب ‎CHE‏ شملهٌ افروخته ‎oles pty‏ مردرسادر کارهاومنه:فلان‌شهاب
الحرب‌ای‌ماض‌فیها,شپب ککتب جمم » شهبان بالضم والکسر واشپب‌کا کلب مثله"«منتهی‌الارب» .

‎. Coa) Gk ‏مخفف شاه‎ - A
. ‏شه بالا‎ : dy ‘es

‎٩‏ - مخفف «شامپالا» (هم.) ورك: شهباله.
```


## [2026-09-06T21:37:16.575Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HUB sustan/soi\"; grep -n -i \"šōi\\|soi '\\|sustan\\|šustan\\|xšaudra\\|xsaudra\\|šuštan\" HUB.txt | head -10; echo; echo \"### NYB asob\"; grep -n -i \"āšōb\\|asob\\|āšuft\\|asuft\\|šōy\\|soy\" NYB_vol2_glossary.txt | head -15"
}
```


### [2026-09-06T21:37:16.648Z] TOOL RESULT

```
### HUB sustan/soi
2795:stampfen*. Aber die Bedeutung von np. Sustan ist
7095:wasche', inf. sustan, bal. sddag, nb. sdJJay (s. oben p. 79);
8311:§%r *Milch* = skr. kslra- ; sustan Vaschen H. 782 , oben
10743:sustan 79.

### NYB asob
696:a-soyisn [ "swdšn']
752:III; Verbum 184); cf MPrth. ”šwb-gr ‘instigator to rebellion’, abstr ’swbgryft (S); NP āšēb. V. also āšuft-kārēh.
757:āšuft-kārēh [’swptk’lyh] subversion, up- heaval 1081. — From äsuftan äsöp-, v. äsöp and cf visuftan; MPrth ’syft (A-H III). Ghilain 95; Bailey, BSOS VI, 1930, 73.
5546:’TWS-: arvés ’ry’nwyjn: Eran-včj >Šyft: āšuft-karēh "ws: avas
7454:Soy, Sauhar: šēd
```


## [2026-09-06T21:37:17.648Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### DKS (ISS_alt) \"; grep -n -i \"ksaub\\|xsaub\\|āsuft\\|asuft\\|ksubh\\|xsaud\\|ksud\" ISS_alt_DKS.txt | head -15"
}
```


### [2026-09-06T21:37:17.701Z] TOOL RESULT

```
### DKS (ISS_alt) 
1621:ksü 'hunger', SuvP. 64r3 Ағи ttarna hamthrri ‘tormented by hunger (and) thirst’, BS Asut-bipasarditena, SuvP. 71v3 kşųna ttarrna, BS &sut-targa-pipása- ; Z 24:467 inst. sing. Айна; JS Grr kşuna, 32r1 ksune, тут ёри ttarrna; Sid. 373 Asu, Tib. skom-pa. Adjective 2 11:10 Азйѓа, JS азу: suva. From *Asudh-, Iran. Av. fud-, Zor.P. sad, Oss. D. sud, І. syd; Вајоё fu8a, fu8 ‘hunger’, fudig, $u8ig, fuxi "hungry', verbal suñay, Susta 'be hungry'. O.Ind. ksodh-:Rgudh-, ksudh- ‘hunger’, hyudhyati ‘be hungry’. IE &seudh-, isolated, see Рок, 625.
1622:ksuna- ' section, period of time, in datation ‘period of rule in a year’, also written : Rgupma-, kgampa-, Rsauna-, hgauna- (or to be read ksudmmna-, or Rsüumga-), ksu, за; тү 20:8 36mye ksunä “іп the 36th regnal year’; v 2107361 T5ntye hguna; U 33, 3010 33 hsumi; 11 129580 tcürmye ksumná; Iv 18:1 35mye hand; п 57743 (=K 15144) with a and и on the one aksara, pūhye ksüumnád “іп the fifth year’; ту rı sparadirsamye ksu (For hsu(ná ?)) “іп the 35th year’; 11 22, 16b3 sparadirsamye зй; v 385:92 naumye Rsauna tin the ninth year'; и 42:1 hau hsanyá (in the initial incom- plete words). The word occurs in five other sources: Tumšuq Saka xíama-, ed. 5. Konow ri ximane xšane tin the sixth year’; Surx Kotal Greek script xpovo from *xjana or possibly *xšuna-; Kroraina Prakrit бб ij'a ksunami tin this period of time’; 1211 isa ksunammi, with dental -л-, not -g-. Kharosthi inscriptions, with both -п- and -n-, ed. S. Know 87:1 isa Аҳипаті; 751 ise ksunami, rendered by Konow 'at that term”, and “ас this instant’; 85:3 256) divasa-Rsupami, rendered ‘оп this day- егт’. Parallel is 39:2 itra hhanasa rendered ‘ас this instant’. Tokhara B Asum, kgune, Кита, kgumntsa (see S. Lévi, JA 1913, 2, 8-10; J. Filliozat, JA 1958, to p. 88 facsimile). in datation.
1753:khvih- “to be agitated', SuvO. гд akhothënau, aksubhyä 'Aksobhya unshakable'; Z 13:22 pharui háde hhwihátá ütca ' much, greatly the water is agitated for him’, From (s)&(I)eubh- to *khüh- with -ya- *hhuhya- to khwiha-, to IE Pok. 955 skeubh- ‘move swiftly’, Not to Slav. xvejat- sja 'be moved'.
4771:prraksividi ‘they reject’, K бт, 41r4 ci ttu süttrq prraksividi и draya ramna avajsamya yanamdi ' who may reject this sütra-text and treat the #riratma three jewels with dis- respect’, From *para-xsaub- (or pari-) see s.v. praksautta- ' rejected.
7968:bajse 'small animals, worms’, SuvO. 24v4 pära u hajse ‘worms and insects’, BS hrmi-ksudra-, "lib. srim-buhi phun-po ( = variant Arimi-skandha-). Possibly from IE Pok. 895 sek- 'to cut’, hence like Greek £vrogos ‘insect’, Lat. зесб, secáre ‘to cut’,
```


## [2026-09-06T21:37:31.253Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '745,760p' NYB_vol2_glossary.txt; echo \"=== DKS praksautta ===\"; grep -n -A3 \"praksautta\" ISS_alt_DKS.txt | head -20"
}
```


### [2026-09-06T21:37:31.314Z] TOOL RESULT

```
āšnavišn ['šnwšn'] the act of hearing; hearing 6627. 9415. 1119; hence
āšnavišnēh [ŠMHn-šnyh] det. v.n. in compounds: pas hac én gobišn ~ after having heard this speech 518, with the gl. ka šmāh én gobišn āšnūt; pat han gobišn ~ 5119, with the gl. ka ētšān han gobišn āšnūt būt. — Paz. šnavašni (SGV, Mx).
āšnūtan ['šnwtn'; ŠMHn-tn'] āšnav- to hear 21! ete.; 128%; with kū that 1515, 1823; apar āšnūt had heard, been told, informed 6115, — OP (NRjb) ā-všnav-, Benveniste, TPhS 1945, 47-50; MPrs 'šnwudn (S), imp. *šnww (A-H II); MPrth ‘snwdn (8), pres. 'šnw- (A-H III); NP šunudan, šinidan, šinav-; Paz. cf the predecing w.
ašok Pšwk] = ahlav, g. v.; pl. cas. obl. ~-dn 1061. — A learned w., taken over as a religious term from Av. ašava, nom. of ašavan-, v. s. v. ahlav.
ašop ['šwp'] confusion, tumult, sedition 381. 1081, — MPrthPrs swb, *šwb (A-H
www.parsianjoman.org | oe ww
äsöp
III; Verbum 184); cf MPrth. ”šwb-gr ‘instigator to rebellion’, abstr ’swbgryft (S); NP āšēb. V. also āšuft-kārēh.
aštak [’Stk'] messenger, apostle 36°. 579-11; ~ cas. rect. pl. 58%. — Av. (260) ašta-.
aštakčh mission 364; apostolate 5515-19, 562.
astéh [’Styh] peace 5612-13, 6416, 669. 7818, 796, — Av. (311) āzšti-; MPrs St; xw- >št-wrz ‘bringing about good peace’ (A-H II) xw?štyh (S); NP äst. V. also an- ašteh.
aštr ['štl] scourge 9621, — Av. (263) aštrā-.
āšuft-kārēh [’swptk’lyh] subversion, up- heaval 1081. — From äsuftan äsöp-, v. äsöp and cf visuftan; MPrth ’syft (A-H III). Ghilain 95; Bailey, BSOS VI, 1930, 73.
at [’t] the independent form of the cas. obl. of the pers. pron. 2nd p. sg., for encl. -t (g. v.): taking up čo after a relative clause 334; cf am, aš.
atin [’t’n'] pl. of the preceding w., for encl. -tän: taking up $mäh after a relative clause 451.
"štaro (Prth) [?'trw] fire, pl. cas. obl. ātarūn Ptrwn] SPrth: 2-3, v. ātur. — The reading *trwn (Ghirshman: ?tryn) is con- firmed by KZSPrth 1. 19, where -wn is perfectly clear.
=== DKS praksautta ===
437:apabüysiyeti ‘attacks it', v 66:9 apahüysiye-t-i stakülai yanāti si hvi mila bastd midi ' he who may attack it and abuse it, that man dies presided over by the Rat’. Parallel phrase v 330, 13v4. sütru aprramā(nu ya)nde, BS G 37, rIb3 sad-dharma-pratiksepid, v 388, 19r ttu dàtu apramünu yanüre, BS G 37, 13b6 sad-dharma-prati- hgepakaih satvaih; also SuvP. 64v1 cu dā praksauttai ime, BS sad-dharmah prakşiptah syád. . me; K 61, 4114 ci ttu süttrq prraksividi. Hence apahaystye denominative from *pahàysa- ' grasping, approving’ to base has- ‘seize’, Av. hasz-, O.Ind. sahate, IE Рок. 888-9 seh-, Greek Exco, Éaxov.
438-apiye ' without fat’, Sid. 13514, Tib. sa-snum bag chun-ba. Bee рӣуй ‘fat’.
439-*apihi 'unchecked', see тїрїї, ayihī, avihi.
440-apüstye ‘uninterrupted’, rr 48:6 apnstye bhavana gilma, K 112:372 apvastya bavaia gihna ‘by help of uninter- rupted bAavanü-meditation'; п 72:5 Sä sali Siri apvasti khu vyachīmdi harbaisi pile '(exert yourselves) for one year well, uninterruptedly, so that all troubles vanish’. Possibly = BS anacchedya-; пі 53:111 BS anüchida. See -püsja-, from *pa(ti)brasta- "break off’. Parallel to K 54, 1412 aharstë bhüvana.
--
1633:ksautte ' thrown', Z 2-44 ggūne pharu śśāre tcabriye dise viri brinthe jsa kşautte ‘hairs abundant lie scattered every- where tossed by the storm'. See Asdu-, veksotta-, naksa- uita-, praksauttai, #šaksautta-. From xfaub-:xsub-. “to disturb’, Av. xfaob-, xsufsan, M. Pers.T. wšwb-, wyswub-, "$b-, wšwb'g; Zor.P. višōpišn, visuft, visüpet, М№.Регз. üfuftan, aiüftan, йїдЬ, gušuftan. YE Рок. 625 hseubh- 'swing', O.Ind. ksdbhate, ksübhyati, ksobha-, Rsubdha- ; Slav. Polish chybaé 'swing' (Polish ch = x).
1634-kha ‘а measure for grain, grapes’ used with high numbers, after hüsa-, before samga and simga-, from fuller spelling khara, as pharu, phara, pha ‘much’; v 211, 39:5 dysam kha 8 güra kha 7 ' arzana-millet 8 Rha-measures, grapes 7 kha- measures’; V 181, 2a2 ganam küsa 13 kha 5 'wheat 13 küsa-measures, 5 kha-measures'; ibid. 3 дашт küsa I3 kha 5 'gavarsa-millet 13 hiisa-measures, 5 kha-measures' ; v 17422 (in a list of gifts) aysdam kha 4 *the aysdam-
1635-grain(7) + Aha-measures'; v 120, сах ganan kha б visakámnta piha hauda * Višakünta gave the price of whear 6 kha-measures'; v 306: 172 barija asti 104 kūsa kha 9 ће crop, there is 104 &üsa-measures, 9 kha-measures’. The fuller form khara is in three passages, п 36:104 //Janirüda. khara їй ' Aniruddha (gave) one &Atara-measure' (sd fem.) ; u 25292 38 khara и б gamga drrai šega ‘58 khara- measures and 6 samga, three simga’; U 2572003 u guñi- haysüka hvamdi tta hā jsārä jseņi hauda 64 khara kşi samga 2 (syai(gayll| 'and the carriers of sacks, so fine grain was given, 64 &hara-measures, six samga, 3 simga'. Possibly a word basically meaning 'receptacle', not a loan-word, but cognate with O.Ind. khāra-, khāri-, khārī-'of 18 drona-measures' and of other values, Variant -аға- and -üra-, note also Aara-, ћага- ‘тей’ (Asiatica, Festschrift Fr. Weller 16-9); O.Ind. khara- 'hard', N.Pers. zar, Base uncertain, possibly IE Рок. 925 (s)&el- tto split’, O.Norse skala ' drinking-vessel', O.Sax. scala 'cup' (as Oss. D. &'os ‘cup’, beside Khotan Saka Aisa- ta measure"), O.Engl. sciell ‘shell’; (s)k(At)-, see also IE Pok. 930 skheng- O.Ind. khanjati ‘limp’, Greek ax&co, Celtic Mid.Ir. scingim ' jump', O.Norse shaker 'limping', OHG Ainkan ‘ќо limp’.
1636-khaca 'food', It 120195 {асп saika ävūā са ma ќаи dva hhaca haira yai ttuva-in padaya khaysa u ca va baisa jq ‘I came well to Sacü, what were my one or two things for food, that I ate on the road, and what there was, was all used up’ (khaysa taken as *hhaysita- in 1 sing. ‘I ate"). From xad- 'to eat', with suffix *xad-£d-, see hhays-, khāysa-, See also khacai.
--
4771:prraksividi ‘they reject’, K бт, 41r4 ci ttu süttrq prraksividi и draya ramna avajsamya yanamdi ' who may reject this sütra-text and treat the #riratma three jewels with dis- respect’, From *para-xsaub- (or pari-) see s.v. praksautta- ' rejected.
4772:praksautta- ‘rejected’, SuvP. 64vi-2 cu dà prrahsauttai ime, avaramjsd rrastá abviya, ‘Į who have rejected the dharina-doctrine, the favourable, the right, being ignor- ant’, BS sad-dharmah praksiptah syüd ајапатепа me sada; v 1054 (right half now lost)-N 158-34 pamjsa anamttanarya yudāmdä idi u däru prakgauttandád "they have committed the five anantarya-sins and long time rejected (the dharma-doctrine)'. From *pará-xfaub- (or pari-), see cognates s.v. ksdu- 'to toss’.
4773-pratarü-, prrarā- ‘nature’ rendering BS prakrti- and sva- bhava-, N go:27 pratare jsa ttusfa|[], Suv. ed. Nobel 248 гаку ca sūnyä; V 155, 185b2 hamaggä pratara; ibid. 5 tvà pratara üraugyüdá 'they have honoured this nature? (BS aragaya-); К. 8, 306v3 hio? aysmor prratari vasvatte jsa ‘his own mind, with purity of nature’; frequently in later form jrrara, prara (inflected -i, -e, -ai), Sid. 7v2 prara, BS prahkrti-, Tib. ran-bšin; second component -wrrara-, Sid. 7v2 bimna-wrrard (-i-—-ai-), BS vata- prakrtika-, Tib. rlun-gi ran-báin-éan ‘having nature of wiad’. Adjective, Z 10:8 pratárastu badána ттаѓа vasuta käde isasta utüra päşkälsta ārsta sañyau jsa dhyana- pürümata bvāña ‘the dhyāna-meditation Paramita-per- fection is to be known to be naturally in time in control,
4774-254 prranama — prrastharznada
4775-pure, exceedingly calm, exalted (BS udara-), distinctive, full-grown with plans’; K 54, rsv2 prrarasta ttüsüttü 'voidness by nature’, BS Prahrti-fnyata; Manj. 158 prrarasia sünyatta; Manj. 288 prrarastye raste; Мап). 301 jprrarasta їйпуаћа, Manj. 391 prrarasta suenyatta rasta ‘natural fünyatü-voidness, right’, =Z 09-15 soabhavána Sunyd abhüvi. From *parü-karü- or *pari-kara- 'active around or for’, if Iranian, but possibly NW Prakrit *prakar(d)u-« *brakrti, see -rr- in parramaü- ‘image’ from Prakrit *pardima, BS pratima-. Written К. 38:143 prrirà ‘state of affairs’, == K 30209 frrara.
```


## [2026-09-06T21:37:42.646Z] TOOL CALL #46: Bash

```json
{
 "command": "head -40 tools/fetch_source.py; echo ...; head -30 tools/verify_check.py"
}
```


### [2026-09-06T21:37:42.690Z] TOOL RESULT

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
...
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
```


## [2026-09-06T21:37:51.233Z] TOOL CALL #47: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/آشفتن\" \\\n \"https://en.wiktionary.org/wiki/آشوب\" \\\n \"https://en.wiktionary.org/wiki/شستن\" \\\n \"https://en.wiktionary.org/wiki/شوهر\" \\\n \"https://en.wiktionary.org/wiki/شوی\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 280, Kseubh/Kseud entries: modern etymology of the Persian words\" ; done 2>&1 | tail -20"
}
```


## [2026-09-06T21:37:53.262Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/elixir\" \\\n \"https://www.etymonline.com/word/serenade\" \\\n \"https://www.etymonline.com/word/serene\" \\\n \"https://www.etymonline.com/word/xero-\" \\\n \"https://en.wiktionary.org/wiki/ξηρός\" \\\n \"https://en.wiktionary.org/wiki/إكسير\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 280, Ksero entry: Greek xeros > Arabic al-iksir > French/English elixir; Latin serenus\" ; done 2>&1 | tail -20"
}
```


### [2026-09-06T21:37:57.986Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/48dd264a2070100e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c2257ac7b451f06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7c4ae9aa499c241e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6300ded41d00ab3b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9e37459623fbdae.txt
```


### [2026-09-06T21:38:02.444Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/09f0f99121d6482a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a2cf78a2139125ab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1eb7a1db25d4eb01.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b80d5377da985c0b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/defa7ed4c8567f9f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/42647893e462bfc2.txt
```


## [2026-09-06T21:38:05.867Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 48dd264a2070100e 0c2257ac7b451f06 7c4ae9aa499c241e; do echo \"##### $f\"; sed -n '1,10p' $f.txt; echo \"---- etym ----\"; grep -n -i -A12 \"Etymology\" $f.txt | head -50; done"
}
```


### [2026-09-06T21:38:07.568Z] TOOL RESULT

```
##### 48dd264a2070100e
URL: https://en.wiktionary.org/wiki/آشفتن
FETCHED: 2026-09-06T21:37:56Z
STATUS: 200
TITLE: آشفتن - Wiktionary, the free dictionary

آشفتن - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
---- etym ----
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Verb 
72-
73- 1.4.1 
74- Conjugation 
75-
76- 1.4.2 
77- Related terms 
--
156: Etymology
157- [ edit ] 
158-
159- Inherited from Middle Persian [Book Pahlavi needed] ( ʾšwptn' /⁠āšuftan⁠/ ) , derived with the preverb *aH- from the root Proto-Iranian *xšawb- ( “ to rustle, tremble ” ) , from Proto-Indo-European *k⁽ʷ⁾sewbʰ- ( “ to rock, tremble ” ) . Cognate with Sanskrit क्षुभ् ( kṣubh , “ to shake, be agitated ” ) , Proto-Germanic *skeubaną ( “ to push, drive ” ) , Lithuanian skùbti ( “ to start to hurry ” ) , Proto-Slavic *xybàti ( “ to sway ” ) . Note the Iranian borrowings: Old Armenian ապշոպ ( apšop ) , շփոթ ( špʻotʻ ) , Old Georgian შფოთი ( špoti ) .
160-
161- Pronunciation
162- [ edit ] 
163-
164- ( Classical Persian ) IPA ( key ) : /ʔaː.ʃuf.ˈtan/ 
165-
166- ( Dari, formal ) IPA ( key ) : [ʔɑː.ʃʊf.t̪ʰán] 
167-
168- ( Dari, formal ) IPA ( key ) : [ʔɑː.ʃʊf.t̪ʰán] 
--
1045: The template Template:R:fa:Herzenberg:2014 does not use the parameter(s): 1=āšuftan Please see Module:checkparams for help with this warning. Herzenberg, L. G. ( 2014 ), “Studies in Persian Etymology II”, in Acta Linguistica Petropolitana ‎ [1] , volume 10 , number 1, published by P. A. Kocharov and A. V. Shatskov, page 38 of 19–48 
1046-
1047- Horn, Paul ( 1893 ), Grundriss der neupersischen Etymologie (in German), Strasbourg: K.J. Trübner, § 32 , page 8 
1048-
1049- Horn, Paul ( 1898–1901 ), “Neupersische Schriftsprache [ New Persian written language ]”, in Wilhelm Geiger, Ernst Kuhn , editors, Grundriß der iranischen Philologie [ Outline of Iranian Philology ] (in German), volume I, part II, Strassburg: K. J. Trübner, page 136 
1050-
1051- Hübschmann, Heinrich ( 1895 ), Persische Studien [ Persian Studies ] (in German), Strasbourg: K.J. Trübner, pages 7, 233 
1052-
1053- Retrieved from " https://en.wiktionary.org/w/index.php?title=آشفتن&oldid=91810394 "
1054-
1055- Categories : Persian terms inherited from Middle Persian 
1056- Persian terms derived from Middle Persian 
1057- Persian terms derived from Proto-Iranian 
##### 0c2257ac7b451f06
URL: https://en.wiktionary.org/wiki/آشوب
FETCHED: 2026-09-06T21:37:56Z
STATUS: 200
TITLE: آشوب - Wiktionary, the free dictionary

آشوب - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
---- etym ----
73: Etymology 
74-
75- 2.2 
76- Pronunciation 
77-
78- 2.3 
79- Noun 
80-
81- 2.3.1 
82- Descendants 
83-
84- 2.3.2 
85- References 
--
228: Etymology
229- [ edit ] 
230-
231- Inherited from Middle Persian [script needed] ( ʾšwp /⁠āšōb⁠/ , “ turmoil, disturbance ” ) . Cognate with Parthian 𐫀𐫀𐫢𐫇𐫁 ( ʾʾšwb /⁠āšōβ⁠/ , “ turmoil, disturbance ” ) .
232-
233- Pronunciation
234- [ edit ] 
235-
236- ( Classical Persian ) IPA ( key ) : /ʔaː.ˈʃoːb/ 
237-
238- ( Dari, formal ) IPA ( key ) : [ʔɑː.ʃoːb] 
239-
240- ( Dari, formal ) IPA ( key ) : [ʔɑː.ʃoːb] 
##### 7c4ae9aa499c241e
URL: https://en.wiktionary.org/wiki/شستن
FETCHED: 2026-09-06T21:37:57Z
STATUS: 200
TITLE: شستن - Wiktionary, the free dictionary

شستن - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
---- etym ----
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Verb 
69-
70- 1.1.2.1 
71- Usage notes 
72-
73- 1.1.2.2 
74- Conjugation 
--
80: Etymology 2 
81-
82- 1.2.1 
83- Pronunciation 
84-
85- 1.2.2 
86- Verb 
87-
88- 1.3 
89- References 
90-
91- Toggle the table of contents 
92-
--
167: Etymology 1
168- [ edit ] 
169-
170- From Middle Persian [script needed] ( HLLWN-tn' /⁠šustan⁠/ ) , from Proto-Iranian *xšawd- ( “ to wash ” ) , from Proto-Indo-Iranian *kšáwd- ( “ to crush, disperse ” ) , traditionally derived from Proto-Indo-European *k⁽ʷ⁾sewd- ( “ to crush, disintegrate ” ) , though Cheung has reservations on this derivation due to the wide semantic divergence of the PIE root's alleged descendants. [ 1 ] 
171-
172- Compare Northern Kurdish şûştin , Central Kurdish شتن ( ştin ) , Southern Kurdish شۊردن ( şürdin ) , Zazaki şutene , Gurani شتەی ( ştey ) , Gilaki شوردن ( šurdən ) , Mazanderani بشوردن ( bašurdan ) .
173-
174- Pronunciation
175- [ edit ] 
176-
177- ( Classical Persian ) IPA ( key ) : /ʃus.ˈtan/ 
178-
179- ( Dari, formal ) IPA ( key ) : [ʃʊs.t̪ʰán] 
--
1043: Etymology 2
1044- [ edit ] 
1045-
1046: See the etymology of the corresponding lemma form.
1047-
1048- Pronunciation
1049- [ edit ] 
1050-
```


## [2026-09-06T21:38:14.916Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 6300ded41d00ab3b e9e37459623fbdae; do echo \"##### $f\"; sed -n '1,6p' $f.txt; grep -n -i -A10 \"^ Etymology$\" $f.txt | head -60; done"
}
```


### [2026-09-06T21:38:16.370Z] TOOL RESULT

```
##### 6300ded41d00ab3b
URL: https://en.wiktionary.org/wiki/شوهر
FETCHED: 2026-09-06T21:37:57Z
STATUS: 200
TITLE: شوهر - Wiktionary, the free dictionary

شوهر - Wiktionary, the free dictionary 
185: Etymology
186- [ edit ] 
187-
188- From Proto-Iranian *fšautar , from Proto-Iranian *fšau- ( “ to raise cattle ” ) , from Proto-Indo-European *peh₂- ( “ to protect; to shepherd ” ) . Compare Khotanese [script needed] ( kṣondai , “ husband ” ) , Yidgha [script needed] ( šfuy , “ husband ” ) , Avestan 𐬟𐬱𐬎𐬌𐬌𐬀𐬥𐬝 ( fšuiiant̰ , “ husbandman, commoner ” ) , [ 1 ] Northern Luri شی ( şi , “ husband ” ) , Baluchi شو ( šú , “ husband ” ) .
189-
190- Pronunciation
191- [ edit ] 
192-
193- ( Classical Persian ) IPA ( key ) : /ʃaw.ˈhar/ 
194-
195- ( Dari, formal ) IPA ( key ) : [ʃäw.háɾ] 
##### e9e37459623fbdae
URL: https://en.wiktionary.org/wiki/شوی
FETCHED: 2026-09-06T21:37:57Z
STATUS: 200
TITLE: شوی - Wiktionary, the free dictionary

شوی - Wiktionary, the free dictionary
```


## [2026-09-06T21:38:22.961Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### شوهر refs\"; grep -n -i \"Hasandust\\|Bailey\\|Cheung\\|Horn\\|Reference\" 6300ded41d00ab3b.txt | head -20; echo; echo \"### شوی etymologies\"; grep -n -B2 -A8 \"Etymology\" e9e37459623fbdae.txt | sed -n '1,120p'"
}
```


### [2026-09-06T21:38:23.027Z] TOOL RESULT

```
### شوهر refs
91: References 
344: References

### شوی etymologies
60-
61- 1.1 
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Noun 
69-
70- 1.2 
71: Etymology 2 
72-
73- 1.2.1 
74- Pronunciation 
75-
76- 1.2.2 
77- Noun 
78-
79- 1.3 
80: Etymology 3 
81-
82- 1.3.1 
83- Pronunciation 
84-
85- 1.3.2 
86- Noun 
87-
88- 1.4 
89: Etymology 4 
90-
91- 1.4.1 
92- Pronunciation 
93-
94- 1.4.2 
95- Noun 
96-
97- 1.5 
98: Etymology 5 
99-
100- 1.5.1 
101- Pronunciation 
102-
103- 1.5.2 
104- Verb 
105-
106- 1.5.3 
--
176- [ edit ] 
177-
178: Etymology 1
179- [ edit ] 
180-
181- From the same root as شوهر ( šawhar  / šowhar , “ husband ” ) , see there for more.
182-
183- Pronunciation
184- [ edit ] 
185-
186- ( Classical Persian ) IPA ( key ) : /ˈʃuːj/ 
--
224- husband 
225-
226: Etymology 2
227- [ edit ] 
228-
229- Akin to Old Armenian շապիկ ( šapik ) , an Iranian borrowing; see there for more.
230-
231- Pronunciation
232- [ edit ] 
233-
234- ( Classical Persian ) IPA ( key ) : /ʃa.ˈwiː/ 
--
272- shirt , shift 
273-
274: Etymology 3
275- [ edit ] 
276-
277- Pronunciation
278- [ edit ] 
279-
280- ( Classical Persian ) IPA ( key ) : /ʃi.ˈwiː/ 
281-
282- ( Dari, formal ) IPA ( key ) : [ʃɪ.wiː] 
--
320- small vestibule 
321-
322: Etymology 4
323- [ edit ] 
324-
325- Pronunciation
326- [ edit ] 
327-
328- ( Classical Persian ) IPA ( key ) : /ʃu.ˈweː/ 
329-
330- ( Dari, formal ) IPA ( key ) : [ʃʊ.weː] 
--
366- starch , paste , size 
367-
368: Etymology 5
369- [ edit ] 
370-
371- See the etymology of the corresponding lemma form.
372-
373- Pronunciation
374- [ edit ] 
375-
376- ( Classical Persian ) IPA ( key ) : /ˈʃoːj/
```


## [2026-09-06T21:38:31.561Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 09f0f99121d6482a a2cf78a2139125ab 1eb7a1db25d4eb01 b80d5377da985c0b; do echo \"##### $f\"; sed -n '1,5p' $f.txt; grep -n -m1 -A14 \"elixir (n\\|serenade (n\\|serene (adj\\|word-forming element\" $f.txt | head -30; echo; done"
}
```


### [2026-09-06T21:38:33.476Z] TOOL RESULT

```
##### 09f0f99121d6482a
URL: https://www.etymonline.com/word/elixir
FETCHED: 2026-09-06T21:38:00Z
STATUS: 200
TITLE: Elixir - Etymology, Origin & Meaning

23: elixir (n.) 
24-
25- mid-13c., from Medieval Latin elixir "philosopher's stone," believed by alchemists to transmute baser metals into gold and/or to cure diseases and prolong life, from Arabic al-iksir "the philosopher's stone," probably from late Greek xerion "powder for drying wounds," from xeros "dry" (see xerasia ). Later in medical use for "a tincture with more than one base." General sense of "strong tonic" is 1590s; used for quack medicines from at least 1630s.
26- also from mid-13c. 
27-
28- Entries linking to elixir 
29-
30- xerasia (n.) 
31-
32- "excessive dryness of hair," 1706, medical Latin, from Greek xerasia "dryness," from xeros "dry, withered" (see xero- ).
33-
34- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
35-
36- More to explore
37-

##### a2cf78a2139125ab
URL: https://www.etymonline.com/word/serenade
FETCHED: 2026-09-06T21:38:00Z
STATUS: 200
TITLE: Serenade - Etymology, Origin & Meaning

23: serenade (n.) 
24-

##### 1eb7a1db25d4eb01
URL: https://www.etymonline.com/word/serene
FETCHED: 2026-09-06T21:38:00Z
STATUS: 200
TITLE: Serene - Etymology, Origin & Meaning

23: serene (adj.) 
24-
25- mid-15c., of a day, "clear, fair, calm," from Old French serein and directly from Latin serenus "peaceful, calm, clear, unclouded" (of weather); figuratively "cheerful, glad, tranquil"(from PIE root *ksero- "dry," source also of Greek xeros "dry, arid;" see xerasia ).
26-
27- In English, the word has been applied to persons, characters, etc. since 1630s: "tranquil, unruffled." Related: Serenely . Middle English also had serenous (mid-15c.), of places, "having clear, fair weather."
28- also from mid-15c. 
29-
30- Entries linking to serene 
31-
32- xerasia (n.) 
33-
34- "excessive dryness of hair," 1706, medical Latin, from Greek xerasia "dryness," from xeros "dry, withered" (see xero- ).
35-
36- Serena 
37-

##### b80d5377da985c0b
URL: https://www.etymonline.com/word/xero-
FETCHED: 2026-09-06T21:38:01Z
STATUS: 200
TITLE: Xero- - Etymology & Meaning of the Suffix

25: before vowels, xer- , word-forming element of Greek origin used from mid-129c. in scientific and technical terms, meaning "dry," from Greek xero- , combining form of x ē ros "dry, arid, withered."
26-
27- This is reconstructed in Watkins, etc., to be from PIE root *ksero- "dry" (source also of Latin serenus "clear, unclouded," serescere "become dry;" Greek xeron "dry land;" Old High German serawen , German serben "to dry out").
28-
29- Entries linking to xero- 
30-
31- xerasia (n.) 
32-
33- "excessive dryness of hair," 1706, medical Latin, from Greek xerasia "dryness," from xeros "dry, withered" (see xero- ).
34-
35- xeric (adj.) 
36-
37- "having little moisture, very dry," 1926; see xero- + -ic .
38-
39- xeroderma
```


## [2026-09-06T21:38:38.796Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '23,40p' a2cf78a2139125ab.txt; echo \"=== xeros greek wiktionary ===\"; grep -n -m1 -A8 \"Ancient Greek\" defa7ed4c8567f9f.txt | head -20; echo \"=== إكسير ===\"; grep -n -m1 -A8 \"Etymology\" 42647893e462bfc2.txt | head -25"
}
```


### [2026-09-06T21:38:38.866Z] TOOL RESULT

```
 serenade (n.) 

 1640s, "a musical performance at night in open air" (especially "one given by a lover under the window of his lady" [OED]), from French sérénade (16c.), from Italian serenata "an evening song," literally "calm sky," from sereno "the open air," noun use of sereno "clear, calm," from Latin serenus "peaceful, calm, serene" (see serene (adj.)). The sense was influenced by Italian sera "evening" (from Latin sera , fem. of serus "late"). The meaning "piece of instrumental music suitable for a serenade" is attested from 1728.
 also from 1640s 

 serenade (v.) 

 1660s, "perform a serenade," from serenade (n.). Transitive sense, "entertain with nocturnal music," is by 1670s. Related: Serenaded ; serenader ; serenading .
 also from 1660s 

 Entries linking to serenade 

 serene (adj.) 

 mid-15c., of a day, "clear, fair, calm," from Old French serein and directly from Latin serenus "peaceful, calm, clear, unclouded" (of weather); figuratively "cheerful, glad, tranquil"(from PIE root *ksero- "dry," source also of Greek xeros "dry, arid;" see xerasia ).

 In English, the word has been applied to persons, characters, etc. since 1630s: "tranquil, unruffled." Related: Serenely . Middle English also had serenous (mid-15c.), of places, "having clear, fair weather."

=== xeros greek wiktionary ===
57: Ancient Greek 
58-
=== إكسير ===
65: Etymology 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2
```


## [2026-09-06T21:38:41.821Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== إكسير etym ===\"; sed -n '/^ Etymology$/,+8p' 42647893e462bfc2.txt | head -30; echo; echo \"=== ξηρός etym ===\"; sed -n '/^ Etymology$/,+8p' defa7ed4c8567f9f.txt | head -30"
}
```


### [2026-09-06T21:38:43.539Z] TOOL RESULT

```
=== إكسير etym ===
 Etymology
 [ edit ] 

 Borrowed from Classical Syriac ܟܣܝܪܝܢ ( ksīrīn ) , from Ancient Greek ξηρίον ( xēríon , “ medicinal powder ” ) .

 Noun
 [ edit ] 

 إِكْسِير • ( ʔiksīr )  m ( plural أَكَاسِير ( ʔakāsīr ) ) 

=== ξηρός etym ===
 Etymology
 [ edit ] 

 From Proto-Indo-European *kseros ( “ dry ” ) . Cognates include Latin serescō , Old High German serawēn , Old Armenian չոր ( čʻor ) , Middle Armenian չիր ( čʻir ) , and perhaps Sanskrit क्षार ( kṣārá , “ sharp, acrid, pungent ” ) . However, the lengthened vowel η where ε would normally be expected is problematic. [ 1 ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ksɛː.rós/ → /ksiˈros/ → /ksiˈros/
```


## [2026-09-06T21:39:24.380Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LEW serenus\"; grep -n -o \"serenus[^\\n]\\{0,300\\}\" LEW_1910.txt | head -3; echo \"### LAT serenus\"; grep -n -o \"serenus[^\\n]\\{0,300\\}\" LAT.txt | head -3; echo \"### SKT serene\"; grep -n -o \"Serene[^\\n]\\{0,250\\}\" SKT.txt | head -3; grep -n -o \"Serenade[^\\n]\\{0,250\\}\" SKT.txt | head -3; echo \"### SKT elixir\"; grep -n -o \"Elixir[^\\n]\\{0,250\\}\" SKT.txt | head -3"
}
```


## [2026-09-06T21:39:26.125Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LKT iksir\"; grep -n -o -i \"iksir[^\\n]\\{0,300\\}\" LKT.txt | head -4; echo \"### PHN elixir\"; grep -n -o -i \"elixir[^\\n]\\{0,300\\}\" PHN.txt | head -4; echo \"### AFM اکسیر\"; grep -n \"اكسير\\|إكسير\\|اکسیر\" AFM.txt | head -4; echo \"### FVQ iksir\"; grep -n -o -i \"iksir[^\\n]\\{0,200\\}\" FVQ.txt | head -3"
}
```


### [2026-09-06T21:39:26.531Z] TOOL RESULT

```
### LEW serenus
### LAT serenus
6395:serenus d'un auster umidusj 3° la r 6 gion
57514:serenus, illic
57531:serenus.
### SKT serene
16928:Serene.  (I*)  I^  sertnus^  bright,  clear. Allied  to  Gk.  ff^Aar,  brightness,  o'cXf7nh moon,    cySWAR.)
### SKT elixir
```


### [2026-09-06T21:39:28.981Z] TOOL RESULT

```
### LKT iksir
2174:iksir:
### PHN elixir
### AFM اکسیر
### FVQ iksir
```


## [2026-09-06T21:39:35.990Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LKT ctx\"; sed -n '2165,2190p' LKT.txt; echo \"### LEW seresc\"; grep -n -o -i \"seresc[^\\n]\\{0,300\\}\" LEW_1910.txt | head -3; grep -n -o \"serenus\\|serenum\" LEW_1910.txt | head -3; echo \"### LAT 6395 ctx\"; sed -n '6385,6400p' LAT.txt"
}
```


### [2026-09-06T21:39:37.705Z] TOOL RESULT

```
### LKT ctx
899.  Ar.  'ijär:
'Eichmaß,  Feingehalt  des  Goldes  oder Silbers,  Pendel  zum  Regulieren  einer LTir',  ebenso  tk.  ajar ;  hieraus  rum.  aiar 'Eichmaß,  Regulator'.
900.  Tk.  iki:
'Zwei';  hieraus  vielleicht  rum.  ichm 'ßleiknöchel  oder  -würfel'  beim  Knöchel- spiele.
901.  Tk.  ikindi:
'Die  Stunde,  die  den  Nachmittag  in  zwei gleiche  Teile  teilt';  hieraus  rum.  chindie 'Vesper,  Bauerntanz',  den  die  Landleute häufig  nach  dem  Vesperbrote  tanzen.
902.  Ar.  iklil:
'Krone';  a)  iklil  algahal,  eigentlich 'Bergkrone',  ist  ein  Pflanzenname,  Ros- marinus  ofBcinalis;  hieraus  sp.  pg.  ale- crim  'Rosmarin'  [Gonstancio  Dicc  47  c. DE  97].
b)  mit  simäll,  Adj.  zu  simäl  'Süden', ergibt  sich  ar.  al-iklil  as-simäli,  hieraus Achleischemali,  Name  des  Sternbildes Corona  borealis  [Devic  DEt  40].
903.  Ar.  iksir:
[Aus  gr.  Zr)piov  'das  Trockene']  'Stein der  Weisen',  d.  h.  die  besondere  Sub- stanz, die  bewirken  sollte,  daß  unedle Metalle  in  edle  verwandelt  würden ;  ins- besondere sollte  die  Masse  auch  die Kraft  besitzen,  den  menschlichen  Kör- per zu  gesunden,  zu  stärken  und  zu verjüngen,  also 'Lebenssaft' ;  hieraus  it. elissire,  elisire  'Heiltrank',  frz.  elixir, sp.  pg.  rum.  elixir,  dtsch.  Elixir,  engl. elixir.  [DE  259/260.  Devic  108/109. Lammens  Rem  104/105.   Kluge  III.
904.  Ar.  'ilka:
[Vom  Vb.  'alaka  II  'aufhängen']  'kost- barer Besitz';  hieraus  mit  ar.  Art.  sp. alahilca  'Wandbekleidung',  besonders
Teppiche  als  Wandschmuck,  Arazzi. [DE  54.
905.  Ar.  iniäm:
[Vom  Vb.  amma  'vorhergehen']  'Vor- gesetzter, Vorsteher',  insbesondere  die- jenige Person,  die  einer  Versammlung vorsieht,  um  das  Zeremoniell  bei  den öffenthchen  Gebeten  am  Freitag  und an  den  Beiramsfesten  zu  leiten.  Da  dies in  den  ersten  Zeiten  des  Islams  von  den Kalifen  selbst  geschah,  so  nahmen  sie den  Titel  imäm  an;  dieser  Titel  wurde sodann  auch  erteilt  1.  den  Lehrern  der ersten  islamischen  Jahrhunderle  als  den ersten  Auslegern  des  Korans,  2.  den Rehgionsdienern,  die  an  den  Moscheen die  Obliegenheiten  des  Priestertums  im Namen  des  obersten  Imäms  ausübten. Tk.  ebenso  iniam;  hieraus  rum.  imam, engl,  imam,  ungenau  iman;  ebenso  frz. iman,  imam,  dessen  Funktionen  imamat, imanat  heißen;  russ.  imam  'Ik.  Schrift- gelehrter'. [Devic  DEt  142.  Lammens Rem  136.
906.  Tk.  imanie:
'Mundstück  einer  Pfeife';  hieraus  rum. imamea  'Bernsteinmundstück'.
907.  Ar.  intära:
'Befehl'  [vom  Vb.  amara  'befehlen',  s. hier  Nr.  69],  'Zeichen';  hieraus  mit  ar. Art.  sp.  alimara  [alter  Ausdruck,  jünger ahumada  <^  lat.  adfumata]  'Feuersignal von  Wachttürmen  und  hohen  Punkten aus',  das  alte  miUtärische  Fernsignal, das  in  den  Zeiten  der  sog.  reconquista auf  maurischer  wie  christlicher  Seite viel  angewandt  wurde  [Dicc  Gast  94  b; DE  141/142].
908.  Ar.  'imära :
'Öffentliches  Gebäude,  fromme  Stiftung [Moschee,  Schule,  Armenküche]' ;  hieraus frz.  imaret  nach  der  tk.  Aussprache  des ar.  Grundworts]  'eine  Art  tk.  Gasthauses, in  dem  die  Schüler  der  verschiedenen Schulen  ihre  Mahlzeiten  einnehmen können,  Hospiz'.  [Devic  DEt  142.  Lam- mens Rem  136.
909.  India:
N.  pr.,  Halbinsel  in  Südasien  [ursprüng- lich ind.  sindh,  hieraus  pers.  hind  mit lautgesetzlichem  Übergange  von  s  zw  h und  schließlich  gr.  'Ivbia,  Adj.  'IvbiKÖ?, lat.  India,  indicus].  Bereits  gr.  ivbiKÖv bezeichnete  einen  Farbstoff,  den  die Spanier  später  aus  Ostindien  nach  Europa einführten:  ein  tiefes  Blau,  das  aus Pflanzenstoffen  hergestellt  wird,  und zwar  aus  einer  Papilionacee  Indigofera. Aus  lat.  tndicum  wurde  dann  sp.  endico, indigo,  pg.  indigo,  it.  indaco,  afrz.  iiide, prov.  inde,  frz.  indigo,  dtsch.  Endich, Indiek,  Indigo  'indischblau'.  —  Nach
73
[Tk.  ingi.
### LEW seresc
### LAT 6395 ctx
fixe obs-, os-. Le scultator de V^gfece soit sans doute s'expliquerauspex
1.08
de la meme ffifon.
D 4 rives (rares); auscultatio,-tor,-tus.
Pour le premier hiement de ce verbe qui a l'air d 1 un juxtapose,
v. auris', quant 1 -culto, 1'origine en eat inconnue.
auspex: v.auis.
auster, -trl m.: i° auster, vent du Midi, le voro£ des Grecs, qua-
lifie d 'imbricus par Pl., Mer.876. Vent venant d'Afrique, qui ambae
la pluie et la tempete; pendant de 1 ’aquilon. Pline, 3 , 137 > n6anmoins
distingue un auster siccus, serenus d'un auster umidusj 3° la r 6 gion
d'oii souffle ce vent, le Midi, ad austrum = Ttpoc voxov s'opposant a
ad aquilonem, ab boreae partes (= ad septentriones, -nem) ; de la austra¬
lis: austral. Les representants du mot dans les 1 . ronanes sont de
la langue savante; cf. M.L.807. Les gloses ont un verbe austrdre expli-
qu6 par hunefacere , cf.Thes. s.u.
```


## [2026-09-06T21:39:46.025Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '57500,57545p' LAT.txt"
}
```


### [2026-09-06T21:39:46.076Z] TOOL RESULT

```
Les formes roaanes remontent k serrare, cf.M.L.7867, dont il faut
rapprocher les formes de gloses serra, sarra et'serraculum, "gou-
vernail". glost 7 tT) 8 aXi,ov, clauis nauis , M.L.7862. La gtminte est
obscure (formation expressive? ou, plutot, influence de serra, en
raison de la forme dentelte de certaines pibces de serrure ou de
cadenas, cf.British Museum, A guide to the exhibition illustr. Greek
and Soman Life, fig.171,17«,174,175).
Comme il s'agit d'un terme technique, le rapprochement avec les
groupes de serO, sertus ne saurait etre affirmt. Mais on ne voit
pas pourquoi les ttynologistes s'accordent k 1 'tcarter.- Le vocalisme
0 de toga en face de tegd ne s'y retrouve pas; mais le cas de toga
est isolt en latin.
serSpud, -a, -un: serein (se dit du ciel, de 1' atmosph.br e, etc.J
puis s'emploie par image); serenum: temps ou ciel serein. Le sens
premier est "sec", cf.Pl., Me .877 hic fauonius est serenus, illic
auster imbricus} Vg.,. G.1,100 umida solstitia atque hiemes orate
serenas} Pline, 10,188 salamandra magnis imbribus proueniens atque
serenitate deficiens ;■ et Lucr. emploie seresco dans le sens de "se
stcher" par opposition k UuSsco, 1,306: denique fluctifrago suspensae
in litore uestes | uuescunt, eaedem dispansae in sole serescunt.
~ Anci en (Bnn.), usuel. Panroman, M.L.7843.1089 -
HfM
Ddrivds et composds: serSnitSs’, serene,-ds, Serendtor (dpith. de
Jnpiter); sereni-fer,-ficus (dpoq.imp.).
Serenus eat formd comae terrenus, egenus, d'un ancien *seres-no-sy
sana doute ddrivd d'un ancien theme nentre en -os/es~ ddsignant
l f dtat clairet aec du ciel.
Le aena de "aec" suggbre nn rapprochement avec gr. grjpoC, i-epoC
"aec" et avec v.h.a. serauen "sdcher" (v. H.Pederaen ,_ Tergi, Gr.d. k. Spr.,
I 78). Mala tout ce groupe eat obacnr et mal ddfini, ponr le aena
comme ponr la forne. Le mot grec ^epoC ne s'applique qu*A la terre
ferme, hom. ijepov T| 7 tei,poto, et le aena en eat bien loin d e serenus.
En soaae, rien de clair.
serSscS: t* le prdcddent.
sSria, -ae f.: jarre, cruche; cf.Rich, a.n. Attestd depnia Plaute
jusqu'au Digeste. M.L.7846. Sana doute empruntd i une langue mddi -
terrandenne. Dim.sdriolo, M.L.7851.
serichatum, -I n.: piante aromatique, mentionnde par Pline 13 ,
99, non autrement cqnnue. Non latin.
sericus, -a, -urn: tldrivd du nom de peuple SSres (transer. du
gr. S^pei) "lea Chinois", et appliqud i certaina produits originaires
de Chine, notannent la soie: -a uestis, etc.j de 14 . sericum, et
serica,-erum, M.L.7O48 serica et sarica, strica; passd en celt.:
iri., gall. siric, et en germ.: v.angi. syric, v.h.a.st lihho, v.norr.
silke, etc. Le mot n'apparaat paa avant 1 ' dpoque d'Auguste.
Ddrivds et composds tardifa: sericeus; sericdriu.s, sericdtus} seri¬
```


## [2026-09-06T21:39:57.901Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC\"; grep -n -o \"Kser[^\\n]\\{0,200\\}\\|Kseub[^\\n]\\{0,200\\}\\|Kseud[^\\n]\\{0,200\\}\\|Ksēr[^\\n]\\{0,200\\}\" IEC.txt | head -8; echo \"### SYN dry/wash\"; grep -n -o \"15.83 WASH[^\\n]\\{0,300\\}\\|DRY (adj[^\\n]\\{0,400\\}\" SYN.txt | head -6"
}
```


## [2026-09-06T21:39:59.168Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### ARY latin index\"; grep -n -i \"KSERO\\|KSEUBH\\|KSEUD\\|KSEU\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"### ARY persian\"; grep -n \"آشفتن\\|اکسیر\\|شستن\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T21:39:59.594Z] TOOL RESULT

```
### IEC
8251:Ksero- *sixsome'. Cf. ksueKs Arm. cf. vecir 'sixthly; Olr. sesser, Ir. seisear *sixsome'; MHG séhser, id.; G Sechser, id.; Cz. šestero, id.; Li. cf. šešeri, SeSerios, f. id.
### SYN dry/wash
```


### [2026-09-06T21:39:59.650Z] TOOL RESULT

```
### ARY latin index
10158:ala SKEU- | KSEUs gly! y stn Gat, aly jt) Cai cal lan jly BUCK ~¥
### ARY persian
1282:(به معنی هستی دادن و پا روی تخم نشستن و جوجه آوردن) نیز از همین ريشه باشند.
1850:۶ آشوب آشفتن» آشوفتن
7697:چم این واژه در زبان یونانی: نشستن» خود را شق نگهداشتن.
13387:۲ برخی واجریشه شناسان معتقدند که ریشه‌ی این واژه "محل نشستن" است و لذا با واژه‌ی انگلیسی 817 (به چم
14751:۸ ا نشست. نشاندن» نشستن ۱
```


## [2026-09-06T21:40:05.841Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### ARY 1840-1880\"; sed -n '1835,1885p' incoming/ARY/ARY_pages.txt; echo \"### page tag\"; awk 'NR<=1850 && /\\[pdf page/ {p=$0} END{}' incoming/ARY/ARY_pages.txt; grep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | awk -F: '$1<1850' | tail -2"
}
```


### [2026-09-06T21:40:07.932Z] TOOL RESULT

```
### ARY 1840-1880
بادداشت: 5
۱- چم اصلی واژه‌ی "آش": خورش (طلاً در واژ‌ی "آشپز).
ان واژه‌های همریشه‌ی "آش" در زبان‌های دیگر همه به صورت شکل‌های گرتاگون فمل "خوردن" هستند (مثلاً
واژه‌ی آنگلیسی 3۸7 یعنی "خوردن" و واژه‌ی هنبت 131811 یعنی "می‌خورم"). ای ای هو
ی ی
ند
اوسنایی (41557400: ,ش۸181 ,۸۷18189۸ برنانی (07880): ۸
9 1 لانین (770ه۸ل): ,۸۲701715
پهلری (1شالله۲): ۳ اسلاری کهن (16/بما5 بل تال 0ا0):
تخاری 8 (8 ((فلم707): 6 لاه ,۸۷171
۵0۵0 لینوانی (12هنا777): 05
سانکریت (5۸۸/۶8/7): ,۸۷۸ ۰ ,۸۷18 ام هتبت (4777772): -18[16
5
۸۸
[pdf page 65]
۶ آشوب آشفتن» آشوفتن
پسگشت‌ها 5 2 (۸1001818) :00/5
8 ۶008000 8 صلقاطی :7و
4 (101883ه) امد ار ان پرهان قاطع :۶" ۳۵
3 (5۷105311) ,13 :020/28 ۱/۸ تایه
بادداشت:
۱- معنی این واژه در هند و اروپایی و سانسکریت و اوستایی: فهمیدن» فهم.
معنی این واژه در لاتین و زبان‌های رومانس» یونانی: شنیدن.
معنی این واژه در تخاری 8 : تفکر روحانی,
۲- واژه‌های ۸17017 ,۸170188108 و شتقات آنها در انگلیمی و فرانسه و اسپانیایی و ابتالیایی از ربشه‌ی لاتین
این واژه برگرفته شده‌اند. :
: ۹
اوستایی (/7511۸078:41287:40 ,۸76511۸08
پهلری (۷1بماللم۸ه): ز دنه پسگشت‌ها 5
ساسکریت (6۸(/96/7: 1250873۸ را
اد اه 1 (01871788۸0168) ۰ قادلنقن مزر
لهستانی (/۳0(8): 0۸ لفت‌نامه دهخدا: ۱۵۵-۶
| ماگلیس سروز نان ی 86
سانسکریت (84۸96/7): نیا ای ان پسگشت‌ها ند در
301 نی
ایردی میانه (۸/31ا ظاط0ا/0: ۰ 0585 38 لاه
برهان قاطع : 8 ۳۷
لفت‌نامه دهخدا: 1۵۹
فرهنگ بزرگ سخن: ۱7۱
[pdf page 66]
لگ
آکندن» آکنده» آکنش, آگنش,- آگین / ۶۷
:
پهلوی (2:]4۲ :۸0۸30۸7216۸10۸7۷ ,7 مفان6۸ 00۳57578
سانسکر بت (54(/570077): ,1۸۸5 لینوانی (1777040/140.ت): 6۸3۷01771 ,0۸۸
0 ,۸۸310
ارمنی (4//1۸(0): 007 پسگشت‌ها ۶2۳52225
یرنانی 07888/0): 15 1 200900
اسلاوی کهن (ع1ها5 لع#ناقل) صاه): برهان قاطع : ۷۵-۶
بادداشت:
۱- معنی این واژه در اسلاوی کهن و لیتوانی: کافی بودن.
### page tag
1813:[pdf page 64]
1849:[pdf page 65]
```


## [2026-09-06T21:40:19.099Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC ks\"; grep -n -o \"^Ks[a-zēū-]*[^\\n]\\{0,180\\}\" IEC.txt | head -20; echo; echo \"### SYN wash\"; grep -n -o \"9.36 WASH[^\\n]\\{0,400\\}\\|WASH$\" SYN.txt | head -5; grep -n \"15.83\\|9\\.36\" SYN.txt | head -5"
}
```


## [2026-09-06T21:40:20.476Z] TOOL CALL #63: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/اکسیر/\" \"https://www.ahdictionary.com/word/search.html?q=elixir\"; do python3 tools/fetch_source.py \"$u\" --note \"page 280, Ksero entry: Mo'in (MON:331) on Persian eksir; AHD dictionary entry elixir (AHD:424)\"; done 2>&1 | tail -5"
}
```


### [2026-09-06T21:40:22.002Z] TOOL RESULT

```
### IEC ks
ugrep: error: error at position 339
x80-\x8f][\x80-\xbf][\x80-\xbf]){0,180}
          exceeds complexity limits___/



### SYN wash
14603:9.36 WASH
1990:3. Ir. flechud : Ir. fliuch ‘wet’ (15.83).
7049:fluenced by the words for ‘stall, Stable’) . Grk. craddoow ‘drip’. Walde-P, 2.649 Henry 252. Loth, Rom. 19,593, 5. OHG seichan, MHG seichen (NHG dial. id.), LG séken (sbs. OHG seih MUHG seich), fr. IE *seig-, beside *sei. in ChSl. sicati, Boh. scdti, Pol. szcedg Russ. scat’ : OF séon, OHG sthan, NHG sethen ‘strain, filter’, Skt. sic- ‘pour out, shed’, Lat. stat: obpe? ert Bpédous (gl.). Walde-P. 2.466f. Weigand-H. 2.835, Briickner 545. MHG harmen, hermen, NHG harnen, fr. sbs. NHG harn, MHG harm, harn, OHG haran, ‘urine’ cf. MHG vb. hur- men ‘manure’, prob. : Lith. garmas ‘lye from ashes’, Lett. sarms, OPruss. sirmes ‘lye’. Walde-P. 1.463. 6. Lith. myZzlz etc., above, 1. Lith. Slapumas ‘wetness’ (: glapias ‘wet’, 15.83) and, esp. pl., slapwmai, ‘urine’. 7. ChSl. sicati, ete. : OHG seichan, etc. (above, 5). SCr. mokriti, Boh. moéiti, etc., with sbs. SCr. mokraéa, Boh. moé, etc. : ChSl. mokri ‘wet’ (15.83). 8. Skt. mth-, Av. miz-, etc., above, 1. Skt. miatraya-, mitra-: Ir. min, ‘urine’, etc., above, 4.
11305:OHG dwahilla, twehilla, MHG dwehel twehel, zwehel, etc., fr. OHG dwahan, Goth. pwahan, etc. ‘wash’ (9.36), Hence MLat. toacula, (It. tovaglia ‘tablecloth’) OFr. toaille (> ME towaille > Nir. tudille, NE towel > W. tywel), Sp. toalig (fr. Prov. toalha). Lett. dvielis fr. MLG dwele (Mihl.-Endz. 1.538). REW 8720,
11433:3. ON foal, Sw. tvél = OE puéal, OHG dwahal, Goth. bwahl ‘washing, purification’ : Goth. bwahan, OE puéean, ON fva, ete. ‘wash’ (9.36). Hellquist 1253.
11435:4. Boh. mydlo, Pol. mydto, Russ. mylo (> Lith. muilas) : ChSl. myti ‘wash’ (9.36).
```


### [2026-09-06T21:40:25.786Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6c7152375ea1f754.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/142435129206aab4.txt
```


## [2026-09-06T21:40:29.259Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SYN 9.36 WASH\"; sed -n '14603,14625p' SYN.txt; echo; echo \"### SYN DRY\"; grep -n \"15.84 DRY\\|15\\.84\" SYN.txt | head -3"
}
```


### [2026-09-06T21:40:29.327Z] TOOL RESULT

```
### SYN 9.36 WASH
9.36 WASH
(a, The Body or Certain Parts of the Body; b, Clothes or the like : otherwise Generic)
Grk. — otw (a), vitw (a), Goth. Awahan Lith. mazgoti mdbrw (b) ON fod, vaska Lett. mazgat NG —s_ zAbw, vifw (a), Dan. _vaske, tvatte ChSl.  myti, plakatj (b) Aobtw (a) Sw. tvdtla, vaska SCr.  prati, miti (a) Lat.  lavare OE pwian (a), wescan Boh. myfti, prdti (b) It. lavare (b), swillan Pol. my€, praé (b) Fr. laver ME _ wasche, swyle Russ. myt', stirat’ (b) Sp. lavar NE wash Skt. nij-, dhav- Rum. = spdila, la (a) Du. wasschen Av. sna-, niz- Ir. nigim, folcaim, ind- OHG wascan, dwahan (a) aim (a) MHG waschen, twahen (a) Nir. = nighim (folcaim) NHG = waschen W. golcht Br. gwele’ hi
In several of the IE languages, as often in non-IE, there are different words for ‘wash’ according to the object, whether the body (but, except for Grk. dotw, special words for ‘bathe’ are not included), or certain parts of the body as hands, feet, face, head (sometimes with differentiation even here), or cloth- ing or the like. Such special uses may be original but are often only survivals in special connections of once generic use, as Rum. Ja now ‘wash the hair’, from Lat. lavdre ‘wash’ and similarly in many other cases.
But the idiomatic differentiation is so varied, even between corresponding words in the same group (as Gme. or Slavic), that it cannot be fully shown in the following discussion, still less in the summary notation adopted in the list. Thus, for example, Boh. myli, Pol. myé, Russ. myt’ are used for washing parts of the body, but also dishes, etc., that is, are generic except with reference to clothes, for which there is a different word. Conversely, SCr, prati (= Boh. prdti, Pol. praé ‘wash clothes’) is virtual- ly generic, while miti is restricted to use with reference to the head, or hands and feet, etc. according to the local dialect (cf. Rjetnik Akad. s.v.). In the Munster
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
dialect of Irish three different words are used with reference to the hand, head, and foot, respectively (cf, Atkinson, Passions and Homilies 711). OF wes- can is used for washing clothes or the like (nets in Gospels, Lk. 5.2), wean (and likewise OHG dwahan) for washing parts of the body (also dishes, cf. Gos- pels, Mk. 7.8), but otherwise one or the other of the two Gme. words is the usual generic term in nearly all connections, the former in West Gme. and Dan., the latter in Goth., ON, Sw. and Nlcel. (where vaska survives only in vaska jisk).
There are two groups pointing to IE roots which probably already had the meaning ‘wash’ with some, not now de- terminable, differentiation of applica- tion. Others reflect, on the one hand, the use of water, by connections with words for ‘water, wet, flow’ or the like; on the other, the process of rubbing or beating, the latter especially applicable to the old method of washing clothes.
1. TE *neig’-. Walde-P. 2.322.
Grk. vigw (fut. vive, ete., hence), later virrw, only of parts of the body, as like- wise NG vigrw and vigw (Hatzidakis, Mec. 1.282); Ir. nigim (of parts of the body, but also generic), NIx. nighim
ae he es ao oo ee of 2
am. 115); Skt. nij- B88- niz- (388: naénizaitt). 441, Ernout- 1.773 ff. (Hom. dow, oe, fr. *dfw) d bathe’ (cf. AouTpov, Hom. ‘yeash the boc, NG oisw (Hatzidakis, esp. ‘wash the hair’; (> It. lavare, Fr. laver, Sp. Ja arch. except as ‘wash the lavas Eatin s.v.); Arm. loganem bat dr, OE léapor ‘foam’ ipathe’ : ON lawor, : OR
7 lather), ON laug ‘bath (water)’, <= Q tc. a nee only of clothing, but NG sive, pop. wher (Hatzidakis, Mer 1,295) also of face, etc., generic TEW ‘sail’, Skt. plu- ‘float, swim, sail’, OF flowan ‘flow’, etc.; with like semantic development OHG flewen (‘wash’ nets, Tat. 19.4=Lk. 5.2), Arm. luanam ‘wash’, Walde-P. 2.94 f.
4, Rum. spdla, fr. Lat. *experlavare, epd. of lavare (above, 2). REW 3044. Puscariu 1613.
5, Ir, foleaim (NIr. esp. ‘bathe, dip, steep’), W. golchi, Corn. golhy Br. quelchi : Tr, fole ‘deluge’, Lett. vals ‘damp’, Lith. vilgyti ‘moisten’, OHG wih ‘damp, limp’, Walde-P. 1.306, Pedersen 1.59,
_ lt ind-aim, of hands or feet, vbl. n. Si also indlat, etym. dub. Lewis- ene (revision of Pedersen tion with oe possible connec- gether’), » yam- ‘hold, hold to-
6 Sw, ae Fear ON pva (Dan. to, se Stly replaced by tveette, tuatt ine so COtespondin aie 1g’, Dan, ive Sy 'g Nouns for ‘wash- bretta Tare, Neel, (ea ON b vattr; ON uean, OHG duvan ‘alk nonsense’), OF
SeNCES in use an, MAG twahen Ges
? cf. above), without
Clear Outs} ext gg CoEteCtiOns except OPruss bing brush for the bath”
r nenokli)s Av.
Meo. 1.276) now
Lat. lavare

### SYN DRY
8460:Ir. secc ‘dry’, loanwords fr. Lat. siccus ‘dry’ (: sttis? see 15.84), Loth, Mots lat. 209.
25878:15.82 Licut (in Weight) 15.83 Wet, Dame 15.84 Dry
27220:15.84 DRY Grk, Enpbs, ad i NG y aos Goth. paursus Lith. sausas Lat, fenés, oreyvbs ON purr Lett. sauss I, “us, Gridus Dan. gr ChSl.  suchit th tea, ascrutto (arido) Sw. torr SCr. suh Sp, Ee (aride) OE = drgge, pyrre, séar Boh.  suchy Rum, et Budo ME  drie, sere Pol. —suchy Ir, peal Sec NE dry Russ. suchoj Nir, tintin Du. droog Skt.  cuska- uf na. OHG — durri, trucchan Av. huSka-, hiku-, hiSku- Br, Bech, rg MHG _ trucken, dtirre
```


## [2026-09-06T21:40:30.769Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### abadis\"; grep -n -A6 \"فرهنگ معین\\|معین\" 6c7152375ea1f754.txt | head -30; echo \"### ahd\"; sed -n '1,6p' 142435129206aab4.txt; grep -n -i -m2 -A6 \"elixir\" 142435129206aab4.txt | head -30"
}
```


### [2026-09-06T21:40:30.857Z] TOOL RESULT

```
### abadis
27: اکسیر. [ اِ ] ( معرب ، اِ ) به اصطلاح کیمیاگران جوهر گدازنده و آمیزنده و کامل کننده که ماهیت جسم را تغییر دهد یعنی جیوه را نقره و مس را طلا کند و چنین جوهری وجود خارجی ندارد و فرض محض است. ( از مؤید الفضلاء ) ( از آنندراج ) ( از برهان ) ( ناظم الاطباء ). کیمیاء. ( منتهی الارب ). کیمیا. ( منتهی الارب ) ( دهار ) ( غیاث اللغات ) ( مهذب الاسماء ). کیمیا که بدان نقره زر شود. ( از شرفنامه منیری ). جوهری گدازنده که ماهیت اجسام را تغییر دهد وکاملتر سازد مثلا جیوه را نقره و مس را طلا سازد. ( فرهنگ فارسی معین ). دارویی که بدان مس و جز آن به زر وسیم بدل کنند. کیمیا. ( یادداشت مؤلف ) : 
28-بدین فصاحت و این علم شاعری که تراست 
29-مکوش خیره کش ابریز کردی و اکسیر. غضایری ( در هجو عنصری ).
30-زر اکسیر آفتاب است و سیم اکسیر ماه و نخست کس که زر و سیم از معدن بیرون آورد جمشید بود. ( نوروزنامه ).
31-خاک پایت ز من دریغ مدار
32-تا کنم زر چو یافتم اکسیر. سوزنی.
33-سائل از زر تو گردد قارون 
--
65: فرهنگ معین
66-
67- ( اِ ) [ معر. ] (اِ. ) ۱ - ماده ای که ماهیت اجسام را تغییر دهد و با ارزش تر سازد مثلاً مس را طلا سازد. ۲ - هر چیز مفید و کمیاب . ۳ - دارویی که به عقیدة قدما هر مرضی را علاج می کرد. 
68-
69- فرهنگ عمید
70-
71- ۱. کیمیا، جوهری که تصور می شد می تواند ماهیت جسمی را تغییر دهد، مثلاً جیوه را نقره و مس را طلا کند.
--
127:فرهنگ فارسی معین
128-فرهنگ واژه های سره
129-
130- باسلام 
131-در زبان ترکی استانبولی کلمه ای مشابه اِکسیر به شکل اِکسی ( Eksi ) به معنای منها و کم وجود دارد. 
132-نمی دانم ریشه ترکی دارد یا نه؟
133-
134: کیمیای اکبر ؛ اکسیر. ( ناظم الاطباء ) ( فرهنگ فارسی معین ) .
135-
136- elixir 
137-
138- مثل جواهری است که ارزش انسان را بالا می برد
139-
140- اکسیر: در نظر مردم باستان ماده ای که ماهیت اجسام را دگرگون سازد و کامل تر کند مثلاً جیوه را نقره و مس را زر کند. اکسیر واژه ای است یونانی، کیمیا نیز مترادف آن است. این که عشق همچون اکسیر انسان را کامل تر می سازد در ادبیات عرفانی بارها مطرح شده است . 
### ahd
URL: https://www.ahdictionary.com/word/search.html?q=elixir
FETCHED: 2026-09-06T21:40:25Z
STATUS: 200
TITLE: American Heritage Dictionary Entry: elixir

American Heritage Dictionary Entry: elixir 
1:URL: https://www.ahdictionary.com/word/search.html?q=elixir
2-FETCHED: 2026-09-06T21:40:25Z
3-STATUS: 200
4:TITLE: American Heritage Dictionary Entry: elixir
5-
```


## [2026-09-06T21:40:36.192Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '5,40p' 142435129206aab4.txt"
}
```


### [2026-09-06T21:40:36.240Z] TOOL RESULT

```
American Heritage Dictionary Entry: elixir 

 HOW TO USE THE DICTIONARY
 To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
 Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.
 guide to the dictionary 

 THE USAGE PANEL
 The Usage Panel is a group of nearly 200 prominent scholars, creative writers, journalists, diplomats, and others in occupations requiring mastery of language. Annual surveys have gauged the acceptability of particular usages and grammatical constructions.
 The Panelists 

 NEED HELP SOLVING A CROSSWORD PUZZLE?

 Go to our Crossword Puzzle Solver and type in the letters that you know, and the Solver will produce a list of possible solutions.

-->
 AMERICAN HERITAGE DICTIONARY APP
 The new American Heritage Dictionary app is now available for 
 iOS and Android. 

 THE AMERICAN HERITAGE DICTIONARY BLOG
 The articles in our blog examine new words, revised definitions, interesting images from the fifth edition, discussions of usage, and more.

 OPEN DICTIONARY PROJECT

 Share your ideas for new words and new meanings of old words!

 Start Sharing Now! 

 --> See word lists from the best-selling 100 Words Series!
 Find out more! 

 INTERESTED IN DICTIONARIES?
 Check out the Dictionary Society of North America at http://www.dictionarysociety.com
```


## [2026-09-06T21:40:51.025Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23525,23560p' MON_part2.txt"
}
```


### [2026-09-06T21:40:51.083Z] TOOL RESULT

```
خسشفت: ۲ (ع. ۰] (مص م ) آشکا ر ساختن» 
بدا کردن» پرده برداشتن. دفع بدی و ضرر 
کردن. (امص.) پیدایی؛ برداشتگی پرده از 
روی چیزی. (تص.) ظهور عوالم معنوی و 
حقایق جهان باطن بر سالکك. (عر.) نوعی 
زحاف که عبارت است از اسقاط تاء 
«مفعولات». دور کشف: (اسماعیلیه) عهدی 
که در آن حقایق آشکار شود؛ مق. دور ستر. 
کشفت: ۲5۸۱ (ص.) پراکنده؛ پر بشان. 
(فع.) سوم شخص مفرد ماضی از « کشفتن». 
کشفتن: ۲:۱۵ (- شگفتن - شکافتن ] 
(مص ع.) شکافتن» گشودن. 


۱۳۹۴ فر هن فارسی معیر کشفتن 


کشفشن: 32-0 (مص‌م.) پرا کنده کر دن» 
پرشان ساختن. بژمرده کر دن. معدوم کردن. 
کشی: :12 (.) نوعی از للنیات که عبارت 
است از دردی ماست یا دوغ که پس از 
جوشاندن خشکك کنند؛ پینو؛ بین و کد؛ 
قر وت. . (مج.) هیچ» پوج؛ بیهوده. . شیح 
حسین کشکت را بساب: (مثل) به همان کار 
اصلیت مشغول باش. کشکك چی؛ پشم چی ! 
(عم.) چه موضوعی" چه اصلی! (در مقام 
انکار). یعنی کشک: یعنی هیچ و پوچ. 
کشکاب: ۷:3 (- کشک او - کشکو] 
ور کح آ ناه که ای رد 
ترید کنند و خورند. آش‌جو که بیماران را 
دهند. آب‌جو؛ ماءالشعیر. 

کشکبا: ۲۵:7 (امر.) آش حلیم. 
کشکرک: مه (۱.) (جاد.) پرنده‌ای 
است از راسته سبکبالان جزو دسته دندانی 
نوکان از تیرة کلاغ‌ها که در اکثر نقاط کرة
```


## [2026-09-06T21:40:51.217Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27220,27260p' SYN.txt | head -40"
}
```


### [2026-09-06T21:40:51.274Z] TOOL RESULT

```
15.84 DRY Grk, Enpbs, ad i NG y aos Goth. paursus Lith. sausas Lat, fenés, oreyvbs ON purr Lett. sauss I, “us, Gridus Dan. gr ChSl.  suchit th tea, ascrutto (arido) Sw. torr SCr. suh Sp, Ee (aride) OE = drgge, pyrre, séar Boh.  suchy Rum, et Budo ME  drie, sere Pol. —suchy Ir, peal Sec NE dry Russ. suchoj Nir, tintin Du. droog Skt.  cuska- uf na. OHG — durri, trucchan Av. huSka-, hiku-, hiSku- Br, Bech, rg MHG _ trucken, dtirre
BLSELT NHG_trocken, diirr
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Ee
Sa S|
1076
In the principal inherited groups and in most of the other words one cannot go behind the sense of ‘dry’. A few are from the notion of ‘extract the juice’, and in a Gme. group ‘dry’ is probably associated with ‘firm’, as sometimes ‘wet’ with ‘soft’.
1. TE *saus-, *sus-. Walde-P. 2.447.
Grk. (Hom.) aios, Att. atos; OE séar, ME (NE) sere (esp. ‘withered’), MLG sor; Lith. sausas, Lett. sauss, ChSI. sucht, etc., general Balto-Slavic; Skt. cuska- (for *sus-ka-), Av. huska-, OPers. uska-.
2. IE *ters- in words for ‘dry’, ‘be dry’, (dry) ‘land’ (1.21), ‘thirst’ (5.15), etc. Walde-P. 1.737f. Ernout-M. 1048. Falk-Torp 1318.
Here as adj. ‘dry’. Ir. tir (rare), usu- ally tirim, NIv. tirim, trim; Goth. paur- sus, ON purr, Dan. ifr, Sw. torr, OE pyrre, OHG durri, MHG diirre, NHG diirr.
3. Grk. tnpos, NG pop. tepés (np > ep reg., aS in vepd ‘water’, etc.) prob. : Lat. seréscere ‘become dry’, serénus ‘fair’ (of weather), OHG serawén ‘become dry, wither’. Walde-P. 1.503 Ernout-M. 928.
NG oreyvés, fr. class. Grk. oreyvds ‘waterproof’, this fr. créyw ‘cover’.
4. Lat. siccus (> It. secco, Fr. sec, Sp. seco, Rum. sec), etym. disputed; perh. : Av. hiku- ‘dry’, haééah- ‘dryness’, these : Av. Skt. sic-, hié- ‘pour out’. Ernout-M. 937. Barth. 1812. Other- wise, fr. “*sit(z)-co-s : sitis ‘thirst’, Walde-P. 1.506, etc.
Lat. dridus (> It., Sp. arido, OFr. are, Fr. aride), with Grére ‘be dry’ : Skt. dsa- ‘ashes, dust’, Toch. A dsar ‘dry’, root *ds-, with guttural extension in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
Goth, azgo, OHG asca ‘ashes’, Arm. az. zem ‘T dry’, dental in Grk. fe ‘dry wy ete. Walde-H. 1.65. Ernout-M. 70 oe
It. asciutto, fr. Lat. exstictus, pple of exstigere ‘suck out’, epd. of sagere ‘e,a.1 REW 3074. pies tage
Rum. uscat, pple. of usca ‘to dry’ (= It. asciugare, Fr. essuyer ‘dry, wipe dry’) fr. VLat. *ex-sticdre ‘extract } (sticus ‘juice’). 1841.
5. Ir. firim, etc., above, 2.
W. sych, Br. sec’h, also MIr. seco, (Cormac), fr. Lat. siccus (above, 4), Loth, Mots lat. 209. Vendryes, De hib. voc. 176.
Br. krin : W. crin ‘withered, sere’, Ir, crin, NIr. crion ‘worn out, withered, old’, Ir. air-crinim ‘disappear, perish’, root connection? Pedersen 2.498,
6. Goth. paursus, OE pyrre, etc., above, 2.
OE driyge, ME drie, NE dry, Du. droog, and with n-sufiix OHG trucchan, MHG itrucken, NHG trocken; cf. ON draugr ‘dry log’, prob : OPruss driktai ‘firmly’, Lith. dial. driaktas ‘thick, strong’, ON drjigr ‘lasting, strong’, etc., fr. an extension of the root in Skt. dhr- ‘hold, bear’, etc. Walde-P. 860. Wei- gand-H. 2.1074.
7. Balto-Slavic words, above, 1.
8. Skt. cuska-, Av. huska-, above, 1.
Av. hiku-, above, 4. pre
Av. higku- : Ir. sese ‘dry, not giving milk’, W. hysb, Br. hesk (hesp) ‘dried up (of a stream), not giving milk’, etc., fr. *si-sk-us, reduplicated form fr. the root root *sek-in Lith. sekti ‘fall’ (of water), nusekti ‘flow off, dry up’, Chsl. i-seknah ‘decrease’, etc. Walde-P. 2.473. Barth. 1816 f.
the juice’ REW 3073. Puscariy
=
a at HM = [Pe fs >
The distinction according to the de- 2 of heat, as in NE hot, warm, holds for the Gme. and Balto-Slavie words. Most of the other words listed are used without such distinction, though there may be special words for ‘lukewarm, tepid’, which are not included.
Apart from inherited groups, the words are connected with verbs for ‘boil’ (5.22, 10.31) or ‘burn’ (1.84).
It is well known that extreme heat and cold, as in touching a red-hot iron ora piece of ice, produce the same sensa- tion, and there is every probability that acertain group of words for ‘hot’ (Lat. calidus, etc.) and another for ‘cold’ are, in fact, cognate. Cf. also Lat. pruina ‘hoar-frost? beside ‘“prina ‘live coal’,
rurtre ‘itch’ é Purire ‘itch’, and OE fréosan, etc. freeze’
LIK *
gq” her- Suffix, 1687 ¢, 1.532 ¢.
Grk, Sepuds; OLat, Sormus; Av. gara-
```


## [2026-09-06T21:41:16.933Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"فر هن\\|فرهنگ فارسی معین\\|فر هنگ فارسی\" MON_part1.txt | awk -F: '$1>15700 && $1<16000' | head -5; echo \"--- head of part1 ---\"; head -5 MON_part1.txt; echo \"--- around 15846 ---\"; sed -n '15800,15815p' MON_part1.txt"
}
```


## [2026-09-06T21:41:17.823Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/fetch_source.py \"https://abadis.ir/fatofa/کشفتن/\" --note \"page 280, Kseubh entry: Dehkhoda/Mo'in on Persian kašoftan\" 2>&1 | tail -2"
}
```


### [2026-09-06T21:41:18.973Z] TOOL RESULT

```
15730:۱۸۲ فرهنگ فارسی معین اکتناف 
--- head of part1 ---
0 
2 


چم 
--- around 15846 ---

اکرام: «ج [ع.] (مص‌م.) بز رگداشتن» 
گرامی دشن احترام کر دن. احسان کردن. 
(امص.) زرخداف؛ حرمت. احسان» انعام؛ 


آکراه: .| (مصم.) ناخوش داشتن» 
اپسند داشتن. کسی را به زور به کاری وا 
داشتن» به ستم بر کاری داشتن 0 (.) 
ناخواست» فشار» زور. 

اکرم: (ع.] (ص تفض..) گرامی‌تر» 
آزاده‌تر» جوانمردتر. بزرگتر. 

اکره: [ع.] (ص تفض..) منفور تر) 
زشت تر.
```


### [2026-09-06T21:41:21.894Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8a3aeb94343784ac.txt
```


## [2026-09-06T21:41:28.824Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m1 -A20 \"کشفتن\\.\" 8a3aeb94343784ac.txt | head -30"
}
```


### [2026-09-06T21:41:28.876Z] TOOL RESULT

```
16: کشفتن. [ ک َ ش َ ت َ / ک ُ ش ُ ت َ ] ( مص ) گشودن. شکافتن. ( از فرهنگ جهانگیری ) ( از برهان ).
17-- برکشفتن ؛ گشودن. ( از ناظم الاطباء ). برداشتن : 
18-دل برگرفته ام ز بد و نیک روزگار
19-تا پرده های راز فلک برکشفته ام. کمال الدین اسماعیل ( از جهانگیری ).
20- || پراکنده شدن. پریشان شدن. ( از فرهنگ جهانگیری ) ( از ناظم الاطباء ) ( از برهان ) : 
21-دولت آنها فرتوت شد و کار کشفت 
22-هرکه فرتوت شود هرگز برنا نشود. منوچهری.
23-کشفتند بزم می رودو باد
24-پراکنده شد انجمن مست و شاد. اسدی.
25- || پژمرده شدن. پژمرده گشتن. ( از فرهنگ جهانگیری ) ( از ناظم الاطباء ) ( از برهان قاطع ) : 
26-شکفته بدم چون به نیسان درخت 
27-کشفته شدم چون به آبان گیاه. عبدالواسع جبلی ( از جهانگیری ).
28- || نابود و معدوم شدن. ( از فرهنگ جهانگیری ) ( ناظم الاطباء ) ( برهان ).
29-- برکشفتن یا بکشفتن ؛ نابود کردن : 
30-سخنهائی چنان دلگیرگفتی 
31-که خانه صابری را برکشفتی. ( ویس و رامین ).
32-بکشفت سپهر باز بنیادم 
33-بشکست زمانه باز پیمانم. مسعودسعد.
34-چو زر به سایل بخشی بدست خویش مده 
35-که از نهیب تو گردد بر او کشفته نگار. حکیم سوزنی.
36-
```


## [2026-09-06T21:41:42.098Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### FSD xeroderma\"; grep -n -o -i \"xeroderma[^\\n]\\{0,200\\}\" FSD_vol4.txt | head -3; echo \"### FSD serenade\"; grep -n -o -i \"serenade[^\\n]\\{0,200\\}\" FSD_vol4.txt | head -2; echo \"### WEB elixir\"; grep -n -o -i \"elixir[^\\n]\\{0,250\\}\" WEB_vol1.txt | head -3; echo \"### BQT v1 اکسیر\"; grep -n \"اکسیر\" BQT_v1_pages.txt | head -5"
}
```


### [2026-09-06T21:41:44.375Z] TOOL RESULT

```
### FSD xeroderma
### FSD serenade
7311:serenade: opposed  to  aubade  [Pr ,   <   seren,  serene,  <   L   serenus, serene,  as  if  <   serus  late  1
7313:serenade  II.  u To  engage  in  or  tender  a   serenade  —   ser"e-nad'cr,  n SPr"e-nade%  n   1   An  ev  emng  song,  specif  ,   a   song  sung in  the  open  air  at  mght,  also,  the  music  of  such 
### WEB elixir
10376:elixir. är’cà-tūre, n. [from ML. arcata, arcade; and -ure.] in architecture, (a) a small arcade; (b) a closed or false arcade, as for ornament, årc”-böu”täńt’ (ar’boq"tiih’), n.; pl. årcs”- böu”täńts’ (ar’boo/tin’), [Fr.] in architec- ture, a flying buttre
62979:elixir; Sp. elixir; Port. elexir, from Ar. el iksir, the philosopher's stone; el, al, the, and iksir, philosopher's stone; prob. from Gr. xéros, dry.]
62981:elixir of life.
### BQT v1 اکسیر
```


## [2026-09-06T21:42:51.970Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HUB 2790-2800\"; sed -n '2788,2800p' HUB.txt; echo \"### HUB 8305-8315\"; sed -n '8305,8315p' HUB.txt; echo \"### HRN asuften\"; grep -n -o \"asuften[^\\n]\\{0,220\\}\\|äsuften[^\\n]\\{0,220\\}\\|Süften[^\\n]\\{0,200\\}\" HRN.txt | head -5; echo \"### HRN leaf29 (p8)\"; awk 'BEGIN{RS=\"\\f\"} NR==30' HRN.txt | head -30"
}
```


### [2026-09-06T21:42:54.010Z] TOOL RESULT

```
### HUB 2790-2800
trennen.
777. Aus *aiwiStap' ware np. ^afstap, arm. *austap geworden.
Das arm. LW. stap kann nur auf ein phi. §tap, istap
oder ustap zuriickgehen. Der von Horn angefiihrte
pehl. Infinitiv kann ostaftan oder ttstaftan gelesen
werden, da anlaut. D und u gleich geschrieben werden.
782. Nach F r. M ii 1 1 e r , WZKM. 8, 96 zu skr. ksud 'schlagen,
stampfen*. Aber die Bedeutung von np. Sustan ist
'waschen = reinigen', pOkTza kardan, vgl. paz. sus-
tan Vaschen, reinigen , bal. SOday Vaschen, reinigen,
baden etc.— 80 -
784. Np. SuS Xunge' aus suS mit Assimilation des Anlautes
an den Auslaut. Wenn sus = zd. 8U§i- = afgh.
### HUB 8305-8315
zd. xsi; sab 'Nacht* = ap. xsapa-iva) 'des Nachts'; sas
sechs*, zd. x§va$; suma *ihr*, gd. xsmakem (zd. yUsmakem
gen.); sinaxtan erkennen', pr. sinasam (oben p. 81), ap.
xsnasatiy; sahr *Stadt*, alter 'Land' = ap. xsa&''a-; sBb
'Abhang u. s. w. , zd. xsva^pd- ; mar i sibCL *Viper , seva
'beredt (oben p. 82, 83), zd. xsva^wa-; sSd 'Sonne*, zd. xsa^ta-;
§%r *Milch* = skr. kslra- ; sustan Vaschen H. 782 , oben
p. 79 ; mar *Gatte H. 796, oben p. 82 ; isnOsa 'Niesen H.
90, oben p. 15.
Nach Praefixen und in Komp. : nis^b abwarts, unten ,
phi. nisSpak Untergang (oben p. 101) = zd. '^nixsvaepa-
### HRN asuften
### HRN leaf29 (p8)
— 8
27. äsmän *Himmel', äsmä, semän,
g. asbän,
ap. asman- 'Himmel'; aw. asman-; phlv. äsmän; ai.
dgmafi-.
kiird. LW. asmärij äsimün, asmm; a{y, LW. äsmän;
bei. n. äzmän (22); sangl. minj. LW. asma, wa/. sar.
si/n. LW. äsmän,
28. äsüden ^beruhigen, ruhen', Praes. äsäy-em, -äsä,
äsäijis^ äsäyist (jüd.-per$.).
aw. *ä + sävayeitl (Bedeutung?); phlv. äsiitan^
äsäy(i)sn,
29. äs *Brühe, Speise .
skr. äga- in prataräga- Trühstück'. säyamäga- 'Abend-
essen ; vergl. aw. kahrkäsa- *Hühnerfresser.
kurd. LW. äspezyßne 'Küche'.
Zweifelhaft, denn np. s passt nicht zu skr. g, aw. s;
vergl. aber näsnä (No. 1019).
30. ÜHäm 'Trank', äsärmden,
aw. säman- 'Tropfen, vergl. fräsmi- (Geldner,
3 Yasht, 115); phlv. vergl. apisamak oder apismak
(vd. 5. 149, 7. 164).
31. äsH 'Friede*.
aw. äxsti' (ä/ßä), Bartholomae, Ar. Forsch. II,
100 (?); aw. ä/sti- 'Friede'; phlv. ästth, anästfh.
yayn. astiato forti 'se reconcilier (Tomaschek, 746).
32. äffuften, äSöften 'in Bewegung versetzen, Praes.
äsöb-em, äsöh, JTiNZIlÄ'N (Is. 9, 10), ]r;2^\t/^ (Is. 22, 5).
aw. ä-\-/sufsqn; phlv. äsöftan (vd. 9. 132, Gl.), äsöp
(d. i. äsöw)y äsöft'kärih (DK.); ai. [/^ksubh-, ksobhate
```


## [2026-09-06T21:43:07.858Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10700,10716p' BRT.txt | cat -n; echo \"--- nearby col numbers ---\"; awk 'NR>10650 && NR<10730 && /^[0-9]{3}$|55[0-9]|54[0-9]/' BRT.txt | head"
}
```


### [2026-09-06T21:43:09.539Z] TOOL RESULT

```
     1	Az-j;  — yim  yimim  't>m  Yt/p.  31;  — yimäi  °t5i  V./^.  39;  — yimat  haia  "iäi YL/^.35-
     2	KonripA.,  E. ').  —    \'gl.  axsattta-,    - ■Sonne'.  —  Pü.!  rSht.  (lu  Y.  26J:  ; 2  a):  j-am  JS.  —  OS  20?-  2  »E-  —  ")  S.  noch unter  kvanxia^la-,
     3	•  '].  xsaetö.puOrya-  n.  'Besiu  herrlicher
     4	xsaSra-  1  i
     5	542
     6	Söhne':  haomS  daaaiti ..''^rim  Uta  asava.- frasaintTm  X.g.tt.
     7	Ableit  aus  *j:jii//ö^iro- Adj.  —  Pü.:  hurdiiin
     8	fius,  Sü.:  diftimän  putra^.
     9	•  j.  xsao9ah-  n.  'Fluss,  Strömung,  Wasser- Schwall';  airy!>.layamm  .  ,  yahmya  äpu navaya  .  .  °taipha  %waxhnle  Yt  10. 14.
    10	:.  ifidas-  n.  —  Vgl.  lu  xsusla-. j.  xloodrinum  V.  16.  7:  lies  xsävd'. j.  xiaudrim  N.  6!# :  lies  xläud:
    11	•  j.  xsaob-  V.,  nur  Praes.  14  (Inkoh.) vu/sa-^^  'in  Aufregung  geraten', /u/  aspanqm  sri/a  (sd.)  xsufsqn  Yt./o.
    12	j.,  g.  xäaSra-,  p.  xSsO-'a-  n.  'imperium, regnum,  Herrschaft,  Reich';  uzw.  im  Sinn von  1)  "Herrschgewalt,  Obergewalt,  Herr- schermacht'"; i)  I  im  Ap.:  c^ur^mazdä h'am  mann  fmbara''  Bh./.s,i3;  9,  'D.4. 1,17. 1 ;  —  °^^am  iyt^  bäbirauv  hauv  agar- blyaiiJ  Bh.7.  16;  11';  —  vasnä  a^urO^- mazdäA^  imJ'  °h''am  därayämiy  Bh.  /. 9;  9;  —  °'ii''amiim  adam  adlnant  Bh./. 13;  i3i  —  "''"*  "ä'^'»'«  fy<^  gaumätc^ ty^  maguS  üdin^  ia''bBßyam  aitJ'  ''i'aiii ha'ä  paruviyata''  amäxam  taumäya  aha Bh./.i2;  —  '^'am  tyJ" ..paräbarfam  aha^ .  .patipadam  akunavam  Bh.  /.  1 4.  ||  2)  im jAw.T  uparäi  amäi  .  .  v»r?'hrSi  ..  °%räi A.  /.  8;  —  '%rakela  paiti  bäiiumais  dan- yayasca  paiti  darr^S.jXtSiS  Yt  y.  135; —  ''%r)mca  paiti.astlmca  darrfö.xsa^rfin "'hrahe  darr^5.j.ttJm  ustanahe  A.  /.  8;  — yim3  asti  hr.?>e(s6.}  '^rayä  (GD,)  V.  2. -  ^ahmi  '>re  Vr. /^_2(P);  P.  2^; — yimahe  °&re  nSit  aotftn  SnHa  .  .  yavata xsaySit  (sd.)  . ,  "unter  Ks  Herrschaft  .  ," Y.^.j;  V.2.S; — yim?m  . .  ye/'jhe  ''^rula .  .  nöit  aottm  fff»ha  . .  para  ahmSl  yat . . Yt.  IQ.  33 ;  —  yimS  . .  yat  kirmaot  aiähe '"ifräha  *amarsanta  pasu  vira  Y.g.  4;  Yt 15. 16; — Auxsa'hrS.ttmaiät  al  ""kmin  äfyai A.J.6;  —  zard^ustrim  ..ya^  as  ..*%rfm huxsa^rJ.ümS  (sd.)  \t  1^.79;  A.^.4,  Vs. 5^_j; —  'ir.lt  xsayamiia  VytJ5;  — yal^a anyhsBt  ""^räl  xlayamnä  hatnö-xiahrS.- xiayamnS  Yt.  J5.  54;  —  As  araHwya  '"^ra nsit  xiayeti  Vyt  47;  —  us  nü  atühäi  vJse jamyäl  asimea  "'hrsmca  savasca  .  .  Y.  60. 2;  —  zaraiiultrahe  ,  ,  paoiryai  hanhanuse gqrnifa  ahmla  .  .  uxüahyäca  (sd.)  i
    13	dby  Google
    14	543  x5a*ra-  I  3
    15	'hnm^a  YL  13.  88.  a)  mit  Gen.  'über  -' (s.  3  a):  ya>^a  aztm  up^mim  °'^r>in  baväni vispanqm    äaRyunqm    Yt5.  22.  3)   im
    16	gAw. :  ahya  '"kräXa  maziiiäcä  *hvapa- nhäisca  (sd.)  tsm  at  ,  .  yasamaidl  Y.^J/. a;  —  kudä  (sd.)  asim  vohuca  maus '%r)m^ä  Y.  25.  1 1 ;  —  yüism  aäbyS  .  . aogü  data  .  .  '%nmc3  .  .  yl  kuhitts  rä- mqmcS  (sd-)  däl  Y.  2p.  10;  —  isasä  (sd.) . .  maibyö  '"^nm  aojönahvat  yehy3  vfndä (sd.)  vanalmS  *drujim  Y.J/.  4;  benutzt V.ao.  8;  —  tat  mazdä  tava  '>rfm  yä  .. düAf  drigaov!\sA.)  vaiyj  Y.ß^.g;  — yJ vahyJ  varihSuS  dagdi..ahurö  '"S^rä  mazdä Y.5J.  6;  —  tici  '^rä  mazdä  dqmis  (sd.) ahurS  'V.4$.T,  9;  —  maibyS  masds  tavä rafinS  JräxStuiam  (sd.)  kyat  ^wä  °&rJ a/Jt  hacä  frqifa  Y.  4!?.  1 4 ;  34. 15;  —  y} dfmanahyä  'hnm  M^rahya  vä  daSySu:" va ../radahäi{sA.)  aspinzatä  Y.Ji,  16;  — yastJm  °ärJ/  mazäJ  mSÜai  (sd.)  jyätSul Vä  Y.  46.  4;  —  at  ratqm  zara'iuitrS  .  . dadäiij  paurvatätim  . .  mazdiU . .  ux^aHyäcß (sd.)  ifraespm  '"irimcä  "..  den  Gehorsam und  die  Herrschgewall"  \.33.i4;  benutzt Yt  IJ.  88 ;  —  vauhstts  dazd,l{%ü.)  manau/iS lyaöhananqm  a»fiSus  mazdäi  ''knmca ahuräi  a  X.2-j.iy,  —  hux^a^rSJimäi (sd.)  .  .  '"ir^m  .  .  äad)mahicä  cismahicä *hvqnmakicä  Y.^5. 5;  —  yS  dngvSUi '"^nm  hunüiiJ  {?,d.)  Y.j/,  15;  —  yais *ffrMm3{sd.)  asäivaratä..°'^r3mca  lianqm *dnfim  Y. 32.13;  —  '>rais  yujin  (sd.) karapanU  .  .  akäis  syaohanäis  .  .  Y.  46. II.  a)  mit  Gen.  'über  — '  (s.  2  a);  tarn
    17	kavä  vistäsps  magaAyä(^.)  'hrä  nasal., astlm  Y.5J.  16;  —  tu  v7  masdil  .  .'dSisä möi  isteis  (%A.)  -'hnm  Y.j/.a;  benutzt Vyt.  46.  b)  mit  InE:  ial  vi  xsair^m kii  Jltis  (sd.)  syadäaiiifi  mazda  Y.  34. j.  2)  'Henschgebiet"';  i)  II  im  Ap.-, mäm  ^ur^mazdi  päluv  utamaiy  °~ii''am via  tyt^  maiui  tartam  X.J.  4;  2.3,  4. 3.  2)   im  jAw.:  ya>a  .  .  masa  °>ra
--- nearby col numbers ---
542
543  x5a*ra-  I  3
544
545
546
```


## [2026-09-06T21:43:19.816Z] TOOL CALL #75: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg280.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/280.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-06T21:43:19.898Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T21:50:33.721Z] TOOL CALL #76: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk280.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nE = \"https://www.etymonline.com/word/\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Ksero\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ksē-ro- 'dry' (of sky and weather also 'dry = bright, clear'); AHD/Watkins *ksero-\",\n \"note\": \"Pokorny IEW p.625 heads the entry 'ksē-ro- \\u201etrocken\\u2018; vom Himmel und Wetter auch \\u201etrocken = hell, klar\\u2018', collecting exactly the material Nourai charts: Gk. \\u03be\\u03b5\\u03c1\\u03cc\\u03bd / \\u03be\\u03b7\\u03c1\\u03cc\\u03c2, Lat. serescunt, serenus, OHG serawen. Root name, language label ('Indo-European') and gloss ('dry') are therefore all faithful to the cited source, and Watkins (AHD) has the identical headword 'ksero-. Dry.' The one nuance the chart does not show is that Pokorny himself calls *ksē-ro- 'wahrscheinlich eine Erweiterung von ks\\u0101- \\u201ebrennen, versengen\\u2018' (p.624-5), and that the Latin branch is only 'perhaps' (Watkins) / 'possibly' (Klein) attached: Ernout\\u2013Meillet judge the whole group 'obscur et mal d\\u00e9fini'.\",\n \"note_fa\": \"\\u0631\\u06cc\\u0634\\u0647\\u0654 \\u0647\\u0646\\u062f\\u0648\\u0627\\u0631\\u0648\\u067e\\u0627\\u06cc\\u06cc \\u0622\\u063a\\u0627\\u0632\\u06cc\\u0646 *ks\\u0113-ro- \\u0628\\u0647 \\u0645\\u0639\\u0646\\u06cc \\u00ab\\u062e\\u0634\\u06a9\\u00bb \\u0627\\u0633\\u062a \\u0648 \\u067e\\u0648\\u06a9\\u0648\\u0631\\u0646\\u06cc \\u062f\\u0631 \\u0635 \\u06f6\\u06f2\\u06f5 \\u0647\\u0645\\u06cc\\u0646 \\u0633\\u0631\\u0648\\u0627\\u0698\\u0647 \\u0631\\u0627 \\u0628\\u0627 \\u0647\\u0645\\u06cc\\u0646 \\u0645\\u0639\\u0646\\u0627 \\u0622\\u0648\\u0631\\u062f\\u0647 \\u0648 \\u0627\\u0641\\u0632\\u0648\\u062f\\u0647 \\u0627\\u0633\\u062a \\u06a9\\u0647 \\u062f\\u0631\\u0628\\u0627\\u0631\\u0647\\u0654 \\u0622\\u0633\\u0645\\u0627\\u0646 \\u0648 \\u0647\\u0648\\u0627 \\u0645\\u0639\\u0646\\u06cc \\u00ab\\u0631\\u0648\\u0634\\u0646 \\u0648 \\u0635\\u0627\\u0641\\u00bb \\u0645\\u06cc\\u200c\\u062f\\u0647\\u062f\\u061b \\u067e\\u0633 \\u0646\\u0627\\u0645 \\u0631\\u06cc\\u0634\\u0647\\u060c \\u0628\\u0631\\u0686\\u0633\\u0628 \\u0632\\u0628\\u0627\\u0646\\u06cc \\u0648 \\u0645\\u0639\\u0646\\u0627\\u06cc\\u06cc \\u06a9\\u0647 \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u062f\\u0627\\u062f\\u0647 \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a. \\u0648\\u0627\\u062a\\u06a9\\u06cc\\u0646\\u0632 \\u062f\\u0631 \\u067e\\u06cc\\u0648\\u0633\\u062a \\u0641\\u0631\\u0647\\u0646\\u06af \\u0645\\u06cc\\u0631\\u0627\\u062b \\u0622\\u0645\\u0631\\u06cc\\u06a9\\u0627\\u06cc\\u06cc \\u0646\\u06cc\\u0632 \\u0647\\u0645\\u06cc\\u0646 \\u0631\\u06cc\\u0634\\u0647 \\u0631\\u0627 \\u0628\\u0627 \\u0647\\u0645\\u06cc\\u0646 \\u0645\\u0639\\u0646\\u0627 \\u062b\\u0628\\u062a \\u06a9\\u0631\\u062f\\u0647 \\u0627\\u0633\\u062a. \\u062a\\u0646\\u0647\\u0627 \\u0646\\u06a9\\u062a\\u0647\\u200c\\u0627\\u06cc \\u06a9\\u0647 \\u0646\\u0645\\u0648\\u062f\\u0627\\u0631 \\u0646\\u0634\\u0627\\u0646 \\u0646\\u0645\\u06cc\\u200c\\u062f\\u0647\\u062f \\u0627\\u06cc\\u0646 \\u0627\\u0633\\u062a \\u06a9\\u0647 \\u067e\\u06cc\\u0648\\u0646\\u062f \\u0644\\u0627\\u062a\\u06cc\\u0646\\u06cc serenus \\u0628\\u0627 \\u0627\\u06cc\\u0646 \\u0631\\u06cc\\u0634\\u0647 \\u0642\\u0637\\u0639\\u06cc \\u0646\\u06cc\\u0633\\u062a \\u0648 \\u0627\\u0631\\u0646\\u0648\\u2013\\u0645\\u0647\\u200c\\u06cc\\u0647 \\u0647\\u0645\\u0647\\u0654 \\u0627\\u06cc\\u0646 \\u062e\\u0648\\u0634\\u0647 \\u0631\\u0627 \\u00ab\\u062a\\u0627\\u0631\\u06cc\\u06a9 \\u0648 \\u0646\\u0627\\u0645\\u0634\\u062e\\u0635\\u00bb \\u062e\\u0648\\u0627\\u0646\\u062f\\u0647\\u200c\\u0627\\u0646\\u062f.\",\n \"sources\": [E+\"xero-\", W+\"\\u03be\\u03b7\\u03c1\\u03cc\\u03c2\"],\n \"ref_check\": [\n   {\"ref\": \"POK:625\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW p.625, read in POK_02.txt leaf 285-286 (awk 'BEGIN{RS=\\\"\\\\f\\\"} NR==285'): 'ks\\u0113-ro- \\u201etrocken\\u2018; vom Himmel und Wetter auch \\u201etrocken = hell, klar\\u2018. Gr. \\u03be\\u03b5\\u03c1\\u03cc\\u03bd (nur Akk.) \\u201efestes, trockenes Land\\u2018, dehnstufig \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 \\u201etrocken, d\\u00fcrr\\u2018 ... lat. serescunt ... serenus \\u201eheiter, hell, klar, trocken\\u2018 (vom Himmel und Wetter); ahd. serawen ... WP. I 503'. Exactly Nourai's root name, language and gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 503 s.v. kser- (WLD_Bd1_pages.txt leaf 512, running head 'kser- \\u2014 ksuelp- 503')\", \"stance\": \"supports\",\n    \"note\": \"'kser- \\u201etrocken\\u201c; vom Himmel und Wetter auch \\u201etrocken = hell, klar\\u201c. Gr. \\u03be\\u03b5\\u03c1\\u03cc\\u03bd ... lat. serescunt ... serenus \\u201eheiter, hell, klar, trocken\\u201c' \\u2014 the source Pokorny 625 refers to.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix s.v. ksero- (AHD_watkins1985.txt line 648)\", \"stance\": \"supports\",\n    \"note\": \"'ksero-. Dry. 1. Lengthened-grade form *ks\\u0113ro- in Greek x\\u0113ros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHALMIA. 2. Perhaps suffixed variant form *kseres-no- in Latin ser\\u0113nus, serene, bright, clear: SERENE. [Pok. ksero- 625.]' \\u2014 the whole chart in one entry, with 'Perhaps' on the Latin branch.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, Selected Synonyms 15.84 DRY \\u00a73 (SYN.txt line 27220 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'Grk. \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 ... prob. : Lat. seresc\\u0113re \\u201ebecome dry\\u2018, ser\\u0113nus \\u201efair\\u2018 (of weather), OHG serawen \\u201ebecome dry, wither\\u2018. Walde-P. 1.503, Ernout-M. 928.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, Indo-European Comparative Dictionary (IEC.txt line 8251)\", \"stance\": \"silent\",\n    \"note\": \"Mann's only 'Ksero-' is a homonym meaning 'sixsome' (to *ksue\\u1e31s 'six'); he has no entry for the 'dry' root, so the book neither supports nor contradicts.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\"id\":1,\"lang\":\"Greek\",\"words\":\"x\\u011bros\",\n  \"verdict\":\"plausible\",\n  \"derivation\":\"Greek \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 (x\\u0113r\\u00f3s) 'dry, withered' is the lengthened-grade *ks\\u0113-ro- beside the short-vowel \\u03be\\u03b5\\u03c1\\u03cc\\u03bd (only acc.) 'dry land' \\u2014 both are printed side by side on Pokorny's p.625, and Nourai's 'x\\u011bros' with a breve reflects the \\u03be\\u03b5\\u03c1- variant rather than the \\u03be\\u03b7\\u03c1- one. The gloss is where the node slips: \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 is simply the adjective 'dry', while 'dry powder, medicine' is the sense of the substantivised neuter derivative \\u03be\\u03b7\\u03c1\\u03af\\u03bf\\u03bd (x\\u0113r\\u00edon) 'desiccative powder for wounds', which is the actual etymon of Arabic al-iks\\u012br. Nourai has telescoped the two forms into one box, so the arrow to Arabic is right but the form it starts from is not the one the sources name. A further caveat that neither Nourai nor his sources flag: Wiktionary notes that the lengthened \\u03b7 where \\u03b5 is expected is itself problematic.\",\n  \"derivation_fa\":\"\\u06cc\\u0648\\u0646\\u0627\\u0646\\u06cc \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 (x\\u0113r\\u00f3s) \\u06cc\\u0639\\u0646\\u06cc \\u00ab\\u062e\\u0634\\u06a9\\u060c \\u067e\\u0698\\u0645\\u0631\\u062f\\u0647\\u00bb\\u060c \\u0635\\u0648\\u0631\\u062a \\u06a9\\u0634\\u06cc\\u062f\\u0647\\u0654 *ks\\u0113-ro- \\u0627\\u0633\\u062a \\u062f\\u0631 \\u0628\\u0631\\u0627\\u0628\\u0631 \\u03be\\u03b5\\u03c1\\u03cc\\u03bd \\u00ab\\u062e\\u0634\\u06a9\\u06cc\\u060c \\u062e\\u0634\\u06a9\\u06cc \\u062f\\u0631\\u06cc\\u0627\\u00bb \\u06a9\\u0647 \\u067e\\u0648\\u06a9\\u0648\\u0631\\u0646\\u06cc \\u0647\\u0631 \\u062f\\u0648 \\u0631\\u0627 \\u062f\\u0631 \\u0635 \\u06f6\\u06f2\\u06f5 \\u06a9\\u0646\\u0627\\u0631 \\u0647\\u0645 \\u0622\\u0648\\u0631\\u062f\\u0647 \\u0627\\u0633\\u062a. \\u0627\\u0645\\u0627 \\u0645\\u0639\\u0646\\u0627\\u06cc\\u06cc \\u06a9\\u0647 \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u062f\\u0627\\u062f\\u0647 (\\u00ab\\u06af\\u0631\\u062f \\u062e\\u0634\\u06a9\\u060c \\u062f\\u0627\\u0631\\u0648\\u00bb) \\u0627\\u0632 \\u0622\\u0646\\u0650 \\u062e\\u0648\\u062f \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 \\u0646\\u06cc\\u0633\\u062a \\u0628\\u0644\\u06a9\\u0647 \\u0627\\u0632 \\u0622\\u0646\\u0650 \\u0645\\u0634\\u062a\\u0642 \\u062e\\u0646\\u062b\\u0627\\u06cc \\u0622\\u0646 \\u03be\\u03b7\\u03c1\\u03af\\u03bf\\u03bd (x\\u0113r\\u00edon) \\u00ab\\u06af\\u0631\\u062f\\u0650 \\u062f\\u0627\\u0631\\u0648\\u06cc\\u06cc \\u062e\\u0634\\u06a9\\u200c\\u06a9\\u0646\\u0646\\u062f\\u0647\\u0654 \\u0632\\u062e\\u0645\\u00bb \\u0627\\u0633\\u062a \\u06a9\\u0647 \\u0647\\u0645\\u06cc\\u0646 \\u0648\\u0627\\u0698\\u0647 \\u0627\\u0635\\u0644 \\u0639\\u0631\\u0628\\u06cc \\u0627\\u0644\\u0625\\u06a9\\u0633\\u06cc\\u0631 \\u0627\\u0633\\u062a\\u061b \\u067e\\u0633 \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u062f\\u0648 \\u0635\\u0648\\u0631\\u062a \\u0631\\u0627 \\u062f\\u0631 \\u06cc\\u06a9 \\u062c\\u0639\\u0628\\u0647 \\u0627\\u062f\\u063a\\u0627\\u0645 \\u06a9\\u0631\\u062f\\u0647 \\u0627\\u0633\\u062a. \\u062c\\u0647\\u062a \\u0648\\u0627\\u0645\\u200c\\u06af\\u06cc\\u0631\\u06cc \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a \\u0648\\u0644\\u06cc \\u0635\\u0648\\u0631\\u062a \\u0645\\u0628\\u062f\\u0623 \\u062f\\u0642\\u06cc\\u0642 \\u0646\\u06cc\\u0633\\u062a\\u061b \\u0628\\u0646\\u0627\\u0628\\u0631\\u0627\\u06cc\\u0646 \\u0627\\u062f\\u0639\\u0627 \\u0628\\u0627 \\u0627\\u062d\\u062a\\u06cc\\u0627\\u0637 \\u067e\\u0630\\u06cc\\u0631\\u0641\\u062a\\u0646\\u06cc \\u0627\\u0633\\u062a.\",\n  \"sources\":[W+\"\\u03be\\u03b7\\u03c1\\u03cc\\u03c2\", E+\"xero-\", E+\"elixir\"],\n  \"ref_check\":[\n    {\"ref\":\"POK:625\",\"status\":\"supports\",\"note\":\"POK_02.txt leaf 285-286: 'Gr. \\u03be\\u03b5\\u03c1\\u03cc\\u03bd (nur Akk.) \\u201efestes, trockenes Land\\u2018, dehnstufig \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 \\u201etrocken, d\\u00fcrr\\u2018' \\u2014 the Greek word is there under this root, but with the plain sense 'dry', not 'dry powder, medicine'.\"},\n    {\"ref\":\"AHD:424\",\"status\":\"partial\",\"note\":\"The New College Edition p.424 (the dictionary entry 'elixir', which is where AHD gives 'Late Greek x\\u0113rion, desiccative powder, from Greek x\\u0113ros, dry. See ksero- in Appendix') could not be paged: only the appendix is on disk. The appendix entry (AHD_watkins1985.txt line 648) does say 'Lengthened-grade form *ks\\u0113ro- in Greek x\\u0113ros, dry: XERO-; ELIXIR ...', i.e. it supports the substance of the arrow.\"}\n  ],\n  \"consulted\":[\n    {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. elixir, KLN_1966.txt leaf 277 (printed p.508-509)\",\"stance\":\"partial\",\n     \"note\":\"'ML., fr. Arab. al-iksir, which is formed fr. Arab. al-, \\u201ethe\\u2018, and Gk. \\u03be\\u03b7\\u03c1\\u03af\\u03bf\\u03bd, \\u201edry medicinal substance, cataplasm\\u2018, fr. \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 \\u201edry\\u2018' \\u2014 Klein separates the two Greek forms that Nourai's single box merges.\"},\n    {\"src\":\"SYN\",\"where\":\"Buck 15.84 DRY \\u00a73 (SYN.txt line 27220 ff.)\",\"stance\":\"supports\",\n     \"note\":\"lists Grk. \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 as the ordinary word for 'dry', 'prob. : Lat. seresc\\u0113re, ser\\u0113nus ... Walde-P. 1.503'.\"},\n    {\"src\":\"WLD\",\"where\":\"Walde-Pokorny I 503 (WLD_Bd1_pages.txt leaf 512)\",\"stance\":\"supports\",\n     \"note\":\"'Gr. \\u03be\\u03b5\\u03c1\\u03cc\\u03bd (*nur Akk.) \\u201efestes, trockenes Land\\u201c, dehnstufig \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 \\u201etrocken, d\\u00fcrr\\u201c'.\"}\n  ]},\n\n {\"id\":2,\"lang\":\"Arabic\",\"words\":\"al-iksir\",\n  \"verdict\":\"confirmed\",\n  \"derivation\":\"Arabic \\u0627\\u0644\\u0625\\u0643\\u0633\\u064a\\u0631 al-iks\\u012br 'the philosophers' stone; elixir' = the article al- + iks\\u012br, a loan of Greek \\u03be\\u03b7\\u03c1\\u03af\\u03bf\\u03bd x\\u0113r\\u00edon 'drying powder (for wounds)'; the Greek \\u03be- (ks-) is rendered by Arabic \\u0643\\u0633 ks, which Devic (1876) defends against the objection that Arabic usually writes Greek \\u03be as \\u0633\\u0643 sk. Wiktionary adds the intermediary the chart omits: the word reached Arabic through Classical Syriac \\u071f\\u0723\\u071d\\u072a\\u071d\\u0722 (ks\\u012br\\u012bn), i.e. through the Syriac-speaking translators of Greek medicine and alchemy in the 8th-9th c. In Arabic alchemy (J\\u0101bir, al-R\\u0101z\\u012b) it became the name of the transmuting substance, whence Medieval Latin elixir.\",\n  \"derivation_fa\":\"\\u0639\\u0631\\u0628\\u06cc \\u0627\\u0644\\u0625\\u06a9\\u0633\\u06cc\\u0631 \\u0645\\u0631\\u06a9\\u0651\\u0628 \\u0627\\u0633\\u062a \\u0627\\u0632 \\u062d\\u0631\\u0641 \\u062a\\u0639\\u0631\\u06cc\\u0641 \\u00ab\\u0627\\u0644\\u00bb \\u0648 \\u0625\\u06a9\\u0633\\u06cc\\u0631\\u060c \\u0648 \\u0625\\u06a9\\u0633\\u06cc\\u0631 \\u0648\\u0627\\u0645\\u200c\\u0648\\u0627\\u0698\\u0647\\u200c\\u0627\\u06cc \\u0627\\u0633\\u062a \\u0627\\u0632 \\u06cc\\u0648\\u0646\\u0627\\u0646\\u06cc \\u03be\\u03b7\\u03c1\\u03af\\u03bf\\u03bd \\u00ab\\u06af\\u0631\\u062f\\u0650 \\u062e\\u0634\\u06a9\\u200c\\u06a9\\u0646\\u0646\\u062f\\u0647\\u0654 \\u0632\\u062e\\u0645\\u00bb. \\u062f\\u0648\\u06cc\\u06a9 (\\u06f1\\u06f8\\u06f7\\u06f6) \\u0647\\u0645\\u06cc\\u0646 \\u0631\\u0627 \\u0645\\u06cc\\u200c\\u06af\\u0648\\u06cc\\u062f \\u0648 \\u0627\\u06cc\\u0631\\u0627\\u062f \\u06a9\\u0633\\u0627\\u0646\\u06cc \\u0631\\u0627 \\u06a9\\u0647 \\u0645\\u06cc\\u200c\\u06af\\u0641\\u062a\\u0646\\u062f \\u0639\\u0631\\u0628 \\u03be \\u06cc\\u0648\\u0646\\u0627\\u0646\\u06cc \\u0631\\u0627 \\u0647\\u0645\\u0648\\u0627\\u0631\\u0647 \\u00ab\\u0633\\u06a9\\u00bb \\u0645\\u06cc\\u200c\\u0646\\u0648\\u06cc\\u0633\\u062f \\u067e\\u0627\\u0633\\u062e \\u0645\\u06cc\\u200c\\u062f\\u0647\\u062f. \\u0648\\u06cc\\u06a9\\u06cc\\u200c\\u0648\\u0627\\u0698\\u0647 \\u062d\\u0644\\u0642\\u0647\\u0654 \\u0645\\u06cc\\u0627\\u0646\\u06cc \\u0631\\u0627 \\u0646\\u06cc\\u0632 \\u0645\\u06cc\\u200c\\u0627\\u0641\\u0632\\u0627\\u06cc\\u062f: \\u0648\\u0627\\u0698\\u0647 \\u0627\\u0632 \\u0631\\u0627\\u0647 \\u0633\\u0631\\u06cc\\u0627\\u0646\\u06cc ks\\u012br\\u012bn \\u2014 \\u06cc\\u0639\\u0646\\u06cc \\u0627\\u0632 \\u0631\\u0627\\u0647 \\u0645\\u062a\\u0631\\u062c\\u0645\\u0627\\u0646 \\u0633\\u0631\\u06cc\\u0627\\u0646\\u06cc\\u200c\\u0632\\u0628\\u0627\\u0646 \\u067e\\u0632\\u0634\\u06a9\\u06cc \\u0648 \\u06a9\\u06cc\\u0645\\u06cc\\u0627\\u06cc \\u06cc\\u0648\\u0646\\u0627\\u0646\\u06cc \\u062f\\u0631 \\u0633\\u062f\\u0647\\u0654 \\u062f\\u0648\\u0645 \\u0648 \\u0633\\u0648\\u0645 \\u0647\\u062c\\u0631\\u06cc \\u2014 \\u0628\\u0647 \\u0639\\u0631\\u0628\\u06cc \\u0631\\u0633\\u06cc\\u062f\\u0647 \\u0627\\u0633\\u062a. \\u0627\\u062f\\u0639\\u0627\\u06cc \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a.\",\n  \"sources\":[W+\"\\u0625\\u0643\\u0633\\u064a\\u0631\", E+\"elixir\"],\n  \"ref_check\":[\n    {\"ref\":\"AHD:424\",\"status\":\"partial\",\"note\":\"AHD New College p.424 (s.v. elixir) not on disk; the appendix entry ksero- (AHD_watkins1985.txt line 648) lists ELIXIR among the English words from Greek x\\u0113ros, which is the same claim. Klein, Lokotsch, Webster and Devic (below) all state the Greek > Arabic step explicitly.\"}\n  ],\n  \"consulted\":[\n    {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. elixir (KLN_1966.txt leaf 277, p.508-509)\",\"stance\":\"supports\",\n     \"note\":\"'ML., fr. Arab. al-iksir, which is formed fr. Arab. al-, \\u201ethe\\u2018, and Gk. \\u03be\\u03b7\\u03c1\\u03af\\u03bf\\u03bd, \\u201edry medicinal substance, cataplasm\\u2018, fr. \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 \\u201edry\\u2018.'\"},\n    {\"src\":\"LKT\",\"where\":\"Lokotsch 1927 no.903 (LKT.txt, 'Ar. iksir')\",\"stance\":\"supports\",\n     \"note\":\"'903. Ar. iksir: [Aus gr. \\u03be\\u03b7\\u03c1\\u03af\\u03bf\\u03bd \\u201edas Trockene\\u2018] \\u201eStein der Weisen\\u2018 ... hieraus it. elissire, elisire, frz. \\u00e9lixir, sp. pg. rum. elixir, dtsch. Elixir, engl. elixir. [DE 259/260. Devic 108/109. Lammens Rem 104/105.]' \\u2014 covers the whole chain including Nourai's DEV:108.\"},\n    {\"src\":\"DEV\",\"where\":\"Devic 1876 pp.108-109 (DEV.txt leaf 141)\",\"stance\":\"supports\",\n     \"note\":\"'Elixir. ... C'est l'arabe el-iks\\u012br ... Le mot arabe lui-m\\u00eame n'est autre chose que la transcription du grec \\u03be\\u03b7\\u03c1\\u03cc\\u03bd, sec, m\\u00e9dicament sec.'\"},\n    {\"src\":\"WEB\",\"where\":\"Webster's New Twentieth Century, vol.1 s.v. elixir (WEB_vol1.txt line 62979)\",\"stance\":\"supports\",\n     \"note\":\"'from Ar. el iksir, the philosopher's stone; el, al, the, and iksir, philosopher's stone; prob. from Gr. x\\u0113ros, dry.'\"},\n    {\"src\":\"FVQ\",\"where\":\"Jeffery, Foreign Vocabulary of the Qur'an (FVQ.txt, grep 'iksir')\",\"stance\":\"silent\",\n     \"note\":\"no hit \\u2014 the word is not Qur'anic, so Jeffery has no entry.\"},\n    {\"src\":\"AFM\",\"where\":\"Addi Shir, al-Alfaz al-Farisiyya al-Mu'arraba (AFM.txt, grep '\\u0627\\u0643\\u0633\\u064a\\u0631/\\u0625\\u0643\\u0633\\u064a\\u0631')\",\"stance\":\"silent\",\n     \"note\":\"no hit \\u2014 Addi Shir lists Persian loans in Arabic and does not treat this Greek one.\"}\n  ]},\n\n {\"id\":3,\"lang\":\"Persian\",\"words\":\"eks\\u00eer\",\n  \"verdict\":\"confirmed\",\n  \"derivation\":\"New Persian \\u0627\\u06a9\\u0633\\u06cc\\u0631 eks\\u012br is a straight loan back from Arabic al-iks\\u012br, taken over without the article, as regularly with Arabic alchemical vocabulary in Persian from the 4th/10th c. on; it is a standard word of classical Persian alchemy and of the mystical lexicon (H\\u0101fez, quoted in the chart: '... b\\u0101tel dar \\u012bn xay\\u0101l ke eks\\u012br m\\u012bkonand'). Dehkhoda marks it '\\u0645\\u0639\\u0631\\u0628' and Mo'in '[\\u0645\\u0639\\u0631.]', i.e. an Arabicised (ultimately Greek) word, not an inherited Iranian one; so the chart's Arabic > Persian arrow is right, and the ultimate Greek origin comes with it.\",\n  \"derivation_fa\":\"\\u00ab\\u0627\\u06a9\\u0633\\u06cc\\u0631\\u00bb \\u062f\\u0631 \\u0641\\u0627\\u0631\\u0633\\u06cc \\u0646\\u0648 \\u0648\\u0627\\u0645\\u200c\\u0648\\u0627\\u0698\\u0647\\u200c\\u0627\\u06cc \\u0627\\u0633\\u062a \\u0627\\u0632 \\u0639\\u0631\\u0628\\u06cc \\u0627\\u0644\\u0625\\u06a9\\u0633\\u06cc\\u0631 \\u06a9\\u0647 \\u0628\\u062f\\u0648\\u0646 \\u062d\\u0631\\u0641 \\u062a\\u0639\\u0631\\u06cc\\u0641 \\u0648\\u0627\\u0645 \\u06af\\u0631\\u0641\\u062a\\u0647 \\u0634\\u062f\\u0647 \\u2014 \\u0647\\u0645\\u0627\\u0646\\u200c\\u06af\\u0648\\u0646\\u0647 \\u06a9\\u0647 \\u062f\\u06cc\\u06af\\u0631 \\u0627\\u0635\\u0637\\u0644\\u0627\\u062d\\u0627\\u062a \\u06a9\\u06cc\\u0645\\u06cc\\u0627 \\u0627\\u0632 \\u0633\\u062f\\u0647\\u0654 \\u0686\\u0647\\u0627\\u0631\\u0645 \\u0647\\u062c\\u0631\\u06cc \\u0628\\u0647 \\u0628\\u0639\\u062f. \\u062f\\u0647\\u062e\\u062f\\u0627 \\u0622\\u0646 \\u0631\\u0627 \\u00ab\\u0645\\u0639\\u0631\\u0651\\u0628\\u00bb \\u0648 \\u0645\\u0639\\u06cc\\u0646 \\u0622\\u0646 \\u0631\\u0627 \\u00ab[\\u0645\\u0639\\u0631.]\\u00bb \\u0646\\u0634\\u0627\\u0646\\u0647 \\u0632\\u062f\\u0647\\u200c\\u0627\\u0646\\u062f\\u060c \\u067e\\u0633 \\u0648\\u0627\\u0698\\u0647 \\u0627\\u06cc\\u0631\\u0627\\u0646\\u06cc\\u200c\\u062a\\u0628\\u0627\\u0631 \\u0646\\u06cc\\u0633\\u062a \\u0648 \\u0633\\u0631\\u0627\\u0646\\u062c\\u0627\\u0645 \\u0628\\u0647 \\u06cc\\u0648\\u0646\\u0627\\u0646\\u06cc \\u03be\\u03b7\\u03c1\\u03af\\u03bf\\u03bd \\u0645\\u06cc\\u200c\\u0631\\u0633\\u062f. \\u0627\\u062f\\u0639\\u0627\\u06cc \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a.\",\n  \"sources\":[\"https://abadis.ir/fatofa/\\u0627\\u06a9\\u0633\\u06cc\\u0631/\", W+\"\\u0625\\u0643\\u0633\\u064a\\u0631\"],\n  \"ref_check\":[\n    {\"ref\":\"MON:331\",\"status\":\"partial\",\n     \"note\":\"The 6-vol Amir Kabir pagination cannot be checked on disk; in the two-volume Mo'in on disk the entry stands at MON_part1.txt line 15846 (running head '\\u06f1\\u06f8\\u06f2 \\u0641\\u0631\\u0647\\u0646\\u06af \\u0641\\u0627\\u0631\\u0633\\u06cc \\u0645\\u0639\\u06cc\\u0646' two pages earlier, i.e. p.182-183 of that edition): '\\u0627\\u06a9\\u0633\\u06cc\\u0631: (\\u0627.) (\\u06a9\\u06cc\\u0645.) \\u062c\\u0648\\u0647\\u0631\\u06cc \\u06af\\u062f\\u0627\\u0632\\u0646\\u062f\\u0647 \\u06a9\\u0647 \\u0645\\u0627\\u0647\\u06cc\\u062a \\u0627\\u062c\\u0633\\u0627\\u0645 \\u0631\\u0627 \\u062a\\u063a\\u06cc\\u06cc\\u0631 \\u062f\\u0647\\u062f ...'. The vajehyab/abadis text of the same entry carries Mo'in's origin tag '[\\u0645\\u0639\\u0631.]' (mu'arrab = Arabicised), which is exactly the claim the arrow makes.\"}\n  ],\n  \"consulted\":[\n    {\"src\":\"MON\",\"where\":\"Farhang-e Fars\\u012b s.v. \\u0627\\u06a9\\u0633\\u06cc\\u0631, via abadis.ir\",\"stance\":\"supports\",\n     \"note\":\"'\\u0627\\u06a9\\u0633\\u06cc\\u0631 (\\u0627\\u0650) [\\u0645\\u0639\\u0631.] (\\u0627\\u0650.) \\u06f1- \\u0645\\u0627\\u062f\\u0647 \\u0627\\u06cc \\u06a9\\u0647 \\u0645\\u0627\\u0647\\u06cc\\u062a \\u0627\\u062c\\u0633\\u0627\\u0645 \\u0631\\u0627 \\u062a\\u063a\\u06cc\\u06cc\\u0631 \\u062f\\u0647\\u062f \\u0648 \\u0628\\u0627 \\u0627\\u0631\\u0632\\u0634 \\u062a\\u0631 \\u0633\\u0627\\u0632\\u062f' \\u2014 tagged as an Arabicised word.\"},\n    {\"src\":\"BQT\",\"where\":\"Borhan-e Qate' vol.1 (BQT_v1_pages.txt, grep '\\u0627\\u06a9\\u0633\\u06cc\\u0631')\",\"stance\":\"silent\",\n     \"note\":\"no hit in the OCR of vol.1; Dehkhoda (abadis) cites Borhan for the sense ('\\u0627\\u0632 \\u0628\\u0631\\u0647\\u0627\\u0646') but the etymology there is not given.\"},\n    {\"src\":\"ARY\",\"where\":\"Aryanpur, Farhang-e Rishe-ha (incoming/ARY, grep '\\u0627\\u06a9\\u0633\\u06cc\\u0631')\",\"stance\":\"silent\",\n     \"note\":\"no entry \\u2014 Aryanpur covers only inherited Indo-European Persian vocabulary, and eks\\u012br is a Semitic-mediated loan.\"}\n  ]},\n\n {\"id\":4,\"lang\":\"French\",\"words\":\"\",\n  \"verdict\":\"confirmed\",\n  \"derivation\":\"The box is a pass-through with no word printed: the intended form is French \\u00e9lixir, attested from the 13th c. in alchemical Latin/French texts and taken from Medieval Latin elixir, itself from Arabic al-iks\\u012br, through the Latin translations of Arabic alchemy made in Spain in the 12th c. Devic p.108-109, the reference Nourai cites, is precisely the article 'Elixir' and gives the Spanish, Portuguese and Italian cognates alongside the French word.\",\n  \"derivation_fa\":\"\\u0627\\u06cc\\u0646 \\u062e\\u0627\\u0646\\u0647 \\u062f\\u0631 \\u06a9\\u062a\\u0627\\u0628 \\u062e\\u0627\\u0644\\u06cc \\u0686\\u0627\\u067e \\u0634\\u062f\\u0647 \\u0648 \\u062a\\u0646\\u0647\\u0627 \\u062d\\u0644\\u0642\\u0647\\u0654 \\u0645\\u06cc\\u0627\\u0646\\u062c\\u06cc \\u0627\\u0633\\u062a\\u061b \\u0648\\u0627\\u0698\\u0647\\u0654 \\u0645\\u0648\\u0631\\u062f \\u0646\\u0638\\u0631 \\u0641\\u0631\\u0627\\u0646\\u0633\\u0648\\u06cc \\u00e9lixir \\u0627\\u0633\\u062a \\u06a9\\u0647 \\u0627\\u0632 \\u0644\\u0627\\u062a\\u06cc\\u0646\\u06cc \\u0645\\u06cc\\u0627\\u0646\\u0647 elixir \\u0648 \\u0622\\u0646 \\u0627\\u0632 \\u0639\\u0631\\u0628\\u06cc \\u0627\\u0644\\u0625\\u06a9\\u0633\\u06cc\\u0631 \\u06af\\u0631\\u0641\\u062a\\u0647 \\u0634\\u062f\\u0647\\u060c \\u0627\\u0632 \\u0631\\u0627\\u0647 \\u062a\\u0631\\u062c\\u0645\\u0647\\u0654 \\u0645\\u062a\\u0648\\u0646 \\u06a9\\u06cc\\u0645\\u06cc\\u0627\\u06cc \\u0639\\u0631\\u0628\\u06cc \\u062f\\u0631 \\u0627\\u0633\\u067e\\u0627\\u0646\\u06cc\\u0627\\u06cc \\u0633\\u062f\\u0647\\u0654 \\u062f\\u0648\\u0627\\u0632\\u062f\\u0647\\u0645 \\u0645\\u06cc\\u0644\\u0627\\u062f\\u06cc. \\u0627\\u0631\\u062c\\u0627\\u0639 \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u0628\\u0647 \\u062f\\u0648\\u06cc\\u06a9 \\u0635 \\u06f1\\u06f0\\u06f8 \\u062f\\u0642\\u06cc\\u0642\\u0627\\u064b \\u0647\\u0645\\u06cc\\u0646 \\u0645\\u062f\\u062e\\u0644 \\u0627\\u0633\\u062a.\",\n  \"sources\":[E+\"elixir\"],\n  \"ref_check\":[\n    {\"ref\":\"DEV:108\",\"status\":\"supports\",\n     \"note\":\"Devic 1876, article 'Elixir', pp.108-109 = DEV.txt leaf 141 (the running head 'DES MOTS D'ORIGINE ORIENTALE. 109' falls in the middle of that leaf): 'Elixir. Esp. et portug. elixir, ital. elisire. C'est l'arabe el-iks\\u012br, terme par lequel les alchimistes d\\u00e9signent la pierre philosophale ... Le mot arabe lui-m\\u00eame n'est autre chose que la transcription du grec \\u03be\\u03b7\\u03c1\\u03cc\\u03bd, sec, m\\u00e9dicament sec.'\"}\n  ],\n  \"consulted\":[\n    {\"src\":\"LKT\",\"where\":\"Lokotsch no.903 (LKT.txt)\",\"stance\":\"supports\",\"note\":\"'hieraus it. elissire, elisire \\u201eHeiltrank\\u2018, frz. elixir, sp. pg. rum. elixir, dtsch. Elixir, engl. elixir', citing 'Devic 108/109'.\"},\n    {\"src\":\"PHN\",\"where\":\"Pihan 1866 (PHN.txt, grep 'elixir')\",\"stance\":\"silent\",\"note\":\"no hit in the OCR; Pihan's list does not carry the article.\"},\n    {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. elixir (leaf 277)\",\"stance\":\"partial\",\"note\":\"Klein routes English elixir directly from Medieval Latin rather than through French, so the chart's French link is an addition (a legitimate one \\u2014 cp. Devic and Lokotsch).\"}\n  ]},\n\n {\"id\":5,\"lang\":\"English\",\"words\":\"elixir\",\n  \"verdict\":\"confirmed\",\n  \"derivation\":\"English elixir is attested from the mid-13th c. in the alchemical sense 'philosophers' stone', from Medieval Latin elixir (Klein) or through French \\u00e9lixir (Devic, Lokotsch); the sense 'sovereign remedy, strong tonic' is 1590s and the quack-medicine use 1630s. The route Greek \\u03be\\u03b7\\u03c1\\u03af\\u03bf\\u03bd > (Syriac) > Arabic al-iks\\u012br > Med.Lat. > Fr./Eng. is uncontroversial and agreed by Klein, Lokotsch, Webster and Etymonline.\",\n  \"derivation_fa\":\"\\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc elixir \\u0627\\u0632 \\u0646\\u06cc\\u0645\\u0647\\u0654 \\u0633\\u062f\\u0647\\u0654 \\u0633\\u06cc\\u0632\\u062f\\u0647\\u0645 \\u0645\\u06cc\\u0644\\u0627\\u062f\\u06cc \\u0628\\u0647 \\u0645\\u0639\\u0646\\u06cc \\u00ab\\u0633\\u0646\\u06af \\u06a9\\u06cc\\u0645\\u06cc\\u0627\\u00bb \\u062f\\u06cc\\u062f\\u0647 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f\\u060c \\u0627\\u0632 \\u0644\\u0627\\u062a\\u06cc\\u0646\\u06cc \\u0645\\u06cc\\u0627\\u0646\\u0647 elixir \\u06cc\\u0627 \\u0627\\u0632 \\u0631\\u0627\\u0647 \\u0641\\u0631\\u0627\\u0646\\u0633\\u0648\\u06cc\\u061b \\u0645\\u0639\\u0646\\u06cc \\u00ab\\u062f\\u0627\\u0631\\u0648\\u06cc \\u0634\\u0641\\u0627\\u0628\\u062e\\u0634\\u00bb \\u0627\\u0632 \\u062f\\u0647\\u0647\\u0654 \\u06f1\\u06f5\\u06f9\\u06f0 \\u0648 \\u06a9\\u0627\\u0631\\u0628\\u0631\\u062f \\u0622\\u0646 \\u0628\\u0631\\u0627\\u06cc \\u062f\\u0627\\u0631\\u0648\\u0647\\u0627\\u06cc \\u0634\\u06cc\\u0627\\u062f\\u0627\\u0646\\u0647 \\u0627\\u0632 \\u062f\\u0647\\u0647\\u0654 \\u06f1\\u06f6\\u06f3\\u06f0 \\u0627\\u0633\\u062a. \\u0632\\u0646\\u062c\\u06cc\\u0631\\u0647\\u0654 \\u06cc\\u0648\\u0646\\u0627\\u0646\\u06cc \\u2190 \\u0633\\u0631\\u06cc\\u0627\\u0646\\u06cc \\u2190 \\u0639\\u0631\\u0628\\u06cc \\u2190 \\u0644\\u0627\\u062a\\u06cc\\u0646\\u06cc \\u0645\\u06cc\\u0627\\u0646\\u0647 \\u2190 \\u0641\\u0631\\u0627\\u0646\\u0633\\u0648\\u06cc/\\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc \\u0645\\u0648\\u0631\\u062f \\u0627\\u062a\\u0641\\u0627\\u0642 \\u06a9\\u0644\\u0627\\u06cc\\u0646\\u060c \\u0644\\u0648\\u06a9\\u0648\\u0686\\u060c \\u0648\\u0628\\u0633\\u062a\\u0631 \\u0648 \\u0627\\u062a\\u06cc\\u0645\\u0648\\u0622\\u0646\\u200c\\u0644\\u0627\\u06cc\\u0646 \\u0627\\u0633\\u062a\\u061b \\u0627\\u062f\\u0639\\u0627\\u06cc \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a.\",\n  \"sources\":[E+\"elixir\"],\n  \"ref_check\":[\n    {\"ref\":\"KLN:509\",\"status\":\"supports\",\n     \"note\":\"Klein 1966 vol.I, the leaf carrying the printed page number 508 (KLN_1966.txt leaf 277 = pp.508-509), s.v. 'elixir, n., 1) a substance supposed to prolong life; 2) a substance supposed to change all metals into gold. \\u2014 ML., fr. Arab. al-iksir ... and Gk. \\u03be\\u03b7\\u03c1\\u03af\\u03bf\\u03bd ... fr. \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 \\u201edry\\u2018. See serene and cp. xero-.' \\u2014 Nourai's page number is exact, and Klein's own cross-references reproduce the whole chart.\"}\n  ],\n  \"consulted\":[\n    {\"src\":\"LKT\",\"where\":\"Lokotsch no.903\",\"stance\":\"supports\",\"note\":\"'... dtsch. Elixir, engl. elixir.'\"},\n    {\"src\":\"WEB\",\"where\":\"Webster's 2nd ed. s.v. elixir (WEB_vol1.txt line 62979)\",\"stance\":\"supports\",\"note\":\"'from Ar. el iksir ... prob. from Gr. x\\u0113ros, dry.'\"},\n    {\"src\":\"SKT\",\"where\":\"Skeat, Concise Etym. Dict. (SKT.txt, grep 'Elixir')\",\"stance\":\"silent\",\"note\":\"no hit in the OCR of the concise edition.\"}\n  ]},\n\n {\"id\":6,\"lang\":\"English\",\"words\":\"xer-, xero-; xeroderma\",\n  \"verdict\":\"confirmed\",\n  \"derivation\":\"English xero- (before a vowel xer-) is the learned combining form of Greek \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 'dry', taken directly from Greek into scientific Latin from the mid-19th c.; xeroderma 'roughening/dryness of the skin' is a Medical Latin compound coined by the English dermatologist Erasmus Wilson from xero- + Greek \\u03b4\\u03ad\\u03c1\\u03bc\\u03b1 'skin'. Nourai's gloss 'roughness of the skin' is Klein's own wording, and the branch is a direct Greek > English learned borrowing rather than an inherited one, which the chart's arrow from the Greek box correctly represents.\",\n  \"derivation_fa\":\"\\u067e\\u06cc\\u0634\\u0648\\u0646\\u062f \\u0639\\u0644\\u0645\\u06cc \\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc xero- (\\u067e\\u06cc\\u0634 \\u0627\\u0632 \\u0648\\u0627\\u06a9\\u0647 xer-) \\u0635\\u0648\\u0631\\u062a \\u062a\\u0631\\u06a9\\u06cc\\u0628\\u06cc \\u06cc\\u0648\\u0646\\u0627\\u0646\\u06cc \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 \\u00ab\\u062e\\u0634\\u06a9\\u00bb \\u0627\\u0633\\u062a \\u06a9\\u0647 \\u0627\\u0632 \\u0645\\u06cc\\u0627\\u0646\\u0647\\u0654 \\u0633\\u062f\\u0647\\u0654 \\u0646\\u0648\\u0632\\u062f\\u0647\\u0645 \\u0645\\u0633\\u062a\\u0642\\u06cc\\u0645\\u0627\\u064b \\u062f\\u0631 \\u0632\\u0628\\u0627\\u0646 \\u0639\\u0644\\u0645\\u06cc \\u0648\\u0627\\u0645 \\u06af\\u0631\\u0641\\u062a\\u0647 \\u0634\\u062f\\u0647\\u061b \\u0648\\u0627\\u0645\\u200c\\u06af\\u06cc\\u0631\\u06cc \\u06a9\\u062a\\u0627\\u0628\\u06cc \\u0627\\u0633\\u062a \\u0646\\u0647 \\u0645\\u06cc\\u0631\\u0627\\u062b\\u06cc. xeroderma \\u0631\\u0627 \\u067e\\u0632\\u0634\\u06a9 \\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc \\u0627\\u0631\\u0627\\u0633\\u0645\\u0648\\u0633 \\u0648\\u06cc\\u0644\\u0633\\u0648\\u0646 \\u0627\\u0632 xero- \\u0648 \\u03b4\\u03ad\\u03c1\\u03bc\\u03b1 \\u00ab\\u067e\\u0648\\u0633\\u062a\\u00bb \\u0633\\u0627\\u062e\\u062a\\u0647 \\u0627\\u0633\\u062a. \\u0645\\u0639\\u0646\\u0627\\u06cc\\u06cc \\u06a9\\u0647 \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u0622\\u0648\\u0631\\u062f\\u0647 \\u0639\\u06cc\\u0646\\u0627\\u064b \\u062a\\u0639\\u0631\\u06cc\\u0641 \\u06a9\\u0644\\u0627\\u06cc\\u0646 \\u0627\\u0633\\u062a\\u061b \\u0627\\u062f\\u0639\\u0627 \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a.\",\n  \"sources\":[E+\"xero-\"],\n  \"ref_check\":[\n    {\"ref\":\"KLN:1757\",\"status\":\"supports\",\n     \"note\":\"The local 1966 two-volume OCR breaks off in 'ver-' (last leaf 902), so p.1757 itself cannot be paged; the same entries were read in the 1971 one-volume edition (KLN_1971.txt line 269073 ff.): 'xero-, before a vowel xer-, combining form meaning \\u201edry\\u2018. \\u2014 Gk. \\u03be\\u03b7\\u03c1\\u03bf-, \\u03be\\u03b7\\u03c1-, fr. \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 \\u201edry\\u2018 ... prob. cogn. with L. serenus (for *kseres-nos) ... See serene and cp. elixir' and 'xeroderma, n., roughening of the skin (med.) \\u2014 Medical L., coined by Erasmus Wilson fr. xero- and Gk. \\u03b4\\u03ad\\u03c1\\u03bc\\u03b1, \\u201eskin\\u2018.' The gloss 'roughness of the skin' in the chart is Klein's, and the alphabetical position (x-) is consistent with p.1757 of the 1966 edition.\"}\n  ],\n  \"consulted\":[\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. ksero-\",\"stance\":\"supports\",\"note\":\"'... in Greek x\\u0113ros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHALMIA.'\"},\n    {\"src\":\"FSD\",\"where\":\"Funk & Wagnalls vol.4 (FSD_vol4.txt, grep 'xeroderma')\",\"stance\":\"silent\",\"note\":\"no hit in this OCR volume.\"}\n  ]},\n\n {\"id\":7,\"lang\":\"Latin\",\"words\":\"serenus\",\n  \"verdict\":\"plausible\",\n  \"derivation\":\"Latin ser\\u0113nus 'clear, fair, cloudless, calm' (of sky and weather; hence figuratively 'cheerful, tranquil') is formed like terrenus, egenus from an older neuter s-stem *seres-, so *kseres-no-, with the regular Latin loss of initial ks- > s- (cp. serescere 'to dry' in Lucilius). Pokorny p.625 puts it under ks\\u0113-ro-, and Watkins repeats this \\u2014 but with 'Perhaps', and Klein s.v. serene says the word is 'of uncertain origin. It possibly stands for *kseresnos'. Ernout\\u2013Meillet accept the formation but reject certainty: 'Le sens de \\u201esec\\u2018 sugg\\u00e8re un rapprochement avec gr. \\u03be\\u03b7\\u03c1\\u03cc\\u03c2 ... Mais tout ce groupe est obscur et mal d\\u00e9fini ... En somme, rien de clair', pointing out that Greek \\u03be\\u03b5\\u03c1\\u03cc\\u03c2 is used only of dry land. Skeat's Concise Dictionary offers an altogether different comparison (\\u03c3\\u03ad\\u03bb\\u03b1\\u03c2 'brightness', \\u03c3\\u03b5\\u03bb\\u03ae\\u03bd\\u03b7 'moon'). The chart's arrow is therefore the majority modern view but not a secure one.\",\n  \"derivation_fa\":\"\\u0644\\u0627\\u062a\\u06cc\\u0646\\u06cc ser\\u0113nus \\u00ab\\u0635\\u0627\\u0641\\u060c \\u0631\\u0648\\u0634\\u0646\\u060c \\u0628\\u06cc\\u200c\\u0627\\u0628\\u0631 (\\u062f\\u0631\\u0628\\u0627\\u0631\\u0647\\u0654 \\u0622\\u0633\\u0645\\u0627\\u0646)\\u00bb \\u0645\\u0627\\u0646\\u0646\\u062f terrenus \\u0648 egenus \\u0627\\u0632 \\u0633\\u062a\\u0627\\u06a9\\u06cc \\u062e\\u0646\\u062b\\u0627 \\u0628\\u0627 \\u067e\\u0633\\u0648\\u0646\\u062f -no- \\u0633\\u0627\\u062e\\u062a\\u0647 \\u0634\\u062f\\u0647\\u060c \\u06cc\\u0639\\u0646\\u06cc *kseres-no-\\u060c \\u0628\\u0627 \\u062a\\u0628\\u062f\\u06cc\\u0644 \\u0642\\u0627\\u0639\\u062f\\u0647\\u200c\\u0645\\u0646\\u062f \\u0622\\u063a\\u0627\\u0632\\u06cc\\u0646 ks- \\u0628\\u0647 s- \\u062f\\u0631 \\u0644\\u0627\\u062a\\u06cc\\u0646\\u06cc (\\u0642\\u06cc\\u0627\\u0633 \\u06a9\\u0646\\u06cc\\u062f \\u0628\\u0627 serescere \\u00ab\\u062e\\u0634\\u06a9 \\u0634\\u062f\\u0646\\u00bb). \\u067e\\u0648\\u06a9\\u0648\\u0631\\u0646\\u06cc \\u0648 \\u0648\\u0627\\u062a\\u06a9\\u06cc\\u0646\\u0632 \\u0622\\u0646 \\u0631\\u0627 \\u0632\\u06cc\\u0631 \\u0647\\u0645\\u06cc\\u0646 \\u0631\\u06cc\\u0634\\u0647 \\u0622\\u0648\\u0631\\u062f\\u0647\\u200c\\u0627\\u0646\\u062f \\u0648\\u0644\\u06cc \\u0628\\u0627 \\u0642\\u06cc\\u062f \\u00ab\\u0634\\u0627\\u06cc\\u062f\\u00bb\\u061b \\u06a9\\u0644\\u0627\\u06cc\\u0646 \\u0645\\u06cc\\u200c\\u06af\\u0648\\u06cc\\u062f \\u0627\\u0635\\u0644 \\u0622\\u0646 \\u0646\\u0627\\u0645\\u0639\\u0644\\u0648\\u0645 \\u0627\\u0633\\u062a \\u0648 \\u0627\\u0631\\u0646\\u0648\\u2013\\u0645\\u0647\\u200c\\u06cc\\u0647 \\u0635\\u0631\\u06cc\\u062d\\u0627\\u064b \\u0645\\u06cc\\u200c\\u0646\\u0648\\u06cc\\u0633\\u0646\\u062f \\u00ab\\u0647\\u06cc\\u0686 \\u0686\\u06cc\\u0632 \\u0631\\u0648\\u0634\\u0646\\u06cc \\u062f\\u0631 \\u06a9\\u0627\\u0631 \\u0646\\u06cc\\u0633\\u062a\\u00bb. \\u067e\\u0633 \\u0627\\u06cc\\u0646 \\u067e\\u06cc\\u0648\\u0646\\u062f \\u0628\\u0627 \\u0627\\u062d\\u062a\\u06cc\\u0627\\u0637 \\u067e\\u0630\\u06cc\\u0631\\u0641\\u062a\\u0646\\u06cc \\u0627\\u0633\\u062a.\",\n  \"sources\":[E+\"serene\"],\n  \"ref_check\":[\n    {\"ref\":\"KLN:1422\",\"status\":\"supports\",\n     \"note\":\"Klein 1966, the leaf whose printed page number is 1422 (KLN_1966.txt leaf 755): 'serene, adj., clear, bright; calm. \\u2014 L. serenus, \\u201eclear, fair, cloudless, serene\\u2018, of uncertain origin. It possibly stands for *kseresnos and is cogn. with Gk. \\u03be\\u03b7\\u03c1\\u03cc\\u03c2, \\u201edry\\u2018, OI. k\\u1e63\\u0101r\\u00e1\\u1e25 ... OHG. serawen, \\u201eto become dry\\u2018. Cp. elixir, xerasia, xero-.' Nourai's page number is exact; note Klein's hedge 'of uncertain origin ... possibly'.\"}\n  ],\n  \"consulted\":[\n    {\"src\":\"POK\",\"where\":\"Pokorny 625 (POK_02.txt leaf 286)\",\"stance\":\"supports\",\"note\":\"'lat. serescunt (Lucil. I 306) \\u201e(die Kleider) trocknen (in der Sonne)\\u2018, serenus \\u201eheiter, hell, klar, trocken\\u2018 (vom Himmel und Wetter)'.\"},\n    {\"src\":\"LAT\",\"where\":\"Ernout\\u2013Meillet s.v. ser\\u0113nus (LAT.txt lines 57514-57534)\",\"stance\":\"partial\",\n     \"note\":\"'Serenus est form\\u00e9 comme terrenus, egenus, d'un ancien *seres-no-s ... Le sens de \\u201esec\\u2018 sugg\\u00e8re un rapprochement avec gr. \\u03be\\u03b7\\u03c1\\u03cc\\u03c2, \\u03be\\u03b5\\u03c1\\u03cc\\u03c2 \\u201esec\\u2018 et avec v.h.a. serawen \\u201es\\u00e9cher\\u2018 ... Mais tout ce groupe est obscur et mal d\\u00e9fini, pour le sens comme pour la forme ... En somme, rien de clair.'\"},\n    {\"src\":\"SKT\",\"where\":\"Skeat, Concise s.v. Serene (SKT.txt line 16928)\",\"stance\":\"contradicts\",\n     \"note\":\"'Serene. (F. \\u2014 L.) L. ser\\u0113nus, bright, clear. Allied to Gk. \\u03c3\\u03ad\\u03bb\\u03b1\\u03c2, brightness, \\u03c3\\u03b5\\u03bb\\u03ae\\u03bd\\u03b7 moon, \\u221aSWAR.' \\u2014 Skeat attaches serenus to the 'shine' root, not to *ksero-.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. ksero-\",\"stance\":\"partial\",\"note\":\"'2. Perhaps suffixed variant form *kseres-no- in Latin ser\\u0113nus, serene, bright, clear: SERENE.' \\u2014 supports, but hedged.\"}\n  ]},\n\n {\"id\":8,\"lang\":\"English\",\"words\":\"serene, serenity\",\n  \"verdict\":\"confirmed\",\n  \"derivation\":\"English serene (mid-15c., first of a day or of weather, 'clear, fair, calm', only from the 1630s of persons) comes from Old French serein and directly from Latin ser\\u0113nus; serenity is Middle French serenit\\u00e9, Old French serenite, from Latin serenit\\u0101tem (acc. of serenitas 'clearness'), with the learned suffix -ity. Both are straightforward Latin-through-French borrowings of the Renaissance layer, with no sound change worth naming beyond the French loss of the Latin ending.\",\n  \"derivation_fa\":\"\\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc serene \\u0627\\u0632 \\u0645\\u06cc\\u0627\\u0646\\u0647\\u0654 \\u0633\\u062f\\u0647\\u0654 \\u067e\\u0627\\u0646\\u0632\\u062f\\u0647\\u0645 \\u0645\\u06cc\\u0644\\u0627\\u062f\\u06cc \\u0646\\u062e\\u0633\\u062a \\u062f\\u0631\\u0628\\u0627\\u0631\\u0647\\u0654 \\u0631\\u0648\\u0632 \\u0648 \\u0647\\u0648\\u0627 \\u0628\\u0647 \\u0645\\u0639\\u0646\\u06cc \\u00ab\\u0635\\u0627\\u0641 \\u0648 \\u0622\\u0631\\u0627\\u0645\\u00bb \\u0628\\u0647 \\u06a9\\u0627\\u0631 \\u0631\\u0641\\u062a\\u0647 \\u0648 \\u0627\\u0632 \\u062f\\u0647\\u0647\\u0654 \\u06f1\\u06f6\\u06f3\\u06f0 \\u062f\\u0631\\u0628\\u0627\\u0631\\u0647\\u0654 \\u0627\\u0634\\u062e\\u0627\\u0635\\u061b \\u0627\\u0632 \\u0641\\u0631\\u0627\\u0646\\u0633\\u0648\\u06cc \\u06a9\\u0647\\u0646 serein \\u0648 \\u0645\\u0633\\u062a\\u0642\\u06cc\\u0645\\u0627\\u064b \\u0627\\u0632 \\u0644\\u0627\\u062a\\u06cc\\u0646\\u06cc serenus \\u06af\\u0631\\u0641\\u062a\\u0647 \\u0634\\u062f\\u0647 \\u0627\\u0633\\u062a. serenity \\u0627\\u0632 \\u0641\\u0631\\u0627\\u0646\\u0633\\u0648\\u06cc \\u0645\\u06cc\\u0627\\u0646\\u0647 serenit\\u00e9 \\u0648 \\u0622\\u0646 \\u0627\\u0632 \\u0644\\u0627\\u062a\\u06cc\\u0646\\u06cc serenit\\u0101tem \\u0627\\u0633\\u062a. \\u0627\\u062f\\u0639\\u0627\\u06cc \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a.\",\n  \"sources\":[E+\"serene\"],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference in the book; the claim was checked against Klein p.1422 and Etymonline instead (see consulted).\"}],\n  \"consulted\":[\n    {\"src\":\"KLN\",\"where\":\"Klein 1966 p.1422 (leaf 755)\",\"stance\":\"supports\",\n     \"note\":\"'serenity, n. \\u2014 MF. (= F.) serenite, fr. OF. serenite, fr. L. serenitatem, acc. of serenitas, \\u201eclearness, serenity\\u2018, fr. serenus. See serene and -ity.'\"},\n    {\"src\":\"FSD\",\"where\":\"Funk & Wagnalls vol.4, s.v. serenade/serene (FSD_vol4.txt line 7311 ff.)\",\"stance\":\"supports\",\n     \"note\":\"'< seren, serene, < L serenus, serene' in the entry immediately adjoining.\"}\n  ]},\n\n {\"id\":9,\"lang\":\"French\",\"words\":\"serenade\",\n  \"verdict\":\"plausible\",\n  \"derivation\":\"French s\\u00e9r\\u00e9nade is attested from the 16th c., but it is not formed in French from Latin ser\\u0113nus: it is a borrowing of Italian serenata, literally 'calm (sky)', from sereno < Latin serenus, and the 'at night' component of the meaning \\u2014 which Nourai puts in the gloss \\u2014 comes from a secondary contamination in Italian with sera 'evening' (Latin sera, fem. of serus 'late'), as Klein, Funk & Wagnalls and Etymonline all state. So the Latin > French arrow skips the Italian stage that carries the whole semantic development, and the gloss 'music played at night' belongs to the sera-influenced Italian word rather than to anything in *ksero- 'dry'.\",\n  \"derivation_fa\":\"\\u0641\\u0631\\u0627\\u0646\\u0633\\u0648\\u06cc s\\u00e9r\\u00e9nade \\u0627\\u0632 \\u0633\\u062f\\u0647\\u0654 \\u0634\\u0627\\u0646\\u0632\\u062f\\u0647\\u0645 \\u062f\\u06cc\\u062f\\u0647 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f \\u0648\\u0644\\u06cc \\u062f\\u0631 \\u062e\\u0648\\u062f \\u0641\\u0631\\u0627\\u0646\\u0633\\u0647 \\u0627\\u0632 serenus \\u0633\\u0627\\u062e\\u062a\\u0647 \\u0646\\u0634\\u062f\\u0647 \\u0627\\u0633\\u062a\\u061b \\u0648\\u0627\\u0645\\u200c\\u0648\\u0627\\u0698\\u0647\\u200c\\u0627\\u06cc \\u0627\\u0633\\u062a \\u0627\\u0632 \\u0627\\u06cc\\u062a\\u0627\\u0644\\u06cc\\u0627\\u06cc\\u06cc serenata \\u00ab(\\u0622\\u0633\\u0645\\u0627\\u0646\\u0650) \\u0635\\u0627\\u0641\\u00bb \\u0627\\u0632 sereno. \\u0645\\u0639\\u0646\\u06cc \\u00ab\\u0646\\u0648\\u0627\\u06cc \\u0634\\u0628\\u0627\\u0646\\u0647\\u00bb \\u06a9\\u0647 \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u0622\\u0648\\u0631\\u062f\\u0647 \\u062d\\u0627\\u0635\\u0644 \\u0622\\u0645\\u06cc\\u062e\\u062a\\u06af\\u06cc \\u062b\\u0627\\u0646\\u0648\\u06cc\\u0647 \\u0628\\u0627 sera \\u00ab\\u0634\\u0628\\u060c \\u0634\\u0627\\u0645\\u06af\\u0627\\u0647\\u00bb (\\u0627\\u0632 \\u0644\\u0627\\u062a\\u06cc\\u0646\\u06cc serus \\u00ab\\u062f\\u06cc\\u0631\\u00bb) \\u062f\\u0631 \\u0627\\u06cc\\u062a\\u0627\\u0644\\u06cc\\u0627\\u06cc\\u06cc \\u0627\\u0633\\u062a \\u2014 \\u06a9\\u0644\\u0627\\u06cc\\u0646\\u060c \\u0641\\u0627\\u0646\\u06a9 \\u0648 \\u0648\\u06cc\\u06af\\u0646\\u0627\\u0644\\u0632 \\u0648 \\u0627\\u062a\\u06cc\\u0645\\u0648\\u0622\\u0646\\u200c\\u0644\\u0627\\u06cc\\u0646 \\u0647\\u0631 \\u0633\\u0647 \\u0647\\u0645\\u06cc\\u0646 \\u0631\\u0627 \\u0645\\u06cc\\u200c\\u06af\\u0648\\u06cc\\u0646\\u062f. \\u067e\\u0633 \\u067e\\u06cc\\u06a9\\u0627\\u0646 \\u0645\\u0633\\u062a\\u0642\\u06cc\\u0645 \\u0644\\u0627\\u062a\\u06cc\\u0646\\u06cc \\u2190 \\u0641\\u0631\\u0627\\u0646\\u0633\\u0648\\u06cc \\u062d\\u0644\\u0642\\u0647\\u0654 \\u0627\\u06cc\\u062a\\u0627\\u0644\\u06cc\\u0627\\u06cc\\u06cc \\u0631\\u0627 \\u0646\\u0627\\u062f\\u06cc\\u062f\\u0647 \\u06af\\u0631\\u0641\\u062a\\u0647 \\u0627\\u0633\\u062a.\",\n  \"sources\":[E+\"serenade\"],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference in the book for this box; checked against Klein p.1422, Funk & Wagnalls and Etymonline (see consulted).\"}],\n  \"consulted\":[\n    {\"src\":\"KLN\",\"where\":\"Klein 1966 p.1422 (leaf 755)\",\"stance\":\"partial\",\n     \"note\":\"'serenade, n. \\u2014 F. s\\u00e9r\\u00e9nade, fr. It. serenata, lit. \\u201ecalm sky\\u2018, fr. sereno, \\u201eserene, calm\\u2018, fr. L. serenus. See serene and -ade. It. serenata was influenced in meaning by the noun sera, ... \\u201eplayed at night\\u2018' \\u2014 i.e. Italian, not French, is the immediate source, and the 'night' sense is secondary.\"},\n    {\"src\":\"FSD\",\"where\":\"Funk & Wagnalls vol.4 s.v. serenade (FSD_vol4.txt line 7311)\",\"stance\":\"partial\",\n     \"note\":\"'serenade: opposed to aubade [Pr., < seren, serene, < L serenus, serene, as if < serus late]' \\u2014 the same double etymology (serenus with contamination by serus).\"}\n  ]},\n\n {\"id\":10,\"lang\":\"English\",\"words\":\"serenade\",\n  \"verdict\":\"confirmed\",\n  \"derivation\":\"English serenade is first recorded in the 1640s as 'a musical performance at night in the open air', especially one given by a lover under his lady's window, borrowed from French s\\u00e9r\\u00e9nade; the verb follows in the 1660s and the sense 'instrumental piece in the style of a serenade' in 1728. The French > English step, which is all the chart claims here, is uncontroversial.\",\n  \"derivation_fa\":\"\\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc serenade \\u0646\\u062e\\u0633\\u062a \\u062f\\u0631 \\u062f\\u0647\\u0647\\u0654 \\u06f1\\u06f6\\u06f4\\u06f0 \\u0628\\u0647 \\u0645\\u0639\\u0646\\u06cc \\u00ab\\u0646\\u0648\\u0627\\u06cc \\u0634\\u0628\\u0627\\u0646\\u0647 \\u062f\\u0631 \\u0647\\u0648\\u0627\\u06cc \\u0622\\u0632\\u0627\\u062f\\u060c \\u0628\\u0647\\u200c\\u0648\\u06cc\\u0698\\u0647 \\u0632\\u06cc\\u0631 \\u067e\\u0646\\u062c\\u0631\\u0647\\u0654 \\u06cc\\u0627\\u0631\\u00bb \\u062f\\u06cc\\u062f\\u0647 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f \\u0648 \\u0648\\u0627\\u0645\\u200c\\u0648\\u0627\\u0698\\u0647\\u200c\\u0627\\u06cc \\u0627\\u0633\\u062a \\u0627\\u0632 \\u0641\\u0631\\u0627\\u0646\\u0633\\u0648\\u06cc s\\u00e9r\\u00e9nade\\u061b \\u0641\\u0639\\u0644 \\u0622\\u0646 \\u0627\\u0632 \\u062f\\u0647\\u0647\\u0654 \\u06f1\\u06f6\\u06f6\\u06f0 \\u0648 \\u0645\\u0639\\u0646\\u06cc \\u0645\\u0648\\u0633\\u06cc\\u0642\\u0627\\u06cc\\u06cc \\u0622\\u0646 \\u0627\\u0632 \\u06f1\\u06f7\\u06f2\\u06f8 \\u0627\\u0633\\u062a. \\u0647\\u0645\\u06cc\\u0646 \\u067e\\u06cc\\u06a9\\u0627\\u0646 \\u0641\\u0631\\u0627\\u0646\\u0633\\u0648\\u06cc \\u2190 \\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc \\u06a9\\u0647 \\u0646\\u0645\\u0648\\u062f\\u0627\\u0631 \\u0645\\u06cc\\u200c\\u06a9\\u0634\\u062f \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a.\",\n  \"sources\":[E+\"serenade\"],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference in the book; checked against Klein p.1422 and Etymonline.\"}],\n  \"consulted\":[\n    {\"src\":\"KLN\",\"where\":\"Klein 1966 p.1422 (leaf 755)\",\"stance\":\"supports\",\"note\":\"'serenata, n., serenade. \\u2014 It., whence F. s\\u00e9r\\u00e9nade. See serenade.' with 'Derivatives: serenade, tr. and intr. v., serenad-er, n.'\"},\n    {\"src\":\"FSD\",\"where\":\"Funk & Wagnalls vol.4 (line 7313)\",\"stance\":\"supports\",\"note\":\"'ser\\u2033e-nade\\u2032, n. 1. An evening song, specif., a song sung in the open air at night, also, the music of such ...'\"}\n  ]}\n]\n\njson.dump(e0, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e0.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(e0[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk280.py"
}
```


### [2026-09-06T21:50:37.254Z] TOOL RESULT

```
ok 10
```


## [2026-09-06T21:54:00.539Z] TOOL CALL #77: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk280b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW = \"https://en.wiktionary.org/wiki/\"\n\ne1 = {\n \"entry\": 1,\n \"root\": \"Kseubh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *k(ʷ)seubʰ- 'to sway, rock, tremble' (LIV 372; Pok. 625 kseubh-)\",\n \"note\": \"Pokorny p.625 has the headword 'kseubh- „schwanken, in schwingender Bewegung sein‘' and cites under it precisely the Iranian material of this chart: 'av. xšaob- „in Aufregung geraten‘ (xšufsqṅ), npers. ā-šuftan, ā-šōftan „in Bewegung versetzen‘, ā-šōb „Verwirrung, Tumult‘'. Nourai's gloss 'to shake, rock, disturb' is an accurate rendering of Pokorny's German. The root is still current in this shape: Cheung 2007 (s.v. *xšaub) reconstructs 'PIE *kʷseubʰ- „to rock, tremble‘ = LIV: 372 | Pok.: 625', and Wiktionary derives آشفتن from Proto-Iranian *xšawb- < PIE *k⁹sewbʰ-. Watkins/AHD has no entry for this root (it left no English reflex), which is a gap rather than a disagreement.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *k(ʷ)seubʰ- به معنی «جنبیدن، لرزیدن، در جنبش بودن» است. پوکورنی در ص ۶۲۵ همین سرواژه را آورده و زیر آن اوستایی xšaob- و فارسی «آشفتن، آشوفتن، آشوب» را نقل کرده است؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. چونگ (۲۰۰۷) نیز همین ریشه را با ارجاع به LIV ۳۷۲ و پوکورنی ۶۲۵ تأیید می‌کند. در پیوست واتکینز مدخلی برای این ریشه نیست، ولی این نبود مدخل است نه مخالفت.\",\n \"sources\": [W+\"آشفتن\", W+\"آشوب\"],\n \"ref_check\": [\n   {\"ref\": \"POK:625\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt leaf 286 (Pokorny p.625): 'kseubh- „schwanken, in schwingender Bewegung sein‘. Ai. kṣúbhyati, kṣóbhate ... av. xšaob- „in Aufregung geraten‘ (xšufsqṅ), npers. ā-šuftan, ā-šōftan „in Bewegung versetzen‘, ā-šōb „Verwirrung, Tumult‘ ... WP. I 502 f.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 502 f. s.v. qseubh- (WLD_Bd1_pages.txt leaf 511, printed p.502)\", \"stance\": \"supports\",\n    \"note\": \"'qseubh- „schwanken, in schwingender Bewegung sein“. Ai. kṣubhyati ... av. xšaob- „in Aufregung geraten“ (xšufsqṅ), np. ā-šuftan, ā-šōftan „in Bewegung versetzen“, gu-šuftan „zerstreuen“, ā-šōb „Verwirrung, Tumult“'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix (AHD_watkins1985.txt, grep 'kseubh')\", \"stance\": \"silent\",\n    \"note\": \"no entry: the appendix runs 'ksero- ... ksun ... ku- ... kus-', with no kseubh- between them, because the root has no English descendant.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *xšaub (CHEUNG.txt line 29360 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'*xšaub „to rustle, tremble‘ ... PIE *kʷseubʰ- „to rock, tremble‘ = LIV: 372 | Pok.: 625. IE COGNATES: Pol. chybać, Lith. skubti, Goth. af-skiuban, OE scufan, Engl. to shift.'\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka s.v. kṣautte (ISS_alt_DKS.txt line 1633)\", \"stance\": \"supports\",\n    \"note\": \"'From xšaub-:xšub- „to disturb‘, Av. xšaob-, xšufsan, M.Pers.T. wšwb-, ’šwb-; Zor.P. višōpišn, višuft; N.Pers. āšuftan, āšūftan, āšōb, gušuftan. IE Pok. 625 kseubh- „swing‘.'\"}\n ],\n \"nodes\": [\n  {\"id\":1,\"lang\":\"Avestan\",\"words\":\"xšaob, xšufsan; xšaub; â-xšuf-ta; â-xšaub-a\",\n   \"verdict\":\"plausible\",\n   \"derivation\":\"Only the first pair is genuinely Avestan. Bartholomae (Altiran. Wb., c. col. 542) has a single lemma: 'j. xšaob- V., nur Praes. 14 (Inkoh.) xšufsa- „in Aufregung geraten‘', with the one attested form xšufsqṅ (3pl. subj., Yt 10.113, of horses shying) — so xšaob- is the root, xšufsan the inchoative present, and Nourai's glosses ('disturbance' / 'to shake') are attached to them the wrong way round. 'xšaub' with -b is only the Indo-Iranian shape of the same root (Skt. kṣubh-), not a separate Avestan word. 'ā-xšuf-ta' and 'ā-xšaub-a' are unattested reconstructions: they come from Abolghasemi (FFD p.26), where they are expressly labelled 'ایرانی باستان' (Old Iranian), i.e. the preverb *ā- plus the ta-participle and the a-stem noun that underlie MP āšuft / āšōb. The derivations are right; the language label 'Avestan' is too strong for three of the four items.\",\n   \"derivation_fa\":\"از میان چهار صورت این خانه تنها دوتای نخست واقعاً اوستایی‌اند: بارتولومه تنها یک مدخل دارد، xšaob- با ستاک حال الانفعالی xšufsa- «به هیجان آمدن» که تنها صورت گواهی‌شده‌اش xšufsqṅ در یشت ۱۰ است؛ پس معناهایی که نورایی داده جابه‌جا شده‌اند. «xšaub» صورت هندوایرانی همان ریشه است (سنسکریت kṣubh-) نه واژه‌ای جداگانه، و دو صورت *ā-xšufta و *ā-xšauba بازساخته‌اند و از کتاب ابوالقاسمی (ص ۲۶) گرفته شده‌اند که آنجا صریحاً «ایرانی باستان» نامیده شده‌اند نه اوستایی. پس اشتقاق درست است ولی برچسب زبانی دقیق نیست.\",\n   \"sources\":[W+\"آشفتن\"],\n   \"ref_check\":[\n     {\"ref\":\"POK:625\",\"status\":\"supports\",\"note\":\"Pokorny 625: 'av. xšaob- „in Aufregung geraten‘ (xšufsqṅ)' — exactly the two Avestan items of the box, but only those two.\"},\n     {\"ref\":\"FFD:26\",\"status\":\"supports\",\n      \"note\":\"Abolghasemi, Fe'lhā-ye Fārsi-ye Dari p.26 (FFD_pages.txt pdf page 31): 'آشفتن، آشوفتن — آشفت < فارسی میانه ... < ایرانی باستان *ā-xšuf-ta ... ریشهٔ xšaub به معنی «لرزیدن» است. «آشوفت» زیر نفوذ «آشوب» به‌وجود آمده است. آشوب < فارسی میانه āšōb < ایرانی باستان *ā-xšaub-a' — this is plainly Nourai's source for the two prefixed forms, and it labels them Old Iranian, not Avestan.\"}\n   ],\n   \"consulted\":[\n     {\"src\":\"BRT\",\"where\":\"Bartholomae, Altiranisches Wörterbuch, s.v. xšaob- (BRT.txt line 10710, c. col. 542)\",\"stance\":\"partial\",\n      \"note\":\"'• j. xšaob- V., nur Praes. 14 (Inkoh.) xšufsa- „in Aufregung geraten‘, yat aspanqṁ sriša xšufsqṅ Yt.10.' — the only Avestan lemma of this root; no ā-xšufta, no ā-xšauba, no separate xšaub.\"},\n     {\"src\":\"CHEUNG\",\"where\":\"Cheung 2007 s.v. *xšaub (CHEUNG.txt line 29362)\",\"stance\":\"supports\",\n      \"note\":\"'AVESTAN: Y Av. *xšaob- (xšuf-) „to rustle, tremble‘ ... Pres. inch.: SUBJ. 3pl. YAv. xšufsan (Yt 10.113)' — and the *ā- prefixed forms he cites only from Middle Persian onwards.\"},\n     {\"src\":\"KNT\",\"where\":\"Kent, Old Persian (KNT.txt)\",\"stance\":\"silent\",\"note\":\"no Old Persian reflex of this root is recorded, so the Old Iranian forms of the box remain reconstructions.\"}\n   ]},\n\n  {\"id\":2,\"lang\":\"Pahlavi\",\"words\":\"âšŭp; âšŭptak\",\n   \"verdict\":\"confirmed\",\n   \"derivation\":\"Middle Persian āšōb (Book Pahlavi ’šwp, Manichaean ’’šwb) 'confusion, tumult, sedition' is *ā- + the o-grade noun *xšaub-a-, with the regular Middle Iranian development of initial xš- to š- and of *au to ō; āšuftag (Nourai's 'āšŭptak', spelled ’šwptk’) is the ta-participle *ā-xšuf-ta- plus the adjectival suffix -ag, 'disturbed'. Nyberg's Manual glosses 'āšōp [’šwp’] confusion, tumult, sedition' and derives 'āšuft-kārēh [’šwptk’lyh] subversion, upheaval ... from āšuftan āšōp-'; MacKenzie's Pahlavi dictionary has āšōb 'turmoil'. Parthian shows the same word (’’šwb 'turmoil', ’šwb-gr 'instigator to rebellion'), so the noun is Middle Iranian, not a New Persian back-formation.\",\n   \"derivation_fa\":\"فارسی میانهٔ āšōb (پهلوی کتابی ’šwp، مانوی ’’šwb) «آشفتگی، آشوب، شورش» از پیشوند *ā- و نامِ از ستاک مشددِ *xšaub-a- ساخته شده، با دو دگرگونی قاعده‌مند: xš- آغازین ایرانی باستان در فارسی میانه به ش بدل شده و دوواکهٔ au به ō بدل شده است. «āšuftag» (آشفته) صفت مفعولی *ā-xšufta- با پسوند -ag است. نیبرگ و مکنزی هر دو این صورت‌ها را ثبت کرده‌اند و پارتی نیز همین واژه را دارد؛ ادعای نورایی درست است.\",\n   \"sources\":[W+\"آشوب\"],\n   \"ref_check\":[\n     {\"ref\":\"ISS:11\",\"status\":\"not_checked\",\n      \"note\":\"Bailey, Indo-Scythian Studies: Khotanese Texts VI, is not available online (refs_online.json: 'Khotanese Texts VI itself is not online'), so p.11 could not be read. Bailey's own treatment of the same material is however in his Dictionary of Khotan Saka s.v. kṣautte (ISS_alt_DKS.txt line 1633), which lists 'Zor.P. višōpišn, višuft ... N.Pers. āšuftan, āšōb' under xšaub-, and Nyberg (below) cites 'Bailey, BSOS VI, 1930, 73' for āšuft-kārēh — i.e. Bailey did say what the arrow says.\"}\n   ],\n   \"consulted\":[\n     {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II (Glossary) s.vv. āšōp / āšuft-kārēh (NYB_vol2_glossary.txt lines 752, 757)\",\"stance\":\"supports\",\n      \"note\":\"'āšōp [’šwp’] confusion, tumult, sedition 38¹. 108¹. — MPrthPrs ’šwb, ’’šwb ... cf MPrth. ’’šwb-gr „instigator to rebellion‘' and 'āšuft-kārēh [’šwptk’lyh] subversion, upheaval 108¹. — From āšuftan āšōp-, v. āšōp and cf višuftan; MPrth ’šyft. Ghilain 95; Bailey, BSOS VI, 1930, 73.'\"},\n     {\"src\":\"PHD\",\"where\":\"MacKenzie, Concise Pahlavi Dictionary, English index (PHD.txt line 4095)\",\"stance\":\"supports\",\n      \"note\":\"'turmoil āšōb.' — MacKenzie's Pahlavi form for 'turmoil' is exactly Nourai's âšŭp.\"},\n     {\"src\":\"CHEUNG\",\"where\":\"Cheung 2007 s.v. *xšaub, Middle Persian section (CHEUNG.txt line 29366)\",\"stance\":\"supports\",\n      \"note\":\"'MIDDLE PERSIAN: (+ *a-) MMP ’’šwb, BMP ’šwp /āšob/ „turmoil, disturbance‘ || (+ *ui-) MMP w(y)swb-, BMP wswp- /wisōb-/ „to destroy, disturb‘ ... PARTHIAN: ’’šwb „turmoil‘'.\"},\n     {\"src\":\"HRN\",\"where\":\"Horn 1893 no.32, p.8 (HRN.txt leaf 30)\",\"stance\":\"supports\",\n      \"note\":\"'32. āšuften, āšōften „in Bewegung versetzen‘, Praes. āšōb-em ... aw. ā + xšufsqṅ; phlv. āšōftan (vd. 9.132, Gl.), āšōp (d.i. āšōw), āšōft-kārih (DK.); ai. √kṣubh-, kṣobhate.'\"}\n   ]},\n\n  {\"id\":3,\"lang\":\"Persian\",\"words\":\"âšŭb; âšoftan; kašoftan, kašaftan\",\n   \"verdict\":\"plausible\",\n   \"derivation\":\"آشوب āšūb 'disturbance, tumult' and آشفتن/آشوفتن āšuftan (pres. āšūb-) continue MP āšōb and āšuftan without further change beyond the New Persian shortening of ō > ū; Horn no.32, Cheung, Mo'in's footnote in Borhan-e Qāte‘ and Wiktionary all agree, and Abolghasemi adds the detail that the by-form آشوفت (with -ō-) arose 'under the influence of آشوب'. The third word is where the node becomes doubtful. Abolghasemi (FFD p.26) says explicitly '«کشفتن» هم از ریشهٔ xšaub آمده است', i.e. kašuftan is the same root with a different (fossilised *vi-/*wi- > k- ?) prefix; but Mo'in's own Farhang-e Fārsi lemmatises 'کشفتن [= شگفتن = شکافتن] (مص ع.) شکافتن، گشودن', attaching it to the 'split, burst open' family (شکافتن), and Dehkhoda gives both sets of senses ('گشودن، شکافتن' and 'پراکنده شدن، پریشان شدن، پژمرده شدن'). The Vīs-o-Rāmīn line Nourai quotes turns on the very contrast kašufta / šokufta, which is what makes the two etymologies hard to separate. Two of the three words are certain; the third is genuinely contested.\",\n   \"derivation_fa\":\"«آشوب» و «آشفتن/آشوفتن» (مضارع آشوب-) دنبالهٔ مستقیم فارسی میانهٔ āšōb و āšuftan اند، با همان تحول معمول واکهٔ ō به ū در فارسی نو؛ هرن، چونگ، حاشیهٔ معین بر برهان قاطع و ویکی‌واژه همه همین را می‌گویند و ابوالقاسمی می‌افزاید که صورت «آشوفت» زیر نفوذ «آشوب» پدید آمده است. اما دربارهٔ «کَشُفتن» اختلاف هست: ابوالقاسمی صریحاً آن را از همین ریشهٔ xšaub می‌داند، ولی خودِ معین در فرهنگ فارسی آن را برابر «شگفتن/شکافتن» می‌گیرد و دهخدا هر دو دسته معنا را ثبت کرده است. پس دو واژهٔ نخست قطعی و سومی محل بحث است.\",\n   \"sources\":[W+\"آشفتن\", W+\"آشوب\", \"https://abadis.ir/fatofa/کشفتن/\"],\n   \"ref_check\":[\n     {\"ref\":\"POK:625\",\"status\":\"supports\",\"note\":\"Pokorny 625 names the New Persian words themselves: 'npers. ā-šuftan, ā-šōftan „in Bewegung versetzen‘, ā-šōb „Verwirrung, Tumult‘'.\"},\n     {\"ref\":\"BQT:45\",\"status\":\"supports\",\n      \"note\":\"Borhan-e Qāte‘ vol.1 p.45 (BQT_v1_pages.txt leaf 255, the آش... page), Mo'in's etymological footnote: 'آشفتن — مرکب از پیشوند ā و xšaub اوستائی بمعنی مضطرب شدن، تحریک شدن، در سانسکریت [kṣubh] «بارتولمه ۵۶۲»' — precisely the arrow Nourai draws, with Bartholomae cited.\"},\n     {\"ref\":\"MON:2988\",\"status\":\"partial\",\n      \"note\":\"The 6-volume Amir Kabir pagination is not on disk; in the two-volume Mo'in the entry stands at MON_part2.txt line 23535, on the leaf whose running foot reads '۱۳۹۴ فرهنگ فارسی معین کشفتن': 'کشفتن: [= شگفتن = شکافتن] (مص ع.) شکافتن، گشودن' and 'کشفت: (ص.) پراکنده، پریشان'. The word and the sense Nourai wants are there, but Mo'in's own bracket refers it to شکافتن, not to xšaub — so the reference supports the word but not the derivation.\"},\n     {\"ref\":\"FFD:26\",\"status\":\"supports\",\n      \"note\":\"FFD p.26 (pdf page 31): 'آشوب < فارسی میانه āšōb < ایرانی باستان *ā-xšaub-a ... «کشفتن» هم از ریشهٔ xšaub آمده است' — all three of Nourai's Persian words, including kašuftan, from this root.\"}\n   ],\n   \"consulted\":[\n     {\"src\":\"HRN\",\"where\":\"Horn 1893 no.32, p.8 (HRN.txt leaf 30)\",\"stance\":\"supports\",\n      \"note\":\"'āšuften, āšōften „in Bewegung versetzen‘, Praes. āšōb-em ... aw. ā + xšufsqṅ; phlv. āšōftan ... ai. √kṣubh-'.\"},\n     {\"src\":\"CHEUNG\",\"where\":\"Cheung 2007 s.v. *xšaub, NWIR section (CHEUNG.txt line 29380 ff.)\",\"stance\":\"supports\",\n      \"note\":\"'(+ *a-) NP āsuftan/āsub- „to agitate, disturb‘, Kurd. (Kurm.) (h)ažōtin ... || (+ *ui-) NP *gušuftan (lit., lex.) „to scatter, fade‘' — note that Cheung's second Persian verb with a prefix is gušuftan, not kašuftan.\"},\n     {\"src\":\"MON\",\"where\":\"Farhang-e Fārsi s.v. کشفتن (MON_part2.txt line 23535)\",\"stance\":\"contradicts\",\n      \"note\":\"'کشفتن: [= شگفتن = شکافتن] (مص ع.) شکافتن، گشودن' — Mo'in refers kašuftan to the 'split/burst' family, not to xšaub.\"},\n     {\"src\":\"BQT\",\"where\":\"Dehkhoda's Loghatnāme s.v. کشفتن (via abadis.ir; the entry cites Borhan and Farhang-e Jahāngīri)\",\"stance\":\"partial\",\n      \"note\":\"'کشفتن. (مص) گشودن. شکافتن. (از فرهنگ جهانگیری) (از برهان) ... || پراکنده شدن. پریشان شدن ... || پژمرده شدن ... || نابود و معدوم شدن' with the Vīs-o-Rāmīn and Manuchehri citations — both senses coexist, which is why the etymology is contested.\"},\n     {\"src\":\"ARY\",\"where\":\"Aryanpur, Farhang-e Rishe-hā, entry آشوب / آشفتن / آشوفتن (incoming/ARY/ARY_pages.txt line 1850, pdf page 65)\",\"stance\":\"partial\",\n      \"note\":\"the headword 'آشوب آشفتن، آشوفتن' is there with Avestan, Pahlavi, Sanskrit, Old Slavic and Polish cognate columns and references to Borhan-e Qāte‘ and Dehkhoda, i.e. the same family as the chart; the Latin-script forms in this scan are too corrupt to quote.\"}\n   ]}\n ]\n}\njson.dump(e1, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e1.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(e1[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk280b.py"
}
```


### [2026-09-06T21:54:03.100Z] TOOL RESULT

```
ok 3
```


## [2026-09-06T21:56:09.445Z] TOOL CALL #78: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk280c.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW = \"https://en.wiktionary.org/wiki/\"\n\ne2 = {\n \"entry\": 2,\n \"root\": \"Kseud, Qseud\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Two roots: PIE *kseud- 'to pound small, crush' (Pok. 625) and Indo-Iranian *kšaud- 'liquid; to wash' (WP I 502 'qseud- „Flüssigkeit“, nur arisch'; Cheung *xšaud 'to wash')\",\n \"note\": \"Nourai's double headword 'Kseud, Qseud' is not a variant spelling: it reproduces two adjacent entries on the single page of Walde-Pokorny he cites (WP I 502), 'kseud- „klein stampfen“' and 'qseud- „Flüssigkeit“ (nur arisch)'. Pokorny's revision of 1959 keeps only kseud- 'klein stampfen' on p.625 and refers the Avestan 'liquid' words away to 'a 2. kseud-'. Nourai's composite gloss 'water, to clean by stamping in water' is his own fusion of the two — the 'water' half is qseud-, the 'stamping' half kseud- — and the fusion is also how the older literature explained Persian شستن (Fr. Müller derived it from Skt. kṣud 'to strike, pound', a derivation Hübschmann and Mo'in report with a caveat about the sense). Modern opinion is more cautious: Cheung (2007: 456) says 'The IE correspondences of the common Iranian root are unclear. The comparison to Slavic (OCS xudъ „small, bad“) by Pokorny is semantically difficult', preferring W. P. Schmidt's link to Lith. skudrus 'quick', skaudrus 'flowing quickly'. So the root box is a fair report of the two Walde-Pokorny entries, but the identification of the two roots with one another is not modern consensus.\",\n \"note_fa\": \"سرواژهٔ دوگانهٔ «Kseud, Qseud» دو صورت یک واژه نیست: نورایی دو مدخل پیاپیِ همان صفحه‌ای را که به آن ارجاع داده (والده-پوکورنی، جلد ۱، ص ۵۰۲) کنار هم گذاشته است — kseud- «خرد کوبیدن» و qseud- «مایع» (تنها آریایی). پوکورنی در ویراست ۱۹۵۹ تنها kseud- «خرد کوبیدن» را در ص ۶۲۵ نگه داشته و واژه‌های اوستایی «مایع» را به مدخل دیگری حواله داده است. معنای ترکیبی «آب؛ پاک کردن با کوبیدن در آب» ساختهٔ خود نورایی از این دو است، و ریشه‌شناسی کهن «شستن» (فریدریش مولر از سنسکریت kṣud «کوبیدن») هم بر همین آمیزش استوار بود؛ اما هوبشمان و معین همان‌جا هشدار داده‌اند که معنای فارسی «پاک کردن» است. پژوهش امروزی (چونگ ۲۰۰۷) پیوند هندواروپایی این ریشه را نامعلوم می‌داند. پس ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"شستن\"],\n \"ref_check\": [\n   {\"ref\": \"POK:625\", \"status\": \"partial\",\n    \"note\": \"POK_02.txt leaf 286 (p.625) has only one of the two: 'kseud- „klein stampfen‘. Ai. kṣódati „stampft, zermalmt‘, kṣóda- m. „Stoß, Stampfen, Zermalmen; Mehl, Pulver‘ ... WP. I 502.' The very last line of that entry is the cross-reference that shows the split: 'Verbindung von ai. kṣudrá- mit av. xšudra- „flüssig‘ (s. 2. kseud-) versucht Batakrishna Ghosh ... zu begründen.' So Pokorny p.625 does NOT give the gloss 'water' and does not merge the two roots.\"},\n   {\"ref\": \"WLD1:502\", \"status\": \"supports\",\n    \"note\": \"Walde-Pokorny I 502 (WLD_Bd1_pages.txt leaf 511, running head '502 qseu-, qsneu-, qneu-, sneu- — qseubh-') carries both roots on the one page: 'kseud- „klein stampfen“. Ai. kṣóduti „stampft, zermalmt“ ...' and immediately after 'qseud- „Flüssigkeit“ (nur arisch). Ai. kṣódas- n. „bewegtes Wasser, Flut, Wassermasse, Strom“ = av. xšaodah- n. „Fluß, Strömung, Wasserschwall“, xšudra-, xšūdra- „flüssig; n. Flüssigkeit“, xšusta- (*ksud-ta-) „flüssig, breiig, geschmolzen“, fra-xšuδra- n. „Vorwärtsfließen“.' This is exactly Nourai's 'Kseud, Qseud' and his gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny p.625 (POK_02.txt leaf 286)\", \"stance\": \"partial\",\n    \"note\": \"gives kseud- 'klein stampfen' only, and treats the Avestan 'liquid' group as a separate root.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 502 (leaf 511)\", \"stance\": \"supports\",\n    \"note\": \"both kseud- and qseud- on the cited page, with the Avestan material under the latter.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix (grep 'kseud')\", \"stance\": \"silent\",\n    \"note\": \"no entry — the root has no English reflex.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *xšaud, PIE section (CHEUNG.txt line 29440 ff.)\", \"stance\": \"partial\",\n    \"note\": \"'PIE: The IE correspondences of the common Iir. root are unclear. The comparison to Slavic (OCS xudъ „small, bad“, etc.), by Pokorny is semantically difficult. W. P. Schmidt (Gs Henning: 377 f.) suggests a connection with Lith. skudrus „quick“, skaudrus „flowing quickly“ ... = LIV: 372 | Pok.: 625.'\"}\n ],\n \"nodes\": [\n  {\"id\":1,\"lang\":\"Avestan\",\"words\":\"xšaod, xšaud; xšudra; xšâudra; xšvîd; svěstas\",\n   \"verdict\":\"transcription_suspect\",\n   \"error_in\":\"book\",\n   \"book_prints\":\"the Avestan box of the third chart on printed p.250 lists, one under the other: 'xšaod, xšaud : flow / xšudra : water, liquid, semen / xšâudra : male, husband / xšvîd : milk / svěstas : butter'\",\n   \"correct_form\":\"svěstas is Lithuanian svíestas 'butter', not an Avestan word (Walde-Pokorny I 502 quotes it as the Baltic comparison for Av. xšvīd-); and xšâudra- is not an attested Avestan lemma but Horn's reconstruction *xšaudra-/*xšaudraka- made to explain NP šōhar\",\n   \"derivation\":\"The extraction is faithful to the page (checked on the 300-dpi render, copied to data/verification/sources/refs/ocr/BOOK/280.png); the errors are the book's. Item by item: (1) xšaod-/xšaud- — Bartholomae has the noun xšaoδah- n. 'Fluß, Strömung, Wasserschwall' (Yt 10.14) and Cheung reconstructs OAv. *xšaod- 'to become liquid', so 'flow' is right. (2) xšudra-/xšuδra- — Bartholomae c. col. 555: '1) Adj. „flüssig“; 2) n. „Flüssigkeit“, a) alkoholische, „Wein“; b) „Samenflüssigkeit, semen virile“', so Nourai's 'water, liquid, semen' is an accurate summary. (3) xšâudra 'male, husband' — no such Avestan word exists; the form with long ā is Horn's reconstruction (Grundriss no.796, p.177: 'aw. *xšaudraka-, vergl. xšudra- „Same“, xšāudra-, np. šōi „Gatte“ ... setzen ein aw. *xšauda- voraus'), taken over by Mo'in in his Borhan footnote and by Nourai as if it were attested. (4) xšvīd- 'milk' is genuinely Avestan (Bartholomae: 'j., g. xšvīd- m. „Milch“'), but Walde-Pokorny expressly keep it OUT of this root: 'av. xšvīd „Milch“ zu lit. svíestas „Butter“, dessen Anlaut trotz Ch. nicht wohl aus ksv- herleitbar ist'. (5) svěstas 'butter' is precisely that Lithuanian svíestas, printed here as though it were Avestan — Nourai has copied Walde-Pokorny's comparandum into the wrong box.\",\n   \"derivation_fa\":\"استخراج با صفحهٔ چاپی مطابقت دارد (تصویر ۳۰۰ نقطه‌ای در data/verification/sources/refs/ocr/BOOK/280.png)، پس خطا از خود کتاب است. یک‌به‌یک: xšaoδah- «رود، جریان، خروش آب» در بارتولمه هست و چونگ ستاک *xšaod- «روان شدن» را بازمی‌سازد؛ xšudra-/xšuδra- در بارتولمه «مایع؛ مایع، شراب؛ نطفه» است، پس معنای نورایی درست است. اما «xšâudra» به معنی «مرد، شوهر» واژهٔ گواهی‌شدهٔ اوستایی نیست، بلکه بازساختهٔ هرن (بند ۷۹۶) است که برای توضیح «شوهر» فارسی ساخته شده و معین هم در حاشیهٔ برهان قاطع آن را نقل کرده است. xšvīd- «شیر» واقعاً اوستایی است ولی والده-پوکورنی آن را از این ریشه بیرون می‌گذارد. و «svěstas» اصلاً اوستایی نیست: لیتوانیایی svíestas «کره» است که در والده-پوکورنی تنها به عنوان هم‌سنجِ xšvīd آمده و نورایی آن را در خانهٔ اوستایی نشانده است — خطای چاپی و مفهومیِ خود کتاب.\",\n   \"sources\":[W+\"شستن\"],\n   \"ref_check\":[\n     {\"ref\":\"POK:625\",\"status\":\"partial\",\n      \"note\":\"Pokorny 625 s.v. kseud- mentions av. xšudra- 'flüssig' only in order to refer it elsewhere; the other four items of the box are not on that page at all.\"},\n     {\"ref\":\"WLD1:502\",\"status\":\"supports\",\n      \"note\":\"WP I 502 s.v. qseud- has three of the five: 'av. xšaodah- n. „Fluß, Strömung, Wasserschwall“, xšudra-, xšūdra- „flüssig; n. Flüssigkeit“, xšusta- (*ksud-ta-) ...'; and the same page has the sentence that exposes the last two: 'und av. xšvīd „Milch“ zu lit. svíestas „Butter“, dessen Anlaut trotz Ch. nicht wohl aus ksv- herleitbar ist' — svíestas is Lithuanian, and xšvīd is expressly excluded from qseud-.\"}\n   ],\n   \"consulted\":[\n     {\"src\":\"BRT\",\"where\":\"Bartholomae, Altiran. Wb., s.vv. xšaoδah-, xšudra-, xšusta-, xšvīd- (BRT.txt lines 10709, 10863, 10985; c. cols 542, 555, 561)\",\"stance\":\"partial\",\n      \"note\":\"'• j. xšaoδah- n. „Fluss, Strömung, Wasserschwall“ ... Yt 10.14'; '• j. xšudra-, xšuδra- 1) Adj. „flüssig“ ... 2) n. „Flüssigkeit“ ... b) „Samenflüssigkeit, semen virile“'; 'xšusta- Adj. „flüssig“ ... PPfP. einer Basis (ar.) *ksaud-, wozu noch xšaoδah-, xšudra-'; '• j., g. xšvīd- m. „Milch“'. No lemma xšāudra-, and of course no svěstas.\"},\n     {\"src\":\"CHEUNG\",\"where\":\"Cheung 2007 s.v. *xšaud, Avestan section (CHEUNG.txt line 29411 ff.)\",\"stance\":\"partial\",\n      \"note\":\"'AVESTAN: OAv. *xšaod- „to become liquid‘, YAv. xšaodah- (n.) „gush, flush of water‘ (Yt 10.14), YAv. xšuδra- (Yt 19.58), YAv. xšudra- „liquid, fluid‘ ... Partic.: perf. pass. YAv. xšusta- „melted, liquid (of metals)‘' — the same three words, and no 'husband' word and no milk/butter.\"},\n     {\"src\":\"KNT\",\"where\":\"Kent, Old Persian (KNT.txt)\",\"stance\":\"silent\",\"note\":\"no Old Persian form of this root.\"}\n   ]},\n\n  {\"id\":2,\"lang\":\"Persian\",\"words\":\"šostan; šǔy\",\n   \"verdict\":\"disputed\",\n   \"derivation\":\"The two Persian words the box joins are not one word. (a) شستن šostan 'to wash', pres. stem شوی šōy-, is beyond doubt from this root: MP šustan / šōy- (MacKenzie: 'šustan, šūy- [HLLWN-tn’] wash'), Parthian šw(w)d-, from Proto-Iranian *xšaud 'to wash' (Cheung 455-6), with initial xš- > š- and the past stem from *xšud-ta- (Abolghasemi's *xšud-ta, 'د پیش از t به s بدل شده'). Horn's no.782 on the very page Nourai cites (p.172) gives 'šusten „waschen“, Praes. šōy-em; phlv. šustan, šōyēnd, šōy(i)šn'. (b) شوی šūy 'husband' (with شوهر، شو، زناشویی) is a different word that merely fell together with the present stem of 'wash' in Middle Persian — MacKenzie lists them as two lemmas, 'šōy [šwd] husband' and 'šustan, šūy- wash'. Nourai follows Horn no.796 (p.177: 'šōher (*šōhr) „Gatte“. aw. *xšaudraka-, vergl. xšudra- „Same“ ... setzen ein aw. *xšauda- voraus'), i.e. 'husband' as 'the one with the seed', and Mo'in repeats it in his Borhan footnote. Modern Iranian etymology rejects this: the word goes back to Proto-Iranian *fšautar 'cattle-raiser, husbandman', to *fšau- 'to raise cattle' (PIE *peh₂- 'to protect, shepherd'), cf. Av. fšuiiaṇt- 'husbandman', Khotanese kṣondai 'husband', Yidgha šfuy, Baluchi šú — a source that yields Persian š- just as regularly as *xš- does. Cheung, who reconstructs *xšaud in full, does not list šōy 'husband' among its descendants at all.\",\n   \"derivation_fa\":\"این خانه دو واژهٔ جدا را یکی گرفته است. نخست «شستن» با ستاک حال «شوی-»: این یکی بی‌گمان از همین ریشه است — فارسی میانه šustan/šōy-، پارتی šw(w)d-، از ایرانی آغازین *xšaud «شستن» (چونگ ۴۵۵)، با تبدیل قاعده‌مند xš- آغازین به ش و ستاک گذشته از *xšud-ta که در آن د پیش از t به s بدل شده است؛ هرن در همان ص ۱۷۲ که نورایی ارجاع داده همین را آورده است. اما «شوی ۲» به معنی «شوهر» واژهٔ دیگری است که تنها در فارسی میانه با ستاک حالِ «شستن» هم‌آوا شده؛ مکنزی آن دو را دو مدخل جدا آورده است. نورایی از هرن (بند ۷۹۶) و معین پیروی کرده که «شوهر» را از *xšaudraka- (وابسته به xšudra «نطفه») می‌دانستند، اما ریشه‌شناسی امروزی این را رد می‌کند و «شوهر/شوی» را از ایرانی آغازین *fšautar «پرورندهٔ گله» (از *fšau-، هندواروپایی *peh₂- «پاسداری کردن») می‌گیرد، هم‌ریشه با اوستایی fšuiiaṇt- «گله‌دار»، ختنی kṣondai «شوهر» و بلوچی šú. پس نیمهٔ نخست ادعا درست و نیمهٔ دوم مردود است.\",\n   \"sources\":[W+\"شستن\", W+\"شوهر\", W+\"شوی\"],\n   \"ref_check\":[\n     {\"ref\":\"HRN:172,177\",\"status\":\"supports\",\n      \"note\":\"Both pages say what Nourai reports. Horn p.172 (HRN.txt leaf 194) no.782: 'šusten „waschen“, Praes. šōy-em; phlv. šustan, šōyēnd, šōy(i)šn; kurd. LW. šuštin ...'. Horn p.177 (leaf 199) no.796: 'šōher (*šōhr) „Gatte“. aw. *xšaudraka-, vergl. xšudra- „Same“, xšāudra-, np. šōi „Gatte“, phlv. šōi (vd. 15 (29) Gl.) setzen ein aw. *xšauda- voraus, das dieselbe Bedeutung wie *xšaudraka- hatte.' — this is the source of Nourai's 'xšâudra : male, husband' as well.\"},\n     {\"ref\":\"BQT:1267\",\"status\":\"supports\",\n      \"note\":\"Borhan-e Qāte‘ p.1267 = BQT_v3_pages.txt pdf page 58 (offset +1209), Mo'in's footnote: 'شستن — بضم اول و فتح سوم. پهلوی shustan، کردی shushtin (تطهیر)، بلوچی ... بقول Fr. Müller از سانسکریت kshud (زدن، خرد کردن). اما در فارسی به‌معنی تطهیر، پاک کردن (رخت آب زدن) آمده، قس: پازند shustan ... هویشمان ۷۸۲' — the Skt. kṣud connection Nourai's root box rests on, with Mo'in's own semantic caveat.\"},\n     {\"ref\":\"BQT:1312\",\"status\":\"supports\",\n      \"note\":\"Borhan-e Qāte‘ p.1312 = BQT_v3_pages.txt pdf page 103 (the next leaf carries the running head ۱۳۱۳), Mo'in's footnote: 'شوهر — بفتح اول و سوم؛ اوستا xshaudraka، ... xshudra (تخم، منی)، xshaudra ... «شوی» + هر ... در فارسی ساخته شده «هوبشمان»' — Mo'in reproduces Horn's derivation, exactly as Nourai charts it.\"},\n     {\"ref\":\"FFD:63\",\"status\":\"partial\",\n      \"note\":\"FFD p.63 (FFD_pages.txt pdf page 68): 'شست < فارسی میانه šust < ایرانی باستان *xšud-ta ... xšud صورت ضعیف ریشهٔ xšaud' and 'شوی < فارسی میانه šōy < ایرانی باستان *xšauda ... «شور» به جای «شوی» جدید است'. Abolghasemi's شوی here is the present stem of شستن 'wash' in a dictionary of verb stems, not the noun 'husband' — so the page supports the first Persian word only.\"}\n   ],\n   \"consulted\":[\n     {\"src\":\"CHEUNG\",\"where\":\"Cheung 2007 s.v. *xšaud (CHEUNG.txt lines 29410-29440)\",\"stance\":\"partial\",\n      \"note\":\"'MIDDLE PERSIAN: MMP šwy-, BMP šws- (HLLWN-) /šus-/ „to wash‘ ... Inf.: BMP šwstn /šustan/. PARTHIAN: šw(w)d- „to wash‘. NWIR: NP šustan/šōy-, Kurd. šuštin/šo- ...' — the wash-verb is fully covered; 'husband' is absent from the entry, and Cheung even rejects deriving the dialect present stems in -r- from šuhr 'sperm'.\"},\n     {\"src\":\"PHD\",\"where\":\"MacKenzie, Concise Pahlavi Dictionary pp.79-80 (PHD.txt lines 585, 589)\",\"stance\":\"contradicts\",\n      \"note\":\"two separate lemmas: 'šōy-, v. šustan. šōy [šwd | N ~] husband.' and 'šustan, šūy- [HLLWN-tn’ < A √ḥll | M šwst, šwy-, N ~] wash.' — MacKenzie does not connect the noun 'husband' with the verb 'wash'.\"},\n     {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien p.79 (note to Horn 782) and p.82 (HUB.txt lines 2795, 8311)\",\"stance\":\"partial\",\n      \"note\":\"'782. Nach Fr. Müller, WZKM. 8, 96 zu skr. kṣud „schlagen, stampfen“. Aber die Bedeutung von np. šustan ist „waschen = reinigen“, pākīza kardan ...' and, in the list of NP š- from OIr. xš-, 'šustan „waschen“ H. 782, oben p.79; šuhar „Gatte“ H. 796, oben p.82' — Hübschmann accepts both as xš- words but flags the semantic difficulty of the 'pound' etymology.\"},\n     {\"src\":\"MON\",\"where\":\"Farhang-e Fārsi / Dehkhoda s.v. شوی، شوهر\",\"stance\":\"partial\",\n      \"note\":\"Mo'in's Borhan footnote (BQT:1312, quoted above) gives the Horn derivation; the modern reference works no longer do.\"},\n     {\"src\":\"ARY\",\"where\":\"Aryanpur, Farhang-e Rishe-hā (incoming/ARY, grep 'شستن')\",\"stance\":\"silent\",\n      \"note\":\"no usable entry located in the OCR for شستن or شوهر.\"}\n   ]}\n ]\n}\njson.dump(e2, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e2.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(e2[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk280c.py"
}
```


### [2026-09-06T21:56:11.921Z] TOOL RESULT

```
ok 2
```


## [2026-09-06T21:56:16.029Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/'\nout={\"pdf_page\":280,\"book_page\":250,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-06\",\n     \"entries\":[json.load(open(S+f)) for f in ('e0.json','e1.json','e2.json')]}\njson.dump(out, open('data/verification/page-280.json','w'), ensure_ascii=False, indent=1)\nprint('written')\nEOF\npython3 -m json.tool data/verification/page-280.json > /dev/null && echo \"valid json\" && python3 tools/verify_check.py 280"
}
```


### [2026-09-06T21:56:19.766Z] TOOL RESULT

```
written
valid json
nodes verified: 15/15
node verdicts: {'plausible': 5, 'confirmed': 8, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 14, 'partial': 6, 'not_checked': 4}
books consulted: {'partial': 14, 'supports': 23, 'silent': 10, 'contradicts': 3} | by book: {'KLN': 6, 'CHEUNG': 5, 'FSD': 4, 'LKT': 3, 'MON': 3, 'ARY': 3, 'WEB': 2, 'BQT': 2, 'SKT': 2, 'AHD': 2, 'BRT': 2, 'KNT': 2, 'PHD': 2, 'HRN': 2, 'SYN': 1, 'WLD': 1, 'DEV': 1, 'FVQ': 1, 'AFM': 1, 'PHN': 1, 'POK': 1, 'LAT': 1, 'NYB': 1, 'HUB': 1}
```


## [2026-09-06T21:56:28.431Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\np='data/verification/page-280.json'\nd=json.load(open(p))\nn=0\ndef fix(o):\n    global n\n    if isinstance(o,dict):\n        if o.get('src')=='ISS_alt_DKS':\n            o['src']='ISS'; n+=1\n        for v in o.values(): fix(v)\n    elif isinstance(o,list):\n        for v in o: fix(v)\nfix(d)\njson.dump(d, open(p,'w'), ensure_ascii=False, indent=1)\nprint('fixed',n)\nEOF\npython3 tools/verify_check.py 280"
}
```


### [2026-09-06T21:56:30.771Z] TOOL RESULT

```
fixed 1
nodes verified: 15/15
node verdicts: {'plausible': 5, 'confirmed': 8, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 14, 'partial': 6, 'not_checked': 4}
books consulted: {'partial': 14, 'supports': 23, 'silent': 10, 'contradicts': 3} | by book: {'KLN': 6, 'CHEUNG': 5, 'FSD': 4, 'LKT': 3, 'MON': 3, 'ARY': 3, 'WEB': 2, 'BQT': 2, 'SKT': 2, 'AHD': 2, 'BRT': 2, 'KNT': 2, 'PHD': 2, 'HRN': 2, 'SYN': 1, 'WLD': 1, 'DEV': 1, 'FVQ': 1, 'AFM': 1, 'PHN': 1, 'POK': 1, 'LAT': 1, 'NYB': 1, 'HUB': 1}
```


## [2026-09-06T21:56:50.026Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-280.json` written; `verify_check.py 280` reports 15/15 nodes, 0 PROBLEM lines.

**Page 280 (book p.250) — 3 entries, 15 nodes**
- Roots: confirmed 2 (Ksero, Kseubh), plausible 1 (Kseud/Qseud)
- Nodes: confirmed 8, plausible 5, disputed 1, transcription_suspect 1
- Ref checks: supports 14, partial 6, not_checked 4 (ISS:11 — Bailey KT VI not online; the three unreferenced serene/serenade boxes)

**disputed**
- Kseud/Qseud, Persian شوی šūy "husband": Nourai follows Horn no.796 and Mo'in's Borhan footnote (Av. *xšaudraka-, xšudra "semen"); modern etymology derives شوهر/شوی from Proto-Iranian *fšautar "cattle-raiser" (*fšau-, PIE *peh₂-), cf. Av. fšuiiaṇt-, Khot. kṣondai. Cheung's *xšaud entry has no "husband" reflex; MacKenzie lists šōy "husband" and šustan/šūy- "wash" as separate lemmas. (شستن itself is confirmed.)

**transcription_suspect** (`error_in: "book"` — page render saved to `data/verification/sources/refs/ocr/BOOK/280.png`)
- Kseud/Qseud, Avestan box: "svěstas : butter" is Lithuanian svíestas, printed inside the Avestan box; Walde-Pokorny I 502 cites it only as the Baltic comparandum for Av. xšvīd- and explicitly keeps xšvīd out of this root. Also in the same box, "xšâudra : male, husband" is not an attested Avestan lemma but Horn's reconstruction.

**No extraction errors** — the JSON matches the printed page everywhere I checked (including the empty French box in entry 0 and the کَشُفتن script/extras).

Other notable but non-flagged findings: the Greek box merges ξηρός "dry" with its derivative ξηρίον "drying powder" (the actual etymon of al-iksīr; Arabic took it via Syriac ksīrīn); Latin serenus is only "perhaps" from this root (Watkins/Klein hedge, Ernout–Meillet "rien de clair", Skeat gives a different etymology); French sérénade is borrowed from Italian serenata with the "night" sense from contamination by sera, not from serenus directly; and کَشُفتن is contested — Abolghasemi (FFD:26) derives it from xšaub, while Mo'in's own Farhang equates it with شگفتن/شکافتن.
