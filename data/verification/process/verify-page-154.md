# Verification process log — verify-page-154


## [2026-09-05T20:27:02.925Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 154 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-154.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-154.json. Write /home/sfmqrb/git/rishe/data/verification/page-154.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 154` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:27:04.723Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:27:05.431Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:27:05.449Z] TOOL RESULT

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


## [2026-09-05T20:27:05.750Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-154.txt"
}
```


### [2026-09-05T20:27:05.766Z] TOOL RESULT

```
1	=== PDF page 154 (book page 124) ===
2	--- entry 0 ---
3	ROOT [Indo-European] En; Ndher, Ndhos, Ndhi : in, inside; in, under  (refs POK:311)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:311; DZA:57 | an-tar, an-tare, antara : among, in
5	  #2 (parent #1) [Persian] refs=HRN:27; BRT:132 | andar «اندر ۱» : inside | extra: اندران ، اندرون
6	#3 (parent #0) [Avestan] refs=KLN:1677 | hača-adairi : from under ☞Sekw
7	  #4 (parent #3) [Pahlavi] refs=None | azîr, azěr : under
8	    #5 (parent #4) [Persian] refs=BQT:1051 | zîr «زیر» : under
9	#6 (parent #0) [Old Persian] refs=POK:311 | adi, adyi : in ; adi-sta : in standing ☞Stâ ; adi-var : in truth, indeed ☞Wel 1
10	  #7 (parent #6) [Pahlavi] refs=HRN:6,20 | ô-statan : to be in standing ; ě-var : indeed ; ě-vâr : ? ; ě-vân : ?
11	    #8 (parent #7) [Persian] refs=HRN | îstâdan «ایستادن» : to stand ; ârî «آری» : yes, indeed
12	#9 (parent #0) [Greek] refs=AHD | en-, eis- : in, inside ; para-en-tithenai : put in besides ☞Dhě 2 ; epi-eis-hodos : coming in besides ☞Sed
13	  #10 (parent #9) [French] refs=None | paranthese
14	    #11 (parent #10) [Persian] refs=MON:652 | parântez «پرانتز» : parenthesis
15	  #12 (parent #9) [English] refs=None | parenthesis, episode
16	#13 (parent #0) [Germanic] refs=AHD | in, innera, anda
17	  #14 (parent #13) [English] refs=None | in, and, under
18	#15 (parent #0) [Latin] refs=AHD | intrô, intrâ, inter
19	  #16 (parent #15) [English] refs=None | inter-, international, interest, interface, intestine, intimate, in- 1, en-, inferior
20	--- entry 1 ---
21	ROOT Enek -> redirect to Neku
22	--- entry 2 ---
23	ROOT Enk -> redirect to Neku
24	--- entry 3 ---
25	ROOT Eno -> redirect to An 2
26	--- entry 4 ---
27	ROOT Enomn -> redirect to Nomn
28	
```


## [2026-09-05T20:27:09.355Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-154.json",
 "description": "Read source JSON for page 154"
}
```


### [2026-09-05T20:27:09.394Z] TOOL RESULT

```
{
  "pdf_page": 154,
  "book_page": 124,
  "entries": [
    {
      "root": {
        "name": "En; Ndher, Ndhos, Ndhi",
        "lang": "Indo-European",
        "refs": "POK:311",
        "gloss": "in, inside; in, under"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:311; DZA:57",
          "words": [
            {"translit": "an-tar, an-tare, antara", "gloss": "among, in", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:27; BRT:132",
          "words": [
            {"translit": "andar", "gloss": "inside", "script": "اندر ۱"}
          ],
          "script_extra": "اندران ، اندرون",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:1677",
          "words": [
            {"translit": "hača-adairi", "gloss": "from under", "script": null, "see": ["Sekw"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "azîr, azěr", "gloss": "under", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:1051",
          "words": [
            {"translit": "zîr", "gloss": "under", "script": "زیر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:311",
          "words": [
            {"translit": "adi, adyi", "gloss": "in", "script": null},
            {"translit": "adi-sta", "gloss": "in standing", "script": null, "see": ["Stâ"]},
            {"translit": "adi-var", "gloss": "in truth, indeed", "script": null, "see": ["Wel 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Pahlavi",
          "refs": "HRN:6,20",
          "words": [
            {"translit": "ô-statan", "gloss": "to be in standing", "script": null},
            {"translit": "ě-var", "gloss": "indeed", "script": null},
            {"translit": "ě-vâr", "gloss": "?", "script": null},
            {"translit": "ě-vân", "gloss": "?", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "HRN",
          "words": [
            {"translit": "îstâdan", "gloss": "to stand", "script": "ایستادن"},
            {"translit": "ârî", "gloss": "yes, indeed", "script": "آری"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "en-, eis-", "gloss": "in, inside", "script": null},
            {"translit": "para-en-tithenai", "gloss": "put in besides", "script": null, "see": ["Dhě 2"]},
            {"translit": "epi-eis-hodos", "gloss": "coming in besides", "script": null, "see": ["Sed"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "paranthese", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:652",
          "words": [
            {"translit": "parântez", "gloss": "parenthesis", "script": "پرانتز"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "parenthesis, episode", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "in, innera, anda", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "in, and, under", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "intrô, intrâ, inter", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "inter-, international, interest, interface, intestine, intimate, in- 1, en-, inferior", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Enek", "redirect": "Neku"},
      "nodes": []
    },
    {
      "root": {"name": "Enk", "redirect": "Neku"},
      "nodes": []
    },
    {
      "root": {"name": "Eno", "redirect": "An 2"},
      "nodes": []
    },
    {
      "root": {"name": "Enomn", "redirect": "Nomn"},
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:27:10.155Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:27:10.197Z] TOOL RESULT

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


## [2026-09-05T20:27:15.264Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','DZA','HRN','BRT','KLN','BQT','MON','AHD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900]); print()\n\""
}
```


## [2026-09-05T20:27:15.444Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 data/verification/page-124.json; echo; echo ---; sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-05T20:27:16.908Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

DZA {"title": "M.T. Rashed Mohassel, Daramadi bar Dastur-e Zaban-e Avestai, Khajeh 1364/1985", "kind": "purchase", "url": "taaghche.com (revised edition ebook)", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: the 1364 Khajeh edition is not digitised; a revised edition is sold as an ebook on Taaghche."}

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
```


### [2026-09-05T20:27:16.954Z] TOOL RESULT

```
{
  "pdf_page": 124,
  "book_page": 94,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Dhě 2",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
      "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
      "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را ا
---
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
```


## [2026-09-05T20:28:03.955Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 311\" POK_full.txt | head -20\necho \"=== ndher ===\"\ngrep -n \"ndher\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:28:04.023Z] TOOL RESULT

```
26858:Page(s): 311-314 
=== ndher ===
90676:High German also 'wallow'. Old Icelandic valku. "das Hinundhergeworfenwerden, esp. auf
```


## [2026-09-05T20:28:05.495Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD en ===\"; grep -n \"^en\\b\\|^en\\.\" AHD_watkins1985.txt | head -20\necho \"=== AHD ndher ===\"; grep -n \"ndher\" AHD_watkins1985.txt | head -20\necho \"=== AHD en- entry ctx ===\"; grep -n \"\\ben-\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:28:05.580Z] TOOL RESULT

```
=== AHD en ===
442:en. In. 1. Germanic *in in: a. Old English in, in: IN; b. Germanic (comparative) *inn(e)ra in Old English innera, farther in, inner: INNER; C. Germanic *innan in Old English binnan, within (be, by; see ambhi + innan, in, within): BEN!. 2, Latin in, in-, in, into: EN-!, IN-?. 3. Greek en, en-, in: EN-2; ENKEPHALIN, PARENCHYMA, PARENTHESIS. 4. Suffixed form *en-t/e)ro- in: a. Latin intré, inward, within: INTRO-; INTRODUCE, INTROIT, INTROMIT, INTRORSE, INTROSPECT; b. Latin inird, inside, within: ENTER, INTRA-; INTRADOS, INTRINSIC. 5. Suf- fixed form *en-ter in Latin inter, inter-, between, among: ENTRAILS, INTER-, INTERIM, INTERIOR, INTERNAL. 6. Latin (superlative) intimus (*-mo-, superlative suffix), innermost: INTIMA, INTIMATE?. 7, Old Latin endo, Latin indu-, within, in industria, diligence, activity (*stru-, to construct; see ster-2): INDUSTRY. 8. Suffixed form *en- tos in: a. Latin intus, within, inside: DEDANS, INTESTINE, INTINE, INTUSSUSCEPTION; b. Greek entos, within: ENTO-. 9. Suffixed form *en-tero- in Greek enteron, entrails: ENTERIC, ENTERO-, ENTERON; DYSENTERY, MESENTERY. 10. Extended form *ens in: a. Greek eis, into: EPISODE; b. suffixed form *ens-6 in Greek esd, within: ESOTERIC. 11. Suffixed zero-grade form *n-dha possibly in Germanic *anda, *unda in Old English and, and: AND. [Pok. 1. en 311.]
443:en-. Year. Zero-grade form *n- in compound “per-n-yo-, of last year (see per’). [Pok. 2. en- 314.]
444:en-es-. Burden. Latin onus (stem oner-), burden: ONER- OUS, ONUS; EXONERATE. [Pok. enos- 321.]
=== AHD ndher ===
773:ndher-. Under. 1. Germanic *under- in Old English under, under: UNDER. 2. Latin inferus, lower: INFERIOR. 3. Latin infernus, lower: INFERNAL, (INFERNO). 4. Latin infra, below: INFRA-. [Pok. ndhos 771.]
997:sta-. To stand; with derivatives meaning “place or thing that is standing.” Contracted from *stag-. I. Basic form *std-. 1. Extended form *stddh- in: a. Germanic *stéd- J6n- in Old English stéda, stallion, studhorse ( < “place for breeding horses”): STEED; b. Germanic *st6d6 in Old English stéd, establishment for breeding horses: sTuD2. 2. Suffixed form *std-lo- in Germanic *stdlaz in: a. Old English st6/, stool: sTooL; b. compound *faldistélaz (see pel-3). 3. Latin stdre (third person singular present subjunctive séet), to stand, with its past participle status (< “sta-to-) and derivatives statira, height, stature, and statuere, to set up, erect, cause to stand: STAGE, STANCE, STANCH, (STANCHION), (STANZA), STATOR, (STATUE), STATURE, STATUTE, STAY!, STET; ARREST, CIRCUM- STANCE, CONSTANT, CONSTITUTE, CONTRAST, (COST), DESTITUTE, DISTANT, ESTANCIA, EXTANT, INSTANT, IN- STITUTE, OBSTACLE, OBSTETRIC, (OUST), PROSTITUTE, REST?, RESTITUTE, RESTIVE, SUBSTANCE, SUBSTITUTE, SUPERSTITION. 4. Suffixed form *std-men- in Latin std- men, thread of the warp (a technical term): STAMEN, STAMMEL. 5. Suffixed form *std-mon- in Greek stémén, thread: PENSTEMON. 6. Suffixed form “s¢d-ro- in Russian staryi, old (“long-standing”): STARETS. II. Zero-grade form *st- (before consonants). 1. Nasalized extended form *sfa-n-t- in Germanic *standan in: a. Old English standan, to stand: STAND; b. Old English understandan, to know, stand under (under-, under; see ndher): UN- DERSTAND; Cc. Old French estandard, rallying place: STANDARD; d. secondary zero-grade form in Germanic *stund-6 in Old English stund, a fixed time, while: STOUND. 2. Suffixed form *sé-tyo- in Germanic *stath- Jon- in Old Norse stedhi, anvil: strTHY. 3. Suffixed form *sta-tlo- in Germanic *stathlaz in Old English stathol, foundation: STADDLE, STARLING?. 4, Suffixed form *sta-mno- in Germanic *stamniz in Old English stefn, stem, tree trunk: sTeM!. 5. Suffixed form *sta-ti- in: a. Germanic *stadiz in (i) Old English stede, place: STEAD (ii) Dutch stad, place: STADHOLDER (iii) Old High Ger- man stat, place: SHTETL; b. Latin stati6, a standing still: STATION; C. Latin -stitium, a stoppage (in solstitium, solstice; see sawel-): ARMISTICE; d. Greek stasis, a standing, a standstill: sTAsIs; HYPOSTASIS, ICONOSTASIS, IsOSTASY. 6. Suffixed form *sfo-to- in Greek statos, placed, standing: STATIC, STATICE, STATO-; ASTASIA, ASTATINE. 7. Suffixed form “sta-no- in: a. Latin désti-
1678:INERTIA ar- INEXORABLE 6r- INFAMOUS bha-2 INFANT bha-2 INFANTRY bha-2 INFARCT bhrekw- INFECT dhé-1 INFELICITY dhé&(i)- INFER_ bher-1 INFERIOR ndher- INFERNAL ndher- INFERNO ndher- INFEST dhers- INFEUDATION peku- INFIDEL bheidh- INFIRM dher-2 INFIRMARY dher-2 INFIX dhigw- INFLAME bhel-1 INFLATE bhié-2 INFLICT  bhiig- INFLUENCE bhieu- INFLUENZA bhleu- INFRA- ndher- INFRACT bhreg- INFRANGIBLE bhreg- INFRINGE bhreg- INFUSE gheu- INGENIOUS gene- INGENUOUS gene- INGEST gerere INGRATE gWere-3 INGRATIATE gWere-3 INGRESsS ghredh- INGUINAL engW- INGURGITATE gWere-4 INHABIT ghabh- INHERE ghais- INHERIT ghé- INHIBIT ghabh- INHUME dhghem- INIMICAL amma INITIAL ej-1 INITIATE ei-1 INJECT yé- INJUNCTION yeug- INJURY yewes- INK kéu-
2436:UNCIAL ol-no- UNCIFORM = ank- UNCINARIA ank- UNCINATE ank- UNCINUS ank- UNCLE awo- UNCOUTH gn6- UNCTION ong¥- UNCTUOUS ongW- UNCUS ank- UNDER ndher- UNDERNEATH ni UNDERSTAND sta- UNDINE wed-! UNDULATE wed-1 UNGAINLY gagina UNGUENT ong¥- UNGUIS nogh- UNI- oi-no- UNICORN ker-1, oj-no- UNION oi-no- UNIQUE oi-no- UNISON swen- UNITE oi-no-
=== AHD en- entry ctx ===
442:en. In. 1. Germanic *in in: a. Old English in, in: IN; b. Germanic (comparative) *inn(e)ra in Old English innera, farther in, inner: INNER; C. Germanic *innan in Old English binnan, within (be, by; see ambhi + innan, in, within): BEN!. 2, Latin in, in-, in, into: EN-!, IN-?. 3. Greek en, en-, in: EN-2; ENKEPHALIN, PARENCHYMA, PARENTHESIS. 4. Suffixed form *en-t/e)ro- in: a. Latin intré, inward, within: INTRO-; INTRODUCE, INTROIT, INTROMIT, INTRORSE, INTROSPECT; b. Latin inird, inside, within: ENTER, INTRA-; INTRADOS, INTRINSIC. 5. Suf- fixed form *en-ter in Latin inter, inter-, between, among: ENTRAILS, INTER-, INTERIM, INTERIOR, INTERNAL. 6. Latin (superlative) intimus (*-mo-, superlative suffix), innermost: INTIMA, INTIMATE?. 7, Old Latin endo, Latin indu-, within, in industria, diligence, activity (*stru-, to construct; see ster-2): INDUSTRY. 8. Suffixed form *en- tos in: a. Latin intus, within, inside: DEDANS, INTESTINE, INTINE, INTUSSUSCEPTION; b. Greek entos, within: ENTO-. 9. Suffixed form *en-tero- in Greek enteron, entrails: ENTERIC, ENTERO-, ENTERON; DYSENTERY, MESENTERY. 10. Extended form *ens in: a. Greek eis, into: EPISODE; b. suffixed form *ens-6 in Greek esd, within: ESOTERIC. 11. Suffixed zero-grade form *n-dha possibly in Germanic *anda, *unda in Old English and, and: AND. [Pok. 1. en 311.]
444:en-es-. Burden. Latin onus (stem oner-), burden: ONER- OUS, ONUS; EXONERATE. [Pok. enos- 321.]
687:lep-'. To peel. 1. Greek lepein, to peel (> lemma, husk): LEMMA?2, LEPTO-, LEPTON!; SARCOLEMMA. 2. Suffixed form *lep-i- in Greek lepis, lepos, a scale: LEPER, LEPI- DO-, LEPIDOTE. 3. Suffixed variant form */ap-aro- in Greek /aparos, soft: LAPAROTOMY. 4. O-grade form “Jop- in Greek elops, ellops, a fish (< *en-lopos, having scales; en-, in; see en): ELAPID. [Pok. 2. lep- 678.]
805:op-'. To work, produce in abundance. 1. Suffixed form *op-es- in Latin opus (stem oper-), work, with its denomi- native verb operari, to work, and secondary noun opera, work: OPERA!, OPERATE, OPEROSE, OPUS; COOPERATE, INURE, MANEUVER, MANURE, OFFICINAL. 2. Latin offi- cium, service, duty, business (< *opi-fici-om, “perform- ance of work”; -fici-, doing; see dhé-1). 3. Suffixed form *op-en-ent- dissimilated in Latin opulentus, rich, wealthy: OPULENT. 4. Suffixed form “*op-ni- in Latin omnis, all (< “abundant’”): OMNI-, OMNIBUS; OMNIUM- GATHERUM. 5, Suffixed (superlative) form *op-tamo- in Latin optimus, best (< ‘‘wealthiest’’): OPTIMUM. 6. Prefixed Latin form *co-op- (co-, collective and inten- sive prefix; see kom) in Latin cdpia, profusion, plenty: COPIOUS, COPY; CORNUCOPIA. [Pok. 1. op- 780.]
1486:EXxO- eghs EXOCRINE krei- EXODUS sed-2 EXOERGIC werg- EXONERATE en-es- EXOPHTHALMOS okw- EXORDIUM ar- EXOSTOSIS ost- EXOTERIC eghs EXOTIC eghs EXPAND pete- EXPATRIATE peter- EXPECT spek- EXPECTORATE peg- EXPEDITE ped-! EXPEL pel-6 EXPEND (s)pen- EXPERIENCE per-4 EXPERIMENT per-4 EXPERT per-4 EXPIATE pius EXPIRE spirare EXPLAIN pele-2 EXPLETIVE pela-1 EXPLICATE plek- EXPORT per-2
1977:ONAGER agro-, asinus ONCE oi-no- ONCOGENESIS nek-2 ONCOLOGY nek-2 ONE oi-no- ONEIROMANCY oner- ONEROUS en-es- ONOMASTIC no-men- es ONOMATOPOEIA kWej-2, no-men- ONSLAUGHT ant, slak- -ONT es-
1979:ONUS en-es-
```


## [2026-09-05T20:28:11.827Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26840,26880p' POK_full.txt"
}
```


### [2026-09-05T20:28:11.875Z] TOOL RESULT

```
"inward, internal; n. as subst., sing, and plur. the intestines'; 



Middle Low German Modern High German dial, inser^ eatable internal parts of animals 
', Old Norse Tstru., Tstrai., " the fat surrounding the intestine ' {*en-s-tro-)\ 

Old Prussian /nstran lat', Latvian ?striP\. " kidneys' {*en-s-tro-)\ Latvian leksa^ Inneres ', 
PI. ' intestines, entrails ' {*en-t-Ja), Old Lithuanian //75C/c»5 "heart', Lithuanian /sc/bs" 
intestines, entrails ' ( *en-s-tio-). 

About die compression Latin endo, indu^\v\\ wherefore gr. to £v5Tva, Old Irish inne^ 
intestines, entrails ', (common Celtic -ns-, -nt- > -nn-), see above S. 182 - About gr. £v-5ov 
"*in the house, indoors' (wherefore £v5o-0£v, -9i, Lesbian Doric £v5oi after oiko-0£v, -9i, 
oiKoi) s. dem-io build'. 

References: WP. I 125 ff., II 335 f., WH. I 687 f., 694, 708 f., 71 1 f., 870, Trautmann 69 f., 
198 f. W. Schuize Kl. Schr. 70 ff. 
Page(s): 311-314 

Root / lemma: en-2 

Meaning: year 

Material: Gr. bjoc, "year' Hes., doubtful, whether m. or n., 5i-£vo(; " biennial ', T£Tpa-£vr|<;, -£<; 

"quadrennial, four years old', hom. Akk. Sg. rjviv, Akk. PI. Ivrjc; "annual', irpnT-nv " one- 

year-old lamb' (to Doricnpc(TO(; from *prtos?)\ £v-iauT6(; "year' (to iau£iv: " wenn das Jahr 

^uht, Jahreswende '??). 

zero grade -n- in: 

Gothic fram fair-n-in jera. Old Saxon fer-n-un gere. Middle High German verne^ last 
year'; 

Lithuanian per-n-ar last year ', Latvian p^rns "the previous year'; 

russ. dial., Czech lo-ni {*ol-nJ) " letztjahrig '.
```


## [2026-09-05T20:28:12.633Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ndhos\\|Page(s): 771\" POK_full.txt | head"
}
```


### [2026-09-05T20:28:12.684Z] TOOL RESULT

```
63199:Page(s): 771 
63213:Page(s): 771 
63225:Page(s): 771
```


## [2026-09-05T20:28:16.147Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '63180,63230p' POK_full.txt\necho \"=== find en-1 header ===\"\ngrep -n \"Root / lemma: en-1\\|Root / lemma: en, \" POK_full.txt | head"
}
```


### [2026-09-05T20:28:16.209Z] TOOL RESULT

```
in a downward direction, down ' (?); 

Avestan ada/ri'under, below', Gothic undaretc. Old High German unfarand untah 
"under', neologism after Indo Germanic *upeh{0\d Indie uparieio. "above'); 

Old Indie adhara-, Avestan a5ara-'Vne lower, those below (pl.)| the dead ', Latin Tnferus ds. 
{*enferos, Indo Germanic *nd!^eros), Tnfernus' lower| under; underground! of the lower regions! 
infernal; of hell ' ds. (after supernus), infra'be\ow, underneath ' {*inferad) with Aniaut treatment 



of -d^-; gr. aGspo- placed perhaps in aGspi^u) " despise ' (compare Old Indie adhanna- ' 
despises'); Gothic i//7o'5/'o preposition "under' (Abl. auf-do) = Old Indie Adv. adharat 
"under'; 

Old Indie adhama-^ the lowest ' = Latin /hf/musds. 

References: WP. I 323, WH. I 698, Specht Indo Germanic Dekl. 2591. 
Page(s): 771 

Root / lemma: psi-s {*he- psi-s) 

Meaning: sword 

Note: only Aryan and Italic 

Material: Old Indie asi-m. " sword, butcher's knife '; Avestan arjhO-t ds.; Latin ensis 

"sword'. 

References: WP. I 324, WH. II 406, Specht KZ. 66, 34 f. 

Page(s): 771 

Root / lemma: psi- {*he- psi-) 

Meaning: dirt, black 

Material: Old Indie asi-ta-, fem. asi-knf swart, black'; gr. aa\c, "slime, mud (of a river)', 

aoioc; "muddy'. 

References: WP. I 324, W. Schuize Kl. Schr. 1 16 f. 

Page(s): 771 

Root / lemma: do^el- {*heb^e/-) 

Meaning: to sweep; to multiply 

=== find en-1 header ===
```


## [2026-09-05T20:28:22.574Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '63155,63185p' POK_full.txt\necho \"==== en1 material ====\"\nsed -n '26770,26845p' POK_full.txt"
}
```


### [2026-09-05T20:28:22.651Z] TOOL RESULT

```
since; henceforth, from now on, from this time on ', Lithuanian nunaPnow' (see above); Old 
Bulgarian nb " yet ', nyne' now' (see above); Tocharian A nuB no enk\. " yet, because'; 
Hittite /7i/ (sentence-prefatory particle); k/-nun 'now, yet', nu-wa 'stWV, nu-kwit' numquid '; 
Gothic nauh'sWW, Old Frisian noch. Old Saxon Old High German noh Adverb "still, also 
now, yet' from *nu-k"e; about the conjunction " neither ... nor ' see above S. 757 under ne1. 

Indo Germanic nu\s probably zero grade to neuo- "new', compare Old Indie nutane- 
"present, current' and "new', gr. vsov ti " just, recently ', Old High German niwes {ady. Gen.), 
Lithuanian naujafiresh, recently '. 

Maybe alb. ta-ni'now' [ta- {a-te) "this, that' + */7/"now'] : Old Prussian in tei-nu: Skt. nu 

"now, just, but' [adv]; Go. nu'now' [adv] 

References: WP. II 340, WH. II 186 ff., Trautmann 201. 

Page(s): 770 

Root / lemma: od'^os, pd^eri{*he- pd^os) 

Meaning: under 

Material: Old Indie adhah ' under' (as preposition m. Akk. and Gen.), Avestan ado'under', 

Armenian dnd{rr\. Instr.) "under'. Old Icelandic undds., Tocharian A ahc'under, downwards, 

in a downward direction, down ' (?); 

Avestan ada/ri'under, below', Gothic undaretc. Old High German unfarand untah 
"under', neologism after Indo Germanic *upeh{0\d Indie uparieio. "above'); 

==== en1 material ====
Czech russ. /7/Vads. {*neiuaVj\ 

zero grade Old English neowol, neol, nihor inclined forward, stooping forward; rushing 
down or past; precipitous, steep; inclined, well-disposed, favorable; easy ' from *niwol. 
Middle Low German n/ge/'\o\N, base'; 

here probably also with full grade Lithuanian /7e/Vc»//"torment, smite', Latvian nievaV 
disdain, scorn ' (also Gothic *naiw^ eveTxsv ' Marc. VI 19?). 

Maybe alb. A7/Ve/" levelled ground'? 

compare Indo Germanic /7/-zo'c»s"nest' under 5e(/-"sit, place'. As "run down, tell off, 
rebuke' (as Latvian nievat) based on probably also neid- " reproach, rebuke, censure, 
blame, esp. by word ', neit-^ to be hostile towards, attack ' neiq-{see there), in ne/-, n/-. 

enter, pter' between - in', en-tero- " inward ': 

Old Indie antar, Avestan antars. Old pers. antar' between ', adnom. with Lok., Instr., 
Akk., Gen.; Old Indie antara- " internal ', Avestan antara- " inner ', Superl. Old Indie 
antama-'t\r\e closest ' (not to ant/, anta-), Avestan antsma-^ the most internal, intimate, 
inmost '; Old Indie antra-, also with Vrddhi antra- v\. " intestines, entrails '; 

Armenian 9nder-k'P\. " intestines, entrails ' (gr. loanword ? s. HiJbsehmann Arm. Gr. 
1447 f.); 

gr. EVTspov, mostly PI. ' intestines, entrails '; 

alb. nder, nder^ between, in', further ndjer, ngjereic. "until' {*entero-)\ (common Slavic 
dz\ Albanian dj, gl, ^yallophones) 



Latin enter, inter^ prep, with ace. between, among, amid; during, in the course of ', 
adnom. m. Akk. (solidified m. Gen. intervias, interdius), intro, intra, intrin-secus, interus^ 
internal ', interior, intimus, in tes tin us {see below), Oscan Entraf^* Interae ', zero grade, 
Oscan anter^ between, among, amid; during, in the course of, Umbrian anter, ander 
"during', adnom. m. Lok. and Akk.; 

Old Irish eter, etir, etar^ between ', adnom. m. Akk., corn, ynter, yntre, bret. entre{\.\\e 
ending after tre-, dre= cymr. trwy), acymr. ithr^ between, among, amid; during, in the 
course of; gall, inter ambes 'bebNeen streams'; 

Old High German untaretc. "under = between' = Oscan a/7/e'/'(differentfrom Germanic 
* under. Old High German etc untar'be\o\N' from *nd'^er, Latin infra); compare Gothic 
undaurni-mats ' lunch ' = " breakfast ', Old Norse undornn. "morning (at nine clock)'. Old 
Saxon undorn. Old English i//7o'e/77 "midday'. Old High German ^/7/o/77 "midday, lunch' (/?- 
suffix as in Latin internus); zero grade as gr. svTspa etc. Old Norse idrarP\. " intestines, 
entrails ' (from *innrar, *int^erdz), innre, idre^\he inner' (if not specific nord.-zio- has 
derivatived from inn= Gothic //7/7"hinein', see above); (under the influence of common 
Celtic -ns-, -nt- > -nn-). 

Slavic *§tro\n Old Church Slavic y^/AO "liver', ablaut, gtroba^ywer, *intestines, cavity of 
the body', gtrt ' eigw '. 

about Hittite anturiias^ inner, interior ', andurza^ inside, within ' s. Lohmann I. F. 51, 320 
f. 

Note: 

The inanimate suffix -ur-: Hittite anturiias^ inner, interior ' : 'lAAupioi , oi, lllyrians, 'lAAupia , 
n, lllyria, also'lAAupi? , n. Adj. 'lAAupiKO? , n, 6v, lllyrian: -Kr), the region or province of lllyria, 
lAAupi^U) , speak the lllyrian language, 'IAAupia:--hence Adv. 'lAAupiaii. 

e/7/'d5"(from) inside ' (compare Old Indie /-/a/? "from here', Latin caeiitus eic): 

gr. EVTOc; " inside ', whereof evtog-Gev, -0i and further evtogGiq, £VToa9i5ia " intestines, 
entrails ' (or latter with from svtogGs lengthened in 9 for *£VTOGTia, compare Old Indie 
antastya-r\. " intestines, entrails ', Pick I"* 363, Vendryes Rev. et. gr. 23, 1910, 74); 

Latin intuslrom inside, within; inside ', therefrom with analog metathesis intestmus 
"inward, internal; n. as subst., sing, and plur. the intestines'; 



Middle Low German Modern High German dial, inser^ eatable internal parts of animals 
', Old Norse Tstru., Tstrai., " the fat surrounding the intestine ' {*en-s-tro-)\
```


## [2026-09-05T20:28:28.409Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=26690 && NR<=26770' POK_full.txt | head -60"
}
```


### [2026-09-05T20:28:30.089Z] TOOL RESULT

```
alb. //T/" until, in ' {*en/); 

Latin //?, oldest err, Oscan en, Umbrian en- {en-dendu^ stretch out, reach forth, extend 
'), postposition Oscan -en, Umbrian-e/r?, -e, adnom. with Dat. (= Lok.), Akk. and Gen. (of 
ambit); 

Old Irish //7-"in' adnominal m. Dat. and Akk.; nasalized), in- (derived from *eni, compare 
/ngenirom proto Irish //7/-^e/75 "daughter'; mixed with /nd-= gall, ande-, s. Thurneysen 
Grammar 531 f., Pedersen KG. I 45), acymr. abret. en, //7"in', corn. bret. en, ncymr. yn-, 
gall, essedon {*en-sedon) " chariot ', embrekton^ immersed (swallowed) bite ' (see below 
mereq-); 

Gothic //7"in', adnom. m. Dat., Akk., Gen.; Old High German Old Saxon Old English in. 
Old Norse /""in', adnom. m. Dat. and Akk., from *e/7/ (about derivatives as Gothic inn^\n, 
into', inna, innana, probably from *eni-n-, s. Brugmann IF. 33, 304 f.); (under the influence 
of common Celtic -ns-, -nt- > -nn-). 

Old Prussian e/7"in', adnom. m. Dat. and Akk., Latvian /e-(only prefix); zero grade */7in 
Lithuaniany~(older and nowadays dial, in, int) "in', adnom. m. Lok. and Akk.; 

Old Church Slavic on-{on-usta^ footwear', p-o'o/i. "valley'), zero grade vbn-, i/b"in', 
adnom. m. Lok. and Akk.; 



Tocharian AB y-, yn-, B in- (only prefix). 

^-dh/;Old Indie adhi^aboui, on', Old pers. ao'/j/'in'; gall, intensive prefix /4/7ofe-(PN 
Ande-roudus^ the very red '), cymr. an{ne)- in anne-T contrivance ' (common Celtic -ns-, - 
nt- > -nn-) = Old Irish /nde-/{*n6^/-/-om), cymr. an-daw^ eavesdrop ' (to taw^ 
closemouthed '); Old Irish ind- (partly from *indi-, partly from secondary *indo) in ind-reth " 
incursion ' {*indi-reto-), indnaide {see further under), etc. Pedersen (KG. I 45) will also 
place here Gothic und'up to'; s. about other possibilities above S. 50 and S. 1 81 . 

(ejnero-' inner': Armenian *nero-' the inside ', assumed from ner- ' within, in, into', 
nerk's' inside ', nerk'oy' inside, within '; perhaps gr. svspoi as " those below, those 
beneath the earth, of the dead and the gods below ', namely in the earth; or better 
Hypostase from oi £v spg? 

/?/-, /7e/-"low, base', comparative nitero-\o^' (in contrast to " upper '): 

Old Indie nf, Avestan nf down; downward ', Old Indie nitaram^ underneath ', Avestan 
nitama- " the lowest '; 

Armenian ni-, n- "low'; 

Celtic */7efrom */7e/in Old Irish ar-neut-sa, in-neut-sa^ I expect, anticipate ', (Proto Irish 
*-ne-sedLJ), verbal noun indn(a)ide ( *indo-ne-sodJon) and in ar-neigdeV\.o pray' ( *ari-ne- 
gedont); compare different Bergin Eriu 10, 111; 

Old High German nidar. Old Saxon nithar. Old English niPer, Old Icelandic nidr^ down; 
downward ', Old High German nidana. Old Saxon n/thana ' under' , Old English neodan, 
n/Pan 'down, downward, under'. Old Icelandic nedana' from here below ', preposition with 
Akk. "below'. Old Saxon nitheMv. 'under'. Old High German /7/b'a preposition with Dat. 
and Akk. "below, under'; 

Old Bulgarian nizh " down, downwards ' (formation as pre-zh etc.); 

in compound:
```


