# Verification process log — verify-page-108


## [2026-09-05T15:05:42.239Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 108 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-108.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-108.json. Write /home/sfmqrb/git/rishe/data/verification/page-108.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 108` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T15:05:43.646Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T15:05:44.419Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T15:05:44.436Z] TOOL RESULT

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


## [2026-09-05T15:05:44.976Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-108.txt"
}
```


### [2026-09-05T15:05:44.996Z] TOOL RESULT

```
1	=== PDF page 108 (book page 78) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dâ 1, Dâi, Di : to divide, cut in pieces  (refs POK:175)
4	#1 (parent #0) [Sanskrit] refs=POK:175; BQT:904 | dâtra : sickle ; dhâra : sword blade
5	  #2 (parent #1) [Pahlavi] refs=BQT:813 | dâs : sickle
6	    #3 (parent #2) [Persian] refs=POK:175; BQT:333,813 | dâs «داس» : sickle ; bî-das-tar «بیدستر» : beaver. An animal that cuts trees "without sickles". ☞Apo
7	  #4 (parent #1) [Persian] refs=BQT:904 | dahreh «دهره» : a sickle shaped weapon
8	#5 (parent #0) [Germanic] refs=AHD | tîmo : a period (piece) of time, time ; tîdiz : tide, used as a measure of time
9	  #6 (parent #5) [English] refs=AHD | time, tide
10	#7 (parent #0) [Greek] refs=AHD | děmos : a division of society ; děmos-keratos : people's government ☞Kar 1 ; daimôn : provider of shares, divinity ; epi-děmos : (illness) among people ☞Epi
11	  #8 (parent #7) [French] refs=None | democratie
12	    #9 (parent #8) [Persian] refs=MON:1561 |  | extra: دموکراسی ، دموکرات
13	    #10 (parent #8) [English] refs=AHD:351 | democracy
14	  #11 (parent #7) [English] refs=AHD | demography, demon, epidemic
15	#12 (parent #0) [Indo-European] refs=IEC:129; AHD:1511 | Dabh, Dâbh, Dabhn, Dap : apportion, share, one's turn or strike in battle, hurt, harm
16	  #13 (parent #12) [Avestan] refs=IEC:129 | daivis : deceit
17	  #14 (parent #12) [Persian] refs=IEC:129; MON:1492 | dâv «داو» : one's turn or strike in a game ; dâv-talab «داوطلب» : one who seeks his turn, volunteer | extra: داو دار
18	  #15 (parent #12) [Latin] refs=AHD;1511 | damnum : damage, harm (from a strike)
19	    #16 (parent #15) [English] refs=AHD | damn, damage, condemn, indemnify
20	
```


## [2026-09-05T15:05:48.172Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-108.json",
 "description": "Read page 108 source JSON"
}
```


### [2026-09-05T15:05:48.209Z] TOOL RESULT

```
{
  "pdf_page": 108,
  "book_page": 78,
  "entries": [
    {
      "root": {
        "name": "Dâ 1, Dâi, Di",
        "lang": "Indo-European",
        "refs": "POK:175",
        "gloss": "to divide, cut in pieces"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:175; BQT:904",
          "words": [
            {"translit": "dâtra", "gloss": "sickle", "script": null},
            {"translit": "dhâra", "gloss": "sword blade", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:813",
          "words": [
            {"translit": "dâs", "gloss": "sickle", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:175; BQT:333,813",
          "words": [
            {"translit": "dâs", "gloss": "sickle", "script": "داس"},
            {"translit": "bî-das-tar", "gloss": "beaver. An animal that cuts trees \"without sickles\".", "script": "بیدستر", "see": ["Apo"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:904",
          "words": [
            {"translit": "dahreh", "gloss": "a sickle shaped weapon", "script": "دهره"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "tîmo", "gloss": "a period (piece) of time, time", "script": null},
            {"translit": "tîdiz", "gloss": "tide, used as a measure of time", "script": null}
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
            {"translit": "time, tide", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "děmos", "gloss": "a division of society", "script": null},
            {"translit": "děmos-keratos", "gloss": "people's government", "script": null, "see": ["Kar 1"]},
            {"translit": "daimôn", "gloss": "provider of shares, divinity", "script": null},
            {"translit": "epi-děmos", "gloss": "(illness) among people", "script": null, "see": ["Epi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "democratie", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:1561",
          "words": [],
          "script_extra": "دموکراسی ، دموکرات",
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": "AHD:351",
          "words": [
            {"translit": "democracy", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "demography, demon, epidemic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "IEC:129; AHD:1511",
          "words": [
            {"translit": "Dabh, Dâbh, Dabhn, Dap", "gloss": "apportion, share, one's turn or strike in battle, hurt, harm", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Avestan",
          "refs": "IEC:129",
          "words": [
            {"translit": "daivis", "gloss": "deceit", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "Persian",
          "refs": "IEC:129; MON:1492",
          "words": [
            {"translit": "dâv", "gloss": "one's turn or strike in a game", "script": "داو"},
            {"translit": "dâv-talab", "gloss": "one who seeks his turn, volunteer", "script": "داوطلب"}
          ],
          "script_extra": "داو دار",
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 12,
          "lang": "Latin",
          "refs": "AHD;1511",
          "words": [
            {"translit": "damnum", "gloss": "damage, harm (from a strike)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "damn, damage, condemn, indemnify", "gloss": null, "script": null}
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


## [2026-09-05T15:05:48.925Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T15:05:48.961Z] TOOL RESULT

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


## [2026-09-05T15:06:27.800Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py; echo ---; ls data/verification/ | head -50",
 "description": "Inspect verify_check tool"
}
```


### [2026-09-05T15:06:27.845Z] TOOL RESULT

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
---
agent
page-100.json
page-101.json
page-102.json
page-103.json
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
page-66.json
page-67.json
page-68.json
page-69.json
page-70.json
page-71.json
page-72.json
```


## [2026-09-05T15:06:29.908Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','AHD','IEC','MON','PHD','HRN','HUB','BRT','WLD','KLN','SYN','LEW','ARY']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-05T15:06:31.836Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-05T15:06:36.869Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==183' POK_01.txt | head -80",
 "description": "Print Pokorny p.175"
}
```


## [2026-09-05T15:06:38.577Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"dāp-\\|dap-\\|damnum\" AHD_watkins1985.txt | head -30; echo ===; grep -n \"^dā-\\|dā-. To divide\\|To divide\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-05T15:06:38.742Z] TOOL RESULT

```
 ndd.  brüsken  da? mhd.  bräsche  ^Brause,  Wasserbrause^  aschwed.  brüsa  ,einherstürmen<i norw.  mdartl.  brösa  ^SturmböeS  aisl.  brusi  ^Ziegenbocke  isl.  bruskr  ^Büschel Besen^  engl,  brush  .Bürste,  Pinsel,  Quast,  Schwanz  (des  Fuchses/,  bi-us) loood  ,Gebüsch,  Gestrüpp^  mengl.  bruschen,  engl,  to  brush  ,mit  Kraft  sic| stürzen'^,  norw.  dial.  brauska^  bruska  und  brausta,  brusta  ,sich  Ram machen,  sich  gewaltsam  hervordrängen';  schwed.  bruska  ,knistern,  lärmeu'J
Mit  germ.  Hruska-z  ,GestrüppS  Hruskan  ,knistern'  {-sk-  kann  idg.  z^ sein)  vergleicht  man  die  baltoslav.  Gruppen  lit.  bruzgai  PI.  ,Gestrüppf briauzgä  ,Schwätzer',  bruzgii,  4ti  ,rascheln',  russ.  brjuzgdju,  -dth  ,murmeln< brjuzzdth  ,brummen,  murren,  knurren'  usw.;  doch  sind  die  Verba  vielleichj eine  erst  baltoslav.  Schallbildung.  Wegen  der  germ.  Bed.  ,spritzen'  is vielleicht  andererseits  russ.  bryzgaju,  -ath  ,spritzen,  sprühen'  usw.  zu' vergleichen.
WP.  II  199  f.,  Trautmann  38.
bbroisqo-,  bhrisqo-  ,herb  von  Geschmack'.
Russ.-ksl.  obrezgnuti,  obrhzgnuti  ,sauer  werden',  cech.  bresk  ,herber  Ge-^^ schmack',  poln.  brzazg  ,unangenehmer,  herber  Geschmack;  üble  LauneVgl^ russ.  brezgdth  (alt  brezgati)  ,sich  ekeln' ;  zunächst  zu  norw.  bj^isk  ,bitterer  ^^: Geschmack',  brisken  ,bitter,  herbe';  wohl  zu  bhrei-  ,schneiden'  (wie  mndl.  Ji; brine  ,Salzwasser').  V.
WP.  II  206.
j.  bhrü'  , Augenbraue',  z.  T.  mit  anlautendem  Vokal,  idg.  o-  oder  a-  (vollere  v Wurzelform?);  nach  Persson  Beitr.  17  liegt  ein  verdunkeltes  Kompo-J^; sitionsglied  "^oku-  ,Auge'  (mit  Kons.-Assimilation)  vor.  y'
Ai.  bh'ü-h  f.,  Akk.  bhrüv-am  ,Braue',  aA^  brvat-  f.  (Du.)  ,Brauene  npers.  T ehm,  brü  ds.  (Hübschmann  lA.   10,  24);
gr.  öq)Qvg,  -vog  f.  ,Braue',  übertragen  .erhöhter  Rand,  Hügelrand*  (nach  | Meillet  BSL  27,  129 f.  mit  griech.  Vokalprothese?);
maked.  dßQOvreg  ,dcpQveg'  (von  Kretschmer  Einl.  287  in  äßqovfeg  geän- dert; von  Meillet,  s.  Boisacq  733  Anm.  3,  wegen  der  anderweitig  bezeugten Form  äßqoxeg  und  wegen  av.  brvat-  festgehalten);
mir.  brüad  Gen.   Du.,  bräi,  bröi  Nom.  Du.  f.  ,Brauen'  (zum  Diphthong  W s.  Thurneysen  Grammar  199),  air.  forbru  Akk.  PL  (*bhrüns  :  A
```


### [2026-09-05T15:06:38.786Z] TOOL RESULT

```
Exit code 1
162:This principle has left clear traces in the Indo-European vocabulary. The root d6- of Latin déndre means “to give” in most dia- lects but in Hittite means “to take.” The root nem- is “to distribute” in Greek (NEMESIS), but in German it means “to take,” and the cognate of English GIVE (ghabh-) has the meaning “to take” in Irish. The notion of exchange predominates in the roots skamb- and gher-5. The root dap- means “to appor- tion in exchange,” which may also carry a bad sense; Latin damnum is “damage entail- ing liability.” The GuEsT (ghos-ti-) in Indo- European times was the person with whom one had mutual obligations of hospitality. But he was also the stranger, and the stran- ger in an uncertain and warring tribal society may well be hostile; the Latin cognate hostis means “enemy.”
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
375:mild, gentle: DAFT. 2. Probably suffixed form *dhabh-ro- in Latin faber, artisan (< “he who fits together”): FABRIC, (FABRICATE), FORGE}. [Pok. 2. dhabh- 233.] dhal-. To bloom. Suffixed form *dhal-yo- in Greek thal- lein, to flourish, bloom, sprout (> thallos, a shoot): THALIA, THALLUS; PROTHALLUS. [Pok. dhail- 234.] dhé-', To set, put. Contracted from *dheo-. 1. O-grade form *dhé- in Germanic *don in Old English dén, to do: Dol; FORDO. 2. Suffixed form *dhé-ti-, “thing laid down or done, law, deed,” in Germanic *dédiz in Old English déd, doing, deed: DEED. 3. Suffixed o-grade form *dho-mo- in Germanic *démaz in: a. Old English dom, judgment (< “thing set or put down”): Doom; b. Old English -d6m, abstract suffix indicating state, condition, or power: -DOM; c. Old Norse -démr, condition (see ka-); d. Gothic déms, judgment, akin to the Germanic source of Russian Duma, Duma: Duma; e. Germanic denomina- tive *“ddmjan in Old English déman, to judge: DEEM. 4. Suffixed o-grade form *dhé-t- in Latin agential suffix -dés in Latin sacerdés, priest, “(performer of sacred rites” (see sak-). 5. Zero-grade form “dha- in: a. prefixed form *kom-dha- in Latin condere, to put together, establish, preserve (*kom, together; see kom): CONDIMENT; AB- SCOND, INCONDITE, RECONDITE, SCONCE?; b. compound *kred-dha- (see kerd-'). 6. Suffixed zero-grade form *dha-k- in: a. Latin facere (< *fak-yo-), to do, make (> French faire, to do), and Latin combining form -fex (< *.fak-s), “maker”: -FACIENT, FACT, FACTION, FACTITIOUS, FACTOR, FASHION, FEASIBLE, FEAT!, FEATURE, (FETISH), -FIC, (-FY); AFFAIR, AFFECT!, (AFFECT2), (AFFECTION), AMPLIFY, ARTIFACT, ARTIFICE, BEATIFIC, BENEFACTION, BENEFIC, (BENEFICE), (BENEFICENCE), BENEFIT, CHAFE, COMFIT, CONFECT, (CONFETTI), COUNTERFEIT, (DEFEA- SANCE), DEFEAT, DEFECT, (DEFICIENT), (DISCOMFIT), EDIFICE, (EDIFY), EFFECT, (EFFICACIOUS), (EFFICIENT), FACSIMILE, FACTOTUM, FORFEIT, HACIENDA, INFECT, JUSTIFY, MALEFACTOR, MALFEASANCE, MANUFACTURE, MISFEASANCE, MODIFY, MOLLIFY, NIDIFY, NOTIFY, NUL- LIFY, OFFICINAL, PERFECT, PETRIFY, (PLUPERFECT), PON- TIFEX, PREFECT, (PROFICIENT), PROFIT, PUTREFY, QUALIFY, RAREFY, RECTIFY, REFECT, (REFECTORY), RU- BEFACIENT, SACRIFICE, SCIRE FACIAS, SPINIFEX, SUF- FICE, (SUFFICIENT), SURFEIT, TUBIFEX, TUMEFACIENT, viviry; b. Latin derivative faciés, shape, face (< “form imposed on something”): FACADE, FACE, (FACET), (FA- CIAL), FACIES; (DEFACE), EFFACE, PRIMA FACIE, (SUR- FACE); c. Latin compound officium (< *opi-fici-om), service, duty, business, performance of work (*opi-, work; see op-'): OFFICE; d. further suffixed form *dha-k-li- in Latin facilis (< Old Latin facul), feasible, easy: FACILE, (FACILITY), FACULTY; DIFFICULTY. 7. Suffixed zero-grade form *dha-s- in Latin fds, divine law, right: NEFARIOUS. 8. Possibly Latin -farius, -doing: MULTIFARIOUS, OMNI- FARIOUS. 9. Reduplicated form *dhi-dhé- in Greek tithe- nai, to put: THESIS, THETIC; ANATHEMA, ANTITHESIS, APOTHECARY, (APOTHECIUM), BODEGA, BOUTIQUE, DI- ATHESIS, EPENTHESIS, EPITHET, HYPOTHESIS, METATHE- SIS, PARENTHESIS, PROSTHESIS, PROTHESIS. 10. Suffixed form *dhé-k- in Greek théké, receptacle: THECA, TICK?; AMPHITHECIUM, BIBLIOTHECA, CLEISTOTHECIUM, ENDO- THECIUM, PERITHECIUM. 11. Suffixed zero-grade form *dha-mn in Greek thema, “thing placed,” proposition: (THEMATIC), THEME. 12. Reduplicated form *dhe-dhé- in Sanskrit dadhdti, he places: SANDHI. 13. Reduced form *dh- (see aw-2). [Pok. 2. dhé- 235.] dhé-2. To vanish. Contracted from *dhea-. 1. Possibly Old Norse d%sa, to languish, decay: DASTARD. 2. Possibly Old Norse *dasa, to tire out (attested only in reflexive form dasask, to become exhausted), akin to the Scandi- navian source of Middle English dasen, to stun: DAZE. [Pok. 3. dhé- 239.] dheb-. Dense, firm, compressed. Germanic suffixed form *dap-ra- in Middle Dutch and Middle Low German
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1409:Dart dhabh- DAINTY dek-1 DAIRY dheigh- DAISY agh-2, okw- DALE dhel- DALLES dhel- DAMAGE dap- DAME deme-! DAMN dap- DAMNIFY dap- Dan? deme-! DANDELION dent- DANE dan- DANEGELD gheldh- DANELAW dan-, legh- DANGER deme-1 DaNIsH dan- DAPPER dheb- DARE dhers- DARK dher-! DASTARD dhé-2 DASYURE dens-2 DATE do- DATIVE do- DATUM do- DAUB _albho- DAUGHTER dhugheter- DAUNT deme-2 DAWN agh-2
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
(eval):1: == not found
```


## [2026-09-05T15:06:46.400Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"zerschneiden, zerreißen\\|zerschneiden,  zerreißen\\|dāi-\\|dai-, dī-\" POK_full.txt | head -20; echo \"=== POK_01 leaf scan\"; for n in 180 181 182 183 184 185; do echo \"--- leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_01.txt | head -3; done",
 "description": "Locate Pokorny dā- entry"
}
```


## [2026-09-05T15:06:48.385Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"TIDE \\|TIME \\|DEMOCRACY\\|DEMOGRAPHY\\|DEMON \" AHD_watkins1985.txt | head; echo === ; grep -n \"dā-. To divide\\|d4-. To divide\\|To divide. 1\\|dai-\" AHD_watkins1985.txt | head",
 "description": "Grep AHD for time/tide/demos root"
}
```


### [2026-09-05T15:06:48.464Z] TOOL RESULT

```
=== POK_01 leaf scan
--- leaf 180
reu-,  bhreu-d-  m.  ,sprießen,  schwellend
Lat.  friitex,  -icis  m.  ,Staude,  Strauch,  Gesträuch^  beruht  wohl  auf  einem Partiz.  *bhrütös  ,hervorgesprossen^ ;  air.  broth  ,Granne,  Haar^;  hierher das  (Z-Präsens:  mhd.  briezen,  bröz  ,knospen,  schwellen^,  ahd.  mhd.  broz ,Knospe,  Sprosset  Vgl.  1.  bJireu-s-  ,schwellen''',  bhriigJino-  , Zweigt
WP.  II  195,  WH.  I  554.
--- leaf 181
  ,streichen^ (mit  unursprüngl.  Intonation)  und  lit.  brükis  m.  ^Streifen,  Strich*,  lett. brüce  f.  ,Schramme,  Narbe^,  dazu  lit.  brukne^  brukms  f.,  lett.  briiklem f.  , Preiselbeere^;
slav.  Hrusg  *brusiti  (ursprgl.  Iterativ)  in  bulg.  brüsja  (briurtch)  ,ab-^ schütteln,  abschlagen^,  skr.  brusim  brüsltl  , wetzen^,  cech.  brousiti  ds. ' dazu  aksl.  ubrxLST>  ,Schweißtuch'^,  skr.  brüs  (Gen.  brüsa)^  russ.  brus  (Gen. brusa]  meist  brusök)  ,Schleifstein^;  russ.  usw.  brusnika  ,Preiselbeere' (,leicht  abstreifbar^);  ablaut.  r.-ksl.  bnsmiti  ,schaben,  rasieren^,  russ.  brosdU (dial.  brokdt'b),  brösith  .werfen^,  brösnuth  ,Flachs  riffeln^,  bros  ,AbfalF  usw. im  Ablaut  zu  bulg.  briH  ,reibe  ab^  Mit  m  der  Iterativstufe:  aksl.  sirbrysati ,abschaben'^,  brysalo  ,penicillus^
Vielleicht  hierher  skr.-ksl.  bruU  ,Nagel',  bulg.  brut  ds.  als  *brukh,  vgl. zur  Bed.  lit.  brükti  ,mit  Gewalt  hineinstecken^,  zur  Form  lett.  braukts ,Messer  zum  Flachsreinigen*.
--- leaf 182
.  bi-iost  N.  PL,  ag's.  breost,  aisl.  5?'ios^  ^Brusf^,  schwund- stufig' go^-  brusts  f.  PL,  ahd.  6?*?<5^,  nhd.  Bmist]  as.  brustian  ^knospen^ (slav.  ^bTbsU  Jvnospe^),  nhd.  Brös-chen  (aus  dem  md.)  , Brustdrüse  des Rindes';  schwäb.  Brüste,  bair.  Brilsel,  Briesel,  Bries  ds.,  dän.  brissei, scliwed.  halfbräss,  mit  Ä:-Suffix  dän.  bryske,  engL  brisket  ^Brust  der  Tiere^
AisL  briösk  ^Knorpel^,  mhd.  h-üsche,  nhd.  Brausche  ^Beule^^  nhd.  diaL hrausche,  brauschig  ^turgidus^  wulstig^^  brauscJien  ,aufschwellen^
Russ.  brjücho  ^Unterleib,  Bauch,  Wanst^,  diaL  brjüchnuth  , weichen, quellen,  anschwellen^,  cech.  alt.  brück,  bfucho,  heute  brich,  bficho  ,Bauch* usw.  {*bhreuso-s,  -m);
--- leaf 183
 ndd.  brüsken  da? mhd.  bräsche  ^Brause,  Wasserbrause^  aschwed.  brüsa  ,einherstürmen<i norw.  mdartl.  brösa  ^SturmböeS  aisl.  brusi  ^Ziegenbocke  isl.  bruskr  ^Büschel Besen^  engl,  brush  .Bürste,  Pinsel,  Quast,  Schwanz  (des  Fuchses/,  bi-us) loood  ,Gebüsch,  Gestrüpp^  mengl.  bruschen,  engl,  to  brush  ,mit  Kraft  sic| stürzen'^,  norw.  dial.  brauska^  bruska  und  brausta,  brusta  ,sich  Ram machen,  sich  gewaltsam  hervordrängen';  schwed.  bruska  ,knistern,  lärmeu'J
Mit  germ.  Hruska-z  ,GestrüppS  Hruskan  ,knistern'  {-sk-  kann  idg.  z^ sein)  vergleicht  man  die  baltoslav.  Gruppen  lit.  bruzgai  PI.  ,Gestrüppf briauzgä  ,Schwätzer',  bruzgii,  4ti  ,rascheln',  russ.  brjuzgdju,  -dth  ,murmeln< brjuzzdth  ,brummen,  murren,  knurren'  usw.;  doch  sind  die  Verba  vielleichj eine  erst  baltoslav.  Schallbildung.  Wegen  der  germ.  Bed.  ,spritzen'  is vielleicht  andererseits  russ.  bryzgaju,  -ath  ,spritzen,  sprühen'  usw.  zu' vergleichen.
WP.  II  199  f.,  Trautmann  38.
--- leaf 184
kk.  ö(pQvg)f  M fm^brü  Gen.  PL  ,supercilia';    unklar  sind  mir.  PL   abrait  (*abrant-es  oder  -^' *abranti)  , Augenlider,    Brauen',   desgleichen    mbr.    abrant   ,Braue',    cjmr.    ^ amrant  ,Augenlid',  die  Specht  (Dekl.  83,  162)  zu  lat.  fröns  ,Stirn'  stellen möchte;  aber  Vokalismus  und  Bedeutung  weichen  ab;
173
^trs.  hrü,  aisl.  hrürij  PL  brynn  ^B^-aue^  (kons.  St.,  aus  *brutoün-,  vgl. *ULiuiün,  tungo,  kontrahiert  und  dadurch  zur  flexivischen  Sonderentwicklung geUaügt).
--- leaf 185
),  daraus  ent lehnt  arm.  bun  ds.,  während  arm.  an-dund-lc  ^Abgrund^  aus  *bhundl assimiliert  scheint.  Aus  uriran.  *bundhas  stammt  tscherem.  pundas  ^Boden^
Gr.  Ttv&^rjv  (*cpvd'-)  m.  ,Boden,  Fuß  eines  Gefäßes^  nvvöa^  m.  ds.  (f (pvvda^  nach  Ttv-d-f-ii^v,  Schwyzer  Gr.  Gr.  I  71,  333).
Maked.  ON  TLvöva  (*bhudhna),  dissimil.  Kvöva?
```


### [2026-09-05T15:06:48.507Z] TOOL RESULT

```
Exit code 1
159:community may have been grouped into divi- sions by location; this seems to be the basic meaning of the *dd-mo- (from da-) in Greek démos, people (DEMOCRACY).
355:da-. To divide. Contracted from *dag-. Variant *dai- from extended root *dagi-. 1. Root form *dai- in Greek daies- thai, to divide: GEODESY. 2. Suffixed variant form “di-t- in Germanic *tidiz, division of time, in: a. Old English tid, time, season: TIDE!; EVENTIDE; b. Old English de- nominative tidan, to happen (< “to occur in time”): TIDE?; c. Old Norse tidhr, occurring: TIDINGS. 3. Suffixed variant form *di-mon in Germanic *tim6én- in Old Eng- lish tima, time, period: TIME. 4. Suffixed form *dd-mo-, perhaps “division of society,” in Greek démos, people, land: DEME, DEMOS, DEMOTIC; DEMAGOGUE, DEMIURGE, DEMOCRACY, DEMOPHOBIA, ENDEMIC, EPIDEMIC, PAN- DEMIC. 5. Suffixed form *dai-mon-, divider, provider, in Greek daimén, divinity: DEMON. [Pok. dé- 175.]
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1419:DEMENT men-1 DEMETER mater- DEMILUNE leuk- DEMIT (s)meit(a)- DEMIURGE da-, werg- DEMOCRACY da- DEMOLISH mé6- DEMON da- DEMONSTRATE men-! DEMOPHOBIA da- DEMOS da- DEMOTIC da- DEMUR mere- DEN dan- DENARIUS dekm DENARY dekm DENDRO- deru DENDRON deru DENIER? dekm DENIGRATE negW-ro- DENOMINATE no-men- DENOUEMENT ned- DENOUNCE neu-! DENSE dens-2 DENTAL dent- DENTATE dent- DENTI- dent- DENTICLE dent- DENTIFRICE bhréi- DENUDE nogw- DENY ne
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
1818:MARE? mori- MARGARIC margarités MARGARIC ACID margarités MARGARINE margarités MARGARITE! margarités MARGARITE2 margarités MARGIN merg- MARGRAVE gravo-, merg- MARICOLOUS mori- MARICULTURE mori- MARINARA mori- MARINE mori- MARITAL mari- MARITIME mori- MARK! merg-
1903:NAY aiw-, ne NEAP TIDE ken-2 NEAR néhw-iz
2389:THYME dheu-! -THYMIA dheu-1 THYROID dhwer- TICK? deigh- TICK3 dhé-1 TICKET steig- TIDE! da- TIDE2 da- TIDINGS da- TIE deuk- TIERCE trei- TIFFANY bha-1 TIGER steig- TIGHT tenk-2 TILE (s)teg- TILLER? teks- TILLERS del-3 TILT? del-3 TIMBER deme-1 TIME da- TIMOCRACY kWeig-1 TINCT teng- TINGE teng- TINSEL skeei- TINT teng-
(eval):1: == not found
```


## [2026-09-05T15:06:58.112Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 186 187 188; do echo \"=== leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_01.txt; done",
 "description": "Print POK leaves 186-188"
}
```


### [2026-09-05T15:06:59.741Z] TOOL RESULT

```
=== leaf 186
 ame  yFettj  Speck,  Talg^  in  noch  nicht  geklärter  Weise  zusammenhängt; das  Fett  kann  als  das  beim  Braten  flüssig  werdende  benannt  sein  (vgl. aksl.  loj  ,adeps'^  :  lijati  ,gießen^).  Hierher  auch  kelt.  Dänuvius  ,Donau'^, gall.  ON  Condäte  ,Confluens^;  sechs  engl.  Fl  Don  (*dänu-)j  cymr.  FIN Donwy  (*dänuuia).
Benveniste  stellt  zu  arm.  tam-uk  noch  hett.  dame{ii)k-  ,als  Regen  fallen' (BSL  33,  143).  -
WP.  I  763,  M.Förster  Tkemse  145 f.,  Kretschmer  Gl.  24,  1  ff.,  15 ff., Mel.  Pedersen  76  ff.,  Benveniste  BSL  33,  143.
da  :  dg-  und  däi-  :  d9i  :  di-  ,teilen,  zerschneiden,  zerreißen',  ursprgl.  athemat. Wurzelpräsens;    Nominalbildungen    dä-mo-s  f.  ,Volksabteilung',   dä- ter-   ,Zerleger',   dä-tro-m  ,Zugeteiltes',   dä-tu-   ,Teil',   ddi-lO'  ,Teil-, di-t-  ,Zeitabschnitt'. Ai.  däfi,  dydti  ,schneidet  ab,   mäht,   trennt,  teilt',  Partiz.  dind-h,  ditd-hj komponiert  ava-ttah  ,abgeschnitten',  diti-h  ,das  Verteilen',  dänam  ,das  Ab- schneiden', dändm  n.  , Verteilung,  Teil',  dätu  n.  ,Teil',  dätdr-  m.  (=  Sai- 'TQÖg)    ,Schnitter',    däträm    , Zugeteiltes',    dätram    n.    ,Sichel',    npers.    dära ,Gehalt',  das  ,Sichel';  ai.  dayä  ,Teilnahme,  Mitgefühl'  =  ddyate  (^ddi-etai) ,teilt,  nimmt  Anteil,  hat  Mitgefühl;  zerstört'.
gr.  daioiiai  med.  ,teile,  verteile'  mit  wohl  nach  Fut.  daiaoi  und  den folgenden  Worten  bewahrtem  i  (lautgesetzlich   ddrjTat  Konj.  0  375  ,wird
176
zerstört);  daig^  -rög,  dairrj,  hom.  auch  daityq,  -voq  ,Portion^  Mahl^  Opfer'  (; dätu)]    SairvfKbv  ^Gast'  (als  ^dem  Mahle    beiwohnend'),   dairgög  ,der   Y^ Schneider' (:  ai.  c^ä^ar-),   daitgöv  jPortion^  (:  Si.i.  dätrdm]    das   ai   dieser  i Worte  ist  teils  lautgesetzlich  —  äi,  di  — ,  teils  analogisch,  wie  im  kr? Perf.    dedaia^ai    zu    öarso^uaL,    vgl.    auch    kret.   daTaig    ^Teilung',    xa^? daiaxal  ^Verteiler  von  Früchten'),  daivvj^i  ,bewirte^  wohl  auch  Salftcov ,Gott,  Göttin;  Geschick'  (eigentlich  ,zuteilend;  oder  ,Totengott  als  LeicheJ fresser',  Porzig  IF.  41,  169 ff.,  Kretschmer  Gl.  14,  228 f.;   über  des  Arcl lochos  daliJ,cov  ^darjf.Lcov''  s.  u.  *dens-  ,hohe   Geisteskraft');    öalZw,  Fut.  -[ Aor.  -fa  ,teilen,  zerschneiden,  zerstören'  (auf  Grund  eines  *dä-J^6-g  ,z^ schnitten,  zerstört'),  U-öaxog'  dtöialQsrog  Hes.y  ödvog  n.  ,Zins,  Wucher' (s Grund  eines  Partiz.  *dd-n6-s  =  ai.  dind-hj  vgl.  ddvag'  fisglöag)]
gall.  arcanto-danos  ,monetarius'  als  ,das  Silber  verteilend'.
Mit  Formans  -mo-  :  dämos  f.  ,Volk' :  gr.  dfjf.Log,  dor.  öänog  m.  ,(Voll abteilung)  Volk,  Gebiet;  in  Atben  der  einzelne  Gau',  air.  däm  f.  ,Gefolj Schaft,  Schar',
=== leaf 187
  acymr.  dauii  ,cliens',  ncymr.  daw^  daiof  ,Schwiegersohn4 offenbar  alter  fem.  o-Stamm;  dazu  hett.  da-ma-a-is  (damai§?)  ,ein  Andere Fremder',  aus  ,*fremde  Leute',  ursprgl.  ,*Volk',  Pedersen  Hitt.  51  ff.
Mit  Formans  -lo-  vielleicht  aksl.  däh  ,Teil'  (*ddi-lo-)  (s.  unter  *di , spalten');  über  air.  fo-dälim  usw.  s.  ebendort.  Hierher  gehört  wohl  auci got.  dails  ,Teil',  runeninschr.  dali]lipun  ,teilten',  aisl.  deillj  ags.  dcel,  ahc teil  m.  ,Teil';  aisl.  deila  f.  ,Teilung,  Zwiespalt',  ahd.  teila  f.  ,Teilun^ aisl.  deila j  ags.  döelan,  ahd.  teilan  ,teilen'  usw.  Sie  können  kaum  aus  dei SlaA^,  wohl  aber  aus  dem  Ven.-IUyr.  stammen,  da  die  Wzlform  "^ddi-  ii südillyr.  PN  Dae-tor  bezeugt  ist.  Eine  Nebenform  idg.  dhdi-  neben  ddi Aväre  unglaubhaft.
Mit  Tiefstufe  di-  :  arm.  ti.  Gen.  tioy  ^Alter,  Jahre,  Tage,  Zeit'  {*di-t[^ oder  *dl-to-y  "^di-tä),  ahd.  zU  f.  (n.  Isidor),  as.  ags.  tid,  anord.  tid  f.  ,Zeit Stunde'  {*tip-,  idg.  *dl-t-,  ursprgl.  ,Zeitabschnitt'),  dazu  anord.  fidr  ^üblich^ häufig',  ags.  tldan  ,vorfallen',  anord.  tida  ,trachten,  streben';  anord.  tl-i ,zerpflücken,  einzeln  herausnehmen,  ausscheiden,  reinigen';
über  got.  til  ,passend'  usw.  s.  unter  2.  ad-,  über  got.  dails  unter  3.  <ZeZ;|
hierher    dagegen    ahd.   zlla   ,Reihe,    Linie'^    westfäl.    tue   ,Garbenreihe';J nhd.  Zeile,  wohl  aus  *tld-ld-.
p-Er Weiterung  däp-,  dQp-:  dop-no-,  -ni-  , Opfermahl': ai.  däpayati  ,teilt';  arm.  taun  (*dap-ni-)  ,Fest';  gr.  ddjtTü)  {*da7ti(ü)\ .zerreiße,  zerfleische,  zerlege',  mit  Intensivredupi.  Sagdamü)  ,zerreiße, {yiTTjfAaTa)  verprasse',  öanavri  f.  ,Aufwand,  besonders  aus  Bewirtung  (;  dafi} erwachsender',  dartavog  ,verschwenderisch',  öartaväa}  ,wende  auf  (daraus^ lat.  dapinö  ,tische  auf),  öaipdög  (Empedokles),  öayjdrjg  ,(*verschwenderisch)j
üppi^;
177 reichlich;    freigebig^;    lat.    daps    /^Portion)    Mahl^   Schmaus,    bes.
'  f  »niiahl*  dammim  ^Verlust,  Schaden,  Nachteil,  Geldbuße^,  damnösus  ,ver- A  blich^  (*dap-no-  :  öaTiavt],  anders  Pedersen  Hitt.  42);  anord.  tafn  (*dap- )  Opfertier,  OpfermahF,  vgl.  den  germ.  GN  Tanfana  (Tacit.),  wenn US  *tafnana,  Marstrander  NTS.  1,  159.
Aus  dem  Genn.  reiht  man  noch  vieles  an,  was  eine  Bed.-Entw.  von «erteilen^  zu  ,zerreißen,  zupfen,  kurz  betasten,  kurze  täppische  Bewegun- gen machen^  u.  dgl.  voraussetzen  würde;  am  nächsten  der  Bed.  von  öa- naväv  damnum  kommt  aschw.  tappa  und  iapa  ,ein  Ende  machen,  ver- lieren^;  aisl.  tapa  ds.;  afries.  tapia  ,zupfen^,  ags.  tssppe  f.
=== leaf 188
  ,Tuchstreifen^, meno-1.  tappen  (engl,  tap)  ,leicht  schlagen^,  mnd.  tappen,  täpen  (Dehnung in  offener  Silbe?)  ,zupfeu,  pflücken*^;  anord.  tcepr  ,kaum  anrührend^,  isl. i4h)ta  (*täpatjan)  ,eben  anrühren^,  norw.  mdartl.  tcepla  ,leicht  berühren, leise  treten^;  aber  norw.  mdartl.  taap{e)  m.,  dän.  taahe  ,Tor,  Tropf,  täp- pischer Mensch^,  norw.  taapen  ,schwach,  kraftlos,  untauglich^,  tcepe  n. unbedeutendes  Ding^,  anord.  föepiligr  ,knapp^,  mit  anderen  Labialstufen 8chwed.  mdartl.  tahh,  tahhe  ,Tölpel^,  tahhet  ,einfältig^,  sind  wohl  Schall- worte, ebenso  wie  ndd.  tappe,  Schweiz,  täpe,  nhd.  Tappe  ,Pfote^,  sowie iavpen,  täppisch  usw.;  s.  auch  unter  1.  dhabh-.
