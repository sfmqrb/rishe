# Verification process log — verify-page-166


## [2026-09-05T20:33:52.096Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 166 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-166.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-166.json. Write /home/sfmqrb/git/rishe/data/verification/page-166.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 166` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:33:53.396Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:33:54.278Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:33:54.289Z] TOOL RESULT

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


## [2026-09-05T20:33:54.828Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-166.txt"
}
```


### [2026-09-05T20:33:54.847Z] TOOL RESULT

```
1	=== PDF page 166 (book page 136) ===
2	--- entry 0 ---
3	ROOT [Iranian] Gabbah : dome, vault, blister  (refs AFM:123)
4	#1 (parent #0) [Persian] refs=MON:2894,2898 | kobbeh «کبّه ( کپّه )» : pile, heap ; kapîdan «کپیدن ۱» : to pile up
5	#2 (parent #0) [Arabic] refs=FVF:520; AFM:120 | qabbah : it was arched, bent ; al-qubbah : the arch, vaulted tent ; q.b.b : to be bent, crooked, vaulted | NOTE: KLN:46 claims these words are from the Semitic root "q.b.b: to be bent"
6	  #3 (parent #2) [Persian] refs=MON:2637; VGH:94; FVA:323 | qobbeh «قبّه ( قباب )» : dome, vault
7	  #4 (parent #2) [Spanish] refs=KLN:46 | alcoba : arched area
8	    #5 (parent #4) [French] refs=KLN:46 | alcove
9	      #6 (parent #5) [English] refs=KLN:46; TYL:567 | alcove : a recessed section in a room
10	--- entry 1 ---
11	ROOT Gag -> redirect to Kak 4
12	--- entry 2 ---
13	ROOT [Indo-European] Gal, Galgh, Galagh : to shout, complain  (refs POK:351)
14	#1 (parent #0) [Avestan] refs=POK:351 | garez : to complain
15	  #2 (parent #1) [Pahlavi] refs=BQT:1832 | gilak : complaint
16	    #3 (parent #2) [Persian] refs=BQT:1832 | geleh «گِله» : complaint
17	#4 (parent #0) [Germanic] refs=AHD | kall : to shout
18	  #5 (parent #4) [English] refs=None | call
19	--- entry 3 ---
20	ROOT Galagh -> redirect to Gal
21	--- entry 4 ---
22	ROOT Galgh -> redirect to Gal
23	
```


## [2026-09-05T20:33:58.102Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-166.json",
 "description": "Read source JSON page 166"
}
```


### [2026-09-05T20:33:58.140Z] TOOL RESULT

```
{
  "pdf_page": 166,
  "book_page": 136,
  "entries": [
    {
      "root": {
        "name": "Gabbah",
        "lang": "Iranian",
        "refs": "AFM:123",
        "gloss": "dome, vault, blister",
        "note": null
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:2894,2898",
          "words": [
            {
              "translit": "kobbeh",
              "gloss": "pile, heap",
              "script": "کبّه ( کپّه )"
            },
            {
              "translit": "kapîdan",
              "gloss": "to pile up",
              "script": "کپیدن ۱"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVF:520; AFM:120",
          "words": [
            {
              "translit": "qabbah",
              "gloss": "it was arched, bent",
              "script": null
            },
            {
              "translit": "al-qubbah",
              "gloss": "the arch, vaulted tent",
              "script": null
            },
            {
              "translit": "q.b.b",
              "gloss": "to be bent, crooked, vaulted",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "KLN:46 claims these words are from the Semitic root \"q.b.b: to be bent\"",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2637; VGH:94; FVA:323",
          "words": [
            {
              "translit": "qobbeh",
              "gloss": "dome, vault",
              "script": "قبّه ( قباب )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Spanish",
          "refs": "KLN:46",
          "words": [
            {
              "translit": "alcoba",
              "gloss": "arched area",
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
          "lang": "French",
          "refs": "KLN:46",
          "words": [
            {
              "translit": "alcove",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:46; TYL:567",
          "words": [
            {
              "translit": "alcove",
              "gloss": "a recessed section in a room",
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
        "name": "Gag",
        "redirect": "Kak 4"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gal, Galgh, Galagh",
        "lang": "Indo-European",
        "refs": "POK:351",
        "gloss": "to shout, complain",
        "note": null
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:351",
          "words": [
            {
              "translit": "garez",
              "gloss": "to complain",
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
          "refs": "BQT:1832",
          "words": [
            {
              "translit": "gilak",
              "gloss": "complaint",
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
          "refs": "BQT:1832",
          "words": [
            {
              "translit": "geleh",
              "gloss": "complaint",
              "script": "گِله"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "کو پیک صبح تا گِله های شب فراق - با آن خجسته طالع فرخنده پی کنم ؟",
            "poet": "Hâfez"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "kall",
              "gloss": "to shout",
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
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "call",
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
        "name": "Galagh",
        "redirect": "Gal"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Galgh",
        "redirect": "Gal"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:33:58.925Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-05T20:33:58.973Z] TOOL RESULT

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
page-311.json
page-31.json
page-32.json
----
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
```


## [2026-09-05T20:34:03.218Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '120,260p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Rest of source matrix"
}
```


### [2026-09-05T20:34:03.259Z] TOOL RESULT

```
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


## [2026-09-05T20:34:05.039Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AFM','FVF','FVQ','KLN','MON','BQT','POK','AHD','VGH','FVA','TYL','PLA','LKT','DOZ','DEV','PHN','LAM','AFA','SKT','WEB','FSD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600]); print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-05T20:34:07.368Z] TOOL RESULT

```
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

VGH {"title": "H. Khadiv Jam, Vazhe-name-ye Ghazalha-ye Hafez, Elmi 1371/1992", "kind": "website", "url": "https://ketabnak.com/book/121989 (145 pp. PDF, login)", "lookup_hint": "Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF page exists; not fetched."}

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

TYL {"title": "W. Taylor, Arabic Words in English (S.P.E. Tract XXXVIII), Oxford 1933", "edition_found": null, "kind": "hathitrust_fullview", "url": "https://babel.hathitrust.org/cgi/pt?id=uc1.b4089843 (S.P.E. Tracts nos. 31-40 bound volume incl. Tract XXXVIII, rightsCode pdus = full view in the US; record 000519279) ; mdp.39015005310308 (nos. 36-58) search-only", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_LeedsStudiesInEnglish_ArabicWordsInBenJonson_pp44-50.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incom

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed 

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start wit

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
```


## [2026-09-05T20:34:25.996Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,80p data/verification/page-147.json && echo ===== && sed -n 1,60p tools/verify_check.py",
 "description": "Inspect example output and checker"
}
```


### [2026-09-05T20:34:26.051Z] TOOL RESULT

```
Exit code 1
{
 "pdf_page": 147,
 "book_page": 117,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 2,
   "root": "Ed",
   "verdict": "confirmed",
   "modern_form": "PIE *h₁ed- 'to eat' (older notation *ed-), athematic present *h₁és-ti, with the participial derivative *h₁dónt-/*dnt- 'tooth' ('the biting one')",
   "note": "Pokorny IEW 287 heads the entry 'ed- \"essen\"' and adds 'Nominalformen: ed-ono-, ed-men-, ed-uen-… ; edont-, dont-, dnt- \"Zahn\"', which is precisely Nourai's root box plus the tooth branch he draws under Germanic and Latin. Walde-Pokorny I 118 has the same headword; Watkins/AHD 1985 p.417 'ed-. To eat; original meaning \"to bite\". See dent-. [Pok. ed- 287.]'. Language label ('Indo-European'), form and gloss are all right; the modern laryngeal notation is *h₁ed-. The two weak places on this page are the Avestan box (node 1: 'xarka-asa' is a misprint for kahrka-āsa- and 'asa' is glossed 'food' where it means 'eating'), the Persian box (node 2: آش is disputed), and the reconstructed compound in node 3, where every other source writes *aspa-asti- (with the -ti- abstract), not 'aspa-asa'. The extraction is faithful: I rendered pdf page 147 at 200 dpi (copy at data/verification/sources/refs/ocr/BOOK/147.png) and every form, gloss, script string and reference in page-147.json matches the printed chart. One citation error of Nourai's own: BQT:1624 is the کرکس page, so it supports nodes 1-2 but not node 8 (فسفسه stands at BQT p.1489).",
   "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپایی آغازینِ *h₁ed- «خوردن» است که پوکورنی در صفحهٔ ۲۸۷ فرهنگ خود با صورت قدیمی‌ترِ ed- و معنای آلمانی «essen» آورده و در همان‌جا می‌افزاید که صورت‌های اسمیِ edont-, dont-, dnt- به معنی «دندان» نیز از همین ریشه‌اند؛ یعنی هر دو شاخهٔ «خوردن» و «دندان» که نورایی رسم کرده، درست است. والده-پوکورنی (جلد ۱ ص ۱۱۸) و واتکینز در پیوستِ فرهنگ American Heritage (ص ۴۱۷) نیز همین را می‌گویند: «ed-. خوردن؛ معنای اصلی: گاز گرفتن». پس جعبهٔ ریشه، برچسب زبان و معنا هر سه درست است و ادعای نورایی در این حد پذیرفتنی است. سه نقطهٔ سست در نمودار هست: صورت «xarka-asa» در گرهٔ ۱ (که غلط چاپی به‌جای kahrka-āsa- است)، ریشه‌شناسی «آش» در گرهٔ ۲ که امروزه محل اختلاف است، و ترکیبِ بازسازیِ گرهٔ ۳ که در همهٔ مأخذها *aspa-asti- نوشته می‌شود نه aspa-asa.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ed-"
   ],
   "ref_check": [
    {
     "ref": "POK:287",
     "status": "supports",
     "note": "POK_01.txt, form-feed page 300 (= IEW pp. 287-288; grep -n \"cd-  ,essen\" → line 4121, the OCR reads initial e- as c-): 'ed- ,essen'; ursprüngl. athematisch, aber meist thematisch geworden; Nominalformen: ed-ono-, ed-men-, ed-uen-… ; edont-, dont-, dnt- ,Zahn'.' The same page then lists 'av. 3. Sg. Konj. adäiti', 'lat. edö, es, est ,essen'', 'got. themat. itan … ags. etan, engl. eat'. Exactly the root box and the three first-generation branches Nourai draws."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Walde-Pokorny I 118 (WLD_Bd1_1930_dli_70244_djvu.txt line 7698)",
     "stance": "supports",
     "note": "'ed- „essen“. Praes. unthematisch ai. admi, atti „esse, ißt“ … lat. edo, es, est … Thematisch got. itan, an. eta, as. ags. etan, ahd. ezzan „essen“' — the source Pokorny 287 abridges."
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, AHD_watkins1985.txt line 417 (ed-) and line 364 (dent-)",
     "stance": "supports",
     "note": "'ed-. To eat; original meaning \"to bite.\" See dent-. 1. Germanic *etan in: a. Old English etan, to eat: EAT; b. Old High German ezzen … : ETCH … 2. Latin edere, to eat: EDACIOUS, EDIBLE … [Pok. ed- 287.]'; and 'dent-. Tooth. (Originally participle of ed- in the earlier meaning \"to bite.\") 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dnt- perhaps in Germanic *tunth-sk- in Old English tūsc, tūx, canine tooth: TUSK. 3. Full-grade form *dent- in Latin dēns … [In Pok. ed- 287.]'"
    },
    {
     "src": "IEC",
     "where": "Mann, IEC.txt lines 3420-3426, 3693",
     "stance": "supports",
     "note": "'edmi, (edō), 3s esti \"eat\". WP I, 118 — Skt. ádmi; Av. ad-; Hitt. ēdmi; Hom. édō; Lat. edō, 3s ēst; Osc. edum; Go. itan; OE etan; OHG eʒʒan …'; also 'edolis, os, om \"edible; food\"' and 'ēskā \"food\"'."
    },
    {
     "src": "SYN",
     "where": "Buck 5.11 EAT (SYN.txt line 8318 ff.)",
     "stance": "partial",
     "note": "'1. IE *ed-. Walde-P. 1.118 … Grk. édō, Lat. ēsse, late edere, Osc. edum … Goth. itan, so all Gmc.' — but Buck's Avestan column for 'eat' gives 'Av. xᵛar-, gah-', not ad-: in Avestan itself the inherited root survives only marginally (the subjunctive adāiti and compounds), the ordinary verb being xᵛar-."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan",
     "words": "adâiti; asa 1; xarka-asa",
     "verdict": "transcription_suspect",
     "error_in": "book",
     "book_prints": "xarka-asa : eating bird ☞ Ker 3",
     "correct_form": "kahrka-āsa- (Av. kahrkāsa- 'vulture', lit. 'fowl-eater')",
     "derivation": "Three items, three different situations. (a) adâiti is real: Pokorny 287 cites 'av. 3. Sg. Konj. adāiti' as the Avestan continuation of athematic *h₁ed-, i.e. a 3sg subjunctive 'he shall eat' — not an infinitive, and not the ordinary Avestan verb for 'eat', which is xᵛar- (Buck 5.11); Bartholomae's Altiranisches Wörterbuch col. 55 has only an ad- 'to say'. So the root is preserved in Avestan only marginally, in this form and in compounds. (b) 'asa 1 : food' is Avestan -āsa-, but it is a compound-final adjective 'eating, eater' (Mo'in glosses it خورنده), never an independent noun 'food'; Nourai's gloss reverses the word class. (c) 'xarka-asa' is a misprint. The Avestan word is kahrkāsa- m. 'vulture' (Bartholomae col. 456, 'j. kahrkāsa- m. \"Geier\" … Komp.: *kahrka- + *āsa-'), a bahuvrihi-type compound of kahrka- 'cock, hen' (Nourai's own root 'Ker 3'; he spells it kahrkatât on book p. 227 = pdf 257) with -āsa- 'eating'. It therefore means 'fowl-EATER', not 'EATING bird' — the compound is object + verbal noun, and Mo'in states it flatly: «مرغ‌خوار». I rendered pdf p.147 at 200 dpi: the printed page really shows 'xarka-asa : eating bird', so the extraction is faithful and the error is Nourai's own (probably a compositor's loss of the first syllable ka(h)- of kahrka-).",
     "derivation_fa": "این جعبه سه واژه دارد و وضع هر سه فرق می‌کند. نخست، adâiti واقعی است: پوکورنی در ص ۲۸۷ آن را «صیغهٔ التزامیِ سوم‌شخص مفرد اوستایی» از ریشهٔ *h₁ed- می‌آورد؛ یعنی «بخورد»، نه مصدر. باید توجه داشت که فعل معمولِ «خوردن» در اوستا xᵛar- است و بارتولومه در ستون ۵۵ فرهنگ خود فقط ad- به معنی «گفتن» را آورده است؛ پس این ریشه در اوستا تنها به‌صورت پراکنده (همین صیغه و در ترکیب‌ها) مانده است. دوم، asa صفتِ پایانِ ترکیب است به معنای «خورنده»، نه اسم به معنای «خوراک»؛ معین هم آن را «خورنده» معنی کرده است. سوم، «xarka-asa» غلط چاپیِ کتاب است: صورت درست اوستایی kahrkāsa- «کرکس» است، مرکب از kahrka- «کرک، مرغ» و āsa- «خورنده»، یعنی «مرغ‌خوار» و نه «پرندهٔ خورنده»؛ خودِ نورایی در ص ۲۲۷ کتاب kahrkatât می‌نویسد. تصویر صفحهٔ چاپی را دیدم: در کتاب هم «xarka-asa» چاپ شده، پس خطا از خوانشِ اسکن نیست، خطای چاپی خودِ کتاب است.",
     "sources": [
      "https://en.wiktionary.org/wiki/%DA%A9%D8%B1%DA%A9%D8%B3"
     ],
     "ref_check": [
      {
       "ref": "POK:287",
       "status": "supports",
       "note": "IEW 287 (POK_01.txt, \\f-page 300): 'av. 3. Sg. Konj. adäiti' — the exact form of the chart, under ed- 'essen'."
      },
      {
       "ref": "BQT:44",
       "status": "supports",
       "note": "BQT_v1_pages.txt leaf 255 (= printed p. 44/45; offset ≈ leaf − 210), Mo'in's footnote 5 s.v. آش: «آش — در سانسکریت aś، هم‌ریشهٔ ad بمعنی خوردن و با edo لاتینی … مانند essen آلمانی و (to) eat انگلیسی … این ریشه در چند کلمهٔ فارسی بجا مانده: کرکس، آش، ناشتا» (OCR: 'در ساسکرت ۸5 همریقة 80 بمعتی خوردن … کر کس ,آش, ناثتا'). Exactly the root and the three Persian reflexes."
      },
      {
       "ref": "BQT:1624",
       "status": "supports",
       "note": "printed p. 1624 = BQT_v3_picofile.pdf p. 417 (pagemap), the کرکس page; Mo'in's footnote 9: «کرکس. اوستا kahrkāsa (کرکس). پهلوی kargās … کلمهٔ اوستایی مرکب از دو جزء است: kahrka (= کرک، مرغ) + āsa (خورنده)، جمعاً یعنی مرغ‌خوار». It supports the derivation but spells the first member kahrka, not Nourai's xarka, and glosses the compound 'fowl-eater', not 'eating bird'."
      }
     ],
(eval):1: ==== not found
```


## [2026-09-05T20:34:28.862Z] TOOL CALL #8: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-05T20:34:28.894Z] TOOL RESULT

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


## [2026-09-05T20:34:37.019Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['AFM','MON','BQT','POK','AHD','KLN','TYL','FVQ']:\n    e=d[k]\n    print(k,'| offset:',e.get('page_offset'),'| hint:',e.get('lookup_hint'))\n    print('   local:',e.get('local_file'))\n    print()\nEOF",
 "description": "Get page offsets for key refs"
}
```


### [2026-09-05T20:34:38.708Z] TOOL RESULT

```
AFM | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']

MON | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']

BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']

POK | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt

AHD | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt

KLN | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt

TYL | offset: None | hint: Not on IA (searched 'arabic words in english', 'society for pure english tract 38'); Google Books record has no view. Taylor's related 'Etymological List of Arabic Words in English' (1933) id QmBbAAAAIAAJ is snippet only.
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_LeedsStudiesInEnglish_ArabicWordsInBenJonson_pp44-50.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_BenJonson_pages.txt']

FVQ | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt']
```


## [2026-09-05T20:34:43.230Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK leaf 359 (p.351) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==360' POK_01.txt | head -60\necho \"=== POK leaf 358 (p.350) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==359' POK_01.txt | head -60",
 "description": "Print Pokorny pages 350-351"
}
```


### [2026-09-05T20:34:44.814Z] TOOL RESULT

```
=== POK leaf 359 (p.351) ===

=== POK leaf 358 (p.350) ===
```


## [2026-09-05T20:34:47.262Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la POK_*.txt\npython3 -c \"\nd=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nprint('pages',d.count('\\f'))\n\"\ngrep -n \"lemma: gal\" POK_full.txt | head -20",
 "description": "Check POK files"
}
```


### [2026-09-05T20:34:48.874Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
pages 363
29635:Root / lemma: gal-1\ "bald; naked' derived from Root/ lemma: koi-lo-\ "naked; miserable'. 
29669:Root / lemma: gal-2 
29744:Root / lemma: gal-3ox ghal-
```


## [2026-09-05T20:34:50.719Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29660,29760p' POK_full.txt",
 "description": "Print Pokorny gal-2 entry"
}
```


### [2026-09-05T20:34:50.766Z] TOOL RESULT

```
Baltic and slaw, intonation {galvc[ : goiovu) do not agree; compare Meillet Slave 
commun2 183, 503; Baltic pushed intonation spoke after Trautmann 77 rather for kinship 
with Armenian ^/^-^"head' from *^/7dA/-/rc»- (Meillet Esquisse 36); then however, Germanic 
words must be observed as Latin loanword (from calvus). 

References: WP. I 537 f., WH. I 143 f., Trautmann 77; different MiJhlenbach-Endzelin I 596 
f., Specht Dekl. 85, 132. 
Page(s): 349-350 

Root / lemma: gal-2 

Meaning: to call, cry 

Material: 1. Cymr. ga/w'caW, shout, cry, subpoena, send an invitation to court, summon'. 

Middle Breton ga/u 'caW, appeal; claim, summons; plea' {*ga/-uo-), Middle Irish ga//lan\e, 

glory, honor ' ( *gal-no-s, covered only doubtfully), probably also ga/Z'swan'; 



Old Church Slavic glagoljq, glagolati {* gal-gal-) 'speak', glagolt "word", russ. gologolitb 
"chatter, joke, jest, tell a funny tale '; perhaps Old Indie gargara-h " a certain music 
instrument ' (= Old Church Slavic glagoli^, if with /"from Indo Germanic /, Meillet Et. 229; or 
to *ger- or *g"er-, what in alignment these onomatopoeic words are not closed, compare 
from still from one more such Old Indie gharghara-^ rattling, clashing, gargling, gurgling; 
m. din, fuss, noise'). 

2. gal-so-\'c\. 

osset. yalas^ cpoovri ', Old Church Slavic glasi^, russ. golos'b 'voice', Lithuanian galsas 
"echo ', Old Norse kallu. ' the calls ', whereof kalla^caW, shout, cry, sing'. Old English 
call/an {eng\. call) ds.. Old High German kallon^ speak, babble, chatter a lot and loudly ', 
with -/A from -Iz-, next to which -Is- in Old Norse kails n. 'provocation, incitation, irritation'. 

from Latin ^a//i/5 "rooster, cock' (only afterwards supported in the Gaul's name) vorder 
Old Saxon loanword, also as gr. KaAAaiov ' a cock's comb '? 

Maybe alb. ^/e/' rooster, cock' 

In addition perhaps as extensions, but rather independent onomatopoeic words: 

3. gla^\ 

gr. yAa^w ' lets a song resound ' (*YAaYju)); 

Old Norse A/a/ra 'chirp, twitter'. Old English clacui. 'insult', further plural with function in 
"resounding, roaring, banging blow' Middle High German /r/5C "applause, clapping of the 
hands, slam, bang, strike, noise, crack', klecken^ meet, break, crack with a bang ', engl. 
c/ac/r "clatter, rattle, clash, chat, prate'. Old Norse klakk-sarr^ injurious, malign, pernicious 
', and m. d. meaning " make move, put into motion slapping, tattling, splotch, stain; smear' 
Middle High German klac a\so " splash, splotch, stain, blob, spot, blot ', Middle Low 
German klacken^ make blot, splash, splotch, stain ' (Modern High German klecksen, 
Klecks= ndd. klakks). Old Norse klakkr^ blot, splash, splotch, stain, clump, cloudlet, 
cloudling, small cloud '; 

4. gal-gh-, g{^a)lagh- " lament, wail, scold, chide': 

Old \n6\c garhatl, -te, ved. 3. PI. grhate' complains, reproves, rebukes ', garha 
"reprimand', grhu- " beggar, mendicant ', Avestan gerszaitr complains, cries, wails ', 
osset. ^3/2-^/7 "groan, moan', Avestan graza, npers. gila^ lament'; 



Old High German klaga' lament', klagon^ wail '; 

Middle Irish ^/a/77 "clamor, curse, swearword, evil proclamation ' {*glagh-sma)\ 

5. nasalized glengh- : Old High German k//ngan'r\ng, sound, clink' (without close 
connection to Latin clangor, gr. KAavYH sound'), next to which with Germanic 'thin, fine; 
delicate; weak, feeble' Old High German klinkan6s., engl. clink, Swedish klinka^ clink '. 

In Germanic furthermore *kalt-, *klat-, *klap-, e.g. Middle High German kalzen, kelzen^ 
babble, chatter'; Old Frisian /r5///5 'speak'; Old English c/a//7a/7 'clatter, rattle, clash', 
Modern High German /(7a/z 'smirch, stain, splotch, smear', bekletzen; Old Norse klappu. 
'sound of a kiss; sound of a lash; gossip, rumors, blow, knock'. Old High German klapfm. 
'gossip, slam, bang, strike, blow, knock, shove '. 

References: WP. I 538 f., WH. I 580 f., Trautmann 77. 

See also: compare the similar to onomatopoeic words ghel-, kel-. 

Page(s): 350-351 

Root / lemma: gal-3ox ghal- 

Meaning: to be able 

Material: Cymr. gallu^ to be able, can be able ', corn, gallos^^o^ef, bret. gallouV to be 

able ' (//< In), Irish gal\. ' braveness, boldness, courageousness ', abret. gar skill, ability, 

power'; Old Irish dT-gal\., cymr. dial, corn. dyaF revenge, vengeance '; gallorom. *galla^ 

power' (Wartburg); in addition Celtic VN Galll, raAarai; 

Note: 

The name VN Galll, gr. raAarai, Keltoi seem synonymous as Keltoi is an attribute noun 

modelled after lllyrian adj. (see alb. numbers).
```


## [2026-09-05T20:35:03.608Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG garz ===\"; grep -n -i \"garz\" CHEUNG.txt | head -30\necho \"=== BRT gərəz ===\"; grep -n \"gərəz\\|g@r@z\\|garəz\\|garez\" BRT.txt | head -20\necho \"=== AHD gal ===\"; grep -n \"^gal-\\|^gal\\b\" AHD_watkins1985.txt | head -10",
 "description": "Grep Cheung, Bartholomae, AHD"
}
```


### [2026-09-05T20:35:03.683Z] TOOL RESULT

```
=== CHEUNG garz ===
7801:gilak, golak (IIFL I: 395), with -z- Bakht. gerza, also ‘mouse’ in Gil. garze, garza, 
7802:NP garzah (Rudaki). The -z- variants are derived from an unsupported base *garz ‘to 
7896:*NWIR: ? NP garzin ‘arrow’, ? Tt. (Sag.) u-jir ‘lift !’ (u- prev. ‘up’). 0 Schwartz, Gs 
7897:Henning: 387 f. cites NP garzin from the lexicographical source Farhang-i Jahangiri 
7898:in support of a rather obscure base *garz ‘to bite, sting, prick’. Alternatively, garzin 
8067:*garz 111 
8113:*garz ‘to lament, weep’ 
8127:BMP glc- /garz-/ ‘to weep, lament’? (LW) || (+ *upa-) MMP ’bgrysn ‘moaning, 
8131:BMP glydynd, gldynd /griyénd/, BMP glcynd /garzénd/, SUBJ. 152. MMP gryy’n, etc. 
8736:*gr(a)id. The Persian meaning hardly allows separation from *garz ‘to lament, 
35150:glc- /garz-/, 112 
40993:garzah, 106 
40995:garzin, 108 
45248:garze, garza, 106 
57038:*ban (s.v.), *garz, *karp, 
58386:*bram, *garz, *snaud, *xSai, 
=== BRT gərəz ===
=== AHD gal ===
235:gal-?. 3. Expressive form *gall-...
476:gal-'. Bald, naked. Suffixed form “gal-wo- in Germanic *kalwaz in Old English calu, bare, bald: cALLOow. [Pok. 1. gal- 349.]
477:gal-2, To call, shout. 1. Germanic expressive form *kall- in Old Norse kalla, to call: CALL. 2. Germanic *klat- in Old English *clatrian (> Middle English clateren), to clatter: CLATTER. 3. Expressive form *gall- in Latin gallus, cock (< “the calling bird”; but probably also associated with Gallus, Gallic, as if to mean “the bird of Gaul,” the cock being archaeologically attested as an important symbol in the iconography of Roman and pre-Roman Gaul): GALLINACEOUS, (GALLINULE). [Pok. 2. gal- 350.]
478:gal-’. To be able, to have power. Gallo-Roman “galia, strength, power, in Old French galliart, lively: GALLIARD. [Pok. 3. gal- 361.]
```


## [2026-09-05T20:35:09.386Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8110,8150p' CHEUNG.txt",
 "description": "Print Cheung *garz entry"
}
```


### [2026-09-05T20:35:09.434Z] TOOL RESULT

```
25; NEVP: 32; Kiefer 2003: 196 


*garz ‘to lament, weep’ 

*AVESTAN: goroz- ‘to lament, weep’ => Liste: 19f. 

Pres. {1} athem.: IND. med. 1sg. OAv. garazdi/garazé (Y 32.9, Y 46.2), INJ. med. 3sg. OAv. garazda (Y 
29.1); Pres. {2} athem. red.: INJ. 3р1. OAv. (tr.!) jigorozat (Y 32.13); Pres. {3} them.: IND. med. 35р. 
YAv. gorozaite (Yt 10.53), OPT. med. 35р. YAv. gorezaeta (Yt 17.57 ff); Partic.: pres. {1} ҮАУ. 
%әгәғапа- 


112 *gau (*jau) 


*MIDDLE PERSIAN: MMP gry-, BMP gl(y)dy- /griy-/ ‘to weep’ (< OP *grad-ya-) || 
BMP glc- /garz-/ ‘to weep, lament’? (LW) || (+ *upa-) MMP ’bgrysn ‘moaning, 
crying’? = DMMPP: 164a, 10b 

Well attested: Pres.: IND. Isg. MMP gryym, 3sg. MMP “gryyd, 1р1. MMP gryy’m, 3pl. MMP gryynd, 
BMP glydynd, gldynd /griyénd/, BMP glcynd /garzénd/, SUBJ. 152. MMP gryy’n, etc. 

*PARTHIAN: grzysn ‘complaint’? = DMMPP: 165b 

*BACTRIAN: yipC- ‘to complain’ = S-W, Bact.: 189a 

*NWIR: NP giristan/giriy- ‘to weep’, NP gilah ‘complaint; lamentation’, Kurd. 
(Kurm.) giriZin/giriz- ‘to be grumpy, grumble, growl’, Awrom. gırawäy/gıraw- 
(LW), Bakht. girévistan “о weep, cry’, Gz. griye ‘weeping, lamenting’, Siv. ger-, 
gir-/gerd, gird ‘to lament’ 

*NEIR: Oss. I. qerzyn/qerzt, D. Serzun/gerzt ‘to groan’, Oss. I. gast, D. gast (orig. 
ppp. ?) ‘complaint, grief? 

*SANSKRIT: garh ‘to complain’ (RV+) = EWAia I: 475, 495 

9 An IE origin of this common IIr. root is uncertain. The Germanic and Irish forms 
cited by Pokorny (1.с.), OHG chlaga ‘complaint’, chlagön ‘to complain’ (etc.) and 
Olrish glam ‘cry, curse’, are probably from a substrate source, on which see 
Boutkan — Siebinga: 216.
```