## [2026-09-05T20:28:35.319Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT adiy ===\"; grep -n \"adiy\" KNT.txt | head -30\necho \"=== KNT antar ===\"; grep -n \"antar\" KNT.txt | head -20"
}
```


### [2026-09-05T20:28:35.384Z] TOOL RESULT

```
=== KNT adiy ===
112:the Іпбсайуе.................... 90 Tense Азресі...................... 91 The Perfect Тепѕе.................. 91 The Ёшїше........................ 91 Coordination and Subordination. . 91 The Coordinating Continence: pice '!! The Negative Adverbs.............. 92 The Subordinating Conjunctions. „... 92 The Conjunction уйӣій.....:......... 92 The Conjunction уй0............... 92 The Conjunction yadátga. . . ......... 93 The Conjunction yadiy............. . 98 The Conjunction уй@............... 93 The Conjunction 4ya............:... 9
419:ХРе ASayarsa : xsdyadiya : vazraka :
806:yadiyarsa.
818:Jud : тфу фат? = jvadiy : paradayadém A’Sd 3; uncertain words.
1061:daéva-, Skt. devd-, Lt. divos deus. pIE *ped- ‘foot’, loc. in ОР ni-padiy, Skt. padi,
1282:dh (imv.), OP jadiy, Skt. jaht (Skt. 7 by
1515:*ped- or pod- Чоо? in ni-padiy pati-padum Gurma-pada-, (Ar.) *pàd- in pddaibiya ‘with the two feet’.
1528:*gthen- in ajanam ‘I smote’, *g*hn- in jadiy ‘do thou smite’, -jata ‘slain’.
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
1648:radiy; fra-haravam.
1654:nai-mà, nai-maty, nai-$im, nat-pati-mà, pali-maty, iyat-Saty, imat-vd, yadi-patiy, yadi-và, [us}i-ca; similarly in phrasal compounds, pati-padem, ni-padiy. By analogy, naty-di§ DB 4.73, 78.
1678:Prep. patiy, but pati-padam; party, but pari- barümiy; prefix ni- (not found separately in OP) in ni-padiy, ni-rasdtiy.
1774:йр- ‘water’, zíap- ‘night’, xfnau- in u-zfnau- ‘well satisfied’, gau- ‘cow’ in compounds, bard- ‘year’, dwar- ‘door’ in duvara-, nar- ‘man’ in üv-nara-, nàv- ‘ship’, паћ- ‘nose’, pad- ‘foot’ in nipadiy etc., vas- ‘wish’ in adv. vasiy, vib- ‘house’, séd- in upa-stá- ‘aid’, zam- ‘earth’ in u- zma- etc.; perhaps napdl- ‘grandson’, an old pIE word, probably a compound; possibly dà- in ‘wada- as element of Paisiyà-uvüdà-, and vaj- in gen. daha-vaja. $143. Noun AND ApjectivE STEMS WITH THE-
2228:rüdiy, -padiy in ni-padiy, vasiy (but cf. Lex. s.v.) “have the regular pIE endings of their cases: acc.
2321:$197, Tue PIE Retative Pronoun *0- sur- vives in OP as the second element of hya hyd tya (8198); in the nom.-ace. nt. yaciy ‘whatever’ from *'od-q*id; and in the subordinating conjunctions уйй, yaà, yada, yadiy, yaniy, yàvà, the formation of which is given in the Lex. s.vv.
2345:The adverbs from this stem are атайй, avadā, ava-pard, avahya-radiy, pasdva (from *pasd ava).
2404:„ рту. *g*hn-dhi, OP jadiy, Skt. jaht; so alko 2d pi, imv. *o*hn-le, OP jata, and 3d sg. imf. mid. *egthn-lo, OP patiy-ajalà| imf. *eg*hen-m, OP ajanam, Skt. áhanam (with antevocalic de- velopment of m, $07.11), whence with the- matic vowel 3d рі. OP -ajana" in avajana* and perhaps the restored subjunctive 3d pl. i-Janá"tty.
2486:pIE *g*hedh- in pAr. *fadhja-, Av. Jaiüyeiti, OP — 4 jadiyāämiy 1 entreat’. |
2531:$220. Tue Passive-Votce Present STEM of pIE was formed by the addition of the suffix pIE -je-/-4o-, which is accented in Sanskrit; in OP the root regularly has the normal grade, with -a-: imf. 3d sg. and pl. abariya abariya", to root bar-; ayadiya ayadiya", to yad-; akaniya, to root kan- ‘dig’; afahya and afahiya, to Ваћ-; avaniya, to van-; ajantya, to jan-; akariya akariya"la, to kar-; pres. ist pl. &ahyàmahy, to dah-; opt. 3d sg. kariyaiš to kar-, frabiyats to frað-, 3d pl. yadiyaiša” to yad-.
2548:П. Thematic stems have optatives with -i- (as zero-grade of -;&-, cf. I) added to the thematic vowel pIE -о-, making pIE -o7-: cf. 2d and 3d sg. Gk. depos tpo, Skt. bháreg bhdret. Examples: 3d sg. vi-nãbðayaiš, pass. kariyaiš frafiyars, pass. pl. yadiyaiía" (for ending, $282.11); 2d sg. mud. with ending -so, yadas3á, cf. Gk. $€po.
2561:I. The primary ending -mi is attached directly to non-thematic stems, as in pIE *es-mz, Skt. dsmz, Av. ahmi, ОР amiy. The ending of thematic stems was the lengthening of the thematic vowel o, as in Lat. ferd, Gk. феро; but to this -б there was added in Aryan the ending -mz, as in Skt. bhdra-mt, Av. barümi, ОР pari-barümiy. Other OP examples: parsimiy, Skt. prechámi; dárayamiy, Skt. dhard- ydmi; vatndmty, jadiyämiy.
2573:fer from the sigmatic aorist, where the termina- tions would be pIE -?s-m -is-s -is-t, pAr. -isam -iš -1&; the identity of second and third personal forms gives an analogy to the 2d sg. imperfect in -1-$# (no examples extant in OP), whence impf. 3d sg. in 4$. After u the phenomena are the same.? The OP examples are àt$ ‘went’, 0170-07 ‘went past’, aku- naus ‘паде’ (Skt. ékynot), adarsnaus ‘dared’ (Skt. ddhrgnot); and the thematic optatives active vi- ndlayars, passive kariyars fradiyars (cf. for ending Gk. $€po,, Skt. bhdret).
2583:II. The secondary ending was pIE -nt, which - lost the final ¢ in pAr. unless sentence phonetics ` permitted its retention; for in pAr. only a single consonant could stand at the end of a word. In OP, also, the final n was not written (§112). Be- fore this ending the thematic vowel was -o-: pIE *ebheront, Gk. égepov, Skt. dbharan, OP abara”; OP abava", anaya”, ayauda", asiyava", alarsa”, agar- báya"; passive арата", ayadiya". Non-thematic stems would normally have pIE -nt after conso- nants, becoming pAr. -at; but this was commonly replaced by -an(t) after the -am of the Ist sg.: pIE *és-nt, but Skt. азат, ОР аһа”; OP apariy- diya”, avájana",
2584:III. The sigmatic aorist similarly remodeled its 3d pl. from -sat (< -s-nt) to -san(t); thus in ОК, s-aorist €\vo-av ‘they loosed’, whence strong aorist &o-cay ‘they gave’, and (late Greek) thematic éhaBo-cav ‘they took’. So also in OP, the -san j spread to some verhs,! being regularly -ha^ after a _ and -ša” after 1: abaraha^ alongside abara”, patiy- dia", opt. pass. yadiyaisa*, and with extension of — -ša” to the position after a, adurujtyasa", akuna- vasa” alongside akunava*.
2604:I. The second smgular active of thematic stems is the stem without suffix: jivà, Skt. jiva; pari-bará, Skt. bhára, Gk. $€pe; parsa, Skt. prechd, Lat. posce. That of non-thematic stems has an accented -dhi, attached to the zero grade of the root: pIE *i-dht, OP -idiy in paraidiy and paridiy, Skt. tht, Gk. 16; pIE *gthn-dht, OP jadiy, Skt. jaht; OP pädiy, didiy (5129), G-rsnudiy.
2663:D. As double object, one of the person and the other of the thing: DB 1.44f айа xšaçam tya Gaumdta hya magus айта Kabügiyam ‘this king- ship which Gaumata the Magian took away from Cambyses’ or ‘of which Gaumata deprived Cam- byses’; so also 1.46f, 59, 65f, and its passive in 1.49f hya атат Gaumàlam Шат magum тёасат ditam салтта ‘who might make that Gaumata the Me- dian deprived of the kingship’, DB 4.65 лау Skaurim (= skaubim) пай tunwatam züra akuna- vam ‘neither to the weak nor to the powerful did І do wrong’. DPd 20-2 айа adam yànam jadiya-
2763:I. The pronouns haw, ava-, -fim, -dim, and their forms are often used to refer back to a pre- ceding phrase or relative clause; a preceding phrase is usually in the nominative, as in DB 2.30f Ката kya hamiçiya тапа nary gaubatary avam jadiy ‘the rebel army which does not call itself mine—that do thou smite’, but sometimes in its own proper case, as in DB 2.84 kdram hamiciyam hya mand naty gaubdtaiy атат jatà ‘the rebel army which may not call itself mine—that do ye smite’.
2802:VI. In two passages tya- is demonstrative: DB 3.73 nipadiy tyaiy ‘close after them’, where the text is certain, and 051 14 [уй ‘these two’, which rests upon only slight traces of the characters.’
2811:§264. Tug DEMONSTRATIVE ava- ‘that’ is simi- larly either pronoun or adjective; it commonly refers to something already mentioned, but some- times has a forward reference, as in naimd ava ката tya tunuvd skaubars radiy miła kariyars ‘that is not my desire, that the mighty should have wrong done to him by the weak’ (DNb 10f; also DB 3.58, 5.21, DNa 39, DNb 20, 53, 55, 57, DSa 4, DSe 34, XPh 49, 51f). It has also the meaning ‘yonder’ as applied to the sky: Auramazdà hya imam bümim ada hya атат asmdénam айй ‘Ahura- mazda, who created this earth, who created yonder sky’ (DNa 1-3, eto.).
2829:verb. yàlà, prep. w. loc. уйй à, prep. w. abl. radiy, postp. w. gen.
=== KNT antar ===
1336:pIE "enter ‘inside’, ОР ачаг, Av. antara, Skt. атт, Lt. inter.
4950:atar (i.e. ачат), prep. with ace., ‘within, among’: Av. antara, Skt. antar, Lt. inter, pIE tenter (831). DB 1.21; 2.78; 4.32, 92; XPh 30, 35.
5397:ja*tar- sb. ‘smiter, slayer’: Av. Jantar-, Skt. hantdr-; pIE *g*hen-tor-, agent noun to OP root jan- ($154.11). Jat пзш. ($186.1) DB 4.58, 78.
```


## [2026-09-05T20:28:44.570Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ *ad[iíì]\\|^adi\\| adi \\|adi-\" KNT.txt | head -20\necho \"=== BRT adairi ===\"; grep -n \"a5airi\\|adairi\\|aoairi\\|aöairi\" BRT.txt | head -20\necho \"=== BRT haca ===\"; grep -n \"ha.a-a5\\|haca a5\" BRT.txt | head"
}
```


### [2026-09-05T20:28:44.720Z] TOOL RESULT

```
1654:nai-mà, nai-maty, nai-$im, nat-pati-mà, pali-maty, iyat-Saty, imat-vd, yadi-patiy, yadi-và, [us}i-ca; similarly in phrasal compounds, pati-padem, ni-padiy. By analogy, naty-di§ DB 4.73, 78.
1877:Only compounds of stem + stem will be here discussed. Either stem may itself be a compound; either stem may already have one or more suffixes. The initial syllable of the first element, especially in adjectives, may show vriddhi or lengthening of the vowel, as in dáraniya-kara- ‘gold-worker’ to daranzya- ‘gold’; less often this appears in the sec- ond part, as in Baga-yadi- 'god-worshipping (month)’, where it is seen in both parts, and in asa-bàra- ‘horse-borne’, where it indicates passive meaning.
1913:a. Accusative: Aspa-canah- ‘Having love of horses’; Baga-yadi- ‘(Month) marked by the wor- ship of the bagas’.
1960:With vriddhi in both parts: Baga-yadi-.
1962:Perhaps with vriddhi in prefix: Vi-yax-na- (radi- cal element uncertain). .
2926:(c) In alternative general clauses, the first intro- duced by ya6ü ‘when’ and the second by yadi-và ‘or if’; the main clause omits the copula: vaindhy . . . drsnavéhy DNb 29f.
2994:$297. THe Consuncrion yadty ‘if, when’ has several uses. In the meaning ‘i’, it most often takes the present subjunctive as the protasis of a future condition; the apodosis has the affirmative imperative or optative, the negative injunctive or optative, or the present subjunctive (DPe 22) as a future indicative. In DNb 20f yadi introduces a future less vivid condition, with present optative in both parts. In DNb 25 and 29 yadi-và ‘or if’ re- peats tya '(that) which’ in introducing an alterna- tive verb; in 29 the verb is in the subjunctive with the main verb omitted, and in 25 both verbs are in the present indicative. In general conditions the ‘if? easily passes into ‘whenever’, as in the two instances in DNb 38f, where the present indicative is used in both parts in a timeless gen- eral condition; and ‘whenever’ passes into ‘when’, used of past facts with the imperfect indicative, DB 1.38 and DSf 14.
3001:(b) Alternative: the alternative to a general relative clause is introduced by the relative with the enclitic -vă (DB 4.68f) when the relative is in the nominative case, but it is introduced by yadi- và ‘or if? (DNb 25) when the relative is in the ac- cusative; the alternative to a general temporal clause introduced by yada ‘when’ is introduced by yadi-vé ‘or if? (DNb 29).
4105:28 : Katpatuka : Sparda : Yauna : бака : {уау : pa 29 radraya :Skudra : Yauna : takabarà : Рибу 30 à : Каўуя : Maciya : Karka : дану : D 31 drayavaus : xšāyaðiya : Auramazda : ya 32 & : avaina : imàm : bümim : yaudatem : 33 pasávadim : manā : frábara : mam : 28d 34 уадуат :akunaus : adam : x&àyatiya 85 :amiy.:.vasnd : Auramazdahd : a 30 damSim : gafava : niyašādayam : tyašā 37 m : adam : afaham : ava : akunava : yabā : mam: 38 Ката : aha : yadipatiy : maniyáhaty : t 39 ya :ciyakaram.: dha : ava : dahyiva 40 :tyà : Darayavaus : xSayafiya 4] :adáraya : patikarà : didiy : tyaiy : g 42 àfum : baratiy : vadā : xSnasahy : 43 adataiy : azdà : bavatiy : Pārsahyā : 44 martiyahyà : diraiy : artes : pa 45 ràgmatà : adataiy : azdà : bavāti 46 y :Parsa :martiya : dürayapiy : hacà : Pa 47 rsà : partaram : patiyajata : 6itiy : Da 48 rayavauS : xSdyafiya : aita : буа : karta 49 m :ava :visam : vasnà : Auramazdaha : ak 50 unavam : Àuramazdá(ma)iy : upastàm : aba 51 ra : yütà : kartam : akunavam : mém:A 52 uramazdà : pàtuv : аса : gasid : utama 53 iy : vitam : uta : imàm : dahyàum : aita : ada 54 m : Auramazdam : jadiyámiy : aitama 55 iy : Auramazda : dadatuv : 56 martiya : hyà : Auramazdah 57 & : framana : hauvtaty : gas 58 tā : ma : adaya : раб : .. 50 {уаш : ristim : mà 60 : avarada : mà : stabava Nores то DNa: The text of DNa now rests upon the photographs of F. Stolze (Persepolis: Berlin, 1882) and of А. Sevruguin (accessible in Wb. Grab, Plates 2-3). The following readings, which either replace older wrong readings or confirm older doubted readings, are assured by the photographs; the restorations agree with the length of the gaps: ^? framatà- | ram; ™ düraiapty; 9 patiyazsayaty; 9^? aba[ra]- | ha; * adáraiya (for nor- malization, ef. $48); 25 haumavargá ; * akunava; * yadi- patiy : maniy|ühaty : t]- | ya (for -haiy, cf. note on DB 4.39); * {aha} Wb.; “ no space for [mand] before ga6um; £ a[va]dà; **düraiy; 4 dárayapiy; ® Auramazda(ma)ty, with omission of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim],
4746:A’Pa = ARTAXERXES III, PERSEPOLIS А, B, C, D. 1 Бара : vazraka : Auramazda : hya :' 2 упал : bümàm :adà : һуа :a 8 vam : asmünàm : ada : һуа : marti 4 yam : adi : hya : &yatàm : adi : mart ` 5 ihyà : һуа : mim : Агіахёаса : х$ауз 6 буа, : akunaus : aivam : parüvnàm :
5627:(1) Adv. ‘thereto, again’: DB 2.37, 48, 57; 3.04, 71. pati-maty ($186) DNb 32f.  nai-pati-mà ($133, 5186) DNb 20. yadi-patiy (8136) DNa 38. (ya-patiy XPa 15; XPf 40f.
5829:yad- vb. ‘reverence, worship’, usually middle: Av. yazaite, Skt. ydjati, Gk. aterat, pIE *raój- (888, §113). See also Agiyadiya-, dyadana-, Bagayadi-, zyadā. yadataiy mid. ($213, §235.1) XPh 53. ayadaty lst sg. imf. mid. ($288.Ш) DB 5.16, 32; DSf 18°; DSk 5; XPh 40f. ayadiya imf. pass. ($220) DB 5.16°, 32.  ayadiya^ 3d pl. imf. pass. (8220, $282.11) XPh 36, 40. yadàátaiy subj. mid. (6999 11, 8235.1) DB 5.19, 34f. yadaišä 2d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39.
5835:yadiy conj. ^if, when’: Av. yetéi, Skt. yddi: per- haps pAr. nt. rel. *iad + deietic 4. Syntax $297. (1) Sf, with subj.: DB 4.38f, 54, 57, 721, 77; DPe 19, 22; DNa 38 (yadi-patiy), DNb 29 (yadi- và; cf. Hz. ApI 359); XPh 47 (yadi-maniyáty; 841, $92. VI); with opt., DNb 20f; with pres. ind., ОХЬ 25 (yadi-và). (2) ‘when’, with imf. ind., DB 1.38, DSf 11; ‘whenever’, with pres. ind., DNb 38f, 39.
5864:-vä encl. conj. ‘or’ (8133, $291.11); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
=== BRT adairi ===
3256:•  j.  adairi  Praep.  'unter,  unterhalb';  i)  mit Akk.:    ao'  hax>m  nivöiryeite  V.  <¥.  69;  —
4557:Z«hen beider Füsse':  aoairi  'ia(AD.)  V.Ä
4622:Zehen  beider  Füsse':  aoairi 'ta(AD.)  V.*.
8360:•  j.  upairi.dahyav-  Adj.  (auch  mask.) 'der  über  dem  Land  ist':  mür^m  °yüm  .. aoairij/a/iyBm  (ASm.)  YLjo.  144.
=== BRT haca ===
```


## [2026-09-05T20:29:02.829Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== HRN leaf 27 (p.6) =====\"; awk 'BEGIN{RS=\"\\f\"} NR==28' HRN.txt\necho \"===== HRN leaf 41 (p.20) =====\"; awk 'BEGIN{RS=\"\\f\"} NR==42' HRN.txt"
}
```


### [2026-09-05T20:29:04.670Z] TOOL RESULT

```
===== HRN leaf 27 (p.6) =====
6 -
phlv. evar (vd. 5 (146) Gl., Men.), päz. äwar^),
evarih (vd. 5 (146) Gl.). (Darmesteter, Et. ir. I, 251).
phlv. evar führe ich auf ap. *adi -+- [/'var- zurück;
adi (ai. adlii) kommt auch noch in estäden (und
vielleicht in evän, evar (^INZ^N Jer. 5, 6) vor (vergl.
KZ. 32, 581).
17. ärey 'Hass, Feindschaft*, rey,
ap. araika- Teind'; aw. ara^ka-.
Statt ärey ist vielleicht erey zu verbessern (dann
wäre rey die lautgesetzliche Form); die altpersische
Form könnte andernfalls natürlich auch äraika- gelesen
werden.
18. äz 'Begierde' (z. B. Vis und RämTn, Seite 47 Vers 14),
ahmend, azver {äzür),
aw. asi- 'Gier ; phlv. äs, äzmand, äzvar,
19. äzäd *frei', äzöde.
.^^x^^ aw. äzäta- *frei, edel*; phlv. azät, arm. LW. azat,
azatak, vergl. atarrj tXsv&soia sc. napd Ils()(T(ag (Hes.).
kurd. aza *brav, tapfer* (Houtum-Schindler).
20. äzär Xeid*, azärden^ azdris; äzerden^ äzerm^).
aw. a + [/'zar-j azärayeiMi sie peinigen' ; phlv. äzär,
äzartan etc.; ai. [/har- 'zürnen.
21. äzmUden 'erproben, versuchen', Praes. äzwäy-em,
äzmä, äzmäyis\ li'^NQilN (Is. 7, 12).
phlv. özmütan, özmay(i)sn es ist zu versuchen' (vd. 5
(146) GL), 'Versuch' (Men. 60, 14, K 43).
bei. äzmäyag (LW.), n. äzmainay (23).
aw. *a (oder nach dem Pehlevi wohl ava) + uz +
i/'mä'.
^) Np. aver *wahr, Wahrheit*, äverl brauchen nur Pazendworte
zu sein; doch bin ich über Sahn. I, 35 Vers 19 noch nicht im Klaren
{reftäwerl wäre eine sehr bedenkliche Bildung). Etwa: *"Wir müssen als
Köche zum Sah gehen — fürwahr! und dann ein Mittel ersinnen etc. ?
*) Im Pehlevi auch schon in der kaum hierher gehörenden Be-
deutung *Ehre, Achtung* (GF.), anäzarm (Men.), vergl. Vis und Kämln,
Seite 32 Vers 12, 86 Vers 3 v. u.
===== HRN leaf 41 (p.20) =====
- 20 -
81. est ^Knochen, este 'Knochen, Kern' (vergl. künjeste,
AM. 80 Zeile 5, 163 Zeile 5 v. u., 170 Zeile 3, daneben
auch gün]estej AM. 126 Zeile 4 v. \x,), /estu,
g. äste,
aw. ast-^) *Knochen ; phlv. ast 'Knochen*, astak *Kern;
ai. asthdn-, dsthi-,
kurd. haste 'Knochen etc.; oss. stag, L stäg (228);
minj. asti, sangl. astak.
82. i8tä%, istaky sitak 'Zweig*.
de Lagard e vergleicht arm. cax, aber np. istäx könnte
im Armenischen nur als stax erscheinen. Die ältere
Form ist istak, sitäk, phlv. stak (Bund.). Zu l^sthä-.
83. iistäd, ustaö *Meister'.
aw. "^avastata- 'Vorsteher; phlv. östat, arm. LW. ostat,
LW. kurd. üstä; aiy. usfaä; bei. vastäd (286).
84. istäden stehen*, estäden, Praes. esf-em^)^ sitaden,
p^N^xriD^t* (Jer. 5, 26).
ap. V^stä' (ai. sthü-); päz. estädan.
Im Sähnäme reimt ist *stehe* auf nest, ist also est zu
sprechen {me est I, 136 Vers 125). Ich leite np. estaden,
später istäden, von ap. *adi + l^stä- ab, vergl. phlv.
evar (unter No. 16) und KZ. 32, 581 No. 7.
oss. t. sfln, d. isfün aufstehen* (144) ; sist 'stehe auf*
etc., mit Praefix s (ms).
phlv. ösfätan [ava + \/'stä-) ; bei. östag, vustag n. östay
(402) finden sich im Np. nur dialektisch in g. ustädmün,
vistädmün.
Das PehlevT besass auch die mittlere^) Wurzelform
stT' in stinik (vd. 5 (38), aw. ereöwa-) ^b^%stm 'aufrecht
stehend* (vd. 18 (98) GL), vergl. skr. sthTyat^ (Brähm.)*).
^) Bartholomae, Arische Forschungen II, 112.
*) Auch in Indien spricht man nur Waden,
') Zur mittleren Wurzelform aihä- vergl. Hübschmann, Das
indogermanische Vocalsystem 20, 63.
*J NatürUch könnte man die Pehleviforraen auch steulk, -sten
lesen und skr. sthimän- etc. vergleichen, dessen e (*ai) aus ai/i ent-
standen sein könnte (vergl. Bartholomae, zuletzt Indog. Forsch. I,
490). Die Lesung stenik, sten scheint Bartholomae nach brieflicher
Mitteilung vorzuziehen.
```


## [2026-09-05T20:29:16.883Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== HRN leaf p.5 =====\"; awk 'BEGIN{RS=\"\\f\"} NR==27' HRN.txt | head -40\necho \"===== HRN p.27 (andar) =====\"; awk 'BEGIN{RS=\"\\f\"} NR==49' HRN.txt"
}
```


### [2026-09-05T20:29:18.842Z] TOOL RESULT

```
===== HRN leaf p.5 =====
5 -
gesetzlich unmögliche Etymologie Spiegel' s (Keil-
inschriften 2, 238, Ar. Periode 284) findet sich noch bei
Bechtel, Hauptprobleme, 163.
12. äräm *Ruhe*, ärarmden, arätnis, nu^'0'nN (jüd.-pers.
Bibelübs. ^).
aw. äramayat *er erfreute'; phlv. aramUan, äräni
*Ruhe'.
af/. bei. (18) LW. äräm,
Vergl. räm (No. 604).
\^. ärd 'Mehl'.
\ Käs. ort, ürt, vergl. auch s. v. äsyäh : ör, ä/-, ir,
aw. asa- gemahlen', anasa- (Hübschniann ZDMG.
38, 428); phlv. ärd ^Mehl'.
kurd. är, ärd (Jaba-Justi), ärf, irt (Houtum-
Schindler); af/. öra; bei. ärt n. arf (15); arm. aZ^wr
*Mehr, ahxm 'mahlen* (unsicher, H. No. 7).
14. uren *Elle', äreng^ ärenj,
phlv. äranj (PPGL).
oss. arm-arün *Elle'; sar. yovn 'Ellbogen*; gr. wXsvfj;
lat. ulna.
Vergl. aw. radni- in frara&nidrajö^); phlv. eratn (?);
ai. aratni' 'Elle'.
Die neupersischen Worte werden richtiger mit ä
(bezw. e) zu schreiben sein.
15. äroy (AM. S. 95 Zeile 2), üröq *das Rülpsen , äröytden,
röy,
gr. BQsvyo/Liai 'rülpsen*; lat. ructäre^ ructus 'das
Rülpsen*; lit, raugmi, rugiü 'rülpsen'; ksl. rygayq;
ags. rocetan (Hörn).
Zu arm. orc 'Speichel, Erbrochenes*, orcam erbrechen,
rülpsen* vergl. H. No. 233 und Bartholomae, Studien
n, 134.
16. äri 'fürwahr.
Käs. ore, dre^ drl.
^) Die Endung -ist ist bekanntlich im Afghanischen in der Form
'ist und -ast nicht selten.
*) Bartholomae BB. 17, 111 Anmerkung.
===== HRN p.27 (andar) =====
— 27 —
arab. LW. hinzamn 'Menschenmenge' (de Lagaide,
Armen. Studien, No. 1235).
115. en^lden zerschneiden, zerstückeln', Praes. enjln-em,
ap. *Aam + [/cay- (aw. und ai. 'zusammenlegen,
ansammeln etc.') ; phlv. ancUan bezw. han- , anj-
^krümmen, zusammenziehen (Bund.).
Zu dem Bedeutungs Wechsel vergl. np. ciden 'sam-
meln; schneiden'.
116. end *so viel, einige'; vergl. endek, endi, bes]end.
phlv. and 'so, so viel', andak Venig',
kurd. hind 'so viel', hindik 'wenig'.
Vom Pronominalstamm er-, aber nicht gleich aw.
avant-, phlv. havand, vd. 15 (48).
117. endäyiten * werfen', Praes. endäz-em, endaz 'Plan,
Absicht', endüze 'Mass'.
phlv. andäytan 'werfen'; sinnen* (Bund.), andäcak
*Mass', andäöUan erwägen , ermessen', andäc(i)sn
'Meinung ; arm. LW. amiacem 'überlegen', arab. LW.
muhandis 'Feldmesser', hmdasat 'Geometrie' u. a. m.
(de Lagarde, Arm. Stud., No. 116).
aw. hqm + {/^tac- ; Bedeutungswechsel wie auch bei
np. perdä/ten (No. 286).
118. endäm 'Körper, Glied'.
aw. hondäma- 'Glied' ; phlv. andäm, arm. LW. andam.
119. {i)ender 'm\ vergl. enderün,
ap. a(n)tar 'in, innerhalb'; aw. antare; phlv. andar^);
ai. antdr; arm. vergl. ender/c, ^nterk 'Eingeweide'
(H. No. 109).
Steht enderün für enderän (zu ün für an vergl. gerdün
No. 904), wozu man z. B. Sahn. I, 61 Vers 525 ver-
gleiche 2)? Vergl. jNTD, Ps. 68, 7, 8 (Grill).
120. {2)'ender in peder\euder {ped]ender), mader]ender
{mäd\ender)^ beräder]ender, /'aher]ender etc. 'Stief-'.
skr. antard' 'anderer, verschieden von'; osset. ändär
'andere, fremd' (20); got. anpar; lit. antras.
^) Phlv. andarg ist Unsinn.
') Das Pehlevi hat auch schon andarün (für aw. aw/ara-).
```


## [2026-09-05T20:29:29.645Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"antara\\b\\|antar9\\|antars\" BRT.txt | head -20\necho \"=== which leaf ===\"\npython3 - <<'EOF'\nd=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i,p in enumerate(pages):\n    if 'adairi' in p or 'antara' in p:\n        print(i, repr(p[:120]))\nEOF"
}
```


### [2026-09-05T20:29:31.371Z] TOOL RESULT

```
4330:•  j.  an-antar9  Adv.  'nicht  innerhalb,  nicht drinnen' :  "^rigiimi  antar}  'tan  aia  antar? fata>a.^  N..Vy(?).
4554:'antara-
4588:•  j.  ^'antara.iS'wa-  Adj.  'dazwischen  ab- zuschreiten': ya%ii  v3  gJntq  ävala  *dasaca °'iwqm  (NPn.)  "oder  soviel  als  zwölf  ab' zuschreitende  Schritte"  F.  27  a'*.
4590:•  j.  antars.iixtay-  £  'Aufsagespnich, Scheidespnich':  aniarxa  drvanUm  ämrüta aya  °ti:  nöit  n3  mani  "und  er  sagte dem  Z>r.  auf  mit  folgendem  Scheidespruch : 'nicht  (usw.,  Y. 45-2)'"  Y. /^.  15.
4592:•  j.  antar9.ka]»ha-  m.,  Plur.  Name  eines Gebirgs:  ahmat  haca  garayS  fraoxsyan  . . "tihaca  Yt  79.4.
4596:•  j.  antarsäa-  Adj.  'innerhalb  befindlich': "iräyS  'üi  (NP.)  ava.antara  *ptmntara maya'^^  frakäraySis  "drei  (Furchstriche) sollst  du  (so)  ziehen,  (dass)  darinnen  (sind) die  an  die  innem  angrenzenden  (jedoch) abgesonderten"  Löcher"  V.p.i  i.  a)  IS. als  Adv.  'inmitten  von  — ,  zwischen',  mit Akk.3*:  avat  virüraymm  .  .  yai  aslt  °h vehtixsakrqm  vaMflStslim  Vr.  20. 2*';  — wiederholt:  'ca  zam  °ca  asmamm  Y.61.1*,
4601:•  j.  antara.daöhav-,  °daliyav-  Adj,  (auch mask.)  'der  inmitten  des  Landes  ist': mi>nm  aiwi.daRyam  ..  '.ä/Sot  ( ASm.)  Yt lo.  1 44.  A)  m.  Name  eines  Berges  oder Gebirgs:  ahmat  haca  garayS  fraoxlyqn  ., dassmS  °/ihu/ Ytig.2.
4612:•  j.  antars-stä-  Adj.  'dazwischen  befind- lich' (näml,  zwischen  Himmel  und  Erde) ; imqmca  sfm  .  .  aomca  asmamm  . ,  iäca voka..yä  'st3  (APn.)  Yty.153.
4615:SuperL,  S.  'antara-.  —  ai.  anlama-  Adj.  —  Pü. : aiidarliim,  (zu  Vd.):  ha/diar.  —  ')  zSt.  Bthl. IF.  77,  115.  —  »)  Hds.  x^t>mHi\  s.  Bthl.  IF. II,  13t.  —  1>  Pü.  erl.:  ligBn  razikä.
4633:'antara-  13z
4636:KompA.,  E.  i  Ableit.  —  ai.  antär  Adv.  (usw.).  — FS.:  anäar,  andark,  andar  andark.  —  ')  Wohl aiilarän  lu  lesen.  —  >)  FoY  KZ.  35.  4z  will piiri^  Italt  d'lqr  lesen;    s.  abec  Rl.  iSt.    — 3)  l\Af,./rähU'ilintar>;'V'a.: ..  artdari.  —  *)  llds. fehlenil ;  s.  aber  Pü.,  die  iwelmal  andar  bietet. —  5)  Uiw.  Plor-i   vU,  nur'als  Vertreter  des AP. •  j.  'antara-  Adj.  'der  innere,  innen  be- findlich': °rpm  arpopui  nmänaAe  "ins  Innere des    Hauses"   V.  ö,  43;   —    VJ/V.  2. 40 PüZ.         a)   'räi  tsaemäi  'innerhalb',  mit folg.  i)  Gen.,  2)  Lok.,  3)  Instr.,  4)  Akk., uzw.  a)  räumlich,  b)  zeithch:'*  i  a)  a"  n° JiairaAe'Ü.Go;  104';  —  *a°  n°  *yii)yastsis N.  7/ T'>;    —    a'   w    aliö.draJaAyeAe    N. Ijg;  —  a'  «°  %rigäniye/ie  N.  6<}.  i  b)  a°
4641:KompE^  —  Konipar.;s.  gr.Vv. —  ai.  'äir/ara- Adj., np.  andar  'in,  innerhalb'.  —  Pü.:  andamcmai, andardn  ntmai.  —  i)  Vgl.  anlari.naem5l.  S. auch  'antara-.  —  ")  Hds.  aräl  11'.  —  J)  Hier
4985:•  j.  ■•'ava.antara-'*  Adj.  'an  das,  was innen  ist,  hinabreichend,  angrenzend": antanca  (sd.)  *''/-a'>.,  maya  Y.g.w.
7395:•  j.  ävistayae-.'ir  Inf,;  s.  unter  wV/iyaJ-Ja. g,,  j.  ävis  Adv.  'offenbar,  vor  Augen': •°    IUI   antars   hlttta    .  .    rätayö  (sd.)  Y.
11358:—  Ayiü  paourvlm  tat  ust?m>m{sd.)üi  Y. 5  öl  I,  Vr.p.  7;  —  aaj  ya^  bavaiti  avi.- spasls  sSsta  daiiakSui  .  .  tä  hasHi  vpa.- zbayette  Yt  13.  69;  —  yd  *a//  antarst nalmät  "hrigamyehe  paiti  apalcit  barSit  N. 6g;  6g;  —  m}r»n^aite..ydha  sat>m  kaya- oanqm  avavat  a^ava.jaHt  Yt  10.  2 ;  —  yi maibyä  yaol  ahmäi  as(sd.)^t  vakt/tä  . .  äft- iim  ^.46.1%.  ß)  des  Nebensatzes;  a)  II  im Ap.,  \i\v.tzx yähä: ya'i:3 pantvamciy  ava'^S Bh.  1. 1 43,  b)  im  Aw. :  *«//  tat  paiti  druxi nä/aite  (sd.)  yaiäi  (sd.)  alwi^i  jayma£ Yt/p.  iz;  —  astica  im  si  avaiti  iasff  ya- vaiti /raias^ij  Y. ig.7;  —  mrBi%i  tai mq%- Wim  yal  aemüii  ..  V.  2.  g  PüZ.;  —  hinter ya'ia:  avm  daZqm..ti/trlm  avSfitfm (ad.) .  .  ya^a  mqmcit  yim  ahursm  Yt  tf.  so; 70.  I ;  —  tl  mqm  ava^a  virsninte  yd^a ar/yäscij'^  ariUnS  , .  ham.vfnnavainti  V.  18. 32;  Yt/5.  54(?);  —  aoi  mqm  .  .  stüili yaha  mJ''  aparaHt  saosyants  stavqn  Y. g.  2;  V.5.  36;  —  avaha  hl  baisastm  (sd.) upsisay>n yd%a  dahmäicit  a^aone  V./_J.35;
15253:•  j.  panfa.saO'want-  Adj.  'fünfzigfach': °%itiä  (näml.  asti  mi^rs)  antars  huyäyna
16025:■  j.  pärantara-,  pärantara-  ■>  Adj. i)  'abseits,  gesondert  gelegen':  "^räys antanca  (sd.)  *ava.anlara  *'ra  '>  (alsAPm.) mtTfa  fi-akuraydii  V.g.  11;  —  airtme gätBm  hl  »i/AiäaSa  ..*'rpm^  haca  anyait- bys  maedayasnaeibyö  V-S-SS;  —  pas/aSa ..msAiol'it,,*anlarvm(s,d.)  ar>%>m  mayahe *'ffm  3*  Aaca  anyasibyS  mayaiibyü  V.  g. 29.  a)  ASn.  als  Adv.  'abseits  von  — '
20336:•  j.  mäzdräjah'ya-  n.  'Dauer  eines Monats':  antarst  tialmat  'hfm  "innerhalb (d.  i.  vor  Ablauf)  eines  Monats"  V,  5. 43;  —  ^rix^apanm  vS  'hfm  vä  V.5. la;  42.
24885:•  j.  raodah'ya-  Adj.  'licht,  hell',  Plur.  neutr. Tageslicht':  {antari)  'cake  (APn.)"'  nBii antars  (sd.)  timahe  li.68.
25066:•  j.  ratu-naya-  m.  'Laie'  (im  Gegensatz zu  'ratav):  ratus  'nasin  a^a  'nays  ratüm A.J.  13;  —    myazdavi  ratus  amyazdc n?m     'naim    ayasttim   (sd.J    daste    antara mazdayasnäis  K.3.T,  8-12.
=== which leaf ===
69 'h  unten  an- ziehen . .,  wenn  (von  unten)  nach  oben  . ." N.53.  2)    \'von    unten,    vom  Tiefland\nherkommend\''
106 " Adj.  'nicht  mangelhaft, vollkommen' :  uyamna  (sd.)  °nais  daste  Vr. J5.1.\nPu.-.  tavandnilh  (^  ei  i  abavanäak"
108 "Fmäl  Y.  J/.  21:  lies  anlari.n'.\n•  j,  +antar«.ar98am ''  Adv,  ('zwischen  den Seiten',  sva.)  1) 'innerhalb',  m"
109 'ya1ia  an\' i\'jhrka  "schädlicher  . ,  als  sonst  der  Hund\ndby  Google\n131  angraya\nyqm)  \'tam(\\V.)  V.S.ji^.         '
126 " .  .  yä  .  .  upa.dvqsaiti  V, 17;  17;  —  Aaca  'vai/ihai  Jahikayäi  .  . yä  .  .  upa.baraiti  (sd.)  Yt.  17. 5"
270 "  allgemeinster Verwendung ;  'ausfuhren,  /u  Stande  bringen, vollziehen,  schaffen,  zeugen,  bereiten,  tun': •hit  "
503 "re,  bes.  zu  Kriegszeiten  auftretende\nHautkrankheit):  tßil  t^ra  airyi  daifihävB\nfrqs  hyai  . .  HiTit  'ma  Yt  "
534 " Yt./5.S5; — sadr^m  ahmai ..yahinät saota  anasava  ..  pasca  'ma  frakika  p?r3- nsmla  °ma  staranS  danypm^a  yasmm"
713 "m  paiH.jasaili  kva  .  .  druxi yä  nasul  upa.dvqsaitil  V.^*.  69;  41-68'*;\n—  y  dim  nsit  yaozddhfnte  %risBm  a"
714 'i nsii  vindäite  kuha  . .  vfmyan  . .  matda-  V.  ü.  34.**  4)  mit  Inf.  statt  des  Verb. yamai  V.y.  35f.;  6.'
717 '  besteigen .  .  ziigein"  Y.  11.  z \'\'.\nZum  V.  yaog-,  —  ai.  vgl-  yuktay-  f.  —  Pü-  (lu F.):  äyBosn,  (luY.)'
729 'ay  an  der  Pforte  des  Winters, den  ZSp.,  indem  er  . ."  Y.  57. 12.\nPFP.  lum  V,  varp-,  eig.  "pedicandus\'.  '
823 "(statt  NP'.);  —  agtämtJ(sd.)  'fris yaval  framaratti  N._?<S'i  3g  (statt  NP.), 2/',  2j;  —  °fril  canmanqmca  p"
```


