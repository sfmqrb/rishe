# Verification process log — verify-page-163


## [2026-09-05T20:31:27.839Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 163 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-163.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-163.json. Write /home/sfmqrb/git/rishe/data/verification/page-163.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 163` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:31:29.511Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:31:30.218Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:31:30.230Z] TOOL RESULT

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


## [2026-09-05T20:31:30.475Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-163.txt"
}
```


### [2026-09-05T20:31:30.487Z] TOOL RESULT

```
1	=== PDF page 163 (book page 133) ===
2	--- entry 0 ---
3	ROOT Eueguh -> redirect to Wegwh
4	--- entry 1 ---
5	ROOT Eu-es -> redirect to Wes 3
6	--- entry 2 ---
7	ROOT Ewân -> redirect to Eu 1
8	--- entry 3 ---
9	ROOT Ewegwh -> redirect to Wegwh
10	--- entry 4 ---
11	ROOT Ew-es -> redirect to Wes 3
12	--- entry 5 ---
13	ROOT Ey -> redirect to Ei
14	
```


## [2026-09-05T20:31:33.810Z] AGENT

Page 163 looks like it's all redirects. Let me confirm against the source JSON and check how the checker handles this.


## [2026-09-05T20:31:34.629Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-163.json | head -100; echo \"=== checker ===\"; cat tools/verify_check.py"
}
```


### [2026-09-05T20:31:36.731Z] TOOL RESULT

```
{
    "pdf_page": 163,
    "book_page": 133,
    "entries": [
        {
            "root": {
                "name": "Eueguh",
                "redirect": "Wegwh"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Eu-es",
                "redirect": "Wes 3"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Ew\u00e2n",
                "redirect": "Eu 1"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Ewegwh",
                "redirect": "Wegwh"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Ew-es",
                "redirect": "Wes 3"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Ey",
                "redirect": "Ei"
            },
            "nodes": []
        }
    ]
}
=== checker ===
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


## [2026-09-05T20:31:42.000Z] TOOL CALL #4: Bash

```json
{
 "command": "for f in data/verification/page-*.json; do n=$(python3 -c \"import json,sys;d=json.load(open('$f'));print(len(d.get('entries',[])))\"); echo \"$f $n\"; done | awk '$2==0'; echo \"---existing files---\"; ls data/verification/ | head -50"
}
```


### [2026-09-05T20:31:48.591Z] TOOL RESULT

```
data/verification/page-146.json 0
---existing files---
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
page-146.json
page-147.json
page-311.json
page-31.json
page-32.json
page-33.json
```


## [2026-09-05T20:31:51.387Z] TOOL CALL #5: Bash

```json
{
 "command": "cat data/verification/page-146.json; echo; echo \"=== src 146 ===\"; python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-146.json'));print([ (e['root'].get('name'),e['root'].get('redirect'),len(e['nodes'])) for e in d['entries']])\""
}
```


### [2026-09-05T20:31:53.322Z] TOOL RESULT

```
{
  "pdf_page": 146,
  "book_page": 116,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "note": "This page contains no charts. Both entries are cross-reference stubs: 'Dyě  see root: Dei' and 'Dyeu  see root: Dei'. Per the verification instructions redirect entries are skipped, so this file carries no entries. Checked against the printed page (site/pages/146.jpg, book p. 116): the page shows exactly two headword boxes with 'see root: Dei' in italics and nothing else, so the extraction in data/extracted/batch/page-146.json is faithful. The redirect target is real: the root box 'Dei, Deiw, Dyeu, Dyě' stands on PDF page 112 (verified in data/verification/page-112.json), and it explicitly lists both Dyě and Dyeu among its variant spellings, so both pointers resolve correctly. Nourai's variants correspond to the standard PIE root *dyew- / *dei̯H- 'to shine; sky, day, god' (Pokorny 183-187 dei-, deia-, di-, deía-).",
  "note_fa": "این صفحه هیچ نموداری ندارد؛ هر دو مدخل آن تنها ارجاع‌دهنده‌اند: «Dyě» و «Dyeu» هر دو به ریشهٔ «Dei» ارجاع داده شده‌اند. بر پایهٔ دستورالعمل ارزیابی، مدخل‌های ارجاعی بررسی نمی‌شوند، پس این پرونده بدون مدخل است. تصویر صفحهٔ چاپی (صفحهٔ ۱۱۶ کتاب) با دادهٔ استخراج‌شده مطابقت کامل دارد و خطای خوانش در کار نیست. ریشهٔ مقصد نیز واقعی است: جعبهٔ «Dei, Deiw, Dyeu, Dyě» در صفحهٔ ۱۱۲ پی‌دی‌اف آمده و هر دو صورت را در خود جای داده است؛ این صورت‌ها همان ریشهٔ شناخته‌شدهٔ هندواروپایی آغازین *dyew- / *dei̯H- «درخشیدن؛ آسمان، روز، خدا» (پوکورنی، صفحات ۱۸۳–۱۸۷) هستند.",
  "entries": []
}

=== src 146 ===
[('Dyě', 'Dei', 0), ('Dyeu', 'Dei', 0)]
```


## [2026-09-05T20:32:01.068Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob,os,re\ntargets=[\"Wegwh\",\"Wes 3\",\"Eu 1\",\"Ei\"]\nfor f in sorted(glob.glob(\"data/extracted/batch/page-*.json\"), key=lambda p:int(re.search(r'(\\d+)',os.path.basename(p)).group())):\n    d=json.load(open(f))\n    for i,e in enumerate(d[\"entries\"]):\n        n=e[\"root\"].get(\"name\",\"\")\n        if any(n==t or n.startswith(t) for t in targets) or n in (\"Wegwh\",\"Wes 3\",\"Eu 1\",\"Ei\",\"Eu\",\"Wes\",\"Ei, Ai\"):\n            print(os.path.basename(f), i, repr(n), \"redirect=\",e[\"root\"].get(\"redirect\"), \"nodes=\",len(e[\"nodes\"]), \"| lang/gloss:\", str(e[\"root\"].get(\"gloss\") or e[\"root\"])[:120])\nEOF"
}
```


### [2026-09-05T20:32:02.917Z] TOOL RESULT

```
page-148.json 1 'Ei, Ey, I 1, Iâ 1' redirect= None nodes= 13 | lang/gloss: to go
page-149.json 0 'Ei, Ey, I 1, Iâ 1' redirect= None nodes= 19 | lang/gloss: to go
page-149.json 2 'Eis 1' redirect= None nodes= 4 | lang/gloss: passion
page-150.json 0 'Eis 2' redirect= None nodes= 6 | lang/gloss: ice
page-162.json 4 'Eu 1, Ewân, Wâ' redirect= None nodes= 6 | lang/gloss: to be empty
page-532.json 0 'Wegwh, Ewegwh, Euegh' redirect= None nodes= 5 | lang/gloss: to speak solemnly
page-551.json 0 'Wes 3, Ew-es, Eu-es' redirect= None nodes= 15 | lang/gloss: to wear, put on
```