## [2026-09-05T20:35:22.434Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD gilag ===\"; grep -n \"gilag\\|glk\\b\\|gilak\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n \"gilag\\|glk'\" NYB_vol2_glossary.txt | head -20\necho \"=== HRN gila ===\"; grep -n \"gila\\b\\|gile\\|Klage\" HRN.txt | head -30",
 "description": "Grep MacKenzie, Nyberg, Horn"
}
```


### [2026-09-05T20:35:22.516Z] TOOL RESULT

```
=== PHD gilag ===
PHD.txt:380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
PHD.txt:1304:complaint garzišn, gilag, must.
PHD.txt:2553:lamentation brāmag, čēhišn, gilag, móyag.
PHD.txt:5358:darak, gilag garm darmān garmāg garmābag
PHD.txt:5489:dagr-zīwišn gilagobàr
PHD.txt:5490:gilag dagr-pattày dast!, xwarrah! xwarrahómand! dastkārīh! dast(a)gird! samor
PHD_mackenzie.txt:2514:gilag [g(y)lk' I N gila] complaint, lamentation.
PHD_mackenzie.txt:6205:cloak kabah.                             complaint garzisn, gilag, must.
PHD_mackenzie.txt:6952:lamentation briimag, cehisn, gilag,       lemon balm wiidrangboy.
PHD_mackenzie.txt:10479:garzisnig                 \~t-'U&     darak, gilag               \~
PHD_mackenzie.txt:10837:gilagobar               ~Q),....r                   sust
PHD_mackenzie.txt:10839:gilag                                  ,}..a..      suft                       \ t"VtO
=== NYB ===
=== HRN gila ===
1940:Klagen (Is. 14, 31 ; 15, 4, 5), nwXir:N2 (Is. 57, 13).
5723:646. {\)xär 'Klagen', zäri^ zäre^), zandefi.
7206:828. feryäd *Hilfe; Hilferuf, Klage.
8079:930. gile 'Klage .
8080:aw. gerezü" 'Klage', vergl. [/^gar2-, gerezaiti 'klagen';
8083:kurd. gilt 'Klage', gire 'Streit'; oss. d. yärziin, t.
8665:997. möye 'Weinen, Klage', möylden,
8681:*Klage*, mustmeud,
9132:necä 'Klage', nevtden, vergl. nevaliden, nallden.
```


## [2026-09-05T20:35:25.956Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8075,8095p' HRN.txt\necho \"=== HUB ===\"; grep -n \"gile\\|gilak\\|gerez\" HUB.txt | head -20",
 "description": "Horn no.930 gile and Hübschmann"
}
```


### [2026-09-05T20:35:26.017Z] TOOL RESULT

```
*) Ein np, Deminutivsuffix -le finde ich nachträglich sehr häufig
bei den Bergjuden im Kaukasus. Aus Mi Her 's Glossar habe ich mir— 208 —
indog. Deminutivsuffix -/o- vergl. Brugmann, Grund-
riss II, 186 folg.
930. gile 'Klage .
aw. gerezü" 'Klage', vergl. [/^gar2-, gerezaiti 'klagen';
plilv. garzTtan j garz{i)s7i, gilak (Men.); ai. l^garh-,
garhate 'klagen, anklagen' ^).
kurd. gilt 'Klage', gire 'Streit'; oss. d. yärziin, t.
gärzin stöhnen* (89).
931. f/ii^ii«/Sfeii/an vertrauen, übergeben', Praes. gumär-em.
ap. *»/ -r V^mar- mit Bedeutungswechsel, vergl. skr.
vi- r smav' 'vergessen' ; phlv. gumästan, gumür.
Unsicher.
932. gtitnän 'Zweifel; Meinung'.
aw. '^vwianah' 'Zweifel', vergl. mmiwöhya-; phlv.
gnmän,
LW. kurd. afy. gumän 'Zweifel*; bei. gtarän (121).
933. f/unäh 'Sünde'.
g. venall.
skr. vinäga- 'das Verlorengehen, Vernichtung, Unter-
=== HUB ===
3258:gerezman 'Grab* nichts zu thun. Vgl. Fr. Muller,
5079:herezaiti; gila 'Klage' = zd. gerezd-; kistan saen', skr.
7853:= phi. gilak Phi. Min. p. 18, Z. 2 aus ap. *grda" = zd.
7854:gereza-., 15) np. hilad *lasst* aus ap. *hrdatiy ~ zd. here-
8809:guftan *sprechen', ap. gaub-; gila 'Klage = zd. gereza-
9322:(siehe § 34, a und b) ; gUa 'Klage* = phi. gilak, ap. "^grdor-
9323:= zd. gereza- (siehe § 110).
```


## [2026-09-05T20:35:40.426Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN alcove ===\"; grep -n \"^alcove\\|alcove,\" KLN_1966.txt KLN_1971.txt | head\necho \"=== KLN 1966 leaf for p46 ~ leaf 35 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==36' KLN_1966.txt | grep -n -i \"alcove\" ",
 "description": "Grep Klein for alcove"
}
```


### [2026-09-05T20:35:42.262Z] TOOL RESULT

```
=== KLN alcove ===
KLN_1971.txt:10681:alcove, n., 1) a recessed section in a room; 2) any 
KLN_1971.txt:10682:recess. — F. alcove, fr. Sp. alcoba , fr. Arab, al- 
KLN_1966.txt:2139:alcornoque,  n„  the  bark  of  several  trees.  —  Sp., Port,  ‘cork  tree’,  a  hybrid  coined  fr.  Arab,  al-, ‘the’,  and  L.  quercus,  ‘oak’,  changed  into  *quer - nus.  See  cork  and  cp.  Quercus. alcove,  n.,  1)  a  recessed  section  in  a  room;  2)  any recess.  —  F.  alcove ,  fr.  Sp.  alcoba,  fr.  Arab,  al- qubbah,  fr.  al-,  ‘the’,  and  qubbah,  ‘arch,  vaulted tent’,  which  is  rel.  to  Arab,  qabba,  ‘it  was  bent’, and  to  Heb.  qubbd \  ‘vaulted  tent’,  Syr.  qebha- bhd,  ‘vault,  vaulted  tent’,  Akkad,  qababu, ‘shield’.  All  these  words  are  derivatives  of  the Sem.  base  q-b-b,  ‘to  be  bent,  crooked,  vaulted’, aldea,  n.,  hamlet,  villa.  —  Sp.  and  Port.,  ham¬ let’,  fr.  Arab,  al-,  ‘the’,  and  dayah,  ‘farm,  ham¬ let’.  Cp.  aldeia.
=== KLN 1966 leaf for p46 ~ leaf 35 ===
```


## [2026-09-05T20:35:52.045Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=d.find('alcove,  n.,  1)')\nprint('leaf index (0-based):', d[:i].count('\\f'))\nEOF\necho \"=== AFM leaves 125-135 grep qubba/kubba ===\"\npython3 - <<'EOF'\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(d),'leaves')\nfor i,p in enumerate(d):\n    if 'القبة' in p or 'الكبة' in p or 'قبّة' in p:\n        print('---leaf',i, p[:80].replace('\\n',' '))\nEOF",
 "description": "Locate Klein leaf, search AFM for qubba"
}
```


### [2026-09-05T20:35:53.970Z] TOOL RESULT

```
leaf index (0-based): 36
=== AFM leaves 125-135 grep qubba/kubba ===
198 leaves
---leaf 89 لكر ).لد (السدِلّ) هو كثلثة بيوت في 7 45 » من سه اي ثلاثة ومن دل اي وسط اومن دير
```