## [2026-09-05T20:29:37.317Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3230,3275p' BRT.txt"
}
```


### [2026-09-05T20:29:37.393Z] TOOL RESULT

```
PPM.  zum  V.  dab-.  —  Pu.r  admvakihä\\  — ■)  Geschr.  al  aoy'\  s.  No.  4.  —  '  Bei  DsT. •yjmmm;  ob  Druckfehler?—  JJ  Vgl.  aiaiiyS.-
dby  Google
S ;  aJiaoyo.xratav-
xralav:  —  4)  So!  DsT.  ZA.  3.  64  liest  Fva- iiiä  und  siebt  darum  in  anyatina-  (s.  Ko.  1) "nn  d^nominalif  de  a'z-a-".    S.  nach  /liavay:
•  j.  adaoyöjiratav-  Adj.  'des  Verstand untrüglich  ist':  maoyö  aki  •tus  . .  vispö.- vinvh  Vt.  i2.i'K
0  Vgl  V.  4j.  6  e,  P.  27.
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
ao'  p3wm  g>us  \K.i'j.$$;  56.  a)  mit
Ah\.'.  yal . .nöit  avat^rasay.y  aä'  hare^raii- fyÄ  tiJy,  —  m'  ia/aa'fyö  R.Vj.
KompA.  —  Vgl.  aiam-.  —  Pü.:  aiar  {Päi.  fr),
•  j.  aSairi.dahyav-  Adj.  (auch  mask.)  'der unter  dem  Land  ist* :  mi'kr?m  upairi^ahyOm ..  'yam  (ASm.)  Yt. /O.144.
Npü.;  ka  ia  jJr  i  sahrhä  ml  mlinini.
•  j.  aSairi.naema-  m.  'die  untere  Seite': "^wamca  drujitnca  niüamn  'ntpmca  Yt4-
$(>>■  ,
Vgl.  aSara.nattna-,   —  Npü.:  fuma  i  ar.
•  '}.  a8mri.z9ma-  Adj.  'unter  der  Erde, Erdoberfläche  befindlich,  sich  aufhaltend':
7'lspäis  ,  .  yäis  däman  'mäisca  (als  Subj.) upairi^maiica  YtÄ48.
Ableit.  lu  alairi+iam-;  BB.  TJ.  18.
•  '].  havqm  adasta'*  upaMat»ti..'Vyt.jg. '»  Anscheinend  sSPrM.  lu  'itä:
•  j.  a-dahma-  Adj.  'der  nicht  dahma- (sd.),  nicht  unterrichtet  ist';  saota  anasava "mö  atanu.tnai<r3  Vt./o.iaS;  —  jahi  .  . yö  xsudrh  ham.rasiwayeiti  dahmanam 'manamca  V.1S.62.
Pü.  :*  aJaim.
•  g.  a-dä-,  j.  a-8ä-  f.,  n.:  s.  unter  adä:
•  j.  a-dätay-  f.  'Nichtgeben,  Nichtdar- bringen,  Verweigerung':  «J  gJu/  ml  vas- trahe  hatö  "oditlm  vaocöit  "man  soll  nicht das  Nichtgeben  eines  wirklich  vorhandenen Fleischstücks  oder  Kleids  behaupten"  V. 4.46'*; — paoiryeheca  nH  myazdake  'oätii {]Si.) yat  mai'iydi.sar^myeAe"\inA6.zi:iz,Aa:&s man  den  ersten  My.,  den  des  jW. -Festes, nicht  darbringt"  A.  j.?;  8-12  (,  SWienAW. (17,839);  —  kat  «3  *dazi'ayasnäi  vä  .  . giul  'iaitya'"  ästryeiti  "begeht  man  da- durch Sünde,  dass  man  einem  Z>. . .  kein Fleisch  gibt?"  N.  i(?; —  •oaiti  */rilraihya-
,«(sd.)  P.56",  N.54.
Pü. ;  ai/aiiitilÄ i  s.  noch  No.  I.  —  ')  Db.  wenn
ob,Google
```


## [2026-09-05T20:29:49.605Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"adairi\\|aoairi\\|a5airi\" KLN_1966.txt KLN_1971.txt | head\necho \"=== leaf 850 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==851' KLN_1966.txt | head -50"
}
```


### [2026-09-05T20:29:51.226Z] TOOL RESULT

```
=== leaf 850 ===
nimal’,  and  av-9-pcd7ro(;,  ‘man’. See  therio-  and  anthropo-.
Theridiidae,  n.  pi.,  a  family  of  spiders  {entomol.) —  ModL.,  formed  with  suff.  -idae  fr.  Gk.  flvjpi- Stov,  dimin.  of  Arjpiov,  itself  dimin.  of  flrjp, ‘beast,  animal’.  See  therio-. therio-,  before  a  vowel  theri-,  combining  form meaning  ‘wild  beast’.  —  Gk.  Ar,pio-,  fb]pt-,  fr. Arjpiov,  ‘wild  animal,  beast,  animal’,  formally  a dimin.  of  flrjp,  of  s.m.,  which  is  rel.  to  Lesbian Gk.  9t]p,  of  s.m.,  from  l.-E.  base  ghwer -,  ‘wild, wild  animal’,  whence  also  L.  ferns,  ‘wild’.  See fierce  and  cp.  words  there  referred  to.  Cp.  also prec.  word  and  the  second  element  in  Acera- therium,Dinotherium,  Megatherium,  Nyctereutes, Oenothera,  paleothere.
theriomorphic,  adj.,  having  the  form  of  an  ani¬ mal.  —  Formed  with  adj.  suff.  -ic  fr.  Gk.  fbjpto- p.op90(;,  which  is  compounded  of  flrjpiov,  ‘ani¬ mal’,  and  uopor,,  ‘form,  shape’.  See  therio-  and morpho-.
theriomorphous,  adj.,  theriomorphic.  —  See  prec. word  and  -morphous.
therium,  combining  form  denoting  a  genus  of  ani¬ mals  (conventionally  mammals).  —  ModL.,  fr. Gk.  At- ptov,  ‘animal’.  See  therio-. therm,  n.,  British  thermal  unit  (physics).  —  Gk. Arpur,,  ‘heat’,  rel.  to  Acp|r6p,  ‘warm’,  which stands  for  *g" hermos,  fr.  I.-E.  base  *gwher-, ‘warm’.  See  warm  and  cp.  thermae,  Thermidor, thermion,  thermo-,  athermancy,  diathermancy, diathermic,  hydrothermal,  isothere,  isotherm, therm-,  form  of  thermo-  before  a  vowel, thermae,  n.  pi.,  hot  springs  or  baths.  —  L.,  fr. Gk.  A^ppai,  pi.  of  Aepjj.r,,  ‘heat’.  See  prec. word.
thermal,  adj.,  pertaining  to  thermae;  pertaining to  heat.  —  Formed  with  adj.  suff.  -al  fr.  L. thermae.  See  therm.
thermantidote,  n.,  an  apparatus  for  cooling  the air.  —  Compounded  of  therm  and  antidote, thermesthesia,  thermaesthesia,  n.,  sensitiveness  to heat  (physiol .)  —  Compounded  of  therm  and esthesia.
•thermia,  also  -thermy,  combining  form  denot¬ ing;  1)  the  state  of  heat;  2)  generation  or  ap¬ plication  of  heat.  —  ModL.  -thermia,  formed fr.  Gk.  flippy,,  ‘heat’,  with  L.  suff.  -ia.  See therm  and  -y  (representing  L.  -ia). thermic,  adj.,  pertaining  to  heat.  —  Formed  with adj.  suff.  -ic  fr.  Gk.  flipper),  ‘heat’.  See  therm. Thermidor,  n.,  the  eleventh  month  (lasting  fr. July  19th  to  Aug.  17th)  of  the  French  revolu¬ tionary  calendar.  —  A  word  coined  by  Fabre d’figlantine  in  1793  fr.  Gk.  flippy],  ‘heat’,  and Scopov,  ‘gift’;  see  therm  and  donation. Thermidorian,  n.  (French  hist.)  —  F.  Thermido- rien,  lit.  ‘pertaining  to  Thermidor'.  See  prec. word  and  -ian.
thermion,  n.,  an  electrically  charged  particle emitted  from  an  incandescent  body  (physics).  — Coined  by  the  English  physicist  Sir  Owen Willans  Richardson  (1879-1959)  fr.  Gk.  flippy), ‘heat’.  See  therm  and  -ion.
Derivatives:  thermion-ic,  adj.,  thermionics  (q.v.) thermionics,  n.  pi.,  that  branch  of  physics  which deals  with  the  emission  of  electrons  from  heated bodies.  —  See  prec.  word  and  -ics. thermit,  n.,  a  mixture  of  aluminum  with  an  iron oxide  (trade  mark)  —  G.,  formed  fr.  Gk.  flippy), ‘heat’  (see  therm)  with  suff.  -it,  fr.  Gk.  -in); (see  subst.  suff.  -ite) ;  so  called  because  of  the great  heat  it  produces  when  it  is  ignited, thermo-,  before  a  vowel  therm-,  combining  form meaning  ‘heat’.  —  Gk.  fleppo-,  flepp-,  fr. flippy;,  ‘heat’.  See  therm.
thermobarometer,  n.,  a  thermometer  used  for measuring  the  altitude  by  determining  the  boil¬ ing  point  of  water.  —  Compounded  of  thermo- and  barometer.
thermochemistry,  n.,  that  branch  of  chemistry which  deals  with  the  relation  between  heat  and chemical  action.  —  Compounded  of  thermo- and  chemistry.
thermocouple,  n.,  a  thermoelectric  couple.  — Compounded  of  thermo-  and  couple, thermodynamics,  n.,  that  branch  of  physics  which deals  with  the  reaction  between  heat  and  me¬ chanical  energy.  —  Compounded  of  thermo- and  dynamics.
thermoelectric,  adj.,  pertaining  to  thermoelectric¬ ity.  —  Compounded  of  thermo-  and  electric. Derivatives:  thermoelectric-al,  adj.,  thermoelec- tric-al-ly,  adv.
thermoelectricity,  n.,  electricity  produced  by  heat. —  Compounded  of  thermo-  and  electricity, thermoelectrometer,  n.,  an  instrument  for  meas¬ uring  the  power  of  an  electric  current  by  the heat  which  it  produces.  —  Compounded  of thermo-  and  electrometer, thermogenesis,  n.,  the  production  of  heat,  esp.  in
the  body.  —  Compounded  of  thermo-  and genesis.
thermogenetic,  adj.,  pertaining  to  thermogenesis.
—  Compounded  of  thermo-  and  genetic, thermogenic,  adj.,  relating  to  the  production  of
heat.  —  Compounded  of  thermo-  and  -genic, thermogenous,  adj.,  thermogenic.  —  Compound¬ ed  of  thermo-  and  -genous.
thermogram,  n.,  the  record  produced  by  a  ther¬ mograph.  —  Compounded  of  thermo-  and  Gk. Ypdp,p.a,  ‘that  which  is  written’.  See  -gram, thermograph,  n.,  a  self-registering  thermometer.
—  Compounded  of  thermo-  and  Gk.  -ypatpoi;, fr.  ypaepew,  ‘to  write’.  See  -graph.
thermolabile,  adj.,  unstable  when  subjected  to moderate  heat.  —  A  hybrid  coined  fr.  Gk. fllpuy),  ‘heat’,  and  L.  labilis,  ‘unstable,  waver¬ ing’.  See  therm  and  labile  and  cp.  thermostable. thermology,  n.,  the  study  of  heat.  —  Com¬ pounded  of  thermo-  and  Gk.  -Xoyla,  fr. -Xoy op,  ‘one  who  speaks  (in  a  certain  manner); one  who  deals  (with  a  certain  topic)’.  See  -logy, thermolysis,  n.,  1)  dissociation  by  heat  ( chem .); 2)  dispersion  of  heat  from  the  body  (physiol.)  — G.  Thermolyse,  coined  by  the  German  pharma¬ cist  Karl  Friedrich  Mohr  (1806-79)  fr.  thermo- and  Gk.  Xuai;,  ‘a  loosing,  a  setting  free;  dis¬ solution’,  fr.  Xusiv,  ‘to  loose,  set  free;  to  dis¬ solve’.  See  lysis.
thermometer,  n.  —  F.  thermometre,  coined  by  the Jesuit  Father  Leurechon  in  1624  fr.  Gk.  Aepirr), ‘heat’,  and  pitpov,  ‘measure’.  See  therm  and meter,  ‘poetical  rhythm’, thermometry,  n.,  the  measurement  of  heat.  — Compounded  of  thermo-  and  Gk.  -petpia,  ‘a measuring  of’.  See  -metry.
Derivatives :  thermometr-ic,  thermometr-ic-al, adjs.,  thermometr-ic-al-ly,  adv. thermophile,  thermophilic,  adj.,  ‘heat  loving’  (said of  certain  bacteria).  —  Compounded  of  thermo- and  Gk.  tpiXo?,  ‘friend’.  See  philo-. thermophore,  n.,  an  apparatus  for  conveying  heat.
—  Gk.  flEppoq)6pop,  ‘boiler’,  compounded  of flippy),  ‘heat’,  and  -9 opo;,  ‘carrying’.  See therm  and  -phore.
thermopile,  n.,  a  thermoelectric  battery.  —  A  hy¬ brid  coined  fr.  Gk.  A£pjrr),  ‘heat’,  and  L.  pila, ‘pillar’.  See  therm  and  pile,  ‘heap’, thermoplegia,  n.,  a  heatstroke.  —  Compounded of  thermo-  and  Gk.  7rXr)Yr,,  ‘blow,  stroke’, which  is  cogn.  with  L.  plaga,  ‘stroke,  wound’. See  plague  and  1st  -ia.
thermos  bottle,  thermos  flask.  —  Fr.  Gk.  Aeppoc, ‘warm,  hot’,  which  is  rel.  to  flip  pi],  ‘heat’.  See
therm.
thennoscope,  n.,  an  instrument  for  indicating differences  in  temperature  without  measuring them  in  degrees.  —  ModL.  thermoscopium, compounded  of  thermo-  and  Gk.  -ox6mov,  fr. ctxotceiv,  ‘to  look  at,  examine’.  See  -scope. Derivatives:  thermoscop-ic,  thermoscop-ic-al, adjs.
1.1  ici  Mut-m
thermostable,  adj.,  stable  when  subjected  to  a moderate  degree  of  heat.  —  A  hybrid  coined  fr. Gk.  flsppt),  ‘heat’,  and  L.  stabilis,  ‘stable’.  See therm  and  stable,  adj.,  and  cp.  thermolabile. thermostat,  n.,  a  device  for  the  automatic  regula¬ tion  of  temperature.  —  Compounded  of  thermo- and  Gk.  aTardp,  ‘placed,  standing'.  See  static and  cp.  aerostat  and  words  there  referred  to. Derivative:  thermostat-ic,  adj. thermostatics,  n.,  the  science  that  treats  of  the equilibrium  of  heat.  —  See  prec.  word  and  -ics. thermotaxic,  adj.,  pertaining  to  thermotaxis.  — See  next  word  and  adj.  suff.  -ic. thermotaxis,  n.,  the  regulation  of  bodily  heat (physiol.)  —  ModL.,  compounded  of  thermo- and  Gk.  to (£14,  ‘arrangement’.  See  taxis, thermotensile,  adj.,  pertaining  to  tensile  force  as affected  by  changes  in  temperature.  —  A  hybrid coined  fr.  Gk.  flippy,  ‘heat’  (see  therm),  and tensile  (q.v.),  a  word  of  Latin  origin, thermotherapy,  n.,  the  treatment  of  disease  by heat.  —  Compounded  of  thermo-  and  -therapy, thermotic,  adj.,  pertaining  to  heat.  —  Gk.  fleppw- tixo?,  fr.  fleppouv,  ‘to  make  hot’,  fr.  Asp  pop, ‘hot’.  See  therm  and  -otic, thermotics,  n.,  the  science  of  heat.  —  See  prec. word  and  -ics.
thermotropic,  adj.,  having  the  property  of  thermo¬ tropism.  —  See  next  word  and  adj.  suff.  -ic. thermotropism,  n.,  property  of  an  organism  of turning  toward,  or  away  from,  heat  ( biol .)  — Compounded  of  thermo-  and  tropism.
-thermy,  combining  form.  —  See  -thermia. thero-,  before  a  vowel  ther-,  combining  form meaning  ‘wild  animal,  beast’.  —  Gk.  Atjpo-, At) p-,  fr.  fl7)p,  gen.  flt)p6p,  ‘wild  animal,  beast, animal’.  See  therio-.
theroid,  adj.,  resembling  a  beast.  —  Compounded of  ther-  and  Gk.  -oEtSTic,  ‘like’,  fr.  eTSoc,  ‘form, shape’.  See  -oid.
therology,  n.,  the  study  of  mammals,  mammalogy
—  Compounded  of  thero-  and  Gk.  -Xcr-ia,  fr. -XoYop,  ‘one  who  speaks  (in  a  certain  manner); one  who  deals  (with  a  certain  topic)’.  See  -logy.
Theropoda,  n.  pi.,  a  suborder  of  carnivorous  dino¬ saurs  (paleontol.)  —  ModL.,  compounded  of thero-  and  -poda.
theropodous,  adj.,  pertaining  to  the  Theropoda.
—  See  prec.  word  and  -ous.
thersitical,  adj.,  pertaining  to,  or  resembling, Thersites;  scurrilous.  - —  Formed  with  the  suffix -ical  fr.  L.  Thersites,  fr.  Gk.  ©e-cht r,c,  name of  the  ugliest  of  the  Greeks  before  Troy,  a  man notorious  for  his  scurrility.  The  name  lit.  means ‘bold’,  esp.  ‘bold  of  speech’  (cp.  flEptnsmf)?, ‘bold  of  speech’),  fr.  Aspaoi;,  Aeol.  equivalent of  Ion.,  Old  Att.  Aapaoc,  Att.  flappoc,  ‘cour¬ age,  audacity’,  and  rel.  to  flapauc,  flpaaup, ‘bold,  audacious’,  Aaposiv,  Att.  flap  pt tv,  ‘to  be bold’,  fr.  l.-E.  base  *dhars-,  ‘to  dare,  be  coura¬ geous’.  See  dare  and  cp.  thrasonical.  For  the  end¬ ing  of  the  name  ©ep<jiT»]i;  see  subst.  suff.  -ite.
thesaurus,  n.,  a  treasury ;  a  treasury  of  words,  lexi¬ con.  —  L.,  fr.  Gk.  ifrjax'jp'jc,  ‘treasure,  treasure- house',  a  compound  whose  first  element  prob. derives  fr.  -!>/]-,  ‘the  stem  of  -n.9evai,  to  place, put'  (see  theme) ;  the  second  element  is  of  uncer¬ tain  origin.  Cp.  treasure, these,  demonstr.  pron.  —  ME.  thise,  these,  fr. OE.  pies,  ‘these',  a  collateral  form  of  pas,  pi.  of pes,  ‘this'.  See  this.  OE.  pas  survives  in  E.  those (q.v.)
Theseus,  n.,  the  most  famous  hero  of  Attica,  son of  Aegeus  ( Greek  mythol.)  —  L.,  fr.  Gk. ©tjcjeu;,  which  is  of  unknown  etymology, thesis,  n.  —  L.,  fr.  Gk.  (Hot;,  ‘a  placing,  setting’, fr.  I.-E.  *dhc-ti-,  whence  also  Ol.  -(d)hitih  (only in  c
```


## [2026-09-05T20:29:59.841Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if 'under,  prep' in p or 'under, prep' in p or ('undergo' in p and 'undern' in p):\n        print(\"LEAF\",i)\n        import re\n        j=p.find('under')\n        print(p[max(0,j-200):j+1500])\n        break\nEOF"
}
```


### [2026-09-05T20:30:01.701Z] TOOL RESULT

```
903
LEAF 888
ts  are  of  Greek  origin, undecennial,  adj.,  occurring  every  eleventh  year. —  Formed  fr.  L.  undecim,  ‘eleven’  (see  prec. word),  with  suff.  -ennial,  on  analogy  of  decennial (q.v.)
under,  prep.  —  ME.,  fr.  OE.  under,  rel.  to  OFris. under,  OS.,  Goth,  undar,  ON.  undir,  Dan., Swed.,  OFris.  under,  Du.  onder,  OHG.  untar, unter,  MHG.  under,  unter,  G.  unter,  fr.  I.-E. *ndher,  ‘under’,  whence  also  OI.  adhah,  ‘below’, adharah,  ‘lower’,  Avestic  adara-,  ‘lower’,  Toch. A  and,  ‘under’,  Arm.  lnd,  ‘under’,  L.  inferus, ‘lower’,  infra,  ‘below’  and  perh.  Gk.  aOepi^eiv, ‘to  make  light  of  (for  sense  development  cp.  OI. adharina-,  ‘despised,  made  light  of’,  fr.  adhah, ‘below’).  Cp.  inferior,  infernal,  infra.  —  Cp.  also I.-E.  *nter,  ‘between,  among’,  whence  OE.  un¬ der,  OHG.  untar,  Goth,  undar,  ‘among’,  OI. antar,  ‘among,  between’,  L.  inter,  ‘between, among’,  Gk.  evxepa,  ‘intestines’.  See  inter, prep.,  and  cp.  words  there  referred  to. Derivatives:  under,  adv.  and  adj. under-,  pref.  —  From  prec.  word, undercroft,  n.,  a  crypt.  —  Compounded  of  under and  obsol.  croft,  ‘vault’,  which  is  borrowed  fr. VL.  crupta,  fr.  L.  crypta,  fr.  Gk.  xpujrxr,,  ‘crypt, vault’ ;  see  crypt.
undergraduate,  adj.  and  n.  —  A  hybrid  coined  fr. under  and  graduate,  a  word  of  Latin  origin.
undercurrent,  n.  —  A  hybric  coined  fr.  under  and current,  a  word  of  Latin  origin, underestimate,  tr.  v.  —  Loan  translation-  of  F. sous-dvaluer,  a  word  coined  by  the  French  poet and  critic  Pierre-Charles  Baudelaire  (1821-67) fr.  F.  sous,  ‘under
```


## [2026-09-05T20:30:26.481Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,glob,re\nfor f in sorted(glob.glob('page-*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for rc in e.get('ref_check',[])+[r for n in e.get('nodes',[]) for r in n.get('ref_check',[])]:\n            if rc['ref'].startswith('KLN'):\n                print(f, rc['ref'], rc['status'], rc['note'][:220])\nEOF"
}
```


### [2026-09-05T20:30:28.204Z] TOOL RESULT

```
<persisted-output>
Output too large (69.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b47erv163.txt

Preview (first 2KB):
page-100.json KLN:163 supports KLN_1966.txt form-feed leaf 97 (printed pp. 163-164, running numerals '170 171' appear at leaf 101): "ben, n., son. — Heb. ben, 'son', rel. to Arab. ibn, Aram.-Syr. bar, 'son', Akkad. binu/bini, 'grandson'. Cp. Benjamin,
page-100.json KLN:163 supports KLN_1966.txt form-feed leaf 97 (printed pp. 163-164, running numerals '170 171' appear at leaf 101): "ben, n., son. — Heb. ben, 'son', rel. to Arab. ibn, Aram.-Syr. bar, 'son', Akkad. binu/bini, 'grandson'. Cp. Benjamin,
page-100.json KLN:163, 164 supports KLN_1966.txt leaf 97 covers both printed pages: p. 163 'ben, n., son. — Heb. ben, "son" …' and p. 164 'Benjamin, masc. PN.; in the Bible, Jacob's youngest son. — Heb. Binyamin, lit. "son of the right hand", fr. ben "son"
page-100.json KLN:163 supports KLN_1966.txt leaf 97 (p. 163-164): 'ben, n., son. — Heb. ben … Cp. Benjamin, B'nai B'rith, boanerges' and 'Ben, masc. PN. — Dimin. of Benjamin (q.v.)'; Big Ben is treated a few pages on (leaf 101/102) and is referred bac
page-101.json KLN:164 supports KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, from the stem of bērākh, he blessed, which is rel. to Aram. bārākh, Arab. bāraka, Ethiop. bārāka, he blessed, Akkad. karābu (a metath
page-101.json KLN:164 supports KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, from the stem of bērākh, he blessed, which is rel. to Aram. bārākh, Arab. bāraka, Ethiop. bārāka, he blessed, Akkad. karābu (a metath
page-101.json KLN:274 supports KLN_1966.txt leaf 155 (printed pp. 274-275), s.v. 'cherub': 'Heb. kerūbh, winged angel, prob. rel. to Akkad. karābu, to bless, karibu, one who blesses, epithet of the bull-colossus, and to Heb. bērēkh, he blessed, berākh
...
</persisted-output>
```


## [2026-09-05T20:30:38.828Z] TOOL CALL #23: Bash

```json
{
 "command": "ls site/pages/154.jpg 2>/dev/null; pdftoppm -f 154 -l 154 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg154 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T20:30:41.054Z] TOOL RESULT

```
site/pages/154.jpg
total 15356
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:30 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
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
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:30:44.179Z] TOOL CALL #24: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg154.png"
}
```


### [2026-09-05T20:30:44.590Z] TOOL RESULT

```

```


## [2026-09-05T20:30:44.584Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:31:11.703Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 852 853 854 855; do echo \"----- leaf $n -----\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | head -c 400; echo; done"
}
```


### [2026-09-05T20:31:13.756Z] TOOL RESULT

```
----- leaf 852 -----
,  ‘incense’,  9uo<;,  ‘burned  sac¬ rifice’  (whence  L.  thus,  gen.  thuris,  ‘frankin¬ cense’),  9up6 p,  ‘spirit,  breath,  life,  mind,  soul, desire,  courage,  anger',  OOstv,  Ouia^Eiv,  ‘to rage’.  Cp.  thanato-,  Thuja,  thurible,  Thyiad, thyine,  thyme,  thysano-,  tumble,  typhlo-,  typhus, the  first  element  in  Thymelaeceae  and  the  second element  in  athym
----- leaf 853 -----
thorax.  —  Gk.  ffcopaxo-,  -Ucopax-, fr.  gen.  •Bcopaxoi;.  See  next  word,
thorax,  n.,  part  of  the  body  between  the  neck  and the  abdomen  ( anat .)  —  Gk.  •fleipa^,  gen.  ffo>- paxop,  ‘breastplate,  breast,  chest’,  of  uncertain origin.  It  is  perh.  cogn.  with  OI.  dhdrdyati, ‘holds',  from  I.-E.  base  *dher-,  *dhere-,  ‘to hold’,  whence  also  Gk.  
----- leaf 854 -----
odi-al,  threnod-ic,  adjs.,  thren- od-ist,  n.
threpsology,  n.,  the  science  of  diet.  —  Compound¬ ed  of  Gk.  S-pe^i?,  ‘nourishment’,  and  -Xoyla, fr.  -X6y o?,  ‘one  who  speaks  (in  a  certain  man¬ ner);  one  who  deals  (with  a  certain  topic)’.  The first  element  is  a  derivative  of  xpetpsiv,  ‘to  feed, nourish’ ;  see  next  word.  For  the  second  elem
----- leaf 855 -----
,  ‘deceiver’,  fr. OI.  sthagah,  of  s.m.,  fr.  sthagati,  ‘conceals’, which  is  cogn.  with  Gk.  axbfci v,  L.  tegere,  ‘to cover’.  See  thatch.
Derivatives :  thuggee  (q.v.),  thugg-ess,  n. thuggee,  n.,  murder  as  carried  out  by  thugs.  — Hind,  thagi,  fr.  thag,  ‘a  deceiver’.  See  prec.  word. Thuja,  n.,  a  genus  of  plants,  the  arbor  vitae  (but.) —
```


