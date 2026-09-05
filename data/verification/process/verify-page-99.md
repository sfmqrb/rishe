# Verification process log — verify-page-99


## [2026-09-05T14:36:20.026Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 99 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-99.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-99.json. Write /home/sfmqrb/git/rishe/data/verification/page-99.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 99` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:36:21.533Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:36:22.201Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:36:22.221Z] TOOL RESULT

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


## [2026-09-05T14:36:22.346Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-99.txt"
}
```


### [2026-09-05T14:36:22.373Z] TOOL RESULT

```
1	=== PDF page 99 (book page 69) ===
2	--- entry 0 ---
3	ROOT [Pahlavi] Bistak : pistachio  (refs UNV:78)
4	#1 (parent #0) [Persian] refs=PLA:210; AHD:998 | pesteh «پسته» : pistachio, figuratively used to mean (smiling) lips
5	  #2 (parent #1) [Greek] refs=AHD:998; PLA:210; SKT:394; KLN:1190 | pistake, pistakion | NOTE: MON:2545 claims these Greek words were borrowed from Arabic.
6	    #3 (parent #2) [Latin] refs=AHD:998 | pistacia, pistacium
7	      #4 (parent #3) [Italian] refs=KLN:1190 | pistacchio
8	        #5 (parent #4) [English] refs=AHD:998 | pistachio
9	    #6 (parent #2) [Arabic] refs=PLA:210 | fustug, fostoq : pistachio | NOTE: MON:2545 claims this word is taken from Aramaic and then passed to Greek.
10	      #7 (parent #6) [Persian] refs=MON:2545 | fostoğ «فُستُق ( فستقی )» : pistachio
11	      #8 (parent #6) [French] refs=AHD:535 | fustic, fistic
12	        #9 (parent #8) [English] refs=AHD:535 | fustic, fistic
13	--- entry 1 ---
14	ROOT [Arabic] B.k.r : he rose up early  (refs KLN:44)
15	#1 (parent #0) [Arabic] refs=KLN:44 | bîkr : early, fresh, young, virgin ; al-bakrah : the young camel
16	  #2 (parent #1) [Persian] refs=FVA:51 | bekr «بکر ( بکارت )» : fresh, young, new, virgin ; ebtekâr «ابتکار ( مبتکر )» : ingenuity, fresh idea
17	  #3 (parent #1) [Spanish] refs=AHD:29; KLN:44 | al-bacora : "the young camel", referring to a large fish
18	    #4 (parent #3) [English] refs=AHD:29; KLN:44 | albacore : a large fish
19	
```


## [2026-09-05T14:36:25.303Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-99.json",
 "description": "Read source JSON for page 99"
}
```


### [2026-09-05T14:36:25.353Z] TOOL RESULT

```
{
  "pdf_page": 99,
  "book_page": 69,
  "entries": [
    {
      "root": {
        "name": "Bistak",
        "lang": "Pahlavi",
        "refs": "UNV:78",
        "gloss": "pistachio"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "PLA:210; AHD:998",
          "words": [
            {"translit": "pesteh", "gloss": "pistachio, figuratively used to mean (smiling) lips", "script": "پسته"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "گرچه از کبر ، سخن با من درویش نگفت - جان فدای شکرین پستهٔ خاموشش باد",
            "poet": "Hâfez"
          }
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Greek",
          "refs": "AHD:998; PLA:210; SKT:394; KLN:1190",
          "words": [
            {"translit": "pistake, pistakion", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "MON:2545 claims these Greek words were borrowed from Arabic.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": "AHD:998",
          "words": [
            {"translit": "pistacia, pistacium", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Italian",
          "refs": "KLN:1190",
          "words": [
            {"translit": "pistacchio", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:998",
          "words": [
            {"translit": "pistachio", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 2,
          "lang": "Arabic",
          "refs": "PLA:210",
          "words": [
            {"translit": "fustug, fostoq", "gloss": "pistachio", "script": null}
          ],
          "script_extra": null,
          "note": "MON:2545 claims this word is taken from Aramaic and then passed to Greek.",
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:2545",
          "words": [
            {"translit": "fostoğ", "gloss": "pistachio", "script": "فُستُق ( فستقی )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "ماه تمام بر فلک سبز پوش نیست - چون عارض تو پیش خط سبز فستقی",
            "poet": "Ahmad Ebn Mohammad"
          }
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "French",
          "refs": "AHD:535",
          "words": [
            {"translit": "fustic, fistic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD:535",
          "words": [
            {"translit": "fustic, fistic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "B.k.r",
        "lang": "Arabic",
        "refs": "KLN:44",
        "gloss": "he rose up early"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:44",
          "words": [
            {"translit": "bîkr", "gloss": "early, fresh, young, virgin", "script": null},
            {"translit": "al-bakrah", "gloss": "the young camel", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:51",
          "words": [
            {"translit": "bekr", "gloss": "fresh, young, new, virgin", "script": "بکر ( بکارت )"},
            {"translit": "ebtekâr", "gloss": "ingenuity, fresh idea", "script": "ابتکار ( مبتکر )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Spanish",
          "refs": "AHD:29; KLN:44",
          "words": [
            {"translit": "al-bacora", "gloss": "\"the young camel\", referring to a large fish", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:29; KLN:44",
          "words": [
            {"translit": "albacore", "gloss": "a large fish", "script": null}
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


## [2026-09-05T14:36:25.937Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T14:36:25.978Z] TOOL RESULT

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


## [2026-09-05T14:36:30.736Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['UNV','PLA','AHD','SKT','KLN','MON','FVA','FVQ','LKT','LEW','HJB','WEB','FSD','AFM','TAD','ARB','AFA','DEV','PHN','BQT','ARY','PHD','HRN','HUB']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\""
}
```


### [2026-09-05T14:36:33.504Z] TOOL RESULT

```
UNV {"title": "J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Text Der König Husrav und sein Knabe', Heidelberg diss. 1917]", "edition_found": "1917 German dissertation edition (text + glossary); 1963 Paris ed. not found", "kind": "archive_djvu", "url": "https://archive.org/details/derpahlavitextde00unva", "identifier": "derpahlavitextde00unva", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt", "page_offset": "leaf = printed + 2 (e.g. leaf 9 = p.7); only 48 leaves. local file has \\f between leaves (0-based l

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
```


## [2026-09-05T14:36:43.643Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 pistachio ===\"; grep -n -i \"pistachio\" KLN_1966.txt | head -20\necho \"=== KLN 1971 pistachio ===\"; grep -n -i \"pistachio\" KLN_1971.txt | head -20\necho \"=== SKT pistachio ===\"; grep -n -i \"pistach\" SKT.txt | head -20\necho \"=== AHD pistach ===\"; grep -n -i \"pistac\\|fustic\" AHD_watkins1985.txt | head -20\necho \"=== UNV bistak ===\"; grep -n -i \"bistak\\|pistak\\|pistachi\" UNV.txt | head -20"
}
```


### [2026-09-05T14:36:43.731Z] TOOL RESULT

```
=== KLN 1966 pistachio ===
15604:pistachio.
28932:piss,  intr.  and  tr.  v.  —  ME.  pissen,  fr.  OF.  pissier (F.  pisser),  of  imitative  origin, pistachio,  n.  —  It.  pistacchio  (whence  also  F. pistache,  Sp.  pistacho),  fr.  L.  pistacium,  fr.  Gk. mardbaov,  ‘pistachio  nut’,  fr.  mar <&xy],  ‘pista¬ chio  tree’,  fr.  Pers.  pistah,  ‘pistachio  nut’.  Cp. fustic.
=== KLN 1971 pistachio ===
98960:pistachio. 
183261:pistachio, n. — It. pistacchio (whence also F. 
183263:moraxtov, ‘pistachio nut’, fr. 7U<iTdcx7), ‘pista- 
183264:chio tree’, fr. Pers. pistah, ‘pistachio nut’. Cp. 
=== SKT pistachio ===
14076:Piatachio.  Pistaoho,  the  mit  of  1 ccrtiiin  tree.  (Span.  —  L.  —  Gk.  —  Pet*l Span,  pistacho.  ••  L.  pistacimm.  —  Gk wxcramov,  a  nut  of  the  tree  called  rtviici.
14077:—  Pers.  pistah,  the  pistachio  nut.
23611:Spanish  from  Latin  from  Greek  from  ^ Persian:  pistachio  (pistacho).
=== AHD pistach ===
=== UNV bistak ===
```


## [2026-09-05T14:36:45.035Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN albacore ===\"; grep -n -i \"albacore\" KLN_1966.txt KLN_1971.txt | head -20\necho \"=== KLN bikr ===\"; grep -n -i \"bakrah\\|bikr\\|bakara\" KLN_1966.txt | head -30\necho \"=== SKT albacore ===\"; grep -n -i \"albacore\" SKT.txt | head"
}
```


### [2026-09-05T14:36:45.117Z] TOOL RESULT

```
=== KLN albacore ===
KLN_1971.txt:10402:albacore, n., a species of tunny ( zool .) — Sp. alba- 
KLN_1971.txt:102062:germon, n., the albacore (Ger mo alalunga). — 
KLN_1966.txt:2099:albacore,  n.,  a  species  of  tunny  ( zool .)  —  Sp.  alba- cora,  fr.  Arab.  albakrah,  ‘the  young  camel’,  fr.  al-, ‘the’,  and  the  collective  noun  bakr,  ‘young camels',  whence  bdkrah,  ’young  she-camel’,  rel. to  bikr,  ‘virgin,  woman  having  first  child’,  from the  stem  of  the  verb  bdkara,  ’he  rose  early,  did something  early’,  and  to  Heb.  bekhor,  ‘first born’,  bikhordh,  ‘the  right  of  first  born’,  bikh- rdA,  ‘young  camel’,  bikkurd1',  ‘first  ripe  fig’, bikkurfm,  ‘first  fruits’,  Ethiop.  bakur,  ‘first bom’.
KLN_1966.txt:16069:Derivatives:  germination  (q.v.),  germinat-ive, adj.,  germinative-ly,  adv.,  germinat-or,  n. germination,  n.  —  L.  germinatio,  gen.  -onis,  ‘a sprouting  forth,  budding’,  fr.  germinatus,  pp.  of germinare.  See  prec.  word  and  -ion. germon,  n.,  the  albacore  ( Germo  alalunga).  ■ — F.,  of  unknown  origin, geront-,  form  of  geronto-  before  a  vowel, gerontic,  adj.,  pertaining  to  old  age.  —  Gk.  ye- povxixoi;,  ‘pertaining  to  an  old  man’,  fr.  ycpcov, gen.  yipovzoq,  ‘old  man’.  See  geronto-  and  -ic. geronto-,  before  a  vowel  geront-,  combining  form
=== KLN bikr ===
2099:albacore,  n.,  a  species  of  tunny  ( zool .)  —  Sp.  alba- cora,  fr.  Arab.  albakrah,  ‘the  young  camel’,  fr.  al-, ‘the’,  and  the  collective  noun  bakr,  ‘young camels',  whence  bdkrah,  ’young  she-camel’,  rel. to  bikr,  ‘virgin,  woman  having  first  child’,  from the  stem  of  the  verb  bdkara,  ’he  rose  early,  did something  early’,  and  to  Heb.  bekhor,  ‘first born’,  bikhordh,  ‘the  right  of  first  born’,  bikh- rdA,  ‘young  camel’,  bikkurd1',  ‘first  ripe  fig’, bikkurfm,  ‘first  fruits’,  Ethiop.  bakur,  ‘first bom’.
=== SKT albacore ===
```


## [2026-09-05T14:36:55.804Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== fustic KLN66 ===\"; grep -n -i \"fustic\\|fustoc\\|fustet\" KLN_1966.txt | head -10\necho \"=== fustic SKT ===\"; grep -n -i \"fustic\" SKT.txt | head -10\necho \"--- page markers near 2099 ---\"; sed -n '2060,2110p' KLN_1966.txt | grep -n \"\" | grep -i -E \"^\\s*[0-9]+:\\s*[0-9]{1,4}\\s*$\" | head\necho \"--- raw context 2090-2102 ---\"; sed -n '2090,2102p' KLN_1966.txt"
}
```


### [2026-09-05T14:36:57.477Z] TOOL RESULT

```
=== fustic KLN66 ===
15603:fustic,  n.,  the  wood  of  a  Mexican  tree  (Chloro- phora  tinctoria)  and  the  yellow  dye  it  yields.  — Sp.  fas  toe,  fr.  Arab,  fustuq,  fr.  Pers.  pistah.  See
24412:morin,  n.,  a  yellow  coloring  matter  found  in  the  fus¬ tic  tree  ( chem ). —  F .morine,  coined  by  the  French chemist  Michel-Eugene  Chevreul  (1786-1889) in  1837  fr.  ModL.  Morus  (see  Morus)  and  suff. -ine  (see  chem.  suff.  -ine);  so  called  by  him  be¬ cause  the  genus  Morus  formerly  included  the fustic  tree.
28932:piss,  intr.  and  tr.  v.  —  ME.  pissen,  fr.  OF.  pissier (F.  pisser),  of  imitative  origin, pistachio,  n.  —  It.  pistacchio  (whence  also  F. pistache,  Sp.  pistacho),  fr.  L.  pistacium,  fr.  Gk. mardbaov,  ‘pistachio  nut’,  fr.  mar <&xy],  ‘pista¬ chio  tree’,  fr.  Pers.  pistah,  ‘pistachio  nut’.  Cp. fustic.
=== fustic SKT ===
--- page markers near 2099 ---
6:43
41:44
--- raw context 2090-2102 ---
aicnemy
Derivatives :  alarm ,  tr.  v.,  alarm-able,  alarm-ed, adjs.,  alarm-ed-ly,  adv.,  alartn-ing,  adj.,  alarm- ing-ly,  adv.,  alarmist  (q.v.) alarmist,  n.,  i)  one  who  starts  alarming  rumors; 2)  one  easily  frightened.  —  A  hybrid  coined  fr. F.  alarme  (see  prec.  word)  and  -ist,  a  sufT.  of Greek  origin.
alarum,  n.  —  A  poetical  variant  of  alarm, alary,  adj.,  pertaining  to  wings.  —  L.  alarms,  fr.
ala,  ‘wing’.  See  aisle  and  -ary  and  cp.  alar, alas,  interj.  —  F.  helas,  composed  of  he,  a  word
of  imitative  origin,  and  las,  ‘tired,  weary’,  in  OF. also  meaning  ‘unfortunate’,  fr.  L.  lassus,  ‘tired, weary’.  See  lassitude  and  late.  E.  alas  was  prob. influenced  in  form  by  alack  (q.v.)
Alastor,  n.,  son  of  Neleus  and  brother  of  Nestor in  Greek  mythology;  fig.  used  in  the  sense  of  an avenging  spirit.  —  Gk.  ’  AXacrrap,  lit .  ‘wanderer’, a  derivative  of  dXao&ai,  ‘to  wander,  roam’.  See hallucinate  and  cp.  the  first  element  in  Aleo- chara.
alas  trim,  n.,  a  mild  form  of  smallpox  ( med .)  — Port.,  fr.  alastrar,  ‘to  ballast  a  ship’,  fig.  ‘to cover  all  over,  spread,  strew’,  fr.  a  (fr.  L.  ad), ‘to’,  and  lastro,  ‘ballast’,  fr.  G.  Last,  ‘load,  charge, burden,  weight’.  See  ad-  and  last,  ‘burden’, alate,  alated,  adj.,  winged.  —  L.  Hiatus,  ‘winged’, fr.  ala,  ‘wing’.  See  aisle  and  adj.  suff.  -ate  and cp.  words  there  referred  to. alatern,  alaternus,  n,,  a  buckthorn  ( Rhamnus  ala- ternus).  —  L.  alaternus,  ‘buckthorn’,  of  Etrus¬ can  origin.
Alauda,  n.,  a  genus  of  birds,  the  skylark  (orni- thol.)  —  ModL.,  fr.  L.  alauda,  ‘lark’,  of  Gaulish origin,  and  prob.  literally  meaning  ‘tufted’, alazor,  n.,  the  safflower.  —  Sp.,  fr.  Arab,  al-usfur, in  vulgar  pronunciation  al-'osj'dr,  fr.  al-,  ‘the’, and  'usfhr,  resp.  osfdr,  ‘safflower’.
alb,  a  long  white  vestment.  — -ML.  alba  for  L. alba  ( vestis ),  ‘while  (garment)’,  fern,  of  albus, ‘white’;  cogn.  with  Gk.  aXcp 64,  ‘dull-white  lep¬ rosy’,  SXcpi,  aXtptvov,  ‘barley  meal’,  OHG. albi3,  elbi3.  OE.  elfet,  ‘swan’,  lit.  ‘the  white bird’,  OSlav.,  Russ,  lebedi,  Serb,  labud,  Pol. labgdi,  Czech  labud,  ‘swan’,  for  orig.  *olh-edi, *olb-fdi,  *olb-(>di,  ‘the  white  bird’.  Cp.  also  Arm. alauni,  ‘white  pigeon,  dove',  Alb.  el'p,  el'bi,  ‘bar¬ ley’,  Hitt,  alpash,  ‘cloud’.  Cp.  abele,  ablet,  al¬ bedo,  albescent,  albino,  albite,  albo-,  Albuca,  al¬ bugo,  album,  albumen,  albumin,  alburnum,  at- phitomancy,  aubade,  aube,  auburn,  daub.
albacore,  n.,  a  species  of  tunny  ( zool .)  —  Sp.  alba- cora,  fr.  Arab.  albakrah,  ‘the  young  camel’,  fr.  al-, ‘the’,  and  the  collective  noun  bakr,  ‘young camels',  whence  bdkrah,  ’young  she-camel’,  rel. to  bikr,  ‘virgin,  woman  having  first  child’,  from the  stem  of  the  verb  bdkara,  ’he  rose  early,  did something  early’,  and  to  Heb.  bekhor,  ‘first born’,  bikhordh,  ‘the  right  of  first  born’,  bikh- rdA,  ‘young  camel’,  bikkurd1',  ‘first  ripe  fig’, bikkurfm,  ‘first  fruits’,  Ethiop.  bakur,  ‘first bom’.
44
albatross,  n.  —  Port  alcatraz,  ‘cormorant,  peli¬ can’  (whence  also  F.  albatros),  a  variant  of alcatruz,  ‘the  bucket  of  a  water  wheel',  fr.  Arab. al-qddds,  'machine  for  drawing  water;  jar’,  fr. al-,  ‘the’,  and  Gk.  xd8o?,  ‘jar’,  which  is  a  loan word  from  Heb.  kadh,  of  s.m.  The  name  was orig.  applied  to  the  pelican  as  ‘the  water  carrier’, i.e.  the  bird  that  carries  water  in  its  pouch.  For sense  development  cp.  Arab,  saqqd,  ‘pelican’, lit.  ‘water  carrier’.  The  alteration  of  Port,  alca¬ traz  to  E.  albatross  (after  L.  albus,  ‘white’)  was prob.  suggested  by  the  white  color  of  the  alba¬ tross.  ModPort.  albatroz  has  been  reborrowed fr.  F.  albatros.  Cp.  alcatras.
Alban,  masc.  PN.  —  L.  Albanus,  lit.  ‘of  Alba’,  fr.
```


## [2026-09-05T14:36:57.487Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT pistazie/fustuq ===\"; grep -n -i \"pistaz\\|fustuq\\|fustuk\\|pistak\" LKT.txt | head -20\necho \"=== DEV pistache ===\"; grep -n -i \"pistach\\|fustoc\\|fustet\" DEV.txt PHN.txt | head -20\necho \"=== AFA fustuq ===\"; grep -n -i \"fustuq\\|fustuk\\|Pistazie\" AFA.txt | head -20"
}
```


### [2026-09-05T14:36:57.578Z] TOOL RESULT

```
=== LKT pistazie/fustuq ===
1554:'Pistazie,  Pistazienbaum'  [aus  pers.  fistik, woraus  auch  gr.  iriaTciKiov] ;  hieraus rum.  fistic,  sp.  alföstigo,  alföcigo,  al- fönsigo,  pg.  alfostico  'dass.'.    [DE  115.
3802:Ebenso  tk.  fystyk,  ar.  fistik,  fustak 'Pistazie,  Pistacia  vera';  hieraus  rum. fistic  'Pistazien bäum',  fistica  'Pistazie', it.  pistacchio,  frz.  pistache,  sp.  pistacho, prov.  festnc,  pg.  festuc;  mit  ar.  Art.  sp. alfonstgo,  alfostigo,  wohl  auch  frz. pasteque  'Melone'.  [DE  115.  Eguilaz 169.    ML  6535.
=== DEV pistache ===
DEV.txt:249:les  doubles  l'orincs  cadi  et  alcade  j  hhandjar  et  alfange,  pro- viennenî  d'un  même  terme  diiïéremment  accentué.  Mais cadi  et  khamJjar  sont  de  ^simples  transcriptions  de  l'arabe, qu'on  ne  saurait  invocpier  ici.  J'aime  mieux  m'appuyer sur  l'exemple  cpie  m'a  fourni  ]\f .  Defrémery  ^  :  (^'jLmJùS  al- fosioq,  pistache,  est  devenu  en  espagnol  alfostigo^  dont l'analogie  avec  albcrchlgo  est  évidente.  On  peut  y  joindre (dhondiga ,  hôtellerie,  de  ^.XjLiJl  aJ-fondouq^,  et  alhoiidiga, boulette,  de  (3*^^-!^^  aJhondouq.
=== AFA fustuq ===
5217:^j?v f »Pistazie" ist als Fremdwort schon Ton den Ara-
```


## [2026-09-05T14:37:07.818Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- page marker after fustic (15603) ---\"; sed -n '15595,15615p' KLN_1966.txt | grep -nE \"^[0-9]{2,4}$\"\necho \"--- around 15600-15606 ---\"; sed -n '15598,15608p' KLN_1966.txt\necho \"--- page marker after pistachio (28932) ---\"; sed -n '28925,28945p' KLN_1966.txt | grep -nE \"^[0-9]{2,4}$\""
}
```


## [2026-09-05T14:37:09.084Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA context ===\"; sed -n '5205,5235p' AFA.txt\necho \"=== AFM فستق ===\"; grep -n \"فستق\\|الفستق\" AFM_pages.txt | head -10\necho \"=== TAD فستق ===\"; grep -n \"فستق\" TAD_pages.txt | head -10"
}
```


### [2026-09-05T14:37:09.660Z] TOOL RESULT

