# Verification process log — verify-page-448


## [2026-09-14T01:56:05.070Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 448 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-448.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-448.json. Write /home/sfmqrb/git/rishe/data/verification/page-448.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 448` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:06.493Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:56:07.361Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:07.384Z] TOOL RESULT

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


## [2026-09-14T01:56:07.860Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-448.txt"
}
```


### [2026-09-14T01:56:07.885Z] TOOL RESULT

```
1	=== PDF page 448 (book page 418) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Seu 2 : juice, to take liquid, squeeze  (refs POK:912)
4	#1 (parent #0) [Avestan] refs=POK:912; KNT:211 | hau 1 : to press, squeeze ; haoma : ephedra plant, mahuang shrub
5	  #2 (parent #1) [Persian] refs=HRN:249; BQT:2398 | howm «هوم» : a juicy plant which was considered very holy by the ancient Aryan people
6	#3 (parent #0) [Germanic] refs=AHD | sŭp : soup
7	  #4 (parent #3) [French] refs=AHD:1234 | soupe
8	    #5 (parent #4) [Persian] refs=MON:1944 | sŭp «سوپ» : soup
9	    #6 (parent #4) [English] refs=AHD:1234 | soup
10	#7 (parent #0) [Sanskrit] refs=KNT:211 | su : press
11	#8 (parent #0) [Germanic] refs=AHD | sŭk : suck ; suk : soak
12	  #9 (parent #8) [English] refs=AHD | suck, soak
13	--- entry 1 ---
14	ROOT [Indo-European] Seu 3, Sŭ 4, Sŭtus : to give birth  (refs POK:913)
15	#1 (parent #0) [Avestan] refs=POK:913; KLN:1473 | hav, hunâmi : to give birth ; hunuš : son
16	#2 (parent #0) [Germanic] refs=KLN:1473 | sunuz : son
17	  #3 (parent #2) [English] refs=None | son
18	--- entry 2 ---
19	ROOT [Indo-European] Seu 4, Sew : to boil  (refs POK:914)
20	#1 (parent #0) [Avestan] refs=POK:914; KLN:1411 | hâvayan : they boil, roast ; hâvayeiti : roasts
21	#2 (parent #0) [Germanic] refs=AHD; KLN:1411 | siuthan : to boil ; suth : swamp
22	  #3 (parent #2) [English] refs=AHD | seethe, sod
23	--- entry 3 ---
24	ROOT Sew -> redirect to Seu 4
25	
```


## [2026-09-14T01:56:10.600Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-448.json",
 "description": "Read page 448 source JSON"
}
```


### [2026-09-14T01:56:10.639Z] TOOL RESULT

```
{
  "pdf_page": 448,
  "book_page": 418,
  "entries": [
    {
      "root": {
        "name": "Seu 2",
        "lang": "Indo-European",
        "refs": "POK:912",
        "gloss": "juice, to take liquid, squeeze"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:912; KNT:211",
          "words": [
            {"translit": "hau 1", "gloss": "to press, squeeze", "script": null},
            {"translit": "haoma", "gloss": "ephedra plant, mahuang shrub", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:249; BQT:2398",
          "words": [
            {"translit": "howm", "gloss": "a juicy plant which was considered very holy by the ancient Aryan people", "script": "هوم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "sŭp", "gloss": "soup", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "AHD:1234",
          "words": [
            {"translit": "soupe", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1944",
          "words": [
            {"translit": "sŭp", "gloss": "soup", "script": "سوپ"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:1234",
          "words": [
            {"translit": "soup", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "KNT:211",
          "words": [
            {"translit": "su", "gloss": "press", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "sŭk", "gloss": "suck", "script": null},
            {"translit": "suk", "gloss": "soak", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "suck, soak", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Seu 3, Sŭ 4, Sŭtus",
        "lang": "Indo-European",
        "refs": "POK:913",
        "gloss": "to give birth"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:913; KLN:1473",
          "words": [
            {"translit": "hav, hunâmi", "gloss": "to give birth", "script": null},
            {"translit": "hunuš", "gloss": "son", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:1473",
          "words": [
            {"translit": "sunuz", "gloss": "son", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "son", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Seu 4, Sew",
        "lang": "Indo-European",
        "refs": "POK:914",
        "gloss": "to boil"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:914; KLN:1411",
          "words": [
            {"translit": "hâvayan", "gloss": "they boil, roast", "script": null},
            {"translit": "hâvayeiti", "gloss": "roasts", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD; KLN:1411",
          "words": [
            {"translit": "siuthan", "gloss": "to boil", "script": null},
            {"translit": "suth", "gloss": "swamp", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "seethe, sod", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sew",
        "redirect": "Seu 4"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:56:12.444Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','KLN','AHD','HRN','BQT','MON','WLD','IEC','SYN','BRT','PHD','NYB','HUB','ARY','CHEUNG','SKT','FSD','WEB']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-14T01:56:13.545Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
```


## [2026-09-14T01:56:47.594Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T01:56:47.647Z] TOOL RESULT

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


## [2026-09-14T01:56:48.277Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && ls data/verification/page-44*.json 2>/dev/null"
}
```


### [2026-09-14T01:56:48.331Z] TOOL RESULT

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
SKT_dli_revised.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
data/verification/page-44.json
```


## [2026-09-14T01:56:50.894Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"seu-\" POK_full.txt | sed -n 1,80p"
}
```


### [2026-09-14T01:56:50.979Z] TOOL RESULT

```
49389:An extension of the stem *Rasen- (: kas-n-o-) and *Raseu-, kasou- (: kas-u-o) with 
74187:Root /lemma: seu-1, se"&-: su- 
74203:The old laryngeal became a sibilant in satem languages : *heu- > seu-. 
74221:3. seu-d- in Old English i?e-5J//5/7 'smudge', westfal. 50/" filth '; Old Icelandic sut'care, 
74273:Root / lemma: seu-2, (seya-), su- 
74302:Root / lemma: seu-3 : su- : seya- : su- 
74321:sua(i)nemvc\. "rope, cord' {*seu-n-Ja-md)\ Lithuanian siauras{*seu-ro-) " narrow, tight, slim, 
74326:seu-k-: osset. xurx' whey ' (Aryan *si//r/'a-.' Lithuanian sukrus^*was sich leicht dreht'); 
74342:Root / lemma: seu-4, seu-t- 
77377:Root / lemma: skeu-3, kseu- 
78903:Old Indie sunSti^ squeezed, pressed ' = Avestan hunaoitioi Root/ lemma: seu-1, se^a-. 
83978:See also: compare also seu-an6 suef/J-'bend'. 
84592:originally " Gebarerin ', to seu-2. su- " to give birth to children ' (above S. 913 f.); compare
```


## [2026-09-14T01:56:51.860Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"haoma\\|hunu\\|hāvay\\|havay\" POK_full.txt | head -40"
}
```


### [2026-09-14T01:56:52.018Z] TOOL RESULT

```
13957:{*b^dud, vocalism as in Old Indie bhavayati, bhava-h, Slavic baviti). 
74284:Old Indie sunu-m.; Avestan hunu-s, Gothic sunus. Old Icelandic sunr. Old High German 
74346:Material: Avestan havayqn^sxe schmoren', /7ai/aye///"erschmort' (3. Sg. Opt. huyaras- 
80425:sphatf-t ' fattening, prospering; flourishing ', Kaus. sphavayati^masiei, verstarkt', sphara-
```


## [2026-09-14T01:56:53.706Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '74180,74380p' POK_full.txt"
}
```


### [2026-09-14T01:56:53.774Z] TOOL RESULT

```
influence of suchen' seek '); Old English sys/n. f. {*suh-sla-) " sorrow ', seoslig {* seuh-sla- 
) "gepeinigf. Old Icelandic sysl, sysla^ occupation, Amt, Amtsbezirk (from the through 
Pflichtarbeit ausgelosten Unlust)', sj?s/Adj. " eager bemijht, sorgsam' {*sOsli-R). 

References: WP. II 472 f. 
Page(s):915 

Root /lemma: seu-1, se"&-: su- 

Meaning: juice; liquid, *rain 

Material: 1 . Gr. usi " it is raining ', uw " allows to rain ' ( *su-id), u£t6(; "heavy rain' ( *suu- 

etos, as vT(P£t6(;); alb. s/7/"rain' {*su-)\ Tocharian B swese^ra\v\\ su-, sn/as- "rain'; to U£i 



perhaps uQKoq {uaQKoq, uaKoq Gramm.) m. "empty gossip' (as though " letting drip 

monotonously '); 

Note: 

The old laryngeal became a sibilant in satem languages : *heu- > seu-. 

Illyrian Savus {*Souos) displays satem characteristics : alb. s/7/^'rain'. 

2. Old Indie sunotT squeezes, presses ' = Avestan hunaoiti6s.\ Old Indie savana-m, 
sava- m. ' Kelterung des Soma ', suta- " pressed ', soma- = Avestan hauma- m. ' Soma '; 
Old High German sou. Old English seaw^\u\ce, sap', isl. 5C>g^/'"humid, wet' {*sawwia-)\ 
Old Irish s^//7 "juice, sap, milk' {*su-tu-s)\ here probably also FIN gall. Save, Savara, -ia 
and (Illyrian) Savus {*Souos). 

Note: 



Old Indie savana-m, sava-m. " Kelterung des Soma ' : Illyrian Savus prove the satem 
nature of lllyrian-alb. Proto Illyrian was probbaly the bridge between satem and centum 
languages. 

3. seu-d- in Old English i?e-5J//5/7 'smudge', westfal. 50/" filth '; Old Icelandic sut'care, 
sorrow', syta ' grieve '. 

4. Guttural extension: seuk-, suk- and seug-, sug-: 

Latin sugo, -ere^sucV!; Latin sJci/s "juice, sap', cymr. sugno. Middle Breton sunaff, 
nbret. suna6s., s^/7 'juice, sap', cymr. sugnedydd^ pump' {*seuk-n-, cymr. ^from Latin 
loanword s^^'juice, sap'), acymr. dissuncgnetic^ exhaust, suffer through, endure ' 
(morphologically difficult group); Old English sucan, Dutch zuiken^ sucV!; Old English 
socian {*sukdn) ' steep, absorb, suck', gesocu. 'the sucking'. Old Icelandic suga{sjuga) 
"suck', sogu. ' the sucking ', Old English Old Saxon Old High German sugan^suck', Kaus. 
Norwegian dial, soygja. Middle High German sougen^ suckle ', Middle High German sue, 
soc, g. 5c»^es and souc, -^es 'juice, sap'. Old English sogedam. 'gulp'; Latvian sukt' suck'; 
Old Prussian suget 'rain'. 

Maybe alb. shushunje leech, bloodsucker' : Latin sanguisuga [sangu/^b\ood + suga 
'sucker'] : Italian sanguisuga : Spanish sanguijuela; sanguja; sanguisuela : French 
sangsue : Calabrese sancisuca : Portuguese sanguessuga : Sardinian Campidanesu 
sangunera : Valencian sangonera : Venetian sangueta : Zeneize sanguetta ' leech '. 

5. Aformant: gr. uAr| "ordure, slime, mud', uAi^u) "filter, clean'; Old Indie sura-m. 
"intoxicating potion'; s^as "alcohol', Avestan hura'Kumys' (wogul. sara, syrj. s^^from 



Iranian) = Lithuanian Latvian sula^ abfiielsenaer tree juice ' (with t7 Latvian sOlat^ siepen '), 
Old Prussian sulo^ coagulated milk'; Old English solu. "slime, mud, puddle, slop'. Old 
High German Middle Low German sol 6s., Old English 5y//a/7 "smudge'. Old Saxon 
sulwian. Old High German sullen 6s., Modern High German suhlen, suhlen^ sjch im Kot 
walzen '; Gothic bl-sauljan' blemish ', Norwegian S0yla6s. 

6. seup-, seub-:0\d Indie supa-m. "broth, soup'; Old Icelandic supa. Old English supan. 
Old High German sufan^ slurp, drink, swig ', suFbroih, soup'. Middle High German suf, 
so/" soup'. Old English sypexx\. " soaking up ', Old IcelandicsO/O/m., Old English sopa 
"gulp', full grade Old High German so^rsoup'. Old Icelandic saupu. " buttermilk '; Old 
English soppi. " sop ', Middle Low German (out of it Middle High German) soppe, suppe 
"sop'. Old High German sopha, soffa^ broth, also with soaked slices; settlings '; Gothic 
supon^ spice ' = Old High German soffon ds. (actually " dunk into broth '); Middle High 
German sOftxw., Middle Low German s^c/7/"sigh'. Old High German suft(e)dn. Middle High 
German sluften, s/ufzen's\g\r\'; Old Icelandic Old English sufln. " Zukost ', Old Saxon 
suval. Old High German suvll(l), -a" sorbiuncula '; Middle Low German suvel, Dutch zuivel 
" der Buttergehalt der Milch '; 

Maybe turk. {*su-) su 'water, aqua, juice' 

Old Church Slavic shs-g, -atl. Iter. sysa//"suck' probably from *sup-s-. 

alb. s/se, th/the 'teat', thith{*sis-) "suck' [common alb. s->th-] 

References: WP. II 468 f., WH. II 622 f., Trautmann 257, 291 f. 
Page(s): 912-913 

Root / lemma: seu-2, (seya-), su- 
Meaning: to bear child; son 