## [2026-09-05T20:32:51.372Z] TOOL CALL #7: Bash

```json
{
 "command": "ls site/pages/163.jpg 2>/dev/null; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null | head; pdftoppm -f 163 -l 163 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg163\" && ls -la \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/\""
}
```


### [2026-09-05T20:32:53.728Z] TOOL RESULT

```
site/pages/163.jpg
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
total 15848
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:32 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:32:55.563Z] AGENT

Now let me look at the printed page itself.


## [2026-09-05T20:32:57.048Z] TOOL CALL #8: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg163.png"
}
```


### [2026-09-05T20:32:57.553Z] TOOL RESULT

```

```


## [2026-09-05T20:32:57.551Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:33:11.019Z] AGENT

Printed page confirms 6 cross-reference stubs. Let me verify the redirect targets and the underlying PIE roots against local sources.


## [2026-09-05T20:33:13.660Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nfor p in (532,551,162,148,149):\n    d=json.load(open(f'data/extracted/batch/page-{p}.json'))\n    for i,e in enumerate(d['entries']):\n        r=e['root']\n        print(p,i,r.get('name'),'|',r.get('gloss'),'| refs=',r.get('refs'), '| lang=',r.get('lang'))\n\" 2>&1 | head -30; echo \"=== POK files ===\"; ls data/verification/sources/refs/ | head -60"
}
```


### [2026-09-05T20:33:15.310Z] TOOL RESULT

```
532 0 Wegwh, Ewegwh, Euegh | to speak solemnly | refs= POK:348 | lang= Indo-European
532 1 Wei 1 | to bend, turn, twist | refs= POK:1120 | lang= Indo-European
551 0 Wes 3, Ew-es, Eu-es | to wear, put on | refs= POK:1172 | lang= Indo-European
551 1 Wes 4 | eat, feed | refs= POK:1171; WLD1:307 | lang= Indo-European
162 0 Esu | None | refs= None | lang= None
162 1 Ěter | internal (insignificant) organs | refs= POK:344; IEC:1347; WLD1:264 | lang= Indo-European
162 2 E-tero | None | refs= None | lang= None
162 3 Eti | above, beyond | refs= POK:344; KLN:545 | lang= Indo-European
162 4 Eu 1, Ewân, Wâ | to be empty | refs= POK:345 | lang= Indo-European
148 0 Eg | I | refs= POK:291 | lang= Indo-European
148 1 Ei, Ey, I 1, Iâ 1 | to go | refs= POK:293,501; KLN:825 | lang= Indo-European
149 0 Ei, Ey, I 1, Iâ 1 | to go | refs= POK:293,501; KLN:825 | lang= Indo-European
149 1 Ĕik | None | refs= None | lang= None
149 2 Eis 1 | passion | refs= POK:299 | lang= Indo-European
=== POK files ===
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


## [2026-09-05T20:33:18.879Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | grep -i -E 'POK|WLD|AHD'"
}
```


### [2026-09-05T20:33:18.926Z] TOOL RESULT

```
AHD_watkins1985.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
WLD_band3.txt
```


## [2026-09-05T20:33:23.032Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- eu̯egʷh / euegwh ---\"; grep -n -i -E \"eu.egʷh|euegwh|eu̯egʷh|ewegwh\" POK_full.txt | head -10; echo \"--- ues- clothe ---\"; grep -n -E \"^ues-|ṷes-.*(kleiden|Kleid)|ues-.*kleiden\" POK_full.txt | head -10; echo \"--- eu- leer ---\"; grep -n -E \"eu-.*leer|leer, mangelnd\" POK_full.txt | head -10; echo \"--- ei- gehen ---\"; grep -n -E \"^ei-|ei-.*gehen\" POK_full.txt | head -10"
}
```


### [2026-09-05T20:33:23.135Z] TOOL RESULT

```
--- eu̯egʷh / euegwh ---
--- ues- clothe ---
7526:ues-:W\\h Old Indie avas'dosNn' attached together formant Germanic wes-'\n Modern 
8322:ues-, u6s-\v\ Old Indie vasar-han- "striking in the morning, early morning', vasara-^ear\)/ 
42694:ues-, u6s-:Q\^ Indie vah, Avestan i/aenkl. for Akk. Gen. Dat. PI., Dual. Old Indie vam; 
--- eu- leer ---
--- ei- gehen ---
24616:ei-en-\v\ Lithuanian fenai. " thill pole '; 
24818:ei-K), 101 (Old Indie ihf, Hittite i-i-t);
```


## [2026-09-05T20:33:27.705Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs/../refs_online.json'))\nfor k in ('POK','WLD','AHD','KLN','IEC','SYN'):\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-05T20:33:29.899Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
```


## [2026-09-05T20:33:34.964Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\np=d['POK']\nfor k,v in p.items(): print(k,':',str(v)[:800])\n\""
}
```


### [2026-09-05T20:33:36.844Z] TOOL RESULT

```
title : J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
edition_found : 1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers
kind : archive_djvu
url : https://archive.org/details/indogermanisches01pokouoft
identifier : indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)
local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
notes : Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)
local_files : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt']
cites : page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)
```


## [2026-09-05T20:33:39.239Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### Page(s): 348\"; grep -n -B12 \"Page(s): 348\" POK_full.txt | head -40; echo; echo \"### lemma eu\"; grep -n \"lemma: eu\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:33:39.309Z] TOOL RESULT

```
### Page(s): 348
29058-The origin of labialized Old laryngeals: 
29059-
29060-common Armenian Celtic *hue- > gw- > u-. 
29061-
29062-gr. Euxojjai " I promised, prayed, wished, praised ', athemat. Impf. sukto (= gath.- 
29063-Avestan aogada, j.-av. aoxta^ spoke, talked, conversed ') to a present *eugh-tai 
29064-(Schwyzer Gr. Gr. I 679); suxoq n, " thing prayed for, object of prayer, boast, vaunt, vow, 
29065-votive offering ', suxn " profession, declaration, prayer, request, imploration'; in addition 
29066-perhaps also auxsw 'boast, brag, vaunt, boast', abstracted from K£V£-auxn<; " the empty 
29067-boasting ' (*K£V£-£uxn<;, Bechtel Lexilogus 192). 
29068-
29069-References: WP. I 110. 
29070:Page(s): 348 

### lemma eu
28832:Root / lemma: euk- 
28864:Root /lemma: eu-1, eua-\ ua- ua-{**hue-) 
28918:Root / lemma: eu-2 
28961:Root / lemma: eu-3, with present formants -et- : yet-, ut- 
28980:Root / lemma: eu-4 
28995:Root / lemma: eus- 
29030:Root / lemma: eueg^h-i* huehueg^h-) 
29563:Root /lemma: euA'^-, du6^- m^-
```


