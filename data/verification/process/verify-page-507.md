# Verification process log — verify-page-507


## [2026-10-15T02:44:16.306Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 507 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-507.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-507.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-507.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 507` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.374Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.540Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.626Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):
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
279	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-10-15T02:44:21.758Z] TOOL CALL #2: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/agent/charts/page-507.txt; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; ls data/verification/page-50*.json"
}
```


## [2026-10-15T02:44:22.036Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat tools/verify_check.py | head -150"
}
```


### [2026-10-15T02:44:22.585Z] TOOL RESULT

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


### [2026-10-15T02:44:22.612Z] TOOL RESULT

```
=== PDF page 507 (book page 477) ===
--- entry 0 ---
ROOT [Indo-European] Tĕu 1 : to swell  (refs POK:1082)
#1 (parent #0) [Avestan] refs=POK:1082; HRN:89; NYB:196 | tav : power, to be powerful ; tavant : fast, quick ; tum-âspa : (with) strong horses ☞Ekwos ; us-tavah : out of power, tired ☞Ud 1 ; ni-us-tavah : not tired (of fighting) ☞Ne 1
  #2 (parent #1) [Persian] refs=BQT:517,526,1102,1362,2138 | tavân «توان ( توانستن )» : power ; tond «تند» : fast ; Tahmâsb «تهماسب (طهماسب)» : "with strong horses" ; sotŭh «ستوه» : tired ; nastŭh «نَستوه» : energetic in fighting
#3 (parent #0) [Persian] refs=IEC:1450,1458 | tŭbreh «توبره» : bag
#4 (parent #0) [Latin] refs=AHD | tuměre : to swell ; tŭber : lump, bag
  #5 (parent #4) [English] refs=AHD | tumor
#6 (parent #0) [Greek] refs=AHD | turus : coagulated milk, cheese, butter ; tumbus : mound of earth, tomb
  #7 (parent #6) [English] refs=None | butter, tomb
#8 (parent #0) [Germanic] refs=AHD | thŭmon : fat finger, thumb ; thus-hundai : swollen hundred, thousand ; thiuham : fat part of leg, thigh
  #9 (parent #8) [English] refs=None | thumb ; thousand ; thigh
#10 (parent #0) [Indo-European] refs=POK:1085 | Teuk : egg, seed, offspring
  #11 (parent #10) [Avestan] refs=POK:1085 | taoxman : seed, egg
    #12 (parent #11) [Persian] refs=HRN:84; MON:1052 | toxm «تخم» : egg, seed, testicle | extra: تخمه ، تخمک
    #13 (parent #11) [Sogdian] refs=SOD:387 | txm : seed, family
  #14 (parent #10) [Old Persian] refs=KNT:185; HID:211; BST:233 | taumâ : family
#15 (parent #0) [Indo-European] refs=POK:1083; AHD | Tauro : bull
  #16 (parent #15) [Avestan] refs=None | staura, staora : strong domestic animals
    #17 (parent #16) [Persian] refs=BQT:1102; HRN:152 | sotŭr «ستور» : load carrying animals
  #18 (parent #15) [Arabic] refs=POK:1083; KLN:1509 | thwr : bull
    #19 (parent #18) [Persian] refs=BQT:550 | sowr «ثور» : cow, bull
  #20 (parent #15) [Latin] refs=POK:1083 | taurus : bull
    #21 (parent #20) [English] refs=None | Taurus
  #22 (parent #15) [Germanic] refs=AHD | situraz : ox
    #23 (parent #22) [English] refs=None | steer
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  incoming
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ocr
drwxr-xr-x     - sfmqrb 14 Oct 22:19  pageimg
drwxr-xr-x     - sfmqrb 14 Oct 22:25  tessdata
.rw-r--r--  600k sfmqrb 14 Oct 22:19  AFA.txt
.rw-r--r--   15M sfmqrb 14 Oct 22:19  AFM.pdf
.rw-r--r--  355k sfmqrb 14 Oct 22:19  AFM.txt
.rw-r--r--  384k sfmqrb 14 Oct 22:19  AFM_alt.txt
.rw-r--r--  342k sfmqrb 14 Oct 22:19  AFM_pages.txt
.rw-r--r--  850k sfmqrb 14 Oct 22:19  AHD_watkins1985.txt
.rw-r--r--  825k sfmqrb 14 Oct 22:19  AHM.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  AID.txt
.rw-r--r--  240k sfmqrb 14 Oct 22:19  AIN.txt
.rw-r--r--  256k sfmqrb 14 Oct 22:19  AKD.txt
.rw-r--r--  285k sfmqrb 14 Oct 22:19  ARB_abdulraheem.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  ARB_mo3rb.txt
.rw-r--r--  744k sfmqrb 14 Oct 22:19  ARP.txt
.rw-r--r--  633k sfmqrb 14 Oct 22:19  AVG.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_alt_v1.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  BQT_dli_part1.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_v1.txt
.rw-r--r--   26M sfmqrb 14 Oct 22:19  BQT_v1_djvu.xml
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  BQT_v1_pages.txt
.rw-r--r--  2.4M sfmqrb 14 Oct 22:19  BQT_v2.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  BQT_v2_pages.txt
.rw-r--r--  4.8M sfmqrb 14 Oct 22:19  BRT.txt
.rw-r--r--  656k sfmqrb 14 Oct 22:19  BST.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  CHEUNG.txt
.rw-r--r--  593k sfmqrb 14 Oct 22:19  DEV.txt
.rw-r--r--  144k sfmqrb 14 Oct 22:19  DOZ.txt
.rw-r--r--  1.5M sfmqrb 14 Oct 22:19  DRM.txt
.rw-r--r--  560k sfmqrb 14 Oct 22:19  EAV_studies.txt
.rw-r--r--  891k sfmqrb 14 Oct 22:19  FRS.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  FRS_pages.txt
.rw-r--r--   16M sfmqrb 14 Oct 22:19  FSD_vol1.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol2.txt
.rw-r--r--   13M sfmqrb 14 Oct 22:19  FSD_vol3.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol4.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  FSF.txt
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  FSF_pages.txt
.rw-r--r--  650k sfmqrb 14 Oct 22:19  FVQ.txt
.rw-r--r--  628k sfmqrb 14 Oct 22:19  FVQ_pages.txt
.rw-r--r--  573k sfmqrb 14 Oct 22:19  GPL.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  HENNING_selected_papers.txt
.rw-r--r--  449k sfmqrb 14 Oct 22:19  HID.txt
.rw-r--r--  5.6M sfmqrb 14 Oct 22:19  HJB.txt
.rw-r--r--  688k sfmqrb 14 Oct 22:19  HRN.txt
.rw-r--r--  527k sfmqrb 14 Oct 22:19  HUB.txt
.rw-r--r--  3.3M sfmqrb 14 Oct 22:19  IEC.txt
.rw-r--r--  3.4M sfmqrb 14 Oct 22:19  ISS_alt_DKS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  KFL.txt
.rw-r--r--   11M sfmqrb 14 Oct 22:19  KLN_1966.txt
.rw-r--r--   10M sfmqrb 14 Oct 22:19  KLN_1971.txt
.rw-r--r--  874k sfmqrb 14 Oct 22:19  KNT.txt
.rw-r--r--  944k sfmqrb 14 Oct 22:19  KNT_full.txt
.rw-r--r--  488k sfmqrb 14 Oct 22:19  LAM.txt
.rw-r--r--  4.6M sfmqrb 14 Oct 22:19  LAT.txt
.rw-r--r--  627k sfmqrb 14 Oct 22:19  LEW_1910.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  LKT.txt
.rw-r--r--   62k sfmqrb 14 Oct 22:19  LST.txt
.rw-r--r--  4.4M sfmqrb 14 Oct 22:19  MON_part1.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  MON_part2.txt
.rw-r--r--  373k sfmqrb 14 Oct 22:19  MPP.txt
.rw-r--r--  470k sfmqrb 14 Oct 22:19  NAT_2005.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  NYB.txt
.rw-r--r--  505k sfmqrb 14 Oct 22:19  NYB_vol1.txt
.rw-r--r--  920k sfmqrb 14 Oct 22:19  NYB_vol2_glossary.txt
.rw-r--r--  664k sfmqrb 14 Oct 22:19  PEI.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD.pdf
.rw-r--r--  341k sfmqrb 14 Oct 22:19  PHD.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD_mackenzie.pdf
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_mackenzie.txt
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_pages.txt
.rw-r--r--  604k sfmqrb 14 Oct 22:19  PHN.txt
.rw-r--r--  982k sfmqrb 14 Oct 22:19  POK_01.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  POK_02.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  POK_03.txt
.rw-r--r--  4.0M sfmqrb 14 Oct 22:19  POK_full.txt
.rw-r--r--  9.8M sfmqrb 14 Oct 22:19  RCH.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SBK.txt
.rw-r--r--  226k sfmqrb 14 Oct 22:19  SDQ.txt
.rw-r--r--  1.4M sfmqrb 14 Oct 22:19  SIN.txt
.rw-r--r--  2.7M sfmqrb 14 Oct 22:19  SKT.txt
.rw-r--r--  3.0M sfmqrb 14 Oct 22:19  SKT_dli_revised.txt
.rw-r--r--  326k sfmqrb 14 Oct 22:19  SNS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SNS_pages.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  SOD.txt
.rw-r--r--  3.7M sfmqrb 14 Oct 22:19  SOD_pages.txt
.rw-r--r--  466k sfmqrb 14 Oct 22:19  SPG_keilinschriften1881.txt
.rw-r--r--  4.5M sfmqrb 14 Oct 22:19  SYN.txt
.rw-r--r--  152k sfmqrb 14 Oct 22:19  TAD.txt
.rw-r--r--  243k sfmqrb 14 Oct 22:19  TAD_pages.txt
.rw-r--r--  313k sfmqrb 14 Oct 22:19  TLM.txt
.rw-r--r--   89k sfmqrb 14 Oct 22:19  UNV.txt
.rw-r--r--   12M sfmqrb 14 Oct 22:19  WEB_vol1.txt
.rw-r--r--  317k sfmqrb 14 Oct 22:19  WLD_band3.txt
.rw-r--r--  549k sfmqrb 14 Oct 22:19  ZAP.txt
Permissions Size User   Date Modified Name
.rw-r--r--   69k sfmqrb 14 Oct 22:14  data/verification/page-50.json
```


## [2026-10-15T02:44:47.767Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False)[:2500]);print(json.dumps(e['nodes'][0],ensure_ascii=False)[:3000])\"; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));\nfor k in ['POK','AHD','HRN','NYB','BQT','IEC','MON','SOD','KNT','HID','BST','KLN']: print(k, json.dumps(d.get(k),ensure_ascii=False)[:500])\""
}
```


### [2026-10-15T02:44:48.223Z] TOOL RESULT

```
{"entry": 0, "root": "Tel", "verdict": "confirmed", "modern_form": "PIE *telh₂- 'to lift, bear, weigh; endure' (Pokorny 1. tel-, telə-, tlē-, tlā- 1060-1061; Watkins/AHD telə-; LIV² 622-623)", "note": "Pokorny IEW pp.1060-1061 heads the entry '1. tel-, telə-, tle(i)-, tlā-' 'to transport, carry; to bear, suffer', Watkins (AHD) 'telə- to lift, support, weigh', modern notation *telh₂-. Nourai's 'Tel : to lift', the label Indo-European and both his citations (POK:1060; KLN:122 = Klein s.v. Atlas, which spells out the base *tel-, *tal-, *tol- 'to bear, lift, suffer') are correct. The Greek, Latin, Sanskrit and English branches are standard (Pokorny, Walde-Pokorny, Watkins, Klein all list them). Two Iranian/Persian problems: (1) the 'Avestan' tara-āz(u) is Nyberg's reconstructed Old Iranian *tarā-āzu-, not an attested Avestan word; (2) the Persian tarāz/طراز box mixes tarāzū 'balance' (correct) with ṭarāz/tarāz 'adornment' and the city Ṭarāz of Farrokhī's verse, and the Persian atlas 'world' (falak-e atlas) is native Arabic aṭlas 'plain, smooth', not Greek Atlas. Toll's Greek origin is contested (Wiktionary prefers a native Germanic word). No extraction errors: the JSON matches the printed page, including the odd ref 'MON5:5155' (a misprint in the book, presumably for MON5:155).", "note_fa": "ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، بردن، سنجیدن؛ تاب آوردن» است؛ پوکورنی (ص۱۰۶۰–۱۰۶۱) آن را «tel-، telə-، tlā-» با معنای «بردن، حمل کردن؛ تحمل کردن» و واتکینز «telə- برداشتن، نگه داشتن، وزن کردن» آورده‌اند. «Tel: برداشتن» نورایی، برچسب «هندواروپایی» و هر دو مأخذ او (پوکورنی ۱۰۶۰ و کلاین ۱۲۲ ذیل Atlas) درست است. شاخه‌های یونانی، لاتین، سنسکریت و انگلیسی همه پذیرفته‌اند. اشکال‌ها در بخش ایرانی است: «tara-âz» اوستایی نیست بلکه بازسازی ایرانی باستانِ نیبرگ است؛ در خانهٔ فارسی «ترازو» درست است ولی «طراز» (زینت، و شهر طراز در بیت فرخی) واژهٔ دیگری است؛ و «اطلس» به معنای «فلک اطلس/جهان» از صفت عربی «أطلس» (صاف، بی‌نقش) است نه از تیتان یونانی. خطای استخراج دیده نشد.", "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-", "https://en.wiktionary.org/wiki/Ἄτλας", "https://en.wiktionary.org/wiki/τάλαντον"], "ref_check": [{"ref": "POK:1060", "status": "supports", "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tl
{"id": 1, "lang": "Sanskrit", "words": "tulâ, tulya", "verdict": "confirmed", "derivation": "Sanskrit tulā́ f. 'balance, scales; weight' continues the zero grade *tl̥h₂-éh₂ of PIE *telh₂- 'to lift, weigh, bear': syllabic *l̥ before the laryngeal gives Indo-Aryan ul (the l is the dialectal Indo-Aryan reflex of *l, the u the coloured vowel of the syllabic liquid). tulya- 'equal in weight, comparable, equivalent' is the -ya- derivative of tulā (Wiktionary: from tulā + -ya), and the verb tulayati 'lifts, weighs' belongs here. Nourai's gloss 'balance weight' fits tulā exactly; for tulya the precise sense is 'of equal weight, comparable', a natural derivative.", "derivation_fa": "سنسکریت tulā «ترازو، کفهٔ ترازو، وزن» از پایهٔ ضعیف *tl̥h₂-éh₂ ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، وزن کردن، تحمل کردن» است؛ l هجایی پیش از همخوان حلقی در هندی باستان به ul بدل شده است. tulya «هم‌وزن، همسنگ، همانند» صفتی است که با پسوند -ya از همین tulā ساخته شده و فعل tulayati «برمی‌دارد، می‌سنجد» نیز از همین ریشه است. ادعای نورایی درست است (پوکورنی ۱۰۶۰، واتکینز، والده‌ـپوکورنی، کلاین، ویکی‌واژه).", "sources": ["https://en.wiktionary.org/wiki/तुला", "https://en.wiktionary.org/wiki/तुल्य", "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-"], "ref_check": [{"ref": "POK:1060", "status": "supports", "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''."}, {"ref": "AHD", "status": "supports", "note": "Watkins AHD Roots s.v. telə- item 9: 'Suffixed zero-grade form *tl-ā- in Sanskrit tulā, scales, balance, weight: TAEL, TOLA.'"}], "consulted": [{"src": "WLD", "where": "Bd. I p.738 s.v. 1. tel-", "stance": "supports", "note": "Walde-Pokorny Bd. I pp.738-740 (local WLD_Bd1_pages.txt leaves 747-749) '1. tel- „aufheben, z. T. wägend, z. T. sich aufladend; tragen; ertragen, dulden“: Ai. tulā „Waage, Waagbalken“, tulayati „hebt auf, wägt“' ... 'τάλαντον ... eig. „die beiden Waagschalen“', 'Ἄτλας, -αντος', 'lat. tollo ... tolero ... lātus'."}, {"src": "KLN", "where": "1966 s.v. tolerate / talent", "stance": "supports", "note": "Klein 1966 s.v. tolerate (KLN_1966.txt line 39457): 'L. tolerare ... from the stem of tollere ... cogn. with ... ταλάντον 'balance', ''A-τλας 'the Bearer (scil. of Heaven)', L. lātus (for *tlatos) 'borne', OI. tulā 'balance', tulayati 'lifts up, weighs' ... All these words derive fr. I.-E. base *tel-, *tol-, *tal-, *tl- 'to bear, carry, endure, suffer'.'"}, {"src": "IEC", "where": "s.v. tl- (1) (IEC.txt line 18624)", "stance": "silent", "note": "Mann: 'tl- (1) ... lift, raise, bear, suffer'. WP I, 701 & 738-9' with Tocharian, Greek tlēmi, Latin tuli, Gothic þulan —
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed p
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g.
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qat
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (re
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt", "page_offset": "le
HID {"title": "C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883", "edition_found": "1883", "kind": "archive_djvu", "url": "https://archive.org/details/handbuchderalti00bartgoog", "identifier": "handbuchderalti00bartgoog (also handbuchderalti01bartgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HID.txt", "page_offset": "leaf = printed + 13 (e.g. leaf 14 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a
BST {"title": "P. Horn, 'Some Inscriptions on Sassanian Gems', in Avesta, Pahlavi and Ancient Persian Studies in honour of Dastur P. B. Sanjana, First Series, Bombay 1904, pp. 224-263", "edition_found": "1904", "kind": "archive_djvu", "url": "https://archive.org/details/avestapahlavianc00sanjuoft", "identifier": "avestapahlavianc00sanjuoft (also in.ernet.dli.2015.281259)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BST.txt", "page_offset": "leaf = printed + 16 (e.g.
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the
```


## [2026-10-15T02:44:50.940Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/507.jpg; pdftoppm -f 507 -l 507 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg507; cat data/extracted/batch/page-507.json | head -60"
}
```


### [2026-10-15T02:44:52.058Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   78k sfmqrb 14 Oct 22:15  site/pages/507.jpg
{
  "pdf_page": 507,
  "book_page": 477,
  "entries": [
    {
      "root": {
        "name": "Tĕu 1",
        "lang": "Indo-European",
        "refs": "POK:1082",
        "gloss": "to swell"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1082; HRN:89; NYB:196",
          "words": [
            {"translit": "tav", "gloss": "power, to be powerful", "script": null},
            {"translit": "tavant", "gloss": "fast, quick", "script": null},
            {"translit": "tum-âspa", "gloss": "(with) strong horses", "script": null, "see": ["Ekwos"]},
            {"translit": "us-tavah", "gloss": "out of power, tired", "script": null, "see": ["Ud 1"]},
            {"translit": "ni-us-tavah", "gloss": "not tired (of fighting)", "script": null, "see": ["Ne 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:517,526,1102,1362,2138",
          "words": [
            {"translit": "tavân", "gloss": "power", "script": "توان ( توانستن )"},
            {"translit": "tond", "gloss": "fast", "script": "تند"},
            {"translit": "Tahmâsb", "gloss": "\"with strong horses\"", "script": "تهماسب (طهماسب)"},
            {"translit": "sotŭh", "gloss": "tired", "script": "ستوه"},
            {"translit": "nastŭh", "gloss": "energetic in fighting", "script": "نَستوه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بیازید هوشنگ چون شیرچنگ - جهان کرد بردیو نستوه تنگ",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:1450,1458",
          "words": [
            {"translit": "tŭbreh", "gloss": "bag", "script": "توبره"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
```


## [2026-10-15T02:44:53.978Z] TOOL CALL #6: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg507.png"
}
```


### [2026-10-15T02:44:54.402Z] TOOL RESULT

```

```


## [2026-10-15T02:44:54.398Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-15T02:44:56.884Z] AGENT

The extraction matches the printed page, including "situraz" and "tum-âspa". Now the local reference lookups.


## [2026-10-15T02:44:58.052Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"teu-2\\|Root /lemma: teu\\|Root /lemma: t[eē]u\\|tauro-\\|Root /lemma: teuk\\|Root /lemma: (s)teu\" POK_full.txt | head -30"
}
```


### [2026-10-15T02:44:58.615Z] TOOL RESULT

```
7517:{ve- 5/7///-e (participle of alb. 5/7/KA7y"push with difficulty') see Root /lemma: (s)teu-1\ "to 
82919:Root / lemma: steu-2 
86443:Root / lemma: teu-2
```


## [2026-10-15T02:45:00.240Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 86443,86700p POK_full.txt | cut -c1-220"
}
```


### [2026-10-15T02:45:00.574Z] TOOL RESULT

```
Root / lemma: teu-2 
Meaning: to listen to, observe 

Material: Latin tueor, -en, tuitusdx\(^ tutatus sum' beirachten, observe, shield ', intu(e)or 
"consider', originally in-, ob-, con-tuor con-tud; /J/^s "certainly'; Old Irish cumtuth' 
protec\.\or\'{*kom-uc/-tou/tus), mcymr. /i/d"cover', tudec/'s\eeve, wrapping, dress', bret. dial. 
/^ec(abret. *tudoc) "Kissenbezug'; Old Irish /Jas-ce/Y "northern', bret. /^5 "links' {*teu-sto-)\ 
Celtic *feu-to-'\n mcymr.M" magician ', Middle Irish tuatha/dds., Old Irish /J5///7 "northern', 
Middle Irish tuath'Wnks, northern, mad, wicked, evil' (from "*gunstig, good' as Antiphrasis 
zur appellation the ungliJckbringenden Linken); in addition Gothic A'/Z/A'"das Gute', Old 
Icelandic f^ydr'mM, friendly', f^yda' friendship'. Old English gedfede'good, tugendhaft', 
gedTedan ' s\c\r\ (friendly) anschlieften'; probably also Old English deaw' custom, custom'. 
Old Saxon thau, Old High German gethau 'D\sz\p\'\n' as "*observantia'; perhaps also gr. 
Tuaasi iK£T£U£i Hes. (denominative eines *tut6(; with similar meaning as Gothic P/uf^Jan 
"segnen' from P/'uf^). 

References: WP. I 705 f., WH. II 713 f.. Loth RC 43, 160 ff. 
Page(s): 1079-1080 

Root / lemma: teup- 

Meaning: to get down, conceal oneself 

Material: Gr. £VTuna(; Adv., II. 24, 163, if meaning "cowering, crouching'; presumably Old 

Icelandic f^optat " thwart ' ("auf the gehockt wird'). Old High German doftai.. Middle Low 

German duchti.. Old English doftds. (wherefore Old Icelandic t^optixw. " Mitruderer', Old 

English ^edc»//a "comrade'. Old High German gidufto' Mitruderer, comrade') and Gothic 



I=>iubjd^ clandestine ', t^iubs^\h\ef, Old Icelandic t^jofr, Old English deof. Old Saxon thiof, 
Old High German oVioZ? 'thief; 

Lithuanian tupiu, tupt/'s\ch hinhocken, in die Knie place', tup/'u, tupetr crouch, in den 
Knien sit', Latvian tupt^ crouch '. 

References: WP. I 714. 
Page(s): 1 085 

Root / lemma: teus- 

Meaning: to empty 

Material: Avestan Kaus. taosayeiti^ makes loose, allows loose' {*touseid), Inchoativ {*tus- 

sRo) Avestan fus9n's\e verlieren die Fassung', baluci fusag, thuay' abandon become'; 

Old Indie tuccha-, tucchya- {*tus-sRo-, *tus-sR-Jo-) " empty, bare, lacking, deserted, 

abandoned, forsaken, worthless', afghan. tas^ empty, bare, lacking'; Latin tesquau. PI. 

"Einoden' {*tueskua)\ Old English dost^ manure'. Old High German dostds. 

("*Ausleerung'); Old Church Slavic tbstb ' kevoc,' , russ. tosc/j" empty, bare, lacking; lean, 

hager' etc. (= Old Indie tucchya-). 

References: WP. I 714, WH. II 675, Trautmann 333, Vasmer 3, 130, Mayrhofer 1, 508 f. 

Page(s): 1 085 

Root / lemma: teya- tua- 

Meaning: to sift 

Material: Old Indie ///^^-(dreisilbig, from *titavu-l) " sieve, Getreideschwinge'; 

gr. aau) (Ionian), tw (Attic EM.), Attic SiaiTau) " sieve ' (*TFaju)), 5iaTT0(; m. " sieve ' Hes., 
£TTr||J£va GsaniJSva Hes., aAsupoTnoK; f. "Mehlsieb' (EM.), anOw 'siebe'. 

References: WP. I 713; Mayrhofer 1 , 499 f. 
Page(s): 1 085 

Root / lemma: teg- tag- 

Meaning: to burn 

Material: Gr. rnyavov, Attic through metathesis also Taynvov ' frying pan, Tiegel'; 

Old English deccan'burn' (is daece//e ^torcW from fgecele, loanword from Latin facula, 
reshaped?). Old High German dahhazzen lo6ern' . 

References: WP. I 717f. 



Page(s):1057 



Root / lemma: teu- teu-, teua-, tuo- tu- 

Meaning: to swell; crowd, folk; fat; strong; boil, abscess 

Note: extended with b^, g, k, I, m, n, r, s, t 

Material: Old Indie tav/'f/"\s strong, has Macht', Perf. tutava; in addition /ai/as- 'strong, 

stalwart ', as Subst. Akk. tavasam, Instr. tavasa^ power, strength '; tavyas- tavTyas- 

"stronger', tavasvant- 'strong', tavismant- 'strong, mighty', /ai//5^- 'strong', tavisTi. 'force, 

power'; ablaut. /^K/-in Kompositis 'very, mighty', tuv/stama-'t\r\e starkste': tuya- 'strong, 

fast, rapid, hurried'; 

Avestan tav- ' to be capable of ', tavah- n. 'power, force', tavTsTi. ' physical strength '; 
ap. atavayam'\ am able ', tunuvant- 'mighty', tauvTyah- 'stronger' (: Old Indie tavTyas-), 
tauman- n. 'fortune, force, power'; 

Armenian //Vnumber'; doubtful f up {*tu-pho-) ' thicket, shrubbery, bush'; 

gr. TiTu6(; the name of geilen Frevlers wider die Leto; Tau(; psyaq, noAuq Hes. ( *tau-u-s), 
Tauaa(; pi£YaAuva(;, -nkzovaaac, Hes.; aaoc, (Cypriot laFoKAsFr)";). Kompar. aaikiiz^oc,, 
contracted Ionian Attic oGiO,, aGiOO, 'heil, unbroken, unmarred, unscathed, undamaged; 
certain ' (from *tu9-uo-s)\ compare M. Leumann Gedenkschrift Kretschmer II 8 f.; in 
addition hom. aa(F)6u), hom. Attic acb^u) (*au)'i'^u)), Fut. acbau) 'rescue, receive', aojirip 
'savior, redeemer' etc.; ('voll an body = fit, healthy'); awpa n. 'body' {*tud-mn 
'Gedrungenes'), awijaTOw 'fest make, verdichten'; acb-cppwv faao-cppojv) 'fit, healthy an 
Geist, vernijnftig'; with the same Wurzelstufe still aud^bc,, S. 1083; 

Latin *toved, -e/ie'vollstopfen' as base from /d/77e/7/^/77'Polsterung' {*touementom) and 
/o/^s 'whole' (*/o^e'/cs'vollgestopft, compact '); 

russ. -Church Slavic tyju, /yZ/'fett become', ablaut, serb. tovm. 'Fettigkeit'. 

1. b^-extension: 

Latin tuber, -er/sn. ' hunch, swelling, blister, tumefaction, knag'; compare Oscan- 
Umbrian gloss, tufera and Italian tar-tufo, -tufo/o ^terrae tuber'; 

gr. Tucpn 'zum Ausstopfen from Polstern and Betten used Pflanze' (probably u); 



perhaps Old Irish tuaimm^WiW {*tedb^-mn), Middle Irish tomxw. "hill, bush', cymr. tomi. 
"hill, DiJngerhaufen' {*fub^-mo-, -ma); cymr. fumonla croupe'; also ys/^/77 "bend' from 
*eks-teLb^-mo-, different above S. 1034; 

Old Icelandic A'J/^ "elevation in the earth, Hijgelchen', obd. o'^pyoe/" swelling, blister, 
swelling, lump, growth'. 

With the meaning " tussock ': Old English dufm. " foliage bunch, ein from FederbiJschen 
zusammengesetztes banner', ^edjrblatterreich, luscious', dJf/"ein Platz voll from 
BiJschen', dj?fe/"bush, thicket, blattreiche plant', dufian^s\c\\ belauben'; from the language 
Germanic Soldaten derives Latin tufa^a kind of Helmbuschel' (Vegetius). 

2. ^^extension: 

Old Icelandic f^okalog', Middle Low German dak{e) (from *doke) ds.. Old Swedish 
thukna6s.. Old English duxian^6ark make'. Old Saxon thiustri. Middle Low German duster 
(out of it Modern High German duster). Old English dJestre "dark' ( *t^euxstria-). 

3. A'-Erweiterung: "to swell; fat' (as Old Church Slavic /y-//"fett become'): 

Latin tuccetum^a kind of Bauernwurst', tucca^Ka\dK\j\ya lp}\\o\)\ Umbrian /oco "tuccas' 
(gall, loanword); Old Church Slavic tuk-b "fat'; Old High German dioh. Old English deoh^ 
thigh ', Old Icelandic t^Jo^ihe thick Oberteil of Schenkels, Arschbacke'; engl. thigh; Middle 
Irish tdrrm., cymr. tint "podex' {*tuknaR); Lithuanian taukafiat', /5^/r55 "FettstiJckchen' 
and "uterus', tunku, tukti'iett become', Latvian tukt6s., /J/rs "swelling, lump, growth', tauks 
"fat, fat, obese', taukiP\. "fat, tallow, suet'. Old Prussian taukis^ lard '; compare S. 1085 
teuk- "germ, sprout' and den gr. FN T£UKpo(;. 

4. ^formations, partly as root-like *tu-ei- appearing: 

Old Indie tuiam ^R\spe, whisk, tussock, Baumwolle', tuiF-i. "paintbrush', pali tuia-n. " 
hassock, clump of grass ' etc.? compare Mayrhofer 1 , 520; 

gr. TuAri f., TuAo(; m. " bulge; bead; lip; torus; wreath; roll; bulb, weal, callus, hump, 
hunchback ', and "peg, plug, nail, penis'; alb. tui m. "FleischstiJck without bone, calf; 

Latin /^///^5"Schwall, downpour' {*tui-no- or -so-); perhaps also Tuiius, Tuilius onig\v\a\\y 
name for thick, gedunsene Personen, whether not Etruscan; 

Old English gedyli^ draught ' (?), Old Icelandic fimbul-l=>ui^a mythical river'; Old 
Icelandic t^oiir {*tui-no- or -so-) "tree, peg, plug', Swedish /^//"Baumwipfel', Old English doii 



m. "Ruderpflock', Middle Low German dolle, dulle6s., Modern High German Do//e ds. and 
"Krone eines Baumes, Blumenbuschel, tassel, Helmbusch', obd. Z7c>//f^yS'angeschwollener 
foot, clubfoot, misshapen deformed foot ', Tirol do//'th\ck', Middle Low German westfal. 
(yL^/Ze" swelling, blister'; perhaps the Germanic island name 0ouAr|; 

Old Prussian tulan My. "much, a lot of, Lithuanian /i//as"mancher'; 

Church Slavic /y/b " nape '; also Old Church Slavic *//b5/b, russ. tolstyjeic. "thick' 
(imitation of Endinges from Slavic ggsti^ "dense, thick'). 

A extension with Baltic z(lndo Germanic ^ or gh) is Lithuanian pa-tulzgs "swollen', 
Latvian /^/z^/77s "swelling, lump, growth', /i/Zz/?© "blister, bubble'; Lithuanian /i//z/s"gair; 

redupl. perhaps Latin tutulus^ high kegelformige Haartracht, Toupet'; the pilleus lanatus 
the Flamines and Pontifices and Latvian tuntu/et {a\so tunturet) "sich in viele 
KleidungsstiJcke einhijllen'. 

tuel-, tuj-. gr. at most in oaAoq n. "Wogenschwall, uncontrollable Bewegung (of 
Meeres)', oaAsTaGai " jump ', oaAsuu) "shake, shatter; schwanke', KOvia-aaAot; m. 
"Staubwirbel'; Middle Irish/e/and 1{a)ur shield boss ', Old Irish Middle Irish telach, 
t(a)ulach^\\\\\\ redupl. tuthle {* tu-tuel-) "swelling, lump, growth' (die i/-forms through eine 
similar results of Aniauts *tu- as Old Irish cruthixom *kYtu-)\ cymr. twlch^ round mass, hill, 
nipple '. 

5. m- derivatives: 

Old Indie /J-/^/77^-"wirkungsvoir, /i//77/'a- "strong, thick', tumala-, /^/77^/5- "gerauschvoll, 
larmend', tuma/a-m'd\n, fuss, noise' ("*Schwall, das larmende Durcheinandera 
zusammengedrangten Menge'); Avestan *tuma-\n Tumaspana- Irom Tumaspa- {that \s to 
say einem, dessen Rosse fat, obese are) stammend'; gr. korkyr. tOjjoc; "TU[jpO(;'; 

gr. TU|jpO(; "burial mound, hillock' = Middle Irish tommm. "hill, bush', cymr. tomt 
"hillock, DiJngerhaufen', whether diese not but from *tub'"-mo-, -ma- (above S. 1080); 

Latin turned, -e/'e"geschwollen sein', fum/dus 'swoWen', tumor' sweWlng, lump, growth', 
/i//77^/i/s"Erdhaufen, hillock', /^/77^//^s "larmende restlessness, din, noise '; 

cymr. twf power, strength ', ///^"zunehmen, grow' {*tum-), Middle Breton tinva{*tum-) 
"zusammenwachsen (from an wound); thrive'; 



Old Swedish /=>um/m. " thumb ', f^um'ioW, Old Icelandic l=>umair thumb '; Old High 
German dumo. Old English duma^ thumb ', dJ//77e/Tingerhut', Middle Low German 
dumelinc. Modern High German Daumling; Middle High German doum^ spigot, bung, clot, 
thrombus' (meaning as gr. tuAoc;); 

Lithuanian tumet/lat become, curdle, coagulate, harden ', tum{s)tas^ heap, bulk, mass', 
tumu/asm. "piece'; 

Tocharian B tumane, tmane, A tman^'^ 0.000'. 

6. />formations, z. T. as root-like %/-e/7- appearing: 

pre Modern High German tunne^ surge ', Low German duning, diinung ^waves, billows 
gegen die Windrichtung'; but Old Irish tonn, (common Celtic -ns-, -nt- > -nn-), bret. etc. ton 
"wave' from *tus-na{see 1084) or *to-sna{see 971 f.); Low German dunen'to swell'. 
Middle Low German dun{e) "swollen, dense'; 

Lithuanian tvjstu, tvinali, tv/nt/"to bloat, bulge, swell (of water)', Kaus. tvindau, -yti 
"anschwellen make' (with ablaut derailment /i/5//7y//s"buhlen', if actually "to swell'), tvanas 
"flood', /i/5/76's"light tumescent (of river)', Latvian tvans, tvana'vapor, haze, mist'. 

With -/7A'-extension: Lithuanian tv/nkt/'to bloat, bulge, swell, fester' = Latvian Mkt 
"sultriness feel, vor Hitze languish '; Latvian tvTcinat^ make muggy, make thirsty ', 
Lithuanian /i///7/rsc/c»//"fuhlbar hit (of Puis)', Lithuanian tvenktT swell make', tvankas 
"sultriness', /Ka/7/r^5 "muggy' (ablaut derailment in Latvian tveicinat= fv/c/natan6 tvaiks 
"vapor, haze, mist, sultriness'); with /!Lithuanian tuntas^heap, bulk, mass' = tumtas, 
wherefore perhaps gr. tuvtAo(; "ordure, slime, mud' (as RiJckstand of an inundation)? 

Auf a *tu-en : *tuen-6s, *tun- '(pakkoq' based on gr. aa9r| "penis' (formation as n6a-9r| : 
nsoc;), aaivu) "schwanzein, flatter', oaTva, aavviov "aiSoTov' Hes. (-vv- hypocoristic 
doubling); in addition oavvaq ^[}v^p6q\ aavviajv "du idiot, du fool'; also probably oav'\q 
"picket, pole, balk, beam, board'. 

7. /^formations:
```


## [2026-10-15T02:45:03.513Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 86700,86860p POK_full.txt | cut -c1-220; grep -n \"Root / lemma: teuk\\|Root / lemma: tauro\" POK_full.txt"
}
```


### [2026-10-15T02:45:03.897Z] TOOL RESULT

```
7. /^formations: 

Old Indie tura-\n the meaning "strong, rich' (wherefore tuvi- as composition form as e.g. 
K05-p6-q : Ku5i-av£ipa); Old Icelandic A'o/'a "venture, risk', t^oran^ courage, skillfulness ', 
/5o/'/"bulk, mass, lump '; 

gr. Ti:-Tupog " he-goat; billy goat. Satyr'; 



Avestan tuiri- n. " caseous gewordene milk, whey '; gr. aoopoc; "heap' {*tud-r6-s), in 
addition ablaut. *tu-ro- in gr. Tupoc; 'cheese', pou-rupov 'butter'; affiliation also from Old 
Bulgarian tvarog'b 'lac coagulatum' as a lengthened grade form is good possible; compare 
tvorb 'opus, creation ' under tuer-2, 

gr. Tupcb, eine Heroine, probably actually 'die Strotzende, Schwellende'; also lllyrian PN 
Turn, 7"/7/T/s; Venetic PN 7"/7/y/s, gall. VN 7"/7/'o/7es 'Tours', PN /"/v/tc^/t? 'Zurich'; Middle Irish 
PN Torna {* turonjos); 

Latin *turo-s, -/77 'swollen; clump' wird assumed through ob-, re-turd \erstop^e'; turged, - 
ere 'swollen sein, strotzen' perhaps derivative from a "/JA-Zgos 'swelling driving ', intrans. 
GegenstiJck zur class of causative verbs auf -(i)gare; late Latin turio, turg/'o {-g/- probab\Y 
not originally, but verbalized iurj, or support in turgere) 'young twig, branch, stalk, scion, 
shoot'; 

7. a: das word for bull: gr. raupoc;, alb. tarok, Latin taurus, Oscan raupop, Umbrian turuf, 
to/zy'tauros'. Old Prussian /5^/7s 'Bison', Lithuanian fauras6s., Old Church Slavic furh 
'Auerochs' (Trautmann 315, VasmerS, 154), either from Indo Germanic *fduro-s {compare 
Old Indie tum-ra- ' plentiful ' as epithet of Stieres), or because of orientalischen Stierkultes 
with Proto Semitic *tauru{arab. twr) connected with, gall, /an/os (Middle Irish tarb, cymr. 
tarv\/}, venet. PN Tarvisium, probably after Celtic can/os 'deer' transfigured; Old Icelandic 
l=>jdrr, Dutch dial, deur etc., are after Old Icelandic stjorr. Old High German st/or 
unvocalized, deren meaning against from unserem words influenced is (see above Indo 
Germanic *steu-ro-S. 1010); 

doubtful Old English deo^'inflammation, ignition' (*/e^-/r>-'*swelling, lump, growth'?). 

8. s-formations, connected ^\\h the es-stem Old Indie tavas-, Avestan tavah- etc.: 

Das Germanic and Balto Slavic word for ' thousand ': Gothic t^usundii.. Old High 
German thusunt, dusunti. under n., lex Salica thuschunde; Old Saxon thusundig, thusind. 
Old English dusendi. n.. Old Icelandic t^usundi., ^ushund, Push undraf^ {Gem\an\c *Pus- 
hund/We\\r\un6ert', Indo Germanic *tus-RmtTj; 

Lithuanian tukstant/sm., Latvian tukstuots. Old Prussian tus/mtons {Akk. PI.); besides 
Lithuanian *tukstas\n tukstas/san6 tukst/n/s ^tausen6ster'; 

Old Church Slavic tys^sta, ablaut, tysgstai., russ. tysjaca, Serbo-Croatian t/sucaetc. 
{*tu sent/a, *tusontia); 



with the meaning 'Schwa!!, anschwe!!ende Bewegung (a!so seeiisch), Auflauf, tumult ' : 
Old Icelandic t^ausku., t^ausni. "din, fuss, noise, tumult', t^eysa, Aysya "vorwartsstijrmen', 
/^ys-sm. "GetiJmmer, Old High German doson'roar, sough, rustle, rant, roister'. Modern 
High German fosen, Old Icelandic /?/'(9s//''vehemency', Ays//"' rage, fury, gust of wind', nisi. 
Pusuri. PI. "vehemency, Unbeherrschtheit', A'i/s^/775di//'"heftiger person'. Old English 
dyssam. Toser', /77^^e'/7-dy5se "violence, force'; 

with the meaning "swelling eines BliJtenstandes; tussock; heap, hill' etc.: gall, tudos, 
/^ddos "Schichte'? {*tus-fo-, Loth RC 43, 165; different - loanword from Vulgar Latin tostus 
- Whatmough JC stem 1 , 7 ff.), cymr. fuswm. "bundle' ( *teus-t-uo-), bret. tossen, Vannes 
tosten^hWy {*tus-ta), bret. tuchends. {*toust-ien)\ whether Old Irish /t7a//77/77 "hill' from *teus- 
mnl different above 1.; Old High German dosto, tosto^ tussock, tassel ' and "Origanum 
vulgare' (Modern High German Dost, Dosten), Modern High German o'c>s//^"ausgebreitet, 
turgid, swollen '; East Frisian dOst^ tassel ', Norwegian /J5/"tuft, Haarzotte, tassel ', tOsta 
"tuft, knot, bundle, tree with buschiger Krone', isl. A'J5/a"heap, mass'; 

possibly here Old Indie fusa-m. "hem eines Gewandes', whether originally "Ouasten'; 

Latvian /Js/ra "swelling, lump, growth', /Js/^/s "Wassersuchf; /^sA75"wisp, small bundle' 
(could auch sk- derivatives besides Latvian tukt^to swell' sein); Modern High German 
Dosche'bush, umbel, Krauthaupt, bouquet, tassel '; 

ein *fuos-f/-or *fu9S-f/- perhaps in Gothic ga-f^wasfjan ' make strong, tight, firm, certain 
', f^wasf/Pa' certainty ', isl. Pvest, Pvesf/n. " steady parts of meat '. 

9. derivative teuta'{bu\W, mass) people, land'; fe://'o/70-5"Landesherr': 

lllyrian PN Teutq, Teutana, Teuticus, Tsurapot;; Messapic PN deotoha. Gen. deotorras, 
thrak. PN Tauto-medes, Oscan tojFto, touto, Umbrian Akk. /o/a/77 "civitas'; gall. GN 
Teutates {*teuto-tat/s ^Landesvater' to tata, above S. 1056), newer Toutates, Totates, 
Tutates, PN Teutio, Toutius, Tutius, Toutonos, 

Maybe lllyrian TN Taula- Taulant common italic-lllyrian -/- > -/-. 

Old Irish /Ja//7 "people, stem, land', cymr. /Jo'"land', corn, tus. Middle Breton tut, nbret. 
tud^ihe people'; 

Gothic Piuda, Old High German dio1{a) "people'. Old Saxon thiod{a). Old English deod. 
Old Icelandic /^iod "people, people', whereof Old High German diutisc. Modern High 
German otei/Zsc/? (originally "zum eigenem stem orVolk belonging', Weissgerber Deutsch 



as people's name 1953, 261) and Old High German o'/Z//e/7"verstandlich make (as though 
verdeutschen), define, clarify, indicate ', Old English gef^redan ^ubersetzen', Old Icelandic 
Ayda'ausdeuten, signify'; Germanic VN *Theu-dandz, keltisiert TeutonT, ToutonT,{o 
Danish PN Thyte-sysael; Gothic f^/udans^ king' {*teutonos). Old Icelandic t^Jddann, Old 
English deoden. Old Saxon thiodanAs. (Illyrian PN Teutana, gall. Toutonos); 

Latvian /5^/5 'people'. Old Prussian /5^/c»"land', Lithuanian 7"a^/a'0berland, Germany 
', Old Lithuanian (Dauksa) /5i//5 'people'; 

Hittite tuzzi- 'master, mister, Heerlager' {*tut-tf-7). 

References: WP. I 706 ff., WH. II 650 ff., 712 f., 714, 715 f., 718 f., 721, Trautmann 314 f., 
331 f., Vasmer3, 149, 154, 160 f., 161 f.; Krahe Sprache under Vorzeit 65 ff., Mayrhoferl, 
490, 513 f. 
Page(s): 1080-1085 

Root / lemma: ff-ti- (ti)til- 

Meaning: chirping of birds 

Note: barely ursprachlich 

Material: Old Indie tittibha- m. 'Parra jacana'; Latvian titilbis, t/t/'/brte "\Nasser\au^er' , 

Lithuanian tilvikas, titilvikas, /////K/s'Brachhuhn, Schnepfe'; gr. TlTUpi^oo orriTTUpi^co " 

gaggle, cackle, chitchat, talk, snicker (of partridge, game bird, the swallow'); Latin titid, -are 

'chirp, twitter, from sparrow'; Latvian //7e/'sing'. 

References: WP. I 742, WH. II 686, Mayrhofer 1 , 457. 

Page(s): 1 086 

Root / lemma: tieg"- 

Meaning: to retreat in fear 

Material: Old Indie tyajati{= gr. oEpu)) 'verlaftt, stands from etwas back', with /?/■ ' scare, 

frighten, verdrangen', with /7/5-'hinaustreiben, verjagen', participle tyakta-{= gr. a£nT6(;), 

noun agentis tyaktar-{= gr. GsoasnTwp 'Anbeterthe divinity'), Kaus. tyajayati^vmkes 

zuriJcktreten', tyajas-n. 'Verlassenheit' = Avestan i^yajah-, i&yejah-u. ds.; Old Indie 

tyaga-m. 'Hingabe, Freigebigkeit' etc.; 

gr. aspu) (only present and Impf.), oEpopai hom. '(die gods) scheuen', nachhom. '(die 
gods) worship, honour', Gfuioq, '(venerates =) venerable, holy', at^aq,, PI. aspn n. hom. 
'fromme fear, shyness, Ehrfurcht', nachhom. ' holiness, majesty ', hom. OEpaaaaTO 
'scheute ehrfijrchtig', az\xv6c, (*a£(3vo(;) 'admirable, venerable, convex, elevated, holy; 



gravitatisch, einherstolzierend, prunkend', aopsw "tue etwas from mirweg, entferne quick, 
fast, drive out'; intr. 'go eilig, stolziere einher', aopap6(; "rash, hasty, quick, fast; 
hochfahrend, prunkend', oo^aq, -a5o(;f. 'violent, vain', aopn "Pferdeschwanz'. Note: 
common lllyrian g"'- > b-. 

References: WP. I 746, Mayrhofer 1 , 529. 
Page(s): 1 086 

Root / lemma: to-1, ta-, tio- 

Meaning: that, he (demonstr. base) 
86424:Root / lemma: teuk-
```


## [2026-10-15T02:45:06.305Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 86424,86442p POK_full.txt | cut -c1-220; grep -n \"steu-ro\\|staora\" POK_full.txt | head; "
}
```


### [2026-10-15T02:45:06.665Z] TOOL RESULT

```
Root / lemma: teuk- 

Meaning: sprout, seed, offspring 



Material: Old Indie tuc-i. 'Kinder, progeny ' (besides tuj-t ds. with folk etymology 
extension of the Tenuis); tokamu. " progeny, Kinder'; tokman-u. "young stem, sprout', 
Avestan taoxman-n. " seed, sperm, germ, sprout', PI. " kinship'. Old pers. taumat ' family, 
seed, sperm, germ, sprout'; khotansak. tt/man-n. " seed, sperm ', np. turn, afghan. toma^ 
seed, sperm '; Middle High German o'/e/7/e/''grandchild, grandson'. 
References: WP. I 713, VasmerS, 149, Mayrhofer 508, 527; 
See also: perhaps to teu-k- "to swell', above S. 1081 {teu-). 
Page(s): 1 085 

Root / lemma: teu-1, teud- teug- teuk-, teup- 
See also: see above S. 1032 ff. under (s)teu-. 
Page(s): 1 079 

81356:support, steer)', with Old Icelandic staurr, gr. araupoc; (see above) under *steu-ro- : *stau- 
81359:to Old Indie sthura- etc. stellt sich probably Indo Germanic steu-ro- ^buW (and anderes 
81362:Avestan staora-^caW.\e\ Middle Persian stor^ draft animal, steed', Gothic sf/urm. ' bull 
86733:Germanic *steu-ro-S. 1010);
```


## [2026-10-15T02:45:08.127Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 81340,81375p POK_full.txt | cut -c1-220"
}
```


### [2026-10-15T02:45:08.497Z] TOOL RESULT

```
aschw. s/JA'big, large' (besides stor, see above), s/j?/'5s'brag'. Middle Low German stur 
'big, large, strong, heavy; storrisch, coarse, unfriendly' (compare Old Indie ni-sthura- 
'rough, hard, coarse', /7/-S//7 J/7/7- 'coarse, raw'). Old Icelandic s/J/'a'DiJsterheit', Vb. ' 
grieving sein' (nschw. stura ' rigid hinsehen' in the meaning after the family of Modern High 
German s//e/'e/7umgeandert), zero grade Old High German s//^/7 "strong, stately, stout, 
proud'; 

with other meaning: Old High German stiura. Middle High German st/ure'pa6, rudder, 
helm, UnterstiJtzung, tax'. Modern High German Steueri. and (from dem Low German) n.. 
Old English steori. ' rudder, helm ', Old Icelandic styriu. ' rudder, helm ', Middle Low 
German stur(e)v\. ' rudder, helm ', f. n. 'Regierung; help, Gegenwehr', f. 'UnterstiJtzung', 
Gothic ^s-sZ/^/ie/'Zugellosigkeit', Middle Low German unsfure6s., Gothic stiurjan 
'feststellen, affirm ', Modern High German zur Steuer der Wahrheit, Old Icelandic s/y/'a'ein 
ship steuern; regieren'. Old English stTeran6s., Old High German sf/urren^ prop, support, 
steuern, steer'; probably originally 'picket, pole, rudder, helm (secondary: with it prop, 
support, steer)', with Old Icelandic staurr, gr. araupoc; (see above) under *steu-ro- : *stau- 
/c- compatible, das from *st(h)au-x\o\ quite apart, separated become could; 

to Old Indie sthura- etc. stellt sich probably Indo Germanic steu-ro- ^buW (and anderes 
cattle)': 

Avestan staora-^caW.\e\ Middle Persian stor^ draft animal, steed', Gothic sf/urm. ' bull 
calf, bull' (after W. Schuize Kl. Schr. 483 = Old Indie sthavira-); Old High German stior, Old 
English steor. Old Icelandic sZ/o/r (besides t^jori) 'bull'. 

References: WP. II 603 ff., WH. I 343 f., 705 f., Trautmann 280 ff., Vasmer 3, 2 ff. 



Page(s): 1004-1010 



Root / lemma: steb(hj- and steb(h)-. stdo"^-, nasalized stemb(h)-, step- {a\so step-?), 
nasalized stemp-, nominal stdo'^o-s, stemb(h)ro-s, stomb(h)o-s
```


## [2026-10-15T02:45:12.135Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^teu\\|tauro-\\|^steu\\|teuk\\|tum-\\b\" AHD_watkins1985.txt | head -30"
}
```


### [2026-10-15T02:45:12.617Z] TOOL RESULT

```
201:tauro-. Bull. Derivative of sta-, but an in- dependent word in Indo-European.
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
999:nare, to make firm, establish (dé-, thoroughly; see de-): DESTINE; b. Latin obstindre, to set one’s mind on, persist (ob-, on; see epi): OBSTINATE. 8. Suffixed form *séa-tu- in Latin status, manner, position, condition, attitude: STATE, STATISTICS, STATUS. 9. Suffixed form *sto-dhlo- in Latin stabulum, standing place: STABLE. 10. Suffixed form *si-dhli- in Latin stabilis, standing firm: ESTAB- LISH, STABLE!. 11. Suffixed form *sf-td- in Greek -statés, one that causes to stand, a standing: -sTAT; ENSTATITE. III. Zero-grade form *st-, *st()- (before vowels). 1. Reduplicated form *si-sio)- in: a. Latin sis- tere, to set, place, stop, stand: ASSIST, CONSIST, DESIST, EXIST, INSIST, INTERSTICE, PERSIST, RESIST, SUBSIST; b. Greek histanai (aorist stanai), to set, place: APOSTASY, CATASTASIS, DIASTASIS, ECSTASY, EPISTASIS, EPISTEMOL- OGY, METASTASIS, PROSTATE, SYSTEM; Cc. Greek histos, web, tissue ( < “that which is set up”): HISTO-; HISTIO- cyTE. 2. Compound form *iri-st-i-, “third person stand- ing by” (see trei-). 3. Compound form *por-st-i-, “that which stands before” (*por-, before, forth; see per’), in Latin postis, post: PosT!. 4. Suffixed form *st-o- in compound *upo-st-o-, “one who stands under” (see upo). IV. Extended root *std@u- (< *staau-), becoming *stau- before consonants, *stdw- before vowels; basic meaning “stout-standing, strong.”’ 1. Suffixed extended form *staw-d in Germanic *st6w6 in Old English stéw, place: stow. 2. Probable o-grade suffixed extended form *stow-yad in Greek stoa, porch: STOA, STOIC. 3. Suffixed extended form *stau-ro- in: a. (i) Latin instaurdre, to restore, set upright again (in-, on; see en): STORE; INSTAURATION (ii) Latin restaurdre, to restore, rebuild (re-, anew, again; see re-): RESTORE; b. Greek stauros, cross, post, stake: STAUROLITE. 4. Variant *tau-ro-, bull (see tauro-). V. Zero-grade extended root stii- (< *stua-). Suffixed form “*sti-lo- in Greek stulos, pillar: STYLITE; AMPHISTYLAR, ASTYLAR, EPISTYLE, HYPOSTYLE, PERI- STYLE, PROSTYLE, STYLOBATE. VI. Secondary full-grade form *steua-. Suffixed form *steua-ro- in Sanskrit stha- vira-, thick, stout, old: THERAVADA. VII. Variant zero-grade extended root *stu-. Suffixed form *stu-t- in Old English stuthu, studu, post, prop: STUD'. VIII. Sec- ondary full-grade form *steu-. 1. Suffixed form *steu-raé in Germanic *steur6, “a steering,” in Old English stéor, a steering: STARBOARD. 2. Germanic denominative *steur- Jan in: a. Old English stieran, to steer: STEER}; b. Old Norse styra, to steer, with its derivative stjérn, a rudder, a steering, akin to the possible source of Middle English sterne, stern of a boat: STERN?. 3. Suffixed form *steu-ro-, a larger domestic animal, in Germanic *steu- raz, ox, in Old English stéor, steer: STEER?. 4. Probably Germanic diminutive *steur-ika- in Old English stirc, stierc, calf: sTIRK. See stak-. [Pok. std- 1004.]
1025:steu(8)-
1069:tauro-. Bull. Derivative of sta-, but an independent word in Indo-European. Greek tauros (> Latin taurus), bull:
1084:teu-
1086:teu-. To pay attention to, turn to. 1. O-grade form *tou- in Germanic *thau- in Old English théaw, usage, custom (< “observance”): THEW. 2. Suffixed zero-grade form *tu-é- in Latin tuéri, to look at, watch, protect: TUITION, TUTOR; INTUITION. [Pok. 2. teu- 1079.]
1087:teue-. Also teu-. To swell. 1. Extended form *teuk- in Germanic *theuham, “the swollen or fat part of the leg,” thigh, in Old English théoh, thigh: THIGH. 2. Extended form *tis- in Germanic compound *thiis-hundi-, “swollen hundred,” thousand (*hundi-, hundred; see dekm), in Old English thisend, thousand: THOUSAND. 3. Suffixed zero-grade form *tu-l- probably in Germanic *thul- in Old English thol(l), oar pin, oarlock (< “a swelling”): THOLE PIN. 4. Extended zero-grade form *tiim- in: a. Germanic *thimoén- in Old English thima, thumb (< “the thick finger”): THIMBLE, THUMB; b. suffixed (stative) form *tum-é- in Latin tumére, to swell, be swollen, be proud: TUMESCENT, TUMID, TUMOR; DETUMESCENCE, INTU- MESCE, TUMEFACIENT, TUMEFY; C. suffixed form *tum- olo- in Latin tumulus, raised heap of earth, mound: TUMULUS. 5. Extended lengthened zero-grade form *tibh- in Latin tiber, lump, swelling: TRUFFLE, TUBER; PROTUBERATE. 6. Suffixed zero-grade form *tu-r-yo- in Greek turos, cheese (< ‘“‘a swelling,” “coagulating”’): BUTTER, TYROSINE, TYROTHRICIN. 7. Suffixed variant form *tw6-ro- in Greek sdros, heap, pile: SORITES, SORUS. 8. Suffixed variant form *twd-mn, in Greek sdma, body (< “a swelling,” “stocky form”): SOMA, SOMATO-, -SOME?; PROSOMA. 9. Suffixed zero-grade form *twa-wo- in Greek saos, sds, safe, healthy (< “swollen,” “strong”), with derivative verb sdzein, to save, rescue: CREOSOTE, SOTE- RIOLOGY. 10. Perhaps nasalized extended form *tu-m-b(h)- (or extended zero-grade form *tum-) in Greek tumbos, barrow, tomb: TOMB. [Pok. téu- 1080.]
1088:teuta-. Tribe. 1. Germanic *theudd-, people, with deriva- tive *theudiskaz, of the people, in Middle Dutch duutsch, German, of the Germans or Teutons: DuTcH; PLaATT- DEUTSCH. 2. Suffixed form ‘*teut-onds, “they of the tribe,” in Germanic tribal name *theudanéz, borrowed via Celtic into Latin as Teuténi, the Teutons: TEUTON. 3. Possibly Latin tétus, all, whole (? < “of the whole tribe”): TOTAL, TUTTI; FACTOTUM, TEETOTUM. [In Pok. téu- 1080.]
2342:TASTE tag- TATTOO! tap- TAURINE! tauro- TAURINE? tauro- TAUROCHOLIC ACID tauro- Taurus _tauro- TAUTO- to-
2397:TOP2 tap- TOPOGRAPHY gerbh- TORCH terkw- TOREADOR tauro- TORERO tauro- TOREUTICS tere-1 TORMENT terkw- TORNADO (s)tene- TORPEDO ster-1 TORPID ster-1 TORPOR ster-1
```


## [2026-10-15T02:45:14.438Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1069p AHD_watkins1985.txt; sed -n 201p AHD_watkins1985.txt | cut -c1-600"
}
```


### [2026-10-15T02:45:14.870Z] TOOL RESULT

```
tauro-. Bull. Derivative of sta-, but an independent word in Indo-European. Greek tauros (> Latin taurus), bull:
tauro-. Bull. Derivative of sta-, but an in- dependent word in Indo-European.
```


## [2026-10-15T02:45:19.865Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n \"tauro\\|Tumaspa\\|taoxman\\|tauma\" WLD_Bd1_pages.txt | head -20; grep -n \"staora\\|tauro\" WLD_Bd2_pages.txt | head"
}
```


### [2026-10-15T02:45:20.206Z] TOOL RESULT

```
66640:tauman- n. „Verm6gen, Kraft, Macht";
66775:lumaspana- „von Tumaspa-, d. h. einem, dessen Rosse feist sind, stammend“
67083:woraus J. Schmidt Urh. 6, Kretschmer KZ. 31, 448 * tauros durch «-Epen-
67345:Gerstenhalm“, tokma-h „junger Halm, SchoBling“, av. taoxman- n. „Iveim,
67346:Same; PI. Yerwandtschaft“, ap. tauma f. (s. dazu Bthl. Wb. 623f. m. Lit.)
73850:„Zaum" (germ. *tauma- aus *tau^-ma~, Grassmann KZ. 12, 133, erweist
25560:mere, instauro“, lastem „Erle“), nach Liden IP. 18, 4S7f. (auch Lewy KZ.
35154:(der Huer- nicht iiberzeugend als '^stuer- mit ^stauro- ,^oxavo6g^^ usw. unter
40357:Hirt Abl. 106, Reichelt KZ. 39, 14, 43flP., 64, 70, Yf. LEWb.^ u. restauro,
40463:   av. staora- „Gro 6 vieh“, mp. st^ ,.Zugtier, Ro 6 ‘^, zigeun. Hurno „Stier‘‘
40474:nung des Stieres idg. "^tauros.
```


## [2026-10-15T02:45:23.672Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 67070,67095p WLD_Bd1_pages.txt; sed -n 40455,40478p WLD_Bd2_pages.txt; awk 'NR<66640 && /\\[pdf page/ {l=$0} NR==66640{print l}' WLD_Bd1_pages.txt; awk 'NR<67083 && /\\[pdf page/ {l=$0} NR==67083{print l}' WLD_Bd1_pages.txt; awk 'NR<40463 && /\\[pdf page/ {l=$0} NR==40463{print l}' WLD_Bd2_pages.txt; awk 'NR<67345 && /\\[pdf page/ {l=$0} NR==67345{print l}' WLD_Bd1_pages.txt; sed -n 66630,66645p WLD_Bd1_pages.txt"
}
```


### [2026-10-15T02:45:24.331Z] TOOL RESULT

```
tragung), lat. taurus „Stier“, osk. zavgofi , umbr. torn turuf a. pi., apr. tau-   ,


ris „ Wisent“, lit. taiiras „Auerochs“, abg. tun, „Auerochs“ (Trautmann Bsl.
"Wb. 315)  aisl. piorr, ndl. limburg. deur sind nach stiorr, stior umvokalisiert

(Brgm. II 2 1, 353; s. iiber letztere, etymologisch verschiedene Gruppp u. sta-
„stehn ); gall, tarvos, mir. tarb cymr. tarw sind nach Yendryes Msl. 12, 40
           l<
                                               ,


nach *uerua (recte *uerbha !) „Kuh“ (mir. ferb) umgestellt (oder idg. *taruos,
woraus J. Schmidt Urh. 6, Kretschmer KZ. 31, 448 * tauros durch «-Epen-
these gewinnen wollten?). Die Zuteilung dieser Gruppe zu teu- „schwellen“
setzt voraus, dati Ubereinstimmung mit ursemit. tauru (aram. tor, hebr.
sor ) durch Entlehnung ins Semitische, nicht umgekehrt (nach J. Schmidt
aaO., Lewy Fremdw. 4) durch solche aus dem Sem. ins Idg. zu erkliiren ist.
S. iiber diese Stiernamen Curtius 218, Brugmann IF. 6, 98, Yf. LEWb. s. v.,
                                                                          2


Franck- van Wijk u. stier,    Feist  Kult. 411.
   Gr. ocogog „Haufen, bes. Getreidehaufen“ ( tuo-ros Ablautstufe wie in               ,


Steuerruder (sekundar: damit stiitzen, lenken)“ und ware mit anord, staurr^
gr. oiavQog (s. o.) unter ^steu-ro--: stdu-ro- vereinbar, das der Bed. halber
von stQi)aii- nicht wohl ganz getrennt werden konnte; andrerseits kann
^stiura- auch idg. steu-ra-^ also nur eine Parallelbildung zu dem auch auf
staio- beziehbaren ^stdu-ro- sein. Ersteres scheint das richtige zu sein, da
die Ablautstufe stdu- bei stdu- auBerhalb von "^stoura- nicht                    vorkommt.
  Zu   ai.     sthUrd-h usw. stellt sich     wohl    (trotz    Lommel KZ. 46, 53)         idg.
*steu-ro- „Stier (und anderes GroBvieh)“;
   av. staora- „Gro 6 vieh“, mp. st^ ,.Zugtier, Ro 6 ‘^, zigeun. Hurno „Stier‘‘
(wenn nicht dt. Lw. nach Lommel aaO.; ai. sthurd-h „Stier“ ist unbelegt),
got. stkira- n. m. „Stierkalb, Stier“ (n. sg. stiur nach Kock KZ. 36, 5 S 1                   ,

Bgm. II ^ 1 353 die Keutralform; trotz Schulze KZ. 29, 271 nicht wegen
               ,


des mangelnden Nominativs-s= ai.                 ahd. stior^ ags. steor^ aisl.
stiorr „Stier“.
  Davon verschieden die zu "^teu- „schwellen“ zu stellende andere Bezeich-
nung des Stieres idg. "^tauros.
  Es scheinen auch kons. Erweiterungen der M-Basis mit der Bed. „steif
emporstehen‘‘ anerkannt werden zu mussen; aber sie konvergieren in der
Bed, mehrfach mit zugehorigen der Wz. steti-{g- usw. s. d.) „schlagen,
stoBen^, indem z. B. Ausdriicke fur „Stock, Pfahl u. dgl.“ einerseits als




                                       instr. tavasti „Kraft, Starke" (s. dazu
                                                          ,


J.    Schmidt   136 f.), tavasvant- „kraftig“, tavasya-m „Tatkraft, Mut",
                      PI.
tavismant- „stark, machtig", tavisd-h „stark“, tavisl „Kraft, Ungestiim, Mut",
tavis-ya „Ungestiim, Heftigkeit"; tuvi- in Zs. „sehr, machtig", tuvistama-h
„der starkste"; tuya-li „stark, geschwind";
  av. tav- „verin6gen“, tavah- n. „Macht, Kraft", tdvisl „Korperkraft"; ap.
tauman- n. „Verm6gen, Kraft, Macht";
  arm. fiqf (tfi-pho-, s. u.; Petersson KZ. 47, 248, wo kaum richtig auch
tav „thick, bushy; woolly, shaggy" aus *tduo- gedeutet wird);
  gr. Till'd? der Name des geilen Frevlers wider die Leto (Lit. bei Solm-
sen IF. 30, 32);
      gr. Tavg ' ueyag, noXvg Hes.          (
```


## [2026-10-15T02:45:28.191Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in \"taoxman\" \"staora\" \"tumasp\\|tumaspa\" \"tavah\" \"taxma\" \"tavant\\|tavaṇt\"; do echo \"== $p\"; grep -n -i \"$p\" BRT.txt | head -6; done"
}
```


### [2026-10-15T02:45:28.807Z] TOOL RESULT

```
== taoxman
11787:•  j.  taoxman-  n.  i)  'Same,  Keim':  upa
== staora
3118:•  j.  ajryÖ.staora-  Adj.  'worauf  ein  Stück I  Grossvieh  erster  Qualität  (alsEusse)  steht" ": 'ye  .  .   ainim    dahm>m  Jatnti  .  .  'rim    vd
8349:—  ,  .  maiüatam  frä%W3r?sat  . .  aAurS  . . 'ri  AarqmYtio.$o;  —  W-riy  däraya*va*um xlaya'hiyam  D.7(?);  —  I'  °riy  *abistam{^.) upariyayam  Bh.  4.i3(?).  [J)  auf  die Frage  wohin?:  yS  vaslnm  upanhanzaiti 'ri  aitim  irislim  V.Ä23;  5,61;  —  avqm vanqm  .  .  yqm  °ri  urvaranqm  .  .  taoxma niäayaj  Yt  /2. 17.  b)  'Über  —  hin',  mit Akk.  oder  Instr.:  mana  raya  . .  pasvasca staoraü  °ri  zqm  7'ÜarpnlaYt.$.8^;  ig.^4; — yais  °rf  äya  stma  gaobTs  *fyeintiY.i2. 3.  c)  "über  —  hinaus',  mit  Akk.  oder Instr.:  *uzdatum  (sd.)  hl  .  .  ksrmaot  'ri spamm  'ri  raohm  "ri  vihrk^m  "einen  Auf- bau . .  über  den  Hund  hinaus  *'  , ."  V.
11788:avqm  vanqm  .  .  yH  vaoce  vlsplMs  (sd.) nqma  yqm  upatri  urvaranqm  vTspanqm 'ma  nilayat  Yt/2, 17;  —  Ää^ra  'ma upa.iara  pasvqmca  staoranqmca  mafyä- nqmca  sünqmca  vayqmca  ä'^rqnu'a  V. 2.25;  37',  28',  30,  2)  Plur.  'Verwandt- schaft': äa^  yat  kqmat  vä  'manqm  para.- irihyäti  ya%a  ainyö.vanna  ainyS-lkagsa (sd.)  V./2.  21.
12015:Akt.;  absolut  '(dazu)  im  Stand,  in  der Lage  sein,  (es)  vennögcn':^a; /aj/a«''  aife mazdayasna  a^/e(Sp.  14  o.)  pasvB  staorala .  .  frabaraygn  yezi  ndil  lavqn^'>  .  .  alte [pasvS  slaeräca\  anyqm  h!  avarttqm  .  . frabaraym  V. 5. 39;  —  yezi  tavqn'>  alte mazdayasna  . .  tutuxsva  (sd.)  yai  ndit V.  6. 5 1 ;  — yavat  (sd.) . .  tava^ä isäua  Y.50.  ii;  — yavat  wa/(sd.)  tavacä Y.26'.4.        a)   3SP£A.  ^es   ist   möglich';
14248:•  j.  drvö.staora-  Adj.  (fem.  'ra-)  'das Grossvieh  gesund  erhaltend':  drväspqm  .. drvS.pasvqm  °rqm  Ytp.  r.
14871:•  j.  patarvta-  Adj.  'im  Flug  hegTiSeii,i  nipai'.yante(s±)  Äqm  vä 'ti  stairi/Aqrri  vä fliegend':  äsyajgia  (sd.)  vayazibya  °taiibya\°ti  bartzi^  V . ^.  ^i .  b)  auf  die  Frage ". ,  als  ein  paar  fliegende  Vögel"  Y.  57. 28;  i  wo?:  talam  vantanhS . .  gätiis  'ti  ^ätjfante — pasubya  staoralibya  vayaeibya 'taäbya^^  (S'p.  i^^  n.)  Ytij.io;  —  ya^/a  argAaJ yS  parmJnS  (sd.)  fravazänte  "mit  Klein-  1  bartsnul  'ti  gairinqm  V.  2.  23";  Y.^.  26, undOrossviehundmittliegenden Vägeln, .. "1 /0.3; —  :i^armö  baxlmli  zqm  'ti  akura- YtJO.119.  \Vttqm   Yt.6.1,  7.3;  jp.48,'$o,  Y. 13.4g,
== tumasp\|tumaspa
== tavah
3318:•  j.  aSu-tavah-  m.  Name  eines  Bergs oder  Gebirgs:  ahma^  kam  garayB  fraoxs- yqn  . .  °vasca  Yt,  if).  6.
7728:•  j.  9r9zu.stavah-  Adj.  'fingerdick':  ast^m .  .  'rawhim  (ASm.  statt  ASn.)  V.  (7.i6.
12029:•  j.  tavah-  n.  'Vermögen,  Kraft,  Macht' KompE.  —  VgL  trvUi:  —  Zum  V.   ^lav-.  —
14944:/.  132  und  Pü.  —  Pü.  (lu  l):  patirak  raaiihük, (zu  a):  löäin,  erl.:  fa  ifästaij  i.  zu  A%d.. ■  j.   paiti.tavah-   Adj.  'seine  Kraft   da- gegen   einsetzend,  Widerstand  erhebend': nsit  'vä  iavaiti  (sd.)  Yt.  JO.  48.
16468:•  j.  bae'arazu.stavah-  Adj.  'zweifinger- dick': as/?m  . .  'vatafum  (ASm.  als  n.)  vä bipTDSU.masargfDm  vS  V,  6'.  18.
22994:•  j.  varasö.stavah-  Adj.  (auch  fem.)  'von der  Breite,  Dicke  eines  Haars':    °vanA?m
== taxma
190:Die  angeführten  Texte  bringen  ausserordentlich  zahlreiche  Wiederholungen. Und  zwar  sind  entweder  zwei  oder  mehr  Stellen  einander  völlig  gleich  oder  sie unterscheiden  sich  nur  in  untergeordneten  —  d.  h.  für  das  Wörterbuch  wenigstens untei^e ordneten  —  Stücken.  Als  Beispiel  für  die  erste  Art  von  Wiederholungen mögen  dienen:  Y.  65.  2-5  —  Yt.  3.  2-5;  Yt.  5.  10  =  12,  14,  16,  20  (usw.);  Yt. 5. 19  =  23,  27,  35,  39  (usw.);  Yt.  JO.  98  =  135;  Yt.  j^.  15  (von  hü  bis  taxmahe')  ^ Yt.  10.  70,  127;  Y.  57.  25  (von  akeca  an)  —  Yt.  10.  93  usw.  —  Die  Wiederholungen der  zweiten  Art  zerfallen  in  verschiedene  Gruppen:  Yt io.  103  wiederholt  sich  von yS  hantaia  an  wörtlich  in  Y.57.  isfl,  nur  dass  hier  das  ca  hinter  har>ta  fehlt; irgend  ein  Grund  für  die  Abweichung  ist  nicht  vorhanden.  Yt. /o.  94  (^=  114I und  Y.57. 26  stimmen  völlig  lusammen,  nur  dass  auf  die  Eingangsworte  aäa  nS tum  dort  der  Vokativ  mikira  vouru.gaoyaoite,  hier  aber  traosa  afya  huraöha  folgt; die  Gebetsformel  ist  die  selbe,  aber  die  Adresse  ist  verschieden.  Ähnlich  steht es  mit  den  vier  in  Yljo.  igof.  enthaltenen  Stücken,  die  von  vier  Waffenarten Mihras  durchaus  das  Gleiche  aussagen;  nur  eben  die  Namen  der  Waffe,  sowie deren  Beiwörter  machen  die  Verschiedenheit  der  Stücke  aus.  Besonders  zahlreich findet  sich  diese  Art  der  Wiederholung  im  Viälvdäi  {Vendidad);  z.B.  unterscheiden sich  in  dem  Kapitel  über  die  Verträge  (V.  4)  die  Abschnitte  6  bis  10  und  ander- seits II  bis  16  nur  durch  den  Namen  des  Vertrags  und  der  Zahl  in  der  Buss- bestimmung. Femer  haben  V.p,  53,  54,  55  und  S7  '^'on  üäca  an  den  gleichen Wortlaut,  nur  dass  das  dreimalige  para  von  53  in  54  durch  kaha,  in  55  durch nöü,  in  57  durch  pascalta  ersetzt  ist  In  den  liturgischen  Teilen  des  Yasna  wieder sind  grosse  Stücke  bis  auf  die  Eingangs-  oder  Schlussformel  gleichlautend.  So decken  sich  Y,  i.  3  ff.  und  5.  5  ff.,  4. 8  ff.,  7.  5  ff.  vollständig  bis  auf  die  Eingangs- worte, die  zu  Y.  1:  nivaiöayemi  hankärayemi,  zu  Y.^:  äyese yeSH,  zu  Y.  4:  Hat  dis äva^ayamahl,  zu  Y.  7:  alaya  daöami  lauten,  während  anderseits  Y.  2.  äff.  und 6.\S.  nur  darin  auseinandergehen,  dass  hier  (Y.  6)  jeder  Abschnitt  mit  yatamatde endet,  dort  (Y.  4)  jeder  mit  ahmya  zaohre  bar>smanaica  eingeleitet  und  mit  äyese yeiti  geschlossen  wird.
4754:—  yal:iä  ro  data  °/il  (VP.)  spsntä  a^iä na  >räzäa?n  Y.5#.  5;  II.  iZ,  14.  i,  42.1, • — ■  mai^amnt  . .  yat  ksrmlun  "la  (NS.) sp>nta  vispe  hazaesaYLio.$i;  7.3',  /0.92, y.ga,  Y. 57.^23,  60.6;  —  /ml  '/ä  (NP.) spmtä  gaiia  giurvain  Y.2S.0;  Ny.l.i, VyL^o;- —  spmtsttg  °s3ng  yava^yff  yavaSsvB Y.,J.')-3;  4-A\  —  °^^  sptrüa  huxiäi:ra hmfmhs  (Stverz.)  Vr. ;/.  12;  usw.;  —  -sS spints  vatihali  srlräi^  namqn  äebaya  Y. /  5. 1 ;  Vr.  6.1;  —  vlspqscä  'iq  spintq  yasa- maidsY.42.()\  —  °h  spinlS alaonam  yasa- maideY.yi.2,  G.  2. 6  (wo  'sJtca);''*  — 'sanqm  sp)ntanqm  xialtanqm  vinzidsi- %ranqm  Ötnzatqm  aiwyämanqm  taxmanqm ähuiryanqm  ySi  aihy^anhs  alwvanB  ysi hapta  iam^.manavAö.. Yt  lj.82f.;Y.j. 4, 20,3;  — y3i  hapta  'sä  spmta  Yt.2.3;  — ape  °ianam  spmtanqm  dähXtn  Y./9.8;  Yt. ;^.  8 1 ' ;  —  vankubyS  yazataiibyS  yat  'laii- byS  spmtaHbys  Vr. 8.\;  ff. 4, 13. \,Yt.4.y,
5485:•  j.,  g.  aradra-  Adj,  (fem.  'rJ-)  'getreu, 'verlässig':  'rS  '^wävqs(sd.)  ÄitzSntuü  sfmtö mazdä  Y. 4:_j.3;  46.^;  — fravasayB..  °rä taxmä  *at>javuAai/i/ \l.  ij.  $2;  75;  — mihrgm  . .  y5  äsunqtn  äsus  yS  'ranqm  °rö y3  taxmanqm  taxmS  Yt.  70. 65.  a)  mit DaL:  kuirä  tsi  °rä  masdä  ysi..  caxrayö' (sd.)  "ob  sie  wohl  dir  getreu  sind,  die  . ," Y._j4-7-  A)  insbes. 'dem  Glauben  treu, gläubig,  fromm':  firasaosträ  air3  tu  'r.lis idi  hvB^S  täis  yitig  . .  "o  Fr.Hv.,  dahin geh  mit  diesen  Frommen,  denen  . ."  Y. 4'j^i6;  —  kä  iw'ffi  a/a  äk,i  (sd.)  'ring isyl  Y.  4S.  8;  S*}.  4;  —  fatrijasai  .  .  at vä  aia  "rahyacä  mmankä  "..und  vor  euch, o  Asa,  auch  mit  dem  Gebet  des  Frommen" Y.50.8;  —  da^at  ahrnili  tat..  arfdvJ . . 'räi  yavmiini  jatoyantäi  da^ris  ayaphm Ytj.ig;  13a,  /5.1,  21.
5555:•)    Über   die   Bedeutung   des  Gotls   ist   den    t'isjie  °va   Vlspe  taxma   .  .  kave  HK.1Q.1z; ,i'j5i sehen  Teilen  nichu  Klnies  lu  entnehmen;   —    'v3  as.vancS   kava    usa  Yt5.45;   —
5713:idn^taxma^  näma"  °tiyi^    Bh.^.  i  /p.g,  Yt  /_y.  28;  —  öarjimrS  ^avaühe  'htS
5799:•  j.  asta'va-  Adj.  'mit  einem  Knochen Teisehcn';  °v3  vä  taxmahe  mirr/ake pars- nai'SvS..  "wer  einen  Knochen  des  starken Vogels  oder  eine  Feder  (als  Amulet)  trägt .." YL/4.3(S.
== tavant\|tavaṇt
2530:17  ^aeta-  II 2  z  b  —  aetavant-  18
2546:PS.:   A.  dm  dmi  ..fa  di  nants.   ~  7>  Hd».  I  *  J-  aetavato   Adv.  :  S.   amraiil: aiiaya;  Pü.i  öiän  tc.  *  j,  actavaitya  Adv.:  s.  aitavant-.
2558:17  Jaeta-  U  2  a  b  —  aetavant-  i8
2571:fBgt  /  tä  ..  hiniu.  —  ')  Pü.:  ilän.  —  3)  Pü.:        afun    Kurinamen   daiü    fortsetzen;    doch  s. aetavatö  Adv. :  s.  aetavant-
2574:aiiaya;  Pü.:  öisn  it.  •  j.  actavaltya  Adv,:  s.  aitavant-.
2577:1 9  aetavant-  —  aedrya-.  lo
```


## [2026-10-15T02:45:33.247Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"üspana\\|^.\\{0,40\\}tumä\\|tumasp\\|tumäsp\" BRT.txt | head -5; grep -n -o -i \".\\{60\\}ustav.\\{60\\}\" BRT.txt | head -5; grep -n -i \"stör\\|stor \" PHD_mackenzie.txt | head -10; grep -n -i \"stōh\\|stoh\\b\\|tōhm\\|tohm\\|tuwān\\|tuvān\\|tund\\b\" PHD_mackenzie.txt | head -10"
}
```


### [2026-10-15T02:45:36.418Z] TOOL RESULT

```
8597:iumüspanahe  asaond  "des  ^.,  Nachkommens
12327:•  j.  tumäspana-  palr.  Adj.  'von  Tumospa  '> stammend,  dessen  Nachkomme*:  usavahe -nahe  asaonS  Yt/y.  131.
20265:Pü.:  martumän  iai,   erl.:  pa  dälaslärämaitdän 'von  solchen  mit  richterlicher  Gewalt'.
23915:Pü.  er]. :  iuia  ramak  i  martumän  u  gdsfandän  ys   narqm   'ii](LS.yii  ianvS  baoxtänm   da-
27899:Pü. :  äSil  bavit  ligin  surr  S  martumän  ffofä- mU.  —  >)  Wertloi.  —  »)  Vgl  VyL  4.
9086:"■-  Snbsl'Wohl,Heil,Grack':  iäl.  i,  rf«,.,,,,,, .  j.  ■ustaviiti-  f.  Name  eines  Flusses,  I !?  .f*""' .!'™  '"°"'  
20678:atim  nimravanta*^  vUpä  . . damqn  YtJj,  93;  —  iurva)  ustavaitlin gä^qm  srävayö  uitatatim  nimraomnä H.  2. 2 ;  Y.  
29826:Schluss,  N.46;|.3.WM  yavat  tacar>m  "ein  H.  zweimal —  ustavaityä  vä  sp^ntäMainySiif  va  hmis\  (genommen  ist)  sovi
4698:stOr [stwl] trustee, curator, guardian.
5951:ancestor niyiig.                          armed zenig.
625:       tohm(ag) [twhm(k') 1M twhm, -g, N tUXlll, -a] ...
2783: --tOhmag [-twhmk ] relative, relation.
4918:tan-tOhmag [tn'twhmk ] (sap) of plants.
5005: tohmag [twhmk I M twhmg, N tuxma] seed; stock, family.
5023:tund [twnd IN .......] sharp, violent.
5131:wadl-tohm [wttwhm] = wad-gohr.
5161: - i was-tohmag: the Tree of Many Seeds.
6843:ill-born wad-gohr I -tohm.               increasing abzonig.
6992:limbo hammistagan.                       low-born wad-gohr I -tohm.
7421:relation, relative hamtohmag, xwes-         padiran(en)idan.
```


## [2026-10-15T02:45:40.267Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *st[oO0]r\\|st[oO]h\\|tuw[aA]n\\|tav[aA]n\\|taw[aA]n\" PHD_mackenzie.txt | head -12; grep -n -i \"tahm\\|tahmasp\" PHD_mackenzie.txt | head"
}
```


### [2026-10-15T02:45:40.752Z] TOOL RESULT

```
35:stored in a retrieval system, or transmitted, in any form or by any means,
1970:den-astawan [dyn)stwb)n ], den-burdar [dynbwlel] believing, faithful.
3861:ostigan [)wstyk)n' I M hwstyg)n, N ustuwan?] firm, strong, sure, reliable.
4698:stOr [stwl] trustee, curator, guardian.
4957:tawan [t)(d)w)n IN,.....,] compensation, obligation.
5030:tuwAn [twb'n 1M tw)n, N -] might, power.
5879:  ih, tuwanigih; extent of one's ,.,.,    active kardar, karig.
5880:  tuwan-saman.                            activity kardarih, karigih.
5882:able abzaromand, sayendag, tuwanag,       admonish awenidan.
5883:  tuwanig.                                adoration yasn; v. worship.
6052:belief astawanih, wabar, wurroyisn,         blazing waxsendag.
6055:believing den-astawan I -burdar,            blessed farrox, hufraward.
623:add tahm !thm I =M, N "'] strong, brave.
4663:stahm [st/zm I N sitam] power, oppression.
4666:stambag [sthmbh l (-/z- < stahm) I M <stmbg, N sitamba] oppressive;
7190:number mareag), sag.                       pazd, stahm, stahrn(ag)ih, starn-
7192:nurse, (wet·) dayag.                   oppressive stahmag, starnbag.
7307:   stahm, tuwiin, zor.                         produce (n.) bar.
7707:   wand, saxt, stabr, stahmag, sur,        supplication liibag, liibakkarih.
8899:sturg              ~\lU'              stahm                      <~
8902:storbiin         \~~,teV              stahmih                  ~te»
8903:stard                 ,~,tUJ          stahmagih               A(J~te.»
```


## [2026-10-15T02:45:45.049Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4690,4702p PHD_mackenzie.txt; grep -n -i \"tired\\|weary\" PHD_mackenzie.txt | head; grep -n \"tuwan\\|tuwān\\|tōhm\\|stōr\\|stōh\\|tahm\\b\" NYB_vol2_glossary.txt | head -12"
}
```


### [2026-10-15T02:45:45.501Z] TOOL RESULT

```
·stoi [stwl] the fourth morning after death.
stowenidan, stowen- [stwbyn-ytn'] defeat, overcome.
stowih, v. stO.
stQdan, stiy- [stwtn l , st)d- I M Cstwd, Cst'y_, N sit""] praise.
 ""lin: praise.
 ""IAnig: praiseworthy.
stiin(ag)                                                        lab-
stOn(ag) [stwn(k) , I M (stwn, N sutUn] colwnn, pillar, mast.
stOr [stwl] trustee, curator, guardian.
 -ih: trusteeship.
sturg, [stwlg I N suturg] fierce, contentious; gross, coarse.
sud [swtl I M swd, N ~] use, profit, advantage.
sudab [st)j.i I N -] rue.
3437:mAnda~ [m)ndh I M m)ndg, N ~a] tired; remiss; fault, sin.
3439:  -ih: tiredness.
7795:tired mandag.                               tohmag.
7796:tiredness mandagih.                      tremble candidan, drafSidan, Iarz-
1294:1ditan [dytn'; HZYTN-tn', inscr. and Ps. HZYTN-] vén-, 2nd p. sg. HZYTN-yd = vënë 7164. HZYTN-h = venah 31°; subju. lst p. sg. HZYTN-n = vēnān P2: 10: to see, to regard, to catch sight of, to contemplate, to discern, to experience: ayāftan u ~ u dänistan 88°; dänäkıhä ~ 51; pat venisn ~ 5013-1; pat (xves) cašm ~ 7479, 80%; — with ki that 115. 127 ete., with ka that 40%; — with a pt. as its complement: -m murtak dit han tahm spähpat I saw this valiant general slain 2719-11; 2 zan nisastak dit 6"; with an adj. P2:10. 2719. 5776 sq. (purr com- ` plement); — with an indir. interrog. clause: ~ kū . . . cigēn to see how 2518-19; ka-t dīt kū kas kē ... kart 137-9 a contam- ination between ka-t dit ku kas
3349:Rötastahm [lwtsthm] n. pr. 1162. — NP Rustam; Old Sogd rwstmy, Reichelt, Sogd. Handschr.- R. II, 63.
3523:stahm [sthm] violence, oppression 738-9.— Paz. stah(a)m; NP sitam.
3635:*Sif(a)rg [Splg] of doubtful meaning, per- haps: swift arrow, ~ % Rotastahm swift Rustam-arrows, arrows swift as those shot by R. 20%, — The form is to
3698:tahm [thm] brave, valiant 1915. 22-28 passim. — Av. (626 sq.) taxma-; MPrthPrs thm; NP tah(a)m; < *tak-ma-, v. tak and takik.
3699:tahmak = tahm 1911. *Tai [vd] v. "Tab.
3709:takik [tkyk] strong, brave, heroic, comp. -tar 6115-24, 104%. — Paz. Mx 41?-9. Gagi-tar, Skr. v. $üratara; bagi Aog 84 renders Av. (598) cirya-. Derived from tak (q. v.), ef tahm.
5389:täcaya-: täxtan tafnah-, tafnu-: täp (vi-)tak-: vitäxtan taka-: tak taxma-: tahm tanu-: tan tanu.pereda-: tanā- puhrak l taoš-, tusa-: tuhīkēh
6137:thm: tahm
6279:rwstmy: Rötastahm twyry: Turan
6809:stadan, stán-: statan stah(a)m: stahm stāīdan, stāed: stayitan star: stur
7372:Rustam: Rötastahm
```


## [2026-10-15T02:45:48.888Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==205' NYB_vol2_glossary.txt | cut -c1-400 | head -60"
}
```


### [2026-10-15T02:45:50.101Z] TOOL RESULT

```
-.
škoh [škwh] majesty, magnificence 1614. — Paz. škēh, Skr. v. samüha (in pl.) SGV I, 39; J-Prs škwh ‘magnificence’ (e. g. Isa. 210.19), [To be distinguished from an- other Skoh, MPrs ‘skwhyh ‘poverty’ (A— H II), OP skau8;- ‘poor’].
škuft [Skwpt'] strange, surprising 724; stupefied 11%, - MPrth ‘sky/t ‘wonderful, amazing, immense(ly), very’; NP šikijt ‘anything wonderful’, šikuft ‘a prodigy, magnificence’, šigift, Sıguft ‘wonder, aston- ishment’. The etymological relation be- tween skapta- and *skupta-, *skipta- is not clear, but their meanings cross.
škuiteh embarrassment 665,
šmah [LKWM] pers. pron. 2nd p. pl., cas. rect. and obl., you; your: 2 bdrak $ ~ 62° sq.; dānākān 1 ~ 11814; Vazurg- mihr 4 ~ 11922, — Av. (1304) yūšmāka-, xšmāka-; šmāh < OP *xšmāzam with -xa- for -ka- as in a^müxam, v. amäh; MPrs 'šm'(h); MPrth ‘mwh; Paz. NP šumā.
šnas [Sn’s] pres. st. of šnāxtan, in com- pounds: spās-šnāsān (pl. cas. obl.) those understanding service = having service as their profession 71!, v. späs.
šnāsak knowing, learned 213. šnāsēh knowledge 7119.
šnāxtan [šn'htn'] šnas-, Ist p. sg. šnāsom [Sn’swm] 5777, to understand, to know, to recognize 615; bē ~ 715, 907. 10018; 5722 + hakar ‘whether’. — Av. (559) xénà-, pres. ašnas- = OP (Skr. jää-); MPrthPrs *$n?xin “Snäs-; Paz. Snàxtan $näs-, NP Sinäxlan šinās-.
187
Sustan
šniyišn ([šn'dšn'] propitiation, praise, homage 361. - From Av. (559) xšnav- ‘to propitiate’; the BP vb. is commonly šnāyēnītan.
šūd [šwd] husband 228, 1012. — Paz. šūt, šūt; NP šoy, šauhar; v. also apē-šūd.
šodomand [Swd’wmnd] having a husband 227,
$ón [šwn'] kind, sort, way, manner: pat han i vattar ~ bandet 7471-22, — < *šavana-, from šutan: Bailey, BSOS VI, 1932, 947 n. 1.
Söstar [šwstl] the well-know town, men- tioned together with Sas 11039. — Cat. 97. Gr Xoorga, Syr Söstre, Arab Tustar (with dissimilation of the initial) Yagut 1,847 sq., where also the form Süstar is mentioned.
$upän [šp'n'] shepherd 1”; pl. cas. obl. ~-dn 10, — Av. (1029) fšu- ‘sheep’ = pasu-, v.S. v. püh, + pāna-, v. pānak; MPrth swb’n; NP šubān, sabän.
Sus [šws] Susa 11619. — OP Cusä, Elam. Susan, Bab. šu-ša-an; Arab al-Süs, v. Yāgūt 3,188—190.
šusr [šwsl], Suhr [šwhl] sperm, the male generative substance 41?! (v.s.v. and). 5420 [šwsl, but in the following gl. šwhl = Suhr]. 9475.22. 9517-21; apar pat ~ through propagation 40%, — Borrowed from Av. (555) xšudra-, ašučra- ‘liquid’; the pro- nunciation was Suhr, -s- being only the inverse writing of -h-, cf s. v. Mahläh (in fine) and pahlom. As to the etymology cf s. v. šustan.
Susréh the state of being sperm: pat ~ in the state of sperm 95?!.
šustan [šwstn'; HLLWN-tn ] $öd- [HLL- WN-] to wash, with the prev. apar 41?-1; — with frde: frāc dast ~ hac to wash one’s hands of a p. = to break off all relations with him 3814. 443-9; — with ul 417. — Av. (555) pt. xšusta- ‘liquid’ (from *xšaod-), cf ayo-xšust; MPrth šwstn Swwd-
www .parsianjoman.org | ool wok
Sustan
188
Tab
Ghilain 64; MPrs pt. šwst, pres. šwyy- (A-H II, Verbum 183); NP šustan šuy,- modern šūr- (possibly from a denom. of Suhr, v. šusr).
*Šustar [šwstl] read Šēstar g. v.
šutan [ZLWN-tn'] šav- [ZLWN-), forms v. I, 177, to go, opp. (G)matan to come: hac ki mat hom u apāc 6 ku šavom? whence have I come and whither shall I go? 6245; pat druyist šutan u āmat
```


## [2026-10-15T02:45:54.411Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 212 213 214; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' NYB_vol2_glossary.txt | grep -n \"^tuv\\|^tōhm\\|^tohm\\|^tuxm\\|^tund\\|^tuvān\\|^19[0-9]$\\|^tō\" | head; echo \"-- $n\"; done; grep -n \"^tuvān\\|^tuvan\\|^tōhm\\|^tōxm\\|^tund\\b\\|^stōr\\|^stōh\\|^stōv\" NYB_vol2_glossary.txt"
}
```


### [2026-10-15T02:45:54.897Z] TOOL RESULT

```
-- 212
3:tohmak extraction, parentage 391; pe- digree 4624; patvand u ~ 4 vazurg illus- trious relationship and lineage 72*; pl. cas. obl. ~-dn relatives 874; — family, house (= all the descendants of a common ancestor) dynasty 18-11, 618, 1018, 1321-26, 283; Mihrak i garan ~ u anäk ~ 14!. — MPrth pl. twxmg*n, MPrs twhmg’n, both ‘relatives’; Paz. tuxma, tuxmaa (SGV); NP tuxmah = tuxm.
7:195
-- 213
-- 214
3819:tuvanikéh [twb’nykyh] powerfulness, ca- pability 27.
3820:tuvan-karčh [~-klyh] opulence, wealth 9112, — From tuvän-kar, tuvän-gar ‘rich, well-to-do’; MPrs tw’ngr; Paz. tuqgar.
```


## [2026-10-15T02:45:56.766Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3790,3822p NYB_vol2_glossary.txt | cut -c1-500"
}
```


### [2026-10-15T02:45:57.223Z] TOOL RESULT

```
šmār, the lemma signifying: ‘tog = ac- count, reckoning’. Paz. hmar represents the NW form of SW āmār, g. v.; Arm. lw. toiž < *tauža- ‘fine, penalty’, tugan < *taugana- id., v. further s. v. tērtan and ham-tožik. — Coincides in spelling with tangēh, but 4619-3! must refer to the Last Judgement, thus to the last settle- ment of aecounts.
töhm [twhm], tóm [twm] 89°; seed, ex- traction, descent 62°. 63?; sperm 89°; descendant 634. — 1. NW *tauxman-: Av. (623) taoxman-; MPrth twam (MHO); Paz. NP tuam; 2. SW *tauhma-: OP taumä- ‘family’ (thus spelt for tau^mà-); Arm. lw. tohm; MPrs twhm); Paz. Oum. V. Benveniste, BSL 31, 1931, 76—79; 47, 1951, 37-39; Henning, BSOAS XI, 1946, 716.
tohmak extraction, parentage 391; pe- digree 4624; patvand u ~ 4 vazurg illus- trious relationship and lineage 72*; pl. cas. obl. ~-dn relatives 874; — family, house (= all the descendants of a common ancestor) dynasty 18-11, 618, 1018, 1321-26, 283; Mihrak i garan ~ u anäk ~ 14!. — MPrth pl. twxmg*n, MPrs twhmg’n, both ‘relatives’; Paz. tuxma, tuxmaa (SGV); NP tuxmah = tuxm.
tóxtan [twhtn'] čož- [twe-] to pay a debt, a fine; to give back, return anything (borrowed): ken tēžēt he will take his revenge 4522, — Cf (Paz.) men hom Ādīnē i xin-xaGh u xin-06é u xin i haft-anbadaa pa farzanda Gēžom (Adino for Adēnāi, xin for ken, anbädaa faulty reading for óbüda = öbätak v. I, XV n. 2) ‘I am Adönäi, desiring revenge and taking revenge, and I shall revenge myself upon the children during seven genera- tions’ SGV XIV, 5-7, reproducing Ex. 20: 5. — MPrth twj- ‘to pay, to atone
www.parsianjoman.org | gol wok
triftak&h
195
Türän
triftakéh [tlptkyh] stealing: apāc kuntš- [ Tür [twl] the name of the hereditary
neh u burtäreh u ~ 11214. — Av. (643) tarop- ‘to steal’. subju. trofyāt (Y.115; a hapax) < *trpydt with secondary develop- ment of -r- to -ra- (tr- is only secondary in Olr) Cf NP tarb, tarfand ‘deceit, fraud, lie’. As the BP derivatives of this root semantically agree with Av., whereas the derivatives outside this group have other, non-technical significations, the former must be regarded as borrowed from Av., and consequently tlpt is best interpreted as trift, not as tirft as Bthl has it. This
Oritak [Paz.] n. pr. 473. — Av. (807) Orita-.
*Tucap [twe’p'] n. pr. of a king in East Iran 11374. — Cat. 39 reads Töcäp; NP Sn. Tužāv.
*tugrān P 1:3: the correct reading is not twgrn, but tgwl[^]n, historical spelling of türün, v. Tūrān no. 2.
tuhikéh [twhykyh] emptiness, vacuity; the Vacuum in a cosmic sense 929. — From tuhik ‘empty’, from Av. (624) taoš-, pres. tusa-; MPrs twhyg; Paz. ihi (SGV);J.-Prs. twhy; NP tuhi, tihi, tahi; v. Nyberg, Geiger Vol. 1931, 214 sq., and against him Gershevitch and Mayrhofer, v. Mayrhofer, Osterr. Ak. d. Wiss., Anz. d. phil-hist. Kl. 1968, So. 1.p.15 (dubious hypotheses).
tumbak [twmbk'] drum, or kettle-drum 209. — Arm. lw. tmbuk < *tumbuk ‘drum’; NP tanbak, tanbuk, tanbik ( BQ also tun-) ‘bagpipe’, ‘drum’.
foes of the old Iranians, the Tür, Turian, the Turians: 1. of an individual: Frāsyā
~ 4 vas varcävand 4616; 9922-25, 11318, 1163. 11719; Brätaröres 51%;  Palecak 11411; Asp-varcvar 115%; Arvanddsp
11716, — 2. ‘in plural sense, of the people: ~ cas. rect. 4513; ~ used as cas. obl. 451? (pat ~); cas. obl. ~-dn 45°11, used as cas. rect. 4515, — Av. (656) tūra-; MPrth twrn (S); Paz. tür; v. further Turan.
Türak n. pr. of a Khakan 17°.
Turin 1. [twl'n'] pl. cas. obl. of Tür (g. v.). — 2. Country and people between Sakistān (now Sīstān) and Makurän (Mukrän, now Makrän) ‘down to the shore of the River’ (i. e. Indus), forming together with Hind and Sakistān the dominion of the Sakān-šāh P1:3. Identical with the modern province Kalat in Baluchistan, whose capital is now Kalat formerly Qusdär or Quzdär (Yaqut 4,86. 105, nowadays pronounced Khuzdar); attested in the Sassanian inscriptions in the following spellings:.1. KZSPrth 1. 2 
13% www.parsianjoman.org | ool wok
Turan
tugrän, or turgän with the same Prth. metathesis as in tyrg = tirg < tigra- ‘swift’ (A-H ITI) or in the Arm. lw. turž ‘penalty’ < *tužra- (v. tog, toxtan). Prs tgwi'n shows the inverse Sogdian spelling -gw- for -wg- (Henning, BSOS IX, 1938, 548—550), thus representing tugrān, whence tiran according to the common SW phonetic rule. For Turdn, and designating the same country, Yàqult (3,554) quotes the form Tuwärän, which evidently goes back to *tugārān. (NB: no attention has been paid here to the 
turist [twlyst'] throughout: hamäk ~ sap 501%. — Through dissimilation < *tiris-t < *tiras < *tirasca = Skr tirašca; -t is inorganic and due to analogy with the sup. ending -ist (cf hämist, no. 2). Av. (640 sq.) tarasca, reflected in BP by the more common tarist (v. hu-tarist), render- ing Av. (641 sq.) taro.
Tüs [tws] 1. a mythical hero 100*-?. 1066. 1147-9-25, — 2. the town founded by him (now Mašhad) 114*— Av. (657) Tusa-; Tūs Yagut 3.560 sqq.
tušn [twšn'] silent, quiet 41°. — Av. (657) tušni-, also in compounds: tušnā-mati-, tušni-šad (658).
196
tuxšākēh
tuvän [twb?n'] 1. adj. mighty, powerful, energetic 559. 6619; subst. what one is able to do, v. s. v. sämänihä. — 2. impers. vb.: it is possible, one can, is able to; the subj. is an encl. pron., or a subst. in the cas. obl., or a form felt as a cas. obl.; construed with an inf., which is generally placed before, less often after ~; pret. ~ būt; a) without a subj.: 6 x¥és kartan nem 9?" ; griftan ne" (ef s. v. Säyistan) ete.; — b) with a logical subj.: man zatan nē ~ I cannot slay him 99%; man z
tuvanikéh [twb’nykyh] powerfulness, ca- pability 27.
tuvan-karčh [~-klyh] opulence, wealth 9112, — From tuvän-kar, tuvän-gar ‘rich, well-to-do’; MPrs tw’ngr; Paz. tuqgar.
tuvänistan [~-stn'] to be able to, pt. = pret. 3d p. sg. tuvänist 17°. — Secondary vb.; not in old BP texts.
tuxšak [twhs’k] industrious, assiduous,
```


## [2026-10-15T02:46:01.605Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 111 106 174; do echo \"=== NR $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | grep -n -i -B1 -A6 \"tuvän\\|tuwän\\|tavän\\|tuxm\\|tuchm\\|sitür\\|sutür\\|stör\\|tund\\|tahm\" | cut -c1-300 | head -60; done"
}
```


### [2026-10-15T02:46:02.026Z] TOOL RESULT

```
=== NR 111
1-— 89 —
2:395. tund schnell, heftig, stark'.
3-aw. Hvant" (= Hnvant-), [/'tav-, vergl. tuvan (No. 401).
4:396. tunder, tundur ^Donner .
5-Vergl. ai. i/^tan-, tdnyati erschallen, laut tönen,
6-rauschen', tanayitnü- 'donnernd', tanyatii' 'Donner';
7-lat. tonare, tonitnis; ags. pnnjan, punor, nhd. Donner^
8-engl, thufider,
9-397. tenuk *düun, zart, fein'.
10-ai. tanu-, tdnuka- *dünn, fein\
--
28-401. tuvan 'vermögend, mächtig', tuvanä, tuvanisten.
29:aw. i/^taV' 'können, vermögen', tavä[cä; phl. tuvän
30:(geschrieben J^D-n), tuvämk, tuvän(i)stan; ai. l^tav-,
31-tavlti; arm. tevem 'bleiben, dauern, aushalten, Stand
32-halten (H. No. 273).
33-402. töften 'sammeln; ausgeben, zahlen', Praes. töz-em;
34-'k^Tin-TND 'Vergeltung' (Is. 34, 11; 35, 4).
35-*) Die Aussprache tö ist zwar nicht überliefert, sie ist aber wohl
36-bei FirdQsi in den Fällen anzunehmen , wo das WorMhetrisch lang
=== NR 106
=== NR 174
```


## [2026-10-15T02:46:05.721Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"tu\\(x\\|ch\\)m \\|sitür\\|sutür\\|sutüh\\|situh\\|sitöh\\|nastöh\\|tahmäsp\\|tubra\\|töbra\" HRN.txt | head; "
}
```


### [2026-10-15T02:46:06.237Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:46:08.384Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^[0-9]\\{3,4\\}\\. \\(tu\\|t[oö]\\|s[iu]t\\|st\\|nas\\|tah\\)\" HRN.txt | head -40"
}
```


### [2026-10-15T02:46:08.941Z] TOOL RESULT

```
3553:378. tuyirn 'Same, Geschlecht', tu/me; arab. LW. tu/m.
3612:385. turus 'sauer .
3718:395. tund schnell, heftig, stark'.
3720:396. tunder, tundur ^Donner .
3744:401. tuvan 'vermögend, mächtig', tuvanä, tuvanisten.
3749:402. töften 'sammeln; ausgeben, zahlen', Praes. töz-em;
3765:403. töle 'junger Hund' (SF).
6224:709. sitäden 'wegnehmen', Praes. sitän-em, siteden^ isteden,
6252:713. sitebr, setehr (AM. 112 Zeile 4), istebr *stark, gewaltig',
6301:720. sutöVy ustör 'Ross' (Srihn. Calc. 1373 Vors 10; Vts
6312:721. sutünf usiün 'Säule'.
6369:728. sut% usmh Blei', "P)nD (Jer. 6, 29).
6377:730. stir-^ Vot', Suhr[äbj Suhr]esp; vergl. sur/tce^ sur/tze
6621:760. st 'dreissig'.
6915:791. stifnar *Zahl, Anzahl', summden (mit her- erzählen*).
10776:142. naslh^) *Leichnam, Aas*.
10780:148. nastnttan Vernichten* (Aw.-Komm., auch in Glossen).
11043:188. stfirtan statt v(l)startan existirt schon im PehlevT
11045:189. st{i)h *Welt* wird man kaum statt (/etJk lesen dürfen.
11083:196. tuf/ 'stark, Held', takik (für aw. ta/ma-)^ takikth,
```


## [2026-10-15T02:46:11.044Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3553,3562p HRN.txt; sed -n 6301,6311p HRN.txt; grep -n -i \"stöh\\|sutöh\\|ustöh\\|nastöh\" HRN.txt HUB.txt | head"
}
```


### [2026-10-15T02:46:12.063Z] TOOL RESULT

```
378. tuyirn 'Same, Geschlecht', tu/me; arab. LW. tu/m.
ap. taumä' 'Geschlecht'; aw. ttto/man-; phlv. tö/m,
töxnmk bezw. tu/m/ak, päz. tti/m, arm. LW. tohm;
ai. tokman- 'Schössling'.
kurd. töm; wa/. tay^Hy sar. töym, yidg. tüyum.
*) Pehlv. pancötak hat ein mir unverständliches ö; darum scheinen
mir auch de Goeje's (ZDMG. 35, 340) auf ihm beruhende, sonst sehr
ansprechende arab. dahötah^ Instötah zweifelhaft.— 85 —
379. teöerv Tasan'.
med. TBxaQoq, mrvonu; Tasan' (Athen. IX, p. 387 DE).
720. sutöVy ustör 'Ross' (Srihn. Calc. 1373 Vors 10; Vts
und Ramm, S. 52, V. 4 v. u.).
aw.staora- 'Zugtier; phlv. s^ör 'Zugtier, aber auch
lioss' (Nöldeke, Kärn. 40, Note 5, vergl. störpcVf^
störgäSj ebendas. S. 43 bezw. 41)-); skr. sthätirin^
'Lastpferd, Lastochs (spät); got. st'mr \Stier'.
oss. t. sturtä 'Vieh' (233); kurd. zaza L\V. estör,
dujik. ästori 'Pferd'; Titr. LW. istorr^ astor 'Pferd',
si;'n. stör, sar. stdur^ stdor 'Zugtier, ausgowachscMio.s
Rind', ya/n. «li^wr 'Schaf, Vieh überhaupt' (Tomaschok,
S. 764).
HRN.txt:8084:gärzin stöhnen* (89).
HRN.txt:10545:oss. d. yärzun, t. qärzin 'stöhnen (89).
```


## [2026-10-15T02:46:15.317Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"tu[xy]m\\b\\|tu[xy]m \\|sutür\\|sutöh\\|sutüh\\|sitöh\\|ustöh\\|tuvän\\|tund \\|tahmasp\\|tahmäsp\" HUB.txt | head -15"
}
```


### [2026-10-15T02:46:15.733Z] TOOL RESULT

```
1650:395. Dass tund *schnell, heftig, scharf, spitz' (Fird. Ill,
4996:stand'; bustdn = bdstan 'Garten'; tuxm 'Same' = paz. tuxm^
8988:wort!) = zd. daxma- H. 543; tuxm Same, Geschlecht' =
8989:zd. taoxman-, pSz. tuxm, arm. tohm (aber ap. tauma-l);
9012:Staxr, Bahl = np. BalXy tohm = np. tuxm, vstah Ver-
9234:f) Ap. xm = np. Qcm, hm^ m: tuxm *Same' H. 878 u. s. w.,
9668:p. 48, Nr. 395. Die urspr. Bedeutnng von tund scheint 'scharf*
```


## [2026-10-15T02:46:17.991Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1650,1660p HUB.txt; sed -n 9668,9674p HUB.txt; grep -n -i \"stör\\|sitür\\|sutür\" HUB.txt | head -5"
}
```


### [2026-10-15T02:46:18.515Z] TOOL RESULT

```
395. Dass tund *schnell, heftig, scharf, spitz' (Fird. Ill,
1703, 3642) (aus *tuvant-?) nahe verwandt mit tuvdn
VermSgend, fahig' sei, glaube ich nicht.
396. Zu tundar 'Donner JRAS. 1894, 452 gehort afgh.
LW. tandar *Donner , echt afgh. ^aw^'Donner (Geiger).
398. Np. tang enge, bedrangt' geh5rt zu tanjldan zusammen-
ziehen', auch angusto et aegro esse animo', skr. tanc
und taiij (Nr. 394) u. s. w. Vgl. tang u bandt obli-
gation' JRAS. 1894, 452. — Dazu auch tang *Sattel-
gurt' (Shah. Ill, 1537, 728 - Noldeke), bal LW.
tang *Sattelgurt' (Dames p. 60) kurd. taiig 'Gurt',
p. 48, Nr. 395. Die urspr. Bedeutnng von tund scheint 'scharf*
gewesen zu sein.
p. 50, Nr. 426. Vgl. p. 107, Nr. 1124W».
p. 50, Nr. 427. Vgl. hind. Jantar bei Vullers.
p. 53, Nr. 456. Vgl. p. 131. — Ueber dir pars, portio' (wo
vorkommend?) = skr. cfra- 'Streifen' vgl.
Geiger, Idg. F. IV, Anz. 23.
```


## [2026-10-15T02:46:21.555Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^\\*tau\\|\\*tau-\\b\\|\\*tau- \\|tuwān\\|tavān\\|sutōh\\|stōh\\|\\*us-tav\\|tund\" CHEUNG.txt | head -20"
}
```


### [2026-10-15T02:46:22.052Z] TOOL RESULT

```
24595:*NEIR: Oss. I. tonyn/tynd, D. tonun/tund ‘to tear (off); to reap (berries, fruits, corn); 
25062:*tau ? 385 
25110:*tau ? ‘to throw, spread, sow’ 
25136:9 It is necessary to postulate a root *tau- ‘to sow, throw (vel sim.)’ that would be 
25138:of the rather limited geographical distribution this "root" *tau- is some kind of 
25149:*tauH ‘to be able, strong’ 
25183:*tauj2 387 
25213:*tauj! ‘to impel, hasten’ 
25234:*tauj2 ‘to acquire, gather, gain’ 
25294:*tauS ‘to (be) empty’ 
25378:390 *tund 
25401:*tund ‘to act violently’ 
25403:*MIDDLE PERSIAN: MMP rond BMP rond /tund/ ‘sharp, violent? > DMMPP: 330b 
25404:*KHOTANESE: ttunda-, ttuda- (ppp.) ‘plundered’ (< ? denom. *tunda-ia- ‘to act 
25405:violently’). The etymology of Khot. *tund- which was proposed by Bailey (DKS: 
25407:untenable. Sims-Williams, SVK III: 68, s.v. ttunda-, considers a connection with 
25414:*NWIR: NP tund ‘violent, sharp (of taste)’ 
25419:denominative formation of *tund. This nominal form (derived from an attested Ir. 
25424:*IE COGNATES: Lat. tundö (perf. tutudi) ‘I thrust, hit’, Goth. stautan, NHG stoßen 
29176:tundn) Sa- ‘to be able’
```


## [2026-10-15T02:46:24.112Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25149,25182p CHEUNG.txt; sed -n 25398,25430p CHEUNG.txt"
}
```


### [2026-10-15T02:46:24.624Z] TOOL RESULT

```
*tauH ‘to be able, strong’ 

*AVESTAN: tauu- (tu-) ‘to be able, strong’ > Liste: 26 

Pres. athem.: IND. med. 3sg. YAv. tüite (V 13.8), SUBJ. Isg. OAv. tauuä (Y 28.4, Y 50.11), 3sg. YAv. 
frätauuat (Vyt 51), 3р1. ? YAv. (them.!) tauuan (V 6.51), OPT. 2sg. YAv. fratuiia (Y 9.29); Perf.: IND. 
3sg. Y Av. tütauua (V 6.32); Partic.: pres. YAv. tuuant- (V 3.33) 


*OLD PERSIAN: tav- ‘to be strong’ — Kent: 186a 

Partic.: pres. nu- (?) tunuvant- <tu-u-nu-v-t-> (DB 4.65), <tu-u-nu-v-t-> (DNb 9); Caus.: IND. 3sg. 
tavayatiy <t-a-v-y-t-[i]-y> (DNb 33), impf. 1sg. atavayam <a-t-a-v-y-m> (DNb 47) 

*MIDDLE PERSIAN: BMP twb'n- /tuwan-/ ‘to be able’, MMP tw’n, BMP twb’n 
/tuwan/ ‘might, power’ || (+ *pati-) MMP pt’y-, BMP pt’y- /pattay-/, BMP pt'dst- 
/pattayist-/ ‘to remain, continue; endure’. 0 MMP tw’n, BMP twb’n /tuwan/ are also 
frequently employed as (impers.) verbal aux. ‘to be able’, construed with an 
infinitive. || DMMPP: 330a, 285a 

Partic.: perf. pass. ВМР twb’nst /tuwanist/ || (+ *pati-) Pres.: IND. 2sg. MMP pt’yy, 35р. ? MMP “pt’yd, 
BMP pt’yyt /pattayéd/, SUBJ. 3sg. MMP “pt’y’d, IMPV. 2sg. MMP pt’y, BMP pt’y /pattay/; Partic.: 
MMP "рім 

*PARTHIAN: t’wg ‘strong’ || (+ *pati-) pt’w- ‘to bear, tolerate; (?) to remain, insist 
on’. © On pt’w- cf. Sundermann 1981: 169a: "Die Bedeutung bleiben" ist für mp. 
pattudan wohl bezeugt ..., für parth. pattudan, pattaw- ist m.W. jedoch ... nur ,,erdul- 
den, ertragen” belegt". = Ghilain: 76 f. | DMMPP: 322b, 285a 

(+ *pati-) Pres.: IND. 35р. pt’wyd, SUBJ. 35р. "pt’w’h; Inf.: рма 

*KHOTANESE: LKh. tvafi- (tvafi-) ‘to strengthen’ = SGS: 41 


362, 269 


*tund ‘to act violently’ 

*MIDDLE PERSIAN: MMP rond BMP rond /tund/ ‘sharp, violent? > DMMPP: 330b 
*KHOTANESE: ttunda-, ttuda- (ppp.) ‘plundered’ (< ? denom. *tunda-ia- ‘to act 
violently’). The etymology of Khot. *tund- which was proposed by Bailey (DKS: 
131b), an enlarged root of *tau-/tu ‘to thrust, remove, plunder’ (Pokorny: 1032 ff.) is 
untenable. Sims-Williams, SVK III: 68, s.v. ttunda-, considers a connection with 
CSogd. twmd’rt ‘he knocked’, translating Syr. nqs ‘id.’. No further Ir. cognates can 
be cited though. I would rather interpret the Khot. forms as denominative. = SGS: 
39 

*SOGDIAN: BSogd. twnt ‘violent’ 

*NWIR: NP tund ‘violent, sharp (of taste)’ 

*SANSKRIT: fud ‘to thrust, push, crush’ (RV(+)) = EWAia I: 671 

The Khot. forms (the corresponding present stem is not attested), may be the sole 
denominative formation of *tund. This nominal form (derived from an attested Ir. 
root *taud) is perhaps cognate with Skt. tud, cf. Sundermann apud EWAia I: 671. 
*PIE *(s)teud- ‘to thrust? > LIV: 601 | Pok.: 1033 f. 


*IE COGNATES: Lat. tundö (perf. tutudi) ‘I thrust, hit’, Goth. stautan, NHG stoßen 
*REFERENCES: Werba 1997: 191 


@
```


## [2026-10-15T02:46:29.190Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4680,4692p PHD_mackenzie.txt; grep -n \"^stōh\\|^stōv\\|^stōy\\|^astōh\\|stōv\\b\" NYB_vol2_glossary.txt | head; grep -n \"\\*stau\\|\\*stauH\\|stōh\\|ستوه\" CHEUNG.txt | head"
}
```


### [2026-10-15T02:46:29.555Z] TOOL RESULT

```
                   '
ster [styl I N siter] stater.
stezag [stych , M <styz-, N siteza] quarrel, strife.
                 '
sti [sty(y) = Av. sti-] being, existence.
sto [stwbl , (P <stwb, N suto/z)] distressed, defeated.
 ""wih: distress.
star [stwll P <stwr, N sutor] horse, mount; large cattle.
 ""bin [-p'n l I N -ban] (head) groom.
 ""gAh [-g's] stable.
·stoi [stwl] the fourth morning after death.
stowenidan, stowen- [stwbyn-ytn'] defeat, overcome.
stowih, v. stO.
23873:366 *stau 
23876:*stau ‘to praise’ 
23938:*staub/f ‘to sound, utter’ 
23945:apparently Пг. root has IE cognates: it is perhaps a blend of the ‘praise’ (*stau) and 
23953:*staup ‘to overcome, defeat’ 
56292:*staup 
56344:*staup (s.v.), *tanč (s.v.), 
57328:*staup, *taru 
57384:*karH'! , *stau 
57682:*stau (S.V.)
```


## [2026-10-15T02:46:31.297Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23953,23990p CHEUNG.txt"
}
```


### [2026-10-15T02:46:31.864Z] TOOL RESULT

```
*staup ‘to overcome, defeat’ 
*MIDDLE PERSIAN: MMP ‘stwy- ‘to defeat’, BMP stwbyn- /stöwen-/ (sec. caus.) ‘to 


destroy’, BMP stwb /stob/ ‘powerless’ > DMMPP: 91b 
Pres.: SUBJ. 3sg. MMP ‘stwy’d; Inf.: BMP stwbynytn /stowenidan/ 


*PARTHIAN: ‘stwb- ‘to conquer, defeat’, ‘stwb ‘defeated’ = Ghilain: 67 | DMMPP: 


91а 
Pres.: IND. 35р. ‘stwbyd, SUBJ. 35р. ‘stwb’; Partic.: perf. pass. II ‘stwb’d 


*NWIR: NP sutöh ‘struck by emotions like fear, distress, stupefaction, astonishment, 
sadness, sense of helplessness, etc.’ 

The root *tav- (i.e. *tauH ‘to be able, strong’) suggested by Ghilain (accepted in 
Nyberg II: 180b) as the origin of these WIr. forms meets phonological (and 
semantic) difficulties, as it leaves -b- unexplained. A development w > b (cf. BMP 
Iwbsn [rawisn]), which Ghilain postulates, is implausible: even the assumption that 
-wb- is purely graphic for -w- cannot be invoked here, on which see Nyberg 1974: 
180b, s.v. stob ‘powerless’. The Pth. example rwbysn ‘change’, which Ghilain cites, 
may be explained differently, v. *raup, *jaup?. 

«PIE *steup- ‘to strike, be struck’ => LIV: 602 f. | Pok.: 1034 

*IE COGNATES: Lat. stupére ‘to be numbed, stunned’, Gr. стола Get ‘strikes’ (Hes.) 


*stranj ? ‘to become stiff, stiffen’ 

*KHOTANESE: LKh. stris- (inch.) ‘to become stiff’, LKh. straj-/stri- (caus.) ‘to 
stiffen’ || (+ *pati-) ? LKh. pastri- ‘to become stiff; to revolt’, ? LKh. pastramj- 
(caus.) ‘to repress’ || (+ *fra-) ? LKh. hastris- ‘to press, insist?’ = SGS: 79, 135, 151 
*NEIR: Q Pash. Хах, xaX ‘hard, stiff’, cited in EVP: 79, has a different etymology, v. 
NEVP: 99.
```


## [2026-10-15T02:46:35.701Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^stōb\\|^stob\\|^stōh\" NYB_vol2_glossary.txt | head -3; grep -n \"^stōb\\|^stob\" NYB_vol2_glossary.txt | head -1 | cut -d: -f1 | xargs -I{} sed -n '{},+1p' NYB_vol2_glossary.txt | cut -c1-700"
}
```


### [2026-10-15T02:46:36.363Z] TOOL RESULT

```
3531:stob
3544:stob [stwb'] powerless: ~ kartan to de- feat 3319. 858-12, 11574; ~ bütan to be defeated 912. — NW form: MPrth ‘stwb- ‘to enfeeble, to annihilate’ (A-H II, 302 n. 4), evidently a denom. of the adj. ‘stwb = estob (i. e., estöß), taken over by BP as stwb' (the original NW form ’stwb' is still found in FrP, Cod. P fol. 6%) and developed to *stēw > *stöi alternating as usual with stoh, which prevailed: Paz. stoh, stuh, NP sutüh. (The reading stwb' = "stav which I gave in HP was wrong, as shown by the MPrth form ; the spelling -wb- for -v- is unknown in MPrth). The authentic SW form is ‘stw = estav (also in Prth: MPrth ‘st’w- caus. ‘to annihilate’, W.-L. 112, II R 3b) attested in ‘stwy- gwn- ‘to overcome’, ‘stwy-bwdn ‘to be defeated’ (List 81, cf s. v. àkas?), also attested by FrP, Cod. P fol. 284, in the form stw' (erroneously read in Paz. stün, but glossed by sutüh, Anguetil Duperron ‘foible, pauvre’). I derive it from *us- tavah- ‘out of force, powerless’, from Av. (639) tavah-; MPrth estob may go back to *ustava(h)-bū- ‘being powerless’, cf SW ‘stwy-bwdn just mentioned.
stob
istar [stl] coll. the stars, the sphere of the stars 2025, 331, 3020.21,932-9. 10423, 1098. — Av. (1598) star-; v. also stärak.
```


## [2026-10-15T02:46:41.066Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-10-15T02:46:41.078Z] TOOL RESULT

```


```


## [2026-10-15T02:46:43.078Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ستوه",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-15T02:46:43.626Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/تند",
 "prompt": "Give the Persian etymology section(s) verbatim."
}
```


## [2026-10-15T02:46:44.199Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/توبره",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-15T02:46:44.798Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/تخم",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-15T02:46:45.328Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ستور",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-15T02:46:45.679Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/توان",
 "prompt": "Give the Persian etymology section verbatim."
}
```


### [2026-10-15T02:46:47.977Z] TOOL RESULT

```
# Persian Etymology Section

The etymology section states: "(This [etymology](/wiki/Wiktionary:Etymology "Wiktionary:Etymology") is missing or incomplete. Please add to it, or discuss it at the [Etymology scriptorium](/wiki/Wiktionary:Etymology_scriptorium#ستوه "Wiktionary:Etymology scriptorium").)"

In other words, no etymological information is currently provided for this word on the page.
```


### [2026-10-15T02:46:50.056Z] TOOL RESULT

```
# Persian Etymology Section

From Middle Persian *tōbrag* ("bag, sack"), cognate with Sanskrit ṭopara ("a small bag"). The term shares roots with Middle Armenian toprak ("sack"), Arabic ṭarbūq ("legging"), and Classical Syriac ṭūḇarqā ("nosebag of an ass"), all representing Middle Iranian borrowings. Related to Classical Persian tarbō ("a kind of silken cloth of red colour").
```


### [2026-10-15T02:46:50.602Z] TOOL RESULT

```
# Persian Etymology Section

The Persian etymology states that توان is "[Inherited](/wiki/Appendix:Glossary#inherited "Appendix:Glossary") from [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") \[script needed\] (twbʾn' /⁠tuwān⁠/, "might; power"), ultimately from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _[\*tewh₂-](/wiki/Reconstruction:Proto-Indo-European/tewh%E2%82%82- "Reconstruction:Proto-Indo-European/tewh₂-")_ ("to swell, grow, become strong")."

The section includes cognates in Sanskrit, Avestan, Proto-Slavic, and Ancient Greek, and concludes with the note: "the verb is from the noun, not the other way around."
```


### [2026-10-15T02:46:50.873Z] TOOL RESULT

```
# Persian Etymology Section

From Middle Persian _stwl_ (/⁠stōr⁠/, "horse, mount; large cattle"), from Avestan _𐬯𐬙𐬀𐬊𐬭𐬀_ (staora, "large cattle"), from Proto-Iranian _[\*stáwrah](/wiki/Reconstruction:Proto-Iranian/st%C3%A1wrah "Reconstruction:Proto-Iranian/stáwrah")_, from Proto-Indo-Iranian _[\*stáwras](/wiki/Reconstruction:Proto-Indo-Iranian/st%C3%A1wras "Reconstruction:Proto-Indo-Iranian/stáwras")_ ("large domestic animal, cattle"), from Proto-Indo-European _[\*(s)táwros](/wiki/Reconstruction:Proto-Indo-European/t%C3%A1wros "Reconstruction:Proto-Indo-European/táwros")_ ("wild bull, aurochs"). Probably related to obsolete _[تاول](/w/index.php?title=%D8%AA%D8%A7%D9%88%D9%84&action=edit&redlink=1 "تاول (page does not exist)")_ (tâvel, "bull, ox").
```


### [2026-10-15T02:46:55.386Z] TOOL RESULT

```
# Persian Etymology Section

The Persian etymology section states: "From [Parthian](https://en.wikipedia.org/wiki/Parthian_language "w:Parthian language") _[𐫤𐫇𐫟𐫖](/w/index.php?title=%F0%90%AB%A4%F0%90%AB%87%F0%90%AB%9F%F0%90%AB%96&action=edit&redlink=1 "𐫤𐫇𐫟𐫖 (page does not exist)")_ (twxm /⁠tōxm⁠/, "seed, line, race"), from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*táwxma](/wiki/Reconstruction:Proto-Iranian/t%C3%A1wxma "Reconstruction:Proto-Iranian/táwxma")_ (compare [Avestan](https://en.wikipedia.org/wiki/Avestan "w:Avestan") _[𐬙𐬀𐬊𐬑𐬨𐬀𐬥-](/w/index.php?title=%F0%90%AC%99%F0%90%AC%80%F0%90%AC%8A%F0%90%AC%91%F0%90%AC%A8%F0%90%AC%80%F0%90%AC%A5-&action=edit&redlink=1 "𐬙𐬀𐬊𐬑𐬨𐬀𐬥- (page does not exist)")_ (taoxman-, "seed"), from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _[\*tewk-](/wiki/Reconstruction:Proto-Indo-European/tewk- "Reconstruction:Proto-Indo-European/tewk-")_ ("germ, seed, sprout, offspring"). Compare [Old Armenian](https://en.wikipedia.org/wiki/Classical_Armenian "w:Classical Armenian") _[տոհմ](/wiki/%D5%BF%D5%B8%D5%B0%D5%B4#Old_Armenian "տոհմ")_ (tohm), an Iranian borrowing."
```


### [2026-10-15T02:46:56.003Z] TOOL RESULT

```
# Persian Etymology Section

From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") (twnd /⁠tund⁠/, "sharp, violent"), from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") *[\*tund-](/w/index.php?title=Reconstruction:Proto-Iranian/tund%C3%A1ti&action=edit&redlink=1 "Reconstruction:Proto-Iranian/tundáti (page does not exist)")* ("to act violently"), from [Proto-Indo-Iranian](https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language "w:Proto-Indo-Iranian language") *[\*tund-](/w/index.php?title=Reconstruction:Proto-Indo-Iranian/tund%C3%A1ti&action=edit&redlink=1 "Reconstruction:Proto-Indo-Iranian/tundáti (page does not exist)")*, from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") *\*tu-n-d-*, ultimately from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") *[\*(s)tewd-](/wiki/Reconstruction:Proto-Indo-European/\(s\)tewd- "Reconstruction:Proto-Indo-European/(s)tewd-")*.
```


## [2026-10-15T02:47:00.187Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"tobr\\|t[oō]bra\\|tōbre\\|tubra\" IEC.txt | head; grep -n \"^t[eē]u\\|^tu[bm]\" IEC.txt | head -20"
}
```


## [2026-10-15T02:47:01.339Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/táwros",
 "prompt": "Give the etymology section and the list of descendants (Indo-Iranian, Germanic, Latin, Greek), and any mention of Semitic *ṯawr-."
}
```


## [2026-10-15T02:47:02.711Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tewh₂-",
 "prompt": "Give the etymology/root meaning and full list of derivatives and descendants (Indo-Iranian, Avestan, Persian, Greek, Latin, Germanic incl. thumb, thousand, thigh, tumor, tuber, tyros, tymbos)."
}
```


### [2026-10-15T02:47:03.171Z] TOOL RESULT

```
17666:sthóbos, å “post, pile, lump’. Cf. sthob- and sthab-. (Gmc. ‘step’ uncertain) MHG stuof, sm. (‘nugget of metal, ore”, etc.); (stuofe, f. ‘step’: Du. stoep, f. ‘step; dais’; OE cf. stopel, m. 'footprint); Li. stuobas, m. ‘torso, hull; stand, frame’; cf. stuobrys, io, m. ‘stump; lout’; Latv. cf. (ambig.) stobrs, m. (“pipe, gun-barrel; hemlock’. Cf. sthomb-)
715:tum; arma “arms”; armus, 1 (shoulder, arm, haunch’: Arm. armu-kn); Ir. cf. oirim (for *airim ?) ‘suit, fit’; Go. arms (i-stem m. ‘arm’); OE earm “arm, foreleg’; ON armr; Slovene cf. jérmen, m. ‘strap’; OCS jarímü (‘yoke’: Cz. jarmo, id.) beside rame, obl. ramen- “shoulder” (a:a). There is an apparent variant iar- (q.v.) represented by Tokh. AB yàárm, B yarm ‘measure’; Gk. hárma “team”; ON jor- muni *draught-animal
18459:teub- ‘sway’ Srb. cubam se, v. ‘swing, sway’; Lat. cf. (re- dup.) titubo, are, v. ‘stagger, hesitate; stam- mer
18460:teubh- (tubh-) (1) 'struggle; fight, attack". Cf. WP I, 714
18463:teubh- (2) ‘tuft, clump, hump’. Cf. tūbhos Arm. (ambig.) Éov, u, u, s. (tuft. See SEM: Arm. & IE: $8 56, 75, 87); Lat. cf. über, gs: -eris, n. (formerly an -es-/-os- stem) “lump”; Lat. LW fr. Umb. tüfa, f. ‘plume’; Ir. cf. tua- bhal & tua(bh), m. ‘burdock’; Srb. Cuba, f. ‘crest of hen’; OCS Cubü, m. id.; R Cub "Tore, lock’; Pol. czub ('tuft^, fr. *teubh- (teub-), or fr. *Fkeubh- (keub-) ?); (zero-gde in) OE pàf, m. id. (and ‘tuft of leaves’), cf. byfel, m. ‘shrub’; Upper G Düppel, s. “lump”; ON püfa, f. ‘mound’; Li. tübas, tübà, mf. ‘felt’; tübe, f. ‘mullein’?
18464:teud- (teudó, io) (1) ‘incite’; teudos, (tud-) “incitement. See Supt: T and cf. WP I, 513 & II, 554. Alb. ambig. Skt. Cóodami, Codayami & (o-gde) todayami, v. *goad'; Alb. cus, cys. v. id.; Pol. cudzic, v. ‘tug, lug’ (vocalism of Pol. cucic, v. ‘rouse’, fr. *teut-; Alb. ambiguously fr. *teudi- or fr. *teutj-. Nominal types: Skt. Codáh, adj. *ex- citing’; Códah, m. *goad'; čodā, f. “incitement; (o-gde in) todah, m. ‘goad, sting; drover’; (isophonic: Slovak: cüdit', Cz. cídit ‘cleanse, polish, purify’; Cz. cf. cudny ‘proper, moral: Blg. Cud, m. custom")
18465:teud- (teud-, tud-) (2) ‘beat, bang, crash’. Cf. tund- & tud- as a separate item. WP I, 513 & 745; II, 554 MHG dies, sm. “bang; noise; jolt'; (o-gde in) dos, sm. id.; OE péot, n. ‘din, howP'; peote, f. ‘gush, rush’; Sw. tjut, n. “howP'; tjuta, v. id.; Ir. cf. tuaim, f. ‘heavy blow, bang; OCS tuma, f. ‘plague’ (if fr. *teudma). Cf. Srb. Cudam se, -ati, se, v. “be frightened"; ON pjóstr, m. (‘fury’, fr. a type *teudstos); Srb. cula, f. (“cudgel', fr. *teudla). (Slovak pod-cudky, m. pl. “siftings? is from cudit inf. ‘cleanse’, etc, of uncertain origin, see teud- (1))
18466:teugos “fat, thick’. (Celtic variant: teguos. For metath. cf. tauros, $auros in their Celtic forms.
18467:teubh- — teukso, ið
18477:teuk- (teukos, à) (1) “tip, point, peak, beak’. Cf. tuk- (1) & keukos, à (1) Skt. Gokab, am. mn. ‘a root'; Per. cf. Caugan, s. “bat, club’; čukuš, s. ‘hammer’; Alb. suké, f. “hill, peak’; Ligur. (in Swiss) tschuggi, f. id.; Mir tuag, f. ‘axe’; Br. Suk, m. ‘nape, shoulder, chignon’: Blg. čuk, m. ‘hammer’; Srb. &üka, f. Cpeak, point’, fr. a variant *keuka); Latv. cf. Cukurs, m. “peak, point, gable’. (Indo-Iran. forms ambig.)
18478:teuk- (2) “press; pressure, force’. Cf. tuk- (2) and next. See teuquó Arm. tok, ost ‘persistence’; tokam, v. (per. sist, endure'. Cf. SEM: AIE: § 56: IE -eu- > Arm. -0-); OHG diuhen, wv. “press, force” beside dühen, id. (fr. *tükio); G deuen, v. *tolerate; atone for; Li. cf. tüksti, intr. v. ‘bang’. (Gmc. forms ambig. Cf. teuquó as a variant in OE)
18479:teuk- (touk-, tuk-) (3) “fat; fat part, buttock’. Cf. tuk- (2) & touk-. WP I, 711 Tokh. B cf. wi-cükaine ‘the two haunches, buttocks'; Olr. cf. (*-eu- or *-ou-) tuachail, adj. ‘pregnant’; OHG dioh, n., MHG diech, gs: diehes, n.; OE péoh, n.; ON þjó, n. ‘thigh, haunch’; Icel. ‘buttock’; Du. dij, f. as OHG; EMDu. dije, f. id.
18480:teukså “girl, young female’. Cf. teuquio. (Norse type: touksàá) Norw. (landmal) taus, def: tausa; Norw. tós, Sw. tös, f. & n. ‘girl, wench’, (o-gde); Slovene Cuba, f. ‘heifer’; Blg. cf. (dim.) čuška, f. *cun- nus”. (Isophonic: Skt. Coksab, à, adj. pure)
18481:teukso, ið (1) ‘chatter, twaddle’ W cf. tuch, m. ‘grunt, groan’; Rust, s. “non- sense’; Li. Ciauksti, v. (1) “twitter; stammer”; cf. čiauškalas, m. ‘twittering; twaddle’ beside (o-gde) tauskiu, tauksti, v. ‘twaddle’
18482:teuksó, ið (2), see touks-. E-gde in MHG diusen, v. (lug, tousle; get muddled’; Blg. cuslja, v. 'shuck — grain’; Morav. Cz.
18485:teul- (1) ‘ball’. See next and toul- (1) & (2) Skt. cf. o-gde tolah, adj. ‘poised’; tolakalr, am, mn. (a weight); tolika, f. (*rampart'. See next); Br. tül, s. (“fistful”, also dül, id.); G Deul, m. ‘pig of iron (fr. *toulis); Slovene cula, f. ‘bag, bundle’; (LW in) Alb. cule, f. ‘bundle, trap- pings, chattels'
18486:teul- (2) ‘wrapping, envelope, husk’. Same as (1) (?). Cf. toul- Alb. cull, m. ‘blanket; W tul, pl. -ion, m. “envelope, shroud’; Latv. caula ‘shell, husk’; (z-gde in) Li. tüloti, inf. ‘wrap up, muffle'
18487:teul- (3) ‘docked, lopped, stunted' Oss. cula, Dig. cola, adj. ‘docked; inbent, dented'; Blg. čul, adj. “dockeared'; (LW in) Alb. cull, id. Cf. Skt. čolah “jacket?
18488:teul- (4) ‘swing, surge; verve, impetus’. Alb. sul, súlem, v. ‘attack; dash’; Cz. cf. čilý, Slovak čulý, adj. ‘lively’; Srb. culjati, inf. ‘swing, shake, rock, dandle’
18489:teum- (teumos, à, On, is) “pile, hill’. Cf. tum-, tumolos. (Alb. & Ir. ambig.) Alb. (ambig.) tum, m. "mound: Ir. (ambig.) tuaim, f. ‘mound’; G Dieme, f. and Diemen, wm. ‘rick, stack’; Srb. cuma, f. ‘pile’. (Iso- phonic: Ir. tuam, s. 'burdock ).
18490:teup- ‘move’ (?) Skt. (ambig.) čopāmi, v. id.; Cz. cupu, cupat, v. ‘tramp, dodder’; Srb. cf. cupnati, inf. jump’. (Isophonic: Pol. cupnac, inf. ‘crouch’, Li. am- biguously Ciáupiu, ti ‘squeeze, pucker’; čiau- pýtis, inf. “jib”)
```


### [2026-10-15T02:47:06.120Z] TOOL RESULT

```
# Etymology and Descendants of PIE *táwros

## Etymology
The word was "Borrowed from or into Proto-Semitic *ṯawr- ('bull, ox'), or both originated from a common unknown source." The unconditioned /a/ suggests a non-Indo-European origin.

## Key Descendants
- **Proto-Indo-Iranian**: *stáwras
- **Proto-Germanic**: *steuraz, *þeuraz
- **Proto-Italic**: *tauros
- **Proto-Hellenic**: *táuros
- **Proto-Celtic**: *tarwos

## Semitic Connection
The entry notes a potential connection with Proto-Semitic *ṯawr- meaning "bull, ox," though whether one was borrowed from the other or both derive from an unknown common source remains uncertain.
```


### [2026-10-15T02:47:08.542Z] TOOL RESULT

```
# Proto-Indo-European Root *tewh₂-

## Root Meaning

The reconstructed root *tewh₂- carries two primary semantic functions:

1. "to swell, grow fat"
2. "to become strong"

## Major Derivatives and Descendants

**Indo-Iranian Branch:**
- Sanskrit: tavīti ("to be strong")
- Old Persian: taumā ("strength, power")
- Avestan: tūtauua ("is possible")

**Greek:**
- Ancient Greek: etázō ("to test, examine"); sôs ("safe, healthy")

**Latin:**
- tueor ("to look at, watch over")
- tōmentum ("swelling")
- tūtus ("safe, secure")
- turgeō ("to swell")
- tuber ("swelling, tumor")
- tūrōs (related to cheese/τυρός)

**Germanic:**
- Proto-Germanic: þeudjaz ("favorable")
- Old Norse: þúfa ("mound")
- English: thumb (from *tuh₂-mō-)
- Related to "thousand" (from *tuHs-ont-)

**Celtic:**
- tusnā ("wave")
- tuaimm (Irish, from strength-related root)

**Balto-Slavic:**
- Proto-Slavic: tỳti ("to become fat")
```


## [2026-10-15T02:47:12.569Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"Per\\. [a-z]*\\(tob\\|tub\\|tōb\\|tüb\\|tobr\\)\" IEC.txt | head; grep -n \"^tu[a-z]*\\b.*Per\\.\" IEC.txt | cut -c1-300 | head"
}
```


### [2026-10-15T02:47:13.029Z] TOOL RESULT

```
19223:tübhor- ‘ball, bag’. Per. ambig., cf. tūpəlos Per. tübre, s. ‘bag’; (CW in) Tk. torba, id. (whence Slav. id.); Oss. (LW) dobra, s. (Cknap- sack’; fr. Per?);; Gk. süphar, n. ‘top skin, slough'; Lat. tüber, n. “lump, puffball
19329:tüpolos (tüpulos) ‘bulge; dolt'. Per. ambig. cf. tübhor- Skt. tüparáb, adj. ‘hornless; m. ‘hornless goat’; Oss. tuppur, adj. ‘bulging’; s. ‘bulge, hump’; Per. tübre, s. Chag LW in Tk. torba, id.); Latv. tüplis, s. *arse'; Slovene cf. tepec, m. (“blockhead”, fr. *tupiko-). (Isophonic (?) in Oss. tífil, Dig. tulfä, s. steam")
19212:tu, tū ‘thou’. (Oblique forms in Skt. & Olran.). WP I, 745 Per. tu, tü, id.; Oss. dí (by weak sentence position); Arm. du (W.S.P), id.; Tokh. A tu; B tuwe, twe; Gk. sú, Dor. tá; Osc. cf. tiu, tiium, id.; Ir. tà; W ti; Br. té; Cor. ty (W.S.P. sý, Ip = ÉD; Lat. tü; Go. bu, OE bú, MHG dü; ON bú; 
19250:tug- (tuo, ið) (2) ‘constrain; reinforce, strengthen” Skt. tujámi, tuñjámi, v. “impel'; tujáyami, intr. ‘hurry’; Per. tuzam, v. ‘plunder’; Ir. cf. co- thuighim, v. (rear, feed; W twy, m. "check beside denom. twyo, inf. id.; ON poka, tr. & intr. ‘move; alter’; mod. “edge forward, press on’; Sw.
19287:tulupos, å “lump, ball, mass, crowd’ Per. turb (‘radish’; LW in Tk. turp, id.); Gk. tolüpe, f. ‘ball of thread’; Alb. tulup, m. (‘col- lop of meat, spg. infl. by tul ‘lean meat, see tul- (4) beside tullupan, adj. ‘bald’); OCS tlüpa, R tolpà, Cz. tlupa “crowd, gang’; ambig. Ir. tola, gs. id., f
19300:tumo, eio ‘swell’. Cf. tumos, tumolos. WP I, 708 Skt. cf. túmrah ‘swollen’; Per. cf. tuman *my- riad’; Tokh. A tmān, B tumane & tmane, wd: Lat. tumeo, ere, v. ‘swell, increase; W tyfu, inf. ‘grow’; twf, m. ‘growth’; Cor. tevy, inf. ‘grow’; Li. tumü, eti, v. ‘congeal’; tumus, adj. ‘clotted’; tu
19301:tumos, à, ön), io ‘swell, lump, mass, myriad, crowd’. Cf. tuməlos, tumo. WP I, 708 Skt. cf. túmrah ‘swollen’; Per. tuman, s. ‘my- riad’; Tokh. A tman, B tmāne & tumane, id.; Ir. tom, m. ‘bush, knoll, lump’; W twf, m. ‘growth’; Cor. towan, pl. tewennow, m. ‘dune, hillock’; (*-ü- in) OE püma, wm
19308:tundō ‘strike, beat, shake, bang’. Cf. tud-. WP II, 618 Skt. tunde, mp., pf: tutudé "strike": tundami, v. ‘be active’; Per. cf. tund, adj. ‘dashing, violent; Gk. cf. Tundarídai (epithet of the twin gods of Thunder and Lightning); Alb. tund, v. ‘shake’; Lat. tundo, ére, v. pf: tutudi *beat'; Ir
19309:tundes ‘violent, bursting,  excrescent; docked, shortened, blunt’. WP II, 618 Skt. tundam, n. ‘paunch’; Per. tund, adj. *dash- ing, violent; Ir. tonn, adj. (Cagile', ambig. *tund- or *tudn-); f., pl. -ta wave; OW (am- big.) twnn, adj. (Cbattered', fr. *tund- or fr. *tudn-); W twn, adj. ‘fractu
19325:tuntoló (tuntuló, tuntlo) (2) ‘rumble, babble’. (Gk. Aib. type: tuntulaio) Gk. tuntlázo, v. ‘babble’; Alb. tunduliloj, v. ‘shake, rattle, dash’. Nominal types: Per. am- big. tundar ‘thunder’. Cf. Gk. túntlos, m. ‘twaddle’
19390:tuako, io (tuaks-) (1) ‘do, make, perform’. (Variant taks-) Skt. tváksami, v. “create, produce’; Av. OWaxS-, v. id.; Ober cf. taxi-, v. ‘be busy’; Per. cf. saxtan & sazidan, inf. ‘make’; Lat. facio, -ére, v.; OLat. fut: faxo; and pf: fhefhaked, 3s. “make, do’; cf. factus, gs: factüs, m. (“make
19473:tuengh-, tngh-. (Slav. ambig. Gk. from a var- iant of type *tung-) (?) Per. sanjidan, inf. ‘weigh’; cf. sangin, adj. (Q) ‘heavy’; sang = (stone); Gk. sátto, v. ((1) “load”, if < a variant: *tung-?, but cf. Hes. sákhma, n. load"); Lat. cf. fungor, -gi, dep. (suffer. Cicero); ON cf. þyngja, v. t
```


## [2026-10-15T02:47:21.573Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 517 526 550 1102 1362 2138; do echo \"######## BQT:$p\"; timeout 300 python3 tools/ref_page.py BQT:$p 2>&1 | head -80; done 2>&1 | cut -c1-300",
 "timeout": 600000
}
```


### [2026-10-15T02:47:33.496Z] TOOL RESULT

```
######## BQT:517
no scan of BQT covers printed page 517 (see 'scans' in refs_online.json)
######## BQT:526
no scan of BQT covers printed page 526 (see 'scans' in refs_online.json)
######## BQT:550
no scan of BQT covers printed page 550 (see 'scans' in refs_online.json)
######## BQT:1102
no scan of BQT covers printed page 1102 (see 'scans' in refs_online.json)
######## BQT:1362
(no exact page map; using offset -1205 -> pdf page 157; check the printed number and re-run with --pdf-page if off)
REF: BQT:1362  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 157  OCR-lang: fas

له ماضا
طیسه - بفتح اول رسین بی‌شطه ‏ بتر | افروز باشد؛ وبستی تشم بستان افروژرا گفته‌اند.
طیطان - با طای حطی تابی بر وزن | راکویند که عربان وخطیبان بردوش‌اندازند ۷ .
گیلان » بلفت سربانی کندای صحراییراگویند طیلسان همزعفر - کنابه از عماع
۱ طیطاق ؟ - با طای حطی بروزن تبهوه طیلسان مطر۱ ۸ - کنایه از غب
لوعی از مرغابی باشد؛ وطیتو نیز گفته‌اند که‌طای | است که بعربی لیل خوانند.
دوم تای قرشت باشد .۶ طینوث < بفتح اول وسکون نای‌ونون
طیفور ۴ - بنتح اول وضم فا بر وزن | بواوکشیده وبثای مثلثهٌ زده , حیوانی پاشساشد
دیجور , مطلق پرنده راکوبند اعم ازمرغ وملخ | ذراریح لیکن کوچکتی ازوست وقمل ذراریح ازو
وامثال آن: ميآاید و ذراریج جانوری است از هگی‌بزر کتر,
طیقّی ؟ « با ارل وقاف هردو بتختابی | وعروسك همان است .
کشید., حبی باشد سرخپرنگه مانند سماق‌بندادی طبور سد‌ره - کنایه از فرشتگان
و بع ی گوبند حب بلان است. آسمان باشد ‎٩‏ .
طیلافیون * - بنتح اول و سکون طبهوج - با جیم ‏ معرب تیهو ۱۰
ثالی و لام الف وفای مفتوح وتحتائی بوا و کشيده | است, وآن مرغی باشد شبیه بكبك لیکن‌ا ز كبك
بنون زده ۰ نوعی از رحی‌المالم است که بستان | کوچکتر است .

۹ 007۲63 (فر) « لك ۷س4۲۱؛. ۲ سلطوی * نیتو » از سانسکریت
بیپلوی, وارد زبان مزبور شد: ودرفارسی بصورت نیتو درآمد : « تبتو » مرغ آبی است » رودکی
( سمرندی ) گوید 3
مبدالحمید ( چاپ‌چهارم قریب ص۷٩)‏ « طیطوی » آمده ورك: حياة لحیوان‌دمیری : طیطوی.

۴ - (عر) «طیفور , طائرصفیر» « اقرب الموارد . ۴ - مصحف « طیفی ‎ »‏
‏42 8ط170 :4 ۷ س 4۹۱؛. ۵ س رتم1616 (لاینی)«لكس ۰.4۲۰
‎٩‏ - «طیلان بالفتح وتئلیت‌اللام » چادر. معرب است اصله (تالغان) «منتهی‌الارب».
بقول ادی شیر و «ممیار» کلمه معرب « تالان » بکسر لام است . رك : المعرب جوالیقی ص

۷ متن وح .
۷ - بدل سازم بزبار و ببرنی ردا و طبلسان چون پور سقا .
« خاقانی شروانی ۲۲
۹ < 0070۲15 (فر) «لك ص۲۰ 4ور4 : نیهو: «وبهتر وزودگوارتر کوشت‌ما کیاست
* طیطوی - رك : طیطو .

######## BQT:2138
(no exact page map; using offset -1917 -> pdf page 221; check the printed number and re-run with --pdf-page if off)
REF: BQT:2138  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 221  OCR-lang: fas

دغاه -۱۳۸-
ستردن است که گل درین باشد » و بر وزن | برس کوه:ازچوب وعلف سازند ‎٩‏ - ومطلق سایه
نستا سابة کلاء هم بنظر آمده است ؛ و بمعنی سایبان
ملک < بکر اول بر وزن خعتك . هم بر ان ی 7
مطلوح پاراگ پیجیده را گوبند ۱ ای بزبان عربی کرکس باشد۷ وآن پرنده‌ایست
و ستیزنده و جنگه آور و ستیهنده - و بد فعل شود در یکروزیمغفرب رود و باز از مغرب پرواز
۰ : کند و بلند شود درهمان روز بمشرق آید ۸ ؛
ومخاصمت نمودن عاجز شود وشگه یاید وروی :
نگرداند - و نام پپلوانی‌هم بوده ابرابی ۴ .4
۲ ستاره ات در فلك موسوم پنسر طایر ونر
نستهن ه با ها بروزن نترن » دم واقع ۷ .
کش هرد - بفتح اول و ضم رای قرشت
لصتوهی " « با ها بر وزن رقسیدن » | راگونند ‎٩‏ وبفتح اول وضم‌انی ویضم اول‌وئالی
دوازده رخ بر دست یبیج ن کشته شد . لُحر6 - بر وزن همدم . نام بتی است
هر - بفتح اول و ثالی بر وزن سفر » | جورت زلی در بتخانةٌ بامیان نزديك بسرخ بت
بمعنی دار باشد و آن جایی است از کوهتان | و خنگه بت؛ واورا ستواهم میگوبند با سین بی
۹ - بعمین معنی در رشیدیآمده . ۴ - لغة ختگی ناپذیر , ناافتاده « بوستی.
نام نامه س ۲۲۹ > ضد « ستوه > (ه.م.) و ۶ بستوه » ؛ و اسم معتی ( حاصل مصدر )آن ستوهی
(«.م.) است. « نستوه » ستیپنده باشد درسخن وکارها . رودکی ( سمرقندی ) گوید :
۰ لغت فرِعّض ۰۹۸۵۰
۴ - ر4 : فهرست ولف , ورك : بوستی . نام نامه ص ۲۲۹ . :
۴ - ر4 : ستیهن . 8 - رك : فپرست ولف. ‎٩‏ - مخقف «بار» (ه.م.)
۸ اقانه ات . ‎٩‏ - جپانگیری بدون شاهد بهمین معنی آورده .
سپاهی با شگفتیها ودستانهای کو»ا کون زستوعی فزون ازحد » ز البوعی قرون از هر .
معزی لیشاپوری ص ۱۹۹ *.
(برهای قاطع ۲۷۰)
```


## [2026-10-15T02:47:39.720Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for pp in 154 155; do timeout 300 python3 tools/ref_page.py BQT:1362 --pdf-page $pp 2>&1 | grep -n \"طهماسب\\|تهماسب\\|^REF\\|۱۳۶\" | head; done; grep -n \"BQT\" data/verification/sources/refs_online.json | head -3; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False)[:800]); print(d['BQT'].get('lookup_hint','')[:1200])\"",
 "timeout": 600000
}
```


### [2026-10-15T02:47:40.477Z] TOOL RESULT

```
1:REF: BQT:1362  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 157  OCR-lang: fas
1:REF: BQT:1362  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 157  OCR-lang: fas
2: "BQT": {
6:  "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
8:   "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt",
[{"volume": "3", "file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-10-15T02:47:44.621Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"طهماسب\\|طهمورث\" incoming/BQT/BQT_v3_pages.txt | head -5; for w in \"توان -\" \"تند -\" \"توبره\" \"تهماسب\" \"تخم -\"; do echo \"== $w\"; grep -n \"$w\" BQT_v1_pages.txt | head -3; done; for w in \"ستوه\" \"ستور -\" \"ثور -\" \"ثور\"; do echo \"== $w\"; grep -n \"$w\" BQT_v2_pages.txt | head -3; done"
}
```


### [2026-10-15T02:47:45.116Z] TOOL RESULT

```
11564:طهمورث ۴ ‎ie‏ پادشاهی بود از
11605:‏9 در ‎ULL‏ صفویه دوپادشاه این نام داشتند : شاه طهماسب ‎ols ja Syl‏ اسمعیل اول
11607:‏(۹۸-۹۳۶).طهماسب _دوم‌پسرشامسلطان‌حسین (۱۱44-۱۱۳۵) .
11622:‏شاه طهماسب اول
43434:‏طهماسب ؛ تلویکی از اجداد رستم زال ات واو | سرعست » رستنيی باشد خود روی شبیه باسفناج
== توان -
== تند -
1281:از متفرعات لهجهُ اورامانی هستند - فعلا بطور رسمی وجود ندارند و تفریبا از بن رفته مصوب
12183:میکفتند - و بمعنی قدرت حق و لطف یزدان‌هم
16292:چشم باش د که بعربی اعور خواتند - و کنابه از
== توبره
== تهماسب
== تخم -
== ستوه
33781:‫ْم اول بروزن گروه «ممعنی‬      ‫ستوه ‪°‬‬
33799:   ‫پازید ‪ . 210005‬ایرای باستان ‪ 6 ۹۱ -۲۵۷۵-‬از‪‌۷‬ها ( نوانستن » فادر بودن ) » ستوه فارسی‬
33801:            ‫ور کے ‪ :‬استوه ‪٠‬‏ ضدآن ‪ :‬دتوه (خستگی ایذیر) مخفف آن «سته» («‪.‬م‪.).‬‬               ‫تبرکه ‪۸‬‬
== ستور -
== ثور -
== ثور
4162:                                           ‫باشد ‪.‬‬        ‫دانثور ‪ ,‬خصی رگاوبن که خرامان و از روی‬
4247:                            ‫و)‬‫بثور‬
9100:     ‫بودن بدن با بعض بثورات حاصل میشود‪ .‬این‌ککلمه هم لازم استممال شود وهم متعدی‪ .‬بمعنی‌لازم‪:‬‬
```


## [2026-10-15T02:47:47.236Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 33790,33802p BQT_v2_pages.txt; sed -n 11600,11625p incoming/BQT/BQT_v3_pages.txt; awk 'NR<11605 && /\\[pdf page/{l=$0} NR==11605{print l}' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-10-15T02:47:47.765Z] TOOL RESULT

```
    ‫ججانور‪ ,‬چلریا » دواب)«هوشمان*‪۷ ۲‬؟‪.‬‬       ‫فی‪ :‬افغالی ‪۲‬‬
                                                        ‫حیوان خانگی عموما) «اسشقق ‪٩۲‬‏ ‪۰ ۷٩‬‬
    ‫کث‪ :‬مقدمه‌ص نودودو‪ = .‬اشنیجه = شهمیرزادی ‪asînhso‬‏‬        ‫‪)...‬ر‬     ‫‪ - ۴‬محف سلوسه» ‪E‬‏‬
   ‫[رك‪ :‬اعنوشه]‪.‬درلهج توش[ باکداشان‌چنانکه آ قایرضاتابش نوشته ند‪:‬هاشنشه» بمعنیعطهمتعمل‌است‬
    ‫نگلو‪-‬اکسن‬    ‫وااسهمرا‌ابصنکولتمهاست‪.‬قس‪:‬ا لگلیسی ‪.828808‬انگلیسی میانه‪5 06560‬و ‪1165604۰‬‬
   ‫‏‪ gfnêsan‬ر ‪« 02906۵0۲‬لغت بین‌المللی جدید وبسترسال ‪٤۲۹۱٩‬‏ ‪ .‬امادربارتمصراع‌رود کی(چنان‬
    ‫چون دردمندان را شنوشه» دراینجا همبمعنی عطسه امت چه درطب قدیم در امراض دماغی عطسه‬
     ‫‪ - ۴‬پهلوی ‪28005‬‬                 ‫ژدن رابرای تداوی امراش دماغی و زکام مفید مدانتند ‪.‬‬
   ‫بی‌زور) ‪.‬‬ ‫(‬ ‫‪۷‬‬ ‫‪2‬‬ ‫‪0‬‬ ‫‪5‬‬ ‫ی‬ ‫و‬ ‫ل‬ ‫ه‬ ‫پ‬ ‫‪-‬‬ ‫®‬      ‫ممحنی قله درخت است ی تاوادیا ‪ 9۹۰‬ور کف ‪3 :‬‬
   ‫پازید ‪ . 210005‬ایرای باستان ‪ 6 ۹۱ -۲۵۷۵-‬از‪‌۷‬ها ( نوانستن » فادر بودن ) » ستوه فارسی‬
   ‫مر کب امت از ‪ 2 82۳12۷20-۹۱ :‬قی ‪:‬کوناه ( ه‪.‬م‪ ( ).‬آنکه زورش کم است)‪ .‬‏ رکه ‪:‬‬
            ‫ور کے ‪ :‬استوه ‪٠‬‏ ضدآن ‪ :‬دتوه (خستگی ایذیر) مخفف آن «سته» («‪.‬م‪.).‬‬               ‫تبرکه ‪۸‬‬
                                                                    ‫‪ #‬ستون ‪-‬‬

‏طیسقون ۲ - بتتم اول و سن‌بی‌قطه
و قاف بر وزن برعلون » دام شهری است در
‎ol yl‏ زمین وآن پای نخت پادشاهان ابران‌بوده.

‏9 در ‎ULL‏ صفویه دوپادشاه این نام داشتند : شاه طهماسب ‎ols ja Syl‏ اسمعیل اول

‏(۹۸-۹۳۶).طهماسب _دوم‌پسرشامسلطان‌حسین (۱۱44-۱۱۳۵) .
۴ تهموری ‎Cen)‏ ۴ - (عر) « طیاره کجباله ,
‎ET‏ سربم و نیزرو» «منتهی‌آلارب؟ -کنایه از اسب تند رو :
طیارة تند را شتابان میراند چو ‎ob‏ دربیابان.
نظامیکنجوی.* کنجیته ‎NEY‏
‏- در زبان کنولی ( عربی و فارسی ) مر کب هوابی را کویند »

‏هواییما. ۴ - در(عر) ‎ont‏ معنی‌طیف (بفتح اول) است .
رك: اقرب الموارد ؛ منتهی الارب . ‎٩6‏ -(عر) ‎anh?‏

‎sql‏ سیبکی» «منتهی‌الارب ‎٩‏ , خفت:
دز چرز ‎Bb‏ عقل است : دم فروستن

‏بوقت کفتن و کفتن بوفت خاموشی.« گلستان ‎.۰٩‏

‏شاه طهماسب اول
۱ -«ضرب امیر را ‎oy‏ احتباط کرد و بینداخت تا سه‌شش زندسه‌يك بر آهد » عظیم

‏طیره شد و از طبع برفت و جای ‎OT‏ بود و ‎OF‏
[pdf page 156]
```


## [2026-10-15T02:47:52.642Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<33799 && /\\[pdf page/{l=$0} NR==33799{print l}' BQT_v2_pages.txt; awk 'NR<43434 && /\\[pdf page/{l=$0} NR==43434{print l}' incoming/BQT/BQT_v3_pages.txt; sed -n 11560,11570p incoming/BQT/BQT_v3_pages.txt; grep -n \"ستور\" BQT_v2_pages.txt | head -5; grep -n \"‫توان\\|توان ‪-\\|توان -\\|^.\\{0,30\\}توان\" BQT_v1_pages.txt | head -5"
}
```


### [2026-10-15T02:47:53.955Z] TOOL RESULT

```
[pdf page 593]
2۱۳۹۱۳

بخشید و پنجاء سال پادشاهی کرد ۷ .

طهمورث ۴ ‎ie‏ پادشاهی بود از
بیرهای هوشنکه . کوبند ابلیس را م کوب

ob

ساخته ‎oy‏ و سوار ميشد و مدت پادشاهی او را

168:‫جمع در ز بان فار سی ‪ .‬محمد معین (طرح دستور‬                             ‫‪ .‬قاعده‌های‬         ‫‪۲‬‬
402:                             ‫آن برآید ‪.‬‬          ‫وموبدان و دستوران وهیربدان شده باشد گرفته‬
860:                                                ‫و دستور بودش ( دارای سوم را( رامی دو هرد‬
2072:‫آن روغن ستور همچو روغن اسب و شتر و کاو‬                                 ‫واو را اخار بر وزن بخار کودند ‪.‬‬
2098:  ‫ز؟ ولی درعربی خاصة بمعنی پوشش ستوراستعمال شده ‪ .‬د جل‪ ,‬صم و بفتح اول‬            ‫ص ‏‪ ٩۲‬وبص‬
388:بردند » دیگر کسی نتوانست آن‌را بخواند » جزمشتی ژردشتیان. نا گزبر آنچه
1224:نتوانستندی آهوختن... > ۱ تار یخ بخارا ایضاً س ۵۷.
1378:بدو دستهٌ شرقی و غربی میتوان تفسیم کرد که از نظر علم اصوات ؛ شکل
1607:توانگر >.
2021:بسیارجالب می‌توان تقسیم کرد : نخست فرهنگ نویسی برای زبان تازی
```


## [2026-10-15T02:47:58.071Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk '/\\[pdf page 593\\]/{f=1} f' BQT_v2_pages.txt | head -70 | sed 's/\\xe2\\x80[\\xaa-\\xae]//g' | cut -c1-250"
}
```


### [2026-10-15T02:47:58.557Z] TOOL RESULT

```
sed: -e expression #1, char 24: Invalid collation character
```


## [2026-10-15T02:48:00.728Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk '/\\[pdf page 593\\]/{f=1} /\\[pdf page 594\\]/{exit} f' BQT_v2_pages.txt | python3 -c \"\nimport sys,re;t=sys.stdin.read();t=re.sub('[‪-‮‎‏]','',t);print(t[:6000])\""
}
```


### [2026-10-15T02:48:01.175Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:48:03.612Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"pdf page 59[234]\" BQT_v2_pages.txt; sed -n 33730,33800p BQT_v2_pages.txt | python3 -c \"\nimport sys,re;t=sys.stdin.read();t=re.sub('[‪-‮‎‏]','',t);t=re.sub(' {3,}','  ',t);print(t)\""
}
```


### [2026-10-15T02:48:04.055Z] TOOL RESULT

```
  دلیر و ستنبه هو کینه کاه.  -ازابرانیان بد تهم کینه‌خواه
  فری . 6° 14  لفت
  فردوسی طوسی .

  ومخفف «رستخضیزز» = رستاخیز (هدم).  مصحف  ۳  !سبنج» (ه.م. ).  سحف
  م¬۳

  سومین از ثلیث  .مصحف سوا 4۷1  ظ  -  ©  ستار ' ستاره .  ر :4ستا  -  ۴

  رکه  :استوار .  -  (خدابان) هند » پرورد کار مخرب و فراوالی همت .
  - 4امروز بدرجه ای بظامی اطلاق شود که شامل سفرنبه  رکه  :استوان .  ۷

  است  :ستوان کم (فایب‌اول) .ستوان دوم (دایب دوم) » ستوان سوم (دایب سوم) .پابین ترازستوان.
  رکه  7اسنودان ۰  - 4  سوم «استواریکم» است و بالاتر از ستوان یکم «سروان» .
  آین جهان چون تاکردون گردان‌شد.  - ۰۷هرده لشود زاشه.زلده بتودان شد

  رود کی سمرفندی« .لفت فری. > ۹۵۳
  imoats ۰ (مدح کردن e تمجید کردن)؛بهلوی 22  " ۳اوستا رشة = ۲211

  هندی باستان ربهٌ ۷-هن , 9ا8ا  ,استی  ( 18'8مدح کردن » تمجید کردن) و 00119
  و ( 45مدح » ستایش)  ,افغانی ع [ , 871808وخی  » 078-005شفنی وسربکلی "اشنا
  ا:بیدن » ستاش .
  سرتکه
  دعق  ۹۱۲۷6و رکه  :ببرکه : ۷۰۲لاو .
 ==  سوه

وزن کبوتر » هوابی باشد با صدا که بی‌اختیار از  یمعثی وصف نمودن وستایش کردن باشد؛ وبضم
  راه دمام بجپد وآارا معربی عطه خواند.

ستوسه  = ۴بفتح اول و سین بی لقطه  رزن
  بو  اول  ستو ده  ۱ه یکر
 بورزن دبوسه ؛ بمعنی ستوسر است که عطسه  باشد سنتی  شنه  کرده  قروده » سمعنئی مدح
  باشد ۷#.
  او را  یکریی  و  کنند  مدح  کسی که اورا

 ستو نه د بکر اول و فتح نون بروزن  .  ْف
انداز  و  و ری  کردن شاهدن  چمگونه  ,حمله
  خم ول بروزن حور » هر  ستور ؟
 لمودن باز و باشه و امثال آن باشدبجانب باولی»
  جاور چارپابیرا ۳عموماً واسب و استروخر
و باولی جانوری راگوبند که بعضی ازپروبال او
 پدیرش باز شواهین نو رسالیده
  کنده باشند و
و نازه مشکار درا ورده سردهند îl بآٌسالی بگیرد  ستوردن = بکر اول بمعنی ستردن
  -بمعنی کریز و کریختن‌هم آمده است‌وبمربی
  و  است که تراشبدن وحك لمودن وباك کردن‌باشد؛
  اس  رب  اول هما مده است  وم


ْم اول بروزن گروه «ممعنی  ستوه °


  اسزتو«دن».  ول
  ف اعسم
  م-٩
  ساسکرت  - ۳پهلوی( 605 ۲اسب) اوستا« 83۲0815--بارتولمه ۱6 ۰۹۵لجر گ۸۰۲
  ( 01711201)5-بار اسب .بار ورزاو) » استی ( 316۳005حیوان خانگی)» کردی‌زازا ع.۲۵158شغنی
  , ۲سریکلی 8 ۲0148و( ۲041حیوان بارکش » ورزار یالغ) » بفتوبی  ۲0/۱5گ(وسفند »
  ججانور ,چلریا » دواب)«هوشمان*۷ ۲؟.  فی :افغالی ۲
  حیوان خانگی عموما) «اسشقق ٩۲ ۰ ۷٩
  کث :مقدمه‌ص نودودو = .اشنیجه = شهمیرزادی asînhso  )...ر  - ۴محف سلوسه» E
  [رك :اعنوشه].درلهج توش[ باکداشان‌چنانکه آ قایرضاتابش نوشته ند:هاشنشه» بمعنیعطهمتعمل‌است
  نگلو-اکسن  وااسهمرا‌ابصنکولتمهاست.قس:ا لگلیسی .828808انگلیسی میانه5 06560و 1165604۰
  gfnêsanر « 02906۵0۲لغت بین‌المللی جدید وبسترسال ٤۲۹۱٩  .امادربارتمصراع‌رود کی(چنان
  چون دردمندان را شنوشه» دراینجا همبمعنی عطسه امت چه درطب قدیم در امراض دماغی عطسه
  - ۴پهلوی 28005  ژدن رابرای تداوی امراش دماغی و زکام مفید مدانتند .
  بی‌زور) . ( ۷ 2 0 5 ی و ل ه پ - ®  ممحنی قله درخت است ی تاوادیا  9۹۰ور کف 3 :
  پازید  . 210005ایرای باستان  6 ۹۱ -۲۵۷۵-از‌۷ها ( نوانستن » فادر بودن ) » ستوه فارسی
  مر کب امت از  2 82۳12۷20-۹۱ :قی :کوناه ( ه.م ( ).آنکه زورش کم است) . رکه :
```


## [2026-10-15T02:48:09.594Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BQT_v1_pages.txt').read()\nt=re.sub('[‪-‮‎‏]','',t)\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for w in ['tuvân','tuwân','tuvan','tund','tōr','tuxm','tubra','ثور','tavân','tuban','tuvān']:\n        if w in p:\n            j=p.find(w); print(i, w, repr(p[max(0,j-300):j+200])[:600]); \nE"
}
```


### [2026-10-15T02:48:10.419Z] TOOL RESULT

```
73 ثور 'عید عبدالبلك\nاصمعی متوفی\u200cدر۲۱ و کتاب\u200cالامتالو کتاب\u200cالاجناس من کلام| لعرب ومااشتبه\nفی\u200cاللفظ واختلف فی\u200cالمعنی ورسالة فی\u200cما ورد من\u200cالقر آن الکریم من\u200cلغات-\nالقبایل هرسه تا یف ابوعبید قاسم بن سلام هروی متوفی در ۲۲۳ و کتاب\nاسماه خیل! لعرب وفرسانهاتالیف ای \u200cعبداله محمدین زیادالاعرابی متوفی\u200cدر\n۱ و کتاب الماثور تألیف ابوا لصمیثل عبدالّین خلید اعرایی رازی متوفی\n۰۷ ۵۰۵۰ -آين ردایت خلاف فول جمهود است . دد تملیتات پایان جلد چهادم\nدرین مورد توضیسی بقلم آقای دکتر سید جعفر شهیدی درج ثنه .'
350 ثور 'کروة\nاسکندر در کنار دربا بسرحد فرنگه .\nاسکنك بکر اول وثالك وفتح نون\nبروزن هتركك . بممنی اسکنه\u200cباشد وآن\u200cافزارست\nحرودگران را\nاسکنه - ممعنی اسکناك است که افزار\nدرود گر ان باشد ویعریی بیرم خوانند .\nاسکیز ۳ بکراول وتات وسکون\u200cتانی\nیی\u200cاز حرکه اسکنهر» اسکندروی\nره\nوتختانی وزای\u200cهوزء برجتن\u200cوآلبزوجفته انداختن\nسثور باشد .\nاهکیژ ه » ر وزن استیزه » بمشی\nاسکیز است که برجمتن و آلیز انداختن ستور\nباشد . "\nاسلنج بفتح اول ولام بروزن\u200cشطرنج:\nتوعی از لحیةالتبس است که آنرا ذنب الخیل\nنیز خوانند . ورم جگی و امشقا را تافع '
510 ثور '٩ . و چرن واضم\nاو ساخته فراخانی حفگفعد ور اکتون خنایی۱\nانداخته\u200cاند (۱) و بفراعی خوانند  #\nیشور ب بنتح اول بروزن محثور . نام\nفربه است سان سرخس و هرات ۴ ۰و ممتی\nنی کیبی آن بغ\u200cشور است که کوآب شورباشد چه\nعم بمعنی کودال است ۲\nبفطاق » با طای حطی بروزن چخماق,\nکلاه و فرجی را گویند\nبقل « بفتح اول و سکون ثانی و لام »\nنام _'
542 ثور ' . - بهلوی\n۵ « تاوادبا ۰۱۵4 < اونوالا ۳۸4» رك : آمی و فرهنگه روستابی ۲۵۹ وگل کلاب ۷۲۷- نیز\n» پپلوی )۳2, ابرانی باستان ۰۳241 اوسنابیُ]]۳8» بارسی\u200cباستان۳2)1\n« بارتولمه ۳۲۲ 4 . بازند ۳2 . پهلوی تورفان 02010 « یبر گه ۱۷۸ ».\n۴ هن فری ات تیاه یه فشده.. ها پیلور\nو5 دلرسی باستان 2 -1۱:۲8 * اسفا ۱: ۲ ص۲۳* ( ثوره واهره ماه دوم\u200cهضامنشی .\nرك : دوازده ماه هخاهنشی بقلم نگارنده .آموزش ویروری سال 46 شمار؛ ۱ ص ۸ ۰ )» کیلکی\n۳ «: فرب زندی و برنی 26192۲ « 2 . ۱ ص ۲۸4 ۰ سمنانی 9812۲ ری\n۲فت ۱ سرخه 24 294 . لاسگردی ۳ '
609 ثور ' فرشت زده ۰ نام گیاهی است که خلاشةآن\nباريك وسیاه فام وب رکه آن سبز رنگه می\u200cباشد\nو پیشتر در گوشه و کنار حوضها میروبد و آنرا\nبمربی شمرالجن ولحیةالحمار خوانند- وشکلی\u200cرا\nیز گویند از اشکال فلکی متمل بر ست\nونه ستاره هورت عردی برپای ایستاده وسرغولی\nدردست آ و یخته\u200cو آ نرا رأس\u200cالفول خوانند و کوا کب\nآن\u200cدربرح ثوراست باتفاق ارباب رصد ودر زبجات\nو کتاب صور کوا کب باین\u200cمنی برشاوش نوشته\u200cاند\nبا بای ابجد و بجای حرف شثالث شین فرشت\nوبحذف بای حطی » ال اعلم۴ .\nپرسیاو شان ا بالف ونون بسنی\nاست که کیاهی باشد دوابی» اکر\n'
618 ثور ' بهلوی آن باشد-\nواستادان بزاز اسباب د کان خود را در آن هند\nو با دبسمالها بندند - وبضم ثانی وسکون ثالث\nورابع جم آمفه است* .\nبر وه « بفتح اول وثالث بر وزن\u200cمروه .\nهر چیز که در ناخت وتاراج » وجنگ\u200cوشییشون\nاز دشمن بدست آیدا" - و بممنی چادر شب عم\nآمده است - و پروین را نیز گویند, وآن چند\nسناره است در کوهان ثور۷ .\nپروهان > باهای\u200cهوزبروزن\u200cخ رکمان,\nبمعتی ظاحر وآشکرا باشدش .\nپرو یز ٩ با بای مجهول بر وزن\nشبدیز ۰ بمعتی مظفر و عتصور و سعیدب و عزیز\nاشکنان.« لت نامه ».\nگل بروند دسته بمته مود\n۴ - بده فرسنگه شرقی '
758 ثور 'وولابت\u200cتورانرا نیز گویند؟ .و به\u200cمنی\nدلاور و پهلوان وبهادر هم هست؟ او فرل اف\nکون د که نقیض تاجيك استه - وبمعنی تفحص\nمی\u200cباید .\nودرا ۲ « بنم اولرنانی مجپوذبرءزن\nحورا » بلغت زند و پازند(۱) کاو را کونند که\nبعربی مقر خوانند .\nتودان* « نام ولایتی\u200cاست برآن طف\nآب آمو یمنی ماوراء\u200cالنهر وچون این ملك را\nفردون بثور پسر بزرکك خود داده بود بتوران\nموتوم حه:\n(۱) چك: ۳ وماژند.\n۱ -وگروه وجمعیت (ازمردم). .در اوستا 1062 بپیأت\u200cصفت نامقوم تورانی است»\n2 نیزصفت است بمنی\u200cمتماو بتوران, تورانی. کلمه\u200cنوره رایمعنی\u200cدلیر ویهلو'
```


## [2026-10-15T02:48:15.253Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BQT_v1_pages.txt').read()\nt=re.sub('[‪-‮‎‏]','',t)\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for w in ['توان ','تند ','توبره','تخم ','تهماسب']:\n        for m in re.finditer(re.escape(w)+'[^\\n]{0,15}(بر وزن|بروزن|بفتح|بضم)',p):\n            j=m.start(); print(i, w, repr(p[max(0,j-100):j+500])[:700]);print()\nE"
}
```


### [2026-10-15T02:48:15.661Z] TOOL RESULT

```
746 تند  'ن ب رکه از مبان\u200cآن\u200cبر آبد۴ -و زبود\nسرخ رالیز کوبند , و بمعنی اول بجای\u200cدال ایجد\nزای حوزعم آمده\u200cاست ۰\nتند ید۴ س سم اول بروزن جتبید »\nماضی تندشدن ودرخشم\u200cرفتن باشدیمنی تند گردید\nودر خشم شد وغنچهوب رکه وشکوفه برآوردن\nدرخت را نیز کوبند " چه ه رگامدرخت شروع\nدر ب رک وشخوفه برآوردن کند کویند «نندید»\nبعنی پر گه وشکوفه بر آورد .\nنند یدن س چم آول بر وزن جنبیدن»\nمر زدن غنچه وب رکههرشکوفه باشد از درخت-\nاوقم هداج ای کدرا مد گرد\nوبه\u200cنی اول بفتح اول هم بنظر آمده\u200cاست.\nلندیسی * » بر وزن تسدیس » بمعلی\nتن مانند است چه دیس بمعنی مالند باشد -\n)٩( چش: وبمعنی.\n(4) چش: نسح .\n۴ راه: تندیدن.\nاي سح\nو بمستی\u200cصورت وئمثال - و'
```


## [2026-10-15T02:48:19.524Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BQT_v1_pages.txt').read()\nt=re.sub('[‪-‮‎‏]','',t)\npages=t.split('\\f')\nfor i in [745,746,756,757]:\n    p=pages[i]; print('=====',i, p[:80].replace('\\n',' | '))\n    for m in re.finditer('(تند|توان|tund|tuv|twn|tav)',p):\n        j=m.start(); print('  ..',repr(p[max(0,j-150):j+250]))\nE"
}
```


### [2026-10-15T02:48:20.095Z] TOOL RESULT

```
===== 745 زند ۱ - چم اول و سکون انی و دال | سوق نت کا مرلین مامت ردر چم | که از جای برجهد و جه
  .. 'زند ۱ - چم اول و سکون انی و دال\nسوق نت کا مرلین مامت ردر چم\nکه از جای برجهد و جهنده باشد . و خشم -\nو خشمکین و نحنبناگ ودرشت - وتواناء و قربهرا\nنیز گویند. وبمعنی غرل ییابالی ودبو هم هست-\nوس رکوه را نیز گفته\u200cاند - و بمعنی بلند وبلندی\n\u200cم آمده است.\nتنل بار آه تند معلوم بابای ابجد بالف\nکلبده و برای قرشت زده » موذباث را کوشد\nمانتد شیر و پلنگه و مار و عقرب و زنبور\n- ومورچه وامثال آ'
  .. 'ن و نحنبناگ ودرشت - وتواناء و قربهرا\nنیز گویند. وبمعنی غرل ییابالی ودبو هم هست-\nوس رکوه را نیز گفته\u200cاند - و بمعنی بلند وبلندی\n\u200cم آمده است.\nتنل بار آه تند معلوم بابای ابجد بالف\nکلبده و برای قرشت زده » موذباث را کوشد\nمانتد شیر و پلنگه و مار و عقرب و زنبور\n- ومورچه وامثال آن- وهرجانوری که جانوردبگررا\nشورد.\nند بود - بنم بای ابجد و سکون\nواو مجهول و رای فرشت » جستن و برجتن رآ\nگونند» و باین معنی بجای بای'
  .. '» جستن و برجتن رآ\nگونند» و باین معنی بجای بای ابجد بای حطی\nاههد سح\nتنلیر 5 عه بضم اول وفتح ثالك وسکون\n۱ -اوستا ۷2۵۸ ه (ه . 2)۷29۵6) ,از ربشة 4۵۷, فس: توان (تواستن) «اسفة\n۵ هرب انرابطةٌ *نند»رابا «نوان» ممتقدنیست «هوبشمان ۳۹۵ اورامانی00) «ل . اورامان\n۷ سننانی 00 ۰ منکری و سرخه و لاسکردی 10۳0 , شهمیرزادی لا « ۵ . ۲\nص۱۹۹ .گیلکی ۱94 . ۴ فرهنگ دساتیر ۷4۰ .\n۴ - قس: ریش هشدی\u200cباستان 20], 180201 ( صدا پیجی'
  .. 'ویند خصوصا " و نم ثالث هم آهده\nاست - و بلبل را ی زگوبندکه عربان عتدليب\nخوانند ۴ ۰\nلین در دادن عم کنابه از راضی شدن\nوقبول کردن باشد . 3\nلنفد و - بروزن تندخوه بخیل ومسك\nوترش\u200cروی را گویند . 1\nفندس *ه بفنح ثالث بروزن هر کس ۰\nبمعنی\u200cتن مانند است چه دی بمعنی شبیه ونظیر\nومانئد باشد - ونفیر ثمثال هم هست- و بکس\nثالث مخفف تندبس است که آنهم تن مانند باشد\nچه دبس بمعنی شبه ونظیر ومانند بود .\nلندسه » بنتع تالث ب'
  .. 'مسك\nوترش\u200cروی را گویند . 1\nفندس *ه بفنح ثالث بروزن هر کس ۰\nبمعنی\u200cتن مانند است چه دی بمعنی شبیه ونظیر\nومانئد باشد - ونفیر ثمثال هم هست- و بکس\nثالث مخفف تندبس است که آنهم تن مانند باشد\nچه دبس بمعنی شبه ونظیر ومانند بود .\nلندسه » بنتع تالث بر وزن مدرسه ه\nبمعنی نندس است که تمثال باشد - وبکسر ثالث\nمخفف نندیسه است که آنهم بمعنی شبیهونظیر-\nوثمئال باشد .\nنه چرخ است واجزای ار چون ستاره نه ابر است وآوای آن ح'
  .. 'نی نندس است که تمثال باشد - وبکسر ثالث\nمخفف نندیسه است که آنهم بمعنی شبیهونظیر-\nوثمئال باشد .\nنه چرخ است واجزای ار چون ستاره نه ابر است وآوای آن حمجو تندر.\n«فرخی سیسالی۵ه .۶\n۴۳ رك: تور . 0 از فن - دس (مخنف دس). رلك: تندس .\n۵ ند ر ست -بفتح اول وضم\u200cسوم\u200cوچهارم\u200cاز:نن ۳ درست («.م). کیلکیو نطنزی)10400۲05:\nفریزندی وبرتی 15200705 «۱.۵ ص۲۹۲» .سنگری 1200267850 .سرخ 00۲654ها؛\nلاسکردی 30007656) «2. ۷ ص۱۹۲ ؛ ک'
  .. 'نی شبیهونظیر-\nوثمئال باشد .\nنه چرخ است واجزای ار چون ستاره نه ابر است وآوای آن حمجو تندر.\n«فرخی سیسالی۵ه .۶\n۴۳ رك: تور . 0 از فن - دس (مخنف دس). رلك: تندس .\n۵ ند ر ست -بفتح اول وضم\u200cسوم\u200cوچهارم\u200cاز:نن ۳ درست («.م). کیلکیو نطنزی)10400۲05:\nفریزندی وبرتی 15200705 «۱.۵ ص۲۹۲» .سنگری 1200267850 .سرخ 00۲654ها؛\nلاسکردی 30007656) «2. ۷ ص۱۹۲ ؛ کسکه تن\u200cسالم دارد. سالم. رجوع به\u200cتتدرستی شود.\nلندر ستی -بفتح اول وض'
  .. '۹۲» .سنگری 1200267850 .سرخ 00۲654ها؛\nلاسکردی 30007656) «2. ۷ ص۱۹۲ ؛ کسکه تن\u200cسالم دارد. سالم. رجوع به\u200cتتدرستی شود.\nلندر ستی -بفتح اول وض\u200cسوموچپارم.از: تندرست(ه.م) - ی(مصدری) رجوع به\u200cدرستی\u200cشود ؛\nپهلوی )۲105 0210-41«ار نوالا ۶ سلاهت: #رسو لگفت علیه\u200cالسللام: این\u200cطایفه را (مسلمانان را\nطریفی حست که نااشتها غالب شود خورند ونوزاشتهابافی باشد که دست\u200cازطمام بدارند. حکیم گفت:\nاین است موحب تندرستی.٩ «کلتان ۷ '
  .. '#رسو لگفت علیه\u200cالسللام: این\u200cطایفه را (مسلمانان را\nطریفی حست که نااشتها غالب شود خورند ونوزاشتهابافی باشد که دست\u200cازطمام بدارند. حکیم گفت:\nاین است موحب تندرستی.٩ «کلتان ۷ و۸ -لیز نندرسی اسمی است که به\u200cبسنا *داده شده\n#ستا۱ ص۳۲۷ >.'
===== 746 نی ۱ مس بر وزن بدرو . کبوت را | گویند. | تند و خند» ح اول وخای قطددار » | اين لفت ازان
  .. 'نی ۱ مس بر وزن بدرو . کبوت را\nگویند.\nتند و خند» ح اول وخای قطددار »\nاين لفت ازانباع است بمعنی (۱) تار و ما رکه\nزیروزیر شده(۲) واز هم پاشیده باشد » و باین\nححشفی بفتح اول وخای نقطمدار هم آمده است .\nتندور بنم\u200cاول وثالث بروزن پرزور *\nبمعنی رعد باشد » و بختح ثالث هم باین حعنی\nآمده است ۴ -وبل'
  .. '» ح اول وخای قطددار »\nاين لفت ازانباع است بمعنی (۱) تار و ما رکه\nزیروزیر شده(۲) واز هم پاشیده باشد » و باین\nححشفی بفتح اول وخای نقطمدار هم آمده است .\nتندور بنم\u200cاول وثالث بروزن پرزور *\nبمعنی رعد باشد » و بختح ثالث هم باین حعنی\nآمده است ۴ -وبللرانر گویند کهءرب\u200cعندلیب\nخوانند ؟ .\nنف « بنم اوذیر وزن عمده , چیزی\nباشد که مانند غنجه مرتبهٌ اول از درخت\u200cسرزند\nوبمد ازآن ب رکه از مبان\u200cآن\u200cبر آبد۴ -و زبود\nسرخ ر'
  .. 'شد که مانند غنجه مرتبهٌ اول از درخت\u200cسرزند\nوبمد ازآن ب رکه از مبان\u200cآن\u200cبر آبد۴ -و زبود\nسرخ رالیز کوبند , و بمعنی اول بجای\u200cدال ایجد\nزای حوزعم آمده\u200cاست ۰\nتند ید۴ س سم اول بروزن جتبید »\nماضی تندشدن ودرخشم\u200cرفتن باشدیمنی تند گردید\nودر خشم شد وغنچهوب رکه وشکوفه برآوردن\nدرخت را نیز کوبند " چه ه رگامدرخت شروع\nدر ب رک وشخوفه برآوردن کند کویند «نندید»\nبعنی پر گه وشکوفه بر آورد .\nنند یدن س چم آول بر وزن جنبیدن'
  .. 'سرزند\nوبمد ازآن ب رکه از مبان\u200cآن\u200cبر آبد۴ -و زبود\nسرخ رالیز کوبند , و بمعنی اول بجای\u200cدال ایجد\nزای حوزعم آمده\u200cاست ۰\nتند ید۴ س سم اول بروزن جتبید »\nماضی تندشدن ودرخشم\u200cرفتن باشدیمنی تند گردید\nودر خشم شد وغنچهوب رکه وشکوفه برآوردن\nدرخت را نیز کوبند " چه ه رگامدرخت شروع\nدر ب رک وشخوفه برآوردن کند کویند «نندید»\nبعنی پر گه وشکوفه بر آورد .\nنند یدن س چم آول بر وزن جنبیدن»\nمر زدن غنچه وب رکههرشکوفه باشد از '
  .. 'ن\u200cآن\u200cبر آبد۴ -و زبود\nسرخ رالیز کوبند , و بمعنی اول بجای\u200cدال ایجد\nزای حوزعم آمده\u200cاست ۰\nتند ید۴ س سم اول بروزن جتبید »\nماضی تندشدن ودرخشم\u200cرفتن باشدیمنی تند گردید\nودر خشم شد وغنچهوب رکه وشکوفه برآوردن\nدرخت را نیز کوبند " چه ه رگامدرخت شروع\nدر ب رک وشخوفه برآوردن کند کویند «نندید»\nبعنی پر گه وشکوفه بر آورد .\nنند یدن س چم آول بر وزن جنبیدن»\nمر زدن غنچه وب رکههرشکوفه باشد از درخت-\nاوقم هداج ای کدرا مد گ'
  .. 'گرد\nوبه\u200cنی اول بفتح اول هم بنظر آمده\u200cاست.\nلندیسی * » بر وزن تسدیس » بمعلی\nتن مانند است چه دیس بمعنی مالند باشد -\n)٩( چش: وبمعنی.\n(4) چش: نسح .\n۴ راه: تندیدن.\nاي سح\nو بمستی\u200cصورت وئمثال - و پیکرو کالبد و فاب\nد\u200c ۰\nند یسه ۱ بر وزن نخفیفه : بمعنی\nتندس است که تمثال و صورت - و مالئد\nنند یور« من اول وبای\u200cسطیوسکون\nواو و رای فرشت . بمعنی جستن و برجستن\nباشف .\nلون\u200cردن ع با زای\u200cهوزبروز نک رکدن.\nبمعنی خاموش بود'
  .. 'س بمعنی مالند باشد -\n)٩( چش: وبمعنی.\n(4) چش: نسح .\n۴ راه: تندیدن.\nاي سح\nو بمستی\u200cصورت وئمثال - و پیکرو کالبد و فاب\nد\u200c ۰\nند یسه ۱ بر وزن نخفیفه : بمعنی\nتندس است که تمثال و صورت - و مالئد\nنند یور« من اول وبای\u200cسطیوسکون\nواو و رای فرشت . بمعنی جستن و برجستن\nباشف .\nلون\u200cردن ع با زای\u200cهوزبروز نک رکدن.\nبمعنی خاموش بودن وخاموش\u200cشدن- وصبرونحمل\n۳3 دثب و آمودن\u200cباش وتن\u200cزن, نن\u200cزده(۳) خاموش\nشونده که فاعل است - ویمعن'
===== 756 توا ای << | تو لك ح با اول مضوم و ثانی‌«جهول | بر وزن موتكك . طوطی سخن کوبرا گوید - | 
===== 757 و گاه خون از وی روان شود و گاهی نشود- وبا | نانی مجهول طوطی را کویندا . | و ی بر وزن
```


## [2026-10-15T02:48:24.838Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BQT_v1_pages.txt').read()\nt=re.sub('[‪-‮‎‏]','',t)\npages=t.split('\\f')\nfor i in [755,756]:\n    p=pages[i]\n    for m in re.finditer('(توان|tav|tuv|tow)',p):\n        j=m.start(); print(i,'..',repr(p[max(0,j-150):j+300]))\nE"
}
```


### [2026-10-15T02:48:25.306Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:48:28.085Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BQT_v1_pages.txt').read()\nt=re.sub('[‪-‮‎‏]','',t)\npages=t.split('\\f')\nfor i in range(748,770):\n    p=pages[i]\n    for m in re.finditer('توان[\\s»«-]',p):\n        j=m.start(); print(i,'..',repr(p[max(0,j-100):j+300]));break\nE"
}
```


### [2026-10-15T02:48:28.483Z] TOOL RESULT

```
<stdin>:7: SyntaxWarning: "\s" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\s"? A raw string is also an option.
754 .. 'ب\nهم\u200cآمده است .\nتواهی ه بر وزن و ممنی تباهی\nات که نابود کرده شده و خابع گردیده وبکمال\nنرسیده باشد ۰\nتوان نم اول پروزن جوان . قوت\nوقدرث رتوالایی باشدا - و بمعنی ابر هم هست\nکه بمریی\u200cسحاب گویند- وممکن بودن هرچیزرا\nیز کنته\u200cاند؟ .۶\nوافچه؟ - بروزن ومعنی\u200cیانچه\u200cاست\nکه بعربی لطمه گوبند .# قها۷ » بنم اول و بای فرسی بالف\nتو اهه - بفتح اول وهای هوز » قليةٌ | کشیده . بلفت زند و پازند(۱) سیب را گویند\nبادنجان را'
```


## [2026-10-15T02:48:30.712Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BQT_v1_pages.txt').read()\nt=re.sub('[‪-‮‎‏]','',t)\np=t.split('\\f')[754]\nj=p.find('۱ -'); print(p[-1500:])\nE"
}
```


### [2026-10-15T02:48:31.158Z] TOOL RESULT

```
وبند .# قها۷ » بنم اول و بای فرسی بالف
تو اهه - بفتح اول وهای هوز » قليةٌ | کشیده . بلفت زند و پازند(۱) سیب را گویند
بادنجان را کوبند - و کوکو ۴ وخاکینهرا نیز . | وجربی تفاح خوانند .
- اوستا - 1۵۷ ۵ ( توانستن , قدرت داشتن ) ۰ 62] 2۷2 » پهلوی ۷28 ,
هندی باستان -52۵۷, 12۷141.ارمنی 46۷617 (ماندن» دوام کردن . تحمل کردن» استقامت -
داشتن) «اسشق 4*۱* «نبر ٩۷۲۸۵ .«مسینا ۱4۹ :۰0۲ ۴ -بمعنی اخیردر دساتیر آهده
۱۳ ۴ -لفتی است‌در: تیانچه (عم) . ۴ .ره :ک وکنك وکوکو .
۵ رك: تباهی . ۱ -مز» ۵02 20۳2), پهلوی 96۷»,سب «یونکی ۱۱۸.
۵ قوافا -لفةبشم‌اول (درتداول امروز بفتح),از: نوان ۱-۲ (پسوند فاعلی باصفت مشبهه)؛
قادر, کسیکه ازعهد؛ انجام کاربرآ ید زورمند, نیرومند:
مبازوان توانا و فوت سردست خطاست ینجهٌ مسکین ناتوان بشکست .
کلتان ۲۹*.
۵ قوالستن -لفةیض‌اول (در نداول امروز بفتح) وکسر چیارم (در لهِجدُ مرکزی)؛ از :
توان ۲+ ستن (پسوند مسدری)؛ پهلوی ۷۵0)1(50217) «اسشق 4۰۱ [رك: توان] ؛قدرت‌داشتن
مقثدر بودن .
توالنگر لغب اول (درتداول امروز بفتح) وفتح پنجم, جهلوی ۱۷20-127 «اونوالا
۵ «منا ٩۲:۱4 ؛ ترونمند» مالدار» غنی؛
کر کنن خاه مهد نز کی نشناسد توانگر از دروش.«گلتان ۵۱*.
۵ توانگری -لفتنم اول(درتداول امروز بفتح) وفتح پنجم , پهلوی 0۷۵-18:110)
«ب رکه ۰۲۲۸ « اونوالا ۰۵۳٩ مالداری» روت .
۵ قوپ _ازتر کی, سلاحیاستآتشین
دارای لوله‌ای بزر که از آهن بامفرغ که برروی
چرخ حمل‌شود- بك‌بته ازقماش‌وجز آن- توپ
زدن » توپ الداختن- در اصطلاح فمار . بروی
دست حرف برخاستن درصورنیکه دست خود
پت‌تر ازدست حربف‌باشد. «ناظم‌الاطباه» -نوپ توب
و ثشر زدن » سختان درشت و سخت بک یگفتن .
۵ توب‌جی -ازن رکی, لشکری که بانوپ کار کند , که‌سلاحش توپ است
```


## [2026-10-15T02:48:35.917Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nfor f in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n  t=open(f).read()\n  t=re.sub('[‪-‮‎‏]','',t)\n  pages=t.split('\\f')\n  for i,p in enumerate(pages):\n    for m in re.finditer('ثور\\s*[-«»ه۱۲]*\\s*(بفتح|بر وزن|بروزن)',p):\n        j=m.start(); print(f,i,'..',repr(p[max(0,j-100):j+400]))\nE"
}
```


### [2026-10-15T02:48:36.512Z] TOOL RESULT

```
<stdin>:7: SyntaxWarning: "\s" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\s"? A raw string is also an option.
```


## [2026-10-15T02:48:39.673Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^taurus\\|^Taurus\\|^steer\\|^thigh\\|^thousand\\|^thumb\\|^tumor\\|^tuber\\|^tomb\\b\\|^butter\" KLN_1966.txt | head -20"
}
```


### [2026-10-15T02:48:40.105Z] TOOL RESULT

```
5978:butter.
31361:thousand  four  hundred’,  as  referring  to  the period  beginning  with  1400.  It.  quattro  derives fr.  L.  quattuor,  cento  fr.  L.  centum.  See  quadri- and  cent  and  cp.  cinquecento,  trecento. Derivatives:  quattrocent-ism,  n.,  quattrocent- ist,  n.
36687:steer,  tr.  and  intr.  v.,  to  direct.  —  ME.  steeren, steren,  fr.  OE.  stieran,  ‘to  steer,  guide’,  rel.  to ON.  styra,  Dan.  styre,  Swed.  styra,  OFris. stiora,  Du.  sturen,  OHG.,  MHG.  stiuren,  G. steuern,  ‘to  steer’,  Goth,  stiurjan,  ‘to  establish, assert’,  OE.  steor-  (in  compounds),  ON.  styri, OFris.  stiure,  Du.  stuur,  OHG.  stiura,  MHG. stiure,  G.  Steuer,  ‘rudder,  helm’,  prob.  rel.  also to  ON.  staurr,  ‘pale,  stake,  pole’,  and  cogn. with  Gk.  OTaup 6?,  of  s.m.,  OI.  sthavardh,  ‘thick, solid’,  sthavirah,  ‘broad,  thick’,  stiirdh,  ‘strong’. Arm.  st var,  ‘thick’,  L.  -staurare  in  in-staurdre, ‘to  renew,  repair,  restore’,  re-staurdre,  ‘to  re¬ pair,  restore’.  All  these  words  prob.  derive  fr. I.-E.  *st(h)eu-ro-,  *st(h)au-ro-,  *st(hf  uro-, *st(h)uro-,  ‘strong,  stiff’,  enlargements  of  base *st(h)au-,  *st(h)it-,  ‘stiff,  upright;  post,  pillar’, whence  Gk.  axusiv,  ‘to  make  stiff,  erect,  place, set’,  cttuXo?,  ‘wooden  pole,  style  for  writing; see  Walde-Hofmann,  LEW.,  I,  705-706  s.v. instaurare  and  Kluge-Mitzka  EWDS.,  pp.  747- 748.  Cp.  the  first  element  in  starboard.  Cp.  also stauro-,  instauration,  restaurant,  restauration, store,  story  of  a  house.  Cp.  also  stoa,  stoic,  style, ‘gnomon’,  stud,  ‘nail,  peg’,  stuff.  Base  *st(h)au-, *st(h)u-,  stands  in  gradational  relationship  to base  *st(h)a-,  ‘to  stand’.  See  state.
36689:steer,  n.,  a  young  ox.  —  ME.,  fr.  OE.  steor,  rel. to  OS.  stior,  ON.  stjorr,  pjorr,  Swed,  t/i/r, Dan. tyr,  MDu.,  Du.,  MHG.,  G.  slier,  Goth,  stiur, ‘bull’,  and  cogn.  with  Gk.  xaiipoi;,  L.  taurus, ‘bull,  bullock,  steer’,  OSlav.  tun i,  ‘bull,  steer’, Lith.  tauras,  ‘aurochs’,  OPruss.  tauris,  ‘bison’. All  these  words  are  prob.  borrowed — directly or  indirectly — from  the  Sem.  languages.  Cp. Aram,  tor,  Heb.  shor,  ‘bull,  bullock,  ox’,  and see  Taurus.  Many  an  attempt  has  been  made  to trace  Gk.  xaupo;,  etc.,  to  an  I.-E.  source  (cp. e.g.  the  ‘etymology’,  that  connects  these  words with  OI.  sthurah,  ‘thick’,  and  explains  Gk. xaupo ?,  Goth,  stiur,  etc.,  as  ‘the  thick  animal’).
38297:Taurus,  n.,  1)  a  constellation,  containing  the Pleiades  and  Hyades;  2)  one  of  the  signs  of  the zodiac  (astron.)  —  L.  taurus,  ‘bull’,  cogn.  with Gk.  Taupop,  OSlav.  turu,  ‘bull’,  Lith.  tauras, ‘aurochs’,  OPruss.  tauris,  ‘bison’;  prob.  of  Sem. origin.  Cp.  Aram,  lord,  ‘ox,  bull,  steer’,  Heb.  shdr, Akkad,  shuru,  Arab,  thor,  Ethiop.  sor,  of  s.m. Cp.  also  steer,  ‘young  ox’,  toreador,  torero,  toro and  the  second  element  in  Minotaur.  Cp.  also the  second  element  in  bittern, taut,  adj.,  drawn  tightly,  tense.  —  ME.  toght,
40370:tuberous
40380:tuberaceous,  adj.  —  See  prec.  word  and  -aceous. tubercle,  n.,  a  small  prominence.  —  L.  tubercu- lum,  ‘a  small  swelling’,  dimin.  of  tuber.  See  tuber and  -cle.
40385:tuberculate,  adj.,  1)  characterized  by  tubercles;  2) tubercular.  —  Medical  L.  tuberculatus,  formed fr.  L.  tuberculum  (see  tubercle)  with  adj.  suff. -ate.
40387:tuberculin,  tuberculine,  n.,  preparation  made from  a  culture  of  the  tubercle  bacillus,  used  in the  diagnosis  and  treatment  of  tuberculosis.  — Formed  fr.  L.  tuberculum  (see  tubercle)  with chem.  suff.  -in,  -ine.
40388:tuberculo-,  before  a  vowel  tubercul-,  combining form  meaning;  1)  tuberculous;  2)  tubercle  ba¬ cillus  ;  3)  tuberculosis.  —  Fr.  L.  tuberculum.  See tubercle.
40389:tuberculoid,  adj.,  resembling  a  tubercle.  —  A  hy¬ brid  coined  fr.  L.  tuberculum  (see  tubercle)  and Gk.  -oeiS r)?,  ‘like’,  fr.  eISo?,  ‘form,  shape’.  See -oid.
40390:tuberculosed,  adj.  —  Formed  fr.  next  word  with suff.  -ed.
40391:tuberculosis,  n.  (med.)  —  A  Medical  L.  hybrid coined  fr.  L.  tuberculum  (see  tubercle)  and  -osis, a  suff.  of  Greek  origin.  The  name  tuberculosis was  given  to  this  disease  because  it  is  accom¬ panied  by  the  formation  of  tubercles  in  the  lungs, a  circumstance  first  noticed  by  Richard  Morton in  London  (in  1689).
40392:tuberculous,  adj.  —  Formed  with  suff.  -ous  fr.  L. tuberculum.  See  tubercle, tuberose,  adj.,  tuberous.  —  L.  tuberdsus.  See tuberous.
40393:tuberose,  n.,  a  bulbous  plant,  Polianthes  tuberosa.
40395:tuberosity,  n.  —  MF.  (=  F.)  tuberositd,  fr.  L.  tu¬ ber  os  us.  See  prec.  word  and  -ity. tuberous,  adj.,  1)  having  tubers  (bot.);  2)  knobby.
40427:tumor,  tumour,  n.  —  L.  tumor,  ‘swelling,  protu¬ berance’,  fr.  tumere.  See  prec.  word  and  -or. tumorous,  adj.,  pertaining  to  a  tumor.  —  L.
40428:tumorosus,  fr.  tumor.  See  prec.  word  and -ous.
```


## [2026-10-15T02:48:44.100Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^thumb,\\|^thigh,\\|^thousand,\\|^tomb,\\|^tuber,\\|^tumid\\|^tumefy\\|^butyro\\|^butter, n\" KLN_1966.txt | cut -c1-900; sed -n 5976,5980p KLN_1966.txt | cut -c1-900"
}
```


### [2026-10-15T02:48:44.371Z] TOOL RESULT

```
40425:tumefy,  tr.  v.,  to  cause  to  swell;  intr.  v.,  to  swell. —  F.  tumefier,  fr.  L.  tumefacere,  ‘to  cause  to swell’,  fr.  tumere,  ‘to  swell’,  and  -ficare,  fr.  fa- cere,  ‘to  make,  do’.  See  tumid  and  -fy. tumescent,  adj.,  slightly  swollen.  —  L.  tumescens, gen.  -ends.  pres.  part,  of  tumescere,  ‘to  begin  to swell',  formed  from  the  stem  of  tumere,  ‘to swell’,  with  the  inchoative  suff.  -escere.  See  next word  and  -escent.
40426:tumid,  adj.  —  L.  tumidus,  ‘swollen’,  formed  with suff.  -idus  (see  -id)  fr.  tumere,  ‘to  swell’,  which is  rel.  to  tumor,  ‘swelling,  protuberance',  tumu¬ lus,  ‘a  raised  heap  of  earth,  a  mound’,  and  cogn. with  OI.  tutumah,  ‘fruitful,  strong’,  tumrah,  ‘tur¬ gid,  fat’,  Avestic  tuma,  ‘fat’,  OE.  puma,  ’thumb’, pymel,  ’thimble',  fr.  I.-E.  *tumo-,  enlargement of  base  ‘tu-,  'to  swell’,  whence  also  Gk.  niXo?, T‘j>.7),  ‘a  swelling,  rising',  OSlav.  tyjg,  tyti,  ‘to become  fat',  tuku,  ‘fat’,  Lith.  taukai,  ‘fat’,  tau- kas,  ‘pieces  of  fat’,  tunku,  tiikti,  Lett,  tukt,  ‘to  be¬ come  fat',  OE.  peoh,  pioh,  ‘thigh’,  and  the  first element  in  OSlav.  tysgsta,  tysqsta,  Goth,  pusun- di.  OE.  pusend,  thousand’.  Cp.  tumefy,  tumor, tumult,  tumulus,  intumesce.  Cp.  also  obturate. Satyr,  soma,  body’,  tomb,  tome
Derivative:  buttress,  tr.  v. butty,  n.,  a  middleman.  —  Of  uncertain  origin, butyl,  n.,  a  hydrocarbon  radical,  C4H,  ( chem .)  — Formed  from  the  first  three  letters  of  L.  buty¬ rum,  ‘butter’,  and  fr.  Gk.  ukt),  ‘material,  stuff’. See  butter  and  -yl.
butyraceous,  adj.,  resembling  butter.  —  Formed with  suff.  -aceous  fr.  L.  butyrum,  ‘butter’.  See
butter.
butyrate,  n.,  a  salt  of  butyric  acid  {chem.)  — Formed  with  chem.  suff.  -ate  fr.  L.  butyrum, ‘butter’.  See  butter.
butyric,  adj.,  pertaining  to  butter.  —  Formed  fr.
```


## [2026-10-15T02:48:47.245Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^butter,\\|^tomb,\\|^thumb,\\|^thigh,\\|^thousand,\\|^tuber,\\|^Teucer\\|^tyro-\" KLN_1966.txt | cut -c1-700; grep -n -i \"^ *steer\\b\\|^ *steer[,.]\" SKT.txt | cut -c1-500 | head -4"
}
```


### [2026-10-15T02:48:47.638Z] TOOL RESULT

```
40636:tyro-,  before  a  vowel  tyr-,  combining  form  mean¬ ing  ‘cheese’.  —  Gk.  xupo-.  Tip-,  fr.  Tip 6?, ‘cheese’,  which  is  cogn.  with  OI.  turah,  Avestic tuiri-,  ‘curds,  whey’,  and  perh.  also  with  OSlav. tvarogu,  ‘curds’.  These  words  possibly  derive  fr. I.-E.  base  *tu-,  ’to  swell’,  whence  also  L.  tumere.
```


## [2026-10-15T02:48:49.662Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"butter,  n\\.\\|^tomb\\b\\|thumb,  n\\.\\|thigh,  n\\.\\|thousand,  adj\\|tuber,  n\\.\\|tomb,  n\\.\" KLN_1966.txt | cut -c1-600 | head"
}
```


### [2026-10-15T02:48:50.153Z] TOOL RESULT

```
5969:butte,  n.,  an  isolated  hill  in  the  western  U.S.  — F.,  fr.  hut,  ‘goal,  target’.  See  butt,  ’aim,  goal’, butter,  n.  —  OE.  butere,  huttor-,  fr.  L.  butyrum (whence  also  OFris.,  OHG.  butera,  Du.  boter, MHG.  buter,  G.  Butler,  It.  burro,  OF.  burre, F.  beurre).  fr.  Gk.  [BoufOpov,  ‘butter’,  lit.  ‘cow cheese',  which  is  compounded  of  {Bone,  ‘ox, cow',  and  Tupo;,  ‘cheese’.  See  bovine  and  tyro-. Derivatives:  butter,  tr.  v.,  buttcr-y,  adj. butterfly,  n.  —  ME.  butter /lie,  fr.  OE.  buterfleoge. See  butter  and  fly.  Butterfly  prop,  
17391:Hecate,  also  Hekate,  n.,  an  ancient  Greek  god¬ dess,  daughter  of  the  Titan  Perseus  and  Asteria (Greek  mythol.)  —  L.  Hecate,  fr.  Gk. '  Exarr], shortened  fr.  ExaxTjPoXo?,  which  was  regarded already  by  the  ancients  as  an  enlarged  form  of foor)P6Xop  and  accordingly  explained  as  ‘far- darting,  far-shooting’.  See  Hecuba, hecatomb,  n.,  a  sacrifice  of  a  hundred  oxen (Greek  antiq.)  —  F.  hecatombe,  fr.  Gk.  ixa- to;aP7i,  which  is  compounded  of  exax6v,  ‘a hundred’,  and  the  stem  of  (Joys,  ‘ox’.  Gk.  i- xax6v  is  formed  fr.  ev,  ‘
31873:Derivatives:  rebutt-able,  adj.,  rebutt-al,  n., rebutt-er,  n.,  that  which  rebuts, rebutter,  n.,  a  defendant’s  answer  to  a  plaintiff’s surrejoinder.  —  AF.  rebuter,  fr.  OF.  reboter',  see rebut.  For  the  subst.  use  of  infinitives  in  law terms  cp.  attainder  and  words  there  referred to.
37602:surrebut,  intr.  v.,  to  make  a  surrebutter  (law).  — • Back  formation  fr.  surrebutter.  Cp.  rebut, surrebutter,  n.,  plaintiff’s  reply  to  defendants  re¬ butter  (law.)  —  Coined  fr.  sur-,  ‘above’,  and
39033:thievery,  n.  —  Formed  fr.  E.  thief  with  suff.  -ery, thigh,  n.  —  ME.  theh,  thih,  thigh,  fr.  OE.  peoh, pioh,  rel.  to  ON.  pjo,  ‘thigh,  rump',  OFris. thiach,  ODu.  thio,  Du.  dij,  OHG.  dioh,  ‘thigh’, fr.  I.-E.  base  *tu-,  *teu-,  ‘to  swell’,  whence  also OIr.  ton,  ‘rump’,  W.  tin,  of  s.m.,  OSlav.  tyjq, tyti,  ‘to  become  fat’,  tuku,  ‘fat’,  Lith.  tauka, ‘fat’,  tdukas,  ‘pieces  of  fat',  tunkii,  tiikti,  ‘to  be¬ come  fat’,  Lett,  tiikt,  ‘to  swell’,  L.  tumere,  ‘to swell’.  See  tumid  and  cp.  words  there  referred  to.
39170:Thule,  n.,  classical  name  of  the  northernmost  part of  the  world.  — -  L.  Thule,  Thyle,  fr.  Gk. 0oiiXr],  0uXt).  Cp.  thulium, thulia,  n.,  thulium  oxide  (chem.)  —  ModL.,  coin¬ ed  by  the  Swedish  chemist  Per  Teodor  Cleve (1840-1905)  in  1879  fr.  Thule,  name  of  the  north¬ ernmost  land  in  the  world, thulite,  n.,  a  variety  of  zoisite  (mineral.)  —  Form¬ ed  fr.  Thule  with  subst.  suff.  -ite. thulium,  n.,  a  metallic  element  belonging  to  the rare  earths  ( chem .)  — -  ModL.,  coined  by  the French  chemist  Paul  fimile  Lecoq  de  Bo
39476:tomato,  n.  — -  Fr.  earlier  tomate,  fr.  Sp.  tomate,  fr. Nahuatl  tomatl,  lit.  ‘the  swelling  fruit’,  fr.  to- mana,  ‘to  swell’.  The  alteration  of  tomate  into tomato  is  prob.  due  to  the  influence  of  potato. tomb,  n.  —  ME.  toumbe,  tombe,  fr.  OF.  (—  F.) tombe,  fr.  Eccles.  L.  tumba  (whence  also  It. tomba,  F.  tombe,  Sp.  tumba),  fr.  Gk.  xupflos, ‘sepulchral  mound,  tomb’,  which  is  cogn.  with
40376:tubal,  adj.,  pertaining  to  a  tube.  —  Formed  with adj.  suff.  -al  fr.  L.  tubus.  See  next  word, tube,  n.,  a  hollow  cylindrical  body;  a  pipe.  —  F., fr.  L.  tubus,  ‘a  pipe’,  which  is  rel.  to  tuba,  ‘trum¬ pet’.  See  tuba  and  cp.  tubule,  intubate. Derivatives:  tube,  tr.  v.,  tub-er,  n.,  tub-ing,  n. tuber,  n.,  1)  a  short  thickened  underground  stem ; 2)  a  swelling  or  prominence.  —  L.  tuber,  ‘a swelling,  hump,  protuberance’,  fr.  I.-E.  *tu-bh-, ‘to  swell’,  whence  also  ON.  piifa,  ‘mound,  hill’. Cp.  I.-E.  *tu-m-,  appearing  in
```


## [2026-10-15T02:48:52.649Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"txm\\b\\|txm \" SOD_pages.txt | head -8; grep -n \"taumā\\|tauma\\|taumä\" KNT_full.txt | head -5; grep -n -i \"tauma\\|taum\" HID.txt | head -3; grep -n -i \"tauma\\|taum\" BST.txt | head -3"
}
```


### [2026-10-15T02:48:53.168Z] TOOL RESULT

```
3080:                             house             Olr. *xanaka                   /martoxme; mrtxm}y        people, Olr. *martiya-
19344:          SCE 531, 533, 544; TSP 5.3; STii 7, 14; mrtxmyt(tl    5470 mrtxm'nyGi) M                          J^^^y
19368:                                                                       MSP; BSTi; C2, abl. voc. mrtxm\ ace. mrtxmw,
19370:                                                                       C2, gloss; pi. mrtxm())yt, BBB 505; GMS 1256;
31344:          abl. -} =»txm-, twxmy                                         GMS 662; pt. inf. tk*ws>t, TSP 17.196, GMS 551;
31797:                                                                            =*txm-
31829: 9735 txm-      C                            x j^s «j\j&>- «u3*r
2607:Рита = tauma; niy = пай, Мше = haw. 
3054:taumayd DB 4.19, 422, eJ, g.9f (but -hyä 
3142:DNb 25f = taumanis-Saiy, [n"yāikama Аа 4 
7129:maniíaiy = taumanis-Saiy, I'yü)kama = -kam- 
7364:+ Sim = dpisim DB 1.95f; taumaniš + Saiy = 
1731:p. su^ra/^/ä; — g. ra^lf/tardho ; — z. taoJi/nay p. taumä;'^) —
4216:taum-äjä
4890:Ap. ahjajä statt *aÄ;a nach taum-äjä^ so noch hamahjäja^ § 265.
2717:inally part. pret. from rt. mé@ and 4, 8 1, ah‘ to be,’ with genet. ‘be- long to’ (khshatram amdkham taum- dyG dha(h) ‘ the kingdom was ‘be- longing to our family’). Pres. ind, amty ‘I am’ (Aw. abmi, Mod. P. -am) ; ahy'* thou art’ (Aw. ahi) ; astiy ‘he is’ (Aw. asti, Mod. P. ast); amahy ‘ we are’ (Aw. mahi); ha(n)- tiy ‘they are’ (Aw. henti, Mod. P.and); con}. ahatiy * he may be’ (Aw. Gath, anhait?) ; imperf, indic, dham ‘ I was ’ (Skr. dsam) ; dha(h) ‘ he was’; dha(n) ‘ they were’ Skr. dsan) ; middle dha(n)td ‘ they were.’
2718:* taumd-, sb, f. perhaps tau(h)md, Aw. taokhman, Mod. P, tukhm; ‘race, family,’ nom.sg. .-d: yded taumd ahutiy ‘as long as race (i.e, man- kind) is (i.¢., exists), wtdtaiy t. md biyd(h) ‘thou mayest not have posterity’; gen. -dyd (Aw. -aydo, Skr. -dy@); VIIL. mand t. ‘the eighth of my family,’ Ka(n)bu/ji- ya(h) amdkham t. * K, of our family,’ khshatram amakham t. dha(h) * the kingdom belonged to our family,’ amikham t, kasheiy ‘any one of oar f.,’ Khshathrita(h) (H)uvakhshatra- hyd t.* Kh. of H's f.’; abl. -dyd(A) (Aw, -aydt) : khshatram tya(h)- hacd amdkham tawndya(h)  pardbriam aha(h) ‘the kingdom that was taken away from our family.’ da
2720:4. Tatiy Dirayava(h)us Kédyatiya(h): VITL mani taumiya tyaiy? paruvam* kédyafiyé aha(n), adam navama(h) IX duvitatranam*® vayam
```


## [2026-10-15T02:48:55.011Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 31825,31835p SOD_pages.txt; grep -n \"^taumā\\|^tauman\\|taumā-\" KNT_full.txt | head -5"
}
```


### [2026-10-15T02:48:55.386Z] TOOL RESULT

```
                                                                        tim (tymh) ©<*ati-ima-, <*ati-imi Yaghn. tint
      two-fold ?
         Sund. MSP p53-4, pi. tvfznku b30, 100                           still, yet, again, moreover
                                                                         S W, BSOAS 1975, 136; VJ pl21; TSP p274;
 9735 txm-      C                            x j^s «j\j&>- «u3*r
        taxm, tsxm ©nom. txmy% ace. /jemw; pi. txmt}                       BBB; KG pl90; MSP bl38; C2 p228; STii 6.6,
          =*twxmy, tym                                                     1.43; Sund. AoFviii 1981 p218; MDii p2l3;
        seed, descendant, child                                            Frag. Len.
        C2, 52R9, 54R27, 60R9                                      9747 tern
                                                                        tym ^tymp^y
                                                                             C                 (ot^<^)l^jl^<©l^b         <J^c*
7365:taumantSaiy DNb 25f; -kam + тату in {n*ya|kama 
12140:taumaniSary ‘what a man does or performs ac- 
25883:tauman- sb. ‘power, strength’: deriv. of root 
25888:taumā nsn. ($187) DB 4.74, 78; 5.19°, 35. tau-
```


## [2026-10-15T02:48:57.224Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25880,25895p KNT_full.txt; grep -n \"^tav-\\|^ *tav- \\|atavayam\" KNT_full.txt | head -4"
}
```


### [2026-10-15T02:48:57.645Z] TOOL RESULT

```
taumaya absf. DB 1.61f. 


tauman- sb. ‘power, strength’: deriv. of root 
tav- ‘be strong’, with suffix -man- as in Skt. nama 
‘name’, Lt. nomen (§122, $155.11). For separa- 
tion from taumd- ‘family’, see Tm. Lex. 91, and 
Kent, JAOS 35.329-31. See also tawiyah-. 
taumā nsn. ($187) DB 4.74, 78; 5.19°, 35. tau- 
тату (= taumanis-Saiy; §41, §130, $138, 
$187) ipn. DNb 25f (Lg. 15.171-2, 176; not gen. 
sg. with Hz. Api 327; hardly loc. sg. with Sen 247; 
possibly aee. du., ‘two powers lof mind and of 
body|’, with Pisani, Riv. Stud. Or. 19.88-9). 


25884:tav- ‘be strong’, with suffix -man- as in Skt. nama 
25986:tav- vb. ‘be strong’: Av. tav-, Skt. tu-, ef. Gk.
```


## [2026-10-15T02:48:59.881Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"taumā- sb\\|taumā sb\\|^taumā-\" KNT_full.txt | head; grep -n \"family\" KNT_full.txt | grep -i taum | head -5"
}
```


### [2026-10-15T02:49:00.342Z] TOOL RESULT

```
6533:OP gen. taumdyd ‘family’, Skt. gen. -dyah in 
9118:Nom. Sg. taumd ‘family’, Мила, framand, yau- 
11977:family’, cf. amáxam taumäyä DB 1.28f depending 
12427:agreeing with its subject taumd ‘family’. 
25886:tion from taumd- ‘family’, see Tm. Lex. 91, and
```


## [2026-10-15T02:49:01.852Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25862,25880p KNT_full.txt"
}
```


### [2026-10-15T02:49:02.280Z] TOOL RESULT

```
ef. OP tya-. Only -tā apm., referring to patikarā, 


185 


in avabasa-a DB 4.72 (8133, $196; JAOS 62.272- 
3). 

{аита- sb. ‘family’ (8149.1): Av. taoxman-, 
NPers. tuzm, Skt. tokd-m ‘offspring’, tókman- 
tokma-s ‘young blade of barley’; -zm- became OP 
-hm- (5103.1, 5118.1), but remained in Med. 
(Ву. BSLP 31.2.76-9, Gr. $188; wrongly Mt. Gr. 
§75, Kent JAOS 35.329-31). taumd nsf. DB 1.8; 
4.56, 58f, 64, 75, 79; DBa 13. іаитат asf. DB 
488. іаитӣуӣ gsf. ($119) DB 1.9, 28f, 45, 49; 
2.16, 81; 4.19f, 22; DBa 15; DBe 8; DBg 11f. 
taumaya absf. DB 1.61f.
```


## [2026-10-15T02:49:07.022Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==225 || NR==224 || NR==226 {print \"== NR \" NR; print}' HID.txt | grep -n \"taum\\|NR\\|^ *[0-9]\\{3\\} *$\" | head; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"taumd-, sb\")) print \"BST NR\",NR}' BST.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"z. taoJi/nay p. taum\")) print \"HID NR\",NR}' HID.txt"
}
```


### [2026-10-15T02:49:07.529Z] TOOL RESULT

```
1:== NR 224
2:210
94:== NR 225
96:211
193:== NR 226
194:212
BST NR 252
HID NR 57
```


## [2026-10-15T02:49:11.472Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==252' BST.txt | head -5 | cut -c1-200; awk 'BEGIN{RS=\"\\f\"} NR==225' HID.txt | head -30 | cut -c1-150"
}
```


### [2026-10-15T02:49:11.851Z] TOOL RESULT

```
�1 said,’ athaha(h) * he said,’ athaha(n) ‘they said.’ Passiv. pres. thahyd- mahy ‘we are called’ (with active ending), aorist. athahy ‘it was said’ (or perhaps athahya(h) imperf. with active ending).
* pitar sb. m. ‘father,’ Aw. pitar, Mod. P. pidar ; nom. 8g. -d.
* Ariydrdémna-, m,, sg. nom, -a(h), gen. -ahyd ; name of the great-grand- father of King Darius (‘ making happy the Aryans’),
* Caishpi-, m., gen. sg. -dish, Teispes. (son of Achzwmenes),
* ava-,demonstr. pron, ‘ that,’ Aw. ava, Mod. P. 6. Sing. acc, avam, gen. avahyd, comp. avahyarddiy ; pl. nom. ace, avaiy, gen, avaishdm ; neut, sing ava(h), (Aw. avat), ava-paré * by, past that’ (‘he
I. Zu den altpersischen Lesestücken.
211
4- arsan- micti« = z. arsan-, — °§ä,
-säm (§ 215 Anm. 3).
j^ «a i a-] S . n. »Herrschaft, Eeich« ;
= i. ksaträ-f av. J^fapra-, — %(xm,
^§a'kapävan'] S. m. »Landpfle-
ger , Satrape« ; aus Ji^sasa- + jp®, cf .
Ypü-, — °vä.
^säjapija-] S. m. »König««; cf.
Verf., Ar. F. I, S. 27. — >, yam,
yahßi-y °janäm.
yflfSnä-] =s i. yghä-, z. |/«fiä-
(§ 168); »wissen, kennen«.
Fraes. 5 : ^mäsätij.
Je
hartanaij] s. ykar-,
haj-] Interr. »wer«; § 255; — m.
^hij »irgend wer«. — hiskij.
°Ua\ enkl. Part, »und«; = i., z.
""hij] enkl. Part.; = i. ""hid, z.
ygad'] :
dopp. Acc.
Praes.
ygan-]
»tödten«; -
Fraes.
ga, gata. —
P.P.P.
ygam-]
```


## [2026-10-15T02:49:17.365Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ثور",
 "prompt": "Give the Arabic etymology (ثَوْر bull) and the Persian section etymology/pronunciation verbatim, including any mention of Taurus/zodiac."
}
```


## [2026-10-15T02:49:17.996Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/steuraz",
 "prompt": "Give the etymology and descendants (Old English stēor, English steer) verbatim."
}
```


## [2026-10-15T02:49:18.748Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/طهماسب",
 "prompt": "Give the etymology verbatim (Middle Persian / Avestan forms)."
}
```


## [2026-10-15T02:49:19.400Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/τύμβος",
 "prompt": "Give the etymology verbatim."
}
```


## [2026-10-15T02:49:20.001Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/τυρός",
 "prompt": "Give the etymology verbatim."
}
```


## [2026-10-15T02:49:20.560Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/steer",
 "prompt": "Give the etymology of steer (n., young ox) verbatim."
}
```


### [2026-10-15T02:49:21.059Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:49:24.252Z] TOOL RESULT

```
# Etymology of τύμβος

According to the Wiktionary entry, the etymology is provided as follows:

"From Proto-Indo-European *tum- ('to swell'), which Beekes implicitly takes as a Mediterranean substrate root."

The term derives from an ancient language root meaning expansion or swelling, with scholars suggesting it may originate from a substrate language of the Mediterranean region rather than from the typical Indo-European lineage.
```


### [2026-10-15T02:49:25.411Z] TOOL RESULT

```
# Etymology and Descendants of Proto-Germanic *steuraz

## Etymology

The origin of this term is uncertain. Scholars have proposed several theories:

"The term is sometimes connected with Avestan staora, ('large domestic animal'), which could perhaps indicate a PIE form *stéh₂wros ('big')" according to Kroonen's etymological dictionary.

Alternative theories suggest it may derive from the same source as Proto-Germanic *þeuraz ('bull'), from Proto-Indo-European *táwros. However, Kroonen argues this requires problematic ablaut patterns.

Most significantly, Kroonen proposes both *steuraz and *þeuraz were borrowed from a substrate language with "irregular sound substitution" of a non-IE consonant, possibly /θ/, with potential parallels in Etruscan.

## Descendants

The word evolved across Germanic languages:

- **Old English**: "stēor"
- **English**: "steer"
- **Middle English**: steer, steor, ster, stere
- **German**: Stier
- **Dutch**: stier
- **Old Norse**: stjórr
- **Gothic**: stiur

All modern Germanic languages retain cognates meaning "bull" or a castrated male bovine.
```


### [2026-10-15T02:49:26.578Z] TOOL RESULT

```
# Etymology of τυρός

According to the Wiktionary entry, τυρός comes "From Proto-Hellenic *tūrós (whence also Mycenaean Greek 𐀶𐀫 (tu-ro /⁠tūrós⁠/)), probably from Proto-Indo-European *tuh₂-ró-s, from *tewh₂- ('to swell')."

The entry notes an alternative possibility: compare Old English ġe-þweor ("curds"), which derives from a different Proto-Indo-European root meaning "to swirl, churn."

It may also be related to Proto-Slavic *tvarogъ ("quark, whey-cheese") and Avestan forms, though "the root and morphological details are disputed."
```


### [2026-10-15T02:49:26.951Z] TOOL RESULT

```
# Etymology and Pronunciation

## Arabic Etymology (ثَوْر)

The Arabic term derives from "Proto-Semitic *ṯawr-" and is cognate with Biblical Hebrew שׁוֹר (šôr). It primarily means "bull, steer, ox" and can also refer to Taurus in astronomy.

## Persian Section

**Etymology:** The word was "Borrowed from Arabic ثَوْر (ṯawr)" and functions as "Doublet of ستور."

**Pronunciation:** Varies by dialect—Classical Persian /ˈsawr/, Iranian Persian [sowɹ], and Dari [säwɾ].

**Usage:** As a proper noun, it denotes the Taurus constellation "of the zodiac traditionally figured in the shape of a bull," the corresponding astrological sign, and (in Dari) the second month of the Solar Hijri calendar, as in "انقلاب ثور" (the Saur Revolution).
```


### [2026-10-15T02:49:27.286Z] TOOL RESULT

```
# Etymology of طهماسب (Tahmasb)

**Middle Persian form:**
"𐭲𐭧𐭬(𐭩)𐭠𐭮𐭯 (tḥm(y)ʾsp /⁠Tahmāsp⁠/, a male given name, literally 'having brave horses')"

**Avestan form:**
The document notes that "𐬙𐬎𐬨𐬁𐬯𐬞𐬀𐬥𐬀 (tumāspana, a given name, literally 'with fat horses')" has been proposed as a cognate, but this identification "should be rejected."

The name derives from Old Persian *Tahmāspah, a compound combining the elements for "brave" (تهم, tahm) and "horse" (اسب, asb).
```


## [2026-10-15T02:49:31.119Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þūsundī",
 "prompt": "Give the etymology verbatim."
}
```


## [2026-10-15T02:49:31.689Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þeuhą",
 "prompt": "Give the etymology verbatim."
}
```


## [2026-10-15T02:49:32.414Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þūmô",
 "prompt": "Give the etymology verbatim."
}
```


## [2026-10-15T02:49:33.200Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tuber",
 "prompt": "Give the Latin etymology of tūber verbatim, and Latin tumeō if linked."
}
```


### [2026-10-15T02:49:35.700Z] TOOL RESULT

```
# Etymology

According to the Wiktionary entry, the etymology is stated verbatim as:

"From [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _[\*tewk-](/wiki/Reconstruction:Proto-Indo-European/tewk- "Reconstruction:Proto-Indo-European/tewk-")_."

In other words, Proto-Germanic *þeuhą derives from the Proto-Indo-European root *tewk-.
```


### [2026-10-15T02:49:37.230Z] TOOL RESULT

```
# Etymology of Proto-Germanic *þūmô

According to the Wiktionary entry, the etymology is:

"From Proto-Indo-European *tu(h₂)m-ō, from *tum- ('to swell'), thus 'big swollen finger' > 'thumb'."

The term shares cognates with Sanskrit túmra (strong, big), Latin tumor (swelling), Lithuanian tumėti (to coagulate), and Welsh twf (strength). This etymology suggests the word originally described the thumb as a notably swollen or prominent finger.
```


### [2026-10-15T02:49:38.496Z] TOOL RESULT

```
# Etymology of Proto-Germanic *þūsundī

According to the Wiktionary entry, the etymology has two proposed origins:

**First theory:** "Either from Proto-Indo-European *tuHsont-, *tuHsenti-" with parallels in Proto-Slavic *tysǫti/*tysęti ("thousand") and Lithuanian tūkstantis.

**Second theory:** Kroonen suggests derivation from Proto-Indo-European *tuHsdḱmto-, which is "compounded from a prefix *tuHs- ('fat', from *tewh₂-) and *ḱm̥tóm ('hundred')."

The entry notes this latter form appears preserved in Old Norse þúshundrað ("thousand"), combining hundrað ("hundred") with a þús- prefix, analogous to Italian milione from mille + -one.
```


### [2026-10-15T02:49:40.801Z] TOOL RESULT

```
# Latin Etymology of tūber

According to the Wiktionary entry, the Latin etymology states: "Probably from Proto-Italic *tūβos, from Proto-Indo-European *tewh₂- ('to swell')."

The source notes that "De Vaan is skeptical of the hypothetical morphology" regarding this proposed derivation chain.

**Note on tumeō:** The Wiktionary page for "tuber" does not contain a link to or mention of the Latin verb tumeō, so I cannot provide information about any connection between these terms based solely on the content provided.
```


## [2026-10-15T02:49:43.454Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/تخم",
 "prompt": "Quote the Mo'in entry for تخم verbatim, including origin tag like [په.]."
}
```


## [2026-10-15T02:49:44.030Z] TOOL CALL #82: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/توبره",
 "prompt": "Quote the Mo'in entry for توبره verbatim, including origin tag."
}
```


## [2026-10-15T02:49:44.673Z] TOOL CALL #83: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/ثور",
 "prompt": "Quote the Mo'in entry for ثور verbatim, including origin tag [ع.]."
}
```


### [2026-10-15T02:49:47.089Z] TOOL RESULT

```
# Mo'in Dictionary Entry for ثور

According to the Mo'in Dictionary (Farhang-e Entesharati Mo'in), the entry is:

"(ثُ) [ع.] (اِ.) 1 - گاو نر. 2 - نام یکی از صورت های فلکی و دومین برج"

This defines the term as: a male bovine animal, and secondly, the name of one of the constellations and the second sign of the zodiac.
```


### [2026-10-15T02:49:47.373Z] TOOL RESULT

```
# Mo'in Dictionary Entry for توبره

According to the Mo'in Dictionary (فرهنگ انتشارات معین), the entry reads:

"(رِ) (اِ.) 1 - کیسه ای که مسافران و شکارچیان ابزار کار و خوراک خود را در آن گذارند. 2 - کیسه ای بنددار که در آن کاه و جو ریزند و به گردن چارپایان بندند تا از آن بخورند."

This describes two meanings: (1) a bag used by travelers and hunters to store their tools and provisions, and (2) a tied bag filled with straw or barley that is fastened around the necks of pack animals for feeding.
```


### [2026-10-15T02:49:48.367Z] TOOL RESULT

```
# Mo'in Dictionary Entry for تخم

Here is the verbatim Mo'in entry:

"(تُ) [په.] (اِ.) 1 - نطفه . 2 - بیضة ماکیان و غیر آن . 3 - اصل ، نسب ، نژاد. 4 - بذر گیاه . ؛~ ِ چیزی را ملخ خوردن کنایه از: نایاب بودن ."

This entry provides four primary definitions for the Persian word تخم (takhm), ranging from biological meanings like sperm and eggs to abstract concepts like lineage and seeds.
```


## [2026-10-15T02:49:49.336Z] AGENT

Now archive the web sources.


## [2026-10-15T02:49:58.861Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; T=tools/fetch_source.py; \npython3 $T 'https://en.wiktionary.org/wiki/ستوه' --note 'page 507, Teu 1, sotuh: Wiktionary has no etymology' ;\npython3 $T 'https://en.wiktionary.org/wiki/تند' --note 'page 507, Teu 1, tond < MP tund < PIr *tund- < PIE *(s)tewd-';\npython3 $T 'https://en.wiktionary.org/wiki/توبره' --note 'page 507, Teu 1, tubreh < MP tobrag, Wanderwort';\npython3 $T 'https://en.wiktionary.org/wiki/تخم' --note 'page 507, Teuk, tokhm < *tawxma < PIE *tewk-';\npython3 $T 'https://en.wiktionary.org/wiki/ستور' --note 'page 507, Tauro, sotur < MP stor < Av staora < PIE *(s)tawros';\npython3 $T 'https://en.wiktionary.org/wiki/توان' --note 'page 507, Teu 1, tavan < MP tuwan < PIE *tewh2-';\npython3 $T 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/táwros' --note 'page 507, Tauro root, Semitic *thawr- borrowing';\npython3 $T 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tewh₂-' --note 'page 507, Teu 1 root';\npython3 $T 'https://en.wiktionary.org/wiki/ثور' --note 'page 507, Tauro, Arabic thawr < Proto-Semitic; Persian sowr loan';\npython3 $T 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/steuraz' --note 'page 507, Tauro, steer < PGmc *steuraz (Kroonen)';\npython3 $T 'https://en.wiktionary.org/wiki/طهماسب' --note 'page 507, Teu 1, Tahmasb = tahm brave + asp, Tumaspana rejected';\npython3 $T 'https://en.wiktionary.org/wiki/τύμβος' --note 'page 507, Teu 1, tymbos';\npython3 $T 'https://en.wiktionary.org/wiki/τυρός' --note 'page 507, Teu 1, tyros';\npython3 $T 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þūsundī' --note 'page 507, Teu 1, thousand';\npython3 $T 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þeuhą' --note 'page 507, Teu 1, thigh';\npython3 $T 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þūmô' --note 'page 507, Teu 1, thumb';\npython3 $T 'https://en.wiktionary.org/wiki/tuber' --note 'page 507, Teu 1, Latin tuber';\npython3 $T 'https://vajehyab.com/moein/تخم' --note 'page 507, MON tokhm [په.]';\npython3 $T 'https://vajehyab.com/moein/توبره' --note 'page 507, MON tubreh, no origin tag';\npython3 $T 'https://vajehyab.com/moein/ثور' --note 'page 507, MON sowr [ع.]' 2>&1 | tail -3",
 "timeout": 400000
}
```


### [2026-10-15T02:50:01.905Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bd1b91adb32887d9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7f98ded676d9449d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d912d10a634b144d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/33f923e7cec68e92.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/abe8c98700161887.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9ae1f49de64597cb.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bf13dc295410e544.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c4320a19f31eca86.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b7168d15fbf9a324.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9b8a5ac63591dcce.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/24fb42998cf364c9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1e7f085237adc220.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/60bd5574b5b2c49d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2aa450d58322ebec.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2bcb021ebecf1941.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/87dfd3ca5eb0edd3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e583f13db39ee2f6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4bb8bcd960615f28.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d882b5f4b6bcf163.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e63e35d00919037f.txt
```


## [2026-10-15T02:50:05.595Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; for w in \"TAVAN\\|TAVÂN\\|TOVAN\" \"SOTUR\\|SOTOR\\|SOTÛR\\|SOTUH\\|SOTOH\" \"TOXM\\|TOKHM\\|TOKHOM\" \"TOND\\b\" ; do echo \"== $w\"; grep -n \"$w\" ARY_latin_index_pages.txt | head -3; done; grep -c . ARY_pages.txt; grep -n \"ستور\\|ستوه\\|توان\\b\" ARY_pages.txt | head -5"
}
```


### [2026-10-15T02:50:05.981Z] TOOL RESULT

```
== TAVAN\|TAVÂN\|TOVAN
== SOTUR\|SOTOR\|SOTÛR\|SOTUH\|SOTOH
== TOXM\|TOKHM\|TOKHOM
5457:POKORNY; = SS~S~*~*~*«dR ‘TOHM, TOM, TOXM, TOHMAG
5461:we 1b oly TOKAM, TOXMAN, TOHM
== TOND
15706
22:ارستایی -> پارسی‌باستان -> هند و اروپایی. ولی به دلائلی که در دیباچه آمده همیشه تتوانسته‌ام شاهد
24:۰ ۳-هرجاکه توانسته‌ام واژه‌های همریشه‌ی کردی و بلوچی و افغانی و اوستی و سغدی و ختنی را
148:اگر پذیریم که زبانهای هند و اروپایی از یک زبان واحد سرچشمه گرفته‌اند که می‌توان
170:دستوری و آوایی و واژگان آن) زبان کوچگران هند و اروپایی را متقابلاً تحت تأثیر قرار داد. این
200:گسترش سریح قبایل ترکك نشان می‌دهد که سرعت تهاجم و تصاحب می‌تواند :
```


## [2026-10-15T02:50:08.608Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 5450,5465p ARY_latin_index_pages.txt; awk 'NR<5457 && /\\[pdf page/{l=$0} NR==5457{print l}' ARY_latin_index_pages.txt; grep -n \"STAOR\\|STOR\\b\\|TAV-\\|TAOXM\\|STÖR\\|STAURA\" ARY_latin_index_pages.txt | head"
}
```


### [2026-10-15T02:50:08.970Z] TOOL RESULT

```
84, (ENDEAVOUR) 112
leedloak
a EIN spr lad 5 ely (V5) A paley Gbadhy 22 05s ol
Mee Sinks ©) able ates y sash Us Ss leaks 22 Sls atl
DIEHTER TAOXMAN- AVESTAN) .oleos
TAUMA — (OLD PERSIAN) ol oa
REFERENCES bethy (PAHLAVI) 5.344
POKORNY; = SS~S~*~*~*«dR ‘TOHM, TOM, TOXM, TOHMAG
‘MACKENZIE: (SEED) 132 TOM, TOV, TOXIM (KURDISH) 52,5
BUCK: (SEED) 505-506 TOMA (AFGHAN) (4) gil
AMOMDAROV: (SEED) 283 (SANSKRIT) 4 Smile
we 1b oly TOKAM, TOXMAN, TOHM
- (MIDDLE HIGH GERMAN) di giaST
teeta goin
3 al git 5 5209 al
SANSKRIT) 4 Sie TITAR, TADAR, —:(PAHLAV1) «5.4,
[pdf page 190]
3167:DELAMARRE: (CASTOR) 131 BIBAR
4713:‘DELAMARRE: FODA, FODOR, FEDAN, FOSTOR
5454:DIEHTER TAOXMAN- AVESTAN) .oleos
7207:SWESTRO :(OLD PRUSSIAN) eS 53.2 SWEOSTOR
10105:TJOR, TYR (NORWEGIAN) «5}4,: STAORA., STAWRA-:(AVESTAN) .gl-3!
10106:STIE (DUTCH) sacha STOR PAHLAVI) <5 slgy
10108:TURD ASTOR KURDISH) 53,6
10125:ONINOS: (STEER) 866 STEOR, STOR ea
10128:irr SMdsias abcd TJUR, STOR (SWEDISH) «58 p+
```


## [2026-10-15T02:50:10.807Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk 'NR<10105 && /\\[pdf page/{l=$0} NR==10105{print l}' ARY_latin_index_pages.txt; sed -n 10095,10130p ARY_latin_index_pages.txt | cut -c1-120"
}
```


### [2026-10-15T02:50:11.445Z] TOOL RESULT

```
[pdf page 348]
POKORNY, ——~=~S~*~S*~S*~S*S*~S«CS STUO, STID, STAUN :(OSSETIC) 2-31
DELAMARRE: 287 STAYAL (AFGHANI) (24) gil
MACKENZIE: (PRAISE) 128 SANSKRIT) Ske
wel seb dey STU-, STAU., STAVATE, STAUTI
ent loo
oie Sib
[pdf page 348]
4
\
YA | oe |
TJOR, TYR (NORWEGIAN) «5}4,: STAORA., STAWRA-:(AVESTAN) .gl-3!
STIE (DUTCH) sacha STOR PAHLAVI) <5 slgy
(OLD CHURCH SLAVIC) 5 53+ STURTA HOSSETIC) gm!
TURD ASTOR KURDISH) 53,6
TAURAS — (44U)(LITHUANIAN) gi SUTUR AFGHANI) (gu) lai!
(4LE}(OLD PRUSSIAN) AS gd. STHAVIRAS (SANSKRIT) cy Sits
TAURIS STHAURIN ARMENIAN) 5s)
TARB —(4L4}(OLD IRISH) oyS 5.) p\ TADROS (ayLEY(GREEK) gb y,
TARVOS (4 (GAULISH) SF ‘TAURUS (QUYLATIN) gt
TARW (QU (WELSH) 535 TAUREAU (alt}(FRENCH) «il5
TARO (4LE(BRETON) 35 TORO (ayLE}(SPANISH) pale!
TAROK (ALALBANIAN) glT TORO (QU (TALIAN) ge!
TAUR (ayl2)}(RUMANIAN) gly,
REFERENCES — both TOURO — (4L!}(PORTUGUESE) Js 4
POKORNY ———=—=S*~S*~S~S~S«TO STIUR AGOTHIC) Sa,
BARNHART: (STEER) 1064 (OLD SCANDINAVIAN) AS :he\
DELAMARRE: (TAUREAU) 137 STJORR, THJORR
MACKENZIE: STIOR:(OLD HIGH GERMAN) oS gilt
(CATTLE) 106, (HORSE) 118 STIER GERMAN) glalT
BUCK: 152-155, 145 (OLD ENGLISH) pS guSl |
ONINOS: (STEER) 866 STEOR, STOR ea
SKEAT: (STEER) 601 STEER ENGLISH) 'jy-JS a
wer seb olny aye, stor ipanist Ss
irr SMdsias abcd TJUR, STOR (SWEDISH) «58 p+
Jeathoak
Sipe 9 BF Sale 59 039 gal oe
```


## [2026-10-15T02:50:34.199Z] TOOL CALL #88: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg507.png /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/507.png && ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK | head -3"
}
```


### [2026-10-15T02:50:34.889Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   96k sfmqrb 14 Oct 22:19  33.png
.rw-r--r--   99k sfmqrb 14 Oct 22:19  39.png
```


## [2026-10-15T02:54:38.489Z] TOOL CALL #89: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-507.py",
 "content": "import json\n\nW = \"https://en.wiktionary.org/wiki/\"\nU_TEWH = W + \"Reconstruction:Proto-Indo-European/tewh₂-\"\nU_TAWROS = W + \"Reconstruction:Proto-Indo-European/táwros\"\n\nPOK_TEU = {\"ref\": \"POK:1082\", \"status\": \"supports\", \"note\": \"Pokorny IEW pp.1080-1085 (POK_full.txt line 86576 'Root / lemma: teu- teu-, teuə-, tuə- tu-', 'Meaning: to swell; crowd, folk; fat; strong; boil, abscess'): 'Avestan tav- ' to be capable of ', tavah- n. 'power, force'... ap. atavayam 'I am able', tunuvant- 'mighty'... tauman- n. 'fortune, force, power'' (p.1080).\"}\n\ndef C(src, where, stance, note):\n    return {\"src\": src, \"where\": where, \"stance\": stance, \"note\": note}\n\nWLD_TEU = C(\"WLD\", \"Bd. I pp.706 ff. s.v. teu- (WLD_Bd1_pages.txt line ~66630)\", \"supports\", \"'av. tav- „vermögen“, tavah- n. „Macht, Kraft“, tāviṣī „Körperkraft“; ap. tauman- n. „Vermögen, Kraft, Macht“' under teu- 'schwellen'.\")\nAHD_TEU = C(\"AHD\", \"Watkins 1985 s.v. teuə- (AHD_watkins1985.txt line 1087)\", \"supports\", \"'teuə-. Also teu-. To swell.' with THIGH (*theuham), THOUSAND (*thūs-hundi- 'swollen hundred'), THUMB (*thūmōn- 'the thick finger'), TUMOR (tumēre), TUBER (tūber), BUTTER (Greek tūros 'cheese'), TOMB (Greek tumbos, 'perhaps'). [Pok. teu- 1080.]\")\nKLN_TUMID = C(\"KLN\", \"1966 s.v. tumid (KLN_1966.txt line 40426)\", \"supports\", \"'L. tumidus ... fr. tumere, to swell ... cogn. with OI. tumrah, turgid, fat, Avestic tuma, fat, OE. þuma, thumb ... fr. I.-E. *tumo-, enlargement of base *tu-, to swell, whence also ... OE. þeoh, thigh, and the first element in ... OE. þusend, thousand'; 'Cp. ... tomb'.\")\n\nentries = []\n\n# ---------------- entry 0 -----------------\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"tav; tavant; tum-âspa; us-tavah; ni-us-tavah\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Only tav- is a solid Avestan word: Av. tav-/tauu- 'to be able, strong' (pres. tūite, perf. tūtauua, participle tuuant- V 3.33; noun tavah- n. 'power') continues PIE *tewh₂- 'swell, become strong' (Pokorny, Bartholomae, Cheung *tauH). The other four forms are scholars' reconstructions, not Avestan words with the stated meanings: 'tavant' 'fast, quick' is Horn's starred *tavant- (= *tuvant-) invented to explain NP tund (Horn no. 395) — the attested participle tuuant- means 'being able', never 'fast'; 'tum-âspa' is Pokorny's *Tumāspa- 'whose horses are fat', inferred only from the patronymic tumāspana- (Yt 13.131), and modern work rejects it as the source of Tahmāsp; 'us-tavah' and 'ni-us-tavah' are Nyberg's/Mo'in's reconstructed *us-tavah- 'out of force' and its negation, not attested in the Avesta, and Cheung derives the Persian words from a different root (*staup).\",\n \"derivation_fa\": \"از این پنج صورت تنها tav- واژهٔ واقعی اوستایی است: tav-/tauu- «توانستن، نیرومند بودن» و tavah- «نیرو» از ریشهٔ هندواروپایی آغازین *tewh₂- «باد کردن، نیرومند شدن» (پوکورنی، بارتولومه، چونگ). «tavant» به معنای «تند» ساختهٔ ستاره‌دار هرن (*tavant-) برای توضیح «تند» است و صفت فاعلی اوستایی tuuant- تنها «توانا» معنی می‌دهد؛ «tum-âspa» بازسازی پوکورنی از نام پدرتباری tumāspana- است و پژوهش امروزی آن را خاستگاه «تهماسب» نمی‌داند؛ «us-tavah» و «ni-us-tavah» بازسازی‌های نیبرگ و معین‌اند نه واژه‌های گواهی‌شدهٔ اوستا. بنابراین این خانه جز tav- پذیرفتنی نیست.\",\n \"sources\": [U_TEWH, W + \"توان\", W + \"طهماسب\"],\n \"ref_check\": [\n   POK_TEU | {\"note\": POK_TEU[\"note\"] + \" p.1083 (5. m-derivatives): 'Avestan *tuma- in Tumāspana- from Tumāspa- (that is to say one whose horses are fat) stammend' — the source of Nourai's tum-âspa; no 'us-tavah', no 'tavant' 'fast'.\", \"status\": \"partial\"},\n   {\"ref\": \"HRN:89\", \"status\": \"partial\", \"note\": \"Horn p.89 no. 395 'tund schnell, heftig, stark' — 'aw. *tavant- (= *tuvant-), √tav-, vergl. tuvān (No. 401)'; no. 401 'tuvān vermögend, mächtig ... aw. √tav- können, vermögen ... phl. tuvān'. Horn gives the starred *tavant-, confirming it is a reconstruction.\"},\n   {\"ref\": \"NYB:196\", \"status\": \"supports\", \"note\": \"Nyberg Manual II p.196 (NYB_vol2_glossary.txt line ~3815) 'tuvān [twbʾn'] 1. adj. mighty, powerful, energetic ... 2. impers. vb. it is possible, one can'. And p.180 s.v. stōb: 'I derive it from *us-tavah- out of force, powerless, from Av. (639) tavah-' — the source of us-tavah (a reconstruction).\"}\n ],\n \"consulted\": [\n   C(\"BRT\", \"col. 638-639 s.v. tav-, tavah- (BRT.txt lines 12015, 12029)\", \"supports\", \"'tavah- n. Vermögen, Kraft, Macht ... Zum V. tav-'; tav- '(es) vermögen'; line 12327 'tumāspana- patr. Adj. von Tumāspa- stammend, dessen Nachkomme' — only the patronymic is attested.\"),\n   C(\"CHEUNG\", \"p.385 s.v. *tauH (CHEUNG.txt line 25149)\", \"partial\", \"'*tauH to be able, strong. AVESTAN: tauu- (tu-) to be able, strong ... Partic.: pres. YAv. tuuant- (V 3.33)' — tav- confirmed, but tuuant- means 'able'; s.v. *staup (line 23953) Cheung rejects *tav- as the origin of sutōh.\"),\n   WLD_TEU,\n   C(\"KNT\", \"p.186 s.v. tav- (KNT_full.txt line 25986)\", \"supports\", \"'tav- vb. be strong: Av. tav-, Skt. tu-'; OP atavayam 'I am able'.\")\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"tavân; tond; Tahmâsb; sotŭh; nastŭh\",\n \"verdict\": \"disputed\",\n \"derivation\": \"tavān 'power' (توان, verb tavānestan) is correct: MP tuwān [twbʾn] 'might, power; it is possible' < OIr. *tav-/*tauH- 'be able' (PIE *tewh₂-); NP tavān with the modern a for older u. tond 'fast, sharp' is NOT from tav-: MP tund 'sharp, violent' belongs with Sogd. twnt, Khot. ttunda- and Skt. tud- 'thrust', PIE *(s)teud- (Cheung *tund; Wiktionary); Hübschmann already rejected the link with tuvān. Tahmāsb (Safavid royal name; طهماسب is the Arabicised spelling) is MP Tahmāsp 'having brave horses' = tahm 'brave' (< Av. taxma-, Nyberg: '< *tak-ma-') + asp 'horse' — not from *tuma- 'fat'; Wiktionary explicitly rejects the Tumāspana identification. sotūh 'weary, overcome' and its negation nastūh 'untiring' (Ferdowsi's dīv-e nastūh) go back to MP stōh/stōb 'powerless, defeated' (Parth. ʾstwb 'defeated'): Nyberg and Mo'in derive them from *us-tavah- 'out of force' (Nourai's view), but Cheung (2007) shows the -b- of stōb cannot come from *tav- and derives them from *staup- 'overcome' (PIE *steup- 'strike', Lat. stupēre). So one word confirmed, one plausible-but-contested pair, two disputed.\",\n \"derivation_fa\": \"«توان» درست است: از فارسی میانه tuwān «نیرو، توانایی» و ایرانی باستان *tav- «توانستن» از ریشهٔ هندواروپایی *tewh₂-. ولی «تند» از فارسی میانه tund «تیز، تند» است که چونگ و ویکی‌واژه آن را از ریشهٔ ایرانی *tund-/*taud- «کوبیدن، تندی کردن» (هم‌ریشه با سنسکریت tud- و لاتین tundō، هندواروپایی *(s)teud-) می‌دانند و هوبشمان هم پیوندش را با «توان» نپذیرفته است. «تهماسب» (طهماسب معرّب است) از فارسی میانه Tahmāsp «دارندهٔ اسبان دلیر» است، یعنی «تهم» (دلیر، از اوستایی taxma-) + «اسب»، نه از *tuma- «فربه». «ستوه» و «نستوه» از فارسی میانه stōh/stōb «ناتوان، شکست‌خورده»اند؛ نیبرگ و معین آن را از *us-tavah- «بی‌نیرو» گرفته‌اند (همان رأی نورایی) ولی چونگ به دلیل b در stōb آن را از ریشهٔ *staup- «شکست دادن» می‌داند. پس ادعای نورایی برای «توان» درست، برای «ستوه/نستوه» محل اختلاف، و برای «تند» و «تهماسب» نادرست است.\",\n \"sources\": [W + \"توان\", W + \"تند\", W + \"طهماسب\", W + \"ستوه\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:517\", \"status\": \"partial\", \"note\": \"Borhan vol.1 s.v. تند (BQT_v1_pages.txt leaf 745), Mo'in's footnote: 'اوستا ... از ریشهٔ tav-، قس: توان (توانستن)' and 'هوبشمان رابطهٔ «تند» را با «توان» معتقد نیست (هوبشمان ۳۹۵)' — Mo'in offers Nourai's link but records Hübschmann's rejection.\"},\n   {\"ref\": \"BQT:526\", \"status\": \"supports\", \"note\": \"Borhan vol.1 s.v. توان (BQT_v1_pages.txt leaf 754): 'توان ... قوت وقدرت وتوانایی باشد'; Mo'in: 'اوستا tav- (توانستن، قدرت داشتن) ... پهلوی ... هندی باستان ... ارمنی (ماندن، دوام کردن، تحمل کردن)'.\"},\n   {\"ref\": \"BQT:1102\", \"status\": \"supports\", \"note\": \"Borhan s.v. ستوه (BQT_v2_pages.txt line 33781-33801, pdf page 593): Mo'in: 'پهلوی ... (بی‌زور) ... پازند ... ایرانی باستان *us-tav- از tav (توانستن، قادر بودن)؛ ستوه فارسی مرکب است از us ... (آنکه زورش کم است) ... ضد آن: نستوه (خستگی‌ناپذیر)'.\"},\n   {\"ref\": \"BQT:1362\", \"status\": \"partial\", \"note\": \"Borhan vol.3 (BQT_v3_pages.txt pdf page 156, near طیسفون/طهمورث): Mo'in's note only says 'در سلسلهٔ صفویه دو پادشاه این نام داشتند: شاه طهماسب اول ... طهماسب دوم' — the name is listed, no etymology 'strong horses' given.\"},\n   {\"ref\": \"BQT:2138\", \"status\": \"supports\", \"note\": \"Borhan vol.4 p.2138 (ref_page.py OCR, BQT_v4 pdf page 221): 'نستوه ... ستیزنده و جنگ‌آور ... (Mo'in) خستگی ناپذیر، ناافتاده ... ضد «ستوه» (ه.م.)' — confirms the meaning and the link to ستوه, no further etymology.\"}\n ],\n \"consulted\": [\n   C(\"CHEUNG\", \"p.385 *tauH; p.390 *tund; p.366 *staup (CHEUNG.txt lines 25149, 25401, 23953)\", \"contradicts\", \"*tauH: 'BMP twbʾn- /tuwān-/ to be able, ... /tuwān/ might, power' (supports tavān). *tund: 'MMP tund ... sharp, violent ... NP tund violent, sharp ... PIE *(s)teud- to thrust' (contradicts). *staup: 'NP sutōh ... The root *tav- (i.e. *tauH) suggested by Ghilain (accepted in Nyberg) ... meets phonological (and semantic) difficulties, as it leaves -b- unexplained ... PIE *steup-' (contradicts).\"),\n   C(\"NYB\", \"Manual II p.180 s.v. stōb, p.188 s.v. tahm, p.196 s.v. tuvān (NYB_vol2_glossary.txt lines 3544, 3698, ~3815)\", \"partial\", \"stōb: '... developed to ... stoh, which prevailed: Paz. stoh, stuh, NP sutūh ... I derive it from *us-tavah- out of force, powerless' (supports sotūh); tahm: 'brave, valiant — Av. taxma-; NP tah(a)m; < *tak-ma-' (contradicts Tahmāsb < *tuma-); tuvān 'mighty, powerful' (supports).\"),\n   C(\"HUB\", \"p.48 no. 395 (HUB.txt line 1650)\", \"contradicts\", \"'Dass tund schnell, heftig, scharf, spitz (aus *tuvant-?) nahe verwandt mit tuvān vermögend, fähig sei, glaube ich nicht.'\"),\n   C(\"HRN\", \"p.89 nos. 395, 401 (HRN.txt lines 3718, 3744)\", \"partial\", \"395 'tund schnell, heftig, stark — aw. *tavant- (= *tuvant-), √tav-'; 401 'tuvan vermögend, mächtig ... aw. √tav-'. Horn supports tavān and (with a starred form) tund.\"),\n   C(\"PHD\", \"MacKenzie pp.80-84 (PHD_mackenzie.txt lines 623, 4685, 5023, 5030)\", \"partial\", \"'tahm [thm] strong, brave'; 'stōb [stwb, P ʾstwb, N sutōh] distressed, defeated'; 'tund [twnd] sharp, violent'; 'tuwān [twbʾn] might, power' — MacKenzie gives the MP forms without derivation from *tav- for stōb or tund.\")\n ],\n \"quote_note\": \"Chart quotes Ferdowsi: بیازید هوشنگ چون شیرچنگ - جهان کرد بر دیو نستوه تنگ\"\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"tŭbreh\",\n \"verdict\": \"plausible\",\n \"derivation\": \"NP tūbre (توبره) 'nosebag, haversack' continues MP tōbrag 'bag, sack'; the word spread as a Middle Iranian loan to Armenian toprak, Syriac ṭūbarqā 'nosebag of an ass', Arabic ṭarbūq and Turkish torba (whence Slavic torba). Mann (IEC) sets up an IE *tūbhor- 'ball, bag' with Latin tūber 'lump' and Persian tūbre, but marks the Persian 'ambig.'; Wiktionary compares only Skt. ṭopara 'small bag' (retroflex ṭ, suggesting a non-IE Wanderwort). MP ō could reflect *au < *teubh-, so a link with the 'swell' root is phonologically possible but is supported only by Mann; no Iranian etymological dictionary (Horn, Hübschmann, Mo'in) endorses it.\",\n \"derivation_fa\": \"«توبره» (کیسهٔ خوراک چارپا، کوله) از فارسی میانه tōbrag «کیسه» است و همین واژه به‌صورت وام‌واژه به ارمنی (toprak)، سریانی (ṭūbarqā)، عربی و ترکی (torba) رفته است. مان آن را با لاتین tūber «برآمدگی» از *tūbhor- «گوی، کیسه» و ریشهٔ «باد کردن» پیوند داده ولی خودش صورت فارسی را «مبهم» خوانده است؛ ویکی‌واژه تنها سنسکریت ṭopara «کیسهٔ کوچک» را مقایسه می‌کند که بیشتر نشانهٔ واژه‌ای سرگردان (Wanderwort) است. پیوند نورایی ناممکن نیست ولی جز مان پشتوانه‌ای ندارد؛ با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"توبره\", \"https://vajehyab.com/moein/توبره\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:1450\", \"status\": \"supports\", \"note\": \"Mann IEC (IEC.txt line 19223) 'tūbhor- ball, bag. Per. ambig., cf. tūpəlos. Per. tūbre, s. bag; (LW in) Tk. torba, id. (whence Slav. id.); Oss. (LW) dobra ... Lat. tūber, n. lump, puffball' — Nourai's source, with Mann's own caveat 'ambig.'.\"},\n   {\"ref\": \"IEC:1458\", \"status\": \"partial\", \"note\": \"Mann (IEC.txt line 19329) 'tūpəlos (tūpulos) bulge; dolt. Per. ambig. cf. tūbhor-. Skt. tūparáḥ hornless ... Per. tūbre, s. (LW in Tk. torba)' — same Persian word set under a second root, showing Mann's uncertainty.\"}\n ],\n \"consulted\": [\n   C(\"MON\", \"vajehyab.com/moein/توبره\", \"silent\", \"'(رِ) (اِ.) ۱- کیسه‌ای که مسافران و شکارچیان ابزار کار و خوراک خود را در آن گذارند. ۲- کیسه‌ای بنددار که در آن کاه و جو ریزند و به گردن چارپایان بندند' — no origin tag.\"),\n   C(\"HRN\", \"grep 'tūbre|tōbra|tubra' in HRN.txt\", \"silent\", \"no entry for tūbre in Horn's Grundriss.\"),\n   C(\"PHD\", \"grep 'tōbrag' in PHD_mackenzie.txt\", \"silent\", \"no hit (OCR); the MP form tōbrag is cited by Wiktionary.\"),\n   C(\"BQT\", \"grep 'توبره' in BQT_v1_pages.txt\", \"silent\", \"the headword was not found in the OCR text of vol. 1 (OCR gaps).\")\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Latin\",\n \"words\": \"tuměre; tŭber\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin tumēre 'to swell, be swollen' is a stative -ē- verb from the zero-grade extended root *tum- (PIE *tewh₂- 'swell'), whence tumor, tumidus, tumulus. Latin tūber 'lump, swelling, truffle' continues *tūbh-es-/-os- (Proto-Italic *tūβos), a bh-extension of the same root; de Vaan is cautious about the exact morphology, but the root attribution is standard (Pokorny, Watkins, Klein, Walde-Pokorny). Nourai's gloss 'lump, bag' for tūber: 'lump' is right, 'bag' is his own bridge to Persian tūbre.\",\n \"derivation_fa\": \"لاتین tumēre «باد کردن، ورم داشتن» فعل حالتی از پایهٔ ضعیف *tum- ریشهٔ هندواروپایی *tewh₂- «باد کردن» است و tumor «ورم» و tumulus «پشته» از آن ساخته شده‌اند. tūber «برآمدگی، غده، دنبلان» از گسترش bh همان ریشه (*tūbh-) است. ادعای نورایی درست است، جز آنکه معنای «کیسه» برای tūber ساختهٔ خود اوست و معنای واقعی «برآمدگی» است.\",\n \"sources\": [W + \"tuber\", U_TEWH],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. teuə- (AHD_watkins1985.txt line 1087): '4b. suffixed (stative) form *tum-ē- in Latin tumēre, to swell, be swollen ... TUMOR'; '5. Extended lengthened zero-grade form *tūbh- in Latin tūber, lump, swelling: TRUFFLE, TUBER'.\"}],\n \"consulted\": [\n   C(\"POK\", \"pp.1080-1081, 1083 s.v. teu- (POK_full.txt line 86576 ff.)\", \"supports\", \"'1. bh-extension: Latin tūber, -eris n. hunch, swelling, blister, tumefaction, knag'; '5. m-derivatives: ... Latin tumeō, -ēre geschwollen sein, tumidus swollen, tumor swelling, tumulus Erdhaufen'.\"),\n   C(\"KLN\", \"1966 s.v. tuber (KLN_1966.txt line 40376) and tumid (line 40426)\", \"supports\", \"'tuber ... L. tuber, a swelling, hump, protuberance, fr. I.-E. *tu-bh-, to swell'; 'tumid ... fr. tumere, to swell'.\"),\n   C(\"LEW\", \"grep tumeo/tuber in LEW_1910.txt\", \"silent\", \"not consulted in detail; Walde-Hofmann II 712 ff. is cited by Pokorny for this group.\"),\n   C(\"IEC\", \"s.v. tumo (IEC.txt line 19300)\", \"supports\", \"'tumo, eiō swell ... Lat. tumeo, ēre, v. swell, increase'.\")\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"English\",\n \"words\": \"tumor\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English tumor (British tumour), first a 'swelling' (late Middle English, 16th c. in the modern spelling), was borrowed from Latin tumor 'swelling, protuberance', the action noun of tumēre 'to swell'; the medical sense 'morbid growth' developed in English medicine.\",\n \"derivation_fa\": \"انگلیسی tumor «غده، تومور» در انگلیسی میانهٔ پسین و سدهٔ ۱۶ از لاتین tumor «ورم، برآمدگی»، اسم‌مصدر tumēre «باد کردن»، وام گرفته شد و معنای پزشکی «رشد بیمارگونه» در خود انگلیسی پدید آمد. ادعای نورایی درست است.\",\n \"sources\": [U_TEWH],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. teuə-: 'Latin tumēre, to swell ...: TUMESCENT, TUMID, TUMOR'.\"}],\n \"consulted\": [\n   C(\"KLN\", \"1966 s.v. tumor (KLN_1966.txt line 40427)\", \"supports\", \"'tumor, tumour, n. — L. tumor, swelling, protuberance, fr. tumere'.\"),\n   C(\"SKT\", \"grep 'tumour' in SKT.txt\", \"silent\", \"Skeat lists tumour < Latin tumor < tumere (not quoted; Klein suffices).\")\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Greek\",\n \"words\": \"turus; tumbus\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Nourai's turus = Greek tūrós 'cheese' (Mycenaean tu-ro), probably PIE *tuh₂-ró- from *tewh₂- 'swell' ('the curdled, thickened [milk]'), cognate with Av. tūiri- 'curdled milk, whey' (Pokorny 1081, Watkins, Klein); Wiktionary notes an alternative link with OE ġeþweor 'curds' (a 'churn' root), so 'probable'. His gloss 'butter' is loose: butter is boútȳron 'cow-cheese' (bous + tūros). tumbus = Greek túmbos 'burial mound, tomb', which Watkins lists under this root only as 'perhaps' (nasalised *tu-m-b(h)-) and Beekes treats as a Pre-Greek/Mediterranean substrate word. So tūros confirmed-probable, túmbos plausible.\",\n \"derivation_fa\": \"یونانی tūrós «پنیر» (در یونانی موکنایی tu-ro) به احتمال قوی از *tuh₂-ró- از ریشهٔ *tewh₂- «باد کردن، سفت شدن (شیر)» است و با اوستایی tūiri- «شیر بسته، دوغاب» هم‌ریشه است؛ معنای «کره» که نورایی آورده دقیق نیست و «کره» در یونانی boútȳron «پنیر گاو» است. túmbos «گور، پشتهٔ خاک» را واتکینز تنها «شاید» از این ریشه دانسته و بیکس آن را واژه‌ای از زیرلایهٔ مدیترانه‌ای می‌شمارد. پس tūrós پذیرفته و túmbos با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"τυρός\", W + \"τύμβος\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. teuə-: '6. Suffixed zero-grade form *tū-ro- in Greek tūros, cheese (< a swelling, coagulating): BUTTER'; '10. Perhaps nasalized extended form *tu-m-b(h)- ... in Greek tumbos, barrow, tomb: TOMB'.\"}],\n \"consulted\": [\n   C(\"POK\", \"pp.1081-1083 s.v. teu- (POK_full.txt lines ~86700, ~86650)\", \"supports\", \"'Avestan tūiri- n. caseous gewordene milk, whey ... ablaut. *tū-ro- in gr. τῡρός cheese, βού-τῡρον butter'; 'gr. τύμβος burial mound, hillock = Middle Irish tomm hill, bush ... whether not but from *tubh-mo-'.\"),\n   C(\"KLN\", \"1966 s.v. tyro- (line 40636), butter (line 5969), tomb (line 39476)\", \"supports\", \"'Gk. τυρός cheese, cogn. with OI. tūraḥ, Avestic tūiri-, curds, whey ... possibly derive fr. I.-E. base *tū-, to swell'; butter 'fr. Gk. βούτυρον, butter, lit. cow cheese'; tomb 'fr. Gk. τύμβος, sepulchral mound, tomb, which is cogn. with ...'.\"),\n   C(\"WLD\", \"Bd. I pp.709-713 s.v. teu-\", \"supports\", \"Walde-Pokorny list τυρός and τύμβος in the teu- 'schwellen' family (Pokorny's source).\")\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"English\",\n \"words\": \"butter, tomb\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"butter: OE butere < West Germanic loan from Latin būtȳrum < Greek boútȳron 'butter', literally 'cow-cheese' (boûs 'cow' + tūrós 'cheese'); only the second element belongs to the 'swell' root. tomb: Middle English tumbe/toumbe < Anglo-French/Old French tombe < Late (ecclesiastical) Latin tumba < Greek túmbos 'burial mound'. Both chains are uncontroversial; the ultimate root attribution of túmbos is the uncertain part (see #6).\",\n \"derivation_fa\": \"انگلیسی butter «کره» از انگلیسی باستان butere، از لاتین būtȳrum و یونانی boútȳron «پنیر گاو» (boûs «گاو» + tūrós «پنیر») است، پس تنها جزء دوم آن به این ریشه می‌رسد. tomb «گور» از فرانسوی کهن tombe و لاتین کلیسایی tumba از یونانی túmbos است. این زنجیره‌ها پذیرفته‌اند؛ ادعای نورایی درست است.\",\n \"sources\": [W + \"τυρός\", W + \"τύμβος\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of Nourai's own; AHD teuə- (BUTTER, TOMB) covers it.\"}],\n \"consulted\": [\n   C(\"KLN\", \"1966 s.v. butter (line 5969), tomb (line 39476)\", \"supports\", \"'butter, n. — OE. butere ... fr. L. butyrum ... fr. Gk. βούτυρον, butter, lit. cow cheese, which is compounded of βοῦς, ox, cow, and τυρός, cheese'; 'tomb, n. — ME. toumbe, tombe, fr. OF. tombe, fr. Eccles. L. tumba ... fr. Gk. τύμβος, sepulchral mound, tomb'.\"),\n   C(\"AHD\", \"Watkins s.v. teuə- items 6, 10\", \"supports\", \"BUTTER and TOMB listed as English derivatives.\")\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Germanic\",\n \"words\": \"thŭmon; thus-hundai; thiuham\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *þūmô 'thumb' < PIE *tuh₂-m-ō 'the swollen (big) finger' (Wiktionary, Watkins *tūm-, Pokorny 1083: OE þūma, OHG dūmo, ON þumall). *þūsundī 'thousand' (Goth. þūsundi, ON þúshundrað) is analysed as *þūs-hundi 'swollen/fat hundred' (Watkins, Kroonen *tuHs-dḱm̥to-), or as *tuHs-ont- 'great (number)' — either way from the s-stem of the 'swell, be strong' root (Skt. tavas-, Av. tavah-), so Nourai's thus-hundai matches Pokorny's 'Germanic *Þus-hundi'. *þeuhą 'thigh' (OE þēoh, ON þjó) < *tewk-, the k-extension 'to swell, fat' (Pokorny 1081, Watkins *teuk-, Klein). Nourai's spellings are informal renderings of these reconstructions.\",\n \"derivation_fa\": \"ژرمنی آغازین *þūmô «شست» از *tuh₂-m-ō «انگشتِ ستبر» است؛ *þūsundī «هزار» را واتکینز و کرونن «صدِ باد کرده/بزرگ» (*þūs-hundi) و برخی *tuHs-ont- «شمار بزرگ» می‌دانند که هر دو به صورت s‌دار همین ریشه (همانند سنسکریت tavas- و اوستایی tavah- «نیرو») می‌رسند؛ *þeuhą «ران» از گسترش k ریشه (*tewk- «فربه شدن») است. انگلیسی thumb، thousand و thigh از این‌ها آمده‌اند. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Germanic/þūmô\", W + \"Reconstruction:Proto-Germanic/þūsundī\", W + \"Reconstruction:Proto-Germanic/þeuhą\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. teuə-: '1. Extended form *teuk- in Germanic *theuham, the swollen or fat part of the leg, thigh ... THIGH. 2. Extended form *tūs- in Germanic compound *thūs-hundi-, swollen hundred, thousand ... THOUSAND ... 4a. Germanic *thūmōn- in Old English thūma, thumb (< the thick finger)'.\"}],\n \"consulted\": [\n   C(\"POK\", \"pp.1081-1084 s.v. teu- (POK_full.txt lines ~86680-86760)\", \"supports\", \"'3. k-extension: to swell; fat ... Old High German dioh, Old English þēoh thigh'; '5. m-derivatives ... Old English þūma thumb'; '8. s-formations ... the Germanic and Balto-Slavic word for thousand: Gothic þūsundi ... Old Icelandic þūshund (Germanic *Þus-hundi- Vielhundert, Indo-Germanic *tūs-ḱmtī)'.\"),\n   C(\"KLN\", \"1966 s.v. thigh (line 39033), tumid (line 40426)\", \"supports\", \"'thigh ... OE. þeoh ... fr. I.-E. base *tū-, *teu-, to swell'; tumid: 'OE. þuma, thumb ... first element in ... Goth. þūsundi, OE. þusend, thousand'.\"),\n   C(\"SYN\", \"Buck §13.37 'thousand'\", \"silent\", \"not quoted; Buck discusses the Germanic/Balto-Slavic 'thousand' as 'swollen hundred' (referenced by Pokorny/Watkins).\")\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"English\",\n \"words\": \"thumb; thousand; thigh\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Inherited, not borrowed: OE þūma > ME thoumbe > thumb (the -b is a 13th-c. excrescent spelling); OE þūsend > thousand; OE þēoh, þīoh > ME thegh, thih > thigh, each the regular English reflex of the Proto-Germanic forms in #8 (Grimm's law *t > þ).\",\n \"derivation_fa\": \"این سه واژه وام نیستند و از ژرمنی به انگلیسی به ارث رسیده‌اند: انگلیسی باستان þūma > thumb (حرف b از سدهٔ ۱۳ افزوده شد)، þūsend > thousand، þēoh > thigh؛ t هندواروپایی طبق قانون گریم در ژرمنی به þ (ث) بدل شده است. درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Germanic/þūmô\", W + \"Reconstruction:Proto-Germanic/þeuhą\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given on this node; AHD teuə- (THUMB, THOUSAND, THIGH) covers it.\"}],\n \"consulted\": [\n   C(\"KLN\", \"1966 s.v. thigh (line 39033)\", \"supports\", \"'thigh, n. — ME. theh, thih, thigh, fr. OE. þeoh, þioh'.\"),\n   C(\"AHD\", \"Watkins s.v. teuə-\", \"supports\", \"THIGH, THOUSAND, THUMB listed as English derivatives of teuə-.\")\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Indo-European\",\n \"words\": \"Teuk\",\n \"verdict\": \"plausible\",\n \"derivation\": \"PIE *tewk- 'sprout, seed, offspring' (Pokorny 1085 teuk-: Skt. tuc- 'children', tókman- 'young shoot', Av. taoxman- 'seed', OP taumā 'family', NP tuxm) is a real reconstructed root (Wiktionary *tewk-). Placing it as an offshoot of *tewh₂- 'swell' follows Pokorny's own cross-reference 'perhaps to teu-k- to swell' — a possible but unproven connection; the root itself is secure.\",\n \"derivation_fa\": \"ریشهٔ هندواروپایی *tewk- «جوانه، تخم، فرزند» (پوکورنی ۱۰۸۵) ریشه‌ای پذیرفته است و سنسکریت tókman- «جوانه»، اوستایی taoxman- «تخم» و پارسی باستان taumā «تبار» از آن‌اند. اما وابستن آن به *tewh₂- «باد کردن» تنها حدس «شاید» پوکورنی است؛ پس خود ریشه درست و پیوندش با ریشهٔ اصلی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"تخم\"],\n \"ref_check\": [{\"ref\": \"POK:1085\", \"status\": \"supports\", \"note\": \"Pokorny p.1085 (POK_full.txt line 86424) 'teuk- Meaning: sprout, seed, offspring. Old Indie tuc- Kinder, progeny ... tókman- young stem, sprout, Avestan taoxman- n. seed, sperm, germ, sprout, Pl. kinship. Old pers. taumā family ... np. tuxm ... See also: perhaps to teu-k- to swell, above S. 1081'.\"}],\n \"consulted\": [\n   C(\"WLD\", \"Bd. I p.713 (WLD_Bd1_pages.txt line 67345)\", \"supports\", \"'tokma-ḥ junger Halm, Schößling, av. taoxman- n. Keim, Same; Pl. Verwandtschaft, ap. taumā f. (s. dazu Bthl. Wb. 623 f.)'.\"),\n   C(\"AHD\", \"grep 'teuk' in AHD_watkins1985.txt\", \"silent\", \"Watkins has no separate *teuk- 'seed' root (only *teuk- 'fat' under teuə-).\"),\n   C(\"ARY\", \"Aryanpur Latin index pdf page 190 (ARY_latin_index_pages.txt line 5454)\", \"supports\", \"groups TAOXMAN- (Avestan), TAUMA (Old Persian), TOHM/TOXM (Pahlavi), TOKMAN (Sanskrit) under one root citing Pokorny.\")\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Avestan\",\n \"words\": \"taoxman\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan taoxman- n. 'seed, germ' (pl. 'kinship'), from Proto-Iranian *tauxman- (Wiktionary *táwxma), PIE *tewk-men-; the -xm- reflects OIr. *-k- before m (spirantised to x), cf. Skt. tókman- 'young shoot'. Attested e.g. Yt 12.17, V 2.25 ('taoxma ... pasvąmca staoranąmca').\",\n \"derivation_fa\": \"اوستایی taoxman- «تخم، نطفه، جوانه» (در جمع «خویشاوندی») از ایرانی آغازین *tauxman- و هندواروپایی *tewk-men- است؛ k پیش از m در ایرانی به x سایشی شده است و با سنسکریت tókman- «جوانه» هم‌ریشه است. ادعای نورایی درست است.\",\n \"sources\": [W + \"تخم\"],\n \"ref_check\": [{\"ref\": \"POK:1085\", \"status\": \"supports\", \"note\": \"Pokorny p.1085: 'Avestan taoxman- n. seed, sperm, germ, sprout, Pl. kinship'.\"}],\n \"consulted\": [\n   C(\"BRT\", \"col. 623 s.v. taoxman- (BRT.txt line 11787)\", \"supports\", \"'taoxman- n. 1) Same, Keim: ... 2) Plur. Verwandtschaft'.\"),\n   C(\"HRN\", \"p.84 no. 378 (HRN.txt line 3553)\", \"supports\", \"'tuxm Same, Geschlecht ... ap. taumā Geschlecht; aw. taoxman-; phlv. tōxm ... ai. tokman- Schössling'.\")\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Persian\",\n \"words\": \"toxm\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP toxm/tokhm (تخم) 'seed, egg, testicle' and tokhme 'race, lineage' < Parthian/NW Middle Iranian tōxm 'seed, line' (Wiktionary, Nyberg: NW *tauxman-) — the SW (Persian proper) form was tōhm (OP taumā, MP tōhm, Arm. loan tohm), so the NP form with -xm is a north-western (Parthian) form taken into Persian. OIr. *au > MP ō > NP o/u; Arabic borrowed it as tukhm 'arab. LW' (Horn). Mo'in tags it [په.].\",\n \"derivation_fa\": \"«تخم» (و «تخمه»، «تخمک») از پارتی/فارسی میانهٔ شمال‌غربی tōxm «تخم، نژاد» است؛ صورت جنوب‌غربی (پارسی) این واژه tōhm بوده (پارسی باستان taumā، فارسی میانه tōhm، وام‌واژهٔ ارمنی tohm)، پس «تخم» فارسی نو صورت شمال‌غربی است. au ایرانی باستان در فارسی میانه ō و در فارسی نو o/u شده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"تخم\", \"https://vajehyab.com/moein/تخم\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:84\", \"status\": \"supports\", \"note\": \"Horn p.84 no. 378: 'tuxm Same, Geschlecht, tuxme; arab. LW. tuxm. ap. taumā Geschlecht; aw. taoxman-; phlv. tōxm, tōxmak ... ai. tokman- Schössling'.\"},\n   {\"ref\": \"MON:1052\", \"status\": \"supports\", \"note\": \"Mo'in (vajehyab.com/moein/تخم): '(تُ) [په.] (اِ.) ۱- نطفه. ۲- بیضهٔ ماکیان ... ۳- اصل، نسب، نژاد. ۴- بذر گیاه' — Pahlavi origin, meanings seed/egg/lineage.\"}\n ],\n \"consulted\": [\n   C(\"NYB\", \"Manual II p.194 s.v. tōhm (NYB_vol2_glossary.txt line ~3791)\", \"supports\", \"'tōhm [twhm], tōm ... seed, extraction, descent; sperm ... 1. NW *tauxman-: Av. taoxman-; MPrth twxm; Paz. NP tuxm; 2. SW *tauhma-: OP taumā- family'.\"),\n   C(\"PHD\", \"MacKenzie (PHD_mackenzie.txt lines 625, 5005)\", \"supports\", \"'tōhm(ag) [twhm(k), M twhm, N tuxm]' ; 'tōhmag ... seed; stock, family'.\"),\n   C(\"HUB\", \"p.? (HUB.txt line 8988)\", \"supports\", \"'tuxm Same, Geschlecht = zd. taoxman-, pāz. tuxm, arm. tohm (aber ap. tauma-!)'.\"),\n   C(\"ARY\", \"Latin index pdf page 190\", \"supports\", \"TOHM, TOM, TOXM, TOHMAG (Pahlavi) with TAOXMAN- (Avestan).\")\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Sogdian\",\n \"words\": \"txm\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian txm- (taxm/təxm, also spelt twxmy) 'seed, descendant, child' < OIr. *tauxman-, with the Sogdian reduction of the diphthong in a closed syllable; cf. the compound mrtxm- 'man, people' (*martiya-tauxma- 'of human seed'). Gharib's 'seed, family' matches.\",\n \"derivation_fa\": \"سغدی txm- (taxm) «تخم، نسل، فرزند» از ایرانی باستان *tauxman- است و واکهٔ مرکب در سغدی کوتاه شده است؛ واژهٔ مرکب mrtxm «مردم» (از «مرد» + «تخم») نیز از آن است. ادعای نورایی درست است.\",\n \"sources\": [W + \"تخم\"],\n \"ref_check\": [{\"ref\": \"SOD:387\", \"status\": \"supports\", \"note\": \"Gharib SOD entry 9735 (SOD_pages.txt line 31829): '9735 txm- C taxm, təxm ... nom. txmy, acc. txmw; pl. txmty =*twxmy ... seed, descendant, child' (Nourai's 387 is a page number near this entry).\"}],\n \"consulted\": [\n   C(\"SOD\", \"entry 9735\", \"supports\", \"'seed, descendant, child'.\"),\n   C(\"POK\", \"p.1085 s.v. teuk-\", \"silent\", \"Pokorny lists Khotanese ttumaa- and NP tuxm but no Sogdian form.\")\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Old Persian\",\n \"words\": \"taumâ\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian taumā- f. 'family' (DB 1.8 'amāxam taumā' 'our family', etc.), spelt t-u-m-a for *tauhmā: OIr. *-xm- became OP -hm- (Kent §103), while Median/Avestan kept -xm- (taoxman-). It continues *tewk- (Pokorny 1085). Kent separates it from tauman- 'power' (< tav-). The empty box to its right on the printed page has no Persian word; MP tōhm is its Persian continuant.\",\n \"derivation_fa\": \"پارسی باستان taumā «خاندان، تبار» (در کتیبهٔ بیستون: amāxam taumā «خاندان ما») در اصل tauhmā خوانده می‌شود: xm ایرانی باستان در پارسی باستان به hm بدل شده ولی در مادی و اوستایی (taoxman-) مانده است؛ دنبالهٔ آن در فارسی میانه tōhm است. کنت آن را از tauman- «نیرو» جدا می‌کند. ادعای نورایی درست است.\",\n \"sources\": [W + \"تخم\"],\n \"ref_check\": [\n   {\"ref\": \"KNT:185\", \"status\": \"supports\", \"note\": \"Kent p.185 (KNT_full.txt line 25869): 'taumā- sb. family: Av. taoxman-, NPers. tuxm, Skt. tokám offspring, tókman- ...; -xm- became OP -hm- ... taumā nsf. DB 1.8; 4.56 ...'.\"},\n   {\"ref\": \"HID:211\", \"status\": \"not_found\", \"note\": \"HID p.211 (leaf 225) is the start of the OP reading glossary (arsan-, xšaça-, xšāyaθiya- ...); taumā is not on that page. Elsewhere (HID.txt leaf 57) Bartholomae gives 'z. taoxman-, p. taumā'.\"},\n   {\"ref\": \"BST:233\", \"status\": \"supports\", \"note\": \"Horn/Sanjana vol. (BST.txt leaf 252, glossary of OP texts): '* taumā-, sb. f. perhaps tau(h)mā, Aw. taokhman, Mod. P. tukhm; race, family' — the leaf prints a page ~2 off from 233.\"}\n ],\n \"consulted\": [\n   C(\"NYB\", \"Manual II p.194 s.v. tōhm\", \"supports\", \"'2. SW *tauhma-: OP taumā- family (thus spelt for tauhmā-); Arm. lw. tohm; MPrs twhm'.\"),\n   C(\"BRT\", \"col. 623 (BRT.txt line 11787 'Bthl. Wb. 623f.' cited by WLD)\", \"supports\", \"Bartholomae lists ap. taumā- with taoxman-.\"),\n   C(\"KNT\", \"p.185\", \"supports\", \"see ref_check.\")\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Indo-European\",\n \"words\": \"Tauro\",\n \"verdict\": \"plausible\",\n \"derivation\": \"PIE *táwros 'bull, aurochs' (Gk. taûros, Lat. taurus, Osc. ταυρομ, OPruss. tauris, Lith. tauras, OCS turъ, with *s- mobile in Av. staora-, Gmc. *steuraz) is a solid reconstruction, but its origin is debated: Pokorny (1083) sets it under teu- 'swell' only as one option, the other being a connection with Proto-Semitic *ṯawr- through an oriental bull cult; Walde-Pokorny note that assigning it to teu- presupposes that the Semitic word is the borrowing; Watkins (AHD) derives it instead from *stā- 'stand' via *stau-ro- 'stout'; Wiktionary says 'borrowed from or into Proto-Semitic *ṯawr-, or both from a common unknown source' (the unconditioned *a points to non-IE origin); Klein calls it 'prob. of Sem. origin'. Nourai's placement under Tĕu 'to swell' is therefore one minority option.\",\n \"derivation_fa\": \"واژهٔ هندواروپایی *táwros «گاو نر، گاو وحشی» (یونانی taûros، لاتین taurus، لیتوانیایی tauras، اسلاوی کهن turъ؛ و با s آغازین در اوستایی staora- و ژرمنی *steuraz) بازسازی استواری است، ولی خاستگاهش محل اختلاف است: پوکورنی آن را با تردید زیر ریشهٔ «باد کردن» آورده و احتمال پیوند با سامی آغازین *ṯawr- را هم داده؛ واتکینز آن را از *stā- «ایستادن» می‌داند؛ ویکی‌واژه و کلاین آن را وام از سامی یا از زبانی ناشناخته می‌شمارند (واکهٔ a نشانهٔ غیرهندواروپایی بودن است). پس قرار دادن آن زیر «Tĕu» با احتیاط پذیرفتنی است.\",\n \"sources\": [U_TAWROS],\n \"ref_check\": [\n   {\"ref\": \"POK:1083\", \"status\": \"partial\", \"note\": \"Pokorny p.1083 (POK_full.txt line ~86718) '7. a: das word for bull: gr. ταῦρος, alb. tarok, Latin taurus ... either from Indo Germanic *tāuro-s (compare Old Indie tura- plentiful as epithet of Stieres), or because of orientalischen Stierkultes with Proto Semitic *tauru (arab. ṯwr) connected' — Pokorny leaves both options open.\"},\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins (AHD_watkins1985.txt line 1069) 'tauro-. Bull. Derivative of stā-, but an independent word in Indo-European. Greek tauros (> Latin taurus)'; under stā- IV.4 'Variant *tau-ro-, bull' — the root is right, but Watkins attaches it to stā-, not teuə-.\"}\n ],\n \"consulted\": [\n   C(\"WLD\", \"Bd. I p.711 s.v. teu- (WLD_Bd1_pages.txt line 67070-67090)\", \"partial\", \"'lat. taurus Stier ... Die Zuteilung dieser Gruppe zu teu- schwellen setzt voraus, daß Übereinstimmung mit ursemit. tauru (aram. tōr, hebr. šōr) durch Entlehnung ins Semitische, nicht umgekehrt ... durch solche aus dem Sem. ins Idg. zu erklären ist'.\"),\n   C(\"KLN\", \"1966 s.v. Taurus (line 38297), steer n. (line 36689)\", \"contradicts\", \"'L. taurus, bull ... prob. of Sem. origin. Cp. Aram. tōrā, Heb. shōr, Akkad. shūru, Arab. thōr'; steer: 'All these words are prob. borrowed — directly or indirectly — from the Sem. languages'.\"),\n   C(\"IEC\", \"grep 'tauros' (IEC.txt line 18466)\", \"silent\", \"Mann mentions tauros only in passing (Celtic metathesis tarwos).\"),\n   C(\"ARY\", \"Latin index pdf page 348 (ARY_latin_index_pages.txt line 10105)\", \"supports\", \"Aryanpur groups STAORA-/STAWRA- (Avestan), STOR (Pahlavi), TAUROS (Greek), TAURUS (Latin), STIUR (Gothic), STEOR (OE), STEER under one entry with Pokorny.\")\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"Avestan\",\n \"words\": \"staura, staora\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Avestan staora- 'large domestic animal (horse, cattle)' is well attested (V 2.25 'pasvąmca staoranąmca', V 5.39, compounds drvō.staora- 'keeping the cattle healthy', aγryō.staora-), from Proto-Iranian *stáwra-. Its link with *táwros is the s-mobile hypothesis (Wiktionary lists Indo-Iranian *stáwras as a descendant of *(s)táwros); Pokorny (1010) and Walde-Pokorny instead derive staora- and Gmc. *steuraz from *steu-ro- 'stout' (Skt. sthūra- 'thick, strong') and keep them apart from *tauros, and Kroonen suggests a substrate word. 'staura' is not a separate Avestan spelling — only staora- is attested.\",\n \"derivation_fa\": \"اوستایی staora- «چارپای بزرگ (اسب و گاو)» واژه‌ای گواهی‌شده است (وندیداد ۲.۲۵ و ۵.۳۹ و ترکیب drvō.staora-) از ایرانی آغازین *stáwra-. پیوند آن با *táwros «گاو نر» بر فرض s آغازینِ افتادنی استوار است (ویکی‌واژه همین را می‌پذیرد) ولی پوکورنی و والده آن را از *steu-ro- «ستبر، استوار» (هم‌ریشه با سنسکریت sthūra- «ستبر») جدا می‌کنند. صورت «staura» در اوستا گواهی نشده و تنها staora- درست است. پس واژه درست و پیوندش با Tauro با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"ستور\", U_TAWROS],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; Pokorny p.1010 and Bartholomae were checked instead (see consulted).\"}],\n \"consulted\": [\n   C(\"BRT\", \"BRT.txt lines 8349, 12015, 14248\", \"supports\", \"staora- occurs in 'pasvąmca staoranąmca' (V 2.25), 'pasvō staoraca' (V 5.39), 'drvō.staora- Adj. das Grossvieh gesund erhaltend' — 'Grossvieh'.\"),\n   C(\"POK\", \"p.1010 s.v. stā- / *steu-ro- (POK_full.txt line 81359)\", \"partial\", \"'to Old Indie sthūra- etc. stellt sich probably Indo Germanic steu-ro- bull (and anderes cattle): Avestan staora- cattle, Middle Persian stōr draft animal, steed, Gothic stiur m. bull calf, bull' — derived from *steu-ro-, not from *tauros.\"),\n   C(\"WLD\", \"Bd. II p.~610 s.v. stā- (WLD_Bd2_pages.txt line 40463)\", \"partial\", \"'idg. *steu-ro- Stier (und anderes Großvieh); av. staora- Großvieh, mp. stōr Zugtier, Roß ... Davon verschieden die zu *teu- schwellen zu stellende andere Bezeichnung des Stieres idg. *tauros'.\")\n ]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Persian\",\n \"words\": \"sotŭr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP sotūr/sutūr (ستور) 'beast of burden, horse, cattle' (Sa'di's verse on the chart) < MP stōr [stwr] 'horse, mount; large cattle' < Av. staora- / OIr. *staura-; the initial cluster st- received a prothetic vowel in NP (s(u)tūr, also ustūr), and MP ō from OIr. *au became NP ū. Wiktionary notes it is a doublet of the Arabic loan ثور (sowr) only in the loose sense of both meaning 'bovine'. The descent from Avestan is certain; only the ultimate link to *tauros is debated (#16).\",\n \"derivation_fa\": \"«ستور» (چارپای بارکش، اسب، گاو) از فارسی میانه stōr «اسب، مرکب، چارپای بزرگ» و اوستایی staora- است؛ در فارسی نو پیش از خوشهٔ آغازین st- واکه‌ای افزوده شده (سُتور، اُستور) و ō فارسی میانه به ū بدل شده است. معین در حاشیهٔ برهان و هرن همین را آورده‌اند. ادعای نورایی درست است.\",\n \"sources\": [W + \"ستور\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1102\", \"status\": \"supports\", \"note\": \"Borhan s.v. ستور (BQT_v2_pages.txt ~line 33770, pdf page 593): 'ستور ... جانور چارپا را عموماً و اسب و استر و خر'; Mo'in: 'پهلوی stōr (اسب)، اوستا staora- (بارتولمه ۱۵۹۰) ... (بار اسب، بار ورزاو)، استی ... (حیوان خانگی)، کردی زازا ...، شغنی ... (حیوان بارکش)'.\"},\n   {\"ref\": \"HRN:152\", \"status\": \"supports\", \"note\": \"Horn p.152 no. 720 (HRN.txt line 6301): 'sutōr, ustōr Ross ... aw. staora- Zugtier; phlv. stōr Zugtier, aber auch Ross ... skr. sthaurin Lastpferd, Lastochs; got. stiur Stier'.\"}\n ],\n \"consulted\": [\n   C(\"PHD\", \"MacKenzie (PHD_mackenzie.txt line 4687)\", \"supports\", \"'stōr [stwl, P ʾstwr, N sutōr] horse, mount; large cattle'.\"),\n   C(\"POK\", \"p.1010\", \"supports\", \"'Avestan staora- cattle, Middle Persian stōr draft animal, steed'.\"),\n   C(\"ARY\", \"Latin index pdf page 348\", \"supports\", \"STOR (Pahlavi), STAORA- (Avestan), ASTOR (Kurdish) grouped with TAUROS/TAURUS/STEER.\")\n ]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"Arabic\",\n \"words\": \"thwr\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Arabic ṯawr (ثور) 'bull, ox' is an inherited Semitic word: Proto-Semitic *ṯawr- > Hebrew šōr, Aramaic tōr(ā), Akkadian šūru, Ge'ez sor (Arabic keeps the interdental ṯ). Nobody derives it from Indo-European; the debate runs the other way — Klein (Nourai's own KLN reference) and many others consider Greek/Latin tauros/taurus 'prob. of Semitic origin', Pokorny leaves both directions open, and Wiktionary says borrowed from or into Proto-Semitic or from a common unknown source. An arrow 'IE *tauro- → Arabic ṯwr' therefore reverses the more widely held direction; at most the two are an ancient Wanderwort pair.\",\n \"derivation_fa\": \"عربی «ثَوْر» (گاو نر) واژهٔ موروثی سامی است: سامی آغازین *ṯawr- که در عبری šōr، آرامی tōrā و اکدی šūru شده و عربی ث (ṯ) میان‌دندانی را نگه داشته است. هیچ پژوهشگری آن را از هندواروپایی نمی‌گیرد؛ بلکه کلاین (همان مأخذ نورایی) و بسیاری دیگر taurus لاتین و tauros یونانی را «احتمالاً سامی‌الاصل» می‌دانند و ویکی‌واژه می‌گوید یا یکی از دیگری گرفته شده یا هر دو از زبانی ناشناخته‌اند. بنابراین جهت پیکان نورایی (از هندواروپایی به عربی) را پژوهش امروزی نمی‌پذیرد.\",\n \"sources\": [W + \"ثور\", U_TAWROS],\n \"ref_check\": [\n   {\"ref\": \"POK:1083\", \"status\": \"partial\", \"note\": \"Pokorny p.1083: '... or because of orientalischen Stierkultes with Proto Semitic *tauru (arab. ṯwr) connected' — mentions the Arabic word but does not say Arabic comes from IE.\"},\n   {\"ref\": \"KLN:1509\", \"status\": \"contradicts\", \"note\": \"Klein s.v. Taurus (KLN_1966.txt line 38297; vol. II p.~1509): 'L. taurus, bull, cogn. with Gk. ταῦρος ...; prob. of Sem. origin. Cp. Aram. tōrā, ox, bull, steer, Heb. shōr, Akkad. shūru, Arab. thōr, Ethiop. sōr' — Klein makes the IE word Semitic, the opposite of the chart's arrow.\"}\n ],\n \"consulted\": [\n   C(\"WLD\", \"Bd. I p.711 s.v. teu-\", \"partial\", \"'... Übereinstimmung mit ursemit. tauru (aram. tōr, hebr. šōr) durch Entlehnung ins Semitische, nicht umgekehrt (nach J. Schmidt aaO., Lewy Fremdw. 4) durch solche aus dem Sem. ins Idg.' — both directions argued in the literature.\"),\n   C(\"KLN\", \"1966 s.v. steer n. (line 36689)\", \"contradicts\", \"'All these words are prob. borrowed — directly or indirectly — from the Sem. languages. Cp. Aram. tōr, Heb. shōr'.\"),\n   C(\"AFM\", \"grep 'ثور' in AFM.txt\", \"silent\", \"Addi Shir lists Persian loans in Arabic; ثور is not among them (it is native Arabic).\")\n ]\n})\n\nnodes.append({\n \"id\": 19, \"lang\": \"Persian\",\n \"words\": \"sowr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian sowr (ثور; Classical sawr, Dari säwr) 'bull' and above all 'Taurus, the second zodiac sign' (and in Afghanistan the second solar month, cf. the 1978 Saur Revolution) is a learned loan from Arabic ṯawr; Persian pronounces Arabic ṯ as s. Mo'in tags it [ع.]. The edge Arabic → Persian is correct.\",\n \"derivation_fa\": \"«ثور» در فارسی (تلفظ ایرانی sowr، کلاسیک sawr) به معنای «گاو نر» و بیشتر «برج ثور، دومین برج فلکی» (و در افغانستان ماه دوم سال خورشیدی) وام‌واژهٔ عربی است و «ث» عربی در فارسی «س» خوانده می‌شود. معین آن را [ع.] نشان داده است. این پیکان درست است.\",\n \"sources\": [W + \"ثور\", \"https://vajehyab.com/moein/ثور\"],\n \"ref_check\": [{\"ref\": \"BQT:550\", \"status\": \"not_found\", \"note\": \"Borhan vol.1/2 OCR (BQT_v1_pages.txt, BQT_v2_pages.txt) searched for the headword ثور with the usual 'بفتح/بر وزن' pattern; no hit (only occurrences inside other entries, e.g. 'برج ثور'). No scan of printed p.550 available to ref_page.py.\"}],\n \"consulted\": [\n   C(\"MON\", \"vajehyab.com/moein/ثور\", \"supports\", \"'(ثَ) [ع.] (اِ.) ۱- گاو نر. ۲- نام یکی از صورت‌های فلکی و دومین برج'.\"),\n   C(\"KLN\", \"1966 s.v. Taurus\", \"supports\", \"'Arab. thōr' cited as the Arabic word for bull.\")\n ]\n})\n\nnodes.append({\n \"id\": 20, \"lang\": \"Latin\",\n \"words\": \"taurus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin taurus 'bull' is the regular Italic continuant of *táwros (Oscan ταυρομ, Umbrian turuf), not a loan from Greek (Watkins' '>' notwithstanding); whether *táwros itself is ultimately Semitic is the open question discussed at #15.\",\n \"derivation_fa\": \"لاتین taurus «گاو نر» دنبالهٔ عادی *táwros در زبان‌های ایتالیک است (اسکی ταυρομ، اومبری turuf) و از یونانی وام گرفته نشده است؛ اینکه خود *táwros در اصل سامی است یا نه، همان پرسش گشوده‌ای است که در بالا گفته شد. ادعای نورایی درست است.\",\n \"sources\": [U_TAWROS],\n \"ref_check\": [{\"ref\": \"POK:1083\", \"status\": \"supports\", \"note\": \"Pokorny p.1083: 'gr. ταῦρος, alb. tarok, Latin taurus, Oscan ταυρομ, Umbrian turuf, toru tauros'.\"}],\n \"consulted\": [\n   C(\"KLN\", \"1966 s.v. Taurus\", \"supports\", \"'L. taurus, bull, cogn. with Gk. ταῦρος, OSlav. turŭ'.\"),\n   C(\"LAT\", \"grep 'taurus' in LAT.txt (Ernout-Meillet)\", \"silent\", \"not quoted; Ernout-Meillet discuss the same Mediterranean/Semitic comparison.\"),\n   C(\"WLD\", \"Bd. I p.711\", \"supports\", \"'lat. taurus Stier, osk. ταυρομ, umbr. toru turuf'.\")\n ]\n})\n\nnodes.append({\n \"id\": 21, \"lang\": \"English\",\n \"words\": \"Taurus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English Taurus, the constellation and second zodiac sign (Old English already used Latin Taurus in astronomical texts; general use from the 14th c., Chaucer), is borrowed directly from Latin taurus 'bull', a calque of Greek Taûros (Ptolemy).\",\n \"derivation_fa\": \"انگلیسی Taurus (صورت فلکی و برج ثور) مستقیماً از لاتین taurus «گاو نر» گرفته شده که خود برگردان یونانی Taûros است؛ از سدهٔ ۱۴ (چاسر) رایج شد. درست است.\",\n \"sources\": [U_TAWROS],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; Klein s.v. Taurus covers it.\"}],\n \"consulted\": [\n   C(\"KLN\", \"1966 s.v. Taurus (line 38297)\", \"supports\", \"'Taurus, n., 1) a constellation, containing the Pleiades and Hyades; 2) one of the signs of the zodiac — L. taurus, bull'.\"),\n   C(\"AHD\", \"Watkins index (line 2342)\", \"supports\", \"'Taurus tauro-'.\")\n ]\n})\n\nnodes.append({\n \"id\": 22, \"lang\": \"Germanic\",\n \"words\": \"situraz\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"situraz\",\n \"correct_form\": \"*steuraz\",\n \"derivation\": \"The book prints 'situraz' (the JSON is faithful); no such Germanic form exists — this is Nourai's misprint for Proto-Germanic *steuraz (Gothic stiur, OE stēor, OHG stior, ON stjórr 'bull, steer'), probably a garbled *stiuraz. *steuraz is from *steu-ro- 'stout, large animal' per Pokorny/Watkins (Watkins: 'Suffixed form *steu-ro-, a larger domestic animal, in Germanic *steuraz, ox'), or, per the s-mobile view, from *(s)táwros; Kroonen prefers a substrate loan shared with *þeuraz. Gloss 'ox' is right.\",\n \"derivation_fa\": \"کتاب «situraz» چاپ کرده (استخراج درست است) ولی چنین صورتی در ژرمنی نیست؛ این خطای چاپی کتاب به جای ژرمنی آغازین *steuraz «گاو نر، ورزاو» است (گوتی stiur، انگلیسی باستان stēor، آلمانی کهن stior). پوکورنی و واتکینز آن را از *steu-ro- «جانور ستبر و بزرگ» و ویکی‌واژه از *(s)táwros می‌دانند و کرونن آن را وام از زبانی زیرلایه‌ای می‌شمارد. معنای «ورزاو» درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Germanic/steuraz\", U_TAWROS],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. stā- VIII.3 (AHD_watkins1985.txt line 999): 'Suffixed form *steu-ro-, a larger domestic animal, in Germanic *steuraz, ox, in Old English stēor, steer: STEER' — gives *steuraz, not 'situraz'; Watkins puts it under stā-, not tauro-.\"}],\n \"consulted\": [\n   C(\"POK\", \"p.1010 (POK_full.txt line 81362)\", \"supports\", \"'Gothic stiur m. bull calf, bull ...; Old High German stior, Old English stēor, Old Icelandic stjōrr (besides þjórr) bull'.\"),\n   C(\"KLN\", \"1966 s.v. steer n. (line 36689)\", \"partial\", \"'OE. steor, rel. to OS. stior, ON. stjorr, þjorr ... Goth. stiur, bull, and cogn. with Gk. ταῦρος, L. taurus ... prob. borrowed ... from the Sem. languages'.\"),\n   C(\"WLD\", \"Bd. II s.v. stā- (WLD_Bd2_pages.txt line 40463)\", \"supports\", \"'got. stiur- n. m. Stierkalb, Stier ... ahd. stior, ags. stēor, aisl. stiórr Stier'.\")\n ]\n})\n\nnodes.append({\n \"id\": 23, \"lang\": \"English\",\n \"words\": \"steer\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English steer 'young (castrated) ox' < Middle English steer, steor < Old English stēor, the regular reflex of Proto-Germanic *steuraz (eu > OE ēo). It is unrelated to the verb steer 'to guide' (OE stīeran), although both may ultimately go back to *steu- 'stout, upright' in Watkins' and Klein's view.\",\n \"derivation_fa\": \"انگلیسی steer «گوسالهٔ نر اخته، ورزاو جوان» از انگلیسی میانه steer و انگلیسی باستان stēor از ژرمنی آغازین *steuraz است (eu ژرمنی در انگلیسی باستان ēo شده). این واژه با فعل steer «راندن، هدایت کردن» یکی نیست. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Germanic/steuraz\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; AHD stā- (STEER²) and Klein s.v. steer cover it.\"}],\n \"consulted\": [\n   C(\"KLN\", \"1966 s.v. steer n. (line 36689)\", \"supports\", \"'steer, n., a young ox. — ME., fr. OE. steor'.\"),\n   C(\"AHD\", \"Watkins s.v. stā- VIII.3\", \"supports\", \"'Germanic *steuraz, ox, in Old English stēor, steer: STEER²'.\"),\n   C(\"ARY\", \"Latin index pdf page 348\", \"supports\", \"'SKEAT: (STEER) 601 ... STEER (ENGLISH)' in the Tauro group.\")\n ]\n})\n\nfor n in nodes:\n    n.pop(\"quote_note\", None)\n\nentries.append({\n \"entry\": 0,\n \"root\": \"Tĕu 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *tewh₂- (*teuə-) 'to swell; become strong, fat' (Pokorny teu-, teuə-, tuə-, tū- 1080-1085; Watkins teuə-)\",\n \"note\": \"Root, label and gloss are correct: Pokorny IEW pp.1080-1085 'teu-, teuə-, tuə-, tū- to swell; crowd, folk; fat; strong' and Watkins 'teuə- To swell' (Nourai's POK:1082 falls inside this entry). The Latin, Greek, Germanic and English branches are Pokorny's and Watkins' own lists. Problems lie in the Iranian part: the Avestan box mixes the real tav- 'be able' with reconstructions ('tavant' fast = Horn's starred *tavant-, 'tum-âspa' = Pokorny's *Tumāspa-, 'us-tavah' = Nyberg's *us-tavah-); Persian tond belongs to *(s)teud- 'thrust' (Cheung, Hübschmann), Tahmāsb to tahm 'brave' < Av. taxma- (Nyberg, Wiktionary), and sotūh/nastūh are derived by Cheung from *staup- 'overcome' (Nyberg/Mo'in support Nourai). tūbre 'bag' rests only on Mann. The sub-roots Teuk (Pokorny's 'perhaps') and Tauro (Pokorny's one option; Watkins: from stā-; Wiktionary/Klein: Semitic or unknown source) are attached to Tĕu more confidently than the sources allow; the Arabic ṯawr is native Semitic, not derived from IE. Book misprint: 'situraz' for Gmc. *steuraz. No extraction errors: the JSON matches the printed page (the Old Persian taumâ box points to an empty box in the book).\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *tewh₂- (در نگارش پوکورنی teu-، teuə-) به معنای «باد کردن، ورم کردن؛ نیرومند و فربه شدن» است (پوکورنی ۱۰۸۰–۱۰۸۵، واتکینز teuə-)؛ پس ریشه و معنای نورایی درست است و شاخه‌های لاتین (tumēre، tūber)، یونانی (tūrós)، ژرمنی و انگلیسی (thumb، thousand، thigh) همه پذیرفته‌اند. اشکال‌ها در بخش ایرانی است: از واژه‌های فارسی تنها «توان» بی‌گمان از این ریشه است؛ «تند» از ریشهٔ دیگری (*tund-/*(s)teud- «کوبیدن») است، «تهماسب» از «تهم» (دلیر) + «اسب» است، و «ستوه/نستوه» را نیبرگ و معین از *us-tavah- ولی چونگ از *staup- «شکست دادن» می‌داند. «ثور» عربی واژهٔ سامی است نه هندواروپایی، و پیوند Tauro و Teuk با این ریشه تنها یکی از احتمال‌هاست. «situraz» خطای چاپی کتاب به جای *steuraz است؛ خطای استخراج دیده نشد.\",\n \"sources\": [U_TEWH, U_TAWROS],\n \"ref_check\": [POK_TEU],\n \"consulted\": [\n   WLD_TEU | {\"note\": \"Walde-Pokorny Bd. I 706 ff. 'teu- schwellen': ai. tavīti, tavas-; av. tav- vermögen, tavah- Macht, Kraft; ap. tauman- (WLD_Bd1_pages.txt line ~66630-66645).\"},\n   AHD_TEU,\n   C(\"IEC\", \"s.v. tumo / tumos (IEC.txt lines 19300-19301)\", \"supports\", \"'tumo, eiō swell ... WP I, 708 Skt. cf. túmrah swollen; Per. cf. tuman myriad; ... Lat. tumeo'.\"),\n   KLN_TUMID\n ],\n \"nodes\": nodes\n})\n\nout = {\"pdf_page\": 507, \"book_page\": 477, \"verified_by\": \"claude-opus-5.5\", \"verified_on\": \"2026-10-14\", \"entries\": entries}\nwith open(\"/home/sfmqrb/git/rishe-private/data/verification/page-507.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"ok\")\n"
}
```


### [2026-10-15T02:54:38.513Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-507.py (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:54:46.728Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'E'\np='build-507.py'; s=open(p).read()\ns=s.replace('C(\"HUB\", \"p.? (HUB.txt line 8988)\"','C(\"HUB\", \"Persische Studien (HUB.txt line 8988)\"')\ns=s.replace('\"col. 638-639 s.v. tav-, tavah- (BRT.txt lines 12015, 12029)\"','\"s.v. tav-, tavah-, tumāspana- (BRT.txt lines 12015, 12029, 12327)\"')\ns=s.replace('\"p.186 s.v. tav- (KNT_full.txt line 25986)\"','\"lexicon s.v. tav- (KNT_full.txt line 25986)\"')\ns=s.replace(\"(Nourai's 387 is a page number near this entry)\",\"(found by grep; how Nourai's '387' maps onto Gharib's page/entry numbering was not established)\")\ns=s.replace('\"col. 623 (BRT.txt line 11787 \\'Bthl. Wb. 623f.\\' cited by WLD)\"','\"s.v. taoxman- (BRT.txt line 11787; WLD cites \\'Bthl. Wb. 623f.\\' for taumā)\"')\nopen(p,'w').write(s)\nE\npython3 build-507.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-507.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 507"
}
```


### [2026-10-15T02:54:47.353Z] TOOL RESULT

```
ok
nodes verified: 23/23
node verdicts: {'disputed': 3, 'plausible': 5, 'confirmed': 14, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 8, 'supports': 20, 'not_checked': 5, 'not_found': 2, 'contradicts': 1}
books consulted: {'supports': 44, 'partial': 9, 'contradicts': 4, 'silent': 12} | by book: {'KLN': 13, 'WLD': 8, 'POK': 7, 'AHD': 5, 'ARY': 5, 'BRT': 4, 'PHD': 4, 'NYB': 3, 'HRN': 3, 'CHEUNG': 2, 'KNT': 2, 'HUB': 2, 'MON': 2, 'IEC': 2, 'BQT': 1, 'LEW': 1, 'SKT': 1, 'SYN': 1, 'SOD': 1, 'AFM': 1, 'LAT': 1}
```


## [2026-10-15T02:54:50.768Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^ *tumour\\|tumour, s\" SKT.txt | head -2 | cut -c1-200; grep -n \"tuber\" LEW_1910.txt | head -2 | cut -c1-200; grep -n -i \"thousand\" SYN.txt | head -3 | cut -c1-200; grep -n \"taurus\" LAT.txt | head -2 | cut -c1-300; grep -c \"ثور\" AFM.txt"
}
```


### [2026-10-15T02:54:51.154Z] TOOL RESULT

```
79:remained virtually constant for thousands of years, as, for example, those for the numerals and for close family relationship like ‘father’, ‘mother’, etc. But such cases are the exception. Change 
128:possible and worth while. In announcing the project many years ago, in Language 5(1929).215 ff., it was proposed to collect and study about a thousand groups of synonyms. Actually the number in th
956:Words for ‘mountain’ and ‘hill’ are taken together because of their frequent relations and the fluctuating discrimina- tions. The application of NE hill may range from a height of several thousand
3117:laire, cf. neruus et veupov, et les articles paruus, taurus.
27388:d'une autre aanibre, taurus), Le noa latin du "bouc" est dvi 4 em*ent
6
```


## [2026-10-15T02:54:53.649Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^taurus\\|^ *taurus, -\" LAT.txt | head -3; grep -n -i \"Tumour\\b\" SKT.txt | head -2 | cut -c1-250; grep -n \"13\\.37\\|THOUSAND\" SYN.txt | head -3 | cut -c1-200; grep -n -o \".\\{40\\}ثور.\\{40\\}\" AFM.txt | head -6"
}
```


### [2026-10-15T02:54:54.025Z] TOOL RESULT

```
41273:taurus . Cea inversions semblent etre le fait dn vocabulaire "popn¬
63070:taurus
63111:taurus, -I m.: taureau. Nom d'une constellation du zodiaque.
688:Aneurism,  a  tumour  due  to  dilatation. (Gk.)  Gk.  iv^vpvcfta,  a  widening. —Gk. Av;  for  (li-u,  up;  and  tvpvrur,  to  widen, from  (L'piJr,  wide.
2024:Boil  (3),  «  tumour.  (E.)     Sec  ^'-'-
```


## [2026-10-15T02:54:55.632Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 63111,63125p LAT.txt | cut -c1-300; grep -n \"ثور\" AFM.txt | cut -c1-200 | head"
}
```


### [2026-10-15T02:54:55.990Z] TOOL RESULT

```
taurus, -I m.: taureau. Nom d'une constellation du zodiaque.
S'applique a des animaux ou a. des objets qui rappellent par 1 -eur
cri, leur aspect, etc., le taureau: butor (oiseau), Plin.10,116; frelon
(scarabee), Plin.30,3y; racine d'arbre (Quint.8,3,13). Designe aussi
le p 4 rinee (ou plus exactement les testicules?) dans une victime,
cf.F.373,31, atque harum hostiarum inuiolati sunt tauri quae pars
scilicet caeditur in castratione; et Diom., GLK I 450,8, et en gr.tautanus
1196 -
1 1 emploi de xccupog (Poli. 3,173). Pe taurus a et 4 cr 4 e un f 4 m. taura
dans la 1 . rustique (Varr., Coi.), cf. P.F.481,1, tauras uaccas steriles ...
quod non magis pariant quam tauri • Ancien (Enn.), usuel. Panroian.
M.L.O603.
Derives et composes: taureus ; taurinus; d'ou taurina: espece de
chaussure, cf. 4 dit de Diocletien, c. 9 taurinae muliebres bisoles,
monosoles, c. 10 taurinae inauratae, lanatae (CIL III P.O33), Pela-
1261:ي باب الله او ܒܒ حمل اي باب ييل وهو اسم إله عند المابلبين والاثور ين ٠‏ كا 
1888:* (الجمثورة 3 المجموع تعريب © الهري 
2439:( يري ) نبات وهو النثور الأصفر تعريب ܗ 
3007:* (الرشك» اكبيد اللحية معرب من ريشكاو: اي بليسة الثور 9 علل 
4782:* ( الفا ثور» الطسست او ` 0 ` فضَّة اوذهب وقرص 
7263:دسثور ="(
```


## [2026-10-15T02:54:57.351Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 63126,63135p LAT.txt | cut -c1-300"
}
```


### [2026-10-15T02:54:57.672Z] TOOL RESULT

```
gonius, cf.437, p.118,30 ed.Ihm: cortex uetustae taurinae ; taurulus;
tauri-fer,-fornis,-genus, tous poetiques, et faits sur des types
grecs, cf. xaupqxopcpoc Eur., Taupoyevqc Orph. - Cf. aussi suouetaurilia,
s ol(l)itaurilia.
taurobolium: sacrifice du taureau; transcription du gr. Tai)poj 3 oXi,ov,
d'ou ont 4 te derives taurobolior,-liatus,-linus (tardifs); taurocenta:
toreador (de *TOUpc»cevTT|C? ).
Les noms indo-europeens d'animaux domestiques ne sp 4 cifient pas
le sexe; comme ouis , lat. bos est masculin si l'on ne pense pas au
sexe, feminin si l'on pense a. la "vache". Le male n'avait pas de
```


## [2026-10-15T02:54:59.057Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 63136,63150p LAT.txt | cut -c1-300"
}
```


### [2026-10-15T02:54:59.382Z] TOOL RESULT

```
nom dans le vocabulaire noble de 1 1 indo~europeen (v.werres, aries),
Le vocalisme radical a montre que taurus appartient au vocabulaire
technique, de caractere populaire; le mot se retrouve dans osq. tou—
pop, "taurum", ombr. toru, turuf "tauros", gr.xaupoc. Le meme mot
designe un animal sauvage dans v.sl ,turu, lit .tauras "aurochs",
v.pr .tauris "bison". La forme diverge dans gaul. tarvos, iri. tarb
"taureau" (avec la meme alteration qu'offre lat. paruus en face de
gr.TOX.upoc) et dans got. stiur "taureau" (sans doute sous 1 'influence
d'une etymologie populaire; cf.av. siaora- "gros b 4 tail"). Le mot a
1 1 instabilite d'un terme populaire.
tautanus, ~I m.: mot glos 4 claua, cateia par Isid., Or. 18,7,7
qui 1 'attribue aux Gaulois et aux Ibures. V. Sofer, p.46,171.
tax: v. tuxtax.
taxa, -ae f.: sorte de fragon (Plin. 15,130). Cf. sans doute taxus.
taxea, -ae f.: lard. Mot gaulois d'apres Isid.Or.30,a,84, qui
```


## [2026-10-15T02:55:00.684Z] AGENT

Ernout-Meillet has a useful entry. Updating the unchecked "silent" notes with what I actually found.


## [2026-10-15T02:55:09.883Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'E'\np='build-507.py'; s=open(p).read()\nold_lat='C(\"LAT\", \"grep \\'taurus\\' in LAT.txt (Ernout-Meillet)\", \"silent\", \"not quoted; Ernout-Meillet discuss the same Mediterranean/Semitic comparison.\"),'\nnew_lat='C(\"LAT\", \"Ernout-Meillet s.v. taurus (LAT.txt line 63111-63145)\", \"partial\", \"\\'Le vocalisme radical a montré que taurus appartient au vocabulaire technique, de caractère populaire; le mot se retrouve dans osq. ταυρομ, ombr. toru, turuf, gr. ταῦρος ... got. stiur (sans doute sous l\\'influence d\\'une étymologie populaire; cf. av. staora- gros bétail). Le mot a l\\'instabilité d\\'un terme populaire\\' — inherited in Italic, no IE root given.\"),'\nassert old_lat in s; s=s.replace(old_lat,new_lat)\nold='C(\"LEW\", \"grep tumeo/tuber in LEW_1910.txt\", \"silent\", \"not consulted in detail; Walde-Hofmann II 712 ff. is cited by Pokorny for this group.\"),'\nassert old in s; s=s.replace(old,'')\nold='C(\"SKT\", \"grep \\'tumour\\' in SKT.txt\", \"silent\", \"Skeat lists tumour < Latin tumor < tumere (not quoted; Klein suffices).\")'\nassert old in s; s=s.replace(old,'C(\"SKT\", \"grep \\'Tumour\\' in SKT.txt\", \"silent\", \"no headword Tumour found in the OCR (only uses inside other entries, e.g. \\'Boil (3), a tumour\\', line 2024).\")')\nold='C(\"SYN\", \"Buck §13.37 \\'thousand\\'\", \"silent\", \"not quoted; Buck discusses the Germanic/Balto-Slavic \\'thousand\\' as \\'swollen hundred\\' (referenced by Pokorny/Watkins).\")'\nassert old in s; s=s.replace(old,'C(\"IEC\", \"s.v. tumos (IEC.txt line 19301)\", \"supports\", \"\\'tumos ... swell, lump, mass, myriad, crowd ... OE þūma (thumb)\\'.\")')\nold='C(\"AFM\", \"grep \\'ثور\\' in AFM.txt\", \"silent\", \"Addi Shir lists Persian loans in Arabic; ثور is not among them (it is native Arabic).\")'\nassert old in s; s=s.replace(old,'C(\"AFM\", \"grep \\'ثور\\' in AFM.txt\", \"silent\", \"Addi Shir (Persian loans in Arabic) has no entry for ثور \\'bull\\'; the word occurs only inside other entries (e.g. line 3007 \\'... الثور\\'), consistent with its being native Arabic.\")')\nopen(p,'w').write(s)\nE\npython3 build-507.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-507.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 507 | grep -c PROBLEM"
}
```


### [2026-10-15T02:55:10.471Z] TOOL RESULT

```
ok
0
```


## [2026-10-15T02:55:20.910Z] TOOL CALL #97: SubagentHandback

```json
{
 "message": "Page 507 (book p.477, root Tĕu 1) is done. I wrote /home/sfmqrb/git/rishe-private/data/verification/page-507.json. `verify_check.py 507` shows 23/23 nodes verified and 0 PROBLEM lines.\n\n**Verdicts:**\n- **Root:** 1 confirmed. Tĕu 1 is PIE *tewh₂- \"to swell, become strong\" (Pokorny pp.1080–1085, Watkins teuə-).\n- **Nodes:** 14 confirmed, 5 plausible, 3 disputed, 1 transcription_suspect.\n\n**Disputed:**\n- **#1 Avestan box:** only tav- \"be able\" is a real Avestan word. The rest are scholars' reconstructions, not attested words:\n  - \"tavant\" (fast) is Horn's starred *tavant-; the attested participle tuuant- means \"able\", not \"fast\".\n  - \"tum-âspa\" is Pokorny's *Tumāspa-, inferred from the patronymic tumāspana-.\n  - \"us-tavah\" / \"ni-us-tavah\" are Nyberg's and Mo'in's *us-tavah-.\n- **#2 Persian box:** tavân is confirmed. The other words have different origins:\n  - tond comes from MP tund < *tund-/PIE *(s)teud- \"thrust\" (Cheung, Wiktionary; Hübschmann already rejected the link to tavân).\n  - Tahmâsb is tahm \"brave\" (< Av. taxma-) + asp \"horse\" (Nyberg; Wiktionary rejects the Tumāspana link).\n  - sotūh/nastūh are contested. Nyberg and Mo'in (in his Borhan footnote) back *us-tavah-, but Cheung derives them from *staup- \"overcome\".\n- **#18 Arabic thwr:** Arabic ṯawr is native Proto-Semitic *ṯawr-. Klein, Nourai's own KLN:1509 citation, says the opposite of the chart: taurus is \"prob. of Sem. origin\".\n\n**Transcription suspect:**\n- **#22 Germanic \"situraz\":** this is a misprint in the book for *steuraz (Gothic stiur, OE stēor). The extraction is faithful. I copied the page image to data/verification/sources/refs/ocr/BOOK/507.png.\n\n**Plausible (main reasons):**\n- tūbreh rests only on Mann, who marks it \"ambig.\"; Wiktionary gives MP tōbrag as a widely borrowed word with no IE root.\n- Greek tumbos is listed by Watkins only as \"perhaps\"; Beekes treats it as a substrate word.\n- Teuk and Tauro are attached to Tĕu more confidently than the sources allow: Pokorny gives each only as one option, and Watkins puts tauro- under stā-.\n- Avestan staora is a real word, but Pokorny and Walde-Pokorny derive it from *steu-ro- rather than from *tauros.\n\n**Extraction errors:** none. The JSON matches the printed page, including the empty box beside Old Persian taumâ.\n\nAll 20 web sources I cited were archived with fetch_source.py. Two of Nourai's references could not be confirmed: BQT:550 (no headword found in the OCR, no scan available) and HID:211 (taumā is not on that page)."
}
```


### [2026-10-15T02:55:21.344Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
