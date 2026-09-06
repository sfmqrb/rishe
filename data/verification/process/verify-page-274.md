# Verification process log — verify-page-274


## [2026-09-06T21:10:40.772Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 274 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-274.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-274.json. Write /home/sfmqrb/git/rishe/data/verification/page-274.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 274` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:10:42.442Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T21:10:43.180Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:10:43.197Z] TOOL RESULT

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


## [2026-09-06T21:10:43.236Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-274.txt"
}
```


### [2026-09-06T21:10:43.249Z] TOOL RESULT

```
1	=== PDF page 274 (book page 244) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Koro / Koros : Koro: war, army, a large crowd. Koros: fighting, bullying, arrogance.  (refs POK:615; IEC:536)
4	#1 (parent #0) [Old Persian] refs=POK:615; KNT:175 | kâr 2, kâra 2 : war, army, people ; u-kâra : good army ☞Su 1
5	  #2 (parent #1) [Persian] refs=BQT:1575; HRN:237; MON:2957 | kâr- «کار ۲» : a prefix meaning war, army ; kâr-dâr «کاردار» : operations chief ☞Dher 1 ; kâr-vân «کاروان» : army, caravan ; kor-nâ «کرنا» : army horn ☞Nedo ; kâlenjâr «کالنجار» : fight | extra: کارزار؛ کلنجار
6	    #3 (parent #2) [French] refs=KLN:238 | caravane
7	      #4 (parent #3) [English] refs=None | caravan, van
8	#5 (parent #0) [Germanic] refs=AHD | harjaz, hari : army ; harjon : to raid ; harja-waldaz : army commander ; harja-bergaz : army hill ☞Bherg
9	  #6 (parent #5) [English] refs=None | Oliver, Herbert, Herman, Walter ; Harry ; Harold ; harbor
10	#7 (parent #0) [Indo-European] refs=IEC:538 | koruos : bitter, harsh
11	  #8 (parent #7) [Persian] refs=IEC:538 | karb «کرب» : sorrow | NOTE: MON:2932 claims this is derived from Arabic
12	  #9 (parent #7) [Germanic] refs=IEC:538 | hare, harwer, herwes : bitter
13	    #10 (parent #9) [Italian] refs=IEC:538 | garbo : bitter
14	--- entry 1 ---
15	ROOT Kor-ôna -> redirect to Sker 1
16	--- entry 2 ---
17	ROOT Koros -> redirect to Koro
18	--- entry 3 ---
19	ROOT koruos -> redirect to Koro
20	
```


## [2026-09-06T21:10:48.438Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-274.json && echo \"=== refs_online keys ===\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','KNT','BQT','HRN','MON','KLN','AHD','WLD','SYN','PHD','NYB','HUB','ARY','FVQ','AFM','PLA','SKT','WEB','FSD','CHEUNG','LKT','TTS','BRT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T21:10:50.096Z] TOOL RESULT

```
{
  "pdf_page": 274,
  "book_page": 244,
  "entries": [
    {
      "root": {
        "name": "Koro / Koros",
        "lang": "Indo-European",
        "refs": "POK:615; IEC:536",
        "gloss": "Koro: war, army, a large crowd. Koros: fighting, bullying, arrogance."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:615; KNT:175",
          "words": [
            {"translit": "kâr 2, kâra 2", "gloss": "war, army, people", "script": null},
            {"translit": "u-kâra", "gloss": "good army", "script": null, "see": ["Su 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1575; HRN:237; MON:2957",
          "words": [
            {"translit": "kâr-", "gloss": "a prefix meaning war, army", "script": "کار ۲"},
            {"translit": "kâr-dâr", "gloss": "operations chief", "script": "کاردار", "see": ["Dher 1"]},
            {"translit": "kâr-vân", "gloss": "army, caravan", "script": "کاروان"},
            {"translit": "kor-nâ", "gloss": "army horn", "script": "کرنا", "see": ["Nedo"]},
            {"translit": "kâlenjâr", "gloss": "fight", "script": "کالنجار"}
          ],
          "script_extra": "کارزار؛ کلنجار",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": "KLN:238",
          "words": [
            {"translit": "caravane", "gloss": null, "script": null}
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
            {"translit": "caravan, van", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "harjaz, hari", "gloss": "army", "script": null},
            {"translit": "harjon", "gloss": "to raid", "script": null},
            {"translit": "harja-waldaz", "gloss": "army commander", "script": null},
            {"translit": "harja-bergaz", "gloss": "army hill", "script": null, "see": ["Bherg"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Oliver, Herbert, Herman, Walter", "gloss": null, "script": null},
            {"translit": "Harry", "gloss": null, "script": null},
            {"translit": "Harold", "gloss": null, "script": null},
            {"translit": "harbor", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "IEC:538",
          "words": [
            {"translit": "koruos", "gloss": "bitter, harsh", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "IEC:538",
          "words": [
            {"translit": "karb", "gloss": "sorrow", "script": "کرب"}
          ],
          "note": "MON:2932 claims this is derived from Arabic",
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "Germanic",
          "refs": "IEC:538",
          "words": [
            {"translit": "hare, harwer, herwes", "gloss": "bitter", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Italian",
          "refs": "IEC:538",
          "words": [
            {"translit": "garbo", "gloss": "bitter", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Kor-ôna", "redirect": "Sker 1"},
      "nodes": []
    },
    {
      "root": {"name": "Koros", "redirect": "Koro"},
      "nodes": []
    },
    {
      "root": {"name": "koruos", "redirect": "Koro"},
      "nodes": []
    }
  ]
}
=== refs_online keys ===
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
CHEUNG MISSING
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
```


## [2026-09-06T21:11:20.942Z] TOOL CALL #4: Bash

```json
{
 "command": "ls tools/ && ls data/verification/ | head -30 && ls data/verification/sources/refs/ | head -60"
}
```


### [2026-09-06T21:11:20.989Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
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


## [2026-09-06T21:11:21.034Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T21:11:21.071Z] TOOL RESULT

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


## [2026-09-06T21:11:26.948Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','KNT','KLN','AHD','HRN','BQT','MON','WLD','SYN','BRT','PHD','NYB','HUB','ARY','SKT','FSD','WEB','LKT','LEW','LAT','SIN','HJB']:\n    v=d.get(k) or {}\n    print('==',k, '| offset:', v.get('page_offset'), '| local:', v.get('local_file'), '| hint:', (v.get('lookup_hint') or '')[:300])\n\""
}
```


### [2026-09-06T21:11:28.515Z] TOOL RESULT

```
== POK | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== IEC | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== KNT | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== KLN | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== AHD | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== HRN | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== MON | offset: None | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== WLD | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== SYN | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== BRT | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HUB | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== ARY | offset: printed page = pdf page + 1 | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== SKT | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== FSD | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== LKT | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== LEW | offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt | hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
== LAT | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt | hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
== SIN | offset: leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt | hint: Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sections are numbered with plant/product names in caps; grep the Persian/Chinese word or the page number.
== HJB | offset: leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt | hint: Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.
```


## [2026-09-06T21:11:32.855Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: kor\" POK_full.txt | head -20\necho \"--- POK_01 leaf 623 ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==624' POK_01.txt | head -60"
}
```


### [2026-09-06T21:11:34.669Z] TOOL RESULT

```
48081:Root / lemma: koro-s, kono-s 
--- POK_01 leaf 623 ---
```


## [2026-09-06T21:11:37.393Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '48075,48105p' POK_full.txt\necho \"=== leaves in POK_01/02/03 ===\"\nfor f in POK_01 POK_02 POK_03; do echo -n \"$f: \"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f.txt; done"
}
```


### [2026-09-06T21:11:39.026Z] TOOL RESULT

```
eagle (as black bird?)", (common gutturals k- >^- Celtic Baltic), shqiptar^ eagle man", 
shqip^ clear, fluently ". 

References: WP. I 457, Trautmann 299. 
Page(s): 614-615 

Root / lemma: koro-s, kono-s 

Meaning: war, warrior 

Material: 1. without formant -io-, -Ja-. Lithuanian Raras^\Nar, fight" and lengthened grade 

Old pers. Rara-rc\. " war people, army; people", npers. Rar-zar' battlefield ". 

2. Gr. Koipavot; (from *Koipovo(;) " military leader, king, master, mister" (derivative from 
*KoTpo(; from *K6pjO(; with formants -no-, also Old Icelandic herjann^ father of the army " as 
epithet of Odins from harja-^ army " from; Koipavsu) " command; rule ", Koipavia "power, 
rule", compare of the unadjusted *KoTpo- EN as Koip6|jaxo(; (Boisacq s. v.); 

Middle Irish cuirem. "troop, multitude, crowd, bulk, mass", gall. 777-, Petru-corii 
Volkernamen ("die drei-, vierstammigen"); 

Gothic harjis. Old Icelandic herr. Old English here^ army ", Old High German Old Saxon 
heri^ army, bulk, mass", PN Old Germanic Hari-gasf/ (Dat), perhaps god"s name (Meckel 
KZ. 60, 284); 

Lithuanian kar/as' army", kare'\Nar, fight", /ra/ys "warrior", Latvian kar's '\Nar, fight, army 
", Old Prussian /ra/y/is (consigns kragis) " army ", caryawoytis kVk. Sg. "military parade, 
military march"; 


=== leaves in POK_01/02/03 ===
POK_01: 363
POK_02: 433
POK_03: 429
```


## [2026-09-06T21:11:44.260Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '48105,48125p' POK_full.txt\necho \"=== POK_02 leaf 271 (p.615?) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==272' POK_02.txt | head -70"
}
```


### [2026-09-06T21:11:45.830Z] TOOL RESULT

```
compare also above kar-1S. 530, where Balto Slavic examples can also belong here. 

References: WP. I 353, 462, Trautmann 118. 
Page(s): 615-616 

Root / lemma: kos(e)lo- 

Meaning: hazel 

Material: Latin corulus^ a hazel-tree, filberttree ', colurnus {*corulinos) " of the hazel, of 

hazel-wood '; 

Old Irish coll, acymr. coll etc. ' hazel' (also gall. Coslo-\n EN); (common Celtic alb. 
abbreviation), [common Celtic si- > II-] 

Old High German hasal(a). Old English haesel. Old Icelandic haslm. " hazel'. Old High 
German hesllfn. Old English hseslen^ of hazel-wood '; 

=== POK_02 leaf 271 (p.615?) ===
,  WH.  I  314,  859.
jco  kOf  kak(k)-f  ku(r)kur-   u.  dgl.   als   Nachahmung   des  Naturlautes  der Hühner;  Worte  ohne  nachweisbare  ältere  Geschichte.
I.  Gr.  y,aycxdßr]  f.,  Kaytytaßig  f.  ,Rebhuhn',  ytax-naßll^siv  vom  Naturlaut  der Rebhühner  (ebenso  das  entlehnte  lat.  cacabäre),  xaxxd^etv  , gackern';
lat.  cacilläre  ,gackern  (von  der  Henne)';
ndd.  kakkeln  ,gackern',  nl.  kokkelen  ,kollern  (vom  Hahn)',  woneben ahd.  gackizön  ,gackern  (von  der  ein  Ei  legenden  Henne)',  nhd.  gackern, dial.  gaggezen,  nhd.   Gockel  (s.  auch  unter  ghegh-).
II.  Lat.  coco  coco  ,Naturlaut  der  Hühner'  (Petron  59,  2),  franz.  coq  ,Hahn', dän.  kok,  schwed.  mdartl.  kokk  ,Hahn',  anord.  (afrz.  Lw.)  kokr,  ags.  cocc, nl.  alt  cocke  ds. ;  aksl.  kokotT>  ,Hahn',  kokoh  ,Henne',  russ.  kokotdth ,gackern'  usw.
III.  Ai.  kurkuta-,  kukkuta-  m.  ,Hahn',  kukkubha-  m.  (mind.  für  */cwr- kubha-)  , Fasan' ;  lat.  cücurriö,  -Ire  ,kollern'  (vom  Hahn),  cücuru  Inter- jektion; nhd.  kikeriki  (älter  kükerukü,  kükerlüküh),  md.  kuckern,  kockern, köcken  ,krähen^;  lit.  kakarykü  ,kikeriki',  klruss.  usw.  kukuriku  ds.,  serb. kukitrijeSem-,  -ijekati,   russ.    kukorekath   usw.   ,krähen',   gr.   xovql^w  ds.
IV.  Gr.  y,ULQQog,  y,Ly,y.ög  ,Hahn'  Hes. ;  osk.  cicirrus,  Cognomen  des  Messius, wohl  , Kampfhahn'.
WP.  I  455  f.,  WH.  I  126,  212,  242,  300.
koksä  jKörperteilbenennung'  (arisch  auch  *kokso-s).
Ai.  kdk§ä  f.,  kaksa-  m.  , Achselgrube,  Gurtgegend  der  Pferde',  av.  kasa- m.  , Achsel'  (erweist  -ks-)]
lat.  coxa  f.  , Hüfte';
air.  coss  f.  ,Fuß',  abrit.  Aq'/svrd-Y.o^og  etwa  ,  Weiß  fuß'  (aber  cymr.  coes ,Bein'  ist  aus  dem  Lat.  entlehnt) ;
ahd.  hähsina  ,Kniebug  des  Hinterbeins',  mhd.  hehse,  nhd.  Hachse,  Hesse, bair.  Haxn.
WP.  I  456  f.,  WH.  I  188,  283,  858.
kolQ-  :  klö-  , spinnen'  ?
Gr.  y,Xd)d-cji),  nXcodKü)  ,spinne',  xAw^w  eig.  ,die  Spinnerin',  xkiüOxrjQ,  -fJQog ,Faden,  Spindel';
39*
612
lat.  colus
```


## [2026-09-06T21:11:50.190Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"koro-s\" POK_02.txt | head\necho \"---\"\nawk 'BEGIN{RS=\"\\f\"} /koro-s/{print \"LEAF \" NR; print; exit}' POK_02.txt | head -60"
}
```


### [2026-09-06T21:11:52.015Z] TOOL RESULT

```
4321:koro-s,  korio-s  ,Krieg,  Kriegsheer*;  korio-no-s  , Heerführer*.
---
LEAF 276
w.)  kos^  ,AmseF.  —  Meillet  legt  (MSL  18,  171)  unter  An- nahme von  idg.  k-  (das  in  kosi,  wegen  des  folgenden  s  als  k  festgehalten
r
615
sei)  eine  Schallwurzel  kop-  zugrunde :  ksl.  so'pg  ,spiele  die  Flöte*,  abg.  so^phch ^(xblrixYiq^ ,  russ.  sofUh   ,keuclien'    usw.    und   ai.    sdb-d-a-    m.  ,Laut,   Schall, Rede,  Wort*  (zum  -cZ-Suffix  in  Worten  für  Lärm  s.  Brugmann  II*  1,  467), Sdpati  ,verflucht',  -te  ,beteuert,  gelobt*. WP.  I  457,  Trautmann  299.
iorkä  (krokä?),  -Ja  ,Kies,  Kiesel*?
Ai.  sdrkarä  {sdrkara-h)  ,Gries,  Kies,  Geröll,  Sandzucker*; gr.   y.Q6y.ri,    yiQOiidXT]   ,Kieselstein* ;    vielleicht   hat   ein   HoQy.dXa  :  sarkarä erst  nach  x^^xw  ,schlage*  Umstellung  zu"  TCQOxdXrj  erfahren. WP.  I  463.
kormen-  ,Wiesel*,  s.  oben  unter  6.  ker-,
iormno-,  krmno-  ,ätzende,  beißende  Flüssigkeit,  Lauge,  Harn*.
Mhd.  hurmen  , düngen*  (ursprüngl.  wohl  mit  Jauche),  nhd.  harrij  härm, ahd.  karan  ,Harn*;
lit.  Sdrmas  ,Asclienlauge*,  lett.  särms  ,Lauge*,  apr.  (mit  der  Ablautstufe von  mhd.  hurmen)  sirmes  (für  *sirmis)  , Lauge*.
WP.  I  463,  Trautmann  300.
kormo-  ,Qual,  Schmerz,  Schmach*.
Av.  fsardma-  m.  , Scham  (gefühl  vor)*,  mpers.  sarm  ds. ;
aisl.  harmr  ,Betrübnis,  Kummer,  Harm,  Kränkung*,  ags.  hearm  m. jKummer,  Schmerz,  Schade*,  as.  härm  , Schmerz,  Kränkung*,  mnd.  härm , Schmerz*,  ahd.  har{a)m  ,Leid,  Harm,  Schimpf*,  nhd.  Harm,  ags.  hearm, as.  härm  »schmerzlich,  verletzend*;
abg.  sram^  , Scham*.
WP.  I  463,  Trautmann  299.
koro-s,  korio-s  ,Krieg,  Kriegsheer*;  korio-no-s  , Heerführer*.
1.  Ohne  formantisches  -to-,  -la- :  lit.  käras  , Krieg*  und  dehnstufig  apers. kära-  m.  ,Kriegsvolk,  Heer;  Volk*,  npers.  kär-zar  , Schlachtfeld*.
2.  Gr.  ycoigavog  (aus  *KoiQOvog)  ,Heerführer,  König,  Herr*  (Ableitung  von *y(,oTQog  aus  ^xögiog  mit  Formans  -no-',  ebenso  aisl.  herjann  , Heervater* als  Beiname  Odins  von  harja-  ,Heer*  aus;  ytoLgaviw  ,befehlige;  herrsche*, %OLQavla  , Herrschaft*,  vgl.  vom  unerweiterten  *xor(>o-  EN  wie  KoLgöfxaxog (Boisacq  s.  v.) ;
mir.  cuire  m.  , Schar,  Menge*,  gall.  Tri-,  Petru-corii  Völkernamen  (,die drei-,  vierstämmigen*);
got.  harjis,  aisl.  herr,  ags.  here  ,Heer*,  ahd.  as.  herl  ,Heer,  Menge*,  PN altgerm.  Hari-gasti  (Dat.),  vielleicht  Göttername  (Neckel  KZ.  60,  284);
616
lit.  kärias  ,HeerS  häre  ,KriegS  harys  ,KriegerS  lett.  har'^  ,Krieg,  Heer', apr.  kargis
```


## [2026-09-06T21:11:59.102Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^koro\" IEC.txt | head -20\necho \"--- koru ---\"\ngrep -n \"^koru\" IEC.txt | head -20\necho \"--- korios ---\"\ngrep -n \"^kori\" IEC.txt | head -20"
}
```


### [2026-09-06T21:11:59.176Z] TOOL RESULT

```
7670:koron-, see koróon-
7696:korono- 'curve-'; Mir cf. corann, Ir. corann, f. ‘crown, garland’; W cf. coryn “crown of head" beside caran, f. id.
7697:korops-, korpor-, cf. kerp- (kerep-) and krp- Skt. cf. karparah ‘skull, tortoise-shell; cup, bowl; Arm. karap and karapn, gs karapin ‘skull
7698:koros (1) ‘skin, hide’. See korā Skt. cf. karkarah (queried, redup: “leather strap’); Lat. corius “leather whip, tawse, thong’; corium ‘hide; husk’; W cwr, pl. cy- roedd, m. ‘skin’, fr. *koros, -es-?); OCS kor, kora (shell, crust, rind', and com. SL); Li. kara ‘lime-bark’; LW in Finn. kuoria ‘shell, peel, husk’
7699:koros (2) ‘arrogance, rudeness, bullying, fighting’. (SI. & Balt. ambig. w. influence of type kar-, q.v.) Gk. kóros ‘arrogance’; OCS korü ‘contumely’; Cz. cf. kory ‘stiff; Li. káras ‘war’; Latv. cf. karš, id.
--- koru ---
7722:korubho, ið (?) “bend, turn, depart". (Variant: korumbh-?) ON hörfa (retire, retreat’; Blg. korübja se ‘bend, stoop’. (For Gk. korüpto “butt w. the head”, cf. Koru-, Ker- ‘head’. Cf. however Phryg. korübantes *whirling dancers")
7723:koruos, ə (1) fibre, flax, hair’. Cf. WP I, 356 & 449. Ambig. Cf. Koruos (3), koruos (2) Myc. cf. koura (queried: adj. ... of cloth- lengths); koureja (epithet relating to wooD; Gk. cf. kouríx, adv. “by the hair; MHG har, OHG haro, gs *harwes, *harawes ‘flax’; ON horr, ds horvi, id.; Sw. hór, id.; Srb. korov ‘weed’ (7); Finn. LW karva ‘hair
7724:koruos (2) ‘bitter, harsh’. Ambig. Cf. Koruos (1) Per. karb ‘sad’; Ir. cf. corbaim, v. ‘waste, tor- ture, destroy, corrupt’; MHG hare, gs harwer; here, gs herwes ‘sharp, bitter, tart’; It. LW fr. Gmc. garbo ‘bitter’; Finn. LW karvas, id. (Iso- phonic: Nor. Sw. harv ‘harrow’; harve, harva, v. id. not E ‘harrow’, v. wh. is fr. OE hergian, cf. koros (2). G herb is of twofold origin: FK:EWDS, 17)
7725:koruos (3) ‘black’ Av kaurvō, id.; Gk. korós, id.; Lat. cf. corvus ‘crow’
--- korios ---
7673:koris ‘itch, scab, ringworm; biting insect". WP II, 576 Gk. kóris, gs eos, m. & f. ‘bug’; R kori, f., Ukr. kir ‘moth, measles’
7674:korið (koreið) (1) ‘annoy, tire, abuse’. Cf. karinaio & WP I, 353 Ir. coirim, coraim ‘tire, annoy’; OHG harjon ‘harry’; OE hergian, ON herja, id.; OCS korjo, iti “abuse; Cz. kofit ‘humiliate’; Pol. korzyc, id. W ceryddu, v. inf. ‘to reprove’ is ambig.
7677:korio (2) ‘give, put-. (Variants: koreió, kortið) Hitt. kariyami “yield; gratify’; Ir. cuirim ‘put’; OBr. cf. hebcorim, s. (privation'. See seque); W heb-gor, -gori, inf. ‘set aside’
7678:koriom, see koros (1)
7679:korios (1) ‘troop, band, flock, host. WP I, 462. Cf. kort-, korst- OPer. cf. kara- people, host; Hitt. cf. kuri- wanas (LW? 'governor"); Cypro-Minoan (que- ried) koiro- ‘flock’; Gk. cf. koíranos ‘captain’; Mir cuire ‘band, troop’; Gaul. (in names) corio-, Tri-, Petru-corii; Romanized Gmc. cha- rio-; Go. harjis ‘army’; OHG hari, heri, OE here, ON her, pl. herjar, id.; cf. also MHG harst, harsch “band, crowd’; Li. kare, f., kã- rias, m. ‘army’; Latv. karš, id.; OPr. kans ‘troop’
7688:korió — korsos
```


## [2026-09-06T21:12:08.124Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\n# map line -> leaf\nleaf=0\npos=0\nfor i,l in enumerate(lines,1):\n    if i in (7670,7679,7698,7699,7723,7724,7725,7688):\n        print(i,'leaf',leaf, '->approx printed p', (leaf-15)*2, (leaf-15)*2+1)\n    leaf += l.count('\\f')\nEOF"
}
```


### [2026-09-06T21:12:10.058Z] TOOL RESULT

```
7670 leaf 304 ->approx printed p 578 579
7679 leaf 305 ->approx printed p 580 581
7688 leaf 305 ->approx printed p 580 581
7698 leaf 305 ->approx printed p 580 581
7699 leaf 305 ->approx printed p 580 581
7723 leaf 306 ->approx printed p 582 583
7724 leaf 307 ->approx printed p 584 585
7725 leaf 307 ->approx printed p 584 585
```


## [2026-09-06T21:12:14.972Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==306{print \"=== LEAF 305 ===\"; print}' IEC.txt | head -40\necho\nawk 'BEGIN{RS=\"\\f\"} NR==308{print \"=== LEAF 307 ===\"; print}' IEC.txt | head -40"
}
```


### [2026-09-06T21:12:16.772Z] TOOL RESULT

```
=== LEAF 305 ===
ird". Cf. WP I, 413 Per. kalay ‘crow’; Lat. (ambig.) corvus, id.; Blg. cf. krag-uj 'sparrow-hawk'; Cz. krah-ujec, id.
kor- “harsh, hard; torture, torment’ Skt. kárjami ‘torment’; Oss. karz, adj. ‘strict’; Alb. cf. n-gardh, v. ‘stigmatize, brand’; ngardhë, f. ‘stigma’; Arm. korcem, kocem, v. (1) ‘beat; ON harka ‘harshness, hardness’; mod. harki ‘dearth’; harka, v. ‘rack, torment’; Du. cf. harkerig ‘stiff, awkward’. (Isophonic are: ON harka (1) ‘scrape’; Sw. harka ‘rake’; Du. (and G fr. LG) barken, v. id. ON also herkja ‘drag oneself along’; Norw. harke, v. ‘hawk, cough’)
koris ‘itch, scab, ringworm; biting insect". WP II, 576 Gk. kóris, gs eos, m. & f. ‘bug’; R kori, f., Ukr. kir ‘moth, measles’
korið (koreið) (1) ‘annoy, tire, abuse’. Cf. karinaio & WP I, 353 Ir. coirim, coraim ‘tire, annoy’; OHG harjon ‘harry’; OE hergian, ON herja, id.; OCS korjo, iti “abuse; Cz. kofit ‘humiliate’; Pol. korzyc, id. W ceryddu, v. inf. ‘to reprove’ is ambig.
535
Cf. kar-
korio (2) ‘give, put-. (Variants: koreió, kortið) Hitt. kariyami “yield; gratify’; Ir. cuirim ‘put’; OBr. cf. hebcorim, s. (privation'. See seque); W heb-gor, -gori, inf. ‘set aside’
koriom, see koros (1)
korios (1) ‘troop, band, flock, host. WP I, 462. Cf. kort-, korst- OPer. cf. kara- people, host; Hitt. cf. kuri- wanas (LW? 'governor"); Cypro-Minoan (que- ried) koiro- ‘flock’; Gk. cf. koíranos ‘captain’; Mir cuire ‘band, troop’; Gaul. (in names) corio-, Tri-, Petru-corii; Romanized Gmc. cha- rio-; Go. harjis ‘army’; OHG hari, heri, OE here, ON her, pl. herjar, id.; cf. also MHG harst, harsch “band, crowd’; Li. kare, f., kã- rias, m. ‘army’; Latv. karš, id.; OPr. kans ‘troop’
kork- (?) ‘scotch, scotched', etc. (kark-?) Arm. karkem ‘baffle; silence’; MHG hargen limp, hobble’; Li. cf. karksóti, inf. “hang around, be disconsolate, mope’
korkoros (variant of karkor-, q.v.) Gk. (Hes.) kórkora “a raucous bird’; (Cz. krá- kor ‘crowing, cackle’, etc. ambig. See karkor-)
korkos (1) ‘filth’. Cf. kurguos (1) Skt. kalkah, id.; Arm. (ambig.) kork, i-st.; MIr. cf. corc-ach ‘marsh’
korkos (korok-) (2) (demon, monster’. Cf. kark- Scythian cf. kórakos ‘demon’; Alb. cf. kark- in kark-zogé, usu. kaké-zogé *blindworm, slowworm'; Cz. krak *sea-monster'. (Skt. kar- kah, m. ‘crab’ is ambig. Cf. kark-)
korn- (kornt-) (?) *prickle? Skt. cf. kantah ‘thorn’; Romani karno, kanro, karo, id..; Arm. karn, Let ‘cardoon thistle’; Gk. (Sicilian) kórnos *butcher's broom’
kornks ‘crow’. Cf. korok- Gk. kórax, id.; Lat. cornix, gp cornicum, id.; Umb. curnaco, acc. sg. id. Cf. variants: Skt. karatah ‘crow’; Latv. karaks “jackdaw”; karnis ‘heron’
korðn-, korən- “edge, rim, border’. Cf. kor- and WP I, 413, II, 591 Per. karán, id.; Gk. koróne, id. (and ‘curve, crown’. LW in Lat. corona); Myc. cf. (queried)
thwart, cripple; be
korió — korsos
20
23
30
35
40
45
536
korono- 'curve-'; Mir cf. corann, Ir. corann, f. ‘crown, garland’; W cf. coryn “crown of head" beside caran, f. id.
korops-, korpor-, cf. kerp- (kerep-) and krp- Skt. cf. karparah ‘skull, tortoise-shell; cup, bowl; Arm. karap and karapn, gs karapin ‘skull
koros (1) ‘skin, hide’. See korā Skt. cf. karkarah (queried, redup: “leather strap’); Lat. corius “leather whip, tawse, thong’; corium ‘hide; husk’; W cwr, pl. cy- roedd, m. ‘skin’, fr. *koros, -es-?); OCS kor, kora (shell, crust, rind', and com. SL); Li. kara ‘lime-bark’; LW in Finn. kuoria ‘shell, peel, husk’
koros (2) ‘arrogance, rudeness, bullying, fighting’. (SI. & Balt. ambig. w. influence of type kar-, q.v.) Gk. kóros ‘arrogance’; OCS korü ‘contumely’; Cz. cf. kory ‘stiff; Li. káras ‘war’; Latv. cf. k

=== LEAF 307 ===
 cf. koura (queried: adj. ... of cloth- lengths); koureja (epithet relating to wooD; Gk. cf. kouríx, adv. “by the hair; MHG har, OHG haro, gs *harwes, *harawes ‘flax’; ON horr, ds horvi, id.; Sw. hór, id.; Srb. korov ‘weed’ (7); Finn. LW karva ‘hair
koruos (2) ‘bitter, harsh’. Ambig. Cf. Koruos (1) Per. karb ‘sad’; Ir. cf. corbaim, v. ‘waste, tor- ture, destroy, corrupt’; MHG hare, gs harwer; here, gs herwes ‘sharp, bitter, tart’; It. LW fr. Gmc. garbo ‘bitter’; Finn. LW karvas, id. (Iso- phonic: Nor. Sw. harv ‘harrow’; harve, harva, v. id. not E ‘harrow’, v. wh. is fr. OE hergian, cf. koros (2). G herb is of twofold origin: FK:EWDS, 17)
koruos (3) ‘black’ Av kaurvō, id.; Gk. korós, id.; Lat. cf. corvus ‘crow’
kos-, o-gde of kesð (2), q.v. R kosà (1) ‘tress’; Li. kasà, id.
kosolos (kosulos, koslos) ‘hazel’. WP I, 464
` Arm. cf. kayin, gs kayno, id.; Lat. corulus,
35
40
45
corylus, id.; Gaul. coslos, cosla, id.; OBr. cf. limn-collin, pl. -collou ‘lime-tree’; MIr. and Ir. coll, W coll ‘hazel’; Br. cf. kel-vez, Cor. coll- wedhen, id.; OHG hasal, id.; cf. hesilin, adj. ‘of hazel; OE hæsel ‘hazel’; Du. cf. hazel- noot *hazel-nut'; ON hasla, f. pl. hoslur ‘ha- zel'; Li. (?) kasula ‘cluster, bunch’. Cf. (?) Per. kahar ‘brown’
kosmä (komsā) ‘hair, tress’. Cf. kos, kes-, kos- Gk. kómē, id.; Lat. (LW fr. Gk.) coma, id.; OCS cf. kosmü ‘hair’; kosmatü ‘hairy’; Cz. kosma “lock, curl, shag’; R kosmà, id.; Latv. kosa (“mane”, fr. *komsa)
koso, ið ‘rake, comb, trim, scrape’. Cf. kes-,
539
kos-, kostos, (kaso) Skt. (ambig.) kasàmi (rub, scratch, scrape’. Cf. kas0); Gk. cf. kónnos (/beard', fr. *kosno-,
as zónnümi fr. *iðsn-), beside (?) kóas, Myc. .
kowo- (fleece, if fr. *kosu-); R cf. kos-ulja ((1) ‘plow’, fr. *kos-aulio, cf. Gk. aülax 'furrow'); Li. kasüs, Latv. kasus, s. ‘itch’; adj. *diggable' beside Li. kasaü, inf. kasyti ‘comb, scrape, graze, rake'; Latv. kasit, id. and Li. kasu, -ti “dig, mine’; Latv. kašas ‘scraps, scratchings', fr. *kosijàs, fpl.). (In sense of ‘touch’, SI. kos- derives fr. kas-, q. v.)
kostos, à, is (combings, fibre, grass, tress, bristle’. Cf. kes-, kos-, koso Gk. kóstos 'prickly-leaved spice-plant, burr or thistle’; kostai, pl. ʻa barbed fish'?); cf. Hes. kóstai, fpl. “barley? beside Gk. akosté, id.; kósta, npl. (perh. "linchpins"); Alb. kashtë ‘straw’; Ir. cuise ‘meadow-grass’; ON haddr ‘tress’ beside (e-gde) OE heorde ‘hards of flax’; Pol. cf. kost-rzewa ‘fescue’; Blg. koSC- riàva «timothy-grass'; Cz. cf. kostrbaty 'shag- gy’; koště, n. ‘broom for sweeping’; Li. cf. kastuvas ‘currycomb’. (LW in Lat. costus, costum ‘amōmum hirsutum, zedoary’, fr. Gk.). Here also prob. W. Cor. cos, f. ‘itch’
kosthios, (kost-) (?) ‘wood, stem, base, leg, bone”. Cf. WP I, 456 & 464 Skt. (alleged) kasthah (^wood, timber’: Hind. kath, Romani kast, id.); Hes. (Epirot? Illy- rian?) káston, n. id. (Athamantes — Hes.); Ir. cos, f. “leg, foot, stem, trunk'; OCS kosti, f. Cbone’ and com. Sl.)
kotəros, à (?) ‘scrap’ Arm. (ambig.) kotor, o-st. id.; OHG hadara (Cas G Hader); LW in Li. kadaras ‘rag’
koukos, à, ios ‘bend, twist, curl’. Cf. keuk-, kuk- & kük- Skt. cf. kocami, tr. (2) “bend, curve’; kočah, adj. ‘shrivelling’; cf. kucikah, a “an eel-like fish’; Olr. cúac ‘crooked’; MIr. coach f. lock of hair, plait, fold’; Cz. cf. kucera ‘curl
koulió ‘be round, form a circle, roll" See koulos (2) Br. küPa ‘get plump, get fat, get round’; Cz. kulit se, inf. ((rolP, tr); Ukr. kulyty, inf. ‘snuggle’
koulos, io (1) ‘pig’
kostos, a, is — krab-
20
25
30
35
40
45
540
Skt. kolah �
```


## [2026-09-06T21:12:34.910Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"kāra\\|kara-\" KNT.txt | sed -n 1,40p\necho \"=== leaf for p175 (=+15 -> 190) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==191' KNT.txt | head -50"
}
```


### [2026-09-06T21:12:37.069Z] TOOL RESULT

```
587:tarsatiy with Iran. tars- because of NPers. (0708, $ despite Av. drasaiti, from is-, both with IE Ж suffix -ske-; but Skt. trásati from "ireseti. 1 cartanaty: the c shows that a front vowel formerly 3 stood immediately after it; therefore car- from Ж *cer- from *ker-. 4 Karka, Gk. Каре, Kapuol; Elam. kur-ga-ap seems ' to have no evidential value. E | valrtaiyaty, if identical with Skt. variaye; see $ Lex. s.v. vart- for reff. ; | $32. Отр Persian ara seems to be established * in the following: E i By cognates in Skt. and Avestan: apataram, $ aparam, para, hamarana-, partaram, and the * verbal nouns -kara- and -bara- as second ele- ments of compounds. | $ By Elamite and other transcriptions: Arakadri $ (or Ark- ?), Arabäya, the final of Nabukudra- ° cara.
1247:$99. PAR. k AND é are found without further change in OP, in the following: pIE q-, in OP kāra- ‘people, army’, ef. Lith.
1254:pàr. root kar- ‘make, do’, OP pres. kunautzy, imf. pass. akariya, züra-kara- ‘evil-doer’; but *ker- in pres. inf. cartanaiy, *kér- in ucdram ^well- done, successful’, *be-kr- in perf. opt. caxriyd.
1331:q*e. On züra-kara ‘evil-doer’ from *zurah-kara-,
1481:Apparently the suffix -as- or -az- was in some forms replaced by -ah- where -ah- yielded an easler phonetic development. We may assume that raucabi$ is from raucah-bhi$, that the А became voiced before the voiced stop and was lost in OP, but in Ау. and Skt. was lost with an attendant change of the preceding vowel to 6. A similar replacement is seen in ztira’-kara- ‘evil- doer’, where the Л is lost before the voiceless stop; ef. Skt. manah-pait- ‘Lord of the Mind’.
1494:pIE gh: brazmaniya-, Uvárazmi-, игта-, züra-, zü- rakara-.
1563:dérantya-kara- ‘goldsmith’, to daranzya- ‘gold’.
1776:І. Attached to a verbal root, the ablaut grade of the root varying: kara- in compounds, u-céra-, küma-, Катёа-, gausa-, raga-, adv. daríam, drauga-, baga-, bara- and bāra- in compounds, zana- in compounds; less certain formations in d-baha- in daha-vaja, casa-, U-t&na-, u-tava-, gara- in batu-gara-, Vi-vdna-, varga- in hauma-varga-.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1785:Agents: baga- ‘dispenser, god’; drauga- ‘deceiver, the Lie’; arSti-bara- ‘spear-bearer’; züra-kara- ‘evil-doer’; dáraniya-kara- ‘gold-worker, gold- smith’,
1786:Passives: ha™-dugd- ‘im-pressed’ = ‘inscription’; pati-kara- ‘made thereto’ = ‘sculptured figure’; asa-bara- ‘horse-borne’.
1876:5169. Noun AND Apsective COMPOUNDS IN ОР, apart from phrasal adverbs (§191.1V), may have as prior element an inseparable adverb as in a- zsata- ,"u-cüra-, dus-iydra-, ham-arana- (8268); or a prepositional adverb, as in apa-dàna-, pati-kara- (5268); or a noun or adjective stem! They have as second element a noun or adjective stem, which may receive an additional suffix.
1877:Only compounds of stem + stem will be here discussed. Either stem may itself be a compound; either stem may already have one or more suffixes. The initial syllable of the first element, especially in adjectives, may show vriddhi or lengthening of the vowel, as in dáraniya-kara- ‘gold-worker’ to daranzya- ‘gold’; less often this appears in the sec- ond part, as in Baga-yadi- 'god-worshipping (month)’, where it is seen in both parts, and in asa-bàra- ‘horse-borne’, where it indicates passive meaning.
1894:hamarana-kara- ‘battle-making’; züra-kara- ‘evil- doing’; ddraniya-kara- 'gold-working'; ciyd- kara- ‘doing how much’, ava-kara- ‘doing that’.
2346:8201. THE IwTERROGATIVE-INDEFINITE PIE *g**o- /*q*i- occurs only sparingly іп ОР. Nsm. kaš- ciy ‘anybody’ is *q*o-s, Skt. kas, Av. kas-, + enci. -cly; asn. сі&-сїу ‘anything’ is *g%i-d, Gk. т, Lt. quid, + епо. -ciy: both with Median sandhi-de- velopment ($105). Enclitic -ciy is pIE *q*id, Skt. cid, Av. -cit, Lt. quid, etc. See also aciy, yaciy, Ка, -kaiy, сий, cina], ciytikara- in the Lexicon.
2800:IV. This pronoun as article occasionally pre- cedes its noun to attach to it an adjective or a genitive; there are these examples: DB 1.8 and DBa 12f hyà атахат iauma; DB 1.28 tyand mand айй, cf. DNa 21; DB 3.32 hya aniya kāra Parsa; DB 4.87f tyäm imatsam martiyanàm taumam; DB 5.12 tyamsém тай йат; DNa 56f hyd Auramaz- daha framünà; ПОЇ 12f hya тала mia Vistaspa
2819:ПІ. A descriptive adjective is likewise incor- porated within the clause, in DB 2.30f (and 2.50f) kāra hya hamiçiya mana лашу gaubataiy ‘the hos- tile army which does not call itself mine’; but such adjectives usually stand outside, as in DB 2.84 küram hamiciyam hya тапа naiy gaubdtaiy, cf. also DB 2.21, 3.86.
3444:9 агза : mand : рага : tya : ukāram 10 : uvaspam : vašnā : Auramazdaha : im 11 ām : dahyaum : dàrayàmiy : mam :
3551:S! avajaniyd, ef. Kent, JAOS 62.274. 6 тагал KT, with omission of the d*. 55 patiydeahyaty Jn., KT. % Sika- lya]uvati$ KT. 6% abrieris RI, WB, Jn., KT. 606. {ү Ja., KT, for Rl's eéibeis[e]a; ef. Lex. for lit. on various normalizations and interpretations. ® Ву. MSLP 23.182-3 finds an haplography and would read adiná : adam |: patiyübaram : adam] : kāram. ™ Upadar- mahyà RI., Wb. KIA; Upadara*mahya Opp. Méd., Hüsing, KT, Tm.; U"padara^mahyà HK.
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3645:8 kāram : hamiciyam KT, without R18 уат between the words, 89 Г сўе legible, acc. to Cameron, séttling old disputes; [ujcSuam KT, -Feasma Jn., ucasma Wb., ucasam Kent Lg. 19.225-6; cašma Bv. TPS 1045.53-4, after Jn. IF 25.182-3 (cf. conj. of Spiegel, Altp. Keilinsch. 21n, 218), whence саат Kent; see Lex. s.v. caša-. 0-98 Except as noted, the supplements are those of WB and KT. * RI. records hya as visible before mand pila; but KT omit without comment, ** avahar{[+] KT; avahar- фа] Wb. ZDMG 61.726; avahar(ja] Tm. VS 1.22, Lex. 16, corrected to avahar{da] Tm. CS 21. % Vis[pa]uzia]ti $ KT; Vispjāvaušatiš Rl.; Vispauzati$ WB. " akunava WB; ajkunau[s KT.
3692:4 :pasáva : Vistáspa : āyasatā : avam : kāram : ašiyava : Patigraba
3720:38 Snà : Auramazdaha : kāra : hya : manā : avam : káram : tyam : Vahya
3723:42 mufa : aSiyava : Paxsyàuvadàm : hacd : avadaga : kāram : àyasa
3744:62 y : upastàm : abara : va&nà : Auramazdaha : kāra : һуа : manā : avam : káram : tya Be 63 m : hamigiyam : aja : vasiy,: Animakahya : mahya : XIII: raucabi$ : @akatā : аһа: a ^ V a
3756:80 uš : hacá : avadata : hauv : kārahyā : avaba : adurujiya : adam : Nabukud
3883:92 ipis : hacáma : amavata : haruvada : atar : dahyàva : kāra : hama : amaxmata
4081:22 y : yadiy : kāra : Parsa : pata : ahatiy :һуй:' “i
5092:avd adv. ‘thus’, correlative to уаба: perhaps isn. of !а0а-, but more probably error for атаба ($52.УТ), by omission of one character, as taken by MB Cr. $59; see also avdkara-. DB 4.51.
5095:avdkara- adj. ‘of such sort’: avd ‘thus’ + kara- ‘doer’ (§160.Ia; wrongly Hz. ApI 101-3, who takes -kara- in avükara- and ciyükara- not from kar- ‘do’, but as kara- ‘time’, as in hakaram, q.v.). avakaram nsn. (6259) DNb 6; avdkaram-ca-mary ($109, $133, $135) DNb 2f.
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5159:ukdra- adj. ‘having good people or army’: from u- ‘good’ + kāra- ‘people, army’.  uküram asn. for asf. AsH 9 ($52.11).
5225:ushamaranakara- sb. ‘good warrior’: u- ‘good’ + hamaranakara- ‘warrior’ (§140.VI). ushamara- nakara nsm. DNb 34.
5252:karonaoitt, Skt. kr-, pres. krndti karóti (809, $122, $132.2, 5182.3). See also akarta-, ucára-, kara-, dastakarta-, duskarta-, hakarta-.
5277:kara- sb. ‘doer, maker’, as 2d element of cpd.: deriv. of kar- ($82, §143.1); found in avükara-, ciyükara-, düraniyakara-, zürakara-,  hakara-, hamaranakara-, and with passive meaning, 'thing made’, in patikara- (cf. Bv. Gr. $289).
5383:ci- interrog.-indef. pron. ‘what, any’; col- lateral stem (8201) to OP ka-. See also -ciy, cid, cind, cijükara-.  ciš-ciy asn. ‘anything’ (§9.VI, $105, 5132.2, §201) DB 1.58, Lt. quicquid, pIE *q*id-q*id: reduplicated form with Med. sandhi; see OP -ciy for exact cognates.
5395:ciyăkara- (§53) adj. ‘how great’; nt. аз sb., ‘how great a thing’: *ciya(n)t-, cf. Skt. kiyat nsn. ‘how much, how many’, + kara- to root kar- ‘make’ ($160.19; Bthl. AiW 597; hardly to kara- ‘time’, cf. hakaram, as taken by MB Gr $293, Hz. ApI 101-3). ciyakaram nsn. (§259) DNa 39; ciyükaram DNb 50; ciyakaram-ca-maiy (written — : -"m*m*eur; $41, $51, $132, $138.I; Lg. 15.178, — | against Hz. ApI 240) DNb 51, 51f. 1
5522:daraniya- sb. ‘gold’: Av. zaranya- Ars. Phl.. zarén, NPers. zárr, Skt. htranya-m, pIE *ghj-enio- ($82, $66.П, $88, §126, §144.IV), cf. NEng. gold. See also dáranzyakara-. — daraniyam nsn. DSf 35. darantyam asn. DSf 49f. But Gk. $арекб, a Persian gold coin, is from the name of Darius (Bv. BSLP 30.1.59), and not from a short form of darantya- (as taken by Mt. Gr. $129, Hz. ApI 134-5).
5523:déraniyakara- sb. ‘goldsmith’: NPers. zärgär ‘goldsmith’; daraniya- with vriddhi, + kara- ‘maker’ ($126, §143.V, $160.18; König, Burgbau 65; Hz. AMI 3.73-4; Kent, ЈАО 53.21). dàrami- уакатӣ npm. DSf 49 (on Frag. Theta, Scheil 21, plate 11, see 544; Konig, Burgbau, Tafel 5; Kent, JAOS 53.21, against 51.195-6).
5629:(3) Prefix with verbs avahya-, ay-, ziay-, jan-, рӣ-, fraf-, d-bar-, zbü-; prior element in nouns palikara-, Patigraband-, perhaps Pátisuvari- and
=== leaf for p175 (=+15 -> 190) ===
. Skt. apa, Gk.
and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, pIE *apo. Used with vb. gaud- and in sbb. apaddna-, apa- niydka-; with suffix in apalara-, apara-.
apataram adv. ‘farther off, far off’; nsn. of
apatara-, which is apa- + comp. -fara- ($82,
5190.111), ef. Gk. adv. ётотіро. DNa 18; DSe 16f; XPb 25; XPh 16.
apaddna- sb. ‘palace’: from apa- + déna- ($147.I) to root *dà-, cf. Skt. apadhá- ‘conceal- ment’, Gk. атоблк ‘storehouse’. For development in later Iranian, with ара- by secondary length- ening (but not OP appa-, cf. $130), see Henning, Trans. Philol. Soc. 1944.110n. apadünam asm. D*Sal; АНЬ. apadàna (852.V) A’Sa 3, 4; A?Ha 5.
apantyüka- sb. ‘great-great-grandfather’: from apa- + niyäka- ‘grandfather’, cf. Lt. ab-avos
OLD PERSIAN
'great-great-grandfather'. §52.1) пет. A’Sa 3.
apara- adj. "later, after’: Av. Skt. apara-, from apa- + comp. -ra- ($32, 419.11). арата пет, XPh 47. aparam asn. as adv. DB 4.37, 42, 48, 68, 70, 87; DSt 10° (not apara-ma, nsm. with enel. abl., DB 4.37, 68, 87—and DSt 10°—as Bthl. AiW 77 suggests, following АКК. $a be-la-a ar-kt-a ‘who shall rule after me’).
apan*ydka-ma — (822,
pi- sb. ‘water’: Av. áp-, NPers. db, Skt. pl. nom. dpas, acc. apás, pIE *йр-, with or without i-extension, which seems to have become 5 in OP ($422). āpišim (= apis-Sim; $41, $130) nsf. DB 1.95f. apiyálsf. DB 1.95. abis (Skt. adbhts, and dat.-abl. Skt. adbhyds, Av. aiwyó, both from *ap- bh-; §75.1V, $130, §188.V, JAOS 62.269-70; see also s.v. abi) ipf. DB 1.86.
apiy adv. ‘thereto, very’: Av. arpi, Skt. ápi, Gk. prep. &t ‘on’, pIE *epi (§44, §191.1). In OP, normally enclitic, but sometimes written sepa- rately; often with dūraiy ‘afar’ (5136): dürai-apty ‘far and wide’ DNa 12; düray-apiy DNa 46; dū- raiy apiy as two words, DSe 11, DZe 6, DE 19, ХРа 9, XPb 18f, ХРе 8, XPd 13, ХР? 13, XPh 10f, XE 18, XV 14, A!Pa 14^, A*He 17f. Prob- ably vafsna[pi]y X Pg 7f (Ву. BSLP 34.1.32-4) with crasis, rather than vadsnd-[cily or vasnà-[di]y (Lg.
9.230); KT's lapli-maiy is eliminated by - -
-€
Cameron’s reading of utämaiy as completely visi- -
ble, DB 4.46 (ef. note ad loc.).
afuvayd, error of writing for aruvdya (855.11); see aruva-.
abiy prep. and prefix ‘to, against, in addition to’: GAv. aibi. LAv. aiwi, Skt. abht; conflux of pIE *mbhi, oHG umbi ‘round about’, and pIE *obhi, oCS ой ‘beside, by’.
(1) Prep. with acc., DB 140, 76, 80, 82, 84; 2.12,17, 73, 88; 3.2, 3, 14, 27, 56, 60, 71, 82; 5.12f, 21, 22^, 28, 26, 28°; DPd 18; DPe 24; DZc 9f, 12; XPg 10.
(2) Prefix with verb jav-, and first element in abicaris, abyapara, perhaps in Abirddus, but prob- ably not the base of abif. — —
abicari& DB 1.64f, word of uncertain form and meaning, probably asn. of s-stem (5185.11), to abi- + root car- ‘move, go’ (Av. caraiti, Skt. cárati, Lt. colit, 8”; $107), giving, in association
with the following gaidam ‘living personal prop- — .
LEXICON
erty’, а meaning ‘pasture lands’, cf. NPers. cáridán ‘to pasture’ (Spiegel, KT, Bthl. AW 89). Cf. also Tm. Lex. 64-5; Gray, JAOS 33.281-8; Hüsing, KZ 48.155-6; Hz. Ар] 51-4.
abiyaparam. adv. ‘later, afterward’, from abiy + aparam (§191.1V). ab*yapara (822, §52.V) A’Sa 4.
Abirüdu- sb. ‘Abiradu’, a village in Elam: first part perhaps abi-.— Abirüdus пэт. DSf 46.
abi$ DB 1.86, probably not adv. ‘thereby’, abi- + adverbial -s, but ipf. of арі- ‘water’ (q.v.): not an error for äpiš nsf. ‘water’ as proposed by König, Кар 70-1.
abyapara see abiyaparam.
-am, enclitic particle extracted by wrong di- vision from pAr. *azham T’, perhaps even in pIE times, and therefore *-om from *ej(h)om; seen in OP tuvam (cf. adam T’), iyam, imam, patisam, cf. Skt. fuvám тубт imám ete.
ama- sb. ‘offensive power’, see ArSdama-.
amaxamaté, DB 4.92, read by KT, and ap- parently corresponding to Elam. ‘were pleased (at the inscription)’ (cf. Wb. KIA 72n, quoting vari- ant interpretations): possibly for ham-axmatá, aor. mid. of ham- + kam- ‘like, love’ (OP Хата- ‘wish’, Skt. vb. kam- ‘love’),
```


## [2026-09-06T21:12:41.612Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"people, army\" KNT.txt | head -20"
}
```


### [2026-09-06T21:12:41.662Z] TOOL RESULT

```
1247:$99. PAR. k AND é are found without further change in OP, in the following: pIE q-, in OP kāra- ‘people, army’, ef. Lith.
2765:III. Plural pronouns are often used where the antecedent is ‘men’ implied in a preceding kara ‘people, army’ or dahydus ‘province’ or the like: thus DB 1.65 -diš goes back to 64 kärahyä; DB 2.19-21 -šīm in two occurrences and the two plural imperatives go back to kéram; DB 3.11f akunava"tà is plural by the meaning of dahydué, as are agarbdya” 3.48 and agarbaya” 3.49 by refer- ence to kära 3.45. DNa 36f -&m refers back to -šim 36, denoting ‘men’ (cf. II, above) implied from bümim32. DB 4.5f -šim has the meaning ‘foe(s)’ by reference to hamaraná ‘battles’ (see JAOS 85.844—50, 41.74-5).
5159:ukdra- adj. ‘having good people or army’: from u- ‘good’ + kāra- ‘people, army’.  uküram asn. for asf. AsH 9 ($52.11).
5278:küra- sb. ‘people, army’: Lith. káras ‘war’, dialectal ‘army’, Gt. harjis ‘army’, NGm. Heer (8143. III); ef. König, КИР 66. See also ukdra-.
```


## [2026-09-06T21:12:47.702Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=1\nfor i,l in enumerate(lines,1):\n    if i in (5159,5277,5278,5252):\n        print(i,'leaf',leaf)\n    leaf += l.count('\\f')\nEOF\necho \"=== leaf 200/201/202 heads ===\"\nfor n in 199 200 201 202; do echo \"--- NR==$n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | grep -o \"^.\\{0,80\\}\" | head -3; done"
}
```


### [2026-09-06T21:12:49.505Z] TOOL RESULT

```
5159 leaf 198
5252 leaf 202
5277 leaf 203
5278 leaf 203
=== leaf 200/201/202 heads ===
--- NR==199 ---
DB 1.34f, 41, 461; 2.74, 88f; 5.19f, 35; DNb 30, 37, 40f, 43, 45; XPf 19f; XPh B
щй AsH 13; DB 1.34 bis, 34f, 41 ter, 46 bis, 47, 57, 67, 77, 85; 2.3, 4, 18, 74 
utü-maiy АЗН 12; DB 4.46 (visible to Cameron; ef. note ad loe.); DPh 10; DNa 52f
--- NR==200 ---
 by Hz, ApI 71-2).
ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893)
uba- adj. ‘both’: GAv. uba-, Skt. dual ubhá(u), pIE *ubhó(u), cf. Gk. &p-dw, Lt.
--- NR==201 ---
B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vriddhied), and by H. H
Uvárazmi- sb. ‘Chorasmia’, a province of the Persian Empire: Elam. ma-ra-18-mi-1
Uvürazmiya- adj. ‘Chorasmian’: deriv. to pre- ceding ($144.11). (Uvarajzm*ya (82
--- NR==202 ---
to the wall alongside it (König, - Burgbau 32n; Hz. AMI 3.54-5, Ар! 224). katam 
Katpatuka- sb. ‘Cappadocia’, a province of the Persian Empire; also, as adj., ‘C
(1) ‘Cappadocia’: Katpatuka nsm. РВ 1.15f; DPe 12; DNa 28; DSe 27°; D8m 8^; XPh
```


## [2026-09-06T21:12:59.420Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==203' KNT.txt | head -40"
}
```


### [2026-09-06T21:13:01.497Z] TOOL RESULT

```
om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2).
акша aor. mid. ($66.1, §218.11, §235.11) CMb 4; DB 1.47.
akunavayalà imf. pass. (§220, $235.IT) DB 1.20, 24.
akariya imf. pass. (585.1, §99, $220) DSf 37; XPh 42.
akarzya^tà За pl. imf. pass. (§35.1, $66.IT, $220, 8236.11) DB. 3.92. !
[c]àzr[;yatà]| or cazr{iyatd] perf. pass. ($219, $220) DB 4.90 (Kent, JAOS 62.267-8, for KT's „ада... after König, Klotho 446).
kunavahy 2d sg. sub). (8222. TIT) DB 4.75, 79.
kunavánazy lst sg. subj. mid. (§66.1, $222. III, $233.IV) DSI 4 (Bv. BSLP 30.1.65; not act. -nty, with Wb. AfOF 7.39).
kunavdtaiy subj. mid. (5222.11) DNb 56.
caxriya perf. opt. ($99, $1081, $122, $219, 6228.1, $228.II) DB 1.50.
kariyaiš opt. pass. (585.1, $220, $223.IT, $228.- Ш) DNb 9, 11 (not desiderative future, as taken by Hz. Apl 228).
kunautuy imv. (§210.1, 5237.П) DB 4.76.
kušuvā 2d sg. aor. imv. mid. (5218.1, $237.11) DNb 50.
eartanaiy inf. (581, $99, $122, 5238) DB 1.94; 2.33, 381, 44, 53, 58, 67; 3.36, 431, 60, 651; DSf 20°; DSn 1°.
karta nsm. past pte. pass. (Av. karata-, NPers. hard, Skt. kid-; $30, 506, 8122, 242.1) DPe; ЮР; DSf 38, 40, 43; XPi*; AM,
kartā nsf. A?Pa 28. kartā npf. ($119) DSi 46.
kartam nsn. DB 1.27; 2.27, 37, 42, 47, 57, 62, 02, 08; 3.8f, 10, 19, 21, 40, 47, 53, 64, 69, 76; 4.2, 42, 46f, 49, 511, 52, 54; "Ма 48f; DNb 29, 48, 56°; DSe 44; DS} 5f°; DSn 2; DSs 7; XPa 14, 15f, 19, 20; XPb 23f, 25, 30; ХРе 13, 14; XPd 19; XPf 38, 461, 47; XSc 5°; XV 27°; XH; A'Pa 24°. kartā (for nsn., $56:V) А?Ра 26. kartam asn. DNa 51; XPf 40; XPg 10; XPh 46; A’Sd 4.
kara- sb. ‘doer, maker’, as 2d element of cpd.: deriv. of kar- ($82, §143.1); found in avükara-, ciyükara-, düraniyakara-, zürakara-,  hakara-, hamaranakara-, and with passive meaning, 'thing made’, in patikara- (cf. Bv. Gr. $289).
küra- sb. ‘people, army’: Lith. káras ‘war’, dialectal ‘army’, Gt. harjis ‘army’, NGm. Heer (8143. III); ef. König, КИР 66. See also ukdra-.
180
Ката nsm. DB 1.33, 40, 79, 85; 2.16, 18, 25, 27, 301, 35, 40, 46, 50, 55, 60, 751, 87, 90, 94; 3.3, 17, 26, 32, 38, 45, 59, 62, 67, 81; 4.92; DPe 22; DSi 29,32. Ката-йт DB 1.50. káram asm. DB 1.51, 52, 66, 78, 86, 88, 95; 2.19, 20f, 25, 35, 41, 46, 55, 61, 68, 72, 81, 83f, 87, 97; 3.1f, 4, 7, 15, 17, 29, 38, 42, 46, 55, 58, 62, 67, 84, 85; 4.34; 5.7; DPe 21. kárahyà gsm. DB 1.31f, 38, 64, 75; 2.10, 15, 80; 3.24, 70, 80; 4.54, 55, 58. kárá ism. DB 1.93; 2.22, 67, 85, 95; 3.15f, 33, 36, 73, 861; 5.9, 21, 24; DPe 8f. |
Karka- adj. ‘Carian’; pl., also a province of the Persian Empire: Elam. kur-qa-ap, Akk. kar-sa, Gk. Kapes, Карко{ (§31, §106); cf. Eilers, OLZ 38.201-13, with lit. Karka пет. А?Р 30. Karka npm. DNa 30; DSe 30°; DSf 33; XPh 28.
karnuvaka- sb. ‘stonemason’: from root kart- ‘cut’, Av. pres. karanv-, Skt. kyi-, pIE *gert-, + suffix -aka- (§30, $146.D), ef. JAOS 51.210. There are also forms of this root without -i- (JAOS 53.20), such as Gk. керө (cf. Boisaca, Dict. étym. de la langue greeque, s.v.). See also Bv. BSLP 30.1.06; Hz. AMI 3.78; Kónig, Burgbau 69-70; Wb. AfOF 7.48. — karnuvakà npm. DSf 47.
Karmüna- sb. ‘Carmania’, a district of South- ern Iran ($166.I): NPers. Kirmān, Gk. Kapyavia. Karmánà absm. DSf 35.
karSa- sb. ‘weight, (unit by) weight’ (like Lt. pondo, Lg. 19.227-9), = 83.33 gr. or slightly less than 3 oz. avoirdupois (Gray, JAOS 20.55; Sehmidt, Treasury of Persepolis 62): Skt. karga- ‘pull, unit by weight’ (§29.n2, $80, $1431, VI). The OP kar$a- was one-sixth of the Babylonian mana ‘mina’ (weight; not unit of value). Elam. transcribes kur-Sa-wm, = kršam, which may mark the word as netter, since Elam. transcriptions commonly represent the nom. sg. of the foreign word; but the other evidence is rather for the masc. karšā ism. (§252D; Lg. 19.227-9; not ndm.) Wal. karíayá lsm. (§251C; Lg. 19.227-9; not npm.) We 1; Wd 1.
kasaka- sb. ‘semi-precious stone’; Elam. ga- st-ga causes König and Wb. to write kás'ka, but this is not warran
```


## [2026-09-06T21:13:09.556Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==198' KNT.txt | grep -n \"^1[0-9][0-9]$\\|ukdra\\|ukāra\\|^u- insep\" \necho \"--- full-ish leaf 198 numbers ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==198' KNT.txt | grep -nE \"^[0-9]{3}$\"\necho \"--- context around ukara ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==198' KNT.txt | sed -n '1,12p' | cut -c1-120"
}
```


### [2026-09-06T21:13:11.958Z] TOOL RESULT

```
14:ukdra- adj. ‘having good people or army’: from u- ‘good’ + kāra- ‘people, army’.  uküram asn. for asf. AsH 9 ($52.11).
20:175
--- full-ish leaf 198 numbers ---
20:175
--- context around ukara ---
�; 4.33; DPe 7; DNa 16; DSe 15; DSm 5°; XPh 14. ima apf. DB 1.21; D$g 3°.
ima nsn. DB 1.27, 72; 2.01; 3.10, 20, 58, 76; 4.1, 9, 40, 49, 59; 5.2; DPh 4; ОМ 32; DSf 22; DH 3. ima asn. DB 1.25 bi
Imaniš- sb. ‘Imanish’, name assumed by the Elamite rebel Martiya (§163.V): Elam. um-man- nu-$, АКК. tm-nia-ni-e
уат demonst. adj. and pron. ‘this’ ($11, $260.I1I, $265): from * nsf. (perhaps also from *? suffixless пзш.) -
DPd 6; DZe 10; iya (§52.V) DB 4.90; т |
DB 4.91 (written тё, $52. VI).
isuvd- sb. ‘battle-ax’ (Junge, Klio 33.223; Kent, JNES 4.233): etymology unknown (stem- formation $143.IV). Not ‘b
LEXICON
as- vb., see atš-,
isti- sb. ‘sun-dried brick’ (5152.11, 5179.11): Av. tštya-, NPers. 110, Skt. istaka-, Medieval Skt. isttka- (König
ета or lismar\uy asn., of uncertain mean- ing, possibly ‘(gold) inlay’ (Cameron, Persepolis Treasury Tablets 129-
Izalàü- sb. 'Izala', a district in Assyria (86, $107): Elam.?5-$1-la.  Tizaljä nsf. DB 2.58, as re- stored by Wb ZDMG
```


## [2026-09-06T21:13:20.980Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN grep karawan/karwan ===\"\ngrep -n -i \"kārwān\\|karwan\\|kārawān\\|karawan\\|Karawane\" HRN.txt | head -20\necho \"=== HRN leaf 258 (p237) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==259' HRN.txt | head -40"
}
```


### [2026-09-06T21:13:22.901Z] TOOL RESULT

```
=== HRN grep karawan/karwan ===
7253:np. karwän 'Karawane' finden; Nöldeke (mündliche
=== HRN leaf 258 (p237) ===
— 237 —
*m + V^göp- "behüten, verwahren*, vergl. ai. X^göp- ;
plilv. n(i)huflan 'verbergen*.
kurd. nixiftifi *sich verbergen*, nix^ftin Causat.
^verbergen.
Bartholomae meint nach briefl. Mitteilung, dass
nihuften sein h von np. niMti (No. 1058) bezogen
habe; ai. i^^göp- sei vielleicht eine Nebenform von
[y^göh^ und die dazu gestellten Formen stammten
also nur zum Teil von göpä- 'Hirt*. Vergl. auch
Johansson, Indog. Forsch. IL 50, 51. Jedenfalls
wird es schwer, mhffffeti gänzlich von \ ^göh- zu
trennen.
1060. nei 'Schilf, «af *Flöte\ näl; vergl. A-e/Te|wfl7, stlrjndT
Testflöte* '), seh^näi ; nnlze.
g. nad.
ap. *nada' 'Schilf; phlv. nai bezw. nad (PPGl);
ai. nadd-, nadd- Schilfrohr (Pischel, ZDMG. :U),
717 folg., Ved. Studien I, 183 folg.); arm. net Pfeil*
(H. No. 219)?
Die Lautverhältnisse sind noch nicht richtig er-
kannt. Np. nei, g. nad setzen unbedingt eine Urform
*nada- voraus ; neben dieser gab es eine zweite Form
*narda-, auf welche ai. nadd- (gr. LW. vdodo^*, hebr.
LW. '^.IJ-)) und np. näf zurückgehen. Das jüngere
skr. näld- ist persisches Lehnwort. Wie häufig,
erscheint dann auch eine gedehnte Form, np. näl^
ai. nädt-, die nicht mehr 'Schilf, sondern ein 'Musik-
instrument aus Rohr, Flöte* bezeichnet. Skr. Hald-
wird jüngere Form für nadd- sein, wie Pischel an-
nimmt, nalada- ist sanskritisirtes vd^öoq,
1061. ne 'nicht' (Öähn. I, 198 Anm. 2, Calc), vergl. nPsi
(No. 1066), niy[ayed,
ap. naiy 'nicht'; aw. nöit, na^ci-; päz. ne; ai. ncd.
oss. d. 7ie6i, t. ntci nichts' (201).
*) Kauk.-bergjüd. eürnai 'Schalmei*, russ. LW. zurna.
*) Die aus dorn Persiacbeii entlehnt sind.
```


## [2026-09-06T21:13:32.066Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7230,7270p' HRN.txt\necho \"=== page of line 7253 ===\"\npython3 - <<'EOF'\nlines=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=1\nfor i,l in enumerate(lines,1):\n    if i==7253: print('leaf',leaf,'printed p',leaf-22+1)\n    leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-06T21:13:34.406Z] TOOL RESULT

```
K.
/,8:J1. (i)kär *Wcrk, Tlmt\
aw. kära- in käravaitl; plilv. kär; skr. -küra- *i:Iand-
limg, That\
Allgemein entlehnt.
832. (2)'kär 'Tliäter , z. B. in sitahkär, destkar,
ai. -kära- '-tuend'; plilv. -kär,
Vergl. np. gär (No. 884).
■ym, kärd 'Messer.
aw. kareta- Messer ; plilv. kürt; ai. vergl. [/kart-,
kfntdti 'schneiden*.
kurd. kir, ktrd (H.-Sch.); oss. d. t. ßa?'d 'Messer,
d. kärdtm, t. Mrdln 'schneiden'; bei. kärc^ kärca^
n. ßarca (195).
834. kär[»är 'Kampf, Schlachtfeld*, vergl. karJ 'Kämpfer.
phlv. kärejar (y. 11 (8)).
vergl. ap. kära- *Heer'; lit, käras 'Krieg'; ksl. kara
'Zank, Streit'; got. harjis 'Heer.
Das Suffix -eflr ist unklar. Im PehlevT lautet es
'jär, was nicht -cär gelesen werden kann; vergl.
dialektisch grl. käljär (Vullers), Kä§. K. kast^jori —
kistzär.
Fr. Müller (WZKM. 5, ;354) will dasselbe kär in
np. karwän 'Karawane' finden; Nöldeke (mündliche
Mitteilung) stellt hierher np. kärdär 'Vezir .
835. kästen Vermindern, verringern', Praes. käh-eni,
^ kahldefiy Icästi,
phlv. kahltan, kähet, kälünltan, käh{i)sn (Men. s. v.
khah"),
Wohl zu demselben Stamm wie aw. kasu-, np. kih
(No. 877).
y'836. kästen (Sahn. 111, 1544 Vers 842), kisten 'säen',
Praes. kär-em, kist,
g. kastmün,
aw. [/kars-f ya{i\lxarsti, vergl. karsosca frakäroyöis;- 186 -^
plilv. hisUw, kis 'Furcliü (vd. 9 (132)), i/^r/är 'Acker-
land' (vd. 5 (22) Gl.), akist (aw. akarsta-, vd. 3 (79)),
kär 'Besäung' (AV.); ai. 2. [/kars-^ kfsdti 'Furchen
ziehen, pflügen.
af/. karal 'säen'; bei. kisag ^ n. kisay (198); wa;^.
kilr-am, sar. cär-am,
=== page of line 7253 ===
leaf 207 printed p 186
```


## [2026-09-06T21:13:55.898Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"karnā\\|karnâ\\|kurnā\\|kornā\\|karnai\\|karnä\\|kurna\\b\" HRN.txt | head\necho \"=== HRN entries on p.237-ish? Numbers ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==259' HRN.txt | grep -nE \"^ *10[0-9][0-9]\\.\" \necho \"=== search 'kalanjar|kālanjār' ===\"\ngrep -rn -i \"kalanjar\\|kālanjār\\|kalinjar\" HRN.txt IEC.txt KLN_1966.txt | head"
}
```


### [2026-09-06T21:13:57.472Z] TOOL RESULT

```
=== HRN entries on p.237-ish? Numbers ===
14:1060. nei 'Schilf, «af *Flöte\ näl; vergl. A-e/Te|wfl7, stlrjndT
32:1061. ne 'nicht' (Öähn. I, 198 Anm. 2, Calc), vergl. nPsi
=== search 'kalanjar|kālanjār' ===
```


## [2026-09-06T21:14:06.181Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls incoming/BQT/\necho \"=== find printed 1575 ===\"\npython3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('n pages',len(pages))\nfor i,p in enumerate(pages):\n    if '1575' in p[:400] or '۱۵۷۵' in p[:400]:\n        print('--- idx',i, p[:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T21:14:08.116Z] TOOL RESULT

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
=== find printed 1575 ===
n pages 721
```


## [2026-09-06T21:14:10.584Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport json\nm=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))\nprint(type(m), list(m)[:5] if isinstance(m,dict) else m[:5])\nEOF"
}
```


### [2026-09-06T21:14:12.198Z] TOOL RESULT

```
<class 'dict'> ['pdf', 'pdf_pages', 'offset_mode', 'anchors', 'map']
```


## [2026-09-06T21:14:15.437Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport json\nm=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))\nprint(m['offset_mode'], m['anchors'][:5] if isinstance(m['anchors'],list) else m['anchors'])\nmm=m['map']\n# find printed 1575\nif isinstance(mm,dict):\n    for k,v in list(mm.items())[:5]: print(k,v)\n    print('1575 ->', mm.get('1575'))\nEOF"
}
```


### [2026-09-06T21:14:17.119Z] TOOL RESULT

```
1203 34
1210 1
1211 2
1212 3
1213 4
1214 5
1575 -> 368
```


## [2026-09-06T21:14:19.914Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (367,368,369):\n    print('==== pdf page',i,'====')\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-06T21:14:21.598Z] TOOL RESULT

```
==== pdf page 367 ====
[pdf page 368]
‎—\eve—‏ کالجوش
کویندکه ‎Ge‏ باشد ‎ASE ASH, ٩‏ |
‎oly!‏ مقدار باشد که اسب وآدم لتواند چست -
و تخته سنك تنك و ‎SW‏ را ‎SaaS js‏ بر
روی مردروهای(۱) زیرحمام وجوبهایآب‌پوشند.
کالاشکن ۴ ه بسکون شین تقطمدار
وفتح‌کاف بروزن وا داشتن » لوعی از حلواباشد .
کالب ۴ » بر وزن و معنی قالب است

‏که آنرا کالبد نیز گویند .
‎gee TAIT‏ با وسکون‌دال ‎ion!‏
‏بمعنیکالب (۲) است که قالب هر چیز باشد -
وبمعنی تن وبدنآدمی وحیوانات دیگرنیزهست؛

‏ویفتح بای ابجد هم گفته‌اند .
کالبوی ‎٩‏ - با بای ابجد بواورسیده

‏(۱) چش: مروررودهای . (۲) چش : قالب .

‏وتحتانی زده ؛بععنی س رکشته و متحیر و حیران
باشد - و بمعنی نادان وهیجمبان همآمدماست؛
وبحذف نحتالی‌هم درست‌است که بروزن هزبوباشد.
کالچاه ۱ = باجي ‎BL‏ کید ,
بلفت ‎OS‏ بروزن ومعنی‌کارزار است که ‎Kee‏
‏وجدال ‎ath‏ - ومزرعةً برج را نی زگوبند۷ .
کال‌جوش - باجم بروزن‌تالپوش,
‎gy!‏ ازماحض باشد که دروبشان پزند وآن‌چنان
باشد که تالرا ریزه کنند همجتان که پرای‌اکنه
ریزه میکنند وکشك باب نرم کرده رابا روغن
‎duly‏ قلفل وزیرء و منز کردکان و ‎Bal‏ ریزء
کرده درديك ریز ند ودوسه جوشی داده‌فرود آرند
وخورند ۸ .

‏۱ « درمیان مردم خراسان مثل است که جابی که کالار است هیزم نیست و ‎ile‏ که
هیزم است کالارنیست» ‎only‏ مثل بدان میکوبند که هرجا که کالار باشد هیزم زودتر کنده‌میشود.»
« جهانگیری » ورك : فرهنگ نظام . ۴ کلاشکن ‎Cea)‏
‏برافراختند از قفایش چو باد از کالاشکن سنجق ‎Jue‏ وداد . . بحاق‌اطعمه «فرهنگه تظام».

‏۴ ره :کالید ۰ ۴ - پهلوی 1220 (شکل » صورت) »پازنت2[000ع1,
مستمار از بوتانی ‎kalopédhion‏ (قالب) . ارمتی ‎kalapar‏ از ‎kalapadh‏ ۵ سریبانی ع
0 عربی قال * نیب رکك ص۱۱۸ ۰« اسشق ص ۲۸۲ ۲ در اوراق مانوی بیهلوی 1۳10/0
‎IG)‏ » وضم ۰ جم) . ( هنینگ . فهرست لفات پارسی‌میانه. 13505 ‎Cty . 1 TX.‏

‏۵ _ مسحف «کالیو» س کالیوه (هیم.) ...۰ ‎"٩‏ کالیجار ‏ کالنجار . موستی در
نام ‎be‏ ابر آفی (ی ۱۵۳ ) «کالنجار» را ازاصل « کالجار» کیلکی و 2۳108۲ پهلوی و کارزار
فارسی و ‎kalinjarai‏ سانسکریت بمعنی ‎Ke‏ و حرب کرفته . ( رك: کارزار ). هوار نیز در
دائرتالمعارف اسللام (دره ابو ‎(GIT‏ همین قول‌را نقل کرده‌امت ورثك . انجمن آرا ‎Dy IT?‏
لت نامه حرف الف ص ‎VAN‏ ستون۲. ۱-۷ دیگر کالنجار بمعنی برنجزار که‌شلتوگزار
نیز گویندآمده و بعبارت و اصطلاح ‎IS al‏ وتبرستان بممنی ‎Coke‏ ملك وزمین وزراعت‌خواهد
بود » «انجمن آرا » ظ : کالنجار صورتی از کالیجار ص کألی ( قس : کال ی کیلکی بمعنی سأقه‌های
خشك ‎ts‏ برنج و شالی بمعتی شلتوك )+4 جار ( زار ‎rye‏ مکان ) . رك : لت‌نامه حرف

‏الف س ۷۸۱ ستون ۲. ۸ — هدایت گوید : « کال جوش ازانگوبند که بسیار پشته
نگردد ... سه جوش بیشتر تگذارند بخورد و بردارند و بخورند . نظام‌الدین قمری اصفهانی گفته:
مائیم سه چار شخص ممهود آزرده زدور چرخ و انجم
دارم ‎cle‏ کالجوشی از
==== pdf page 368 ====
[pdf page 369]
‎as‏ سفنه
‎SHUT‏ - بفتم تالك وسکون دال ابسد,

‏آنجا آورند , ویل‌چیزیست که بدان‌چیزهارنگ

‏یمنی درهم شود- ‎+p Say‏ کنند .
کالفته. - بروزن آلفته , بسنی آهنته کالنچه » بکر ‎ct‏ وفتح ‎tier‏

‏را کویند ‎OT,‏ پردده‌است مشپور وشبرازبانآ ترا
قالنجه خوانند وبعربی ‎Jake‏ گویند ؛ و بمضی
عکه را نیز قالنجه خوانند .

‎TIE‏ - با ثاك بواو کشیده و بجیم
زده »کنوتر رااگویند وآن پرنده‌است معروفت
‎Sly‏ شت کوچك را هم میگویند که عربان‌ختص
خوانند ؛ وباین‌معنی با جیم فارسی‌هم آمده‌است -

‎MS abs ‏بسکون خای‎ - EME
‏بدبوی و بسن یگوبند گندناست وآن سبزیی‎ ath
. ۷ ‏باشد که خورند‎

‎HIE‏ بروزن سالوس » بمعن‌نادان
‎ably‏ (۱) وبیعقل واحمق باشد ۸ .

‏کالوسك - بسکون سین بی‌نقطهوکاف,
‎WL‏ را گویند .
کالوشه - ‎tie‏ شین نقطه‌دار » دبگه

‏وشیدایی و دبوانه مزاج وپریشان حال باشد؟ .

‏کالفه ؟ - نم ثالث و فتح فا » بمعنی
کالفته است که آشفته وشیدایی باشد .

‎el‏ « بفتح لام وسکون‌کاف؛خربزه
تارسیده كوچك را کونند و بعربی خضف خوانند
- وکدوی استادان حجام را کویند که با آن
حجات کنند.

‎AT‏ شم تالك و سکون میم » زیرا
کوبند که شوهرش مرده باشد با طلاق گرفته
‎Fash‏ .

‎GI‏ - بنتح الك وسکون نون‌وجيم»
تلم میوماست شبیه کا وآنرا درخراسان علف
شیران وبمربی زعرور خواند .

‎pe‏ ۱ - بت فتح ‎ot‏ و جیم بروزن
آهنگر » تلم ‎Spans » eles‏ تیل از

‎. ‏ابله‎ - : ose )۱(

‎. ‏-رك: کالیدن‎ ٩
‏-فروآید زیشتش پورملعون . شدهکالفته چون خرسی‌خشینه. لبیبی«لفت فرس44۲.‎ ۴
‏پوند پدید آورندة اسمازصفت)‎ ) 3+ p.m) ‏رك : کالفته. ۴ از :کال‎ ۴
) ‏خربزه‎ ( kAlak ‏کاله )4.0( ,کردی 68186 ( خریزه ) ۶ ژایا ص ۰۳۲۳ طبری نیز‎ =
oto ‏واژء نامه‎ «
. ‏کالم که نیز دکند شوی‎ wh ‏پای تو از میانه دفت وزت‎ -
* ۳۳۹ ‏منجيك ترمذی « لفت فری‎
‏مرجوم ادیپ پیشاوری درحاشيةٌ تاریخ بیهقی (جاپ‌تهران۱۳۰۷ ص۱۷۸ )نوشته‌اند:‎ - ۲
SE ‏بمعنی‌سیاه و ج رکه‌ممرب کر‎ MOS ‏اين کلمه م رکب است از دو لفظ هندی‎ , pull
‏هند است. پس کالنجر بمعنی سیاه قلمه ( است ) و این‎ al ‏تازی و راء غلیظ که مخصوص لهج‎
© ‏قلمه در شمالی لاهور وجتوبی کشمیر بود در ابأم قدیم‎
‏له کیکیز.‎ SE ‏بنفثه بوی نه کالوخ  گنده دهالی کرفی‎ Gls ‏کنده‎ ۴
.* ‏موزلی سمرقندی . « فرهنگه نظام‎
‏مکن‌بگاراا این‌خوی وطبع‌را بگذار‎ ath ‏ملول مردم » کالوس بی‌محل‎ A
.* ۱۹4 ‏ابوالموید بلخی . « لفت فرص‎

==== pdf page 369 ====
[pdf page 370]
—\evy—

‎eb‏ پزبرا گوبند ۱ - وآشی هم‌هست مخصوص
مردمان دیلمان که از برنج و نخود و چفندر
و رکه پزند وچون پخته شود کشنیزتر و نعناع
,1 پاهم کوفته در روغن بربان کنند وبربالای ‎OF‏
‏ریخته ‎Byte‏ .

‎IME‏ ۴ = بروزن‌انونی » نام کیاهی
است کهآنرا بعربی سعتر میگویند.

‎ve‏ = بر وزن لاله » بمعنی کالا است
که اسباب ومتاع باشد ۴ - ‎UIE,‏ پنبشحلاجی
کردموینبه‌ای که بجهت رشتن‌قتبله کردهباشند ۴
- وه کدورا نیز کویندعموماً و کدوبی که‌شراب
‎OT‏ کنند خصوصاً ‎٩‏ - و بمعنی کالك هم‌آمده

‏است که خربزء کوچك نارسیده‌باشد. وزمینیرا

‏یز کوبند که بجپت زراعت کردن آراسته و مهیا
ساخته باشند ۷ .

‏(۱) ظ : ژولیده کردیده موی مادرزاد .

‏کالهدان ‎A‏ - با دال ابجد بروزن لاله
سان, سله وسبدی باشد کهزنان پنبفرشتن‌ورسمان
رشته شده را درآن گذارند .

‏کالی - بر وزن قالی » بمعنی محافظت
کننده و نگاهبان باشد 6 - و درعر‌بی‌بمعتی‌سیه
است که اقیض ‎ai‏ باشد *۷.

‎AIT‏ ۰۱۱ بروزن ‎vase‏ ماضی‌کالیدن
است ‎git‏ درهم شد - و درهم کرد - و آمیخت
-و بمعنی کریخت‌هم آمده است که‌ماضی کربختن
‎ath‏ .

‏کالیدن 2 بر وزن الیدن . بمعنی
درهم شدن؟۱- و درهم کردن - و گریختن‌باشد.

‏کالیكه ه بر وزن مالیده » بمعنی
درهم ‎oat‏ وآمیخته - وآشفته وژولیده کردیده
- و موی مادر زاد (۱) ۱۴ - و گربخته باشد ‎a‏

‏- جهانگیری و ولف این شمر فردوسی را برای این معنی شاهد ورده‌اند:

‏( یکی ‎oy»‏ دستار در زیر مك
‎wi‏ و کالوثه‌ای بر ‎she‏

‏پبازار شد . گوشت آورد ‎(Sy‏
‏وزان رنج , مهمأن همی کرد یاد .
‎blak «‏ بخ ج ۷ ص ۲۷6 ۷ .

‏رلی‌محتمل است که‌مراد همآن کالجوش(ه.م.) ‎cath‏ بعنی کالوشه را بارکرد . رك: معنی‌دوم کلمه.

‏۴ - مسیف «کاکوتی * (دمضدا) .
لوخرانی که رسیدند ببازار کهن

‏۴ پاینمعنی ‎Sy‏ :گاله .

‎٩‏ کند ‎Op SUS‏ تهی ز درد شفق

‏۱ - رك : کالك .
۸- ظ. از ‎dale‏

‏۴ « ولا :

‎. ‏کاسد ابشان ببهابی برسید‎ U6
© ‏مولوی « فرهنگه نظام‎

‏شبی که زهره بیادش شاط کاله کند .
‎asl‏ ایوردی « جهانگیری * .

‏۷ - درخراسان باین ‎gue‏ استممال کنند «فرهنگه نظام >.
= کالا) + دان (پسوند)ه

‎cal "WIS? : ‏عربی‌است‎ - ٩

‏وکلاء و ‎UT, ATH‏ نگاهبانی وی کرد . » « منتهی‌الارب *.

‏و۳۳۹ : « منتهی‌الارب * .

‏۱ رك : کالیین .

‏- از :کال ‎Cpa)‏

‎Oat‏ (پوندمصدری) . رشیدی (ص۱۲۱ و۱۲4) «کالیدن»آورده بمعنی‌دورشدن وکنار گرفتن.

‎ap ۴‏ دیا تا بکی کالیدات

‏هر زمان جوشیدن و نالیدت .

‏شاکر ‎he‏ فیسی . رودکی ج ۳ ص ۱۱۷۷ و رل ‎Lal‏ ۰۱۱۹69۱۱۹۱

‏۴ ازین خفرفی موی کالیده‌ای

‏بدی » س رکه در روی مالیده‌ای +
بوستان «تعلیقات فیه‌مافیه . فروزانفرس۳۲۷*.
```


## [2026-09-06T21:14:40.793Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"== $f ==\"; wc -l $f; awk 'BEGIN{RS=\"\\f\"} END{print \"leaves:\",NR}' $f; head -c 600 $f; echo; done"
}
```


### [2026-09-06T21:14:42.837Z] TOOL RESULT

```
== MON_part1.txt ==
99339 MON_part1.txt
leaves: 1
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی 
== MON_part2.txt ==
94500 MON_part2.txt
leaves: 1
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاعات فیپا. 
۱. فارسی -- واژه‌نامه‌ها. الف. عنوان. 
۴۵ف ۲۹۵۴/۸۷ ۳112 ۳ فا ۴ 
۱۳۸۱ 
کتابخانه ملی ایران ۷۹۵ - ۸۱م 


انتشارات آدنا 
فر هنگ دوجلدی معین 
گردآورنده عزیزالته علیزاده 
�
```


## [2026-09-06T21:14:56.637Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 caravan ===\"; grep -n \"^caravan\" KLN_1966.txt | head\necho \"=== KLN van ===\"; grep -n \"^van,\" KLN_1966.txt | head\necho \"=== KLN harbor/harbour ===\"; grep -n \"^harbor\\|^harbour\\|^harry,\" KLN_1966.txt | head\necho \"=== SKT caravan ===\"; grep -n \"^CARAVAN\\|^VAN\" SKT.txt | head\necho \"=== PHD kārawān / kārzār ===\"; grep -n \"^kārwān\\|^kārawān\\|^kārezār\\|^kārzār\\|kārwān\\|kāre\" PHD.txt | head\necho \"=== PHD kār ===\"; grep -n \"^kār \" PHD.txt | head\necho \"=== NYB ===\"; grep -n \"kārwān\\|kārečār\\|kārčār\" NYB_vol2_glossary.txt | head\necho \"=== BRT kāra ===\"; grep -n \"kāra-\" BRT.txt | head -5\necho \"=== AHD watkins koryo ===\"; grep -n \"koro-\\|korio-\\|kóryo\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T21:14:56.794Z] TOOL RESULT

```
=== KLN 1966 caravan ===
6497:caravan
6499:caravan,  n.  F.  caravane,  fr.  Pers.  karwan, ‘company  of  travelers,  caravan’,  which  is  rel. to  OI.  karabhdh,  ‘camel,  young  camel,  young elephant’.
6501:caravanserai,  n.,  Eastern  inn,  esp.  for  caravans. —  F.  caravanserai,  fr.  Pers.  karwansarai,  fr. karwan  (see  caravan)  and  sarai,  ‘mansion,  inn’, which  is  prob.  rel.  to  Avestic  {trayeihti,  ‘they protect’,  Ol.  trdyate,  ‘protects’, caravel,  carvel,  n.,  any  of  various  kinds  of  light vessels.  —  F.  earavelle,  fr.  Sp.  carabela,  dimin. formed  fr.  cdrabo,  ‘a  small  vessel’,  fr.  Arab. qdrib,  ‘bark’,  which  is  traceable  to  Gk.  x£px|3o<;, 'horned  beetle;  crayfish;  a  light  ship’.  See  scarab, caraway,  n.,  a  plant  with  aromatic  seeds.  —  ME carawai,  fr.  OSp.  (=  Sp.)  alcaravea  (whence Sp.  carvi),  fr.  Arab,  al-karawiyd’ ,  fr.  a /-,  ‘the’, and  karawiyd',  fr.  L.  carum,  careum,  fr.  Gk. xxpov,  xapcov,  ‘caraway’,  which  is  of  uncertain origin.  Cp.  skirret.
=== KLN van ===
41062:van,  n.,  a  winnowing  fan.  —  ME.,  fr.  OF.  (=  F.)
41065:van,  fr.  L.  vannus,  ‘winnowing  fan’,  which  is  of uncertain  origin.  It  is  possibly  rel.  to  L.  ventus, ‘wind’.  See  wind,  ‘air  in  motion’,  and  cp.  fan,  ‘an instrument  for  winnowing’.
=== KLN harbor/harbour ===
17260:harry,  tr.  v.,  1)  to  ravage;  2)  to  harass.  —  ME. harien,  herien,  fr.  OE.  hergian,  ‘to  ravage,  lay waste’,  rel.  to  ON.  herja,  ‘to  make  a  raid,  to plunder’,  OHG.  herion,  MHG.  hern,  ‘to  ravage, plunder’,  OHG.  firherion,  MHG.  verhern,  ‘to destroy  by  war’,  G.  verheeren,  ‘to  destroy’. These  words  lit.  mean  ‘to  afflict  with,  or  destroy by,  an  army’,  being  denominated  fr.  OE.  here, resp.  ON.  herr  (whence  Dan.  hser,  Swed.  har), OHG.  hari,  heri,  MHG.  her,  G.  Heer,  ‘host, army’,  which  are  rel.  to  OS.,  OFris.  heri,  Du. heir,  Goth,  harjis,  of  s.m.  These  latter  words orig.  meant  ‘that  which  pertains  to  war’,  and are  cogn.  with  Lith.  karas,  ‘war,  quarrel’,  kare, ‘war’,  karias,  ‘host,  army’,  OPruss.  karjis, ‘army’,  OSlav.  kara,  ‘strife’,  Mir.  cuire,  ‘troop’, OPers.  kara,  ‘host,  army’,  Gk.  xoipavo?,  ‘ruler, leader,  commander’  (prop,  ‘leader  of  an  army’, fr.  *xoipa,  for  *xopta,  ‘army’).  Cp.  prec.  word. Cp.  also  the  first  element  in  arriere-ban,  har¬ binger,  harbor,  harness,  Harold,  herald,  Herbert, heretoga,  heriot,  Herman,  hership,  and  the second  element  in  Lothario,  Oliver,  Walter. Harry,  masc.  PN.  —  F.  Henri.  See  Henry, harsh,  adj.  —  ME.  harsk,  of  Scand.  origin.  Cp. Dan.,  Norw.,  harsk,  Swed.  harsk,  ‘rancid’, which  are  rel.  to  MLG.,  G.  harsch,  ‘harsh, rough,  raw’;  fr.  I.-E.  base  *qars-,  ‘to  scrape, scratch,  rub",  whence  Lith.  karsiu,  karsti,  ‘to comb’,  OSlav.  krasta  (for  *korsta),  Russ. kordsta,  ‘itch’,  MLG.  harst,  ‘rake’,  L.  carrere,
=== SKT caravan ===
=== PHD kārawān / kārzār ===
159:p. 166 |142) after si add dig. p. 179 [115; for kārēzār read kārezār. wp. 220 [33] for arg, halag read alag, halag.
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
940:battlefield kārezār, razmgāh.
=== PHD kār ===
=== NYB ===
=== BRT kāra ===
=== AHD watkins koryo ===
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGHER; Cc. Middle Dutch burch, town: BURGOMASTER; d. Late Latin bur- gus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG. 5. Suf- fixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-?): FORCE, FORT, FORTALICE, FORTE!, FORTE?, FORTIS, (FORTISSIMO), FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY, (PIANOFORTE), REINFORCE. [Pok. bheregh- 140.] bhers-. Quick. Latin festindre (< *fers-ti-), to hasten: FESTINATE. [Pok. bheres- 143.] bhes-', To rub. 1. Zero-grade form with unclear suffix *(bh)s-amadho-, sand (in Greek psamathos), in Germanic *sam(a)dam, *sandam in Old English sand, sand: SAND. 2. Suffixed form *(bh)s-abh- in the further suffixed form *sabh-lo- in Latin sabulum, coarse sand: SABULOUS. 3. Suffixed form *bhs-d- in (i) Greek psén, to rub, scrape: PALIMPSEST (ii) Greek pséphos, ballot, pebble: PSEPHOLO- GY. 4, Perhaps suffixed form *bhs-ilo- in Greek psilos, smooth, simple: EPSILON, PSILOMELANE, UPSILON. [Pok. bhes- 145.] bhes-2. To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCHO-; METEMPSYCHOSIS. [Pok. 2. bhes- 146.] bheudh-. To be aware, to make aware. 1. Germanic *(for)beudan (*for, before; see per') in: a. Old English béodan, to proclaim: BID; b. Old English forbéodan, to forbid: FORBID; ¢. Old High German farbiotan, to forbid: VERBOTEN, @: Germanic *tudén- in Old English boda, messenger, hence bodian, to announce: BODE!. 3. Ger- manic *budilaz, herald, in Old English bydel, herald, messenger: BEADLE. 4, Germanic *budam in Old Norse bodh, command: OMBUDSMAN. 5. Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE. [Pok. bheudh- 150.]
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ormo- 615.] koro-. War; also war-band, host, army. I. Germanic *harjaz, army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compound *harja- waldaz, “‘army commander” (*wald-, rule, power; see wal-), in Anglo-Norman herald, herald: HERALD. II. Ger- manic denominative *harjén in Old English hergian, to ravage, plunder, raid: HARRY. III. Germanic compound *harihring, assembly, “host-ring” (*hringaz, ring; see sker-3), in Medieval Latin harenga, harangue: HA- RANGUE. [Pok. koro-s 615.] koselo-. Hazel. Germanic *haselaz in Old English hesel, hazel: HAZEL. [Pok. kos(e)lo- 616.] kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.] krau-. Also kru-. To conceal, hide. Suffixed extended form *krup-yo- in Greek kruptein, to hide: CRYPT, CRYP- TIC, CRYPTO-, KRYPTON; APOCRYPHA. [Pok. krd(u)- 616.] kred-. Framework, timberwork. Possible root. Germanic *hr6(d)-st- in Old English hrést, roost: Roost. [Pok. kred- 617.] krei-. To sieve, discriminate, distinguish. 1. Basic form with variant instrumental suffixes in: a. suffixed form *krei-tro- in Germanic *hridra-, a sieve, in Old English hridder, hriddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog- in Middle English row, roe: ROE}. [Pok. 2. krek- 619.] krem-. Wild garlic, onion. O-grade form *krom- in Ger- manic *hram- in Old English hramsan, onion, garlic: RAMSON. [Pok. kerem- 580.] kret-'. To shake. O-grade form *krot- in Germanic *hra- thaz, swift, nimble, in Old English hreth(e), nimble, quick, prompt, ready: RATHE, (RATHER). [Pok. 1. kret- 20.
1122:(see koro-). 3. Suffixed extended o-grade form *wold-ti- in Russian oblast’, oblast: OBLAST. [Pok. wal- 1111.]
1260:ARMADILLO = ar- ARMATURE ar- ARMIGER gerere ARMILLARY SPHERE al- ARMISTICE sta- ARMOIRE ar- ARMY ar- ARPENT pert ARRAIGN  ar- ARRANGE sker-3 ARRAY reidh- ARREARS re- ARREST sta- ARRIERE-BAN koro- ARRIVE rei-1 ARROGATE reg-1 ARROW arku- ARSENIC ghel-2 ARSIS wer-2 ARSON as-
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
1598:HERALD koro-
1600:HERE ko- HEREDITAMENT ghé- HEREDITY ghé- HERIOT koro-, taw- HERITAGE ghé- HERMIT er@-2 HERNIA ghere- HERO ser-1
```


## [2026-09-06T21:15:18.800Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=1\nfor i,l in enumerate(lines,1):\n    if i in (6497,6499,17260,41062): print(i,'leaf',leaf,'≈pp',(leaf-12)*2,(leaf-12)*2+1)\n    leaf+=l.count('\\f')\nEOF\necho \"=== leaf content check ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==131' KLN_1966.txt | grep -oE \"^.{0,60}\" | head -3\nawk 'BEGIN{RS=\"\\f\"} NR==131' KLN_1966.txt | grep -nE \"^ *2[0-9][0-9] *$\" | head"
}
```


### [2026-09-06T21:15:21.265Z] TOOL RESULT

```
6497 leaf 137 ≈pp 250 251
6499 leaf 137 ≈pp 250 251
17260 leaf 381 ≈pp 738 739
41062 leaf 896 ≈pp 1768 1769
=== leaf content check ===
lo-  and  melancholy. Calonyction,  n.,  a  genus  of  plant
calori-,  combining  form  meaning  ‘heat’.  —  L. calori-, 
See  caldron.
16:226
17:227
```


## [2026-09-06T21:15:25.795Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==137' KLN_1966.txt | grep -nE \"^ *2[0-9][0-9] *$|^caravan\" | head\necho \"--- 1966 harry leaf 381 page nums ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==381' KLN_1966.txt | grep -nE \"^ *[0-9]{3} *$\" | head\necho \"--- 1971 caravan ---\"\ngrep -n \"^caravan,\" KLN_1971.txt | head"
}
```


### [2026-09-06T21:15:27.573Z] TOOL RESULT

```
12:caravan
14:caravan,  n.  F.  caravane,  fr.  Pers.  karwan, ‘company  of  travelers,  caravan’,  which  is  rel. to  OI.  karabhdh,  ‘camel,  young  camel,  young elephant’.
16:caravanserai,  n.,  Eastern  inn,  esp.  for  caravans. —  F.  caravanserai,  fr.  Pers.  karwansarai,  fr. karwan  (see  caravan)  and  sarai,  ‘mansion,  inn’, which  is  prob.  rel.  to  Avestic  {trayeihti,  ‘they protect’,  Ol.  trdyate,  ‘protects’, caravel,  carvel,  n.,  any  of  various  kinds  of  light vessels.  —  F.  earavelle,  fr.  Sp.  carabela,  dimin. formed  fr.  cdrabo,  ‘a  small  vessel’,  fr.  Arab. qdrib,  ‘bark’,  which  is  traceable  to  Gk.  x£px|3o<;, 'horned  beetle;  crayfish;  a  light  ship’.  See  scarab, caraway,  n.,  a  plant  with  aromatic  seeds.  —  ME carawai,  fr.  OSp.  (=  Sp.)  alcaravea  (whence Sp.  carvi),  fr.  Arab,  al-karawiyd’ ,  fr.  a /-,  ‘the’, and  karawiyd',  fr.  L.  carum,  careum,  fr.  Gk. xxpov,  xapcov,  ‘caraway’,  which  is  of  uncertain origin.  Cp.  skirret.
22:238
23:239
--- 1966 harry leaf 381 page nums ---
20:706
--- 1971 caravan ---
39435:caravan, n. — F. caravane , fr. Pers. karwdn ,
```


## [2026-09-06T21:15:46.660Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport json,re\nm=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))['map']\ninv={v:k for k,v in m.items()}\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor pat in ['کاروان','کارزار','کرنا','کاردار']:\n    print('#####',pat)\n    for i,p in enumerate(t):\n        if pat in p:\n            print('  pdf',i,'printed',inv.get(i))\nEOF"
}
```


### [2026-09-06T21:15:48.780Z] TOOL RESULT

```
##### کاروان
  pdf 16 printed 1225
  pdf 31 printed 1240
  pdf 219 printed 1426
  pdf 295 printed 1502
  pdf 342 printed 1549
  pdf 351 printed 1558
  pdf 352 printed 1559
  pdf 423 printed 1630
  pdf 616 printed 1819
##### کارزار
  pdf 59 printed 1268
  pdf 350 printed 1557
  pdf 352 printed 1559
  pdf 367 printed 1574
  pdf 527 printed None
  pdf 565 printed 1768
  pdf 576 printed 1779
##### کرنا
  pdf 17 printed 1226
  pdf 21 printed 1230
  pdf 25 printed 1234
  pdf 199 printed 1406
  pdf 215 printed 1422
  pdf 216 printed 1423
  pdf 217 printed 1424
  pdf 219 printed 1426
  pdf 558 printed 1761
  pdf 563 printed 1766
  pdf 595 printed None
  pdf 671 printed 1875
  pdf 674 printed 1877
##### کاردار
  pdf 47 printed 1256
  pdf 351 printed 1558
```


## [2026-09-06T21:15:56.307Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (350,351,352):\n    print('#### index',i)\n    print(t[i][:3000])\nEOF"
}
```


### [2026-09-06T21:15:57.912Z] TOOL RESULT

```
#### index 350
[pdf page 351]
—Seoa- ‏کلدی‎

. 9 ‏بروزن شادی» بانی‌است | کوبند ۴ - و بمعنی سخن حمکفته‌الد‎ - )۱( ۱ GOT
‏بمعنی‎ ey ‏بیار خوشبوی و آن از درختی حاصل میشود کار ]یب - یک رای‎
. ٩ ‏بافراط خوردن باشد‎ ye | GS ‏بثیرازی کل‎ YT ‏مانئد درخت خرما و‎

کونند. و درملك دکن کوره ‎JEL‏ وسکون کار اس ه با تاك الف کتیده و شین
‎sly‏ و قتح رای ب‌نقطه خوانند . شراب‌آن ‎CP‏ | بی‌نقطه بتحتانی رسیدء » نام جانورکی است که
‎aT‏ ,کند وجذام را نافم با

پثه وجدری ند وجدام را ‎CN‏ باشد. آواز ‎oF‏ دارد, وبعض یگویند مرغی‌است خوش

۷ ‏آواز‎ | gee ‏ع بسکون رای بی نقطه ؛‎ FIT

صنمت و هنر وپیشه باشد - وبمعنی کشت‌وزراعت کار ] گاه * - با کان فارسی بر وزن
هم‌آمده است - و امر بزراعت کردن هم ‎Se‏ | پاپاشاه , کسیراگوبند که ازحقیقت‌کار, آگاء (۷)
یعنی بکار وزراعت کن ۴ م وجنك وجدالرا ‎ad‏ | و با خبر باشد - و مردم صاحب فراست ومنهیرا

‎Ae )۱(‏ « چش: ‎GIS‏ . (0) چش :+ بود .

‏۱ - (عر) کادی با کانی = ‎Pandanus odoratissimus‏ درختی ‎col‏ شببه‌بنخل
که در هند » چین و جنوب عربتان روبد ۰ « دزی ج ۲ ص 4۳4 .

‏۴ - ابرانی.باستان - ‎oy Col. okdrya‏ - 68۲۷2 ۰ بپلوی ۵۲ ( شغل ‎(A.‏
‏« نیب ‎VY) oT‏ هرن در اشتقاق « کار» گوید : اوستا - 12۲2 در ]6۵۲2۸۷۵10 ؛ پهلوی62۲
‎kara - 2 Col‏ - ( عمل .کار ) « اسشق ۸۳۱ ۰ از مصدر ‎kar‏ اوستابی و پارسی باستان
بمعنی کردن ۰ شهمبرزادی ‎de kar‏ . ۲ ص ۱۷۷ * , گیلکی ‎har‏ ممرب‌آن «کار» « دزی ج
۲ص ۳4 . ۴ - از مسدر «کاشتن » . ۴ - ی : کارزار .

‎٩‏ - نیز پسوند شغل » در هندی باستان - ‎kara‏ — پهلوی ‎kar‏ قی : فارسی
‎avy gel > gar‏ درکردی نیز - کار (هرزه کار) «ژابا 44۲>. این ‎sigs‏ اسماء دال‌پرمبالفه
میسازد : ستمکار , خطاکار ۰ زبان کار .

‏1 = بس‌بس‌ایدلز کارآب, که عقل هت ازآب کار او بیزار . « خاقانی شروانی. ص۲۰۱ >.

‎LI? - ۴‏ حکیم‌وطبیب وبهر کاردانا , زیراکه «آسی؟ درعربی بممنی طبیب‌وتجربه
کار باشد » و بمضی گفته‌اند نام حکیمی است که پش‌سلطان محمود س رکذشت پیشرنیان‌مبخواند.
فلکی (شروانی) گوید :

‏رند بحطرت ‎py‏ زمان گروهی‌نو بشکل بوعلی و گوشیار و کاراسی.
و خاقانی ( درتحفة ‎gil all‏ ) گوبد :
قمری ز تو پارسی زبان کشت کاراسی کارنامه خوان گشت.

‏و بعضی درین بیت گفتداند نام مرغی است که آواز حزین دارد و دراین تأمل است چه بمعنی‌اول
( حکیم ) نیز مناسب است » وموید ‎gpl‏ معنی آنت که برای هرمرغی ‎eh‏ بیت تعرریفآورده و
ظاهرآ که بمعنی مرغ ‎gil ule SG‏ بیت .» « رشیدی». باید دانست که ‎BE AIS?‏
بوده « شاهنامه خوان » وراوی کناب « زار ‎gly » GLI‏ ندیم عضدالدوله ‎yall tay‏ دیلمی ‎age‏
‏که سپس بخدمت محمود غزنوی شتافت و در4۲۱ محکومت قروین مثصوب گردید و در 4۲۲ با
‎ole ۳‏ ظلم در آنجا بقتل رسید. )4 : کارآسی شاهنامه خوان بقلم آقای عبای اقبال .با گار
۲ ص*۲ ۲۲ . ۸ - ‎AST IS? OT Gare‏ فرهنگتان ‎MTT IS?‏ را بجای‌پلیس
مخفی 616001۷6 ‎a,‏ > واژه‌های نو . فرهنگتان ص۰۹۹ .

#### index 351
[pdf page 352]
—\oo8—

۱ ‏می‌دمیکه‌اخبار باطرآف‌برسانند‎ ets S55
AST Sy ‏؛‎ lS ‏و قاصد وجاسوس را یز‎ -
‏است که دانابان و اصحاب فراست‎ STB ear
‏و اهل تجربه و منجمان باشند چه منجم را نیز‎
. ‏کارا که میگونند‎

کار با ۴ » با بای ‎uml‏ بروزن پارسا »
مخفف‌کاء ربا است و ‎ay yee OT‏ است.

کار بان ۴
و استر و خر الاغ را گویند - و بمعنی قافله
وکاروان هم‌آمده است چه در فارسی با و واویپم
تبدیل ‎ttle‏ +

‎cell tae - Oe WIS‏ و فرمان
برداری کردن باشد .

‏کار یچ = بروزن مار پیج(۱) ؛ جامه
و پارچه‌ای را گویند که کشيده گران ‏ وگلایتون
دوزانلفافة کار خود سازند بجت محافظت آن.

‏کار ن ۴ © بفتح فوقانی وسکون نون»
عنکبوت را گویند. اکر پای عنکبوت بر کسی
بندند که شبها تب میکرده باشد تب ازومفارقت
کند. ۱ ‎eS‏ عنکبوت را با علكرومی‌بخور
کنند تمام بگریزند والا بمیرند .

‏= بروزن ساربان . فطارشتر

‏(۱) خم۱ : بارییچ .

‏کاردان فلك :

‏کارتنه * - سکن نات وفتح فوقانی

‏و تون » بمعنی کارتن است که عنکبوت باشد
و آنراگاد قنلك حم خوانند (۷) - ویفتح‌تالت

‎pal, ۰ ‏رابع بمعتی شنبلیت است‎ os
. ‏باشد معروف وبعربی حلبه گویند‎

‏کار چراغ خلوتیان ه کنابه‌از
آفروختن بدوام ‎ath‏ - و روشن أختن‌جای‌تارك
را نیز ‎a gh‏ - و دوده افکندنرا هم گفتهاند.

‏کار چوب = پروزن مارچوب . چویپا
‎YT,‏ باشد که جولاهگان جامهای ‎LS‏ فراز
کرده را با آنها ببافند وبعربی منشج گونند.

‎ples ‏ازدنا‎ ats” = ‏قلاگ‎ bu
Maslel ‏بطریق‎ aS ‏را نیز‎ oT, - ‏است‎

‏کار داد ۷ ه بادال ابجد بروزن‌کامکار,
وزیر پادشاء را کویند وکارداران جمع آنت که
وزیران باشند .

‎goof‏ ۷ - بادال ابجد بروزن‌ساربان,
بمعنی کاردار است که وزیر باشد .

‏کاردان ‎MS‏ - کنایه از ‎SS‏
‏عطارد است - و کواکب دیگر را نیز گفته‌اند
ومجموع را کاردانان فلك میگونند .

‏(۷) چك . چش: میگوند .

‏۱ - مخفف‌آن «کارآ که»: خبرشد ازابشان‌بکارا گپان به‌پیرانبگفتنديك‌بك مهان..
۶ فردوسی طوسی . شاحنامة بخ ج۳ ص۸4۰ *
۴ < کاروان (هم.) .
‎F‏ کارتنه ‏ کارتنك سم کرهءتن ‏ کروننه ‎pa)‏
‏۷ - از:

‎. ‏رك : کاهریا‎ ۴
Aga) i= 5

‏کار + دار ( دارنده ). امروزه بمعتی« مأمور سیاسی است که در غیاب‌وزیررمشتار

‏با سفی ‎By ST‏ نمابندکی دولت خود را تزد دولت دبگری عهده‌دار مشود و پیشتر«شارژدافر»

‏گفتهمبشد»(فرهنگتان. واژه‌های نوص‌ص۹). ۰ ۷- از: کار + دان (داننده) اغقبمعنیمطلم‌وخبیر.
۵ کارد - بسکون سوم » اوستا - 62۳648 (کارد +

‏چافو) ؛ پهلوی ‎kart‏ ؛ فی‌هندی باستانی - ‎krntéti kart‏ لو ‎Scum‏

‎(ou)‏ کردی ‎kird .kit‏ استی ‎k'ard‏ )35( تست کار

‏7 ( بربدن ). باوچی ‎gel 1768 ۰ kare‏ ۸۳۲ ؛ آلت برنده‌ای از آهن وفولاد

‏که دارای ‎ates‏ وتفه است .


#### index 352
[pdf page 353]
lev ‏کاردانك‎

کاردا فاك ۱ » بفتح نون وسکون‌کاف. | باشد - وآسمان را نیز گوبند بطریق اضافه .
پرندهء‌است که آنرا کاروانك میگوبند که بجای کار گاه کن‌فکان ۱ - کنابه ‎Lisl‏
‎Jb‏ واو باشد وبعربی کروان خوانشد. ومافیها است که موجودات دارین باشد.
‎MII‏ ۲ - با زای نقطه دار بر وزن کار گر ۷ ۰ بقتح ‎GE‏ فارسی بر وزن
کام‌کار ؛ بمعنی ‎ie‏ وجدال باشد ۴ . تاجور , مخفف‌کاریگر است۸ که خداوندوصاحب
کارسان ۴ « با را وسن‌بی‌قطه بروزن | کار و کار کننده باشد - و بمعنی أثر کننده
پاسبان » ظرفی باشد مانند صندوقی و انرا از | ‎Shee‏ همهست - و بمعنی صفت شخص‌هم بنظر
چوب و کل هم سازند ونان حلوا وامثال آن‌درآن | آمده است٩‏ ۰
گذارند . ‎LFS‏ - بکس ‎GE, alt‏ فارسی*۱
کار شناسان * - بکرتین نقط‌دار. | وتحتانی بالف کشيده ‏ بمعنی پادشاه ‎pay‏ وکار
کنابه از دانابان و منجمان و اصحاب فراست | فرما وکاردان ‎ath‏ - و هريك ازعناصر اربعه را
و ‎Jal‏ تجربه و ‎se‏ و قانون دانان و عارفان | نز کفته‌اند. #
ویخردان وعاقلان باشد . کار نامه ۱ با نون بالف کشیده وفتح
کار گاه ‎CUS‏ - کنایه از ‎lus‏ وعالم میم ,کار ‎sy‏ وصنمتی را گویند که کم کسی

۱ - مسحف «کاروانك» (هم) . ۴ - پهلوی 12۳6[8۴ م رکب از: کار بمعنی
‎Ke‏ (فس: پارسی‌باستان- 68۲2 (سیاء) ؛ لیتوانی6۵۲85 (جنگه), کتی ‎harjis‏ (سیاء) + زار
‎kAricat syle js ۳:‏ ,۲۵112۵۴ = پازند ‎KArizar‏ قس: کاروان«هوبتمان
: بارتولمه ‎Ne‏ تب رگ۱۲۱۵ . «زار» پوندمکان ومحل‌است ؛ قس: لالهزار.مرغزار.

۴ ~ چورای وعزم و ضمیر تو هست؛ حاجت لیست

خداییگان: جهان را بکارزار و بکین ۰
«معزی ‎Soles‏ ص ‎VEO‏

۴ = کرمان « جهانگیری» - از : کار ‎OL‏ (پوئد مکان ) ؛ محل کار » کارگاه
« دارمستتر - تتیعات ج۱ ص۲۹۹ . ‎ee?‏ «کارشتای » از: کار( شنای (شناسنده)؛
آنکه در کارها خبیر باشد « دارستتر. تبمات ج۱ ص‌۳۱۵» فرهنگتان «کار شناس » را بجای
‎Jol‏ خبره 6۳6۲4 ‎Sy‏ « واژه‌های نو . فرهنگتان ص ‎OW‏

۱ -فی : انما امره آذا ‎OMEN‏ بقولله کن فبکون ( سورة ‎۳٩‏ (بس) ‎ART‏

۷ - از : کار (- گر ( پسوند شفل ) « دارمستتر . تبعات ‎ele‏ ۲۹۲ >

۸ -«کاریگر » خود لفتی‌است دره کارگر» پاشباع کسره‌ای که در ببض لهجه‌ها به راء
‎SIT‏ دهند . ‎٩‏ - مطلق کار کننده - عمله , فعله . *۶- صحیح « کارکیا »
‎GK‏ تازی است ‎yy‏ : کار کیایی(ح).  ‎9٩‏ پهلوی کارنامك ‎mamak‏ - 627 (کتاب‌اعمال)
« نب رکه ص۱۲۱ » ونیز بمعنی تاریخ وتاربخچةٌ زندکی اشضاص . کارنامك ارتخشیر ‎OBL‏ نام
‎ioe DL,‏ است بیهلوی وآن س رگذشت اردشیر ‎GEL‏ است :

فانة کپن ‎LUIS‏ بدروغ بکارتابد » رو در دروغ رنج مبر ‎ .‏ «فرخی‌سیتانی ۴۹۷.

۶ کار کیایی - از کار کیا )4 ‎Ls:‏ )+بی ( اس مصدر ) ؛ کارفرمابی ؛سالاری »
پادشاهی : * ایتج می‌بینی هم شعار پادشاهی وآتار کار کیابی اوست. ... » « مرزبان نامه‌چاپ‌دوم
تهران ص۳۸ با ‎gules‏ حاشیه *.
```


## [2026-09-06T21:16:23.207Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport json\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'کرنای' in p or 'كرنای' in p:\n        print('idx',i,'pdf',i+1,'printed~',i+1+1207)\nEOF"
}
```


### [2026-09-06T21:16:25.052Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:16:28.634Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if re.search('کرنا', p):\n        # print snippet\n        for m in re.finditer('کرنا', p):\n            print('idx',i,'printed~',i+1+1207,'::', p[max(0,m.start()-120):m.start()+160].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-06T21:16:30.519Z] TOOL RESULT

```
idx 17 printed~ 1225 ::  )۰  ‎Jy ۱‏ : شال نمه .  ‏# شاگرد - یکسر سوم ‎inal)‏ م رکزی) ‎(CLS.‏ 5282۳0 کنابادی ‎shagerd‏  ‏«کتابادی» ۰ کلپایگانی و کرنانشاهی 5118670 «قاسمی» هوحدت» ؛ ‎SST‏ نزد مملمواستاد کسب علم وهتر کند » کسکه در مدرسه تحصیل داش کند » متملم ۰ ‎aul‏ - کسیکه در ‎ap‏ ‎ot‏ خدمت کند ‎KTH‏ در ‎c
---
idx 21 printed~ 1229 :: ند وبریکطرف ‎oF‏ ولایت بیابان ریک است که کافران در ‎OF‏ ‏مقام دارند ‎٩‏ - و بای رومی را نیز گفته‌اند که ‎pe‏ برادر کوچك کرنا ‎ath‏ وآنرا نای‌روین هم خوالند . _  ‏(۱) چك :- ابجد .  ‏۱ - رك: شاله سر . چون برادرت داد در يك شعر سنایی غزنوی. «فرهنك ‎«lls‏  ‏۴ - «شاوران ‎dad‏ شروان است
---
idx 25 printed~ 1233 :: ۵ .۷  ‏شاه ‎Sate‏ = بکس الث وزای ‎abe‏ ‏دار بالف کذیده و شم واو وسکون لام » اشاره بسلطان محمود سبکتکین است.  ‏شاه‌ز نگ بکرناك وفت‌رابم‌وسکون لون وکاف‌فارسی,شب را کویشدوبعربی‌لیل‌خوانند.  ‏شاه زيره - ‎ge‏ زبرة بز رکه و دام کروبا است که ‎ag SLT‏ و نان خواه خوانند 259 رومی همان است.
---
idx 199 printed~ 1407 :: ا نیز کنته‌اند ۴  غر ناطه - بفتح اول وسکون انی‌ونون بالف کشیده وطای حطی مفتوح . نام ولایتی‌است درهندوستان وبز بان آ نجا کرناتك خوانند ,وبسنی  گونند معرب کرناتك است ۴ غر فبه - بنم اول و ثانی و سکون ‎HWE‏ ‏و فتح بای ابجد , بانگ و فرباد وشور و مشقله و خروش را گویند ۴  هم آمده است عر
idx 199 printed~ 1407 :: اول وسکون انی‌ونون بالف کشیده وطای حطی مفتوح . نام ولایتی‌است درهندوستان وبز بان آ نجا کرناتك خوانند ,وبسنی  گونند معرب کرناتك است ۴ غر فبه - بنم اول و ثانی و سکون ‎HWE‏ ‏و فتح بای ابجد , بانگ و فرباد وشور و مشقله و خروش را گویند ۴  هم آمده است عر لمیك = ضماول‌ونانی .ماضی‌غرنبیدن
---
idx 215 printed~ 1423 :: گویند. .  ‏غند رود ۷ ‎er‏ اول وسکون انی وثالك و رای بی نقطه بواو کشیده و بدال ابجد زده + بممنی ‎pit‏ باشد که براد رکوچك کرنااست و چون در ‎pad‏ آنرا ‎com‏ فراهم آمدن وجمع شدن‌مردم‌مینواخته‌اند ‎A‏ وغند بمعتی‌جمع‌وفراهم  ‎8c 4°‏ صفحه‌فیل. ۳ هه غنعه  ‏۴ - نیز « غنجه , رعنایی وغنج نا
---
idx 216 printed~ 1424 :: یز کوبند - ونوعی از عنکبوتراهم گفته‌اند که زهردارو گزنده ‎thes‏ وعربان رتیل خواشش ۴ - و نقیر را نیز کوبند که برادر کوچك کرنا است ‎٩‏ .  ‏غنفهدروك ۱ - بر وزن سرمه سود  ‏(۱) چك : - شطددار .  ‎. ‏غنده‎ UY  ‏۴ هس غندم (هم)  ‎۱6۲6  ‏بمعنی غندرود است که نفیر برادر کوچك کرنا باشد . کوین
idx 216 printed~ 1424 :: ك ۱ - بر وزن سرمه سود  ‏(۱) چك : - شطددار .  ‎. ‏غنده‎ UY  ‏۴ هس غندم (هم)  ‎۱6۲6  ‏بمعنی غندرود است که نفیر برادر کوچك کرنا باشد . کویند "در زمان قدیم ‎Lt‏ بجهت جمع آمدن و کرد شدن مردم‌میتواخته‌اند ووجه‌تسيةً ‎OT‏ هم ‎SL‏ جمعیت است چه غنده بمعنی جمع و فراهم آعده ورود ساژ رااگوین
---
idx 217 printed~ 1425 :: ول و سکون ‎GU‏ . صدا وآواز بیاربلندرا کونند ‎ash‏ فریادیکه‌بهادران در روز چنگه کنند ‎٩‏ - و صدای رعد و آواز کوی ‎pity‏ وکرنا وامثالآنها را نی زگفته‌اند.  ‎GE‏ = بت اول و کس بای ابید  ‏(۱) چك : که .  ‏۱ رد : غدودن . ۴ - بناپارسایی ‎SG‏ نفنوی  ‏۴ - اسم مفعول از « غنودن ۰ .  ‏۵ - یم
---
idx 219 printed~ 1427 :: ء و غور و فراء از بلاد خراسان ( قدیم ) است , چنانکه الوری گفته :  ‏عرصهٌ مملکت غور چه نامسدود است  ‏که درآن عرصه چنین لشکرنامسوداست!  ‏با این تقاصیل صاحب جهاد‌گیری غور را « غوژه » خوانده و « غنچه » فپمیده , و ‎SV‏ منظور لالم غنچه بودی چرا « خوژه » فرمودی ‎low ply‏ اول قارورکسرت ف
---
idx 558 printed~ 1766 :: باستان-6368 - ؛ پهلوی 62۳ - ‎at gel‏  ‏6 - دنا همه در غرور دارد باری ‎wt‏ غره مشو ز روز ‎GIS IS‏  ‎Jit‏ جهانگیری‌بدون ذ کرنام‌شاعر. ساکنون « کاری» را بارابه‌ای که بااسب کشیده شود . اطلاق کنند . اين لفظ هندی است‌ودرهندی پمعتی مطلق گردرن است ودر قرن ‎asl‏ داخل فارسی شده «فرهنکه نظا
---
idx 563 printed~ 1771 :: ‌وسکون‎ ‏ها ورای قرشت » بمعنی کاو پیکر است که کرز‎ ‏فربدون باشد و آن را بهیات س رکاومیش ازآهن‎ . ‏صاخته بودند‎ cab le ‏بکرنالت بروزن‎ - OIL” . ‏خم ۱ : فرمانیون‎ (1) ‏شمال انگیخته هرسو خروشی‎ - ۱ . ‏کاوچشم‎ : tte ‏دزی ج ۲ ص‎ : Ay . ‏:گارچشم‎ af  مرش را بدین ‎ee ISBS‏  کاور  زند وپ
idx 563 printed~ 1771 :: دوسکونلام. بد دل ونادان واحمق را ‎aS‏ .  گاودم - ‎pe‏ رابع و سکون میم » بمعنی نفیرباشد که برادر کوچك کرلاست؛وبسنی کوبند کرنا است که بعوبی بوق خوانند۴ .  اوه فیال - مرجیزی رشکلی که‌يك سرآن پهن وسر ‎Ss‏ آن باريك باشد و ‎UT‏ ‏مخروطی کویند .  گاو دوش" - فرفی ‎ah‏ سر آن کشاده وین آن ت
---
idx 595 printed~ 1803 :: کر کر ( بفتح اول و سوم , ممرب) شهری به‌اران (آذربابجان) ترديك بیلقان - ابن‌ااثی ‎Sa ST‏ کرحصنی است ترديك ملطیه - ویز کر کرناحیه ایست از بفداد - و بیزحصنی است ‎ge‏ سمیاط و حصن زیاد , وآن ‎al‏ ای ‎Soy‏ خراب شده « ممجم‌البلدان ‎٩‏ + ‎«was LT ۴‏ 55 خوانند « جهانگیری ‎ol‏ سوت است. قس:
---
idx 671 printed~ 1879 :: سیاروانبوه نیزآمده است وباین ععنی عم ‎ys‏ گفته نمشود؛ و بفیر اژین سه‌محل ‎cle ye‏ دنگراستممال‌نشده ات ؟ .  ‏لاخشته ۳ - بکرنالت بروزن آغشته, نوعی از آش آرد باشد ؛ و بسضی گویند آش‌تتماج است +  ‏لاخشه ۴ < بروزن فاحته.بمعنیلاختته است که نوعی از آش‌آرد باشد ؛ گویندآش‌تتماج است . لاخه 
---
idx 674 printed~ 1882 :: : لاغیه .  ‏۴ در عقار ۷۱۵ آمده : « لاعية ( با عين مهمله ) هی الحلبلاب » و بمجمية الاندلی لختر ‎Jy‏ ( 126087101 ) و قد ‏ کرناها من اصناف البتوع .» در بسض نخ ‎ate‏ ابن الببطار دلاغیه » آمده ‎oly‏ صحیح با عين مهمله است = ‎Buphorbe‏ )3( « عقار ۷۱۵ ف >.  ‏۵ رك : منتهی‌الارب ؛ و رك : ل
---
```


## [2026-09-06T21:16:40.946Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T21:16:40.953Z] TOOL RESULT

```


```


## [2026-09-06T21:16:45.016Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%C3%B3ryos",
 "prompt": "Give the full reconstruction, gloss, and all descendants listed (especially Proto-Iranian/Old Persian kāra-, Proto-Germanic *harjaz, Balto-Slavic). Quote the etymology section."
}
```


## [2026-09-06T21:16:46.773Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B1%D9%88%D8%A7%D9%86",
 "prompt": "Quote the Persian etymology of کاروان (kārvān) in full, including Middle Persian form and any reconstructed Old Iranian etymon, and the list of borrowings into other languages (Arabic, Italian, French, English)."
}
```


### [2026-09-06T21:16:49.848Z] TOOL RESULT

```
# Proto-Indo-European *kóryos

**Full Reconstruction:** *kóryos

**Gloss:** war, troops

**Etymology:** "From [\*ker-](/wiki/Reconstruction:Proto-Indo-European/ker- "Reconstruction:Proto-Indo-European/ker-") ("army")."

**Descendants Listed:**
- Proto-Baltic: *karjas
- Proto-Celtic: *koryos
- Proto-Germanic: *harjaz

**Note:** The page does not include Proto-Iranian/Old Persian descendants. The Germanic descendant *harjaz is documented, along with derived forms *harjanaz and *harjōną, but Iranian cognates are not mentioned in this entry.
```


### [2026-09-06T21:16:52.156Z] TOOL RESULT

```
# Persian Etymology of کاروان

**Etymology Source:**
"From Middle Persian _kʾlwʾn'_ (kārawān, 'caravan; military column'). See descendants there."

The Wiktionary entry does not provide a reconstructed Old Iranian etymon beyond the Middle Persian form.

**Key Borrowings into Other Languages:**

The word spread extensively through Medieval Latin (_caravana_) into European languages:

- **Arabic:** قَيْرَوَان (qayrawān)
- **Italian:** carovana, caravana
- **French:** caravane
- **English:** caravan

Additional pathways include borrowing via Old Anatolian Turkish and Ottoman Turkish into Balkan and Eastern European languages, plus independent borrowings into Turkic, Indo-Aryan, and other language families documented in the descendants section.
```


## [2026-09-06T21:16:55.253Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Middle_Persian/k%CA%BE%C4%81rw%C4%81n",
 "prompt": "Etymology of Middle Persian kārawān 'caravan, military column' - what is it derived from? Quote."
}
```


## [2026-09-06T21:16:56.201Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/caravan",
 "prompt": "Quote the full etymology entry for caravan, and also anything said about 'van' (vehicle) as a shortening."
}
```


### [2026-09-06T21:16:57.289Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T21:17:04.162Z] TOOL RESULT

```
# Etymology of Caravan

**Full Etymology Entry:**

"1590s, in reference to in North Africa or western Asia, 'company of travelers, pilgrims, merchants, etc., going together for security,' from French _caravane_, from Old French _carvane_, _carevane_ 'caravan' (13c.), or Medieval Latin _caravana_" — words derived during the Crusades via Arabic _qairawan_ from Persian _karwan_ "group of desert travelers" (connected to Sanskrit _karabhah_ "camel"). Later usage (1660s-1670s) expanded to describe any large traveling group with baggage, then large covered carriages and mobile dwellings. Modern British usage (1930s onward) treats it similarly to the American camper or recreational vehicle.

**On "Van" as a Shortening:**

The word "van" originated in 1829 as "shortened of _caravan_" describing "covered truck or wagon." The entry notes that scholars "suggest _caravan_ was perhaps regarded as _*carry-van_." Originally employed for moving household goods, it later expanded to motor vehicles used by tradespeople and hippies for transport and delivery services.
```


## [2026-09-06T21:17:10.507Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/harjaz",
 "prompt": "Quote the etymology of Proto-Germanic *harjaz, its gloss, derived terms (*harjōną, *harjabergō, *harjawaldaz etc.) and descendants."
}
```


## [2026-09-06T21:17:11.947Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D8%B1%D8%A8",
 "prompt": "Quote the Arabic entry for كرب (karb): root, meaning 'grief, anguish, sorrow', etymology if given, and any Persian section for کرب."
}
```


### [2026-09-06T21:17:16.112Z] TOOL RESULT

```
# Proto-Germanic *harjaz

**Etymology:** Derived from Proto-Indo-European *kóryos ("war, troops"), from *ker- ("army"). The entry notes "Cognate with Old Irish cuire, Lithuanian kãras, Ancient Greek koíranos, Old Persian k-a-r."

**Gloss:** The term means both "army" and "army leader; commander; warrior."

**Selected Derived Terms:** The text lists *harjōną, *harjaberhtaz, *harjawaldaz, *harjamann-, and *harjanaz among numerous compounds.

**Key Descendants:** West Germanic forms include Old English here (Modern English "here" in compounds), Dutch heer, and German Heer. Norse descendants include Old Norse herr. Gothic harjis and Vandalic *haris represent East Germanic reflexes.
```


### [2026-09-06T21:17:17.052Z] TOOL RESULT

```
# كرب (Karb) - Wiktionary Entry Summary

**Root:** ك ر ب (k r b)

**Arabic Noun Definition:**
"worry, sorrow, care, grief, apprehension, concern, anxiety, fear, heartache, agony, affliction, anguish"

**Etymology:** The page does not provide an etymology section for the Arabic entry, only noting it as a root term.

**Persian Section:** There is no Persian (فارسی) section on this page. The entry only covers Arabic and Chadian Arabic, with a reference note directing to the Persian variant کرب at the top.
```


## [2026-09-06T21:17:23.458Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8",
 "prompt": "Quote the Persian entry for کرب (karb): meaning and etymology (is it from Arabic?)."
}
```


## [2026-09-06T21:17:23.955Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/harbor",
 "prompt": "Quote the full etymology of harbor (noun), including Old English herebeorg and the here 'army' element."
}
```


### [2026-09-06T21:17:26.996Z] TOOL RESULT

```
# Persian Entry for کرب (karb)

**Meaning:** The word کرب (karb) refers to the field maple, a type of tree with the scientific name *Acer campestre*.

**Etymology:** According to the Wiktionary entry, this term was "Borrowed from Mazanderani." So it is not from Arabic, but rather adopted from the Mazanderani language into Persian.
```


### [2026-09-06T21:17:30.739Z] TOOL RESULT

```
# Etymology of Harbor (Noun)

According to the Online Etymology Dictionary, the noun "harbor" originates from Middle English *herberwe* meaning "temporary dwelling place, quarters, lodgings; an inn." 

The source traces it back to Old English *here-beorg* (West Saxon) or *here-berg* (Anglian), denoting "lodgings, quarters." This derives from a Proto-Germanic compound *harja-bergaz* meaning "shelter, lodgings," combining *heri* (meaning "army, host") with *burzjan-* (meaning "protection, shelter").

The *here* element, referring to an armed force or military group, appears in related Germanic languages. The second component connects to the PIE root *bhergh-*, which means "to hide, protect." This etymological path reveals that the modern sense of a sheltered waterside location developed from the original military sense of providing quarters for troops.
```


## [2026-09-06T21:17:40.708Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/garbo",
 "prompt": "Quote the Italian entry/entries for garbo: all senses (grace/politeness, and any 'tart/sour/bitter' sense) and their etymologies (Germanic *garwa vs *harwa, Arabic qālib, etc.)."
}
```


## [2026-09-06T21:17:42.501Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%B1%D8%A8/",
 "prompt": "Quote the فرهنگ معین and دهخدا entries for کرب — meaning and origin tag (e.g. [ع.] Arabic)."
}
```


### [2026-09-06T21:17:47.738Z] TOOL RESULT

```
# Italian Entry for "Garbo"

## Senses

The Italian entry presents these meanings:

1. **Politeness/Grace**: "politeness, gentleness, tact, grace"
2. **Form**: "graceful form"
3. **Nautical**: "curvature of the hull"

There is no 'tart/sour/bitter' sense listed in this entry.

## Etymologies

The entry provides two competing origin theories:

**Primary etymology**: Borrowed from Old High German *garwi* ("dress; equipment; preparation"), from Proto-Germanic *garwijaną* ("to prepare"). The entry notes: "More at garb."

**Alternative etymology**: The entry states it is "perhaps borrowed from Arabic قَالِب (qālib, 'model, outline'), from Persian کالب (kâlob, 'form, mold'), from Ancient Greek κᾱλοπόδιον (kālopódion, 'shoemaker's block')..." with a possible connection to English "galoshe."

The entry does not mention a *harwa root in either etymology.
```


### [2026-09-06T21:17:49.304Z] TOOL RESULT

```
# کرب - Dictionary Entries

## فرهنگ معین
**Origin tag:** [ع.] (Arabic)

"اضطراب ، وحشت ، اندوه . ج . کروب"

Translation: disturbance, fear, sorrow (plural: کروب)

## لغت نامه دهخدا
**Origin tag:** [ع اِ] (Arabic)

"اندوه دم گیر. ج ، کُروب"

Translation: suffocating sorrow (plural: کروب)

The Dehkhoda entry additionally defines کرب as an emotional state that "suppresses breath" and provides various related terms including تاسه (anxiety) and تلواسه, with citations from classical Persian sources.
```


## [2026-09-06T21:18:04.110Z] TOOL CALL #45: Bash

```json
{
 "command": "ls site/pages/274.jpg 2>/dev/null; pdftoppm -f 274 -l 274 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg274 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T21:18:06.526Z] TOOL RESULT

```
site/pages/274.jpg
total 19284
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:18 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     374 Sep  6 17:16 agents.txt
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
-rw-rw-r-- 1 sfmqrb sfmqrb  157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65729 Sep  6 17:10 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44171 Sep  6 17:16 pg277.png
```


## [2026-09-06T21:18:09.626Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg274.png"
}
```


### [2026-09-06T21:18:10.105Z] TOOL RESULT

```

```


## [2026-09-06T21:18:10.102Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T21:18:36.355Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Harry",
 "prompt": "Quote the entries for Harry (masc. proper name) and harry (verb) — their etymologies."
}
```


## [2026-09-06T21:18:37.208Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Harold",
 "prompt": "Quote the etymology of the name Harold, and if present on the page also Herbert, Herman, Walter, Oliver."
}
```


### [2026-09-06T21:18:41.211Z] TOOL RESULT

```
# Etymology of "Harry"

## Harry (masc. proper name)
"A familiar form of Henry." The etymology notes that the overwhelming number of Harris and Harrison surnames suggests "Harry," not "Henry," was the Middle English pronunciation of Henry.

## harry (verb)
"Old English hergian 'make war, lay waste, ravage, plunder,' the word used in the Anglo-Saxon Chronicle for what the Vikings did to England." It derives from Proto-Germanic *harjon, ultimately tracing to the PIE root *korio- meaning "war" or "war-band, host, army." The sense weakened to "worry, goad, harass" around 1400.
```


### [2026-09-06T21:18:42.605Z] TOOL RESULT

```
# Etymology Response

## Harold
According to the page, Harold is a "masc. proper name, Old Norse _Haraldr_" derived from "Proto-Germanic _\*harja-waldaz_ 'army commander.'" The first element relates to "harry" (war/armed force), while the second connects to Proto-Germanic _\*waldan_, meaning "to be strong." The name shares etymological roots with "herald."

## Herbert, Herman, Walter, Oliver
These names do not appear in the provided etymonline content about Harold.
```


## [2026-09-06T21:18:46.844Z] TOOL CALL #49: WebSearch

```json
{
 "query": "italiano \"garbo\" aspro agro etimologia germanico *harw vino garbo acido Treccani"
}
```


## [2026-09-06T21:18:48.736Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D9%86%D8%A7",
 "prompt": "Quote the Persian entry for کرنا (karnā/kornā): meaning and etymology (Middle Persian, Sanskrit karṇa, etc.)."
}
```


### [2026-09-06T21:18:55.164Z] TOOL RESULT

```
Web search results for query: "italiano "garbo" aspro agro etimologia germanico *harw vino garbo acido Treccani"

Links: [{"title":"Agro¹ - Significato ed etimologia - Vocabolario - Treccani","url":"https://www.treccani.it/vocabolario/agro1/"},{"title":"Agro¹ Sinonimi e Contrari - Treccani","url":"https://www.treccani.it/vocabolario/agro1_(Sinonimi-e-Contrari)/"},{"title":"Garbo³ - Significato ed etimologia - Vocabolario - Treccani","url":"https://www.treccani.it/vocabolario/garbo3/"},{"title":"Garbo - Significato ed etimologia - Ricerca - Treccani","url":"https://www.treccani.it/vocabolario/ricerca/GARBO/"},{"title":"Agro- - Significato ed etimologia - Vocabolario - Treccani","url":"https://www.treccani.it/vocabolario/agro/"},{"title":"Germanico - Significato ed etimologia - Ricerca - Treccani","url":"https://www.treccani.it/vocabolario/ricerca/germanico/"},{"title":"Agro - Significato ed etimologia - Ricerca - Treccani","url":"https://www.treccani.it/vocabolario/ricerca/agro/"},{"title":"Agro: significato Dizionario Italiano","url":"https://sapere.virgilio.it/parole/vocabolario/agro"},{"title":"GARBO - Treccani - Treccani","url":"https://www.treccani.it/vocabolario/ricerca/GARBO/5/"},{"title":"agro - Wikizionario","url":"https://it.wiktionary.org/wiki/agro"}]

I've performed the web search and found relevant information from Treccani. Here's what I found:

**For "agro" (sour/acid/tart):**
According to Treccani, "agro" comes from Latin "acer acris," related to "acutus, acetum," etc. It describes a complex flavor linked to acidic substances, typical of lemon and unripe fruit, and figuratively means sour, pungent, unpleasant, revealing ill will.

**For "garbo" (grace/elegance/courtesy):**
Treccani indicates that "garbo" probably comes from Arabic "qālib" meaning "model". It refers to grace, elegance, beautiful manner in movements and conduct, especially in dealing with people, and also courtesy and propriety.

Regarding the Germanic etymology (*harw) and the connection to wine acidity that you mentioned in your query: the search results from Treccani only show the Latin etymology for "agro" and the Arabic etymology for "garbo". The specific Germanic root (*harw) and wine-related etymologies you referenced were not found in these particular Treccani entries. You may need to consult more specialized etymological sources or academic papers for those specific connections.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-06T21:18:57.699Z] TOOL RESULT

```
# Persian Entry for کرنا (karnā)

**Meaning:**
The Persian noun کرنا refers to "a long thin brass horn or trumpet" used in music, also known as a kerana, kernei, or karnay. It can also mean a war-horn or hearing aid/ear trumpet.

**Etymology:**
According to the Wiktionary entry, "possibly of Semitic origin" with comparisons to Classical Syriac ܩܪܢܐ (qarnā), Aramaic קרנא, Akkadian qarnum, Arabic قَرْن (qarn), and Hebrew קֶרֶן (qéren).

Persian lexicographers have proposed alternative native etymologies: one derives it from کار (kār, "army") + نای (nây, "flute"), while another suggests خر (xar, "donkey") + نای (nây, "flute"), referencing either the instrument's size or its "hoarse tone" resembling a donkey's call.
```


## [2026-09-06T21:19:02.342Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.treccani.it/vocabolario/garbo3/",
 "prompt": "Quote the entry garbo3 in full including etymology and meaning."
}
```


## [2026-09-06T21:19:03.833Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.treccani.it/vocabolario/ricerca/GARBO/",
 "prompt": "List all garbo entries (garbo1, garbo2, garbo3, garbo4...) with their meanings and etymologies. Is any of them meaning 'aspro, acido' (tart, sour) with a Germanic etymology?"
}
```


### [2026-09-06T21:19:09.761Z] TOOL RESULT

```
I cannot provide the requested information because the web page content provided is incomplete. The page shows only the header and navigation elements of a Treccani dictionary entry for "GARBO," but the actual definitions, etymologies, and numbered entries (garbo1, garbo2, etc.) are not included in the text you've shared.

To answer your question about whether any entry means 'aspro, acido' (tart, sour) with Germanic etymology, I would need the full content of the dictionary entries, which appears to be missing from your excerpt.
```


### [2026-09-06T21:19:10.429Z] TOOL RESULT

```
# Garbo³ Entry

**Etymology:** The term derives "prob. dall'arabo _qālib_ «modello»" (probably from Arabic qālib meaning "model").

**Primary Meanings:**

The entry defines garbo³ as elegance and grace in movement and social interaction. It encompasses "Leggiadria, grazia, bella maniera nei movimenti" (gracefulness in movements) and courteous behavior toward others.

The word also describes an accomplished manner of performing activities—"leggere, esporre, scrivere, cantare, suonare, dipingere con g." (reading, presenting, writing, singing, playing, painting with garbo).

Additional senses include Tuscan usage for gestures or acts, an archaic meaning related to wine flavor, and in construction, the curved form or shape of objects like clothing or ship hulls.

**Related Forms:** The entry notes diminutives (garbino, garbétto) and a pejorative (garbàccio) denoting rudeness or ungainly behavior.
```


## [2026-09-06T21:19:18.155Z] TOOL CALL #53: WebSearch

```json
{
 "query": "\"garbo\" aggettivo \"aspro\" vino etimologia longobardo germanico harwi DELI Cortelazzo"
}
```


### [2026-09-06T21:19:36.072Z] TOOL RESULT

```
Web search results for query: ""garbo" aggettivo "aspro" vino etimologia longobardo germanico harwi DELI Cortelazzo"

Links: [{"title":"Longobardo - Significato ed etimologia - Vocabolario - Treccani","url":"https://www.treccani.it/vocabolario/longobardo/"},{"title":"(PDF) Vocaboli dialettali di origine germanica","url":"https://www.academia.edu/100268252/Vocaboli_dialettali_di_origine_germanica"},{"title":"Lombardo e Longobardo","url":"https://www.summagallicana.it/lessico/l/Lombardo%20e%20Longobardo.htm"},{"title":"longobardo - Wikizionario","url":"https://it.wiktionary.org/wiki/longobardo"},{"title":"1 “La lingua dei Longobardi, caratteristiche e problemi”","url":"https://www.valcenostoria.it/wp-content/uploads/2021/10/La_lingua_dei_Longobardi.pdf"},{"title":"Glossarietto longobardo","url":"https://www.bighipert.com/p/glossarietto-longobardo.html"}]

I found information about Germanic etymology and Longobard linguistic heritage, but I need to perform a more specific search to find information about the particular terms you're asking about (garbo, aspro, harwi, and their connection to wine etymology and Cortelazzo's DELI dictionary).

Links: [{"title":"Garbo (singer)","url":"https://en.wikipedia.org/wiki/Garbo_(singer)"},{"title":"Vino cotto","url":"https://en.wikipedia.org/wiki/Vino_cotto"},{"title":"Vino Nobile di Montepulciano","url":"https://en.wikipedia.org/wiki/Vino_Nobile_di_Montepulciano"},{"title":"wanderlog.com","url":"https://wanderlog.com/place/details/7563589"},{"title":"garbo enologia criativa","url":"https://wanderlog.com/place/details/7563589/garbo-enologia-criativa"},{"title":"Vino 1966 Barbera D'Asti Riserva Degli Etruschi Duca D'Asti 72cl 13% (101)","url":"https://www.ebay.de/itm/266984972235"}]

Links: [{"title":"Vino Greco","url":"https://en.wikipedia.org/wiki/Vino_Greco"},{"title":"Glossario delle frasi fatte - A Flashcards | Quizlet","url":"https://quizlet.com/298644196/glossario-delle-frasi-fatte-a-flash-cards/"},{"title":"Manlio Cortelazzo Paolo Zolli DELI DIZIONARIO ETIMOLOGICO DELLA LINGUA ITALIANO | eBay","url":"https://www.ebay.it/itm/361404785489"},{"title":"Vino cotto","url":"https://en.wikipedia.org/wiki/Vino_cotto"},{"title":"DELI - Dizionario etimologico della lingua italiana di Manlio Cortelazzo e Paolo Zolli. Edizione minore","url":"https://www.research.unipd.it/handle/11577/1340758"},{"title":"Garbo Vino Rosato Vendita Online | Gustotosto Sito Ufficiale","url":"https://www.gustotosto.it/prodotto/garbo/"},{"title":"Il nuovo etimologico : DELI : Dizionario etimologico della lingua italiana in SearchWorks catalog","url":"https://searchworks.stanford.edu/view/4296132"},{"title":"Gambero Rosso","url":"https://en.wikipedia.org/wiki/Gambero_Rosso"},{"title":"Manlio Cortelazzo, Paolo Zolli, Dizionario Etimologico della Lingua Italiana (DELI), N. Zanichelli Ed., Bologna: 1. A-C, 1979 ; 2. D-H, 1980","url":"https://books.google.com/books/about/Manlio_Cortelazzo_Paolo_Zolli_Dizionario.html?id=_2xfMwEACAAJ"},{"title":"Kurtinig an der Weinstra%C3%9Fe","url":"https://en.wikipedia.org/wiki/Kurtinig_an_der_Weinstra%C3%9Fe"}]

The second search didn't return specific results about the etymological connection. Let me try a more targeted search focusing on the linguistic relationship between these terms.

Links: [{"title":"Vino Greco","url":"https://en.wikipedia.org/wiki/Vino_Greco"},{"title":"Vino - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/vino"},{"title":"vino - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/vino"},{"title":"вино - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D0%B2%D0%B8%D0%BD%D0%BE"},{"title":"What is the origin of the word “vino”? - Jean Leon","url":"https://jeanleon.com/en/cual-es-el-origen-de-la-palabra-vino/"},{"title":"Wine - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/wine"},{"title":"Vino Nobile di Montepulciano","url":"https://en.wikipedia.org/wiki/Vino_Nobile_di_Montepulciano"},{"title":"Aleatico","url":"https://en.wikipedia.org/wiki/Aleatico"}]

Links: [{"title":"garb - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/garb"},{"title":"garbo - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/garbo"},{"title":"Garbo, n.¹ meanings, etymology and more | Oxford English Dictionary","url":"https://www.oed.com/dictionary/garbo_n1"},{"title":"garbo","url":"https://bibliamedieval.es/bibliateca.es/corominas/DATA/HTML/garbo.html"},{"title":"UniMorph 4.0: Universal Morphology","url":"https://arxiv.org/pdf/2205.03608"},{"title":"Garibald (name)","url":"https://en.wikipedia.org/wiki/Garibald_(name)"},{"title":"germanico - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/germanico"},{"title":"Deep encoding of etymological information in TEI","url":"https://arxiv.org/pdf/1611.10122"}]

Excellent! I found relevant information. Based on the search results, I can now provide you with information about the etymology of "garbo" and its Germanic connections.

## Results

Based on the web search, I found information about the etymology of **garbo**:

The Italian word "garbo" is borrowed from Old High German garwi ("dress; equipment; preparation"), from Proto-Germanic *garwijaną ("to prepare"). 

In English, "garb" comes from Middle French garbe (graceful outline, silhouette), from Italian garbo (grace, elegance), from Germanic sources (compare Old High German garwi, garawi meaning "dress, equipment, preparation"), ultimately from Frankish *garwijan ("to prepare"), from Proto-Germanic *garwijaną ("to prepare").

Additionally, I found that in Tuscan, "garba" is attested with the Old High German antico "garawi", Old Saxon "garwian", and Old English "gearwe", with the English "garb" having the meaning of characteristic and distinctive clothing.

Regarding the DELI dictionary you mentioned (Cortelazzo-Zolli), while I confirmed it exists as a major etymological dictionary of Italian, the search results did not return specific entries about the relationship between "garbo," "aspro," wine terminology, and the Longobard etymon "harwi" that you're asking about. To access detailed information about these specific etymological connections in the DELI, you would need to consult the dictionary directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T21:19:47.939Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/herb#German",
 "prompt": "Quote the German entry for herb (adjective, 'tart, bitter'): its etymology, Middle High German forms (hare, herwe), and whether any connection to Proto-Indo-European *koru- or to Italian garbo is mentioned."
}
```


## [2026-09-06T21:19:49.237Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://de.wiktionary.org/wiki/herb",
 "prompt": "Quote the Herkunft (etymology) section for German herb: mittelhochdeutsch forms, Proto-Germanic reconstruction, and any mention of Italian garbo or an Indo-European root."
}
```


### [2026-09-06T21:19:53.190Z] TOOL RESULT

```
# German "herb" Entry Analysis

**Etymology:** From Middle High German *hare*, *here* (inflected *harwe*, *herwe*), from Old High German *\*haro*, from Proto-West Germanic *\*haru*.

**No connections mentioned:** The entry does not reference Proto-Indo-European *koru- or Italian garbo. The etymology traces only to Proto-West Germanic origins, stopping short of deeper Indo-European reconstructions or Romance language comparisons.

**Adjective meaning:** The German adjective means "slightly bitter or sharp to the taste" in food/drink contexts, or figuratively "harsh; hard" regarding events or deeds.
```


### [2026-09-06T21:19:54.910Z] TOOL RESULT

```
# Response

I cannot provide the requested etymology section for German "herb" because it is not included in the web page content provided. 

The Wiktionary page shown contains:
- German definition (an adjective meaning bitter/harsh in taste or appearance)
- English definition (a noun meaning herb/culinary plant)
- Translations across multiple languages
- Usage examples and related terms

However, there is **no Herkunft (etymology) section** visible in this document. The page content jumps from the main definitions directly to usage examples and synonyms, without including historical linguistic information about Middle High German forms, Proto-Germanic roots, or Romance language connections.

To obtain the etymology you're seeking, you would need to access a more complete version of the Wiktionary entry or consult a comprehensive etymological dictionary.
```


## [2026-09-06T21:20:07.489Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN army/war ===\"; grep -n \"20\\.4[0-9] \" SYN.txt | head -20\necho \"=== SYN ARMY ===\"; grep -n \"ARMY\" SYN.txt | head -10\necho \"=== WLD band3 harjis/kāra ===\"; grep -n \"harjis\\|kāra\\|koros\" WLD_band3.txt | head -10\necho \"=== HUB kārzār ===\"; grep -n -i \"kārzār\\|karzar\\|kārezār\\|karwan\" HUB.txt | head -10\necho \"=== LKT Karawane ===\"; grep -n -i \"karawane\\|karwan\" LKT.txt | head -10\necho \"=== HJB CARAVAN ===\"; grep -n \"^CARAVAN\" HJB.txt | head\necho \"=== PLA karb ===\"; grep -n \"karb\\b\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head\necho \"=== FVQ karb ===\"; grep -n -i \"karb\" FVQ.txt | head"
}
```


### [2026-09-06T21:20:07.617Z] TOOL RESULT

```
=== SYN army/war ===
34330:| CHAPTER 20 i WARFARE 20.11 Freur (vb.) 20.28 Gun; CANNoNn 20.12 BatrxE (sb.) 20.29 GuNPOWDER 20.13 War 20.31 Anmor (Defensive) : 20.132 Enemy 20.32 BreasTPLaTr, Corsier hea ies 20.338 HetMer ne aes 20.34 Snreip 20, Renton 20.35 Fortress 20.18 GENERAL 2030 = LOWnE 20.19 Ap 20.41 Victory 20.21 Wearons, ARMS 20.42 Derzat (sb.) 20.22 Crus 20.43 Arrack (sb.) 20.222 BATTLE-Ax 20.44 DEFENSE 20.23 Sune 20.45 RETREAT (sb.) 20.24 Bow 20.46 SuRRENDER (vb.) 20.25 Arrow 20.47 Captivr, PRISONER : 20.26 SpPEar 20.48 Boory, Srors : 20.27 Sworp 20.49 AxpusH (sb.) 20.11 FIGHT (vb.) ee péxopal, qroenewo one meu Lith. kovott, kautis, muStis TONELO erjask, vega Lett. kauti Lat.  pugndare, proeliari Dan. tee bare ChSl. mtrdli 46, bratt It. combattere, pugnare Sw. kampa, fikta, sldss SCr. _boriti se (biti se) : Be. Fee en OE feohtan, wigan, win- eer oS Sia se) - , nan ol.  walezyd, bid sie : sa Pa ME Ee kempe Russ. eee Nee bit'sja, . chim, cai rie rat'sja | a ON al troidim ne Ae vechten Skt.  yudh- : ym ehtan Av. parat-, yud- Br. en em ganna MHG vehten, wigen
35152:20.41 VICTORY
35182:20.42 DEFEAT (sb.)
35184:ally equivalent to ‘be victorious over, conquer’, and is generally expressed by the verbs mentioned in 20.41 (e.g. Grk. vikaw, Lat. vincere, in pass. regularly ‘be defeated’), the nouns corresponding to which mean ‘victory’. Such verbal ex- pressions of defeat are more common than the use of a noun for ‘defeat’ vs. ‘victory’, and in some cases such a dis- tinctive noun seems to be lacking or at least has not been found quotable. Most of the nouns for ‘defeat’ are based on such notions as ‘inferiority, de- struction, disaster, loss, breaking, blow’. 1. Grk. jooa, Att. jr7a (also NG lit.), back-formation to jccéopuat ‘be inferior, be defeated’, fr. joowy ‘inferior, weaker’, comp. to ady. jxa ‘slightly, gently’,
35218:20.48 ATTACK (sb.)
35258:20.44 DEFENSE
35288:20.45 RETREAT (sb.)
35314:20.46 SURRENDER (vb.)
35335:1414 SELECTED INDO-EUROPEAN SYNONYMS 20.47 CAPTIVE, PRISONER
35365:20.48 BOOTY, SPOILS Grk. ela, Addvpa, cxDAa Goth. meee Lith. grobis NG Adgupa, TALaTOLKA ON herfang Lett. laupijums Lat. __praeda, spolia Dan. _ bytte, rov ChSl.  koristt, plénit It. preda, bottino, spoglie Sw. byte, rov SCr. plijen Fr. bulin OE reaf, fang, (here-)hiup Boh. korist (plen) Sp. botin ME botye, spoyle(s), preye Pol. tup (zdobycz) Rum. pradé NE booty, spoil(s) Russ. dobyéa Ir. brat Du. buit Skt. loptra- NIr.  creach OHG roub, herehunda W. ysglyfaeth, ysbail MHG roup, biute Br. preiz NHG beute
35405:20.49 AMBUSH (sb.)
=== SYN ARMY ===
34478:WARFARE 1377 20.15 ARMY Grk. orparés, orparevpa Goth. harjis Lith. kariuomene (karias, NG otparés (Byz. ON herr armija) goooGrov) Dan. her, armé Lett. kar’§ (kar’a spéks) Lat.  exercitus Sw. har, armé ChSl.  vojt It. esercito, armata OE here, fierd SCr.  vojska, armija Tr. armée ME (h)oste, here, ferd Boh.  vojsko, armdda Sp. ejército NE army Pol. wojsko, armia Rum. armatd, ostire (oaste) Du. __ heer, leger Russ. armija (vojsko) Ir. sliag OHG heri Skt.  sena- Nir. arm, sluagh MHG her(e) y Av. haéna-, spada- W. byddin (lu) NHG heer, armee OPers. kdra-, haina-
=== WLD band3 harjis/kāra ===
=== HUB kārzār ===
=== LKT Karawane ===
1821:Vulgäre  Aussprache  des  klass.-ar.  kaum 'Truppe,  Schar',  im  Magrib  [s.  hier Nr.  674]  gebräuchlich;  hieraus  frz.  goum 'Raubkarawane',  nach  Devic  DEt  131 auch  jContingent  militaire  des  tribus alg^riennes".
2377:996.  Ar.  käflla: 'Reisegesellschaft,   Karawane',  hieraus sp.  pg.  cufila  'dass.,  Haufen,  Menge'; angloind.  capla  'Geleitzug  zur  See'.  [DE 244.    Hobson-Jobson  142.
2436:'Schloß,  Burg' ;  hieraus  mit  ar.  Art.  Äl- calä,  N.  pr.,  Name  vieler  sp.  Städte.  Eben- so, Kala,  Qualah,  hieß  im  Mittelalter  der Hauptstapelplatz  für  Zinn  auf  Malakka, wo  sich  etwa  im  9.  Jahrhundert  die  Han- delskarawanen aus  Ost-  und  Westasien trafen  [QUATREMERE  im  Journal  des Savants  1846,  S.  751  ;  W.  v.  Heyd,  Ge- schichte des  Levantehandels  im  MA  I, 37] ;  hieraus  mal.  kelang  'Zinn',  pg.  calah7i 'sehr  feines  ind.  Zinn'  [Constancio  Dicc 205b;  DE  245].  Über  tk.  kalaj  [ngr. Ka\di]  wurde  serb.  kalaj  'Zinn',  bulg. ebenso;  ferner  rum.  calangiü  'Verzinner'.
2551:'KameP  [eigentlich  'Schnelligkeit  ha- bend'], hieraus  wahrscheinlich  pers. kärwän  oder  käricän  'Kamelzug,  Reise- gesellschaft', in  alle  europäischen  Spra- chen übergegangen:  rum.  caravanä, chervanä,  it.  caravana,  carovana,  pg. sp.  caravana,  frz.  caravane;  engl,  cctra- van,  ndl.  karavaan;  dtsch.  Karawane, schwed.  fcßj'afrtn;  vxxss.  karawan,  bulg. kerwan,  serb.  karawan,  öech.  karavana, poln.  karaivana.  Mit  pers.  säräi  'Palast' [Horn  NpEt  S.  161,  Nr.  727]  ergibt  sich die  Bezeichnung  für  die  Herbergen  der Karawanen :  känvänsäräl.  Hieraus  rum. cherväsärie  'Lagerhaus,  Stapelplatz',  it. caravanserraglio,  frz.  caravanserail,  pg. caraicansarä ;  dtsch.  A'^rrtwanserai;  russ. karatvanseraj  [vgl.  Karl  Müller,  Die Karawanserai  im  Vorderen  Orient.  Ber- hn  1920].  [Klutre  227/228.  FR.  MÜL- LER in  WZKM  V,  354.
5789:1068 A'ar«i*('  1004 Karaffe  689 Karakal  1081 ifa>-rt<  1182 Karawane  1075 Karatvanserai  1075 Karbatsche  1279
=== HJB CARAVAN ===
5222:CARAVAN.
5238:CARAVANSERAY,
=== PLA karb ===
6683:[08173 L,> - barbädbän = karbädgan q. v. 
6684:OlssL_>- Zarbädgan - karbädhän q. v. 
6687:sbylo- karbädgäni: Nisba v. karbadgän. 
6739:karb 83 Sardaq 
16491:GelsT karabis: Pl. vor karbäs q.v 
=== FVQ karb ===
```


## [2026-09-06T21:20:17.880Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT around 2551 ===\"; sed -n '2545,2556p' LKT.txt\npython3 - <<'EOF'\nlines=open('LKT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=1\nfor i,l in enumerate(lines,1):\n    if i in (2551,): print(i,'leaf',leaf,'printed p',leaf-27)\n    leaf+=l.count('\\f')\nEOF\necho \"=== HJB caravan ===\"; sed -n '5222,5240p' HJB.txt | cut -c1-1500"
}
```


### [2026-09-06T21:20:19.829Z] TOOL RESULT

```
=== LKT around 2551 ===
'Einzelner  Hiigel,  Anhöhe',  plur.  kär; hieraus  mit  ar.  Art.  sp.  kat.  alcor  'Hügel'. [DE  92.    Eguilaz  140.    ML  6901.
1073.  Mal.  kära:
Auch  kärah,  käret  'Schale  der  Schild- kröte, Schildpatt'  [Pijn  171];  hieraus sp.  carey,  frz.  caret,  ndl.  karet,  dtsch. Karettschildkröte ,  Chelone  imbricata Schweigg.,  deren  Schalen  zur  Herstel- lung von  Schildpatt  dienen.  [MMM 11/12.
1074.  Pers.  käräbä:
'Große  lederne'  Milchflasche'  [offenbar mit  ar.  kirba  'Schlauch'  verwandt] ;  hier- aus engl,  carboy  'große  Glasflasche  zum Verschicken  von  Säuren  und  Explosiv- stoffen' [Hobson-Jobson  162/163].  — , Wenig  appetithch  ist  der  Anblick  der sauren  Milch,  die  in  einem  Zeugbeutel mitgeschleppt  wird,  der  an  dem  Hinter- schenkel des  Pferdes  herabhängt.  Die durchträufelnde  Flüssigkeit  gibt  dem Pferde  einen  sehr  widerlichen  Anbhck, der  vor  dem  Genüsse  der  so  transpor- tierten Milch  abschreckt.  Hat  die  Milch in  dieser  Weise  ein  gut  Stück  Weges hinter  sich,  so  ist  in  dem  Beutel  eine weiße  käseartige  Masse  zurückgeblieben, die  von  den  Persern  unter  dem  Namen Mas  zum  Brote  gegessen  wird."  Brugsch, Reise  der  k.  preußischen  Gesandtschaft nach  Persien  1860  u.  1861.  Leipzig 1862.  I,  156.
1075.  Sskr.  karabha:
'KameP  [eigentlich  'Schnelligkeit  ha- bend'], hieraus  wahrscheinlich  pers. kärwän  oder  käricän  'Kamelzug,  Reise- gesellschaft', in  alle  europäischen  Spra- chen übergegangen:  rum.  caravanä, chervanä,  it.  caravana,  carovana,  pg. sp.  caravana,  frz.  caravane;  engl,  cctra- van,  ndl.  karavaan;  dtsch.  Karawane, schwed.  fcßj'afrtn;  vxxss.  karawan,  bulg. kerwan,  serb.  karawan,  öech.  karavana, poln.  karaivana.  Mit  pers.  säräi  'Palast' [Horn  NpEt  S.  161,  Nr.  727]  ergibt  sich die  Bezeichnung  für  die  Herbergen  der Karawanen :  känvänsäräl.  Hieraus  rum. cherväsärie  'Lagerhaus,  Stapelplatz',  it. caravanserraglio,  frz.  caravanserail,  pg. caraicansarä ;  dtsch.  A'^rrtwanserai;  russ. karatvanseraj  [vgl.  Karl  Müller,  Die Karawanserai  im  Vorderen  Orient.  Ber- hn  1920].  [Klutre  227/228.  FR.  MÜL- LER in  WZKM  V,  354.
87
[Tk.  karadas,
1076.  Tk.  karadas:
'Schiefer  [aus  tk.  kara  'schwarz',  s.  hier Nr.  1070,  und  das,  fas  'Stein'] ;  hieraus russ.  karandas,  bulg.  karandas  'Bleislift'.
1077.  Tk.  karagan: 'Steppenfuchs';  hieraus  russ.  karagan 'dass.'.
2551 leaf 115 printed p 88
=== HJB caravan ===
CARAVAN.
of  account,  if  not  actual.  To  discuss the  carat  fully  would  be  a  task  of extreme  complexity,  and  would  occupy several  pages.
Under  the  name  of  siHqtia  it  was the  24th  part  of  the  golden  solidus  of Constantine,  which  was  again =|  of an  ounce.  Hence  this  carat  was= rir  of  an  ounce.  In  the  passage  from St.  Isidore  quoted  below,  the  cerates is  distinct  from  the  sUiqua^  and  = 1^  nliquae.  This  we  cannot  explain, but  the  nXiqua  Graeca  was  the  irepdrcor ; and  the  gihmia  as  ^^  of  a  solidus  is the  parent  of  the  carat  in  all  its  uses. [See  Prof.  Gardner,  in  Smith,  Diet. Ant  3rd  ed.  ii.  675.]  Thus  we  find the  carat  at  Constantinople  in  the  14th century = A  of  the  hyverpera  or  Greek bezant,  which  was  a  deoased  representa- tive of  the  solidus  ;  and  at  Alexandria A  of  the  Arabic  <{tnc7r,  which  was  a purer  representative  of  the  solidus. And  so,  as  the  Roman  uncia  signified iV  of  any  unit  (compare  (mncey  inch), so  to  a  certain  extent  carat  came  to signify  A.  Dictionaries  give  Arab. kirrdt  as  "A  of  an  ounce/'  Of  this we  do  not  know  the  evidence.  The Engltth  Cyclopaedia  (s-v.)  a^n  states that  "the  carat  was  oriffinally  the 24th  part  of  the  marc,  or  half-pound, amoncthe  French,  from  whom  the  word came."  This  sentence  perhaps  contains more  than  one  error ;  but  still  both of  these  allegations  exhibit  the  carat as  Ath  part.  Amon^  our  goldsmiths the  term  is  still  usea  to  measure  the proportionate  quality  of  gold  ;  pure gola  
The  carat  is  also  used  as  a  weight for  diamonds.  As  tH  of  an  ounce  troy this  ought  to  make  it  3i  grains.  But these  carats  really  run  151^  to  the ounce  troy,  so  that  the  diamond  carat is  3^  m.  nearly.  This  we  presume was  aoopted  direct  from  some  foreign system  in  which  the  carat  vxts  i\j  of  the local  ounce.  [See  Ball,  Tavemier,  ii. 447.]
c.  A.D.  036. — '^Siliqiia  vigesima  quarta pars  solidi  ost,  ab  arbcnris  semine  vocabulum tenena.  Gmrates  oboli  pars  media  est  siliquS habexis  tinam  semis,    nanc  latinitas  semi-
obultt  yocat ;  Cerates  autem  Graece,  Latino siliqua  oomufl  interpretatur.  Obulns  siliquis tribua  appenditur,  babens  cerates  duos,  caloos qa&tVLor.—Isidori  Ifispalensit  Opera  (ed. Paris,  1601),  p.  224.
1298.— "The  Great  Kaan  sends  his  com- missioners to  the  Province  to  select  four  or five  hundred  ...  of  the  most  beautiful young  women,  according  to  the  scale  of beauty  enjoined  upon  them.  Hie  commis- sioners .  .  .  assemble  all  the  g^irls  of  the province,  in  presence  of  appraisers  appointed for  the  purpose.    These  carefully  survey  the
Soints  of  each  girl.  .  .  .  They  will  then  set own  some  as  estimated  at  16  carats,  some at  17,  18,  20,  or  more  or  less,  according  to the  sum  of  the  beauties  or  defects  of  each. And  whatever  standard  the  Great  Kaan  may have  fixed  for  those  that  are  to  be  brought to  him,  whether  it  be  20  carats  or  21,  the commissioners  select  the  required  number from  those  who  have  attained  to  that  stan- dard."—iforco  Poloy  2nd  ed.  i.  850-361.
1673. — "A  stone  of  one  Cazrack  is  worth lOL"— Fryer,  214.
0  ABA  VAN,  s.  P.  karwdn;  a convoy  of  travellers.  The  Ar.  iMla is  more  generally  used  in  India.  The word  is  found  in  French  as  early  as the  13th  century  {lAttr^.  A  quota- tion below  shows  that  the  English transfer  of  the  word  to  a  wheeled conveyance  for  travellers  (now  for goods  also)  dates  from  the  17th  century. The  abbreviation  van  in  this  sense seems  to  have  acquired  rights  as  an English  word,  though  the  altogether analogous  bus  is  still  looked  on  as slang.
c.  1270. —  "  Meanwhile  the  convoy  (la earavana)  from  Tortosa  .  .  .  armed  seven vessels  in  such  wise  that  any  one  of  them could  take  a  galley  if  it  ran  idongside." — Chronicle  of  James  of  Aragon,  tr.  by  Foster, i.  879.
1380. — *'De  hac  civitate  reoedens  cum earavanis  et  cum  quadam  societate,  ivi versus  Indiam  Superiorem."—  Friar  Odorie, in  Cathay^  &c.,  ii.  App.  iii.
1384. — "Rimonda  che  I'avemo.  vedemo venire  una  ^randisdma  oarovana  di  cammelli e  di  Saracini,  che  recavano  spesierie  delle parti  d'  India.,"— Fresoobafdiy  64.
0.  1420. — *'Is  adolescens  ab  Damasco  Sy- riae,  ubi  mercaturae  ^ratiH  erat,  perceptH prius  Arabum  linguA,  in  coetu  mercatorum — hi  sexcenti  erant — quam  vulgo  caroaaam dicunt.  .  .  .'* — N,  Conti,  in  Poggius  de  VariC' tote  Fortunae.
1627. — **  A  Caravan  is  a  convoy  of  souldiers for  the  safety  of  merchants  that  trauell  in  the East  Countreys. "— if ijw/ieir,  2nd  ed.  8.v.
1674.— "Caravan  or  E[aravan  (Fr.  cam- vcme)  a  Convoy  of  Souldiers  for  the  safety of  Merchants  that  travel  by  Land.  Also  of late  corruptly  used  with  us  for  a  kind  of
CARAVANSERAY,
162
CARBOY.
```


## [2026-09-06T21:20:30.343Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index kar ===\"; grep -n -i \"KARVAN\\|KAREVAN\\|KARZAR\\|KAR \" incoming/ARY/ARY_latin_index_pages.txt | head -20\necho \"=== ARY pages کاروان ===\"; grep -n \"کاروان\\|کارزار\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== NYB kār ===\"; grep -n \"kārawān\\|kārečār\\|^kār\\b\\|kār \" NYB_vol2_glossary.txt | head -10\necho \"=== CHEUNG kar army ===\"; grep -n \"kāra-\\|kārezār\" CHEUNG.txt | head -5\necho \"=== FSD caravan ===\"; grep -n \"^caravan\" FSD_vol1.txt | head -3\necho \"=== WEB caravan ===\"; grep -n \"^caravan\" WEB_vol1.txt | head -3"
}
```


### [2026-09-06T21:20:30.461Z] TOOL RESULT

```
=== ARY latin index kar ===
6131:JECUR, JECORIS (LATIN) 5s JAGAR, JIKAR 3} eantLavy 34
6946:SUEKAR (SERBIAN) pe °~-« SOCRU, SOCRA {RUMANIAN) gs
11510:KRUG DUTCH) ade KAR (PAHLAVI) (5 shay
11511:(LITHUANIAN) 3\ 5 KAR KURDISH) 53,5
11512:KARAS, KARIAS, KARE KAR HAFGHAND (4) gist
12957:| (VARY 2 GU Ble p) slag ay ae VFKAR cy Soils softy bly esl Sifts gl dlatiya “1
13154:LACHE FRENCH) sil 3 SLAKKAR —.(TOKHARIAN A) A 5)
=== ARY pages کاروان ===
11759:۶ | کار (به چم *ارتش * و "جنگ" کارزار
11785:۲- در فارسی واژه‌ی " کارزار" بعنی "محل نبرد؟: "کار" * نبرد و پا جنگ و آزار"< محل (مانند "گلزار").
=== NYB kār ===
859:ayyāt-kār [---k'1] *remembrance-work"' = memorabilia, memoirs 184; memoran- dum 108%, 113% — Paz. ayädagär; NP yüdgàr; cf Ps. *by*tk*lyhy ‘recollection’, MPrs ’y’dg’ryh ‘mention’ (S).
2191:kām-kār [k?mk?l] acting according to his own will, sovereign, autocrat: pat Hran- šahr ~ 1376; comp. ~-tar Supreme So- vereign 3°, adj. 418-19, — MPrth k’mg’r ‘free, happy’ (A-H III). V. kar.
2220:kārēcār [k'lyc'l] battle, combat 1198, with: ~ % 8?9, 4 apäk 108%; pat ~ bē dzatan to kill in battle 9722; ~ xtinrécisnéh (q.v.) 1312-13, kéasisn u kārēcār 901; ~ kartan to fight 25-29, passim. 511. 95!1; vas ~ u ozanišn apāk ... kart 138-4; ~ dästan to keep contending, wrestling 329-19; be 0 m~ ìi... šutan to engage in battle with 9617-18 ete. — MPrs kryer, krer (S); Paz. kārīžār, NP kürzür; käre- cas. obl. of kar < OP kära- ‘army’, + cär from Av. (449) 5kar- ‘to move’, cf NP caridan ‘to graze’ and vicar-.
2465:martóm [mltwm; "NSWT?] 1. in an in- dividual sense: a human being: ~ hom 62°. 631; pl. cas. rect. ~: šmāh kē ~ het 67°; har ~ aed mat to everyone came a message 208-9, — 2. ~ in a collective sense: man, mankind, men, people; when subj., mostly construed as a pl. (thus serving as the pl. cas. rect. of 1): ka hamäk ~ avinüs bē bavénd 3412-13, 672, 961-2, 9717-18 (constr. ad sensum): 19. 104°. 10618-19, 12021, but ka Krisäsp kār (ag.) martöm (subj.) özat but 351, and thus 327. 9516. — 3. with the pl. cas. obl. ~-dn [mltwm’n', "NSW'T^-n']: a) gen.: andar tant ~ -än 65°; ~ -dn nē dänistan ... rād as men do not know 8016 etc.; — b) dir. obj.: ~-an pat kunisn girend 652, ete.; — c) dat.: dišop ... but 10718 sq.; as the logical subj. of an impers. pred.: ~-dn pat én 3 rah saxt estisn men must keep steadily to these 3 ways 65977; ~-dn ... dänistan nē tuvàn 8045; ~-n ... Süyet x"astan 891-2; — d) agent: —-čin guft ku 15-16, ete.; — e) after a prep.: hac ~-Gn 7?!; passim; — f) secondarily as the cas. rect. pl.: 58. 69-19 etc. passim; — as the app. of a pl.: amah c--ün 11%; astömandän ~-dn, viturtan
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
3135:pēšak-kār [py3k°l] craftsman, pl. cas. obl. n-ān 8117-19, — Paz. pēšagar, Skr. v. vid yavant.
3856:uskār [^wsk?l] consideration, deliberation : 6 ~ kartan to take into consideration, with inf. 10913; speculation 109%,
4726:JN = Jamasp-namak: 1) Jámáspi, Pahlavi, Pázend and Persian texts with Gujarati Transliteration of the Pahlavi Jámáspi, English and Gujarati Translations with Notes of the Pahlavi Jámáspi, Gujarati Translation of the Persian Jámáspi, and English Translation of the Pazend Jámáspi, by Jivanji Jamshedji Modi. Bombay 1903 (Pahlavi Translations, Part III). 2) Giuseppe Messina, Libro apocalittico Persiano Ayātkār i Zämäspik, Biblica et Orientalia N. 9. Roma 1939.
6772:agar: pēšakkār pēšavāē: pēšēpāi pēšiār: pēšārvār pēšīnaga: pēšēnīk phālum: pahlom pīm: pēm pradim: fratom puh(a)l: puhl pulādīn: pēlāvatēn pur: purr pursīdan: pursītan puštaspān: puštēpān
=== CHEUNG kar army ===
=== FSD caravan ===
=== WEB caravan ===
```


## [2026-09-06T21:20:41.275Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor i,l in enumerate(lines,1):\n    if 11745<=i<=11795: print(i,l)\nEOF"
}
```


### [2026-09-06T21:20:43.595Z] TOOL RESULT

```
11745 
11746 انگلیسی کین 9ل5لاه(یم :۰ ۲۵۲۸ پسگشت‌ها_ 837882۷023
11747 
11748 انگلیی ربروررم/(ه), ۹۰ * دی 395 اما
11749 
11750 نروژی (۸/038501۸): 0 8 (00۷8) :8/7
11751 
11752 اسلاوی کهن (ع1//(ها5 تال (ا0): 2 (0۷8) 0/0
11753 ه023 0 (0۷۴ح) :57
11754 
11755 لهستانی (157ا0): 612 بش12 ,01211۸ فرهنگ معین : ۴۵۱
11756 
11757 چکه (4ع28)): 12 لغت‌نامه دهخدا: ۱۳۸۵۷
11758 [pdf page 395]
11759 ۶ | کار (به چم *ارتش * و "جنگ" کارزار
11760 بادداشت:
11761 ۱ بازگشت به‌زگوهگوی ی
11762 ۲- چم این واژه در زبان‌های غیراز فارسی: اتانکد» خوکك دونی» غار» کلبه» تفای ی و
11763 چم اين واژه در زبان‌های انگلیسی نوین: خلیج کوچکه ی
11764 ۳ واژه‌های " کوژ" و "قوز" نیز از همین ریشه‌اند.
11765 اوستایی (415574/۷): 1۵7۸۷۸11 بفالق سوئدی (ل550[15): 16
11766 پارسی باستان (۳8781۸ 010): هم نروژی (077801۸0/): 6
11767 پهلری (1ها(م«): 3 هلندی (7لع007): از ۱۹۸
11768 کردی (۸(8(137)+ ۸ لبترانی (4142لهلالل7).
11769 افغانی (پشتو) (/4۳0/۸۷): 3اه ,5۸3۸8 ,کفش
11770 سانسکریت (7ل8۸(/587): ۸ نونی (لتی) (ق7۲ها): اند ۱
11771 یونانی 07/6870): 05 پروسی کهن ۳8-۹۹۸0 010): 1۸3018
11772 گرتیک (0077/0): 11۸87۸ ,73۸815 ایرلندی کهن (4لولع[ صرا0): 3
11773 ایسلندی کهن (7+۸۷۵(۷طنته صام).
11774 قددان پسگشت‌ها 1/5
11775 ساکسوی کهن ((54:0 طا0): دنا 6 ۶00800
11776 فریزی کهن (الفاول۶۶ ضام). دا دنا #4 هام0
11777 آلمانی کهن (/687/40 بزه ]با صزم): و ۱ شا
11778 41 ,فا 311 0۴۵ ۸0
11779 آلمانی (0284490): ان برهان قاطع + ۱۵۸
11780 انگلیسی کهن 8۱/0/0 0۱2: 11888 فرهنگ معین : ۳۸۹
11781 دانمارکی (0۸(/18[7): 6
11782 یادداشت: ۹
11783 ۱- امروزه پیشتر دانشمندان معتقدند که واژه‌های انگلیسی 4 ور فرانسه‌ی 811123838 از این واجريیشه مشتق
11784 نشده‌اند بلکه از واجریشه‌ی هند و اروپایی ۷۷338* هستند.
11785 ۲- در فارسی واژه‌ی " کارزار" بعنی "محل نبرد؟: "کار" * نبرد و پا جنگ و آزار"< محل (مانند "گلزار").
11786 ۳ البته ان واژه در فارسی امروز به چم "عمل" و "پیشه" و "کردار" بکار می‌رود.
11787 چ
11788 [pdf page 396]
11789 کارد / ۳۹۷
11790 اوستایی (4287427): چکه (2804): 8 نی انش
11791 157 ۴۸۹8۲۸ ۰ لینرانی (/7/۸(/4۸): 38871 ,1637
11792 پهلری (الاماتلوم: ز نی (تی) (اسمتاتمم: ‏ 0987 ,۲3830
11793 اوستی (05957/0): باقشا پروسی کهن (/(5914تا۲۸ ۰:۵ 118715
11794 کردی (08.0150): ,161830 آلبانی (7420لمهلم: ۳
11795 بلوچی (/ل۲ناملم8): ۸ ما هنیت (17۳7175): ۸7۸7
```


## [2026-09-06T21:21:10.273Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T21:21:11.734Z] TOOL RESULT

```
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
```


## [2026-09-06T21:21:17.993Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B1%D9%88%D8%A7%D9%86/",
 "prompt": "Quote the فرهنگ معین entry for کاروان — meaning and origin tag (e.g. [په.] Pahlavi). Also quote the دهخدا etymology if given."
}
```


## [2026-09-06T21:21:19.248Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B1%D8%B2%D8%A7%D8%B1/",
 "prompt": "Quote the فرهنگ معین and دهخدا entries for کارزار — meaning and origin/etymology (Pahlavi kārēzār?)."
}
```


### [2026-09-06T21:21:25.505Z] TOOL RESULT

```
# کاروان (Caravan)

## فرهنگ معین Entry
**[ په . ] (اِمر. ) "قافله ، عده ای مسافر که با هم حرکت کنند."**

The abbreviation "په" indicates Pahlavi origin, and "اِمر" denotes it as a compound word.

## Etymology (لغت نامه دهخدا)
The Dehkhoda dictionary traces کاروان to **کاربان** (from جهانگیری and برهان sources), also noting alternative forms like **قیروان** and **عیر**. The entry documents this as a collective noun for merchants and travelers moving together.

According to Dr. Jelal al-Din Kazazi's analysis cited in the general encyclopedia section, the word's structure breaks down as: **کاره (kara) + وان (van/ban)**, where کاره derives from Old Persian meaning "army/military force" and وان functions as a suffix—thus originally meaning "that which warriors guard."
```


### [2026-09-06T21:21:25.681Z] TOOL RESULT

```
# کارزار (Kārzār)

## Farhang-e Moein Entry
"(اِ.) جنگ، جدال، نبرد" — This classical dictionary defines the term as battle, quarrel, and combat.

## Dehkhoda Entry
The Dehkhoda dictionary provides etymological insight: the word combines "kār" (meaning war/combat) with "zār" (a suffix denoting abundance or place), literally describing a "place of warfare." The entry notes this composition parallels words like "morgh-zār" (pheasant grounds) and "lāla-zār" (tulip fields).

## Pahlavi Origin
The historical documentation indicates the term derives from Pahlavi "kārēčār" (کارچار), maintaining the same compositional structure of war + place designation that evolved through Persian literary tradition into the modern meaning of battle or engagement.
```


## [2026-09-06T21:21:39.541Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kóryos|page 274 root Koro: PIE *kóryos 'war, troops' and descendants\" \\\n \"https://en.wiktionary.org/wiki/کاروان|page 274 node 2: Persian karvan from MP karawan, borrowings into Arabic/Italian/French/English\" \\\n \"https://www.etymonline.com/word/caravan|page 274 nodes 3-4: French caravane, English caravan and van\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/harjaz|page 274 node 5: PGmc *harjaz 'army' and compounds harjaberhtaz/harjawaldaz\" \\\n \"https://www.etymonline.com/word/harbor|page 274 node 6: harbor from OE herebeorg, *harja-bergaz\" \\\n \"https://www.etymonline.com/word/Harry|page 274 node 6: Harry (name) = familiar form of Henry; harry (verb) from *harjon\" \\\n \"https://www.etymonline.com/word/Harold|page 274 node 6: Harold from PGmc *harja-waldaz 'army commander'\" \\\n ; do\n  url=\"${u%%|*}\"; note=\"${u#*|}\"\n  python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T21:21:44.452Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b752b1380767177a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/af7d2726753d17b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1773570b399651c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a7658c832804b6a1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b6723f326757c9c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/27d028af1686ed73.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/327f0dd5e33ca348.txt
```


## [2026-09-06T21:21:53.393Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/كرب|page 274 node 8: Arabic karb 'grief, anguish', root k-r-b\" \\\n \"https://en.wiktionary.org/wiki/کرب|page 274 node 8: Persian karb entry (field maple, from Mazanderani) - no IE 'sorrow' word\" \\\n \"https://abadis.ir/fatofa/کرب/|page 274 node 8: Mo'in and Dehkhoda mark Persian کرب as Arabic [ع.]\" \\\n \"https://en.wiktionary.org/wiki/garbo|page 274 node 10: Italian garbo etymology (OHG garwi / Arabic qalib)\" \\\n \"https://www.treccani.it/vocabolario/garbo3/|page 274 node 10: Treccani garbo3 - Arabic qalib, archaic wine-flavour sense\" \\\n \"https://en.wiktionary.org/wiki/herb|page 274 node 9: German herb < MHG hare/here, infl. harwe/herwe < PWGmc *haru\" \\\n \"https://en.wiktionary.org/wiki/کرنا|page 274 node 2: Persian karna 'long trumpet' - Semitic qarna vs native kar+nay\" \\\n \"https://abadis.ir/fatofa/کاروان/|page 274 node 2: Mo'in [pahlavi] karvan; Kazzazi kara 'army' + van\" \\\n \"https://abadis.ir/fatofa/کارزار/|page 274 node 2: Dehkhoda karzar = kar 'war' + zar 'place', Pahlavi karecar\" \\\n ; do\n  url=\"${u%%|*}\"; note=\"${u#*|}\"\n  python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T21:22:03.589Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/69085ea758d5d714.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b63a09db56ceb2b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0d243a512652e8d2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2874f3f93c7731b6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd80431ff995a978.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/990e52e81caf9ecb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/084319d2105ad65c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c7e5571899b227e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e0560d52bd8bcdb0.txt
```


## [2026-09-06T21:22:06.248Z] TOOL CALL #65: Bash

```json
{
 "command": "sed -n 1,160p tools/verify_check.py"
}
```


### [2026-09-06T21:22:06.289Z] TOOL RESULT

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


## [2026-09-06T21:22:33.165Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK bitter roots kor ===\"; grep -n \"lemma: kor\" POK_full.txt; grep -n \"^kor\" POK_02.txt | head -20\necho \"=== POK ker- 3 grow / koros satiety ===\"; grep -n \"Sättigung\\|satiety\" POK_02.txt | head -5"
}
```


### [2026-09-06T21:22:33.232Z] TOOL RESULT

```
=== POK bitter roots kor ===
48081:Root / lemma: koro-s, kono-s 
4311:kormen-  ,Wiesel*,  s.  oben  unter  6.  ker-,
4316:kormo-  ,Qual,  Schmerz,  Schmach*.
4321:koro-s,  korio-s  ,Krieg,  Kriegsheer*;  korio-no-s  , Heerführer*.
=== POK ker- 3 grow / koros satiety ===
3643:gT.  ixÖQsaa,  nogi-oo)  (späteres  Präs.  xogsayLO)  und  xogevvvfiL]  Perf.  x«xd- osoiiai)  ,sättigen',»  -/.oqoq  , Sättigung';  *yiOQ>Fog  in  att.  xögog  ==  hom.  ion. y.ovQOg,  dor.  '/,cüQog  ,adulescens'  (später  auch  , Schoß,  Schößling,  junger Zweig'),  fem.  ark.  Dat.  Sg.  xögJ^ai,  att.  -aögr],  hom.  ion.  xovqt],  dor.  xw^a , Mädchen,  Jungfrau;  Augenstern',  hom.  xovQ7]Teg  , waffenfähige  Jungmann- schaft^;  wahrscheinlich  v.elcüQ,  -wgog  ,Sohn,  Abkömmling'  (diss.  aus  *y,SQcoQ, ursprüngl.  n.  , Nachkommenschaft') ;
```


## [2026-09-06T21:22:34.584Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CF%81%CE%BF%CF%82",
 "prompt": "Quote the Ancient Greek entries for κόρος: the senses ('satiety, surfeit, insolence' and 'boy') and their separate etymologies (PIE roots)."
}
```


### [2026-09-06T21:22:39.701Z] TOOL RESULT

```
# Ancient Greek κόρος: Entries and Etymologies

## Etymology 1: "Boy" Sense
**Entry:** "boy, youth" with alternate meanings of "soldier" and "son"

**Etymology:** Derived from Proto-Hellenic *kórwos* meaning "boy," ultimately tracing to Proto-Indo-European *ḱer-* meaning "to grow"

## Etymology 2: "Satiety" Sense
**Entry:** "being satisfied, satiety, surfeit" and "insolence, petulance"

**Etymology:** Also sourced from Proto-Indo-European *ḱer-* with the same "to grow" meaning

Both senses share the same ultimate PIE root despite their distinct semantic developments in Ancient Greek.
```


## [2026-09-06T21:22:52.762Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==471' incoming/WLD/WLD_Bd1_pages.txt | head -30"
}
```


### [2026-09-06T21:22:55.234Z] TOOL RESULT

```
                                                                                                                 -




462                                             kor         qor-


wahracheinlich gr. Lw., mit Ausgang nach modius, so daB dafiir keine Wzf.
auf -gh- anzunehmen ist, Uhlenbeek IP. 13,217).      Unsicher lett. sence
„Huschel“ (Prellwitz 1 155, 2 232), da sence die richtigere Form scheint
(Bezzenberger BB. 27, 175 Anm. 1; seine zw. Anreihung yon nsloven. sence
„Schlafe“ ist mir wegen des Alleinstehens des Wortes im Slay, und bes.
wegen seiner Gdf. *semcb nicht glaublich).
   Gr. xoylog, y.oyXiag „Muschel, Schneckenhaus, Sehnecke" (von Thurneysen
H. Osthoff zum 14. August 1894, Karl II. Meyer IF. 35, 232 Anm. abwei-
chend zu kagh- „umfassen“, richtiger „Flechtwerk“, gestellt, was aber den
Sinn verfehlt), und kaum als nasallose Varianten anzureihen, die Nasal-
losigkeit auch kaum aus Kreuzung mit xayXrj £ „Stein, Kiesel, Uferkies"
(a.                      Fick II 1 i>9 verbindet sie mit ir. cuailen, angeblieh
       kaghlo-) zu verstehn.
„Krause, Haarlocke" (?), ebenfalls wenig glaubwiirdig.


kor- „Reiserbesen (und damit fegen); Reisigbiindel                                        (als   Fischreuse, als
        Seihvorrich tung)“ ?
   Gr. y.ogog „Besen", xogecn „auskehren, ausfegen, reinigen", veco-xogog
„Tempelaufseher“, (der ihn rein zu halten hat), ogxo-xogog „Stallknecht“?
xoaxivov „Sieb“ (Denominativ einea *xoay,a> = *x og-axml Wiirde aber altes
verbalea „fegen“ vorauaaetzen.     Lit. kos-iu, -ti, lett. hast „aeihen“ hat idg.
```


## [2026-09-06T21:22:59.275Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Kriegsheer\\|harjis\" incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-06T21:22:59.325Z] TOOL RESULT

```
43828:qor- „Kriegsheer, Krieg".
43845:      got. harjis, aisl. herr, ags. here „Heer“, ahd. as. fieri „Heer, Menge 11 (aber
```


## [2026-09-06T21:23:02.838Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '43828,43860p' incoming/WLD/WLD_Bd1_pages.txt\npython3 - <<'EOF'\nlines=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=1\nfor i,l in enumerate(lines,1):\n    if i==43828: print('leaf',leaf,'printed p',leaf-9)\n    leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-06T21:23:04.747Z] TOOL RESULT

```
qor- „Kriegsheer, Krieg".
  Gr. xoigavog „Heerfiihrer, Konig, Herr“ (Ableitung von *xoiga aus *xogta
mit Formans -no-, wie z. B. got piudans „Konig von pinda „Yolk“; eben-
                                                .
                                                                           f
                                                                               ‘



ao aisl. hcrjann „Heervater“ als Beiname Odins von harja- „Heer“ aus;
OathoffIF. 5, 275 ff. mit Beurteilung friiherer Deutungen von xoigavog Falk-                                ;


Torp  u. fuer), xoigavem „befehlige; herrsche", xoigavia „Herrschaft“, vgl.
vom unerweiterten *xoTga (oder *xolgo-). EN. wie Koigoyayog (Boisacq a. v.);
      mir. cuire „Schar,       Menge", gall. Tri-, Petru-corii Yolknamen                             („die drei,
vier Heere‘‘);
      got. harjis, aisl. herr, ags. here „Heer“, ahd. as. fieri „Heer, Menge 11 (aber
dt.    Hiiringl,    ahd. haring,       ags. licering fiigt         sich        im Yok. nicht;         a.   Kluge 8   ,

auch Weigand-Hirt a. v.).
      Lit. karias „Heer“, karijs „Krieger“, lett. kar's „Krieg‘‘, apr. knrqis (iiber-
liefert k rag is;     Bezzenberger BB. 28, 159) „Heer                 [
                                                                          ‘,       caryawoytis „Heerschau“.
       Ohne formantisches -{o-,          -fa-       lit.   Lams „Krieg“ (wahrend kdie „Krieg“
mit -e aus -in;             beide    nicht besser zu gar- „schmahen, strafen“) und
dehnstufig         apers.    Kara-     m. „Kriegsvolk, Heer; Yolk", npers. kar-zar
                         korka (kroka?)    -ela   — kormno-, krmno-                             463

„Schlachtfeld“. Sind diese durch riicklaufige Ableitung aus *qor-{o- ent-
standen oder dessen Grundlage?
  Vgl. auBer Osthoff aaO. noch Zupitza Gutt. 109 (hier unter Vermengung
mit qar- „schmahen‘‘, wie auch bei Fiek I 4 377, und anderem), Berneker 578,
leaf 471 printed p 462
```


## [2026-09-06T21:23:28.578Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT Heerschar / kara ===\"; grep -n \"Heerschar\" BRT.txt | head -5\necho \"=== BRT 1215 ===\"; grep -n \"kara-\\|kāra\" BRT.txt | head -8\necho \"=== FSD caravan v1 ===\"; grep -n \"caravan,\" FSD_vol1.txt | head -3\necho \"=== WEB caravan ===\"; grep -n \"car'a-van\\|caravan \" WEB_vol1.txt | head -3\necho \"=== SKT CARAVAN ===\"; grep -n -i \"caravan\" SKT.txt | head -5\necho \"=== DEV caravane ===\"; grep -n -i \"caravane\" DEV.txt PHN.txt | head -5"
}
```


### [2026-09-06T21:23:28.690Z] TOOL RESULT

```
=== BRT Heerschar / kara ===
28704:.  j.  'haena-,  p.  haini-  f.  'Heer,  Heer-  ■  ■  ^'^  Z'^",  h«^_^rinHi  .  .  a3aih>a schar'  uzw.  rfa?^ischer  Wesen,  'Feindes-  'i^^lsva  . .  hau  astt  äafvö. .  avat  daa,a heer,  feindliche  Heerschar':  Wabiy  imäm  ^^'"'^'"■'»^  ' . .  (sva.)  dort  ist  der  Z>. . daÄyäum  mä  5>;/.,>J*  ma  'nä  D.4.3;  V-Z-SafO;  _  s.  noch  H.1.7  (Sp.173»  o.); ^  n^it  i^ra  atryA  dai^hävS  fräs  (%A..)  "  ™  Gegensatz  zu  ÄJ  (Sp.  1718  o.):  >Sff yiyj/  •;«»  YtÄs6;  F.l-^;  -  ^«laäa  «P^-m^r^tS  i%^.  1143  m.)  ,4 5 «  ,.j-;tjr^.- «(■rr-^-b'iT  rfa/Vi^«4>.S  ■««  (NP.)')  frapatänti  '""'^  iäW  ..V.4.AS;  -  zugleich  aul  ein Yt..y.6i:  —  ya'ba  yai  hazarirS.aspam  erläuterndes  Nomen  vorausweisend:  aoa 'nam  avazeit  mäzduya'sni!  avi  vis5  Y.  hau  apa^^arS bvatzraya»ks vouru.kaiahe i8'.i^;  -  Ümäm  daAyüufn  ^ura^mazdj  ^""^  yH  haosravA  nqma  Ytip.sS;  59, patup  haia'nmD.4.6;  —  'nayä^axra-  ^'-  ")  '"  schwachdciktischer  Vcr- vai^yä  z>yazJayä  (sd.)  Aog.  A;  Yt  5.  131,  Wendung  jener,  der';  I)  zurückweisend; 4.  3.  19-  93,  ^-  II  (wo  'nayiuay-'nyhla  ^  *"/  f  ?  ^^O'uen;  a)  auf  ein  Substantiv; .  .  davai^yi  pataihyä  Y.0.18;  —  fiairi  «>  adjektivisch:  II  War««*  näm^  pärsa* ^•nyhsia  pöiynäuyS  Y.  68. 13;  -  ivi  'nayi  1  ■  ■  ''/'"'  ^'^rnaf  hada  kärä  al,yav^  Bh. (AP.)'>  xrvi^ätl!  Yt  10.  8;  />  49,  /<?.  54;  1  ^-  K^^'  '■  »?'  ^-  ?-  5-  • !  —  'Jäw«  /Jwa« —  ;*a.n<i>7'a/4yff*-«ÄS;'?"  Y.i7.asi>.  ^fi-ätfayam  . .  ya-^a  hauv  karJ'  parä- Ableit.  —  Zum  V.  ^(>>.  —  ai.  sinä-  f.  '"öJir  . .  Bh.  5. 1 ;  ü  —  »flr?m  afavarum  .. 'Heer';  mp.  (Pü.)  Äe«.  —  ')  NPn.  aUtt  NPf.  j  *hau  *n3"  .  .  P.2^;  —  zugleich  auf  ein (wie    umgekehrt,  S   ¥"■    3  d).     Vgl.    dazu  1  Rglativum    vorausweisend:    Wkärt/'    hyi^
=== BRT 1215 ===
3623:Ableit.  BPS  "apa-skara-  m.;  Et.  und  Bed.?
9227:•  j.  'kara-  n.  Name  eines  Fisches";  'r5'     Karchedonier  (KarthagerV
9234:.]  'kara-m.EN.emesTuramers:.^.j^e^^  ^'^^^   ^^^  ^^^^^._  \           y^  j^/,jJl
9238:•  j.,  p.  ^kara-  Adj.  (fem,  VT"-)  'machend  'Geier'O,  al.  fytaivafav-  m.  'Hahn'.  —  Pü,: (usw.)'.  *'^*-  —  '*  ZDMG.  s6.  63  i  haplol.  auä  *iar-
9503:465  kara-  —  ^kiritaji-  466
9527:•«M.  m.  'Tal'.    lum  V.  iar-.    —    ai.  'kara-,    ,,.        ,   ,°  °  °
9671:•  j.  ^gaiwa  kUTÖ  kurö  lartwani  kara- panS  rä>wyasnam  buxtä  mähe"  FrW.2.  z.
10635:•  j.,  g.  xrafstra-  n.  i)  im  gAw.  'wildes Tier,  Raubtier":  atibyS  mas  äsä  syasdat (sd.)  yentat  ahmat  aurunä  'rH  (AP.)  Y. $4.  9.  a)  im  Plur.  als  Bezeichnung  für die  nicht  sesshaften  Religionsfeinde  und deren  Gölter,  sva.  'Raubgesindel':  anä mq'ira  maxist?in  väurüimaidl  (sd.)  Tä (A'P.)  hizvä  Y.  28.5;  —  pari  *vä  vJspäis pars  vaox?mä  dalviliscil  °räis  maSyäis^ä "losgesagt  haben  wir.  uns  von  allen  Xraf- stra^ (allem  Raubgesindel),  den  Daivas wie  den  Menschen"  "  Y.34. 5 ;  verwendet  Y. ig.  2.  2)  im  jAw,  Bezeichnung  fUr  alle schädlichen  ((/iZÄischen)  Tiere,  bes.  der niederen";  paitUtätie  a/astaca  zBüdiftaca apayantamaheca  a?prahe  mainyius  °ra Yt  21.1;  —  duye  Saite  kahyäcit  ar>rö.- mainyavanqm  "ranqm  ava.janyäl  V.  16. 12;  —  ähva  vyar?hähva  (sd.)  e^mB  'ra ham.bavainti  yim  tnasyäka  spis(sd.  tiqma aojaitt  V.  z/. 3;  —  *maxSiMhrpa  ..*akara- tum-driwyi  (sd.)  ya%a  taehdistäiS  'räis V.  7.  2;  —  Y.  ig.  2:  s.  unter  1.
=== FSD caravan v1 ===
57462:Addison  Spectator,  Jan.  St,  i ***“-'*  * [<  Per.  tdrtcdnsarOJ,  <   Idricdn,  caravan,  + ■   tnr&i,  palace.] car'a-van'se-ra};  car"a-Tan'sc-ral};  car -   car"a-ran-sc'rl-al,  a.  Of  or  relating  to  a   carovonwry.
=== WEB caravan ===
36562:ine: punts are often directed to a coffin cor- ner so that the ball will roll out of bounds and be put back into play near the opponent's goal line. f s cof’fin joint, the joint in a horse's foot above the coffin bone. i cof’fin nail, a cigarette. [Slang.] coffin plate, an inscribed metal plate fastened to the lid of a coffin. cof'fle, n. [Ar. kafila, a caravan.) a number persons or animals fastened together; cially a caravan or gang of slaves chained gether or driven along together. a cof’fle, v.t.; coffled, pt.. pp.; coffling, ppr. fasten together in or as in a c s cof’fret, n. {Fr.] a smali coffer; an orn casket. ant co-found/ér, S a joint founder. cog, v.t.; cogged, pt., pp.; cogging, ang extension of cog Persie 1. to flatter; to wh e; to sedi from, by adulation or artifice. I'll cog their hearts from them. 2. to obtrude or thrust in, by deception; as, to cog in a wi pose. [Rare. f a te udulently; as, _ 4. to cheat; io aerate $ load a die
=== SKT CARAVAN ===
2978:Caravan.  (F.-Pers.)  F.  caravam.'^ VtT%,  karufdn,  a  caravan,  convoy.
2979:oaravanaary.  (Pen.)  Pcrs.  kanvdn- tardy^  cm  bin  for  camvans.  —  Fcrs.  kartptin, caravan;  saniy,  public  building,  uax,
23616:flertiani  bang  (t),  barbican?,  bashitw, LT,  caravan,  caravansary',  dervia  (der- bi.  divan,  durbar,  6rman,  ghoul,  bonri, leal,  jasmine  ijetsambe),  Lascar,  mohur,
=== DEV caravane ===
DEV.txt:998:Cahavanskiiah..  En  persan  ^^\yjéj\^yi  karwân-serfn ,  hôtel de  la  caravane.
DEV.txt:1016:Caravane.  Du  persan  ij^^y^  karwfm,  même  sens.  De  îè vient  :
DEV.txt:1017:Caravansérail.  En  persan  ^^\y^'\^^é  karwân-serâï ,  hôtel de  la  caravane.
DEV.txt:1125:Chiaoux  ou  Ghaoux.  DansBocthor  (j;iw)^l^  djâoulch;  mais le  mot  est  pris  du  turc  {j^^^  tchâouch,  en  persan  (j^^ji^^s- khâwoïich,  chef,  conducteur,  r^ Proprie  est  vox  Turcica,  dit Vullers,  significans  apparitor,  famulus  aulicus.  ?)  M.  Pavet de  Courteille,  dans  son  Dict.  du  turc  oriental,  a  noté  (J^^^ avec  le  sens  de  huissier,  conducteur  de  caravane,
DEV.txt:2115:Simoun  ou  Semoun.  De  l'arabe  ^^^s»  semoûm,  vent  brû- lant de  l'Afrique,  ainsi  nommé  de  la  racine  jpw  samm,  em- poisonner, c^  C'est  un  coup  de  simoun  qui  nous  arrive.  Con- fortablement pelotonnés  sur  nos  banquettes,  nous  sommes à  l'abri  des  dangers  du  fameux  vent-poison  si  redouté  des caravanes,  w  (Guill.  Lejean^)
```


## [2026-09-06T21:23:36.259Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/κόρος\" --note \"page 274 root Koro: Ancient Greek koros 'satiety, insolence' belongs to PIE *ker- 'to grow', not to *koryos\" 2>&1 | tail -2"
}
```


### [2026-09-06T21:23:38.963Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c3e840e994094f1f.txt
```


## [2026-09-06T21:31:29.061Z] TOOL CALL #73: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk274.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n \"entry\": 0,\n \"root\": \"Koro / Koros\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *koro-s / *kor-yo-s (Wiktionary *kóryos) 'war; war-band, host, army'\",\n \"note\": (\"The first half of the box is solidly confirmed. Pokorny 615-616 heads the entry \"\n   \"'koro-s, korio-s ‚Krieg, Kriegsheer‘; korio-no-s ‚Heerführer‘', with exactly the two \"\n   \"branches Nourai draws: 'apers. kāra- m. ‚Kriegsvolk, Heer; Volk‘, npers. kār-zār \"\n   \"‚Schlachtfeld‘' and 'got. harjis, aisl. herr, ags. here ‚Heer‘, ahd. as. heri ‚Heer, Menge‘'. \"\n   \"The gloss 'a large crowd' is justified by that 'Heer, Menge' and by Mir. cuire 'Schar, Menge'. \"\n   \"The second line, 'Koros: fighting, bullying, arrogance', is lifted verbatim from Mann IEC 536, \"\n   \"who however keeps koros (2) 'arrogance, rudeness, bullying, fighting' as a SEPARATE lemma from \"\n   \"korios (1) 'troop, band, flock, host' (also p.536) and himself warns '(Sl. & Balt. ambig. w. \"\n   \"influence of type kar-, q.v.)'. Mann's only non-Balto-Slavic witness for that lemma is Gk. \"\n   \"κόρος 'arrogance', which belongs elsewhere: Pokorny 577 and Wiktionary put κόρος \"\n   \"'satiety, surfeit; insolence' (beside κορέννυμι 'to sate') under PIE *ḱer- 'to grow, feed', with a \"\n   \"palatal *ḱ- that cannot yield the velar *k- of *koryos. Merging the two lemmas into one root box, \"\n   \"and the resulting gloss 'fighting, bullying, arrogance', is therefore Nourai's own step, not Mann's; \"\n   \"the Lithuanian káras 'war' that Mann files under koros (2) is in fact the same word Pokorny files \"\n   \"under koro-s. Verdict plausible: right root, over-wide gloss.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *koro-s / *kor-yo-s «جنگ؛ سپاه، گروه جنگاور» در پوکورنی \"\n   \"(صفحهٔ ۶۱۵–۶۱۶) و والده–پوکورنی (جلد ۱ ص ۴۶۲) دقیقاً همین دو شاخه را دارد که نورایی کشیده \"\n   \"است: پارسی باستان kāra- «سپاه، مردم» و فارسی «کارزار» از یک سو، و گوتی harjis و انگلیسی کهن \"\n   \"here «سپاه» از سوی دیگر. امّا سطر دوم جعبه («Koros: دعوا، زورگویی، گردن‌کشی») عیناً از مدخل \"\n   \"جداگانهٔ koros (2) در فرهنگ من (ص ۵۳۶) گرفته شده و خود من آن را از korios (1) «سپاه، گروه» جدا نگاه \"\n   \"داشته و آن را مشکوک خوانده است. گواه اصلی آن مدخل، یونانی κόρος «سیری، گستاخی»، در پوکورنی (ص ۵۷۷) و \"\n   \"ویکی‌واژه زیر ریشهٔ *ḱer- «روییدن، سیر کردن» آمده که کاف کامی آن با کاف خالص *koryos سازگار نیست. \"\n   \"پس ادعای نورایی در بخش «جنگ و سپاه» درست است، ولی افزودن معنای «گردن‌کشی» با احتیاط پذیرفتنی است.\"),\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/kóryos\", W+\"κόρος\"],\n \"ref_check\": [\n   {\"ref\": \"POK:615\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW p.615-616 (POK_02.txt leaf 276, line 'koro-s,  korio-s  ,Krieg,  Kriegsheer*;  korio-no-s  , Heerführer*.'): '1. Ohne formantisches -io-, -ia-: lit. káras ‚Krieg‘ und dehnstufig apers. kāra- m. ‚Kriegsvolk, Heer; Volk‘, npers. kār-zār ‚Schlachtfeld‘' ... 'got. harjis, aisl. herr, ags. here ‚Heer‘'. Exactly Nourai's 'Koro: war, army, a large crowd'.\"},\n   {\"ref\": \"IEC:536\", \"status\": \"partial\",\n    \"note\": \"Mann IEC p.536 (IEC.txt leaf 305, page number '535'/'536' printed on the leaf) has BOTH 'korios (1) ‘troop, band, flock, host. WP I, 462 ... OPer. cf. kara- people, host; ... Go. harjis ‘army’' AND, as a separate lemma, 'koros (2) ‘arrogance, rudeness, bullying, fighting’. (Sl. & Balt. ambig. w. influence of type kar-, q.v.) Gk. kóros ‘arrogance’; OCS korŭ ‘contumely’; ... Li. káras ‘war’'. The page carries both of Nourai's glosses, but as two entries, not one root.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.462 (WLD_Bd1_pages.txt leaf 471)\", \"stance\": \"supports\",\n    \"note\": \"'qor- „Kriegsheer, Krieg“. Gr. κοίρανος „Heerführer, König, Herr“ ... got. harjis, aisl. herr, ags. here „Heer“ ... dehnstufig apers. kara- m. „Kriegsvolk, Heer; Volk“, npers. kar-zar „Schlachtfeld“.' No 'arrogance' sense.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. koro- (AHD_watkins1985.txt)\", \"stance\": \"supports\",\n    \"note\": \"'koro-. War; also war-band, host, army. I. Germanic *harjaz, army. ... [Pok. koro-s 615.]' Gloss identical to Nourai's first line; no 'arrogance'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 20.15 ARMY, p.1377\", \"stance\": \"supports\",\n    \"note\": \"Buck's ARMY table lists 'Goth. harjis ... ON herr ... OE here ... OHG heri ... Lith. kariuomene (karias) ... OPers. kāra-, haina-' — the same equation of OP kāra- with Gmc *harjaz.\"},\n   {\"src\": \"POK\", \"where\": \"IEW p.577 ker-3 (POK_02.txt, „Sättigung‘)\", \"stance\": \"contradicts\",\n    \"note\": \"Pokorny files 'gr. κορέσαι, κορέννυμι ‚sättigen‘, κόρος ‚Sättigung‘' under ker- ‚wachsen‘ — i.e. the Greek word behind Mann's 'arrogance' lemma is not from the war-root.\"}\n ],\n \"nodes\": []\n}\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"kâr 2, kâra 2; u-kâra\", \"verdict\": \"confirmed\",\n \"derivation\": (\"OP kāra- (Nourai's 'kâr 2, kâra 2') is the ordinary Achaemenid word for the levy: \"\n   \"Kent's lexicon (p.180) gives 'kāra- sb. ‘people, army’: Lith. káras ‘war’, dialectal ‘army’, Gt. harjis \"\n   \"‘army’, NGm. Heer', and it is the word used throughout the Bisotun inscription (DB 1.33 kāra, DB 2.30f \"\n   \"kāra hya hamiçiya 'the rebel army'). Formally it is a lengthened-grade *kōro- beside Lith. káras, \"\n   \"Gmc *harjaz (Pokorny 615: 'dehnstufig apers. kāra-'). The compound u-kāra- is u- 'good, well' \"\n   \"(Av. hu-, Skt. su-, PIE *h₁su-, hence Nourai's cross-reference to Su 1) + kāra-, attested once as \"\n   \"ukāram in Artaxerxes' Hamadan inscription (AsH 9). Both the language label and both glosses are right.\"),\n \"derivation_fa\": (\"«kāra-» در پارسی باستان به معنای «سپاه، مردم» است و در سنگ‌نبشتهٔ بیستون بارها به کار رفته \"\n   \"(مانند kāra hya hamiçiya «سپاه نافرمان»). کنت (ص ۱۸۰) آن را هم‌ریشهٔ لیتوانیایی káras «جنگ» و گوتی harjis \"\n   \"«سپاه» می‌داند؛ پوکورنی نیز آن را صورت کشیده‌واکه (dehnstufig) ریشهٔ *koro-s می‌شمارد. ترکیب \"\n   \"u-kāra- از پیشوند u- «خوب» (اوستایی hu-، سنسکریت su-) و kāra- ساخته شده و یک بار در کتیبهٔ ارتخشتر در \"\n   \"همدان (AsH 9) به صورت ukāram آمده است. ادعای نورایی درست است.\"),\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/kóryos\"],\n \"ref_check\": [\n   {\"ref\": \"POK:615\", \"status\": \"supports\",\n    \"note\": \"IEW 615: 'dehnstufig apers. kāra- m. ‚Kriegsvolk, Heer; Volk‘' — the OP word is cited in the root entry itself.\"},\n   {\"ref\": \"KNT:175\", \"status\": \"supports\",\n    \"note\": \"KNT.txt leaf 198 carries the printed page number '175' and, on it, 'ukāra- adj. ‘having good people or army’: from u- ‘good’ + kāra- ‘people, army’. ukāram asn. for asf. AsH 9'. Nourai's page is exactly right for u-kāra; the simplex kāra- is five pages later (p.180, leaf 203).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"p.180 s.v. kāra- (leaf 203)\", \"stance\": \"supports\",\n    \"note\": \"'kāra- sb. ‘people, army’: Lith. káras ‘war’, dialectal ‘army’, Gt. harjis ‘army’, NGm. Heer (§143.III); cf. König, KIP 66. See also ukāra-.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.462\", \"stance\": \"supports\",\n    \"note\": \"'dehnstufig apers. kara- m. „Kriegsvolk, Heer; Volk“, npers. kar-zar „Schlachtfeld“' under qor- „Kriegsheer, Krieg“.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 20.15 ARMY p.1377\", \"stance\": \"supports\",\n    \"note\": \"'OPers. kāra-, haina-' listed as the Old Persian words for 'army'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p.536 korios (1)\", \"stance\": \"supports\",\n    \"note\": \"'OPer. cf. kara- people, host' heads Mann's list of descendants of korios (1).\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"kâr- «کار ۲»; kâr-dâr «کاردار»; kâr-vân «کاروان»; kor-nâ «کرنا»; kâlenjâr «کالنجار» (+ کارزار، کلنجار)\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Word by word. (a) kār 2 'war, army' as a first member: real and well attested. OP kāra- \"\n   \"'army' > MP kār, which MacKenzie (PHD 48) still lists separately as '2kār [kʾI], pl. -ān: (other) people'; \"\n   \"its clearest survival is kārzār (printed on the page in parentheses after کار ۲), MP kārēzār, on which \"\n   \"Nyberg's glossary is explicit: 'kārē- cas. obl. of kār < OP kāra- ‘army’, + čār from Av. kar- ‘to move’'. \"\n   \"This kār is homonymous with, but distinct from, the everyday kār 'work' (< Av./OIr. *kārya-, Mo'in's \"\n   \"footnote in Borhan p.1553), which is why Nourai numbers it '2'. (b) kār-dār 'chargé d'affaires, \"\n   \"operations chief' = kār + dār 'holder' (☞ Dher 1). Horn no. 834 reports 'Nöldeke (mündliche Mitteilung) \"\n   \"stellt hierher np. kārdār ‚Vezir‘', i.e. Nöldeke did assign it to the 'army' kār; Mo'in's footnote \"\n   \"(Borhan p.1559) simply writes 'از: کار + دار (دارنده)' without deciding which kār — plausible, not proven. \"\n   \"(c) kār-vān: MP kārawān, glossed by MacKenzie precisely 'caravan, military column'. Mo'in himself invites \"\n   \"the connection ('قس: کاروان' at the end of his kārzār footnote, Borhan p.1560), and Kazzazi analyses it as \"\n   \"kāra 'army' + -vān; but Klein (238), Lokotsch 1075 and Etymonline instead derive Pers. karwān from Skt. \"\n   \"karabha- 'camel', and Wiktionary stops at MP kʾārwān without an etymology. Genuinely contested. \"\n   \"(d) kor-nā/karnā 'long war-trumpet' (☞ Nedo = nāy 'reed-pipe'): the analysis kār 'army' + nāy is the \"\n   \"traditional Persian one and is reported as such by Wiktionary, which nevertheless prefers a Semitic \"\n   \"source (Syriac qarnā, Akk. qarnum, Ar. qarn 'horn'); a third native guess is xar 'donkey' + nāy. \"\n   \"(e) kālenjār 'fight': Mo'in's footnote on the very page Nourai cites (Borhan p.1575, s.v. کالجار/کالنجار) \"\n   \"reports the derivation from Gilaki kālčār, Pahlavi kārēčār and Persian kārzār, adding 'رک: کارزار'; a rival \"\n   \"note on the same and the next page derives کالنجار from kālī 'dry rice stalks' + -زار (rice-field) or from \"\n   \"the Indian fort-name Kalinjar. So: (a) and (e) confirmed, (c) and (d) plausible-but-contested, \"\n   \"(b) plausible; node verdict plausible.\"),\n \"derivation_fa\": (\"الف) «کار ۲» به معنای «جنگ، سپاه» جدا از «کار ۱» (= عمل، پیشه، از *kārya-) است؛ این کار از پارسی باستان \"\n   \"kāra- «سپاه» > فارسی میانه kār می‌آید و روشن‌ترین بازماندهٔ آن «کارزار» (پهلوی kārēčār) است؛ نیبرگ \"\n   \"صریح می‌گوید kārē صورت مایل kār < پارسی باستان kāra- «سپاه» است. ب) «کاردار» = کار + دار؛ نولدکه \"\n   \"(به نقل هرن، شمارهٔ ۸۳۴) آن را به همین «کار» سپاهی برمی‌گرداند، ولی معین در حاشیهٔ برهان قاطع فقط می‌نویسد «از: کار + \"\n   \"دار (دارنده)». ج) «کاروان» از فارسی میانه kārawān است که مکنزی آن را دقیقاً «caravan, military column» \"\n   \"معنا کرده و معین نیز در پایان حاشیهٔ کارزار «قس: کاروان» آورده است؛ امّا کلاین و لوکوچ آن را به سنسکریت \"\n   \"karabha- «شتر» می‌برند. د) «کرنا»: ریشه‌شناسی سنتی فارسی آن را کار (سپاه) + نای می‌داند، ولی نگاه امروزی \"\n   \"آن را وام‌واژه‌ای سامی (سریانی qarnā «شاخ، بوق») می‌شمارد. ه‌) «کالنجار»: در همان صفحهٔ ۱۵۷۵ برهان \"\n   \"قاطع که نورایی ارجاع داده، معین آن را از گیلکی «کالجار»، پهلوی kārēčār و فارسی «کارزار» گرفته است. \"\n   \"روی هم رفته، ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [W+\"کاروان\", W+\"کرنا\", \"https://abadis.ir/fatofa/کاروان/\", \"https://abadis.ir/fatofa/کارزار/\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1575\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' printed p.1575 = BQT_v3_pages.txt pdf page 368. The page has 'کالجار ... بلغت گیلکی بروزن و معنی کارزار است که جنگ و جدال باشد' and Mo'in's footnote 6: 'کالیجار = کالنجار ... «کالنجار» را از اصل «کالجار» گیلکی و kārēčār پهلوی و کارزار فارسی و kalinjarai سانسکریت بمعنی جنگ و حرب گرفته. (رک: کارزار)'. Exactly Nourai's kâlenjâr 'fight' under the war-kār.\"},\n   {\"ref\": \"HRN:237\", \"status\": \"not_found\",\n    \"note\": \"HRN.txt leaf 259 carries the printed '— 237 —' and contains nos. 1059-1061 (nihuften, nei, ne) — nothing about kār. The passage Nourai wants is Horn no. 834, pp.185-186: 'kār[e]zār ‚Kampf, Schlachtfeld‘ ... phlv. kārečar ... vergl. ap. kāra- ‚Heer‘; lit. kāras ‚Krieg‘; ksl. kara ‚Zank, Streit‘; got. harjis ‚Heer‘. ... Fr. Müller (WZKM. 5, 354) will dasselbe kār in np. karwān ‚Karawane‘ finden; Nöldeke (mündliche Mitteilung) stellt hierher np. kārdār ‚Vezir‘.' The claim is Horn's, the page number is not.\"},\n   {\"ref\": \"MON:2957\", \"status\": \"not_checked\",\n    \"note\": \"The six-volume Amir Kabir Farhang-e Farsi is not online and its pagination cannot be mapped (refs_online.json MON). Content checked instead on vajehyab/abadis: Mo'in s.v. کاروان gives '[په.] (اِمر.) قافله، عده‌ای مسافر...' (Pahlavi tag, no Latin etymon shown online).\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. kārēčār\", \"stance\": \"supports\",\n    \"note\": \"'kārēčār [kʻlycʻl] battle, combat ... — MPrs krycʻr, krʻcʻr (S); Paz. kārīžār, NP kārzār; kārē- cas. obl. of kār < OP kāra- ‘army’, + čār from Av. kar- ‘to move’'. Explicit MP link OP kāra- > kār 'army'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.48-49 s.v. 2kār, kārawān, kārēzār\", \"stance\": \"supports\",\n    \"note\": \"'2kār [kʾI], pl. -ān: (other) people'; 'kārawān [kʾIwʾII | P kʾrwʾn, N kārwān] caravan, military column'; 'kārēzār [kʾIycʾ | M kʾrycr, N kārzār] battle(-field)'. The gloss 'military column' for kārawān is the strongest independent support for Nourai's kār-vān 'army, caravan'.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan p.1560 (pdf 353), Mo'in's footnote 2 to کارزار\", \"stance\": \"supports\",\n    \"note\": \"'پهلوی kārēčār مرکب از: کار بمعنی جنگ (قس: پارسی باستان kāra (سپاه)؛ لیتوانی karas (جنگ)، گتی harjis (سپاه)) + زار ... قس: کاروان «هوبشمان» ... بارتولمه ستون ۱۲۱۵'. Mo'in cross-refers kārzār to kārwān.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 834, pp.185-186\", \"stance\": \"supports\",\n    \"note\": \"Contains the whole of Nourai's Persian box: kārzār, and 'Fr. Müller ... will dasselbe kār in np. karwān ‚Karawane‘ finden; Nöldeke ... stellt hierher np. kārdār ‚Vezir‘.'\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur p.396 (ARY_pages.txt pdf 395) s.v. کار\", \"stance\": \"supports\",\n    \"note\": \"Headword 'کار (به چم «ارتش» و «جنگ») کارزار' with Avestan/OP/Pahlavi/Gothic HARJIS/OE HERE cognates; note 2: 'در فارسی واژهٔ کارزار یعنی محل نبرد: کار = نبرد و جنگ، زار = محل (مانند گلزار)'; note 3 adds that in modern Persian the word means 'deed, craft'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein p.238 s.v. caravan\", \"stance\": \"contradicts\",\n    \"note\": \"'caravan, n. F. caravane, fr. Pers. karwan, ‘company of travelers, caravan’, which is rel. to OI. karabháḥ, ‘camel, young camel, young elephant’.' Klein does NOT connect kārwān with kār 'army'.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1075, p.88\", \"stance\": \"contradicts\",\n    \"note\": \"'1075. Sskr. karabha: ‚Kamel‘ ... hieraus wahrscheinlich pers. kārwān oder kāriwān ‚Kamelzug, Reisegesellschaft‘' — same camel etymology; Lokotsch nonetheless cites 'FR. MÜLLER in WZKM V, 354', the very paper Horn quotes for the kār 'army' analysis.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in / Dehkhoda s.v. کارزار (abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"Dehkhoda: kār 'war/combat' + zār (place suffix), 'place of warfare', from Pahlavi kārēčār; Mo'in s.v. کاروان tags it [په.] and abadis quotes Kazzazi: کاره (OP 'army') + وان.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"French\", \"words\": \"caravane\", \"verdict\": \"plausible\",\n \"derivation\": (\"French caravane does come from Persian kārwān, but not directly as the chart's single arrow \"\n   \"suggests. Etymonline: Old French carvane, carevane (13c.) and Medieval Latin caravana are Crusade-era \"\n   \"borrowings that reached Romance through Arabic qayrawān (Wiktionary lists قَيْرَوَان among the descendants \"\n   \"of MP kārawān) and Italian carovana/caravana, the word of the Levant trade; the modern French form \"\n   \"caravane replaced carvane in the 16th c. Klein's p.238 entry, which Nourai cites, likewise gives only \"\n   \"'F. caravane, fr. Pers. karwan'. So the endpoint is right and the direction is right; the omitted \"\n   \"Arabic and Italian relay is what keeps this from 'confirmed'.\"),\n \"derivation_fa\": (\"فرانسوی caravane در نهایت از فارسی «کاروان» است، امّا نه بی‌واسطه: نخست از راه معرّب آن قَیْرَوَان و \"\n   \"سپس ایتالیایی carovana/caravana در دوران جنگ‌های صلیبی به فرانسوی کهن به صورت carvane/carevane \"\n   \"(سدهٔ ۱۳ م.) راه یافت و در سدهٔ ۱۶ به caravane دگرگون شد. کلاین (ص ۲۳۸) نیز همین را می‌گوید. ادعای نورایی \"\n   \"درست است، ولی حلقهٔ عربی و ایتالیایی از نمودار افتاده است.\"),\n \"sources\": [\"https://www.etymonline.com/word/caravan\", W+\"کاروان\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:238\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 137 (page numbers '238'/'239' printed on the leaf): 'caravan, n. F. caravane, fr. Pers. karwan, ‘company of travelers, caravan’, which is rel. to OI. karabháḥ, ‘camel...’.' Page number exactly right for the French-from-Persian claim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale, s.v. Caravane\", \"stance\": \"supports\",\n    \"note\": \"'Caravane. Du persan کاروان karwān, même sens.' (and 'Caravansérail. En persan karwān-serâï, hôtel de la caravane').\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. Caravan\", \"stance\": \"supports\",\n    \"note\": \"'Caravan. (F.-Pers.) F. caravane. Pers. karwan, a caravan, convoy.'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1075\", \"stance\": \"partial\",\n    \"note\": \"Lists 'frz. caravane' among the European reflexes of pers. kārwān, but routes the word out of Skt. karabha 'camel' rather than out of kāra 'army'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"caravan, van\", \"verdict\": \"confirmed\",\n \"derivation\": (\"English caravan is first recorded in the 1590s in the sense 'company of travellers going \"\n   \"together for security', taken straight from French caravane (Etymonline); the sense 'large covered \"\n   \"carriage' follows in the 1670s and 'house on wheels' in the 19th c. Van is the clipped form: \"\n   \"Etymonline dates 'covered truck or wagon' to 1829, 'shortened of caravan', and Hobson-Jobson \"\n   \"(p.161-162, s.v. CARAVAN) already notes 'The abbreviation van in this sense seems to have acquired \"\n   \"rights as an English word, though the altogether analogous bus is still looked on as slang.' Note \"\n   \"that van 'winnowing fan' (Klein) is a different, Latin word (vannus) — Nourai plainly means the \"\n   \"vehicle.\"),\n \"derivation_fa\": (\"انگلیسی caravan از دههٔ ۱۵۹۰ م. مستقیماً از فرانسوی caravane گرفته شده و نخست «قافله» معنا می‌داد؛ \"\n   \"سپس در سدهٔ ۱۷ به «کالسکهٔ سرپوشیده» و در سدهٔ ۱۹ به «خانهٔ چرخدار» تحول معنایی یافت. van کوتاه‌شدهٔ همین واژه \"\n   \"است (از ۱۸۲۹ م.)؛ یول و برنل در هابسن‌جابسن نیز همین را گفته‌اند. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/caravan\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The node carries no reference of its own in the book; the chain is covered by the parent's KLN:238.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson pp.161-162 s.v. CARAVAN\", \"stance\": \"supports\",\n    \"note\": \"'CARAVAN, s. P. karwān; a convoy of travellers... The word is found in French as early as the 13th century (Littré). A quotation below shows that the English transfer of the word to a wheeled conveyance... dates from the 17th century. The abbreviation van in this sense seems to have acquired rights as an English word.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein p.238 (caravan) and p.1768 (van)\", \"stance\": \"partial\",\n    \"note\": \"Klein has 'caravan ... F. caravane, fr. Pers. karwan' but his headword 'van, n., a winnowing fan. — ME., fr. OF. van, fr. L. vannus' is the homonym, not the vehicle; the vehicle-van is the clipping of caravan (Etymonline, Hobson-Jobson).\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Germanic\", \"words\": \"harjaz, hari; harjon; harja-waldaz; harja-bergaz\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Proto-Germanic *harjaz 'army' is *koryos with Grimm's law (*k > *h) and the regular Germanic \"\n   \"loss of the *-y- before the nominative ending: Goth. harjis, ON herr, OE here, OHG/OS heri 'Heer, Menge' \"\n   \"(hence Nourai's second form hari). *harjōną is the denominative verb 'to make war on, ravage' > OE \"\n   \"hergian > NE harry. The two compounds are exactly Watkins's: *harja-waldaz 'army commander' (*wald- \"\n   \"'rule, power') > ON Haraldr, OE Hereweald, Anglo-Norman herald; *harja-bergaz 'army-hill, hill-fort', \"\n   \"later 'shelter, lodging, quarters' > OE herebeorg > ME herberwe > harbor, OF herberge > harbinger. \"\n   \"One caveat on the cross-reference ☞ Bherg: Watkins 1985 does file *harja-bergaz under bhergh-2 'high; \"\n   \"hill', which is Nourai's Bherg, but Etymonline and Kroonen analyse the second member as *burzjan- \"\n   \"'protection, shelter' from bhergh-1 'to hide, protect'; Aryanpur's note 1 on p.396 likewise reports that \"\n   \"'most scholars today' no longer take harbour/auberge from this root. The Germanic forms themselves are \"\n   \"not in doubt.\"),\n \"derivation_fa\": (\"ژرمنی آغازین *harjaz «سپاه» همان *koryos است پس از قانون گریم (k > h): گوتی harjis، نروژی کهن herr، \"\n   \"انگلیسی کهن here، آلمانی علیای کهن heri (= صورت hari در جدول). *harjōną فعل اسمی «تاختن، غارت \"\n   \"کردن» است که به harry انگلیسی رسیده. دو ترکیب *harja-waldaz «فرماندهٔ سپاه» و *harja-bergaz «تپهٔ سپاه، سپس \"\n   \"پناهگاه» عیناً در واتکینز (پیوست ریشه‌های هندواروپایی AHD) آمده‌اند. تنها نکته آنکه بخش دوم harja-bergaz را \"\n   \"امروزه بیشتر از *bhergh- «پناه دادن» می‌گیرند نه از *bhergh- «بلند، تپه». ادعای نورایی درست است.\"),\n \"sources\": [W+\"Reconstruction:Proto-Germanic/harjaz\", \"https://www.etymonline.com/word/harbor\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. koro-: 'I. Germanic *harjaz, army. 1. Old English here... 3. Compound *harja-bergaz, “army hill,” hill-fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-2)... HARBOR... 4. Compound *harja-waldaz, “army commander” (*wald-, rule, power; see wal-)... HERALD. II. Germanic denominative *harjōn in Old English hergian, to ravage, plunder, raid: HARRY.' All four of Nourai's Germanic forms, with the Bherg cross-reference.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 615\", \"stance\": \"supports\",\n    \"note\": \"'got. harjis, aisl. herr, ags. here ‚Heer‘, ahd. as. heri ‚Heer, Menge‘, PN altgerm. Hari-gasti (Dat.)'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein p.706 s.v. harry\", \"stance\": \"supports\",\n    \"note\": \"'harry ... fr. OE. hergian, ‘to ravage, lay waste’ ... denominated fr. OE. here, resp. ON. herr ... OHG. hari, heri ... Goth. harjis ... cogn. with Lith. karas ... OPers. kara, ‘host, army’.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 20.15 ARMY p.1377\", \"stance\": \"supports\",\n    \"note\": \"Goth. harjis / ON herr / OE here / OHG heri all tabulated as the Germanic words for 'army'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.462\", \"stance\": \"supports\",\n    \"note\": \"'got. harjis, aisl. herr, ags. here „Heer“, ahd. as. heri „Heer, Menge“' under qor-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"Oliver, Herbert, Herman, Walter; Harry; Harold; harbor\", \"verdict\": \"disputed\",\n \"derivation\": (\"Nourai's list reproduces Klein's own list at the end of s.v. harry ('Cp. also the first element \"\n   \"in arrière-ban, harbinger, harbor, harness, Harold, herald, Herbert, heretoga, heriot, Herman, hership, \"\n   \"and the second element in Lothario, Oliver, Walter'), and most of it holds. Herbert = OHG Heribert, \"\n   \"PGmc *harja-berhtaz 'army-bright'; Herman = OHG Hariman, *harja-mann- 'army-man'; Walter = OHG Walthari, \"\n   \"*wald-harjaz 'rule-army' (the same two elements as Harold in the other order); Harold = ON Haraldr / OE \"\n   \"Hereweald < *harja-waldaz 'army commander' (Etymonline s.v. Harold); harbor < OE herebeorg 'lodgings, \"\n   \"quarters' < *harja-bergaz. Oliver is weaker: Klein files it under -hari, but its origin is genuinely \"\n   \"unsettled (OF Olivier, either a Germanic *Alfihari / ON Ólāfr latinised, or Latin oliva). The clear \"\n   \"error is Harry. Klein's very next headword reads 'Harry, masc. PN. — F. Henri. See Henry', and \"\n   \"Etymonline agrees: 'Harry, masc. proper name, a familiar form of Henry', i.e. Germanic *Haimirīk \"\n   \"'home-ruler', which has nothing to do with *harjaz. Nourai, listing Harry among the personal names on \"\n   \"its own line, has taken the wrong one of Klein's two adjacent headwords. (The verb to harry, from \"\n   \"*harjōną, would of course belong here — but the chart's capitalised Harry sits in a list of names.)\"),\n \"derivation_fa\": (\"فهرست نورایی همان فهرست کلاین ذیل harry است و بیشتر آن درست است: Herbert از *harja-berhtaz \"\n   \"«درخشان‌سپاه»، Herman از *harja-mann-، Walter از *wald-harjaz و Harold از *harja-waldaz (دو جزء وارونه)، و harbor \"\n   \"از انگلیسی کهن herebeorg «اتراقگاه سپاه». ولی Harry از این ریشه نیست: خود کلاین در مدخل بعدی می‌نویسد \"\n   \"«Harry از فرانسوی Henri» و اتیموآنلاین نیز آن را گونهٔ خودمانی Henry (< ژرمنی *Haimirīk «فرمانروای \"\n   \"خانه») می‌داند. Oliver نیز محل اختلاف است (یا ژرمنی *Alfihari یا لاتین oliva). پس پژوهش امروزی دربارهٔ \"\n   \"Harry ادعای نورایی را رد می‌کند.\"),\n \"sources\": [\"https://www.etymonline.com/word/Harry\", \"https://www.etymonline.com/word/Harold\",\n             \"https://www.etymonline.com/word/harbor\", W+\"Reconstruction:Proto-Germanic/harjaz\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"No reference printed on this node; the parent Germanic box cites AHD, whose koro- entry covers HARBOR, HARRY (verb), HERALD but none of the personal names.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p.706 s.v. harry, and the immediately following entry 'Harry, masc. PN.'\", \"stance\": \"partial\",\n    \"note\": \"Klein supplies Nourai's whole list ('...Harold, herald, Herbert, ... Herman, ... and the second element in Lothario, Oliver, Walter'), but the next headword reads 'Harry, masc. PN. — F. Henri. See Henry' — so Klein himself excludes the name Harry.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. koro-\", \"stance\": \"partial\",\n    \"note\": \"Lists only HARBOR, HARBINGER, HARANGUE, HARRY (the verb), HERIOT, HERALD, ARRIERE-BAN under koro-; the personal names are not in Watkins's index.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur p.396, note 1\", \"stance\": \"contradicts\",\n    \"note\": \"'امروزه بیشتر دانشمندان معتقدند که واژه‌های انگلیسی harbo(u)r و فرانسهٔ auberge از این واج‌ریشه مشتق نشده‌اند' — a minority caveat against putting harbor here at all.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Indo-European\", \"words\": \"koruos\", \"verdict\": \"unverified\",\n \"derivation\": (\"This box is Mann IEC 538 verbatim: 'koruos (2) ‘bitter, harsh’. Ambig. Cf. koruos (1)'. No other \"\n   \"reference work on the shelf reconstructs such a root: it is absent from Pokorny (whose kor- entries at \"\n   \"615-616 are koro-s 'war', kormo- 'Qual, Schmerz, Schmach', kormno- 'Lauge, Harn', kos(e)lo- 'hazel'), from \"\n   \"Walde-Pokorny Bd. I, from Watkins/AHD, and from Wiktionary, which takes German herb no further back than \"\n   \"Proto-West-Germanic *haru. Mann himself flags it 'Ambig.' and warns that the neighbouring Germanic \"\n   \"'harrow' words are only isophonic. So: not refuted, but unsupported outside Mann — and note that Nourai \"\n   \"hangs it under the war-root Koro, whereas Mann keeps koruos (2) two lemmas away from korios (1) and does \"\n   \"not connect them.\"),\n \"derivation_fa\": (\"این جعبه عیناً از مدخل koruos (2) در فرهنگ تطبیقی من (ص ۵۳۸) گرفته شده است که خود من آن را \"\n   \"«Ambig.» (مشکوک) خوانده است. هیچ مرجع دیگری — نه پوکورنی، نه والده–پوکورنی، نه واتکینز، نه ویکی‌واژه — \"\n   \"ریشه‌ای هندواروپایی به معنای «تلخ، گس» با این صورت بازسازی نمی‌کند. افزون بر این، من این مدخل را به ریشهٔ \"\n   \"«سپاه/جنگ» پیوند نمی‌زند؛ این پیوند کار نورایی است. بنابراین منبع مستقلی برای تأیید یا رد آن یافت نشد.\"),\n \"sources\": [W+\"herb\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:538\", \"status\": \"supports\",\n    \"note\": \"IEC.txt leaf 307 (page numbers '539'/'540' printed further down the leaf, so this column is p.538): 'koruos (2) ‘bitter, harsh’. Ambig. Cf. koruos (1) Per. karb ‘sad’; Ir. cf. corbaim ... MHG hare, gs harwer; here, gs herwes ‘sharp, bitter, tart’; It. LW fr. Gmc. garbo ‘bitter’...'. Nourai's box, and nodes 8-10, are this entry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 615-616 (POK_02 leaf 276)\", \"stance\": \"silent\",\n    \"note\": \"The kor- run at 615-616 has kormen-, kormo- „Qual, Schmerz, Schmach‘, kormno-, koro-s, kos(e)lo- — no *koru- 'bitter'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I pp.462-463\", \"stance\": \"silent\",\n    \"note\": \"The qor-/kor- run (kor- „Reiserbesen‘, qor- „Kriegsheer‘, korka, kormno-) has no 'bitter' root.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, root list\", \"stance\": \"silent\",\n    \"note\": \"No koru-/koruos root; the nearest entries are koro- 'war' and kormo- 'pain'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"karb «کرب»\", \"verdict\": \"disputed\",\n \"derivation\": (\"Persian کرب karb 'grief, anguish' is an Arabic loan, not an Iranian inheritance. Mo'in's own \"\n   \"dictionary tags it '[ع.]' (Arabic) and glosses 'اضطراب، وحشت، اندوه، ج: کروب'; Dehkhoda has '[ع اِ] اندوه \"\n   \"دم‌گیر، ج: کُروب'. The word is Arabic کَرْب karb, verbal noun of کَرَب karaba 'to distress, oppress' \"\n   \"(root k-r-b), well established in Qur'anic and classical Arabic and the source of the plural کروب and \"\n   \"of کربلا folk-etymologies; it entered Persian as an ordinary literary Arabism. The only support \"\n   \"Nourai has is Mann's bare 'Per. karb ‘sad’' inside the doubtful koruos (2) lemma. Wiktionary's Persian \"\n   \"کرب is a different word entirely ('field maple', borrowed from Mazanderani). The chart's own NOTE \"\n   \"records Mo'in's Arabic verdict, and modern scholarship sides with Mo'in.\"),\n \"derivation_fa\": (\"«کرب» در فارسی معرّب نیست بلکه وام‌واژه‌ای عربی است: معین آن را با نشانهٔ [ع.] می‌آورد و \"\n   \"«اضطراب، وحشت، اندوه، ج: کروب» معنا می‌کند؛ دهخدا نیز «[ع اِ] اندوه دم‌گیر». اصل آن مصدر عربی کَرْب از \"\n   \"ریشهٔ ک–ر–ب است. تنها دستاویز نورایی یک اشارهٔ کوتاه در مدخل مشکوک koruos (2) در فرهنگ من است. \"\n   \"پژوهش امروزی ادعای نورایی را رد می‌کند و همان دیدگاه معین (عربی بودن) را می‌پذیرد؛ خود یادداشت جدول نیز \"\n   \"به این نکته اشاره دارد.\"),\n \"sources\": [W+\"كرب\", W+\"کرب\", \"https://abadis.ir/fatofa/کرب/\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:538\", \"status\": \"supports\",\n    \"note\": \"Mann p.538 koruos (2) does list 'Per. karb ‘sad’' as its first witness — so Nourai reports his source correctly; the source itself is the weak link.\"},\n   {\"ref\": \"MON:2932\", \"status\": \"partial\",\n    \"note\": \"Cited by Nourai in the node's own NOTE. The 6-vol Mo'in cannot be paged online, but Mo'in's text is verifiable on vajehyab/abadis and reads '[ع.] اضطراب، وحشت، اندوه. ج. کروب' — the Arabic tag Nourai reports is there.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. کرب (abadis.ir)\", \"stance\": \"contradicts\",\n    \"note\": \"'[ع.] اضطراب، وحشت، اندوه. ج. کروب' — Arabic, not Iranian.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Persian IE-roots dictionary\", \"stance\": \"silent\",\n    \"note\": \"No کرب headword in ARY_pages.txt; Aryanpur claims no Indo-European root for it.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n    \"note\": \"grep 'karb' in PLA_asbaghi_1988_ia_djvu.txt returns only karbās / karbādgan entries — Asbaghi does not treat karb 'grief' as a Persian word borrowed into Arabic, which is what a genuine Iranian origin would predict.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\",\n    \"note\": \"grep 'karb' finds nothing — Jeffery does not list Qur'anic karb among the foreign words, i.e. he treats it as native Arabic.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Germanic\", \"words\": \"hare, harwer, herwes\", \"verdict\": \"plausible\",\n \"derivation\": (\"The forms are real Middle High German: the adjective 'bitter, tart, sharp' is MHG hare / here \"\n   \"with inflected stem harwe- / herwe- (Mann cites the genitives harwer, herwes), whence modern German herb. \"\n   \"Wiktionary takes it back to OHG *haro and Proto-West-Germanic *haru, and there stops — no Indo-European \"\n   \"etymology is offered, and none of Pokorny, Walde-Pokorny or Watkins provides one. So the Germanic side of \"\n   \"Nourai's koruos branch is well attested as a word family, but its attachment to any PIE *koru- (let alone \"\n   \"to the war-root Koro) rests on Mann alone; Mann himself adds that 'G herb is of twofold origin'. Nourai's \"\n   \"spelling 'harwer, herwes' copies Mann's genitive citation forms rather than nominatives, which is why \"\n   \"they look odd as headwords — that is faithful to the source, not a misprint.\"),\n \"derivation_fa\": (\"این صورت‌ها واقعی‌اند: آلمانی علیای میانه hare / here «تلخ، گس» با ستاک صرفی harwe-/herwe- \"\n   \"(صورت‌های harwer و herwes در جدول همان حالت ملکی اند که من نقل کرده) که به herb آلمانی نو رسیده است. \"\n   \"ویکی‌واژه آن را تا آلمانی علیای کهن *haro و ژرمنی غربی آغازین *haru پی می‌گیرد و فراتر نمی‌رود؛ \"\n   \"پیوند آن به ریشهٔ *koruos تنها بر رأی من استوار است. پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [W+\"herb\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:538\", \"status\": \"supports\",\n    \"note\": \"'MHG hare, gs harwer; here, gs herwes ‘sharp, bitter, tart’' — Nourai's three forms verbatim from Mann p.538.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 615-616 and the ker-/kor- runs\", \"stance\": \"silent\",\n    \"note\": \"Pokorny nowhere connects MHG hare/herwe with an IE root; the word is absent from his kor- entries.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I pp.462-463\", \"stance\": \"silent\",\n    \"note\": \"No entry for the MHG 'bitter' adjective under kor-/qor-.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\",\n    \"note\": \"No root supplied for German herb.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Italian\", \"words\": \"garbo\", \"verdict\": \"plausible\",\n \"derivation\": (\"Italian garbo in the sense 'tart, sourish (of wine)' does exist — Treccani's garbo entry records \"\n   \"an 'ant.' (archaic) sense referring to the flavour of wine, beside the living sense 'grace, elegance, \"\n   \"courtesy'. But Nourai's arrow, taken from Mann ('It. LW fr. Gmc. garbo ‘bitter’'), makes it a loan of the \"\n   \"MHG harwe- word, with Germanic h- rendered as Italian g-, which is the normal treatment of Germanic w-/h- \"\n   \"in Lombardic loans but is not what the Italian dictionaries say. Treccani derives garbo 'prob. dall'arabo \"\n   \"qālib «modello»', and Wiktionary offers Old High German garwi 'dress, equipment, preparation' (PGmc \"\n   \"*garwijaną, whence also English garb), with the Arabic qālib route as the alternative. Neither mentions a \"\n   \"Germanic 'bitter' etymon. So the word and the sense are real, the Germanic source is defensible for the \"\n   \"wine sense, but the standard reference works route garbo elsewhere.\"),\n \"derivation_fa\": (\"ایتالیایی garbo در معنای «ترش‌مزه (دربارهٔ شراب)» در ترکانی همچون معنای کهن ضبط شده، ولی \"\n   \"فرهنگ‌های معتبر ریشهٔ دیگری برای آن می‌دهند: ترکانی «احتمالاً از عربی قالب» و ویکی‌واژه از آلمانی \"\n   \"علیای کهن garwi «سازوبرگ، آماده‌سازی» (هم‌ریشهٔ garb انگلیسی). وام‌گیری از ژرمنی *harwa «تلخ» با بدل \"\n   \"h > g (مانند وام‌واژه‌های لمباردی) از نظر آوایی ممکن است ولی در فرهنگ‌های امروزی پذیرفته نیست؛ \"\n   \"پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [W+\"garbo\", \"https://www.treccani.it/vocabolario/garbo3/\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:538\", \"status\": \"supports\",\n    \"note\": \"Mann p.538, koruos (2): 'It. LW fr. Gmc. garbo ‘bitter’' — exactly the arrow Germanic > Italian that Nourai draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. garb\", \"stance\": \"partial\",\n    \"note\": \"Klein routes English garb through F. galbe / It. garbo from Germanic *garwi 'preparation, equipment' — a Germanic source, but a different one from Mann's 'bitter' word.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs\", \"stance\": \"silent\",\n    \"note\": \"grep for garbo in LKT.txt finds no entry — Lokotsch does not treat it as an orientalism, which leaves Treccani's Arabic qālib route unconfirmed on this shelf too.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\",\n    \"note\": \"No Indo-European root supplied for garbo in either sense.\"}\n ]\n})\n\nroot[\"nodes\"] = nodes\nout = {\n \"pdf_page\": 274,\n \"book_page\": 244,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [root]\n}\nwith io.open(\"data/verification/page-274.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk274.py && python3 -m json.tool data/verification/page-274.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 274"
}
```


### [2026-09-06T21:31:31.361Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 10/10
node verdicts: {'confirmed': 3, 'plausible': 4, 'disputed': 2, 'unverified': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 9, 'not_found': 1, 'not_checked': 3, 'partial': 1}
books consulted: {'supports': 17, 'contradicts': 4, 'partial': 5, 'silent': 11} | by book: {'KLN': 5, 'WLD': 4, 'AHD': 4, 'ARY': 3, 'LKT': 3, 'POK': 3, 'SYN': 2, 'MON': 2, 'KNT': 1, 'IEC': 1, 'NYB': 1, 'PHD': 1, 'BQT': 1, 'HRN': 1, 'DEV': 1, 'SKT': 1, 'HJB': 1, 'PLA': 1, 'FVQ': 1}
```


## [2026-09-06T21:31:40.429Z] TOOL CALL #74: Bash

```json
{
 "command": "head -c 200 data/verification/page-274.json && echo && python3 -c \"\nimport json;d=json.load(open('data/verification/page-274.json'))\ne=d['entries'][0]\nprint(e['verdict'], len(e['nodes']))\nfor n in e['nodes']: print(n['id'], n['verdict'], bool(n.get('derivation_fa')), len(n.get('consulted',[])), len(n.get('ref_check',[])))\nprint('note_fa', bool(e.get('note_fa')))\n\""
}
```


### [2026-09-06T21:31:42.809Z] TOOL RESULT

```
{
  "pdf_page": 274,
  "book_page": 244,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-06",
  "entries": [
    {
      "entry": 0,
      "root": "Koro / Koros",
      "verdict": "plausib
plausible 10
1 confirmed True 4 2
2 plausible True 8 3
3 plausible True 3 1
4 confirmed True 2 1
5 confirmed True 4 1
6 disputed True 3 1
7 unverified True 3 1
8 disputed True 4 2
9 plausible True 3 1
10 plausible True 3 1
note_fa True
```


## [2026-09-06T21:32:03.584Z] AGENT

Page 274 (book p. 244) verified. `verify_check.py 274` → 10/10 nodes, **0 PROBLEM lines**.

**Verdicts** — root: 1 plausible. Nodes: 3 confirmed (#1 OP kāra-, #4 Eng. caravan/van, #5 Gmc *harjaz), 4 plausible (#2 Persian, #3 Fr. caravane, #9 MHG hare/herwe, #10 It. garbo), 2 disputed, 1 unverified.

**Disputed / weak items**
- Root *Koro/Koros* (plausible, not confirmed): "Koro: war, army" is solid (POK 615-616 `koro-s, korio-s ‚Krieg, Kriegsheer‘`; WP I 462; Watkins koro-; Buck 20.15). But the second gloss "Koros: fighting, bullying, arrogance" is copied from Mann IEC 536 `koros (2)`, a *separate* lemma Mann himself calls ambiguous; its Greek witness κόρος 'insolence' belongs to PIE *ḱer- 'to grow' (Pokorny 577). The merge is Nourai's.
- **#6 English, "Harry"** (disputed): Nourai's list is Klein's list under *harry*, but Klein's very next headword reads "Harry, masc. PN. — F. Henri. See Henry"; Etymonline agrees. Harry (the name) is from Henry < *Haimirīk, not *harjaz. Oliver is also unsettled. Herbert/Herman/Walter/Harold/harbor are fine.
- **#8 Persian karb «کرب» 'sorrow'** (disputed): an Arabic loan (كَرْب, root k-r-b). Mo'in tags it `[ع.]`, Dehkhoda `[ع اِ]` — as the chart's own NOTE concedes. Only Mann supports the IE derivation.
- **#7 IE koruos 'bitter, harsh'** (unverified): exists only in Mann IEC 538, who flags it "Ambig."; silent in Pokorny, Walde-Pokorny, Watkins and Wiktionary (German *herb* stops at PWGmc *haru).

**Nourai's own citations**
- POK:615, KNT:175, KLN:238, IEC:536, IEC:538, BQT:1575, AHD all check out. KNT:175 is exactly the `ukāra-` page; BQT:1575 is exactly Mo'in's کالنجار footnote deriving it from Gilaki kālčār / Pahlavi kārēčār / کارزار.
- **HRN:237 is a wrong page number** (`not_found`): Horn p.237 has nos. 1059-1061 (nihuften, nei, ne). The passage Nourai needs — kārzār < ap. kāra- 'Heer', plus Fr. Müller on *karwān* and Nöldeke on *kārdār* — is Horn no. 834, pp. 185-186.
- MON:2957 / MON:2932 `not_checked` (6-vol Amir Kabir pagination not mappable); content verified on vajehyab/abadis instead.

**Extraction issues for the owner** — none serious; the JSON is faithful to the printed page. One nuance: the page prints the parenthetical scripts inline with their words — «کار ۲ (کارزار)» and «کالنجار (کلنجار)» — but the extraction dropped both into a page-level `script_extra` field, so کارزار (the best-attested reflex of the war-*kār*, and the form all the sources actually discuss) is detached from the `kâr-` word it belongs to.

16 web sources archived via `fetch_source.py`.