## [2026-09-05T20:33:43.449Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '29030,29045p' POK_full.txt; echo \"=== eu-1 ===\"; sed -n '28864,28880p' POK_full.txt; awk 'NR>28864 && NR<28920 && /Page\\(s\\)/' POK_full.txt"
}
```


### [2026-09-05T20:33:45.337Z] TOOL RESULT

```
Root / lemma: eueg^h-i* huehueg^h-) 

Meaning: to praise, worship 

Material: ueg^h-. Old Indie ved. {*gvaghat) vaghat-^ the vowing, worshiper, organizer of a 

sacrifice ', Avestan rastare-vaysnti- EN; 

Armenian gog "say!', gogces " you can say '; 

The origin of labialized Old laryngeals: 

common Armenian Celtic * hue- > gw- > g-, u-; Old Indie gw- > v-, Latin gw- > v-, u-. 

Latin voved, -ere, vovT, votum (this at first from *vdve-vai, -turn) " to vow, promise 
solemnly, engage religiously, pledge, devote, dedicate, consecrate ', Umbrian vufetes (= 
=== eu-1 ===
Root /lemma: eu-1, eua-\ ua- ua-{**hue-) 
Meaning: to lack; empty 



Note: esp. in partizipialen /70-formations 

Material: Old Indie una-, Avestan una-^ insufficient, inadequate, lack, be short of, Avestan 
uyamna6s. (participle present Med. to present u-ya-)\ npers. {*gvang) vang^ empty, bare, 
lacking, poor, needy', pamir vanao^ Leerheit, vanity, pride '; 

The origin of labialized Old laryngeals: 

common Celtic *hue- > gw- > f- ; Armenian Old Indie gw- > u-. 

Armenian unain' empty, bare, lacking' (Indo Germanic u)\ 

Page(s): 345-346
```


## [2026-09-05T20:33:48.866Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ei- ===\"; grep -n \"lemma: ei-\" POK_full.txt | head; echo; echo \"=== ues clothe ===\"; grep -n \"lemma: ues-\" POK_full.txt | head"
}
```


### [2026-09-05T20:33:48.925Z] TOOL RESULT

```
=== ei- ===
24565:Root / lemma: ei-3 {*hei-S} 
24599:Root / lemma: ei-4 : oi- {*hei-4) 
24782:Root / lemma: ei-s-2, ei-n- {*heis-) 
24798:Root / lemma: ei- {*hei-) 

=== ues clothe ===
28560:Root /lemma: es-en-, os-en-, -er-\ harvest time, *autumn' : Root /lemma: ues-f. spring'. 
92346:Root / lemma: ues-1 {* hauhes-f) 
92407:Root / lemma: ues-2 {* hauhes-2) 
92432:Root / lemma: ues-3 {* hyes-3) 
92461:Root / lemma: ues-4 {*hues-4) 
92484:Root / lemma: ues-5 {* haues-5) 
92523:Root / lemma: ues-no- {* haues-no-) 
92549:Root / lemma: ues-7 {* haues-7) 
92575:Root / lemma: ues-9 {* hayes-) 
92621:Root / lemma: ues-f{*h2auhies^
```


## [2026-09-05T20:33:52.317Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24798,24806p' POK_full.txt; awk 'NR>24798 && NR<24880 && /Page\\(s\\)/' POK_full.txt; echo \"=== ues-4 ===\"; sed -n '92461,92470p' POK_full.txt; awk 'NR>92461 && NR<92490 && /Page\\(s\\)/' POK_full.txt; echo \"=== ues-5 ===\"; sed -n '92484,92492p' POK_full.txt; awk 'NR>92484 && NR<92525 && /Page\\(s\\)/' POK_full.txt"
}
```


### [2026-09-05T20:33:54.072Z] TOOL RESULT

```
Root / lemma: ei- {*hei-) 

Meaning: to go 

Note: extended eZ-d^-, ei-gh-, i-ta-3indj-a-,j-e-.jd-.j9- 

Material: Old Indie emi, eti, imah, yant/' go', Avestan ae/t/, yeinti. Old pers. a/t/y 'goes', 
themat. Med. Old Indie aya-teetc. (apparent lengthened grade of Old Indie a/'t/, Avestan 
a/t/" goes to, comes to, comes up to, approaches, draws near ' is *a-a/t/, with prefix a); 
=== ues-4 ===
Root / lemma: ues-4 {*hues-4) 

Meaning: to stick, pierce 

Material: Old Indie nivasita- 'ums Leben gebracht', n/rvasana-m^ das Ermorden, Toten', 

y0a/7Vas5ya//"sehneidetrings ab, from' ; Old Irish ;fe/7/75/o'"schindet' {*ues-na-ti)\ (common 

Celtic -ns-, -nt- > -nn-), alb. usht^ ear '; 

Page(s):1172 
=== ues-5 ===
Root / lemma: ues-5 {* haues-5) 

Meaning: to dress, put on 

Material: Old Indie i/a5/e"kleidet sich, zieht an', Avestan vasteds. (compare the unthemat. 

gr. EGoai, -soTai), varjhaiti 6s.\ Old Indie vasana-, Avestan varjhana- n. " garment '; Old 

Indie vasman- n. "cover' (= z\\\a)\ vastra-, Avestan vastra- n. " clothing ' (: gr. FEGipa, 
Page(s): 1172-1173
```


## [2026-09-05T20:33:57.235Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>24798 && NR<25100 && /Page\\(s\\)/ {print NR\": \"$0}' POK_full.txt | head -3"
}
```


### [2026-09-05T20:33:59.230Z] TOOL RESULT

```
25043: Page(s): 293-297
```


## [2026-09-05T20:34:05.701Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -E \"speak solemnly|To clothe\\.|To go\\.|lacking, empty|empty, lacking\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:34:05.811Z] TOOL RESULT