## [2026-09-05T20:35:59.077Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(126,134):\n    print('======== leaf',i)\n    print(d[i][:900])\nEOF",
 "description": "Print AFM leaves 126-133"
}
```


### [2026-09-05T20:36:00.770Z] TOOL RESULT

```
======== leaf 126
ܚ ܘ ( ܙ -
المار. وهى ܩܪܛܠܐ بالسريانّة
( القرم) صبغ ارمني يكون من عصارة دوه يكون 4 قل هو اجر
>العدين حب بقع عل نوع امن ܐܕܝܐ في شهر اذار فان 0 عله و يمع ا
طائرًا وطار ( حيط المحيط )٠فارستة‏ قرمز.قال في البرهان القاطع ما $ <
قرمزء ٠‏ 37 اطمرة قدر 5 9 الرانحة بقع على الشجر
ܕܠܐ على الشجرة 03 حيدار في بلاد الماد ٠‏ وهذا الدود ܚ ܕ¦ܛܚܡܚ ܐ[
ܕ ܐ بوضعه في الماء الا - ٠‏ ويقال له بالعر بّة دودة الصباغين . ويطاق اسم القرمز
ايضاً على ضرب من المبوب يقال ل بالتركيّة قرءز تخمى (اي بزد القرمز) ويصبغرن به
ايضاً ` ` 405 | عركّمة من الفارسي .كام اي دودة ومن آل اي الدودة
الدراء .< الاي تاليف جسلتيرسن): او من كم زا يدف الروك
الاخيرة اي الدودة اللسناء ٠‏ وهو بالعبرانيّة 3 اقرب الى كم آل وبالارمنية
”,݇ܐ .وام بالعبرائئّة التدعة فهو ده و ܪܟܡ ١؟‏ ايام: ¥ :3 :€( و1:5١).‏
وكذا ورد اسمة ܙ ,)̈ܐ ܬܘܠܥܬܐ (اثعيا 18:1) و ܣܣܓܘܙܐ . وباللانيية
1105 ومنه 4 الفرضي 1 + ٠‏ وهو 610120151 11 و ܠ ܐܐ =
12 و 11115011ܐ¢ بالاتكايرءة و 11
======== leaf 127
+
٠‏ ܐ
ܨ
0
ܢܙ -
ما قيل قول ܐܕܐ في المعرب : القسطار هو 5( ¢ 3 1 لاذي :ܸܛ
امور القر ® وَسُووم, | قسطار وهو راح بع الى معنى الممزان اه وهو ܐܐܐ بحض نين
التسطاس اي الميزان والقسطار اى ® "فلن 0140 اله تعريب روعي
17 ومن ܚ ]0 ܥ 3206 بده ܬ الاموال وخزائن ال شيخة وعليه
ان يوزعها على امنود والمتوظفين ( راجع ايضأ فرتكل ص : 13
100 :3 مرك كن كن اي 630
ومن / وهي اداة التفضيل
4 السو 'الاسد» و( القَمَوَرَة) العزيز والاسد والشجاع و <التَنْسَري )
الرجل 050 21 ذلك معرب ܪܝܕ( ومعناه العظيم العريز
* 05 × اق مأخوذة عر 43 بان ومعناها صاحب 5
+ ( القشنيزة ) ترايت كنزلا وهى عشة 3 توق رق الهندباء 5 خضراء
$ ܢܐ الناس :
ܟ ععنى دق ܕܝ 0 ار ومله ; صم دم
بالسريانة و ܩܨܝܪܐ باللغة الربانة ( ܨܐ ص : ܝܐ )® > 20
والتركة
* (القصري) ما يبقى 5 من اللي بعد ان يداس 7( 88 ومئة
خه !+ بالسريايّة 0
¬ 5 ¥ ` 5 © 8.33
الأحق :
50 ܕܠܐ( غلاف المكحلة مركن ٠‏ 3 الكحل ومن دان
دهي اداة تاحق الأمياء ٠‏ فتدل على ܐܨ ܬ 1 القَْرَة وهي 52 اا نوص لعطر
1 
======== leaf 128
_ ¥ ܙ -
0035 والحرمالي 8 والايطاليالي 5 5 وهو 5 :
3 1
* (التَمَنْدَر والتَيْدر) اليم المنظر والشديد الرأس معرب كناد ار وهو مركب
من :® اي الشدّة ومن دار اي ܟܐ ܗܝܢ
( ܢܐܐ ) 000 ة تعريب كفجه ليز
(القأل) معرب كالب ٠‏ والفارسي مسأخوذ من ܐܝܬܠܲܢ ,«منةة مجم
9 19:47 5 © ذلك ان 16 ® ܗ يكاب
+ ( |( ) - 31 أى: لست ܐܙ اللبن تعريب كأنه 0 ويطلق
܂$[ على كل ذا بة مسِئّة لا تصاح © ومنهُ معرب ايضاً (القلاط ) اي القصير
دن 13 والسئانير
* ( ايلحم ) سكل الضخم عظي ܕ ( ܐܳܢ 0 التعظم في تقس 00
بك ` .= © ܗ الهامة٠‏ و١‏ التلمم ) الشيخ
1 :كل ذلك مأخوذ من كلهتخم اي »6 2 0 0 ܨ 7 قاض
ان ̈ܐܢ ܕܝܪ £ والعلَكُوم ,)£ ; )6 ܕ 7 9 ܕܐܐ حكد
ܝܐ ܢ 9 4 < < ܙ( ܝ ܝܨ والعاندى والعَمَلّس والعَمَلَط وَالمَمْضَّج ܙ[ܐܫܝܵܐ
0 :1:00 ܐܧܝ وغيرها كثارة كلها لغات في القلخم 35 0
العظيم من الئاس ܙ[ ܠ ܐܐܝ
» ( اللا ) الداهي المفلس 4 ܨ
290 معرب عن الردعي ܐ }| : وهو 7 90 يعنى الصغير ܗ
36 :1 0 < ܕܬܐ ܨ 5
لقاش ± 0 قصير ܘ وكل طويل احمق
(القلع ) معدن ينْسّب ال
======== leaf 129
ܗ ]1 كم
مف را 9 والقجّة ٠‏ ومنة التري كله " القئة فعر بة عن اليوناني
»سن أو عن ܐܒܝܨܢ :01111
١ 1‏ الث ) الخاربة 11 وهو التتصير. والمارية هريب
اروي 1 نيت
ذالتلدسر 1 ܐ ܐܝܝ »)0 بعنى 07 33 $
وقول 1 4 »ܗ ܝ ` 0¢01811002 اقرب الى
ܐܟ 00:59 تكون معر بة عن الفارسي 0 رك و لشاف
رأئن وهن يوش 5 ولمل الاجد راان يقال ان | ± 0
العامة ܨ 0513 ܨܪ ܡ الفرذي 1ه وعن الفارسي كاله 7 09
ܟܠܘܬܐ بالسرياشّة الدارجة
+ (المَلَهان») الرجل الطويل ٠١و‏ (التَأْهب» الرجل القويم الضخم ٠ ٠‏ و( | )
الرجل الضخم ` عو( القليبئع) المسيم المرتفع ܒ ذلك مثحق عن كله
ܬ وهو 60 زم كله اي "رام د
9( لاس ܢ من كأن اي قوس ومن كير اي ماسسك ٠‏ ܕ ]̈ܣ ܐ(
ايض لغتان فيه
5 ( القَمْطَرير) من ܣ( الشديد ܟܐܢ معرب عن خم اريك ومعناه قببة
الللام
, ( القَمَه ) 20 الشهوة الطعام مأخوذ عن "كي ܝ الثيء القليل
2 ( القنهدة الرجل 21 الاصل معرب 1 ليم حقبقة
( || ܡ ݀ܫ ® ܘܬܬ ܐ يافى ܩܢܦܐ ومن السريالى مأخوذ ܐܐܝܕ
20100 ܐܨ 598 وهر :224111 بالفرنسة و 31724 ܐܠ ܐ| ;
ܕ 11011 3 ®
======== leaf 130
}¥ ܙ -
الصوت والعظ 005 30( إما ܣܠ وهو الفيل العظم <
كانوا يشدون اسلحة على خرطومه فيقودونة الى 3 او عن حوره ومعناها
الذروة
20د 01وج الشكر أذا جد معرب كند وهو قصب ܗ= وه
الككردي ܗ
» (المنْد) تمريب 'كند
00107 إل الت التستاى <العرق :2ه ).: «التتداو والنسداة
5 في كل "ذلك الييند أن معرب 0 :3 ?3
- على الها معر بة غرابة < 0 ܪ عن ܘ لهذه الالفاظ
من المعالي الكثيرة 50 السئ الغذاء 5 الخلق والغليظط ܠ
الرجال وقيل هو الكبير العظي الرأس الصغير الل م الهزول :0 :8
لمقدم والقصير العنق الشديد 0 س ٠‏ وقيل هو 00 والصلب. ٠ ٠‏ وخلاصة الى
راحقة كايا الى معنى الكلمة المونامة ܝ يننا 00 والمد. مر واللصض
والداهية وامري || لخو 0 5 ع ܘ ܪ ܐ من التصحيف فان الستداو
صقت | 37 والسندر والسندري » . .قلت ܕܠ ܟ ان القددأو 1:5
والعندأوَ مشتقّة من الفارسي ܨ ومعناه الغليظ الضخم 03906 2030
فقل ان القندأوَ + الغليظ والسئ 2 الخ معرب عن > 502 ؛ القدم
ܝܢ ܘ و 0 اميا ا مشجيع ٠‏ .1 ابرق 50 10700
تمعربة 95 ومعناه املف 05
0 -_- فس < تكلب لاه
======== leaf 131
ܡ ري شد
وفتح 5 التكلى يقال له ® ܢܗܟ ( 90 5 9 2 <
ܡܪ 2 قاجا لضن ܚܐܒ ܚ بكرن سكن ܟܬܐ 7 : وهو توغان
3230 206 9 0( 16( 97590 037 11595
0( تولّد الذكور .وأ كل ( 6 3 5( الاناث ٠‏ واليابس
ܘܠܦ قاطع الشهوة ٠والطري‏ مورث ܐܢܘܐ ܘܬܐ كان في كل ܚܠܘ ܚܪܝܐ ويضعفان
بالمناوبة 20 4 العرب بقاتل اخيه ».قال ايضأ في ترجمة كندبيدستر : حكند هي
5 5( مالي يقال 4 قندز 35 ني ماده 1 وان
خضيتةُ تدخل في الأدوية وهي معروفة بتندز حايدسى ويقال لها بالعر يّة خصية
ܨ .
( | ܘܡ ) العجوزء و( العَندَفيل ) الضخهم !ܕ الضخمة الراس من النوق معربان
0 ܠܐܘ دير ومعنى كنده ܣܒ ومغنى دير ܇ ܐܗܘ او العدوز
* (القَنْدَل والقتَادل والقَنْدويل ) ܐܝܐ الراس من الاوبل والدوات (القاموسش) :
وفي اللسان:« القندل بوزن جعفر الطويل ٠»‏ وهذا أصح لاله تعريب كندواله وفعناة
الشات القوى الطويل
# ( | ) 0 ْ الخلق وقيل الشرس الصعب من كل شثيء رتب كتوزه
ܢܝܫ اتكار الال
| ) الخنشة يعاق عليها القصصاب الحم مغرب 4( ܀ ٠‏ ܙܝܐ( $( فنها
( المهرمآن ) 6 53907 ومعناه الآمر صاحب )
======== leaf 132
ܢ ܗܙ ܝܝ
660 ܣ 70 2 7 75:35 20
0 _ +> ال 40016 معرب 6.076
73 ܙܝ حاروان والفرشي 1376 ¢ ܥ | الى 200124
و الاتكليزي 00011 والالالي 6 ܕ ܐܠܐܘ سس سم رما والعر يي
ܣ 391 والسر ܠܐܠ الدارج جذهى .وام | ܐ فعربة عن ܩܦܠܐ
بالارامسة
باب الكاف
6
1:
( ܐܐܟ ) اي القدح وهو بالفارسيّة كاه وبالاراميّة ܟܣܐ وبالباباية
65 3 6 ` ¬ وبالكردية كاسك اظن انْ 3 097
الاصل ماخردة من . ܦܣܐ ܠܐܐ ܠܟ سب النسمية ظاهر .0 الكرز ذهر
ܘܡ{ ٠‏ فتكون الفارسية قذ اخذت من اللغات السامة كه :3 نا
413 ® ܟܘܙܐ بالسر ܐܸܝ واامابامة ٠‏ و يقرب ܟܣܐ 1 اه
0 ܕܐ 3 واأر دعي عتلى :
* (آلكنابة) دواء صيني فارسلتة كا به . قال في ܫܐ )5 بد على
وزن ܐܢܬ دواء معروف و سسميه البعض كا به مه ويقال 4 ܝܚ حب 3 .
واحسنة الذي ܐܝܢ من ܥܨ يرة شلاهاط من جزائر الصين و يسمِيه البعض ܫ
 ( °‏ )ܒ )
00 0.0 95 9 وهر 79959 9505 0:75
ܪ ܥ 20015 والاتكايزي 1ه والفرنسى اع لمق
======== leaf 133
1 ܢ
+ ( ܬܐܨ والخاصة ) من الابل ܥܪܐ ܙ ܐܬܐ القوي الشديد تعريب
كيز
(الكبكج )نت قصيز الساق كثير (53[9ً(0005::3 350
( حيط الحيط ) ٠‏ فارسيتة ܦܥ . قال في البرهان القاط لع : حكبيكج ضرب من
الككرفس البري يقال له 93 السبع وشجر الضفادع ٠‏ ويستى في شإراز
« كس وبران» وفي اصفهان « موسك › - ܕ ܐ 4 70 ; « ܬ ܚܝܕ | ܫ
ويرتجيار اياسى ودوكون جيجكى وقور بغه اولى ودوكرن اولى ٠»‏ والنبات 1 ܨ
لا ن هذا الضرب وهو من )ܐ.ܕ 15 وطلاه مع الخل يتداوى به من داء
الثعلب ٠‏ قيل ان كبيكيم بالسر يانّة امم 0 الحشرات »٠لا‏ بوجد
كذا كلمة بالسر 5
كر كل )00 بالحندب. والحندب قيل هو الصغير من 070 غير
ܬ( للملا تل الكبُوتل قريب لفظا من 9 وامله |
0 0 #اتتملى 05 15.2 ٠وقيل‏ هو الملك
الخزرين وقيل دودة كبيرة تعش في الماء تن هارا وتظهر ليلا وتكل )0 من
السمك ( | )ܬܐ لقاطم »
. 3 ننت ييخلط بالمناء وبيخضب به الشعر فيبقى اونة واصلة اذا طبخ
بالماء كان ܘܬܘ مداد نالكتابة وف ܩ دفي كتب الطب مين 1 ܬ
62 الاس © به مدقوقاً 100 ܨܒ اذا نضج وقد ܒ
:4 دفن ܐ̈ܝ
```


## [2026-09-05T20:36:10.180Z] TOOL CALL #20: Bash

```json
{
 "command": "sed -n '1,80p' tools/ref_page.py",
 "description": "Read ref_page.py"
}
```


### [2026-09-05T20:36:10.218Z] TOOL RESULT

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
    else:
        print(f"no scan of {abbr} covers printed page {page} (see 'scans' in refs_online.json)"); return 1
    pdf = scan["file"] if os.path.isabs(scan["file"]) else os.path.join(REFS, scan["file"])
    if not os.path.exists(pdf):
        print("PDF not found:", pdf); return 1
    lang = scan.get("lang", "fas")
    out_dir = os.path.join(OCR, abbr + vol)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"{page:04d}")
    png, txt = base + ".png", base + ".txt"
    if not os.path.exists(png):
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", pdf, base], check=True)
    if not os.path.exists(txt):
        # try the PDF's own text layer first; fall back to tesseract
        r = subprocess.run(["pdftotext", "-layout", "-f", str(pdf_page), "-l", str(pdf_page), pdf, "-"], capture_output=True, text=True)
        text = r.stdout if len(r.stdout.strip()) > 80 else ""
        if not text:
            env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
            r = subprocess.run(["tesseract", png, "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
            text = r.stdout
```


## [2026-09-05T20:36:16.121Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(d):\n    for m in re.finditer(r'قب', p):\n        print(i, repr(p[max(0,m.start()-40):m.start()+60].replace('\\n',' ')))\nEOF",
 "description": "Search AFM for qb sequences"
}
```


### [2026-09-05T20:36:17.868Z] TOOL RESULT

```
4 ' فان ماً وجذاماً كانوا حاورين لاهل | والقبط ٠\u200f وقضاعة وغسان واياد كانوا منتلطين مع الاراميين والعبرا'
4 '( ܚ ° ± ٠\u200f ولس ܳܐ 3 المجاودة للفرس بل القبائل البعيدة )37 70.39 حلمها حص تال ܚ في شفاء الغليل :« بال'
19 ' .و يقال وقعوا في ÷ ܟܢ وبرخاس ( البريد) قبل اصله متا" 80 0360 5 85 ܙܥ̈ܝܐ. - وقبل ܓ اصلة 35 وهو دابة '
19 'د) قبل اصله متا" 80 0360 5 85 ܙܥ̈ܝܐ. - وقبل ܓ اصلة 35 وهو دابة |« ܢܐܝ ( الاب ميسن في كتاب العروق ) ܀'
24 'جل 2 في القاموس سجيتة مشتق :1 ܒܝ 2 3 المقبول 005 ` 0 ردت'
25 ' في الني لطر ير الي 4 مشتق من ياد وهو القبيح النظر ܝ * (التَطْريق » الرجل الخال مزهو .و( الاق الرجل '
32 'لو 0 سفت ܐܵܝ 2466 ܨܚ في 11114 ضأن 2 305 قبل 4 )ܥ 0 يالب من مديئة در بند وهو العروف عند الأطاء بشالي '
42 'ره اهل القرية لما ينوبهم من تفقات من 46 قبا السلطات معرب كزير. ومنة ܓܰܙܝܪܐ ܨ ركز ير بالتركيّة ܐ 000 '
47 'على حصان قوي عظي | (الجَهبلة » المرأة القبيحة تمري ب ܐܢ اي الأحق الثقيل ( الجهاركاه ) اللحن الرابع م'
49 'َوَرَب) .231 2 تعرينت #وديا دا مف دا اي قبر الرجل ٠\u200f < ܥ 208 ܐܘ ܨ | الدارج ܓܘܪܒܐ + (الأورس) ماخوذ من'
53 ' بلمه وقرهجه اوت ٠»\u200f وا كان تناول 579 5 قبل .2 353 8 0 ± 2 قوردبوغان » ( ارربيل ) الممقاء او العجوز '
55 ' ٠ ٠\u200f وف حديث علي لى نعى عن ركوب 5 عليه قبل اراد به 9 ܠ 04381 ܐ وهر المصنوع ܝ 7245 07 سم دابة ثم سني'
65 ' » © 33 06 0 وهي العطية والاجرة المعطاة قبل العمل : » (الدَستَفْمار) العمل اليد ܐܬܫܩ باليد مركب من د'
65 '.\u200f وام صحراء بتركستان دهي معردفة ܕܐ ܚ̈ܝ قبجاق واسم قرية من قرى اصفهان ٠\u200f واسم مكان في شيراز وهو المع'
67 'انة ) زجاجة كيايرة واسعة اللوف ܟܩ العنق قبل فارسسّة ونم أجدها 01 0 وَالدمازة) الهلاك ٠\u200f ܘܐܬ 4 1065 و'
70 ' عن الداهية والموت فأطلق ` (الداماً ) 0 قبل ® والاصح 5 5 + (الديك) 3 بالاثافي ܙ ܐܝܐ ععنى ديك افاسي و'
74 "ر البادية دقل هو الا ܝܨ¿ ܪܝܐ[ الفار وقد قبل العود الذي ' 9 به في الصحاح : قال الأصيي ورم شِجوا إل كه"
75 ' /\u200f ܘ 3( ܀܀ .\u202b . ܀ ܨ 7 سكوت » زهره يظهر قبل ورقه وهو قدر البلوط اصفر احمر اسود ابيض 2" الرانحة كثيرً'
75 'دي رَهوال * (الروند والريوند والراوند ) قبل 0 اصل 309 في الصين وقيل اصل 441 المندى 2 راوند وهو اصل ܬ'
81 'ومنة 4 ܐ ܙܘܢܓܦܪ السفق فيها ثقت وهى 0 55 قبل زئذان -فارميية زند وهر التود الأعلى : :ܣ « يازند ». وزند'
82 ' 010 الرنذ” 50 :في كتات الأ بستا ܩܘ حيث قبل :2 اننا ܣܠ الصلاة٠ ٠0\u200f تكى ارب الزنده ܀ وخر .هما جميعاً '
84 '0742 ٠وهو\u200f نوعان ٠\u200f نوع ܚܝ موجود في دست قبجاق (في تركستان) وهو في الأصل ماء 2 ܧܥ . والنوع الشالي معد'
86 'يد 5 ينوا ` 00 ܨ بيه ول لوا قا 1 9 ® ات قبل معرابة 917 000 9 3 الغليل) : ܣܡܘ 5 مقطوعة ¶( 62 ܨܒ تقد ܝ'
87 'ر. وقيل له سددير لانه كان في داخله ثلاث قبب فان ܕܨ باللفة المهاوة معناها القيّة 9 في مادة ` ± على وز'
89 'سه اي ثلاثة ومن دل اي وسط اومن دير اي القبّة ٠\u200f او هو ` 3 0 السداي والسد اف 6 لنت شارف عت رمات ل 11 '
94 'عر بة عن ٠\u200f ܨܘ واصل معناها أرجلها في الثقب ٠\u200f وفيها اغات السَلَحَنَى والسلْحفى والساحفاء 0 م 001 5 ب'
102 'ك فى لكان انوشروان وان وذ بره بإد#هر ܠܝ قبالتها لعبة الترد ܝܨ معروفة ٠\u200f والشطرنج معرب 29 سترنك ٠\u200f وق'
102 'الزهر وفي وسط زهره زُغب يضرب الى الصفرة قبل انه افع من | لصرع ٠\u200f ܝ 4 بالتركة 1 # (الشتن) فشر بضرب من'
104 'صغ به اليد اذا مستة + 10( فاسي محض وهو اقبح العيب والعارء وقالوا فيه 3 = الى غير ذلك + ( 5 3 55 السئ'
105 '› !ܐ رياأا ويقال له بالعربّة ضميران ٠\u200f وقبل ان سبب ظلهوره كان ان ,انوشروان ينما كن برها جالساً على س'
112 '( الطدس ) ܆ دون كل نشوىء تعر يب مت اي القبيح 0 ܟ 7 دواء 8 في حوف القنا المندي اوهو رماد ܟܕܬ | معرب 3'
114 "ور 0 5 © 3 7 ¥ $ ' الاسبانية ( الس ؟ 55 قبل “فارسكة الأصل لا واحد لها يقال الناس 3 5 اي ܟܝܝܨܬܰܢ ( حي"
119 ' وهو 3 117 الذى 0 ܨ( ( الرغيف سقط £ 31 وقبل فتات اير وقيل قطع العجين. ٠\u200f فيل 36 مسرت من كران وذ والا'
124 'شجيع : ` والقامة ومن وس اداة التشيه ( القباط والقبئْط والقتيطاء 06 0 تمر د 0 | وهر نوع من ܐܠܐ ܨܒ يصن'
124 ' والقامة ومن وس اداة التشيه ( القباط والقبئْط والقتيطاء 06 0 تمر د 0 | وهر نوع من ܐܠܐ ܨܒ يصنّع من ال'
125 'ة أو الدروع الغليظة او الغفر له بيضة أو قباء بحشو ( ܬܐ َّ الغليل ) ( ܨܢ( 7 ا 0 لطو دل مر مت من لخر ا'
126 ' نحت الدرع ( ` ( > 30300 إيشد في الوسط وقبل كوسند للشاة ݀_ 00 040 ܒܘܝܐ ܘܕܬ ܐܦ ܘܗܝ ( ܟܠܐ والقَسْطر) ا'
129 'من ܣ( الشديد ܟܐܢ معرب عن خم اريك ومعناه قببة الللام , ( القَمَه ) 20 الشهوة الطعام مأخوذ عن "كي ܝ ال'
129 ' 2 ( القنهدة الرجل 21 الاصل معرب 1 ليم حقبقة ( || ܡ ݀ܫ ® ܘܬܬ ܐ يافى ܩܢܦܐ ومن السريالى مأخوذ ܐܐܝܕ 201'
138 'ن حديد ܓ 9 3( ܓ < وهنه ܬܝ ܥ » 350 )ܝ اياقب في انبر ,0003 54450 - ` © 50 )ܐܢ 39 ܛܘܦܐ × 0 القطعة ܐܐܳܐܬ'
145 'عرلي الأروح 15 صغار ,+ شيل كيار الدر ܡ وقبل 2 جان 1 , 0 : وقال 3990 لا ܨ تانق هو ام م داعي ܨ تقدير ز'
150 ' 6( بالياء 9 بهمزة ܓ 5( فيها الماء والمثقب ويقال 2 وصفها ابن السكيت والفراء وابو حاتم ٠\u200f وفي التهذيب'
152 'فقيل 1 ( حيط المحيط ) ٠\u200f 0 هو وضع زرجهر قبل لا بل اقدم منه والترد عبارة ܧ عن سبع ܐܐ وهي بالفارسية فا'
152 'ܐ 2 ܝ بوم جديل ٠ورمًا\u200f ܡ 4 بوم فرح 0039 قبل ܨ الى علي شي ء من 592 0 0( للنيروز: فقال ܓ 9 16 بوم ٠\u200f د'
158 'سب ¥ © |{ ܗ 0 قبل ܟܪ ܀ ܫ )1:1 ܥ وهم || ܡ . ٠وقبل\u200f عظلاء ٠\u200f ܐܩܝ وقيل ܢܣ وقب'
158 '© |{ ܗ 0 قبل ܟܪ ܀ ܫ )1:1 ܥ وهم || ܡ . ٠وقبل\u200f عظلاء ٠\u200f ܐܩܝ وقيل ܢܣ وقبل ܗ نار الأجوس الواحد هر ربد ( '
158 'وهم || ܡ . ٠وقبل\u200f عظلاء ٠\u200f ܐܩܝ وقيل ܢܣ وقبل ܗ نار الأجوس الواحد هر ربد ( حيط المحدظ ) ٠\u200f والمعنى الا'
180 'ا 7 ساييالى فسلكن بي تمك اإعاس و5 سموزر قبق ١١+\u200f سموزلك اولى وس ܫ ܕܢ وه سندان 5ه 0 ܡ ܡܢ + شافول شاهو'
```


## [2026-09-05T20:36:34.356Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA (Asbaghi) ===\"; grep -n \"qubba\\|Qubba\\|kubba\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20\necho \"=== AFA (Fraenkel) qubba ===\"; grep -n \"qubba\\|Kubba\\|Kuppe\" AFA.txt | head -20\necho \"=== FVQ ===\"; grep -n -i \"qubba\" FVQ_pages.txt | head\necho \"=== TAD ===\"; grep -n \"القبة\\|قبة\" TAD_pages.txt | head",
 "description": "Grep Asbaghi, Fraenkel, Jeffery, Unaysi"
}
```


### [2026-09-05T20:36:34.441Z] TOOL RESULT

```
=== PLA (Asbaghi) ===
=== AFA (Fraenkel) qubba ===
9596:lASiO >Ei** dann »Kuppel" entspricht arabischem L^Ij ,
=== FVQ ===
=== TAD ===
647: ‫بيقة والعامة تقول بأقبة ‏ يوناني داعااط وفي اللانينية ‪ 2017‬وهي الكرسة‬
1874: ‫ءا املناوقبة وقد بزن فلسين وني زماننا هو جزء من كيلوغرام أي من‬
```


## [2026-09-05T20:36:40.404Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA context ===\"; sed -n '9585,9605p' AFA.txt\necho \"=== LKT qubba ===\"; grep -n -i \"qubba\\|alkoven\\|alcoba\" LKT.txt | head -20\necho \"=== DEV alcove ===\"; grep -n -i \"alcôve\\|alcove\" DEV.txt PHN.txt LAM.txt DOZ.txt | head -20",
 "description": "Fraenkel context, Lokotsch, French Arabists"
}
```


### [2026-09-05T20:36:40.485Z] TOOL RESULT

```
=== AFA context ===
mek^^räb Dillmann 836 übernommen ist. Nur bei der
Annahme einer Entlehnung ist die Möglichkeit da, die Ab-
weichung Yon der üblichen Lautentsprechung zu erklären.
Dann ist natürlich auch nicht mit Dillmann mek^^räb
zur arab. Wurzel V;^ zu ziehen, deren einziges hierher
gehöriges Derirat eben t^Ls^uo ist, sondern \^\y^jf ge-
hört zur äthiop. und arab. Wurzel v^«5^ zu der yermuthlich
auch 0^3113 zu stellen ist.
Die Kirche LLu Agäni IH. 16, 12; Y. 142, 5 a. f.;
XV. 7, 5a.f:; XV. 133,7; Div. Hud. 3,5 ist schon durch
die Lautrerschiebung als aramäisch gesichert» Denn aram.
lASiO >Ei** dann »Kuppel" entspricht arabischem L^Ij ,
also muss &juj fremd sein.
"- s
[Wohl nur missbräuchlich findet sich JSjuj einmal (Agäni
XIX. 97 , 11 a. f.) Ton einem jüdischen Bethause gebraucht.]
Natürlich ist auch (}X2i als »Kirche**, wie es yon A^iä
ZDMG. XXXIII. 216; ^Antara Appendix 16, 3 gebraucht
wird , sicher erst aus ILa^oi übernommen. Ich möchte aber
glauben, dass dies Wort überhaupt nicht arabisch ist,
sondern ursprünglich »grosses Gebäude** bedeutete, und so
=== LKT qubba ===
1973:'Großer  Bogen,  Gewölbe';  hieraus  mit ar.  Art.  sp.  alhania  'Alkoven,  Nische zum  Schlafen'  [wie  bereits  in  den  ar. Häusern  Spaniens,  vgl.  Graf  Schack, Poesie  und  Kunst  in  Spanien  und  Sizilieu.
2867:in  Nordafrika,  mit  dem  Grabe  eines Heiligen,  frz.  irrtümlicli  marabout,  s.  hier Nr.  141U,  genannt]';  hieraus  zum  Teil mit  ar.  Art.  sp.  alcoba,  pg.  alcova  'Schlaf- kabinett', kat.  alcova,  prov.  alcuba  'Zelt', afrz.  aucnbe  'dass.',  frz.  alcdve  'kleines Nebenzimmer',  rum.  alcove;  siz.  cnbba 'Wasserturm',  sp.  alcubilla  'dass.';  mit romanischer  Demin.-Endung  it.  ctipola, frz.  coiipole.  Dtsch.  Alkoven,  Ktqypel, mhd.  ekub  'Zelt'  [bei  WOLFRAM  VON ESCHENBACH],  ndl.  alkoof,  engl,  alcove 'Zimmervvinkei  für  Sitz  oder  Bett'  [m einem  Zimmer  oder  einer  Bibliothek].. Bulg.  kube,  serb.  kube,  kuba  'Kuppel, Gewölbe',  russ.  alkow  'Alkoven';  über vulg.  ar.  kiibbat,  kas.-tat.  kibbet,  kirgis. kibü  wurde  russ.  kibitka  'Verdeck  über einem  russ.  Wagen,  halbverdecktes  russ. Fuhrwerk'.  —  Auf  die  vulg.  Form  ar. kubbäja  'Glas  zum  Trinken'  geht  viel- leicht siz.  ciibbäita  'Art  Mandelkuchen aus  geriebenen  Apfelsinenschalen,  Honig, Karamel!'  usw.  zurück  [wegen  der  zylin- drischen Form;  vielleicht  auch  vom  ar. kubbait  'Mandelkuchen',  vgl.  Dozy  Suppl s.  V.  kubbat].  Als  Eigenname  hat  sich in  Palermo  für  ein  sarazenisches  Gebäude der  Name  La  Ctiba  erhalten  [vgl.  Schack, Poesie  und  Kunst  der  Araber  in  Spanien und  Sizilien.  ^.  II,  266/269].  —  [Mög- licherweise geht  das  ar.  Grundwort  selbst auf  pers.  gunbäd  zurück,  ZDMG  L,  646.] [Kluge  11.  DE  90/91.  95.  Eguilaz  131. Devic  DEt  14.  Lammens  Rem  8.  ML 6909.  Hobson-Jobson  11/12.  Gorjajew 4  und  139.  Bern  SlEtWb  635.  GrS VociSic  232/233.
5708:.4?awrtc  St.  75 Albatros  1)88 Alchabor  St.  12 Alchimie  1157 Aldebaran  St.  451 Aleppin  792 Algebar  St.  629 Algebra  631 Algedi  St.  035 Algenib  St.  664 Algomeiza  St.  749 ^Z^^oZ  St.  741 Algorab  St.  754 Alhabor  St.  12 Alhajoth  St.  41 Alhidade  896 Alizarin  116 Alkakandschi  1016 ^ZA-«?i  1029 ^/fro/io?  1227 Alkoran  1250 Alkoven  1221 ^/^«/t  59 Alleluja  793 alligaßr  mhd.  2229 Abnagest  1348 Almanach  1389 Almemor  j.  1461  a Alphard  St.  587 Alpherath  St.  586 Alpheraz  St.  586 Alpheta  St.  574 ^/<«/r  St.  1575
=== DEV alcove ===
LAM.txt:216:mots espagnols dérivés de Tarabe); v dans alcôve ^ a-
LAM.txt:852:qui vient probablement de la même source que alcôve.
LAM.txt:871:valu : almagra (i), alcôve etc. Il n'y a d'exception que
LAM.txt:1372:Alcôve. Esp, et Ptg: alcoba. Cat. Major q. et Ptg :
LAM.txt:7862:Alcôve. Dans le passage arabe cité, traduisez : «sous
LAM.txt:7865:couverte: Mas'oûdî VII. 108. Quant au sens d'alcôve,
LAM.txt:7867:l^iVI •ti^b .-ImôIIc^ ^j-KV ; il avait une alcôve d'hiver
LAM.txt:7869:Loir [Voyage du Levant p. 70) parle des alcôves con-
LAM.txt:8311:Alcôve
DEV.txt:366:AlcÔve.   Esp.  alcoba,  portug.  alcova,  ital.  alcova,  alcovo;
DEV.txt:2480:Alcoba,  esp.  voy.  Alcôve.
DEV.txt:2490:Alcova,  pg.  ital.  voy.  Alcôve.
DEV.txt:2491:Alcôve.
DEV.txt:2492:Alcovo ,  ital.  voy.  Alcôve.
DEV.txt:3767:Kubbe,  voy.  Alcôve.
DEV.txt:4994:*^  voy.  Alcôve.
PHN.txt:1231:ALCÔVE, s. f. (a.)
PHN.txt:1239:akovo et ie français alcôve,
PHN.txt:1673:empruntés à l'arabe , tels que alcôve, algarade, etc. , cet article
PHN.txt:2163:tels que alcohol, alcôve, a^èbre, etc., cheval qui porte des alzanes
```


## [2026-09-05T20:36:48.573Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 2860-2870 ===\"; sed -n '2860,2868p' LKT.txt\necho \"=== DEV 360-380 ===\"; sed -n '360,385p' DEV.txt\necho \"=== PHN 1225,1245 ===\"; sed -n '1225,1245p' PHN.txt\necho \"=== LAM 1370,1385 ===\"; sed -n '1368,1385p' LAM.txt",
 "description": "Read alcove entries in Lokotsch, Devic, Pihan, Lammens"
}
```


### [2026-09-05T20:36:48.645Z] TOOL RESULT

```
=== LKT 2860-2870 ===
1220.  Ar.  Krümlr:
N.  pr.,  vulg.  Aussprache  von  'humair, einer  berüchtigten  Mischbevölkerung  an der  Grenze  von  Tunesien  und  Algerien, teils  Araber,  teils  Berber.  Ihre  Züge über  die  Grenze  Algeriens  waren  be- kanntlich für  die  Franzosen  der  Vor  wand, im  März  1881  eine  Expedition  nach Tunesien  vorzunehmen  und  dieses  Land besetzt  zu  halten  [vgl.  Rudolf  Fitzner, Die  Regentschaft  Tunis.  Berlin  1895. S.  349].  Hieraus  ergibt  sich  frz.  kroumir 'roher  Kerl,  Pfuscher,  Streikbrecher', it.  crumiro  'Streikbrecher'.
1221.  Ar.  kubba:
'Gewölbe',  jedes  gewölbte  Gebäude,  also 'Zelt,  Nebenzimmer,  Grabkapelle  [bes.
7
Ar.  kubti.]
98
in  Nordafrika,  mit  dem  Grabe  eines Heiligen,  frz.  irrtümlicli  marabout,  s.  hier Nr.  141U,  genannt]';  hieraus  zum  Teil mit  ar.  Art.  sp.  alcoba,  pg.  alcova  'Schlaf- kabinett', kat.  alcova,  prov.  alcuba  'Zelt', afrz.  aucnbe  'dass.',  frz.  alcdve  'kleines Nebenzimmer',  rum.  alcove;  siz.  cnbba 'Wasserturm',  sp.  alcubilla  'dass.';  mit romanischer  Demin.-Endung  it.  ctipola, frz.  coiipole.  Dtsch.  Alkoven,  Ktqypel, mhd.  ekub  'Zelt'  [bei  WOLFRAM  VON ESCHENBACH],  ndl.  alkoof,  engl,  alcove 'Zimmervvinkei  für  Sitz  oder  Bett'  [m einem  Zimmer  oder  einer  Bibliothek].. Bulg.  kube,  serb.  kube,  kuba  'Kuppel, Gewölbe',  russ.  alkow  'Alkoven';  über vulg.  ar.  kiibbat,  kas.-tat.  kibbet,  kirgis. kibü  wurde  russ.  kibitka  'Verdeck  über einem  russ.  Wagen,  halbverdecktes  russ. Fuhrwerk'.  —  Auf  die  vulg.  Form  ar. kubbäja  'Glas  zum  Trinken'  geht  viel- leicht siz.  ciibbäita  'Art  Mandelkuchen aus  geriebenen  Apfelsinenschalen,  Honig, Karamel!'  usw.  zurück  [wegen  der  zylin- drischen Form;  vielleicht  auch  vom  ar. kubbait  'Mandelkuchen',  vgl.  Dozy  Suppl s.  V.  kubbat].  Als  Eigenname  hat  sich in  Palermo  für  ein  sarazenisches  Gebäude der  Name  La  Ctiba  erhalten  [vgl.  Schack, Poesie  und  Kunst  der  Araber  in  Spanien und  Sizilien.  ^.  II,  266/269].  —  [Mög- licherweise geht  das  ar.  Grundwort  selbst auf  pers.  gunbäd  zurück,  ZDMG  L,  646.] [Kluge  11.  DE  90/91.  95.  Eguilaz  131. Devic  DEt  14.  Lammens  Rem  8.  ML 6909.  Hobson-Jobson  11/12.  Gorjajew 4  und  139.  Bern  SlEtWb  635.  GrS VociSic  232/233.
1222.  Ar.  kubtl:
=== DEV 360-380 ===
^  Ou  plutôt  de  sulfure  de  plomb.  (Voy.  Alquifoux.)  Le  cobeul,  en  Perso et  en  Turquie,  est  souvent  appelé  a«.™w  mrmeh,  mot  quelquefois  employé dans  les  relations  des  voyageurs  français.
■'   Pharmacopée  royale,  a'édit.  1682,  l.  P',  p.  3i',.
■■  Lexicoii  alch eniia.'  {iGHii),  p.  3o.
\U  DICTIONNAIRE  ETyMOLO(iIQUE
Alcohan.  Transcription  de  l'aral)c  ^^yt^^  al-qorân.  Al est  l'article;  aussi  dit-on  de  préférence  aujourd'hui  1r Coran.  (jUi  qorân  signiCie  proprement  lecture,  récitation. ^Le  Coran,  dans  sa  forme  primitive,  était  une  récita- tion plutôt  qu'une  lectm^e,  et   c'est   dans  ce  sens   qu'il
faut  entendre  le  verbe  i^Jj  qaraa^  dans  plusieurs  des  pas- sages où  on  l'a  traduit  par  lire.  ?5  (E.  Renan  ^)
AlcÔve.   Esp.  alcoba,  portug.  alcova,  ital.  alcova,  alcovo;
de  l'arabe  aIaJ!  al-qohha,  qui,  entre  autres  sens,  a  celui de  petite  chambre,  cabinet,  ainsi  que  le  montre  M.  Lane (jTAc  thousand  and  one  Nights,  I,  281).  Voir  l'intéressant article  de  M.  Dozy,  Gloss.  p.  90,  ()i.  Le  mot  est  employé avec  son  sens  le  plus  ordinaire  dans  ce  passage  de  Niebuhr  : t^Les  derniers  seigneurs  de  Taœs.  .  .  ont  bâli  de  beaux palais  pour  eux  et  leur  postérité,  et  se  sont  contentés  d'un petit  kubhe  pour  leur  servir  d'oratoire  et  de  sépulture  -.  v
Aldécar/Vn.  Nom  d'une  étoile  brillante  de  la  constella- tion du  Taureau.  C'est  l'arabe  ^^!jj*xJ1  al-deharân^.  Elle  est comptée,  par  Alfergani,  parmi  les  quinze  étoiles  de  pre- mière grandeur  :  ^y.\\  ^^j^  J.s.  (^*x]1  j^^^  (^^\  ;^iii  j,^ ^j!w*>Jî  is^^^.^  ç^Dans  le  (signe  du)  Taureau,  l'étoile  rouge qui  est  sur  l'œil  du  Taureau  et  qu'on  nomme  ad-debarân^.  5' Dans  le  commentaire  des  Séances  d'Ahmed  ben  al-Moàddem^, le    mot  est  ainsi   expliqué  :    bJJi  »;^*>J  (jV*^^^  ^  *^*  ^
'  Hist.  des  tangues  sémit.  W  édit.  t.  I*',  p.  306.
'■^   Voy.  en  Arab.  édit.  Smilh,  p.  28/1.
^  La  prononciation  arabe  serait  ad-detjaràn ;  mais  il  arrive  cpioltpiefois, dans  le  passajjo  de  Tarahc  aux  lanfrncs  romanes,  que  le  /  de  Tarlide  al  ne s'assimile  pas  à  la  lettre  solaire  suivante,  surtout  quand  le  mot  est,  comme ici,  un  terme  purement  scientifique.
''  Edit.  de  Golius,  p.  76.
•''  JjOS  douze  séances  du  clieikii  Almied  ben  al-Moa'ddom .  notées  et  pu- bliées par  Soliman  al-lJaraïri ,  p.  r,  note  10.
DES  MOTS  D'ORIGINE  ORIENTALE.  15
c^Elle  est  ainsi  iiomiiioe  parce  qu'elle  vient  derrière  les Pléiades.  51  o^  iJahar,  en  effet,  signifie  venir  derrière ,  suivre. Toutes  les  étoiles  qui  viennent  derrière  une  constellation, ajoute  naïvement  le  commentateur,  n'ont  pas  reçu  ce  nom de  Dcbaran;  mais  les  Arabes  Font  ainsi  appelée  en  parti- culier, de  même  que  les  Pléiades  ont  été  plus  particuliè- rement désignées  sous  le  nom  de  a^I^  an-noucljoum ,  les étoiles.  On  peut  lire  la  même  explication  dans  l'ouvrage intitulé  Eplieinericles  Persanim,  de  Math.  Frider.  Beckius,
1  ()(jG,p.  9i?.
Aldée.  Esp.  aldea,  portug.  aldea,  aldeia;  de  l'arabe iixjj^\  ad-day'a,  ferme,  bourgade.  Le  /de  l'article  ne  s'est pas  assimilé  à  la  lettre  suivante,  ce  qui  peut  t(3nir  ici  à  la prononciation  emphatique  du  ijo  d,  qui,  dans  les  langues hispaniques,  entraîne  souvent  l'introduction  d'un  /.  (i/- calde,  d-hayalde,  etc.  — Voy.  Alcade,  Abit.)
Alepiine.  Etoffe  qui  tire  son  nom  de  la  ville  d'Alep,  en arabe  c^^Lw  Haleb,  soit  c[ue  le  mot  ait  été  formé  directe- ment en  français,  soit  qu'on  ait  pris  l'adjectif  arabe  (Si^ halehl,  d'xAlep.
Alezan.  Esp.  alazan,  portug.  alazào,  se  dit  d'un  cheval de  couleur  fauve  ou  rougeâtre  plus  ou  moins  foncée.  On a  proposé  (voy.  Littré,  Dict.fr. ^  trois  étymologies  arabes: ^^j^il  al-hasan,  le  beau,  (jUa^:^  al-hisan,  le  cheval  de  race, et  enfin  (^ji*ii  al-athan,  la  fumée.  Aucune  des  trois  ne  me paraît  satisfaisante.  Sans  s'arrêter  à  la  dernière,  qui  me semble  de  pure  fantaisie,  on  peut  dire  des  deux  autres qu'elles  ne  spécifient  point  une  couleur  de  robe;  car  il serait,  croyons-nous,  bien  difficile  de  montrer  que  les Arabes  aient,  à  une  époque  quelconque,  attribué  une  su- périorité de  beauté  ou  de  race  à  l'alezan.  Al-hisan  est  sou-
16  DICTIOiNNAlHE  ETYMOLOGIQUE
vent  pris  pour  ïétalon  par  0])p()silion  à  ^^afaras,  jument, comme  dans  l'exemple  cité  plus  loin.  11  paraît  même qu'au  Magreb  il  se  dit  du  cheval  en  général.  Mais  tout cela  est  sans  rapport  avec  l'adjectif  alezan^  et  M.  Dozy trouve  fort  suspecte  cette  étymologie,  donnée  par  M.  En- gelmann  dans  la  première  édition  de  son  Glossaire^.
Il  y  a  quelques  années,  j'en  ai  proposé  une  quatrième^, acceptée  depuis  par  iM.  Littré  [Addit.  au  Dict.)-,  c'est  l'ad- jectif (j^Àa-i  ahlas,  fém.  halsa,  ç^spadix  equus,?5  disent  les dictionnaires  (voy.  Freytag  au  mot  (j-^^X^w,  9'  forme),  ce que  nous  traduirions  par  cheval  bai  ou  alezan.
Nous  dérivons  notre  mot  français  du  féminin  du  terme arabe  (comme  nous  le  ferons  plus  loin  pour  balzan).  On peut  conjecturer  que  le  féminin  l'a  emporté  sur  le  mas- culin par  suite  d'un  emploi  plus  fréquent  :  le  terme  gé- nérique ^j^^faras,  cheval,  signifie  plus  ordinairement  la jument,  ainsi  que  nous  le  disions  tout  à  l'heure  :  «i^lî  ^ji ^\y^  ^\j>^  J^ft  o^yilî  J^"  Li  J-ç^j-îî  J^  St^  '^  Dans  ce passage,  qu'on  peut  se  dispenser  de  traduire,  ^^  est  dit par  opposition  à  (jl^a^»-.
Quant  il  la  finale  n  qui  s'est  ajoutée  au  mot  halsa,  on en  peut  citer  d'autres  exemples,  tels  que  camocan,  de  [^ kamkhâ;  arduran,  de  l;*xJi  ad-dourâ  (voy.  Doura);  bosan, de  »3^j  bousa;  alchocoden,  de  î^x^^^  ketklioudâ;  azacan (^portenr  d'eau,  en  espagnol),  de  pUuJi  as-saqqâ ,  etc.
Alfânge.  C'est  un  mot  espagnol  introduit  en  France par  nos  écrivains  du  xvif  siècle.  De  l'arabe  jjs^il  al-khan- djar,  sabre ,  que  nous  avons  pris  directement  et  sans  l'ar- ticle, sous  les  formes  cangiar,  khanjar,  khandjar.
=== PHN 1225,1245 ===
et déjà précédés de l'article al. — Une autre irrégularité à la-
quelle il est bien difficile de remédier, c'est de voir le ^ g
rendu en français tantôt par c, tantôt par k ou q; j'ai cru
devoir adopter, à cet égard, la transcription fournie par nos
dictionnaires, quand il ne s'agissait pas d'un équivalent rigou-
reux de l'orthographe orientale.
ALCÔVE, s. f. (a.)
*iM\ [alqoubbat] la coupole, la voûte, et, en général, tout édifice
coMtruit en voûte; se dit aussi d'une tente en peau à l'usage des
Arabes nomades. — Chez nous on appelle akâve un enfonce-
ment réservé dans une chambre à coucher pour y placer un
lit. — Le mot arabe qoubbat, précédé de l'article al, a été
d'abord adopté par les Espagnols avec l'orthographe akoba,22 ALË
et s'est introduit ensuite dans le portugais akava, Titalien
akovo et ie français alcôve,
ALDÉBARAN, n. pr. (a).
^I^«>JI [addébarân] Nom arabe d'une étoile fixe, de première
grandeur, dans l'Œil du Taureau, près des Hyades. — Pour
être correct, on devrait écrire Addébaran, attendu que ie ^ d
qui commence le mot fait partie des quatorze lettres dont on
double la prononciation lorsqu'elles sont précédées de l'ar-
=== LAM 1370,1385 ===
lit dans Cuba ( Hortus sanitatis. 98). Il est cité avec celui
d'Abremon comme un poisson très-soigneux pour ses
petits, qui s'attache aux navires et les rend immobiles».
(Dict. d'hist. nat. I. 2Ç3 ).
Alcôve. Esp, et Ptg: alcoba. Cat. Major q. et Ptg :
alcova. Ba^^' : alcoba. Ital: alcova, alcovo, de i2\alqaoab-
ba, qui signifie dôme, et aussi : petite chambre, cabinet,
pavillon, et même baldaquin, comme dans ce passage du
Kitab Alictifa cité par M. de Eguilaz : « Sur un trône
porté par 3 mules, et sous un baldaquin orné de pierres
précieuses et de saphirs (i). CjMi *!jiC J^ x^r^ J©
. Aldébaran. De ûU ^^ aJdabarân^ étymologie bien con-
nue. «On la nomme dabaran^ parcequ'elle suit les Pléiades.
' >
On la nomme aussi la suivante des Pléiades, \^x^ JL-
^ ^\ «)t ^^^j Wl ©jjiJ^I (Abdurrahman. 1 37) En effet x *^
dabar, signifie venir derrière, suivre. C'est un des rares
• ^_
```


## [2026-09-05T20:36:57.935Z] TOOL CALL #25: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:36:57.942Z] TOOL RESULT

```


```


## [2026-09-05T20:38:10.100Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D8%A8%D8%A9",
 "prompt": "Give the Arabic etymology section for قبة (qubba) — root ق ب ب, meaning dome/vault, and any noted origin (Semitic or Persian loan), plus descendants (Spanish alcoba, French alcôve, English alcove)."
}
```


## [2026-09-05T20:38:11.474Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/alcove",
 "prompt": "Full etymology of \"alcove\": route through French, Spanish, Arabic al-qubbah, and the Arabic verb qubba/qabba. Quote it."
}
```


### [2026-09-05T20:38:15.999Z] TOOL RESULT

```
# Etymology of "Alcove"

The word "alcove" traveled through multiple languages before reaching English. According to the Online Etymology Dictionary, it entered English in the 1670s from French *alcôve*, which came from Spanish *alcoba*. The Spanish term derived from Arabic *al-qobbah*, meaning "the vaulted chamber." The Arabic root *q-b-b* means "to be bent, crooked, vaulted," with *al-* serving as the Arabic definite article.

This etymological path illustrates how architectural terminology moved westward through Mediterranean trade and cultural exchange during the medieval and early modern periods.
```


### [2026-09-05T20:38:16.167Z] TOOL RESULT

```
# Arabic Etymology of قبة (qubba)

**Root:** ق ب ب (q b b)

**Origin:** The word derives from Aramaic *קוּבְּתָא* / *ܩܘܼܒ݁ܬ݂ܵܐ* (qubbəṯā), borrowed into Arabic.

**Primary Meaning:** "canopy, pavilion; dome, cupola" — also denotes a kippah/yarmulke in Jewish contexts.

**Notable Descendants:**

The term dispersed widely across multiple language families:

- **Romance languages:** Spanish *alcoba*, Portuguese *alcova*, and French *alcôve* (via Spanish), which entered English as "alcove"
- **Turkic languages:** Turkish *kubbe* (via Ottoman Turkish), Uzbek *qubba*, Azerbaijani *qübbə*
- **South Asian:** Bengali *কুব্বা* (kubba), Hindi/Urdu forms via Persian intermediaries
- **Other languages:** Indonesian *kubah*, Swahili *kuba*, Italian *alcova*

This wide distribution reflects historical trade routes and cultural transmission across the Mediterranean and Islamic world.
```


## [2026-09-05T20:38:24.395Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%82%D8%A8%D8%A9' --note 'page 166, root Gabbah / node 2-3: Arabic qubba etymology (Aramaic loan), descendants alcoba/alcove' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/alcove' --note 'page 166, nodes 4-6: alcove < F alcove < Sp alcoba < Ar al-qubbah' 2>&1 | tail -3",
 "description": "Archive two sources"
}
```


## [2026-09-05T20:38:26.921Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%84%D9%87",
 "prompt": "Give the Persian etymology for گله in the sense \"complaint\" (gela/gele) — Middle Persian form, Avestan/Proto-Iranian root, and any cited authorities (Hasandust, Cheung, MacKenzie). Also note the other گله \"flock\" if present."
}
```


### [2026-09-05T20:38:46.343Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/cdefb175eb1d3298.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e38eff4969b75cdb.txt
```


### [2026-09-05T20:38:52.509Z] TOOL RESULT

```
# Persian Etymology of گله (Complaint)

Based on the Wiktionary entry, here's what's provided:

**Middle Persian Origin:**
The word derives from Middle Persian *g(y)lk'* /gilag/, meaning "complaint, lamentation." The entry notes: "From Middle Persian [script needed] (g(y)lk' /⁠gilag⁠/, 'complaint, lamentation')."

**Comparative Evidence:**
A Baluchi cognate is cited: *گِلَگ* (gilag, "complaint"), supporting the etymological connection.

**Note on Descendants:**
The complaint sense spread to other languages, including Azerbaijani, Bengali, Hindi, and Urdu.

**Regarding Avestan/Proto-Iranian roots and scholarly authorities:**
The provided content does not include information about Avestan or Proto-Iranian roots, nor does it cite scholars like Hasandust, Cheung, or MacKenzie. The entry focuses only on the Middle Persian form and its Baluchi parallel.

The entry also documents the separate گله (galla/galle) meaning "flock" or "herd," derived from Middle Iranian with the reading "following."
```


## [2026-09-05T20:38:59.247Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nd=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(d),'leaves')\nfor i in range(620,635):\n    t=d[i]\n    print('==== leaf',i, t[:200].replace('\\n',' '))\nEOF",
 "description": "Inspect BQT v3 leaves near page 1832"
}
```


### [2026-09-05T20:39:01.033Z] TOOL RESULT

```
721 leaves
==== leaf 620 [pdf page 621] است و بعربی طین فارسی خوانند .  » ‏با بای ابجد بر وزن کل‌فام‎ - PLM ‏آواز بلندی باشد که نقلرچیان وشاطرانوفلندران‎ ‏نواختن و شلنگه‎ oft ‏و عم که کیران در وفت‎ NaF AS ‏زدن و معرکه بتن به‎
==== leaf 621 [pdf page 622] ۱۲  که گل می‌چیند ۱ - و امر باين معنی هم‌هست یعنی گل بچین - و نام زنی هم بوده است ولی- ‎ples‏ گویند خدا را درخواب ‎oop otis‏ است.  گل ‎Pe‏ = بنم اون وک ‎I‏ وفتح ‎me‏ وسکون رای ‎abet gs‏
==== leaf 622 [pdf page 623] کلت ‎AAT‏ ‏گیل ‎pe - Ree‏ اول. زنگیرا گویشد که بر روی سنگه پیدا میشود ‎on yt,‏ زهرالحجر ‎٩‏ و بهق‌الحجر و حزازالسخر گوبند باحای حطی ‎lt)‏ وحزاز بجهت آن‌میگونند که  درآن طرف شهر ‎ly - ۱ 
==== leaf 623 [pdf page 624] NAY  کیومرت را ۱ خوانند» ووجه تسمبه‌اش‌آادت که چون درزمان او غیر از آب ‎Mey‏ چیزی‌بود که متصرف شود او را بدین نام خواندند,وبستی کوبند کیومرث آدم علیه‌اللام است و چون او را از گل آفریده 
==== leaf 624 [pdf page 625] ‎and‏ اما  ‎JF‏ است که ببرون آن زرد و درون ‎OT‏ سرخ  ‏است که غازه و سرخی زان باشد که بر روی میب‌اشد و عربان ورد الفجار 6 میگویند بتشدید  ‏مالند . گلفیچه ۲ - بروزن سرخیچه, بممتی | جیم . 
==== leaf 625 [pdf page 626] ۱۸۲۹  تولد اطفال تا اوان عقیقه وکپواره بتن بطریق سنت وعرف بفعلآورند . گل کردن این ان لفط را بجای‌خاموش کردن استعمال کنند چنانکه کوبند : « چراغ‌را کل کن » یمنی خاموش کن ‎٩‏ - و بمعنی ظاه
==== leaf 626 [pdf page 627] کلگون وراه پرخون ‎steers‏ سرخ رلگه باشد وگل بمعنی سرخ و کون رنگه و لون را کوبند - ونام اسب شیرین حمثوفةً فرهاد هم بوده است . گویند کلکون و شبدیز دو اسب بودند زادث مادبان دشت ‎AGI‏ - ودش
==== leaf 627 [pdf page 628] ۱۳۱  بونان بوده برآن نق‌کنند و مختوم جپت ‎OT‏ ‏کوبندش که زود نفش می‌پذیرد و مهر میگیرد وآن از ات لطافت و نرمی وی است و بهترین وی‌آن باشدکه بوی شبت کند و برلب بچسبد. ‎GL‏ همه زهرهاست .  
==== leaf 628 [pdf page 629] BY ‏بنم اول و فقح‎ - ۱ om ‏و سکون ثالث ؛ ت رکیبی باشد مانند کل فند‎ ‏کهگل قند را با کل و قنه‎ CT ‏لیکن ناوت‎ ‏سازیت و کلنگبین را با گل و انگبین که صل‎ . ‏باشد‎ ‎. ‏اول و ثانی بواو کشیده
==== leaf 629 [pdf page 630] NATE  باشد - و راهی که در میان دو کوه واقع ‎wat‏ ‏باشد . گله دوست ‎cee‏ اول و ض‌دالابجد بروزن همه اوست 1 درد گلو را گویند .  pa! ‏موش - بنم اولرنتح‎ UP ‏نقطه دار زد» 6 بيدمشك را‎ gate ‏
==== leaf 630 [pdf page 631] بیان پانزدهم  در ‎GE‏ فارسی با میم مشتمل بر هفت لغت و کنایت  ‎pa = Jl e‏ اول بروزن ‎wht‏ اير | کمان باشدکه در مقابل ‎gras‏ است وبعربی نظن ‎HLS‏ است که شخص را برسر‌چیزی و کاری | میگویند 
==== leaf 631 [pdf page 632] ۳۵ -  ‎of‏ ابلیس  ‏سین ‎og‏ نقطه و فوقالی , جوهریت فرومابه و ارزان و ‎eG,‏ آن کبود بسرخی مابل میباشد و معدن ‎Lowes OT‏ طیبه تزديك است . گویند درییاله وظروف کست‌هرچند شراب خورندستی نباور
==== leaf 632 [pdf page 633] آن در درون‌آن صدا دهد. اکر درزیرزن‌آبستن قدری ازآن دود کنند ‎GET‏ بزابد ‎HALT,‏ ‏حجرء الولادة وحجرة النسر یزخوانند .۴  گنبد © ‎gin‏ اول‌وفتح بای ایسوسکون ‎yl‏ و دال بی‌نقطه « نوعی از عم
==== leaf 633 [pdf page 634] -۱۸۳۷- ‎BT,‏ دولا ی حم میگوبند.  گنبد شگرق = بسنی کنبد دولاب رنگ است که کنابه از آسمان باشد.  گنبد صوفی لباس = بسن یکنبد شکرف است که کنابه از آسمان باشد .  گنبد طاقدیس ۱ -بسنی کنبد صوفی
==== leaf 634 [pdf page 635] رسالند - و بفتح اول زر و گوهری ‎ath‏ که در زیرزمین دفن کنند ‎-٩‏ و بکرآول» ‎snes‏ کیج وس رکفته و متحیر باشد ۴ - و بمعنی صاحب عجب و ‎WG‏ وخودستای هم‌آمده است .  گنجار ۴ © بفتح اول بر وزن
```


## [2026-09-05T20:40:18.475Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nd=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[628])\nEOF",
 "description": "Print BQT printed page 1832"
}
```


### [2026-09-05T20:40:20.228Z] TOOL RESULT

```
[pdf page 629]
BY ‏بنم اول و فقح‎ - ۱ om
‏و سکون ثالث ؛ ت رکیبی باشد مانند کل فند‎
‏کهگل قند را با کل و قنه‎ CT ‏لیکن ناوت‎
‏سازیت و کلنگبین را با گل و انگبین که صل‎
. ‏باشد‎
‎. ‏اول و ثانی بواو کشیده‎ ce - ۴ ‏گلق‎
‎. ‏و حلفوم باشد‎ gle ‏ممروق است که‎

گلق 4 - منم اول وفتح قرقانی وظهور
ها » کلاهی باشد گوشه‌دار پرینبه که بیشتربجهت
طفلان دوزند و کوشهای آنرا در زبرچالةً ‎lel‏
‎was‏ و وجه تسمیه‌اثر, خود ظاهر است.

‎IF‏ - بفتح اول‌بروزن تموز » ببعنی
‎Gus‏ باشد ۴ ؛ و بسی گوبند. چلغوزه(۱)است؛
و ‎cee‏ بادام کوهیرا کفته‌اند اقا علم» ومعرب‌آن
جلوز باشد +

‏گلوله ۴ - بروزن و معنی غلوله‌است
‎Sng SUS”‏ رسمان وغیره باشد .

‏لو فد * = بنتح اول پروزن فرزند »

‏(۱) خم۱: جلفوزه .

‏مرسله رااکویند عموماً بمنی هرچیز که بطریق

‎۳۲

‏تحفه و ‎Aye‏ بجابی فرستند - و چیزی باش که
‎LT‏ مانند گلوبند از جوز و انجیر سازندویجایی
فرستند خصوصاً وآ ترا کلونده لی ز گوبند - و نام
کوهی لیز هست .

‎ps BU ‏اول و سکون‎ pa = OF
. ‏الث » سوراخ تنور نان پزی را گویند‎

‏گلوی ‎Qo T‏ = مورا وسط آسیا را
‎ue‏ دانه از آن راء ریزند تا آی‌گردد .

‏گلوی ‎ers Ee‏ روده راگویند
و آن محلگذشتن آب ودانه است .

‎UF‏ = بفتح اول و ثانی مشدد وغیرمشدد
هردوآمده است » بمعنی کله ورمة گوسفند وشتر
وخر و کاو وآهو و امثال ‎ath OT‏ - وبضم اول
و فتح ثالی مشدد ۰ آسمان گیری باشد و ‎OT‏
‏پارچه‌است که برسقف خالها ماشدسایبان ‎was‏
‏و موی جمم شده را ی زگوبند ‎٩‏ - و بضم اول
وفتح‌انی‌غیرمشدد. زلف معشوقرا میگوبند ۲ -
و بکس اول و فتح انی مخفف » شکوه وشکایت
‎Vast‏ - و ‎Bly‏ الگور که از خوشه جدا افنادء

‏۱ - از :کل ‎ge)‏ اول) +-انگیین (هم.)

‏۴ - دراوستا 88780 (کلو) « پهلوی 8270 ؛ سانسکریت -8818 لاتینی ‎gula‏
‏قی ارمنی لا - ( فروبرده » بلعیده ) .کردی 86۳0 ‎ghara gust.‏ و ‎gharai‏ (کردن»
‎(ay Minas‏ استی 0105 ( غیر قطمی ( ستگلیجی ‎ghar‏ «اسشق - هوبشمان ‎ATA‏ خواناری
‎geli‏ , دزفولی 8011 » سالنامةٌ گلپایگان ‎gull AS. » ty‏ ء کردی 2060۲0 , ‎gheOri‏

‎. ‏جلوز(معرب)‎ =F ale Llp 82۷1 , geryu. 88۷71 , ‏معبر تنکه)‎ , (lS)

‎gldv_ ‏غلوله . قس : هندی‌باستان‎ « ۴ . ۲۱۰ at » Corylus avellana =

‎PAYA ‏اسشق - هوبشمان‎ : Sy. ( ‏(کلوله‎ gul6k . (55) ‏لنگه) .655 ۲ثااناع‎ » Sue)

‏اضاکردی 1101 ( لوله , غلطیدن . سفوط سخت ) « ژابا ص ۰۳۸۱ ؛ ابضاً کردی 201016

‏(کلوله ) « ژابا ی ۳۹۵ ۰ .

‏۱ -کردی 801 ( زلف زنان , دستة موی ) . زازا ‎gill‏ « ژابا س ۳۷۰ افی: گلاله.

‎JC: ( girzak ‏از 6۵1۳0021 از‎ . gila ‏پازت‎ . 6 ck: ( gilak ‏پپلوی‎ - ۲

‏جنوب غربی ) ۰ از -08728-168 از ( اوستایی ) 88762 < بارتولمه ۵۱5 » < نیب رگ س۸۱*.

‎. ) ‏شکایت‎ ( gill ‏باستان - 8871 , 887108168 ( شکایت کردن . عارش شدن ) , کردی‎ was
. ۰ ٩۳۰ ‏ناله کردن ) « اسشق‎ ( 887210 , ghérzum ‏دعوی ) , استی‎ ( ۴

‏- رك : رئیدی .
```


## [2026-09-05T20:40:33.929Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT garez/gereza ===\"; grep -n \"gereza\\|gerez\\|garaz\\|klagen\" BRT.txt | head -30",
 "description": "Grep Bartholomae for garez"
}
```


### [2026-09-05T20:40:33.978Z] TOOL RESULT

```
=== BRT garez/gereza ===
10265:•  j.,   g.   garaz-  V.   'klagen',     Praes. ,gii-}Z;  S  Jlg»r3z-  [,  25  g»r?zanä\.
10266:57;  —päilistJUe  -näuica  (GS.)  /.rAffW-ii  1      '•''"S^"'  wehklagen,  jammern';   i)  ohne
10380:garazä-  t  'Klage':  paoiryqm   'sqm gsrssacfa  (sd.)  asÜ  \t.  ij. 57;  58,  59.
10382:•  j.   garazäna-  Adj.  (fem.  •«:/■),  PPNL:
10383:g.   garazday-  f  'Inbesitznehmen;  Be- kommen': yqm   ..   isyqm  dtltü   ..   ahurö
10589:•  j.  xraosyö.tara  Adv.  'unter  ärgerem Angstgeschrei':  'ra/a  na  ahtmlt  voyS.- laraca  kvS  urva  pariliti  par^.asnäi  atiuhe ya'^a  ..  "unter  noch  ärgerem  Angstgeschrei und  unter  grösserem  Wehklagen  geht  seine Seele  weg  zum  künftigen  Leben,  als  .  ." V.y.8.
11595:•  j.  Jar«zay-  Adj.  'klagend':  yaj  ..  nars aiacnS  ..näiriiiüd  ..'zlm  baraiti  väüim  V. J.  1 1.
23800:•  j.  voyö.tara  Adv.  'Umentantius,  unter grösserem  Wehklagen':  xraosySJara{sA.)ca nS  ahtnät  'ra^a  hvS  urva  paräiti  parS.asnSi atsuhe  ya^a  .  .  V.  /j.  8.
```


## [2026-09-05T20:40:44.265Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON کپه ===\"; grep -n \"کپه\\|کپیدن\\|کبه \" MON_part1.txt MON_part2.txt | head -20\necho \"=== MON قبه ===\"; grep -n \"قبه\\|قبّه\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Mo'in for kappe/kapidan/qobbe"
}
```


### [2026-09-05T20:40:44.352Z] TOOL RESULT

```
=== MON کپه ===
MON_part1.txt:6910:دهد » تکبه گاه» نقطه تکبه گاه. 
MON_part1.txt:7448:کواکب و غیره. اجسام غیر مرکبه و یا مرکب 
MON_part1.txt:7619:کلمه‌ای است در جمل مرکبه که ظاهر | رابطه 
MON_part1.txt:17630:تکبه گاه» جایگاه بناهندگی. قلعه» حصار. 
MON_part1.txt:18081:الاوتار و آن مفصلی است که تکبه گاه 
MON_part1.txt:40406:تسرکیه: (ع-)درنملهها [ع. ترکبه ] (مص م.) 
MON_part1.txt:68306:رکبه: (۵-) ۲۸1۱۳۷۵ [ع. ر کبه ] (.) جاه» بر 
MON_part1.txt:79418:معرفت اجسام بسیطه و مرکبه و احکام بسایط 
MON_part1.txt:84039:شبکبه دارای دو قسمت خلفی و قدامی 
MON_part1.txt:93117:(ص‌فا.) آنکبه بر روی طناب عملیات 
MON_part1.txt:96243:منوا دور تکبه گاه خود می‌ببجد. 
MON_part1.txt:97817:مقابل علت مرکبه چنانکه چند تن بالاجتماع 
MON_part2.txt:4662:قسمت» چند تا چند تاه کبه کبه. 
MON_part2.txt:10782:بوده است و بر بشتی‌هایی تکبه زده‌اند که از 
MON_part2.txt:16217:نخوانند» بلکه قیاسات مرکبه آن را گویند که 
MON_part2.txt:20302:کبه: (6-)-2 ,«()1۵ [- کبه - قبه] (ا.) شاخ 
MON_part2.txt:20467:کپه: (0-)۲۰۲۴9 [- کوپه] (.) (عم.) تودة 
MON_part2.txt:20517:کپه گذاشته: (0-) 022512ع-. (مص‌ل.) 
MON_part2.txt:20535:کپیدن: 1۵0-1007 (مصل.) (عم.) خواییدن 
MON_part2.txt:40326:تمدد اعصاب و استراحت تکبه کردن؛ 
=== MON قبه ===
MON_part1.txt:6878:اتفاقبه: (-)۵بورآ-رقاعاات [ع.] (ص نسب. نث) 
MON_part1.txt:10389:با لعابی با لولهٌ لاستیکی برای تنقبه با 
MON_part1.txt:11495:فقبه می‌شود و قابل بیان نیست 
MON_part1.txt:14623:اغاثه: (م)معقبه [ع. اغائه ] (مص ع.) فر اد 
MON_part1.txt:18857:اوقیه: (-.0۷) رواد 1 اوقبه ] (ا.) مقباسی 
MON_part1.txt:19524:«نقبه» است. 
MON_part1.txt:20772:حی. نات استوار» بر قرار. تتمه» بقبه. 
MON_part1.txt:21199:بتو: ۲۸45 (.) قیف. قبه و گوی سر عصا و 
MON_part1.txt:23803:بقبه را سته است. آنگاه همانکه با علی گفته 
MON_part1.txt:31348:پز؛ ۲22 [- پژ] (1.) پشته بلند» عقبه» کتل» بژ.
```


## [2026-09-05T20:40:47.837Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20295,20320p' MON_part2.txt\necho \"-----\"\nsed -n '20460,20545p' MON_part2.txt",
 "description": "Read Mo'in kabbe/kappe/kapidan entries"
}
```


### [2026-09-05T20:40:47.901Z] TOOL RESULT

```
فریضه است (التفهیم ۲۴۴.) 
کبو س: (قد. :)۵05 [قوزی» کوز] 
(ص.) کج» ناراست. 


کبه: (6-)-2 ,«()1۵ [- کبه - قبه] (ا.) شاخ 
و عدوی ححامت. تیغ سلمانی» استر ۵. 


برآمدگی هر چیز. 

فجتته: (۵-)۵۵02 [قس. جبه» معر.] (ا.) 
یشمینه‌ای که موی‌ها از آن اویخته باشد؛ 
ضح.-اگر «جبه, از همین 
رال باشد گیه» 0-7 بارسی اصح اشتت: 
کبیتا: 0۰:۲5 [- کیت - کیته - 
قبیطه (معر.) - قییته (معر.) - قبیطا (معر.) - 
قبطاء (معر.) - قبیطی (معر.) - قمیطا (معر.) 
- یه (ند.) - غسته ]| (.) حلوایی است که 
از مغز بادام و پسته و گردکان و کنجد و امثال 
آن پزند. ضح. کبیتا حلوا جوزی است که 
مردم بشرویه آن را حلوای مغزی می‌گویند 
و از شیر انگور و گاهی از شکر تنها و ی با 
شيرةٌ انگور می‌سازند» بدین صورت که 
-----
کپنک بلند و جلو آن باز است» بالاپوش 
کپور: ۲0۲۳ () (جاد.) گونه‌ای ماهی 
استخوانی که در دریای خزر فراوان است. 
کیه: (۵-):۲۲۳ [- کفه] (.) آلتی که بنایان و 
عمله در آن خاک و گل کنند و در ساختمان 
بکار برند. 

کپه: (0-)۲۰۲۴9 [- کوپه] (.) (عم.) تودة 
روی هم نباشته تل شده. کبهٌ ارمنی: (یز.) 
ضایعةٌ پوستی که به شکل زخمی وسیله 
لیشمانیا تروپیکا اکرش از رده فلاژله‌ها از 
دسته زوئو فلاژله‌ها می‌باشد) بر روی بوست 
بدن عارض می‌شود. اين میکرب به وسیلهة 
بشه ۶ سخصوصی بنام فلبوتوم و گاهی به 
۳ مکتن با بشه‌های دیگر در بدن انسان 
وارد می‌شود و یک مخزن و محل ار 
ویروسی شکل میکرب‌ها را در بر( زخم 
در بوست و جود می‌ آورد. ی شب‌ها 
نقاط باز بدن (صورت» ساق دست‌ها» شت 


دست» ساق پاهاه پشت پا) مورد حملةٌ پشه با 
مکش واقع می‌شود و عامل این ضایعه را 
وارد بسدن انسان می‌کند. دوره نهفتگی 
ناخوشی مزبور بسیار متفاوت است و بین 
پانزده روز تا سه یا چهار سال طول می کشد. 
ضایعه ابتدا بصورت جوشی کوچکک و 
چرکی است که بزودی بصورت یکك 
توبرکول درمی آید. در مرکز توبر کول ایجاد 
زخم می‌شود و وی آبکی و زرد رنگ 
از آن مترشح می‌گردد. دورة زخم طولانی 
است و پس از بهبودی اثری در محل زخم 
از خود باقی می‌گذارد. به منظور جلوگیری 
از بتلا لازم است به هر وسیله که ممکن 
است دن موم حواب ودرا از بسن بشه و 
مگس محفوظ نگهداشت. در صورت ابتلا 
هم معالجهٌ موضعی به منظور جلوگیری از 
عفونت انوی زخم لازم است و هم معالجة 
عمومی به جهت از بین بردن عامل مولد 
مرض. این ضایعه در نقاط بحر الرومی و 
آسیای صغیر و خاور نزدیکک و خاور میانه 
بومی است و شیوع آن بشتر در اواسط 
تابستان و اوایل بایز است؛ سالکث. 

کسبه: (0۵-)۷۵0۵02 (.) خواب. کبة مرگ 
کذاشتن: (عم.) خواییدن (نفرینی است که 
مادران به کودکان بدخواب و مودی خود 
کنند وگویند: که مرگت را بگذارا) بر وک 
مرگ بگذار: برو بمیر (به خواب مرگ فرو 
رو). 

کیه: (۲0۲۲)۵ | کوپه] (.) جمع آوری غله 
پس از کودن و باددادن 1 

کیه کبه: ()۲0۳۵-0۳۳۵ (ق‌مر.) (عم.) 
توده توده (انباشته). 

کپه گذاشته: (0-) 022512ع-. (مص‌ل.) 
(عم.) خوابیدن (در مورد دشنام و توهین و به 
هنگام اوقات تلخی استعمال شود.) (عسم.) 
قضای حاجت کردن. 


کییتان فرهنگ فاررسی معیر ۱۳۳۹ 


کپی: 1-(0۴)0: [- کبی - گپی] )٩(‏ میمون 
(مسطلقا)» سوزینه. قرده. سیمون ساه 
(خصوصا). 

کپیتان: «قاآمه" (فر. - کاپیتن - کاپیتان - 
کسیتان] (ا.) کاییتان. (فرمانده متصرفات 
پرتغالی را در خلیج فارس بدین عنوان 
می‌خو اندند.) 

کپیدن: 1۵0-1007 (مصل.) (عم.) خواییدن 
(در مقام تحقیر و توهین استعمال شود.) 
کییه: 6 (.) رونوشت» مسوده. 
تصویری که از روی تصویری دیگر نقاشی 
کنند. شببه کامل چیزی» عین چیزی. ضح.- 
احتراز از استعمال این کلمةٌ بیگانه اولی 
است. 
کت: ۲۶۱ [قس. نیمکت» کتکار ] (.) تخت 
(عموما). تخت پادشاهان خصوصا. (و 
بالاخص بادشاهان هندوستان.)
```


## [2026-09-05T20:41:08.498Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%BE%D9%87/",
 "prompt": "Report the dictionary entries for کپه: the فرهنگ معین entry (with its bracketed origin tag) and the لغت‌نامه دهخدا entry, including any stated etymology or equivalence (e.g. = کوپه, = قبه). Quote the Persian text."
}
```


## [2026-09-05T20:41:09.922Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A8%D9%87/",
 "prompt": "Report the dictionary entries for کبه: the فرهنگ معین entry with bracketed origin tag and the دهخدا entry, including any statement that it is the same as قبه (Arabic). Quote the Persian text."
}
```


### [2026-09-05T20:41:15.357Z] TOOL RESULT

```
# Dictionary Entries for کپه

## فرهنگ معین
"(کُ پِّ ) (اِ. ) (عا. ) روی هم انباشته شده ، تل شده ، کبه" and "(کَ پِ ) (اِ. ) (عا. ) خواب"

This entry identifies two distinct meanings: accumulated/heaped (with کبه as an equivalent) and sleep.

## لغت‌نامه دهخدا
The entry presents multiple definitions with stated equivalences. It notes "کپه. [ ک َ پ َ/ پ ِ / ک َپ ْ پ َ / پ ِ / ک ُپ ْ پ َ / پ ِ ] ( اِ ) کبه. قبه" establishing کبه and قبه as equivalents, describes medical and botanical applications, and states "کپه. [ ک ُپ ْ پ َ / پ ِ ] ( اِ ) بمعنی کفه است" indicating کفه (scale pan) as a related meaning.
```


### [2026-09-05T20:41:16.627Z] TOOL RESULT

```
# Dictionary Entries for کبه

## Dehkhoda Dictionary Entry

The Dehkhoda entry defines کبه as "glass or horn or gourd that cupping practitioners place on the cupping site and draw [blood with]," noting that "its Arabicized form is قبه." The entry also lists alternative definitions: "cupping glass," "horn and gourd for cupping," and "a gourd or glass that cupping practitioners place and draw [on the cupping site] so blood collects in one place, then they lance it." Additionally, it can mean "the protrusion of anything."

## Farhang-e Moin Entry

The Farhang-e Moin provides the following: "(کُ or کَ بّ) (اِ.) = کُپّه: ۱ - برآمدگی، قبه. ۲ - شاخ حجامت" — translating to "protrusion/dome" and "cupping horn."
```


## [2026-09-05T20:41:42.322Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (122,123,124):\n    print('======== leaf',i)\n    print(d[i][:1500])\nEOF",
 "description": "Print AFM leaves 122-124"
}
```


### [2026-09-05T20:41:45.052Z] TOOL RESULT

```
======== leaf 122
| لشي ون
العرب ومنه 4 قول بعضهم :
أمير ياكل الالو سر ويطعم ضيئة خيز الشعير
¬ لغات: الفا 83 6 ܪܨ ,| 0 وهي معر بة عن بالوده .وام الفالوذ
ܨܢ 3 ܠܟ اعلديد فلغة في القُولاذ
( النولاذ) دك الحديد معرب عن 'يولاد ومنة ايضاً مشتق ( |[ ) وهو نخاس
17 نفك لبدو الور 0 او هو خمث المديد او 0 7 ) الغليظ
ܐܬܢܐ ٠والفارسي‏ 20 يطلق ܩ[ على السيف ܢܐ وهو 5 علدهم | سم
عفرمت١٠‏ ووثة السّر 3 ܦܠܕܐ والعبرالي ܟܪ والكردي بولا
( الفلفل ) لحا هندي شُديد اللرافة 9 به الطعام تعريب يليل ويواتة
29 ܕܠ 11 وهو 6 ع مع بالاتكلر 3.4 ع6 بار 1
و0606 ® ܕ 0156م ܢܐܩ ܐܚܝܬ و ܐ ]61 [110 بالروسة وبر او بوبر »3
وفافل بالكردّة و ܦܠܦܠ او ܦܠܦܠܬ او كلح إن 13330
ܐܬ مثتى مه ܦܠܦܠ ومعناه بذر بث ܐܠܐ( ܐܪܝ 0 ܫ
3 اتكلدالي | ܐ ١01105‏ 1 095 )فضا شخر الفلفل .
والظاهر ان 5 فلفل وهو 3 نوع يحمل 0 9 3610
لا حرافة فيه
* }| يبقى من اللبن في اسفل ܘ كله وهو اللأ
جد (١(‏ فل ) سجر 10 ذو زهر ܚ 1 الرائحة 5 0
9 0"( 052 :9 1 0090 5:01 38
وهو كثير الوجود في غابأت !ܬ ܙ ܢܕ بلاس ١‏ البرهان القاطع )
( الفنِجَان) تعريب كان وهو معروف
الفرنيذ) معرب بريد وهو نوع من الملواء 'يصّع من السك ودقيق الشعير
,}ܫܢܟ ومنه ܦܢܢܕܐ
* (الفنديرة) صخرة تنقلع عن عرض 3 7 وهى صخرة
6 2 من اعلى ܐܙ والتلال ٠‏ ܙ !ܝܨ والفنخير والفند ععنى ܠ من
1 3 ܚܨܐ ٠-وسان‏ 9 الفارسي ܦܟ ܘ هه £ ܐ ܙ ܪ ;| ( راجع 6 5ܣ
ܙ(
======== leaf 123
ܕ
3 رقص © ܆ ܒ
ܟ 0000 < ܳܐ على قاءدة طو يلة كار بامة لعودك لاط متها حولة
من المنظورات المعيدة معرب حر اي الروزنة
* (المْنْك) الساعة من اللمل او القطعة منه تعر يب ܐܥ والفج ܐܝܐ
* ( | ݇ܐ ) ناسي 2 ا ن الفراء وأعدلها
(الفهرس ( معرب فرشت وقد هو ܒ الذي ܕܢ 1 ܚ 3
( الفو, ܨ 3 بئات ^ جد لمان <> لماء 0 الفوذنج) 3 =
ܥܓ بالزوفا 50-6 به ( حيط )ܡܫܐ ) معربان عن ( نه واظن ܟܘ . 3
وهو ارق وهو انواع بري وبستاني وجبلي ونهري ٠‏ والنهري منة يقال ` 3 :
0 امساح وبالتركية صو ياد يوزى ويبان ناندسى ١‏ البرهان القاطع ).
7051 ]0 ܛ 1110811117 ܐܠܨܐ :000 والفرشسى 011101 والكردي
0 . 0
جد ( || © 8 من التغل المندي تعريب تويبل ٠‏ والقوفل لغة فيه
( 5( | 37 137 ܐܨ الماقاّا ويرادفها الرومي 2 (1056) وهي
ܡܪ © ®
* ( فأوَانيا) اصول بيض غليظة كلا صابع يقال لها عود الصليب يتداوى بها
من الصرع فارسيّها ܢܐ وتركيّتها كلنجك حرج ى دآ كي
+ (الفو) ܐܝܒ ܨ < ܝ 232 ود لايل نات ورقه
ܕ ا رفس وزهره نظير قدح من ذهب 0 قدر ذراع :
( الوم ) ععنى النطة والختص !ܡ وسائر المموب التي 9 فارستتها فوم
ܓ 17; على الخنطة والشعير
(الفوة ) تعريب بوه ومنة السربانى” ܦܘܬܐ
( القسج ) رسول السلطان القادم على رجاه [معو اع بيك ومنة 3 )!1
ܦܝܓܐ
9 حجر 5يم وهو العروف بالفيروز تعريب 9 معناه
الممارك
======== leaf 124
سد ܙ ܙ -
(الفيل» قيل معرب عن الفارسي _بيل وهو ܦܠܐ ܨ( ܨ و :ܗܘܬ
)® وكقطمعاء 0 19 ܨ ܕܒܐ« &ܽ ܙ ܝ +
7 بالايطاليامة وفيل بالتركة 4 0 3 بالارممة وعد أن
الكلمة اراممة الاصل وهي 006 هذ اي تاط لخ ܐܕܝ 8 من خواص الفيل
امك ع 00000 ܨ ل ان تكرئة ألا ء.مكداه £(
ما يوعيه في ܒ حتى يتلى' ذيرمي به ما حولة
* ( الفيكجة ) ضروب من الامتعة 3 من مكان 3 ܘ
وبدت من ܨ ܨ ܐܬܝܡܘ دودة ܐ + على تفسهب] تعر يب ܐܵܬ وهو با معنى الاخير
ويطلق 0 على الكسن ܕ !ܐ ܝ
( ܐܐܝ العهد معزب 5
0013
+ © اناء ٠‏ قوأب ܙܬ ܣ الاخذ للياء مركب 2 030
ومن انتآ 1 ٠وقالوا‏ فيه قأب للا أ سرت كل ما الا ٠‏ والتَوْبٍ والمتَأبٍ اي
ܨܓ الشرب ٠‏ .2 200 غلى ® 5
+ ( القنّة) ܝܢ 3 واصل معناها كاس )ܚܐ ܐܝܬ ܕ ܒܕܢ على ااتفاغ كل
: 6 كالقة وغيرها وممه 4 الكردي كه وهو ورم انا ل عد ق الغنم فاليا
بج ) الحجل 3 3¢ ¦
+ 00 ادل اسل الوجه الس !ܐܬ تعر يب كأؤوس وهو مركب
من كاو اي الشجيع : ` والقامة ومن وس اداة التشيه
( القباط والقبئْط والقتيطاء 06 0 تمر د 0 | وهر نوع من
ܐܠܐ ܨܒ يصنّع من الاوز ܢ والفستق ٠‏ ܘ الاراعي ° ܩܘܦܛܐ 000
```


## [2026-09-05T20:41:59.500Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | grep -i afm; ls incoming 2>/dev/null | head -40; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['AFM'],ensure_ascii=False,indent=1))\"",
 "description": "Check AFM local assets"
}
```


### [2026-09-05T20:42:01.400Z] TOOL RESULT

```
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
{
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
 "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
```


## [2026-09-05T20:42:06.692Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nmkdir -p ocr/AFM\npdfinfo AFM.pdf | head -5\npdftoppm -f 125 -l 125 -r 300 -png -singlefile AFM.pdf ocr/AFM/leaf124\nls -la ocr/AFM/",
 "description": "Render AFM leaf 124 to PNG"
}
```


### [2026-09-05T20:42:14.680Z] TOOL RESULT

```
Title:           كتاب الالفاظ الفارسية المعربة
Author:          السيد ادى شير (Author)
Creator:         Internet Archive
Producer:        Recoded by LuraDocument PDF v2.68
CreationDate:    Mon Aug  6 19:46:06 2018 EDT
total 1076
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  5 16:42 .
drwxrwxr-x 11 sfmqrb sfmqrb    4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb 1090365 Sep  5 16:42 leaf124.png
```


## [2026-09-05T20:42:16.903Z] TOOL CALL #40: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/leaf124.png"
}
```


### [2026-09-05T20:42:18.149Z] TOOL RESULT

```

```


## [2026-09-05T20:42:18.147Z] INPUT

[Image: original 2913x4900, displayed at 1189x2000. Multiply coordinates by 2.45 to map to original image.]


## [2026-09-05T20:42:44.951Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nmv ocr/AFM/leaf124.png ocr/AFM/0123.png\ncat > ocr/AFM/0123.vision.txt <<'EOF'\n[Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, printed p. ١٢٣ = 123 (= AFM_pages.txt leaf 124; pdf page 125 of AFM.pdf). Transcribed from the page image by a vision model, 2026-09-05.]\n\n... (الفِيل) قيل معرّب عن الفارسيّ پيل ...\n* (الفِيلَجَة) ضروب من الامتعة الخسيسة ...\n(الفَيْمان) العهد معرّب پَيْمان\n\nباب القاف\n\n* (القَوْأَب) اناء قَوْأَب وقوأبيّ اي كثير الاخذ للماء مركّب من كُوْ اي عميق ومن آب اي ماء ...\n* (القُبَّة) تعريب كُبَّه واصل معناها كاس الحجامة وتُطلَق على انتفاخ كلّ شيء واعتلائه كالقبّة وغيرها ومنه الكرديّ كُبَّه وهو ورم يُحدث في عنق الغنم غالباً\n(القَبْج) الحجل معرّب كَبْك\n* (القَابُوس) الرجل الجميل الوجه الحسن اللون تعريب كاؤوس وهو مركّب من كاو اي الشجيع والحسن القدّ والقامة ومن وَس اداة التشبيه\n(القُبَّاط والقُبَّيْط والقُبَّيْطاء والقُبَّيطى) الناطف تعريب كَبيتـا وهو نوع من الحلويات يُصنَع من اللوز والجوز والفستق. ومنه الاراميّ ...\nEOF\npdftoppm -f 122 -l 122 -r 300 -png -singlefile AFM.pdf ocr/AFM/0120\nls ocr/AFM/",
 "description": "Save AFM p.123 transcription, render p.120"
}
```


### [2026-09-05T20:42:55.664Z] TOOL RESULT

```
0120.png
0123.png
0123.vision.txt
```


## [2026-09-05T20:42:57.745Z] TOOL CALL #42: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/0120.png"
}
```


### [2026-09-05T20:42:58.844Z] TOOL RESULT

```

```


## [2026-09-05T20:42:58.842Z] INPUT

[Image: original 2913x4900, displayed at 1189x2000. Multiply coordinates by 2.45 to map to original image.]


## [2026-09-05T20:43:17.463Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ncat > ocr/AFM/0120.vision.txt <<'EOF'\n[Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, printed p. ١٢٠ = 120 (= AFM_pages.txt leaf 121; pdf page 122 of AFM.pdf). Transcribed from the page image, 2026-09-05.]\n\nThis page is still in باب الفاء: the entries are (الفُسكول والفُسكُول والفُسْكُل), (الفُشار), (الفاشِريّ), (الفاشِرْشير), (الفَشّ) «الكساء الغليظ الرقيق الغزل تعريب پَش», (الفَلاتج), (الفالُوذ). There is NO entry for القبّة or any q-b-b word on this page; باب القاف only begins on p. 123.\nEOF\ngrep -n \"قبه:\\|قبة:\" MON_part1.txt MON_part2.txt | head",
 "description": "Save AFM p120 note, grep Mo'in for qobbe"
}
```


## [2026-09-05T20:43:18.878Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%D8%A8%D9%87/",
 "prompt": "Report the entries for قبه: فرهنگ معین (with bracketed origin tag such as [ع.]) and دهخدا, including plural قباب and any etymological remark. Quote the Persian."
}
```


### [2026-09-05T20:43:18.989Z] TOOL RESULT

```
MON_part1.txt:6878:اتفاقبه: (-)۵بورآ-رقاعاات [ع.] (ص نسب. نث) 
MON_part1.txt:38433:مهذب (کتب پیشینیان). تحریر رقبه: آزاد 
MON_part1.txt:46176:نقبه: 0:0 (ع. ثشقبة] (.) سوراخ 
MON_part1.txt:68085:رقبه: (ه)هحادره؟ [ع.] .( گردن؛ ج. رقاب» 
MON_part1.txt:97170:عقبه: [ع. . عقمه ] (ا.) راه دشوار در 
MON_part2.txt:11351:قبه: (0-)02 ۲۵۱2 [ع. قه | .۲ با رگاهی که سر 
MON_part2.txt:54039:مرقبه: (ه)دطمودن [ع. مرقه ] (.) جای
```


### [2026-09-05T20:43:27.562Z] TOOL RESULT

```
# Lexicographic Entries for قبه

## فرهنگ معین
**(قُ بَّ ) [ع. قبة]** (اِ. ) 
"برآمدگی ، بنایی که سقف آن برآمده و گرد باشد. ج . قباب"
(A protrusion; a structure with a raised, rounded ceiling. Plural: قباب)

The etymological tag [ع.] indicates Arabic origin.

## دهخدا
**(قبة) [ق ُب ْ ب َ] (ع اِ )**
"قبه. برآمدگی هر چیز راگویند"
(The prominence/protrusion of anything)

Also defined as: "بنای گرد برآورده چون گنبد"
(A rounded, elevated structure like a dome)

**Plural forms:** قُبَب، قِباب (qubab, qibab)

The entry notes multiple specialized meanings, including a Bedouin barber's tool, a shepherd's thousand-tent enclosure, and various poetic metaphorical uses for celestial phenomena.
```


## [2026-09-05T20:43:36.715Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON qobbe ===\"; sed -n '11351,11360p' MON_part2.txt\necho \"=== WLD gal- call ===\"; grep -n \"gal-\" WLD_band3.txt | head -5; grep -n \"^gal\\|gal-so\\|galgh\\|glagh\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20\necho \"=== KLN call ===\"; grep -n \"^call, v\" KLN_1971.txt | head -3\necho \"=== SKT call ===\"; grep -n -i \"CALL, to cry\" SKT.txt | head -3",
 "description": "Mo'in qobbe, Walde-Pokorny gal, Klein/Skeat call"
}
```


### [2026-09-05T20:43:36.816Z] TOOL RESULT

```
=== MON qobbe ===
قبه: (0-)02 ۲۵۱2 [ع. قه | .۲ با رگاهی که سر 
فراز آن گنبدی باشد. سقف برجسته و 
مدون گنبد. قهٌ آب: (کد.) قنة بادین: (کد.) 
ظ. حباب يا گردباد که به شکل قبه نماید 
(معارف بهاء‌ولد ۴۸۵). قبةٌ پرگل: جام 
شراب. قبً زبرجد (زبرجدین): (کد.) 
آسمان. قبهٌ زربفت: ( کن.) آسمان در شب پر 
ستار ه. ی (کد.) عمود 
تج قبه ششم: کی اتمان » فلک 
ششم. قبة علیاز (کد.) فلکد. قبة گرردنده 
=== WLD gal- call ===
3118:242 rufen jhowd- — echersen Leid- rulen @howd- 529, | San wa- 512°, gdr- ba7. sauber ork iio", 8. gal- B38. euner wiro-e 513*. pal. Log Bauer werden bra Na l. mew. S23*_. bdel- 119°. Ruhe 2. afi- 457", 1. eeu- 405°. hu 2 ore 144. Sau leied- 405° 3 el. 152, 3 wus 5147, 2. rem- 371" echaben 2. gone G2. (beliaglich) gMepe 510. debh- Gd0 goy- 530. a r- 150". Rundung 1, g2¢t- G71, hhrti~ 14° ranzeln 1, (s}ger-- 865". réd- SO0*. aygerely( h)- (awep- G50" iss". Sthaden dap, yee ruplen (Walla) 2 peb’- 16°, pan ped - ego Sohaden sfiinapeet ee ee Rute ejrdd- 285, | sebddiyen 17 pr Gal. ae aal: - 40°, Aver- S60 g- 442°, ie : bey O° hilegaume) 2. yeie- 240 tie) | dele 58. des ia  dAreugh- 874 sohfimen{siah) aig*h- 7. qeyti. 24th. pehairfen b'di- 454. 2. rete Ho a 513 on 74". > Sack (aus Foll) moter 303". | hd SUT eiien aeg- 450*, Sclivitatong Lb. pte 508 a. sthher. B70" schiumeni jee rape a pe r grant A} ad- 4H4*, Bohn 2..a+ iso. opi-e 157
6200:galbus, lit. raibas „bunt“ neben rainas; Brugmann Grdr. II 2 1, 388 f.), ist 
9110:gall. Renos „Rhein“ (ob auch nach Stokes KZ. 37, 260 ir. riasc „a marsh", 
12339:gall, uer-tragus „eine ArtsehnellffiSiger Hunde“ Ver-cingeto-rij- (das inselkelt. 
12800:gall. Jovinc-illus, -a fidg. * utuuh'js, s. u.), nacli dem Komp. -Sup. zu kelt. 
13600:gall. Vaelo , Vailico. Vgl. Fick II 4 259. Uber arm. gail „Wolf“, welches 
24347:gall, camisia niichststehendj ; eher hierher als zu qem- „w61ben‘" <s. d. : auch 
26473:gall. y.ovQfu ,,Bier" usw. s. u. *ker- „brennen“. 
33887:gal- 
33914:„klagen“; mir. glam „Geschrei. Fluch“ (*glagh-sma; allenfalls als *jlag->md 
36354:gall. Boduo-geuus, Litugenms (z. B. Fick II 4 UOf.j, air. ingen , ogom. ini- 
37322:gala- ( *goro -) „Schilf, Strick“, wohl auch garala-m „ein Biindel Gras“ 
39243:galbinus „grfingelb“, galbulus „ein so gefarbter Yogel; CypressennuB 41 (wenn 
39412:galanda, galasti „scharfen, schleifen“, lett. galuods „Wetzstein w , pr. glan- 
39546:galiicha, gah f. „Spafi, Gelachter“, nagalih „taktmaBig schreien, singen, 
39557:galveren, golveren „schallen, heulen 44 ); lit. gulbinti „riihmen, preisen 44 , daher 
41700:glogli- : glagh- „Stachel, Spitze". 
42167:gall. Bitu-rlijes d. i. „Weltkonige“ (vgl. o. die ahnliche Bed. von av. yaedcl) 2 ): 
42520:gallertartige Dingo", norw. rndartl. kvabb, \p)kvrq> ..breiartige schleimige 
42735:gall.-lat. battuo „schlage“ gehoren, wobei die Bed. -Yerschiebung von 
43682:gall.-lat. galba und got. Jcil-pei „Hutterleib“ usw.). Nach Zupitza Gutt. 77, 
=== KLN call ===
=== SKT call ===
```


## [2026-09-05T20:43:40.188Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '33880,33930p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Print Walde-Pokorny gal- entry"
}
```


### [2026-09-05T20:43:40.234Z] TOOL RESULT

```
aus der gr. Sippe von y.d/laiov „Hahnenbart“. — Ganz fraglich ist, ob 
lat. gloria ,,Ruhm“, glnris r ,,uvl)<)/jr/og u (Gloss.) nach Bezzenberger BB. 
2. 156, Stolz IF. 10 , 70 f., Yf. LEWb. 2 340f. auf Grund einer Basis *g e)ld- 
mit s- oder r-Formans entfernter verwandt sind. 



gal- 


539 


Dazu wohl als Erweiterungen: 

idg. *g lag- : gr. y/«£co „lasse einen Gesang erklingen 11 (*ylayiio); gal. 
glag „Gerausch von etwas fallendem“, nir. glagan „Hiihlengeklapper“ 
(vgl. u. engl. clack- ), vielleicht air. glam s. u.; anord. Idaho „zwitschern“, 
ags. clacu „Kampfgetose, Streit“, ferner mehrfach mit Anwendung auf 
drohnenden, klatschenden Schlag, mkd. Mac „Handeklatschen, Ivnall, Krach, 
RiG“, kleckrn „mit einem Knalle treffen, bersten“, nd. klak „Knall Ge- 
riiusch von Schliigen“, engl. clack „klappern, rasseln, plaudern“, norw. 
mdartl. klakka „scklagen, klopfen, klatschen, knallen“, klekkja til „zu- 
schlagen“, anord. klakk-sarr „wund“, und m. d. Bed. „klatschend anwerfen, 
beklecksen“, mhd. Mac auch „Ivlecks, Pleck“, mnd. klacken „Ivleckse 
machen“ (nhd. kleckstn , Klecks = nd. klciklcs ), anord. klcikkr „Klecks, Ivlum- 
pen, Wolkchen 41 . — Zupitza Gutt. 211 m. Lit., Fick III 3 4 55, Falk-Torp 
u. klak; ai. g&rjati „ briillt, brummt, braust“ (Prellwitz 2 95 zw.) hat wohl 
idg. /•, s. *ger - ; 

idg. *gal-gh-, g(a)la x gh- „klagen, sehelten“ : ai. garhati, -te „klagt, tadelt“, 
garJta „Tadel“, av. g wrozaiti „klagt, jammert“, osset. yilrzun „stohnen“, 
av. np. gile „Klage“ (Horn Np. Et. 208); ahd. klaga „Klage“, klagon 

„klagen“; mir. glam „Geschrei. Fluch“ (*glagh-sma; allenfalls als *jlag->md 
zur Wzf. glag-, die aber sonst nicht gerade fur „Klage“ verwendet er- 
scheint). — Zupitza Gutt. 82, Fick II 4 119, Stokes BB. 20, 17, Falk-Torp 
u. Kluge, Klak. Gr. fjhjyj) 'Lit. bei Boisacq s. v.) gehort zu lie- „bloken“; 

nasaliert *glengh - : ahd. klingan „ldingen, tonen l ‘ (ohne naheren Zs- 
hang mit lat. clangor , gr. y.layyt) „Klang“), woneben mit germ. Tenuis 
ahd. klinlcan ds., engl. clink, schwed. klinka „klimpern“ (s. Fick III 4 56, 
Falk-Torp u. klinge, llinke). 

Im Germ, aufierdem *kalt-, *klut-, *klap- (s. Fick III 4 41, 55, 56), z. B. 
mhd. kaizen , lei mi „schwatzen, plappern“ (air. adgladur „rede an“ aber 
zu gr. y.eyldda); afries. kaltia „sprechen“; ags. clatrian „klappern, rasseln “, 
nhd. Klats „Sclimutzfleck“, hckletzen; anord. klupp n. „Ivlatsch, Schlag“, 
ahd. klapf m. „Geschwatz, Ivnall, Schlag, StoB“. 

Ygl. die iihnlichen Schallwzln. ghcl-, kel-.
```


## [2026-09-05T20:43:50.333Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD gal- rufen (above) ===\"; sed -n '33840,33882p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== IEC ===\"; grep -n \"galsos\\|kalla\\|\\\"call\\\"\" IEC.txt | head -10",
 "description": "WLD gal- rufen section, Mann IEC"
}
```


### [2026-09-05T20:43:50.403Z] TOOL RESULT

```
=== WLD gal- rufen (above) ===
Aksl. ijlava nicht besser zu anord. hollr „abgerundeter Gipfel, Kopf“ 
(s. Falk-Torp u. holl m. Lit.; neuerdings wieder Persson Beitr. 932; Wz. *gcl- 
„ballen Ll , *gleu- Hirt Abl. 119); aueh nicht besser zu arm. glux, gen . glxoy 
„Kopf“ (Fick BB. 1, 173, Pedersen KZ. 39, 152, Trautmann Bsl. Wb. 77, 
der als arm. Gdf. gholii-qho ansetzt; wieder anders fiber das arm. Wort 
Scheftelowitz BB. 28, 157; 29, 44, 54 1 ; gegen Iljinskij's Afsl. Ph. 29, 166 un- 
richtige Analyse von aksl. goh s. z. B. Petersson Sprakl. Uppsatser IY, 143. 

Als Anlautdubletten sucht man mit sehr zweifelhaftem Rechte zu ver- 
einigen die Sippe von lat. calvus (s. q e huo- „kahl“) (Zupitza Gutt. 144, 
KZ. 37, 389, Lewy KZ. 40, 420), andrerseits anord. shalli m. „kahler Kopf“, 
shollottr „kahl“ (Fick III 4 416, Falk-Torp u. shaldet, shalle; , unter Tren- 
nung von norw. shalle „Schadel“, die aber mindestens bedenklich ist. 

2. gal- „rufen, schreien“. 

Cymr. gahv „rufen, vorladen 1 ', mbret. gain „appeP‘, mir. gall „Rubm“ 
(*gal-no-s; nur in einem nicht hgg. Glossar, Fick II 4 107). wohl auch gall 
„Sehwan“ idas wegen seines a kaum zu ghcl- in anord. gjallu „er- 
tonen"‘ u. dgl.) ; aksl . glagoljg, glagolati „reden, sprechen“, glagoh „Wort“, 
russ. gologolih ,,plappern, scherzen“ (nicht wahrscheinlicher zu got. goljan 
„begrfi6en“, ahd. galan „singen“, Wz. ghel-, s. Berneker 321); vielleicht 
ai. gar gar a- h „ein bestimmtes Musikinstrument“ (— aksl. glagoh, wenn mit 
r aus idg. /, Meillet Et. 229; oder zu *ger- oder *g1er-, was beim Keben- 
einander dieser Schallwurzeln nicht auszumachen ist, vgl. von noch einer 
andern solchen ai. gharghara- „rasselnd, gurgelnd; m. Larin “). 

*gal-sn- (zum Formans -so- in Worten iihnlicher Bed. s. Berneker 323) 
in osset. yalas „<ro)r>] u (Hfibschmann Osset. Spr. 33), aksl. glash , russ. golosb 
,.Stimme“, lit. galsas „Widerhall“ (Endzelin KZ. 52, 124), anord. hall n. 
„das Rufen“, wovon hallci „rufen, singen“, ags. callian (engl. call ) ds., 
ahd. hallon „viel und laut sprechen, schwatzen“, mit -ll- aus -Is-, wo- 
neben -Is- in anord. halls n. „ Aufreizung“, mnd . holsen ( *hcilsdn ) „plaudern„ 
— Curtius 1 77 f., Fortunatov BB. 6, 218, Noreen Urg.Ltl. 123, Zupitza Gutt. 
143, Trautmann Bsl. Wb. 77. 

Aber lat. gallus „IIahn“ kaum als „(Frfih)sanger, Kraher“ hierher, son- 
dern entweder nach Wilamowitz Phil. Unters. I 78, Niedermann IA. 18, 7S 
als „der Gallier“ bezeichnet (wie bei den Griechen als Mrjdog oder Ileo- 
oiy.og) oder eher erst nachtraglich an den Galliernamen angelehntes Lw. 
aus der gr. Sippe von y.d/laiov „Hahnenbart“. — Ganz fraglich ist, ob 
lat. gloria ,,Ruhm“, glnris r ,,uvl)<)/jr/og u (Gloss.) nach Bezzenberger BB. 
2. 156, Stolz IF. 10 , 70 f., Yf. LEWb. 2 340f. auf Grund einer Basis *g e)ld- 
=== IEC ===
3869:Li. gagü, eti. Cf. *gagaio in Blg. gagam; Latv. gagaju, id. gagos (gaglis) ‘knob, lump, berry’; as adj. *lumpish, boorish’ Alb. gogël “berry, oakapple'; gogé ‘boorish’; Sw. koka (&clod'. Ambig. cf. gogos); Li. gõgas ‘Jump, hump; withers’; Icel. kaekur, m. (' vice. Mod. -æ- for ON -ce-) gāið (1) ‘croak, caw'. WP I, 526. Cf. gauið, gouo Skt. gāyāmi ‘sing’; cf. G kaien ‘prattle’; keien “blub, weep’; OCS gajọ, ati ‘croak, caw’ gāið (2), see gígāmi gàios, à (1) “raucousness, cawing; jay, mag- pie, or other raucous bird’. WP I, 526. Cf. gaio (1) Skt. gayah ‘song’; Arm. čaj, Lat (jay, with induced palatalism); Lat. gaius, gaia “jay, mag- pie; G (short vowel) Kai ‘prattle’; Norw. Sw. Scots kaja, kaie, kae ‘jackdaw’; E caw; R gaj ‘caw’. Cf. Ukr. Zaj-voronok Clark fr. *gēi-); Pol. ga-wron, Cz. ha-vran ‘raven’ gaios, om (2) ‘pace, gait'. Cf. gígàmi, ghàio. WP I, 526 & 677 Skt. gayah, adj. ‘striding’; Av. gàyom ('pace', also 'yard-measure)); (ambig.) Cz. hej-no, OCz. hajno ‘flock’; (ambig.) cf. Li. góju, son ‘amble, wade’; Latv. (ambig.) gāju Cl went, but Arm. gaci, id. is fr. ghai-, q.v.); cf. also gājums ‘gait, track’; gājējs ‘pedestrian’ galdāið, galdeio ‘bawl, exuit, howl’. Skt. gardāmi, Av. garəd- (1); Alb. (denom.) galdoj ‘exult’; Lat. gallo, are (‘rave���, but poss. denom. of gallus, cf. gagol-); MHG kalzen, kelzen *bawl'; kelz “loud talk’; OFris. kaltia “talk”; Du. kouten chat": kout, s. id.; R. cf. galdét ('brawl', but the phonol. is irregular) galið *shout'. Cf. gald-, galu- Gk. cf. a-gállo ‘glorify’; MHG kallen ‘shout, chatter, sing, croak’; Du. G kallen ‘chatter’; LG kohlen, id.; Tirol. kallen ‘bellow, rut; OE ceallian: ON kalla (“calP', etc.). Cf. also Alb. galé ‘rook’; Br. gal-dü “black sea-bird"; OE -calla *-crier'. (Ambig. or variant in Skt. járe, Av. jar- ‘creak, rustle; call’, cf. &el-) galuó ‘call’. Cf. galið, gald-; galuos, s. Skt. cf. garvah ‘pride’; Br. galv ‘appeal’; W galw ‘call, vocation’; Ir. (?) gailbh ‘squall’;
4569:ghaloros ‘distorted, wrong, awry’. (Variant: ghalon-) Arm. galar 'twisted'; Hitt. kallaras, kallar (queried: “bad, monstrous); Gk. khalarós ‘slack’; Mir galar “disease, grief, affliction’; W. Cor. galar ‘sorrow’. Cf. (variant: *ghalon- in) W galan ‘corpse’; Sw. galen ‘wrong’
14160:quolos, -es- “turning, turn, wheel, axis, centre, community'. WP I, 515 and cf. I, 464. Cf. quol- extns. and queló Arm. cf. olor, Let, (twist, curl", fr. *quolesi-); Myc. -qoro-; Gk. pólos, m. 'axis, globe, dial, round chaplet’; cf. oneiro-pólos ‘interpreter of dreams; Alb. cf. kalla- in kalla-tumba *head- over-heels'; Thrac. cf. kól-abros ‘a dance’ be- side koléa, id. (if fr. *quoleso. Hes.); Lat. colus gs: -1, and -üs, f. 'spinning-wheeP" beside in-
15448:Alb. ambig.) Hitt. cf. skallai(mi), v. (queried: “split'); Gk. cf. skállo, v. “hoe, harrow, rake’; skaleús, m. ‘hoe’; Alb. halë, f. *pine-needle; scale; awn; prickle; splinter; flake of chaff; W ysgall, pl. ‘thistles’; Cor. ascal, id.; Br. cf. askol, m. Cthistle', perh. fr. *aK-skol-); Go. skalja, f. ‘stile’: MHG schal(e), s & wf. “shell, cup’; OE scealu, sciell, f. *shell, husk; scale; scale-pan'; WG Schall, f. “bolt, bar; Du. schel, f. ‘scale, glaucoma’; G. dial. Schelle (beside Schale), f. ‘dish’; ON skel, plur. -jar, f. ‘shell’ beside skál, pl. -ir, f. “bowl, scale-pan'; OCS skoli- ka ‘shell’; R cf. o-skólok, m. ‘splinter, chip’; Li. skalà, f. id.; skalüs ‘fissile’; Latv. skals (1log: Li. skàálas, id.)
15542:skel- (1) (skelið, skh-) “divide, distinguish, discern; split, division”, etc. Cf. skel-, skil-, skol- (skhel-, etc.), and skál-. WP II, 592 Alb. cf. cel, v. Copen’, fr. *skhelijo); LLat. *sce- lio, Ere, v. (“choose in It. sceglere, pp: scelto); OFris. skilla, v. ‘quarrel’; LG schelen, v. fdis- tinguish'; Du. schelen, v. ‘differ’; Li. skeliü, skélti, v. ‘split; Latv. Skelu, Skelt, id. (NB. There is some confusion in Gmc. between types *skel- and *skil-, q.v.). O-gde in Hitt. skalla(imi), v. (queried: ‘split, têar’). Nominal types: Arm. xelk, g: xelac, ab. xelawk, pl. ‘brain’; OE scelle & scielle, f. ‘cutting, separa- tion’; LG schel, f. ‘difference, separation, boundary’; R scel', f. ‘chink, slit’; Latv. cf. Skelte, id.; Sw. skål, n. “faculty of reason?
15766:skol- (1) o-gde variant of type skel-, q.v. in Hitt. skallai(mi), v. (queried: 'split); Arm. cf. (redup.) xoy-xoyem, v. ‘slaughter’; Gk. skó- los, m. ‘thorn’; cf. skol-ópax, -ópakos, m. (^woodcock,, if for “bent-bill', cf. opák-); Alb. halë, pl. a f. (scale, prickle, awn, splinter, pine-needle'; pl. "chatt: Mir, cf. scoltaim, v. ‘split’; Ir. scoltad, s. ‘splitting’; W ysgol, pl. -ion, f. (1) ‘peak’; Br. cf. askol, m. (‘thistle’, for *aK-skol-, but cf. W ysgall, coll. id. fr. *skal-); OHG skala, f. ‘shell, scale’; ON skál, pl. at -ir, f. ‘scale; bowl’; Go. skalja, f. (tile: E shell); OE scealu, f. ‘shell, husk; dish’; Fris. skale, s. ‘furrow dividing fields’; G cf. zer- schellen, v. ‘shatter’; Sw. skól, m. ‘rift, gorge’; OCS cf. skolíka, f. 'shel; R o-skólok, m. ‘splinter, chip’; Cz. skolek, m. ‘splint, stake’; skoliti, inf. (2) ‘kill’; Li. skalà, f. as R.; skalùs, adj. ‘fissile’ beside (e-gde) skélti, inf. ('split'. See skel-); Latv. skals, m. “log? beside skaldīt, inf. ‘split’; cf. also LG schal, f. *hoof-disease in horses'
```


## [2026-09-05T20:43:57.998Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"kalla\" KLN_1971.txt | head -5\necho \"--- SKT ---\"; grep -n \"kalla\" SKT.txt | head -5\necho \"--- SYN ---\"; grep -n \"kalla\\|ceallian\" SYN.txt | head -8",
 "description": "Klein/Skeat/Buck for call"
}
```


### [2026-09-05T20:43:58.072Z] TOOL RESULT

```
37449:lian, ‘to shout’, rel. to ON. kalla , ‘to shout, 
51276:kallai , ‘to break’. Arm. celum, ‘I cleave, split*, 
103062:OSlav. glagolu is cogn. with ON. kalla, ‘to 
--- SKT ---
--- SYN ---
1438:k. opt He dpéa, Goth. brunna Lith.  Saltinis, versmé; Se alone uN : ON kelda, brunnr $ulinys , Lat. fons; puleus Dan.  kilde; brénd Lett. avuots; aka, acina It. fonte, sorgente; pozzo Sw. kalla; brunn ChSl. istotinikii; studentct, Fr, source; puits OE wella, spryng; pytt ; kladgzt Sp. Suente; pozo ME _ welle, spring SCr. —zzvor, vrelo; studenac Rum. zvor; put, finting NE spring; well Boh. pramen, z¥idlo, zdroj; Ir. topur Du. wel, bron; put studné Nir. tobar OHG  brunno, ursprinc; Pol. 4rédlo, zdréj; studnia W. fynnon, pydew pfuzzt Russ. kljué, rodnik, istot- Br. elenenn, mammenn; MHG brunne, sprinc; pfutze nik; kolodec
31499:Grk.  Bodw, xpafw, xpavyatw Goth. hropjan, wopjan Lith. rékti, Saukti NG = gwvatw ON epa, kalla, hropa Lett. kliegt, sauke Lat. clamare Dan. raabe ChSl. vitpiti, vitztipiti, kpy It. gridare Sw. ropa tati 1s Fy. crier OE hryman, clipian, hrd- = SCr. _kritati, vikatj Sp. gritar pan Boh. —kiiéeti Rum. siriga, {ipa ME _ shoute, reme, clepe, Pol. —kerzyczeé Ir. gatrim rope Russ. kriéat’ NIr. _gairim, glaodhaim, NE _ shout, cry Skt. krue- screadaim Du. schreeuwen, roepen Av. xraos- W. bloeddio OHG  (h)ruofan, harén, Br. krial scrian
31524:ON kalla, also ‘call, summon’ = OF callian (once; ME calle, NE call, prob. fr, ON), OHG callén ‘talk much or loud, chatter’ : ChSl. glasti ‘voice’, ete. (18.11). Walde-P. 1.538. Falk-Torp 485f. NED s.v. call.
32132:Grk. = xadéiw Goth. haitan Lith.  Saukti NG guvdtw, kpatw, ahd ON kalla Lett.  saukt Lat. vocdre Dan. _kalde ChSl.  (pri)ztivati It. chiamare Sw. kalla SCr. zati Fy. appeler Or clipian, ciegan Boh.  volati Sp. lamar ME _clepe, calle Pol. wolaé Rum. chema NE call Russ. vat’ I. (do-)gatrim Du. _—roepen Skt.  hva- NIx. = gairim, gairmim OHG (h)ruofan, halon Av. zav- W. galw MHG ruofen
32144:W. galw, MBr. galu, Br. gervel (pple. galvet, cf. galv sb. ‘call, summons’; Pe- dersen 1.491): ON kalla ‘shout, call, claim’, Dan. kalde, Sw. kalla, OE (rare) callian, ME calle, NE call ‘call’, OHG kallon ‘speak loudly or much, gossip’, ChSl. glagolati ‘speak’, glast% ‘voice’. Walde-P. 1.538. Falk-Torp 485.
32146:ON kalla, etc. : W. galw, ete. (above, 3). Mae clipian, ME clepe ‘shout’ (18.18) and ‘call’.
32161:Grk. xadéw, dvouatw Goth. haitan, namnjan Lith. vadinti NG  A€yu, dvopatw ON heita (also b), kalla Lett.  saukt Lat.  vocdre Dan. _kalde, hede (b) ChSl.  nareSti It. chiamare Sw. kalla, heta (b) SCr. nazvati Tr. appeler OE hdtan (also b), cli- Boh. nazvatz Sp. lamar pian, nemnan Pol. nazwaé Rum. chema ME hote, hight (esp. b), Russ. nazvat’ Ir. gatrim (?) clepe, calle nemne Skt. abhi-dha- Nir.  gairim NE call, name W. galw Du. noemen, heeten (b) Br. gervel (or phrase with OHG _heizan (also b)
```


## [2026-09-05T20:44:13.886Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nsed -n '37440,37460p' data/verification/sources/refs/KLN_1971.txt\nmkdir -p data/verification/sources/refs/ocr/BOOK\npdftoppm -f 166 -l 166 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/166\nls -la data/verification/sources/refs/ocr/BOOK/166.png",
 "description": "Klein call entry; render book page 166"
}
```


### [2026-09-05T20:44:15.902Z] TOOL RESULT

```
calk, n., projections at the ends of horseshoes to 
prevent slipping. — Back formation fr. calkin. 