Ebenfalls  fernzuhalten  sind  ahd.  zahalön,  nhd.  zappeln,  sowie  ahd. zapfo,  nhd.  Zapfen,  ags.  txppa  ds.  (germ.  *tappon-)]  ebenso  nur  germ. Worte  mit  i  und  u  (vgl.  Specht  Dekl.  152 f.):  mengl.  tippen,  engl,  tip ,loise  anrühren,  leise  stoßen^,  nhd.  tippen,  mhd.  zipfen  ,(in  kurzen  Bewe- gungen) trippeln^,  anord.  tifask  ,trippeln^,  mhd.  zipf  ,Zipfel,  Spitze^, nasaliert  mnd.  timpe  f.  , Zipfel,  Ende^,  ags.  ä-timplian  ,mit  Nägeln  ver- sehen^; andrerseits  norw.  mdartl.  tuppa,  nhd.  zupfen,  anord.  toppr  ,Haar- schopf,  Gipfel'^,  ags.  topp  m.  ,Spitze,  Zipfel',  toppa  m.  ,Faden^,  ahd. zopf  ,Zopf,  Haarflechte,  Ende  eines  Dings^;  mnd.  tuhhe,  tobbe  ,Zapfen^, tobben  ,zupfen,  reißen'^,  süddt.  zöfeln  ,zögern^  (wie  zapf  ein)]  vielleicht  hierher auch  ahd.  zumpo  ,penis^,  mhd.  zumpf{e),  nhd.  Zumpt,  worüber  unter  dumb-.
Hierher  toch.  A  täp  ,aß'^.  Van  Windekens  Lexique  187.
t-Erweiterung  dd-t-  (vgl.  aber  das  Partiz.  dQ-to-s):
gr.  darsof-iac  ,teile,  zerreiße,  verzehre'  (Fut.  ddaoead-ai,  Aor.  hom.  daa- naad-aL,  att.  ddcaad-aC),  wozu  Safffiög  ,Teilung',  ddaf.ia  , Anteil',  öarr.Qiog »zerteilend'  (dies  sicher  von  *dä-TrjQ  :  ai.  dä-tdr-  ,Schnitter'),  ädaatog  ,un- geteilt';  dareoixai  ist  griech.  Neubildung  (Schwjzer  Gr.  Gr.  I  676)  und nicht  idg.  *6?a-^;
got  ungatass  ,ungeregelt'  (ygl.ä-daazog),  mndl.  getes  ,sich fügend,  passend'; •ahd.  Zeiten  .(verteilend)  streuen,  ausbreiten',  nhd.  verzette(l)n,  wohl  auch
12
178
anord.    teäja    ,Mist  ausbreiten',    tad:  n.  ,(*ausgebreiteter)   Mist';   ahd.  zot^^ zata  f.  , Zotte,  zusammen  herabhängende  Haare,  Fäden  oder  Wolle'  (davoi^"-* zaturra  ,scortum'),  ags.  toßttec  (expressives  tt)  , Fetzen,  Lumpen',  an.  tqtuti:0A ,Fetzen';  altdän.  tothae,  älter  dän.  und  dän.  mdartl.  tede,  taade  »verzögern '^^| hindern'.
Daneben  mit  w-Vok.   anord.  toddi  , kleines   Stück*,   hoU.  todde  »Fetzen^^ ahd.  zota,  zotta  , Haarbüschel',  nhd.  Zotte,  Zote]  mhd.  zoten  ,langsam  geheu*^^ nhd.  zotteln,  ostfries.  todden  , ziehen,  schleppen'  u.  dgl.;  über  nhd.  zaudei^ s.  Kluge  1^  704.
toch.  A  tät-k  jteilen,  zerschneiden'.
s-Erweiterung  d-es-i
ai.  ddsyati  , leidet  Mangel,   verschmachtet',  upaddsyati  ,ge
```


## [2026-09-05T15:07:27.401Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"dabh\\|dābh\\|dabhn\" IEC.txt | head -30",
 "description": "Grep Mann IEC for dabh"
}
```


### [2026-09-05T15:07:27.449Z] TOOL RESULT

```
2018:dabh- ‘harm, hurt, damage’. Cf. WP I, 764 & I, 850. See next and dabhn- Skt. dábhah ‘deceptive’; Av. daivis ‘deceit’; LW in Arm. dav, o-st. id; Per. dav “stroke; bet’; Icel. töf, pl. tafir (obstacle: Av. daivis) beside ON tefja ‘hinder’; G (Alem.) cf. Zep- pel ‘quarrel’
2019:dàbh- (long-grade variant of dabh-, q. v.) Skt. dabhah ‘harmful’ beside á-dabhyah (neg. adj. trustworthy"); Per. dav (*a or *à ‘stroke, bet); Oss. davin “carry off, steal; Du. toeven ‘stop, dally, wait’; Sw. tóva ‘hinder’; Li. dobiù, dóbti ‘hit’; Iran. LW in Arm. dav (o-st. “trick?)
2020:dabhn- (theme of dabh-, q.v.) Skt. dabhnómi "hurt: Lat. damnum, damna- re; ON tafn ‘victim, prey
2238:dü-dum and jügis); ON (?) tjóa ‘avail’. (Oss. davín, davün, v. “carry off seems to be in- dependent. Cf. dabh-?)
2247:penos Arm. tawn, Let *feast-day'; Gk. dapáne *out- lay’; Lat. cf. dapino, are “provide food" (= Gk. dapanáo 'spend') (For Lat. damnum, see dabhn-)
2635:dui-bhàn- in Gk. dipháninos lákhnos; Arm. erkban ‘amphibious, ambiguous’; *-bhàt- in Skt. dvibhatam; Arm. erkbajK ‘doubt, sus- pense; Gk. diphásios, díphatos, diphasía; *-bher- in Gk. díphoros, díphros; Ir. dabhar ‘pitcher’; OHG zwibar, zubar 'two-handled pot; LW in Cz. Cber, Ukr. ceber mus": *-dent-, -dont-, -dnt- in Skt. dvidantah, dvidat; OLat. dvidéns; Lat. bidéns; Li. dvidafitis; *-duid- in Arm. kr-kut (i-st. “twig'); cf. Lat. divido, Ere (Arm. variant zurk 'deprived', represents a variant *di-duid-, isophonic w. Lat.); *-duin-
2692:dhabros (2) ‘puny, trivial’. (In Indo-Iranian this form has become confused with type dabh-, q.v. as in Skt. dabhráh “little, trivial: Av. davro, id., though, formally, metathesis is possible). Cf. dhabh-. E dapper ‘small’; ON dapr, acc.sg. dapran ‘faint, weak, glum’ be- side daprast ‘grow faint’; Icel. depra ‘weak sight’; LG cf. bedeppert ‘flummoxed’ beside SG deppen ‘humiliate, make a fool of; Depp *fool'; Li. cf. dabüs ‘timid’. (A possible cognate of type dheb- occurs in Hitt. tepus *small). Cf. also OE dafte ‘meek, mild”
2701:nature’; Finn. LW tapa, id.; Li. cf. dabnùs, dabinti “elegant; to adorn’ dhābh- ‘limp, flaccid’. Cf. dhabros D Skt. (ambig.) -dābhyah (‘frivolous’, in a- ° *serious); Alb. i dobë, í dobët ‘weak’; Sw. dof (‘sultry, blunt, stupid". Infl. of LG? & NG döf ‘stupid’. See dhoubh-); Go. cf. af- dobnan ‘grow dumb’ dhabhló, dhabhró, ið (?) ‘surge’. Cf. dabh- Skt. dabhráh (ocean; EMDu. daveren ‘tremble’; ON dafla ‘dabble, splash? dhadhló, dhadhró, ið (?) ‘waver, tremble’. Cf. dhedher- MHG tatern ‘chatter’; G tattern ‘shake, dod- der, twaddle’; Icel. daðra ‘flirt; Sw. darra ‘tremble’; cf. E dial. daddle ‘stagger, dawdle’. (A form *dhadh- seems to be present in EME to dade ‘to toddle’ and Li. dadu, eti “cackle') dhagh- ‘beautiful, fine, abundant, good, harmonious’ Gaul. dago-; OBr. da; W da ‘good’; MHG tagen, tegen ‘confer, arbitrate’; Du. dagen ‘summon’; G cf. Reichs-tag; Du. Rijks-dag; EME days-man ‘arbitrator’; EMDu. cf. dege- lijk ‘honest’; LG cf. d&g, m & f ‘good man- ners’; Li. dažyti ‘to eeh daZalas “orna- ei: ; dažnas ‘many 3... * Latv daZs, id. dhaloros, is ‘verdant, lush". WP I, 825. Cf. dhalió Arm. dalar (i-st. *green"); Gk. thalerós, id. dhalgho “hold, squeeze'
13586:pró-sed-, cf. pro-, séd- Skt. pra-sadabh, m. “high seat; palace’; -sadi- kah, adj. ‘friendly’; Gk. (hapax) pro-edikós, adj. “landed, ground-; OCS pro-sédati, v. ‘penetrate’
```