```
428:ei-'. To go. 1. Full-grade form *ei- in: a. Latin ire, to go: ADIT, AMBIENT, (AMBITION), CIRCUIT, COITUS, COMITIA, EXIT!, EXIT?, INTROIT, ISSUE, OBITUARY, PERISH, PRAE- TOR, PRETERIT, SEDITION, SUBITO, SUDDEN, (TRANCE), TRANSIENT, (TRANSIT), (TRANSITIVE); b. Greek ienai, to go: ION; ANION, CATION, DYSPROSIUM. 2. Suffixed zero-grade form *i-t- in: a. further suffixed form *i-t-yo- in Latin initium, entrance, beginning (in-, in; see en): COMMENCE, INITIAL, (INITIATE); b. Latin comes (stem comit-), companion (< “one who goes with another”; com-, with; see kom): COUNT?; CONCOMITANT, CONSTA- BLE, (VISCOUNT). 3. Suffixed form ‘*i-ter in Latin iter, journey (> Late Latin itinerdre, to travel): (ERRANT), EYRE, ITINERANT, ITINERARY. 4. Extended form *yd- (< *yaa-) in suffixed forms *yd-no-, yd-nu- in: a. Latin Janus, archway, and Jdnus, god of doors and of the beginning of a year: JANITOR, JANUARY, JANUS; b. San- skrit ydnam, way (in Buddhism, “mode of knowledge,” “vehicle”): HiINAYANA, MAHAYANA. [Pok. 1. ei- 293.]
438:el-3, To go. Suffixed extended form *ela-un-yo- in Greek elaunein, to drive (< “to cause to go”): ELASTIC, ELATER, ELATERITE; ELASMOBRANCH. [Pok. 6. el- 306.]
469:eu-?. Lacking, empty. Extended forms *eua-, *wd-, *wa-. 1. Suffixed form *wo-no- in: a. Germanic *wanén in Old English wanian, to lessen, and wana, lack: WANE; b. North Germanic *wanatdn in Old Norse vanta, to lack: WANT. 2. Suffixed form *wd-no- in Latin vanus, empty: VAIN, VANITY, VAUNT; EVANESCE, VANISH. 3. Ex- tended form *wak- in Latin vacdre (variant vocdre), to be empty: VACANT, VACATE, VACATION, (VACUITY), VAC- UUM, VOID; (AVOID), (DEVOID), EVACUATE. 4. Extended and suffixed form *wds-to- in Latin vdstus, empty, waste (> vdstdre, to make desolate): WASTE; DEVASTATE. [Pok. 1. eu- 345.]
615:kenk-’. Heel, bend of the knee. 1. Germanic *hanhaz in Old English héh, heel: HocK!. 2. Germanic *hanhilén- in Old English héla, heel: HEEL!. [Pok. 3. kenk- 566.] kens-. To proclaim, speak solemnly. Form *kens-é- in Latin cénsére, to judge, assess, estimate, tax: CENSOR, CENSUS; RECENSION. [Pok. kens- 566.]
693:in: a. Old English -Jéosan, to lose: LORN, (LOSEL); b. Ger- manic *fer-leusan, *far-leusan (*fer-, *far-, prefix denot- ing rejection or exclusion; see per’) in (i) Old English forléosan, to forfeit, lose: FORLORN (ii) Dutch verliezen, to lose (past participle verloren): FORLORN HOPE. 2. Ger- manic */aww6 in Swedish lagg, barrel stave (< “split piece of wood”), akin to the probable source of LAG?. 3. Germanic *lausaz in: a. Old English léas, “loose,” free from, without, untrue, lacking: LEASING, -LESS; b. Old English los, loss: LOSE, (LOSS); CG. Old Norse Jauss, louss, loose: LOOSE; d. Swiss German lésch, loose: LOESS. 4. Zero-grade form *lu- in: a. Greek luein, to loosen, release, untie: LYSIS, LYSO-, -LYTE, -LYTIC; ANALYSIS, CATALYSIS, DIALYSIS, LYASE, PARALYSIS, TACHYLYTE; b. Latin lués, plague, pestilence (< “dissolution, putre- faction”): LUES; Cc. prefixed form *se-lu- (se-, apart; see s(w)e-) in Latin solvere, to loosen, untie: SOLUBLE, SOLUTE, SOLVE; ABSOLUTE, (ABSOLVE), ASSOIL, CONSO- LUTE, DISSOLVE, RESOLVE. [Pok. 2. Jeu- 681.] leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere; por- for pr6-, forth, forward; see per’): POLLUTE. 2. Suffixed zero-grade form */u-to- in Latin lutum, mud, mire, clay: LUTE?. [Pok. 1. leu- 681.] léu-1, Stone. Welsh Jlech, flat stone (from an uncertain preform): CROMLECH. [Pok. 2. léu- 683.] léu-2. Echoic root. 1. Extended form */eut- in Germanic *leuth- in Old High German liod (> German Lied), song: LIED; VOLKSLIED. 2. Extended variant form *laud- in Latin laus, praise, glory, fame: LAUD. [Pok. 3. éu- 683.] leubh-. To care, desire; love. I. Suffixed form *leubh-o- in Germanic *leubaz in Old English /éof, dear, beloved: LIEF; LEMAN, LIVELONG. II. O-grade form *loubh-. 1. Germanic */aubé in: a. Old English léaf, permission (< “pleasure, approval”): LEAVE?; b. Middle Dutch verlof, leave, permission (ver-, intensive prefix, from Germanic *fer-; see per'): FURLOUGH; Cc. Germanic *galaubd (*ga-, intensive prefix; see kom) in Old English geléafa, biléafa (bi-, about; see ambhi), belief, faith: BELIEF. 2. Ger- manic *galaubjan (*ga-, intensive prefix; see kom), “to hold dear,” esteem, trust, in Old English geléfan, beléfan (be-, about; see ambhi), to believe, trust: BELIEVE. III. Zero-grade form *lubh-. 1. Suffixed form *lubh-a- in Germanic */ubé in Old English Jufu, love: LovE. 2. Suf- fixed (stative) form *lubh-é- in Latin libére, to be dear, be pleasing: QUODLIBET. 3. Latin libid6, pleasure, desire: LIBIDO. [Pok. leubh- 683.] leud-. Small. Germanic */it- in: a. West Germanic *lutti- laz in Old English /ytel, little: LITTLE; b. Old English liitan, to bend down: LouT?; c. Old Norse lita, to bend down (< “to make small”): (LouT!); d. perhaps Middle Dutch loteren, to shake, totter (< “to make smaller”), perhaps akin to the source of Middle English Joitren, to idle away time: LOITER. [Pok. leud- 684.] leudh-'. To go. Zero-grade form *(e)ludh- in suffixed unextended form *elu-to- in Greek prosélutos, “one who comes to a place,” stranger (pros-, to; see per’): PROS- ELYTE. [In Pok. 6. e/- 306.] leudh-2. To mount up, grow. Suffixed form */eudh-ero- in Latin liber, free (the precise semantic development is obscure): LIBERAL, LIBERATE, LIBERTINE, LIBERTY, LIV- ERY; DELIVER. [Pok. 1. leudh- 684.] leu(e)-. To wash. 1. Suffixed form *lou-kd- in Germanic *laugo in Old English /éag, lye: LYE. 2. Suffixed form *lou-tro- in Old English /éathor, washing soda: LATHER. 3. Variant form *Jaw- in: a. Latin lavere, to wash, with its derivative -luere, to wash: LOTION; ABLUTION, ALLU- VION, COLLUVIUM, DELUGE, DILUTE, (ELUANT), ELUTE, ELUVIUM; b. form */aw-d- in Latin lavdre, to wash: LAVE, LOMENT; C. Latin lavatrina, ldtrina, a bath, privy: LATRINE. [Pok. Jou- 692.] leug-'. To bend, turn, wind. 1. Germanic *Jauk-, leek (semantic transition obscure), in Old English Jéac, leek: LEEK; GARLIC. 2. Zero-grade form *lug- in Germanic *luk- in: a. Old English loc, lock (perhaps < “a bending
912:grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
1116:wadh-2, To go. 1. Basic form *wadh- in: a. Germanic *wadan, to go, in Old English wadan, to go: WADE; b. Latin vadum, ford: vADOSE. 2. Lengthened-grade form *wddh- in Latin vddere, to go, step: VAMOOSE; EVADE, INVADE, PERVADE. [Pok. uddh- 1109.]
1132:form *weg-slo- in Latin vélum, a sail, curtain, veil: VEIL, VELUM, VEXILLUM, VOILE; REVEAL. [Pok. weg- 1117.] weg-2. To be strong, be lively. 1. Suffixed o-grade form *wog-é- in Germanic *wakén in Old English *wacan, to wake up, arise, and wacian, to be awake: WAKE}. 2. Suf- fixed o-grade form *wog-no- in Germanic *waknan in Old English wecnan, wecnian, to awake: WAKEN. 3. Germanic *wakjan in Old English weccan, to be awake: WATCH. 4. Germanic *wahtwo in Old High Ger- man wahta, watch, vigil, in dialectal German beiwacht, supplementary night watch: BIvouac. 5. Germanic *waht- in: a. Old North French waitier, to watch: WAIT; b. Middle Low German wachten, to watch, guard: WAFT. 6. Suffixed (causative) o-grade form *wog-eyo- in Latin vegére, to be lively: VEGETABLE. 7. Suffixed (stative) form *weg-é- in Latin vigére, to be lively: vicor. 8. Suf- fixed form *weg-eli- in Latin vigil, watchful, awake (> vigilare, to watch, be awake): VEDETTE, VIGIL, (VIGI- LANT), VIGILANTE; REVEILLE, SURVEILLANT. 9. Suffixed form *weg-slo- in Latin véldx, fast, “lively”: VELOCITY. [Pok. weg- 1117.] wegh-. To go, transport in a vehicle. 1. Germanic *wegan in Old English wegan, to carry, balance in a scale: WEIGH}. 2. Germanic lengthened form *wég-6 in Old English wég(e), weight, unit of weight: WEE. 3. Suffixed form *wegh-ti- in Germanic *wihti- in Old English wiht, gewiht, weight: WEIGHT. 4. Germanic *wegaz, course of travel, way, in Old English weg, way: WAY; ALWAYS, (Away). 5. Suffixed form *wogh-no- in Germanic *wag- naz, vehicle, in: a. Old English we(g)n, wagon: WAIN; b. Middle Dutch wagen, wagon: WAGON. 6. Suffixed o-grade form *wogh-lo- in: a. Germanic *waglaz in Old Norse vagl, chicken roost, perch, beam: WALLEYED; b. Greek okhlos, populace, mob (< “moving mass’): OCHLOCRACY, OCHLOPHOBIA. 7. Distantly related to this root are: a. Germanic *wag-, “to move about,” in (i) possibly Middle English waggen, to wag: wac! (ii) Old High German waggo, wacko, boulder rolling on a river- bed (> German Wacke, boulder): GRAYWACKE; b. Ger- manic *wéga-, water in motion, in Old Italian vogare, to row: VOGUE; c. Germanic *wig- in (i) Old English wicga, insect (< “thing that moves quickly”): EARWIG (ii) Middle Dutch and Middle Low German wiggelen, to move back and forth, wag: WIGGLE. 8. Basic form *wegh- in Latin vehere (past participle vectus), to carry: VECTOR, VEHICLE; ADVECTION, CONVECTION, EVECTION, INVEIGH. 9. Suffixed basic form *wegh-yd in Latin via, way, road: FOY, VIA, VOYAGE; CONVEY, DEVIATE, DEVIOUS, (ENVOI), ENVOY!, OBVIOUS, PERVIOUS, PREVIOUS, (TRIVIAL), TRIV- IUM, (vIADUCT). 10. Suffixed form *wegh-s- in Latin vexdre, to agitate (< “to set in motion”): VEX. 11. Prob- ably suffixed form *wegh-so- in Latin convexus, “carried or drawn together (to a point),” convex (com-, together; see kom): CONVEX. [Pok. vegh- 1118.] weg-. Wet. 1. Germanic *wakw-6 in Old Norse vdk, a crack in ice (< “wet spot’): WAKE?. 2. Suffixed zero-grade form *ug’-sm- in: a. Latin (hjiimére, to be wet: HUMECTANT, HUMID; b. Latin (hj)iimor, fluid: HU- mor. 3. Suffixed zero-grade form *ug’-ro- in Greek hugros, wet, liquid: HYGRO-. 4. Regarded by some as an extended form of this root (with the meaning “the impregnator”), but probably a distinct Indo-European word, is *uk”s-en-, bull, ox, in Germanic *uhs6dn- in: a. Old English oxa, ox: 0x; b. Old High German ohso, ox, in German Aurochs, aurochs: AUROCHS. [Pok. uweg#- 1118.] weg”h-, Also eug’h-. To preach, speak solemnly. Suf- fixed o-grade form *wog’h-eyo- in Latin vovére, to pledge, vow: VOTARY, VOTE, (VOTIVE), VOW; DEVOTE, (DEvouT). [Pok. ewegvh- 348.] wei-'. Also weie-. To turn, twist; with derivatives refer- ring to suppleness or binding. I. Form *wei-. 1. Germanic suffixed form *wi-ra-, *wé-ra- in Old English wir, wire: WIRE. 2. Probably suffixed Germanic form *wai-ra- in
1162:wes-‘. To clothe. Extension of eu-'. 1. Suffixed o-grade form *wos-eyo- in Germanic *wazjan in Old English werian, to wear, carry: WEAR}, 2. Suffixed form *wes-ti- in Latin vestis, garment: VEST; DEVEST, INVEST, REVEST, TRAVESTY. 3. Suffixed form *wes-nu- in Greek hennunai, to clothe: HIMATION. [Pok. 5. wes- 1172.]
```