Material: Old Indie sute{sautl), suyate{suyati), savatr gebxert, zeugt', sJ/? "progenitor', 
sutu-m. "Schwangerschaff (: *sufu-s\n Old Irish sutii), suta- m. "son'; sJ//- "birth, progeny 
', susutl-i. "leichtes parturition'; Avestan hav- {hunami) " to give birth to children. Kinder zur 
Welt bringen', hazarjrd-huna' e\v\e, die 1000 Kinder zur Welt bringt'; Old Irish suth {*sutu-s) 
"birth, fruit'; cymr. hog-en "girl' ( *suka), in addition hog-yn "lad, young boy'; due to the 
present *sunami {zoxxv^axe Avestan hunami) and *5^/i7(compare Old Indie suyate): Indo 
Germanic *sunu-s and *5t(/i/-5 originally "*the parturition, birth', then " foetus, son'; 

Old Indie sunu-m.; Avestan hunu-s, Gothic sunus. Old Icelandic sunr. Old High German 
Old English sunu, Lithuanian sunus. Old Church Slavic synt "son'; 



gr. uiu(; (Gen. horn, ultoq) and (secondary) uioq "son' (in addition liom. ui(jov6(; 
"grandchild, grandson' from *sujd[u]-n6-s), as proto Indo Germanic formation verified 
through tochar. B soya {A se) "son' and that reshaped after o'i/s//'" daughter' Armenian ustr 
"son'; also Old English 5^/7/e/ya "grandchild, grandson, nephew ' kann eine corresponding 
reshuffling after Tochter "daughter' sein. 

In Italian-Celtic Gehiete fehlen diese words for 'son'. 

Maybe alb. {*tsun) gun'son'. 

References: WP. II 469 f., Trautmann 292. 
Page(s): 913-914 

Root / lemma: seu-3 : su- : seya- : su- 

Meaning: to bend, turn 

Material: Old Indie suvati^ sets in motion, excites, arouses, animates ', suta- "veranlaftt, 

angetrieben', pra-suta-"\n Bewegung gebracht, angetrieben, entsendet', nr-suta-lrom 

Mannern angetrieben', pra-suti-^ motion; agitation ', sava- " actuation, incitation, 

command, order, Belebung; the Anreger, Befehlende', savTmaniLok. "in actuation, in 

behest ', savitar- " hastener, impeller, motivator, exciter; the god Savitar '; 

Avestan hav- " set in motion ', /7^/7a///"verschafft, seeks to obtain ', hv^nmahi{ *su-en-) " 
we seek to obtain '. apavanvainti {* su-en-u-) "sie lenken ab', ma/nyu-sufa- ' oi Ge\st 
getrieben', hvd/sta-'t\r\e hochste, beste; oldest'; 

Old Irish sd{a)/c/'6reht, kehrt' {*sdu-eie-ti), ess-/'c»-5C»-"miftlingen' (*hinwegdrehen); 
sua(i)nemvc\. "rope, cord' {*seu-n-Ja-md)\ Lithuanian siauras{*seu-ro-) " narrow, tight, slim, 
slender, thin, narrow'; 

Hittite 5i/i/a/-"bump, poke, urge, press, push'. 

seu-k-: osset. xurx' whey ' (Aryan *si//r/'a-.' Lithuanian sukrus^*was sich leicht dreht'); 
Lithuanian sunkalaiP\. "wheys', pa-sukos 6s.; Lithuanian suku, s^M'turn', sukrus 
"movable, nimble, agile', apsukalas^JuxauqeX, Latvian sukt^ escape; to get away ', sukata 
"Drehkrankheif, Slavic *S'bkg, *sb/ra// (preterit-stem *suka-) in russ. sku, s/ra/b "zwirnen, 
zusammendrehen, wind up, roll up ', ablaut. Church Slavic 5^/ra//"turn' (reshaped from 
*soukeJe-, compare russ. sucftb "zwirnen'); 

References: WP. II 470, Trautmann 291, Liden KZ 61, 7 f., Pedersen Hittite 134. 
See also: s. also seuio- " left ' and suei- "bend'. 



Page(s):914 



Root / lemma: seu-4, seu-t- 

Meaning: to boil, move vividly 

Material: Avestan havayqn^sxe schmoren', /7ai/aye///"erschmort' (3. Sg. Opt. huyaras- 

Old Indie *suyur\.o a present 7750/// after the Wurzelklasse); 

in addition Germanic *sau^- in Old Icelandic sjoda 'simmer, seethe, boil, cook'. Old 
English seoda/? (engl. seethe) ds.. Old High German siodan. Middle High German Modern 
High German sieden. Old Icelandic seyd'brausendes water', seyd/r'Kochfeuer'; Gothic 
saut^s^ sacrificial animal ', Old Icelandic sai/d^'sheep, also anderes small cattle'; Old 
Swedish 5a^A'/7"Sprudelquelle'; Germanic *sut=>a- in sodn. TIeischsuppe, broth'; 

Lithuanian siauciu siausti\ corn, grain) winnow, fan, die chaff of corn, grain segregate; 
play; dash, rage ', siuntu, siusti^XoW become'; besides also the meaning "hit' in zem. s/ut/s' 
shove ', Latvian sai/s/ 'geiftein'; compare also Lithuanian saubt/^age, clamor, dash', 
saJM'umhertoben', Old Lithuanian s/autit/" prank pull '; Latvian sau/fsm. 'gate'; 

maybe alb. (*5/-) 5/7^' "thresh, winnow'. 

russ. sucu, sutftb "spaften, joke', s^/(Gen. sut^ m. " merrymaker, buffoon ', slov. sutec 
■fool'. 

References: WP. II 471 f., Trautmann 260. 
Page(s): 914-915 

Root / lemma: seua- su- 

Meaning: to let, leave (?) 

Material: Gr. saw ' allow ' (*£Fa(ji)), spaaov saaov. lupaKouaioi, sua = la Hes., Put. saau), 

Aor. siaaa (to *£Ta); zero grade Old High German vir-sOmen, Modern High German 

saumen, ver-saumen {\nou\6 be denominative eines *sO-md-s' slackening, saumend'). 

References: WP. II 472, SchwyzerGr. Gr. 1, 682, 752.
```


## [2026-09-14T01:57:08.941Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"seuə\\|seua-\\|seu[aə]-1\\|^seu\\|sup-\\|To take liquid\\|to take liquid\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-14T01:57:08.995Z] TOOL RESULT

```
931:seue-', To give birth. Suffixed zero-grade form in deriva- tive noun *su(2)-nu-, son, in Germanic *sunuz in Old English sunu, son: SON. See also su-. [Pok. 2. seu- 913.]
932:seue-2, To take liquid. I. Suffixed zero-grade form
1050:swento-. Healthy, strong. Zero-grade form *sunto- in Germanic *sunth- in Old English gesund, healthy (ge-, intensive prefix; see kom): SOUND?. [Pok. suento- 1048.] swep-'. To sleep. 1. Suffixed form *swep-os- in Latin sopor, a deep sleep: SOPOR; (SOPORIFIC). 2. Suffixed form *swep-no- in Latin somnus, sleep: SOMNI-, SOMNOLENT; INSOMNIA. 3. Suffixed zero-grade form *sup-no- in Greek hupnos, sleep: HYPNO-, HYPNOS, (HYPNOSIS), HYPNOTIC. [Pok. 1. swep- 1048.]
1051:swep-2. To throw, sling, cast. 1. O-grade form *swop- perhaps in Germanic variant expressive form *swabb- in Middle Dutch swabbe, mop, splash: swaB. 2. Suffixed zero-grade form *sup-d- in Latin dissipdre, to disperse (dis-, apart): DISSIPATE. [Pok. 2. swep- 1049.]
1105:uper. Over. 1. Extended form *uperi in Germanic *uberi in: a. Old English ofer, over: OVER; b. Middle Dutch over, over: ORLOP. 2. Variant form *(sjuper in: a. Latin super, super-, above, over: SOUBRETTE, SOVEREIGN, SUPER-, SUPERABLE, SUPERIOR, SUPREME, (SUPREMO), SUR-; SIRLOIN; b. suffixed form *(s)uper-no- in Latin supernus, above, upper, top: SUPERNAL,; C. suffixed form *super-bhw-o-, “being above” (*bhw-o-, being; see bheue-), in Latin superbus, superior, excellent, arrogant: SUPERB; d. suffixed (superlative) reduced form *sup-mo- in Latin summus, highest, topmost: SUM, SUMMIT; @. var- iant form *(s)juprd in Latin supra, above, beyond: (so- PRANINO), SOPRANO, SUPRA-; SOMERSAULT. 3. Basic form *uper in Greek huper, over: HYPER-. [Pok. uper 1105.]
1108:eaves: EAVES; b. Germanic *obisdrup-, dripping water from the eaves (*drup-, to drip, from *dhrub-; see dhreu-), in Old English yfesdrype, yfes drypx, water from the eaves: EAVESDROP. 6. Variant form *(s)up- in: a. Latin sub, under: SOUTANE, SUB-; b. Latin supinus, lying on the back (< “thrown backward or under’): SUPINE!, SUPINE?; Cc. suffixed form *sup-ter in Latin subter, secretly: SUBTERFUGE; d. Latin supplex, “with legs folded under one” (-plex, -fold; see plek-): SUPPLE. 7. Basic form *upo in Greek hupo, under: HYPO-. 8. Suf- fixed variant form *ups-o- in Greek hupsos, height, top: HYPSO-. 9. Basic form *upo- in Celtic *vo-, under, in Latin verédus, post horse (see reidh-). 10. Compound *upo-st-o- probably in Celtic *wasso-, “one who stands under,” servant, young man (*sto-, standing; see sta-), in Medieval Latin vassus, vassal: VALET, (VARLET), VASSAL. 11. Sanskrit wpa, near to, under (in upanisad, Upani- shad): OPAL, UPANISHAD. [Pok. upo 1106.]
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
```


## [2026-09-14T01:57:11.663Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '931,934p' AHD_watkins1985.txt; echo ---; grep -n \"seut-\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T01:57:11.769Z] TOOL RESULT

```
seue-', To give birth. Suffixed zero-grade form in deriva- tive noun *su(2)-nu-, son, in Germanic *sunuz in Old English sunu, son: SON. See also su-. [Pok. 2. seu- 913.]
seue-2, To take liquid. I. Suffixed zero-grade form
skei-
*sua-yo-, contracted to *si-yo- in Greek huein, to rain, and huetos, rain: ISOHYET. II. Possible extended zero-grade form *sib-. 1.Germanic *sip- in: a. Old English sipan, sipian, to drink, sip: suP!; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic “supp- in: a. Old English sopp, bread dipped in liquid: sop; b. possibly Low German sippen, to sip, probably akin to the source of Middle English sippen, to sip: stp. III. Possible ex- tended zero-grade form “sig-. 1. Germanic *sik- in Old English sican, to suck: sucK. 2. Germanic shortened form *sukdn in Old English socian, to steep: SOAK. 3. Latin siigere, to suck: SUCTION, SUCTORIAL. 4, Variant form *sik- in Latin siicus, succus, juice: SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High German sudelen, to soil, do sloppy work, akin to Middle Dutch soetler, sutler: SUTLER. [Pok. 4. seu- 914.] si-lo-. Silent. Suffixed (stative) form *si/-é- in Latin silére, to be silent: SILENT. [In Pok. 2. sé(i)- 889.] skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.] skai-. Also kai-. Bright, shining. 1. Extended form *kaid- in Germanic *haiduz, “bright appearance,” manner, quality, in Old English -hdd, quality, condition: -Hoop. 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kdi- 916.] [skalkaz. Servant, slave. Germanic noun of unknown origin. 1. Old High German compound marahscalc, “horse-servant” (see marko-). 2. Germanic compound *sini-skalkaz, “old servant” (see sen-'). [In Pok. (s)kel- 929.]] skamb-. Also kamb-. To curve, bend. Suffixed form *kamb-o- in Celtic *kambo-, crooked, and denominative verb *k(a)mb-yo-, to turn, exchange, whence Gallo-Latin cambidre, to exchange: CAMBIST, CAMBIUM, CHANGE. [Pok. (s)kamb- 918.] skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; AS- CEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-sld- in Latin scdlae, steps, ladder: ECHELON, ESCALADE, SCALE?. sked-. To split, scatter. Extension of sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian, to scatter: SHATTER. 2. Variant nasalized form *ska-n-d- in Latin scandula, a shingle for roofing (< “split piece”): SHINGLE}. [Pok. (s)k(hjed- 918.] skeei-. To gleam. 1. Suffixed form “ske(ji-no- in Ger- manic *skinan, to gleam, shine, in: a. Old English scinan, to shine: SHINE; b. Old High German scinan, to shine: GEGENSCHEIN. 2. Germanic extended form *ski-m- in Old English scimerian, scymrian, to shine brightly: SHIM- MER. 3. Possibly suffixed form *ski-nto-, shining, in Latin scintilla, a spark: SCINTILLA, SCINTILLATE, STEN- CIL, (TINSEL). 4. Suffixed zero-grade form *skia-G-, *skiy-d- in Greek skia, shadow: SKIAGRAM, SKIASCOPE, SQUIRREL. [Pok. skai- 917.] skei-. To cut, split. Extension of sek-. 1. Germanic suffixed form *ski-nd- in: a. Old English scinu, shin, shinbone (< “piece cut off’): SHIN!-; b. Old French eschine, backbone, piece of meat with part of the back- bone: CHINE, 2, Latin scire, to know (< “to separate one thing from another,” “discern”): SCIENCE, SCILICET, SCIOLISM, SCIRE FACIAS; ADSCITITIOUS, CONSCIENCE, CONSCIOUS, NESCIENCE, (NICE), OMNISCIENT, PLEBI- SCITE, PRESCIENT. 3. Suffixed zero-grade form *skiy-end in Old Irish scian, knife: SKEAN. 4. Extended root *skeid- in: a. Germanic *skitan, to separate, defecate, in Old English *scitan, to defecate: SHIT; b. suffixed zero-grade
---
934:*sua-yo-, contracted to *si-yo- in Greek huein, to rain, and huetos, rain: ISOHYET. II. Possible extended zero-grade form *sib-. 1.Germanic *sip- in: a. Old English sipan, sipian, to drink, sip: suP!; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic “supp- in: a. Old English sopp, bread dipped in liquid: sop; b. possibly Low German sippen, to sip, probably akin to the source of Middle English sippen, to sip: stp. III. Possible ex- tended zero-grade form “sig-. 1. Germanic *sik- in Old English sican, to suck: sucK. 2. Germanic shortened form *sukdn in Old English socian, to steep: SOAK. 3. Latin siigere, to suck: SUCTION, SUCTORIAL. 4, Variant form *sik- in Latin siicus, succus, juice: SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High German sudelen, to soil, do sloppy work, akin to Middle Dutch soetler, sutler: SUTLER. [Pok. 4. seu- 914.] si-lo-. Silent. Suffixed (stative) form *si/-é- in Latin silére, to be silent: SILENT. [In Pok. 2. sé(i)- 889.] skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.] skai-. Also kai-. Bright, shining. 1. Extended form *kaid- in Germanic *haiduz, “bright appearance,” manner, quality, in Old English -hdd, quality, condition: -Hoop. 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kdi- 916.] [skalkaz. Servant, slave. Germanic noun of unknown origin. 1. Old High German compound marahscalc, “horse-servant” (see marko-). 2. Germanic compound *sini-skalkaz, “old servant” (see sen-'). [In Pok. (s)kel- 929.]] skamb-. Also kamb-. To curve, bend. Suffixed form *kamb-o- in Celtic *kambo-, crooked, and denominative verb *k(a)mb-yo-, to turn, exchange, whence Gallo-Latin cambidre, to exchange: CAMBIST, CAMBIUM, CHANGE. [Pok. (s)kamb- 918.] skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; AS- CEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-sld- in Latin scdlae, steps, ladder: ECHELON, ESCALADE, SCALE?. sked-. To split, scatter. Extension of sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian, to scatter: SHATTER. 2. Variant nasalized form *ska-n-d- in Latin scandula, a shingle for roofing (< “split piece”): SHINGLE}. [Pok. (s)k(hjed- 918.] skeei-. To gleam. 1. Suffixed form “ske(ji-no- in Ger- manic *skinan, to gleam, shine, in: a. Old English scinan, to shine: SHINE; b. Old High German scinan, to shine: GEGENSCHEIN. 2. Germanic extended form *ski-m- in Old English scimerian, scymrian, to shine brightly: SHIM- MER. 3. Possibly suffixed form *ski-nto-, shining, in Latin scintilla, a spark: SCINTILLA, SCINTILLATE, STEN- CIL, (TINSEL). 4. Suffixed zero-grade form *skia-G-, *skiy-d- in Greek skia, shadow: SKIAGRAM, SKIASCOPE, SQUIRREL. [Pok. skai- 917.] skei-. To cut, split. Extension of sek-. 1. Germanic suffixed form *ski-nd- in: a. Old English scinu, shin, shinbone (< “piece cut off’): SHIN!-; b. Old French eschine, backbone, piece of meat with part of the back- bone: CHINE, 2, Latin scire, to know (< “to separate one thing from another,” “discern”): SCIENCE, SCILICET, SCIOLISM, SCIRE FACIAS; ADSCITITIOUS, CONSCIENCE, CONSCIOUS, NESCIENCE, (NICE), OMNISCIENT, PLEBI- SCITE, PRESCIENT. 3. Suffixed zero-grade form *skiy-end in Old Irish scian, knife: SKEAN. 4. Extended root *skeid- in: a. Germanic *skitan, to separate, defecate, in Old English *scitan, to defecate: SHIT; b. suffixed zero-grade
2236:SEETHE seut- SEGMENT sek- SEGNO  sekw-1 SEGREGATE ger-1, s(w)e- SEGUE sekw-1 SEGUIDILLA sekw-1 SEICENTO dekm, s(w)eks SEIGNIOR sen- SEISIN sag-
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
2324:SUCK seue-2 SUCTION seue-2 SUCTORIAL seue-2 SUDATORIUM sweid-2 SUDDEN ei-1 SUDORIFEROUS sweid-2 SUDORIFIC sweid-2 suDs_ seut-
2328:SURE cilra, s(w)e- SURFACE dhé-1 SURFEIT dhé-1 SURGE reg-! SURGEON ghesor- SURGERY ghesor-, werg- SURLY sen-1 SURMISE (s)meit(9)- SURMULLET mel-2, saus- SURPLICE pel-4 SURPLUS pele-' SURPRISE ghend- SURRENDER d6- SURREPTITIOUS rep- SURROUND wed-! SURVEILLANT weg-2 SURVEY weid- SURVIVE gWei- SUSCEPTIBLE kap- SUSPECT spek- SUSPEND (s)pen- SUSPIRE spirare SUSTAIN ten- SUSURRATION swer-2 SUTLER seut- SUTRA syil- SUTTEE e@8- SUTURE syu- SVELTE wel-4 SWAB swep-2 SWAG sweng(W)- SWAIN s(w)e- SWALE swel-2 SWALLOW! swel-1 SWAMI s(w)e- SWAMP swombho- SWAN swen- SWANK sweng(w)- swaP swei-2 SWARF swerbh- SWARM swer-2 SWART swordo- SWASTIKA @S-, SU- SWEAR swer-1 SWEAT sweid-2 SWEET swad- SWELTER swel-2 SWERVE swerbh- SWIFT swei-2 SWILL swel-!
```


## [2026-09-14T01:57:27.942Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sunus\\|hunami\\|hunu\" KLN_1966.txt | head -20; echo \"=== 1971 ===\"; grep -n \"hunami\\|hunu-\\|sunuz\" KLN_1971.txt | head -20"
}
```


### [2026-09-14T01:57:28.019Z] TOOL RESULT

```
35905:Derivative:  somnolent-ly,  adv. son,  n.  —  ME.  sune,  sone,  fr.  OE.  sunu,  rel.  to OS.,  OFris.  sunu,  ON.  sour,  Dan.  sen,  Swed.  son, MDu.  sone,  Du.  zoon,  OHG.  sum,  sun,  MHG. sun,  G.  Sohn,  Goth,  sunus,  ‘son’,  and  cogn.  with OI.  suniih,  Avestic  hunush,  OSlav.  synu,  Lith. sunus,  ‘son’,  and — without  n-formativc  ele¬ ment — with  Toch.  B  soya,  A  se,  Gk.  ui6?,  ‘son’, Arm.  ustr,  ‘son’  (influenced  in  form  by  dustr, ‘daughter’),  OI.  sulah,  ‘son’,  sute,  siyate,  savati, ‘begets,  procreates’,  OIr.  suth  (for  su-tu),  ‘fetus’. All  these  words  derive  fr.  I.-E.  base  *seu-,  *su-, ‘to  bear,  bring  forth ;  birth’, sonance,  sonancy,  n.  —  Formed  from  next  word with  suff.  -ce,  resp.  -cy.  Cp.  assonance,  conso¬ nance,  dissonance,  resonance, sonant,  adj.  and  n.  —  L.  sonans,  gen.  -antis,  pres, part,  of  sonare,  ‘to  sound’,  which  stands  for *swenare  and  is  rel.  to  sonus  (for  *swonos), ‘sound’,  fr.  base  *swen-,  ‘to  sound'.  See  sound, ‘noise’,  and  cp.  assonant,  consonant,  dissonant, resonant,  resound,  sonata,  sonnet,  sound,  ‘noise’, and  the  second  element  in  unison.  For  the  ending see  suff.  -ant.
=== 1971 ===
```


## [2026-09-14T01:57:29.273Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"havayeiti\\|hāvayeiti\\|havayan\\|seethe\" KLN_1966.txt | head -20; echo \"=== 1971 ===\"; grep -n \"havayeiti\\|seothan\\|seethe\" KLN_1971.txt | head -20"
}
```


### [2026-09-14T01:57:29.513Z] TOOL RESULT

```
4462:barm,  n.,  yeast.  —  ME.  berme,  fr.  OE.  beorma, rel.  to  Du.  berm,  MLG.  berm,  barm,  LG.  barme (whence  G.  Barme),  and  cogn.  with  L.  fermen- tum,  ��substance  causing  fermentation’,  fr.  I.-E. base  *bher-,  ‘to  boil,  seethe’,  whence  also  OI. bhurati,  ‘moves  convulsively,  quivers’,  Mir. berbaim,  ‘I  boil,  seethe’.  Cp.  brand,  bread,  brew, broil  (in  both  senses),  broth.  Cp.  also  ferment.
5617:‘fermented  liquor  made  from  barley,  beer’,  L. defrutum,  ‘must  boiled  down’,  fervere  or  fervere, ‘to  boil,  glow,  foam’,  Alb.  brum,  brume,  ‘leaven’, Russ,  bruja,  ‘current’,  bruit',  ‘to  stream  with force’,  OIr.  bruth,  ‘heat’,  Mir.  berbaim,  ‘I  boil, seethe’.  Base  *bheru-,  *bhreu-,  *bhru-  represents enlargement  forms  of  base  *bher-,  ‘to  boil,  fer¬ ment’,  which  appears  e.g.  in  L.  fermentum,  ‘sub¬ stance  causing  fermentation’.  Cp.  brewis.  Cp. also  barm.  Bourbon,  bourn,  ‘stream’,  brand, bread,  breath,  brede,  ‘to  roast’,  brindled,  broil  (in both  senses);  brood,  broth,  burbot,  burn,  n.  and v.  Cp.  also  ferment,  fervent,  fry,  ‘to  cook  in  fat’. Derivatives:  brew,  n.,  brew-age,  n.,  brew-er,  n., brew-er-y,  n.,  brew-ing,  n.,  brewster  (q.v.) brewis,  n.,  beef  broth.  —  ME.  broues,  brouet, brouis,  ‘broth’,  fr.  OF.  (=  F.)  brouet,  of  s.m., derivative  of  breu,  ‘broth’,  which  is  of  Teut. origin.  See  brew  and  cp.  words  there  referred  to. brewster,  n,,  a  brewer.  —  Formed  fr.  brew  with suff.  -ster.  The  word  denoted  orig.  a  female brewer.
5797:Derivatives:  Buddh-ic,  adj.,  Buddh-ism,  n., Buddh-ist,  n.,  Buddh-ist-ic,  Buddhist-ic-al,  adjs. Buddleia,  n.,  a  genus  of  shrubs  (bot.)  —  Named after  the  English  botanist  Adam  Buddie  (died in  1715).  For  the  ending  see  suff.  -ia. buddy,  n.,  chum,  companion,  former  soldier  (col- loq.)  —  Orig.  the  noun  buddy  was  an  affection¬ ate  term  for  a  child  and  is  etymologically  iden¬ tical  w  ith  the  adj.  buddy,  ‘full  of  buds,  resembling a  bud'.  See  bud  and  adj.  suff.  -y. budge,  intr.  and  tr.  v.,  to  stir,  move.  —  F.  bouger, fr.  VL.  *bullicare,  ‘to  bubble,  boil  up,  seethe’, hence  ‘to  be  agitated,  to  be  in  movement’,  fr. L.  bullire,  ‘to  bubble’.  Cp.  It.  bulicare,  ‘to bubble,  seethe’,  and  O Proven;,  bolegar,  ‘to  stir, budge’,  which  are  of  the  same  origin  as  F. bouger,  and  see  boil,  v.
5888:burbot,  n.,  a  fresh-water  fish  of  the  cod  family.  — F.  bourbotte,  fr.  bourbe,  ‘mud,  mire’,  fr.  Gaulish *borva-,  a  form  reconstructed  from  Borvo,  name of  a  thermal  deity  (whence  the  place  name Bourbon),  rel.  to  OIr.  berbaim,  ‘I  boil,  seethe’, fr.  I.-E.  base  *bheru-,  ‘to  boil’.  See  brew  and  cp. F.  barbote,  ‘eelpout’,  barboter,  ‘to  dabble  about in  mud  or  in  muddy  water’,  which  are  related to  bourbe,  ‘mud,  mire’.  Cp.  also  Bourbon, burd.n.,  lady.  — •  ME.  byrd,  burd,  prob.  metathesis of  OE.  bryd,  ‘bride’.  See  1st  bride, burden,  n.,  a  load.  —  ME.  burden,  birden,  birthen, fr.  OE.  byrden ,  rel.  to  ON.  byrdr,  OS.  bur- thinnia,  OHG.  burdi,  MHG.,  G.  biirde,  Goth. baurpei;  lit.  ‘that  which  is  borne’,  fr.  I.-E.  base *bher-,  ‘to  bear,  carry’.  See  bear,  "to  carry’  and cp.  burthen.
7310:cheese,  n.,  milk  curd.  —  ME.  chese,  fr.  OE.  cese, fr.  L.  cascus,  ‘cheese’,  whence  also  OS.  kasi, MDu.  case  (Du.  kaas),  OHG.  chdsi,  kasi (MHG.  ksese,  G.  Kase).  L.  cascus  is  prob.  cogn. with  Prakrit  chdsi,  ‘buttermilk’,  OSlav.  kvasu, ‘leaven’,  kyselu,  ‘sour’,  kyseti,  ‘to  turn  sour’, and  with  OI.  kvathati,  ‘boils,  seethes’,  but  OE. hwseg  (see  whey)  is  not  cognate.  Cp.  casein, catechu,  chcssel.
12625:ectro-,  combining  form  denoting  congenital  ab¬ sence  (med.)  —  Fr.  Gk.  Exxpaxric,  ‘miscarriage’, fr.  EXTixpcoaxetv,  ‘to  miscarry’,  fr.  ex  (see  ec-) and  TixpdxrxEiv,  ‘to  wound,  hurt,  injure’.  See throw  and  cp.  words  there  referred  to. ecu,  n.,  an  old  French  silver  coin.  —  F.,  fr.  OF. escu,  fr.  L.  scutum,  ‘shield’.  See  scutum  and  cp. escudo.  The  coin  was  called  ecu  (‘shield’)  from the  coins  issued  under  Louis  IX,  which  had  the shield  of  France  as  device, ecumenic,  ecumenical,  adj.,  general,  universal.  — Late  L.  oecumenicus,  fr.  Gk.  oixoup.Evrxoc,  ‘open to  the  whole  world’,  fr.  oixoupivr]  (scil.  yt)), ‘the  inhabited  world’,  fern,  of  the  pass.  pres, part,  of  oExelv,  ‘to  inhabit’,-  fr.  olxog,  ‘house, abode,  dwelling’.  See  economy  and  -ic.  For  the use  and  force  of  the  passive  suff.  *-menos  in English  words  of  Greek  and  Latin  origin  see alumnus  and  cp.  words  there  referred  to. Derivatives:  ecumenical-ly,  adv.,  ecumenic-ity,r\. eczema,  n.,  inflammatory  disease  of  the  skin (med.)  —  Medical  L„  fr.  Gk.  gx^Efia,  prop, ‘something  thrown  out  by  heat’,  fr.  ix  (see  ec-) and  £e[zx,  ‘that  which  is  boiled’,  fr.  I.-E.  base *yes-,  ‘to  boil,  seethe’.  See  yeast  and  cp.  the first  element  in  zeolite  and  the  second  element in  apozem.
14582:ferment,  n.  —  F.,  fr.  L.  fermentum,  ‘substance causing  fermentation’,  fr.  I.-E.  base  *bher-, ‘to  boil  up,  seethe'.  See  barm  and  cp.  fervent. Cp.  also  fry,  ‘to  cook  in  fat’.  For  the  ending see  suff.  -ment.
14611:fervent,  adj.,  i)hot;  2)  deeply  earnest;  ardent.  — L.  fervens,  gen.  -entis,  pres.  part,  of  fervere,  ‘to boil,  glow,  foam’,  fr.  I.-E.  base  *bheru-,  en¬ larged  form  of  *bher-,  ‘to  boil,  seethe’,  whence also  L.  defrutum ,  ‘must’.  See  barm  and  -ent  and cp.  ferment.
15483:fruticose,  adj.,  bushy,  shrubby.  —  L.  fruticosus, ‘full  of  shrubs  or  bushes’,  it.  frutex,  gen.  fruticis. See  prec.  word  and  adj.  suff.  -ose. fry,  tr.  v.,  to  cook  in  fat;  intr.  v.,  to  be  cooked in  fat.  —  ME.  frien,  fr.  frire,  fr.  L.  frigere,  ‘to roast,  parch,  fry’,  which  is  cogn.  with  OI. bhfjjdti,  ‘roasts’,  bharjanah,  ‘roasting’  (part.); ModPers.  birishtan,  ‘to  roast’,  Gk.  (ppuvetv,  ‘to roast,  bake’,  Lith.  birgelas,  ‘small  beer’,  Lett. btrga,  ‘vapor,  smoke’,  OPruss.  au-birgo,  ‘owner of  a  cook  shop’.  All  these  words  derive  fr.  I.-E. *bher(e)g-,  *bhrig-,  *bhritg-,  enlargements  of base  *bher-,  ‘to  boil,  seethe’.  See  brew  and  cp. fervent.  Cp.  also  fricandeau,  fricassee,  frit, fritter,  ‘piece  of  fruit’.
34438:Derivatives:  seesaw,  tr.  and  intr.  v.,  adj.  and  adv. seethe,  tr.  and  intr.  v.  —  ME.  sethen,  fr.  OE.  seo- dan,  rel.  to  ON.  sjoda,  Dan.  syde,  Swed.  sjuda, Norw.  sjoa,  OFris.  sidtha,  Du.  zieden,  OHG. siodan,  MHG.,  G.  sieden,  ‘to  seethe’,  Goth. saups,  ‘sacrificial  animal,  victim’,  fr.  I.-E.  base *sew-,  ‘to  seethe,  boil’,  whence  also  Avestic hdvayeiti,  ‘stews’.  Cp.  sod,  ‘turf’,  sodden,  suds, sutler.
34439:Derivatives:  seethe,  n.,  seeth-ing,  adj.,  seeth-ing- ly,  adv.
35794:sod,  n.,  turf.  —  ME.  sodde,  sod,  fr.  MLG.  or MDu.  sode  (Du.  zode),  ‘turf’,  which  is  rel.  to OFris.  satha,  ‘sod’,  and  to  E.  sodden  and  seethe. Derivatives:  sod,  tr.  v.,  sodd-ing,  n. sod,  obsol.  past  tense  and  pp.  of  seethe, sod,  n.  — •  Contraction  of  sodomite, soda,  n.,  an  alkaline  substance.  —  ML.,  fr.  ML. sodanum,  lit.  ‘headache  remedy’,  fr.  soda, ‘headache’,  fr.  Arab.  sudd‘,  in  vulgar  pronun¬ ciation  $oda\  ‘splitting  headache’,  fr.  sdda‘a, ‘he  split’.  Cp.  sodalite,  sodium.
35798:sodden,  adj.  —  ME.  soden,  fr.  OE.  soden,  pp.  of seodan,  ‘to  boil,  cook,  seethe’.  See  seethe. Derivatives  -.sodden,  tr.and  intr.  v. ,  sodden-ness,  n. sodic,  adj.,  containing  sodium.  —  Formed  fr. sodium  with  adj.  suff.  -ic.
37362:Sudra,  n.,  the  lowest  Hindu  caste.  —  OI.  sudrah. suds,  n.  pi.,  1)  soapy  water;  2)  foam.  —  Lit. ‘things  sodden’;  rel.  to  MDu.  sudde,  ‘marsh, lake’,  and  to  E.  sodden  and  seethe  (q.v.) sue,  tr.  and  intr.  v.  — -  ME.  siwen,  suwen,  suen,  fr. OF.  suir,  a  collateral  form  of  sivre,  sivir  (F. suivre),  fr.  VL.  *sequere,  *sequire,  correspond¬ ing  to  L.  sequi,  ‘to  follow’.  See  sequel  and  cp. ensue,  pursue.  Cp.  also  suit,  pursuit.
37639:sustain,  tr.  v.  - —  ME.  susteinen,  fr.  AF.  sustein-, stem  of  OF.  sustenir,  soustenir  (F.  soutenir),  ‘to hold  up’,  fr.  VL.  *sustenire,  corresponding  to L.  sustinere,  ‘to  hold  up,  maintain',  which  is formed  fr.  sus-  and  tenere,  ‘to  hold’.  See  tenable and  cp.  abstain  and  words  there  referred  to.  Cp. also  sostenuto,  souteneur, sustenance,  n.  —  ME.,  fr.  OF.  sustenance,  souste- nance  (F.  soutenance),  fr.  Late  L.  sustinentia, ‘endurance’,  fr.  L.  sustinens,  gen.  -entis,  pres, part,  of  sustinere.  See  prec.  word  and  -ance. sustentation,  n.,  maintenance;  preservation.  — OF.  sustentacion  (F.  sustentation),  fr.  L.  susten- tationem,  acc.  of  sustentatio,  ‘maintenance’,  fr. sustentatus,  pp.  of  sustentare,  ‘to  hold  up,  sup¬ port’,  freq.  of  sustinere  (pp.  sustentus).  See  sus¬ tain  and  -ation  and  cp.  prec.  word, susurrant,  adj.,  whispering.  —  L.  susurrans,  gen. -antis,  pres.  part,  of  susurrdre.  See  next  word, susurration,  n.,  whisper,  murmur.  —  ME.,  fr.  L. susurratio,  gen.  -onis,  fr.  susurrat(um),  pp.  stem of  susurrdre,  ‘to  hum,  whisper,  murmur’,  fr. susurrus,  ‘whisper,  murmur’,  from  the  redupli¬ cation  of  the  I.-E.  imitative  base  *swer-,  *sur-, *surr-,  ‘to  sound’,  whence  OI.  svarati,  ‘sounds, resounds’,  Gk.  trupiy!;,  ‘flute’,  upov  (for •mipov),  ‘beehive,  swarm,  crowd’,  L.  surdus, ‘dull’.  OSlav.  svirati,  ‘to  whistle’,  Lith.  surma, ‘pipe,  shawm’,  G.  schwirren,  surren,  ‘to  buzz', OE.  swearm,  ‘swarm’.  See  swarm  and  cp.  surd, sordine,  sordinella,  Sorex,  syrinx, susurrous,  adj.,  whispering,  rustling.  —  Formed with  suff.  -ous  fr.  L.  susurrus.  See  prec.  word, sutler,  n.,  a  person  who  follows  the  army  to  sell food  to  the  soldiers.  —  MDu  soeteler,  ‘bad cook,  camp  cook’  (whence  Du.  zoetelaar, ‘sutler’),  fr.  soetelen,  ‘to  cook  badly’,  which  is rel.  to  Late  MHG.  sudelen,  of  s.m.,  and  to  MDu., MHG.,  G.  sieden,  Du.  zieden,  ‘to  seethe’;  see seethe.  (G.  sudeln  in  the  above  sense  is  not  to  be confused  with  G.  sudeln  in  the  sense  of  ‘to  cover
=== 1971 ===
26120:base *bher~, ‘to boil, seethe’, whence also OI. 
26122:berbaim , ‘I boil, seethe’. Cp. brand, bread, brew, 
33654:seethe’. Base *bheru-, *bhreu-, *bhru- represents 
34911:fr. VL. *bullicare, ‘to bubble, boil up, seethe’, 
34914:bubble, seethe’, and OProven?. bolegar, ‘to stir. 
35444:Bourbon), rel. to OIr. berbaim , ‘I boil, seethe’, 
44687:and with OI. kvathati, ‘boils, seethes’, but OE. 
78935:*yes-, ‘to boil, seethe’. See yeast and cp. the 
91832:‘to boil up, seethe’. See barm and cp. fervent. 
92023:larged form of *bher-, ‘to boil, seethe’, whence 
98114:base *bher-, ‘to boil, seethe’. See brew and cp. 
216948:seethe, tr. and intr. v. — ME. sethen, fr. OE. seo- 
216951:siodan , MHG., G. sieden , ‘to seethe’, Goth. 
216953:*se w -, ‘to seethe, boil’, whence also Avestic 
216954:havayeiti , ‘stews’. Cp. sod, ‘turf’, sodden, suds, 
216957:Derivatives: seethe, n., seeth-ing, adj., seeth-ing- 
225584:OFris. sdtha, ‘sod’, and to E. sodden and seethe. 
225587:sod, obsol. past tense and pp. of seethe, 
225620:seodan , ‘to boil, cook, seethe’. See seethe. 
236165:lake’, and to E. sodden and seethe (q.v.)
```


## [2026-09-14T01:57:43.437Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=35880 && NR<=35910' KLN_1966.txt | grep -n \"14[0-9][0-9]\\|1[45][0-9][0-9]\" | head; echo \"--- markers near seethe/son ---\"; grep -n \"^\\s*1[34][0-9][0-9]\\s*$\" KLN_1966.txt | awk -F: '$1>34300 && $1<36200' | head -30"
}
```


### [2026-09-14T01:57:44.744Z] TOOL RESULT

```
11:1473
--- markers near seethe/son ---
34468:1413
34538:1416
34661:1422
34721:1424
34722:1425
34760:1426
34761:1427
34814:1428
35054:1439
35080:1440
35081:1441
35136:1442
35161:1443
35193:1445
35205:1444
35251:1446
35289:1448
35311:1449
35341:1450
35342:1451
35407:1452
35416:1453
35451:1454
35452:1455
35494:1456
35716:1465
35748:1466
35761:1467
35790:1469
35851:1470
```


## [2026-09-14T01:57:48.081Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\s*1[34][0-9][0-9]\\s*$\" KLN_1966.txt | awk -F: '$1>34200 && $1<34480' | head -20; echo ===; sed -n '34400,34412p' KLN_1966.txt"
}
```


### [2026-09-14T01:57:49.205Z] TOOL RESULT

```
Exit code 1
34241:1405
34468:1413
(eval):1: == not found
```


## [2026-09-14T01:57:54.516Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"haoma\\|Haoma\\|hôm\\|hūm\\|hum \" HRN.txt | head -20"
}
```


### [2026-09-14T01:57:54.604Z] TOOL RESULT

```
5188:^'j Wahrsolioinlioh ist wie in panedahum noch c zu lesen.- 129 -
9491:den 8äh^s findet sich hijdehum (z. ß. S. 84).
9607:4ll3. höm 'Haomastrauch, -pflanze*; vergl. hfun (d-majüH
9608:. -^wo^ *Magierhaoma (eine nicht näher zu bestimmende
10395:75. dürös *den Tod fernhaltend' (Haoma).
13174:niihum 1056.
16848:sicdahum 763 u. Anm.
21865:Sgl. hum 440.
```