## [2026-09-05T15:07:28.064Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 78 79 80 81; do echo \"=== leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | head -60; done",
 "description": "Print IEC leaves near p.129"
}
```


### [2026-09-05T15:07:29.815Z] TOOL RESULT

```
=== leaf 78
beside birüs ‘apt to fall.
bhrio (2) see bhráið & bhur- (2)
bhrio (3) ‘raise’. Variant of bhrgh- (?) OW (ambig.) cf. bry (above'. See bhrghus);
` OHG burian ‘raise’ beside bor “height, upper
room’; MHG bor ‘up’; OE bor-lice “very”
bhrios (bhro(n)) (1) ‘bearer, holder’. See bheró, bhor- Skt. cf. bhrpámi ‘bear’; OHG OS -boro; OE bora, -bora; ON cf. ó-byr-ja ‘sterile woman’; Gk. pharía 'vessel
bhrios (2) ‘son, young man. (Semantically related to (1)) Kurd. cf. bire “a stalwart’; Per. barnà, burnā ‘young man’; OE bora ‘son’ and byre, id.; Alb. bir, pl. bij, id.; Go. baür, cons. st. id., cpds. -born; ON burr, pl. rir, id.
bhrios, bhrà (3) “bore, hole’. Cf. bhraio Alb. birë “hole; OHG bora 'gimlet; OE, MLG bor, id.
bhrkos, à, o(n) (1) ‘spike, splinter ` Lat. (ambig.) furca 'fork, prop, gibbet" beside forco *ploughpoint'; Ir. cf. (either) briogún ‘skewer (or) bráca ‘harrow’, brácaim, v. “har- row’ (*-T-); Srb. Slovene bøk ‘moustache’; Cz. brk ‘quill’; Pol. barki, pl. ‘shoulders’; Lusat. cf. bórkać (‘root up ground": Ir. brá- caim); Li. birka ‘tally-stick’; Latv. birka ‘chip, point
bhrkos, om, à (2) (?) "boat Gallo-Lat. barca; Br. bark ‘boat’; Slovak brko. ‘keel
(bhrm- ‘bore, hole’. Cf. bhrios (3). Alb. brimë ‘hole’)
bhrnio ‘tingle, burn” Gk. cf. os-phrainomai ‘smell, sniff? (initial to osmé. EB otherwise); OFris. burna; Fris. baerna; OE byrnan beside biernan (vocalism obscure); OCz. Cz. brnéti ‘tingle’
bhro (bhur-), see bhràio
bhrs- “break; fragment. Cf. bhris-, bhrus-, bhrst- Hitt. pars-mi, -imi, -ihi “break, divide’; cf.
115
parsür “crumbs'; Gk. phársos, n. (1) “frag- ment’; OCS (ambig.) brúseli (“potsherd”, but for OCS brúsno, -noti ‘destroy’, cf. bhris-. Ir. brisim ‘break’ seems to represent a form bhrst-, q.v., while OE brysan represents a form containing -ü-, cf. bhrus- (2)
bhrsos, ios, à, is ‘shag, tuft, bristles, fur. Cf. bhrstis Av. cf. boro$o ‘backbone’; Arm. bars (i-st. ‘horsehair, mane"); Gk. phársos (2) ‘cluster’; Phryg.? (LW in Gk.?) bürsa ‘rawhide, skin bag’; Lat. (LW or Gallo-Lat?) burra ‘shaggy garment’; re-burrus, adj. ‘bristly’, cf. also LLat. borr-àágo (“borage”, lit. *bristly plant"); variant (*bhors-) in Olr. barr *tree-foliage, spray’; Cor. bar (1) “bunch, tufted branch? beside Oir. barrán “head of hair; ME burre ‘burr’; Norw. Sw. borre, id. (Sw. also 'thistle- head, sea-urchin’); Cf. OCS brí$-ljanü *spindle- Dee beside Cz. brs-len, id.; cf. also Cz. brs- ina ‘grassy slope’. See bhors-
bhrstis, os (bhurst-, bhrust-) ‘spike, shoot, twig, bristle’. WP II, 131 Sk. bhrstíb; Oss. barc ‘mane’; Hitt. parsdus ‘sprout; Lat. (ambig. füstis ((stick', fr. *bhurst-? cf. bhrustos (2)); Ir. bruis *brush- wood", ambig. cf. bhrust-); Br. cf. bréSen ‘twig; OHG burst, OE byrst; ON burst ‘bristle’; Sw. borst, id.; cf. Mod. Icel. byrstur, adj. ‘harsh’; Blg. brüst ‘green twigs’; Cz. bršť, Pol. barszcz 'hogweed' Srb. bfst *shoot'. (The Slav. forms are ambig. cf. bhrust-)
bhrstið ‘break out, shoot, burst. Cf. WP IL, 206 and bhrstis above W brysio ‘hasten’, brys ‘haste’; Br. brésia ‘scamper’; OS brustian ‘break out; Slovene brstiti ‘sprout’; Icel. cf. byrstur, adj. ‘harsh, gruff; OE cf. byrst ‘loss’
bhrt- (bhrt-) (1) ‘strike, blow; striker; fate’. Cf. bherio & bhrio (1) Oss. bårdin ‘cudgel; Arm. bah ‘spade’; Per. bil, id.; Lat. fors; Ir. bráth ‘judgment; W brawd, id.; Br. breed ‘ple; MHG burt ‘pledge, duty’
=== leaf 79
; OE byrd ‘fate’; Du. beurt ‘turn, lot; OFrankish, cf. staim-bort (a weapon: *stone-throwing catapult’)
bhrt- (2) ‘bearing, load, product. WP II, 153. Cf. bhero, bhoros
bhrsos, ios, à, is — bhübh-
15
20
25
30
35
40
45
116
Sk. bhrtíh; Av. borotis; Olr. brith; Go. ga- baürps, baürpei; MHG burt; bürde; OE byrd; ON byrð, f. beside byrór “birth; load"
bhrt- (3) “boring, bore, hole, hollow’. Cf. bhraio ON byrða “bin, trough”; Pol. barc, Cz. brt, R bort ‘hollow in tree, hive of wild bees’
bhrtós, á “borne, carried'. Cf. bherð Sk. bhrtáh; Av. boroto; Per. bilà ‘alms’; ON burór (*bearing?, etc.)
bhrug- (bhorug-, bhor-) ‘neck, windpipe’. Cf. bhrug- Oss. bárzài ‘neck’; Gk. phárux (& phárugx); ON barki
(bhru-, see bheru-. Z-gde radical in Per. balwà ‘tumult; OE brymm, m. ‘surf, sea”, prob. also in MHG brunne ‘spring’; ON brunnr, id.)
bhruos, à “arch, span, beam, bridge’. (prob. variant of bhruu- q. v.) Gaul. brivo-, brio-, briva (‘bridge’, in place- names); ON brú; Sw. bro, id.; Blg. brúvi, Srb. brv “sleeper; footbridge’; OCz. břev, pl. břvi, f. ‘beam, rafter’; cf. OCS brüvno ‘beam’; Cz. břevno, Ukr. berveno; Slovene bruno
bhū- (bhüu-) (1) theme of verb ‘to be’. Cf. bhüio & bhui-. WP II, 141 Skt. á-bhut, pf., bhütáh, pp.; Av. büta, npl.; Per. budan, inf; Gk. phüs, m. ‘son’ beside Hes. pháos ‘plant’; phué ‘growth’, éphün, aor., etc: Ir. budh (was, 3sg);; W OBr. bu, wd: Lat. Dm. id. beside OLat. fuam ‘may be’ and OBr. bi “will be’; OS bū, OE bü ‘dwelling’; Norw. bu ‘booth’; ON búi ‘dweller’; bua “dwell, be’; beside byggva ((populate', fr. *bhuu-); OHG bü, gs buwes ‘farming’; OCS byxü, etc. ‘was’; Li. būvis, 10, m. ‘creature’ beside buvau “I was’; Latv. büveju ‘I build”
bhū- (2) ‘howl, gale, blast. Cf. bhübh- Arm. bu (o-st. 'owl) beside buk, pl. form “gale, storm’; Per. cf. bü timàr ‘heron’; Phryg. or Mac. büza ‘owl’; Du. bui ‘squall’; cf. Lat. butio and MIr. bufa (‘bittern’, fr. *bhuuo-). Sw. rágn-by (LW < Du.)
bhübh- “a hooting animal’. WP II, 112 Arm. bbun (/noise', fr. *bhübhon); Lat. bübon (owl, w. assimilated consonants) beside bū- bulo, are (onomat. *büb-); MIr. cf. búbaire,
117
m. ‘bittern’; Li. bübe ‘heifer’ beside bübauti ‘bellow’
bhubbh- (expressive variant of above) ‘mut- ter, burble’ OE à-byffan; Latv. bubinaju, id. See next
WP II, 114. See bubul- Lat. bullio (assimilated consonants); MLG bubbeln; Du. bobbelen; OCS bübljo, čti & -ati; Alb. bubullon (3sg *thunder); Cz. be- blati, Pol. bebłać ‘stammer; slobber’
bhubhlos, see bhubhulos
bhubhos, à (bhubbh-) (1) ‘creature, monster’ Hitt. pupus (queried) ‘paramour, concubine’ Alb. bubë ‘grub’; LW in Srb. buba, Blg. bùba, id. and ‘bogey’; Lat. bufo 'toad' is ambig. cf. bhudh-; Ir. bob ‘trick’; MIr. boban ‘calf; Gael. ‘boy’; OFris. bobba, wm. “child”; E dial. bob *flea-beetle'; Sw. bubba ‘cockroach’; Slo- vene beba ‘dolt’; (Gmc. forms with -b-, -bb- are fr. bhubbh-); Li. bübis, io, Latv. bubis ‘spook’
bhubhos, à (bhubbh-) (2) “lump, swelling; crest’ Arm. cf. bbuk (dim. type, a-st. ‘crest, comb’); Rum. (substr.) bubă ‘tumour’; Ir. cf. bubán ‘coxcomb’; Du. bof (3) ‘mumps’ beside bobbekop (‘big-headďd’, fr. *bhubbh-); E bob (fr. *bhubbh-) beside dial. bub ‘breast’; Li. bubas *ball, pellet, egg, apple', etc.
bhubhos, ó(n) (3) ‘noise’. Cf. bub-, bubul-, etc. Arm. bbun ‘noise’; Du. bof (1) ‘thud’; cf. Li. baübti ‘bellow’ beside bübauti, id. (*-ou-/ -ü-) beside (*-u-) bubu, eti, id.
bhubhulos, à, is (bhubhlos
=== leaf 80
, à, is) "ball, round creature, bubble’. Cf. bubul- and bhubhos (2) Arm. bubul ənkujz ‘walnut’; Lat. bulla (dial. or expressive: “boss, knob, stud, seal, bubble’. Assim. as in barba is also possible); MHG (Alemannic type) popeln ‘bubble’; G bub- beln, id.; LG Bobbel, bobbeln, s & v id.; Fris. Du. bobbel “lump, pimple, bubble'; Sw. bubbla v. ‘bubble’; Cz. dim. bebelka ‘louse’; Li. bubulis, io “ball, pellet; Latv. bubulis "knot in yarn’
bhud- ‘stumpy, blunt; stump, chunk? Arm. cf. but ((blunt, fr *bhudtó- or
bhubbh- — bhudhmn- (bhudno-)
10
15
20
25
30
35
40
45
118
*bhudstó-); Ir. (ambig.) bod "boor": MHG butze ‘bit’; LG butt ‘clod’; adj. ‘blunt’; Du. ` bot n. ‘tip, bone’; f. ‘bud’; adj. ‘blunt’; Du. & Fris. bot (also: silly”); OE cf. buttuc “stub, butt, corner of land’ beside bytt ‘corner of land'; G Boss “peg on ploughbeam', cf. bos- sig ‘wild, defiant; ON butr “butt, stump’: Li. bude "lichwake mushroom’. (Verbal ex- tensions in MHG butzen *jolt'; OFris. botta, id.; LG botten “beat flax’; Du. botsen ‘crash’, fr. *bhudsKo) | : bhüdo(n) ‘burst, sprout, projection’ Ir. búdán ‘frontal bone of horned animal; stump’; MHG büse ‘sprout; outburst be-
. side būzen ‘swell, sprout'; E bout; Fris. bût
‘pal’; Du. (?) buit (booty. The semantic link obscure)
(bhüdü, cf. abhu)
(bhudtós, see bhud- Arm. but ‘blunt: Norw. buttet *dumpy?)
bhudh-, theme of emphatic vb. “to be? Osc. cf. fufens ‘they were; W byddent, id.
bhüdhlos, à, om, ön “existence, being, crea- ture'. Cf. WP II, 141 OE bold ‘dwelling’; Cz. bydlo, id.; Li. büklà,. büklé, id. (Lat. fulló ‘earwig, beetle may represent a variant *bhudlo- cf. OE botl, n. ‘dwelling’; Eng. bottle ‘fly’. Cf. bIue-bottle)
bhudhmn- (bhudno-) “base, bottom, stock, stump, root, stone'. WP II, 190 Skt. budhnáh, -ám; Av. buno; Per. bun; Oss. bín, bun, beside bíndur, cpd. (bín + dür “boundary stone; farm); LW in Arm. bun (i-st. ‘trunk, root, origin); Gk. puthmén; cf. Gk. (Anatolian? Phryg.?) púndax "bottom", cf. bhrgh- for a ref. to pürgos; Alb. bun “mark, goal; spring-head, mountain hut? be- side buzém *yule-log', fr. *bhudhimn-); Lat. fundus; MIr. Ir. bun "base, root, foot? beside bond, bonn “sole of foot; Mir also bunne ‘spring, source’; Gallo-Lat. bodina *bound- ary; Br. men bonn (‘boundary stone’. LW in OFr. bonde, E bound); W bon 'stem, base, stock; OBr. cf. bon-ed ‘race, nobility: W bonedd, id.; Ligur. cf. Bodin-cus (river-name of Po, said to mean *bottomless"); variants in OHG bodam; Du. bodem as against OE botm; ON botn; Cz. cf. bedna “chest, box’;
119
R cf. bodnarí ‘cooper: LL budinarius (fr. Gall)
bhudhó, ið “wake, watch, care, notice’. WP II, 147. Cf. bheudh-, bhudhros Skt. búdhye, intr.; cf. budháh (^wise'. LW in Arm. but “watchful'); Av. fra-būiðye; OE bodian; OFris. bodia; MHG boten; ON boóa; OCS büzdo, büdéti ‘keep watch, be awake” (and com. SI.); Li. budüà, and budiù, budeti, id. Nasal-infix in Gk. punthánomai (lit. "am roused': “hear of")
bhudho(n) (1) in OHG boto ‘messenger’; cf. ON boði, id. & OE bod ‘message’. See bhudho above
bhudho(n) (2) “creature” Gk. puthón; (Rustic) Lat. bufo (*toad', assi- milated conss. as in barba, bulla) beside LLat. bufus, bufa a poisonous insect; Lat. cf. also fullo ((2) ‘earwig’, fr. *bhudlon, cf. E bottle 'fly); Ir. bod ((boor, cpds. *'bird") (the expected form *bodán does not occur); SWG Butten 'polecat; LG budde “earth- worm, louse’; OE budda ‘beetle’; EME boude *corn-worm'; ONorw. budda ‘young animal’
bhudhros “awake, alert’. Cf. bhudho, io. WP II, 148 Skt. cf. budbah ‘wise’; Av. (zaeni) budro ‘alert’; (Iran. LW in Tk.
=== leaf 81
 bidar, id.?); OCS büdrü, id. (and comm. S1.); Li. budrüs, id.
bhugo, ið (1) “bend, turn, flee’. WP II, 144. Cf. bhugho, bheugó Skt. bhujami, pp. bhugnábh; Lat. fugio, ire; Gk. cf. éphugon, aor. ‘I fled, feared”; inf.: phugein; Ir. boghaim “bend, arch'. Ambig. cf. bhugho; MHG bochen ‘defy’ beside bocken ‘be bowed, sink’; OFris. buckia ‘bend, bow’; G (sich) bücken; Norw. bukka; Sw. bocka, id.; Li. cf. bügstu, bügti (“be frightened'. Ambig. cf. bhugho)
bhugo, ið (2) ‘beat Gk. cf. s-phuzo ‘pulsate’, s-phugmós ‘pulse’; MHG bochen ‘knock’ beside buch ‘cudgel’; (Alemannic) G pochen: Dan. poge ‘knock’
bhugos, à ‘bend, turn, flight’. Cf. bhugo & bhugho. WP II, 144 Skt. bhujah w. secondary -j-: ‘curve, branch, arm’; Gk. fugé, füza, f. ‘flight’; Lat. fuga, id.; G buck (2) ‘timid’; Li. cf. bügus (‘dan-
bhudhó, ið — bhukió
20
25
30
35
40
45
120
gerous, frightful’. Ambig. cf. bhugho)
bhugho, io ‘turn, bend, fold”. Cf. bhugo Gk. (synth. cpd.) ptüsso “fold? beside ptüx, gs ptukhós, also ptukhé, f; Ir. (ambig.) boghaim ‘bend, arch’; ON buga ‘bow, beng’; Go. (Crimean) boga, OHG and OE boga ‘bow’; cf. Norw. bugne ‘bend’? & G Bucht ‘bay’; E bight beside EME bought ‘arch’. Doubtfully to Go. bugjan ‘buy, and ON byggja ‘hire out, pledge’. Cf. OE bygu & byga ‘curve, bend, angle’: ON bugr, id.
bhught-, bhughtiom, io “bend, turn, exchange barter’. Cf. bhugho Per. (?) büyée ‘wrapper; Myc. cf. puktalia (queried: ‘a garment); G Bucht ‘bay’; E bight, id. beside EME bought ‘arch’; ON býti; Norw. bytte ‘barter, exchange, deal beside bukt, bukte “bend”, w. phonology of LG
bhu$- (bhug-) “pleasure; eating, food” Skt. bhuj ‘pleasure’; adj ‘eating’; Arm. bujc, Let ‘food’; Lat. cf. Fugia ‘goddess of joy; G Duck (1) “fat, stodgy’. Cf. (*-ü-) Oss. büz, Dig. boz ‘thankful; thanks’
bhuĝos, ios, o(n) ‘small animal’. WP II, 189 Av. büzo ‘buck’; Per. buz ‘goat; Oss. bodz, Dig. bodzo, id.; Arm. buc, a-st. lamb; MHG boc, gs bockes ‘he-goat’; ON bokkr, bukkr, id. Finn. LW pukki, id.
bhugh- ‘bogey, insect. Cf. WP II, 117 W bw ‘bogey; ME bugge ‘scarecrow’; cf. E bug “insect? and bugbear (cpd.); Li. bu£Zys, io ‘bogey; insect?
bhüio, bhuiio “being, essence’. See next Gk. phué; OCS bije ‘substance’
bhŭið, bhuiið “bring into being; become, be’. WP II, 141. Skt. bhūyé, Av. buye :Gk. phúð, phuío; Alb. bij ‘sprout, grow’; mbij, id. (fr. *en-bhuiio); beside buj “quarter; lodge’; Lat. fio, fieri; (Osc. Diet 3pl.), cf. (probably) im-buo ‘impregnate’; Ir. bia, biad (impers. ‘will be’), W byddaf, 3s bydd; OBr. bi ‘will be’; OE būan, büian ‘dwell’; ON búa beside byggva ‘dwell; populate’; Latv. biju ‘I was? beside da-būju (‘reach’: ON búa, id.); OCS cf. bije ‘substance’ beside by (3s. ‘was’). (For Lat. -bundus (mira-, vaga-, mori-) cf. im-buð (lit.? ‘cause to be’)). See bhū-
bhukið ‘roar, hum, bellow’. Cf. bhükos &
121
WP II, 112 Arm. b
```


## [2026-09-05T15:07:44.493Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:2017])\nleaf=t[:idx].count('\\f')\nprint('leaf(0-based)',leaf,'->awk NR',leaf+1)\npage=t.split('\\f')[leaf]\nimport re\nprint([m for m in re.findall(r'\\n(\\d{2,4})\\n', page)][:10])\nprint(page[:200])\nprint('...TAIL...')\nprint(page[-300:])\nEOF",
 "description": "Find IEC leaf/page for dabh-"
}
```


## [2026-09-05T15:07:45.629Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"daivi\\|dab-\\|dabaiti\\|dbaēš\\|daibiti\" BRT.txt | head -25",
 "description": "Grep Bartholomae for Avestan dab-"
}
```


### [2026-09-05T15:07:46.102Z] TOOL RESULT

```
leaf(0-based) 85 ->awk NR 86
['129', '10', '30', '40', '130']
word' in Rom- ance and Gmc.)
bhutlo-, see bhutolo-
bhutos, à, om “being, existence, life, growth, dwelling, place'. Cf. bhü- and next Arm. but (o-st. (food); Myc. Gk. phutón *plant, race', etc. beside
...TAIL...
MHG biunde, biunte; G Beunde ‘plot, estate’ from a type *bhuiiont-; see also bhuio, bhüu-
bhzd- (a notional root of onomatopoeic content, cf. bzd-, burzd-) Osset. cf. bíz-bíz künín “fart; Arm. bzzam, bzzem “hun” beside bzez, gs bzezi 'cock- chafer'; E buzz
Arm. tacem *embrocate' beside tac (i-st. ‘f
```


### [2026-09-05T15:07:46.142Z] TOOL RESULT

```
3230:PPM.  zum  V.  dab-.  —  Pu.r  admvakihä\\  — ■)  Geschr.  al  aoy'\  s.  No.  4.  —  '  Bei  DsT. •yjmmm;  ob  Druckfehler?—  JJ  Vgl.  aiaiiyS.-
3243:Pü.  (m  Yt.  7):  afrlfak,  erl. :  kaiän  ni  frfpim, (lu  Vr.  21)-.   adamak  (lum  V.  dab-,   vgL  aiao-
3680:•  j.,  g.  aipi,  p.  apiy  I)  Adv.  i)  'dazu auch,  desgleichen  auch',  ein  neues  Subjekt anreihend,  von  dem  die  gleiche  Aussage gilt:  at  yuS  dasva  .  .  akät  mananhs  sl<l cihr^m  . .  yasca  vä  . .  yazatte  . .  ^yaotnqm 'pl  daibitilnn  yäis  ..  "..  desgleichen  auch die   (eure)  Taten,    durch   die  . ."  Y.32.
12671:•  j.,g.'dab-V, 'betrügen'.  Praes.2  dava-^'', lob  dibmav-'^,  iddiivia-^'"^^  24davaya-''>, 26  (Pass.)  iytf(yii-'>,  30  (Iter.)  däbaya-.  —
12676:•  g.  'dab-  V.  (etwa)  'üben'.  Praes.  2  daba-.
12678:Et.?')  —  PiL:  te  äH  iöini/rt/iSr')--aAnonöf - ätnöxlun  i  den  i  vrh  pa  siu^an  u  hmiht.  — «)  Falsch  KZ.  ja  528,  36.  140;  s.  noch  No.  2.  — )>  Also  tu  ^dab-;  die  an  Pü.  sich  anschliessen- den Oberseliungen  -  zuletzt  von  Dst.  und Mills  -  gehen  keinen  Sinn.
12829:»  j.  'davant-  Adj.  (fem.  'vainil-),  PPA.: s.  ^dab-.
18756:i)    'verschwinden,    sich    fort    machen, weichen',  a)  absolut:  ffawCaSIA.)''  daivi druxs  Siß.  3;  J^;  —    natyät  drvxs' Ytj. 17;  —  vispa  druxs  ni^äiti  Yt  2. 1 1 ;  —  , maire  näsaite  Yt.^.  8;  —  *aia'jca  *maire   ■ näiätalca  mairyS  Vl  ig.  12.  b)  Von  -
19062:Gebrauch  von  tf  nähert  sich  dem  von ma  'fif;  a)  im  gAw.;  es  folgt  Optativ; zu  i):  ff  daibitim  dus.saitis  Isd.)  aAsm mprq^yät  Y.4$.\;  —  tf  ahya  ma  ahris (sd.)  .  .  /rdsyäi  Y.  46.  S;  —  rf  na  pgurüs (sd.)  dngvatff  hyii  Hxsnuil  Y.  4:^.15;  — mit  Ellipse  von  hyai:  n'  3r>s>jyBi  frajysitil (sd.)  «•  fsuyenil  dr>gvasü  pairt  Y.  2g. 5.  zula):  anäis' zni  n' ahura  . .  yanSis taranaima  (sd.)  Y.28.1).  b)  irnjAw.; zu  I);  es  folgt  Optativ:  n'  ihra  airyi daiAhavS  frqs{^d)  hyät  halna  «'S..  Yt 5.56;  —  »•  Ais  barSit  upa  kahm  N.26';
```


## [2026-09-05T15:07:57.278Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Betrug\\b\\|'Betrug'\\|,Betrug\" BRT.txt | head -20; echo \"=== daiv\"; grep -on \"daivi[a-zš]*\" BRT.txt | head -20",
 "description": "Grep Bartholomae for Betrug and daivi"
}
```


### [2026-09-05T15:07:57.342Z] TOOL RESULT

```
12830:•  j.  davay-  m.  'Betrug'.
24063:•  j.  vi-davay-  Adj.  (auch  mask.)  Tiei von  — ,  sicher  vor  Betrug':  *aöavli'  ttqma ahmt  *'Mj  (NSra.)  nqma  ahmt  Yt /.  14.
=== daiv
18756:daivi
```


## [2026-09-05T15:07:59.010Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD das\"; grep -n \"dās\\|das \\[\" PHD.txt | head -20; echo; echo \"=== PHD_mackenzie\"; grep -n \"^dās\\|dās \" PHD_mackenzie.txt | head -20",
 "description": "Grep MacKenzie for dās"
}
```


### [2026-09-05T15:07:59.071Z] TOOL RESULT

```
=== PHD das
310:das [d’s | N ~] sickle. dàs?r [d’sl = Av. dātra-) gift, reward. dast [Y DE < A yd-h; dst! | = M, N ~] hand. dastag [dstk! | N —a] bunch, bundle, group. dast(a)gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate. dast- gir [dst OH DWN, (v. griftan) | N ~] 1. helper; 2. captive. dast-graw [dstglwb!] captivity. dast-kàrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. dašn [dšn! | = M] right hand. dāšn [d”$n' | M d’s(y)n] gift. dašnaģ [dsnk' | N ~a] 1. right hand; 2. dagger. dašt [dst! | = M, N —] plain, open ground. daštān [dft?n! | N ~] menstruation; menstruous. „estān [-st?n'] secluded place for menstruous women. -—--màh [-m?h] menstrual cycle. -ūmand [-’wmnd] menstruous. dāštan, dar- [YHSNN-tn! < А V ben: d^ftn', Pl- | M d'An, ar-, N ~] have, hold, keep, preserve. pad . . . dāštan: hold by, to; take for. pad éd dāštan [cf. N pindāštan] consider. --išn: preservation, maintenance. dāštār [4° #1 keeper, preserver. daw-, v. dawidan, dawistan. idawāl [dwb’l | N ~] leather, skin. ždawāl [dwbl | N ~] deceit, trickery. idawīdan, daw- [LH TWN-tn! < A Vrht; dwytn', dwb- | M dw-, N ~] run. *dawidan, daw- [dw-ytn'] speak (daevic). 1, 2 dawistan [LH TWN-stn!, dwstn'] = 1 * dawidan. daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction). „estān [-si?n!] cemetery. dax$ag [dhšk! | M dxsg] mark, sign, characteristic; memory. pad ~ dàštan : remember. az — hištan: forget. ~6mand [-’wmnd] marked. Day [ddw' | M dyy, N ~] Creator; cal. roth month; 8th, 15th, 23rd days. dayag [d^yk! | M d?yg-, N ~aj (wet-)nurse. „ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning.
3437:reward mizd, pādāšn, dās*r.
5577:Чадан! däs, "*gāh gāhwārag dār-! dārišn! даап! dāsār yāsaman gahbedīh gahbed dahigān Gayomart dahibed dāyagānīh dāyag

=== PHD_mackenzie
```


## [2026-09-05T15:08:13.803Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,60p tools/ref_page.py",
 "description": "Inspect ref_page.py"
}
```


### [2026-09-05T15:08:13.845Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-05T15:08:15.362Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pdf page\" BQT_v2_pages.txt | head -5; echo ...; grep -c \"\" BQT_v2_pages.txt; echo \"=== v1\"; grep -n \"pdf page\" BQT_v1_pages.txt | head -3",
 "description": "Check BQT page files structure"
}
```


### [2026-09-05T15:08:15.431Z] TOOL RESULT

```
...
41071
=== v1
```


## [2026-09-05T15:08:19.304Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/ 2>/dev/null; echo ---; ls data/verification/sources/refs/ocr/BQT 2>/dev/null | head -40",
 "description": "List OCR cache"
}
```


### [2026-09-05T15:08:19.359Z] TOOL RESULT

```
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
---
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1455.png
1455.txt
1488.png
1488.txt
1803.png
1803.txt
180.png
180.vision.txt
181.png
181.vision.txt
1878.png
1878.txt
1900.png
1900.txt
1908.png
1908.txt
```


## [2026-09-05T17:21:33.008Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in BQT_v1_pages.txt BQT_v2_pages.txt; do echo \"###### $f\"; echo \"--- بیدستر\"; grep -n \"بیدستر\\|بيدستر\" $f | head -5; echo \"--- دهره\"; grep -n \"دهره\" $f | head -5; echo \"--- داس\"; grep -n \" داس \" $f | head -5; done",
 "description": "Grep BQT text for headwords"
}
```


### [2026-09-05T17:21:35.422Z] TOOL RESULT

```
###### BQT_v1_pages.txt
--- بیدستر
--- دهره
19471:بزمین رسب وضم اول و سکون انی دهره ۴ را
26964:* بر وزن دهره , ینعی پای
--- داس
###### BQT_v2_pages.txt
--- بیدستر
11937:  ‫تش‌هم‌باشد » وی‬       ‫سوزنده را گودند که درآنآ‬         ‫جند بیدستر باشد ‪ .‬گوبند خایة سک آبی‬
37460: ‫میباشد و بتازی‌عنب‌التعلب کوبند ‪ -‬ودرفرهنگه‬                       ‫مجگان است که جند بیدستر باشد‪.‬‬
--- دهره
12978:‫از دهرهای حن خیز است داخل جهاز دختران‬                     ‫« با‬    ‫)‪۱‬‬       ‫است‬   ‫ووامی‬   ‫نام جا وعقامی‬   ‫‪۰‬‬   ‫ویواو رده‬
16061:‫سداب خوائشدت ودهره رانز کفتمانه وآتسلاحی‬               ‫ماندڭك فاصله وجوب ‪re‬‏ عر ص بربالای آن دو‬
16145:                              ‫رکه ‪ :‬داستار‪.‬‬   ‫‪۳۳‬‬    ‫‪۳‬‬                     ‫‪ :‬دهره ‪.‬‬     ‫رکه‬       ‫‪- ۱‬‬
--- داس
```


## [2026-09-05T17:21:38.920Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for p in 333 813 904; do echo \"########## BQT:$p\"; timeout 600 python3 tools/ref_page.py BQT:$p --image 2>&1 | tail -40; done",
 "description": "Render BQT pages 333, 813, 904",
 "timeout": 600000
}
```


### [2026-09-05T17:21:40.961Z] TOOL RESULT

```
########## BQT:333
no scan of BQT covers printed page 333 (see 'scans' in refs_online.json)
########## BQT:813
no scan of BQT covers printed page 813 (see 'scans' in refs_online.json)
########## BQT:904
no scan of BQT covers printed page 904 (see 'scans' in refs_online.json)
```


## [2026-09-05T17:21:43.483Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "Show BQT ref config"
}
```


### [2026-09-05T17:21:45.345Z] TOOL RESULT

```
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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
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
```


## [2026-09-05T17:21:52.744Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in range(548,566):\n    p=t[i]\n    hit='بيدستر' in p or 'بیدستر' in p\n    print(i, 'HIT' if hit else '', repr(p[:90]))\nEOF",
 "description": "Scan BQT v1 leaves for bidastar"
}
```


### [2026-09-05T17:21:54.250Z] TOOL RESULT

```
777
548  'غشب را فرو نشاند ۰ و او موکل است ب رگلوان\nو گومقندان , اکثر چهار پابان ؛ و تدییر امور\nو مص'
549  '۳۷۹ -\nپمنحه 2 با جیم ونون بروزن\u200cدد\nو عجمان در ين روز عید کنند و جشن سازند »\nبا بر قاعدث کل'
550  'یم - بر وزن فهیم : تلم یکی آزرابان\nو بزرگان هند ات۳٩\u200f\nگزنشد \u200f\nلین ۰ بکس ۳ وزن نگین »\n۱۳\nی '
551  'بجوم\nآب با بخون ۱ .\nباآب یا بخون ۱ .\nنی خساند و ق م کرد - و آحیخت و سرشت\nآب و با پفون و چر'
552  'که پس رکیوین کودرز باشد .\nیحو هر - کنابه از مردم بی هنرویی\nعفل و هیچمکاره باشد .\nکنابه ازگ'
553  'ابثان کتاب آسمانی است ت - و ممعنی حوش وشمور\nهم بنظرآعده است و در مویدالّلاء موش\u200cلوشته\nبودن'
554  'بید کیا\nبید گیا - بکر کاف فارسی و نحتانی\nبالف کشیده . نوعی از حرشف است که کنگی\nباشد. سرد د'
555  '- ۳۳ 7\nیر دک بنتم رابع بر وزن نك بی »\nبمعئی برژه انته ات صمفی\u200cباشف منتو, که\u200cبارزد\nگوشش ٩\u200f '
556  'بیرونآحدن\nبیرون آ هلان - سسروف است که\nنفیض درون رفتن باشد- و کنابه از ترك اطاعت\nوانقیاد هم'
557  'پیمما --\nلیستون ۱- نام کوهی است\nمشپور که فرهاد بفرمودة شیرین آنرا\nمبکند و کنابه ازآسمان هم'
558  'از "1 رن اه\nلیشه » بر وزن ربشه جنگل و نستانرا\nگونند و بعربی اجم خوانند؟ - وسازی هم\u200cهنت\nاز '
559  '۳۹۳6 سد\nبیقاد ه بنتح اولبروزن نیزار , سرزنش\nوطعنه باشد.\nبیغاره بر وزن گهواره » بمعنی بیفار'
560  'بنم ثانث مر وزث میگفت اه\nستارژ زهره را گوبند .\nبیلقان \u200f بنتح اول و و\nبر وزن نهروان ۰ شپرست'
561  '۳:۱\nماه است که بعربی شه ر گوبندا .\nکه مردمرا در حالت ماشفه دیده میشوده وآنرا\nمربی ممایثه ک'
562  'نبویرد\nشده است واوباریدتن بفتح همزه بمعنی\nفرو بردن و بلم کردن باشدا . ۱\nایو بر ك ع بکس اول'
563  '۳۳\nخوانند .\nلیو ث » بر وزن ربوند » بمعنی غدر:\nاست که بیوفابی کردن باشد .\nی ۵ » بروزن هیوه»'
564  'گفتار 3\nاز کاب برهان قاطم درحرف بای فارسی با حروف نبجی\nمبتتی بربیست و يك بیان و محئوی بریک'
565  'با آ هو - بالف بسدکشيده و های\nبواو رسیده » باصطلاح بنایان خانةٌ شش بهلو\nباشد وآنرا بعریی ع'
```


## [2026-09-05T17:22:02.769Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (552,553,554):\n    print('='*20,'leaf',i)\n    print(t[i])\nEOF",
 "description": "Print BQT v1 leaves 552-554"
}
```


### [2026-09-05T17:22:04.493Z] TOOL RESULT

```
==================== leaf 552
که پس رکیوین کودرز باشد .
یحو هر - کنابه از مردم بی هنرویی
عفل و هیچمکاره باشد .
کنابه ازگوشت است که بتازی لحم کوند .9
لیکستن « بکر اول بروزن دلبستن»
بمعنی درماندن و عاجز شدن باشد .
و عاجز شده - و محبوس و بندیرا گویند.
بیکشت مه بنتح اول وضم ثالث بر وزن
زردشت » هر چیز کهآ نرا از یخ بر کنده باشند
ماشد درخت و امثال‌آن » ومجای شین قطه دار
صین ی نقطه هم آمده استه وف ورست ات
چه در فارسی هر دو بهم تبدیل می‌بابند چنانکه
ور فواید گذشت .
بیخ کوهی - بر کاف بواو رسیده
شو کران باشد و آنرا بیونانی نودربون کوشده
و بپترین آنرا از تفت آورند و تفت از اعمال
بزد است .
(۱) چك : خا.
( رن
۱۳۳ ت
ی خویش ه با واو ممدوله‌پروزن
بی دیش ؛ بی خود و بی‌هوش را کوبند .
لی خی لسن با :ای فرشت » بمعنی
ی خیله » با خای نقطه دار بر وزن بی
حیله . خرفه را کونند و جربی بقلة الحمقا
خوانند .
فيك بکسر ارل و سکون ثانی ودال»
نام درختی است مشهور و آنر! بعر ی صفصافی
خوانند ۴ - و تام دیوی بوده در مازسران که
رستم او را کشت - و بمعنی «باشید» و «بوید»
ضت؟ - و کرهکی را نیز گویند که کاغذ
وجاههای شمین‌را
و تباه مازد؟ -
و بمنی ببهوده
و می فایده و نا
سودمند باشد یه
وفتی که مرادف بادباشدچت‌انکه گونند «بادویید»
بمنی بی فایده و ناسودمند - و بزبان حندی تلم
کتایی است6 مشثمل‌براحکام‌دین حندوان وباعتقاد
ص ۷۲۹ ۰ .
۴ - بایراییان کفت بیدار بد
۴ - رف : بت (یکسر اول).
زییکار دشمن عشوار ببد. فر دوسی‌طوسی.
قبه در سفحه ۳۳۳
==================== leaf 553
ابثان کتاب آسمانی است ت - و ممعنی حوش وشمور
هم بنظرآعده است و در مویدالّلاء موش‌لوشته
بودند که عربان فاره خوانند» وا اعلملا .
يفاك « ممروف است ی که طلم و سم
باشد؟ - و نام شهری است تب از تر کستان وبادشاه
آن‌شهر کافورنم جادوبی‌بوده آ دمی‌خوار. رستم‌او را
کرفت و کشت رآن شهر را عفتوح سلخت ۰
بید‌ار مقر - کنابه از هردم عافل
و هوشیار و خبر دار باشد .
ید بر که - برآوزن دبکه ب رکه, نوعی
از پیکان تبر باشد شبیه ببر که بید.
بیدخج ه بفتح اول بر وزن برزخ» اسب
جلد و نند و تیز خیز را کویند. وبکر اول هم
هت ات ۲ ۹
ید خام - بکر اكث . عود خام را
گو مد .
بید خت ؟ - با بای مجهول بر وزن
کمخت , ستار؛ زهره را گویند که صاحب فلك
(۱) چك : تا .
لید‌ستر * ع_ با ثانی مجهور و ثای
فرشت(۱) بر وزن بی مسطر ء نام حیوانی است
بحری که هم در
آد نوی نت
خوانند .
دید ست و باشدن ژتابه‌ازس اسبه
کردیدن باشد .
بیك‌ طبر ی « نوعی از بید باشد وبعضی
س مق و۱ مس طبری: کرشة ۷ و بستی
پید موله را کویند که بید مجنون باشد .
لیفق ح_بروزن احمق, ببادة شطرنج‌را
کویند وآن مهره ای باشد از حملةٌ مپره حای
شطرنج. و ععرب‌یاده است ۸ .
یدق سیم - کنابه از کو کب و سثاره
باشد .
۳ ت رد 7 فوروز نامه ۹۱۳ ۵ص۵/.
بضی اسای ی بدوح ۰ ای وی
هزدسنا ۰ و۳۲۹
۷ .2680011868 #«نأه۹:ناتی۱5:۹*.
۱ رگ : آش بجگان .
فهرست مزدسنا .
بقیه ازصفحهٌ ۳۳۲
==================== leaf 554
بید کیا
بید گیا - بکر کاف فارسی و نحتانی
بالف کشیده . نوعی از حرشف است که کنگی
باشد. سرد دخشك است در اول. جراحتهای‌نازمرا
غافع باشد .
ثيل لا - پکس اول وئالث وسکون‌نانی
مجپول و لام بالف کشیده . سخنان بی ربط
و حذبانرا گونند .
بیدمال - با میم کشیده بر وزن تيك
فال » با کردن زنگه باشدازرو ی آیینه وشمشیر
و سایر اسلحه بچوب_بید با چوب دیگر که
این کار را شایف.
دیل مشاث - نوعی ازیید است که بهار
آن عنی شکوفه‌آن بغایت خوشبوی هبباشد (۱)
و عرق را یجهت نفریح دل و تبرید
باشامند ۷ .
نید موش « بروزن فبل گوش, بععنی
بیدمشك‌باشد وآنراکرية بید هم میگوند.
لیدواد - با ثانی مجهول بر وزن
یشواز. نام کوهی است از ولات ماوراد النهر.
بیلو فك - با واو بروزن ربشخند » نام
داروبی است که آنرا شادنه گویند و بجهت
داروی چشم بکار برند .
لهر ح کر اول و مکون ثانی و رای
فرشت ۰ جامه خواب را گویند مانند نهالی
ونوشك» وآنجه کتردنی باشد بجهت خواییدن
خصوصا - و ماه و طوفان را نیز گفته اند -
و بمعنی حفظ و از بر کردن هم آمده است ۴
و در عربی چاء را کویند ۴ - و بهندی بمعنی
برادر و پهلوان و شجاع باشد- و بش کی يك را
)0 ث ۳ خوشو باشد.
۱ رك : صفحه قبل ح ۷.
گویند که عدد اول است.
لیر اد - - باثانی مجهول بروزن شیرازه
شاخ حیوانات را گوشد.
ثبر ان « بروزن ومعنی ویران باش دکه
نقیضی آماد است * .
یر انه « بروزن ومعنی ویرانه است که
خرابه بائد ٩‏ .
ثیر ا۵ ۱ س دوطرف راء را گوشد که در
آن جاده نناشد و کنابه از عردم نا هشخص -
وکارهای ناشاسته باشف ‏
ثیر بو شا ۷ - با بای ابجد بواو رسیده
وشین قرشت بالف کشیده, بلفت زند وپازند (۷)
خبار بادرنگ را کویند.
یر رگ - بفتح زای تفطه دار و سکون
دال بی‌نقطه. صمفی باشد مانتد مصطکی . سبك
وخشك و بوی یزی دارد ۰ و طبیمت آن گرم
و خشك است » علاج عرق النساء و نقری کند
وحیض را براند ؛ و بچه مرده از شکم بیندازد
ودر مرهمها نیز داخل کنند »و ممرب آن بارزد
باشد ۸ - و براده‌ای رائیز گوبندکه روبگران
ازسوش سوهان جمم کنند - و براد فلزات را
کتهاند مطلقا - و دارویی باش که بردمید کیها
مالئد تامگس برآن ننشیند وبه کند - و چیززبرا
فیز وتا کته رویگران بجپت لحیم کردن
ووصل نمودن چیزها بکار برند .
ثبر ۵2 « با ها ء بر وت و ممنی اول
برزد باشد؛ وآن صمفی است بفایت گنده ومنتن
تن انتف ۳
1 اوسنابی ۵۷1۳۸ (اطلاع) «اسفا ۱: ۲ ص۲۹ درپهلوی ۷۱۲111 بمعنی خردمندی‌وهشیاری
ی . گودی ۱۷۹۲ ومکری و1 .۰ و13 (آموخته وباد گرفته) ۰ رل ارداو بر افنامه بقلم نگارنده
ف .2۲ (: - شش ( چاه) . و۲ و فان : ۵ د رظ : ویرالد .
۱ - بپاوی 2۳6725 « منای ۰۲۹۷ . - هز, 0۷۵۱15 بادرنک « بوستی .
شدهش. ۳« ۸ ره : برزه و سرزی . - ره : سرزد وببرزی -
```


## [2026-09-05T17:22:25.094Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in range(266,276):\n    print(i, repr(t[i][:120]))\nprint('---')\nfor i in range(356,366):\n    print(i, repr(t[i][:120]))\nEOF",
 "description": "Locate BQT v2 leaves for pp.813, 904"
}
```


### [2026-09-05T17:22:27.076Z] TOOL RESULT

```
684
266 '                                     \u202bگفتار هم\u202c\n\n \u202bاز کاب برهان قاع در بیرف دال ہبی قطه با عروف پجی\u202c\n\n \u202bمبتنی بربست و یك'
267 ' \u202bداد\u202c\n\n\u202bداخم د بكر اك بروزن قاسم »\u202c                          \u202bفرشت (\u202a )۱\u202cولام\u200cبتحتانی کشیده ویمیم زده » طایفه\u202c\n\n       '
268 ' \u202bیارس\u202c    \u202b¬\u202a۸\u202c\u202c                                                                                         \u202bداما\u202c\n\n      '
269 '                                                                                                       \u202b=\u202c         \u202b\u202a06\u202c'
270 '   \u202bوت\u202c                                                                                                         \u202bدارا\u202c\n\u202b'
271 ' \u202bدار شش\u200cدو\u202c                                                                                      \u202bسس\u202c   \u202b\u202a۱۱\u202c\u202c\n\n\n\u202bدارخا'
272 '                                                                                 \u202bداز شمان\u202c\n\n\n\n\n                        '
273 ' \u202bدای\u202c                                                                                              \u202bسور\u202c\n\u202bچوب بندند کتب'
274 '      \u202bا\u202a6\u202cس\u202c\n\n               \u202bداستخاله است که مذ کور شد \u202a.\u202c\u202c              \u202bاست مانند دای ودسته دزازی هم دارد و حرية "\u202c\n'
275 ' \u202bداغ سو\u202c                                                                                                            \u202bس\u202c'
---
356 '\u202bپاسس\u202c                                                                                                   \u202bذو روژی\u202c\n\n\u202b\u202a ۱'
357 '  \u202bدوس\u202c                                                                                              \u202bو\u202c\n\n\u202bعزیز دارندش م'
358 '     \u202b—~\u202a—~AAA\u202c\u202c                                                                                                        '
359 ' \u202bدوکار \u202a:\u202c\u202c                                                                                                        \u202bتس\u202c'
360 '  \u202b\u202a ۵\u202cات\u202c   \u202bتن\u202c\n                                                                                                    \u202bد'
361 '                                                                                                             \u202b=\u202c   \u202b\u202a۱\u202c\u202c'
362 '    \u202bهت\u202c                                                                                             \u202bدوبره\u202c\n           '
363 '  \u202bدپهنجی\u202c                                                                                            \u202bوروت\u202c\n\u202bده انگشت ب'
364 '   \u202b\u202a-\u202c\u202c    \u202b\u202a۰\u202c\u202c    \u202bیت\u202c\n                                                                                              '
365 '                                                                                           \u202b\u202a6\u202c\u202c   \u202b= \u202a۵\u202c\u202c\n\n\n\n\n\u202bدهگانی س'
```


## [2026-09-05T17:22:38.568Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(268,278):\n    p=t[i]\n    print('='*15,'leaf',i, 'printed~',i+543)\n    print(re.sub(r'[‪-‮]','',p)[:1600])\nEOF",
 "description": "Print BQT v2 leaves 268-277"
}
```


### [2026-09-05T17:22:40.269Z] TOOL RESULT

```
=============== leaf 268 printed~ 811
 یارس    ¬۸                                                                                         داما

           نگیوزبند ؛ وبکرثالك گهفتمه‌اند .                                       .     وماضی دادن هم هت
                      داد ا
رست» با رای قرشت بر وزن                                 بادودال بالفکشیده.هر کنیز ()۱          3۵
                بازخواست » بمعنی عادل باشد .             راگونند عموماً وپیر کنیز کی را( )۲که ازطفلی
دادر فلت بنتح الك بر وزن ناپسند .                                      خدمت کی کرده باشد خصوصا .
                      پرادریزر گے راگو بی 0              دادار  = ۲بر وزن بازار "نام خدای
دادستان = بکون‌سین بنیقطه‌بروزن                          عوزجل باشد  -وپادشاه‌عادل رائیز گویند ومعنی
                                                                  آن داد ورعده وداد دهنده اعت . ۴
تابستان *بمعنی شرىك شدن  -وراضی کردیدن
باشد دکارری -وبکرسین .بممتی‌داورودادری ٩‏                از نامهای     یکی        داد  ۲فر بد =
و یفن 0وی  ۷هم گفته‌اند -کونابه ازیادشاه نیز              خدایتمالی است عزوجل  -و نام توابی هم هت
                                       هت . ۸                                        از موسیقی .
دادفر مای = با فا ومیم بر وزن پای                        داد قرفی ادم ات از اسمای
برجای .یکی ازتامهای‌حقتمالیاست  -وپادشاان                         الهی -ونوافی ات از موسقی (. )۳

                             عادل رانیز گومند ۰          داد ۵ص بکر دال سیم وسکون ها .
مالك پروزن‌چايك» پیرغلام          دالگ                   تامی‌است ازنامهای خدای‌نعالی -ونام روزچهاردهم
 قدیمی باشده  -ومخقف دادبیگه‌است واوشخصی                                    
=============== leaf 269 printed~ 812
                                                                                                       =         06




                                                 از جعنهای                  هست ¬ E‏
ادى= بروزن هادی.ا وحبی
است بیار تلخ باندام جولیکن از جو باربکتی
را جوجادولیز کوبند  .بواسیر
                          نآودرازترمیشود و
                                                  سینبی تقطهوفوفانی مفتوح برای‌فرشت ()۱زده ۰
                           را بقابت نافع است
                                                   نام خدای       که       داد گر اس ےت     دوم    و       اول   بمعنی

 دادی دومی  -درایی است که
                                                   عزوجر؟  -وعادل باشد  -کونایه ازدل هم‌هست
 آنرا برومی هوفاریقون  ۸کوبند » و آن حبی                                            که بعربی قکلوبیند ۶3.
 باشد سرخرنگه مانندسماق بغدادی .کرم وخشك
                                                  دادر ند       یایند  ,مخقف         روزن    ند ۵          داد
اورام   طف
         لوملل
             است در سیم و چهارم  .مح                                       است که برادر برزک باشد . ۴
                                       باشد .
                                                  دادو  = ۴بروزن بابو » مطلق غلام را
داد د بر وزن خار  ۰مطلق درخت را
                                                      گویند عموما ( -)۲ویر غلامیرا که اکزوچکی
 کوبند  -وچوییکه دزدان  ۴را ازآن بلق                                        کسی کرده باشف را                     خدعت

 آریز ند -وچوبیکه بدان خانه پوشند  -وبمعنی
 دارنده باشد وقتی که باکلمه‌ای‌تر کیب شودهمچو     گراست     بروزن ومعنی داد    
=============== leaf 270 printed~ 813
   وت                                                                                                         دارا
داادرار کردن" » با دال ابجد ,                                 است در هندوستان  -و داامروبی که آنرا
کنابه ازدیر باسدن وشات داشتن -ومدارا کردن-                     -و بممنی داشتن و امر           وزبند
                                                                                                  ی دگرا
                                                                                                       ظمفل
                                   باشد   ویسار ماندن         بداشتن‌هم هت  -وبمعنی داورهم آمده است که
                                                              خانه      بی
                                                                         روع-
                                                                            یشد
                                                                              مکی از نامهای خدایتمالی با
ممدوده       قریں  - ۸با همزه              دار
                                                                                         ومحله رگاونند .
ومتصوره هردوآمده است وسکون‌فا .هرچیز که
                                                               دارا = بروزن خارا  ,نام بادشاه مشپور

وینچره       وامثال آن     وخواه سنوای     آن مححری
                                                               است که دارای! کبر,اشد واورا داراب نیز گوبند.
                                                               ولو درزمان سکندر کشته شد ودارای اصفر پس
را نز گربند که دریش خاله مابن دو                ومحجری
                     
=============== leaf 271 printed~ 814
 دار شش‌دو                                                                                      سس   ۱۱


دارخال = با خای نقطه دار بر وزن                       دار با » ۱بابای ابجد بالف کشیده ۲
پارسال  ,درختی که آنرا پوند نکرده باشند -                       مابحتاج وضروری ودرباست راگویند .
وشاخ‌درختان( )۳توشانده رائیز گویند  - ۷وهر            دار بار  - ۲بروزنکارساز ,شخصی را
بونه ودرختی بود که از جابی بر کنده باشند()4
                                                      کوبند که چوب بلندیرا در زمين محکم سازد
                       ودرجای دیگربنشانند .               وبر اطراف آن ریسمانها بندد ویربالایآن چوب
داردار کردن  ۰ ۲کنابه از در                                          رود وبازبپای عجیب وغریب کند .
پاییدن وثبات داشتن  -ومدارا کردن  -و بيار             دار بام  = ۳بروزن شادکام " شاه تیررا
                            ماندن باشد ()e‏ .         کویند » وان چوب برزکی باشد که بدان بام
                                                                                            خاله بوشند .
دار دان .وبزرن‌اردان» بمعنی‌تخمدان
برآن   باشد» وآن زمینی‌است که شاخهای درخت
                                                      دار بر = بضم بای ابجد و سکون رای
فبرروند تاسبز شاوزدآونجا بجای دیگر هل                 قرشت( » )۱نام مرغیست سبزرنگ که درختانرا
                                                      ممنقار سوراخ کند * و آن را بشیرازی دار نمك
                                                                                                خواند . ۴
داررومی = داروبی باشد رومی .
                   گوبند نافع لقوه است .              دناربپارن ه بفتح بای فارسی .
                        
=============== leaf 272 printed~ 815
                                                                                 داز شمان




                        -     دار کوب             دارشعان  = ۱باشن‌شطهدار وعین
                       بز وزن خاکروب ,            بی‌نقطه بورزن آبریز گان » درختی باشد سطبر
                        بزبان .کیلالی‌مرغی‌را     و خاردار وپوست آن بقرفه ماندلیکن از آن
                       کونند که بامتقاردرخت       کت تقر وسرخ نرمیشود  .اکرقدری ازآن‌سحق
                               را سوراخ کند .
                       دار بوگاوورسیشده۔
                                                 کنتد وما سر که سرشند وبردندان لهند درد را
                                                  فروشاند» وقدری ازچوب آن‌زنان‌بخود ب رگبرند
      دارکوب                      باکاف قارسی     قرزهدی که درشکم مرده باشد بیفتد  -و ستبل
و مشین نقطه دار زده » امر به نگاهداشتن باشد       هتدی را فز دارششمان خوانند و دارشیمان «م
               بعنی نگاهدار ومحافظت کن © .                          کوبند بحذف شین دوم .
دار کیسه  ۱س بکر کاف و سکون                                             دفار
                                                 رلی  - ۲باوفراای قرشت بر
بای حعلی وفتحصین بینقطه " کسه مانندی‌است
که دربعضی از درختها بهم ءیرسد ودرون‌آن پر        وزن بتماکین » سفهوسکو ود کهکروابند که
                                                  تن در بیش درخالپا سازند  -و مطلق       بجهت
                            از یشه میباشد .                          تکه کاهر ا نیز کفته‌اند ۱
دار هك » بامیم بروزن آبچك » نوعی
                                                      دار فلفل  ۴مهعروف است گ
                                    
=============== leaf 273 printed~ 816
 دای                                                                                              سور
چوب بندند کتباوتران ودمگر پرندکان برآن                 دار و برد بادال ابجد درآخربروزن
            .      بنشینند  -وترجمة لفظ هم‌هست       ساز وبرگك » بمعنی طاق وترتب گویرودارو کر
بر وزن طاس » افزاری است       داس                                             وفر وتبخترباشد .
که بدان‌غله درو کنند وبعربی‌منجل خوانند- ۴            داره = بروزن چاره  ۰وطیفه وراب را
                                                      وشفف دایره است  -وهاله ماهر اثبز
                                                                                     م  کن
ده برسردانه‌های کندم
                   وخهای‌سر تیزرانیزکوبن ک
                                                                                            کفته‌اند ١‏ #.٭#
وجوی است که درخوشه میباشد  - ۴ونوعی از
اک ار با کت و تسیر (]۱                                داره س با زای نقطه دار بروزن تازه »
 ری     رها
          نکآایی
               است دو             هی
                                   -ویتا
                                       گ‌هس
                                          هم         آن است که دو چوب بلند را پر زمین فروبر ند
سداب خوائشدت ودهره رانز کفتمانه وآتسلاحی               ماندڭك فاصله وجوب re‏ عر ص بربالای آن دو


                                                                         .    ) (۱چش :لخحر


  « وازء»       باین معنی مصحف     ۴          ۱ع-بنابینعربی است  .رك  :داظم لاطبا .
                                                                                  م
  ۴پ-لوی  . 58هندی باستان  ( 210۵1 -دای » کردی
  
=============== leaf 274 printed~ 817
      ا6س

               داستخاله است که مذ کور شد .              است مانند دای ودسته دزازی هم دارد و حرية "
                                                         و استخوان ماهی را لیز           ۱       مردم کیلان ات
دستحاله  = ۷بخاای نقطه‌دار بروزن
                               ا
پارساله » بمعنی داستکاله است که دای کوچك                                                                   کوبند .
 باغبادان باشد  -وعصای سر کج را نکیفزته‌اند.
                                                          داساد ؟ ب‏روزن پاکر ,دلال راکوند
داس ر رین د کنابه از ماه نو ات                                               وحریی سمسار خوانند .
                             وبعربی هلال گوبند .          داستاره بانای فرشت بر وزن نادار
                   داسفاله  ۷د باغن                       یمعئی دامار است که دلال وسمار باشد وبعربی
                   نقطه‌دار» بروزن ومعنی داسخاله

                  است که دای کوچك و عسای                  داستان؟ س بروزن پاسبان » شهرت -
داسفاله (داسکاله)             سر کج باشد.                و مثل باشد  - ۴و حکات و افانه را لز
                                                                                                       کونند ® .
داسگاله  ۲ه با کاف .بروزن ومعنی
                           وفته شد .
                                   داسفاله است گ
                                                          داستخاله  - ۱باخای قطه دار بالف
                                                                                     کشیده و فتح
                                                         لام ؛ دای کوچکی باشد که بدان
 -نات و قتح‌دال             وس
      
=============== leaf 275 printed~ 818
 داغ سو                                                                                                            س
                                                                                                                   ری ۱
                                                                                                                      تس


 داشن  = ۲بروزن دامن؛ عطا وبخشش                             خوشه است ٩‏ -وداسی را گیوزیند که غله
وانعام باشد  -واجر ومکافات لیکیرا هم گوبند                                                    ۰   کنند ۳           بدان درو


 ودر زند ()۱مرقوم است که داشن نقد وجنیرا                   داش س بر وزن فاش » کوره ایکه
                                                                                ۰                          =



گوبند که پارسیان‌درعید وجشنهابرسم نذرباصدقه                   وخموکاسه و کوژه وامثال ‏ ن‌دران‌بیز ند۰ ۴                حشت

                   بففرا ومسا کین بدهند . ۸                                         وهمعني کاستان همکفته‌اند ۰

داع  = ۹بروزن باغ» ممروف‌است *-۱                              داشاب = بروزن داراب » بمعنی داد
وبمعنی‌شان همآمده است ومعنیی ( )۲که شاعر                                    ودهش وچیزی بمردم دادن باشد .
                                       چ
ند جا ببندد  -ونام شاعرکه درغزل و فصده                        داشاك « بروزن آزاد » بمعنی شاط -
                                           مذ کور شود
                                                              و عطا وبخشش وانعام باشد وبمعنی اجر وتلافی
 کنابه ازنشانی‌باشد           داع بلندان ت
                                             
=============== leaf 276 printed~ 819
 ”“AI                                                                                                          داغ شدن

دالیز و٩‏ تست س بای اد و فتح زای                                       داع شدن  -بنایتآزرده شدن باشد.
هوز ,مرغی است کوچك وجهنده که عرب صموه                                   کونابه ازهیب دارگردیدن  -وشهرت بافتن -
گوبندش ؛ و بعضی گوبند نوعی از وطواط است                                            وکهنه ومتعمل بودن هم‌هست ٩‏ :
                                           وعربی وصع خوانند .          داغ گاز ران = نشانی‌باشد که‌بر کذار
دال پور ببای ابجد ودال پوز                                              پارچه کنند تا درشستن بدل نشود  -و داغیکه
با بای فارسی بروزن خام سوز » نوعی از وطواط                                                            بهنج چیر نرود .
                       اوسفتر-اشتروك را نگیوزمند .                       ارغول,
                                                                              ووازومنجه‌ولش ب
                                                                                            با      داغول ۲
دال بوده"  ۰ودال پوزه بازبادنی                                                         عار ومکار وحرامزاده گروایاد .
ها » یمعنی دال بوز است که نوعی از وطواط-                                 داغولی  = ۴بمعنی حرامزادکی
وفراشتروك باشد؛ و درهردولفت بجای بای ابجد                               وعیاری باشد ‏ ونام جاسوس نصر سیارهم هست .
                            بای حطی هم بنظرآهده است .                   داغینه = بروزن‌بارنه ,کهنه ومستممل
 دال خال  ۳۱۰باخای قطم‌دار بروزن                                                                
=============== leaf 277 printed~ 820
 دامن بدندا نکرفتن                                                                            ۷۱رس

                                        گفته‌اند . ۴     دام = بروزن رام» نقیض ددباشد که‌آن
                                                         وحشی غیر درنده است عموماً و آهوو غزال و
                                                         لیر را()۱گویند خصوصا  - ۱وحشرات‌الارش
                                                         وپرنده را هم میگوبند  -و هرچیز که جانوران
دامگاه ستول = بمعنی دامگاه دیو
                                                         در آن بفریب گرفتار شوند  - ۴و نزد محققین
                     است که عالم سفلی است .
 e‏ تیدام اور         گرگ            دامگاه                                             بمعنی زخارف

        است کهجهان فانی وعالم سفلی باشد .                                              دلیوی و آنچه
دام آشتن > کابه از بازی دادن ودام                                                   باعثبازماندکیاز
                                                            مبداء باشد . # .نوعی‌دام (تور) ماهیگیری
           -وخلاصی از دام باشد 9 .           سردن

دامن باغی گرفتن -کنابهازخلوت
                                                         دامفول -با غين نقطه‌دار وواوه‌جهول
                زیدن گووشه نشینی باشد .                  بروزن زاغنول ,دانهاو گرهها باشد مانند گردکان
دامن بد ندان گردن = کنایه از                             که ازاعنا کولوی مردم برمیآید ودردنمبکند
نمودن باشد د و کنایه از        فروتنی کردن و عجز         نورآاسلعه میکوبند -وغول‌بیابانی رائیز گفته‌اند
                  گرشختن هما مدهاست (. )۲
```


## [2026-09-05T17:22:58.611Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(359,366):\n    p=re.sub(r'[‪-‮]','',t[i])\n    if 'دهره' in p or 'دهر' in p:\n        print('='*15,'leaf',i,'printed~',i+543)\n        print(p[:2500])\nEOF",
 "description": "Find dahreh in BQT v2"
}
```


### [2026-09-05T17:23:00.247Z] TOOL RESULT

```
=============== leaf 364 printed~ 907
   -    ۰    یت
                                                                                                                                 An



مرد بار دلیر وشجاع باشد  -و مردم‌کاز کرده                             الى و فتح           وسکون   یکراول           .       دهچه


 وصاحب غیرت رانیزگفته‌اند -وبمعنی حرامزاده                            جیم فارسی  ۰بزبان دیلم رعیت و دهقان را
                                         ۱       همآ مده است



ذهر نکوهی  - ۸کات دنیاکردن                                             ور نس   دم خدا  » ۱بکراول ,کدخدا
وبد اگوفتن باشد  ,چه دهر بمعنی دنیا و عالم                                                              ویزرکف ده را گونند ۲

 سفلی و تکوهی بمعنی عیب جویی و بگدویی
                                                      ۰   باشد
                                                                      دار نده ده را گونند هنی سر کر ده رعایا ومزارع-

  دهر ه ٩‏ ت بر ورن هره حربه ات                                                                                            وه و بدار .
دمته دار ودسته‌اش از هن وسرش‌مانند دای باشد
                                                                      ده دله  = ۲بفتح اول و سکون انی
ودرغایت تیزی بوده و بیشتر مردم گیلان دارند                             کر دال ابجد ولام مفتوح  ۰بیوفا جواهیری‌راو
                                                                      وسی که هردم‌دل بدیگری دهد واو      کویته  -ک
گویند       ند وبعهي
                   افزاری‌است که بدان غله دکرو                        ایوالهوی خوانند  -ونر دم‌طدفقن آنکه هر لحظه
                                                                                                                  ر

                                                                      باعتقادی و کیشی‌باشد  - ۴و کنابه ازمردم شجاع
مالاد        و      دمه   ودو   کوچك     دهر ه شمدبرست


                          سر سنان باروك وتیز میباشد.                                                               دولیر هم هت .
 ذهرة صبح -کنابه از روشنی سبح                                           -بر وزن ابله » زر بی عیب                           دهه"
                                                                                                                              د
                                                          ات                                                   .       وخالص راگوبند

ده سال = باسن بی‌نقطه بروزن ابدال,                                     ابلهی بمعلى دهده        = بروزن        دھی'              ۵
 بمعنی کوا کب س
```


## [2026-09-05T17:23:10.992Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=re.sub(r'[‪-‮]','',t[364])\nprint(p[2000:])\nEOF",
 "description": "Print footnotes of BQT leaf 364"
}
```


### [2026-09-05T17:23:13.480Z] TOOL RESULT

```
                                     -بر وزن ابله » زر بی عیب                           دهه"
                                                                                                                              د
                                                          ات                                                   .       وخالص راگوبند

ده سال = باسن بی‌نقطه بروزن ابدال,                                     ابلهی بمعلى دهده        = بروزن        دھی'              ۵
 بمعنی کوا کب سیاره است که زحل ومشتری()۱
                                                                     باشدکهطلا و زر خالص بعییب و تعام عبار
 ومر بخ وآفتاب وزهره وعطارد ( )۲وقمرباشف -                                                                                      است . ۷
 وبیونانی بگزهر‌ترین موجه رگوابند ازموجهای
                                                          وتا         دهر کاسه گردان » کنابه از دیا
                                                                                                   وروز کارعالم مفلی باشد .
 نام شهر      دهستا  = ۱۱:بروزن دستّان»
                                             :    ومدننه‌انست         ر ګه۔ باکاف فارسی بر وزن معر که»                          ۵


                                         -عطارد .         )<( چش:                  .     ) 0چجش :و عطارد وهشتری

    ‏ - ٩از  :دخهد+ا (صاحب .روئیس) .همن‌کلمه‌است که درقزوینی  ۷0×30گردیده.
         - ۳از  :ده (عدد) ٣‏ دل Fo‏ (نمیت‌واتصاف)                              ۰       از  :ده  +دار (دارنده)               ۳


                  صراف وجود باش وخود را چله کن(؟)                     هرده یله کن            ای نه داه ددهله                ۴
   انتت که         وراد   (نست)        + ).ی       ده ( .۵م      از  :ده   -   ۹              دهی. ‎    :ده   رك       -    e


                           دهی.   ده     .رك :رر      بفار eaF‏ ننست            رر است ومخلوط           دهم (تمام)مكوك.               ده


            باززجستدد (منجمان)سیم ده پنجی                                      در ترازوی آسمان سنجی                         ۷
            قد ,وزیا گنز شانه .امه :                                                   آمد    خود زر ده دهی نك

   اظامی کنجوی «هفت یبکر چاپ ارمغان ص .۵4 ۷اشار هید اش بپرام گور ازیزد گرد بزهکار.

    -ساسکرت 272۳14                ۵                 اسم مصنر از #بکوهیدن» بجای «نکوهش» .                                    ۸
    یه در صفحةٌ ۵۰٩‏
```


## [2026-09-05T17:23:26.995Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T17:23:27.011Z] TOOL RESULT

```


```


## [2026-09-05T17:23:31.096Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1",
 "prompt": "Give the full etymology of Persian بیدستر (bidastar) 'beaver' — the reconstructed Proto-Iranian/Avestan forms, Middle Persian form, and any cited sources."
}
```


## [2026-09-05T17:23:32.200Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%B3",
 "prompt": "Give the Persian entry داس (dās) 'sickle': its etymology, Middle Persian form, Proto-Iranian and PIE root, and cited sources."
}
```


### [2026-09-05T17:23:35.630Z] TOOL RESULT

```
Based on the Wiktionary article provided, I can only offer limited etymology information:

The article states the word "Perhaps a compound word from Proto-Indo-European *widʰu- ('tree, beam') and *h₁ed- ('to eat'), literally means a 'wood-eater'."

However, the source does not provide:
- Reconstructed Proto-Iranian or Avestan forms
- Middle Persian forms
- Cited academic sources for these etymologies

The only etymology given traces the word back to Proto-Indo-European roots, suggesting a descriptive compound meaning "wood-eater," which would be semantically fitting for a beaver. No intermediate historical forms or scholarly citations are included in this Wiktionary entry.
```


### [2026-09-05T17:23:37.919Z] TOOL RESULT

```
# Persian Entry: داس (dās) - Sickle

## Etymology

The word داس derives from a long linguistic lineage:

**Middle Persian:** dʾs (/dās/)

**Proto-Iranian:** *dáHθra-

**Proto-Indo-Iranian:** *dáHtram ("sickle")

**Cognate comparison:** Sanskrit दात्र (dātra) shares the same root.

## Sources Cited

The entry references two primary sources:

1. **Steingass, Francis Joseph** (1892). *A Comprehensive Persian–English dictionary*. London: Routledge & K. Paul.

2. **Nourai, Ali** (2011). *An Etymological Dictionary of Persian, English and other Indo-European Languages*, page 78.

The etymology demonstrates the word's ancient Indo-European origins, tracing back through multiple language families and preserving its meaning across millennia of linguistic evolution.
```


## [2026-09-05T17:23:47.126Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN bidastar/dās\"; grep -n -i \"bīdastar\\|bidastar\\|bêdastar\\|Biber\" HRN.txt | head -10; echo \"=== HRN das\"; grep -n -i \"dās .Sichel\\|Sichel\" HRN.txt | head -10; echo \"=== HUB\"; grep -n -i \"bidastar\\|Biber\\|Sichel\" HUB.txt | head -10",
 "description": "Grep Horn/Hübschmann"
}
```


### [2026-09-05T17:23:47.210Z] TOOL RESULT

```
=== HRN bidastar/dās
1984:aw. bawri' 'Biber*; phlv. baprak d. i. bawrak *Biber
1986:Das np. Wort bezeichnet den *Biber' nicht, es scheint
1987:aber lautlich identisch zu sein. Ob Biber heute in
10247:48. batvrak Biber, siehe oben No. 181.
=== HRN das
4729:525. (IffS 'Sichel'.
4730:ai. dätra- 'Sichel'; phlv. das (AV.).
4731:afy. lür 'Sichel'; LW. kurd. bei. (76) das,
=== HUB
814:'Biber' (Horn Nr. 181). So kommen wir uber np. habr,
3443:'Mondsichel', auch *ein ihr ahnlicher Schmuck' (Jes. 3,
7254:zd. padra^; das ^Sichel', phi. das Gl. and Ind. 181, skr.
```


## [2026-09-05T17:23:48.799Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY داس\"; grep -n \"داس\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY latin index DAS\"; grep -n -i \"sickle\\|DATRA\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Aryanpur for das"
}
```


### [2026-09-05T17:23:48.877Z] TOOL RESULT

```
=== ARY داس
379:داستان برج بابل چه بود؟
383:از ساختن پرج دست بکشند. این داستان اخلاقی عواقب غرور را نشان می‌دهد ولی طی قرون متمادی
424:ندارد. ولی چون هنوز پایبند داستان برج بابل بودند این عدم شباهت را ناشی از دانحراف» و «پستی»
526:داستان برج بابل اعتقاد داشت و فکر می‌کرد این زبانها همه از زبان واحدی سرچشمه گرفته‌اند و این
985:کین‌تر همین کار را می‌کردند. مثلاً در داستان جنگ تروا آمده است که آقاممنون
1105:شاعر و داستان گزار دربار شاه السینوس (۸1.21770175) در حماسه‌ی ادیسه (0195883) نمونه
1337:بررسی قرار داد. این گوئه توضیحات که معمولاً همراه با یک داستان ارائه می‌شوند جالب‌اند ولی
3222:۲ / بر وَبر (به چم "بیداستر" یااسگ آبی-)
7668:داس» داسه / ۲۶۱
11857:چم این واژه در زبان‌های آلمانی و لیتوانی و لتونی: داس دسته بلند» داس :
=== ARY latin index DAS
7511:POKORNY, = SSO*~*~S*~*~«dS DATRAM, (DATRA, OATI, DAYAT!)
```


## [2026-09-05T17:23:57.991Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN 1978-1995\"; sed -n '1978,1995p' HRN.txt; echo; echo \"=== HRN 4725-4740\"; sed -n '4725,4740p' HRN.txt; echo; echo \"=== HUB 805-825\"; sed -n '805,825p' HUB.txt; echo; echo \"=== HUB 7248-7262\"; sed -n '7248,7262p' HUB.txt",
 "description": "Print Horn/Hübschmann passages"
}
```


### [2026-09-05T17:23:58.066Z] TOOL RESULT

```
=== HRN 1978-1995
wo findet sich aber die Form?)?).
Zusammenhang mit ai. vyäghrd- 'Tiger, arm. vagr
Tiger* ist unklar. — Kustem's bebr^T beyan gehört
wohl zu np. geber, der zweite Teil ist ganz dunkel.
181. {2)beber * wildes katzenähnliches aber schwanzloses
Tier, dessen Fell man verwendet*, auch weber (FR.).
aw. bawri' 'Biber*; phlv. baprak d. i. bawrak *Biber
(Men., Bund.); vergl. ai. babhrü- *braun, Ichneumon.
Das np. Wort bezeichnet den *Biber' nicht, es scheint
aber lautlich identisch zu sein. Ob Biber heute in
Fersien vorkommen, ist nach Blanford, Seite 51,
zweifelhaft.
r
W82. but ^Götzenbild; Liebchen.
aw. Büiti- N. pr. ; phlv. Büt, Bütjan (Gemme, Hörn,
Mitteilungen, Heft IV, S. 40, Note).
Wenn die Zusammenstellung richtig ist, so gehört
np. but in dieselbe Kategorie wie gStl^ ätes, petyäre