## [2026-09-05T20:34:19.012Z] AGENT

Let me check Watkins' eu-1 and the target root box as printed on PDF page 532.


## [2026-09-05T20:34:24.622Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o -E \"eu-.{0,120}To dress.{0,200}\" AHD_watkins1985.txt | head -3; cd /home/sfmqrb/git/rishe; pdftoppm -f 532 -l 532 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg532\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg532.png'); print(im.size)\nim.crop((0,0,im.size[0],int(im.size[1]*0.28))).resize((int(im.size[0]*1.6),int(im.size[1]*0.28*1.6))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg532_top.png')\n\""
}
```


### [2026-09-05T20:34:29.402Z] TOOL RESULT

```
ugrep: error: error at position 89
x80-\xbf][\x80-\xbf]*){0,200}
exceeds complexity limits___/


(1275, 1650)
```


## [2026-09-05T20:34:31.161Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg532_top.png"
}
```


### [2026-09-05T20:34:31.309Z] TOOL RESULT

```

```


## [2026-09-05T20:34:31.307Z] INPUT

[Image: original 2040x739, displayed at 2000x725. Multiply coordinates by 1.02 to map to original image.]


## [2026-09-05T20:34:41.114Z] AGENT

Confirmed — the printed p. 532 root box reads "Eueguh", but the extracted JSON says "Euegh". Let me verify that and archive a couple of web sources.