## [2026-09-14T01:57:55.176Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"haoma\\|hauma\" BRT.txt | head -20"
}
```


### [2026-09-14T01:57:55.243Z] TOOL RESULT

```
2899:•  j.,  g.  'ao}ah-  n.  '(physische)  Kraft,  Stärke': asistim  narl  alaotw  °Jö  Y.  60. 3;  —yakmi niyne  nars  'Jartha  Y.  /o.  a ;  —  ai-avaia '}arfka  yaia  yal  panca  narS  "mit  solcher Kraft,  als  wären  es  fünf  Männer"  V.  jj. loPaZ.;  Yt,2.i2,  14;  —  usla  U yd  ä"j 'jaiika  vasöjciairä  ahi  haoma  Y.9.25; —  kacaiti  dim  aspahe  "Jö  uitrahe  °Jö vlrahe  °j<>  Yt.  it).(i&;  8.2^^;  —  "jö  tanvö vispaya  Yt/.^.29;  —  -jö  vJspdMnüM  Y. 5.17;  —  drfahela  paiti  °)arakö  Yt,  i_j. 134;  ~-  y~'  itfsfro)  arinam  ..  matilüm 'jö  abaraiii  \t  14.12;  —  apa  .  .  buei'ä- °}5  , .  barahi  apa  pä',ayä  sävar»  Yt.  10. 23;  62;  —  haomö  asibil  yöi  ..  zävari "jssca  baxhili  Y.  9. 22; —  °Jasca  nn- S«)Wf'a..Y.  77.8,  yi.j.22,y.i,Y.  72.6;  — yS  nü  asSif  °janAil  vandayaÜJ  (sd.)  ., gae^am  Y.50,3.  a)  AS.  °jö  als  Adv,
3365:—  'Ha  ASvana  haoman  hunylt  (sd.)  N, G8;  —  Oj  j^aaas  -^'ä  . .  '%ä . .  'ia  vi ut3  Xylma  ..  iäPm  räitt  (sd.)  Y.40.4;  — °Ü(i  zJ  aüikä  (daSnayli)  asti  yaoidlitis V.J0.19;  Y.20,  I,  aj  nachgestellt:  la- "^warasia  '"ia  garayö  ..  ytig-J;  — hinter  yar.  yezl  '^iJ  sfJ  AaüTm  (sd.)  .  . at  . .  Y.J4.6;  —  taj  Sroä  p»riS3  . .  y.i fravaxlyj  yezX  tJ    °><1    /iai>yJ  Y.44.6;
3867:•  j.aiwri.vaeSayanta-  Adj.  'der  zugewiesen werden  soll,  wird,  dedicandus':  haoma  . . asiiya  aiwi.vaioayamna  asaya  'la  ". .  qui dedicantur  .  .  dedicabuntur"  Y\.f).$.
4673:(es  ist)  .  .  als  sonst  die  Wölfe  (es  s\nA)"^Vfr>nfnU  ya^a  "«y.f  J'Ä/ (NPm.)  arsän5  V. 18.32;  YL/5.54;  —  baval  ai7fi.vanya  . . ta^ryavantfm  . .  piSammca  . .  uta  -nyasät (als  APm.)  .  .  fyaoninhS  Yt/(J,87'>;  — Aazannm  azinqm  udarS^rqsanqm  ..duyt /lazaare'nyaiiqmcii'V.iS.TyiT^.  b)  Plur. mit  vorausgch.  vjspa-  'alle  andern':  vispe ZI  "nye  *maoaKiAs  .  .  äai  Ab  yB  haomahe maoB  Y,  /0.8;  Yt  77.  5;  —  ya%a  azPtn avavata  v}r>^ra  hacfäneyaia  vupe  *'nye^ airt  Ytj.ög;  —  azSm  ..fravBivXd!  vTspSng "nySng  . ,  Y.  44. 1 1.  c)  Sing,  und  Plur.
4778:;von  Arn.  geschützten  Pflanzen",  in  Dual- verbindung mit  haurvatat-  (sva.  Wasser): 3^ar3%3m  myasdam  haurvatä  °r)tata  gäus huha  haomitnca para.haomamid Y.8.i;j.i, 4.1,  6.1T,  7.26.
5835:KompA.    —    Vgl.    aHt-n-.    —    ai.  vgl.  asihaii- vänl;    asihima-l-    Adj.  S)     —    Pü. :    ailömaaii, laaSmai-d.  —  ■)  Hds.  aslir.i'.  —  »)  Them.  An 2.  St.  Hds.  ast.ahc.  —  J)  Slveri.  unter  aa/ia-.-. —  4)  Hds.  ';üi!i.  -^  s)   Eine  E^oi   verfehlte Deutung  von  as/za»t-  MSL-  7.  356. •  j.  f,  g.),  p.  aspa-  m.;  j.,  g.  'aapä-,  aspi-  (?) f.  'Ross'>;  Rossstute':   ^räyj  *hai>im.asa- vatiS  .  .  gäusca    "pasca   haomasca   Y.ii.i; 2;  —  II  aniyahyä  -pä  (.\Pm.)  patiyanayam "dem  andern  (Teil)  liess  ich  Rosse  herzu- bringen"    Bh.  /.  18;     —     'pahe     kihrpa aurasahe  Yt.  8.  1 8,  /4.  9 ;  —  -pake  kjhrpa sämaht   Yx.8.z\;    ig.z<)\   —    "pauhB  .. tisaz-ö  ravö.frao^jmanS  Yt/7.12; —  aur- vatiiö  'pa  (als  AP.)  Yt.  10. 42;  —  'pa  (NP.)    . Yt /o.  20,  Aog.  Ä^  Yyl.2f};  —  äsyanha (sd.)    'pafibya   Y.57.  28;  —  yö   mqm  .  . 'paisu  paiti  pantata  (sd.)  Ytj.  50;  ig. 77;  —  harisaesu  paiti  'panqm  Yt;o.  11;
5972:mit  upa  i)  'hinzubringen':  yat  bäoa upäzatti'*  .  .  haomahe  . .  äasi-ar?  bailazsm "wo  man  ..  hinzubringt.."  Y. jo. 7;  — upaitayai'a  (s.  bes.).  a)  Akt  '(als  Strafe, Busse)  auferlegen,  bestimmen':  altahe paiti p»söJanuye  duye  satte  upazananam  upszSit spähe  astraya  "datihr  bestimme  man  ihm, der  ein  pi^öJatia  (sd.)  ist,  200  Strafen (d.  i.  Hiebe)  mit  der  Pferdepeitsche"  V. 4.20";  usw.S*.
6076:—  'sähe  paiti  mq^rfm  'sähe  paiti  fra-  manarihäY.4ß.  10;  —  '/ahya  yäsa  (sd.) sasiim  V.  4.  43  (s.  a);  —  'fa  i-iyaca  Vyt  a^m  Y.54.  i;  —ySais'sMt  nipSrfhi  (sd.) 75;  —  yS  'sili  hr>jyqsl>mS  (sd.)  R  /;  —  manasut  vohn  V.28.  11.  3)  im  jAwr.: airyamarum  isfm . ,  matistim  'saht  srava-  hs  aiwyiixsayatB  hadü  'Saia  vasträca  .  . tthqm  Y.54'3;  —  'iahe  myazdanqm  Vr.  Y.  3<?.  4;  —  yöi.äim  hanhana  (sd.)  'säca ^■3;  —  y^i  til/'rat  (sd.)  aurö  mainyus  frSriticaH.8.i; —  •/«lä""  nmtaahana.. dahlm 'sähe rauh fus  Yt.13.TT,  —  haoma..  yaorum  (sd.)  äste  V,4.45;  —  ahunm haÜTm^a  'sa/ie  xi'r  (sd.)  ahi  Y.  10.  4^  — \mazdqm   yS    'sähe    apanöJ?mS  yS    'sähe
6201:—  ^«M  jTvyqm  a°  usdätqm  Y.  22.  i;  — haoma  .  .  a'  usdata  a'  uzdahyamna  a' aiwi.vag'jayamna  Vr,(?.3;  3^^  Y.22.1;  — bansmanqmca  a'  */rashr^anqm  haoma- nqmca  a°  kutanqm  Vr. /2.3;  —  bar»sma . .  a'/rastar^fym  Y.2.1,  4~^,  /1.23,  V._j.i5, Ä14,  15,  Vyt2_3,Vr./i.  2;  io.  2;  —  bar)sma a'  aiwyasUm  Vyt  23;  —  yal  ba  paiti  .  . airihä  samS  naire  asaone  vprxyJi  a' daoaifi  V._J,  34".  a)  in  Verbindung mit  vanhuya  (sd.):  yat  na  kasvikamcina ya»huyanqm  .  .  naire  a/apne  jasia  a°  va- nhuya  riBij  daoaiti  V.  18.  $4;  28,  37,J-35'*;
6267:75.56,  FrW.7.i;  Y.J.2;  —  haomaheca..
6281:—  r3laca  vaauhi  .  .  °saane  (VS.)  V.  /(?. 19,  Vytjö;  S,  1.5,  2.5;  —  raziflam  astim ..  "saonJm  Yt.16.1,  4;  o,  20;  —  airyama- mm  iitm  '^avan^m  Vr.  24-  3 ;  —  kaomS °^ava  Y.p.a';  10,14;  —  haoma  °lava (als  Vok.)"'  duraosa  Y.  j/.  10;  —  rasmiö °lilum  Yt  J2. 7;  9; —  sraohm  .  .  '/avarum Y-  57-  2i  33,  Yt.  II. T,  —  Aaurvat3t>m 'savaram''^  asahe  ratüm  Y.  71.  12;  — am^ntät^m  "savanpm'i^  asahe  ratüm  Y.7J, 13;  —  ahura  müra  .  .  •s'avana  (AD.) Y.  2. 1 1 ;  YL  70. 14s;  —  ahuraHbya  miitraei- iya  '/avanaäiya  Y,  j.  11,  a)  bes.  von Ahura Mazääh:  3  äim  tä  vaca  rämayal ahurS  masdä  'sava  alavansm  zarä^ulinm V.5.2I;  jp.15  (statt  Akk.),  Y.7/.4,  5,  57. 24,  Yt.S.i,  11.1%  12.4,  16.3,  Yt/0.89, 7J.  14,  15;  —  ahur)m  mazdqm  'iavamm aiahe  ratüm  Y.2,2,    t6.\,  ^5.1,  7/.2,  4;
6311:•  j.  a^-vazah-  Adj.  'das  Aia  fördernd': haomahe  °zar>As  Y.  lO.  i,  8.^,  S.  /.  30,  Yt 20-0,  3.
6328:•  j.  aia.ratav-  m.  'üaiav  des  Asa,  heiligen Rechts':  haoma  pairiJiarisyaUe  mazäa.- xsä^ra  °lavS  V.  27.6.
6583:—  yet'ikh  vS  aisS  ultrSMäniS  anhal  V, '  (auch  mit  dat.  Inf.) ;  Bj  im  Aw, :  mahmai 75.24; —  am?^anqm  sp^ntanqm ..  yaEsqm\hyättt  *ava>ihl  Y.50.J;  —  s3raos5  ilä asti  hamtm  manB  Yty.Ss;  —  asit"^  sWastB  ahurahs  tnazds  yasnäiY.  ^6.\;  1—3, iaitn  y.i^a  apannSyliiaAe  V, /j,  44;  44*; ;  70.Ö,  Vr.p.  7,  15.2;    —    nil>ma  *haoma.-
6645:nJmanä  /i..Yt. 4.3;  —  katärS ..vikrkayl ^  -7-6;  —  yt  -  -  ^iw/J  anhat  ViVjayamnö jai:w3.tarS  aahm    V.jj.41,  Bii)    im  Yt.  75.52;  52'(?);  —  yöt  k»nH  haoma  .  .
6655:—  yadn  küö  aahat  yl.fyao'ianascä  ^-Si.  die  geistige  Welt  .  .  geschaffen  wurde"  Y. 16;  30.  j;  —  kJ  airyamä  . .  a»hai  Y.  49.  2.  19PÜZ.;  —  ysi  kmti  haoma  .  .  uzdlta 7;  —  tat  zT  hui  hussn»n  fsd.)  a»hal  Y.  .  .  uzdihyamna  (s.  o)  Vr.^.  3;  —  ya>a 5J.5;  —  hä  am  ahy3*magnis(sd.)  arfhai..  te  anlun  yasta  <T/J  FrW. /.  2.  PPA.: Y.44.i9i  19;  —  %wöi  as  *ärmaitif  "iicS  yd  hlm  (näml.  dasnani)  statqm  hitnm ä  gSus   tasä  (sd.)   as  ..    Y.j/.g;  J4.  8;  haitim  ttzpaint  haca   AinBiwy^  (sd.)  Yl
7133:fraiatimea  .  .  g}us  *vTmitim  N.  tf5(?);  — hat  drajo  haca  ''iirat . .  apat  . ,  baraimn /rast jiryiltV. 3.1(1;  17,  16.^,  l-J.a,;-^  aal tum  nisAioOis  apasca  .  .  yazimnö  'tarimca H.  2. 1 3 ;  —  (7/;»«  ä  va  °trpm  ä  vä  V.  7. *S;  5-37.  *.i04-io6,  Y.7.12,  2.12;  — '^/r  .  ,  aiwyö  V, /<S'.  70;  —  yoi  nmaiia hamiaräntaki  'trimca  bansmaca  tastaca haomaca  hävanaca  V.5,39;  40;-—  'trsm yaxaita  bansma  st}r>na3a  V.  12. 2 ;  J.  1 5, Vt.;2.3,  A.4.5,  Y.f?.s6.  b)  von  dem beim  Gottesdienst  (im  atas  dan  'Feuerbe- liäiter')**'  dämmenden  Feuer:  Hat  ätra- vaxsake  (sd.;  nämL  kairim  atthat)  yat '■tr>mca  aiwi.vaxsayät  ''^rasca  Hlr5  iiraxtis yaoida'^al  N.  Jj;  ffi;  —  aal  frahratarS Isd.)  yat    'Tirasca    alfqm    %raxlim  yaoz-
7857:frayazaite  . .  kahmaiHt  °zat)Aqm  biwivä Yt.  ry.  41;  —  ravasla  o^idrimla  (sd.)  . . aiaonö  stsil  'eas/a  dtäa'intiUa  . .  drvats stSisY.S.8; — yas/a  ml  ail^m  nanm  "zö <vi  avag>r?pt>m  ravöhu  paiti  uzbäraya£ 'imd  wer  den  .  .,  der  in  Gefangen- schaft verbracht  ist,  wieder  in  Freiheit versetzt"  V.  r<?.  10;  —  haoma  .,  yalcit ■zahu  dirilärihs  Jaininam  *upa  *d?rfzaAu (sd.)  Y.  io.17.  a)  liS.  'zaKAe  als  Inf.
7948:;  —  \  da/iyävc^  . .  <i'iar  °ml  dahyäv^ Bh.  7.7f.;  8;  —  nämSnTs  ..  'mä  nUminr/ Yti.j$f.;  —  l'maiy  9  xiäya'^iyä  adam agarbäyam  ti'tar  °mil  (APn.)  hamaraiiS "diese  (genannten)  9  Könige  habe  ich  in diesen  (bezeichneten)  Schlachten  gefangen genommen"  Bh.4-3.  2)  substantivisch, auf  einen  Satz  (,  direkte  Rede,  Aufzählung) : °mat  vS  SpB  jai'yani  "darum  (in  S  '  i) bitte  ich  euch,  ihr  Wasser"  Y. (jj.  12; 13",  Yt.4.3';  —  'mal  a^rff  äfri- <m  "so  (wie  vorher)  lautet  des  Feuers Segenswunsch"  Y.62.10;  —'^ya'^ä  °mt/' kasiyam  naiy  duruxlam  (sd.)  adam  akuna- Bh.^.  7 ;  —  II  °wa*  ly^  maitä  kartam par'iavaiy  "das  (wars),  was  ich  in  P.  tat" Bh,_y. 2;  4,  12,  2.15,  4-^;  —  in  Kon- gruenz mit  dem  Fraedikat:  1  'ma  dakySvJ^ lya  mann  paliyaila"  "das  (in  S  6)  sind die  Länder,  die  . ."  Bh.J.  7;  —  'nie  aste vala  yöi  hinti  ..  sna'ä^m  V.  fo.  16;  17; —  "mas)  U  haoma  gä%a  Y,  10. 18;  iS-J, i9(?).  a)  in  Verbindung  mit  la-,  a)  ad- jektivisch: *vlsqs  (sd.)  *l'lca  °ma  niJmJnls parslasca  .  .  vTsante  Yt. /.  19.  ß)    sub-
8560:•  j.  us«-fritay-  £  'Weihe,  feierliche  Dar- brlngung*:  yd  .  .  haomake  hutahe  daoätti 'tiiiam  (Gen.  part.  ab  Obj.)  vä  ntyezdinam V.  18. 1  z.
```


## [2026-09-14T01:58:01.923Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9595,9625p' HRN.txt; echo \"=== page markers ===\"; grep -n -- \"^- [0-9]\\{2,3\\} -\" HRN.txt | awk -F: '$1>9400 && $1<9800'"
}
```


### [2026-09-14T01:58:03.045Z] TOOL RESULT

```
1112. {2)Jiö8 *Tod* (Vis und Rämin, Seite 82 Vers 13) 4).
aw. aosah' 'Tod'; phlv. hös, hösömand, ahös 'un-
sterblich (Men.).
Eigentum, das Vullers auf diese Weise seinen Büchern einverleibt hat.
Allerdings ist die Klaue des Löwen an sehr vielen Stellen auch ohne
Citat, dai>- Vullers übrigens gewiss nicht mala fide unterlassen hat,
deutlich zu erkennen. Die Lesung uner verbietet wohl die Etymologie.
M Vergl. Jacobi, KZ. 31, 315.
*) Sämmtliche Belege stammen von Herrn Prof. Nöldeke.
^) Ausführliche Angabe der Literatur pro und contra neuerdings
bei Johansson, BB. 18, 25.
*) Stellen aus dem Öähnärae bei Spiegel, Glossar, 368.- 249 —
4ll3. höm 'Haomastrauch, -pflanze*; vergl. hfun (d-majüH
. -^wo^ *Magierhaoma (eine nicht näher zu bestimmende
^^|j^' Pflanze, AM. 268).
'' aw. haowa-; phlv. hötn; ai. soma-.
bei. vergl. hörn (LW., 99).
V1114. Äe^ jemand, jemals*, mit Negation 'niemand, nichts;
ec (äähn. I, S. 4 Vers 59).
W^ Käs. K. Z. ec,
ap. *(tiva ~r ciy (Salemann, Mel. asiat. IX, 241);
phlv. ec bezw. hec (päz. hec, hSöi),
1115. herhud *Feuerpriester , herkede, hermend, {her *Feuer',
das man daraus erschlossen hat, ist aber bedenklich^).
aw. aeAlrapaiti' ; phlv. ehrpat (Inschriften), lierput,
herpatastän, herputlh bezw. erpat,
1116. lilrek, {^hereh?) 'Bockchen, Zickchen'.
ap. *yö*V7/ra- 'Jährling (Tomas chek, Centralasiat.
Studien II, 766).
si/n. yirk 'ausgewachsenes , männliches Schaaf,
Zuchtwidder.
=== page markers ===
```


## [2026-09-14T01:58:08.552Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && ls; grep -c \"\" BQT_v4_pages.txt BQT_v5_pages.txt BQT_v3_pages.txt 2>/dev/null"
}
```


### [2026-09-14T01:58:08.618Z] TOOL RESULT

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
BQT_v5_pages.txt:10090
BQT_v4_pages.txt:22553
BQT_v3_pages.txt:51425
```


## [2026-09-14T01:58:09.227Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"سوپ\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-14T01:58:09.320Z] TOOL RESULT

```
MON_part2.txt:32320:سوپ‌خوری سرکه و دو سیر قندداغ داخل 
MON_part2.txt:70664:ورزش بکار برند. میل سوپاپ: (مک.) 
MON_part2.txt:70672:است و عملش باز و بستن سوپاپ‌ها است به 
MON_part2.txt:78401:کمپوت است و پس از مدتی شیر و سوپ به 
MON_part2.txt:85609:تهیه شود و آن را در سوپ و آش بکار 
MON_part1.txt:23855:خوردن غذاهایی مانند سوپ بکار رود. 
MON_part1.txt:62812:پخته و سوپ رقیقی تهیه کرده و خورند. 
MON_part1.txt:76324:گیسوی خود را در آن نهند؛ گیسوپوش. 
MON_part1.txt:80830:سوپ: : 5۱0 (.) آب‌گوشت سبزی و 
MON_part1.txt:80834:سوپاپ: ۲ (۱.) (مگ.) پولکی که روی
```


## [2026-09-14T01:58:14.288Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '80825,80840p' MON_part1.txt; echo \"=== page tags near ===\"; grep -n \"\\[pdf page\\|^\\f\\|صفحه\" MON_part1.txt | awk -F: '$1>80500 && $1<81000' | head"
}
```


### [2026-09-14T01:58:15.381Z] TOOL RESULT

```
و حشم. (مل.)باج‌هایی که بصورت هدایا 
گرفته می‌شده (ایلخانان). 

سواری گرفتن: 0 (سصل.) 
(عم.) دیگری را به نفع خود به کار کشیدن. 
سوپ: : 5۱0 (.) آب‌گوشت سبزی و 
حبوب» آشی رقیق شبیه شوربا و آن شامل 
انواع متعد‌د است؛. 

سوپاپ: ۲ (۱.) (مگ.) پولکی که روی 
دهانة دریچه‌های سرسیلندر قرار گرفته و 
دریچه‌ها را سد می‌کند. اگر این پولک از 
بالا و روی رس تال وم سور آن را 
(سوپاپ از رو) و اگر در بدنة سرسیلندر 
واقع شود وی را (سوپاپ از زیر) گویند. در 
هر سیلندر دو سوپاپ وجود دارد: یکی 
=== page tags near ===
```


## [2026-09-14T01:58:21.201Z] TOOL CALL #22: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2398 2>&1 | head -60"
}
```


### [2026-09-14T01:58:29.852Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 481; check the printed number and re-run with --pdf-page if off)
REF: BQT:2398  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 481  OCR-lang: fas

حولس -۸ ۳۹
وییم باشد۹ ۰ اصب کنند تاآب برآن خورده بگردش در آید
هو لس؟ - بلاپوسی‌بی‌شله وحر کت | وبفتح اول آبلةٌ دست وپارا گوبند۴ - ویممنی
غیرمعلوم» جالرا کویند وبمریی روح خوانشد .| اهلاکت هم بنظن آمده است۴ - ومویز را لیز
هولشك < بنم اور وکر نات گفته اند۴ که انگور خشغك شده باشد .
وسکون شین نقطه دار وکاف» هردم کثیف‌ونکیتی هولی < بفتح اولوسکون نالی وثالث
راگویند- وشخسی که پیوسته رخت‌خودرا ملورن | بتختاای کشیده .کره اسبی را کوبند که هنوز
گرداف . زین برپشت‌اوننپاده باشندگ - وبهندی‌پممنی(۱)
ولا - بنم اون با تانی مجهول بر آهته وهموار باشد - و بضم اول هم در هندی
وزن كوچك. جوزبازی و گردکان بازی‌راکوبنی, | لام عیدی وجشنی است .
وبستی کردون بازیرا گفته اند وآن چرخی باشد هوم! < بروزن موم » لام مردی است
که طفلان ازچوب وخلاشه سازند وبرآب روان | ازآل فربدون واو پیوسته درویرانها بسربردی ۰
() چش: - بمعنی .
۱- (عر) «هول , بالفتح » ترس - کاربیمناك که راه آن دربافته نشود : اهوال و عوول
جمم.» «منتهی آلارب». .۰ - ظاهرکلمه پوتانی نماید. دربونانی8908 بمعنی‌روج است .
ر: (0:000287 0۳۲6۵( ۳۵819 ,۷۵۵۵۵۵۶6۵ .6 .8
۴ - «هولك نفت (نقطه. دهغدا) وخلاك نیز بود شاعن گوید:
چو هولك بر دو چشم دلبر افتاد درون آمد ز پا آن سرو آژاد :
«لمت فری ص ۰.6۳۰۷۲
۴ - «حولك دیگر موبز بود. صیدلای گوید:
چو روشن شد انگور همچون چراغ بکردند انگور هولك بباغ . »
«لفت فری ص۳۹۳ .
- دراراك (سلطان آباد) بهمي معنی مسطلح است ولیز فحش است و در مقام سرزاش
و توییخ بئوکر وخانه شا کرد که کاری را خوب انجام نداده باشد کوبند : * چرا مثل عولی کار
کرده‌ای؟» «مکی نژاد». ‎٩‏ - هرن کلمه را درفارسی13۵77 شبط کرده و هوبشمان 130۳0
آورده گوید که درشمر با «بوم» قافیه آورده شده «اسشق - هوبشمان۱۱۱۳*؛ [رك : م۲۸۰۰ ح
اشمار فردوسی ] اسح تلفظ اول است . در ساسکریت 507718 » دراوستا 1801822 ۰ درپهلوی
۵( قس: بلوچی 8۵70 «اسشق ۱۱۱۳ نام گیاهیست زرد رنگه دارای گرههای نرديك بهم .۰
این گیاه کوهستانی دارای ساقةٌ درم وپرالیاشست وغیره‌ای سپید براگه شیر دارد. طبق آزمایشهای
دکنر اتکینن ۸۵۸11۵18800 .۳ و دمکنم ۸1۵006060 38.06 (رئیس -ابق هیشت
حفاران فراسوی در خوش ) گیاه مزبور همان ۷۷188۲15 نبا تن 1 است که عصاره اش بنام
0 (فر ) دراطب بکار میرود . در افغاستان « هوم » به « ربوای > اطلاق میشو د که
بگیاه مورد بحك ربطی ندارد . آربائیان قدیم گیاه مزبور را مقدی میدانتند و عمارة آنرا
خیجواندند بحدی که دارای رنگه شود. وبرآن بودند که شره آن روح ر1 فرح می بشدد. این
نوشایه خدابان‌را قوی دل ومصرور. وحی جنگجوبیآ نانرا تهییج‌میکند. مخصوضاً ابندره1804۳8
(رب النوع رعد) ازین مسکر بسیار میآشامد وپس ازآن هیج فوه‌ای قادرلیست دربرابر اومقاومت
ورزد . استه‌مال مایع هزبور درموقع قربانی یکی از کهن نربن رسوم عبادت آربایی است . این
بقیه در صفحه بمد
```


## [2026-09-14T01:58:40.182Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hauma\\|haumavarga\\|hu- 'press\\|press\" KNT.txt | head -20"
}
```


### [2026-09-14T01:58:40.237Z] TOOL RESULT

```
61:reproduced on pages 12 and 215. My grateful appreciation is also expressed to those numerous frends who during the preparation of the vol- ume have shown their interest in it and have urged that it be completed without undue delay. My special thanks are extended to Dr. Erich F. Schmidt, leader of The Persepolis Expedition sponsored jointly by the Oriental Institute of the University of Chicago, the Boston Museum of Fine Arts, and the University Museum in Philadelphia, for generous permission to include new texts found by The Expedition and to use the evidence of The Expedition’s photographs of inscriptions already known as well as of those newly discovered. This indebtedness is acknowl- edged in many places, not infrequently being made by the statement that data have been fur- nished by Dr. Schmidt or by Dr. George G. Cam- eron, formerly his colleague at the Oriental In- stitute, and now Chairman of the Department of Near Eastern Studies at the University of Mich- igan. Dr. Cameron has for years given me in every way the benefit of his direct acquaintance with the inscriptions and of his rich scholarship, and recently has transmitted to me the chief results of his examination in 1948 of the Behistan Inscription, with permission to use them although he had himself as yet not placed them in printed form before the public; to him, for all these favors, my profound gratitude is here expressed, though any such expression must needs fall far short of his deserts.
62:Finally, my unending thanks are here given to a small group of those who have studied with me, who—when the American Oriental Society found that it did not have at its command funds adequate to publish the volume—undertook to secure the financial support necessary to see it through the press, and carried their plan through to successful completion: Ruth Lilienthal Pearce, Alfred Senn, Maria Wilkins Smith, Е. A. Speiser.
66:of press of work, delegated the task of proofread- grateful to any reader who sends me a list of ing in his stead. Her repeated skillful readings such misprints and errors as he may discover. caught numerous misprints that had escaped R.G. К. me; yet with all our care I dare not think that Wynnewood, Pa.,
412:$3. Tne ScmrPr or THE Or» Persian IN- SCRIPTIONS 18, a8 we have said, of the cuneiform type: that is, the characters are made of strokes Which can be impressed on soft materials by a stylus having an angled end. The OP inscrip- tions, being on hard materials, must have been made with engraving tools with which the strokes
413:impressed on soft materials were imitated. There was no tradition from antiquity as to the signifi- cance af the characters, nor was any OP inscrip- tion accompanied by a version in a previously known system of writing; modern scholars were therefore obliged to start from the very beginning in the task of decipherment.
584:By the Elam. writings: Атта (or Araza), Arbairé-, Armina, Asagaria, Paréava, Fravartis (also РЫ. fravartikdn), Margu&, Marduniya, -vard- in Ar- tavardiya, Vidafarna (also Av. хатто), Vidarna, Sparda, haumavargd: many of these confirmed also by Greek forms, ete.
1387:5111. OP Unwairren Меріл, Nasars. OP nasals were not, expressed in writing before stops and spirants (except m before enclitics, $39), but the presence of the sounds is indicated by the transliterations ito other languages, or by the evidence of etymological comparisons. Ka"pa*da a district in Media, Elam, qa-um-
1461:IV. The writing Аи was normal for hau, as in haus, hauvam, haumavarga-, Vahauka-, but was not used for hu; to express hu, with vocalic u, the single character u was used, and to express hus for hy (from sy), u was written—the А being omitted in both situations:
1619:-iya- in the interior of words > -i-, see $23.T. The view has been expressed that À was lost
1631:For the sequence #0 there are some wrong writings in XPh: ahame = йМїт for ah*m* = Gham ‘I was’, атой = ahanty for *ah*an*iy = *ahüniy ‘may I be’, (gen.) амттг% а = Aura- mazdaha (4 occurrences; also twice in XPf) for -d"ah* = -dàha or -d'ahea = -dähã; but these miswritings, some of them probably explainable (852, 558, $222.1), do not controvert the views expressed above.
1698:The origins of OP sounds, as expressed in the normalized transcription, may be traced from the
1776:І. Attached to a verbal root, the ablaut grade of the root varying: kara- in compounds, u-céra-, küma-, Катёа-, gausa-, raga-, adv. daríam, drauga-, baga-, bara- and bāra- in compounds, zana- in compounds; less certain formations in d-baha- in daha-vaja, casa-, U-t&na-, u-tava-, gara- in batu-gara-, Vi-vdna-, varga- in hauma-varga-.
1786:Passives: ha™-dugd- ‘im-pressed’ = ‘inscription’; pati-kara- ‘made thereto’ = ‘sculptured figure’; asa-bara- ‘horse-borne’.
1805:Expressing place: apa-dd-na-, daiva-di-na-, à- yada-na-, fem. us-tasa-nd-, d-vaha-na-, std-na-, varda-na-.
1806:Expressing abstracts (actions): fem. fra-má-nà-, loc. adv. aS-naiy, adj. *u-rada-na-, yà-na-, vaš- na-, ham-ara-na-; possibly fem. Patt-graba-né-, becoming a place-name.
1807:Expressing concretes: arja-na-, fem. stü-nà-, fem. hai-nà-.
1808:Expressing adjectival actor, as personal name: Vi- dar-na-; name of month, Vi-yaz-na-.
1820:1. Primary, in the following: dar-ma- in per- sonal name Upa-darma-, gar-ma- in month name Garma-pada-, fem. tau-mà-, ad]. taz-ma- in per- sonal names (see Lex.), hau-ma- in hauma-varga-. On dubious атат, see Lex.
1896:z5aca-püvan- ‘kingdom-protecting, satrap’; du- varði- (for *duvar-varði-) ‘doorway-covering, col- onnade’; hauma-varga-, maz-dah-, bátu-gara-, see Lex. s.vv.
2040:Nom. Pl. martiyd, z$ayatiyà, hamiciyd, anuštyā, takabard, tigrazaudà, haumavargà, paruva, Mada, Вока, Mudrüyà, Yauna, Uvjiya; with double
```


## [2026-09-14T01:58:43.393Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hauma-varga-\\|haumavarga-\\s*:\" KNT.txt | tail -10; echo ===; grep -n \"Skt. su\\|sunoti\\|soma\" KNT.txt | head"
}
```


### [2026-09-14T01:58:43.472Z] TOOL RESULT

```
Exit code 1
1776:І. Attached to a verbal root, the ablaut grade of the root varying: kara- in compounds, u-céra-, küma-, Катёа-, gausa-, raga-, adv. daríam, drauga-, baga-, bara- and bāra- in compounds, zana- in compounds; less certain formations in d-baha- in daha-vaja, casa-, U-t&na-, u-tava-, gara- in batu-gara-, Vi-vdna-, varga- in hauma-varga-.
1820:1. Primary, in the following: dar-ma- in per- sonal name Upa-darma-, gar-ma- in month name Garma-pada-, fem. tau-mà-, ad]. taz-ma- in per- sonal names (see Lex.), hau-ma- in hauma-varga-. On dubious атат, see Lex.
1896:z5aca-püvan- ‘kingdom-protecting, satrap’; du- varði- (for *duvar-varði-) ‘doorway-covering, col- onnade’; hauma-varga-, maz-dah-, bátu-gara-, see Lex. s.vv.
(eval):1: == not found
```


## [2026-09-14T01:58:45.388Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"haumavarga\" KNT.txt | sed -n 1,20p | cut -c1-400"
}
```


### [2026-09-14T01:58:45.465Z] TOOL RESULT

```
1461:IV. The writing Аи was normal for hau, as in haus, hauvam, haumavarga-, Vahauka-, but was not used for hu; to express hu, with vocalic u, the single character u was used, and to express hus for hy (from sy), u was written—the А being omitted in both situations:
4581:26 Katpatuka : Daha : Saka : haumavarga : Saka
4740:Notes то А?Р: 4 @ataguiya Smith, Hz.; if correct, for Galaguviya; or a wrong writing for Satagudaya or 8atagudiya, cf. Gk. Larraybdar, 4 There із an extra verti- cal hasta between the g* and the a in haumavarga. ? imy*, miswritten for илт,
```


## [2026-09-14T01:58:49.671Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Av\\. haoma\\|Skt\\. soma\\|soma-\" KNT.txt | head; echo \"---211---\"; grep -n \"^211$\\|^ *211 *$\" KNT.txt | head"
}
```


### [2026-09-14T01:58:51.392Z] TOOL RESULT

```
---211---
```


## [2026-09-14T01:58:54.554Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hauma\" KNT.txt | wc -l; grep -n \"LEXICON\\|Lexicon\" KNT.txt | tail -5; tail -c 300 KNT.txt; echo; grep -n \"haruva\\|hamaranam\\|haxâmanis\\|Haxāmaniš\" KNT.txt | tail -5"
}
```