```
--- page marker after fustic (15603) ---
15:632
--- around 15600-15606 ---
fuss,  n.,  bustle.  —  Prob.  of  imitative  origin. Derivatives:  fuss,  intr.  and  tr.  v.,  fass-y,  adj., fuss-i-ly,  adv.,  fuss-i-ness,  n.
fust,  n.,  1)  the  shaft  of  a  column  (archil.)',  2)  a strong  moldy  smell.  —  OF.  fast  (F  .fat),  ‘shaft, cask’,  fr.  L.  fastis,  ‘stick,  staff,  cudgel,  club’, whence  also  It.  fusto,  ‘stem,  stalk,  trunk’, OProven?.  fast,  ‘staff,  cask’.  L.  fastis  cor¬ responds  to  Gaul.  *bustis,  ‘trunk  of  a  tree (whence  O Proven?,  bust,  of  s.m.).  For  Teut. cognates  of  L.  fiistis  see  bush  and  cp.  words there  referred  to.  E.  beat  is  not  cognate.  Cp. fustian,  fustigate.
Derivatives:  fust-y,  adj.,  moldy,  fast-i-ness,  n. fustanella,  n.,  a  short  skirt  of  stiffened  linen.  —  F. fastanelle,  fr.  It.  fustanella,  dimin.  of  fustagno, fr.  ModGk.  (poucr-rdvi,  fr.  ML.  fustaneum.  See next  word  and  -ella.
fustian,  n.,  thick  cloth  of  cotton.  —  Orig.  ‘a  coarse cloth  of  cotton’,  fr.  ME.  fastyane,  fr.  OF.  fus- taigne,  fustaine  (F.  fataine),  fr.  ML.  fustaneum, translation  of  Septuagint  Greek  X(va  £iiXiva, ‘cotton  of  wood’,  i.e.  ‘tissue  of  cotton  coming from  a  tree’.  Fustaneum  is  prop,  an  adjective formed  from  L.  fiistis,  ‘stick,  staff’;  see  fust. For  sense  development  cp.  G.  Baumwolle,  ‘cot¬ ton’,  lit.  ‘wool  of  a  tree’,  and  the  explanation  of ML.  xylinum  (=  Gk.  £uXivov)  as  lana  de  ligno, ‘wool  coming  from  wood’.  Arabic  fushtdn  is  a Romance  loan  word.  The  usual  derivation  of fustian  fr.  Fostat,  name  of  a  suburb  of  Cairo,  is untenable.  Cp.  fustanella.
Derivative:  fustian,  adj.
fustic,  n.,  the  wood  of  a  Mexican  tree  (Chloro- phora  tinctoria)  and  the  yellow  dye  it  yields.  — Sp.  fas  toe,  fr.  Arab,  fustuq,  fr.  Pers.  pistah.  See
pistachio.
fustigate,  tr.  v.,  to  cudgel.  —  L.  fustigatus,  pp. of  fustigare,  ‘to  cudgel’,  which  is  formed  on analogy  of  castigare,  ‘to  chastise’,  fr.  fastis, ‘staff,  cudgel’,  and  agere,  ‘to  set  in  motion, drive,  lead;  to  do,  act’.  See  fust  and  agent  and cp.  castigate  and  the  compound  words  there referred  to.
Derivatives:  fustigat-ion,  n.,  fastigat-or,  n., fustigat-ory,  adj.
Fusus,  n.,  a  genus  of  marine  snails  (zool.)  —  L.
futchel
--- page marker after pistachio (28932) ---
```


### [2026-09-05T14:37:09.728Z] TOOL RESULT

```
=== AFA context ===
X*inV = aatureja Low 325. Einschub eines ^Ain ist
auch sonst zu constatieren ; z. B. überliefert Jäküt L 621, 7
als Volksaussprache fübc sT) (mit yolksetymologischer An-
lehnung) fi .V und ebenso lO^vJu für ^^L Jaküt l. 672, 2.
Die Wurzel JJuo scheint nämlich echt arabisch Ja^üt ü.
204, 5. [^nns Rga. der Gaönim Berlin 42, 6 p^lp 'yos^
iny V]. — oLoA^ > Weide" ist entlehnt aus HfivaS Low 301.
Daselbst ist für die Synonymik Sabb. 36* 8 nachzutragen.
{jiSmßji ist entlehnt aus pD*lS Low 148.
^^ »Portulak'* (woneben nach Gauh. auch ^^jJ^ vor-
kommen soll; dies ist aber wohl Fehler für ^^yx^pJ^) i>t
entlehnt aus Ki^nSnö Low 320 (^ = ^).
^j?v f »Pistazie" ist als Fremdwort schon Ton den Ara-
bern (Mu'arrab 108) erkannt; es kann direct aus dem Per-
sischen, wie Gawali^ meint , oder auch mittelbar durch
das Aramäische ppHDS L^Asu Low 80 in's Arabische
gedrungen sein. — J^ ist entlehnt aus T^fi Low 312. —
^j-S3ui =3 T^yetvov kennen schon die Araber (Mu^arr. 111)
als fremd.
eis »Kürbis" halten schon die Araber (Mu^arrab 122) für
ein unechtes Wort Ich stimme ihnen ToUkommen beif
und erklare es für entlehnt aus lli^ K*1p L5w 351. So
wie nach Nöldekes Bemerkung ebenda die Westsyrer t^-o
für )^^ sprachen, so wurde im Arabischen durch Asnmi-144
ImtiOD des I an das vorhergehende emphatische i^ c o aus
Jjtj~j > Gewürznelke" ist gelegentlich duect durch
Umbildung von iiifus^u\xa* erklärt worden. Das arabi-
sche Wort ist aber gewiss ein Jirecter Spross eines noch
aufzufindenden indischen Originales,, aus welchem auch
iixp-j6^i/>.>.iv mit rolksetjmologischer Anlehnung entstanden
sein wird. Das J^^ ist seit alter Zeit ia Arabien ver-
=== AFM فستق ===
201:ارجن وهو الفستق البري وقيل الاوز المر واسمة 6 9 اي لوز الل
572:الفستق
596:سمس كالدودة الكثيرة الأرجل في داخلها شى #«كالفستق زعفوضة وعللاوة اتامة 3
3051:ܦܣܬܩܐ رااتري والكردي فستق ٠‏ والارمني بإسسسمن وهر ايضاً ܦܝܢܣܬܩܐ
3150:ܐܠܐ ܨܒ يصنّع من الاوز ܢ والفستق ٠‏ ܘ الاراعي ° ܩܘܦܛܐ 000ا
3546:شجر الفستق يشتعل بالنار مثل الكبريت ولهذا قيل له سيّد الكباريت ٠‏ وقيل يأبع
5796:فستق ܀ ‏ |
=== TAD فستق ===
1991:   ‫فستق ‪ -‬ارامي « فستقا » لانمنشأهذه الشجرة الشام أى سوريا فنقل الى ا‬
2026:           ‫(‪ )1‬اهالى دمشقى اشام يمونيا فستقية لكوتما على شك الفدقة ‪ .‬وقال التباب المجازى‬
2655:    ‫مصطكي ‪ -‬ونانى ‪8‬وعناموه هو عصارة شجرة نشبه الفستق واليطم تمد‬
```


## [2026-09-05T14:37:24.253Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- pistachio page markers ---\"; awk 'NR>=28900 && NR<=28960' KLN_1966.txt | grep -nE \"^[0-9]{3,4}$\"\necho \"--- AFM entry near 5796 ---\"; sed -n '5780,5805p' AFM_pages.txt\necho \"--- AFM pdf page tag near 5796 ---\"; awk 'NR<=5796 && /\\[pdf page/ {p=$0; n=NR} END{print n\": \"p}' AFM_pages.txt"
}
```


## [2026-09-05T14:37:25.328Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\ngrep -n -i \"pista\\|fustuq\\|fistiq\\|pesta\" PLA_pages.txt | head -30\necho \"=== page tag search ===\"; grep -n \"\\[pdf page\" PLA_pages.txt | sed -n '200,215p'"
}
```


### [2026-09-05T14:37:26.197Z] TOOL RESULT

```
--- pistachio page markers ---
23:1190
--- AFM entry near 5796 ---
زلال ܣ
0000
زور ^
٠١6 شوربا‎
شيرازه وه
+ ص ع
٠١5 صابون‎
صتدل ١5+‏
جد ط +
طاس ܙ ܙ |
١١٠7 طبك‎
ܩܒ ܧܥ ”997
١١" طسث‎
طولك .ܙ | ܙ
+ ف ا
فاق * ܙ ܙ
فستق ܀ ‏ |
فلفل ١١‏
فيل ܙ« ܙ
+ ى +
فز هوه
ترعز ١6‏
قفس +¥« ܙ
قلات *« ܙ
ܒܚܢ ¥« |
ܪܐ به"(
--- AFM pdf page tag near 5796 ---
:
```


### [2026-09-05T14:37:26.255Z] TOOL RESULT

```
454:           pers. h/e                ar.    a z. B.:          pers.         piStahte           > ar.       biStahta
3089:=       -    bista$:               aus       dem       pers.    al. peste              "Pistazien"           T       MP    eos pistag          5
3098:Gi           bastag:               "Pistazien'"                aus    dem    pers. Au             peste       Ss.    bistagß       8,
3192:ass) -                baStahta:            "Schreibtisch"                aus     dem       pers.      sy        piStabte        Ic    mp.
6394:       Pistazien            und      Rosenwasser"            pers,          7    aus     dem    pers.        5 busk         "trocken,
11800:Se        -       fustug:              "Pistazie"                   pers. «, peste               2 mp.           Ir»o   3,   u.   bistag
11802:          Pistazie                    pers.             >     griech.        >      lat.       6, frz.        pistache »-
11805:a3»           - fustuga:                    nom,        un.   v.    is        fustug          "eine    Pistazie".
11808:OR            - fustugi:                     "pistaziengrün".
=== page tag search ===
```


## [2026-09-05T14:37:32.628Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\nhead -5 PLA_pages.txt; echo \"---\"; grep -c $'\\f' PLA_pages.txt; echo \"--- context 11790-11815 ---\"; sed -n '11790,11815p' PLA_pages.txt\necho \"=== which leaf ===\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"fustug:\")>0) print \"leaf(1-based)\",n}' PLA_pages.txt"
}
```


### [2026-09-05T14:37:34.286Z] TOOL RESULT

```
             Asya Asbaghi


Persische Lehnwörter im Arabischen

---
301
--- context 11790-11815 ---

bs                _         asätin:          Pl.        v.olus      fustän         q.    v.


als           -       fustän:           "Überkleid,                Jacke,      Joppe"          pers.     ı


obs - fustän = fustän                                     a. v.

                                                                                                                                            4
Se        -       fustug:              "Pistazie"                   pers. «, peste               2 mp.           Ir»o   3,   u.   bistag
          aram.              Sans.
          Pistazie                    pers.             >     griech.        >      lat.       6, frz.        pistache »-


a3»           - fustuga:                    nom,        un.   v.    is        fustug          "eine    Pistazie".


OR            - fustugi:                     "pistaziengrün".


ansıms - fisfisa:                            "Luzerne"         pers.         ?. 7, dtsch.              Alfalfa.

o5lhs - faßsäga:                             "Rakete",


=== which leaf ===
leaf(1-based) 225
```


## [2026-09-05T14:37:39.028Z] TOOL CALL #15: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['PLA'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-05T14:37:41.321Z] TOOL RESULT

```
{
 "title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988",
 "edition_found": null,
 "kind": "archive_djvu",
 "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)",
 "identifier": null,
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"
 ],
 "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).",
 "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "notes": "Open full text obtained. Alphabetical Arabic headwords with Persian/MP etyma; OCR fair (German + transliteration), Arabic script mostly garbled. Provenance: a user upload of an in-copyright 1988 Harrassowitz book — grey copy; publisher sells it (harrassowitz-verlag.de).",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
   "first_printed": 1,
   "last_printed": 300,
   "pdf_offset": 0,
   "lang": "deu+ara"
  }
 ],
 "cites": "page number of Asbaghi, Persische Lehnwörter im Arabischen (1988), alphabetical by Arabic word"
}
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


## [2026-09-05T14:37:41.526Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN pistah/piste ===\"; grep -n -i \"pista\\|piste\\b\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"pistak\\|pista\" HUB.txt | head -20\necho \"=== PHD pistag ===\"; grep -n -i \"pistag\\|pystk\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n -i \"pistak\\|pistag\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-05T14:37:41.629Z] TOOL RESULT

```
=== HRN pistah/piste ===
2357:bei. gvan, gön Vilde Pistazie (?) (133).
3060:skr. pistaka-),
9102:ap. ni + [/^pais-, nipistanaiy 'schreiben* 2) — ai.
=== HUB ===
406:*) Vgl. auoh phi. stik ip sftk-pistan *with prominent breasts'
4817:von zd. ap. ni-, vgl. ap. nipistam geschrieben', nipiStanaiy- 138 -
6212:*schreiben', ap. nipistanaii/; kdbln *Mitgift* = kdvm JRAS.
6597:2) Wie aber verhalt sich np pistan 'Brust' zu zd. fstana-? Vgl.
6598:oben p. 41. Etwa pistan (aus ^pdatdna-?) zu. fstana' (aus *pstana-)
8410:das Verhaltniss von zd. fstdna- zu np. pistan 'Brust', siehe
8440:= ap. nipistanaiy, pr. nuvesam, Wrzl. pdk^ ; histan 'lassen*,
8445:= zd. xsvasti- ; pist 'Mehl' = skr. pista- ; mahist (ZDM6.
=== PHD pistag ===
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:3131:pistachio nut pistag; ~ tree wan i gurgānīg.
PHD.txt:4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
PHD_mackenzie.txt:4246:pistag [pstk l I N pista] pistachio nut.
PHD_mackenzie.txt:7289:pistachio nut pistag; -- tree wan          poplar sped-dar.
PHD_mackenzie.txt:8617:pattay-                 - ~ \"CU        pistag                  \~t'bJQJ
=== NYB ===
2752:nipistan [npštn'; YKTYBWN-tn'] nipés- to write 419. 110? etc. ; nipist estet it has been written, it is written 1139; nipist ēstāt it was written 1!—?; — pres. pass. nipēsihēt [YKTYBWN-yhyt'] is being written 18%; — pat dp i zarr nipištak 1079; apar nipistak written down 108?!; nāmak ~ 6 to write a letter to 49-9. 822, an inscription P 2:3.4; apar fravartak čton nipišt estat kū it was written in the letter (then dir. speech) 1872; apar én ayyätkär nipišt estet 1135-9. — OP ni-pais- ; MPrthPrs nbyštn nbys-; Paz. nawaštan nivés-; NP nuvistan, nivištan, nivés-.
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
```


## [2026-09-05T14:37:54.218Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"size:\"; wc -l UNV.txt; grep -c $'\\f' UNV.txt\necho \"=== grep ===\"; grep -n -i \"istak\\|pistazie\\|nuts\\|Nuss\" UNV.txt | head -30"
}
```


### [2026-09-05T14:37:55.986Z] TOOL RESULT

```
size:
1213 UNV.txt
45
=== grep ===
609:53.  Die  Dattel  von  Hirat, die  mit  Walnüssen  gefüllt ist,  die  frische  Pistaziennuß, und  der  armenische  Pfirsich'^, die  Eichel,  die  Kastanie  mit Zucker  und  Kandis.
612:51.  ^  Ich  nehme  3^  lüer  und  in  §  52  gleich  np.  'Pistaziennnß’.  —
```


## [2026-09-05T14:37:56.150Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part1 پسته ===\"; grep -n \"پسته\" MON_part1.txt | head -10\necho \"=== MON فستق ===\"; grep -n \"فستق\" MON_part2.txt MON_part1.txt | head -10\necho \"=== BQT پسته ===\"; grep -n \"پسته\" BQT_v1_pages.txt BQT_v2_pages.txt | head -10"
}
```


### [2026-09-05T14:37:56.254Z] TOOL RESULT

```
=== MON part1 پسته ===
1175:شکرء کف چوبکک و مغز پسته. نوعی از 
10075:ار غ: ب»ه (ص.) بادام و پسته و فندق و گردو 
23127:بی‌مغز. پسته پوکك» بزغند. از بزغنج به علت 
25793:سماقی‌ها که شبیه پسته معمولی است و 
25802:منظور تکثیر پسته می‌زنند. از پوست ایین 
25998:و فندق و پسته و بادام و درت در تاله‌های 
31667:هرگاه مقدار پسته‌ای از آن بخورند تا چند 
31751:پسته: (م)هامه۳ [آراء فستقا] (.) (گٌیا.) 
31758:فراوانی کشت می‌گردد. مغز پسته: (گیا.) مغز 
31759:میوة درخت پسته که خوراکی است و نوعی 
=== MON فستق ===
MON_part1.txt:31751:پسته: (م)هامه۳ [آراء فستقا] (.) (گٌیا.) 
MON_part1.txt:51113:هر یک به منزلهةً غوزه است)) بندق فستق. 
MON_part2.txt:3740:آنچه خورده نمی‌شود؛ ناخوردنی فستق»: 
=== BQT پسته ===
BQT_v1_pages.txt:7543:است که از فند ومغز بادام و پسته و تخود مقس
BQT_v1_pages.txt:14810:زنند خصوساً - و بادام و پسته وکردکان وامثال
BQT_v1_pages.txt:17268:غالیه گویند و آن مانند پسته میباشد لیکن زود
BQT_v1_pages.txt:19461:۵ 4 - بنم‌اول , م رکب از : بز + غاله (کاله) شانة صضیر«اسفا!:۲سص۹۹» ؛ بچةٌ بز .کنفه . کوبند که‌درخت‌پسته مکال میوه‌فزدار
BQT_v1_pages.txt:19696:درخت پسته است » و بعضی گویند کندر است >
BQT_v1_pages.txt:19725:پسته و چم - بفتح را وکر حا هر دو
BQT_v1_pages.txt:27904:پسته ‏ وبلا فاسله هم‌آمده است - و کسی رالیز
```


## [2026-09-05T14:38:04.425Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== UNV 600-625 ===\"; sed -n '600,625p' UNV.txt\necho; echo \"=== MON part1 31745-31765 ===\"; sed -n '31745,31765p' MON_part1.txt"
}
```


### [2026-09-05T14:38:04.486Z] TOOL RESULT

```
=== UNV 600-625 ===
.  taivarzatah
■»  ^5yü-*oo  jM)  or
i  sälidänah  ap)äh  liamvär  he  58.
49.  Es  sagt  der  Knabe: ‘Möget  Ihr  unsterblich  sein! Diese  Sclialenfriiclite  sind  alle fein  und  gut:
50.  Die  Kokosnub,  wenn man  sie  mit  Zucker  ißt;  im
Indischen  nennt  man  sie  Ko-
*
kosnuß,  und  im  Persischen nennt  man  sie  indische  Wal¬ nuß.
51.  Die  hyrkanische  Pi¬ staziennuß  ,  wenn  man  sie auf  einem  Bräter  röstet,  und frische  Linsen,  wenn  man  sie mit  dem  Saft  der  Oliven  ißt.
53.  Die  Dattel  von  Hirat, die  mit  Walnüssen  gefüllt ist,  die  frische  Pistaziennuß, und  der  armenische  Pfirsich'^, die  Eichel,  die  Kastanie  mit Zucker  und  Kandis.
58.  Aber  niemals  kann  sich mit  Hanfkörnern  von  Kesäli-
49.  '  Mk.3v^-
51.  ^  Ich  nehme  3^  lüer  und  in  §  52  gleich  np.  'Pistaziennnß’.  —
^  s.  §26.  No.  a.  —  ^  Hss.  —  *  Hss.  ^  p]rgänzt  nach  der  Parallele  in  §21.
—  ^  Hss.  3^3^;  s-  §21,  No.  5.
^  Hier  ist  wohl  das  Rost  iin  allgemeinen  zn  verstehen;  s.  §  26,  No.  b.
52.  ^  zn  np.  s.  §  96.  No.  3.  —  s.  §  51.  No.  1.  —  ^  np.  afy.
'the  oaktree,  an  acorn.  a  chesnut‘  (Raverty).  —  *  np.  'glans  regia’.  —
^  Ergänzt  nach  §  50.
^  ^Yörtlich:  'die  Pfirsichpflaimie’;  s.  np.  'PÜanme’  nnd  §40,  No.  1.
53.  ^  np.  nnd  GrBd.  118.  2.
27
^iiexe)  [-’]  )ie)  ^sD^eJHXJüi
hrist  päcan  [i]  pih  pa  he  n^mlipürlh
pa  x^as  ce  nest  patkär  därenah  eci  estet
ucj  ncj  Jv})^

=== MON part1 31745-31765 ===
فرو تشاند ی ۵ 

پستو. تاد (امر.) اطاقکی که در شت 
اطاق نشیمن و غیره تهیه کنند و اشیا و لوازم 
خانه را در آن نهند. 

پسته: (م)هامه۳ [آراء فستقا] (.) (گٌیا.) 
درختی از تبره سماقی‌ها که دست مخصو ص 
را تشکیل می‌دهد. این درخت دو بایه است 
و به حالت خودرو در سوریه و افغانستان 
می‌روید (در ايران نیز در قسمت‌های شمال 
خراسان بصورت وحشی دیده می‌شود) و در 
کرمان» آذربایجان» قزوین و دامغان به 
فراوانی کشت می‌گردد. مغز پسته: (گیا.) مغز 
میوة درخت پسته که خوراکی است و نوعی 
از آجیل می‌باشد و مطبوع است. ( کذد.) دهان 
معشوق. پستة زمینی: (گیا.) گیاهی از تيرة 
پروانه‌واران جز و دستة اسپرس‌ها که علفی و 
باه اس ور باه سب ار ماع ۰ نا 
۰ سانته یمتر می‌رسد . گل آن زرد و دارای 
پستی: آ-۲۸51 (حامص. .) فرودی» پایینی.
```


## [2026-09-05T14:38:26.564Z] TOOL CALL #20: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-05T14:38:26.622Z] TOOL RESULT

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


## [2026-09-05T14:38:28.238Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD fustic ===\"; grep -n -i \"fustic\" FSD_vol2.txt | head -5\necho \"=== WEB fustic ===\"; grep -n -i \"fustic\" WEB_vol1.txt | head -5\necho \"=== SKT fustic/fustet ===\"; grep -n -i \"fustet\\|fustoc\" SKT.txt LKT.txt | head -10\necho \"=== DEV fustet ===\"; grep -n -i \"fustet\\|fustoc\" DEV.txt PHN.txt LAM.txt | head -10"
}
```


### [2026-09-05T14:38:28.371Z] TOOL RESULT