## [2026-09-05T20:34:45.633Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-532.json'));print(json.dumps(d['entries'][0]['root'],ensure_ascii=False))\"\necho \"=== archive ===\"\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81wegwh-' --note 'page 163, redirect target Wegwh/Ewegwh/Eueguh, PIE root to vow/speak solemnly' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wes-' --note 'page 163, redirect target Wes 3 / Ew-es / Eu-es, PIE *wes- to clothe' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ey-' --note 'page 163, redirect target Ei / Ey, PIE *h1ey- to go' 2>&1 | tail -3"
}
```


### [2026-09-05T20:34:49.926Z] TOOL RESULT

```
{"name": "Wegwh, Ewegwh, Euegh", "lang": "Indo-European", "refs": "POK:348", "gloss": "to speak solemnly"}
=== archive ===
/home/sfmqrb/git/rishe/data/verification/sources/web/ec99e5a445c8f03f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4c8f69f23d3ef8f2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a20c273b41f2ed77.txt
```


## [2026-09-05T20:34:52.366Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in ec99e5a445c8f03f 4c8f69f23d3ef8f2 a20c273b41f2ed77; do echo \"###### $f\"; head -c 1200 $f.txt | tr -s '\\n' '\\n'; echo; done"
}
```


### [2026-09-05T20:34:54.011Z] TOOL RESULT

```
###### ec99e5a445c8f03f
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81wegwh-
FETCHED: 2026-09-05T20:34:48Z
STATUS: -1
TITLE: 
FETCH FAILED: HTTP Error 404: Not Found
###### 4c8f69f23d3ef8f2
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wes-
FETCHED: 2026-09-05T20:34:49Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/wes- - Wiktionary, the free dictionary
Reconstruction:Proto-Indo-European/wes- - Wiktionary, the free dictionary 
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
 Proto-Indo-European 
 Toggle Proto-Indo-European subsection 
 1.1 
 Etymology 1 
 1.1.1 
 Root 
 1.1.1.1 
 Derived terms 
 1.1.1.2 
 Descendants 
 1.2 
 Etymology 2 
 1.2.1 
 Root 
 1.2.1.1 
 Derived terms 
 1.3 
 Etymology 3 
 1.3.1 
 Root 
 1.3.1.1 
 Derived terms 
 1.4 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ wes- 
 Add languages 
 Reconstruction 
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
 
###### a20c273b41f2ed77
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ey-
FETCHED: 2026-09-05T20:21:45Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₁ey- - Wiktionary, the free dictionary
Reconstruction:Proto-Indo-European/h₁ey- - Wiktionary, the free dictionary 
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
 Proto-Indo-European 
 Toggle Proto-Indo-European subsection 
 1.1 
 Root 
 1.1.1 
 Derived terms 
 1.2 
 See also 
 1.3 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ h₁ey- 
 Add languages 
 Reconstruction 
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
 Get shortened
```


## [2026-09-05T20:36:12.213Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81we%C7%B5%CA%B0-' --note 'page 163, redirect target Wegwh, PIE root to vow' 2>&1|tail -2; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81weg%CA%B7%CA%B0-' --note 'page 163, redirect target Wegwh/Ewegwh/Eueguh = PIE *h1wegwh- to vow, speak solemnly' 2>&1|tail -2; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81weh%E2%82%82-' --note 'page 163, redirect target Eu 1 / Ewan / Wa = PIE *h1weh2- to leave, be empty' 2>&1|tail -2"
}
```


### [2026-09-05T20:36:15.956Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/11d8707d5a26c5aa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d7be8c2555333bee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/455e676ffb4a7425.txt
```


## [2026-09-05T20:36:18.853Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 11d8707d5a26c5aa d7be8c2555333bee 455e676ffb4a7425; do echo \"###### $f\"; sed -n '1,6p' $f.txt; grep -n -m4 -E \"Root ?\\[|to vow|to leave|to clothe|Pokorny\" $f.txt | head -8; done"
}
```


### [2026-09-05T20:36:20.657Z] TOOL RESULT

```
###### 11d8707d5a26c5aa
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81we%C7%B5%CA%B0-
FETCHED: 2026-09-05T20:36:14Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found###### d7be8c2555333bee
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81weg%CA%B7%CA%B0-
FETCHED: 2026-09-05T20:36:15Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₁wegʷʰ- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/h₁wegʷʰ- - Wiktionary, the free dictionary 
145: to promise , to vow 
225: Pokorny, Julius ( 1959 ), “ eṷeg ṷ h- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 1, Bern, München: Francke Verlag, page 348 
###### 455e676ffb4a7425
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81weh%E2%82%82-
FETCHED: 2026-09-05T20:36:15Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₁weh₂- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/h₁weh₂- - Wiktionary, the free dictionary 
250: Pokorny, Julius ( 1959 ), Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 1, Bern, München: Francke Verlag, page 345 of 345, 346
```


## [2026-09-05T20:36:27.684Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"== h1weh2 meaning ==\"; grep -n -m3 -E \"to leave|abandon|empty|lack\" 455e676ffb4a7425.txt | head -5; echo \"== wes- clothe ==\"; grep -n -m6 -E \"to clothe|to dress|wear\" 4c8f69f23d3ef8f2.txt | head -8; echo \"== h1ey ==\"; grep -n -m3 -E \"to go|Pokorny\" a20c273b41f2ed77.txt | head -5"
}
```


### [2026-09-05T20:36:27.759Z] TOOL RESULT

```
== h1weh2 meaning ==
141: to be/become empty [ 2 ] 
168: Hittite: 𒌋𒌦𒄩𒍣 ( u-un-ḫa-zi /⁠unḫazi⁠/ , “ to empty ” , 3s.pres. ) ( with generalised weak stem ) 
190: Proto-Celtic: *wāstos ( “ empty ” ) ( see there for further descendants )
== wes- clothe ==
165: to dress , clothe 
174: > ? Hittite: 𒉿𒀸𒊺𒄑𒍣 ( wa-aš-š-še-ez-zi /⁠waššezzi⁠/ , “ to wear, clothe ” ) 
178: *wés-tor ( “ to be wearing ” , deponent athematic Narten root present ) [ 4 ] 
180: *wos-éye-ti ( “ to dress ” , causative ) [ 4 ] 
== h1ey ==
139: to go
```