### [2026-09-14T01:58:54.644Z] TOOL RESULT

```
13
5678:LEXICON
5712:LEXICON 199
5744:LEXICON
5783:LEXICON 203
5833:LEXICON | 205
arch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
4203:1 adam : Dàrayavau 2 $:xSdyafiya 3 : vagraka : xSaya 4 буа : xšāyaði 5 yanim : xSdya 6 (ya : dahyünà 7 m : xSdyablya : '8 haruvahyáàya : 9 bümiyà : Vist 10 àspahy& : puça ll : Haxāmanišiya TRANSLATION OF DSb: Iam ... (= DPa 1-4), King in all the earth, ... (= DPe 4-5).
4247:15 m : XSyam : akunau’ : ahyyà : BUyà : ‚ Auramazd 16 dm : плада : Ката : ha : haruvahyaya : BUya : mar 17 йат : mim : avarnavalé / mam : XSyam : akunaus : 18 haruahüyà : BUyà г adam : Auramazdàm : ayadaty : 19 Auramazdamaiy : upastām : abara ; ; tyamaiy : : fram - 20 álam : cartanaty : ava : исйтатайу : akunaus : t
4430:2 üvnàm : Vistispahya : puça : Haxāmanišiya :
4481:XPc = XERXES, PERSEPOLIS C. 1 Бара : vazraka : Auramazda : hya : пойт : bümim : 2 ада : hya : avam : asmànam : ada : һуа : marti 3 yam : ada : һуа : Siyátim ; ada : martiyahyà 4 : һуа : Xšayāršām : XS8m : akunaus : aivam : pa 5 rūnām : XSm : aivam : pariinam : framátàram 6 :adam : XSayarsa : XS : vazraka : XŠ : XSanam : XS: 7 dahyünàm : paruv : zandndm : XS : аһуйуй : b 8 ümiyà : vazrakiya : düraiy : apiy : Darayava 9 haus : XShya : puça : Haxāmanišiya : 6atiy : X 10 šayāršā : XS : vazraka : vašnā : Aurahya Mazdaha : i 11 ma ; hadis : Dárayavaus : XS : akunaus : hya : manā : 12 pità : mim : Auramazda : pátuv : hada : baga 13 ibis : utd : tyamaty : kartam : uta : tyamaiy : 14 pica : Darayavahau’ : XShyá : камат : avaSely 15 : Auramazda : pátuv : hada : bagaibis
5713:fraharavam, phrasal adverb ($191.]II), ‘in all’: fra- ($1401) + asn. haravam with variant orthography ($22, $26), to haruva-. DB 1.17.
```


## [2026-09-14T01:58:58.438Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"LEXICON 21\\|LEXICON 209\\|LEXICON 213\" KNT.txt | head; echo ===; grep -n \"hauma-varga\\|hauma-\\|Sacae\\|Amyrgian\" KNT.txt | sed -n 1,30p | cut -c1-250"
}
```


### [2026-09-14T01:58:58.750Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-14T01:59:00.156Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"LEXICON\" KNT.txt | tail -20"
}
```


### [2026-09-14T01:59:00.210Z] TOOL RESULT

```
4971:LEXICON
5017:LEXICON
5062:LEXICON
5105:LEXICON
5153:LEXICON
5201:LEXICON
5246:LEXICON
5305:LEXICON
5351:LEXICON
5403:LEXICON
5448:LEXICON
5504:LEXICON
5546:LEXICON
5589:LEXICON
5636:LEXICON 195
5678:LEXICON
5712:LEXICON 199
5744:LEXICON
5783:LEXICON 203
5833:LEXICON | 205
```


## [2026-09-14T01:59:04.167Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>5833' KNT.txt | grep -n \"hauma\\|hau-\\|Skt. su\" | cut -c1-500"
}
```


### [2026-09-14T01:59:05.162Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:59:06.964Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>5833' KNT.txt | grep -n \"hau\" | cut -c1-300 | head -20; echo \"=== total lines ===\"; wc -l KNT.txt"
}
```


### [2026-09-14T01:59:07.991Z] TOOL RESULT

```
33:vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
=== total lines ===
5868 KNT.txt
```


## [2026-09-14T01:59:14.979Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"haruva- adj\\|haruva-\\b\" KNT.txt | cut -c1-200 | head; echo ===; grep -n \"hakaram\\|hacā\\|hadā\\|hainā\\|haina-\" KNT.txt | cut -c1-160 | head"
}
```


### [2026-09-14T01:59:15.076Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-14T01:59:16.739Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5700,5740p' KNT.txt | cut -c1-300"
}
```


### [2026-09-14T01:59:16.800Z] TOOL RESULT

```
frafara- adj. ‘superior’: fra- + variant com- par. suffix -thara- seen in Av. fraéara- ($1491, 6190.11; Wb. ЖА 41.319; Bv. 33.2.150-1, 34.1.33-4, Hz. AMI 4.126-7, 8.3940, ApI 166-7), cf. superl. -thama- in Skt. prathamd- ‘first’. Cf. also uradara-. — fra&aram asn. XPf 26f, 37.
Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-ra-da, АКК. pa-ra-da-’ ; perhaps thematic noun- stem (§141) to fra- + *dà-, with vriddhi ($126), cf. Av. früd- ‘to further, increase’ (ТИМ. AiW 1012), but more probably hypocoristie to a com- pound name ($164.П1; Bthl. AiW 1018) of
framatar- sb. ‘master, lord’ (‘giver of judicial decisions’, ace. to Hz. ApI 150-4): fra- + root mā- + agent suffix -tar- (5154.1). framatéram asm. (§124.VI, $1861) DNa 7f; DSe 7; DSf 5; DE 11; XPa 5; XPb 11; XPe 5; XPd 8; ХР? 7f; XPh 6; XE 11; XV 9; A'Pa 8°; A?He 7. frama- ібгат 
framána- sb. ‘command’ (judgment, deci- sion’, acc. to Hz. ApI 144-50): РЫ. framán, NPers.
OLD PERSIAN
fürmán; fra- + mä- + suffix -nà- ($128, $1471), ef. Skt. pramána-m ‘measure, standard’. — framánà nsf. DNa 57; DNb 28; DSj 3°, framánáyà isf. DNb 37.
fravata adv. ‘forward, downward’: Phl. frót, NPers. fáród јато; from *frava-, extension of fra- as in Gk. rpõros ‘first’ from *proya-, + -tos as in amata (§191.1I; JAOS 51.204, 53.15; Bv. BSLP 30.1.59; hardly with Kénig, Burgbau 51; not identical with Skt. isf. pravátà ‘downhil
Frovartz- sb. ‘Phraortes’, a Median rebel: Elam. pir-ru-mar-t-18, Akk. pa-ar-ti-mar-ti-1§ Gk. Ppadprys: identical either with Av. frava&i- ‘guar- dian angel, soul’, from fra- + var- ‘protect’ + -ti- (S31, 8152.11) as ‘Protection’, or with Av. fraoroti- "Siehbekennen zu’, from fra-
fras- vb., see јтаб-.
fraša- adj. ‘excellent’ (‘tauglich’, König Burg- bau 48, Brd. АКМ 39.87): Av. frasa- ‘directed toward, useful’, formed on adv. fraša to frünk-, Skt. adv. praca to ртайс-, from pra- + añe- (Bthl. AiW 1006-7); the irregular -3- for -s- of Sy- may be a contamination of *frasa- 
frašta DSa 5, DS] 6: discussed by Bv. ВІР 30.1.63-4, Gr. $103, Gray AJP 53.67, Brd. WZKM 39.20-1; but fra$am @adaydlary and not frašta ðadayämaiy ($54.11) should be read in both pas- sages (Hz. AMI 3.9-10, ApI 156-8). See under frasa-.
(mu. em lere Am ee шшш. ште у. mi ease e +
LEXICON 199
fraharavam, phrasal adverb ($191.]II), ‘in all’: fra- ($1401) + asn. haravam with variant orthography ($22, $26), to haruva-. DB 1.17.
. baug- vb. ‘free’: Av. baog-, NPers. boxtén; in Attydbausna-, Bagabuxsa-.
Düxtri- sb. ‘Bactria’, a province of the Persian Empire: Elam. ba-ak-&-18, ba-ik-tur-ri-i$, Akk. ba-ah-tar, Gk. (nt. pl) Béxrpa (§9.1, $79, 6103.111). OP %-stem, for older 7-stem (8152.II), seen in Av. báxói. — Büziri$ nsf. DB 1.16; DPe 16; DNa 23; DSe 22°; D8m 9°; XPh 21. Ваг- triy
bag- vb., see under baga-, bàji-.
baga- sb. ‘god’: Av. baga- ‘lot, good fortune’, Skt. bhdga- ‘dispenser (of good fortune)’, Gk. -paryos ‘eater’, OCS bogi ‘god’, pIE *bhago- ($101, $122, 5143.1, V, VI); ef. Hz. ApI 105-10. See also Bagábigna-, Bagabuxsa-, Bagayddi-, bà. рада nsm. AmH 6; AsH 6; DNa 1; DNb 1
Bagábigna- sb. ‘Bagabigna’, a Persian, father of Hydarnes: Elam. ba-qa-pi-ig-na; from baga- ‘sod’ + d-bigna-, pte. in -na- of an unidentified verbal root, cf. perhaps Skt. bija-m ‘seed’ (575.1, $103.IV, $160.Ie, $243). Baglalbignah{ya} gsm. DB 4.84f.
Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithra
‘(Month of) Mithras’ (Justi, ZDMG 51.247; Bthl. AiW 952-3). Bágayádait gsm. DB 1.55.
bàji- sb. ‘tribute’: NPers. Баг; deriv. (§152.1, $165) of root seen in Skt. bhdga- ‘portion, dis- penser’, OP baga- ‘god’, the verb being Skt. bhájatt ‘apportions’, Av. bag-, РЫ. bäztän (§101, $122, $128, $126). Балт asf. DB 1.19; DPe 9; DNa 19; DSe 18; XPh 17.
batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devou
ba*d- vb. ‘hind’: Av. band-, Skt. bandh-, Gt. bindan, pIE *bhendh-. See also badaka-. basta (NPers. bäst) nsm. past pte. pass. (867, $85, 5120, $122, 5182.1, 52421) DB. 1.82; 2.75, 90; 5.26. basta apm. DB 3.88".
ba"daka- sb. ‘subject, servant’ (cf. König, Кыр 64): Phi. bandak, NPers. bändäh; deriv. (§146.1T) of OP *ba"da- ‘bond, fetter’, Av. banda-, Skt. bandhd-, to pIE root *bhendh- (OP ba"d-; $39, $75.11, $111, §122, 8132.1). badaka пет. DB 2.20, 30, 49f, 82; 3.13, 31, 56, 85; 5.8. bada
Bábiru- sb. (Babairu- because of Pali Báveru-, MB Gr. $80) ‘Babylon’, a city (S56.III, $166); ‘Babylonia’, a province of the Persian Empire; by transfer, ‘Babylonian’: Elam. ba-pi-li, Akk. bab-ilu, bab-ilàni ‘gate of the god(s)’, Gk. Вав (§75.V, $107). See also Babirwiya-. Bah
200 OLD PERSIAN
2.5, 6; 3.79, 88, 92; 4.2; DBd 7f; DBi 11 (written Bab*raw, $22); DSf 33 as loc. with усій, 33 as abl. with Ласа (hardly a real abl., corresponding to Av. -aut despite Hz. AMI 3.55n, Kent ЈАО 53.16).
Bābirwiya- adj. ‘Babylonian’: deriv. ($144.- ПТ) to preceding. — Bábiruviya nsm. DB 1.77, 79; 8.81; 4.13; DSf 20. Babiruviyam asm. DB 3.86. Babiruviyé npm. DB 3.78; DSf 53f. Bäbiruviyä apm. DB 3.88.
bar- vb. ‘bear, lift up, esteem’: present stem bara-, Av. батат, N Pers. bard, Skt. bhárati, Gk. dpa, Lt. fert, Gt. batrip, pIE *bhere/o- (8213). See also ubarta-, uSabdri-, Gaubaruva-, bara-. bara^tiy 3d pl. ($122, 5232.1) DB 5.22f (written berety, 522); DNa 42. abaram Ist sg. imf. ($61, 
à + bar- ‘perform’: dbaratiy ($218, $228.1) DNb 25. Cf. also Hz. Ар] 110-1, who refers to à-bar- certain other forms listed above as augmented forms of uncompounded bar-.
pati- + à + bar- ‘bring back, restore’: райуй- baram Ist sg. imf. DB 1.68 (but -à- perhaps only by influence of pardbartam, JAOS 62.275; 558, $206c).
para + bar- ‘bear away, take-away’: pardbara imf. DB 1.71, 96. pardbartam nsn. past pte. pass. (§242.1) DB 1.62, 67f.
pari- + bar- ‘protect, preserve’ (cf. Hz. Ар 112-3): paribarümiy Ist sg. (8226.]) DNb 17. paribarühy 2d sg. subj. ($27, $136, §222.IT, 4227.1) DB 4.78; paribaráh*-di$ (827, etc.) DB 4.74. pari- barā 2d sg. imv. (5237.1) DB 4.72, 88.
fra- + bar- ‘proffer, grant’: frábara imf. AmH 7; AsH 9; DB 1.12, 25, 60; DPd 3f, 7f; DPh 8; DNa 33; DSf 11; DSm 3°; DSp 2°; D8s 6; DZc 4; DH 7; A’He 18f, 20.
bara- sb. ‘bearmg, bearer’: Av. -bara-, Skt. -bhara-, Gk. -фороѕ, pIE "bhoros ($32, $122, $1431, ҮТ), to root bar- ‘bear’, in aritibara-, takabara-, vacabara-; also bāra- ‘borne by, rider of’, with vriddhi (8122, $126, 5148.1), in asabdra-, ef, usabüri-. See Hz. Ар] 95.
bard- vb. ‘be high’: Ау, baraz- ‘high’, baraz- ant- ‘lofty’, NPers. burz ‘high’, Skt. brhánt- ‘lofty’, OHG berg ‘mountain’, pIE *bhergh-; in Bardiya-, barsan-, probably in brazman-.
Bardiya- sb. Smerdis’, brother of Cambyses ($16411): Elam. bir-h-ia, АКК. bar-zi-ia, Gk. Урёрӧ ($29.02, $30). Репу. (§144.1V) of OP bard- ‘be high’ (575.11): ‘The Exalted’. Bardiya пет. DB 1.30, 32, 39, 52f; 3.25, 35, 54; 4.9, 27, 82; DBb 4f; DBh 5. Bardiyam asm. DB 1.31 bi
barSan- sb. ‘height, depth’ (S81): Av. barazan- .
(ВМ. AiW 950); deriv. of OP bard- (575.1, $155.1; Scheil 21.26; Konig, Burgbau 51; Hz. AMI 3.57; Bv. Gr. $812; Kent, JAOS 51.204, 99.15). bar$nà ism. (806, $120) DSf 26, 26f.
```


## [2026-09-14T01:59:41.637Z] TOOL CALL #34: Bash

```json
{
 "command": "sed -n 1,60p tools/fetch_source.py"
}
```


### [2026-09-14T01:59:41.915Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-14T01:59:52.656Z] TOOL CALL #35: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/haoma\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%D9%88%D9%85\" \\\n \"https://en.wiktionary.org/wiki/soup\" \\\n \"https://www.etymonline.com/word/soup\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D9%BE\" \\\n \"https://en.wiktionary.org/wiki/son\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 448, Seu roots (haoma/soup/son)\" ; done"
}
```


## [2026-09-14T01:59:54.662Z] TOOL CALL #36: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/seethe\" \\\n \"https://www.etymonline.com/word/seethe\" \\\n \"https://www.etymonline.com/word/sod\" \\\n \"https://en.wiktionary.org/wiki/suck\" \\\n \"https://en.wiktionary.org/wiki/soak\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/sunuz\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 448, Seu roots (seethe/sod/suck/soak/son)\" ; done"
}
```


### [2026-09-14T01:59:57.781Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ad8c08a3b16133d6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eda8b5f62296c071.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35c688151591d051.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/094f030aa7bbdc58.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd7159645262468a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7c18575ee9525e6a.txt
```


### [2026-09-14T02:00:03.084Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4f329c535914cdbc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8fc6ad3e18d646c0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/55977f0c7fc82056.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0980d493c44f2c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fc1bdc6dc73ba27c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4cf0f421969df83f.txt
```


## [2026-09-14T02:00:05.049Z] TOOL CALL #37: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"### haoma\"; grep -n -A6 -i \"Avestan.*haoma\\|From Proto-Iranian\\|Proto-Indo-Iranian\" ad8c08a3b16133d6.txt | head -40"
}
```


### [2026-09-14T02:00:05.104Z] TOOL RESULT

```
### haoma
158: Transliteration of Avestan 𐬵𐬀𐬊𐬨𐬀 ( haoma ) . Doublet of soma .
159-
160- Noun
161- [ edit ] 
162-
163- haoma ( uncountable ) 
164-
--
178: Avestan: 𐬵𐬀𐬊𐬨𐬀 ( haoma ) 
179-
180- Finnish: haoma , homa 
181-
182- Persian: هوم   (fa) ( hum ) 
183- Middle Persian: hwm ( hōm ) 
184-
```


## [2026-09-14T02:00:06.861Z] TOOL CALL #38: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"### هوم fa\"; grep -n -i -B3 -A10 \"Persian\" eda8b5f62296c071.txt | head -60"
}
```


### [2026-09-14T02:00:06.957Z] TOOL RESULT

```
### هوم fa
```


## [2026-09-14T02:00:09.213Z] TOOL CALL #39: Bash

```json
{
 "command": "cd data/verification/sources/web && wc -c eda8b5f62296c071.txt cd7159645262468a.txt; sed -n 1,60p eda8b5f62296c071.txt"
}
```


### [2026-09-14T02:00:09.291Z] TOOL RESULT

```
3470 eda8b5f62296c071.txt
3322 cd7159645262468a.txt
6792 total
URL: https://en.wiktionary.org/wiki/%D9%87%D9%88%D9%85
FETCHED: 2026-09-14T01:59:55Z
STATUS: 200
TITLE: هوم - Wiktionary, the free dictionary

هوم - Wiktionary, the free dictionary 

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
 Malay 

 Toggle Malay subsection
```


## [2026-09-14T02:00:13.977Z] TOOL CALL #40: Bash

```json
{
 "command": "cd data/verification/sources/web && sed -n 60,200p eda8b5f62296c071.txt; echo \"=====SUP=====\"; sed -n 55,140p cd7159645262468a.txt"
}
```


### [2026-09-14T02:00:14.037Z] TOOL RESULT

```
 1.1 
 Interjection 

 2 
 Moroccan Arabic 

 Toggle Moroccan Arabic subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Pronoun 

 2.3.1 
 See also 

 Toggle the table of contents 

 هوم 

 4 languages 

 فارسی 
 Magyar 
 Malagasy 
 Русский 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

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

 Malay
 [ edit ] 

 Interjection
 [ edit ] 

 هوم 

 Jawi spelling of hum .‎

 Moroccan Arabic
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Arabic هُمْ ( hum ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /huːm/ 

 Pronoun
 [ edit ] 

 هوم • ( hūm )  m or f 

 they ( masculine or feminine plural subject pronoun ) 
 Synonym: هوما ( hūma ) 

 See also
 [ edit ] 

 Moroccan Arabic personal pronouns

 1 st person

 آنا ( ʔāna ) , أنا ( ʔana ) 

 حنا ( ḥnā ) 

 2 nd person

 m 

 انت ( ntā ) , انتينا ( ntīna ) , انتين ( ntīn ) 

 انتوما ( ntūma ) , انتوم ( ntūm ) 

 f 

 انت ( ntī ) , انتينا ( ntīna ) , انتين ( ntīn ) 

 3 rd person

 m 
=====SUP=====

 1 
 Baluchi 

 Toggle Baluchi subsection 

 1.1 
 Alternative forms 

 1.2 
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 Toggle the table of contents 

 سوپ 

 14 languages 

 Deutsch 
 فارسی 
 Français 
 Hrvatski 
 Magyar 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Malagasy 
 Norsk bokmål 
 Polski 
 پښتو 
 Русский 
 中文 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link
```


## [2026-09-14T02:00:16.504Z] TOOL CALL #41: Bash

```json
{
 "command": "cd data/verification/sources/web && awk 'NR>140' cd7159645262468a.txt | sed -n 1,80p"
}
```


### [2026-09-14T02:00:17.486Z] TOOL RESULT

```
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

 See also: شوت , سوت , سوب , and سؤت 

 Baluchi
 [ edit ] 

 Alternative forms
 [ edit ] 

 سروپ ( sròp, srup ) 

 Etymology
 [ edit ] 

 Inherited from Proto-Iranian *cáywaH . Cognate with Persian سیب ( sib ) , Central Kurdish سێو ( sêw ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /soːp/ [soːp] 
 ( Iran ) IPA ( key ) : [sɯːp] 

 Noun
 [ edit ] 

 سوپ • ( sòp ) 

 apple 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from French soupe .

 Pronunciation
 [ edit ] 

 ( Iran ) IPA ( key ) : [suːpʰ] 

 Noun
 [ edit ] 

 سوپ • ( sup ) ( plural سوپ‌ها ) 

 soup 
 Synonym: آشامه ( âšâme ) 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=سوپ&oldid=92019887 "

 Categories : Baluchi terms inherited from Proto-Iranian 
 Baluchi terms derived from Proto-Iranian 
 Baluchi terms with IPA pronunciation 
 Baluchi lemmas 
 Baluchi nouns 
 bal:Fruits 
 Persian terms borrowed from French 
 Persian terms derived from French 
 Persian terms with IPA pronunciation 
 Persian lemmas
```


## [2026-09-14T02:00:21.323Z] TOOL CALL #42: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"### etymonline soup\"; grep -n -i -A12 \"soup (n.)\" 094f030aa7bbdc58.txt | head -40"
}
```


### [2026-09-14T02:00:21.378Z] TOOL RESULT

```
### etymonline soup
23: soup (n.) 
24-
25- "liquid food," 1650s, from French soupe "soup, broth" (13c.), from Late Latin suppa "bread soaked in broth," from a Germanic source (compare Middle Dutch sop "sop, broth"), from Proto-Germanic *sup- , from PIE *sub- , from root *seue- (2) "to take liquid" (see sup (v.2) and compare sop (n.)).
26-
27- Served usually before the meat or fish at a formal dinner, hence soup to nuts "everything" (1910), nuts being commonly served after the meal. Soup-kitchen , "public establishment supported by voluntary contributions, for preparing and serving soup to the poor at no cost" is attested from 1839. In Ireland, souper meant "Protestant clergyman seeking to make proselytes by dispensing soup in charity" (1854).
28- also from 1650s 
29-
30- soup (v.) 
31-
32: "increase the horsepower of an engine," 1921, probably from soup (n.) in slang sense of "narcotic injected into horses to make them run faster" (1911) and influenced by supercharge (v.). Related: Souped-up (1931).
33- also from 1921 
34-
35- Entries linking to soup 
36-
37- sop (n.) 
38-
39: Middle English soppe , "something soaked," from Old English sopp- "bread soaked in water, wine, milk, or some other liquid" (in soppcuppe "cup into which sops are put"), from Proto-Germanic *supp- , which is related to Old English verb suppan (see sup (v.2)) and probably reinforced by Old French soupe (see soup (n.)). The meaning "something given to appease" is from 1660s, a reference to the sops given by the Sibyl to distract Cerberus in the "Aeneid." Also "dull or foolish person" (1620s).
40-
41- sup (v.2) 
42-
43- "to sip, to take into the mouth with the lips, drink or swallow with small mouthfuls," Middle English soupen , from Old English supan (West Saxon), suppan , supian (Northumbrian) "sip, taste, drink, swallow" (strong verb, past tense seap , past participle sopen ).
44-
45- This is from Proto-Germanic *supanan (source also of Old Norse supa "to sip, drink," Middle Low German supen , Dutch zuipen "to drink, tipple," Old High German sufan , German saufen "to drink, booze"). The Germanic word is from PIE *sub- , possibly [Watkins] an extended form of the root *seue- (2) "to take liquid" (source also of Sanskrit sunoti "presses out juice," soma ; Avestan haoma , Persian hom "juice;" Greek huetos "rain," huein "to rain;" Latin sugere "to suck," succus "juice, sap;" Lithuanian sula "flowing sap;" Old Church Slavonic soku "sap," susati "suck;" Middle Irish suth "sap;" Old English seaw "sap").
46-
47- If this is correct, the two verbs sup are cognates out of Germanic, the other one via French. The noun meaning "a small quantity of liquid" is by 1560s.
48-
49- supercharge 
50- soupy 
51- See All Related Words (5)
```


## [2026-09-14T02:00:22.680Z] TOOL CALL #43: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"### wikt soup etym\"; grep -n -i -B2 -A8 \"Old French\\|Frankish\\|Proto-West Germanic\\|suppa\" 35c688151591d051.txt | head -60"
}
```


### [2026-09-14T02:00:22.741Z] TOOL RESULT

```
### wikt soup etym
284- Wikiquote 
285-
286: The noun is from Middle English soupe , sowpe , from Old French soupe , souppe , sope , from Late Latin suppa ( “ sopped bread ” ) , from Proto-Germanic *supô (compare Middle Dutch sope ( “ broth ” ) ). Doublet of sop and zuppa . See also sup and supper .
287-
288- The verb is from the noun. [ 1 ] 
289-
290- Noun
291- [ edit ] 
292-
293- soup ( countable and uncountable , plural soups ) 
294-
--
678- Indonesian: sup   (id) , sop   (id) 
679-
680: Interlingua: suppa 
681-
682- Irish: anraith   m 
683- Middle Irish: sésúr   m 
684- Old Irish: brothchán   m 
685-
686- Italian: minestra   (it)   f , brodo   (it)   m , zuppa   (it)   f 
687-
688- Japanese: 汁   (ja) ( しる, shiru ) , スープ   (ja) ( sūpu ) , 露   (ja) ( つゆ, tsuyu ) 
--
829- Shor: мӱн ( mün ) , мин ( min ) 
830-
831: Sicilian: suppa   (scn)   f , zuppa   (scn)   f 
832-
833- Silesian: zupa   f 
834-
835- Sinhalese: සුප් ( sup ) 
836-
837- Slovak: polievka   (sk)   f 
838-
839- Slovene: juha   (sl)   f 
--
1061- English terms inherited from Middle English 
1062- English terms derived from Middle English 
1063: English terms derived from Old French 
1064- English terms derived from Late Latin 
1065- English terms derived from Proto-Germanic 
1066- English doublets 
1067- English lemmas 
1068- English nouns 
1069- English uncountable nouns 
1070- English countable nouns 
1071- English terms with usage examples
```


## [2026-09-14T02:00:28.232Z] TOOL CALL #44: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"### etymonline seethe\"; sed -n '20,40p' 8fc6ad3e18d646c0.txt; echo; echo \"### etymonline sod\"; sed -n '20,40p' 55977f0c7fc82056.txt"
}
```


### [2026-09-14T02:00:28.317Z] TOOL RESULT

```
### etymonline seethe

 Origin and history of seethe 

 seethe (v.) 

 Middle English sethen , from Old English seoþan "to boil, be heated to the boiling point, prepare (food) by boiling," also figurative, "be troubled in mind, brood" (class II strong verb; past tense seaþ , past participle soden ), from Proto-Germanic *seuthan (source also of Old Norse sjoða , Old Frisian siatha , Dutch zieden , Old High German siodan , German sieden "to seethe"), from PIE root *seut- "to seethe, boil."

 Driven out of its literal meaning by boil (v.); it survives largely in metaphoric extensions. Of a liquid, "to rise, surge, or foam" without reference to heat, from 1530s. Figurative use, of persons or populations, "to be in a state of inward agitation" is recorded from 1580s (implied in seething ). It had transitive figurative uses in Old English, such as "to try by fire, to afflict with cares, be tossed about as in turbulent water." Now conjugated as a weak verb, its old past participle sodden (q.v.) is no longer felt as connected.

 Entries linking to seethe 

 boil (v.) 

 early 13c. (intransitive) "to bubble up, be in a state of ebullition," especially from heat, from Old French bolir "boil, bubble up, ferment, gush" (12c., Modern French bouillir ), from Latin bullire "to bubble, seethe," from PIE *beu- "to swell" (see bull (n.2)). The native word is seethe . The figurative sense, of passions, feelings, etc., "be in an agitated state" is from 1640s.

 I am impatient, and my blood boyls high. [Thomas Otway, "Alcibiades," 1675]

 The transitive sense "put into a boiling condition, cause to boil" is from early 14c. The noun is from mid-15c. as "an act of boiling," 1813 as "state of boiling." Related: Boiled ; boiling . Boiling point "temperature at which a liquid is converted into vapor" is recorded from 1773.

 sodden (adj.) 