calkin, n., calk (in the sense of prec. word). — 
OF. calcain , fr. L. calcanqym, ‘heel’, fr. calx, 
gen. calcis, ‘heel’. See calcaneum. 

call, intr. and tr. v. — ME. callen , fr. OE. ceal- 
lian, ‘to shout’, rel. to ON. kalla , ‘to shout, 
sing’, Du. kallen, ‘to talk’, OHG. kallon , ‘to 
call’, and cogn. with Mir. gall, ‘glory; swan’, 
W. galw, ‘to call’, OSlav. glasii (for * got sit), 
‘voice’, Czech and Slovak bias, of s.m., OSlav. 
glasiti, ‘to cry, announce’, Czech hlasiti , Slo- 
vak hlasit\ of s.m., OSlav. glagolu , ‘word’, 
Czech and Slovak hlahol , ‘loud talk’, OSlav. 
glagolati, ‘to speak’, Czech hlaholiti, Slovak 
hlaholiV , ‘to sound’. Cp. Glagolitic. 
Derivatives: call, n., call-able , adj., caller (q.v.), 
call-ing , n. 
-rw-rw-r-- 1 sfmqrb sfmqrb 60832 Sep  5 16:44 data/verification/sources/refs/ocr/BOOK/166.png
```


## [2026-09-05T20:44:17.930Z] TOOL CALL #50: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/166.png"
}
```