## [2026-09-05T20:31:23.986Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD azer ===\"; grep -n \"azēr\\|azer\\b\\|ʾcyl\" PHD.txt PHD_mackenzie.txt | head -10\necho \"=== PHD andar ===\"; grep -n \"^andar\\| andar \\b\" PHD.txt | head -5\necho \"=== PHD estad ===\"; grep -n \"ēstād\\|estad\\|ēst-\" PHD.txt | head -10\necho \"=== PHD ewar ===\"; grep -n \"ēwar\\|ewar\\b\" PHD.txt | head -10"
}
```


### [2026-09-05T20:31:24.086Z] TOOL RESULT

```
=== PHD azer ===
PHD.txt:227:azbāy- [*2b*d-] invoke. ~išn: invocation. azd [zd | = M] known. Azdahag Pcydi’k' | M ?zdh?g, (N aždahā)] a legendary ‘dragon’ king, Dahāg. azdénidan, azdén- Pzdyn-ytn'] inform. azēr [%cdl | N zér] below, under. azg [22 | N аху) branch. aziš [hcf | М *cy$, 22у] from him, it; postposition (= az) from, ~-keh [-ks] inferior, subordinate. ~-meh [-ms] superior. āz-kāmaģ [?ck’mk'] greedy. ~ih: greediness. azmüdan, azmāy- ['zmwtn!,?zm'd- | N 2~] = uzmüdan. aznawar Pzrw/l | M ?zn] noble. azraw-, v. azruftan. azray- ['zr'd-] adorn. azruftan, azraw- [)zlwp-tn! | M *zrw-] go out, be extinguished. āzurdan [Pcwltn! | N ~] = āzārdan, āzwar [?*cwl | N ~] greedy. ~ih: greed.
PHD.txt:975:below ēr, azēr.
PHD_mackenzie.txt:1428:azer [hedll N zir] below, under.
PHD_mackenzie.txt:2210:ler [)dll M )yr, v. azer] down, below; low; under.
PHD_mackenzie.txt:6060:below er, azer.                             blissful huram.
PHD_mackenzie.txt:7859:under azer, er.                          unworthyanarzanig.
PHD_mackenzie.txt:11438:abusih; iibusih             ~\o-              aber; azer                 ~t)t
=== PHD andar ===
1286:andar ámadan; ~ to, upon abar rasidan; ~ to an end 6 ham madan.
1367:contained, be — in andar büdan.
3012:outstrip andar widardan.
3595:set hištan, nišāstan; (sun) andar Sudan,
5524:andar!
=== PHD estad ===
164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
942:be būdan, ēstādan, h-.
3799:stand awištādan, ēstādan, pādan: ~ up āxistan.
4523:ālag! šahrewar šahr frést-t šahryār šahryārīh fréstidan! šahrestān frēstādanī álag!
4555:jaw! Jawēnī šēwan frēst-Ī frēstādan? hil-t hilišnī hištanī šagr, šīr šīrēnīh šīrēn šēb šēb- šēbāg šēbišn šīšag šēdā šēd uzwānī šnāxtan šnāy- šnās- šnāyēn- šnāyēnīdan
=== PHD ewar ===
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
912:backgammon nēwardaxšīr.
1186:certain a- | abē-gumān, ēwar, tāštīg.
1187:certainly ēwar.
2864:move ēwarzīdan, jumbidan, raftan, wazidan, wihēz-; — quickly šēb-; cause to — jumbēnīdan, wāzīdan.
2880:myriad bēwar.
4384:Amahraspandan Wahman Ardwahišt (Urd-, Ašwahišt) Šahrewar Spandarmad Hordād Amurdād
4388:I Frawardin II Ardwahišt III Hordad IV Tir V Amurdad VI Sahrewar
4392:3 Ardwahist 4 Sahrewar
4523:ālag! šahrewar šahr frést-t šahryār šahryārīh fréstidan! šahrestān frēstādanī álag!
```


## [2026-09-05T20:31:32.678Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ewar headword ===\"; grep -n \"ēwar \\[\" PHD.txt PHD_mackenzie.txt | head\necho \"=== PHD estadan headword ===\"; grep -n \"ēstādan, ēst-\\|ēstādan \\[\\|estadan \\[\" PHD.txt PHD_mackenzie.txt | head\necho \"=== NYB ===\"; grep -n \"ēwar\\|ēstāt\\|azēr\\|ayār\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T20:31:32.750Z] TOOL RESULT

```
=== PHD ewar headword ===
=== PHD estadan headword ===
=== NYB ===
445:motion: šutan, dväristan, opastan, ete., and with ēstātan and nisastan (also ~ 6). — 2. prep. in, local, temporal and figura- tive: ~ Pārs; ~ im xünak P1:6; ~ miyàn i in the middle of 865; ~ han hangam at the time 613; ~ ham zamān at the same time 127°; ~ zamān in due time 221, etc.; ~ sap in the night 529, 614; ~ hàsr for a single moment 663; ~ hàn in the meantime 5615-17; — xtatäyeh + Xösrör 1184; ~ Vistasp šāh kisvarikan when V. was the emperor of the world 365; — freftür ~ : concerning 3419-20, 10923; spasdārēh ~ , an-ispās ~ : to, against; with other substantives, v. these separately ; — together with another prep.: ~ 6 into, on to, up to: ~ 6 nun 404; with apakandan, burtan, guméxtan (also without 6), hištan, kartan (v.s.v. kar); apar ~ 402, — Av. (131 sq.) antara, antarš, OP antar (better read antara^); MPrthPrs ’ndr; Paz. NP andar; v. also niyandar.
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
509:apar-āstišnēh [’pl’stSnyh] the act of ac- cepting and taking care of: ~ % én den rād 589, with the gl. kū tà? pat én den bē éstat (subju. 3d p. sg., v. estátan) ; 5919. — < apar + ēstātan; as to the alternation é-: à- cf ästenisn.
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
1456:ēstišn [Pystšn', ystšn'] v. n. of ēstātan, used as pred.: has to, must stand fast, persevere 65’; subst. persistence 34?!; standstill, cessation of progress, of the stars 57. — V. also dstisn(éh).
1934:*hārēftan [h'lyptn'] *hārēf-; [h'lyp-] 1. to mix, referring to the coition 4315: after ēvak apar, apāk dit, apar ēstāt hend 6 én kar 4314-15 (v. ?apük 2) the narrator continues api-šan MDM hareft: as the construction is pass. we expect here a subj.; this is probably hidden in MDM which is, in that case, the wrong ideogr. for aw. ’pl = "pr or ?c] = "cr, or the like, signifying ‘the genital fluid’ : the fluids from their genital organs were mixed together, with the gl. kū-šān pat takoš (g. v.) frac grift ‘that is: they clasped tightly’. — 2. to infect: api-š 61 dit Zartuxst pas andarg haxt ka hārēft ēstāt purr gaz (etc.) and Z. saw her from behind, between her thighs, (and saw) that they were in- fected, full of snakes (ete.) 5726-581, — 3. to attach, to assign a th. to (6) a p,: whenever Pourušāsp desires to have a divine service ‘performed yazišn 6 yas- taran härefät he shall assign the service to (true) ministrants 5314-15, with the gl. ki 6 yazāt ke apāyet yastan that is: that one shall perform the divine service to whom it pertains to perform such service’, ef s. v. bahr. — (1483) ham.raedwayeiti ‘to mix, to mingle, to infect’, from which the signi- fication ‘to attach’ was easily derived (cf the simplex vb. in the expression kahrpam raēdwayeiti ‘assumes a visible shape’ Yt. 813); a den. of rae0wa- ‘mixture, muddle’. *ham-ra- > hara-, cf (1529) rgroma- < *ramrama- (the Av. spelling ham- is a compromise between hq- and ham-); *har- in Milr > har-. The Milr vb. be- longs to the NW linguistic area: raēdw- > réf- is a normal NW development. As the vb. is a den., the pres. st. kārēf- must be regarded as the primordial form, and
1973:hayyar [hdyb?l] helper 253. 84%; pl. cas. rect. ~ 106%, hdyb?l F:7 (reading settled by Henning); pl. cas. obl. ~-dn 461. — The spelling hdyb’l is also evidenced by the Ps., v. next w.; v. I, 136 H. — SW form; MPrs hy(y)’r (S, A-H I); FrP, Cod. S, I, 18 with the gl. (NP) xiyär; Paz. ayār; NP yar; — hayyär with secondary aspi- ration < *adyār < adyävar, the NW form: MPrth ’dy’wr, Mand. lw. ’dy’wr’, going back to OlIr *adydva-bara-, cf Av. (61) aidyü- ‘helpful, useful’. Szemerény, JAOS 70, 1950, 226-229.
2281:. he whose virtue and sin are equal 7924-25; seldom % ke: cigon mart-ē ké-§ vēhēh veš u ēvak i ke vēhēh kam as a man whose goodness preponderates and an- other whose goodness is deficient 96°’ ; — it cannot be governed by a prep.; in such cases, a) the prep. is placed in the rel. clause and governs a dem. pron. referring to the antecedent: (dätär) ke hac & aštak veh (the Creator) from whom a good Messenger (has come) 5711; ke... hac ēišān ēvak ravēt (the three sons of Zartuxšt) of whom one ... shall appear 7115-16, 181; kē-š pat han urvar bē barēt [YDLWN-x-] by which he removes the plants 569-10; han kas ke yuvat hac či nē vicarét the man without whom you will not get on 416-1’; b) the prep., changed into an adv. and assuming its special form if there exists any, is placed in the rel. clause and may refer directly or through an encl. to kč: hàn ke én x"amn patiš dit the one about whom this dream was dreamt 21-9 (patiš for pat referring to ke); Hutös ke ... 30 haciš zàt H. of whom 30 children have been born 24? (haciš for hac); han gàv pem kē tan gohr à Zartuxst avis mat ēstāt the cow-milk into which the bodily element of Z. had entered 4225-26 (avi$ for 0); hamäk cis ke-š martömän rämisn ... haciš everything from which men derive pleasure 10020-21 (haciš for hac referring to ke through the intermedium of the encl. -š in ke-$); han keš pātiyāvandtar kē-š pätix$äych apāk bavēt that religion is most powerful to- gether with which there is royal power (which is joined with royal power) 8018-12 (apak here adv., referring to ké through the intermedium of the enel. in ké-8); béstan-é ke-š hamäk urvarihā u spramīhā andar a garden in which there are all sorts of plants and flowers 105! (ké-§ . . .
2752:nipistan [npštn'; YKTYBWN-tn'] nipés- to write 419. 110? etc. ; nipist estet it has been written, it is written 1139; nipist ēstāt it was written 1!—?; — pres. pass. nipēsihēt [YKTYBWN-yhyt'] is being written 18%; — pat dp i zarr nipištak 1079; apar nipistak written down 108?!; nāmak ~ 6 to write a letter to 49-9. 822, an inscription P 2:3.4; apar fravartak čton nipišt estat kū it was written in the letter (then dir. speech) 1872; apar én ayyätkär nipišt estet 1135-9. — OP ni-pais- ; MPrthPrs nbyštn nbys-; Paz. nawaštan nivés-; NP nuvistan, nivištan, nivés-.
2771:nivistan [nwstn'] to announce: ka... 6 Ohurmazd nivist ēstāt after this had been announced to O. 431-2, — Av. (1317 sg.) ni-lvačd-.
2952:par-ēstātan [pl YK‘YMWN-tn'] to go and stand in front of (pēš) a p. in order to protect him: peš Zartuxšt par-ēstāt 4919-20, — pari + ēstātan, cf Av. (1603) pairi-stä ‘to check, to prevent, to with- hold’.
2961:paristätan [plst’tn'], paristitan [plstytn'] parist- to worship, to adore, to submit to, to embrace (a religion) 194. 7511, 82.12, — < pari + stā-, v. ēstātan and cf par- ēstātan; Prth *part-štā- in Arm. lw. am- barišt ‘impious’ < Arm neg. an- + *parištā-, pastaun < *parštaun < "pariš- tamna- (middle pt.) ‘cult, service, office’, past-em ‘to worship’; in SW with -st- > -st-: MPrs pres. pryst-, and the inf. assum- ing the SW ending -ītan (cf MPrth pwrs'dn: MPrs pwrsydn, etc.): Paz. pa- rastidan parast- = NP; Verbum 194 sq.
3088:pattän [pt’n'] continually, uninterrupted- ly, right on to (6) 209; [ka Gäyömart hac x"& früc but dit... spihr 6 gartisn, x'aréet u mah 6 ravisn ēstāt u ~ hend when G. woke up from his sleep he saw that the vault of heaven had begun to turn, and Sun and Moon to move, and they are still (in turning and moving) BdA p. 44 5-?; possibly written PWN ZK KnS VI, 4, but the text is not sure]. — < *pati-tāvana- from pati + tav-, v. the preceding w. Parallel with the series pattāt, pattūk (v. this w.), pattān is the series with the prev. *ati-: *attāk < *ati-tävaka-, Arm. lw. atak ‘capable’: attūk < *ati-tuvaka- id.: attān < "ati- tāvana- ‘solvent’ (attānīk DkM 139—140, opp. an-attān 'insolvent'). Cf Bthl., MirM III, 15, ZsR III, 53. — Cf ham-tak, tāhēkār, tāk, tāyītan, tuvān.
3201:. raftan to keep company with, to communicate with 702-8; — apar én zamik ravét he moves on this earth 3333; apar zanišn raft hend they went to slay (him) 4515-16. — hac from 62. 569.809; — 6 to 3726, 385-9 etc. passim ; — pat gehän *hamāi raft hom I roamed the world all about 318-9 (kame would not suit the context; cf 952° s, v. hamäk); — with prev.: andar ~ : ka srav ... 0$ (prep.) mart (+...) andar rajt ēstāt when the report had reached that man (who ...) 4424-26; došar"% ... andar 6 [KN] ravét will move, roam freely in Hell 347-8; — apar ~ : 6 õi ket apar raft hénd they went off to the sooth- sayer 379; 3811-15, 415, ete. — be ~ : fra- tom 6 änöd apar raft, avdom be raft (he was the first to step in there) and the last to step out 496-?-20; 5714-15; pas patvand hac oisan be raft then offspring proceeded from them 941°; very often bē only indicates the aspect: ētēn sart bē raft i-š ... went ahead so vehemently that 3315; bē rav! 6019; adak ēišān bē raft hend 5712; — frac ~ : frac raft Pourusäsp
3286:ravišn [Iwbšn'] l. pred.: apar-ip-im — I must ascend 4076. — 2. v. n. motion: ēstišn u ~ i stārakān station and motion of the stars 57; motion of the sun, of the moon and of the stars 872-22, 881, 8918; pat ~ ēstāt was in motion 9315-19; nıhän- ~ whose going is clandestine = sneaking 1038.
3536:startéh, sturtéh [stwltyh] swoon, torpor 541.8.12, 1031? (cf ēstātan + frdc).
5365:(abi-)-stā-: ēstātan
```


## [2026-09-05T20:31:39.468Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ēstātan\\|ēstātan \\[\\|estatan \\[\" NYB_vol2_glossary.txt | head\necho \"---\"; grep -n \"ēvar\\|évar\\|ēwar\" NYB_vol2_glossary.txt | head -10\necho \"--- azer/er ---\"; grep -n \"^ēr \\[\\|azēr\\|acēr\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-05T20:31:39.539Z] TOOL RESULT

```
2952:par-ēstātan [pl YK‘YMWN-tn'] to go and stand in front of (pēš) a p. in order to protect him: peš Zartuxšt par-ēstāt 4919-20, — pari + ēstātan, cf Av. (1603) pairi-stä ‘to check, to prevent, to with- hold’.
---
377:| Sahrévar, Harvadat, Amurdat and Span-
916:bar [bl] fruit 661%; as to 38 v. évar. — Ps. bly; Paz. NP bar, but MPrthPrs b?r. '
995:bevar [bywl] ten thousand; 2 — späh an army of 20000 men 1811-16-17; 12 ~ späh 29233; won 15 ~, 14 ~, 13 ~ 2372.17, 248-11; 131 ~ ziön äyend 24115; 12 x 12 ~ 2427; 12 ~~ 251; 3 ~ nēzak (g. v.) balas 1041, — Av. (913) baévar-, baévan-; MPrth- Prs bywr ; Arm. lw. biur; Paz. baévar ; ear- rly NP bevar.
996:Bévar-asp [bywl’sp'] n. pr. 78%. — Paz. Baévardsp; NP Bévarasp.
1467:évak [HDwk'; on coins *ywky] num. one, passim; hàn + ~ Arjäsp A. alone 2416, 2927; ~ ~ one by one 92$; har ~ every- one 1045-%, 10617. 11318; ~~ bēvar ten thou- sand 244; 3 ~ one third 6329-22, 9316, 1025; 4 ~-é [-’y] one fourth 998; 5 ~-é [^y] 10015-17, 10227. 1031-2; — in correspon- dence with dit, ditikar, ane, v. these ws. — Av. ačva-. OP awa- + -ka-, v. s. v. žē; MPrs yk; Paz. yak, iak, NP yak — as against MPrth ‘yw ‘one’, *ywg ‘alone’.
1470:évar ['dwl; 3% incorrectly y bl] adj. true [duat ~, with the gl. kū ke mat zat a true daughter, i.e. whom the mother has born PR 135-$:] adv. verily, certainly 38. — FrP 25: ’dwl : *ywl. Paz. čvar; NP ävar ‘true, certain’. V. also ēvarihā.
1471:évar ['dw'lj plundering, pillage: ~ u róp 10829, — KZSPrth 1. 16 ’w’r, Prs. equiv- alent, last w. of 1. 20, not quite clear, but possibly ’dw’ly, Gr. v. &prayn; Arm. lw. awar ‘booty’; Mand. lw. ^w?r *plun- dering’, Bal dvdr ‘spoil, plunder’, NP
1474:s. v. lēvāc, ēvar.
1476:ēvarihā ['dwlyh?] truly 8021. — Paz. sub- stitutes awäharihä, Skr. v. samyak-yatayä.
1477:ēvarz ['dwlc'] review, muster, as a mili- tary term: ~ kartan to review, to muster (an. army) 2014; — [hence ēvarzīk kas probably *a man called up for military service, DkM 750!?]. — Originally ‘com- putation, calculation, account’, ef the following examples: ~ 4 x“atdydn 6 osti- kan the rulers’ calling of their trustees to account DkM 40416; étar *zarvan i (K drang) àivan (< K) andak, ~ züt; änöd dātavār (!) rāst here (in this world) the term of the court is short, and the account swift; there (in heaven) is & righteous *judgment DkM 5481-11; apar hān 4 andar nihvārēh ~ about the items (necessary) in combat FrP 14, heading. In all probability to be connected with NP dvàr(ah) ‘calculation, reckoning; an account-book’ (of which dvārjah, dvarcah ‘a cash-book, a book of receipts and dis- boursments, a diary, or register’ is the diminutive) < *abi-varda- SW form of *abi-varza-; dvdr : ēvarz, cf ēvāc, Evar, évar. (Wrong interpretation by Nyberg, TMK 69 sq., Pagliaro, Iscr. Dura-Europo 592. 595). — From varz-, v. varz, varzitan.
--- azer/er ---
```


## [2026-09-05T20:32:07.192Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:32:07.199Z] TOOL RESULT

```


```


## [2026-09-05T20:32:11.430Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%B1",
 "prompt": "Give the Persian etymology section for زیر 'under, below' verbatim: Middle Persian form, Proto-Iranian reconstruction, Avestan comparanda, and any cited authorities."
}
```


## [2026-09-05T20:32:12.299Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D8%B1",
 "prompt": "Give the Persian etymology of اندر 'in, inside' verbatim: Middle Persian, Old Persian/Avestan, Proto-Iranian, PIE, and cognates."
}
```


### [2026-09-05T20:32:17.942Z] TOOL RESULT

```
# Persian Etymology of زیر

Based on the Wiktionary entry, here is the etymology section information:

**Middle Persian form:** The entry indicates Middle Persian \[script needed\] (hcdl /⁠azēr⁠/, "underneath")

**Proto-Iranian reconstruction:** The word derives from Proto-Iranian *háčaH ("from") and *(H)adárah ("under")

**Old Persian component:** The etymology traces to Old Persian *hacā-adari, combining:
- 𐏃𐎨𐎠 (h-c-a /⁠hacā⁠/, "from")
- *adari ("under")

**Proto-Indo-European roots:** The entry references *sékʷ-eh₂ and *(H)n̥dʰ-ér-o-s, noting the word is "distantly related to English *under*"

**Note on Avestan:** The source document does not provide Avestan comparanda or citations to specific authorities beyond general etymological reconstruction frameworks. The references section lists historical philological sources but no Avestan cognates are explicitly mentioned in the etymology section itself.
```


### [2026-09-05T20:32:18.619Z] TOOL RESULT

```
# Persian Etymology of اندر (andar)

Based on the Wiktionary entry, here is the etymological chain:

**Middle Persian:** "𐭡𐭩𐭭 (BYN /⁠andar⁠/)"

**Old Persian:** "𐎠𐎫𐎼 (a-t-r /⁠aⁿtar⁠/, 'among, within')"

**Proto-Iranian:** "*Hántarah"

**Proto-Indo-European:** "*h₁énteros ('inner, what is inside')"

The entry notes that the Persian term descended from the Old Persian root meaning "among, within," which itself derived from earlier Indo-European layers. The modern Persian preposition represents an archaic and poetic form, with the shortened "در (dar)" becoming dominant after the twelfth century, though "اندر" persists in poetry for metrical purposes.
```


## [2026-09-05T20:32:24.770Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%B3%D8%AA%D8%A7%D8%AF%D9%86",
 "prompt": "Give the Persian etymology of ایستادن 'to stand' verbatim: Middle Persian form, Proto-Iranian/Old Iranian reconstruction, prefix analysis, and cited authorities."
}
```


## [2026-09-05T20:32:25.878Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B1%DB%8C",
 "prompt": "Give the Persian etymology of آری 'yes' verbatim: Middle Persian form, any Old Iranian reconstruction, and cited authorities."
}
```


### [2026-09-05T20:32:30.889Z] TOOL RESULT

```
# Persian Etymology of ایستادن

**Middle Persian Form:**
"YKOYMWNtn' /⁠ē̆stādan⁠/" (from Middle Persian, requiring script specification)

**Proto-Iranian Reconstruction:**
The verb derives from Proto-Iranian "*staH-" meaning "to place, stand," ultimately traced to Proto-Indo-European "*steh₂-" with the same sense.

**Prefix Analysis:**
The entry does not employ a separable prefix. The verb consists of the root stem (ایست) combined with the infinitive marker (-ن).

**Cited Authorities:**
1. MacKenzie, D. N. (1971) — *A Concise Pahlavi Dictionary* (Oxford University Press)
2. Cheung, Johnny (2007) — *Etymological Dictionary of the Iranian Verb* (Brill)

The etymology demonstrates inheritance from Middle Persian through Old Persian and Proto-Iranian branches of the Indo-European language family.
```


### [2026-09-05T20:32:32.137Z] TOOL RESULT

```
# Persian Etymology of آری (yes)

Based on the Wiktionary entry, here is the verbatim etymological information:

**Middle Persian form:** The article states it is "Possibly inherited from Middle Persian \[script needed\] (ʾywl /⁠ēwar⁠/, 'certainly, assuredly')"

**Old Iranian reconstruction:** "from Old Persian \[script needed\] (adi-var, 'in truth, indeed')"

**Cited authority:** The etymology cites "Nourai, Ali (2011), An Etymological Dictionary of Persian, English and other Indo-European Languages, page 124"

**Note:** The entry indicates that both the Middle Persian and Old Persian forms lack their original scripts in the source document, denoted by the "[script needed]" placeholders.
```


## [2026-09-05T20:32:38.674Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ēstād\\|estad\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:32:38.741Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:32:39.383Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB istadan/andar ===\"; grep -n \"istäden\\|estäden\\|ender\\|andar\" HUB.txt | head -20"
}
```


### [2026-09-05T20:32:39.432Z] TOOL RESULT

```
=== HUB istadan/andar ===
545:120. Vgl. afgh. plandar *Stiefvater von plar 'Vater' wie np.
546:pidandar von pid = pidar. ^)
547:121. Np. andarx^ar *passend' stimmt nicht gut zur Wzl.
807:uWy aw werden musste. So kann auch t>ai (in andar-
1654:LW. tandar *Donner , echt afgh. ^aw^'Donner (Geiger).
1725:jandar 'a mill, millstone*, das nach Dames = sindhT
1727:auch xM^.jandara Tresse zum Glatten von Zeug' etc.
2094:546. Np. dar 'hinein, in' aus andar wie darun aus andarUft,
2095:darx^'ar aus andarx^ar. Vgl. deutsch raus = heraus,
3804:17. Lies andarmahj ys. 1, 24 u. s. w.
4099:ap. *duxtd neben duxtar -— ap. *diixtaram (vgl. auch pad-andar *Stief-
4100:vater', mdd'andar *Stiefmutter*, duxi-andar *Stieftochter' JRAS. 1894,
4374:sind: me aus tiame (Horn Nr. 1104), dar aus andar, vgl.
4407:muy- in muyanandarzbad (Hoffmann, Ausziige p. 50), phi.
4548:anderjapet^ handerjapet neben andarj 'Testament' = np.
4554:vor h und r. Ausserdem: Spandaramet (fiir gr. /liowaoQ)
6155:anl. sp, st, sk etc. geblieben ist 2) (vgl. Spandaramet, Span-
6734:andar 'in' = phi. andar, zd. antare; vgl. phi. andarmOh (im
6735:Jasna) = zd. antaremdnha-; phi. andarvdi *Atmosphare'
6747:mqdrem spentem; np. Sipanddrmad = phi. Spandaramat— 191 —
```


## [2026-09-05T20:32:45.284Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"staH\\|\\*stā-\\|awestādan\\|ēst-\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:32:45.334Z] TOOL RESULT

```
11017:sim., go back to *fra- + *staH. 
23400:358 *staH 
23411:*staH ‘to place, set; [intr.] stand’ 
23455:*staH 359 
23506:360 *staH 
23573:*staHn ? ‘to take’ 
23598:© This root is perhaps originally a pres. n-stem of *staH (?). 
23995:instance, *staH ‘to place, set, stand’ and *@ra(n)é ‘to (op)press'. 
55885:*parH?. (s.v.), *staHn (s.v.), 
57368:*daH’, *kan', *staH 
57789:*staH 
57980:*pad, *staH, *uindar 
58114:*staHn
```


## [2026-09-05T20:32:48.081Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23400,23520p' CHEUNG.txt | grep -n -i \"MP\\|Pers\\|ēstā\\|ist\\|awest\" | head -40"
}
```


### [2026-09-05T20:32:48.133Z] TOOL RESULT

```
17:|| (+ *ni-) ‘to order’ || (+ *ham-) ‘to come into existence’ = Liste: 64 
19:Pres. them. red.: IND. med. Zeg YAv. histahe (V 3.29), 3sg. Y Av. histaiti (Yt 8.9, Yt 8.32), ҮАУ. раш 
20:histaiti (Yt 10.36), med. YAv. histaité (Y 42.4, etc.), YAv. fraxstaite (Yt 10.107, Yt 19.92, V 15.45), 3р1. 
21:YAv. histanti (Yt 6.1, Yt 7.3, V 5.19, etc.), YAv. ham.histonti (Yt 8.32), med. YAv. histante, INJ. 3sg. 
22:Y Av. upa.histat (Yt 17.21), ? OAv. "axstat (Y 51.4), med. 3sg. YAv. fraxstata (Yt 13.97), med. 3pl. YAv. 
23:histonta (Yt), SUBJ. 159. ҮАУ. xsta (Y 12.3), med. 1sg. YAv. fraxstane (Y 9.20), 3sg. ҮАУ. paiti.histaiti 
24:(N 22), YAv. histät (Yt 8.32), Y Av. auua.histät (V 4.33, V 8.33, V 16.5), YAv. xstat (F 304), med. 3sg. 
25:Y Av. fraxstaite (Yt 10.107, Yt 19.92, V 15.45), 3р1. YAv. usahistan (Yt 19.11), ОРТ. 25р. ҮАУ. 
26:auua.histois (V 9.12), IMPV. 25р. Y Av. auua.hista (Yt 17.57), Y Av. upa.hista (Yt 17.21), usohista (V 
27:18.19, V 18.21, V 18.26, V 21.4), 2pl. YAv. usohistata (V 18.16, V 18.24); Aor. s-: SUBJ. 3sg. YAv. 
28:stanhaiti (N 42), OAv. stanhat (Y 50.4); Perf.: IND. 1sg. YAv. auua.hista (V 8.97, V 8.100, V 8.103), 3р1. 
29:Y Av. visastaro (Yt 19.8); Partic.: pres. YAv. histant-, med. YAv. histemna- (Yt 15.52, Yt 17.61, N 37), 
30:Y Av. paiti histemna- (Yt 10.36), perf. pass. Y Av. stata-, Y Av. auuastata- (F 149); Caus.: pres. IND. 15р. 
33:staiiāt (N 63), OPT. med. 3р1. YAv. astaiianta (V 3.18, V 5.49), IMPV.2sg. Y Av. auuastaiia (V 2.26) 
34:*OLD PERSIAN: stä- ‘to set, [med.] to stand’ || (+ *aua-) ‘to set down, place, restore’ || 
37:Pres. red.: impf. IND. med. 3sg. aistatä <a-i-8-t-t-a> (DB 1.85); Caus.: impf. IND. 1590. avastayam < 
40:(DB 4.92), 3sg. niyastaya <n-i-8-[t]-[a]-[y]> (DSn 1), <n-i-y-8-t-a-y> (XPh 50, XV 21), nistäya 
43:MIDDLE PERSIAN: (+ *abi-) MMP ‘yst-, ВМР yst-, ’(y)st- (YK‘YMWN-) /ést-/ ‘to 
44:stay, stand, be’ (also aux.), MMP ‘ystyn-, BMP ’styn- (YK‘YMWN-) /éstén-/ (sec. 
45:caus.) ‘to place, put, set’, MMP ‘ystyh- (caus. pass. ?) ‘to be placed’ || (+ *aua-) 
46:BMP ’wst’- /östä-/ ‘to set out’ || (+ *upa-) MMP "Ьуз! ‘place of refuge’, ВМР ’pst’n 
47:/abestan/, (?) BMP "Bet ml /abestam/ ‘reliance, refuge, support, trust’ || (+ *pari-) 
48:MMP pryst-, BMP plst- /parist-/ ‘to serve (through worship); to worship’ || (+ *fra-) 
49:MMP pryst-, fryst-, BMP plyst- (SDRWN-) ‘to send’ > DMMPP: 99b f., 17a, 
52:(+ *abi-) Widely attested: Pres.: IND. 3sg. MMP ‘ystyd, ‘styd, 1р1. MMP ‘yst’m, 2р1. MMP ‘ystyd, 3р1. 
53:MMP ‘ystynd, etc. || (+ *aua-) Pres.: IND. 1р1. BMP ’wstym /dstém/; Partic.: perf. pass. BMP "watt 
59:/ostad/ || (+ *pari-) Pres.: IND. 3р1. MMP prystynd, SUBJ. 3р1. MMP pryst’nd || (+ *fra-) Pres.: IND. 25р. 
60:BMP plystyh /fréstéh/, 152. MMP pryst’n, 3sg. MMP pryst’d, 3р1. MMP pryst’nd, IMPV. 2sg. MMP 
61:*pryst; Partic.: perf. pass. MMP fryst’d, pryst'd, II prystyd, prystyhyst; Inf.: MMP pryst’dn 
64:?) ’wyst- ‘to place, put’ = Ghilain: 78, 90 | DMMPP: 94, 76 
69:‘wyst’dn; Caus. (?): pres. 15р. ’wyst’m, 3р1. 'wystynd, SUBJ. 15р. ’wyst’n, ’wst’n, 2sg. *’wyst’, IMPV. 
73:become weary’ || (+ *aua-) vast- (vist-) ‘to remain’, (perf.) also ‘to approach’, vistä- 
74:(visti-) ‘to place, establish’ || (+ *a-) ? est- (*a-hista- ?) ‘to endure, be firm’ || (+ 
95:3р1. CSogd. pstynt, Impf.: IND. 1sg. dur. SSogd. ""psty^m ’skwn, 3sg. CSogd. p’Sty; Pret.: tr. IND. 1sg. 
97:*pari-) Impf.: IND. 35р. CSogd. pryst’y; Pret.: tr. IND. 35р. CSogd. pst'd'rt, 2р1. MSogd. prst'tó róó; 
102:IND. Ipl. pres. MSogd. nystymskwn, IMPV. 25р. SSogd. nsty ‘announce’; Impf.: IND. 1sg. MSogd. 
118:‘to place, put, impose’ || (+ *pari-) mapotptaoo ‘surrounding area’ || (+ *fra-)
```


## [2026-09-05T20:33:02.823Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TLM adiy ===\"; grep -n \"adiy\" TLM.txt | head -20\necho \"=== IEC ndhi/adhi ===\"; grep -n \"adhi \" IEC.txt | head -10\necho \"=== WLD Bd1 ndhi ===\"; grep -n \"adhi\\b\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-05T20:33:02.941Z] TOOL RESULT

```
=== TLM adiy ===
138:67.  0atiy  darayavaus  xsaya0iya  tuvarn  [ka]  xsaya0iya  68.  h}ra aparam  ahy  martiya  [kya]  draujana  ahatiy  hyava  [zujrakara  +   + ahat-69.  iy  avaiy  rua  dausta  +   +   +   a   ufrastadiy  parsa
185:2avahyaradiy.  In  the  modern  Persian  dialects  the  survival  of  radiy  is noteworthy;  in  New  Pers.  rn  is  used  in  a   general  adverbial  sense,  e.  g. r   iz-ra,  by  day,  ci-ra,  why;  cf.  Horn,  NS,  53,  C;  in  Afy.  lara  (metathesis for  rala)  is  an  affix  for  dat.,  e.  g.  >ra  ( mountain )   +   lara,  Geiger,  SA,  17; in  Balnei  ra  is  postposition  for  dat.  and  acc.,  e.  g.  togiira,  Geiger,  SB,  9; in  Kurd,  ra  is  also  affix  for  dat.,  Sociu,  SK,  158.
225:13.  ft'itiy  Darayavaus  Xsaya^iya  naiy  aha  martiya  49)naiy Parsa  naiy  Mada  naiy  amaxam  taumaya  kasciy  hya  avam  Gau- 50)matam  tyam  magum  xsa0ram  dltam  caxriva  karasim  haca darsma"2  a-51)tarsa  karam  vasiy  avajaniya  hya  paranam  Bardi- yam  adana  avahyar-52)adiy  karam  avajaniya  matyamam  xsnasa- tiv  tya  adam  naiy  Bard-53 )iya  amiy  hya  Kuraus  pu0ra  kasciy naiy  adarsnaus  cisciy  0astana-54)iy  pariy  Gaumatam  tyam magum  yfita  adam  arasam  pasava  adam  Aura-55  )maz[d]am  pati- yavahyaiy3  Auramazdamaiy  upastam  abara  Bagayadais  56)mahya X   raucabis  0akata  ahan  ava0a  adam  hada  kamnaibis  martiyai- bi-57)s  avam  Gaumatam  tyam  magum  avajanam  uta  tyaisaiy fratama  mar-58)tiya  anush'a  ahaDta  Sika[ya]uvatis  nama4  dida Nisaya  na-59)ma  dahyaus  Madaiy  avadasim  avajanam  xsa0ram- sim  adam  adlnam  va-60)sna  Auramazdaha  adam  xsayatfiya abavam  Auramazda  xsa0ram  mana  fr-61)abara
248:18.  0atiy  Darayavaus  xsayafliya  pasava  adam  Ba-84)  birum  asi- yavam  abiy  avam  Nadintabairam  hya  NabukMracara  aga[ubat]- a   8o)kara  hya  Nadintabairahya  Tigram  adaraya  avada  aistata2  uta 86)abis  n   a   viva  aha  pasava  adam  karam  maskauva  avakanam  am iyam  usa-87)barim3 4  akunavam  aniyahya  asarn*  f ranayam5  Aura- [maz]damaiy  upas[t]am  88)abara  vasna  Auramazdaha  Tigram viyatarayama6  [a]vada  avam  karam  89)tyam  Nadintabairahya adam  ajanam  vasiy  A0r[i]yadiya[h}"a]  mahya  XXYI  rau-90)cabis Sakata  aha“  a[  va0]a  hamaranam  akum[a]
319:10.  0atiy  Darayavaus  xsaya0iya  +   +   +   +   +Vaumisa  nama  Parsa mana  ban-50)daka  avam  adam  fraisayam  Arminam  ava0asaiy a0aham  paraidiy  kara  51)hya  hami0riya  mana  naiy  gaubataiy avam  jadiy  pasiiva  Vaumisa  a-52)siyava  ya0a  Arminam  pararasa pasava  hami[0riy]a  hangmata  paraita  pa-53)tis  Yaumisam  harna- ranam  cartanaiy  I   +   +   +   +   a1  nama  dahyaus  A0uray-54)a  avada hamarauam  akuuava”  Auramazda[ma]iy  upastam  abara  vasna Au-55)ramazdaha  kara  hya  mana  avam  karam  t[yam]  hami0riyam ajan  vasiy  56)Anamakahya  mahya  XV  raucabis  0a kata  aha”  ava- 0asam  hamaranam  57)  kartam
322:13.  0atiy  Darayavaus  x-71)saya0iya  pasava  hauv  Fravartis hada  kamnaibis  asabaribis  amu0a  Ra-72)ga  nama  dahyaus  Ma- daiy avapara4  asiyava  pasava  adam  karam  f-73)raisayam  nipadiy5 Fravartis  agarbT[ta]6  anayata  abiy  mam  ada-74)msai[y]  uta  naham uta  gausa  uta  harab;lnam7  frajanam  utasa-75)iy  [ucasjma8  avajam duvarayamaiy  basta  adariy  haruvasim  k-76)ara  avaina  pasavasim
327:6   nipadiy,  KT.  tyaipatiy,  ed.  See  voc.
367:3.  0!tiy  Darayavau-ll)s  xsayatfiya  Margus  nama  dahyaus hauvmaiy  hami0riya2  abava  12)1  martiya  Frada  nama  Margava avam  ma0istam  akunava"ta  pasa-13)va  adam  fraisayam  Dadarsis nama  Parsa  mana  bandaka  Baxtriy-14)a  xsa0rapava  abiy  avam ava0asaiy  a0aham  paraidiy  ava-15)m  karam  jadiy  hya  mana  naiy gaubataiy  pasava  Dadarsis  hada  k-16)ara  asiyava  hamaranam akunaus  hada  Margavaibis3  Auramazd-17)amaiy  upastam  abara vasna  Auramazdaha  kara  hya  mana  avam  karam  18)tyam  hami- 0riyam  ajan  vasiy  A0riyadiyahya  mahya  XXIII  raucabi-19)s  Sa- kata aha"  ava0asam  hamaranam  kartam
381:3.  Says  Darius  the  king:  There  (is)  a   region  Margiana  by name;  it  became  rebellious  to  me;  one  man  Frada,  a   Margian, him  they  made  chief;  afterwards  I   sent  forth  Dadarshi  by  name, a   Persian,  my  subject,  satrap  in  Bactria  against  him;  thus  I   said to  him;  go,  smite  that  army  which  does  not  call  itself  mine; afterwards  Dadarshi  with  the  army  went  away  (and)  engaged in  battle  with  the  Margians;  Ahura  Mazda  bore  me  aid;  by  the grace  of  Ahura  Mazda  my  army  smote  that  rebellious  army  ut- terly; 23  days  in  the  month  A0riyadiya  were  completing  then- course — then  the  battle  (was)  fought  by  them.2
468:8.  0atiy  Darayavaus  xsaya-46)0iya  vasna  Aura[mazdaha  ap]i- maiy  aniyasciy  vasiy  astiy  karta-4T)m  ava  ahyaya  d[i]p[iy]a  naiy nipistam  avakyaradiy  naiy  n-48)ipistam  mat[ya  hya  apa]ram imam  dipim  patiparsatiy  avah-49)ya  paruv  0a [day a3  tya]  mana kartam  nais[im]  ima4  varnavataiy  d-50)uruxtam  maniyaftaiy]5
470:10.  0a-53)tiy  Darayavaus  x[sa]ya0iya  nuram6  0uvam  varnav- atam tya  man-54)a  kartam  ava0a  ka[rahya  0]a[kv  avahya]radiy7 * mii  apagaudaya  yadiy  imam  55)handugam  naiy  [a]pa[gau]da[yak]y karahya  0aky  Auramazda  0uvam  56)dausta  blya  uta[ta]iy  tauma vasiy  blya  uta  dargam  jlvfi
471:11.  5T)0atiy  Darayavaus  [xsaya]0iya  yadiy  imam  haMugam apagaudaya-58)hy  naiy  0a by  [k]ara[hya]  Auramazdatay  jata  blya utataiy  taum-59)a  ma  blya
480:7sa  +   +   +   +   d   +   +   +   +   +   adiy,  KT.  ka[rahya  fljafk}7  avahya] radiy,  Tol-
492:2 1   would  read  ava^a  ka[rahya  0]a[hy  avahyajradiy,  tell  it  thus  to  the people-,  for  this  reason,  which  can  fit  the  few  traces  of  characters  on  the rock.  Since  KT  do  not  give  the  extent  of  the  lacuna,  I   feel  some  doubt whether  the  space  justifies  the  supplement  of  the  last  word.  KT  however read  the  Elam,  as  hu[pentukkime],  wherefore.  I   would  add  that  my  read- ing is  in  full  accord  with  Weissbach’s  emendation  of  the  Bab.  version,  u amat  kit-  turn  a-na  u-ku  ki-[bi ?],  and  declare (?)  the  true  record  to  the  people, ZDMG,  61,  729.
498:14.  0atiy  Darayavaus  xsayafliya  tuvam  [ka]  xsayafliya  68)hya aparam6  ahy  martiya  [bya]  draujana  ahatiy  hyava  [zu]rakara++T ahat-69)iy  avaiy  ma  dausta  [bly]a8  ufrastadiy  parsa
501:17.  flatiy  Darayavaus  xsa-77)yafliya  yadiy  im[a]m  dipim  i- maiva  patikara  vainahy  vikanah(i)dis15  ut-78)ataiy  yava  tau[m]a ahati[y  nai]ydis  paribarahy16  Auramazdataiy  jata  b-79)Iya  uta- taiy taum[a  ma  blya]  uta  tya  kunavahy  avataiy  Auramazd-80)a nika”tuv
571:3.  9)0atiy  Darayavaus  xsaya0iya  avahya-10)radiy  vayam  Haxa-
667:3.  0atiy  Darayavaus  xsaya-13)0iya  mami  Auramazda  upastam 14)baratuv  hada  vi0aibis  bagai-15)bis  uta  imam  dahyaum  Aura- 16)mazda  patuv  baca  hainav-l7)a  baca  dusiyara1  baca  dra-lS)uga abiy2  imam  dahyaum  ma  19)ajamiya  ma  ba[i]na  ma  dus-20)iya- ram3  [m]a  drauga  aita  adam  21)yanam4  jadiyamiy5  Auramazd-
672:5   jadiya[m]iy,  Stolze’s  Phot,  jadiyamiy,  Jn.  See  voc.
693:3.  0iltiy  19)Darayavaus  xsayafliya  yadiy  2O)ava0a  maniyahay7 haca  aniya-21)nii  ma  [ta]rsam  imam  Parsam  karam  padi-22)y yadiy  kara  Parsa  pata8  ahatiy  hya  23)duvais[ta]m  siyatis  axsata hauvci-24)y  Aura  nirasatiy  abiy  imam  vi0am
=== IEC ndhi/adhi ===
=== WLD Bd1 ndhi ===
3975:fiber die mehrdeutigen ai. adhi „an, auf“, ap. adiy „in“ (* n-dhi oder *cdhi, 
52300:Milch gemachter Quark" (: ai. dadhi).
```


## [2026-09-05T20:33:14.935Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3960,3990p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== page tag ===\"\ngrep -n \"pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('mehrdeutigen')\nprint(t[max(0,i-3000):i+500][-1200:])\nEOF"
}
```


### [2026-09-05T20:33:16.734Z] TOOL RESULT

```
lit. nuo m. Gen. „von— herab, von— weg“ (diese woher-Bed. erst durch 
die Yerbindung mit dem Ablativ neu entstanden), in Nominalzs. nuo-, in 
Yerbalzs. nu- (proklit. Kfirzung wie in pri- neben prie), lett. nuo m. Gen. 
„von“, als Praefix nuo-; apr. no, na m. Ace. auf (wohin), gegen, fiber— hin“, 
als Praef. „nach; von— weg“ (s. auch Bezzenberger KZ. 44, 304); aksl. na 
m. Acc. und Loc. „auf— hin; auf, an“ (dazu nacb prc : pre-dz neugebildet 
na-dz „oberhalb, fiber" m. Acc. und Instr. und Praeverb) ; ai. na- vielleicht 
in nadhita „bedrangt“, s. u. na- „helfen“. 

Hierher vermutlich lit. -na, -n „in (Richtung wohin)“, Postposition bei 
Verben der Bewegung (aber durch aksl. nevodz „Netz“ u. dgl., Berneker 
IP. 10, 166, wird kein ahlautendes nc- glaublich gemacht) av. na-zdijah-, 
ai. nediyas- „naher“ („*herangerfickter“; Wz. sed- „sitzen“; vermutlich 
ahnlich got. nek, ahd. nah Adv. „nahe“ als „heranschauend, herangevcn- 
det“ (mit Wz. oepi- als 2. Glied); s. Brugmann Grdr. II 2 2, 798 f., wo auch 
fiber die mehrdeutigen ai. adhi „an, auf“, ap. adiy „in“ (* n-dhi oder *cdhi, 
*odhil) und (S. 802, 860) arm. ond. 

Als ffirs Uridg. gesichert dfirfen gelten die Formen *an und and, no, 
wohl auch no {net). Die Annahme von Beziehung zum Demonstrati vpron. 
(no-, eno -) ano- (Fick I 4 367, Prellwitz 2 37 f.) bedarf noch niiherer Begrfin- 
dung, ist aber grundsatzlich ebenso zulassig, wie z. B. die Yerwandtschaft 
von ai. a „an, auf, herbei" (nicht aus *Ti nach Fick 1 4 367, Hirt Abl. 92) 
mit dem Demonstrativstamm e-, o-. 

Eine g-Ableitung wahrscheinlich in got. anaks adv. „plotzlich, sogleich", 
lit. nor/las, abg. nagh „plotzlich, jah“ (Grienberger Unt. 22, Brugmann II 2 
1, 507; die Yerbindung dieser Worte mit ai. ved. anjas, ailjasa Adv. „rasch, 
plotzlich", s. J. Schmidt KZ. 23, 268 m. Lit., ist nicht wahrscheinlich; die 
ai. Formen mogen nach Fick, auch Wb. I 4 23, II 4 11, bei andkti „salbt“, 
ni-anj- „schlfipfen“ als „im Ausgleiten" verbleiben; eine andere Deutung 
=== page tag ===
eg“ (s. auch Bezzenberger KZ. 44, 304); aksl. na
m. Acc. und Loc. „auf— hin; auf, an“ (dazu nacb prc pre-dz neugebildet  :


na-dz „oberhalb, fiber" m. Acc. und Instr. und Praeverb) ai. na- vielleicht ;


in nadhita „bedrangt“, s. u. na- „helfen“.
   Hierher vermutlich lit. -na, -n „in (Richtung wohin)“, Postposition bei
Verben der Bewegung (aber durch aksl. nevodz „Netz“ u. dgl., Berneker
IP. 10, 166, wird kein ahlautendes nc- glaublich gemacht) av. na-zdijah-,
ai. nediyas-    „naher“ („*herangerfickter“; Wz. sed- „sitzen“; vermutlich
ahnlich got. nek, ahd. nah Adv. „nahe“ als „heranschauend, herangevcn-
det“ (mit Wz. oepi- als 2. Glied); s. Brugmann Grdr. II 2 2, 798 f., wo auch
fiber die mehrdeutigen ai. adhi „an, auf“, ap. adiy „in“ (* n-dhi oder *cdhi,
*odhil) und (S. 802, 860) arm. ond.
   Als ffirs Uridg. gesichert dfirfen gelten die Formen *an und and, no,
wohl auch no {net). Die Annahme von Beziehung zum Demonstrati vpron.
(no-, eno -) ano- (Fick I 4 367, Prellwitz 2 37 f.) bedarf noch niiherer Begrfin-
dung, ist aber grundsatzlich ebenso zulassig, wie z. B. die Yerwandtschaft
von ai. a „an, auf, herbei" (nicht aus *Ti nach Fick 1 4 367, Hirt Abl. 92)
mit dem Demonstrativs
```


## [2026-09-05T20:33:23.476Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in ['adairi','a5airi','aöairi','antarj','antars','antare','inferus']:\n    for m in re.finditer(pat,t):\n        print(pat, m.start(), repr(t[m.start()-300:m.start()+300]))\n        break\nEOF"
}
```


### [2026-09-05T20:33:25.125Z] TOOL RESULT

```
adairi 1056513 'n, wie auch die \ngr. bei Bezzenberger BB. 27, 161. Falsch Fay Cl. Rev. 13, 396. \n\n*ndhos, pdheri „unter, sub“, ndhero- „der untere“, ndh e mo- „der unterste‘‘. \n\nAi. adhd-h (-as) ,.unten“ (als Praep. m. Acc. Gen. Abl.), gthav. add „unten“, \nvielleicht arm. snd in der Bed. „unter“ (m. Instr.). — Av. adairi „unter, \nunterlialb" (Praep. m. Acc. Abl.) = got. undar, ahd. nntar und untari \n(letzteres Satzinlautform mit bewahrtem alten Auslaut), as. undar, aisl. \ntinder „unter, sub“ (als Praep. mit Acc. und „Dativ“) ; ob lat. inf erne, \ninf emus ein entsprechendes * infer voraussetzt oder nach intern'
antare 1457847 's)q 0 l - „Tierjunges, junger Hund“ bezogen werden \n(Osthoff Par. I 274 ff.). \n\nkel-, kol-, kal- „betoren, vorspiegeln, schmeicheln, betriigen“. \n\nGr. att. xrjleco (urgr. rj) „bezaubern, betoren“, y.rjXr]& pog „Bezauberung“, \nxrjXrjdoveg PL f. „bezaubernde Wesen“ (nicbt wahrscheinlicher als , in- \ncantare“ zu y.aXkm, Wz. *ktl- „rufen“, Prellwitz 2 220 als Alternative); \n\nlat. calvor , -i und calvio, Ire „Ranke schmieden, hintergehen, tauschen“, \ncahimnia „Lug, Trug Yerlaumdung, Ranke“ (* culvomnia ), sehr wahr- \nscheinlich auch cavilla „Neckerei, Stichelei, Trotzelei“, cavillor, -an „necken, \n'
inferus 1056855 '. Abl.) = got. undar, ahd. nntar und untari \n(letzteres Satzinlautform mit bewahrtem alten Auslaut), as. undar, aisl. \ntinder „unter, sub“ (als Praep. mit Acc. und „Dativ“) ; ob lat. inf erne, \ninf emus ein entsprechendes * infer voraussetzt oder nach interns : internns, \nsuperus : superne vom Adj. inferus aus geschaffen ist, bleibt fraglich (iiber \ngot. undaurnimats s. u. en-, enter-). — Adj. ai. adhara-, av. adara- „der \nuntere“ (ai. adharCit Adv. „unten“ == got. undaro Adv. und Praep. m. ,,da \nunten“), lat. inferus „der untere“ (zum f s. Yf. LEWb. 2 s. v.), Adv. und \nPraep. m. Acc. infra (*'
```


## [2026-09-05T20:33:33.565Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt',encoding='utf-8',errors='replace').read()\ni=t.find('en-, enter-')\nprint(i)\nimport re\nfor m in re.finditer(r'\\nen, eni', t):\n    print(m.start(), repr(t[m.start():m.start()+700]))\nfor m in re.finditer(r'enter-, ptcr', t):\n    print(m.start(), repr(t[m.start()-200:m.start()+700]))\nEOF"
}
```