=== HRN 4725-4740
524. dm*e 'Gehalt, Salair'.
aw. dadra- 'Geschenk, Gabe'; phlv. ddsr; ai. däfra-
'Gabe'.
Hörn, KZ. 32, 584 No. 15.
525. (IffS 'Sichel'.
ai. dätra- 'Sichel'; phlv. das (AV.).
afy. lür 'Sichel'; LW. kurd. bei. (76) das,
526. däS 'Ofen*.
Zu [/'dagli' (aw. dajjz-, ai. rfa/i-), brennen (Nöldeke,
mündliche Mitteilung).
527. dästen 'halten, besitzen', Praes. där-em, dar, dara,
g. dartmfm; Käs. dörtän^ dördhi, dörd^nmn^ dort.
ap. l/^rfar-, darayamiy, adäraya 'halten, besitzen';
aw. [/^dar-^ däray^M; phlv. dästan^ dar-am, dar(i)sv^
dästar [syr. LW. *T1, ödg (de Lagarde, Ges. Abh.
33) sind verlesen (Nöldeke, Tabarl-Übersetzung,

=== HUB 805-825
upa + eti) zuriickgehen. Aus upO^ konnte nur ba
werden, wahrend sonst upa^ in Comp. vor Conson. zu
uWy aw werden musste. So kann auch t>ai (in andar-
vdi 'Bedurfnis*) formell = skr. upaya- fAnnaherung,
Mittel, Weg') gesetzt werden.
180. Vgl. afgh. bavr 'a leopard, a panther', kurd. bdvru-
beyOn Parderfell*, bavlubayan Telzkaputze* (?) Socin,
Samml. II, 286. Die Pehleviformen sind wohl wertlos,
vgl. phi. baprak (Phi. Min. p. 37, Z. 8) d. i. bawrak
'Biber' (Horn Nr. 181). So kommen wir uber np. habr,
*bawr 'Tiger nicht hinaus.
181. Dieses Wort ist auch arabisch: vaftr animal quadrupes
fele minus, pulveris colorem habens, cauda carens*.
Nach Noldeke ist vabr 'Klippdachs* „wohl echt
arabisch**.
*) Also falsoh ftir vavar, vgl. avar oben Nr. 53.- 26 -
182. Np. hut ^Gotzenbild, Idol' (afgh. LW. but) nach Fr.
Miiller = Buddha, nach H o r n ~ zd. buiti 'Name eines
Damons' (vd. 19, 1). Beides schon im grossen Bunde-
hesh, vgl. Darmesteter, le Zend-Avesta II, p. 259.
184. Np. haSa, haSSa Munges, Kind' = phi. vacak (aus

=== HUB 7248-7262
§ 96. Ap. &^ wird im Np. zu s oder hr:
a) zu 5 in: si, [liter se *drei' (s. oben p. 78) = zd. g.
pi. x^rayqm, vgl. ap. ^Htiya- *der dritte*; si 'dreissig =
ap. "^Old^at-, zd. drisat-] pus 'Sohn (daraus pnsar, pisar
nach pidar u. s. w.) = ap. pud^a-; pas 'Wache', phi. pOs
Gl. and Ind. 91, Bdh. Gl. 96, paspamh *Schutz' Bdh. Gl. 96,
zd. padra^; das ^Sichel', phi. das Gl. and Ind. 181, skr.
datra-; obis-tan 'schwanger, phi. apustan Gl. and Ind. 16,
apus H. 5 = zd. "^apu&ra- (fiir apu&ra-), s. oben p. 5.
b) sonst zu hr, das nach urspr. langem oder zum Er-
satz^) gedehnten Vokale zu r wird: pur *Sohn = phi. puhr
V V V V
in S(a)puhr = arm. Sapuh (alter Sapurh), np. Sapur, ap.
pud^'a-; pahra^) 'Wache, arm. pah 'Nachtwache, Wache,
Gewahrsam, Gefangennahme, Belagerung' (alter parhY
```


## [2026-09-05T17:23:59.521Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7660,7680p' incoming/ARY/ARY_pages.txt; echo \"=== 11850-11870\"; sed -n '11850,11870p' incoming/ARY/ARY_pages.txt; echo \"=== 3215-3230\"; sed -n '3215,3230p' incoming/ARY/ARY_pages.txt",
 "description": "Print Aryanpur passages"
}
```


### [2026-09-05T17:23:59.587Z] TOOL RESULT

```
اسلاوی کهن (ح ماد تل#تاتل صزم): برهان قاطم + ۸.۹
۸ ,075۷0
یادداشت:
۱ در بیشتر زبان‌های هند و اروپایی این واژه هم به چم آدرخت" و هم به چم "چوب" بکار می‌رفته.
۲- چم این واژه در زبان‌های ابرلندی کهن و گالی: درخت بلوط.
۳ چم واژه‌ی 73۸6 در زبان ارمثی: محکم.
[pdf page 260]
۹
داس» داسه / ۲۶۱
| چم اگلسی سرواژی نارس نس ۱8068
پهلوی (41اتقهه): کة0
سانسکریت (84(/5077): پسگشت‌ها 35
0۸۸71 با0۸5 بف0378) ,0377۸3 8 20000
اسپانیایی (1874ل52۸)(شاید) ت0۸ 2 هقی :۸4275
لیتوانی (7770۸۷14(4/)(شاید) ‏ 2۸1/015 507 لاه
لترنی (لتی) (/147774۸)(شاید) ‏ 20۸7018 برهان قاطع : ۴۳
اوستایی (/ل4۲857): 328۸8171 ,0۸3 ۰ 7 ۳۸33۲
پارسی باستان (87814۸ صرا0): انگلیسی کهن (لدلا80/0 صا0): ۲فتق0۸ ۱
9 0۸ آنگلیسی (6(701/827) از لانین) ۳
پهلری (7ماللهه): 01۸0 اسلاوی کهن (ع۲7شا5 ل#ناتل صت0):
اوستی (05987/0): ۰ 2۸78 ,0۸410 0802۸71
=== 11850-11870
ا
کپ (به چم *دهان" "دهانه"» *ظرف شیشیه‌ای بزرگ"»» "قرابه») / ۳۹۹
91932 مل یبا
بادداشت:
۱ واژه‌ی "شکافتن " نیز از همین واجریشه‌ی هند و اروپاپی است (پهلوی: ۱5736۸۳7۸۸۷ کردی 573114۳717
برنانی: 157۸۳70 اوستایی:82۸۳71-)
۲- چم این واژه در زبان لاتین: خرد کردن؛ کوفتن.
چم این واژه در زبان‌های آلمانی و لیتوانی و لتونی: داس دسته بلند» داس :
کردی (0701571): همه ,6۲5۲ انگلیسی کهن (0ل3ا2(/0 ۰:0۵ 007۳
سانسکریت (5۸4۷۶/7): 1۳۸5 انگلیسی (82/0]8[1): 02
یرنانی (06524): ای ۱۹1۱ هلندی (0176071): 05
لاتین (/4710ما): ۸ ,1۳۸ ولزی (لقل): لا ره
فرانسه (۳82۸/673): رای برتونی (8/670/7): 07۳
اسپانیابی (5۳۸(۷/]524): 0۸ :
ایتالیایی (للل7۸): 0۸ پسگشت‌ها رای رد دادن
رومانی (44(/]4۸۷ا0): 03 [ و ۸000
پرتغالی (۳0777010585): 0۳۸ 2 (0۳) ی رن ان
ابسلندی کهن (/(5(/010۸4 0ا۵): 0 (0۲8) تلقملماظ۳
3 3349 82
ورس کهن (۸0۳85 010): 0۳ 1 (008157) 0
ی . فریز ی کهن 7791400 صا۵): 0/۳ برهان قاطع + . ۱1۹۳
=== 3215-3230
آلمانی (88۸/۸(۷): 88668 ,۳۸1005 6 (877065) ی ۱
انگلیس یکهن (80018 صل0): 721-2 ماه ۱
,۲01۸ ۲۵,8۷ ۷۷ 7 (8۸10305) :005 ۱
انگلیسی (تلولناه/(8): زا۱۱1۱ 4 (831065) :7
دانمارکی (4ل0۸415): دراه دی را پرهان قاطم + ۳۳۰ ِ
[pdf page 111]
لا ا ‏
۲ / بر وَبر (به چم "بیداستر" یااسگ آبی-)
یادداشت,
۱- معنی اين واژه در زبان‌های ژرمنی وگالی: پل
۲ این واجریشه‌ی هند و اروپایی به چم"دیرک" و یر" بوده است و شاید عل دهرگرنی معنی آن در برخی زبان‌ها
این باشد که پل‌های اولیه را از تیرهای چوبی می‌ساختند. ۱ ید
اوستایی (۸۲597۸/4): 3۸7۷81 ,ش8۸1۷ اسلاوی کهن (5].0170 0770767 017):
پهلوی (۲7مالز۸): ,3۸8۸6 ,8۸78۸ ( ز لن ۱
3۸۷۸/۸ لهستانی (/۳03): دزادنا
تخاری ۸ (۸ ((4ل/7057): 0 روسی (/فا55ل): 3
```


## [2026-09-05T17:24:14.323Z] TOOL CALL #37: WebSearch

```json
{
 "query": "ریشه‌شناسی بیدستر حسن‌دوست فرهنگ ریشه‌شناختی سگ آبی"
}
```


## [2026-09-05T17:24:16.114Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1/",
 "prompt": "Show the دهخدا and فرهنگ معین entries for بیدستر: definition and any etymology/origin tag (e.g. [پهل.], [يونانى], Latin/Greek forms)."
}
```


### [2026-09-05T17:24:25.737Z] TOOL RESULT

```
# بیدستر - Lughah-e Dehkhoda and Farhangh-e Moein Entries

## Lughah-e Dehkhoda (لغت نامه دهخدا)

**Etymology:** The entry notes the compound origin: "بی + دست + ار = اره، بی اره" (bi + dast + ar = arae, bi arae), meaning "without a saw" per the Farhangh-e Farsi-ye Moein.

**Definition:** An aquatic mammal living in both water and land. Its testicles are called "خایه سگ آبی" (water-dog testicles). In Turkish it's called "قندز" (qandiz). The entry describes hunting practices and notes the medicinal use of its gland secretion for treating phlegmatic and melancholic diseases.

---

## Farhangh-e Moein (فرهنگ معین)

**Etymology tag:** (دَ تَ) (اِمر.) - compound origin indicator

**Definition:** "پستانداری از راستة جوندگان که نسبتاً بزرگ است با وزن بیست کیلوگرم و قد هفتادوپنج سانتیمتر، موهای بدنش زیباست" - a rodent mammal weighing approximately 20 kg, 75 cm tall, with beautiful fur prized for hunting, also called water-dog.
```


### [2026-09-05T17:24:28.021Z] TOOL RESULT

```
Web search results for query: "ریشه‌شناسی بیدستر حسن‌دوست فرهنگ ریشه‌شناختی سگ آبی"

Links: [{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"(PDF) نقد فرهنگ ریشه‌شناختی زبان فارسی [نوشتۀ دکتر محمد حسن‌دوست Review of \"An Etymological Dictionary of the Persian Language,\" by M. Hassandoust]","url":"https://www.academia.edu/24471058/%D9%86%D9%82%D8%AF_%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87_%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C_%D9%86%D9%88%D8%B4%D8%AA%DB%80_%D8%AF%DA%A9%D8%AA%D8%B1_%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86_%D8%AF%D9%88%D8%B3%D8%AA_Review_of_An_Etymological_Dictionary_of_the_Persian_Language_by_M_Hassandoust_"},{"title":"جندبیدستر - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%AC%D9%86%D8%AF%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1/"},{"title":"جندبادستر - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%AC%D9%86%D8%AF%D8%A8%D8%A7%D8%AF%D8%B3%D8%AA%D8%B1"},{"title":"کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) اثر محمد حسن دوست | ایران کتاب","url":"https://www.iranketab.ir/book/40213-farsi-language"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی | راهک","url":"https://raahak.com/?p=942"},{"title":"بیدستر | در فرهنگ لغات ها (دهخدا،معین و ... ) + سایر منابع اطلاعاتی | جدول یاب","url":"https://www.jadvalyab.ir/fa2fa/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1"},{"title":"کتاب فرهنگ ریشه‌شناختی زبان فارسی (جلد 5)","url":"https://fanuus.org/library/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AC%D9%84%D8%AF-5/"},{"title":"کاربرد نام سگ آبی، بیدستر و سمورآبی :: حفاظت حیات وحش و زیستگاه‌های ایران","url":"https://iranwildlife-habitats.blog.ir/1400/03/05/Persian%20name%20of%20Otter%20and%20Beaver"}]

نتایج جستجوی شما به سؤالات مختلفی درباره این موضوعات پاسخ می‌دهد:

## فرهنگ ریشه‌شناختی زبان فارسی

فرهنگ ریشه‌شناختی زبان فارسی یک فرهنگ لغت اختصاصی برای ریشه‌شناسی زبان فارسی تألیف محمد حسن‌دوست است که در سال ۱۳۹۳ در پنج جلد و از سوی انتشارات فرهنگستان زبان و ادب فارسی چاپ و منتشر شده است. این کتاب در سی‌وسومین دورهٔ جایزهٔ کتاب سال جمهوری اسلامی ایران، در گروه «زبان‌های باستانی»، به‌عنوان اثر برگزیده شناخته شد.

متن اصلی فرهنگ ریشه‌شناختی زبان فارسی (آ - ی) در جلدهای اول تا چهارم قرار دارد و مشتمل بر ۲۹۵۵ صفحه و حاوی ۵۵۱۴ مدخل است.

## بیدستر و سگ آبی

بیدستر به بیضة بیدستر اطلاق می‌شود که سابقاً در تداوی ضددردهای عصبی و ناراحتی‌های روحی و ضایعات سیفلیسی و مراض عفونی دیگر به کار می‌رفته است و خایة سگ آبی نیز نامیده می‌شود. سگ آبی حیوانی است که در این متون مذکور است.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T17:24:38.434Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://fa.wikipedia.org/wiki/%D8%AC%D9%86%D8%AF%D8%A8%D8%A7%D8%AF%D8%B3%D8%AA%D8%B1",
 "prompt": "What does this article say about the origin/etymology of the words جندبادستر / بیدستر? Give any Persian, Greek, Arabic or Middle Persian forms mentioned."
}
```


## [2026-09-05T17:24:39.455Z] TOOL CALL #40: WebSearch

```json
{
 "query": "bīdastar Persian beaver etymology \"wud-astar\" OR \"*bidastar\" Middle Persian castoreum"
}
```


### [2026-09-05T17:24:43.644Z] TOOL RESULT

```
# Etymology of جندبادستر/بیدستر

The article provides limited etymological information. It states that **جُندُبادَستَر** is "معربِ **گُندِبیدَستَر**" (an Arabicized form of گُندِبیدَستَر).

The article explains that the Persian word "گند" means "بیضه" (testicle), though it clarifies that the castoreum sacs are not actually related to testicles despite this naming convention.

However, the article does not provide:
- Greek etymologies
- Arabic root forms
- Middle Persian origins
- Any other historical linguistic sources for these terms

The focus is primarily on clarifying what the word literally translates to rather than tracing its linguistic ancestry.
```


### [2026-09-05T17:24:50.049Z] TOOL RESULT

```
Web search results for query: "bīdastar Persian beaver etymology "wud-astar" OR "*bidastar" Middle Persian castoreum"

Links: [{"title":"BEAVER - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/beaver-castor-fiber-l/"},{"title":"Gendebeduster - Simon Online","url":"https://www.simonofgenoa.org/index.php/Gendebeduster"},{"title":"Avestan \"bawra\" = beaver or otter? | WordReference Forums","url":"https://forum.wordreference.com/threads/avestan-bawra-beaver-or-otter.2595261/"},{"title":"بیدستر - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1"},{"title":"Castoreum","url":"https://en.wikipedia.org/wiki/Castoreum"},{"title":"Jund Bedastar (Castoreum): Medicinal Potential of an ...","url":"https://actascientific.com/ASPS/pdf/ASPS-07-0926.pdf"},{"title":"Bidaxsh","url":"https://en.wikipedia.org/wiki/Bidaxsh"},{"title":"Morphology of an Early Oligocene beaver Propalaeocastor irtyshensis and the status of the genus Propalaeocastor","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5436589/"}]

Based on the search results, here is the etymological information about bīdastar and related terms:

## Etymology of bīdastar

The Persian word bīdastar (or bādastar) is composed of bī "without"/bā "with" + dast "hand" + ar "saw," probably referring to the fact that the beaver, without a hand-saw or as if with a hand-saw, is able to "saw," i.e., to gnaw down, some trees with its strong sharp front teeth. However, Bīrūnī offers an alternative explanation: bī "without" + dast [= tāmm] "entire, complete," meaning "incomplete as to its two testicles."

Another source presents a different etymology: Perhaps a compound word from Proto-Indo-European *widʰu- ("tree, beam") and *h₁ed- ("to eat"), literally means a "wood-eater."

## Related terms

The term gund-i bīdastar means "testicles of the beaver," and gundebīdastar refers to beaver's castoreum. In Persian, castoreum is called Gand Bādastar, where Gand means testes, Bād means air and Astar means to cut, i.e., a drug that resolves pneuma from the body.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T17:25:03.666Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/beaver-castor-fiber-l/",
 "prompt": "Quote exactly what the article says about the etymology of the Persian word bīdastar / bādastar and about Avestan bawri-, and any Middle Persian forms."
}
```


## [2026-09-05T17:25:04.926Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BE",
 "prompt": "Give the Sanskrit entry धारा (dhārā): meanings ('edge/blade', 'stream') and the etymology / PIE root(s) given, with cited sources."
}
```


### [2026-09-05T17:25:05.792Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T17:25:12.632Z] TOOL RESULT

```
# Sanskrit धारा (dhārā)

## Meanings

The Sanskrit entry lists two etymologies with distinct meanings:

**Etymology 1** includes: stream, current, flood, gush, jet, drop, shower, rain, torrent, leak, uniformity, custom, usage, continuous line/series, and family line.

**Etymology 2** encompasses: margin, sharp edge, rim, blade (especially of swords/knives), flame of fire, mountain edge, wheel rim, garden fence, army van, ear tip, highest point, summit, glory, excellence, night, and turmeric.

## Etymology and PIE Roots

According to the article, Etymology 1 derives from **Proto-Indo-European *dʰórh₃-eh₂**, stemming from *dʰerh₃- meaning "to leap, spring." The source cites Mayrhofer's *Etymologisches Wörterbuch des Altindoarischen* (1992) and Lubotsky's *The Indo-Aryan Inherited Lexicon* (2011).

An alternative theory by Lubotsky and Mayrhofer traces it to PIE *dʰṇh₂-reh₂*, derived from *dʰenh₂- ("to set in motion, flow"), making it cognate with Sanskrit धन् (dhan, "to move, run").

Etymology 2 is "probably the same as Etymology 1," noting blades may have been traditionally sharpened using streaming water.
```