### etymonline sod

 Origin and history of sod 

 sod (n.1) 

 "turf, slice of earth with grass on it," mid-15c., sodde , apparently from Middle Dutch sode "turf," or Middle Low German sode , both related to Old Frisian satha "sod" and all of uncertain origin. Perhaps the notion is water saturation and the group is related to sog . Colloquial the (old) sod "one's native country," especially if it is Ireland, is from 1812.
 also from mid-15c. 

 sod (n.2) 

 term of abuse, 1818, short for sodomite (also see sodomy ). British colloquial sod-all is attested from 1930.
 also from 1818 

 sod (v.1) 

 c. 1400, sodden , "to cover with sod," especially "put in a grave," from sod (n.). Related: Sodded ; sodding .
 also from c. 1400 

 sod (v.2) 

 "go, depart," in sod off (1960), British slang term of dismissal; see sod (n.2).
```


## [2026-09-14T02:00:36.960Z] TOOL CALL #45: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"### wikt son\"; grep -n -m3 -A4 \"Proto-Germanic \\*sunus\\|From Middle English sone\\|Proto-Indo-European\" 7c18575ee9525e6a.txt | head -30; echo \"### PGmc sunuz\"; grep -n -m4 -B2 -A6 \"suHnús\\|From Proto-Indo-European\" 4cf0f421969df83f.txt | head -30"
}
```


### [2026-09-14T02:00:37.034Z] TOOL RESULT

```
### wikt son
1280: From Middle English sonn , sone , sun , sune , from Old English sunu ( “ son ” ) , from Proto-West Germanic *sunu , from Proto-Germanic *sunuz ( “ son ” ) , from Proto-Indo-European *suHnús ( “ son ” ) , from Proto-Indo-European *sewH- ( “ to bear; give birth ” ) .
1281-
1282- Pronunciation
1283- [ edit ] 
1284-
--
1425: From Middle English sonen , sunen , from the noun (see above).
1426-
1427- Pronunciation
1428- [ edit ] 
1429-
--
1483: From Dutch zon , from Middle Dutch sonne , from Old Dutch sunna , from Proto-Germanic *sunnǭ , from Proto-Indo-European *sh₂un- , *sóh₂wl̥ .
1484-
1485- Pronunciation
1486- [ edit ] 
1487-
### PGmc sunuz
144- [ edit ] 
145-
146: From Proto-Indo-European *suHnús ( “ son ” ) , with a long vowel contraction in a pre-stressed position, per Dybo's law . [ 1 ] 
147-
148- Pronunciation
149- [ edit ] 
150-
151- IPA ( key ) : /ˈsu.nuz/ 
152-
--
257-
258- Categories : Proto-Germanic terms derived from Proto-Indo-European 
259: Proto-Germanic terms derived from the Proto-Indo-European word *suHnús 
260- Proto-Germanic terms inherited from Proto-Indo-European 
261- Proto-Germanic terms derived from the Proto-Indo-European root *sewH- 
262- Proto-Germanic terms with IPA pronunciation 
263- Proto-Germanic lemmas 
264- Proto-Germanic nouns 
265- Proto-Germanic masculine nouns
```


## [2026-09-14T02:00:39.025Z] TOOL CALL #46: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"### wikt suck\"; grep -n -m2 -A6 \"Middle English souken\\|Old English sūcan\" c0980d493c44f2c9.txt | head -20; echo \"### wikt soak\"; grep -n -m2 -A6 \"Old English socian\\|Middle English soken\" fc1bdc6dc73ba27c.txt | head -20"
}
```


### [2026-09-14T02:00:39.097Z] TOOL RESULT

```
### wikt suck
246: Old English sūcan 
247: Middle English souken 
248- English suck 
249-
### wikt soak
220: From Middle English soken , from Old English socian ( “ to soak, steep ” , literally “ to cause to suck (up) ” ) , from Proto-Germanic *sukōną ( “ to soak ” ) , causative of Proto-Germanic *sūkaną ( “ to suck ” ) . Cognate with Middle Dutch soken ( “ to cause to suck ” ) . More at suck .
221-
222- Pronunciation
223- [ edit ] 
224-
225- ( UK ) enPR : sōk , IPA ( key ) : /səʊk/ 
226-
```


## [2026-09-14T02:00:46.636Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hunu-\\|hunus\\|hunāmi\\|hunami\" BRT.txt | head -10 | cut -c1-400"
}
```