```
=== FSD fustic ===
20832:H-.sct'ic,  1   fi-.set'ik:  S   fl-siit'lc,  a.  a/iem.  ot,  perliiinlni;  to,  or derived  from  ftwtlc.  ( <   (l,  flnetho'.z,  Itlnd  of  fustic,  <   finct  •.» rii.sTKT.l  --  li.scllc  acid, a   yellow, crystalline,  volatile  eolor- lng»nuitter  (Cfnlinitij)  extracted  from  young  fustUs  (A'/cim cntUin.-i),.—  lls'e-llw,  n.  A   form  of  iloetie  atdd  (CJioIl  uiOf).
28387:HiaO  23)  in  young  fustic:  used  to  produce  yellow  colors.  4..  Qr
28437:fus'tet,  1   fiis'tet;  8   ffls'tet,  n.  1.  The  Venetian  suinae  or smoke-tree  {Cotinus  cotinm) ;   also,  Its  wood.  8.  Young  fus- tic. See  FUSTIC.  [F.,  klndoftree,<  L,/Msffs,  cudgel.] fiis'tian,  1   fus'cSlien;  2   ftis'ohan,  a.  1.  Made  of  fustian, Ha  wore  a   broad-skirted  fustian  coat,  porploxed  with  half  a hundred  pookots.  Invitia  Metch-Baoh  p.  i05.  (a.  p.  r.  1801.] 8.  Making  use  of  or  characterized  by  fustian;  pompous; bombastic.  3.  Of  no  value;  good-for-nothing, fus'tiaii,  n.  1.  Formerly,  a   kind  of  stout  cloth  made  of cotton  and  flax;  now,  a   coarse  twilled  linen  or  cotton fabric,  such  as  corduroy  or  velveteen.
28447:yellowwood;  old  fustic.  [ <   F. /usfoc,  <   Sp. /jistoc,  <   -   ,   -   -
28449:—   American  fustic, the  yelUiwwood  of  tbe  southern  United  fu'ture,  it.  1.  The  time  yet  to  come;  time  later  than
=== WEB fustic ===
73683:fis’e-tin, 2. a yellow crystalline dyestuff ob- tained from the wood of Rhus cotinus or young fustic.
79177:fustic
79193:a . fustigated, pl., pp.; fustigat- fus/tigatey H aha pp. ol fa stigare, to beat ing, PPr; 2 fustis, a stick.] to beat with with a stick OF © ub. (L. sap aki) from fusticore, mt N a cudgel, from ustis, a stick or to beat iat ab by beating with a stick or freemen in ancient Rome. fus-ti la/ridin, n. a scamp; @ scoundrel, [Obs.] us: ti-l fust/ilug, As A a perenne dyestuff from young fustic. fue ess, n. a fusty state or quality. ius ty. a.; comp. fustier; superl, fustiest, 1. fusci: musty; ill-smelling; rank; rancid. ma not up-to-date; old-fashioned. 3. melancholy; listless. [Obs.] fū'şüre (-zhūr), n. [L. fusura, from fundere, to a our, melt.] a smelting. eee : fell, n. [origin unknown] in a carriage, a fe ee ei canner the shaits or pole. fa/thiark n. [from its first six letters: f. u, th, z (-a) r. c (-k).] the runic alphabet: formerly also futharc, futhorc, futhork. {i 4 fa'tile a. (Fr, futile, from L. futilis, that easily 5 from the root of fundere, to pour.]
=== SKT fustic/fustet ===
=== DEV fustet ===
```


## [2026-09-05T14:39:52.759Z] TOOL CALL #22: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/pistachio\" \\\n \"https://www.etymonline.com/word/fustic\" \\\n \"https://www.etymonline.com/word/albacore\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CE%B9%CF%83%CF%84%CE%AC%CE%BA%CE%B9%CE%BF%CE%BD\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B3%D8%AA%D9%82\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA%D9%87\" \\\n \"https://en.wiktionary.org/wiki/albacore\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%83%D8%B1\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 99: pistachio/fustic/albacore chains\" ; done"
}
```


## [2026-09-05T14:39:54.955Z] TOOL CALL #23: Bash

```json
{
 "command": "pdftoppm -f 99 -l 99 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg99 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T14:39:59.752Z] TOOL RESULT

```
### https://www.etymonline.com/word/pistachio
/home/sfmqrb/git/rishe/data/verification/sources/web/ab56664dc22f73f0.txt
### https://www.etymonline.com/word/fustic
/home/sfmqrb/git/rishe/data/verification/sources/web/a83c2b2487fffe46.txt
### https://www.etymonline.com/word/albacore
/home/sfmqrb/git/rishe/data/verification/sources/web/ccf9a34cba5eaf11.txt
### https://en.wiktionary.org/wiki/%CF%80%CE%B9%CF%83%CF%84%CE%AC%CE%BA%CE%B9%CE%BF%CE%BD
/home/sfmqrb/git/rishe/data/verification/sources/web/de41cb49e71ef061.txt
### https://en.wiktionary.org/wiki/%D9%81%D8%B3%D8%AA%D9%82
/home/sfmqrb/git/rishe/data/verification/sources/web/959338483ff43c84.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/0bd9f77683fa4b04.txt
### https://en.wiktionary.org/wiki/albacore
/home/sfmqrb/git/rishe/data/verification/sources/web/ffa4ae351c7c0905.txt
### https://en.wiktionary.org/wiki/%D8%A8%D9%83%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/b18499036c5ea9a4.txt
```


### [2026-09-05T14:40:01.842Z] TOOL RESULT

```
total 31496
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 10:40 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
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
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


## [2026-09-05T14:40:05.033Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in ab56664dc22f73f0 a83c2b2487fffe46 ccf9a34cba5eaf11; do echo \"=== $f ===\"; sed -n '1,80p' $f.txt | grep -v \"^\\s*$\" | head -50; echo; done"
}
```


### [2026-09-05T14:40:06.562Z] TOOL RESULT

```
=== ab56664dc22f73f0 ===
URL: https://www.etymonline.com/word/pistachio
FETCHED: 2026-09-05T14:39:55Z
STATUS: 200
TITLE: Pistachio - Etymology, Origin & Meaning
Pistachio - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of pistachio 
 pistachio (n.) 
 1590s, "nut of the pistachio tree," from Italian pistacchio , from Latin pistacium "pistachio nut," from Greek pistakion "pistachio nut," from pistakē "pistachio tree," from Persian pistah "pistachio." Borrowed earlier in English as pystace , pistace (mid-15c.), from Old French pistace (13c.) and Medieval Latin pistacia , ultimately from the same source.
 also from 1590s 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 tree 
 Old English treo, treow "tree" (also "timber, wood, beam, log, stake"), from Proto-Germanic *trewam (source also of Old Frisian tre, Old Saxon trio, Old Norse tre, Gothic triu "tree"), from PIE *drew-o-, suffixed variant form of root *deru- "be firm, solid, steadfast," with speci
 vaccination 
 1800, used by British physician Edward Jenner (1749-1823) for the technique he publicized of preventing smallpox by injecting people with the similar but much milder cowpox virus (variolae vaccinae), from vaccine (adj.) "pertaining to cows, from cows" (1798), from Latin vaccinus 
 ABBA 
 Swedish pop music group formed 1972, the name dates from 1973 and is an acronym from the first names of the four band members: Anni-Frid Lyngstad, Björn Ulvaeus, Benny Andersson, Agnetha Fältskog....Biblical title of honor, literally "father," used as an invocation of God, from L
 perfunctory 
 "done mechanically or without interest or zeal and merely for the sake of being rid of the duty of doing it; done so as to conform to the letter but not the spirit," 1580s, from Late Latin perfunctorius "careless, negligent," literally "like one who wishes to get through a thing,
 grief 
 early 13c., "hardship, suffering, pain, bodily affliction," from Old French grief "wrong, grievance, injustice, misfortune, calamity" (13c.), from grever "afflict, burden, oppress," from Latin gravare "make heavy; cause grief," from gravis "weighty" (from PIE root *gwere- (1) "he
 virtue 
 c. 1200, vertu, "moral life and conduct; a particular moral excellence," from Anglo-French and Old French vertu "force, strength, vigor; moral strength; qualities, abilities" (10c. in Old French), from Latin virtutem (nominative virtus) "moral strength, high character, goodness; 
 holiday 
 1500s, earlier haliday (c. 1200), from Old English haligdæg "holy day, consecrated day, religious anniversary; Sabbath," from halig "holy" (see holy) + dæg "day" (see day); in 14c. meaning both "religious festival" and "day of exemption from labor and recreation," but pronunciati
 fudge 
 "put together clumsily or dishonestly," by 1771 (perhaps from 17c.); perhaps an alteration of fadge "make suit, fit" (1570s), a verb of unknown origin. The verb fudge later had an especial association with sailors and log books. The traditional story of the origin of the interjec
 toilet 
 1530s, earliest in English in an obsolete sense "cover or bag for clothes," from French toilette "a cloth; a bag for clothes," diminutive of toile "cloth, net" (see toil (n.2)). Toilet acquired an association with upper class dressing by 18c., through the specific sense "a fine c
 dragon 
 mid-13c., dragoun, a fabulous animal common to the conceptions of many races and peoples, from Old French dragon and directly from Latin draconem (nominative draco) "huge serpent, dragon," from Greek drakon (genitive drakontos) "serpent, giant seafish," apparently from drak-, str
 Share pistachio 
 ‘ cite ’ 
 Page URL :
 https://www.etymonline.com/word/pistachio Copy 
 HTML Link :
 <a href="https://www.etymonline.com/word/pistachio">Etymology of pistachio by etymonline</a> Copy 

=== a83c2b2487fffe46 ===
URL: https://www.etymonline.com/word/fustic
FETCHED: 2026-09-05T14:39:56Z
STATUS: 200
TITLE: Etymonline - Online Etymology Dictionary
Etymonline - Online Etymology Dictionary 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.
 About
 Who Did This 
 Sources 
 Introduction 
 Links 
 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 
 Apps
Get Chrome Extension 
Get iOS App 
Get Android App 
 Dark
 Auto
 Light
 Terms of Services Privacy Policy 
 English (English) 
 © 2001–2026 Douglas Harper & Talia Felix

=== ccf9a34cba5eaf11 ===
URL: https://www.etymonline.com/word/albacore
FETCHED: 2026-09-05T14:39:56Z
STATUS: 200
TITLE: Albacore - Etymology, Origin & Meaning
Albacore - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of albacore 
 albacore (n.) 
 name given to a large type of tuna caught in the Tropics, 1570s, from Portuguese albacora , from Arabic al bakara "milk cow;" the fish so called for its size.
 also from 1570s 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 tunny 
 large sea-fish of the mackerel order, 1520s, probably from French thon (14c.), from Old Provençal ton and directly from Latin thunnus "a tuna, tunny," from Greek thynnos "a tuna, tunny," possibly with a literal sense of "darter," from thynein "dart along."  In ancient Greece
 aunt 
 "sister of one's father or mother," c. 1300, from Anglo-French aunte, Old French ante (Modern French tante, from a 13c. variant), from Latin amita "paternal aunt" diminutive of *amma a baby-talk word for "mother" (source also of Greek amma "mother," Old Norse amma "grandmother," 
 providence 
 late 14c., "foresight, prudent anticipation, timely care or preparation," from Old French providence "divine providence, foresight" (12c.) and directly from Latin providentia "foresight, precaution, foreknowledge," abstract noun from present-participle stem of providere "look ahe
 facility 
 early 15c., "gentleness, lightness," from Old French facilité "easiness, ease," from Latin facilitatem (nominative facilitas) "easiness, ease, fluency, willingness," from facilis "easy to do," from facere "to do" (from PIE root *dhe- "to set, put"). First in a medical book: If i
 month 
 "one-twelfth part of a year; one of the twelve parts into which the calendar year is arbitrarily divided," Old English monað, from Proto-Germanic *menoth- (source also of Old Saxon manoth, Old Frisian monath, Middle Dutch manet, Dutch maand, Old High German manod, German Monat, O
 militia 
 1580s, "system of military discipline," from Latin militia "military service, warfare," from miles "soldier" (see military (adj.)). The sense of "citizen army" (as distinct from professional soldiers) is first recorded 1690s, perhaps from a sense in French cognate milice. Histori
 decimate 
 c. 1600, "to select by lot and put to death every tenth man," from Latin decimatus, past participle of decimare "the removal or destruction of one-tenth," from decem "ten" (from PIE root *dekm- "ten"). The killing of one in ten, chosen by lots, from a rebellious city or a mutinou
 article 
 c. 1200, "separate parts of anything written" (such as the statements in the Apostles' Creed, the clauses of a statute or contract), from Old French article (13c.), from Latin articulus "a part, a member," also "a knuckle; the article in grammar," diminutive of artus "a joint" (f
 amethyst 
 violet-colored quartz, late 13c., amatist, from Old French ametiste (12c., Modern French améthyste) and directly from Medieval Latin amatistus, from Latin amethystus, from Greek amethystos "amethyst," noun use of an adjective meaning "not intoxicating; not drunken," from a- "not"
 crusade 
 "military expedition under the banner of the cross," 1706, a respelling or replacement of croisade (1570s), from French croisade (16c.), Spanish cruzada, both from Medieval Latin cruciata, past participle of cruciare "to mark with a cross," from Latin crux (genitive crucis) "cros
 Share albacore 
 ‘ cite ’ 
 Page URL :
 https://www.etymonline.com/word/albacore Copy 
 HTML Link :
 <a href="https://www.etymonline.com/word/albacore">Etymology of albacore by etymonline</a> Copy
```


## [2026-09-05T14:40:12.755Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== GREEK pistakion ===\"; grep -n -A6 -B2 \"Etymology\" de41cb49e71ef061.txt | head -60"
}
```


### [2026-09-05T14:40:12.802Z] TOOL RESULT

```
=== GREEK pistakion ===
63-
64- 1.2 
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
153- βιστάκιον ( bistákion ) , φιττάκια ( phittákia ) , ψιττάκια ( psittákia ) 
154-
155: Etymology
156- [ edit ] 
157-
158- From πιστάκη ( pistákē , “ pistachio tree ” ) +‎ -ιον ( -ion , diminutive suffix ) .
159-
160- Pronunciation
161- [ edit ]
```


## [2026-09-05T14:40:13.983Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== ARABIC فستق ===\"; sed -n '1,120p' 959338483ff43c84.txt | grep -v \"^\\s*$\" | head -60"
}
```


### [2026-09-05T14:40:15.965Z] TOOL RESULT

```
=== ARABIC فستق ===
URL: https://en.wiktionary.org/wiki/%D9%81%D8%B3%D8%AA%D9%82
FETCHED: 2026-09-05T14:39:57Z
STATUS: 200
TITLE: فستق - Wiktionary, the free dictionary
فستق - Wiktionary, the free dictionary 
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
 Arabic 
 Toggle Arabic subsection 
 1.1 
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Declension 
 1.3.2 
 Synonyms 
 1.3.3 
 Derived terms 
 1.3.4 
 Descendants 
 1.4 
 References 
 2 
 Central Kurdish 
 Toggle Central Kurdish subsection 
 2.1 
 Etymology 
 2.2 
 Pronunciation
```


## [2026-09-05T14:40:19.748Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk '/^ Etymology$/{f=1} f' 959338483ff43c84.txt | grep -v \"^\\s*$\" | head -40\necho \"=====PESTE=====\"\nawk '/^ Etymology/{f=1} f' 0bd9f77683fa4b04.txt | grep -v \"^\\s*$\" | head -40"
}
```


### [2026-09-05T14:40:21.295Z] TOOL RESULT

```
 Etymology
 [ edit ] 
 From Middle Persian pstk' ( pistag ) , if not via Aramaic ( Jewish Babylonian Aramaic פיסתקא ( pistəqā ) , פסתקא ( pistəqā ) , Classical Syriac ܦܘܣܬܩܐ ( pustəqā ) , ܦܷܣܬܩܐ ( pestəqā ) ).
 Pronunciation
 [ edit ] 
 IPA ( key ) : /fus.tuq/ , /fus.taq/ 
 Noun
 [ edit ] 
 فُسْتُق or فُسْتَق • ( fustuq or fustaq )  m 
 pistachio ( Pistacia vera tree and fruit)
 Declension
 [ edit ] 
 Declension of noun فُسْتُق ( fustuq )‎; فُسْتَق ( fustaq )
 singular
 basic singular triptote 
 indefinite
 definite
 construct
 informal
 فُسْتُق ‎; فُسْتَق 
 fustuq ‎; fustaq 
 الْفُسْتُق ‎; الْفُسْتَق 
 al-fustuq ‎; al-fustaq 
 فُسْتُق ‎; فُسْتَق 
 fustuq ‎; fustaq 
 nominative
 فُسْتُقٌ ‎; فُسْتَقٌ 
 fustuqun ‎; fustaqun 
 الْفُسْتُقُ ‎; الْفُسْتَقُ 
 al-fustuqu ‎; al-fustaqu 
 فُسْتُقُ ‎; فُسْتَقُ 
 fustuqu ‎; fustaqu 
 accusative
 فُسْتُقًا ‎; فُسْتَقًا 
 fustuqan ‎; fustaqan 
 الْفُسْتُقَ ‎; الْفُسْتَقَ 
 al-fustuqa ‎; al-fustaqa 
 فُسْتُقَ ‎; فُسْتَقَ 
 fustuqa ‎; fustaqa 
 genitive
=====PESTE=====
 Etymology 
 2.2 
 Pronunciation 
 2.3 
 Noun 
 2.4 
 References 
 3 
 Persian 
 Toggle Persian subsection 
 3.1 
 Etymology 
 3.2 
 Pronunciation 
 3.3 
 Noun 
 3.3.1 
 Derived terms 
 3.3.2 
 Descendants 
 3.4 
 Further reading 
 Toggle the table of contents 
 پسته 
 9 languages 
 فارسی 
 Français 
 Magyar 
 Kurdî 
 Malagasy 
 پښتو 
 Русский 
 Sängö 
 中文 
 Entry 
 Discussion 
 English 
 Read 
 Edit 
 View history
```


## [2026-09-05T14:40:27.143Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n \"Persian\" -A400 0bd9f77683fa4b04.txt | sed -n '1,400p' | grep -v \"^\\s*$\" | grep -n -i \"Middle Persian\\|Descendants\\|pistag\\|Etymology\\|Greek\\|Arabic\\|Ancient\" | head -40"
}
```


### [2026-09-05T14:40:28.912Z] TOOL RESULT

```
6:90- Etymology 
18:102- Descendants 
101:185- Arabic spelling of pistə ( “ pistachio ” ) 
163:247- Etymology
194:278- Etymology
197:281: From Middle Persian pstk' ( /⁠pistag⁠/ , “ pistachio nut ” ) , from Old Persian *pistaka , attested as Elamite [script needed] ( pi-iš-tuk-ka₄ /⁠pistaka⁠/ , “ pistachio nut ” ) . Related to Persian بسته ( busta  / boste , “ nut ” ) , cognate with Sanskrit बुस्त ( busta , “ husk or shell of fruit ” ) .
251:335- Descendants
254:338- See also descendants from Old and Middle Iranian at pstk' . 
289:373- Arabic script: پستو ( pisto ) 
308:392- Khalaj terms in Arabic script 
315:399: Persian terms inherited from Middle Persian 
316:400: Persian terms derived from Middle Persian
```


## [2026-09-05T14:40:34.896Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i \"bakara\\|first-born\\|Proto-Semitic\\|firstborn\\|early\" b18499036c5ea9a4.txt | head -30\necho \"=== albacore wikt ===\"; grep -n -i -A4 \"Etymology\" ffa4ae351c7c0905.txt | grep -v \"^\\s*$\" | sed -n '1,40p'"
}
```


### [2026-09-05T14:40:36.467Z] TOOL RESULT

```
220: Compare Hebrew בְּכוֹר ( bəḵōr , “ firstborn ” ) .
225: بَكَرَ • ( bakara ) I ( non-past يَبْكُرُ ( yabkuru ) , verbal noun بُكُور ( bukūr ) ) 
227: to be early [ with إِلَى ( ʔilā ) ‘at something’ ]
229: to come early [ with إِلَى ( ʔilā ) ‘to something’ ]
230: بَكَرَ إِلَيْهِ قَبْلَ أَنْ يُغادِرَ بَيْتَهُ. bakara ʔilayhi qabla ʔan yuḡādira baytahu. (please add an English translation of this usage example) 
232: to get up early 
305: bakara 
328: bakarat 
331: bakaratā 
676: to be early [ with إِلَى ( ʔilā ) ‘at something’ ]
678: to come early [ with إِلَى ( ʔilā ) ‘to something’ ]
680: to get up early 
682: to early or prematurely [ with فِي ( fī ) or بِ ( bi , + verbal noun ) ‘do something’ ]
1185: firstborn child
1395: Borrowed from Arabic بِكْر ( bikr , “ firstborn; virgin ” ) . Doublet of بكار ( bekâr , “ bachelor ” ) .
1409: firstborn , firstling , the first child born to in the birth order of a couple through childbirth 
1464: to be early 
1569: بكّير ( bakkīr , “ early ” ) 
=== albacore wikt ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
154: Etymology
155- [ edit ] 
156-
157- From Portuguese albacor , from Arabic اَلْبَكُورَة ( al-bakūra , “ the young camels ” ) . 
158-
```


## [2026-09-05T14:40:48.092Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%CF%80%CE%B9%CF%83%CF%84%CE%AC%CE%BA%CE%B7\" \\\n \"https://en.wiktionary.org/wiki/fustic\" \\\n \"https://en.wiktionary.org/wiki/albacora\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%AA%DA%A9%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/pstk%27\" \\\n \"https://en.wiktionary.org/wiki/pistacium\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 99: pistachio/fustic/albacore/ebtekar chains\"; done"
}
```


## [2026-09-05T14:40:49.721Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON بکر ===\"; grep -n \"^بکر\\|بکر:\" MON_part1.txt | head -10\necho \"=== MON ابتکار ===\"; grep -n \"ابتکار\" MON_part1.txt | head -10\necho \"=== TAD/AFM بکر ===\"; grep -n \"البكورة\\|بكورة\" AFM_pages.txt TAD_pages.txt | head"
}
```


### [2026-09-05T14:40:54.958Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%CF%80%CE%B9%CF%83%CF%84%CE%AC%CE%BA%CE%B7
/home/sfmqrb/git/rishe/data/verification/sources/web/a67d861432a9b205.txt
### https://en.wiktionary.org/wiki/fustic
/home/sfmqrb/git/rishe/data/verification/sources/web/9b5b70b7e5f226c6.txt
### https://en.wiktionary.org/wiki/albacora
/home/sfmqrb/git/rishe/data/verification/sources/web/d00da0de5c5b6fd5.txt
### https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%AA%DA%A9%D8%A7%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/c59111e732bb4698.txt
### https://en.wiktionary.org/wiki/pstk%27
/home/sfmqrb/git/rishe/data/verification/sources/web/7b0ef96441a90726.txt
### https://en.wiktionary.org/wiki/pistacium
/home/sfmqrb/git/rishe/data/verification/sources/web/baf8e97d36dfc407.txt
```