## [2026-09-05T17:25:25.685Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### MON داوطلب\"; grep -n \"داوطلب\\|داو طلب\" MON_part1.txt MON_part2.txt | head -8; echo \"### MON دموکراسی\"; grep -n \"دموکراسی\\|دمکراسی\" MON_part1.txt MON_part2.txt | head -8; echo \"### MON داو \"; grep -n \"^داو\\| داو \" MON_part1.txt | head -8",
 "description": "Grep Mo'in for dāv, dāvtalab, demokrāsi"
}
```


### [2026-09-05T17:25:25.804Z] TOOL RESULT

```
### MON داوطلب
MON_part2.txt:19604:کاند بدا 8 (.) داو طلب مقامی و 
MON_part2.txt:59797:داوطلبانه برای جهاد با کفار جمع می‌شد ند و 
MON_part1.txt:11266:استاز: 2اه (.) دورة خدمتی که داوطلبان 
MON_part1.txt:13124:(حامص.) نوشتن تن نام داوطلب یا نام خود در 
MON_part1.txt:15767:که داوطلبی بدست می آورد به شرطی که 
MON_part1.txt:15768:زیادتر از آراء داوطلبان دیگر باشد. 
MON_part1.txt:41338:کردن, منقاد شدن. داوطلب گر دیدن. (فّ.) 
MON_part1.txt:50230:سربازان داوطلب تعلیم ندیده» جنکجویانی 
### MON دموکراسی
MON_part1.txt:63014:دموکراسی علاقمند به حکومت ملی. 
MON_part1.txt:63017:دموکراسی: 0۵0027 (امر .) حکومتی 
MON_part1.txt:67222:مسمکلت: رژیم دموکراسی رژیم 
### MON داو 
2265:بار. پایین اطاق» صف نعال» بای ماچان. داو 
51969:داور. 
53927:داور. 
53936:داوری» قضاء. منشور» ابلاغ فرمان. اجازه 
56693:قمار کند. داو و شرط گروبندی در قمار. 
59508:داو: 0 (.) نوت بازی» (شطر نج» برد و 
59512:مراتب اعداد منحصر است تا به نه» پس داو 
59517:داو: ۷ (- دای | (ا.) هر چننه و رده و مر شه
```


## [2026-09-05T17:25:27.539Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### LEW damnum\"; grep -n \"damnum\" LEW_1910.txt | head -5; echo \"### LAT damnum\"; grep -n \"damnum\" LAT.txt | head -5; echo \"### KLN damn\"; grep -n \"damnum, damage\\|F. damner\\|damnum\" KLN_1966.txt | head -6; echo \"### SKT damn\"; grep -n \"^Damn\\|Damn,\" SKT.txt | head -5",
 "description": "Grep Latin/English refs for damnum"
}
```


### [2026-09-05T17:25:27.646Z] TOOL RESULT

```
### LEW damnum
### LAT damnum
15767:damnum, -i n.: doaaage, perte, depense. S'oppose k lucrum, cf.
15768:Pl., Cap.337, ubi... damnum praestet facere quam lucrum, k incrementum;
15773:damnum et dare. L'expression damnum dare n 1 est pas une figura etyao-
15774:logica; le sens est "casser un doaaage" (a'opposant k damnum facere
15775:"faire une depense, une perte", e.g. Pl.Ci.106, Tru.338 ( damnum dare),
### KLN damn
10266:damage,  n.  —  ME.,  fr.  OF.  damage  (F.  dommage), fr.  VL.  *damnaticum,  fr.  L.  damnum,  ‘harm, loss’.  See  damn  and  subst.  suff.  -age.  F.  dom¬ mage  was  prob.  influenced  in  form  by  a  con¬ fusion  with  L.  dominus,  ‘lord,  master’. Derivatives:  damage,  tr.  and  intr.  v.,  damag-er, n.,  damage-able,  adj.,  damage-abl-y,  adv.,  dam- age-able-ness,  n.
10279:damn,  tr.  v.,  to  condemn;  intr.  v.,  to  say  ‘damn’, to  swear.  —  ME.  damnen,  fr.  OF.  damner,  damp- ner  (F.  damner),  fr.  L.  damnare,  ‘to  injure,  cause loss,  condemn’,  fr.  damnum,  ‘harm,  loss’,  which stands  for  *dap-nom  and  orig.  meant  ‘expendi¬ ture’,  and  is  rel.  to  daps,  ‘sacrificial  feast,  ban¬ quet’,  and  cogn.  with  Gk.  Samxvr),  ‘cost,  expen¬ diture’,  Sa7rretv,  ‘to  devour’,  OI.  dapayate,  ‘he shares’,  and  prob.  also  with  Toch.  A  tap-,  ‘to eat’.  All  these  words  prob.  derive  fr.  I.-E.  base *dap-,  a  -^-enlargement  of  I.-E.  base  *da-, *dai-,  *dt-,  *d1-,  ‘to  cut  off,  separate,  divide, distribute’,  whence  OI.  ddti,  dyati,  ‘cuts,  sepa¬ rates,  divides’,  da-yate,  ‘divides’,  Gk.  SoueaDm, ‘to  divide,  distribute;  to  feed  on’,  Salpcov,  ‘god, goddess’,  lit.  ‘divider,  distributor  (of  men’s destinies)’.  See  demon  and  cp.  damage,  condemn, indemnify.  Cp.  also  the  first  element  in  dapifer. Derivatives:  damn,  n.,  damnable  (q.v.),  dam¬ nation  (q.v.),  damnatory  (q.v.),  damn-ed,  adj., damn-er,  n„  damn-ing ,  adj.,  damn-ing-ly,  adv., damn-ing-ness,  n.
10282:damnation,  n.,  condemnation.  —  OF.  (=  F.),  fr. L.  damnationem,  acc.  of  damnatio,  ‘condem¬ nation’,  fr.  damnatus,  pp.  of  damnare.  See  damn and  -ation  and  cp.  condemnation, damnatory,  adj.,  condemnatory.  —  L.  damnato- rius,  fr.  damnatus,  pp.  of  damnare.  See  prec. word  and  adj.  suff.  -ory  and  cp.  condemnatory, damnify,  tr.  v.,  to  cause  damage.  —  OF.  dam- nifier,  fr.  Late  L.  damnificare,  fr.  L.  damnificus, ‘injurious,  hurtful’,  which  is  compounded  of damnum ,  ‘harm,  loss’,  and  -ficare,  fr.  facere,  ‘to make  do’.  See  damn  and  -fy  and  cp.  indemnify. Derivative:  daminific-ation,  n.
10335:Daphnis,  n.,  a  shepherd  in  Sicily,  the  inventor  of pastoral  songs  (Greek  mythol.)  —  L.,  fr.  Gk. Aaipvtg,  which  is  rel.  to  Saqmg,  ‘bayberry’,  fr. Saipvrj,  ‘laurel’.  See  Daphne, dapifer,  n.,  a  servant  waiting  at  table.  —  L.,  ‘a bringer  of  meat’,  compounded  of  daps,  gen. dapis,  ‘sacrificial  feast,  banquet’,  lit.  ‘expense’, and  fero,ferre,  ‘to  bear,  carry’.  The  first  element is  rel.  to  L.  damnum  (for  *dap-nom),  ‘harm, loss’,  orig.  ‘expenditure’,  and  cogn.  with  Gk. Samxvr),  ‘cost,  expenditure’.  See  damn.  For  the second  element  in  dapifer  see  -fer. dapper,  adj.,  neat;  smart.  —  ME.  daper,  ‘agile, strong’,  fr.  MDu.  (=  Du.)  dapper,  ‘strong, valiant,  brave’,  which  is  rel.  to  ON.  dapr,  ‘de¬ jected,  sad’,  Dan.  tapper,  ‘brave’,  OHG.  tapfar, ‘heavy,  weighty’,  MHG.  tapfer,  dapfer,  ‘thick, weighty’.  Late  MHG.  and  G.  tapfer,  ‘brave’,  fr. I.-E.  base  *dheb-,  ‘thick,  heavy,  strong’,  whence also  Toch.  A  tappo,  ‘worth,  force’,  OSlav.  dobru.
19147:indemnification,  n.  —  See  next  word  and  -ation. indemnify,  tr.  v.  —  Formed  with  suff.  -fy  fr.  L. indemnis,  ‘unhurt,  uninjured’,  fr.  in-,  ‘not’,  and damnum,  ‘loss,  injury’.  See  damn.  For  the  change of  Latin  a  (in  damnum)  to  e  (in  in-demnis )  see accent  and  cp.  words  there  referred  to. indemnity,  n.  —  F.  indemnite,  fr.  Late  L.  indem- nitatem,  acc.  of  indemnitas,  ‘security  from damage  or  loss,  indemnity’,  fr.  L.  indemnis.  See prec,  word  and  -ity.
39227:tide,  n.  —  ME.  tid,  tide,  fr.  OE.  tid,  ‘time,  season’, which  is  rei.  to  OS.  tid,  ON.  tid,  Dan.,  Swed., Norw.  tid,  Du.  tijd,  OHG.,  MHG.  zit,  G.  Zeit, ‘time’,  fr.  Teut.  *ti-di-,  prop,  ‘division  of  time’, fr.  base  *ti-,  ‘to  divide;  division;  division  of time’,  whence  also  ON.  ti-mi,  OE.  ti-ma,  ‘time’ ; see  time  and  cp.  ted,  tiding,  tidy.  Teut.  base *ti-  corresponds  to  I.-E.  base  *da-,  *dai-, *di-,  *ds-,  ‘to  cut  off,  separate,  divide,  distribute’, whence  OI.  dati,  dyati,  ‘cuts,  divides’,  dayate, ‘divides’,  ditih,  ‘division’,  Gk.  Satsaffat,  ‘to divide,  distribute;  to  feed  on’;  Safe;,  Saf-nr), ‘meal,  feast,  banquet’,  Sat^eiv,  ‘to  cleave  asun¬ der,  rend,  divide’,  8affi.<ov,  ‘god,  goddess’,  lit. ‘divider,  distributor  (of  men’s  destinies)’,  S^p-oe;, ‘district,  people’,  Arm.  ti,  gen.  tioy,  ‘age,  time’, OIr.  dam,  ‘troop,  company’.  Cp.  I.-E.  *dap-,  a -p-enlargement  of  base  *dd-,  whence  Gk. Sa7tdv7),  ‘expenditure  (esp.  expenditure  arising from  the  entertaining  of  guests)’,  L.  daps,  ‘ex¬ penditure,  sacrificial  feast  banquet’,  damnum (for  *dap-nom),  ‘harm,  loss’,  orig.  ‘expenditure’, Toch.  A  tap-,  ‘to  eat’.  For  the  sense  develop¬ ment  of  OE.  tide,  ‘time;  flood  tide’,  cp.  Du.  tij, ‘flood  tide’,  distinguished  from  tijd,  ‘time’,  and MLG.  getide,  tide,  G.  G ezeiten,  ‘flood  tide’.  Cp. the  first  element  in  Zeitgeist  and  the  second  ele¬ ment  in  yahrzeit.  Cp.  also  dah,  damage,  damn, dan,  dapifer,  deme,  democracy,  demon,  demos, demotic,  endemic,  epidemic.
### SKT damn
```


## [2026-09-05T17:25:37.831Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== 59495-59530\"; sed -n '59495,59530p' MON_part1.txt; echo; echo \"=== 63005,63030\"; sed -n '63005,63030p' MON_part1.txt",
 "description": "Print Mo'in dāv and demokrāsi entries"
}
```


### [2026-09-05T17:25:37.904Z] TOOL RESULT

```
=== 59495-59530
عدد از غله» حب» رورس و 
حبه‌ای که مرغان با منقار خود بررمی‌چینند 

ی 9 ایب 
عدد از هر چیز (واحد شمارش). آبله. گلوله 


بت 
دانه گانه؛ (م-)هطقع-.0 [< دانگانه ] (امر.) 
اسات و متاع دسوی. 
دانی: ]127 [غ.] (افا. ص.) نزدیکك؛ ج. دناه 
(دنات). 
دانی: آمةه [ع.] (افا. ص.) پست؛ فرومایه. 
داو: 0 (.) نوت بازی» (شطر نج» برد و 
مانند آن)» نوبت قمار. نوت تیراندازی. 
زیاده کردن خصل قمار و آن از هفده زیاده 
نمی‌باشند چه ازدیاد آن به جز طاق نیست و 
مراتب اعداد منحصر است تا به نه» پس داو 
اول یکی است و دوم سه و سیم پنج و 
همچنین هفت و نه و بازده تا هفده که مر تبة 
اعداد است؛ می‌رود تا تمام می‌شود» 
دعوی کاری» ادعای امری. 
داو: ۷ (- دای | (ا.) هر چننه و رده و مر شه 
از دیوار گنی که روی هم گذارنده؛ دای. 
داودی: -02714 (ص‌نسب.) منسوب به داود 
نبی: لحن داودی. نوعی زره جنگ. (کیا.) 
گیاهی از تیرهٌ مرکبان جزو دستة آفتابی‌ها 
دارای گسلی درشت و پرپر به رنگ‌های 
سرخء زرد» سفید. این گیاه دارای شاخه‌های 
ستقیم و بلند و برگ‌های مضر س است و 
ار تفاعش به یکث متر می‌رسد. 
داور؛ 02-27 (ص.) آنکه مین مر دم حکم و 
فصل دعوی کند؛ انصاف دهنده» قاضی. 
داور اختصاصی: (حق.) حکم انختعض ان : 
داور مشتر کث: (حف.) مشتر کث. بادشاه 


=== 63005,63030
ریزند» مزبله» خا کروه‌دان ) ج. دمن. 

دم‌و دستگا ۵ 20ع)120-0-025 (اسر.) 
شحو 6 حلال. اساب‌و آلات. 

دمور. تحددل (.) آواز نرم و آهسته. 
دمور؛ تام [ع.] (مسصل.) تساه شدن» 
هلاک گشتن. (امص.) تباهی» هلاکت. 
دمسوکرات: ۱ (ص.) ط فدار 
دموکراسی علاقمند به حکومت ملی. 
دسوکراتیک: 06001621-1 (ص‌نس..) 
طرفدار به دموکرات وابستهبه حکومت ملی. 
دموکراسی: 0۵0027 (امر .) حکومتی 
که در آن قدرت عالیه مشعث از ملت است و 
ملت اعمالش را هدایت می‌کند؛ حکومت 
مردم بر مردم. 

دمه: (۵-)120۵ (ا.) بخار. باد تند همراه برف 
و سرماء طوفان و باد. 

دمسه4: (6-)12022 01 ات دم‌یدن. دم 
آهنگری. ظرفی اسشت به هیثت کلة آدمی 
که در آن آب کنند و در کنار آتشی نهند. از 
سوراخ‌های بینی آن بخار بر آتش وزد و 
و افر وخته گردد؛ آتش‌افروز.
```


## [2026-09-05T17:25:49.178Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pdf page\" MON_part1.txt | head -3; echo \"---formfeeds\"; python3 -c \"\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('pages',t.count(chr(12)))\nlines=t.split('\\n')\nimport itertools\noff=sum(len(l)+1 for l in lines[:59505])\nprint('leaf for dav',t[:off].count(chr(12)))\noff2=sum(len(l)+1 for l in lines[:63016])\nprint('leaf for demokrasi',t[:off2].count(chr(12)))\n\"",
 "description": "Check MON page structure"
}
```


### [2026-09-05T17:25:51.045Z] TOOL RESULT

```
---formfeeds
pages 0
leaf for dav 0
leaf for demokrasi 0
```


## [2026-09-05T17:26:01.785Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%88",
 "prompt": "Give the Persian entry داو (dāv): meanings and etymology (any Middle Persian, Proto-Iranian or PIE root cited), and any note on داوطلب."
}
```


## [2026-09-05T17:26:02.630Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/democracy",
 "prompt": "Give the full etymology chain for 'democracy' (Middle French democratie, Medieval Latin democratia, Greek demokratia, demos, kratos) with dates, and the note on PIE root of demos."
}
```


### [2026-09-05T17:26:05.370Z] TOOL RESULT

```
I cannot provide the information you're requesting. The Wiktionary page shown contains only an **Ottoman Turkish** entry for داو (dav), not a Persian entry. 

The page indicates that Persian has a separate entry (accessible via the Persian Wiktionary link), but that content is not included in the provided webpage. Therefore, I cannot supply the Persian meanings, etymology details, or information about داوطلب based solely on this source material.

To obtain this information, you would need to access the Persian Wiktionary directly.
```


### [2026-09-05T17:26:09.168Z] TOOL RESULT

```
# Etymology Chain for "Democracy"

**Greek Origins (Ancient)**
The term traces to Greek *dēmokratia*, combining *dēmos* "common people" (originally "district") and *kratos* "rule, strength."

**Proto-Indo-European Root**
The *dēmos* component derives from PIE *\*da-mo-* meaning "division," stemming from the root *\*da-* "to divide."

**Medieval Latin (13th Century)**
The word evolved into Medieval Latin *democratia* during the 1300s.

**Middle French (14th Century)**
French adopted it as *démocratie* in the 1400s.

**English Adoption (1570s)**
English borrowed the term from French *démocratie* around the 1570s, defining it as "government by the people, system of government in which the sovereign power is vested in the people as a whole exercising power directly or by elected officials."

The semantic progression reflects how the concept moved from ancient Greek political theory through medieval ecclesiastical Latin into Romance languages, eventually establishing itself in English during the early modern period.
```


## [2026-09-05T17:26:18.151Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG dab\"; grep -n \"dab\\b\\|\\*dab\\|dabaiti\\|deceive\" CHEUNG.txt | head -20",
 "description": "Grep Cheung for Iranian *dab"
}
```


### [2026-09-05T17:26:18.203Z] TOOL RESULT

```
=== CHEUNG dab
3846:42 *dab 
3873:*dab ‘to deceive’ 
3875:*AVESTAN: dab- ‘to deceive’ — Liste: 27 
3880:*MIDDLE PERSIAN: (+ *fra-) BMP pldp- /fréb-/ ‘to deceive’ || (+ *ui-) MMP wyyb-, 
3881:MMP wyd(y)b- ‘to deceive, delude’, MMP wyps- (inch.) ‘to be deceived’, 
3883:deceive, seduce’ > DMMPP: 351a f. 
3890:*PARTHIAN: db ‘trick, deception’ || (+ *ui-) wdyfs- (orig. inch.) ‘to be deceived’ 
3895:*KHOTANESE: (+ *ui-) LKh. bev- ‘to deceive, injure’ = SGS: — 
3904:*CHORESMIAN: (+ *pari-) prößs- ‘to be deceived’, prö’ßy- (caus.) ‘to deceive’ 
3907:*NWIR: (+ *fra-) NP faréftan/faréb- ‘to deceive’ 
3910:ӧым(ы)у-/бомоуа ‘to steal’, also berw-/bowd ‘to deceive’ 
3912:*SANSKRIT: dabh ‘to deceive’ (RV+) = EWAia I: 694 f. 
3914:«PIE *d"eb"- ‘to deceive, harm (someone), belittle, lessen’ > LIV: 132 f. | Pok.: 240 
6095:«PIE *d"reu- ‘to deceive’ = LIV: 156 | Pok.: 277 
6212:*drauj ‘to lie, deceive’ 
6214:*AVESTAN: druj- (druZ-) ‘to lie, deceive’ (on Z- < *ji- see Martínez 1999: 127 f.) || + 
6215:*abi-) ‘to deceive, lie to someone’ || (+ *a-) “id.” > Liste: 32 
6220:*OLD PERSIAN: d(u)ruj- ‘to lie, deceive’ = Kent: 191b 
6229:*MIDDLE PERSIAN: MMP drwz-, ВМР dlwc- /dröz-/ ‘to deceive, break (contract)’ 
6256:*SANSKRIT: drogh ‘to deceive, deceit? (RV+) = EWAia I: 760
```


## [2026-09-05T17:26:19.397Z] TOOL CALL #50: WebSearch

```json
{
 "query": "\"داو\" ریشه‌شناسی واژه فارسی \"داو\" شرط قمار حسن‌دوست اوستایی"
}
```


### [2026-09-05T17:26:26.760Z] TOOL RESULT

```
Web search results for query: ""داو" ریشه‌شناسی واژه فارسی "داو" شرط قمار حسن‌دوست اوستایی"

Links: [{"title":"ریشه‌شناسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C"},{"title":"قمار به انگلیسی - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatoen/%D9%82%D9%85%D8%A7%D8%B1/"},{"title":"گرو - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%DA%AF%D8%B1%D9%88/"},{"title":"جست‌وجوی داو","url":"https://www.vajehyab.com/?q=%D8%AF%D8%A7%D9%88"},{"title":"داو، قمار و زایش سوژه - سوشیانس","url":"https://www.soshians.ir/fa/%D8%AF%D8%A7%D9%88%D8%8C-%D9%82%D9%85%D8%A7%D8%B1-%D9%88-%D8%B2%D8%A7%DB%8C%D8%B4-%D8%B3%D9%88%DA%98%D9%87/"},{"title":"معنی داو - فرهنگ فارسی عمید","url":"https://lamtakam.com/dictionaries/amid/17210/%D8%AF%D8%A7%D9%88"},{"title":"معنی داو زدن - فرهنگ فارسی معین","url":"https://lamtakam.com/dictionaries/moen/13994/%D8%AF%D8%A7%D9%88+%D8%B2%D8%AF%D9%86"}]

I found search results related to the etymology of the Persian word "داو" (dāw) and its connection to gambling. Here's what the search results show:

The word "داو" (dāw) refers to a turn or round in a game, particularly in gambling, and "داو دادن" means to give the opponent the right to go first or to give one's turn in a game or gambling context.

According to Arabic-origin meanings, "داو" can mean deceiving a wolf or trickery, and it can also refer to a fox tricking a gazelle.

However, the search results do not contain specific information about the etymological analysis of the word "داو" as presented by Hassan Doustkhah (حسن‌دوست اوستایی) or a detailed etymological discussion comparing it to other roots. The results show various dictionary definitions and uses of the word, but not the specific etymological source material or scholarly analysis you're looking for.

To find more detailed etymological information from Hassan Doustkhah's work specifically, you might want to search for his published works on Persian etymology or consult specialized Persian linguistic resources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T17:26:41.236Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 108 -l 108 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg108 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 108"
}
```


## [2026-09-05T17:26:42.713Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '15760,15800p' LAT.txt; echo \"=== POK 240 dhebh\"; grep -n \"dhabh-\\|dheb-\\|dhebh\" POK_full.txt | head -10",
 "description": "Ernout-Meillet damnum, Pokorny dhebh"
}
```


### [2026-09-05T17:26:43.470Z] TOOL RESULT

```
total 33028
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 13:26 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb    32690 Sep  5 13:24 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb   169766 Sep  5 10:57 pg104_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22122 Sep  5 10:58 pg104_charlatan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31584 Sep  5 11:00 pg104_tea.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55270 Sep  5 11:01 pg106.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48976 Sep  5 11:01 pg107.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68501 Sep  5 13:26 pg108.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


### [2026-09-05T17:26:43.529Z] TOOL RESULT

```
13; le genre aasc. a entrain£ la cr^ation d'une forae dammus (damus
Not.Tir.108,73, cf. M.L.3466): daia. - Attest 4 depuis Virgile. Soaan.
Passe en gem. : v.h.a.toa, ags.do; le breton dem provient du fr.daim.
Dia.: dammula (Apulae, l.de 1 'figl.) dam(m)ulus.
Un rapport avec domare n'est pas plausible, k cause du sens. Mot
^tranger, peut-etre celtique; cf. irl.da* allaid "cerf" (do* signifiamt
"boeuf").
damnum, -i n.: doaaage, perte, depense. S'oppose k lucrum, cf.
Pl., Cap.337, ubi... damnum praestet facere quam lucrum, k incrementum;
8'allie a sumptus (Ps.Asc.Yerr., p.175), iactura, detrimentum. En droit,
d^signe qnelquefois lea "doaaages et int^rets" paybs pour une perte
aat^rielle (L. des HI tables), et par extension l ,,, aaende" ou la peine.
Quoi qu'on en dise parfois, aucun rapport n'est senti en latin entre
damnum et dare. L'expression damnum dare n 1 est pas une figura etyao-
logica; le sens est "casser un doaaage" (a'opposant k damnum facere
"faire une depense, une perte", e.g. Pl.Ci.106, Tru.338 ( damnum dare),
Ba.1033,784, etc., cf. Thes. V 30,*9sqq, Daas Pl., As.183, neque ille scit
quid det, quid damni faciat, Tru.8i-a, eadem postquam alium repperit
qui plus daret, \ damnosiorem meo exinde immouit loco, 1 1 allit^ration
n'iaplique pas un rapport btynologique. 11 est donc iapossible d'ap-
puyer sur les sens et eaplois attestes a date historique un rapport
entre do et damnum. Attest^ k toutes les 4 poques; surtout au pluriel
chez les pobtes. Bien repr^sente dans les 1 .roaanes, ainsi que damnare,
M.L.S467-8.
D 6 riv 4 s et coapos^s: damnosus: i° qui cause des pertes, couteux; 9° qui
fait des pertes ou des d^penses, prodigue; indemnis: sans doaaage,
indeane (k partir de S6n.); indemnitas (jurisc.); damno,-ds: " damnS
adficere " (Nonius), cf.Pl., Tri.829, nobilest apud homines pauperibus
te (= teptunum) parcere solitum, diuites damnare atque domare-, cf.
aussi 1'expression damnare aliquem uotl (udto ), les fomules d'h6ritage
heres meus damnas esto, legatum per damnationem, et la glose de Non.
«76,18, -are est exheredare. Lucilius Sat. lib. H (as»): ...hunc ful-
lius, inquam, | index heredem facit, et damnati alii omnes. Dans la
1. du droit damnare, usit£ d'abord dans le sens de "frapper d'une
anende", e.g. Cic., Verr.1,38, minoris BS triciens praetorium homine*
non posse damnari, s'est dit ensuite de toute espbce de distinent:
"condaaner" (opp. 1 absoluo), d'oi indemnatus "non condant" (depuis
Pl.), de neae que le coapos^ condemno (cf.condBnS) eri 6 pour aarquer«93
dapsilis
le fait de la condamnbtion (aspect determine). Damnare s'est employe
au sens propre comme au sens figur 4 ; dans la 1 . de 1 'figl. il a servi
=== POK 240 dhebh
```


## [2026-09-05T17:26:49.412Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg108.png"
}
```


### [2026-09-05T17:26:49.759Z] TOOL RESULT

```

```


## [2026-09-05T17:26:49.757Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T17:27:27.700Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### NYB das\"; grep -n \"dās\\b\\|d's\" NYB_vol2_glossary.txt | head -8; echo \"### SKT tide\"; grep -n \"^Tide\\|Tide, s\\|Time, s\\|Demon, s\\|Damn, v\" SKT.txt | head -10; echo \"### SYN sickle\"; grep -n -i \"sickle\" SYN.txt | head -8",
 "description": "Grep Nyberg, Skeat, Buck"
}
```


### [2026-09-05T17:27:27.781Z] TOOL RESULT

```
### NYB das
1515:Frähim Rwānly Zčiš [Paz.] tFrahin Rvänän Zčiš [*pl’hyn' lw’n'n' zwyš] n. pr. the mother of Zartuxst’s mother 371.5, — ‘The wife of Frahim Rwandan’, i.e. of Frähim of the Rwän clan, v. zētš. The perpendicular stroke after -ān- in Paz. Rwäng (confirmed by the now edited MS) is certainly only a reminiscence of the Phl. spelling, which sometimes sepa- rates the ending -än from its noun in this way, and has no significance. The husband's name is given in BdA p. 236}? as Ferahumruvänän, in BdJ 804 as Fra- humrava, both in Paz.
2768:nišēm [nšdm] a bird's nest 2018. — < *atšadman, v. nišastan; Paz. nišim, na- šim ‘a resting-place' (Mx), nišāmī (SGV); NP nišim.
### SKT tide
### SYN sickle
5768:4.207. Several of the words for ‘jaw’ owe this use to some resemblance in shape, as that of a ‘sickle’ to the lower jaw in side view, of a ‘wagon, cart’ to the palate or upper jaw, of a ‘box’ to the
5786:Rum. falcd, fr. *falea for Lat. falz, falcis ‘sickle’ (8.33), hence ‘jaw’ from the similar shape of the lower jaw in side view. REW 3175. Puscariu 575.
5788:NIr. corran ‘sickle’ (8.33) is used for the lower ‘jaw’.
12743:Sp. guadafiar (guadafia ‘sickle’ is a back-formation), as orig. ‘harvest’, fr. a Gme. (Frank., Langob.?) *waidanjan = OHG weidenen ‘hunt, go out in search of food’, weidon ‘pasture, hunt’, ON veida ‘hunt, fish’, etc. REW 9483.
12744:Rum. secera, fr. secere ‘sickle’ (8.33).
12761:_ Sickle’ (the older implement) and scythe’ are sometimes expressed by the “me word, notably Lat. falz, covering sickle’ (falz messoria), ‘scythe’ (fale pe), and also ‘pruning hook’ (Grk. oS ile sickle’ but is also used of the h ca # the Persian chariots). But sh : they are denoted by different 10 distinct formal, though similar : a namely, the notion of ot Cf. Niedermann, Es- Gtk, gen ae asloanneed ee OW serr (but i = at. serra ‘saw’ by - voc. 177, Loth, Mots
12769:8. Skt. la ‘cut’ and ‘mow’ (ef. lavitra- ‘sickle’) : Grk. Atw ‘loose’, ON /é ‘sickle’, etc. Walde-P. 2.407.
12770:Skt. daé- (3 sg. dati, dyatz) ‘cut off, divide’ and ‘mow’ (cf. ddtra- ‘sickle’) : Grk. datoua: ‘divide, share’, etc. Walde- P. 1.763 ff.
```


## [2026-09-05T17:27:29.207Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### WLD Bd1 da-\"; grep -n \"teilen, zerschneiden\\|dā(i)-\\|dāi-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"### POK dhebh 240\"; grep -n \"dhabh-\\|dhebh-\\|dhembh\" POK_01.txt | head -10",
 "description": "Grep Walde-Pokorny and Pokorny dhebh"
}
```


### [2026-09-05T17:27:29.283Z] TOOL RESULT

```
### WLD Bd1 da-
### POK dhebh 240
2564:Aus  dem  Genn.  reiht  man  noch  vieles  an,  was  eine  Bed.-Entw.  von «erteilen^  zu  ,zerreißen,  zupfen,  kurz  betasten,  kurze  täppische  Bewegun- gen machen^  u.  dgl.  voraussetzen  würde;  am  nächsten  der  Bed.  von  öa- naväv  damnum  kommt  aschw.  tappa  und  iapa  ,ein  Ende  machen,  ver- lieren^;  aisl.  tapa  ds.;  afries.  tapia  ,zupfen^,  ags.  tssppe  f.  ,Tuchstreifen^, meno-1.  tappen  (engl,  tap)  ,leicht  schlagen^,  mnd.  tappen,  täpen  (Dehnung in  offener  Silbe?)  ,zupfeu,  pflücken*^;  anord.  tcepr  ,kaum  anrührend^,  isl. i4h)ta  (*täpatjan)  ,eben  anrühren^,  norw.  mdartl.  tcepla  ,leicht  berühren, leise  treten^;  aber  norw.  mdartl.  taap{e)  m.,  dän.  taahe  ,Tor,  Tropf,  täp- pischer Mensch^,  norw.  taapen  ,schwach,  kraftlos,  untauglich^,  tcepe  n. unbedeutendes  Ding^,  anord.  föepiligr  ,knapp^,  mit  anderen  Labialstufen 8chwed.  mdartl.  tahh,  tahhe  ,Tölpel^,  tahhet  ,einfältig^,  sind  wohl  Schall- worte, ebenso  wie  ndd.  tappe,  Schweiz,  täpe,  nhd.  Tappe  ,Pfote^,  sowie iavpen,  täppisch  usw.;  s.  auch  unter  1.  dhabh-.
3326:2»  dhabb-  .passend  fügen,  passend';  dhabh-ro-s  ds.
3404:dhebh-,  dbebh-eu-  ^beschädigen;  verkürzen,  betrügen',  die  nasalierten  Fori (*dhembh-)  sind  als  proportionale  Neubildungen  nach  -^i-haltigen  Wurzel zu  verstehen.
```


## [2026-09-05T17:27:38.232Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:3403])\nleaf=t[:off].count('\\f')\nprint('leaf idx',leaf,'awk NR',leaf+1)\npg=t.split('\\f')[leaf]\nprint(pg[:2500])\nEOF",
 "description": "Print Pokorny dhebh- entry page"
}
```


### [2026-09-05T17:27:39.862Z] TOOL RESULT

```
leaf idx 250 awk NR 251
  sein'.
In  allen  Gliedern  etwas  zweifelhafte  Verbindung.  Über  air.  de'd(a). vgl.  Pedersen  KG.  II  504  f.  (von  einem  Perf.  *dhe-doue  aus  zu  got.  diwans , sterblich'?  s.  dheu-  , hinschwinden',  wo  auch  über  air.  dlth,  arm.  di).  Die germ.  Sippe  endlich  erinnert  z.  T.  an  die  unter  "^dheues-  ,stieben'  bespro- chene von  ndd.  dösig  und  könnte  nicht  bloß  in  der  5-Erw.,  sondern  auch in  der  Bed.  sich  z.  T.  nach  dieser  gerichtet  haben;  immerhin  ist  mit  einer alten  Verwandtschaft  von  anord.  dcesask  usw.  und  ir.  -deda  zu  rechnen.
WP.  I  829,  WH.  I  451.
dheb-  ,dick,  fest,  gedrungen'.
Ahd.  tajpfar  , gravis,  gravidus;  schwer^  gewichtig',  mhd.  tapfer  ,fest, gedrungen,  voll,  gewichtig,  bedeutend',  spät  ,tapfer  (fest  im  Kampfe)', ahd.  tapfare  ,mole',  tapfarl  f.  ,moles',  mnd.  dapper  , schwer,  gewichtig, gewaltig',  ndl.  dapper  , tapfer;  viel',  norw.  daper  ,trächtig',  anord.  dapr ,schwer,  schwermütig,  düster,  traurig'.
Vielleicht  an.  damrarj  nhd.  Damm,  mhd.  tarn  ds.,  got.  faurdamwjan ,verdämmen,  hindern',  als  dhobmö-  hierher?
Aksl.  deheh  ,dick',  russ.  mdartl.  dehelyj  , wohlbeleibt,  stark,  fest',  abl. dohölyj  ,stark,  kräftig'  (usw.,  s.  Berneker  182);  apr.  deblkan  ,groß';  viel- leicht auch  lett.  dabVs  u.  dähls  , üppig',  dahVi  audzis  , üppig  gewachsen', dahVigs  ,üppig'  (Berneker  aaO.;  nach  Mühlenbach-Endzelin  I  428  sind jedoch  die  lett.  Wörter  wahrscheinlich  mit  aksl.  dohrh  zu  verbinden);
toch.  A  tsopats  ,groß',  täppo  ,Mut',  tpär  ,hoch',  B  tappre,  täpr-  ds., Pedersen  Toch.  243,  Toch.  Sprachg.  23,  27,  29,  Van  Windekens  Lex.  135, 148.    Zweifelhaft.
WP.  I  850,  WH.  I  437.
240
dhebh-,  dbebh-eu-  ^beschädigen;  verkürzen,  betrügen',  die  nasalierten  Fori (*dhembh-)  sind  als  proportionale  Neubildungen  nach  -^i-haltigen  Wurzel zu  verstehen.
x-Vi.  dahhnöti , beschädigt,  versehrt,  betrügt,  Pass.  nimmt  Schaden'  (*dhebl n-eu-ti),  Perf.  daddbha  und  (geneuert)  daddmhha,  Partiz.  Perf.  Pass.  dahdl und  (von  der  Wurzelform  auf  -u:)  d-dhlm-ta-  Adj.  ,wunderbar',  eigentli( ,*der    Täuschung    unzugänglich,     unantastbar';     damhhdyati    ,macht   aj schänden'    {damhhd-h    ,Betrug'),    Desid.    dipsati   (=  av.   dhv^-.    s.   unten] dabhrd-  ,wenig,  gering,  dürftig';
av.  dab'  ,betrügen,   um   etwas   bringen' :  davqi-d-yä  G.  Sg.  f.  ,der  b
```


## [2026-09-05T17:27:51.354Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '12665,12690p' BRT.txt; echo \"=== davay ctx\"; sed -n '12825,12835p' BRT.txt",
 "description": "Print Bartholomae dab-/davay- entries"
}
```


### [2026-09-05T17:27:51.414Z] TOOL RESULT

```
'].  da%;  Verbalf.:  s.  'rfä-.
•  j.  daS^na-  Adj.,  PPM.:  s.  Vj-.  [Y. 5.31:  s.  unter  matda-;  —  N._J7;  lies pa^Snl!.]
KompE.
•  g.  daSra-  a.  'Festsetzung':  mlsdsm  (sd.) masdä  yehyä  tU  °%r7m  ".  .  cuius  tu  (es) constitutio    (sva.   constitutor)"  Y.34.  13''.
Zum  V.  da:  —  Vgl.  'rföVa-  und  BtML.  ZDMG. 50.  674  ~  Pü. !  ""E^  . .  ■*'  andar  in  o  öi  i li  dahihet,  Sü.i  yaira  tvadiyiya  diyale.  — ')  Vgl,  iSt  Y.  40.  I  {/radadi%a)  und  43.  5. j.  altm/a  dapasfa  N.  ßJ;  lies  ahmfa  10 pasia.
•  j.  dapta-  Adj.  (fem.  Hä-\  PPfP.:  s.  ".Ai^-.
•  j.,g.'dab-V, 'betrügen'.  Praes.2  dava-^'', lob  dibmav-'^,  iddiivia-^'"^^  24davaya-''>, 26  (Pass.)  iytf(yii-'>,  30  (Iter.)  däbaya-.  —
PPfP.  dapta-^;  PFP.  'daoya-^^;  In£  rfja»-
'betrügen,  hintergehen' :  */atiysi^  . .  ya *mainyate  davayeinti{liSI.)  ^ravanimla haomtmia  A3  yU  dapta  (NS£)''  apanas- yeiti  ". .  die  den  Priester  und  den  Ä  zu betrügen  vermeint,  sie  die  (selber)  betrogen zu  Grunde  gehen  wird"  Y.  ro.  1 5 ;  —  raitts (sd.)  . .  hwahya  xratfus  ySm  naicü  d3ba- ydtx  ".  .  deiner  Weisheit,  die  Niemand betrügen  kann"  Y. 4?-6;  —  hatnyiüa.. davqi%ya  (GSf.)  patqikyä  W.ff.  i8'>;  — 'haoyamna-,  a)    'Jemanden    betrügen,
bringen  um -•  (Gen.) :  lä  dfitnaota {2?VrA.) mastm  AuffSiSi/ (sd.)  Y.j2.  5.
ai.  daihnoä  'er  tauscht,  schädigt'^,  difisah, daihyaH:;  daidhäh;  otsss.  .^a:»» 'stehlen',  PDw. lUt^deiusam  'ich  mache  Profit''(GIrPh.y  b.  321); ann.  [LW.?)9>  dmii  ■hintergehen'.  VgL  noch lÜHBi-  und  Pü,  EU  diavay-.  —  Pü.:  fre/lan;  s. noch  No.  6,  7.  —  «)  iSchr.  s.  S  2&J.  37.  — •)  Ar.  *i^hana%-\  vgl.  Bthl.  IF. /.  78,  wo weitre  Litt.  —  i1  Bthl.  IF.7.  87  No.  und  lu q/7a-.  —  4)  Ohne  Desiderat! vbedentung,  — S)  %S3  n.  1.  — 6)  Pg.:/fl  fl„/r^.  -  7)P6.r hin  . .  ie  pa  freflarlh  fugend.  —  •)  Zum  angebl. ai.  Praes.  a  däbhaü  s.  Bthi_  IF.  7.  83.  — «  Hbm.  AGr.  /.  438.
•  g.  'dab-  V.  (etwa)  'üben'.  Praes.  2  daba-.
•üben,  betätigen':  vaAifia  f/tif  (sd.)  . . sara%uäraAe  .  .  yaicä  (Sp.  S74  m)  ^ dabtn  sask»nlä  dalnayä  var)htyä  uxiä "hanäcs  ". .  (So)  auch  denen,  die  seiner guten  Religion  Worte  und  Werke  üben und  merken"  Y.  _y,  j.
Et.?')  —  PiL:  te  äH  iöini/rt/iSr')--aAnonöf - ätnöxlun  i  den  i  vrh  pa  siu^an  u  hmiht.  — «)  Falsch  KZ.  ja  528,  36.  140;  s.  noch  No.  2.  — )>  Also  tu  ^dab-;  die  an  Pü.  sich  anschliessen- den Oberseliungen  -  zuletzt  von  Dst.  und Mills  -  gehen  keinen  Sinn.
•  j.  davvay-  f.  Name  eines  bestimmten
Gebrechens  (oder  Siechtums):  mä  a%ra  .. daiwii  .  .  mäta.cim  anyqm  daxstanqm  . . anrake  mainySul  V,2,  29,  A)  aüsÖalva pei^onifizirt:  datwis  daivS  y.ig.^y
Et.?  —   Pü.:   frlftär  (daher  D.W.  •trampear';
5.  'doj/ay).
g.  daiiif,  daibis' :  t.  bei  db:
•  j.  dawra'maeSi-  m.  EN.  eines  Gläu- bigen'': °siii/'>  a/aonS  yt  13.122.
Eig.  'feiste,  fette  Schafmültei  besitiend'.  — mp.  diner  (d  p  r^  vgl.  JusTi  NB.  82,  107»), Bd.  34,  3 :  mfl  i  ryäi  i  daair  i  sfil  ert-or  meiäH rat  und  lu  liar?la-.  —  ')  Nach  der  ^'-Dekl.  — •)  ^-j/V  tnnaBd._j/.  7  ist  verkehrte  Umsetiung von  d  p  r . . . ,  d.  L  dmvrgäv.
Uiflitized  by  VjOOQ  IC
68i
da^nya-
dainhusastay-
•  g.  dafänya-  Adj.  'der  betrogen  werden wird,  soll':  onJi'/  a  duivanikaNÄä  *yj hSfOB  "also:  deren  Tim  Übel  ist,  die  sollen (werden)  die  betrogenen  sein"  Y.  5J.  8.
=== davay ctx
689
dava
•  j-  y<^01  «i«  dava  ^itsii  uxriltif  P. 54:  -  ?  -.
•  j.  ", .  yitn  davata  aüi  . ."  FtD.  7. ■  g.  'davant-  Adj.,  PPA.:  s.  ^dav-,
»  j.  'davant-  Adj.  (fem.  'vainil-),  PPA.: s.  ^dab-.
•  j.  davay-  m.  'Betrug'.
KompE.  —  Zum  V.  idai-;  %  36S,  37.  —  mp. vgl  a^auiai;  s.  in  aiauay-.  —  Vgl.  Pö,  in daway-.
•  j.  davayant-  Adj,  (fem,  yäniv-),  PPA,: s,  'dai-.
•  j.  "startvs  vä  puiti  psSti  davaisne  »a" V,  7. 43  PüZ.
•  j.  dava^ah-  Adj,  (?)  —  ?  — :  draxs  hx pairiJvarat  büiü  dalvB  i%yejB  mariaomm •si  V.  Jp,  i;  2.
Gmnz  unklar,  —  Pü. :  fte/tär.
```


## [2026-09-05T17:27:53.119Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\np=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(p))\nfor i,pg in enumerate(p):\n    if 'Sichel' in pg and ('dätram' in pg or 'datram' in pg or 'dāt' in pg):\n        print('leaf',i, pg[:300].replace('\\n',' '))\nEOF",
 "description": "Find Walde-Pokorny dā- root page"
}
```


### [2026-09-05T17:27:54.892Z] TOOL RESULT

```
895
```


## [2026-09-05T17:28:20.124Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\np=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,pg in enumerate(p):\n    if 'Sichel' in pg and 'teilen' in pg:\n        print('leaf',i, repr(pg[:400]))\n        print('---')\nEOF",
 "description": "Search WLD Bd1 for da- root"
}
```


### [2026-09-05T17:28:21.792Z] TOOL RESULT

```
leaf 285 '            :                                                                                              :\n\n\n\n\n                                                 uers-   — nrei-                                     277\n\nurappcn „wickeln" (Pick III 4 4 7, Falk-Torp u. vrpvle: ahd. rein, relo\n                                                  1\n\n\n\n„Schlingfaden, Ranke, Rebe", schwed. reva ..Auslaufer '
---
leaf 771 '                                                  s                   .\n\n\n\n\n                                                  1\n<la-   oder de-           .,fliissig,   flieBen       .\n\n\n\n\n     Ai.       dil-na-    n.    „die    beim Elefanten zur\n                                               Brunstzeit aus den Schlafen\nquellende Fliissigkeit  da-nn- n. f. ,.jede triiufelnde Fliisssigkeit. Tropfen'
---
leaf 820 '                                                ;                       :\n\n\n\n\n812                                                              del-\n\n\n\n  alb. daloj         :\n                         ,ich scheide, teile"             (Jokl SBWienerAk. 168, I 12).\n  Erweiterung * del-gh -                            ,\n                                                         *dl-egh-\n  Air. dlongid    '
---
```


## [2026-09-05T17:28:27.738Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\np=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (771,772,773):\n    print('='*20,'leaf',i)\n    print(p[i][:2600])\nEOF",
 "description": "Print Walde-Pokorny I 763ff"
}
```


### [2026-09-05T17:28:29.344Z] TOOL RESULT

```
==================== leaf 771
                                                  s                   .




                                                  1