### [2026-09-05T20:44:18.261Z] TOOL RESULT

```

```


## [2026-09-05T20:44:18.259Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:45:05.080Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%BE%DB%8C%D8%AF%D9%86/",
 "prompt": "Report all dictionary senses of کپیدن (Dehkhoda and Mo'in): does any sense mean \"to heap up / pile up\" (کپه کردن، توده کردن) and/or \"to sleep\"? Quote the Persian."
}
```


## [2026-09-05T20:45:08.450Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TYL local ===\"; grep -n -i \"alcove\\|qubba\" incoming/TYL/TYL_Taylor1934_BenJonson_pages.txt | head\necho \"=== HJB alcove ===\"; grep -n -i \"^ALCOVE\\|alcove\" HJB.txt | head -5\necho \"=== FSD alcove ===\"; grep -n -i \"alcove\" FSD_vol1.txt | head -3\necho \"=== WEB alcove ===\"; grep -n -i \"alcove\" WEB_vol1.txt | head -3",
 "description": "Check Taylor, Hobson-Jobson, Funk&Wagnalls, Webster for alcove"
}
```


### [2026-09-05T20:45:08.545Z] TOOL RESULT

```
=== TYL local ===
=== HJB alcove ===
1678:ALCOVE,
1699:ALCOVE,  s.  This  English  word comes  to  us  through  the  Span,  alcova and  Fr.  alcove  (old  Fr.  aucvhe\  from Ar.  aUkuhbahy  applied  first  to  a  kind of  tent*  (so  in  Hebr.  Ntmbers  xxv.  8) and  then  to  a  vaulted  building  or recess.     An  edifice  of  Saracenic  con-
23538:Alcatraz,  106,  11a Alchah,  13a,  6,  57a Alchore,  4096 Aloorana,  116 Alcove,  116 Aldea,    Ald^e,    12a,
=== FSD alcove ===
11420:1.  A   covered  recess  (originally  vaulted)  connected  with or  at  the  side  of  a   larger  room;  specifically,  a   recess  for a   bed;  also,  a   compartment  for  books  in  a   large  library; hence,  any  embowered  or  secluded  spot;  as,  **  the  al- coves of  death.*'  Holmes  Parting  Health  st.  4. Great-eyed  gazelles  in  runny  alcoves  browsed The  blown  red  rosea.  E.  Arnold  Light  of  ^D£a  bk.  ii.Bt.J-i
23590:abacus nbamurus abat-jour abat-vent abutment acanthus acropolis acroterlura adytum aisle alcazar alcove alette olurc
48038:Bret  Habte  Thankful  Blossom  pt.  ii,  p.  35.  [o.  a   co.  1877.J 4f.  An  inner  room:  opposed  to  hall.  [   <   AS.  bur,  chamber. <   buan,  dwell.]  bourt;  bowret-  Syn.:  alcove,  arbor, boudo!r,recess, retreat.—  bow'er*maId",n.  [Poet.]  A   lady’s chambermaid;  tirewoman,  b.smaldenj;  b.*womanf.— b. ethane,  n.  In  early  English  history,  a   chamberlain.— bow'er-let,  n.  [Rare.]  A   small  bower.
=== WEB alcove ===
5131:al-, in Arabic, a prefix, corresponding to the Italian il, and the Spanish el and la. equiva- lent to the English definite article, the; as, Alkoran, the Koran, or the book; alcove, al- chemy, alembic, almanac.
16878:1. an opening or alcove marked off by pil- lars, columns, etc.
16943:bay win’dōw, 1.a window or series of win- dows usually rising from the ground and pro- jecting from the wall, forming an alcove or recess within. :
```