### [2026-09-05T14:40:55.040Z] TOOL RESULT

```
=== MON بکر ===
24527:بکر: ۱ [ع.] (ص.) دختر؛ دوشیره. تازه» 
24530:ج. بکران» ابکار. اندیشة بکر: فکر بکر. بکر 
24533:مشاطهً خزان. فکر بکر: اندیشه‌ای که پیش از 
24537:کسی نگفته باشد. موضو) بکر: موضوعی 
24543:بکران: «۰< (ع. ف.] (.) ج. بکسر. 
24544:بکران چرخ: ( کد.)"ستارکان آسمان..یگران 
24547:بکر تراشی: آ-0۵۲-۱۸۲۵3 (حامص.) ( کد.) 
25736:بکران» ته دیگ. 
28384:بکرتز اعا رک اسان کار بان » 
97247:بکر را در قضيةٌ فوق دو ارتباط است: یکی 
=== MON ابتکار ===
5975:نو آوردگی» اختراع: قوٌ ابتکار. 
41183:فرق گذارند: در تتصنیف جنبهةً ابتکار 
90310:تقلید يا ابتکار» به عبارت دیگر وسیله‌ای 
=== TAD/AFM بکر ===
```


## [2026-09-05T14:40:57.709Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON بکر entry ===\"; sed -n '24525,24548p' MON_part1.txt\necho \"=== MON ابتکار entry ===\"; sed -n '5968,5980p' MON_part1.txt"
}
```


### [2026-09-05T14:40:57.778Z] TOOL RESULT

```
=== MON بکر entry ===
چند که بهم وصل‌کرده‌اند و بر روی آن 
مخمل و زریفت و امثال آن کشیده‌اند. 
بکر: ۱ [ع.] (ص.) دختر؛ دوشیره. تازه» 
دست ناخورده» نو ایین. اندیشه و تصوری 
که یشتر در ذهن کسی خطور نکرده باشد؛ 
ج. بکران» ابکار. اندیشة بکر: فکر بکر. بکر 
پوشیده روی: شراب انگوری که هنوز در 
خم بود و کسی از آن نخورده باشد؛ بکر 
مشاطهً خزان. فکر بکر: اندیشه‌ای که پیش از 
این در ذهن کسی خطور نکرده باشد. کار 
کر کاز له که کش نیز تیان ۳3 نکر ده 
اون وی کش ارام 
کسی نگفته باشد. موضو) بکر: موضوعی 
که قلا مورد بحث قرار نکر فته باشد. 
یکرات: ۲۸ آف. ۰ ۰] (ق‌مر.) به 
دفعات» مکررآ؛ بارهاء چندین بار. بگرانق ۲ 
بمرات: بارها؛ مکررآ. 

بکران: «۰< (ع. ف.] (.) ج. بکسر. 
بکران چرخ: ( کد.)"ستارکان آسمان..یگران 
بهشت: ( کد.) حوریان بهشتی. 

بکر تراشی: آ-0۵۲-۱۸۲۵3 (حامص.) ( کد.) 
ایجاد کردن مضمون غریب و تازه. 
=== MON ابتکار entry ===
استفاء: "هدام [ع. ف. استغا] (مص م.) 
جستن» طلب کردن» خواستن. (مص‌ل.) 
مزاوارشدن. 

انتکار : :8 [ع.] (مص‌ل.) در بامداد 
رفتن» پگاه برخاستن. (مصم.) نو آوردن» 
امر بکر و بی‌سابقه پدید کردن. (اسص.) 
نو آوردگی» اختراع: قوٌ ابتکار. 

ابتلاء: 2" [ع. ف. انتلا] (مص‌ل.) دجار 
شدن» گرفتار شدن» در بلا افتادن. (مص‌م.) 
آزمودن» امتحان کردن» ارشاشن کتواون: 
(امص.) گرفتاری» مصیبت.
```


## [2026-09-05T14:40:59.535Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== pistake ===\"; awk '/^ Etymology/{f=1} f' a67d861432a9b205.txt | grep -v \"^\\s*$\" | head -20\necho; echo \"=== fustic ===\"; awk '/^ Etymology/{f=1} f' 9b5b70b7e5f226c6.txt | grep -v \"^\\s*$\" | head -25\necho; echo \"=== albacora ===\"; grep -n -i -A5 \"Etymology$\" d00da0de5c5b6fd5.txt | grep -v \"^\\s*$\" | head -40"
}
```


### [2026-09-05T14:41:01.149Z] TOOL RESULT

```
=== pistake ===
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Inflection 
 1.3.2 
 Derived terms 
 1.4 
 References 
 1.5 
 Further reading 
 Toggle the table of contents 
 πιστάκη 
 3 languages 
 Ελληνικά 
 Suomi 
 Malagasy 
 Entry 

=== fustic ===
 Etymology 
 1.3 
 Pronunciation 
 1.4 
 Noun 
 1.4.1 
 Synonyms 
 1.4.2 
 Derived terms 
 1.4.3 
 Translations 
 1.5 
 References 
 Toggle the table of contents 
 fustic 
 6 languages 
 Malagasy 
 Русский 
 தமிழ் 
 తెలుగు 
 Tiếng Việt 
 中文 
 Entry 
 Discussion 
 English 

=== albacora ===
220: Etymology
221- [ edit ] 
222-
223- From Andalusian Arabic , from classical Arabic اَلْبَكُورَة ( al-bakūra , “ the young camels ” ) .
224-
225- Pronunciation
--
256: Etymology
257- [ edit ] 
258-
259- Borrowed from Spanish albacora ( “ swordfish ” ) , from Arabic اَلْبَكُورَة ( al-bakūra , “ the young camels ” ) .
260-
261- Pronunciation
--
321: Etymology
322- [ edit ] 
323-
324- From Andalusian Arabic اَلْبَاكُورَة ( al-bācórah ) , from classical Arabic باكورة ( bākūrah , “ early fruits ” ) .
325-
326- Pronunciation
```


## [2026-09-05T14:41:10.634Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== pistake etym ===\"; grep -n -A6 \"^ Etymology$\" a67d861432a9b205.txt | grep -v \"^\\s*$\" | head -30\necho; echo \"=== fustic etym ===\"; grep -n -A8 \"^ Etymology$\" 9b5b70b7e5f226c6.txt | grep -v \"^\\s*$\" | head -30\necho; echo \"=== pistacium etym ===\"; grep -n -A6 \"^ Etymology$\" baf8e97d36dfc407.txt | grep -v \"^\\s*$\" | head -20\necho; echo \"=== MP pstk etym ===\"; grep -n -A8 \"^ Etymology$\" 7b0ef96441a90726.txt | grep -v \"^\\s*$\" | head -30"
}
```


### [2026-09-05T14:41:13.112Z] TOOL RESULT

```
=== pistake etym ===
147: Etymology
148- [ edit ] 
149-
150- Of Iranian origin. Compare Northern Kurdish pisteq , Persian پسته ( pesta, peste ) , Middle Persian pstk' ( pistag , “ pistachio nut ” ) , Old Armenian պիստակ ( pistak ) (from Iranian). [ 1 ] 
151-
152- Pronunciation
153- [ edit ] 

=== fustic etym ===
158: Etymology
159- [ edit ] 
160-
161- From Middle English fustik , from Middle French fustec , variant of fustet .
162-
163- Pronunciation
164- [ edit ] 
165-
166- ( US ) IPA ( key ) : /ˈfʌstɪk/ 

=== pistacium etym ===
150: Etymology
151- [ edit ] 
152-
153- Borrowed from Ancient Greek πιστάκῐον ( pistákĭon ) . See also πιστάκη ( pistákē ) .
154-
155- Pronunciation
156- [ edit ] 

=== MP pstk etym ===
140: Etymology
141- [ edit ] 
142-
143- From unattested Old Persian *pistaka , hence Elamite [script needed] ( pi-iš-tuk-ka₄ /⁠pistaka⁠/ , “ pistachio nut ” ) , probably from Proto-Iranian *pištakáh ( “ crushed ” ) , from Proto-Indo-Iranian *pištás + *-ikas , from Proto-Indo-European *pis-tó-s , from *peys- ( “ to grind, crush ” ) . [ 1 ] [ 2 ] The name perhaps refers to the ease of crushing pistachios and the culinary value of crushed pistachios.
144-
145- Noun
146- [ edit ] 
147-
148- pstk' • ( pistag )
```


## [2026-09-05T14:41:20.034Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg99.png"
}
```


### [2026-09-05T14:41:20.388Z] TOOL RESULT

```

```


## [2026-09-05T14:41:20.385Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T14:41:29.819Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 99 -l 99 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg99_400 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg99_400.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.28),int(h*0.34),int(w*0.80),int(h*0.40))).save('pg99_french.png')\n\""
}
```


### [2026-09-05T14:41:32.958Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-05T14:41:34.768Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg99_french.png"
}
```


### [2026-09-05T14:41:34.783Z] TOOL RESULT

```

```


## [2026-09-05T14:41:48.106Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT leaf for pistachio ===\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"Piatachio\")>0 || index($0,\"pistacimm\")>0) print \"leaf(1-based)=\"n\", printed=\"n-20}' SKT.txt\necho \"=== NYB pist ===\"; grep -n -i \"pistak\\|pistag\\|Pistazie\" NYB_vol1.txt NYB_vol2_glossary.txt | head\necho \"=== PHD leaf ===\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"pistag [pstk\")>0) print \"PHD leaf(1-based)=\"n\", printed=\"n-21}' PHD.txt\necho \"=== POK peis- crush ===\"; grep -n \"peis-\\|pis-to-\\|pistó\" POK_full.txt | head -10\necho \"=== SIN pistachio ===\"; grep -n -i \"pistachio\\|pistacia\" SIN.txt | head -5"
}
```


### [2026-09-05T14:41:49.635Z] TOOL RESULT

```
=== SKT leaf for pistachio ===
leaf(1-based)=378, printed=358
=== NYB pist ===
NYB_vol2_glossary.txt:2752:nipistan [npštn'; YKTYBWN-tn'] nipés- to write 419. 110? etc. ; nipist estet it has been written, it is written 1139; nipist ēstāt it was written 1!—?; — pres. pass. nipēsihēt [YKTYBWN-yhyt'] is being written 18%; — pat dp i zarr nipištak 1079; apar nipistak written down 108?!; nāmak ~ 6 to write a letter to 49-9. 822, an inscription P 2:3.4; apar fravartak čton nipišt estat kū it was written in the letter (then dir. speech) 1872; apar én ayyätkär nipišt estet 1135-9. — OP ni-pais- ; MPrthPrs nbyštn nbys-; Paz. nawaštan nivés-; NP nuvistan, nivištan, nivés-.
NYB_vol2_glossary.txt:3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
=== PHD leaf ===
PHD leaf(1-based)=95, printed=74
=== POK peis- crush ===
65150:Root / lemma: {peis-'H) : pis- 
65176:Root / lemma: peis-2, speis- 
65180:Material: With s-/ Latin spTro, -are'b\o\N, breathe, breathe' {*speis-), spTritus, -Js "breath, 
70786:e. reup- ^ausre'\Q>en, tear, break, rupture'; roupa-^ho\e, aperture ', rupeis-xocV! . 
=== SIN pistachio ===
60:The  Pistachio   246
176:"The  principal  fruits  are  of  thirty  kinds,  and  there  are  ten  species the  inside  and  outside  of  which  are  fit  to  eat,  as  the  fig,  the  apple,  the quince,  the  citron,  the  grape,  the  mulberry,  the  pear,  and  others  of  this kind.  There  are  ten  the  outside  of  which  is  fit  to  eat,  but  not  the inside,  as  the  date,  the  peach,  the  white  apricot,  and  others  of  this  kind; those  the  inside  of  which  is  fit  to  eat,  but  not  the  outside,  are  the  walnut, the  almond,  the  pomegranate,  the  coco-nut,1  the  filbert  (Junduk),  the chestnut  (Sahbalut),  the  pistachio  nut,  the  vargdn,  and  whatever  else of  this  description  are  very  remarkable.
672:THE  PISTACHIO
673:3.  Pistacia  is  a  genus  of  trees  or  shrubs  of  the  family  Anacardiaceae, containing  some  six  species,  natives  of  Iran  and  western  Asia,  and  also transplanted  to  the  Mediterranean  region.  At  least  three  species (Pistacia  vera,  P.  terebinthus,  and  P.  acuminata)  are  natives  of  Persia, and  from  ancient  times  have  occupied  a  prominent  place  in  the  life  of  the Iranians.  Pistachio-nuts  are  still  exported  in  large  quantities  from Afghanistan  to  India,  where  they  form  a  common  article  of  food  among the  well-to-do  classes.  The  species  found  in  Afghanistan  and  Baluchis- tan do  not  cross  the  Indian  frontier.1  The  pistachio  (Pistacia  vera)  in particular  is  indigenous  to  ancient  Sogdiana  and  Khorasan,2  and  still is  a  tree  of  great  importance  in  Russian  Turkistan.3
675:The  youths  of  the  Persians  were  taught  to  endure  heat,  cold,  and rain;  to  cross  torrents  and  to  keep  their  armor  and  clothes  dry;  to pasture  animals,  to  watch  all  night  in  the  open  air,  and  to  subsist  on wild  fruit,  as  terebinths  (Pistacia  terebinthus),  acorns,  and  wild  pears.8
```


## [2026-09-05T14:41:49.866Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://ahdictionary.com/word/search.html?q=fustic\" \"https://ahdictionary.com/word/search.html?q=albacore\" \"https://ahdictionary.com/word/search.html?q=pistachio\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 99: AHD entries for fustic/albacore/pistachio (Nourai cites AHD:535, AHD:29, AHD:998)\"; done"
}
```


### [2026-09-05T14:41:52.594Z] TOOL RESULT

```
### https://ahdictionary.com/word/search.html?q=fustic
/home/sfmqrb/git/rishe/data/verification/sources/web/5055ca877a76574a.txt
### https://ahdictionary.com/word/search.html?q=albacore
/home/sfmqrb/git/rishe/data/verification/sources/web/0ff1f83aad2c4d73.txt
### https://ahdictionary.com/word/search.html?q=pistachio
/home/sfmqrb/git/rishe/data/verification/sources/web/ca3cfbd550126655.txt
```


## [2026-09-05T14:42:00.130Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 5055ca877a76574a 0ff1f83aad2c4d73 ca3cfbd550126655; do echo \"=== $f ===\"; grep -n -i -o \"\\[.\\{0,300\\}\\]\" $f.txt | head -8; echo \"---raw---\"; grep -n -i \"Middle English\\|Arabic\\|Persian\\|Portuguese\\|Spanish\\|Greek\" $f.txt | head -10; done"
}
```


### [2026-09-05T14:42:01.717Z] TOOL RESULT

```
=== 5055ca877a76574a ===
50:[Middle English fustik , from Old French fustoc , from Arabic fustuq , from Greek pistak ē , pistachio; see PISTACHIO .]
---raw---
50: [Middle English fustik , from Old French fustoc , from Arabic fustuq , from Greek pistak ē , pistachio; see PISTACHIO .]
=== 0ff1f83aad2c4d73 ===
48:[Portuguese albacor , from Arabic al-bak ū ra : al- , the + bak ū ra , albacore; see bkr in the Appendix of Semitic roots .]
---raw---
48: [Portuguese albacor , from Arabic al-bak ū ra : al- , the + bak ū ra , albacore; see bkr in the Appendix of Semitic roots .]
=== ca3cfbd550126655 ===
49:[Ultimately (partly via Middle French pistache ) from Italian pistacchio , from Latin pistacium , pistachio nut, from Greek pistakion , from pistak ē , pistachio tree, of Iranian origin; akin to Middle Persian pistag .]
---raw---
49: [Ultimately (partly via Middle French pistache ) from Italian pistacchio , from Latin pistacium , pistachio nut, from Greek pistakion , from pistak ē , pistachio tree, of Iranian origin; akin to Middle Persian pistag .]
```


## [2026-09-05T14:42:01.762Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"Spanish  from  Latin  from  Greek  from\")>0) print \"SKT leaf=\"n\", printed=\"n-20}' SKT.txt\necho \"--- SIN pistachio section ---\"; sed -n '672,700p' SIN.txt | head -40"
}
```


### [2026-09-05T14:42:03.541Z] TOOL RESULT

```
SKT leaf=640, printed=620
--- SIN pistachio section ---
THE  PISTACHIO
3.  Pistacia  is  a  genus  of  trees  or  shrubs  of  the  family  Anacardiaceae, containing  some  six  species,  natives  of  Iran  and  western  Asia,  and  also transplanted  to  the  Mediterranean  region.  At  least  three  species (Pistacia  vera,  P.  terebinthus,  and  P.  acuminata)  are  natives  of  Persia, and  from  ancient  times  have  occupied  a  prominent  place  in  the  life  of  the Iranians.  Pistachio-nuts  are  still  exported  in  large  quantities  from Afghanistan  to  India,  where  they  form  a  common  article  of  food  among the  well-to-do  classes.  The  species  found  in  Afghanistan  and  Baluchis- tan do  not  cross  the  Indian  frontier.1  The  pistachio  (Pistacia  vera)  in particular  is  indigenous  to  ancient  Sogdiana  and  Khorasan,2  and  still is  a  tree  of  great  importance  in  Russian  Turkistan.3
When  Alexander  crossed  the  mountains  into  Bactriana,  the  road was  bare  of  vegetation  save  a  few  trees  of  the  bushy  terminthus  or terebinthus.4  On  the  basis  of  the  information  furnished  by  Alexander's scientific  staff,  the  tree  is  mentioned  by  Theophrastus5  as  growing  in the  country  of  the  Bactrians;  the  nuts  resembling  almonds  in  size and  shape,  but  surpassing  them  in  taste  and  sweetness,  wherefore  the people  of  the  country  use  them  in  preference  to  almonds.  Nicandrus of  Colophon6  (third  century  B.C.),  who  calls  the  fruit  fiiaranov  or  ^lttolklov, a  word  derived  from  an  Iranian  language  (see  below),  says  that  it  grows in  the  valley  of  the  Xoaspes  in  Susiana.  Posidonius,  Dioscorides,  Pliny, and  Galenus  know  it  also  in  Syria.  Vitellius  introduced  the  tree  into Italy;  and  Flaccus  Pompeius,  who  served  with  him,  introduced  it  at the  same  time  into  Spain.7
The  youths  of  the  Persians  were  taught  to  endure  heat,  cold,  and rain;  to  cross  torrents  and  to  keep  their  armor  and  clothes  dry;  to pasture  animals,  to  watch  all  night  in  the  open  air,  and  to  subsist  on wild  fruit,  as  terebinths  (Pistacia  terebinthus),  acorns,  and  wild  pears.8
1  Watt,  Dictionary  of  the  Economic  Products  of  India,  Vol.  VI,  p.  268.
2  Joret,  Plantes  dans  l'antiquite\  Vol.  II,  pp.  47,  76.
3  S.  Korzinski,  Vegetation  of  Turkistan  (in  Russian),  pp.  20,  21.
4  Strabo,  XV.  11,  10.
■  Hist,  plant.,  IV.  iv,  7. "Theriaka,  890.
7  Pliny,  xv,  22,  §91.  A.  de  Candolle  (Origin  of  Cultivated  Plants,  p.  316) traces  Pistacia  vera  only  to  Syria,  without  mentioning  its  occurrence  in  Persia.
8  Strabo,  XV.  hi,  18.
246
The  Pistachio  247
The  Persians  appeared  to  the  ancients  as  terebinth-eaters,  and  this title  seems  to  have  developed  into  a  sort  of  nickname:  when  Astyages, King  of  the  Medians,  seated  on  his  throne,  looked  on  the  defeat  of  his men  through  the  army  of  Cyrus,  he  exclaimed,  "Woe,  how  brave  are these  terebinth-eating  Persians!"1  According  to  Polyaenus,2  terebinth- oil  was  among  the  articles  to  be  furnished  daily  for  the  table  of  the Persian  kings.  In  the  Bttndahisri,  the  pistachio-nut  is  mentioned  to- gether with  other  fruits  the  inside  of  which  is  fit  to  eat,  but  not  the outside.3  "The  fruits  of  the  country  are  dates,  pistachios,  and  apples of  Paradise,  with  other  of  the  like  not  found  in  our  cold  climate."4
Twan  C'en-si  It  $  ^,  in  his  Yu  yah  tsa  tsu  MiiS,  written about  a.d.  860  and  containing  a  great  amount  of  useful  information on  the  plants  of  Persia  and  Fu-lin,  has  the  following: —
"The  hazel-nut  (Corylus  heterophylla)  of  the  Hu  (Iranians),  styled a-yiie  H  M ,  grows  in  the  countries  of  the  West.6  According  to  the statement  of  the  barbarians,  a-yiie  is  identical  with  the  hazel-nuts of  the  Hu.  In  the  first  year  the  tree  bears  hazel-nuts,  in  the  second year  it  bears  a-yiie."6
C'en  Ts'an-k'i  W  W.  II,  who  in  the  K'ai-yuan  period  (a.d.  713-741) wrote  the  Materia  Medica  Pen  ts'ao  H  i  ^  #•  &  5ft,  states  that  "the fruits  of  the  plant  a-yiie-hun  M  R  W-  are  warm  and  acrid  of  flavor, non-poisonous,  cure  catarrh  of  the  bowels,  remove  cold  feeling,  and make  people  stout  and  robust,  that  they  grow  in  the  western  countries, the  barbarians  saying  that  they  are  identical  with  the  hazel-nut  of  the Hu  fifl  $1  -?\  During  the  first  year  the  tree  bears  hazel-nuts,  in  the second  year  it  bears  a-yiie-hun."
Li  Sun  ^  ^J,  in  his  Hat  yao  pen  ts'ao  M  M  ♦  ^  (second  half  of  the eighth  century),  states,  "According  to  the  Nan  lou  ki  ^f  #H  12  by Su  Piao  fe  $£,7  the  Nameless  Tree  (wu  mih  mu  $&  %\  /fc)  grows  in  the mountainous  valleys  of  Lin-nan  (Kwan-tun) .  Its  fruits  resemble  in  appear- ance the  hazel-nut,  and  are  styled  Nameless  Fruits  (wu  mih  tse  $&  &
1  Nicolaus  of  Damaskus  (first  century  B.C.),  cited  by  Hehn,  Kulturpflanzen, p.  424.
*  Strategica,  IV.  111,  32.
8  These  fruits  are  walnut,  almond,  pomegranate,  coconut,  filbert,  and  chestnut. See  West,  Pahlavi  Texts,  Vol.  I,  p.  103.
4  Marco  Polo,  Yule's  edition,  Vol.  I,  p.  97.
8  The  editions  of  the  Yu  yan  tsa  tsu  write  ©  HI,  "in  the  gardens  of  the  West"; but  the  T'u  Jm  tsi  I'en  (section  botany,  Ch.  311)  and  Ci  wu  tnin  H  t'u  k'ao,  in  repro- ducing this  text,  offer  the  reading  ]§  S ,  which  seems  to  me  preferable.
8  Yu  yan  tsa  tsu  jj||  ft,  Ch.  10,  p.  3  b  (ed.  of  Tsin  tat  pi  Su).
7  This  work  is  quoted  in  the  Ts'i  min  yao  Su,  written  by  Kia  Se-niu  under  the Hou  Wei  dynasty  (a.d.  386-534).
248  Sino-Iranica
■?■).  Persians  3£  $ft  1%.  designate  them  a-yiie-hun  fruits."1  For  the  same period  we  have  the  testimony  of  the  Arabic  merchant  Soleiman,  who wrote  in  a.d.  851,  to  the  effect  that  pistachios  grow  in  China.2
As  shown  by  the  two  forms,  a-yiie  of  the  Yu  yan  tsa  tsu  and  a-yiie-hun of  the  Pen  ts'ao  H  i  and  Hai  yao  pen  ts'ao,  the  fuller  form  must  repre- sent a  compound  consisting  of  the  elements  a-yiie  and  hun.  In  order  to understand  the  transcription  a-yiie,  consideration  of  the  following  facts is  necessary.
The  Old-Iranian  word  for  the  walnut  has  not  been  handed  down  to us,  but  there  is  good  evidence  to  prompt  the  conclusion  that  it  must have  been  of  the  type  *ag5za  or  *ahgOza.  On  the  one  hand,  we  have Armenian  engoiz,  Ossetic  angozii  or  anguz,  and  Hebrew  egdz;3  on  the other  hand,  we  meet  in  Yidgha,  a  Hindu-Kush  language,  the  form ogiizo,  as  compared  with  New  Persian  koz  and  g5z.A  The  signification of  this  word  is  "nut"  in  general,  and  "walnut"  in  particular.  Further, there  is  in  Sanskrit  the  Iranian  loan-word  akhdta,  aksofa,  or  aksoda, which  must  have  been  borrowed  at  an  early  date,  as,  in  the  last-named form,  the  word  occurs  twice  in  the  Bower  Manuscript.5  It  has  survived in  Hindustani  as  axrot  or  dkrot.  The  actual  existence  of  an  East- Iranian  form  with  the  ancient  initial  a-  is  guaranteed  by  the  Chinese transcription  a-yiie;  for  a-yiie  M  M  answers  to  an  ancient  *a-hwie5 (hw'e5)  or  *a-gwie5,  a-gwii5;6  and  this,  in  my  opinion,  is  intended  to represent  the  Iranian  word  for  "nut"  with  initial  a-,  mentioned  above; that  is,  *ahgwlz,  angwOz,  agOz.
```


## [2026-09-05T14:42:18.681Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SIN pistak etymology ===\"; grep -n -i \"pistak\\|bistak\\|pistag\\|Middle Persian.*pist\\|Pahlavi.*pist\" SIN.txt | head -20"
}
```


### [2026-09-05T14:42:18.728Z] TOOL RESULT

```
=== SIN pistak etymology ===
319:In  ancient  Iran,  alfalfa  was  a  highly  important  crop  closely  associated with  the  breeding  of  superior  races  of  horses.  Pahlavi  aspast  or  aspist New  Persian  aspust,  uspust,  aspist,  ispist,  or  isfist  (Pu§tu  or  Afghan  spastu, SpeZta),  is  traceable  to  an  Avestan  or  Old-Iranian  *aspo-asti  (from  the root  ad,  "to  eat"),  and  literally  means  "horse-fodder."2  This  word  has penetrated  into  Syriac  in  the  form  aspesta  or  pespestd  (the  latter  in  the Geoponica).  Khosrau  I  (a.d.  531-578)  of  the  Sasanian  dynasty  included alfalfa  in  his  new  organization  of  the  land-tax:3  the  tax  laid  on  alfalfa was  seven  times  as  high  as  that  on  wheat  and  barley,  which  gives  an idea  of  the  high  valuation  of  that  forage-plant.  It  was  also  employed in  the  pharmacopoeia,  being  dealt  with  by  Abu  Mansur  in  his  book on  pharmacology.4  The  seeds  are  still  used  medicinally.5  The  Arabs derived  from  the  Persians  the  word  isfist,  Arabicized  into  fisfisa;  Arabic designations  being  ratba  and  qatt,  the  former  for  the  plant  in  its  natural state,  the  latter  for  the  dried  plant.6
726:The  Japanese  name  fusudasiu  or  fusudasu  is  doubtless  connected with  Persian  pista,  from  Old  Iranian  *pistaka,  Middle  Persian  *pistak,8 from  which  is  derived  Greek  /SicrdKiov,  ^ittclkiov,  TnaraKiov  or  ^iotcucioj', Latin  psittacium,  and  our  pistacia  or  pistachio.  It  is  not  known  to  me, however,  to  what  date  the  Japanese  word  goes  back,  or  through  what channels  it  was  received.  In  all  likelihood  it  is  of  modern  origin,  the introduction  into  Japan  being  due  to  Europeans.
5985:*agoz-van  250 agOza,  angOza  248,  254 aspo-asti  209 a§i  301 bangha  294 budawa  225 *buksuk,  buxsux  213 dipi  532 *go§wi  298 hafianaepata  277 •koswi  298 ma5a  241 maSav  225 magupati  53 1 *pistaka  251 spaina  515 tanva  496 x5adra-pavan  529 xsa^rya  530 xsaeta  530 x§ayafiiya  530
6008:parnlkan  537 *pistak  251
```


## [2026-09-05T14:42:20.130Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- SKT page markers near 14076 ---\"; sed -n '14040,14100p' SKT.txt | grep -nE \"^[0-9]{2,4}$|Page|PISTACHIO\"\necho \"--- lines 14070,14080 ---\"; sed -n '14070,14082p' SKT.txt"
}
```