<la-   oder de-           .,fliissig,   flieBen       .




     Ai.       dil-na-    n.    „die    beim Elefanten zur
                                               Brunstzeit aus den Schlafen
quellende Fliissigkeit  da-nn- n. f. ,.jede triiufelnde Fliisssigkeit. Tropfen,
Tau", av. da-nu- f. ,,FluB, Strom", osset. don „Wasser, FluB"; mit For-
mans -mo- arm. tamuk „feucht, benetzt", tamkanam „vygcdvco, madefio'- und
vermutlich gr. drjjuog (urgr. d oder >j ?) .,Fett, Schmer von Tieren und
Menschen", womit alb. Sjame „Fett, Speck, Talg" in noch nicht geklarter
Weise zusammenhangt; das Fett kann als das beim Braten fliissig werdende
benannt sein (vgl. aksl. loj „adeps" lijnti ,,gieBen •). Hierher auch kelt.
                                                              :




Ddnuvius „Donau“. Liden Arm. St. 73 f. m. Lit. M. Forster ZfslavPh. I ff.                  1




da[i]-     :   dl-   und da- „teilen, zerscbneiden, zerreiBen'
   Ai. duti, dijati , schneidet ab, maht, trennt, teilt c , ptc. dina- (s. u. ddvog),
ditd- (s. u. ddarog). zsges. avn-ttns ,,abgesehnitten", diti-li „das Verteilen",
danam „das Abschneiden", dunam „Verteilung, Teil", data n. „Teil“, datdr-
„Schnitter“, datrdm „zugeteiltes“,                    dot ram n. ,,Sichel“, np. dura „Gehalt",
das „Sichel"          ;
                          ai.   day ate ( *doi-etai) „teilt, nimmt Anteil, hat Mitgefiihl; zer-
stort",        dayu ,,Teilnahme, Mitgefiihl'-;
     gr. daiofxai  med. ,,teile, verteile" (fjxog datexai Horn, a 48 „ist zerrissen,
schneidet mir ins        Herz" oder hat Anteilnahme"?) mit wohl nach fut.
                                                          ,


datoco und den folgenden Worten bewahrtem < (lautgesetzlich datjxai Konj.
    375 „wird zerstort", Schulze KZ. 29, 258, der aber unberechtigt zwei
verschiedene Wz. in den Bed. „teilen" und „zerstiickeln" annimmt), dot's,
-ro?, dairy, daixvg, -vog „Portion, Mahl, Opfer" (: ai. data; dairy jucbv „Gast“
als „dem Mahle beiwohnend"), dairgog „Zerleger“ (: ai. datar-), daixgov
,,Portion" (: ai. datrdm; das ai dieser gr. Worte ist nach dalo/uai, dalvvfu
an Stelle von a oder a getreten, wie im kret. Pf. dsdaio/uai zu dnxsofxai                      ,

s. u., vgl. auch kret. daToig „Teilung“, Kagnodaiaxal „Yerteiler von Friich-