### [2026-09-05T20:45:10.941Z] TOOL RESULT

```
# Dictionary Senses of کپیدن

Based on the Dehkhoda and Mo'in dictionary entries provided:

**Sleep sense:** Yes, both dictionaries include this meaning.
- Dehkhoda: "خفتن. خوابیدن. تمرگیدن" (to sleep/doze)
- Mo'in: "۱ - خفتن ، خوابیدن" (to sleep)

**Heap/pile up sense:** No evidence of this meaning appears in either dictionary entry shown.

The senses documented are:
1. To sleep/rest
2. To steal/snatch (ربودن، دزدیدن)
3. To take/grab (برداشتن)

The provided content does not include any definition corresponding to "کپه کردن" (heaping or piling up).
```


## [2026-09-05T20:45:41.128Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB glk / garz ===\"; grep -n \"glk\\|garz\\|gilak\" NYB_vol2_glossary.txt | head -10\necho \"=== BQT کبه/کپه ===\"; python3 - <<'EOF'\nimport glob\nfor f in ['incoming/BQT/BQT_v3_pages.txt','incoming/BQT/BQT_v4_pages.txt']:\n    d=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    for i,p in enumerate(d):\n        if 'کبه' in p or 'کپه' in p:\n            print(f,i,[l for l in p.split('\\n') if 'کبه' in l or 'کپه' in l][:2])\nEOF",
 "description": "Nyberg garz, Borhan kabbe/kappe"
}
```


### [2026-09-05T20:45:42.983Z] TOOL RESULT

```
=== NYB glk / garz ===
1643:garzišn ([glešn'] wailing. lamentation, complaint 95°; used as pred. = pres. 3d p. pl. 982°. — Paz. garzašni; NP garziš. — V. girzitan.
1662:gil- pres. 3d p. sg. gilēt wrongly written ‘HDWN-yt' for gylyt', which also could be read girét (from griftan): to weep, to complain 1021, — < "girdet < *grd-, SW form of girz-, v. girzitan, garzitan and gristan; another instance of wrong *HDWN- v. *gir-. — From *grd- also
1663:gilak [gylk'] distress 761, — Paz. gila, Skr. v. aparddha; NP gilah ‘complaint, re- proach’, cf MPrs gylg’y ‘complaining’ (S, cf s. v. cašm-kāt).
1669:girzitan [gyleytn'] to complain, to lament 6119, — girz- < *gyz-, Av. (516) garaz-, pres. goroz-; NW form; SW form gil-, gristan, subst. gilak (v. these ws.); v. also garzitan.
1717:gristan [glystn; BKYWN-stn'] . griy- (BKYWN-], pt. pret. 3d p. grist [glyst', BKYWN-st'], to weep, to cry, to lament 111’. 7418-26 (Paz. substitutes here vagined, cf vàng); be ~ to burst out crying 1138. 3417.18, 511.4, �� gristan < *griy-istan formed from the pres. griy- < *grady-; * grad- SW form of garz-, v. girzitan and gil-. Ps. pt. glydyt = gliyit, pres. glydty = griyet; MPrs pres. gryy-; NP giristan giry-. Verbum 204 sq.
2602:must [mwst', inscr. mwsty] violation, outrage: ~ u gilak 761; api-š ... must u dróg andar nést and there is no violation and no lie (fraud) in it (= in the passage, i.e., to be feared when passing over the bridge) F:7; [~ u adātihā i-Sän patiš kunénd violation and iniguities which they commit against them (viz. water and fire) JN 16%]. — Paz. must, Skr. v. balätkära (Mx), possibly SW form < mušti- from Skr mus- ‘to rob, to steal, to plunder’; not identical with NP must, v. S. v. mödak.
5987:gylg’y: cašm-kāi, gilak
6602:garzašni: garzišn
6609:gila: gilak
7144:garziš: garzišn
=== BQT کبه/کپه ===
incoming/BQT/BQT_v3_pages.txt 98 ['کنونی قصبه\u200cایست دارای چند دکان وکبه\u200cهای کوچك وبك دبتان . رودشاور \u200epail\u200f آن گذرد.']
incoming/BQT/BQT_v3_pages.txt 382 ['\u200f. کبه \u200eel\u200f بنم اول و فتح انی مشدد »']
incoming/BQT/BQT_v3_pages.txt 385 ['\u200f۴ کبه (هم) .']
incoming/BQT/BQT_v3_pages.txt 405 ['«کربه\u200cبوزن ومعنی\u200cکبه». . ۷- درفهرست مخزن\u200cلادوبهآمده: « کربه, بفارسی\u200cنبائیست \u200ees VS\u200f']
incoming/BQT/BQT_v3_pages.txt 420 ['\u200fرود است. رك: کبهان. جفرافیای طبیعی ص٩۸ \u200ete\u200f نز = کرند \u200eKis)\u200f رنگرزان ) :']
incoming/BQT/BQT_v3_pages.txt 471 ['\u200f۱ - در فارسی \u200ekolombi\u200f و ۷۵۱0603 (کپه , توده, جمع شده ) درخراسان« کلنبه»']
incoming/BQT/BQT_v3_pages.txt 496 ['\u200esigs (\u200f اصاف ) باشد » به از : کند (شجاع) + آور (آورنده) چه آور در \u200eALT\u200f فرکبه ازاسم']
incoming/BQT/BQT_v3_pages.txt 529 ['کو کبه \u200epc =F\u200f اول و ثالت و بای', 'است . ۴- (عی) «ک وکبه » ستار؛ بزرکه - وکروه مردم .> « منتهی\u200cآلارب > -']
incoming/BQT/BQT_v4_pages.txt 242 ['۷ - (عر) « نکب محرکة . ظلع بالیمیر » و قیل داء یأخة الابل فی\u200cمناکبها تطلع مته']
```


## [2026-09-05T20:45:54.131Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nd=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=d[382]\nprint(p[:2600])\nEOF",
 "description": "Print BQT leaf 382 (kabbe entry)"
}
```


### [2026-09-05T20:45:55.914Z] TOOL RESULT

```
[pdf page 383]
کبود پشت
رسیده و ثالك بالف "کشیده و ‎Ope‏ زده » دم
قربه‌ایست از مضافات لیشابور ‎٩‏ - و تخمی باشد
که آترا ‎al Le‏ خوالند .
کبوود پشت؟ = بنمبای‌فارسی‌وسکون
‎oot‏ ونای فرشت . کنابه ازآسمان است.
کبود حصاد - بسنی کبود ‎ct‏
‏است ۳ کهکنابه از آسمان باشد.

‎OF‏ - با دال ‎aml‏ بروزن کبوتر»

‎. ‏ماهیان کوچكخورند؛‎ VT, ‏باشددرآب‎ OS

‏وبستی گویند مرغی است آبی وماهی‌خوار ‎WT,‏
‏بوتیمارخوانند ؛ وجممی گوبند کرمی‌است‌بز رکه
وماهی خوار که جز درشب پیدا نشود وروزمخفی
باشد ۴ .

‏کبود طشت * ۰ بنتح طای حطی .
کنابه از آسمان است .

‏کبوده = بر وزن نبوده » نام چوپان
افراسیاب بوده ۷ - ردرختی باشد بز رکک۷ که
‎oT‏ لطیف و خوش آینده باشد ؛ و بعضی

‏(۱) چك » چش : و .

‏مهو ات

‏کوند درخث پشه غال است - و لوعی ازیید ,

‏هست ؛ وبسی گونند درخت بیدمشك است.

‏کبوس ۸ ۰ با راو مجهول بر وزن
مجوس » بمعن ی کج وناراست ‎ath‏ . ودرفرهنگه
جهانگیری باین معنی بجای حرف ثالی‌بای‌حطی
هم‌آمده است .

‏کبوكه ‎٩‏ @ بفتح اولرئانی ‎sly‏ کشیده
‎Gy‏ زده ؛ مرغی است کبود رنگه بمقدارباشه.
‎SS‏ با هم جنس خود جفت نشود ؛ وبسنی
کویند مرفی است آبی وسرخ رنگه ‎UTS‏
‏سرخاب گویند وترکان عنقد خوانند - و بتشدید
تانی ‎Aske‏ باش دکه عربان ابوالءلیش‌خوانند.

‏. کبه ‎el‏ بنم اول و فتح انی مشدد »

‏شيشه با شاخ با کدوبی باشد که حجامان آنرابر
محل حجامت نهند و بمکند ۱۱ و معربآن‌قبه
است - و برآمدکی هرچیز را 55 گوینداوبفیس
تشدید هم درست است ؛ و پفتح اول نیز بنظر
‎oul‏ است؛ وبا بای فارسی هم هست.

‎٩‏ - در معجم البلدان یاقوت آمده : « کبوزان بذال معجمه و آخر آن نون ؛ موضی
است .> ۴ - مصحف : «کبود تشت, یمتی آسمان » « رشیدی »- کبود طشت ( «م. )

‎. ‏تشت وخایه < طشت وخایه‎ oS ‏طشت‎ : dy

‎“tert

‏۴ -«کبودر »کرمکی بود خرد درآب . خورش او ماهی خرد بود (ظ . وخورش‌ماهی

‎: ‏دهشدا ( رودکی (سمرفندی ) کوید‎ . oy
‏ماهی آسان گرد کبودر ۰ گوبی‎
Cem) ‏تشت‎ oy Sm 6

‏بولت ماهی است دشمنانت کبودر. < افت قری*۱۹ *.
۱ رك : فهرست ولف .

‎Populus 2102 - ۲‏ درختی از نوع ‎hae‏ ازتیرء بیدها «گل گلاب ۲۷۲ .

‎. ۳۲۱ ‏-قی :کردی ۷۵002 ( فوزی ,کوژ ) « ژابا‎ A

‎٩‏ = «کپوك » مرغی است آسمان کون » چند باشد و او را از جنس خود جفت نبود.
کرد مرغان کردد تأ از ابشان بچه‌آرد . منجيك (ترمذی) گوید :

‏خارش ‎ST‏ و بضوی اندر غمی شده

‏همچون کپوك خواستمی جفت کام‌کام.

‎. ‏حمچون کبوك خاسته می‌جست کامکام ) » « لغت فرس ۲۸5 -۷ ۴ . فس: کبوتر‎ : JO)

‏۶- رك : قبه .

‎aly gb wy‏ بمکد وال

‎Looe 4 Som ۱‏ حجامان بود. معروقی گوید :
کیرتو کوش ‎Soe‏ مکد ‎Sy‏

‎. ٩ ۵۷ ‏فرس‎ cal?
```


## [2026-09-05T20:46:13.177Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in 'https://en.wiktionary.org/wiki/%DA%AF%D9%84%D9%87' 'https://abadis.ir/fatofa/%DA%A9%D9%BE%D9%87/' 'https://abadis.ir/fatofa/%DA%A9%D8%A8%D9%87/' 'https://abadis.ir/fatofa/%D9%82%D8%A8%D9%87/' 'https://abadis.ir/fatofa/%DA%A9%D9%BE%DB%8C%D8%AF%D9%86/'; do\npython3 tools/fetch_source.py \"$u\" --note 'page 166: Gabbah/Gal charts — Persian dictionary entries (Mo'\"'\"'in, Dehkhoda) / Wiktionary gele' 2>&1 | tail -1\ndone",
 "description": "Archive Persian dictionary sources"
}
```


## [2026-09-05T20:46:14.742Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/call",
 "prompt": "Give the full etymology of the verb \"call\": Old English ceallian, Old Norse kalla, Proto-Germanic *kall-, PIE root *gal- \"to call, shout\". Quote it."
}
```


### [2026-09-05T20:46:22.405Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fe4d7242d254c000.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/95d409a4b8635303.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/188e923ed17aa763.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8449120afe6569e9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65e8b91a91836dfd.txt
```


### [2026-09-05T20:46:28.441Z] TOOL RESULT

```
# Etymology of "Call" (Verb)

Based on the Online Etymology Dictionary, here's the full etymological chain:

The verb "call" traces back through multiple language layers:

**Quote:** "mid-13c., _callen_, 'cry out; call for, summon, invoke; ask for, demand, order; give a name to, apply by way of designation,' from Old Norse _kalla_ 'cry loudly, summon in a loud voice; name, call by name,' reconstructed to be from Proto-Germanic _\*kall-_" (127 characters)

The path continues further back: Proto-Germanic *kall- derives from the Proto-Indo-European root *gal-, which means "to call, shout." 

The document also notes that Old English had the cognate term "ceallian" (meaning to shout or utter loudly), though this was "late and rare," with "clipian" being the more common Old English expression for calling.
```


## [2026-09-05T20:46:31.555Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/call' --note 'page 166, entry 2 nodes 4-5: call < ON kalla < PGmc *kall- < PIE *gal-' 2>&1 | tail -1",
 "description": "Archive etymonline call"
}
```


### [2026-09-05T20:46:33.730Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/47de9c6bfa16315d.txt
```


## [2026-09-05T20:47:51.047Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN kubbe/kappe/gunbad ===\"; grep -n -i \"kubbe\\|kappe\\|gunbad\\|gumbad\" HRN.txt | head\necho \"=== HUB ===\"; grep -n -i \"kubbe\\|qubba\\|gunbad\" HUB.txt | head\necho \"=== PLA arabic script قبة ===\"; grep -n \"قبة\\|qubba\\|Kuppel\" incoming/PLA/PLA_pages.txt | head\necho \"=== PLA count lines ===\"; wc -l incoming/PLA/PLA_pages.txt\necho \"=== TAD قبة ===\"; grep -n \"( القبة\\|القبة )\" TAD_pages.txt | head",
 "description": "Check silence of Horn, Hübschmann, Asbaghi"
}
```


### [2026-09-05T20:47:51.138Z] TOOL RESULT

```
=== HRN kubbe/kappe/gunbad ===
22731:engl.! ^0 kappen 119.
=== HUB ===
=== PLA arabic script قبة ===
5410:Be Zu £umbad:                           "Kuppel"             aus    dem       pers.         >)        gumbad mp.         >£r gumbad             .
10824:Sb -     täqg:         "Mauerbogen,                   Gewölbe,           Kuppel"              —      pers. st t äg ?            mp. ur         täg            ”.
=== PLA count lines ===
16026 incoming/PLA/PLA_pages.txt
=== TAD قبة ===
```


## [2026-09-05T20:47:58.160Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\ni=d.find('Zu £umbad')\nprint(d[max(0,i-1200):i+400])\nEOF",
 "description": "Print Asbaghi gumbad context"
}
```


### [2026-09-05T20:47:59.966Z] TOOL RESULT

```
        ?.


    orL» - Banäbiza:                              Pl.    v.    ZU         $änbäz            s.    bänbäz.

ads             - Kanäbiza:                       Pl. v.       IL, Banbaz s. Banbaz.

     >wier-             Zanäabid:               Pl.     v. =>           Zumbad        s.     Zumbad.

ei» -           Bunäh:                "Sünde"           aus    dem       pers.        oLS        gonah     2 <np.       au]    vinäs    3, mand.
                     4
           gunah              .


    &,>\o - $anädira:                             Pl.    v. ‚I. Zandär                 s.        Zandär.

„ur -           &unnär:                 "Granatblüte"                   aus    dem     pers.           ‚LUX golnar      > Ss. $ulnär        mit       reg.
           tot.          ass.           v.l zun.


„ie -           ginär:                "Platane"              aus    dem       pers.        Lo         &enär   mp        1?    %inär    6,


re - $anäzir:                                   Pl. Vene                $anzir s. Zanzir 7,

.                   .                                                                            P4                                         8
Be Zu £umbad:                           "Kuppel"             aus    dem       pers.         >)        gumbad mp.         >£r gumbad             .


tn         -    $ambaz:                 "einer,          der       zu    teuer       verkauft!"            aus   dem   pers.    PTR     Eänbäz          9,


    bs -        Kambaz:                 "sich          wie    ein       Scharlatan               b
```


## [2026-09-05T20:48:07.444Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\ni=d.find('Zu £umbad')\ntags=[(m.start(),m.group(0)) for m in re.finditer(r'\\[pdf page \\d+\\]',d) if m.start()<i]\nprint(tags[-1] if tags else 'no tags', ' | leaf idx:', d[:i].count('\\f'))\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['PLA']['page_offset'])\"",
 "description": "Locate Asbaghi page"
}
```


### [2026-09-05T20:48:09.506Z] TOOL RESULT

```
no tags  | leaf idx: 106
301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
```


## [2026-09-05T20:48:21.073Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:54:38.628Z] TOOL CALL #61: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk166.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\ndata = {\n \"pdf_page\": 166,\n \"book_page\": 136,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Gabbah\",\n   \"verdict\": \"disputed\",\n   \"modern_form\": \"no Iranian *gabbah- is attested anywhere; the family is Arabic قبّة qubba(t) 'dome, vault, vaulted tent', a regular noun of the Semitic geminate root q-b-b 'to be bent, vaulted' (Hebrew qubbāh Num. 25:8, Syriac qubbəṯā, Akkadian qabābu 'shield'), by some accounts an Aramaic loan into Arabic\",\n   \"note\": \"Nourai's citation is accurate: Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba p. 123, s.v. القبّة, does say «تعريب كُبَّه واصل معناها كاس الحجامة وتُطلَق على انتفاخ كلّ شيء واعتلائه كالقبّة» — i.e. Arabic qubba is an Arabicization of Persian kubba 'cupping-glass', extended to the swelling ('blister') and doming of anything; that sentence is where Nourai's gloss 'dome, vault, blister' comes from. Borhan-e Qate' (p. 1585, s.v. کبه) says the same from the Persian side: «معرّب آن قبّه است». But this is the old Persian-lexicographic tradition, not modern scholarship. Klein p. 46 (the reference Nourai himself quotes in the chart's NOTE), Hobson-Jobson pp. 11-12, Fraenkel and Wiktionary all make qubba Semitic: Akkadian qabābu and Hebrew qubbāh (Numbers 25:8, the 'vaulted tent' Phinehas enters) antedate any Iranian-Arabic contact, and the root q-b-b is fully productive in Arabic (qabba 'it was arched', qibāb, qubayba). Asbaghi's Persische Lehnwörter im Arabischen (1988), the standard modern inventory, does not list qubba at all; the Persian 'dome' word it does list is Arabic ǧumbad/ǧunbaḏ < Persian gumbad (p. 92). The only modern echo of an Iranian source is Lokotsch no. 1221's parenthesis '[Möglicherweise geht das ar. Grundwort selbst auf pers. gunbäd zurück, ZDMG L, 646]' — and that would be گنبد gunbad, not a *gabbah. Finally the root's own shape is Nourai's: even Addi Shir writes the Persian word with k- (كُبَّه), never g-.\",\n   \"note_fa\": \"نورایی ریشه‌ای ایرانی به صورت «Gabbah» با معنای «گنبد، طاق، تاول» فرض کرده و مأخذش ادّی شیر است. ارجاع او درست است: ادّی شیر در «الالفاظ الفارسیة المعرّبة» ص ۱۲۳ ذیل «القبّة» می‌نویسد «تعریب کُبّه و اصل معناها کاس الحجامة و تُطلَق علی انتفاخ کلّ شیء»، و برهان قاطع (ص ۱۵۸۵ ذیل «کبه») هم می‌گوید «معرّب آن قبّه است»؛ همین دو جمله سرچشمهٔ معنای سه‌گانهٔ نمودار است. اما این ادعا از سنت فرهنگ‌نویسی فارسی می‌آید نه از پژوهش امروزی: کلاین (ص ۴۶)، هابسن-جابسن (ص ۱۱–۱۲)، فرنکل و ویکی‌واژه قبّه را واژه‌ای سامی از ریشهٔ مضاعف ق‌ب‌ب می‌دانند، با هم‌ریشه‌های عبری qubbāh (سِفر اعداد ۲۵:۸)، سریانی qubbəṯā و اکدی qabābu «سپر» که همگی پیش از هرگونه تماس ایرانی‑عربی گواهی شده‌اند. اصباغی در «وام‌واژه‌های فارسی در عربی» (۱۹۸۸) قبّه را اصلاً در فهرست وام‌واژه‌ها نیاورده و واژهٔ فارسی «گنبد» را همان جُمبَذ/جُنبَذ عربی می‌داند (ص ۹۲). افزون بر این هیچ صورت ایرانی با g آغازین (*gabbah) در جایی گواهی نشده و خودِ ادّی شیر آن را با ک می‌نویسد؛ پس ریشهٔ نمودار ساختهٔ نورایی است و پژوهش امروزی آن را رد می‌کند.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D9%82%D8%A8%D8%A9\",\n    \"https://www.etymonline.com/word/alcove\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"AFM:123\", \"status\": \"supports\",\n     \"note\": \"Verified on the page image (AFM.pdf pdf-page 125 = printed ١٢٣; PNG + transcription saved as data/verification/sources/refs/ocr/AFM/0123.png and 0123.vision.txt). باب القاف opens on this page and the second entry reads: «* (القُبَّة) تعريب كُبَّه واصل معناها كاس الحجامة وتُطلَق على انتفاخ كلّ شيء واعتلائه كالقبّة وغيرها ومنه الكرديّ كُبَّه وهو ورم يُحدث في عنق الغنم غالباً». That is exactly Nourai's root: a Persian kubba behind Arabic qubba, with the three senses 'dome / vault / blister (swelling)'. Addi Shir writes the Persian etymon with k-, not g-.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966, p. 46 s.v. alcove (KLN_1966.txt \\\\f-leaf 36; KLN_1971.txt line 10681)\", \"stance\": \"contradicts\",\n     \"note\": \"'alcove … fr. Sp. alcoba, fr. Arab. al-qubbah, fr. al-, \\\"the\\\", and qubbah, \\\"arch, vaulted tent\\\", which is rel. to Arab. qabba, \\\"it was bent\\\", and to Heb. qubbāʾ, \\\"vaulted tent\\\", Syr. qebhabhbā, \\\"vault, vaulted tent\\\", Akkad. qababu, \\\"shield\\\". All these words are derivatives of the Sem. base q-b-b, \\\"to be bent, crooked, vaulted\\\".' No Iranian element.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen, p. ~274 (AFA.txt line 9596)\", \"stance\": \"contradicts\",\n     \"note\": \"'aram. [qubbəṯā] … dann »Kuppel« entspricht arabischem قبّة, also muss بيعة fremd sein' — Fraenkel uses Arabic qubba as the inherited Semitic counterpart of the Aramaic word, i.e. it is native/Aramaic, not Iranian.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, p. 92 (PLA_pages.txt leaf 107) and passim\", \"stance\": \"contradicts\",\n     \"note\": \"Asbaghi's inventory has 'ǧumbad: \\\"Kuppel\\\" aus dem pers. gumbad, mp. gumbad' but contains no entry qubba at all — the standard modern list of Persian loanwords in Arabic does not regard qubba as one.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch 1927, no. 1221 'Ar. kubba' (LKT.txt line 2867)\", \"stance\": \"partial\",\n     \"note\": \"'Ar. kubba: \\\"Gewölbe\\\", jedes gewölbte Gebäude … hieraus zum Teil mit ar. Art. sp. alcoba, pg. alcova … frz. alcôve … engl. alcove'; and in square brackets '[Möglicherweise geht das ar. Grundwort selbst auf pers. gunbäd zurück, ZDMG L, 646.]' — the only modern trace of an Iranian source, and it names گنبد gunbad, not *gabbah.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' printed p. ~1585 (BQT_v3_pages.txt leaf 382, pdf 383), s.v. کبه\", \"stance\": \"supports\",\n     \"note\": \"«کبه: بضم اول و فتح ثانی مشدد، شیشه یا شاخ یا کدویی باشد که حجامان آنرا بر محل حجامت نهند و بمکند، و معرّبِ آن قبّه است — و برآمدگی هر چیز را کبه گویند»; Mo'in's footnote 6 only cross-refers «رک: قبه». So the Persian tradition (Borhan, and Addi Shir after it) does claim Persian → Arabic, but offers no Old/Middle Iranian form.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"kobbeh «کبّه ( کپّه )»; kapîdan «کپیدن ۱»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The box conflates two unrelated Persian words and gives a verb a sense no dictionary knows. (a) کبّه kabba/kobba is, in Borhan-e Qate' (p. 1585) and Dehkhoda, 'the glass, horn or gourd a cupper sets on the cupping-place and sucks with' and, by extension, 'the protuberance of anything' — never 'pile, heap'; both lexica add «معرّبش قبّه است», i.e. they see the Arabic qubba as its Arabicization, and Mo'in's own entry glosses کبه as «= کپه: ۱ برآمدگی، قبه؛ ۲ شاخ حجامت», explicitly equating it with Arabic قبه. Since Arabic qubba is a Semitic q-b-b noun (Akkadian qabābu, Hebrew qubbāh), the traffic is more plausibly the other way: Persian کبّه is the Arabic word taken back with k for q, a common substitution in Persian (cf. کبیتا/قبیط). (b) کپّه kappe 'heap, pile' is a different word: Mo'in tags it [= کوپه] «تودهٔ روی هم انباشته، تل شده», i.e. a variant of کوپه kūpa 'mound, heap', with nothing vaulted about it; Nourai has taken his gloss 'pile, heap' from this word and attached it to کبّه. (c) کپیدن is glossed by Mo'in «خفتن، خوابیدن» (colloquial, pejorative 'to sleep') and secondarily «ربودن، دزدیدن» ('to snatch, steal'); Dehkhoda has 'خفتن، خوابیدن، تمرگیدن'. No source gives 'to pile up'. So neither the gloss nor the descent from an Iranian *gabbah stands.\",\n     \"derivation_fa\": \"این جعبه دو واژهٔ جدا را یکی گرفته و به فعلی معنایی داده که در هیچ فرهنگی نیست. نخست «کبّه»: برهان قاطع (ص ۱۵۸۵) و دهخدا آن را «شیشه یا شاخ یا کدویی که حجامان بر محل حجامت نهند» و سپس «برآمدگی هر چیز» معنی کرده‌اند، نه «توده و انباشته»؛ و هر دو می‌افزایند «معرّبش قبّه است» و معین هم آن را برابر «برآمدگی، قبه» گذاشته است. چون قبّهٔ عربی واژه‌ای سامی از ریشهٔ ق‌ب‌ب است (با هم‌ریشه‌های اکدی qabābu و عبری qubbāh)، جهت وام‌گیری وارونه است: «کبّه»ی فارسی همان قبّهٔ عربی است که با ابدال ق به ک بازگرفته شده (مانند قبیط/کبیتا). دوم «کپّه» به معنی «تودهٔ روی هم انباشته» واژهٔ دیگری است که معین آن را گونهٔ «کوپه» می‌داند و ربطی به گنبد و طاق ندارد؛ معنای «pile, heap» در نمودار از همین واژه گرفته شده و به «کبّه» چسبیده است. سوم «کپیدن» در فرهنگ معین «خفتن، خوابیدن» (عامیانه و تحقیرآمیز) و «ربودن، دزدیدن» است و در دهخدا «خفتن، خوابیدن، تمرگیدن»؛ معنای «توده کردن» برای آن در هیچ مأخذی نیامده. پس هم معنای گره و هم انتسابش به ریشهٔ فرضی ایرانی مردود است.\",\n     \"sources\": [\n      \"https://abadis.ir/fatofa/%DA%A9%D9%BE%D9%87/\",\n      \"https://abadis.ir/fatofa/%DA%A9%D8%A8%D9%87/\",\n      \"https://abadis.ir/fatofa/%DA%A9%D9%BE%DB%8C%D8%AF%D9%86/\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:2894,2898\", \"status\": \"partial\",\n       \"note\": \"The 6-volume Mo'in pagination cannot be checked (only the 2-vol. Adena abridgement, MON_part1/2, and the entry texts on abadis/vajehyab are available), but the entries themselves are: «کبه (کُ یا کَ بّ) = کُپّه: ۱ برآمدگی، قبه؛ ۲ شاخ حجامت» and «کپه (کُ پِّ) [= کوپه] تودهٔ روی هم انباشته، تل شده» and «کپیدن (کَ دَ) ۱ خفتن، خوابیدن؛ ۲ ربودن، دزدیدن». Mo'in therefore supports the existence of the words but gives 'heap' only for کپه (deriving it from کوپه) and 'to sleep', not 'to pile up', for کپیدن.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.vv. کبه، کپه، کپیدن (abadis.ir; MON_part2.txt lines 20302, 20467, 20535)\", \"stance\": \"partial\",\n       \"note\": \"«کپه: (کُ پِّ) (اِ.) (عا.) روی هم انباشته شده، تل شده، کبه» / «کبه … = کُپّه: ۱ برآمدگی، قبه؛ ۲ شاخ حجامت» / «کپیدن … (عا.) خوابیدن (در مقام تحقیر)». The bracket [= کوپه] on کپه is Mo'in's only etymological statement; there is no Iranian *gabbah anywhere.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. ~1585 s.v. کبه (BQT_v3_pages.txt leaf 382)\", \"stance\": \"partial\",\n       \"note\": \"«کبه … شیشه یا شاخ یا کدویی باشد که حجامان آنرا بر محل حجامت نهند و بمکند و معرّب آن قبّه است — و برآمدگی هر چیز را کبه گویند». Supports the Persian→Arabic tradition but not the glosses 'pile, heap' / 'to pile up'.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie — grep for kubbe/kappe/gunbad\", \"stance\": \"silent\",\n       \"note\": \"Horn has no article on کبه/کپه/کپیدن at all (the only hit for 'kappe' is the English word 'to cap' at no. 119); the words are not part of the inherited Iranian lexicon he treats.\"},\n      {\"src\": \"ARY\", \"where\": \"Dehkhoda, Loghatnāme s.v. کپه / کبه (abadis.ir)\", \"stance\": \"partial\",\n       \"note\": \"«کپه … (اِ) کبه. قبه» and «کبه: شیشه یا شاخ یا کدو که حجامان بر موضع حجامت نهند … معربش قبه است»; «کپیدن: خفتن، خوابیدن، تمرگیدن». Dehkhoda equates کپه/کبه/قبه but nowhere glosses کپیدن 'to pile up'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Arabic\",\n     \"words\": \"qabbah; al-qubbah; q.b.b\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The three items are real Arabic: qabba (qabb-) 'it was arched, bent', the geminate root q-b-b, and al-qubba(t) 'the dome, the vaulted tent' (pl. qibāb/qubab). What is disputed is the arrow: Nourai has them descend from an Iranian *gabbah, while the whole Semitic comparison points inward. Klein p. 46 — the very page Nourai quotes in the chart's own NOTE — lists Hebrew qubbāh 'vaulted tent' (Numbers 25:8, the tent Phinehas enters, quoted in Hobson-Jobson s.v. alcove), Syriac qebhabhbā 'vault, vaulted tent' and Akkadian qabābu 'shield' as derivatives of the same base q-b-b 'to be bent, crooked, vaulted'; Akkadian and Biblical Hebrew are centuries older than any Persian-Arabic contact. Fraenkel treats Arabic qubba as the native counterpart of Aramaic qubbəṯā, and Wiktionary now makes the Arabic noun a borrowing from Aramaic qubbəṯā — Semitic either way. Asbaghi 1988, the standard list of Persian loans in Arabic, does not include qubba; the Persian 'dome' word that really was borrowed is gumbad > Arabic ǧumbad/ǧunbaḏ (Asbaghi p. 92). Nourai's own note therefore records the view that modern scholarship holds, and his chart contradicts it.\",\n     \"derivation_fa\": \"هر سه صورتِ این جعبه عربیِ اصیل‌اند: فعل قَبَّ «خمید، طاق‌وار شد»، ریشهٔ مضاعف ق‌ب‌ب، و القُبّة «گنبد، خیمهٔ طاق‌دار» (جمع: قِباب/قُبَب). آنچه محل ایراد است پیکانِ نمودار است، یعنی برآمدن این‌ها از ریشهٔ فرضیِ ایرانی. کلاین در همان ص ۴۶ که نورایی در یادداشتِ نمودار نقل کرده، عبری qubbāh «خیمهٔ طاق‌دار» (سِفر اعداد ۲۵:۸)، سریانی qebabbā و اکدی qabābu «سپر» را مشتقات همین ریشهٔ سامی می‌شمارد؛ گواهی اکدی و عبری قرن‌ها پیش از هر تماس فارسی‑عربی است. فرنکل نیز قبّهٔ عربی را برابرِ بومیِ قوبّتای آرامی می‌داند و ویکی‌واژه امروز آن را وام‌واژه‌ای از آرامی می‌شمارد؛ در هر دو صورت سامی است نه ایرانی. اصباغی هم قبّه را در فهرست وام‌واژه‌های فارسی نیاورده و تنها «گنبد» را به‌صورت جُمبَذ عربی ثبت کرده است. پس ادعای نورایی را پژوهش امروزی رد می‌کند و یادداشت خودِ او دیدگاه درست را نقل کرده است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%82%D8%A8%D8%A9\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"FVF:520\", \"status\": \"not_checked\",\n       \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi (Tehran 1347): no digital copy on any permitted platform (refs_online.json lists only noorlib/ketabnak viewers behind a login).\"},\n      {\"ref\": \"AFM:120\", \"status\": \"not_found\",\n       \"note\": \"Checked the page image (AFM.pdf pdf-page 122 = printed ١٢٠; saved as data/verification/sources/refs/ocr/AFM/0120.png + 0120.vision.txt): p. 120 is still inside باب الفاء (الفسكول، الفشار، الفاشريّ، الفاشرشير، الفشّ، الفلاتج، الفالوذ) and contains no q-b-b word. باب القاف and the القبّة entry begin on p. 123 — the page Nourai cites for the root box. The node's page number is off by three.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 46 s.v. alcove (KLN_1966.txt leaf 36)\", \"stance\": \"contradicts\",\n       \"note\": \"'…qubbah, \\\"arch, vaulted tent\\\", which is rel. to Arab. qabba, \\\"it was bent\\\", and to Heb. qubbāʾ, \\\"vaulted tent\\\", Syr. qebhabhbā …, Akkad. qababu, \\\"shield\\\". All these words are derivatives of the Sem. base q-b-b, \\\"to be bent, crooked, vaulted\\\".'\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson pp. 11-12 s.v. ALCOVE (HJB.txt line 1699)\", \"stance\": \"contradicts\",\n       \"note\": \"'This English word comes to us through the Span. alcova and Fr. alcove (old Fr. aucube) from Ar. al-kubbah, applied first to a kind of tent (so in Hebr. Numbers xxv. 8) and then to a vaulted building or recess.' The Hebrew attestation is decisive against an Iranian source.\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Aram. Fremdwörter im Arabischen (AFA.txt line 9596)\", \"stance\": \"contradicts\",\n       \"note\": \"'aram. … dann »Kuppel« entspricht arabischem قبّة' — the Arabic word is treated as the regular Semitic counterpart of the Aramaic one.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi 1988, p. 92 (PLA_pages.txt leaf 107)\", \"stance\": \"contradicts\",\n       \"note\": \"'ǧumbad: \\\"Kuppel\\\" aus dem pers. gumbad, mp. gumbad' is the Persian dome-word Asbaghi records as an Arabic loan; qubba is absent from his whole inventory.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"qobbeh «قبّه ( قباب )»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian قبّه qobbe 'dome, cupola, boss' is a straightforward Arabic loan of the ʿAbbasid period, taken over with its Arabic broken plural قباب qibāb (the chart's parenthesis) — the normal treatment of Arabic nouns in literary Persian. Mo'in tags it «[ع. قبة] برآمدگی؛ بنایی که سقف آن برآمده و گرد باشد. ج. قباب» and Dehkhoda «(ع اِ) برآمدگی هر چیز؛ بنای گرد برآورده چون گنبد», both marking it explicitly as Arabic; the inherited Persian word for the same thing is گنبد gonbad (MP gumbad), which is why Persian keeps both. The arrow Arabic → Persian is thus correct even though the arrow above it (Iranian → Arabic) is not; on the majority view the pair کبّه/قبّه in Persian is a single Arabic word taken in twice.\",\n     \"derivation_fa\": \"«قبّه» در فارسی نو وام‌واژه‌ای عربی است که همراه با جمع مکسّر عربی‌اش «قِباب» (همان که در نمودار در کمانک آمده) گرفته شده است؛ این شیوهٔ معمولِ ورود اسم‌های عربی به فارسی ادبی است. معین آن را با نشانهٔ «[ع. قبة]» می‌آورد: «برآمدگی؛ بنایی که سقف آن برآمده و گرد باشد. ج: قباب»، و دهخدا نیز «(ع اِ) برآمدگی هر چیز؛ بنای گرد برآورده چون گنبد». واژهٔ بومی فارسی برای همین معنا «گنبد» (فارسی میانه gumbad) است و به همین سبب هر دو در فارسی به‌کار می‌روند. پس این پیکان (عربی ← فارسی) درست است، هرچند پیکان بالای آن (ایرانی ← عربی) نادرست است.\",\n     \"sources\": [\n      \"https://abadis.ir/fatofa/%D9%82%D8%A8%D9%87/\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:2637\", \"status\": \"supports\",\n       \"note\": \"The 6-vol. page number itself is not verifiable (only the 2-vol. abridgement and the online entry text), but Mo'in's entry is exactly what the node claims: MON_part2.txt line 11351 «قبه: [ع. قبة] بارگاهی که سرفراز آن گنبدی باشد؛ سقف برجسته و مدوّر؛ گنبد … قبهٔ زبرجد: (کن.) آسمان», and abadis' Mo'in text «(قُ بَّ) [ع. قبة] (اِ.) برآمدگی، بنایی که سقف آن برآمده و گرد باشد. ج. قباب» — Arabic origin and the plural قباب both confirmed.\"},\n      {\"ref\": \"VGH:94\", \"status\": \"not_checked\",\n       \"note\": \"Khadiv Jam, Vazhe-name-ye Ghazalha-ye Hafez: not on archive.org; only a login-walled ketabnak PDF (refs_online.json).\"},\n      {\"ref\": \"FVA:323\", \"status\": \"not_checked\",\n       \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi: no digital copy found on any permitted platform (re-searched 2026-09 per refs_online.json).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. قبه (abadis.ir; MON_part2.txt line 11351)\", \"stance\": \"supports\",\n       \"note\": \"«قبه: (قُ بَّ) [ع. قبة] (اِ.) برآمدگی، بنایی که سقف آن برآمده و گرد باشد. ج. قباب» — the [ع.] tag is Mo'in's marker for an Arabic loan.\"},\n      {\"src\": \"ARY\", \"where\": \"Dehkhoda, Loghatnāme s.v. قبه (abadis.ir)\", \"stance\": \"supports\",\n       \"note\": \"«قبة. [ق ُب ْ ب َ] (ع اِ) قبه. برآمدگی هر چیز راگویند … بنای گرد برآورده چون گنبد»; plural forms قُبَب، قِباب. Marked (ع اِ) = Arabic noun.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. ~1585, footnote 6 to کبه (BQT_v3_pages.txt leaf 382)\", \"stance\": \"supports\",\n       \"note\": \"Mo'in's footnote simply cross-refers «رک: قبه», i.e. he treats Persian کبه and قبه as the same word, the latter in Arabic dress.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Spanish\",\n     \"words\": \"alcoba\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Spanish alcoba 'sleeping recess, small vaulted chamber' is the Andalusi-Arabic al-qubba taken over with the article agglutinated, the standard shape of Arabisms in Ibero-Romance (cf. alcázar, aldea, alcohol); the Arabic word had already developed in Spain the sense 'small side-room, bed alcove' (Lokotsch no. 1221; Lane, cited by Devic). The form shows the regular Ibero-Romance treatment of Arabic q by [k] and of the geminate -bb- by simple -b-, with -a for Arabic tāʾ marbūṭa. Attested in Castilian from the 13th-14th c. and continued by Portuguese alcova, Catalan alcova, Provençal alcuba 'tent'.\",\n     \"derivation_fa\": \"«alcoba»ی اسپانیایی همان «القُبّة» عربیِ اندلسی است که با حرف تعریف al- یک‌جا وام گرفته شده؛ این شکل، صورتِ معمولِ عربی‌واژه‌ها در زبان‌های شبه‌جزیرهٔ ایبری است (مانند alcázar، aldea، alcohol). واژهٔ عربی در اندلس پیش‌تر معنای «اتاقک کناری، جای خواب» یافته بود (لوکوچ، شمارهٔ ۱۲۲۱). دگرگونی‌های آوایی همه قاعده‌مندند: ق عربی به k، مشدّدِ -bb- به -b- ساده، و تاء مربوطه به -a. صورت‌های پرتغالی alcova و کاتالانی alcova و پرووانسی alcuba «خیمه» نیز از همین ریشه‌اند.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/alcove\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:46\", \"status\": \"supports\",\n       \"note\": \"Klein 1966 p. 46 (KLN_1966.txt leaf 36): 'alcove … fr. F. alcove, fr. Sp. alcoba, fr. Arab. al-qubbah, fr. al-, \\\"the\\\", and qubbah, \\\"arch, vaulted tent\\\"'. The Spanish step is exactly as drawn.\"}\n      ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1221 (LKT.txt line 2867)\", \"stance\": \"supports\",\n       \"note\": \"'hieraus zum Teil mit ar. Art. sp. alcoba, pg. alcova \\\"Schlafkabinett\\\", kat. alcova, prov. alcuba \\\"Zelt\\\", afrz. aucube …'\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale, p. 14 s.v. Alcôve (DEV.txt line 366)\", \"stance\": \"supports\",\n       \"note\": \"'Alcôve. Esp. alcoba, portug. alcova, ital. alcova, alcovo; de l'arabe القبّة al-qobba, qui, entre autres sens, a celui de petite chambre, cabinet, ainsi que le montre M. Lane.'\"},\n      {\"src\": \"LAM\", \"where\": \"Lammens, Remarques sur les mots français dérivés de l'arabe, p. 8 s.v. Alcôve (LAM.txt line 1372)\", \"stance\": \"supports\",\n       \"note\": \"'Alcôve. Esp. et Ptg: alcoba … Ital: alcova, alcovo, de al-qoubba, qui signifie dôme, et aussi: petite chambre, cabinet, pavillon, et même baldaquin.'\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"French\",\n     \"words\": \"alcove\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"French alcôve was borrowed from Spanish alcoba in the first half of the 17th century, when Spanish court fashion (the curtained bed-recess) reached France; the accent circonflexe marks the long open o of the Spanish stressed syllable and the final -e is the French adaptation of Spanish -a. Pihan explains the chain in exactly those terms: 'le mot arabe qoubbat, précédé de l'article al, a été d'abord adopté par les Espagnols avec l'orthographe alcoba, et s'est introduit ensuite dans le portugais alcova, l'italien alcovo et le français alcôve.' Older French also has aucube 'tent' from the same Arabic word by a separate, earlier route (Lokotsch no. 1221).\",\n     \"derivation_fa\": \"«alcôve»ی فرانسوی در نیمهٔ نخست سدهٔ هفدهم از «alcoba»ی اسپانیایی وام گرفته شد، هم‌زمان با رواج مُدِ درباری اسپانیا (تختِ پرده‌دار در فرورفتگی دیوار) در فرانسه؛ نشانهٔ ^ نمایندهٔ کشیدگی واکهٔ تکیه‌دار اسپانیایی و -e پایانی برابرنهادِ -a اسپانیایی است. پیهان همین زنجیره را روشن بیان می‌کند: واژهٔ عربی qoubbat با حرف تعریف al نخست در اسپانیایی به‌صورت alcoba پذیرفته شد و سپس به پرتغالی alcova، ایتالیایی alcovo و فرانسوی alcôve راه یافت. صورت کهن‌ترِ فرانسوی aucube «خیمه» از همان واژهٔ عربی است اما از راهی جداگانه و پیش‌تر (لوکوچ ۱۲۲۱).\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/alcove\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:46\", \"status\": \"supports\",\n       \"note\": \"Klein p. 46: 'alcove … — F. alcove, fr. Sp. alcoba' — the French step as drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHN\", \"where\": \"Pihan, Dict. étym. des mots … dérivés de l'arabe, du persan ou du turc, p. 21 s.v. ALCÔVE (PHN.txt line 1231)\", \"stance\": \"supports\",\n       \"note\": \"'[alqoubbat] la coupole, la voûte … Le mot arabe qoubbat, précédé de l'article al, a été d'abord adopté par les Espagnols avec l'orthographe alcoba, et s'est introduit ensuite dans le portugais alcova, l'italien alcovo et le français alcôve.'\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1221 (LKT.txt line 2867)\", \"stance\": \"supports\",\n       \"note\": \"'… afrz. aucube \\\"dass.\\\", frz. alcôve \\\"kleines Nebenzimmer\\\", rum. alcove … ndl. alkoof, engl. alcove.'\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"alcove\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English alcove is a 17th-century borrowing of French alcôve (first recorded in the 1670s, in the architectural sense 'recess in a room, esp. one for a bed'), spelled without the accent and pronounced with initial stress. The chain Arabic al-qubbah > Spanish alcoba > French alcôve > English alcove is one of the best-documented Arabisms in English and is given identically by Klein, Hobson-Jobson, Funk & Wagnalls ('a covered recess (originally vaulted) connected with or at the side of a larger room') and Etymonline. The semantic path is 'vaulted tent' → 'vaulted chamber' → 'curtained bed-recess' → 'any recess'.\",\n     \"derivation_fa\": \"«alcove»ی انگلیسی وام‌واژه‌ای از فرانسویِ alcôve در سدهٔ هفدهم است (نخستین کاربرد در دههٔ ۱۶۷۰ به معنای «فرورفتگی اتاق، به‌ویژه جای تخت»)، بدون نشانهٔ ^ و با تکیه بر هجای نخست. زنجیرهٔ القُبّة عربی ← alcoba اسپانیایی ← alcôve فرانسوی ← alcove انگلیسی از مستندترین عربی‌واژه‌های انگلیسی است و کلاین، هابسن‑جابسن، فرهنگ فانک و واگنالز و اتیمآنلاین همگی همین را می‌گویند. سیر معنایی چنین بوده است: «خیمهٔ طاق‌دار» ← «اتاق گنبدی» ← «جای تختِ پرده‌دار» ← «هر فرورفتگی».\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/alcove\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:46\", \"status\": \"supports\",\n       \"note\": \"Klein 1966 p. 46 (leaf 36): 'alcove, n., 1) a recessed section in a room; 2) any recess. — F. alcove, fr. Sp. alcoba, fr. Arab. al-qubbah …' — even Nourai's English gloss is Klein's wording verbatim.\"},\n      {\"ref\": \"TYL:567\", \"status\": \"not_checked\",\n       \"note\": \"W. Taylor, Arabic Words in English (S.P.E. Tract XXXVIII, 1933): not on archive.org and the HathiTrust volume is US-full-view only; the local TYL files cover only Taylor's 1934 Leeds article on Ben Jonson (pp. 44-50), which does not mention alcove.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary s.v. alcove (FSD_vol1.txt line 11420)\", \"stance\": \"supports\",\n       \"note\": \"'1. A covered recess (originally vaulted) connected with or at the side of a larger room; specifically, a recess for a bed; also, a compartment for books in a large library.'\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson pp. 11-12 s.v. ALCOVE (HJB.txt line 1699)\", \"stance\": \"supports\",\n       \"note\": \"'This English word comes to us through the Span. alcova and Fr. alcove (old Fr. aucube) from Ar. al-kubbah …'\"},\n      {\"src\": \"KLN\", \"where\": \"Etymonline s.v. alcove (archived via fetch_source.py)\", \"stance\": \"supports\",\n       \"note\": \"'entered English in the 1670s from French alcôve, which came from Spanish alcoba, from Arabic al-qobbah \\\"the vaulted chamber\\\"; the Arabic root q-b-b means \\\"to be bent, crooked, vaulted\\\".'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Gal, Galgh, Galagh\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *gal- 'to call, shout' (Pokorny 2. gal- 350-351; Watkins gal-²), with the extended bases *gal-so- (> Germanic *kall-) and *gal-gh- / *g(ə)lagh- 'to lament, complain, scold'\",\n   \"note\": \"All three of Nourai's headword shapes are Pokorny's own: IEW 350f. heads '2. gal- \\\"rufen, schreien\\\"' and its section 4 reads 'gal-gh-, g(ə)lagh- \\\"lament, wail, scold, chide\\\"', which is where 'Galgh, Galagh' come from; Walde-Pokorny I 538f. has the identical layout. The language label ('Indo-European') and the gloss ('to shout, complain') are therefore both right, and the page number 351 is right (the entry runs 350-351). One caveat modern scholarship adds: the unity Nourai's chart draws — Iranian gərəz- and Germanic *kall- under one root — is Pokorny's, and Cheung (EDIV 2007: 112, s.v. *garz) writes 'An IE origin of this common IIr. root is uncertain. The Germanic and Irish forms cited by Pokorny, OHG chlaga \\\"complaint\\\" … and OIr. glam \\\"cry, curse\\\", are probably from a substrate source'. Both branches are onomatopoeic-expressive, so the shared root is likely but not provable. Nothing on the page is misprinted; the extraction matches the printed chart exactly (page image at data/verification/sources/refs/ocr/BOOK/166.png).\",\n   \"note_fa\": \"هر سه صورتِ سرواژهٔ نورایی از خودِ پوکورنی گرفته شده است: در «فرهنگ ریشه‌شناختی هندواروپایی» صص ۳۵۰–۳۵۱ مدخل «2. gal- rufen, schreien» آمده و بند چهارم همان مدخل «gal-gh-, g(ə)lagh- klagen, schelten» است؛ یعنی «Galgh» و «Galagh» نیز از همان‌جاست. والده‑پوکورنی (جلد ۱ صص ۵۳۸–۵۳۹) هم دقیقاً همین ساختار را دارد. پس برچسب زبان («هندواروپایی») و معنا («فریاد زدن، شکایت کردن») هر دو درست است و شمارهٔ صفحهٔ ۳۵۱ نیز درست است. تنها احتیاطی که پژوهش امروزی می‌افزاید این است که یکی‌دانستن شاخهٔ ایرانی (garz-) با شاخهٔ ژرمنی (*kall-) از آنِ پوکورنی است و چونگ در «فرهنگ ریشه‌شناختی فعل ایرانی» (ص ۱۱۲) می‌نویسد که خاستگاه هندواروپایی این ریشهٔ مشترکِ هندوایرانی قطعی نیست و صورت‌های ژرمنی و ایرلندی احتمالاً از زبانی زیرلایه‌اند. هر دو شاخه آوایی‑تقلیدی‌اند، پس این پیوند محتمل است ولی اثبات‌ناپذیر.\",\n   \"sources\": [\n    \"https://www.etymonline.com/word/call\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:351\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt lines 29669-29750, 'Root / lemma: gal-2 | Meaning: to call, cry … Page(s): 350-351'. Section 2 gives 'gal-so-: … Old Norse kall \\\"the calls\\\", whereof kalla \\\"call, shout, sing\\\", Old English callian (engl. call)'; section 4 gives 'gal-gh-, g(ə)lagh- \\\"lament, wail, scold, chide\\\": Old Indic garhati … Avestan gərəzaiti \\\"complains, cries, wails\\\", osset. γärz-in \\\"groan\\\", Avestan gərəza, npers. gila \\\"lament\\\"; Old High German klaga \\\"lament\\\"'. Both branches of Nourai's chart stand on this one page.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 538-539 (WLD_Bd1_1930_dli_70244_djvu.txt lines 33862-33925)\", \"stance\": \"supports\",\n     \"note\": \"'2. gal- \\\"rufen, schreien\\\" … *gal-sn- [so-] in osset. γalas … anord. kall n. \\\"das Rufen\\\", wovon kalla \\\"rufen, singen\\\", ags. callian (engl. call) ds., ahd. kallon … idg. *gal-gh-, g(ə)lagh- \\\"klagen, schelten\\\": ai. garhati … av. gərəzaiti \\\"klagt, jammert\\\", osset. γärzun \\\"stöhnen\\\", av. np. gile \\\"Klage\\\" (Horn Np. Et. 208); ahd. klaga \\\"Klage\\\"'. The source Pokorny abridges, and it names both of Nourai's variant roots.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gal-² (AHD_watkins1985.txt line 477)\", \"stance\": \"supports\",\n     \"note\": \"'gal-². To call, shout. 1. Germanic expressive form *kall- in Old Norse kalla, to call: CALL. 2. Germanic *klat- … 3. Expressive form *gall- in Latin gallus, cock … [Pok. 2. gal- 350.]' — same root, same gloss; Watkins does not carry the Iranian branch.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, Indo-European Comparative Dictionary s.vv. galið, galuó (IEC.txt line 3869)\", \"stance\": \"supports\",\n     \"note\": \"'galið \\\"shout\\\". Cf. gald-, galu- … MHG kallen \\\"shout, chatter, sing, croak\\\"; Du. G kallen \\\"chatter\\\" … OE ceallian: ON kalla (\\\"call\\\", etc.)'; and 'galuó \\\"call\\\" … W galw \\\"call, vocation\\\"'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung, Etymological Dictionary of the Iranian Verb, p. 112 s.v. *garz (CHEUNG.txt lines 8113-8150)\", \"stance\": \"partial\",\n     \"note\": \"'*garz \\\"to lament, weep\\\" … AVESTAN gərəz- … NWIR: NP giristan/giriy- \\\"to weep\\\", NP gilah \\\"complaint; lamentation\\\" … SANSKRIT garh \\\"to complain\\\" … An IE origin of this common IIr. root is uncertain. The Germanic and Irish forms cited by Pokorny (l.c.), OHG chlaga \\\"complaint\\\" … are probably from a substrate source.' Confirms the Iranian branch, doubts its union with the Germanic one.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"garez\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"'garez' is Nourai's simplified spelling of Avestan gərəz- 'to complain, lament, wail' — Bartholomae, Altiranisches Wörterbuch col. 515f.: 'j., g. gərəz- V. \\\"klagen\\\"', with the noun gərəzā- f. 'Klage'. It is attested from the Gathas onwards: middle 1sg. gərəzdī/gərəzē (Y 32.9, Y 46.2), injunctive gərəzdā (Y 29.1), Young Avestan gərəzaite (Yt 10.53), optative gərəzaēta (Yt 17.57ff.), participle gərəzāna- (Cheung, EDIV 112). Pokorny 351 cites exactly this form ('Avestan gərəzaiti \\\"complains, cries, wails\\\"') as the Iranian member of *gal-gh-, alongside Old Indic gárhate 'reproaches', so the arrow root → Avestan is the one Nourai's own reference draws. The Avestan verb belongs to the *gal-gh- extension, not to the plain *gal- of the Germanic branch — which is why Nourai's root box lists all three shapes.\",\n     \"derivation_fa\": \"«garez» املای ساده‌شدهٔ نورایی برای فعل اوستایی gərəz- «شکوه کردن، نالیدن» است؛ بارتولمه در «فرهنگ ایرانی باستان» ستون ۵۱۵ آن را «gərəz- V. klagen» و اسمِ آن را gərəzā- «شکوه» آورده است. این فعل از گاهان به بعد گواهی دارد: gərəzdī/gərəzē در یسنا ۳۲:۹ و ۴۶:۲، gərəzdā در یسنا ۲۹:۱، gərəzaite در یشت ۱۰:۵۳ و صفت فاعلی gərəzāna- (چونگ، ص ۱۱۲). پوکورنی در ص ۳۵۱ همین صورت را («av. gərəzaiti klagt, jammert») در کنار سنسکریت gárhate ذیل گونهٔ گسترده‌شدهٔ *gal-gh- می‌آورد؛ پس پیکانِ ریشه ← اوستایی همان است که خودِ مأخذِ نورایی می‌کشد. توجه شود که فعل اوستایی به گونهٔ *gal-gh- تعلق دارد نه به *gal- سادهٔ شاخهٔ ژرمنی، و همین سبب شده نورایی هر سه صورت را در جعبهٔ ریشه بیاورد.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%AF%D9%84%D9%87\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"POK:351\", \"status\": \"supports\",\n       \"note\": \"IEW 350-351, gal-2 §4: 'Avestan gərəzaiti \\\"complains, cries, wails\\\", osset. γärz-in \\\"groan, moan\\\", Avestan gərəza, npers. gila \\\"lament\\\"' (POK_full.txt line ~29744).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 515-516 (BRT.txt lines 10265, 10380, 11595)\", \"stance\": \"supports\",\n       \"note\": \"'j., g. gərəz- V. \\\"klagen\\\", Praes. gərəz-'; 'gərəzā- f. \\\"Klage\\\": paoiryąm … gərəzača (sd.)'; also 'j. garəzay- Adj. \\\"klagend\\\"'. Nyberg (below) cites this very column, 'Av. (516) gərəz-'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 112 s.v. *garz (CHEUNG.txt line 8113ff.)\", \"stance\": \"supports\",\n       \"note\": \"'*garz \\\"to lament, weep\\\". AVESTAN gərəz- \\\"to lament, weep\\\" … Pres. {1} athem.: IND. med. 1sg. OAv. gərəzdī/gərəzē (Y 32.9, Y 46.2) … YAv. gərəzaite (Yt 10.53)'.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 930 (HRN.txt lines 8079-8083)\", \"stance\": \"supports\",\n       \"note\": \"'930. gile \\\"Klage\\\". aw. gərəzā \\\"Klage\\\", vergl. √garz-, gərəzaiti \\\"klagen\\\"; phlv. garzītan / garz(i)šn, gilak (Mēn.); ai. √garh-, garhate \\\"klagen, anklagen\\\".'\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"gilak\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Pahlavi word is right: MacKenzie's Concise Pahlavi Dictionary p. 36 has 'gilag [g(y)lk' | N gila] complaint, lamentation' (with the compound gilag-ōbār 'swallowing complaint, suffering in silence'), and Nyberg's glossary has 'gilak [gylk'] distress (Mēnōg ī Xrad 761) — Paz. gila … NP gilah \\\"complaint, reproach\\\"'. What is a shortcut is the arrow 'from Avestan'. Nyberg sets out the dialect split: 'girzītan [gylcytn'] to complain, to lament — girz- < *gṛz-, Av. (516) gərəz-; NW form; SW form gil-, gristan, subst. gilak', i.e. Pahlavi has a north-western doublet girz- that answers Avestan gərəz- directly, while gil-/gilak is the south-western (Persid) form in which Old Iranian *ź appears as Old Persian d and then as Persian l (*gṛd- > gil-), exactly as Hübschmann had derived it ('np. gila \\\"Klage\\\" = phl. gilak, aus ap. *gṛdā- = zd. gərəzā-', Persische Studien §110). Mo'in's footnote on the very page Nourai cites draws the same chain with the intermediate step Nourai omits. So the root and the word are confirmed; Avestan is a sister form rather than the ancestor, and the -l- specifically presupposes an Old Persian *gṛd-.\",\n     \"derivation_fa\": \"خودِ واژهٔ پهلوی درست است: مکنزی در «فرهنگ کوچک پهلوی» ص ۳۶ می‌آورد «gilag [g(y)lk'] شکوه، شکایت» (و ترکیب gilag-ōbār «شکایت‌فروخوردن») و نیبرگ در واژه‌نامهٔ خود «gilak [gylk'] اندوه (مینوی خرد ۷۶۱)، پازند gila، فارسی نو گِله». آنچه ساده‌سازی شده پیکانِ «از اوستایی» است. نیبرگ دوگانگی گویشی را روشن می‌کند: girzītan «شکایت کردن» صورت شمال‌غربی است و مستقیماً برابر اوستایی gərəz-، حال آنکه gil-/gilak صورت جنوب‌غربی (پارسی) است که در آن ź ایرانی باستان در پارسی باستان به d و سپس در فارسی به ل بدل شده (*gṛd- > gil-). هوبشمان نیز همین را گفته است: «np. gila = phl. gilak، از ap. *gṛdā- = zd. gərəzā-». حاشیهٔ معین در همان صفحه‌ای که نورایی ارجاع می‌دهد نیز همین زنجیره را با حلقهٔ میانی (girzak/girz) می‌آورد. پس ریشه و واژه تأیید می‌شود، اما اوستایی نیای مستقیم نیست بلکه صورتِ خواهر است و «ل» در gilak حتماً صورت جنوب‌غربی *gṛd- را می‌طلبد؛ ادعای نورایی با این احتیاط پذیرفتنی است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%AF%D9%84%D9%87\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1832\", \"status\": \"supports\",\n       \"note\": \"Printed p. 1832 = BQT_v3_pages.txt leaf 628 / pdf page 629 (checked against the running numerals ۱۸۲۹ on leaf 625 and ۱۸۳۷ on leaf 633: printed = pdf + 1203). Mo'in's footnote 2 to گله reads: «پهلوی gilak، پارتی gila، از girzak از girz (؟ گویش جنوب غربی)، از garza-ka- از (اوستایی) garəza < بارتولمه ۵۱۵، < نیبرگ ص ۸۱* … باستان garz, garzaiti (شکایت کردن)، کردی gili (شکایت) … اُستی gharzum (ناله کردن)». Exactly Nourai's chain, plus the intermediate *girzak he leaves out.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 36 (PHD_mackenzie.txt line 2514; PHD.txt line 380)\", \"stance\": \"supports\",\n       \"note\": \"'gilag [g(y)lk' | N gila] complaint, lamentation. ~-ōbār [-wp'l] swallowing complaint, suffering in silence.' English-Pahlavi side: 'complaint garzišn, gilag, must' (line 1304).\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Glossary s.vv. gilak, girzītan, gil- (NYB_vol2_glossary.txt lines 1662-1669)\", \"stance\": \"partial\",\n       \"note\": \"'gilak [gylk'] distress 761 — Paz. gila … NP gilah \\\"complaint, reproach\\\"'; 'girzītan [gylcytn'] to complain, to lament — girz- < *gṛz-, Av. (516) gərəz-, pres. gərəz-; NW form; SW form gil-, gristan, subst. gilak'; 'gil- … < *girdet < *gṛd-, SW form of girz-'. Supports the root but replaces the direct Avestan→Pahlavi arrow with a NW/SW dialect split.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §110 and §34 (HUB.txt lines 7853, 9322)\", \"stance\": \"partial\",\n       \"note\": \"'= phl. gilak Phl. Mīn. p. 18, Z. 2 aus ap. *gṛdā- = zd. gərəzā-' and 'gila \\\"Klage\\\" = phl. gilak, ap. *gṛdā- = zd. gərəza- (siehe §110)' — the Persian/Pahlavi l goes back to an Old Persian d, not to the Avestan z.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 930 (HRN.txt line 8081)\", \"stance\": \"supports\",\n       \"note\": \"'phlv. garzītan / garz(i)šn, gilak (Mēn.)' — Horn cites the Pahlavi noun from the Mēnōg ī Xrad, the same passage Nyberg numbers 761.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"geleh «گِله»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian گِله gela/gele 'complaint' continues Middle Persian gilag with the regular New Persian loss of the Middle Persian suffix -ag > -a/-e (nāmag > nāma, xānag > xāna), so gilag > gila > modern gele; Wiktionary derives it from MP g(y)lk' /gilag/ 'complaint, lamentation' and cites the Balochi cognate گِلَگ gilag, which preserves the older shape. MacKenzie writes the New Persian outcome 'N gila' in the same entry, and Horn no. 930 heads his article 'gile \\\"Klage\\\"'. Borhan-e Qate' p. 1832, the reference Nourai cites, gives the word with its vocalisation: «و بکسر اول و فتح ثانی مخفف، شکوه و شکایت باشد». It is to be kept apart from the homograph گَله galla 'flock, herd'. The Hafez couplet the chart quotes ('کو پیک صبح تا گله‌های شب فراق …') is a genuine attestation of this word in the plural.\",\n     \"derivation_fa\": \"«گِله» در فارسی نو دنبالهٔ فارسی میانهٔ gilag است؛ پسوند -ag فارسی میانه در فارسی نو به -a/-e بدل شده (nāmag > نامه، xānag > خانه)، پس gilag > gila > گِله. ویکی‌واژه آن را از فارسی میانهٔ g(y)lk' /gilag/ «شکوه، شکایت» می‌گیرد و هم‌ریشهٔ بلوچی «گِلَگ» را گواه می‌آورد که صورت کهن‌تر را نگه داشته است. مکنزی در همان مدخل صورت فارسی نو را «N gila» می‌نویسد و هرن هم مدخل ۹۳۰ خود را «gile Klage» نامیده است. برهان قاطع در ص ۱۸۳۲ — همان مأخذِ نورایی — واژه را با ضبط حرکات آورده است: «و بکسر اول و فتح ثانی مخفف، شکوه و شکایت باشد». باید آن را از هم‌نویسه‌اش «گَلّه» (رمهٔ گوسفند) جدا داشت. بیت حافظ که در نمودار آمده گواهی درست همین واژه به‌صورت جمع است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%AF%D9%84%D9%87\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1832\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' printed p. 1832 (BQT_v3_pages.txt leaf 628): the گله article, «و بکسر اول و فتح ثانی مخفف، شکوه و شکایت باشد»، with Mo'in's etymological footnote 2 tracing it to Pahlavi gilak and Avestan gərəzā-. Both the Pahlavi node and this Persian node rest on the same page, and the page really carries both.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 36 s.v. gilag (PHD_mackenzie.txt line 2514)\", \"stance\": \"supports\",\n       \"note\": \"'gilag [g(y)lk' | N gila] complaint, lamentation' — the '| N gila' is MacKenzie's notation for the New Persian continuation.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 930, p. 208 (HRN.txt line 8079)\", \"stance\": \"supports\",\n       \"note\": \"'930. gile \\\"Klage\\\". aw. gərəzā \\\"Klage\\\" … kurd. gili \\\"Klage\\\", gire \\\"Streit\\\"; oss. d. γärzun, i. gärzin \\\"stöhnen\\\".' Walde-Pokorny I 539 cites this very page for 'av. np. gile \\\"Klage\\\" (Horn Np. Et. 208)'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. gilak (NYB_vol2_glossary.txt line 1663)\", \"stance\": \"supports\",\n       \"note\": \"'Paz. gila, Skr. v. aparādha; NP gilah \\\"complaint, reproach\\\", cf. MPrs gylg'y \\\"complaining\\\".'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 112, *garz, NWIR section (CHEUNG.txt line ~8137)\", \"stance\": \"supports\",\n       \"note\": \"'NWIR: NP giristan/giriy- \\\"to weep\\\", NP gilah \\\"complaint; lamentation\\\", Kurd. (Kurm.) girizîn \\\"to be grumpy, grumble\\\"' — the modern standard work lists گله under *garz.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Germanic\",\n     \"words\": \"kall\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Nourai's 'kall' is the Proto-Germanic expressive stem *kall- (from *kalz-, PIE *gal-so-), whose -ll- comes from -lz- by the regular West/North Germanic assimilation of -lz- (Walde-Pokorny I 539: 'mit -ll- aus -ls-', beside unassimilated -ls- in Old Norse kalls n. 'provocation'). It is continued by Old Norse kall n. 'a calling', kalla 'to call, shout, sing', Old English ceallian 'to shout', Old High German kallōn 'to speak much and loudly, chatter', Dutch kallen 'to talk'. The zero-suffix relatives outside Germanic are Old Church Slavonic glasъ, Russian golos 'voice', Lithuanian galsas 'echo' and Ossetic ɣalas 'voice' — the same *gal-so- noun. Watkins, whose appendix is Nourai's reference here, states it in one line under gal-²: 'Germanic expressive form *kall- in Old Norse kalla, to call: CALL'.\",\n     \"derivation_fa\": \"«kall» در این جعبه همان ستاکِ آواییِ ژرمنی آغازین *kall- است که از *kalz- و در نهایت از *gal-so- هندواروپایی می‌آید؛ -ll- آن از همگونیِ قاعده‌مندِ -lz- پدید آمده است (والده‑پوکورنی جلد ۱ ص ۵۳۹: «mit -ll- aus -ls-»، در کنار صورت همگون‌نشدهٔ kalls در نورس باستان). دنبالهٔ آن‌ها: نورس باستان kall «فریاد» و kalla «فریاد زدن، خواندن، سرودن»، انگلیسی باستان ceallian، آلمانی علیای باستان kallōn «پرگویی و بلندگویی»، هلندی kallen «سخن گفتن». هم‌ریشه‌های بیرون از ژرمنی از همان اسمِ *gal-so-اند: اسلاوی کلیسایی glasъ و روسی golos «صدا»، لیتوانیایی galsas «پژواک» و اُستی ɣalas «صدا». واتکینز — که مأخذِ نورایی در همین جعبه است — ذیل gal-² می‌نویسد: «صورت آواییِ ژرمنی *kall- در نورس باستان kalla: CALL».\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/call\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 477): 'gal-². To call, shout. 1. Germanic expressive form *kall- in Old Norse kalla, to call: CALL … [Pok. 2. gal- 350.]' — the node's form, gloss and parent root, all three.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 539 (WLD_Bd1 djvu line ~33866)\", \"stance\": \"supports\",\n       \"note\": \"'*gal-so- … in osset. γalas, aksl. glasъ, russ. golosъ \\\"Stimme\\\", lit. galsas \\\"Widerhall\\\", anord. kall n. \\\"das Rufen\\\", wovon kalla \\\"rufen, singen\\\", ags. callian (engl. call) ds., ahd. kallon \\\"viel und laut sprechen, schwatzen\\\", mit -ll- aus -ls-.'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. galið (IEC.txt line 3869)\", \"stance\": \"supports\",\n       \"note\": \"'MHG kallen \\\"shout, chatter, sing, croak\\\"; Du. G kallen \\\"chatter\\\"; LG kohlen, id. … OE ceallian: ON kalla (\\\"call\\\", etc.).'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck, Dict. of Selected Synonyms 18.41 'call' (SYN.txt lines 32144-32146)\", \"stance\": \"supports\",\n       \"note\": \"'ON kalla \\\"shout, call, claim\\\", Dan. kalde, Sw. kalla, OE (rare) callian, ME calle, NE call, OHG kallōn \\\"speak loudly or much\\\", ChSl. glagolati \\\"speak\\\", glasъ \\\"voice\\\". Walde-P. 1.538.'\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"call\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English call continues the Germanic *kall- of the parent box, but the immediate source is almost certainly Old Norse rather than the native Old English word: Old English ceallian is attested once, late and in a Norse-influenced context, and Middle English callen (mid-13c.) appears first in the Danelaw area, so the standard dictionaries treat NE call as a Scandinavian loan — Buck 18.41 'OE (rare) callian, ME calle, NE call, prob. fr. ON'; Etymonline 'from Old Norse kalla \\\"cry loudly, summon in a loud voice; name, call by name\\\", from Proto-Germanic *kall-', noting OE ceallian was 'late and rare', the usual Old English verb being clipian. Klein, more conservatively, has 'call … ME. callen, fr. OE. ceallian, \\\"to shout\\\", rel. to ON. kalla'. Either way the box's Germanic *kall- → English call is correct; the chart simply does not show the Norse detour. The box carries no reference of its own.\",\n     \"derivation_fa\": \"فعل انگلیسی call دنبالهٔ همان *kall- ژرمنیِ جعبهٔ بالاست، اما سرچشمهٔ بی‌واسطهٔ آن به‌احتمال قوی نورس باستان است نه واژهٔ بومی انگلیسی: ceallian در انگلیسی باستان تنها یک بار و آن هم دیرهنگام و در بافتی زیر تأثیر نورس آمده، و callen در انگلیسی میانه (میانهٔ سدهٔ سیزدهم) نخست در ناحیهٔ دِین‌لا پیدا می‌شود؛ از این رو فرهنگ‌های معیار آن را وام‌واژه‌ای اسکاندیناویایی می‌دانند — باک (۱۸٫۴۱): «OE (نادر) callian، ME calle، NE call، احتمالاً از نورس باستان»؛ اتیمآنلاین: «از نورس باستان kalla، از ژرمنی آغازین *kall-»، با این یادآوری که فعل معمولِ انگلیسی باستان clipian بوده است. کلاین محتاطانه‌تر می‌نویسد «call … انگلیسی میانه callen، از انگلیسی باستان ceallian، هم‌ریشه با نورس باستان kalla». در هر حال پیکانِ ژرمنی ← انگلیسی درست است و نمودار تنها گذرِ نورسی را نشان نداده است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/call\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"(none given)\", \"status\": \"not_checked\",\n       \"note\": \"The English box on the printed page carries no reference symbol (confirmed on the page image, data/verification/sources/refs/ocr/BOOK/166.png); the JSON's refs=null is faithful. The parent box's AHD citation covers this step ('*kall- in Old Norse kalla, to call: CALL').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. call (KLN_1971.txt line 37449)\", \"stance\": \"supports\",\n       \"note\": \"'call, intr. and tr. v. — ME. callen, fr. OE. ceallian, \\\"to shout\\\", rel. to ON. kalla, \\\"to shout, sing\\\", Du. kallen, \\\"to talk\\\", OHG. kallōn, \\\"to call\\\", and cogn. with Mir. gall, \\\"glory; swan\\\", W. galw, \\\"to call\\\", OSlav. glasŭ … \\\"voice\\\".'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 18.41 (SYN.txt line 31524)\", \"stance\": \"partial\",\n       \"note\": \"'ON kalla, also \\\"call, summon\\\" = OE callian (once; ME calle, NE call, prob. fr. ON), OHG kallōn \\\"talk much or loud, chatter\\\" : ChSl. glasъ \\\"voice\\\", etc. Walde-P. 1.538. Falk-Torp 485f. NED s.v. call.' — same root, but the English word is a Norse loan.\"},\n      {\"src\": \"WEB\", \"where\": \"Etymonline s.v. call (archived via fetch_source.py)\", \"stance\": \"partial\",\n       \"note\": \"'mid-13c., callen … from Old Norse kalla \\\"cry loudly, summon in a loud voice; name, call by name\\\", from Proto-Germanic *kall-'; Old English ceallian is 'late and rare', clipian being the usual word.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-166.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk166.py",
 "description": "Write page-166.json"
}
```


### [2026-09-05T20:54:41.066Z] TOOL RESULT

```
written
```


## [2026-09-05T20:54:45.476Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -m json.tool data/verification/page-166.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 166",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-05T20:54:47.173Z] TOOL RESULT

```
JSON OK
nodes verified: 11/11
node verdicts: {'disputed': 2, 'confirmed': 8, 'plausible': 1}
root verdicts: {'disputed': 1, 'confirmed': 1}
ref checks: {'partial': 1, 'not_checked': 5, 'not_found': 1, 'supports': 8}
books consulted: {'partial': 7, 'silent': 1, 'contradicts': 4, 'supports': 24} | by book: {'HRN': 4, 'KLN': 3, 'MON': 2, 'BQT': 2, 'ARY': 2, 'HJB': 2, 'LKT': 2, 'CHEUNG': 2, 'PHD': 2, 'NYB': 2, 'SYN': 2, 'AFA': 1, 'PLA': 1, 'DEV': 1, 'LAM': 1, 'PHN': 1, 'FSD': 1, 'BRT': 1, 'HUB': 1, 'WLD': 1, 'IEC': 1, 'WEB': 1}
```


## [2026-09-05T20:55:09.780Z] AGENT

Done. `verify_check.py 166` reports 11/11 nodes, 0 PROBLEM lines.

**Page 166 (book p. 136) — 2 charts, 3 redirects skipped**

Verdicts: roots 1 confirmed / 1 disputed; nodes 8 confirmed, 1 plausible, 2 disputed. Ref checks: 8 supports, 1 partial, 1 not_found, 5 not_checked.

Disputed items:
- **ROOT "Gabbah" [Iranian] "dome, vault, blister"** — Nourai's AFM:123 citation is accurate (Addi Shir p. 123 s.v. القبّة: «تعريب كُبَّه واصل معناها كاس الحجامة … انتفاخ كلّ شيء»), and Borhan p. 1585 s.v. کبه says «معرّب آن قبّه است» — but that is the old Persian-lexicographic tradition. Klein 46, Hobson-Jobson 11–12, Fraenkel and Wiktionary make qubba Semitic (Akkadian qabābu, Hebrew qubbāh Num. 25:8, Syriac qubbəṯā, root q-b-b); Asbaghi 1988 does not list qubba among Persian loans in Arabic at all (the real Persian dome-word he lists is ǧumbad < gumbad, p. 92). No Iranian *gabbah with g- exists anywhere.
- **#1 Persian kobbeh «کبّه (کپّه)» / kapîdan** — conflates two words and misglosses a verb: کبّه = "cupping-glass; protuberance" (never "heap"), کپّه "heap" is per Mo'in a variant of کوپه, and کپیدن is «خفتن، خوابیدن» (and «ربودن») in both Mo'in and Dehkhoda — no dictionary gives "to pile up".
- **#2 Arabic qabbah / al-qubbah / q.b.b** — words real, arrow from Iranian rejected; the chart's own NOTE (Klein) states the view modern scholarship holds.

Other notes:
- **#2 Pahlavi gilak → plausible**: word confirmed (MacKenzie p. 36 'gilag … | N gila'), but "from Avestan" is a shortcut — Nyberg makes girz- the NW form matching Av. gərəz- and gil-/gilak the SW form < *gṛd- (so Hübschmann §110, and Mo'in's own footnote at BQT 1832 inserts *girzak).
- **Nourai citation error**: AFM:120 (Arabic node) is wrong — p. 120 is still باب الفاء; the القبّة entry is on p. 123. Verified on the page image (saved as `data/verification/sources/refs/ocr/AFM/0120.png`/`0123.png` + `.vision.txt`).
- **No extraction errors**: rendered pdf page 166 (`data/verification/sources/refs/ocr/BOOK/166.png`) — every form, gloss, script string, quote and reference in page-166.json matches the printed chart.
- Inaccessible refs: FVF:520, VGH:94, FVA:323, TYL:567 (no digital copies).