### [2026-09-05T20:33:35.117Z] TOOL RESULT

```
1056931
```


## [2026-09-05T20:33:38.217Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'ai\\. antar', t):\n    print(m.start()); print(repr(t[m.start()-1500:m.start()+900])); print('---')\nEOF"
}
```


### [2026-09-05T20:33:39.979Z] TOOL RESULT

```
289284
'Wb. 2 27) ; air. aile, n. a, ill \n„anderer“, cymr. usw. ail ds., gedoppelt air. aluile, araile, n. alaill, araill, \nmcymr. usw. avail , pi. ere ill „ein anderer“ (-11- fur -l- aus dem Adv. all, \nebenso meist in den Zs. wie gall. Allo-broges = mcymr. allfro „auslandisch, \nyerbannt“, gall. ’APAo-roiyeg, air. all-slige „zweites Aushauen“ — aber al- \nanman „andere Namen" — , mcymr. all-dut „Auslander“; s. liber die kelt. \nFormen bes. Tburneysen GGA. 1907, 801, Hdb. 289 f., Pedersen KG. I 156, \nII 195 ff.) ; got. aljis „anderer“, sonst nur in Zs. wie as. eli-lendi n. „fremdes \nLand i£ , abd. elilenti „ds., Landesverweisung" (nhd. Elend), got. aljaleikos \n„anders“, anord. elligar, filar „oder, sonst :! , ags. ellicor , elcor „sonst, anders- \nwo“, abd. cliclwr „ferner“, und in Adv. wie ags. elles (engl. else ) „anders“, \nanord. ell a „andernfalls“ u. dgl. ; eine Komparativbildung *alira ist ags. \nelra „der andere". \n\nArm. ail „anderer“ (Hiibschmann Arm. St. I 77, Arm. Gr. I 41 7). DaB \nai. anyci- „anderer“ nach antard- umgebildetes *alyu sei (Sommer IF. 11,3) \nist moglieb, aber nicht erweisbar. \n\nEine dem gr. dkXo-Tgtog abnliche Komparativbildung mit Formans -tero- \n(Beschrankung auf die Wahl zwischen zweien) ist lat. alter, -ter a, -terum \n„der andere von zweien" = osk. alttram „alteram“ (bei Plautus auch altro-; \nin altrinsecus, altrdvorsum ist die Synkope durch die Lange des Wortganzen \nbedingt. Nicht nach Wood Cl. Ph. 7, 302 aus idg. *al-teros, das sich zu \n*al-ios verhalte wie ai. antara-h zu anya-h oder aus *an-tero-s und al-ios \nverschrankt sei, denn dies lieBe durch weg synkopiertes lat. * altro- erwarten; \nvielmehr aus idg. *ali-teros, vgl. detji-og : dsil-regog, oder allenfalls erst im \nI tab neugebildetem *ali-teros; in letzterem Falle in jungerer Beziehung zum \nersten Glied von ali-quis\'!); da von altera.ro, adulter , alter nus, alter can (auch \naltercuml Zimmermann KZ. 45, 136f.). \n\nYgl. zum Pron.-St. al-, ol- bes. Rozwadowski IF. 3. 264 ff., Quaest. gramm. \n(Rozprawy akad. Krak. Ser. II, tom X) 1—21, Brugmann Dem. 95, 107, \nGrdr. II 2 2, 340, Vf. LEWb. 2 538. \n\n2. al- ,,wachsen; wacbsen machen, nabren“. \n\nGr. veabjs „munter, stark" ( veog al- ; Prellwitz 2 , Boisacq s. v.) ; \n\nlat. alo , -ere, -ui, -itum und -turn „nahren, groBzieben" = got. ags. alan (ol) \n„aufwachsen“ (intr. wie lat. adoleo), aisl. ala ( ol ) „nahren, hervorbringen", \nair. alini „na'
---
417535
".) yn-, gall, esseda aus *en-seda, em-brekton ; \n\ngot. in „in :: , adnom. m. Dat., Aee., Gen., ahd. as. ags. in, anord. 7 „in“, \nAdnom. m. Dat. und Acc., aus *eni (fiber Ableitungen wie got. inn „hinein“, \ninna, innana, wolil aus *eni-n-, s. Brugmann IF. 33, 304 f.) apr. en „in“, \nadnom. m. Dat. u. Acc., lett. ie- (nur Praefix) : tiefstufig *n in lit. ? (alter \nund heute dial, in, Belege bei v. d. Osten-Sacken IF. 33, 218 f.) .,in“, \nadnom. m. Loc. und Acc. \n\nAksl. on- ( on-usta ,,Schuhwerk :: , n-dolb „Tar‘j raw-, n „in“, adnom. m. \nLoc. und Acc., aus idg. on? oder *en ? ? Oder zu gr. dvd, idg. *aw? (siehe \nBrugmann aaO. S2S). \n\nAi. in dnika- n. „Angesieht“ (=ao. ainika- ds.) aus *eni- 0 (ft-; *ni- in \nai. ni-ja- „eingeboren, innewohnend, bestandig, eigen“, ao. ni-zonta „ein- \ngeboren, ingenuus“, ai. ni-tya- „bestandig, eigen“ = got. nipji-s „Yerwandter“, \nanord. nidr „Yerwandter“. ags. nippas pi. „Manner, Menschen“ (s. Schulze \nKZ. 40, 41 Iff. 416), auch im Yerbalpraef. ar. ni- „hinein l ‘, z. B. ar. nlgam-, \nao. nigam- „in einen Zustand gelangen u (Brugmann II 2 2, 828,861). \n\n( e)nero - „innerlich“ : arm. *nero- „das Innere“, vorausgesetzt von ner- \n„intra, hinein“, nerks „innen“, nerkoy „drinnen“ (Brugmann II 2 2, 696, 698, \n707 i; vielleicht gr. evegoi als „die drinnen, niimlich in der Erde“ (Sonne \nKZ. 14, II, Gtintert IF. 27, 49; priignanter nimmt Bezzenberger BB. 27, \n\n1 54 f. Hapostare aus ol iv eog an). \n\nenter , nter „zwischen — hinein“, en-tero- ,,innerlich“ : \n\nai. antar, uv. antara, ap. a n tar ^zwischen 1 ', adnom. mit Loc. Instr. Acc. \nGen.; ai. antar a- „innerlich“, a w. antar a- ^innerer 1 ', Sup. ai. dntama- „ der \nnachste“ (trotz Fick I 4 to, 263 nicht zu anti , anta -), av. antama- „der. \ninnerste, vertrauteste, intimus“; ai. antra-, auch mit Yrddhi antra- n. „Ein- \ngeweide“, arm. mder-k PI. „Eingeweide“ (gr. Lw.? s. Hiibschmann Arm. \nGr. I 447f.); \n\ngr. tvTEQOv, meist PI. „Eingeweide“ (fiber urtaov s. aber u. an- „hauchen Ll ; \nalb. nder ,,zwischen, in“ (wolil nicht lat. Lw., s. Pedersen Rom. Iber. 9, \n213 , ferner (JokI SBWienAk. 168, I 59) ndjer, ntjer, nyera, ner, per „bis l< \n{ *entcro -); lat. enter, inter „zwischen'‘, adnom. m. Acc. (orstarrte m. Gen. \ninterivia-s, interdiiis , intro, intra, intrin-secus , interns „innerlich“, interior, \nintimus , intesinus (s. u.), osk. entrai ,,*Interae“, tiefstufig 's. Yf. Kelten und \nItaliker"
---
417620
"e., Gen., ahd. as. ags. in, anord. 7 „in“, \nAdnom. m. Dat. und Acc., aus *eni (fiber Ableitungen wie got. inn „hinein“, \ninna, innana, wolil aus *eni-n-, s. Brugmann IF. 33, 304 f.) apr. en „in“, \nadnom. m. Dat. u. Acc., lett. ie- (nur Praefix) : tiefstufig *n in lit. ? (alter \nund heute dial, in, Belege bei v. d. Osten-Sacken IF. 33, 218 f.) .,in“, \nadnom. m. Loc. und Acc. \n\nAksl. on- ( on-usta ,,Schuhwerk :: , n-dolb „Tar‘j raw-, n „in“, adnom. m. \nLoc. und Acc., aus idg. on? oder *en ? ? Oder zu gr. dvd, idg. *aw? (siehe \nBrugmann aaO. S2S). \n\nAi. in dnika- n. „Angesieht“ (=ao. ainika- ds.) aus *eni- 0 (ft-; *ni- in \nai. ni-ja- „eingeboren, innewohnend, bestandig, eigen“, ao. ni-zonta „ein- \ngeboren, ingenuus“, ai. ni-tya- „bestandig, eigen“ = got. nipji-s „Yerwandter“, \nanord. nidr „Yerwandter“. ags. nippas pi. „Manner, Menschen“ (s. Schulze \nKZ. 40, 41 Iff. 416), auch im Yerbalpraef. ar. ni- „hinein l ‘, z. B. ar. nlgam-, \nao. nigam- „in einen Zustand gelangen u (Brugmann II 2 2, 828,861). \n\n( e)nero - „innerlich“ : arm. *nero- „das Innere“, vorausgesetzt von ner- \n„intra, hinein“, nerks „innen“, nerkoy „drinnen“ (Brugmann II 2 2, 696, 698, \n707 i; vielleicht gr. evegoi als „die drinnen, niimlich in der Erde“ (Sonne \nKZ. 14, II, Gtintert IF. 27, 49; priignanter nimmt Bezzenberger BB. 27, \n\n1 54 f. Hapostare aus ol iv eog an). \n\nenter , nter „zwischen — hinein“, en-tero- ,,innerlich“ : \n\nai. antar, uv. antara, ap. a n tar ^zwischen 1 ', adnom. mit Loc. Instr. Acc. \nGen.; ai. antar a- „innerlich“, a w. antar a- ^innerer 1 ', Sup. ai. dntama- „ der \nnachste“ (trotz Fick I 4 to, 263 nicht zu anti , anta -), av. antama- „der. \ninnerste, vertrauteste, intimus“; ai. antra-, auch mit Yrddhi antra- n. „Ein- \ngeweide“, arm. mder-k PI. „Eingeweide“ (gr. Lw.? s. Hiibschmann Arm. \nGr. I 447f.); \n\ngr. tvTEQOv, meist PI. „Eingeweide“ (fiber urtaov s. aber u. an- „hauchen Ll ; \nalb. nder ,,zwischen, in“ (wolil nicht lat. Lw., s. Pedersen Rom. Iber. 9, \n213 , ferner (JokI SBWienAk. 168, I 59) ndjer, ntjer, nyera, ner, per „bis l< \n{ *entcro -); lat. enter, inter „zwischen'‘, adnom. m. Acc. (orstarrte m. Gen. \ninterivia-s, interdiiis , intro, intra, intrin-secus , interns „innerlich“, interior, \nintimus , intesinus (s. u.), osk. entrai ,,*Interae“, tiefstufig 's. Yf. Kelten und \nItaliker 54 f.), osk. anter , umb. anter, under „inter“, adnom. m. Loc. Acc.: \nair. eter. eti"
---
2710380
' fur sich“ \n\n(= lett. deju, del „Eier legen“, deju det „zusammenloten“, aksl. dejq „lege“, \nacech. deju „tue, mache“). Pf. ai. dadhdu, dadhimd, av. 3. sg. dad a (: gr. \nzE&e-yat, lat. -dull, o. pru-ffed, ahd. teta usw.). \n\n\n\ndhe- \n\n\n827 \n\n\nArm. ed Aor. „er setzte“ {= ai. a-dhat ; 1. ag. edi, 2. sg. edir ), Praes. \ndnem „ich setze“ ( *dinem , Hiibschmann Arm. Gr. I 439, Bgm. II 2 3, 315 \n= russ. dcnu „setze, stelle, lege\' - \', skr. djenem „tue, stelle, lege“). \n\nGr. xiih] fu „setze\'‘ (Aor. i\'lhjy.a — s. u. — , edepev, e&exo, Fut. fjoa>), \nPtc. •&ET o?) : \n\nLat. con-dere ,,griinden, einlegen; bergen, bewahren, verstecken, bedecken", \nabdere „wegtun, verstecken, anoxidhai 1 , perdere „vernichten“, credere „glau- \nben, vertrauen" (s. u. *kered- „Herz“; uber Einmischung von zu dare ge- \nhorigen w-Formen s. Yf. LEWb. 2 u. duim ); Pf. condidl usw., osk. pru-ffed \n„posuit“ (*-fefed). Mit einer k- Erw. lat. facio, -ere, feci (: e&gy.a), factum \n„tun, machen“, osk. fakiiad, umbr. facia „faciat“, umbr. fakurent Fut. II \n„fecerint“, praen. (Manios-Inscbrift) fhefhaked ,, fecit", osk. fefacid Konj. \nPf. „fecerit“, fefacust Fut. II „fecerit“, mi t*fek- umbr. feitu, jetu „facito“ ; \nfacilis „(tunlicb) leicht", umbr. fayefele ds. (dieselbe Bed. in aisl. deed aus \n*dhe-lis ); facies „Aussehen, Erscheinung, Antlitz" i v s. Yf. LEWb. 2 s. v.), fa- \ncinus (s. zur Bildung Meillet Msl. 15, 259), ponli-fex, arti-fex bene-ficus u. dgl. ; \nzur Bed. von interficio „tote“ („*lasse verschwinden"), vgl. ai. antar-hita-h \n„verschwunden ,: (Hirt IF. 37, 231). \n\nDieselbe &-Erw. auSer in gr. e&rjy.a auch in {hrjy.rj „Behaltnis“, ai. dha- \nka-h „Behalter“ und phryg. (Ramsay KZ. 28, 385) ad-daxex. \n\nGall, dede „posuit“ (Fick II 4 143); vgl. lat. con-, ah-, cre-didl, ahd. teta \n„ich tat". \n\nAhd. tom, tuom, as. dom, aga. ddm „tue“, Inf. ahd. tuon, as. ags. don \n„tun“ (a. zum Formalen Bgm. II 2 3, 102), Praet. ahd. teta „ich tat" (2. ag. \ntati , pi. tatu-m , -t, -n nach dem Typus got. setum umgebildet), as. deda \n(2. ag. dtdos, 3. pi. dadun, dedun ), ags. dyde < dudi (a. o. zu ai. dadhdu). \n\nLit. deti „legen, stellen", Praes. 2. pi. deste ( *dhe-dh-te ) ag. derm, desie-s, \ndest(i) (vgl. Buga Kalba ir a. 158, 213), neugebildet dedic ; lett. det (a. o.); \n\naksl. deti „legen“ (auch „sagen“), Praes. dezdq ( *dedio ) und dejq (a. o.) ; \ndpjq, dejati „legen, verrichten" ; -wi -Iterati v aksl. o-devati'
---
```


## [2026-09-05T20:33:47.173Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nfor key in ['enter , nter','enter, nter','ai. antar, uv. antara','Av. adairi','ndhos']:\n    i=t.find(key)\n    if i<0: \n        print(key,'NOT FOUND'); continue\n    seg=t[:i]\n    tags=re.findall(r'\\[pdf page (\\d+)\\]',seg)\n    print(key,'-> pdf page', tags[-1] if tags else '?')\nEOF"
}
```


### [2026-09-05T20:33:49.396Z] TOOL RESULT

```
enter , nter NOT FOUND
enter, nter NOT FOUND
ai. antar, uv. antara NOT FOUND
Av. adairi -> pdf page ?
ndhos -> pdf page ?
```


## [2026-09-05T20:33:55.220Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la BQT_v2_pages.txt; grep -c \"\" BQT_v2_pages.txt\ngrep -n \"pdf page\" BQT_v2_pages.txt | head -3\ngrep -n \"pdf page\" BQT_v2_pages.txt | tail -3"
}
```


### [2026-09-05T20:33:55.293Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
41071
```


## [2026-09-05T20:33:58.075Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -40 BQT_v2_pages.txt; echo \"===FF count===\"; python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint(t.count('\\f'))\nprint(repr(t[:300]))\""
}
```


### [2026-09-05T20:34:00.078Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان‬

                      ‫‪۴2 ۱‬‬

                  ‫رک یمن‬
                  ‫م سارو کی و ررك‬


                 ‫جلررومدا‬
             ‫چاپ دوم فروردین ‪۳۴۳۱‬‬
                 ‫با تجدید نظر کامل‬
          ‫بسرمایه کتابفروشی ابن سیتناپران‬




                   ‫چاپ افست رشدبه‬
                   ‫م‬ ‫و‬
‫نآکو سخنیم بیاموزد مرا‬
                       ‫د‬ ‫د‬ ‫ل‬ ‫ج‬ ‫م‬ ‫ة‬ ‫چ‬ ‫ا‬ ‫ی‬ ‫د‬
‫على ‪۰‬‬             ‫بند گر دا ند ‪۰‬‬                       ‫‪۳‬‬      ‫‪۳7‬‬

‫داربان مقدمهٌ مجلد اول برحان قاطع ( صفحدٌ صد وسی ودو ) نگارنده از‬
                                                                ‫ی‬
‫خوانند گان فاضل درخواست کرد که اطلاعات خودرا درموضوعهای مختلف کتاب تراسا‬
‫دربارة لغات مربوط بلهجه‌های محلی وشاهدهای شان ونادر مرفوم‌دارند‪ .‬چندتن دعوت‌وبرا‬
‫اجات کردند وشغاهاً وکا اطلاعاتی دردسترس مصحح گذاشتند‪ .‬وماآنچهرا که‌توانستيم‬

‫درحواشی کتاب حاضر با ذکرنام آنان جای دادیم» ودربنجا با سیاسگزاری اسامی‌ابشان‌را‬
                     ‫باذ کرلهجه‌هابی که از آنها لغاتی را توضیح داده‌اند بادميکتيم ‪۰‬‬
 ‫امام (محمدعلی) (دزفولی)؛ لسانسية دانشکده ادیات و دیرادبیات فارسی در‬
                                       ‫بغداد (لغات دزفولی وانه کی از لغات شوشتری)‪.‬‬
===FF count===
683
'\x0c                                         \u202b\u202a7\u202c\u202c\n\n                          \u202bرن\u202a۳\u202c\u202c\n    \u202bنات\u202c\n      \u202bا م\u202c\n              \u202bلض\u200cبال \u202a ۰ ۲۶\u202cرک\u202c\n\u202b\u202a۱\u202c\u202c       \u202bاسا تعدولیدیارتم و\u202c\n                                     \u202b\u202a7\u202c\u202c\n\u202b\u202a ۰\u202cو زل رسوا »وا روون لات سا روصا مواقم\u202c      \u202bوتان\u202c\n\n                      \u202b\u202a۴2 ۱\u202c\u202c'
```


## [2026-09-05T20:34:04.562Z] TOOL CALL #46: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-05T20:34:04.606Z] TOOL RESULT

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


## [2026-09-05T20:34:07.737Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb && python3 tools/ref_page.py BQT:1051 --image 2>&1 | head -60"
}
```


### [2026-09-05T20:34:09.458Z] TOOL RESULT

```
python3: can't open file '/home/sfmqrb/tools/ref_page.py': [Errno 2] No such file or directory
```


## [2026-09-05T20:34:11.870Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:1051 --image 2>&1 | head -80"
}
```


### [2026-09-05T20:34:13.575Z] TOOL RESULT

```
no scan of BQT covers printed page 1051 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:34:16.868Z] TOOL CALL #49: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'), ensure_ascii=False, indent=1))\nprint(json.dumps(d['MON'].get('scans'), ensure_ascii=False, indent=1))\n\""
}
```