## [2026-09-05T20:36:34.309Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/BOOK | head; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; cp $S/pg163.png data/verification/sources/refs/ocr/BOOK/163.png; cp $S/pg532.png data/verification/sources/refs/ocr/BOOK/532.png; ls -la data/verification/sources/refs/ocr/BOOK/163.png data/verification/sources/refs/ocr/BOOK/532.png"
}
```


### [2026-09-05T20:36:35.959Z] TOOL RESULT

```
100.png
101.png
102.png
103.png
104.png
105.png
106.png
108.png
109.png
110.png
-rw-rw-r-- 1 sfmqrb sfmqrb 25911 Sep  5 16:36 data/verification/sources/refs/ocr/BOOK/163.png
-rw-rw-r-- 1 sfmqrb sfmqrb 44812 Sep  5 16:36 data/verification/sources/refs/ocr/BOOK/532.png
```


## [2026-09-05T20:36:37.985Z] AGENT

Now writing the verification file.


## [2026-09-05T20:37:24.293Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; cat > data/verification/page-163.json <<'JSON'\n{\n  \"pdf_page\": 163,\n  \"book_page\": 133,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"note\": \"This page contains no charts. All six entries are cross-reference stubs, printed as a column of six headword boxes each followed by italic 'see root:' and a target: Eueguh -> Wegwh, Eu-es -> Wes 3, Ewan -> Eu 1, Ewegwh -> Wegwh, Ew-es -> Wes 3, Ey -> Ei. Per the verification instructions redirect entries are skipped, so this file carries no entries. Checked against the printed page (rendered with pdftoppm -f 163, copy saved as data/verification/sources/refs/ocr/BOOK/163.png; also site/pages/163.jpg): the page shows exactly those six stubs and nothing else, so the extraction in data/extracted/batch/page-163.json is faithful, including the spelling 'Eueguh' and the running header 'Eueguh | Ey'. All four redirect targets resolve to real root boxes elsewhere in the book, and all four are genuine PIE roots: (1) Wegwh, Ewegwh, Eueguh 'to speak solemnly' stands on PDF page 532 with refs POK:348 - Pokorny's lemma 'eueg^h- (*hue-hueg^h-), Meaning: to praise, worship ... Page(s): 348' (data/verification/sources/refs/POK_full.txt line 29030ff), Watkins/AHD 'weg^wh-, Also eug^wh-. To preach, speak solemnly ... [Pok. ewegvh- 348]' (AHD_watkins1985.txt line 1132), Wiktionary *h1wegwh- 'to promise, to vow' citing Pokorny p. 348; Latin voveo, votum, Greek eukhomai, Skt. vaghat- belong here. (2) Wes 3, Ew-es, Eu-es 'to wear, put on' stands on PDF page 551 with refs POK:1172 - Pokorny 'ues-5 (*haues-5), Meaning: to dress, put on ... Page(s): 1172-1173', Watkins 'wes-4. To clothe. Extension of eu-1 ... [Pok. 5. wes- 1172]', which also explains why Nourai lists Eu-es / Ew-es as variants of the same root. (3) Ewan -> Eu 1: the box 'Eu 1, Ewan, Wa: to be empty' stands on PDF page 162 with refs POK:345 - Pokorny 'eu-1, eua-, ua- ua- (*hue-), Meaning: to lack; empty ... Page(s): 345-346', Watkins 'eu-2. Lacking, empty. Extended forms *eua-, *wa-, *wa- ... [Pok. 1. eu- 345]' (which matches Nourai's variants Ewan = *eua- and Wa = *wa-), Wiktionary *h1weh2- 'to be/become empty' citing Pokorny 345-346. (4) Ey -> Ei: the box 'Ei, Ey, I 1, Ia 1: to go' stands on PDF pages 148-149 with refs POK:293,501; KLN:825 - Pokorny 'ei- (*hei-), Meaning: to go ... Page(s): 293-297', Watkins 'ei-1. To go ... [Pok. 1. ei- 293]', Wiktionary *h1ey- 'to go'. One inconsistency, which belongs to the extraction and not to the book: the root box on PDF page 532 is printed 'Wegwh, Ewegwh, Eueguh' (see data/verification/sources/refs/ocr/BOOK/532.png), but data/extracted/batch/page-532.json records its name as 'Wegwh, Ewegwh, Euegh' - the 'u' of 'Eueguh' was dropped in extraction. The stub on this page is therefore correct as printed, and the pointer Eueguh -> Wegwh resolves exactly once page 532 is fixed. Nourai's own spelling 'Eueguh' is simply his transliteration of Pokorny's eu(e)gwh- with the labiovelar written 'guh' rather than 'gwh'; both spellings occur in the book.\",\n  \"note_fa\": \"این صفحه هیچ نموداری ندارد؛ هر شش مدخل آن تنها ارجاع‌دهنده‌اند: «Eueguh» و «Ewegwh» به ریشهٔ «Wegwh»، «Eu-es» و «Ew-es» به «Wes 3»، «Ewân» به «Eu 1» و «Ey» به «Ei». بر پایهٔ دستورالعمل ارزیابی، مدخل‌های ارجاعی بررسی نمی‌شوند، پس این پرونده بدون مدخل است. تصویر صفحهٔ چاپی (صفحهٔ ۱۳۳ کتاب) با دادهٔ استخراج‌شده مطابقت کامل دارد و خطای خوانشی در کار نیست. هر چهار ریشهٔ مقصد واقعی‌اند و در جای خود در کتاب آمده‌اند: «Wegwh» در صفحهٔ ۵۳۲ پی‌دی‌اف، برابر با هندواروپایی آغازین *h₁wegʷʰ- «سوگند خوردن، سخن آیینی گفتن» (پوکورنی، صفحهٔ ۳۴۸؛ واتکینز؛ ویکی‌واژه)؛ «Wes 3» در صفحهٔ ۵۵۱، برابر با *wes- «پوشیدن، جامه پوشاندن» (پوکورنی، صفحات ۱۱۷۲–۱۱۷۳)، که واتکینز آن را گسترش‌یافتهٔ همان ریشهٔ eu- می‌داند و همین توضیح می‌دهد چرا نورایی صورت‌های Eu-es و Ew-es را نیز آورده است؛ «Eu 1، Ewân، Wâ» در صفحهٔ ۱۶۲، برابر با *h₁weh₂- «تهی بودن، کم داشتن» (پوکورنی، صفحات ۳۴۵–۳۴۶)؛ و «Ei، Ey» در صفحات ۱۴۸–۱۴۹، برابر با *h₁ey- «رفتن» (پوکورنی، صفحات ۲۹۳–۲۹۷). تنها ناهمخوانی به این صفحه مربوط نیست: در صفحهٔ ۵۳۲ پی‌دی‌اف، کتاب «Wegwh, Ewegwh, Eueguh» چاپ کرده، ولی در دادهٔ استخراج‌شده «Euegh» ثبت شده است؛ این خطای خوانش اسکن است و باید در پروندهٔ page-532.json اصلاح شود.\",\n  \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81weg%CA%B7%CA%B0-\",\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wes-\",\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81weh%E2%82%82-\",\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ey-\"\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p. 348 (eueg^h-), p. 345-346 (eu-1), p. 1172-1173 (ues-5), p. 293-297 (ei-)\", \"stance\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: eueg^h-i* huehueg^h-) / Meaning: to praise, worship ... Page(s): 348' (line 29030); 'Root /lemma: eu-1, eua-, ua- ua-(**hue-) / Meaning: to lack; empty ... Page(s): 345-346' (line 28864); 'Root / lemma: ues-5 (* haues-5) / Meaning: to dress, put on ... Page(s): 1172-1173' (line 92484); 'Root / lemma: ei- (*hei-) / Meaning: to go ... Page(s): 293-297' (line 24798). All four match the POK page numbers carried by the target root boxes.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. weg^wh-, wes-4, eu-2, ei-1\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt: 'weg”h-, Also eug’h-. To preach, speak solemnly ... [Pok. ewegvh- 348.]'; 'wes-4. To clothe. Extension of eu-1 ... [Pok. 5. wes- 1172.]'; 'eu-2. Lacking, empty. Extended forms *eua-, *wa-, *wa- ... [Pok. 1. eu- 345.]'; 'ei-1. To go ... [Pok. 1. ei- 293.]'. Watkins' own double headword 'weg^wh-, also eug^wh-' is exactly Nourai's variant pair Wegwh / Ewegwh(Eueguh).\"},\n    {\"src\": \"BOOK\", \"where\": \"printed pp. 133 and 502 (pdf 163, 532)\", \"stance\": \"partial\", \"note\": \"pdf 163 prints six 'see root:' stubs exactly as extracted; pdf 532 prints the root box as 'Wegwh, Ewegwh, Eueguh : to speak solemnly' while data/extracted/batch/page-532.json has 'Wegwh, Ewegwh, Euegh' - an extraction error on page 532. Images: data/verification/sources/refs/ocr/BOOK/163.png, 532.png.\"}\n  ],\n  \"entries\": []\n}\nJSON\npython3 -m json.tool data/verification/page-163.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 163"
}
```