ten"), daivv/M „bewirte“, wohl auch datjuxov              ,Gott, Gottin; Geschick"
(eigentlich „zuteilend; zugeteiltes; andere Deutungen verz. Boisacq 162,
1104; die Mikkolas WuS.
==================== leaf 772
764                                                     da[i]-       :   di-, da-



teilend“         hierher,    gegen Fick II 4 141), wovon bave[*a]iov ,.Darlehen“, ba-
vuQm Jeihe Geld auf Zinsen". —                                           Curtius 5 230.                  Mit der Tiefstufe *di-
der Wzf. *dai- reiht sich an anord. ti-na „zerpflucken, einzeln herausnehmen,
die Einzelheiten einer Sache darstellen, ausscheiden, reinigen"; arm. ti,
gen. tioy „Alter, Jahre, Tage, Zeit“ (*di-t oder *dl-te -, -to-, -tn- „Zeit-
abschnitt" (Liden Arm. St. 91 f.) ahd. sit                                           f.   (n.)    „Zeit, Zeitalter, Jahreszeit,
                                   1
Festzeit; Tag, Stunde ', as. tid , pi. tidi                                      f.,-     ags. tld       f.,   anord. lid   f.,       pi. -ir
„Zeit,     richtiger           Stunde“ (Fick I 4 450, Persson Wzerw. 115,
                            Zeitpunkt,
KZ. 33, 287. Liden aaO.; nach letzterem ursprgl. Rons. St. *ti-p- *tt-3A;                                                         :



ahd. std n. Isidor alter pi. *tJ-p-is wie der ursprgl. Rons. St. buoh auch als
                                                            ,

n. erscheint), s. weiteres Zubehor (z. B. anord. tidr „iiblich, haufig“, ags.
iulan ,,vorfallen‘', anord. tlSa „trachten, streben", mnd. tiden ds.) bei Fick
III 4 160,        Falk-Torp       mit Formans -men- anord. tlmi, ags. tima,
                                   u. tid, tidt;
engl.     time ,,Zeit“,        nbd. alemann. zJme
                                          „Gelegenheit, Zeit“ (Fick, Pers-
son, Liden aaO.; gegen Rluges ZfdtWtf. 8,145 Yerbindung mit lat. dies
s. Vf. LEWb.
             2
               u. dips und dies; eine Wz. *dei- „sich ausdehnen, erstrecken"
hatte keinen anderweitigen Anhalt, s. u. *del- „es worauf abgesehn haben“\
wozu wieder anord. lima „widerfahren“, ags. getlmian „vorfallen, geschehn“.
  Mit Formans -mo-: gr. brjpog, dor. bapos „(Volksabteilung) Yolk, Ge-
biet; in Athen der einzelne Gau“ (Mangold CSt. 6, 403 IF., Persson RZ.
          air. dam ,.Gefolgschaft, Schar nir. ddmh „atribe, family, kindred,
                                                                            11
33, 287      ,                                                                   ,


relationship", acymr. dauu „cliens“, ncymr. daw, dawf „Schwiegersohn“
(Fick I 4 451, II 4 142, Pedersen                           RG. I 48).
      Mit Formans -lo- vielleicht aksl. dch „Teil“                                               (s.   u. *del- „spalt
==================== leaf 773
                                    da[i]-   :   di-,       de-                                                    765

Curtius 5 232 f, Fick I 4 64, 450    (Nicht iiberzeugend iiber die gr. und                                         lat.
Worfce Reichelt KZ. 46, 343.).
  Als „opferbares Tier 0       reiht man (ygl. auBer Curtius bes. J. Schmidt
PI. 199)    gewohnlich an die auf idg. *dtp-ro- weisende ahd. zebar „Opfer-
                                     0
tier°, got. tibr ^debgov, Opfergabe (Besserung aus iiberliefertem aibr, s. Liden
Arm. Stud. 8; anders Streitberg Got. Elem. 6 253; von Wood MLN. 21, 39nicht
iiberzeugend mit ai. iblxya- „reich° verglichen), ags. tlfer, fiber „Opfertier,
Opfer“, spatmhd. ungezibere, unzfver nhd. TJngeziefer, eigentlich „unreines,
                                             ,

nicht zum Opfern geeignetes Tier 0 (zu den Belegen fiir 7 s. J. Schmidt
und Liden m. Lit.); da eine Wzf. *deip- oder *deip-, die mit dem Yokalis-
mus von da[i\, dap- nicht leicht vereinbar ware, an gr. deinvov „Mahl“
(das von andern, ebenfalls ganz unsicher. mit got. teua „Ordnung° ver-
glichen wird) nur eine fragliche Stiitze findet, waren diese germ. Worte
eher als Tiefstufe dip- zu *da\i]p aufzufassen. Doch trennt sie Liden aaO.
wegen des auf dippa zuriickfiihrbaren arm. tvar „Schafbock, Schafherde,
auch Kalb, Stier, Ochs, Farse, Herde von GroBvieh 0 beachtenswert als
selbstandige Sippe der Bed. „Yieh, Opfertier“ ab.
   Aus dem Germ, reihen Fick III 4 155 (1. tab), 164 {tippa), 168 ( tuppa),
Falk-Torp u. taabe, tabe, tap, ttfve, tip, top noch vieles an, was eine Bed.-
Entw. von „zerteilen“ zu „zerreifien, zupfen, kurz betasten, kurze tappische
Bewegungen machen“ u. dgl. voraussetzen wurde; am nachsten der Bed.
von danavav damnum kommt aschw. tappa und tapa (p vielleicht Ver-
              ,


mittlung von t und pp aus                  „ein Ende machen, verlieren w aisl.                                 ,

tapa ds.; afries. tapia „zupfen“, mengl. tappen (engl. tap ) „leicht schlagen“.
mnd. tappen, tapen (idg. C oder Dehnung in offerer Silbe?) „zupfen, pflucken“.
nd. tappe „Pfote u  ;
                         anord. tapr „kaum anriihrend                         11
                                                            isl. tcepta (*tapatjan),

„eben anriihren“, norw. mdartl. tcepta „leicht beriihren, leise treten",
tcepla „tappend beriihren 0   ;
                                   norw. mdartl. taap(e ) m., dan. taabe „Tor,
Tropf, tappischer Mensch 0 norw. taapen „schwach, kraftlos, untauglich 0
                              ,
```


## [2026-09-05T17:28:43.717Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg108.png data/verification/sources/refs/ocr/BOOK/108.png; ls -la data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page image to audit dir"
}
```


### [2026-09-05T17:28:45.342Z] TOOL RESULT

```
total 3052
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 13:28 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-05T17:28:52.369Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%B3' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1' \\\n 'https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1/' \\\n 'https://www.etymonline.com/word/democracy' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BE' \\\n 'https://www.iranicaonline.org/articles/beaver-castor-fiber-l/' ; do\n echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 108, root Da 1: das/bidastar/dahreh/demos/dav verification' 2>&1 | tail -3; done",
 "description": "Archive web sources",
 "timeout": 600000
}
```


### [2026-09-05T17:28:59.950Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%B3
/home/sfmqrb/git/rishe/data/verification/sources/web/b0d1e89d8f080549.txt
### https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/f287e6eab01e8406.txt
### https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1/
/home/sfmqrb/git/rishe/data/verification/sources/web/bcecc17eaa4b1885.txt
### https://www.etymonline.com/word/democracy
/home/sfmqrb/git/rishe/data/verification/sources/web/ff55c7ac46891403.txt
### https://en.wiktionary.org/wiki/%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BE
/home/sfmqrb/git/rishe/data/verification/sources/web/651164bf608d9841.txt
### https://www.iranicaonline.org/articles/beaver-castor-fiber-l/
/home/sfmqrb/git/rishe/data/verification/sources/web/f8da4bf6b856d076.txt
```


## [2026-09-05T17:29:03.546Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; wc -c f8da4bf6b856d076.txt; grep -n -i \"bīdastar\\|bidastar\\|without\\|saw\\|bawri\" f8da4bf6b856d076.txt | head -20",
 "description": "Check archived Iranica beaver text"
}
```


### [2026-09-05T17:29:03.602Z] TOOL RESULT

```
23429 f8da4bf6b856d076.txt
59: The beaver in Islamic Iran . The existence of several Persian or dialectal Iranian names (all obsolete now) for the beaver and especially for its “testicles” (see on castoreum below) in Persian sources of the Islamic period indicates a continued interest in the beaver, no longer for its pelt (considered “unclean” in the Islamic law like the skin of any other dog), but for the medicinal properties of its gond/jond “testicle” (i.e., castoreum), which were made known to the physicians-pharmacologists of the Islamic period through the Arabic translation of Dioscorides’ treatise on materia medica by Ḥonayn b. Esḥāq and Stephanos (Eṣṭefān b. Basīl) under the caliph al-Motawakkel (232-47/847-61). The earliest mention of the beaver in Islamic Iranian lands is probably that by the 4th/10th-century historian and philologist Ḥamza Eṣfahānī (quoted by Bīrūnī, Ṣaydana , ed. Said, p. 142): “ Vīdastar [i.e., the beaver] is an animal found only in the valley of the Aras [River] in Azarbaijan and in the valley of Atil, the Khazar capital.” For the animal we also find the following names, all mentioned, or quoted from earlier authors, by Bīrūnī, op. cit., pp. 141-42; saglāb(ī)/saklābī/saglāv(ī) (corruptions of sag-e ābī , qondoz/qondos (according to Shirr, p. 129, an arabicized form of gond-e sag , lit. “dog testicle”; cf. the turkicized qondūz , still used in Turkish for this animal); hazad(ū) , and ḵazadū (the last one probably a variant or alteration of hazadū in the Persian adaptation of Bīrūnī’s Ṣaydana by Kāsānī, I, pp. 218-20). By far the commonest name for the beaver in Persian and (with arabicized variants) in Arabic sources is bīdastar or bādastar , which, according to Moʿīn ( Farhang-e fārsī , s.v.), is composed of bī “without” /bā “with” + dast “hand” + ar “saw,” prob­ably referring to the fact that the beaver, without a hand-saw or as if with a hand-saw, is able to “saw,” i.e., to gnaw down, some trees with its strong sharp front teeth (but cf. Bīrūnī’s explanation, p. 141: bī “without” + dast [ = tāmm ] “entire, complete,” “that is, incom­plete as to its two testicles”).
60: More numerous are the names for the beaver’s “testicle(s).” This animal being unknown in Arabic-speaking lands (see Maʿlūf, pp. 31-32), the authors of the Islamic period took for granted Dioscorides’ inaccu­rate description of the kástor (Gk., beaver), and his misinterpretation that castoreum or castor (variously arabicized as qasṭorīūn , qasṭūrīūn , qasṭūr , etc.) is the testicle [sing.: sic ] of the beaver (see below; in Ar.: ḵoṣyat al-kalb al-baḥrīy “testicle of the marine dog,” ḵoṣā kalb al-māʾ “testicle of the water dog,” etc.). The Persian gond-e bīdastar/bādastar , hazad-gond , qondoz-qūrī , etc., and the Turkish qūndūz ḵāya-sī (all recorded as such by Bīrūnī, loc. cit.) reflect the same original description by Dioscorides (as quoted by Ebn al-Bayṭār, pt. 1, pp. 171-­72): “The qāsṭor is an animal adapted to living both in water and out of it but mostly living in water, where he feeds on fish and crabs. His testicle is the jond-bādastar . This animal is fit to live both on land and in the sea, [but] he is usually in streams with snakes and crocodiles. . . . False is the report that this animal, when chased and wanted, extracts his testicle and throws it [to the hunters], for it is impossible for him to reach it, because it is stuck like a pig’s testicle. [To do this,] he should rend the skin covering the testicle and take this out with the ḥejāb (envelope) containing a honey-like moist matter, which is [then] dried, and taken internally” (it should be noted that the misinformation that the beaver “is usually in streams with snakes and crocodiles” does not occur in the translation of Dioscorides by Ḥonayn and Stephanos and later revised by Abū ʿAbd-Allāh Nātelī in 380/990-91; see the relevant fol. of the Leiden ms. of this revised translation as reproduced by Sadek, p. 184). Unrelated names for castoreum are: āš-e baččagān/baččahā (cf. its Turk. tr. oḡlān-āšī ) of dubious literal meaning (“the children’s āš ”? cf. the unconvinc­ing etymology proposed by Pūr-e Dāvūd, quoted by Moʿīn in Borhān-e qāṭeʿ I, p. 44, n. 6: āš “many” + baččagān “children,” lit. “[having/bearing] many pups”), mentioned by Bīrūnī, loc. cit.; fāješa ( sic ; given by Bīrūnī, and recorded in Borhān-e qāṭeʿ s.v., as Persian, but cf. the Arabic al-fāḥeša mentioned by Ebn Maymūn, no. 79, along with ḵoṣyat al-baḥr , lit. “sea testicle,” and ḵoṣā al-sammūr , lit. “testicle of the sable,” etc., as synonyms for jondabādostor [ sic ]); and ḵazmīān (recorded by Bīrūnī and in Borhān-e qāṭeʿ , s.v.; origin uncertain; for a probable connection with ḵaz “weasel”? see the sam(m)ūr below). Another Persian name for castoreum, sag(-e) āb , lit. “water dog,” also in Bīrūnī, recalls the confused use of one and the same word for this animal and its “testicle,” as is the case for the Engl. castor meaning both (cf. also Ebn al-Bayṭār, pt. 4, p. 21, who uses qasṭūra as a synonym for jondabādastar ).
61: Actually, castoreum is a musk-like strong-smelling resinous matter secreted by a pair of bulky glandular pouches united by a common excretory duct and located side by side under the abdominal skin in the urogenital region of both male and female beavers (it probably serves to delimit the beaver’s territory and/or to attract the opposite sex). The fact that she-beavers also possess these musk glands (though less developed than in males) must have passed unnoticed by classical authors and their Islamic imitators—hence the confu­sion of these pouches with he-beavers’ testicles (to be noted incidentally that the word musk , designating a substance similar to castoreum and secreted by an abdominal pouch in the male musk deer, goes back—through the Persian mošk —ultimately to the Skt. muṣká meaning “testicle, scrotum”). These glands were mistaken for testicles because, in addition to their outward resemblance to the latter, they were often sold in pairs (Meyerhof, in Ebn Maymūn, p. 42). Apparently because of the scarcity of genuine castoreum, it was often adulterated (according to Dioscorides, with some gum ammoniac and another resin mixed with blood and a little castoreum, all placed in single bladders and let to dry up); therefore, it was recommended to eventual users to “select always those twin [“testicles”] which have a common [excretory] outleṭ . . . and the inside of which is divided into numerous natural fossae ( ḥojob ) contain­ing [a matter] like blood, malodorous, hot, pungent, and easily detachable [from the inner walls of the pouches]” (Dioscorides, loc. cit., condensed by Bīrūnī, loc. cit., Ebn Sīnā, II, Pers. tr., p. 106, etc.; cf. Anṭākī, I, p. 95, who states that “the best jondabīdastar is the red, sweet-­smelling [ sic ], friable one, not older than three years”).
62: Probably because of the nonexistence of the beaver in the greater part of the Islamic world, confusion has also developed about the very animal yielding castoreum. The confusion seems to have been first with a certain fur-bearer of the family Mustelidae: sammūr in some Arabic texts, and ḵaz(z) in some Iranian sources. For instance, Ebn Beklāreš (2nd half of the 5th/11th century), quoted by Renaud and Colin (p. 48, no. 103), while giving the synonym ḵoṣyat al-baḥr for jondobādas­tar [ sic ], states that “it comes from the animal called sammūr ; and Ebn Maymūn (6th/12th century), loc. cit., believing that “ jondabādostor is the testicle of the sammūr ,” explains that the latter “is a sea animal, the “water dog,” which comes out [of water] and feeds/roams freely on land.” Bīrūnī (d. 440/1048) reports ( al-­Jamāher , p. 102) some people’s belief that “the hunters of ḵazz castrate it and [that] its testicle is [called] jondbīdastar .” Esmāʿīl Jorjānī (6th/12th century) states (p. 603) that “ jond-e bīdastar is the testicle of the animal called ḵaz in Persian and qondos by Turks.” Kāsānī (1st half of the 8th/14th century), loc. cit., quotes “some people” as saying that “the jond-e bīdastar is the testicle of the animal from the hair of which ḵaz clothes are woven [ sic ]” (cf. also ḵazmīān “castoreum” above). As an animal unanimously acknowledged as bearing a valuable fur, the sammūr (Pers. samūr , Pahl. samōr ) has been generally identified by modern authors as Mustela/Martes zibellina , the sable (see, e.g., Schlimmer, p. 393, Maʿlūf, p. 213, and Ghaleb, s.v., who, however, has “common sammūr ” = ḵazz = Mustela martes and reserves M. zibellina for the “ sammūr of Siberia”), and the ḵaz(z) variously as Martes martes , pine marten, Mustela martes , “common marten,” or M. foina , weasel (see the same sources, and Dāʾerat al-maʿāref-e fārsī I, Tehran, 1345 Š./1966-67, s.v.; for the great confusion in the identification of the sam(m)ūr , ḵaz(z) and the like in Arabic and Persian sources, see Maʿlūf, pp. 158-60 and 213).
84: M. Golzārī, Safar-nāma-ye Melgūnof be sawāḥel-e janūbī-e Daryā-ye Ḵazar (1858, 1860) , Tehran, 1364 Š./1985.
```


## [2026-09-05T17:29:38.593Z] AGENT

Now I have everything I need. Let me write the verification file.


## [2026-09-05T17:37:01.998Z] TOOL CALL #64: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk108.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 108,\n \"book_page\": 78,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [{\n   \"entry\": 0,\n   \"root\": \"Dâ 1, Dâi, Di\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *deh\\u0324\\u2082(y)- / trad. *dā-, *dāi-, *dī- 'to divide, cut up, apportion'\",\n   \"note\": (\"Pokorny p.175 heads the entry 'dā : dǝ- und dāi- : dǝi- : dī- \\u201eteilen, zerschneiden, zerreißen\\u201c', \"\n     \"with the nominal derivatives dā-mo-s 'Volksabteilung', dā-ter- 'Zerleger', dā-tro-m 'Zugeteiltes', dǝi-lo- 'Teil', \"\n     \"di-t- 'Zeitabschnitt' \\u2014 exactly the set of meanings and formations the chart draws. Walde-Pokorny I 763-765 and \"\n     \"Watkins/AHD ('dā-. To divide. Contracted from *daə-. Variant *dai- ... [Pok. dā- 175]') give the same root. \"\n     \"The language label ('Indo-European') and the gloss 'to divide, cut in pieces' are correct; today the root is written \"\n     \"*deh\\u2082(y)- (laryngeal notation), and the p-extension *dap- and the t-extension *dā-t- are treated as branches of it. \"\n     \"Nourai's numbering 'Dâ 1' distinguishes it from his 'Dâ 2' (*deh\\u2083- 'to give'), which is the correct modern separation too. \"\n     \"The one real problem on the page is the sub-root box #12 (see there): it merges PIE *dap- 'apportion' (which does belong here) \"\n     \"with *dʰebʰ- 'harm, deceive' (Pokorny 240), a different root.\"),\n   \"note_fa\": (\"ریشهٔ «Dâ 1, Dâi, Di» همان ریشهٔ هندواروپایی آغازین *deh\\u2082(y)- (به نگارش سنتی *dā-/*dāi-/*dī-) به معنای «بخش کردن، بریدن، پاره کردن» است. \"\n     \"پوکورنی در صفحهٔ ۱۷۵ فرهنگ ریشه‌شناختی هندواروپایی خود همین ریشه را با همین معنا آورده و ساخت‌های اسمی آن را dā-mo- «بخشی از مردم»، \"\n     \"dā-tro- «سهمِ داده‌شده» و di-t- «برشِ زمان» می‌داند؛ والده\\u2013پوکورنی (جلد ۱، ص ۷۶۳ به بعد) و واتکینز (پیوست ریشه‌های هندواروپایی فرهنگ امریکن هریتیج) نیز همین را می‌گویند. \"\n     \"پس نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است. تنها اشکال صفحه در جعبهٔ فرعی شمارهٔ ۱۲ است که ریشهٔ *dap- «سهم دادن» را با ریشهٔ جداگانهٔ *dʰebʰ- «آسیب زدن، فریفتن» (پوکورنی ۲۴۰) یکی گرفته است.\"),\n   \"sources\": [W + \"Reconstruction:Proto-Indo-European/deh%E2%82%82y-\"],\n   \"ref_check\": [{\"ref\": \"POK:175\", \"status\": \"supports\",\n     \"note\": (\"Pokorny IEW p.175 (local POK_01.txt, awk 'BEGIN{RS=\\\"\\\\f\\\"} NR==186'): 'da : dg- und däi- : dgi : di- ,teilen, zerschneiden, zerreißen', \"\n       \"ursprgl. athemat. Wurzelpräsens; Nominalbildungen dä-mo-s f. ,Volksabteilung', dä-ter- ,Zerleger', dä-tro-m ,Zugeteiltes', dä-tu- ,Teil', \"\n       \"ddi-lo- ,Teil-', di-t- ,Zeitabschnitt'.' Root, language and gloss are exactly Nourai's.\")}],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I 763-765 (WLD_Bd1_pages.txt leaf 771-773)\", \"stance\": \"supports\",\n      \"note\": \"'da[i]- : di- und da- \\u201eteilen, zerschneiden, zerreißen\\u201c ... Ai. dāti, dyati ,schneidet ab, mäht, trennt, teilt\\u2019 ... dātram n. \\u201eSichel\\u201c, np. dāra \\u201eGehalt\\u201c, dās \\u201eSichel\\u201c' \\u2014 the very source Pokorny abridged, and it already lists NPers. dās under the root.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. dā- (AHD_watkins1985.txt line 355)\", \"stance\": \"supports\",\n      \"note\": \"'dā-. To divide. Contracted from *daə-. Variant *dai- from extended root *daəi-. 1. Root form *dai- in Greek daiesthai, to divide ... 4. Suffixed form *dā-mo-, perhaps \\u201cdivision of society,\\u201d in Greek dēmos ... 5. Suffixed form *dai-mon-, divider, provider, in Greek daimōn, divinity: DEMON. [Pok. dā- 175.]'\"},\n     {\"src\": \"KLN\", \"where\": \"s.v. tide (KLN_1966.txt line 39227)\", \"stance\": \"supports\",\n      \"note\": \"'Teut. base *ti- corresponds to I.-E. base *dā-, *dai-, *dī-, *də-, \\u2018to cut off, separate, divide, distribute\\u2019 ... Cp. I.-E. *dap-, a -p-enlargement of base *dā-'; Klein cross-refers exactly the same set: dah, damage, damn, dapifer, deme, democracy, demon, demos, endemic, epidemic.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck 8.33 'sickle' (SYN.txt line 12770)\", \"stance\": \"supports\",\n      \"note\": \"'Skt. dā- (3 sg. dāti, dyati) \\u2018cut off, divide\\u2019 and \\u2018mow\\u2019 (cf. dātra- \\u2018sickle\\u2019) : Grk. δαίομαι \\u2018divide, share\\u2019, etc. Walde-P. 1.763 ff.'\"}\n   ],\n   \"nodes\": []\n }]\n}\n\nN = doc[\"entries\"][0][\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"dâtra; dhâra\", \"verdict\": \"disputed\",\n \"derivation\": (\"dātra: correct. Skt. dā́tra- n. 'sickle' is a tool-noun in -tra- built on the root dā- / dyáti 'cuts off, mows, divides' \"\n   \"(*deh\\u2082-tro-m 'the cutting instrument'), and Pokorny prints it under this very root ('dātram n. \\u201eSichel\\u201c'), as do Walde-Pokorny I 763 and Buck 8.33. \"\n   \"The Greek exact match is δαιτρόν 'portion' (same *-tro- formation from the same root), which shows the suffix is inherited, not Indic. \"\n   \"dhāra: not correct here. Skt. dhā́rā 'edge, blade (of a sword), rim' begins with the voiced aspirate dʰ-, which cannot continue PIE *d- of *deh\\u2082(y)-; \"\n   \"Mayrhofer (EWAia) and Lubotsky derive dhā́rā either from *dʰórh\\u2083-eh\\u2082 (root *dʰerh\\u2083- 'to leap, spring') or from *dʰn\\u0325h\\u2082-reh\\u2082 (*dʰenh\\u2082- 'to set in motion, flow'), \"\n   \"i.e. the same word as dhā́rā 'stream' \\u2014 blades being sharpened in a stream of water. Nourai took dhāra from Mo\\u2018in's footnote to Borhān-e Qāte\\u2018 p.904 \"\n   \"(where it is offered as the source of Persian dahre, node #4), and then wrongly re-attached it to the *dā- root because both mean 'cutting edge'.\"),\n \"derivation_fa\": (\"سانسکریت dātra- «داس» درست است: این واژه اسم ابزار با پسوند -tra- از ستاک dā-/dyáti «بریدن، درو کردن، بخش کردن» است \"\n   \"(هندواروپایی *deh\\u2082-tro-m)، و پوکورنی خودِ آن را ذیل همین ریشه آورده است؛ همتای دقیق یونانی‌اش δαιτρόν «سهم» است. \"\n   \"اما dhārā «تیغهٔ شمشیر، لبه» به این ریشه ربطی ندارد: واکِ آغازینِ آن dʰ (بای دمیده) است و از *d هندواروپایی برنمی‌آید. \"\n   \"مایرهوفر و لوبوتسکی آن را از *dʰerh\\u2083- «جهیدن» یا *dʰenh\\u2082- «روان شدن» می‌دانند، یعنی همان dhārā به معنی «جویبار» \"\n   \"(تیغه را در آبِ روان تیز می‌کردند). نورایی این واژه را از حاشیهٔ معین بر برهان قاطع (ص ۹۰۴، ذیل «دهره») برداشته و به‌اشتباه زیر ریشهٔ Dâ نشانده است. \"\n   \"نتیجه: بخش نخستِ گره درست و بخش دومِ آن را پژوهش امروزی رد می‌کند.\"),\n \"sources\": [W + \"%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BE\", W + \"%D8%AF%D8%A7%D8%B3\"],\n \"ref_check\": [\n   {\"ref\": \"POK:175\", \"status\": \"partial\",\n    \"note\": \"POK_01 leaf 186 (p.175) has 'dātram n. \\u201eSichel\\u201c' under dā- \\u2014 supports dātra. It has no dhāra: what it prints next is 'npers. dāra \\u201eGehalt\\u201c' (salary), a different word; Pokorny nowhere puts Skt. dhā́rā here.\"},\n   {\"ref\": \"BQT:904\", \"status\": \"partial\",\n    \"note\": \"Borhān-e Qāte\\u2018 vol.2 leaf 364 = printed p.904 (fixed by its own catchline 'بقیه در صفحهٔ ۹۰۵'); the headword there is «دهره» and Mo\\u2018in's footnote 9 reads 'سانسکرت dhārā'. So BQT:904 does give Skt. dhārā, but as the etymon of Persian dahre, not as a member of the *dā- 'divide' family.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 763 (leaf 771)\", \"stance\": \"partial\",\n    \"note\": \"'dātram n. \\u201eSichel\\u201c, np. dāra \\u201eGehalt\\u201c, dās \\u201eSichel\\u201c' \\u2014 dātra yes; dhārā absent.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.33 (line 12770)\", \"stance\": \"supports\",\n    \"note\": \"'Skt. dā- ... \\u2018cut off, divide\\u2019 and \\u2018mow\\u2019 (cf. dātra- \\u2018sickle\\u2019)'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. dātrom (IEC)\", \"stance\": \"silent\",\n    \"note\": \"Mann's entry for the *-tro- noun was not located in the OCR at the leaves checked (leaves 85-86 hold dabh-/dābh-/dabhn-); no statement either way on dhārā.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"dâs\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Middle Persian dās [d\\u02bcs] 'sickle' continues Old Iranian *dāθra- (= Av. dāθra-, Skt. dā́tra-), with the regular Iranian development \"\n   \"of the cluster *-θr- to Middle/New Persian -s- (the same change that gives OP puθra- > MP pus(ar) 'son' and Av. pāθra- > MP pās 'watch'). \"\n   \"Hübschmann sets it out as a paradigm case of that rule. The arrow Sanskrit > Pahlavi in the chart is of course a cognate relation, not a borrowing: \"\n   \"Skt. dātra- and MP dās are parallel Indo-Iranian reflexes of *dáHtram, not one from the other.\"),\n \"derivation_fa\": (\"فارسی میانه (پهلوی) dās «داس» بازماندهٔ ایرانی باستان *dāθra- (اوستایی dāθra-، سانسکریت dā́tra-) است. \"\n   \"خوشهٔ *-θr- ایرانی باستان در فارسی میانه به‌قاعده به س بدل می‌شود؛ همان دگرگونی که در puθra- > پسر و pāθra- > پاس دیده می‌شود، و هوبشمان (پژوهش‌های پارسی، بند ۹۶) \"\n   \"همین «داس» را نمونهٔ شاخص این قاعده آورده است. مکنزی نیز در فرهنگ کوچک پهلوی «dās [d\\u02bcs] داس» را ثبت کرده است. \"\n   \"تنها نکته آنکه پیکانِ «سانسکریت ← پهلوی» در نمودار را باید هم‌ریشگی خواند نه وام‌گیری: dātra و dās هر دو مستقلاً از *dáHtram هندوایرانی آمده‌اند. ادعای نورایی درست است.\"),\n \"sources\": [W + \"%D8%AF%D8%A7%D8%B3\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:813\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāte\\u2018 vol.2 leaf 273 (= printed p.813 on the offset fixed by the دهره page): headword «داس» \\u2018بر وزن طاس، افزاری است که بدان غله درو کنند و بعربی منجل خوانند\\u2019, and Mo\\u2018in's footnote 4 to it reads (through the OCR) 'پهلوی dās، هندی باستان dātra-, ... کردی ...' \\u2014 i.e. exactly Nourai's Sanskrit > Pahlavi > Persian chain.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.v. dās (PHD.txt line 310)\", \"stance\": \"supports\",\n    \"note\": \"'dās [d\\u02bcs | N ~] sickle.' (immediately followed by 'dāšr [d\\u02bcsl = Av. dātra-) gift, reward', which is the homophonous \\u2018gift\\u2019 word, i.e. Pokorny's np. dāra \\u201eGehalt\\u201c).\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien \\u00a7 96 (HUB.txt line 7254)\", \"stance\": \"supports\",\n    \"note\": \"'\\u00a7 96. Ap. \\u03b8r wird im Np. zu s oder hr: a) zu s in: ... dās \\u2018Sichel\\u2019, phl. dās Gl. and Ind. 181, skr. dātra-'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n    \"note\": \"grep of NYB_vol2_glossary.txt for 'dās' / 'd\\u02bcs' returned no headword for the sickle word (Nyberg's glossary covers only the texts he edits).\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"dâs \\u00abداس\\u00bb; b\\u00ee-das-tar \\u00abبیدستر\\u00bb\", \"verdict\": \"disputed\",\n \"derivation\": (\"dās \\u00abداس\\u00bb 'sickle' is correct and is one of the textbook Iranian reflexes of this root: Proto-Iranian *dāθra- > MP dās > NP dās, \"\n   \"with *-θr- > -s- (Hübschmann \\u00a796); Pokorny himself prints 'npers. ... dās \\u201eSichel\\u201c' on p.175, and Horn no. 525 has 'dās \\u2018Sichel\\u2019: ai. dātra- \\u2018Sichel\\u2019; phlv. dās (AV.)', \"\n   \"noting the Kurdish and Balochi loans of the same word. \\n\"\n   \"bīdastar \\u00abبیدستر\\u00bb 'beaver' does NOT belong here. The analysis 'without sickles' is Nourai's re-shaping of Mo\\u2018in's own folk etymology: \"\n   \"Mo\\u2018in (Farhang-e Fārsī, quoted by Dehkhodā and by Encyclopaedia Iranica s.v. BEAVER) reads it bī 'without' / bā 'with' + dast 'hand' + arr(e) \\u00abاره\\u00bb 'saw', \"\n   \"i.e. 'the animal that saws trees down without a hand-saw' \\u2014 arre 'saw', not dās 'sickle'. Both are folk etymologies of the same kind. \"\n   \"Two things tell against any such segmentation: (i) the oldest attestation, Ḥamza Eṣfahānī (4th/10th c., quoted in Bīrūnī's Ṣaydana p.142), has vīdastar with initial v-, \"\n   \"which rules out bī- 'without'; (ii) Bīrūnī himself already offered a rival split (bī 'without' + dast [= tāmm] 'complete', 'incomplete as to its testicles'), \"\n   \"showing the word was opaque to Persian speakers by the 11th century. The inherited Iranian word for 'beaver' is a different stem altogether: Av. bawri-/bawra-, \"\n   \"MP bawrag/babrag (Horn no. 181), NP babr. Wiktionary's alternative ('wood-eater', *widʰu- + *h\\u2081ed-) is likewise a guess. Verdict for the word: disputed.\"),\n \"derivation_fa\": (\"«داس» درست است و از نمونه‌های کلاسیک همین ریشه است: ایرانی باستان *dāθra- ← فارسی میانه dās ← فارسی نو «داس»، با تبدیل قاعده‌مند *-θr- به س. \"\n   \"پوکورنی در همان صفحهٔ ۱۷۵ «npers. dās \\u2018داس\\u2019» را آورده و هرن (بند ۵۲۵) نیز آن را با dātra- سانسکریت و dās پهلوی سنجیده است. \"\n   \"اما «بیدستر» (سگ آبی) به این ریشه ربطی ندارد. تحلیل نورایی («بی‌داس» یعنی جانوری که بی داس درخت می‌برد) صورتِ دگرگون‌شدهٔ ریشه‌شناسی عامیانهٔ خود معین است که آن را \"\n   \"بی + دست + ار (= اره) می‌خواند، یعنی «بی‌اره». دو نکته این تجزیه را رد می‌کند: نخست آنکه کهن‌ترین ضبط، از حمزهٔ اصفهانی به نقل صیدنهٔ بیرونی، «ویدستر» با واو آغازین است \"\n   \"و جای «بی» نفی را نمی‌گذارد؛ دوم آنکه خودِ بیرونی تجزیهٔ رقیبی پیش نهاده (بی + دستِ تام)، و این نشان می‌دهد واژه از سدهٔ پنجم هجری برای فارسی‌زبانان تیره بوده است. \"\n   \"واژهٔ موروثی ایرانی برای «سگ آبی» ستاک دیگری است: اوستایی bawri-، پهلوی bawrag/babrag، فارسی «ببر». پس این بخش را پژوهش امروزی رد می‌کند و آن را ریشه‌شناسی عامیانه می‌داند.\"),\n \"sources\": [W + \"%D8%AF%D8%A7%D8%B3\", W + \"%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1\",\n             \"https://www.iranicaonline.org/articles/beaver-castor-fiber-l/\",\n             \"https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1/\"],\n \"ref_check\": [\n   {\"ref\": \"POK:175\", \"status\": \"supports\",\n    \"note\": \"POK_01 leaf 186 (p.175): '... dātram n. \\u201eSichel\\u201c, npers. dāra \\u201eGehalt\\u201c, dās \\u201eSichel\\u201c' \\u2014 Persian dās is expressly in Pokorny under this root. Pokorny says nothing about bīdastar.\"},\n   {\"ref\": \"BQT:333\", \"status\": \"partial\",\n    \"note\": \"Borhān-e Qāte\\u2018 vol.1 leaf 553 = printed p.333 (fixed by its catchline 'بقیه از صفحهٔ ۳۳۲'): headword «بیدستر» \\u2018بر وزن بی مسطر، نام حیوانی است بحری ...\\u2019 with a footnote carrying Latin-script forms (OCR unreadable). The page has the word, but the analysis attached to it in Mo\\u2018in's Farhang-e Fārsī (reported by Dehkhodā and Iranica) is bī + dast + arre \\u2018saw\\u2019, not dās \\u2018sickle\\u2019.\"},\n   {\"ref\": \"BQT:813\", \"status\": \"supports\",\n    \"note\": \"vol.2 leaf 273 = p.813, headword «داس» with Mo\\u2018in's footnote giving Pahlavi dās and Old Indian dātra-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 525 (HRN.txt line 4729)\", \"stance\": \"supports\",\n    \"note\": \"'525. dās \\u2018Sichel\\u2019. ai. dātra- \\u2018Sichel\\u2019; phlv. dās (AV.). afγ. lūr \\u2018Sichel\\u2019; LW. kurd. bal. dās.' (Horn no. 181 treats babr/bawrak \\u2018Biber\\u2019 separately and never mentions bīdastar.)\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, s.v. داس/داسه, p.261 (ARY_pages.txt line 7668)\", \"stance\": \"supports\",\n    \"note\": \"entry «داس، داسه» lists پهلوی dās, سانسکریت dātra-, اوستایی dāθra- and cites Pokorny and Borhān-e Qāte\\u2018; Aryanpur's separate entry بر/وبر (p.~110) glosses بیدستر as the meaning of the inherited Av. bawra-/bawri- word, i.e. he does not analyse bīdastar as bī+dās.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien \\u00a7 96 (HUB.txt line 7254)\", \"stance\": \"supports\",\n    \"note\": \"'dās \\u2018Sichel\\u2019, phl. dās Gl. and Ind. 181, skr. dātra-' as an instance of Ap. \\u03b8r > Np. s.\"},\n   {\"src\": \"MON\", \"where\": \"Mo\\u2018in, Farhang-e Fārsī s.v. بیدستر (via Dehkhodā/abadis and Iranica)\", \"stance\": \"contradicts\",\n    \"note\": \"Iranica s.v. BEAVER: 'bīdastar or bādastar, which, according to Mo\\u2018īn (Farhang-e fārsī, s.v.), is composed of bī \\u201cwithout\\u201d/bā \\u201cwith\\u201d + dast \\u201chand\\u201d + ar \\u201csaw\\u201d' \\u2014 arre, not dās; and 'Vīdastar' in Ḥamza Eṣfahānī via Bīrūnī, Ṣaydana p.142.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"dahreh \\u00abدهره\\u00bb\", \"verdict\": \"plausible\",\n \"derivation\": (\"Persian dahre \\u00abدهره\\u00bb is a heavy hooked billhook/sickle-knife, characteristically of Gīlān; Borhān-e Qāte\\u2018 p.904 defines it \"\n   \"'a hafted weapon whose haft is of iron and whose head is like a sickle (dās), extremely sharp, mostly owned by the people of Gīlān; some say it is an implement \"\n   \"with which grain is reaped'. Mo\\u2018in's footnote to that entry derives it from Sanskrit dhārā ('edge, blade'), and that is exactly Nourai's arrow. \"\n   \"The derivation is defensible as a Wanderwort/Indic loan into the Caspian region (dhārā 'blade' > dahre with the ordinary Persian anaptyxis of a short vowel and \"\n   \"the -a ending), but it does not belong under this root: Skt. dhārā is from PIE *dʰerh\\u2083-/*dʰenh\\u2082- (Mayrhofer, Lubotsky), not from *deh\\u2082(y)- 'divide'. \"\n   \"No independent Iranian handbook (Horn, Hübschmann, Cheung) treats dahre at all, so Mo\\u2018in's note is the only real authority. Hence 'plausible' for the Sanskrit link, \"\n   \"but the placement under Dâ 1 is wrong.\"),\n \"derivation_fa\": (\"«دهره» تیغِ داس‌مانند و دسته‌دارِ گیلانی است. برهان قاطع (ص ۹۰۴) آن را چنین می‌آورد: «حربه است دسته‌دار و دسته‌اش از آهن و سرش مانند داس باشد و در غایت تیزی بوده و بیشتر مردم گیلان دارند». \"\n   \"معین در حاشیهٔ همان صفحه (پانوشت ۹) آن را از سانسکریت dhārā «لبه، تیغه» می‌داند و نورایی نیز همین را گرفته است. \"\n   \"این وام‌گیری از هندی باستان پذیرفتنی است، ولی جای این واژه زیر ریشهٔ Dâ نیست: dhārā خود از ریشهٔ *dʰerh\\u2083- یا *dʰenh\\u2082- هندواروپایی است، نه از *deh\\u2082(y)- «بخش کردن». \"\n   \"هیچ‌یک از هرن، هوبشمان و چونگ به «دهره» نپرداخته‌اند و تنها مرجع، حاشیهٔ معین است. پس: با احتیاط پذیرفتنی، اما جایگاهش در نمودار نادرست است.\"),\n \"sources\": [W + \"%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BE\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:904\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāte\\u2018 vol.2 leaf 364 = printed p.904 (its own catchline reads 'بقیه در صفحهٔ ۹۰۵'): «دهره ۹ - بر وزن هره، حربه است دسته‌دار و دسته‌اش از آهن و سرش مانند داس باشد و در غایت تیزی بوده و بیشتر مردم گیلان دارند ... و بعضی گویند افزاری است که بدان غله درو کنند»; footnote 9 at the foot of the same page: 'سانسکرت dhārā'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo\\u2018in, Farhang-e Fārsī, s.v. دهره\", \"stance\": \"supports\",\n    \"note\": \"same editor, same etymology as his Borhān footnote; the lexicon entry keeps the Gīlānī billhook sense.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss\", \"stance\": \"silent\",\n    \"note\": \"grep of HRN.txt for 'dahre'/'dahra' returns nothing; Horn has no entry for the word.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb\", \"stance\": \"silent\",\n    \"note\": \"not a verb; no entry (grep of CHEUNG.txt for 'dahr' finds only unrelated *dar- material).\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Germanic\", \"words\": \"t\\u00eemo; t\\u00eediz\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Both are the standard Germanic reflexes of the zero-grade *dī- of this root. *tīdiz f. 'division of time' < PIE *dī-ti- (Grimm's Law d > t, \"\n   \"*-ti- abstract suffix) gives OE tīd, OS tīd, ON tíð, OHG zīt, Ger. Zeit; *tīmōn- m. < PIE *dī-mon- (the same base with the -mon- suffix that also makes Gk. daimōn) \"\n   \"gives OE tīma, ON tími. The Germanic pair is the exact formal counterpart of Arm. ti, gen. tioy 'age, time' (*dī-t-), which Pokorny cites alongside it. \"\n   \"The gloss 'a period (piece) of time' correctly renders the etymological sense 'a cut-off stretch'.\"),\n \"derivation_fa\": (\"هر دو صورت، بازتاب قاعده‌مندِ درجهٔ صفرِ *dī- این ریشه در ژرمنی‌اند. *tīdiz «برشِ زمان» از *dī-ti- هندواروپایی است (با تبدیل d به t بنا بر قانون گریم و پسوند اسم‌ساز *-ti-) \"\n   \"که انگلیسی کهن tīd، آلمانی Zeit و اسکاندیناوی کهن tíð از آن آمده؛ و *tīmōn- از *dī-mon- است، با همان پسوند -mon- که در daimōn یونانی نیز هست، که انگلیسی کهن tīma را داده است. \"\n   \"همتای دقیقِ این ساخت، ti ارمنی (مضاف‌الیه tioy) «سن، زمان» است که پوکورنی در کنار آن آورده. معنای ریشه‌شناختی «پارهٔ بریده‌شدهٔ زمان» است و ترجمهٔ نورایی درست است. ادعای او تأیید می‌شود.\"),\n \"sources\": [W + \"Reconstruction:Proto-Germanic/t%C4%ABdiz\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. dā-: '2. Suffixed variant form *dī-t- in Germanic *tīdiz, division of time, in: a. Old English tīd, time, season: TIDE ... 3. Suffixed variant form *dī-mon in Germanic *tīmōn- in Old English tīma, time, period: TIME.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.176 (POK_01 leaf 187)\", \"stance\": \"supports\",\n    \"note\": \"'Mit Tiefstufe di-: arm. ti, Gen. tioy \\u201eAlter, Jahre, Tage, Zeit\\u201c (*di-t- oder *dī-to-), ahd. zīt f., as. ags. tīd, anord. tíð f. \\u201eZeit, Stunde\\u201c (*tīþ-, idg. *dī-t-, ursprgl. \\u201eZeitabschnitt\\u201c)'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. tide (KLN_1966.txt line 39227)\", \"stance\": \"supports\",\n    \"note\": \"'fr. Teut. *ti-di-, prop. \\u2018division of time\\u2019, fr. base *ti- ... whence also ON. ti-mi, OE. ti-ma, \\u2018time\\u2019'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 764 (leaf 772)\", \"stance\": \"supports\",\n    \"note\": \"'ahd. zīt f. ... as. tīd, ags. tīd f., anord. tíð f. ... mit Formans -men- anord. tími, ags. tíma, engl. time \\u201eZeit\\u201c'.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"time, tide\", \"verdict\": \"confirmed\",\n \"derivation\": (\"OE tīma > ME time > time; OE tīd 'time, hour, season' > ME tid(e) > tide, the modern sense 'ebb and flow of the sea' being a specialisation \"\n   \"of 'fixed time' first common in Middle English (cf. Du. tij 'flood tide' beside tijd 'time', MLG getīde, Ger. Gezeiten). Klein makes the same point; \"\n   \"the old sense survives in eventide, Yuletide, and in the phrase 'time and tide'.\"),\n \"derivation_fa\": (\"انگلیسی time از انگلیسی کهن tīma و tide از انگلیسی کهن tīd «زمان، هنگام، فصل» است. معنای امروزیِ tide یعنی «جزر و مد» تحول معناییِ متأخری است \"\n   \"که در انگلیسی میانه از «وقت معیّن» پدید آمده؛ همین دوگانگی در هلندی هم دیده می‌شود (tij «مد» در برابر tijd «زمان») و در آلمانی Gezeiten. \"\n   \"معنای کهن در ترکیب‌هایی چون eventide و Yuletide بازمانده است. کلاین همین را می‌گوید. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/tide\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins index (AHD_watkins1985.txt line 2389): 'TIDE1 dā- TIDE2 dā- TIDINGS dā- ... TIME dā-'; both English words are listed under this root in the AHD appendix.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. tide (line 39227)\", \"stance\": \"supports\",\n    \"note\": \"'tide, n. \\u2014 ME. tid, tide, fr. OE. tīd, \\u2018time, season\\u2019 ... For the sense development of OE. tide, \\u2018time; flood tide\\u2019, cp. Du. tij, \\u2018flood tide\\u2019, distinguished from tijd, \\u2018time\\u2019.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\",\n    \"note\": \"the OCR of SKT.txt does not carry a locatable 'Tide'/'Time' headword line (grep for '^Tide'/'Time, s' empty); no statement recorded.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Greek\", \"words\": \"d\\u011bmos; d\\u011bmos-keratos; daim\\u00f4n; epi-d\\u011bmos\", \"verdict\": \"transcription_suspect\",\n \"derivation\": (\"dēmos (\\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2, Doric \\u03b4\\u1fb6\\u03bc\\u03bf\\u03c2) 'district; the people (of a district)' is *dā-mo- 'a division (of land/society)', with the -mo- suffix; \"\n   \"the Doric ā guarantees the inherited long vowel, and the Celtic cognate OIr. dám 'company, retinue' confirms the formation. Correct. \\n\"\n   \"daimōn (\\u03b4\\u03b1\\u03af\\u03bc\\u03c9\\u03bd) 'divinity' is *dai-mon- 'apportioner, allotter (of men's destinies)', an agent noun to \\u03b4\\u03b1\\u03af\\u03bf\\u03bc\\u03b1\\u03b9 'I divide, apportion'; \"\n   \"Pokorny and Klein both give exactly this ('eigentlich \\u201ezuteilend\\u201c'). Correct. \\n\"\n   \"epidēmos (\\u1f10\\u03c0\\u03af\\u03b4\\u03b7\\u03bc\\u03bf\\u03c2) 'among the people, prevalent in a country' = \\u1f10\\u03c0\\u03af 'upon, among' + \\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2, whence \\u1f10\\u03c0\\u03b9\\u03b4\\u03b7\\u03bc\\u03af\\u03b1 'a stay in a place; an epidemic'. Correct. \\n\"\n   \"'děmos-keratos' is not a Greek word. The compound is \\u03b4\\u03b7\\u03bc\\u03bf\\u03ba\\u03c1\\u03b1\\u03c4\\u03af\\u03b1 / \\u03b4\\u03b7\\u03bc\\u03bf-\\u03ba\\u03c1\\u03b1\\u03c4- 'rule of the people', second member \\u03ba\\u03c1\\u03ac\\u03c4\\u03bf\\u03c2 'strength, rule' (kratos), \"\n   \"not *keratos (which would be \\u03ba\\u03ad\\u03c1\\u03b1\\u03c2, gen. \\u03ba\\u03ad\\u03c1\\u03b1\\u03c4\\u03bf\\u03c2 'horn' \\u2014 an unrelated word). I checked the printed page: the book itself prints 'děmos-keratos' with the cross-reference \"\n   \"\\u261e Kar 1, i.e. Nourai's own root box for kratos; so the mistake is the author's, not the extraction's, and it is a simple metathesis/vowel intrusion in his transliteration.\"),\n \"derivation_fa\": (\"\\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2 (dēmos، دوری \\u03b4\\u1fb6\\u03bc\\u03bf\\u03c2) «ناحیه؛ مردمِ یک ناحیه» از *dā-mo- «بخش، پاره» با پسوند -mo- است؛ آلفای بلندِ گویش دوری، بلندیِ موروثی واکه را تأیید می‌کند. \"\n   \"\\u03b4\\u03b1\\u03af\\u03bc\\u03c9\\u03bd از *dai-mon- «بخش‌کننده، قسمت‌دهنده» است، اسم فاعل از \\u03b4\\u03b1\\u03af\\u03bf\\u03bc\\u03b1\\u03b9 «بخش می‌کنم»؛ پوکورنی و کلاین هر دو همین را می‌گویند. \"\n   \"\\u1f10\\u03c0\\u03af\\u03b4\\u03b7\\u03bc\\u03bf\\u03c2 نیز \\u1f10\\u03c0\\u03af «بر، میان» + \\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2 است. تا اینجا همه درست. \"\n   \"اما «děmos-keratos» صورتی یونانی نیست؛ ترکیبِ درست \\u03b4\\u03b7\\u03bc\\u03bf\\u03ba\\u03c1\\u03b1\\u03c4\\u03af\\u03b1 با جزء دومِ \\u03ba\\u03c1\\u03ac\\u03c4\\u03bf\\u03c2 (kratos) «توان، فرمانروایی» است، نه keratos که در یونانی «شاخ» معنی می‌دهد. \"\n   \"تصویر صفحهٔ چاپی را دیدم: خودِ کتاب «děmos-keratos» را چاپ کرده است، پس این خطای چاپی/آوانگاریِ نویسنده است نه خطای خوانشِ اسکن.\"),\n \"sources\": [\"https://www.etymonline.com/word/democracy\"],\n \"error_in\": \"book\",\n \"book_prints\": \"d\\u011bmos-keratos : people's government \\u261e Kar 1\",\n \"correct_form\": \"d\\u0113mo-kratos / \\u03b4\\u03b7\\u03bc\\u03bf\\u03ba\\u03c1\\u03b1\\u03c4\\u03af\\u03b1 (\\u03ba\\u03c1\\u03ac\\u03c4\\u03bf\\u03c2 'rule')\",\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. dā-: '4. Suffixed form *dā-mo-, perhaps \\u201cdivision of society,\\u201d in Greek dēmos, people, land: DEME, DEMOS, DEMOTIC; DEMAGOGUE, DEMIURGE, DEMOCRACY, DEMOPHOBIA, ENDEMIC, EPIDEMIC, PANDEMIC. 5. Suffixed form *dai-mon-, divider, provider, in Greek daimōn, divinity: DEMON.' Supports all three real words; AHD spells the compound DEMOCRACY (kratos).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.175-176 (POK_01 leaf 186)\", \"stance\": \"supports\",\n    \"note\": \"'wohl auch \\u03b4\\u03b1\\u03af\\u03bc\\u03c9\\u03bd \\u201eGott, Göttin; Geschick\\u201c (eigentlich \\u201ezuteilend\\u201c)' and 'Mit Formans -mo-: dāmos f. \\u201eVolk\\u201c: gr. \\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2, dor. \\u03b4\\u1fb6\\u03bc\\u03bf\\u03c2 m. \\u201e(Volksabteilung) Volk, Gebiet\\u201c, air. dām f. \\u201eGefolgschaft, Schar\\u201c'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. damn / tide (lines 10279, 39227)\", \"stance\": \"supports\",\n    \"note\": \"'\\u03b4\\u03b1\\u03af\\u03bc\\u03c9\\u03bd, \\u2018god, goddess\\u2019, lit. \\u2018divider, distributor (of men\\u2019s destinies)\\u2019 ... \\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2, \\u2018district, people\\u2019'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 764 (leaf 772)\", \"stance\": \"supports\",\n    \"note\": \"'Mit Formans -mo-: gr. \\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2, dor. \\u03b4\\u1fb6\\u03bc\\u03bf\\u03c2 \\u201e(Volksabteilung) Volk, Gebiet; in Athen der einzelne Gau\\u201c'.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"French\", \"words\": \"democratie\", \"verdict\": \"confirmed\",\n \"derivation\": (\"French d\\u00e9mocratie (the book prints it without the accent) is not a direct continuation of Greek but a learned borrowing: Gk. \\u03b4\\u03b7\\u03bc\\u03bf\\u03ba\\u03c1\\u03b1\\u03c4\\u03af\\u03b1 \"\n   \"(Herodotus, 5th c. BCE) > Medieval Latin democratia (13th c., in the scholastic translations of Aristotle's Politics) > Middle French democracie/d\\u00e9mocratie (14th c., Oresme). \"\n   \"The chart's Greek > French arrow is therefore right in substance; the unmarked intermediary is Medieval Latin.\"),\n \"derivation_fa\": (\"«démocratie» فرانسه (که کتاب بدون علامتِ حروف‌صدادار چاپ کرده) دنبالهٔ مستقیم یونانی نیست، بلکه وام‌واژه‌ای عالمانه است: \"\n   \"یونانی \\u03b4\\u03b7\\u03bc\\u03bf\\u03ba\\u03c1\\u03b1\\u03c4\\u03af\\u03b1 (هرودوت، سدهٔ پنجم پیش از میلاد) ← لاتینِ میانه democratia (سدهٔ سیزدهم میلادی، در ترجمه‌های مدرسیِ سیاستِ ارسطو) ← فرانسهٔ میانه démocratie (سدهٔ چهاردهم، اورم). \"\n   \"پس پیکانِ «یونانی ← فرانسه» در نمودار در جوهر درست است و تنها حلقهٔ لاتینِ میانه نانوشته مانده است.\"),\n \"sources\": [\"https://www.etymonline.com/word/democracy\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own in the book (refs=None); checked against Etymonline and Klein instead.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. democracy\", \"stance\": \"supports\",\n    \"note\": \"Klein's cross-reference list under 'tide' explicitly includes 'democracy' among the derivatives of I.-E. *dā-; his democracy entry routes F. d\\u00e9mocratie < ML. democratia < Gk. \\u03b4\\u03b7\\u03bc\\u03bf\\u03ba\\u03c1\\u03b1\\u03c4\\u03af\\u03b1.\"},\n   {\"src\": \"DEV/PHN\", \"where\": \"Devic / Pihan (French words of Oriental origin)\", \"stance\": \"silent\",\n    \"note\": \"not an Orientalism, so absent from both \\u2014 as expected.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"\\u2014 (script only: دموکراسی \\u060c دموکرات)\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Persian دموکراسی demokrāsi and دموکرات demokrāt are 20th-century borrowings from French d\\u00e9mocratie / d\\u00e9mocrate, taken in during the \"\n   \"Constitutional period and the language of the early Majles; the French route is visible in the vocalism (-krāsi with -sī rendering French -tie [si], not English -cracy [kr\\u00e6si]) \"\n   \"and in the derivative دموکراتیک demokrātik < French d\\u00e9mocratique. Mo\\u2018in's Farhang-e Fārsī prints the French etymon in Latin script beside each of the three entries.\"),\n \"derivation_fa\": (\"«دموکراسی» و «دموکرات» وام‌واژه‌های سدهٔ چهاردهم خورشیدی از فرانسه‌اند (d\\u00e9mocratie و d\\u00e9mocrate) که در دورهٔ مشروطه و زبان مجلس اول وارد فارسی شدند. \"\n   \"مسیر فرانسوی از آواشناسیِ واژه پیداست: پایانهٔ «-اسی» برگردانِ -tie فرانسوی است نه -cracy انگلیسی؛ و مشتقِ «دموکراتیک» نیز از d\\u00e9mocratique فرانسه است. \"\n   \"معین در فرهنگ فارسی برای هر سه مدخل صورت فرانسویِ لاتین‌نویس را در کنار واژه آورده است. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/democracy\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1561\", \"status\": \"supports\",\n    \"note\": \"Mo\\u2018in, Farhang-e Fārsī (MON_part1.txt lines 63014-63017): 'دموکرات: [Latin-script French etymon] (ص.) طرفدار دموکراسی، علاقمند به حکومت ملی' / 'دموکراتیک: d\\u00e9mocratique (ص‌نس.)' / 'دموکراسی: d\\u00e9mocratie (امر.) حکومتی که در آن قدرت عالیه منبعث از ملت است ...'. The three entries stand together exactly as the chart's box has them; the OCR of this text carries no page numerals, so p.1561 itself could not be re-checked.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsī, دموکرات / دموکراتیک / دموکراسی\", \"stance\": \"supports\",\n    \"note\": \"Mo\\u2018in tags all three with Latin-script French etyma, i.e. he too routes them through French, not English or Greek directly.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur covers inherited Indo-European vocabulary only; no entry for the modern loan (grep of ARY_pages.txt for 'دموکراس' empty).\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"democracy\", \"verdict\": \"confirmed\",\n \"derivation\": (\"English democracy is first recorded in the 1570s, borrowed from Middle French d\\u00e9mocratie, itself from Medieval Latin democratia (13th c.) < Gk. \"\n   \"\\u03b4\\u03b7\\u03bc\\u03bf\\u03ba\\u03c1\\u03b1\\u03c4\\u03af\\u03b1 = \\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2 'people' + -\\u03ba\\u03c1\\u03b1\\u03c4\\u03af\\u03b1 'rule' (\\u03ba\\u03c1\\u03ac\\u03c4\\u03bf\\u03c2 'strength, power'). The English ending -cracy is the regular Anglicisation \"\n   \"of French -cratie. The chart's French > English arrow is exactly the accepted route.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسی democracy نخستین بار در دههٔ ۱۵۷۰ میلادی ثبت شده و وام‌گرفته از فرانسهٔ میانه d\\u00e9mocratie است که خود از لاتینِ میانه democratia (سدهٔ سیزدهم) \"\n   \"و آن از یونانی \\u03b4\\u03b7\\u03bc\\u03bf\\u03ba\\u03c1\\u03b1\\u03c4\\u03af\\u03b1 (\\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2 «مردم» + \\u03ba\\u03c1\\u03ac\\u03c4\\u03bf\\u03c2 «توان، فرمانروایی») آمده است. پسوندِ انگلیسیِ -cracy برگردانِ قاعده‌مندِ -cratie فرانسوی است. \"\n   \"پس پیکانِ «فرانسه ← انگلیسی» در نمودار همان مسیرِ پذیرفته‌شده است.\"),\n \"sources\": [\"https://www.etymonline.com/word/democracy\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:351\", \"status\": \"partial\",\n    \"note\": \"p.351 of the AHD New College edition is the dictionary page carrying 'democracy' (not the IE appendix); that page could not be re-read, but the Watkins appendix index (AHD_watkins1985.txt line 1419) lists 'DEMOCRACY dā-', which is the substantive claim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein, cross-reference list s.v. tide\", \"stance\": \"supports\",\n    \"note\": \"'Cp. also dah, damage, damn, dan, dapifer, deme, democracy, demon, demos, demotic, endemic, epidemic.'\"},\n   {\"src\": \"WEB/FSD\", \"where\": \"Webster's New Twentieth Century / Funk & Wagnalls\", \"stance\": \"silent\",\n    \"note\": \"not consulted for a chain this uncontroversial; Etymonline (archived) covers it with dates.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"demography, demon, epidemic\", \"verdict\": \"confirmed\",\n \"derivation\": (\"All three go back to \\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2/\\u03b4\\u03b1\\u03af\\u03bc\\u03c9\\u03bd. demography is a modern (1880s) learned coinage, Gk. \\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2 + -\\u03b3\\u03c1\\u03b1\\u03c6\\u03af\\u03b1 'writing, description' \"\n   \"(coined in French, d\\u00e9mographie, by Achille Guillard 1855). demon comes through Latin: Gk. \\u03b4\\u03b1\\u03af\\u03bc\\u03c9\\u03bd 'divinity, tutelary spirit' > Lat. daemon, which in Christian Latin and \"\n   \"the Vulgate took over the pejorative sense 'evil spirit' from the Septuagint's use of \\u03b4\\u03b1\\u03b9\\u03bc\\u03cc\\u03bd\\u03b9\\u03bf\\u03bd for pagan gods; hence ME demon. epidemic is Gk. \\u1f10\\u03c0\\u03b9\\u03b4\\u03b7\\u03bc\\u03af\\u03b1 \"\n   \"'a stay among the people; a disease prevalent among a people' > French \\u00e9pid\\u00e9mique (16th c.) > English. The chart is right to hang them all on the Greek node.\"),\n \"derivation_fa\": (\"هر سه واژه به \\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2 و \\u03b4\\u03b1\\u03af\\u03bc\\u03c9\\u03bd یونانی برمی‌گردند. demography ساختِ عالمانهٔ نو است (نخست در فرانسه d\\u00e9mographie، ساختهٔ آشیل گیار در ۱۸۵۵) از \\u03b4\\u1fc6\\u03bc\\u03bf\\u03c2 + -\\u03b3\\u03c1\\u03b1\\u03c6\\u03af\\u03b1. \"\n   \"demon از راه لاتین آمده است: \\u03b4\\u03b1\\u03af\\u03bc\\u03c9\\u03bd یونانی «ایزد، روحِ نگهبان» ← daemon لاتین؛ بار معناییِ منفیِ «دیو، روح پلید» را از کاربردِ \\u03b4\\u03b1\\u03b9\\u03bc\\u03cc\\u03bd\\u03b9\\u03bf\\u03bd در ترجمهٔ سبعینی (برای خدایان بت‌پرستان) و سپس لاتینِ کلیسایی گرفته است. \"\n   \"epidemic از \\u1f10\\u03c0\\u03b9\\u03b4\\u03b7\\u03bc\\u03af\\u03b1 «اقامت در میان مردم؛ بیماریِ همه‌گیر» از راه فرانسهٔ \\u00e9pid\\u00e9mique به انگلیسی رسیده. جای دادنِ هر سه زیر گرهٔ یونانی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/demon\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins index (line 1419): 'DEMOCRACY dā- DEMON dā- DEMOPHOBIA dā- DEMOS dā- DEMOTIC dā-'; and s.v. dā- item 4 lists ENDEMIC, EPIDEMIC, PANDEMIC.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. damn, cross-refs (line 10279)\", \"stance\": \"supports\",\n    \"note\": \"'\\u03b4\\u03b1\\u03af\\u03bc\\u03c9\\u03bd, \\u2018god, goddess\\u2019, lit. \\u2018divider, distributor (of men\\u2019s destinies)\\u2019. See demon and cp. damage, condemn, indemnify.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW p.175 (leaf 186)\", \"stance\": \"supports\",\n    \"note\": \"'\\u03b4\\u03b1\\u03af\\u03bc\\u03c9\\u03bd \\u201eGott, Göttin; Geschick\\u201c (eigentlich \\u201ezuteilend\\u201c)' \\u2014 the etymological sense behind demon.\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Indo-European\", \"words\": \"Dabh, D\\u00e2bh, Dabhn, Dap\", \"verdict\": \"disputed\",\n \"derivation\": (\"This sub-root box reproduces S. E. Mann, An Indo-European Comparative Dictionary p.129 almost word for word: Mann has three consecutive entries \"\n   \"'dabh- \\u2018harm, hurt, damage\\u2019', 'dābh- (long-grade variant of dabh-)' and 'dabhn- (theme of dabh-)', and it is Mann who assembles under them Skt. dabhah, Av. daiβiš, \"\n   \"Per. dav and Lat. damnum, damnare. Modern scholarship does not accept the assembly: it separates two roots that Mann merged. (i) PIE *dʰebʰ- 'to harm, deceive' \"\n   \"(Pokorny 240 'dhebh-, dhebh-eu- \\u201ebeschädigen; verkürzen, betrügen\\u201c'; LIV 132) gives Skt. dabhnóti, dabhrá-, Av. dab- 'to deceive' and, in Iranian, NP farēb/farēftan; \"\n   \"(ii) PIE *dap- 'to apportion (in exchange)' \\u2014 a p-extension of this page's own root *deh\\u2082(y)-, which is why Watkins files it '[In Pok. dā- 175]' \\u2014 gives Lat. daps, \"\n   \"damnum (*dap-no-), Gk. \\u03b4\\u03b1\\u03c0\\u03ac\\u03bd\\u03b7, ON tafn. The initial consonants alone decide it: *dʰ- (Skt. dabh-, Av. dab-) cannot be the *d- of Lat. damnum. So the box is right \"\n   \"about 'Dap' and wrong to put 'Dabh/Dābh/Dabhn' beside it \\u2014 and wrong, therefore, to hang the Avestan and Persian children (#13, #14) on the same node as Latin damnum (#15). \"\n   \"The AHD:1511 citation is to the New College appendix page for dap-, whose text is the one quoted above.\"),\n \"derivation_fa\": (\"این جعبهٔ فرعی تقریباً واژه‌به‌واژه از فرهنگ تطبیقی هندواروپاییِ استوارت مان (ص ۱۲۹) گرفته شده است؛ مان سه مدخلِ پیاپیِ dabh- «آسیب، زیان»، dābh- و dabhn- دارد \"\n   \"و اوست که dabhah سانسکریت، daiβiš اوستایی، «داو» فارسی و damnum لاتین را زیر یک سقف گرد می‌آورد. پژوهش امروزی این گردآوری را نمی‌پذیرد و دو ریشهٔ جداگانه می‌شناسد: \"\n   \"نخست *dʰebʰ- «آسیب زدن، فریفتن» (پوکورنی ۲۴۰) که dabhnóti سانسکریت، dab- اوستایی و در ایرانی «فریب/فریفتن» فارسی از آن است؛ \"\n   \"دوم *dap- «سهم دادن، بخشیدن در مبادله» که خود گسترشِ پ‌داری از همین ریشهٔ *deh\\u2082(y)- صفحه است (واتکینز آن را صریحاً ذیل «پوکورنی ۱۷۵» می‌گذارد) و daps و damnum لاتین و \\u03b4\\u03b1\\u03c0\\u03ac\\u03bd\\u03b7 یونانی از آن آمده‌اند. \"\n   \"همخوانِ آغازین به‌تنهایی داوری می‌کند: *dʰ (در dabh- و dab-) هرگز به *d لاتینِ damnum نمی‌رسد. پس «Dap» درست و کنارِ آن نهادنِ «Dabh/Dābh/Dabhn» نادرست است، و در نتیجه پیوندِ فرزندانِ اوستایی و فارسی (گره‌های ۱۳ و ۱۴) با damnum لاتین نیز نادرست است.\"),\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/d%CA%B0eb%CA%B0-\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:129\", \"status\": \"supports\",\n    \"note\": \"Mann, IEC p.129 (local IEC.txt leaf 86, which carries the printed numerals 129 and 130; lines 2018-2020): 'dabh- \\u2018harm, hurt, damage\\u2019. Cf. WP I, 764 & I, 850. See next and dabhn- Skt. dábhah \\u2018deceptive\\u2019; Av. daiβiš \\u2018deceit\\u2019; ... Per. dav \\u2018stroke; bet\\u2019 ...' / 'dābh- (long-grade variant of dabh-) ...' / 'dabhn- (theme of dabh-, q.v.) Skt. dabhnómi \\u2018hurt\\u2019: Lat. damnum, damnare; ON tafn \\u2018victim, prey\\u2019.' Nourai's box is a faithful copy of the page \\u2014 including the merger.\"},\n   {\"ref\": \"AHD:1511\", \"status\": \"partial\",\n    \"note\": \"the AHD IE appendix (Watkins 1985 text, line 360) has 'dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for reparation), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, INDEMNIFY, (INDEMNITY). [In Pok. dā- 175.]' \\u2014 supports 'Dap' and the Latin child, but AHD has no root *dabh-/*dabhn- at all and files nothing Avestan or Persian here.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.240, s.v. dhebh- (POK_01 leaf 251)\", \"stance\": \"contradicts\",\n    \"note\": \"'dhebh-, dhebh-eu- \\u201ebeschädigen; verkürzen, betrügen\\u201c ... Ai. dabhnóti \\u201ebeschädigt, versehrt, betrügt\\u201c ... dabhrá- \\u201ewenig, gering\\u201c; av. dab- \\u201ebetrügen, um etwas bringen\\u201c' \\u2014 Pokorny puts the whole dabh- family 65 pages away from dā- 175, i.e. in a different root.\"},\n   {\"src\": \"POK\", \"where\": \"IEW p.176-177 (leaf 187), p-extension\", \"stance\": \"supports\",\n    \"note\": \"'p-Erweiterung dāp-, dǝp-: dǝp-no-, -ni- \\u201eOpfermahl\\u201c: ai. dāpayati \\u201eteilt\\u201c; ... lat. daps ... damnum \\u201eVerlust, Schaden, Nachteil, Geldbuße\\u201c ... (*dap-no- : \\u03b4\\u03b1\\u03c0\\u03ac\\u03bd\\u03b7)' \\u2014 so 'Dap' genuinely belongs under this page's root.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb, s.v. *dab (CHEUNG.txt lines 3873-3914)\", \"stance\": \"contradicts\",\n    \"note\": \"'*dab \\u2018to deceive\\u2019 ... AVESTAN: dab- \\u2018to deceive\\u2019 ... MIDDLE PERSIAN: (+ *fra-) BMP pldp- /frēb-/ ... NWIR: (+ *fra-) NP farēftan/farēb- \\u2018to deceive\\u2019 ... SANSKRIT: dabh \\u2018to deceive\\u2019 (RV+) ... \\u00abPIE *dʰebʰ- \\u2018to deceive, harm (someone), belittle, lessen\\u2019 > LIV: 132 f. | Pok.: 240'. Cheung's Iranian reflex of the root is farēb, not dāv, and the PIE etymon is *dʰebʰ-.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 764 and I 850 (as cited by Mann himself)\", \"stance\": \"partial\",\n    \"note\": \"Mann's own cross-reference 'Cf. WP I, 764 & I, 850' shows he was knowingly joining two separate Walde-Pokorny entries (I 763ff. = dā(i)- 'teilen', with the dāp- extension; I 850 = the dheb-/dhebh- material).\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"Avestan\", \"words\": \"daivis\", \"verdict\": \"plausible\",\n \"derivation\": (\"The form is real but the gloss and the root assignment are shaky. Bartholomae's Altiranisches Wörterbuch records a Younger Avestan feminine stem \"\n   \"daβvay- whose nominative singular is daiβiš, attested at Vd. 2.29 (mā aγra .. daiβiš .. mā ta.cim anyąm daxštanąm .. aŋrahe mainyə̄uš) and Vd. 19.43 \"\n   \"(daiβiš daēvō, the personified aūšδaēva); Bartholomae defines it as 'Name eines bestimmten Gebrechens (oder Siechtums)' \\u2014 the name of a particular ailment \\u2014 \"\n   \"and marks the etymology with 'Et.?'. The sense 'deceit' comes only from the Pahlavi translation, which renders it frēftār 'deceiver', and it is that Pahlavi gloss \"\n   \"(via Darmesteter's 'tromper') that Mann turned into 'Av. daiβiš \\u2018deceit\\u2019'. The genuine Avestan noun for 'deceit' is a different word in Bartholomae's own dictionary: \"\n   \"daβay- m. 'Betrug', to the verb dab-/dav- 'to deceive'. So: the transliteration is defensible (daiβiš, spelt 'daivis' by Mann and copied by Nourai), the meaning is a \"\n   \"Pahlavi-based guess, and the parentage \\u2014 if the word is from dab- at all \\u2014 is PIE *dʰebʰ-, not the *dā-/*dap- of this page.\"),\n \"derivation_fa\": (\"صورت واژه واقعی است، ولی معنا و جایگاه ریشه‌شناختی‌اش لرزان است. بارتولومه در فرهنگ ایرانی باستان ستاکِ مؤنثِ اوستاییِ نو daβvay- را ثبت کرده که \"\n   \"صورتِ فاعلیِ مفردِ آن daiβiš است و در وندیداد ۲٫۲۹ و ۱۹٫۴۳ (daiβiš daēvō) آمده؛ بارتولومه معنای آن را «نامِ بیماری یا نقصِ معیّنی» می‌داند و در برابرِ ریشه‌شناسی‌اش تنها «؟» می‌گذارد. \"\n   \"معنای «فریب» یکسره از ترجمهٔ پهلوی می‌آید که آن را frēftār «فریبنده» برگردانده است، و مان همین را به «daiβiš اوستایی: فریب» بدل کرده و نورایی از او گرفته است. \"\n   \"واژهٔ اوستاییِ راستینِ «فریب» در خودِ بارتولومه چیز دیگری است: daβay- مذکر «فریب»، از فعل dab-/dav- «فریفتن». \"\n   \"پس: آوانگاری پذیرفتنی است، معنا برداشتی از سنّتِ پهلوی است، و اگر واژه اصلاً از dab- باشد ریشه‌اش *dʰebʰ- است نه *dā-/*dap- این صفحه. با احتیاط پذیرفتنی.\"),\n \"sources\": [W + \"Reconstruction:Proto-Iranian/dabH-\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:129\", \"status\": \"supports\",\n    \"note\": \"Mann p.129 (IEC.txt line 2018) literally prints 'Av. daiβiš \\u2018deceit\\u2019' under dabh-, and again in the Icelandic comparison 'Icel. töf, pl. tafir (obstacle: Av. daiβiš)'. Nourai's node is a faithful copy of Mann; the weakness is Mann's, not Nourai's.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW, s.vv. \\u00b9dab-, daβay-, daβvay- (BRT.txt lines 12671, 12830, and the daβvay- entry between cols. ~681-689)\", \"stance\": \"partial\",\n    \"note\": \"'j., g. \\u00b9dab- V. \\u201ebetrügen\\u201c. Praes. 2 dava-, ... 30 (Iter.) dābaya-.' / 'j. daβay- m. \\u201eBetrug\\u201c.' / 'j. daβvay- f. Name eines bestimmten Gebrechens (oder Siechtums): mā aγra .. daiβiš .. V.2,29. A) aūšδaēva personifizirt: daiβiš daēvō V.19.43. Et.? \\u2014 Pü.: frēftār (daher D.W. \\u2018tromper\\u2019; s. \\u00b9daβay-).' The form exists; the gloss 'deceit' is the Pahlavi commentator's, and Bartholomae leaves the etymology open.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *dab 'to deceive' (lines 3873-3914)\", \"stance\": \"partial\",\n    \"note\": \"confirms Av. dab- 'to deceive' and its PIE etymon *dʰebʰ- (Pok. 240), but lists no nominal daiβiš and no connection to *dap-/damnum.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian\", \"stance\": \"silent\",\n    \"note\": \"no Old Persian correspondent of this stem (grep of KNT.txt for 'daibis'/'daiv' yields only daiva- 'daeva' material, unrelated).\"}\n ]\n})\n\nN.append({\n \"id\": 14, \"lang\": \"Persian\", \"words\": \"d\\u00e2v \\u00abداو\\u00bb; d\\u00e2v-talab \\u00abداوطلب\\u00bb (script extra: داو دار)\", \"verdict\": \"plausible\",\n \"derivation\": (\"The Persian meanings are exactly right: Mo\\u2018in's Farhang-e Fārsī s.v. «داو» gives 'نوبت بازی (شطرنج، برد و مانند آن)، نوبت قمار؛ نوبت تیراندازی ... دعوی کاری، ادعای امری' \"\n   \"\\u2014 one's turn or throw in a game, one's stake at gambling, hence a claim; and «داوطلب» is a hybrid compound of that noun with the Arabic verbal noun ṭalab 'seeking', \"\n   \"'one who asks for his turn', used since the Constitutional period for 'volunteer' (with داوطلبانه, داوطلبی). The etymology, however, rests on a single authority: \"\n   \"Mann, IEC p.129, lists 'Per. dav \\u2018stroke; bet\\u2019' under dabh-/dābh- and even hesitates over the vowel ('Per. dav (*a or *ā \\u2018stroke, bet\\u2019)'). No Iranian handbook supports it: \"\n   \"Horn, Hübschmann and Cheung have no entry for dāv, and Cheung shows that the regular New Persian continuation of Iranian *dab- 'deceive' is farēb/farēftan, not dāv. \"\n   \"The semantic bridge Mann needs (\\u2018strike, blow\\u2019 > \\u2018turn at play\\u2019) is also not demonstrated for Persian. So the words and glosses are confirmed, the derivation is a \"\n   \"single-source conjecture: plausible at best.\"),\n \"derivation_fa\": (\"معناهای فارسی درست‌اند: معین در فرهنگ فارسی ذیل «داو» می‌آورد: «نوبت بازی (شطرنج، برد و مانند آن)، نوبت قمار؛ نوبت تیراندازی ... دعوی کاری، ادعای امری»؛ \"\n   \"و «داوطلب» ترکیبی دورگه است از همین اسم فارسی با مصدرِ عربیِ «طلب»، یعنی «کسی که نوبتِ خود را می‌خواهد»، که از دورهٔ مشروطه به معنای «داوطلب/volunteer» رایج شده و مشتق‌هایی چون «داوطلبانه» و «داوطلبی» دارد. \"\n   \"اما ریشه‌شناسی تنها بر یک مرجع استوار است: مان در ص ۱۲۹ «dav فارسی: ضربه؛ شرط» را ذیل dabh-/dābh- آورده و خود نیز در کوتاهی یا بلندی واکه تردید کرده است. \"\n   \"هیچ‌یک از هرن، هوبشمان و چونگ مدخلی برای «داو» ندارند، و چونگ نشان می‌دهد بازماندهٔ قاعده‌مندِ *dab- ایرانی در فارسی نو «فریب/فریفتن» است نه «داو». \"\n   \"پُلِ معناییِ «ضربه ← نوبتِ بازی» نیز برای فارسی اثبات نشده است. پس واژه و معنا تأیید می‌شود، ولی اشتقاق حدسی تک‌منبع است: با احتیاط پذیرفتنی.\"),\n \"sources\": [W + \"%D8%AF%D8%A7%D9%88%D8%B7%D9%84%D8%A8\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:129\", \"status\": \"supports\",\n    \"note\": \"Mann p.129 (IEC.txt lines 2018-2019): 'dabh- ... Per. dav \\u2018stroke; bet\\u2019' and 'dābh- ... Per. dav (*a or *ā \\u2018stroke, bet\\u2019)'. The claim is verbatim Mann's.\"},\n   {\"ref\": \"MON:1492\", \"status\": \"supports\",\n    \"note\": \"Mo\\u2018in, Farhang-e Fārsī (MON_part1.txt lines 59508-59517): 'داو: (ا.) نوبت بازی (شطرنج، برد و مانند آن)، نوبت قمار. نوبت تیراندازی ... دعوی کاری، ادعای امری.' followed by a second homonym 'داو: (- دای) (ا.) هر چینه و رده ... از دیوار گلی'. Mo\\u2018in gives the meanings the chart gives but no etymological tag; the OCR carries no page numerals, so p.1492 itself could not be re-checked.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *dab (lines 3873-3914)\", \"stance\": \"contradicts\",\n    \"note\": \"'NWIR: (+ *fra-) NP farēftan/farēb- \\u2018to deceive\\u2019' \\u2014 the New Persian outcome of this Iranian root is farēb; Cheung records no dāv.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\",\n    \"note\": \"grep of HRN.txt for 'dāv'/'dav ' produces no headword for the gambling word; Horn does not derive it.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\",\n    \"note\": \"no entry for dāv (grep of HUB.txt).\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsī s.v. داوطلب / داوطلبانه\", \"stance\": \"supports\",\n    \"note\": \"Mo\\u2018in and the surrounding entries (MON_part1 lines 13124, 15767) use داوطلب in the modern sense 'candidate, volunteer', confirming the compound and its meaning.\"}\n ]\n})\n\nN.append({\n \"id\": 15, \"lang\": \"Latin\", \"words\": \"damnum\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Latin damnum 'loss, damage, fine' goes back to *dap-no-m, a -no- derivative of the same base as daps, dapis 'sacrificial banquet, expenditure', \"\n   \"with the regular loss of the intervocalic p before n (*dapnom > damnum, cf. somnus < *swep-no-). Its original sense is 'outlay, expenditure', which is also that of \"\n   \"the exact Greek cognate \\u03b4\\u03b1\\u03c0\\u03ac\\u03bd\\u03b7 'expense', and it narrowed in Roman legal language to 'loss entailing liability, fine' (already in the Twelve Tables). \"\n   \"Pokorny gives it under the p-extension dāp-/dǝp- of the root of this page, Watkins under 'dap-', Klein s.v. damn; Ernout-Meillet warn only against the popular \"\n   \"association with dare ('aucun rapport n'est senti en latin entre damnum et dare'), which does not touch the *dap- etymology. Nourai's gloss 'damage, harm (from a strike)' \"\n   \"adds the 'strike' notion from Mann's merged root; the sense is really 'expenditure, loss'.\"),\n \"derivation_fa\": (\"لاتین damnum «زیان، خسارت، جریمه» از *dap-no-m است، ساختِ اسمی با پسوندِ -no- از همان ستاکِ daps «خوانِ قربانی، هزینه»، با افتادنِ قاعده‌مندِ p پیش از n \"\n   \"(مانند somnus از *swep-no-). معنای نخستینِ آن «هزینه، خرج» بوده \\u2014 همان معنای همتای دقیقِ یونانی‌اش \\u03b4\\u03b1\\u03c0\\u03ac\\u03bd\\u03b7 \\u2014 و در زبان حقوقیِ روم به «زیانِ موجبِ ضمان، جریمه» محدود شده است (از الواح دوازده‌گانه). \"\n   \"پوکورنی آن را ذیل گسترشِ پ‌دارِ dāp-/dǝp- همین ریشه آورده، واتکینز ذیل *dap-، و کلاین ذیل damn. ارنو\\u2013مِیه تنها هشدار می‌دهند که پیوندِ عامیانهٔ damnum با dare در لاتین احساس نمی‌شده، که به اشتقاقِ *dap- آسیبی نمی‌زند. \"\n   \"افزودهٔ نورایی («از ضربه») از ریشهٔ درهم‌آمیختهٔ مان می‌آید؛ معنای اصلی «خرج، زیان» است. در مجموع ادعای او درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/damn\"],\n \"ref_check\": [\n   {\"ref\": \"AHD;1511\", \"status\": \"supports\",\n    \"note\": \"(the book prints the ref with a semicolon: 'AHD;1511'.) Watkins 1985 line 360: 'dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for reparation), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, INDEMNIFY, (INDEMNITY). [In Pok. dā- 175.]'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.176-177 (POK_01 leaf 187)\", \"stance\": \"supports\",\n    \"note\": \"'lat. daps \\u201e(Portion) Mahl, Schmaus\\u201c ... damnum \\u201eVerlust, Schaden, Nachteil, Geldbuße\\u201c, damnōsus \\u201everderblich\\u201c (*dap-no- : \\u03b4\\u03b1\\u03c0\\u03ac\\u03bd\\u03b7)'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. damnum (LAT.txt lines 15767ff.)\", \"stance\": \"partial\",\n    \"note\": \"'damnum, -i n.: dommage, perte, dépense. S'oppose à lucrum ... Quoi qu'on en dise parfois, aucun rapport n'est senti en latin entre damnum et dare.' Ernout-Meillet confirm the sense 'dépense/perte' but caution against the do- etymology; they do not contest *dap-.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. damn (KLN_1966.txt line 10279)\", \"stance\": \"supports\",\n    \"note\": \"'L. damnare ... fr. damnum, \\u2018harm, loss\\u2019, which stands for *dap-nom and orig. meant \\u2018expenditure\\u2019, and is rel. to daps ... All these words prob. derive fr. I.-E. base *dap-, a -p-enlargement of I.-E. base *dā-, *dai-, *dī-, *də-.'\"},\n   {\"src\": \"LEW\", \"where\": \"Walde-Hofmann (LEW_1910.txt)\", \"stance\": \"silent\",\n    \"note\": \"grep for 'damnum' in the 1910 scan returned no usable hit (the D fascicle is missing from this OCR).\"}\n ]\n})\n\nN.append({\n \"id\": 16, \"lang\": \"English\", \"words\": \"damn, damage, condemn, indemnify\", \"verdict\": \"confirmed\",\n \"derivation\": (\"All four are Latin-via-French: damn < ME damnen < OF damner/dampner < L. damnāre 'to condemn, cause loss'; damage < OF damage (mod. dommage) \"\n   \"< Vulgar Latin *damnāticum; condemn < L. condemnāre (com- intensive + damnāre), reshaped in Middle English after the Latin spelling; indemnify < L. indemnis \"\n   \"'unhurt' (in- 'not' + damnum, with the regular Latin vowel weakening a > e in the second syllable of a compound) + -fy. Klein sets out exactly this set under damn. \"\n   \"The silent -n of damn/condemn is the Latin -mn- kept in spelling after French had lost it.\"),\n \"derivation_fa\": (\"هر چهار واژه از لاتین و از راه فرانسه‌اند: damn از انگلیسی میانه damnen و فرانسهٔ کهن damner/dampner از damnāre لاتین؛ \"\n   \"damage از damage فرانسهٔ کهن (dommage امروزی) از لاتینِ عامیانه *damnāticum؛ condemn از condemnāre لاتین (پیشوندِ تأکیدیِ com- + damnāre) که املای انگلیسی میانه‌اش را بعداً به لاتین نزدیک کردند؛ \"\n   \"و indemnify از indemnis لاتین «بی‌آسیب» (in- نفی + damnum، با تضعیفِ قاعده‌مندِ a به e در هجای دومِ ترکیب) به‌علاوهٔ پسوندِ -fy. \"\n   \"کلاین دقیقاً همین مجموعه را ذیل damn آورده است. «ن» خاموشِ damn و condemn بازماندهٔ خوشهٔ -mn- لاتین در املاست. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/damn\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins index (lines 1409, 1389, 1676): 'DAMAGE dap- DAMN dap- DAMNIFY dap-', 'CONDEMN dap-', 'INDEMNIFY dap- INDEMNITY dap-' \\u2014 all four of Nourai's English words are filed under dap- in the AHD appendix.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. damn, damage, indemnify (lines 10279, 10266, 19147)\", \"stance\": \"supports\",\n    \"note\": \"'damage, n. \\u2014 ME., fr. OF. damage (F. dommage), fr. VL. *damnaticum, fr. L. damnum'; 'damn ... fr. OF. damner, dampner (F. damner), fr. L. damnare'; 'indemnify ... fr. L. indemnis, \\u2018unhurt, uninjured\\u2019, fr. in-, \\u2018not\\u2019, and damnum'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\",\n    \"note\": \"no locatable 'Damn' headword line in this OCR (grep '^Damn' empty); nothing recorded either way.\"}\n ]\n})\n\nwith io.open('data/verification/page-108.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint(\"wrote\", len(N), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk108.py && python3 -m json.tool data/verification/page-108.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 108",
 "description": "Write and validate page-108 verification"
}
```


### [2026-09-05T17:37:04.138Z] TOOL RESULT

```
wrote 16 nodes
JSON OK
nodes verified: 16/16
node verdicts: {'disputed': 3, 'confirmed': 9, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 5, 'supports': 15, 'not_checked': 1}
books consulted: {'partial': 5, 'supports': 24, 'silent': 13, 'contradicts': 4} | by book: {'KLN': 8, 'POK': 6, 'WLD': 4, 'MON': 4, 'CHEUNG': 4, 'HUB': 3, 'HRN': 3, 'ARY': 2, 'SKT': 2, 'SYN': 1, 'IEC': 1, 'PHD': 1, 'NYB': 1, 'DEV/PHN': 1, 'WEB/FSD': 1, 'BRT': 1, 'KNT': 1, 'LAT': 1, 'LEW': 1}
```


## [2026-09-05T17:37:11.795Z] TOOL CALL #65: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/page-108.json; git status --short | head -20",
 "description": "Confirm output file and git status"
}
```


### [2026-09-05T17:37:11.846Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66355 Sep  5 13:37 /home/sfmqrb/git/rishe/data/verification/page-108.json
 M data/verification/sources/web/index.jsonl
?? data/verification/page-108.json
?? data/verification/sources/web/18da60ec4a0e2821.txt
?? data/verification/sources/web/196c8250a01f8342.txt
?? data/verification/sources/web/22664546d4c2399f.txt
?? data/verification/sources/web/2c4e9682f4b18a5b.txt
?? data/verification/sources/web/3a3b6d7497c1e1f1.txt
?? data/verification/sources/web/3c0c859d79aff9b2.txt
?? data/verification/sources/web/4ee49e29ff4d36cd.txt
?? data/verification/sources/web/5bfe55a5ce8921a9.txt
?? data/verification/sources/web/6c9085bc41e57c54.txt
?? data/verification/sources/web/77d36874687f4822.txt
?? data/verification/sources/web/927eda0ce5233ae6.txt
?? data/verification/sources/web/9f1c56c359bf99e7.txt
?? data/verification/sources/web/c41ec9c4ce5ac1df.txt
?? data/verification/sources/web/d6937d5cb7398b19.txt
?? data/verification/sources/web/d9acf167e2a97dd9.txt
?? data/verification/sources/web/e546ea4c1a33db8f.txt
```


## [2026-09-05T17:37:26.462Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deh%E2%82%82y-' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/t%C4%ABdiz' \\\n 'https://www.etymonline.com/word/tide' \\\n 'https://www.etymonline.com/word/demon' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eb%CA%B0-' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/dabH-' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%88%D8%B7%D9%84%D8%A8' \\\n 'https://www.etymonline.com/word/damn' ; do\n echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 108, root Da 1 verification' 2>&1 | tail -2; done",
 "description": "Archive remaining cited URLs",
 "timeout": 600000
}
```


### [2026-09-05T17:37:30.346Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deh%E2%82%82y-
/home/sfmqrb/git/rishe/data/verification/sources/web/61badcdc6116e72d.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/t%C4%ABdiz
/home/sfmqrb/git/rishe/data/verification/sources/web/bc1cdba3b3bcd5a4.txt
### https://www.etymonline.com/word/tide
/home/sfmqrb/git/rishe/data/verification/sources/web/c425735ee2297282.txt
### https://www.etymonline.com/word/demon
/home/sfmqrb/git/rishe/data/verification/sources/web/dc8c1c13a291ce4e.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eb%CA%B0-
/home/sfmqrb/git/rishe/data/verification/sources/web/0f511b241661b6ee.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/dabH-
/home/sfmqrb/git/rishe/data/verification/sources/web/489eaf3d6f8b2883.txt
### https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%88%D8%B7%D9%84%D8%A8
/home/sfmqrb/git/rishe/data/verification/sources/web/9c061edf0c652022.txt
### https://www.etymonline.com/word/damn
/home/sfmqrb/git/rishe/data/verification/sources/web/2ce147dc8ee8c372.txt
```


## [2026-09-05T17:37:34.625Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 61badcdc6116e72d bc1cdba3b3bcd5a4 0f511b241661b6ee 489eaf3d6f8b2883 9c061edf0c652022; do echo \"### $f  ($(wc -c <$f.txt) bytes)\"; head -c 400 $f.txt | tr '\\n' ' '; echo; done",
 "description": "Spot-check archived wiktionary pages"
}
```


### [2026-09-05T17:37:36.372Z] TOOL RESULT

```
### 61badcdc6116e72d  (4439 bytes)
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deh%E2%82%82y- FETCHED: 2026-09-05T17:37:28Z STATUS: 200 TITLE: Reconstruction:Proto-Indo-European/deh₂y- - Wiktionary, the free dictionary  Reconstruction:Proto-Indo-European/deh₂y- - Wiktionary, the free dictionary    Jump to content    Main menu    Main menu   move to sidebar   hide    Navigation   Main page   Community 
### bc1cdba3b3bcd5a4  (5519 bytes)
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/t%C4%ABdiz FETCHED: 2026-09-05T17:37:28Z STATUS: 200 TITLE: Reconstruction:Proto-Germanic/tīdiz - Wiktionary, the free dictionary  Reconstruction:Proto-Germanic/tīdiz - Wiktionary, the free dictionary    Jump to content    Main menu    Main menu   move to sidebar   hide    Navigation   Main page   Community portal   Requested entr
### 0f511b241661b6ee  (9480 bytes)
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eb%CA%B0- FETCHED: 2026-09-05T17:37:29Z STATUS: 200 TITLE: Reconstruction:Proto-Indo-European/dʰebʰ- - Wiktionary, the free dictionary  Reconstruction:Proto-Indo-European/dʰebʰ- - Wiktionary, the free dictionary    Jump to content    Main menu    Main menu   move to sidebar   hide    Navigation   Main page   Communit
### 489eaf3d6f8b2883  (160 bytes)
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/dabH- FETCHED: 2026-09-05T17:37:29Z STATUS: -1 TITLE:   FETCH FAILED: HTTP Error 404: Not Found
### 9c061edf0c652022  (2627 bytes)
URL: https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%88%D8%B7%D9%84%D8%A8 FETCHED: 2026-09-05T17:37:30Z STATUS: 200 TITLE: داوطلب - Wiktionary, the free dictionary  داوطلب - Wiktionary, the free dictionary    Jump to content    Main menu    Main menu   move to sidebar   hide    Navigation   Main page   Community portal   Requested entries   Recent changes   Random entry   Help   Glossar
```


## [2026-09-05T17:37:40.676Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '1,200p' 9c061edf0c652022.txt | grep -A5 -i \"persian\\|etymolog\" | head -30",
 "description": "Check داوطلب archived content"
}
```


### [2026-09-05T17:37:40.729Z] TOOL RESULT

```
 Persian 

 Toggle Persian subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
--
 Persian
 [ edit ] 

 Persian Wikipedia has an article on: داوطلب 

 Wikipedia fa 

 Etymology
 [ edit ] 

 From داو ( dâv , “ ( gambling ) move, turn at play ” ) +‎ طلب ( talab , “ to seek ” ) , originally a gambling term ("one who seeks his turn").

 Pronunciation
--
 Categories : Persian compound terms 
 Persian terms with IPA pronunciation 
 Persian lemmas 
 Persian nouns
```


## [2026-09-05T17:37:49.322Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nimport json,io\np='data/verification/page-108.json'\nd=json.load(open(p,encoding='utf-8'))\nn=[x for x in d['entries'][0]['nodes'] if x['id']==13][0]\nn['sources']=[\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eb%CA%B0-\"]\nn14=[x for x in d['entries'][0]['nodes'] if x['id']==14][0]\nn14['derivation'] += (\" (Wiktionary's داوطلب entry gives the same analysis of the compound: 'From داو (dâv, ‘(gambling) move, turn at play’) + \"\n  \"طلب (talab, ‘to seek’), originally a gambling term (“one who seeks his turn”)' — confirming Nourai's reading of the compound while saying nothing about the PIE root.)\")\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write('\\n')\nprint('ok')\nEOF\npython3 -m json.tool data/verification/page-108.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 108",
 "description": "Fix dead source URL and re-validate"
}
```


### [2026-09-05T17:37:51.266Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 16/16
node verdicts: {'disputed': 3, 'confirmed': 9, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 5, 'supports': 15, 'not_checked': 1}
books consulted: {'partial': 5, 'supports': 24, 'silent': 13, 'contradicts': 4} | by book: {'KLN': 8, 'POK': 6, 'WLD': 4, 'MON': 4, 'CHEUNG': 4, 'HUB': 3, 'HRN': 3, 'ARY': 2, 'SKT': 2, 'SYN': 1, 'IEC': 1, 'PHD': 1, 'NYB': 1, 'DEV/PHN': 1, 'WEB/FSD': 1, 'BRT': 1, 'KNT': 1, 'LAT': 1, 'LEW': 1}
```


## [2026-09-05T17:38:15.960Z] AGENT

Page 108 (book p. 78) verified — `data/verification/page-108.json`, 0 PROBLEM lines.

**Counts** — 1 entry, root `confirmed`; nodes 16/16: 9 confirmed, 3 plausible, 3 disputed, 1 transcription_suspect. Ref checks: 15 supports, 5 partial, 1 not_checked. Books consulted: 24 supports, 5 partial, 4 contradicts, 13 silent.

**Disputed / flagged**

- **#1 Sanskrit `dhâra` "sword blade"** — disputed. Skt. dhā́rā has initial *dʰ-*, impossible from PIE *deh₂(y)-; Mayrhofer/Lubotsky derive it from *dʰerh₃-/*dʰenh₂- (= dhā́rā "stream"). Nourai lifted it from Mo'in's footnote at BQT:904 and re-attached it to the wrong root. `dâtra` itself is confirmed (Pokorny 175, WP I 763, Buck 8.33).
- **#3 Persian `bî-das-tar` "beaver"** — disputed. "Without sickles" is Nourai's reshaping of Mo'in's own folk etymology bī + dast + arr(e) "saw" (so Dehkhoda and Iranica s.v. BEAVER). The oldest attestation is *vīdastar* (Ḥamza Eṣfahānī via Bīrūnī, Ṣaydana 142), which rules out bī- "without"; the inherited Iranian beaver word is Av. bawri-, MP bawrag, NP babr (Horn no. 181). `dâs` in the same node is confirmed (Pokorny prints "npers. dās 'Sichel'").
- **#12 IE box `Dabh, Dâbh, Dabhn, Dap`** — disputed. It is a verbatim copy of Mann IEC:129, which merges two roots modern scholarship keeps apart: *dʰebʰ- "harm, deceive" (Pokorny 240; Cheung s.v. *dab → NP farēb/farēftan) and *dap- "apportion" (the p-extension of this page's own root, whence Lat. damnum). *dʰ-* cannot yield the *d-* of damnum. This also invalidates hanging #13/#14 on the same node as #15.
- **#7 Greek `děmos-keratos`** — transcription_suspect, `error_in: "book"`. The printed page (checked at 200 dpi, copied to `data/verification/sources/refs/ocr/BOOK/108.png`) does show "děmos-keratos ☞Kar 1"; correct is δημο-κρατ- / kratos (keratos = "horn"). Author's misprint, extraction faithful. dēmos, daimōn, epi-dēmos in the same node are all confirmed.
- **#13 Avestan `daivis`** — plausible, not a misreading: Bartholomae has daβvay-, nom. sg. **daiβiš** (Vd. 2.29, 19.43), but glosses it "name of a certain ailment", marks the etymology "Et.?", and the sense "deceit" comes only from the Pahlavi rendering frēftār. The real Av. noun "Betrug" is daβay-.
- **#14 Persian `dâv` / `dâv-talab`** — plausible. Meanings confirmed by Mo'in and Wiktionary; the PIE derivation rests solely on Mann, and Horn, Hübschmann and Cheung are silent or point elsewhere.

**Extraction errors:** none — every form, gloss, script and ref string in `page-108.json` matches the printed page, including the book's own typo `AHD;1511` on the Latin node. One cosmetic gap: the printed page draws an arrow from the Avestan box (#13) into a **blank, unlabelled box** at the right margin, which the extraction does not represent; it carries no content, so probably a layout artefact, but the owner may want to confirm.

**Reference page offsets pinned** (useful for later pages): Borhān-e Qāteʿ vol. 2 printed page = `BQT_v2_pages.txt` leaf + 540 (verified by the catchline "بقیه در صفحهٔ ۹۰۵" on leaf 364 = p. 904); vol. 1 leaf 553 = p. 333. Mann IEC p. 129 = `IEC.txt` leaf 86. All 14 web pages cited are archived under `data/verification/sources/web/`.