### [2026-09-05T20:34:18.628Z] TOOL RESULT

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
null
```


## [2026-09-05T20:34:26.434Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# look for pages containing 'زیر' as an obvious headword and try to detect printed numbers\ndef digits(s):\n    return re.findall(r'[۰-۹]{3,4}', s)\nfor i in range(490,530):\n    p=pages[i]\n    print(i, digits(p)[:6], p[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:34:28.080Z] TOOL RESULT

```
684
490 ['۵۱۲', '۶۶۲', '۳۵۲', '۹۹۱']  ‫‪٩‬‏ ‪۱ ۵‬سه‬   ‫سز‬                                      
491 ['۱۰۷', '۲۰۲۰', '۲۵۱', '۷۹۱', '۱۱۲']   ‫رمج‬                                                     
492 ['۹۳۳', '۸۵۷', '۴۳۱']  ‫‏—‪ opo‬اسه‬     ‫طعم‬       ‫مانئد‬   ‫قطه‌دار و فوقانی »
493 ['۱۰۳۱', '۳۵۲', '۷۵۷', '۳۵۲۲', '۵۸۲', '۹۷۱۱']                                                             
494 ['۳۳۰', '۹۹۱', '۲۵۲', '۸۷۲۶', '۵۹۳'] ‫=‪m‬‬                                                      
495 ['۸۲۱', '۳۲۱']                                         ‫بیان بدانهزم‬      
496 []       ‫و‬                                                   
497 ['۲۶۷', '۲۳۱']      ‫زتجیر‬                                                
498 ['۰۸۰', '۹۹۱', '۷۲۳۱', '۸۱۱', '۱۳۵', '۰۰۰۱']    ‫خر و‬                                                   
499 ['۹۸۲', '۱۵۱', '۵۷۲۷']  ‫زف بای‬                                                   
500 ['۵۹۵۲']   ‫سیز‪۳‬ه‪-۱‬‬                                             
501 ['۷۰۱', '۷۹۱', '۷۲۳۱', '۷۱۱', '۹۱۱']                                                             
502 []    ‫‪ ۵‬اس‬   ‫و‬      ‫زگله * ‪ -‬بفتح اولوآخ رکهلام باشد‪.
503 []                                                             
504 ['۰۳۱', '۳۰۵', '۵۲۲', '۰۳۱', '۸۰۱', '۲۵۲']                    ‫وبفتح اول نام داروبی است که‬            
505 ['۹۸۱', '۹۶۲', '۵۲۷', '۷۵۲۰', '۷۹۱', '۳۷۰']   ‫زورق‬                                                    
506 ['۲۹۲۱', '۷۲۵']  ‫‪٩۰ 6‬‬                                                   
507 ['۸۲۲۲', '۲۲۵', '۸۵۱۵']   ‫زوترگ‬                                                   
508 ['۹۸۱', '۰۵۹', '۷۷۹', '۸۱۷', '۱۳۱'] ‫—‬        ‫‪4 6٩‬‬                                         
509 ['۰۵۲', '۸۷۱']   ‫زحراوی‬                                                  
510 []   ‫‪— ۱‬‬   ‫‪4‬‬    ‫س‬                                    
511 ['۹۷۲', '۱۱۱']                                                             
512 ['۱۰۷۱', '۰۰۷۱', '۹۷۹', '۱۲۷', '۰۸۱', '۵۸۱']    ‫—‬       ‫‪9‬و‬   ‫=‬      ‫بزان = بروزن میزان‪.‬به‌عنی‌
513 ['۹۹۲', '۰۸۱']      ‫زبرزبان گفتن‬                                         
514 ['۰۹۳', '۲۳۲', '۳۵۰۱']  ‫ات‬        ‫او‬                                           
515 ['۱۳۲۰', '۹۲۳۰', '۰۹۲', '۰۸۲']                                                             
516 ['۰۸۲', '۰۵۹۱', '۱۵۹۱', '۵۵۲', '۱۱۱', '۷۳۱']   ‫==‬                                                      
517 ['۷۲۰', '۲۷۷', '۱۰۸']   ‫زين‬                                                     
518 []                                           ‫کفتار دو آزدهم‬  
519 []                                                             
520 ['۹۲۳']                                           ‫بیان دوم‬        
521 ['۵۸۱', '۷۰۱', '۷۹۱']  ‫ژغاله‬                                                    
522 ['۰۲۷']   ‫اف‬    ‫د‬                                               
523 []                                              ‫بیان هفتم‬    
524 ['۸۳۱']                                              ‫بیان هشتم‬    
525 ['۲۱۷', '۳۱۲']  ‫زون‬                                                      
526 ['۶۷۰', '۷۱۵', '۵۵۳']   ‫—‬        ‫=‬                                            
527 []                                 ‫از کناب پرهان قاطمگفتار سیر
528 ['۸۹۲', '۳۲۷۰', '۷۷۱', '۳۳۲', '۹۶۱']        ‫ها‬                                                 
529 ['۳۳۳', '۱۹۱', '۱۱۱']     ‫ساده‬
```


## [2026-09-05T20:34:40.838Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re,unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(510,520):\n    p=pages[i]\n    c=p.count('زیر')\n    print('=== leaf',i,'count زیر',c)\nEOF"
}
```


### [2026-09-05T20:34:42.770Z] TOOL RESULT

```
=== leaf 510 count زیر 0
=== leaf 511 count زیر 0
=== leaf 512 count زیر 0
=== leaf 513 count زیر 6
=== leaf 514 count زیر 9
=== leaf 515 count زیر 0
=== leaf 516 count زیر 0
=== leaf 517 count زیر 0
=== leaf 518 count زیر 0
=== leaf 519 count زیر 0
```


## [2026-09-05T20:34:45.676Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (513,514):\n    print('======= leaf',i)\n    print(pages[i][:3500])\nEOF"
}
```


### [2026-09-05T20:34:47.515Z] TOOL RESULT

```
======= leaf 513
     ‫زبرزبان گفتن‬
                                                                                                                ‫تب ای ‪ ۵‬ات‬




     ‫زرا ‪ ۴‬بکر اولوثاك بالف کشبده‪.‬‬                                  ‫لفظ فارسی است‌یا عربی ‪ -‬وبا جیم فارسی‌بمعنی‬
                        ‫‪.‬‬    ‫ازبر ای آن و آزین جهت‬       ‫سی‬         ‫بیرون آوردن و بیرون کشیدن باشد ‪ -‬و خوش‬
                                                                    ‫وچايك وجلد وخوش وضع را نگیوزبند ‪-‬ونومی‬
     ‫کنابه اززبون بودن‬           ‫زير از میانه =‬
                                                                    ‫از انگور بقایت خوش لذت باشد ‪ -‬وبمعنی لاغ‬
                                       ‫و بد بودن باشد ‪.‬‬
                                                                    ‫وم‌خر ‪ 3۳‬همآمده است ‪ -‬وزهوار کفش وموزه‬
     ‫شیر افکن ‪.‬‬             ‫وبزرن‬
                                ‫زیرافکی * =‬                         ‫را هم میگوبند ‪ -‬و ربه‌انهاییکه استادان نقش‬
     ‫ووشك و آنچه در زیر افکنده‬
                             ‫بمعنی نهالی ت‬                                              ‫ند لش جامها را بدان نندلد‪.‬‬

                                                  ‫خوالند ‪.‬‬          ‫ر بجك = باجیم فارسی بروزن ميخك"‬
                                                                    ‫رگوودسفند راگونندکهبگاوشت وبرنج‌ودیگر‬
     ‫زير افکند * = بسکون‌نون ودالابجد‪.‬‬
                                                                ‫باشند و بگذارند تا خشك شود‬                     ‫دره‬
                                                                                                                 ‫رپ‬‫کالح‬
                                                                                                                      ‫مص‬
     ‫بممنی زبر افکن است کهنهوالتیوشك و آله‬                          ‫و در زمستان بپزند وبخورند ؛ ویعطی گوبندرور‪:‬‬
     ‫در زبرافکنده باشد ‪ -‬و نام مقامی‌است ازموسیقی‬
                              ‫کنرچك است ‪.‬‬  ‫که آ‬
                                                                    ‫بر شیر خواره است که آلرا پاکیزه کنند و در‬
                                                                    ‫هم بیچند مالند نارئجی و چندی از آن را بر‬
     ‫در بر = بضم بای ایجد (‪ )۱‬وسکون‬                                 ‫فقرا‬          ‫ان‬
                                                                                   ‫بارا‬
                                                                                      ‫بندرو"‬
                                                                                           ‫کن‬             ‫ب‬
                                                                                                          ‫او‬‫بند‬
                                                                                                              ‫کخ کش‬
                                                                                                                  ‫سی‬
     ‫رای فرشت )‪ » (۱‬کتابه‌از که برباشد‪ .‬وشخصی‬
                                                                                                                    ‫خوانند ‪.‬‬
     ‫والماید‬     ‫را نکیفزته‌اند که بظاهر خود را دوست‬
                                  ‫و در باطن دشمن باشد ‪.‬‬             ‫زید لك ‪ = ۱‬با دال بروزن زبرلك ‪.‬غلام‬
                                                                                           ‫بچة نرك مقبول کروابند ‪.‬‬
      ‫زیر بزر گان ب=ائانی مجهول‌رسکون‬
‫‪.1٩۰‬‬
   ‫‪««۹‬ظ_ظ
======= leaf 514
 ‫ات‬        ‫او‬                                                                              ‫زیرفون‬
‫بکهد‌یگرباشرت کنند ‪ -‬کونایه ازخطاهم‌هست‪.‬‬          ‫زیر فون ‪ = ۱‬بافا بروزن‌یلگون‪ ,‬لوعی‬
‫زیر وزاده با زای هطه دار (‪ )۱‬بر‬                    ‫از درخت سنجد است وآنرا لمر ومیوه لمیباشد‬
‫رزن کیرودار‪ .‬کنابه ازآو ازحز بن وآهسته‌باشد‪9 .‬‬      ‫سرد وخشك است ودر‬          ‫د‪.‬‬
                                                                               ‫ومشق‬
                                                                                  ‫شر د‬
                                                                                     ‫یر د‬
                                                                                        ‫مپشت‬
                                                                                           ‫و‬
                                                                                   ‫قابات بکار برند‪.‬‬
‫زریرہبا؟ » با بای ابجد (‪ )۲‬بر وزن‬
‫دیدسا * آشی راگوبند که باگودت مرغ فربه‬
                                                   ‫زقيران ‪ -‬بفااف بر وزن شیرخان ‪,‬‬
‫و زره وسر که پزند ‪ .‬منطو بر‪ ۱‬نافع است سنی‬
                                                                ‫عم ماهی است ازماههای ملکی؟ ‪.‬‬
                             ‫شکم بزرکه را ‪۰‬‬
                                                    ‫زیر لكه برومزينرك » داناحوکیم‬
                                                    ‫رفعیم ومدرك و صاحب هوش باشد ‪ - ۴‬و بمعنی‬
                                                                         ‫فولاد جوحردار نز گفته‌اند ‪:‬‬
           ‫کراوبا (‪)e‬‏ وزنان ونان خواه گوند‪.‬‬
                                                    ‫زیر لاه = بائالیمجهول بروزن‌یشگاه‪,‬‬
‫دیز = بااول مکسور بثالی رسیده وزای‬                             ‫بععنی کرسی باشد که برآن شینند‪.‬‬
                  ‫قطه دار زده ‪ ,‬ریز های برف‬        ‫بالف‬       ‫ه‬
                                                              ‫طیی‬
                                                                ‫شسین‬
                                                                   ‫با‬          ‫زر لك سار‬
                 ‫وبرف ریزهایی‌باشد که از حوا‬       ‫کشده وبرای بی‌نقطة زده » خداوند اراك وفهم‬
                  ‫بهنگام سرما بارد اورآا بعربی‬                                         ‫وشمور باشد ‪.‬‬
                  ‫سقیطه گوند ‪ -‬و جالوری هم‬         ‫دار لب گفتن ‏ بمعنی زبرزبان‌گفتن‬
                  ‫هت کوچکتر از ملخ و شبها‬           ‫است هککنایه‌از آهتهوپوشیده حرف‌زدن‌باشد ‪.‬‬
      ‫زز‬          ‫بانگ طولانی کندوعربان صرار‬        ‫ز یروبالا» ممروف است نکحهت‌وفوق‬
                                  ‫کونره ‪#.‬‬        ‫رد با‬ ‫پاشد ‪ -‬و کنابه از آست که داو پمسر‬
            ‫(‪ )۳‬چش » چب ‪ ۱‬کراریا‪.‬‬                                    ‫‪.‬‬     ‫‪-‬ا‬
                                                                            ‫از‬‫پك‪:‬‬
                                                                                ‫(‪ )۱‬چ‬

                                                                ‫‪ - ۱‬رك ؛ زیزفون (ع) ‪.‬‬
  ‫واقم شد ‪ :‬اول اينکه زیرقان درقاموس بابای ابجد موجود است و دراینجا با بای حطی لوشته »‬
  ‫دوم اشکه دربدان معنی گفته که نام ماهی است ازماههای ملکی» حال آنکه صاحب قامو سگفته‪:‬‬
  ‫« زبرکان کفته‌اند ‪ :‬دوست راچندان‬       ‫‪۴‬‬          ‫الربرقان بالکرالقمر‪ « ».‬چك ص‪ ۰۹۳‬ح > ‪.‬‬
                                             ‫قوت مده که کر دشمنی کند تواند‪ « ».‬کلنان *ه > ‪.‬‬
  ‫‏‪- a‬زیز ‪#‬همدرعربی
```


## [2026-09-05T20:35:00.953Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[512][-3000:])\nEOF"
}
```


### [2026-09-05T20:35:03.123Z] TOOL RESULT

```
                           ‫اد ‪ .‬بممنی زینت و تیکوبی و آراش‬
‫و سکن ثالی‬                 ‫سور‬
                             ‫ربج ‪ -‬بمااکول‬                                                                  ‫اشد ‪. ۷‬‬
 ‫و جیم ابجد » معرب زیگه‌است» کوتآانبی‌باشد‬
 ‫ورکات افلاك و کوا کب‌را‬
                       ‫که منجمان احوار ح‬                        ‫لیا *‪ -‬بروزن‌دیباءبسمنی ییکووخوب‬
‫از آن‌مملوم کنند *‪ -9‬ونختَة بنابان ومعماران که‬                   ‫وعنی‬‫‪-‬م‬
                                                                      ‫امت که نقیض زشت و بد باشد ‪٩‬‏ ب‬
                                                                                                    ‫زیتله هم هست‪.‬‬
 ‫بناییرا‬        ‫تة‬
                 ‫‪-‬و‬‫ر‏ش‬
                     ‫در آن طرح عمارت کشند ‪٩۱‬‬
 ‫نیزگفته‌اند ‪۴۱‬؛ و بستی گوبند باين دو معنی‬                      ‫ریبال ‪ -‬با بای ابجد بر وزن قیقال »‬
 ‫اما اصممی‌میگوید‪ :‬من نمیدانم‌این‬                 ‫عربی است ‏‬       ‫تندروباشد‪.‬‬    ‫لی‬
                                                                                  ‫او‬‫وشتر‬
                                                                                       ‫یوا‬
                                                                                         ‫حسب‬
                                                                                           ‫رازا‬
                                                                                              ‫هایه‬
                                                                                                 ‫کت‬
                                                       ‫(‪ )۱‬خم‪ : ۱‬عکرالزیت ؛ چش ‪ :‬حکرالزنته ‪.‬‬

   ‫‏‪( - ٩‬عر) « زبادة بالکر‪ .‬افزونی» «منتهی الارب» و درفارسی فصیح نیز زیادت وژباده‬
   ‫‪ - ۴‬صیغة دعابی از «زید» سوم شخص عفرد‬                                ‫‪ :‬خاله گیر ‪.‬‬   ‫رك‬    ‫‪- ۴‬‬             ‫‪۰‬‬   ‫آورید‬


   ‫‪ - ۴‬پهلوی ‪ , 02112‬اوستا ‪ ( 80822 - ۰ 88872 -‬ضرر )‬                                       ‫مضارع از د زستن > ‪.‬‬
    ‫‪anayj -‬‏ ) طلم ) * کردی ع‬                       ‫ساسکرت‬              ‫« بارتولمه ‪۱۰۷۱٩ ۰ ۰۰۷۱‬‏ لیر گے‬
    ‫اقنانی ع ‪ ۳7132‬؛ باوچیع ‪ 102712‬استىع ‪ . ۳41012. 0812‬ارمنی ع ‪«0262‬اسشق‪.*۹۷۹‬‬
   ‫راسم فاعل از «زستن» ‪ « :‬زردشت را کفتند ‪:‬‬                    ‫‪۱‬‬           ‫سحیح «زینده» است ‪.‬‬           ‫‪6‬‬

   ‫جانور چندنوع است؟ ‪.‬گ‪..‬فت ‪ :‬زبائی کوبا وزبالی کوبا مرا وزبانی‌میرا » رك‪ :‬قابوسنامه باهتمام‬
    ‫سی ص ‪ ۱۲۷‬بامقابلة‪ :‬عبارتی‌از قابوسنامه بنقگلمارنده ‪ .‬مجلهٌیما سال‪ ۱‬شمارة ‪ 4‬ص*‪.۰۸۱-۵۸۱‬‬
                    ‫ندارد برآن روی لاله زب‬                           ‫بوی‬    ‫دارد مر آن زلف مك‬               ‫‪۲‬‬

       ‫«لفت فر ی ‪۷۲‬‬        ‫‪۰‬‬   ‫مروزی‬   ‫عمارء‬



  ‫دروی زیا‬            ‫‪٩‬‏‬                 ‫از ‪ :‬زب ‪ (۱ ۳‬فاعلی وصفت مشبهه) = زیبنده ‪.‬‬                      ‫‪۵‬‬
           ‫‪ °‬رك ‪ :‬زیگه ‪.‬‬                         ‫مرحم دلهای خسته‌است وید درهای‌بته‪« » .‬کلتان ‪. 6۱۱‬‬
```


## [2026-09-05T20:35:24.958Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(510,516):\n    p=pages[i]\n    for ln in p.split('\\n'):\n        if 'پهلوی' in ln or 'اوستا' in ln or 'ازیر' in ln or 'azer' in ln.lower():\n            print(i,'|',ln.strip()[:250])\nEOF"
}
```


### [2026-09-05T20:35:26.817Z] TOOL RESULT

```
512 | ‫‪ - ۴‬پهلوی ‪ , 02112‬اوستا ‪ ( 80822 - ۰ 88872 -‬ضرر )‬                                       ‫مضارع از د زستن > ‪.‬‬
513 | ‫‪ - ۴‬هنی پایین ‪ ۰‬پهلوی ‪« 7128‬منای‪.* ۹۹۲‬‬                                ‫در رده (ه‪.‬م‪۰ ).‬‬   ‫مصحف‬            ‫‪۱‬‬
513 | ‫‪۲81108_0281 . 7۲2‬دیی رکه ‪ ۱‬ازاوستابی ‪hda‬‏ ‪ , 2020‬کردی ‪ , 7112‬بلوچیع‬
515 | ‫اوستاد کن »‬           ‫شش‬     ‫برره‬                        ‫من بدین مکر وحبله زر ندهم‬
```


## [2026-09-05T20:35:34.936Z] TOOL CALL #55: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ | grep -i bqt; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/"
}
```


### [2026-09-05T20:35:34.985Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  2634275 Sep  4 14:06 BQT_alt_v1.txt
-rw-rw-r--  1 sfmqrb sfmqrb      139 Sep  4 14:06 BQT_dli_part1.txt
-rw-rw-r--  1 sfmqrb sfmqrb 26399828 Sep  4 14:06 BQT_v1_djvu.xml
-rw-rw-r--  1 sfmqrb sfmqrb  2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2620060 Sep  4 14:06 BQT_v1.txt
-rw-rw-r--  1 sfmqrb sfmqrb  4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2359504 Sep  4 14:06 BQT_v2.txt
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
```


## [2026-09-05T20:35:51.420Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ntr=str.maketrans('۰۱۲۳۴۵۶۷۸۹','0123456789')\nhits=0\nfor i in range(20,len(pages)):\n    nums=set(int(x.translate(tr)) for x in re.findall(r'[۰-۹]{3,4}',pages[i]))\n    for off in [538]:\n        if i+off in nums:\n            hits+=1\n            print(\"leaf\",i,\"-> printed\",i+off)\nprint(\"hits\",hits)\nEOF"
}
```


### [2026-09-05T20:35:53.752Z] TOOL RESULT

```
leaf 115 -> printed 653
leaf 214 -> printed 752
leaf 475 -> printed 1013
leaf 493 -> printed 1031
hits 4
```


## [2026-09-05T20:35:58.099Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[513][-2500:])\nEOF"
}
```


### [2026-09-05T20:35:59.866Z] TOOL RESULT

```
                     ‫معنی پوشیده وپنهان هموهت‬
     ‫گس انت‬          ‫کمان کمرور را گویند ‪ -‬و کتابه از‬
                                                                    ‫‌اند ‪-‬‬
                                                                         ‫فرتنهیز‬
                                                                               ‫بزرگ و مگهت‬                     ‫تی‬
                                                                                                                ‫عو‬‫برم‪-‬‬
                                                                                                                     ‫وج‬
     ‫که هرطور او را خواهند و عرچه باو بگونندیا‬                      ‫ونامگیاهی است که بقامت زرد و باربك می‌باشد‬
                             ‫بفرماند فرمان بردار باشد ‪.‬‬
                                                                     ‫ی‌هم‬
                                                                        ‫وآلرا زریر واسپرك میگونند ‪ -‬وکبمتعنان‬
     ‫خررد بضم خای شطه دار (‪)۳‬‬
                            ‫زي‬                                      ‫آمده است» وآن بارچه‌ای باشدکه درتایستان‌ها‬
     ‫بود از‬    ‫لحنی‬    ‫را و دال بی قطه ‪ .‬تام‬       ‫سکون‬    ‫و‬
                                                                    ‫پوشند ‪ .‬گونند اکر کسی درزمتان جامة کتان‬
                                                  ‫موسبقی ‪.‬‬
                                                                     ‫نو بپوشد بدن اولاغر شود واگر درتابستان‌بپوشد‬
                                                                    ‫فربه کرده و اکر در زمستان کتان شسته بپوشد‬
         ‫از پوشیده و پنړان وآهسته سخن کفتن‌باشد‪.‬‬                                          ‫فربه شود و در تابستان لاغر‪.‬‬

         ‫(‪ )۳‬چك ‪ - :‬بض‌خا ‪.‬‬                     ‫(‪ )0‬چك ‪ :‬سکون را ‪.‬‬                    ‫(‪ )۱‬چك ‪ - :‬بضمب ‪.‬ا‬
        ‫‪ - ۴‬هنی پایین ‪ ۰‬پهلوی ‪« 7128‬منای‪.* ۹۹۲‬‬                                ‫در رده (ه‪.‬م‪۰ ).‬‬   ‫مصحف‬            ‫‪۱‬‬

       ‫‪۲81108_0281 . 7۲2‬دیی رکه ‪ ۱‬ازاوستابی ‪hda‬‏ ‪ , 2020‬کردی ‪ , 7112‬بلوچیع‬
       ‫‏‪ cêra‬و ‪ ۵2۲6۵5‬و ‪. ۲۵05‬رك ‪ :‬اسشق ‪ ,‬هویشمان ‪ ۰ ۰۸۱‬کیلکی ‪٣‬ا‏ز ؛ در اوراق مالوی بپارقی‬
               ‫‪١‬ص‏ ‪۶۸‬‬        ‫‪۰‬ج ‪X1‬‏ ‪»٠‬‬       ‫‏‪ . 'dryy‬رك ‪ :‬حنتکه ‪ :‬فهرستی ازکامات بارسی صاله‪5058 ....‬‬
                 ‫‪.‬‬    ‫رك ‪ :‬زیرافکن‪‎‬‬      ‫*‬          ‫‪.‬‬   ‫زیر افکند‬    ‫‪:‬‬   ‫رك‬   ‫‪-‬‬   ‫‪۴‬‬       ‫‪ :‬ازبرا‪.‬‬   ‫رك‬    ‫‪-‬‬    ‫‪۴‬‬
```


## [2026-09-05T20:36:10.033Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"پرانتز\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null\ngrep -n \"پرانتز\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -5\ngrep -n \"پرانتز\" MON_part1.txt | head -5"
}
```


### [2026-09-05T20:36:10.119Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part2.txt:0
MON_part1.txt:0
```


## [2026-09-05T20:36:13.196Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"پرانتز\" \"پرانتر\" \"رانتز\" \"پرانت\"; do echo \"-- $w\"; grep -c \"$w\" MON_part1.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null; done\necho \"=== ARY ===\"; grep -n \"پرانتز\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-05T20:36:15.856Z] TOOL RESULT

```
-- پرانتز
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
-- پرانتر
MON_part1.txt:1
incoming/MON/MON_2vol_Adena_v1_djvu.txt:1
-- رانتز
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
-- پرانت
MON_part1.txt:1
incoming/MON/MON_2vol_Adena_v1_djvu.txt:1
=== ARY ===
```


## [2026-09-05T20:36:18.571Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -m2 \"پرانتر\" MON_part1.txt | cut -c1-500\necho \"---adena---\"\ngrep -n -m2 \"پرانتر\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | cut -c1-800"
}
```


### [2026-09-05T20:36:18.629Z] TOOL RESULT

```
29918:پرانتر: 2 (.) نشانه‌ای است مر کب 
---adena---
29918:پرانتر: 2 (.) نشانه‌ای است مر کب
```


## [2026-09-05T20:36:20.686Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29905,29935p' MON_part1.txt"
}
```


### [2026-09-05T20:36:20.728Z] TOOL RESULT

```
(ص‌مر.) آنکه دلی پراکنده دارد؛ پریشان 
خاطر؛ پراگنده خاطره» بی 7 ارام. 
پراگنیدن: 02۲72۵19-7 [- ۵ ِِ 
پرا گنیدن] (مص‌م.) سرپیچی کردن» تخلف 
کردن. 

پسرالک: ([- سلا رک ] (ا.) آهن 
جوهردار. بیع و شمشیرء بلار کث. 

پران: م۲۵ ,۲2۲-3 (ص‌فا.) هر چیز که 
می بر دء بر ند۵. (حا.) در حال پر بدن. 
پرانتر: 2 (.) نشانه‌ای است مر کب 
از نیم قوس عمودی بدان شکل () و آن 
برای نوشتن جملهٌ معترضه و مانند آن بکار 
رود؛ قوسین» هلالین. 

پراندن: ۵-(0۵۲)۲ [- برانیدن ] (مص ع.) 
برواز دادن طبوره برانیدن» اطاره. پر تاب 
کردن: 0 ری : . سجن درشت و 
بی‌جا گفتن ؛ متلکك براندن. لاف زدن و 
مبالغه در مدح کسی؛ تعریف بیجا کردن. 
(عم.) در نهان با مرد آمیختن (زن)؛ تکث 
پراندن» تک برانی 

پراور: ۲۶۰-۰۲ [- پرآور] (ص‌مر.) دارای 
بر» پرنده» تيز بر. تبزرو. 

پسرپا: ۰۶ [- پرپای] (اسر.) (جان.) 
کبوتری را گویند که بر روی استخوان کف
```


## [2026-09-05T20:36:29.772Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%D8%B1%D8%A7%D9%86%D8%AA%D8%B2/",
 "prompt": "Quote the \"فرهنگ معین\" (Mo'in) entry for پرانتز verbatim, including any origin tag such as [فر.] and the French source word. Also quote any دهخدا or عمید etymology given."
}
```


## [2026-09-05T20:36:30.857Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/parenthesis",
 "prompt": "Quote the etymology of 'parenthesis' verbatim (Greek parenthesis, para- + en + thesis, tithenai), and any note on French parenthèse. Also state what it says about 'episode' if mentioned."
}
```


### [2026-09-05T20:36:35.352Z] TOOL RESULT

```
# Etymology of "Parenthesis"

**Greek Origin:**
The term derives from Greek *parenthesis*, literally meaning "a putting in beside," composed of *para-* ("beside") + *en-* ("in") + *tithenai* ("to put, to place").

**French Source:**
The word entered English from "French *parenthèse* (15c.) or directly from Medieval Latin *parenthesis*."

**Note on "Episode":**
The webpage content provided does not mention "episode" or discuss its etymology.
```


### [2026-09-05T20:36:36.362Z] TOOL RESULT

```
# پرانتز - Mo'in Dictionary Entry

From **فرهنگ معین**:

"(پَ تِ ) [ فر. ] (اِ. ) نشانه ای است قوسی شکل ( ) که برای نوشتن جملۀ معترضه"

This entry indicates the word has French origins (marked as [فر.]) and describes parentheses as a curved punctuation mark used for inserting parenthetical clauses.

The **لغت نامه دهخدا** provides etymological context, noting that پرانتز refers to two semicircular marks "( )" and cross-references "پارانتز" as the related form.

No specific etymology from عمید is provided in the content shown—only a definition describing the symbol's mathematical and textual applications.
```


## [2026-09-05T20:36:41.276Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/episode",
 "prompt": "Quote the etymology of 'episode' verbatim: Greek epeisodion, epeisodios, epi + eisodos (eis 'into' + hodos 'way'), and how it entered English."
}
```


## [2026-09-05T20:36:43.026Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81en",
 "prompt": "Quote the reconstruction, meaning, and descendants list for Proto-Indo-European *h₁en, including Proto-Indo-Iranian/Indo-Iranian, Greek en/eis, Latin in, Proto-Germanic *in, and derived terms such as *h₁énteros."
}
```


### [2026-09-05T20:36:47.245Z] TOOL RESULT

```
# Etymology of "Episode"

According to the Online Etymology Dictionary, the word entered English in the 1670s. Here's the etymology:

**Greek Origins:**
"from Greek _epeisodion_ 'an episode,' literally 'an addition,' noun use of neuter of _epeisodios_ 'coming in besides,' from _epi_ 'in addition' + _eisodos_ 'a coming in, entrance'"

The second component breaks down further: "_eis_ 'into' + _hodos_ 'a way, path; a journey; a method, system'"

**Entry into English:**
The term arrived through "French _épisode_ or directly from Greek _epeisodion_" during the 1670s, initially describing "commentary between two choric songs in a Greek tragedy" and "an incidental narrative or digression within a story, poem, etc." The modern sense of an "outstanding incident, experience" emerged by 1773, while its application to "individual broadcasts of serial radio programs" developed by the 1930s.
```


### [2026-09-05T20:36:50.064Z] TOOL RESULT

```
# Proto-Indo-European *h₁én

**Reconstruction:** *h₁én (alternatively *én)

**Meaning:** "in"

## Key Descendants

**Direct reflexes across language families:**
- Proto-Indo-Iranian: *Hāndrás and related forms
- Ancient Greek: ἐν (en), εἰς (eis), ἐς (es)
- Latin: intus
- Proto-Germanic: *eni
- Proto-Celtic: *eni
- Proto-Balto-Slavic: *in
- Armenian: ի (i) / յ- (y-)

## Major Derived Terms

Notable formations include *h₁énteros ("inner, located inside"), *h₁entór ("between"), and *h₁en-dró-s ("egg, scrotum"), which yielded Sanskrit आण्ड (āṇḍa) and related words across Indo-Aryan languages.

## Reconstruction Notes

The traditional reconstruction with initial *h₁ faces challenges. Certain Greek and Sanskrit compounds suggest the laryngeal may be absent, indicating an alternative form *én without the initial element.
```


## [2026-09-05T20:37:11.132Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ēwar\\b\" PHD.txt | head -5 | cut -c1-600\necho \"---mackenzie---\"\ngrep -n \"ewar\\|éwar\" PHD_mackenzie.txt | head -5 | cut -c1-400"
}
```


### [2026-09-05T20:37:11.198Z] TOOL RESULT

```
1186:certain a- | abē-gumān, ēwar, tāštīg.
1187:certainly ēwar.
2880:myriad bēwar.
---mackenzie---
1567:bewar [bywll M bywr, N,....,] myriad, ten thousand.
1908:dasBr [d'sl = Av. dii8ra-] gift, reward.
1984:dewar [dyw'll M dyw'r, N -] wall.
2178:ebarag edyp)lk l , )dw)lk l I N ewar] evening.
2250:ewar eywll J )y,9)r] certain(ly), assured(ly).
```


## [2026-09-05T20:37:17.634Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"estadan\\|ēstādan\\|estad,\" PHD_mackenzie.txt | head -5 | cut -c1-400\necho \"--- andar ---\"; grep -n \"^andar\\|andar \\[\" PHD_mackenzie.txt | head -5 | cut -c1-400\necho \"--- er/azer ---\"; grep -n \"^ler \\|azer \\[\" PHD_mackenzie.txt | head -5 | cut -c1-300"
}
```


### [2026-09-05T20:37:17.708Z] TOOL RESULT

```
2391:frestadan / frestidan, frest- [SDRWN-(y)tn l < A '" IdTj plyst-)tn ' ,
5877:abandon abaz estadan az, histan.          action kard, kardag(an), karm,
7062:master awestad, rad, salar; ,.,., of the   merry wiyufsisnig; V. happy; make--
8340:frestadanI
8667:franam-                     -4~t)        frestadan             \\te.>'~Cb
--- andar ---
979: Aleksandar ['Ikmdll M 'lxsyndr, N Iskandar] Alexander (of Macedon).
1081:andar [B YN < A byn I M 'ndr, N ......] in, among, towards, concerning.
1088:andarag, ['ndlg] in, between, among.
1089:andarmah ['ndlm'h] new moon.
1090:andaron ['ndlwn l I M 'ndrwn, N ......run] inside, within.
--- er/azer ---
1428:azer [hedll N zir] below, under.
2210:ler [)dll M )yr, v. azer] down, below; low; under.
2212:ler eyl] noble; hero.
```


## [2026-09-05T20:37:24.693Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"And, conj\" \"Under, prep\" \"Inter-, prefix\" \"Episode\" \"Parenthesis\" \"Intestine\" \"Intimate\" \"Inferior\" \"In, prep\"; do echo \"== $w\"; grep -n \"$w\" SKT.txt | head -2 | cut -c1-450; done"
}
```


### [2026-09-05T20:37:26.443Z] TOOL RESULT

```
== And, conj
== Under, prep
== Inter-, prefix
== Episode
5921:Episode,  a  story  introduced  into  another. (Gk.)  Gk.  irrtiaaiot,  a  comiut>  in  besides. •»Gk.  iw'  (jwi).  besides;  fitroSov,  an  en- ttonce,  «t(TiS5iot,  coming  in,  froui  tli,  iii^ iW«,  a  way.
== Parenthesis
== Intestine
== Intimate
== Inferior
9201:Inferior.  (F.-L)  O.  F.  imfirieur. L  inftriortm.  aoc  of  in/eri^r,  lower,  covp. of  inftrus,  low,  nether.  Strictly.  vttf^W is  itself  a  compar.  form,  answeriof  to tft/^dm,  lower,  from  aJMajt  adv.,  nndcfBcallb low,  down.
== In, prep
```