### [2026-09-14T02:00:46.714Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:00:47.578Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hav-\\|havaya\\|schmoren\" BRT.txt | head -15 | cut -c1-400"
}
```


### [2026-09-14T02:00:47.638Z] TOOL RESULT

```
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma 
3941:•  j.  aiwiS.huta-  Adj.,  PPfP. :  s.  'hav-.
4120:anhav-  106
4132:•  j.,  g.  anhav-":  aku-^''  ra,  'Sein,  Da- sein, Leben',  vora  leiblichen  und  geistigen;
4137:ashav-  I  i  a
4138:anhav-  H  A  2
4151:aahav-  n  A  3
4166:No.  I. j.  aaht:  s.  'ii-  und  anhav-.
4601:•  j.  antara.daöhav-,  °daliyav-  Adj,  (auch mask.)  'der  inmitten  des  Landes  ist': mi>nm  aiwi.daRyam  ..  '.ä/Sot  ( ASm.)  Yt lo.  1 44.  A)  m.  Name  eines  Berges  oder Gebirgs:  ahmat  haca  garayS  fraoxlyqn  ., dassmS  °/ihu/ Ytig.2.
5066:•  j.  a-vaahav-  Adj.  'ungut,  böse':  tT daSväil  ayäis  ^'tihls  (IV.y ..  sar)m  mruyl Y.12.4.
5471:—  ya  'du/at  *apaiHtal  äjayaurva  (sd.) N.  5^;  —  *°duia''>  havayaahim  ^axt?m N.rjC?);  —  puxh^mHi  (sd.)  °du!qm  tanüm piryeiti\.4.iT, — ya%a  ü'hrusum  *yärf gä%ä  asrävayd  hyai  *'du/''''^  hi  syao- %an»m  "wenn  er  ein  Vierteljahr  lang  die G.  nicht  aufeagt,  so  (gilt)  sein  Tun  einer -4.-SQnde  (gleich)"  N.  42.  a)  mit  sna'^a- verbunden:  yö  nar
6061:•  Jt  g.  'aäa-  n.,  nur  Sing.  'Wahrheit,  Recht" (nur  Komp.).')  A)  insbes.  als  dogma- tJschcr  Tenn.  techn.  'As^,  sehr  oft,  bes.  im jAw.,  mit  vanhav-  oder  vahtsta-  Adj.  verb.; mw.    I)"   'Inbegriff  dessen,    was    wahr
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  stäomi a^3m  n3isml  äagvs\t.24.y,  Y. //.  19  und /2. 1 ;  —  sardiiustrahe  .  .  yd  paoiryö  .  . Staat  'Lm  naist  daivS  Yt.  13. 89;  —  yal  nä . .  %ris  "s^n  ufajtuyät  V.  18. 43 ;
6193:AaSmnä  W.öo.^;  —  Aaomanam  •A»7  .  . eistsis  basidsa  haHmnanqm  Vr.  p.  i ;  — yamäüa  .  .  yat  /aymasyS  'Ms  .  .  ratu/ri- tsi/Vr.g.S.  a)  sonst  mit  vauhav-  Adj.: 'silvanuhi  srTra  xssi'kni ..  kainins  kfhrpa srTrayä  Yt  13.  107;  —  'stm  vaauklm x^Bii-nXm  bsrfsaitlm  .  .  dv/oarym  ahurahe mazdi  li'aKhanm  aimsanqm  spmli Yt77.i  f.;  3',  18.2,;  —  k
6371:I S  7  aSävaohav-  —  ailÖäS-  258
```


## [2026-09-14T02:00:55.678Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hav-\\b\" BRT.txt | wc -l; grep -n \"'hav-\\|\\\"hav-\\|hav-'\" BRT.txt | head -20 | cut -c1-200; echo \"=== search 'gebären' ===\"; grep -n \"gebären\\|gebären'\" BRT.txt | head -10 | cut -c1-200"
}
```


### [2026-09-14T02:00:55.784Z] TOOL RESULT

```
2
3941:•  j.  aiwiS.huta-  Adj.,  PPfP. :  s.  'hav-.
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  st�
29501:•  j,  'hav-  V.  'auspressen',  den  Haoma. Praes.  10  Aunav- :  ium>-'\  11  Aun-'\ ij  (Fut)  iaorya-'K  —  PPfP.  Au/a-,  PFP. Aao/yanta-;  Inf.  °hutayae-ca.        [Vgl.  noch
29506:lä.satiiU,  sofyati;  sulak;  XB.'^.  huhUan,  Aif/(Bd. 34.   18).    —    Pü.:  hunilan\\  —    i>  Vgl.  'hav-
29508:•  j.,  g.  'hav-  V.  'antreiben'.  Praes.  lob «"fl«^-»,  iia*w«3-'>,  iib^i-OÄ-'l— PPfP. 'Aata-.         [Vgl  noch  '"par>:^äi>e\
29567:KompE.  —  Zum  V.  'hav-.  —  ai.  vgl.  aähifä- vaifa-  Adj.  'lut  Somab ereil ung  dienend',  n. Du.  '  Somapressc'.  Vgl.  GON.  KZ,  tS-  526, Bthl.  IF.  5.  370.  —  Pü.j  käv
30497:Zum  V.  'hav-^).  —  ai.  sürä-  f.]),  mp.  (PÜ.) Aur.  —  Pü.  (2U  V.):  Aur,  (zu  A.  und  H.): iaiar.—  0  Wein  aus  Pferdemilch  bereiten), im  Cegeniaiz  zu  rnaiav-  (sd.). 
=== search 'gebären' ===
6003:•  j.  a-zäta-  Adj.  (fem.  °td-)  '(noch)  nicht geboren'  sva,  '(noch)  zu  gebären,  künftig* : hätamca  aaAusämca  zätanamca  'tanamla aiamamY.6^.6',  —  irfri^u/am  ../vantam . 
15761:ai.  -^f^.  pürva-sti-  Adj.  'erEtgebärend'. —  Pö. : fehlt.
16805:14.  ß)  durch  Praen.:  yesi  sl  zao^r^  mit  aiti  'etwas  (wieder)  hinübertragen, baraiti  avi  ii  mai%an3m  "wenn  er  sich  -bringen  zu  — '  (ava  mit  Akk.):  us  kata die  Z.  zu
24426:>r3dat.förya  .  .  yä  'vairüa  nqma  avaia 'vairi  ya%a  hä  hm  zUanäl  yd  vTsp€ taurvayat . .  fiagfä  ". .  die  auch  K  heisst. darum  K,  weil  sie  den  gebären  wird,  der al
27620:•  j.  'zan-  V,  'zeugen,  gebären',  von  ahuri- sehen  Wesen  ■'.  Praes.  5  *zazafi-'\  zizan-, II  ziin-i\    17  (FuL)  zqAya'*\  27  (Pass.)
27622:'gebären';  1)  von  Menschen;  a)  Ait: SicöM  (nJimlandvIin)  Üaräitii zizanaitt^ (NPf.)  Jaihyante  huzämim  (sd.)  ".  .  ge- bärende Frauen  . ."  Yt.5.87;  —  3r»hqm raya  .  .  A
27625:mit  US  i)  'erzeugen',  von  Menschen: dvaiibya  haca  mrsbya  dva  nara  us.zayeinte (statt  Du.)  mßiwana  strii'a  nairyas^a  "von dem  Menschenpaar  wird  ein  Menschen- paai  erzeugt . .
28049:•  j.  *zazäite"  Inf.  '(Kinder)  zu  erzeugen, zu  gebären"*;  vanta  . .  ySi  h»n  kikrpa srazsla  zaz'  "die  beiden  Frauen  . .,  die den  schönsten  Körper  haben  zur  Zeugung vo
29512:•  3  hav-  V.  'gebären',  von  äafvischen Wesen".     Praes.  11  Aunä-'K
29513:'gebären    (absoL) ,    Kinder    zur    Welt
```


## [2026-09-14T02:00:58.121Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29495,29530p' BRT.txt | cut -c1-600"
}
```


### [2026-09-14T02:00:58.183Z] TOOL RESULT

```
aby  Google
i78i
haya-
bei  7Tn«ligein  Auftreten  smil  sich  >nr  ein Feminin  bezieht,  spricht  vielmehr  lu  ihren Gunsten.  Aber  die  Aasgänge  der  Fonnen werden  doch  die  der  ^'-Delilinalion  gewesen »ein. —  M)  Eine  merkwürdige  Verwechslung; Um  =  mp.  hem  (damals  schon  Mm)  'Charak- ter'!   S.  noch  zu  htm  (Part)  No.  i.
•  j.  haya-,  hya-^''  n.  'Eigentümlichkeit, eigen lütnlicti es  Gebahren':  asti  ii  (näml. sünahe)  Aaim  ya^a  .  .  "er  (der  Hund) zeigt  ein  Gebahren  wie  . ,"  V.  ij.  44*;  — ai/i  sl  (näml.  sBiiahe)  '"hatiH'^  yd^a  .  . "soviel  Gcbahningen  zeigt  er  (der  Hund) wie  .  ."  V.jy.  45-48*.
KompE.  {'Äya.y  —  np.  ximi)  'Charaliler'.  — Pü.;i™]).  —  ')  Die  Kompform  Aya^  weist  nach IF.  /.  71  darauf  hin,  dass  Aaj-a-  aus  uridg. 'sfiti-  hervorgegangen  isL  —  ')  Stumpfsinnige Wiederholung,  statt  *Äaya,  Flur.  —  3>  Au»  ir.
•  j,  'hav-  V.  'auspressen',  den  Haoma. Praes.  10  Aunav- :  ium>-'\  11  Aun-'\ ij  (Fut)  iaorya-'K  —  PPfP.  Au/a-,  PFP. Aao/yanta-;  Inf.  °hutayae-ca.        [Vgl.  noch
'auspressen,  ausstampfen,  keltern',  den Haoma:  aia  hävana  haomqn  kunyät  "so soll  der  Havanan  die  Haemazvi\%t  aus- pressen" N.Öl?;  —  kaa  %wqm  paoiryS haoma  ..  kunäta  Y.fj.  3;  4;  —  hävana- yas{sA.)ca  Aaoma  Aunvatntya  (GDf.)  Vr. 12.3;  —  yäi  h)nH  haoma  .  .  asaya  hun- vana  asaya  Aaosyatiia  "die  Zfacwazweige, die  . .  jetzt  ausgepresst  werden  und  künftig ausgepresst  werden  sollen"  Vr.p.j;  — nSit  haomS  hutö  axii/  nSit  tnahrks  .  . ava  alle  ahuta  V.  6.  43;  —  pasca  fra- riuAaniti  haemahe  Autahe  H.  1.  9;  V. 18.  13;  
niit  aiwi  'auskeltern,  durch  Kellern zubereiten',  den  Haoma:  yS  mqm  *aiwis.- hut>m  (näml.  haomun)  därayehi  (sd.) jaia  täyüm  pflSMrim  Y.  i/.  3;  —  s. noch  Ini
niit  ä  dnwS.:  hsvanäns  (näml.  kairim aaAat)  yat  Aaopamca  oAunavaf  (3SKA.) aaAavaiDUi^a  *vImanät(Sp.  1135  u.)N.  72.
mit  /rä  'durch  Keltern  fertig  machen', den  Haoma:  ä  mqm  (näml.  haom»m) yäsaaitha.  ./rä  mam  AunvaauAa^^  :^antSe Y.S.2.  '
lä.satiiU,  sofyati;  sulak;  XB.'^.  huhUan,  Aif/(Bd. 34.   18).    —    Pü.:  hunilan\\  —    i>  Vgl.  'hav-
tien  nach  »ich;  vgl.  'latt-  No.  2.  —  ")  Nur im  PFP,  hoBiyania-,  sd.  —  3)  Them.  —  *)  -Statt dessen  steht  N./adas Ideogramm  von  :^arilan; 1.  lu  hulay-,  ahviiJiHlayaiia  und  Bthl.  )F. //.  116.
•  j.,  g.  'hav-  V.  'antreiben'.  Praes.  lob «"fl«^-»,  iia*w«3-'>,  iib^i-OÄ-'l— PPfP. 'Aata-.         [Vgl  noch  '"par>:^äi>e\
i)  'antreiben,  in  Bewegung  setzen':  s. 'iata-,  a)  'etwas  antreiben  nach  Jemand hin  (Dat.),  einem  etwas  zu  verschaffen suchen':  y.l  *malnil  (sd.)  yJ  drigvalti (Sp. 7760.)  xsä^nm  hunaiti  duL^aö^anäi ahurä  ".  .  der  dem  Z>M(ygenossen  die Herrschaft  zu  verschaffen  sucht,  dem  Übel- täter, o  Ahr  Y._3i.  15;  —  Aux/a^rSJtmiti (sd.) . .  xsa'irfm  . .  Mmahicä  *AvanmaAicä  '* Y.  J5-  5-
mit  apa  'ablenken':  yöi ..  tagiriptfmHi snahfm  apasa  apaj^anvainii  "dit.. seihst den  Schlag,  zu  dem  schon  ausgeholt  ist, rückwärts  ablenken"  Vt.  i4-  46-
ai.  suviü,  süläh,  —  Vgl.  a^ai-.  —  Pü. :  kartaii, (zu  Y.  3S  erl.):  liiriin  afe  tarlaiti  Sü.  (lu Y.  s&-  d^""«.  (lu  V.  35)1  karlum;  Npu.  (zu Yt.  /j):  iiiailaHS).  —  0  Bthl.  BB.  13.  6t, IF.  /.  76,  78.  —  ')  Vgl.  'Am-  No.  1.  -  3)  S. zu  j»flA-.
•  3  hav-  V.  'gebären',  von  äafvischen Wesen".     Praes.  11  Aunä-'K
'gebären    (absoL) ,    Kinder    zur    Welt
bringen':  /Om  xT  asva  . .  aiiaiwyäsü'/ {sd.) hunaAi^l . .  nava  (sd.)  az»m  . .  anaiwyäs/i/ Aunämi  V.  18. 30  f.
ai.  sule;  mp.  Tnsüt  'asfjat,  vinirmitaA'  (Mi.). —  Vgl.  Aaatitrö.huitit:  —  Pü.;  himidaicnJ- lan'}.  —  '}  Im  Gegensatz  zu  'lou-i  vgl.  Pü., kaela-  nnd  lu  hiinav-  mit  Mo.  i,  ferner  mp. viiütaiän  'duflasi-ffayai,  iptdrajanlaiialf'  (Mx.). S.  aber  iukah-T-.  —  ')  Vgl.  ^hav-  No.  i.  — 3)  Them.
•  j.  ♦hav-  V.  'schmoren',  Praes.  r  Au-, 30  (Iter.)  Asvaya-,
'schmoren,  rösten':  yal  .  .  Strim  nasu- päk»m  frajasqn  nasBm  Aqmpacqn  natüm hävayqn  "wenn  (sie)  .  .  zu  einem  Feuer kommen,  womit  man  eine  Leiche  kocht  — sie  kochen  eine  Leiche,  sie  schmoren  eine Leiche  — :  .  ."  V.Ä73;  —  mqnaym  aAe ya'ha  ätars  huskim  alsmtm  .  .  aipiJunn- taiti  Aävayeüi  äaiaiti  ".  .  wie  das  Feuer trockenes  Holz  . .  zerstückt,  schmort,  ver- brennt" Y.  71. 8;  —  ya%a  . .  yBim  yHi masyaia  ä^ary^a  :^asta  (sd.)  Auyar>£ (3POA.)'>  gqm^a   ifUstsm  ifaraiti   "wie
dby  Google
1783
hava-  I
hava- 3  b
1784
ihr,  die  Menschen,  . .  Speisen  schmort und  gares  Fteisch  esst"  V.  7. 55.
Et.?  —  iBed.  s,  DsT.  ZA,  2.  136.  —  Pii.  (la
W.Sy.Aäi'FHJp),  {luY.l:  ka  Hn-intnd fa  hävan
liaSin,  (zu  V./):  j^artt  (mit  dem  Ideogrsmm
gesclü.)').  —  >)  Mui  verlangte  eine  2.  Hur.  —
')  Wie    für    du   folgende  ^antiiij    oflenbar
irrtümlich.
•  j,  hava-,  Jhva-,  j.,  g.  'x''a-'>,  p.  *uva-
```


## [2026-09-14T02:01:09.531Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Sohn'\" BRT.txt | head -20 | cut -c1-250"
}
```


### [2026-09-14T02:01:09.596Z] TOOL RESULT

```
15918:Die  Lesung  ist  nnsicher;  nach  Jp  I,  Mr2 u.  a.  wäre  pusavaiä  zu  schreiben,  d.  i. 'mit  einem  Biadem  (fusä-)  versehen';  so las  wohl  auch  PB.  —  Fü.:  puiänSmand,  erL: vis  bacak  apäi\  Scheint  fusavaiä  gelesen  
30389:•  j.,  g.  hunav-  m.  'Sohn'  uzw.  i^aÄnschcr!  ^O-  '<";  —  «""^  kihrpa  .  .  yancö  Yl Wesen'*:  kvB  datnBil  drUjS  'nul  "der  ist  \  ^'-  •3-
```


## [2026-09-14T02:01:11.723Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30389,30400p' BRT.txt | cut -c1-700"
}
```


### [2026-09-14T02:01:11.786Z] TOOL RESULT

```
•  j.,  g.  hunav-  m.  'Sohn'  uzw.  i^aÄnschcr!  ^O-  '<";  —  «""^  kihrpa  .  .  yancö  Yl Wesen'*:  kvB  datnBil  drUjS  'nul  "der  ist  \  ^'-  •3-
ein  Sohn  aus  der  Schöpfuiw  der  .Dr."|  Komp.  mit  (Ableit.  ans)  •*,«fl/rr--(?)f..  sn. \.  51. 10 -j  —  'navO  {UV.)  i0uru.*ao>:ranqm\  '*    ''  ' -^  ^
(sd.)  Ytfo.  113;  —  nurvii  'H.it'J  j'aäti-]»  j.  hu-oi'vixta-  Adj.  'gut  hera,bge- kaya  (sd,)  Vtj.  57;  —  >ff  /a«a/  °navB  Schwüngen,  gescbleuderf :  vazrvm  -ttm {ais  AP.)  yai  pa^^sanaya  nava  •ruivasca\kamfr^e  paiti  daffvanqm  Yt().%;  10.  1^2; nivikahe  •navascd*  ..  Yt.  7(^.41;  5.  54.        , —    vatrö  'tB  Yt.i^.'jt;    —    vaxracit  .  .
Znm  V.  ihav-.   —  Vgl,  kaola..    —    ai.  süniv-    'ta  (NP.)    Yt,  10. 40.
m,,  goL  sUHUs;  iVerSch.  «  -  »  s.  BtHl.  IF.7.  1  Zum  V.  t«i<p-.  —  Vgl  vaa-  i  hufixl  fVd.i.  —
107.    —    Pa.  (lu  y.  5/):  humiSait).  —  ■)  Im  I  po.;  ^kuvixt')  (NpÜ.i  ^ii  miida),     d«iu    die
Gegen».  lu /uSra-.   —  >)  Aus  dem  Aw.-Won  Erl.:  ^kuvixOk')   e  tu   iäsiän   mtnöü/ij    oft
gefonnt,  vgL  Pü.  lu  luuat!rö.kuna-  und  hutm- '  ^avtl  u  vinäiiärän  päli/räi  afii  iuntt  u  m/nä-
Saitnilan  (unter  ihav)  und  JusTi  PrJ.  88. 147, :  iiAi  5  kanCir  {i^it).   —    '»  Geschi.  an  o  mam
WEST  SBF_  4^.  40.  51,  39.  \,km,ixm-i)  sUtt  annd«;  B.  No.  2.  —  »)  G«chi.
•  j-,  g.  hunara-  m.  i)  -Können,  Kunst':'     «"""°>'  «""  »"dstda;  s.  No.  i. kyal     da     ^yaohana     mlidavqn    (sd.)    .  .  •  j.  huovana-  Adj.,  PPM.:  s.  'Aai-. %wä   'ra   ".  .  durch   dein   Können"   Y.  ,  j.  hunvant-  Adj.  (fem.  'vaintt-),  PPA.: 4^.5".         a)  'Kunstfertigkeit,  Geschick- js,  'hav.
lichkeit':    kva    asti    spä    vokunazgB  (sd)  1      .         ,  .  ,.  ,  ,     ,
```


## [2026-09-14T02:01:18.403Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hōm\\|hom \\[\\|hwm\" PHD.txt PHD_mackenzie.txt | head -20 | cut -c1-300; echo \"=== NYB ===\"; grep -n \"hōm\\|haoma\" NYB_vol2_glossary.txt | head -10 | cut -c1-300"
}
```


### [2026-09-14T02:01:18.489Z] TOOL RESULT

```
PHD.txt:186:~ih: heresy. āhēg Phwk' | M >ле, N ahd] fault, blemish. ahógénidan, áhógén- ["nokyn-ytn!] defile. a-homānāģ [’hwm’r’k'] unlike. ahēš [nof] deathless, immortal.
PHD.txt:223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īd
PHD.txt:318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-
PHD.txt:390:hambār [kmb’l | N anbdr] store. hambārīdan, hambār- [hm-, hnb'l-ytn! | M hmb'r-, N anbürdan] fill, collect. hambasān [Anbs?n! | M *mbs*n] enemy, opponent. ~ig [-yk'] inimical, opposing. hambast [Ambst' | N anbast] compact. !hambastag [Ambstk' | N anbasta] formed, composed. shamba
PHD.txt:398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Но
PHD.txt:514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, wat
PHD.txt:516:—jh: weakness. nizārīh- [nz?lyh-] become weak. nē [ТА < A t£? | М пол, N nuh] nine. nóg [nek! | М mwg, N naw] new, recent. ~erz [-hvc | N nawróz] New Year's day. ---zád(ag) [-z't(k)! | N nawzàád] new-born. nohom [nhwm | = M, N ~] ninth. nózdah [nwzdh | № ~] nineteen.
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahr
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w
PHD.txt:663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lord
PHD_mackenzie.txt:951:                a-hominig [)hwm)n)k ] unlike.
PHD_mackenzie.txt:1352: a-xwamn ['hwmn ] sleepless.
PHD_mackenzie.txt:1853:dahom [d'hwm I M dhwm, N ,...,] tenth.
PHD_mackenzie.txt:2132: .......-humat [-hwmt ] evil thought.
PHD_mackenzie.txt:2714:hamb6y- [hnbwd- I M hwmbwy-, N anboy-idan] smell (tr.) .
PHD_mackenzie.txt:2907: HOm [hwm IN ......] the sacred plant Haoma (ephedra).
PHD_mackenzie.txt:2911: h6mast [hwm)st ] various series of prayers.
PHD_mackenzie.txt:2913: h6m\en, -ig [hwmyn , -yk ] of Haoma.
PHD_mackenzie.txt:2949:humat [hwmt = Av. humata-] good thought.
=== NYB ===
635:ariön-kaft [~-kpt'] measuring one cubit in length: 2 ~ hom two haoma-stalks measuring one cubit each 407. — -kaft from the root kap-, Lat. capio, ‘to hold, to take'; Bailey TPhS 1954, 146-153; cf *gri-kaft. l
1884:. cigon ul 6 hàn hom nē handācēt and as I [standing on the ground] do not reach up to that haoma [placed at the top of the tree] 402%. — Ps. *nd’hiny, 'nd?e- ‘to judge’; MPrs pres. ’nd’c-, Verbum 186; Paz. NP andāxtan andäz-. — V. handä- ción, handácak.
2015:hom [hwm] the haoma-plant, whose juice is the chief element in the Zoroastri- an cult: 3818, 3919.24-25 405-8.15.21.24.26, 415. 4274, 431; — pl. ói$ün ~ these haoma- stalks 4119.13; — ~ 4 spēt 937; ~ u mang 6016; ~ u barsom 90?’; — ~-tar containing more haoma 40%. — Av. 1732 sqq. V
2019:hömikän [hwmyk’n'] containing haoma, “haomic”: äp + ~ 5623.15, — As to the suff., cf östikän, vāvarīkān; šāhīkān ‘royal’ FrP 2. — V. also *huhömikän.
2047:*hu-hómik, pl. cas. obl. *huhömikän [hwhwmyk'n'] things (plants) containing good haoma 40?'. — Spelt as the well- known ‘whrmzd’n'=Ohurmazdän, but this is out of the question here. We must assume the above reading, confirmed by the paro- nomasia huhömikän homtar, v.s. v. hom.
2804:oi [LH], 6 [L] dem. and det. pron. this; also the pers. pron. of the 3d p.: he, she, it; when used adjectively placed before its headw.: 0? mart this man; det. 0% ke 6671; õi veh ke 223- mänäk(k)äi (g.v.) 6 či cigon ke ... 4182; 6% is the normal form, 0 is rare: 6 ydtuk 5412-18; 6 màn thi
3099:patvastan patvand-, to bind, to attach, to join: Tir patvast 7'-® meaning not clear: (joined to [the planet] Tir =) be- ing in conjunction with it (?); han hom andar hàn draxt bà patvast this haoma was attached to this tree 4015; cë rād ka mē- noyan u gētīkān dāntšn u kār-ākāhēh 
3371:sahistan [MDMHn-stn'] sah-, subj. 3d p. sg. sahät 35%, opt. sahē [MDMHn-yd] 4027, to appear, to be visible, to seem, to please: 1. with a subj.: pattāk sahist pat hamkarpeh i amahraspandān he was manifestly seen in the same shape as the Amahraspands 38?6; an õi sahist Vahuman pes-karp V. a
4380:xujiyišn [hw’dän'] v. n. of z%dstan 1. as a pred. : api-män han hom ~ we must search for this haoma 40°. — 2. as an inf.: the act of searching, research 11217; request 11719, — < guidišn (the SW form with -d- < -z-, V.S. V. x”ästan) with the regular change of -d- > -y-; parallel
```


## [2026-09-14T02:01:28.175Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hôm\\|hōm\\|haoma\\|Haoma\" HUB.txt | head -15 | cut -c1-300"
}
```


### [2026-09-14T02:01:28.272Z] TOOL RESULT

```
4982:106, zd. haoma-, Vgl. auch Bum *das byzantinische Reich'
```


## [2026-09-14T02:01:30.780Z] TOOL CALL #55: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B3%D9%88%D9%BE/\" --note \"page 448, Persian سوپ, Mo'in entry (MON:1944)\" && grep -n -i -A4 \"معین\" data/verification/sources/web/$(python3 -c \"import hashlib;print(hashlib.sha1('https://abadis.ir/fatofa/%D8%B3%D9%88%D9%BE/'.encode()).hexdigest()[:16])\").txt | head -30"
}
```


### [2026-09-14T02:01:33.375Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ce2925bb6f233e9c.txt
32: فرهنگ معین
33-
34- [ فر. ] (اِ. ) نوعی آش رقیق که قبل از غذا خورده شود. 
35-
36- فرهنگ عمید
--
126: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
127-
128- لینک ها 
129-
130- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد.
```


## [2026-09-14T02:01:36.458Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4975,4990p' HUB.txt | cut -c1-400"
}
```


### [2026-09-14T02:01:36.512Z] TOOL RESULT

```
arm. goin^ zd. gaona- ; paz. driew 'a consecrated cake' Min.
Gl. 64 — zd. draonah-; surun (surln) 'Hinterbacken' = zd.
sraoni"^ Faredunf i^^?., Fredun, arm, Hruden (sassanidisch,
aus *Hredun umgestellt) = zd. &ra^iaona-\ mUm 'Wachs',
arm. mom (5. Jhd.); rum (bei Vullers rom) 'Schamhaare*
= skr. rdman-; hum 'Homapflanze' (vgl. hUm bei Mu-
waffaq p. 268, s. Horn Nr. 1113) = paz. hum Min. Gl.
106, zd. haoma-, Vgl. auch Bum *das byzantinische Reich'
(reimt auf bum Fird. I, 403) =' Poi/nT], lat. Roma, — Ausser-
dem ist altes o z\i U geworden in : samur 'Zobel' = parth.
aifuoo (de Lag. G. A. 71, 226), arm. samoir (= phi. ^samor)
und np. kahUd blau = arm. kapoit *dunkelblau (vgl. Horn
Nr. 842).
») Vgl. pSz. xaim Min. Gl. 124, phi. x{a)8m und tism Gl. and
Ind. 29, 68, Bdh. Gl. 124. Ebenso mit a fur i (i, e): ahan 'Eisen* =
phi. aatn (reap. a«g«) s. oben p. 10; mazldan *8augen, schmecken' s. § 17.
```


## [2026-09-14T02:01:53.722Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; grep -n \"seu-\\|sū̆-\" WLD_Bd2_pages.txt | head -20 | cut -c1-200"
}
```


### [2026-09-14T02:01:53.787Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
31065:468                                              seu-
31130:                                                     seu-, sa                                       469
31155:    Eine Erw. seu-d sucht Holthausen AfnSpr. 121, 294 in ags. besutian „be-
31229:(nicht ^seu-ip; nur soldo ware moglich).         S. Pedersen KG. II 635 ff.,
31234:     seu-q-:          lit.    sulcus   suhti „drehen,       wenden'^, suhriis „beweglich,     flink*^,
31242:8chleudem“; dazu vielleicht als idg. seu-b{hy, lit. saubti usw. (s. u. qseubh-)
31266:3.   seu- „sieden, heftig bewegt sein^^ (daneben seue-, sue-t-,           siiei-t-),
31291:  Unter Annahme einer Wurzelvariation "^seu- sue- stellten hierher auch
31298:*seu-e- erweisen wiirde ^Solmsen Unters. 271 stellt swadul zu gr. dexyLov'
31357:„losla8sen‘- anzureiben (s. seu- „biegen^'. Vgl, L. Meyer KZ. 2i, 472, Pers-
34114:fiir    Morast und Schmutz             (:   ^seu- „sucus‘3 Yf. LE^Yb.^ u.                    siis    zw. benannt.
34141:chung mit "^seu- „SafP wohl zutreffend, indem „Milch'' (vgl. ir. suih in
34217:        LEWb.2u.5wo) neben siu- ein bereits idg. 5^7- (seu-) bestanden habe
35284:usw., s. u. seu- „Saft‘‘),
36577:                                                      sqeu-, qseu-                                                551
36628:3. sqeu-,       qseu- schallmalend „niesen'^
```


## [2026-09-14T02:01:56.532Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '31060,31080p;31125,31150p' WLD_Bd2_pages.txt | cut -c1-300"
}
```


### [2026-09-14T02:01:56.755Z] TOOL RESULT

```
                                                                      p, s. u.);
Bodenstelle^, serb. stpifi „rieseln, fein ^egnen‘^
  Im Germ, auch Formen mit germ, p (die an sich ebenso wenig den Schlu&
auf idg. h rechtfertigen, wie die unter Vii- „ausgie6en‘‘ angeftihrten Formen
mit germ, k den auf idg. ^): ags. sJpian, mnd. slpen „tropfenweise                             fallen,
468                                              seu-



sickern^',      ndl.   Bijpplen „tr6pfeln'^,    mhd. slfen   (st. V.)    ds.,    schwed. mdartl.
sipa „langsam          fiiefien,   sickern*^ dan. Mter sibe „tropfenweis flieBen", norw.
mdartl. sTpa „ weinen“, mnd. sip „Bachlein“, slpe „iiiedrige und feuchte
Wiese“, mhd. slfe ,;langsam rinnender Wasserlauf, niedrige *Wiese‘‘; hieher
auch der germ. Name der Seife: ahd. seifa^ seiffa^ seipfa „Seife, auch
Harz‘S, mnd. sepe „Seife“, ags. sape f, (daraus nord. sCtpa) „Seife" (sap
„Harz, Pomade'"), vgl. Yf. LEWb.^ u. sapo (germ, Lw.), Schrader RL. 761,
 H. Schroder ZfdPh. 38, 519, Uhlenbeck IF. 25, 145, Falk-Torp u. sashe
hber die Frage, ob das Wort ursprgl. „TJrin‘" als Waschmittel (vgl. ahd.
seicJi „Harn“ von Wz. seiJc) oder ein „Eesinat“ (vgl. as. drupil „Harz‘' dt.                :


                                                                                                           :




                                                     seu-, sa                                       469

studier 192 f.], Prellwitz u. vkiCco,                 Wood AlPh. 21, 181, Falk-Torp a. s^le^
und z.     T. auf s'^el-         benihendes          u.   *5^Z- „8chlingen*0*           r-Formantien
ahd. sUrougi „triefaugig‘‘, aisL saurr „feuchte Erde, Kot‘‘ (Persson Wzerw. 8;
s. weiteres germ, bei Falk-Torp u. serpe)       und wohl die ganze u. *sUros
„sauer‘‘ behandelte Sippe.
    3.   Gutturalerw.: seug, sUq und seug^                       sUg (kaum nach Hoffmann BB.
26, 131 seugJi),
    Lat. siicus „Saft“            (s.    auch u. suaq^os); sugOj         -ere „saugen'‘;    air.   sugim
„sauge‘‘, sug „Saft^‘; mit q cymr. sugno^ mbret. sunaff^ nbret. suna ds., sun
„Saft“, cymr. sugnedgdd „Pumpe^‘ (ds. Bed. in mnd. sucJce)^ acymr, dis-
suncgnetic                (morph ologisch schwierige Gruppe, s. Pedersen
                  „exanclata“
KG. I 72,  125, 488;   nicht nach Yendryes De hib. yoc. 181 aus dem Lat.
entlehnt); ags. sucan^ a. ndl. zuiken „saugen“, ags. socian {*sukon) „auf-
saugen“, gesoc n. „das Saugen“; aisl. suga (sjuga) „saugen‘', sog n. „da8
Saugen“, ags. as. ahd. sugan „saugen “3 Eaus. norw. mdart. s^gja, mhd.
sougen „saugen“, mhd. sue, soc, g. soges und souc, -ges „Saft“, ags. sogopa
m. „Schluck8er‘^ Yielleicht z. T. hieher lett. sukt „saugen“ (auch lit.
sunkd „Saft“?), s. u. seq- „abrinnen“; apr. suge f. „Regen“ (? s. Trautmann
```


## [2026-09-14T02:02:02.919Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"hunaoiti\\|haoma\\|sumtti\\|soma-\" WLD_Bd2_pages.txt | head | cut -c1-300; echo \"=== supa/suppe ===\"; grep -n \"supa\\b\\|„Suppe\\|suf „Br\" WLD_Bd2_pages.txt | head | cut -c1-300"
}
```


### [2026-09-14T02:02:02.999Z] TOOL RESULT

```
31103:     Ai. sunoti „pre6t aus, keltert"" = av. hunaoiti ds., ai. sdvana-m^ savd-h
31105:„Kelterung des Soma", sutd-h „gekeltert", soma-li = av. Jiauma- m. „Soma";
=== supa/suppe ===
31157:  A, seup-, seuh-:       ai. supa-h „Bruhe, Suppe“;        aisl. supa „schlurfen”
31160:mhd. suf^ 5o/* „Suppe‘^, ags. sype m. „das Einsaugen“, aisl. sopi m. „Schluck‘‘,
31288:germ. *supa in sop n. „Pleischsuppe, siedendes Wasser. worin man Fleisch
```


## [2026-09-14T02:02:09.398Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '31266,31295p' WLD_Bd2_pages.txt | cut -c1-300"
}
```


### [2026-09-14T02:02:09.460Z] TOOL RESULT

```
3.   seu- „sieden, heftig bewegt sein^^ (daneben seue-, sue-t-,           siiei-t-),

   Av. havayqn „sie schmoren“, havayeiti „er schniort“ (3. p. opt. huyards
=  ai. ^suyilr zu einem Praes.        nach der Wurzelklasse) nicht gleich ;


zu setzen mit Jiav- „keltern, auspressen^           =
                                            ai. sunoti, denn von letzterem

kommt nur das -we^^-Praesens vor (und ein “?^<^-Praesens im Av. durch
Umbiidung nach ilhnlich klingenden Yerben), ferner scheint Ifiimao^^su-
noti gerade ein Kunstausdruck fiir die Kelterung des Somas zu sein. Wir
haben also eine selbstandige Wurzel seii^; unrichtig Scheftelowitz ZDMG.
59, 710 Qinv- zu evco^ das aber natiirlich          =====



     Dazu (Charpentier KZ. 40, 425f.; germ, "^saup- in aisl. siopa „sieden,
kochen'", ags. seodan ds., ahd. siodan,mhd. nhd. siedf^ii, aisl. seyp „brausen-
des Wasser“, srypir ,,a fire-pot“; got. saups „OpfertieP', aisl. scinpr „Schaf,
auch anderes KleinvieK', wozu nschw. dial. sd\„Schaf“ gamj-sd „Dorfstier,
ein Stier, der von den Bewohnern eines Dorfes gemeinsam gefiittert wird“;
germ. *supa in sop n. „Pleischsuppe, siedendes Wasser. worin man Fleisch
gekocht hat“, sopna „gekocht werden“ (s. a. Pick III ^ 443, Palk-Torp 64,
940, 1561 m. Lit).
  Unter Annahme einer Wurzelvariation "^seu- sue- stellten hierher auch
                                                            :


ahd. sw'ednn „Dampf', mbd. swadem, stvaden "„Dunst“, nhd. ScJiwaden, ags.
```


## [2026-09-14T02:02:17.365Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk 'NR>=31140 && NR<=31300' WLD_Bd2_pages.txt | grep -n \"^ *4[67][0-9] *$\\|47[0-9]\\|seu-, s\" | head -20"
}
```


### [2026-09-14T02:02:18.510Z] TOOL RESULT

```
52:470                                                  sen-
```


## [2026-09-14T02:02:21.010Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"^ *47[0-4] \\|  47[0-4]$\" WLD_Bd2_pages.txt | awk -F: '$1>31100 && $1<31400' | cut -c1-120"
}
```


### [2026-09-14T02:02:22.266Z] TOOL RESULT

```
31375:                                                      sek-, senk-                                              47
```


## [2026-09-14T02:02:27.438Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"SOUP\" \"SON,\" \"SEETHE\" \"SOD,\" \"SUCK\" \"SOAK\"; do echo \"### $w\"; grep -n \"$w\" SKT.txt | head -3 | cut -c1-400; done"
}
```


### [2026-09-14T02:02:28.627Z] TOOL RESULT

```
### SOUP
### SON,
### SEETHE
### SOD,
### SUCK
18780:SUCK.
### SOAK
```


## [2026-09-14T02:02:31.424Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^Soup\\|Soup, \\|Soup\\.\" SKT.txt | head -5 | cut -c1-300; echo ===; sed -n '18775,18790p' SKT.txt | cut -c1-300"
}
```


### [2026-09-14T02:02:31.513Z] TOOL RESULT

```
Exit code 1
23574:French  from  Teutonic :  bacon,  bonrd  ?, brawl(a),  broil  (1),  burgeon, cantle, crochet, crosier,  crotchet,  croup  ^a),  crupper,  crush, damel  ?,  guide,  hoop  (a),  hubbub,  huge  !, label,  moat,  mock,  moraine,  patrol,  patten, raiUi)»  rally  (j),  ramp,  mndom,  rappee,  re- 
(eval):1: == not found
```


## [2026-09-14T02:02:34.090Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Soup\\|SEETHE\\|Seethe\\|Sod,\\|Soak\" SKT.txt | head -12 | cut -c1-350"
}
```


### [2026-09-14T02:02:34.390Z] TOOL RESULT

```
16828:Seethe,  to  boil.  (E)  Pt.  /a/;  pp.  jaA i/en,  M.  E.  sethen,  pt.  t.  seeth  (pi.  soden), pp.  soden,  K.  S.  st^^n^  pt.  t.  «Jfi,  pp. i^L/<r«.  "f  IceL  /;^Sd»  pt.  t.  sauf^  :  Don. rn/f  ;  Swed.  sjuda  \  G.  sieden.  Allied  to Goth,  sauihs,  a  bomt-ofTering,  Icel.  svfKj, to  bum,  singe.
17668:Soak :  :«e  Suck.
17683:Sod,  turf;  see  Beetha.
18824:Budfl;  see  Seethe.
```


## [2026-09-14T02:02:41.389Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Sup,\\|Sop,\\|Soup\\b\\|Son,\\|Suck,\" SKT.txt | head -12 | cut -c1-400; echo \"=== 18780 ===\"; sed -n '18778,18784p' SKT.txt | cut -c1-400"
}
```


### [2026-09-14T02:02:41.475Z] TOOL RESULT

```
=== 18780 ===
CoioeO  word,  made   from    V .   nu  »  !«.
Off    tunumf   above ;     so    that    F.
SUCK.
fuuraim  answers  to  a  Low  L.  tuseraMUs* OT  suntrantM*.  p.  The  h.  xursum  =  tu- uorittmt  •,  lit  luiiicd  U]»waids  ;  from  SU'  » /»^,  up,  and  ucrsum^  uirsum,  neut.  otpp, of  Mtritre,  to  turn.
Bubaltom :  sec  Alien.
Subaqueous ;  hcc  Aquatio.
Subdivide ;  see  Dlvido.
```


## [2026-09-14T02:02:46.490Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SYN son\"; grep -n \"sūnú\\|sunus.*'son'\\|2\\.41\" SYN.txt | head -6 | cut -c1-300; echo \"### SYN soup\"; grep -n -i \"soup\" SYN.txt | head -5 | cut -c1-250"
}
```


### [2026-09-14T02:02:46.604Z] TOOL RESULT

```
### SYN son
855:1. Grk. és (also xov-oprés ‘dust stirred up’, but simply ‘dust’ in NT), NG pop. oxévy (o fr. forms of the article, ris, etc.; cf. Hatzidakis, Mec. 2.412) : Lat. cinis ‘ashes’, perh. fr. the root seen in Grk. xvaw ‘scrape’. Walde-P. 1.392. Boisacq 490.
1897:same source), OHG-NHG luft (> Dan., Sw. luft), is in origin the same as ON lopt ‘oft, attic, etc.’ (> ME, NE loft; OE loft ‘sky’). Development from ‘ceiling, loft’? to ‘sky, air’. Further connection prob. (but less certain and immaterial for the immediate source of ‘air’) wi
2095:4. ON logi, poet. leygr, Dan. Lue, Sw. liga, OF lieg (leg, lig), ME leye and lowe (latter fr. ON), MLG log, OHG loug, MHG lohe (NHG lohe) : Goth. liuhap, NE light, etc. (1.61). Walde-P. 2.410. Falk-Torp 659. NED s.vy. leye, low, sb.
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTOR
2436:3. Ir. mace ‘boy’ and ‘son’ (NIr. mac, W., Br. mab ‘son’), see under ‘son’ (2.41),
2712:4. Goth. liugan (a in act., b in pass), also liuga ‘marriage : Ir. luge ‘oath’, etc. Walde-P. 2.415. Feist 333. .
### SYN soup
8394:7. Lith, valgis, used of prepared food also ‘an article of food’ : wilgyz ‘moist. en’, Lett. valgs ‘moist’, SCr. vlaga “Mois- ture’, Russ. vologa used of rich soup and various dainties. Development through ‘moist food, dainty�
8719:4. Ir. mias ‘table, dish’, NIr. ‘dish’, Goth. més ‘table, platter’, ChSl. misa ‘platter’, Boh. mtsa, Pol. misa ‘bowl, dish’, Russ. misa, miska ‘soup-dish’, etc. fr. VLat. mésa, Lat. ménsa ‘table’ (7.44). Feist 355.
8895:1. Grk. pvorthy, also pborpor, pvoridd- ptov, orig. a piece of bread hollowed out for supping soup or gravy, later used also of metal spoons (utorpwy xpvoay Athen. 128c), etym.? Boisacq 653.
8979:DINNER SUPPER Selarvov Getrvov yebpua, detrvov betrrvov céna céna pranzo, desinare cena diner souper comida cena prinz, masa masé de seard, cind, ojina praind 3 teen dinnéar (proinn) sutpéar (seire) cinio Swper lein, merenn koan undaurnimat
9004:Fr. souper ‘supper’ (OFr. soper > ME soper, NE supper), sb. use of souper ‘sup’ deriv. of sowpe in its earlier sense of ‘sop’, orig. a Gme. word (5.64).
```


## [2026-09-14T02:02:47.484Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC\"; grep -n \"sūnus\\|sunus\\|sūnu-\\|seu-\\|sup-\" IEC.txt | head -12 | cut -c1-250"
}
```


### [2026-09-14T02:02:47.566Z] TOOL RESULT

```
### IEC
6558:iüs "boiling; decoction, broth". WP I, 199 Skt. yüh, yus, yüsab; Per. jus (£-); Lat. jus, gs jüris; Ir. cf. úsc, m. (juice, fat”? contamination with uisge water: W cf. is-gell ‘soup, brine’; MHG jūs ‘snack’; G Jause ‘teatime�
12108:oléo & oléso ‘destroy’ beside oloós 'destruc- tive, deadly’; cf. also (?) ól-unthos *winter- fig that does not mature’; Lat. cf. ab-oleo, -olere “destroy” beside vi-olens, -olentis (^vio- lent, fr. *uis-^) and vi-olàre, pf. -ol
12910:pins-, form of type pis-, see pisio “crush, grind, pound’. WP II, 9 Skt. cf. pina$mi (sic!), 3s: pinasti, id.; cf. pisi- lam (sic: *platter); pistib, f. ‘flour, powder; Lat. pinso, ére, v. *pound, knead; peck; scoff, berate’; Lat. cf. 
15040:se- 'self-. (Residual root of type seue, seu-, sebhi, etc. Long-grade se-) Gk. he; Alb. -he in veté-he (Coneself, fr. *auto- se); Arm. i (3), prp. “from”; Lat. se ‘self? and së-, px. “without, apart, dis-°; Ir. -se (in mi-se “mysel
15278:seu- (séu-) ‘sigh, pant, gasp’. (Arm. ambig. cf. seubó, io). Cf. WP I, 502 Arm. (ambig.) hev, s. (breath, gasp’; hevk, pl. id.; hevam, v. id.; hivand, adj. (sick, ill, fr. *ségont- ?); Gk. cf. heu ‘alas’; OHG cf. siunon, OE séonia
15279:(seu-, seu- “self”, see seue)
15280:seubð, ið ‘fume, pant, gasp’. Cf. seu- (séu-) above, and WP I, 502 Arm. (ambig.) hevam, v. ‘pant’ beside hivand ‘sick’; G cf. seufzen, v. (sigh. FK:EWDS untenable); Li. siaubiü, ti, v. ‘fume, rage’; siaubas, m. ‘fury, squa
15281:seu£o, ið ‘faint, fail, fall il. Cf. WP II, 8 & 472 Arm. hiwcem, v. 'emaciate'; hiwcim, v. ‘pine’; hiwcanim, v. id.; Go. siuks, adj. ‘sick’; MHG siechen, wv. “be ill; siuche, sf. & wm. “ill- ness’. (For Br. hü-anad ‘sigh’
15287:seu- (1) ‘start, move’. (Variants: sou-, su-). Cf. seuos (2) Skt. saumi, sávami, pp: sutáb, v. “drive, impel, move’; saváh, m. ‘starter, impulse’; variant: suvámi, v. “create, start"; Av. hunàmi, v. “bear — a child; prep
15288:seu- (2), see seue
15289:seue (seu-, seu-) ‘of self, self-, apart, special"; seuos ‘one’s own’; seuios, comparat. form “own, personal. WP IT, 455 Hom. Gk. heé, heu of self" beside he, acc. ‘self’; Alb. u ‘self; Umb. cf. seuum (queried: ‘singly, separ
15292:seu- — sorbhóo, io (sorb-)
```


## [2026-09-14T02:02:53.245Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15287p' IEC.txt | cut -c1-1200; echo \"=== sunus ===\"; grep -n \"sunus, sunos\\|sūnus\\|sunus m\\|'son'\" IEC.txt | head -8 | cut -c1-200"
}
```


### [2026-09-14T02:02:53.351Z] TOOL RESULT

```
seu- (1) ‘start, move’. (Variants: sou-, su-). Cf. seuos (2) Skt. saumi, sávami, pp: sutáb, v. “drive, impel, move’; saváh, m. ‘starter, impulse’; variant: suvámi, v. “create, start"; Av. hunàmi, v. “bear — a child; prepare’; havohom, n. ‘preparation’; Arm. hav, u-st. 'beginning, origin'; Ukr. (ambig.) sovaty, inf. (thrust. Cz. souvat, id.). (Uncertain cognates are W hu, adj. “persua- sive; penetrative; bold? and huan, f. ‘sun’, cf. Skt. saváh, m. ‘sun’).
=== sunus ===
2853:dhetis, io (1) ‘suckling; suckling animal’; dheétus ‘for sucking’, etc. Cf. WP I, 828 and dheio- (1) Skt. dhátuh (1) “for sucking’; Arm. cf. perhaps or-di, gs -dvo ('son', if fr. *p
3117:dhroughos dhrugh-) (1) *'comradely; com- rade, friendship, band'. WP I, 860 Skt. cf. (z-gde) druhah 'son'; LLat. dructis ‘escort’; OE dryht (1) ‘company, band be- side ge-dréag, id. (o-gde
17829:sūnus ‘son’. (Gmc: sunus). WP II, 470 Skt. sünúh, m. id.; Av. hunus, pl. -avo, m. id.; Go. sunus, gs: Aus, id.; OHG sunu, id.; OE sunu, id.; ON sunr, sonr id. (and com. Gmc.); OCH synü,
```


## [2026-09-14T02:02:58.299Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"هوم\" ARY_pages.txt | head -8 | cut -c1-250; echo \"=== latin index ===\"; grep -n -i \"HAOMA\\|SEU\\|SEUE\" ARY_latin_index_pages.txt | head -8 | cut -c1-200"
}
```


### [2026-09-14T02:02:58.401Z] TOOL RESULT

```
748:مهمترین این نوشتارها عبارتند از دو حماسه‌ی هومر به نام‌های «ایلیاد» و «اودیسه» و نمایشنامه‌ها و
995:تصویر دنیای پس از مرگك که در آثار هومر منعکس شده نمونه‌ی خوبی است: سرزمین مردگان در
1026:هومر) نشان می‌دهند که رسم چند زنی نیز در میان توانگران هند و اروپایی رایج بوده است. ژول
1029:می‌گرفتند. در حماسه‌ی ابلیاد (1۸0ن11) اثر هومر آمده است که پریام (/۳۸1۸3) شاه تروا دو زن
1069:در آثار هومر یونانی آمده است که بردگان زن مسئول انجام کارهای شاق (مثلاً آردکر دن گندم وجو
1086:‏بررسی قهرمانان حماسه‌های هومر و فردوسی و ورجیل (۷180112) و همچنین اسطوره‌های .|
4896:تخار: که ۸ (۸ الفتقه 00 اهوم 1 (385قم) هام05
5016:اسپایایی (نتوااهومی: انم اسلاوی کهن (۲12ماک ات ام
=== latin index ===
910:S63 F Oris: V(OIS sli AVIS 14 Sls COWIS sg 250 gly) 9 ua seul
991:oY NAPAT gliay! NAPAT sey SL NEPOT Toe logy y a seul
1213:Sash yl ME yeu Serabj go ghajly gyealt SeuiglSouieo Wl
1290:seul 5 ee
2466:Poko, —=~SO*~C~*~CS~S~«S 0S, 08S, OSSEUM LATIN) eV
3693:BLATEN (DUTCH) gala BLEKHAOMAI, GREEK) gibi
4039:Bs, Sree yey CML Gril) seul Jlel ds cag shih bez 6S)
4580:Seutloah
```


## [2026-09-14T02:03:03.249Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '4890,4900p' ARY_pages.txt | cut -c1-300; echo \"=== pdf page tag ===\"; awk 'NR<=4896 && /\\[pdf page/' ARY_pages.txt | tail -2"
}
```


### [2026-09-14T02:03:04.464Z] TOOL RESULT

```
2 8۸87۸ پردسی کهن (534تا۲ صزم:. ‏ جقوم
پهلوی (1ماتلهه): ,8۸8 آلبانی (0هفانمقتم: 2۸8
اوستی (ع083871): 8۸872080 ,7281760
کر دی (08۵8): ۳۸8۵ ,تقوم پسگشت‌ها اه راد ۳۳
بلوچی 10ل0تاتمه: ۳۸ 0
افغانی (پشتو) (/۸(7لا0م): نا 42 (۳۵87) تاک ان
تخار: که ۸ (۸ الفتقه 00 اهوم 1 (385قم) هام05
سانسکریت (۸(7877ه), 2
و 3۸۲۳۸ ,ق8۸8۲ باق‌فوط 1 (381)) ,10 (۸80 12 کم ,6
ار (30(عیم:. 9 7 9 :005
یونانی (0723): -808 119 ۸0
=== pdf page tag ===
[pdf page 165]
[pdf page 166]
```


## [2026-09-14T02:03:13.792Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && timeout 180 curl -sL -A \"rishe/1.0\" \"https://archive.org/download/old-persian-grammar-texts-lexicon/old-persian-grammar-texts-lexicon_djvu.txt\" -o kent-448.txt; wc -c kent-448.txt; grep -n -i \"haumavarga\" kent-448.txt | tail -5 | cut -c1-500"
}
```


### [2026-09-14T02:03:19.037Z] TOOL RESULT

```
146 kent-448.txt
```


## [2026-09-14T02:03:22.111Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat kent-448.txt | head -5; timeout 180 curl -sL \"https://archive.org/metadata/old-persian-grammar-texts-lexicon\" | python3 -c \"import sys,json;d=json.load(sys.stdin);print([f['name'] for f in d.get('files',[]) if 'txt' in f['name'] or 'djvu' in f['name']])\""
}
```


### [2026-09-14T02:03:23.653Z] TOOL RESULT

```
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
['Old Persian grammar, texts, lexicon_djvu.txt', 'Old Persian grammar, texts, lexicon_djvu.xml', 'Old Persian grammar, texts, lexicon_hocr_searchtext.txt.gz']
```


## [2026-09-14T02:03:26.559Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && timeout 300 curl -sL -A \"rishe/1.0\" \"https://archive.org/download/old-persian-grammar-texts-lexicon/Old%20Persian%20grammar%2C%20texts%2C%20lexicon_djvu.txt\" -o kent2-448.txt; wc -c kent2-448.txt; grep -n -i \"haumavarga\\|hauma-varga\" kent2-448.txt | tail -6 | cut -c1-600"
}
```


### [2026-09-14T02:03:32.150Z] TOOL RESULT

```
929137 kent2-448.txt
8501:onnade’; hauma-varga-, maz-dah-, batu-gara-, see 
21859:26 Katpatuka : Daha :Saka : haumavarga : Saka 
22579:: Saka : haumavarga : 
22640:cal hasta between the g and the a in haumavarga. ” imey*, 
29673:varga- sb., see haumavarga-. 
30319:haumavarga- adj. ‘hauma-drinking’ or
```


## [2026-09-14T02:03:34.360Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && sed -n '30310,30340p' kent2-448.txt"
}
```


### [2026-09-14T02:03:34.414Z] TOOL RESULT

```
2°. hau-dim DSf 32. hau-dis D8s 6°. 

haw nsf. ($196) DB 5.4f; hauv-maiy DB 3.11; 
hauy-taiy DNa 57; hauv-cry DPe 23f. 

haw adj. nsm. DB 1.82, 92°; 2.21, 27, 66, 71; 
3.3, 30, 41, 54, 59, 70, 91°; 5.9°. 


haumavarga- adj. ‘hauma-drinking’ or 
‘hauma-preparing’ (§160.la): Elam. u-mu-mar-ga, 
Akk. ti-mu-ur-ga-’, Gk. ’Auipywt. From hauma- 
($149.0), Av. haoma-, Skt. séma- name of a plant, 
also a drink prepared from the juice of its crushed 
stems, to root Av. hau-, Skt. su~ ‘press’, + varga- 
(§31, §143.D, of unknown connections. hauma- 


212 


varga npm. DNa 25; DSe 24f°; XPh 26; as nsm. 
(§56.11), ArP 14. 


hauvam pron. ‘he’, nsm. DB 1.29: haw (q.v.) 
+ -am from adam, tuvam, ete. (§48, §137, §196). 
Cf. MB Gr. §158. 


hakaram adv. ‘once’ (§191.JII, §204.1): Av.
```


## [2026-09-14T02:03:46.791Z] TOOL CALL #76: Bash

```json
{
 "command": "for u in \\\n \"https://archive.org/download/old-persian-grammar-texts-lexicon/Old%20Persian%20grammar%2C%20texts%2C%20lexicon_djvu.txt\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sewH-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/s%C3%A1wmas\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/seu%C3%BEan%C4%85\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 448: Kent lexicon p.211 haumavarga; PIE sewH-; PII sawmas; PGmc seuthana\"; done"
}
```


### [2026-09-14T02:03:54.155Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a997192c51bace2b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4f68bd4478299d52.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/de43a98c7ba2ce22.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/61625b790df8e7a0.txt
```


## [2026-09-14T02:03:56.760Z] TOOL CALL #77: Bash

```json
{
 "command": "cd data/verification/sources/web && for f in 4f68bd4478299d52 de43a98c7ba2ce22 61625b790df8e7a0; do echo \"=== $f ===\"; head -4 $f.txt; grep -n -m3 -A3 \"Root\\|Etymology\" $f.txt | head -20; done"
}
```


### [2026-09-14T02:03:57.952Z] TOOL RESULT

```
=== 4f68bd4478299d52 ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sewH-
FETCHED: 2026-09-14T02:03:51Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/sewH- - Wiktionary, the free dictionary
62: Etymology 
63-
64- 1.2 
65: Root 
66-
67- 1.2.1 
68- Derived terms 
--
134: Etymology
135- [ edit ] 
136-
137- Perhaps an extension of *sew- ( “ to pour; squeeze ” ) .
=== de43a98c7ba2ce22 ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/s%C3%A1wmas
FETCHED: 2026-09-14T02:03:52Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-Iranian/sáwmas - Wiktionary, the free dictionary
62: Etymology 
63-
64- 1.2 
65- Noun 
--
140: Etymology
141- [ edit ] 
142-
143- From Proto-Indo-European *sów-mo-s , from *sówh₁-mo-s with the Saussure effect , from *sewh₁- ( “ to pour out, rain, to press out, extract ” ) +‎ *-mos . [ 1 ] 
=== 61625b790df8e7a0 ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/seu%C3%BEan%C4%85
FETCHED: 2026-09-14T02:03:54Z
STATUS: 200
TITLE: Reconstruction:Proto-Germanic/seuþaną - Wiktionary, the free dictionary
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
--
146: Etymology
147- [ edit ] 
148-
149- From Proto-Indo-European *h₂sewt- ( “ to move about, roil, seethe ” ) , perhaps a t-extension of *(h)sew- ( “ to burn ” ) , for which see *swīþaną ( “ to burn, ache ” ) for more. Cognate with Proto-Slavic *šutiti ( “ to joke, jest ” ) , Lithuanian siaũsti ( “ to play, rage ” ) , [ 1 ] Ancient Greek ἀϋτμή ( aütmḗ , “ breath, scent ” ) . [ 2 ] 
--
344: ^ Vladimir Orel ( 2003 ), “*seuþanan”, in A Handbook of Germanic Etymology ‎ [2] , Leiden, Boston: Brill , →ISBN , page 326 
345-
346- Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Germanic/seuþaną&oldid=92150179 "
347-
```


## [2026-09-14T02:04:05.182Z] TOOL CALL #78: Bash

```json
{
 "command": "cd data/verification/sources/web && sed -n '130,200p' 4f68bd4478299d52.txt"
}
```


### [2026-09-14T02:04:05.240Z] TOOL RESULT

```
 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Perhaps an extension of *sew- ( “ to pour; squeeze ” ) .

 Root
 [ edit ] 

 *sewh₁- or *sewh₃- [ 1 ] 

 to bear (a child)

 to give birth 
 Synonym: *ǵenh₁- 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *sewH- (46 c, 0 e) 

 *séwH-tor ~ *séwH-n̥tor ( root present ) [ 2 ] [ 3 ] [ 4 ] [ 5 ] 
 Proto-Indo-Iranian: *súHtay 
 Proto-Indo-Aryan: *súHtay 
 Sanskrit: सूते ( sū́te ) 

 Proto-Iranian: *húHtay 
 Khotanese: ahvyāña- ( “ not produced, eternal ” ) ( + neg. *a- ) [ 6 ] 

 *su-né-H-ti ~ *su-n-H-énti ( nasal-infix present ) [ 2 ] [ 3 ] [ 7 ] 
 Anatolian:
 Luwian: 𒋗𒈾𒀜𒊒𒉿𒀭𒋾𒅔 ( šu-na-at-ru-u̯a-an-ti-in /⁠šunatruu̯antin⁠/ , “ rich in outpourings ” , acc.sg.c. ) 

 Hittite: 𒋗𒌦𒈾𒄿 ( šu-un-na-i /⁠šunnai⁠/ , “ fills ” , 3sg.pres.act. ) 

 Palaic: 𒋗𒌑𒈾𒀜 ( šu-ú-na-at /⁠šūnat⁠/ , 3sg.pres.act. ) 

 Proto-Indo-Iranian: *sunáHti 
 Proto-Iranian: *hunáHti [ 4 ] 
 Younger Avestan: 𐬵𐬎𐬥𐬁𐬨𐬌 ( hunāmi ) , 𐬵𐬎𐬥𐬁𐬵𐬌 ( hunāhi , “ give birth, beget ” ) 

 *se-sówH- ~ *se-suH- ( reduplicated perfect ) [ 2 ] 
 Proto-Indo-Iranian: *sasúHwa 
 Proto-Indo-Aryan: *sasúHwa 
 Sanskrit: ससूव ( sasū́va ) 

 > ? *súH-s ( “ sow > pig ” ) 

 *séwH-tus [ 8 ] 
 Proto-Celtic: *sutus 
 Old Irish: suth 

 *sowHus or *sowHows [ 9 ] 
 Proto-Anatolian: *sóʔus or *sóʔaus 
 Hittite: 𒋗𒌋𒍑 ( šu-u-uš /⁠sós/, /sɔ́ʔus⁠/ , “ full ” , nom.sg.c. ) 

 *suHnús 

 *súHs 
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: सू ( sū ) 

 *suH-tós 
 Proto-Indo-Iranian: *suHtás 
 Proto-Indo-Aryan: *suHtás 
 Sanskrit: सूत ( sūtá )
```


## [2026-09-14T02:04:12.861Z] TOOL CALL #79: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py"
}
```


### [2026-09-14T02:04:12.919Z] TOOL RESULT

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


## [2026-09-14T02:04:15.427Z] TOOL CALL #80: Bash

```json
{
 "command": "sed -n 80,140p tools/verify_check.py"
}
```


### [2026-09-14T02:04:15.540Z] TOOL RESULT

```
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


## [2026-09-14T02:05:25.871Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"soup,  n\\|soup, n\\.\" KLN_1966.txt | head -3 | cut -c1-700; echo \"=== suck/soak ===\"; grep -n \"suck,  tr\\|soak,  tr\\|soak,  intr\" KLN_1966.txt | head -4 | cut -c1-700"
}
```


### [2026-09-14T02:05:25.959Z] TOOL RESULT

```
36016:soup,  n.  — -  F.  soupe,  fr.  OF.,  which  is  of  Teut. origin.  See  sup,  ‘to  sip’,  and  words  there  referred to.
=== suck/soak ===
35756:so,  n.,  the  fifth  note  (=  G.)  in  the  scale  of  C major  ( mus .)  —  The  same  as  sol. soak,  tr.  and  intr.  v.  —  ME.  soken,  fr.  OE.  socian, in  gradational  relationship  to  OE.  sucan,  ‘to suck’.  See  suck  and  cp.  soggy,  sowens. Derivatives:  soak,  n.,  soak-age,  n.,  soak-er,  n., soak-ing,  adj.,  soak-ing-ly,  adv.,  soak-y,  adj. soap,  n.  —  ME.  sope,  fr.  OE.  sape,  which  is  rel.  to MLG.  sepe,  Du.  zeep,  OHG .  seiffa,seifa,  MHG., G.  seife,  ‘soap’,  OHG.  seifar,  ‘foam’,  and  prob. also  to  OE.  sap,  ‘resin’;  fr.  I.-E.  base  *se(i)b-, ‘tallow,  resin’,  whence  also  L.  sebum,  ‘tallow, suet,  grease�
37339:suck,  tr.  and  intr.  v.  —  ME.  suken,  souken,  fr. OE.  siican,  rel.  to  OE.  sugan,  OS.,  OHG.  sugan, ON.  suga,  Dan.  suge,  Swed.  suga,  MDu.  siighen, Du.  zuigen,  MHG.  siigen,  G.  saugen,  ‘to  suck’, and  cogn.  with  L.  sugere,  ‘to  such’,  sucus, succus,  ‘juice,  sap’,  Lett,  siizu,  sukt,  W.  sugno, ‘to  suck’.  All  these  words  derive  fr.  I.-E.  base *seuq-,  resp.  *seug-,  ‘to  suck;  sap’.  Cp.  sick, soak,  sowens,  succose,  succulent,  suction,  sugent, suggillate,  sumen  and  the  second  element  in honeysuckle.  I.-E.  bases  *seuq-,  *seug-,  are  en¬ largements  of  base  *seu-,  ‘sap,  juice;  to  squeeze, press;
```


## [2026-09-14T02:05:29.981Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:13:08.694Z] TOOL CALL #82: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-448.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nKENT = \"https://archive.org/download/old-persian-grammar-texts-lexicon/Old%20Persian%20grammar%2C%20texts%2C%20lexicon_djvu.txt\"\n\ndoc = {\n \"pdf_page\": 448,\n \"book_page\": 418,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------- ENTRY 0 ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Seu 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *sewh₁- (older notation *seu-, *seuə-, *sū-) 'to press out, extract; juice, liquid'\",\n \"note\": \"Pokorny p. 912 'Root/lemma: seu-1, seuə-: su-, Meaning: juice; liquid' — exactly Nourai's gloss. Pokorny's sub-sections are the whole of Nourai's chart: §2 Skt. sunóti 'presses' = Av. hunaoiti, soma- = Av. hauma-; §4 guttural extension seuk-/seug- (suck, soak); §6 seup-/seub- (sup, sop, soup). Watkins/AHD has the same root as 'seuə-2 To take liquid [Pok. 1. seu- 912]'. Nourai's serial number 'Seu 2' is his own house numbering (Pokorny numbers this root seu-1); the page reference 912 is correct. Modern laryngealist reconstruction: *sewh₁- (Wiktionary, s.v. Proto-Indo-Iranian *sáwmas < PIE *sówh₁-mos).\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sewh₁- (در نوشتار قدیمی پوکورنی: seu-/sū-) به معنای «فشردن، افشردن، شیره، مایع» است؛ پوکورنی در صفحهٔ ۹۱۲ همین معنا را می‌آورد و همان شاخه‌هایی را برمی‌شمارد که نورایی در نمودار آورده است: سنسکریت sunóti برابر اوستایی hunaoiti، و افزوده‌های کامی و لبی که به suck/soak و sup/soup می‌رسند. شمارهٔ «۲» ساختهٔ خود نورایی است (پوکورنی آن را seu-1 می‌نامد)، ولی ارجاع صفحه درست است. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-Iranian/s%C3%A1wmas\", \"https://www.etymonline.com/word/soup\"],\n \"ref_check\": [\n   {\"ref\": \"POK:912\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt l.74187 'Root/lemma: seu-1, seuə-: su- / Meaning: juice; liquid, *rain … Page(s): 912-913'; §2 'Old Indic sunoti “squeezes, presses” = Avestan hunaoiti … soma- = Avestan hauma-'; §6 'seup-, seub-: Old Indic sūpa- “broth, soup” … Old High German sūf “broth, soup”'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 468-470\", \"stance\": \"supports\",\n    \"note\": \"WLD_Bd2_pages.txt l.31103 'Ai. sunoti „preßt aus, keltert“ = av. hunaoiti ds., … soma-ḥ = av. hauma- m. „Soma“'; l.31157 '4. seup-, seub-: ai. sūpa-ḥ „Brühe, Suppe“'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. seuə-2\", \"stance\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt l.932-934 'seuə-2, To take liquid … [Pok. 1. seu- 912]' with soup, sop, sip, suck, soak, suction, succulent as its derivatives.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1550 s.v. suck\", \"stance\": \"supports\",\n    \"note\": \"KLN_1966.txt l.37339 'I.-E. bases *seuq-, *seug-, are enlargements of base *seu-, “sap, juice; to squeeze, press”' — Klein's base *seu- = Nourai's root.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"hau 1; haoma\", \"verdict\": \"confirmed\",\n \"derivation\": \"Bartholomae's AiW col. 1781 has ¹hav- 'auspressen, den Haoma' (to press out the haoma), present stem hunav-/hunu- (3sg. hunaoiti), ppp. huta-, PFP haosyant- — this is Nourai's 'hau 1', the superscript 1 being Bartholomae's homonym number. From the same root a -ma- noun Av. haoma- m. 'the haoma plant and its pressed juice' = Skt. sóma-, both from Proto-Indo-Iranian *sáwmas < PIE *sówh₁-mos (o-grade + *-mo-). Old Persian preserves it in the tribal name hauma-varga-, which Kent p. 211 glosses 'hauma-drinking / hauma-preparing … to root Av. hau-, Skt. su- press'. The botanical gloss is right: MacKenzie glosses Pahl. hōm 'the sacred plant Haoma (ephedra)', and ephedra = Chinese ma-huang, so 'ephedra plant, mahuang shrub' is accurate.\",\n \"derivation_fa\": \"در اوستا ستاک hav- (شمارهٔ ۱ نزد بارتولومه، ستون ۱۷۸۱) به معنای «فشردن، افشردن هوم» است؛ ماضارع آن hunaoiti و اسم مفعولش huta-. از همین ریشه و با پسوند -ma- واژهٔ haoma- ساخته شده که هم‌ریشهٔ سنسکریت sóma- است و هر دو از هندوایرانی *sáwmas می‌آیند. در پارسی باستان هم در نام قوم hauma-varga- برجای مانده است که کنت در صفحهٔ ۲۱۱ آن را «هوم‌نوش / هوم‌فشار» معنا کرده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"haoma\", KENT],\n \"ref_check\": [\n   {\"ref\": \"POK:912\", \"status\": \"supports\", \"note\": \"POK_full.txt l.74202 'Old Indic sunoti “squeezes, presses” = Avestan hunaoiti … soma- = Avestan hauma- m. “Soma”' (p. 912).\"},\n   {\"ref\": \"KNT:211\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, lexicon p. 211 (archive.org djvu text, just before the '212' page marker): 'haumavarga- adj. “hauma-drinking” or “hauma-preparing” … From hauma-, Av. haoma-, Skt. sóma- name of a plant, also a drink prepared from the juice of its crushed stems, to root Av. hau-, Skt. su- “press”'. (The local KNT.txt OCR is truncated at v-, so this was read from the archive.org copy.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1781 s.v. ¹hav-\", \"stance\": \"supports\",\n    \"note\": \"BRT.txt l.29501 '• j. ¹hav- V. “auspressen”, den Haoma. Praes. hunav-: hunu-, … PPfP. huta-' with the Vendidad/Yasna citations for pressing haoma-stalks.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 468\", \"stance\": \"supports\",\n    \"note\": \"'Ai. sunoti „preßt aus, keltert“ = av. hunaoiti ds. … soma-ḥ = av. hauma- m. „Soma“' (WLD_Bd2_pages.txt l.31103-31105).\"},\n   {\"src\": \"PHD\", \"where\": \"p. 45 s.v. Hōm\", \"stance\": \"supports\",\n    \"note\": \"PHD.txt l.398 'Hōm [hwm | N ~] the sacred plant Haoma (ephedra)' — confirms the ephedra identification of the gloss.\"}\n ]})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"howm «هوم»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Av. haoma- > Middle Persian hōm (Pahlavi spelling hwm; MacKenzie, Nyberg) > New Persian هوم hōm, later hūm by the regular New Persian raising of MP ō to ū. Horn, Grundriss no. 1113 (p. 249) sets out exactly this chain; Hübschmann cites np. hūm 'Homapflanze' = Pāzand hūm, Av. haoma-. The gloss ('a juicy plant held very holy by the ancient Aryans') is Mo'in's: his footnote to Borhan-e Qate' p. 2398 says the ancient Aryans held the plant sacred, pressed it and drank its juice, and identifies it botanically with Ephedra after Aitchison. The word is inherited, not borrowed.\",\n \"derivation_fa\": \"«هوم» از فارسی میانهٔ hōm (به خط پهلوی hwm) و آن از اوستایی haoma- است؛ واوی کشیدهٔ فارسی میانه در فارسی نو گاه به واو مجهول (hūm) بدل شده است — هوبشمان در «پژوهش‌های ایرانی» همین را می‌گوید. هرن (شمارهٔ ۱۱۱۳، ص ۲۴۹) همین زنجیره را می‌آورد و معین در حاشیهٔ برهان قاطع (ص ۲۳۹۸) می‌نویسد که آریاییان قدیم این گیاه را مقدس می‌دانستند و عصارهٔ آن را می‌آشامیدند، و گیاه را با Ephedra یکی می‌گیرد. واژه میراثی است نه وام‌واژه؛ ادعای نورایی درست است.\",\n \"sources\": [W + \"haoma\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:249\", \"status\": \"supports\", \"note\": \"HRN.txt l.9607, immediately after the page mark '— 249 —': '1113. hōm ‚Haomastrauch, -pflanze‘ … aw. haoma-; phlv. hōm; ai. soma-.'\"},\n   {\"ref\": \"BQT:2398\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:2398 (= BQT_v4_picofile.pdf pdf page 481, header هول — ۲۳۹۸) gives the entry هوم with Mo'in's long footnote: 'هرن کلمه را در فارسی … ضبط کرده و هوبشمان … در سانسکریت soma ، در اوستا haoma ، در پهلوی …' plus 'آریائیان قدیم گیاه مزبور را مقدس میدانستند و عصارهٔ آنرا … میخواندند' — i.e. exactly Nourai's gloss and derivation (OCR cached under refs/ocr/BQT/).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 45 s.v. Hōm\", \"stance\": \"supports\", \"note\": \"'Hōm [hwm | N ~] the sacred plant Haoma (ephedra)' (PHD.txt l.398) — MP hōm continued unchanged in New Persian.\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary p. 100 s.v. hom\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt l.2015 'hom [hwm] the haoma-plant, whose juice is the chief element in the Zoroastrian cult … — Av. 1732 sqq.'\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 24\", \"stance\": \"supports\", \"note\": \"HUB.txt l.4981 'hūm ‚Homapflanze‘ (vgl. hūm bei Muwaffaq p. 268, s. Horn Nr. 1113) = paz. hūm Min. Gl. 106, zd. haoma-', in the section on old ō > ū.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep هوم\", \"stance\": \"silent\", \"note\": \"Only هومر 'Homer' matches in the Aryanpur OCR; no هوم entry retrievable.\"}\n ]})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Germanic\", \"words\": \"sŭp\", \"verdict\": \"confirmed\",\n \"derivation\": \"Zero-grade of the root with a labial extension: PIE *seup-/*seub- (Pokorny §6, p. 912f.) gives Proto-Germanic *sūpaną 'to sip, swallow' (OE sūpan, OHG sūfan, ON sūpa) and the weak noun *suppō(n) 'sopped bread, broth' (OE sopp, OHG sopha/soffa 'broth, also with soaked slices'). Watkins prints the Germanic stem as *sup- and derives Old French soup(e) from it. It is that Germanic noun — not the verb — that was carried into Gallo-Romance.\",\n \"derivation_fa\": \"صورت صفر‌پایهٔ ریشه با افزودهٔ لبی (*seup-/*seub- نزد پوکورنی، ص ۹۱۲) در ژرمنی آغازین به ستاک *sūpaną «هورت کشیدن» و اسم *suppō «نان خیسانده، آب‌گوشت» رسیده است (انگلیسی کهن sopp، آلمانی علیای کهن sopha). همین اسم ژرمنی است که به زبان‌های رومانس راه یافته است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/soup\", W + \"soup\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.934 's. Possible extended zero-grade form *sub-. 1. Germanic *sip- [read *sup-] in: a. Old English sipan, sipian, to drink, sip: SUP1; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic *supp- in: a. Old English sopp, bread dipped in liquid: SOP'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 912f. §6\", \"stance\": \"supports\", \"note\": \"'6. seup-, seub-: Old Indic sūpa- “broth, soup”; Old Icelandic sūpa, Old English sūpan, Old High German sūfan “slurp, drink”, sūf “broth, soup” … Middle Low German (out of it MHG) soppe, suppe “sop”'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 469\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt l.31157 '4. seup-, seub-: ai. sūpa-ḥ „Brühe, Suppe“; aisl. sūpa „schlürfen“ … mhd. suf, sof „Suppe“'.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1552 s.v. sup, 'to sip'\", \"stance\": \"supports\", \"note\": \"Klein sends soup to 'sup, to sip' (KLN_1966.txt l.36016 'soup, n. — F. soupe, fr. OF., which is of Teut. origin. See sup, “to sip”').\"}\n ]})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"soupe\", \"verdict\": \"confirmed\",\n \"derivation\": \"The Germanic noun entered Gallo-Romance as Late Latin suppa 'bread soaked in broth' (Merovingian Latin, 6th c.), whence Old French soupe (12th–13th c.) 'sop; broth poured over bread', modern French soupe. The arrow as drawn (Germanic → French) is correct in substance but silently skips the Late Latin stage that all modern dictionaries insert; Klein says simply 'F. soupe, fr. OF., which is of Teut. origin'.\",\n \"derivation_fa\": \"واژهٔ ژرمنی از راه لاتینی متأخر suppa «نان خیس در آب‌گوشت» (سدهٔ ششم میلادی) به فرانسهٔ کهن soupe و سپس فرانسهٔ امروز soupe رسیده است. فلش نمودار (ژرمنی ← فرانسه) درست است، اما مرحلهٔ لاتینی را نیاورده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/soup\", W + \"soup\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1234\", \"status\": \"not_checked\", \"note\": \"Only the Watkins IE-root appendix of the AHD is available locally (AHD_watkins1985.txt), not the body of the 1975 New College edition where p. 1234 (s.v. soup) lies. The appendix entry seuə-2 does give 'Old French soup(e), soup: SOUP', which is the claim of this arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1487 s.v. soup\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l.36016 'soup, n. — F. soupe, fr. OF., which is of Teut. origin.'\"},\n   {\"src\": \"WEB\", \"where\": \"web: Etymonline s.v. soup\", \"stance\": \"partial\", \"note\": \"'from French soupe “soup, broth” (13c.), from Late Latin suppa “bread soaked in broth,” from a Germanic source' — same route, with the Late Latin stage the chart omits.\"}\n ]})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"sŭp «سوپ»\", \"verdict\": \"confirmed\",\n \"derivation\": \"سوپ sūp is a 20th-century loan from French soupe, taken in with the rest of French restaurant vocabulary during the Qajar/Pahlavi period; French [u] is rendered by Persian و and the final -e is dropped, giving sūp. Mo'in's dictionary tags the word [فر.] = French and glosses it 'نوعی آش رقیق که قبل از غذا خورده شود'. It is thus a distant round-trip relative, not a descendant, of Persian هوم.\",\n \"derivation_fa\": \"«سوپ» وام‌واژه‌ای است از فرانسهٔ soupe که در سدهٔ چهاردهم خورشیدی همراه با دیگر واژگان خوراک‌شناسی فرنگی وارد فارسی شده است؛ مصوت پایانی فرانسه افتاده و u به واو بدل شده است. معین نیز آن را با نشانهٔ [فر.] فرانسوی می‌داند. پس «سوپ» و «هوم» در نهایت هم‌ریشه‌اند ولی یکی از دیگری نیامده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%B3%D9%88%D9%BE\", \"https://abadis.ir/fatofa/%D8%B3%D9%88%D9%BE/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1944\", \"status\": \"supports\", \"note\": \"Mo'in's entry, read on abadis.ir (فرهنگ معین section): 'سوپ [فر.] (اِ.) نوعی آش رقیق که قبل از غذا خورده شود' — the [فر.] tag is 'French', i.e. Nourai's arrow. The same entry is in the local OCR (MON_part1.txt l.80830, French tag garbled by the OCR); the exact 6-volume page number 1944 could not be checked against the two-volume reprint on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt l.80830\", \"stance\": \"supports\", \"note\": \"'سوپ: … آب‌گوشت سبزی و حبوب، آشی رقیق شبیه شوربا' — entry present, the Latin source-word rendered '5۱0' by the OCR.\"},\n   {\"src\": \"BQT\", \"where\": \"grep سوپ in BQT_v3/v4 pages\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' is a 17th-century dictionary and has no entry for this modern loan, as expected.\"}\n ]})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"soup\", \"verdict\": \"confirmed\",\n \"derivation\": \"Middle English soupe (from Old French soupe) first means 'sop, piece of soaked bread'; the modern sense 'liquid food' is a re-borrowing of French soupe recorded from the 1650s. English thus has a doublet pair: inherited sop/sup (< OE sopp, sūpan) beside the French-mediated soup, both from the same Germanic *sup-.\",\n \"derivation_fa\": \"انگلیسی soup از فرانسهٔ soupe گرفته شده است؛ در انگلیسی میانه به معنای «نان خیس‌خورده» بود و معنای امروزی آن از حدود ۱۶۵۰ میلادی با وام‌گیری دوباره از فرانسه پدید آمده است. این واژه با sop و sup انگلیسی (میراثی) دوگانه می‌سازد. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/soup\", W + \"soup\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1234\", \"status\": \"not_checked\", \"note\": \"AHD body not on disk; the Watkins appendix (seuə-2) lists SOUP as the English outcome of Old French soup(e), which is what the arrow claims.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1487 s.v. soup\", \"stance\": \"supports\", \"note\": \"'soup, n. — F. soupe, fr. OF., which is of Teut. origin. See sup, “to sip”' (KLN_1966.txt l.36016).\"},\n   {\"src\": \"WEB\", \"where\": \"web: Etymonline s.v. soup\", \"stance\": \"supports\", \"note\": \"'“liquid food,” 1650s, from French soupe “soup, broth” (13c.)'.\"}\n ]})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Sanskrit\", \"words\": \"su\", \"verdict\": \"confirmed\",\n \"derivation\": \"Sanskrit root sú- (5th class present sunóti) 'presses out, extracts (the soma)', with sávana- 'the pressing of soma', sutá- 'pressed', sóma- 'the pressed juice'. It is the exact Indic match of Av. hav-/hunaoiti (Indo-Iranian *s > Iranian h before vowel), and Kent p. 211 pairs them in just these words: 'to root Av. hau-, Skt. su- press'. The chart's bare 'su : press' is the traditional citation form of the root.\",\n \"derivation_fa\": \"ریشهٔ سنسکریت sū-/sunóti «فشردن، افشردن سوما» برابر دقیق hav-/hunaoiti اوستایی است؛ سِ‌ایرانی در آغاز واژه به ه بدل می‌شود، بنابراین sóma- و haoma- دو صورت یک واژه‌اند. کنت در صفحهٔ ۲۱۱ همین دو را کنار هم می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [KENT, W + \"Reconstruction:Proto-Indo-Iranian/s%C3%A1wmas\"],\n \"ref_check\": [\n   {\"ref\": \"KNT:211\", \"status\": \"supports\", \"note\": \"Kent p. 211 s.v. haumavarga-: '… to root Av. hau-, Skt. su- “press”' (archive.org djvu text of the AOS edition).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 912 §2\", \"stance\": \"supports\", \"note\": \"'Old Indic sunoti “squeezes, presses” = Avestan hunaoiti; Old Indic savana-m, sava- m. “pressing of the Soma”, suta- “pressed”, soma- = Avestan hauma-'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 468\", \"stance\": \"supports\", \"note\": \"Same equation in Walde-Pokorny: 'Ai. sunoti „preßt aus, keltert“ = av. hunaoiti ds.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. seu- (1)\", \"stance\": \"partial\", \"note\": \"IEC.txt l.15287 'seu- (1) ‚start, move‘ … Skt. saumi, sávami … Av. hunàmi' — Mann files the Skt./Av. forms under a 'move, impel' root, i.e. he groups Pokorny's seu-1 and seu-3 differently.\"}\n ]})\n\ne0[\"nodes\"].append({\n \"id\": 8, \"lang\": \"Germanic\", \"words\": \"sŭk; suk\", \"verdict\": \"confirmed\",\n \"derivation\": \"Guttural extension of the root, PIE *seuk-/*seug- (Pokorny §4, p. 912), giving Proto-Germanic *sūkaną 'to suck' (OE sūcan, ON sūga, OHG sūgan) beside the shortened causative/iterative *sukōną (OE socian 'to steep, soak'), literally 'to make suck up'. Latin sūgere 'suck', sūcus 'juice' belong here too. Nourai's two forms sŭk / suk are precisely this long-grade/short-grade pair.\",\n \"derivation_fa\": \"افزودهٔ کامی ریشه (*seuk-/*seug- نزد پوکورنی ص ۹۱۲) در ژرمنی آغازین به دو ستاک رسیده است: *sūkaną «مکیدن» و ستاک سببی *sukōną «خیساندن، واداشتن به مکیدن»؛ همین دو صورتاند که نورایی با sŭk و suk آورده است. لاتینی sūgere و sūcus نیز هم‌ریشه‌اند. ادعای نورایی درست است.\",\n \"sources\": [W + \"suck\", W + \"soak\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.934 'III. Possible extended zero-grade form *sug-. 1. Germanic *sūk- in Old English sūcan, to suck: SUCK. 2. Germanic shortened form *sukōn in Old English socian, to steep: SOAK. 3. Latin sūgere, to suck … [Pok. 1. seu- 912]'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 912 §4\", \"stance\": \"supports\", \"note\": \"'4. Guttural extension: seuk-, suk- and seug-, sug-: … Old English sucan “suck”; Old English socian (*sukōn) “steep, absorb, suck”'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 469\", \"stance\": \"supports\", \"note\": \"'3. Gutturalerw.: seug, sūq und seug, sūg … ags. sucan, ags. socian (*sukōn) „aufsaugen“'.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1550 s.v. suck\", \"stance\": \"supports\", \"note\": \"'All these words derive fr. I.-E. base *seuq-, resp. *seug-, “to suck; sap” … enlargements of base *seu-, “sap, juice; to squeeze, press”'.\"}\n ]})\n\ne0[\"nodes\"].append({\n \"id\": 9, \"lang\": \"English\", \"words\": \"suck, soak\", \"verdict\": \"confirmed\",\n \"derivation\": \"OE sūcan (class II strong verb) > ME suken, souken > suck; OE socian (weak, from *sukōn-) > ME soken > soak, with OE /o/ lengthened in the open syllable and diphthongised to /oʊ/. Klein: 'soak — ME. soken, fr. OE. socian, in gradational relationship to OE. sūcan, “to suck”'; Skeat simply prints 'Soak: see Suck.'\",\n \"derivation_fa\": \"انگلیسی suck از انگلیسی کهن sūcan (فعل قوی دستهٔ دوم) و soak از انگلیسی کهن socian است؛ این دومی ستاک سببی همان فعل است و از روی ابدال مصوت («گراداسیون») با آن مرتبط است. کلاین و اسکیت هر دو همین را می‌گویند. ادعای نورایی درست است.\",\n \"sources\": [W + \"suck\", W + \"soak\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins seuə-2: 'Old English sūcan, to suck: SUCK … Old English socian, to steep: SOAK'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1465 s.v. soak; p. 1550 s.v. suck\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l.35756 'soak, tr. and intr. v. — ME. soken, fr. OE. socian, in gradational relationship to OE. sucan, “to suck”'; l.37339 'suck … ME. suken, souken, fr. OE. sūcan'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Soak\", \"stance\": \"supports\", \"note\": \"SKT.txt l.17668 'Soak: see Suck.'\"}\n ]})\n\ndoc[\"entries\"].append(e0)\n\n# ---------------- ENTRY 1 ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Seu 3, Sŭ 4, Sŭtus\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *sewH- (*sewh₁-/*sewh₃-) 'to bear (a child), give birth', with *suHnús 'son' and *suH-tó- 'born'\",\n \"note\": \"Pokorny p. 913 'Root/lemma: seu-2, (seuə-), su- / Meaning: to bear child; son', listing Skt. sūte/savati, sūtú- 'birth', sutá- 'son', Av. hav- (hunāmi), Av. hunu-š = Goth. sunus, and OIr. suth. Nourai's three head-forms map onto that entry: 'Seu 3' = Pokorny's seu-2, 'Sŭ 4' = the sū-/su- zero grade, 'Sŭtus' = the *sū-tu-s noun (Skt. sūtú-, OIr. suth). Watkins has it as 'seuə-1, To give birth … *su(ə)-nu-, son … [Pok. 2. seu- 913]'. Modern reconstruction *sewH- with *suHnús. The root label, language and gloss are all correct.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sewH- «زاییدن، به دنیا آوردن» که پوکورنی در صفحهٔ ۹۱۳ با همین معنا آورده است. سه صورتی که نورایی در سرواژه آورده همان ستاک پره، ستاک صفر (sū-/su-) و اسم *sū-tu-s (سنسکریت sūtú-، ایرلندی کهن suth) است. از همین ریشه واژهٔ *suHnús «پسر» ساخته شده که در اوستایی hunu- و گوتی sunus دیده می‌شود. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/sewH-\", W + \"Reconstruction:Proto-Germanic/sunuz\"],\n \"ref_check\": [\n   {\"ref\": \"POK:913\", \"status\": \"supports\", \"note\": \"POK_full.txt l.74273ff 'Root/lemma: seu-2, (seuə-), su- / Meaning: to bear child; son … Avestan hav- (hunami) “to give birth to children” … Indo Germanic *sunu-s … Avestan hunu-s, Gothic sunus … Page(s): 913-914'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. seuə-1\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt l.931 'seuə-1, To give birth. Suffixed zero-grade form in derivative noun *su(ə)-nu-, son, in Germanic *sunuz in Old English sunu, son: SON. [Pok. 2. seu- 913.]'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 469-470\", \"stance\": \"supports\", \"note\": \"Pokorny's own reference for this root is 'WP. II 469 f.'; Mann (IEC s.v. sūnus) likewise cites 'WP II, 470'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. sūnus\", \"stance\": \"supports\", \"note\": \"IEC.txt l.17829 'sūnus „son‘. (Gmc: sunus). WP II, 470 Skt. sūnúḥ, m. id.; Av. hunuš, pl. -avo, m. id.; Go. sunus … OE sunu'.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"hav, hunâmi; hunuš\", \"verdict\": \"confirmed\",\n \"derivation\": \"Bartholomae distinguishes four Avestan roots hav-; the third, AiW col. 1782, is '³hav- V. “gebären”, von ahurischen Wesen. Praes. hunā-', attested in the 1sg. hunāmi of Vd. 18.30f ('anaiwyāstī hunāmi'), i.e. exactly Nourai's 'hav, hunāmi'. The present is the PIE nasal-infix formation *su-né-H-ti > Proto-Iranian *hunáHti. From the same root the u-stem hunu- m. 'son' (nominative singular hunuš), which Bartholomae explicitly refers 'Zum V. ³hav-' and equates with Skt. sūnú-, Goth. sunus. Indo-Iranian *s- > Iranian h- before a vowel accounts for h- against Skt. s-.\",\n \"derivation_fa\": \"بارتولومه در فرهنگ ایرانی باستان (ستون ۱۷۸۲) ریشهٔ سومِ hav- را به معنای «زاییدن» می‌آورد که ماضارعش hunā- است و صیغهٔ hunāmi در وندیداد ۱۸ آمده است؛ این ساخت همان ماضارع با «میانوند خیشومی» هندواروپایی *su-né-H-ti است. از همین ریشه اسم hunu- «پسر» (فاعلی مفرد: hunuš) ساخته شده که هم‌ریشهٔ سنسکریت sūnú- و گوتی sunus است. سِ ایرانی آغازین در اوستایی به ه بدل شده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/sewH-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:913\", \"status\": \"supports\", \"note\": \"'Avestan hav- (hunami) “to give birth to children, Kinder zur Welt bringen” … Avestan hunu-s, Gothic sunus' (POK_full.txt l.74280-74285).\"},\n   {\"ref\": \"KLN:1473\", \"status\": \"supports\", \"note\": \"Klein s.v. son (KLN_1966.txt l.35905, on the page carrying the marker '1473'): 'Goth. sunus, “son”, and cogn. with OI. sūnúḥ, Avestic hunush, OSlav. synŭ, Lith. sūnus, “son” … All these words derive fr. I.-E. base *seu-, *su-, “to bear, bring forth; birth”'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 1782 and 1787\", \"stance\": \"supports\", \"note\": \"BRT.txt l.29512 '• ³hav- V. „gebären“ … Praes. hunā- … anaiwyāstī hunāmi V.18.30f.'; l.30389 'hunav- m. „Sohn“ … Zum V. ³hav-. — ai. sūnú- m., got. sunus'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. sūnus\", \"stance\": \"supports\", \"note\": \"'Av. hunuš, pl. -avo, m. “son”' (IEC.txt l.17829).\"},\n   {\"src\": \"KNT\", \"where\": \"Kent lexicon (OP)\", \"stance\": \"silent\", \"note\": \"Old Persian has no attested reflex of this root, so Kent has no entry; searched the archive.org text for hunu-/hauna-.\"}\n ]})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Germanic\", \"words\": \"sunuz\", \"verdict\": \"confirmed\",\n \"derivation\": \"PIE *suHnús (a u-stem verbal noun to *sewH-, literally 'the one born') > Proto-Germanic *sunuz, with the long vowel shortened in pre-tonic position (Dybo's law), whence Goth. sunus, ON sunr/sonr, OS/OFris./OE sunu, OHG sunu/sun. The exact cognates Skt. sūnú-, Lith. sūnús, OCS synъ and Av. hunuš fix the reconstruction.\",\n \"derivation_fa\": \"ژرمنی آغازین *sunuz از هندواروپایی *suHnús (اسم مصدری بر وزن -u- از ریشهٔ *sewH- به معنای «زاده») می‌آید؛ مصوت کشیده پیش از تکیه کوتاه شده است (قانون دیبو). گوتی sunus، انگلیسی کهن sunu و آلمانی علیای کهن sunu همگی از همین‌اند و با اوستایی hunuš و سنسکریت sūnú- هم‌ریشه‌اند. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Germanic/sunuz\", W + \"son\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1473\", \"status\": \"supports\", \"note\": \"Klein s.v. son, p. 1473: 'ME. sune, sone, fr. OE. sunu, rel. to OS., OFris. sunu, ON. sonr … Goth. sunus, “son”, and cogn. with OI. sūnúḥ, Avestic hunush'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. seuə-1\", \"stance\": \"supports\", \"note\": \"'*su(ə)-nu-, son, in Germanic *sunuz in Old English sunu, son: SON'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. sūnus\", \"stance\": \"supports\", \"note\": \"'sūnus “son”. (Gmc: sunus) … Go. sunus, gs: -aus, id.; OHG sunu; OE sunu; ON sunr, sonr (and com. Gmc.)'.\"},\n   {\"src\": \"POK\", \"where\": \"p. 913f.\", \"stance\": \"supports\", \"note\": \"'Indo Germanic *sunu-s and *suiu-s originally “the parturition, birth”, then “foetus, son”: … Avestan hunu-s, Gothic sunus, Old Icelandic sunr, OHG/OE sunu'.\"}\n ]})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"son\", \"verdict\": \"confirmed\",\n \"derivation\": \"OE sunu (u-stem) > ME sone/sune/sunn > NE son. The spelling with o is the Anglo-Norman scribal device for /u/ next to minim letters (as in come, love); the vowel then took part in the Middle English shortening and later STRUT unrounding, giving modern /sʌn/. Wholly regular; the node carries no reference in the book, and none is needed.\",\n \"derivation_fa\": \"انگلیسی son از انگلیسی کهن sunu است؛ نوشتن o به جای u عادت کاتبان آنگلونورمن بوده است (مانند come و love) و تلفظ امروزی /sʌn/ حاصل دگرگونی‌های منظم بعدی است. این حلقه در کتاب مأخذی ندارد و نیازی هم ندارد؛ ادعای نورایی درست است.\",\n \"sources\": [W + \"son\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node; the parent node's KLN:1473 covers the whole chain (Klein s.v. son).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1473 s.v. son\", \"stance\": \"supports\", \"note\": \"'son, n. — ME. sune, sone, fr. OE. sunu'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. seuə-1\", \"stance\": \"supports\", \"note\": \"'in Old English sunu, son: SON'.\"}\n ]})\n\ndoc[\"entries\"].append(e1)\n\n# ---------------- ENTRY 2 ----------------\ne2 = {\n \"entry\": 2,\n \"root\": \"Seu 4, Sew\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *seut- / *sew- 'to boil, seethe' (Pokorny 4. seu-, seu-t-, pp. 914-915); Watkins 'seut- To seethe, boil'\",\n \"note\": \"Pokorny p. 914 'Root/lemma: seu-4, seu-t- / Meaning: to boil, move vividly', with Av. havayąn and Germanic *seuþ-/*suþ-; Watkins prints it as 'seut-. To seethe, boil … [Pok. 4. seu- 914]'. Walde-Pokorny II 471 argues expressly that this is an independent root and 'nicht gleich zu setzen mit hav- „keltern, auspressen“ = ai. sunoti' — i.e. modern scholarship endorses Nourai's decision to keep this root separate from Seu 2. The alternate head-form 'Sew' is Nourai's cross-reference (the redirect entry on this page); modern Germanic handbooks (Orel, followed by Wiktionary) reconstruct *seuþaną from *h₂sewt-, a laryngeal-initial variant of the same t-extension.\",\n \"note_fa\": \"ریشهٔ هندواروپایی *seu-t- «جوشیدن، جوشاندن» که پوکورنی در صفحهٔ ۹۱۴ آورده است. والده–پوکورنی (جلد ۲، ص ۴۷۱) به صراحت می‌گوید که این ریشه را نباید با hav- «افشردن» یکی گرفت؛ پس جدا کردن آن از «سئو ۲» در کتاب نورایی درست است. در پژوهش امروزی (اورل و ویکی‌واژه) صورت *h₂sewt- بازسازی می‌شود. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Germanic/seu%C3%BEan%C4%85\", \"https://www.etymonline.com/word/seethe\"],\n \"ref_check\": [\n   {\"ref\": \"POK:914\", \"status\": \"supports\", \"note\": \"POK_full.txt l.74342ff 'Root/lemma: seu-4, seu-t- / Meaning: to boil, move vividly / Material: Avestan havayąn „sie schmoren“, havayeiti „erschmort“ … Germanic *sauþ- in Old Icelandic sjoða … Old English seoþan (engl. seethe) … Page(s): 914-915'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 471\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt l.31266ff '3. seu- „sieden, heftig bewegt sein“ … Av. havayąn „sie schmoren“, havayeiti „er schmort“ … nicht gleich zu setzen mit hav- „keltern, auspressen“ = ai. sunoti … Wir haben also eine selbständige Wurzel seu-.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. seut-\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt l.934 'seut-. To seethe, boil. 1. Germanic *seuthan in Old English sēothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- … [Pok. 4. seu- 914.]'\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1411 s.v. seethe\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *sew-, “to seethe, boil”' — Klein's base *sew- is Nourai's second head-form 'Sew'.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"hâvayan; hâvayeiti\", \"verdict\": \"confirmed\",\n \"derivation\": \"Bartholomae's fourth Avestan hav- (AiW col. 1782) is 'V. ‚schmoren‘' with a causative/iterative stem hāvaya-, attested in exactly the two forms of the chart: hāvayąn 3pl. (Vd. 8.73, of people who cook or roast a corpse) and hāvayeiti 3sg. (Y. 71.8, of fire that 'cuts up, roasts and burns dry wood'). Nourai's 'hâvayan' renders the nasalised ą of hāvayąn. Formally the stem is the -áya- causative of a root *hav- < *sewt-/*sew- with loss of the -t- before the suffix; Pokorny and Walde-Pokorny put these forms at the head of the 'to boil' root, and Klein cites 'Avestic hāvayeiti, “stews”' s.v. seethe. Note that Bartholomae himself leaves the etymology open ('Et.?').\",\n \"derivation_fa\": \"چهارمین ریشهٔ hav- در فرهنگ بارتولومه (ستون ۱۷۸۲) به معنای «برشته کردن، پختن» است و ستاک سببی hāvaya- دارد؛ دو صیغهٔ hāvayąn (وندیداد ۸:۷۳) و hāvayeiti (یسنا ۷۱:۸) همان‌هایی است که نورایی آورده؛ «hâvayan» همان صورت خیشومی‌شدهٔ hāvayąn است. پوکورنی و والده همین دو صورت را سر مادهٔ «جوشیدن» نشانده‌اند، هرچند خود بارتولومه ریشه‌شناسی آن را باز گذاشته است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/seethe\"],\n \"ref_check\": [\n   {\"ref\": \"POK:914\", \"status\": \"supports\", \"note\": \"'Material: Avestan havayąn „sie schmoren“, havayeiti „erschmort“ (3. Sg. Opt. huyarəs…)' (POK_full.txt l.74346).\"},\n   {\"ref\": \"KLN:1411\", \"status\": \"supports\", \"note\": \"Klein s.v. seethe (KLN_1966.txt l.34438, on the page between the '1405' and '1413' markers, i.e. p. 1411): 'fr. I.-E. base *sew-, “to seethe, boil”, whence also Avestic hāvayeiti, “stews”'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1782 s.v. ⁴hav-\", \"stance\": \"partial\", \"note\": \"BRT.txt l.29517ff '• j. ⁴hav- V. ‚schmoren‘, Praes. hu-, (Iter.) hāvaya- … nasūm hāvayąn „sie schmoren eine Leiche“ V.8.73 … hāvayeiti dažaiti Y.71.8' — forms and meanings exactly as in the chart, but the entry ends 'Et.?', i.e. Bartholomae does not commit to the IE root.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 471\", \"stance\": \"supports\", \"note\": \"'Av. havayąn „sie schmoren“, havayeiti „er schmort“ … Wir haben also eine selbständige Wurzel seu-.'\"},\n   {\"src\": \"PHD\", \"where\": \"grep hāw-/hāy- in PHD.txt\", \"stance\": \"silent\", \"note\": \"MacKenzie has no Middle Persian continuant of this verb; the root died out in Iranian after Avestan.\"}\n ]})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Germanic\", \"words\": \"siuthan; suth\", \"verdict\": \"plausible\",\n \"derivation\": \"The first form is impeccable: Proto-Germanic *seuþaną 'to boil' (Goth. *siuþan, ON sjóða, OE sēoþan, OHG siodan, G sieden) from *seut-, with Verner-free þ. The second, 'suth : swamp', is Watkins's zero-grade 'Germanic *suth-', but there the 'marsh, swamp' gloss belongs to its Middle Dutch reflex sudde/sudse, whose English outcome is SUDS, not sod; Walde-Pokorny instead reconstruct Gmc *suþa- as ON/OE sōd n. 'Fleischsuppe, siedendes Wasser, worin man Fleisch gekocht hat' ('broth'). So the stem is real and correctly placed under the root, but Nourai's gloss 'swamp' is borrowed from the Middle Dutch word rather than from the Germanic stem itself.\",\n \"derivation_fa\": \"صورت نخست درست است: ژرمنی آغازین *seuþaną «جوشیدن» (انگلیسی کهن sēoþan، آلمانی sieden). صورت دوم (suth «مرداب») همان ستاک صفر‌پایهٔ *suþ- نزد واتکینز است، اما معنای «مرداب» از آنِ هلندی میانه sudde/sudse است و حاصل انگلیسیِ آن suds است نه sod؛ والده–پوکورنی خود *suþa- را به معنای «آب‌گوشت» می‌گیرد. پس ادعا با احتیاط پذیرفتنی است و معنای داده‌شده دقیق نیست.\",\n \"sources\": [W + \"Reconstruction:Proto-Germanic/seu%C3%BEan%C4%85\", \"https://www.etymonline.com/word/seethe\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt l.934 'seut-. … 1. Germanic *seuthan in Old English sēothan: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: SUDS' — both stems are Watkins's, but the 'marsh, swamp' gloss is his gloss of the Middle Dutch noun, and its English descendant is suds.\"},\n   {\"ref\": \"KLN:1411\", \"status\": \"supports\", \"note\": \"Klein s.v. seethe: 'ME. sethen, fr. OE. seoðan, rel. to ON. sjoða … OHG. siodan … Goth. sauþs, “sacrificial animal” … Cp. sod, “turf”, sodden, suds, sutler' — Klein groups exactly Nourai's two outputs under the root.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 914f.\", \"stance\": \"partial\", \"note\": \"'Germanic *sauþ- in Old Icelandic sjóða … Old English seoþan … Germanic *suþa- in sōd n. „Fleischsuppe, broth“' — the zero-grade noun is 'broth', not 'swamp'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 471\", \"stance\": \"partial\", \"note\": \"'germ. *suþa- in sōþ n. „Fleischsuppe, siedendes Wasser, worin man Fleisch gekocht hat“'.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1554 s.v. suds\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l.37362 'suds, n. pl. … Lit. “things sodden”; rel. to MDu. sudde, “marsh, lake”, and to E. sodden and seethe' — the 'marsh' word is the MDu. one.\"}\n ]})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"seethe, sod\", \"verdict\": \"plausible\",\n \"derivation\": \"seethe is beyond doubt: OE sēoþan (class II strong, pret. sēaþ, ppl. soden) > ME sethen > seethe, driven out of its literal sense by boil and surviving in figurative use. 'sod' is the weaker half. In Nourai's own sources it is defensible: Klein lists 'sod, obsol. past tense and pp. of seethe' and also derives sod 'turf' from MDu/MLG sode 'turf', 'related to OFris. satha and to E. sodden and seethe', and Skeat writes simply 'Sod, turf; see Seethe'. But modern scholarship pulls back: Etymonline calls sod (n.1, mid-15c.) 'from Middle Dutch sode “turf” … all of uncertain origin', and Watkins's actual English derivative of Germanic *suth- is suds, with sodden (not sod) given under *seuthan. Verdict plausible: the seethe arrow is confirmed, the sod arrow rests on Klein/Skeat and is no longer the standard view.\",\n \"derivation_fa\": \"برای seethe تردیدی نیست: از انگلیسی کهن sēoþan «جوشیدن» که بعدها جای خود را به boil داد و بیشتر در معنای مجازی ماند. اما sod: کلاین و اسکیت آن را به seethe/sodden پیوند می‌دهند (اسکیت: «Sod, turf; see Seethe»)، ولی ریشه‌شناسی امروز (اتیمولاین) آن را از هلندی میانه sode «چمن‌کنده» با خاستگاه نامعلوم می‌داند و واتکینز از ستاک *suþ- واژهٔ suds را بیرون می‌آورد. پس نیمهٔ نخست قطعی و نیمهٔ دوم با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/seethe\", \"https://www.etymonline.com/word/sod\", W + \"seethe\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins seut-: 'Old English sēothan, to boil: SEETHE, (SODDEN)' — the appendix gives SEETHE and SODDEN and SUDS, but no SOD.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1465 s.v. sod; p. 1411 s.v. seethe\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l.35794 'sod, n., turf. — ME. sodde, sod, fr. MLG. or MDu. sode (Du. zode), “turf”, which is rel. to OFris. satha, “sod”, and to E. sodden and seethe. … sod, obsol. past tense and pp. of seethe'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Seethe, Sod\", \"stance\": \"supports\", \"note\": \"SKT.txt l.16828 'Seethe, to boil. (E) … A.S. seóðan, pt. t. seað, pp. soden'; l.17683 'Sod, turf; see Seethe.'\"},\n   {\"src\": \"WEB\", \"where\": \"web: Etymonline s.v. sod (n.1)\", \"stance\": \"contradicts\", \"note\": \"'“turf, slice of earth with grass on it,” mid-15c., sodde, apparently from Middle Dutch sode “turf,” or Middle Low German sode, both related to Old Frisian satha “sod” and all of uncertain origin' — no descent from the 'boil' root.\"}\n ]})\n\ndoc[\"entries\"].append(e2)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-448.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-448.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-448.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 448"
}
```


### [2026-09-14T02:13:10.102Z] TOOL RESULT

```
written
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 13, 'plausible': 2}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 15, 'not_checked': 3, 'partial': 2}
books consulted: {'supports': 31, 'silent': 4, 'partial': 5, 'contradicts': 1} | by book: {'KLN': 8, 'WLD': 6, 'POK': 5, 'BRT': 3, 'PHD': 3, 'WEB': 3, 'IEC': 3, 'SKT': 2, 'AHD': 2, 'NYB': 1, 'HUB': 1, 'ARY': 1, 'MON': 1, 'BQT': 1, 'KNT': 1}
```


## [2026-09-14T02:13:34.692Z] AGENT

Done. `verify_check.py 448` reports **0 PROBLEM lines** (15/15 nodes, 3 roots).

**Page 448 (book p. 418) — Seu 2 / Seu 3 / Seu 4** (the 4th entry, `Sew`, is a redirect and was skipped)

- Node verdicts: **13 confirmed, 2 plausible**; root verdicts: **3 confirmed**
- Ref checks: 15 supports, 2 partial, 3 not_checked · books consulted: 31 supports, 5 partial, 4 silent, 1 contradicts

Plausible items (no `disputed`, no `transcription_suspect`, no extraction errors):
- **Seu 4 #2 [Germanic] `suth : swamp`** — the stem is Watkins's Gmc *suth-, but "marsh, swamp" is his gloss of the *Middle Dutch* reflex sudde/sudse (whose English outcome is *suds*); Walde-Pokorny II 471 glosses Gmc *suþa- as "Fleischsuppe/broth". Stem correctly placed, gloss borrowed from the wrong level.
- **Seu 4 #3 [English] `seethe, sod`** — *seethe* confirmed; *sod* "turf" is backed by Nourai's own Klein (p. 1465, "rel. to E. sodden and seethe") and Skeat ("Sod, turf; see Seethe"), but Etymonline/modern work calls MDu *sode* "of uncertain origin", and AHD's derivative of *suth- is *suds*, not *sod*.

Notable findings:
- **KNT:211 verified**: the local `KNT.txt` OCR is **truncated at v-** (the h- section, pp. 211-215, is missing). Fetched the archive.org djvu text of `old-persian-grammar-texts-lexicon` instead — Kent p. 211 s.v. *haumavarga-* says verbatim "to root Av. hau-, Skt. su- 'press'", i.e. supports both the Avestan and Sanskrit nodes.
- **BQT:2398 verified** via `ref_page.py` (= BQT_v4 pdf page 481, header ۲۳۹۸): Mo'in's footnote to هوم cites Horn/Hübschmann, gives Skt soma / Av. haoma / Pahl. hōm, identifies the plant as Ephedra, and says the ancient Aryans held it sacred — exactly Nourai's gloss. OCR cached.
- **HRN:249** is a bullseye: Horn no. 1113 "hōm 'Haomastrauch' … aw. haoma-; phlv. hōm; ai. soma-".
- **MON:1944**: Mo'in's سوپ is tagged **[فر.]** (French) — checked on abadis.ir since the local OCR garbles the Latin source-word; the 6-vol page number itself couldn't be checked against the 2-vol reprint on disk.
- AHD:1234 (×2) marked `not_checked`: only the Watkins IE-root appendix is on disk, not the AHD dictionary body — but the appendix (seuə-2) does give "Old French soup(e) → SOUP".
- Worth noting for the owner: Nourai's root numbering is his own — his "Seu 2/3/4" are Pokorny's seu-1/seu-2/seu-4 — yet every page citation (912, 913, 914) is correct. Walde-Pokorny II 471 explicitly endorses keeping the "boil" root separate from the "press" root, which is what the chart does.