### [2026-09-05T14:42:21.964Z] TOOL RESULT

```
--- SKT page markers near 14076 ---
53:353
--- lines 14070,14080 ---
PISTOL.
Pisoee.  the  Fish.  (L.)  L. /urn,  pi.  il pistil^  a  6sh  ;  cognate  with  E.  FiaU,  q.  t.
Plah  I  ^E.)  Uf  imitative  origin  ;  begin- ning with  expnlfiioa  of  breath,  and  enaiii| in  a  hiss.
Pismire ;  see  Piaa.
Piae.  (F.)  F.  piutrx  ropposcd  lolci Romance  word,  and  of  imitative  oitiziu
pismire,  an  ant  (F.  ^nd  &  . old  name  of  the  ant ;  from  i. urinous  smell  of  an  antliill.  Ric  imi syllable  is  from  F.  pisstr  (above),  ^.  TW second  is  M.  E.  mirt,  an  ant;  from  Swtl myra,  Dan.  myrt,  Icel.  m$aHrrf  an  nl This  word  for  *ant*  is  widely  sprad  i  d Irish  ptoir6k,  W.  mcr-^rtigym,  Ku» muravei,  Gk.  tivpfii^,  an  ant :  CanL mitf-rian,  ants.
Piatachio.  Pistaoho,  the  mit  of  1 ccrtiiin  tree.  (Span.  —  L.  —  Gk.  —  Pet*l Span,  pistacho.  ••  L.  pistacimm.  —  Gk wxcramov,  a  nut  of  the  tree  called  rtviici.
—  Pers.  pistah,  the  pistachio  nut.
Pistil,  in  a  flower.  (L.*!  Named  fi«a the  resemblance  in  shape  to  the  pestle  erf  l mortar.  -  L.  pistillum^  «  smsU  pal)^ dimin.  of  an  obsolete  form pestle.  — L.  piscum,  supme  of pound. -^Gk.  ariff^ii',  Skt, /u4,  to (V  PIS.)
pestie.   (F.-L.)    M.E, /«>^/.»0.R pejtfl.  later  petttU  (CoU).- ( above).
piston.  (F.-llol.-L)     F. pestcll.'  Cot. ;  also  a  piuon.*  ItaL a  piston :  ptstoHt.  a  large   pestle. putiiri.  Late  L.  piitare,  to  poiadrj
(F. F.  piifoU.  -  Ital.  pistc'a, '  a  dag  or Florio.     \Vc  aUo  fmd  O.  lal. grcut  dagger,*  in  Florio ;  and  tt  a that    the    name   was    5rst    applied dagger,  and  thence  tron&ieitcd  to  the  pis^ which  even  in  E.  was  at  fir^l  c^Ue^l  1 (F.  a!af«/,  a  dagger).     A  ' what  a  dagger  is  to  a  sw< PistoUig  (,  =  Low  \^  piste:. longing  lo  Pistola  ;    so  n from  Piftola^  now  called in  Tuscany,  near  Florcnct     The name  of  the  town  was  /Httori*,
pistole,  s  gold   coin  01  Spain. Ital.)    Thennmc.  bowercr,  is  not but   French,    and   the   corns  wcfc   it called  pmMits.     The  name  is  of  ioet origin. -F.  pistoUt,  a  little  plilot.  al»
```


## [2026-09-05T14:42:44.997Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT پسته headword ===\"; grep -n \"پسته\" BQT_v1_pages.txt | sed -n '1,40p'\necho \"=== ARY پسته ===\"; grep -n \"پسته\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY latin index ===\"; grep -n -i \"PESTE\\|PISTACHIO\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-05T14:42:45.074Z] TOOL RESULT

```
=== BQT پسته headword ===
7543:است که از فند ومغز بادام و پسته و تخود مقس
14810:زنند خصوساً - و بادام و پسته وکردکان وامثال
17268:غالیه گویند و آن مانند پسته میباشد لیکن زود
19461:۵ 4 - بنم‌اول , م رکب از : بز + غاله (کاله) شانة صضیر«اسفا!:۲سص۹۹» ؛ بچةٌ بز .کنفه . کوبند که‌درخت‌پسته مکال میوه‌فزدار
19696:درخت پسته است » و بعضی گویند کندر است >
19725:پسته و چم - بفتح را وکر حا هر دو
27904:پسته ‏ وبلا فاسله هم‌آمده است - و کسی رالیز
=== ARY پسته ===
=== ARY latin index ===
```


## [2026-09-05T14:42:47.058Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== UNV gurgan/hyrkan ===\"; grep -n -i \"gurgan\\|hyrkan\" UNV.txt | head\necho \"=== UNV leaves ===\"; awk 'BEGIN{RS=\"\\f\"} {n++} END{print n\" leaves\"}' UNV.txt\necho \"=== FVQ fustuq ===\"; grep -n -i \"fustuq\\|pistachio\" FVQ_pages.txt | head"
}
```


### [2026-09-05T14:42:48.699Z] TOOL RESULT

```
=== UNV gurgan/hyrkan ===
608:51.  Die  hyrkanische  Pi¬ staziennuß  ,  wenn  man  sie auf  einem  Bräter  röstet,  und frische  Linsen,  wenn  man  sie mit  dem  Saft  der  Oliven  ißt.
=== UNV leaves ===
47 leaves
=== FVQ fustuq ===
```


## [2026-09-05T14:42:57.152Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '27895,27915p' BQT_v1_pages.txt\necho \"--- pdf page tag ---\"; awk 'NR<=27904 && /\\[pdf page/ {p=$0} END{print p}' BQT_v1_pages.txt\necho \"=== search فستق in BQT v1 ===\"; grep -n \"فستق\" BQT_v1_pages.txt BQT_v2_pages.txt | head"
}
```


### [2026-09-05T14:43:00.470Z] TOOL RESULT

```
ویمعنی پیوند هم هست که ماضی پیوسئن وپیود
کردن و الحاق باشد- و باسطلاح .-حنفین‌وسول
سالك است از قید شید بدرجهٌ اطلاق حققت
اسدای ای فان لس ای
شد ۵ .
پیوستگان + مر کباترا گونند همچو
نبات وجماد وحیوان ٩‏ .»
مق ست4 » بروزن برجسته, بمعنی‌هميشه
ودایم باشد - ویمعنی پیوند کرده شده و در عم
پسته ‏ وبلا فاسله هم‌آمده است - و کسی رالیز
کون د که از بیاری کریستن تواند مخن گفتن
وگن کوند گر برمخنش أفد رد
. مازندرانی کتونی
برادران را بوسف چو داد گندم وجو
اگر بناعت مزجاه . پشم و پینو بود
۳ - رشك: سنو .
۴ رژد: سوس.
فرهنگه دساتس .
۵ _ ره :
نبود گندم وجولیر جز تیک
سوزنی‌سمر قندی. #جهانگیری».
--- pdf page tag ---

=== search فستق in BQT v1 ===
BQT_v1_pages.txt:25742:۵ پسه ‏ بکر اول وشتح سوم» درتازی فستق ازآرامی فتفا (بکسراول), چه معا آن
BQT_v2_pages.txt:2220:                                                               ‫روزه چ»یزی باشد مانند فستق و باریکتر ازآن‬
BQT_v2_pages.txt:2410:‫و چون بشکننددرون‌آن فستقی بودکرم‌مصده را‬
BQT_v2_pages.txt:6612:                                      ‫‪« - ۴‬چلنوزه» چیزی‌است مانندفستق‪ .‬رود کی(سمرقندی) گوید‪:‬‬
```


## [2026-09-05T14:43:07.123Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '25735,25760p' BQT_v1_pages.txt\necho \"--- nearest pdf page tag before ---\"; awk 'NR<=25742 && /pdf page/ {p=$0;n=NR} END{print n\": \"p}' BQT_v1_pages.txt\necho \"--- any tags? ---\"; grep -c \"pdf page\" BQT_v1_pages.txt; grep -n \"pdf page\" BQT_v1_pages.txt | head -3\necho \"--- form feed count before line ---\"; awk 'NR<=25742{c+=gsub(/\\f/,\"\")} END{print \"leaf(0-based)=\"c}' BQT_v1_pages.txt"
}
```


### [2026-09-05T14:43:08.581Z] TOOL RESULT

```
مقطح مت
یرون میا بد:
تهی‌دید پستان کاوش زشیر دل میزبان جوان کشت پیر .
فردوسی طوسی. «لفت نامه».
۵ پستاقك - بکسر اول وفتح پنجم ( از: منان ۵ پوند شباحت) »
ظرفی ازبلور با غیر آن شبیه بستان که مادران بی‌شیر» شیرحیوان با زنی دیگر
پتانك در آن‌کنند وبدهان طفل هند . * لفت نامه *.
۵ پسه ‏ بکر اول وشتح سوم» درتازی فستق ازآرامی فتفا (بکسراول), چه معا آن
شام ( سوربه ) است و بونانی نقل شد ۳۱50۵108 و از آن
بدیگر زبانهای ارویابی داخن شد . در ابتالیابی نمی 5)2ز۳ هه
«لفس» ؛ درختی است میوه دار که درآب و هوای معتدل واراضی --
سيك خوب میروید . مهمترین نوع آن همان یسته معمولی تک
( ۷۵۲2 ۱582012 ) است . مراکز مهم یس ابران کرمان,
آذرباجان» داعفان وفزوناست.رگ: فرهنگه روستابی۲۷۵ بعد بسله
وثابتی ۱۷۰ و کل کلاب ۰۲۱۷ ۱
۵ پسر - بکس اول وفتح دوم (درلهجةٌ مر کری) » در پارسی باستان واوستا ۳09072 ؛
پهلوی ۳فکنا۳ و کنام [ رك و ره سیون , کردی 15 . استی +5
واع1] , بلوچی 0۱1528 , وخی 0۵4۲ : شغنی 0۷6 . سربکلی ۳4: عنجی ۳۲ » ممرب
آن قور در قنفور؛ امه ها ور مه راک ممصص :ریات
#9" , نطنزی ۳0۲ <2 . ۱ص ۸۵ ۰ ۰ سمثانی ۳1۳ ۶ مشگکری و نرخةٌ
ولاسگردی0ا۳» شهمیرزاوی ۳6526۲ 4 ,۲ صس ۱۸۷ در فارسی نیز پس ویور؛ فرژند فرینه
این . ولد .پربچه ی ۱ ۱ وت
مخنور " مخذف پسواندو است که پسر ژن باشد
از شوهر دبگر با پسر شوهر باشد اززن دمگو»
و بکس اول بروزن سکندر همآمده‌است.
بسنده؟ سٍ بروزن‌دهنده مخفف بند نده
--- nearest pdf page tag before ---
: 
--- any tags? ---
0
--- form feed count before line ---
leaf(0-based)=629
```


## [2026-09-05T14:43:29.716Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB fistic ===\"; grep -n -i \"fistic\\b\\|fistick\" WEB_vol1.txt FSD_vol2.txt | head -10\necho \"=== WEB fustic entry ===\"; sed -n '79170,79180p' WEB_vol1.txt\necho \"=== FSD fustic entry 28447 ===\"; sed -n '28445,28452p' FSD_vol2.txt"
}
```


### [2026-09-05T14:43:29.829Z] TOOL RESULT