## [2026-09-05T20:37:33.420Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"^And,\" \"^Under,\" \"^In,\" \"^Inter-\" \"^Parenthesis\" \"^Intestine\" \"^Intimate\" \"^Interest\"; do echo \"== $w\"; grep -n \"$w\" SKT.txt | head -2 | cut -c1-500; done"
}
```


### [2026-09-05T20:37:35.251Z] TOOL RESULT

```
== ^And,
== ^Under,
20427:Under,  beneath,  t  E.)     A.  S.  umMt om/er^  Icel.  ttnJir,  Dan.  Swcil.  unJer^ v»(i!c2r,  GuWrr,  under.  Commonosai
== ^In,
18332:In,  Tamine.  Taminy.  Tommy, ■fstuPTi  kcc  Slute,
22778:In,  lu-.  3^6-329. m&.  nu*.  a5a-369. mi.  mi-.  370-374. mu.  ma-.  375-379. na,iu-,  175-183,
== ^Inter-
== ^Parenthesis
== ^Intestine
== ^Intimate
== ^Interest
```


## [2026-09-05T20:37:40.887Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"and, conj\" \"inter-, pref\" \"in, prep\" \"intimate, adj\" \"intestine, n\" \"parenthesis, n\" \"episode, n\" \"inferior, adj\" \"interest, n\"; do echo \"== $w\"; grep -n -m1 \"$w\" KLN_1966.txt | cut -c1-700; done"
}
```


### [2026-09-05T20:37:43.171Z] TOOL RESULT

```
== and, conj
== inter-, pref
== in, prep
18998:in,  adj.  —  Fr.  prec.  word, in,  adv.  —  ME.  in,  fr.  OE.  in,  inn,  inne,  rel.  to the  adverbs:  OS.  in,  inn,  ON.  inn,  OHG.  in  and to  OE.  in,  prep.  See  in,  prep, in-,  pref.  meaning  in,  into,  toward,  up,  against, as  in  in  born,  incline.  —  E.  in  or  L.  in;  see  in, prep.  In  words  of  Latin  origin,  in-  becomes  il- before  /,  ini-  before  b,  m  and  p,  ir-  before  r  (see il-,  ‘in’,  im-,  ‘in’,  ir-,  ‘in’).  Cp.  em-,  en-. in-,  privative  pref.,  as  in  in  advertence.  —  L.  in-, ‘not’,  cogn.  with  Goth.,  OE.  un,  ‘not’;  see  un-, priv.  pref.  L.  in-,  ‘not’,  becomes  *-  before  gn, il-  b
== intimate, adj
== intestine, n
== parenthesis, n
== episode, n
== inferior, adj
== interest, n
```


## [2026-09-05T20:37:46.644Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -m1 \"^in,  prep\\| in,  prep\\.\" KLN_1966.txt | cut -c1-900\necho \"=== parenthesis ===\"; grep -n -m1 \"parenthesis\" KLN_1966.txt | cut -c1-900\necho \"=== episode ===\"; grep -n -m1 \"episode\" KLN_1966.txt | cut -c1-700\necho \"=== and conj ===\"; grep -n -m1 \"and,  conj\" KLN_1966.txt | cut -c1-700"
}
```


### [2026-09-05T20:37:46.734Z] TOOL RESULT

```
2853:Derivatives:  announce-ment,  n.,  announc-er,  n. annoy,  n.  —  ME.  anoi,  anui,  fr.  OF.  enui  (F.  en¬ nui),  ‘worry’,  back  formation  fr.  enuier,  ‘to worry,  vex,  annoy’.  See  annoy,  v. annoy,  tr.  v.  —  ME.  anuien,  fr.  OF.  anoier,  en- noier  (F.  ennuyer),  fr.  VL.  inodiare,  ‘to  hate’, fr.  L.  in  odio,  ‘in  hate,  in  aversion’.  See  in,  prep., and  odium  and  cp.  ennui,  noisome.  Cp.  also  It. annoiare,  OProven?.  enojar  (whence  Sp.  enojar), ‘to  vex,  annoy’,  which  also  derive  fr.  VL. inodiare.
=== parenthesis ===
27395:Derivative:  parenteral-ly,  adv. parenthesis,  n.,  word,  clause  etc.  inserted  into  a sentence.  —  ML.,  fr.  Gk.  Trapevffeai?,  ‘inser¬ tion’,  lit.  ‘a  putting  in  beside’,  fr.  napEm-Uevat, ‘to  put  in  beside’,  fr.  reapa,  ‘beside’,  ev,  ‘in’,  and Tiffsvai,  ‘to  put,  place’.  See  para-,  ‘beside’,  2nd en-  and  thesis.
=== episode ===
13417:Derivative :  episcopal-ly,  adv. episcopalian,  adj.,  pertaining  to  bishops  or  to episcopacy.  —  See  prec.  word  and  -ian. Derivative :  episcopalian-ism,  n. episcopalism,  n.,  the  doctrine  that  authority  re¬ sides  in  a  body  of  bishops  and  not  in  any  in¬ dividual.  - —  Formed  with  suff.  -ism  fr.  Eccles. L.  episcopalis.  See  episcopal, episcopate,  n.,  1 )  the  office  or  dignity  of  a  bishop ; 2)  the  whole  body  of  bishops.  —  Eccles.  L. episcopdtus,  ‘dignity  of  a  bishop’,  fr.  episcopus, ‘bishop’.  See  episcopal  and  subst.  suff.  -ate. episio-,  combining  form  denoting  ‘relation  to the  vulva’.  —  Fr.  Gk
=== and conj ===
2698:and,  conj.  —  ME.,  fr.  OE.  and,  rel.  to  OS.  endi.
```


## [2026-09-05T20:37:52.906Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2698p' KLN_1966.txt | cut -c1-1200"
}
```


### [2026-09-05T20:37:52.952Z] TOOL RESULT

```
and,  conj.  —  ME.,  fr.  OE.  and,  rel.  to  OS.  endi.
```


## [2026-09-05T20:37:55.173Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2698,2702p' KLN_1966.txt | cut -c1-1400"
}
```


### [2026-09-05T20:37:55.222Z] TOOL RESULT

```
and,  conj.  —  ME.,  fr.  OE.  and,  rel.  to  OS.  endi.
72
73
anemo-
ande,  OFris.  and(a),  ande,  MDu.  ende,  enn,  Du. en,  OHG.  enti,  anti,  later  unfa,  unti ,  MHG.  unde, und,  G.  und,  ‘and’,  ON.  enn,  en,  ‘and,  but’,  prob. fr.  I.-E.  *i}thd-,  whence  also  OI.  athS,  ‘then, and’.  Cp.  an,  ‘if’,  and  ampersand, anadabata,  n.,  a  Roman  gladiator  whose  helmet had  no  opening  for  the  eyes.  — -  L.,  a  word  of Gaulish  origin.  The  first  element  of  this  word means  ‘blind’,  and  is  cogn.  with  OE  andhah, Avestic  anda,  of  s.m.  The  second  element  is  of the  same  origin  and  meaning  as  L.  battuere,  ‘to beat,  strike’.  See  batter,  ‘to  beat’,  and  cp.  words there  referred  to.
```


## [2026-09-05T20:38:01.573Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC ===\"; grep -n -m3 \"en- 'in'\\|ndher\\|enter- \" IEC.txt | cut -c1-500\necho \"=== SYN in ===\"; grep -n -m3 \"antar\\|Av. antara\" SYN.txt | cut -c1-400\necho \"=== LAT inter ===\"; grep -n -m2 \"inter, prép\\|INTER\\b\" LAT.txt | cut -c1-500"
}
```


### [2026-09-05T20:38:01.644Z] TOOL RESULT

```
=== IEC ===
1227:bhendheros, bhendhros ‘kinsman, mate’. WP II, 152 Gk. pentherós, pentherá 'father-, mother-in- law’; Li. befidras ‘colleague’; adj. jointe’); Latv. biedrs, id.
2657:duism “in two, through the middle Gk. dià; Alb. cf. ndér-dym (in doubt, fr. enter- ^); Per. düyum, s, duvum, adj. “second: OE cf. twinn *double'; twiman *waverer, hy- pocrite
11809:noit- (2), o-gde variant of type *neit-, see nit- (1) Lat. cf. (vowel ambig.) nitor, sup. nisus & nixus (of two separate origins but here in the sense of “strive*); Cz. cf. pod-nét 'enter- prise’; pod-nítit, inf. ‘undertake’. (For sup. nixus, cf. niks- (1) above)
=== SYN in ===
6497:6. ChSl. jetro, SCr. jetra, Boh, jatra, Pol. watroba (like ChSI. qtroba ‘womb’) : ChSl. qtr?, Lat. inter, Skt. antar ‘within’, Grk. &repa ‘entrails’, etc. Walde-P. 1.127. Berneker 269. Briickner 605.
8995:2. Lat. centaculum, iantaéculum ‘break- fast’, fr. vb. centdre, iantare ‘take break- fast’ : déitinus, ididinus ‘hungry’, fur- ther etym.? Ernout-M. 472. Walde-H. 1.674 f.
13144:Lat. planta ‘cutting, shoot, slip’ (in this sense always Varro, RR), never ‘plant’, but the source of the modern Romance, Celtic, and Gme. words in the latter sense (but OE, ME plante in sense of Lat. planta), same word as planta ‘sole of the foot’? Some suggest a back-formation fr. the vb. plantare ‘plant’ taken as fr. planta ‘sole of the foot’. But, beside the fact tha
=== LAT inter ===
```


## [2026-09-05T20:38:13.208Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%B3%D8%AA%D8%A7%D8%AF%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%A2%D8%B1%DB%8C' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81en' \\\n 'https://abadis.ir/fatofa/%D9%BE%D8%B1%D8%A7%D9%86%D8%AA%D8%B2/' \\\n 'https://www.etymonline.com/word/parenthesis' \\\n 'https://www.etymonline.com/word/episode' ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 154 (book 124), root En/Ndher: verification of nodes zir, andar, istadan, ari, parantez, parenthesis, episode, PIE *h1en\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T20:38:17.666Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7b2c819a2414c3c6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b2a6adec0e1055ef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7f63e697c3c55410.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/82f101b0194447c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b63affa4cbab8ad9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/009343e3dc6e44d5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e1954a6e88402694.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7fb4547d723e4c89.txt
```


## [2026-09-05T20:38:58.972Z] TOOL CALL #76: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg154.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/154.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-05T20:38:59.033Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T20:39:40.664Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json\nd=json.load(open('page-127.json'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        for rc in n.get('ref_check',[]):\n            if rc['ref'] in (None,'','none','(none)','None'):\n                print(json.dumps(rc,ensure_ascii=False)); break\nEOF\ngrep -o '\"ref\": \"[^\"]*\"' page-127.json | sort -u | head -20\necho \"=== verify_check tail ===\"; sed -n '60,140p' ../../tools/verify_check.py"
}
```


### [2026-09-05T20:39:42.935Z] TOOL RESULT

```
{"ref": "(none)", "status": "not_checked", "note": "the box carries no reference in the printed chart; the claim is covered by the POK:248 citation on the English node below."}
{"ref": "(none)", "status": "not_checked", "note": "the box carries no reference in the printed chart; the parent Latin box cites AHD, which lists FOUNTAIN among the English reflexes of dhen-¹."}
"ref": "AHD"
"ref": "BQT:876,877"
"ref": "BQT:888"
"ref": "FSF:88"
"ref": "HRN:127"
"ref": "HRN:128"
"ref": "KLN:399"
"ref": "MON:1562"
"ref": "(none)"
"ref": "POK:247"
"ref": "POK:248"
"ref": "POK:249"
=== verify_check tail ===
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


## [2026-09-05T20:41:05.720Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /adairi  Praep/ {print NR}' BRT.txt\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'adairi  Praep' in p:\n        import re\n        print('leaf',i)\n        print([l.strip() for l in p.split('\\n') if re.search(r'\\b\\d{2,4}\\b', l)][:8])\nEOF\necho \"=== HUB zir ===\"; grep -n \"zTr\\|zir \\|zér\\|Ml Ir\" HUB.txt | head -10 | cut -c1-300"
}
```


### [2026-09-05T20:41:07.553Z] TOOL RESULT

```
70
leaf 69
['h  unten  an- ziehen . .,  wenn  (von  unten)  nach  oben  . ." N.53.  2)    \'von    unten,    vom  Tiefland', 'herkommend\',  d.i. \'westlich\':  vät>m  \'r?m ..  upanm  ..fratanm  ..pasiqüTm  "den westlichen,  östlichen,  südlichen,  nördlichen Wind"  S.  2,  jz;  —  vätaAe  ..  \'rohe  S. 7.22.', 'KompA.  —  Vgl.  aiaiti.  —  ai.  aJiara-  Adj., np.  -»gl.  «>»).    —    Pü.   (lu  S.,    N.  52):    alar,\\', '74  19-', "•  j.  adairi  Praep.  'unter,  unterhalb';  i)  mit Akk.:    ao'  hax>m  nivöiryeite  V.  <¥.  69;  —", "ao'  p3wm  g>us  \\K.i'j.$$;  56.  a)  mit", "•  j.  aSairi.dahyav-  Adj.  (auch  mask.)  'der unter  dem  Land  ist* :  mi'kr?m  upairi^ahyOm ..  'yam  (ASm.)  Yt. /O.144.", 'Ableit.  lu  alairi+iam-;  BB.  TJ.  18.']
=== HUB zir ===
2507:'under gegeniiber zir {jlr) 'the fine or highest note of
2509:681. Zu zirak 'scharfsinnig, schlau = phi. zTrak (oder Strak)— 72 -
3701:1084. Vgl. arm. gzir (nur bei CaxCax) capo del villaggio*
3703:einnehmer'), syr. g^zTrayB 'Gensdarmen' (Hoffmann,
3704:Ausziige p. 62, Nr. 542). Ueber vazir vgl. N ft 1 d e k e ,
5769:Das moderne gzir capo del villaggio' = np. gizir hat
8771:sinnig, schlau' = phi. zTrak H. 681, oben p. 71; namak
9746:Also hat gezir u.s. w.mit vazir nichts zu thun.
```