### [2026-09-05T20:37:28.012Z] TOOL RESULT

```
JSON OK
nodes verified: 0/0
node verdicts: {}
root verdicts: {}
ref checks: {}
books consulted: {} | by book: {}
```


## [2026-09-05T20:37:32.879Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git status --porcelain | head"
}
```


### [2026-09-05T20:37:32.956Z] TOOL RESULT

```
 M data/verification/sources/web/index.jsonl
?? data/verification/page-163.json
?? data/verification/sources/web/b2cc3784ee98a8e2.txt
?? data/verification/sources/web/bd6eddd0dfe470fb.txt
```


## [2026-09-05T20:37:37.176Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git check-ignore -v data/verification/sources/web/d7be8c2555333bee.txt; ls -la data/verification/sources/web/ | grep -E \"d7be|455e|4c8f|a20c|b2cc|bd6e\" ; git log --oneline -1 -- data/verification/sources/web/d7be8c2555333bee.txt"
}
```


### [2026-09-05T20:37:39.217Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb    7739 Sep  5 16:36 455e676ffb4a7425.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   11764 Sep  5 16:34 4c8f69f23d3ef8f2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    7581 Sep  5 16:21 a20c273b41f2ed77.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   17286 Sep  5 16:37 b2cc3784ee98a8e2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    2781 Sep  5 16:37 bd6eddd0dfe470fb.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6360 Sep  5 16:36 d7be8c2555333bee.txt
7d1576c Verify page 134 (Dhegh: dagh, dakhmeh, godakhtan)
```


## [2026-09-05T20:37:43.816Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git check-ignore -v data/verification/sources/refs/ocr/BOOK/163.png; git status --porcelain --ignored=no -- data/verification/sources/refs/ocr/BOOK | head -3"
}
```


### [2026-09-05T20:37:45.442Z] TOOL RESULT

```
.gitignore:9:data/verification/sources/refs/	data/verification/sources/refs/ocr/BOOK/163.png
```


## [2026-09-05T20:37:59.315Z] AGENT

Done. `data/verification/page-163.json` written; `python3 tools/verify_check.py 163` reports **0 PROBLEM lines** (`nodes verified: 0/0`).

**Page 163 (book p. 133) — verdict counts: 0 nodes, 0 root entries**

The page carries no charts at all. It is a column of six cross-reference stubs, which per the instructions are skipped, so the file has `entries: []` plus a documented `note` / `note_fa` / `consulted` (same shape as the earlier all-redirect page 146):

- Eueguh → Wegwh · Eu-es → Wes 3 · Ewân → Eu 1 · Ewegwh → Wegwh · Ew-es → Wes 3 · Ey → Ei

Checks performed anyway (recorded in the file):
- Printed page rendered and read (`data/verification/sources/refs/ocr/BOOK/163.png`): the six stubs match `data/extracted/batch/page-163.json` exactly, spelling "Eueguh" included. Extraction of page 163 is faithful.
- All four targets resolve to real root boxes in the book and are genuine PIE roots: Wegwh (pdf 532, POK:348 = Pokorny *eu̯egʷh- "to praise, worship"; Watkins "weg\*wh-, also eug\*wh- To preach, speak solemnly"; Wiktionary *h₁wegʷʰ-), Wes 3 (pdf 551, POK:1172 = Pokorny ues-5 "to dress, put on"; Watkins "wes-4 To clothe, extension of eu-1", which also justifies Nourai's Eu-es/Ew-es variants), Eu 1/Ewân/Wâ (pdf 162, POK:345 = Pokorny eu-1 "to lack; empty", Watkins extended forms *euə-/*wā- matching Ewân/Wâ), Ei/Ey (pdf 148–149, POK:293 = Pokorny ei- "to go").

**Extraction error for the owner to fix (on another page, found while resolving the redirect):**
- `data/extracted/batch/page-532.json` entry 0 root name is `"Wegwh, Ewegwh, Euegh"`, but the printed box (book p. 502 / pdf 532, image saved as `.../ocr/BOOK/532.png`) reads **"Wegwh, Ewegwh, Eueguh"** — the "u" was dropped. With that fixed, page 163's `Eueguh → Wegwh` pointer matches verbatim.

No disputed or transcription_suspect items (no nodes exist on this page). Four Wiktionary pages archived via `fetch_source.py`; the file is written but not committed.