```
=== WEB fistic ===
WEB_vol1.txt:73853:fist/ic, a. having to do with boxing; fought with the fists; pugilistic; as, fistic exploits; fistic heroes. [Colloq.]
FSD_vol2.txt:21124:lls"tl-an'a,  n.  pi.  l^uglllstlo  anecdotes  or  Items.—  list'lc,  55 1, a.  Pertaining  to  tbo  fists,  e.speclalli’  when  used  In  boxing:  ’ lienee,  puglltstle;  as,  the  fisHo  arena;  a   fistic  career.-  Hst'- wl.se,  a.  Like  a   fist.— Ilst'y.  I.  a.  [Haro.]  Relating  to the  lists  or  pugilism.  II.  [Dial,]  A   fist. flst>,n.  ApulTbalU  [<  Ico.  jlsa,  break  wind.) lists,  1   foist,.  3   fist,  ft,  [S.  &   W.  U.  fJ.l  1.  Same  as  exob.  3.
=== WEB fustic entry ===
against excess of current; also, a plug in a Europe; the Ulex europeus. system of water pipes, for fire protection of
fii’si-form, a. [L. fusus, a spindle, and forma, Dene, n. a small bird found in southern form.] shaped like a spindle; thick, tapering mgland,
3. made by melting and molding, or cast-
/ fū’şil, n. (Fr. fusil, a steel for striking fire, a fi : fusus, a spindle, shaft of a column.]in musket; It. focile, fucile; LL. focile, a steel for
; ‘archi! e, ldi iL: dun- Striking fire, from L. focus, a fireplace.] an te daretie Bere molding generally Pen un old-fashioned, light musket or firelock resem-
fū’şil, n. [from L. fusus, a spindle.] a bearing in
, far, fast, fall, final, cdre, at; méte, prey, hér, met; pine, marine, bird,
fustic
fi-sil-lade’, n. [Fr. fusi ‘ . fusilla. shoot, from fusil, a aukai from fusiltey i l. a simultaneous or stil : cipcharee 3: many firearms » Something lik is: a questions. Se tbis Tasa fusillade of fu-sil-lade’, v.t.; fusilladed, Dl be ete roe phr. to attack and fight wit Pa fsllag. ū’şion, n. [L. fusio, Silla, melt.]’ Ue from fundere, to pour a 1. a fusing; a melting or melti ' _.2. (a) the union of different thas together. if by melting; a blending; coals ey Fas fusion of political parties; (b) thay as, a fact of being so united, ` € state or 3 anything roade by fusing . in biology, t i > separated, Ey: the MnOn tot parts Usually 5. in optics, the act of bringi visual line so that the rays fone eyes in point fall on corresponding localitie a single eye and are conveyed to a single TR In each ter, producing the impression of asua cen- watery fusion; the melting of a cr Stana water of crystallization by heat, tl iMits fū’şion-işm, n. in politics, the support coalition of parties or factions pelts fai’sion-ist, n. an adherent of fu coe in a political fusion, u/’sion-ist, a. of fusionism or fusioni fu’soid, a. same as Susi orm. a forgome, a. handsome; neat; notable, [Brit, fuss, n. [17th-c. slang, prob. echoi : 2 ', P ' oic, used es in phr. keep a fuss with y p. RE paf (now, make a fuss 1. a bustle; unnecessary activi trivial matters; a nervous, ‘excited etal aa 2. a fussy person, $ yn.—stir, excitement, tumult, bustle, flurry, fidget. bedese ceo, fuss, v.i.; fussed (fust), pt., pp.; fussi » Dt., BA sing, È ALE about or worry, especially is fuss, v.t. to bother or worry with trifling mat- ters; to make uncomfortable. [Colloq.] fuss’ball, n. same as fussball. fuss’-budg"et, n. [fuss and budget, prob, in sense of ‘bag, sack.’*] a fussy person. [Colloq.] fuss/i-ly, adv. with much ado, fuss/i-ness, n. the quality of being fussy. fuss/dck, 7. a large, fleshy woman. [Brit. Dial.) fuss’y, a.; comp. fussier; superl. fussiest, 1. ha- Pitually susan; bustling about or worrying over trifles. 2. showing or needing careful attention. 3. full of details, especially if unnecessary or showy. fust, v.i. to become moldy or fusty. [Obs.] fust, n. [OFr. fustié, fusty, tasting of the cask, from fuste, a cask.] a strong, musty smell. (Brit. Dial.] © fust, n. [OFr. fust, fuist, a stick, shaft, tree, from L. fuslis, a knobbed stick, club.] in ar- chitecture, the shaft of a column from the astragal to the capital. fus-ta-nelle’, fus-ta-nel/la, n. (LL. fustanella, from fustianwm, a fustian,] a short white pet- ticoat sometimes worn by men in modern Greece. Pe fus’tee, fus’tie, n. [W. Ind.] the offspring of a white person and an octoroon. prub fus/tér-ic, n. the coloring matter of the s fustet. fus’tet, n. [Fr. fustet; LL. fustetus, a tree, from L. fustis, a stick.] $ ; i the wood of the Rhus cotinus, or Venice sumac. 2. the tree itself. r x fus/tiin (-chän), n. [ME. fustian; Om taine, from LL. fustianum, fustanum, tus T. prob. from Jusis, wooden stick, transl. 0 xylinon, wooden. d ot originally, a coarse cloth of cotton an linen. Shoe f- 2. now, a coarse, twilled cotton stuff, as CO duroy, velveteen, etc. s iting; 3. an inflated style of talking or bombast; rant; high soe pales een fus/tiin, a. 1. made of fustian. | tic; 2. pompous; ridiculously tumid; bombastic pretentious but empty. bast. fus’tiăn-ist, n. one who writes bomb
fus’tic, n. [Fr. fustoc; Sp. fustot, fustie
and continuous
=== FSD fustic entry 28447 ===
.   fas'tl-bale,  1   fus'ti-iiBl;  2   fria'ii-;i»ii,  n.  A   stafl-sUng.  [< L.  fusiis,  stafl,  +   Gr.  hallo,  throw.]  fus-tib'a-lust. fus'tic,  1   fus'tik;.  8   fiis'tic,  n.  The  wood  of  the  Chloro- ,   :   phoratinctoria,  oHho  family  Moracets.  oi  South  Amer- ’"a  and  the  West  Indies,  u.sed  as  a   yellow  dyestuff;
feet  tense,  a   tense  expressing  action  as  past  with  reference to  a   point  In  the  future;  as,  **  I   shall  have  gone.”—  f.  tense, that  tense  of  a   verb  or  verbal  form  that  expresses  future action  or  time.— f.  yield  (Forailry),  the  amoimt  of  wood which  given  trees  upon  a   given  area  will  contain  after  a given  period.— f. -yield  table  (Fomlry),  a   tabular  state- ment or  record  of  future  yield.  Giffoed  Pinchot  Terms Used  in  Forestry,  V.  S.  Dept,  of  Ayr.,  Bulletin  No.  61 .   [aov. PTo.  OFF.  ’05.]  —   fu't«re-lyt,  adv.  In  the  future.— fu'- turc-ness,  n.  Futurity.—  ftt'tar-!ze,-’»L  [Rare.]  To  ex-
yellowwood;  old  fustic.  [ <   F. /usfoc,  <   Sp. /jistoc,  <   -   ,   -   -
/a, 2(e«e,  smoke-tree,  <   L. /wHs,  club.]  fus'Uket;  fus'toct-  press  future  action  or  time.
—   American  fustic, the  yelUiwwood  of  tbe  southern  United  fu'ture,  it.  1.  The  time  yet  to  come;  time  later  than
States  (CJadrasfis  ifectoria).— old  f.,  same  as  fustic.— young  f.,  the  wood  ot  Cotinus  catlnus.  Xho  Venetian  sumac, usad  as  a   yellow  dycBtuft.  fus'tett. fus':ti-gate,lfus'ti-g6t;  2faa't{-gat, [-gat'bd;  -gat"- ING.]  To  beat  with  a   stick;  cudgel.  [<  L.  fustigaius,  pp. ,   of/Msfitfo,<  /«sfis,  club,-!-  affo,  drive.]  —   fus"tl-ga'tloii,  n, — fus'fcl-ga"tor,n.
the  present;  that  which  will  be  or  occur  in  time  subse- quent to  the  present;  as,  to  live  in  the  future;  to  reveal the  future;  specif.  (Relig.),  the  state  of  the  soul  after death.  8.  Prospects  or  outlook;  future  career.
A   groat  man  without  a   past,  if  he  ho  not  an  impossibiUty,  will oortaiiily  have  no  future,  hovrapi,  Among  mu  Books,  Lessing in  first  sor.,  p.  302,  [a.  u.  &   oo.  1886.1
```


## [2026-09-05T14:43:37.180Z] TOOL CALL #49: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T14:43:37.221Z] TOOL RESULT

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


## [2026-09-05T14:43:39.085Z] TOOL CALL #50: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg99.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/99.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-05T14:43:39.170Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r-- 1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T14:44:21.356Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -A4 \"^ Etymology$\" c59111e732bb4698.txt | grep -v \"^\\s*$\" | head -12\ncd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW pistacium ===\"; grep -n -i \"pistaci\" LEW_1910.txt LAT.txt | head -5\necho \"=== KLN 1190 leaf check ===\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"pistachio,  n.\")>0) print \"KLN leaf=\"n}' KLN_1966.txt\necho \"=== IEC/SYN pistachio ===\"; grep -n -i \"pistach\" IEC.txt SYN.txt | head -5"
}
```


### [2026-09-05T14:44:23.212Z] TOOL RESULT

```
140: Etymology
141- [ edit ] 
142-
143- Borrowed from Arabic اِبْتِكَار ( ibtikār ) .
144-
=== LEW pistacium ===
=== KLN 1190 leaf check ===
KLN leaf=636
=== IEC/SYN pistachio ===
```


## [2026-09-05T14:50:39.088Z] TOOL CALL #52: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk99.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 99,\n \"book_page\": 69,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Bistak\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Middle Persian pstk' = pistag 'pistachio nut' (< Old Persian *pistaka-, attested in Elamite pi-iš-tuk-ka₄)\",\n   \"note\": (\"The root box is real and the gloss is right: MacKenzie reads the Pahlavi spelling <pstk'> as pistag 'pistachio nut' \"\n            \"(A Concise Pahlavi Dictionary p. 74), and Laufer reconstructs Middle Persian *pistak from Old Iranian *pistaka \"\n            \"(Sino-Iranica p. 251). The only issue is the transliteration of the root name: Pahlavi book script does not \"\n            \"distinguish p from b, so <pstk'> can be read either way, and Nourai (following Unvala and the older transcription \"\n            \"practice, and probably influenced by the Greek by-form βιστάκιον recorded by Nicander) prints Bistak; Asbaghi \"\n            \"likewise transcribes mp. bistag. The reading accepted today is pistag, guaranteed by Elamite pi-iš-tuk-ka₄ and by \"\n            \"New Persian پسته with p-. Hence 'plausible' rather than 'confirmed' — real word, right language, right meaning, \"\n            \"non-standard reading of the initial consonant. Further back the word is probably Proto-Iranian *pištaka- 'crushed', \"\n            \"from PIE *peys- 'to grind, crush' (Pokorny 796 peis-1), i.e. 'the nut one cracks'.\"),\n   \"note_fa\": (\"خانهٔ ریشه «Bistak» در واقع همان واژهٔ فارسی میانه است که در دبیرهٔ پهلوی <pstk'> نوشته می‌شود؛ مکنزی آن را \"\n               \"pistag «پسته» می‌خواند (فرهنگ کوچک پهلوی، ص ۷۴) و لاوفر در «سینو-ایرانیکا» (ص ۲۵۱) صورت ایرانی باستان *pistaka \"\n               \"و فارسی میانهٔ *pistak را بازسازی می‌کند. چون در خط پهلوی «پ» و «ب» یک نشانه دارند، خواندن bistak نادرست نیست، \"\n               \"ولی خوانش پذیرفتهٔ امروزی pistag است، زیرا صورت ایلامی pi-iš-tuk-ka₄ و «پسته»ی فارسی نو هر دو پ دارند. \"\n               \"دورتر، این واژه احتمالاً از ایرانی آغازین *pištaka- «کوبیده، شکسته» و ریشهٔ هندواروپایی *peys- «کوفتن، ساییدن» است. \"\n               \"نتیجه: ادعای نورایی در اصل درست است، اما آوانویسی آغازهٔ واژه با «ب» با معیار امروزی نمی‌خواند.\"),\n   \"sources\": [\n     \"https://en.wiktionary.org/wiki/pstk%27\",\n     \"https://ahdictionary.com/word/search.html?q=pistachio\",\n     \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA%D9%87\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"UNV:78\", \"status\": \"not_checked\",\n      \"note\": (\"Only the 1917 Heidelberg dissertation of Unvala's 'Der Pahlavi-Text Der König Husrav und sein Knabe' is on disk \"\n               \"(refs/UNV.txt, 47 form-feed leaves, printed pp. ≲46), so p. 78 of the 1963 Paris edition (which carries the fuller \"\n               \"glossary) could not be reached. The corresponding text passage IS in the scan: §51 'Die hyrkanische Pistaziennuß, \"\n               \"wenn man sie auf einem Bräter röstet' and §53 'die frische Pistaziennuß' (UNV.txt lines 608-609), with footnote 51.1 \"\n               \"'Ich nehme … und in §52 gleich np. ‘Pistaziennuß’' — i.e. Unvala does gloss the Pahlavi word as the pistachio nut, \"\n               \"which is what Nourai cites him for.\")}\n   ],\n   \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"p. 74 (leaf 95 of refs/PHD.txt)\", \"stance\": \"supports\",\n      \"note\": \"MacKenzie: \\\"pistag [pstk' | N pista] pistachio nut\\\"; also in the English-Pahlavi index \\\"pistachio nut pistag; ~ tree wan ī gurgānīg\\\" (PHD.txt line 3131). Same word, same gloss, but read with p-.\"},\n     {\"src\": \"SIN\", \"where\": \"pp. 246, 251\", \"stance\": \"supports\",\n      \"note\": \"Laufer, Sino-Iranica: \\\"Persian pista, from Old Iranian *pistaka, Middle Persian *pistak, from which is derived Greek βιστάκιον, φιττάκιον, πιστάκιον or ψιττάκιον, Latin psittacium, and our pistacia or pistachio\\\" (SIN.txt line 726; index s.v. '*pistak 251'). Note that Laufer records the Greek by-form with β-, which is the nearest thing to Nourai's 'Bistak'.\"},\n     {\"src\": \"NYB\", \"where\": \"Glossary (vol. II), grep 'pistak|pistag|Pistazie'\", \"stance\": \"silent\",\n      \"note\": \"Nyberg's Pahlavi glossary has no entry for the pistachio (only nipištak 'written'); the word does not occur in the texts he glosses.\"},\n     {\"src\": \"PLA\", \"where\": \"p. 210 (leaf 225)\", \"stance\": \"partial\",\n      \"note\": \"Asbaghi cites the Middle Persian etymon of Arabic fustuq as 'bistag' — the same b-reading Nourai uses — but for her the immediate source is NP peste, not a Pahlavi root box.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"pesteh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"New Persian پسته pesta/peste continues Middle Persian pistag <pstk'> directly: Pahlavi -ag regularly gives NP -a/-e \"\n                    \"(cf. MP nāmag > NP نامه nāme), so pistag > pista > modern peste. Behind it stand Old Persian *pistaka-, guaranteed by \"\n                    \"the Elamite Persepolis-tablet spelling pi-iš-tuk-ka₄ /pistaka/ 'pistachio nut', and probably Proto-Iranian *pištaka- \"\n                    \"'crushed' (PIE *peys- 'grind, crush'), the tree being native to Sogdiana, Khorasan and Kerman (Laufer, Sino-Iranica 246). \"\n                    \"The figurative sense 'the beloved's (smiling) lips' that Nourai gives is a standard image of classical Persian poetry — \"\n                    \"the half-open shell of the ripe pistachio — and is exactly what the Hāfez line quoted in the box plays on \"\n                    \"(«جان فدای شکرین پستهٔ خاموشش باد»: the 'silent pistachio' is the mouth that will not speak).\"),\n     \"derivation_fa\": (\"«پسته» در فارسی نو دنبالهٔ مستقیم فارسی میانهٔ pistag (نوشتهٔ پهلوی <pstk'>) است؛ پسوند ـag پهلوی در فارسی نو \"\n                       \"به ـه بدل می‌شود (مانند nāmag > نامه)، پس pistag > پسته. پیش از آن ایرانی باستان *pistaka- را داریم که صورت ایلامی \"\n                       \"pi-iš-tuk-ka₄ در گِل‌نبشته‌های تخت‌جمشید گواه آن است، و احتمالاً از ایرانی آغازین *pištaka- «کوبیده» از ریشهٔ \"\n                       \"هندواروپایی *peys- «ساییدن، کوفتن». کاربرد مجازی «پسته» برای لبِ خندانِ معشوق نیز از تصویرهای رایج شعر فارسی است \"\n                       \"(پوستِ نیم‌شکافتهٔ پستهٔ رسیده)، چنان‌که در بیت حافظِ همین خانه «پستهٔ خاموش» یعنی دهانِ فروبستهٔ یار. \"\n                       \"نتیجه: ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA%D9%87\",\n       \"https://en.wiktionary.org/wiki/pstk%27\",\n       \"https://ahdictionary.com/word/search.html?q=pistachio\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"PLA:210\", \"status\": \"supports\",\n        \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p. 210 (leaf 225 of PLA_pages.txt), s.v. fustuq: \\\"fustuq: 'Pistazie' … pers. peste … mp. … bistag … Pistazie pers. > griech. > lat. > frz. pistache\\\" — the Persian word peste is the starting point of her chain, as in Nourai's chart.\"},\n       {\"ref\": \"AHD:998\", \"status\": \"supports\",\n        \"note\": \"AHD s.v. pistachio: \\\"…from Greek pistakē, pistachio tree, of Iranian origin; akin to Middle Persian pistag\\\" (ahdictionary.com/word/search.html?q=pistachio) — the Iranian word is the source, as Nourai draws it.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"vol. 1, Mo'in's footnote 5 s.v. پسته (BQT_v1_pages.txt line 25742, leaf 630)\", \"stance\": \"partial\",\n        \"note\": \"«پسته: بکسر اول و سکون سوم، در تازی فستق از آرامی فستقا (بکسر اول)، چه منشأ آن شام (سوریه) است و به یونانی نقل شد pistakion و از آن به دیگر زبانهای اروپایی داخل شد. در ایتالیایی pistacchio…» — Mo'in has the Persian word but sends the Arabic (and through it the Greek) back to Aramaic, i.e. he does not derive the European words from Persian.\"},\n       {\"src\": \"MON\", \"where\": \"s.v. پسته (MON_part1.txt line 31751)\", \"stance\": \"partial\",\n        \"note\": \"«پسته: [آرا. فستقا] (اِ.) (گیا.) درختی از تیرهٔ سماقی‌ها…» — Mo'in tags the headword as Aramaic فستقا, not as an inherited Iranian word; he has the tree native to Syria/Afghanistan/Khorasan.\"},\n       {\"src\": \"SIN\", \"where\": \"pp. 246-251\", \"stance\": \"supports\",\n        \"note\": \"\\\"The pistachio (Pistacia vera) in particular is indigenous to ancient Sogdiana and Khorasan\\\"; \\\"Persian pista, from Old Iranian *pistaka, Middle Persian *pistak, from which is derived Greek βιστάκιον … πιστάκιον\\\" — Persian is the source, not the borrower.\"},\n       {\"src\": \"PHD\", \"where\": \"p. 74\", \"stance\": \"supports\",\n        \"note\": \"\\\"pistag [pstk' | N pista] pistachio nut\\\" — MacKenzie himself equates the Pahlavi word with New Persian pista.\"},\n       {\"src\": \"HRN\", \"where\": \"grep 'pista|piste' in HRN.txt\", \"stance\": \"silent\",\n        \"note\": \"Horn's Grundriss has no entry for پسته (only the unrelated nipištan 'write' and a passing 'wilde Pistazie (?)' at no. 133); a fruit-name of this kind fell outside his selection.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Greek\", \"words\": \"pistake, pistakion\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Greek πιστάκη pistákē 'pistachio tree' is a loan from an Iranian form of the pistag type, with the diminutive/fruit \"\n                    \"derivative πιστάκιον pistákion 'pistachio nut' (πιστάκη + -ιον). The borrowing is early and its route is documented: \"\n                    \"Theophrastus (Hist. plant. IV.iv.7, late 4th c. BCE), reporting Alexander's scientific staff, describes the nut-bearing \"\n                    \"tree of Bactria, and Nicander of Colophon (Theriaka 890, 3rd c. BCE) already uses βιστάκιον / πιστάκιον of the fruit \"\n                    \"growing in the Choaspes valley in Susiana; Posidonius, Dioscorides, Pliny and Galen then know it from Syria, and \"\n                    \"Vitellius planted the tree in Italy (Pliny XV.22.91). The fluctuating Greek initial (πιστ-, βιστ-, φιττ-, ψιττ-) is exactly \"\n                    \"what a loan from Pahlavi <pstk'> would produce. The NOTE in the box reports Mo'in (MON:2545), who has the Greek word \"\n                    \"borrowed from Arabic; that is chronologically impossible — the Greek word is attested some nine centuries before the \"\n                    \"Arabic one — and no modern authority follows it.\"),\n     \"derivation_fa\": (\"یونانی πιστάκη «درخت پسته» وام‌واژه‌ای است از صورتی ایرانی از گونهٔ pistag، و πιστάκιον «دانهٔ پسته» با پسوند ـion \"\n                       \"از آن ساخته شده است. تاریخ وام‌گیری روشن است: تئوفراستوس (سدهٔ چهارم پیش از میلاد، بر پایهٔ گزارش همراهان اسکندر) \"\n                       \"درخت آن را در بلخ وصف می‌کند و نیکاندروس کولوفونی (سدهٔ سوم پیش از میلاد) صورت‌های βιστάκιον/πιστάκιον را برای \"\n                       \"میوه‌ای می‌آورد که در درّهٔ کرخه در خوزستان می‌روید. نوسان آغازهٔ یونانی (πιστ-، βιστ-، φιττ-، ψιττ-) درست همان چیزی است \"\n                       \"که از وام‌گیری صورتِ پهلوی <pstk'> انتظار می‌رود. یادداشت درون خانه، به نقل از معین، یونانی را وام‌گرفته از عربی می‌داند؛ \"\n                       \"این از نظر تاریخی ناممکن است، زیرا واژهٔ یونانی نزدیک نُه سده پیش از واژهٔ عربی گواهی شده است. \"\n                       \"نتیجه: ادعای نورایی درست است و ادعای معین پذیرفتنی نیست.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%CF%80%CE%B9%CF%83%CF%84%CE%AC%CE%BA%CE%B7\",\n       \"https://en.wiktionary.org/wiki/%CF%80%CE%B9%CF%83%CF%84%CE%AC%CE%BA%CE%B9%CE%BF%CE%BD\",\n       \"https://ahdictionary.com/word/search.html?q=pistachio\",\n       \"https://www.etymonline.com/word/pistachio\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD:998\", \"status\": \"supports\",\n        \"note\": \"AHD s.v. pistachio: \\\"…from Latin pistacium, pistachio nut, from Greek pistakion, from pistakē, pistachio tree, of Iranian origin; akin to Middle Persian pistag.\\\"\"},\n       {\"ref\": \"PLA:210\", \"status\": \"supports\",\n        \"note\": \"Asbaghi p. 210 s.v. fustuq gives the chain \\\"Pistazie pers. > griech. > lat. > frz. pistache\\\" — Persian to Greek, as drawn.\"},\n       {\"ref\": \"SKT:394\", \"status\": \"partial\",\n        \"note\": \"The entry exists but not on p. 394 of the copy on disk: SKT.txt has \\\"Pistachio, Pistacho, the nut of a certain tree. (Span. — L. — Gk. — Pers.) Span. pistacho. — L. pistacium. — Gk. πιστάκιον, a nut of the tree called πιστάκη. — Pers. pistah, the pistachio nut\\\" on printed p. 353/354 of the 1911 corrected impression (line 14076; page marker 353 a few lines above), with a cross-reference list entry \\\"Spanish from Latin from Greek from Persian: pistachio (pistacho)\\\" on p. 620. Content supports the Greek < Persian arrow; only the page number of Nourai's reprint differs.\"},\n       {\"ref\": \"KLN:1190\", \"status\": \"supports\",\n        \"note\": \"Klein 1966 p. 1190 (leaf 636, page marker '1190' on the same leaf): \\\"pistachio, n. — It. pistacchio (whence also F. pistache, Sp. pistacho), fr. L. pistacium, fr. Gk. πιστάκιον, 'pistachio nut', fr. πιστάκη, 'pistachio tree', fr. Pers. pistah, 'pistachio nut'. Cp. fustic.\\\"\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SIN\", \"where\": \"pp. 246, 251\", \"stance\": \"supports\",\n        \"note\": \"\\\"Nicandrus of Colophon (third century B.C.), who calls the fruit βιστάκιον or πιστάκιον, a word derived from an Iranian language … says that it grows in the valley of the Choaspes in Susiana\\\" — dates the Greek word to the 3rd c. BCE and makes it Iranian.\"},\n       {\"src\": \"LKT\", \"where\": \"nos. at LKT.txt lines 1554, 3802\", \"stance\": \"partial\",\n        \"note\": \"Lokotsch: \\\"'Pistazie, Pistazienbaum' [aus pers. fistik, woraus auch gr. πιστάκιον]\\\" and \\\"ar. fistik, fustak 'Pistazie, Pistacia vera'; hieraus … it. pistacchio, frz. pistache, sp. pistacho\\\" — agrees that Greek took the word from Persian, but routes the Romance forms through Arabic rather than through Latin.\"},\n       {\"src\": \"KLN\", \"where\": \"p. 1190\", \"stance\": \"supports\",\n        \"note\": \"\\\"fr. Gk. πιστάκιον … fr. πιστάκη … fr. Pers. pistah\\\".\"},\n       {\"src\": \"MON\", \"where\": \"s.v. پسته; BQT vol.1 fn. 5 s.v. پسته\", \"stance\": \"contradicts\",\n        \"note\": \"Mo'in: «در تازی فستق از آرامی فستقا … و به یونانی نقل شد pistakion» — Greek from the Semitic word, the view reported in the chart's NOTE and rejected here on chronological grounds.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Latin\", \"words\": \"pistacia, pistacium\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Latin borrowed both Greek forms in the 1st c. CE, when the tree itself reached Italy: pistacium n. 'pistachio nut' \"\n                    \"< Greek πιστάκιον, and pistacia f. 'pistachio tree' < Greek πιστάκη. Pliny (NH XV.22.91) records that Vitellius brought \"\n                    \"the tree to Italy and Flaccus Pompeius to Spain in the reign of Tiberius, which fixes the date of the loan; the Greek \"\n                    \"-ki- is simply rendered -ci- and the neuter -ον becomes -um. Medieval Latin pistacia is the form from which Old French \"\n                    \"pistace and Middle English pistace/pystace (mid-15c.) come.\"),\n     \"derivation_fa\": (\"لاتینی هر دو صورت یونانی را در سدهٔ یکم میلادی وام گرفت، درست هنگامی که خود درخت به ایتالیا رسید: \"\n                       \"pistacium «دانهٔ پسته» از πιστάκιον و pistacia «درخت پسته» از πιστάκη. پلینیوس (تاریخ طبیعی، ۱۵٫۲۲) می‌گوید \"\n                       \"ویتلیوس درخت را به ایتالیا و فلاکوس پومپیوس آن را به اسپانیا برد؛ همین تاریخِ وام‌گیری را روشن می‌کند. \"\n                       \"در آوانویسی، ـki ـ یونانی به ـci ـ و پایانهٔ خنثای ـον به ـum بدل شده است. \"\n                       \"نتیجه: ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/pistacium\",\n       \"https://ahdictionary.com/word/search.html?q=pistachio\",\n       \"https://www.etymonline.com/word/pistachio\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD:998\", \"status\": \"supports\",\n        \"note\": \"AHD: \\\"from Italian pistacchio, from Latin pistacium, pistachio nut, from Greek pistakion\\\" — the Latin link is exactly as drawn.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 1190\", \"stance\": \"supports\",\n        \"note\": \"\\\"It. pistacchio … fr. L. pistacium, fr. Gk. πιστάκιον\\\".\"},\n       {\"src\": \"SKT\", \"where\": \"p. 353/354\", \"stance\": \"supports\",\n        \"note\": \"\\\"Span. pistacho. — L. pistacium. — Gk. πιστάκιον\\\".\"},\n       {\"src\": \"SIN\", \"where\": \"p. 251\", \"stance\": \"partial\",\n        \"note\": \"Laufer cites the Latin form as \\\"psittacium\\\" beside \\\"pistacia\\\" — the same word with the ψιττ- variant of the Greek; supports the Greek > Latin step but with a different Latin spelling.\"},\n       {\"src\": \"LEW\", \"where\": \"grep 'pistaci' in LEW_1910.txt / LAT.txt\", \"stance\": \"silent\",\n        \"note\": \"Neither Walde 1910 nor Ernout-Meillet (as digitised here) has an article on pistacium — it is a transparent Greek loanword and gets no entry.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Italian\", \"words\": \"pistacchio\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Italian pistacchio continues Latin pistacium with the regular Italian outcome of Latin -cium: -ci- palatalises and the \"\n                    \"yod geminates to -cchi- /kkj/ (cf. L. bracchium > It. braccio, but with the learned/half-learned treatment here giving \"\n                    \"-cchio, as in L. specul(um) > It. specchio). From Italian the word spread again in the 16th c.: French pistache, \"\n                    \"Spanish pistacho and, through Italian directly, English pistachio.\"),\n     \"derivation_fa\": (\"ایتالیایی pistacchio دنبالهٔ لاتینی pistacium است؛ خوشهٔ ـcium لاتینی در ایتالیایی به ـcchio /kkjo/ بدل می‌شود \"\n                       \"(مانند specul(um) > specchio). از ایتالیایی، واژه در سدهٔ شانزدهم دوباره پخش شد: فرانسوی pistache، \"\n                       \"اسپانیایی pistacho و انگلیسی pistachio. نتیجه: ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/pistachio\",\n       \"https://ahdictionary.com/word/search.html?q=pistachio\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"KLN:1190\", \"status\": \"supports\",\n        \"note\": \"Klein p. 1190: \\\"pistachio, n. — It. pistacchio (whence also F. pistache, Sp. pistacho), fr. L. pistacium\\\" — Latin > Italian, and Italian as the radiating centre, precisely as drawn.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"s.v. pistachio (online appendix edition of the same dictionary)\", \"stance\": \"supports\",\n        \"note\": \"\\\"Ultimately (partly via Middle French pistache) from Italian pistacchio, from Latin pistacium\\\".\"},\n       {\"src\": \"LKT\", \"where\": \"LKT.txt line 3802\", \"stance\": \"partial\",\n        \"note\": \"Lokotsch lists \\\"it. pistacchio, frz. pistache, sp. pistacho\\\" but derives them from the Arabic/Turkish form rather than from Latin.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"pistachio\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"English pistachio is first recorded in the 1590s in the sense 'nut of the pistachio tree', taken straight from Italian \"\n                    \"pistacchio (partly through Middle French pistache); the Italian -cchio was anglicised as -chio /ʃoʊ/. An earlier and \"\n                    \"separate borrowing had already given Middle English pistace, pystace (mid-15c.) from Old French pistace and Medieval \"\n                    \"Latin pistacia — a doublet that died out in favour of the Italian form. The colour sense 'pistachio green' is 19th c.\"),\n     \"derivation_fa\": (\"واژهٔ انگلیسی pistachio نخستین بار در دههٔ ۱۵۹۰ به معنی «دانهٔ پسته» ثبت شده و یکسره از ایتالیایی pistacchio \"\n                       \"(تا اندازه‌ای از راه فرانسوی میانه pistache) گرفته شده است؛ ـcchio ایتالیایی در انگلیسی ـchio شده است. \"\n                       \"پیش از آن، وام‌گیری جداگانه‌ای در انگلیسی میانه صورتِ pistace/pystace را از فرانسوی کهن و لاتینی میانه به دست داده بود \"\n                       \"که دوگانهٔ (doublet) همین واژه است و بعدها از میان رفت. نتیجه: ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/pistachio\",\n       \"https://ahdictionary.com/word/search.html?q=pistachio\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD:998\", \"status\": \"supports\",\n        \"note\": \"AHD s.v. pistachio: \\\"[Ultimately (partly via Middle French pistache) from Italian pistacchio, from Latin pistacium…]\\\" — the Italian > English step Nourai draws.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 1190\", \"stance\": \"supports\",\n        \"note\": \"\\\"pistachio, n. — It. pistacchio…\\\" (Klein takes English straight from Italian).\"},\n       {\"src\": \"SKT\", \"where\": \"p. 353/354\", \"stance\": \"contradicts\",\n        \"note\": \"Skeat routes the English word through Spanish: \\\"Pistachio, Pistacho, the nut of a certain tree. (Span. — L. — Gk. — Pers.) Span. pistacho\\\" — a minority view; the 1590s date and the -chio spelling favour Italian.\"},\n       {\"src\": \"FSD\", \"where\": \"vol. 3 s.v. pistachio\", \"stance\": \"silent\",\n        \"note\": \"Funk & Wagnalls' pistachio article was not recoverable from the OCR of the volume on disk (only the fustic/fustet region of vol. 2 is legible); no statement either way.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Arabic\", \"words\": \"fustug, fostoq\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"The Arabic word فُسْتُق fustuq / fustaq 'pistachio' is real and its ultimate source is Iranian, but the parent drawn here \"\n                    \"— Greek — is not the one modern scholarship accepts. Wiktionary, with references, has it \\\"from Middle Persian pstk' \"\n                    \"(pistag), if not via Aramaic (Jewish Babylonian Aramaic פיסתקא pistəqā, Classical Syriac ܦܷܣܬܩܐ pestəqā)\\\"; Fraenkel, \"\n                    \"Die aramäischen Fremdwörter im Arabischen pp. 143-144, says the word \\\"kann direct aus dem Persischen, wie Ǧawālīqī \"\n                    \"meint, oder auch mittelbar durch das Aramäische ppHDS/ܦܣܬܩܐ in's Arabische gedrungen sein\\\"; al-Unaysī's Tafsīr \"\n                    \"al-alfāẓ al-dākhila likewise: «فستق – ارامي (فستقا)». Nourai's own citation here, PLA:210, also contradicts the Greek \"\n                    \"parent: Asbaghi derives fustuq from Persian peste / MP bistag and lets the Greek word go off on its own branch. \"\n                    \"Phonetically the borrowing is straightforward: Arabic has no /p/, so Iranian p- is substituted by f- (cf. Pers. pīl > \"\n                    \"Ar. fīl), and the Iranian a-vowel is fitted to the fuʿlul pattern fustuq. What is true is that AHD:535 (which Nourai \"\n                    \"cites at the French node) does route Arabic fustuq through Greek pistakē — an older view still printed in that \"\n                    \"dictionary — so the chart is following a real source, just not the prevailing one. The box's NOTE, reporting Mo'in's \"\n                    \"Aramaic mediation, is on this point closer to current opinion than the arrow above it.\"),\n     \"derivation_fa\": (\"واژهٔ عربی «فُستُق» راست است و سرچشمهٔ آن نیز ایرانی است، اما پدرِ ترسیم‌شده در نمودار — یونانی — با دیدگاه امروزی نمی‌خواند. \"\n                       \"ویکی‌واژه آن را «از فارسی میانه pistag، اگر نه از راه آرامی (فیستقا در آرامی بابلی یهودی، ܦܷܣܬܩܐ در سریانی)» می‌داند؛ \"\n                       \"فرنکل در «وام‌واژه‌های آرامی در عربی» (ص ۱۴۳-۱۴۴) می‌نویسد این واژه «یا مستقیم از فارسی — چنان‌که جوالیقی می‌گوید — یا \"\n                       \"با میانجی آرامی به عربی رسیده است»؛ طوبیا العنیسی نیز می‌نویسد «فستق – ارامي فستقا». حتی مرجعی که خودِ نورایی آورده \"\n                       \"(اصبغی، ص ۲۱۰) فستق را از «peste» فارسی و «bistag» پهلوی می‌گیرد، نه از یونانی. از نظر آوایی، چون در عربی «پ» نیست، \"\n                       \"پ ایرانی به ف بدل شده (مانند پیل > فیل) و واژه در وزن فُعلُل نشسته است. \"\n                       \"نتیجه: پژوهش امروزی این پیکان را رد می‌کند و می‌گوید فستق یکراست (یا از راه آرامی) از فارسی گرفته شده است.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%D9%81%D8%B3%D8%AA%D9%82\",\n       \"https://ahdictionary.com/word/search.html?q=fustic\",\n       \"https://en.wiktionary.org/wiki/pstk%27\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"PLA:210\", \"status\": \"contradicts\",\n        \"note\": \"Asbaghi p. 210 (leaf 225 of PLA_pages.txt): \\\"fustug: 'Pistazie' … pers. peste … mp. … bistag … aram. …\\\" — she makes Arabic fustuq a loan from Persian (possibly via Aramaic), not from Greek; the Greek/Latin/French forms are listed as a parallel line of descent from Persian, not as its source.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AFA\", \"where\": \"Fraenkel pp. 143-144 (AFA.txt lines 5217-5222)\", \"stance\": \"contradicts\",\n        \"note\": \"\\\"فستق 'Pistazie' ist als Fremdwort schon von den Arabern (Muʿarrab 108) erkannt; es kann direct aus dem Persischen, wie Ǧawālīqī meint, oder auch mittelbar durch das Aramäische … in's Arabische gedrungen sein\\\" — Persian or Aramaic, never Greek.\"},\n       {\"src\": \"TAD\", \"where\": \"al-Unaysi, TAD_pages.txt line 1991\", \"stance\": \"contradicts\",\n        \"note\": \"«فستق - ارامي «فستقا» لان منشأ هذه الشجرة الشام أي سوريا فنقل الى العربية» — Aramaic, the tree being (in his view) Syrian.\"},\n       {\"src\": \"AFM\", \"where\": \"Addi Shir, AFM_pages.txt (headword فستق, index line 5796; Syriac ܦܣܬܩܐ cited at line 3051)\", \"stance\": \"partial\",\n        \"note\": \"Addi Shir's Kitāb al-alfāẓ al-fārisiyya al-muʿarraba lists فستق among the Persian words Arabicised, citing the Syriac ܦܣܬܩܐ and Kurdish/Armenian parallels — Persian source, Aramaic mediation, no Greek.\"},\n       {\"src\": \"LKT\", \"where\": \"LKT.txt line 3802\", \"stance\": \"partial\",\n        \"note\": \"Lokotsch: \\\"tk. fystyk, ar. fistik, fustak 'Pistazie, Pistacia vera'\\\" and elsewhere \\\"[aus pers. fistik, woraus auch gr. πιστάκιον]\\\" — Arabic and Greek are for him two independent borrowings from Persian, i.e. sisters, not parent and child.\"},\n       {\"src\": \"MON\", \"where\": \"BQT vol.1 Mo'in fn. 5 s.v. پسته; MON s.v. پسته\", \"stance\": \"partial\",\n        \"note\": \"«در تازی فستق از آرامی فستقا» — Mo'in derives Arabic fustuq from Aramaic, i.e. the chart's own NOTE, and (unlike Nourai) makes Greek the daughter of the Semitic word rather than its parent.\"},\n       {\"src\": \"FVQ\", \"where\": \"grep 'fustuq|pistachio' in FVQ_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Jeffery's Foreign Vocabulary of the Qurʾān has no entry — فستق does not occur in the Qurʾān.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Persian\", \"words\": \"fostoğ\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"فُستُق fostoq in Persian is a re-borrowing: the native word پسته pesta went into Arabic as fustuq (with f- for p-, since \"\n                    \"Arabic lacks /p/), and the Arabicised form came back into literary Persian as a learned Arabism, chiefly in the \"\n                    \"derived adjective فستقی fostoqi 'pistachio-green', which is how it is used in the couplet quoted in the box \"\n                    \"(«خط سبز فستقی» — the beloved's downy green cheek-line). This is a textbook Persian > Arabic > Persian round trip, of \"\n                    \"the same type as پیل > فیل > فیل or دیبا > دیباج > دیباج; Mo'in's own footnote to Borhān-e Qāṭeʿ makes the identity \"\n                    \"explicit — «پسته … در تازی فستق».\"),\n     \"derivation_fa\": (\"«فُستُق» در فارسی وام‌واژه‌ای بازگشتی (معرّبِ بازگردانده) است: واژهٔ بومی «پسته» به عربی رفت و چون در عربی «پ» نیست \"\n                       \"به صورت «فستق» درآمد، و همین صورتِ معرّب دوباره — بیشتر در صفتِ «فُستُقی» به معنی «سبزِ پسته‌ای» — وارد فارسی ادبی شد؛ \"\n                       \"چنان‌که در بیت همین خانه «خط سبز فُستُقی». این همان روند فارسی › عربی › فارسی است، از گونهٔ پیل › فیل و دیبا › دیباج. \"\n                       \"حاشیهٔ معین بر برهان قاطع نیز همین‌همانی را روشن می‌گوید: «پسته … در تازی فستق». \"\n                       \"نتیجه: ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%D9%81%D8%B3%D8%AA%D9%82\",\n       \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA%D9%87\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"MON:2545\", \"status\": \"supports\",\n        \"note\": \"Mo'in's article on پسته and his footnote 5 to Borhān-e Qāṭeʿ (BQT_v1_pages.txt line 25742) give «در تازی فستق از آرامی فستقا» and tag the headword «[آرا. فستقا]» — the Arabic form فستق is identified with the Persian word, which is what the arrow Arabic > Persian fostoq needs. (The six-volume Mo'in itself is not digitised; checked in the 2-vol. Adena condensation, MON_part1.txt line 31751, and in Mo'in's Borhān footnotes.)\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"vol. 1, Mo'in fn. 5 s.v. پسته\", \"stance\": \"supports\",\n        \"note\": \"«پسته: بکسر اول و سکون سوم، در تازی فستق از آرامی فستقا …» — the Arabic doublet of the Persian word, as the node requires.\"},\n       {\"src\": \"PLA\", \"where\": \"p. 210\", \"stance\": \"supports\",\n        \"note\": \"Asbaghi lists the derivatives \\\"fustuqa: nom. un. v. fustuq 'eine Pistazie'\\\" and \\\"fustuqī: 'pistaziengrün'\\\" — the very adjective فستقی used in the Persian couplet in the box.\"},\n       {\"src\": \"MON\", \"where\": \"MON_part1.txt line 31751\", \"stance\": \"supports\",\n        \"note\": \"«پسته: [آرا. فستقا]» — Mo'in explicitly equates the Persian headword with the Semitic فستقا/فستق.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"French\", \"words\": \"\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"extraction\",\n     \"book_prints\": \"(empty box: the French node on p. 69 has only the header 'French  AHD:535' and no word line)\",\n     \"correct_form\": \"(no word) — the French form intended is fustoc (Old French) / fustet, not 'fustic, fistic'\",\n     \"derivation\": (\"On the printed page the French box is a bare header — 'French [book] AHD:535' — with no word row at all; the words \"\n                    \"'fustic, fistic' belong to the English box to its right. The extraction has copied the English forms into the French \"\n                    \"node, so the JSON says something the book does not. The pass-through step itself is sound: the Romance form is Old \"\n                    \"French fustoc (also fustet, from Provençal fustet), a borrowing of Arabic fustuq that reached the West through the \"\n                    \"Andalusian and Levantine dye trade — Wiktionary: English fustic \\\"from Middle English fustik, from Middle French \"\n                    \"fustec, variant of fustet\\\"; AHD s.v. fustic: \\\"Middle English fustik, from Old French fustoc, from Arabic fustuq\\\". \"\n                    \"The name was transferred from the pistachio/sumac wood (Cotinus coggygria, 'young fustic') to the Central American \"\n                    \"dyewood Maclura/Chlorophora tinctoria ('old fustic') after 1500.\"),\n     \"derivation_fa\": (\"در صفحهٔ چاپی، خانهٔ «French» تنها یک سرصفحه است و هیچ واژه‌ای در آن نوشته نشده؛ «fustic, fistic» متعلق به خانهٔ \"\n                       \"انگلیسی کنار آن است. بنابراین این خطای خوانشِ اسکن است، نه خطای کتاب. خودِ حلقهٔ فرانسوی درست است: صورت \"\n                       \"فرانسوی کهن fustoc (و fustet از پرووانسی) وام‌واژه‌ای از «فُستُق» عربی است که از راه بازرگانی رنگ در اندلس و شام \"\n                       \"به اروپا رسید؛ ویکی‌واژه: fustic انگلیسی «از انگلیسی میانهٔ fustik، از فرانسوی میانهٔ fustec، گونهٔ fustet»، و \"\n                       \"فرهنگ AHD: «از فرانسوی کهن fustoc، از عربی فستق». سپس این نام از چوب سماقِ ونیزی به چوب رنگرزی امریکای مرکزی \"\n                       \"منتقل شده است. نتیجه: خطای خوانش اسکن؛ داده باید اصلاح شود.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/fustic\",\n       \"https://ahdictionary.com/word/search.html?q=fustic\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD:535\", \"status\": \"supports\",\n        \"note\": \"AHD s.v. fustic: \\\"[Middle English fustik, from Old French fustoc, from Arabic fustuq, from Greek pistakē, pistachio; see PISTACHIO.]\\\" — the (Old) French step Nourai draws, and also the source of his Arabic < Greek arrow at node #6.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 632 s.v. fustic (KLN_1966.txt line 15603)\", \"stance\": \"contradicts\",\n        \"note\": \"\\\"fustic, n., the wood of a Mexican tree (Chlorophora tinctoria) and the yellow dye it yields. — Sp. fustoc, fr. Arab. fustuq, fr. Pers. pistah. See pistachio.\\\" — Klein makes the intermediary Spanish, not French, and takes the Arabic word straight from Persian.\"},\n       {\"src\": \"FSD\", \"where\": \"vol. 2 s.v. fustic (FSD_vol2.txt line 28447)\", \"stance\": \"partial\",\n        \"note\": \"\\\"[< F. fustoc, < Sp. fustoc, < …]\\\" — French, but itself from Spanish; and s.v. fustet: \\\"fus'tet … 1. The Venetian sumac or smoke-tree (Cotinus cotinus); also, its wood. 2. Young fustic.\\\"\"},\n       {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1 s.v. fustic (WEB_vol1.txt line ~79177)\", \"stance\": \"supports\",\n        \"note\": \"\\\"fus'tic, n. [Fr. fustoc; Sp. fustoc, …]\\\" — French fustoc named first, as in AHD; and \\\"fus'tet, n. [Fr. fustet; LL. fustetus…]\\\".\"},\n       {\"src\": \"DEV\", \"where\": \"grep 'fustet|fustoc' in DEV.txt / PHN.txt\", \"stance\": \"silent\",\n        \"note\": \"Neither Devic nor Pihan has an article on fustoc/fustet in the OCR on disk; Devic mentions only the Spanish alfostigo < al-fostoq (DEV.txt line 249).\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"fustic, fistic\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"English fustic 'a yellow dyewood and the dye from it' is attested from the 15th c. as Middle English fustik, borrowed \"\n                    \"from Old/Middle French fustoc, fustec (variant of fustet), itself from Arabic fustuq — the pistachio-tree name applied \"\n                    \"first to the related Venetian sumac Cotinus coggygria ('young fustic') and after the discoveries to the tropical \"\n                    \"American Maclura tinctoria ('old fustic'), whose heartwood gave the standard yellow of European dyeing until aniline \"\n                    \"dyes. The second form, fistic, is a different animal: it is the obsolete English word for the pistachio nut itself \"\n                    \"('fisticke nuts' in 16th-17th c. English), taken through Italian fistico/Spanish alfóstigo from the same Arabic \"\n                    \"fustuq — a genuine English word from the same Arabic etymon, but not a spelling variant of the dyewood term, and the \"\n                    \"modern English adjective fistic means only 'pugilistic'. The node is therefore right about the route and about \"\n                    \"fustic, but conflates two distinct English words.\"),\n     \"derivation_fa\": (\"انگلیسی fustic «چوب رنگرزی زرد و رنگِ آن» از سدهٔ پانزدهم به صورت fustik در انگلیسی میانه گواهی شده و از \"\n                       \"fustoc/fustec فرانسوی، و آن از «فُستُق» عربی گرفته شده است: نام درخت پسته نخست به سماق ونیزی و سپس، پس از \"\n                       \"کشف امریکا، به چوب رنگرزی امریکایی داده شد. اما صورت دوم، fistic، واژهٔ دیگری است: نام کهن و منسوخِ خودِ «پسته» \"\n                       \"در انگلیسی («fisticke nuts» در سده‌های شانزدهم و هفدهم) که از راه ایتالیایی fistico و اسپانیایی alfóstigo از همان \"\n                       \"«فستق» عربی آمده است؛ در انگلیسی امروز fistic تنها به معنی «مشت‌زنی» به کار می‌رود. \"\n                       \"نتیجه: مسیر درست است، ولی دو واژهٔ جدا در یک خانه با هم آمیخته شده‌اند؛ با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/fustic\",\n       \"https://ahdictionary.com/word/search.html?q=fustic\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD:535\", \"status\": \"supports\",\n        \"note\": \"AHD s.v. fustic: \\\"[Middle English fustik, from Old French fustoc, from Arabic fustuq, from Greek pistakē, pistachio; see PISTACHIO.]\\\" — French > English, as drawn. AHD gives no variant 'fistic'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 632 s.v. fustic\", \"stance\": \"partial\",\n        \"note\": \"\\\"fustic, n., the wood of a Mexican tree (Chlorophora tinctoria) and the yellow dye it yields. — Sp. fustoc, fr. Arab. fustuq, fr. Pers. pistah. See pistachio.\\\" — same Arabic etymon and the same botanical sense, but via Spanish; no 'fistic'.\"},\n       {\"src\": \"FSD\", \"where\": \"vol. 2 s.v. fustic, fustet, fistic (FSD_vol2.txt lines 28437, 28447, 21124)\", \"stance\": \"contradicts\",\n        \"note\": \"Funk & Wagnalls has \\\"fustic … yellowwood; old fustic. [< F. fustoc, < Sp. fustoc …]\\\", variants \\\"fus'tiket; fus'toct\\\", \\\"young f., the wood of Cotinus cotinus\\\" — and a quite separate entry \\\"fist'ic, a. Pertaining to the fists, especially when used in boxing\\\". 'Fistic' is not a variant of fustic in the dictionaries.\"},\n       {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt lines 73853, ~79177\", \"stance\": \"contradicts\",\n        \"note\": \"\\\"fust'ic, n. [Fr. fustoc; Sp. fustoc, fustie…]\\\" beside \\\"fist'ic, a. having to do with boxing; … pugilistic\\\" — the same split as in Funk & Wagnalls.\"},\n       {\"src\": \"LKT\", \"where\": \"LKT.txt line 1554\", \"stance\": \"partial\",\n        \"note\": \"Lokotsch groups the Romance reflexes \\\"rum. fistic, sp. alföstigo, alföcigo, alfönsigo, pg. alfostico\\\" under the Arabic/Persian word — the fistic-type form is Romanian/Turkish, not English.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"B.k.r\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Arabic root ب-ك-ر b-k-r, verb بَكَرَ bakara 'to rise/come early, do a thing early' (Proto-Semitic *bkr 'first-born, early')\",\n   \"note\": (\"The root is real, the language label is right and the gloss is right. Klein — the reference Nourai cites — states it in the \"\n            \"same words at p. 44: the Arabic words come \\\"from the stem of the verb bákara, 'he rose early, did something early'\\\", and he \"\n            \"ties in Hebrew bəkhōr 'first-born', bikkūrīm 'first fruits' and Ethiopic bakur 'first-born', i.e. a common Semitic root whose \"\n            \"core sense is 'be first / be early'. Wiktionary's Arabic entry بكر gives بَكَرَ bakara 'to be early, to come early, to get up \"\n            \"early' and بِكْر bikr 'firstborn; virgin', comparing Hebrew בְּכוֹר bəḵōr. Nothing in the box needs correction.\"),\n   \"note_fa\": (\"ریشهٔ عربی «ب‌-ک‌-ر» و معنی «بامداد برخاستن، زود کاری کردن» هر دو درست است. کلاین (ص ۴۴) — همان مرجعی که نورایی \"\n               \"آورده — می‌نویسد این واژه‌ها «از ستاکِ فعلِ بَکَرَ، یعنی زود برخاست و کاری را زود انجام داد» است و آن را با عبری bəkhōr \"\n               \"«نخست‌زاد»، bikkūrīm «نوبر» و حبشی bakur «نخست‌زاد» می‌سنجد؛ یعنی ریشه‌ای سامی با هستهٔ معنایی «نخست‌بودن، زودبودن». \"\n               \"ویکی‌واژه نیز بَکَرَ «زود آمدن، پگاه برخاستن» و بِکْر «نخست‌زاد؛ دوشیزه» را می‌آورد. نتیجه: ادعای نورایی درست است.\"),\n   \"sources\": [\n     \"https://en.wiktionary.org/wiki/%D8%A8%D9%83%D8%B1\",\n     \"https://ahdictionary.com/word/search.html?q=albacore\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"KLN:44\", \"status\": \"supports\",\n      \"note\": \"Klein 1966 p. 44 (page marker '44' immediately after the entry, KLN_1966.txt line 2099), s.v. albacore: \\\"…rel. to bikr, 'virgin, woman having first child', from the stem of the verb bákara, 'he rose early, did something early', and to Heb. bekhōr, 'first born'…\\\" — Nourai's root box is a direct paraphrase of this sentence.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"AHD\", \"where\": \"s.v. albacore, Appendix of Semitic roots s.v. bkr\", \"stance\": \"supports\",\n      \"note\": \"\\\"[Portuguese albacor, from Arabic al-bakūra: al-, the + bakūra, albacore; see bkr in the Appendix of Semitic roots.]\\\" — AHD sets up exactly this Semitic root.\"},\n     {\"src\": \"KLN\", \"where\": \"p. 44\", \"stance\": \"supports\",\n      \"note\": \"See ref_check; Klein also lists Heb. bikkūrīm 'first fruits', bikhrāh 'young camel', Ethiop. bakur 'first born'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Arabic\", \"words\": \"bîkr; al-bakrah\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Both words are regular nominal formations on b-k-r. بِكْر bikr (Nourai writes bîkr; the vowel is short i) is the \"\n                    \"fiʿl-pattern noun/adjective 'first-born, first of its kind', hence 'virgin, untouched, fresh, new' — the semantic step \"\n                    \"'first' > 'not yet used' being the same one seen in Hebrew bikkūrīm 'first fruits'. اَلْبَكْرَة al-bakrah is the \"\n                    \"faʿla-pattern singulative of the collective bakr 'young camels', so 'the young she-camel'; Klein spells out the \"\n                    \"derivation: \\\"the collective noun bakr, 'young camels', whence bákrah, 'young she-camel', rel. to bikr\\\". Both are \"\n                    \"denominal to the verb bakara 'to be early', a young animal being one that has come 'early'.\"),\n     \"derivation_fa\": (\"هر دو واژه ساخت‌های قاعده‌مندِ ریشهٔ ب‌-ک‌-ر هستند. «بِکْر» (که نورایی bîkr می‌نویسد؛ مصوت کوتاه است) بر وزن فِعْل \"\n                       \"به معنی «نخستین، نخست‌زاد» و از همین‌جا «دست‌ناخورده، تازه، دوشیزه»؛ همان تحول معنایی «نخست» › «به‌کارنرفته» که در \"\n                       \"عبری bikkūrīm «نوبر» هم دیده می‌شود. «البَکْرَة» بر وزن فَعْلَة، مفردِ اسمِ جمعِ «بَکْر» (شترانِ جوان) است، یعنی «شترِ \"\n                       \"مادهٔ جوان»؛ کلاین همین را می‌گوید: «اسم جمع bakr «شتران جوان» و از آن bakrah «شتر مادهٔ جوان»، هم‌ریشه با bikr». \"\n                       \"هر دو از فعلِ بَکَرَ «زود آمدن» گرفته شده‌اند، چون جانورِ جوان همان است که «زود» آمده است. نتیجه: ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%D8%A8%D9%83%D8%B1\",\n       \"https://ahdictionary.com/word/search.html?q=albacore\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"KLN:44\", \"status\": \"supports\",\n        \"note\": \"Klein p. 44: \\\"fr. al-, 'the', and the collective noun bakr, 'young camels', whence bákrah, 'young she-camel', rel. to bikr, 'virgin, woman having first child', from the stem of the verb bákara\\\" — both of Nourai's words, both glosses.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 44\", \"stance\": \"supports\", \"note\": \"As quoted; Klein is the source Nourai paraphrases.\"},\n       {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān\", \"stance\": \"silent\",\n        \"note\": \"No entry: bikr and its family are native Arabic, so Jeffery (who treats only foreign words) has nothing — itself a small confirmation that the root is Semitic and not a loan.\"},\n       {\"src\": \"AHD\", \"where\": \"Appendix of Semitic roots s.v. bkr (via s.v. albacore)\", \"stance\": \"supports\",\n        \"note\": \"\\\"from Arabic al-bakūra: al-, the + bakūra, albacore; see bkr in the Appendix of Semitic roots\\\" — same root, with the by-form bakūra 'young camels / early fruits'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"bekr; ebtekâr\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Both are ordinary Arabic loans in Persian, of the learned written kind that entered from the 9th-10th c. onwards. \"\n                    \"بکر bekr is Arabic بِكْر bikr taken over unchanged in the consonants (Persian pronounces the short i as e), used in \"\n                    \"Persian for 'virgin' and, in the transferred senses Nourai lists, 'fresh, new, untrodden' — فکر بکر 'an idea nobody \"\n                    \"has had before', موضوع بکر 'a subject not yet treated'; the noun بکارت bekârat 'virginity' shown in brackets is the \"\n                    \"Arabic maṣdar bakāra. ابتکار ebtekâr is the Arabic form-VIII verbal noun ibtikār of ibtakara 'to do a thing first, to \"\n                    \"be the first at something' — the same root with the reflexive infix -t-, so literally 'taking-the-first(-fruits)', \"\n                    \"whence Persian 'innovation, originality, initiative', and the participle مبتكر mobtaker 'innovator'. Mo'in's own \"\n                    \"article preserves the older, literal sense beside the modern one: «ابتکار … در بامداد رفتن، پگاه برخاستن؛ نو آوردن، \"\n                    \"امر بکر و بی‌سابقه پدید کردن».\"),\n     \"derivation_fa\": (\"هر دو واژه وام‌واژه‌های عربی‌اند از گونهٔ کتابیِ رایج از سدهٔ سوم و چهارم هجری به بعد. «بکر» همان بِكْر عربی است \"\n                       \"(مصوت کوتاهِ i در فارسی e تلفظ می‌شود) به معنی «دوشیزه» و در معنی‌های گسترش‌یافته «تازه، نو، دست‌نخورده»: «فکر بکر»، \"\n                       \"«موضوع بکر»؛ «بکارت» داخل کمانک نیز مصدرِ عربیِ بَکارَة است. «ابتکار» مصدرِ باب افتعال از همان ریشه است \"\n                       \"(ابتکر «نخستین کسی بود که کاری کرد»)، با میانوندِ ـت ـ بازتابی، پس تحت‌اللفظ «نوبر برگرفتن» و از این‌جا «نوآوری، \"\n                       \"ابتکار عمل»، و اسم فاعلِ آن «مبتکر». معین در فرهنگ خود هر دو معنی کهن و نو را نگاه داشته است: «ابتکار … در بامداد \"\n                       \"رفتن، پگاه برخاستن؛ نو آوردن، امر بکر و بی‌سابقه پدید کردن». نتیجه: ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%AA%DA%A9%D8%A7%D8%B1\",\n       \"https://en.wiktionary.org/wiki/%D8%A8%D9%83%D8%B1\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"FVA:51\", \"status\": \"not_checked\",\n        \"note\": \"S.M. Nahvi, Farhang-e vāžehā-ye ʿarabi dar fārsi (1368/1989) has no digital copy on any permitted platform — refs_online.json records a re-search in 2026-09 that again found only library catalogue records (OpenLibrary OL2012991M). Page 51 could not be consulted.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"s.v. بکر (MON_part1.txt line 24527) and s.v. ابتکار (line 5972)\", \"stance\": \"supports\",\n        \"note\": \"«بکر: [ع.] (ص.) دختر؛ دوشیزه، تازه، دست ناخورده، نو آیین …» and «ابتکار: [ع.] (مص‌ل.) در بامداد رفتن، پگاه برخاستن. (مص‌م.) نو آوردن، امر بکر و بی‌سابقه پدید کردن. (اسم مص.) نو آوردگی، اختراع: قوّهٔ ابتکار» — Mo'in tags both as Arabic [ع.] and, for ebtekâr, records the literal 'to go out at dawn, to rise early' sense first, which is the very link to the root B.k.r that Nourai's arrow asserts.\"},\n       {\"src\": \"KLN\", \"where\": \"p. 44\", \"stance\": \"supports\",\n        \"note\": \"Klein's account of bikr 'virgin' < bakara 'he rose early' is what the Persian loan carries over unchanged.\"},\n       {\"src\": \"ARY\", \"where\": \"grep in ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry — as expected, since بکر/ابتکار are Semitic loans and outside its scope.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Spanish\", \"words\": \"al-bacora\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Spanish albacora, a large tunny, is a genuine Andalusian-Arabic borrowing carrying the article al-, and its Arabic \"\n                    \"etymon is of the b-k-r family; but the sources disagree on which member. Klein (p. 44), whom Nourai follows, has \"\n                    \"\\\"Sp. albacora, fr. Arab. al-bakrah, 'the young camel'\\\", the fish being named for its size; Wiktionary's Spanish entry \"\n                    \"has albacora \\\"from Andalusian Arabic, from classical Arabic اَلْبَكُورَة al-bakūra, 'the young camels'\\\", i.e. the \"\n                    \"collective plural rather than the singulative; and a third line (Portuguese albacora, and Etymonline's \\\"al bakara \"\n                    \"'milk cow'\\\") reads the name from بَاكُورَة bākūra 'early/first fruits, that which comes early', the tuna being an \"\n                    \"early-arriving fish. All three stay inside b-k-r, so Nourai's arrow is right in substance; the exact Arabic form and \"\n                    \"the exact image ('young camel' vs 'first fruits') are not settled, hence 'plausible' rather than 'confirmed'. Note \"\n                    \"also that the box prints the Spanish word with the Arabic article still detached, al-bacora, whereas Spanish has it \"\n                    \"fused as albacora.\"),\n     \"derivation_fa\": (\"«albacora»ی اسپانیایی نامِ نوعی ماهی تُنِ بزرگ است و به‌راستی وام‌واژه‌ای از عربیِ اندلسی با حرف تعریفِ «ال» است، \"\n                       \"و ریشهٔ آن نیز از خانوادهٔ ب‌-ک‌-ر؛ اما در اینکه کدام صورت، منابع یکسان نیستند: کلاین (ص ۴۴) — که نورایی از او گرفته — \"\n                       \"«اسپانیایی albacora از عربی البَکْرَة «شترِ مادهٔ جوان»» می‌آورد و می‌گوید ماهی را به سببِ بزرگی چنین نامیده‌اند؛ \"\n                       \"ویکی‌واژه «از عربی اندلسی، از البَکُورَة «شتران جوان»» می‌نویسد؛ و روایت سوم (پرتغالی albacora و اتیمانلاین) آن را از \"\n                       \"«باکورة» «نوبر، آنچه زود می‌رسد» می‌داند، چون این ماهی زود از راه می‌رسد. هر سه درون همان ریشه‌اند، پس پیکانِ نورایی \"\n                       \"در اصل درست است، ولی صورت دقیق عربی و انگیزهٔ نام‌گذاری قطعی نیست. همچنین کتاب واژه را با «ال»ِ جدا نوشته \"\n                       \"(al-bacora) حال آنکه در اسپانیایی به‌هم‌پیوسته albacora است. نتیجه: با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/albacora\",\n       \"https://www.etymonline.com/word/albacore\",\n       \"https://ahdictionary.com/word/search.html?q=albacore\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"KLN:44\", \"status\": \"supports\",\n        \"note\": \"Klein p. 44: \\\"albacore, n., a species of tunny (zool.) — Sp. albacora, fr. Arab. albakrah, 'the young camel', fr. al-, 'the', and the collective noun bakr, 'young camels'…\\\" — Spanish, and 'the young camel', exactly as in the box.\"},\n       {\"ref\": \"AHD:29\", \"status\": \"partial\",\n        \"note\": \"The current AHD gives \\\"[Portuguese albacor, from Arabic al-bakūra: al-, the + bakūra, albacore; see bkr in the Appendix of Semitic roots.]\\\" (ahdictionary.com/word/search.html?q=albacore) — same Semitic root, but Portuguese rather than Spanish and the bakūra form; the 1975 New College edition p. 29 that Nourai cites is not on disk, and older AHD printings did give 'Spanish'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 44\", \"stance\": \"supports\", \"note\": \"As quoted — the only source that gives precisely 'Spanish' + 'the young camel'.\"},\n       {\"src\": \"LKT\", \"where\": \"grep 'albacora|albakora' in LKT.txt\", \"stance\": \"silent\",\n        \"note\": \"Lokotsch's dictionary of European words of Oriental origin, as OCR'd here, yields no albacora article.\"},\n       {\"src\": \"DEV\", \"where\": \"DEV.txt line 249\", \"stance\": \"partial\",\n        \"note\": \"Devic discusses the same Andalusian pattern of Arabic al- + noun giving Spanish al-forms (\\\"al-fostoq, pistache, est devenu en espagnol alfostigo … On peut y joindre alhondiga, de al-fondouq\\\") — it confirms the borrowing mechanism for Spanish al-words without treating albacora itself.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"albacore\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"English albacore appears in the 1570s, in accounts of tropical fishing, as a borrowing of an Ibero-Romance form of the \"\n                    \"Arabic word: Klein and the older AHD say Spanish albacora (which is what the chart draws), while Etymonline, the \"\n                    \"current AHD and Wiktionary say Portuguese albacor/albacora — the Portuguese route being favoured because the first \"\n                    \"English attestations come from the Portuguese Atlantic and Indian-Ocean voyages. The word is unchanged in form apart \"\n                    \"from the English spelling -core for Romance -cora/-cor. Either way the chain English < Ibero-Romance < Andalusian \"\n                    \"Arabic al-bak(ū)ra < b-k-r is agreed; only the identity of the Romance donor is uncertain, so 'plausible'.\"),\n     \"derivation_fa\": (\"واژهٔ انگلیسی albacore در دههٔ ۱۵۷۰ در گزارش‌های ماهیگیری مناطق گرمسیری پدیدار می‌شود و وام‌واژه‌ای است از صورتی \"\n                       \"ایبریایی از همان واژهٔ عربی: کلاین و چاپ‌های کهن‌ترِ AHD «اسپانیایی albacora» می‌گویند (همان که در نمودار آمده)، \"\n                       \"ولی اتیمانلاین، AHD امروزی و ویکی‌واژه «پرتغالی albacor/albacora» را ترجیح می‌دهند، چون نخستین کاربردهای انگلیسی \"\n                       \"به سفرهای دریایی پرتغالی‌ها در اقیانوس اطلس و هند بازمی‌گردد. تغییر صوری تنها در املای پایانهٔ ـcore به‌جای ـcora است. \"\n                       \"در هر حال زنجیرهٔ انگلیسی ‹ ایبریایی ‹ عربی اندلسی البَک(ُو)رة ‹ ریشهٔ ب‌-ک‌-ر پذیرفته است و تنها زبانِ میانجی محل \"\n                       \"اختلاف است. نتیجه: با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/albacore\",\n       \"https://en.wiktionary.org/wiki/albacore\",\n       \"https://ahdictionary.com/word/search.html?q=albacore\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"KLN:44\", \"status\": \"supports\",\n        \"note\": \"Klein p. 44 heads the entry \\\"albacore, n., a species of tunny (zool.) — Sp. albacora…\\\" — English from Spanish, as the chart draws.\"},\n       {\"ref\": \"AHD:29\", \"status\": \"partial\",\n        \"note\": \"Current AHD s.v. albacore: \\\"[Portuguese albacor, from Arabic al-bakūra…]\\\" — same word and root, Portuguese donor. The 1975 New College p. 29 could not be checked (that edition's dictionary text is not on disk; only Watkins' IE appendix is).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 44\", \"stance\": \"supports\", \"note\": \"\\\"albacore … — Sp. albacora, fr. Arab. albakrah, 'the young camel'\\\".\"},\n       {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century vol. 1 (A-)\", \"stance\": \"silent\",\n        \"note\": \"The albacore article is not legible in the OCR of the volume on disk (the scan of the early A pages is heavily damaged); no statement recoverable.\"},\n       {\"src\": \"FSD\", \"where\": \"vol. 1 (A-Dive)\", \"stance\": \"silent\",\n        \"note\": \"grep for 'albacore' in FSD_vol1.txt returns nothing usable — the entry did not survive the OCR.\"},\n       {\"src\": \"SKT\", \"where\": \"grep 'albacore' in SKT.txt\", \"stance\": \"silent\",\n        \"note\": \"Skeat's Concise has no albacore entry.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-99.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk99.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-99.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 99"
}
```


### [2026-09-05T14:50:44.610Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 8, 'disputed': 1, 'transcription_suspect': 1, 'plausible': 3}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 14, 'partial': 3, 'contradicts': 1, 'not_checked': 1}
books consulted: {'partial': 12, 'supports': 18, 'silent': 11, 'contradicts': 7} | by book: {'KLN': 9, 'MON': 5, 'LKT': 5, 'FSD': 4, 'SIN': 3, 'SKT': 3, 'WEB': 3, 'BQT': 2, 'AHD': 2, 'FVQ': 2, 'DEV': 2, 'PHD': 1, 'HRN': 1, 'LEW': 1, 'AFA': 1, 'TAD': 1, 'AFM': 1, 'PLA': 1, 'ARY': 1}
```


## [2026-09-05T14:51:02.669Z] AGENT

Done. `data/verification/page-99.json` written; `verify_check.py 99` shows **0 PROBLEM lines** (13/13 nodes).

**Page 99 (book p. 69) — 2 entries, 13 nodes**
- Node verdicts: confirmed 8, plausible 3, disputed 1, transcription_suspect 1
- Root verdicts: `Bistak` plausible, `B.k.r` confirmed
- Ref checks: supports 14, partial 3, contradicts 1, not_checked 1

Flagged items:
- **disputed — Bistak #6, Arabic `fustug, fostoq` ← Greek.** Modern scholarship derives Arabic فستق from Middle Persian *pistag* directly (or via Aramaic *pistəqā*), not from Greek: Wiktionary, Fraenkel AFA 143-4 ("direct aus dem Persischen … oder mittelbar durch das Aramäische"), al-Unaysi TAD, Addi Shir. Nourai's own cited PLA:210 (Asbaghi) **contradicts** the Greek parent. Only AHD:535 supports it.
- **transcription_suspect — Bistak #8, French node.** `error_in: extraction`. See below.
- **ROOT `Bistak` plausible:** Pahlavi ⟨pstk'⟩ is read *pistag* today (MacKenzie p.74; Elamite *pi-iš-tuk-ka₄*); Nourai's b- reading is defensible (Asbaghi writes "bistag", Nicander has βιστάκιον) but non-standard.
- **plausible — B.k.r #3/#4 (Spanish al-bacora → English albacore):** Klein/AHD-1975 give Spanish; Etymonline, current AHD and Wiktionary give Portuguese *albacor* < Arabic *al-bakūra*. Root link unaffected.
- **plausible — Bistak #9, English `fustic, fistic`:** *fustic* (dyewood) is right; *fistic* is a separate obsolete English word for the pistachio nut (via It. *fistico*), not a variant of *fustic* — the node conflates two words.

**Extraction error the owner must fix (JSON ≠ printed page):**
- Entry 0, node #8 (French, AHD:535): the printed page shows an **empty French box** — header only, no word row. The JSON wrongly copies `"fustic, fistic"` from the adjacent English box into it. `data/extracted/batch/page-99.json` node 8 `words` should be empty.

Notable side-finding: Mo'in's footnote 5 s.v. پسته in Borhān-e Qāṭeʿ («در تازی فستق از آرامی فستقا … و به یونانی نقل شد pistakion») confirms that both chart NOTEs faithfully report MON:2545 — but Mo'in's Greek-from-Semitic claim is chronologically impossible (πιστάκιον is in Nicander, 3rd c. BCE; the tree in Theophrastus, 4th c. BCE — Laufer, *Sino-Iranica* 246, 251).

Page image archived at `data/verification/sources/refs/ocr/BOOK/99.png`; 17 web sources archived via `fetch_source.py`.