## [2026-09-05T20:41:15.434Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2495,2515p' HUB.txt\necho \"=== leaf/page ===\"\npython3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"under gegeniiber zir\")\npages=t[:i].count('\\f')\nprint('leaf(0-based ff count)',pages)\nEOF"
}
```


### [2026-09-05T20:41:17.199Z] TOOL RESULT

```
des Suffixes a (= phi. ak) davon ab, was doch das
natiirlichste ist, wahrend NOldeke dem Worte zahr^
das sich nur in der Bedeutung 'Gift' nachweisen lasst,
als urspriingliche Bedeutung 'Galle' zuschreiben muss,
um zahr = zahra auf ap. "^zartor- = "^zartaka- gelb'
zuriickfiihren zu k5nnen. Eine Neubildung ist zahra
'Galle' so wie so fiir nicht mehr vorhandenes ''^zdr =
zd. zaras(6a) = x^^^^^ X^^Vf d. GaUe etc.
680. In den Nachtragen bemerkt Horn sehr richtig, dass
np. ztr 'hoch, hohe Stimme, hellste Saite' (= arm. zU
Sopran") mit f (nicht B) zu sprechen und also von
zer 'unter' zu trennen ist. Vgl. die LW. afgh. zBr
'under gegeniiber zir {jlr) 'the fine or highest note of
a lute, the treble in music*.
681. Zu zirak 'scharfsinnig, schlau = phi. zTrak (oder Strak)— 72 -
Ganj. 61. p. 10 gehSren als LW. kurd. zlr^ zlrek ge-
schickt, klug' ZDM6. 38, 72, afgh. zlrak acute, saga-
cious, intelligent*.
683. Arm. zipak (spat belegt) wird moderne Schreibweise fiir
iihak = arab. zlbaq, np. ^wa, jlva sein.
684. tJber die Zusammenstellung von skr. hraduni- mit ksl.
=== leaf/page ===
leaf(0-based ff count) 81
```


## [2026-09-05T20:50:58.115Z] TOOL CALL #80: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build154.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n \"entry\": 0,\n \"root\": \"En; Ndher, Ndhos, Ndhi\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"two PIE lemmas: *h₁en 'in' (Pokorny '1. en', pp. 311-314; Watkins/AHD 'en. In.') and *n̥dʰ-os / *n̥dʰ-eri / *n̥dʰ-ero- 'under' (Pokorny 'n̥dʰos, n̥dʰeri', p. 771; Watkins/AHD 'ndher-. Under.')\",\n \"verdict_reason\": None,\n \"note\": \"Every form in the box is real and correctly glossed, and the two glosses are correctly matched to the two form-groups: 'En : in, inside' = Pokorny's 1. en (311-314), 'Ndher, Ndhos, Ndhi : in, under' = Pokorny's n̥dhos, n̥dheri (771) plus the *n̥-dhi section that stands inside the en article at p. 311 ('n̥-dhī: Old Indic adhi „about, on“, Old pers. adiy „in“'). What is not right is the citation: Nourai gives only POK:311, but the Ndher/Ndhos half is a separate Pokorny lemma on p. 771, and Watkins likewise keeps 'en' and 'ndher-' apart as two roots. The consequence runs through the chart: the Persian and Greek branches all hang from *h₁en, while node #3-#5 (zǎir/zīr 'under') and the words 'under' and 'inferior' in the two English boxes hang from *n̥dher-. Merging them in one box is defensible as a presentational device (the two are formally close and Pokorny cross-refers), but the page number is incomplete and no reference at all is given for p. 771.\",\n \"note_fa\": \"جعبهٔ ریشه در واقع دو مادهٔ جداگانهٔ هندواروپایی آغازین را یکجا آورده است: *h₁en «در، درون» که پوکورنی در صفحات ۳۱۱–۳۱۴ آورده، و *n̥dʰos / *n̥dʰeri «زیر، زیرین» که مادهٔ جداگانه‌ای در صفحهٔ ۷۷۱ همان کتاب است. صورت‌ها و معناها درست‌اند و عنصر سوم (Ndhi) نیز درست است، زیرا پوکورنی در همین صفحهٔ ۳۱۱ می‌نویسد: «*n̥-dhī: سنسکریت adhi، پارسی باستان adiy در». ایراد تنها در ارجاع است: نورایی فقط POK:311 را آورده و به صفحهٔ ۷۷۱ اشاره نکرده؛ این نکته مهم است چون «زیر» و واژه‌های under و inferior در نمودار از نیمهٔ دوم ریشه می‌آیند نه از *h₁en. در مجموع ادعای نورایی درست است اما ارجاعش ناقص است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81en\"],\n \"ref_check\": [\n   {\"ref\": \"POK:311\", \"status\": \"partial\",\n    \"note\": \"POK_full.txt, lemma header 'Root / lemma: en' with 'Page(s): 311-314'; the article contains both 'enter, n̥ter' ('Old Indic antar, Avestan antarə, Old pers. antar „between“') and 'n̥-dhī: Old Indic adhi „about, on“, Old pers. adiy „in“'. It does NOT contain Ndher/Ndhos: that is a separate lemma, 'Root / lemma: n̥dʰos, n̥dʰeri, Meaning: under ... Avestan adairi „under, below“ ... Latin īnferus (*enferos, Indo Germanic *n̥dʰeros)', with 'Page(s): 771'. So POK:311 supports two thirds of the box and misses the third.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 311-314 (lemma 'en') and p. 771 (lemma 'n̥dʰos, n̥dʰeri')\", \"stance\": \"partial\",\n    \"note\": \"Two lemmas, not one: 'Meaning: in' at 311-314 vs. 'Meaning: under' at 771; Pokorny's own references are 'WP. I 125 ff., II 335 f.' for en and 'WP. I 323' for n̥dhos.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 125-127 (en, enter/n̥ter) and Bd. I 323 (*n̥dhos, n̥dheri)\", \"stance\": \"supports\",\n    \"note\": \"Bd. I 323: '*ndhos, n̥dheri „unter, sub“, ndhero- „der untere“ ... Av. adairi „unter, unterhalb“ (Praep. m. Acc. Abl.) = got. undar, ahd. untar ... lat. inferus „der untere“'; Bd. I 126: 'enter, nter „zwischen — hinein“ ... ai. antar, av. antara, ap. antar „zwischen“'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. 'en' and 'ndher-'\", \"stance\": \"partial\",\n    \"note\": \"'en. In. ... [Pok. 1. en 311.]' and separately 'ndher-. Under. 1. Germanic *under- ... 2. Latin inferus, lower: INFERIOR ... [Pok. ndhos 771.]' — Watkins too keeps the two apart.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §6497 note\", \"stance\": \"supports\",\n    \"note\": \"'ChSl. ǫtrь, Lat. inter, Skt. antar „within“, Grk. ἔντερα „entrails“, etc. Walde-P. 1.127.'\"}],\n \"nodes\": []\n}\n\nN = []\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"an-tar, an-tare, antara\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan antarə (adv./prep.) 'between, among, within', its by-form/adjective antara- 'inner', and Old Persian antar (written a-t-r, DB 1.21, 2.78, 4.32, 4.92, XPh 30, 35) 'within, among'. All three continue PIE *h₁en-ter, the *-tero- contrastive derivative of *h₁en 'in' — the same formation as Sanskrit antár, Latin inter, Oscan anter, Umbrian ander, Old Irish eter, Greek ἔντερον 'entrails'. Nourai's three shapes are simply the Avestan adverb (antarə), its written variant with final -e, and the stem antara-; the hyphen in 'an-tar' is his own analytic device, not a form.\",\n \"derivation_fa\": \"اوستایی antarə «میان، در میان» و صفت antara- «درونی»، و پارسی باستان antar (در کتیبهٔ بیستون ۱؍۲۱ و جز آن) «در، میان» هر سه از صورت هندواروپایی آغازین *h₁en-ter می‌آیند، یعنی ریشهٔ *h₁en «در» با پسوند سنجشی *-tero-. هم‌ریشه‌های آن سنسکریت antár، لاتین inter و یونانی ἔντερον است. کنت (فرهنگ پارسی باستان) و بارتولومه هر دو همین را می‌گویند؛ ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81en\"],\n \"ref_check\": [\n   {\"ref\": \"POK:311\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt, inside the 'en' article (Page(s): 311-314): 'enter, n̥ter „between - in“, en-tero- „inward“: Old Indic antar, Avestan antarə, Old pers. antar „between“, adnom. with Lok., Instr., Akk., Gen.; Old Indic antara- „internal“, Avestan antara- „inner“'.\"},\n   {\"ref\": \"DZA:57\", \"status\": \"not_checked\",\n    \"note\": \"DZA = Rashed Mohassel, Darāmadī bar Dastūr-e Zabān-e Avestāʾī (Khajeh 1364). refs_online.json records lookup_hint 'Not found.' — the 1364 edition is not digitised; only a revised e-book on taaghche.com.\"}],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. atar\", \"stance\": \"supports\",\n    \"note\": \"'atar (i.e. antar), prep. with acc., „within, among“: Av. antara, Skt. antar, Lt. inter, pIE *enter (§31). DB 1.21; 2.78; 4.32, 92; XPh 30, 35.' Also § on the suffix: 'pIE *enter „inside“, OP antar, Av. antara, Skt. antar, Lt. inter.'\"},\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, cols. 131-133 s.vv. ¹antara-, ²antara-\", \"stance\": \"supports\",\n    \"note\": \"Column header printed '¹antara- 132' in BRT.txt; the entry ends 'Kompos., — Kompar.: s. gr.¹v. — ai. ¹antara- Adj., np. andar „in, innerhalb“'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 126\", \"stance\": \"supports\",\n    \"note\": \"'enter, nter „zwischen — hinein“, en-tero- „innerlich“: ai. antar, av. antara, ap. antar „zwischen“, adnom. mit Loc. Instr. Acc. Gen.'\"}]})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"andar\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian اندر andar 'in, inside' continues Middle Persian andar (written with the Aramaic ideogram BYN, MacKenzie 'andar [BYN < A byn | M ʾndr, N ~] in, among, towards, concerning'), which is the regular reflex of Old Iranian antar(a)-: the cluster -nt- is voiced to -nd- after the nasal in Middle Persian, and the final vowel is lost. The chart's extra Persian forms belong here too: اندرون andarūn is already Middle Persian andarōn 'inside, within' (PHD s.v.), and اندران is its variant — Horn asks whether 'enderun steht für enderan'. In later New Persian andar was clipped to در dar (Hübschmann §546: 'Np. dar „hinein, in“ aus andar wie darun aus andarūn'), so andar survives mainly as a poetic archaism.\",\n \"derivation_fa\": \"«اندر» فارسی نو دنبالهٔ فارسی میانهٔ andar است (در متون پهلوی با هزوارش BYN نوشته می‌شده) که خود از ایرانی باستان antar(a)- می‌آید؛ دگرگونی آوایی آن قاعده‌مند است: ت پس از نون در فارسی میانه واکدار و به د بدل شده و واکهٔ پایانی افتاده است. «اندرون» نیز پیشاپیش در فارسی میانه به صورت andarōn آمده است. هرن (شمارهٔ ۱۱۹، ص ۲۷) و هوبشمان و مکنزی و نیبرگ همگی همین را تأیید می‌کنند؛ در فارسی متأخر «اندر» کوتاه شده و «در» شده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%A7%D9%86%D8%AF%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:27\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss p. 27 no. 119 (HRN.txt form-feed leaf 42, 'leaf = printed + 21'): '119. (i)ender „in“, vergl. enderun. ap. a(n)tar „in, innerhalb“; aw. antare; phlv. andar; ai. antár' — with the footnote 'Das Pehlevi hat auch schon andarūn (für aw. antara-)', which covers Nourai's اندرون.\"},\n   {\"ref\": \"BRT:132\", \"status\": \"supports\",\n    \"note\": \"Bartholomae's COLUMN 132: BRT.txt has the running column header '¹antara- 132' immediately before the ¹antara-/²antara- entries, and the entry closes 'ai. ¹antara- Adj., np. andar „in, innerhalb“'.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.vv. andar, andarōn\", \"stance\": \"supports\",\n    \"note\": \"'andar [BYN < A byn | M ʾndr, N ~] in, among, towards, concerning'; 'andarōn [ʾndlwnʹ | M ʾndrwn, N ~rūn] inside, within'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II, s.v. andar\", \"stance\": \"supports\",\n    \"note\": \"'— Av. (131 sq.) antara, antarə, OP antar ...; MPrthPrs ʾNDR; Paz. NP andar' — Nyberg's Bartholomae reference '131 sq.' is exactly the column Nourai cites.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §546 and p. 191\", \"stance\": \"supports\",\n    \"note\": \"§546: 'Np. dar „hinein, in“ aus andar wie darun aus andarūn, darxʷār aus andarxʷār'; and 'andar „in“ = phl. andar, zd. antare; vgl. phl. andarmōh (im Jasna) = zd. antarəmåŋha-'.\"}]})\n\nN.append({\n \"id\": 3, \"lang\": \"Avestan\", \"words\": \"hača-adairi\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both halves are genuine Avestan words: hačā 'from' (< PIE *sekʷ-eh₂, the ablative-like adverb of *sekʷ- 'follow' — Nourai's cross-reference ☞Sekw is right, cf. Latin secus), and aδairi (Nourai's 'adairi'), a preposition 'under, beneath' with the accusative and the ablative (Bartholomae, AiW s.v. aδairi: \\\"Praep. 'unter, unterhalb'\\\", with Vd. 8.69 and Yt. 17.55). What is not Avestan is the combination: *hačā aδairi is a reconstructed Old Iranian prepositional phrase set up to explain Middle Persian azēr, not an attested Avestan compound — Bartholomae himself writes it as a phrase, 'Das wäre j. hača aδarāt (mp. hač adar)' (with the ablative aδarāt of aδara- rather than the preposition aδairi), and Wiktionary reconstructs it as Old Persian *hacā-adari. So the derivation is right, the language label is loose: the etymon is Old Iranian, and its exact shape (aδairi or the ablative aδarāt) is still argued.\",\n \"derivation_fa\": \"دو جزء این صورت هر دو اوستایی‌اند: hačā «از» (هم‌ریشه با لاتین secus، از ریشهٔ *sekʷ-) و aδairi «زیر، زیرِ» که بارتولومه آن را حرف اضافهٔ اوستایی ثبت کرده است. اما ترکیب hača-adairi در اوستا مرکّبی مستقل نیست؛ بلکه گروهی حرف‌اضافه‌ای است که برای توضیح azēr پهلوی بازسازی شده است؛ خود بارتولومه صورت hača aδarāt (بایی از aδara-) را پیشنهاد کرده و ویکی‌واژه آن را پارسی باستان *hacā-adari می‌نویسد. پس این اشتقاق با احتیاط پذیرفتنی است و برچسب «اوستایی» دقیق نیست.\",\n \"sources\": [W + \"%D8%B2%DB%8C%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1677\", \"status\": \"not_found\",\n    \"note\": \"Klein 1966-67 p. 1677 is not about this. With the documented offset (KLN_1966 leaf ≈ floor(p/2)+12, calibrated on leaf 748 = p. 1469) p. 1677 falls on form-feed leaves 851-853, which carry only th- words (therio-, thermo-, thesaurus, thesis, thorax, thug). Klein's entry that does bear on the chart is 'under, prep.' at leaf 888 ≈ pp. 1747-48: 'ME., fr. OE. under ... fr. I.-E. *ndher, „under“, whence also OI. adhah, „below“, adharah, „lower“, Avestic adara-, „lower“ ... L. inferus, „lower“, infra, „below“' — it supports the *ndher- half of the root box, but says nothing about hačā-aδairi or Persian zīr.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.vv. aδairi, aδara-, aδara-naema-\", \"stance\": \"supports\",\n    \"note\": \"'j. adairi Praep. „unter, unterhalb“; 1) mit Akk.: ... V. 8.69; ... 2) mit Abl.'; and under aδara- the footnote 'Das wäre j. hača aδarāt (mp. hač adar)', with the Pahlavi version of aδara-naema- given as 'Npü.: az zēr i taxt' — i.e. Bartholomae himself equates the Avestan phrase with Pahlavi/Persian zēr.\"},\n   {\"src\": \"POK\", \"where\": \"p. 771, lemma n̥dʰos / n̥dʰeri\", \"stance\": \"supports\",\n    \"note\": \"'Avestan adairi „under, below“, Gothic undar etc. Old High German untar ... Old Indic adhara-, Avestan aδara- „the lower“ ... Latin īnferus.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 323\", \"stance\": \"supports\",\n    \"note\": \"'Av. adairi „unter, unterhalb“ (Praep. m. Acc. Abl.) = got. undar, ahd. untar und untari ..., aisl. under „unter, sub“.'\"}]})\n\nN.append({\n \"id\": 4, \"lang\": \"Pahlavi\", \"words\": \"azîr, azěr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian azēr (Book Pahlavi ʾcʹdl) 'below, under' — MacKenzie 1971: 'azēr [ʾcʹdl | N zēr] below, under', beside the simplex 'ēr [ʹdl | M ʾyr, v. azēr] down, below; low; under'. The form is the univerbation of the Old Iranian phrase *hačā aδari: hačā gives the Middle Persian preposition hač/az (initial h- lost, -č- > -z- in the unstressed proclitic), and aδari gives -ēr, with intervocalic -δ- lost and the sequence a-i contracted to ē — exactly the change that turns Avestan *daipi- into MP dēb or *(h)aiwa- into ēw. Nourai's two spellings are one word: 'azēr' is MacKenzie's reading, 'azīr' the later reading back-formed from the New Persian pronunciation.\",\n \"derivation_fa\": \"فارسی میانه azēr (در پهلوی کتابی ʾcʹdl) «زیر، پایین»؛ مکنزی آن را چنین می‌آورد: «azēr ... below, under» و صورت سادهٔ آن را هم به صورت ēr می‌آورد. این صورت حاصل یکی شدنِ گروه *hačā aδari است: hačā در فارسی میانه به hač/az بدل شده و aδari با افتادنِ دالِ میان‌واکه‌ای و همگونی a-i به ای کشیده (ē)، به ‎-ēr رسیده است. دو ضبطِ نورایی (azīr / azēr) یک واژه‌اند؛ ادعای او درست است.\",\n \"sources\": [W + \"%D8%B2%DB%8C%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\",\n    \"note\": \"the printed box carries no reference; the neighbouring boxes cite KLN:1677 (above) and BQT:1051 (below), and MacKenzie supplies the form independently.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.vv. azēr, ēr\", \"stance\": \"supports\",\n    \"note\": \"'azēr [ʾcʹdl | N zēr] below, under'; 'ēr [ʹdl | M ʾyr, v. azēr] down, below; low; under'; the English-Pahlavi part has 'below ēr, azēr' and 'under azēr, ēr'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II (glossary), greps for 'azēr', 'acēr', 'ēr'\", \"stance\": \"silent\",\n    \"note\": \"the Frahang/Kārnāmag-based glossary does not contain the word; Nyberg's corpus simply does not use it.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW s.v. aδara-naema-\", \"stance\": \"supports\",\n    \"note\": \"the Pahlavi rendering of Avestan aδara-naemāt is quoted as 'Npü.: az zēr i taxt' — the Middle Persian word in its phrase form.\"}]})\n\nN.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"zîr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian زیر 'under, below' is Middle Persian azēr with loss of the unstressed initial a-, the ordinary Persian aphaeresis (cf. MP awēšān > ēšān, MP azēr > dialectal žēr, čēr). Moʾin's footnote on the very page Nourai cites gives the chain and the sister forms: Pahlavi [azēr], from Avestan, with Kurdish žēr and Baluchi čēr beside it, referring to Hübschmann. One caution about the transliteration: Hübschmann (Persische Studien §680) insists that the word for 'under' is zēr with ē, and that the homograph zīr 'high, treble string of a lute' (Armenian zir) is a different word that must be kept apart; Nourai's 'zîr' simply reflects the modern pronunciation, in which ē and ī have merged.\",\n \"derivation_fa\": \"«زیر» فارسی نو همان azēr فارسی میانه است که الفِ آغازین بی‌تأکیدِ آن افتاده است. معین در حاشیهٔ برهان قاطع (ص ۱۰۵۱) زیرِ «زیر» می‌نویسد: «بمعنی پایین ؍ پهلوی … که از اوستایی … کردی … بلوچی …» و به هوبشمان ارجاع می‌دهد. یک نکته: هوبشمان (پژوهش‌های فارسی، بند ۶۸۰) تأکید می‌کند که واژهٔ «زیر» به معنای پایین zēr است و باید از zīr «زیرِ ساز، بمّ‌ترین زه» جدا شود؛ ضبط zîr در کتاب فقط تلفّظ امروزی را نشان می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%B2%DB%8C%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1051\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāteʾ (Moʾin's ed.) printed p. 1051 = form-feed leaf 513 of BQT_v2_pages.txt (offset printed = leaf + 538, calibrated on four legible page numbers: leaves 115→653, 214→752, 475→1013, 493→1031). That leaf carries the زیر article (running head زیرزبان گفتن, entries زیرا، زیرافکن، زیربزرگان …) and Moʾin's etymological footnote no. 4, which the OCR gives as '۴ - بمعنی پایین ؍ پهلوی […] … که ازاوستایی […]، کردی [žēr]، بلوچی … cêra … رک: … هویشمان ۱۸۰ …' — a Pahlavi + Avestan etymology for زیر 'below', exactly the chain Nourai draws (the Latin transliterations are mangled by the Persian OCR).\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. azēr\", \"stance\": \"supports\", \"note\": \"'azēr [ʾcʹdl | N zēr] below, under' — MacKenzie gives the New Persian outcome himself.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §680 (pp. 71-72)\", \"stance\": \"partial\",\n    \"note\": \"'In den Nachträgen bemerkt Horn sehr richtig, dass np. zīr „hoch, hohe Stimme, hellste Saite“ (= arm. zir „Sopran“) mit ī (nicht ē) zu sprechen und also von zēr „unter“ zu trennen ist.' — supports the etymology but corrects the vowel of Nourai's transliteration.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān p. 1051, Moʾin's footnote\", \"stance\": \"supports\", \"note\": \"see ref_check above.\"}]})\n\nN.append({\n \"id\": 6, \"lang\": \"Old Persian\", \"words\": \"adi, adyi; adi-sta; adi-var\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The simplex is real in the older handbooks: Pokorny prints inside the en article 'n̥-dhī: Old Indic adhi „about, on“, Old pers. adiy „in“', and Walde-Pokorny discusses 'die mehrdeutigen ai. adhi „an, auf“, ap. adiy „in“ (*n̥-dhi oder *ədhi, *odhi)'. It is the Old Persian counterpart of Sanskrit ádhi, a zero-grade *n̥-dhi of *h₁en. Two cautions. (1) Kent's Old Persian (1950/53) — the standard lexicon since Nourai's sources were written — has no preposition adiy at all; the reading rests on nineteenth-century interpretations of the Behistun text and is not part of the current Old Persian corpus, so 'Old Persian' is an over-confident label. (2) adi-sta and adi-var are not attested Old Persian words in any form: they are Horn's starred reconstructions, 'ap. *adi + ∟stā-' and 'ap. *adi + ∟var-', built backwards from the Pahlavi forms in the next box; Nourai prints them without the asterisk. The glosses ('in standing', 'in truth, indeed') and the cross-references ☞Stâ (*steh₂-) and ☞Wel 1 are consistent with Horn's analysis.\",\n \"derivation_fa\": \"صورت سادهٔ adiy در منابع کهن‌تر واقعاً آمده است: پوکورنی در صفحهٔ ۳۱۱ می‌نویسد «*n̥-dhī: سنسکریت adhi، پارسی باستان adiy در» و والده–پوکورنی نیز همین را با بازسازی *n̥-dhi می‌آورد. امّا دو احتیاط: یکم اینکه کنت در فرهنگ پارسی باستان (۱۹۵۰) اصلاً حرف اضافهٔ adiy را ثبت نکرده است و این خوانش امروز در پیکرهٔ پارسی باستان جایی ندارد؛ دوم اینکه adi-sta و adi-var هرگز در کتیبه‌ها نیامده‌اند و فقط بازسازی‌های ستاره‌دارِ هرن‌اند (*adi + ∟stā-، *adi + ∟var-) که نورایی ستارهٔ آن‌ها را انداخته است. پس این جعبه با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81en\"],\n \"ref_check\": [\n   {\"ref\": \"POK:311\", \"status\": \"partial\",\n    \"note\": \"POK_full.txt, en article (Page(s): 311-314): 'n̥-dhī: Old Indic adhi „about, on“, Old pers. adiy „in“; gall. intensive prefix Ande-, cymr. an(ne)- ... Old Irish ind-'. Pokorny thus supports 'adi/adiy : in' but has nothing on adi-sta or adi-var.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I (an-/ana- article, citing Brugmann Grdr. II² 2, 798 f.)\", \"stance\": \"supports\",\n    \"note\": \"'wo auch über die mehrdeutigen ai. adhi „an, auf“, ap. adiy „in“ (*n̥-dhi oder *ədhi, *odhi) und (S. 802, 860) arm. ըnd.'\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (pp. 164 ff.)\", \"stance\": \"contradicts\",\n    \"note\": \"grep of KNT.txt for 'adiy' returns only the enclitic/verbal forms (jadiy, yadiy, ni-padiy, avahya-rādiy, jadiyāmiy …); there is no headword adiy 'in'. Kent's list of Old Persian prepositions has antar, patiy, abiy, hačā, parā, pariy, upariy — not adiy.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW, Old Persian entries beginning ad-\", \"stance\": \"silent\",\n    \"note\": \"Bartholomae has 'p. *ada-kiy Adv. „damals“', 'p. adam', 'j. (p.) adav- „Wasserlauf“' — no p. adiy.\"}]})\n\nN.append({\n \"id\": 7, \"lang\": \"Pahlavi\", \"words\": \"ô-statan; ě-var; ě-vâr; ě-vân\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"ô-statan\",\n \"correct_form\": \"ē-stātan (Horn's ēstāten / ēstādan)\",\n \"derivation\": \"The three ē- forms are exactly Horn's, on the two pages Nourai cites. Horn p. 6 (under no. 16 ārī): 'phlv. ēvar (vd. 5 (146) Gl., Men.), pāz. āwar, ēvarīh ... phlv. ēvar führe ich auf ap. *adi + ∟var- zurück; adi (ai. adhi) kommt auch noch in ēstāden (und vielleicht in ēvān, ēvar) vor' — which is where Nourai's 'ě-vâr : ?' and 'ě-vân : ?' with their question marks come from (Horn's own 'vielleicht'). But the first line of the box is wrong: Horn's form is ēstātan/ēstāden, and on the very page cited (p. 20, no. 84) he expressly assigns ōstātan to a different prefix — 'phlv. ōstātan (ava + ∟stā-)' — while deriving the ancestor of ایستادن from *adi. The printed page of Nourai (PDF p. 154) plainly shows 'ô-statan', so the extraction is faithful and the error is the book's: it should read ē-stātan. A second, substantive point: Cheung's Etymological Dictionary of the Iranian Verb (2007), s.v. *staH, assigns the Middle Persian verb to the prefix *abi-, not *adi- ('(+ *abi-) MMP ʾyst-, BMP yst-, ʾ(y)st- (YKʿYMWN-) /ēst-/ „to stay, stand, be“'), so even the corrected form does not belong under this root on the current view.\",\n \"derivation_fa\": \"سه صورتِ با ایِ مجهول (ēvar، ēvār، ēvān) دقیقاً از هرن گرفته شده‌اند؛ هرن در صفحهٔ ۶ می‌نویسد که پهلوی ēvar را از *adi + ∟var- می‌گیرد و همین پیشوند در ēstāden هم دیده می‌شود. امّا سطر نخست ِجعبه خطاست: صورت درست ē-stātan است نه ō-stātan؛ خودِ هرن در همان صفحهٔ ۲۰ تصریح می‌کند که ōstātan از ava + ∟stā- است و واژهٔ دیگری است. تصویر صفحهٔ چاپی (ص ۱۲۴ کتاب) نشان می‌دهد که همین ô-statan چاپ شده، پس خطای چاپی کتاب است نه خطای خوانش اسکن. افزون بر این، چونگ (۲۰۰۷) پیشوند این فعل را *abi- می‌داند نه *adi-.\",\n \"sources\": [W + \"%D8%A7%DB%8C%D8%B3%D8%AA%D8%A7%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:6,20\", \"status\": \"partial\",\n    \"note\": \"Horn p. 6: 'phlv. ēvar ... führe ich auf ap. *adi + ∟var- zurück; adi (ai. adhi) kommt auch noch in ēstāden (und vielleicht in ēvān, ēvar (ʾYNZʾN Jer. 5, 6)) vor (vergl. KZ. 32, 581)'; Horn p. 20 no. 84: 'Ich leite np. ēstaden, später istāden, von ap. *adi + ∟stā- ab, vergl. phlv. ēvar (unter No. 16)'. The pages support the derivation but give the form as ēstātan; the same page has 'phlv. ōstātan (ava + ∟stā-)' as a separate verb, which is what the book's 'ô-statan' actually names.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.vv. ēwar, ābāz ēstādan, ōstā-\", \"stance\": \"partial\",\n    \"note\": \"'ēwar [ʾywl | M ʾywʾr] certain(ly), assured(ly)' — the word is real; MacKenzie also has 'ēstādan' (in phrases such as 'abāz ēstādan az: abandon, desist from') and separately 'awestād ... master (craftsman)', but gives no *adi- etymology and no NP ārī.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II 1470 s.v. ēvar\", \"stance\": \"partial\",\n    \"note\": \"'ēvar [ʾdwl; …] adj. true … adv. verily, certainly … Paz. ēvar; NP āvar „true, certain“' — Nyberg gives the New Persian reflex as āvar, not آری, and offers no Old Persian prefix analysis.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *staH, Middle Persian section\", \"stance\": \"contradicts\",\n    \"note\": \"'MIDDLE PERSIAN: (+ *abi-) MMP ʾyst-, BMP yst-, ʾ(y)st- (YKʿYMWN-) /ēst-/ „to stay, stand, be“ (also aux.) … || (+ *aua-) BMP ʾwstʾ- /ōstā-/ „to set out“' — the ē- prefix is *abi-, and ōstā- is the *ava- compound, confirming that 'ô-statan' names the wrong verb.\"}]})\n\nN.append({\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"îstâdan; ârî\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Both Persian words are real. ایستادن īstādan 'to stand' is Middle Persian ēstādan (ideogram YKʿYMWN-tnʹ), Horn's 'ēstaden, später istāden'; آری ārī 'yes, indeed' is Horn's no. 16, which he traces to Pahlavi ēvar. The arrow from this root, however, is what modern work rejects for īstādan: Cheung (EDIV 2007) files the Middle Persian verb under *staH with the prefix *abi- (→ ē-), and Wiktionary, following MacKenzie 1971 and Cheung, gives ایستادن < MP ēstādan < Proto-Iranian *staH < PIE *steh₂- with no *adi- and no connection to *h₁en. The prefix is the whole of Nourai's claim here, so the link to En/Ndhi falls with it. For آری the position is weaker still: Wiktionary's entry does derive it from MP ēwar < 'Old Persian adi-var', but it cites Nourai, An Etymological Dictionary, page 124 — this very page — so it is not independent confirmation; the only real authority is Horn's own conjecture of 1893, and Nyberg gives the New Persian reflex of ēvar as āvar, not ārī. آری is therefore 'plausible', ایستادن 'disputed', and the node takes the worse verdict.\",\n \"derivation_fa\": \"هر دو واژه واقعی‌اند، امّا پیوند آن‌ها با این ریشه محل اشکال است. «ایستادن» از فارسی میانهٔ ēstādan است، اما چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (۲۰۰۷) این فعل را زیر *staH با پیشوند *abi- می‌آورد نه *adi-؛ ویکی‌واژه نیز به پیروی مکنزی و چونگ همین را می‌گوید. پس پژوهش امروزی این پیکان را رد می‌کند. دربارهٔ «آری» ویکی‌واژه همان اشتقاق را می‌آورد ولی مأخذش خودِ همین صفحهٔ ۱۲۴ نورایی است (استدلال دوری)؛ مأخذ مستقل فقط حدس هرن (۱۸۹۳) است و نیبرگ بازتاب فارسی ēvar را «آور» می‌داند نه «آری».\",\n \"sources\": [W + \"%D8%A7%DB%8C%D8%B3%D8%AA%D8%A7%D8%AF%D9%86\", W + \"%D8%A2%D8%B1%DB%8C\"],\n \"ref_check\": [\n   {\"ref\": \"HRN\", \"status\": \"supports\",\n    \"note\": \"Horn p. 20 no. 84 'īstāden „stehen“, estāden, Praes. est-em ... ap. ∟stā- (ai. sthā-); pāz. estādan ... Ich leite np. estaden, später istāden, von ap. *adi + ∟stā- ab' and p. 5-6 no. 16 'ārī „fürwahr“. Kās. ore, āre, ārī' → 'phlv. ēvar ... auf ap. *adi + ∟var-'. The bare 'HRN' on the chart is Horn, and Horn does say this.\"}],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *staH\", \"stance\": \"contradicts\",\n    \"note\": \"the Middle Persian reflex is listed as '(+ *abi-)', i.e. *abi-staH, not *adi-staH; the *adi- prefix does not appear in Cheung's article at all.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, ēstādan / ēwar\", \"stance\": \"partial\",\n    \"note\": \"both Middle Persian words are there ('ēwar ... certain(ly), assured(ly)'; ēstādan in the verb phrases), but MacKenzie gives no New Persian ārī and no Old Persian prefix.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II 1470\", \"stance\": \"partial\",\n    \"note\": \"'ēvar ... Paz. ēvar; NP āvar „true, certain“' — a different New Persian outcome from Nourai's آری.\"}]})\n\nN.append({\n \"id\": 9, \"lang\": \"Greek\", \"words\": \"en-, eis-; para-en-tithenai; epi-eis-hodos\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek ἐν 'in' is the direct reflex of *h₁en; εἰς/ἐς 'into' is the extended form *ens (Watkins: 'Extended form *ens in: a. Greek eis, into: EPISODE'). παρεντιθέναι 'to put in beside' = παρά 'beside' + ἐν 'in' + τιθέναι 'to put' (root *dʰeh₁-, Nourai's ☞Dhě 2), whence the verbal noun παρένθεσις 'insertion'. ἐπεισόδιος 'coming in besides' = ἐπί 'in addition' + εἴσοδος 'entrance' (εἰς + ὁδός 'way', root *sed-, Nourai's ☞Sed), whence ἐπεισόδιον, originally what is brought in between two choric songs of a tragedy. Nourai's hyphenated 'para-en-tithenai' and 'epi-eis-hodos' are analytic spellings of the real Greek compounds, and both cross-references are correct.\",\n \"derivation_fa\": \"یونانی ἐν «در» بازتاب مستقیم *h₁en است و εἰς «به درون» از صورت گستردهٔ *ens می‌آید. παρεντιθέναι «در کنار نهادن» از παρά + ἐν + τιθέναι (ریشهٔ *dʰeh₁- «نهادن») ساخته شده و اسم فعل آن παρένθεσις است؛ ἐπεισόδιος نیز از ἐπί + εἴσοδος (= εἰς + ὁδός «راه»، ریشهٔ *sed-) است. واتکینز در پیوست فرهنگ American Heritage و کلاین و اسکیت همین را می‌گویند؛ ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/parenthesis\", \"https://www.etymonline.com/word/episode\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. en: '3. Greek en, en-, in: EN-²; ENKEPHALIN, PARENCHYMA, PARENTHESIS ... 10. Extended form *ens in: a. Greek eis, into: EPISODE; b. suffixed form *ens-ō in Greek esō, within: ESOTERIC. [Pok. 1. en 311.]'\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966-67 s.v. parenthesis\", \"stance\": \"supports\",\n    \"note\": \"'parenthesis, n. — ML., fr. Gk. παρένθεσις, „insertion“, lit. „a putting in beside“, fr. παρεντιθέναι, „to put in beside“, fr. παρά, „beside“, ἐν, „in“, and τιθέναι, „to put, place“.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Episode\", \"stance\": \"supports\",\n    \"note\": \"'Episode, a story introduced into another. (Gk.) Gk. ἐπεισόδιον, a coming in besides. — Gk. ἐπί, besides; εἴσοδος, an entrance, ἐπεισόδιος, coming in, from εἰς, in, ὁδός, a way.'\"},\n   {\"src\": \"POK\", \"where\": \"p. 311-314\", \"stance\": \"supports\",\n    \"note\": \"the en article lists the Greek material (ἔντερον, ἐντός, ἔνδον) under this root.\"}]})\n\nN.append({\n \"id\": 10, \"lang\": \"French\", \"words\": \"paranthese\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"paranthese\",\n \"correct_form\": \"parenthèse\",\n \"derivation\": \"There is no French word 'paranthese'. The French word is parenthèse, attested from the fifteenth century, taken from Medieval Latin parenthesis, itself from Greek παρένθεσις (Etymonline s.v. parenthesis: 'from French parenthèse (15c.) or directly from Medieval Latin parenthesis'). The chart on the printed page (PDF p. 154, book p. 124) does read 'paranthese', so the JSON is a faithful extraction and the misprint is Nourai's; the missing grave accent is his usual practice, but the a for e is an error. It may have been drawn from the Persian outcome, where French nasal -en- [ɑ̃] is regularly rendered آن (see the next node), but that is a Persian development, not a French spelling.\",\n \"derivation_fa\": \"در فرانسه واژه‌ای به صورت paranthese وجود ندارد؛ صورت درست parenthèse است که از سدهٔ پانزدهم میلادی از لاتینی میانه parenthesis و آن از یونانی παρένθεσις گرفته شده است. تصویر صفحهٔ چاپی نشان می‌دهد که همین paranthese در کتاب چاپ شده؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن. شاید از روی صورت فارسی «پرانتز» ساخته شده باشد، که خود حاصل بازنمودِ واکهٔ خیشومی فرانسوی [ɑ̃] با «ان» است.\",\n \"sources\": [\"https://www.etymonline.com/word/parenthesis\"],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\",\n    \"note\": \"the box carries no reference in the printed chart; the parent Greek box cites AHD, which lists PARENTHESIS among the English reflexes of en.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. parenthesis\", \"stance\": \"partial\",\n    \"note\": \"Klein routes the English word through 'ML., fr. Gk. παρένθεσις' without the French stage; the French form, where it is given (Etymonline), is parenthèse.\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. parenthesis\", \"stance\": \"contradicts\",\n    \"note\": \"'from French parenthèse (15c.) or directly from Medieval Latin parenthesis' — spelled parenthèse, never paranthese.\"}]})\n\nN.append({\n \"id\": 11, \"lang\": \"Persian\", \"words\": \"parântez\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"پرانتز parāntez 'parenthesis, round bracket' is a modern (late Qajar / Pahlavi-era) loan from French parenthèse, taken by ear: French [pa.ʁɑ̃.tɛz] gives Persian pa-rān-tez, the nasal vowel [ɑ̃] being rendered by ان ān (as in رستوران restorān, آبونمان ābonomān), and the final voiced -se [z] by ز. Moʾin tags the word [فر.] = French, which is exactly the arrow Nourai draws.\",\n \"derivation_fa\": \"«پرانتز» وام‌واژه‌ای نو (از اواخر دورهٔ قاجار به بعد) از فرانسوی parenthèse است که از راه شنیداری گرفته شده: واکهٔ خیشومی فرانسوی [ɑ̃] در فارسی به «ان» بدل شده (مانند رستوران و آبونمان) و پایانهٔ -se که در فرانسه [z] تلفّظ می‌شود به «ز» نوشته شده است. معین نیز برای آن نشانهٔ [فر.] می‌گذارد؛ پس ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D9%BE%D8%B1%D8%A7%D9%86%D8%AA%D8%B2/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:652\", \"status\": \"supports\",\n    \"note\": \"Moʾin does carry the word with a French origin tag: the online text of Farhang-e Moʾin (abadis.ir/fatofa/پرانتز) gives '(پَ تِ) [ فر. ] (اِ.) نشانه ای است قوسی شکل ( ) که برای نوشتن جملهٔ معترضه'; the same article stands in the Adena two-volume abridgement on disk (MON_part1.txt line 29918, OCRed as 'پرانتر: 2 (.) نشانه‌ای است مرکب از نیم قوس … قوسین، هلالین'). The printed page 652 of the six-volume Amir Kabir edition could not be checked directly — that edition is not on disk and page numbers are not mapped online — but the content of the cited entry is confirmed.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt line 29918 (Adena 2-vol abridgement)\", \"stance\": \"supports\",\n    \"note\": \"'پرانتز: [فر.] (ا.) نشانه‌ای است مرکب از نیم قوس عمودی بدان شکل ( ) و آن برای نوشتن جملهٔ معترضه و مانند آن بکار رود؛ قوسین، هلالین' (the OCR reads the final ز as ر).\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. parenthesis\", \"stance\": \"supports\",\n    \"note\": \"confirms the French link in the other direction: 'from French parenthèse (15c.)'.\"}]})\n\nN.append({\n \"id\": 12, \"lang\": \"English\", \"words\": \"parenthesis, episode\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English parenthesis (1560s, via Medieval Latin from Greek παρένθεσις) and episode (1670s, via French épisode or directly from Greek ἐπεισόδιον, first of the matter between two choric songs of a Greek tragedy, then 'a digression in a narrative', then from 1773 'a notable incident' and from the 1930s a broadcast instalment). Both are the English endpoints Watkins lists under en, so the arrow direct from the Greek box is right.\",\n \"derivation_fa\": \"هر دو واژهٔ انگلیسی از یونانی گرفته شده‌اند: parenthesis (دههٔ ۱۵۶۰ میلادی) از راه لاتینی میانه از παρένθεσις، و episode (دههٔ ۱۶۷۰) از ἐπεισόδιον که نخست به معنای بخشِ میانِ دو سرود همسرایان در تراژدی یونانی بوده است. واتکینز هر دو را زیر مادهٔ en فهرست کرده است؛ ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/episode\", \"https://www.etymonline.com/word/parenthesis\"],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\",\n    \"note\": \"no reference in the printed box; the parent Greek box cites AHD, which lists both PARENTHESIS and EPISODE under en.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. parenthesis\", \"stance\": \"supports\", \"note\": \"'parenthesis, n., word, clause etc. inserted into a sentence. — ML., fr. Gk. παρένθεσις …'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Episode\", \"stance\": \"supports\", \"note\": \"'Episode, a story introduced into another. (Gk.) Gk. ἐπεισόδιον, a coming in besides.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. en\", \"stance\": \"supports\", \"note\": \"'PARENTHESIS' under §3 and 'EPISODE' under §10a.\"}]})\n\nN.append({\n \"id\": 13, \"lang\": \"Germanic\", \"words\": \"in, innera, anda\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two of the three are secure: Germanic *in (Gothic in, Old English/Old High German/Old Saxon in, Old Norse í) from *h₁en / *h₁eni, and the comparative *inn(e)ra (Old English innera 'farther in, inner'). The third, *anda/*unda underlying Old English and, is only probable: Watkins writes 'Suffixed zero-grade form *n̥-dha possibly in Germanic *anda, *unda in Old English and', and Klein 'prob. fr. I.-E. *n̥dhā, whence also OI. átha, „then, and“'. Both authorities hedge, so the box is right in substance but overstates the last item; note also that *n̥-dhā is the Ndhi/Ndher half of Nourai's root box, not the En half.\",\n \"derivation_fa\": \"دو صورت نخست قطعی‌اند: ژرمنی آغازین *in (گوتی in، انگلیسی کهن in) و صورت سنجشی *inn(e)ra (انگلیسی کهن innera «درونی‌تر»). امّا *anda که انگلیسی کهن and از آن می‌آید فقط احتمالی است: واتکینز می‌نویسد «possibly» و کلاین می‌نویسد «prob. fr. I.-E. *n̥dhā». افزون بر این، *n̥-dhā به نیمهٔ دوم جعبهٔ ریشه (Ndhi/Ndher) تعلق دارد نه به En. پس این جعبه با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81en\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins s.v. en: '1. Germanic *in in: a. Old English in, in: IN; b. Germanic (comparative) *inn(e)ra in Old English innera, farther in, inner: INNER' — exact; but '11. Suffixed zero-grade form *n̥-dha possibly in Germanic *anda, *unda in Old English and, and: AND' is explicitly hedged with 'possibly'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. and, in\", \"stance\": \"partial\",\n    \"note\": \"'and, conj. — ME., fr. OE. and, rel. to OS. endi, ande, OFris. and(a), … G. und, „and“, ON. enn, en, „and, but“, prob. fr. I.-E. *n̥dhā, whence also OI. áthā, „then, and“.'\"},\n   {\"src\": \"POK\", \"where\": \"p. 311-314 (en) and p. 771\", \"stance\": \"supports\",\n    \"note\": \"the en article has 'Gothic in „in“ … Old High German Old Saxon Old English in, Old Norse í „in“, from *eni' and derivatives 'Gothic inn „in, into“, inna, innana, probably from *eni-n-'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. ndher-\", \"stance\": \"supports\",\n    \"note\": \"'ndher-. Under. 1. Germanic *under- in Old English under, under: UNDER' — the Germanic 'under' of the daughter box belongs here, not to *in/*anda.\"}]})\n\nN.append({\n \"id\": 14, \"lang\": \"English\", \"words\": \"in, and, under\",\n \"verdict\": \"plausible\",\n \"derivation\": \"'in' (Old English in) and 'and' (Old English and) follow straight from the Germanic forms in the parent box, with the caveat about *n̥-dhā noted there. 'under' does not: it is Old English under < Germanic *under-, which Watkins and Klein derive from *n̥dher- ('under, prep. — ME., fr. OE. under … fr. I.-E. *ndher, „under“, whence also OI. adhah, „below“ … Avestic adara-, „lower“ … L. inferus'), i.e. from the Ndher/Ndhos half of Nourai's root box, not from Germanic *in/*innera/*anda. Because the box merges the two PIE roots, the word is in the right chart but hangs from the wrong parent; Klein does add that Germanic *under also continues *n̥ter 'between' in the sense 'among' (OHG untar, Goth. undar 'among'), which is presumably why Nourai grouped them.\",\n \"derivation_fa\": \"واژه‌های in و and مستقیماً از صورت‌های ژرمنی جعبهٔ بالا می‌آیند، امّا under چنین نیست: این واژه از انگلیسی کهن under و ژرمنی آغازین *under- است که کلاین و واتکینز آن را از *n̥dher- «زیر» می‌گیرند، یعنی از نیمهٔ دوم جعبهٔ ریشه و نه از *in/*anda. چون نورایی دو ریشه را در یک جعبه آورده، واژه در نمودارِ درستی است ولی زیر پیکانِ نادرست. (کلاین می‌افزاید که *under ژرمنی در معنای «میان» ادامهٔ *n̥ter هم هست.)\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81en\"],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\",\n    \"note\": \"no reference in the printed box; the parent Germanic box cites AHD, whose en article ends the Germanic items with 'IN', 'INNER' and 'AND' — but not 'UNDER', which Watkins puts under ndher-.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. under, prep.\", \"stance\": \"partial\",\n    \"note\": \"'under, prep. — ME., fr. OE. under, rel. to OFris. under, OS., Goth. undar, ON. undir … fr. I.-E. *ndher, „under“, whence also OI. adhah, „below“, adharah, „lower“, Avestic adara-, „lower“, Toch. A aṅc, „under“, Arm. ըnd, „under“, L. inferus, „lower“, infra, „below“ … Cp. also I.-E. *nter, „between, among“, whence OE. under, OHG. untar, Goth. undar, „among“.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Under\", \"stance\": \"supports\",\n    \"note\": \"'Under, beneath. (E.) A.S. under; Icel. undir, Dan. Swed. under, … Goth. undar, under.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.vv. en, ndher-\", \"stance\": \"partial\",\n    \"note\": \"'IN' and 'AND' are listed under en, 'UNDER' under ndher- ('[Pok. ndhos 771.]').\"}]})\n\nN.append({\n \"id\": 15, \"lang\": \"Latin\", \"words\": \"intrô, intrâ, inter\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin intrō 'inward, within' and intrā 'inside, within' are the suffixed form *h₁en-t(e)ro- (the same *-tero- comparative as Avestan antara-), and inter 'between, among' is *h₁en-ter, the exact match of Avestan antarə/Old Persian antar in node #1 and of Sanskrit antár. Walde-Pokorny group them all in one paragraph: 'lat. enter, inter „zwischen“ … intro, intra, intrin-secus, interus „innerlich“, interior, intimus, intestinus'; Old Latin still has the older enter.\",\n \"derivation_fa\": \"لاتینی intrō «به درون» و intrā «درون، درونِ» از صورت پسونددار *h₁en-t(e)ro- و inter «میان» از *h₁en-ter است؛ یعنی inter دقیقاً همان ساختِ antarə اوستایی و antar پارسی باستان و antár سنسکریت است. والده–پوکورنی و واتکینز و باک همگی همین را می‌گویند؛ صورت کهن‌تر لاتینی enter بوده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81en\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. en: '4. Suffixed form *en-t(e)ro- in: a. Latin intrō, inward, within: INTRO-; … b. Latin intrā, inside, within: ENTER, INTRA- … 5. Suffixed form *en-ter in Latin inter, inter-, between, among: ENTRAILS, INTER-, INTERIM, INTERIOR, INTERNAL.'\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 126-127\", \"stance\": \"supports\",\n    \"note\": \"'lat. enter, inter „zwischen“, adnom. m. Acc. … intro, intra, intrin-secus, interus „innerlich“, interior, intimus, intestinus (s. u.), osk. entrai „*Interae“ … osk. anter, umb. anter, ander „inter“.'\"},\n   {\"src\": \"POK\", \"where\": \"p. 311-314\", \"stance\": \"supports\",\n    \"note\": \"the same paragraph appears in Pokorny: 'Latin enter, inter prep. with acc. „between, among, amid“ … intro, intra, intrin-secus, interus „internal“, interior, intimus, intestinus.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §6497 note\", \"stance\": \"supports\",\n    \"note\": \"'Lat. inter, Skt. antar „within“ … Walde-P. 1.127.'\"}]})\n\nN.append({\n \"id\": 16, \"lang\": \"English\",\n \"words\": \"inter-, international, interest, interface, intestine, intimate, in- 1, en-, inferior\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Most of the list is right but the parent box does not cover all of it. inter-, international and interest are Latin inter- compounds (interest = inter + est 'it is between, it concerns'); interface is a nineteenth/twentieth-century English coinage on the same prefix. But intestine is from Latin intestinus < intus 'within' (Watkins §8a, 'Suffixed form *en-tos … Latin intus, within, inside: DEDANS, INTESTINE'); intimate is from the superlative intimus (§6); in-¹ and en-¹ are from Latin in / Greek ἐν (§§2-3) — all of these are from *h₁en but not from intrō/intrā/inter, the three words actually printed in the Latin box. inferior is different again: Latin īnferior is the comparative of īnferus < *n̥dʰeros (Watkins 'ndher- … 2. Latin inferus, lower: INFERIOR'; Skeat: 'Inferior. (F.–L.) O.F. inferieur, L. inferiorem, acc. of inferior, lower, comp. of inferus, low, nether'), so it belongs to the Ndher half of the root box and not to the Latin box above it at all.\",\n \"derivation_fa\": \"بیشتر این واژه‌ها درست‌اند امّا همه از سه واژهٔ جعبهٔ لاتینی بالا نمی‌آیند: inter- و international و interest و interface از inter، امّا intestine از لاتینی intus «درون»، intimate از صفت برترین intimus، و in-1 و en- از لاتینی in و یونانی ἐν است. مهم‌تر اینکه inferior از لاتینی īnferus < *n̥dʰeros است، یعنی از نیمهٔ Ndher ریشه و نه از inter/intrā/intrō. پس جعبه درست است ولی پیکانِ آن برای چند واژه دقیق نیست.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81en\"],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\",\n    \"note\": \"no reference in the printed box; the parent Latin box cites AHD, and Watkins's en article indeed ends with the English capitals INTRO-, INTRODUCE, ENTER, INTRA-, INTER-, INTERIM, INTERIOR, INTERNAL, INTIMA, INTIMATE, INDUSTRY, DEDANS, INTESTINE, ENTERIC … but INFERIOR appears only under ndher-.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins s.vv. en §§2-9, ndher- §2, and the index\", \"stance\": \"partial\",\n    \"note\": \"the index line reads 'INFERIOR ndher- INFERNAL ndher- INFERNO ndher- … INFRA- ndher-', while INTIMATE, INTESTINE and INTER- are indexed to en.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Inferior\", \"stance\": \"supports\",\n    \"note\": \"'Inferior. (F.–L.) O.F. inferieur, L. inferiorem, acc. of inferior, lower, comp. of inferus, low, nether … from Skt. adhas adv., underneath, low, down.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. in-, pref.; under\", \"stance\": \"partial\",\n    \"note\": \"'in-, pref. meaning in, into, toward, up, against … — E. in or L. in; see in, prep. … Cp. em-, en-.' — i.e. in-¹/en-¹ come from Latin in, not from inter/intrā.\"}]})\n\nroot[\"nodes\"] = N\nroot.pop(\"verdict_reason\", None)\n\ndoc = {\"pdf_page\": 154, \"book_page\": 124,\n       \"verified_by\": \"claude-opus-5\", \"verified_on\": \"2026-09-05\",\n       \"entries\": [root]}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-154.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build154.py"
}
```


### [2026-09-05T20:51:00.610Z] TOOL RESULT

```
ok
```


## [2026-09-05T20:51:05.295Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-154.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 154"
}
```


### [2026-09-05T20:51:06.948Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 8, 'plausible': 5, 'transcription_suspect': 2, 'disputed': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 8, 'not_checked': 6, 'not_found': 1, 'partial': 3}
books consulted: {'supports': 29, 'silent': 2, 'partial': 11, 'contradicts': 4} | by book: {'KLN': 6, 'PHD': 5, 'BRT': 4, 'WLD': 4, 'NYB': 4, 'POK': 4, 'SKT': 4, 'AHD': 4, 'KNT': 2, 'HUB': 2, 'CHEUNG': 2, 'Etymonline': 2, 'BQT': 1, 'MON': 1, 'SYN': 1}
```


## [2026-09-05T20:51:23.127Z] AGENT

Done. `data/verification/page-154.json` written; `verify_check.py 154` reports 16/16 nodes and **0 PROBLEM lines**.

**Page 154 (book p. 124) — root `En; Ndher, Ndhos, Ndhi`, 1 entry, 16 nodes**
- Root: **plausible** — forms/glosses correct, but the box merges two Pokorny lemmas (*h₁en* p. 311–314 and *n̥dʰos/n̥dʰeri* p. 771) and cites only POK:311.
- Nodes: 8 confirmed, 5 plausible, 2 transcription_suspect, 1 disputed.
- Ref checks: 8 supports, 3 partial, 1 not_found, 6 not_checked (all "no reference printed" boxes plus DZA:57, which is not digitised).

**Flagged items**
- **#7 Pahlavi `ô-statan` — transcription_suspect (book's error).** Horn (p. 20 no. 84, the page Nourai cites) derives Persian ایستادن from *ap. \*adi + √stā-* as **ēstātan**, and on the same page assigns **ōstātan** to *ava + √stā-*, a different verb. Should read `ě-statan`. PDF p. 154 prints `ô-statan`, so the extraction is faithful.
- **#10 French `paranthese` — transcription_suspect (book's error).** No such French word; it is **parenthèse**. Printed page confirms `paranthese`.
- **#8 Persian `îstâdan; ârî` — disputed.** Cheung (EDIV, s.v. *staH) files MP /ēst-/ under prefix **\*abi-**, not \*adi-, and Wiktionary follows MacKenzie+Cheung — the arrow from this root fails for ایستادن. For آری, Wiktionary's supporting entry cites **Nourai p. 124 itself** (circular); only Horn's 1893 conjecture stands, and Nyberg gives MP ēwar → NP *āvar*, not آری.
- **KLN:1677 (node #3) — not_found.** Klein p. 1677 is in the *th-* range (therio–thesis); the relevant Klein entry is *under* (≈ p. 1747). Possibly a mis-citation in the book.

**No extraction errors** — the JSON matches the printed page throughout (incl. `پرانتز`, `اندران ، اندرون`, `ô-statan`, `paranthese`).

Page image archived to `data/verification/sources/refs/ocr/BOOK/154.png`; 8 web sources archived via `fetch_source.py`. Notable positive finding: BQT:1051 verified exactly — Borhān leaf 513 of `BQT_v2_pages.txt` (offset calibrated on four legible page numbers) carries the زیر article with Moʾin's Pahlavi/Avestan footnote.
